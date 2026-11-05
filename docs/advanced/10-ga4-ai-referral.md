# GA4 配置 AI 引荐流量

> 把"AI 带来的访客"从普通流量里剥出来单独看——这是老板唯一愿意听的 GEO 证据。

## 前提认知

GA4 记录 AI 引荐的条件：用户浏览器携带 referrer（如 chatgpt.com）或 AI 平台给链接加了 UTM。**大量 AI 答案点击不带 referrer**（zero-click 与隐私设置），GA4 天然低估 AI 流量——它是下限，不是全量（wandered.io / maxaeo 口径）。

## 第 1 步：确认 GA4 原生 AI Assistant 渠道

2025 年起 GA4 已内置 **AI Assistants 默认渠道分组**（seoninja 2026 确认）：
- 后台 → 管理 → 自定义设置 → 渠道分组 → 找 "AI Assistants"。
- 若你的属性是新建的，多数已自动生效；老属性确认该分组存在且启用。

## 第 2 步：建自定义渠道组兜底

原生分组覆盖不全时（各引擎 referrer 域名行为不一），手动补：

1. 管理 → 自定义定义 → **渠道分组** → 创建自定义。
2. 匹配条件（会话来源匹配正则）：
```
chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|grok\.com|deepseek\.com|doubao\.com|coze\.cn
```
3. 命中归入自定义渠道"AI Search"。

注意域名清单要随引擎更新季度复查；中文引擎（豆包/元宝）referrer 行为以实测为准——先在"流量获取→所有会话"报表里按来源筛出可疑域名再定正则。

## 第 3 步：建探索报表（Exploration）

自由格式报表：
- 维度：会话来源/媒介 + 落地页 + 设备。
- 指标：会话数、参与会话率、每次会话转化数。
- 对比期：上周 vs 本周、优化上线前 vs 后。

输出物：每引擎每周 AI 会话趋势 + 哪些落地页吃到 AI 流量（这些页面就是被引用的页面，反推引擎偏好继续复制）。

## 第 4 步：主动打 UTM（可控场景）

在你控制的分发渠道（llms.txt 链接、GitHub README、社交媒体 bio）给链接加：
```
?utm_source=ai-interface&utm_medium=llms-txt&utm_campaign=geo
```
无法控制引擎输出链接的 UTM，只能靠 referrer 被动识别——所以 UTM 数据同样是下限。

## 报表节奏

每周固定看：AI 会话数趋势、AI 会话转化率 vs 自然搜索转化率（AI 流量意图更强，转化率通常更高——若不高说明落地页没接住）。

## 延伸阅读

- GA4 AI 流量追踪（含正则）：https://better-ga.com/blog/track-ai-traffic-in-ga4
- Conversios 分步指南：https://www.conversios.io/blog/track-ai-referral-traffic-from-chatgpt-in-ga4/
- 原生 AI Assistant 渠道：https://www.seoninja.com/blog/ai-seo/how-to-track-ai-referral-traffic-in-ga4/
- GA4 识别不到的部分：https://wandered.io/guides/track-ai-traffic-google-analytics

---
*上一篇：[技术可达性实操](09-technical-accessibility.md) ｜ 下一篇：[案例-90天端到端实战](../case-studies/04-end-to-end-90days.md)*
