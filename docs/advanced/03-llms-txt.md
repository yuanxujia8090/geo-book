# llms.txt 实战

> 给 LLM 的一张"网站导览图"：提案是什么、支持现状如何、怎么生成。

## 提案内容

- **提出者**：Jeremy Howard（Answer.AI 创始人），2024-09 发布，2026-08 修订为 v2（llmstxt.org 官方）。
- **格式**：网站根目录放一个 `/llms.txt` Markdown 文件，包含：
  - `# 站点名`（唯一必需的 H1）
  - `> 引用块简介`
  - 背景/上下文段落
  - `## Sections` 分组链接列表，每个链接附一句话说明
  - 可选 `## Optional` 段：次要链接
- **配套约定**：尽量提供内容的 Markdown 版本（如 `page.md` 或 `page.html` + 同名 `.md`），让 LLM 跳过 HTML 解析噪声。
- **动机**：LLM 上下文窗口装不下整站；llms.txt 是人工精选的"值得读"地图， inference 时直接投喂。

## 模板

```markdown
# MyBrand

> AI-powered CRM for small teams. 一句话说明本站是干什么的。

## Docs
- [Getting Started](https://example.com/docs/start.md): 5 分钟上手指南
- [Pricing](https://example.com/pricing.md): 定价方案与对比

## Optional
- [Blog](https://example.com/blog): 技术博客
```

## 现状与争议（诚实口径）

- **支持侧**：Perplexity 等引擎被报道消费 llms.txt 信号；大量框架插件已内置生成（mkdocs-llmstxt、Next.js/Fastro 插件等）。
- **怀疑侧**：OpenAI/Google 未官方确认将其纳入检索权重；有分析指出主流引擎多数忽略该文件（clickcentricseo 梳理）。llms.txt 更像"低成本期权"：做了不亏，别指望单点起效。
- **务实定位**：llms.txt 解决"喂给 Agent 的上下文"问题多于"排名"问题——对文档站、API 站、被编程 Agent 访问的站点价值最高。

## 架构实验（X 一手观察）

X 用户 @The_Muhib 的 GEO 架构实验（2026）：**双界面网站**——人看极简落地页，AI 读托管在同域名下的数千个结构化 .md 文件（llms.txt 哲学的放大版）。值得做内容型站点参考。

## 生成工具

- mkdocs-llmstxt（GitHub 插件）：https://github.com/pawamoy/mkdocs-llmstxt
- 手写即可：本质是一个 Markdown 文件，10 分钟工作量。

## 延伸阅读

- 官方提案 v2：https://llmstxt.org/
- 2026 完全指南：https://llmpulse.ai/blog/llms-txt-guide/
- 格式与局限：https://clickcentricseo.com/learn/llms-txt-guide

---
*上一篇：[Schema 结构化数据](02-schema-structured-data.md) ｜ 下一篇：[E-E-A-T 与权威信号](04-eeat-authority.md)*
