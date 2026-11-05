# 主流海外 AI 引擎画像

> 每个引擎的信源偏好不同，GEO 策略要按引擎分轨。

## 引擎对比表

| 引擎 | 检索机制 | 信源偏好 | GEO 重点 |
|------|---------|---------|---------|
| **ChatGPT Search** | OAI-SearchBot 实时检索 + Bing 索引历史依赖 | 权威媒体、Wikipedia、Reddit；2025-02 起全用户可用 | 放行 OAI-SearchBot；被 Bing 收录仍重要；Reddit 声量 |
| **Google AI Overviews / AI Mode** | Gemini + Google 搜索索引 RAG | 强依赖自然排名（97% 引用来自 top 20）；FAQ/列表结构 | SEO 地基优先；答案片段化；Schema |
| **Perplexity** | 自有爬虫 PerplexityBot + 实时检索 | 新鲜内容容忍度高、论坛/评测站友好、引用透明 | 放行爬虫；被评测/对比文章收录；llms.txt 采纳较早 |
| **Gemini** | Google 索引 + 训练知识混合 | 与 AI Overviews 高度重叠，多模态权重 | 同 AI Overviews 打法 |
| **Grok** | 深度绑定 X.com 实时数据 | X 上的讨论、发帖、长文 Article | 在 X 建立品牌讨论阵地是 Grok 独有入口 |
| **Copilot** | Bing 索引 + ChatGPT | Bing Webmaster 体系 | Bing 收录、IndexNow 提交 |

## 值得记住的差异

1. **X 是 Grok 的护城河**：品牌在 X 上的真实讨论会直接影响 Grok 回答——这是唯一以社交平台为第一信源的主流引擎。
2. **Perplexity 是小站最大机会**：对新鲜、小众、深度内容最友好，引用格式清晰，适合新站冷启动验证 GEO 效果。
3. **AI Overviews 是 SEO 的延长线**：没有自然排名基本没有引用资格，先做好传统 SEO。
4. **2026 数据点**：Google AI Mode 月活已破 10 亿（awesome-geo 汇编口径，medium 置信）。

## 引擎覆盖率建议

做 GEO 监测时至少覆盖：ChatGPT、Google AI Overviews、Perplexity、Gemini 四家（占查询量绝大多数），B2B 加 Claude，社交驱动品牌加 Grok。

## 延伸阅读

- 引擎对比（B2B 视角）：https://mydigipal.com/en/blog/geo-vs-seo-2026-rank-chatgpt-perplexity-ai-overviews
- 完整平台指南：https://rankscope.ai/blog/complete-guide-generative-engine-optimization-2026
- 三框架实测对比（GEO/AEO/LLM-SEO）：https://wetheflywheel.com/en/ai-search/generative-engine-optimization/

---
*上一篇：[AI 引用机制](05-how-ai-engines-cite.md) ｜ 下一篇：[中文 AI 引擎生态](07-chinese-ai-engines.md)*
