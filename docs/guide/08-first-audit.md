# 上手首查：30 分钟站点自检

> 新手第一篇动手文：不装任何工具，30 分钟搞清楚"AI 现在能不能看到你"。

读完这篇你能独立完成：查 AI 引擎对你的现状认知、验证页面可达性、记录基线数据。这是所有后续优化的起点。

## 第 1 步：问引擎"你了解我吗"（5 分钟）

分别打开 ChatGPT（开联网搜索）、Perplexity、豆包/Kimi（中文站），问：

```
[SystemX 是什么？它解决什么问题？和竞品比怎么样？]
```

记录三件事：
1. AI 认不认识这个产品/品牌（完全不知道 = 可见度为 0，问题很大）。
2. AI 说的对不对（说错 = 训练数据里有脏信息，需要纠正层）。
3. AI 引用了哪些域名（这些就是你的目标信源类型，也暴露竞品在哪些阵地）。

## 第 2 步：问"推荐类"问题（10 分钟）

用 5-10 个用户真实会问的推荐句式（详见[提示词研究](09-prompt-research.md)）：

```
推荐几个适合 [目标人群] 的 [品类]
[SystemX] 和 [竞品Y] 哪个好？
[品类] 怎么选？
```

记录：你出现吗？排第几？竞品谁出现？答案引用了哪些来源页面？——**被引用的来源页面就是你的"作业范本"**，逐页打开看它们长什么样。

## 第 3 步：验证爬虫可达性（10 分钟）

```bash
# 1. robots.txt 是否误拦 AI 爬虫
curl -s https://你的域名/robots.txt

# 2. 关键页面对爬虫是否返回完整 HTML（不是空壳）
curl -s -A "OAI-SearchBot" https://你的域名/关键页 | grep -c "正文关键词"
# 命中数 >0 说明内容在 HTML 里；=0 说明内容靠 JS 渲染，AI 看不到（见进阶-技术可达性）

# 3. sitemap 是否存在且包含关键页
curl -s https://你的域名/sitemap.xml | grep -c "<loc>"
```

## 第 4 步：填首查记录表（5 分钟）

| 引擎 | 认识品牌? | 信息准确? | 引用域名 | 你被引用? |
|------|----------|----------|---------|----------|
| ChatGPT | ☐ | ☐ | | ☐ |
| Perplexity | ☐ | ☐ | | ☐ |
| AI Overviews | ☐ | ☐ | | ☐ |
| 豆包 | ☐ | ☐ | | ☐ |

这张表就是你的 Day 0 基线。之后每两周重跑一次同样问题（问题集冻结不许改，见[度量篇](../advanced/07-measurement.md)），对比变化。

## 结果解读

- **不认识 + HTML 无内容** → 先修技术层（[进阶-技术可达性](../advanced/09-technical-accessibility.md)）。
- **认识但说错** → 建事实源页面 + llms.txt + Schema（advanced/02、03）。
- **认识、正确、但推荐时不出现** → 内容层与第三方声量问题（advanced/01、05）。
- **已经偶尔出现** → 直接进入工作流放大（advanced/08）。

## 延伸阅读

- 免费手工监测协议（含表格模板）：https://www.wizgrowth.com/blog/how-to-track-ai-citations-manually/
- 无预算七步跟踪法：https://deepsmith.ai/blog/track-ai-citations-no-budget
- ChatGPT 引文跟踪工作流：https://www.earlyseo.com/blogs/how-to-track-chatgpt-citations

---
*上一篇：[中文 AI 引擎生态](07-chinese-ai-engines.md) ｜ 下一篇：[提示词与问题集研究](09-prompt-research.md)*
