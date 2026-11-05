# GEO 开源项目

> GitHub 高星 GEO 开源项目清单（star 数核验于 2026-11-05，GitHub API 一手数据）。

## 平台级（自托管）

| 项目 | Stars | 语言 | 一句话 |
|------|-------|------|--------|
| [aigclink/geolook](https://github.com/aigclink/geolook) | 808 | Python | **端到端实施平台**（非纯监测）：状态→诊断→工单→资产生成→自动验收→客户交付包；含 RFC 9309 robots 解析、WAF-UA 差异探测、Chrome 采样助手、17 引擎矩阵（中文引擎一等公民）；仅依赖 requests/bs4/lxml |
| [yaojingang/GEOInflow](https://github.com/yaojingang/GEOInflow) | 803 | TypeScript | 自托管 Web+AI 爬虫分析：追踪访客、AI 搜索引荐、抓取日志 |
| [yaojingang/GEOLab](https://github.com/yaojingang/GEOLab) | 748 | — | **研究数据总仓**：54 篇 GEO/AEO 论文库 + CN-GEO 中文引用数据集（187,818 条去重引用）+ 海外跨平台实验数据（602 prompts），可 duckdb 复算 |
| [elmohq/elmo](https://github.com/elmohq/elmo) | 566 | TypeScript | 开源 AEO/GEO 平台，追踪 ChatGPT/Claude/Perplexity 中的品牌表现 |
| [yaojingang/GEORank](https://github.com/yaojingang/GEORank) | 532 | Python | 完整自托管 GEO 工作台（Next.js+FastAPI+PG/Redis/Qdrant/Neo4j）：多人协作/对客交付场景；JSON-LD/llms.txt/标题生成器可直接用 |
| [ai-search-guru/getcito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) | 505 | TypeScript | 自称首个开源 AIO/AEO/GEO 工具 |
| [yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow) | — | PHP/Laravel | 规模化 GEO 内容生产与分发运营系统（Docker） |
| [yaojingang/yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) | — | — | 21 个细分环节 agent 技能包：意图挖掘/页面体检/路线图/解释页/对比页/标题优化等 |
| [AI2HU/gego](https://github.com/AI2HU/gego) | 109 | Go | 跨 LLM 的品牌 GEO 追踪 |

## 研究与框架

| 项目 | Stars | 一句话 |
|------|-------|--------|
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | 236 | ICLR'26 论文官方实现：自动学习生成式引擎偏好并改写网页内容 |
| [mverab/eGEOagents](https://github.com/mverab/eGEOagents) | 218 | 开源 GEO/AEO 工具箱（电商场景起家，对应 E-GEO 论文） |
| [geo-team-red/geo-optimizer](https://github.com/geo-team-red/geo-optimizer) | 103 | Go 语言可插拔 GEO 优化框架 |
| [GitHiteshZope/aigeo](https://github.com/GitHiteshZope/aigeo) | 72 | Laravel 生态的 GEO 组件，让产品进 AI 答案 |

## Agent 技能类

| 项目 | Stars | 一句话 |
|------|-------|--------|
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) | 1355 | Claude Code 技能包：16 个基础模块提升 AEO/GEO 得分（当前最高星） |
| [liangdabiao/GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) | 233 | 中文 GEO 内容优化方法论技能（面向 ChatGPT/Perplexity/Gemini） |

## 审计 CLI

| 项目 | 一句话 |
|------|--------|
| [vasco-branco06/geo-check](https://github.com/vasco-branco06/geo-check) | 开源 CLI：从 robots.txt/sitemap/llms.txt+抽样页给站点的 AI 爬虫可达性打分，评分路径不含 LLM（结果可复现） |
| [shadowresearch/auto-geo](https://github.com/shadowresearch/auto-geo) | 开源 CLI：审计页面 AI 引用就绪度，实测 5 大引擎是否引用你的域名 |

## Awesome 清单

| 清单 | Stars | 一句话 |
|------|-------|--------|
| [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) | 539 | GEO 资源精选：指南、工具、研究 |
| [luka2chat/awesome-geo](https://github.com/luka2chat/awesome-geo) | 133 | 中英双语 awesome 清单，论文区最全 |
| [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) | 128 | 偏学术研究方向 |
| [izak-fisher/generative-engine-optimization-tools](https://github.com/izak-fisher/generative-engine-optimization-tools) | 120 | 纯工具清单 |

## 选型建议

- 想**看懂学界怎么做**：AutoGEO + GEO-bench；要**一手数据自己复算**：GEOLab（parquet + duckdb）。
- 想**单人跑完整 GEO 项目并交付客户**：geolook（零基础设施，文件即数据库，`git init` 即备份）。
- 想**自建监测**：GEOInflow（含爬虫日志）或 elmo；多人协作/产品化：GEORank。
- 想**零成本审计**：geo-check 跑一遍，10 分钟出报告。
- 用 **Claude Code/Agent 工作流**：gtm-engineer-skills、yao-geo-skills 或中文的 GEO-Content-Optimizer-Skill。

## 一个有用的品类区分：监测 SaaS vs 实施平台

多数商业 GEO 产品是**监测**（看提及率、给建议、数据在厂商云）；少数开源项目做**实施**（诊断→工单→生成资产→程序化验收→交付）。选型先问自己要哪种：只要仪表盘选监测，要"干完活能验收"选实施平台。监测数据在谁手里也是企业选型的硬约束。

---
*上一篇：[工具总览](01-tools-overview.md) ｜ 下一篇：[商业监测平台](03-commercial-platforms.md)*
