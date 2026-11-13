# What the return FLAGGED_149 changes

Claude Fable 5.2 (effort max), 13 November 2026. Companion to `REVIEW.md` in this folder. No prompt was edited.
Statement numbers are the return's. GOOD_REDUCTION was read in its `_work` version of 12 November; the packaged
copy in `pro_prompts_archive_20261112\GOOD_REDUCTION\` was not reopened, so item labels are to be checked against it.

## 1. GOOD_REDUCTION (unsent)

Its main question is answered by F17.6 and F17.7 (correct in the intake; resting on six quoted places, REVIEW F3).
Item by item:

| Item | Status after FLAGGED_149 | What remains |
|---|---|---|
| A1 (i), (ii), (iv) | F17.6: node groups injected, normalized cyclotomically after a finite extension, for every splitting; pairwise non-conjugate with the cusp groups, maximal procyclic (Mochizuki Prop. 1.2) | nothing; without rationality: F17.8 (G_k permutes nodes); the sign under branch exchange is CYCLOTOMIC_KERNEL E4 |
| A1 (iii) | not proved in general; F17.2 and F17.3 give the twist in two examples; non-triviality follows from F17.1 | the profinite Dehn multi-twist formula with the thicknesses m_e |
| A2, Lead 3 | only the weight-0 quotient (F.12) and the sequence (F.14) for trees | the multiplicities t, 2(g − t), t + ν − 1 for every splitting |
| A3 (the theorem), Lead 1 | F17.7 | nothing |
| A4 | F17.6 (iii) | nothing |
| B1 | F17.1 (Tamagawa (5.3), not opened) | nothing |
| B2, Lead 5 | not addressed | c) ⟺ good reduction of the Jacobian and T fixing each point of D; d) for one ℓ ⟺ c) |
| B3 | F17.2, F17.3, with class two | the statement for abelian varieties that his margin of scan 100 recalls |
| B4, Lead 4 | F17.1 and F17.7: the realizing curve exists over k itself | nothing |
| B5, Lead 6 | F17.5; F17.7 gives the realizing curve as the descent of the special fibre by α : G_k → Gal(K_1/K); REVIEW F4 gives the finiteness criterion and K(ϖ^{1/n}) | the twist written as the image of the class of σ in H¹(k, Ẑ(1)) → H¹(k, μ_n) → H¹(k, Aut C′) |
| B6 | all cells but one: a ⇔ b ⇒ c ⇒ d; a ⇒ e; c, d ⇏ a; c, d ⇏ e; e ⇏ a, c, d | d ⇒ c |
| B7, Lead 7 | first sentence: F17.5; second: F17.6 (iv) with F17.7 | the predicate stated once and its equivalence with e) written |
| B8 | ZCF11: no criterion on the Jacobian detects good reduction of the curve, also with ℓ = p (y² = (x³ − 5⁶)(x³ − 1) over Q_5) | the statement for the Jacobian itself (Grothendieck's criterion) and what replaces (30) |
| C1, Lead 8 | the inertia map κ_i ∘ (μ·id) is C3 | the statement for points and cusps of the realizing curve |
| C2, C3, C4 | not addressed | all three |
| D1 | F17.2 with F17.6 | nothing |
| D2 | F17.3, F17.4 (the coefficient splitting), F17.6 (every splitting) | nothing |
| D3, D5, D6 | not computed; D3 is non-admissible by F17.6, D5 and D6 are potentially good and realized by F17.7 | the explicit models and realizing curves |
| D4 | F17.5 | nothing |

So the prompt, as packaged, asks for a theorem that is proved. Before anything is sent:

1. **A source check of F17.6** (an agent, not Pro): open Illusie 2002 Thm 7.6, Hoshi 2009 Cor. 3.9, Mochizuki 2007
   Example 2.5 and Prop. 1.2 with Def. 1.1 and Remarks 1.1.3–1.1.4, Hoshi–Mochizuki Def. 2.10 (iv), Lemma 2.11,
   Remark 2.14.1, Stix Thm 20 and Cor. 21, Tamagawa (5.3), Knudsen 2.7; compare each with the use made of it in
   F17.1, F17.6, F17.7.
2. **A rewritten GOOD_REDUCTION** with R1–R9 replaced by F17.1–F17.8 as results, Leads 1, 4 and the first half of
   6 removed, and the Parts reduced to the right-hand column above. Its main item becomes A1 (iii) with A2 (the
   action of T and the weights), then C3 and C4 (what Γ° fixes at a degenerate fibre; whether the image of T
   determines the nodes and thicknesses), then B2 with the cell d ⇒ c.
3. **From my map (`research_maps_20261112\CONNES_CONSANI_CFT\MAP.md`, §3), revised.** The first half of the
   sentence proposed there is F17.1, which already covers residue characteristic p with Π^(p′). What stays, as an
   item after B8: "Residue field finite, K/Q_p finite, Π^(p′) the maximal prime-to-p quotient. Under good marked
   reduction, prove that the outer action of G_K on Π^(p′) factors through G_k and is the action of Frobenius on
   the prime-to-p fundamental group of the special fibre, acting on each cusp group by the q-th power, q = #k; for
   split stable reduction determine the image of the tame inertia ∏_{ℓ≠p} Z_ℓ(1) in Out(Π^(p′)) and prove the
   analogue of F17.6 (i), (ii) for the node groups. Prove or refute the analogue of F17.7 with G_k = Ẑ: the action
   of Frobenius through a splitting is that of a smooth curve over k if and only if the reduction is potentially
   good; the weight argument of F17.6 is not available as written, since AE1 uses the cyclotomic kernel of a field
   finitely generated over Q. Reference for the rank-one case: Connes–Consani, arXiv:2501.06560, Prop. 3.4,
   Prop. 4.1, Thm 4.2; CYCLOTOMIC_KERNEL D14." And the lead for C3: "for K = Q_p, G_{K(μ_∞)} is the stabilizer in
   the cyclotomic kernel of G_Q of a place over p."

## 2. LM6 (unsent)

A second "New since" block is needed, for FLAGGED_149. Where it bears:

- **Part A (e), F (c).** ZCF5 restates the précisions; nothing new beyond CYCLOTOMIC_KERNEL.
- **Part B (a).** Done there: the local extension and its torsor (F10a), the packets (F10b, known; F10c for
  (0,2)), the class of the normalizer extension, c_1 of the normal line with the sign fixed (C6), the splitting
  criterion (C7), O(S)^* inside its completion (C8), tangential specialization and the change of uniformizer
  (C9), the intersection formula κ_q ∘ [μ] and the five conditions of scan 90 (C3). What remains of B (a) is the
  comparison with Deligne's tangential base point, the fibres in the extension by π^ab, and the norm of 1-forms.
- **Part B (b).** B1, B2 (Théorème 3 in his generality), B5 (polycurves, π^Γ = 1); in characteristic p: B6 (full
  groups), B7, B8, B10; open: B9.
- **Part F (b).** (1) is ZCF5 again. For open homomorphisms: ZCF1 (known: Mochizuki 17.1) and ZCF4, a
  non-dominant closed immersion H ⊂ C³ inducing an isomorphism of fundamental groups over G_Q. Any sentence of
  F (b) that asks for "open image ⟹ dominant" with a target of dimension ≥ 2 is refuted by ZCF4 and is to be
  replaced by the curve-target form (Mochizuki 16.5).
- **Part F (d).** ZCF12 (continuous B′ is B, proved in full), ZCF8. Open: ZCF6 (4).
- **Part F (e).** D4, D5, D10 (inertia, normalizers), ZD5 (the uniqueness clause of conjecture a) is false for
  valuations of rank ≥ 2), ZD6, D9; ZD11: conjecture b) for all curves over all finitely generated fields is
  equivalent to the section conjecture (Bresciani). Open: ZD10, ZCF6 (2), (3).
- **Part F (f).** GOOD_REDUCTION: F17.1–F17.8, as in §1.
- **Part F (g).** (1) is C7, C8. (3) is proved in my map (note L6) in three lines.
- **Part C.** A1 (cd, the real exception), A2 (τ, known).

**My map's sentences, revised now that FLAGGED_149 has returned.**
- The three sentences addressed to FLAGGED_149 move to LM6. F2 (reference): unchanged, to LM6 C (b), (c). F8
  (corollaries): A9 of the return proves E ≅ Aut(P) ×_{Out(P)} Γ for every extension with Z(P) = 1, with its
  topology; so the sentence for LM6 F (d) becomes: "By FLAGGED_149 A9 and F8a, G_Q ≅ Aut(Γ°) ×_{Out(Γ°)} Ẑ^* and
  Ẑ^* → Out(Γ°) is injective. Prove: for every number field K the sequence 1 → Γ_K° → Γ_K → χ(Γ_K) → 1 has no
  continuous splitting over any open subgroup of χ(Γ_K) (A2: no element of odd order); determine the classes of
  sections of E_U over Γ_K° that extend to Γ_K as the classes fixed by χ(Γ_K) on which an obstruction class
  vanishes, and compute that class." F14–F15 (ideles): C7 and C8 prove the frame; the item "(3 bis)" for LM6
  F (g) stands as written in the map.
- LM6 B (f), A (d), C (b), (c): unchanged.
- LM8 (E3): unchanged.

## 3. A FLAGGED_149 push prompt: the four items

Each item is one open statement of the return, with what is proved, the inputs to attach and leads. Leads are
mine, unverified.

**P1 = B9. Point sections in the geometrically prime-to-p group.**
*Target.* For every smooth proper geometrically connected curve C of genus ≥ 2 over a finite field k of
characteristic p and all P ≠ Q in C(k): the point sections of P and Q in π_1(C)/ker(Δ → Δ^(p′)) are not
conjugate under Δ^(p′); equivalently the exceptional set of Saïdi–Tamagawa is empty; equivalently some finite
étale cover with geometrically prime-to-p Galois closure has non-isomorphic Frobenius-sets over P and Q. Or a
curve and a pair for which they are conjugate, with the proof. With it, his sentence of scan 36 (compatible
p-primary differences on all prime-to-p covers force P = Q).
*Inputs.* B6–B8, the reductions (a)–(c) of B9, B14, B15, the genus-2 analysis: Q̃ = (Q, b) the only possible
lift, [8] = Σ_H r_H^* r_{H*} − 7π^*π_*, K_2 ⊂ J_Z[8], π^*J_C[8] ⊂ K_2; Saïdi–Tamagawa 2009 Prop. 1.8, Cor. 1.11
and 2017 Thm 1.9; the programs F7_test and F7_test5.
*Leads.* (1) Genus 2, odd p: compute K_2 exactly (is it π^*J_C[8]?) and decide whether a class
p^a[Q̃ − P̃] can lie in it: apply π_* (it gives 16x = p^a[Q − P]) and the 35 quotients by subgroups of index 4.
(2) The same with Z_ℓ = C ×_{J,[ℓ]} J for every prime ℓ ≠ p: the lift is (Q, ℓ^{-1}[Q − P]), and the incidence
identity for the hyperplanes of F_ℓ^{2g} is Σ_H N_H = ℓ^{2g−1} + c·N_G, so the joint kernel of the norms to the
quotients of degree ℓ is killed by ℓ^{2g−1}. Compare the residual classes for two primes ℓ, ℓ′ on the common
cover Z_{ℓℓ′}, and prove or refute that they cannot both be nonzero.
(3) A collision makes the Frobenius elements of P and Q equal in every finite quotient, so for every lisse
ℓ-adic sheaf on C whose geometric monodromy group has all finite quotients of order prime to p, the fibres at P
and Q are isomorphic Galois modules. For an abelian scheme A → C′ over a prime-to-p cover C′ and ℓ of
multiplicative order > 2 dim A modulo p, this makes A_P and A_Q isogenous (Tate). Kodaira–Parshin families
(covers of C branched at the moving point and its image under a fixed-point-free automorphism of a cover) give
fibres whose point counts can be compared by program: a finite test for each pair, valid when p > 2g′ + 1 for the
fibre genus g′. (4) Reduce "empty" to "finite with a bound independent of the cover": by (c), |E_V| = d|E_U|, so
any bound on |E_V| that grows more slowly than the degree gives emptiness; look for one through gonality (a class
of order N gives a map of degree N to P¹ from the cover).

**P2 = ZCF6. The existence assertions.**
*Targets.* (1) Every section of π_1(P¹ ∖ {0,1,∞}) → G_Q with C_Π(s(G_Q°)) = 1 is the section of a rational
point. (2) Every section of G_{Q(t)} → G_Q lies in the decomposition group of a rational place. (3) Every section
of a hyperbolic curve lifts compatibly through π_1(U ∖ D) → π_1(U) for all finite D. (4) Conjecture B′ for
abstract semilinear actions of G_Q on the universal pro-cover of P¹ ∖ {0,1,∞}, or an action normalizing no deck
group of a finite quotient.
*Inputs.* ZCF5, ZCF12, CYCLOTOMIC_KERNEL D0b, B7, D4, D13; ZD11 (Bresciani A, B: (3) over all finitely generated
fields is the section conjecture); ZCF7 (all fail over Q(μ_∞)); Mochizuki 16.5 and 17.1; the tool (T1) of LM6
(the p-adic section conjecture claimed by OpenAI, 6 October 2026, unrefereed) and Koenigsmann for the birational
p-adic case; Harari–Stix and Stoll (finite descent).
*Leads.* (1) With (T1) and the real case, s is locally a point or a cusp at every place; s lifts to exactly one
twist a·uⁿ + b·vⁿ = c·wⁿ of each Fermat cover; for n = 4 the twisted quartics have elliptic quotients, and where
one of them has rank 0 Stoll's theorem makes the finite descent set equal to the rational points: prove (1) for
all sections whose twist class meets that condition, then describe the twist classes left. (2) The section
defines ev_s : Q(t)^* → Q̂^* (pull back Kummer classes), with local components κ(f(x_p)) at the Koenigsmann
points x_p. By the idele decomposition lim_n A_Q^×/n = Q̂^* × Ẑ^* (map, note L6), ev_s(f) ∈ Q^* as soon as
v_p(f(x_p)) = 0 for almost all p: prove this integrality for f = t − c, then recover x from c ↦ ev_s(t − c).
(3) By ZD11, (3) for U over Q(t) implies (1): work the other way, from (1) for the covers. (4) Write
ρ(g) = a_g ρ_0(g) with the cocycle identity of ZCF6; an action with an infinite orbit on a field generator must
move it through infinitely many levels: construct a_g from a discontinuous automorphism of Q̄ acting on the
tower's constants, or prove that every abstract action has open stabilizers (automatic continuity for G_Q acting
on a countable field is false in general, so look first for a counterexample).

**P3 = ZD10. Lifting sections to the function field.**
*Target.* For U = P¹ ∖ {0,1,∞} over Q: every section of π_1(U) → G_Q lifts to a section of G_{Q(t)} → G_Q; and
(a) of scan 126 without its uniqueness clause: every section of G_{Q(t)} → G_Q lies in D_v for a rational place.
*Inputs.* ZD3, D4, D5, D10, ZD5, ZD11, CYCLOTOMIC_KERNEL B7–B9; Bresciani (Theorems A, B); Borne–Emsalem–Stix
Thm 27; Stix on the birational conjecture with local conditions.
*Leads.* The second half is P2 (2). For the first: the extension E_s = G_{Q(t)} ×_{π_1(U)} G_Q has kernel
generated by the inertia groups of the interior points (ZD3); a splitting exists iff every finite embedding
problem for E_s is solvable compatibly; G_Q is not projective, so the obstruction is local–global: solve over
each Q_p by (T1) (a local point or cusp gives a local lift through D_v) and measure the global obstruction in
the abelianized kernel, a product of induced modules Ẑ(1) over the closed points of U, whose H² is controlled by
Poitou–Tate. By ZD11 a proof for all base changes Q(t_1, …, t_n) is the section conjecture for U.

**P4 = Z142g. The later programme of cote 142.**
*Targets.* (i) A positive-characteristic version of the category (Z.2) with finite-cover factorization, path
transport and base-extension equivalence, or a proof that no category has the three properties when wild covers
are admitted. (ii) An intrinsic description of the completed category of all types and the image of the action
of Aut(k) of Z142d. (iii) A definition of the isotopy relation for the category generated by finite étale maps
and puncture fillings, and a completion theorem for it.
*Inputs.* G4, G6–G10, Z142a–Z142f, in particular Z142c (y^p − y = tx) and Z142e (the path f_t); Bertin–Romagny
6.9, 6.14, 6.20; Noohi 20.4; Bresciani A.22, A.23.
*Leads.* (i) Z142c gives covers in continuous families, so Hom sets depend on k: prove the impossibility in
exact form, then construct the tame category (prime-to-p Galois closures, Hurwitz stacks over Z[1/|G|]) and its
specialization functor from characteristic 0. (ii) The automorphism group of the completed category restricted
to types (0,4) and (0,5) with the puncture-forgetting functors of Z142f: prove that it maps to the
Grothendieck–Teichmüller group and that the action of G_Q factors through it injectively (Belyi); whether the
image is everything is the question GT = G_Q, which target (ii) as he wrote it contains.
(iii) Two candidates: isotopy inside a stratum of fixed incidence data (the corrected statement of Z142e), and
the relation generated by paths through étale maps (which identifies f_0 and f_t). For the second, the space of
étale maps of given combinatorial type fibres over a configuration space of Y; compute its fundamental groupoid
as an extension by a surface braid group and prove that the completed Hom spaces are the double-coset spaces of
the profinite completions.

## 4. Order

1. The source check of F17.6 (agent).
2. GOOD_REDUCTION rewritten as in §1, then sent.
3. LM6 with the two "New since" blocks.
4. The push prompt: P1 is the item most likely to close; P2 (1)–(3) and P3 are the section conjecture and its
   equivalents, and under the no-stopping rule a prompt that contains them does not end before they are decided.
