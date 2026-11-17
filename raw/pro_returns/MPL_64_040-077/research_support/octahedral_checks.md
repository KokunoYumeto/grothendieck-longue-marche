# Octahedral checks for frozen cote 64, scans 045–057

Research support by GPT-6 Astra Pro, agent `/root/octahedral_checks`, 17 November 2026. The transcription freeze was **2026-11-17 23:04:47 UTC**; this report uses the frozen text and subsequently opened context, without inspecting scan/crop images or changing transcription, combined text, or doubts. The supplied `context/README.md`, `context/notes/RESULTS_STATE.md`, and `context/hua_project/README.md` were read before using Hua's modernised reading. The local statement IDs below are stable and may be mapped to the main research-note IDs by the parent agent.

**Conclusion.** With 2 invertible, the three-way correspondence between Klein-four subgroup schemes, étale forms of S4 subgroup schemes, and **regular octahedral structures with their opposition retained** is valid; the normalizer, orientation, and descent arguments below include characteristic 3 and characteristic 5. The stronger assertions identifying that S4 with the **full stabilizer of the unstructured six-point divisor**, or asserting a unique opposition on that divisor, fail in characteristic 5. **Hua's project had already identified this exception, its explicit witness, and the five regular structures; these are his prior corrections, independently checked here, not discoveries of this run.**

## Source and context map

| Source | Exact locator | Relationship and status |
|---|---|---|
| Frozen cote 64 | scans 045–047, (1)–(6) | Étale normal form of a faithful Klein-four action and its three axes. |
| Frozen cote 64 | scans 048–050, (7)–(8), stabilizer argument | The full six-point stabilizer is asserted to be étale S4 under only the standing characteristic-not-2 condition; characteristic 5 refutes this stronger statement. |
| Frozen cote 64 | scan 051, definition of regularity and margins | Regularity requires **all combinatorial direct automorphisms to extend to X**; it does not mean that the full six-point stabilizer is the direct group. The orientation margin is compatible with the corrected structured theorem. |
| Frozen cote 64 | scans 052–053, theorem and corollaries | The three sets in the theorem can be retained, but the formula for c)→b) must use the direct group of the chosen opposition; the additional full-stabilizer equality and uniqueness corollary require 5 invertible. |
| Frozen cote 64 | scans 054–057, (9)–(16), both trace margins and final torsor margin on 056 | Four-point Klein action, cubic resolvent, trace conic, and the distinct torsors I and K. |
| `context/hua_project/64.modern.tex` | “II. Structures octaédrales … — 1. Actions du groupe de Klein, configuration octaédrale”, their pp.43–52 = our scans044–053 | **Supports, with the same necessary refinement.** Hua gives the characteristic-five correction, the sum-of-four-points proof, five oppositions, and the structured theorem; his claimed Lean checks are not audited here because the cited Lean file is not supplied. |
| Same | “2. Courbes relatives de type (0,4)”, their pp.53–56 = our scans054–057 | **Supports and adds precision.** The frozen 056 margins explicitly make the constant-I hypothesis superfluous and identify the three degree-four covers; Hua describes his reading of that page and its margins as incomplete. |
| `context/notes/RESULTS_STATE.md` | Hua finding `64-octahedral-configurations-relative`, their pp.44–52 = our scans045–053 | Status supplied: **conjecture/candidate, their search found no reference; intake “new to us: our package … waiting.”** The excerpt is truncated; the structured claim visible in it is supported by the proof here, without establishing literature novelty or auditing unseen text. |
| `context/LM_140-2_text.tex` | scan363, Fermat conic paragraph | **Restates the geometric model; adds a relative construction.** The exponent-two quotient and the explicit conic already appear there; the surrounding normalizer/arithmetic claims are explicitly hypotheses and are not settled by these calculations. |
| `context/MPL_142_094-122_notes.md` | B01, scan108 | Prior first-pass note with the same Klein group and quotient `q(z)=z²+z⁻²`; it points to `LM_140-2_text.tex`, scans568–571. The present report uses only the elementary quotient formula, rechecked below, not its proposed modular identifications. |
| `context/MPL_146_001-099_notes.md` | R084, scans065,067 | Prior first-pass note giving `g₂(z)=−(z²−1)²/(4z²)` with the same Klein deck group; this is the same quotient after `g₂=(2−q)/4`, rechecked below. |
| `context/LM_140-1_text.tex` | scan17, orientation/torsor discussion around `Pol_τ` | **Conceptual parallel only.** Its use of unoriented polyhedra and orientation data is consistent with the torsor distinction here; it is not a proof of the algebraic μ4* identification. |
| `context/notes/RESULTS_STATE.md` | `LM4_SUCCESSOR B.38`; `LM4 D.12`; `EXIT_TOWER E.24` | All **Open (the return's claim)** in the supplied register. A characteristic-five stabilizer exception is not a level-five congruence-kernel result, an S4 action is not a classification of profinite GT torsion, and the orientation character is not an arithmetic-image computation. |

## Proposed note items

### OCT-S01 — The axes and normal form need only 2 invertible

**Scans:** 045–047, (1)–(6). **Kind:** targeted proof check. **Status:** verified in the stated relative sense.

Étale locally, a faithful Klein-four subgroup has the form `V={z,−z,1/z,−1/z}`, with three disjoint degree-two fixed divisors `{0,∞}`, `{±1}`, and `{±i}`. Splitting the first axis, writing the second commuting involution as `a/z`, and adjoining a square root of the unit a gives the displayed normalization; adjoining i is also étale because 2 is invertible. This supports Hua's modernised reading, §II.1, and does not require excluding characteristic 3 or 5. See Proof A.

### OCT-S02 — The normalizer survives the characteristic-five exception

**Scans:** 052–053, a)→b), quotient margin. **Kind:** independent re-proof. **Status:** verified.

