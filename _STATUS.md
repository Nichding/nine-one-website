# Nine One 官网 — STATUS（接力棒）

> 改完谁更新，接手先读。**最近更新：2026-07-10**
>
> ⏳ **发布中（待 Nicholas 合 PR）**：本轮全部改动已 commit 并推到 `redesign/ci-v2-phase2`（tip `ca31bde`）。Nicholas 已批准整套 8 页上线（选项 A）。**直接 push main 被仓库钩子禁止（须走 PR），且本会话 gh 未登录** → 最后一步由 Nicholas 在 GitHub 手动合 PR：<https://github.com/Nichding/nine-one-website/compare/main...redesign/ci-v2-phase2?expand=1> → Merge → Netlify 自动部署上线。
> ⚠️ **线上曾有平行 Phase 2 提交 `bf1a6fe`（Facility 页+移动导航），不在本分支**。已用 `git merge -s ours origin/main` 把它记入历史但**内容以本分支为准**（PR 因此无冲突、干净可合）；合并即以本分支全面取代它。若发现 bf1a6fe 有本分支缺的东西，再单独补。
> 这是文档侧（OneDrive）的正本接力棒。代码侧 `~/Projects/nineone/website/_STATUS.md` 是同内容的就近副本，以本文为准。

---

## 2026-07-10 执行记录（Air Dome 收尾 / 能力卡 / P1）

- **分支边界**：全部工作只在 `redesign/ci-v2-phase2`；未碰 `main`，未 push，未创建或合并 PR。
- **T1 · Air Dome**（commit `a032d0f`）：`airdome/` 现行草稿已接入 9 张 1080px 优化图与 3 条 1080p 视频。图片已检查并清理 Gemini 标记；`team-onsite` 同时清理车辆品牌字样。视频已清理 Kling / 生成标记，单条 1.5–2.1MB。未确认的 24/7、备用电源、远程监控等配置已撤回；hero 只保留已确认的 25 年设计寿命、10 年质保，安装周期保留 `[__]`。估算器已撤掉具体成本区间，仅保留 `courts × 1200` 占位逻辑，前端无真实成本系数。
- **T1 素材对号**：hero-wide / membrane-skyline / aerial-pushin → hero 三段轮播；allyear → All Year；cost-interior → Cost；durability 1/2/3 → membrane / structure / control；team-onsite → One Team；all-weather → Your Sport；city-design → closing CTA。
- **T1 素材遗留**：`facility-airdome-allyear-storm-01.jpg` 已优化入库但当前没有独立合适版位，未强行重复使用。Air Dome 页继续 `noindex`、未进正式导航。
- **T2 · Play 能力详情**（commit `d0810e8`）：6 个 `.capplus` 已接同一个 overlay modal；支持 Esc、点击遮罩关闭、关闭后焦点返回、移动端全屏。六段英文详情初稿各 80–85 词，页面内明确标注“待 CI §22 + Nicholas 签字”。
- **T3 · P1**：新增 `sitemap.xml`、官方标志 favicon（SVG + 16 / 32 / 180 / 192 / 512 PNG）和 `site.webmanifest`，已接入 8 个正式页面及 Air Dome 草稿页。
- **P1 归档清单（未硬删）**：`play-framework.html`、`play-specs.html`、`css/main.css`、`_old/`、字面目录 `{css,js,pages}` 已原样移入 `_backup/p1-archive-20260710/`。
- **sports-specs 材质残留（只记录、未擅改）**：第 218 行及第 293 行仍有通用 `materials` 表述，分别位于配置说明和规格免责声明；待 Nicholas 决定是否要改成 capability / specification 语言。
- **自测**：8 个正式页面 + Air Dome 共 9 页，390 / 768 / 1440 三档共 27 次检查，无横向溢出；favicon / manifest / `Move Together.` 全部存在。能力弹层在 390px 为全屏，Esc 可关。Air Dome 仅使用 CI token / Facility token 与对应 rgba；Inter + Spline Sans Mono；OG / Twitter meta 齐。

### 仍待 Nicholas 拍板

1. 六段能力详情英文初稿通过 CI §22 并签字。
2. Air Dome 其余 `[__]` 规格真值；未确认前不补数字或配置。
3. 估算器真实逻辑由受控数据源提供，敏感成本系数不得进入前端。
4. `_backup/p1-archive-20260710/` 内旧文件最终保留还是删除。
5. Air Dome 最终并入 `facility.html` 还是保留独立产品页；确认前维持 `noindex` 且不进导航。

---

## 2026-07-10 · CI V2 视觉基础迁移（文案冻结）

