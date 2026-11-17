# Book II planning questions: research after the transcription freeze

## Scope, sources, and evidence status

This research began only after the parent confirmed that all 43 supplied pages of cote 57, scans 226–270 excluding blank scans 232 and 247, had been transcribed, second-audited, and frozen at **2026-11-17 11:46:42 UTC**. No source image was opened, no transcription was performed, and no page, combined transcription, doubts file, or final notes file was edited by this research agent. The present report compares the frozen textual witness with the supplied context; it does not authenticate the earlier transcription against its images.

The mandatory `context/README.md` and `context/notes/RESULTS_STATE.md` were read before the comparisons and before writing this report. The RS rows **WG2 §2.4 #4**, **WG2 §2.3 #12**, and **WG H9** are explicitly unchecked planning questions or hunches; no relevant prior proof has been promoted to a reviewed result here.

| Key | Exact file | Use and status |
|---|---|---|
| P57 | `MPL_57_226-270/MPL_57_226-270_transcription.tex` | Current frozen transcription; all 43 scan sections read in this research pass. |
| CT | `context/MPL_16+47+54+44_transcription.tex` | Supplied earlier transcription; the complete mathematical text of cote 47, scans 2–11, and cote 44, scans 2–9, was read, with whole-file searches including cotes 16 and 54. It remains a provisional textual witness, not newly image-audited evidence. |
| CN | `context/MPL_16+47+54+44_notes.md` | Earlier unreviewed research claims and bibliographical leads; in particular F1–F10 and D08–D14 were read. No external source cited there was newly verified for this task. |
| CD | `context/MPL_16+47+54+44_doubts.md` | Records uncertainty in the supplied context readings; relevant 47:3–11 and 44:2–9 rows read. Its claims about prior visual audits are not independent audits by this agent. |
| SN | `context/same_cote_57/MPL_57_271-315_notes.md` | F01–F03 and J01–J07 read only as previous leads. Their assertions about scans 271–315 were not independently checked and do not establish the findings below. |
| RS | `context/notes/RESULTS_STATE.md` | Research-state and planning inventory, especially its seven planning rows. |

## Findings for the two explicit questions

**Question 1, second witness of cote 47 with compatibility checked:** no such witness is identified in the present 43-page package. This is a substantive comparison with the actual unfinished map, supported by reading all of P57 and by the searches recorded below; it is not inferred solely from absence of the word “Fourier.”

**Question 2, earlier forms of cote 44 Theorems 1–7:** none is established by the present package. P57 has ordinary Picard groups and schemes, projectivity and completion results, and reused n° 227 linear-system theorems. These give related foundations, but their objects, hypotheses, conclusions, and numbering do not match the seven-theorem programme.

Both findings are restricted to **cote 57 scans 226–270 as frozen**. They do not assert absence in the rest of cote 57, in the Montpellier archive, or in published mathematics, and they do not close WG2 §2.4 #4 globally. The current package supplies no new proof of the programme represented by WG2 §2.3 #12 and no verification or refutation of the unchecked height/positivity hunch WG H9.

## 1. What would count as completing the cote 47 check?

CT, **47:3**, defines a derived integral transform by a rigidified line bundle on an abelian scheme times a parameter scheme and claims conversion of convolution into tensor product. CT, **47:4–6**, then studies inversion by composing the transform with its transposed kernel, inserting the symmetry, cohomological shift, and determinant line. The composition kernel is supported on the anti-diagonal, conditional on Lemma 1 computing the derived direct image of the Weil line bundle.

The exact remaining comparison is visible in CT, **47:7–8**. After admitting Lemma 2, the vanishing assertion for a nontrivial algebraically trivial line bundle, 47:7 constructs

\[
\mathbf Rp_*W\longrightarrow e_*(\mathcal O_S)\otimes_S\tau_{B^*}[-n]
\]

using the top-cohomology identification

\[
R^nq_*\mathcal O_B\simeq\Lambda^nR^1q_*\mathcal O_B\simeq\Lambda^nt_{B^*}.
\]

CT, **47:8**, says that one tests the comparison on derived fibres; away from the unit the admitted vanishing lemma applies, whereas at a point of the form `e(s)` the text ends **“à faire une vérification de compatibilité.....”**. Thus a matching witness must identify the effect of this particular canonical comparison at the unit, including its degree and determinant conventions. Equality of dimensions, an abstract isomorphism between the two cohomologies, a proof of the off-unit vanishing lemma, or a general Picard base-change theorem is not itself that check.

CN, **F7–F8**, is useful precisely because it preserves this distinction. F7 is labelled an editorial proof plan, and F8 an exterior-power/Koszul calculation; F8 expressly stops short of “completing the compatibility of the actual comparison map.” These are leads from the previous run, not a second manuscript witness and not evidence that the check was already completed. SN, **F01–F02**, makes the analogous distinction for scans 271–315, but those scan claims were not used as independently established evidence.

P57, **57:250–258**, instead compares coherent cohomology and unit cohomology along infinitesimal neighbourhoods, using Grauert's theorem, the exponential sequence, Mittag–Leffler conditions, and the five lemma. In particular **57:256** says **“On en conclut, grâce au lemme des 5”** after its diagram `(D)`, and **57:258** concerns the map from the germ Picard group to the inverse limit of Picard groups. P57 contains no derived Weil-kernel comparison, no convolution construction, no anti-diagonal inversion calculation, and no zero-section compatibility computation answering 47:8. The word “Weil” at **57:230** belongs to “Weil homology” in a separate speculation about completion and topological invariants, not to the Weil/Poincaré line bundle of cote 47.

CD retains several important uncertainties in the earlier witness: category subscripts `parf|prof`, several projection subscripts, and determinant notation at 47:5–7. None needs to be resolved to identify the explicit unfinished sentence at 47:8; none licenses repairing CT or P57 in this report.

## 2. Cote 44's actual targets and the present package

CT, **44:2**, is headed **“Programme de travail”**. The dated letter at **44:8**, **“Bures le 12.8.1964”**, says **“je n'ai pas prouvé grand-chose dessus pour l'instant”** and calls the proposed objects intermediate Jacobians for algebraically trivial cycles. The printed word “Th.” in the programme therefore cannot itself be taken as proof status for every assertion, especially in view of the explicit qualifications in the letter and the supplied context's reading doubts.

| Cote 44 target | Precise comparator in CT | What P57 supplies, and what remains absent |
|---|---|---|
| Theorem 1: kernel of a parameter-family map | **44:2:** `N(ξ)⊂Alb(S)` is “en substance” the kernel of the natural map from `Alb(S)` to cycles modulo the proposed Albanese equivalence. | **57:269, 267, 265** prove finiteness of `L(D)` by induction on dimension and restriction to divisors. No parameter-family Albanese quotient, `N(ξ)`, or cycle-quotient kernel is defined. The two “Theorem 1” labels name different statements. |
| Theorem 2: uniform dimension bound | **44:2:** `dim(Alb(S)/N(ξ))≤½ b^{2i−1}(X)`; **44:8** adds a proposed Tate-module realization. | **57:269** bounds the dimension of a fixed divisor's linear system by proving it finite; **57:244**, labelled Theorem 2, concerns completeness of hypersurface systems. Neither bounds all parameter-family Albanese quotients by the odd Betti number. |
| Theorem 3: abelian variety of cycles and complementary duality | **44:2:** `Z^i_alg(X)/Z^i_alb(X)=P^i(X)` is to be an abelian variety with complementary-degree duality; **44:8** explicitly names the endpoints `J^1=Pic^0` and `J^n=Alb^0`. | P57's Picard schemes, e.g. **57:239–245**, are related degree-one foundations; **57:263** uses the ordinary Jacobian of a curve in a base-point argument. There is no construction of the all-codimension cycle quotient, no stated universal property identifying it, and no complementary-degree duality. Do not identify the whole `Pic(X_n)` with the connected endpoint `Pic^0`. |
| Theorem 4: positivity of the middle self-duality | **44:2:** for `n=2m−1`, the canonical self-duality is to arise from a polarization; **44:8–9** formulates a divisor correspondence and ends “A prouver que cette dernière est positive !”. | **57:260**, Corollary 1.8, and **57:266**, Corollary 2.2, lift an already ample line bundle to establish projectivity. They do not prove that a specified symmetric correspondence on a higher Jacobian is ample. This leaves the relevant part of **WG H9** unchanged. |
| Theorem 5: Néron–Tate height/intersection formula | **44:4:** for restrictions to a generic hyperplane-pencil member, `⟨ζ,ζ′⟩=(-1)^m Z·Z′`, with a fibration/local-variant margin. | **57:263** uses a pencil and a curve Jacobian, but proves a base-point assertion. **57:228, 241, 262** invoke Néron's finiteness theorem for the Picard ML argument. No height pairing, height normalization, intersection identity, vertical correction, or Hodge-index reduction is supplied. |
| Theorem 6: hyperplane restriction and fixed factor | **44:4:** three dimension ranges for `P^i(X)→P^i(Y)`, including a critical fixed-factor assertion; some layers are deleted or uncertain. | P57's stabilized images in **57:227, 237–245, 258, 264** are images under restriction to infinitesimal thickenings. The hypersurface systems in **57:244** likewise do not state the higher-Jacobian hyperplane restriction or fixed-factor theorem. Stable images in a thickening tower and the fixed part of a pencil family require different comparisons. |
| Theorem 7: numerical and tau equivalence | **44:6:** “L'équivalence numérique = τ-équivalence”; scope and the meaning of tau need care, as CN D14 notes. | P57 has Néron–Severi stabilization and torsion conditions on transition kernels/cokernels, but no definition or equality of numerical and tau equivalence on cycles. None of the n° 227 statements supplies that comparison even at the divisor level. |

### The n° 227 numbering is internal to a different typescript

The current frozen text gives these independent identifiers:

| P57 scan | Internal page and heading | Actual numbered statement |
|---|---|---|
| **57:269** | n° 227, p. 10, “2. Systèmes linéaires”; “Addition au chapeau : On suppose V complète.” | **Theorem 1:** for a divisor `D` on complete `V`, `L(D)` is finite-dimensional over `k`. Its proof continues on internal pp. 11–12, at **57:267, 265**. |
| **57:244** | n° 227, p. 15 | **Theorem 2:** the displayed pole condition gives `φ=g/f` with `g∈I_n`; for normal `V`, high-degree hypersurface systems are complete. The draft deletes the definition of `I` as the integral closure, so that local textual issue should not be silently filled in. |
| **57:263** | n° 227, p. 44 | **Theorem 3:** a pencil of genus at least one has no base point simple on `V`. The proof embeds its parameter curve `C` in its Jacobian and cites “le théorème 6 de VA.” |

The theorem number 3 and the word “Jacobienne” in 57:263 do not identify this with CT 44:2, Theorem 3. In the current page the Jacobian is the ordinary Jacobian of the curve `C` already appearing as the target of `f:V→C`; no higher-dimensional variety's codimension-`i` cycle group is being represented. Its reference to “théorème 6 de VA” is a citation in that reused typescript, not an identified reference to the programme's Theorem 6.

The word “pencil” is also insufficient to identify 57:263 with CT 44:4, Theorem 5. The current argument uses its positive-genus parameter curve and an extension/base-point obstruction; CT studies restrictions of cycles to the generic hyperplane-section fibre and a Néron–Tate pairing. WG H9's unchecked formulation explicitly puts its Lefschetz pencil over `P^1`, which further shows why the genus condition in the reused theorem must not be transferred to it.

### Chronology and exact reading limits

P57 **57:227** explicitly dates the Hironaka letter **July 6, 1962**; CT **44:8** explicitly dates the Serre letter **12.8.1964**. The former therefore predates the latter as a dated document, but its analytic/formal Picard completion theorem is not an earlier textual form of the seven-theorem cycle programme. The n° 227 sheets and the current Picard notes do not acquire a date for each textual layer from adjacency to that letter; no historical priority claim for those layers is established here.

The duality index in CT **44:2**, Theorem 3, remains `n−i|n+1−i` in CT/CD, although the letter at **44:8** independently writes `n+1−i`. Likewise CT/CD record uncertainty in the pairing indices and hypotheses of **44:4**. The comparison above identifies the programmes without silently resolving those diplomatic readings.

## 3. Proposed short notes for the parent to adapt

The prose of each proposed note is one to four sentences. Metadata and search terms are separate. These are documentary comparisons of the frozen text, not new mathematical proofs.

### B01 — The Fourier compatibility check has no second witness here

**Kind:** unpursued implication.  
**Current file/scans:** P57, **57:250–258**, especially 256.  
**Current quote:** “On en conclut, grâce au lemme des 5”.  
**Bears on:** **WG2 §2.4 #4** (unchecked plan).  
**Context searched:** CT **47:3–11**, CN **F3–F8**, CD **47:5–8**; whole P57.  
**Searches:** S01, S03, S06, S07; `Fourier`, `Pontryagin`, `convolution`, `compatib`, `faisceau de Weil`, `Module de Weil`, `anti-diagonale`, `mapping-cylindres`.

The five-lemma argument at 57:256 compares exponential-sequence cohomology with completion, whereas CT 47:7–8 constructs the specific derived Weil-kernel map and leaves its unit-fibre test at “à faire une vérification de compatibilité.....”. None of the 43 current pages supplies that map or its missing check, so this package gives no identified second witness answering WG2 §2.4 #4. CN F7–F8 supplies only an unreviewed proof plan and an exterior-power calculation that expressly leaves the actual-map compatibility unfinished.

### B02 — Reused Theorems 1–2 belong to linear systems

