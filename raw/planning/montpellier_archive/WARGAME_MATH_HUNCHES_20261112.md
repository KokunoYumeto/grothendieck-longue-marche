# Mathematical hunches from the war game

Claude Fable 5.2 (effort max), round 2, 12 Nov 2026. Written from what the war-game author held in context after
`PROGRAM_WARGAME_ROUND2_20261112.md`; nothing new was read, no file was opened, nothing was computed by machine.
Every entry is unchecked. **Believe** means I expect a proof along the route given; **guess** means I would bet on it
without a route. "The returns' claims" are statements of GPT-6 Astra (ChatGPT Pro mode) returns not yet reviewed.
Citations are from memory unless the war game marks them checked.

---

## H1. The centralizer theorem holds for every subgroup with no invariants in Tate modules (sharpens S6/R2). Believe.

**Statement.** Let K be a number field, U a hyperbolic curve over K, π its geometric fundamental group, s a section
of π₁(U) → Γ_K, and Δ a closed normal subgroup of Γ_K such that for every finite extension K′ and every abelian
variety A over K′ the Tate module T(A) = ∏_ℓ T_ℓ(A) has no non-zero invariant under Δ ∩ Γ_K′. Let C be the
centralizer of s(Δ) in π. Then C = 1, except when U is affine, s normalizes an inertia group I_x, and the cyclotomic
character is trivial on Δ; in that case C = I_x. Instances: Δ = Γ° (Ribet); Δ the group of K(μ_(ℓ^∞)) for one ℓ
(Imai, Serre). For Δ the group of K^ab the hypothesis fails exactly in the presence of complex multiplication
(Ruppert), and the statement should fail with it.

