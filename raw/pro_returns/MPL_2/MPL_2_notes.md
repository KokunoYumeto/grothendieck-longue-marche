# MPL_2 — Research notes

## Scope, evidence and status

These notes concern **cote 2, scans 002–045, excluding the three omitted blank scans 006, 027 and 031**. The primary reader completed the transcription and the second visual reading of all 41 retained sheets, recorded the 42 SHA-256 hashes, and froze the transcription at **2026-11-16 20:56:22 UTC**, before opening the context. Research calculations, literature comparisons and alternative interpretations below have not changed any frozen transcription file.

The supplied context contains only `README.md` and `notes/RESULTS_STATE.md`. The README places this cote in Book I, I.X, intersections/Chern classes/Riemann–Roch, at package 246, rank 25, and asks the standing questions; it supplies no neighboring transcript. The register has **zero matching open, settled, intake, returned-package or planning entries** from the user's own project. Its unrelated LM4/LM7 referee list does not establish anything about this cote. The three relevant rows are **Hua, findings register** imports explicitly described as AI-produced, with intake status “new to us: our package for this cote is waiting”; the comparisons here do not promote them to reviewed results.

Each individual note states its scan and kind; own ideas carry confidence and the reason for it. Brief quotations refer to the frozen transcription: a reading marked doubtful there remains provisional here, even when only its readable portion is quoted. “No context match” means no relevant counterpart in the two supplied files, not absence from the archive or literature. Per-note searches were actually run and are retained in `records/context_search_primary.md`, `records/context_search_chern_curves.md`, `records/context_search_lambda.md`, `records/context_search_supports.md`, `records/context_search_standing.md` and `records/context_search_bridge.md`; matching words alone were not treated as mathematical agreement.

The register contains **80 individual substantive notes**, followed by **10 entries for explicitly unverified steps** and **9 title/pagination entries**. Longer independent calculations are retained in the accompanying research records so that the individual notes remain short. Line locators refer approximately to the frozen page fragment or the position on the scan, not to a new editorial line numbering of the manuscript.

### Assessment of the three imported findings

| Supplied register ID | Supplied source scans | What this package adds or changes | Status retained |
|---|---|---|---|
| **2-chern-ring-gamma-comparison** | 021, 022, 029, 030 | The factorial comparison needs its positive-degree scope, the sign discrepancy between 021 and 022 recorded, and the modified product on the return map's target on 030. The explicit λ-homomorphism definition and the shorter relation list on 029 require separate treatment. | Unreviewed imported lead; conditional calculations and primary-literature comparisons below, no claim of novelty. |
| **2-chern-ring-not-injective-pn** | 022 | The sheet answers its own question “Non,” specifies a single chosen geometric generator, and shows how adding `nL−1` changes the universal ring. The exact small case and homogeneous torsion calculation make the example testable. | Unreviewed imported lead; the dependence on the chosen geometric family is essential. |
| **2-trivial-total-chern-class** | 010, 012, 014 | The register describes the cancelled hypersurface setup; the live elliptic point-difference example is verified integrally. Rank zero, the zero/unit convention and the distinction between a sufficient factorial bound and minimal dimension are recorded separately. | Unreviewed imported lead; attribution and hypotheses refined, with a conditional verification of its stated Cartier-divisor version. |

## 1. Curves, the preliminary class group and integral structure

### A01 — Cote 2, scans 003–004, definitions and proposition — unproved claim

The assertions “C'est l'annulateur de E₀,” “E=Φ+D,” and “Φ∩D=0” concern a preliminary group of sheaf classes before the final exact-sequence quotient, whose restricted relations are difficult to read. The familiar rank–determinant description of the final K-group therefore does not by itself prove every intermediate equality on these sheets; a proof must specify the initial relation subgroup, the product, and the map from divisors before identifying its kernel with principal divisors. The adjacent proposition is a proposed reduction of relations, not a supplied proof of those identifications.

Context: no topical counterpart in supplied `README.md` or `notes/RESULTS_STATE.md`, and no neighboring scan; search A01 in `records/context_search_primary.md`.

### A02 — Cote 2, scans 003–004, Φ_N definition — reading question

Scan 003 reads provisionally “Quotient de Φ par le sous-groupe,” but then writes Φ/Φ_N, while 004 writes Φ∩N=Φ_N. Those later occurrences suggest that Φ_N is intended as the relation subgroup or ideal, so “sous-groupe” or a different scope for “Quotient” is a mathematical alternative to investigate against another witness. The frozen word “Quotient” remains untouched: this is a consistency question, not a licence to replace visible ink.

Context: no Φ_N or quotient-definition counterpart in either supplied context file; no neighboring scan.

### A03 — Cote 2, scan 004, formula (1) and lower diagram — self-flagged / unproved claim

The diagram places a literal “?” on the branch from L=D∩N to N; its scope is not expressly given, whereas “Pour vérifier(1), il suffit…” reduces the numerical RR assertion to point sheaves and the structure sheaf. That reduction needs the preceding description of generators and a setting in which Euler characteristics are finite—properness or an explicit replacement—which the isolated opening “X courbe non singulière” on 003 does not state. On a smooth proper connected curve, the displayed degree expression becomes deg(F)+rank(F)(1−g), but this standard specialization does not resolve what the diagram's question mark targets (Borel & Serre, 1958, §§7–9).

Context: `README.md` places the cote under Riemann–Roch but supplies no other scan; `notes/RESULTS_STATE.md` contains no entry about this curve reduction or question mark.

### A04 — Cote 2, scan 005, first half — unproved claim

The sheet asserts “L'idéal d'augmentation…est de carré nul,” vanishing γ^i(x) for i≥2 on augmentation-zero elements, and cl(E)=[rg(E),det(E)] under its noetherian, ample-line-bundle, dimension≤1 assumptions. The rank–Picard description is consistent with the dimension-one statement explicitly used by Pedrini and Weibel (1994, Appendix A, p. 404), but the λ-structure needs to be checked as well: once reduced classes are identified with [L]−1 and their products vanish, γ_t([L]−1)=1+([L]−1)t supplies the claimed higher vanishing. This adds a precise proof route to the bare assertion and keeps connected components, irreducible components, and the homological K-group separate.

Context: neither supplied context file has a rank–Picard or dimension-one K entry; no neighboring scan.

### A05 — Cote 2, scans 007–008, μ_i and the class of 1 — own idea

The phrase “seul invariant de la situation” in the zero-dimensional case is naturally tested on R=k[ε]/(ε^m): finite projective modules are free, finite modules have a composition series with residue-field factors, and the map K₀(R)→G₀(R) is multiplication by m under rank and length. Thus the sheet's μ=length(O_X) detects a genuine integral obstruction even when the two groups are abstractly Z; for m>1 its cokernel is Z/m. Confidence: high, because the calculation follows directly from a length-m filtration of R, and it distinguishes the structure-sheaf map from the abstract group identifications.

Context: neither supplied context file contains this length/Cartan-map test; no neighboring scan.

### A06 — Cote 2, scans 007–008, splitting and δ — own idea

The author calls the homological splitting “non naturel” and writes δ=1−Σμ_i1_i; replacing the chosen lifts 1_i by 1_i+e_i with e_i∈K_(0) changes δ to δ−Σμ_ie_i. Consequently the residue of δ in K_(0)/(Σ_i μ_iK_(0)) is independent of those lift choices, even though δ itself is not. For finitely many components this quotient is K_(0)/dK_(0), where d is the greatest common divisor of the μ_i, so relatively prime generic multiplicities force the residue to vanish. Confidence: high for this elementary abelian-group consequence of the displayed formula, and medium for its usefulness as a geometric invariant until functoriality of the chosen filtration and base-change maps is specified.

Context: no splitting, residual-class, or δ entry in either supplied context file; no neighboring scan.

### A07 — Cote 2, scan 008, lower cancelled construction — withdrawn in the same text

The attempted “On se définit un hom” and c_•=ch_• construction are crossed out and end with an unfinished minus sign, while the upper formula for the structure-sheaf map remains live. Scan 007 already explains why a splitting-based formula would lack naturality under base change, which supplies a plausible internal motivation without proving why the author cancelled this particular version. Any later use should cite 007–008 together and distinguish the live map from the withdrawn proposed character.

Context: no matching formula in supplied `README.md` or `notes/RESULTS_STATE.md`; no neighboring scan.

### A21 — Cote 2, scan 003, multiplication convention — own idea

For X=P¹_k and a k-rational closed point p, the point-sheaf class [O_p] lies in the rank-zero part and is nonzero in the final K-group, since its Euler characteristic is 1, while ordinary tensor product gives O_p⊗O_p≃O_p. The locally free resolution 0→O(-p)→O→O_p→0 instead gives Tor₀(O_p,O_p)≃Tor₁(O_p,O_p)≃O_p and alternating class 0, showing why the asserted annihilator property needs a derived product or an equivalent convention. Confidence: high for this global test, medium for reconstructing the product on the preliminary ring E from it; compare the Tor-product construction in Borel and Serre (1958, §§4–5).

Context: no Tor-product or annihilator counterpart in either supplied context file; no neighboring scan.

## 2. Torsion and trivial total Chern classes

### CC01 — Cote 2, scan 010, left square and composition — Unproved claim

The label “injectif” is supported on the sheet by `p_*i_*(x)=(pi)_*x=x`, which supplies a left inverse to the constant-section pushforward in coherent K-theory under the usual proper-pushforward conventions. This identifies the correct nonvanishing argument for the later torsion example: it uses the projection's direct image, not a claim that restriction to the section is injective (Borel & Serre, 1958, §5d). **Context:** `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, already asserts nonvanishing; this page supplies its key step, without turning that unreviewed register row into an independently established result.

### CC02 — Cote 2, scans 010–012, Chern product and Q-polynomials — Unproved claim

The leading term `1+(-1)^{r-1}(r-1)! eta^r` and the later `Q_1^{(r)}(c^1)=-rc^1` point to two distinct factorial coefficients: the rank term has `(r-1)!`, while a rank-zero curve class contributes `r!` one degree later. An integral product expansion of the written binomial sum verifies this distinction, so the two coefficients should not be conflated by a rational Chern-character argument (appendix A of `records/research_chern_curves.md`). **Context:** `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, retains only the stronger `(r-1)!` annihilation condition; these calculations refine its sufficient criterion.

### CC03 — Cote 2, scan 012, final warning — Unpursued implication

“s'il y a de la torsion dans A(X), l'hom (i_*)_r est non injectif” needs a statement about the order and degree of that torsion relative to the actual coefficients for the fixed r. On the abstract graded ring `A=Z⊕(Z/5)α`, `α²=0`, the rank-zero part for r=2 is multiplication by 2 and is injective, so an argument based only on the presence of torsion is insufficient. This is an abstract algebraic diagnostic, not an assertion that a smooth scheme with this Chow ring occurs in the manuscript's geometric family or a geometric counterexample under its unstated conventions. **Own diagnostic confidence: high** for that limited conclusion, by the integral calculation in appendix A of `records/research_chern_curves.md`; **context:** `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, supplies an explicit annihilation hypothesis that is safer than the unrestricted wording.

