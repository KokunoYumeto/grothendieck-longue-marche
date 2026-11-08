# LM_C3-663-681 — editorial and research notes

## Source and scope

This edition transcribes the 19 supplied manuscript images in filename order, scan663 through scan681. The scan numbers in `\scanpage` follow the filenames, as required by the task. The handwritten lower-left counters run from 662 through 680, one lower than the filenames; those counters are retained as marginal items. The author's separate top pagination is retained only where visible. The institutional imprint, web address and printed counter outside the black manuscript border are archival metadata and are not included in the manuscript text.

All readings were made from the supplied scans and enlargements. No published transcription, external reconstruction or mathematical correction was used. Research notes refer to this supplied excerpt and do not claim that a statement remains unresolved elsewhere in the manuscript or in the literature.

**Source reference (APA form, using the supplied identification):** Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Manuscript, Montpellier archive, cote 140-3; supplied scan files 663–681]. Université de Montpellier.

## Editorial conventions and verification

The transcription is a LaTeX fragment without a preamble or macro definitions. It uses only the requested editorial macros, standard LaTeX mathematical commands and TikZ-CD. The receiving document must define the editorial macros and load the relevant mathematical and TikZ-CD packages. TikZ-CD matrices use `ampersand replacement=\&` so that they can occur safely inside the `\diagram` macro argument. No rendered image or scan crop is embedded.

Alternatives inside `\unsure{reading|alternative}` are editorial alternatives, not extra symbols asserted to occur in the manuscript. In particular, the broad continuous ambient-group glyph is encoded as `\unsure{\mathfrak{G}|\mathcal{G}}`, and its recurring angular superscript as `\unsure{\natural|\sharp}`. Neither the exact printed alphabet nor the conventional name of that superscript can be established confidently from the ink alone. Earlier M glyphs on scans 668–671 are additionally marked `\unsure{M|\mathcal{M}}`: an independent comparison found no consistent upright-versus-script distinction that would justify treating them as a different alphabet from the later calligraphic M. No mathematical distinction is inferred from this encoding.

Visible ditto strokes remain strokes rather than expanded wording. Deletions, insertions, marginal notes, duplicated equation labels, surprising indices and uncertain arrow decorations are retained locally. Straight diagram connectors without a discernible head are kept as headless lines. Relative diagram geometry has been arranged for editable typesetting; crowded overwriting is represented by the deletion and doubt macros rather than by invented clean readings.

Every scan was read as a whole, transcribed in detail, reread against its image and inventoried. Independent rereads were also used for difficult prose, marginalia, diagram connections and the final pages. Static checks cover the page order, inventories, balanced LaTeX groups/environments and TikZ-CD destinations. Full TeX compilation was unavailable: the installed executables lack the required LaTeX format files and packages. The source is therefore structurally checked, not certified by a successful render.

## Pagination and coverage


| Filename scan | Author top page | Handwritten border counter | Inventoried elements |
|---|---|---|---|
| 663 | 634 | 662 | 22 |
| 664 | None visible | 663 | 10 |
| 665 | 635 | 664 | 19 |
| 666 | None visible | 665 | 14 |
| 667 | 536 / 636 (uncertain) | 666 | 14 |
| 668 | None visible | 667 | 21 |
| 669 | 637 | 668 | 22 |
| 670 | None visible | 669 | 23 |
| 671 | 638 | 670 | 20 |
| 672 | None visible | 671 | 7 |
| 673 | 639 | 672 | 21 |
| 674 | None visible | 673 | 12 |
| 675 | 640 | 674 | 17 |
| 676 | None visible | 675 | 21 |
| 677 | 641 | 676 | 20 |
| 678 | None visible | 677 | 9 |
| 679 | 642 | 678 | 25 |
| 680 | None visible | 679 | 13 |
| 681 | 643 | 680 | 8 |


## Table of doubts


Locations refer approximately to the manuscript page and its displayed equation numbers. Confidence describes the reading of the ink, not the mathematical plausibility of the expression. Repeated global alphabet/superscript uncertainties are also marked in the transcription.


### Scan 663


| Scan | Approximate line / element | Reading | Alternatives / reason | Confidence |
|---|---|---|---|---|
| 663 | Lines 1–2 | « effectivement mis en jeu par (38) » | The strokes after « effectivement » are severely abbreviated; « mis en jeu » is only a tentative reading. | low |
| 663 | Throughout | `\mathfrak{G}` | `\mathcal{G}`; a continuous flourished G, with no certain separate tilde. | medium |
| 663 | Throughout | `\natural` | `\sharp`; angular hooked superscript, explicitly retained as a doubt. | low |
| 663 | (46d) | « automatique si …, vu a) b) » | Alternative: « vu c) b) ». The final short reference is crowded against the right edge. | medium |
| 663 | (47), left membership | `\in` | `\notin`; an upright heavy stroke overlaps the sign. | low |
| 663 | (47), right | « t.q. » | Tiny joined strokes. | medium |
| 663 | (48), cancelled superscripts | G | Original lettering is densely overwritten. | low |
| 663 | (48), set condition | « t.q. » | Tiny joined strokes after the unit group. | medium |
| 663 | (49), right-hand defined object | `S\widetilde N_0` | `\widetilde N_0`; initial stroke can be a joined S. The factor inside the parentheses appears `N_0`, and has not been silently prefixed by S. | low |
| 663 | Between (49) and (50) | `\widetilde N_0` with special superscript | Isolated overwritten interlinear group symbol; no unambiguous attachment arrow. | low |
| 663 | (51), underbrace label | plain u | underlined u; the fresh independent reading favors a plain letter. | medium |
| 663 | (51), final product | underlined u | Plain u; underline is indistinct at the lower edge. | medium |

### Scan 664


| Scan | Approximate line / element | Reading | Alternatives / reason | Confidence |
|---|---|---|---|---|
| 664 | Throughout | Flourished G / angular superscript | `\mathfrak{G}\|\mathcal{G}` and `\natural\|\sharp`, as on scan 663.; medium / low | low |
| 664 | Line 3, cancelled word | de | Small crossed-over word before a surviving de. | low |
| 664 | Line 3, cancelled notation | L_0 with special superscript | Heavily cancelled group symbol. | low |
| 664 | Line 3, embedding subscript | L_0,G | Exact last subscript glyph is uncertain. | low |
| 664 | First sequence number | 52 | 51; retained explicitly as an alternative, not corrected from « 52 bis ». | medium |
| 664 | Below first sequence, cancellation | avec G | Several overwritten strokes; G is particularly unclear. | low |
| 664 | Cross-reference before final formula | 46 with a cancelled preceding 4 | Crowded rewriting. | low |
| 664 | End of (52 bis) target | semicolon-like mark | Could be an unfinished closing stroke; best symbol retained with doubt. | low |

### Scan 665


| Scan | Approximate line / element | Reading | Alternatives / reason | Confidence |
|---|---|---|---|---|
| 665 | Throughout | Flourished G / special superscript | `\mathfrak{G}\|\mathcal{G}` and `\natural\|\sharp`.; medium / low | low |
| 665 | (53), first row | bold a | Ordinary a; the two occurrences are heavily inked. | low |
| 665 | (53), second row | rho in both b(rho) and rho to a power | sigma is a possible alternative; the ink looks much more like rho. The apparent mismatch with the subscript on N has not been corrected. | medium |
| 665 | (53), second row | où | Highly contracted word / repetition sign. | low |
| 665 | NB, opening of parenthesis | Dans | Large first letter with the rest reduced to strokes. | medium |
| 665 | NB, page references | 580, 580' | Second reference's terminal strokes are unclear. | low |
| 665 | NB, « je me suis … » | entrecorné | entortillé; internal letters cannot be settled from the scan and no dictionary form has been substituted confidently. | low |
| 665 | NB, cancellation after difficult verb | natural-like glyph | Densely overwritten mark. | low |
| 665 | (55), second map label | delta_Z | delta_z; case uncertain. | medium |
| 665 | (56), first kernel | Z_rho | Overwritten glyph; no clean original state is recoverable. | medium |
| 665 | (56), crossed-out final word | surjectif | Lettering heavily crossed; best tentative reading. | low |
| 665 | Left lower margin | semi-dir | Terminal abbreviation stroke uncertain. | medium |
| 665 | (57), cancelled glyph before chi | kappa | Heavily overwritten small letter. | low |
| 665 | Last line | p.580' | Final prime-like mark uncertain. | medium |
| 665 | NB, first sentence | traîner | trainer; circumflex indistinct on a fresh independent reread. | medium |

### Scan 666


