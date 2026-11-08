# LM_P022 — Notes accompanying the diplomatic transcription

## Source, numbering, and scope

The sole reading basis is the ten supplied image files, `LM_P022_scan211.jpg` through `LM_P022_scan220.jpg`. The manuscript identification below follows the accompanying task sheet, not an independent bibliographical investigation:

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, Montpellier archive, cote 140-2, scans 211–220 of the file identified as pages 1–292; supplied contrast-enhanced images].

Scan numbers, rather than the printed image-footer numbers, identify every reference in these notes. The upper handwritten numbers 106, 107, 108, 109, and 110 occur on scans 212, 214, 216, 218, and 220 and are recorded with `\mspage`. The other handwritten sequence, 210–219 at the left edge/lower left, is preserved with `\margin`; its attribution to the author rather than an archivist cannot be established from this batch. The printed archive footer and its repeated page number are not transcribed as manuscript text.

The `.tex` file is a fragment, not a standalone document. It begins with `\scanpage{211}` and has no preamble or macro definitions. Comments of the form `% L…` supply approximate reading locations only; they are not manuscript text. A temporary wrapper with the prescribed macros defined as pass-through commands was used for a LaTeX syntax check; it is not part of the delivery.

All ten scans are represented, but not all handwriting has been deciphered. No published transcription, OCR output, later manuscript passage, or external mathematical result was used to supply missing text. Apparent inconsistencies have not been corrected. The two diagrams are described in brackets because a complete reconstruction of every overwritten label or arrow would imply greater certainty than the images support.

## 2. Table of doubts

Locations refer approximately to handwritten baselines or to a named page region, not to physical lines in the `.tex` file. Display rows and interlinear additions make exact line counts unstable. The table lists every occurrence of `\unsure` and `\illegible` in reading order, including repetitions and readings inside deleted text. A proposed reading inside `\deleted` remains a deleted reading, not an adopted statement.

**Confidence concerns the reading, not the truth of the mathematics.** “Medium” means a plausible visual reading with an unresolved feature; “low” means substantial ambiguity, overwriting, or a gap. A missing alternative means that no second reading can responsibly be supplied. Counts in `\illegible{n}` are estimates; inside formulas they may represent one unreadable symbol cluster rather than a word. An empty alternative written `\,` in the fragment means that a small apparent superscript may instead be an ink trace.