**Why.** The proof of R2 uses Γ° only through the vanishing of invariants: for z ≠ 1 in C and H = N⟨z⟩, the class
of z in H^ab is Δ-invariant, hence zero in the Tate module of the Jacobian of the covering; in the proper case this
contradicts z generating H/N; in the affine case it puts z in the weight −2 part for every H, hence in an inertia
group (Nakamura's criterion), and the relation [z] + [z′] = [zz′] in a covering with four cusps forces one inertia
group.

**Smallest test.** U = P¹ minus {0, 1, ∞} over Q, s the tangential section at 0, z = [x, y]. In the Fermat covering
of level ℓ^n the class of z generates H^ab over the group ring, and σ acts on it by Ihara's power series F_σ. The
prediction is that z is not centralized by s(Γ°), that is, F_σ ≠ 1 for some σ fixing all roots of unity. This is
known (the series F_σ carries Jacobi sums). The same test with y in place of z gives a class in the weight −2 part,
as it must.

**What would refute it.** A non-trivial non-inertia element whose class is of weight −2 in every open subgroup
containing it (the criterion quoted from Nakamura would then be misquoted); or a covering in which two distinct
inertia groups of C cannot be separated among four cusps.

**Bears on.** 149 scans 45, 49, 54–56, 59–63; LM 2:sc433, 2:sc483; FINDINGS F5, F17; LM3b D.5; R2 and R3 of round 2.

**Prompt (CYCLOTOMIC_KERNEL, extended).** Prove the statement for a general Δ as above, each step written out, with
the weight criterion for inertia quoted from its source with its hypotheses. List the Δ for which the hypothesis is
a theorem (Ribet, Imai, Serre, and the recent results on Kummer-type extensions of cyclotomic fields). For Δ the
group of K^ab and a curve with a CM Jacobian, decide whether C can be larger, by an explicit computation on a
two-step nilpotent quotient and then in π. Done: a proof or counterexample per item. Unacceptable: assuming any form
of the section conjecture.

---

## H2. A limit action always carries its vanishing cycle; a smooth proper curve never does (completes R4). Believe.

**Statement.** (a) Let C be a smooth proper curve of genus ≥ 2 over a number field k, π its geometric fundamental
group, Γ′ an open subgroup of Γ_k. There is no element γ ≠ 1 of π such that Γ′ preserves the conjugacy class of the
closed subgroup ⟨γ⟩ and acts on it through the cyclotomic character. For a smooth affine curve the classes with this
property are exactly those of subgroups of inertia groups. (b) For a stable degeneration over a henselian trait with
residue field k and any splitting of 1 → T → 𝓔_η → 𝓔_k → 1, the limit action of 𝓔_k preserves the conjugacy class of
the procyclic group of each vanishing cycle and acts on it through the cyclotomic character. Hence the limit action
is never that of a smooth proper curve over a finite extension of k, in all cases of bad reduction; and for affine
curves, good reduction holds if and only if the number of such classes of maximal procyclic subgroups equals the
number of cusps. This closes the case R4 left open (compact type with isogenous components).

**Why.** (a) is the argument of H1 with weights in place of Ribet: the normalizer of ⟨γ⟩ in π₁(C) maps onto an open
subgroup of Γ_k; in H = N⟨γ⟩ the class of γ spans a Galois-stable line of H^ab on which Galois acts by the cyclotomic
character, and Hom(Z_ℓ(1), T_ℓ(A)) = 0 over a number field by weights; so the class is zero, against γ generating
H/N. (b): inertia acts through a profinite multitwist; 𝓔_k normalizes it and acts on T by the cyclotomic character;
a profinite Dehn twist determines its curve up to conjugacy (results of combinatorial anabelian geometry, Hoshi and
Mochizuki, quoted from memory).

**Smallest test.** Genus 2 degenerating to two elliptic curves E₁, E₂ joined at a point, with E₁ = E₂ of complex
multiplication: here H₁ with its symplectic form cannot decide, and the separating vanishing cycle γ in [π, π]
does.

**What would refute it.** A smooth proper curve over a number field whose outer Galois action normalizes a
procyclic subgroup with cyclotomic action; or a limit action in which the class of ⟨γ⟩ is not preserved, which would
contradict the rigidity of profinite Dehn twists.

**Bears on.** 149 scans 99–103 (the "conjecture-à-tout-hasard", e ⟹ a); 147 §§9–10; cote 64 (unread); RESIDUE H.3
(the lifting category BZ at a node; the returns' claim); R4 of round 2.

**Prompt (a Part of LM6 revised, or GOOD_REDUCTION).** Prove (a) and (b) with every profinite step written out,
citing the exact statement on profinite Dehn twists that is used. Deduce the full table of 149's
"conjecture-à-tout-hasard" a) to f): a ⟺ b (Oda, Tamagawa, cited), c and d strictly weaker (example of compact
type), e ⟹ a in all cases. State what "pas trop loufoque" (his f) can be made to mean so that f ⟺ a. Done: proofs,
or the precise missing statement.

---

## H3. The two-level principle is rank selection in a Cohen–Macaulay curve complex; in genus 0 there is a k-level principle (sharpens S1). Believe in genus 0; guess beyond.

**Statement.** Let d = 3g − 3 + n, let V_k be a regular neighbourhood in the Deligne–Mumford compactification of the
union of the strata of dimension ≤ k, and V_k° its part in M(g, n). (i) The homotopy fibre of V_k° → M(g, n) is the
realization of the poset P_k of multicurves with at least d − k components. (ii) In genus 0, P_k is (k − 1)-connected
for every k, so V_k° → M(0, n) is k-connected: onto on π₁ for k = 1 (generators from the strata of dimension ≤ 1),
an isomorphism on π₁ for k = 2 (relations from dimension 2: the two-level principle), and for each k the k-type of
the tower with its structure at infinity is carried by the strata of dimension ≤ k + 1. (iii) In genus g ≥ 1, P_k is
(k − 1)-connected for k ≤ 2 (Hatcher–Thurston; Hatcher–Lochak–Schneps) and cannot be for all k when g ≥ 2, because the
curve complex has homotopy dimension 2g − 3 + n < d − 1 (Harer); guess: P_k is (min(k, 2g − 2 + n) − 1)-connected.

