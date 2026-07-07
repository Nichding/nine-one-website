# Nine One Website — STATUS
> 接力棒。改完谁更新；接手先读。最近更新：2026-06-26

## 一句话现状
8 页官网已全部重做成 **Apple 式产品生态站**(Inter + Spline Mono，严格 6-token CI，白底为主，零非 CI hex)；Play 页(`sports.html`)已深度打磨多轮，**视觉到位、但图全是占位图、证据层偏弱**。仅本地 + 桌面预览，**未上线**。

## 进行中
- [ ] Play 页(`sports.html`)精修收尾——hero、区块顺序、轮播样式都已按 Nicholas 多轮反馈改好
- [ ] 待办的"大动作"是 **AI 配图系统**(见下，还没开始)

## 已完成(本轮要点)
- **全站 8 页**：`index`(Home)/`sports`(Play 旗舰)/`sports-specs`(Play 规格)/`technologies`/`facility`/`ecosystem`/`about`/`build`。每页：严格 6 hex、Inter+Spline、官方 logo SVG、og/twitter/canonical、`Move Together.` 页脚、零非 CI hex。
- **紧凑导航(全站)**：`--nav-h:70px`、logo 40px、副导航 `.psub` 50px(仅 sports/sports-specs)；整个 header 120px。
- **内容列收窄(全站)**：`--maxw / --maxw-wide = 1024px`，宽屏下左内距 ~265px(贴近 Apple)。
- **Play 页 hero(`.vstage` 滚动吸顶)**：左下角图说式标题 `[no logo] Nine One │ Play`(logo 与字同高 + 竖线，标题 max 44px、logo 37px) + 一行正文 + 右下角 `Plan a site`；整条 bar 滚动渐隐、JS 拉到可见底部。**hero 文字左内距已减半到 132px**(CTA 仍 265 右)。
- **Play 区块顺序**：vstage → vdemo(全幅图) → closer(细看球场·6卡) → 全幅图 → **Designed for New Zealand**(5卡) → 全幅图 → materials(7卡) → moments(共同时刻·已统一成图+说明轮播·5卡) → Play OS(深色·future) → CTA → footer。
- **轮播统一**：图+说明(`.cslide-cap`) + 底部居中箭头(`.carousel-foot`) + `scroll-padding-left` 让首卡对齐内容列。
- **已删**：幕后技术(`.tech`)、规格入口(`.specteaser`)、Built for(`.audience`)三段 + 对应死 CSS。
- 备份在 `_backup/`；旧草稿 `play-framework.html`/`play-specs.html` 还在(已被取代，未上线，可清理)。

## 设计方向(已和 Nicholas 谈定的北极星)
- **公式：用 Apple 的完成度 + Warren and Mahoney 的内容(项目/证据/规格) + Vitsœ 的克制世界观。** Apple = 质量标杆，W&M = 内容模型。
- **硬约束：现在没有真实球场，所有配图只能 AI 生成。** 要点：① 锁一套视觉配方让所有图"像同一次拍摄"(一致性 > 单张惊艳)；② **诚实框架**——用 concept/visualisation/"designed as"，绝不暗示成已建成项目；③ logo 后期合成(AI 不画 logo)。
- **Spline Sans Mono = 可信度杀手锏**：规格/数字/流程用等宽字，给"工程级、可核实"感。

## 阻塞 / 待 Nicholas 拍板
- **配图**：现全是 `assets/images/opt/*.jpg` 优化占位图(stock 味)。需先产出 AI 成套图再替换——这是和"Apple 感"之间最大的沟。
- **文案签字**：新增对外文案(Designed for New Zealand、hero 等)属对外产出，发布前须过 CI §22 合规清单 + Nicholas 过目。
- **上线**：**未批准**。一律本地 + 预览，等 Nicholas 明确说「上线」才推 `main`(Netlify 自动部署)。
- P1：sitemap/favicon；清理 `play-framework.html`/`play-specs.html`；结构图需更新(`Desktop/NineOne-Play-StructureMap.html` 已过时)。

## 下一步
1. **锁定设计方向**(Apple 完成度 + W&M 内容 + AI 配图，基本已定)。
2. **AI 配图系统**：写 master prompt 配方 + 全站 shot list → 生成 → 统一调色 → 合成官方 logo → 替换占位图。
3. **补证据层**(无真实项目时的可信来源)：能力/规格(Spline Mono)、流程"接下来会发生什么"、诚实 concept 框架；同时"再删一轮"做到一屏一意。
4. 文案签字 → §22 合规 → 等「上线」再部署。

## 工作方式
PM 会话判断/拆活，网站的活派 **`web` 执行者**(代码在 `~/Projects`，文案在 OneDrive；遵守 Nine One CI)。工作流见 `OneDrive/_AI_Rules/Workflow.md`。

## 关键文件指针
- 代码：`~/Projects/nineone/website`(GitHub，Netlify 自动部署 `main`)
- 文案/CI 计划：`0_Company/Website/`
- CI 正本：`0_Company/Brand_CI/NINEONE_CI_System.html`(发布前过 §22)
- 6 token：paper `#F4F4F1` / ink `#121311` / graphite `#76766E` / black `#0B0B0B` / greige `#D9D8D2` / Play accent `#F6BE83`(其余一律这些的 rgba)
- 字体：Inter(正文/标题) + Spline Sans Mono(标签/规格)。**禁** Figtree/Public Sans(已归档的旧 CI 陷阱)
- 桌面预览(自包含)：`Desktop/NineOne-Play-Preview.html`、`Desktop/NineOne-Home-Preview.html`(每次改完用内联 base64 脚本重生成)
- 自测：零非 CI hex / Inter+Spline / 官方 logo img / 黑≤35% / 390·768·1440 无横滚 / og+twitter / `Move Together.` 页脚