| ID | Scan | Approximate line / region | Reading | Alternative / unresolved point | Confidence |
|---|---|---|---|---|---|
| D001 | 211 | L1--4 (haut de la page) | `H_\nu` | No secure alternative | medium |
| D002 | 211 | L1--4 (haut de la page) | `transforment` | `transportent` | low |
| D003 | 211 | L1--4 (haut de la page) | `H_\nu` | No secure alternative | medium |
| D004 | 211 | L1--4 (haut de la page) | `à` | No secure alternative | medium |
| D005 | 211 | L1--4 (haut de la page) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D006 | 211 | L1--4 (haut de la page) | `H_\nu` | No secure alternative | medium |
| D007 | 211 | L5--9 | `$\overline{\mathrm m}$` | No secure alternative | medium |
| D008 | 211 | L5--9 | `\mathcal P_{\nu'}(U_\nu)` | `F_{\nu'}(U_\nu)` | low |
| D009 | 211 | L10--14, formule (30) | `!` | `*` | low |
| D010 | 211 | L10--14, formule (30) | `$\parallel$ déf` | No secure alternative | medium |
| D011 | 211 | L10--14, formule (30) | `$\parallel$ déf)` | No secure alternative | medium |
| D012 | 211 | L10--14, formule (30) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D013 | 211 | L10--14, formule (30) | `\{\nu+1\}` | No secure alternative | medium |
| D014 | 211 | L10--14, formule (30) | `a_{g,\nu}` | No secure alternative | medium |
| D015 | 211 | L15--18, bas de la page | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D016 | 211 | L15--18, bas de la page | `inclusions` | No secure alternative | medium |
| D017 | 211 | L15--18, bas de la page | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D018 | 211 | L15--18, bas de la page | `A_{g,\nu}` | No secure alternative | medium |
| D019 | 211 | L15--18, bas de la page | `B_{g,\nu}^{\circ}` | No secure alternative | medium |
| D020 | 211 | L15--18, bas de la page | `\supset` | No secure alternative | medium |
| D021 | 211 | L15--18, bas de la page | `A_{g,\nu}` | No secure alternative | medium |
| D022 | 211 | L15--18, bas de la page | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D023 | 211 | L15--18, bas de la page | `par isom.` | No secure alternative | low |
| D024 | 212 | L1--5, diagramme (31) | `\mathrm{inv.}` | No secure alternative | medium |
| D025 | 212 | L1--5, diagramme (31) | `\mathfrak S_\nu` | No secure alternative | medium |
| D026 | 212 | L1--5, diagramme (31) | `\longrightarrow` | `\supset` | low |
| D027 | 212 | L1--5, diagramme (31) | `\mathrm{inv.}` | No secure alternative | medium |
| D028 | 212 | L1--5, diagramme (31) | `\mathfrak S_\nu` | No secure alternative | medium |
| D029 | 212 | L1--5, diagramme (31) | `\hookrightarrow` | No secure alternative | medium |
| D030 | 212 | L1--5, diagramme (31) | `\hookrightarrow` | No secure alternative | medium |
| D031 | 212 | L1--5, diagramme (31) | `a_{g,\nu}` | No secure alternative | medium |
| D032 | 212 | Marge gauche, à hauteur de L4--13 | `stabilisateur` | No secure alternative | medium |
| D033 | 212 | Marge gauche, à hauteur de L4--13 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D034 | 212 | Marge gauche, à hauteur de L4--13 | `pt marqué` | No secure alternative | low |
| D035 | 212 | Marge gauche, à hauteur de L4--13 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D036 | 212 | Marge gauche, à hauteur de L4--13 | `interprétation` | No secure alternative | medium |
| D037 | 212 | Marge gauche, à hauteur de L4--13 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D038 | 212 | Marge gauche, à hauteur de L4--13 | `exposant` | No secure alternative | medium |
| D039 | 212 | Marge gauche, à hauteur de L4--13 | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D040 | 212 | Marge gauche, à hauteur de L4--13 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D041 | 212 | Marge gauche, à hauteur de L4--13 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D042 | 212 | Marge gauche, à hauteur de L4--13 | `ponctué` | `pointé` | low |
| D043 | 212 | L6--9 | `crochets` | No secure alternative | medium |
| D044 | 212 | L6--9 | `invariantes $=$` | No secure alternative | medium |
| D045 | 212 | L10--15 | `par` | No secure alternative | medium |
| D046 | 212 | L10--15 | `A_{g,\nu+1}^{\circ}` | No secure alternative | medium |
| D047 | 212 | L16--19 | `A_g` | No secure alternative | medium |
| D048 | 212 | L16--19 | `U_{g,\nu}` | No secure alternative | medium |
| D049 | 212 | L16--19 | `avec` | No secure alternative | medium |
| D050 | 212 | L16--19 | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D051 | 212 | L16--19 | `flèches` | No secure alternative | medium |
| D052 | 212 | L16--19 | `(` | No secure alternative | medium |
| D053 | 212 | L16--19 | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D054 | 212 | L16--19 | `\mathfrak S_\nu` | No secure alternative | medium |
| D055 | 212 | L16--19 | `)` | No secure alternative | medium |
| D056 | 212 | L16--19 | `\mathfrak S_\nu` | No secure alternative | medium |
| D057 | 212 | L25--26, fin de page | `déduire` | `décrire` | low |
| D058 | 213 | L1--5, formule (32) | `\mathfrak S_\nu` | No secure alternative | medium |
| D059 | 213 | L1--5, formule (32) | `\circ` | No superscript; the mark may be residual ink | low |
| D060 | 213 | L6--12 | `en` | No secure alternative | medium |
| D061 | 213 | L6--12 | `a_{g,\nu}` | No secure alternative | medium |
| D062 | 213 | L6--12 | `B_{g,\nu}` | `B_{g,\nu}^{\circ}` | low |
| D063 | 213 | L6--12 | `=(A_{g,\nu}^{\circ})_{a_{g,\nu}}` | No secure alternative | medium |
| D064 | 213 | L13--16 | `ponctué` | `pointé` | low |
| D065 | 213 | L13--16 | `Théorème` | No secure alternative | medium |
| D066 | 213 | L13--16 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D067 | 213 | L17--21, théorème et ajouts | `ponctué` | `pointé` | low |
| D068 | 213 | L17--21, théorème et ajouts | `dans` | No secure alternative | medium |
| D069 | 213 | L17--21, théorème et ajouts | `a_{g,\nu+1}` | No secure alternative | medium |
| D070 | 213 | Marge gauche, à hauteur de L17--22 | `Cette assertion` | No secure alternative | low |
| D071 | 213 | Marge gauche, à hauteur de L17--22 | `vraisemblable` | No secure alternative | low |
| D072 | 213 | Marge gauche, à hauteur de L17--22 | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D073 | 213 | Marge gauche, à hauteur de L17--22 | `on va voir` | No secure alternative | medium |
| D074 | 213 | Marge gauche, à hauteur de L17--22 | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D075 | 213 | Marge gauche, à hauteur de L17--22 | Unread passage (4 estimated word(s)/symbol group(s)) | Not recovered | low |
| D076 | 213 | Marge gauche, à hauteur de L17--22 | `raisonnable` | No secure alternative | medium |
| D077 | 213 | Marge gauche, à hauteur de L17--22 | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D078 | 214 | L1--4 | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D079 | 214 | L1--4 | `donne` | No secure alternative | medium |
| D080 | 214 | L5, suite (35) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D081 | 214 | L9--13, formule (36) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D082 | 214 | L9--13, formule (36) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D083 | 214 | L9--13, formule (36) | `retenir` | No secure alternative | low |
| D084 | 214 | L9--13, formule (36) | `facile` | `faible` | low |
| D085 | 214 | L17--25, ensemble barré en diagonale | `déjà` | No secure alternative | medium |
| D086 | 214 | L17--25, ensemble barré en diagonale | `ssi` | No secure alternative | medium |
| D087 | 214 | L17--25, ensemble barré en diagonale | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D088 | 214 | L17--25, ensemble barré en diagonale | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D089 | 214 | L17--25, ensemble barré en diagonale | `Ceci équivaut` | No secure alternative | medium |
| D090 | 214 | L17--25, ensemble barré en diagonale | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D091 | 214 | L17--25, ensemble barré en diagonale | `à` | No secure alternative | medium |
| D092 | 215 | L1--8, théorème | `et la` | No secure alternative | medium |
| D093 | 215 | L1--8, théorème | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D094 | 215 | L1--8, théorème | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D095 | 215 | L1--8, théorème | `cas anabélien` | `cas abélien` | low |
| D096 | 215 | Cette note borde l'accolade à gauche de a) et b). | `Dans le cas` | No secure alternative | medium |
| D097 | 215 | Cette note borde l'accolade à gauche de a) et b). | `de` | No secure alternative | medium |
| D098 | 215 | Cette note borde l'accolade à gauche de a) et b). | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D099 | 215 | Cette note borde l'accolade à gauche de a) et b). | `simplement` | No secure alternative | medium |
| D100 | 215 | Cette note borde l'accolade à gauche de a) et b). | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D101 | 215 | Cette note borde l'accolade à gauche de a) et b). | `contract.` | No secure alternative | low |
| D102 | 215 | L9--14 | `\pi` | `K` | low |
| D103 | 215 | L15--20, formules (37), (38) | `1` | No secure alternative | medium |
| D104 | 215 | L15--20, formules (37), (38) | `a encore` | No secure alternative | medium |
| D105 | 215 | L15--20, formules (37), (38) | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D106 | 216 | L1--4 | `dans` | No secure alternative | medium |
| D107 | 216 | L5--9, corollaire remanié | `Pour` | No secure alternative | medium |
| D108 | 216 | L5--9, corollaire remanié | Unread passage (4 estimated word(s)/symbol group(s)) | Not recovered | low |
| D109 | 216 | L5--9, corollaire remanié | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D110 | 216 | L5--9, corollaire remanié | `soit` | No secure alternative | medium |
| D111 | 216 | L5--9, corollaire remanié | `il f. et s.` | No secure alternative | low |
| D112 | 216 | L5--9, corollaire remanié | `muni` | No secure alternative | medium |
| D113 | 216 | L5--9, corollaire remanié | `\mathbb U\times\mathbb U` | No secure alternative | medium |
| D114 | 216 | L5--9, corollaire remanié | `\mathbb U` | No secure alternative | medium |
| D115 | 216 | L5--9, corollaire remanié | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D116 | 216 | L10--13 | `connexe` | `compact` | low |
| D117 | 216 | L10--13 | `on peut prendre` | No secure alternative | medium |
| D118 | 216 | L10--13 | `\operatorname{GO}(3,\mathbb R)` | `\operatorname{SO}(3,\mathbb R)` | low |
| D119 | 216 | L10--13 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D120 | 216 | L10--13 | `cas de` | No secure alternative | medium |
| D121 | 216 | L10--13 | Unread passage (5 estimated word(s)/symbol group(s)) | Not recovered | low |
| D122 | 216 | L10--13 | `\simeq\operatorname{PGL}(2,\mathbb C)` | No secure alternative | medium |
| D123 | 216 | L14--20 | `topologie` | No secure alternative | medium |
| D124 | 216 | L14--20 | `compactifiée` | `compactification` | low |
| D125 | 216 | L14--20 | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D126 | 216 | L14--20 | `la composante` | No secure alternative | medium |
| D127 | 216 | L14--20 | `du groupe des` | No secure alternative | medium |
| D128 | 216 | L21, fin de page | `\subset` | `\simeq` | low |
| D129 | 217 | L1--8, texte principal sous la note marginale | `espace homogène` | No secure alternative | medium |
| D130 | 217 | L1--8, texte principal sous la note marginale | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D131 | 217 | L1--8, texte principal sous la note marginale | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D132 | 217 | L1--8, texte principal sous la note marginale | `\pi_1(U)` | No secure alternative | medium |
| D133 | 217 | L1--8, texte principal sous la note marginale | `exacte` | No secure alternative | medium |
| D134 | 217 | L1--8, texte principal sous la note marginale | `\pi_1` | No secure alternative | medium |
| D135 | 217 | L1--8, texte principal sous la note marginale | `comm.` | No secure alternative | medium |
| D136 | 217 | L1--8, texte principal sous la note marginale | `réciproques` | No secure alternative | low |
| D137 | 217 | L1--8, texte principal sous la note marginale | `sont non-triviales` | No secure alternative | low |
| D138 | 217 | Marge diagonale supérieure gauche | `unique` | No secure alternative | low |
| D139 | 217 | Marge diagonale supérieure gauche | `$gu$` | No secure alternative | low |
| D140 | 217 | Marge diagonale supérieure gauche | `A_{g,(\nu,\nu+k)}` | No secure alternative | medium |
| D141 | 217 | Marge diagonale supérieure gauche | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D142 | 217 | Marge diagonale supérieure gauche | `A_{g,\nu}` | No secure alternative | medium |
| D143 | 217 | Marge diagonale supérieure gauche | `\Gamma_{g,(\nu,\nu+k)}` | No secure alternative | medium |
| D144 | 217 | Marge diagonale supérieure gauche | `\Gamma_{g,\nu+k}` | No secure alternative | medium |
| D145 | 217 | Marge diagonale supérieure gauche | `\simeq` | No secure alternative | medium |
| D146 | 217 | Marge diagonale supérieure gauche | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D147 | 217 | Marge diagonale supérieure gauche | `A_{g,\nu+k}^{\circ}` | No secure alternative | medium |
| D148 | 217 | Marge diagonale supérieure gauche | `contractile` | No secure alternative | medium |
| D149 | 217 | Marge diagonale supérieure gauche | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D150 | 217 | L9--14, tableau (39) et annotations à gauche | `\nu` | `2` | low |
| D151 | 217 | L9--14, tableau (39) et annotations à gauche | `K(\mathbb Z,1)` | No secure alternative | medium |
| D152 | 217 | L9--14, tableau (39) et annotations à gauche | `\operatorname{GP}(1,\mathbb C)` | No secure alternative | medium |
| D153 | 217 | L15--19 | `\operatorname{GP}(1,\mathbb C)` | No secure alternative | medium |
| D154 | 217 | L15--19 | `\operatorname{GO}(3,\mathbb R)` | `\operatorname{SO}(3,\mathbb R)` | low |
| D155 | 218 | L1--5, calcul barré en diagonale | `\mathbb U\times\mathbb U` | No secure alternative | medium |
| D156 | 218 | L1--5, calcul barré en diagonale | `g` | `1` | low |
| D157 | 218 | L1--5, calcul barré en diagonale | `B_{g,\nu}=` | No secure alternative | medium |
| D158 | 218 | L6--8, formule (40) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D159 | 219 | L1--8, corollaire | `dirons nous` | No secure alternative | low |
| D160 | 219 | L9--14 | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D161 | 219 | L9--14 | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D162 | 219 | L15--20, théorème, avec ajouts interlinéaires | `S-groupe` | No secure alternative | low |
| D163 | 219 | L15--20, théorème, avec ajouts interlinéaires | `A_{g,\nu}^{\circ}` | `A_{g,\nu+1}^{\circ}` | low |
| D164 | 219 | L15--20, théorème, avec ajouts interlinéaires | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D165 | 219 | L15--20, théorème, avec ajouts interlinéaires | `\mathfrak S_\nu` | `\mathfrak S_{\nu+1}` | low |
| D166 | 219 | L15--20, théorème, avec ajouts interlinéaires | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D167 | 219 | L15--20, théorème, avec ajouts interlinéaires | `\Gamma_{g,\nu+1}^{!}` | No secure alternative | medium |
| D168 | 219 | L15--20, théorème, avec ajouts interlinéaires | `déduite` | No secure alternative | low |
| D169 | 220 | L9--15 | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D170 | 220 | L9--15 | `un sous-groupe` | No secure alternative | medium |
| D171 | 220 | L9--15 | `\mathfrak S_\nu` | No secure alternative | medium |
| D172 | 220 | L9--15 | `\mathfrak S_{\nu+1}` | No secure alternative | medium |
| D173 | 220 | L9--15 | `\mathfrak S_{\nu+1}` | No secure alternative | medium |
| D174 | 220 | L16--19, formule (42) | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D175 | 220 | L16--19, formule (42) | `a un sens` | No secure alternative | low |
| D176 | 220 | Marge inférieure gauche, note barrée | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D177 | 220 | Marge inférieure gauche, note barrée | Unread passage (2 estimated word(s)/symbol group(s)) | Not recovered | low |
| D178 | 220 | Marge inférieure gauche, note barrée | Unread passage (3 estimated word(s)/symbol group(s)) | Not recovered | low |
| D179 | 220 | Marge inférieure gauche, note barrée | Unread passage (1 estimated word(s)/symbol group(s)) | Not recovered | low |
| D180 | 220 | Marge inférieure gauche, note barrée | `\simeq` | No secure alternative | medium |