**Why.** (i): lift to Teichmüller space; the regions where the curves of a multicurve are short are contractible
and meet exactly along unions of multicurves; the nerve lemma gives P_k, and Teichmüller space is contractible.
(ii): by Harer the curve complex of a sphere with n holes is a wedge of spheres of its top dimension n − 4, and the
link of a simplex is a join of curve complexes of genus 0, of the right dimension (the count is Σ(n_i − 3) =
n − 3 − c); so the complex is homotopy Cohen–Macaulay, and a rank-selected subposet of a Cohen–Macaulay poset is
Cohen–Macaulay of dimension the number of ranks minus one. P_k selects k + 1 ranks.

**Smallest test.** (0, 5): P_1 is the curve complex, a connected graph that is not simply connected; V_1° → M(0, 5)
is onto on π₁ with kernel generated by the pentagon. (0, 6): P_2 must be simply connected and P_3 contractible.

**What would refute it.** A simplex of a genus-0 curve complex whose link is not spherical of the right dimension;
or a mistake of variance in (i), visible already at (0, 5).

**Bears on.** 147 scan 60 ("J'ai l'impression"), scan 104 (the "Programme"), §§7–10; 146 scan 100; Esquisse §2;
LM3 F.5–F.16; STRATA F.4–F.7, F.17 and RESIDUE H.4 (4, 26, 236 strata; the returns' claims); S1.

**Prompt (a Part of EXIT_TOWER).** Prove (i) and (ii) in the language of entrance categories: for the full
subcategory of exit arrows from strata of dimension ≤ k to the open stratum, the map of classifying spaces to
BΓ(0, n) is k-connected. Write the resulting presentation of Γ(0, n) as a graph of groups with relations, and say
which strata of dimension 3 give the first syzygies. For g ≥ 1 determine the connectivity of P_k, proving or
refuting the guess, with (1, 2), (1, 3), (2, 0), (2, 1) computed. Then the profinite version: which of these
connectivity statements survive completion.

---

## H4. His "déploiement" is the real oriented blow-up; S2 is asphericity and π₁-injectivity of its faces; the property is toroidal (sharpens S2, S3). Believe; the last clause is a guess.

**Statement.** For a normal-crossings pair (X, D) let X^log be the real oriented blow-up of X along D (the
Kato–Nakayama space), a manifold with corners with interior U whose faces are torus bundles T^J over the strata
D_J°. (i) The exit-path ∞-category of (X, D) is the category of faces of X^log with paths, and the flag categories
of the gluing theorem in Cat are its faces. (ii) It is an ordinary category if and only if every face is aspherical
and injects on π₁ into every face containing it in its closure. (iii) This property is unchanged by blowing up the
closure of a stratum of codimension ≥ 2 and is destroyed by blowing up a point of a stratum of codimension 1: the
exceptional divisor then carries a copy of (S², point). (iv) Guess: any two compactifications of U with the
property are joined by blow-ups and blow-downs along strata.

**Why.** (ii) is the long exact sequence of the homotopy fibre of a link, as in STRATA F.2. (iii): after a blow-up
along a crossing stratum the new meridian is the sum of the old ones and the lattice of meridians at each new
crossing is a unimodular change of the old; after blowing up a point of D_1°, the stratum E° is an affine line and
the link of its point at infinity is a circle that dies in it.

**Smallest test.** (P¹, ∞): X^log is a closed disc whose boundary circle is not π₁-injective: his "Remords" of 147
scan 180. M̄(0, 4): a pair of pants, injective: an ordinary category. The margin of 149 scan 130 is case (iii).

**What would refute it.** A pair in which all faces are aspherical and injective and some exit mapping space is not
discrete; for (iv), two good compactifications of a surface not related by toroidal moves.

**Bears on.** 147 scans 164–169, 179–181; 149 scans 128–136 (and the margin of scan 130: "y a-t-il un modèle
minimal ?"); 150, 151 (unread: the prediction is that "déploiement" there is this construction for stratified
spaces); STRATA C.1–C.5, F.1–F.3; S2, S3, S25.

**Prompt (EXIT_ONE_TYPE, Parts 1–3).** Prove (i)–(iii). For (iv) treat surfaces completely (minimal
normal-crossings completions) and Artin's elementary neighbourhoods; give a counterexample if it fails. Compute the
exit category for a fibre with finite monodromy after resolution, where injectivity may fail for unavoidable
reasons, and say what replaces the criterion there (an orbifold structure on the boundary).

---

## H5. On PSL₂(F_q), GT₀ and the Galois group can differ only by a character with values in the outer automorphism group (sharpens S10). Believe (i), (ii); guess (iii).

**Statement.** Let G = PSL₂(F_q), q odd, and N(G) the set of generating pairs (x, y) modulo inner automorphisms.
(i) By Macbeath's theorem a generating triple (x, y, z), xyz = 1, is determined up to Aut(G) by its trace triple.
An element (λ, f) of GT₀ sends (x, y, z) to a triple whose entries are conjugate to x^λ, y^λ, z^λ, so its action on
N(G)/Out(G) is the trace-power map, the same as for an element of Γ_Q with cyclotomic character λ. Any difference
between GT₀ and Γ_Q on G therefore lives in the fibres, which are torsors under quotients of Out(G), a group of
order 2e for q = p^e. (ii) If one entry has order p, the fibre action is forced as well: the unipotent class splits
in G, and x^λ lies in the class of x exactly when λ is a square modulo p. (iii) For triples of orders prime to p
the fibre action of GT₀ is a character GT₀ → Out(G); the guess is that it is always λ ↦ the Legendre symbol of λ
modulo p (for q = p), so that no separation occurs on any PSL₂(F_p). The first groups where a separation is not
excluded by (i)–(ii) are those with larger Out: q = 9 (the group A₆, Out of order 4) and q = 8, 27.

**Why.** (i) and (ii) are formal from the shape of GT₀. (iii) agrees with the congruence case (LM2 C.d1: action on
SL₂(Z/n) through units modulo squares) and with the expectation that the fibre character is read on the field of
definition of the covering with its group action.

**Smallest test.** G = PSL₂(F₇), types (3, 3, 4), (3, 4, 4), (4, 4, 4): compute the two-element fibres and the
action of the level of GT₀ that LM2 B.f5 left undetermined (a shadow of order 1,024). Expected answer: swap exactly
when λ is a non-residue modulo 7, or trivial action; in either case arithmetic.

**What would refute it.** An element of a GT₀-shadow acting on a fibre by a character that does not factor through
λ. That would separate GT₀ from Γ_Q at a finite level and is worth the computation for that reason alone.

**Bears on.** Cotes 79, 83, 72 (unread); 142 scans 108–114; LM §§36–37, 53; LM2 B.f5, B.g15, C.d1, C.r1–C.r3;
Esquisse §4; S10.

**Prompt (POLYHEDRA_SHADOWS, Part A).** Prove (i) and (ii) with the exceptional and singular trace triples treated.
Compute the fibre character for PSL₂(F_q), q = 7, 9, 11, 13, on all types of orders prime to p, at the first levels
of GT₀ and GT that act faithfully on the kernels involved; tabulate against the arithmetic action computed from
fields of moduli. For q = 9 include the exotic outer automorphism of A₆. Done: a table with every entry either
"factors through λ, by this formula" or an explicit separating element.

---

## H6. The localizer of finite-dimensional local systems is a fundamental localizer whose localization is schematization (sharpens S11). Believe (a), (b); guess (c).

**Statement.** For a field k of characteristic 0 let W_fd(k) be the functors (or maps of spaces) f such that f*
is an equivalence on local systems of finite-dimensional k-vector spaces and an isomorphism on cohomology with
coefficients in them; equivalently, f* is an equivalence on locally constant diagrams of perfect complexes.
(a) W_fd(k) is a fundamental localizer in the convention with relative Theorem A, strictly between W_D(k)^lc
(bijection on components, isomorphism on π₁, k-homology of universal covers) and the k-homology equivalences.
(b) It is closed under filtered colimits, fails the axiom (7 F) and is not proper. (c) It is accessible in ZFC, and
its localization restricted to connected spaces of finite type is Toën's schematization over k (the equivalences of
Katzarkov–Pantev–Toën).

