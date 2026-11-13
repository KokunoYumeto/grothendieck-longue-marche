# Sample check of the first pass MPL_6_038-067+7_001-060 (cote 6, scans 38-67; cote 7, scans 1-60; 85 scans; package 31)

Checked 13 Nov 2026 by Claude Fable 5.2 (effort max). The run is by GPT-6 Astra (ChatGPT Pro mode), 12 Nov 2026.
It is the first package run under the one-stream rule.

## Summary

- **Errors:** 0.99 per 100 words (5 in 506 words, one in 101), against 1.56 for package 9 (MPL_142_001-093), 2.15 for
  package 3, 0.73 for package 2 and 1.90 for package 1. Misread words and symbols: 0.79 per 100 words (4), against
  1.01, 1.70, 0.55 and 0.92. Unmarked errors: 0.59 per 100 words (3), against 1.46, 1.52, 0.27 and 1.25. All four
  pages are handwritten. MPL_5+6_001-037, run in four streams the same evening, has 1.65, 1.42 and 1.42 on its
  handwritten pages.
- **This sample is half the size of the earlier ones** (four pages, not eight; compute bound), read from the
  package's half-page images with enlargements of the doubtful places only. Five errors give a wide interval (roughly
  0.3 to 2.3 per 100 words); small marks are under-counted. The rates are lower estimates.
- **Minutes per page:** one stream, scans in order: 122.0 minutes for 85 pages, 1.44 per page and 1.03 per 100
  words (package 2, the other one-stream run: 1.32 and 1.06; within a stream, package 9: 1.83 and 1.16; package 3:
  1.61 and 1.12). Second reading of every page 21:50-22:18 UTC (28.3 minutes, 0.33 per page), freeze 49.1 minutes
  after the last page; 171.5 minutes in all. The log gives no separate time for the notes: its validation line at the
  freeze already counts 255 notes.
- **Completeness:** every scan transcribed. 85 page files, each with its `\scanpage`; the combined file is their
  concatenation; 1,232 inventory rows, all `yes`, every scan covered, with the new `sheet_kind` column (72 text, 7
  reused typed sheets, 5 covers, 1 cancelled draft); no "[...]", no crop-candidate comment. The later pages are not
  thinner: words per unit of ink are 1.02, 0.98 and 1.00 of the average over the thirds of the run.
- **Research notes:** 255 (227 from the source, 28 own ideas), from the supplied pages only: the log states that no
  context zip was supplied. Four were read against the ink (7:018, two notes; 6:041, two notes): quotations right,
  page described correctly. They state what is open; none carries out a test. One note quotes the misread *esquisse*
  of 7:018.

## Method

The run is one stream (the "done" lines follow the package order), so it was cut into quarters (6:038-6:060,
6:061-7:016, 7:017-7:038, 7:039-7:060) and one page was taken from each, the second or second-to-last page of text:
6 scan 041 (early), 7 scan 015 (late), 7 scan 018 (early; the slowest page of the run, 5.00 minutes), 7 scan 059
(late). Every line was compared with the page halves (7:015 with the whole-page image) in `img/`; doubtful places were
enlarged (`img/c*.jpg`; the sideways margin note of 7:059 was rotated, `c7_059_margin_rot.jpg`). The ink decided.
Scoring and word count as in the check of MPL_16+47+54+44 (the re-implemented word count reads about 5 % low, so
rates read about 5 % high on the earlier scale). The scans were unzipped to `scans_unzipped/` (104 MB). The package
folder holds no context zip.

Kinds: MW misread word; MS misread symbol; OM omission; PL wrong placement; DI deletion or insertion wrongly marked;
OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 6:041 | a), parenthesis | `commutant aux \unsure{homom\textsuperscript{t}} de structure` | `transp.t de structure` (transports): crossed t, descender of p (`c6_041_transport.jpg`) | MW | yes, wrong | medium |
| 6:041 | same parenthesis | `\unsure{?}` after "en X," | a sign like & or g | MS | yes | low |
| 6:041 | c) | `H^i(X_C,\mathbb Z_\ell)` | the exponent is a dot or a short stroke | MS | no | low |
| 7:015 | "en passant aux …" | `C^\bullet_{\mathrm{str}}` | the bullet is not visible on the whole-page image | MS | no | low |
| 7:018 | "Je propose d'…" | `\unsure{imaginer\|essayer}` | `essayer`: the descender stands near the end (`c7_018_propose.jpg`) | MW | yes, alternative right | medium |
| 7:018 | same line | `l'esquisse suivante` | `l'approche suivante`: two descenders, then *che* | MW | no | medium |
| 7:018 | "une ~~immersion~~ …" | `application` | `morphisme`: descender of p, ascender of h (`c7_018_morphisme.jpg`) | MW | no | medium |
| 7:018 | "Alg. de W-M B" | `\underline B` | no underline visible | MS | no | low |
| 7:059 | end of "restriction des scalaires" | — | the circled star that ties "(On le note alors Q^{i-1}[M])" to the footnote at the bottom; the first pass has the star only at the footnote | OM | no | medium |
| 7:059 | l. 3 | `\deleted{tout}` in the line | the struck word stands above the line | PL | no | low |
| 7:059 | l. 3 | `en $M$` | *en* is written over another word | DI | no | low |

