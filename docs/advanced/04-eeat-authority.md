# E-E-A-T 与权威信号

> AI 判断"这个来源值不值得引用"的信号体系。

## 概念

E-E-A-T = Experience（经验）、Expertise（专业）、Authoritativeness（权威性）、Trustworthiness（可信度），Google 质量评估框架（Search Quality Rater Guidelines），2022 年加入首个 E。2026 年的 agentic GEO 研究（Agent2UCB，arXiv:2608.29063）明确把 E-E-A-T 式可信度检查纳入自动优化循环——说明这框架已被 AI 系统采纳为可计算信号。

## 四维落地

### Experience 经验
- 第一人称使用记录："我们实测了 X 周，结果是……"
- 实拍图、真实截图、原始数据表。
- 案例细节：具体数字、具体场景，AI 无法从泛泛内容生成这些。

### Expertise 专业
- 作者页：资历、作品、社交主页（`Person` Schema + `sameAs`）。
- 内容深度分层：入门 + 进阶并存，展示领域纵深。

### Authoritativeness 权威
- 被权威站点引用（外链仍然是代理指标）。
- 行业名录、协会、媒体报道。
- Princeton 论文实测：authority 与 source authority 两个特征直接提升可见度。

### Trustworthiness 可信
- HTTPS、清晰联系方式与实体信息。
- 更正政策、数据来源声明。
- 站内外信息一致（名称、定位、数据不打架）。

## 与第三方阵地的关系

E-E-A-T 一半发生在自己站外：AI 交叉验证时，Reddit 讨论、Wikipedia 词条、评测站提及构成"他证"。自己说权威没用，第三方说你权威才有用——见[第三方声量建设](05-third-party-presence.md)。

## 延伸阅读

- Agent2UCB（含 E-E-A-T 检查的 agentic GEO）：https://arxiv.org/abs/2608.29063
- AI SEO 可信度框架：https://aithinkerlab.com/generative-engine-optimization-2026/
- Google 质量评估指南背景：https://services.google.com/fh/files/misc/hsw-sqrg.pdf

---
*上一篇：[llms.txt 实战](03-llms-txt.md) ｜ 下一篇：[第三方声量建设](05-third-party-presence.md)*
