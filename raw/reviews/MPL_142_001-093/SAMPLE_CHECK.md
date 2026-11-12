# Sample check of the first pass MPL_142_001-093 (cote 142, scans 1–93)

## Summary

- **Errors:** 1.56 per 100 words (one in 64), against 2.15 for package 3, 0.73 for package 2 and 1.90 for package 1.
  Misread words and symbols: 1.01 per 100 words (one in 99), against 1.70, 0.55 and 0.92. Unmarked errors: 1.46 per
  100 words (one in 68), against 1.52, 0.27 and 1.25. Two of the 17 errors are one notation decision: stream 2 writes
  his curled G as a plain G_J, without a mark. Without it the rates are 1.37, 0.82 and 1.28; package 3 without its
  repeated decision had 1.25, 0.81 and 0.72, package 2 0.46, 0.27 and 0.27. Nine of the 17 errors stand on one page,
  026, in a sentence he rewrote and in its formulas.
- **Doubt marks:** right where the ink decides them, absent where the errors are. Of the 18 marks the ink decides, 17
  have the right first reading; of the 17 errors, one carries a mark (package 3: 7 of 24).
- **Minutes per page:** GPT-6 Astra (ChatGPT Pro mode) split the 90 scans into four parallel streams of 22–23 scans
  (001–024, 025–047, 048–070, 071–093). Within a stream: 1.83 minutes per page and 1.16 per 100 words, against 1.61
  and 1.12 for package 3, 1.32 and 1.06 for package 2 (one stream) and 2.55 and 1.28 for package 1. On the clock: 54.1
  minutes for the 90 pages, 0.60 minutes per page. A second worker then audited every page (1.40 reader-minutes per
  page), the transcription was frozen 25.1 minutes after the last page, and the notes took 51.3 minutes: 130.8
  minutes in all, against 101.5 for package 3's 90 scans.
- **Completeness:** every supplied scan is transcribed in full. All 89 pages after the printed cover carry the pencil
  number (scan − 1), the inventory has 1,716 rows, all `yes`, and nothing is summarized or skipped. The later scans
  are not thinner: words per unit of ink are 0.99, 0.93 and 1.09 of the package average over the thirds of the run,
  1.03, 0.98 and 0.99 over the thirds of each stream. Scans 23, 43 and 65, left out of the package as blank, are not
  blank: they hold the pencil numbers 22, 42 and 64 and, on 23 and 43, short pencil notes. The return repeats the
  prompt: "omitted … as blank".
- **The rules added after package 3:** the shared notation table, his double quotation marks, a confidence of its own
  for every row of the doubts register, and the ink first in a doubt mark were followed. The reconciliation of
  recurring signs across all pages was not: his curled G stands in three forms (18 marked, 15 plain, 14 script).
  One abbreviation is written out (*correspond.*), one read as a word (*esst.* as *est*).
- **Research notes:** 307 notes in one format; those read compare each point with La Longue Marche or cote 147 by
  file and scan, and none of the six read against the sample rests on an error found here. Their mathematics was not
  checked in this report.
- **Verdict:** complete, and less accurate than package 2, the one package run in a single stream. Package 3's check
  set the condition for going back to 45 scans in one stream: streams that disagree on a recurring sign, or a rate
  above 1.0 per 100 words without repeated decisions. Both hold here.

## Method

This is the ninth package sent (`packages_done/09_MPL_142_001-093`); packages 4–8 have not been checked, so the
comparison is with packages 1–3. Eight pages were checked against the scans. `progress.log` shows four parallel
streams (the "done" times of 001–024, 025–047, 048–070 and 071–093 interleave), so the second and the second-to-last
page of each stream were taken, the positions of the earlier samples: 026 and 046, 049 and 069, 072 and 092. In
stream 1 the second and second-to-last scans (002, 022) are title sheets of two lines, so the second and
second-to-last pages of text were taken: 004 and 021.

