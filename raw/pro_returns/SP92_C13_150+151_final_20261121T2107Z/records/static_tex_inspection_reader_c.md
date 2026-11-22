# Static TeX inspection — reader C

## Scope

Read-only inspection of all 25 current files in `pages/` and the supplied source `PREAMBLE.tex`. No manuscript images, witnesses, sealed readings or comparison data were used; no TeX engine was run. This report records the pre-repair snapshot. Root subsequently authorized and completed the encoding-only repairs listed below; `records/static_tex_encoding_repairs_reader_c.json` records every changed file, exact JSON leaf and before/after hash.

Inspection timestamp: 2026-11-21T20:47:59.349471+00:00.

## Definite source issues

| Current file and location | Issue | Reading-preserving structural repair |
| --- | --- | --- |
| `pages/151_scan003.tex`, lines 9–11 | `\deleted{\diagram{\begin{tikzcd}...}}` sends the paragraph-producing `\diagram` directly into text-mode `\sout`. The preamble defines `\diagram` with `\par`/`center` and `\deleted` with ulem. | Put `\diagram` outside the cancellation, and box the complete drawing: `\diagram{\deleted{\mbox{\begin{tikzcd}...\end{tikzcd}}}}`. |
| `pages/151_scan003.tex`, lines 26, 37, 48 and 49 | Four `\deleted{\[...\]}` constructions put display delimiters directly into text-mode `\sout`. | Keep the same formula and cancellation state, using `\[\deleted{...}\]`. |
| `pages/150_scan099.tex`, line 46 | `\unsure{V}_{...}^{...}` receives `^{?}` from the math branch of `\unsure`, followed by a second superscript on the same atom. | Group the already marked base: `{\unsure{V}}_{...}^{...}`. Preserve both index arguments and their uncertainties. |
| `pages/150_scan081.tex`, lines 20–23 | A `tikzcd` inside `\diagram`/`\margin` uses ordinary `&` matrix separators. These have already been tokenized as alignment characters when the surrounding macro takes its argument, before TikZ can make them active matrix separators. | Add `ampersand replacement=\&` and replace only this matrix's separators with `\&`. |
| `pages/150_scan083.tex`, lines 40–43 | The same pre-tokenized ordinary-ampersand construction. | The same explicit ampersand replacement. |
| `pages/150_scan098.tex`, lines 4–11 | The same pre-tokenized ordinary-ampersand construction. | The same explicit ampersand replacement. |

The 151003 count is **one directly nested diagram and four directly nested displays**.

## New 151_scan005 B07 construction

Lines 62–70 are balanced and have the intended structural form:

```tex
\margin{
  \diagram{\deleted{\mbox{\begin{tikzpicture}...\end{tikzpicture}}}}
  \diagram{\begin{tikzpicture}...\end{tikzpicture}}
}
```

`\diagram` is outside `\deleted`; the canceled TikZ drawing is contained in an `\mbox`. The live second drawing remains outside the deletion. There is no direct paragraph/display nesting inside ulem here. No edit is indicated by the static inspection. Its inspected SHA-256 is `91aed3c693dcb0abaac0097a17b5d0241c09a3ebe8a7e3e8d0355a751650f4f9`.

## Other results and limits

- The control-sequence-aware scan found no unbalanced braces, mismatched `\begin`/`\end` environments, mismatched explicit `\[...\]` or `\(...\)` delimiters, or odd counts of unescaped dollar delimiters across the 25 pages. Manual review distinguished row breaks such as `\\[-.4ex]` from display delimiters and `\\rent` from a spurious `\rent` command.
- No fused control word remains in the inspected command inventory. In particular, current 094 has `\quad i`, and current 099 has separated `\qquad V` and `\cap V`.
- All six `\illegible` occurrences are in text contexts: 095 and 097 canceled prose, and the autograph/clipped-line entries of typed 151004 and 151006. None is in a formula or diagram.
- The page-level macros are defined by the supplied preamble or belong to the declared LaTeX/AMS/ulem/TikZ packages. No definite missing source-level macro or additional TikZ-library requirement was identified. The node-coordinate shifts used by the annotation brackets do not, by themselves, require the `calc` library. The local `kpsewhich` lookup resolves neither `article.cls` nor the declared packages, so this inspection does not certify a runnable TeX installation; no package installation or compilation was attempted.
- Root owns the ongoing 151007 audit. The inspected 151007 snapshot has SHA-256 `f763e115f0c40976ad0a2a1ff8afc0d5a736bca2d7371f1d2d0d9a0e1897f60f`. Its three canceled drawings already use `\diagram{\deleted{\mbox{...}}}`, rather than the defective direct-nesting form. This report does not freeze or approve subsequent source changes.
- Static checks do not establish typography, margin fit, line wrapping, arrow geometry or visual fidelity. No source reading or uncertainty was normalized.

