# 中文信源生态实测榜

> 187,818 条中文 AI 引用记录实算：官网只占 1.37%。这一篇改变你的资源分配。

## 数据来源（先说清可信度）

CN-GEO 数据集 v2.0.1（2026-07-14 发布），187,818 条去重引用、19,190 条域名×平台记录、12 个平台终端。上游为开源数据集 [yaojingang/GEOLab](https://github.com/yaojingang/GEOLab)（原 geo-citation-lab，748⭐，核验于 2026-11-05）。**这是大样本实算而非厂商口径，置信高**；但原始层缺完整回答与采集时间——覆盖分布可直接用，趋势/情感/推荐率不能。

## 三个改变资源分配的数字

| 结论 | 数字 |
|------|-----:|
| 品牌官网占全库中文 AI 引用 | **1.37%**（52 域名） |
| 商业推荐/榜单站占全库引用 | **9.1%**（仅 28 个域名） |
| 内容平台（qq/toutiao/baidu/iesdouyin 四家） | **16.4%** |

**核心认知：官网是事实源，不是引用源。** 官网的作用是让 AI 描述你时口径正确、被第三方引用时有可信落点；指望"把官网做好就被引用"是战略性误判。官网做到"可抓取+有定义+有结构化数据+口径统一"就够了，边际收益远低于在一个榜单站拿到词条。

## 生态割据：每个引擎住在自家生态里

| 引擎 | 自家生态占比 | 硬门槛 |
|------|------------|--------|
| 百度 AI / 文心 | baidu.com 占 29-37.7%，Top8 集中度 66%+ | 不做百度百科/百家号/百度知道基本进不去 |
| 豆包 App | iesdouyin 占 28.1% | 抖音图文/视频是主入口 |
| 元宝 | qq.com 占 20.5% | 微信公众号/腾讯新闻是唯一高效路径 |
| 千问 | sm.cn（夸克）占 19.2% | 优化夸克收录=优化千问 |
| DeepSeek | Top8 仅 21.8%，无自家生态 | 唯一中立战场，内容质量导向回报最高 |
| 抖音 AI | 只引 iesdouyin 一个域名 | 外部内容进不去，不值得单独投入 |

## 榜单站霸榜

被引位置最靠前的域名里，maigoo（买购网）、cnpp（品牌网）、phb123（排行榜123）等榜单站密集出现——AI 回答"哪个好/怎么选"时最省事的做法就是抄现成榜单。**跨平台通吃层优先级**：

1. 榜单/品牌库：maigoo、chinapp、cnpp、phb123（覆盖 11 平台端，性价比最高且多数团队没做）
2. 内容平台：公众号/头条号；新闻媒体：sohu/163/sina；消费决策：smzdm
3. 平台生态层：按上表选你的目标引擎对应阵地
4. 专业内容层（B2B/技术）：cnblogs、csdn、zhihu、36kr

## Web 与 App 必须分开测

同产品两端信源重合度（Jaccard）：千问仅 24.5%、元宝 31.4%——**用 web 端结论推 App 端，四分之三是错的**。每个平台+终端单独记录、单独出指标。

## 复算方法（一手数据自主可验）

```bash
curl -sLO https://raw.githubusercontent.com/yaojingang/GEOLab/main/03-cn-geo-citation-dataset/data/marts/source_visibility.parquet
python3 -m venv .venv && .venv/bin/pip install duckdb
```
```python
import duckdb
c = duckdb.connect()
c.sql("""SELECT domain, sum(deduplicated_citation_count) cit,
        count(DISTINCT platform_code) plats
        FROM 'source_visibility.parquet'
        GROUP BY domain ORDER BY cit DESC LIMIT 25""").show()
```

## 延伸阅读

- 数据总仓 GEOLab：https://github.com/yaojingang/GEOLab
- 中文引擎分引擎打法：[中文 AI 引擎生态](07-chinese-ai-engines.md)
- 第三方阵地方法论：[第三方声量建设](../advanced/05-third-party-presence.md)

---
*上一篇：[提示词与问题集研究](09-prompt-research.md) ｜ 下一篇：[新站冷启动](11-cold-start.md)*