An earlier agent (Claude Opus 5.5, effort max) did the reading: it checked the eight first-pass pages against the
package's page images (`img/`), enlarged the disputed places (`img/c*.jpg`) and wrote `pages_checked/` by applying
its corrections to the first-pass files. It stopped before the report and left no list of low-confidence items. For
this report (Claude Opus 5.5, effort max) each first-pass page was compared word by word with its checked page, every
difference was classified, and every correction was checked again against its crop. One correction was reversed:
(2b) on 026, which the earlier check had made (b) (`c026_2b_compare.jpg`). One discrepancy was added: *correspond.*
on 072, which the checked page still wrote out (`c072_correspond_zoom.jpg`). `pages_checked/` now carries both. Pages
outside the sample were looked at where a pattern or completeness needed it: 024, 030 and 034 (the curled G, the end
of 024), 011, 030 and 044 (pencil numbers), and scans 23, 43 and 65 as rendered from `142.pdf`.

Scoring rule, as for packages 1–3: the error rates count discrepancies of high and medium confidence; low ones are
listed in the same table and counted separately. Words are estimated from the checked transcription with package 2's
script: 1,093 words on the eight pages (package 3: 1,116; package 2: 1,091). The low items cannot be compared with
the earlier checks, which listed 11 to 27 small marks per sample; this sample has the one seen while the corrections
were checked. The error rates can.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 004 | after (7), *homéomorphismes de X … Y'* | `de $X$ en $Y'$` | `de X sur Y'`: the shape of his *sur* in *de X sur lui* four lines below, which the first pass reads as *sur* (`c004_X_sur_Y.jpg`, `c004_X_sur_lui.jpg`) | MW | no | medium |
| 021 | l. 4, *(i.e. avec … flèches plus gros)* | `des flèches` | `de flèches`: d and one flat stroke, as in *catégorie de Galois* on the same page; his *des* in *des complexes* ends in an s (`c021_de_fleches.jpg`, `c021_des_complexes.jpg`) | MW | no | medium |
| 026 | *permutés … par G_J* | `$G_J$` | his curled G, which the package's notation table writes `\unsure{\mathcal G_J\|G_J}` (`c026_permutes.jpg`) | MS | no | medium |
| 026 | after *groupoïde).* | `\deleted{Les relations $(2)$ deviennent}` | only *deviennent* is struck; *Les relations (2)* is live (`c026_des_relations.jpg`) | DI | no | high |
| 026 | above *Les relations* | — | an inserted word, *Dans* or *Des* (a D and two short strokes), with a guide line to before *Les* (`c026_des_relations.jpg`) | OM | no | medium |
| 026 | same sentence | `\inserted{La} partie` | *la* on the line after the struck *deviennent*, live text (`c026_relations.jpg`) | DI | no | medium |
| 026 | same sentence | `partie $(2)$ devient` | `partie (a)`: a closed loop, unlike his small 2 in the (2) above *relations* (`c026_partie_a_zoom.jpg`) | MS | no; the register has "(2); partie (3); introduit", medium | medium |
| 026 | same sentence | `la partie $(3)$` | `la partie (b)`: ascender and bowl (`c026_partie_b_zoom.jpg`) | MS | no; register as above | high |
| 026 | same sentence | `, introduit les` | `, on introduit les`: a dot and a short stroke before *introduit* (`c026_partie_b_zoom.jpg`) | OM | no; register as above | medium |
| 026 | same sentence | `\deleted{… deviennent}` | a comma under the struck *deviennent* | OT | no | low |
| 026 | *simpl. transitive sous G_J* | `$G_J$` | the curled G, as above | MS | no | medium |
| 026 | (19), boxed line | `\underbrace{\varepsilon_0\sigma_\infty}_{\rho^{-1}}` | the brace and ρ⁻¹ stand above: `\overbrace{\varepsilon_0\sigma_\infty}^{\rho^{-1}}` (`c026_rho_inv.jpg`) | MS | no | high |
| 049 | before *et des constructions* | `\unsure{notions\|notations}` | `notations`: two crossed t (`c049_notations_zoom.jpg`) | MW | yes, alternative right | medium |
| 072 | l. 1 | `des $f\ldots$ la formule` | `des f on a la formule`: a dot with a short arc, then a dot; no ellipsis (`c072_f_dots_raw.jpg`) | OM | no | medium |
| 072 | l. 1 | `, est identique` | `, esst. identique`: e, two s, t and a period, his abbreviation of *essentiellement*, which the first pass writes `ess\textsuperscript{t.}` on 026 (`c072_esst_raw.jpg`) | MW | no | medium |
| 072 | struck paragraph, insertion | `\inserted{sur qui opère $\Gamma$,}` | `\inserted{\unsure{avec} op. de $\Gamma$,}`: *op.* with its period and *de* are clear, the first word is not (`c072_avec_op_raw.jpg`) | MW | no | medium |
| 072 | struck paragraph, after the insertion | `correspondant à ce $1$-cocycle` | `correspond. à ce 1-cocycle`: an abbreviation written out; the period follows the d (`c072_correspond_zoom.jpg`) | OT | no | medium |
| 092 | after the struck *ce* | `foncteur` | `factorisé`: f, a, c, t, o, r, i with its dot, s, é with its accent (`c092_factorise_raw.jpg`) | MW | no | high |

