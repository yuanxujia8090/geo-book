#!/usr/bin/env python3
"""从 docs/ 结构生成 mdBook 的 src/SUMMARY.md，然后本地构建。

mdBook 约束：SUMMARY.md 必须在 src 目录内；分组标题必须写成 [标题]()。
用法：python3 scripts/gen-web.py            # 生成 SUMMARY + 构建到 web/
      python3 scripts/gen-web.py --serve    # 构建后起本地预览 :8899
"""
import os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'docs')

SECTIONS = [
    ('guide', '一、入门指南'),
    ('advanced', '二、进阶实践'),
    ('projects', '三、开源项目深析'),
    ('tools', '四、工具'),
    ('reverse', '五、GEO 逆向'),
    ('cn-vs-global', '六、国内外差异'),
    ('news', '七、行业动态'),
    ('case-studies', '八、案例分析'),
]

def title_of(path):
    text = open(path, encoding='utf-8').read()
    m = re.search(r'^# (.+)$', text, re.M)
    return m.group(1).strip() if m else os.path.basename(path)[:-3]

def main():
    out = ['# Summary', '', '- [导读：GEO 是一条什么线](WALKTHROUGH.md)']
    for d, label in SECTIONS:
        out.append(f'- [{label}]()')
        for f in sorted(x for x in os.listdir(os.path.join(SRC, d)) if x.endswith('.md')):
            out.append(f'  - [{title_of(os.path.join(SRC, d, f))}]({d}/{f})')
    summary_path = os.path.join(SRC, 'SUMMARY.md')
    old = open(summary_path, encoding='utf-8').read() if os.path.exists(summary_path) else ''
    new = '\n'.join(out) + '\n'
    if old != new:
        open(summary_path, 'w', encoding='utf-8').write(new)
        print(f'SUMMARY.md generated: {len(out)-2} chapters')
    else:
        print('SUMMARY.md unchanged')
    r = subprocess.run(['mdbook', 'build'], cwd=ROOT)
    if r.returncode != 0:
        sys.exit('mdbook build FAILED')
    s = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'seo-inject.py')], cwd=ROOT)
    if s.returncode != 0:
        sys.exit('seo-inject FAILED')
    print('web/ built OK')
    if '--serve' in sys.argv:
        subprocess.run(['python3', '-m', 'http.server', '8899', '--directory', os.path.join(ROOT, 'web')])

if __name__ == '__main__':
    main()