### CC04 — Cote 2, scan 012, first cases display — Reading question

The frozen cases display for `Q_i(---)` has no `eta^r` factor in its second branch, although the following total-class formula includes that factor and calls `Q_{i-r}^{(r)}` a coefficient polynomial. It is worth checking whether this is deliberate coefficient extraction or a dropped factor; neither interpretation licenses inserting it into the frozen transcription. **Context:** the per-note search found no `Q_i`, isobaric-weight, or eta passage in README.md or `notes/RESULTS_STATE.md`, and no neighbouring scan was supplied.

### CC05 — Cote 2, scan 014, crossed upper block and live N.B. — Withdrawn in the same text

The hypersurface proposal beginning “Soit donc Y une hypersurface” is crossed out on the same sheet, whereas the live replacement uses “x=(a)-(0)” on an elliptic curve. **Context:** `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, describes `i_!(O_Y)` and thus preserves the withdrawn setup rather than accurately identifying the final written example; a nonzero effective divisor of torsion class cannot occur on a proper smooth curve, since its degree is positive. Nevertheless, under a smooth ambient-space/effective-Cartier-divisor interpretation the register's conditional vanishing assertion can be checked by the integral calculation in appendix B of `records/research_chern_curves.md`, so the necessary correction is to its attribution and hypotheses, not a blanket mathematical rejection.

### CC06 — Cote 2, scan 014, live elliptic example — Unproved claim

The example “a+a=0, a≠0” works over C: take a nontrivial 2-torsion line bundle L on an elliptic curve E, put `x=[L]-1` with `α=c_1(L)≠0`, and push it along a constant section into `E×P^3`. The direct integral formula `c(i_!x)=1-6αh^3=1`, together with `p_!i_!x=x≠0`, verifies the intended vanishing of all positive Chern classes without discarding torsion; x is the rank-zero divisor-class representative of the written point difference. **Context:** this checks the central phenomenon in `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, while replacing its description by the sheet's live example; no novelty or reviewed-status claim is made.

### CC07 — Cote 2, scans 012 and 014, epsilon term versus N.B. — Own idea

The N.B. assertion that all `C^i(x)` being annihilated implies vanishing after pushforward requires a rank-zero condition if `C^i` means positive Chern classes: the visible `epsilon(x)` term on 012 remains. Indeed `x=[O_X]` has zero positive Chern classes, whereas `c_r(i_!x)=(-1)^{r-1}(r-1)!h^r` is nonzero for the section into a projective-space factor. **Confidence: high**, because this is the rank term of the sheet's own formula and is also verified by the Koszul resolution; **context:** Hua **2-trivial-total-chern-class** in `notes/RESULTS_STATE.md`, scans 010/012/014, implicitly has rank zero through `O_Y`, but the live general sentence on 014 needs that qualification or an explicit augmented-class convention.

### CC08 — Cote 2, scans 010/012/014, zero versus unit — Reading question

The frozen text alternates formulas with initial 1 and the statement `Ctilde(y)=0`; in an augmented Chern ring whose addition is multiplication of total classes, additive zero is represented by `(0,1)`, so these need not express opposite mathematical claims. Grothendieck's published construction explicitly uses `Z×(1+A_+)` with that additive convention (Grothendieck, 1958, §4,2°, pp. 147–149), but it is external comparison rather than permission to rewrite 014. **Context:** `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, writes total Chern class 1 and should identify this convention rather than silently substituting 1 for the manuscript's 0.

### CC09 — Cote 2, scans 012/014, factorial bound — Own idea

