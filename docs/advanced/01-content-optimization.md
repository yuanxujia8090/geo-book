# GEO 内容优化：让 AI 想引用的写法

> 内容可引用性（quotability）是 GEO 的第一杠杆。这一篇给可直接套用的写作规范。

## 核心原则：为"被摘录"而写

AI 引用的是**片段**而不是整页。每个关键段落都要能脱离上下文独立成立。

## 八条可落地写法

1. **结论前置（Answer First）**：每个 H2/H3 下第一句话直接回答问题，再展开论证。CXL 研究显示被引片段集中在页面中前部。
2. **问句式标题**：用用户真实提问做小标题（"GEO 需要多久见效？"），与查询句式直接对齐，提升召回命中。
3. **数据锚点**：给出具体数字、百分比、日期。Princeton GEO 论文实测 statistics 是最有效策略之一——AI 偏爱可核查的硬事实。
4. **引用来源**：正文内外链权威机构/论文（added citations 同样是论文实测 Top 策略）。你引用权威，AI 更信你。
5. **引用短语（quoted phrases）**：加入精炼、可整句摘录的金句/定义句。
6. **自包含段落**：段内重复主语，禁用"如上所述""该方法"这类跨段指代——切块后指代全部失效。
7. **结构化呈现**：列表、表格、步骤编号。LLM 解析结构化文本的准确率显著高于长散文。
8. **实体一致性**：品牌名、产品名全文统一拼写，别混用中英文名/缩写——实体混淆会被过滤。

## 内容形态选择

| 形态 | GEO 价值 | 适用 |
|------|---------|------|
| 问答页/FAQ | 高：直对查询句式 | 每个核心问题一页或一节 |
| 对比页（X vs Y） | 极高：AI 被问对比时缺中立信源 | 竞品对比、方案选型 |
| 数据/统计页 | 高：数字锚点富集 | 行业数据汇编、基准测试 |
| 教程/步骤 | 高：HowTo 结构清晰 | 技术产品 |
| 观点散文 | 低：难被摘录 | 品牌叙事保留但别指望引用 |

## 反面清单（会杀死引用）

- 弹窗、正文折叠、懒加载图片承载关键信息（爬虫抓不到）。
- 营销形容词堆砌（"业界领先""颠覆性"）——无可摘录事实。
- 关键数据只放在图片/PDF 里不写进正文。
- 标题党与正文不符——生成期一致性检查会降权。

## 延伸阅读

- Backlinko GEO 指南：https://backlinko.com/generative-engine-optimization-geo
- 8 战术完整版：https://www.enrichlabs.ai/blog/generative-engine-optimization-geo-complete-guide-2026
- 5 步结构化方法：https://developer.aliyun.com/article/1747511
- 三框架实测（改写策略对比）：https://wetheflywheel.com/en/ai-search/generative-engine-optimization/

---
*上一篇：[中文 AI 引擎生态](../guide/07-chinese-ai-engines.md) ｜ 下一篇：[结构化数据与 Schema](02-schema-structured-data.md)*
