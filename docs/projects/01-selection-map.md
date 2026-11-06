# GEO 开源项目选型地图

> 全部数据 GitHub API 一手核验于 2026-11-06。深析见本板块后续各篇。
> 先问自己要哪种物种，再进对应篇挑具体项目。

## 一、四个物种（GEO 开源世界的分类学）

GEO 开源项目 2025-2026 爆发后快速分化成四个物种，形态、商业模式、适用人完全不同。混着比会选错。

| 物种 | 交付形态 | 代表 | 解决什么 | 给谁用 |
|------|---------|------|---------|--------|
| **监测平台** | 自托管/云仪表盘，持续追踪提及率排名 | elmo(570)、limelit(386)、geo-aeo-tracker(320)、oneglanse(250) | "AI 现在怎么说我" | 有站要长期盯的人 |
| **实施平台** | 诊断→工单→资产→验收→交付包闭环 | geolook(808)、GEORank(533)、GEOFlow(4032) | "把 GEO 干完并能验收" | 顾问/服务商/自己动手的团队 |
| **Agent 技能包** | 装进 Claude Code/Codex 等助手的 skill | gtm-engineer-skills(1355)、Auriti(1280)、yao-geo-skills(914)、geo-doctor(354) | "一句话让 AI 助手替我做 GEO" | 已在用 AI 编码助手的个人/小团队 |
| **研究框架** | 论文官方代码+数据集+可复训模型 | AutoGEO(236)、GEOLab(749)、E-GEO(50)、SafeGEO(10) | "引擎到底偏好什么、数据哪来" | 要机理和一手数据的研究者 |

另有一个边缘带：**工程组件**（给某语言/框架加 GEO 能力的小库：Go 版 geo-optimizer(103)、PHP 版 aigeo(72)/geo-friendly(5)、双标记基础设施 dualmark(123)、内容 lint geoptimize(263)），见 [06 内容工厂与工程组件](06-content-factories.md)。

## 二、决策树

```
你要做什么？
│
├─ 只想知道 AI 怎么提我（看数不动手）
│   └─ 监测平台 → 五大引擎全覆盖选 elmo；要爬虫日志选 GEOInflow；
│       极简单页选 geo-aeo-tracker；要 18 万条中文引用语料复算选 GEOLab
│
├─ 要把 GEO 做完交付（客户或自己老板要结果）
│   ├─ 单人零基础设施、文件即数据库 → geolook
│   ├─ 多人协作/产品化（PG/Redis/Neo4j 全家桶）→ GEORank
│   ├─ 规模化内容生产+多站分发 → GEOFlow（⚠️ AGPL-3.0，商用分发需谨慎）
│   └─ 出方案不改代码、纯顾问流程 → 本书 reverse/ + advanced/08 手工跑
│
├─ 我天天用 Claude Code/Codex，想要"一句话开工"
│   ├─ 英文站 16 模块工程化 → gtm-engineer-skills
│   ├─ 单点审计能否被引用 → Auriti/geo-optimizer-skill
│   ├─ 21 个细分环节自由拼 → yao-geo-skills
│   └─ 中文站免费轻量全流程 → geo-doctor
│
└─ 我要写论文/搞清机理/拿数据集
    ├─ 偏好规则+重写框架 → AutoGEO（ICLR'26）
    ├─ 中文引用语料 → GEOLab（187,818 条，duckdb 可复算）
    ├─ 电商场景 → E-GEO；GEO 攻击安全面 → SafeGEO
```

## 三、选型时的三个硬约束（比 star 数重要）

1. **许可证**：GEOLab=NOASSERTION（API 字段，用前读 LICENSE 原文）；GEOFlow=AGPL-3.0（把它的能力嵌进你的 SaaS 会触发传染条款）；多数竞品是 MIT/Apache-2.0 可放心参考实现。本书引用一律标注核验日期与字段来源。
2. **活跃度**：GEO 赛道普遍"爆星后停滞"。硬指标看 `pushed_at`：geolook 停在 2026-08-10（近 3 个月）、AutoGEO 停在 06-14（学术项目正常）；elmo/GEOLab/GEOFlow 推到 11-04/06（活跃）。选停滞项目 = 接受自维护 fork。
3. **数据主权**：监测类一半是"开源壳+厂商云数据"。真自托管（数据在你机器）：GEOInflow、limelit、geolook、oneglanse；伪自托管要逐个读部署文档确认数据落点。

## 四、存疑区（不参与正文排名与深析）

刷星在 GEO 赛道是公开的秘密。以下项目 star 与账号画像/社区信号明显不匹配，**收录但不采信其热度**，仅作功能参考：

| 项目 | 星标 | 疑点（API 一手核验 2026-11-06） |
|------|------|----------------------------------|
| Ryze-AI-Adgent/open-seo-mcp-skills | 8872 | 账号名含拼写错误"Adgent"且名称字段原样如此；账号 2025-10 注册、followers 仅 12、公开仓库 7 个，与 8.8k★ 严重不匹配 |
| aaron-he-zhu/aaron-marketing-skills | 3075 | 账号画像正常（2023 注册、111 followers、活跃推送），但"120 个营销技能"体量与 3k★ 集中在单仓的分布异常，待社区讨论交叉核实 |
| yaojingang/GEOInflow | 810 | 2026-10-26 创建，11 天 810★+253 fork，增速远超自然扩散曲线；同作者 5 个 GEO 仓库互相导流 |

判定方法（可复用）：`/users/{login}` 看注册时间和 followers、`/repos/{owner}/{repo}/stargazers` 抽样看星主画像、hn.algolia.com 看讨论声量。零声量高星 = 红灯。

## 五、与本书其他板块的关系

- 品类概念（监测 vs 实施）：见 [tools/02-open-source](../tools/02-open-source.md) 末节。
- 引擎引用机理（为什么这些工具长这样）：[guide/05-how-ai-engines-cite](../guide/05-how-ai-engines-cite.md)。
- 中文生态差异（为什么 geo-doctor 这类中文技能会火）：[cn-vs-global/01](../cn-vs-global/01-structural-differences.md)、[guide/10](../guide/10-cn-source-ranking.md)。
- 时效信号（掉星、新上线）：跟踪在 [news/01-signal-log](../news/01-signal-log.md)。

## 六、本板块目录

| 篇 | 主题 | 状态 |
|----|------|------|
| [02 实施平台深析](02-implementation-platforms.md) | geolook/GEORank/GEOFlow/GEOInflow | ✅ |
| [03 监测平台对比](03-monitoring-trackers.md) | elmo/limelit/oneglanse/gego 等五款 | ✅ |
| [04 Agent 技能包深析](04-agent-skills.md) | 五包横评+中文支持对比 | ✅ |
| [05 研究框架与数据集](05-research-frameworks.md) | AutoGEO/GEOLab/SafeGEO 等 | ✅ |
| [06 内容工厂与工程组件](06-content-factories.md) | geoptimize/dualmark/语言组件 | ✅ |

---
*数据核验：GitHub REST API，2026-11-06。季度复查。*
