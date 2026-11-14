# Independent proof audits

## Root Part B: full peripheral injection

The proposed proof is sound for a smooth affine geometrically connected curve over an algebraically closed field, excluding only the characteristic-zero affine line. The following points make the proof complete.

Fix one composition series of the original finite local Galois extension, whose finite group is a p-group extended by a prime-to-p cyclic group (cyclic in characteristic zero). Every step is cyclic of prime order. After a global auxiliary covering has produced a completion E_i containing F_i, base-change the next original cyclic extension: E_i F_{i+1}/E_i is cyclic of the same prime or trivial. Globalize this step and continue. There are exactly the original finite number of steps. No restarted tower or unproved decreasing-degree measure is necessary. The Galois closure of the final global cover is finite étale over the open curve; its restricted local action kernel lies in the kernel of the prescribed finite local quotient. This proves injection of the complete local absolute Galois group.

For Artin–Schreier globalization, the principal-parts exact sequence has cokernel H¹(O_X). Its Frobenius-minus-identity map is the additive polynomial v↦Cv^[p]−v with differential −I. It is étale, hence its image is an open subgroup of connected affine space, and is surjective. Lift a preimage of the obstruction class to principal parts and subtract its Artin–Schreier coboundary. The desired local class is obtained exactly, including specified zero local classes at the other cusps.

For a prime ℓ≠p, two cusps x,y permit a Kummer function with divisor x−y−ℓE, using ℓ-divisibility of Pic⁰. For one cusp and positive genus, the pro-ℓ surface presentation maps onto UT₃(F_ℓ), taking one handle pair to the elementary generators. Their commutator has exact order ℓ, including ℓ=2. This realizes the unique tame degree-ℓ local extension. In positive characteristic, the affine-line auxiliary cover y^p−y=x^m with p∤m and (p−1)(m−1)/2≥1 gives positive genus and one cusp. Positive genus persists under finite separable covers by Riemann–Hurwitz; the existence of at least two cusps also persists, because each old cusp has a preimage. Thus the induction stays in the usable range.

## Root B.10–B.13

The orientation, local-support, and compact-support complexes are correct with the stated effective-local and prime-to-characteristic qualifications. The genus-zero/one-puncture exception to the ordinary mixed topos is retained correctly.

The trace hypothesis T′≃T is explicitly supplied by the manuscript: directly viewed LM scan131, folio64, and read LM_P014 lines11–21. Scan132 calls the top trace contragredient to that isomorphism. If φ:T′→T is named, the direction T′∨→T∨ is (φ⁻¹)∨. The derived-duality construction works for the given abstract group homomorphism, without assuming an algebraic or proper geometric realization. Equivariance and arithmetic descent require the group homomorphism, orientation identification, and their coherence to be Γ-equivariant.

B.12's functor on triples preserves finite limits and all colimits componentwise, so it defines the geometric morphism. The collapsed-cusp datum and its specified two-cell are essential. The quotient to the filled group follows because all source peripheral inertia maps into target peripheral normal closure or becomes trivial. B.13's torsor, twisted extension, splitting, and centralizer formulas are correct; trivial automorphism group implies unique isomorphisms within a fixed isomorphism class, not existence or uniqueness of a splitting class.

## Root C.7 and C.11

C.7 should begin with a genuine profinite extension 1→G→E→Γ→1. For N open normal in E, the finite sequence with terms G/(G∩N), E/N and Γ/p(N) is exact. The p(N) are cofinal among open normal subgroups of Γ. The finite classifying-topos pullback is B(G/(G∩N)); coherent inverse limits commute with this pullback, giving B(E)×_{BΓ}Set≃BG. This proves the exact continuous interpretation, using the compatible system of finite torsors and no nonexistent discrete regular Γ-torsor. A finite set of components can be handled by the corresponding finite profinite-groupoid extension.

C.11's inversion is correct. Directly viewed LM scan107: its actual relation is Λ=uΛ′∘(d id_T). Write a=uκ′ and κ=ad. Self-centrality implies a(T)⊂κ(T), hence a=κe and ed=id. This works for any abelian T; since d is an integer scalar it commutes with e, so de=id as well. Thus d is an automorphism of T. For Z and full Zhat, an integer d must be ±1; for prime-to-p Zhat it may be ±p^m. The geometric ramification convention is the reverse relation a=κd.

