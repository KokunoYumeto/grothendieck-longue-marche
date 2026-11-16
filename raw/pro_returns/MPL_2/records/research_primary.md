# Primary-reader research notes: structural, equivariant, reused-sheet and inventory items

These notes were written after the transcription freeze; none changes the LaTeX. The context archive contains only `README.md` and `notes/RESULTS_STATE.md`, with no neighboring transcript, so a negative context comparison means no supplied textual counterpart, not absence elsewhere in the archive. The register has no matching settled/open result of the user's own project; the unrelated LM4/LM7 referee list supplies no applicable theorem.

## A01 — Cote2, scans003–004, definitions and proposition — unproved claim

The assertions “C'est l'annulateur de E₀,” “E=Φ+D,” and “Φ∩D=0” concern a preliminary group of sheaf classes before the final exact-sequence quotient, whose restricted relations are difficult to read. The familiar rank–determinant description of the final K-group therefore does not by itself prove every intermediate equality on these sheets; a proof must specify the initial relation subgroup, the product, and the map from divisors before identifying its kernel with principal divisors. The adjacent proposition is a proposed reduction of relations, not a supplied proof of those identifications.

Context: no topical counterpart in supplied `README.md` or `notes/RESULTS_STATE.md`, and no neighboring scan; search A01 in `context_search_primary.md`.

## A02 — Cote2, scans003–004, Φ_N definition — reading question

Scan003 reads provisionally “Quotient de Φ par le sous-groupe,” but then writes Φ/Φ_N, while004 writes Φ∩N=Φ_N. Those later occurrences suggest that Φ_N is intended as the relation subgroup or ideal, so “sous-groupe” or a different scope for “Quotient” is a mathematical alternative to investigate against another witness. The frozen word “Quotient” remains untouched: this is a consistency question, not a licence to replace visible ink.

Context: no Φ_N or quotient-definition counterpart in either supplied context file; no neighboring scan.

## A03 — Cote2, scan004, formula(1) and lower diagram — self-flagged / unproved claim

The diagram places a literal “?” on the branch from L=D∩N to N; its scope is not expressly given, whereas “Pour vérifier(1), il suffit…” reduces the numerical RR assertion to point sheaves and the structure sheaf. That reduction needs the preceding description of generators and a setting in which Euler characteristics are finite—properness or an explicit replacement—which the isolated opening “X courbe non singulière” on003 does not state. On a smooth proper connected curve, the displayed degree expression becomes deg(F)+rank(F)(1−g), but this standard specialization does not resolve what the diagram's question mark targets (Borel & Serre,1958,§§7–9).

Context: `README.md` places the cote under Riemann–Roch but supplies no other scan; `notes/RESULTS_STATE.md` contains no entry about this curve reduction or question mark.

## A04 — Cote2, scan005, first half — unproved claim

The sheet asserts “L'idéal d'augmentation…est de carré nul,” vanishing γ^i(x) for i≥2 on augmentation-zero elements, and cl(E)=[rg(E),det(E)] under its noetherian, ample-line-bundle, dimension≤1 assumptions. The rank–Picard description is consistent with the dimension-one statement explicitly used by Pedrini and Weibel(1994,AppendixA,p.404), but the λ-structure needs to be checked as well: once reduced classes are identified with [L]−1 and their products vanish, γ_t([L]−1)=1+([L]−1)t supplies the claimed higher vanishing. This adds a precise proof route to the bare assertion and keeps connected components, irreducible components, and the homological K-group separate.

Context: neither supplied context file has a rank–Picard or dimension-one K entry; no neighboring scan.

## A05 — Cote2, scans007–008, μ_i and the class of1 — own idea

The phrase “seul invariant de la situation” in the zero-dimensional case is naturally tested on R=k[ε]/(ε^m): finite projective modules are free, finite modules have a composition series with residue-field factors, and the map K₀(R)→G₀(R) is multiplication by m under rank and length. Thus the sheet's μ=length(O_X) detects a genuine integral obstruction even when the two groups are abstractly Z; for m>1 its cokernel is Z/m. Confidence: high, because the calculation follows directly from a length-m filtration of R, and it distinguishes the structure-sheaf map from the abstract group identifications.

Context: neither supplied context file contains this length/Cartan-map test; no neighboring scan.

## A06 — Cote2, scans007–008, splitting and δ — own idea