For the standard V, its centralizer is V and its normalizer is a finite étale form of S4, with exact sequence `1→V→N(V)→Aut(V)→1`, where `Aut(V)` is locally S3 (constant S3 when V is constant); no claim is made that this sequence has a canonical splitting or is surjective on S-rational points. The generators `z↦iz` and `z↦(z+1)/(z−1)` realize two transpositions of the three nonidentity elements of V, and the induced action on the four antipodal face pairs identifies the resulting group of order24 with S4. This proof works in characteristic 3 as well as 5 and supports the precise normalizer part of Hua's corrected theorem. See Proof A and the finite-field certificate.

### OCT-S03 / OCT-S03R — Full divisor stabilizer: the missing hypothesis is 5 invertible

**Scans:** 048–050, (7)–(8), final stabilizer conclusion; 053, c)→b). **Kind:** refuted assertion with refined statement. **Status:** original full-stabilizer assertion refuted; refinement verified.

Hua already observes that in characteristic 5, with i=2, the six-point divisor is all of `P¹(F5)`, so its full stabilizer has order120, whereas the normalizer of a chosen Klein group has order24. His witness `z↦2z+1` fixes ∞ and −1 but changes the standard opposition, directly refuting the final pair-fixer conclusion of scan050 under only 2 invertible. With 5 also invertible, Hua's sum argument gives `5(a−1)=0` for a putative fixer `az+(a−1)`; together with the order24 normalizer this proves that the full stabilizer is exactly S4, including characteristic 3. Over `Z[1/2]` the full stabilizer scheme of the standard divisor is finite and unramified but cannot be étale across characteristic 5, since its geometric fibre size jumps from24 to120; see Proof B.

### OCT-S04 / OCT-S04R — Five regular oppositions, not a unique one, in characteristic 5

**Scans:** 049–051 and 053, Corollary1. **Kind:** refuted assertion with refined statement. **Status:** uniqueness refuted in characteristic5 and verified with 10 invertible.

The divisor `P¹(F5)` has exactly five regular opposite-pair structures, as Hua had already stated; the other ten perfect matchings have projective stabilizer order12 and cannot be regular. Exhaustive enumeration recovers five matchings with stabilizer24, one orbit under the full order120 group, and a faithful permutation action on those five structures, also certifying `PGL₂(F5)≅S5`. The claim of uniqueness becomes valid when 5 is invertible, because the direct S4 is then the full stabilizer and its characteristic normal V4 recovers the three axes. The source's definition of regularity itself survives; the failure concerns forgetting its opposition.