Not errors: (2b) in *La relation (2b) devient* on 026, where his small 2, the stroke of the (2) above *relations*,
stands before the b (`c026_2b_compare.jpg`), and 024 writes *(2b) s'écrit* for the same relation; the six bold Γ on
069, where (7) defines the plain Γ as a quotient of the bold one; the I after the J in (10) on 046, his change of
letter (note N046.4 takes it up); and the pencil numbers placed at the top of 011, 030, 044, 051, 082 and 090, where
those sheets have them (seen on 011, 030 and 044).

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 004 | 1, early | 1.32 | 148 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.68 | 1 | 0 |
| 021 | 1, late | 0.37 | 62 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1.61 | 1 | 0 |
| 026 | 2, early | 1.78 | 158 | 0 | 5 | 2 | 0 | 2 | 0 | 9 | 5.70 | 9 | 1 |
| 046 | 2, late | 3.18 | 92 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 049 | 3, early | 0.57 | 120 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.83 | 0 | 0 |
| 069 | 3, late | 1.42 | 169 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 072 | 4, early | 1.03 | 153 | 2 | 0 | 1 | 0 | 0 | 1 | 4 | 2.61 | 4 | 0 |
| 092 | 4, late | 1.93 | 191 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.52 | 1 | 0 |
| **All** | | | **1093** | **6** | **5** | **3** | **0** | **2** | **1** | **17** | **1.56** | **16** | **1** |

Streams: 1 = scans 001–024, 2 = 025–047, 3 = 048–070, 4 = 071–093. Minutes on page: the gap between this page's
"done" line in `progress.log` and the previous page's in the same stream.

Overall: 1.56 errors per 100 words (one in 64); 1.46 unmarked errors per 100 words (one in 68); misread words and
symbols alone, 1.01 per 100 words (one in 99). Without the curled-G decision on 026 (its two errors left out, as
package 3 left out its "!" and package 2 *standart*): 15 errors, 1.37 per 100 words; 0.82 for misread words and
symbols; 1.28 unmarked. One of the 17 errors carries a doubt mark, with the ink as its alternative (package 3: 7 of
24; package 2: 5 of 8; package 1: 10 of 29). By stream: stream 1, 2 errors in 210 words (0.95); stream 2, 9 in 250
(3.60), all on 026; stream 3, 1 in 289 (0.35); stream 4, 5 in 344 (1.45). Without page 026: 8 errors in 935 words,
0.86 per 100 words.

Pace by stream, from `progress.log`:

| Stream | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| 1 (001–024) | 23 | 39.4 | 1.71 | 1.19 |
| 2 (025–047) | 22 | 54.1 | 2.46 | 1.55 |
| 3 (048–070) | 22 | 32.1 | 1.46 | 0.92 |
| 4 (071–093) | 23 | 39.2 | 1.71 | 0.99 |
| All, within a stream | 90 | 164.9 | 1.83 | 1.16 |
| All, on the clock | 90 | 54.1 | 0.60 | 0.38 |
| Audit, within a reader | 90 | 126.4 | 1.40 | 0.89 |

