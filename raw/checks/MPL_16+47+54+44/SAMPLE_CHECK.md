# Sample check of the first pass MPL_16+47+54+44 (cotes 16, 47, 54, 44; 82 scans; package 11)

Checked 13 Nov 2026 by Claude Fable 5.2 (effort max). The run is by GPT-6 Astra (ChatGPT Pro mode), 12 Nov 2026.

## Summary

- **Errors:** 0.36 per 100 words (3 in 823 words, one in 274), against 1.56 for package 9 (MPL_142_001-093), 2.15 for
  package 3, 0.73 for package 2 and 1.90 for package 1. Misread words and symbols: 0.24 per 100 words (2), against
  1.01, 1.70, 0.55 and 0.92. Unmarked errors: 0.12 per 100 words (1), against 1.46, 1.52, 0.27 and 1.25.
  One of the four pages is a typed letter (16 scan 044, 322 words, no error); on the three handwritten pages the
  rates are 0.60, 0.40 and 0.20 (3 errors in 501 words).
- **This sample is half the size of the earlier ones** (four pages, not eight; compute bound), and the pages were read
  from the package's half-page images with enlargements of the doubtful places only, not from the archive PDF. Three
  errors give a wide interval (roughly 0.1 to 1.1 per 100 words), and small marks are under-counted. The rate is a
  lower estimate.
- **Minutes per page:** four parallel streams, and a fifth piece (16 scans 020-023) taken up when the first stream had
  finished. On the clock: 40.5 minutes for 82 pages, 0.49 per page. Within a stream: 1.88 minutes per page and 0.91 per
  100 words (package 9: 1.83 and 1.16; package 3: 1.61 and 1.12; package 2: 1.32 and 1.06). Audit by a second reader
  15:21-15:54 UTC, freeze 32.3 minutes after the last page, notes 19.6 minutes: 92.4 minutes in all.
- **Completeness:** every scan transcribed. 82 page files, each with its `\scanpage`; the combined file is their
  concatenation; 1,716 inventory rows, all `yes`, every scan covered; no "[...]", no crop-candidate comment, no summary.
  The later pages are not thinner: words per unit of ink are 0.92, 0.96 and 1.12 of the average over the thirds of the
  run, and 0.92, 0.95 and 1.14 over the thirds of each stream.
- **Research notes:** 428 (347 page notes and 81 literature supplements). Four page notes were read against the ink
  (54:3:2, 54:3:3, 47:10:2, 47:10:3): their quotations and their descriptions of the page are right. They state the gap
  and what a proof needs; none carries out a test. The 81 literature supplements were not checked.

## Method

`progress.log` has no reader tag on the "done" lines; the streams were found from the order of the scans: 54:001-44:009
(17 pages), 16:001-019 (18), 16:046-47:011 (22), 16:025-045 (21), then 16:020-023 (4 pages, begun at 15:12:46 UTC when
the first stream ended). One page per stream was taken, the second or the second-to-last page of text: 16 scan 003
(early), 16 scan 044 (late), 54 scan 003 (early), 47 scan 010 (late). Every line of the first pass was compared with
the two page halves (`img/`); doubtful places were cropped and enlarged from the same images (`img/c*.jpg`). The ink
decided. Scoring as in the earlier checks: high and medium discrepancies count, low ones are listed. Words: prose
words, struck text included, plus one per formula and one per relation sign or comma in it, counted on the first
pass with a re-implementation of the earlier script (it gives 1,066 words on package 3's eight checked pages, where
the earlier script gave 1,116: rates here read about 5 % high on the earlier scale). The scans were unzipped to
`scans_unzipped/` (112 MB). The package folder holds no context zip.

Kinds: MW misread word; MS misread symbol; OM omission; PL wrong placement; DI deletion or insertion wrongly marked;
OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 16:003 | insertion over l. 3 | `du module \unsure{non-gradué}` | `du module ss-jacent` (`c16_003_top.jpg`) | MW | yes, wrong | medium |
| 16:003 | same insertion | `\unsure{(le produit)}` | `(ss graduation)` | MW | yes, wrong | medium |
| 16:003 | l. 2, first word | `Soit` | `Soient` with the ending struck | DI | no | low |
| 16:044 | typed, l. 12 | `independant` | two letters typed over; the first pass never records overtyped letters | OT | no | low |
| 54:003 | "Autre interprétation" | `\deleted{elle} se \deleted{définie}\inserted{classifie} \inserted{une telle extension se} par` | *une telle extension se* stands above the struck *elle se*, before *classifie* (`c54_003_classifie.jpg`) | PL | no | medium |
| 54:003 | universal extension | arrow with a head from `V(t_B^\vee)` to `E` | no head visible | MS | no | low |
| 47:010 | "considérons le exp D" | `le` | *le* looks struck (`c47_010_Gr1.jpg`) | DI | no | low |
| 47:010 | boxed formula | `\psi_D(b)` | the second ψ_D is written over another sign | DI | no | low |

