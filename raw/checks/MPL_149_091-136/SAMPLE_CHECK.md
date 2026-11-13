# Sample check of the first pass MPL_149_091-136 (cote 149, scans 91–136)

Checked on 13 Nov 2026 by Claude Fable 5.2 (effort max), in one run with packages 4 and 5 (MPL_147_138-190,
MPL_149_001-090). This is package 6 (`packages_done/06_MPL_149_091-136`).

## Summary

- **Errors:** 1.03 per 100 words (6 in 583 words, one in 97). Misread words and symbols: 1.03. Unmarked errors:
  0.00: all six carry a doubt mark, and in five of them the ink is the alternative. Three of the six are one
  decision repeated on scan 092: the letter K under E read first as η. Without it the rates are 0.51, 0.51 and
  0.00. Earlier packages: 2.15, 1.70 and 1.52 for package 3; 1.56, 1.01 and 1.46 for package 9; 0.73, 0.55 and
  0.27 for package 2, the other package run in one stream.
- **The sample is four pages, half of the earlier samples of eight.** With 6 errors the 95 % range of the rate is
  0.38 to 2.2 per 100 words. The writing of cote 149 is faint on the scans, and the check used the package images, not the
  archive's PDF: an unmarked misreading of a faint word is harder to catch here than in the earlier checks, so the
  zero for unmarked errors is the weakest of the three figures.
- **Minutes per page:** GPT-6 Astra (ChatGPT Pro mode) worked in one stream, scans in order: 46 pages in 84.8
  minutes, 1.84 minutes per page and 1.27 per 100 words, against 1.32 and 1.06 for package 2 (one stream) and 1.71
  and 1.10 within a stream for package 5, the first half of this cote. The context was opened 2.3 minutes after the
  last page. The log ends there: it has no audit line, no freeze line and no end time, so the time of the notes and
  of the whole run is not on record.
- **Completeness:** every scan is transcribed in full. All 46 pages start with their scan marker and end with the
  pencil number, the main file is the exact concatenation of the pages, the inventory has 611 rows, all `yes`, and
  nothing is summarized or skipped. The later scans are not thinner: words per unit of writing are 1.05, 0.92 and
  1.02 of the package average over the thirds, and words follow the writing closely (r = 0.93).
- **Research notes:** 157 notes in three numbering schemes. Five were read; their quotations agree with the ink,
  and the three context locations tested are at the stated file and scan.
- **Verdict:** complete; every error found is marked, which is what a first pass is asked for. The K-or-η question
  needs one decision for the whole package: η stands without a mark 9 times on scan 096 and 8 times on scan 100.

## Method

Four pages were checked against the scans, spread over the one stream: 092 (second page), 106, 121 and 135
(second-to-last page). Package 2, the other one-stream package, was checked on eight; this check covers three
packages within one compute bound.

Every line of the first-pass page was compared with the two page halves from `MPL_149_091-136_scans.zip` (`img/`);
disputed places were cropped and enlarged from the same images (`img/c*.jpg`). The archive's own page images lie
outside the folders this check could read. The ink decided.

