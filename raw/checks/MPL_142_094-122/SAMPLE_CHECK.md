# Sample check of the first pass MPL_142_094-122 (cote 142, scans 94–122)

Checked 13 Nov 2026 by Claude Fable 5.2 (effort max). The transcription is by GPT-6 Astra (ChatGPT Pro mode).

## Summary

- **Errors:** 0.65 per 100 words (one in 154) on four pages, against 1.56 for package 9 (MPL_142_001-093), 2.15 for
  package 3, 0.73 for package 2 and 1.90 for package 1. Misread words and symbols: 0.52 per 100 words (package 9:
  1.01; 3: 1.70; 2: 0.55; 1: 0.92). Unmarked errors: 0.26 per 100 words (package 9: 1.46; 3: 1.52; 2: 0.27; 1: 1.25).
  One of the four pages (109) is a typed sheet; on the three handwritten pages alone the rates are 0.86, 0.86 and
  0.22.
- **The sample is half the usual size:** four pages (769 words), one from each stream, because three packages had
  to be checked inside one compute bound. Five errors is a small count: the rate could be twice as high or half as
  high on another sample. Disputed places were enlarged from the package's own page images (1,685 pixels wide), not
  from the archive's PDF, so small marks are harder to see than in the earlier checks.
- **Minutes per page:** four parallel streams (094–100, 101–107, 108–114, 115–122). Within a stream: 2.17 minutes
  per page and 1.29 per 100 words (package 9: 1.83 and 1.16; package 3: 1.61 and 1.12; package 2: 1.32 and 1.06).
  On the clock: 20.0 minutes for the 29 pages, 0.69 per page. Every page was then audited by a second reader
  (14:18–14:36 UTC), the transcription was frozen 42.1 minutes after the start, and the notes took 29.6 minutes:
  71.8 minutes in all.
- **Completeness:** every scan of the package (94–122) is transcribed, none left out as blank. All 29 pages carry
  the pencil number (scan − 1), the inventory has 529 rows, all `yes`, and nothing is summarized or skipped. The
  pages with few words are thin in the ink as well (title sheet 105, drawings 106 and 119, two lines on 122).
- **Research notes:** 92 notes. Seven were read and checked (R05–R08, C19–C21) against the ink, the context files
  and by recomputing; no wrong claim.
- **Verdict:** the best rate since package 2, with the audit pass as the visible difference from package 9. The
  errors found are two misread phrases inside doubt marks, a variable (q for s) and a printed "5" left out.

## Method

Four streams show in `progress.log` (the "done" times of 094–100, 101–107, 108–114 and 115–122 interleave). One page
per stream was taken, by a rule fixed before any page was opened: the second page of streams 1 and 3 (095, 109) and
the second-to-last page of streams 2 and 4 (106, 121). Every line of the first-pass page was compared with the two
page halves from `MPL_142_094-122_scans.zip` (unzipped to `scans_unzipped/`, the sampled pages copied to `img/`);
disputed places were cropped and enlarged from the same images (`img/c*.jpg`). The ink decided. Scans 105, 119 and
122 were viewed for completeness (`img/c_sheet_105_119_122.jpg`).

