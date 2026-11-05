# 进入 LLM 训练数据（长期层）

> 检索层见效快，训练数据层是护城河。品牌"被 AI 记住"是季度到年的慢变量。

## 两层可见性

AI 提到你时来自两层之一（subscribepr.com 框架）：
1. **实时检索层**：引擎刚才搜到了你的内容——天/周见效。
2. **训练数据层**：模型预训练时"学过"你——季度/年见效，但脱离联网也能被提及，更持久。

多数 GEO 工作做第 1 层是对的（快）；第 2 层决定长期心智。

## 训练数据从哪来

| 来源 | 说明 | 可控性 |
|------|------|--------|
| Common Crawl | 开源网页语料，几乎所有实验室的底座 | 需被 CC 抓到且不被 robots 拦截（拦 CCBot=放弃这层） |
| 数据授权协议 | Reddit-OpenAI/Google、AP、NewsCorp 等付费授权 | 被授权平台提及=间接进入 |
| Wikipedia | 各实验室必用 | 词条存在即进入 |
| 代码托管 | GitHub 公开仓库（开发者工具类品牌） | 文档/README/示例质量 |
| 论文/技术报告 | arXiv 等 | 被引用、被复现 |

## 进入训练数据的检查清单（rctrl.com 框架）

1. **确认在 Common Crawl**：用 CC 索引查询域名是否被收录。
2. **解除拦截**：robots.txt 放行 CCBot；检查 CDN 层是否误拦。
3. **写"能过过滤器"的散文**：训练管线过滤低质/重复/纯模板页；原创、信息密度高的内容存活率高。
4. **进入授权源**：在 Reddit、被授权媒体、百科等"实验室实际购买的数据源"里积累提及。

## 品牌实体沉淀技巧

- 统一品牌实体表述：`品牌名 + 品类`固定搭配反复共现（"RunLLM Locally——本地大模型工具"），LLM 学到稳定关联。
- 同义实体收敛：一个名字打天下，别同时推 3 个品牌变体。
- sameAs 网络：官网、GitHub、X、LinkedIn 互链（Schema sameAs），把实体图谱钉死。

## 风险提示

- 往训练数据"灌"营销内容违反平台规则，且模型更新会稀释——质量与真实声量才是正道。
- 训练数据不可精确控制，只能提高概率；把预算大头留在检索层是理性选择。

## 延伸阅读

- Common Crawl 入圈指南：https://rctrl.com/blog/get-into-llm-training-data-common-crawl
- 训练数据 playbook：https://subscribepr.com/blog/how-to-get-into-llm-training-data/
- Reddit/Wikipedia/评测站角色：https://praised.co/blog/reddit-wikipedia-llm-sources

---
*上一篇：[第三方声量建设](05-third-party-presence.md) ｜ 下一篇：[GEO 度量与监测](07-measurement.md)*