### Layer, attachment, and comparison doubts

These entries concern the arrangement of the page rather than a single doubtful word. They supplement the occurrence table above.

| Scan | Region | Issue retained in the transcription | Confidence |
|---|---|---|---|
| 211 | Formula (30) and cancelled lower diagram | The tiny superscript of the first numerator, the definition under the second denominator, and the connection of the small interlinear note are not fully secure. The heavily crossed diagram is not reconstructed as a clean chain of group inclusions. | low |
| 212 | Diagram (31) | The horizontal inclusion directions are more legible than the tiny labels. Some vertical hooks and the bracketed left-hand addition remain uncertain; the diagram description marks those uncertainties. | medium |
| 212 | Proof of the identity-component equality | An overwritten/interlinear `A` term is recorded separately; the exact replacement target is uncertain. | low |
| 213 | Torsor paragraph and theorem | Two stabilizer expressions and the exclusions near the theorem are additions. The scope of the inserted exclusions, especially relative to the following parenthesis about contractibility, needs checking against the image. | medium |
| 214 | Quotient preceding (35); map immediately after (35) | The written order appears reversed relative to (33) and to the neighboring exact-sequence terms. The visible order is retained rather than repaired. | high for the visible order; low for the intended correction |
| 215 | Conditions c) and d) | Extra conditions involving `(0,1)` and an intervening cancelled annotation are retained, but their revision layer is not resolved. | medium |
| 216 | Rewritten corollary and group names | The opening sentence, the compactification phrase, and the overlaid group-name insertion are among the least reliable central-text readings. No standard group model has been substituted for the ambiguous ink. | low |
| 217 | Long diagonal note | The opening sharpening and the transitivity claim are more legible than the later product decomposition and component-group formulas. The note is not assumed to precede or supersede the central argument. | low overall |
| 217 | Sphere case | `GP` and the possible `GO`/`SO` reading have not been standardized to a modern notation. In particular, the following quotient by `{±1}` is retained, not used to force a choice of preceding letters. | low for the letters; medium for the quotient |
| 219 | Theorem at the foot of the page | The inserted subgroup, its denominator, the prime, and the symmetric-group subscript are crowded together. Their exact relation to the original full-group statement remains unresolved. | low |
| 220 | Conditions following (42) | The final excluded pair is read as `(0,1)`, unlike `(0,2)` in earlier passages. This is retained as a reading issue, not diagnosed as an error by the author. | medium to high for the visible numeral |
| 220 | Bracketed outer-action paragraph | An opening bracket is visible; a corresponding closing bracket is not securely visible in this batch. None has been supplied. | medium |

