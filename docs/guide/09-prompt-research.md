# 提示词与问题集研究（Prompt Research）

> AI 时代的关键词研究 = 提示词研究。问题集选错了，后面全白做。

## 为什么这是第一步

传统 SEO 优化"关键词"，GEO 优化"提示词"：用户不再敲 3 个词，而是对 AI 说一整句甚至一段话（Semrush 定义：prompt research 追踪人们在 AI 工具里问什么、工具推荐了谁）。你的内容要匹配的是**问题**，不是词。

## 五路找问题（按性价比排序）

### 1. 自问发散（免费，10 分钟）
让 ChatGPT 扮演你的目标用户：
```
我是[目标人群]，想买/选/用[品类]。列出我会向 AI 助手问的 30 个问题，
包括新手问题、对比问题、避坑问题、预算问题。
```
产出通常 80% 可用，去重后留 20-30 个。

### 2. 真实语料挖掘（免费，效果最好）
- **Google 搜索框**：输入品牌词/品类词看下拉联想，切"People Also Ask"逐层展开。
- **Reddit/知乎垂直版块**：搜品类关键词，高赞帖标题就是真实问法。
- **客服记录/销售问题**（有客户的 B2B 必做）：客户真实问过什么，用户就会问 AI 什么。

### 3. 引擎反向挖掘（免费）
直接问引擎："用户关于 [品类] 最常问你的 20 个问题是什么？"——答案本身可能不准，但句式结构可模仿。

### 4. 竞品引用反查（免费）
首查（[guide/08](08-first-audit.md)）里引用竞品的页面，打开看它回答了哪些问题——那些问题已被引擎验证有价值。

### 5. 商业工具（付费）
Semrush/Ahrefs 的 AI 关键词/prompt 库、Otterly Prompt Explorer 等提供真实提示词量与竞争度。

## 问题集设计规则

一个能用的监测问题集（prompt pack）必须满足：

1. **三类配比**：品牌词问题（"X 是什么"）20% + 品类推荐问题（"推荐 X 工具"）50% + 对比问题（"X vs Y"）30%。
2. **冻结**：选定后写死存文件（frozen prompts），每次监测逐字不变——改一个字结果就不可比。
3. **真实句式**：口语化完整句，别用关键词堆砌（"CRM 中小团队 报价"❌ → "我们 5 人团队想要个简单的 CRM，一年预算 1 万，有什么推荐？"✅）。
4. **规模**：起步 20-30 个，每引擎每问题采样 ≥3 次（答案随机性对策）。

## 把问题变成内容

每个高价值问题 → 页面上一个自包含答案块：问句式 H2 + 前置 40-80 字直答 + 数据/例子支撑（写法见[内容优化](../advanced/01-content-optimization.md)）。问题集 = 内容选题清单 = 监测问题集，三合一，这是 GEO 工作流的核心闭环。

## 延伸阅读

- Semrush prompt research：https://www.semrush.com/features/prompt-research/
- Otterly AI 关键词研究：https://otterly.ai/blog/ai-keyword-research/
- Similarweb 分步方法：https://aisearch.similarweb.com/blog/prompt-research/
- 提示词发现法：https://surferstack.com/guides/the-prompt-discovery-method-how-to-find-high-value-ai-search-queries-your-competitors-dont-know-exist-in-2026

---
*上一篇：[上手首查](08-first-audit.md) ｜ 下一篇：[进阶-技术可达性](../advanced/09-technical-accessibility.md)*
