# Picard context comparison after the transcription freeze

Prepared 18 November 2026 by the package-validation/context-comparison agent for the root editor. **This is a research memo and candidate-note bank, not an amendment to the transcription or to the results register.** The root editor froze the transcription at **2026-11-18 08:54:59 UTC** before authorizing context access. No scan image was opened by this agent, no OCR was used, and no page file was changed during this work.

## Sources, coverage, and citation conventions

The following were read in full: `context/README.md`; `context/notes/RESULTS_STATE.md` (495 lines); `context/hua_project/README.md`; `context/hua_project/57.modern.tex` (2,975 lines, including its methodological preface and all later sections); and `context/same_cote_57/MPL_57_271-315_notes.md` (682 lines). The present comparison used the frozen TeX page files for scans 133–145, 147–155, 157–164, 166–167, 170–171, and 173–179. References to handwriting, cancellation, or uncertainty below describe the **root's frozen TeX representation**, not a new visual reading by this agent.

Paths are relative to `/workspace/scratch/641dc45262b6` unless specified otherwise:

| Key | Exact source |
|---|---|
| P | `MPL_57_133-179/pages/MPL_57_133-179_57_scanNNN.tex`; `P 147:25–31` means scan 147, physical lines 25–31 of that file. |
| H | `context/hua_project/57.modern.tex`; always credited as **Hua, modernised reading of cote 57**, with the exact section title below. |
| LP | `context/same_cote_57/MPL_57_271-315_notes.md`; a first-pass returned-package note, not a new examination of the later scans. |
| RS | `context/notes/RESULTS_STATE.md`; statuses remain the supplied register's claims with its stated review qualifications. |

Hua's page numbers in the relevant titled sections are archive foliation, one less than the current scan number. The frozen `% archive foliation` comments establish this locally; LP §9, item T08 records the same offset for the later package. Thus H's page 137 is current scan 138, and his page 303 is the later package's scan 304. This convention must be kept explicit in final notes.

The exact RS scope for Hua material lacking an individual finding ID is **“Michel Hua's project: its modernised reading of these cotes” → “Cote 57: the opening of `transcripts/57/57.modern.tex` in his project”** (RS lines 285–339). RS's orientation explicitly says its digest lists no Hua finding for these scans (line 18). The finding labels `57-analytic-pic-completion-criterion` and `57-ns-p-divisibility-generization` occur inside LP's older commentary; they are not newly supplied standalone finding entries in the present RS and should not be manufactured as such.

Hua's preface expressly supplies implicit hypotheses, corrects statements, normalizes notation, and omits reused texts; it identifies its pass as AI-produced and not checked against the pages by a human. His text is a comparison lead. LP likewise remains a first-pass lead, including its reports about printed sources that this agent did not reopen.

## Exact topic map

| Current scans | Hua's title and file lines | Later-package connection and limit |
|---|---|---|
| 133, 135 | **“Le noyau pour un morphisme surjectif (pages 132 et 134)”**, H 1706–1727 | LP P04 and P09 distinguish quotient conventions and universal hypotheses; neither verifies the present kernel proof. |
| 138–140 | **“$\mathrm{Pic}$ relatif et suite de Leray (pages 137 à 139)”**, H 1729–1748 | **“Dévissage pour un composé (page 282)”**, H 2693–2704; LP P09, later scan 283. |
| 141–145 | **“Une obstruction pour une courbe épointée (pages 141 à 144)”**, H 1753–1783 | **“Contracter un sous-schéma fini (page 303)”**, H 2864–2884; LP C04 and I03, later scans 304–305. |
| 147, 149, 151, 155 | **“Le Picard d'une courbe réduite (pages 146 à 150)”**, H 1785–1832; also H's opening departure list | LP C04/I03 supply the unit-quotient mechanism; they do not reprove the singular-curve classification. |
| 153, 155 | **“Courbes stables (pages 152 et 154)”**, H 1834–1856 | RS EXIT_TOWER A.5 is a possible moduli-stratum lead, not a result proved by this calculation. |
| 157–162 | **“Plongements projectifs et foncteur de Picard (pages 156 à 163)”**, H 1859–1895 | LP P05–P06, later scans 275–277: quotient sheaf, torsor, and representability are separate obligations. |
| 164 | **“Diviseurs et Picard : la suite tangente (page 163)”**, H 1897–1909 | LP E01/E06/E07, later scans 284–286, 294, 297; LP D07 is a boundary against turning extensions into canonical splittings. |
| 166–167, 170–171 | **“Pseudo-morphismes et diviseurs (pages 165 à 170)”**, H 1912–1950 | No LP counterpart proves quasi-coherence of the pseudo-function sheaf. LP's reused divisor notes concern other leaves. |
| 173–179 | **“Le foncteur de Picard (pages 172 à 182)”**, H 1953–2012 | LP P05/P06/P09 and H's later composed-morphism discussion. H continues beyond this packet into current scans 180–183. |
| Reused 134, 136, 143, 148, 150, 152, 154, 159, 161, 163 | H's preface **“Not restated”**, lines 88–94; **“Ce qui n'est pas lu ici”**, lines 277–287, plus local footnotes | Their full frozen transcription adds documentary material omitted from Hua's mathematical narrative; no textual identity with another source is established merely by topic. |

## Candidate research notes

Each candidate's body is one to four sentences. Metadata identifies evidence and the intended RS connection. A claim attributed to H or LP remains that source's claim unless an explicit narrow check is recorded below.

### RPC01 — The kernel statement and its hypotheses are less uniform in the frozen text

