#!/usr/bin/env python3
"""Check root-relative links and assets in Hugo's rendered HTML."""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(sys.argv[1] if len(sys.argv) > 1 else 'public')
if not (root / 'index.html').is_file():
    raise SystemExit(f'Build the site first: {root}/index.html is missing')
missing = {}
checked = 0


class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global checked
        for key, value in attrs:
            if key not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.netloc and url.netloc != 'hmzhao.me':
                continue
            if not url.path.startswith('/'):
                continue
            checked += 1
            target = root / unquote(url.path).lstrip('/')
            if not target.is_file() and not (target / 'index.html').is_file():
                missing.setdefault(url.path, set()).add(str(page.relative_to(root)))


for page in root.rglob('*.html'):
    if page.relative_to(root).parts[0] == 'admin':
        continue
    Links().feed(page.read_text())
for url, pages in sorted(missing.items()):
    print(f'Missing {url}: {", ".join(sorted(pages))}')
print(f'Checked {checked} internal links/assets; {len(missing)} missing targets.')
sys.exit(bool(missing))
