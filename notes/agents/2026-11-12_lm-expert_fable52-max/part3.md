
---

## Part 2. Primary sources

All paths are under `Free or receipted\free\lm-expert-20261112\`.

### 1. Grothendieck, *Brief an G. Faltings*, 27 June 1983

- Source: German text as printed in *Geometric Galois Actions 1* (LMS Lecture Note Series 242, 1997, pp. 49–58),
  copy at `https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/GanF.pdf` (the Grothendieck Circle,
  page of L. Schneps, co-editor of the volume; the editors' note says Faltings gave permission to reproduce it).
  This is an editor's page, not the author's; the shelf already holds EGA and FGA from the same host. Local:
  `grothendieck-faltings-1983\grothendieck_brief_an_faltings_GanF.pdf`. Read in full.
- **The conjecture (7), p. 54.** For an anabelian curve X over an "absolute" field K (finitely generated over the
  prime field; characteristic 0 assumed): "Es sei Γ(X/K) die Menge aller K-wertigen Punkte (also 'Schnitte') von X
  über K, man betrachtet die Abbildung (7) Γ(X/K) → Hom ext_{π_1(K)}(π_1(K), π_1(X)), wo die zweite Menge also die
  Menge aller 'Spaltungen' der Gruppenerweiterung (3) ist ..., oder vielmehr die Menge der üblichen
  Konjugationsklassen solcher Spaltungen via Aktion der Gruppe π_1(X̄). Es ist bekannt, dass (7) injektiv ist, und die
  Hauptvermutung sagt aus, dass sie bijektiv ist. [siehe unten Berichtigung]"
- **Third formulation and the correction, pp. 56–57.** With X̃ the universal covering and X̃^ its normalized
  completion: for a given splitting, "Die Vermutung ist nun, dass letztere Aktion (genau) einen Fixpunkt besitzt"
  (on X̃^(K̄)). Then: "die Formulierung von der Hauptvermutung via (7) ... nur im Fall wo X eigentlich ist eine
  korrekte ist ... Im Falle hingegen, wo X nicht eigentlich ist, also 'unendlich ferne Punkte' besitzt, so liefert
  jeder dieser Punkte auf naheliegende Weise ein erkleckliches Paket von Spaltungsklassen (deren Mächtigkeit das des
  Kontinuums ist), die sich nicht durch im endlichen liegende Punkte erhalten lassen. Diese entsprechen dem Fall
  eines Fixpunktes in X̃^, der nicht in X̃ liegt. Die Einzigkeit des Fixpunktes besagt unter anderen, ausser der
  Injektivität von (7), dass die 'Pakete', die verschiedenen Punkten im Unendlichen entsprechen, leeren Durchschnitt
  haben, also dass jede Spaltungsklasse, die keinem endlichen Punkt entspricht, einem eindeutig bestimmten Punkt im
  Unendlichen entspringt."
- **The PS, p. 58: a group-theoretic characterization of the image of (7)** ("mutmasslich ... in beiden
  Richtungen"): with π_1(K)° = Kern von π_1(K) → Ẑ^* (cyclotomic character): for a splitting, "π_1(K)° operiert auf
  π_1(X̄) ... Die Bedingung ist nun, dass die Fixpunktgruppe dieser Aktion nur aus 1 bestehen soll!"
- **On injectivity, p. 52:** "Der Beweis ergibt sich ziemlich einfach aus dem Mordell–Weilschen Satz, dass die Gruppe
  A(K) ein endlich erzeugter Z-Modul ist, wo A die 'jacobienne généralisée' von Y ist".
- Bears on: F7, H5; 2:sc63–64 (case III), 2:sc77–79, 2:sc431–433.
- Verdict: **confirms** F7. The 1981 text (2:sc77–79) already has the 1983 conjecture in the same form: at each
  rational point at infinity a torsor of classes under H^1(K, T(G_m)) = lim K^×/n ("famille transcendante"; in 1983
  "Paket ... Mächtigkeit des Kontinuums"), the classes for distinct points at infinity distinct, and "peut-être n'y
  a-t-il pas d'autres scindages" = existence of the fixed point. Both take the **whole** packet, not only its
  K^×-subtorsor of tangential sections. Two corrections to carry: (a) in both texts the injectivity is credited to
  "G(K) (resp. A(K)) de type fini" for the generalized Jacobian; this is false when the toric part is non-trivial
  (K^× is not finitely generated); what is true and suffices is that G(K) has no non-trivial divisible element
  (item 3). (b) The criterion of the PS is the precise form of his "peut-être même π^{Γ⁺} = 1" (2:sc433) and of
  "π̂_{0,3}^{Γ''⁺} = 1" (2:sc480–482); the weaker condition π^Γ = 1 does not separate points from cusps (item 6).

### 2. Cuspidal sections and tangential base points

**Stix, *On cuspidal sections of algebraic fundamental groups*, arXiv:0809.0017v1 (2008).** Local:
`stix-cuspidal\`. k of characteristic 0, U = X ∖ Y a curve, U_y the scheme of nearby points at y ∈ Y.
- Definition (1.3): "A cuspidal section of π_1(U/k) is a section that factors over some π_1(U_y) for a point y ∈ Y
  with residue field κ(y) = k." "There is also a version of the section conjecture for affine curves stating that
  all but cuspidal sections come from rational points."
- Prop. 8: "The extension π_1(U_y/κ(y)) splits and there is a natural free transitive action on S_{π_1(U_y/κ(y))} by
  [the pro-N completion of] κ(y)^*" (= H^1(κ(y), Ẑ(1))).
- For U hyperbolic. Prop. 11: inertia groups at distinct cusps of the universal cover meet trivially. Cor. 12: "The
  normalizer of I_{ỹ/y} in π_1(U ⊗ k^alg) (resp. π_1(U)) are I_{ỹ/y} (resp. D_{ỹ/y})." Cor. 13: "Let A be an abelian
  subgroup of π_1(U) that nontrivially intersects an inertia subgroup I_{ỹ/y}. Then A is contained in I_{ỹ/y}."
- Thm 14: "Let us assume that the injectivity part of the section conjecture holds for proper curves of genus at
  least 2 over finite extensions of k. Then the following holds. (1) A cuspidal section uniquely determines the cusp
  y for which it factors over π_1(U_y). (2) Let y be a k-rational cusp of U. The natural map S_{π_1(U_y/k)} →
  S_{π_1(U/k)} is injective and the image disjoint from the sections induced by rational points u ∈ U(k) or cuspidal
  sections originating from a different cusp." Remark 15: the image "is called the 'Paket' ... in [Gr83]"; the
  assumption holds when A(k) has no divisible elements for every abelian variety A/k.
- Thm 17 (abelianized extension): for k with non-trivial Kummer theory and (i) no non-trivial divisible torsion in
  A(k) or (ii) infinite Ẑ-rank of the completion of k^*: "The natural map S_{π_1(U_y/k)} → S_{π_1(U/k)} has
  uncountable image", already in the extension by π_1^ab.
- Thm 20 (Nakamura), Cor. 21, 22: for k that "distinguishes tori from abelian varieties" (Hom_{Gal_k}(T S, T A) = 0;
  e.g. number fields k with kQ^ab/Q^ab finite, Lemma 19) and U hyperbolic: a non-trivial closed subgroup lies in an
  inertia group iff it is pro-cyclic and (essentially) cyclotomically normalized; "the set of inertia subgroups in
  π_1(U) coincides with the set of maximal closed subgroups of π_1(U) among those which are pro-cyclic and
  cyclotomically normalized"; "A section s ∈ S_{π_1(U/k)} is cuspidal if and only if the image s(Gal_k)
  cyclotomically normalizes a pro-cyclic subgroup of π_1(U)."
- Listed by Stix as missing (1.4): "(2) recognize tangential sections within cuspidal sections".

**Esnault–Hai, *Packets in Grothendieck's section conjecture*, arXiv:math/0703877v2 (2007).** Local: `esnault-hai\`.
- Conjecture 2.2 (their statement of the letter): U hyperbolic over k of finite type over Q. (SC1) U(k) → sections
  injective. (SC2) a geometric section has a unique fixed point on the compactified universal cover, above the
  point. "(SC3) For a non-geometric section, the resulting action of Γ on X(U_ū) has also a unique fixed point, which
  lies at infinity ..., and projects on a point in (X ∖ U)(k). This implies in particular that the set of non-geometric
  sections is divided into disjoint 'packets' P_x, x ∈ (X ∖ U)(k). (SC4) Each packet P_x has the cardinality of the
  continuum."
- Proved there: Thm 5.1 (SC1 for U "elliptic or hyperbolic" over k of finite type over Q; "The ellipticity
  assumption is sharp", A^1 fails); Prop. 5.3 (semi-abelian A/k: A(k) → classes of fibre functors injective, by
  "Since k is of finite type over Q, there are no k-rational points which are infinitely divisible"); Thm 5.5 (at
  most one fixed point); Thm 6.5 (for U hyperbolic over any k of characteristic 0, T_x = P_x: the packet at x is
  exactly the set of fibre functors coming from the punctured tangent space at x); Cor. 6.9 (for k of finite type
  over Q, P_x has the cardinality of the continuum). Open there: SC3 (existence of the fixed point).

**Deligne, *Le groupe fondamental de la droite projective moins trois points* (1989), §15 "Points base à l'infini".**
Source: IAS, `https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf`; local `deligne-1989\`
(OCR text layer; §15 read, pp. 229–242 of the original). 15.13–15.26: for a curve X̄ over k of characteristic 0,
S finite, X = X̄ − S, s ∈ S, T_s the tangent space and T_s^0 = T_s − {0}: a functor R ↦ R^(s) from finite étale
covers of X to finite étale covers of T_s^0, by principal parts (15.14–15.15), valid over non-closed k (15.18), with
the algebraic form T_s^0 = Spec Gr(K_s) for the filtered local field (15.20–15.21) and the description through a
formal isomorphism φ of (T_s, 0) with (X̄, s) with φ'(0) = 1 (15.24–15.26). A k-rational non-zero tangent vector is
then a fibre functor on the covers of X, i.e. a base point "à l'infini" defined over k.
- Bears on: F7; 2:sc75–77 (his construction: a uniformizer t gives a section; t and tu, u ∈ 1 + m, give the same
  class; the classes form a torsor under H^1(k, T(G_m)); (m/m²)^* embeds as a Θ(k^*)-subtorsor).
- Verdict: **confirms** F7. His 1981 construction is Deligne's tangential base point (dependence only on the
  tangent vector = on t mod m²), and the two torsors are Stix's Prop. 8 and Esnault–Hai's Thm 6.5. **One
  correction to his text**: 2:sc79 says the classes for distinct points at infinity are distinct "même en se ramenant
  aux scindages correspondants de l'extension de Γ par π_ab". In the full group this is Stix's Thm 14. In the
  extension by π_ab it holds for genus ≥ 1 (the classes map to the classes of the distinct points y_i in the
  extension by π_ab(X), Jacobian argument) but **fails in genus 0**: on U = P^1 ∖ {0,1,∞} the abelianized class of a
  point x is (x, 1−x) ∈ (completion of K^×)², the packet at 0 is {(a, 1)}, the packet at 1 is {(1, b)}, and the
  tangential sections "0 towards 1" and "1 towards 0" both give (1, 1). (Equivalently: the Galois cocycle f_σ
  comparing these two base points lies in the closure of the commutator subgroup.) Within one packet the abelianized
  classes all coincide when ν = 1 (the loop subgroup dies in π_ab). So the abelianized form is true for distinct
  cusps when g ≥ 1, false in general when g = 0, and inside one packet it needs at least ν ≥ 2 (Stix's Thm 17 then
  gives an uncountable image under its hypotheses).

### 3. Injectivity of points → sections

- Stix, arXiv:0809.0017, Appendix B, Thm 45: "Let k be a field such that the group of k-rational points A(k) has no
  nontrivial divisible elements for any abelian variety A/k. Let x, y ∈ X(k) be k-rational points of a variety X/k
  that immerses into an abelian variety such that the associated sections s_x, s_y ∈ S_{π_1(X/k)} agree. Then x equals
  y." Remark 46: "The assumptions ... are valid for number fields (resp. local fields) by the Mordell–Weil Theorem
  (resp. compactness). In particular the injectivity part of the section conjecture holds for hyperbolic curves over
  such fields as the Albanese map is eventually an immersion for suitable finite étale covers."
- Esnault–Hai Thm 5.1 and Prop. 5.3 (item 2): k of finite type over Q; curves that are elliptic or hyperbolic
  (genus ≥ 1, or genus 0 inside G_m); semi-abelian varieties. This is exactly the generality of 2:sc64 ("g = 0 ⇒
  ν ≥ 2": no component isomorphic to P^1 or the affine line; G_m is allowed).
- Mochizuki, *The local pro-p anabelian geometry of curves* (1999), Thm 19.1 (sub-p-adic fields, complete curves of
  genus > 1): **primary not obtained in this fork**; quoted by Koenigsmann (Remark 1.2 (2)): "By Theorem 19.1 of
  [Mo], σ_{X/K} is injective for any smooth complete curve X of genus > 1 over a sub-p-adic field K".
- The 2026 paper's own proof for finite k/Q_p (Section 7).
- Verdict for 2:sc64: **confirms** the statement, **corrects** the reason: the input is "G(K) has no non-trivial
  divisible element" for the semi-abelian G (true for K finitely generated over Q: for the abelian quotient by
  Mordell–Weil–Lang–Néron, for the torus because K^× is a finitely generated group times a free abelian group, and
  the extension is handled by multiplying by the exponent of the torsion of A(K)); "G(K) de type fini" is false as
  soon as the torus is non-trivial. His excluded cases are g = 0 with ν ≤ 1 (not ν = 2).

### 4. The birational and the valuative theorems over p-adic fields

- Koenigsmann, *On the 'section conjecture' in anabelian geometry*, arXiv:math/0305226v1 (J. reine angew. Math. 588
  (2005)). Local: `koenigsmann-2005\`. Def. 1.1 (SP): σ_{X/K}: X(K^perf) → {non-branch sections}/conj. bijective,
  "where a section is called non-branch section, if the image is not in a decomposition subgroup of π_1(X) w.r.t. a
  branch point, i.e. a point in X̃ ∖ X". Prop. 2.4 (quoted in 1.A). Cor. 2.6: a section of G_{K(X)} → G_K over a
  number field K forces points over all completions. Lemma 1.7: for K finite over Q_p, finitely generated over Q, or
  finite, the (birational) section property for all curves is equivalent to the weak one for all curves (limit
  argument; Faltings or compactness).
- Pop, *On the birational p-adic section conjecture*, MPIM preprint 2007-102 (Compositio Math. 146 (2010)). Local:
  `pop-birational-2007\`. Thm A (k/Q_p finite containing μ_p, K the function field of a complete smooth curve X):
  "1) Every k-rational point x of X gives rise to a bouquet of liftable sections s_x: G'_k → G'_K. 2) Let s': G'_k →
  G'_K be a liftable section. Then there exists a unique k-rational point x of X such that s' equals one of the
  sections s_x", where ' is the maximal Z/p-elementary abelian quotient and "liftable" means liftable to the Z/p
  metabelian quotients.
- Pop–Stix, arXiv:1111.1354v1 (J. reine angew. Math. 725 (2017)). Local: `pop-stix-2011\`. Thm 26 and 6.1 (quoted
  in 1.A); classification of the valuations above p (Appendix A: types 1v, 2h, 2v, 2u); 6.2: the valuation given by
  Thm 26 is never of type "2u smooth".
- Mochizuki–Tsujimura [17], Thm F (i): for H ⊂ G_K closed with H ∩ I_K ↠ Z_l and a section s_X: H → Π_X^{(Σ)} of a
  proper hyperbolic curve defined over a p-adic local field: at most one fixed point in the pro-Berkovich space of
  the universal covering (exactly one if the l-adic cyclotomic character has open image on H); "s_X arises from an
  Ω^H-rational point ∈ X(Ω^H) if and only if its image is a maximal stabilizer ... of a point".
- Bears on: F7 (its sentence on 019), 2:sc63–64 over local fields. Verdict: **confirms** what F7 says about the
  local theorem and its ingredients.

### 5. The real section conjecture

- Mochizuki, *Topics surrounding the anabelian geometry of hyperbolic curves* (2003), §3 (author's page; local
  `mochizuki-topics\`).
  - Thm 3.6 ("General Discrete Real Section Conjecture"): (X, ι) a real complex manifold with an ι-invariant metric
    whose universal cover satisfies (*): "the correspondence Y ↦ ι_Y defines a bijection π_0(X(R)) ≅
    Hom_{Gal(C/R)}(Gal(C/R), π_1(X^ι)) from the set of connected components of the real locus X(R) to the set of
    conjugacy classes of sections of π_1(X^ι) → Gal(C/R) (or, equivalently, involutions in π_1(X^ι)). Moreover, the
    centralizer of an involution ι_Y ∈ π_1(X^ι) is the image of π_1(Y^ι) in π_1(X^ι)."
  - Cor. 3.7: the same for every hyperbolic real Riemann surface (compact or not). Remark after it: "there is no
    discussion of 'tangential sections' ... every tangential section arising from a real point at infinity may be
    obtained as a limit of a sequence of real points that are not at infinity ..., hence is 'automatically
    included' in the connected component containing those real points."
  - Cor. 3.8: the same for the moduli stacks M_{g,r} (2g − 2 + r > 0), discrete groups: π_0(M_{g,r}(R)) ≅ classes of
    involutions of the extended mapping class group lying over complex conjugation, with centralizers.
  - Cor. 3.13 ("Profinite Real Section Conjecture for Real Hyperbolic Curves"): "Let X be a hyperbolic curve over R.
    Then ... π_0(X(R)) ≅ Hom_{Gal(C/R)}(Gal(C/R), π_1^alg(X))" (classes of sections). X need not be proper.
  - Cor. 3.15: the profinite statement with centralizers for M_{g,r}, g ≤ 2 only (goodness of the mapping class
    group is not known for g > 2).
- Stix, arXiv:0802.4125 (Amer. J. Math. 132 (2010)), Appendix A, Thm 26: "Let X/R be a smooth, projective curve of
  genus ≥ 1. Then the map π_0(X(R)) → S_{π_1(X/R)} ... is a bijection of finite sets." Local `stix-period-index\`.
- Bresciani–Vistoli, arXiv:2012.06278v2: "The real section conjecture holds for ... (1) Torsors for semiabelian
  varieties. (2) Smooth quasiprojective curves, with the exception of the projective curves of genus 0 without real
  points." Local `bresciani-vistoli\`; proof read.
- Pál (J. London Math. Soc. 83 (2011)), Wickelgren (Math. Ann. 358 (2014)), Esnault–Wittenberg (Mosc. Math. J. 9
  (2009), Remark 3.7 (iv)): **primaries not obtained**; their results are as summarized in the introduction of
  Bresciani–Vistoli (other proofs of the same bijection for curves).
- Bears on: H7, F7; his theorem of 2:sc440–445 (§33) and (29)–(30) of 2:sc377–378.
- Verdict: **confirms** H7 and sharpens it. (a) His §33 theorem (π_0(U^σ) ≅ classes of splittings over Z/2; the
  centralizer π^{σ_i} is 1 for a component ≅ R and Z for an oval) is Mochizuki's Thm 3.6 / Cor. 3.7 (2003), with the
  same centralizer statement; he proved it in 1981 modulo the lemma on anti-involutions of the disc. (b) The profinite
  bijection is a theorem for all hyperbolic real curves, affine included (Mochizuki Cor. 3.13; Bresciani–Vistoli).
  (c) **Correction to the picture with cusps**: over R all sections come from components of U(R); the packet at a
  real cusp has exactly two elements (H^1(R, Ẑ(1)) = Z/2, the two half-branches), and each is the class of the
  adjacent component of U(R). So "π_0(U(R)) ≅ non-cuspidal sections" is false; the non-cuspidal classes are the ovals
  of X(R) that carry no cusp. (d) Not found in the literature read: the profinite centralizers of the involutions for
  curves (expected 1 and Ẑ; Mochizuki states the profinite centralizer only for moduli in genus ≤ 2).

### 6. "Proper case plus cuspidal sections gives the affine case" (H5; his axiom ⑤, 2:sc418)

In the literature in substance, as the neighbourhood (limit) argument:
- Koenigsmann Lemma 1.7 and Def. 1.1 (statement for affine curves with non-branch sections);
- Stix, arXiv:1203.3236v3, 2.1.2 ("the limit argument") and the proof of Cor. 5: "The limit argument ... implies that
  s = s_a for any a ∈ im(X_s(k) → X(k)). Since we assumed s not to be cuspidal, we may even deduce that a ∈ X(k)
  [the open curve]";
- Bresciani, arXiv:2108.13397 (abstract): "the section conjecture is equivalent to the cuspidalization of all
  sections over all finitely generated fields";
- Steklov, arXiv:2602.17746v2, Introduction: the conjecture stated as bijectivity of
  V(k) ⊔ ⊔_{y ∈ Y(k)} S_{π_1(V_y/k)} → S_{π_1(V/k)}.
What is proved this way: if surjectivity holds for all proper curves of genus ≥ 2 over k (number field: with
Faltings' finiteness for the limit; local field: compactness), then every section of an affine hyperbolic curve over
k is the section of a point or cuspidal; the derivation is written out in 1.C for local fields. Together with Stix
Thm 14 (packets injective and disjoint) this is his ⑤ a), b), c) for a hole fixed by Γ. I did not find his axioms
①–⑥ themselves compared with the standard forms anywhere; that comparison is new work, but each arrow is of this
kind.
On "admissible = normalizes no loop subgroup": a section is cuspidal iff its image lies in D_ỹ = the normalizer of
I_ỹ (Stix Cor. 12), so every member of a packet, tangential or "transcendental", normalizes a loop subgroup; over
fields distinguishing tori from abelian varieties, cuspidal ⇔ cyclotomically normalizes a pro-cyclic subgroup
(Stix Cor. 22). So his admissible sections are exactly the non-cuspidal ones there. His rigidity condition
π^Γ = 1 holds for point sections and for cuspidal sections alike (for a cuspidal section the centralizer lies in
I_ỹ ≅ Ẑ(1), where Γ has no fixed point); only the kernel of χ sees the difference: Ker χ centralizes I_ỹ.
Verdict: **H5 confirmed in substance**; the equivalence with his axioms is to be written; his "π^Γ = 1" must be
replaced by "π^{Ker χ} = 1" (his own 1983 PS) wherever it is meant to exclude cusps.

### 7. Search for 2026 (and late 2025) results (claims, unchecked unless said)

Searched 12 Nov 2026 (web search; arXiv abstract pages read directly).
- **Steklov, *Fermat's Last Theorem for Selmer sections*, arXiv:2602.17746v2 (3 March 2026).** Introduction read.
  Thm A: "All Selmer sections s ∈ S_{π_1(V_ℓ/Q)} of the Fermat curve V_ℓ/Q are cuspidal for ℓ ≥ 7" (V_ℓ: X^ℓ + Y^ℓ + Z^ℓ
  = 0, XYZ ≠ 0; Selmer: rational or cuspidal at every place). Thm B: "The section conjecture for all hyperbolic curves
  over all finite extensions of k, implies the section conjecture for all hyperbolic DM-curves over k" (e.g. the
  moduli stack of elliptic curves). Thm C: for k sub-p-adic, "the fully faithfulness in the section conjecture holds
  for all hyperbolic DM-curves over k". **Consequence to check**: with Thm 1.1 of 019 and the affine derivation of
  1.C, every section over Q of an affine hyperbolic curve is a Selmer section, so every section of π_1(V_ℓ) → G_Q
  would be cuspidal for ℓ ≥ 7: the section conjecture for the affine Fermat curves, which is the statement behind
  his remark of 2:sc65 on Fermat.
- **Porowski, *On reductions of Selmer sections*, arXiv:2509.15660 (19 Sep 2025)**: "the conjugacy class of a
  noncuspidal Selmer section is uniquely determined by its reduction on a set of density one"; ***Families of curves
  separating points*, arXiv:2607.27746v1 (30 July 2026)**, Thm 1.5: for proper hyperbolic X with stable reduction
  over a number field, the reduction map on Selmer sections is injective for every set of places of strongly
  positive density; "It is an important open problem to show that the map red_Ω is injective whenever the set Ω is
  infinite".
- **Bresciani, *The section conjecture for the toric fundamental group over p-adic fields*, arXiv:2409.07923v5
  (14 Sep 2026)**: the analogue of the conjecture for the toric fundamental group over p-adic fields; "a new
  interpretation of Selmer sections as toric Galois sections".
- **Sun, *The absolute anabelian geometry of virtual curves of arbitrary genus*, arXiv:2604.23485 (26 April 2026)**:
  "group-theoretic conditions under which a section of an arithmetic fundamental group arises from a rational point"
  (abstract only).
- **Yamaguchi, arXiv:2601.07112v4 (24 May 2026)** (the item on the reading-list card): "the maximal m-step solvable
  quotients of the étale and tame fundamental groups of a hyperbolic curve over a separably closed field are
  torsion-free and center-free", m ≥ 2. (For F5, not for sections.)
- Older, needed as limits of what can be asked: Hoshi, *Existence of nongeometric pro-p Galois sections of hyperbolic
  curves*, Publ. RIMS 46 (2010) 829–848 (primary not obtained; cited from Hoshi–Tsujimura RIMS-1950 (2021), read:
  explicit non-geometric pro-p sections of punctured projective lines over finite extensions of Q and of Q_p; open:
  the same for an irregular prime); Saïdi, arXiv:1510.06864 and arXiv:2109.14882 (non-geometric sections of the
  "étale-by-geometrically abelian", geometrically metabelian and pro-nilpotent-by-abelian quotients over p-adic
  local fields; abstracts read).
- Not found: any independent check, erratum or public discussion of the OpenAI paper of 6 Oct 2026; any 2026 preprint
  by other authors claiming the p-adic or the global conjecture.
