# Haimeng Zhao's academic website

A Hugo site with Markdown publications, posts, talks, and an Academic-based
layout. The current presentation uses self-hosted Google Sans, a warm neutral background,
green accents, responsive publication rows, and light/dark themes.

## Build and preview

Install **Hugo Extended 0.166.0** from the official
[Hugo releases](https://github.com/gohugoio/hugo/releases/tag/v0.166.0).
The Extended build is required for the theme's Sass styles.

```sh
git submodule update --init --recursive
hugo version
./view.sh
```

Open <http://localhost:1313/>. To produce the static site:

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_site_links.py public
```

Netlify uses the same Hugo version, pinned in `netlify.toml`. Previewing and
building locally do not deploy the site.

## Editing

- Biography: `content/authors/admin/_index.md`
- Homepage sections: `content/home/`
- Publications and BibTeX: `content/publication/`
- Posts: `content/post/`
- CV: `static/files/CV.pdf` (case-sensitive)
- Navigation and settings: `config/_default/`
- Visual design: `assets/scss/custom.scss`, `data/themes/editorial.toml`,
  and `data/fonts/editorial.toml`

## Compatibility and dependencies

The Academic submodule remains pinned at
`4549c9bde91f21201d22fb35dd849ae9a4ba8e61`. This is a compatibility update
of the existing site, not a migration to a new Academic/Wowchemy content model.
Project-level templates in `layouts/` override the legacy Hugo APIs, author
lookup, web manifest link, navigation accessibility, and publication layout.
The source theme is MIT-licensed; see `themes/academic/LICENSE.md`.

Frontend updates:

- jQuery 3.7.1 (compatible with Bootstrap 4)
- Bootstrap JavaScript bundle 4.6.2, including Popper
- highlight.js 11.11.1, using `highlightAll()`

`data/assets.toml` pins CDN assets and their integrity hashes. The remaining
legacy dependencies and Bootstrap Sass remain at the pinned theme's versions;
a full Bootstrap 5 / modern-theme migration is separate work. When changing
CDN files, update their SRI hashes too. Retest search, citations, theme switching,
mobile navigation, publication archives, math, and code highlighting.

The contact form still uses Netlify Forms and must be tested on the deployed
Netlify site. No form submissions are made by local checks. Existing third-party
comments, analytics, and CMS configuration are retained; they are not validated
by a successful Hugo build.

Google Sans webfonts in `static/fonts/google-sans/` are sourced from Google Fonts
and licensed under the included SIL OFL. WOFF2 subsets retain Latin (including
IPA), Greek, Cyrillic, punctuation, and mathematical symbols; Chinese text uses self-hosted Fandol Kai subsets in `static/fonts/homepage-kai/`,
with the upstream font, license, and reproducible build script included. Typography uses 20px desktop / 18px mobile body text,
1.65 line height, and compact publication actions (30px desktop / 36px mobile).

## Bilingual book reviews

The three `content/post/maths-physics-book-reviews-*/` bundles are complete
local articles. Their original URLs are in `original_url`, not `external_link`.
Each `bilingual.json` contains ordered blocks with stable IDs, a block kind,
and Chinese (`zh`) / English (`en`) HTML. Keep each paragraph or list paired
when editing; retain original formulas and reference links in both languages.

- Layout: `layouts/_default/book-review.html`
- Content renderer: `layouts/shortcodes/book-review.html`
- Reading-mode enhancement: `static/js/book-review.js`
- Styling: the book-review section of `assets/scss/custom.scss`
- Source snapshots, exclusions, and migration record: `docs/book-review-migration/`

The default is Chinese-left / English-right, with pairs stacked below 900px.
The full article works without JavaScript; JavaScript adds single-language
reading modes. MathJax typesets the preserved TeX formulas. The original slugs
and publication dates are retained, including the historical `2022-fall` slug
whose displayed title follows the original second-year autumn/winter wording.

After changes, run:

```sh
hugo --gc --minify --panicOnWarning
python3 scripts/check_book_reviews.py public
python3 scripts/check_site_links.py public
```

The migration keeps the author's historical opinions and reading status;
it is a translation, not an update of the scientific claims. The original prose, quotations (including the complete Eliot passage), and
book-card titles are preserved; retailer purchase hyperlinks are removed at the author’s request. Only platform-generated keyword
search links and commerce UI (live prices, purchase buttons, ad badges, and
shopping thumbnails) are omitted. Every normalized Chinese block is checked
against the saved source snapshots without exceptions. Do not add editorial
notes or explanatory prefaces to the articles. Translate the informal voice,
including jokes, parenthetical asides, enthusiasm, criticism, and uncertainty,
without summarizing or softening it.


## Bilingual maths and physics articles

The eigenvalue, entropic-uncertainty, spacetime-diagram, and conformal-mapping
posts use the same bilingual renderer. Their source records and original asset
hashes are in `docs/article-migration/`. The original covers and eight body
figures are local page resources, kept byte-for-byte; captions are translated
without redrawing or relabeling the original diagrams. Figures open at full
resolution when clicked. Footnote IDs are scoped per language at render time.

`python3 scripts/check_book_reviews.py public` now checks seven bilingual articles and the English-only Quantum AI article, including inline/display TeX, original-image hashes, and footnote
targets. The four new articles preserve the original exposition, qualifications,
quotations, and technical claims rather than editing the mathematics or physics.


## Quantum AI: English original

`content/post/unleashing-the-advantage-of-quantum-ai/` hosts only the complete
English Quantum Frontiers original, at the author's request. The text lives in
`index.md`; all four original illustrations remain local resources. The page
uses `layouts/_default/original-article.html`, with a single reading column and
no translation or language controls. The immutable reference is
`docs/article-migration/quantum-ai.source.json`, checked by the migration validator.
