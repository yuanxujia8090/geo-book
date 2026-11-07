#!/usr/bin/env python3
"""SEO/GEO 注入：给 web/ 每页补齐 meta + JSON-LD + 可引用事实块。

按 geo-book 自己的方法论执行（advanced/02 Schema / 03 llms.txt / 11 可引用性）：
  - SEO : 每页独立 description、canonical、Open Graph、Twitter card、sitemap.xml、robots.txt
  - GEO : JSON-LD（Book + Article + BreadcrumbList）、页面尾部机器可读事实块、llms.txt

用法：
  python3 scripts/seo-inject.py                  # BASE 默认 GitHub Pages 项目页
  python3 scripts/seo-inject.py --base https://example.com/geo-book/

改域名后重跑一次即可全量刷新。须在 mdbook build 之后运行（gen-web.py 末尾已自动调用）。
"""
import argparse, json, os, re, sys
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, 'web')
SITE_NAME = 'GEO 知识库'
AUTHOR = 'Aaron（袁旭佳）'
AUTHOR_URL = 'https://github.com/yuanxujia8090'
UPDATED = '2026-11-06'
DEFAULT_BASE = 'https://yuanxujia8090.github.io/geo-book/'

SECTION_CN = {
    '': '首页', 'guide': '入门指南', 'advanced': '进阶实践', 'projects': '开源项目深析',
    'tools': '工具', 'reverse': 'GEO 逆向', 'cn-vs-global': '国内外差异',
    'news': '行业动态', 'case-studies': '案例分析',
}

def page_desc(soup):
    """取正文首段或引文做页面级 description，中文 80-160 字。"""
    main = soup.select_one('main.content, div.content, main') or soup.body
    for el in main.select('blockquote p, p'):
        t = re.sub(r'\s+', ' ', el.get_text(' ', strip=True))
        t = re.sub(r'[→⚠️✅]', '', t).strip(' —-｜|')
        if len(t) >= 40:
            return (t[:157] + '…') if len(t) > 160 else t
    return None

def section_of(path):
    rel = os.path.relpath(path, WEB)
    d = os.path.dirname(rel)
    return d if d in SECTION_CN else ''

