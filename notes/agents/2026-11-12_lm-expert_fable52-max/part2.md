
### 1.B The companion: *Étale covers with a prescribed exterior sheet* (OpenAI, 24 September 2026, 7 pp.)

It is not cited by the main paper and is not used in the proof of Theorems 1.1 and 1.2; it is an earlier,
independent consequence of the same resolution-of-nonsingularities input.

| No. | Statement (hypotheses in full) | Verdict |
|---|---|---|
| Thm 1.1 | k/Q_p finite, Ω the completion of k̄; X/k̄ smooth proper connected of genus ≥ 2; distinct b_1..b_d ∈ X(k̄) (d ≥ 1) with rational local parameters t_i; pairwise disjoint open discs B_i = {abs(t_i) < R_i}; radii r_i in the value group, 0 < r_i < R_i; V_i = {abs(t_i) < r_i}; U = X^an minus the V_i, assumed non-empty with an Ω-rational point. Then there are a smooth proper connected Y/k̄ and a finite étale surjective g: Y → X such that (i) a connected component of g^{-1}(U) maps isomorphically to U; (ii) for every i, every connected component of g^{-1}(V_i) maps to V_i with degree divisible by p. | Proof verified (below), given the positive-genus form of resolution of nonsingularities. |
| Lemma 2.1 | f: C → X connected finite étale Galois with group G; D = U or some V_i. Every component of f^{-1}(D) is finite étale and surjective over D; G is transitive on components; a component with stabilizer B has degree order(B). | Verified. |
| Prop 2.2 | There is a connected finite étale Galois Z → X whose stable skeleton contains, for each i, an embedded circle lying entirely above V_i. | Verified: two positive-genus stable vertices above V_i (input), a skeletal path between them above V_i, an F_ℓ-torsor on the special fibre connected on the two end components (surjectivity of H^1 of the special fibre onto the H^1 of the normalized components; lifting by SGA 1 IX 1.10), Betti number of the inverse graph ≥ ℓ − 1 > 0; Galois refinement keeps a circle. |
| Lemma 3.1 | For every i there is a connected cyclic finite étale cover of Z of degree p, trivial over all of U_Z = Z^an ×_{X^an} U, whose restriction to at least one component above V_i is connected. | Verified: a cyclic degree-p covering of the skeleton cut at a type-3 point of the circle (retraction fibre a single point, so the image of U_Z avoids the cut); topological coverings of a Berkovich curve are analytic (de Jong, Lemma 2.6) and algebraize. |
| Section 4 | Proof of Thm 1.1: T = a component of the fibre product of all conjugates, G = Gal(T/X), P = Gal(T/Z) elementary abelian p; H = stabilizer of a component over U; H ∩ P = 1; B ∩ P ≠ 1 for every stabilizer B of a component over V_i; Y = T/H. | Verified (degree of the image of a component with stabilizer B is [B : B ∩ H]; it is 1 for B = H and divisible by order(B ∩ P) over V_i). |

