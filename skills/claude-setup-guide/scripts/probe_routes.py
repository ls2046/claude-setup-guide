#!/usr/bin/env python3
"""Read-only HTTP comparison through existing loopback proxy listeners."""
import argparse
import json
import math
import os
from pathlib import Path
import statistics
import subprocess
import time
from urllib.parse import urlsplit


def route(value):
    try:
        label, address = value.split('=', 1)
        u = urlsplit(address)
        if (not label or not label.replace('-', '').replace('_', '').isalnum()
                or u.scheme not in ('http', 'https', 'socks5h')
                or u.hostname not in ('127.0.0.1', 'localhost', '::1')
                or not u.port or u.username or u.password or u.query or u.fragment
                or u.path not in ('', '/')):
            raise ValueError()
    except ValueError:
        raise argparse.ArgumentTypeError('Use label=http://127.0.0.1:PORT; no credentials')
    return label, address


def public_target(value):
    u = urlsplit(value)
    if (u.scheme != 'https' or not u.hostname or u.username or u.password
            or u.query or u.fragment or any(c.isspace() for c in value)):
        raise argparse.ArgumentTypeError('Use a public HTTPS endpoint without credentials/query/fragment')
    return value


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--route', type=route, action='append', required=True)
    ap.add_argument('--url', type=public_target, action='append', required=True)
    ap.add_argument('--rounds', type=int, default=3)
    ap.add_argument('--interval', type=float, default=1)
    ap.add_argument('--timeout', type=float, default=15)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if not (1 <= args.rounds <= 60 and 0 <= args.interval <= 60 and 1 <= args.timeout <= 60):
        ap.error('rounds 1..60, interval 0..60, timeout 1..60')
    if len({r[0] for r in args.route}) != len(args.route):
        ap.error('Route labels must be unique')
    # Reserve a new private output; never overwrite prior evidence.
    fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    results = []
    report = {'scope': 'HTTP endpoint probe only; not model generation or leak test',
              'results': results, 'summary': [], 'complete': False}
    metrics = '%{http_code}\t%{time_namelookup}\t%{time_connect}\t%{time_appconnect}\t%{time_starttransfer}\t%{time_total}\t%{size_download}\t%{remote_ip}'
    try:
        for n in range(args.rounds):
            for label, address in args.route:
                for url in args.url:
                    cmd = ['curl', '-q', '--silent', '--show-error', '--proxy', address,
                           '--noproxy', '', '--connect-timeout', str(min(8, args.timeout)),
                           '--max-time', str(args.timeout), '--max-filesize', '1048576',
                           '--output', os.devnull, '--write-out', metrics, '--url', url]
                    row = {'round': n + 1, 'route': label, 'url': url,
                           'timestamp_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
                    try:
                        r = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout + 3)
                        row['curl_exit'] = r.returncode
                        values = r.stdout.rstrip('\r\n').split('\t')
                        if len(values) == 8:
                            row.update(zip(['status', 'dns_s', 'connect_s', 'tls_s', 'ttfb_s',
                                            'total_s', 'bytes', 'remote_ip'], values))
                            for key in ['dns_s', 'connect_s', 'tls_s', 'ttfb_s', 'total_s', 'bytes']:
                                row[key] = float(row[key])
                            row['status'] = int(row['status'])
                        row['http_success'] = r.returncode == 0 and 200 <= row.get('status', 0) < 300
                    except subprocess.TimeoutExpired:
                        row.update(curl_exit=None, http_success=False, error='process_timeout')
                    results.append(row)
                    print(json.dumps(row, ensure_ascii=False), flush=True)
                    if args.interval:
                        time.sleep(args.interval)
        for label, _ in args.route:
            for url in args.url:
                rows = [r for r in results if r['route'] == label and r['url'] == url]
                durations = sorted(r['total_s'] for r in rows if r['http_success'])
                report['summary'].append({'route': label, 'url': url, 'attempts': len(rows),
                    'successes': len(durations),
                    'median_success_s': statistics.median(durations) if durations else None,
                    'p95_success_s': durations[math.ceil(len(durations) * .95) - 1] if durations else None})
        report['complete'] = True
    finally:
        with os.fdopen(fd, 'w') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            f.write('\n')
    print(json.dumps(report['summary'], ensure_ascii=False))


if __name__ == '__main__':
    main()
