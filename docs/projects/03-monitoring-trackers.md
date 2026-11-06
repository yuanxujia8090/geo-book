# 监测类平台对比：elmo / limelit / geo-aeo-tracker / oneglanse / gego

> 物种定义见 [01 选型地图](01-selection-map.md)。监测类回答一个问题：**AI 现在怎么说我、引用谁**。不修内容不发工单，只做持续测量——所以选型看的是引擎覆盖、采样方式、数据主权三件事。
> 数据 GitHub API 一手核验于 2026-11-06；机制来自 README 原文。

## 对比总表

| 维度 | elmo (570★) | limelit/open (386★) | geo-aeo-tracker (320★) | oneglanse (250★) | gego (109★) |
|------|------------|--------------------|----------------------|-----------------|-------------|
| 许可 | MIT | Apache-2.0 | MIT | MIT | ⚠️ GPL-3.0 |
| 语言/形态 | TypeScript | 单二进制 | 轻量 | — | Go+Vue3 |
| 引擎覆盖 | 6+（抓真实消费端 App+API 双轨） | 6（含 Google AI Mode） | 5 | 5 | 可插拔（含 Ollama 本地） |
| 判定方式 | judge model 确认提及 | 明确"答案=引擎实际给的" | 提及监测 | 提及监测 | 别名匹配+引用抽取 |
| 数据主权 | 自托管或 Cloud($29/mo) | 你的密钥你的数据 | 自托管 | 自托管 | PG+MongoDB+etcd 自管 |
| 活跃度 | ✅ push 11-06，142 open issue | ✅ push 10-30 | ✅ push 10-19 | push 10-04 | push 07-23 |

## 逐个点评

### elmo（elmohq/elmo）——社区最活跃的正规军
- **优势**：双轨采样是硬差异——ChatGPT/Google AI Mode/AI Overviews/Gemini/Perplexity/Copilot 走真实消费端抓取（"用户实际看到的答案"），Claude/Grok 走 API；提及匹配名称+别名+域名后再过 judge model 确认，误报控制有层次。引用按域名×类别分组（你的/竞品的/社交/机构），直接读出"你这个品类 AI 信任谁"。onboarding 向导从官网自动建议 prompts/竞品/人设。
- **不足**：开源+Cloud 双轨意味着部分便利功能在云端（$29/mo 起）；142 个 open issue 既是活跃也是消化不过来的信号；judge model 引入自身偏见的风险 README 未讨论。
- **场景**：要"消费端真实答案"级监测、不想自己写爬虫的中大型团队。**与本书**：advanced/07 度量指标的产品化对照；其"API≠网页端"实践印证 advanced/12 的采样纪律。

### limelit-co/open——极简单二进制派
- **优势**：一个二进制+你的密钥+你的数据，部署摩擦最低；自带 MCP server，AI 助手直接调监测数据（同类首个把 MCP 做成内置的）；demo 展示 21 竞品×6 引擎的"赛马"视图。对引擎 ID/工具名的命名与其商业版 Limelit 一致，迁移无痛。
- **不足**：品牌混排（README 大量导流自家站）；judge/解析细节披露少；社区规模小。
- **场景**：要把监测塞进 agent 工作流的开发者（MCP 是决定点）。**与本书**：advanced/10 GA4 之外另一条归因路——直接在 agent 里查可见度。

### geo-aeo-tracker / oneglanse——轻量单点
- 两者同构：5 引擎提及/引用监测，MIT，个人可跑。oneglanse 上过 Product Hunt（Day #28，badge 自报）。
- **共同不足**：功能面窄（采数+看板），无诊断无工单；采样频次/环境卫生细节披露有限——用它之前先读本库 advanced/12 把自己的纪律立住，工具只是执行器。
- **场景**：预算为零、要"先有数再说"的起步监测。

### gego（AI2HU/gego）——Go 分布式调度样本
- **优势**：架构上是本组唯一的分布式设计：cron 调度→etcd 队列→独立 worker 执行，可横向加 worker；支持 Ollama 把国内合规定位做进架构（本地模型跑采样）；JWT 角色权限，多用户可用。
- **不足**：⚠️ GPL-3.0——嵌入闭源商业产品有传染风险，仅作参考实现或独立部署；依赖栈重（PG+MongoDB+etcd 三件套，个人劝退）；push 停 07-23 半停滞。
- **场景**：Go 技术栈、需要分布式采样调度的国内团队。

## 监测选型的三个判断题

1. **API 采样够不够？** API 便宜稳定但≠消费端答案（advanced/12）；要给客户看"真实 AI 怎么说"选 elmo 双轨，内部趋势用 API 即可。
2. **数据放哪？** 五款都能自托管——但 elmo 的 Cloud 引流、limelit 的官网导流提示：确认你跑的是全功能本地版还是试用壳，部署前读 docker-compose 的数据卷。
3. **要不要 MCP？** 已在用 agent 干 GEO 的，limelit 内置 MCP 省一层胶水；否则不重要。

---
*上游：[01 选型地图](01-selection-map.md) ｜ 度量方法论：[advanced/07](../advanced/07-measurement.md)、[advanced/12](../advanced/12-sampling-discipline.md)*
