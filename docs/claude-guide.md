自从Claude加强封控以来，就开始折腾Claude开通，学习了不少文章，总结了自己的经验：

这段时间，从自建 VPS 到机场加静态 IP，从电脑到手机，再到注册、订阅和 KYC，我把整个流程都折腾了一遍。中间遇到过网络卡顿、支付页面打不开，也遇到过钱扣了，会员却没开通。

这篇就按我的操作顺序，带大家从准备网络开始，一步步完成注册和订阅。

**先记住一件事：网络没有稳定之前，不要急着注册，更不要急着付款。**

## 第一步：准备网络，让 Codex 直接配置

网络准备这一步，我给大家两个建议：

- **不差钱：买独立 VPS，让 Codex 帮你部署代理。**
- **想省钱：选机场加静态 IP，让 Codex 接到现有机场上。**

**我个人更推荐静态 IP 方案，主要就是比较便宜。** 尤其是已经有机场的，再补一个静态代理就能搭起来。

配置文件、节点和分流规则这些细节，交给 Codex 处理。我会在电脑上的 Codex 里打开一个本地项目，把连接资料准备好，让它检查现状、备份配置、完成部署和测试。

完整教程、Claude 专属 skill 和可复制的配置提示词统一从这里获取：[GitHub 教程与 skill](https://github.com/ls2046/claude-network-setup)。按自己选择的方案使用对应提示词即可。

### 经济方案：机场加静态 IP（我更推荐）

我使用的是 [Webshare](https://www.webshare.io/) 的静态代理，原来的机场继续保留。连接顺序是：

**电脑或手机 → 机场节点 → 静态代理 → Claude。**

机场负责中转，静态代理负责最终出口。以后机场节点慢了，可以让 Codex 换中转，同时保留原来的静态出口。

自己只需要准备两样东西：一个目前能正常使用的机场，以及买好的静态代理。把静态代理的地址、端口、协议、用户名和密码保存在本地文件里，再把文件路径告诉 Codex；已有机场配置让它直接检查，不用重新抄一遍。

准备好资料后，使用上面 GitHub 教程里的“机场加静态 IP”提示词，让 Codex 直接完成配置和检测。

如果连接资料不好整理，也可以把供应商提供的代理配置保存到本地，让 Codex 从里面读取。我自己只负责购买、必要的授权和最终核对，剩下的配置交给它处理。

### 预算充足：独立 VPS 自建代理

选择这套方案，就先购买一台目标地区、带独立公网 IP 的 VPS，准备好 SSH 连接地址、端口、用户名和本机密钥路径。服务器部署和客户端导入，同样交给 Codex。

准备好后，使用 GitHub 教程里的“独立 VPS”提示词，让 Codex 部署服务、导入节点，并完成联网检测。

电脑配置好以后，再按下一步连接手机，让 Codex 把同一个固定出口配置到手机上。

## 第二步：连接手机，检查电脑和手机的网络

电脑配置完成后，我会把手机也交给 Codex 配置，再分别检查两台设备的实际结果。配置提示词里已经包含检测要求，下面说明手机怎么连接，以及我要看哪些结果。

检测入口是 [Net.Coffee Claude 网络检测](https://ip.net.coffee/claude/)。只使用电脑的，可以跳过手机连接部分。

### 1. 先连接手机，让 Codex 配置和检测

iPhone 用 Mac 的“iPhone 镜像”，安卓用 ADB 或 scrcpy 投屏。连接好以后，让 Codex 接着导入配置、打开检测页并读取结果。

**iPhone：打开 Mac 的“iPhone 镜像”**

1. 准备支持 iPhone 镜像的 Mac 和 iPhone，两台设备登录同一个开启双重认证的 Apple 账户，并打开 Wi-Fi 和蓝牙。
2. 在 Mac 上打开“iPhone 镜像”，第一次使用时，按提示完成配对和验证。
3. 把 iPhone 放在 Mac 附近并锁屏，等电脑里的镜像窗口显示手机画面。
4. 在具有电脑操作能力的 Codex 会话里，让它通过这个窗口操作手机。连接要求可以对照 [Apple 的镜像说明](https://support.apple.com/120421)。

镜像连接成功后，使用 GitHub 教程里的“iPhone 镜像配置与检测”提示词，让 Codex 接着操作。

如果镜像提示“iPhone 正在使用”，就把手机重新锁屏。如果需要在手机上输入密码、验证码或完成面容验证，我会拿起手机自行处理，完成后锁屏，让 Codex 接着操作。

**安卓：开启 USB 调试，使用 ADB 或投屏窗口**

1. 用支持数据传输的 USB 线连接电脑和手机，先解锁手机。
2. 在手机设置中找到“关于手机”，通常连续点击“版本号”七次，开启开发者选项；不同品牌的入口可能略有区别。
3. 进入开发者选项，打开“USB 调试”。手机弹出授权时，核对是自己的电脑，再点击“允许”。
4. 让 Codex 检查电脑是否已经安装 [Android Platform Tools 中的 ADB](https://developer.android.com/tools/adb)，没有就先安装。
5. 让它运行 `adb devices -l`。设备状态显示 `device` 才是已连接、已授权；显示 `unauthorized` 就回手机完成授权，列表为空则先检查数据线和连接。
6. 连接成功后，可以明确授权 Codex 使用 ADB 操作这台手机。如果想在电脑上看到手机画面，再打开 [scrcpy 安卓投屏](https://github.com/Genymobile/scrcpy)，让 Codex 通过投屏窗口操作。

scrcpy 的常规 USB 投屏也依赖 ADB，前面的 USB 调试和授权步骤同样要完成。电脑只连接一台安卓设备时，安装好后运行 `scrcpy` 就能打开投屏；连接多台设备时，先让 Codex 核对目标手机的型号和序列号。

连接并授权后，使用 GitHub 教程里的“安卓 ADB / scrcpy 配置与检测”提示词，让 Codex 接着配置手机网络。

**连接好以后，确认手机自己的代理已启动**

镜像和 ADB 只是操作手机的方式，不会自动让手机使用电脑的代理。手机自己的代理客户端仍然要启动 VPN，并选中正确配置。

接下来，让 Codex 在电脑和手机上分别打开检测页，按下面三项核对结果。手机切换网络、更新订阅，以及正式付款前，我也会再确认一次代理是否正常。

### 2. 核对电脑和手机的出口 IP

让 Codex 读取页面里的“Claude 出口 IP”，确认电脑和手机都使用了预期的固定出口。

页面还有一个“中国出口 IPv4”。如果国内网站设置了直连，这里显示国内运营商地址是正常的。重点是 Claude 的请求有没有走对线路。拿不准时，让 Codex 查客户端的连接记录，确认 Claude 请求实际用了哪个节点。

### 3. 检查 DNS、WebRTC 和 IPv6

继续往下看 DNS、WebRTC 等检测结果，也可以打开 [BrowserLeaks](https://browserleaks.com/) 交叉检查。

我会重点确认：DNS 有没有意外走本地运营商，WebRTC 有没有暴露直连公网地址，IPv6 有没有绕过代理。如果发现绕行，就让 Codex 继续排查客户端的 DNS 接管和 IPv6 设置。

WebRTC 里出现内网地址不一定是问题。我手机之前显示的 `172.19.0.1` 就是 VPN 内网地址，要和真实公网地址区分开。

### 4. 单独测试速度和稳定性

让 Codex 连续访问几次目标网站，再用小文件下载测试速度，观察有没有超时、断流和明显波动。

这里把两件事分开：检测页的分数反映它对 IP 风险和信誉的评估，跟网速没有关系。出口和泄露情况检查完以后，再单独测速度、超时和断流。

如果加上静态代理后明显变慢，就让 Codex 用同一个网站、同一个文件，对比“机场直接访问”和“机场加静态代理访问”。前者正常、后者慢，再继续检查静态代理和中转线路，别把时间耗在反复改语言、改时区上。

如果手机检测页能打开，但结果一直空白，就让 Codex 检查浏览器版本，再用其他检测页复测。我之前就在旧安卓手机上遇到过这种情况。

**出口对得上、没有发现意外绕行、连续访问稳定，再进入下一步。检测分数不用追求满分。**

## 第三步：准备浏览器和邮箱

我会单独留一个浏览器或浏览器配置文件用于 Claude，方便保持登录状态，也避免几个账号混在一起。普通的 Chrome、Edge 就可以，保持更新。

语言用自己习惯的，系统时间保持准确。环境设置好后，就固定下来使用。如果网页反复跳到不需要的语言，顺手检查浏览器自动翻译和账号语言设置。

邮箱我优先用 Gmail。如果你已经有能正常收信的 Gmail，直接用现有的就可以。

**如果需要新注册，我推荐先在手机上注册 Google 账号，再开通 Gmail。** 我自己这样注册了 3 个，过程都比较顺利。

先在手机的 Google 登录页面选择创建账号，按提示完成注册，再打开 Gmail，用刚才的账号登录。如果还没有 Gmail 地址，就按提示创建；注册时已经创建过的，直接进入邮箱即可。

注册完成后，我会先确认能正常收邮件，再保存好密码和恢复信息，后面注册 Claude、接收验证码都用这个邮箱。

如果不准备使用 Gmail，也可以注册 Proton 邮箱：

1. 打开 [Proton Mail](https://proton.me/mail)。
2. 选择创建账号，按页面选择免费方案。
3. 填写用户名和密码，完成页面要求的验证。
4. 进入邮箱，保存密码和恢复信息，确认能正常收邮件。

### 关于“Gmail 老号更稳定”的误解

很多人说，注册 Claude 最好用已经使用几年的 Gmail 老号，这样账号更稳定。**我个人觉得，把邮箱年龄当成稳定性的保证，有点玄学。** 我自己新注册的 Gmail 也能正常使用，所以不会为了这个专门去买老号。

原因很简单：如果只是给邮箱发验证码，Claude 验证的是你能不能收到邮件，这个过程本身不会告诉它 Gmail 注册了多久。即使使用“通过 Google 登录”，[Google 公布的标准登录信息](https://developers.google.com/identity/openid-connect/reference)里，也没有 Google 账号的注册时间；登录凭证的签发时间，不是邮箱的创建时间。

因此，我不会把“老号注册成功”直接归因于邮箱老，也不会把“新号遇到验证”直接归因于邮箱新。平台还可能结合其他信号判断风险。对我来说，邮箱能长期掌握、正常收信、方便找回，比纠结它用了几年更实际。

## 第四步：注册 Claude

网络稳定、邮箱准备好以后，打开 [Claude](https://claude.ai/)。

1. 选择邮箱注册或登录入口。
2. 输入准备好的邮箱地址。
3. 打开邮箱，找到 Claude 发来的邮件。
4. 按提示输入验证码或打开验证链接。
5. 完成页面上的账号信息，进入 Claude 首页。
6. 发送一条简单消息，确认能正常聊天。

注册过程中，我会一直使用刚才测好的网络。收不到邮件，先检查邮箱地址和垃圾邮件；页面超时，先检查连接，不要连续换节点、反复点注册。

## 第五步：选择订阅入口，核对付款信息

注册并登录以后，就可以准备订阅。先确认当前登录的 Claude 账号就是要开通 Pro 的那个账号。

### 我更推荐 Google Play 绑定国内外币卡

支付方式上，**我更推荐通过 Google Play，绑定国内发行、支持外币支付的银行卡来订阅。** 我自己用的是招商银行的万事达普卡，申请过程挺简单：在手机上的招商银行 App 申请，再到线下网点领卡。对我来说，这条路比折腾苹果礼品卡更顺手。

我的操作顺序是：

1. 先申请银行卡，按银行要求到网点领卡并完成激活。
2. 打开 Google Play，确认登录的是准备购买订阅的 Google 账号。
3. 进入“付款和订阅 → 付款方式”，添加银行卡，填写自己的真实账单资料，并完成页面要求的验证。
4. 打开从 Google Play 安装的 Claude，登录要升级的 Claude 账号，再进入升级页面。
5. 选好套餐，确认月付或年付；弹出 Google Play 付款窗口后，核对使用的 Google 账号和银行卡。
6. 看清最终金额、币种和续费周期，再确认付款。付款后回到 Claude，如果弹出 KYC，就按下一步完成验证。

### 苹果礼品卡，我自己没走通

我之前也试过苹果礼品卡，但没有成功完成会员开通。具体情况是：Apple 那边已经扣款，Claude 里面却仍然显示 Free，后面还要申请退款和复核。

所以我更推荐 Google Play 加银行卡。别人用苹果礼品卡也可能成功，只是我自己没走通。

如果你还是选择 Apple 礼品卡，购买前先核对礼品卡适用地区和实际购买订阅的 Apple 账户地区。兑换以后，即使看到了扣款，也要回到 Claude 确认会员权益有没有到账。

## 第六步：订阅后处理 KYC 身份验证

订阅完成后，我遇到了整个流程里最头疼的一环：KYC，也就是身份验证。按照我这套方案，正常走下来的顺序是先注册、再订阅，然后处理订阅后弹出的 KYC。

**先说注册。我按照前面这套方案配置网络后，注册新账号并登录，大多数时候没有弹 KYC，也没有要求手机号验证。** 我自己一共注册了 7 次，只有一次弹了 KYC，而且那次我认为和自己的操作失误有关。这也是我为什么一直强调：先把网络配置好、检查稳定，再开始注册。

**但订阅之后，我遇到的情况是都弹了 KYC。** 网上有人分享，从注册到订阅全程都没有验证，这种情况我自己没遇到过。所以在我的流程里，付完款还要继续完成身份验证。

真弹出 KYC，如果自己有护照和海外驾照可以用自己的，按提示完成拍摄及后续验证。拍摄前检查证件是否过期，保证画面清晰、四角完整，减少因为反光、模糊而重复提交。

如果这两种证件都没有，就要再找其他渠道。我最后也是找别人协助处理的 KYC。完成 KYC 后，再回到 Claude 检查会员状态，并发一条消息确认能正常使用。

## 第七步：开通失败或账号停用，怎样退款和申诉

如果订阅和使用都正常，这一步可以跳过。我遇到过两种需要退款的情况：Apple 扣款后会员未生效，第一次退款还被拒；Google Play 订阅后，Claude 账号被停用。我分别按这两种情况提交了申请。

我的做法是先整理证据，再找实际扣款的平台。**未开通就写未开通，账号停用就写停用，把发生时间和无法使用的情况讲清楚。**

### 先准备这些资料

- 购买日期、套餐、币种、实付金额和订单号。
- Claude 账号邮箱，以及购买时使用的 Apple 或 Google 账号。
- 扣款成功的收据或订单截图。
- Claude 显示 Free、报错或账号停用的截图。
- 已经尝试过的处理步骤，以及平台给出的拒绝理由。

这几项放在一起，后面申请、查进度、补充说明都能直接用。提交给官方支持时保留识别订单所需的信息，对外分享时再把邮箱、订单号和付款资料打码。

### Apple：先申请退款，被拒后申请复核

我通过苹果商店购买的订阅，是这样申请的：

1. 打开 [Apple 退款页面](https://reportaproblem.apple.com/)，登录实际购买这笔订阅的 Apple 账户。
2. 在“我需要 / I'd like to”里选择“请求退款 / Request a refund”。
3. 选择符合实际情况的原因，找到对应的 Claude Pro 订单，核对日期和金额。
4. 提交申请，保存提交成功的页面。需要说明时，重点写“已扣款，但付费权益没有开通”。
5. 回到同一个网站，在“查看申请状态 / Check Status of Claims”里查进度，同时留意邮件。Apple 的[进度说明](https://support.apple.com/118224)给出的更新时间通常是 24–48 小时。

如果页面没有找到订单，我会先检查 Apple 账户是不是用错了，而不是重新发起购买。

我第一次被拒时，页面显示这笔购买不符合退款条件，但同时提供了重新审核的入口。如果你也看到“复核决定”或“Reason for review”，就打开原申请，补充此前没有说清楚的事实。

我会重点说明：Apple 的订单和订阅记录已经存在，但购买所用的 Claude 账号仍然是 Free；付费权益没有交付；取消续费只是避免继续扣款，并没有解决这次收费的问题。有附件入口就上传截图，没有的话在说明中写明可以提供证据。

下面这段适合“扣款但从未开通权益”的复核，按自己的实际情况修改：

> I request a review of the refund denial for my Claude Pro subscription. Apple charged me successfully, but the paid subscription was never activated on the Claude account used for the purchase. The app still shows Free, and I have not received the paid features. I can provide the receipt and screenshots showing the mismatch. I cancelled auto-renewal to prevent further charges, but that does not resolve the charge for the undelivered service. Please review this evidence, reverse the denial, and issue a refund. If you maintain the denial, please explain the specific reason.

如果原申请已经没有复核入口，就通过 [Apple 支持](https://support.apple.com/contact)提供原订单和申请记录，请求进一步核查。

另外还有两件事要单独做：

- 到 iPhone“设置 → Apple 账户 → 订阅 → Claude”检查自动续费。我会确认页面显示的是已取消或到期时间，而不是下一次续费日期。
- 获批后再查钱是否到账。我用 Apple 账户余额支付的部分，退款会退回账户余额，不是退回购买礼品卡时使用的支付宝；[Apple 说明](https://support.apple.com/118224)这类退款到账可能需要最多 48 小时。

### Google Play：找到对应订单，说明账号停用后无法使用

Google Play 那笔，我写明的是“订阅后账号被停用，无法继续使用”，没有把它写成“从未购买”或“未经授权扣款”。

操作步骤是：

1. 打开 [Google Play](https://play.google.com/)，登录实际付款的 Google 账号。
2. 点击头像，进入“付款和订阅 → 预算和订单记录”。
3. 找到 Claude Pro，核对金额、日期和以 `GPA.` 开头的订单号。
4. 点击“报告问题”，选择符合情况的选项，填写退款说明并提交。也可以从 [Google Play 官方退款入口](https://support.google.com/googleplay/answer/15574897?hl=zh-Hans)开始。
5. 保存申请记录，通过官方退款页面里的“查看退款申请状态”查询，同时检查邮箱。Google 提示处理一般需要 1–4 天，同一笔订单反复提交不会加快审核。

这类情况可以这样写，把方括号替换成自己的信息：

> I purchased Claude Pro through Google Play on [purchase date]. Order ID: [GPA order ID]. Amount: [amount and currency]. My Claude account was disabled on [date], and I can no longer access the paid subscription. Please review this charge and my request for a refund. I can provide the Google Play receipt and the account-disabled notice. Please let me know if any further evidence is needed.

如果 Google Play 拒绝，或者购买已经超过 48 小时，我会继续通过开发者支持渠道处理，不再反复提交同一张表单。打开 [Claude 退款帮助页](https://support.claude.com/en/articles/12386328-request-a-refund-for-a-paid-claude-plan)，从支持入口提供 Google Play 账号邮箱、GPA 订单号、停用通知，以及 Google 的处理结果，请求核查退款资格。

已经被拒时，可以在前面那段说明后补上：

> Google Play declined my refund request. Please review the purchase and my inability to access the subscription as the developer. The receipt, account-disabled notice, and Google's decision are available for review. Please explain the outcome and the next available step.

账号无法登录时，就从 Claude 帮助中心联系支持，说明原账号邮箱和无法登录的原因。退款和解封是两个诉求，分别写清楚，方便客服处理。

最后，再到 Google Play“付款和订阅 → 订阅 → Claude”检查续费状态，仍在续费就取消。**申请已提交、退款已批准、款项已到账是三个不同的状态，我会一直核对到最终结果。**

---

以上就是我这段时间折腾 Claude 的经验。先把网络弄稳定，再按步骤注册和订阅，希望能帮你少走一些弯路。