## 3. Abbreviations and compact notation encountered

Expansions below are editorial suggestions only. They have not been inserted into the transcription. Entries marked doubtful occur in faint or cancelled material.

| As written / transcribed | Suggested expansion or meaning | Qualification |
|---|---|---|
| `i.e.` | *id est*, c'est-à-dire | Recurrent. |
| `tt` | tout / tous | Depends on the following noun or quantifier. |
| `\overline{\mathrm m}` | même | The short bar over a wavy letter is preserved as a mathematical glyph. |
| `resp.` | respectivement | In the comparison of ambient groups. |
| `ss-groupes`, `ss-groupe` | sous-groupes, sous-groupe | Recurrent. |
| `S-groupe` | sous-groupe | Doubtful reading in the insertion on scan 219. |
| `inv.` | invariant / invariante | Doubtful tiny labels in diagram (31); not expanded in the fragment. |
| `hom.` | homomorphisme; sometimes homomorphismes | Exact local number depends on the sentence. |
| `isom.` | isomorphe | In the homotopy-group discussion. |
| `iso` / `iso.` | isomorphisme or isomorphe | Both noun and adjective uses are possible. |
| `déf` / `déf.` | définition / défini | The cramped uses do not all have the same grammatical function. |
| `rev.` | revêtement | Used with universel and galoisien. |
| `th` | théorème | In the rewritten corollary. |
| `esp.` | espace | In the same corollary. |
| `top.` | topologique | Recurrent in the group discussion. |
| `il f. et s.` | il faut et suffit | The abbreviation itself is a low-confidence reading. |
| `cpt` | compact | Before maximal in scan 217. |
| `alg.` | algébrique | In the complex-structure paragraph. |
| `ens.` | ensemble | In the diagonal transitivity note. |
| `pt`, `pts` | point, points | The occurrence in the scan 212 margin is doubtful. |
| `p.ex.` | par exemple | In the difficult scan 212 margin. |
| `can.` | canoniquement | Before isomorphe on scan 220. |
| `ssi` | si et seulement si | Retained in that compact form. |
| `NB` | *nota bene* | Several marginal notes or reference marks. |
| `comm.` | commutatif | Doubtful reading in scan 217's partly obscured opening argument. |
| `contract.` | contractile | Low-confidence reading in deleted material on scan 215. |
| `Aut` | automorphismes | A mathematical group label, not expanded in the transcription. |
| `Aff` | transformations affines | In `Aff(1, C)`. |
| `GL` | groupe linéaire général | In `GL(1, C)`. |
| `GP` | possibly groupe projectif | The handwriting and the author's precise convention require checking. |
| `GO` / `SO` | possible orthogonal-group labels | Neither the reading nor the intended convention is settled here. |
| `dim` | dimension | No field subscript has been supplied where it is not visible. |