A stream's minutes run from the start of the log to its last page, as for package 3; a reader's audit minutes from
its own last page to its last audit line. The package has 14,250 words. Nine checkpoint zips were saved, after 10,
20, 33, 40, 50, 60, 70, 80 and 90 pages (rule 7). Stream 2, which writes the plain G_J, was the slowest (1.55 minutes
per 100 words) and holds 9 of the 17 errors.

## Early versus late

| Stream | Early page | Errors / 100 words (unmarked) | Late page | Errors / 100 words (unmarked) |
|---|---|---|---|---|
| 1 (001–024) | 004, 1.32 min | 0.68 (0.68) | 021, 0.37 min | 1.61 (1.61) |
| 2 (025–047) | 026, 1.78 min | 5.70 (5.70) | 046, 3.18 min | 0 (0) |
| 3 (048–070) | 049, 0.57 min | 0.83 (0) | 069, 1.42 min | 0 (0) |
| 4 (071–093) | 072, 1.03 min | 2.61 (2.61) | 092, 1.93 min | 0.52 (0.52) |
| All | 579 words | 2.59 (2.42) | 514 words | 0.39 (0.39) |

The early pages carry 15 of the 17 errors: 2.59 per 100 words (2.42 unmarked) against 0.39 (0.39) on the late pages.
Without 026 they still carry 6 of 8, 1.43 per 100 words. The early pages are each stream's second page (in stream 1
its second page of text), finished 4.0 to 5.8 minutes after the start of the run, at 0.81 minutes per 100 words
against 1.34 for the late pages. This is the
pattern of package 1 (3.06 against 0.87) and package 2 (1.11 against 0.36), which package 3 did not show, and the
pattern the template warns of: "The pages done fastest are where errors cluster." Eight pages cannot separate position
from difficulty: 026, with nine errors, carries 22 of the 59 doubt marks of the sample and a sentence rewritten with
a deletion and an insertion. Completeness, measured on all 90 pages, shows no change with position (below).

## Package 3's recommendation and this package's typical errors

- **One notation table for all streams** (rule 5): written, 30 rows at the top of the doubts file, and the log records
  reconciliations across pages for the curled G (024, 025, 039, 044, 045, 085) and the U (022, 083). They stopped at
  the pages compared. The table writes the curled G as `\unsure{\mathcal G_J|G_J}`, which stands 18 times (024, 025,
  039, 044, 045, 085–087); stream 2 writes the same letter as a plain `G_J` without a mark, 15 times on 10 pages
  (026–036, 044), and stream 3 as a bare `\mathcal G_J`, 14 times on 7 pages (051–062). On 026, 030 and 034 the ink
  has the curled letter (`c026_permutes.jpg`). Two of the 17 errors are this decision.
- **His exclamation-mark exponent:** not on these pages; the table records the "!" of his Euler characteristic on 005
  and 047 as a subscript, `\chi_!`.
- **His quotation marks:** followed: 76 pairs written ``…'', no « ».
- **The ink first in a doubt mark:** followed. The eight dash-or-arrow marks put the dash first (`-|\longrightarrow`,
  all in stream 1), and the one decided mark with the ink as its alternative (*notions|notations*, 049) is a misreading,
  not a normalized form.
- **Abbreviations:** one written out, *correspond.* as *correspondant* (072, in a struck paragraph), against rule 2;
  package 3's check found the same abbreviation written out. One read as a word, *esst.* as *est* (072), though the
  first pass writes the same abbreviation right on 026 (`ess\textsuperscript{t.}`).
- **A plausible word in place of the ink:** *foncteur* for *factorisé* (092), *sur qui opère* for *[avec] op. de*
  (072), *en* for *sur* (004), *des* for *de* (021); on 026 the parts (a) and (b) of his relations (2) became the
  numbers (2) and (3).
- **Short words left out:** *on* (026), and *on a* (072), given as an ellipsis.
- **Deletions and insertions:** in one sentence on 026, a deletion drawn too wide (*Les relations (2)* struck with
  *deviennent*), an insertion left out and a live word made an insertion. Struck words given as live text: none.
- **E/F and 3/5 confusions:** none. The equation numbers on the eight pages agree with the ink; (13)|(12) on 072 is
  not decidable.