### OCT-S05 — Characteristic 3 is covered by a proof, not merely by a small-field test

**Scans:** 050, marginal arithmetic; 052, standing hypothesis. **Kind:** targeted proof check and computation. **Status:** no characteristic-three exception to the corrected assertions.

The normalizer proof uses only 2 invertible, and the full-stabilizer proof uses 2 and5 invertible, so both apply over every field of characteristic3 and, étale locally, over arbitrary bases with those residue characteristics. The independent exhaustive `F9` test gives normalizer and full six-point stabilizer order24, while the `F13` control gives the same and `F5` gives24 versus120. Beauville's primary paper works under the order-prime-to-characteristic convention and therefore cannot by itself justify an S4 assertion in characteristic3; its relevant normalizer calculation is complemented here by the direct proof. The finite-field computations are illustrative certificates, not a substitute for that general argument.

### OCT-S06 — What Hua's relative finding actually needs

**Scans:** 051–053, theorem. **Kind:** independent re-proof. **Status:** verified after retaining the structure and correcting c)→b).

The three-way correspondence on a fixed étale form X of the projective line is between V4 subgroup schemes, étale S4-form subgroup schemes, and degree-six divisors **equipped with a regular fixed-point-free opposition**. From V one takes its three axes; from S4 one takes its unique normal V4; from a regular opposition one takes the full combinatorial direct group whose extension is part of regularity. Thus the visible claim in **Hua, findings register, `64-octahedral-configurations-relative`** is supported even in characteristic5, but the manuscript's additional identification with `Aut(X,Δ)` is not. This is an elementary relative proof of the stated precision, not a novelty judgment on Hua's candidate or an audit of the truncated findings excerpt.

### OCT-S07 — μ4* is the orientation torsor, not a chosen global orientation

**Scans:** 051, final margin; 053, Corollary2. **Kind:** independent re-proof. **Status:** verified for a chosen regular opposition.

At a vertex, an octahedral orientation selects a generator of its direct C4 stabilizer, and the multiplier on the tangent line is a primitive fourth root; direct transitivity makes it independent of the chosen vertex. Reversing orientation inverts that multiplier, giving a canonical isomorphism `Or(Δ)≅μ4*` of μ2-torsors, compatible with base change and descent, without choosing i globally. Consequently every projective automorphism preserving a chosen opposition is direct, whereas in characteristic5 a projective automorphism of the bare six-point divisor may change the opposition. See Proof C; the connection with the orientation discussion of `LM_140-1_text.tex`, scan17, is conceptual only.

### OCT-S08 — Degree-four covers and the reference anisotropic conic

**Scan:** 053, Corollary2 and reference model. **Kind:** independent re-proof. **Status:** verified for structured objects.

The conic `C0: x²+y²+z²=0` with its sign-change V4 has constant automorphism group S4 as a **structured** object, so étale descent identifies its forms with S4-torsors, equivalently finite étale covers of degree4. The four-element cover is the set of antipodal face pairs, or equivalently the four Sylow3 subgroups of the direct S4; this remains meaningful in characteristic3 because the group scheme is étale, even though its projective order-three elements are unipotent. A concrete construction from a degree-four étale algebra A uses `E=ker(Tr:A→O)` and `Tr(u²)=0` in `P(E)`, which becomes the displayed C0 after a basis change requiring only 2 invertible. See Proof D; if the opposition is omitted in characteristic5, the automorphism group120 already prevents this equivalence.

### OCT-S09 — A geometric S4-form need not have 24 rational points

**Scans:** 052, “forme” of PGL; 053, anisotropic-real margin. **Kind:** independent re-proof. **Status:** verified; excludes a false stronger interpretation.

