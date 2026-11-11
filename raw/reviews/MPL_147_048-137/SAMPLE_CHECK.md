# Sample check of the first pass MPL_147_048-137 (cote 147, scans 48–137)

## Summary

- **Errors:** 2.15 per 100 words (one in 47), against 0.73 for package 2 and 1.90 for package 1. Misread words and
  symbols: 1.70 per 100 words (one in 59), against 0.55 and 0.92. Unmarked errors: 1.52 per 100 words (one in 66),
  against 0.27 and 1.25. Ten of the 24 errors are one notation decision repeated on scan 117: his exclamation-mark
  exponent (D^!_d, his sign for the rigidified object) written as a prime, with no doubt mark. Without that decision
  the rates are 1.25, 0.81 and 0.72; package 2 without its repeated *standart* had 0.46, 0.27 and 0.27.
- **Minutes per page:** GPT-6 Astra (ChatGPT Pro mode) split the 90 scans into four parallel streams of 22–23 scans
  (048–070, 071–092, 093–115, 116–137). Within a stream: 1.61 minutes per page and 1.12 per 100 words, against 1.32
  and 1.06 for package 2 (one stream) and 2.55 and 1.28 for package 1. On the clock: 45.1 minutes for the 90 pages,
  0.50 minutes per page. Then 27.3 minutes until the transcription was frozen (a "final visual review", per the doubts
  register) and 29.1 minutes of notes: the whole run took 101.5 minutes for 90 scans, against 98 for package 2's 45.
- **Completeness:** every scan is transcribed in full. All 90 pages end with the pencil number at the foot of the page,
  the inventory has 1,548 rows, all `yes`, and nothing is summarized or skipped. The later scans are not thinner:
  words per unit of ink are 3,731 in the first third and 3,938 in the last (package average 3,789), and the package
  has 17 % more words per unit of ink than package 2.
- **Research notes:** 222 notes, written in four sets, one per stream; each body has one to four sentences. Of
  these, 37 were read and 28 checked in detail, with no wrong claim found. None compares with La Longue Marche: the run
  received the first build of the package, whose context zip was empty (22 bytes). The streams that write a prime
  for his "!" carry it into their notes.
- **Verdict:** at 90 scans the package kept its completeness but not its accuracy. The loss does not come from haste:
  minutes per page rose, and the two fastest sampled pages have no error. Its largest part comes from four streams
  that did not share their notation decisions; the rest from misreads and from breaches of two explicit rules
  (abbreviations, punctuation). Keep 90 scans and add one rule to the template: a single notation table for
  all streams, checked across streams before the freeze. Check the next package the same way, and go back to 45 scans
  in one stream if the streams again disagree on a recurring sign, or if the rate without repeated decisions stays
  above 1.0 per 100 words.

## Method

Eight pages were checked against the scans. `progress.log` shows four parallel streams (the "done" times of 048–070,
071–092, 093–115 and 116–137 interleave), so the second and the second-to-last page of each stream were taken: 049
and 069, 072 and 091, 094 and 114, 117 and 136, the positions of the samples of packages 1 and 2. Every line of the
first-pass transcription was compared with the page halves from `MPL_147_048-137_scans.zip` (extracted to `img/`);
disputed places were cropped and enlarged from the archive's own page images in `147.pdf` (crops `img/c*.jpg`;
the sideways margin diagram on 136 was rotated, `c136_margin_rot.jpg`). The ink decided. Pages outside the sample were
looked at where a sampled reading or a pattern needed it: 092, 110, 122, 124 (the exclamation-mark exponent), and 065
and 127 (completeness).

Scoring rule, as for packages 1 and 2: the error rates count discrepancies of high and medium confidence; low ones are
listed in the same table and counted separately. Words are estimated from the checked transcription with package 2's
script: prose words, struck text included, plus one word per formula and one more per relation sign or comma in it:
1,116 words on the eight pages (package 2: 1,091). `pages_checked/` holds the eight pages corrected: errors fixed,
doubt marks that the ink decides resolved, undecidable ones kept.

