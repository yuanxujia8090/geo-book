# AI 爬虫与抓取（robots.txt 决策）

> 先让机器进得来，才谈得上被引用。这一篇认清主要 AI 爬虫并做出放行/拦截决策。

## 主要 AI 爬虫名录

| 爬虫 | 归属 | 用途 |
|------|------|------|
| GPTBot | OpenAI | ChatGPT 训练数据采集 |
| OAI-SearchBot | OpenAI | ChatGPT Search 实时检索（不用于训练） |
| ChatGPT-User | OpenAI | 用户实时触发的抓取 |
| ClaudeBot | Anthropic | Claude 训练/抓取 |
| Claude-SearchBot / Claude-User | Anthropic | 检索与实时抓取分离 |
| PerplexityBot | Perplexity | 答案引擎索引 |
| Perplexity-User | Perplexity | 实时用户请求抓取 |
| Google-Extended | Google | 区分于 Googlebot：控制是否进入 Gemini/训练管道 |
| Applebot-Extended | Apple | Apple AI 功能扩展 |
| CCBot | Common Crawl | 开源数据集，被各家间接使用 |
| Bytespider | 字节跳动 | 训练采集 |

要点：**训练用爬虫与检索用爬虫已分离**（2025-2026 行业共识）。拦截 GPTBot ≠ 拦截 ChatGPT Search；拦截 Google-Extended ≠ 拦截 Googlebot 排名。

## 2026 年头部网站的主流策略

据对 Top 1000 站点的行为研究（presenc.ai，2026）：最常见策略是**拦截纯训练爬虫（GPTBot、ClaudeBot、CCBot），放行答案引擎爬虫（OAI-SearchBot、PerplexityBot、Google-Extended）**——既保护训练数据主权，又保留 AI 引用曝光。

另一视角（alicelabs.ai）：全拦截会直接降低 LLM 引用潜力，多数企业在 2024-2026 选择放行检索类爬虫。

## 决策框架

1. **内容是否有授权价值**（数据新闻、独家报告）→ 考虑拦训练、放检索。
2. **是否需要 AI 曝光获客**（绝大多数商业站）→ 至少放行全部检索类爬虫。
3. **成本问题**：爬虫打爆昂贵路由（如 GitLab 管理员对 /-/blame 返回 403 的案例）→ 用限速而非全拦。

## robots.txt 示例

```
# 允许答案引擎检索
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

# 拦截训练采集
User-agent: GPTBot
Disallow: /
User-agent: CCBot
Disallow: /

# 传统搜索照常
User-agent: Googlebot
Allow: /
```

注意：**CDN 层（Cloudflare 等）有独立的"AI bot 拦截"开关，robots.txt 写了放行仍可能被 CDN 拦**——需两边核对（验证方法见[技术可达性实操](../advanced/09-technical-accessibility.md)的 UA 差异探测）。

## robots.txt 的三种隐形封禁（RFC 9309 语义，逐行正则会漏）

多数在线检测工具按行正则判断，会漏掉三种真实存在的封禁形态：

1. **通配符连坐**：`User-agent: * / Disallow: /` 会封掉**所有没有专属组的 AI 爬虫**——最常见的"无意封禁"：你以为只拦了垃圾爬虫，实际把 PerplexityBot 也关了。
2. **共享 UA 组**：多个 `User-agent:` 行共享一组规则时，逐行正则会把第二个 UA 判成空规则，误报"已放行"。
3. **特异性覆盖**：专属组存在时通配符组整组失效——写了 `User-agent: GPTBot / Allow: /`，GPTBot 就无视通配符组里的任何 Disallow（想拦也拦不住）。

**robots 放行 ≠ 真放行**：WAF/CDN（Cloudflare Bot Fight、阿里云 WAF）可对 AI 爬虫 UA 单独返回 403，浏览器里一切正常，站长自己看不出来。必须用真实 UA（GPTBot/ClaudeBot/PerplexityBot）逐个抓一次首页做差异探测。

**X-Robots-Tag 响应头 noindex**：页面源码里看不到，常是 CDN/中间件全局注入，最容易带病上线——检查响应头而不只查 meta。

## 延伸阅读

- GPTBot 抓取机制（2026）：https://georion.app/blog/how-gptbot-crawls-websites-in-2026-block-or-allow
- AI 爬虫管理指南：https://alicelabs.ai/en/insights/ai-crawler-management
- Top1000 站点拦截行为研究：https://presenc.ai/research/ai-crawler-behavior-on-top-1000-sites-2026
- AI 爬虫流量统计：https://www.digitalapplied.com/blog/ai-crawler-bot-traffic-statistics-2026-data-reference

---
*上一篇：[AI 搜索的工作原理](03-how-ai-search-works.md) ｜ 下一篇：[AI 引用机制](05-how-ai-engines-cite.md)*