For a rank-zero line-bundle difference on a smooth curve, the exact integral coefficient is `(-1)^r r!αh^r`, so the same elliptic 2-torsion construction already gives a nonzero class with trivial total Chern class on `E×P^2`. **Confidence: high**, because the finite-difference computation in appendix A of `records/research_chern_curves.md` is an identity over the integers before torsion specialization. **Context:** `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, scans 010/012/014, says “possible only for r≥3”; this is correct for its stated stronger hypothesis `(r-1)!α=0`, but it is not a minimal-dimension claim for the underlying phenomenon, and the present observation is our extension rather than something the page asserts.

## 3. Equivariant modules and symmetric tensor powers

### A08 — Cote 2, scan 016, restriction of extension — own idea

The asserted “isom…fonctoriel non canonique” u* u_*(F)≃F^(G′/G) needs an underlying-module qualifier if u_* means ordinary induction: for H=C₃⊂S₃ and a nontrivial complex character χ, restriction of the induced representation is χ⊕χ⁻¹, not χ⊕χ. As complex vector spaces the two sides are isomorphic after choosing coset representatives, whereas the H-actions distinguish them; this is the elementary normal-subgroup case of the restriction/induction framework (Serre, 1977, §§7.1–7.3). Confidence: high under the usual induction interpretation, because a generator of C₃ has eigenvalues ζ and ζ⁻¹ on the induced module, but medium as an interpretation of the abbreviated sheet, which may suppress a forgetful functor.

Context: neither supplied context file has an induction or Mackey entry; no neighboring scan.

### A09 — Cote 2, scan 016, stability of free subcategories — own idea

The claim “elles sont stables pour les foncteurs précédents” follows “Lorsque u est injectif,” so whether injectivity remains in force is ambiguous; even for the inclusion 1→Z, restriction of the rank-one free k[Z]-module k[Z] is infinite-dimensional over k and therefore does not preserve finite-type freeness. For subgroup inclusions restriction preserves group-algebra freeness, and finite index suffices for the finite-type version, while extension of scalars preserves finite free modules; under the broader arbitrary-homomorphism interpretation, C₂→1 already sends the free k-module k to a nonfree trivial k[C₂]-module. Confidence: high for these coset-basis and dimension checks, and medium for the scope of the written hypothesis; the subsequent finite symmetric-group inclusions satisfy the needed index condition.

Context: no corresponding stability hypothesis or counterexample in either supplied context file; no neighboring scan.

### A10 — Cote 2, scan 017, projection and exterior-operation promise — unproved claim

The “formule de projection” can be verified for induction by g′⊗(v⊗w)↦(g′⊗v)⊗g′w, with inverse using g′⁻¹ on the second factor, so its equivariance and balancing are concrete checks distinct from the problematic splitting on 016. The promise to deduce Λ^i and other tensor operations “plus bas” is only partially pursued on 018–019 through symmetric tensor powers: descent through short exact sequences still requires the tensor-power filtration, and extraction of alternating representations by averaging would require invertibility of i!. Atiyah (1966, §2, Proposition 2.2) provides a later complex-vector-bundle comparison using signed graded tensor powers; it is not an integral proof for every ringed topos in 016.

Context: no projection-formula or promised-operation counterpart in either supplied context file; no neighboring scan.

### A11 — Cote 2, scan 018, induced product — unproved claim

“Commutative et associative dans un sens évident” is justified by conjugacy of the two block inclusions and by transitivity of induction from S_p×S_q×S_r into S_(p+q+r). The result is naturally a coherent family of isomorphisms of categories, with the ordinary commutative graded ring obtained only after an appropriate Grothendieck-group construction. This is a structural parallel with Atiyah's symmetric-group construction (1966, §1), without a historical priority claim or an assertion that the manuscript supplies all coherence checks.

Context: neither supplied context file discusses this categorical induced product; no neighboring scan.

### A12 — Cote 2, scans 018–019, iterated tensor powers — unpursued implication

The cancelled T^n(F) construction for an S_m-object naturally has the fuller wreath-product action S_m^n⋊S_n on n blocks of m letters, although the written S_m×S_n also acts legitimately through the diagonal S_m inside S_m^n. For the surviving T^m(T^n(F)) the corresponding full action instead uses S_n^m⋊S_m on m blocks of n letters; its written w_(m,n):S_m→S_(mn) can be the outer block-permutation inclusion after forgetting the inner S_n-symmetries. These are compatible candidate reconstructions, so the cancellation does not establish that the direct-product action was impossible, and the retained versus forgotten symmetry must be stated explicitly. Confidence: high for the two permutation actions and their restrictions, medium for the reconstruction of the author's intended convention because the sheet does not state the omitted inner action.

Context: no wreath-product, tensor-power, or w-map comparison in either supplied context file; no neighboring scan.

### A13 — Cote 2, scan 019, admissibility revision — withdrawn in the same text

Reading “somme de faisceaux” as a direct sum, the cancelled requirement that Young-subgroup modules be “libres sur O_X(S_p1×…×S_pr)” is replaced by O_X-locally-free modules “triviaux” for those subgroups. The replacement admits tensor powers locally: on an open set carrying a basis, words of length n have S_n-orbits with Young stabilizers, and each orbit module is induced from the stabilizer's trivial representation. In particular T^n(O_X)=O_X with trivial S_n-action is included, whereas the cancelled direct-sum condition would make every induced summand group-algebra-free and exclude this rank-one example for n≥2; if “somme” instead permits arbitrary quotient-generated sums, that exclusion would need reconsideration. Confidence is high in the local orbit calculation, but the sentence defining admissibility locally lies inside the deleted block, so a global decomposition or a retained locality convention remains unproved.

Context: no admissibility or Young-subgroup entry in either supplied context file; no neighboring scan.

## 4. Universal Chern rings and the gamma filtration

### L01 — The geometric family is part of the input

**Cote/scans:** 2/021, lines 4, 9, 45; 028, lines 6–45; 029, lines 28–32. **Kind:** unpursued implication. **Context:** bears on both Hua IDs; qualifies the formulation of the first and is essential to the second.

The phrase “plus la famille des $E_s$ est grande … plus $CK$ devient petit” on scan 029 makes the chosen family part of the universal problem. Closure under the indicated positive operations must be distinguished from replacement by every element that is algebraically geometric in $K$: the warning on scan 029 and the added $nL-1$ on scan 022 give a concrete difference. Consequently write $C(K,S)$ in a modern restatement, even though the manuscript usually abbreviates this to $CK$.

### L02 — The displayed relations do not by themselves enforce lambda compatibility

**Cote/scans:** 2/028, lines 33–35; 029, lines 6–13. **Kind:** own idea / counterexample to an overbroad restatement. **Context:** bears on **2-chern-ring-gamma-comparison**; contradicts a literal exhaustive reading of that entry's abbreviated relation list. **Confidence:** high, because the explicit countermodel is verified in Appendix A of `records/research_lambda.md`.

Scan 028 explicitly requires an “hom de $\lambda$-anneaux”, whereas the displayed list on scan 029 contains only unit, Whitney, product, and selected rank bounds. Those displayed relations alone admit an augmented ring map from $\mathbb Z[x,y,y^{-1}]$, with $\lambda^2x=y$, to the Chern ring of $\mathbb Z[\epsilon]/\epsilon^2$ sending $x\mapsto[2,1]$ and $y\mapsto[1,1+\epsilon]$, which is not a lambda homomorphism. The intended universal problem must retain lambda compatibility; the explicit gamma-compatibility relations in SGA 6, V, 6.14, p. 358, confirm the distinction (Berthelot, 1971).

### L03 — A sign changes between the proposition and its proof

**Cote/scans:** 2/021, lines 70–74; 022, lines 14, 18, 23, 27, 31, 39. **Kind:** withdrawn/corrected in the same text, with the qualification that the earlier line is not explicitly struck out. **Context:** **2-chern-ring-gamma-comparison** uses the proof's sign and omits this internal discrepancy.

Proposition 2 on scan 021 writes $(-1)^i(i-1)!$, while the proof and conclusions on scan 022 consistently write $(-1)^{i-1}(i-1)!$. The latter is the sign supported by the calculation, and the degree-one case already distinguishes the two. Preserve both manuscript readings and record the change as an internal discrepancy; do not silently replace the proposition by its proof.

### L04 — Precise comparison, including the degree-zero exception

**Cote/scans:** 2/021–022; 029, lines 21–28; 030, lines 8–15. **Kind:** unpursued implication / narrowed claim. **Context:** **2-chern-ring-gamma-comparison**, supported with qualifications.

The corollary “Son noyau est un groupe de Torsion” follows degreewise from the two composites being $d_i\operatorname{id}$, where $d_i=(-1)^{i-1}(i-1)!$ and $i\geq1$. More precisely, for the intended lambda-theoretic universal ring, $\phi_i:C^i(K,S)\twoheadrightarrow\operatorname{gr}^i_\gamma K$ has kernel annihilated by $(i-1)!$, hence is an isomorphism for $i=1,2$ and after rationalization in every positive degree. Degree zero must be treated separately: for the stated $\mathbb Z$-augmentation and the universal graded ring generated in positive degrees it is $\mathbb Z\to\mathbb Z$, not an instance of a formula containing $(-1)!$.

### L05 — The return map lands in a ring with a different product

**Cote/scan:** 2/030, lines 8–10 and 15. **Kind:** unpursued implication. **Context:** qualifies the “map $\psi$ back” in **2-chern-ring-gamma-comparison**; no exact `A!` or `A^!` match occurs in the supplied context.

The marginal restriction “additivement … en degrés $\ne0$” is essential: the coefficient identification of $\operatorname{gr}_{\deg}\widetilde A$ with $A$ does not preserve the ordinary product. For $a\in A^i,b\in A^j$, $i,j>0$, its product is $a\star b=-\frac{(i+j-1)!}{(i-1)!(j-1)!}ab$, so $\psi$ is multiplicative into this modified ring and only a graded additive map when its target is identified with ordinary $A$. Appendix C of `records/research_lambda.md` checks the formula and the factorial composites; the formula is also SGA 6, V, (6.5.3), p. 349 (Berthelot, 1971).

### L06 — The free-ring reduction needs an integral filtration calculation

**Cote/scans:** 2/021, lines 11–40; 022, lines 29–39. **Kind:** unproved claim. **Context:** **2-chern-ring-gamma-comparison**; the manuscript adds the free-ring argument absent from the register summary.

The statements “comme on vérifie … facilement” and “$\varphi_B$ est bijectif” require an integral calculation, not merely a rational splitting argument. With $z_{s,i}=\gamma^i(X_s-n_s)$, the free finite-rank lambda ring has polynomial gamma coordinates, with the determinant units inverted, and its gamma filtration is the weight filtration $\operatorname{wt}z_{s,i}=i$. Appendix D of `records/research_lambda.md` explains why this identifies its associated graded with the polynomial ring and why a surjective augmented lambda map transports the filtration to $K$.

### L07 — Multiplicativity does not complete the lambda-homomorphism verification

**Cote/scans:** 2/021, lines 50–57; 023, lines 18–42. **Kind:** unproved claim. **Context:** **2-chern-ring-gamma-comparison**; no separate context result covers the verification.

“Vérification immédiate!” asserts that the completed natural Chern class is a lambda homomorphism, while scan 023 explicitly works through the multiplication formula and its lowest-weight term. A complete proof must additionally verify compatibility with iterated exterior/gamma operations; the multiplication calculation alone does not supply it. The full statement appears as SGA 6, V, Proposition 6.8, pp. 353–354 (Berthelot, 1971).

### L08 — The projective-space noninjectivity has a precise homogeneous witness

**Cote/scan:** 2/022, lines 41–56. **Kind:** own idea — verification of the manuscript's counterexample. **Context:** **2-chern-ring-not-injective-pn**, supported and sharpened. **Confidence:** high, from the explicit universal calculation in Appendix B of `records/research_lambda.md`.

The answer “Non” to “Est-ce que $\varphi_K$ est tjrs bijectif ???” is justified for $K=\mathbb Z[L]/(L-1)^n$, with only the family generated geometrically by $L$, when $n\geq3$. The complete relation is coefficientwise $P_n(\xi)=1$, where $P_n(z)=\prod_{j=0}^{n}(1+jz)^{(-1)^{n-j}\binom nj}$, and its first relation gives $C^n(K,\{L\})\cong\mathbb Z/(n-1)!$, whereas $\operatorname{gr}_\gamma K=\mathbb Z[\bar y]/\bar y^n$. In particular, for $n=3$, the exact ring is $\mathbb Z[\xi]/(2\xi^3,\xi^4)$, so the nonzero class $\xi^3$ is an explicit element of the kernel.

### L09 — Adjoining the tangent-class element really changes the chosen family

**Cote/scans:** 2/022, line 58; 029, lines 28–32. **Kind:** own idea — verification / unpursued implication. **Context:** adds to **2-chern-ring-not-injective-pn** and qualifies **2-chern-ring-gamma-comparison**. **Confidence:** high, by the rank and coefficient arguments in Appendix B of `records/research_lambda.md`.

The margin “si on adjoint … $nL-1$” imposes $c^n(nL-1)=\xi^n=0$, because $c(nL-1)=(1+\xi)^n$, giving $C(K,\{L,nL-1\})=\mathbb Z[\xi]/\xi^n$. For $n\geq3$, $nL-1$ is geometric but is not generated from $L$ by the stated positive operations and inverses of rank-one elements; thus this is a genuine enlargement of the family. This also furnishes the example promised by scan 029: an admissible Chern theory for the smaller family can have a nonzero high Chern component on another geometric element.

### L10 — Finite exterior degree only forces factorial annihilation of high Chern components

**Cote/scan:** 2/025, lines 4–10. **Kind:** unproved claim, with a verifying example. **Context:** bears on both Chern-ring Hua IDs; the supplied context contains no separate entry for this proposition.

The replacement of the deleted $x^i=0$ by “$(i-1)!x^i=0$” records an important integral distinction. A finite exterior degree in $\widetilde A$ forces factorial annihilation of high Chern coefficients, not their vanishing in arbitrary torsion coefficient rings. The $n=3$ example in appendix B of `records/research_lambda.md` realizes the distinction: the image of $3L-1$ is geometric of rank two but has the nonzero coefficient $\xi^3$, killed by $2!$.

### L11 — The next-degree torsion criterion can be checked in a genuinely truncated ring

**Cote/scan:** 2/025, lines 12–16. **Kind:** own idea — verification with a hypothesis clarification. **Context:** no exact context match for the truncated criterion; it bears on the torsion mechanism in **2-chern-ring-not-injective-pn**. **Confidence:** high under the explicit truncation stated here.

The assertion “il faut et il suffit … $n!x^{n+1}=0$” is valid for a graded ring with all components above $n+1$ zero, as the finite-difference calculation in Appendix E of `records/research_lambda.md` shows. Interpret the manuscript's $A^{n+2}=0$ as a degree-cutoff/filtration condition for this verification; vanishing of just one homogeneous component would be a weaker statement and is not substituted silently. The calculation isolates the first degree in which torsion can let a geometric element have a Chern coefficient above its rank.

### L12 — The live unshifted gamma expression needs a reading/meaning check

**Cote/scan:** 2/025, lines 20–35. **Kind:** reading question / literal counterexample. **Context:** no exact counterpart in the context; relevant to the hypotheses of **2-chern-ring-gamma-comparison**. **Confidence:** high for the counterexample under the package's standard gamma convention; no confidence judgment about the original ink is added here.

The live corollary has $\gamma^m(x)$, with the rank subtraction deleted, whereas its subsequently deleted proof uses $\gamma^m(X-n)$. Read literally with $n=\varepsilon(x)$, it fails for $K=\mathbb Z[L,L^{-1}],x=L,n=1,m=2$: $\gamma^2(L)=L$, while the higher exterior powers vanish and weight-at-least-three gamma terms lie in $(L-1)^3$. The shifted expression $\gamma^m(x-n)$ does belong to the ordinary ideal generated by $\lambda^j(x)$, $j>n$, directly from the generating-function identity in Appendix F of `records/research_lambda.md`; neither this observation nor the deleted proof authorizes a change to the frozen transcription.

### L13 — The determinant condition is redundant under the full definition

**Cote/scan:** 2/028, lines 25–43. **Kind:** self-flagged question, with a conditional answer. **Context:** no determinant match in the supplied context; bears on **2-chern-ring-gamma-comparison**.

The words “conséquence des autres??” are answered affirmatively when “the others” include the full lambda-homomorphism requirement and the selected rank bound. Indeed, if $c(E)=[n,1+a_1+\cdots+a_n]$, then $c(\lambda^nE)=\lambda^n c(E)=[1,1+a_1]$, giving $c^1(E)=c^1(\det E)$. This is SGA 6, V, Proposition 6.6.1(ii), pp. 350–351; it fails for the weaker relation list, as Appendix A of `records/research_lambda.md` shows (Berthelot, 1971).

### L14 — The filtration question has an answer under the stated generating hypothesis

**Cote/scan:** 2/029, line 30; compare 021, lines 4, 31–45, and 023, lines 12–16. **Kind:** self-flagged question / own verification. **Context:** **2-chern-ring-gamma-comparison** mentions the gamma filtration but does not record this question. **Confidence:** high, because Appendix D of `records/research_lambda.md` supplies a free-lambda-ring and quotient argument.

“À voir … [si les $E_s$ engendrent] ???” asks whether gamma monomials in all augmentation-zero elements can be replaced by gamma monomials in the chosen generators. For a special augmented lambda ring ring-generated by the stated finite-rank geometric $E_s$, the answer is yes: the canonical gamma filtration is the image of the free ring's weight filtration. This addresses the filtration only; it does not imply that enlarging the admissible geometric family leaves the universal Chern ring unchanged.

### L15 — The first possible prime obstruction follows from the comparison

**Cote/scans:** 2/022, lines 37–58. **Kind:** own idea / unpursued implication. **Context:** bears on both Hua IDs; the precise prime-by-degree bound has no matching context entry. **Confidence:** high, from the factorial annihilator and Appendix B of `records/research_lambda.md`.

The factorial comparison implies that the $p$-primary part of the kernel is zero in degrees $i\leq p$. The smaller-family example with $n=p+1$ has a nonzero $p$-primary kernel in degree $p+1$, since $C^{p+1}\cong\mathbb Z/p!$. This is a useful sharpness test for the degree bound in this family-dependent setting, not a claim of a new theorem.

### L16 — The unfinished proposition is explicitly withdrawn

**Cote/scan:** 2/022, line 60. **Kind:** self-flagged / withdrawn in the same text. **Context:** no exact context counterpart; related to both Hua IDs through the admissible-family issue.

The struck proposition begins “à prouver directement” and starts an equivalence concerning the chosen geometric family, but its second condition is not completed in the frozen text. It is evidence of an unfinished proof obligation and a withdrawn formulation. Do not reconstruct a theorem from it or use it to erase the family distinction subsequently made on scan 029.

### R01 — Cote 2, scans 021/022/028/029/030 — Unpursued implication / literature comparison

The marginal “un seul générateur X_s=L” on scan 022 distinguishes its smaller-family construction from Mackall's $B(X)$, whose Proposition 2.1 imposes rank bounds for every finite-rank vector bundle and injectivity under projective-bundle pullback. His Theorem 4.1 gives a close factorial comparison, but does not identify these two universal problems; the manuscript's addition of the tangent-class element on 022 already changes its chosen input family (Mackall, 2020, Proposition 2.1 and Theorem 4.1). This makes the imported literature pointer useful for comparison without establishing novelty from its “candidate” or “unsearched” labels. Confidence: high in the distinction, because the stated universal properties were compared directly; no historical dependency is inferred.

**Context:** `notes/RESULTS_STATE.md`, Hua, findings register, **2-chern-ring-gamma-comparison**, scans 021/022/029/030, already mentions Mackall's scheme-based construction, while **2-chern-ring-not-injective-pn**, scan 022, singles out the smaller family; this note develops that existing lead and preserves both rows' unreviewed intake status. Search R01 is recorded in `records/context_search_bridge.md`; no neighboring transcript was supplied.

## 5. Supports, relative perfectness and covariant characters

### S01 — Cote 2, scan 033 — Definition distinction; relative versus intrinsic perfection

**Kind:** reading question / own idea.

**Anchor:** “parfaits rel. à f”; $D^\bullet_{\mathrm{parf}}(i_n)$.

Relative perfection for a closed immersion into a Noetherian ambient scheme is tested by the pushed-forward complex, and is not the condition of being perfect intrinsically on the infinitesimal neighbourhood (Alonso Tarrío et al., 2023, Corollary 4.2). Our diagnostic $A=k[t]$, $B_n=A/(t^n)$, $n\ge2$, shows that $k$ is perfect over $A$ but has an infinite periodic free resolution over $B_n$, so substituting $\operatorname{Perf}(Z_n)$ changes the written category. Context check S01 found no relevant object, scan, or entry ID in either context file; confidence in this distinction is high because the two projective dimensions are explicitly calculable (Appendix A of `records/research_supports.md`).

### S02 — Cote 2, scan 033 — Unproved assertion; finite-stage Ext test

**Kind:** unproved claim / own idea.

**Anchor:** “le foncteur est pl. fidèle.”

The assertion concerns the filtered limit, not each $Ri_{n*}$: already $\operatorname{Ext}^1_k(k,k)=0$ whereas $\operatorname{Ext}^1_{k[t]}(k,k)=k$, represented by the nonsplit extension with middle term $k[t]/(t^2)$. At a thicker stage $B_n$, $n\ge2$, the nonzero higher Ext groups also show that the individual derived pushforward need not be faithful, even though their extra classes can die under transition. This is our high-confidence diagnostic of the work the limit must do, not a counterexample to the written limit claim; context search S02 found no relevant result or ID in **context/README.md** or **context/notes/RESULTS_STATE.md**.

### S03 — Cote 2, scan 033 — Conditional reconstruction of the full-faithfulness claim

**Kind:** own idea — conditional proof.

**Anchor:** $\operatorname{Lim}_nD^\bullet_{\mathrm{parf}}(i_n)\to D_Z(X)$.

For $X=\operatorname{Spec}A$ with $A$ Noetherian and $Z=V(I)$, our reconstruction gives $\varinjlim_n\operatorname{Ext}^q_{A/I^n}(M,N)\simeq\operatorname{Ext}^q_A(M,N)$ for finite modules killed by powers of $I$, and consequently the expected filtered categorical comparison after restricting to complexes perfect over $A$. The proof uses the equivalence between derived $I$-power torsion modules and complexes with torsion cohomology (The Stacks Project Authors, n.d., Tags 0955 and 06UP), together with finiteness of the data in bounded complexes and roofs; Appendix B of `records/research_supports.md` records the actual argument. Confidence is high for this stated affine Noetherian version, but the page's unrestricted “préschéma” formulation, the precise meaning of its categorical limit, and the target notation $D_Z(X)$ require additional conventions before this argument supplies a proof. Context search S03 found no corresponding own entry; the torsion hit **Hua, findings register, 2-chern-ring-not-injective-pn** concerns scan 022 and a different Chern-ring problem, so does not settle this statement.

### S04 — Cote 2, scans 033,035 — Construction condition; families of supports

**Kind:** unproved claim — construction condition.

**Anchor:** “une famille $\Phi$” and the limit over $Z\in\Phi$.

A customary family of supports consists of closed subsets closed under taking closed subsets and finite unions; the latter condition makes the displayed inclusion-indexed limit filtered and permits adding classes carried by different supports. This is a condition to make the proposed construction precise, not a claim that the author intended an arbitrary undirected collection. Context search S04 found no supported-K construction or matching own ID; its “family” and $\varphi$ hits are the unrelated ordinary Chern-ring entries **2-chern-ring-gamma-comparison** (scans 021,022,029,030) and **2-chern-ring-not-injective-pn** (scan 022), both unchecked Hua leads; confidence in the condition is high by the definition of a filtered support system.

### S05 — Cote 2, scan 034 — Reused theorem fragment; an essential prior hypothesis

**Kind:** reading question / own idea.

**Anchor:** “surjectif”; “radiciel”; equivalence of étale categories.

The typed argument and its examples match SGA 4, Exposé VIII, §1, whose topological-invariance theorem concerns universal homeomorphisms; a standard precise hypothesis package is integral, universally injective, and surjective (The Stacks Project Authors, n.d., Tag 04DZ). Our explicit test $D(t)\amalg V(t)\to\mathbb A^1_k$ is radicial and surjective but has disconnected source and connected target, so its small étale topoi cannot be equivalent: integrality cannot simply be dropped. The complete theorem explicitly includes integrality on the preceding source page, SGA 4 VIII, p. 367, so the isolated fragment must not be used to attribute its omission to the full theorem. Context search S05 found no corresponding entry in either context file; confidence is high in the hypothesis distinction and source identification, independently confirmed by the primary reader against original SGA 4 pp. 367–369.

### S06 — Cote 2, scans 034,036,039 — Source identification and qualified chronology

**Kind:** reading question.

**Anchor:** “EGA IV 1.9.9”; “Corollaire 5.11”, “5.12”, “5.13”.

The reused typed passages match SGA 4 VIII §1 (034) and VII §§5.11–5.13 (036,039), including the étale-invariance examples and the successive direct-image continuity corollaries, rather than forming additional handwritten Riemann–Roch arguments. **context/README.md** associates the assembled cote with “[1957]” and “antérieur[es à] 1958,” while the typed stratum's explicit EGA IV reference is to material published in 1964 and its SGA 4 counterparts appeared in the 1972 volume (Grothendieck, 1964; Artin et al., 1972). This is strong evidence against applying a single unqualified 1957 date to all the assembled textual layers, but publication dates are not strict dates for manuscripts or circulated drafts, and these comparisons alone date neither the handwriting nor the physical reuse. Search S06 has that README catalogue entry as its only substantive hit, with no research-result ID in **context/notes/RESULTS_STATE.md**; confidence is high in the bibliographic distinction and deliberately limited on physical chronology.

### S07 — Cote 2, scan 035 — Pseudo-ring; the unit issue is substantive

**Kind:** unpursued implication.

**Anchor:** “pseudoanneau (pas néc d'élément 1).”

Derived tensor product preserves supported perfect complexes, and the ambient perfect-complex ring acts on their Grothendieck group, while the ambient unit $[\mathcal O_X]$ is unavailable when the allowed supports do not contain $X$. Thus the qualified nonunital language fits the construction and should not be silently replaced by “ring with 1”; the modern localized Chern character also has an explicitly multiplicative supported formulation (The Stacks Project Authors, n.d., Tag 0FET). Context search S07 found no relevant supported-ring entry in either context file; confidence in this structural explanation is high, without excluding accidental units for special supports such as an open-and-closed component.

### S08 — Cote 2, scan 035 — Construction ambiguity; rational equivalence with supports

**Kind:** own idea.

**Anchor:** “en prenant tjrs des cycles sur $X$ à support … $\Phi$.”

The phrase leaves a consequential choice between rational-equivalence data that stay inside the allowed supports and the image of supported cycles in the ordinary Chow group. In our test $X=\mathbb A^1_k$, $Z=\{0\}$, the former gives $CH_0(Z)=\mathbb Z$, whereas the class of $0$ maps to zero in $CH_0(X)$ because it is the divisor of $t$ on $X$. This high-confidence calculation shows that forgetting supports can lose information and that the proposed $A^\bullet_\Phi(X)$ is not determined merely as a subobject of $A^\bullet(X)$; context search S08 found no matching result or ID in the two supplied files.

### S09 — Cote 2, scan 035 — Explicit open construction; the supported filtration

**Kind:** self-flagged.

**Anchor:** “on essaiera de définir … via une filtration sur le $\lambda$-pseudo-anneau $K^\bullet_\Phi(X)$ ??”.

This is expressly a proposed construction: a rigorous version must specify supported exterior operations, a unitization or equivalent convention for $\gamma$-operations, the filtration, and the comparison with cycles, rather than importing the ordinary unital-ring argument unchanged. **context/notes/RESULTS_STATE.md**, search S09, supplies the indirect lead **Hua, findings register, 2-chern-ring-gamma-comparison**, scans 021,022,029,030, with unchecked status “new to us … waiting”; that entry concerns geometric elements in an ordinary $\lambda$-ring and proves no supported version here. The rational localized-character homomorphism of Stacks Project Tag 0FET is a concrete later comparison target, but does not by itself establish the integral filtration the page proposes. Confidence is high that the question remains open within these sheets, and medium that the earlier comparison is the most useful route because support and nonunital conventions remain to be fixed.

### S10 — Cote 2, scan 035 — Explicit self-flagged extension

**Kind:** self-flagged / reading question.

**Anchor:** “Classes de Chern [cohomologiques|homologiques] ??” (word reading uncertain in the frozen text).

The double question mark marks an additional proposed extension, and the unresolved cohomological/homological reading must not be settled from the expectation of a later theory. Covariant homological characteristic classes and contravariant/operational characteristic classes require distinct targets and functorialities; the eventual bivariant framework connects them without making them interchangeable (Fulton & MacPherson, 1981). Context search S10 found no same-object entry in either context file; confidence is high in the self-flagged status and only moderate in the proposed literature connection.

### S11 — Cote 2, scan 037 — Explicit doubt; which inverse images have no conditions?

**Kind:** self-flagged / own idea.

**Anchor:** “images inverses sans conditions (?)”.

Absolute perfect complexes admit arbitrary derived pullback, but that fact does not prove unrestricted base change for the proposed relative perfect categories: the modern bivariant construction uses Tor-independent squares (Alonso Tarrío et al., 2023, Proposition 3.11 and Theorem 6.1). Our test base-changes $\operatorname{Spec}k\to\operatorname{Spec}k[t]$ by $\operatorname{Spec}k[t]/(t^2)\to\operatorname{Spec}k[t]$; $\mathcal O_{\operatorname{Spec}k}$ is perfect relative to the first map and is not perfect relative to the resulting classical fibre map, whose target is the dual numbers. This high-confidence obstruction concerns relative classical base change, not ordinary derived pullback of an absolute perfect complex. Context search S11 found no relevant own entry; incidental “Tor” substring hits in Hua's Chern-ring discussion concern different objects and do not resolve the page's question.

### S12 — Cote 2, scan 037 — Proposed covariance; why “sans plus” is plausible

**Kind:** unpursued implication.

**Anchor:** “propreté sur supports (sans plus)” and the displayed equality commuting with $g_*$.

Relative perfection can make proper covariance stronger than covariance of absolute $K^0$: for a proper $g:X\to Y$ between Noetherian schemes over a Noetherian base $S$, $Rg_*$ preserves complexes perfect relative to $S$, without requiring $g$ itself to have finite Tor-dimension (Alonso Tarrío et al., 2023, Proposition 3.5). A later realized analogue is the proper-covariant rational transformation $G_0(X)\to CH_*(X)_{\mathbb Q}$ for quasi-projective schemes, with its module property and smooth Todd normalization (Baum et al., 1975, §0 and Chapter II). This comparison explains the force of the proposal but does not prove every relative, support-indexed assertion in the unfinished sheet; the uncertain word “bivification|homification” remains a reading uncertainty. Search S12 matches only the general Riemann–Roch subject in **context/README.md**, no same-object result ID; confidence is high in the cited mathematics and moderate in identifying the exact intended formalism.

### S13 — Cote 2, scan 037 — Unfinished canonical-element proposal

**Kind:** own idea.

**Anchor:** “un élément canonique explicitable”.

One rigorous candidate for the formal map $K^0(X)\to K^0(X\to S)$, when $X\to S$ is locally of finite type between Noetherian schemes and has finite Tor-dimension, is multiplication by the relative orientation $[\mathcal O_X]$ (Alonso Tarrío et al., 2023, §6.9). The Riemann–Roch image of the structure sheaf is a Todd homology class, and in singular situations that class need not come from an ordinary cohomology class capped with the fundamental class (Baum et al., 1975, §0.2 and IV §6). This supplies a candidate interpretation rather than an identification of the unfinished “canonical element,” and does not establish an integral $K^0$-preimage of any desired Todd factor; confidence is high for the formal distinction and low-to-medium for its identification with this fragment. Context search S13 found no relevant entry in either supplied context file.

### S14 — Cote 2, scan 038 — Hypothesis-sensitive comparison; regular ambient scheme

**Kind:** unproved claim.

**Anchor:** the four vertical labels “iso si $X'$ rég.”.

For a Noetherian regular ambient scheme $X'$, bounded coherent complexes on $X'$ are perfect, giving the expected perfect/coherent comparison, also after imposing cohomological support (The Stacks Project Authors, n.d., Tag 08E0). The thickenings $X_n$ themselves can be singular, so the left-hand relative-perfect categories should still not be replaced by intrinsically perfect complexes on $X_n$; the example in S01 tests exactly this distinction. Confidence is high for this Noetherian interpretation, while the diagram by itself does not prove the comparison under every prescheme convention. Context search S14 found no related result or ID in either context file.

### S15 — Cote 2, scan 038 — Coherent dévissage; stronger than the written surjectivity label

**Kind:** own idea — conditional strengthening.

**Anchor:** $K_\bullet(X_0)\to\varinjlim K_\bullet(X_n)$, “surj. si $X'$ rég.”.

If the lower groups are coherent Grothendieck groups and $X'$ is Noetherian, nilpotent dévissage makes each thickening pushforward $G_0(X_0)\to G_0(X_n)$ an isomorphism, and also identifies $G_0(X_0)$ with the coherent group supported on $X$ inside $X'$; ambient regularity is unnecessary for this lower-row statement (Quillen, 1973, §5, Theorem 4, and §7.3, Propositions 3.1–3.2). The finite ideal-adic filtration supplies the dévissage, while regularity is needed for the passage to the upper perfect groups, not for the filtration itself. Search S15 found only the unrelated “surjectivity” in **Hua, findings register, 2-chern-ring-gamma-comparison** (scans 021,022,029,030; unchecked), not a matching own result. Confidence is high under the explicit Noetherian/coherent interpretation; this is a conditional strengthening, not a transcription correction.

### S16 — Cote 2, scan 038 — Withdrawn arrows and distinct forget-support map

**Kind:** withdrawn in the same text / own idea.

**Anchor:** cancelled $v'$-arrows; live $w'v'=\mathrm{id}$, $v'w'=\mathrm{id}$.

The frozen diagram cancels the diagonal $v'$ and the lower return $v'$, while leaving the two inverse identities written below; this is drafting evidence, not a completed construction of the cancelled arrows. The lower isomorphism from the limit of thickening groups to the supported coherent group must also be distinguished from the other $w'$, the rightmost map forgetting supports. Our high-confidence test $Z=\{0\}\subset\mathbb A^1_k$ sends the nonzero generator of $G_0(Z)$ to zero in $G_0(\mathbb A^1_k)$ by $0\to\mathcal O\xrightarrow{t}\mathcal O\to k\to0$, so no inverse assertion should be transferred to that rightmost map. Context search S16 found no relevant entry in either supplied context file.

### S17 — Cote 2, scan 038 — Supported Riemann–Roch expression

**Kind:** unpursued implication.

**Anchor:** $\operatorname{ch}(i_!x)\operatorname{Todd}(X'/S)$.

For an embedding into a smooth ambient variety, the later singular Riemann–Roch construction combines the localized Chern character of an ambient resolution with the ambient Todd class to obtain a class on the support, and proves independence and proper covariance (Baum et al., 1975, I §6 and II §3). This makes the displayed expression a precise research lead, but the ordinary ambient Chern character alone can lose the supported class, as S08 and S16 demonstrate; a localized character supplies the missing supported target (The Stacks Project Authors, n.d., Tags 0FB0 and 0FET). Confidence is high in this comparison under its smooth-ambient, field, and rational-coefficient hypotheses, but it does not establish the sheet's unrestricted relative formulation. Context search S17 found no same-object result or ID in either context file.

### S18 — Cote 2, scans 036,039 — Reused continuity statements; scope of hypotheses

**Kind:** unproved claim on a cancelled reused sheet.

**Anchor:** “morphismes de transition affines”; “quasi-compacts et quasi-séparés”.

These are étale direct-image continuity statements: in the abelian-sheaf case, filtered limits with affine transitions and quasi-compact, quasi-separated structural morphisms admit the indicated comparison of higher direct images, including the variant formed from an arbitrary sheaf on the limit (The Stacks Project Authors, n.d., Tag 03Q4, Lemmas 59.51.8–59.51.10). The visible revisions replace a single base-change system by two compatible inverse systems, which is a substantive generalization already encompassed by that modern statement. The frozen text marks these reused bodies as cancelled, so they should be identified as a separate source layer rather than adopted as live Riemann–Roch claims. Context search S18 found no matching result or ID; confidence is high in the mathematical comparison and source identification, independently confirmed by the primary reader against original SGA 4 VII, pp. 363–364.

### S19 — Cote 2, scans 036,039 — Type mismatch; retain the written projection letters

**Kind:** reading question.

**Anchor:** scan 036 $u_i^*(R^nf_{i*}F_i)$, with $u_i:X\to X_i$; scan 039 $v_i^*(R^nf_{i*}(u_{i*}F))$, with $v_i:Y\to Y_i$.

The sheaf $R^nf_{i*}F_i$ lives on $Y_i$, so its pullback to $Y$ requires the $Y$-projection, called $v_i$ in 039; the $u_i$ explicitly defined in 036 has the wrong source and target for that operation. Likewise, 036's proof says the question is local on $X_{i_0}$ immediately before making $Y_{i_0}$ affine, which warrants a separate locality-label check. Direct visual collation shows that SGA 4 VII, p. 364, retains the same $u_i$ display mismatch but reads $Y_{i_0}$ in the proof; these are high-confidence type diagnostics, also supported by the well-typed modern formulation in Stacks Project Tag 03Q4, and do not authorize changing the frozen readings. Context search S19 found no related entry in either file.

### S20 — Cote 2, scan 036 — Nontrivial warning; group schemes versus inverse-image sheaves

**Kind:** unpursued implication / own idea.

**Anchor:** “n'est pas un cas particulier”; “au sens du changement de base pour les préschémas”.

The warning is mathematically substantive because base change of a group scheme and inverse image of its associated sheaf on the small étale site need not coincide. Our example takes algebraically closed $k$, $K=k(t)$, and $\mathbb G_m$: the small étale sheaf over $k$ is the constant sheaf $k^\times$, whose inverse image to connected $\operatorname{Spec}K$ still has global sections $k^\times$, whereas the base-changed group scheme has sections $K^\times$. Confidence is high in this explicit distinction, so the printed warning should be retained even where theorem numbers are in revision. Context search S20 found no corresponding result or ID in the supplied files.

### S21 — Cote 2, scan 032 — Cover/title record

**Kind:** reading question — title.

**Anchor:** “Caractères de Chern covariants” and “à supports”.

The cover announces the support/covariance block, while the exact $K$- and $A$-superscript readings remain uncertain in the frozen text. Its marginal “31” is a written number, not a stated count of the ensuing pages, and no page count should be manufactured. Context search S21 found only the cote-level title/date in **context/README.md**, not a specific result or ID in **context/notes/RESULTS_STATE.md**; confidence is high in this bounded title-sheet assessment.

## 6. Riemann–Roch for fibrations, curves and surfaces

### CC10 — Cote 2, scan 041, formula (2) — Unproved claim

“Il y a alors une formule meilleure” displays a quotient by the top Chern class of a normal-type bundle, and a proof must explain both the regular-immersion hypothesis and universal polynomial divisibility before specializing the formula. An evaluated top Chern class need not be invertible and can be zero—for example for the constant section of a trivial projective-space product—so the expression cannot simply mean ordinary division in the Chow ring. The published rational theorem and its contemporary warning about stronger integral formulas give useful comparison points (Borel & Serre, 1958, §7, p. 113), but **context:** neither README.md nor `notes/RESULTS_STATE.md` contains a matching immersion formula or neighbouring scan.

### CC11 — Cote 2, scan 041, E^(i) with fibre cohomology — Own idea

The assertion “E^(i) est le fibré vectoriel … dont la fibre est le iième groupe de cohomologie” requires cohomology-and-base-change hypotheses, since even a product projection with a varying vector bundle can have jumping fibre cohomology. For an elliptic curve, the Poincaré line bundle on `E×Pic^0(E)` has `h^0=h^1=1` at the trivial line bundle and 0 at all nontrivial degree-zero line bundles, so those groups do not form vector bundles of locally constant rank. **Confidence: high**, because degree-zero line bundles with a section are trivial and curve Riemann–Roch gives the stated h^1; this diagnoses a missing condition rather than disproving a suitably restricted meaning of “application fibrée” (The Stacks Project Authors, n.d., Tags 0AYQ,0BDM). **Context:** no relevant cohomology/base-change passage or scan occurs in the supplied context.

### CC12 — Cote 2, scan 041, large twist — Unproved claim

The claim “E^(i)=0 pour i>0 … E(n) … n grand” is justified by relative Serre vanishing when the twist is relatively ample, the morphism proper, and the sheaf coherent over a Noetherian base. Calling the surviving `f_*E(n)` a vector bundle additionally needs the relevant flatness/base-change condition; for a sheaf flat over the base, higher-direct-image vanishing yields finite local freeness (The Stacks Project Authors, n.d., Tags 02O1,0BDM). **Context:** the search in README.md and `notes/RESULTS_STATE.md` found only an unrelated GT-character occurrence of “vanishes,” with no relevant item or source scan.

### CC13 — Cote 2, scan 042, restriction of the Todd class — Unproved claim

The passage from `C_Z(i^*T_X)` to `C_Z(T_Z)` is explained for a fibre of a smooth morphism between smooth varieties by the exact tangent sequence, whose quotient is the constant vector space `T_yY` tensored with `O_Z`, and therefore has trivial positive Chern classes. It is not an equality of the two tangent bundles themselves, and a singular fibre or a nonsmooth morphism requires a different, usually virtual, tangent argument. **Context:** no matching tangent/Hirzebruch/fibre passage or neighbouring scan appears in README.md or `notes/RESULTS_STATE.md`; the published fibre-integration discussion is a useful independent comparison (Borel & Serre, 1958, §17).

### CC14 — Cote 2, scans 042–043, higher components and eventual polynomiality — Unpursued implication

The observation that the positive-degree components contain information absent from numerical Hirzebruch–Riemann–Roch leads to the underlined claim that the “classe de Chern modifiée” of `f_*E(n)` “dépend polynomialement de n.” In the smooth projective setting with relative dimension d, the displayed exponential gives `ch_j(f_!E(n))` as a rational polynomial of degree at most d+j, and relative Serre vanishing identifies `f_!E(n)` with `f_*E(n)` for large n; the ordinary Chern components are then polynomial after tensoring with Q by the universal conversion formulas, without the same automatic degree bound or an assertion about integral torsion (The Stacks Project Authors, n.d., Tags 02O1,02UM). **Confidence: high for this rational consequence**, because the degree bound follows by selecting the codimension d+j term before pushforward. **Context:** no polynomiality or Chern-character passage or source scan is supplied in README.md or `notes/RESULTS_STATE.md`, so this adds a concrete subject beyond the title-based RR placement rather than settling a listed open ID.

### CC15 — Cote 2, scan 043, boxed curve-to-curve formula — Unpursued implication

The half-canonical expression for `f_!(n,d)` follows in `Pic(Y)⊗Q`, but it does not uniquely determine a Picard class when 2-torsion is present. An integral formulation records the actual line bundle `det(f_*O_X)` and uses `det(f_*E)=Nm_f(det E)⊗det(f_*O_X)^n`, thereby retaining the information that a choice-free division by 2 would lose. **Own extension confidence: high** in the finite-flat smooth-curve setting, because this determinant identity can be checked after local trivialization and the rational class agrees with the displayed RR formula; **context:** no Picard, determinant, or canonical-divisor entry or neighbouring scan is present in the two supplied context files.

### CC16 — Cote 2, scan 044, “séparable ou non” — Unpursued implication

The parenthesis “séparable ou non” is compatible with the rank and degree calculation for a finite nonconstant morphism of smooth proper curves: such a map is finite flat, and neither Euler-characteristic preservation nor the rational RR expression requires separability. As a direct check, relative Frobenius of a smooth curve of genus g in characteristic p has rank p and `deg(F_*O_X)=(p-1)(g-1)`, matching the displayed half-canonical degree formula. **Own diagnostic confidence: high**, from the degree–Euler-characteristic identity and finite-flatness criteria (The Stacks Project Authors, n.d., Tags 0AYQ,0BXX); **context:** no separability, ramification, or Frobenius passage or source scan was found.

### CC17 — Cote 2, scan 044, curve-to-surface calculation — Unproved claim

The final live boxed expression is algebraically consistent with `ch_2=(c_1²-2c_2)/2`: for rank n and degree-class d on the source curve, one obtains `ch_1=nδC` and `ch_2=f_*d-(n/2)f_*K_X+(nδ/2)CK_Y`. Thus `c_2=(n²δ²/2)C²-(nδ/2)CK_Y-f_*d+(n/2)f_*K_X`, an equality in `CH²(Y)⊗Q` matching the written live formula, while the quadratic Todd terms crossed out earlier cannot contribute because the pushforward has rank zero on a surface. **Context:** neither supplied context file contains this surface calculation or a neighbouring source scan; the conversion formula is independently fixed by The Stacks Project Authors (n.d., Tag 02UM), and this is an algebraic consistency check, not a retrospective repair of crossed ink.

### CC18 — Cote 2, scan 045, first display and normalization sentence — Own idea

The written `C²(O_C)` is followed by “de la normalisée,” but the preceding044 calculation actually applies to `f_*O_{\widetilde C}` for the normalization map, which differs from `O_C` at singular points. For a reduced Cartier curve in a smooth surface, the integral exact sequence `0→O_C→ν_*O_{\widetilde C}→Q→0` gives `c_2(O_C)=c_2(ν_*O_{\widetilde C})+[Q]`, while the divisor resolution gives `c_2(O_C)=C²`; here `[Q]` is the 0-cycle of normalization defects (The Stacks Project Authors, n.d., Tags 0C44,0ESY). **Confidence: high** under these stated hypotheses, because the two exact sequences fix the sign and identify the missing finite-length term. **Context:** no normalization or `O_C` item or neighbouring scan was found in README.md or `notes/RESULTS_STATE.md`; the issue is an additional diagnostic, not a correction to the frozen wording.

### CC19 — Cote 2, scan 045, numerical genus formula — Own idea

A rational nodal plane cubic gives an explicit test of the displayed expression `1/2(C²-CK_Y)+g-1`: in `Y=P²`, `C=3H`, `K_Y=-3H`, and normalization genus g=0, it gives 8, whereas `c(O_C)=1/(1-3H)` gives `deg c_2(O_C)=9`. The difference 1 is precisely the node's normalization defect, and 8 is the value for the normalization pushforward instead. **Confidence: high**, because this calculation is integral in `CH^*(P²)=Z[H]/(H³)` and is consistent with the normalization exact sequence (The Stacks Project Authors, n.d., Tag 0C44); **context:** neither context file supplies a singular-curve/genus comparison or prior source scan.

### CC20 — Cote 2, scans 041/043/044, target subscripts — Reading question

The frozen text has `C_Y^q(T_{Y/X})` in 041, `varphi_X(f_!(xi))` in 043, and “f_*(O_X) … sur X” in 044, despite the displayed morphism `f:X→Y`. These are source-level type or notation questions: the published direction of coherent direct image suggests target Y in the latter two expressions, but the first additionally depends on what the written relative-normal notation denotes. **Context:** no corresponding formula or neighbouring scan was supplied in README.md or `notes/RESULTS_STATE.md`, so literature gives a type-checking reason to ask the question rather than authority to alter a reading (Borel & Serre, 1958, §5d).

## 7. Reused algebra leaves and their unresolved readings

### A14 — Cote 2, scan 011, typed §6 — reading question

The typed tensor-power construction explicitly assumes “A commutatif,” but the later phrase read as applications f and g “de E dans E” is followed by T^p(E*) and the canonical map to(T^p(E))*. These types suggest E* as an alternative at the first occurrence, already left doubtful in the frozen transcription; the missing star should be checked in another witness rather than silently inferred. This is reused sesquilinear-algebra material carrying n° 234 and printed page −12−, not a proof of the equivariant assertions on 016–019.

Context: neither supplied context file contains the typed leaf or a matching numbered witness; no neighboring scan.

### A15 — Cote 2, scan 013, before equation (17) — reading question

The entry convention u(f_j)=Σ_i λ_ij e_i gives U an n-by-m size, and UᵗRU^J consequently has the required m-by-m size. The frozen words before (17) instead put “m lignes et n colonnes” first inside doubt alternatives, so the dimensional check identifies which alternative is mathematically consistent without changing the reading. The preceding correction from “famille d'…de” to “matrice à…dans” is a separate editorial revision, not evidence that the dimension letters were also corrected.

Context: no matrix or n° 234 witness in either supplied context file; no neighboring scan.

### A16 — Cote 2, scan 015, final remark — self-flagged

A handwritten “?” stands beside the assertion that the preceding formulas remain “valables” for an A-bimodule F, with “à gauche et à droite” underlined. The sheet refers to conditions (1)–(4), which are absent from this package, so the exact scope of the proposed extension cannot be settled merely by treating F as an ordinary central module. The displayed factors 2 and 4 also distinguish identities that remain formally valid from reconstruction of Φ by division, which needs the corresponding integers invertible.

Context: no polarization/bimodule entry or missing conditions (1)–(4) in either supplied context file; no neighboring scan.

### A17 — Cote 2, scan 024, normality proof — unproved claim

The reused typed statement “Dans ces conditions, A est normal” is supported by unique factorization and the exponent valuations, but its proof references and last sentence are incomplete on this leaf. The modern result agrees with the assertion(The Stacks Project Authors, n.d., Tag 0AFV), while the frozen raised A in p_iota^(n_A) is a reading problem: ideal membership x∈p_iota^nA is the natural proof step, not an emendation of the source. No evidence on this sheet connects the typed factoriality argument to the adjoining universal Chern-ring argument.

Context: no factoriality or valuation result in supplied `README.md` or `notes/RESULTS_STATE.md`; no neighboring scan.

### A18 — Cote 2, scan 026, valuation intersection and localization — unpursued implication

The warning that an intersection of valuation rings of k(X) can have smaller fraction field is essential: with X an indeterminate, intersecting all those containing k gives k, since every nonconstant rational function has a pole on the projective line. Transitivity and localization of integral closure agree with the standard statements(The Stacks Project Authors, n.d., Tags 00GH, 0307, 090P), but the editorial request to copy examples from “p.32–39”(first endpoint doubtful) refers to an absent draft rather than providing examples in this package. This reused sheet gives an instructive distinction between an ambient field and the fraction field of the intersection, not a new RR hypothesis.

Context: no integral-closure or valuation counterpart in either supplied context file; no neighboring scan.

### A22 — Cote 2, scan 015, formula (14) and final “?” — own idea

A concrete test of the unrestricted bimodule extension is A=C with J=conjugation, E=C, and F=C with usual left action but right action z·a=z·conjugate(a); then Φ(x,y)=xy is J-sesquilinear in the usual bimodule sense and Q(x)=x². At x=y=1 the right side of the printed complex polarization formula (14) is4+i(2i)−i(−2i)=0, while4Φ(1,1)=4, so that formula needs a centrality condition on the two i-actions if this is the intended definition. Confidence: high for the counterexample under those stated conventions, medium for its bearing on the author's question because the absent conditions (1)–(4) could impose additional compatibility.

Context: no bimodule counterexample or defining conditions in either supplied context file; no neighboring scan.

## 8. Internal structure and chronological layers

### A19 — Cote 2, title scans 002,009,020,032,040 — unpursued implication

The covers “Contre-exemples,” “Filtration des λ-anneaux…classes de Chern universelles,” “Caractères de Chern covariants…à supports,” and “R.R.des surfaces” confirm the README's placement in intersections/Chern/RR rather than functional analysis. They also show several local units, so the cote should not be treated as one continuously paginated treatise or as evidence for a single chronological layer. The title and pagination inventory in section 10 records the visible markers and the absence of an explicit page-count statement.

Context: `README.md`, package 246/rank 25 and cote 2 scans 002–045, is confirmed in subject but refined in internal structure; `notes/RESULTS_STATE.md` has no matching planning-result row, only its three separately assessed Hua claims.

### A20 — Cote 2, reused leaves011/013/015/024/026/034/036/039 — reading question

The printed sequence −9−,−10−,−12− with n° 234, the commutative-algebra leaves−64− and−80−, and the later étale/cohomological draft references belong to reused physical material, not automatically to one original RR pagination. The citation “EGAIV1.9.9.” on 034 and the SGA4 textual parallels discussed in the support notes make the blanket catalogue label “[1957]” insufficient for dating every leaf or inscription. This is a stratigraphic question requiring paper-side pairing or additional archive witnesses; it does not supply an exact date for any handwritten block.

Context: `README.md` gives the inherited “[1957]” catalogue placement for cote 2 but no physical-side reconstruction; `notes/RESULTS_STATE.md` supplies no chronology entry or neighboring scan.

## 9. Standing question: steps explicitly marked as unverified

This register separates literal question marks and explicit proof promises from assertions merely called easy or evident. It reports the writer's marks, including answered and cancelled questions; the mathematical assessments are in the individual research notes. Context searches for every SF- and TP-item are recorded in `records/context_search_standing.md`.

### SF01 — Cote 2, scan 004, lower diagram — Self-flagged

The branch from `L=D∩N` to `N` is labelled “?”. Its intended target is not explained, and the adjacent argument does not expressly resolve the mark; see A03.

**Context:** Neither `README.md` nor `notes/RESULTS_STATE.md` has this diagram or a corresponding neighboring scan; only the README's general RR placement is relevant.

### SF02 — Cote 2, scan 015, final margin — Self-flagged

A handwritten “?” accompanies the extension to an “A-bimodule F,” with “à gauche et à droite” underlined. The conditions (1)–(4) referred to there are absent, so the question remains open as a source-reading issue; A16 and A22 give the precise conditional test.

**Context:** No bimodule or polarization entry, missing defining page, or neighboring scan occurs in either supplied context file.

### SF03 — Cote 2, scan 022, middle — Self-flagged, answered in the same text

“Est-ce que φ_K est tjrs bijectif ???” is immediately answered by the doubly underlined “Non,” followed by the single-generator projective-space λ-ring example. This is an explicitly asked and answered question, not an unresolved conjecture in the retained manuscript; its exact family of geometric elements is essential.

**Context:** `notes/RESULTS_STATE.md`, Hua, findings register, **2-chern-ring-not-injective-pn**, cites this same scan 022; the intake says the package is waiting and does not certify the claim.

### SF04 — Cote 2, scan 022, final cancelled proposition — Self-flagged / withdrawn in the same text

“Proposition (à prouver directement)” begins a statement about a family of geometric elements, the generated sub-λ-ring, and conditions on a λ-homomorphism. The whole proposition is crossed out and stops at “(ii),” so no completed equivalence or proof should be attributed to these lines.

**Context:** The two Chern-ring entries in `notes/RESULTS_STATE.md` concern scans 021/022/029/030 but do not supply the missing second condition or a neighboring witness.

### SF05 — Cote 2, scan 028, determinant box — Self-flagged

The boxed equality `c¹(E)=c¹(dét E)` points to the doubtful words “conséquence des autres??”. It follows under the explicit λ-homomorphism and rank hypotheses on this sheet, but the relation list on 029 needs a separate compatibility check; the λ-ring notes distinguish these two formulations.

**Context:** `notes/RESULTS_STATE.md`, Hua **2-chern-ring-gamma-comparison**, concerns the surrounding construction but gives no determinant-specific argument or source scan 028.

### SF06 — Cote 2, scan 029, margin — Self-flagged

“À voir: la filtration de K définie par les P(γⁱ(x−ε(x))) est aussi celle définie par les P(γⁱ(E_s−ε_s)), [si les E_s engendrent] ???” explicitly leaves a comparison of generating systems to be checked. The preceding “évidemment surjectif” should be read with this remaining proof obligation, rather than as evidence that the marginal question was already settled on the sheet.

**Context:** `notes/RESULTS_STATE.md`, Hua **2-chern-ring-gamma-comparison**, cites scan 029 and restates the comparison; it does not supply a reviewed proof of this step.

### SF07 — Cote 2, scan 035, item 2 — Self-flagged / conjectural construction

“on essaiera de définir … via une filtration sur le λ-pseudo-anneau … ??” proposes a construction of the Chow substitute with supports for general X. The modal wording and double question mark identify a program, whose filtration and functoriality still have to be specified.

**Context:** Neither supplied context file contains a support-theory result or a neighboring scan; the README's broad Chern/RR placement is refined by this proposed extension.

### SF08 — Cote 2, scan 035, item 3 — Self-flagged / reading question

“Classes de Chern cohomologiques|homologiques ??” is itself only a short question, with the adjective left doubtful in the transcription. The retained material does not give a completed definition attached to that line, and the ambiguity should remain visible when this research lead is indexed.

**Context:** Neither `README.md` nor `notes/RESULTS_STATE.md` supplies a matching formulation or neighboring scan.

### SF09 — Cote 2, scan 037, opening — Self-flagged

“images inverses sans conditions (?)” expressly questions the intended variance. The distinction between derived pullback of intrinsic perfect complexes and pullback of a relative theory is material to answering it; the support notes state the hypotheses rather than interpreting “sans conditions” as a proved theorem.

**Context:** No pullback, relative-perfectness, or variance entry and no neighboring scan occurs in the supplied context.

### SF10 — Cote 2, scan 037, tentative notation — Self-flagged / reading question

The repeated lower “?” in `K_?`, `A_?`, `ch_?`, and `g_?` marks provisional notation, while the construction word is read doubtfully as “bivification|homification.” These are signs of an unfinished setup; they do not individually assert that each displayed equality is false or already disproved.

**Context:** No corresponding notation or relative covariant construction is present in the two context files, and no neighboring scan is available to resolve it.

## 10. Standing question: title sheets and page-count statements

No retained cover or interior sheet explicitly states a total such as “19 pages” or a range such as “Pages 1–67.” The count of **41 retained scans** comes from the supplied corpus (002–045 with 006, 027 and 031 omitted), not from a handwritten page-count assertion; visible marginal foliation and reused typed pagination are recorded separately below. None of these markers alone establishes authorship, date, or continuous textual order.

| Item | Cote / scan | Visible title or numbering | Assessment and context comparison |
|---|---|---|---|
| TP01 | 2 / 002 | Cancelled, doubtful “Formulaire sur\|pour / variétés / Énoncé de RR”; boxed filing note read “Classé parmi les cours.”; marginal 1 | **Title / reading question:** the cancelled title and weak filing instruction are both retained; no page count is stated. `README.md` gives the broader catalogue RR title, not these words, and `notes/RESULTS_STATE.md` has no matching title-sheet entry or neighboring scan. |
| TP02 | 2 / 009 | “Contre-exemples —”; marginal 8 | **Title:** this opens the local counterexample unit, without stating its length. `notes/RESULTS_STATE.md`, Hua **2-trivial-total-chern-class**, cites the following scans 010/012/014 and thus identifies part of its mathematical content, but has no separate cover record. |
| TP03 | 2 / 020 | “Cas des schémas” (last word doubtful); “Filtration des λ-anneaux”; “classes de Chern universelles”; “λ-anneaux ‘spéciaux’ i.e. avec éléments ‘géométriques’”; doubtful “Applications”; marginal 19 | **Title:** these are the sheet's separate lines, not an editorial single title; no page count is given. The two Chern-ring findings in `notes/RESULTS_STATE.md` concern the following unit at 021/022/029/030 and support the README's Chern/RR placement, without adding a cover witness. |
| TP04 | 2 / 032 | Doubtful “Caractères de Chern / covariants, et / K^bullet\|K′ et A^bullet\|A′ à supports”; marginal 31 | **Title / reading question:** the superscript alternatives remain unresolved in the transcription; no count is stated. Neither supplied context file has this support-theory title or a neighboring scan. |
| TP05 | 2 / 040 | “R.R. des surfaces / et autres cas / particuliers / divers”; marginal 39 | **Title:** four underlined lines introduce the final local unit and do not supply a page count. The README's RR placement is confirmed, while `notes/RESULTS_STATE.md` has no surface-calculation entry or neighboring witness. |
| TP06 | 2 / 002–045 | Marginal pencil sequence 1–44, with gaps corresponding to omitted scans 006/027/031 | **Pagination / reading question:** the visible sequence follows PDF scan number minus one on the retained sheets, so it is a foliation clue rather than an autograph statement that a particular text has 44 pages. `README.md` supplies the scan range but no attribution or physical-side reconstruction; `notes/RESULTS_STATE.md` explicitly offsets Hua's page references by one. |
| TP07 | 2 / 011, 013, 015 | Typed −12−, −10−, −9−, with n°/N° 234 markings | **Pagination:** the order and repeated document number identify a separate reused typed unit, not continuous RR pagination or a total of 234 pages. Neither supplied context file gives the missing pages, bibliographic identification, or a neighboring witness. |
| TP08 | 2 / 024, 026 | Typed −80− and −64−; 026 also has an editorial reference to “p.32–39,” first endpoint doubtful | **Pagination / reading question:** these are internal typed page numbers and an external copying reference, not a page-range statement about this cote. Neither context file identifies the underlying commutative-algebra draft or supplies the referenced pages. |
| TP09 | 2 / 034 | Internal “(2” plus numbered propositions/references on the reused typed material | **Pagination / reading question:** the internal marker is distinct from marginal 33, and section or proposition references on 034/036/039 are not text lengths. The README's catalogue “[1957]” does not date every reused layer; the SGA4/EGA comparison in the support notes supplies a chronology question, while the context has no physical reconstruction or earlier scan witness. |

The title and pagination observations are source inventory, not proposals for new archive titles. In particular, the unrelated functional-analysis language in the README's general workshop paragraph is not a mathematical description of this cote's main handwritten units.

## 11. References and evidence locators

External references are primary mathematical publications or the Stacks Project's own statements. The user-supplied manuscript is cited by cote and scan throughout; imported project claims are cited only as the rows supplied in `notes/RESULTS_STATE.md`, with their unreviewed status retained. No claim of historical priority or mathematical novelty follows from these comparisons.

Alonso Tarrío, L., Jeremías López, A., & Sancho de Salas, F. (2023). Relative perfect complexes. *Mathematische Zeitschrift, 304*, Article 42. https://doi.org/10.1007/s00209-023-03294-7. Author preprint: https://arxiv.org/pdf/2112.09680, version 4; Definition 3.1, Propositions 3.5 and 3.11, Corollary 4.2, Theorem 6.1, and §6.9.

Artin, M., Grothendieck, A., & Verdier, J.-L. (Eds.). (1972). *Théorie des topos et cohomologie étale des schémas, Tome 2 (SGA 4)* (Lecture Notes in Mathematics, Vol. 270). Springer. https://doi.org/10.1007/BFb0061319. Original scanned edition: https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-2.pdf. The primary reader visually checked VII, pp. 363–365, and VIII, pp. 367–369, against the frozen transcription; individual original page images include https://library.slmath.org/nonmsri/sga/sga/4-2/4-2t_364.jpeg and https://library.slmath.org/nonmsri/sga/sga/4-2/4-2t_368.jpeg.

Atiyah, M. F. (1966). Power operations in K-theory. *The Quarterly Journal of Mathematics, 17*(1), 165–193. https://doi.org/10.1093/qmath/17.1.165. Original paper reprinted in the author's *K-theory* (1967), consulted at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahk.pdf, PDF pp. 171–199; especially §§1–2 and Proposition 2.2.

Baum, P., Fulton, W., & MacPherson, R. (1975). Riemann–Roch for singular varieties. *Publications Mathématiques de l’IHÉS, 45*, 101–145. https://doi.org/10.1007/BF02684299. Original article: https://www.numdam.org/article/PMIHES_1975__45__101_0.pdf; §0.2, I §6, the theorem in Chapter II and II §3, and IV §6.

Berthelot, P. (1971). Généralités sur les λ-anneaux. In P. Berthelot, A. Grothendieck, & L. Illusie (Eds.), *Théorie des intersections et théorème de Riemann–Roch (SGA 6)* (Lecture Notes in Mathematics, Vol. 225, pp. 297–364). Springer. https://doi.org/10.1007/BFb0066289. Exposé V; the primary reader visually checked original pp. 349–351, 353–355 and 358–359, including the modified product, determinant identity, full λ-compatibility, factorial comparison and operation relations.

Berthelot, P., Grothendieck, A., & Illusie, L. (Eds.). (1971). *Théorie des intersections et théorème de Riemann–Roch (SGA 6)* (Lecture Notes in Mathematics, Vol. 225). Springer. https://doi.org/10.1007/BFb0066283. Original scanned edition: https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf; especially Exposé V, §§3 and 6. Locators and calculations are retained in `records/research_lambda.md`.

Borel, A., & Serre, J.-P. (1958). Le théorème de Riemann-Roch. *Bulletin de la Société Mathématique de France, 86*, 97–136. https://doi.org/10.24033/bsmf.1500. Original scan: https://www.numdam.org/article/BSMF_1958__86__97_0.pdf; especially the Tor product and coherent direct image in §§4–5, the theorem in §7, and fibre integration in §17.

Fulton, W., & MacPherson, R. (1981). *Categorical framework for the study of singular spaces*. *Memoirs of the American Mathematical Society, 31*(243). https://doi.org/10.1090/memo/0243. The publisher’s contents identify Part I, “Bivariant theories,” and Part II, “Products in Riemann–Roch”; used here to identify the later framework, without claiming to have verified every proof in the monograph.

Grothendieck, A. (1958). La théorie des classes de Chern. *Bulletin de la Société Mathématique de France, 86*, 137–154. https://doi.org/10.24033/bsmf.1501. Original scan: https://www.numdam.org/article/BSMF_1958__86__137_0.pdf; §4, 2°, pp. 147–149, supplies the augmented Chern-ring convention used as a comparison in CC08.

Grothendieck, A. (1964). Éléments de géométrie algébrique: IV. Étude locale des schémas et des morphismes de schémas, Première partie. *Publications Mathématiques de l’IHÉS, 20*, 5–259. https://doi.org/10.1007/BF02684747. Official bibliographic record: https://www.numdam.org/item/PMIHES_1964__20__5_0/. This publication date is not treated as a strict date for a circulated draft or for the handwriting on a reused sheet.

Mackall, E. (2020). Universal additive Chern classes and a GRR-type theorem. *Journal of Algebra, 560*, 1173–1189. https://doi.org/10.1016/j.jalgebra.2020.06.018. Author's preprint consulted: https://arxiv.org/pdf/2006.14664, version 1, Proposition 2.1 and Theorem 4.1. The scheme-functor universal property is not silently identified with the manuscript's construction for a specified family in a λ-ring; any convention issue in the preprint is recorded in the λ-ring evidence file, without a claim about a journal erratum.

Pedrini, C., & Weibel, C. (1994). Divisibility in the Chow group of zero-cycles on a singular surface. *Astérisque, 226*, 371–409. https://numdam.org/item/AST_1994__226__371_0/. Original scan: https://numdam.org/item/AST_1994__226__371_0.pdf; Appendix A, p. 404, explicitly treats the rank–Picard description in dimension at most one.

Quillen, D. (1973). Higher algebraic K-theory: I. In H. Bass (Ed.), *Algebraic K-theory I: Higher K-theories* (Lecture Notes in Mathematics, Vol. 341, pp. 85–147). Springer. https://doi.org/10.1007/BFb0067053. Original article: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf; §5, Theorem 4, and §7.3, Propositions 3.1–3.2.

Serre, J.-P. (1977). *Linear representations of finite groups* (L. L. Scott, Trans.; Graduate Texts in Mathematics, Vol. 42). Springer. https://doi.org/10.1007/978-1-4684-9458-7. Induction and restriction: §§7.1–7.3; original scan indexed at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Reps.pdf.

The Stacks Project Authors. (n.d.). *The Stacks Project*. Retrieved November 16, 2026, from https://stacks.math.columbia.edu. Individual citations use stable tags as locators:

| Tag | Primary statement used | Link |
|---|---|---|
| 00GH | Finite and integral ring extensions | https://stacks.math.columbia.edu/tag/00GH |
| 02O1 | Relative Serre vanishing, Lemma 30.16.2 | https://stacks.math.columbia.edu/tag/02O1 |
| 02UM | Chern character and tensor products | https://stacks.math.columbia.edu/tag/02UM |
| 0307 | Integral closure commutes with localization, Lemma 10.36.11 | https://stacks.math.columbia.edu/tag/0307 |
| 090P | Valuation-ring intersection, Lemma 10.50.11 | https://stacks.math.columbia.edu/tag/090P |
| 0AFV | Unique factorization implies integral closure, Lemma 10.120.11 | https://stacks.math.columbia.edu/tag/0AFV |
| 0AYQ | Degrees and Euler characteristics on curves | https://stacks.math.columbia.edu/tag/0AYQ |
| 0BDM | Cohomology and base change applications, Lemmas 36.32.1–4 | https://stacks.math.columbia.edu/tag/0BDM |
| 0BXX | Curves and function fields, Lemmas 53.2.3–4 | https://stacks.math.columbia.edu/tag/0BXX |
| 0C44 | Normalization of one-dimensional schemes, Lemma 33.41.2 | https://stacks.math.columbia.edu/tag/0C44 |
| 0ESY | Chern classes of perfect complexes | https://stacks.math.columbia.edu/tag/0ESY |
| 03Q4 | Étale continuity and higher direct images, Lemmas 59.51.8–10 | https://stacks.math.columbia.edu/tag/03Q4 |
| 04DZ | Topological invariance for integral, radicial, surjective morphisms, Theorem 59.45.2 | https://stacks.math.columbia.edu/tag/04DZ |
| 06UP | Derived comparison for a Serre subcategory, Lemma 13.17.4 | https://stacks.math.columbia.edu/tag/06UP |
| 08E0 | Coherent complexes and perfection on a regular scheme, Lemma 36.11.8 | https://stacks.math.columbia.edu/tag/08E0 |
| 0955 | Noetherian derived torsion comparison, Lemma 47.10.1 | https://stacks.math.columbia.edu/tag/0955 |
| 0FB0 | Localized Chern classes and character, Definition 42.50.3 | https://stacks.math.columbia.edu/tag/0FB0 |
| 0FET | Additive and multiplicative localized character on supported perfect K-theory, Remark 42.56.11 | https://stacks.math.columbia.edu/tag/0FET |

### Further evidence kept with this deliverable

The longer integral calculations for CC02/CC05/CC06/CC07/CC09 and CC14–CC19 remain in `records/research_chern_curves.md`, appendices A–F. The λ-ring evidence file contains the universal-product and torsion calculations, and the support-theory file records the exact primary-literature comparisons. These appendices support the short individual notes; they are not alterations or interpolations in the transcription. Earlier reading hypotheses in `records/research_leads.md` and the historical doubt register are explicitly provisional records; the frozen page files, final doubt register and these final notes control the deliverable.
