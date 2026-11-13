# Compactifications: proof and source audit

This contribution treats Parts 2 and 3, and both interpretations of the cuspidal fibre in Part 1(e). The authoritative attachment was PROMPT(20261112-211252).md; the archived prompt was not substituted for it. The original workspace was lost twice during runtime outages. The present files restore the complete mathematical text retained during those outages.

## Deliverables and status

- sections/compactifications.tex: blow-up criterion, end invariance, surface classification, six examples with analytic qualifications, elementary fibrations, profinite inertia, toric comparison, and projective birational reductions.
- sections/cusp.tex: affine and projective cusp resolutions, the entire eight-object exit category, roots, and the good two-object orbifold replacement.
- code/compactifications_checks.py and its JSON output: exact finite checks of matrices, cusp substitutions, root-index kernels and toric examples.
- notes/compactifications_results.csv: every numbered statement, including every new lemma and the explicitly unproved restricted comparison question.
- notes/compactifications_readings.csv: manuscript reading provenance and uncertainty.
- notes/compactifications_references.bib: verified primary references and precise theorem locations.

**Unresolved item:** P3c-general is a restricted scheme comparison question for arbitrary nontoric smooth algebraic threefolds. It is not proved or refuted here. The requested toric zigzag is proved in every dimension. The unrestricted analytic and stack versions are refuted. A common smooth roof made solely by ordinary stratal blow-ups is a different request; the weighted stellar-subdivision theorem does not supply it. Under the user's completion rule, the task must retain INCOMPLETE status if settlement of P3c-general is required. No statement that a question is unproved here is presented as a proof of its status in the literature.

## Proof corrections retained

### Blow-ups

The centre has local equations (x_1,...,x_s,y_1,...,y_t). For t>0, the y_1 chart contains the exceptional divisor and all s old strict transforms. Their full lattice has matrix [I_s | 1] and primitive kernel (−1,...,−1,1). Inspecting only the exceptional meridian is insufficient: it may remain infinite. For t=0, replacing one basis vector by the sum of the centre's normal vectors is unimodular. Disconnected unions of smooth stratal centres are allowed.

Reverse asphericity uses the old punctured normal bundle P_S→S. Its connecting homomorphism has image killed in the open complement, so full meridian injection makes it zero. Its projection is the connecting map of the exceptional torus bundle Q→S. Asphericity of Q then forces asphericity of S. No natural map Q→U is asserted.

The end statement follows from cofinal punctured neighbourhoods under the proper blow-down. With compact boundary and collar links it gives ordinary link homotopy type; for a nonproper ambient space it concerns only the specified boundary end.

### Surfaces and analytic scope

Core means pruning genus-zero vertices of valency at most one, retaining positive genus and counting a self-node twice. Common point resolutions of two core pairs have every noncore curve exceptional over both endpoints. Contracting a last-created noncore curve preserves both projections and produces a common corner refinement.

The nonemptiness criterion starts with an arbitrary completion in one marked meromorphic class. It requires asphericity of U, smooth contractibility of the entire rational fringe, and full generic/node meridian injections on the resulting core. This is not merely a restatement that some good model exists: the candidate is obtained by explicit contractions from the given completion. No algorithm for arbitrary group injectivity is claimed.

Minimality is boundary minimality. Uniqueness in a meromorphic class holds exactly when every smooth rational bivalent component has square at most −2 and every singly self-nodal rational bivalent component has square at most 2. Resolving a multiplicity-two self-node lowers its square by four.

In the analytic category the identity of an open surface need not extend meromorphically, so the global classification is a union over marked meromorphic classes. An algebraic marking has one birational class. The Hopf examples make this distinction substantive.

The first three examples have finite fundamental groups: 1 for C², Z/2 for a smooth-conic complement, and Z/3 for an irreducible nodal-cubic complement. These obstruct every analytic completion. The conic calculation uses ordered versus unordered configurations of two points of P¹; the cubic calculation uses two-strand braid monodromy and the degree-three relation at infinity.

For analytic (C*)², Ueda's classification leaves rational core cycles, hence toric pairs, and one-curve Hopf pairs as the good models. The Serre affine-line bundle has trivial normal meridian. A holomorphic marking can create another meromorphic class even on the same toric pair, for instance (x,y)↦(x,e^x y).