## Inspected snapshot hashes

```text
150_scan079.tex  e860526becf2f1155d61e28f3d6b2022495787871fe66b7f747b1e19dfb8f833
150_scan081.tex  ea9e08cc5eb2109682cd0de5573c6bc5c42d83456a4ade36465e081f3cf0cac1
150_scan082.tex  09a781500a76799a2cc248233977a5e845888e987086601624ed188cedb30438
150_scan083.tex  7486cecdc86eb17d2988d1913f22cd5bcc5543da6975a7e5fef848092c3ea726
150_scan084.tex  3423e76629927b414f4a532a8e2d57c7137df893ecbec2b0be8a9099d3904ca0
150_scan085.tex  6d5d04b487fcad2a0cd225f4213a8c45640197a07a07bb28347826fb6f3f8fc5
150_scan086.tex  581f85a97edd76883a848af57c6ef0838e82eb8a16dda36454385b4be7a59dd2
150_scan087.tex  985077722918f12efdcd9262ef55168a8af617cfbd0044d9cdb2aa052cefa1e2
150_scan088.tex  1756cf2c210cc4589209c1223c0162dc5cb388085d66206ddce1bd3d62b46c3c
150_scan089.tex  0685a4a744c999d351e303df05d62cb4f57e1bcd4c10a6112253d5c7be0c9e59
150_scan090.tex  1101ed6641d1566a9f97bb9dbbfc604ef9b33ac7a1981ca92d49109c00560f4b
150_scan091.tex  079e011b8a9e7a2957bc6659fc545aae06e550ee52a6f344964a72908142ca8a
150_scan092.tex  7e0c861317765575819a8c23899f7e83cc037338cd0ea9a87a164f612dfc39aa
150_scan093.tex  c61600517d8d782dfa791ac15def81207b0da817906bed83e64184769592aaed
150_scan094.tex  8f805074c4ce273aecd75f2e7d6abbb3da74fc754301b2e2e07a623e0462a6bd
150_scan095.tex  1ee4ed735b7d858cb6bac0c091fe3e691a77a1d7b14380e72c907feea81a900d
150_scan096.tex  ec92c35f093d3764a806acb574a54adb1ba053bf3d0ffbdec6a73f966ab7629b
150_scan097.tex  46f380f4f67fc2c17513529c5c67da25f8a453d10d96d1016696c93fa4e7c5b9
150_scan098.tex  25a882b28a525c8a0b9eb1b09a90634ef1d833e3c1fd0954fed268831a30808a
150_scan099.tex  e8a61f50f2f3386dc11e63e133fd20282623a1c7b2440b3722e1d77fa44bfcab
151_scan003.tex  9653b23c0eb38d3b0ff52c7d1cc9d0cb04a684f58ec4f66aa5e4aa6107d13825
151_scan004.tex  2534907d18e8b5fe2b68d7b0250ba6a0143171d58baf5f176d299e1ee6de30d1
151_scan005.tex  91aed3c693dcb0abaac0097a17b5d0241c09a3ebe8a7e3e8d0355a751650f4f9
151_scan006.tex  dffd70838565ae1560e08839e15e7a6260c2296f3d21e436e1a9b9c1cd6e4359
151_scan007.tex  f763e115f0c40976ad0a2a1ff8afc0d5a736bca2d7371f1d2d0d9a0e1897f60f
PREAMBLE.tex  aa8f0b2c36d63a886bae7e8fc7b68697fdb378a0d7d391ab09480f11d785a1bf
```

## Authorized repairs and final 151007 follow-up

The authorized repairs are complete in the five affected page/record TeX pairs and their matching current final representations. The repair log covers 22 changed files. Post-repair static balance checks pass on all 25 current pages, and all targeted defective constructions are absent. Original witness fields, first/second data, second-box readings, superseded entries and change counts remain unchanged. No TeX was compiled.

The finalized `pages/151_scan007.tex` was also read after root completed its audit; its SHA-256 is `ae14ccc976bded8ede1f0dc03b4fbb8ca469a96711d7b4eadd7743e7b9429d1a`. The new square-ended annotations, two-tip arrow and integrated frame cluster are structurally balanced. Canceled drawings remain boxed inside `\deleted` with `\diagram` outside; the crowded caption keeps its uncertainty in a text argument, and the 1/q uncertainty is inside the subscript. No definite additional representation fix was identified, and reader C did not edit 151007.