The author calls the homological splitting “non naturel” and writes δ=1−Σμ_i1_i; replacing the chosen lifts1_i by1_i+e_i with e_i∈K_(0) changes δ to δ−Σμ_ie_i. Consequently the residue of δ in K_(0)/(Σ_i μ_iK_(0)) is independent of those lift choices, even though δ itself is not. For finitely many components this quotient is K_(0)/dK_(0), where d is the greatest common divisor of the μ_i, so relatively prime generic multiplicities force the residue to vanish. Confidence: high for this elementary abelian-group consequence of the displayed formula, and medium for its usefulness as a geometric invariant until functoriality of the chosen filtration and base-change maps is specified.

Context: no splitting, residual-class, or δ entry in either supplied context file; no neighboring scan.

## A07 — Cote2, scan008, lower cancelled construction — withdrawn in the same text

The attempted “On se définit un hom” and c_•=ch_• construction are crossed out and end with an unfinished minus sign, while the upper formula for the structure-sheaf map remains live. Scan007 already explains why a splitting-based formula would lack naturality under base change, which supplies a plausible internal motivation without proving why the author cancelled this particular version. Any later use should cite007–008 together and distinguish the live map from the withdrawn proposed character.

Context: no matching formula in supplied `README.md` or `notes/RESULTS_STATE.md`; no neighboring scan.

## A08 — Cote2, scan016, restriction of extension — own idea

The asserted “isom…fonctoriel non canonique” u* u_*(F)≃F^(G′/G) needs an underlying-module qualifier if u_* means ordinary induction: for H=C₃⊂S₃ and a nontrivial complex characterχ, restriction of the induced representation is χ⊕χ⁻¹, not χ⊕χ. As complex vector spaces the two sides are isomorphic after choosing coset representatives, whereas the H-actions distinguish them; this is the elementary normal-subgroup case of the restriction/induction framework (Serre,1977,§§7.1–7.3). Confidence: high under the usual induction interpretation, because a generator of C₃ has eigenvaluesζ andζ⁻¹ on the induced module, but medium as an interpretation of the abbreviated sheet, which may suppress a forgetful functor.

Context: neither supplied context file has an induction or Mackey entry; no neighboring scan.

## A09 — Cote2, scan016, stability of free subcategories — own idea

The claim “elles sont stables pour les foncteurs précédents” follows “Lorsque u est injectif,” so whether injectivity remains in force is ambiguous; even for the inclusion 1→Z, restriction of the rank-one free k[Z]-module k[Z] is infinite-dimensional over k and therefore does not preserve finite-type freeness. For subgroup inclusions restriction preserves group-algebra freeness, and finite index suffices for the finite-type version, while extension of scalars preserves finite free modules; under the broader arbitrary-homomorphism interpretation, C₂→1 already sends the free k-module k to a nonfree trivial k[C₂]-module. Confidence: high for these coset-basis and dimension checks, and medium for the scope of the written hypothesis; the subsequent finite symmetric-group inclusions satisfy the needed index condition.

Context: no corresponding stability hypothesis or counterexample in either supplied context file; no neighboring scan.

## A10 — Cote2, scan017, projection and exterior-operation promise — unproved claim

The “formule de projection” can be verified for induction by g′⊗(v⊗w)↦(g′⊗v)⊗g′w, with inverse using g′⁻¹ on the second factor, so its equivariance and balancing are concrete checks distinct from the problematic splitting on016. The promise to deduce Λ^i and other tensor operations “plus bas” is only partially pursued on018–019 through symmetric tensor powers: descent through short exact sequences still requires the tensor-power filtration, and extraction of alternating representations by averaging would require invertibility of i!. Atiyah(1966,§2,Proposition2.2) provides a later complex-vector-bundle comparison using signed graded tensor powers; it is not an integral proof for every ringed topos in016.

Context: no projection-formula or promised-operation counterpart in either supplied context file; no neighboring scan.

## A11 — Cote2, scan018, induced product — unproved claim

“Commutative et associative dans un sens évident” is justified by conjugacy of the two block inclusions and by transitivity of induction from S_p×S_q×S_r into S_(p+q+r). The result is naturally a coherent family of isomorphisms of categories, with the ordinary commutative graded ring obtained only after an appropriate Grothendieck-group construction. This is a structural parallel with Atiyah's symmetric-group construction(1966,§1), without a historical priority claim or an assertion that the manuscript supplies all coherence checks.

Context: neither supplied context file discusses this categorical induced product; no neighboring scan.

## A12 — Cote2, scans018–019, iterated tensor powers — unpursued implication

