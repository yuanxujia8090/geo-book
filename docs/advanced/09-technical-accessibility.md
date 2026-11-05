# 技术可达性实操：让爬虫真正拿到内容

> robots.txt 放行只是"允许进门"，这一篇解决"门开了但屋里没东西"——JS 渲染、验证、提交索引。

## 关键事实（先记住）

**多数 AI 爬虫不执行 JavaScript**（clienvora 2026 清单结论）：Google 有第二波 headless Chromium 渲染，但 GPTBot/PerplexityBot 等大多只读原始 HTML。React/Vue CSR（客户端渲染）站点的正文对 AI 直接隐身——这是新手最容易踩且完全不自知的坑。

## 第 1 步：判断你的站点是否"对 AI 隐身"

```bash
# 拿原始 HTML（不执行 JS），搜正文关键词
curl -s https://你的域名/关键页 -A "Mozilla/5.0" > page.html
grep -c "页面正文里必然存在的词" page.html
```

- **命中 >0**：内容是服务端输出的（SSR/SSG/传统渲染），基本安全。
- **命中 =0 且页面明显有内容**：CSR，AI 看不到你的正文 → 必须修。

辅助判断：查看 HTML 里是否有 `<div id="root"></div>` 空壳 + 大段 `<script>`——典型 CSR 特征。

## 第 2 步：修复渲染（按成本选型）

| 方案 | 适用 | 成本 |
|------|------|------|
| **SSG**（构建期出静态 HTML）：Next.js export / Astro / Hugo | 内容型站点、文档站 | 低，首选 |
| **SSR**（请求时渲染）：Next.js SSR / Nuxt | 动态内容多的站 | 中 |
| **Prerender 中间件**（预渲染快照服务，按 UA 返回静态 HTML 给爬虫） | 存量 CSR 站不想重构 | 中，外挂方案（prerendering.com；注意其 2026 观点：某些场景运维成本超过收益，先评估再上） |
| 双界面：核心内容并行发 .md 文件 | 文档/API 站 | 低（llms.txt 配套，见 advanced/03） |

前端类比：CSR 像 SPA 首屏白屏等 JS——浏览器都要等，不跑 JS 的爬虫直接拿到白屏。SSG 是把成品 HTML 在构建时就烤好。

## 第 3 步：验证爬虫抓取通道

```bash
# 逐个 UA 测试关键页返回码与内容
for ua in GPTBot OAI-SearchBot PerplexityBot ClaudeBot Google-Extended Googlebot; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -A "$ua" https://你的域名/)
  echo "$ua -> $code"
done
# 200=放行；403/503=被拦（查 robots.txt 与 CDN/WAF 两层）
```

**CDN 陷阱**：Cloudflare 等有一键"AI bot 拦截"，robots.txt 写了 Allow 也可能被 CDN 挡。验证方法同上——用 UA 请求，403 且 robots 没拦 → 查 CDN 设置。

## 第 4 步：主动提交索引

- **Google**：Search Console 提交 sitemap + URL Inspection 逐个请求编录。
- **Bing/Copilot**：Bing Webmaster Tools 提交 sitemap + **IndexNow**（即时推送协议，参与引擎含 Bing/Yandex/Naver/Seznam；发布新页 10 分钟后 Bing 搜 URL 抽查）。Copilot 走 Bing 索引，所以 Bing 提交间接服务 Copilot。
- **诚实澄清**：坊间流传"IndexNow/收录 Bing = 进 ChatGPT"——**未获确认**（eseospace 2026 明确指出）。ChatGPT Search 有 OAI-SearchBot 自有抓取，别为传闻做动作，两条通道各自保障。

## 第 5 步：日志监控爬虫到访（有服务器权限者）

```bash
grep -E "GPTBot|OAI-SearchBot|PerplexityBot|ClaudeBot" /var/log/nginx/access.log \
  | awk '{print $1, $7, $9}' | sort | uniq -c | sort -rn | head -20
```

看三件事：来没来（0 次=通道有堵点）、抓了哪些页（没抓=内链太浅）、返回码（403/500=白抓）。抓取量是被引用的先行指标（见[度量篇](07-measurement.md)）。

## 可达性验收清单

- [ ] curl 原始 HTML 含正文关键词（非 CSR 空壳）
- [ ] 各 AI UA 返回 200（robots + CDN 双层核对）
- [ ] sitemap.xml 存在、含关键页、无 404
- [ ] Search Console + Bing Webmaster 均验证并提交了 sitemap
- [ ] llms.txt 可访问（可选加分项）
- [ ] 日志中 2 周内能看到检索类爬虫到访记录

## 延伸阅读

- JS SEO 清单（AI 爬虫不执行 JS）：https://www.clienvora.com/checklists/technical-seo/javascript-rendering/
- SPA × AI 爬虫 10 项检查：https://www.w3corner.com/guides/2026-javascript-seo-guide-10-checks-spa-indexing-ai-crawlers/
- 让 JS 站点对 AI 可见：https://www.geo-tool.com/en/blog/make-javascript-websites-visible-to-ai-crawlers
- IndexNow 诚实指南：http://seosubmitterpro.com/resources/indexnow-guide-2026
- Bing+IndexNow 与 AI 搜索的边界：https://eseospace.com/blog/bing-webmaster-tools-indexnow-ai-search/

---
*上一篇：[提示词与问题集研究](../guide/09-prompt-research.md) ｜ 下一篇：[GA4 AI 引荐流量配置](10-ga4-ai-referral.md)*