## 4. Legibility and limitations

The central argument is substantially more readable than the marginal material, but the pencil is faint enough that word endings, accents, very small superscripts, and the distinction between a prime and an exclamation mark cannot always be established. Crossings-out sometimes cover both the original word and a replacement. The hand also makes the symmetric-group symbol and several ordinary versus decorative capitals hard to distinguish; a mathematically familiar interpretation is not sufficient evidence for a font choice.

The weakest regions are the end of scan 211, the diagonal note on scan 212, the lower-left note on scan 213, the revised corollary on scan 216, the long diagonal addition on scan 217, the added theorem wording at the foot of scan 219, and the cancelled lower-left note on scan 220. Some of these regions remain only partially transcribed. Where a replacement's exact insertion point is not secure, the fragment retains a nearby insertion or marginal block and the table records the attachment problem; this is not a claim to have recovered the chronological order of revisions.

The relatively stronger regions are the stabilizer argument on scan 218, much of the main corollary and discussion on scan 219, and the principal displayed sequences on scan 220. Even there, the hypotheses and small superscripts must be checked before quotation or mathematical use. The uncertainty count is not an estimated error rate, and the absence of a mark is not a guarantee against a missed pale stroke.

The extract starts in the middle of an argument and ends after a comma following (43). No preceding definitions or following continuation have been supplied. The manuscript's internal assertions of familiar results are not treated here as bibliographical verification.