**Kind:** unpursued implication.  
**Current file/scans:** P57, **57:269, 267, 265, 244**.  
**Current quotes:** “L(D) est de dimension finie sur k”; “le système d'hypersurfaces de degré n est complet”.  
**Bears on:** **WG2 §2.4 #4; WG2 §2.3 #12** (unchecked plans).  
**Context searched:** CT **44:2, 8**, CN **D08–D10**, CD **44:2**; whole P57.  
**Searches:** S02–S05, S06; `THÉORÈME`, `Systèmes linéaires`, `Albanese`, `Alb`, `N(\xi)`, `Betti`, `b^{2i-1}`, `L(D)`, `hypersurfaces`.

The reused n° 227 sheets label finiteness of a fixed divisor's `L(D)` as Theorem 1 and completeness of high-degree hypersurface systems as Theorem 2. CT 44:2 instead labels an Albanese-to-cycle-quotient kernel assertion and a uniform half-Betti-number bound as Theorems 1–2. The explicit objects and conclusions differ, so the repeated numbers do not establish earlier versions of the programme; CN D08–D10 remains an unreviewed lead about the additional universal-property and dimension arguments it would require.

### B03 — The ordinary curve Jacobian does not supply the higher-cycle theorem

**Kind:** unpursued implication.  
**Current file/scan:** P57, **57:263**, n° 227, internal p. 44.  
**Current quote:** “On peut supposer que C est plongée dans sa Jacobienne.”  
**Bears on:** **WG2 §2.4 #4; WG2 §2.3 #12**, and **WG H9** only as a boundary.  
**Context searched:** CT **44:2, 4, 8–9**, CN **D08, D12**, CD **44:2, 4**; whole P57.  
**Searches:** S02–S06; `Jacob`, `pencil`, `pinceau`, `P^i`, `J^i`, `Z^i`, `Néron`, `Tate`, `hauteur`, `Lefschetz`.

Theorem 3 on 57:263 concerns base points of a positive-genus pencil and uses the ordinary Jacobian of its curve `C`, followed by a citation to “théorème 6 de VA.” CT 44:2, Theorem 3 instead proposes abelian varieties of higher-codimension cycles and their complementary duality, while CT 44:8 identifies ordinary Picard and Albanese varieties only as endpoints. Nor does the shared word “pencil” yield CT 44:4's height/intersection formula: the current base-point proof contains no pairing of restricted cycles or sign calculation. Consequently this reused sheet supplies neither an earlier form of the higher-cycle theorem nor evidence settling WG H9.

### B04 — Lifting ampleness differs from proving the programme's positivity

**Kind:** unpursued implication.  
**Current file/scans:** P57, **57:260, 266**, with **57:228, 241, 262** for the Néron reference.  
**Current quote:** “Ce dernier est ample en vertu de EGA III.”  
**Bears on:** **WG H9; WG2 §2.3 #12; WG2 §2.4 #4** (unchecked hunch/plans).  
**Context searched:** CT **44:2, 4, 8–9**, CN **D12–D13**, CD **44:4, 8**; whole P57.  
**Searches:** S02, S04, S06, S09; `ample`, `polarisation`, `Hodge`, `Néron`, `hauteur`, `intersection`, `fibrations`, `positive`.

The argument at 57:266 starts from an ample line bundle on an infinitesimal thickening, lifts its fibre class through stable Picard images, and invokes EGA III for ampleness on `X`. CT 44:2 and 44:8–9 instead ask whether a particular middle-Jacobian self-duality is a polarization, ending “A prouver que cette dernière est positive !”. Néron's finiteness theorem at 57:228, 241 and 262 serves the Picard stabilization argument and does not supply CT 44:4's Néron–Tate height/intersection identity. Thus neither the positivity assertion nor the height-based reduction conjectured in WG H9 is verified by this package.

### B05 — A dated precursor in subject is not an earlier version of the seven theorems

**Kind:** unpursued implication.  
**Current file/scan:** P57, **57:227**.  
**Current quote:** “Neuilly July 6 1962”.  
**Bears on:** **WG2 §2.4 #4**, chronology only.  
**Context searched:** CT **44:2, 8–9**, CN's cote-44 programme/letter notes, CD **44:8**.  
**Searches:** S08; `1962`, `1964`, `July 6`, `Bures le`, `Programme de travail`.

The Hironaka letter dated July 6, 1962 on 57:227 predates the Serre letter dated August 12, 1964 in CT 44:8. Their explicit statements differ: the current letter concerns Picard completion and projectivity, while the later letter discusses higher-cycle Jacobians and positivity. This establishes chronology for those two dated documents, but neither an earlier version of Theorems 1–7 nor dates for every adjacent undated or reused sheet.

## 4. Search procedure and negative-result boundaries

The commands below were rerun for this record after the initial exploratory searches. Each command is preserved exactly, with exit status, line-numbered output, and nearest cote/scan for transcription matches; exit status 1 means no match, not a tool failure. Searches cover the named files only, with neither archive-wide nor external-literature retrieval. All 43 P57 scan sections were also read continuously, so absence conclusions were checked against content rather than word matches alone.

The broad vocabulary searches deliberately return some irrelevant matches, including `\node` drawing code, unrelated reused theorems, and the word “Weil” in “Weil homology.” Such matches are not counted as Fourier, higher-Jacobian, or height evidence. Exact-symbol queries are supplements only, because different TeX encodings can conceal the same mathematical notation; the continuous reading supplies the substantive safeguard.

No claim made only in CN or SN is adopted as a reviewed mathematical result. No outside theorem or publication mentioned by those notes is cited as newly verified here. The current conclusions use P57 and the supplied provisional CT statements, with CD's doubts retained.

## 5. Exact search record

Recorded UTC: 2026-11-17T11:53:39.739318+00:00

### S01 — Fourier-specific vocabulary across present and context transcriptions

```bash
rg -n -i 'Fourier|Pontryagin|convolution|compatib|Poincar|faisceau de Weil|Module de Weil|anti-diagonale|mapping-cylindres' MPL_57_226-270/MPL_57_226-270_transcription.tex context/MPL_16+47+54+44_transcription.tex
```

Exit status: 0.

```text
context/MPL_16+47+54+44_transcription.tex:1053:\uline{Condition de Poincaré}
context/MPL_16+47+54+44_transcription.tex:1143:compatible avec $\chi',Q$ [on dira que $\widetilde W,\widetilde Q$ est une \uline{extension} de la forme $\chi'$]
context/MPL_16+47+54+44_transcription.tex:2078:Produit de \unsure{convolution}\\
context/MPL_16+47+54+44_transcription.tex:2081:de Fourier sur\\
context/MPL_16+47+54+44_transcription.tex:2101:Alors $\varphi_{\mathcal L}$ transforme produit de Pontryagin $*$ en\\
context/MPL_16+47+54+44_transcription.tex:2147:faisceau de Weil sur $A\times_S B$. Alors l'hypothèse sur $\mathcal L$\\
context/MPL_16+47+54+44_transcription.tex:2249:en \deleted{\unsure{couple}} produit de Convolution.
context/MPL_16+47+54+44_transcription.tex:2289:($W_B$ le Module de Weil sur $B\times_S B^*$), d'où
context/MPL_16+47+54+44_transcription.tex:2297:faisceau de Weil sur $B^{\unsure{*}}\times_S B^{\deleted{\unsure{*}}}$, $p:B^*\times_S B^{\deleted{\unsure{*}}}\mathbin{-}B^*$ la\\
context/MPL_16+47+54+44_transcription.tex:2327:$\varphi:A\simeq C^*$, et \deleted{\unsure{donc}} par suite $K$ est l'\uline{anti-diagonale}\\
context/MPL_16+47+54+44_transcription.tex:2388:isomorphisme (histoire de mapping-cylindres\ldots).\\
context/MPL_16+47+54+44_transcription.tex:2393:compatibilité.....
context/MPL_16+47+54+44_transcription.tex:2416:compatible avec
```

Matched transcription locations: CT 16:25; CT 16:27; CT 47:2; CT 47:3; CT 47:5; CT 47:6; CT 47:8.

### S02 — Seven-theorem programme vocabulary across present and context transcriptions

```bash
rg -n -i 'Albanese|\bAlb\b|intermédiaire|Betti|Néron|\bTate\b|Hodge|polarisation|pencil|pinceau|Lefschetz|numérique|THÉORÈME [1-7]|Th\. [1-7]' MPL_57_226-270/MPL_57_226-270_transcription.tex context/MPL_16+47+54+44_transcription.tex
```

Exit status: 0.