Scoring rule, kinds and word estimate as in `MPL_147_138-190_check/SAMPLE_CHECK.md` (scripts in that folder's
`tools/`; the word estimate can differ from the earlier checks' by a few per cent). As in packages 1–3, a doubt
mark whose first reading is wrong counts as an error, marked. `pages_checked/` holds the four pages; 092 and 106
have the corrections, with the doubt marks that the ink decides resolved.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 092 | l. 5, "la section …" | `\unsure{\mathcal E_{f_\eta}\|\mathcal E_{f_K}}` | `f_K`: the same letter as in K̄ on l. 13 (`c092_K_zoom.jpg`, `c092_Kbar_compare.jpg`). The two other subscripts of this line have K first | MS | yes, alternative right | medium |
| 092 | l. 9, "entre sections de …" | `\unsure{\mathcal E_{U_\eta}\|\mathcal E_{U_K}}` | `U_K` (`c092_sections_EUK.jpg`) | MS | yes, alternative right | medium |
| 092 | l. 9, "sur …" | `\unsure{\mathcal E_\eta\|\mathcal E_K}` | `K` (`c092_sections_EUK.jpg`) | MS | yes, alternative right | medium |
| 092 | l. 15, "de la clôture … de O_{S,s}" | `\unsure{entière\|intégrale}` | `normale`: low letters, one tall letter before the last, no descender, no dot or accent (`c092_cloture.jpg`) | MW | yes, wrong both ways | medium |
| 092 | last display, label | `(\unsure{20\|29})` | `(29)`: the second digit has a tail (`c092_29.jpg`); (27) and (28) stand on scan 089 | MS | yes, alternative right | medium |
| 106 | last display | `(\unsure{\text{Schémas}\|\text{Sch conn}})` | `(Sch conn)`, the c written over another letter (`c106_sch_conn.jpg`); "Y connexe" is inserted five lines above | MW | yes, alternative right | medium |
| 106 | "(pas néc. … clôture alg." | `\deleted{\unsure{une}}` | *une* is small and dark, perhaps written over, not clearly struck | DI | yes | low |
| 121 | struck phrase under "x∈𝔛, k(x)" | `\deleted{\unsure{l'anneau de}}` | looks like `L'ensemble des`: tall letters in the middle, *des* at the end (`c121_struck_phrase.jpg`) | MW | yes | low |
| 121 | "des modèles (réguliers) propres … L sur K" | `propres de` | the word after *propres* is written over (`c121_propres.jpg`) | DI | no | low |
| 121 | same line | `$K$` | K written over another letter | DI | no | low |
| 135 | last line | `\unsure{directes\|induites}` | the word has the shape of *induits* at the end of the same line; the alternative is probably right | MW | yes | low |
| 135 | "que défini modulo" | `que défini modulo` | *défini* stands above the line | PL | no | low |

Not errors: on 106 *notera* after "Si X est un Y-schéma," carries the long bar of its t, not a strike
(`c106_on_notera.jpg`); the margin of 121 agrees with the ink (`c121_margin_rot.jpg`). Pages 121 and 135 have no
counted discrepancy.

## Per page

| Scan | Position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 092 | early | 1.92 | 139 | 1 | 4 | 0 | 0 | 0 | 0 | 5 | 3.60 | 0 | 0 |
| 106 | first half | 2.52 | 111 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.90 | 0 | 1 |
| 121 | second half | 1.67 | 167 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 3 |
| 135 | late | 0.67 | 166 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| **All** | | | **583** | **2** | **4** | **0** | **0** | **0** | **0** | **6** | **1.03** | **0** | **6** |

Minutes on page: the gap between this page's "done" line in `progress.log` and the previous page's.

Overall: 1.03 errors per 100 words (one in 97), all misread words and symbols, none unmarked. Without the K-or-η
decision on 092: 3 errors, 0.51 per 100 words. First half (092, 106): 6 errors in 250 words; second half (121,
135): none in 333. The page done fastest (135, 0.67 minutes) has no error; accuracy does not fall towards the end
of the run.

Pace, from `progress.log`: start 15:44:07 UTC on 11 Nov 2026; scan 136 done 17:08:58; 46 pages in 84.8 minutes
(1.84 per page, 1.27 per 100 words; 6,690 words, 145.4 per page). By thirds: 091–105 in 31.6 minutes, 106–120 in
26.2, 121–136 in 27.1. "Context opened 17:11:18" is the last line of the log.

## Doubt marks

Density: 405 `\unsure` and 2 `\illegible` in 46 pages, 8.8 per page and 6.08 per 100 words (package 2: 6.1 and
4.95; package 5: 5.8 and 3.74). 173 carry an alternative. The register has 407 rows, each with a confidence of its
own (53 high, 242 medium, 112 low).

The four pages carry 34 `\unsure` marks (16 with an alternative).

| | Marks | Share of decided marks |
|---|---|---|
| First reading right | 11 | 65 % |
| First reading wrong, an alternative right | 5 | 29 % |
| Wrong both ways | 1 | 6 % |
| Not decidable from these images | 17 | — |

- First reading right: `U_K`, `K` and `K̄` on 092, *-- ou*, *sans*, *prolonger* (092); *grpes ext* (106); the *même*
  sign twice (121); (38) and *chacun* (135).
- The register rates `\mathcal E_{U_K}` and `\mathcal E_K` on l. 5 of 092 "high" and the `\eta`-first readings four
  lines below "medium": the same letter, read two ways on one page, with the doubt recorded each time.
- Package 2 had 74 % first right and 26 % alternative right; the shares here are close to it.

## K or η

On 092 the subscript of E is the same letter in six places and is the K of K̄. The first pass has K first in three of
them and η first in three. Elsewhere in the package `\eta` stands outside any doubt mark 38 times: 9 on scan 096,
8 on 100, 8 on 129, 4 on 103, 3 on 102, 2 on 108, and once on 093, 098, 101 and 130. He does write η for a generic
point, so these are not counted as errors; they were not viewed. The second pass should decide the letter once, on 092, 096
and 100 together.

## Completeness

- 46 page files, each beginning with its `\scanpage` marker; the main file is their exact concatenation (61,699
  characters). All 46 pages end with the pencil number (`\margin{N}`, scan − 1); 23 carry his sheet number
  (`\mspage`).
- The inventory has 611 rows, all `yes`, 4 to 28 per scan: 199 text blocks, 139 deletions, 133 insertions, 80 margin
  notes, 51 displays, 9 diagrams. The transcription has no "[...]" and no summary or omission note.
- On the four pages nothing is missing: every block, display, margin note, insertion and deletion is present and
  in the order of the page.
- Words against writing ("writing" as defined in `MPL_147_138-190_check/SAMPLE_CHECK.md`):

| Part | Pages | Words per page | Index |
|---|---|---|---|
| First third (091–105) | 15 | 138.3 | 1.05 |
| Middle third (106–120) | 15 | 122.3 | 0.92 |
| Last third (121–136) | 16 | 173.8 | 1.02 |

  No thinning: the lowest index of any page is 0.79 (scan 118), and r = 0.93 between words and writing.
- **Quotation marks:** ``…'' on 36 lines; « » three times, on scans 130 and 131 (« en général », « minimal »,
  « triviale »). The template allows « » only where the ink has them; these three were not viewed.

## Research notes

157 notes: 47 unproved claims, 39 reading questions, 32 own ideas, 25 conjectures, 14 unpursued implications. They
come in three numbering schemes, one per part of the file (RN091-01… for scans 91–104; 106-R1… for 105–122; 123-O2,
132.1… for 123–136), although the transcription ran in one stream. Each note compares with a context file and scan.

Read: RN092-02, RN092-03, 106-R1, 135.1, and the headers of all notes on the sampled pages.

- **Quotations agree with the ink:** "codim 1" and the extension (29) (RN092-02); "On introduit le normalisé S' de
  S" (RN092-03); "la clôture alg. de k(x) dans Ω" and the doubtful first subscript of (4) (106-R1); "On va donc
  admettre que (37)" and the correction by connected components (135.1).
- **None rests on an error found here.** RN092-03 asks that "the stabilizer's ambient-group subscript on scan 092"
  stay as read; that subscript (`\mathcal E_{\overline K}`) is right. No note read uses *entière|intégrale* or the η
  readings of 092.
- **Context locations:** three tested, all at the stated file and scan: "par Kummer" (`LM_140-2_text.tex`, scan 26;
  RN092-02); "faire un raisonnement local général" (`LM_140-2_text.tex`, scan 75; RN092-03); the two π₂
  qualifications (`ARCH_147_003-137_text.tex`, scan 130; 135.1).
- **Not checked:** the mathematics of the notes, the literature references (for instance the Stacks project, Tags
  0BSD and 0BQ8), and the other 152 notes.

## Comparison

| Package | Scans | Streams | Pages, words checked | Errors per 100 words | Misread words and symbols | Unmarked | Minutes per page within a stream |
|---|---|---|---|---|---|---|---|
| 1, MPL_1_002-050 | 3–50 | 4 | 8, 1,526 | 1.90 | 0.92 | 1.25 | 2.55 |
| 2, MPL_147_003-047 | 3–47 (45) | 1 | 8, 1,091 | 0.73 | 0.55 | 0.27 | 1.32 |
| 3, MPL_147_048-137 | 48–137 (90) | 4 | 8, 1,116 | 2.15 | 1.70 | 1.52 | 1.61 |
| 9, MPL_142_001-093 | 1–93 (90) | 4 | 8, 1,093 | 1.56 | 1.01 | 1.46 | 1.83 |
| 4, MPL_147_138-190 | 138–190 (53) | 4 | 4, 524 | 0.38 | 0.38 | 0.38 | 1.41 |
| 5, MPL_149_001-090 | 1–90 (90) | 4 | 4, 574 | 0.52 | 0.17 | 0.52 | 1.71 |
| **6, MPL_149_091-136** | 91–136 (46) | 1 | 4, 583 | **1.03** | **1.03** | **0.00** | 1.84 |

Packages 4, 5 and 6 were checked on four pages each, from the package images; packages 1–3 and 9 on eight, with
crops from the archive's PDF. The lists of low items are shorter here for that reason and should not be compared.
The two one-stream packages (2 and 6) have the lowest unmarked rates of the seven, 0.27 and 0.00, and the highest
shares of doubts whose alternative is the ink. This package took 1.84 minutes per page, level with package 9 and
below only package 1, and with 8.8 doubt marks per page it marks more than packages 2 to 5 (5.8 to 7.4).

## Verdict

1. Complete: every scan in full, nothing summarized or skipped, no thinning towards the end of the run.
2. Accuracy on the sample: 1.03 errors per 100 words, every one with a doubt mark, five of six with the ink as the
   alternative (95 % range 0.38–2.2, from four pages); 0.51 without the repeated K-or-η decision.
3. For the second pass: decide K or η once for 092, 096 and 100; read *normale*, (29) and *Sch conn*; view the
   three « » pairs on 130–131; decide the six low items. The run's log records no audit, no freeze and no end time;
   the notes file states that the pages were frozen before the context was opened.
