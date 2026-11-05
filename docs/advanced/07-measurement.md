# GEO 度量与监测

> 不能测量就不能优化。这一篇定义 GEO 的核心指标与监测方法。

## 核心指标

| 指标 | 定义 | 说明 |
|------|------|------|
| **AI 提及率（mention rate）** | 目标问题集中，AI 回答提到品牌的比例 | 最基础指标，分引擎统计 |
| **引用率（citation rate）** | AI 回答中引用你域名作为来源的比例 | 比提及更硬（带链接） |
| **Share of Voice（SOV）** | 提及中你占的份额（你 vs 竞品） | 竞争视角主指标 |
| **情感（sentiment）** | 提及语境正/负/中 | 提及≠好评 |
| **引用位置** | 品牌出现在答案开头/中段/结尾 | 首屏提及价值更高 |
| **AI 引荐流量** | 从 AI 产品点回网站的会话 | GA4 看 referral：chatgpt.com、perplexity.ai、gemini.google.com |

## 监测方法（从手工到平台）

1. **手工采样**：选 20-50 个真实用户问题（含品牌词、品类词、对比词），每周在各引擎跑一遍记录提及/引用。免费但费力；注意同一问题多次采样（答案有随机性，中文实测研究用 97 次采样就是为了压噪声）。
2. **开源工具**：geo-check、auto-geo 等 CLI 可自动跑引用检测（见[开源项目篇](../tools/02-open-source.md)）。
3. **商业平台**：Profound、Peec、Otterly 等自动追踪 SOV 与趋势（见[商业平台篇](../tools/03-commercial-platforms.md)）。
4. **服务器日志**：grep AI 爬虫 UA（GPTBot/OAI-SearchBot/PerplexityBot）看抓取频次——抓取量是引用量的先行指标。

## 基线先行

做任何优化前先跑 2 周基线：现在各引擎提及率/引用率是多少。没有基线，一切"有效"都是错觉。

## 归因的诚实边界

- AI 回答有随机性，单次结果无意义，看趋势与多次采样均值。
- 多变量同时改无法归因单项——一次改一个变量或接受模糊。
- 引荐流量低估真实影响：多数用户在 AI 产品内完成决策（zero-click）。

## 延伸阅读

- 监测工具横评：https://wikiap.org/en/articles/ai-visibility-monitoring-tools-comparison
- Semrush AI 工具盘点：https://www.semrush.com/blog/best-ai-visibility-tools/
- 度量框架：https://www.promptmonitor.io/blog/generative-engine-optimization
- 平台全景：https://getpromptive.ai/blog-ultimate-guide-geo-platforms-2026

---
*上一篇：[进入 LLM 训练数据](06-training-data-visibility.md) ｜ 下一篇：[工作流与审计清单](08-workflow-checklist.md)*
