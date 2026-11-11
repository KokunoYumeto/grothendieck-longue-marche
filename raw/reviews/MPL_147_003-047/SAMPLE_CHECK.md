# Sample check of the first pass MPL_147_003-047 (cote 147, scans 3–47)

## Summary

- **Errors:** 0.73 per 100 words (one in 136), against 1.90 for package 1. Misread words and symbols: 0.55 per
  100 words (one in 182), against 0.92. Unmarked errors: 0.27 per 100 words, against 1.25. Three of the eight errors
  are one spelling decision repeated (his "standart" given only as the second reading); without it the rates are 0.46
  and 0.27.
- **Minutes per page:** GPT-6 Astra (ChatGPT Pro mode) worked in one stream, scans in order: 45 pages in 59.2
  minutes, 1.32 minutes per page. Package 1 took 40.5 minutes in four parallel streams: 0.90 minutes per page of
  clock time, 2.55 minutes per page within a stream. These pages are lighter (124 words per page against 199), so
  per 100 words the pace is 1.06 minutes against 1.28 within a stream, 17 % faster. The notes then took 36 minutes;
  the whole run 98 minutes.
- **Research notes:** substantive, accurate and sourced. Of the 75 notes, 35 were read and 26 checked in detail
  against the transcription, the ink and La Longue Marche: no wrong claim. All 13 La Longue Marche locations tested
  are at the stated file and scan, with the quoted words. Their strongest result: his claim on scan 031 that the
  closure of a stratum is proper and smooth over Z, and (37) a closed immersion, fails in general (N049–N050, with a
  checked genus-two example). Three literature points could not be checked offline and should be checked before
  reuse.
- **Recommendation:** package 3 at **90 scans** (cote 147, scans 48–137). Quality held and improved; the shorter time
  per page comes from lighter pages and did not cost accuracy. Add one sentence to the template on the order of
  readings in `\unsure` (see the recommendation below).

## Method

Eight pages were checked against the scans. The run had no parallel streams (`progress.log` lists the scans in
order), so it was split into four quarters of 11–12 pages, the size of package 1's streams, and the second and the
second-to-last page of each quarter were taken: the positions of package 1's sample. Every line of the first-pass
transcription was compared with the page halves from `MPL_147_003-047_scans.zip`; disputed places were cropped and
enlarged from the archive's own page images in `147.pdf` (crops `img/c*.jpg`). The ink decided. Line numbers ("l.")
count manuscript lines from the top of the page, insertions included, and are approximate.

Scoring rule, as for package 1: the error rates count discrepancies of high and medium confidence. Low-confidence
discrepancies are listed in the same table and counted separately. Words are estimated from the checked
transcription: prose words, struck text included, plus one word per formula and one more per relation sign or comma
in it. The count was made by a script that reproduces package 1's counts on its eight checked pages (1,601 words
against 1,608). No struck block on these pages is long enough to leave out of the score; the short struck passages
that could not be read better than the first pass (the hatched sum in (13) on 012, the struck sentence after the
display on 046, single struck words) stay in the count.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 004 | top margin, above "infini" | — | `1`: his page number, at the top centre where 5, 12, 16 and 22 stand on 012, 026, 034 and 046 (`c004_heading.jpg`) | OM | no | medium |
| 004 | l. 2, title of § 1 | `\unsure{standard\|standart}` | `standart`, crossed final t | MW | yes, alternative right | high |
| 004 | l. 3, "Une "courbe …"" | `\unsure{standard\|standart}` | `standart` (`c004_courbe_standart.jpg`) | MW | yes, alternative right | medium |
| 004 | l. 9 | `(``ordinaire'')` | `"(ordinaire")`: one quote mark between *quadratique* and the parenthesis, none before *ordinaire* | OT | no | low |
| 004 | l. 17 | `l'ens. ouvert` | no dot visible after *l'ens* at the line end | OT | no | low |
| 012 | l. 2, insertion | `\unsure{standard\|standart}` | `standart` (`c012_insertion.jpg`) | MW | yes, alternative right | medium |
| 012 | l. 10 | `i.e dim` | `ie dim` | OT | no | low |
| 012 | (12), second line | `1-g(X)` | a small letter, like `g(x)` | MS | no | low |
| 012 | (13), end of the struck block | — | a heavily blacked token after the struck sum | OM | no | low |
| 015 | l. 10, after "Mumford-Deligne" | `-- ou de` | one short stroke, then `de`: a dash or a flat *ou*, not both (`c015_ou_de.jpg`) | OT | no | low |
| 015 | l. 13 | `maquettes` | *ma* written over *gr* (start of *graphes*) | DI | no | low |
| 026 | l. 15, "réunion finie …" | `de` | `de~~s~~`: the final s crossed by a heavy bar (`c026_des_zoom.jpg`) | DI | no | medium |
| 026 | (26), ll. 6–17 | `\mathcal M` throughout | two forms of M: a plain capital in (26) and l. 6, a curly 𝓜 on ll. 8 and 14–17 | MS | no | low |
| 034 | l. 12 | `choisit une \inserted{nouvelle} ``origine''` | a quote mark before *choisit*, none before *origine* | OT | no | low |
| 034 | l. 24, "préciser de façon …" | `symétrique` | `simplifi[ée]`: s, i, a flat m, p, l, f, i; no y, t or q (`c034_symetrique_zoom.jpg`) | MW | no | high |
| 037 | l. 2 | `\Pi_1(G')\unsure{\to\|{-}}\Pi_1(G…)` | a plain dash, no arrowhead at either end (`c037_l2_arrow.jpg`) | MS | yes, alternative right | medium |
| 037 | l. 13 | `fls` | `fl` and two small letters, probably `fles` (`c037_fls.jpg`) | MW | no | low |
| 037 | l. 18, last word | `\unsure{définie\|défini}` | `défini`: the line ends with the i and its dot (`c037_defini.jpg`) | MW | yes, alternative right | medium |
| 046 | l. 17 | `$\in\widetilde B'$` | ∈ written over `de` (`c046_de_B.jpg`) | DI | no | low |

