# 什么是 GEO（Generative Engine Optimization）

> 生成式引擎优化：让 AI 搜索引擎在生成答案时引用、提及你的内容。

## 一句话定义

GEO 是通过组织、结构化、增强内容，使生成式引擎（Generative Engine，简称 GE，即基于大语言模型的搜索/问答引擎）在回答用户问题时更愿意检索、信任并引用你的内容的优化实践。

## 概念起源

- 术语由论文 **《GEO: Generative Engine Optimization》**（arXiv:2311.09735）正式提出，2023 年 11 月发布，发表于 KDD 2024（ACM 知识发现与数据挖掘顶会），作者来自 Princeton、IIT Delhi、Allen Institute for AI 等机构。
- 论文核心结论（已核验摘要原文）：
  - 提出"生成式引擎（GE）"统一框架：整合多来源信息 + LLM 总结来回答用户查询。
  - 提出 **GEO-bench** 基准：跨多领域的多样化用户查询 + 相关网页来源。
  - 实测 GEO 策略可将内容在生成式引擎回答中的**可见度提升最高 40%**。
  - 关键限定：**策略效果因领域而异**，需要领域特定的优化方法。
- 论文提出 9 类黑盒优化策略，效果最显著的包括：加入引用来源（added citations）、加入统计数据（statistics）、加入引用短语（quoted phrases）；提升权威机构/作者权威度（authority、source authority）同样有效。

## 为什么重要

1. **流量入口迁移**：用户越来越多直接在 ChatGPT、Google AI Overviews、豆包里得到答案，不再点击蓝色链接（zero-click 零点击搜索）。
2. **内容创作者失控**：生成式引擎是黑盒，内容何时、以何种方式被展示，创作者原本毫无控制权——GEO 就是夺回一部分控制权的方法论。
3. **AI 推荐 = 新信任背书**：被 AI 引用/推荐相当于一次自动化背书，对品牌获客、B2B 线索影响直接。

## GEO 优化对象

| 对象 | 目标 |
|------|------|
| 网页内容 | 被检索命中、被选为引用来源 |
| 品牌 | 被 AI 提及（mention）、推荐 |
| 结构化数据 | 被机器准确解析 |
| 第三方阵地 | Reddit/Wikipedia/评测站形成包围式信源 |

## 延伸阅读

- 原始论文：https://arxiv.org/abs/2311.09735
- ACM 页面：https://dl.acm.org/doi/10.1145/3637528.3671900
- Awesome GEO 论文清单：https://github.com/luka2chat/awesome-geo

---
*来源核验于 2026-11-05。这是全库第一篇，从这里开始 → 下一篇：[GEO vs SEO vs AEO](02-geo-vs-seo-vs-aeo.md)*