- Nicholas 已批准先实施视觉基础层，**页面文案全部冻结，未修改**。
- 当前工作分支：`ci-v2`；基线来自 `redesign/ci-v2-phase2`。未碰 `main`，未 push、未部署。
- token 正源已恢复：`Brand_CI/manifest/tokens.json`，共 29 个 V2 token。
- 新增全站基础层 `css/ci-v2.css`：Master / Play / Technology / Facility 四种语境、Inter + Noto Sans SC + Spline Sans Mono、48/28/16/13/12 type scale、1200px 版心、CI spacing/radius/motion/focus/reduced-motion。
- 已接入 8 个正式页面与 `airdome/` 正主；Play 使用 Jade、Technology 使用 Azure、Facility/Air Dome 使用 Violet，Master 页面保持中性色。
- Air Dome Canvas 动画已改为读取 CSS token，不再内嵌旧色。
- 四个现用官方 Logo SVG 副本仅做颜色归一（Black / Paper），path、viewBox、比例未改。
- 2026-07-10 Logo 决策更新：全站导航与页脚统一改用纯 Mark，不再显示 stacked 文字版；浅底使用 `nineone-mark-ink.svg`（40px 高），深底使用 `nineone-mark-white.svg`（56px 高）。
- 旧 `facility-airdome.html` 仍为未跟踪旧稿，不纳入本次提交；`airdome/index.html` 仍是现行正主。
- 响应式检查：9 页在 390 / 822 / 1440 均无横向溢出；页面计算字体均为 Inter + Noto Sans SC；业务 accent 分别解析为 Jade / Azure / Violet。
- 旧色扫描：正式 HTML/CSS/JS 与现用 Logo 中指定三代旧色归零；`_backup/` 历史档案保持原样，验收 grep 需排除归档目录。

## 一句话现状

8 页官网已整体重做成 **Apple 式产品生态站**（Inter + Spline Sans Mono、严格 6-token CI、白底为主、零非 CI hex）。**AI 配图系统已开跑**：Play 页四条产品线（Kauri / Kawarau / Tekapo / Rangitoto）已全部用上 Gemini 概念渲染图（原档在本文件夹 `Imagery/Renders/`）。之前「7 页未提交」已于 6-28 提交（`751e6cf`）；当前仅 sports.html 的 Rangitoto 段落 + 新图未提交。**线上跑的仍是旧版，本轮重做未上线。**

---

## 仓库 / 分支 / 部署真相（最容易搞混，先读这段）

| | 状态 |
|---|---|
| 线上域名 | **`https://nineonesports.co.nz` 是活的**（`www` 301 跳主域），Netlify 监听 GitHub `main`，push 即自动部署 |
| 线上内容 | **旧版**——本轮重做一行都没上线 |
| 本轮重做位置 | 分支 `redesign/ci-v2-phase2`（当前所在分支） |
| ⚠️ 提交状态 | 大改动已提交至 `751e6cf`（6-28，产品线 + 对比规格 + Facility）。**工作区尚余**：sports.html 的 Rangitoto 段落（+8 行）、新图 `play-rangitoto-01.jpg`（未跟踪）；另有未跟踪的 `_backup/`、旧草稿 `play-framework.html` / `play-specs.html` 待清理。等 Nicholas 点头即 commit（不推 main）。 |
| 分支链 | `main`（线上旧版） → `origin/redesign/ci-v2-phase1`（Phase 1 视觉对齐） → `origin/redesign/ci-v2-phase2`（本轮，当前） |
| GitHub | `https://github.com/Nichding/nine-one-website`（`netlify.toml`：`publish = "."`，纯静态、无构建） |

> 「未上线」指**本轮重做未上线**，不是域名没上线。域名一直在线，只是内容是旧的。

---

## Facility 页重做（7-07 起，进行中）

- **定位已拍板**：Facility = 覆盖类硬件产品线（气膜 / 张拉膜 / 可伸缩顶棚），先做 **Air Dome 单品页**。
- **版式 = tesla.com/solarroof 1:1**（Nicholas 指定，已用 Chrome 实测该页数值落地）：hero 只有 40px/500 居中标题@16vh + 底部「三数据 + 204×40 描边 Order Now」；章节 = 整幅大图(不压字) + 图下白底两栏（左 eyebrow 17/500 + 标题 28/500/lh36 + 3px 描边按钮，右 14px/400 说明段）；深灰半透明产品条。**别再用 Model 3 车型页那套「文字压图」——踩过坑。**
- **草稿文件（两版并存）**：① `facility-airdome.html`（我按 solarroof 实测 1:1 的版本）；② **`airdome/`（index.html + styles.css + script.js，现行正主）**——Nicholas 7-08 给了完整 build spec（外部生成），按 spec 原样执行：文字压图（上标题/下正文居中）、胶囊按钮 260×44、y-proximity scroll-snap、汉堡菜单、估算器已可跑（占位公式 courts×1200，真逻辑待接）。**spec 与实测 solarroof 版式不同（压图 vs 白底带）——以 Nicholas 的 spec 为准**。noindex、未进导航。
- **文案初稿已写入**（PM 叙事：卖「可预订小时数」，对手=天气+盖楼）。已确认真值：**质保 10 年（hero 第三数据 + specs）、设计寿命 25 年（Durability 主打 + specs）**。未确认不写：气压监测/备用风机（Nicholas 确认配置后补）。
- 待办：媒体框换真图/视频（prompt 待出）→ specs 其余 `[__]` 填真值 → 计算器接逻辑（敏感成本系数不进前端）→ §22 → 并入正式 facility.html 或替换。