Kinds: MW misread word; MS misread symbol or formula; OM omission; PL wrong placement of an insertion;
DI deletion or insertion marked wrongly or not marked; OT other.

## Discrepancies

| Scan | Place | First pass | Ink | Kind | Marked? | Confidence |
|---|---|---|---|---|---|---|
| 072 | (88), first relation sign | `\widehat M_{D_1}=\widehat M_{G_1}` | `≃`: a wavy stroke over the bar (`c072_first_sign.jpg`) | MS | no | medium |
| 072 | (88), struck continuation | `\unsure{\mathbb Z/6\mathbb Z\|\mathbb Z/4\mathbb Z}` | `Z/4Z`, which fits j₁ = 1728 = 2⁶3³ (`c072_Z4Z.jpg`) | MS | yes, alternative right | medium |
| 072 | (88), struck continuation | `(correspondant à la courbe` | `(correspond. à la courbe`: an abbreviation written out (`c072_struck_block.jpg`) | OT | no | medium |
| 072 | (88), struck continuation | — | a short struck token after *correspond.* | OM | no | low |
| 072 | struck line after (88) | `\deleted{… \deleted{\unsure{lorsque}} la section …}` | *la section* has a stroke of its own under *lorsque* (`c072_dans_le_dernier.jpg`) | DI | no | low |
| 072 | (89), second line | `M^{\unsure{!\|'}}` | a blacked mark above M, perhaps a struck hat (`c072_89.jpg`) | OM | no | low |
| 091 | l. 1–2 | `« bouchant les trous »` | `"bouchant les trous"`: his double quotes (`c091_quotes.jpg`) | OT | no | medium |
| 091 | struck word before *et en normalisant* | `\deleted{\unsure{et\|en}}` | a tall first stroke (f, l or a bracket): neither reading fits | MW | yes | low |
| 091 | second paragraph | `est donc explicite` | `est donc complète`: c, one accent, no x or p (`c091_explicite.jpg`). The first pass of 092 then makes its agreement follow (*complet … celui*), where the ink of 092 has *complète … celle* (`c092_top.jpg`) | MW | no | high |
| 091 | same sentence, struck | `\deleted{\unsure{le graphe}}` | `la maquette` (`c091_la_maquette_struck.jpg`) | MW | yes, wrong | medium |
| 091 | last line | `Le \deleted{MD}-\unsure{marquage\|marqué}` | `Le ~~MD~~-maquette`: q descender, double t; 092 goes on *complète de X'* (`c091_MD_maquette.jpg`, `c091_last.jpg`) | MW | yes, wrong both ways | high |
| 094 | l. 2, insertion above the line | `\inserted{remplaçant $\unsure{X'\|\widehat X}$ par}` | `\widehat X'`: hat and prime (`c094_remplacant_X.jpg`) | MS | yes, wrong both ways | medium |
| 094 | [défini donc …] | `\unsure{st.ble}` | *stable*, the a reduced to a dot (`c094_stable.jpg`) | MW | yes, wrong | medium |
| 094 | after *ens. de sommets,* | — | a raised mark after the comma (`c094_sommets_mark.jpg`) | OM | no | low |
| 094 | `S'\subset S` | `S'` | S' written over another letter | DI | no | low |
| 114 | l. 1 | `est un mono $\leftarrow$` | an arrow with a hook at one end (`c114_mono.jpg`) | MS | no | low |
| 114 | heading paragraph | `comme une structure` | `comme une une structure`: *une* written twice (`c114_comme_une.jpg`) | OM | no | medium |
| 114 | same sentence | `catégorie \deleted{multiplicité} analytique` | struck *multiplicité* stands on the line below; its place in the phrase is not certain | PL | no | low |
| 114 | *(d'abord 𝓔 dans la cat des espaces analytiques)* | `\margin{…}` after the paragraph | written between the heading lines as an interlinear note (`c114_dabord.jpg`) | PL | no | low |
| 114 | first word of the last paragraph, struck | `\deleted{Et}` | a word of four letters with a dotted i and a crossed t, probably *Soit* (`c114_struck_first.jpg`) | MW | no | medium |
| 114 | (169), composition line | `(D_{**},b)` | b written over another letter (`c114_Db.jpg`) | DI | no | low |
| 117 | b) insertion; left margin; (175) twice; *où … est le revêtement*; the display after it; the definition of D_{d,d',d''}; NB margin (**8 errors**) | `D'_d`, `D'_{d,d'}`, `D'_{d'}` | `D^!_d`, `D^!_{d,d'}`, `D^!_{d'}`: an exclamation mark as exponent, his sign for the rigidified object, as on 110, 122 and 124 (`c117_b.jpg`, `c117_margin.jpg`, `c117_175.jpg`, `c122_Dbang.jpg`) | MS | no | high |
| 117 | first struck d) | `D_{d,d'}\mathbin\times_{D_{d'}}D'_{d'}` | `D^!_{d'}` (`c117_struck_d2.jpg`) | MS | no | medium |
| 117 | second struck d) | `\unsure{D'_{d'}\|D'_{d,d'}}` | `D^!_{d'}` (`c117_struck_d2.jpg`) | MS | yes, wrong both ways | medium |
| 117 | struck word before *diagramme cartésien* | `\deleted{\unsure{rev.}}` | the word seems to begin with D | MW | yes | low |
| 136 | after (224) | `immersion locale de codim` | `immersion loc.le de codim`: an abbreviation written out (`c136_codim.jpg`) | OT | no | medium |
| 136 | same line, struck | `\deleted{$d_0-d'_0$. \unsure{On a}}` | the stroke starts after d₀; d₀ itself is not crossed (`c136_codim_struck.jpg`) | DI | no | low |
| 136 | bracket, second line | `$d'_* = \{\uline{d_1}>\cdots>d_r\}$` | a brace before d'_* as well; the underline stands under *> ⋯ >* (`c136_typique.jpg`) | OT | no | low |
| 136 | (224), top right | `D_{d'_0,\ldots,d'_{r'}}` | no commas: `d'_0 ⋯ d'_{r'}` (`c136_224_right.jpg`) | MS | no | low |
| 136 | NB margin diagram, top middle | `D_{\unsure{\widetilde d_*}}` | `D_{\widetilde{d'}_*}`: the tilde covers d and its prime; 137 writes `D_{\widetilde d'_*}` (`c136_margin_dtilde.jpg`) | MS | yes, wrong | medium |
| 136 | last lines | `le « squelette de dim $p$ »` | `le "squelette de dim p"` (`c136_bottom.jpg`) | OT | no | medium |

