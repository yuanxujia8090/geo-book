# 内容工厂与工程组件：GEOFlow 生产侧 / geoptimize / dualmark / 语言级组件

> 物种定义见 [01 选型地图](01-selection-map.md)。本篇覆盖两类：把内容"批量造出来"的**内容工厂**，和给单页/单栈加 GEO 能力的**工程组件**。共性：都是零件，不是完整闭环——接进你的流水线才产生价值。
> 数据 GitHub API 一手核验于 2026-11-06；机制来自 README 原文。

## 内容工厂

### yaojingang/GEOFlow 生产侧（4032★ / AGPL-3.0，平台整体见 [02 实施平台](02-implementation-platforms.md)）
本篇只拆它的生产管线设计（可借的思想，不碰代码）：**可信知识→AI 生产→AI 质检门禁→人工审核→多站点分发**，每一步留痕可回溯。三个可借点：
1. **质检在人工之前**：机器先过一遍再给人看，审核带宽放大——对照本书 advanced/08，我们的清单是人审为主，可加"机器初筛"层。
2. **知识源单一化**：生产只从"可信知识库"取料（同 advanced/13 品牌事实卡的"单一事实源"原则，双保险）。
3. **分发状态回流**：发布结果回写任务与数据中心，形成运营闭环。
⚠️ 再强调：AGPL-3.0，借思想不借代码。

### beyondtahir/beyondseo（252★ / MIT / 活跃 push 11-04）
"AI SEO 事务所"技能套件：审计、写内容、竞品对比、外链规划在一个 agent 工作区闭环。与 agent 技能类（[04](04-agent-skills.md)）形态相同但定位"全家桶"；README 4.3 万字节的信息密度值得一读其结构组织法。不足：单作者、无第三方实测。

## 工程组件

### cucuwang/geoptimize（263★ / MIT / 活跃 push 11-01 / npm 包）
**确定性内容 lint**：跑 CI/pre-commit，固定规则检查——文档结构、量化声明缺来源信号、元数据问题、JSON-LD 结构、noindex/canonical 控制、重复措辞。**不靠 LLM 判断，结果 100% 可复现**，这是它对抗所有"AI 打分"类工具的存在理由。
- 借点：本书 advanced/08 验收自动化里的"可程序化"一堆，多数检查项它已实现成 npm 一行命令；阈值可按项目调，CI 阻断可配置。
- 前身 aeoptimize（0.8.0 更名），有迁移指南——命名演进本身说明 AEO/GEO 概念市场位的迁移。

### dodopayments/dualmark（123★ / Apache-2.0）
**双标记基础设施**：每个页面同时维护 HTML + Markdown 孪生版（"Markdown twins"），AI bot 直接读结构化孪生版。支付公司做的开源，动机是把 AI 流量引回自家入口。
- 借点：llms.txt 是"清单指路"，dualmark 是"原文投喂"——advanced/03 的争议（llms.txt 采纳有限）的另一半答案：与其指望引擎解析 HTML，不如直接给机器友好版本。
- 不足：双版本一致性维护成本转嫁给内容方，README 未给同步机制细节。

### 语言级组件（样本组）
| 组件 | 栈 | 备注 |
|------|----|------|
| geo-team-red/geo-optimizer（103★, MIT, Go） | Go | 可插拔策略框架，push 停 03-27 已停滞 |
| chnjames/AIGEOTOOLS（183★, MIT） | 全栈中文平台 | 关键词策略/多平台生成/E-E-A-T/多模型验证——中文中小团队"开箱即用"档位 |
| GitHiteshZope/aigeo（72★, MIT, Laravel） | PHP | 创建当天即达峰样，品类存在证明 |
| wzj177/geo-friendly（5★, MIT, PHP） | PHP | 同上，仅存档参考 |

## 选型建议

- **内容团队上 CI**：geoptimize（npm 一行，确定性）→ 有 AGPL 顾虑时的安全牌。
- **要生产管线设计参考**：读 GEOFlow README 画自己的流程图（思想免费）。
- **llms.txt 嫌不够**：评估 dualmark 式孪生页，尤其文档站。
- **PHP 栈**：aigeo/AIGEOTOOLS 二选一前先各自提 issue 试探维护响应。

---
*上游：[01 选型地图](01-selection-map.md) ｜ 落地流程：[advanced/08](../advanced/08-workflow-checklist.md)*