Not errors: the sideways margin note of 7:059 (read after rotation: it agrees); the boxed (si i ≥ 1); the struck
block [P⁰[M] = M …] on 7:059; `zariskienne` on 7:018, read rightly here.

## Per page

| Scan | Quarter, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6:041 | 1, early | 1.43 | 100 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1.00 | 0 | 2 |
| 7:015 | 2, late | 0.93 | 78 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| 7:018 | 3, early | 5.00 | 156 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 1.92 | 2 | 1 |
| 7:059 | 4, late | 2.27 | 172 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0.58 | 1 | 2 |
| **All** | | | **506** | **4** | **0** | **1** | **0** | **0** | **0** | **5** | **0.99** | **3** | **6** |

Two of the five errors carry a doubt mark; one of them has the ink as its alternative. The slowest page has the most
errors, as in package 3: the slow pages are the hard ones. Doubt marks in the package: 505 `\unsure` (81 with an
alternative) and 11 `\illegible`, 5.9 per page and 4.27 per 100 words. The doubts register has 603 rows, each with
its own confidence (337 low, 258 medium, 8 high), and the notation table the rule asks for.

## Speed

| Part | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| Transcription, one stream | 85 | 122.0 | 1.44 | 1.03 |
| Second reading | 85 | 28.3 | 0.33 | 0.24 |
| Whole run to the freeze | 85 | 171.1 | 2.01 | 1.45 |

One stream cost 122 minutes on the clock where four streams cost 40 to 46 minutes for as many pages; the work per
page inside a stream is lower here (1.44 minutes against 1.72 and 1.88). The pages are lighter: 139 words per page
against 207 and 221.

## Completeness

- 85 pages, all with `\scanpage`; `\cotefile` for 6 and 7; on the four sampled pages the pencil number at the foot
  is written `\margin{n}`; 18 pages carry `\mspage`.
- Inventory: 1,232 rows, all `yes`, 2 to 30 per scan: 429 text, 106 displays, 30 diagrams, 42 drawings, 120 margin
  notes, 208 insertions, 297 deletions. 30 `\diagram` and 38 `\figure`, all in TikZ.
- On the four pages nothing larger than a reference mark is missing.
- Words against ink (ink measured for this check, `ink_measured.json`; package average 2,662 words per unit):

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First third (6:038-7:001) | 28 | 145.4 | 1.02 |
| Middle third | 28 | 134.8 | 0.98 |
| Last third | 29 | 137.3 | 1.00 |

  r(words, ink) = 0.47 (typed sheets and covers among the notes). The lowest pages are covers and near-empty sheets:
  6:038, 6:040, 6:052, 6:067, 6:047, 6:051.

## Research notes

Read against the ink: 7:018, unproved claim (the limit "ne commute pas à la localisation par p") and conjecture
("Je propose", a larger site with thickenings "pas purement infinitésimaux"); 6:041, items a and b (the isomorphism
"compatible aux filtrations"; "est-il contenu dans un" C(i), and M with M(i)). All four agree with the page; the
note on 6:041 a) rightly lists its parenthesis as a reading uncertainty. The notes have no comparison with La Longue
Marche or with other cotes, since no context was supplied. Their mathematics was not checked here.

## Verdict

1. Complete, with no thinning over the run.
2. One stream gave about 1.0 errors per 100 words on handwriting, against 1.65 on the handwritten pages of the
   four-stream package of the same evening, and three of five errors unmarked against six of seven. The samples are
   too small to prove the difference; the direction agrees with package 2, the earlier one-stream run (0.73).
3. The errors are again plausible words in place of the ink (*esquisse* for *approche*, *application* for
   *morphisme*, *homom.t* for *transp.t*): the second pass has to re-read every line, marked or not.