For standard V on `P¹_R`, the normalizer has only eight real points: its action on the three axes must fix the unique non-real axis `{±i}`, and the real map `(z+1)/(z−1)` realizes the remaining transposition. By contrast, the conic `x²+y²+z²=0`, which has no real points, carries a constant S4 through signed coordinate permutations modulo simultaneous sign change. Thus “locally isomorphic to S4” concerns a finite étale group scheme and “projective-line bundle” here must include étale forms, not only a globally split P¹ or a projectivized rank-two vector bundle. The `F9` certificate additionally finds eight `F3`-rational points in the normalizer of the same standard V, a finite-field illustration of the distinction.

### OCT-S10 — The trace conic and its quotient descend, also in characteristic3

**Scans:** 055–056, (11)–(13), trace margins. **Kind:** independent re-proof. **Status:** verified.

For a cubic finite étale cover `p:J→S`, the trace pairing of `A=p_*O_J` is nondegenerate, so `Q(u)=Tr(u²)` defines a smooth conic with 2 invertible; the separate quotient line is `Tr(x)=0`, and the map is `x=y²` in the étale algebra. After splitting J, this is coordinatewise squaring from `Σ y_j²=0` to `Σ x_j=0`, a finite flat map of degree4 with sign-change group `F₂^J/F₂` and branch divisor formed by the three coordinate-zero points. In characteristic3, `Tr(1)=0` does not make the trace map zero or the pairing degenerate, and the conic is not the intersection of Q=0 with the trace-zero line in the same copy of the projective plane. This adds the global descent verification to Hua §II.2 and is the relative version of the Fermat-conic example in `LM_140-2_text.tex`, scan363.

### OCT-S11 — The canonical four-point Klein action is smaller than a general permutation action

**Scan:** 054, Proposition. **Kind:** independent re-proof. **Status:** verified.

Étale locally normalize the four marked points to `∞,0,1,λ`; their three double transpositions extend as `λ/z`, `(z−λ)/(z−1)`, and `λ(z−1)/(z−λ)`, with λ and λ−1 units. A projective transformation is determined by three distinct sections, so these formulas glue and the extension is unique. This proves precisely the canonical V4 extension in the source and Hua §II.2, without claiming that every permutation of a general four-point divisor extends. See Proof F.

### OCT-S12 — K and I are distinct torsors; a constant marking is unnecessary

**Scans:** 055–057, (11), (14), (16) and 056 margin. **Kind:** targeted proof check. **Status:** verified.

If `F_x` is the fibre of the reference Klein cover above the section x, then `I≅K∧_V F_x` and, because V has exponent2, `K≅I∧_V F_x`; this is the source's relation between the two degree-four torsors. Thus a fixed nonconstant I is as usable as a constant numbered I, precisely as scan056 states, and the three covers `I`, `J⊔S`, and `K` must not be merged. Hua §II.2 already records the relation but says his reading of this page's margins was incomplete; the frozen text adds the explicit removal of the constancy hypothesis and the list of the three covers. The identity condition in relative H1 retains the specified V-monodromy identification: geometric connectedness alone would permit all six automorphisms of V.

### OCT-S13 — The two contextual quotient formulas differ only by target normalization

**Scans:** current 055–056; contextual cote142 scan108 and cote146 scans065,067. **Kind:** used and rechecked in this run. **Status:** elementary formula verified, contextual modular interpretation not inferred.

The standard Klein group fixes `q=z²+z⁻²`, and `−(z²−1)²/(4z²)=(2−q)/4`, giving a direct identification between the formulas in `MPL_142_094-122_notes.md` B01 and `MPL_146_001-099_notes.md` R084. The supports of their three branch fibers are the same opposite pairs `{0,∞}`, `{±1}`, `{±i}`, so they are coordinate versions of the cover in scan056. This comparison supports the geometric correspondence with `LM_140-2_text.tex`, scan363; it does not identify distinct modular covers merely from a shared finite group.

### OCT-S14 — Scope relative to the supplied open-result register

**Scans:** 045–057. **Kind:** carried as background without fault found. **Status:** the named open problems remain open here.