The cancelled T^n(F) construction for an S_m-object naturally has the fuller wreath-product action S_m^n⋊S_n on n blocks of m letters, although the written S_m×S_n also acts legitimately through the diagonal S_m inside S_m^n. For the surviving T^m(T^n(F)) the corresponding full action instead uses S_n^m⋊S_m on m blocks of n letters; its written w_(m,n):S_m→S_(mn) can be the outer block-permutation inclusion after forgetting the inner S_n-symmetries. These are compatible candidate reconstructions, so the cancellation does not establish that the direct-product action was impossible, and the retained versus forgotten symmetry must be stated explicitly. Confidence: high for the two permutation actions and their restrictions, medium for the reconstruction of the author's intended convention because the sheet does not state the omitted inner action.

Context: no wreath-product, tensor-power, or w-map comparison in either supplied context file; no neighboring scan.

## A13 — Cote2, scan019, admissibility revision — withdrawn in the same text

Reading “somme de faisceaux” as a direct sum, the cancelled requirement that Young-subgroup modules be “libres sur O_X(S_p1×…×S_pr)” is replaced by O_X-locally-free modules “triviaux” for those subgroups. The replacement admits tensor powers locally: on an open set carrying a basis, words of length n have S_n-orbits with Young stabilizers, and each orbit module is induced from the stabilizer's trivial representation. In particular T^n(O_X)=O_X with trivial S_n-action is included, whereas the cancelled direct-sum condition would make every induced summand group-algebra-free and exclude this rank-one example for n≥2; if “somme” instead permits arbitrary quotient-generated sums, that exclusion would need reconsideration. Confidence is high in the local orbit calculation, but the sentence defining admissibility locally lies inside the deleted block, so a global decomposition or a retained locality convention remains unproved.

Context: no admissibility or Young-subgroup entry in either supplied context file; no neighboring scan.

## A14 — Cote2, scan011, typed §6 — reading question

The typed tensor-power construction explicitly assumes “A commutatif,” but the later phrase read as applications f and g “de E dans E” is followed by T^p(E*) and the canonical map to(T^p(E))*. These types suggest E* as an alternative at the first occurrence, already left doubtful in the frozen transcription; the missing star should be checked in another witness rather than silently inferred. This is reused sesquilinear-algebra material carrying n°234 and printed page−12−, not a proof of the equivariant assertions on016–019.

Context: neither supplied context file contains the typed leaf or a matching numbered witness; no neighboring scan.

## A15 — Cote2, scan013, before equation(17) — reading question

The entry convention u(f_j)=Σ_i λ_ij e_i gives U an n-by-m size, and UᵗRU^J consequently has the required m-by-m size. The frozen words before(17) instead put “m lignes et n colonnes” first inside doubt alternatives, so the dimensional check identifies which alternative is mathematically consistent without changing the reading. The preceding correction from “famille d'…de” to “matrice à…dans” is a separate editorial revision, not evidence that the dimension letters were also corrected.

Context: no matrix or n°234 witness in either supplied context file; no neighboring scan.

## A16 — Cote2, scan015, final remark — self-flagged

A handwritten “?” stands beside the assertion that the preceding formulas remain “valables” for an A-bimodule F, with “à gauche et à droite” underlined. The sheet refers to conditions(1)–(4), which are absent from this package, so the exact scope of the proposed extension cannot be settled merely by treating F as an ordinary central module. The displayed factors2 and4 also distinguish identities that remain formally valid from reconstruction of Φ by division, which needs the corresponding integers invertible.

Context: no polarization/bimodule entry or missing conditions(1)–(4) in either supplied context file; no neighboring scan.

## A17 — Cote2, scan024, normality proof — unproved claim

The reused typed statement “Dans ces conditions, A est normal” is supported by unique factorization and the exponent valuations, but its proof references and last sentence are incomplete on this leaf. The modern result agrees with the assertion(The Stacks Project Authors,2026,Tag0AFV), while the frozen raised A in p_iota^(n_A) is a reading problem: ideal membership x∈p_iota^nA is the natural proof step, not an emendation of the source. No evidence on this sheet connects the typed factoriality argument to the adjoining universal Chern-ring argument.

Context: no factoriality or valuation result in supplied `README.md` or `notes/RESULTS_STATE.md`; no neighboring scan.

## A18 — Cote2, scan026, valuation intersection and localization — unpursued implication

The warning that an intersection of valuation rings of k(X) can have smaller fraction field is essential: with X an indeterminate, intersecting all those containing k gives k, since every nonconstant rational function has a pole on the projective line. Transitivity and localization of integral closure agree with the standard statements(The Stacks Project Authors,2026,Tags00GH,0307,090P), but the editorial request to copy examples from “p.32–39”(first endpoint doubtful) refers to an absent draft rather than providing examples in this package. This reused sheet gives an instructive distinction between an ambient field and the fraction field of the intersection, not a new RR hypothesis.