**Why.** (a): it is W^lc for the coefficient system of perfect complexes, and the proof that W^lc_D is a localizer
uses only finite homotopy Kan extensions along the comma categories that occur [to be checked: this is the point].
Strictness: for Higman's group G (acyclic, no finite quotients, no finite-dimensional representations) BG → point
lies in W_fd(k) and not in W_D(k)^lc; B(Z/2) → point is a rational homology equivalence outside W_fd(k). (b): the
witnesses of RESIDUE D.11 for the rational localizers should serve. (c): cohomology with a finite-dimensional
coefficient system is dual to homology with the dual system, so a cardinality argument of Bousfield's type should
apply; for general cohomological conditions accessibility is not provable in ZFC, which is why this is only a guess.

**Smallest test.** BG → point for Higman's group; the circle (not in W_fd: characters); a K(π, 1) with π a lattice
in SL₃(R) against its pro-algebraic completion.

**What would refute it.** A failure of relative Theorem A for perfect coefficients (a functor over a base all of
whose comma maps are in W_fd(k) without being in it): this would need infinitely many comma categories whose
finite-dimensional data do not assemble.

**Bears on.** Cotes 137, 136, 133, 153, 112, 113 (unread); *Pursuing Stacks* VI–VII; *Les Dérivateurs* XVI;
GALOIS Part C, RESIDUE D.5, D.6, D.11, I.9 (the returns' claims); the expert's hunch H9 on accessibility; S11.

**Prompt (SCHEMATIZATION_LOCALIZER).** Prove or refute (a), (b), (c) item by item, starting from the proofs of
GALOIS for W^lc_D and recording exactly which Kan extensions they use. Compute W_fd(k) on finite categories and on
classifying spaces of finitely presented groups in terms of pro-algebraic completions. Compare with W_fd(F_p) and
with the second stage of RESIDUE I.9. State which of Grothendieck's axioms Loc hold, in the table format of
RESIDUE D.11.

---

## H7. The compatibility he left open in cote 47 follows from linearity over the Ext-algebra of the unit section (Book II, 47). Believe.

**Statement.** Let B be an abelian scheme of relative dimension n over S, B* its dual, W the Poincaré sheaf,
p: B* ×_S B → B*, e the unit section of B*, T its normal bundle and τ = Λⁿ T. Let c: R p*(W) → e*(τ)[−n] be the map
he constructs (the identity in degree n after base change). Then L e*(c) is linear over the algebra
Ext*(e* O, e* O) = Λ* T; on the source H*(B, O_B) this algebra acts by cup product through the Kodaira–Spencer map
T → H¹(B, O_B) of the Poincaré family, which is the canonical isomorphism; on the target Λ^(n−i) T^∨ ⊗ τ = Λ^i T it
acts by exterior multiplication. Since c is an isomorphism in degree n and the pairing Λ^i ⊗ Λ^(n−i) → Λⁿ is perfect
on the source, L e*(c) is injective in every degree, hence an isomorphism by ranks. With his Lemma 2 away from the
unit section this proves Lemma 1 and the inversion theorem over any base, with the twist τ.

**Why.** Naturality of the Yoneda action makes L e* of any morphism linear over the Ext-algebra; nothing has to be
computed except that the action on the source is non-degenerate, which is the definition of the dual abelian
scheme as a Picard scheme.

**Smallest test.** n = 1: the map H⁰(E, O) → Tor₁ ⊗ τ is an isomorphism because cup product with the class of the
universal first-order deformation, H⁰(E, O) → H¹(E, O) ⊗ T^∨, is 1 ↦ identity.

**What would refute it.** The Yoneda action on H*(B, O_B) being zero or degenerate, that is, the Poincaré sheaf
being trivial to first order along the unit section.

**Bears on.** 47 scans 5–8 ("à faire une vérification de compatibilité....."); the notes' F7, F8 (which reduce to
derived fibres and stop at this point); Mumford §13; Mukai 1981; Laumon 1996.