**Current evidence:** P 133:5–16; short quotes: “un sous-groupe d'un groupe affine”, “alg.-affine”, “définies si $k$ est parfait”.  
**Context:** H, **“Le noyau pour un morphisme surjectif (pages 132 et 134)”**, 1706–1727; LP P04, later scans 275–277.  
**RS:** WG2 §1.1 #3; exact Hua scope above.  
**Kind:** unproved claim / comparison.

Hua, modernised reading of cote 57, replaces the opening kernel assertion by an extension of a finite group by an affine group and interprets the Néron–Severi subscript as passage modulo torsion. The frozen text instead states an embedding as a subgroup of an affine group, supplies representability for the affine-kernel corollary, and adds a perfect-field qualification to the “parties abéliennes”; it also begins the proof by assuming all Picard objects representable. These formulations should be compared explicitly, with the uncertain Néron–Severi notation retained, since LP P04 warns that quotienting by Picard-zero and by Picard-tau can retain different torsion information. No equivalence of every version, nor a proof without representability, was established here.

### RPC02 — The nonfinite-type warning survives beside the proof

**Current evidence:** P 135:8–22; short quotes: “un mono”, “ne sont pas de type fini”, “on peut sans doute s'en passer !”.  
**Context:** H, same kernel subsection, especially 1719–1725.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** self-flagged proof limitation.

Hua summarizes the reduction through the Stein factorization and stops at a monomorphism, but the frozen page explicitly questions the inference from monomorphism to affine when the Picard schemes are not of finite type. The margin therefore belongs in the mathematical status of the proof, together with the author's suggestion that the existence assumptions might be avoidable. Hua's “par Seshadri” also differs from the frozen uncertain citation “Sorb. chev.” and cannot replace it. The source's reversed-looking Picard arrow at P 135:18 remains a separate reading or drafting question.

### RPC03 — The quotient, not the unquotiented last arrow, is the candidate isomorphism

**Current evidence:** P 138:3–14, 20–22; P 140:20–25; short quote: “le dernier hom est un isom”.  
**Context:** H, **“$\mathrm{Pic}$ relatif et suite de Leray (pages 137 à 139)”**, 1729–1748; **“Dévissage pour un composé (page 282)”**, 2693–2704; LP P09, later scan 283.  
**RS:** WG2 §1.1 #3; exact Hua scope; LP P09 is located by its exact heading, not a fabricated RS entry.  
**Kind:** reading question / unpursued implication.

Hua writes that the map from $\operatorname{Pic}(X)$ is surjective when $X/\Sigma$ has a section, matching the following frozen quotient formula $\operatorname{Pic}'(X/S)\simeq\operatorname{Pic}(X)/\operatorname{Pic}(\Sigma)$. This clarifies the possible intended meaning of “dernier hom est un isom” but is a modernization, so the literal wording stays frozen. The later composed-morphism formula discussed in LP P09 is a useful continuation only with its universal $H^0$ and section hypotheses retained. It is not an unconditional product decomposition derived from the present sketch.

### RPC04 — Hua's inverse in the rigidification is an explicit correction

**Current evidence:** P 138:16–18, compared internally with P 175:7–11; short quote: “$L\otimes\varphi^*(g^*(L))$”.  
**Context:** H, relative-Picard subsection, 1740–1742, and **“Le foncteur de Picard (pages 172 à 182)”**, 1977–1982.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** context-induced reading question; narrow formula check.

Hua explicitly supplies an inverse absent from the frozen expression at scan 138, whereas the later frozen normalization at scan 175 already contains the inverse. Pulling the uncorrected expression back along $g$ gives $(g^*L)^{\otimes2}$; pulling back $L\otimes\varphi^*(g^*L)^{-1}$ gives the trivial bundle. This verifies the reason for Hua's correction under $\varphi\circ g=1$, without changing the reading of the source or proving all the surrounding descent claims.

### RPC05 — The abandoned draft and the different levels of base-change assumptions matter

**Current evidence:** P 138:22; P 139:9–20; P 140:3–20; P 177:7; short quotes: “qu. cpt et qu. sép”, “localement une section”.  
**Context:** H, relative-Picard subsection, especially 1743–1748; LP P09.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** source-status comparison.

Hua identifies the upside-down page as an abandoned attempt, agreeing with the cancelled block preserved at scan 139. The current notes distinguish quasi-compact/quasi-separated hypotheses in scan 138, a faithfully flat quasi-compact comparison in scan 140, and the explicitly universal $H^0$ condition inserted into the later sheaf assertion at scan 177. Those are separate stages; a final note should not silently promote the first fixed-base statement to the last universal one. LP P09 reinforces this distinction for its later composed-morphism formula.

### RPC06 — The current packet supplies the generalized Jacobian behind the later pinching lead

**Current evidence:** P 142:42–46; P 144:3–15; P 145:9–20; short quotes: “$E=\operatorname{Pic}^0_{Z/S}$”, “$P=\operatorname{Pic}^1_{Z/S}$”.  
**Context:** H, **“Une obstruction pour une courbe épointée (pages 141 à 144)”**, 1753–1783; **“Contracter un sous-schéma fini (page 303)”**, 2864–2884; LP C04 and I03, later scans 304–305.  
**RS:** MPL_57_271-315 C04; WG2 §1.1 #3; ANABELIAN_149_PUSH A.1 and SECTIONS_OVER_Q A.198 as possible applications only.  
**Kind:** unpursued implication.

Hua, modernised reading of cote 57, identifies the pinched curve's $E$ as the generalized Jacobian; the frozen current pages explicitly exhibit its torus-to-Jacobian extension and its degree-one torsor. This adds the named geometric object and the obstruction construction to LP C04's later unit-sequence mechanism and LP I03's proposed two-point test. The torus is essential, so these pages cannot be treated as an abelian-variety calculation alone. They do not compute the prime-to-$p$ Kummer kernel or the particular generalized-Jacobian comparison claimed in the two cited research-run entries.

