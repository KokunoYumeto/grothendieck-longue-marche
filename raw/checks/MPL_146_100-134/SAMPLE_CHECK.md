# Sample check of the first pass MPL_146_100-134 (cote 146, scans 100–134)

Checked 13 Nov 2026 by Claude Fable 5.2 (effort max). The transcription is by GPT-6 Astra (ChatGPT Pro mode).

## Summary

- **Errors:** 0.86 per 100 words (one in 117) on four pages, against 1.56 for package 9 (MPL_142_001-093), 2.15 for
  package 3, 0.73 for package 2 and 1.90 for package 1. Misread words and symbols: 0.86 (all five errors are of
  that kind; package 9: 1.01; 3: 1.70; 2: 0.55; 1: 0.92). Unmarked errors: 0.51 per 100 words (package 9: 1.46; 3:
  1.52; 2: 0.27; 1: 1.25). Two of the five errors are one sign: his hooked arrow of an inclusion, drawn as a plain
  arrow on 133. Without it the rates are 0.51, 0.51 and 0.17.
- **The sample is half the usual size:** four pages (583 words), one from each reader, because three packages had to
  be checked inside one compute bound. Five errors is a small count; the rate is rough. Disputed places were
  enlarged from the package's own page images (1,685 pixels wide), not from the archive's PDF.
- **Minutes per page:** four readers in parallel (root 100–107, reader_a 108–116, reader_b 117–125, reader_c
  126–134). Within a stream: 2.40 minutes per page and 1.59 per 100 words (package 9: 1.83 and 1.16; package 3: 1.61
  and 1.12; package 2: 1.32 and 1.06). On the clock: 22.2 minutes for the 33 pages, 0.67 per page. Every page was
  audited by a second reader (22:15–22:32 UTC), the transcription was frozen 36.8 minutes after the start, and the
  notes took 27.6 minutes: 65.5 minutes in all.
- **Completeness:** all 33 supplied scans are transcribed in full; each page carries the pencil number (scan − 1);
  the inventory has 752 rows, all `yes`. Later scans are not thinner (index 0.93, 1.03, 1.03 over the thirds of the
  run). Scans 102 and 105 are not in the package's scans zip and could not be looked at.
- **Research notes:** 96 notes. Four were read and checked (A115-2, B05, C20, C23); no wrong claim.
- **Verdict:** complete, and close to package 2 in accuracy on this sample. The unmarked errors sit on one page
  (133): a word (*on normalise* for *… sa normalisée*) and the two hooked arrows.

## Method

`progress.log` names the transcriber of every page. One page per reader was taken, by a rule fixed before any page
was opened: the second page of text of root and of reader_b (103, 118; scan 101 is a title sheet), the second-to-last
page of reader_a and of reader_c (115, 133). Every line of the first-pass page was compared with the two page halves
from `MPL_146_100-134_scans.zip` (unzipped to `scans_unzipped/`, the sampled pages copied to `img/`); disputed places
were cropped and enlarged from the same images (`img/c*.jpg`). The ink decided. Scans 101, 126 and 127 were viewed
for completeness (`img/c_sheet_101_126_127.jpg`).

Scoring and word count as in `MPL_142_094-122_check/SAMPLE_CHECK.md`: errors of high and medium confidence count;
low ones are listed and counted separately. `pages_checked/` holds the four pages with the errors corrected.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 103 | l. 1, after *P_{G,C},* | `\deleted{\unsure{prennent\|sont}} des fibrés` | a live word, its first letter written over, most likely *proviennent*; the sentence has no other verb, and the next one begins *Ils sont* (`c103_top_cat.jpg`, top band) | MW | yes, wrong both ways, and given as deleted | medium |
| 103 | l. 2 | `\deleted{Ils} est déduisible` | the second word is also written over (*sont* to *est*?), and *déduisibles* seems to keep its s (middle band) | DI | no | low |
| 103 | l. 5 | `\unsure{\widehat{SP}_{G^b}\|SP^{\wedge}_{G^b}}` | the hat stands after P | MS | yes, alternative right | low |
| 115 | first case of ε_a | `\widehat{\vec A}_s-\{a\}` | the sign may be ∖, as in the second case | MS | no | low |
| 118 | after *ℙ¹∖{0,1,∞},* | `\unsure{ordination\|ordonnation}` | *numéro-/tation*: the third line begins *tation des éléments de I* (`c118_isomorphisme_Pi.jpg`, top band) | MW | yes, wrong both ways | medium |
| 118 | same phrase | `\margin{isomorphisme qui dépend …}` | running text inside the parenthesis that opens at *(≃ ℙ¹…* | PL | no | low |
| 118 | *la partition P_i* | `\uline{$P_i$}` | under P_i stands a short struck word, not an underline (bottom band) | DI | no | low |
| 133 | l. 2, after the insertion | `on normalise` | *… sa normalisée*: the word ends in *-lisée*; the short word before it is not settled (`c133_normalisee_arrows_construit.jpg`, top band) | MW | no | medium |
| 133 | first diagram | `\arrow[l]` from Â_k to X̃ | an arrow with a hook at its tail, ↩ (second band) | MS | no | medium |
| 133 | second diagram | `\arrow[rr]` from X̃′ to Â′_k | a line with a hook at the right end and no head: the same inclusion Â′_k ↪ X̃′, as *défini via* then spells out; the first pass has it point the other way (third band) | MS | no | medium |
| 133 | *et qui sur les …* | deleted *normalisées*, deleted *donne des isom.*, inserted *des normalisées donne un iso* | the layers of this correction could not be told apart at this enlargement | DI | partly | low |

Not errors: *construit* on 133 (enlarged, bottom band); `\unsure{ext.|cat.}` on 103, where the ink allows both and
the sense needs *ext.*.

## Per page

| Scan | Reader, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 103 | root, early | 2.68 | 162 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.62 | 0 | 2 |
| 115 | reader_a, late | 3.57 | 110 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| 118 | reader_b, early | 1.80 | 205 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.49 | 0 | 2 |
| 133 | reader_c, late | 4.12 | 106 | 1 | 2 | 0 | 0 | 0 | 0 | 3 | 2.83 | 3 | 1 |
| **All** | | | **583** | **3** | **2** | **0** | **0** | **0** | **0** | **5** | **0.86** | **3** | **6** |

Overall: 0.86 errors per 100 words (one in 117); 0.51 unmarked (one in 194); misread words and symbols, 0.86. Two of
the five errors carry a doubt mark, and in both neither reading offered is right. Early pages (103, 118): 2 errors in
367 words (0.54), both marked; late pages (115, 133): 3 in 216 (1.39), none marked. Four pages cannot separate
position from the reader or from difficulty: all three unmarked errors are reader_c's, on the slowest of the four
pages.

## Doubt marks

Package: 383 `\unsure` and 3 `\illegible` marks on 33 pages, 11.7 per page and 7.74 per 100 words (package 3: 6.9
and 4.82). 180 of the 383 carry an alternative.

The four pages carry 48 marks. The ink decides 11: eight first readings right (*i.e.*, *à un*, *somt* on 103; σ and
the cut-off bracket on 115; *d)* and the two struck tildes on 133), one alternative right (the hat of SP on 103), two
wrong both ways (*prennent|sont*, *ordination|ordonnation*). Of the 37 not decidable, seven are his Gothic S on 118,
each written `\unsure{\mathfrak{S}_4|\mathfrak{G}_4}`: a recurring letter that the notation table should settle once.