Not errors: `Gr^1(A\times A)` on 47:010 (enlarged: A, not B); the equation labels (1.2), (1.3) on 16:003, written over
and rightly marked; ℓ|χ on 16:044 (ℓ, first reading right).

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16:003 | 16:001-019, early | 1.75 | 205 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0.98 | 0 | 1 |
| 16:044 | 16:025-045, late (typed) | 1.77 | 322 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| 54:003 | 54+44, early | 2.12 | 129 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0.78 | 1 | 1 |
| 47:010 | 16:046-47:011, late | 1.93 | 167 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| **All** | | | **823** | **2** | **0** | **0** | **1** | **0** | **0** | **3** | **0.36** | **1** | **5** |

Early pages: 3 errors in 334 words (0.90); late pages: 0 in 489. Two of the three errors carry a doubt mark with no
right reading in it. Doubt marks in the package: 900 `\unsure` (342 with an alternative) and 7 `\illegible`, 11.0 per
page and 5.30 per 100 words (package 3: 6.9 per page; package 1: 22.2). The doubts register has
624 rows, each with its own confidence (336 low, 231 medium, 57 high), and a notation table.

## Speed

| Stream | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| 54:001-44:009 | 17 | 27.7 | 1.63 | 0.83 |
| 16:001-019 | 18 | 35.7 | 1.98 | 0.94 |
| 16:046-47:011 | 22 | 40.5 | 1.84 | 0.86 |
| 16:025-045 | 21 | 38.5 | 1.84 | 0.91 |
| 16:020-023 (after the first stream) | 4 | 11.4 | 2.85 | 1.24 |
| All, within a stream | 82 | 153.8 | 1.88 | 0.91 |
| All, on the clock | 82 | 40.5 | 0.49 | 0.24 |

The pages are heavier than cote 147's: 207 words per page against 124-145. Ten pages carry no doubt mark and no
deletion (covers, title sheets and clean or typed sheets); seven of them took under 1.5 minutes.

## Completeness

- 82 pages, all with `\scanpage`; 78 with `\mspage` (the other four are title sheets); `\cotefile` for 16, 47, 54, 44.
- Inventory: 1,716 rows, all `yes`, 1 to 64 per scan: 704 text, 237 displays, 40 diagrams, 94 drawings, 61 margin
  notes, 231 insertions, 349 deletions. The transcription has 42 `\diagram` and 92 `\figure`, all in TikZ.
- On the four pages nothing larger than a token is missing; every block, display, margin note, insertion and deletion
  is there.
- Words against ink (ink = share of dark pixels of each whole-page image, measured for this check,
  `ink_measured.json`; index = words per unit of ink over the package average of 3,221):

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First, middle, last third in package order | 27, 27, 28 | 214.9, 220.1, 187.1 | 1.14, 0.98, 0.90 |
| First, middle, last third in run order | 27, 27, 28 | 198.1, 190.3, 232.1 | 0.92, 0.96, 1.12 |
| First, middle, last third of each stream | 26, 30, 26 | 194.8, 191.8, 237.3 | 0.92, 0.95, 1.14 |

  r(words, ink) = 0.40 only, because typed and handwritten sheets are mixed. The lowest pages are the title sheets
  (54:002, 16:031, 16:032, 47:002) and 44:006 (18 words; our return notes confirm it holds one theorem and a margin).

## Research notes

Read against the ink: 54:3:2 (the universal vector extension is used, not proved), 54:3:3 ("Je dis que cette extension
n'est autre que S_B" is asserted), 47:10:2 (the boxed ψ_D(a*b) = ψ_D(a)ψ_D(b); the argument cancels T², which the
display confirms), 47:10:3 (the struck block exchanges a, b and x, y: it sets a = ch x and then writes
x*y = ch a * ch b, as the ink has it). All four are right. One note quotes the misread insertion of 16:003
(*non-gradué*, *le produit*). The mathematics of the notes and the 81 literature items were not checked here.

## Verdict

1. Complete, with no thinning towards the end of the run or of a stream.
2. On this small sample the most accurate package so far: 0.36 errors per 100 words, 0.60 on handwriting. The two
   misreads are a plausible phrase in place of the ink, in a small insertion, both marked.
3. The sample cannot confirm this to the precision of the earlier checks; four more pages of cote 16's handwriting
   (for example 16:022, 16:034, 16:042, 16:050, the pages with the most doubt marks) would settle it.
