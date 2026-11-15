# MPL_18_018-062 — Research notes

Alexander Grothendieck, Montpellier archive, cote 18, scans 018–062. Research completed after the diplomatic transcription was frozen on **15 November 2026 at 22:05:33 UTC**; the context payload was opened at **22:05:39 UTC**. These notes use the frozen transcription, the supplied neighbouring material and the primary sources listed below.

## Evidence, notation and status

All 45 whole-page images and their 90 supplied halves were read personally in scan order, with a second reading of every page before the freeze. No OCR was used on the manuscript scans and no part of the transcription was delegated. Research contributions and independent algebra reviews began after freezing; their contributors used the frozen text and the context, without reading the manuscript images or editing the transcription. A preliminary archive-name listing exposed context filenames before the freeze; its payload remained unopened, and the event is recorded in the work log.

`18/NNN` means cote 18, scan NNN, in `pages/MPL_18_018-062_18_scanNNN.tex`; `L` locators refer to that file's lines, while named paragraphs and displays are more stable reading locators. The supplied context is cited by the following exact keys; it is not reproduced in the deliverable.

| Key | Supplied file | Evidential use |
|---|---|---|
| CT | `context/MPL_16+47+54+44_transcription.tex` | Prior first-pass transcription; `CT16/047` means its cote 16, scan 047 section. |
| CN | `context/MPL_16+47+54+44_notes.md` | Prior research leads, paired with CT. |
| PN | `context/same_cote_18/MPL_15_195-228+18_002-017_notes.md` | Prior same-cote research notes; earlier scan locators and quotations remain mediated by this file because the underlying page files were not supplied. |
| RS | `context/notes/RESULTS_STATE.md` | The supplied results register, retaining every stated review status. |
| Oda | `context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf` | Printed primary source; checked also against the published Numdam witness. |

`PN P19` and **P19** denote different local identifiers: the prefix PN always identifies the earlier package. The new observation groups are C (cycle classes), RH (real/Hodge), P (periods/cocycles), MB (motivic bridges), R (reused source layers), SF (author-marked qualifications) and T (titles/pagination). Each observation has a short substantive body with source, search and status metadata; the longer explicit calculations supporting RH06–11 and RH19–20 are collected in Appendices A–C.

A link to an RS row records relevance, not a status promotion. Several PN observations cited below have no individual row in this selective RS extract; they are explicitly prior-note leads. The supplied LM statuses are described as the returns' claims where RS does so, and the notes do not rederive the settled LM1 counterexample or infer a solution to the open LM6, LM7 or cote 149 questions. Executed searches are preserved in `records/context_searches.jsonl` and the subject-specific search records.

## Answers to the package's research questions