## 5. Research notes — separate from the transcription

These notes are in English and are based only on this batch. “Unproved claim” means that a complete justification is not supplied in these ten images; it does not mean the claim is false or absent elsewhere in the manuscript. “Own idea” and “unpursued implication” are analytical suggestions, not recovered manuscript wording, established conclusions, or claims of novelty. No securely legible explicit mathematical conjecture or open question introduced by “je conjecture” or a comparable formula was found; the clear “il me semble” on scan 219 concerns the proposed scope of the subsequent discussion.

### R01 — Scan 211, upper paragraph: transitivity beyond the base space
**Kind: unproved claim.** The phrase “plus généralement” introduces a further transitivity assertion after the action on `U_ν`. The symbol for the additional spaces is uncertain, so they should not yet be identified with a particular configuration-space functor. A proof investigation should first recover their definition and then distinguish algebraic transitivity from the topological requirements needed later for quotient bundles.

### R02 — Scans 211–212, (30)–(31): Cartesian squares and quotient comparisons
**Kind: unproved claim.** “Les deux carrés sont cartésiens” is used alongside the invariant-subgroup labels to compare quotient groups and homogeneous spaces. The extract sketches an identity-component argument, but a full verification would require the exact definitions and ambient inclusions of all the `A` and `B` groups. The exception inserted beside the horizontal inclusions must be kept in that verification rather than suppressed by a uniform normality assumption.