Scoring rule, as for the earlier packages: the rates count discrepancies of high and medium confidence; low ones are
listed and counted separately. Words: prose words, struck text included, plus one word per formula and one more per
relation sign or comma in it; a drawing counts one word plus one per label. The counting script was rewritten for
this check; on the checked pages of packages 2, 3 and 9 it gives 1,125, 1,075 and 1,122 words where their reports
have 1,091, 1,116 and 1,093. `pages_checked/` holds the four pages with the errors corrected.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 095 | l. 4, after *l'identité sur I',* | `\unsure{on écrit},` | *on a unicité,*: a dotted i in the middle of the word and an accent on its last letter (`c095_unicite_ilya_noyau.jpg`, top band) | MW | yes, wrong | medium |
| 095 | NB margin note | `\unsure{tant qu'on se borne à ne parler que} des actions` | *tant que l'on se bornait* (verb ending not settled) *au point de vue des actions*: *point* with its dotted i and crossed t, then two short words (`c095_NB_margin_rot.jpg`) | MW | yes, wrong | medium |
| 095 | a), second line | `\deleted{\unsure{il considère l'action de}} \inserted{\unsure{il y a} une action $\widetilde\Theta$}` | *il considère* is struck at the end of the line above; *il y a* stands on the line, *une* is written above *l'*, and the stroke runs under *action de* (`c095_unicite_ilya_noyau.jpg`, middle band) | DI | yes | low |
| 095 | *est stable sous Θ̃* | `\unsure{\widetilde\Theta'\|\widetilde\Theta}` | a blotted, probably struck, exponent after Θ̃ (bottom band) | DI | yes | low |
| 106 | first drawing | `2 relations` | the 2 is written over another figure | DI | no | low |
| 109 | address label | — | a printed `5` at the right of the label, between *GROTHENDIECK A.* and *MATHEMATIQUES* | OM | no | high |
| 121 | l. 3, insertion above the line | `et les sommets qui leur sont liés` | a short struck word between *sommets* and *leur* (`c121_insertion_Rqs_sigma.jpg`, top band) | OM | no | low |
| 121 | (21), first line | `R_r^{01}\longrightarrow` | `R_r^{0,1}`, with the comma (third band) | MS | no | low |
| 121 | (21), first line | `a_{\tau_0r}^\infty` without a mark, beside `R_{\unsure{\sigma_0(r)\|\tau_0(r)}}` | the same letter in both places; the two readings of one line do not agree | MS | no | low |
| 121 | *Bouchage de trous*, third line | `R_{\unsure{q\|qs}}` | `R_s`: a struck letter, then s (second band). Scan 122 goes on *un tel R_s* | MS | yes, alternative nearer | medium |
| 121 | same line | `(q\in S=S_0\amalg S_1\amalg S_\infty)` | `(s ∈ S = …)`: the letter of the subscript, no descender (second band) | MS | no | medium |
| 121 | last line | `flèches` | a blot or struck letter before the f | DI | no | low |

Not errors: the show-through of the typed verso on 106; the hyphen of *électro-/niques* at a line end on 109; the
struck number before *trois* on 121.

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 095 | 1, early | 2.02 | 227 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0.88 | 0 | 2 |
| 106 | 2, late | 2.27 | 59 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| 109 | 3, early | 0.83 | 306 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0.33 | 1 | 0 |
| 121 | 4, late | 2.27 | 177 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 1.13 | 1 | 4 |
| **All** | | | **769** | **2** | **2** | **1** | **0** | **0** | **0** | **5** | **0.65** | **2** | **7** |

Overall: 0.65 errors per 100 words (one in 154); 0.26 unmarked (one in 385); misread words and symbols, 0.52 (one in
192). Three of the five errors carry a doubt mark. Handwritten pages only (095, 106, 121; 463 words): 4 errors, 0.86
per 100 words, 0.22 unmarked. Early pages (095, 109): 3 errors in 533 words (0.56); late pages (106, 121): 2 in 236
(0.85). Four pages cannot separate position from difficulty.

## Doubt marks

Package: 364 `\unsure` and 5 `\illegible` marks on 29 pages, 12.7 per page and 7.58 per 100 words (package 3: 6.9
and 4.82; package 2: 6.1 and 4.95). 122 of the 364 carry an alternative.

The four pages carry 31 marks, 18 with an alternative.

| | Marks | Share of decided marks |
|---|---|---|
| First reading right | 9 | 75 % |
| First reading wrong, an alternative right or nearer | 1 | 8 % |
| Single reading wrong | 2 | 17 % |
| Not decidable from the scan | 19 | — |

- Right: *autom.*, *il y a*, ℕ, *deviennent informulables* (095); *1 relation*, Λ′¹₋, Λ′¹₊, A⁰¹₊ (106); *de* (121).
- Of the 19 undecidable marks, 5 are his σ or τ on 121. The package writes `\tau_` 91 times and `\sigma_` 9 times,
  with 8 doubt pairs; on 121 the first reading is σ four times and τ once, for one letter. Scan 120, by the same
  stream, has τ without a mark in the same formulas. The second pass has to settle this letter once, on the ink.
- His double quotation marks are written ``…'' throughout (21 pairs, no « »), as the template asks.

## Completeness