### RPC07 — The obstruction comparison is explicitly left to verify

**Current evidence:** P 142:10–40; P 144:19–33; short quotes: “$\xi_n=\delta_n\eta$”, “à vérifier ......”.  
**Context:** H, punctured-curve subsection, 1758–1778.  
**RS:** LM7 E.23; LM6 E.21; WG2 §1.1 #3.  
**Kind:** self-flagged / unpursued implication.

Hua preserves the author's verification flag on the identification of the Leray obstruction $\xi_n$ with the Kummer boundary of the degree-one torsor $\eta$. The current packet gives a candidate abelian obstruction and states that a section of the punctured curve kills it, but does not establish the marked comparison or calculate the fibers of any nonabelian section map. This is therefore relevant groundwork for RS LM7 E.23 and LM6 E.21, not a determination of their still-open metabelian or class-two section classes.

### RPC08 — The torus cohomology shortcut has a visible splitting hypothesis

**Current evidence:** P 145:9–32; short quotes: “si $Y-S$ surjectif”, “Lorsque la suite exacte est splittée”, “$\operatorname{Pic}(S)^I/\operatorname{Pic}(S)$”.  
**Context:** H, punctured-curve subsection, 1777–1783; LP C04 and I03.  
**RS:** MPL_57_271-315 C04; WG2 §1.1 #3.  
**Kind:** hypothesis comparison and narrow algebra check.

The frozen source exposes both the surjectivity proviso for the initial unit sequence and the Brauer-group terms before deriving $H^1(S,T)$ from a split sequence. For a nonempty disjoint union of sections, the unit quotient is explicitly $\mathbf G_m^I/\mathbf G_m$; choosing one index gives the ratio coordinates $u_i/u_0$ and identifies it with $\mathbf G_m^{|I|-1}$. Thus LP I03's two-section example is an actual specialization of the present displayed torus, but the formula $H^1(S,T)=\operatorname{Pic}(Y)/\operatorname{im}\operatorname{Pic}(S)$ should not be detached from the splitting assumption. Hua's compressed final vanishing sentence should be read with these preceding assumptions.

### RPC09 — A vanishing obstruction is not a sufficient section criterion

**Current evidence:** P 142:40; P 145:22–32; short quote: “Cet élément est nul si $U$ a une section”.  
**Context:** H, punctured-curve subsection; LP I03 supplied the small-test motivation.  
**RS:** LM7 E.23 and LM6 E.21, boundary only; WG2 §1.1 #3.  
**Kind:** own idea. **Confidence: high for the elementary point-count boundary; conditional on the manuscript's vanishing statements for the asserted obstruction classes.**

Take $S=\operatorname{Spec}\mathbf F_2$, $X=\mathbf P^1_S$, and $Y=\{0,1,\infty\}$, a disjoint union of étale sections. Then $\operatorname{Pic}(S)=0$ and $X$ has a section, so the hypotheses of the displayed split-case vanishing conclusion hold, while $U=X-Y$ has no $\mathbf F_2$-point and hence no $S$-section. This makes the logical direction concrete: the proposed classes can be necessary obstructions without being sufficient tests for a section. It does not verify the still-marked identity $\xi_n=\delta_n\eta$ or refute the manuscript's one-way assertion.

### RPC10 — Empty punctures test the two-line spectral-sequence formulation

**Current evidence:** P 142:6, 15–19; P 145:9; short quotes: “$Y$ ... étale”, “si $Y-S$ surjectif”.  
**Context:** H, punctured-curve subsection, 1755–1764.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** own idea / hypothesis question. **Confidence: high for this boundary test.**

If empty $Y$ were allowed, take $X=\mathbf P^1$ over an algebraically closed field and an invertible integer $n>1$: then $U=X$ is proper and $H_c^0(U,\mu_n)=H^0(X,\mu_n)$ is nonzero. Thus the two-line description with only degrees 1 and 2 needs nonempty punctures on the relevant fibers, as suggested by scan 145's explicit surjectivity proviso. This is a scoped question about the hypotheses of the opening formulation, not a reason to insert words into scan 142 or to dismiss the intended punctured-curve construction.

### RPC11 — The normalized curve calculation supplies dimensions, not a canonical splitting

**Current evidence:** P 147:3–13, 20–31; P 149:3–21; P 151:27–38; short quotes: “partie linéaire”, “$\dim G=\sum\mu_\alpha-c_0+1$”.  
**Context:** H, **“Le Picard d'une courbe réduite (pages 146 à 150)”**, 1785–1832; LP C04/I03 and D07 as a methodological boundary.  
**RS:** WG2 §1.1 #3; MPL_57_271-315 C04; MPL_57_271-315 D07.  
**Kind:** unpursued implication.

Hua recasts the normalization unit sequence using the standard local $\delta$ notation and obtains a linear part of dimension $\sum\delta_\alpha-c_0+1$. The frozen text supplies the corresponding sequence, local quotient dimension, and genus decomposition while retaining changing $\mu$ notation and cancelled intermediate formulas. These formulas give a concrete explanation for additive and multiplicative contributions beyond the normalized components' Jacobians. They should not be promoted to a canonical splitting of the whole Picard group, paralleling LP D07's warning that extension data are weaker than splitting data.

### RPC12 — Branch incidence, not only component intersections, controls the toric count

