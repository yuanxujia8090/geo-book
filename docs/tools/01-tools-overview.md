# GEO 工具总览

> 三类工具：监测（你在 AI 里长什么样）、优化（改写与生成）、审计（技术可达性）。

## 选型速查表

| 需求 | 免费/开源 | 商业 |
|------|----------|------|
| AI 引用监测 | geo-check、auto-geo、手工采样 | Profound、Peec、Otterly、Scrunch |
| 内容 GEO 评分 | GEO-Content-Optimizer-Skill、AutoGEO | Frase、Clearscope、Surfer、Geol.ai |
| 爬虫可达性审计 | geo-check（robots/sitemap/llms.txt 扫描） | Botify、seoClarity |
| 自建分析 | GEOInflow（自托管爬虫分析）、elmo | Conductor、BrightEdge |
| Schema 生成 | technicalseo 生成器、手写 JSON-LD | Schema Pro（WordPress） |
| llms.txt 生成 | mkdocs-llmstxt、手写 | Foglift（免费扫描+API） |

## 选型原则

1. **先免费跑基线**：手工采样 + geo-check 足够起步，别先买 $500/月的平台。
2. **有竞品追踪需求再上商业**：SOV、情感、多引擎自动化是商业平台核心价值。
3. **数据主权敏感选开源自托管**：GEOInflow、elmo 数据留在自己服务器。
4. **中小团队组合**：一个监测（Peec/Otterly 级）+ 一个内容评分（Frase 级）覆盖 80% 需求。

## 工具地图（按管线环节）

```
抓取层: robots 配置 → geo-check / Botify 审计
检索层: 内容结构 → Frase / Clearscope 评分
生成层: 引用测试 → auto-geo / 手工采样
声量层: SOV 追踪 → Profound / Peec / Otterly
```

## 延伸阅读

- 10 平台对比：https://www.gen-optima.com/geo/best-geo-tools-ai-visibility-platforms-2026/
- 中立工具对比：https://wikiap.org/en/articles/ai-visibility-monitoring-tools-comparison
- 诚实横评（含融资背景）：https://www.surmado.com/blog/best-ai-visibility-tools-2026
- Semrush 官方盘点：https://www.semrush.com/blog/best-ai-visibility-tools/

---
*上一篇：[工作流与审计清单](../advanced/08-workflow-checklist.md) ｜ 下一篇：[开源项目](02-open-source.md)*
