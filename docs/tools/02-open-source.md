# GEO 开源项目

> GitHub 高星 GEO 开源项目速查目录（star/许可/活跃度核验于 2026-11-06，GitHub API 一手数据）。
> 每个项目"优势/不足/场景"的深度分析见 [projects/ 板块](../projects/01-selection-map.md)；本页只做选型索引。

## 物种分类速览

四类物种（监测平台/实施平台/Agent 技能/研究框架）的判别方法和决策树 → [projects/01-selection-map](../projects/01-selection-map.md)。

## 实施平台（诊断→工单→验收闭环）

| 项目 | Stars | 语言 | 许可 | 一句话 |
|------|-------|------|------|--------|
| [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | 4032 | PHP/Laravel | ⚠️ AGPL-3.0 | 规模化 GEO 内容工程与多站点分发（Docker），活跃（push 11-04） |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | 1355 | — | MIT | Claude Code 技能包：16 个基础模块提升 AEO/GEO 得分 |
| [aigclink/geolook](https://github.com/aigclink/geolook) | 808 | Python | MIT | **端到端实施平台**（非纯监测）：状态→诊断→工单→资产生成→自动验收→客户交付包；含 RFC 9309 robots 解析、WAF-UA 差异探测、Chrome 采样助手、17 引擎矩阵（中文引擎一等公民）；仅依赖 requests/bs4/lxml；⚠️ push 停在 08-10 |
| [yaojingang/GEORank](https://github.com/yaojingang/GEORank) | 533 | Python | Apache-2.0 | 完整自托管 GEO 工作台（Next.js+FastAPI+PG/Redis/Qdrant/Neo4j）：多人协作/对客交付场景；JSON-LD/llms.txt/标题生成器可直接用 |

## 监测平台（追踪 AI 提及/引用）

| 项目 | Stars | 语言 | 许可 | 一句话 |
|------|-------|------|------|--------|
| [elmohq/elmo](https://github.com/elmohq/elmo) | 570 | TypeScript | MIT | 开源 AEO/GEO 平台，追踪 ChatGPT/Claude/Perplexity 中的品牌表现；142 个 open issue、push 到 11-06，社区最活跃 |
| [yaojingang/GEOInflow](https://github.com/yaojingang/GEOInflow) | 810 | TypeScript | MIT | 自托管 Web+AI 爬虫分析：追踪访客、AI 搜索引荐、抓取日志；⚠️ 创建 11 天破 800★，增速异常（见存疑区） |
| [limelit-co/open](https://github.com/limelit-co/open) | 386 | — | Apache-2.0 | 自托管 AI 可见度追踪（AEO/GEO/LLMO），五引擎矩阵 |
| [danishashko/geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) | 320 | — | MIT | 轻量追踪器：ChatGPT/Perplexity/Gemini/Copilot/Google AI Mode 提及监测 |
| [oneglanse/oneglanse](https://github.com/oneglanse/oneglanse) | 250 | — | MIT | 开源 AI 可见度追踪器，五引擎覆盖 |
| [ai-search-guru/getcito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) | 449 | TypeScript | MIT | 自称首个开源 AIO/AEO/GEO 工具；⚠️ 一周内 505→449 掉星，清量迹象 |
| [AI2HU/gego](https://github.com/AI2HU/gego) | 109 | Go | GPL-3.0 | 跨 LLM 的品牌 GEO 追踪 |

## Agent 技能包（装进 AI 助手）

| 项目 | Stars | 许可 | 一句话 |
|------|-------|------|--------|
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | 1280 | MIT | GeoReady(geoready.dev) 开源引擎：审计页面能否被 ChatGPT/Perplexity/Gemini 引用 |
| [yaojingang/yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) | 914 | MIT | 21 个细分环节 agent 技能包：意图挖掘/页面体检/路线图/解释页/对比页/标题优化等 |
| [ViryaZheng/recomby-geo](https://github.com/ViryaZheng/recomby-geo) | 454 | MIT | GEO"AI 员工"方案：技能包 + agent/工具精选清单（中文社区向） |
| [Fangx-AI/geo-doctor](https://github.com/Fangx-AI/geo-doctor) | 354 | MIT | **GEO 医生**：一句话装进 Claude Code/Codex/Kimi Code/WorkBuddy；八步问诊闭环（找差距→批量写发→推荐率复查）；中英双语主打豆包/DeepSeek/元宝等国内引擎；免费无服务器；push 11-02 活跃 |
| [liangdabiao/GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) | 233 | 未标 | 中文 GEO 内容优化方法论技能（面向 ChatGPT/Perplexity/Gemini） |
| [beyondtahir/beyondseo](https://github.com/beyondtahir/beyondseo) | 252 | MIT | "AI SEO 事务所"：站内审计+写内容+竞品对比+外链规划一体化 |
| [HeiGeAi/HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) | 87 | MIT | 中国市场优先 GEO+SEO：豆包/千问/DeepSeek/文心/元宝引用优化，兼容多 agent 宿主 |
| [Houseofmvps/claude-rank](https://github.com/Houseofmvps/claude-rank) | 149 | MIT | Claude Code 插件：查站为何不被 AI 引用并自动修可发现性文件 |

## 研究框架与数据集

| 项目 | Stars | 许可 | 一句话 |
|------|-------|------|--------|
| [yaojingang/GEOLab](https://github.com/yaojingang/GEOLab) | 749 | ⚠️ NOASSERTION（用前读 LICENSE 原文） | **研究数据总仓**：54 篇 GEO/AEO 论文库 + CN-GEO 中文引用数据集（187,818 条去重引用）+ 海外跨平台实验数据（602 prompts），可 duckdb 复算 |
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | 236 | MIT | ICLR'26 官方实现：自动挖掘引擎偏好规则→重写文档；双指标 GEO score×GEU score；发 3 个数据集+Qwen1.7B checkpoints |
| [mverab/eGEOagents](https://github.com/mverab/eGEOagents) | 217 | MIT | 开源 GEO/AEO 工具箱（电商场景起家，对应 E-GEO 论文） |
| [psbagga17/E-GEO](https://github.com/psbagga17/E-GEO) | 50 | 未标 | 电商 GEO 测试床 |
| [QianfengWen/SafeGEO](https://github.com/QianfengWen/SafeGEO) | 10 | Apache-2.0 | EMNLP'26：GEO 攻击在 LLM 推荐代理上的 benchmark——攻防视角稀缺品 |

## 工程组件（语言/框架级）

| 项目 | Stars | 一句话 |
|------|-------|--------|
| [cucuwang/geoptimize](https://github.com/cucuwang/geoptimize) | 263 | 确定性内容就绪度 lint：不靠 LLM，固定规则判可引用性（Claude Code skill 形态） |
| [dodopayments/dualmark](https://github.com/dodopayments/dualmark) | 123 | AEO 基础设施：每页双标记（HTML+Markdown 孪生）供 AI 消费 |
| [geo-team-red/geo-optimizer](https://github.com/geo-team-red/geo-optimizer) | 103 | Go 可插拔 GEO 优化框架 |
| [chnjames/AIGEOTOOLS](https://github.com/chnjames/AIGEOTOOLS) | 183 | 中文 GEO 智能内容优化平台：关键词策略/多平台生成/E-E-A-T/多模型验证 |
| [GitHiteshZope/aigeo](https://github.com/GitHiteshZope/aigeo) | 72 | Laravel 生态 GEO 组件 |
| [wzj177/geo-friendly](https://github.com/wzj177/geo-friendly) | 5 | PHP 版 GEO 适配层（样本极小仅作品类存在证明） |

## 审计 CLI

| 项目 | 星标 | 一句话 |
|------|------|--------|
| [SamurAIGPT/geo-checker](https://github.com/SamurAIGPT/geo-checker) | 18 | Next.js SaaS 形态 GEO 审计 |
| [vasco-branco06/geo-check](https://github.com/vasco-branco06/geo-check) | 3 | CLI：robots/sitemap/llms.txt+抽样页给 AI 爬虫可达性打分，评分路径不含 LLM（可复现） |
| [shadowresearch/auto-geo](https://github.com/shadowresearch/auto-geo) | 28 | CLI：审计页面 AI 引用就绪度，实测 5 大引擎是否引用你的域名 |

## Awesome 清单

| 清单 | Stars | 一句话 |
|------|-------|--------|
| [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) | 538 | GEO 资源精选：指南、工具、研究 |
| [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) | 132 | 中英双语 awesome 清单，论文区最全 |
| [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) | 128 | 偏学术研究方向 |
| [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) | 120 | 纯工具清单 |

## 存疑区（收录不采信热度）

刷星判定方法与逐条疑点见 [projects/01-selection-map 第四节](../projects/01-selection-map.md#四存疑区不参与正文排名与深析)。当前名单：open-seo-mcp-skills（8872★，账号画像不匹配）、aaron-marketing-skills（3075★，分布异常待核）、GEOInflow（810★/11 天，增速异常）。

## 选型建议

- 想**看懂学界怎么做**：AutoGEO；要**一手数据自己复算**：GEOLab（parquet + duckdb，先核许可）。
- 想**单人跑完整 GEO 项目并交付客户**：geolook（零基础设施，文件即数据库，`git init` 即备份；接受自维护 fork）。
- 想**自建监测**：elmo（最活跃）或 GEOInflow（含爬虫日志）；多人协作/产品化：GEORank。
- 用 **Claude Code/Agent 工作流**：英文站 gtm-engineer-skills / Auriti；中文站 geo-doctor（免费）；细分拼装 yao-geo-skills。
- 要**不靠 LLM 的可复现审计**：geoptimize（确定性 lint）或 geo-check（CLI）。

## 一个有用的品类区分：监测 SaaS vs 实施平台

多数商业 GEO 产品是**监测**（看提及率、给建议、数据在厂商云）；少数开源项目做**实施**（诊断→工单→生成资产→程序化验收→交付）。选型先问自己要哪种：只要仪表盘选监测，要"干完活能验收"选实施平台。监测数据在谁手里也是企业选型的硬约束。2026 下半年新变量：**Agent 技能包**成为第三极——不分平台形态，直接寄生在你已有的 AI 助手里，geo-doctor/gtm-engineer-skills 是代表。

---
*上一篇：[工具总览](01-tools-overview.md) ｜ 下一篇：[商业监测平台](03-commercial-platforms.md) ｜ 深析：[projects/01 选型地图](../projects/01-selection-map.md)*
