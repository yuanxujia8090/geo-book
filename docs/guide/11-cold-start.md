# 新站冷启动：从零到第一次被引用

> 没有域名权重、没有外链、没有内容历史的新站，怎么拿到第一次 AI 引用。

## 先校准预期（不然会半途放弃）

| 里程碑 | 正常时间窗 |
|--------|-----------|
| 被收录（引擎能抓到） | 数天-2 周（IndexNow 可提速到小时级） |
| 第一次被引用（长尾问题） | 2-8 周 |
| 品类推荐问题稳定出现 | 3-6 个月 |
| 不联网也被"记得"（训练数据层） | 6-12 个月+ |

新站做 GEO 普遍预期 3-6 个月基础工作才见系统性变化，且**首批结果总是窄的**——出现在几个定义明确的小问题上，不是品类大词。看到"只有 2 个问题被引"不是失败，是正常的第一阶段（dengzone 口径，medium 置信）。

## 新站的结构性优势（别只看到劣势）

一个反直觉事实：**AI 引用源和 Google 前十结果重合只有约 12%**（notioncue 分析，medium 置信）。意味着：
- Google 的十年权重壁垒，AI 这边没这么硬。
- 传统 SEO 要 6-12 个月才排得上去的词，AI 答案里可能第 2 周就引你——只要那个问题上没人供给、你供给得最好。
- 技术设置 2-3 小时就能做完（advanced/09 清单），这是新站唯一"当天可完成"的杠杆。

## 冷启动四板斧（按顺序）

### 板斧 1：挑"无人供给"的空位问题，不碰大词
用首查（guide/08）+ 竞品逆向（reverse/02）找这种问题：**用户在问、AI 答得勉强、引用源质量差或没有**。典型是长尾对比题（"X 和 Y 哪个好"里 X/Y 都是小众工具）、新场景题（"M5 芯片跑 70B 模型"这种硬件刚出的题）。一个空位题一篇深度证据页，是新站唯一的正确弹药密度。

### 板斧 2：借站生还——先寄生再自建
新域名没权威，就先把内容/身份铺到**引擎已经信任的域名**上：
- 在目标引擎偏好的平台发布（中文按 guide/10：知乎/CSDN/头条号/公众号；英文 Reddit/Medium/垂直论坛），带作者真名与bio回链。
- 参与真实问答被引用；GitHub 项目（技术类）README 即信源。
- 这些"借来的权威"会带动品牌名与域名的关联识别——之后自有域名引用率才起得来。

### 板斧 3：把 Perplexity 当免费验证器
Perplexity 对新站/新鲜内容最友好、反馈最快（guide/06）。新站每发一页，几天内就能在 Perplexity 上验证"这类写法是否被引"——验证通过的页面模式再复制到 ChatGPT/AI Overviews 战场。冷启动期它是你的试验田。

### 板斧 4：技术面当天做到满配
新站没理由在技术层失分：SSG 渲染、robots 放行、sitemap 提交、IndexNow、Schema、llms.txt、llms.txt 链接验证——照 advanced/09 + guide/08 一天做完。老站改渲染要排期，新站直接选对架构，这是新站独有的先发优势。

## 引用是有寿命的（持续供给的原因）

对 15,661 个被引 URL 的 60 天分析：**52% 的 URL 只被引用了 1 天**（mybrandi 自报，medium 置信）。AI 引用不是"上榜就稳"，是持续再选举。新站正确策略不是攒一批存量页面，而是**保持供给节奏**（每周 1-2 篇证据页 > 一个月憋一篇大文），让引擎的检索池里始终有你的新鲜候选。

## 90 天节奏表（新站特化版）

| 周 | 动作 | 验收 |
|----|------|------|
| W1 | 技术满配 + 问题集 25 题 + 基线 | curl 拿得到正文；基线表填完 |
| W2-3 | 空位题 3 篇证据页 + Perplexity 验证 | 至少 1 题被 Perplexity 引用 |
| W4-6 | 借势平台铺 5-8 处 + 每周 1 篇 | 品牌名在第三方内容出现 |
| W7-12 | 复制已验证模式扩到 15 页 + 周监测 | ChatGPT/豆包开始长尾引用；GA4 见 AI 会话 |

完整版见 [case-studies/04 九十天推演](../case-studies/04-end-to-end-90days.md)。

## 延伸阅读

- 零权重起步的 AEO：https://notioncue.com/blog/aeo-for-startups-early-stage-ai-citations-no-domain-authority
- 新站从域名到引用的实测时间线：https://fogtrail.ai/blog/how-fast-new-website-indexed-and-cited
- 引用寿命分析（52% 只活一天）：https://mybrandi.ai/ai-citation-strategy/
- 初创 GEO 节奏：https://dengzone.com/geo-for-startups-getting-ai-citations-without-an-established-domain-authority/
- 首次引用时间度量：https://maxaeo.ai/blog/time-to-citation-ai-search/

---
*上一篇：[中文信源生态实测榜](10-cn-source-ranking.md) ｜ 下一篇：[进阶-内容优化](../advanced/01-content-optimization.md)（入门篇完，从这里进进阶）*