**Prompt (FOURIER_1970, item i).** Write the proof in full for an abelian scheme over an arbitrary base, with the
derived base change and the perfectness used made explicit; determine the sign with which c agrees with the
standard identification; then the same argument for the margin of scan 3 (flat commutative group schemes, pairings
of torsors), saying where it stops.

---

## H8. Integral hard Lefschetz on an exterior algebra is Wilson's diagonal form (Book II, 16). Believe.

**Statement.** Let M = Z^(2n) with its standard symplectic form ξ, and γ_m(L) the multiplication by the divided
power ξ^m/m!. Under the torus the map γ_m(L): Λ^j M → Λ^(j+2m) M splits into blocks, one for each choice of n − v
"inert" coordinates, and each block is the inclusion matrix of t-subsets in (t + m)-subsets of a v-set. By Wilson's
theorem (1990) this matrix has a diagonal form with entries the binomials C(t + m − i, t − i), 0 ≤ i ≤ t, with
multiplicity C(v, i) − C(v, i − 1). Consequences. (i) The Lefschetz map γ_(n−i)(L): Λ^i → Λ^(2n−i) is an isomorphism
over Z only for i = 0, 1, n; for i = 2 its cokernel is Z/(n − 1). (ii) Without divided powers, condition (6.1)_i of
cote 16 holds over a ring A for all i if and only if n! is invertible in A. (iii) For a principally polarized
abelian variety of dimension g, cup product with the minimal class θ^(g−2)/(g−2)! from H²(A, Z) to H^(2g−2)(A, Z)
has cokernel Z/(g − 1). (iv) The order generated in ∏ Mat_(n−i+1)(Q) by L, Λ and the degree projectors, with or
without divided powers, has index a product of the same binomials.