**Current evidence:** P 149:7, 11–18; P 151:35–38; short quotes: “branches formelles”, “n'est pas déterminé ... par le schém. combinatoire de $C$”.  
**Context:** H, reduced-curve subsection, 1807–1820.  
**RS:** WG2 §1.1 #3; LM7 E.23 and LM6 E.21 as possible abelian-layer applications only.  
**Kind:** unpursued implication.

Hua explains the toric rank through the incidence graph that retains branches of the normalization. This agrees with the frozen warning that the coarser component-intersection picture alone does not determine the count when components have multiple points. The current distinction is useful if these Picard computations are later used to form abelianized fundamental-group or Tate-module data, but no nonabelian group identification or arithmetic section calculation follows from a rank formula alone.

### RPC13 — Ordinary multiple points are already visible in a source correction

**Current evidence:** P 147:30–39; P 149:23; P 151:23–25; P 155:3–17; short quotes: deleted “doubles”, inserted “multiples”; “les $\mu_\alpha=0$”.  
**Context:** H, reduced-curve subsection, 1823–1832, and opening departures list, lines 59–61.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** comparison / reading questions.

Hua attributes an ordinary-double-point restriction to both archive pages 150 and 154, but the frozen scan 151 explicitly replaces “doubles” by “multiples”; scan 155 still uses “pts doubles”. His reformulation using $\delta=r-1$ is therefore partly anticipated by a recorded source correction, and should not be presented wholly as a new repair by the modernizer. The frozen $\mu$ conventions also vary, so scan 155's $\mu_\alpha=0$ cannot simply be substituted into scan 147's $\mu_\alpha=\dim_k(\widetilde O/O)$ without explanation. Finally, Hua calls $\mu=1+\delta$ part of a cancelled passage, whereas the frozen deletion begins after that displayed equation: that discrepancy is a notes-only reading question.

### RPC14 — Hua's stable-curve interpretation has a checkable arithmetic core

**Current evidence:** P 153:18–28, 47–51; P 155:23–33, 42–46; short quotes: “$3g_i-3+\nu_i$”, “courbe elliptique $+\ k$ points”.  
**Context:** H, **“Courbes stables (pages 152 et 154)”**, 1834–1856.  
**RS:** EXIT_TOWER A.5 (RS headline section, lines 33–35); WG2 §1.1 #3.  
**Kind:** attributed interpretation plus own computation. **Confidence: high for the displayed algebra under its stated graph assumptions; no new moduli theorem claimed.**

Hua interprets these sketches as the dimension count for a stratum of stable curves, while expressly noting that the page names neither stability nor a moduli space. Substituting $\rho=c_1-c_0+1$ into his expression verifies $3g-3-[2(c_0+\rho)-c_1-\lambda-2]=3g-3-c_1+\lambda$, and for stable components the correction term is absent. This is a precise numerical bridge to RS EXIT_TOWER A.5, not a verification of its product description, asphericity, fundamental group, or arithmetic assertions. The final elliptic-curve numerical sketch remains incompletely explained in both the frozen source and Hua's account.

### RPC15 — The projective index correction should retain the original convention as a question

**Current evidence:** P 158:5, 11–25; P 160:37–49; short quotes: “rang $N$”, “$\mathrm P_S^N$”, “$GP(N)$”.  
**Context:** H, **“Plongements projectifs et foncteur de Picard (pages 156 à 163)”**, 1859–1895, especially 1862–1864.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** context-induced notation question / narrow index check.

Hua changes $\operatorname{rank}E=N$ to $N+1$ and uses $\mathrm{PGL}(N+1)$ while explicitly recording the source discrepancy. With the modern convention that $\mathbf P^N$ has the $N+1$ coordinate sections of $O(1)$, the displayed isomorphism on global sections does force this rank. That calculation explains his modernization but does not decide whether the manuscript used a different projective-index convention or slipped in its notation. The frozen rank, projective superscript, and $GP(N)$ should all remain as recorded.

### RPC16 — The quotient construction is a program with surviving base-change and representability obligations

**Current evidence:** P 158:27–29, 33–47; P 160:5–55; P 162:3–16; short quotes: “morphisme spécial”, “sans pts fixes”, uncertain “existe, c'est un espace”.  
**Context:** H, projective-embedding section, 1866–1895; LP P05/P06, later scans 275–277.  
**RS:** WG2 §1.1 #3; exact Hua scope; LP P05/P06 by their exact headings.  
**Kind:** unproved claim / hypothesis comparison.

Hua organizes the four equivalences into bases, projective trivializations, line-bundle classes, and Brauer–Severi torsors, then identifies their quotient with large Picard opens. The frozen margins explicitly demand attention to base change in the “special” condition, and the continuation on scan 162 is substantially uncertain. LP P05/P06 show why a free-action or torsor interpretation alone should not be read as a proof that the needed quotient is represented under every proposed hypothesis. This comparison supports the construction's intended direction while leaving its represented-object conclusions qualified.

### RPC17 — The final tangent-sequence degree is a mathematical correction, not a resolved reading

**Current evidence:** P 164:20–34; short quote: “Tangent ... $\operatorname{Pic}/S$”; the final exponent is recorded as `\unsure{1|2}` at line 31.  
**Context:** H, **“Diviseurs et Picard : la suite tangente (page 163)”**, 1897–1909.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** context-induced reading question / narrow cohomological-degree check.

Hua writes the long exact sequence with $R^2f_*O_X$ after $R^1f_*(L|_Y)$ and says the source instead writes degree 1. From the short exact sequence $0\to O_X\to L\to L|_Y\to0$, the connecting map does raise the degree to 2, so the mathematical correction is clear. Our frozen source already records the digit as `\unsure{1|2}`, which must remain a reading uncertainty rather than be resolved from the expected exact sequence. The blurred marginal smoothness assertions require their own vanishing and base-change hypotheses and are not proved by identifying this degree.

