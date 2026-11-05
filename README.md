# GEO 知识库（GEO Book）

> Generative Engine Optimization 生成式引擎优化 —— 让 ChatGPT、Perplexity、Google AI Overviews 等 AI 引擎引用你的内容、提及你的品牌。

从零开始系统学习 GEO：基础知识 → 优化实践 → 工具与开源项目 → 案例分析。

## 为什么要学 GEO

- AI 搜索（ChatGPT、AI Overviews、豆包、Kimi）正在分流传统搜索流量，用户越来越多地直接看 AI 生成的答案而不是点蓝色链接。
- Princeton 论文实测：应用 GEO 方法可将内容在生成式引擎回答中的可见度提升最高 40%（来源见 [01-what-is-geo.md](docs/guide/01-what-is-geo.md)）。
- GEO 不是替代 SEO，而是在 SEO 之上叠加"让机器读懂、信任并引用"的一层。

## 目录

### 一、入门指南（docs/guide/）

| 文档 | 一句话简介 |
|------|-----------|
| [01 什么是 GEO](docs/guide/01-what-is-geo.md) | GEO 的定义、起源（Princeton KDD 2024 论文）、为什么重要。 |
| [02 GEO vs SEO vs AEO](docs/guide/02-geo-vs-seo-vs-aeo.md) | 三个概念的区别与联系，一张表看懂各自优化什么。 |
| [03 AI 搜索的工作原理](docs/guide/03-how-ai-search-works.md) | RAG、Embedding、向量检索：AI 引擎如何找到并用你的内容。 |
| [04 AI 爬虫与抓取](docs/guide/04-ai-crawlers.md) | GPTBot、ClaudeBot、PerplexityBot 是谁、robots.txt 该放行还是拦截。 |
| [05 AI 引用机制](docs/guide/05-how-ai-engines-cite.md) | AI 引擎选中并引用一个来源的决策链路：检索、可信度、片段匹配。 |
| [06 主流海外引擎画像](docs/guide/06-major-engines.md) | ChatGPT Search / AI Overviews / Perplexity / Gemini / Grok 各自的信源偏好。 |
| [07 中文 AI 引擎生态](docs/guide/07-chinese-ai-engines.md) | 豆包、DeepSeek、Kimi、元宝的引用行为差异与中文 GEO 打法。 |

### 二、进阶实践（docs/advanced/）

| 文档 | 一句话简介 |
|------|-----------|
| [01 GEO 内容优化](docs/advanced/01-content-optimization.md) | 结论前置、问答式标题、数据锚点：让 AI 想引用的内容写法。 |
| [02 结构化数据与 Schema](docs/advanced/02-schema-structured-data.md) | FAQPage、Article、Organization 等 JSON-LD 怎么标才有帮助。 |
| [03 llms.txt 实战](docs/advanced/03-llms-txt.md) | Jeremy Howard 提案的格式、现状争议与生成工具。 |
| [04 E-E-A-T 与权威信号](docs/advanced/04-eeat-authority.md) | 经验、专业、权威、可信：AI 判断"值不值得引用"的信号体系。 |
| [05 第三方声量建设](docs/advanced/05-third-party-presence.md) | Reddit、Wikipedia、评测站：AI 训练与检索偏好的第三方阵地。 |
| [06 进入 LLM 训练数据](docs/advanced/06-training-data-visibility.md) | 长期层：Common Crawl、数据授权协议与品牌沉淀。 |
| [07 GEO 度量与监测](docs/advanced/07-measurement.md) | AI 提及率、引用份额、Share of Voice：怎么量化 GEO 效果。 |
| [08 GEO 工作流与审计清单](docs/advanced/08-workflow-checklist.md) | 从诊断到执行到复测的完整落地流程与可复制清单。 |

### 三、工具与开源项目（docs/tools/）

| 文档 | 一句话简介 |
|------|-----------|
| [01 工具总览](docs/tools/01-tools-overview.md) | 监测/优化/审计三类工具选型速查表。 |
| [02 开源项目](docs/tools/02-open-source.md) | GitHub 高星 GEO 项目：AutoGEO、GEOInflow、elmo、geo-check 等。 |
| [03 商业监测平台](docs/tools/03-commercial-platforms.md) | Profound、Peec、Otterly、Semrush AIO 等商业平台对比。 |

### 四、案例分析（docs/case-studies/）

| 文档 | 一句话简介 |
|------|-----------|
| [01 AI Overviews 引用研究](docs/case-studies/01-ai-overview-studies.md) | CXL、Wellows 等机构的引用数据研究说明了什么。 |
| [02 中文引擎实测案例](docs/case-studies/02-cn-engine-tests.md) | 国产六大引擎 12 题实测：引用率与信源偏好一手数据。 |
| [03 品牌 GEO 案例](docs/case-studies/03-brand-cases.md) | Wikipedia 效应 3.2 倍提及、HVAC 本地案例等可借鉴打法。 |

## 学习路径

**零基础（第 1-2 周）**：guide/01 → 02 → 03 → 04 → 05，先建立"AI 怎么找到并引用内容"的心智模型。

**上手优化（第 3-4 周）**：advanced/01 → 02 → 03 → 08，边学边改自己的网站。

**放大与度量（第 5 周起）**：advanced/04 → 07，配合 tools/ 选一个监测工具跑基线。

**长期建设**：advanced/05 → 06，第三方声量与训练数据是慢变量，越早开始越好。

## 资料口径说明

- 所有数据均标注来源链接；标注"自报数据"的是厂商营销口径，未经独立核验。
- GitHub star 数核验于 2026-11-05。
- 本库以英文一手资料为主（arXiv / GitHub / X.com），中文生态单独成篇。

## 项目结构

```
geo-book/
├── README.md            # 本文件：总目录 + 每篇一句话简介
├── SUMMARY.md           # 学习路径与内容总结
└── docs/
    ├── guide/           # 入门指南（7 篇）
    ├── advanced/        # 进阶实践（8 篇）
    ├── tools/           # 工具与开源项目（3 篇）
    └── case-studies/    # 案例分析（3 篇）
```

---

**最后更新**：2026-11-05
