# AI 引用机制：引擎如何选中一个来源

> 被检索到 ≠ 被引用。这一篇拆解从召回到 cite 的决策链。

## 引用决策链

```
查询 → 召回候选(top 数十) → 可信度过滤 → 片段匹配 → 生成时决定 cite 谁
```

1. **召回**：向量/关键词混合检索给出候选集——先决条件是内容可抓取、语义匹配（见[爬虫篇](04-ai-crawlers.md)）。
2. **可信度过滤**：域名权威、作者实体、站点一致性、发布新鲜度。黑盒但方向明确：AI 偏好"看起来可负责"的来源。
3. **片段匹配**：答案片段与查询的语义贴合度。页面里必须存在能直接回答问题的自包含段落。
4. **生成期选择**：LLM 在合成时倾向引用：给出具体数字/定义/步骤的片段 > 观点性泛泛内容。

## 关键实测数据（标注来源）

- **97% 的 Google AI Overviews 引用来自自然排名前 20 的页面；但排名 #1 的页面也只有约 12% 真的被引用**（shadow.inc，2026）——SEO 是必要地基，排名高不保证引用。
- 2025 年中约 75% AI Overview 引用来自前 10 自然结果，2026 年初该比例发生变化，引用来源放宽（toolsolved.com 分析，medium 置信）。
- CXL 对 100 条 AI Overview 引用的定位研究：被引用的片段多位于页面**中前部的直接回答区**，而非文末（cxl.com，2026-03）。
- Wellows 分析 15,847 条 AI Overview 结果归纳 7 大引用因素（wellows.com，厂商自报口径，medium 置信）。

## 提高被 cite 概率的杠杆（按管线归位）

| 杠杆 | 作用环节 | 具体做法 |
|------|---------|---------|
| 答案前置 | 片段匹配 | 每个 H2 下第一段直接给结论 |
| 数据锚点 | 生成期选择 | 具体数字、百分比、日期，AI 爱抄可核查事实 |
| 引用他人 | 可信度 | 外链权威来源（Princeton 论文：added citations 是最有效策略之一） |
| 自包含段落 | 召回+匹配 | 段内重复主语，不依赖"如上所述" |
| 新鲜度 | 可信度 | 更新时间戳、定期刷新数据 |
| 实体清晰 | 可信度 | Schema 标注 Organization/Person，让 AI 知道"谁在说" |

## 延伸阅读

- AI Overview 引用来源分析：https://www.stackmatix.com/blog/ai-overview-citation-analysis
- 100 页引用位置研究：https://cxl.com/blog/google-ai-overview-citation-sources/
- 被引用指南：https://www.shadow.inc/resources/cited-google-ai-overviews

---
*上一篇：[AI 爬虫与抓取](04-ai-crawlers.md) ｜ 下一篇：[主流海外引擎画像](06-major-engines.md)*
