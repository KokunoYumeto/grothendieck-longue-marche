# Sample check of the first pass MPL_5+6_001-037 (cote 5, scans 1-53; cote 6, scans 1-37; 89 scans; package 30)

Checked 13 Nov 2026 by Claude Fable 5.2 (effort max). The run is by GPT-6 Astra (ChatGPT Pro mode), 12 Nov 2026.

## Summary

- **Errors:** 0.95 per 100 words (8 in 843 words, one in 105), against 1.56 for package 9 (MPL_142_001-093), 2.15 for
  package 3, 0.73 for package 2 and 1.90 for package 1. Misread words and symbols: 0.71 per 100 words (6), against
  1.01, 1.70, 0.55 and 0.92. Unmarked errors: 0.83 per 100 words (7), against 1.46, 1.52, 0.27 and 1.25.
  The typed pages hide the rate on handwriting: on the three handwritten pages (5:003, 5:047, 6:036) there are 7
  errors in 423 words, 1.65 per 100 words (1.42 for misread words and symbols, 1.42 unmarked); on the typed pages
  (5:044 and the top half of 6:016) 1 error in 420 words.
- **This sample is half the size of the earlier ones** (four pages and half of a fifth, not eight; compute bound),
  read from the package's half-page images with enlargements of the doubtful places only. Small marks are
  under-counted; the rates are lower estimates.
- **Minutes per page:** four parallel readers (root, reader_b, reader_c, reader_d; the run received the prompt from
  before the one-stream rule: its inventory has no `sheet_kind` column). On the clock: 46.4 minutes for 89 pages, 0.52
  per page. Within a stream: 1.72 minutes per page and 0.78 per 100 words (package 9: 1.83 and 1.16; package 3: 1.61
  and 1.12; package 2: 1.32 and 1.06). The dense pages of cote 6 (reader_c, reader_d) went at 0.6 minutes per 100
  words. Audit by a second
  reader 19:17-20:06 UTC (100 audit lines for 89 pages), freeze 40.0 minutes after the last page, notes 33.3 minutes:
  119.7 minutes in all.
- **Completeness:** every scan transcribed. 89 page files, each with its `\scanpage`; the combined file is their
  concatenation; 1,599 inventory rows, all `yes`, every scan covered; no "[...]", no crop-candidate comment. The later
  pages are not thinner: words per unit of ink are 0.98, 0.95 and 1.06 of the average over the thirds of the run and
  0.99, 1.00 and 1.01 over the thirds of each stream.
- **The streams still differ in notation:** root and reader_b write the pencil number at the foot as `\mspage{n}`,
  reader_c and reader_d as `\margin{n}`; his underlined O is `\underline{O}` 19 times and `\mathcal{O}` 3 times (on
  5:003, where the ink underlines it).
- **Research notes:** 444. Six were read against the ink (5:003 items 1 and 3, 6:036 items 1 and 3, 5:047 items 1 and
  3): their quotations are right and they describe the page correctly. They state the gap and what a proof needs; none
  carries out a test. One note discusses the misread word of 5:003 (*gerbienne|galoisienne*; the ink has
  *zariskienne*).

## Method

One page per reader, the second or second-to-last page of text: 5 scan 003 (root, early), 5 scan 044 (reader_b,
late; a typed sheet of another text), 5 scan 047 (reader_c, early), 6 scan 036 (reader_d, late). Cote 6 scans 2-32
are dense pages of about 370 words and hold 56 % of the package's words, so the top half of 6 scan 016 (reader_d's
second page, a typescript page done in 1.05 minutes) was added, down to "Ne supposons plus". Only 6:016 of these
dense pages was looked at; whether all of them are typed was not checked. Every line was compared with
the page halves (`img/`); doubtful places were enlarged (`img/c*.jpg`). The ink decided. Scoring and word count as in
the check of MPL_16+47+54+44 (the re-implemented word count reads about 5 % low, so rates read about 5 % high on
the earlier scale). The scans were unzipped to `scans_unzipped/` (139 MB). The package folder holds no context zip.