Context: no integral-closure or valuation counterpart in either supplied context file; no neighboring scan.

## A19 — Cote2, title scans002,009,020,032,040 — unpursued implication

The covers “Contre-exemples,” “Filtration des λ-anneaux…classes de Chern universelles,” “Caractères de Chern covariants…à supports,” and “R.R.des surfaces” confirm the README's placement in intersections/Chern/RR rather than functional analysis. They also show several local units, so the cote should not be treated as one continuously paginated treatise or as evidence for a single chronological layer. The title and pagination inventory below records the visible markers and the absence of an explicit page-count statement.

Context: `README.md`, package246/rank25 and cote2 scans002–045, is confirmed in subject but refined in internal structure; `notes/RESULTS_STATE.md` has no matching planning-result row, only its three separately assessed Hua claims.

## A20 — Cote2, reused leaves011/013/015/024/026/034/036/039 — reading question

The printed sequence−9−,−10−,−12− with n°234, the commutative-algebra leaves−64− and−80−, and the later étale/cohomological draft references belong to reused physical material, not automatically to one original RR pagination. The citation “EGAIV1.9.9.” on034 and the SGA4 textual parallels discussed in the support notes make the blanket catalogue label “[1957]” insufficient for dating every leaf or inscription. This is a stratigraphic question requiring paper-side pairing or additional archive witnesses; it does not supply an exact date for any handwritten block.

Context: `README.md` gives the inherited “[1957]” catalogue placement for cote2 but no physical-side reconstruction; `notes/RESULTS_STATE.md` supplies no chronology entry or neighboring scan.

## A21 — Cote2, scan003, multiplication convention — own idea

For X=P¹_k and a k-rational closed point p, the point-sheaf class [O_p] lies in the rank-zero part and is nonzero in the final K-group, since its Euler characteristic is 1, while ordinary tensor product gives O_p⊗O_p≃O_p. The locally free resolution 0→O(-p)→O→O_p→0 instead gives Tor₀(O_p,O_p)≃Tor₁(O_p,O_p)≃O_p and alternating class 0, showing why the asserted annihilator property needs a derived product or an equivalent convention. Confidence: high for this global test, medium for reconstructing the product on the preliminary ring E from it; compare the Tor-product construction in Borel and Serre (1958, §§4–5).

Context: no Tor-product or annihilator counterpart in either supplied context file; no neighboring scan.

## A22 — Cote2, scan015, formula(14) and final “?” — own idea

A concrete test of the unrestricted bimodule extension is A=C with J=conjugation, E=C, and F=C with usual left action but right action z·a=z·conjugate(a); then Φ(x,y)=xy is J-sesquilinear in the usual bimodule sense and Q(x)=x². At x=y=1 the right side of the printed complex polarization formula(14) is4+i(2i)−i(−2i)=0, while4Φ(1,1)=4, so that formula needs a centrality condition on the two i-actions if this is the intended definition. Confidence: high for the counterexample under those stated conventions, medium for its bearing on the author's question because the absent conditions(1)–(4) could impose additional compatibility.

Context: no bimodule counterexample or defining conditions in either supplied context file; no neighboring scan.

## References used in this block

Atiyah,M.F.(1966). Power operations in K-theory. *The Quarterly Journal of Mathematics,17*(1),165–193. https://doi.org/10.1093/qmath/17.1.165 (Original paper reprinted in the author's1967 *K-theory*, consulted at https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahk.pdf,PDF pp.171–199.)

Borel,A.,&Serre,J.-P.(1958). Le théorème de Riemann-Roch. *Bulletin de la Société Mathématique de France,86*,97–136. https://doi.org/10.24033/bsmf.1500 Original scan: https://www.numdam.org/article/BSMF_1958__86__97_0.pdf

Pedrini,C.,&Weibel,C.(1994). Divisibility in the Chow group of zero-cycles on a singular surface. *Astérisque,226*,371–409. https://numdam.org/item/AST_1994__226__371_0/ (AppendixA,p.404.)

Serre,J.-P.(1977). *Linear representations of finite groups*(L.L.Scott,Trans.;Graduate Texts in Mathematics,Vol.42). Springer. https://doi.org/10.1007/978-1-4684-9458-7 (Induction§7.1 and restriction§7.3; original scan indexed at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-Reps.pdf.)

The Stacks Project Authors.(2026). *The Stacks Project*: Tags0B37(rank and determinant),0AFV(UFDs are normal),00GH/0307(integrality and localization),090P(valuation intersections). https://stacks.math.columbia.edu (individual tag URLs appear in the final bibliography).
