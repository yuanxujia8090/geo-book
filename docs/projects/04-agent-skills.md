# Agent 技能包深析：gtm-engineer-skills / geo-optimizer-skill / yao-geo-skills / geo-doctor / recomby-geo

> 物种定义见 [01 选型地图](01-selection-map.md)。Agent 技能包 = 装进 Claude Code/Codex/Kimi Code 等编码助手的 skill 目录，让"做 GEO"从开平台变成说一句话。2026 下半年爆发的主战场。
> 数据 GitHub API 一手核验于 2026-11-06；机制来自 README 原文。

## 为什么技能包是个独立物种

平台类（见 [02 实施平台](02-implementation-platforms.md)）要你部署+运维+学界面；技能包寄生在你已有的 AI 助手里，交付形态是"Markdown 指令+脚本+模板"，零基础设施。代价是：执行质量取决于宿主模型，没有确定性保证。选型第一问：**你要的是系统还是帮办**。

## 1. onvoyage-ai/gtm-engineer-skills（1355★ / 58 fork / MIT / 活跃 push 10-11）

**定位**：16 个模块组成可串联的 GTM 流水线——每个 skill 产出一个具体工件（brand_dna.md、keyword_research.md、content_architecture.md、SVG/CSV/JSON-LD 图表、A-F 审计报告、网站代码修复），上一环输出是下一环输入。

**优势**：
- **管道设计是同类里最系统**：README 有 mermaid 流程图定义 12 个 skill 的上下游关系；产物都是"操作员能审、能发、能测"的文件，不是聊天文本。
- 覆盖面从市场研究（research-brand/reddit-opportunity-research）到工程落地（build-resource-pages 直接往客户代码库建页、improve-aeo-geo 出代码修复）打通。
- 安装方式朴素（git clone + 软链进 ~/.codex/skills），无账号无锁定。

**不足**：
- 23 个 open issue 且近一月未推送响应，维护带宽存疑。
- 英文市场向：无中文引擎（豆包/DeepSeek）覆盖，中文站用户拿去要自己改造。
- 每个 skill 的 prompt 质量需逐包评测，README 无 eval 数据。

**场景**：英文站 + 已用 Codex/Claude Code 的运营者，想要"研究→规划→生产→审计→修码"全流程脚手架。**与本书**：其"quotable passages/图表带文本层"要求即 advanced/01 判据的技能化实现。

## 2. Auriti-Labs/geo-optimizer-skill（1280★ / 151 fork / MIT / 活跃）

**定位**：商业产品 GeoReady 的开源引擎：一条命令给任意网站打 0-100 的 AI 可见度分，并给出修复清单。CLI/Python 库/MCP server/GitHub Action/Astro 集成五种形态。

**优势**：
- **工程质量同类最硬**：16 CLI 命令、9 评分类目、27 个 AI 爬虫检查、47 项内容检查、12 个 MCP 工具、8 种输出格式、2000+ 测试、CI 绿标、PyPI 发布（uvx 零安装即跑）。
- **CI 门禁玩法独有**："AI 就绪度跌了就 fail build"——把 GEO 变成持续集成指标，同类唯一。
- 同一引擎 CLI 与网页版（geoready.dev）共用，开源壳/商业云分层清晰；审计示例真实（example.com 8 分 vs 自家 91 分并排贴出）。

**不足**：
- 评分权重是厂商自定 rubric v2，未公开语料推导过程——分数可复现但"为什么这样加权"是黑盒（对比 geolook 公开 references/）。
- 开源层是审计+修复建议，规模化内容生产在闭源云端。
- 英文引擎矩阵，无中文覆盖。

**场景**：给任意网站快速出体检分和 CI 守护；售前评估演示利器。**与本书**：guide/08（30 分钟首查）的自动化版本即此。

## 3. yaojingang/yao-geo-skills（914★ / 175 fork / MIT / push 10-01）

**定位**：24 个细分环节技能包矩阵（战略诊断/页面技术/内容生产/知识资产/监测归因/研究拓词/GEOFlow 运营），每个 skill 带 SKILL.md+manifest+简报模板+eval 触发用例+产物校验。

**优势**：
- **技能工程规范是同类最完整**：每个 skill 强制"边界+接口+eval"三件套（`evals/trigger_cases.json` 校验触发、`expected_artifacts.json` 校验产物），有仓库级校验脚本 `validate_repository.py`——把"prompt 散装"升级成"可验证资产"。
- 中文监测采样细节独有：DeepSeek/豆包 App/Web 重复采样、ChatGPT 采样概率报告进技能化。
- 与 GEOFlow 打通（geo-operations 分类），技能↔平台联动。