## Per page

| Scan | Quarter, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 004 | 1, early | 0.82 | 164 | 2 | 0 | 1 | 0 | 0 | 0 | 3 | 1.83 | 1 | 2 |
| 012 | 1, late | 1.12 | 107 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.93 | 0 | 3 |
| 015 | 2, early | 0.92 | 176 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 2 |
| 023 | 2, late | 1.15 | 134 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 026 | 3, early | 0.47 | 93 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1.08 | 1 | 1 |
| 034 | 3, late | 4.10 | 164 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.61 | 1 | 1 |
| 037 | 4, early | 0.95 | 107 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 1.87 | 0 | 1 |
| 046 | 4, late | 5.47 | 146 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 1 |
| **All** | | | **1091** | **5** | **1** | **1** | **0** | **1** | **0** | **8** | **0.73** | **3** | **11** |

Quarters of the single stream: 1 = scans 003–013, 2 = 014–024, 3 = 025–035, 4 = 036–047. Minutes on page: the gap
between this page's "done" line in `progress.log` and the previous page's.

Overall: 0.73 errors per 100 words (one in 136); 0.27 unmarked errors per 100 words (one in 364); misread words and
symbols alone, 0.55 per 100 words (one in 182). Five of the eight errors carry a doubt mark, and all five are the same
kind: the right reading is there, but as the alternative, behind a normalized first reading (the dictionary spelling
*standard* for his *standart* three times, an arrow for a plain dash, the agreeing *définie* for his *défini*). The
three unmarked errors are a plausible word in place of the ink (*symétrique* for *simplifi[ée]*), his page number 1,
and a struck final s.

## Early versus late

| Quarter | Early page | Errors / 100 words (unmarked) | Late page | Errors / 100 words (unmarked) |
|---|---|---|---|---|
| 1 (003–013) | 004, 0.82 min | 1.83 (0.61) | 012, 1.12 min | 0.93 (0) |
| 2 (014–024) | 015, 0.92 min | 0 (0) | 023, 1.15 min | 0 (0) |
| 3 (025–035) | 026, 0.47 min | 1.08 (1.08) | 034, 4.10 min | 0.61 (0.61) |
| 4 (036–047) | 037, 0.95 min | 1.87 (0) | 046, 5.47 min | 0 (0) |
| All | 540 words | 1.11 (0.37) | 551 words | 0.36 (0.18) |

The four early pages were each done in under a minute and carry six of the eight errors: 1.11 per 100 words, against
0.36 on the four later pages, which took 1.12–5.47 minutes. This is package 1's pattern (3.06 against 0.87) at about a
third of its level. Accuracy did not decline over the run. Pro worked twice as fast per word in the first half of the
run (scans 003–025: 0.69 minutes per 100 words) as in the second (026–047: 1.47), where the pages carry more
deletions.

