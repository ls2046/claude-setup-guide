# Claude 开通与使用全流程

把 Claude 的网络准备、邮箱注册、订阅支付、KYC、权益异常和退款申诉整理成一套可以交给 Codex 执行的流程。网络支持 **独立 VPS** 和 **机场加静态 IP** 两种方案；从你当前卡住的步骤继续处理。

## 从这里开始

| 你要做什么 | 入口 |
| --- | --- |
| 按步骤了解网络、注册、订阅、KYC 和退款经历 | [完整教程](docs/claude-guide.md) |
| 让 Codex 配置网络或处理当前问题 | [可复制的操作提示词](docs/prompts.md) |
| 安装或查看 Claude 专属 skill | [SKILL.md](skills/claude-setup-guide/SKILL.md) |

教程记录个人经历；skill 根据实际页面和当前规则处理问题。身份核验由本人完成，支付与退款按具体授权和当前工具规则执行。IP 风险评分与网络速度分开检查。

## 如何使用 skill

1. 下载或克隆本仓库：

   ```bash
   git clone https://github.com/ls2046/claude-setup-guide.git
   ```

2. 把仓库内完整的 `skills/claude-setup-guide` 文件夹放到 Codex 的技能目录（默认 `~/.codex/skills/`；设置过 `CODEX_HOME` 时使用其下的 `skills/`）。如果已经有同名 skill，先比较并备份，保留自己的修改。
3. 在 Codex 新会话里调用 `$claude-setup-guide`，再粘贴 [提示词](docs/prompts.md) 中对应的任务。也可以让有本地文件操作能力的 Codex 帮你完成下载、安装与检查。
4. 准备好本地连接资料。需要设备授权或身份验证时自行完成，其余让 Codex 检查、配置并测试。

skill 不会自行提供机场、静态代理或 VPS。只做检查时不会改配置；部署前先备份并验证候选，保留当前网络与管理连接。

旧版本使用 `claude-network-setup` 名称。升级时先备份旧 skill 中的个人修改，再安装新目录并移走旧目录，避免重复调用。GitHub 旧仓库链接会重定向，后续请使用新名称。

## 电脑与手机

- **电脑**：检查系统代理、TUN、当前活动配置、真实规则命中和最终出口。
- **iPhone**：通过 Mac 的 iPhone 镜像操作，手机保持锁定；使用具备电脑操作能力的会话。
- **Android**：USB 调试授权后通过 ADB 或 scrcpy 操作；核对设备序列号、活动配置与 VPN 状态。
- **Claude Code**：检查终端和进程实际使用的代理，不能用浏览器打开网页代替验证。

## skill 的参考资料

- [流程判断与常见问题](skills/claude-setup-guide/references/workflow.md)
- [邮箱、注册与登录](skills/claude-setup-guide/references/account-registration.md)
- [订阅、地区、支付与权益](skills/claude-setup-guide/references/subscription-payments.md)
- [KYC 与账号申诉](skills/claude-setup-guide/references/identity-support.md)
- [退款、复核、进度与取消续费](skills/claude-setup-guide/references/refunds.md)

- [自建 VPS](skills/claude-setup-guide/references/vps.md)
- [机场加静态出口](skills/claude-setup-guide/references/static-chain.md)
- [网络与环境验收](skills/claude-setup-guide/references/verification.md)
- [手机与远程设备](skills/claude-setup-guide/references/devices.md)
- [Claude 访问和支付页面排障](skills/claude-setup-guide/references/app-troubleshooting.md)
- [经验与证据边界](skills/claude-setup-guide/references/session-lessons.md)

## 短请求对照工具

仓库附有只读探针，要求 Python 3 和 curl：

```bash
python3 skills/claude-setup-guide/scripts/probe_routes.py --help
```

它通过已经存在的本地代理监听端口进行短请求对照，不会启动代理或修改系统设置，也不能代替浏览器泄露测试、Claude 聊天和订阅验收。用法见 [检测与验收](skills/claude-setup-guide/references/verification.md)，示例命令在 skill 目录内执行。

## 分享问题

可以提交脱敏后的报错、客户端版本和复现步骤。不要上传代理密码、机场订阅链接、SSH 私钥、Cookie、验证码、支付资料或原始私有配置。

## AI 技术讨论群

欢迎扫码加入微信群，交流 Claude 开通、网络配置和 AI 工具使用经验。

<img src="assets/ai-tech-wechat-group.jpg" alt="AI 技术讨论群微信二维码" width="360" />

二维码有效期以图片提示为准：**11 月 30 日前有效**。过期后请查看本页更新。
