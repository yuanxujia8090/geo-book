# 结构化数据与 Schema

> JSON-LD 是给机器的"标准答案卡"：把实体、关系、答案用标准词汇表声明出来。

## 为什么 Schema 对 GEO 有用

- LLM 检索管线解析 JSON-LD 比解析渲染后的 HTML 准确得多：实体（Organization、Person）、问答（Q&A）、步骤（HowTo）直接是机器可读三元组。
- Google 官方立场：结构化数据不保证排名，但帮助理解内容；AI Overviews 的 RAG 管线同样消费这些信号（stackmatix 分析）。
- 前端类比：Schema 像 TypeScript 的类型声明——HTML 是 any，JSON-LD 是 interface，机器拿到类型才敢用。

## GEO 优先的 Schema 类型

| 类型 | 用途 | 优先级 |
|------|------|--------|
| FAQPage | 问答对直接喂给答案引擎（用量已达百万-千万级域名，schema.org 2026-08 统计） | ★★★ |
| Article / NewsArticle | 作者、发布时间、发布者实体 | ★★★ |
| Organization | 品牌实体锚点：name/logo/sameAs | ★★★ |
| Person | 作者 E-E-A-T 信号 | ★★ |
| HowTo | 步骤化教程 | ★★ |
| Product / Offer | 电商 GEO | ★★ |
| DefinedTerm | 术语定义页，术语类查询命中率高 | ★★ |
| BreadcrumbList | 站点结构理解 | ★ |

## FAQPage JSON-LD 模板

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "GEO 和 SEO 有什么区别？",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "SEO 优化传统搜索结果页排名；GEO 优化 AI 生成式引擎回答中的引用与提及。GEO 以 SEO 为地基，叠加检索层与生成层优化。"
    }
  }]
}
```

要点：`text` 字段就是 AI 可直接摘录的答案——写成自包含完整句。

## 注意事项

- Google 对 FAQ 富结果展示有资格限制（政务/医疗优先等政策波动），展示受限 ≠ 对 AI 解析无效，两者分开评估（squin.org 2026-03 梳理）。
- 标记内容必须与可见正文一致，虚假标记是垃圾信号。
- 用 Google Rich Results Test 验证语法。
- React/Next.js 项目：`next-seo` 或直接 `<script type="application/ld+json">` 注入均可（aeoscore.io 有各框架代码示例）。

## 延伸阅读

- schema.org 官方：https://schema.org/
- FAQPage 类型：https://schema.org/FAQPage
- AEO Schema 选型：https://searchatlas.com/blog/schema-for-aeo/
- 可直接复制的多类型代码：https://alicelabs.ai/en/insights/schema-org-for-ai
- Rich Results Test：https://search.google.com/test/rich-results

---
*上一篇：[内容优化](01-content-optimization.md) ｜ 下一篇：[llms.txt 实战](03-llms-txt.md)*