| Question | Evidence and conclusion in this return | Detailed items |
|---|---|---|
| Where is a written period conjecture? | **18/059** names “conjecture de transcendance N° 1”, calls the comparison point generic and reformulates it using the image of an automorphism-indexed map; **18/061** corrects its multiplication order. The base of genericity, the cocycle convention and the topology are retained explicitly. | P15–P18, P20–P26 |
| How do correspondence rings reach motives here? | **18/025** supplies the correspondence action $x\mapsto p_{2*}(p_1^*x\,P(z))$, linking CT16's realization homomorphism $\Phi\to E$ to the later category and fibre-functor notation. A historical construction specifying all objects, morphisms, equivalence relations, twists and summands is still unlocated in the supplied witnesses. | C05, MB01–MB02 |
| Is cote 16's $\mathfrak{sl}_2$ the displayed motivic group action? | The partial-inverse lowering operator is converted explicitly into the weighted $\mathfrak{sl}_2$ operator. On $H^*(\mathbf P^1)$ the Lefschetz action moves the unit line whereas the displayed Tate-group action fixes it; the matrices prove the failure of that particular factorization and give its surviving conjugation and Tate-twist relations. | MB03–MB04, MB03b, MB06 |
| Is the grading its motivic weight cocharacter? | On $H^i(X)$, $\lambda_X(t)=t^{i-d}=t^{-d}w_X(t)$ for $d=\dim X$ and $w_X(t)=t^i$. Their endomorphism conjugations agree; the Tate character gives $\varepsilon\circ w=t^2$, which must be compared with the earlier $\varepsilon\circ j=\mathrm{id}$. | MB05 |
| Which A–D lettering is present? | The operational matches manuscript A→printed A and manuscript C→printed B have supplied witnesses. B→printed D and D→printed C remain provisional; the new scans give no missing definitions. | MB07; table below |
| Does cote 14 carry out the singular-hypersurface programme? | CT16/047 expressly changes to singular hypersurfaces after reporting Serre's objection. The actual cote 14 scans or transcription are absent from this context, so their register summaries remain leads requiring that witness. | MB08, R12 |
| What exact motivic sequence over $\mathbf Q$ is supported? | The new pages contain real-conjugation and cocycle constructions. The arithmetic sequence is checked for rational Nori motives through base change and the Artin inclusion, with Kahn's actual v4 and published locators; it is not assigned to a missing historical formula. | MB09–MB11; S15 table below |
| What changes the real-Frobenius discussion? | The Artin–Tate line $A\otimes\mathbf Q(-1)$ has real Frobenius $+1$ and weight 2, with an explicit algebraic projector. This verifies the objection to the even-Tate assertion on 18/036,038, while the sign Artin line supplies the tensor-square obstruction on 18/035. | RH06–RH13; Appendices A–B |
| What does Oda contribute? | Printed Corollary 5.11 identifies $M(A[p])$ with degree-one de Rham cohomology and identifies the submodule corresponding to the Hodge filtration. It addresses CT54/007's extension-recovery question in that precise abelian setting. | RH17–RH18 |

## The requested “linear statement, non-linear statement” table

For the Hom row, fix smooth proper geometrically connected curves $X,Y$ of genus at least two over one number field $K$, with Jacobians $J_X,J_Y$, geometric groups $\Delta_X,\Delta_Y$, arithmetic groups $\Pi_X,\Pi_Y$ and $G_K=\operatorname{Gal}(\bar K/K)$. For the real row use a smooth projective hyperbolic curve over $\mathbf R$; for the weight row use a hyperbolic curve over a number field and a prime $\ell$. These choices put each displayed map in a specified domain.

| Topic | Linear statement | Non-linear statement | Exact map relating the displayed objects |
|---|---|---|---|
| Tate and anabelian Hom | $\operatorname{Hom}_K(J_X,J_Y)\otimes\mathbf Z_\ell\simeq\operatorname{Hom}_{G_K}(T_\ell J_X,T_\ell J_Y)$, via Faltings's endomorphism theorem applied to $J_X\times J_Y$; Tate gives the finite-field version [F83; T66]. | Dominant curve morphisms correspond to the prescribed open continuous $G_K$-homomorphisms of arithmetic fundamental groups, modulo $\operatorname{Inn}(\Delta_Y)$ [M99, Theorem A]. | $f\mapsto\pi_1(f)\mapsto\pi_1(f)^{\mathrm{ab},\ell}=T_\ell(f_*)$; the second map takes geometric pro-$\ell$ abelianization. **MB13.** |
| Semisimplicity and trivial centres | Rational $\mathbf G_m$-representations split into characters; its conjugation homomorphism has kernel $\mathbf G_m$. Numerical motives also have Jannsen's semisimplicity theorem, connected to homological correspondences by the quotient on morphism spaces [J92]. | For the hyperbolic geometric group, $\Delta\to\operatorname{Inn}(\Delta)$ is an isomorphism, and the arithmetic extension is recovered as $G_K\times_{\operatorname{Out}(\Delta)}\operatorname{Aut}(\Delta)$ [M04]. | $1\to Z(G)\to G\to\operatorname{Inn}(G)\to1$; the two examples compute its kernel. The correspondence quotient is separately specified in **MB12**, and the conjugation comparison in **MB14**. |
| Polarizations and real structures | A specified polarization morphism over $\mathbf R$, $q:V\otimes V\to\mathbf Q(-n)$, gives $q(fx,fy)=(-1)^nq(x,y)$ and $B(x,y)=(2\pi i)^nq(x,Cy)$; the written normalizer relation yields $B(fx,fy)=B(x,y)$ [MSh, (5.4)–(5.5)]. | $\pi_0(X(\mathbf R))$ maps bijectively to geometric-conjugacy classes of continuous sections of $\Pi_X\to\operatorname{Gal}(\mathbf C/\mathbf R)$ in this curve case [Pal]. | A section supplies $\operatorname{Ad}(s(c))$; on dual abelianization, $\chi\mapsto\chi\circ\operatorname{Ad}(s(c))^{-1}$ gives real Frobenius through comparison. Inner conjugation disappears in this action; the entire abelianized section cocycle is not discarded by this calculation. **RH19–RH20; Appendix C.** |
| Weights and cyclotomic normalizers | $\operatorname{Hom}_{G_K}(\mathbf Z_\ell(1),T_\ell A)=0$ for abelian varieties over number fields [S12, Definition 26]. | Stix's inertia criterion uses a closed $I\simeq\mathbf Z_\ell$ in $\Delta_U$ and $N\leq N_{\Pi_U}(I)$ with open arithmetic image and cyclotomic conjugation [S12, Definition 29, Theorem 30]. | Conjugation $N\to\operatorname{Aut}_{\mathrm{cont}}(I)\simeq\mathbf Z_\ell^\times$ must equal $\chi_\ell\circ(N\to G_K)$. The displayed LM6 summaries do not supply that identity. **MB15.** |

