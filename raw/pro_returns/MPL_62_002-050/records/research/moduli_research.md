# Independent post-freeze research: cote 62, moduli and ramification

**Role and evidence boundary.** Research-only report by `/root/moduli_research`, 16 November 2026. All manuscript references below are to the root's frozen diplomatic text; no scan image has been viewed or interpreted by this researcher, and no TeX has been edited. Mathematical qualifications are own calculations, not replacement readings or claims of discovery. The supplied README was read in full and `notes/RESULTS_STATE.md` read before constructing notes; the latter and prior-run notes are treated as claims with their stated review status. This file is an intermediate evidence record for the root's final package.

## Sources and exact contextual links

- **F019–F050:** `MPL_62_002-050_work/pages/MPL_62_002-050_62_scanNNN.tex`, cote 62, scan NNN. Only the frozen text was read.
- **CX16K:** `MPL_62_002-050_context/MPL_16+47+54+44_transcription.tex`, cote 16, scan 52, n°5, text at line 1922: asks for the Kummer description of complete totally tamely ramified extensions by extracting a root of a uniformizer. The corresponding prior-run note is `MPL_16+47+54+44_notes.md`, item **16:52:8**, lines 1651–1655. This is a direct, substantive link to 62:019 and 62:046; the roots-of-unity and residue-field qualifications in the prior note are pertinent.
- **CX16B:** same context transcription, cote 16, scan 21, §8.2, line 882; scan 23, §8.3, line 963. These use the Kummer sequence for the cohomological Brauer group. They provide background for torsors and Brauer obstructions, not the actual classification of genus-zero triples. The intersection discriminant on scan23 is not the cubic discriminant on 62:021–023.
- **CX54:** same context transcription, cote 54, scan 3, lines 2609–2655, universal vector extension and tangent/de Rham duality; scans 5 and 7 continue exterior-algebra and Frobenius–Verschiebung questions. These are a different problem from the genus-zero quotient classification. A claim that the moduli calculation settles those duality questions is unsupported.
- **Hua:** `MPL_62_002-050_context/notes/RESULTS_STATE.md`, **62-triples-rigidified-moduli**, line116, marked a candidate conjecture because the other project's search found no reference. Its “three equivalent ways” describes a standard quotient-stack/descent construction once the objects and hypotheses are specified; failure of a prior literature search is not evidence of novelty. Their range pp41–53 is not identical to this package's scan range. Root reports that scan047 includes handwritten trisection annotations on a reused typed page; do not dismiss that entire scan or all odd scans as irrelevant.
- **LM7 E.30**, same register line76, status **Proved (the return's claim)**, concerns the arithmetic orbifold group of `[P¹−{0,1,∞}/S3]`. This is exactly the stack presented by 62:050, so there is a direct object-level bridge. The manuscript's finite algebraic quotient does not itself prove the register's relative-completion assertion.
- **LM4 E.20**, same register line67, status **Proved (the return's claim)**, concerns the centralizer of geometric S3 inside `Out_lac` of the profinite tripod. This is a different ambient group from `PGL2` in 62:030; the centralizers must not be identified.
- **LM4 D.32**, same register line47, a refereed proved return claim, supplies the three-cusp framework. **LM4 C.12**, line34, and **LM8 A.12**, line23, remain open return claims. A concrete S3-action on P¹ supplies an example already realized geometrically and settles neither the infinite-operator kernel problem nor arbitrary finite profinite-action realization.
- **WG2 §2.4 #4**, register line110, asks about a second Fourier-transform compatibility witness and earlier cote44 theorems. The genus-zero moduli portion supplies neither. **WG H9**, line107, concerns the Mordell–Weil lattice and Hodge index, also not established by this calculation.

A targeted search of the complete supplied transcription and notes for `trisection`, `rigidif`, `normalisateur`, `Kummer`, `Kumm`, `cyclotom`, S3 spellings, `gerbe`, and `mu_2` found no parallel genus-zero-triple classification there. The relevant Kummer hits are CX16K/CX16B; “birigidifié” hits in cote47 refer to Poincaré kernels, not rigidification by the elliptic involution. These negative findings are limited to the supplied files, not the absent source projects named by the register.

## Primary references verified online

**P1.** Silverman, J. H. (2009). *The arithmetic of elliptic curves* (2nd ed., Graduate Texts in Mathematics 106). Springer. https://doi.org/10.1007/978-0-387-09494-6 . Opened full text at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/silverman.pdf ; Proposition III.1.7, printed pp49–50, gives the Legendre invariant and six anharmonic values. Browser refs `turn25view1`, `turn27view0`.

**P2.** The Stacks Project Authors. (2026). *Quotients by group actions* (Tag 04UV). https://stacks.math.columbia.edu/tag/04UV . Objects of a quotient stack are a torsor and an equivariant map. Opened as `turn14view0`.

**P3.** The Stacks Project Authors. (2026). *Kummer theory* (Tag 03PK). https://stacks.math.columbia.edu/tag/03PK . The étale Kummer sequence applies when n is invertible; H¹(mu_n) includes a Picard n-torsion term, so units modulo nth powers alone require an additional Picard condition. Opened as `turn14view1`.

**P4.** The Stacks Project Authors. (2026). *Purity of branch locus* (Tag 0BMB; Lemma 58.21.4). https://stacks.math.columbia.edu/tag/0BMB . The target regularity hypothesis matters. Opened as `turn14view2`; the page identifies SGA1, Exposé X, Théorème 3.1 as the classical source.

**P5.** The Stacks Project Authors. (2026). *Lemma 10.161.8* (Tag 032L). https://stacks.math.columbia.edu/tag/032L . Integral closure of a Noetherian normal domain in a finite separable field extension is finite, by the trace pairing. Opened as `turn25view0`. No excellence or Japanese hypothesis is needed in this precise situation.

**P6.** The Stacks Project Authors. (2026). *Lemma 10.153.7* (Tag 04GK). https://stacks.math.columbia.edu/tag/04GK . Finite étale algebras over a henselian local ring are equivalent to those over its residue field. Opened as `turn14view4`. See also https://stacks.math.columbia.edu/tag/04GE for completeness implying henselianity.

**P7.** Alper, J. (2023, September 19). *Stacks and moduli* [Working draft], Exercise 6.2.32, pp281–282. https://sites.math.washington.edu/~jarod/moduli-versions/moduli-9-19-23.pdf . The exercise explicitly considers the weight-(4,6) to weight-(2,3) map induced by squaring G_m, and rigidification by the elliptic involution. Opened as `turn25view2`, `turn27view1`. This draft's prose has a typographical confusion between the gerbe morphism and its target; use the explicit quotient map, not a verbatim quotation of that sentence. Root also independently verified Stacks Tag072S, the smooth Weierstrass quotient.

## Note candidates (each 1–4 sentences)

### M01 — 62:019; nilpotents and Kummer labels

The explicit qualification that A has no nilpotents is mathematically consequential: `b³=0` or `c²=0` forces b=0 or c=0 only for reduced A. For the genus-zero triple, the resulting special-locus twists are governed by mu3 and mu2 respectively; identifying mu3 with the constant group Z/3 requires a chosen primitive cube root. This is a direct link to CX16K and P3, not an argument for altering any uncertain exponent in the frozen scratch formulas. **Own assessment: high confidence**, from the Kummer sequence and the explicit nilpotent counterexamples M19.

### M02 — 62:021–023; two discriminant conventions

For `f=x³+a x²+b x+c`, the standard discriminant is `D=a²b²−4b³−4a³c−27c²+18abc`, whereas `∏f′(x_i)=−D`. Thus when a=0 the product computed on scan021 is `4b³+27c²`, while the squared difference product explicitly defining Δ on scan023 is `−4b³−27c²`; the question-marked expression `b³−27c²` is neither under these conventions. This is an arithmetic check of a visibly unfinished calculation, not a reading correction and not the intersection discriminant of CX16B. **Own calculation: high confidence**, by the resultant sign `disc(f)=(-1)^{3}Res(f,f′)` or direct symmetric expansion.

### M03 — 62:023; cubic invariant

Put `N=2a³−9ab+27c`; direct expansion gives `4(a²−3b)³−N²=27D`. Consequently the displayed `−N²/(27D)` equals `1−J/1728`, where `J=256(a²−3b)³/D` is the classical invariant of `y²=f(x)`. The intermediate line lacking a factor a in scan023 can be flagged as an internal mathematical inconsistency while preserving the frozen text. **Own calculation: high confidence**, by polynomial expansion; P1 anchors the classical normalization.

### M04 — 62:025; a change of invariant normalization

For `y²=4x³−h(x+1)`, the Weierstrass invariants give `J=1728h/(h−27)`, so the written `h=27j/(j−1728)` uses classical `j=J`. By contrast the quotient invariant on scans023 and040 is `i=1−J/1728`. The scratch pages therefore cannot be read with one globally uniform numerical meaning of j without qualification. **Own calculation: high confidence**, by substitution in the short Weierstrass formula.

### M05 — 62:025–028; anharmonic action and composition convention

The six maps are exactly the relabelling action on the cross-ratio of four points with one distinguished point. With ordinary function composition `λ∘μ=ψ` for `λ(t)=1/t` and `μ(t)=1−t`; the table's `λμ=φ` is consistent with composition read in the opposite order, so this is a convention to state rather than an automatic erroneous identity. P1, Proposition III.1.7 supplies the same six anharmonic transforms. **Own check: high confidence**, by substitution.

### M06 — 62:028–030; scope of the involution

The matrix of `σ(t)=(t−2)/(2t−1)` has determinant3 and square `−3I`, so it defines an involution in PGL2 when3 is invertible; in characteristic2 it becomes the identity. Over a base with6 invertible it commutes with S3, exchanges the two three-point orbits, and fixes the two roots of `t²−t+1`. Thus the later tame hypotheses are essential when stating the nontrivial central involution. **Own calculation: high confidence**, by matrix multiplication and fixed-point equations.

### M07 — 62:030; normalizer requested in the margin

Over `Z[1/6]`, the centralizer of this S3 in PGL2 is `{1,σ}` and the normalizer is `S3×C2`. One proof first diagonalizes a 3-cycle over the cyclotomic quadratic cover: its centralizer is a torus, the transposition acts on that torus by inversion, and the common centralizer is its two-torsion; since every automorphism of S3 is inner, the normalizer follows. This answers the finite algebraic calculation, while **LM4 E.20** concerns a different profinite ambient group. **Own argument: high confidence**, with the prime2,3 exclusions explicit.

### M08 — 62:030–032; the twisted torus

If `S′=S[√−3]`, the automorphisms preserving the unordered pair of cyclotomic fixed points form `T⋊C2`, where `T=R¹_{S′/S}G_m` is the quadratic norm-one torus (equivalently `R_{S′/S}G_m/G_m`). The involution of S′ acts by inversion on its split torus, giving the twisting described in the manuscript. This identifies the algebraic group rather than assuming the multiplicative group is globally split. **Own argument: high confidence**, by diagonalizing the fixed pair and descending.

### M09 — 62:030–032; branch orbits

For6 invertible, the S3-cover has orbits `{0,1,∞}`, `{-1,2,1/2}`, and the roots of `B=t²−t+1`; their ramification indices are2,2,3 and their quotient values are∞,0,1. Scheme-theoretic fibres consequently have these multiplicities, so “the inverse image is X′” needs a reduced-support interpretation where X′ is an étale trisection. The uncertain third fixed point on scan030 is a reading question; the formula for `ν=t/(t−1)` mathematically has fixed points0,2. **Own calculation: high confidence**, directly from fixed loci and the invariant.

### M10 — 62:032; rationality is not global triviality

Smoothness and fibrewise genus zero, even with rational generic fibre, do not alone imply global isomorphism to `P¹_S`; nontrivial projective bundles show the gap in that inference. For the particular constant finite subgroups here the universal construction over `Z[1/6]`, a quotient section, and freeness of rank-two bundles over this PID can supply the missing argument, as can explicit quotient coordinates. This qualifies the justification, not necessarily its conclusion for this universal family. **Own assessment: high confidence**, distinguishing a general implication from this special case.

### M11 — 62:034; proper curve versus G_m-torsor

The whole proper curve `P¹_S/C3` cannot be a G_m-torsor: a geometric fibre of a G_m-torsor is affine G_m, not proper P¹. Its complement of the two designated zero and infinity sections is the associated G_m-torsor; the curve itself is its projective completion. The two ramification sections of the degree3 quotient are the cyclotomic pair, whereas the orbits `{0,1,∞}` and `{-1,2,1/2}` give branch sections for the subsequent degree2 quotient. **Own assessment: high confidence**, by properness and stabilizers, without modifying the frozen terminology.

### M12 — 62:036; extending the squaring map

The formula `g(s)=s²` extends globally as `[u:v]↦[u²:v²]`; these homogeneous coordinates have no common zero over any base. The inference that every map `G_m,S→G_m,S` is a monomial is valid for the universal reduced integral coefficient ring used here, but fails over arbitrary nonreduced S because Laurent rings then have additional units. The manuscript's explicit universal-base reduction therefore does real work. **Own check: high confidence**, from homogeneous coordinates and, for the warning, the unit `1+εs` over dual numbers.

### M13 — 62:038; normalized cyclic quotient

With `d²=−3`, `x′=(1+d)/2`, and `x″=(1−d)/2`, the coordinate `z=(t−x′)/(t−x″)` changes the cyclic quotient to cubing; the stated normalization yields `f=A/(3d q)` for `A=(t+1)(2t−1)(t−2)` and `q=t(t−1)`. Its uniqueness requires the ordered branch normalization and the marked value stated on the page; degree alone and unspecified branch data would not suffice. Under `d↦−d` the coordinate f changes sign, so f itself need not descend while its square does. **Own calculation: high confidence**, by expansion and normalization.

### M14 — 62:040; normalized quotient invariant

The identity `A²=4(t²−t+1)³−27t²(t−1)²` proves that `i=−A²/(27q²)=1−J/1728`, with `J=256(t²−t+1)³/q²`. Thus i=0 is the classical J=1728 locus and i=1 the J=0 locus; the switch is essential when comparing later special-fibre statements with elliptic-curve literature. This is consistent with P1 but should not be imposed on the differently normalized scratch formula of scan025. **Own calculation: high confidence**, by a polynomial identity.

### M15 — 62:040; action of σ on both quotients

Direct substitution proves `f(σt)=1/f(t)` and `i(σt)=1/i(t)`, giving the requested quotient actions including their behaviour at zero and infinity by the global maps. These identities answer the page's explicit question without relying on an inferred picture or revising the duplicated equation number. **Own calculation: high confidence**, because the rational identities extend between projective lines.

### M16 — 62:042; pairs and the intrinsic associated trisection

An étale labelling of the degree-three divisor identifies the pair with `(P¹,{0,1,∞})`, so descent classifies pairs by S3-torsors and makes the central σ descend intrinsically. Applying σ twice returns the original trisection; its fixed bisection is the corresponding twist of the cyclotomic pair. The projective representation of S3 lifts to its rank-two permutation quotient, so the resulting Brauer–Severi curve is a projective bundle, although not necessarily the trivial P¹-bundle. **Own construction: high confidence**, directly from the labelling torsor; P2 gives the general descent framework.

### M17 — 62:044–050; the exact moduli object

Triples `(X,D,s)` with D an étale trisection and s disjoint from D form the quotient stack `[U/S3]`, `U=P¹−{0,1,∞}`: a label torsor T together with an equivariant `T→U` is precisely scan050's datum. The affine i-line is its coarse quotient, retaining inertiaC2 at i=0 and geometric inertiaC3 at i=1, and cannot replace the stack over all bases. This identifies the object in **LM7 E.30** and resolves the interpretation of **Hua 62-triples-rigidified-moduli** as standard descent, without certifying the register's stronger completion claims or claiming novelty. **Own identification: high confidence**, from the explicit equivalence and P2.

### M18 — 62:044–046; the free open

On `V=A¹−{0,1}`, the S3-action is free, so `[U_free/S3]≅V` and the pullback of the universal degree6 étale cover reconstructs the triple from i uniquely, with no automorphisms. This statement remains valid over nonreduced bases because the quotient is a torsor over this open. It is a statement about triples, not classification of elliptic curves over the base by J alone. **Own argument: high confidence**, using the fixed-point list and the quotient-stack definition P2.

### M19 — 62:048; reduced versus nonreduced special fibres

The equations i=0 or i=1 do not force a map to factor through the reduced branch orbit over a nonreduced base: over `k[ε]/(ε²)` with k algebraically closed of characteristic0, `t=−1+ε` has i=0 but is not S3-equivalent to `t=−1`. Likewise `t=ζ6+ε` has i=1 but is not in the constant cyclotomic orbit; H¹ of either constant finite group on this strictly henselian base is trivial. The H¹ classifications therefore require reduced-base or residual-gerbe qualifications, and scan019 had already explicitly noted absence of nilpotents. **Own counterexamples: high confidence**, because i has zero of order2 and i−1 order3 and distinct Möbius transformations have the stated fixed loci.

### M20 — 62:048; the cubic twist is μ3

On a reduced base with6 invertible, the i=1 locus is the neutral residual gerbe `Bμ3`, with reference triple `(P¹,{x³=1},∞)`; its natural classification is H¹(S,μ3). Over Q its label torsor has sign extension `Q(√−3)` and cannot reduce to the constantC3, although the triple exists and has i=1. After a chosen splitting of the cyclotomic cover μ3 becomes constantC3, recovering that version of the assertion. **Own calculation: high confidence**, since affine automorphisms preserving x³=1 and ∞ are exactly multiplication by μ3; P3 explains the Kummer form.

### M21 — 62:048; two distinct quadratic covers

The fixed-point bisection of the twisted triple, when i is a unit, is represented by `u²=1/i` in the normalized middle quotient and hence is isomorphic to the cover obtained by adjoining √i. The sign cover of the labelling S3-torsor instead has square class `−3i`, since the alternating quotient coordinate `r=A/q` satisfies `r²=−27i`. Confusing these two covers would incorrectly remove the cyclotomic twist at i=1. **Own calculation: high confidence**, from the explicit intermediate quotient and the cubic discriminant identity.

### M22 — 62:046; extension and the two proposed conditions

Let S be normal integral, with regular i generically outside0,1, and let T_K be the induced generic S3-torsor; the triple extends precisely when T_K extends to a finite étale S3-torsor T. Once that holds the equivariant map `T_K→U` extends automatically over normal T, because `U→A¹_i` is finite and its coordinates are integral over the base, so the suggested section-extension condition adds no independent obstruction in this situation. The cubic object can be a product of fields, not necessarily a degree3 field extension. **Own argument: high confidence**, by integral closedness and separatedness; this is not a claim that arbitrary rational maps from normal schemes extend.

### M23 — 62:046; finiteness is not étaleness

When S is locally Noetherian and normal, normalization in the finite separable generic algebra is finite by P5, without an added excellence/Japanese assumption. Finiteness alone does not make it an étale torsor; the ramification condition must still be checked. For arbitrary non-Noetherian normal bases the Noetherian submodule argument does not apply, so a finiteness hypothesis must be justified separately rather than silently assumed. **Assessment: high confidence**, with the first statement exactly P5 and the second shown by ramified DVR covers.

### M24 — 62:046; the local valuation test

For a DVR with residue characteristic different from2,3, the tame local models at the finite branch values are `z²=i` and `z³=i−1`, up to units and étale coordinate changes. After pullback, the ramification indices are `2/gcd(2,v(i))` and `3/gcd(3,v(i−1))`, so admissibility requires and locally gives even `v(i)` or `3|v(i−1)` as appropriate. The general normal-base question is stricter than these codimension-one tests. **Own calculation: high confidence**, by Kummer valuation theory; CX16K is the direct manuscript-context link.

### M25 — 62:046; singular normal bases defeat codimension-one sufficiency

Over algebraically closed characteristic0 k, take `R=k[[x,y,z]]/(xy−z²)` and i=x: its principal divisor is twice the height-one prime `(x,z)`, but the cover adjoining √x normalizes to `k[[u,v]]`, via `x=u²,y=v²,z=uv`, and is ramified at the closed point. Thus the pulled-back tame branch cover can be unramified in codimension one and still fail to be étale on a normal singular base. P4's regularity hypothesis explains why purity cannot be applied here. **Own counterexample: high confidence**, by the invariant-ring presentation and nonfree ±1-action at the origin.

### M26 — 62:050; strict henselian classification

A complete local ring is henselian, and an algebraically closed residue field makes every finite étale torsor trivial (P6); after choosing a labelling, triples are therefore parameters t with t and t−1 units, modulo the six transforms. The choice of labelling is noncanonical, while the groupoid/torsor formulation is functorial, matching the margins. This remains true for nonreduced complete local rings and is compatible with the counterexamples M19. **Assessment: high confidence**, by P6 and the explicit quotient description.

### M27 — 62:019,025,050; the elliptic μ2-gerbe

The genus-zero triple is the quotient of an elliptic curve by its central involution, retaining the image of the origin and the unordered other three branch points; it forgets quadratic twisting. With6 invertible, the triple stack has the discriminant-nonzero weight-(2,3) presentation, while the elliptic stack has weights(4,6), and the squaring homomorphism on G_m gives a μ2-gerbe from elliptic curves to triples (P7; root's independently checked Stacks072S). Globally a lift requires a square root of the triple's weight-one line, with its Kummer H²(mu2) obstruction; after one lift is fixed, lifts with a fixed identification of their triple form H¹(mu2). **Own identification: high confidence**, from centering the cubic and comparing the two scaling actions.

### M28 — 62:044–050; explicit forgotten quadratic twist

Over Q, `E:y²=x³+x+1` and `E′:y²=x³+4x+8` have isomorphic triples by `x↦2x`, but are not Q-isomorphic as elliptic curves: a short Weierstrass isomorphism would require `u⁴=4,u⁶=8`, hence `u²=2`. Their common classical J is `6912/31`, so the example lies in the free triple locus and directly separates coarse-invariant classification of triples from elliptic-curve classification. **Own counterexample: high confidence**, by the coefficient transformation equations.

## Supporting derivations and cautions for integration

1. The polynomial identities to check mechanically are `A²−4B³+27q²=0`, `i(1/t)=i(t)`, `i(1−t)=i(t)`, `r(φt)=r(t)`, `r(λt)=−r(t)`, `r(σt)r(t)=−27`, and `4(a²−3b)³−(2a³−9ab+27c)²−27D=0`. Root reports its 21 algebra checks have passed; this report independently derived the displayed identities.
2. The finite map relevant to normal extension is the restriction of `P¹_t→P¹_i` to inverse image of the affine i-line. Its complement is exactly the three poles0,1,∞, hence its source is U. For a normal affine component of T, every coordinate of a generic lift to this finite S-scheme is integral and therefore lies in the component ring; uniqueness glues the extension and preserves equivariance.
3. The cone example is complete and excellent, so its failure is emphatically not a failure of finite normalization. Its double cover has fixed point at the vertex; on the punctured spectrum the ±1-action is free. In the strict henselian local ring, near i=0 the degree6 pullback consists locally of three tame quadratic components, so the quadratic obstruction is already enough to block the S3-torsor extension.
4. At i=0 the reduced triple gerbe is Bμ2, canonically BC2 when2 is invertible. At i=1 it is Bμ3; the underlying C3 inertia over the cyclotomic double cover is descended using inversion. The classical elliptic automorphism groups instead have orders4 and6, respectively, accounting for the extra central μ2.
5. H¹(S,μn) is not generally `Γ(O_S)^*/Γ(O_S)^{*n}`: P3 gives an additional Pic(S)[n] term. Over a local ring Pic=0, so the scratch unit-quotient descriptions have their expected scope.
6. No priority or novelty assertion is supported by these calculations. The register sources beyond the supplied RESULTS_STATE file were not available to this researcher, and no absent source's theorem or proof has been independently certified.

## Review of the root's integrated draft (B01–C21 and A31)

The root's draft `MPL_62_002-050_work/MPL_62_002-050_notes.md` was read as an editorial research document, not as transcription evidence; no edits were made to it. The central arguments in B09 (normalizer), C08 (normal extension), C09 (DVR branch tests), C10 (normal singular counterexample), C11–C13 (special fibres), and A31 (matrix group) are correct under the stated hypotheses.

**Concrete correction sent to root:** B13's initial phrase “adjoining √−3 splits its two ends” conflates two different pairs. The two zero/infinity sections of the middle quotient already come from the two global three-point orbits; the cyclotomic extension splits the degree-three quotient's ramification bisection. The open obtained by deleting the already defined ends is a G_m-torsor. B12's source description also says quotient by Z/3 whereas its three-section trivialization is the one for the full S3 quotient; distinguish the targets.

**Clarifications sent to root:** The quadratic cover in C14 is √i, whereas the sign of the label torsor is √(−3i); C16 can be strengthened to the μ2-gerbe and square-root-line description of M27. The h-family in B06 is smooth only where h(h−27) is invertible, equivalently J(J−1728) invertible after substituting the written formula; cancellation in the rational j-function must not conceal the singular specialization at J=0. B07's multiplication table is consistent with left-to-right composition, although ordinary function composition gives λ∘μ=ψ, not φ.

### M29 — 62:017, as reported by root; matrix-group verification

For the matrices described by root with diagonal `(1,λ²,λ³)` and translation parameter α in position(1,2), multiplication yields a semidirect product `G_a⋊G_m` with weight2 or−2 according to the action convention. Its projection onto the affine action on the pole-two coordinate has central kernel `diag(1,1,±1)≅μ2`, whereas the usual affine group has trivial center, so these groups are not isomorphic when2 is invertible. The assertion becomes correct after passing to that quotient action, which removes precisely the elliptic deck involution. **Own calculation: high confidence**, from matrix multiplication and conjugation; the manuscript's matrix/wording were supplied by root, and this researcher did not reopen scan017 or its TeX.

For explicit convention checking, with
`M(α,λ)=[[1,α,0],[0,λ²,0],[0,0,λ³]]`, one has
`M(α,λ)M(β,μ)=M(β+αμ²,λμ)` and
`M(0,λ)M(α,1)M(0,λ)^{-1}=M(λ^{-2}α,1)`.
The projection to the upper-left2×2 block is fppf surjective onto the affine group, with kernel λ²=1 and α=0; the third diagonal entry λ³=λ retains the nontrivial kernel element. Surjectivity on arbitrary base-valued points should not be asserted, because an affine multiplier need not be a square globally.
