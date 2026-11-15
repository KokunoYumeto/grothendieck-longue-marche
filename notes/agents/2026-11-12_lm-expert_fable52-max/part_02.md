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