Part of the gain over package 1 is the material: cote 147 is a cleaner copy than cote 1 (166 deletions in 45 pages
against 477, and half the doubt marks per word), so the comparison measures the run and the manuscript together.

## Package 1's typical unmarked errors

- **Struck words given as live text:** none on the eight pages (package 1: five). Deletions are marked word by word;
  the one deletion error runs the other way, a struck final s left out (026).
- **E/F and 3/5 confusions:** none. Every equation number ((1)–(3), (11)–(14), (26)), subscript, prime and hat on the
  eight pages agrees with the ink, apart from one low item (`g(x)` on 012).
- **Abbreviations written out:** none. Every abbreviation on the eight pages stays as written (*alg. clos*, *pts*,
  *ens.*, *comp. irréd.*, *bij. can.*, *ssi*, *nb*, *p.ex.*, *géom.*, *fl.*, *i.e.*); one may have lost a letter
  (*fls*, probably *fles*, low).
- **What takes their place:** normalization inside the doubt marks, with the expected form first and the ink second.
  Package-wide this means 25 `\unsure{standard|standart}`, 3 unmarked *standard* (scan 003 twice and scan 018, outside
  the sample, also *standart* in the ink: `c003_standart.jpg`, `c018_standart.jpg`), 14 arrow-or-dash marks
  (`\to|{-}`, `\longrightarrow|{-}`) and 2 `définie|défini`. And once the first error type the template names: a
  plausible word in place of the ink (*symétrique*).

## Doubt marks

Density: 274 `\unsure` and 2 `\illegible` marks in 45 pages, 6.1 per page and 4.9 per 100 words. Package 1 had 940
`\unsure` marks (and 61 `\illegible`): 20.9 per page and 10.5 per 100 words. Of package 2's marks, 78 of 274 (28 %)
repeat four questions: 25 *standard|standart*, 30 struck primes, 14 arrow or dash, 9 "=" or "m̄" for his sign for
*même*.

On the eight pages the first pass carries 45 `\unsure` marks (19 with an alternative) and 2 `\illegible` marks
(2 words).

| | Marks | Share of decided marks |
|---|---|---|
| First reading right | 14 | 74 % |
| First reading wrong, an alternative right | 5 | 26 % |
| Wrong both ways | 0 | 0 % |
| Not decidable from the scan | 28 | — |

- Of the 11 decided marks with an alternative, 6 had the first reading right (`\xleftarrow{\sim}`, *k(s)*, "=",
  γ_α twice, `I_{(\alpha)}`) and 5 the alternative right: the three *standart*, the dash, *défini*. All 8 decided
  single readings were right (*que*, *contenu*, *et*, *MD*, *se donne*, three struck primes).
- Of the 28 undecidable marks, 22 sit in struck text; the others are overwrites (4), a clipped fragment at the page
  edge (1) and one live phrase (*de ce|du*, 046).
- Package 1: 84 % first right, 6 % alternative right, 10 % wrong both ways, and 19 of 29 errors unmarked. Here no mark
  is wrong both ways and 3 of 8 errors are unmarked; wherever the first reading was wrong, the ink form was the
  alternative.

## Completeness

Nothing larger than a token is missing. Every text block, display, margin note, insertion and deletion on the eight
pages is present, in the order of the page, and every insertion is attached where its caret or line points. The
omissions are his page number 1 (004) and a struck final s (026); among the low items, a blacked token at the end of a
struck formula (012) and two overwrites not recorded (*ma* over *gr* on 015, ∈ over *de* on 046). The eight pages
have no diagrams or drawings, so those were not tested here (the package has 10 and 6). The inventory has 686 rows,
all `yes`. The first pass writes `\mathcal M` for both his plain M and his curly 𝓜; the second pass should settle one
convention for the moduli letter.

## Research notes

Read: N001–N008, N012–N016, N031–N033, N042–N043, N048–N054, N058–N060, N064–N067, N073–N075 and Appendix B
(35 notes, spread over the run). Checked in detail: N001–N004, N007, N012–N016, N031–N033, N042–N043, N048–N051, N053,
N054, N058, N064, N067, N073 and N075, against the transcription, against the ink where the page is in the sample (N016
on 012, N031 on 023, N054 on 034), and against `LM_140-*_text.tex` in the context zip.

