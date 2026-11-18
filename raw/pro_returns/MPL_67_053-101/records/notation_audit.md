# Final notation audit before context

The primary transcriber personally compared recurring signs across the 47 page fragments and their images after completing the second image reading. No OCR or transcription subagent was used. This audit precedes the transcription freeze and the opening of context contents.

## Image-based decisions

- The unit-disc letter has a doubled stem: `\mathbb D`; its interior circle generally lies at upper right: `\mathbb D^\circ` (56–74). Arbitrary discs on 65 use plain `D_i^\circ`. The circle over `D` on 79 is positioned above the letter and remains `\mathring D`.
- Circled section marks are 2 on 56 and 3 on 58; the first mark on 54 remains `\unsure{1|A}`. They are not normalized as A/B/C.
- The tangent line on 62–63 has plain `T`; the apparent overbar in the first pass on 62 was rejected. Actual bars on 53 remain.
- `T^*` and `T^{\vee *}` remain distinct on 75–78. A star is not silently made into a dual sign. Single, double and triple primes on 74–78 remain ticks; the separated vertical stroke and dot on 101 is the exponent `^!`.
- `\Gamma` for the normalizer is distinct from the curled symmetric-group glyph, which remains `\unsure{\mathfrak S}`. The angular partition/subset P on 84–86 does not securely determine an alphabet and is consistently `\unsure{P|\mathcal P}`.
- Literal equals signs serving as a verbal abbreviation are retained on 61, 68, 70, 73, 78, 80, 88, 97 and 98; the full word *même* on 58 is retained. The uncertain/cancelled occurrences on 53 and 60 are not silently expanded or normalized.
- `X(J)`, an overwritten `Z|X`, and later `Z(J)` on 88 remain different as written. `a_i` and `x_i`, and `E'_a` and `E_{a'}`, are not harmonized from mathematical expectation.
- The visible radical in the quadratic ratio on 98 remains `\sqrt3`; the period formulas on 99 remain as written. No mathematical correction was made.
- Underlining, double underlining, quotient bars, frontier delta, dotted U, interval bars, ordered triples, and primes were compared during the second image reading. Double quotation marks are encoded as two backticks and two apostrophes.
- Reused printed sheets 92 and 96 retain their printed job text and character banners. Character counts/spacing and characters underneath colored ink are lower-confidence readings; uncertainty is explicit on the obscured FATAR banner.
- Added emphasis rules and enclosures found on 84, 88, 97, 99 and 100 were entered in the inventory. No scan image was inserted. The complex colored drawing on 96 carries its crop-candidate comment after the best TikZ approximation.
- A stray `\mathbb` introduced in front of the prose heading *Découpe* on 56 during a prior disk-letter replacement was removed against the ink.

## LaTeX validation before freeze

A local pdfTeX LaTeX format was generated from the installed distribution because no prebuilt format/database was discoverable. The full combined fragment passed a draft-mode compilation with `support/compile_check.tex`; the final log contains no undefined commands, math-mode errors, missing-character notices, or overfull/underfull boxes. The local font-map warning and draft-mode warning concern this environment, not the fragment's mathematical content.

Seventeen tikz-cd environments were given `ampersand replacement=\&`, with their cell separators encoded as `\&`, so they can be passed inside the required state macros. Missing math delimiters around isolated cancelled formulas on 84, 86, 91, 93 and 98 were supplied. Accented operator names *Déc* and *dist. géod* were placed in `\text` inside `\operatorname` to preserve their accents. These are typesetting changes, not reading changes.

The support wrapper is a syntax-check device: it color-codes page states and does not aim to reproduce the layout or strikeout geometry of the original. Its 48 output pages include a separate cote heading and must not be confused with the 47 source scan pages or their author pagination. No PDF is offered as a second transcription.