## 进度

### 已完成（本轮要点）
- **全站 8 页重做**：`index`(Home) / `sports`(Play 旗舰) / `sports-specs`(Play 规格) / `technologies` / `facility` / `ecosystem` / `about` / `build`。每页：严格 6 hex、Inter + Spline、官方 logo SVG、og/twitter/canonical、`Move Together.` 页脚、零非 CI hex。
- **三分区架构落地**（Phase 2）：Play / Technology / Facility 三分区 + Ecosystem 收口，`facility.html` 已建为完整页，全站导航/页脚加 Facility。
- **紧凑导航（全站）**：`--nav-h:70px`、logo 40px、副导航 `.psub` 50px（仅 sports/sports-specs）；整 header 120px。
- **内容列收窄（全站）**：`--maxw / --maxw-wide = 1024px`，宽屏左内距 ~265px（贴近 Apple）。
- **Play 页 hero**（`.vstage` 滚动吸顶）：左下角图说式标题 `[logo] Nine One │ Play`（logo 与字同高 + 竖线）+ 一行正文 + 右下 `Plan a site`；整条 bar 滚动渐隐。hero 文字左内距已减半到 132px。
- **Play 区块顺序**：vstage → vdemo(全幅) → closer(细看球场·6卡) → 全幅 → Designed for New Zealand(5卡) → 全幅 → materials(7卡) → moments(共同时刻·图+说明轮播·5卡) → Play OS(深色) → CTA → footer。
- **轮播统一**：图+说明 + 底部居中箭头 + `scroll-padding-left` 让首卡对齐内容列。
- **已删冗余**：幕后技术 `.tech`、规格入口 `.specteaser`、Built for `.audience` 三段及死 CSS。
- 备份在 `~/Projects/nineone/website/_backup/`。

### 已完成（7-06 增量）
- **Play 页四条产品线全部配上 AI 渲染图**：Kauri（Classic/Panoramic/Extreme）、Kawarau（Outdoor/Elite）、Tekapo（Panoramic/Full）各自轮播；**Rangitoto Platform**（架空甲板，单图 + 一句说明，单图不带翻页按钮）7-06 收尾。原档在 `Imagery/Renders/`（master，未合 logo），上线压缩图在仓库 `assets/images/opt/`。
- 自测已过：零非 CI hex（恰好 6 token）、390/768/1440 无横向滚动、图片正常加载。

### 进行中
- [ ] **AI 配图铺全站**：Play 页产品线已换真渲染图，但其余版位（home/about/ecosystem/facility 及 Play 页 hero 外的全幅图）仍是 stock 占位。配方与 Gem 指令在 `Imagery/`。
- [x] **Play 页 §4 区块从「材质」重构为「能力(Capability)」**（7-07）：原「Down to the material.」7 张材质横卡 → 改为 **6 张能力竖卡(3:4)左右滑动轮播**，标题 `More than the materials.`。六个能力：01 Designed for NZ / 02 Global sourcing / 03 Engineered & certified / 04 End-to-end delivery / 05 Smart from day one / 06 Local service。每卡右下角「+」(占位，详情页/弹层是下一步)。CSS 用新 `.caps` / `.carousel--caps` / `.capfig` / `.capplus` 命名，沿用既有 `.carousel-wrap` JS。**决策转向的原因**：材质是供应商的故事、讲不出 Nine One 的差异；能力(设计/采购/认证/交付/智能/服务)才是。
- [x] **能力卡 6 张真图全部上齐**（7-07）：**风格 = 「精致物件/静物」语言**（浅景深、暖中性、雾感高调背景，几乎不出现完整球场与人）。01 建筑比例模型(海边·等高线底座) / 02 地球仪摆件 / 03 蓝图桌面平铺 / 04 序列静物(卷图→钢节点→钥匙) / 05 门禁立柱产品图(黄昏) / 06 高端服务车+空手技师(本地即时响应)。原档在 `Imagery/Renders/`；入库 PIL 压到宽 1080，`assets/images/opt/play-capability-*-01.jpg`。**入库处理要点(以后同类图沿用)**：① 抹掉 Gemini ✦ 水印(右下角，实测在原图约 x1557/y2150)；② 06 原图车尾门有奔驰车标，已抹(CI 图内禁 logo，我们定的无标高端车)。用 PIL 羽化蒙版补丁，坐标先裁角确认再补，别凭估算(踩过坑：估偏没盖住)。
- [ ] **能力卡「+」详情页/弹层**：6 个「+」当前无动作，待建（文案量最大，先出草稿过 §22）。
- [ ] Global sourcing 那张若用图形而非摄影：手画的 SVG 点阵地图已否（Nicholas 嫌丑），改走 Gemini 出图（prompt 已给）。
- [ ] 旧「材质特写」7 张 prompt 作废（区块已不做材质）；`sports-specs.html` 里若还引用材质叙事需同步检查。
- [ ] `sports-specs.html` 对比规格表**尚无 Rangitoto**——它是平台产品不是球场型号，进不进表待 Nicholas 定。

