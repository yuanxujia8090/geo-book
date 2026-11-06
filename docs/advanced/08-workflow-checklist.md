# GEO 工作流与审计清单

> 把前面所有知识串成一套可复制的执行流程：诊断 → 优化 → 监测 → 迭代。

## 四阶段工作流

```
Phase 1 诊断(1周) → Phase 2 地基修复(1-2周) → Phase 3 内容与声量(持续) → Phase 4 监测迭代(每周)
```

### Phase 1 诊断
- [ ] 建问题集：五路找问题 + 冻结（见[提示词研究](../guide/09-prompt-research.md)）。
- [ ] 跑基线：30 分钟首查 + 手工监测协议（见[上手首查](../guide/08-first-audit.md)、[度量篇](07-measurement.md)）。
- [ ] AI 爬虫可达性：robots.txt、CDN 开关、curl 正文验证（见[技术可达性](09-technical-accessibility.md)）。
- [ ] 抓取验证：site: 查询 / 引擎内直接问"总结 example.com 的内容"。
- [ ] 竞品对比：谁已被引用、在哪些页面被引用。

### Phase 2 地基修复
- [ ] 渲染修复：CSR 站 SSR/SSG 化，确保 curl 拿得到正文（见[技术可达性](09-technical-accessibility.md)——这是新手最大隐形坑）。
- [ ] 放行检索类爬虫（OAI-SearchBot、PerplexityBot、Google-Extended…）。
- [ ] 部署核心 Schema：Organization / Article / FAQPage（见[Schema 篇](02-schema-structured-data.md)）。
- [ ] 发布 llms.txt + 关键页 .md 版本（见[llms.txt 篇](03-llms-txt.md)）。
- [ ] 提交索引：Search Console + Bing Webmaster + IndexNow（见[技术可达性](09-technical-accessibility.md)）。

### Phase 3 内容与声量
- [ ] Top 10 问题各建/改一页：问句式标题 + 答案前置 + 数据锚点（见[内容篇](01-content-optimization.md)）。
- [ ] 建作者页与实体页，sameAs 互联。
- [ ] 第三方阵地按优先级推进（Wikidata → 评测 → Reddit 长期）（见[第三方篇](05-third-party-presence.md)）。
- [ ] 中文生态按引擎分发（见[中文引擎篇](../guide/07-chinese-ai-engines.md)）。

### Phase 4 监测迭代
- [ ] 每周固定问题集跑监测，记录趋势。
- [ ] 每月复盘：哪些页面开始被引用 → 复制其模式。
- [ ] 跟踪引擎行为变化（AI Overviews 政策、爬虫 UA 更新）。

## 工单风险分级（优先级 ≠ 风险）

**优先级说"多重要"，风险说"动手时多小心"，两者独立。** 解封 robots 是 P0 也是高风险——改错一行封掉全站。每条任务都应带风险标记：

| 级别 | 含义 | 纪律 |
|------|------|------|
| 低风险快速优化 | 纯新增资产/站外动作，不改已有页面 | 先做这批建立信任，随时可撤 |
| 需观察的内容调整 | 改已有页面内容、新建内容 | 不改 URL、不改已有排名页核心主题；发布后 **7/14/28 天**各复核一次 |
| 高风险技术改造 | 动 robots / WAF / noindex / 渲染架构 | 改前备份、单独排期、小批量发布、留回滚；发布后立刻重跑体检 |

通用保护性铁律：
- **先保护已有 URL、canonical、标题与历史权重，再考虑新增**——GEO 建设不能以毁掉已有搜索资产为代价。
- 禁止一次性批量修改大量已收录页面；每批小量发布并记录修改前基线数据。
- 数据没改善时先分析原因，不要盲目继续批量改动。
- 反向防护：**sitemap 只装值得被引用的规范页**，站内搜索/带参/翻页 URL 用 robots 通配符挡掉（`Disallow: /*?session=`、`Disallow: /search?`）——低价值页进索引会稀释实体表征。
- 多语言站必须 hreflang 互指，否则各语言版被当重复内容、跨市场挂错语言页。

## 验收自动化（"done"要可计算，不是嘴上说）

工单写完没人回答"到底做完没有"。geolook 的启示：把验收拆成**可程序化**与**必须人审**两堆，分别给机制（其示例项目 86%（18/21）工单可自动验证，README 原文 2026-11-06 核验；比例随项目浮动，拆分思想照搬）：

| 验收类型 | 覆盖工单 | 机制 |
|---------|---------|------|
| 可程序化 | llms.txt 已部署且链接有效、JSON-LD 合法、UA 返回 200、sitemap 过滤生效、段落可引扫描通过 | curl/脚本 + 下轮采样自动复算；**回归自动重开工单**（曾经通过又失败=自动回到待办，不靠人记） |
| 必须人审 | 内容事实准确、品牌口径一致、第三方帖未被删、官媒发稿合规 | 人工按 7/14/28 天节奏复核（与风险分级联动） |

手工版最小实现：每张工单加一列 `verify_cmd`（能贴进终端的验证命令）+ 一列 `verified_at`；周报时逐行跑 verify_cmd，失败自动回到待办。没有 verify_cmd 的工单不派发——写不出验收标准的任务说明还没想清楚。

## 常见坑

1. **只改官网**：earned media 偏好是实测结论，自有内容权重有天花板。
2. **无基线就上量**：改了一堆不知道哪个起效。
3. **期待立竿见影**：检索层 2-6 周、训练层 6-12 个月才是正常节奏。
4. **忽略 SEO 地基**：97% AI Overviews 引用来自自然前 20，传统 SEO 塌了 GEO 无从谈起。
5. **黑帽改写**：GEO-Bench（arXiv:2605.29107）测试的操纵式策略短期有效但会被引擎反制，不要碰。

## 延伸阅读

- 完整路线图：https://trackmyvisibility.com/blogs/ai-seo/geo-strategy-complete-roadmap-ai-visibility/
- 2026 playbook：https://www.bspkn.co/insights/optimize-for-ai-search-geo-playbook-2026/
- 审计步骤指南：https://achermouk.com/generative-engine-optimization-geo-2026-complete-guide-chatgpt-perplexity-google-ai/
- GEO-Bench（操纵策略基准）：https://arxiv.org/abs/2605.29107

---
*上一篇：[GEO 度量与监测](07-measurement.md) ｜ 下一篇：[工具总览](../tools/01-tools-overview.md)*