| Scan | Approximate line / element | Reading | Alternatives / reason | Confidence |
|---|---|---|---|---|
| 666 | Throughout | Flourished G / special superscript | `\mathfrak{G}\|\mathcal{G}` and `\natural\|\sharp`.; medium / low | low |
| 666 | (58), central G | subscript rho | Possibly a prior/cancelled group letter under the large rewritten glyph. | low |
| 666 | (58), central horizontal arrow | cancelled hooked arrow | Rewritten arrow shaft contains dense cancellation. | low |
| 666 | (58), upper-right connection | arrow pointing toward N_rho | The two sloping strokes appear to point up-left; direction is explicitly marked beside the connection, without imposing the direction suggested by the group names. | low |
| 666 | (59), N_sigma-to-G edge | b | Small thickened label. | medium |
| 666 | (59), N_rho-to-G edge | cancelled a with rho,sigma | Most of the label is occluded by cancellation; subscript strokes remain. | low |
| 666 | (59), lowest right Z | Z_sigma | Z_rho; the visible subscript is sigma-like and is retained as the first reading. | medium |
| 666 | (60), first cancellation | = N_rho intersect G_rho_sigma | Dense oblique strokes; individual symbols uncertain. | low |
| 666 | (60), second cancellation | SN_rho, SN_sigma with special superscripts | Readable outlines but heavy cancellation. | medium |
| 666 | (61), first kernel | SZ_rho | SN_rho; N/Z overwrite. | low |

### Scan 667


| Scan | Approximate line or location | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 667 | Top pagination | 536 | 636; Low: the first character has a top bar and angular lower stroke; sequence alone cannot settle it. | low |
| 667 | (62), first pair, central groups | N_rho, with or without special superscript | Z_rho; Low: several superposed horizontal and diagonal strokes obscure both base letters. | low |
| 667 | (62), first pair, lower kernel | SZ_rho | SN_rho; Medium: Z is retraced. | medium |
| 667 | (62), right vertical maps; (63), right vertical maps | downward arrow labelled 1 | double-line identity decoration; Medium: a short vertical stroke sits beside the long downward arrow; it is not silently erased. | medium |
| 667 | (63), first upper kernel | Z_rho | I_rho; Medium: the connecting stroke is unusually upright. | medium |
| 667 | Below (63), cancellation | avec (63) | First word and parenthesized numerals are partly overwritten; Low. | low |
| 667 | Above the preceding cancellation | sans | —; Medium. | medium |
| 667 | Before On a donc | d'où, deleted | Short abandoned mark/word; Low. | low |
| 667 | (64), crossed diagonal from the special ambient group towards the bottom ambient group | deleted hook-arrow-like connector | Original arrowhead/decorations obscured; Low: the surviving long oblique stroke is retained. | low |
| 667 | Ambient alphabet and special superscript throughout | fraktur G; natural | calligraphic G; sharp; Medium: global typographic uncertainty. | medium |

The lower first character label in (63) is read epsilon_(3 gamma), with gamma supported by comparison to the fan of character maps in (64). The bottom row of the second (63) pair has no visible epsilon label. In (64), the arrow at the left goes down from the special ambient group to its plus group, and the two right arrows go upward from the lower row; those directions were retained. The top row of (64) reads L_0 with the special superscript equals SZ_(rho,sigma), without a second superscript on SZ. The two closing parentheses after the final reference (45) are preserved.

### Scan 668