```text
MPL_57_226-270/MPL_57_226-270_transcription.tex:37:(i bis) In the inverse system $(\underline{\operatorname{Pic}}_{X_n/\underline{C}})_{n\ \underline{N}}$ of analytic groups, the system of the ``Néron-Sévéri groups'' is constant for $n$ large, whereas for $m>n$ and $n$ large, the Kernel and Cokernel of
MPL_57_226-270/MPL_57_226-270_transcription.tex:59:In the case of a \uline{formal} scheme propr over a complete noeth. local ring with residue field of \uline{caracteristic} 0, the analogon of the previous theorem (reducing to statements (i), (i bis)) \deleted{\unsure{(iii))|(iii)}} hold true, and I wrote a purely algebraic proof of this, relying only on the fact that the Kernel and Cokernel of $\underline{\operatorname{Pic}}_{X_{n+1}}\qquad\underline{\operatorname{Pic}}_{X_n}$ are without torsion, and Néron's finiteness theorem; in particular, the analogon of corollary 1 holds true in this case. These results break down of course in car. $>0$.
MPL_57_226-270/MPL_57_226-270_transcription.tex:335:Le fait que les $\underline{\operatorname{Pic}}_{X_{n+1}/k}\longrightarrow\underline{\operatorname{Pic}}_{X_n/k}$ sont de type fini, \deleted{et} les noyaux \deleted{sans torsion} unipotents, les conoyaux sans torsion, se voit par la \unsure{théorie|thèse} de Oort \deleted{\unsure{et}} \deleted{des obstructions} [cf suite ex. de cohomologie]. De plus, on utilise le th. \inserted{\figure{\begin{tikzpicture}[baseline=-.5ex]\draw (0,0) ellipse (.9 and .28);\node at (0,0) {de finitude};\draw (-.65,-.2)..controls(-.4,-.35)and(-.65,-.4)..(-.45,-.5);\end{tikzpicture}}} de Néron \deleted{\unsure{Séveri}} pour $\underline{\operatorname{Pic}}_{X_0/k}$.
MPL_57_226-270/MPL_57_226-270_transcription.tex:413:THÉORÈME 2. - \uline{Si} $\varphi$ \uline{est une fonction telle que} $(\varphi)\geq-Z(f)$ \uline{pour} $f\in R_n$, \uline{alors il existe} $g\in I_n$ \uline{tel que} $\varphi=g/f$. \uline{Si} $V$ \uline{est normale, alors le système d'hypersurfaces de degré} $n$ \uline{est complet pour tout} $n$ \uline{suffisamment grand}. (Voir la prop.11 de IAG, ch.IV).
MPL_57_226-270/MPL_57_226-270_transcription.tex:773:\uline{Remarque} 1.11. Sur les \unsure{variantes} analytique-formelle et algébrique formelle du th. envisagé. Il y a pour cette dernière une démonstration purement algébrique, utilisant \uline{Pic}, \deleted{\unsure{et}}\inserted{et} th. de finitude de Néron.
MPL_57_226-270/MPL_57_226-270_transcription.tex:782:Soit $\unsure{\mathcal P|\mathcal S}$ un pencil. Un point $P'$ de $V$ est un \uline{point de base de} $\unsure{\mathcal P|\mathcal S}$ si $P'\in|X|$ pour tout $X\in\unsure{\mathcal P|\mathcal S}$.
MPL_57_226-270/MPL_57_226-270_transcription.tex:784:THÉORÈME 3. -- \uline{Soit} $\unsure{\mathcal P|\mathcal S}$ \uline{un pencil de genre} $\geq1$. \uline{Alors} $\unsure{\mathcal P|\mathcal S}$ \uline{n'a pas de points de base qui soit simple sur} $V$.
MPL_57_226-270/MPL_57_226-270_transcription.tex:786:\uline{Dém}. On va se servir d'un peu de variétés abéliennes ; Soit $k$ un corps de rationalité pour $V$, $\unsure{\mathcal P|\mathcal S}$ et $P'$, et soit $f:V\longrightarrow C$ la fonction définissant $\unsure{\mathcal P|\mathcal S}$. Soit $Q$ un point générique de $C/k$ et $P$ un point générique de $V$ tel que $f(P)=Q$. Alors on voit que $P'$ est une spécialisation de $P$ sur $k(Q)$, parce que $P'$ est un point dans le cycle premier rationnel ayant $P$ comme point générique sur $k(Q)$. Mais $P'$ étant rationnel sur $k$, on voit que la fonction $f$ ne peut être définie en $P'$. On peut supposer que $C$ est plongée dans sa Jacobienne. Ceci contredit le théorème 6 de VA.
MPL_57_226-270/MPL_57_226-270_transcription.tex:907:THÉORÈME 1. -- \uline{Soit} $V$ \uline{complète}. \uline{Si} $D$ \uline{est un diviseur sur} $V$, \uline{alors} $L(D)$ \uline{est de dimension finie sur} $k$.
MPL_57_226-270/MPL_57_226-270_transcription.tex:929:Or en vertu du th. 2.1. (iii) on a $\operatorname{Pic}(\widetilde X)\overset{\sim}{\longleftarrow}\operatorname{Pic}(X)$, d'où la conclusion voulue.
context/MPL_16+47+54+44_transcription.tex:589:(i) L'\unsure{endom} $L$ de $M^*$ satisfait la condition de \deleted{Hard} Lefschetz et l'opérateur $\Lambda$ associé est dans $\mathcal E$.
context/MPL_16+47+54+44_transcription.tex:694:8) Soit maintenant $\mathcal E^*$ un anneau gradué, \deleted{muni de} tel qu'il existe $L\in\mathcal E^{(2)}$ satisfaisant aux \uline{conditions de Lefschetz} (\deleted{de} les conditions du corollaire du n\textsuperscript{o} précédent). On dit que $\mathcal E^*$ est un ``anneau \deleted{d'opérateurs Lefschetzien,}\inserted{de correspondances Lefschetzien}'' (\unsure{cette} \deleted{\illegible{3}} \deleted{\unsure{avec le système}} \unsure{au n\textsuperscript{o}} \unsure{(pair)} \unsure{qu'un système de|qui un système de} Lefschetz), et $L$ un de ses ``éléments de Lefschetz''.
context/MPL_16+47+54+44_transcription.tex:696:L'élt $\Lambda$ associé est \deleted{\unsure{dit}} \unsure{``}l'élément \deleted{\unsure{adjoint pour}} \deleted{\unsure{anti}}\inserted{co.}Lefschetzien'' associé à $L$.
context/MPL_16+47+54+44_transcription.tex:699:\node[align=left,text width=3.8cm,rotate=25] at (0,0) {un n\textsuperscript{o} : ``principe de dualité'' pour les anneaux de correspondances Lefschetziens.};
context/MPL_16+47+54+44_transcription.tex:704:On peut se demander de \uline{caractériser} les \deleted{les} éléments de Lefschetz $L$. Une condition nécessaire, lorsque le \unsure{nombre} $2n$ n'est pas redondant, i.e.
context/MPL_16+47+54+44_transcription.tex:864:on trouve une suite exacte canonique \inserted{(où $Z_\ell[1]=\varprojlim_\nu\deleted{Z}\mu_{\ell^\nu}$ est le faisceau $\ell$-adique de TATE)}:
context/MPL_16+47+54+44_transcription.tex:886:en supposant maintenant que $\operatorname{Pic}(X)$ est extension d'un groupe de type fini $\operatorname{NS}(X)$ (le \uline{groupe de Néron--Sévéri}) par un groupe divisible, et que $H^2(X,\uline Z/\ell\uline Z)$ est fini. \deleted{\unsure{x}}On trouve en passant le fait, classique dans la théorie transcendante, que \deleted{le}\inserted{\figure{\begin{tikzpicture}
context/MPL_16+47+54+44_transcription.tex:900:\inserted{(pour un $L_0$ de Lefschetz fixé)}
context/MPL_16+47+54+44_transcription.tex:904:Or.\,--- où, si $L'$ est un autre élément Lefschetzien
context/MPL_16+47+54+44_transcription.tex:916:L^{\unsure{\prime|*}}\ \text{Lefschetzien}\arrow[r,Rightarrow]\&L^n\ \text{\uline{une base de}}\ \mathcal E^{2n}
context/MPL_16+47+54+44_transcription.tex:926:Mais ça ne marche pas non plus pour les endom. associés aux élémts de degré $2$ d'une alg. de Lefschetz, pour la dim $6$
context/MPL_16+47+54+44_transcription.tex:941:\node[anchor=west,align=left,text width=5.1cm] at(.4,.75){$L$ est Lefschetzien,\\$L'$ ne l'est pas, bien que\\$L'^3=L^3$ !};
context/MPL_16+47+54+44_transcription.tex:979:\begin{flushright}\fbox{Algèbres de Hodge d'ordre 2}\end{flushright}
context/MPL_16+47+54+44_transcription.tex:1044:\uline{Condition de Lefschetz}
context/MPL_16+47+54+44_transcription.tex:1183:[27] Tate, J., \uline{Cohomology of abelian varieties over p-adic fields}, (Cf. Notes by S. Lang, Princeton University, May, 1959.)
context/MPL_16+47+54+44_transcription.tex:1215:To treat the case $r=3$, Th. 1 shows that we may assume $A$ is the field $k$. By Th. 4 and the duality theorem used above,
context/MPL_16+47+54+44_transcription.tex:1219:However, the right hand group vanishes by results of Tate [27], and the proof is complete.
context/MPL_16+47+54+44_transcription.tex:1221:One may obtain additional information concerning the cohomology groups with coefficients in $\underset{\sim}{G}_m$ by combining Th. 6 with results of Berkson, and Rosenberg-Zelinsky [5, 21]. Let $k$ be a field, and let $K$ be a purely inseparable extension of $k$. Let $\bigotimes^rK$ denote the $k$-algebra obtained by forming the tensor product of $K$ with itself (over $k$) $r$-times. The face operators
context/MPL_16+47+54+44_transcription.tex:1239:\begin{flushright}Algèbres de Hodge\end{flushright}
context/MPL_16+47+54+44_transcription.tex:1723:I think the best will be to state the index conjecture right after the statement of the main results of Hodge theory, adding that this conjecture will take its whole significance only when coupled with ``conj.A'' in the next paragraph. This will give more freedom in the next paragraph to express some extra relationships between various conjectures, such as $A+\text{index}$ implies $B$.
context/MPL_16+47+54+44_transcription.tex:1725:In c\inserted{h}ar. zero, state some known extra features: index theorem holds, the \deleted{conjectures}\inserted{propositions} $A_{\unsure{\ell|\chi}}$ to $D_{\unsure{\ell|\chi}}$ are independant of $\unsure{\ell|\chi}$ (because of the existence of Betti cohomology, so that these \deleted{conjectures}\inserted{propositions} are equivalent to the corresponding one's for rational cohomology), \deleted{and} $A$ and $C$ are independant of the choosen polarization$_{\mathrm{x}}$ (for $A$ because it is equivalent with $B$, for $C$ because it can be expressed in terms of $A$, $C(X)=(A(X\mathrm{x}X)+A(Y\mathrm{x}Y)+\mathinner{..})$ Thus the \deleted{conjectures}\inserted{conditions} without ambiguity can be called $A(X)$ to $D(X)$, without \deleted{index}\inserted{subscript} $\unsure{\ell|\chi}$ and without indication of polarization. Say too that it is known that $C(X)$ is of finite dimension over $\uline{Q}$, \inserted{(}\unsure{so} that $A$ can also be expressed in terms of an equality of dimensions of $C^i$ and $C^{n-\unsure{i|1}}$\deleted{)}, which again proves it is independant of \hspace{1em}), bu that this is not known in car $p>0$. Contrarily to what I hastily stated in my talk (influenced from my recollections of the car $0$ case) it is not clear to me if in car $p>0$ the \deleted{conjectures}\inserted{conditions} \deleted{$\unsure{A(X)}$} $A_{\unsure{\ell|\chi}}(X,\inserted{\xi})$ and $C_{\unsure{\ell|\chi}}(X,\inserted{\unsure{\xi}})$ are independant of the polarization $\inserted{\xi}$ ; if you do not find some proof of this independance, then the possible dependance should be pointed out, as well as the fact that \deleted{\unsure{a} priori} we do not have a proof that $A$ to $D$ are independant of $\unsure{\ell|\chi}$. Of cour-
context/MPL_16+47+54+44_transcription.tex:1787:By the way, the fact that the $\pi_1$ for a surface are algebraic was pointed out (Tate tells me) by Hodge in Algebraic correspondances between surfaces, Proc. London Math. \unsure{Soc.} Seeies 2, Vol XLIV, 1938, p.226. It is rather striking that this statement should not have struck the algebraic geometers more, and has fallen into oblivion for \inserted{nearly} thirty years !
context/MPL_16+47+54+44_transcription.tex:1791:Thus the main problems arise already for 1-cycles on threefolds, and partially even in car.0 . Urged by Kleimann's question, I \unsure{wihl|will} look again at my old scribbles on that subject (when I pretend to reduce the ``strong'' form of Lefschetz to the ``week'' one). As for the suggestion I made on the phone, to try to get any $X$ as \unsure{biratmonally|birationally} equivalent to a non singular $X'$, which is a spcialisation of a non singular $X''$, itself birationally equivalent to a non singular hypersurface -- this cannot work as Serre pointed out, because such an $X$ would have to be simply connected ! Thus if one wants to reduce somehow to the case of hypersurfaces, one will have to work also with singular ones, and see how to reformulate for singular varieties the standard conjectures \ldots
context/MPL_16+47+54+44_transcription.tex:1829:As a consequence, we see that if $x\in H^i(X)$ is such that $u(x)$ is algebraic ($i$ being now assumed to be even), then so is $x$. The same result should hold in fact if $u$ is a monomorphism, the reason being that in this case there should exist a left-inverse which is algebraic; this exists indeed in a case like $H^{n-1}(X)\to H^{n-1}(Y)$ (where we take the left inverse $\Lambda_X\phi_*$). But to get \unsure{it} in general, it seems we need moreover the Hodge index relation. (The complete yoga then being that we have the category of motives which is semi-simple !). Without speeking of motives, and staying down on earth, it would be nice to explain in the notes that $C(X)$ together with the index relation $I(X\times X)$ implies that the ring of correspondance classes for $X$ is semi-simple, and how one deduces from this the existence \unsure{of|an} left and right inverses as looked for above.
context/MPL_16+47+54+44_transcription.tex:1912:Définir la différente de Dedekind par la trace, et montrer qu'elle coïncide avec celle de Kähler quand $A$ et $B$ sont des anneaux de valuation discrète (il s'agit du gros th. 3 du n° 7, § 2, avec son dévissage, -- éventuellement agrémenté des lemmes du n° 6 s'ils n'ont pas été faits dans un chapitre antérieur pour illustrer la notion d'intersection complète. En tous cas on aura dit que si $A$ et $B$ sont réguliers, $A\to B$ est une intersection complète relative. La prop. 11 sera éclairée par le lemme suivant :
context/MPL_16+47+54+44_transcription.tex:1972:Dans le b) du th. 1, ajouter
context/MPL_16+47+54+44_transcription.tex:2614:\qquad \text{\unsure{Ch.|Coh.} de Hodge-DeRham}
context/MPL_16+47+54+44_transcription.tex:2787:\uline{Th. 1} $N(\unsure{\xi|\zeta})\subset\operatorname{Alb}(S)$ n'est autre\deleted{\unsure{des|donc}}\inserted{\figure{\begin{tikzpicture}\node[draw,rounded corners=9pt,inner sep=3pt](n){en substance};\draw(n.south west)--++(.45,-.02)--++(.04,-.25);\end{tikzpicture}}} que le noyau de l'application naturelle
context/MPL_16+47+54+44_transcription.tex:2789:\varphi_\xi:\operatorname{Alb}(S)\arrow[r]\&\unsure{\mathcal{Z}|Z}^{i}(X)/\unsure{\mathcal{Z}|Z}^{i}_{\mathrm{\unsure{alb|ab}}}(X)
context/MPL_16+47+54+44_transcription.tex:2793:Th. 2 La dimension de $\operatorname{Alb}(S)/N(\xi)=P_\xi$ est majorée par un nb ne dépendant que de $X$ [en fait, par $\frac12 b^{2i-1}(X)$ !]
context/MPL_16+47+54+44_transcription.tex:2798:\uline{Th. 3}
context/MPL_16+47+54+44_transcription.tex:2799:$Z^i_{\mathrm{alg}}(X)/\unsure{\mathcal{Z}|Z}^{i}_{\mathrm{\unsure{alb|ab}}}(X)=\unsure{P}^{i}(X)$ a une structure naturelle de V.A., et $P^i(X)$ et $P^{\unsure{n-i|n+1-i}}(X)$ sont en dualité canonique.
context/MPL_16+47+54+44_transcription.tex:2802:\margin{\figure{\begin{tikzpicture}\node[draw,ellipse,align=center,inner sep=4pt](n){Connu\\tel\\quel};\draw[->](n.south east)--++(.35,-.2);\end{tikzpicture}}\uline{Hodge}}
context/MPL_16+47+54+44_transcription.tex:2803:\uline{Th. 4} Si $n=2m-1$, alors l'autodualité canonique de $P^m(X)$ [\unsure{donc la corr. sur} $\uline{P}^{m}(X)$] est \unsure{associé|associée} à une \uline{polarisation} de $P^m(X)$
context/MPL_16+47+54+44_transcription.tex:2849:\margin{\uline{``Néron''}}
context/MPL_16+47+54+44_transcription.tex:2850:\uline{Th. 5} Soit $X$ Variété projective n.s. de dim $n$
context/MPL_16+47+54+44_transcription.tex:2859:\node[draw,rounded corners=10pt,align=left,inner sep=3pt](n){générique d'un pinceau dont \deleted{\unsure{toutes}} les\\fibres sont géom. intègres...};
context/MPL_16+47+54+44_transcription.tex:2862:donc \deleted{\unsure{sont des}}\inserted{définissent des} éléments de $P^{\unsure{i}}(Y),P^{\unsure{j|0}}(Y)$ et par la forme de Néron--Tate [définie grâce à l'isomorphisme entre $P^{\unsure{i}}(Y)$ et $P^{\unsure{j|0}}(Y)$] on \deleted{alors} définit $\langle\zeta,\zeta'\rangle$. Ceci posé, on a \deleted{[au signe près ??]}
context/MPL_16+47+54+44_transcription.tex:2868:\node[draw,ellipse,rotate=28,align=left,inner sep=6pt]{\uline{N.B.} Sauf\\si $2i=2j=n$\\les deux mbres\\sont nuls\\par Lefschetz \unsure{au|en}\\\unsure{sens général|sens géométrique}};
context/MPL_16+47+54+44_transcription.tex:2876:\deleted{\uline{Cor.}}\inserted{\uline{Th. 6}}
context/MPL_16+47+54+44_transcription.tex:2886:\margin{\uline{``Lefschetz''}\figure{\begin{tikzpicture}\draw(0,0)--(0,3.6);\draw(.12,3.9)--(.12,4.7)--(.36,4.7);\end{tikzpicture}}}
context/MPL_16+47+54+44_transcription.tex:2944:\uline{Th. 7} L'équivalence numérique $=$ $\tau$-équivalence [cycles algébriques sur $X$ projective non singulière].
context/MPL_16+47+54+44_transcription.tex:2974:Je commence à avoir de faibles lumières sur la façon de faire \inserted{d}es VA avec les cycles al\inserted{g}ébriquement équivalents à zéro d'une variété projective non singulière $X$ (sur un corps alg clos $k$). Si $X$ est connexe de dimension $n$, je sais associer à chaque entier $i$ \inserted{c}ompris entre $\unsure{0|1}$ et $n$ une VA $J^i(X)$, jouant le rôle d'une ``jacobienne intermédiaire'' au sens de Weil, correspondant à des classes de cycles de codimension $i$ (pour une relation d'équivalence que je ne sais pas bien identifier pour l'instant, mais qui mérite certainement d'être appelée ``équivalence d'Albanese''). Je suis moralement sûr que ce sont ``les bonnes'', bien que je n'ai pas prouvé grand-chose dessus pour l'instant; par contre, j'ai des conjectures en pagaille. Je te signale seulement que $J^1=\operatorname{Pic}^{0}$ et $J^n=\operatorname{Alb}^{0}$, que $J^i$ et $J^{n+1-i}$ sont canoniquement duales l'une de l'autre, que $\dim J^i\leq\frac12 b_{2i-1}$ (nombre de Betti) -- de façon plus précise $T_{\ell}(J^i)$ est un quotient d'un sous-module de $H^{2i-1}(X,\uline{Z}_{\ell}(i))$ (et quand on sera plus savant, on saura prouver que c'est même un sous-module dudit), en caractéristique $0$ on peut également remplacer la cohomologie de Weil par la cohomologie de Hodge $H^i(X,\uline{\Omega}^{i-1}_X)$ ...
context/MPL_16+47+54+44_transcription.tex:2977:\margin{\deleted{$H^{\unsure{1|i}}(J^i)\simeq$ \unsure{Alg. de Hodge}}}
context/MPL_16+47+54+44_transcription.tex:2979:Moyennant un certain nombre de choses non prouvées (qui risquent d'ailleurs d'être vaches) le théorème de positivité de Hodge se ramène à l'énoncé suivant, que je ne sais pas prouver, et que j'ai envie de te communiquer car il est bien terre à terre. Moralement, il s'agit de prouver que dans le cas où $\dim X=2m-1$, l'autodualité de $J^m$ (qui s'exprime par une classe de correspondance divisorielle sur $J^m\mathbin{x}J^m$ \deleted{anti} \uline{symétrique}, donc provenant -- du moins modulo le facteur 2--
context/MPL_16+47+54+44_transcription.tex:2989:d'un élément du groupe de Néron Severi de $J^m$) est \uline{positive} i.e. l'élément en question de Néron--Severi est ample, i.e. une polarisation.
context/MPL_16+47+54+44_transcription.tex:2995:qui est une classe de diviseurs sur $T\mathbin{x}T$, que nous considérons comme une classe de correspondance divisorielle sur $T\mathbin{x}T$. Si $A=\operatorname{Alb}^0(T)$ (NB si tu veux, tu peux supposer $T=A$ et $a$ l'origine), elle provient donc d'une classe de correspondance sur $A\mathbin{x}A$, évidemment symétrique. Soit $N$ le ``noyau'' de cette classe (i.e. le noyau de $A\longrightarrow(\text{duale de }A)$ qu'elle définit), on obtient alors une classe de correspondance symétrique sur $J\mathbin{x}J$, où $J=A/N$. A prouver que cette dernière est \uline{positive} ! Je me demande si les spécialistes ``abéliens'' pourraient avoir une idée sur une telle question, peut-être Matsusaka ? Ou toi-même ? Notes d'ailleurs que cette question te dévoile pratiquement la méthode de construction des $J^i$ généraux; Si tu veux, tu peux te borner \inserted{aussi} au cas où tu disposes d'une sous-variété de codimension $m-1$ $Y$ de $X$, non singulière si tu y tiens, \deleted{\unsure{tu|xx}} et où $T=\operatorname{Pic}^0(Y)$, considéré comme paramétrant les diviseurs alg équiv à zéro de $Y$, mais considérés comme classes de cycles \deleted{dans} de codimension $m$ de $X$.
```