Not errors: 069's equation number (82) (consistent with (81) on 066 and (83) on 070); the hats struck on 091; the two
displays numbered (225) on 136, which are both his; and the bottom-left pencil number, which this package writes as
`\margin{N}` where package 2 wrote `\mspage`.

## Per page

| Scan | Stream, position | Minutes on page | Words | MW | MS | OM | PL | DI | OT | Errors | per 100 words | unmarked | low items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 049 | 1, early | 0.62 | 143 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 069 | 1, late | 0.33 | 54 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.00 | 0 | 0 |
| 072 | 2, early | 1.12 | 124 | 0 | 2 | 0 | 0 | 0 | 1 | 3 | 2.42 | 2 | 3 |
| 091 | 2, late | 3.88 | 151 | 3 | 0 | 0 | 0 | 0 | 1 | 4 | 2.65 | 2 | 1 |
| 094 | 3, early | 0.90 | 149 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 1.34 | 0 | 2 |
| 114 | 3, late | 2.38 | 158 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 1.27 | 2 | 4 |
| 117 | 4, early | 1.60 | 193 | 0 | 10 | 0 | 0 | 0 | 0 | 10 | 5.18 | 9 | 1 |
| 136 | 4, late | 4.00 | 144 | 0 | 1 | 0 | 0 | 0 | 2 | 3 | 2.08 | 2 | 3 |
| **All** | | | **1116** | **5** | **14** | **1** | **0** | **0** | **4** | **24** | **2.15** | **17** | **14** |