**Why.** ξ^m/m! is the sum of the products p_R over m-subsets R, p_a = e_a ∧ f_a, so on the span of the p_S it is
the inclusion matrix. On primitive vectors Λ^r L^r = (r!)², which gives (ii).

**Smallest test.** n = 3, i = 2: the block on {p_1, p_2, p_3} is the matrix J − I of determinant 2 (computed by
hand in the war game: ±2). n = 4, i = 2: J − I of size 4, determinant −3: cokernel Z/3. n = 2: every Lefschetz map
with divided powers is an isomorphism.

**What would refute it.** A Smith normal form for some n ≤ 5 that disagrees with the binomials; a mistake in the
reduction to inert coordinates.

**Bears on.** 16 scans 14–15 ("sur Z !", the ring Φ₀ and its basis); the notes' R1, R2, S2–S4; 47 scan 9 (the
divisibility of δ′^k); integral Fourier transforms (Moonen–Polishchuk; Beckmann–de Gaay Fortman); cotes 136–137
only as a theme (divided powers).

**Prompt (LEFSCHETZ_RINGS, the integral Part).** Prove the block decomposition and (i)–(iv); verify by Smith normal
forms for n ≤ 6 with a program. Decide which of the classes θ^k/k! and of the cokernel classes in (iii) are
algebraic for Jacobians and for very general abelian varieties, by comparison with the literature on the integral
Hodge conjecture; state Grothendieck's no 7 in its correct integral form.