The final uniqueness fibre in C.11 must be written (i,d)↦Λ_i d⁻¹ when solving for a, or simply as the set of pairs satisfying Λ_i=a d. The expression Λ_i d is equivalent only in the ±1 case. Both stated D∞ and free-group counterexamples are correct.

## Montpellier F.12–F.14

F.12's inverse-limit degeneration proof is correct. F.14's formula Geom(BG,A)=Fun(G,Pt(A)) proves that classifying topoi of discrete groupoids preserve their bicategorical colimits; the example Set⊔_{BZ}Set=Set versus the space pushout S² is correct. Pt(A) is a category if noninvertible two-cells are retained, and its core in the (2,1)-categorical convention.

F.13's finite-cover and two-open pro-pushout calculations are correct. For a globally infinite locally finite cover, mere commutation of filtered colimits and finite homotopy limits is insufficient. The requested repair is to choose neighbourhood stages for each chart datum, double compatibility, triple cocycle, and two-cell comparison; local finiteness makes the requirements finite near each point. A locally finite shrinking and positive continuous radius minorant produce one simultaneous stage. Apply this first for a fixed target, and then take the inverse limit over stages of a pro-target. For non-simple normal-crossings branches, use an étale chart atlas and all fibre products rather than treating normalization maps as globally embedded open tubes. These repairs were sent directly to the Montpellier author.


## Final independent audits of A, F.35–F.39, and F.46–F.49

### A.2–A.4 and A.11

The Boolean-locale proof passes. Boolean disjointification plus the ordinal classification of a Boolean-valued subset of a fixed ordinal proves every sheaf is locally constant without a point argument. A completely prime point of a complete Boolean algebra yields an atom by taking the meet of its filter, so the atomless example has no points. The enough-points/locally-connected reductions in A.3 and the small-projective atom criterion in A.4 also pass.

For A.11 the nucleus from the perfect kernel of the complement preserves binary meets because the perfect kernel of a finite union of closed Polish sets is the union of their perfect kernels. A ball cover in the quotient locale has an ordinary union whose complement is closed and countable. Its complement in a three-dimensional ball is simply connected: polygonal approximation of a loop stays away from that closed set, and a cone vertex can avoid the countably many forbidden planes determined by the loop edges and deleted points. Components of a fixed open remain fixed. These facts justify descent of constant local transition maps to an ordinary covering of the complement. The only suggested wording precision was to transport the trivialization on the original fixed cover and glue there, rather than regard its possibly non-fixed ordinary union as a locale open. This was sent to the owning agent.

### F.35–F.38

The finite-index subgroup/closed-embedding criterion in F.35 and the strict-henselian-DVR limit in F.36 pass. F.37's relative identity twists over a finite field are distinct with the base comparison retained, and cardinality gives the stated failure. F.38 matches the opened Carlson–Stix September 2026 primary version: componentwise universal openness, geometrically unibranch Nagata base, sub-p-adic generic fields, and chivalrous maps are all material. A closed point over a DVR can map to the generic point of the base, so pinned is not a valid replacement for chivalrous in that theorem.

### F.46 and F.47

The punctured-rational-source valuation difference argument was independently extended by the root to algebraic subfields of F Q^ab using the free abelian group M*/mu_infinity. I checked Tsujimura (2022), Proposition4.9, directly: parameter f=1 gives precisely the needed field M=F0 Q^ab. The CRT choices yield multiplicative independence, finitely many integral characters give a nonsingular integer matrix, and its adjugate proves that each completed exponent is integral.

I independently checked the full smooth-curve transfer proof. Corestriction evaluates as the product of residue-field norms. Its residue is the sum weighted by residue degrees, with no ramification factor; a function isolating one rational boundary point therefore detects exactly that residue. Integral residues give a divisor divisible by every integer in Pic. Its degree is zero, and all its dividing classes also have degree zero, so the AVKF input kills it. Unique levelwise unramified lifts are compatible, and AVKF kills their total Picard Tate module. One actual evaluation makes the remaining completed constant actual.