Streams: 1 = scans 048–070, 2 = 071–092, 3 = 093–115, 4 = 116–137. Minutes on page: the gap between this page's
"done" line in `progress.log` and the previous page's in the same stream.

Overall: 2.15 errors per 100 words (one in 47); 1.52 unmarked errors per 100 words (one in 66); misread words and
symbols alone, 1.70 per 100 words (one in 59). Without the exclamation-mark decision on 117 (its ten errors left out,
as package 2 left out *standart*): 14 errors, 1.25 per 100 words; 0.81 for misread words and symbols; 0.72 unmarked.
Seven of the 24 errors carry a doubt mark; one of them has the ink as its alternative, and the other six offer no
right reading. By stream: stream 1, 0 errors in 197 words; stream 2, 7 in 275 (2.55); stream 3, 4 in 307 (1.30);
stream 4, 13 in 337 (3.86; 0.89 without the decision).

Pace by stream, from `progress.log`:

| Stream | Pages | Minutes | Minutes per page | Minutes per 100 words |
|---|---|---|---|---|
| 1 (048–070) | 23 | 26.9 | 1.17 | 0.79 |
| 2 (071–092) | 22 | 35.9 | 1.63 | 1.18 |
| 3 (093–115) | 23 | 45.1 | 1.96 | 1.34 |
| 4 (116–137) | 22 | 37.1 | 1.69 | 1.19 |
| All, within a stream | 90 | 144.9 | 1.61 | 1.12 |
| All, on the clock | 90 | 45.1 | 0.50 | 0.35 |

## Early versus late

| Stream | Early page | Errors / 100 words (unmarked) | Late page | Errors / 100 words (unmarked) |
|---|---|---|---|---|
| 1 (048–070) | 049, 0.62 min | 0 (0) | 069, 0.33 min | 0 (0) |
| 2 (071–092) | 072, 1.12 min | 2.42 (1.61) | 091, 3.88 min | 2.65 (1.32) |
| 3 (093–115) | 094, 0.90 min | 1.34 (0) | 114, 2.38 min | 1.27 (1.27) |
| 4 (116–137) | 117, 1.60 min | 5.18 (4.66) | 136, 4.00 min | 2.08 (1.39) |
| All | 609 words | 2.46 (1.81) | 507 words | 1.78 (1.18) |

Counted in full, the early pages carry more errors; without the decision on 117 the late pages do: 0.82 errors per
100 words on the early pages (0.33 unmarked) against 1.78 (1.18) on the late ones, 5 errors against 9. Eight pages
cannot separate position in the stream from difficulty: the late pages are also the slow ones, 2.65 minutes on
average against 1.06. Completeness, measured on all 90 pages, shows no change with position (next section).

