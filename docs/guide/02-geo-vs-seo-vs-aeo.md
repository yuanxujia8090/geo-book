# GEO vs SEO vs AEO

> 三个概念优化的是同一条链路上的不同环节，不是互相替代关系。

## 三者定义

| 维度 | SEO（Search Engine Optimization 搜索引擎优化） | AEO（Answer Engine Optimization 答案引擎优化） | GEO（Generative Engine Optimization 生成式引擎优化） |
|------|------|------|------|
| 优化对象 | Google/Bing 传统搜索结果页（SERP） | 答案框、精选摘要、语音助手等"直接给答案"的入口 | ChatGPT、Perplexity、AI Overviews 等 LLM 生成式引擎 |
| 成功标志 | 排名进前十、获得点击 | 内容被摘为答案 | 内容被引用/品牌被提及于 AI 生成的回答中 |
| 用户行为 | 点击链接到站 | 看完答案即走 | 与 AI 对话中消费合成信息 |
| 核心手段 | 关键词、外链、技术 SEO | 问答结构、精选摘要片段 | 语义完整、可信信号、结构化、多阵地引用 |
| 时间尺度 | 周-月 | 周-月 | 即时检索层：天-周；训练数据层：季度-年 |

## 关系怎么理解

- 前端类比：SEO 像"让搜索引擎收录并排序你的页面"，GEO 像"让 LLM 的 RAG 检索管线召回你的 chunk，并且生成时愿意 cite 你"。AEO 介于两者之间，聚焦"答案"这个展示形态。
- 业界观点（存在争议）：有从业者认为 GEO/AEO 本质上就是 SEO 在 RAG 管线里的延伸，术语是营销造词（X 上 @Hobo_Web 的 "3 Laws of AI SEO" 论点：GEO 若独立存在，必须住在 RAG 管线的某个环节里）。务实结论：**不管叫什么，检索层 + 生成层两个环节都要优化**。
- 共识部分：GEO 不要求放弃 SEO——AI Overviews 的引用绝大多数仍来自自然排名前 20 的页面（见 [AI 引用机制](05-how-ai-engines-cite.md)）。

## 一个查询的三层竞争

用户问"最好的 CRM 软件"：
1. **SEO 层**：谁排在 Google 前十（拿到点击）。
2. **检索层**：谁的内容被向量检索召回进 AI 上下文（拿到入场券）。
3. **生成层**：LLM 合成答案时引用谁、提及谁（拿到最终曝光）。

GEO 同时打第 2、3 层，且第 1 层是它的地基。

## 延伸阅读

- seo.com 对比指南：https://www.seo.com/ai/geo-vs-seo/
- systemsarchitect 定义：https://systemsarchitect.net/geo-vs-seo-generative-engine-optimization/
- X 讨论（GEO 是否冗余）：https://x.com/Hobo_Web/status/2114455504994877902

---
*上一篇：[什么是 GEO](01-what-is-geo.md) ｜ 下一篇：[AI 搜索的工作原理](03-how-ai-search-works.md)*
