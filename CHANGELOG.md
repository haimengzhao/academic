# Changelog

## 2026-09-21 — Software compatibility and visual refresh

- Pin Netlify to Hugo Extended 0.166.0 and update the local preview flag.
- Restore the pinned Academic submodule and add project-level overrides for
  current Hugo data, locale, pagination, author paths, Sass, and manifest URLs.
- Update jQuery to 3.7.1, Bootstrap JS to 4.6.2 (bundle with Popper), and
  highlight.js to 11.11.1. Keep compatible legacy dependencies explicitly pinned.
- Add an editorial light/dark style with local system fonts, restrained color,
  responsive typography, a smaller portrait, and structured publication rows.
- Label icon controls, correct the mobile menu's ARIA target, fix the theme
  dropdown's conflicting hover handler, and support reduced motion in CSS.
- Fix case-sensitive CV URLs and the footer copyright entity.
- Preserve biography, research statements, publication records, posts, and URLs.

Validation:

- Hugo production build with `--gc --minify --panicOnWarning`: passed, 175 pages,
  no warnings.
- `scripts/check_site_links.py`: 1,525 internal references, zero missing targets.
- Browser: search returned 11 results for `quantum`; BibTeX dialog loaded;
  light/dark selection and mobile section navigation worked; 390px viewport
  had no horizontal overflow; LaTeX code block received syntax highlighting.
- `git diff --check`: passed.

Remaining scope: the pinned Academic theme and some frontend libraries remain
legacy; this is not a full theme/framework migration. Netlify form submission,
third-party comments, analytics, and CMS were not tested. No deployment or
publication was performed.

### Typography refinement

- Switch to self-hosted Google Sans with regular/italic variable WOFF2 fonts
  and the upstream OFL license; compressed subsets total approximately 450 KB.
- Increase body text to 20px on desktop and 18px on phones, with 1.65 line height;
  use larger metadata, controlled paragraph width, and 44px button targets.
- Preserve the tightened Education spacing.
- Verify rendered desktop/mobile sizes and no horizontal overflow at 390px.

### Introduction and publication actions

- Reduce publication buttons to 30px on desktop and 36px on phones.
- Separate the opening introduction from motivation, group research questions,
  and place the unchanged background paragraph in a native expandable section.
- Verify the production build, internal links, and disclosure interaction.

### Layout refinement after visual review

- Reduce Welcome to 36px on desktop / 32.4px on phones and tighten top spacing.
- Keep all introduction wording and links; split the longer background into two
  plain paragraphs.
- Put the Publications heading above the full-width list and emphasize the site
  owner's name, preserving equal-contribution markers and author links.
- Use a 100px portrait alongside name/affiliation on mobile, followed by social
  links. Keep 18px body text and existing compact publication actions.
- Production build and 1,525 internal references pass; browser checks cover the
  desktop layout and mobile first screen.

## 2026-09-21 — Local bilingual book reviews

- Migrate the three existing Zhihu book-review entries to complete local posts,
  preserving their slugs, publication dates, Chinese prose, formulas, and
  reference links. Display semester names from the original Chinese titles.
- Add faithful English translations, aligned by source block, plus a bilingual
  contents list and Chinese / English / parallel reading modes.
- Use two columns on desktop and paired stacked blocks on mobile. Constrain
  long formulas to their own scrollable region.
- Preserve historical opinions, reading-status qualifiers, complete quotations,
  and book-card titles and links. Remove only platform UI, auto-linked keyword
  searches, and live commerce presentation.
- Add saved normalized sources and a migration verifier for Chinese fidelity,
  formula/reference/list parity, block coverage, and local article rendering.

### Source-fidelity and translation-voice correction

- Restore the complete original Eliot quotation in both columns, including
  its line breaks and attribution, and remove the added introductory notices.
- Restore 23 original book-card titles and links at their source positions.
- Review all English blocks and revise neutralized or over-explained wording
  to retain the author's enthusiasm, criticism, self-mockery, and informal voice.
- Chinese equality now has no exceptions: 265 blocks, 18 formulas, and 88
  reference links. The translation verifier also checks list lengths.


### Four additional bilingual articles

- Migrate the existing eigenvalue, entropic-uncertainty, spacetime-diagram, and
  conformal-mapping links into complete local bilingual articles.
- Preserve 426 source blocks and 321 formulas, with original dates and slugs;
  translate all prose and captions without new editorial notes.
- Host eight original body figures and four covers locally, preserving hashes.
- Extend the shared renderer for figures and language-scoped footnotes; retain
  parallel, Chinese-only, English-only, and narrow-screen reading modes.

### Contextual English polish

- Review all seven posts against their high-school and university settings;
  revise 39 English blocks in six articles.
- Clarify physics Olympiads, student research competitions, science-fair peer
  groups, provincial teams, training camps, and school/university admissions.
- Preserve the regular-school-grades meaning of 综合 rather than “all-rounder.”
- Clarify undergraduate research supervision, graduate-level coursework, and
  practical courses, while keeping the author's informal voice.
- Keep Chinese prose, formulas, original quotations, links, and images intact.


### Quantum AI article migration

- Replace the Quantum Frontiers redirect with a local bilingual article.
- Preserve all 28 original blocks, including four illustrations and reference
  links; translate the prose into Chinese without adding editorial notices.
- Extend source-language checks and reader labels for an English original.
- Preserve the existing title, date, slug, and homepage summary.

### Quantum AI: English only

- Remove the declined Chinese translation, translated title, and reading-mode
  controls from this article. Keep the complete English original and four
  illustrations in a single-column local page.

### English-first article titles

- Promote English titles and retain Chinese titles as subtitles for the seven
  bilingual posts; label source and translation in English.
- Use freshman/sophomore college-year terminology consistently in book-review
  titles, headings, prose, and cross-links.

### Final homepage presentation and release validation

- Use Google Sans for Latin text and self-hosted Fandol Kai for Chinese, with
  unicode-range subsets, source font, build script, and license notices.
- Keep educational background in the biography; omit the duplicate Education block.
- Align Publications, Recent Posts, and Contact with the portrait's left edge.
- Keep six profile icons in two rows and six contact icons in one row.
- Refine publication search and literal-text filtering, archive links, row spacing,
  English-first post previews, and mobile book-review title hierarchy.
- Retain the approved biography and correct “at the intersection.”
- Release validation: 175 pages; 1,600 internal references with no missing targets;
  seven bilingual articles and the English-only Quantum AI original verified;
  all 16 original image hashes intact.