- 29 page files, scans 94–122, and the main file is their concatenation. 28 pages end with the pencil number at the
  foot; 118 carries it before a figure that closes the file. The document's own page numbers (15 on 095, 6 on 121, 7
  on 122) are kept as well.
- The inventory has 529 rows, all `yes`, 3 to 46 per scan: 181 text blocks, 61 displays, 122 deletions, 77
  insertions, 44 margin notes, 17 diagrams, 27 drawings. No "[...]", no summary or omission notes; 14 diagrams in
  tikz-cd and 24 drawings in TikZ, none described in words.
- On the four pages nothing larger than a token is missing: the printed 5 on 109 and, among the low items, a struck
  word on 121.
- Words against ink (ink: the fraction of dark pixels of each scan, measured for this check; index: words per unit
  of ink divided by the package average):

| Part | Pages | Words per page | Ink per page | Index |
|---|---|---|---|---|
| First third (094–102) | 9 | 211.0 | 0.0703 | 1.16 |
| Middle third (103–112) | 10 | 136.3 | 0.0607 | 0.86 |
| Last third (113–122) | 10 | 160.9 | 0.0637 | 0.97 |
| First third of each stream | 8 | 212.4 | 0.0683 | 1.20 |
| Middle of each stream | 13 | 161.9 | 0.0662 | 0.94 |
| Last third of each stream | 8 | 133.4 | 0.0587 | 0.88 |

  Words follow the ink (r = 0.85). The fall within a stream comes from pages that are thin on paper: the six pages
  with the lowest index are 119 (a drawing, *Cas IV*), 105 (a title sheet of five lines), 122 (two lines), 108, 110
  and 106 (drawings and diagrams). 105, 106, 119 and 122 were viewed and are complete; 108, 110 and 113 have 4 to 9
  drawings and diagrams each in the inventory and were not viewed.

## Research notes

92 notes in 29.6 minutes, in four sections that follow the streams, one format. Kinds (from `progress.log`): 6
conjectures, 22 unproved claims, 13 unpursued implications, 28 own ideas, 23 reading questions. Each note gives its
scan and place, the search terms it ran on the context files, and a relation to a context passage by file and scan.

Read and checked: R05, R06, R07, R08 (scan 095), C19, C20, C21 (scans 120–121).

- **They quote the ink correctly.** *l'identité sur I′ ∩ X′_K*, *pour Θ̃ convenable!*, *informulables*, the choice
  of ν with Θ^ν x′ = x′ (095); the struck number replaced by *trois* and 10 = 1+3+3+3 (121). R06 and R07 name the
  doubtful readings (`X|Y`, the prime on Θ̃, the margin phrase) and build nothing on them. None rests on the two
  misread phrases of 095.
- **The mathematics checked holds.** C19: for T triangles with all vertices removed, χ = −T/2 and the rank is
  1 + T/2; the counts V = T, E = 3T/2 (scan 120) and V = T/2, E = T (scan 121) give that rank, and E = 2T gives
  T + 1. The counts agree with the page: (20) with its boxed redundancy gives T/2 objects, (21) with (22) gives T
  arrows. C21: by (18) on scan 120, a_r^∞ ends at R_r^{10} and Λ′¹_r starts there, so the written inverse of Λ′¹_r
  does not compose; the note offers the repaired word as a candidate and leaves the text alone. On the ink the Λ of
  (21) is overwritten.
- **The context relation checked is accurate.** R07 cites `LM_140-2_text.tex`, scan 480, for the open-subgroup
  obstruction of outer actions; that passage has it (*il n'opère pas extérieurement pour autant sur un sous-groupe
  ouvert donné*), followed by the hypothesis of a compatible action.
- **Wrong claims:** none found in the seven.

## Verdict

1. Complete: every scan in full, nothing summarized or skipped; the thin pages are thin in the ink.
2. More accurate than packages 1, 3 and 9 on this sample: 0.65 errors per 100 words, 0.52 for misread words and
   symbols, 0.26 unmarked, close to package 2 (0.73, 0.55, 0.27). The sample is four pages and five errors, so the
   figure is rough. The independent audit of every page is the difference from package 9 that the log shows.
3. For the second pass: σ or τ on 120–121 decided once; the phrases inside long doubt marks re-read (both misread
   phrases of 095 stood in such marks).