Matched transcription locations: P57 57:227; P57 57:228; P57 57:241; P57 57:244; P57 57:262; P57 57:263; P57 57:269; P57 57:270; CT 16:15; CT 16:18; CT 16:21; CT 16:22; CT 16:25; CT 16:28; CT 16:30; CT 16:31; CT 16:44; CT 16:47; CT 16:49; CT 16:52; CT 16:54; CT 54:3; CT 44:2; CT 44:4; CT 44:6; CT 44:8; CT 44:9.

### S03 — Literal programme symbols

```bash
rg -n -F -e 'P^i' -e 'J^i' -e 'Z^i' -e 'N(\xi)' -e 'N(\unsure' -e 'b^{2i-1}' -e 'Z\mathbin{.}Z' MPL_57_226-270/MPL_57_226-270_transcription.tex context/MPL_16+47+54+44_transcription.tex
```

Exit status: 0.

```text
context/MPL_16+47+54+44_transcription.tex:298:M^i&\simeq P^i+LP^{i-2}+L^2P^{i-4}\quad\text{---}\\
context/MPL_16+47+54+44_transcription.tex:299:M^{2n-i}&\simeq L^{n-i}P^i+L^{n-i+1}P^{i-2}\quad\text{---}
context/MPL_16+47+54+44_transcription.tex:1249:$X$ variété projective lisse connexe polarisée par $\xi_X\in H^2(X)$, $L_X$ opération de cup-produit associée, $\Lambda_X$ opération de degré $-2$ correspondante, $p_i^X$ les projections de $H^*(X)$ sur les morceaux primitifs $P^i(X)$ pour $0\leq i\leq2n$, $Y$ une section hyperplane lisse de $X$, $\xi_Y\in H^2(Y)$ la self-intersection (induite par $\xi_X$), d'où $L_Y$, $\Lambda_Y$, $p_Y^i$; $\phi:Y\to X$ l'immersion, d'où $\phi^*$ et $\phi_*$.
context/MPL_16+47+54+44_transcription.tex:1321:P^i(X)&\xrightarrow{\sim}P^i(Y) &&\text{si }i\leq n-2\\
context/MPL_16+47+54+44_transcription.tex:1323:P^i(X)&=\operatorname{Ker}\varphi^i &&\text{si }i\geq n
context/MPL_16+47+54+44_transcription.tex:1341:H^*(X)&=\deleted{\unsure{\sum_i}}\coprod_{\substack{i+j\leq n\\i,j\geq0}}L_X^jP^i(X)
context/MPL_16+47+54+44_transcription.tex:1342:=\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_X^jP^i(X)\oplus\coprod_{j\geq n}P^j(X)\\
context/MPL_16+47+54+44_transcription.tex:1343:H^*(Y)&=\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_Y^jP^i(Y).
context/MPL_16+47+54+44_transcription.tex:1348:\deleted{\unsure{=}}\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_X^jP^i(X)
context/MPL_16+47+54+44_transcription.tex:1349:\longrightarrow H^*(Y)=\unsure{\coprod}_{\substack{i+j\leq n-1\\i,j\geq0}}L_Y^jP^i(Y);\]
context/MPL_16+47+54+44_transcription.tex:1355:\[\deleted{\unsure{\sum}}\coprod_{j\geq n}P^i(X)\]
context/MPL_16+47+54+44_transcription.tex:1396:(\unsure{\alpha})\qquad H^*(Y)=\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_X^jP^i(X)\oplus E^{n-1}.
context/MPL_16+47+54+44_transcription.tex:1401:\[\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_X^j\unsure{P^j|P^i}(X)\]
context/MPL_16+47+54+44_transcription.tex:1406:\deleted{qui correspond \unsure{par l'isom can.} à $\displaystyle\sum_{\unsure{n-1\leq i\leq2(n-1)}}P^i(Y)$}. Ainsi on trouve le
context/MPL_16+47+54+44_transcription.tex:1467:\coprod_{\substack{i+j\leq n-2\\i,j\geq0}}L_X^jP^i(X),
context/MPL_16+47+54+44_transcription.tex:1471:\coprod_{\substack{\deleted{\unsure{i+j}}\\i+j=n-1\\i,j\geq0}}\uline{L_X^jP^i(X)}\oplus E^{(n-1)}
context/MPL_16+47+54+44_transcription.tex:1474:(qui n'est d'ailleurs autre que $\displaystyle\coprod_{\substack{\deleted{\unsure{i\geq n}}\\n\leq i\leq2(n-1)}}P^i(Y)$, comme il se doit). L'opération $\Lambda_Y$ est nulle sur $E^{n-1}$, et coïncide sur le morceau
context/MPL_16+47+54+44_transcription.tex:1475:\[\coprod_{\substack{i+j\leq n-1\\i,j\geq0}}L_X^jP^i(X)\]
context/MPL_16+47+54+44_transcription.tex:1478:\coprod_{\unsure{0\leq i\leq n-1}}P^i(X)+E^{n-1}=\coprod_{0\leq i\leq\unsure{n+1|n-1}}P^i(Y),
context/MPL_16+47+54+44_transcription.tex:1482:=\coprod_{\substack{i+j\leq n-2\\\deleted{i\geq0,j>0}\\i,j\geq0}}L_X^{1+j}P^i(X).
context/MPL_16+47+54+44_transcription.tex:1492:Pour la \deleted{dernière}\inserted{\unsure{prem.}} relation, on la vérifie d'abord sur les $P^j(X)$ \inserted{$=$} pour $j\geq n$, \inserted{i.e. les $L_X^{n-i}P^i(X)$ pour $i\leq n-1$)} \deleted{le premier est} \unsure{y est nul} car $\varphi^*$ l'est, le deuxième
context/MPL_16+47+54+44_transcription.tex:1575:Soit $p_X^{i,j}$ les projections sur $L_X^jP^i(X)$ $(i+j\leq n,\ i,j\geq0)$.
context/MPL_16+47+54+44_transcription.tex:1869:Alors $A$ contient $L$\unsure{!}, \deleted{les $\unsure{\pi}$} et les projections sur les facteurs \unsure{élémentaires} $\unsure{\xi^j|\xi_j}P^i$ ($i\leq n$, et \deleted{et $i+2j\leq n$ \unsure{ou} $i+2j\leq 2n-i$ \unsure{ou}} $j\leq n-i$)
context/MPL_16+47+54+44_transcription.tex:1875:(ii) pour tt $1\leq i\unsure{<|\leq}n$, il existe une corr. \uline{alg} induisant $H^{2n-i}(X)\mathrel{-}H^i(X)$ inverse de $\unsure{J^i|\xi^i}$.
context/MPL_16+47+54+44_transcription.tex:1879:\uline{Dém du lemme.}\quad Comme $A$ stable par transposition, il suffit de regarder les $\unsure{\xi^j|\xi_j}P^i$, pour $i+2j\leq n$. Soit $k=i+2j$. -- procéder par récurrence sur $k$, trivial si $k<0$.
context/MPL_16+47+54+44_transcription.tex:1938:D'autre part, si $i+2j=k$, \inserted{$j>0$,} la projection sur $\xi^jP^i$ est aussi $\in A$, comme on voit \deleted{\unsure{ainsi}} par récurrence ascendante sur $i$ (donc descendante sur $j$) ainsi : si $i<0$ rien à prouver. Si c'est fait pour les $i'<i$, on forme $\xi^{n-k+j}T_k$, \deleted{$\unsure{\xi}$} qui induit zéro sur $H^\alpha$ pour $\alpha\neq k$, et induit
context/MPL_16+47+54+44_transcription.tex:1998:$\xi^j u_{k-2j}\xi^{\unsure{n-k+j|n-k-j}}T_k$ n'est autre que la projection de $H^k$ sur $\xi^jH^{k-2j}$, somme des $\xi^{j'}\unsure{p^{i'}|P^{i'}}$ pour $i'+2j'=k$, $j'\geq j$ ; \deleted{\unsure{de}} comme la projection \deleted{sur} partielle sur $\xi^{j'}\unsure{p^{i'}|P^{i'}}$, $j'>j$, est $\in A$, il en est de $=$ de la projection sur $\xi^j\unsure{P^i|p^i}$, par différence.
context/MPL_16+47+54+44_transcription.tex:2787:\uline{Th. 1} $N(\unsure{\xi|\zeta})\subset\operatorname{Alb}(S)$ n'est autre\deleted{\unsure{des|donc}}\inserted{\figure{\begin{tikzpicture}\node[draw,rounded corners=9pt,inner sep=3pt](n){en substance};\draw(n.south west)--++(.45,-.02)--++(.04,-.25);\end{tikzpicture}}} que le noyau de l'application naturelle
context/MPL_16+47+54+44_transcription.tex:2793:Th. 2 La dimension de $\operatorname{Alb}(S)/N(\xi)=P_\xi$ est majorée par un nb ne dépendant que de $X$ [en fait, par $\frac12 b^{2i-1}(X)$ !]
context/MPL_16+47+54+44_transcription.tex:2799:$Z^i_{\mathrm{alg}}(X)/\unsure{\mathcal{Z}|Z}^{i}_{\mathrm{\unsure{alb|ab}}}(X)=\unsure{P}^{i}(X)$ a une structure naturelle de V.A., et $P^i(X)$ et $P^{\unsure{n-i|n+1-i}}(X)$ sont en dualité canonique.
context/MPL_16+47+54+44_transcription.tex:2851:\deleted{\unsure{même}}, $Z^i,Z'{}^j\in\mathcal Z^*(X)$
context/MPL_16+47+54+44_transcription.tex:2864:\langle\zeta,\zeta'\rangle=(-1)^m Z\mathbin{.}Z'
context/MPL_16+47+54+44_transcription.tex:2878:Si $2i\leq n-1$ $P^i(X)\mathbin{-}P^i(Y)$ est un \uline{isomorphisme}; \deleted{\unsure{et}} \uline{si $2i=n$}
context/MPL_16+47+54+44_transcription.tex:2879:Le \uline{facteur fixe} de $P^i(Y)$ est identique à l'image de $P^i(X)$;
context/MPL_16+47+54+44_transcription.tex:2880:\deleted{\unsure{Et} [\unsure{est égale à} $P^i(X)$]}
context/MPL_16+47+54+44_transcription.tex:2883:\deleted{Le noyau de $P^i(X)\mathbin{-}P^i(Y)$ est fini}
context/MPL_16+47+54+44_transcription.tex:2884:[Si \deleted{$\unsure{\leq}$} $2i\geq n+1$, $P^i(X)\mathbin{-}P^i(Y)$ est \inserted{\deleted{$2i\leq n+1$}\uline{surjectif}}]
context/MPL_16+47+54+44_transcription.tex:2974:Je commence à avoir de faibles lumières sur la façon de faire \inserted{d}es VA avec les cycles al\inserted{g}ébriquement équivalents à zéro d'une variété projective non singulière $X$ (sur un corps alg clos $k$). Si $X$ est connexe de dimension $n$, je sais associer à chaque entier $i$ \inserted{c}ompris entre $\unsure{0|1}$ et $n$ une VA $J^i(X)$, jouant le rôle d'une ``jacobienne intermédiaire'' au sens de Weil, correspondant à des classes de cycles de codimension $i$ (pour une relation d'équivalence que je ne sais pas bien identifier pour l'instant, mais qui mérite certainement d'être appelée ``équivalence d'Albanese''). Je suis moralement sûr que ce sont ``les bonnes'', bien que je n'ai pas prouvé grand-chose dessus pour l'instant; par contre, j'ai des conjectures en pagaille. Je te signale seulement que $J^1=\operatorname{Pic}^{0}$ et $J^n=\operatorname{Alb}^{0}$, que $J^i$ et $J^{n+1-i}$ sont canoniquement duales l'une de l'autre, que $\dim J^i\leq\frac12 b_{2i-1}$ (nombre de Betti) -- de façon plus précise $T_{\ell}(J^i)$ est un quotient d'un sous-module de $H^{2i-1}(X,\uline{Z}_{\ell}(i))$ (et quand on sera plus savant, on saura prouver que c'est même un sous-module dudit), en caractéristique $0$ on peut également remplacer la cohomologie de Weil par la cohomologie de Hodge $H^i(X,\uline{\Omega}^{i-1}_X)$ ...
context/MPL_16+47+54+44_transcription.tex:2976:\margin{conjecturalement $\uline{t}_{J^i}\unsure{\subset|\in}H^{\unsure{i}}(X,\uline{\Omega}^{i-1}_X)$}
context/MPL_16+47+54+44_transcription.tex:2977:\margin{\deleted{$H^{\unsure{1|i}}(J^i)\simeq$ \unsure{Alg. de Hodge}}}
context/MPL_16+47+54+44_transcription.tex:2995:qui est une classe de diviseurs sur $T\mathbin{x}T$, que nous considérons comme une classe de correspondance divisorielle sur $T\mathbin{x}T$. Si $A=\operatorname{Alb}^0(T)$ (NB si tu veux, tu peux supposer $T=A$ et $a$ l'origine), elle provient donc d'une classe de correspondance sur $A\mathbin{x}A$, évidemment symétrique. Soit $N$ le ``noyau'' de cette classe (i.e. le noyau de $A\longrightarrow(\text{duale de }A)$ qu'elle définit), on obtient alors une classe de correspondance symétrique sur $J\mathbin{x}J$, où $J=A/N$. A prouver que cette dernière est \uline{positive} ! Je me demande si les spécialistes ``abéliens'' pourraient avoir une idée sur une telle question, peut-être Matsusaka ? Ou toi-même ? Notes d'ailleurs que cette question te dévoile pratiquement la méthode de construction des $J^i$ généraux; Si tu veux, tu peux te borner \inserted{aussi} au cas où tu disposes d'une sous-variété de codimension $m-1$ $Y$ de $X$, non singulière si tu y tiens, \deleted{\unsure{tu|xx}} et où $T=\operatorname{Pic}^0(Y)$, considéré comme paramétrant les diviseurs alg équiv à zéro de $Y$, mais considérés comme classes de cycles \deleted{dans} de codimension $m$ de $X$.
```

