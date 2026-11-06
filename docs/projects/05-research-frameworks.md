# 研究框架与数据集深析：AutoGEO / GEOLab / E-GEO / SafeGEO / AgenticGEO / MAGEO

> 物种定义见 [01 选型地图](01-selection-map.md)。这一组不卖工具，产出的是**机理、规则和可复算的数据**——本书多个章节的量化结论溯源到这里。
> 数据 GitHub API 一手核验于 2026-11-06。

## 1. cxcscmu/AutoGEO（236★ / MIT / ICLR 2026）

CMU 团队（Chenyan Xiong 组）的自动 GEO 框架：从引擎行为自动提取偏好规则→按规则重写→双指标（GEO score 可见度 × GEU score 效用）评估。完整方法拆解见本库 [advanced/14 引擎偏好规则与内容重写](../advanced/14-preference-rules-rewriting.md)，本篇只记选型要点：

- **拿它做什么**：① 读论文搞清"偏好可提取"的实证边界；② 三个数据集（E-commerce/GEO-Bench/Researchy-GEO，HF 公开）直接下载复算；③ Qwen1.7B checkpoints 可本地跑（oMLX 类工具可载）。
- **不足**：研究代码非产品；换引擎须重挖规则重训（README 原文警告）；训练 Mini 要 2×A100（自报）。
- **活跃度**：push 停 2026-06-14——论文项目正常节奏，数据集与结论长期可用。

## 2. yaojingang/GEOLab（749★ / ⚠️双层许可 / 活跃 push 11-05）

**中文 GEO 最重要的一手数据源**：本库 guide/10（中文信源实测榜）、advanced/11（量化判据）的数字底座。

- **内容**：五分区——01-experiments（602 prompts/21,143 citations 跨平台实验+分析脚本）、02-papers（54 篇 GEO/AEO 论文导航）、03-datasets（CN-GEO：187,818 条中文引用去重记录、12 平台终端）、04-whitepapers、05-articles。
- **许可细节（API=NOASSERTION 的真相，已读 LICENSE 原文）**：**软件部分 MIT（LICENSE-CODE）+ 原创内容 CC BY 4.0（LICENSE-CONTENT）**双层许可；第三方论文 PDF/数据集保留原条款。结论：脚本可商用，数据引用须署名，论文 PDF 别整包转发。
- **不足（本库已如实转述的缺陷）**：缺采集时间与模型版本字段 → 趋势类结论不可用，只能做横截面分析。
- **场景**：duckdb 复算中文引用份额、按引擎×渠道交叉出客户报告的数据层。**这是中文 GEO 领域目前唯一大规模公开引用语料，护城河素材。**

## 3. psbagga17/E-GEO（50★ / 未标许可 / push 07-03）

电商场景的 GEO 测试床（testbed）：标准化评测商品内容在生成式引擎中的可见度。mverab/eGEOagents（217★，MIT，活跃 push 11-05）是其工程化延伸——把电商 GEO 做成可跑的多 agent 工具箱。

- **价值**：电商 SKU 级 GEO 是稀缺细分（多数工具做到品牌/域名级）；品类问题集设计可借。
- **不足**：无许可证声明的仓库在法律上默认保留所有权利——用代码前先提 issue 求确认；样本小、社区小。

## 4. QianfengWen/SafeGEO（10★ / Apache-2.0 / EMNLP 2026）

**GEO 攻防视角的稀缺品**：把 GEO 操纵当成攻击面，在 LLM 推荐代理上做安全 benchmark（含对抗数据集）。

- **价值**：给"黑帽 GEO 会被怎么反制"提供学术测量（呼应 advanced/08 常见坑第 5 条 GEO-Bench 警告）；做客户服务时，它论证了"为什么走白帽"——不是道德洁癖，是被反制即归零。
- **不足**：★10/fork 14，几乎无社区；论文期项目。

## 5. AIcling/agentic_geo（46★ / Apache-2.0）与 Wu-beining/MAGEO（37★ / ACL 2026）

自进化 agent 系（AgenticGEO）与多 agent 可复用策略学习（MAGEO）：把 GEO 当 agent 长期任务做方法研究。当前均为论文附属仓库，跟踪价值>使用价值；MAGEO 的"策略复用"思路与本书工单制（advanced/08）在理念上同路，可对照读。

## 选型建议

- **要数据**：GEOLab（先看清双层许可）→ duckdb 复算路径本库 guide/10 已给。
- **要方法**：AutoGEO 论文+advanced/14 的三层递减落地法。
- **要反制证据**：SafeGEO + GEO-Bench（arXiv:2605.29107）组合拳，客户问"能不能走捷径"时的标准答案素材。

## 与本书章节的映射表

| 研究仓库 | 支撑本库章节 |
|---------|-------------|
| AutoGEO | advanced/14、reverse/01 手法 4 |
| GEOLab | guide/10、advanced/11、SUMMARY 速记 4/5/7 条 |
| E-GEO/eGEOagents | advanced/01 内容形态表（电商变体） |
| SafeGEO | advanced/08 常见坑 5 |

---
*上游：[01 选型地图](01-selection-map.md) ｜ 深读方法层：[advanced/14](../advanced/14-preference-rules-rewriting.md)*