Kinds: MW misread word; MS misread symbol; OM omission; PL wrong placement; DI deletion or insertion wrongly marked;
OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 5:003 | "isomorphismes de localisation …" | `\uline{\unsure{gerbienne\|galoisienne}}` | `zariskienne`: the z of X_zar, a tall k (`c5_003_localisation.jpg`) | MW | yes, wrong both ways | high |
| 5:003 | exact sequence (**2 errors**) | `\mathcal{O}_{X}`, `\mathcal{O}_{X_0}` | the index is a script X, unlike the X of X_zar beside it (`c5_003_suite.jpg`) | MS | no | medium |
| 5:003 | same sequence | four `\longrightarrow` | the last two connectors are plain dashes | MS | no | medium |
| 5:003 | "module inversible L sur" | `$\underline{L}$` in the line | L is added above the line with a caret | DI | no | medium |
| 5:003 | same sequence | `\mathcal{O}` | the second O is underlined | MS | no | low |
| 5:003 | diagram | — | two faint thin lines across the diagram | OM | no | low |
| 5:044 | typed, l. 26 | `opérant` | `opèrant` (`c5_044_operant.jpg`) | OT | no | high |
| 5:047 | λ(p) | `\sup_n` | `Sup` | OT | no | low |
| 5:047 | display before the box | `\unsure{r\|p}-1` | undecided; p by the next line | MS | yes | low |
| 6:036 | "Question", l. 2 | `voire un entier` | `resp. un entier`: descender and full stop (`c6_036_resp.jpg`) | MW | no | medium |
| 6:036 | A) a) | `\unsure{Si\|si} quand on est ordinaire` | `Si j mod 𝔪 est ordinaire`: the j of "Cas j entier" (`c6_036_si.jpg`) | MW | no | medium |
| 6:036 | insertion "(… k alg. clos)" | one word before k; given as `\margin` | two short words before k; it is an insertion with an arrow to L⁻²⊗A** (`c6_036_ins.jpg`) | OM, PL | partly | low |
| 6:016 | typed, top half | `X\times_R`, `Specf`, `relatif` | typed x; f added by hand; s of *relatifs* typed over | OT | no | low |

## Per page

| Scan | Reader, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5:003 | root, early | 2.28 | 151 | 1 | 3 | 0 | 0 | 1 | 0 | 5 | 3.31 | 4 | 2 |
| 5:044 | reader_b, late (typed) | 0.95 | 238 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0.42 | 1 | 0 |
| 5:047 | reader_c, early | 2.02 | 148 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| 6:036 | reader_d, late | 2.67 | 124 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 1.61 | 2 | 1 |
| 6:016, top half | reader_d, early (typed) | 1.05 (whole page) | 182 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| **All** | | | **843** | **3** | **3** | **0** | **0** | **1** | **1** | **8** | **0.95** | **7** | **8** |

One error in eight carries a doubt mark. With the script X counted once: 7 errors, 0.83 per 100 words. Doubt marks in
the package: 492 `\unsure` (203 with an alternative) and 58 `\illegible`, 5.5 per page and 2.50 per 100 words, the
lowest density so far (package 3: 4.82 per 100 words). The doubts register has 573 rows, each with its own confidence
(215 low, 269 medium, 89 high).

## Speed

| Reader | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| root (5:001-023) | 22 | 31.4 | 1.43 | 1.11 |
| reader_b (5:024-045) | 22 | 35.7 | 1.62 | 1.07 |
| reader_c (5:046-6:014) | 22 | 39.2 | 1.78 | 0.62 |
| reader_d (6:015-037) | 23 | 46.4 | 2.02 | 0.65 |
| All, within a stream | 89 | 152.7 | 1.72 | 0.78 |
| All, on the clock | 89 | 46.4 | 0.52 | 0.24 |

## Completeness

- 89 pages, all with `\scanpage`; 75 with `\mspage`; `\cotefile` for 5 and 6.
- Inventory: 1,599 rows, all `yes`, 2 to 73 per scan: 601 text, 207 displays, 17 diagrams, 46 drawings, 151 margin
  notes, 225 insertions, 352 deletions. 17 `\diagram` and 44 `\figure`, all in TikZ.
- On the sampled pages nothing larger than a token is missing.
- Words against ink (ink measured for this check, `ink_measured.json`; package average 3,199 words per unit):

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First, middle, last third in package order | 29, 30, 30 | 131.3, 204.4, 324.3 | 0.75, 0.92, 1.23 |
| First, middle, last third in run order | 29, 30, 30 | 223.9, 202.6, 236.7 | 0.98, 0.95, 1.06 |
| First, middle, last third of each stream | 28, 33, 28 | 226.6, 220.0, 216.6 | 0.99, 1.00, 1.01 |

  r(words, ink) = 0.76. The lowest pages are near-empty sheets (5:015 with 2 words, 5:049, 5:021, 5:020, 6:033,
  6:003) and the two covers.

## Research notes

Read against the ink: 5:003 item 1 (the margin question "détermination des points de ces topos ?") and item 3 (the
vanishing of the Chern class as "NS" condition; "une connexion intégrable"); 6:036 item 1 ("image non nulle" in Z_p)
and item 3 (T_p(K) against the later T_p(E_K); the >|≠ doubt); 5:047 item 1 ("À quelle condition peut-on trouver
des") and item 3 (e ≤ p−1). All six agree with the page. No sampled note uses *voire* or *quand on*. The mathematics
and the 29 references were not checked here.

## Verdict

1. Complete, with no thinning towards the end of the run or of a stream.
2. On handwriting about as accurate as package 9 (1.65 errors per 100 words against 1.56; four streams in both), and
   seven of the eight errors carry no mark. The typed pages are nearly clean and pull the package rate under 1.
3. The worst errors are plausible words in place of the ink: *gerbienne|galoisienne* for *zariskienne*, *quand on* for
   *j mod 𝔪*, *voire* for *resp.* The second pass has to re-read every handwritten line; the typed pages need a
   lighter pass (accents, overtyped letters, handwritten additions).