## Completeness

- 33 page files (scans 100–134 without 102 and 105) and the main file is their exact concatenation (78,217
  characters). Every page has one `\mspage` with the pencil number; 30 pages end with it, and 110, 128 and 131 end
  with a margin note or an insertion written below it.
- The inventory has 752 rows, all `yes`, 3 to 73 per scan: 272 text blocks, 94 displays, 164 deletions, 82
  insertions, 40 margin notes, 36 diagrams, 64 drawings. No "[...]", no summary or omission notes; 36 diagrams in
  tikz-cd, 14 TikZ pictures.
- On the four pages nothing is missing: no token, block, display, margin note or insertion.
- Words against ink (ink: the fraction of dark pixels of each scan, measured for this check; index: words per unit
  of ink divided by the package average):

| Part | Pages | Words per page | Ink per page | Index |
|---|---|---|---|---|
| First third (100–112) | 11 | 140.5 | 0.0630 | 0.93 |
| Middle third (113–123) | 11 | 151.2 | 0.0611 | 1.03 |
| Last third (124–134) | 11 | 161.9 | 0.0655 | 1.03 |
| First third of each stream | 11 | 127.3 | 0.0603 | 0.88 |
| Middle of each stream | 11 | 166.1 | 0.0666 | 1.04 |
| Last third of each stream | 11 | 160.3 | 0.0627 | 1.07 |

  Later pages are not thinner (r = 0.80 between words and ink). The first third of each stream is low because two
  streams open on a title sheet: 101 (*Hom de générisation SP_G → SP_{G♮}*, "21 p") and 126 (*Graphes MD*, "6 p").
  127 is a page of graph drawings in rows, reproduced in TikZ. All three were viewed.
- Scans 102 and 105 are absent from the scans zip. Package 9's check found that three scans left out there as blank
  carried pencil numbers and short notes; these two should be looked at in `146.pdf`.

## Research notes

96 notes in 27.6 minutes, each located by scan and TeX line, with a kind and a relation to a context file by scan.

Read and checked: A115-2, B05, C20, C23.

- **B05** (118): the action of 𝔖₄ on the three partitions of type 2,2 has kernel the four-group
  {1, (12)(34), (13)(24), (14)(23)}, so the effective group is 𝔖₃. Correct.
- **A115-2** (115): the subgroupoid induced on Sε_G is equivalent to Π₁(P_G), because it is full and P_G, a torsor
  under a torus, is connected. Correct, and it quotes the page as the ink has it.
- **C20** (133): *net* is the older word for unramified (EGA IV, § 17); a branch of a node gives
  k[[x,y]]/(xy) → k[[x]], a surjection, hence unramified and not flat. Correct. The EGA and Stacks (Tag 02G3)
  citations were not opened.
- **C23** (133): asks whether X here is the proper marked curve, against the convention X = X̂∖I of cote 147. A fair
  reading question; the context passage (scan 91) was not opened, though `X̂∖I` does occur in that file.
- None of the four rests on an error found here. C22 and C23 discuss the lines of 133 that carry the misread
  *on normalise* and the two arrows; their arguments use *sur un corps k* and the finite map, not those readings.
- **Wrong claims:** none found in the four.

## Verdict

1. Complete for the 33 supplied scans; 102 and 105 to be looked at in the PDF.
2. Accuracy on this sample: 0.86 errors per 100 words and 0.51 unmarked, between package 2 (0.73 and 0.27) and
   package 9 (1.56 and 1.46); 0.51 and 0.17 without the hooked arrow. Four pages and five errors make this rough.
3. For the second pass: his hooked arrows (inclusions) across reader_c's pages 126–134; the Gothic S settled once;
   words inside doubt marks that offer two readings re-read, since both such errors had neither reading right.