---

## 已定决策（北极星，已和 Nicholas 谈定）

- **公式：Apple 的完成度 + Warren and Mahoney 的内容模型（项目 / 证据 / 规格）+ Vitsœ 的克制世界观。** Apple = 质量标杆，W&M = 内容模型。
- **硬约束：现在没有真实球场，配图只能 AI 生成。** ① 锁一套视觉配方让所有图「像同一次拍摄」（一致性 > 单张惊艳）；② **诚实框架**——用 concept / visualisation / "designed as"，绝不暗示已建成；③ logo 后期合成（AI 不画 logo）。
- **Spline Sans Mono = 可信度杀手锏**：规格 / 数字 / 流程用等宽字，给「工程级、可核实」感。
- **Phase 2 三分区已拍板并落地**：Sports 显示/定位为 **Play**（文件名仍 `sports.html` 保 SEO/外链）；Facility 直接建完整页进导航；Ecosystem 重写为「统领三分区」的连接叙事。

---

## 阻塞 / 待 Nicholas 拍板

- **配图（最大的沟）**：现全是 `assets/images/opt/*.jpg` 优化占位图（stock 味）。要先产出 AI 成套图再替换——这是与「Apple 感」之间最大的差距。
- **文案签字**：新增对外文案（Designed for New Zealand、各 hero、Facility 等）属对外产出，发布前须过 **CI §22 合规清单** + Nicholas 过目。
- **上线：未批准。** 一律本地 + 预览，等 Nicholas 明确说「上线」才合并到 `main`（Netlify 自动部署）。
- P1 杂项：sitemap / favicon；清理旧草稿 `play-framework.html` / `play-specs.html`（已被取代）；清理仓库历史残留 `_old/`、误建文件夹 `{css,js,pages}`、死文件 `css/main.css`。

---

## 下一步

1. **commit Rangitoto 增量**到 `redesign/ci-v2-phase2`（等 Nicholas 点头；顺带定夺旧草稿 `play-framework.html` / `play-specs.html` 与 `_backup/` 去留）。
2. **AI 配图铺全站**：按 `Imagery/` 配方补齐其余版位（home / about / ecosystem / facility / 全幅图）→ 统一调色 → 需要 logo 的后期合成 → 替换 stock 占位。
3. **补证据层**（无真实项目时的可信来源）：能力 / 规格（Spline Mono）、流程「接下来会发生什么」、诚实 concept 框架；同时「再删一轮」做到一屏一意。
4. 文案签字 → §22 合规 → 等 Nicholas 说「上线」再合并 `main` 部署。

---

## 关键文件指针

- **代码**：`~/Projects/nineone/website`（GitHub `Nichding/nine-one-website`，Netlify 监听 `main` 自动部署）
- **文档 / CI 计划 / 本接力棒**：`2_NineOneSports/0_Company/Website/`（含 `Phase2_CI_Architecture_Plan.md`、`README.md`）
- **CI 正本**：`2_NineOneSports/0_Company/Brand_CI/NINEONE_CI_System.html`（发布前过 §22）
- **6 token**：paper `#F4F4F1` / ink `#121311` / graphite `#76766E` / black `#0B0B0B` / greige `#D9D8D2` / Play accent `#F6BE83`（其余一律这些的 rgba）。Facility 蓝 `#93D2F0` / 深墨 `#0E3B57` 见 CI Facility 段。
- **字体**：Inter（正文/标题）+ Spline Sans Mono（标签/规格）。**禁** Figtree / Public Sans（已归档旧 CI 的陷阱，曾误读踩过坑）。

## 自测清单（每次改完跑）

零非 CI hex · Inter+Spline · 官方 logo `<img>` · 黑占比 ≤35% · 390 / 768 / 1440 无横向滚动 · og + twitter meta 齐 · `Move Together.` 页脚。

## 工作方式

PM 会话判断 / 拆活，网站的活派 **`web` 执行者**（代码在 `~/Projects`，文案在 OneDrive，遵守 Nine One CI）。工作流见 `_AI_Rules/Workflow.md`。