Matched transcription locations: CT 16:9; CT 16:33; CT 16:34; CT 16:36; CT 16:38; CT 16:40; CT 16:51; CT 16:53; CT 16:55; CT 44:2; CT 44:4; CT 44:8; CT 44:9.

### S04 — Current stabilization, finite generation, and potential height terminology

```bash
rg -n -i 'Néron|numérique|tau|\bTate\b|Hodge|polar|hauteur|fixed|fixe|engendrement|torsion' MPL_57_226-270/MPL_57_226-270_transcription.tex
```

Exit status: 0.

```text
37:(i bis) In the inverse system $(\underline{\operatorname{Pic}}_{X_n/\underline{C}})_{n\ \underline{N}}$ of analytic groups, the system of the ``Néron-Sévéri groups'' is constant for $n$ large, whereas for $m>n$ and $n$ large, the Kernel and Cokernel of
59:In the case of a \uline{formal} scheme propr over a complete noeth. local ring with residue field of \uline{caracteristic} 0, the analogon of the previous theorem (reducing to statements (i), (i bis)) \deleted{\unsure{(iii))|(iii)}} hold true, and I wrote a purely algebraic proof of this, relying only on the fact that the Kernel and Cokernel of $\underline{\operatorname{Pic}}_{X_{n+1}}\qquad\underline{\operatorname{Pic}}_{X_n}$ are without torsion, and Néron's finiteness theorem; in particular, the analogon of corollary 1 holds true in this case. These results break down of course in car. $>0$.
121:\margin{(Donc si $H/H^0$ est \unsure{à engendrement} fini, il en est de $=$ de $G/G^0$)}
129:\deleted{\uline{Corollaire}} \inserted{\figure{\begin{tikzpicture}[baseline=-.5ex]\draw (0,0) ellipse (.42 and .34);\node at (0,0) {(iii)};\end{tikzpicture}}} Supposons \inserted{$\operatorname{Ker}\varphi$ soit connexe et} que $\operatorname{Coker}\varphi$ soit ``\unsure{géom\textsuperscript{t}} sans torsion''. Alors $\underline{\pi}_0(\varphi)$ est injectif et $\operatorname{Coker}\underline{\pi}_0(\varphi)$ est sans torsion.
133:Dém\inserted{de (iii)}. Grâce à \unsure{(ii)} précédent, on est ramené au cas où $\varphi$ est une imm fermée, et où $G$ est \unsure{discret géom.} Mais alors $\operatorname{Coker}\varphi$ contient $H^0/G\cap H^0$ où $G\cap H^0\simeq\operatorname{Ker}\underline{\pi}_0(\varphi)$. Si ce \unsure{quotient} est sans torsion, il faut que, ou bien
174:a) $\operatorname{car}k>0$, \deleted{\unsure{alors} $H^0$ fini} \inserted{et} $H^0$ \deleted{\unsure{est}} réduit à un pt; alors $G\cap H^0=\{e\}$ i.e. $\underline{\pi}_0(\varphi)$ est injectif, et du pt de vue géométrique \unsure{ensembliste} on a $\varphi=\underline{\pi}_0(\varphi)$ donc $\operatorname{Coker}\underline{\pi}_0(\varphi)$ est sans torsion
183:qui \unsure{splitte} du pt de vue géométrique ensembliste (car $\unsure{H^0_{\bar{k}}|H^0}$ est divisible). Comme $H/G$ est sans torsion, il en est donc de $=$ de $\operatorname{Coker}\underline{\pi}_0(\varphi)$.
187:\inserted{a) \deleted{\unsure{Si}} $G_0/G_0^0$ est à engendrement fini}
191:\deleted{\unsure{ait}}\inserted{\figure{\begin{tikzpicture}[baseline=-.5ex]\node[draw,rounded corners=10pt,inner sep=3pt] at (0,0) {est de type fini et};\draw (-.7,-.25)..controls(-.65,-.3)and(-.55,-.3)..(-.5,-.45);\end{tikzpicture}}} a un noyau connexe, et un conoyau qui est géométriquement \uline{sans} torsion.
193:\inserted{b) pour $\forall n$, $\underline{\pi}_0(G_n)$ est à engendrement fini.}
201:des points fixes.
203:PROPOSITION 1. - \uline{Soit $\mathcal{L}$ un système linéaire sans composante fixe, et $T$ l'application rationnelle associée. Soit $P'$ un point normal de $V$. Alors $T$ est définie en $P'$ si et seulement si $P'$ n'est pas un point de base.}
207:Soit $\mathcal{L}$ un système linéaire sans composante fixe, et $T:V\longrightarrow V'$ l'application rationnelle induite par $\mathcal{L}$. On va voir que $T$ applique les diviseurs de $\mathcal{L}$ sur les \inserted{\unsure{sections}} \unsure{hyperplans|hyperplanes} de $V'$ de la manière suivante. Prenons $X\in\mathcal{L}$, $P'\in|X|$ et supposons que $P'$ ne soit pas un point de base pour $\mathcal{L}$. Prenons un diviseur $X_0\in\mathcal{L}$ tel que $P'\notin|X_0|$. Soit $L_0$ l'espace dérivé de $\mathcal{L}$ par $X_0$ et $f_0,\ldots,f_n$ une base de $L_0$. Alors chaque fonction $f\in L_0$ peut être écrite
213:Un système linéaire sera dit \uline{ample} \inserted{s'il est sans \unsure{com.|comp.} fixe et} si l'application rationnelle $T$ induite par $\mathcal{L}$ est un isomorphisme de $V$ sur $V'$. Si $D$ est un diviseur tel que $\mathcal{L}(D)$ soit ample, alors $D$ est dit \uline{ample}. Le système des
225:(iii) \deleted{P\unsure{our} \illegible{3}} \deleted{(\unsure{s.c.} \unsure{est nulle})} $\exists n_0$ tq \deleted{et conoyau} que \unsure{pour|$\forall$} $m\geq n\geq n_0$, le \unsure{conoyau|noyau} de $G_m\longrightarrow G_n$ soit un groupe vectoriel \deleted{sans torsion (donc} en car $=0$, et \deleted{\unsure{purement}} radiciel en car. $>0$.
335:Le fait que les $\underline{\operatorname{Pic}}_{X_{n+1}/k}\longrightarrow\underline{\operatorname{Pic}}_{X_n/k}$ sont de type fini, \deleted{et} les noyaux \deleted{sans torsion} unipotents, les conoyaux sans torsion, se voit par la \unsure{théorie|thèse} de Oort \deleted{\unsure{et}} \deleted{des obstructions} [cf suite ex. de cohomologie]. De plus, on utilise le th. \inserted{\figure{\begin{tikzpicture}[baseline=-.5ex]\draw (0,0) ellipse (.9 and .28);\node at (0,0) {de finitude};\draw (-.65,-.2)..controls(-.4,-.35)and(-.65,-.4)..(-.45,-.5);\end{tikzpicture}}} de Néron \deleted{\unsure{Séveri}} pour $\underline{\operatorname{Pic}}_{X_0/k}$.
361:Si on employait un module $L_1$ dérivé de $\mathcal L$ par un autre diviseur $X_1$, on voit que l'application rationnelle $T_1$ obtenue comme ci-dessus diffère de $T$ par une transformation \deleted{linéaire}\inserted{projective}. On peut donc dire que $T$ est uniquement déterminée par $\mathcal L$. De plus, si $\mathcal L$ et $\mathcal L'$ soit deux systèmes linéaires qui ne diffèrent que par une composante fixe, alors on voit immédiatement qu'ils donnent lieu à la même application rationnelle $T$ de $V$, les modules dérivés étant les mêmes. Pour étudier l'application rationnelle associée à un système linéaire, on peut donc se borner, sans perte de généralité, aux systèmes linéaires \unsure{sans'|sans} composantes fixes.
369:Un point $P$ de $V$ est dit un \uline{point de base} du système linéaire $\mathcal L$ si $P\in\inserted{\unsure{\checkmark|\gamma}}|X|$ pour tout $X\in\mathcal L$. Si $Y$ est une composante fixe de $\mathcal L$, alors tous les points de $|Y|$ sont des points de base. Il peut très bien arriver qu'un système linéaire n'ait pas de composante fixe, mais ait
380:\deleted{\uline{Lemme} Sous les conditions du corollaire [car. 0 \unsure{essentielle}, mais non la \unsure{propreté}], le conoyau de $\operatorname{Pic}(X_m)\unsure{\text{---}|\longrightarrow}\operatorname{Pic}(X_n)$ (pour $m\geq n$) est sans torsion.}
409:Si $f_0\in R_m$, alors l'ensemble des fonctions $f/f_0$, $f\in R_m$ est un module $L_0$, et le sup des diviseurs polaires de ces fonctions est exactement $Z(f_0)$. L'ensemble des diviseurs $Z(f)$ où $f$ parcourt $R_n$ est un système linéaire, définit par le module $L_0$. On voit aussi qu'il n'a pas de composantes fixes.
538:constant. En effet (\unsure{cf} ?) $H^i(X_n,\mathbb Z)=\unsure{H^i}(X_0,\mathbb Z)$ est un groupe de type fini, et son quotient par $\operatorname{Ker}\alpha^i$ est sans torsion [car isom à un sous-groupe de $H^i(X,\mathcal O_{X_n})$, qui est un vectoriel sur $\mathbb C$], \deleted{\unsure{d'où}} il suffit donc de noter que pour $n$ grand, le rang du dit quotient est constant.
755:g) \uline{Dérivées partielles}. On suppose maintenant que $E=K^n$ ; soit $x_0=(x_1^0,\ldots,x_n^0)\in E$. La fonction $f:U\to F$ peut donc être considérée comme une fonction $f(x_1,\ldots,x_n)$ de $n$ variables scalaires, à valeurs dans $F$, définie lorsque les $x_i$ sont assez voisins des $x_i^0$. Si on laisse les $x_j$ fixes, égaux à $x_j^0$, pour tout $j\neq i$, on obtient une fonction de la seule variable $x_i$, définie au voisinage de $x_i^0$.
773:\uline{Remarque} 1.11. Sur les \unsure{variantes} analytique-formelle et algébrique formelle du th. envisagé. Il y a pour cette dernière une démonstration purement algébrique, utilisant \uline{Pic}, \deleted{\unsure{et}}\inserted{et} th. de finitude de Néron.
```

