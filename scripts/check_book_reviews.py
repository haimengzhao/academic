#!/usr/bin/env python3
"""Validate bilingual migration fidelity and rendered local pages (stdlib only)."""
import json
import html
import hashlib
from urllib.parse import urlsplit
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'public'
SLASH = chr(92)
MATH = re.compile(re.escape(SLASH + '(') + '.*?' + re.escape(SLASH + ')') + '|' + re.escape(SLASH + '[') + '.*?' + re.escape(SLASH + ']'), re.S)
ALLOWED = {'p', 'a', 'b', 'strong', 'em', 'i', 'code', 'sup', 'sub', 's', 'del', 'br', 'li', 'ul', 'ol', 'small'}


# Author-requested exception: retain link text, remove retailer purchase links.
SHOP_DOMAINS = ('jd.com', 'amazon.com', 'dangdang.com', 'taobao.com', 'tmall.com')

def without_purchase_links(text):
    def unwrap(match):
        host = (urlsplit(html.unescape(match.group(1))).hostname or '').lower()
        if any(host == domain or host.endswith('.' + domain) for domain in SHOP_DOMAINS):
            return match.group(2)
        return match.group(0)
    return re.sub(r'<a href="([^"]+)">(.*?)</a>', unwrap, text, flags=re.S)


class Fragment(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.items = 0
        self.text = []

    def handle_starttag(self, tag, attrs):
        assert tag in ALLOWED, f'Unexpected HTML tag: {tag}'
        attrs = dict(attrs)
        assert set(attrs) <= {'href', 'start', 'id'}, f'Unexpected attributes: {attrs}'
        if tag == 'a':
            url = attrs['href']
            assert url.startswith(('https://', 'http://', '/post/', '#ref_')), url
            self.links.append(url)
        if tag == 'li':
            self.items += 1

    def handle_data(self, data):
        self.text.append(data)


class RenderedReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = Counter()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id', '').startswith('ref_'):
            self.ids[attrs['id']] += 1
        if attrs.get('href', '').startswith('#ref_'):
            self.targets.append(attrs['href'][1:])


count = formulas = links = 0
source_files = sorted((ROOT / 'docs/book-review-migration').glob('*.source.json')) + sorted((ROOT / 'docs/article-migration').glob('*.source.json'))
for source_file in source_files:
    source = json.loads(source_file.read_text())
    folder = ROOT / 'content/post' / source['slug']
    if 'layout: original-article' in (folder / 'index.md').read_text():
        source_text = (folder / 'index.md').read_text()
        assert not (folder / 'bilingual.json').exists(), 'Removed translation must not be published as a resource'
        rendered = (OUTPUT / 'post' / source['slug'] / 'index.html').read_text()
        assert 'original-article' in rendered
        assert 'reading-toolbar' not in rendered and 'js/book-review.js' not in rendered
        assert 'chinese_title:' not in source_text
        position = source_text.index('---', 3) + 3
        for original in source['blocks']:
            anchor = 'id="' + original['id'] + '"'
            start = source_text.index(anchor, position)
            if original['en']:
                assert original['en'] in source_text[start:source_text.index('</div>', start)], original['id']
            if original['kind'] == 'figure':
                assert (folder / original['image']).is_file()
                assert original['image'] in rendered
            position = start + len(anchor)
        print(f'{source["slug"]}: all {len(source["blocks"])} original blocks retained; English-only page OK')
        continue
    article = json.loads((folder / 'bilingual.json').read_text())
    original_language = source.get('source_language', 'zh')
    translated_language = 'zh' if original_language == 'en' else 'en'
    assert len(article['blocks']) == len(source['blocks'])
    assert len({b['id'] for b in article['blocks']}) == len(article['blocks'])
    for original, block in zip(source['blocks'], article['blocks']):
        location = f'{source_file.stem}/{block["id"]}'
        assert (block['id'], block['kind']) == (original['id'], original['kind']), location
        assert block[original_language] == without_purchase_links(original[original_language]), f'Original changed: {location}'
        assert block['en'] == without_purchase_links(block['en']), f'Purchase link remains: {location}'
        assert 'editorial_note' not in block, f'Unrequested commentary: {location}'
        if source_file.name == '408967061.source.json' and block['id'] == 'b121':
            assert block['en'] == original['zh'], 'Original English poem must remain verbatim'
        if block['kind'] == 'rule':
            assert not block[translated_language]
            continue
        if block['kind'] == 'figure':
            assert block['image'] == original['image'] and (folder / block['image']).is_file(), location
            if not block[original_language].strip():
                assert not block[translated_language].strip(), 'Do not invent figure captions'
                count += 1
                continue
        assert block[translated_language].strip(), f'Missing translation: {location}'
        assert not any(ord(c) < 32 and c not in '\n\t' for c in block['en']), location
        zh, en = Fragment(), Fragment()
        zh.feed(block['zh'])
        en.feed(block['en'])
        assert Counter(zh.links) == Counter(en.links), f'Link mismatch: {location}'
        assert zh.items == en.items, f'List-item mismatch: {location}'
        assert Counter(MATH.findall(block['zh'])) == Counter(MATH.findall(block['en'])), f'Formula mismatch: {location}'
        formulas += len(MATH.findall(block['zh']))
        links += len(zh.links)
        count += 1
    frontmatter = (folder / 'index.md').read_text()
    assert 'external_link:' not in frontmatter
    assert source['source_url'] in frontmatter
    rendered = (OUTPUT / 'post' / source['slug'] / 'index.html').read_text()
    refs = RenderedReferences()
    refs.feed(rendered)
    assert all(refs.ids[target] == 1 for target in refs.targets), 'Missing or duplicated footnote target'
    assert 'book-review-header' in rendered and 'js/book-review.js' in rendered
    assert 'book-review-note' not in rendered, 'Unrequested introductory note'
    assert 'Short excerpt; the original article' not in rendered
    assert ('English original' if original_language == 'en' else 'English translation') in rendered
    assert 'data-mode=parallel' in rendered or 'data-mode="parallel"' in rendered
    for block in article['blocks']:
        assert re.search(r'id=["\x27]?' + re.escape(block['id']) + r'(?:["\x27\s>])', rendered), block['id']
    if source.get('cover'):
        assert (folder / source['cover']).is_file()
        assert source['cover'] in rendered
    print(f'{source["slug"]}: {len(article["blocks"])} paired source blocks; local page OK')
print(f'PASS: {count} non-rule blocks verified, {formulas} matching formulas, {links} matching reference links; Original-language text preserved; retailer hyperlinks removed as requested.')

assets_file = ROOT / 'docs/article-migration/assets.json'
if assets_file.is_file():
    for asset in json.loads(assets_file.read_text()):
        path = ROOT / 'content/post' / asset['slug'] / asset['file']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == asset['sha256'], path
    print(f'PASS: all {len(json.loads(assets_file.read_text()))} original image files retain their captured hashes.')