The pattern of packages 1 and 2, errors on the pages done fastest, is absent. The two fastest pages (069 in 0.33
minutes, 049 in 0.62) have no error; the two slowest (091 in 3.88 minutes, 136 in 4.00) have seven. The pages are
harder than package 2's: 4.9 deletions per page against 3.7, 6.9 doubt marks per page against 6.1, and from scan 093
on dense notation (D_d, D^!_{d,d'}, flags, torsors). Streams 3 and 4, which carry that notation, took 1.34 and 1.19
minutes per 100 words against 0.79 for stream 1.

## Package 2's recommendation and this package's typical errors

- **The ink form first in a doubt mark** (package 2's recommendation, now rule 5 of the template): followed. One mark
  on the eight pages has the ink as its alternative (package 2: five), and package-wide 29 of the 30 dash-or-arrow
  marks put the dash first (`\text{---}|\longrightarrow` 18 times, `-|\longrightarrow` 7, `-|\to` 4).
- **Notation decided stream by stream.** Streams 1 and 2 write his exclamation-mark exponent as `^!` (90 times on 22
  pages: M̂^!, Γ^! and the like). Streams 3 and 4 never write it: from 109 to 128 they have 44 primed D, T and P on 12
  pages, without a doubt mark, and on every one of those pages that was looked at (110, 117, 122, 124) the ink has the
  "!". The prime also collides with his real primes (d', D_{d'}). Other recurring signs split the same way: his double
  quotation marks are « » in streams 2 and 4 (17 pairs) and ``…'' in streams 1 and 3; his Gothic S is doubted in each
  stream with a different alternative (`\mathfrak S|\mathcal S` 12 times in stream 3, `\mathfrak S_d|G_d` 10 times in
  stream 4, `\unsure{\mathfrak S}` alone 6 times in stream 1). The 27-minute review before the freeze did not reconcile
  them.
- **Abbreviations written out:** two on the eight pages (package 2: none), *correspond.* as *correspondant* (072) and
  *loc.le* as *locale* (136), against rule 2 of the template.
- **A plausible word in place of the ink:** *explicite* for *complète* (091), which the first pass of 092 then makes
  the grammar agree with; *le graphe* and *marquage|marqué* for *la maquette* and *maquette* (091); *Et* for a struck
  four-letter word (114). Three of the four sit on one page, 091.
- **Struck words given as live text:** none. **E/F and 3/5 confusions:** none; the equation numbers on the eight pages
  agree with the ink ((82), (88), (89), (169), (175), (176), (224), the two (225)), and (166) on 114 is not decidable.

## Doubt marks

Density: 620 `\unsure` and 3 `\illegible` marks in 90 pages, 6.9 per page and 4.82 per 100 words (package 2: 6.1 and
4.95; package 1: 22.2 and 11.19). 263 of the 620 carry an alternative. The most repeated questions are his Gothic S
(41 marks, split by stream as above), the dash or arrow (30), G' (11) and q|d (10).

On the eight pages the first pass carries 50 `\unsure` marks (19 with an alternative) and no `\illegible` mark.

| | Marks | Share of decided marks |
|---|---|---|
| First reading right | 22 | 76 % |
| First reading wrong, an alternative right | 1 | 3 % |
| Wrong both ways (or a single reading wrong) | 6 | 21 % |
| Not decidable from the scan | 21 | — |

- Of the 13 decided marks with an alternative, 9 had the first reading right (*Rmq* on 049, the two "!" in (89) on
  072, the four 𝔖 on 117, ∼ on 117, d on 136); one had the alternative right (Z/4Z, 072); three were wrong both ways
  (*marquage|marqué* for *maquette* on 091, X'|X̂ for X̂' on 094, D'_{d'}|D'_{d,d'} for D^!_{d'} on 117).
- Of the 16 decided single readings, 13 were right (α, β, "=", *évt.*, *géom.* on 072; *on* on 091; *intersection*,
  𝓔, *analytiques* on 114; d'_0, the struck star, *On a*, *reste* on 136) and 3 wrong (*le graphe* for *la maquette*,
  *st.ble* for *stable*, `\widetilde d_*` for `\widetilde{d'}_*`).
- Of the 21 undecidable marks, 11 sit in struck text. The 10 live ones are δ_i (049), (166), σ|s twice and
  *identique* (114), *on aura*, <|≤, d|d'' and an index d (117), *typique* (136).
- Package 1: 84 % first right, 6 % alternative right, 10 % wrong both ways. Package 2: 74 %, 26 %, 0 %. The ink-first
  rule removed the normalized first readings, but where the first reading is wrong here, the alternative is usually
  wrong too.
- **The doubts register** catalogues all 623 occurrences, but 426 of them (68 %) carry a "conservative default `low`",
  which it states is not an assessment: no stream record could be matched to them when the register was assembled.
  Package 2's register assessed every entry. Positions are given as excerpts of the transcription,
  not as places on the page.

## Completeness

Every scan is transcribed in full, and no page is cut short, summarized or skipped.

- The 90 page files are complete and the main file is their exact concatenation (150,975 characters). Each of the 90
  pages ends with the pencil number at the foot of the page, the last thing on it.
- The inventory has 1,548 rows, all `yes`, 4 to 35 per scan: 443 text blocks, 141 displays, 91 diagrams, 67 drawings,
  172 margin notes, 232 insertions, 402 deletions. The transcription has no "[...]", no summary or omission notes and
  no crop-candidate comments; its 92 diagrams are in tikz-cd and its 41 drawings are reproduced in TikZ, none
  described in words.
- On the eight pages nothing larger than a token is missing: the omissions are a repeated word (*une une*, 114) and,
  among the low items, a struck token (072) and a raised mark (094). Every text block, display, diagram, margin note,
  insertion and deletion is present and in the order of the page.
- Words against ink. "Ink" is the fraction of dark pixels on each scan, measured when the package was built
  (`packages_work/MPL_147_048-137/MANIFEST.json`); index = words per unit of ink divided by the package's 3,789.

| Part | Pages | Words per page | Ink per page | Words per unit of ink | Index |
|---|---|---|---|---|---|
| First third (048–077) | 30 | 146.9 | 0.0394 | 3,731 | 0.98 |
| Middle third (078–107) | 30 | 139.4 | 0.0376 | 3,704 | 0.98 |
| Last third (108–137) | 30 | 144.6 | 0.0367 | 3,938 | 1.04 |
| First third of each stream | 28 | 145.5 | 0.0376 | 3,875 | 1.02 |
| Middle of each stream | 34 | 146.1 | 0.0396 | 3,694 | 0.98 |
| Last third of each stream | 28 | 138.6 | 0.0362 | 3,825 | 1.01 |
| Package 2 (003–047) | 45 | 123.9 | 0.0381 | 3,250 | — |

  The later scans are not thinner, neither in the run nor within a stream, and words per page follow the ink (r = 0.73
  over the 90 pages). The pages with the fewest words for their ink are pages of formulas and diagrams: 065 (index
  0.44) and 127 (0.68) were read against the ink and are complete to the last line ((80) on 065; the boxed (203) and
  "hom de générisation" on 127); 083 (0.75) is the struck diagrams (108)–(111).

## Research notes

222 notes in 29.1 minutes (10:26:58–10:56:04 UTC), of which 8.4 went to establishing that the context zip was
empty; package 2 wrote 75 notes in 36 minutes. They come in four sets with four formats and numbering schemes
(N048-01…, R071-01…, R093.1…, R116-01…), one per stream, and each body is limited to one to four sentences. Kinds:
103 unproved claims, 40 reading questions, 35 unpursued implications, 27 own ideas, 17 conjectures.

Read: N049-01, N049-02, N056-01, N060-01, N064-01, N065-02, N066-02, N069-01, N069-02, R072-01, R072-02, R072-03,
R080-02, R085-01, R088-03, R091-01, R091-02, R092-01, R094.1, R094.2, R099.3, R104.3, R109.3, R110.1, R113.3, R114.1,
R114.2, R116-02, R117-01, R122-02, R124-02, R128-02, R130-02, R136-01, R136-02, R136-03, R137-02 (37 notes, 9 or 10
from each set, with every sampled page covered). Checked in detail: N049-01, N049-02, N056-01, N060-01, N064-01,
N065-02, N066-02, N069-01, N069-02, R072-02, R072-03, R080-02, R085-01, R091-01, R091-02, R092-01, R094.2, R109.3,
R113.3, R114.1, R116-02, R117-01, R122-02, R124-02, R130-02, R136-01, R136-02, R136-03 (28), against the
transcription, against the ink where the page is in the sample or was viewed (049, 069, 072, 091, 094, 114, 117, 124,
136), and by recomputing their mathematics.

- **Substantive, but short.** Several carry a concrete test. N060-01 gives a counterexample to "Γ opère
  trivialement" in (74) on 060: the graph of two genus-one vertices joined by one edge, whose involution exchanges the
  two M̂_{1,1} factors, and it names the restriction that would save the claim. N066-02 identifies the incidence graph
  of the ten boundary divisors of M̂_{0,5} as the Kneser graph KG(5,2), the Petersen graph. N069-02 computes the
  stabilizers (orders 12, 8 and 4) that record the two branches hidden by "un seul diviseur à l'infini". R116-02
  builds a finite category with the Boolean source fibres of axiom c) in which two arrows share source and target.
  R130-02 shows with the punctured tautological bundle on P¹ (C²∖{0}) how the fibre lattice fails to inject when
  π₂ ≠ 0, the caveat in his margin on 130. Of the 37 notes read, 11 carry out a test, a calculation or a
  construction; the others state the gap and say what would settle it. Package 2's check found a concrete test in
  each note.
- **Accurate.** Every mathematical claim checked holds. Recomputed: the dimension equation in N056-01 ((0,4), (1,1),
  (0,5), (1,2)); the coefficients 1/8 and 1/6 of (80) in N065-02, and the constant −7/12; the Petersen count in
  N066-02 (10 vertices, 15 edges, 15 partitions of type (2,2,1)); the stabilizers in N069-02; the automorphism groups
  of orders 2, 4, 6, and 12 and 24 in characteristics 3 and 2 (N064-01, R072-02); the exact sequence in R080-02; the
  action-groupoid construction in R085-01; the countermodel in R116-02; the disk bounding the fibre loop in R130-02;
  d ≠ d! for d ≥ 3 in R109.3. The readings the notes quote agree with the ink where checked: *ne s'envoie pas* (091),
  *est un mono* and the analytic margin (114), *structure de drapeaux* (114), *si d'_0 = d_1* and the two (225) (136).
  No note rests on the misreads found on the sampled pages (*explicite*, *marquage*, *st.ble*, *Et*).
- **The prime for his "!" is inherited.** The notes of streams 3 and 4 use D′_d where the ink has D^!_d (R109.3,
  R120-03, R122-02, R124-02). R109.3 treats the decoration of the principal cover on 109–111 as an open reading
  question; on 110 the ink has his "!" (D̃^!_d in (155)), as on 117, 122 and 124. R122-02 and R124-02 stay valid
  questions in the right notation, but their search terms ("Dprime") would miss both the "!" notation of scans
  048–092 and La Longue Marche.
- **Sourced in the literature, not in La Longue Marche.** Each note is marked C0 ("comparison … unavailable") and lists
  search terms it did not run. The bibliography has 22 entries with links and the scope checked. Not checked offline,
  to check before reuse: Kronberg, Soomro and Top (2017), Propositions 2.1 and 3.1 (N064-01, R072-02); Paris and
  Rolfsen (2000), cited as Theorem 7.3 in R092-01 and as Proposition 7.2 in R104.3 for the same paired-twist kernel;
  Noohi (2014), Theorem 5.2 (R080-02); Segal (1968), § 1, for "semi-simplicial" including degeneracies (R128-02);
  Keel (1992), "Catalogue, Facts 1–4" (R072-03); Abramovich, Caporaso and Payne (2015), § 3.4 (R094.2).
- **Wrong claims:** none found.

## The context zip

The notes have no La Longue Marche comparison because the run received the first build of the package. That build's
context zip is a valid zip with no entries (22 bytes); it is kept as
`rejected_builds/MPL_147_048-137_empty_context_DO_NOT_SEND/`, written at 09:12:55 UTC. The run's log starts at
09:14:34 UTC. The corrected package in `packages/MPL_147_048-137/` (context zip 1,635,582 bytes) was written at
09:15:15 UTC, 41 seconds after the run began. The two prompts differ only in the sentence that describes the context
zip, so the transcription was made under the same rules; only the notes lost the comparison, which in package 2 gave
13 tested locations in La Longue Marche. The C0 search terms in each note are a ready list for a notes-only pass with
the real context zip.

## Recommendation for the remaining packages

**Keep 90 scans, with a rule in the template for parallel streams.**

- **Completeness held** at 90 scans, with no thinning in the run or within a stream and more words per unit of ink
  than package 2.
- **Accuracy fell**, to 2.15 errors per 100 words against 0.73; without the one repeated decision, 1.25 against 0.46,
  still 2.7 times package 2's rate. Unmarked errors: 1.52 against 0.27; without the decision, 0.72. The fall is not
  haste: minutes per page within a stream rose by a fifth (1.61 against 1.32), and the two fastest sampled pages have
  no error. Eight pages cannot show whether accuracy changes with position in a stream; completeness does not.
- **The largest cause is the split into streams.** Ten of the 24 errors, and about 44 places in the package, are one
  sign that two streams read and two did not; the quotation marks and the Gothic S split the same way, and two thirds
  of the doubts register carry a default confidence because the streams' records could not be matched when they were
  merged. Going back to 45 scans does not by itself prevent parallel streams: package 1, with 45 scans, also ran in
  four. One stream for 90 scans would take about 2.4 hours of transcription at this package's pace (144.9
  stream-minutes), before the notes.