Matched transcription locations: P57 57:227; P57 57:228; P57 57:233; P57 57:235; P57 57:236; P57 57:237; P57 57:241; P57 57:242; P57 57:243; P57 57:244; P57 57:254; P57 57:261; P57 57:262.

### S05 — Reused numbered statements and their document identifiers

```bash
rg -n -i 'n.*227|THÉORÈME|Systèmes linéaires|Jacob|pencil|simple sur|Addition au chapeau|L\(D\)|hypersurfaces' MPL_57_226-270/MPL_57_226-270_transcription.tex
```

Exit status: 0.

```text
8:\scanpage{227}
199:\margin{n\textsuperscript{o} 227}
355:-- \mspage{16} -- \hfill n° 227
361:Si on employait un module $L_1$ dérivé de $\mathcal L$ par un autre diviseur $X_1$, on voit que l'application rationnelle $T_1$ obtenue comme ci-dessus diffère de $T$ par une transformation \deleted{linéaire}\inserted{projective}. On peut donc dire que $T$ est uniquement déterminée par $\mathcal L$. De plus, si $\mathcal L$ et $\mathcal L'$ soit deux systèmes linéaires qui ne diffèrent que par une composante fixe, alors on voit immédiatement qu'ils donnent lieu à la même application rationnelle $T$ de $V$, les modules dérivés étant les mêmes. Pour étudier l'application rationnelle associée à un système linéaire, on peut donc se borner, sans perte de généralité, aux systèmes linéaires \unsure{sans'|sans} composantes fixes.
401:-- \mspage{15} -- \hfill n° 227
403:linéaire, le système des hypersurfaces de degré donné sur une variété projective.
411:Le système linéaire complet dérivé du système d'hypersurface de degré $n$ est caractérisé algébriquement par le théorème suivant (Zariski, th.1 de \unsure{HS|ES}, démonstration facile et élémentaire ) :
413:THÉORÈME 2. - \uline{Si} $\varphi$ \uline{est une fonction telle que} $(\varphi)\geq-Z(f)$ \uline{pour} $f\in R_n$, \uline{alors il existe} $g\in I_n$ \uline{tel que} $\varphi=g/f$. \uline{Si} $V$ \uline{est normale, alors le système d'hypersurfaces de degré} $n$ \uline{est complet pour tout} $n$ \uline{suffisamment grand}. (Voir la prop.11 de IAG, ch.IV).
451:\S\ 1 Un théorème de géométrie analytique.
695:2) La ramification dans les corps locaux (rédaction tirée en noir à Paris). Apporter le n° 363, (démonstration du théorème de Hasse-Arf).
753:f). \uline{Théorème des fonctions implicites}. Les notations étant celles de b), on suppose que $E$ et $F$ sont \uline{normés} et \uline{complets} (ce qui est toujours le cas lorsque $E$ et $F$ sont de dimension finie, cf. EVT, chap. I, § 2), que $f$ est \uline{strictement dérivable} au point $x_0$, et que $f'(x_0):E\longrightarrow F$ est un \uline{isomorphisme} d'espaces vectoriels topologiques. Soit $y_0=f(x_0)$. Il existe alors $^{(3)}$ une application $g$ d'un voisinage de $y_0$ dans $E$, strictement dérivable en $y_0$, prenant la valeur $x_0$ en ce point, et telle que $g\circ f=1_E$ (resp. $f\circ g=1_F$) au voisinage de $x_0$ (resp. de $y_0$).$^{(4)}$
779:\margin{n° 227}
782:Soit $\unsure{\mathcal P|\mathcal S}$ un pencil. Un point $P'$ de $V$ est un \uline{point de base de} $\unsure{\mathcal P|\mathcal S}$ si $P'\in|X|$ pour tout $X\in\unsure{\mathcal P|\mathcal S}$.
784:THÉORÈME 3. -- \uline{Soit} $\unsure{\mathcal P|\mathcal S}$ \uline{un pencil de genre} $\geq1$. \uline{Alors} $\unsure{\mathcal P|\mathcal S}$ \uline{n'a pas de points de base qui soit simple sur} $V$.
786:\uline{Dém}. On va se servir d'un peu de variétés abéliennes ; Soit $k$ un corps de rationalité pour $V$, $\unsure{\mathcal P|\mathcal S}$ et $P'$, et soit $f:V\longrightarrow C$ la fonction définissant $\unsure{\mathcal P|\mathcal S}$. Soit $Q$ un point générique de $C/k$ et $P$ un point générique de $V$ tel que $f(P)=Q$. Alors on voit que $P'$ est une spécialisation de $P$ sur $k(Q)$, parce que $P'$ est un point dans le cycle premier rationnel ayant $P$ comme point générique sur $k(Q)$. Mais $P'$ étant rationnel sur $k$, on voit que la fonction $f$ ne peut être définie en $P'$. On peut supposer que $C$ est plongée dans sa Jacobienne. Ceci contredit le théorème 6 de VA.
825:\margin{n° 227}
828:Revenons à la démonstration du théorème. Sachant que $L(0)=k$, il suffit de montrer que si le théorème est vrai pour un diviseur positif $D$, alors pour tout diviseur premier $W$, $L(D+W)$ est de dimension finie.
830:Supposons que $W$ apparaisse avec la multiplicité $n$ dans $D$, i.e. $D=nW+\ldots$. S'il n'y a pas de fonction $f\in L(D+W)$ ayant un pôle d'ordre $n+1$ sur $W$, alors $L(D+W)=L(D)$, et nous avons fini. Autrement, supposons qu'il existe une fonction $f$ dans $L(D+W)$ ayant un pôle d'ordre $n+1$ sur $W$. Considérons l'espace vectoriel $f^{-1}L(D+W)$, formé de tous les produits $f^{-1}g$, avec $g\in L(D+W)$. Il est évidemment égal à $L(D+W+(f))$. Aucune des fonctions de cet espace n'a de pôle sur $W$. Par conséquent chacune de ces fonctions induit une fonction sur $W$, et on a un homomorphisme $h\longrightarrow h'$ où $h\in L(D+W+(f))$, et $h'$ est la fonction induite sur $W$. Le lemme, et l'hypothèse d'induction, montrent que l'image de notre homomorphisme est de dimension finie.
832:Si une fonction $f^{-1}g$ induit la constante $0$ sur $W$, alors $f^{-1}g$ a un zéro sur $W$, et $g$ a donc un pôle d'ordre au plus $n$ sur $W$. Mais $g$ étant dans $L(D+W)$, on voit que $g$ est même dans $L(D)$. Le noyau de notre homomorphisme est donc précisément l'espace $L(D)$, qui est
856:\margin{n° 227}
857:$n$ sur $Q$. Mais $z-aw$ est dans $L(D+Q)$, donc dans $L(D)$. Ceci contredit l'indépendence linéaire de $z$ et $w$ mod $L(D)$.
859:Supposons maintenant le théorème démontré pour toutes les variétés de dimension $<r$. On va procéder par induction. Faisons d'abord quelques remarques. Soit $z$ une fonction sur $V$, et $W$ un diviseur premier de $V$. Alors $W$ n'est pas nécessairement normale. Soit $P'$ un point générique de $W$. Alors la spécialisation $P\longrightarrow P'$ induit une place du corps $k(P)$. Si la fonction $z$ n'a pas de pôle sur $W$, elle est dans l'anneau de valuation de cette place et est définie sur $W$. Son image $z'$ dans le corps $k(P')$ définit une fonction sur $W$. La normalisation $W^*$ de $W$ ayant le même corps de fonction que $W$, on peut dire que si $z$ n'a pas de pôle sur $W$, alors $z$ induit sur $W$ ou sur $W^*$ une fonction $z'$. C'est de cette fonction qu'il s'agira dans le lemme suivant.
861:LEMME. -- \uline{Soit} $D$ \uline{un diviseur sur} $V$, \uline{et} $W$ \uline{un diviseur premier de} $V$, \uline{non contenu dans les composantes polaires de} $D$. \uline{Alors il existe un diviseur} $D^*$ \uline{sur la normalisation} $W^*$ \uline{de} $W$ \uline{tel que pour une fonction} $z\in L(D)$, \uline{la fonction induite} $z'$ \uline{sur} $W^*$ \uline{soit dans} $L(D^*)$.
863:\uline{Dém}. Soit $V_i$, $i=1,\ldots,g$ les représentants de $V$. On peut supposer que tous les $V_i$ sont des variétés affines. D'après un théorème d'approximation élémentaire, il existe une fonction $f_i\in K$ telle que pour $z\in L(D)$, la fonction $f_i z$ n'ait pas de pôle ayant un représentant sur $V_i$, et telle que $f_i$ soit une unité sur $W$.
900:\margin{n° 227}
901:2. \uline{Systèmes linéaires}.
903:\uline{Addition au chapeau} : \uline{On suppose} $V$ \uline{complète}.
905:Soit $D$ un diviseur sur $V$. Les fonctions $z$ telles que $(z)\geq-D$ forment évidemment un espace vectoriel sur $k$, qui sera noté $L(D)$. Si $D_1\geq D_2$, on a $L(D_1)\supset L(D_2)$. La dimension de $L(D)$ sur $k$ sera notée $\ell(D)$. Le théorème qui suit montre que cette dimension est finie si $V$ est complète. Remarquons qu'en tout cas, $L(0)=k$, d'après § 1, prop.7.
907:THÉORÈME 1. -- \uline{Soit} $V$ \uline{complète}. \uline{Si} $D$ \uline{est un diviseur sur} $V$, \uline{alors} $L(D)$ \uline{est de dimension finie sur} $k$.
909:\uline{Dém}. La démonstration se fera par induction sur la dimension $r$ de $V$. Remarquons qu'il suffit de démontrer le théorème pour les diviseurs positifs. On peut aussi supposer $V$ normale, car on peut identifier les diviseurs sur $V$ et sur $V^*$.
911:Soit $V$ une courbe. Dans ce cas, l'absence de singularités de dimension $0$ implique que $V$ est normale. Les diviseurs premiers s'identifient aux points de $V$. Il suffit de montrer que si le théorème est vrai pour un diviseur $D$, il l'est aussi pour $D+Q$, où $Q$ est un point sur $V$. En fait, on démontrera que $\ell(D+Q)\leq\ell(D)+1$. (On part de $D=0$). Supposons qu'il existe deux fonctions $z$ et $w\in L(D+Q)$ qui sont linéairement indépendantes mod $L(D)$. Soit $n$ la multiplicité de $Q$ dans $D$. Puisque $z$ et $w$ ne sont pas dans $L(D)$, ces fonctions doivent avoir un pôle d'ordre $n+1$ sur $Q$, et par conséquent, $zw^{-1}$ est une unité à $Q$. Sous la place induite par $Q$ sur le corps de fonctions, $zw^{-1}$ prend une valeur constante $a\in k$. Alors $zw^{-1}-a$ possède un zéro sur $Q$ et $w(zw^{-1}-a)=z-aw$ un pôle d'ordre au plus
```

Matched transcription locations: P57 57:227; P57 57:236; P57 57:242; P57 57:244; P57 57:248; P57 57:259; P57 57:261; P57 57:263; P57 57:265; P57 57:267; P57 57:269.

### S06 — Earlier notes: named leads and explicit incompleteness

```bash
rg -n -i '### F[3-8] |### D0[89]|### D1[0-4]|vérification de compatibilité|cohomology dimensions|completing the compatibility|universal property|height normalization|does not establish|does not itself|Programme de travail|Bures le' context/MPL_16+47+54+44_notes.md
```

Exit status: 0.