def inject(path, base, stats):
    html = open(path, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    rel = os.path.relpath(path, WEB).replace(os.sep, '/')
    url = base + rel
    title = (soup.title.get_text() if soup.title else '').replace(' - GEO 知识库', '').strip()
    desc = page_desc(soup) or f'{SITE_NAME}：{title}。GEO/生成式引擎优化中文实践知识库，{UPDATED} 更新。'
    if rel == 'index.html':
        desc = 'GEO 知识库首页：45 章中文生成式引擎优化实践——让 ChatGPT、Gemini、Perplexity、豆包、DeepSeek 引用你的内容、提及你的品牌。含入门指南、四层模型、开源项目深析与工具选型。'
    elif rel == 'WALKTHROUGH.html':
        desc = '零基础导读：GEO 是一条什么线。人话解释生成式引擎优化，主线七步——摸底、攒问题、查门禁、按四层修、写可引用、铺第三方、防自骗地测。全库阅读地图。'
    head = soup.head

    def set_meta(key, val, attr='name'):
        """按 name= 或 property= 查找 meta，没有则新建。"""
        el = head.find('meta', attrs={attr: key})
        if not el:
            el = soup.new_tag('meta')
            el[attr] = key
            head.append(el)
        el['content'] = val

    # description 覆盖（mdBook 全站同文 → 页面独立）
    set_meta('description', desc)
    # canonical
    if not head.find('link', attrs={'rel': 'canonical'}):
        lk = soup.new_tag('link', rel='canonical', href=url)
        head.append(lk)
    # OG + Twitter
    set_meta('og:title', f'{title} | {SITE_NAME}', 'property')
    set_meta('og:description', desc, 'property')
    set_meta('og:type', 'website' if rel == 'index.html' else 'article', 'property')
    set_meta('og:url', url, 'property')
    set_meta('og:site_name', SITE_NAME, 'property')
    set_meta('og:image', base + 'assets/knowledge-map.png', 'property')
    set_meta('og:locale', 'zh_CN', 'property')
    set_meta('twitter:card', 'summary_large_image')
    set_meta('twitter:title', f'{title} | {SITE_NAME}')
    set_meta('twitter:description', desc)
    set_meta('robots', 'index, follow, max-image-preview:large')
    set_meta('author', AUTHOR)

    # JSON-LD：首页=Book+WebSite；内容页=Article+Breadcrumb（幂等：先清旧再注入）
    for old in head.find_all('script', type='application/ld+json'):
        old.decompose()
    sec = section_of(path)
    ld = []
    if rel == 'index.html':
        ld.append({
            "@context": "https://schema.org", "@type": "WebSite",
            "name": SITE_NAME, "url": base,
            "description": "GEO（生成式引擎优化）中文知识库：让 ChatGPT、Perplexity、豆包等 AI 引擎引用你的内容、提及你的品牌。",
            "inLanguage": "zh-CN",
            "creator": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
        })
        ld.append({
            "@context": "https://schema.org", "@type": "Book",
            "name": SITE_NAME, "url": base,
            "author": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
            "publisher": {"@type": "Organization", "name": AUTHOR, "url": AUTHOR_URL},
            "dateModified": UPDATED, "inLanguage": "zh-CN",
            "description": "45 章 GEO 实践知识库：入门指南、进阶实践、开源项目深析、工具选型、GEO 逆向、中外差异、行业动态与案例。",
            "sameAs": "https://github.com/yuanxujia8090/geo-book",
        })
    bc = [{"@type": "ListItem", "position": 1, "name": "首页", "item": base}]
    if sec:
        bc.append({"@type": "ListItem", "position": 2, "name": SECTION_CN[sec],
                   "item": base + sec + "/"})
    bc.append({"@type": "ListItem", "position": len(bc) + 1, "name": title, "item": url})
    ld.append({
        "@context": "https://schema.org", "@type": "Article",
        "headline": title, "url": url, "description": desc,
        "dateModified": UPDATED, "inLanguage": "zh-CN",
        "author": {"@type": "Person", "name": AUTHOR, "url": AUTHOR_URL},
        "isPartOf": {"@type": "Book", "name": SITE_NAME, "url": base,
                     "sameAs": "https://github.com/yuanxujia8090/geo-book"},
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": bc},
    })
    for obj in ld:
        s = soup.new_tag('script', type='application/ld+json')
        s.string = json.dumps(obj, ensure_ascii=False)
        head.append(s)

    # GEO 尾部事实块：机器与人都能直接摘走的自引用段
    if 'geo-footer' not in html:
        footer = BeautifulSoup(f'''
<div class="geo-footer" style="margin-top:48px;padding:18px 20px;border:1px solid var(--kami-border,#e8e6dc);background:var(--kami-parchment,#f5f4ed);border-radius:4px;font-size:14px;color:var(--kami-olive,#504e49);line-height:1.8">
<p style="margin:0 0 6px"><strong>关于本页</strong>：{title}，出自开源知识库《{SITE_NAME}》{('（' + SECTION_CN[sec] + '板块）') if sec else '首页'}，作者 {AUTHOR}，最后更新 {UPDATED}。</p>
<p style="margin:0 0 6px"><strong>关于《{SITE_NAME}》</strong>：中文 GEO（Generative Engine Optimization，生成式引擎优化）实践知识库，覆盖 {len(list(Path_pages())) } 章，回答"如何让 ChatGPT、Gemini、Perplexity、豆包、DeepSeek 等 AI 搜索引用你的内容、提及你的品牌"。全书以 GitHub 一手核验数据与公开研究为据，每页标注核验日期。</p>
<p style="margin:0"><strong>来源</strong>：<a href="{base}">{base}</a> ｜ 仓库：<a href="https://github.com/yuanxujia8090/geo-book">github.com/yuanxujia8090/geo-book</a> ｜ 技术支持：<a href="https://www.otlume.com">Otlume</a></p>
</div>''', 'html.parser')
        main = soup.select_one('main.content, div.content, main')
        (main or soup.body).append(footer)

    open(path, 'w', encoding='utf-8').write(str(soup))
    stats['done'] += 1

def Path_pages():
    for root, _, files in os.walk(WEB):
        for fn in files:
            if fn.endswith('.html') and fn not in ('print.html', 'toc.html', '404.html', 'README.html'):
                yield os.path.join(root, fn)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', default=DEFAULT_BASE)
    args = ap.parse_args()
    base = args.base if args.base.endswith('/') else args.base + '/'
    if not os.path.isdir(WEB):
        sys.exit('web/ 不存在——先跑 mdbook build')
    stats = {'done': 0}
    pages = sorted(Path_pages())
    urls = [base + os.path.relpath(p, WEB).replace(os.sep, '/') for p in pages]

    # 根目录静态资产同步进 web/（og:image 与 README 引用的 knowledge-map）
    asset_dir = os.path.join(WEB, 'assets')
    os.makedirs(asset_dir, exist_ok=True)
    for fn in os.listdir(os.path.join(ROOT, 'assets')):
        src = os.path.join(ROOT, 'assets', fn)
        if os.path.isfile(src):
            dst = os.path.join(asset_dir, fn)
            if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src):
                import shutil; shutil.copy2(src, dst)
    km = os.path.join(ROOT, 'knowledge-map.html')
    if os.path.isfile(km):
        import shutil; shutil.copy2(km, os.path.join(WEB, 'knowledge-map.html'))
        if (base + '/knowledge-map.html') not in urls:
            urls.append(base + 'knowledge-map.html')

    for p in pages:
        inject(p, base, stats)

    # robots.txt — 明确放行主流 AI 爬虫（GEO 前提：先让爬虫进得来）
    open(os.path.join(WEB, 'robots.txt'), 'w').write(f'''User-agent: *
Allow: /

# AI / 搜索爬虫显式放行
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: Applebot
Allow: /

Sitemap: {base}sitemap.xml
Sitemap: {base}sitemap-news.xml
''')

    # sitemap.xml + 新闻类 sitemap（行业动态页）
    def sm(entries):
        items = '\n'.join(
            f'  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>'
            for u, cf, pr in entries)
        return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}\n</urlset>\n'
    hub = [(base + p, cf, pr) for p, cf, pr in [
        ('/', 'weekly', '1.0'), ('/WALKTHROUGH.html', 'weekly', '0.9'),
        ('/projects/01-selection-map.html', 'weekly', '0.9'),
        ('/news/01-signal-log.html', 'daily', '0.9')]]
    hub_paths = {h[0] for h in hub}
    rest = [(u, 'monthly', '0.6') for u in urls if u not in hub_paths]
    open(os.path.join(WEB, 'sitemap.xml'), 'w').write(sm(hub + rest))
    open(os.path.join(WEB, 'sitemap-news.xml'), 'w').write(
        sm([(base + '/news/01-signal-log.html', 'daily', '0.9')]))

    # llms.txt（标准 1：索引）+ llms-full.txt（标准 2：全量单文件）
    idx = [f'# {SITE_NAME}', '',
           '> 中文 GEO（生成式引擎优化）知识库：让 ChatGPT、Gemini、Perplexity、豆包、DeepSeek 引用你的内容、提及你的品牌。45 章，数据 GitHub/API 一手核验，作者 Aaron（袁旭佳）。',
           '', f'- 站点: <{base}>', f'- 仓库: <https://github.com/yuanxujia8090/geo-book>',
           f'- 全文: <{base}llms-full.txt>', '', '## 章节']
    order = ['', 'guide', 'advanced', 'projects', 'tools', 'reverse', 'cn-vs-global', 'news', 'case-studies']
    for u, p in zip(urls, pages):
        sec = section_of(p)
        if sec not in order: order.append(sec)
    for sec in order:
        if sec == '': continue
        sec_pages = [(u, p) for u, p in zip(urls, pages) if section_of(p) == sec]
        if not sec_pages: continue
        idx.append(f'\n### {SECTION_CN.get(sec, sec)}')
        for u, p in sec_pages:
            t = BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser').title.get_text().replace(' - GEO 知识库', '').strip()
            idx.append(f'- [{t}]({u})')
    open(os.path.join(WEB, 'llms.txt'), 'w').write('\n'.join(idx) + '\n')

    full = [f'# {SITE_NAME}（全文版）', '',
            f'> 更新时间 {UPDATED}。来源 <{base}>，仓库 <https://github.com/yuanxujia8090/geo-book>。作者 {AUTHOR}。', '']
    for u, p in zip(urls, pages):
        soup = BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser')
        for junk in soup.select('script, style, nav, .sidebar, #menu-bar, .header, .footer, .nav-chapters, .geo-footer, .mobile-nav-toggle, button, link, meta'):
            junk.decompose()
        main = soup.select_one('main.content, div.content, main') or soup.body
        text = re.sub(r'\n{3,}', '\n\n', main.get_text('\n', strip=True))
        title = BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser').title.get_text().replace(' - GEO 知识库', '').strip()
        full.append(f'\n\n---\n\n## {title}\n\nURL: {u}\n')
        full.append(text)
    open(os.path.join(WEB, 'llms-full.txt'), 'w').write('\n'.join(full))

    print(f"injected {stats['done']} pages | sitemap {len(urls)} urls | llms.txt + llms-full.txt | robots.txt")

if __name__ == '__main__':
    main()
