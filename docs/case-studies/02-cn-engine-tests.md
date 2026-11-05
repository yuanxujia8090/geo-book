# 案例 2：中文引擎实测

> 国产六大引擎引用行为的一手实测数据与研究方法。

## 案例：国产 AI 引擎 GEO 实测研究（2026-08）

- **方法**（jinghao-leon.github.io/geo-research-cn）：12 个标准化问题 × 6 引擎（豆包、DeepSeek、腾讯元宝、通义千问、文心一言、Kimi）单次实测 + 97 次多次采样压噪声。
- **产出**：量化各引擎引用率、信源域名偏好、GEO 渠道打法差异。
- **可复用点**：
  1. 多采样对抗随机性——单次提问结果不能作为决策依据。
  2. 按引擎拆信源偏好——同一内容在不同引擎的引用渠道完全不同（元宝偏公众号、豆包偏头条系）。
- 链接：https://jinghao-leon.github.io/geo-research-cn/

## 案例：本地服务被 AI 略过的原因研究（英文对照，pickedbyagents.com）

- **方法**：对 2,383 个城市收集 AI 助手对 HVAC（暖通空调）本地商家的推荐结果与理由，数据集开源（github.com/gregm711/ai-assistant-hvac-picks）。
- **发现**：AI 略过本地商家的主因是信息缺失与第三方信号弱，而非规模小。
- **含义**：本地生意的 GEO = Google Business Profile +  Yelp/点评类平台 + 结构化官网三件套。
- 链接：https://pickedbyagents.com/reports/why-ai-passes-hvac-contractors

## 案例：X 上的双界面架构实验（@The_Muhib，2026）

- 人看单页落地页；同域名托管数千个结构化 .md 文件供 AI 读取（llms.txt 哲学放大）。
- 属个人实验阶段（探索性自述，置信低），但方向与"AI Interface"思潮一致。
- 链接：https://x.com/The_Muhib/status/2117936346996355462

## 方法论迁移清单

- [ ] 为你的业务定 12-20 个标准问题集。
- [ ] 每引擎采样 ≥3 次取均值。
- [ ] 记录引用域名分布，找出你的目标引擎偏好的信源类型。
- [ ] 把内容铺到偏好渠道，4 周后复测。

---
*上一篇：[AI Overviews 引用研究](01-ai-overview-studies.md) ｜ 下一篇：[品牌 GEO 案例](03-brand-cases.md)*