### R03 — Scan 212, identity-component paragraph
**Kind: unpursued implication.** The displayed equality beginning “L'égalité” links `B_{g,ν}^∘` to the indicated identity component of `A_{g,ν+1}^!`. One useful continuation would be to check separately the inclusion of subgroups, the passage to connected components, and the equality of component conventions. Those are different steps, especially because the underlying topology of `A` has not been defined within this batch.

### R04 — Scan 213, torsor paragraph
**Kind: unproved claim.** “Par extension des groupes structuraux” relates the larger-group torsors to a torsor for the stabilizer subgroup. A complete construction would need an explicit action on each fiber and a check of the topology and local triviality, not just the formal quotient identities. The uncertain presence of a circle on the stabilizer symbol is consequential and must be resolved before attempting that construction.

### R05 — Scans 213–215, (33)–(38): the proposed universal covering
**Kind: unproved claim.** The theorem asserts “est simplement connexe” and adds a contractibility assertion with exceptional-case qualifications. The next pages reduce the issue to homotopy statements about the automorphism groups and invoke a “Théorème bien connu” rather than giving a full proof of that result. A rigorous account should state the category of automorphisms, the topology, and the exact scope of every added exception before applying the long exact sequence.

### R06 — Scan 214, before and after (35)
**Kind: own idea. Confidence: high that a textual comparison is needed; no confidence claim about the intended correction.** Compare the quotient written before (35) and the map used in the following cokernel sentence with (33) and the neighboring terms of (35). The order appears to change, but it is not appropriate to reverse a map in the diplomatic text on that basis. An annotated mathematical reconstruction should retain the literal reading in one column and test possible intended diagrams in another.

### R07 — Scan 214, (36) and the following sentence
**Kind: unproved claim.** “On veut prouver” isolates bijectivity in degree one as the remaining goal. The relevant proof obligation is the vanishing of the indicated cokernel once the actual map direction is settled, not merely the already stated higher-degree isomorphisms. The deleted theorem below must not be treated as an independent completed proof of that goal.

### R08 — Scan 215, equivalent conditions
**Kind: unproved claim.** The heading “Théorème bien connu” gives no source within the page. Its equivalences connect the numerical condition, noncommutativity of the surface group, simple connectivity, and contractibility of the indicated automorphism-group component. Any proof or literature check needs to account for the inserted `(0,1)` qualifications and the cancelled intervening annotation, whose revision layer is not clear.