## Doubt marks

Density: 798 `\unsure` and 8 `\illegible` marks in 90 pages, 9.0 per page and 5.66 per 100 words (package 3: 6.9 and
4.82; package 2: 6.1 and 4.95; package 1: 22.2 and 11.19). 304 of the 798 carry an alternative. The most repeated
questions are bar-omega or varpi (26, all in stream 3), the curled or plain G (18), bold or plain Γ (13) and the dash
or arrow (8, all in stream 1). By stream: 150, 227, 231 and 190 marks.

On the eight pages the first pass carries 59 `\unsure` marks (19 with an alternative) and no `\illegible` mark.

| | Marks | Share of decided marks |
|---|---|---|
| First reading right | 17 | 94 % |
| First reading wrong, an alternative right | 1 | 6 % |
| Wrong both ways (or a single reading wrong) | 0 | 0 % |
| Not decidable from the scan | 41 | — |

- Of the 12 decided marks with an alternative, 11 had the first reading right (*isotopes* and *congrus* on 004,
  *gros* on 021, J twice on 049, the bold Γ six times on 069) and one the alternative (*notations*, 049). All six
  decided single readings were right (*transitivement* on 026; struck *le* and *cette* on 049; *sympathique*,
  *développer* and the struck (11) on 072).
- Of the 41 undecidable marks, 21 sit in struck text. The 20 live ones are *où* (004); on 026 the three labels of the
  margin drawing and seven indices in (16) and (19); *desdits* (046); *p|pas* (069); (13)|(12) and the index n−2
  (072); on 092 the three ′|* exponents, C|C̃ and *abrég.*
- Package 1: 84 % first right, 6 % alternative right, 10 % wrong both ways; package 2: 74 %, 26 %, 0 %; package 3:
  76 %, 3 %, 21 %. Where the ink decides them, this package's marks are the most reliable of the four; as a guide to
  its errors they are the weakest: 16 of the 17 errors carry none.
- **The doubts register** has 711 rows, each with a confidence of its own: 22 high, 317 medium, 372 low (package 3's
  register gave 68 % of its rows a default). On this sample the labels do not separate right from wrong: the five
  decided marks labelled low were all right, and the one wrong first reading was labelled medium. Rows and marks are
  not one to one: a row can cover a repeated mark (the six Γ on 069) or record a confident reading (the I in (10) on
  046, high), and some rows hold doubts the text leaves unmarked. On 026 the row "(2); partie (3); introduit —
  numerals and verb ending compressed — medium" names three of the errors found here; the transcription marks none of
  them.

## Completeness

Every supplied scan is transcribed in full, and no page is cut short, summarized or skipped.

- The 90 page files cover the 90 supplied scans, and the main file is their concatenation in order with a blank line
  between pages (187,615 characters). The 91 hashes written at the freeze match the files.
- All 89 pages after the printed cover (001) carry the pencil number, scan − 1, as `\margin{N}`: at the foot on 83
  pages, as the last thing on the page, and at the top on 011, 030, 044, 051, 082 and 090, where those sheets have it.
  55 pages also carry his own page number (`\mspage`).
- The inventory has 1,716 rows, all `yes`, 3 to 38 per scan: 436 text blocks, 300 displays, 41 diagrams, 40 drawings,
  201 margin notes, 247 insertions, 451 deletions. The transcription has no "[...]", no summary or omission notes and
  no crop-candidate comments; its 41 diagrams are in tikz-cd and its 40 drawings are reproduced in TikZ, none
  described in words.
- On the eight pages nothing larger than a word is missing: the omissions are an inserted word and *on* (026) and
  *on a* (072); the one structural fault is the sentence on 026 (a deletion drawn too wide, a live word made an
  insertion). Every other text block, display, diagram, drawing, margin note, insertion and deletion is present and in
  the order of the page.
- Words against ink. "Ink" is the fraction of dark pixels on each scan, measured when the package was built
  (`packages_work/MPL_142_001-093/MANIFEST.json`); index = words per unit of ink divided by the package's 3,399. The
  printed cover is left out.