```text
439:**Location:** cote 16, scan 15, matrix units and universal property.
903:**Editorial confidence:** medium. The data are explicit but the manuscript does not establish all equivalences or characteristic restrictions here.
911:The “to appear” entry for Shatz can help identify the provenance and approximate preparation date of this isolated bibliography page. The printed folio 45 and handwritten 27 should be kept distinct; the page does not itself show how the bibliography relates to the surrounding handwritten Hodge-algebra sheets.
935:**Editorial confidence:** high. The construction is finite-dimensional linear algebra once the parenthesized power convention is fixed; this does not establish the manuscript’s assertion.
2031:**Manuscript:** “à faire une vérification de compatibilité.....”
2465:The “Programme de travail” starts with an identification of a subgroup N(ξ) of an Albanese variety as the kernel of a cycle-valued map. A proof requires the exact definition of the equivalence relation in the denominator and an algebraicity/representability argument for that kernel; the interlinear qualification “en substance” makes the intended precision itself a research issue.
2497:**Editorial confidence:** medium. The manuscript moves from family-wise Albanese quotients to a global cycle quotient in one implication, leaving the universal property unstated.
2711:**Manuscript:** “Bures le12.8.1964; Mon cher Serre”
2721:The author proposes abelian varieties J^i(X) attached to algebraically trivial cycles, while explicitly admitting that the defining “équivalence d’Albanese” is not well identified. This is a central incompleteness, not merely an omitted exposition: construction, universal property and independence of the chosen parameter families all need clarification.
3044:The published SGA 3 second volume provides an identifiable comparison text for the indicated exposés (Demazure & Grothendieck, 1970). To determine which corrections were incorporated, one must align the draft's exposé, page, and line references with the corresponding prepublication pagination before comparing the final text. The present identification of a comparison volume does not establish that every listed correction was accepted, nor does it date the handwritten list.
3094:The page proposes ordinary multiplication by an alternating bivector and contraction by its dual as an integral model for the preceding Lefschetz identities, but its displayed construction does not specify divided powers or a change to normalized lowering. The separate editorial calculations R1–R2 exhibit the factorial obstruction to integral hard Lefschetz and distinguish contraction from unit-step lowering; they therefore prevent importing the matrix algebra in item S3 directly into the written \(\Phi_0=\mathbb Z[L_0,\Lambda_0]\). The useful research question is which coefficient localization, lattice, and operator normalization make the claimed universal property valid, with each choice stated before interpreting the margin's proposed extension to an arbitrary ring.
3121:### S5 — The five-dimensional example tests the universal property
3125:At \(n=1\), item S3 gives \(\operatorname{Mat}_2(\mathbb Z)\times\mathbb Z\), with basis corresponding to the three degree projectors and the two off-diagonal operators \(L,\Lambda\), hence rank five as on scan 17. That agreement checks the smallest case but does not establish the general identification of integral orders. The source's point is that prescribing the image of \(L\) alone does not prescribe the homomorphism: the revised proposition additionally controls the images of the grading projectors, and editorial calculation R3 explains why that extra datum matters.
3173:The criterion in scan 48 replaces a particular Lefschetz inverse by the existence of some algebraic isomorphism between complementary degrees, together with rationality of characteristic polynomials. Neither requirement mentions the chosen ample class, so—once the criterion's hypotheses hold for the fixed theory—the argument applies to another polarization through its own hard Lefschetz isomorphism. Kleiman (1968, §§2.9–2.10) proves this criterion and polarization independence. This reasoning does not itself produce one cycle working for every \(\ell\), identify the draft's undefined \(D_\ell\), or justify removing every parameter in scan 44.
3247:### F3 — Cote 47, scans 4–6, inversion theorem and anti-diagonal kernel
3253:### F4 — Cote 47, scan 5, inserted determinant factor; scans 6–7, Lemma 1
3263:### F5 — Cote 47, scan 4, bottom \(K\)-theory theorem; scan 5, corrected composite
3273:### F6 — Cote 47, scan 7, admitted Lemma 2 and following support argument
3279:### F7 — Cote 47, scan 8, first paragraph and unfinished verification
3281:**Kind:** own idea. **Manuscript:** “à faire une vérification de compatibilité.....”.
3283:**Editorial proof plan:** the direct image of the Poincaré line bundle is perfect, and the zero-section pushforward is perfect because that section is a regular immersion, so the cone of the proposed comparison is perfect. Vanishing of all its derived residue-field fibres then proves that the cone vanishes, by the local perfect-complex criterion (The Stacks Project Authors, 2026, Tags 0DJT and 0G99). The remaining task is to show that the particular map induces the required isomorphisms at the unit, not merely that the two sides have equal cohomology dimensions. **Confidence: high**, because the finite-complex criterion is established and isolates exactly the manuscript’s unfinished step.
3285:### F8 — Cote 47, scans 7–8, top cohomology and derived restriction to the unit
3295:Thus the top Tor line supplies the cancellation in degree zero, while degree \(g\) retains \(\det T\), matching the exterior-power pattern of \(R^iq_*\mathcal O_B\) in the manuscript. This uses the Koszul construction (The Stacks Project Authors, 2026, Tag 0621) and asserts the cohomology identification, without asserting a global splitting or completing the compatibility of the actual comparison map. **Confidence: high**, because the calculation is local on a regular sequence and keeps the determinant and shift explicit.
3476:**Confidence: high**, from the difference between existence on an open set and a universal property.
3487:### D08. Cote 44, scan 2, Theorem 3; scan 8, first paragraph of the letter
3489:**Kind:** reading question. **Quote:** “une relation d'équivalence que je ne sais pas bien identifier”. **Status:** comparison requiring a universal property.
3495:### D09. Cote 44, scan 2, Theorem 2 and its implication for Theorem 3
3503:### D10. Cote 44, scan 8, parenthesis strengthening the Tate-module statement
3515:### D11. Cote 44, scan 8, proposed general intermediate Jacobians
3523:### D12. Cote 44, scan 4, Theorem 5 and fibration margin
3528:This is a useful comparison for the manuscript's fibration strategy, but does not establish its formula for a generic member of a pencil on an arbitrary projective variety, nor its sign or positivity.
3529:**Editorial confidence: high** that a proof must specify height normalization and demonstrate invariance under changes of extensions by vertical cycles, because these choices affect the proposed intersection calculation.
3531:### D13. Cote 44, scan 8, primitive-decomposition margin; scan 9, divisor correspondence
3540:### D14. Cote 44, scan 6, Theorem 7 and “Matsusaka” margin
```

### S07 — Earlier doubts relevant to the Fourier map and cycle programme

```bash
rg -n '^\| 47 \| (5|6|7|8) \||^\| 44 \| (2|4|8) \|' context/MPL_16+47+54+44_doubts.md
```

Exit status: 0.

```text
499:| 47 | 5 | category subscripts throughout | parf | prof; repeated short form retained with uncertainty; margin spells parfaits clearly | medium |
500:| 47 | 5 | top determinant formula | Λ with n written immediately above, followed by t_A and t_B | small overmark could be a hat; retained as an uncertain n in the observed overhead position | medium |
501:| 47 | 5 | top cancelled identity phrase | identique, … | two following words beneath cancellation cannot be resolved | low |
502:| 47 | 5 | circled cancellation upper right | de catégories | possibly mathematical letters; almost completely overwritten | low |
503:| 47 | 5 | corollary number and newly defined operator | 3; D_L | number2; operator/subscript glyph could differ | low |
504:| 47 | 5 | first corollary displayed input | F L⊗ G | star and tensor were overwritten; retained tensor/star uncertainty | medium |
505:| 47 | 5 | kernel category | M∈D_parf(A) | only A is written, despite the subsequent kernel calculation on A×A; not repaired | high |
506:| 47 | 5 | kernel formula first derived letter | R | L-like under-stroke beneath retracing; later text explicitly says Rpr₁₃* | medium |
507:| 47 | 5 | final line φ map target | φ:A–B | no star visible after B, although adjacent prose twice says B* | high |
508:| 47 | 5 | cancelled word before produit de Convolution | couple | coupu / coup…; heavily struck | low |
509:| 47 | 6 | diagram and lemma product factors | star on first B, cancelled star on second B | ink on second superscript is densely overwritten; some first-star occurrences are faint | medium |
510:| 47 | 6 | lemma conclusion after e_* | deleted O_B*[−n]⊗τ_B* | O_S may replace O_B*; the deleted tensor/twist segment is highly uncertain | low |
511:| 47 | 6 | lemma zero-section subscript | e_{0*} | e_{B* *}; the subscript is a filled blob | low |
512:| 47 | 6 | left margin differential formula | ω=det*(Ω¹_B*/S) | det e*; denominator could be A; copied locally without imposing a standard determinant convention | low |
513:| 47 | 6 | corollary first display | Lψ*(τ_B*[−n]) | small crossed fragment after τ_B* may contain a superscript rather than a star; no e_* is visible in this display | medium |
514:| 47 | 6 | last paragraph φ target | C* | B* would fit surrounding notation, but the observed letter is a clear open C; preserved C* | high |
515:| 47 | 6 | last cancelled phrase | le même résultat | le …; line heavily crossed and final word compressed | low |
516:| 47 | 6 | projection indices | pr₁/pr′₁ in diagram and corollary, pr₂/pr′₂ in the initial base-change equations | indices are visibly different; not normalized | high |
517:| 47 | 6 | last line | modulo dém. du Lemme1 | first word and abbreviation are lightly written but readable | medium |
518:| 47 | 7 | Lemme2 variety label in cohomology | H^i(X,L), H⁰(X,L) | the prose uses B but the formulas visibly use X; preserved | high |
519:| 47 | 7 | upper cancelled boxed material | si L≄O_B; H⁰(X,L)=k si L≃O_B | large angular cancellations cross the condition and some equals signs; exact first si is uncertain | medium |
520:| 47 | 7 | cancelled lemma proof last clause | si i>0 | last comparison/zero lies beneath double cancellation lines | low |
521:| 47 | 7 | Nous allons … et nous … | montrer | montrerons; ending compressed at right margin | medium |
522:| 47 | 7 | canonical-map cancelled targets | e_*O_S[−n], e_*O_S, and [−n] | some first operator glyphs are fully overwritten; reconstruction limited to visible e/O/S/brackets | low |
523:| 47 | 7 | before e*R^np_*W | eq. | e_B*; short heavy mark may be a label rather than formula | low |
524:| 47 | 7 | last cancelled phrase | fera correspondre | first word may be fera; second word almost fully crossed | low |
525:| 47 | 7 | diagram q edge | plain vertical stroke | no arrowhead distinguishable; other three arrowheads clear | medium |
526:| 47 | 8 | derived pointwise test | x∈B* and Li_x* | b∈B* and Li_b*; first point glyph has several overlapping strokes | medium |
527:| 47 | 8 | complement of unit section | B*−e₁(S) | B*−e(S); a vertical small stroke is visible below e | medium |
528:| 47 | 8 | remark1b surviving convolution formula | Φ_L(F)*e_t | no minus visible before t although preceding two formulas use e_{−t}; not harmonized | high |
529:| 47 | 8 | remark1b cancelled factors | ω[n] and ω[n]e | characters beneath diagonal crossout partly lost; trailing e-like character may be subscripted | low |
530:| 47 | 8 | remark1b opening brace | { before Φ_L(F)*e_t | no matching closing brace clearly visible on the line | medium |
531:| 47 | 8 | rank margin | r-g virtuel | rang virtuel; first word is abbreviated or highly compressed | medium |
532:| 47 | 8 | cancelled start of remark2 | sur les VA relatives | first two words uncertain; VA and relatives more legible | low |
533:| 47 | 8 | determinant operation | det*∘Φ_L | star clearly raised; not replaced by an unstarred determinant | high |
534:| 47 | 8 | left margin, coefficient group in H0 | doubled-stroke Z | bold Z | medium |
622:| 44 | 2 | upper right | 7 | question mark; isolated mark | low |
623:| 44 | 2 | section letter | A | reinforced/overwritten glyph | medium |
624:| 44 | 2 | theorem1 N argument | xi | zeta; long cursive loop | medium |
625:| 44 | 2 | theorem1 cancellation | des | donc; short struck word | low |
626:| 44 | 2 | cycle symbols | calligraphic Z | plain Z; three-stroke curled form differs from straight numerator Z in Th.3 | medium |
627:| 44 | 2 | cycle quotient subscript | alb | ab; middle small stroke | medium |
628:| 44 | 2 | theorem3 target symbol | P^i | very cursive initial P | medium |
629:| 44 | 2 | theorem3 dual index | n−i | n+1−i; first part of superscript overwritten | low |
630:| 44 | 2 | theorem4 bracket | donc la corr. sur | compressed phrase before underlined P^m | low |
631:| 44 | 2 | theorem4 final participle | associé | associée; visible ending not grammatically normalized | medium |
644:| 44 | 4 | top canceled arithmetic | 2n | n; final glyph overwritten | low |
645:| 44 | 4 | canceled word before Z | même | possibly unrelated short clause | low |
646:| 44 | 4 | star and cycle alphabet | mathcal Z star | star heavily reinforced but visible | medium |
647:| 44 | 4 | insertion before i+j=n | et canceled | illegibly overwritten short word | low |
648:| 44 | 4 | pencil callout | dont toutes les fibres sont géom. intègres | toutes canceled; small word fibers inferred from strokes | medium |
649:| 44 | 4 | codimension cancellation | en dim | small obliterated phrase | low |
650:| 44 | 4 | Néron–Tate bracket indices | P^i(Y),P^j(Y) | first superscript faint, second resembles0 | low |
651:| 44 | 4 | pairing sign exponent | m | small m; retained rather than changed to i | medium |
652:| 44 | 4 | left NB ending | au sens général | en sens géométrique; final two words weak | low |
653:| 44 | 4 | right callout | Doit résulter d’un énoncé plus général sur des fibrations | général versus fin; compressed but overall sentence recoverable | medium |
654:| 44 | 4 | theorem6 struck phrase | Et [est égale àP^i(X)] | first word and phrase layered | low |
655:| 44 | 4 | theorem6 canceled condition | Si2i=n, n=2i, si n pair et i=n/2 | multiple overwrites; syntactic order uncertain | low |
656:| 44 | 4 | theorem6 final canceled inequality | 2i≤n+1 | comparison crossed by leader | low |
657:| 44 | 4 | maps in theorem6 | P^i(X)—P^i(Y) | no unequivocal arrowheads; represented by dash | high |
658:| 44 | 4 | main line éléments de in theorem 5 | P^i(Y), P^j(Y) | first superscript overwritten; second is a small loop also compatible with 0, as in following bracket | low |
659:| 44 | 4 | above canceled theorem-6 condition | pour | pair; first reader independently agrees the looped descender favors pour, but heavy cancellation prevents certainty | low |
675:| 44 | 8 | first paragraph range | 0 | 1; typewriter character overwritten and heavy, ink reads0 before1 | low |
676:| 44 | 8 | initial corrected letters | d,g,c | manuscript reinforcements/corrections retained as insertions; overwritten original letters not recoverable separately | medium |
677:| 44 | 8 | Tate-module index | ell | typewritten l with handwritten loop | high |
678:| 44 | 8 | cohomology coefficient underline | underlinedZ_l | underline atZ before ell visible | medium |
679:| 44 | 8 | tangent note relation | subset | in; reinforced left stroke | medium |
680:| 44 | 8 | tangent note H index | i | very small index byH | medium |
681:| 44 | 8 | canceled middle margin | H^1(J^i)≃ Alg. de Hodge | first exponent couldi; words crossed by two long strokes | low |
682:| 44 | 8 | lower margin opening | Ça veut dire | first compressed phrase weak | low |
683:| 44 | 8 | lower margin ellipsis | four dots | four or five visible ink points | low |
```