### R09 — Scans 216–217, the finite-dimensional group inclusion
**Kind: unproved claim.** The assertion continuing as “est une équivalence d'homotopie” concerns the inclusion of the group obtained from a complex structure into the indicated topological automorphism group. The page supplies candidate group models but not a full construction of the equivalence. A proof would need to specify what “homotopy equivalence” means for these topological groups and justify the comparison, rather than relying only on a list of homotopy groups.

### R10 — Scan 217, diagonal marginal note
**Kind: unproved claim.** “On a un résultat plus précis” introduces the minimal number `k` of additional punctures, a dimension statement, and a multiple-transitivity argument. The later product and component-group formulas are less legible than the opening claim. A reconstruction should verify whether the required action is simply transitive on the relevant tuples, since ordinary multiple transitivity alone would not supply the unique factorization apparently used later in the note.

### R11 — Scan 217, (39) and sphere paragraph
**Kind: unpursued implication.** The sphere paragraph explicitly says “n'est pas un K(π,1),” whereas the preceding cases are presented through such models. This separates the obstruction coming from higher homotopy from the calculation of the fundamental group alone. Resolving the `GP` and `GO`/`SO` readings is a prerequisite to making the compact-group comparison precise; the written quotient must not be used to silently choose the letters.

### R12 — Scan 218, (40) and the fiber comparison
**Kind: unpursued implication.** The text says the two inclusion equivalences “équivaut à celui” of the stabilizer inclusion. A fuller proof could organize the two homogeneous-space projections over the common base into a map of fibrations and check the fiber comparison, including connected components. The connectivity of the listed `G_0` groups then has a role distinct from their stronger contractibility assertions in two cases.

### R13 — Scans 218–219, the abelian-case corollary
**Kind: own idea. Confidence: high as an internal consistency test.** Use the listed stabilizers in (40) to audit the two different conclusions: the quotient projection is a homeomorphism in the stated abelian cases, but being a universal covering additionally requires the base itself to be simply connected. This provides a direct test of the exceptional pairs against the models already named in the extract. It is a proposed check of the manuscript's argument, not a replacement for the written hypotheses.

### R14 — Scan 219, paragraph beginning “Supposons donc”
**Kind: conjecture / expectation, specifically an expectation about scope, not a mathematical conjecture.** The remaining abelian cases are described as “sans intérêt pour ce qui va suivre, il me semble.” This should be checked against the continuation: it is an expressed judgment about the planned argument, not a theorem excluding those cases. The present batch does not establish whether the later argument ultimately retains that restriction.

### R15 — Scans 219–220, theorem and (41)
**Kind: unproved claim with an outlined derivation.** The theorem asserts a “suite de composition” and an extension involving `Π_{g,ν}`. A full derivation should track the full group, the group marked by an exclamation mark, and the subgroup marked by a prime as different objects. The crowded insertion at the foot of scan 219 is precisely where conflating these objects would create an unjustified exact sequence.

### R16 — Scan 220, outer-action paragraph
**Kind: unpursued implication.** “Les opérations extérieures” are identified with the action induced from the automorphism group before taking the quotient. One way to make the assertion precise is to compare conjugation in (41) with the induced fundamental-group automorphisms and then track changes of basepoint as inner automorphisms. The text asserts that compatibility but does not carry out all those identifications in this batch.

### R17 — Scan 220, (42)–(43) and adjacent note
**Kind: own idea. Confidence: high that the hypotheses require an audit; medium for the final numeral reading.** The final exclusion is read as `(0,1)`, while the earlier covering discussion excludes `(0,2)` alongside `(1,0)`; the marginal note also asserts an isomorphism in the abelian cases. Construct a case-by-case table using only the groups and stabilizers already named on scans 216–218, checking surjectivity, injectivity, and the proposed kernel separately. This would test possible readings without declaring in advance that the manuscript contains a typo.

### R18 — Scan 220, extensions (41) and (43)
**Kind: own idea. Confidence: medium.** Investigate splitting separately for the exclamation-mark extension and the prime-marked extension, after the notation and hypotheses are fixed. An outer action and an exact sequence do not themselves supply a section, so an attempted construction should explicitly track the choices of representatives fixing the extra point. This is a possible further question, not an assertion that a splitting exists, fails, or is new.
