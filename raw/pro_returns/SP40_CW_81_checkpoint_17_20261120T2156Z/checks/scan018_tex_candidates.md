# Scan018 complete source candidates

No source candidate is selected. Every JSON source locator contains the exact original excerpt, UTF-8 SHA-256, Unicode offsets and line span. Complete outer wrappers, phantom state annotations, nested qualified nodes, source baselines and scopes are preserved.

| Candidate | Words / state inside the complete group | Adjacent source outside | Literal components |
|---|---|---|---|
| A.G01 | l'une; (unique), inserted; des / de; ces n | est dans before; classes after | G01.P1 |
| A.G02 | complete lemma; Lemme underline state in phantom | blank paragraph boundaries | G02.P1, G02.P2 |
| A.G03 | qu'une, inserted; la, deleted via phantom | Dire before; classe donnée after | G03.P1, G03.P2 |
| A.G04 | U_alpha / x, inserted; de Pi_J^circ, inserted; ne | classe donnée before; contient pas after | G04.P1, G04.P2 |
| A.G05 | choisi / choisie, deleted via phantom; two additional qualified points | closed formula before; quoted composant after | G05.P1, G05.P2, G05.P3 |
| A.G06 | éléments; (soit Sigma_i^-), inserted; de | l'un des before; pi_0(X setminus Sigma_i) and comma after | G06.P1 |
| A.G07 | deux, deleted via phantom; card I=2, inserted; comma | cas before; cancelled cela / OK after | G07.P1 |
| A.G08 | OK, locally qualified state with phantom deleted annotation; period; qualified gray spot | final formula comma before; archive comment after | G08.P1, G08.P2 |
| B.G01 | l'une; (unique), inserted; des / de ces n | est dans before; classes after | G01 |
| B.G02 | complete lemma; Lemme underline state in phantom | blank paragraph boundaries | G02-underline, G02-left-rule |
| B.G03 | qu'une, inserted; la, ordinary deleted macro; classe donnée; U_alpha / x de Pi_J^circ, inserted; ne contient | Dire before; pas after | G03a, G03b-main, G03b-hook |
| B.G04 | live E_i; complete qualified upper-rule group with right retrace | pas and deleted Sigma before; i.e. est after | G04-upper-rule |
| B.G05 | choisi / choisie, ordinary deleted macro; complete qualified two-point group | closed formula before; quoted composant / composante after | G05-point1, G05-point2 |
| B.G06 | éléments; (soit Sigma_i^-), inserted; de | l'un des before; pi_0(X setminus Sigma_i) and comma after | G06 |
| B.G07 | deux, deleted via phantom; card I=2, inserted | cas before; comma after | G07-cancellation |
| B.G08 | OK, complete outer unsure with phantom deleted annotation; one rising transverse stroke | final formula comma before; period after | G08-rising-stroke |
| C.G01 | l'une; (unique), inserted; de / des; ces n | est dans before; classes after | G01a |
| C.G02 | complete lemma; Lemme underline state in phantom | blank paragraph boundaries | G02a, G02b |
| C.G03 | qu'une, inserted; la, deleted via phantom; classe | Dire before; donnée is in G04 | G03a, G03b, G03c |
| C.G04 | donnée; U_alpha / x quad de Pi_J^circ, inserted; ne | classe is in G03; contient pas after | G04a, G04b |
| C.G05 | choisi / choisie, deleted via phantom; complete qualified two-point group | closed formula before; quoted composant after | G05a, G05b, G05c |
| C.G06 | first-accent-qualified éléments; (soit Sigma_i^-), inserted; de; pi_0(X setminus Sigma_i) | l'un des before; comma and d'après l'étude du after | G06a |
| C.G07 | cas; deux, deleted via phantom; card I=2, inserted; complete qualified lower hook | d'après l'étude du before; comma after | G07a, G07b |

## Assembly dependencies

- A G03/G04, B G03, and C G03/G04 use different complete word boundaries; selecting one requires consuming the corresponding adjoining source words once.
- B G04 begins before its internal `% G04:` comment. Its complete outer group contains live E_i and the qualified retraced upper-rule node. The preceding deleted Sigma remains outside.
- B G08 has an outer `\unsure` wrapper. Its final period remains outside; A G08 contains its final period and the separate qualified gray spot.
- C G07 contains the qualified lower hook and cas. A/B G07 omit that hook in their exact complete source blocks; these source scopes do not decide ink absence.
- Choosing a full nested shape preserves its enclosing node, local unsure, baseline, bounds, coordinate units and applicable outer scope. Literal stroke bodies alone do not supply those dependencies.
- In A/C G03, G05 and G07, phantom deletion annotations carry state while the separately selected literal path supplies the visible strike. A/B G08 also retains its phantom deletion state annotation.
- The first-occurrence Pi-ring and U-index qualifiers remain bound to their first printed loci; each later independently inspected locus remains separately attached in the record.