### S08 — Explicit dates and programme heading

```bash
rg -n -i '1962|1964|July 6|Bures le|Programme de travail' MPL_57_226-270/MPL_57_226-270_transcription.tex context/MPL_16+47+54+44_transcription.tex
```

Exit status: 0.

```text
context/MPL_16+47+54+44_transcription.tex:1169:[20] Ogg, A. P., \uline{Cohomology of abelian varieties over function fields}, Ann. of Math., 76 (1962), 185-212.
context/MPL_16+47+54+44_transcription.tex:1171:[21] Rosenberg, A. and Zelinsky, D., \uline{Amitsur's complex for inseparable fields}, Osaka Math. J., 14 (1962), 219-240.
context/MPL_16+47+54+44_transcription.tex:1173:[22] Serre, J.-P., Corps Locaux, Actualités scientifiques et industrielles No. 1296, 1962, Paris.
context/MPL_16+47+54+44_transcription.tex:1175:[23] \rule{2cm}{0.4pt}, ``Dimension cohomologique'', \unsure{Notes.at|Notes at} Collège de France, 1962.
context/MPL_16+47+54+44_transcription.tex:2782:\uline{Programme de travail}
context/MPL_16+47+54+44_transcription.tex:2970:Bures le 12.8.1964
MPL_57_226-270/MPL_57_226-270_transcription.tex:10:\begin{flushright}Neuilly July 6 1962\end{flushright}
```

Matched transcription locations: CT 16:28; CT 44:2; CT 44:8; P57 57:227.

### S09 — Current higher-cycle, correspondence, and positivity terms

```bash
rg -n -i 'correspon|polar|dual|\bTate\b|Hodge|codim|équiv|equiv|ample|positive|intersection|fibrations' MPL_57_226-270/MPL_57_226-270_transcription.tex
```

Exit status: 0.

```text
49:\uline{Corollary 1} The following conditions are equivalent:
77:We get for example:
79:\uline{Corollary} 1 The following conditions are equivalent: (i) $X/Y$ projective (ii) $\widehat{X}/\widehat{Y}$ projective (iii) For every $n$, $X_n/Y_n$ projective.
103:``henselian closures'' of the local rings arising from algebras of \uline{finite} type over a field, or over the integers, - although I do not have any result along these lines (except \inserted{those} stemming from my remark on $\pi_0$). \deleted{\unsure{For corollary}} This can be stated of course directly in terms of conjectures for the latter local rings without explicit reference to a henselian closure, for instance corollary 2 would yield the conjectural statement: Let $A$ be a local \deleted{\unsure{rin}} ring of an algebra of finite type over a field, $\widehat{A}$ its completion, $Y$ and $\widehat{Y}$ the spectra, $Y'$ and $\widehat{Y}'$ the complements of the closed points, \deleted{\unsure{i}} then any invertible sheaf on $\overset{\deleted{\unsure{\wedge}}}{\widehat{Y}'}$ can be defined by an inver\deleted{\unsure{si}}tible sheaf on some $Y_1'$, where $Y_1$ is local and $Y_1\quad Y$ is étale with trivial residue field extension (i.e. inducing an isomorphism for the completions in $A\quad A_1$). I wonder what information is given by Mumfords example in his blue paper, p.16, which I believe yields a case where the invertible sheaf considered does not come from an invertible sheaf on $Y'$ ? I \deleted{did} was not able to understand his construction.
213:Un système linéaire sera dit \uline{ample} \inserted{s'il est sans \unsure{com.|comp.} fixe et} si l'application rationnelle $T$ induite par $\mathcal{L}$ est un isomorphisme de $V$ sur $V'$. Si $D$ est un diviseur tel que $\mathcal{L}(D)$ soit ample, alors $D$ est dit \uline{ample}. Le système des
307:PROPOSITION 8.- \uline{Soient} $A$ \uline{un anneau noethérien}, $\underline a$ \uline{un idéal de} $A$, \uline{et} $M$ \uline{un $A$-module de type fini}. \uline{Les conditions suivantes sont équivalentes} :
317:PROPOSITION 9.- \uline{Soient} $A$ \uline{un anneau noethérien}, $\underline a$ \uline{un idéal de} $A$, \uline{et} $M$ \uline{un $A$-module de type fini}. \uline{Pour qu'il existe un entier} $n>0$ \uline{tel que} $a^nM=(0)$, \uline{il faut et il suffit que $a$ soit contenu dans l'intersection des idéaux premiers associés à} $M$.
407:Tous les cycles $Z(f)$, $f\in R_n$, sont linéairement équivalent. En fait, si $f$, $g\in R_n$, on a $(f/g)=Z(f)-Z(g)$.
666:\deleted{Deux} Conditions équivalentes :
717:\uline{Corollaire} 1.8. Soit $f:X\to Y$ un morphisme propre d'espaces analytiques \inserted{sur $\mathbb C$}, et $y\in Y$. Conditions équivalentes :
809:soit un isom il faut s. que $H^1(X,\mathcal O_X)$ soit de longueur finie sur $A$, i.e. $\operatorname{supp}R^1f_*(\mathcal O_X)\subset\{y\}$ ($y$ le pt fermé de $Y$), \deleted{\unsure{ce qui équivaut|ce qui implique} \inserted{\unsure{le groupe|le degré}} \unsure{de} \unsure{isomorphisme|homomorphisme} \unsure{que le syst.} projectif $(\operatorname{Pic}(X_n))$ soit ess\textsuperscript{t}. constant}
819:\uline{Corollaire} 2.2. Conditions équivalentes
845:Soit $L_{n_0}$ Module inv. sur $X_{n_0}$ ample $/Y_{n_0}$. \deleted{\unsure{Je|Il} provient d'un $\unsure{L}$} \inserted{Donc $\unsure{L|L_0}$ en vertu de 2.1. a)} provient d'un module inv. $\mathcal L$ sur $\widehat X$, donc en vertu de \deleted{\unsure{a)|(i)}} 2.1. (ii) il provient aussi d'un module \inserted{inv.} $L$ sur $X$. Ce dernier est ample en vertu de EGA III. Qfd.
882:En particulier, $i_*(\mathcal O_{Y'})$ est cohérent, donc correspond à une algèbre $A'$ finie sur $A$. \deleted{Rien ne change \unsure{à|si}} Cette dernière correspond à un $\unsure{Y_1|X_1}$ fini sur $\unsure{Y|X}$, réduit, tq que
```

Matched transcription locations: P57 57:228; P57 57:229; P57 57:231; P57 57:236; P57 57:240; P57 57:244; P57 57:258; P57 57:260; P57 57:264; P57 57:266; P57 57:268.

### S10 — Previous same-cote leads only

```bash
rg -n '^### F0[1-3]|^### J0[1-7]|### F01|### J03|second witness|earlier textual' context/same_cote_57/MPL_57_271-315_notes.md
```

Exit status: 0.

```text
7:**Answers to the two planning questions:** this selection supplies **no identified second witness of cote 47 with its Fourier compatibility check completed**, and **no established earlier textual form of cote 44's Theorems 1–7**. There are substantial links through relative Picard objects, duality, hyperplane restriction and divisor equivalence; the itemized comparisons below state what those links supply and what they leave open.
25:### F01 — The compatibility gap remains a particular map
32:The relevant earlier gap is CT, 47:7–8: after constructing \(\mathbf Rp_*W\longrightarrow e_*(\mathcal O_S)\otimes\tau_{B^*}[-n]\), the argument at the unit ends “à faire une vérification de compatibilité.....”. The present first-order Picard diagrams at 57:294 and 297 do not display that map, and “Compatibilité aux spécialisations ???” at 57:310 belongs to a different Picard question list. CN F7 is an editorial proof plan and F8 compares cohomology/exterior powers while leaving compatibility of the actual map uncompleted. Consequently these 43 scans do not provide the sought second witness or missing check; this is a bounded documentary conclusion, not a claim that the check is impossible or absent elsewhere.
34:### F02 — An admitted lemma is a separate issue
43:### F03 — Product line bundles and dual equivariance are real bridges
52:### J01 — Theorem 1: the kernel construction is absent
61:### J02 — Theorem 2: tangent dimension is not the Betti bound
68:CT, 44:2, Theorem 2 gives a proposed bound by one half of an odd Betti number, and CT, 44:8 proposes a Tate-module realization; CN D09–D10 are unreviewed leads about the scope of such claims. The current Igusa calculation explicitly distinguishes \(\dim H^1(\mathcal O_X)\) from Picard dimension, while 57:291–292 discuss abstract torsion groups. Neither calculation supplies a bound for all parameter-family Albanese quotients, so no second witness of Theorem 2 is established.
70:### J03 — Theorem 3: ordinary endpoints do not construct all higher representatives
79:### J04 — Theorem 4: a cone does not prove positivity of a correspondence
88:### J05 — Theorem 5: the name Néron is not a height formula
97:### J06 — Theorem 6: a close hyperplane question remains a question
106:### J07 — Theorem 7: the divisor-level comparison is explicit
```

### S11 — Planning entry statuses

```bash
rg -n -F -e '**WG2 §2.4 #4**' -e '**WG2 §2.3 #12**' -e '**WG H9**' context/notes/RESULTS_STATE.md
```

Exit status: 0.

```text
446:- **WG H9** [hunch of the war game (Believe; unchecked)] Th. 5 of cote 44 is the Mordell–Weil lattice formula in codimension m, and it makes Th. 4 equivalent to a Hodge index statement (Book II, 44). Believe (a); (b) as stated is a reduction, believed.: Let X be smooth projective of dimension n = 2m over k, X̃ → P¹ a Lefschetz pencil with generic fibre Y over K = k(t), and Z, Z′ cycl… (WARGAME_MATH_HUNCHES_20261112.md)
448:- **WG2 §2.3 #12** [question or plan item of the war game (round 2; unchecked)] 2.3 The mathematics, and what the literature says to it: *What is there* [C]. Th. 3: Z^i_alg(X)/Z^i_alb(X) = P^i(X) is an abelian variety and P^i(X), P^(n+1−i)(X) are dual. Th. 2: dim ≤ ½ b_(2i−1). Th. 4 ("Hodge"): for n = 2m − 1 the self-duality of P^m(X) is a polarization. Th. 5 ("Néron"): for cycles Z, Z′ of complementary co… (PROGRAM_WARGAME_ROUND2_20261112.md)
449:- **WG2 §2.4 #4** [question or plan item of the war game (round 2; unchecked)] 2.4 How it meets the stages that follow: Abelian varieties and Picard (the folders 06–09 of the archive) ; 47 and 44 are their research end: Fourier transform, intermediate Jacobians ; Is there a second witness of 47 with the compatibility check done? Earlier forms of Th. 1–7 (PROGRAM_WARGAME_ROUND2_20261112.md)
```

### S12 — Standalone negative Fourier query in the current package

```bash
rg -n -i 'Fourier|Pontryagin|convolution|compatib|Poincar|faisceau de Weil|Module de Weil|anti-diagonale|mapping-cylindres' MPL_57_226-270/MPL_57_226-270_transcription.tex
```

Exit status: 1.

```text
(no matches)
```

### S13 — Standalone negative exact-symbol query in the current package

```bash
rg -n -F -e 'P^i' -e 'J^i' -e 'Z^i' -e 'N(\xi)' -e 'b^{2i-1}' -e 'Z\mathbin{.}Z' MPL_57_226-270/MPL_57_226-270_transcription.tex
```

Exit status: 1.

```text
(no matches)
```

