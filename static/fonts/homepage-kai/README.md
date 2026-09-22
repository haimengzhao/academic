# Homepage Kai webfont

Derived from FandolKai Regular v0.3 by the Fandol team (Clerk Ma and Jie Su).
Source: https://ctan.org/pkg/fandol
License: GPL v3 with font exception; see COPYING and UPSTREAM-README.txt.
The upstream OTF and subset build script are included in this directory.

The derived family is renamed Homepage Kai. Changes: CJK-only subsetting,
WOFF2 compression, font family renaming. Glyph outlines are unchanged.
Preview and article characters load separately; remaining glyphs are split into
1024-character subsets. CSS unicode-range loads only the needed subsets.
Latin text continues to use Google Sans. No third-party font requests are needed.

Rebuild with scripts/build_kai_webfont.py and fonttools[woff].
Source OTF SHA-256: ea7e7fb4f9b3ac694a68d43946e04d21deed6e8c29a7c2d3081e1a4138f2f827