---

## H9. Th. 5 of cote 44 is the Mordell–Weil lattice formula in codimension m, and it makes Th. 4 equivalent to a Hodge index statement (Book II, 44). Believe (a); (b) as stated is a reduction, believed.

**Statement.** Let X be smooth projective of dimension n = 2m over k, X̃ → P¹ a Lefschetz pencil with generic fibre
Y over K = k(t), and Z, Z′ cycles of codimension m on X whose restrictions ζ, ζ′ to Y are homologically trivial.
(a) The height pairing of Beilinson and Bloch over the function field K is ⟨ζ, ζ′⟩ = (−1)^m Z·Z′, up to the
normalization of the pairing; for m = 1 this is Shioda's formula ⟨P, Q⟩ = −(φ(P)·φ(Q)) for Mordell–Weil lattices.
(b) Hence the following are equivalent for X: the intersection form is (−1)^m-definite on the algebraic classes of
H^(2m)(X) that vanish on a smooth hyperplane section (the part of the Hodge standard conjecture in the middle
degree that hyperplane sections do not reach); and the height pairing is positive definite on the image of those
cycles in J^m(Y)(K) modulo the K/k-trace. The second follows from his Th. 4 over K (the auto-duality of the abelian
variety J^m(Y) is a polarization), by positivity of Néron–Tate heights for a polarized abelian variety over a
function field. So in characteristic p, Th. 4 for odd-dimensional varieties over function fields implies the Hodge
standard conjecture in the middle degree, by induction on hyperplane sections; this is the reduction he describes
to Serre in 1964, and the auto-duality of Achter, Casalaina-Martin and Vial is the object whose positivity is asked.

**Why.** Over a function field the height pairing is defined as an intersection number of extensions of the cycles
to a model that are orthogonal to vertical cycles; in a Lefschetz pencil of fibre dimension ≥ 2 the fibres are
irreducible, so the cycles Z, Z′ are already such extensions up to multiples of fibres. The sign is that of the
Hodge index theorem on primitive classes of type (m, m).

**Smallest test.** m = 1: an elliptic or higher-genus fibred surface, where (a) is Shioda's theorem and (b) is the
classical equivalence of the Hodge index theorem for surfaces with the positivity of the Néron–Tate height on the
Jacobian of the generic fibre. First new case: m = 2, X a cubic fourfold or an abelian fourfold in characteristic
p, where the Hodge standard conjecture is known (Ancona) and Th. 4 for the threefold Y over K can be tested.

**What would refute it.** A threefold over a function field of characteristic p whose canonical auto-duality is not
positive: it would refute the Hodge standard conjecture for a fourfold. Or a vertical correction term in (a) that
does not vanish for a Lefschetz pencil (reducible fibres in fibre dimension 1 are the known case; they are
excluded by his hypothesis "fibres géométriquement intègres").

**Bears on.** 44 scans 2, 4 (Th. 3–6 and the margins "Néron", "variante locale"), scans 8–9 (the letter to Serre:
"le théorème de positivité de Hodge se ramène à l'énoncé suivant"); 16 scans 44–49 (the index conjecture, I(X × X));
cote 25 (IV 20, hyperplane sections; unread); cote 56 (unread); 032 (claimed).

**Prompt (JACOBIANS_1964, Parts on Th. 4–6).** Prove (a) with a fixed normalization, including the local variant he
announces (contributions of singular fibres when they are reducible). Prove the equivalence (b) and the induction on
hyperplane sections, stating exactly which part of the Hodge standard conjecture is obtained from which instance of
Th. 4. Test on abelian fourfolds in characteristic p against Ancona's theorem, and state what is known about the
positivity of the auto-duality of algebraic representatives in codimension 2.