For C* times the three-punctured sphere, minimal analytic marked classes form the relative Picard group of a holomorphic line bundle on P¹ with a specified trivialization over the punctured base. The fixed fibre coordinate labels the zero and infinity ends: no inversion quotient is taken. Algebraic trivializations give only the smaller Z³ divisor classification. The hyperbolic projection extends by the proved local Picard lemma. The rank-two direct image p_*O(S) gives a meromorphic map to a Hirzebruch surface, proving rationality without assuming an ambient minimal surface.

For a product of two affine hyperbolic curves, both projections extend by the Picard lemma, putting every analytic completion in the product's meromorphic class. The product is its unique minimal good completion.

The Picard proof uses a finite étale target cover with compactification of genus at least two, a Kummer source cover killing finite local monodromy, Schwarz–Pick and positive systole to kill each coordinate loop, a bounded lift to the disc, removable singularities, maximum modulus, and deck descent. Explicit degree-five and degree-three covers handle genus zero and one.

**Rejected shortcut:** Vo Van Tan's nonprojective compactification argument assumes minimal compact surfaces. Steinness only forbids compact curves wholly contained in U, not (−1)-curves meeting U. Contracting the latter can change U. That theorem is not used to infer projectivity of arbitrary analytic completions; the direct Picard/direct-image proof replaces it.

For the stack comparison, the invariant is triviality of all inertia under an ordinary representable blow-up. A nonidentity stabilizer element over the centre fixes an eigenline in the projectivized normal representation, so some inertia survives upstairs. Generic inertia on a particular boundary divisor is not invariant and is not used.

### Elementary fibrations and completion

Horizontal fibre injection holds over any connected base: the image of π₂(base) in the fibre group is central by the clutching-square argument, and a nonabelian free group has trivial centre.

Profinite injection is proved separately. The centre of a finite-rank nonabelian free profinite group is trivial by a mod-p finite regular rose-cover argument: the homology module contains a regular summand and its quotient-group action is faithful. Conjugation into the profinite automorphism group embeds the completed free normal subgroup into the completion of any extension. An immersed labelled circle completed to a finite graph cover proves full induced profinite topology on every nontrivial cyclic subgroup.

Vertical injection explicitly requires the base's full discrete lattice injections and, for the profinite conclusion, its completed full-lattice injections. Compatible recursively stable/toroidal towers establish these inductively. Stable extension on an arbitrary base completion is insufficient: blow up a smooth boundary point of the product of two three-punctured spheres, then take a constant hyperbolic fibre. The resulting genuine three-stage tower retains a rank-two vertical kernel.

The equivalence of full local arithmetic injection and geometric inertia injection requires an injective map on Galois quotients. This holds in the indicated closed-point/finite-field-extension setting, but need not hold for transcendental residue fields.

### Cusp

The affine group is <a,b | a²=b³>, with central h=a²=b³ and m=ab⁻¹=h(ba)⁻¹. Resolution multiplicities are 1,2,3,6 and exceptional squares are −3,−2,−1. Tail-node kernels are (−3,1) and (−2,1); the (m,h) lattice at the strict affine cusp injects. All strata are aspherical, and nontrivial exit circles are displayed with their compositions.

For the projective Weierstrass family, filling the puncture kills the longitude h m⁻⁶. The open group is Z² semidirect Z with monodromy [[0,−1],[1,1]]. The strict transform becomes A¹ and its node has kernel (−6,1). The source records corresponding changes to every link group and mapping space.

After the degree-six base change, the smooth elliptic model descended as [F×Δ/μ₆] is a good orbifold replacement. Boundary groups are C₂*C₃ in the affine case and Z² semidirect μ₆ in the proper case. The normal meridian is h; the ordinary exit category has two objects and crossing set G/<h>. This is not merely a root of the old resolved divisor. Nonzero integral or purely profinite kernels survive finite-index root lattices. Finite monodromy alone is not an obstruction.

### Higher-dimensional reductions

P3c-Mori concerns **algebraic** A¹ maps. Good toric opens have holomorphic entire curves. A nonconstant algebraic A¹ map extends to P¹. If infinity stays in the stratum, asphericity contradicts positive Kähler area; otherwise a normal displacement gives a nonzero full meridian vector bounding a disc. Svaldi's theorem then gives nefness of K+D for projective SNC pairs.