| Part | Pages | Words per page | Ink per page | Words per unit of ink | Index |
|---|---|---|---|---|---|
| First third (002–031) | 29 | 158.5 | 0.0470 | 3,370 | 0.99 |
| Middle third (032–063) | 31 | 156.2 | 0.0494 | 3,159 | 0.93 |
| Last third (064–093) | 29 | 165.7 | 0.0446 | 3,715 | 1.09 |
| First third of each stream | 28 | 176.6 | 0.0506 | 3,490 | 1.03 |
| Middle of each stream | 33 | 162.3 | 0.0485 | 3,347 | 0.98 |
| Last third of each stream | 28 | 140.8 | 0.0419 | 3,361 | 0.99 |
| Stream 1 (002–024) | 22 | 150.0 | 0.0434 | 3,458 | 1.02 |
| Stream 2 (025–047) | 22 | 158.6 | 0.0507 | 3,130 | 0.92 |
| Stream 3 (048–070) | 22 | 159.4 | 0.0481 | 3,313 | 0.97 |
| Stream 4 (071–093) | 23 | 171.6 | 0.0462 | 3,715 | 1.09 |

  The later scans are not thinner, neither in the run nor within a stream: the last third of each stream has fewer
  words per page, and less ink in the same proportion. Words per page follow the ink (r = 0.88 over the 89 pages).
  The ratio depends on the size of the hand and the share of formulas, so it compares parts of one package (package 3,
  cote 147: 3,789). The pages with the fewest words for their ink are 046 (index 0.69), 024 (0.71), 033 and 062
  (0.74) and 021 (0.74). 046 and 021 are in the sample and complete; 046 is written in a large hand on widely spaced
  lines. 024 is complete to its last line: (10) and the pencil number 23.
