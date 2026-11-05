# 案例 4：端到端 90 天 GEO 实战（虚拟推演）

> 一个虚构但按真实方法论推演的完整案例：从零到被引用，每步对应本库哪一篇。

**性质声明**：这是教学用虚拟案例，人物/数据为推演构造，非真实客户战报。价值在于把散在各篇的方法**串成一条带时间轴的执行线**，让你知道"先做什么、多久见效、怎么验证"。所有方法引用真实章节。

## 主角设定

- 站点：`runllm-locally.example.com`——一个教人在 Mac 本地跑大模型的教程站（内容型、技术受众、有 GitHub 仓库）。
- 现状：Next.js CSR 架构、无 Schema、无 llms.txt、robots.txt 默认、从没管过 SEO。
- 目标：90 天内让 ChatGPT/Perplexity/豆包在"本地跑大模型"类问题里引用该站。

## Day 0-7：诊断（对应 guide/08、guide/09）

- **首查**（guide/08）：问 ChatGPT/Perplexity/豆包"怎么在 Mac 上本地运行大模型"，结果——AI 推荐了 Ollama、LM Studio 官网，本站 0 出现；引用域名清一色 Reddit、TowardsAI、官方文档。
- **可达性自检**（advanced/09）：`curl` 抓关键页，正文关键词命中 = 0 → **确诊 CSR 空壳，AI 完全看不到正文**。这是最大堵点。
- **问题集**（guide/09）：ChatGPT 发散 + Reddit r/LocalLLaMA 高赞标题 + People Also Ask，冻结出 25 个问题（品牌 5 + 品类推荐 12 + 对比 8）。
- **基线表**：25 问题 × 3 引擎 × 3 次采样，本站提及率 0/75。

**诊断结论**：技术层（CSR）+ 内容层（无可摘录答案块）+ 声量层（第三方 0 提及）三层全空，但受众精准、赛道热，值得做。

## Day 8-21：修地基（对应 advanced/09、02、03）

- **渲染修复**：Next.js 从 CSR 改 SSG/SSR，关键页 `curl` 复查正文命中 >0。这是本案例**第一个决定性动作**。
- **爬虫通道**：robots.txt 放行 OAI-SearchBot/PerplexityBot/Google-Extended；核对 Cloudflare 未开 AI 拦截。UA 逐个测返回 200。
- **Schema**：全站铺 Article + Organization + 每篇教程 HowTo + FAQ 页 FAQPage（advanced/02 模板）。
- **llms.txt** + 每篇教程提供 `.md` 版本（advanced/03）。
- **索引提交**：Search Console + Bing Webmaster 提交 sitemap，配 IndexNow（advanced/09）。

## Day 22-56：改内容 + 铺声量（对应 advanced/01、05）

- **内容改造**：25 个问题 → 每个做成自包含答案块。例：问题"M5 芯片能跑多大的模型？"→ H2 问句 + 前置直答"M5 统一内存 128GB，可流畅运行 70B 量化模型，实测 23 token/s" + 数据表 + 步骤（advanced/01 八法）。
- **对比页**：新建"Ollama vs LM Studio vs llama.cpp"中立对比页——首查发现引擎缺中立对比信源，这是**空位机会**。
- **第三方声量**（advanced/05）：创始人实名在 r/LocalLLaMA 回答真实问题（披露身份）；GitHub README 优化 + Topics；争取 2 个垂直评测博客收录。慢变量，持续投。

## Day 57-90：监测迭代（对应 advanced/07、10）

- **周监测**：冻结的 25 问题每周五跑一遍填表（advanced/07 手工协议）。
- **GA4**：AI Assistants 渠道 + 自定义正则看引荐回流（advanced/10）。
- **趋势**（推演节奏）：
  - 第 4 周：Perplexity 开始引用对比页（Perplexity 对新鲜/对比内容最友好，最先见效，见 guide/06）。
  - 第 6-8 周：ChatGPT Search 在"M5 跑多大模型"类问题引用教程页。
  - 第 10-12 周：豆包经头条系转载后出现；GA4 可见 AI 会话从 0 到日均两位数。
- **迭代**：发现被引的都是"具体芯片+具体数字"页面 → 追加 M3/M4/A 系列各写一篇同结构页，复制命中模式。

## 90 天复盘要点（可迁移）

1. **顺序不能乱**：先修 CSR 再谈内容——地基不通，内容白写。这是新手最常犯的错（直接开始写文章）。
2. **Perplexity 先行验证**：它见效最快，是免费的"方法有效性探针"。
3. **对比页是空位金矿**：引擎缺中立对比信源，新站最容易切进去。
4. **具体数字 = 引用磁铁**：被引的全是带硬数据的自包含块，不是观点。
5. **第三方是慢变量**：Reddit/GitHub 声量 90 天内只见苗头，但决定第 4-6 个月的天花板。
6. **诚实预期**：检索层 4-8 周见效正常，训练数据层（不联网也记得你）要 6-12 个月（advanced/06）。

## 延伸阅读（真实世界同类参考）

- 本地服务被 AI 略过研究（真实数据）：https://pickedbyagents.com/reports/why-ai-passes-hvac-contractors
- 90 天路线图框架：https://trackmyvisibility.com/blogs/ai-seo/geo-strategy-complete-roadmap-ai-visibility/
- 2026 playbook：https://www.bspkn.co/insights/optimize-for-ai-search-geo-playbook-2026/

---
*上一篇：[GA4 AI 引荐配置](../advanced/10-ga4-ai-referral.md) ｜ 回到 [README](../../README.md)*