- **Substantive.** Each note gives scan and place, kind, Grothendieck's words, a short core and a concrete test: an
  example, a calculation or a counterexample. Reading questions stay out of the transcription and say so (N012, N016,
  N043, N058, N067). N007 turns his margin "faux p. ex. sur les nbs duaux d'un corps" into an explicit automorphism of
  the affine line over the dual numbers that does not extend at infinity. N015 writes out the normalization sequence
  behind his "Démonstration Standart (!)". N049–N050 and Appendix B take a pointed genus-two curve with two
  non-separating nodes and trivial automorphism group: the map (37) has two points over it, and the closure of the
  one-node stratum has local equation uv = 0 there, so it is neither a closed immersion nor smooth. His claim on scan
  031 therefore fails in general; he himself wrote "qui paraît a priori curieux !". N048 shows with a chain of three
  elliptic curves that separating clutching is not injective; N054 notes that the stability test on scan 034 leaves out
  the half-edges inside the new graph.
- **Accurate.** Every mathematical claim checked holds. Recomputed: N007 (the inverse map and the pole at infinity),
  N013, N014, N015 (genus formula), N016 (punctured elliptic curve), N031, N032 (the nodal cubic), N033 (theta graph,
  automorphism group S₃ × Z/2), N049–N050 (the six cross-ratios, the three Klein-four maps and their values 3/7, 9/2,
  2/3 at the marking, the local equation), N053, N054, N064. The readings they rest on agree with the ink where
  checked: the unhatted X in (12) on 012, "poids marqué" on 023, card I_{α,β} + card Ã_{α,β} on 034.
- **Sourced.** The 13 La Longue Marche locations tested are at the stated file and scan with the quoted words: 140-1
  scan 32 (in a cancelled block, as N003 says), 140-2 scans 20, 257, 351, 403, 437, 534, 548, 549, 550 and 561, 140-3
  scan 694, 140-4 scans 254–255. The notes say when the context is only an analogy and never cite the earlier notes as
  results.
- **Wrong claims:** none found. To check online before reuse: N048's statement that Knudsen (1983), Corollary 3.9(b),
  "needs a qualification" (the counterexample itself is right); Edidin and Fulghesu (2012), cited for the normalization
  of the 1-stratum and for coarse local rings; and the preprint of Lochak, Nakamura and Schneps (2026,
  arXiv:2602.12462) in N075. One omission: N031 does not cite his own gloss on scan 014, where the "pts marqués" of a
  component include the branches of the double points; that gloss supports reading the quoted "poids marqué" on 023
  as the total weight, which is the reading N031 proposes.

## Recommendation for package 3

**90 scans: cote 147, scans 48–137.** The cote has 190 scans; the remaining 53 (138–190) make package 4.

- Quality held: 0.73 errors per 100 words against 1.90, misread words and symbols 0.55 against 0.92, unmarked errors
  0.27 against 1.25.
- Minutes per page did not hold literally: 1.32 within the stream against 2.55. Per word the drop is 17 % (1.06
  against 1.28 minutes per 100 words), the pages are 38 % lighter, and accuracy rose on fast and slow pages alike. The
  time saved did not cost accuracy.
- One sentence for the template, from this package's only systematic error: "In `\unsure{reading|alternative}` the
  first reading is what the ink shows: his spelling (he writes *standart*), his agreement (*défini*), a dash where he
  draws no arrowhead; a corrected form may only come second."
- Run length: at this package's pace, 90 scans take about two hours of transcription in one stream, and notes of this
  depth about seventy minutes more, about three hours in all against 98 minutes for this run. If the run stops before
  the zip is offered, the per-page files on disk are what survives.

## Verdict

1. Good enough as a first pass for a second pass to correct, and better than package 1: nothing larger than a token is
   missing, 0.73 errors per 100 words, 0.55 for misread words and symbols.
2. The marked errors are one habit (the expected form first, the ink second), which the second pass can fix by search
   and the template can prevent; but the worst error, *symétrique* for *simplifi[ée]*, carried no mark, so the second
   pass still re-reads every line against the scan.
3. Errors still sit on the pages done fastest, at a third of package 1's level; the shorter minutes per page reflect
   lighter pages. Package 3 can take 90 scans.