### RPC18 — Tangent spaces should not be collapsed to dimensions of reduced Picard varieties

**Current evidence:** P 164:25–34; short quote: `$\underline H^1_f(\underline O_X)$` under “Tangent ... $\operatorname{Pic}/S$”.  
**Context:** H, tangent-sequence subsection; LP E01/E06/E07, later scans 284–286, 294, 297; LP J02/J03 and D07.  
**RS:** WG2 §2.3 #12; MPL_57_271-315 J03; MPL_57_271-315 D07.  
**Kind:** unpursued implication.

The current diagram identifies the cohomological tangent term while preserving later obstruction terms and two conditional smoothness margins. LP E01's reported Igusa example distinguishes a flat Picard object with extra infinitesimal structure from its reduced dimension, and LP E06 explicitly warns against inferring flatness from a condition on points. Those later leads explain why the current $H^1$ term should not be replaced by the dimension of a reduced abelian variety or used alone to prove a Betti bound. No Oda comparison, higher-cycle representative, or canonical de Rham splitting was checked by this agent.

### RPC19 — Hua's pseudo-morphism statement has a separated target and no general noetherian hypothesis

**Current evidence:** P 166:8–24; P 167:3–9; short quotes: “$Y$ séparé sur $S$”, “$X$ ... réduit”, “définit un faisceau”.  
**Context:** H, **“Pseudo-morphismes et diviseurs (pages 165 à 170)”**, 1912–1926.  
**RS:** exact Hua scope; WG2 §1.1 #3 for the surrounding divisor vocabulary only.  
**Kind:** precise hypothesis comparison.

Hua uses separatedness of $Y/S$ for equality on a schematically dense open and for the unique maximal domain of a pseudo-morphism, then uses that domain property for the sheaf assertion. Reducedness of $X$ enters only in identifying schematic density with density and pseudo-morphisms with rational maps; it is not stated as a universal hypothesis for the construction of pseudo-functions. No noetherian hypothesis appears in this opening paragraph. The later phrase “anneau normal noethérien” belongs to the divisor/height-one intersection argument and cannot be imported backward as Hua's claimed hypothesis for the pseudo-function sheaf.

### RPC20 — The cancelled quasi-coherence proposition has no verdict in Hua

**Current evidence:** P 167:9–12; short quote within complete deletion: “Prop. 0.1 Ce faisceau est quasi-cohérent.”  
**Context:** H, pseudo-morphism section, especially 1922–1926; full section searched for quasi-coherence and noetherian assumptions.  
**RS:** exact Hua scope; no direct settled RS entry.  
**Kind:** withdrawn in the same text, with truth value unresolved here.

The entire proposition and its beginning of reduction to $X=\operatorname{Spec}(A)$ are cancelled in the frozen transcription. Hua mentions only the sheaf of pseudo-functions as an algebra containing $O_X$ and gives neither the quasi-coherence assertion nor a reason to reject it. Thus this comparison establishes an omission in the modernization, not a counterexample or a verdict that the cancelled proposition is false. Any mathematical decision about quasi-coherence and the necessary reduced/noetherian hypotheses requires a separate proof or counterexample.

### RPC21 — The two normality relaxations have different mathematical scopes

**Current evidence:** P 170:3–9, 14–18; P 171:5–7; short quotes: “Les résultats précédents”, “le th. se généralise aussi”, “anneau de valuation”.  
**Context:** H, pseudo-morphism/divisor section, 1928–1950.  
**RS:** exact Hua scope; no direct RS theorem in this packet.  
**Kind:** attributed correction / scope distinction.

Hua objects to the first margin's extension of the preceding divisor criterion from normality to regularity in codimension one, supplying the missing $S_2$ issue and a pinched-plane counterexample as his explanation. He separately accepts the relaxation for the theorem about rational maps to a complete target, because its valuative proof uses regularity in codimension one. The frozen scan 170 has two distinct remarks in exactly these positions, followed by the height-one valuative argument on scan 171. This memo credits Hua's distinction and counterexample as a lead; the root editor's independent source-level counterexample work is separate and was not duplicated here.

### RPC22 — The three Picard functors and the base Picard kernel are explicitly separated

**Current evidence:** P 173:6–29; P 174:3–15; P 178:5–14; P 179:3–9; short quotes: “Prépic”, “Prépic'”, “son noyau”.  
**Context:** H, **“Le foncteur de Picard (pages 172 à 182)”**, 1953–2012; LP P05/P06/P09.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** unpursued implication.

Hua distinguishes the absolute Picard presheaf, its Zariski version, and the faithfully flat sheaf, matching the current chain $\mathrm{Prépic}\xrightarrow\alpha\mathrm{Prépic}'\xrightarrow\beta\mathrm{Pic}$. The frozen Leray sequence identifies the obstruction after the relative-class term, while the kernel of the first arrow retains the Picard group of the base under the stated $H^0$ assumption. These distinctions supply foundations for the later quotient questions in LP P05/P06, rather than a general representability theorem for each of the three functors. The source's explicit “dans des cas généraux importants” still leaves representability to later work.

### RPC23 — The rigidified category is clearer than the varying Prépic labels

**Current evidence:** P 174:17–19; P 175:3–14; P 177:3; short quotes: “isom. unique”, “Question: donner une formulation cohomologique”.  
**Context:** H, Picard-functor section, 1977–1982.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** reading question / self-flagged exposition.