## Historical lettering: the supported partial dictionary

| Manuscript letter | Supplied witness | Printed comparison | Result of the comparison |
|---|---|---|---|
| A | CT16/044,047: Lefschetz condition on algebraic classes | Grothendieck 1969 A, algebraic-class clause [G69, p.196] | Operator-level match; printed A also includes its historical hard-Lefschetz clause. |
| B | CT16/044: A plus the index assertion implies B | Printed D, homological and numerical equivalence [K94, §5, p.17] | Provisional: the exact manuscript definition has not been located. |
| C | CT16/048–049: inverse Lefschetz maps represented algebraically | Grothendieck 1969 B [G69, p.196] | Operator-level match. |
| D | CT16/046,048: Künneth and rational characteristic-polynomial role | Grothendieck 1969 C, algebraic Künneth projectors [G69, p.195] | Provisional: the use supports the lead without supplying the definition. |

This table compares the written operators and clauses. It does not silently transport one lettering convention into the frozen text; MB07 records the searches and remaining documentary questions.

## S15: modern group statements with their comparison maps

| Question | Checked result and morphism | Historical comparison still to supply |
|---|---|---|
| Nori and Ayoub | Inverse Hopf-algebra maps $\varphi_A,\varphi_N$ in the paper's PID setup [CG17, Theorem 9.1]. | The specific historical category, coefficients and fibre functors. |
| Pure category | Motivated correspondences give André→pure Nori; Arapura proves equivalence and semisimplicity [A13, 6.4.1, 6.3.3]. | Fullness of algebraic→motivated correspondences. |
| Numerical category | The homological→numerical quotient on correspondences reaches the semisimple numerical category [J92]. | Equality of the kernels for a cohomological realization through that quotient. |
| Hodge realization | The comparison is $C\to\mathrm{MHS}$; A13 labels general fullness Conjecture 7.1.1 and establishes the stated abelian-type case in 7.1.4. | The category on 18/034 itself invokes the Hodge conjectures. |
| Arithmetic sequence over $\mathbf Q$ | $1\to G_{\mathrm{Nori}}(\bar{\mathbf Q})\to G_{\mathrm{Nori}}(\mathbf Q)\to\underline{\operatorname{Gal}(\bar{\mathbf Q}/\mathbf Q)}\to1$, with the first arrow dual to base change and the last to the Artin inclusion [K25]. | A historical occurrence and its fibre-functor convention; no such formula is located on the current leaves. |
| Integral lattices | A chosen integral group isomorphism transports a specified representation and lattice. | The actual lattice choices, existence assertion on 18/055 and finite-index assertion on 18/049, treated in P06–P13 and MB16. |
