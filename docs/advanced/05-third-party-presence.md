# 第三方声量建设

> AI 交叉验证你的品牌时，看的是别人怎么说你。

## 为什么第三方阵地权重高

- **训练数据层面**：Common Crawl 含数十亿 Reddit 页面；Reddit 还与 OpenAI/Google 签数据授权协议（instantpress.co 梳理）。Wikipedia 估计占 LLM 训练语料 5-15%（presenc.ai 估算，medium 置信）。
- **检索层面**：2025-09 论文《How to Dominate AI Search》（arXiv:2509.08919）发现 AI 搜索引擎**系统性偏好赢得的媒体（earned media）而非品牌自有内容**——官网自夸不如第三方评测。
- **实测**：有详细 Wikipedia 词条的品牌获得的 AI 提及是无词条品牌的 3.2 倍（presenc.ai，自报研究口径）。

## 分阵地打法

### Reddit
- 真实参与社区，价值先行；营销号内容会被删且污染品牌。
- 目标：让"best X"类讨论帖里出现你的品牌名（这些帖被 AI 大量检索）。
- 合规红线：不买水军、不伪装用户——被识破的负面帖子同样进训练/检索数据。

### Wikipedia / Wikidata
- 词条门槛高：需满足关注度（notability）标准，先积累媒体报道再申请。
- Wikidata 条目门槛低得多：结构化实体数据，被多家引擎消费，优先做。

### 评测/榜单站
- G2、Capterra（B2B）、垂直领域评测媒体：Perplexity 与 ChatGPT 引用高频信源。
- 对比页（"YourBrand vs Competitor"）被第三方写比被自己写可信度高。

### 行业媒体与播客
- 客座文章、播客访谈：同时供给检索层（文章）与实体层（人名-品牌关联）。

### X.com
- Grok 第一信源；品牌相关的真实讨论、长文 Article 直接进 Grok 上下文。

## 优先级建议（预算有限时）

1. Wikidata 实体条目（免费、快）。
2. 2-3 个高相关评测/对比文章（置换或付费均可，标注披露）。
3. Reddit 长期真实参与（慢但复利最高）。
4. Wikipedia（有关注度后再推进）。

## 渠道加权图谱（阵地不止列清单，要算权重）

分阵地打法之外，工程化做法是把渠道变成**加权图谱**——geolook 的 19 渠道地图给了可借的方法骨架（README 原文，2026-11-06 核验）：

1. **列渠道全集**：把目标市场可能被 AI 引用的阵地全部列出（英文：Reddit/Wikipedia/评测站/论坛/YouTube；中文：百科/榜单站/知乎/CSDN/公众号/垂媒——对照 [guide/10 实测榜](../guide/10-cn-source-ranking.md) 的生态层分类）。
2. **按真实引用语料定权重**：每个渠道的权重 = 它在目标引擎实际引用中出现的份额，不是拍脑袋。中文侧直接用 CN-GEO 数据集（187,818 条引用）按引擎×渠道交叉算；英文侧用引单采集（reverse/01 手法 2）自攒。
3. **算"竞品有你没有"打击清单**：对每个主要竞品，统计其被引用集中在哪些渠道，与你的渠道覆盖做差集——差集就是最优先的第三方阵地工单（比"通用建议发 Reddit"精准一个量级）。
4. **定期重算**：渠道份额随引擎行为漂移（见 [news/01](../news/01-signal-log.md)），季度更新一次。

预算分配跟着权重走：权重高×你缺位的渠道优先，这才是"第三方声量建设"从方法论到排期表的桥。

## 延伸阅读

- Reddit→LLM 管道：https://www.instantpress.co/blog/the-reddit-llm-connection
- Wikipedia 效应：https://presenc.ai/research/wikipedia-effect-on-ai-brand-visibility
- 训练数据入圈 playbook：https://subscribepr.com/blog/how-to-get-into-llm-training-data/
- earned media 偏好论文：https://arxiv.org/abs/2509.08919

---
*上一篇：[E-E-A-T 与权威信号](04-eeat-authority.md) ｜ 下一篇：[进入 LLM 训练数据](06-training-data-visibility.md)*