For a birational morphism between such good pairs, the effective exceptional log-Jacobian divisor is relatively nef and vanishes by negativity. The logarithmic differential map is an isomorphism. A full-rank pivot minor and roots of units produce monomial charts, proving log étaleness and toroidality by Kato's criterion.

For a rational comparison, negativity in both directions gives equality of the pulled-back log canonical divisors. The two effective discrepancy divisors on a common resolution coincide. Their common positive support need not vanish; no simultaneous contraction is asserted. The Atiyah-flop calculation is only a test under its stated local/projective hypotheses.

## Verified primary-reference locations

- Stacks Project, Tag 0C5Q, Lemma 54.17.1: regular-surface birational morphism factorization.
- Ueda (1979), Tohoku Math. J. 31(1), 81–90, DOI 10.2748/tmj/1178229879: Theorem 2 p. 81; case (d) p. 88; Proposition 3 pp. 89–90. Publisher metadata and full primary paper opened.
- Kiernan and Kobayashi (1973), Nagoya Math. J. 50, 199–216, DOI 10.1017/S0027763000015646: normal-crossing punctured-sphere extension p. 213. The needed general curve version is proved here.
- Bresciani (2021), Algebraic Geometry 8(2), 231–267, DOI 10.14231/AG-2021-005: Lemmas 10.9 and 10.11. The stronger arbitrary-base affine-fibre argument here is independent.
- SGA 1, Exposé XII, Théorème 5.1 and Corollaire 5.2, printed pp. 251–253 in the opened revised text, PDF pp. 266–268.
- Włodarczyk (2009), Simple constructive weak factorization, PSPUM 80(2), 957–1004, DOI 10.1090/pspum/080.2/2483958: Theorem 4.7.1 in the full author preprint (toric), Theorem 0.0.1 (general). Publication year is 2009, not the earlier working date 2006.
- Adiprasito and Pak (2026), Invent. Math. 245(3), 1117–1137, DOI 10.1007/s00222-026-01423-7. Publisher date 7 May 2026. Opened arXiv v2: Theorem 1.1, Corollary 1.2, Section 7.1 Question 7.1. Weighted subdivisions and ordinary smooth-centre subdivisions are distinct.
- Svaldi (2019), Selecta Math. 25(5), Article 67, DOI 10.1007/s00029-019-0512-9: Theorem 1.1. Primary preprint v3 and publisher metadata checked.
- Kato (1989), Logarithmic structures of Fontaine–Illusie, pp. 191–224: Theorem 3.5 p. 202, Proposition 3.12 p. 204. Primary PDF https://math.uchicago.edu/~drinfeld/p-adic_periods/Kato_log-structures.pdf . Search OCR interchanges X/Y in one exact sequence; the proof uses the correct pulled-back target differential map.
- Kollár and Mori (1998), Birational Geometry of Algebraic Varieties, Lemma 3.39. The sign convention was independently checked in Xu's author-version K-stability of Fano varieties, Lemma 1.73 p. 51. Xu's published book is 2025, DOI 10.1017/9781009538763; its pagination differs.

## Manuscript reading provenance

The original facsimile background/scans/MPL_149_091-136_scan130.jpg was inspected before the first workspace loss. The official source was subsequently recovered as build/sources/149.pdf. PDF pages 129, 130 and 131 were rendered and visually inspected, with an enlarged view of page 130’s dark right margin. Page 129 bears authored number 64 at the top, whereas page 131 bears authored number 65. Page 130 has no top number and is the continuation of authored folio 64. Its bottom-left archive numeral and institutional footer both read 129; that archive page is not the authored folio. The correct reference is therefore cote 149, folio 64 continuation, archive page 129, PDF/scan 130. The dark margin clearly contains “C'est visiblement faux”, an inserted “en général”, “pour card I(x) ≠1”, passage to another model X′ obtained by blowing up point(s) of D, and a question about a modèle “minimal” containing U. The abbreviated intervening words and the exact final question remain uncertain; they are not reconstructed from the mathematics. Every mathematical conclusion is independently formulated and proved. The original prompt attachment is named as the historical authoritative version, not claimed to remain locally available.

## Computational scope

The program checks exact integer/Fraction identities, not arbitrary asphericity, the surface classification, or factorization conjectures. Finite ranges of fan/root-index examples are labelled. Their role is to detect transcription and sign errors in formulas whose general proofs occur in the TeX source.