Hua formulates the unique rigidified representative for a class in $\operatorname{Pic}'$, but the frozen statements at P 174:19 and P 177:3 display Prépic without the prime. The local-representative proof at scan 175 makes the distinction worth recording, while its inverse normalization and uniqueness argument supply the intended descent mechanism. This is a context-induced prime/quotient question, not permission to regularize the notation. The author also explicitly requests a cohomological formulation of the reasoning.

### RPC24 — Separate the fixed-base, flat-base-change, and universal sheaf statements

**Current evidence:** P 175:16–21; P 176:12–22; P 177:7; short quotes: “quasi-compact séparé”, marginal “q.c. qs”, “tte extension de la base”.  
**Context:** H, Picard-functor section, 1984–1992; LP P09, later scan 283.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** hypothesis comparison.

Hua states Proposition 2 with quasi-compactness and separatedness, which agrees with the frozen main statement at scan 175; the following frozen margin on scan 176 records a possibly weaker “q.c. qs” hypothesis. The universal $H^0$ assumption and local-section hypothesis are separately explicit in scan 177. LP P09's later composed-morphism claim has the same need to preserve universal assumptions before passing from fixed-base groups to sheaves. The present comparison does not replace the source's stronger main hypothesis by the weaker marginal one or prove that every variant suffices.

### RPC25 — The covering-site difficulty is an authorial issue, not an incidental modern convention

**Current evidence:** P 178:5–7; short quotes: “Il y a un ennui”, “morphismes de localisation fidèlement plats”.  
**Context:** H, Picard-functor section, 1994–2005; LP P05, later scans 275–276.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** self-flagged definition issue.

Hua explains the non-quasi-compact covering problem as a precaution incorporated in modern fpqc topology. The frozen page itself changes the proposed description because an arbitrary open cover need not be dominated by one faithfully flat quasi-compact morphism. A note should retain this definitional work and distinguish it from LP P05's later faithfully flat, locally finite type quotient sheaf. Those later site conventions are related leads, not interchangeable labels silently supplied to the frozen text.

### RPC26 — Brauer–Severi data connect the projective construction to the final failure of surjectivity

**Current evidence:** P 160:33–42; P 179:3–5; short quotes: “fibré de Brauer-Severi”, “$\beta$ n'est pas surjectif”, “$H^2(S,\mathbf G_m)$”.  
**Context:** H, projective-embedding section and Picard-functor section, 1878–1889 and 2006–2012; LP P05/P06.  
**RS:** WG2 §1.1 #3; exact Hua scope.  
**Kind:** unpursued implication.

Hua's account links projective torsors and relative line-bundle classes, and the frozen packet later names a nontrivial Severi–Brauer variety as an example where $\beta$ is not surjective. The displayed $H^2(\mathbf G_m)$ obstruction is a concrete warning that a class in the final sheaf need not come from the preceding Zariski relative class or a global line bundle. This is a useful internal connection to the quotient-existence problems in LP P05/P06, with the source's local-section and universal-$H^0$ hypotheses preserved. No specific Brauer class or represented quotient was calculated here.

### RPC27 — The reused sheets and dated letter add documentary evidence omitted by Hua

**Current evidence:** P 134:3–46; P 136; P 143:8–16; P 148/150/152; P 154:3–24; P 159:7–10; P 161:8–9, 31, 39; P 163:3–26. Short quotes: “Massy November 21, 1966”, “Détermination locale d'un morphisme”, “Nouveau fascicule”.  
**Context:** H preface 88–94; **“Ce qui n'est pas lu ici”**, 277–287; local footnotes in the kernel, stable-curve and projective sections; LP §9 T06–T08.  
**RS:** WG2 §1.1 #3; RS “Orientation for this package” lines 13–19.  
**Kind:** documentary addition.

Hua intentionally omits the reused Koszul/Čech material, analytic-surface typescripts, administrative letter, and most EGA proof-sheet text, whereas the frozen packet preserves those texts and their editorial changes. The explicit 1966 date on the administrative letter should be reported separately from the context's broad 1962 correspondence description and should not date adjacent undated Picard arguments. The EGA propositions and marginal corrections also have their own local hypotheses; adjacency does not turn them into steps of the handwritten Picard proof. Like LP's documentary index, this is evidence about the packet's composition, not a new identification of an unprovided original publication or hand.

### RPC28 — The supplied register's wider questions remain wider

**Current evidence:** P 142–145, 147–155, 164, 173–179; the narrow constructions identified in RPC06–RPC26.  
**Context:** H's complete cote interpretation; LP F01–F03, J01–J07, §10 G01–G08.  
**RS:** WG2 §2.4 #4; WG2 §2.3 #12; MPL_57_271-315 J03; LM7 E.23; LM6 E.21.  
**Kind:** scoped negative result / unpursued implication.

These pages supply Picard/descent foundations, a generalized Jacobian with a proposed obstruction class, singular-curve ranks, and a tangent sequence; none of those supplies the particular completed Fourier compatibility check requested by WG2 §2.4 #4. The ordinary Picard and Jacobian endpoints also do not construct the higher-codimension algebraic representatives or the full seven-theorem programme, matching LP J03's boundary. The current obstruction discussion is more specific than mere thematic proximity to the section-class questions, but it still does not calculate the open fibers in LM7 E.23 or LM6 E.21. No status in RS is upgraded by this memo.

## Notes-only reading questions induced by context

These are questions for the final research notes, **not a new visual audit and not changes to any frozen page or doubts entry**.

