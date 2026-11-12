# La Longue Marche à travers la théorie de Galois: reading notes

Notes of the LM field expert (Claude Fable 5.2, effort max, 12 Nov 2026), taken while reading the transcription in
order (current text per package; reading copies in `work\reading2\`). Locations are given as cote and scan
(`2:sc26` = cote 140-2, scan 26) and his page number (`p.11`). Marks: **D** definition, **P** statement he asserts
(with or without proof), **C** conjecture, **Q** question or doubt he leaves, **N** a remark of mine (never his).
Notation is his unless marked. Quote from the source .tex of the package, never from these notes.

Overall plan of the manuscript (from his tables of contents, 2:sc3–4, 3:sc3–5, 4:sc3–4):

- Part I (cote 140-2, pp. 1–292), §§1–37: multi-Galois topoi (§§1–4); the arithmetic setting and the fundamental
  anabelian conjecture (§5); local analysis at a point of S (§6); the "bordelic" reformulation (§7); taxonomy of cases
  (§8); tangential structure, sections "of the second type" (§9); adjusting hypotheses (§10); conditions on systems
  coming from geometry (§11); the topological analogy, exterior groups with loops (§12); return to arithmetic, Galois
  formulations (§13); loop groups again (§13bis); cohomological digression on plugging holes (§14); critical orbits
  and finite subgroups of Autext_lac(π), discrete case (§§15, 17, 18); plugging and drilling holes (§16); the
  Teichmüller tower (§19); 2-isotopic description of the category of 2-spheres (§20); Teichmüller spaces (§21); §22
  missing; surfaces with finite groups of operators, "putting the problem into equations" (§23); the A^{oΓ} and the
  relations Π^Γ_{g,(ν,ν+n-1)} = (1) (§24); "special" Teichmüller groups (§25); case of two groups (§25bis); profinite
  Teichmüller groups, discretifications, the modular Teichmüller topos, a "hasty conjecture" (§26, numbered 25 again);
  change of type (g,ν): plugging holes (§27), passage to a finite covering ("the hasty conjecture creaks", §28);
  critique, adjusted notions and conjectures (§29); properties of N_{g,ν}, Γ_{g,ν} (§30); lifting an exterior action
  of a finite group on a profinite loop group (§31); arithmetic of hole plugging, Γ_{g,ν} versus Γ_{g,ν-1}, the étale
  topos of a complete curve from the π_1 of an anabelian open (§32); anti-involutions of compact oriented surfaces
  (§33, p.221); relations between N_{g,ν}, Γ_{g,ν} for variable g (a second §33, p.239); heuristic profinite
  description of the category of algebraic curves over finite subextensions of Q̄_0/Q (§34); injectivity of
  Γ_Q → Autext_lac(Π̂_{0,3}) (§35); Γ_Q ≃ Γ_{1,1} and injectivity into Autext(SL(2,Z)^) (§36); moduli of elliptic
  curves via Legendre (§37).
- Part II (cote 140-3, pp. 291–650), "Variations sur l'équation des lacets", §§38–49.
- Cote 140-4 (pp. 650bis–787): §50 schematic envelopes of discrete groups, metabelian case; §51 the Fermat tower;
  §52 Lie approximations of Galois–Teichmüller systems; §53 the special Teichmüller group ST_{1,1} ≃ GL(2,Z)~.
- Cote 140-1: a draft (37 scans).

---

## Part I (cote 140-2)

### §1 Topos multigaloisiens (2:sc6–11, pp. 1–3)

- **P 1.1** For a category E equivalent: (a) E is a topos all of whose objects are locally constant; (b) E ≃ Ĉ for a
  groupoid C; (b') E ≃ ∏ Ens(G_i) for a family of groups; (c) exactness conditions of SGA 1 type. b ⇔ b' ⇒ a
  "immediate". **Q** for a ⇒ b he is "less sure": perhaps E must be locally connected with enough fibre functors.
- **D 1.2** multigaloisian topos / category. **P 1.3** (margin) stable under induced topos E/S and under sums.
- **P 1.4** C := category of points of E (opposite of fibre functors); E → Ĉ. For E multigaloisian: C is a groupoid,
  the fundamental groupoid Π_1(E), and E → Ĉ is an equivalence. 0-connected and 1-connected ("simply connected")
  objects defined (2:sc7–8).
- **P 1.5** S 1-connected ⇔ 0-connected and projective ⇔ Hom(S,−) is a fibre functor ⇔ E/S ≃ point topos ⇔ (for
  E = Ĉ) S is representable. **D 1.6** universal covering. **P 1.7** the 1-connected objects E_0 ≃ Π_1(E): every fibre
  functor is representable by an essentially unique 1-connected object. **Cor 1.8**, **D 1.9** pointed universal
  covering over a point P. **Scholie 1.10**: a point of a multigaloisian topos = a universal covering.
- **P 1.11** Hom_top(E,E') ≃ Hom(Π_1 E, Π_1 E') is an equivalence (quasi-inverse through Ĉ → Ĉ'). 1.12 (only a title):
  the 0-connected pointed case Ens(G), Ens(G').

### §2 Application aux revêtements des topos (2:sc12–15, pp. 4–5)

- **P (Thm) 2.1** E locally connected and locally simply connected (margin **Q**: perhaps "enough points" needed):
  the locally constant objects E_lc form a multigaloisian topos and E_lc → E commutes with finite projective limits
  and arbitrary inductive limits. **D 2.2** E_[1] := E_lc, the multigaloisian envelope; canonical morphism E → E_[1].
  NB: the topos analogue of killing π_i, i ≥ 2; expected tower E → ... → E_[i] → E_[i-1] → ... → E_[1] → E_[0]
  under local contractibility hypotheses (**Q**, not constructed).
- 2.3 The fundamental groupoid of E: objects the points of E, morphisms those of the induced points of E_[1];
  Pt(E) –α→ Π_1(E) –β,≈→ Pt(E_[1]); α need not be faithful or full (a 1-connected E can have Hom sets in Pt(E) of
  cardinal > 1); a universal covering of E need not come from a point of E.

### §3 (title only, 2:sc16): pro-multigaloisian and profinite variants. §4 Complément-remords (2:sc16–18, pp. 6–7)

- **P** For multigaloisian E, E': a morphism E' → E is an induction morphism (E' ≃ E/S) iff C' → C is faithful.
  Hence E ≃ the category of groupoids C' over C with faithful structural functor, morphisms = isomorphism classes of
  pairs (f, α: p_2 f ≃ p_1) (margin **Q**: make precise the isomorphisms between pairs). Example: étale k-schemes =
  profinite groupoids faithful over (pt, Gal(k_s/k)). He wants to insert this in a "Galois description" of smooth
  quasi-projective schemes of dim ≤ 1 over k of finite type over Q.

### §5 Arithmetic setting; the fundamental anabelian conjecture (2:sc19–25, pp. 7'–10)

- K of finite type over Q, K̄, Γ = Gal(K̄/K). 5.1: pairs (X,S), X projective smooth of dim ≤ 1 over K, S finite
  reduced (étale over K) in the 1-dimensional components; morphisms f: X' → X with S' = f^{-1}(S)_red.
- **P (Lemme) 5.2** Ω algebraically closed, X connected projective smooth curve of genus g, S ⊂ X(Ω) of n points,
  U = X∖S. Equivalent: (a) π_1(U) non-abelian; (b) Aut(U) finite; (c) finitely many non-constant morphisms from any
  connected reduced finite-type scheme into U; (d) g ≥ 2, or g = 1 and n ≥ 1, or g = 0 and n ≥ 3; (e) (margin, Ω ⊂ C)
  universal covering = Poincaré half-plane; (f) (margin, marked "?!", Ω = Q̄, S ≠ ∅) the universal covering of U is
  isomorphic to that of P^1∖{0,1,∞} (**Q**; N: this is a Belyi-type statement on the profinite/algebraic universal
  cover). **D 5.3** (X,S) anabelian ("anabélique").
- 5.4: X ↦ profinite fundamental groupoid Π_1(X) over Π_1(K) ≃ [Tors(Γ)]; in the pointed connected case a profinite
  group π with π → Γ (open image).
- **C 5.5** The functor X ↦ (Π_1(X) over Π_1(K)), restricted to projective smooth anabelian X of dim ≤ 1 (S = the
  0-dimensional components), is fully faithful. Margin: "C'est un peu faux, cf §9". **C 5.5bis** the pointed form:
  (X, ξ) ↦ (π_1(X,ξ) → Γ) fully faithful. For dim 0 this is Galois theory; in dim 1 it concerns genus ≥ 2 only; false
  for P^1 or elliptic curves (take X' = Spec K), which is why S and the anabelian hypothesis are introduced.

### §6 Local analysis at s ∈ S (2:sc25–28, pp. 10'–12)

- O_s henselization, K_s its fraction field, D_s = Spec O_s ("arithmetic disc"), D_s^* = Spec K_s ("punctured disc").
  (6.1) Π_1(D_s^*) → Π_1(D_s) ≃ Π_1(s) → Π_1(K), first arrow surjective on Hom, second faithful. (6.2)
  Gal(K̄_s/K_s) ↠ Gal(k̄(s)/k(s)) ↪ Γ with kernel canonically T(k̄_s) ≃ T(K̄) (Kummer). Relative π_1 of Π_1(D_s^*) over
  Π_1(D_s) is the Tate local system: π_1(Π_1(D_s^*)/Π_1(D_s)) ≃ q_s^*(T_K). D_S, D_S^* ("multidisc", "multi-annulus");
  ρ_S: Π_1(D_S^*) → Π_1(X∖S).

### §7 The "bordelic" reformulation (2:sc28–54, pp. 12–25)

- **D** A bordelic system: profinite groupoids Π_U, Π_D, Π_{D*} over Π_e = Π_1(Spec K); functors ρ: Π_{D*} → Π_U,
  σ: Π_{D*} → Π_D, φ: Π_U → Π_e, ψ: Π_D → Π_e; α: φρ ≃ ψσ; conditions: σ iso on π_0, epi on Hom, abelian kernel; ψ
  faithful; [ρ faithful; φ epi mod finite groups on Aut]; Kummer isomorphism k: π_1(σ) ≃ ψ^*(T). Morphisms: triples
  of functors with four commutation isomorphisms (a prism), compatible with α, α' and with k, k' — margin correction
  (2:sc33): compatible with Kummer only up to multiplication by the ramification degrees, except for étale morphisms.
  Hom := π_0 of the groupoid of such data; **Q** (2:sc34) he believes Aut(f,α) is always trivial, "j'ai la flemme de
  vérifier". The category B ("catégorie bordélique").
- **C 7.1 (conjecture bordélique)** (2:sc35) The functor (X,S) ↦ B, restricted to X projective smooth of dim ≤ 1 with
  (X,S) anabelian, is fully faithful. Margin: "La fidélité est facile!".
- Group-theoretic description (2:sc35–54): choosing base objects, a reduced system is: I finite; exact sequences
  1 → T(K̄) –k_i→ E_i –p_i→ Γ with open image Γ_i, k_i equivariant; 1 → π → E –p→ Γ (image Γ_0 open); injective
  ρ_i: E_i → E with p∘ρ_i = int(γ_i)∘p_i (one may take γ_i = 1). Simplest form (2:sc43, "catégorie bordélique
  précisée", Π_U connected): E –p→ Γ, a finite family of subgroups E_i ⊂ E with isomorphisms
  k_i: T(K̄) ≃ E_i ∩ π. A morphism (E',...) → (E,...): f: E' → E, β_{i'} ∈ E, α ∈ Γ with (1) p f = int(α) p';
  (2) for each i' a unique i = τ(i') with int(β_{i'}^{-1}) f(E'_{i'}) ⊂ E_i and a unique d_{i'} ∈ N^* with
  int(β_{i'}^{-1}) f k'_{i'} = k_i ∘ (d_{i'}·id). Refined (2:sc50): f^0_{i'} = d_{i'} χ(β_{i'}) id on T(K̄), χ the
  cyclotomic character, β_{i'} = p(α_{i'}) α.
- Simplification (2:sc44–45): give only Π_{D*} –ρ→ Π_U –φ→ Π_e and define Π_D by canonical factorization; 1-morphisms
  = quintuples (f_{D*}, f_U, α_{D*U}, α_{Ue}, K) with one condition: the induced map on π_1(φρ) is multiplication by a
  ramification index π_0(Π'_{D*}) → N^*.
- 0-morphisms (2-cells) between 1-morphisms f, f' (2:sc50–53): μ ∈ E with f'_E = int(μ) f_E, α' = p(μ) α, and
  μ_{i'} ∈ E_i determined uniquely; indeterminacy of μ = Centr_π(f_E(E')). **P** if π' → π has open image (a
  "non-constant morphism") then μ_0 centralizes an open subgroup of π, hence ("sauf erreur") μ_0 = 1 and the Hom
  category is discrete. **P** (margin 2:sc54) the centralizer in Γ of an open subgroup is trivial.
- Reformulated (2:sc53–54): D = (E, subgroups E_i, p: E → Γ, k_i: T(K̄) ≃ E_i ∩ π =: L_i); a morphism is f: E' → E
  with p f conjugate to p' and each f(E'_{i'}) in a conjugate of some E_i, plus the degree condition
  χ_{i'} = d_{i'} χ(β_{i'}).

### §8 Réflexion taxonomique (2:sc55–72, pp. 25'–34)

- dim X = 0 ⇔ p injective (then I = ∅): an open subgroup E ⊂ Γ, i.e. a finite subextension L. Four cases by
  n = dim D, n' = dim D' for Hom(D', D):
  - I (0,0) and II (n'=1, n=0): Hom(D',D) ≃ E∖Transp_Γ(Γ'_0, E) ≃ Hom_K(L, L'): full faithfulness holds, with no
    hypothesis on X' beyond 0-connectedness (X finite étale over K; via sections of X_{X'}/X').
  - **III (n'=0, n=1)**: reduce to X' = Spec K, E' = Γ. Morphisms D' → D = classes of splittings of E → Γ modulo
    conjugation by π = Ker p. **C (2:sc63–64)**: for anabelian (X,S), Γ((X,S)/K) = (X∖S)(K) → {π-conjugacy classes
    of sections of E → Γ} is bijective. Margin: "faux tel quel, cf n° 9 ci-dessous — il faut des conditions
    supplémentaires sur les f ... Peut-être vrai si I = ∅". **P** injectivity: holds whenever U embeds in a group
    scheme G that is an extension of an abelian variety by a torus, by the "absolute" Mordell–Weil theorem (G(K) of
    finite type); the splitting class of the extension E^♮ of Γ by π_ab ≃ H_1 already determines the point; needs only
    "g = 0 ⇒ n ≥ 2". **N.B. (2:sc65)**: suggests an approach to Mordell (finitely many π-conjugacy classes of
    splittings for g ≥ 2) and to Fermat via an extension of Γ by π_1(P^1∖{0,1,∞}).
  - IV (1,1): (a) I = I' = ∅: constants allowed, described by f trivial on π'; (b) I' = ∅, I ≠ ∅: only constants;
    the conjecture says every homomorphism of extensions E' → E (E' for a complete curve, E for X∖S, S ≠ ∅) is trivial
    on π' — **Q** "il faudrait essayer de vérifier ce point directement"; (c) I' ≠ ∅, I = ∅: Hom empty; (d) both ≠ ∅:
    f dominant finite; faithfulness follows from case III; "la pleine fidélité par contre est chose mystérieuse".
- Elementary reductions (2:sc68): reduce to E → Γ epi by finite extension; **P ("sauf erreur")** case III for
  finite-type extensions of K implies the general case for K.
- **Q (2:sc69)** whether Transp_E(L_i^d, L_i) = E_i for all d ∈ N^* (then E_i is known from L_i ⊂ π).
- When the E_i → Γ are surjective (points of S rational, 2:sc70–72): a morphism is (f, τ, (α_{i'} ∈ π)) with f a
  homomorphism over Γ, f(E'_{i'}) ⊂ int(α_{i'}^{-1}) E_{τ(i')} and the induced map on T(K̄) equal to multiplication by
  d_{i'}; the π-conjugacy class of f determines the morphism (presumably in general, "un peu de sueur").
  **Conclusion**: the essential structure describing (X,S) is an "exterior extension" of Γ by π, with π carrying a
  *loop structure* ("structure à lacets"): exterior homomorphisms κ_i: T (= T(K̄) ≃ Ẑ non-canonically) → π; morphisms
  = π-conjugacy classes of homomorphisms E' → E over Γ whose π' → π respects the loop structure.

### §9 Tangential structure at s ∈ S; sections "of the second type" (2:sc72–79, pp. 34–37)

- Sections of Π_{D_i^*} → Π_{D_i}: L_i-conjugacy classes of sections of the extension E_i of Γ_i = Gal(K̄_i/K_i) by
  L_i ≃ T(K̄_i); they form a torsor Σ_i under H^1(K_i, T(G_m)) ≃ lim (K_i^*)_n =: H_i; K_i^* ↪ H_i (injective since
  K_i is of finite type over Q).
- **Construction (2:sc75–77)** k a field of char 0, O a henselian valuation k-algebra with residue field k, L its
  fraction field. For a uniformizer t: O(n,t) = O[T_n]/(T_n^n − t), O(∞,t) = lim; L(∞,t) ⊗ k̄ is algebraically
  closed, giving a section of Π_L over Π_k. t and t' = t u^n (u ∈ O^*) give isomorphic sections; so t and t u with
  u ∈ 1 + m (divisible) give the same class. **P** a canonical map (m/m^2)^* (bases of m/m^2, a k^*-torsor) → classes
  of sections of Gal(L̄/L) → Gal(k̄/k) (a torsor under H^1(k, T(G_m))), compatible with Θ: k^* → H^1(k, T(G_m)); when Θ
  is injective, an embedding of the torsor of non-zero tangent vectors as a Θ(k^*)-subtorsor.
- So each E_i carries a privileged K_i^*-subtorsor of splittings ("algébriques", "géométriques"). **Q** behaviour
  under morphisms and relation with the norm of 1-forms: "j'ai la flemme".
- **P (2:sc78–79)** For I ≠ ∅ and E_i → Γ surjective: for each i a "transcendental family" of splittings of E → Γ
  indexed by (a torsor under) H^1(K, T(G_m)) ≃ lim (K^*)_n, containing the "geometric" subfamily indexed by K^*. The
  π-classes for distinct i are distinct, and distinct from those of rational points of X∖S, already in the extension
  of Γ by π_ab (via Mordell–Weil; details not written).
- **C (corrected case III, 2:sc79)** "sous toutes réserves": perhaps there are no splittings of the extension E of Γ
  by π other than these (rational points of U and the tangential ones at the points of S).
  N: this is the section conjecture with cuspidal sections; note that he allows the whole "transcendental" family
  lim (K^*)_n at each cusp, not only the K^*-indexed geometric one.

### §10 Ajustement des hypothèses (2:sc80–81, p. 38)

- Morphisms should be arbitrary f: X'∖S' → X∖S (so S' ⊃ f̂^{-1}(S)_red). In B: a morphism carries a subset
  I'_f ⊂ I', f_{D*} defined on Π'_{D*,I'_f} only, and f_E trivial on E'_{i'} for i' ∉ I'_f. N.B.: this is "plugging
  the holes" i' ∉ I'_f: replace E' by its quotient by the normal subgroup generated by the L_{i'} (i' ∉ I'_f).

### §11 Conditions on systems coming from geometry (2:sc82–88, pp. 39–42)

For T(K̄) –κ_i→ E_i ↪ E –p→ Γ (dim 1; I may be empty):
- (a) Im p open; a section exists over an open subgroup Γ' ("admissible section", to be defined, excluding the
  "trivial" ones from the E_i). (b) Σ_i = Im(E_i → Γ) open and E_i a trivial extension of Σ_i by L_i, with the
  privileged K_i^*-torsor of "algebraic" splittings.
- Case all E_i → Γ surjective: (c) each exterior κ_i: T → π is compatible with the exterior action of Γ (through χ
  on T): for g ∈ E there is α ∈ π (not only in E) with int(g) κ_i(ξ) = int(α) κ_i(χ(p(g)) ξ). Hence the action of Γ
  on π is "très non triviale"; "il n'était pas même évident a priori (sans raisons arithmétiques profondes!) qu'il
  existe de telles opérations de Γ sur un π".
- (d) There are a basis η of T, α_i ∈ π (κ'_i = int(α_i)∘κ_i), g ≥ 0, x_j, y_j ∈ π with: the κ'_i(η), x_j, y_j
  generate π; the relation ∏_{j=1}^g [x_j,y_j] · κ'_1(η) ... κ'_ν(η) = 1; and this presents π as a profinite group.
  g is determined (π_ab/Σ κ_i(T) free of rank 2g over Ẑ; π_ab free of rank 2g + ν − 1). **P** (2:sc86–87) if η works
  then so does χ(α)η for α ∈ Γ, up to conjugates; taking K = Q (and admitting a curve of genus g over Q with ν rational
  points): if the l_i fit into a privileged generating system, then for every ρ ∈ Ẑ^* suitable conjugates of the
  l_i^ρ fit as well. "Même pour ρ = −1 ce n'est pas entièrement trivial".
- (e) (2:sc87–88) "draconian" non-triviality: for every open subgroup E' ⊂ E, π' = π ∩ E', Γ' its image: the
  representation of Γ' on the quotient of (π'_ab)_(ℓ) by the sum of the images of the L'_{i'} (the "abelian variety
  part") is pure of weight 1, with characteristic polynomials of Frobenius in Z and independent of ℓ.

### §12 The topological analogy (2:sc89–109, pp. 43–53)

- X compact orientable surface, S finite. T := Z twisted by the set of orientations; T-orientation. Π_U fundamental
  groupoid of U = X∖S; Π_{D*} fundamental groupoid of germs of X around S minus S; for T-oriented X the local system
  of π_1 of Π_{D*} is canonically T. **P** (2:sc90) a 2-equivalence between the (isotopy) 2-category of pairs (X,S),
  X compact T-oriented, and the 2-category of systems (Π_{D*} → Π_U, κ: T ≃ π_1(Π_{D*}/e)) satisfying: π_0 finite;
  per component, π with κ_i: T → π such that for a generator of T, an order on I, conjugates l_i of the κ_i(gen) and
  x_α, y_α: (∏ [x_α,y_α]) ∏ l_i = 1 is a defining relation. For I = ∅ the datum is κ: H^2(π,Z) ≃ T (margin: part of
  the definition of loop groups). Exclude (S^2, ∅); (S^2, pt) need not be excluded; outside g = 0, ν ≤ 1 the κ_i are
  injective. For T = Z: elements l_i ∈ π, "la définition usuelle des structures à lacets" (thesis of Yves
  Ladegaillerie; missing there: morphisms other than homeomorphisms, e.g. ramified coverings — **Q** needs an ad hoc
  notion of isotopy).
- Change of orientation: κ ↦ κ^{-1} (l_i ↦ l_i^{-1}; for I = ∅, κ ↦ −κ).
- Group actions (2:sc93–101): Γ acting on (X,S) with a character χ: Γ → {±1} (χ(g) = −1 iff g reverses
  orientation). Mixed fundamental groupoids Π_{D*,Γ} → Π_{U,Γ} → Π_{e,Γ}; E_{U,Γ} = π_1(U,Γ) → Γ; I = S/Γ;
  E_i = π_1(D_{i0}^*, Σ_{i0}) with Σ_{i0} the stabilizer of s_i (cyclic or dihedral if finite and faithful near s_i);
  κ_i: T ≃ L_i = Ker(E_i → Γ), E_i-equivariant through χ p_i. Since Centr(π) = 1 (except the annulus), an extension of
  Σ by π = a homomorphism Σ → Autext(π); the exterior automorphisms respect the loop structure up to the sign χ.
  **P** (2:sc99) E_i = Norm_E(L_s) (uses Norm_π(L_s) = L_s). So the datum (E → Γ, E_i, κ_i) ⇔ (a) π with its T-loop
  structure, (b) a subgroup Σ ⊂ Γ and a homomorphism Σ → "Teichmüller étendu de π" (exterior automorphisms respecting
  the loop structure up to sign), compatible with χ and the sign character.
- **Summary functor (2:sc101)**: {isotopy category of (X,S,Γ): X compact T-oriented surface, S discrete, Γ acting by
  χ-automorphisms, transitive on π_0(X), card S_0 ≥ 3 on sphere components} → {exterior T-loop groups π, non
  commutative, with an action of a subgroup Σ ⊂ Γ}. **P** "Je présume" it is fully faithful without essential
  difficulty (margin: "Ça vaudrait drôlement le coup de le faire très soigneusement"). **Q/open (2:sc101–102)**:
  for Γ a given finite group, essential surjectivity "est un problème ouvert sur lequel les gens sèchent": whether
  every finite subgroup of the extended Teichmüller group is realized as a group acting on (X_0,S_0), essentially
  uniquely; i.e. with A = Homeo (or Diffeo) of X_0, A^0 its identity component (contractible in the anabelian cases),
  A/A^0 = T_{g,ν} (Teichmüller group, genus g, ν holes): does every finite Σ ⊂ T_{g,ν} lift to A, and are two lifts
  conjugate by an element of A^0? (N: Nielsen realization, proved by Kerckhoff 1983; the conjugacy/uniqueness-up-to-
  isotopy part is a separate statement — to be checked in the literature step. This is the topic of LM4.)
- Classifying topoi (2:sc103–109): for an exterior group π with trivial centre, B_π is defined functorially for
  isomorphism classes of exterior isomorphisms (the conjugating element is unique); works for any exterior
  homomorphism with trivial centralizer in π (margin: for anabelian loop groups and homomorphisms with image of
  finite index). For an action of Σ on the exterior group π: B_{π,Σ} = B_E. For an injective exterior Λ = [κ]: T → π
  with Centr_π(κ) = κ(T): the connected abelian groupoid Π_Λ (objects κ ∈ [κ], Hom = Transp_π), B_Λ → B_π; and for
  Θ: π' → π with Λ = Θ∘Λ'∘(d·id_T) a morphism B_{Λ'} → B_Λ with commutation datum. With groups of operators: "Je
  déclare forfait — il est évident que tout marche bien!".

### §13 (B.) Return to the arithmetic case: "Galois" formulations (2:sc109–, p. 53–)

- Over K of finite type over Q (NB: over F_p one would use prime-to-p fundamental groups), with K̄ and
  Γ = Gal(K̄/K): the simplest description is by exterior loop groups with exterior actions of open subgroups Σ ⊂ Γ:
  choose a component Ū_0 of Ū, Σ its stabilizer; Σ acts exteriorly on π_1(Ū_0), which carries a T(K̄)-loop structure
  indexed by I = S_0(K̄).
- (2:sc111–115, pp. 54–56) The action of Σ on π is compatible with the loop structure and the cyclotomic character
  χ; it recovers I as a Σ-set, hence the étale K-scheme S, and the whole diagram Π_{D*} → Π_U → Π_e. Morphisms
  (X',S') → (X,S) (S' ⊃ f^{-1}(S), f dominant) = exterior homomorphisms π' → π compatible with the actions of
  Σ' ⊂ Σ and the anabelian loop structures (a map τ: I' ⊃ S̄'_0 ∩ f^{-1}(S̄_0) → I and integers d_i).
  For I = ∅ the loop structure is completed by κ: T^{⊗-1} ≃ H^2(π, Ẑ), i.e. Ẑ ≃ H^2(π, T), compatible with Σ; a
  morphism with S = S' = ∅ must make the square with the degree d commute (d = order of Coker f^*). **Q (2:sc113)**:
  the compatibility of Kummer data when S = ∅, S' ≠ ∅ = describing a "cohomological" Kummer structure on the group
  π̃' obtained from a loop group π' by dividing by the loops ("bouchage des trous"); same question topologically and
  arithmetically; he will return to it.
- **P/C (2:sc114–115)** For an anabelian (X̄, S̄) over K̄: the group G of "Γ-automorphisms" (γ ∈ Γ, f a loop-respecting
  exterior automorphism of π, compatible) "(pro-fini ???)" with G → Γ of open image and kernel G_0 = loop exterior
  automorphisms of π commuting with the action of the "kernel" (conjecturally, by the bordelic conjecture,
  G_0 ≃ Aut_K̄(X̄, S̄), finite). A model over K = a splitting Γ → G of 1 → G_0 → G → Γ (hoped fully faithful).

### §13bis Return to the notion of loop group (2:sc115–118, pp. 56–57)

- **D** (π, ([L_i])_{i∈I}), a family of conjugacy classes of subgroups, is a *loop structure of type (g,ν)* if there
  are L_i ∈ [L_i] with generators l_i, elements x_α, y_α (1 ≤ α ≤ g) and an order on I with
  [x_1,y_1]...[x_g,y_g] l_1...l_ν = 1 a presentation of π. g = 0 and ν = 0 allowed.
- **P** ν ≠ 0: π free on 2g+ν−1 generators, non-abelian unless g = 0, ν ≤ 2; ν = 0: abelian only for g ≤ 1 (his
  bracket says "g = 0, ν ≤ 3 ou g = 1, ν = 0"; N: the 3 is a slip, π_{0,3} is free of rank 2). Canonical exact
  sequence 0 → T_π → ∏ L_i → π_ab → π̃_ab → 0 with T_π ≃ Z (I ≠ ∅, π ≠ 0) the *module of orientations*, T_π → L_i
  isomorphisms; for I = ∅, g ≠ 0: T_π := H^2(π,Z)^{⊗-1}. Outside g = 0, ν ≤ 2 the classes [L_i] are distinct; every g
  normalizing L_i centralizes it (clear for ν ≥ 2; margin **Q**: check ν = 1 separately: normalizer of ⟨∏[x_α,y_α]⟩
  in the free group). An action of Σ on (π,[L_i]) gives χ: Σ → {±1}; T-loop structures; actions compatible with χ.
- **Q/unproved (2:sc118)** profinite (or prime-to-p) variants: two points to verify: Norm_π(L_i) = Centr_π(L_i) = L_i
  (case ν = 1), and Centr(π) = 1; more generally the centralizer of every open subgroup of π is trivial. Margin: "Ce
  n'est démontré pour le moment dans aucun cas anabélien profini!" (N: settled since; to cite exactly in
  READING_BASE: centre-freeness of profinite surface groups and of their open subgroups; self-normalization of
  inertia/loop subgroups.)

### §14 Cohomological digression on plugging holes (2:sc119–132, pp. 58–64)

- X locally noetherian regular of dim 1, S closed discrete, U = X∖S. Étale sheaves F on X with F|U locally constant
  = triples (F_U, F_D, φ: σ^*F_D → ρ^*F_U) (Artin gluing) on the diagram B_{π1,D*} → B_{π1,U}, B_{π1,D}; the case φ iso
  = locally constant on X; B_{π1,X} is the amalgamated sum; π_1(X) = π_1(U)/⟨⟨ρ_i(Π_i)⟩⟩ (Π_i = Ker σ_i).
- The mixed topos B_{X,U} (later written B_{X;S}): X_ét –f→ B_{X,U} –g→ B_{π1,X}. Questions: (a) compute its
  cohomology by profinite group cohomology; (b) is H^*(B_{X,U},F) → H^*(X_ét, f^*F) an isomorphism for torsion F?
  B_{π1,U} → B_{X,U} is an open induction morphism with closed complement B_{π1,D}; exact sequence with H^i_S.
  **P (Prop., 2:sc129)** the comparison is an isomorphism provided H^i(E, F_E) → H^i(U_ét, F_U) is an isomorphism for
  all i ("cohomology of U computed Galois-wise"). OK for U an affine curve over algebraically closed k and F prime to
  the characteristic; then for affine U over any k; quasi-projective **Q**. Margin: for X with locally constant
  coefficients: not for genus 0; for projective smooth curves of genus ≠ 0 "il faut un argument spécial".
- X projective connected over algebraically closed k: (a) S = ∅: H^2(π,T) ≃ H^2(X,T) ≃ Ẑ; (b) S ≠ ∅: the H^i_!(U,−)
  are computed Galois-wise from the loop group; canonical L_i ≃ H^2(π,Ẑ)^{⊗-1} (g ≠ 0), and in all cases with ν ≠ 0:
  H^2_!(B_{π1,U}, Ẑ) ≃ T_π^{⊗-1}: a cohomological description of the orientation module common to both cases
  (2:sc130–131). **Q** (2:sc131–132) for a homomorphism of loop groups f: π' → π (τ: I'_0 → I, degrees d): construct
  B_{X',U'} → B_{X,U} and a trace on compactly supported cohomology inducing the isomorphism of orientation modules.
- "14" again (2:sc132–137, pp. 64–67): **mixed morphisms** f: (X',S') → (X,S) with S' = S'_0 ⊔ S'_1,
  S'_0 = f^{-1}(S), S'_1 → U. The points of S'_1 give B_{D'_1} → B_U: a family of universal coverings of U, i.e. of
  π-torsors (P_{i'}). With a group Γ of operators: for each orbit a torsor P under π and a splitting of E^P → Γ over
  the stabilizer Γ_{s'}: a class of π-conjugacy of splittings of E over Γ_{s'}. An automorphism = α ∈ π centralizing
  Γ_{s'}. **P/C (2:sc136)** if π^{Γ_{s'}} = 1 the object is defined up to unique isomorphism by its class; "Il me
  semble probable que ceci soit toujours le cas dans le cas arithmétique" (Γ_{s'} open in Γ_K). This "goes in the
  direction of the conjecture that a class of splittings of E over Γ is as good as a rational point of U over K".

### §15 Topological case: critical orbits and splittings; finite groups acting on surfaces (2:sc137–160, pp. 67–79)

- Γ finite acting on a loop group π, coming from Γ acting on (X,S), anabelian case. (a) the action is trivial ⇔
  Γ → Autext(π) trivial (a finite-order automorphism isotopic or homotopic to the identity is trivial).
  Γ^0 = Ker χ; Y = X/Γ^0; conformal structures.
- Each x ∈ U^Γ gives a class of π-conjugacy of splittings of E → Γ (lifts of Γ → Autext π to Aut π).
  **Question (2:sc139)** (Γ^0 ≠ 1) is U^Γ → {classes} bijective? For Γ^0 = 1, Γ = {±1}: π_0(X^Γ − S^Γ) → {classes},
  same question.
- **P (Théorème, 2:sc140–141)** U connected space, Γ finite acting, 1 → π → E → Γ → 1 acting on Ũ. The map (*)
  U^Γ → {π-classes of section subgroups Γ' ⊂ E}; image = classes with Ũ^{Γ'} ≠ ∅; the fibre over [Γ'] is the image of
  Ũ^{Γ'}; Ũ^{Γ'}_x is a torsor under π^{Γ'}. Equivalent: (a) (*) bijective and π^{Γ'} = 1 for every section subgroup;
  (b) every section subgroup Γ' has exactly one fixed point on Ũ.
- **P (Lemme fondamental, 2:sc141–148)** Γ finite acting faithfully on D ≃ R^2 with Γ^0 ≠ 1: (a) exactly one fixed
  point; (b) Γ^0 cyclic, Γ dihedral if Γ ≠ Γ^0; the action is conjugate to the standard one (μ_n, or dihedral with
  complex conjugation). Proof: (a) with an invariant C^2 structure: invariant conformal structure, uniformization,
  maximal compact subgroup O(2,R); the rest = "non-wildness" always holds for Γ^0: induction on the order; existence
  of a fixed point (else D/Γ is a surface and D → D/Γ a ramified covering: pull back a conformal structure);
  uniqueness reduces to **Lemme**: a finite-order homeomorphism of C commuting with z ↦ z+1 and fixing 0 is the
  identity — **gap he leaves (2:sc147)**: "On doit pouvoir terminer par la suite spectrale d'Adams... je n'entre pas
  dans ces dédales". (d) Γ ≠ Γ^0: the unique fixed point of Γ^0 is Γ-invariant. **Missing (2:sc148)**: the analysis
  of an anti-involution near a fixed point (margin: an involutive anti-automorphism τ of D is conjugate to z ↦ z̄;
  would give π_0(U^Γ) ≃ classes of sections for Γ ≃ Z/2 acting by anti-automorphism, U orientable ≠ S^2).
  (N: classical: Brouwer–Kerékjártó–Eilenberg, every periodic homeomorphism of the plane or disc is conjugate to a
  rotation or reflection; to cite.)
- **P (Théorème, 2:sc148–149)** U paracompact connected surface, Γ finite acting faithfully, Ũ non-compact (U not
  S^2, not RP^2); if U orientable, Γ^0 ≠ 1; if U non-orientable, card Γ ≥ 3. Then: (a) U^Γ → {π-classes of splittings
  of E → Γ} is bijective; (b) π^{Γ'} = 1 for every section subgroup; (c) if a splitting exists, Γ is cyclic or
  dihedral.
- **P (Corollaire, 2:sc150–151)** U orientable, Γ orientation-preserving; U^! := {x : Γ_x ≠ 1} (discrete). (a) the
  partial sections attached to x ∈ U^! are maximal among those ≠ 1; (b) U^! → {π-classes of maximal partial sections
  ≠ 1} is bijective (Γ-equivariantly); (c) π^{Γ'} = 1.
- (2:sc152–154) Hence J ≃ U^! is intrinsic in the exterior action of Γ on π; the set of all maximal partial sections
  is an E-set with free π-action, canonically Ũ|U^!; S' = S ∪ U^!: "il s'impose d'essayer de reconstituer" the
  exterior loop group of U' = X∖S' with its Γ-action from E.
- **P (2:sc155)** "draconian" conditions on a geometric extension E (faithful action): every Γ' ⊂ E with Γ' ∩ π = 1
  is cyclic (or dihedral); finitely many π-classes; every section subgroup ≠ 1 lies in a unique maximal one (proved
  for Γ = Γ^0; general case **Q**).
- **D (2:sc155–156)** the extra structure μ_E: {elements of finite order of E} → T ⊗ Q/Z: the "multiplier" (rotation
  number at the fixed point); μ(αuα^{-1}) = μ(u) for α ∈ π, μ(u^n) = nμ(u), order μ(u) = order u.
  **Q (2:sc156, 160)** "J'ignore si" μ is intrinsic in the extension E, or whether two geometric extensions can be
  isomorphic without respecting μ, μ'. Abelian case π ≃ Z^2 (2:sc157–159): E ⇔ a Γ-X_0(π)-torsor via
  H^2(Γ,π) ≃ H^1(Γ, X_0(π)); μ(u) = one of the two eigenvalues of u ⊗ C: for an elliptic curve the extra datum is one
  of the two roots in Ω of the characteristic equation T^2 + aT + b of u, "ne peut se déduire de la seule
  connaissance de l'action de u sur π". Margin answer for the group with 1 loop: yes, μ can be deduced from the
  exterior action on the loop group via the subgroups E_i (extensions 1 → T → E_i → Γ_i → 1 with Γ_i ≃ T/n_iT).
  Hence "C'est cette question de forage de trous qu'il faut ... attaquer!". Anabelian case: "la question reste
  entière" (margin: seems so, since for solvable Γ every action on π is geometrically realizable).

### §16 Plugging and drilling holes: general topos preliminaries (2:sc160–178, pp. 79'–88)

- Start from multigaloisian topoi B_U ←ρ– B_{D*} –σ→ B_S (σ iso on Π_0, surjective on Hom); over a base field the
  square over B_e. Glued (non-multigaloisian) topoi B_{X;S} (from B_U and B_S via σ_*ρ^*) and B_{D;S} (≃ D_ét in the
  geometric case); diagrams (**) (2-cartesian squares, "sauf erreur"), (***) of the Π_1-envelopes with B_X the
  amalgamated sum = "bouchage de trous": π_X = π/⟨⟨ρ_i(L_i)⟩⟩; **Q** B_{X;S} → B_X etc. "ont une nette tendance d'être
  acycliques (il faudrait voir ce point)". Partial plugging B_{U ∪ S_0}; transitivity.
- Actions of a group Γ on a topos B ⇔ B as a Γ-Galois covering of (B,Γ) = "B/Γ"; a diagram B_{D*} → B_U with Γ-action
  ⇔ B_{D*,Γ} → B_{U,Γ} → B_Γ, completed by B_{D*,Γ} → B_{I,Γ} → B_Γ (canonical factorization); recovers the §7
  diagram. The arithmetic situation = the geometric one over K̄ with the action of Γ = Gal(K̄/K). Quotient commutes
  with hole plugging.

### §17 Complement on finite group actions on surfaces (2:sc179–181, pp. 89–90)

- U paracompact connected surface with π_1 ≠ 1; "anabelian" iff π non-abelian (U not C^*, S^1×S^1). Γ finite acting.
  **P** equivalent: (b) every g_U isotopic to id; (b') homotopic to id; (c) the exterior action on π_1(U) trivial;
  (d) (anabelian) E ≃ product extension, (abelian) E central; (a) (anabelian) Γ acts trivially, (abelian) U is a
  topological group (C^* or S^1×S^1) and Γ acts by translations through Γ → U. Margins: prudent to assume Γ
  preserves an orientation (counterexample z ↦ 1/z̄ on C^*); d ⇒ a in the abelian case "pas prouvé!" (needs the
  topological classification of finite group actions on C^* and S^1×S^1); with U^Γ ≠ ∅ it holds.

### §18 Drilling holes; application to exterior actions of finite groups (2:sc182–203, pp. 91–101)

- Π' a loop group of type (g,ν+1), non-abelian; i ∈ I'. π := Π'/⟨⟨L'_i⟩⟩; it is independent of the choice of L'_i up
  to *unique* isomorphism (as a group, not only exterior). **Functor β** ("bouchage du trou i"):
  {exterior loop groups of type (g,ν+1) with a distinguished class i} → {(realized) loop groups of type (g,ν)},
  i.e. a homomorphism (*) Autext(π', i) → Aut(π). Geometrically: after plugging, s_i is a canonical base point.
- **P (Théorème, 2:sc186–189)** If the groups π' and the plugged groups π are both anabelian (his bracket:
  "g ≥ 2, ou g ≥ 1, ν ≥ 2, ou g = 0, ν ≥ 4", the count ν being that of π'), then β is an equivalence:
  Autext(π', i) → Aut(π) is an isomorphism. Proof sketch: Autext_lac(Π_{g,ν}) restricted to identity on I and on T
  =: T^{00}_{g,ν} ("groupe de Teichmüller d'indice g,ν") is π_1 of the complex modular topos M_{g,ν} (2g+ν ≥ 3;
  universal covering contractible, Teichmüller); M_{g,ν+1} is the universal curve with ν numbered holes over
  M_{g,ν}; homotopy exact sequence 1 → Π_{g,ν} → T^{00}_{g,ν+1} → T^{00}_{g,ν} → 1, which "à passage à un sous-groupe
  d'indice 2ν! près" is the wanted extension; the compatibility checks are left. (N: the Birman exact sequence in
  the form Aut(π_{g,ν}) ≃ Autext(π_{g,ν+1}, i).) Quasi-inverse = "forage de trou": from (B_{D*} → B_U, a point Ũ)
  canonically a system of type (g,ν+1).
- With a group Γ acting on π (not only exteriorly): an exterior action on π' fixing i; E'_i := Norm_{E'}(L'_i),
  1 → L'_i ≃ T → E'_i → Γ → 1.
- **P (Théorème, 2:sc191–192)** Γ finite acting faithfully on an exterior loop group π of type (g,ν+1) fixing
  i ∈ I(π): Γ is cyclic (Γ = Γ^0) or dihedral; E_i^0 ≃ Z, x ↦ x^n gives E_i^0 ≃ L_i, hence a canonical isomorphism
  Γ^0 ≃ E_i^0/L_i ≃ T/nT. Reduced to the **lemme fondamental (2:sc193–194)**: a direct exterior automorphism u of
  finite order of a loop group fixing a class i, with trivial induced extension of Z/n by L_i, is trivial;
  equivalently (**Corollaire**) a direct finite-order automorphism u_0 of π that normalizes (= centralizes) a loop
  subgroup L_i is the identity. **Status in his text (2:sc195–196)**: proved *if* every faithful exterior action of
  a cyclic group (prime order suffices) on a loop group of type (g,ν+1) is geometrically realizable — "sauf erreur
  ce résultat est bien connu (même pour les groupes résolubles...)"; doubt whether known for general (g,ν) or only
  g ≥ 2, ν = 0; he *admits* the lemma. (N: Nielsen for cyclic, Fenchel for solvable, Kerckhoff 1983 in general; to
  pin down with exact hypotheses, punctured case included.) Margin: the abelian cases (0,2), (1,0) are not trivial
  but should hold.
- Consequences for a faithful exterior action of finite Γ on an anabelian loop group, extension E: (a) partial
  splittings exist only over Γ' with Γ'^0 cyclic, Γ' dihedral otherwise; (b) for each class of partial splittings over
  Γ' ⊂ Γ^0 a canonical Γ' ≃ T_n: i.e. a canonical map {finite-order elements of Aut_lac(π)} → T ⊗ Q/Z (2:sc196).
  **Questions left for the non-realized case (2:sc197–198)**: (c) for finite Γ ⊂ Aut_lac(π) is π^Γ = 1? (d) if finite
  Γ', Γ'' ⊂ E have Γ' ∩ Γ'' ≠ 1, are they in the π-conjugate of one finite Γ''' (unique maximal section subgroup)?
  (e) finitely many π-classes of lifts of Γ' to E? (c), (e) OK granted realizability of cyclic exterior actions.
  A "Théorème" (2:sc198–200: for finite Γ_0 ≠ 1 in A = Aut_lac(π)^0 the normalizer equals the centralizer Z, and the
  finite-order elements of Z form a cyclic group, the largest finite subgroup containing Γ_0) is struck through and
  marked "pas vrai!", "faux!" (at the uniqueness lemma for a d-th root u of u_0 fixing a).
- **P (proof of (d), 2:sc201–203)** reduction to Γ_0 = Γ' ∩ Γ'' central in Γ and π-conjugation-invariant; the
  centralizer Γ̃ of Γ_0 in E has Γ̃ ∩ π = π^{Γ_0} = 1 and maps onto Γ: a finite subgroup of Aut(π) containing Γ', Γ''.

### §19 Tour de Teichmüller (2:sc204–, pp. 102–)

- X_g compact orientable of genus g, a sequence of distinct points (a_{g,i}); S_{g,ν} = {a_{g,i} : 0 ≤ i ≤ ν−1},
  U_{g,ν} = X_g − S_{g,ν} (the type surface; a_{g,ν} ∈ U_{g,ν}). A_g = Aut(X_g) (homeomorphisms, uniform convergence
  of u and u^{-1}); A_{g,ν} = stabilizer of S_{g,ν} ≃ Aut(U_{g,ν}); A^!_{g,ν} = pointwise stabilizer;
  1 → A^!_{g,ν} → A_{g,ν} → S_ν → 1; A^o_{g,ν} neutral component.
  **D (10),(11)** Γ_{g,ν} := A_{g,ν}/A^o_{g,ν} = π_0(A_{g,ν}) ("groupe de Teichmüller de type g,ν"; it includes the
  orientation-reversing classes and the permutations of the points); Γ^!_{g,ν} := π_0(A^!_{g,ν});
  1 → Γ^!_{g,ν} → Γ_{g,ν} → S_ν → 1 (12). Homogeneous spaces: A_g/A_{g,ν} ≃ P_ν(X_g) (ν-subsets),
  A_g/A^!_{g,ν} ≃ Mon(I_ν, X) (ordered configurations); A_g/A_{g,1} ≃ X_g.
  **P (19)–(27)** A_{g,ν} = Norm_{A_g}(A_{g,ν}) = Norm(A^!_{g,ν}) = Norm(A^o_{g,ν}); S is recovered as the fixed set of
  A^!_{g,S} (or of A^o_{g,S}), or as the points with finite (or non-dense) orbit.
- **D (2:sc208–210)** "couple de Teichmüller de type g": (G, X), a topological group with a conjugacy class of
  subgroups, isomorphic to (A_g, class of A_{g,1}); equivalently X with its homogeneous topology is a compact
  orientable surface of genus g and G → Aut(X) a homeomorphism of topological groups. **P** (G,X) ↦ X is an
  equivalence {Teichmüller couples of type g} → {compact oriented surfaces}; an automorphism of the topological group
  G is inner iff it preserves the class X; centre of G trivial. Same for type (g,ν): (G_ν, {H_ν}) ≃
  (A_{g,ν}, A_{g,ν} ∩ A_{g,ν+1}).
- (2:sc211–213, pp. 105–106) U_{g,ν} ≃ A_{g,ν}/A_{g,(ν,ν+1)} ≃ A^o_{g,ν}/B_{g,ν}, where A_{g,(ν,ν+1)} := A_{g,ν} ∩ A_{g,ν+1}
  =: A^•_{g,ν} (automorphisms of U_{g,ν} pointed at a_{g,ν}), B_{g,ν} := A_{g,ν+1} ∩ A^o_{g,ν}. Diagram (31) of
  inclusions; B^o_{g,ν} = A^o_{g,ν+1}. (32): S_ν ≃ A_{g,(ν,ν+1)}/A^!_{g,ν+1}, Γ_{g,ν} ≃ A_{g,(ν,ν+1)}/B_{g,ν},
  Γ^!_{g,ν} ≃ A^!_{g,ν+1}/B_{g,ν}. **D (33)** Ũ_{g,ν} := A^o_{g,ν}/A^o_{g,ν+1}.
- **P (Théorème, 2:sc213)** Ũ_{g,ν} is simply connected if (g,ν) ≠ (1,0), (0,2) (contractible if ≠ (0,0)): it is the
  universal covering of U_{g,ν} pointed at a_{g,ν}. **Cor (34)** B_{g,ν}/B^o_{g,ν} ≃ π_1(U_{g,ν}; a_{g,ν}) =: Π_{g,ν}.
  Proof from the homotopy sequence (35) and the **"Théorème bien connu" (2:sc215)**: equivalent for (g,ν):
  (a) 2g+ν ≥ 3; (b) π_1(U_{g,ν}) non-abelian; (c) A^o_{g,ν} simply connected (and (g,ν) ≠ (0,1)); (d) A^o_{g,ν}
  contractible. Always π_i(A^o_{g,ν}) = 0 for i ≥ 2 unless (g,ν) = (0,0). (N: Hamstrom; Earle–Eells; Earle–Schatz.)
  Abelian cases (2:sc216–219): G = Aut_C^o(U) ⊂ A^o_{g,ν} is a homotopy equivalence; G ≃ elliptic curve (1,0), C^*
  (0,2), Aff(1,C) (0,1), PGL(2,C) (0,0); margin: if k is least with (g,ν+k) anabelian then dim G = k, G simply
  transitive on k-tuples, A_{g,ν} ≃ A_{g,(ν,ν+k)} × G. **Cor** B_{g,ν} is connected exactly in the abelian cases.
- **P (Théorème, 2:sc219–221; (41),(43))** For (g,ν) ≠ (1,0), (0,2) [he also writes (0,1)]: with
  Γ'_{g,ν+1} := stabilizer of the last point a_{g,ν} in Γ_{g,ν+1} (index ν+1) ≃ A_{g,(ν,ν+1)}/A^o_{g,ν+1}:
  1 → Π_{g,ν} → Γ'_{g,ν+1} → Γ_{g,ν} → 1 (43), and 1 → Π_{g,ν} → Γ^!_{g,ν+1} → Γ^!_{g,ν} → 1 (41); (42)
  Γ'_{g,ν+1} → Γ_{g,ν} is always surjective, an isomorphism in the abelian cases 2g+ν ≤ 2 (45).
- **P ("Théorème bien connu", 2:sc221)** anabelian case: Γ_{g,ν} ≃ Autext_lac(Π_{g,ν}), equivalently (by (44))
  Γ'_{g,ν+1} ≃ Aut_lac(Π_{g,ν}). (N: Dehn–Nielsen–Baer with punctures, extended mapping class group.) **Cor** X ↦ π_1(X)
  is an equivalence {isotopy category of surfaces of type (g,ν)} → {exterior loop groups of type (g,ν)}, and
  (X,s) ↦ π_1(X,s) for pointed surfaces → loop groups; even ∞-isotopically (A^o contractible).
- Abelian cases one by one (2:sc222–229): (1,0): Γ_{1,0} ≃ Γ_{1,1} → GL(2,Z) is an isomorphism (known);
  H × A_{g,ν+1} ≃ A_{g,ν} for U a topological group H (48). (0,2): Γ_{0,2} ≃ Γ'_{0,3}; ρ: Γ_{0,2} → S_2 not injective
  (z ↦ z̄); **D (53)** χ: Γ_{g,ν} → {±1} (action on the orientation module), kernel now written **Γ^+_{g,ν}** (no
  longer Γ^0). **P (55),(56)** Γ^{!+}_{0,2} = 1; Γ^+_{0,3} ≃ S_3 and Γ_{0,3} ≃ S_3 × {±1} by (ρ, χ). (0,1): Γ_{0,1} ≃ {±1}
  (58). (0,0): PGL(2,C) × A^!_{0,3} ≃ A_0, Γ_0 ≃ Γ^!_{0,3} ≃ {±1} (61).
- **D (2:sc229–230)** loop groups of the four abelian types: (1,0): Π ≃ Z^2, T = Λ^2 Π; (0,2): the pair (Π ≃ Z, T) with
  an iso T ≃ Z as structure, automorphisms = any pair (u_Π, u_T); (0,1), (0,0): just an invertible Z-module T plus the
  type. **P (Théorème)** for every (g,ν): {isotopy category of surfaces of type (g,ν)} → {exterior loop groups of
  type (g,ν)} is an equivalence. Not satisfactory in the abelian cases (does not recover the extension for a group
  action): the equivalence is only 0/1-isotopic; in the abelian cases use Ladegaillerie's description
  B_{D*} → B_U (∞-faithful for (g,ν) ≠ (0,0)); the sphere (0,0) is "entièrement réfractaire".

### §20 Digression: 2-isotopic description of the category of topological 2-spheres (2:sc232–250, pp. 116'–125)

- The double covering group 1 → μ_2 → Ã_0 → A_0 → 1 extending SL~(2,C) → PGL~(1,C) (semi-linear automorphisms;
  PGL~(1,C) = conformal automorphisms of the Riemann sphere = R-automorphisms of M_2(C), homotopy equivalent to A_0).
  A sphere X ↦ (ω, R): ω its μ-torsor of orientations, R the μ_2-gerbe of liftings of the A_0-torsor
  Isom(P^1,X) to Ã_0. **P** a 2-equivalence of the 2-isotopic 2-category of topological 2-spheres with the pairs
  (ω, R) (2-faithful since π_2(A^o_0) = π_2(S^3) = 0; not 3-faithful since π_3 = Z). **Q** "On cherche une description
  ∞-isotopique ... Au concours!". Over a base S (CW of dim ≤ 3): H^1(S, A_0) ≃ H^1(S, Z/2) × H^2(S, μ_2) (71), via
  the Gr-stack with π_0 = Γ, π_1 = μ and vanishing Postnikov–Sinh invariant; **Q** his own direct argument for
  surjectivity fails ("je ne m'en tire pas ... consulter Giraud ou Larry Breen"). Azumaya algebras of rank 4 over a
  twisted form C of the complex numbers; fidelity degrees in terms of dim S (marked "??"). Arithmetic analogue
  (2:sc249–250): no faithful "profinite description" of projective lines over a field of finite type (all
  automorphisms from SL(2,K) would be identified with the identity); the category of Azumaya algebras of fixed
  degree "devrait être une 2-catégorie".

### §21 Link with Teichmüller spaces (2:sc251–263, pp. 125–132) [§22 does not exist]

- The group Ã_{g,ν} := A_{g,ν} ×_{Γ_{g,ν}} Γ'_{g,ν+1} (74): an extension of A_{g,ν} by Π_{g,ν}, of Γ'_{g,ν+1} by A^o_{g,ν},
  of Γ_{g,ν} by A^o_{g,ν} ⋊ Π_{g,ν} (75); it acts on the fibration Ũ_{g,ν} → U_{g,ν} (conditions a–d verified).
- With a C^∞ structure (diffeomorphism groups): **D (76)** E_g := conformal structures on X_g (∞-connected).
  E_g/A_g, E_g/A^+_g, E_g/A_{g,ν}, E_g/A^+_{g,ν}: coarse moduli M^♮_g, M^♮_{g,ν} ((77)–(80)). **D (81)**
  M̃_{g,ν} := E_g/A^o_{g,ν}, *the Teichmüller space of type (g,ν)*, with the action of Γ_{g,ν};
  M^♮_{g,ν} = M̃_{g,ν}/Γ_{g,ν}. **P (Teichmüller)** M̃_{g,ν} ≃ C^μ, μ = 3g−3+ν (anabelian), in general μ = 3g−3+ν' with
  ν' the least integer ≥ ν with (g,ν') anabelian. **Cor** in the anabelian case A^o_{g,ν} acts freely on E_g, so
  M̃_{g,ν} is a classifying space of A^o_{g,ν} and its ∞-connectedness ⇔ that of A^o_{g,ν} (the "théorème bien connu").
  He stresses: simple connectedness of M̃_{g,ν} = universal covering of the *modular topos* M_{g,ν} is deep for g ≥ 2.
- **The tower (84)** ... → M̃_{g,ν+1} → M̃_{g,ν} → ... → M̃_g, each step for anabelian (g,ν) a fibration with fibre
  Ũ_{g,ν} (contractible); for abelian (g,ν) a homeomorphism. Reduction of ∞-connectedness to M̃_g (g ≥ 2), M̃_{1,1},
  M̃_{0,3}. The universal curve X = U_{g,ν} ×^{A^o} E over M̃; Γ_{g,ν} acts on X: this realizes the canonical extension
  Γ'_{g,ν+1} of Γ_{g,ν} by Π_{g,ν} as a mixed fundamental group (details omitted by him).

### §23 Return to surfaces with groups of operators: "putting into equations" (2:sc264–281, pp. 133–141)

- 2-category S of *admissible* orientable surfaces (U = X∖S, X compact, S finite, every genus 0 component meets S),
  2-morphisms = homotopy classes of paths in Isom(U,U') (components are K(π,1)); 2-category M of morphisms of
  multigaloisian topoi B_{D*} → B_U (cofibred over the arrow category Δ_1); M_lac ⊂ M the loop condition.
  **P** S → M_lac is a 2-equivalence (Ladegaillerie's 2-faithfulness). With a group Γ, or a groupoid Π:
  RS → RM_lac ("representations" in surfaces vs diagrams B_{D*,Π} → B_{U,Π} → B_Π).
- **C (2:sc270–271)** restricted to Π with finite fundamental groups, R_f S → R_f M_lac is an equivalence of
  2-categories ("3-fidèle"). (N: this is his full classification conjecture for finite group actions on surfaces:
  existence = Nielsen realization, uniqueness up to conjugation by A^o, plus contractibility of centralizers.)
- General frame (2:sc274–281): A a topological group with π_i(A) = 0, i ≥ 2; Gr-category 𝒜 = Π_1(A); for a group Γ:
  {Γ → A} → {homomorphisms of Gr-categories Γ → 𝒜}. When π_1(A^0) = 0 (𝒜 = π_0): 0-fidelity ⇔ π_1((A^0)^u) = 0 for all
  u: Γ → A; 1-fidelity ⇔ moreover π_0((A^0)^u) = 0; 2-fidelity ⇔ moreover two lifts u, v of the same Γ → π_0 are
  conjugate by an element of A^0; 3-fidelity ⇔ moreover every Γ → π_0 = A/A^0 lifts. Summary: 3-fidelity ⇔ every
  u̲: Γ → π_0 has a lift, unique up to A^0-conjugacy, with (A^0)^u connected and simply connected. In general (π_1(A^0)
  ≠ 0) the condition should be π_1(A^{0Γ}) ≃ π_1(A^0)^Γ (margin: "à reprendre avec soin"); best: a homotopy
  equivalence. For A = A_{g,ν}: 0-fidelity ⇔ π_1(A^Γ) → π_1(A) injective. Plan: determine A^{0Γ} and prove it
  contractible (anabelian case, Γ finite).

### §24 Attempt to determine A^{0Γ}; the relation Π^Γ_{g,(ν,ν+n−1)} = (1); programme (2:sc282–294, pp. 142–148)

- Γ = Γ^+ finite acting on U ⊂ X of type (g,ν); X' = X/Γ, S' = image of S, S'^! = branch points in U' = X'∖S',
  V' = U'∖S'^!, V = preimage (a Γ-torsor over V'). f ∈ A^Γ ⇔ an automorphism of the Γ-covering V/V' whose induced
  g on V' extends and preserves S', S'^!; in terms of Π' = π_1(V') with φ: Π' ↠ Γ non-trivial on the loops of S'^!:
  g_• with φ∘g_• conjugate to φ. Since A^0 ∩ Γ = 1, f ∈ A^{0Γ} is determined by g.
- B := elements of Aut(U)^0 fixing S^! pointwise; Aut(U)^0/B ≃ Mon(S^!,U); B^0 = Aut(V)^0;
  B/B^0 ≃ π_1(Mon(S^!,U)); Aut(U)^{0Γ} = B^Γ. **P (2:sc285–286)** the neutral component of Aut(U)^{0Γ} is
  ≃ Aut(V')^0 lifted (∞-connected if V' anabelian), and π_0(Aut(U)^{0Γ}) ⊂ (B/B^0)^Γ ≃ π_1(Mon(S^!,U))^Γ. **Wanted**:
  H^0(Γ, π_1(Mon(S^!,U))) = 1 (the relation of the title: the Γ-invariants of the pure braid-type group vanish).
- **C (Conjecture, 2:sc286–287)** Π an exterior loop group of type (g,ν), Γ finite acting exteriorly. Then there are
  an exterior loop group Π' with a Γ-action, a Γ-stable I'^! ⊂ I', and a hole-plugging Π' → Π (plugging I'^!),
  Γ-equivariant, with (1) every element of I'^! has non-trivial stabilizer in Γ; (2) the extension of Γ by Π' has no
  element of finite order ≠ 1; and (Π', Π' → Π) is determined up to unique isomorphism. Commentary: existence is
  evident in the realizable case; uniqueness "même dans le cas réalisable n'est pas évidente, ni même prouvée";
  faithfulness ⇔ π_1(Mon)^Γ = 1.
- **D** Φ(Π,Γ) := set of Π-conjugacy classes of maximal partial sections ≠ 1 of the extension E ("fixed points"), a
  finite Γ-set. For (Π',Γ, I'^!) with plugging Π: the map (*) Φ(Π',Γ) ⊔ I'^! → Φ(Π,Γ); its bijectivity is proved only
  in the realizable case or for I'^! a single element (then Γ cyclic, realizable).
- **C** the functor (π',Γ,I'^!) ↦ (π,Γ, I'^! ⊂ Φ(π,Γ)) is an equivalence (essential surjectivity clear for
  realizable situations; full faithfulness not proved even there).
- **Programme of attack on realizability (2:sc292–294)**: (I) bijectivity of (*) in general; (II) full faithfulness
  of the functor (reduce to I'^! one singular orbit); (III) when Φ(π,Γ) = ∅ (E torsion-free): prove that E, with the
  E-conjugacy classes of the centralizers of the L_i, is a loop group. First for cyclic groups, by dévissage.
  **D** an exterior action of Γ on (π', I'^!) is *admissible* if Autext(π',Γ,I'^!) ≃ Aut(π,Γ,I'^!) and every other
  action with the same action on π and the same map I'^! → Φ(π,Γ) is conjugate to it. **Criterion**: a faithful
  exterior action of Γ on π is realizable iff it lifts by drilling (I'^! = Φ(π,Γ)) to an admissible action on
  (π', I'^!) whose extension E' of Γ by π' is a loop group.

### §25 "Special" Teichmüller groups (2:sc294–, pp. 148–)

- **D** SA_{g,ν} := automorphisms of X_g that are the identity near S_{g,ν} (compactly supported automorphisms of
  U_{g,ν}; not closed; for surfaces with boundary: identity on the boundary). A_{g,ν}/SA_{g,ν} = germs at infinity.
  SΓ^!_{g,ν} := SA_{g,ν}/SA^0_{g,ν} → Γ^{!+}_{g,ν}.
- Algebraic model: for u ∈ Aut(π) strictly respecting the loop structure, u(l) = int(g_i^{-1})(l^α) on L_i
  (α = χ(u)), g_i determined modulo L_i on the right. **D** SE^! := {(u, (g_i))} with
  (v,(h_i))·(u,(g_i)) = (vu, h_i v(g_i)), a subgroup of E^! ⋉ π^I; 1 → T^I → SE^! → E^! → 1, and likewise SΓ^!
  (classes of auto-equivalences of B_I → B_{D*} → B_U inducing the identity on I), with SE^! the inverse image of
  SΓ^!. Without the restriction "identity on I": extensions SE of E and SΓ of Γ by T^I, and
  1 → T^I × π → SE → Γ → 1. Notation: E_{g,ν} = Aut_lac(Π_{g,ν}) (≃ Γ'_{g,ν+1}), SΓ_{g,ν} = S Autext_lac(Π_{g,ν}).
- (2:sc301–306, pp. 151–154) SA_{g,ν} → SΓ^{!+}_{g,ν} (take γ_i = identities); surjectivity easy; injectivity via
  surfaces with boundary: 1 → SA'^+ → A'^{!+} → ∏ Aut^+(C_i) → 1 and its homotopy sequence
  0 → π_1(SA^0) → π_1(A^0) → T^I → π_0(SA^{!+}) → Γ^{!+} → 1. **P (Théorème, 2:sc304)** for ν > 0: if (g,ν) is anabelian,
  π_0(SA_{g,ν}) ≃ SΓ^{!+}_{g,ν}, i.e. 1 → T^{S_{g,ν}} → π_0(SA_{g,ν}) → Γ^{!+}_{g,ν} → 1; in all cases (SA_{g,ν})^0 is
  ∞-connected. Abelian cases: (0,2): the kernel is T (quotient of T^I by the image of π_1(C^*)); (0,1): π_0(SA) = 0.
  (N: this is the central extension of the mapping class group of the surface with boundary by the boundary Dehn
  twists.) For i ∈ I: the extension of Γ_i by T obtained from (SΓ)_i by pr_i = the group of loop automorphisms of π_i
  normalizing L_i; so SΓ "a une nette tendance à ne pas être triviale" (non-trivial over every finite G ≠ 1 in Γ_i^+).

### §25bis The case of two groups; notation reset (2:sc307–317, pp. 153'–160)

- Model: a curve U over K of finite type with G_K = Aut_K(U) (or G_K̄, finite in the anabelian case) and
  Γ = Gal(K̄/K) both acting exteriorly on π_1(U_K̄). Topologically: G finite, Γ arbitrary, 𝒢 = Γ·G acting on U,
  extension (1) 1 → π → E → 𝒢 → 1. For Q ∈ U with G_Q^+ ≠ 1 and a path class λ from P to Q: a lifting
  r: G_Q → E, unique up to a unique element of π (π^{G_Q} = 1); the lifting of Γ_Q (indeed of 𝒢_Q) is then forced:
  it lies in Centr_E(r(G_Q)) (when Γ centralizes G), and Norm(r(G_Q)) → 𝒢 is injective. **P** "le choix d'un
  relèvement du (petit) groupe G_Q impose déjà le choix d'un relèvement du (grand) groupe Γ_Q, ou 𝒢_Q"; the image in
  𝒢 of the normalizer of r(G_Q) is exactly 𝒢_Q. In the universal Γ' = Autext_lac(π): Γ'(Q) := image of
  Centr_{E'}(r(G_Q)); Γ'^♮ := ∩_Q Γ'(Q) ⊃ 𝒢^♮; **Q** can Γ^♮ (= ∩ Γ_Q, of finite index in Γ) be characterized as
  Centr_{Γ'^♮}(G), and Γ recovered from it?
- His case of interest: profinite variant for U = P^1_Q∖{0,1,∞}, G = S_3, Γ = Gal(Q̄/Q), P = exp(2iπ/6). "Je n'ai pas
  vérifié que Γ → Autext_lac(π̂) soit injectif" (→ §35).
- **Notation from here on (2:sc313–316)**: G for geometric (mostly finite) group actions; Γ for Galois groups; 𝒢 for
  mixed groups; **𝒯, 𝒯_{g,ν}** for the universal Teichmüller-type groups previously written Γ_{g,ν}; **boldface Γ**
  = Gal(Q̄_0/Q) (Q̄_0 the algebraic closure of Q in C); **Γ_{g,ν}** (bold) := Norm_{𝒯̂̂_{g,ν}}(𝒯̂_{g,ν})/𝒯̂_{g,ν} (later
  corrected to use 𝒯̂^+); **𝔖_{g,ν}** for the universal extension of 𝒯_{g,ν} by π_{g,ν} (previously Γ'_{g,ν+1},
  E_{g,ν}); E kept for sub-extensions. Single hat = profinite completion of the discrete group; double hat = the full
  profinite object: 𝒯̂̂ = Autext_lac(π̂), 𝔖̂̂ = Aut_lac(π̂).
  For (0,3): Γ_{0,3} = centralizer of G = S_3 = 𝒯^+_{0,3} in 𝒯̂̂_{0,3}, contained in 𝒯̂̂^!_{0,3}, "peut-être égal";
  canonical **Γ → Γ_{0,3}** (more generally Γ → Γ_{g,ν}), "dont j'ignore pour l'instant s'il est injectif, et encore
  plus s'il est surjectif". Necessary condition for γ ∈ Γ_{0,3} to come from Γ: it has a lift commuting with ρ and a
  lift commuting with σ_0 (interesting if π̂^ρ = π̂^{σ_0} = 1); possibly no restriction.

### §26 Profinite Teichmüller groups; discretifications and prediscretifications; the modular topos; "hasty conjecture" (2:sc318–339, pp. 161–171)

- π a profinite loop group of type (g,ν), T its invertible Ẑ-module of orientations, anabelian. **Admitted (1)**:
  Centre(π) = 1, and the centralizer of every open subgroup is trivial. Then (2') 1 → π → 𝔖̂̂(π) = Aut_lac(π) →
  𝒯̂̂(π) = Autext_lac(π) → 1; 𝒯̂̂(π) = *extended Teichmüller group*.
- **D** a *base* of π: (x_i, y_i, l_j) with l_ν ... l_1 [x_g,y_g] ... [x_1,y_1] = 1 a generating relation, l_j generating
  the loop groups; Bases(π) ≃ Isom_lac(Π̂_{g,ν}, π) (5), a torsor under 𝔖̂̂(π). *Discretization* of π: the subgroup
  Π_0 = u(Π_{g,ν}) generated by a base; Discrét(π) ≃ Isom_lac(Π̂_{g,ν},π)/𝔖_{g,ν} (6) (not Hausdorff since 𝔖_{g,ν} is
  not closed); Aut_lac(π, Π_0) ≃ Aut_lac(Π_0) (7). **Admitted**: 𝔖̂_{g,ν} → closure of 𝔖_{g,ν} in 𝔖̂̂_{g,ν} is
  injective. **D** Discrét'(π) := Isom_lac(Π̂_{g,ν},π)/𝔖̂_{g,ν} (8): its elements = *classes of discretizations* =
  "quasi-", from §27 on **prediscretizations** π_0^♮; stabilizer 𝔖̂(π_0^♮), image 𝒯̂(π_0^♮) ⊂ 𝒯̂̂(π) (10). Depends only
  on the exterior group: Isomext(Π̂_{g,ν},π)/𝒯̂_{g,ν}; the degree 2 covering by /𝒯̂^+_{g,ν}: *oriented*
  prediscretizations. (He notes: "On montre par voie arithmético-géométrique que l'inclusion 𝒯̂ → 𝒯̂̂ n'est jamais
  un iso.")
- **D** the conjugacy class of closed subgroups 𝒯̂(π_0^♮) ⊂ 𝒯̂̂(π): the *geometric Teichmüller subgroups*. A first
  guess (𝒯̂_{g,ν} its own normalizer in 𝒯̂̂_{g,ν}) is retracted in the margin: "complètement déconnant et ultra-faux
  ... La question judicieuse c'est si 𝒯̂ est invariant dans 𝒯̂̂". Characters (12) χ: 𝒯̂̂ → Ẑ^*, (13) 𝒯̂̂ → S_I;
  subgroups 𝒯̂̂^!, 𝒯̂̂^+, 𝒯̂̂^{!+}; χ takes only the values ±1 on 𝒯̂. **D** Σ := 𝒯̂^+(π_0^♮): the *strict* geometric
  Teichmüller subgroups ("peut-être n'y en a-t-il qu'un seul"); **N_Σ := Norm_{𝒯̂̂}(Σ)** (14) ("peut-être toujours
  égal à 𝒯̂̂"); **Γ_Σ := N_Σ/Σ** (bold; Γ_π if Σ is unique). The 𝒯̂ with 𝒯̂^+ = Σ ↔ a conjugacy class of elements of
  order 2 of Γ_Σ: the *canonical involutions* (16).
- **The arithmetic input (2:sc326–333)**: M_{g,ν,Q} the modular topos (stack) over Q of curves of type (g,ν);
  π_1(M_{g,ν}) =: the *arithmetic Teichmüller group*; (19) 1 → π_1(M_{g,ν,Q̄}) → π_1(M_{g,ν}) → Gal(Q̄/Q) → 1; (20)
  π_1(M_{g,ν,Q̄}) ≃ 𝒯̂^+_{g,ν} (transcendental Teichmüller theory); the universal curve 𝒰_{g,ν} gives (21)
  1 → π → π_1(𝒰_{g,ν}) → π_1(M_{g,ν}) → 1 mapping to (22) 1 → π → 𝔖̂̂(π) → 𝒯̂̂(π) → 1. An isomorphism Q̄ ≃ Q̄_0
  (embedding in C) transports the standard oriented discretization class of Π̂_{g,ν} to exactly one oriented
  prediscretization of π; complex conjugation gives the opposite one. The image of π_1(M_{g,ν,Q̄}) in 𝒯̂̂(π) is the
  𝒯̂^+ of any of these classes, independent of the choice (it is normal in the image of π_1(M_{g,ν})): π carries
  canonically a strict geometric Teichmüller subgroup Σ, and (26)
  [1 → π_1(M_{g,ν,Q̄}) → π_1(M_{g,ν}) → Gal(Q̄/Q) → 1] → [1 → Σ → N_Σ → Γ_Σ → 1]; complex conjugation ↦ the canonical
  involution.
- **C ("conjecture hâtive", 2:sc332, (27))** Gal(Q̄/Q) → Γ_Σ is an isomorphism ("La conjecture naturelle ici").
  **C ("encore plus hardie", (28), margin "Conjectural!!")** moreover Σ is normal in 𝒯̂̂(π) (⇔ Σ_{g,ν} normal in
  𝒯̂̂_{g,ν}), i.e. N_Σ = 𝒯̂̂ and **π_1(M_{g,ν}) ≃ 𝒯̂̂(π) = Autext_lac(π)**; Gal(Q̄/Q) = the "arithmetic" quotient of the
  group of exterior loop automorphisms of π.
  (N: for (0,3) this says Gal(Q̄/Q) ≃ the centralizer-type group in Autext_lac(F̂_2), a group containing GT; for
  (0,4), (0,5) it is the statement compared with GT in the literature; see the LM3 review.)
- Consequences he draws if (27) holds (2:sc334–339): a profinite loop group π with Σ ⇔ an algebraic closure Q̄ of Q
  (Galois group N_Σ/Σ) with a universal covering of 𝒰_{g,ν}; exterior π with Σ ⇔ a universal covering of M_{g,ν};
  an oriented prediscretization compatible with Σ ⇔ an isomorphism Q̄ ≃ Q̄_0. A curve of type (g,ν) over Q̄ with a
  universal covering ⇔ (π,Σ) plus a *germ of splitting* of 1 → Σ → N_Σ → Γ_Σ → 1; over a finite subextension K':
  a partial splitting Γ' → N_Σ. "Sûrement, si cette description ... est pleinement fidèle, elle n'est pas 2-fidèle":
  conditions on the splitting are needed. Over K of finite type with Γ = Gal(K̄/K) → Γ_0: a lift of Γ → Γ_0 ≃ N_Σ/Σ
  to an exterior action Γ → N_Σ, with conditions to be found. **Q (2:sc338–339)** a rational point (a germ of true
  action of Γ_Σ on π) should single out a *discretization* inside the given prediscretization: to define.
  **D** strict prediscretization := a discretization modulo inner automorphisms = an exterior base modulo 𝒯_{g,ν}:
  Isomext_lac(Π̂_{g,ν},π)/𝒯_{g,ν} (the datum on π_1 of a variety over K̄ ⊂ C).

### §27 Change of type (g,ν): (a) plugging holes; the "diagramme remarquable" (2:sc340–349, pp. 172–176)

- Terminology: *prediscretization* (ex "quasi"); **arithmetic Teichmüller group** Γ_Σ = N_Σ/Σ associated with
  (π,Σ); its elements = *arithmetically exterior automorphisms* of π; Σ ⊂ 𝒯̂̂(π) = a **prearithmetization** of π.
  The multiplier χ is trivial on Σ and gives χ_Σ: Γ_Σ → Ẑ^* ("cyclotomic character"); **if the fundamental
  conjecture holds, χ identifies (Γ_Σ)_ab with Ẑ^***. Σ → S_I is surjective, Σ^! its kernel ("moralement 𝒯̂^{!+}");
  N/Σ^! ≃ S_I × Γ_Σ and **N^!/Σ^! ≃ Γ_Σ**. Case (0,3): Σ^! = 1, Σ ≃ S_3, N = normalizer of S_3 in 𝒯̂̂, N^! ≃ Γ_Σ its
  centralizer, N = S_3 × N^!.
- Plugging I∖I': bases adapted to I'; 𝔖̂̂_{g,(ν,ν')} → 𝔖̂̂_{g,ν'} sends discretizations, strict prediscretizations,
  prediscretizations (oriented or not) of π to those of π'. **Q** does a prearithmetization Σ of π give one of π'?
- **Diagramme remarquable (2:sc344, p. 174)**: the tower of homogeneous spaces under 𝔖̂̂(π): Bases(π) ≃
  Isom_lac(π̂_{g,ν},π) → oriented discretizations (/𝔖^+_{g,ν}) and exterior bases (/π̂_{g,ν} = Isomext_lac) → strict
  oriented prediscretizations (/𝔖^+·π̂ = Isomext/𝒯^+) → oriented prediscretizations (/𝔖̂^+ = Isomext/𝒯̂^+) →
  prearithmetizations (/M_{g,ν} = Isomext/N_{g,ν}), with groups {±1}, 𝒯_{g,ν}, 𝒯̂_{g,ν} and Γ_Σ = Γ_{g,ν} on the
  arrows; all but the first two are homogeneous under 𝔖̂̂^! (quotients of Isom^! by 𝔖^!, 𝔖^!·π̂, 𝔖̂^!, M^!).
  **D** Γ_{g,ν} := N_{g,ν}/Σ_{g,ν} = N^!_{g,ν}/Σ^!_{g,ν} (Σ_{g,ν} = 𝒯̂^+_{g,ν}); canonically attached to any (π, α) with α
  an oriented prediscretization; the connected groupoid of pairs (π,Σ) with arithmetically exterior isomorphisms
  has automorphism group Γ_{g,ν}.
- **Lemme (margin: "pas prouvé")** N^!_Σ = Norm_{𝒯̂̂^!}(Σ^!). **C (2:sc347)** Prédiscrét^+(π) → Prédiscrét^+(π') is
  bijective; Σ_α = Σ_β ⇔ Σ_{α'} = Σ_{β'}, so Préarithm(π) ≃ Préarithm(π'); and the induced Γ_Σ → Γ_{Σ'} is an
  isomorphism. Argument for I∖I' one point i: **he admits**, "en analogie avec le cas discret", that
  𝒯̂̂(π,i) → 𝔖̂̂(π') is an isomorphism, i.e. 1 → π̂_{g,ν−1} → 𝒯̂̂_{g,(ν,ν−1)} → 𝔖̂̂_{g,ν−1} → 1 exact (the profinite analogue
  of the §18 theorem), containing the discrete and the single-hat sequences. Then 𝒯̂̂^!_{g,ν}/𝒯̂^{!+}_{g,ν} ≃
  𝔖̂̂^!_{g,ν−1}/𝔖̂^{!+}_{g,ν−1} and normalizers correspond. **Cor** Γ_{g,ν} ≃ Γ_{g,ν−1} ≃ ...: Γ_{g,ν} ≃ Γ_{g,0} (g ≥ 2),
  Γ_{1,ν} ≃ Γ_{1,1}, Γ_{0,ν} ≃ Γ_{0,3}; Σ normal in 𝒯̂̂ ⇔ Σ' normal in 𝒯̂̂'. **NB (2:sc349)** "Le fait admis est loin
  d'être évident — même que 𝒯̂̂^!_{g,(ν,ν−1)} → 𝒯̂̂_{g,ν−1} soit surjectif, ou que 𝒯̂̂_{g,(ν,ν−1)} → 𝔖̂̂_{g,ν−1} soit
  injectif, est loin d'être évident, et est peut-être tout à fait faux!"; it amounts to the existence of an inverse
  "forage des trous" functor, "qui en tout état de cause reste incompris".
  (N: this admitted fact is false as stated for the full Autext: the profinite Birman map
  Out^*(π̂_{g,ν}) fixing i → Aut(π̂_{g,ν−1}) is not surjective in general; what holds are the injectivity results and
  the GT-type statements of Nakamura, Harbater–Schneps, Hoshi–Mochizuki–Minamide; exact statements to be fixed in
  READING_BASE and in the LM3 review. The corollary Γ_{0,ν} ≃ Γ_{0,3} is to be compared with: Out^♭(π̂_{0,5}) = GT
  (Harbater–Schneps), GT ⊂ Out(π̂_{0,4}) and with Hoshi–Minamide–Mochizuki on Out of configuration space groups.)

### §28 Change of type (continued): passage to a finite covering (2:sc350–, pp. 177–)

- π profinite loop group of type (g,ν) anabelian, π' ⊂ π of finite index n: π' with the traces of the loop
  subgroups is a loop group; its loop subgroups are the L' with L' = Centr_π(L') ∩ π' and L := Centr_π(L') a loop
  subgroup of π; d(L') = [L:L']; φ: I' → I with (1) Σ_{i' over i} d(i') = n; Hurwitz (2)
  2g'−2 = n(2g−2) + Σ (d(i')−1).
- (2:sc351–363, pp. 177–183) (3) 2g'−2+card I' = n(2g−2+card I): −EP_! ≥ 1 is the anabelian condition, stable under
  coverings. Every discretization of π induces one of π' ⊂ π (oriented ones too, via the trace isomorphism T' ≃ T).
  **C (2:sc352)** for π' normal in π, G = π/π': Discrét(π) → Discrét(π') is injective, with image the π'_0 such that
  G → 𝒯̂̂(π̂'_0) factors through 𝒯(π'_0) (even 𝒯(π'_0)^+). Necessity clear; sufficiency reduces to: the extension π_0
  of G by π'_0 is a loop group with the right d_i — "comme si on savait déjà que toute extension sans torsion d'un
  groupe fini par un groupe à lacets est (de la façon canonique) un groupe à lacets" (N: this is the
  torsion-free-virtually-surface-group statement, a theorem via Nielsen realization/Eckmann–Müller–Linnell and the
  convergence group theorem; exact form for READING_BASE). **Cor** injectivity "en tous cas". **NB** not always
  bijective: conjugate G ⊂ 𝒯(π'_0) by γ ∈ 𝒯̂̂ so that it no longer stabilizes a discretization ("Un tel γ existe
  toujours").
- **C/expectations (4)–(6)**: Prédiscr^+(π) → Prédiscr^+(π') bijective, Préarith(π) → Préarith(π') bijective, and
  Γ_Σ ≃ Γ_{Σ'} canonically. Reduction to π' characteristic; conditions on the inclusions (7)
  𝔖̂^+(π_0) ⊂ M(π_0) ⊂ 𝔖̂̂(π_0) into the same for π'_0: (a) injectivity of P(π) → P(π') ("assez plausible"), (b)
  surjectivity ("beaucoup plus problématique, voire douteuse": 𝒯̂̂(π_0)~ = Norm_{𝒯̂̂(π'_0)}(G) may be much smaller than
  𝒯̂̂(π'_0)), (c) M(π_0) → M(π'_0) (needed to define A(π) → A(π') and Γ_Σ → Γ_{Σ'}; "pas anodine du tout"), (d), (e).
  Test cases he names: π' of index 2; the kernel of π → (π_ab)_2 for π = Π̂_{0,3}: "situation de la courbe de Fermat
  x^2+y^2+z^2 = 0 (revêtement octaédral de P^1∖{0,1,∞})".
- **D (2:sc364–366)** *correspondences* between loop groups π, π': (π'', p: π'' → π, q: π'' → π') with p, q composites
  of hole-pluggings and isomorphisms onto finite-index subgroups; *arithmetic correspondences* (with Σ'' = p^*Σ =
  q^*Σ'); they induce *arithmetically exterior isomorphisms* (P_Σ, Γ_Σ) ≃ (P_{Σ'}, Γ_{Σ'}); the connected groupoid of
  "courbes arithmétiques extérieures", with automorphism group Γ_0 of the reference object; equivalent to the
  category of Γ_0-torsors.

### §29 Critique of the preceding approach (2:sc367–378, pp. 186–191)

- "L'approche des § précédents semble franchement très brutale." Doubts on the hole-plugging conjecture: the
  canonical (1) 𝒯̂̂(π)_i → 𝔖̂̂(π') (stabilizer of i) "il est problématique si c'est un isomorphisme — et même si c'est
  injectif, ou si c'est surjectif". What holds: for a discretization π_0, 𝒯(π_0)_i ≃ 𝔖(π'_0), 𝒯̂(π_0)_i ≃ 𝔖̂(π'_0), so
  (4) 1 → π̂'_0 → 𝒯̂(π_0)_i → 𝒯̂(π'_0) → 1 and an injection (5) i_{π_0}: π' → 𝒯̂̂(π)_i depending on π_0:
  i_{u(π_0)} = int(u)∘i_{π_0}∘u_{π'}^{-1}; independence ⇔ its image is normal in 𝒯̂̂(π)_i. **D** H_{π_0,i} := elements
  of 𝒯̂̂(π)_i normalizing i_{π_0}(π') and acting on it through (1); H_{π_0} := elements of 𝒯̂̂(π) permuting the i_{π_0,i};
  H ⊃ 𝒯̂(π_0). **Key remark (2:sc369)**: the image of π_1(M_{g,ν}) in 𝒯̂̂ must not only normalize 𝒯̂^+ but lie in H.
  "Il est possible que 𝒯̂̂(π_0) soit un groupe à tel point démesuré et pathologique, qu'il ne pourra jamais être
  question d'en dire des choses raisonnables"; one should work with smaller subgroups "qui restent proches du
  discret". In 𝒯̂(π_0) (ν ≠ 0) there is a "structure simpliciale d'extensions successives" respected by Galois: part
  of the "structure à l'infini" of π_1 of the modular multiplicities M_{g,ν} (N: the first appearance of the
  Teichmüller-tower/stratification-at-infinity idea of the Esquisse).
- **New definitions (2:sc371–377)** (replacing the normalizer definitions): from the transcendental construction,
  π_1(𝒰_{g,ν,Q}) with its three-step filtration (π̂_{g,ν}; 𝒯̂^+; Γ_Q) maps ("on présume injectivement") to 𝔖̂̂_{g,ν};
  **M_{g,ν} := its image**, 𝔖̂_{g,ν} ⊂ M_{g,ν} ⊂ 𝔖̂̂_{g,ν}; **N_{g,ν} := M_{g,ν}/π̂**, 𝒯̂_{g,ν} ⊂ N_{g,ν} ⊂ 𝒯̂̂_{g,ν}, with 𝒯̂^+
  normal in N; **Γ_{g,ν} := N_{g,ν}/𝒯̂^+_{g,ν}** (12), with canonical element τ_{g,ν} of order 2; Γ_Q ↠ Γ_{g,ν} (13)
  "dont on présume qu'il est bijectif". For (π, α) (α a prediscretization): M_α, N_α, Γ_α, τ_α by transport.
  **D** *arithmetization* of π: an element of A(π) := Isom_lac(π̂_{g,ν},π)/M_{g,ν} = Isomext_lac/N_{g,ν} (20);
  P(π) := oriented prediscretizations (21); A(π) = P(π)/Γ_{g,ν} (22): P_a is a Γ_{g,ν}-torsor; M_a, N_a, 𝒯̂^+_a
  (independent of α ∈ P_a), Γ_a := N_a/𝒯̂^+_a = Γ_{g,ν} twisted by P_a.
  Three connected groupoids with origin (π̂_{g,ν}, a_{g,ν}): exterior arithmetized loop groups (automorphism group
  N_{g,ν} ≃ π_1(M_{g,ν,Q}) if Γ_Q → Γ_{g,ν} is injective; objects = universal coverings of M_{g,ν,Q}); arithmetized
  loop groups (M_{g,ν} ≃ π_1(𝒰_{g,ν,Q}); objects = universal coverings of 𝒰_{g,ν,Q}); arithmetized loop groups with
  arithmetically exterior isomorphisms (Γ_{g,ν}; conjecturally = algebraic closures of Q).
  **P/C (29),(30)** P_a → {elements of order 2 of Γ_a}, α ↦ τ_α, τ_α = τ_{−α}; if Γ_Q ≃ Γ_{g,ν}: a bijection
  P_a/±1 ≃ {elements of order 2 of Γ_a} (uses: the only elements of order 2 of Γ_Q are the conjugates of τ, and
  Centr(τ) = {1,τ}); an unoriented prediscretization over a = an archimedean valuation of Q̄.

### §30 Properties of the N_{g,ν}, Γ_{g,ν}: (a) properties tied to finite subgroups (2:sc379–391, pp. 192–198)

- Aim: properties, suggested by geometry, formulated purely algebraically, "assez fortes peut-être pour finir par
  caractériser les N_{g,ν}". A curve of type (g,ν) over Q̄ ⇔ a germ of lifting of N_a → Γ_a (kernel 𝒯̂^+_a), over a
  finite K' a lifting on an open Γ'; only *admissible* liftings (special properties, some "du genre Weil").
  For a closed Γ ⊂ M_a with (a) Γ → Γ_a injective with open image: wanted (b) π^{Γ'} = 1 for open Γ' ⊂ Γ (rigidity
  of the category of points); (c) Z := (𝒯̂^+_a)^{Γ^♮} = Centr_{N_a}(Γ̃^♮) ∩ 𝒯̂^+_a is finite (= Aut of the curve over Q̄),
  and conjugate in M_a to a subgroup of some 𝒯(π_0)^+.
- For a finite G ⊂ 𝒯̂^+_a contained in some 𝒯^+(π_0) and realizable: there is an admissible germ Γ_a → N_a
  centralizing G; Centr_{N_a}(G) → Γ_a has kernel 𝒯̂_a^{+G}, not finite in general (the fixed locus of G in
  Teichmüller space has positive dimension unless U/G has genus 0 ...). **(d)** for every finite G ⊂ 𝒯̂^+_a (at least
  G ⊂ 𝒯^+): N_a ∩ Z(G) → Γ_a has open image (Z(G) the centralizer in 𝒯̂̂). Consequence: Γ_{g,ν} ∩ Z'_{g,ν} is open in
  Γ_{g,ν}, Z'_{g,ν} the intersection of the images of the centralizers of the finitely many classes of finite
  subgroups of 𝒯(π_{g,ν}). For finite (cyclic) G ⊂ 𝔖(π_0) (action with a fixed point): π^G = 1 (known discretely,
  admitted profinitely), 𝔖̂̂^G → 𝒯̂̂^G injective. He corrects himself: 𝔖(π_0)^G → 𝒯(π_0)^G is not surjective
  (automorphisms commuting with G only permute the fixed points); only the stabilizer of the point lifts.

### §31 Liftings of an exterior action of a finite group on a profinite loop group (2:sc391–394, pp. 198–199)

- G = G^+ ⊂ 𝒯̂̂(π) finite, with an invariant discretization π_0 (G ⊂ 𝒯(π_0)). Discrete case understood: the finite
  groupoid [U^!] with strict G-action whose points are the π_0-classes of maximal partial sections; u̇ ∈ 𝒯(π_0)^G
  lifts to 𝔖(π_0)^G iff u̇(P) = P. **Q/C (2:sc393)**: (a) is {π_0-classes of splittings of 1 → π_0 → E → G → 1} →
  {π̂_0-classes of splittings of 1 → π̂_0 → Ê → G → 1} bijective? (b) is π^G = 1 for G ≠ 1? "J'ai envie de conjecturer
  sans vergogne qu'il en est ainsi". (N: this is a torsion/conjugacy-separability ("goodness"-type) question for
  virtually surface groups: finite subgroups of the profinite completion of a Fuchsian group are conjugate to
  finite subgroups of the discrete group; to cite exactly — it is known for good/virtually free and Fuchsian
  groups; LM4.)

### §32 Arithmetic aspects of hole plugging: Γ_{g,ν} versus Γ_{g,ν−1}; curves as "potential curves" (2:sc395–436, pp. 200–220)

- (1)–(4) N_{g,ν} = N^!_{g,ν}·𝒯̂^+_{g,ν}, N^!/𝒯̂^{!+} ≃ Γ_{g,ν}. For each i (with (g,ν−1) anabelian, 2g+ν ≥ 4): the
  injective (5) φ_i: π'_i → 𝒯̂^{+!} ⊂ N^! ⊂ 𝒯̂̂_i. **(e)** ("il est vrai que") N^!_{g,ν} normalizes the images of the
  π'_i ↪ 𝒯̂^{!+}_{g,ν} (0 ≤ i ≤ ν−1). **(f)** ψ_i: 𝒯̂̂^!_{g,ν} → 𝔖̂̂^!_{g,ν−1} induces an *isomorphism* (6)
  N^!_{g,ν} ≃ M^!_{g,ν−1}: the map exists and is surjective by the arithmetic-geometric definition, since (8)
  Θ_{g,ν}: Γ_Q ↠ Γ_{g,ν} and Θ_{g,ν−1} are compatible; bijectivity ⇔ Θ_{g,ν} and Θ_{g,ν−1} have the same kernel.
  "Il ne serait pas impossible que (f) soit faux, i.e. que les Θ_{g,ν} soient infidèles, mais de moins en moins
  quand on fait augmenter ν", with (perhaps) only the limit Θ_{g,∞} faithful. He works with (f): the *fundamental
  exact sequences* (9) 1 → π̂_{g,ν−1} → N^!_{g,ν} → N^!_{g,ν−1} → 1 [M/N as in his text], extending (10)
  1 → π̂_{g,ν−1} → 𝒯̂^!_{g,ν} → 𝒯̂^!_{g,ν−1} → 1, "et tient lieu de la suite exacte peut-être défaillante"
  1 → π̂_{g,ν−1} → 𝒯̂̂^!_{g,ν} → 𝒯̂̂^!_{g,ν−1} → 1 (marked ??). For (π,a): arithmetizations a'_i on the π'_i, (11)
  1 → π'_i → (N_a)_i → N_{a'_i} → 1, Γ_a ≃ Γ_{a'_i} (13), P_a ≃ P_{a'_i} (14). No claim on a bijection of the sets of
  arithmetizations. **P** hole plugging = an equivalence {exterior arithmetized profinite loop groups of type (g,ν)}
  ≃ {arithmetized (non-exterior) loop groups of type (g,ν−1)}.
  (N: with the arithmetic definition, (f) is exactly: the kernel of the outer Galois action on π̂_1 of M_{g,ν}-type
  objects is independent of ν; this is known: the kernels of Γ_Q → Out(π̂_1(M_{g,n})) are all trivial by Belyi for
  genus 0 and by Matsumoto/Hoshi–Mochizuki in general; injectivity statements to cite.)
- **Q (15)** describe Γ_{g,ν} inside Γ'_{g,ν} := Norm_{𝒯̂̂}(𝒯̂^+)/𝒯̂^+ via its exterior action on 𝒯̂^+_{g,ν} or 𝒯̂^{+!}_{g,ν}:
  conditions of type (e) (normalizing the π'_i), stable under descent in ν; empty in the limit cases (g,0),
  (1,1), (0,3); "il est possible qu'il faille faire intervenir des propriétés des π_1 des M_{g,ν,Q̄} liées à la
  compactification". Only for (0,3) no such condition is to be expected.
- **D** *potential algebraic curve*: (π, a) with an admissible germ of lifting (16) Γ_a^♮ → N_a; relative to a
  Γ_{g,ν}-torsor P (an algebraic closure of Q). *Points* of π: π-conjugacy classes of admissible liftings (19)
  Γ^♮ → M_a, i.e. germs of true actions with (20) π^{Γ^♮} = 1. **Question liminaire / (g)** ("facultatif"): does
  (π, Σ_a, Γ') determine the arithmetization? ⇔ for every open N' ⊂ N_{g,ν}, the elements of 𝒯̂̂_{g,ν} normalizing
  𝒯̂_{g,ν} and carrying N' into N_{g,ν} lie in N_{g,ν}.
- Plugging I' ⊂ I stable under Γ: Γ ↪ N_{a'} (23); for i' ∈ I' fixed by Γ a canonical Γ → π'(i') lifting the
  exterior action, hence (25) I' → Pts(π',a',Γ). **P ("Je dis que", 2:sc410)** this map is injective — evident
  geometrically; internal reason wanted.
- **Axiomatics (2:sc411–421)**: given, for fixed g, closed subgroups N_{g,ν} ⊂ 𝒯̂̂_{g,ν} normalizing 𝒯̂_{g,ν} with
  M_{g,ν} ≃ ... ≃ M_{g,ν−1} via the ψ_i [(g): (𝔖̂̂_{g,ν})_i → 𝔖̂̂_{g,ν−1} sends (M_{g,ν})_i into M_{g,ν−1}], and a notion
  of *admissible* exterior action of profinite groups Γ on arithmetized π, he asks: (1) stability under open
  subgroups; (2) stability under plugging a Γ-stable I'; a true action is admissible iff the exterior action
  obtained by drilling is; (3) admissible true action ⇒ π^Γ = 1 (rigidity of the Γ-points of B_{π,Γ}); (4) an
  admissible exterior action lifts to an admissible true action on an open subgroup (Pt_ad ≠ ∅); (5) for i fixed by
  Γ, (27) Pt_ad(B_{π,Γ}) → Pt_ad(B_{π'_i,Γ}) is a bijection onto the complement of the canonical point P [a), b),
  c)]; (6) extension of an action from an open Γ' to Γ: existence and uniqueness (uniqueness from L^{Γ'} = 1).
  Consequence: the equivalence (30) {(π,a,I',Γ,θ): Γ fixing each point of I'} ≃ {(π',a',Γ,θ', I' ⊂ Pt_ad(B_{π',Γ})^Γ)}:
  "forage de trous en I'".
- General frame (2:sc422–429): a set X of "points" with groupoids Π_{U_I} for finite I ⊂ X, functorial with strict
  transitivity, loop structures, hole-plugging compatibility, a group Γ acting strictly with all stabilizers Γ_P ≠ 1
  of finite index; wanted: reconstruct X and the Π_{U_I} from the "soft" exterior action of Γ on π = π(∅):
  2°) U_I → Pt(B_{π(I),Γ^♮}) (germs of splittings of the extension E(I) of Γ by π(I)) injective, and with a notion of
  admissible lifting U_I ≃ Pt_ad(B_{π(I)},Γ^♮).
- **"Conjecture provisoire profinie" (2:sc431–433; margin: "Canulé, cf plus bas")**: an exterior action of a
  profinite Γ on an arithmetized anabelian (π,a) is *admissible* if (a) Γ → Γ_a has open image; (b) the effective
  actions deduced by hole plugging normalize no loop subgroup; (c) there are infinitely many π-classes of germs of
  splittings normalizing no loop subgroup (margin: (c) excludes Γ = N_{g,ν} for (g,ν) ≠ (0,3): 𝒰_{g,ν} → M_{g,ν}
  has presumably no étale multisections). An effective action is admissible if the exterior one is and it normalizes
  no loop subgroup. Then: (a) π^Γ = 1 (perhaps even π^{Γ^+} = 1, Γ^+ = Ker χ); (b), (c) no loop subgroup normalized
  after plugging; (d) Pt_ad(B_{π,Γ^♮}) → Pt_ad(B_{π',Γ^♮}) injective with image the complement of {P}.
  **He retracts the surjectivity part (2:sc433–435)**: for Γ = π_1(S), S a parameter scheme of finite type over Q,
  an admissible action = a family of curves over S; two distinct sections need not be disjoint, so surjectivity
  fails. One needs "sections strictement distinctes": proceed by induction on the dimension of S ("se tirer par les
  lacets de souliers"), starting in dimension 0 with *arithmetically faithful* actions (Γ → Γ_a injective), where
  the conjecture "semble raisonnable". "Le test décisif ... serait la possibilité d'obtenir les courbes ainsi
  définies comme des revêtements de P^1∖{0,1,∞}".
  (N: the points-as-sections statements here are the section conjecture for hyperbolic curves over number fields
  with the cuspidal sections removed ("normalize no loop subgroup"), plus its relative version over a base S; the
  remark on non-disjoint sections is the correct obstruction. This is LM6 territory. The claim (5)(c) is the
  section conjecture for the affine curve in terms of the one for the plugged curve.)

### §33 Topological digression: anti-involutions of compact oriented surfaces (2:sc437–, pp. 221–)

- *Algebroid surface*: U = X∖S, X compact orientable, S finite; X = Û the "pure compactification". (U,σ) with σ an
  anti-involution ⇔ (Y,T), Y = Û/σ a compact surface with boundary, T finite; inverse: the oriented double.
  Case ν = 0: χ(Y) = 1 − (γ+μ) for Y non-orientable of genus γ with μ boundary circles; χ(X) = 2χ(Y): g = γ+μ.
  **Proposition/Corollaire as first stated** ((X,σ) of genus g ↔ non-orientable (γ,μ) with γ+μ = g; exactly g+1
  classes, by μ = card π_0(X^σ)) **are corrected in the margins**: this covers only the (X,σ) with X/σ
  non-orientable; there are also the doubles of orientable Y of type (γ,μ), μ ≥ 1, with g = 2γ+μ−1.
  (N: the correct count of conjugacy classes of orientation-reversing involutions of a closed genus g surface is
  ⌊(3g+4)/2⌋ (Weichold/Klein: species (μ, separating or not)); to check in LM4.)
  **Admitted Lemma (2:sc440)**: every anti-involution of the disc (or of C) is conjugate to z ↦ z̄; so its fixed set
  is ≃ R, connected. **Théorème (begins 2:sc440)**: U oriented surface not S^2, σ an anti-involution, E the extension
  of Z/2 by π ...
- **P (Théorème, 2:sc440–445, pp. 222–225)** U an oriented connected paracompact surface not S^2, σ an
  anti-involution, E the extension of Z/2 by π = π_1(U). (a) U^σ is a closed 1-dimensional submanifold; (b) the
  map (5) U^σ → Sc(E, Z/2) (π-classes of splittings = elements of order 2 of E outside π) factors through a
  *bijection* (6) π_0(U^σ) ≃ Sc(E, Z/2); (c) for a component Z_i with element σ_i: π^{σ_i} = 1 iff Z_i ≃ R; (d) if
  Z_i ≃ S^1 with class g_i ∈ π: φ_i: Z → π, n ↦ g_i^n, is injective and π^{σ_i} = Im φ_i (14). Proof from the
  admitted lemma (Ũ^{σ'} non-empty and connected).
- **Cor 1 (2:sc445–447)** for σ_i ∈ 𝒯_g an anti-involution class of X_g with card π_0(X_g^{σ_i}) = i (margin: and
  X_g/σ non-orientable): (a) exactly i Π_g-conjugacy classes of effective order-2 automorphisms of Π_g in the class
  σ_i (so σ_i, σ_j are not conjugate for i ≠ j); (b) Π_g^{u_i} ≃ Z; (c) two such u_i, u'_i are conjugate by some
  h ∈ 𝔖_g^+ (transitivity of Aut(Y) on π_0(∂Y)). **Cor 2** (16): 1 → T → 𝔖_g^{+u_i} → 𝒯_g^{+σ_i}, image of index i.
- Explicit model (2:sc449–471, pp. 227–238): X_g = (sphere X_0 with antipodal τ, minus 2g discs in τ-pairs) ∪ g
  cylinders T_j = S_j × I; on each T_j two anti-involutions τ̇_j(z,t) = (−z e^{πit}, −t) (fixed-point free) and
  τ̇'_j(z,t) = (z, −t) (fixed circle) (27); τ_{I'} for I' ⊂ I: X_g^{τ_{I'}} = ∪_{j∈I'} S_j × {0} (26);
  ρ_j := τ̇'_jτ̇_j: (z,t) ↦ (−z e^{πit}, t), the identity on ∂T_j (N: a Dehn twist of T_j up to the half-turn
  convention; he says ρ_j generates SΓ^{!+}(T_j) ≃ Z); H := ⟨ρ_j⟩ ≃ Z^I, G := ⟨τ_{I'}⟩ = H ⋊ {1,τ} with
  τρτ^{-1} = ρ^{-1} (42): every element of τH is an anti-involution; index of τ∏ρ_j^{n_j} = number of odd n_j (46);
  τρ', τρ'' are H-conjugate iff ρ'ρ''^{-1} ∈ H^2. Symmetric placement: the discs at the 2g-th roots of unity on the
  equator; D_{2g} and D̃_{2g} = D_{2g} × Z/2 act and normalize G: (49)–(51) D̃_{2g}·H ⊃ G acts on X_g; generators
  ε_0, ε_1, τ, τ' with relations (52). **Programme/Q (2:sc467–470)**: (1) compute the exterior action of this group
  on π_g; (2) add "lanières" L, L' (a one-holed torus, then a two-holed torus) and their special Teichmüller groups
  (≈ an extension of SL(2,Z) by Z, "qui rappelle celle de SL(2,R) par Z"); write the relation of π_g in the
  "panachée" disposition; H ≃ Z^g in 𝒯_g "suggère beaucoup la situation d'un tore maximal dans un groupe
  semi-simple": **Q** intrinsic characterization (maximal free abelian subgroups?), its normalizer (= what comes from
  automorphisms of V_0?), do the SL(2,Z)_j play the role of rank-one subgroups? (N: maximal abelian subgroups of the
  mapping class group have rank 3g−3 (Birman–Lubotzky–McCarthy), so H ≃ Z^g is not maximal for g ≥ 2; to put in
  LM4 as a decided item.)

### Second §33 Finite coverings: relations between the N_{g,ν}, Γ_{g,ν} for variable g (2:sc472–482, pp. 239–244)

- For π' open in an arithmetized (π,a): wanted (1) 𝔖̂̂(π_0) → 𝔖̂̂(π'_0) sends M(π_0) into M(π'_0) (so arithmetizations
  and prediscretizations of π induce those of π'), injectivity (2), and **(2)** Γ_a → Γ_{a'} (3) bijective
  (surjective by construction through Γ_Q); P_a ≃ P_{a'}. Via arithmetic correspondences: a connected groupoid whose
  exterior π_1 is the common value of the Γ_{g,ν}; Γ_{0,3} ≃ Γ_{g,ν̃} through a realization of π_{g,ν̃} as a
  finite-index subgroup of π_{0,3}.
- **What is independent of conjecture (2:sc475–478)**: IF for π' characteristic in π one has
  𝒯̂̂(π'_0) ∩ 𝔖̂^+(π_0) = 𝔖̂^+(π_0) ("un énoncé de nature relativement anodin sur des groupes à lacets profinis"), then
  Γ_{π_0} → Γ_{π'_0} is bijective, the kernel of Γ_Q → Γ_{0,3} acts trivially in every Γ_{g,ν}, and Γ_{0,3} → Γ_{g,ν} is
  an isomorphism for ν large enough (whenever a surface of type (g,ν') with ν' ≤ ν is an étale covering of X_{0,3});
  in particular Γ_{0,ν} → Γ_{0,3} bijective; nothing for Γ_{g,0}, Γ_{1,1}. **P (unconditional, 2:sc477–478)** for a
  curve U over a number field K, after enlarging K and removing points so that U' is an étale covering of
  (U_{0,3})_K: the kernel Θ' of Γ' → Γ_{0,3} acts on π' ⊂ π̂_{0,3} through a finite group of exterior automorphisms;
  hence the kernels of Γ_{0,ν} → Γ_{0,3} are *finite*; Θ' acts through a finite quotient on every ∏ T_ℓ(A).
  "Il devient très difficile de s'imaginer comment il pourrait se faire que Θ' n'opère pas, en fait,
  trivialement! J'ai même l'impression que je peux montrer grâce au résultat du russe que m'a signalé Deligne, que
  Γ_Q → Γ_{0,3} est iso!" (→ §35). Then the essential question: "caractériser Γ_{0,3} algébriquement, ainsi que les
  N_{g,ν} — et donner une description algébrique également des scindages admissibles".
- (2:sc480–482) Admissible effective actions of Γ'' ⊂ Γ_{0,3} on π̂_{0,3}: conjecturally exactly the lifts that
  normalize no loop subgroup, or with π̂_{0,3}^{Γ''+} = 1 ("il est concevable qu'il faille y apporter des conditions
  plus subtiles, faisant intervenir les Frobenius"). **Constructive definition via U_{0,3}**: an exterior action of
  Γ' on (π,a) is admissible iff it is obtained from an open π' ⊂ π̂_{0,3} stable under an admissible effective action
  of an open Γ'' ⊂ Γ_{0,3}, by plugging holes. **D** N_{g,ν} in terms of Γ_{0,3}: for ν large, embed π_{g,ν} in π_{0,3}
  compatibly with exterior actions of Γ_{0,3}; then N_{g,ν} = the subgroup of 𝒯̂̂_{g,ν} generated by 𝒯̂_{g,ν} and
  Γ_{0,3}.

### §34 Heuristic profinite description of the category of algebraic curves over finite subextensions of Q̄_0/Q (2:sc483–490, pp. 245–248)

- A geometrically connected anabelian curve U over K ⊂ Q̄_0 ⇔ (1) 1 → π → E → Γ^+ → 1 with Γ^+ ⊂ Γ_Q ≃ Γ_{0,3} open.
  **C (2:sc483)** the loop structure need not be given: it is the only loop structure invariant under the exterior
  action of Γ^+; the loop subgroups L_i are the maximal subgroups of π such that Norm_E(L_i) → Γ^+ has open image
  (and every subgroup ≠ 1 with this property lies in a unique L_i). **C** every homomorphism of such extensions
  E → E' (from curves U, U') with open image respects the loop structures and comes from a unique morphism of
  curves: the functor {curves over K, dominant morphisms} → {profinite exterior groups with Γ-action} is fully
  faithful. (N: this is the Hom-form of the anabelian conjecture for hyperbolic curves over number fields: Tamagawa
  (affine, isomorphisms), Mochizuki (Hom-form, sub-p-adic fields); to cite exactly.) The essential image is known
  without conjecture: open subgroups E' ⊂ E_{0,3}, plug holes in a Γ-stable set (Belyi).
- "Cela ne signifie pas pour autant" that all classes of admissible liftings come from K-rational points; it does
  as soon as full faithfulness for isomorphisms is admitted. **NB** even for the automorphisms of U_{0,3}: "Il
  faudrait prouver que le commutant de Γ_{0,3} dans 𝒯̂̂_{0,3} est réduit à S_3" (N: known: the centralizer of the Galois
  image in Out(π̂_1(P^1∖{0,1,∞})) is S_3 — follows from the Isom-form (Tamagawa/Mochizuki) for P^1∖{0,1,∞} over Q; to
  cite). With arithmetizations it is easier: N_{0,3} ≃ S_3 × Γ_{0,3} and centre(Γ_Q) = 1.
- **Q** a simpler direct description of admissible exterior actions: for g ≥ 1: after plugging all holes the
  Γ^♮-points coming from the holes are distinct; for g = 0, ν > 3: fix I' of 3 holes, plug the rest, the points
  distinct; no condition in the limit cases (g,0), (1,1), (0,3) ("C'est peut-être très brutal"). He prefers the
  constructive form via U_{0,3} and returns to germs of splittings of 1 → 𝒯̂_{g,ν} → N_{g,ν} → Γ_{g,ν} → 1 as algebraic
  points of the modular multiplicity M_{g,ν,Q}.
- **P/C (2:sc489–490)** for an admissible effective action of Γ^♮ on π: a canonical *oriented discretization*
  π_0 ⊂ π (a "réseau"), independent of choices, all in one strict oriented prediscretization; for two points x, y
  the path classes sending π_0(x) to π_0(y) form a connected loop sub-groupoid of Π_1(π,Γ^♮), on which Γ does not
  act. (N: the "integral/Betti lattice at a rational base point" inside the profinite π_1.)

### §35 Injectivity of Γ_Q → Autext_lac(Π̂_{0,3}) (2:sc491–505, pp. 249–256)

- **P (Théorème 1; margin: "démontré modulo le lemme 2")** Θ: Γ = Gal(Q̄_0/Q) → 𝒯̂̂_{0,3} = Autext_lac(Π̂_{0,3}) is
  injective. Proof: K := Ker Θ. Lemme 1: for x ∈ U_{0,3}(Q), K acts trivially on π_1(U_{0,3,Q̄}, x) ≃ Π̂_{0,3}
  (effective action): by "le résultat de Белый" there is a morphism P^1_Q → P^1_Q defined over Q, étale over
  U_{0,3}, with x ↦ 0; K acts through a finite group on π' = π_1 of the covering (normalizer argument), hence on
  π_1(V̄), V = U_{0,3}∖{x}; finite-order inner automorphisms are trivial by Lemme 2. Lemme 3: K acts trivially on the
  exterior π_1(V̄) for every non-empty open V ⊂ P^1_Q. Lemme 4: K acts trivially on the conjugacy classes of loop
  subgroups, i.e. on P^1(Q̄_0): K = 1.
- **Lemme 2 = Théorème 2** π free profinite on a finite set of ≥ 2 elements: (a) centre trivial; (b) no torsion.
  "Finalement je cale sur a) — tout comme je ne vois pas pourquoi le centre de Γ (et de tout sous-groupe ouvert)
  doit être réduit à (1). Consulter Deligne". (b) proved: π lifts into Gal(L̄/L), L = K(x), torsion-free by
  Artin–Schreier (−1 is a square). (N: (a) is standard: free profinite groups of rank ≥ 2 have trivial centre;
  cite Ribes–Zalesskii or Fried–Jarden.)
- **Cor 1** for X a curve over a number field k: there is a non-empty open V ⊂ X with Gal(k̄/k) → Out π_1(V_k̄)
  faithful ("Je présume" faithful for anabelian U itself). **Cor 2** if Γ acts faithfully on π_1(U_k̄), then also on
  π_1(V_k̄) for every geometrically connected étale covering V. Uses **Lemme 5** (margin: proved only modulo (2),
  (4)): an automorphism of a profinite loop group π that stabilizes an open π' and is inner (resp. the identity) on
  π' is inner (resp. the identity); needs (2) L_i = Centr_π(L_i^n) and (4) Centr_π(Λ_i^n) = Λ_i for the procyclic
  subgroups generated by the base elements ("pas prouvé!").
- **Remarque (2:sc502–505)** the strongest faithfulness: Γ → N(π)/𝒯̂^+(π) = Γ_π injective (then an isomorphism) for V
  anabelian over a number field. Known "à présent (modulo peu de chose)" exactly for the types (0,ν), ν ≥ 3; not
  for (g,0), nor any (g,ν) with g ≥ 1, ν ∈ {0,1,2}; "Le premier cas bien intéressant serait donc le cas (1,1)": is
  the arithmetic action of Γ_Q on Π̂_{1,1} (exterior modulo 𝒯̂^+_{1,1} ≃ SL(2,Z)^) faithful?
  (N: faithfulness of Gal(k̄/k) → Out π_1 for every hyperbolic curve: Matsumoto (affine), Hoshi–Mochizuki (proper);
  his finer question, injectivity of Γ_Q → Out(π̂_{g,ν})/(image of 𝒯̂^+) = Γ_{g,ν}, i.e. that no Galois element acts
  like a geometric mapping class, is the injectivity of Γ_Q → Out(π̂_1(M_{g,ν,Q̄}))-type statements; to match with
  the literature on Out(Γ̂_{g,n}) (Oda's problem, Matsumoto, Nakamura, Takao; Hoshi–Minamide–Mochizuki).)

### §36 The isomorphism Γ_Q ≃ Γ_{1,1} and injectivity of Γ_Q → Autext(SL(2,Z)^) (2:sc506–532, pp. 257–271)

- Π'_{0,3} := Π_{0,3}/⟨l_1^2, l_∞^3⟩, the "oriented cartographic group for triangulated structures". **P
  (Proposition)** the exterior action of Γ_Q on Π̂'_{0,3} is faithful: via U_{0,3} → U_{0,3}/S_3 ≃ P^1 with signature
  2{1}+3{∞}: 1 → Π̂_{0,3} → Π̂'_{0,3} → S_3 → 1 (9bis), Galois-compatible; the kernel acts on Π̂_{0,3} through a finite
  group, so it is finite, so ⊂ {1,τ}, and χ(τ) = −1.
- 𝒯_{1,1} ≃ GL(2,Z) (10), 𝒯^+_{1,1} ≃ SL(2,Z), centre ±1; elements u_4, u_6 with u_4^2 = u_6^3 = −1. The Legendre
  family y^2 = x(x−1)(x−λ) gives (39) M^!_{0,4} = U_{0,3} → M_{1,1} and the homomorphism of extensions (40)
  [1 → Π̂_{0,3} = 𝒯̂^{!+}_{0,4} → E_{0,3} = N^!_{0,4} → Γ → 1] → [1 → 𝒯̂^+_{1,1} = SL(2,Z)^ → E_{1,1} = N_{1,1} → Γ → 1];
  discretely (42) Π_{0,3} ↪ Γ(2) = Ker(SL(2,Z) → SL(2,Z/2)), Γ(2) = Π_{0,3} × {±1} in exactly four ways (the four
  lifts; their intersection is the level 4 subgroup, = the commutator subgroup of Π_{0,3}: margin "c'est vrai").
  Discussion of the obstruction classes α ∈ H^2(E_{0,3}, Z/2), β ∈ H^2(U_{0,3}, Z/2) (2:sc525–527), settled by the
  explicit Legendre curve.
- **P (Théorème, 2:sc530)** the natural exterior action of Γ_Q on 𝒯̂^+_{1,1}, and even on 𝒯̂^{+'}_{1,1} = 𝒯̂^+_{1,1}/±1,
  is faithful (uses Π̂_{0,3} ↪ 𝒯̂'^+_{1,1} Galois-compatibly). **Cor (43)** the canonical surjections
  Γ_Q → Γ_{1,ν} (ν ≥ 1) are injective, hence isomorphisms.
  (N: with the §29 definition of Γ_{1,1} = N_{1,1}/𝒯̂^+_{1,1}, N_{1,1} the image of π_1(M_{1,1,Q}) in Out(Π̂_{1,1}), the
  corollary needs the map Γ_{1,1} → Autext(𝒯̂^+_{1,1}) to be well defined on the quotient, i.e. conjugation action of
  N_{1,1} on its normal subgroup 𝒯̂^+_{1,1}: fine; and injectivity of the composite Γ_Q → Out(SL(2,Z)^): this is the
  statement that Gal(Q̄/Q) acts faithfully on the geometric π_1 of M_{1,1} — true by his argument given Belyi and
  centre-freeness of F̂_2. A point to check: 𝒯̂^+_{1,1} := profinite completion of SL(2,Z) is assumed to embed in
  Out(Π̂_{1,1}); injectivity of SL(2,Z)^ → Out(F̂_2) is the congruence subgroup property for Aut(F_2), true by Asada
  2001 / Bux–Ershov–Rapinchuk 2011; to cite.)

### §37 Moduli of elliptic curves via Legendre (level 2 rigidification) (2:sc533–575, pp. 272–292)

- **P (Proposition, 2:sc533–535)** X a paracompact surface, G discrete acting properly, stabilizers faithful and
  orientation preserving near each point; Y = X/G with signature d on Y^!: (a), (b) Rev(X,G) ≃ Rev_d(Y)
  (ramified coverings subordinate to d; quasi-inverse by normalization of X ×_Y Y'); (2)
  Π_1(X,G;x) ≃ Π_1((Y,d),y); (3) 1 → Π_1(X,x) → Π_1((Y,d),y) → G → 1. Variant with 𝒢 ⊃ G normal:
  Π_1(X,𝒢) ≃ Π_1((Y,d),𝒢/G); application 𝔖_{0,3} ≃ 𝒯'_{1,1} (≃ GL(2,Z)/±1), extension of 𝒯_{0,3} = S_3 × Z/2 by Π_{0,3}.
  Example: U_{0,3}(C) with S_3: (7) 1 → Π_{0,3} → Π'_{0,3} → S_3 → 1; arithmetic version (8) with
  E_{0,3} = N^!_{0,4}, Γ_{0,4} = Γ_Q.
- M_{1,1}[n] (Jacobi level n; a scheme iff n ≥ 3; Γ_n = GL(2,Z/n)), M_{1,1} ≃ (M_{1,1}[n], Γ_n) over Z[1/n] (9);
  M_{1,1}[n] → μ_n^* with geometrically connected fibres in char 0 (11); coarse M̃_{1,1} ≃ E^1_Z (affine line);
  M'_{1,1} := (M_{1,1}[n], Γ'_n = Γ_n/±1) (17) (curves "modulo symmetry"); M_{1,1}[2]' := M_{1,1}[2m]/Γ'_{2m,2}, a
  scheme, with M_{1,1}[2] a Z/2-gerbe over it. **(25)** M_{1,1}[2]' ≃ M^!_{0,4} ≃ U_{0,3} over Z[1/2], S_3-equivariant
  via int(σ_1) (40) (the two S_3 ⊂ S_4 acting on M^!_{0,4}: **P** the Klein four-group V(I) acts trivially on M^!_{0,I},
  so S_4 acts through S_3 = S_Ĩ, Ĩ the three (2,2)-partitions).
- **P (2:sc557–560)** π_1(M_{1,1}) is a central extension of π_1(M'_{1,1}) by {±1}; (47) the diagram
  [1 → SL(2,Z)^ → π_1(M_{1,1}) → Γ_Q → 1] → [1 → SL(2,Ẑ) → GL(2,Ẑ) → Ẑ^* → 1] with χ cyclotomic (margin: "ne pas
  confondre SL(2,Z)^ avec SL(2,Ẑ)!!!"); (48)–(51) **π_1(M'_{1,1}) = N'_{1,1} ≃ π_1(U_{0,3}, S_3) = E'_{0,3}** and
  Π'_{0,3} ≃ SL(2,Z)/±1 (to be made explicit on generators: "un calcul-clef").
- j-invariant: f(z) = (3^3/2^2) z^2(z−1)^2/(z^2−z+1)^3 (58), j(λ) = 2^{a+2}(z^2−z+1)^3/(z^2(z−1)^2) with b = 3 and
  a to be determined at 2 by level 3 structure (N: classically j = 2^8 (λ^2−λ+1)^3/(λ^2(λ−1)^2), so a = 6,
  critical value 1728 = 2^6·3^3).
- (2:sc567–573) M_{1,1}[4] → M_{1,1}[2]' ≃ U_{0,3}: Galois of order 8, over μ_4^*; over S' = Spec Z[1/2][i]:
  Galois group SΓ'_{4,2} ≃ sl(2,F_2)/scalars ≃ F_2^2, the universal abelian covering of exponent 2 of U_{0,3}:
  **(71)** M_{1,1}[4]_{S'} ≃ the Fermat curve x^2+y^2+z^2 = 0 (octahedral covering; SL(2,Z/4)' ≃ S_4 expected (70)).
  Table (75): SΓ'_n for n = 2,3,4,5 ↔ M_{1,1}[2]', M_{1,1}[3], M_{1,1}[4], M_{1,1}[5] ↔ spherical bitriangle,
  tetrahedron, octahedron, icosahedron (the rational congruence modular curves = the regular triangulated
  polyhedra). Wish: relations between points of these rational curves and elliptic curves with level 3, 4, 5
  structure "valables simultanément en toutes caractéristiques"; link with the action of Γ_Q on isomorphism classes
  of maps (cartes), in particular regular spherical maps; "C'est assez extraordinaire que Jean Malgoire, depuis
  trois ans que la question est là, n'y ait pas encore touché".
- Complement on the cross-ratio: λ(x_1,..,x_4) = (x_4−x_1)(x_2−x_3)/((x_2−x_1)(x_4−x_3)) (79), characterized by
  homographic invariance and f(0,1,∞,x_4) = x_4; symmetry (80) through S_4 → S_3 → PGL(1). End of cote 140-2 (p.292).

---

**State of these notes (12 Nov 2026, 12:46 UTC):** Part I (cote 140-2, 575 scans, pp. 1–292, §§1–37) is read
in full and noted above. Parts II–IV (cotes 140-3, 140-4, 140-1) are not yet read; only their tables of contents
were looked at (see the plan at the top).
