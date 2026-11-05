# AI 搜索的工作原理（RAG 入门）

> 不理解 RAG，GEO 就是玄学。这一篇讲清 AI 引擎从查询到引用的完整管线。

## 小白版

AI 搜索像开卷考试：
1. 你提问（query）。
2. 系统先去"书库"里翻出最相关的几页纸（检索）。
3. 把这几页纸和你的问题一起塞给"考生"（LLM）。
4. 考生用自己的话写出答案，并标注抄自哪页纸（引用）。

GEO 就是让你的"页纸"更容易被翻到、更容易被采信。

## 专业版：RAG 管线四步

RAG = Retrieval-Augmented Generation = 检索增强生成，AI 搜索的底层架构（奠基论文 arXiv:2005.11401）。

```
网页 → [Ingestion 摄取] → [Chunking 切块] → [Embedding 向量化] → 向量库
用户query → [Retrieval 检索] → [Rerank 重排] → [Augmentation 拼装上下文] → [Generation 生成+引用]
```

1. **Ingestion + Chunking（摄取与切块）**：爬虫抓取网页，切成几百 token 的块（chunk）。标题层级、列表、表格边界都会影响切块质量——结构混乱的页面切出残缺语义块。
2. **Embedding（嵌入/向量化）**：用嵌入模型把每个块映射成高维向量（如 2560 维），语义相近的文本向量距离近。
3. **Retrieval + Rerank（检索与重排）**：查询向量化后在向量库做相似度搜索（常混合 BM25 关键词检索），再经重排模型选出 top-k 块。
4. **Generation（生成）**：LLM 基于选中的块合成答案。系统提示通常要求标注来源，引用标记（[1][2]）即来自这一步的上下文编号。

## 对 GEO 的直接推论

| 管线环节 | GEO 动作 |
|---------|---------|
| 切块 | 每段自包含：小标题+完整答案，别让关键句依赖上文 |
| 嵌入 | 关键词自然密集、语义清晰，避免营销黑话 |
| 检索 | 覆盖用户真实提问句式（问句式标题） |
| 重排 | 权威信号、新鲜度、数据密度影响排序 |
| 生成 | 可摘录性（quotability）：简洁、可独立引用的句子更易被 cite |

## 两种满足查询的方式

- **实时检索（live retrieval）**：引擎现场搜网再答（Perplexity、ChatGPT Search、AI Overviews）。GEO 见效快。
- **参数记忆（parametric memory）**：答案来自训练数据（模型"记得"你）。见效慢但持久，见[进阶-训练数据](../advanced/06-training-data-visibility.md)。

## 延伸阅读

- RAG 奠基论文：https://arxiv.org/abs/2005.11401
- Databricks RAG 工作流详解：https://www.databricks.com/blog/rag-workflow
- RAG 管线深度解析：https://dev.to/derrickryangiggs/rag-pipeline-deep-dive-ingestion-chunking-embedding-and-vector-search-2877

---
*上一篇：[GEO vs SEO vs AEO](02-geo-vs-seo-vs-aeo.md) ｜ 下一篇：[AI 爬虫与抓取](04-ai-crawlers.md)*