| Current location | Frozen reading or representation | Context suggests | Reason and limit |
|---|---|---|---|
| P 133:10 | “alg.-affine” | H kernel footnote says “quasi-affine” | Two textual readings; keep the root's frozen reading. |
| P 133:12 | Uncertain Néron–Severi notation with subscript 0; perfect-field insertion for abelian parts | H interprets modulo torsion and abelian parts up to isogeny | Modern interpretation does not settle the ink or absorb the explicit perfectness qualification. |
| P 135:10 | `\unsure{Sorb. chev.}` | H says “par Seshadri” | Attribution cannot be fixed from the expected descent theorem. |
| P 135:18 | Picard objects in the reversed-looking order | H follows the pullback direction from $Y$ to $X$ | Possible drafting or reading issue; no change after freeze. |
| P 138:11 | Last homomorphism “isom” | H says surjective | The quotient formula follows; it explains a likely intended assertion without rewriting the phrase. |
| P 138:18 | No inverse on $g^*L$ | H supplies inverse | The pullback computation confirms the mathematical need, not a different reading of the symbol. |
| P 147:34–37 | $\mu=1+\delta$ precedes the outer deletion beginning at 37 | H says it lies in a cancelled passage | Record discrepancy without deciding physical cancellation scope from context. |
| P 149:23; P 155:7 | Changing $\mu$ terminology and values | H standardizes to $\delta$, $r-1$, additive defect | The modernization may clarify intent but cannot erase local notation drift. |
| P 151:23; P 155:7 | “doubles” changed to “multiples” on 151; “doubles” remains on 155 | H footnote groups both as “points doubles ordinaires” | Current transcription provides a more differentiated account of the correction. |
| P 158:5, 11, 13 | Rank $N$, $O_S^N$, projective superscript $N$ | H chooses rank $N+1$ | Convention or error question; the modern rank check does not identify the source convention. |
| P 160:7, 25; P 162:3 | An $S$-class “sur $S$”; principal torsors “sur $X$” | H organizes data over $S$ for line bundles on $X$ | Base/object words may be drafting slips or uncertain readings; retain them and report the discrepancy. |
| P 160:23, 27, 35 | `magnifique|amplissime`, `amplissime` | H uses “morphique” in A''' | No contextual replacement of the frozen adjective. |
| P 162:5–16 | `\mathcal J|\mathcal I` and quotient continuation doubtful | H uses one streamlined special-Hom quotient | H itself calls this a fragment and flags thin readings; it does not settle these letters. |
| P 164:31 | `\unsure{1|2}` | H says source 1 and correct mathematics 2 | State the expected cohomological degree while preserving the digit doubt. |
| P 174:19; P 177:3 | Prépic without prime | H says Pic' | The local-representative proof motivates a question; no prime inserted post-freeze. |
| P 175:16; P 176:13 | Main separated hypothesis; marginal uncertain q.c. qs | H retains separated main statement | Do not falsely report that H has strengthened the main statement; its wording matches that line. |

## Negative coverage of Hua topics outside the packet

The full H file was read, not only the overlapping sections. The following are **negative statements about the present packet's coverage**, not declarations that the other mathematics is false or irrelevant to the wider Picard project.

| Hua topic, exact scope | Relation to current scans |
|---|---|
| **Local Picard functor and local completion**, pages 2–12; **Picard des cônes et de leurs anneaux locaux**, pages 183–193; **Théorème analytique** draft, pages 247–271 | No current cone/completion or analytic-algebraization argument. The reused adic-ring sheet at 159 is not a proof of those Picard comparisons. LP P02/P03 keeps the later completion questions conditional. |
| **Carré, cube et Picard d'un produit**, pages 13–18; **Rigidité et schémas abéliens**, pages 23–40; **Groupes rigides et descente**, pages 41–57 | Current rigidification along a section is a third notion, not the product rigidity lemma or dense-torsion notion of rigid group. No theorem-of-the-cube proof or rigid-group classification occurs in this interval. |
| **Albanese**, pages 58–63; **Plan d'un traité**, pages 64–65; **Finitude**, pages 66–71 | The current reduced-curve Picard and quotient discussions are foundations of the same subject, but contain no new general Albanese representability, Matsusaka finiteness, or complete treatise plan. |
| **Fibrés munis d'une connexion / extension vectorielle universelle**, pages 79–93; **Critères d'équivalence par une section hyperplane**, pages 95–100; **Picard et profondeur**, pages 101–102 | The tangent sequence at 164 is not a universal-vector-extension construction, a de Rham splitting, a Lefschetz restriction theorem, or a depth criterion. Those need separate notes if used, not implicit imports into the current diagram. |
| **Seshadri**, pages 103–113; **Séparation, unités et diviseurs**, pages 114–123; **Le principe : recoller par descente**, pages 125–128 | These are adjacent potential dependencies of 133–135, not current supplied proofs. In particular they cannot resolve the uncertain citation or eliminate the nonfinite-type caveat from the frozen page. |
| **$G^0$, $G^\tau$, constructibilité**, pages 200–211; **Dégénérescence**, pages 213–223 | No current general constructibility theorem or nonseparated-Picard degeneration construction. H's later three-line example is a plausible test for the current curve formulas, but was not independently checked here. |
| **Formel/analytique and Hironaka**, pages 225–245; letters to Murre at pages 19–22 and 72–78 | The reused IHES letter at current 143 is administratively and chronologically distinct; it does not supply the mathematical letters' assertions or date the undated sketches. |
| **Néron–Severi and polarizations**, pages 273–280; **Igusa and divisibility**, pages 283–291; **recollement**, pages 293–303; **questions ouvertes**, pages 307–314 | Relevant later leads are explicitly indexed above. None of their claimed examples, nonsaturation phenomena, global quotient existence, or open-question resolutions is reproved merely by the current foundational pages. |

Entirely external to the current mathematical claims are the RS full-profinite GT/CM-image calculations, finite-monoid homotopy results, Fourier transform compatibility map, higher-cycle polarization/height assertions, and nonabelian centralizer classifications. The current curve graphs and obstruction groups do not supply the needed objects or maps for those theorems. The specific connections retained in this memo are the numerical stable-stratum lead (EXIT_TOWER A.5) and the abelian/generalized-Jacobian layer of the named section questions.

## Proposed CHECK_EVENTS rows: only work actually performed

These rows are **proposals for the root editor**. The root owns `CHECK_EVENTS.tsv` and must translate RPC IDs to final note IDs if the corresponding notes are adopted. Reading H, LP, or RS in order is not itself an event. “Used and rechecked” below means the specified cross-source textual/hypothesis comparison, not an independent proof of the entire source theorem; “carried as background” is restricted to claims actually used as leads.

The actor field should be replaced by the root's exact model/effort/run convention if available; this agent has used `GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison` rather than guessing an effort setting.

```tsv
statement_id	date	who	type	outcome
RPC02	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	used and rechecked in this run	Compared H kernel reduction with frozen P135:18-22; recorded the nonfinite-type monomorphism caveat and representability qualification; no complete affine-kernel proof certified.
RPC04	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	targeted proof check	Under phi o g=1, pullback of the frozen product is (g*L)^2, whereas inverse normalization pulls back to O; checked only the rigidification formula, with source unchanged.
MPL_57_271-315 C04	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	carried as background without fault found	Used the first-pass later pinching note as a lead and compared its unit quotient to frozen P142:42-46, P144:3-15 and P145:9-20; no reinspection of later scans or proof of its general pushout exact sequence.
RPC08	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	targeted proof check	For a nonempty split union of sections, ratio coordinates identify G_m^I/diagonal G_m with G_m^(|I|-1); retained splitting and surjectivity qualifications in the cohomological use.
RPC09	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	targeted proof check	P1 over F2 has exactly 0,1,infinity as rational points; removing all three gives no section while Pic(S)=0 and the split puncture hypotheses hold. Boundary to sufficiency, conditional on the manuscript's vanishing conclusions; xi_n=delta_n eta not proved.
RPC10	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	targeted proof check	For empty punctures on P1 over an algebraically closed field and n>1 invertible, proper-support H0(mu_n) is nonzero; verified the need to qualify the two-line spectral-sequence formulation, not a refutation of the intended punctured case.
RPC13	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	used and rechecked in this run	Compared H ordinary-double-point footnote with frozen P151:23 deleted doubles/inserted multiples and P155:7; also localized its cancellation-scope discrepancy with P147:34-37. Textual comparison only, no image audit.
RPC14	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	computation or formal certificate	SymPy expansion of the difference between H's expression and 3g-3-c1+lambda after rho=c1-c0+1 returned zero. Verified arithmetic specialization only, not EXIT_TOWER A.5 or a moduli theorem.
EXIT_TOWER A.5	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	carried as background without fault found	Used supplied RS headline as a possible stable-stratum application of RPC14; its product, asphericity, and fundamental-group claims were not re-proved or upgraded.
RPC15	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	targeted proof check	Under the modern projective-space convention H0(P^N,O(1)) has coordinate basis of size N+1; this explains H's rank normalization but does not decide the manuscript's convention.
RPC17	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	targeted proof check	Applied the degree shift in the long exact cohomology sequence of 0 to O_X to L to L|Y to 0; the term after R1 f_*(L|Y) is R2 f_*O_X. Frozen unsure{1|2} and separate smoothness claims remain unresolved.
RPC19	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	used and rechecked in this run	Checked H1912-1950 against frozen P166-167: separated target retained, reducedness only for rational-map identification, and no general noetherian hypothesis in H's pseudo-function paragraph; normal noetherian belongs to the later divisor argument.
RPC20	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	used and rechecked in this run	Compared fully cancelled P167:11-12 with H1912-1950; H contains no quasi-coherence assertion or truth-value verdict for this proposition. Textual omission established; cancellation gives no falsity verdict.
MPL_57_271-315 D07	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	carried as background without fault found	Used its extension-versus-splitting warning to delimit RPC11 and RPC18; did not reopen its Oda or earlier-cote evidence and did not certify a general splitting theorem.
MPL_57_271-315 J03	2026-11-18	GPT-6 Astra Pro; effort not exposed; package_validation_tools context comparison	carried as background without fault found	Used the first-pass ordinary-endpoints versus higher-cycle distinction to delimit RPC18/RPC28; no higher algebraic representative or seven-theorem programme established.
```

No check event is proposed merely for reading the full context, noticing a theorem in the transcription, or seeing a cancellation. No event claims to re-prove LM7 E.23, LM6 E.21, ANABELIAN_149_PUSH A.1, SECTIONS_OVER_Q A.198, or any complete Hua theorem. Parent work on rigidification counterexamples, normality counterexamples, bibliographic identification, or Oda should receive its own separately scoped events rather than be credited to this memo.

## Handoff

The principal additions are: (1) the source's own nonfinite-type proof caveat; (2) a direct current witness for the later generalized-Jacobian pinching lead, with the obstruction comparison still marked to verify; (3) the source's existing ordinary-double to ordinary-multiple correction; (4) the exact division between a checked stable-graph arithmetic identity and Hua's moduli interpretation; (5) rank and cohomological-degree normalizations that must remain notes-only; (6) precise evidence that Hua supplies no quasi-coherence verdict for the cancelled proposition. This memo changes neither the transcription nor the inventory, doubts register, final notes, or check-event log.