**不足**：
- 作者矩阵效应：同作者 5 个仓库互相关联，独立口碑样本不足。
- 24 个 skill 质量参差是矩阵型仓库的通病，README 无每个 skill 的实测样例覆盖度。

**场景**：想按环节自由拼装工作流的团队（本书 advanced/08 清单的 skill 化对照）。**与本书**：其"意图簇/监测 Prompt"研究对应 guide/09 冻结问题集方法。

## 4. Fangx-AI/geo-doctor（354★ / 101 fork / MIT / push 11-02 最活跃）

**定位**：中文市场免费"GEO 医生"：一句话安装进助手，八步问诊走完"找差距→批量写发→推荐率复查"。主打豆包/DeepSeek/元宝/千问/文心/Kimi + 海外五引擎，中英双语，不用服务器。

**优势**：
- **中文引擎场景覆盖第一**：明确以国内引擎为优化对象（其他技能包几乎全英文向）；连"豆包 App 装不了技能，采样时再去豆包里问"这类边界都实测并诚实标注（2026-10-14 实测记录）。
- 获客形态最轻：安装=发一句话给 AI；Release 附 zip 上传包；已在 WorkBuddy Windows 桌面端实测跑通。
- 开发活跃：三周 354★、11-02 仍在推送；CI 测试徽章常绿。

**不足**：
- 增速异常需观察但账号未见硬伤；核心方法论沉淀（handbook.md）刚起步，深度未经时间检验。
- "批量发"环节知乎/公众号靠排版后人手点发布，规模化能力弱于 GEOFlow 型平台。
- 免费形态不可持续风险：无可见商业模式，停维护概率高（同 geolook 轨迹）。

**场景**：中文站个人站长/小团队零成本起步。**与本书（竞争警示）**：它与 B2B GEO 服务的"诊断→改→复查"流程正面重合，压工具层定价——本书护城河应锚定中文引用语料一手实算（guide/10）+ 交付方法论（advanced/08、case-studies/04），不与免费技能比工具。

## 5. ViryaZheng/recomby-geo（454★ / 39 fork / MIT / push 07-04 已停）

**定位**："AI 员工方案"组装品：业务专家+Agent+办公 CLI（飞书/钉钉/Slack/Notion）+GEO skills 四块拼图，主战场是 `plugins/recomby-geo/` 下 6 个 skill + 7 阶段协作工作流命令。

**优势**：
- **组装而非造轮子**：6 个 skill 多为 vendor 注明来源（199-biotechnologies/toprank/aaron-he-zhu，MIT/Apache 可商用），血缘诚实标注——这个做法本身值得抄。
- Local-first 主张明确：agent 接本地模型（Ollama/vLLM/LM Studio），办公数据不出本地，直击国内合规刚需。
- "AI 员工≠替代员工"的定位话术清晰：虚拟岗位组装产物，业务专家仍在环。

**不足**：push 停在 2026-07-04，alpha 状态未转正；fork 仅 39，社区薄；核心 skill 是 vendor 搬运+组装，原创深度依赖上游。

**场景**：已用飞书/钉钉做业务协作、要"给 agent 定岗"的国内团队。**与本书**：其办公 CLI 集合（clis.md）是国内 GEO 协作工具选型的一手索引。

## 本篇小结

| 维度 | gtm-engineer | geo-optimizer | yao-geo-skills | geo-doctor | recomby-geo |
|------|-------------|---------------|----------------|------------|-------------|
| 覆盖面 | 全流程管道 | 审计单点深 | 24 环节矩阵 | 中文全流程 | 协作组装 |
| 工程质量 | 中 | **最高(2000+测试)** | 规范最全(eval) | 轻 | 薄 |
| 中文支持 | ✗ | ✗ | ✅ | **✅主打** | ✅ |
| 活跃度 | ✅ | ✅ | ✅ | **✅最活跃** | ⚠️停07-04 |
| 星数可信度 | 正常 | 正常 | 矩阵观察 | 增速快无硬伤 | 正常 |

一句话：**英文审计 Auriti、英文流程 gtm、中文免费 geo-doctor、环节拼装 yao、协作组装 recomby。**

---
*上游：[01 选型地图](01-selection-map.md) ｜ 相关：[02 实施平台](02-implementation-platforms.md)*