- **What remains** without that decision, 14 errors, is nine misreads, one omission and four breaches of the rules on
  abbreviations and punctuation. The sample cannot tell whether the misreads come from the harder pages or from how
  the work was split; the next package will.
- **Add to the template:** "If you split the scans into parallel streams, first write one notation table for the whole
  package (signs, letters, quotation marks, abbreviations) and give it to every stream; before freezing, compare the
  streams' readings of every recurring sign against the ink and make them agree. In this hand an exclamation mark as
  exponent (M^!, D^!_d, T^!_d) is a sign of its own, written `^!`, not a prime; his quotation marks are double quotes,
  written ``…'', never « ». The doubts register gives every doubt its own confidence." The sentence on abbreviations
  stays; it was broken twice here.
- **Before upload:** list the context zip and check that it holds La Longue Marche; send only the final build.
- **Check the next package the same way.** Go back to 45 scans in one stream if its streams again disagree on a
  recurring sign, or if its rate without repeated decisions stays above 1.0 per 100 words (this package 1.25,
  package 2 0.46).
- **Second pass of this package:** the stream errors can be repaired by search after checking each place: the 44 primed
  D, T and P on 109–128 (to `^!` where the ink has it), the 17 « » pairs, the doubt pairs of the Gothic S. The rest
  needs the line-by-line re-reading against the scans that the second pass does in any case: 8 of the other 14
  errors carry no mark.

## Verdict

1. Complete: every scan in full, nothing summarized or skipped, and no thinning towards the end of the run or of a
   stream (words per unit of ink 0.98, 0.98 and 1.04 of the average over the thirds). On completeness, 90 scans
   match 45.
2. Not as accurate as package 2: 2.15 errors per 100 words against 0.73, 1.70 against 0.55 for misread words and
   symbols, 1.52 against 0.27 unmarked; without the one repeated decision, 1.25, 0.81 and 0.72 against 0.46, 0.27 and
   0.27. The largest cause is four parallel streams that did not share decisions, which a template rule can prevent.
   The rest comes from misreads, on pages harder than package 2's, and from breaches of the rules on abbreviations and
   punctuation. Haste is not the cause: the fastest pages have no errors.
3. Package size: stay at 90 scans with the stream rule in the template, and check the next package with this method.
   Go back to 45 scans in one stream if its streams again disagree on a recurring sign, or if its rate without repeated
   decisions stays above 1.0 per 100 words.