| Scan | Approximate line / position | Reading | Alternatives / issue | Confidence |
|---|---|---|---|---|
| 668–671 | Earlier M glyphs throughout | M | calligraphic M; independent comparison found no consistent upright/script distinction from the later M glyphs | low |
| 668 | Deleted heading | du cas inserted above Exemple universel | The small words and attachment are partly intersected by the cancellation. | medium |
| 668 | Deleted heading | GL(2,Z)^ | SL(2,Z)^; first letter is crossed. | low |
| 668 | Throughout, large group glyph | \(\mathfrak{G}\) | \(\mathcal{G}\); the ink is a continuous flourished G, not clearly a separate tilde. Every occurrence is marked. | low |
| 668 | Throughout, special superscript | \(\natural\) | \(\sharp\); all occurrences remain explicitly marked. | low |
| 668 | Opening, before groupes | ss- | The abbreviation sits above the line; its insertion status is probable. | medium |
| 668 | Opening list | \(N_\rho^?\) | The N and its small subscript are uncertain; the question mark appears in the manuscript. | low |
| 668 | Opening list, insertion above N | \(M'''(-\bar j)\) | \(M''(-\bar j)\); number of primes and attachment uncertain. | low |
| 668 | Universal-case formula | SL(2,Z)^ | GL(2,Z)^; first letter heavily joined to L. | medium |
| 668 | Before \(=M(0).L_0^\pi\) | \(M[0]'\) | \(M[0]!\); short vertical mark with apparent lower dot. | low |
| 668 | Repeated arguments of M, and (66) | 0 | \(\infty\); the argument is a compressed open wave in these places. The clearly closed loops in (65) and the undeleted part of (67) are retained as 0. | medium |
| 668 | Deleted text after \(G_{\rho,\sigma}\simeq M\) | ss-groupe | Final letters reduced to a stroke. | medium |
| 668 | Following undeleted equality | ss-groupe | Final letters reduced to a stroke. | medium |
| 668 | End of parenthetic universal-case calculation | \(M'\) | \(M'!\); terminal stroke may be emphasis punctuation. | low |
| 668 | Just after \(M'_0\) | Deleted ! | An overinked character survives, not securely identifiable. | low |
| 668 | Lower paragraph, before \(Z_{\rho,\sigma}\) | Deleted le | Small overinked loop may be an abandoned symbol instead. | low |
| 668 | corresponde ... M(0) | à | Two short strokes; preposition probable but not fully resolved. | medium |
| 668 | Above (67) | Deleted possèdera, inserted aura | Both verbs are compressed and crossed; possédera also possible, but the written accent cannot be securely resolved. | low |
| 668 | (67), first object | Deleted \(M_{\rho,\sigma}\), inserted \(G_{\rho,\sigma}\) | Letter forms overlap; which letter is the abandoned one is not certain. | low |
| 668 | (67), canceled right-hand equality | \(G_{\rho,\sigma}^{\natural}\simeq Z_{\rho,\sigma}(0).G^{\natural}\) | Much of the first object and terminal superscript is overwritten. Best visible reading retained in place. | low |

No separate author page number is visible at the top. The border counter is retained as a marginal number; it is not silently substituted for the scan number.

### Scan 669


| Scan | Approximate line / position | Reading | Alternatives / issue | Confidence |
|---|---|---|---|---|
| 669 | Top line, deleted verb | définira | définirait; ending crossed. | medium |
| 669 | Throughout, large group glyph | \(\mathfrak G\) | \(\mathcal G\), as on scan 668. | low |
| 669 | Throughout, special superscript | \(\natural\) | \(\sharp\), as on scan 668. | low |
| 669 | (68), above first equals | dfn | déf; abbreviated definition label is cramped. | low |
| 669 | (68), subgroup arguments | 0 | \(\infty\); several arguments are reduced to a small loop or wave. | medium |
| 669 | (68), second row after decorated Z | \(\subset\) | \(=\); closed C-like stroke has two thick horizontals. | low |
| 669 | (68), cancellation before plain Z | G | Overwritten vertical/looped character. | low |
| 669 | (68), third row, subscript after sigma | 0 | Position differs from the parenthesized subscript in the first row; no parentheses supplied here. | low |
| 669 | Left below (68) | Deleted 67 | Small overinked old numbering may instead be another two-character label. | low |
| 669 | Before (69), canceled sign after hom | \(\varphi\) | Very small dark stroke. | low |
| 669 | Before (71) | Deleted sur \(L_0\) | Long stroke passes through sur and the foot of L; underlining remains a possible reading. | medium |
| 669 | (71), lower matrix, upper-left entry | 1 | Entry overwritten; 1 is the visible best reading, not supplied from the matrix type. | medium |
| 669 | Before (72), canceled introductory word | donc | d'où; remainder “on a” is retained. | low |
| 669 | (72), right vertical character label | \(\chi_\gamma\) | \(\chi_\sigma\); small subscript ambiguous. | low |
| 669 | (72), bottom \(\widehat{\mathbb Z}\)-to-\(B''_0\) arrow | Two right arrowheads | A strengthened single arrowhead is possible; the mapping label on this arrow carries the uncertainty mark. | low |
| 669 | Last word | tout | Crossbar intersects the word; retained as text rather than confidently declared canceled. | medium |

### Scan 670


| Scan | Approximate line / position | Reading | Alternatives / issue | Confidence |
|---|---|---|---|---|
| 670 | First line insertion | 2ième | 2ème; raised abbreviated ending is very small. | medium |
| 670 | End of second line, canceled | et le | Both short words lie under a thick crossing stroke. | low |
| 670 | Third line, after qui | nous | Only low joined horizontal strokes survive. A fresh independent reading also favored nous; there is no separate ink for an expected word such as intéressent. The abrupt syntax is retained. | low |
| 670 | Throughout, special superscript | \(\natural\) | \(\sharp\), as on scans 668–669. | low |
| 670 | Before the first \(G_{\rho,\sigma}^{\natural}\) | Deleted M | Overwritten mathematical letter. | low |
| 670 | Before on peut aussi | Deleted Rem | Alors; canceled word uncertain. | low |
| 670 | Before section | Deleted la | Short crossed article. | medium |
| 670 | Above section | Inserted “bon” | “bonne”; the ending is reduced to a wave, so grammatical agreement has not been imposed. | low |
| 670 | (74), overwritten first object | Deleted \(M_{\rho,\sigma}\), inserted \(Z_{\rho,\sigma}\) | The superimposed letter forms obscure the order of revision. | low |
| 670 | (74)–(76), subgroup argument | 0 | \(\infty\); the small form varies between a loop and a wave. | medium |
| 670 | (75), superscript on \(L_0\) | \(\mu\) | \(\natural\); here the sign looks H-like and differs from the zigzag sign in (76). | low |
| 670 | Last paragraph | est | Rapid terminal strokes are not fully separable. | medium |
| 670 | Final continuation | Ce choix d'un | Le choix d'un; first word is only one broad curve and a short stroke. | medium |

No author page number appears at the top. The small writing above the first line belongs to the insertion “2ième”, not to pagination.

### Scan 671


| Scan | Approximate line / position | Reading | Alternatives / issue | Confidence |
|---|---|---|---|---|
| 671 | First line, subgroup argument | 0 | \(\infty\); wavy small loop. | medium |
| 671 | Throughout, large group glyph | \(\mathfrak G\) | \(\mathcal G\); retained as the common typographic doubt. | low |
| 671 | Throughout, special superscript | \(\natural\) | \(\sharp\); retained as the common typographic doubt. | low |
| 671 | After c'est, canceled phrase | cette définition de G | First word and final G lie under the cancellation stroke. | low |
| 671 | Above canceled phrase | groupe “plus fin” qui serait | “plus fin” is a second insertion above the first. No unobserved ce or le is supplied to regularize the revised syntax. | medium |
| 671 | End of revised sentence | meilleur | meilleure; final short stroke ambiguous. | medium |
| 671 | New approach paragraph | système de restrictions | système des restrictions; the first word is heavily compressed, and the short preposition/article has an extra stroke. | low |
| 671 | Canceled word after qui | doivent | Only initial d and part of the ending survive distinctly. | low |
| 671 | After \(l\in L_0\) | a-shaped sign | Small dark sign immediately after the subscript is retained as a doubtful a; it might be an abandoned mark or another symbol. | low |
| 671 | Universal-case quotient, first numerator superscript | + | *; thick crossing strokes. | low |
| 671 | Parenthetic et ... dans | \(\overline{\mathrm m}\) | =; the lower of the two strokes is slightly wavy, consistent with the author's “même” abbreviation. | medium |
| 671 | Parenthetic quotient denominator | \(\pi\) | \(\tau\); no subscript 0 is visible here. | low |
| 671 | After pas par, canceled word | cette | Letters under the crossing stroke. | medium |
| 671 | End of the central-element discussion | exorciser | Most of the distinctive exorci- is visible; final strokes compressed. | medium |
| 671 | Bottom first group name | Deleted M, inserted G | Overlapping capitals; revision order not fully certain. | low |

### Scan 672


| Scan | Approximate line / element | Reading | Alternatives / reason | Confidence |
|---|---|---|---|---|
| 672 | End of line 5 | deleted “de” | A dark de-shaped word has horizontal overink. The cancellation status is less secure than the letters. | low |
| 672 | Line 6 | au | en; the short joined strokes before “découpage” are compressed. | medium |
| 672 | Last line after § 48 | barred and underlined XI | The right numeral is reduced to an upright/curving stroke; both horizontal marks are retained. | low |

The opening adjective in “aussi fin que possible” is singular in the ink. The raised insertion “encore” belongs before “des erreurs”, and its curved leader is not a parenthesis. Separate enlargement resolved “assez grossières”; that reading is no longer doubtful.

The authoritative scan number is the filename number, 672. The handwritten counter inside the lower left border is 671, and the printed archival footer repeats 671. No original manuscript number is visible at the top. The handwritten border number is retained as a margin item; the printed archive attribution and URL are not manuscript text. The short paragraph continues the unfinished sentence at the end of scan 671. The lower part of the manuscript sheet is blank.

The whole page and enlarged overlapping upper and lower crops were read and reread. Separate enlargements were used for “assez grossières”, the overinked final “de”, the preposition before “découpage”, and the terminal Roman reference. No diagram, formula, or additional marginal prose occurs on the page.

### Scan 673


| Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 673 | All group superscripts | `\natural` | `\sharp` | low |
| 673 | Ambient flourished group letter throughout diagrams | `\mathfrak{G}` | `\mathcal{G}` | low |
| 673 | Heading and all M symbols | `\mathcal{M}` | ordinary `M` written cursively | medium |
| 673 | First (78) label | `(78')` | overwritten `(78)`; last mark indistinct | low |
| 673 | First (78), second formula, struck object | `Z_{\rho,\sigma}` | subscript obscured | low |
| 673 | (79), top-left deleted mark | `1` | one crossed stroke | low |
| 673 | (79), G^natural diagonal | `\sim` | an unlabelled short curved stroke | low |
| 673 | (79), S₀M^natural diagonal | deleted northwest arrowhead | heavy overwritten hook | low |
| 673 | (79), lower M object | deleted `S_0` before M | overwritten letter or insertion mark | low |
| 673 | Above “suites exactes” after (79) | `hom. de` | `hom de` | medium |
| 673 | First lower paired exact sequences | `(80)` | `(89)` | medium |
| 673 | Second lower paired exact sequences | `(82)` | `(81)` | medium |
| 673 | (84), struck beginning of kernel | `L_0^{\natural}\times` | individual strokes indistinct | low |

The long curved arrow in the left margin of the two (78) blocks is reproduced, and the duplicate/overwritten numbering is retained. In the second row of the paired diagram labelled (82|81), the last ambient group is written without a visible plus superscript; no plus has been supplied. The product formula for S₀Γ shows a base subscript under the first multiplication sign only, and this is preserved.

### Scan 674


| Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 674 | All group superscripts | `\natural` | `\sharp` | low |
| 674 | Ambient flourished group glyph | `\mathfrak{G}` | `\mathcal{G}` | low |
| 674 | M alphabet throughout | `\mathcal{M}` | cursively written ordinary M | medium |
| 674 | (85), second line, final object | `Z_{\rho,\sigma}` | overwritten first stroke; possible doubled Z | medium |
| 674 | (86), cancelled left start | `{ S_0` | a cancelled brace and incomplete object | low |
| 674 | (87), second line, middle M subscript | `\rho` | `2` | low |
| 674 | Remark label | `Rmq` | `Remq` | medium |
| 674 | First prose line | `dégelée` | ending and first vowel uncertain | low |
| 674 | First prose line | `donne` | compressed final strokes | medium |
| 674 | Second paragraph, first line | `compétition` | `comparaison` | medium |
| 674 | Same line | `invariants` | ending compressed | medium |
| 674 | After “surtout,” cancelled word | `les` | heavily overwritten short word | low |
| 674 | “la …” shorthand | m above an equals-like double stroke | `\overline{\mathrm m}` shorthand | low |
| 674 | Struck phrase before G | `de façon pré` | incomplete last word | low |
| 674 | Last paragraph, first line | `p. r. à` | `p. v. à` | medium |

In the prose immediately before (88), the first M is visibly without the natural/sharp superscript and the second bears it. This is retained even though the direction of the ensuing normality statement is surprising beside the quotient in (88). The crossed-out phrase “de façon pré” and the replacement “et entre” are both transcribed. The trailing parenthesis is not closed on this page, and no closing parenthesis has been supplied.

### Scan 675


| Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 675 | All group superscripts | `\natural` | `\sharp` | low |
| 675 | Ambient flourished G throughout | `\mathfrak{G}` | `\mathcal{G}` | low |
| 675 | M alphabet throughout | `\mathcal{M}` | cursive ordinary M | medium |
| 675 | First line | `environnants` | compressed ending | medium |
| 675 | (89), subscript on first tau | `M` | `\mu` | medium |
| 675 | (89), struck phrase at right | `d'im.` | `d'où` | low |
| 675 | (89), tuple first component | `\tau'_\rho` | first letter heavily overwritten | medium |
| 675 | (89), group under second tuple component | `N_\rho` | `N_\sigma`; rho-shaped descender remains | low |
| 675 | (89), cancelled group under third component | flourished G `\in G_{\rho,\sigma}` | first glyph heavily obscured | low |
| 675 | Before (90), struck word | `des` | overwritten short word | medium |
| 675 | (90), upper right | `image` | possible abbreviation of the word | medium |
| 675 | (90), upper right two-element set | `\tau_\gamma` | `\tau'_\gamma`; prime uncertain | low |
| 675 | First paragraph after (90) | `bordéliques` | accent/ending uncertain | medium |
| 675 | Same line, page reference | `584` | first digit retraced | medium |
| 675 | Last paragraph | `redévelopper` | compressed middle vowels | medium |
| 675 | Last paragraph, second named group | `SG_{\rho,\sigma}` | `Sg_{\rho,\sigma}` | medium |

The group in the upper right annotation to (90) has no securely visible natural/sharp superscript on M, and none is supplied. The lower-left ambient group in (90) has no securely visible τ subscript, and none is supplied. The membership annotations under the tuple in (89) are oriented vertically in the source and have been retained in a small diagram. The first line continues the preceding page; no unprinted closing parenthesis has been added.

### Scan 676


| Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 676 | Ambient flourished G throughout | `\mathfrak{G}` | `\mathcal{G}` | low |
| 676 | Group superscript throughout | `\natural` | `\sharp` | low |
| 676 | M alphabet | `\mathcal{M}` | cursive ordinary M | medium |
| 676 | Upper-left NB, last verb | `engendrent` | ending reduced to a stroke | medium |
| 676 | Upper-right note, before G_0 arrow G | `noter` | compressed middle letters | medium |
| 676 | After Z, M in the naming sentence | `et` | `etc` | medium |
| 676 | Named invariant after “considération de” | `\Xi_{\rho,\sigma}^{G}` | `\overline Z_{\rho,\sigma}^{G}` | low |
| 676 | (92), lower-left group | G with `++` | one retraced `+` | medium |
| 676 | After “Il revient au” | `=` | shorthand `\overline{\mathrm m}` | medium |
| 676 | “transforment”, two named generators | `\xi_\rho,\xi_\sigma` | `\ell_\rho,\ell_\sigma` | low |
| 676 | After “en des”, lower crossed attempt | `éléments` | highly obscured word | low |
| 676 | Same place, upper crossed attempt | `groupes` | highly obscured word | low |

The upper-left note and the main word “surjectif” occupy overlapping visual lines, but “surjectif” belongs to “l'hom”, not to the NB. The added parenthesis “(dans 1° à 5°)” is above the NB. The bottom arrow of (92) visibly bears a prime on φ; it has not been normalized to the unprimed top label. The cancelled word at the far right after “en des” has two superposed writing layers: both are transcribed tentatively rather than silently lost. The following cancelled `G^natural-conjugués à` is clearly separated from its replacement `éléments G_tau^natural-conjugués`.

### Scan 677


| Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 677 | Ambient flourished G throughout | `\mathfrak{G}` | `\mathcal{G}` | low |
| 677 | Natural/sharp superscript throughout | `\natural` | `\sharp` | low |
| 677 | (93), arrow-label subscript | `Z` | `z` | medium |
| 677 | Before (94), construction name | `Amal.` | Internal letters compressed; A-like initial and l-like ending supported by independent rereading | low |
| 677 | (94), target superscript | cancelled natural/sharp | retraced epsilon-like mark; the cancellation itself is uncertain | low |
| 677 | Paragraph after (95) | `relatifs` | `relatives` | medium |
| 677 | Same paragraph, last line | `s'envoient` | very compressed envoi sequence | medium |
| 677 | Remarque, verb after G′ | `satisfasse` | ending strongly reduced | medium |
| 677 | Remarque, “Pour … couple” | `tt` | universal quantifier `\forall` | low |
| 677 | (96), element following second commutator | `\varepsilon_1` | `\xi_1` | medium |

The curved arrows in the unnumbered pair start at the L groups, pass beneath the intervening inclusion and Z object, and point to the corresponding ambient plus group. The superscript on the target of (94) is retained as an uncertain cancellation; it has not been deleted editorially on mathematical grounds. The broad brace labeled (96) spans the prose condition and (97); the struck duplicate “(96)” inside the brace and the separate “(98)” underneath are both retained. The exponent in (96) reads μ−1, and the profinite integer symbol has no visible unit superscript; no such superscript is supplied.

Fresh independent rereading favors the A-like initial and l-like ending of `Amal.`; that abbreviation remains doubtful, but the following word is resolved as `et`. The earlier alternatives `stand.` and `d’où` were discarded in the final transcription.

### Scan 678


The scan number is the filename number. The lower border has handwritten `677`, retained as `\margin{677}`. No original manuscript page number appears at the top of this image; the printed institutional footer is archival metadata, not manuscript text.

| Scan | Approximate line or location | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 678 | Opening line, cross-reference after `Cent` | `96` | `98`; the second digit has one continuous open upper stroke rather than two visibly closed loops | medium |
| 678 | (99) and subsequent pair of groups, recurring ambient-group glyph | `\mathfrak{G}` | `\mathcal{G}`; the handwriting has a continuous waved upper contour | medium |
| 678 | Superscripts in the pair of groups | `\natural` | `\sharp`; recurrent hooked diagonal glyph | medium |
| 678 | Line after (99), `Alors ... hom` | `tout` | The short compressed letters and their crossing stroke do not permit a fully certain reading | medium |
| 678 | Between the two parenthesised pairs | rightward arrow | bare connecting dash; an arrowhead is not clear | low |
| 678 | Insertion above `universel` | `où` | `i.e.`; the short first word is extremely compressed | medium |
| 678 | Deleted word before `ce qu'on a envie` | `tout` | The crossing stroke partly obscures the internal letters | medium |
| 678 | Final display, argument of the first subgroup | `0` | `\infty`; the ink looks two-lobed, and an omega-like form is also visually possible | low |

### Scan 679


This is filename scan 679, original top pagination `642`, and lower-border number `678`. The lower-border number is retained as a margin item, and the canceled numeral preceding `642` is also retained.

| Scan | Approximate line or location | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 679 | Top, canceled page number before `642` | `646` | `686` or `648` cannot be excluded because of the crossing strokes | low |
| 679 | Upper-left marginal title | `ss-gr.` | `sous-gr.`; the letters run obliquely together | medium |
| 679 | First bracketed argument in the marginal title | `0` | `\rho`; overtracing obscures the centre and lower edge | low |
| 679 | Superscripts on all three marginal subgroup names | deleted `\natural` | deleted `\sharp`; these are inked over in each name | low |
| 679 | Repeated subgroup superscript throughout the page | `\natural` | `\sharp`; the hooked diagonal form remains unresolved | medium |
| 679 | (101), first relation after the bracketed zero | `\subset` | `=`; this sign has been heavily retraced | medium |
| 679 | Prose immediately before (102), final abbreviation | `cano.` | `cano-`, `can.`; the terminal stroke is a dash-like mark | low |
| 679 | Paragraph after (102), adverb after `sont` | `manifestement` | No secure alternative; the middle letters and end are compressed | medium |
| 679 | Fiber product after `isomorphes`, overwritten letter before `N_\rho` | deleted `Z` | an overwritten initial form of `N`; retained separately rather than normalized away | low |
| 679 | Exact-sequence kernel, recurring ambient-group glyph | `\mathfrak{G}` | `\mathcal{G}` | medium |
| 679 | Prose `entre les groupes (...)` | `68` | `64`; the second numeral has a retraced descending lower stroke | medium |
| 679 | Canceled marginal reference beside `On définit` paragraph | `69` | The digits are almost wholly crossed; the second may be `0` | low |
| 679 | Insertion `(ou M(1/2))` above last paragraph | attached after `M(\rho)` | The curve begins after that expression and before `et`; the mathematical meaning has not been used to relocate it | high |

### Scan 680


| Scan | Approximate position | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 680 | Throughout | `\mathfrak{G}` | `\mathcal{G}`; a single broad, internally curled manuscript glyph, not an independently established typographic alphabet | medium |
| 680 | Throughout, especially (103)–(106) | Superscript `\natural` | `\sharp`; the hooked diagonal glyph is clear as a recurring sign, its conventional encoding is not | medium |
| 680 | (103), left label | `103` | Numerals are heavily retraced; no separate earlier number can be distinguished securely; High for final `103` | high |
| 680 | Immediately below (103) | `sous-groupes` | `ss-groupes`; the compressed first component has only a few strokes | medium |
| 680 | Paragraph before (104) | Superscript on `\Gamma_{\rho,\sigma}` retained | This is visibly present even though other occurrences of the quotient on the same page have no such sign; High for presence, medium for encoding | medium |
| 680 | Right of (104) | `1/2 directs` | Final mark can also look like `=`; encoded `\unsure{directs\|direct=}` | medium |
| 680 | Between (104) and (105) | `\overline{\mathrm m}` | Alternative: `=`; the two nearly horizontal strokes do not securely resolve the shorthand. The fresh independent reread adds this doubt rather than expanding it | medium |
| 680 | Introduction to (106) | `aura` | The compressed `ur` cannot be fully separated; `aura` is the best reading | medium |
| 680 | (106), superscript of top middle object | Deleted special superscript on `\mathcal{M}` | The sign is overwritten with short cancellation strokes; retained as `\deleted{\unsure{\natural\|\sharp}}` | medium |
| 680 | (106), horizontal connectors | Initial upper connector and lower middle-to-right connector | Arrowheads weak; each is transcribed as `\unsure{\longrightarrow\|-}`. Plain connectors with no visible head remain dashes | medium |
| 680 | (106), central vertical arrows | `\simeq` | `\sim`; the labels are wavy and nearly vertical, with the straight component difficult to distinguish | medium |
| 680 | First sentence after (106) | `s'identifie` | Final vowel is only a short stroke | medium |
| 680 | Bottom, last kernel | `L_0` with special superscript | The zero curls into the end of the horizontal foot of `L`; it is present | high |

### Scan 681


| Scan | Approximate position | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 681 | Throughout | Special superscript `\natural` | `\sharp`; recurring hooked diagonal glyph | medium |
| 681 | (108), right factors | `\mathfrak{G}` | `\mathcal{G}`; the single broad manuscript glyph does not conclusively establish the typographic alphabet | medium |
| 681 | Paragraph, initial `Z` | Deleted `\Gamma` beneath final `Z` | The upright stroke and upper bar may be an overwritten `Gamma`, or merely a retracing of `Z`; preserved as `\deleted{\unsure{\Gamma}}Z` | low |
| 681 | Parenthetical reference | `cf`, without a full stop | No distinct full stop is visible immediately after the `f`; the reference itself reads `p. 636′ ff` | high |
| 681 | End of parenthetical reference | Full stop | A small triangular dot is visible after the closing parenthesis; it may be a pen mark rather than sentence punctuation | low |
| 681 | Middle paragraph, “on … ce groupe” | `dénote` | The final tall `t` supports this reading; `désigne` was rejected after enlarged inspection because it does not fit the last strokes | medium |
| 681 | Same phrase | `ce` | Compressed two-stroke word; `son` is less well supported | medium |
| 681 | Standalone inclusion and first two lines of (108) | Parenthesized `0` | `\infty`; the opening parenthesis joins a small loop and can appear two-lobed. The last line of (108) separates the strokes more clearly as `(0)` and is transcribed without doubt | medium |
| 681 | (108), second line before the isomorphism sign | Dot | A small separate mark precedes the wavy relation stroke; may be a pen-start artifact | low |
| 681 | (108), final right factor | Ambient group with no superscript | No plus or special superscript is visible; no symbol has been supplied | high |


## Abbreviations met


Expansions below are editorial explanations only. None has been substituted into the transcription. Spellings and punctuation variants are kept together only in this list.


### Scan 663


- `hom`: homomorphisme.
- `int`: automorphisme intérieur / conjugaison intérieure.
- `Aut`: automorphismes.
- `Norm`: normalisateur.
- `t.q.` (doubtful): tel que.
- `idem`: the same assertion.

### Scan 664


- `hom`: homomorphisme.
- `Aut`: automorphismes.
- `Ker`: noyau.
- `i.e.`: id est.
- `bis`: repeated/supplementary numbering.

### Scan 665


- `NB`: nota bene.
- `p`: page(s).
- `Cent`: centralisateur.
- `Ker`: noyau.
- `semi-dir` (doubtful): semi-directe.

### Scan 666


- `etc`: et cetera (written in the manuscript, not an editorial omission).
- `hom`: homomorphismes.

### Scan 667


| As written | Proposed expansion |
|---|---|
| épi | épimorphisme |
| cf. | confer / comparer |
| p. | page |

### Scan 668


| Written form | Proposed expansion (notes only) |
|---|---|
| ss- / ss-groupe | sous- / sous-groupe |
| p. | page |
| ff | and following pages (conventional “following”) |
| 1/2 direct, 1/2 directs | semi-direct, semi-directs |

### Scan 669


| Written form | Proposed expansion (notes only) |
|---|---|
| can. | canonique |
| hom | homomorphisme |
| iso | isomorphisme |
| dfn (uncertain) | définition |
| det | déterminant |

### Scan 670


| Written form | Proposed expansion (notes only) |
|---|---|
| iso | isomorphisme |
| i.e. | id est |
| épi | épimorphisme |
| Rem (canceled, uncertain) | remarque |

### Scan 671


| Written form | Proposed expansion (notes only) |
|---|---|
| cf. | confer / compare |
| i.e. | id est |
| int | intérieur / inner automorphism, according to the displayed notation |
| autom. int. | automorphisme intérieur |
| \(\overline{\mathrm m}\) (uncertain) | même |

### Scan 672


No prose abbreviation is expanded. The section sign and the Roman reference are retained in their visible forms.

### Scan 673


| As written | Proposed expansion |
|---|---|
| `p.` | page |
| `hom. de` (doubtful punctuation) | homomorphismes de |

### Scan 674


| As written | Proposed expansion |
|---|---|
| `Rmq` / `Remq` | remarque |
| `p. r. à` / `p. v. à` | probably “par rapport à”; reading uncertain |
| `autom.` | automorphismes |
| `int.` | intérieurs |
| m with double lower stroke (uncertain) | même |

### Scan 675


| As written | Proposed expansion |
|---|---|
| `d'im.` (struck, uncertain) | d'image |
| `im.` | image |
| `inv.` | inverse |
| `p.` | page |
| `etc` | et cetera |

### Scan 676


| As written | Proposed expansion |
|---|---|
| `NB` | nota bene |
| `hyp.` | hypothèse |
| `Cf.` / `cf` | confer, compare |
| `p.` | page |
| `hom` | homomorphisme |
| `ff` | and following pages |
| `etc` | et cetera |
| `loc. cit` | loco citato |
| `autom.` | automorphisme |
| `i.e.` | id est |
| `=` (uncertain shorthand) | même |

### Scan 677


| As written | Proposed expansion |
|---|---|
| `resp.` | respectivement |
| `hom` | homomorphisme |
| `Amal.` (uncertain) | possibly amalgamée / amalgame; unresolved |
| `n°` | numéro(s) |
| `tt` (uncertain) | tout |
| `conv.` | convenable |
| `Aut` | automorphismes |
| `Cent` | centralisateur |
| `i.e.` | id est |

### Scan 678


| As written | Proposed expansion (notes only) |
|---|---|
| `Cent` | centralisateur |
| `i.e.` | id est |
| `hom` | homomorphisme |
| `ss-groupes` | sous-groupes |

### Scan 679


| As written | Proposed expansion (notes only) |
|---|---|
| `ss-gr.` (uncertain) | sous-groupes |
| `hom` | homomorphisme(s) |
| `cano.` (uncertain) | canonique(s) |
| `isom.` | isomorphismes |

### Scan 680


| As written | Possible expansion (notes only) |
|---|---|
| `ss-groupes` (alternative reading) | sous-groupes |
| `1/2 directs` | semi-directs |
| `\overline{\mathrm m}` | même |
| `ext.` | extension |
| `i.e.` | id est |
| `hom` | homomorphisme |

### Scan 681


| As written | Possible expansion (notes only) |
|---|---|
| `cf` | confer |
| `p.` | page |
| `ff` | following pages |


## Honest legibility assessment


The formulas are often more legible than the running prose, but the most crowded diagrams, overwritten letters, short word endings, marginal notes and shorthand signs remain insecure. In particular, the introductory parenthesis and kernel notation on scan 663, the autobiographical aside on 665, the revisions around (64), the abandoned heading and formulas on 668, the compressed clauses on 670–671, and the corrections on 673–677 should receive editorial attention. The final pages were examined at the same level of enlargement as the first. A marked tentative reading should not be quoted as a settled transcription without checking the image; an inventory value of `yes` means that the element is represented, not that every letter in it is certain.


### Scan 663


The principal sequence of numbered formulas is legible, but the introductory parenthesis, overwritten superscripts in (48), membership sign in (47), and isolated interlinear notation above (50) are insecure. The continuous upper flourish of the ambient group glyph and the angular superscript do not unambiguously identify a printed typeface or glyph; both are marked in place. The bottom border counter is transcribed as a marginal number, not conflated with the author's top pagination.

### Scan 664


The body of this half-written page is fairly readable. The cancellations in line 3 and before the description of the image, the sequence label, the vertical hooked inclusion, and the small final mark in (52 bis) are the least secure features. No upper manuscript pagination is supplied on this sheet.

### Scan 665


The centralizer formulas are comparatively clear. The NB's autobiographical parenthesis, the first row of (56), and the small lower-margin abbreviation are less secure. Both sloping marginal notes were read in rotated crops. The « d'où » preceding (56) belongs to the main text; it is not incorporated into the nearby sloping margin note.

### Scan 666


Both large diagrams have been typeset as diagrams. In (58), plain segments, a second upper stroke labelled a, and the ambiguous upper-right direction are retained; in (59), the two dashed arrows, two labels 2, two labels 3, the hooked inclusions, and the cancelled edge label are included. The central SNρ/SZσ and Nρ/Zσ positions are crowded in the source, so the typeset diagram separates these neighbouring objects enough to keep their incident edges identifiable; their relative order is preserved. The cancellation in (60) and overwritten first kernel in (61) are insecure.

### Scan 667


Most objects in the five diagrams are distinct, but the two rho normalizer letters in (62), several identity-map decorations and the cancelled connector in (64) are overwritten. These are the least secure details on this otherwise sparsely worded page. Straight manuscript connecting segments lacking a readable head remain no-head edges, including the upper gamma-to-1 connector in (64).

### Scan 668


The main prose is relatively readable after enlargement. Confidence is lowest in the canceled heading, the inserted group name above the opening list, overlapping prime/exclamation-like strokes, and the crowded last line (67). The text retains an unclosed parenthesis visible in the manuscript rather than supplying punctuation.

### Scan 669


The prose and matrices are clearer than the corrections in (68). The notation \(B'_0\) in (70) and \(B''_0\) in (72) is preserved with different prime counts: the second display visibly has two strokes. The corresponding arrows and the right-hand vertical character in (72) deserve editorial verification. The bottom sentence continues onto scan 670.

### Scan 670


The matrices and the final expectation are readable. The most fragile prose is the compressed clause after “les cas typiques qui” and the overwritten article/adjective before “section”. Equation (75) retains a distinct doubtful exponent rather than forcing the special superscript used elsewhere. “J'ai des bonnes raisons” is retained with the visible des.

### Scan 671


The opening functoriality discussion is fairly clear. Two layers of revision after “c'est” make the resulting syntax abrupt, and the transcription does not repair it. The small sign after \(L_0\), the quotient denominator in the parenthesis, and the overwritten bottom group name need particular care. The distinctive verb is read as exorciser, not silently replaced by the mathematically plausible exclure.

### Scan 672


This is one of the more legible pages in the range. The heavily abbreviated ductus remains clear enough to read the complete paragraph. The material uncertainties are localized to one cancellation, one short preposition, and the Roman reference; no prose illegibility placeholder is used.

### Scan 673


Most isolated group objects are legible, but the alphabet of the ambient group and the recurring superscript remain uncertain. The cube diagram is cramped: the diagonal from the lower S₀M object, the cancelled prefix of the lower M object, and the distinction between hooks and curved pen entries are the least secure features. The two lower equation labels are retained as doubts rather than silently put into numerical sequence. The manuscript number is 639; the bottom handwritten/archive number is 672 although the input filename is scan673.

### Scan 674


The formula blocks are relatively clear apart from an overwritten subscript, a cancelled start at (86), and the recurrent alphabet/superscript questions. The rapid prose is substantially harder: “dégelée,” “compétition,” and the shorthand following “la” should be checked against the original if higher-resolution material becomes available. The manuscript's apparent reversal of the M normality statement has not been repaired. The filename/archive-footer offset remains +1.

### Scan 675


This is comparatively spacious, but corrections cluster around (89): the first τ, the second group subscript, the cancelled third group, and the changed wording at right. The right-hand definitions in (90) run close to the scan edge and do not allow a confident decision on every prime or superscript. The final paragraph is readable with reservations on the long verb and the capitalization of SG. The filename/archive-footer offset remains +1.

### Scan 676


The main prose is fairly clear, but the opening marginal notes are small and slope in different directions; they were read after rotation and enlargement. The superscript alphabet and the invariant resembling Ξ remain uncertain. The two overwritten attempts at the lower right are the least trustworthy prose readings on this page. In (92) the visible doubled plus and the lower φ′ are preserved, without mathematical correction. The filename/archive-footer offset remains +1.

### Scan 677


The page is comparatively clean but contains several very compressed words. The least reliable readings are the construction name before (94) and the tiny overwritten superscript on that equation's target. The curved homomorphism diagrams are unambiguous in their broad arrangement. The bottom condition is relatively legible at high enlargement; caution remains necessary for the generator letter in (96) and the shorthand before “couple”. The original top number is 641, whereas the archive and bottom handwritten number are 676; the filename is scan677.

### Scan 678


The two paragraphs are comparatively open and legible, and the page is otherwise blank below them. The least secure readings are the opening cross-reference, the arrow/dash between the pairs of groups, and the very short insertion above `universel`. The deletion and both insertions have been retained; no additional mathematical condition has been supplied to make the prose or formula agree with adjacent pages.

### Scan 679


The main prose and the rightward exact-sequence arrows are generally readable. The marginal title, canceled page/reference numbers, overwritten letter in the fiber product, and heavily retraced first inclusion in (101) are the least reliable portions. The right end of (100) lies against the frame; the final equality and closing brace were inspected at enlarged scale. All three inclusion maps and the four-arrow exact sequence are typeset, including their grouping brace and equation label; the long horizontal repetition strokes in (101) have been retained as strokes, rather than expanded into repeated words.

### Scan 680


The formulas are broadly readable, but the special superscript, the canceled superscript in (106), and very short arrowheads require explicit doubt. The source distinguishes the bracketed zero `[0]` from the parenthesized `rho` and `sigma` labels; all are kept. Equation (106) is typeset as a complete TikZ-CD diagram with the opposed directions of the two outside vertical identity maps preserved: the left map points down, the right map points up. Horizontal connectors that are visibly headless remain headless. The top superscript on `Gamma` before (104) is preserved without normalization. The page has no upper manuscript pagination; the handwritten border number 679 is recorded separately from filename scan 680. The institutional archive footer is not manuscript text.

### Scan 681


The final page was read in full and inspected at enlarged scale for the text, reference, overwritten `Z`, subgroup label, and all three lines of (108). Its prose is relatively readable, but “dénote ce”, the parenthesized zero, and the possible correction beneath `Z` are less secure. The explicit absence of a superscript on the final ambient group in (108) has been preserved. The upper manuscript number 643 and lower handwritten border number 680 are both recorded, separately from filename scan 681. There are no additional manuscript blocks in the large blank lower area; the archive imprint below the black border is not manuscript text.


---

## Research notes — separate from the transcription


All items below concern Grothendieck (1981), at the scan locations specified. “Unproved claim” means that a proof is not given in this local excerpt; it does not claim that no proof exists elsewhere. A “conjecture” entry may record an explicit expectation or methodological doubt rather than a formal conjecture. Reader proposals are labelled “own idea,” with their confidence and reason. No proposal is presented as established or as new, and none was used to repair the transcription.


### Scan 663


1. **Scan 663, (45)–(47) — unproved claim.** The paragraph says « son image est formée des systèmes … tels que » and gives four conditions, then a kernel. A proof within this local setup would have to establish both necessity and sufficiency of (46), and verify the identification of representatives in (47); the excerpt refers back to (38), not supplied in this package.
2. **Scan 663, (46d) — unproved claim.** The parenthetical « automatique si … » asserts that the stabilizing condition follows when the two signs agree. The exact final reference is doubtful, so any verification must first settle that reading and then check which of the preceding conjugacy conditions are used.
3. **Scan 663, (50)–(51) — unproved claim.** The claimed isomorphism is qualified by « si … est injectif », followed by a « hom canonique injectif ». The role of uniqueness of the exponent in the procyclic map is worth checking, including the dependence on that injectivity condition.

### Scan 664


1. **Scan 664, first paragraph and (52) — unproved claim.** The text says « il est encore vrai que l'image inverse … est … », then constructs a « suite exacte canonique ». The inverse-image assertion is the point to check: it identifies the kernel of the map induced from scan 663 and requires the embedding denoted by i to be read precisely.
2. **Scan 664, (52 bis) — unpursued implication.** The displayed quotient identifies a kernel of an action with two sign coordinates. This isolates an obstruction to faithfulness after passing to the stated quotient; establishing such an interpretation requires the definitions preceding these supplied pages and is not being claimed here as a separate theorem.

### Scan 665


1. **Scan 665, (53)–(55) — unproved claim.** The equalities identifying centralizers with kernels, and the marginal equalities « SNρ = SZρ, SNσ = SZσ », are stated without a proof on this page. A check needs the definitions of the sign maps and the relevant ambient subgroup; the apparent rho/sigma discrepancy in (53) must be resolved editorially before any formal verification.
2. **Scan 665, (56)–(57) — unproved claim.** The parenthesis explains surjectivity by an element τ′ with both sign values −1, and the margin asserts « Suites exactes semi-directes ». The proposed splitting should be checked as an actual homomorphism with the required image and intersection, not merely as a preimage of the nontrivial sign.
3. **Scan 665, (56), lower margin — unpursued implication.** The last sequence is said also to split using μτ, giving two indicated choices for that row. Comparing the resulting complements and their conjugacy is a natural local question, but this page does not work out such a comparison.

### Scan 666


1. **Scan 666, (58)–(59) — unproved claim.** The replacement introduced by « ou mieux » presents a large network of subgroup maps, including arrows labelled 2 and 3 and two dashed maps from the positive ambient group. Verifying each claimed inclusion and the compatibility of the alternative paths would require the earlier definitions; some arrow directions and one lower subscript remain transcription doubts.
2. **Scan 666, (60)–(61) — unproved claim.** The groups defined by intersections are followed immediately by « On a des suites exactes ». Intersecting with a chosen subgroup preserves the displayed kernels formally, but the asserted surjectivity to the same quotient needs a separate check from the manuscript's hypotheses.
3. **Scan 666, (59) — own idea. Confidence: low.** An incidence-list verification of every arrow, with the arrows labelled 2 and 3 checked separately, could help distinguish an intentional structural claim from overwritten notation. The reason for suggesting this is the dense local overlap and the rho/sigma ambiguity in the lowest row; this is an editorial verification strategy, not a mathematical result or novelty claim.

### Scan 667


- **Scan 667, (63); unproved claim.** The two vertical maps on the kernel and middle group are explicitly labelled “épi.” A proof would need to identify their images and check surjectivity separately; the diagrams alone do not supply that argument on this page.
- **Scan 667, after (63) and (64); unproved claim.** The phrase “diagrammes analogues sans” the special superscript extends the displayed constructions to the unmarked groups. Checking that extension would require a comparison of the defining subgroups and the maps, including the directions preserved in (64).
- **Scan 667, (64); own idea.** The three character maps from gamma could provide a convenient invariant for comparing the three displayed subgroup embeddings. Confidence: low; this is only a suggested organization of the diagram, since the precise kernels and compatibility conditions must be recovered from the surrounding definitions.

### Scan 668


- **Scan 668, opening paragraph — conjecture / expectation.** “l'idéal serait que ce soit ... lui-même” states the wish that the already defined decorated group could supply the desired analogue. The following universal-case calculation is presented as an obstruction to that wish; recovering the prior definitions and checking that calculation would be the first mathematical task.
- **Scan 668, lower paragraph — unproved claim.** “Il n'y a pas de difficulté si on peut définir” reduces the desired construction to finding a subgroup \(Z_{\rho,\sigma}(0)\) giving the splitting in (66). A proof would need to verify the internal product, the indicated action, and the passage from (66) to the factorization (67), with the author's exact ambient groups.
- **Scan 668, (65)–(67) — own idea; confidence medium.** Compare different possible complements \(Z_{\rho,\sigma}(0)\) before treating the resulting construction as canonical. The reason is internal to this page: a splitting is required, but uniqueness or independence of its choice is not asserted here. This is a proposed check, not a claim that such nonuniqueness occurs.

### Scan 669


- **Scan 669, paragraph before (69) — unproved claim.** “une façon standard d'obtenir un scindage can.” announces a canonical splitting from a suitable homomorphism compatible with the \(\tau\)-action. Checking the claim requires precise definitions of the homomorphism's compatibility conditions and of each vertical map in (72); calling the construction standard does not supply that verification on this page.
- **Scan 669, (71)–(72), final sentence — unpursued implication.** The text starts the conditional assertion “Si l'hom (71) est un iso” and continues it on the next scan. The exact-sequence diagram suggests a useful distinction between properties of the left map and properties of the induced splitting, but the statement should be evaluated only with the continuation, not completed from the diagram alone.
- **Scan 669, (72) — own idea; confidence medium.** Verify the displayed lower extension and the two prime counts against their definitions before using this diagram to transport a splitting. The reason is the visible difference between \(B'_0\) and \(B''_0\), which could encode a genuine distinction or a manuscript change; this note proposes a check and does not correct the transcription.

### Scan 670


- **Scan 670, top continuation — unproved claim.** The preceding isomorphism hypothesis is said to let a splitting of the second exact sequence define one of the first “par image inverse”. A proof should track the pullback and check that the indicated inverse image is a subgroup mapping isomorphically to the quotient, rather than merely a set of lifts.
- **Scan 670, upper paragraph — conjecture / question.** The text says the subgroup is “pas assez petit” for the desired ambient construction but “pas assez gros” to obtain an isomorphism in (71). These are distinct size requirements; determining their simultaneous effect in the intended “cas typiques” is a concrete problem left by this discussion.
- **Scan 670, (73)–(76) — unproved claim.** The new hypothesis asks that the inverse image of the displayed diagonal section be a “sous-groupe section”. The transition from the intersection statement (75) to the additional surjectivity requirement is explicit; verifying surjectivity is the substantive missing step.
- **Scan 670, last paragraph — conjecture / expectation.** “J'ai des bonnes raisons de penser que ... cette condition ... [est] satisfaite dans tous les cas vraiment utiles” is an explicit expectation, conditional on the existence of (69). The manuscript does not specify those useful cases or give the reasons on this page.
- **Scan 670, (73)–(76) — own idea; confidence medium.** For each concrete instance, compute the image in the upper-triangular matrix group before testing the diagonal inverse image. The reason is the author's explicit reduction to a section: the calculation could reveal exactly which quotient elements admit a lift with zero upper-right entry, without assuming that all of them do.

### Scan 671


- **Scan 671, first paragraph — unproved claim.** The construction is said to be “fonctoriel” in an “évident” sense, with the functoriality discussion deferred to later. Verifying this requires identifying the admissible morphisms and checking that the chosen subgroup or section is preserved by them.
- **Scan 671, first paragraph — conjecture / expectation.** The finer group is said to merit the simpler notation, subject to the inconvenience of an “un peu trop alambi-quée” definition. This is a methodological preference for the smaller group, not a proof that its proposed definition has all desired properties.
- **Scan 671, middle paragraph — conjecture / question.** “Autre façon de procéder !” proposes suitable restrictions in the definition of \(Z_{\rho,\sigma}\) that would give the displayed membership equivalence. The page does not provide those restrictions; the following example instead explains why one natural strategy is insufficient.
- **Scan 671, universal-case paragraph — unproved claim.** The chosen element is described as “l'élément central non trivial” of the quotient, and its inner automorphism is consequently trivial. The centrality and nontriviality require checking in the stated universal case; their significance here is the author's warning that the indicated action cannot distinguish the element he wants to “exorciser”.
- **Scan 671, final paragraph — conjecture / question.** “peut-être est-il prématuré” explicitly questions whether to refine these groups already. The thought continues on scan 672 and should not be converted into a permanent abandonment of the construction.
- **Scan 671, central-element obstruction — own idea; confidence medium.** Test whether any proposed restriction depends only on the induced inner action before attempting a general construction. The reason is the page's own example: a nontrivial central quotient element has trivial inner action, so a criterion using only that action may be unable to distinguish it from the identity. This is a suggested diagnostic, not a newly established theorem.

### Scan 672


1. **Scan 672, opening lines — conjecture (methodological expectation).** The author allows for “des erreurs d'orientation assez grossières” and expects examination of particular cases to correct them. This is a stated concern about the direction of the construction, not a claim that a particular formula on the preceding pages has been disproved.
2. **Scan 672, final paragraph — unpursued implication.** The author says he will stop investing effort in the current subdivision and may later “raffiner les constructions présentes”. The comparison with the constructions of § 48 is deferred. No such comparison or refinement is carried out on this page.
3. **Scan 672, whole paragraph — own idea; confidence medium.** The preceding proposed complements and the current warning should be tracked separately when extracting mathematical claims from this range. The reason is textual: the current paragraph explicitly suspends refinement pending examples, so a later formal statement should not silently upgrade every preceding exploratory construction to an established canonical one.

### Scan 673


1. **Scan 673, definitions (77)–(78); kind: unproved claim.** The page introduces the fibre-product groups with “On posera comme dans p. 583” and then writes the plain-product isomorphisms for the groups M. Checking these assertions would require the preceding definitions of the structure maps and confirmation whether the multiplication signs in the plain-product displays encode direct products or shorthand for products over the common quotient.
2. **Scan 673, (79)–(84); kind: unproved claim.** “d'où diagramme de suites exactes” asserts the exactness of a network of maps whose proofs are not supplied here. A verification would need to identify each kernel, establish the relevant surjectivity, and check the compatibility of all vertical and diagonal morphisms; the cancelled and overwritten labels must first be resolved against nearby pages.
3. **Scan 673, (77)–(84); kind: own idea.** The definitions suggest constructing a finite-quotient test of the asserted kernel identities, with each structure map represented explicitly. Confidence: medium, because the fibre-product descriptions offer a concrete test mechanism, but no claim about the full profinite construction follows from any finite sample and some manuscript notation remains uncertain.

### Scan 674


1. **Scan 674, remark first paragraph; kind: conjecture / question.** Grothendieck writes, “Je ne suis pas sûr que les variantes S₀ … soient très utiles.” This is an explicit doubt about the usefulness of the enlarged variants, and it invites comparison of what information the forgetful maps preserve or discard.
2. **Scan 674, before and in (88); kind: unproved claim.** “on a des isomorphismes” is followed by the canonical identifications of the three quotients. A proof should identify the common quotient through the structure maps; it should also disentangle the visibly surprising direction of the M normality assertion in the preceding prose without silently correcting the transcription.
3. **Scan 674, final paragraph; kind: unpursued implication.** The larger groups are described as “fourre-touts,” enabling the automorphisms ρ and σ to be regarded as induced by inner automorphisms of the surrounding groups. The precise relation between the outer-action data and these ambient realizations is not worked out on this page.
4. **Scan 674, (85)–(88); kind: own idea.** One could test whether the S₀ variants are needed only to retain a chosen lift through Z, by comparing their universal mapping properties with those of the corresponding M and Γ groups. Confidence: medium; the displayed fibre-product isomorphisms motivate the comparison, but they do not establish redundancy or a universal property on their own.

### Scan 675


1. **Scan 675, (89)–(90); kind: unproved claim.** An element τ′ is written in M^natural “au dessus de” an element of the quotient, followed by “d'où … plongements canoniques.” The canonical nature of these embeddings should be checked by specifying the tuple components and verifying their compatibility over the common quotient, especially because the tuple and its target groups were revised on the page.
2. **Scan 675, paragraph after (90); kind: unproved claim.** “On peut reproduire les diagrammes … de p. 584” defers the expanded diagrammatic argument to an earlier construction. A proof would require an explicit comparison with that construction and checks that replacing the relevant groups by the natural/sharp variants preserves exactness and commutativity.
3. **Scan 675, final paragraph; kind: unpursued implication.** “Je vais voir si je peux me dispenser … de redévelopper les liens” with the named Z and SG groups expressly postpones these relationships, “quitte à y revenir au besoin par la suite.” A later editorial or mathematical study should check where those omitted links are needed, without treating the omission here as a proof of independence.

### Scan 676


1. **Scan 676, upper-left NB; kind: unpursued implication.** The note says that “Jusqu'ici … on n'avait pas utilisé l'hyp.” that ρ and σ generate the ambient plus group, with “(dans 1° à 5°)” inserted. This suggests checking the precise minimal hypotheses for the earlier constructions separately from those needed for functoriality; the note itself does not state a replacement set of hypotheses.
2. **Scan 676, naming paragraph through (92); kind: unproved claim.** The reference to “des conditions équivalentes comme dans loc. cit” is followed by the descent square and the assertion that “lequel u′ sera unique.” A verification would need the earlier equivalent conditions and an explicit use of the stated surjectivity of φ; the visibly primed lower arrow should first be resolved from the author's conventions, not silently repaired.
3. **Scan 676, paragraph after (92); kind: unproved claim.** The page reduces the descent requirement to automorphisms that “stabilisent le noyau de φ.” To justify the equivalence in the precise setting one must verify existence of the induced quotient automorphism as well as compatibility with the normalizer and conjugacy conditions written here.
4. **Scan 676, upper-right note; kind: own idea.** The proposed notation G_0 → G could make a reformulation in terms of a fixed source group and its quotients easier to track across later functoriality diagrams. Confidence: low, because this is an editorial interpretation of the short “Il vaut mieux noter” note, not a mathematical construction explicitly carried out on this page.

### Scan 677


1. **Scan 677, (93)–(95); kind: unproved claim.** The compatibility “avec les actions” and “avec les hom” is used to obtain the maps φ_G and its natural/sharp restriction. A proof should identify precisely the construction named before (94) and verify that its universal property applies to the displayed compatible maps; the name remains palaeographically unresolved here.
2. **Scan 677, paragraph after (95); kind: unproved claim.** “Il n'en faut pas plus” is the stated reason that all earlier “constructions et diagrammes” map to their primed counterparts. This broad assertion calls for a construction-by-construction check of the hypotheses, including kernels, fibre products, and any chosen subgroup data in the preceding pages.
3. **Scan 677, Remarque and (96)–(98); kind: unpursued implication.** The author assumes that a pair satisfying the displayed commutator relation admits an automorphism with the specified values on ρ and σ. The centralizer reformulation in (98) makes this an explicit compatibility problem for two prescribed actions, but this page does not establish the hypothesis or enumerate the groups for which it holds.
4. **Scan 677, (96)–(98); kind: own idea.** One could test the stated extension condition in small finite quotients by enumerating the permitted α′, β′ and checking whether the two centralizer cosets meet in an automorphism with the required values. Confidence: medium as a diagnostic method, not as a proof for the profinite setting; its usefulness depends on whether the chosen quotients preserve the source conditions.

### Scan 678


1. **Scan 678, (99) and following sentence — unproved claim.** The text concludes, “est nécessairement admissible,” for every indicated $(\rho,\sigma)$-homomorphism into the displayed target pair, after expressing the preceding centralizer relation by the preservation of $L_0$. A proof check should identify precisely which hypothesis on the target makes the automorphism $u'$ exist and why the preservation condition is sufficient for admissibility; the opening reference is itself uncertain in the handwriting.
2. **Scan 678, final paragraph — unpursued implication.** “Nous allons appliquer ceci au cas … universel” announces a specialization, but the page postpones it to introduce the three subgroups written $\mathcal M(0)$, $\mathcal M(\rho)$, and $\mathcal M(\sigma)$. The later construction should be checked for dependence on a choice of section, rather than treating the announcement here as a canonical identification.

### Scan 679


1. **Scan 679, (100)–(102) — unproved claim.** After defining the three subgroups by $U=i_Z(u)$, $U=i_\rho(a)$, and $U=i_\sigma(b)$, the manuscript says they are “tous trois isomorphes” to the displayed fiber product. A proof should explicitly use compatibility of each inclusion with its map to $\gamma_{\rho,\sigma}$ and show that projection forgetting $U$ has the prescribed graph as its inverse.
2. **Scan 679, paragraph following the exact sequence — unproved claim.** The projection is said to induce isomorphisms, and hence “les trois groupes sont donc des sous-groupes sections.” To verify this precisely, one should check that the kernels intersect each graph subgroup trivially, as well as verifying surjectivity onto the full indicated $S_0\Gamma_{\rho,\sigma}$; the old cross-reference is retained as written and is uncertain.
3. **Scan 679, final paragraph — unpursued implication.** The manuscript sends the three graph subgroups to corresponding subgroups in $\mathcal M_{\rho,\sigma}$. The distinction between square brackets at the zero label and parentheses at the two other labels is material on these pages: the later kernel computation should be checked before calling all three images complements.
4. **Scan 679, (101) — own idea.** It may be useful to formulate these three constructions uniformly as graph subgroups of a fiber product, and then compare their images under the same quotient map. **Confidence: high as a proposed organizational device, not as a new result**, because all three definitions on the page differ only in which coordinate supplies $U$; injectivity after passing to the quotient still requires a separate check.

### Scan 680


1. **Scan 680, paragraph after (103), unproved claim.** The statement that the two subgroups are “des groupes sections au dessus” of the indicated quotient is followed immediately by (104) and (105). A verification would have to check the projection on each graph subgroup, its trivial intersection with the kernel, and the asserted factorization; the superscript visibly attached to `Gamma` should be checked against the surrounding notation rather than silently removed.
2. **Scan 680, (106) and final paragraph, unproved claim.** The text says that the extension “s'identifie à l'ext.” and then to “l'image inverse de l'extension” involving `Z`. A proof should construct the maps in (106), establish their compatibility with the kernel embeddings and quotient maps, and verify the pullback property.
3. **Scan 680, (104)–(106), own idea.** One could compare the two explicit graph sections and the zero-labeled extension by describing the difference between sections as a kernel-valued cocycle. Confidence: medium; the two displayed semidirect descriptions motivate the comparison, but the precise action and conventions must be recovered from earlier definitions and the cancellation in (106) must remain an editorial uncertainty.

### Scan 681


1. **Scan 681, paragraph after (107), unproved claim.** The text says that a section of the `Z` extension “en définit une” for the pulled-back extension and hence for the bracketed-zero subgroup. A proof should follow the homomorphism (107), write the pullback section explicitly, and verify that the identifications on the preceding page preserve it.
2. **Scan 681, (108), unproved claim.** “donc on aura” introduces three product decompositions after choosing a section. Their verification requires trivial intersection and generation assertions for the displayed factors; the last factor has no superscript in the manuscript, which should be studied as written before any normalization is proposed.
3. **Scan 681, “Quand une telle section est fixée”, own idea.** Investigate how the resulting parenthesized-zero subgroup changes under a different choice of section and which resulting decompositions are conjugate. Confidence: medium; chosen splittings of group extensions naturally suggest a cocycle comparison, but the action, topology, and allowed conjugations are not fully specified on this page alone.