The finite-exception quasi-rationality lemma was written in F.46 for arbitrary smooth proper connected curves. It uses points of arbitrarily large residue degree to force a rational-function identity, so no cardinality claim about the countable algebraic closure is needed. The two shifted outside-field loci cover a cofinite set and have infinite intersection. Varying all translations forces each remaining point value and excludes poles. The constant-factor case is separate.

The higher-dimensional proof in work/foundations/cyclotomic_higher.tex passes: prescribed-point transverse curves detect boundary residues; the Picard/NS lemma retains torsion in NS; divisor classes become principal; the unramified remainder is constant; a second curve through the rational normalization point gives exact pointwise equality. I identified the small bridge from a unit representing the Kummer class after finite constants extension to equality on the original curve. It was repaired using Hochschild–Serre and the rational-point retraction. Applying CHW Theorem4.18 now supplies all sliced etale objects and the full topos morphism, rather than stopping with one point function.

### F.48 source audit

I read work/root/F_source_audit.tex and the actual recovered CYCLOTOMIC B5/C8 rows and C8_hoshi.tex. The arc poset uses closed proper connected arcs, including points. Its groupoid completion is the circle groupoid; strict angular enlargements are necessary for coordinate-independent filters. The sheaf-of-sheets construction yields the actual sector functor, and the once-around calculation is a generator, with the conventional sign between fibre functors and representing covers.

B5's extension, surjective inverse-limit, and nonabelian finite-rank free-group assertions pass. The torsion-free argument via an open subgroup's abelianization is valid. C8's diagonal survives by the strict-trait extension criterion and separatedness. I reopened Hoshi's Lemma2.8 on printed pages175–176 and Carlson–Corwin Proposition3.4 and the proof of Proposition4.12 in their November9,2026 primary preprint. The hypotheses and the retained closure bars agree with the fragment. The blown-up product gives exactly (a,b)->a+b and a nonzero diagonal. I flagged stale unavailable-source sentences in F.19 and F.39 for the root to update.

### F.49 negative field ranges

The relative frame computation is explicit: a central base element changes the comparison on a constant finite cover by u->z composed with u, and the induced framed geometric point is a->z(a). CHW Proposition3.6 was reopened to verify the point identification. For an infinite perfect field, the twist fixes infinitely many rational points but moves a separable point. A polynomial, or a polynomial with finite p-power denominator after perfection, fixing that infinite set must be the identity. All algebraic finite-field extensions are covered, including the algebraically closed endpoint. Every algebraically closed field has a semilinear automorphism fixing an infinite subfield, giving the same obstruction over Set. The exact finite F9 and profinite-coordinate checks are recorded separately in work/montpellier/code/F49_checks.out.


### F.50 and the residual solvable-field audit

F.50 was independently checked in full. The proper-model divisor injection makes the multiplicative quotient free after splitting off its constant subgroup. All division witnesses of one abelian-variety point extend over the same normal spread because each finite etale division fibre has a generic section. The arithmetic-model CRT argument isolates every puncture even when its coordinate is transcendental. For the quasi-rational step, the finite constant field N0=N intersect Qbar and regularity give linear disjointness, hence algebraic numbers of arbitrarily large degree after adjoining all function coefficients. This supplies exactly the high-degree hypothesis needed by the finite-exception proof. No algebraicity of K/Qab is silently used.

The recovered CYCLOTOMIC B2 proof was checked against both primary PDFs: Jarden (2011), Proposition2.5 and definition(2), and Haran–Jarden (1991), Theorem2.4/Corollary2.5. The argument proves trivial ambient centralizer of every nontrivial closed normal subgroup of an absolute Galois group of a Hilbertian field. This is enough for Z(G_Qsolv)=1; it is not silently relabelled as slimness for every open subgroup of an arbitrary closed subgroup. The compact addition to F.44 proves this centralizer assertion, excludes the coefficient-semilinear automorphism route, and gives exact S5 certificates for properness of Qsolv. The new finite program checks the mod2 factorization, twelve mod3 divisions, and derived subgroup orders120,60,60.
