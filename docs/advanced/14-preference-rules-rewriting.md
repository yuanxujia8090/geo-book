# 引擎偏好规则与内容重写

> 前述内容优化（[advanced/01](01-content-optimization.md)）给的是通用判据；这一篇讲**怎么把"引擎喜欢什么"变成可提取的规则、再用规则重写**——AutoGEO（ICLR'26）把这个循环做了学术化，是本书 reverse/ 手法的自动化理论版。
> 机制描述来自 AutoGEO 官方仓库与论文摘要（arXiv:2510.11438，2026-11-06 核验）。

## 一、问题的提出：通用判据 vs 引擎特异偏好

"数字块 +61.6%"这类判据是跨引擎平均数。但实践中每个生成式引擎的偏好不同：Gemini 偏结构化数据、Perplexity 偏新鲜第三方、豆包偏中文社区帖（见 [guide/07](../guide/07-chinese-ai-engines.md)）。同一篇内容在 A 引擎被引、在 B 引擎消失，差的就是引擎特异偏好。

**核心问题：偏好能不能不靠猜、从引擎行为里自动挖出来？** AutoGEO 的答案是能。

## 二、AutoGEO 的三组件方法

```
采样语料（问题 + 引擎回答 + 引用片段）
        │
        ▼
① Rule Extraction ──自动挖掘──▶ 偏好规则集（每引擎一套）
        │
        ├─▶ ② AutoGEO_API：规则塞进提示词 → 大模型按规则重写
        └─▶ ③ AutoGEO_Mini：规则作奖励信号 → GRPO 强化学习训练小模型（Qwen1.7B）
```

1. **规则提取（Rule Extraction）**：喂给引擎大量"问题-回答"对，让模型归纳"它引用的片段长什么样"——带统计数字、给出直接定义、列步骤……产出显式规则集，按引擎×领域分目录存放。
2. **AutoGEO_API**：把提取的规则注入改写提示词，用现成大模型重写目标文档。零训练成本，规则透明可审。
3. **AutoGEO_Mini**：用强化学习（GRPO）把能力蒸馏进 1.7B 小模型——推理便宜，但要 2×A100 训约 48 小时（README 自报）。

## 三、双指标：可见度不能牺牲效用

AutoGEO 的评估是两个分数同时算：

| 指标 | 衡量 | 防什么 |
|------|------|--------|
| **GEO score** | 重写后文档在引擎回答中的可见度（被提及/被引用） | 防"改了没用" |
| **GEU score** | 生成式引擎对重写后文档的效用（内容质量、准确性） | 防"为骗引用把内容改烂" |

这是对黑帽 GEO 的正面回击：只优化 GEO score 的改写会滑向关键词堆砌和事实注水；GEU 把"引擎自己觉得这内容有没有用"纳入约束。**从业者版等价物**：每次改写后，除了重采样看引用率（[advanced/12 采样纪律](12-sampling-discipline.md)），还要人工核事实未被改损。

## 四、诚实边界（README 原文强调）

- **偏好规则不迁移**：换引擎或换领域，必须重跑规则提取、重训 Mini。不存在一套规则通吃。
- 学术实现 ≠ 生产工具：仓库是研究代码，无仪表盘无工单流，落地要自己搭管线。
- 适配成本实打实：API 版要烧采样 token；Mini 版要 GPU。

## 五、从业者怎么借（不必跑代码）

三层递减的工程强度，取你能承受的最低档：

1. **手工版（今天就能用）**：reverse/01 的"引单采集"攒够 50+ 条某引擎的引用片段后，人肉归纳 5-10 条该引擎的偏好规则（形态/长度/内容类型），写进内容简报模板（advanced/13），再按 reverse/01 手法 4"单变量改写"验证——这就是人肉 Rule Extraction + GEU 复核。
2. **提示词版**：把归纳的规则集直接写进改写提示词（AutoGEO_API 的同构做法），让手边任何大模型按规则重写页面正文。
3. **全管线版**：跑 AutoGEO 仓库（MIT；conda 环境+keys.env，`python -m autogeo.extract_rules --dataset X --engine_llm gemini-2.5-flash-lite`），或等工程化产品吸收该方法（观察名单见 [news/01](../news/01-signal-log.md)）。

**与 GEO-Bench 的关系**：AutoGEO 论文同时提出可复现 benchmark（GEOLab 收录其数据集）——它既可用来测方法，也可用来测你的页面：把自己放进基准跑分，是"改写有效"的第三方证据。

## 六、常见误解

1. ❌"AutoGEO 是个 CMS/平台"——它是研究框架+模型权重，没有管理界面。
2. ❌"挖出来的规则永久有效"——引擎版本一更新偏好就漂移，规则集要按采样周期重挖（呼应四层模型"引擎行为会变"的口径）。
3. ❌"重写=AI 洗稿"——GEU 约束存在的全部意义就是把"提升可引用性"和"注水洗稿"切开；只动结构与证据密度，不动事实。

## 延伸阅读

- 论文：https://arxiv.org/abs/2510.11438（What Generative Search Engines Like and How to Optimize Web Content Cooperatively）
- 官方代码与数据集：https://github.com/cxcscmu/AutoGEO ｜ HF: cx-cmu/AutoGEO_mini_Qwen1.7B_*
- 项目页与 Demo：https://cxcscmu.github.io/AutoGEO/ ｜ https://huggingface.co/spaces/cx-cmu/AutoGEO_Mini

---
*上游判据：[四层依赖模型](11-four-layer-model.md) ｜ 实操手法：[黑盒里探规则](../reverse/01-black-box-probing.md) ｜ 深析：[05 研究框架](../projects/05-research-frameworks.md)*