External input: the "alternative formulation" of Σ-RNS stated before Theorem A of Mochizuki–Tsujimura (**checked**,
verbatim: "Let 𝒵 be a compactified model of Z over O_K; z ∈ 𝒵_s a closed point. Then, after possibly replacing K by a
suitable finite extension field of K, there exist a connected geometrically pro-Σ finite étale Galois covering
Y → Z ..., a compactified stable model 𝒴 of Y ..., a morphism 𝒴 → 𝒵 ... that restricts to the finite étale Galois
covering Y → Z, an irreducible component D of 𝒴_s whose normalization is of genus ≥ 1, and whose image in 𝒵_s is
z"), Baker–Payne–Rabinoff (skeleta and models; not checked), de Jong, Poineau, SGA 1 (not checked).
Assessment: correct as far as I can check; no gap found. Relation to Bresciani's theorem that a non-geometric
section has a neighbourhood of index divisible by p (quoted in the main paper's introduction): the companion gives
covers with p dividing the degree over every disc while one exterior sheet is kept; it is not a statement about
sections.

### 1.C What family 019 gives, and does not give, for La Longue Marche

**Given (claimed).**
1. The local p-adic section conjecture for **proper** curves of genus ≥ 2 over **finite extensions of Q_p**
   (Thm 1.1): in his language (2:sc63–64, case III of §8 with I = ∅), the map from K-points to π-conjugacy classes
   of splittings of E → Γ is bijective when Γ = G_k and X is complete of genus ≥ 2.
2. Decomposition groups in π_1(X) of rank-one valuations above p equal the birational ones (Cor. 7.1), and none of
   them contains a section image (Lemma 7.2). Every section is therefore birationally liftable.
3. Over a number field K, for proper C of genus ≥ 2: every section is a Selmer section (locally a point at every
   finite place by Thm 1.1, a component at every real place), and loc(Sec(C/K)) = C(A_K)_•^{f-cov} (Prop. 8.1).
   Hence the exact equivalence, in both directions:
   **the section conjecture holds for C/K if and only if C(A_K)_•^{f-cov} = C(K)** ("C is excellent with respect
   to all coverings" in Stoll's terms; ⇐ is Thm 8.2; ⇒: if every section is s_a, then loc(Sec) = C(K), and Prop. 8.1
   gives the equality). Stoll's Remark 8.9 had the implication ⇒ under the section property.
4. The section conjecture for the curves where that equality is a theorem: a non-constant map to an abelian variety
   with finite Mordell–Weil group and Sha_div = 0; Jacobian with these properties; X_0(N), X_1(N) of genus ≥ 2 over Q.
   For these his finiteness statement of 2:sc65 (finitely many π-classes of splittings) is a theorem (the classes
   are the rational points).
5. Finiteness of the local images loc_v(Sec(C/K)) when K has no CM subfield (Betts–Stix with item 3). With
   Porowski's theorems (arXiv:2509.15660; arXiv:2607.27746, Thm 1.5) a section is determined by its reductions at
   any set of places of strongly positive density. Finiteness of Sec(C/K) itself does not follow: what is missing is
   injectivity (or finite fibres) of loc_v at one place.

**Affine curves and cuspidal sections: not in the paper, but they follow.** Let U = X ∖ S be hyperbolic over a
finite k/Q_p, s a section of π_1(U) → G_k. For open H ⊇ s(G_k) let U_H be the cover and X_H its smooth completion.
The H with genus(X_H) ≥ 2 are cofinal (take H = N·s(G_k) with N characteristic open in the geometric group). By
Thm 1.1 the section induced on X_H is s_{x_H} for a unique x_H ∈ X_H(k); uniqueness makes (x_H) a compatible
system. The fibres of the pro-system of compactified geometric covers over the x_H are non-empty profinite sets, so
there is a point ỹ over all x_H; for γ ∈ s(G_k), γỹ and ỹ have the same image in every X_H, i.e. γỹ ∈ (H ∩ π̄)ỹ for
all H, and ∩(H ∩ π̄) = 1, so γỹ = ỹ. Hence s(G_k) lies in the decomposition group of ỹ, and s is the section of a
point of U(k) or a cuspidal section at a point of S(k). (This is the standard neighbourhood argument: Tamagawa;
Stix, arXiv:1203.3236, 2.1.2 and the proof of Cor. 5.) Injectivity and disjointness of the packets hold over local
fields (Stix, arXiv:0809.0017, Thm 14 with Remark 15 (2) and Thm 45, Remark 46). So, granted Thm 1.1:

> for every hyperbolic curve U over a finite extension k of Q_p,
> U(k) ⊔ ⊔_{y ∈ S(k)} {classes of sections of π_1(U_y) → G_k} → {classes of sections of π_1(U) → G_k} is bijective,

which is his corrected conjecture of 2:sc79 with K replaced by k, and the packet at y is a torsor under
H^1(k, Ẑ(1)) = the profinite completion of k^× ≅ Ẑ × O_k^×. The map Θ: k^× → H^1(k, Ẑ(1)) **is injective** for
such k (k^× ≅ Z × finite × Z_p^n has no non-trivial divisible element); its cokernel is Ẑ/Z. (Over R it is not
injective: H^1(R, Ẑ(1)) = Z/2.)

**Not given.**
- Number fields in general: only the equivalence of item 3; the equality C(A_K)_•^{f-cov} = C(K) "remains a separate
  arithmetic hypothesis" (the paper's words).
- Genus 0 and 1. For genus 1 the statement is false over p-adic fields: sections of π_1(E) → G_k are H^1(k, T E),
  and E(k) → H^1(k, TE) is injective with cokernel the Tate module of H^1(k, E) ≅ Hom(E(k), Q/Z), which contains
  Z_p^{[k:Q_p]}. Punctured genus 0 and genus 1 curves that are hyperbolic are covered by the affine statement above.
- Fields other than finite extensions of Q_p: nothing for finitely generated extensions of Q_p, for p-adically
  closed fields that are not local (there the birational statement fails: Koenigsmann Prop. 2.4 (2)), or for
  function fields.
- Relative versions (his family over a base, 2:sc433–436): nothing.
- Quotients of π_1: nothing; and the statement is false for the pro-p and the geometrically metabelian quotients
  (Hoshi; Saïdi; Part 2, item 7).
- His characterization by Ker χ (letter to Faltings, PS; 2:sc431–433 "peut-être même π^{Γ⁺} = 1"): untouched.
- The Hom-form and Isom-form: untouched (they are Mochizuki's and Tamagawa's).