The octahedral model supplies explicit finite group actions and descent data, but none of these pages or calculations determine the congruence kernels in **LM4_SUCCESSOR B.38**, classify torsion in the full profinite groups in **LM4 D.12**, or determine the arithmetic image in **EXIT_TOWER E.24**. Their exact supplied status is **Open (the return's claim)**, and the present characteristic-five exception concerns a different question from the level-five kernel. The conic paragraph of `LM_140-2_text.tex`, scan363, itself keeps the surrounding arithmetic/normalizer assertions hypothetical, so there is no justification for upgrading those register entries.

### OCT-R01 — Reading and interpretation questions left outside the transcription

**Scans:** 047, 052–054, 056. **Kind:** reading question. **Status:** no image-based adjudication by this agent.

The alternating D2/D4 notation and the written “icosaédrales” are retained diplomatically; the context and Hua's explicit editorial correction support interpreting the theorem as Klein-four/octahedral, not changing its ink. In scan053 the inserted `Or(Δ)≅μ4*` is crowded: the mathematically consistent equivalence equips the **abstract octahedron** with that isomorphism, while a geometric structured pair already has a canonical one; treating it as a second arbitrary choice on the geometric pair would add two components. In scan054, the final “torseur … sous V*” cannot literally use the three-element nonidentity locus as a group, and the preceding sentence and Hua §II.2 support V; scan056 likewise mixes x/y names while the trace formulation fixes their roles. These are post-freeze questions of attachment/notation, not reasons to revise the frozen pages.

## Compact proofs and certificates

### Proof A — Normalization, normalizer, and the structured correspondence

Work étale locally on a base with 2 invertible. Split the first involution's two fixed sections and identify them with 0 and ∞, so it is `s(z)=−z`. A second, distinct commuting involution interchanges those two sections and has the form `t(z)=a/z` for a unit a; after adjoining a square root of a, rescaling gives `t(z)=1/z`. Its product with s is `−1/z`. Their six fixed sections are distinct after adjoining i, since all relevant differences among 0,±1,±i are units when 2 is invertible.

The centralizer of s in PGL2 consists of diagonal and antidiagonal projective matrices. Imposing commutation with t reduces these to `{1,s,t,st}`; this also computes the **group scheme** centralizer, since the residual equations are square-equals-one and 2 is invertible. Conjugation therefore embeds `N(V)/V` in `Aut(V)=S3`. The maps `r(z)=iz` and `h(z)=(z+1)/(z−1)` normalize V, inducing different transpositions of its three nonidentity elements, so the map onto S3 is surjective and N has degree24. The entries and all denominators used require only 2 invertible.

These transformations preserve the three opposite pairs and act as direct octahedral symmetries. In the ordered-axis model, their determinant signs are +1; alternatively, use the signed-coordinate-permutation model of `x²+y²+z²=0`, modulo its central simultaneous sign change. That group acts faithfully on the four antipodal pairs of triangular faces and is S4. Étale descent gives the claimed finite étale normalizer over the original base, whether or not it is constant there.

Every S4-form has a unique normal Klein-four subgroup. In an embedding into `Aut(X)`, the S4-form normalizes that V and hence equals its normalizer by the degree24 calculation. Conversely, for a regular opposition the direct S4 acts on X by definition and its characteristic V4 gives the three axes that recover the chosen opposition; this is checked in the standard six-vertex model. These inverse constructions prove OCT-S06 on arbitrary bases with 2 invertible.

### Proof B — The full six-point stabilizer and the characteristic-five jump

Over an algebraically closed field, let `Δ={0,∞,1,−1,i,−i}` and let G be its full stabilizer. A map fixing ∞ and −1 is `g(z)=az+(a−1)`; it permutes the other four points C, whose sum is1, so `1=Σ_C g(z)=5a−4`. If 5 is invertible, a=1. Since an element of G is then determined by its images of this ordered pair, `|G|≤6·5=30`. The subgroup N(V) already has order24, so Lagrange's theorem forces `|G|=24`; this establishes the assertion in characteristic3 without appealing to tame finite-subgroup classification.

In characteristic5, Δ is all of `P¹(F5)`. Any geometric projective map preserving Δ has coefficients in F5 because the images of three F5-rational points uniquely determine it. Consequently `G=PGL₂(F5)` and `|G|=(5²−1)(5²−5)/(5−1)=120`. The map `2z+1` cycles `0→1→3→2→0` and fixes4=−1 and∞. It changes the pair `{0,∞}` to `{1,∞}`, so it preserves the divisor but not the standard opposition.

After splitting Δ, the full relative stabilizer embeds as a closed subscheme of the constant permutation scheme S6: a permutation of three sections gives a unique projective transformation and the remaining three equalities are closed conditions. Hence it is finite and unramified. Over `Z[1/10,i]` the preceding geometric proof leaves only the 24 components already occupied by N(V), proving relative equality and étaleness there. Across characteristic5 the extra geometric points force nonflatness, so the preceding “net” claim of scan048 survives while its asserted étaleness does not.

For the characteristic-five uniqueness issue, there are 15 matchings of six vertices. The certificate checks every matching and every projective transformation: five have stabilizer24 and form the orbit of the standard regular structure; ten have stabilizer12 and therefore cannot contain the required 24 direct automorphisms. This also proves that no regular structures were omitted, including after algebraic closure, by the three-point rationality argument just given. The characteristic-five observation, the displayed witness, and the sum argument are all credited to **Hua, modernised reading of cote64, §II.1**.

### Proof C — Canonical orientation multiplier

Given an orientation o of the combinatorial octahedral sphere and a vertex v, the cyclic order on its four neighbours selects a generator `r_{v,o}` of its direct vertex stabilizer C4. The extension of this generator to X has tangent multiplier `χ(r_{v,o})` at v; in the standard model it is i or−i. If a direct symmetry sends v to w, it conjugates the selected generators and the derivatives are equal, so the multiplier does not depend on v. Reversing o replaces the generator by its inverse, and hence replaces the primitive fourth root by its inverse. This defines the canonical μ2-equivariant isomorphism `Or(Δ)→μ4*`, with no chosen trivialization.

The construction commutes with projective isomorphisms and base change. An automorphism preserving the chosen opposition must therefore preserve this orientation torsor over μ4*, so it is direct. There is no claim that a map preserving only the divisor preserves the chosen opposition. The group of all abstract octahedral automorphisms is `S4×C2`, the central C2 being antipody; specifying the orientation torsor to be μ4* fixes that C2-twist and leaves precisely an S4 torsor.

### Proof D — Descent and a quadratic form from a quartic cover

Let `C0⊂P²_{Z[1/2]}` be `x²+y²+z²=0` and let V0 act by sign changes modulo simultaneous sign change. Signed permutation matrices modulo the central `±I` give 24 global projective automorphisms; by Proof A these exhaust `Aut(C0,V0)`, making it the constant S4 scheme. Every structured pair is étale locally isomorphic to `(C0,V0)` by Proof A, and effective descent for the conic, its action, and its finite étale axes identifies the groupoid of such pairs with S4-torsors. The standard action of S4 on four letters gives the corresponding finite étale degree-four cover; the four Sylow3 subgroups are its four point stabilizers' order-three subgroups and recover that same S4-set.

For a direct model, let A be the rank-four finite étale algebra of the cover and let `E=ker(Tr:A→O_S)`. Since `Tr(1)=4` is a unit, E is a rank-three direct summand and the nondegenerate trace pairing restricts nondegenerately to E. When `A=O_S^4`, take the basis

`u1=(1,1,−1,−1),  u2=(1,−1,1,−1),  u3=(1,−1,−1,1)`.

Its determinant in a standard basis of E is4, and `Tr((x u1+y u2+z u3)²)=4(x²+y²+z²)`. Permuting the four factors induces the signed-permutation projective S4 action, and its distinguished V4 descends. Thus the construction works with only 2 invertible, including characteristic3. Over R the trivial four-cover gives the anisotropic conic C0, showing why a globally split P¹ interpretation would be too restrictive.

### Proof E — Cubic trace model and the degree-four quotient

For a cubic étale algebra A, the trace pairing is locally the ordinary dot product on `O_S^3`, hence nondegenerate. The conic `Tr(y²)=0` is therefore smooth when 2 is invertible. Squaring in A gives a globally defined map between the two projective bundles, because multiplication is intrinsic and becomes coordinatewise squaring after splitting A. The preimage of the line `Tr(x)=0` is precisely this conic. Locally on the target projective plane, the squaring map has two free square-root coordinates and is finite flat of degree4, so its base change to the line has the same degree.

The sign-change group modulo diagonal sign is `V_J=F₂^J/F₂`. Away from the three coordinate-zero points of the target line its action on the conic is free, and the squaring map is a V_J torsor. At each of those points the fibre has two geometric points, each ramified with index2. All expressions are invariant under permutations of J, proving descent for a nonconstant cubic cover. The trace map is locally `(a,b,c)↦a+b+c`, still surjective in characteristic3; its value on 1 does not control its rank.

### Proof F — Four-point extension and the two torsors

For four disjoint sections `∞,0,1,λ`, the three formulas in OCT-S11 have determinants respectively `−λ`, `λ−1`, and `λ(1−λ)`, all units. Direct substitution gives their double-transposition actions and compositions, so their projective transformations form V4. The uniqueness of a projective transformation with specified images of three sections proves equivariance under relabelling and descent of the action.

Writing the reference V-cover as F over the punctured quotient, the twisted cover is `X*=K∧_V F` and its fibre at x is `I=K∧_V F_x`. A V-torsor T has a canonical trivialization of `T∧_V T`: the class of `(t1,t2)` maps to their difference in V, well-defined because 2V=0. Thus contracting the fibre identity again by F_x gives `K=I∧_V F_x`, without a section of I or a constancy hypothesis. The three nontrivial local inertia elements of the punctured three-point line sum to zero, so its maximal elementary-2 quotient is V_J; a geometrically connected V-torsor gives an automorphism of V_J, whereas the source's “admissible” condition specifies the identity automorphism.

### Certificate record

The package contains `octahedral_certificate.py` and its actual output `octahedral_certificate.json`. It exhaustively enumerates normalized non-singular 2×2 matrices over F9, F5, and F13, verifies the field operations used, computes full divisor stabilizers, centralizers and normalizers, tests all 15 opposite-pair partitions, and checks faithful actions on four face pairs and (in characteristic5) five regular structures. F9 is implemented explicitly as `F3[t]/(t²+1)`; no symbolic package or unprovided formal file is needed. The last run completed successfully at the UTC time embedded in the JSON.

| Field | PGL2 order | Full six-point stabilizer | N(V) | C(V) | Fixer of ∞ and−1 | Regular oppositions |
|---|---:|---:|---:|---:|---:|---:|
| F9, characteristic3 | 720 | 24 | 24 | 4 | 1 | 1 |
| F5 | 120 | 120 | 24 | 4 | 4 | 5 |
| F13 | 2184 | 24 | 24 | 4 | 1 | 1 |

**OCT-S15 — Pointwise versus setwise stabilizers (scan049).** For every displayed field, the pointwise fixer of `{0,∞}` has order4 and its setwise stabilizer has order8. Thus the manuscript's scan049 wording “fixe 0 et∞” must be read pointwise; Hua's shortened phrase “stabilisateur de {0,∞}” should not be upgraded to a setwise order-four assertion. In characteristic5 the full single-vertex stabilizer instead has order20, explaining why the “equal cyclic order-four isotropy groups recover opposites” argument fails for the full group there.

## Primary-source check and limits

The external source actually consulted was **Arnaud Beauville, “Finite subgroups of PGL(2,K)” (2009), arXiv:0909.3942**, [abstract](https://arxiv.org/abs/0909.3942), [paper](https://arxiv.org/pdf/0909.3942), Proposition1.1 and Theorem4.2 with its proof. It explicitly restricts to group order prime to the characteristic, gives the criterion for a constant S4 subgroup of PGL2(K), and identifies the geometric Klein-four normalizer with S4 using the same two displayed generators. Its field-level result does not supply the relative conic/divisor/degree-four-cover equivalence, and it is not used to cover characteristic3. No secondary exposition, unseen Lean source, or unprovided findings-register text is treated as verified.

No part of this support report adjudicates the title-leaf count, reads fresh images, changes diplomatic readings, or performs the parent agent's scans042–043 or064–065 algebra checks. Check events for the mathematical statements above are recorded separately in `octahedral_CHECK_EVENTS.tsv`.