- **Scans 23, 43 and 65.** The package builder left them out as blank (`skipped_blank` in the manifest), and the prompt
  said so. The return repeats it: "scans 023, 043 and 065 were omitted from the supplied set as blank" (doubts
  register), "omitted as blank in the supplied image archive" (notes), "90 nonblank pages" (`progress.log`); there is
  no page file or inventory row for them. In `142.pdf` they are not blank. Each carries its pencil number, 22, 42 and
  64, which fills the gaps in the sequence (022 has 21, 024 has 23), and 23 and 43 carry a pencil note at the top,
  "pages 5 à 23 (= 19 pages)" and "22 pages", of the kind the first pass transcribes on 002 ("19 pages") and 022 ("40
  pages"). The run never saw these scans; the gap is the package's, not the run's.

## The second reader's audit

Rule 8, new in this template: a worker that did not transcribe a page audits it against the image before the freeze.
The log names the readers: the stream-1 worker audited 071–093, the stream-2 worker 001–017, the stream-3 worker
018–047 and the stream-4 worker 048–070. 90 audit lines from 11:57:34 to 12:39:39 UTC; 0.87, 1.44, 1.57 and 1.73
minutes per page for the four readers, counted from each reader's own last page; between a reader's consecutive audit
lines a median of 58 seconds, and less than 40 seconds for 28 of the 90 pages.

- On the sample the audit left every error in place. Six of the eight sampled pages were audited 19 to 38 seconds
  after the reader's previous audit line (026: 27 seconds; 072: 23); 004 after 68 seconds, 069 after 194.
- The log does not say what the audits changed, and the return keeps no version from before them, so their effect
  cannot be measured. The log records three reconciliations (the curled G, the U, the arrowheads of a drawing on 050)
  and nothing else about what the audits changed.
- The freeze held: the 91 hashes written at 12:40:21 UTC are unchanged at the end, and the context was opened twelve
  seconds after the freeze.

## Research notes

307 notes in 51.3 minutes (12:40:33–13:31:52 UTC), with a checkpoint at 13:19:12. They come in one numbering (N003.1,
N003.2, …) and, in the notes read, one format: kind, source, a short quotation, one to four sentences, and a
comparison with the context by file and scan, with the checking state of that passage (first pass, or second pass
checked against the scans).
Kinds: 138 unproved claims, 55 reading questions, 52 own ideas, 33 unpursued implications, 29 conjectures. By stream:
59, 63, 48 and 137 notes (package 3: 222 notes in four formats in 29.1 minutes). The context zip held La Longue
Marche this time (1,797,250 bytes); package 3's notes had no comparison with it.

The eight sampled pages have 29 notes. Six were read against the checked pages: N026.1, N026.2, N046.4, N072.1,
N072.3, N092.1. None rests on an error found here. N092.1 treats the sentence on 092 as a claim about the factor
through the associated cover, which fits the ink's *factorisé* better than the transcription's *foncteur*. The
mathematics of the notes and their references were not checked.

## Recommendation for the remaining packages

**Go back to 45 scans in one stream, as package 3's check set out.**

- The condition is met. Package 3's check: "Go back to 45 scans in one stream if its streams again disagree on a
  recurring sign, or if its rate without repeated decisions stays above 1.0 per 100 words." Here the streams write the
  curled G in three forms, and the rate without that decision is 1.37.
- The four checked packages agree. The one run in a single stream, package 2, is the only one under 1.0 per 100 words
  (0.46 without its repeated decision); the three runs in four parallel streams, at 45 and at 90 scans, stand at 1.90,
  1.25 and 1.37. The notation table and the second reader, added to the template for this run, did not close the gap:
  the table was reconciled on six pages, and the audit left every error found here.
- Add to the template: "Transcribe the pages yourself, one after another, in one stream; do not split them among
  parallel workers." Package 2 took 59 minutes for 45 scans in one stream. The packages built in `packages/` and not
  yet sent need that sentence, and their size set to 45 scans, before they go.
- Build every package with every scan of its range. Scans 23, 43 and 65 were judged blank by their ink and hold pencil
  numbers and notes; a page with only a pencil number costs one image.
- Check the next package the same way.
- **Second pass of this package:** add page files for scans 23, 43 and 65 from `142.pdf`; bring the curled G to one
  form at its 47 places, each checked against the ink; re-read every line against the scans, rewritten passages
  first. Only the curled G can be found by search: 16 of the 17 errors carry no mark, and the register holds doubts
  the text does not mark.

## Verdict

1. Complete: every supplied scan in full, with its pencil number; nothing summarized or skipped; no thinning towards
   the end of the run or of a stream (index 0.99, 0.93 and 1.09 over the thirds of the run, 1.03, 0.98 and 0.99 over
   the thirds of each stream). The three scans the package left out as blank hold the pencil numbers 22, 42 and 64
   and two short pencil notes, which the transcription lacks.
2. Accuracy: 1.56 errors per 100 words, between package 3 (2.15) and package 2 (0.73) and near package 1 (1.90); 1.01
   for misread words and symbols, 1.46 unmarked. Without the one repeated decision: 1.37, 0.82 and 1.28, a little
   above package 3 (1.25, 0.81, 0.72) and three times package 2 (0.46, 0.27, 0.27). The errors gather on the four
   early pages, finished 4 to 6 minutes after the start (15 of 17), and on one rewritten page (9 of 17). By package
   3's own criterion the next packages go back to 45 scans in one stream.
3. What a reader of this transcription should know:
   - About one word or symbol in sixty is wrong, and the doubt marks do not show where. When the ink decides a mark,
     its first reading is right 17 times in 18, but only 1 of the 17 errors carries a mark. Read every passage that
     matters against the scan.
   - The errors gather where he rewrote a sentence (a deletion and an insertion in one line), in short words (*sur*,
     *de*, *on*), in abbreviations (*esst.*, *op.*, *correspond.*) and in labels: the parts (a) and (b) of a relation
     became (2) and (3).
   - His curled G, the group G_J, is written three ways: `\unsure{\mathcal G_J|G_J}`, a bare `\mathcal G_J` (051–062)
     and a plain `G_J` (026–044). They are one letter.
   - The doubts register holds doubts the text does not mark (026); read it with the page.
   - "audited" in `progress.log` means that a second worker looked at the page, not that the page is right.
   - Scans 23, 43 and 65 are not in the transcription. They hold the pencil numbers 22, 42 and 64, and on 23 and 43 the
     notes "pages 5 à 23 (= 19 pages)" and "22 pages".
