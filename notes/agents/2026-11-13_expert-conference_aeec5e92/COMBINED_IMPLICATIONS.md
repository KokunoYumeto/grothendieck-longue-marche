# Combined implications: what the field now knows

Draft for sign-off. Drafter: the shape-map successor (Claude Fable 5.2, effort high; author of Revision 4 of
`braindump_board\SHAPE_MAP_REVISION_20261113.md`). 13 November 2026, 14:15 UTC (machine clock).

**Read for this draft.** AGENDA.md; the five round-1 talks (shape map, Dérivateurs expert, LM7 reviewer in full;
intake §§3–5; EXIT reviewer §§4–7 and its section heads); the five round-2 replies (shape map, intake, EXIT
reviewer in full; Dérivateurs expert and LM7 reviewer with long lines cut at 900 characters); the five floor
questions; the three floor answers present at 14:17 UTC (`shape_map_Q3_answer_intake.md`,
`shape_map_Q2_answer_EXIT_reviewer.md`, `shape_map_Q2_Q3_answer_LM7_reviewer.md`); MINUTES.md (round 1;
no round-2 minutes yet); NEXT_PROMPT_ITEMS.md with its status note; the part headings and Part A of the drafted
FRAISSE_EXACT prompt; the heads of the four new LM4 statements in `LM4_DIFF_1314Z_to_1347Z.md`.
**Not read:** `REVIEW_MAIN_PROOFS_TOTEX2.md` (cited below from the status note that reports it); the EXIT reviewer's
§§1–3 beyond their opening lines; the body of the FRAISSE_EXACT prompt.

**Status marks.**
- **[R]** proved in a return, and the proof read by a participant (named, with how far).
- **[P]** proved here by a participant; "no second reader" unless a second is named.
- **[C]** claimed: a return's statement, read at statement or report level only.
- **[Lit]** a statement of the literature; "opened" with the reader, or "not opened".
All returns are GPT-6 Astra (ChatGPT Pro mode), unrefereed. Row ids: T = TOTAL_EXACT_2, L = LM8, PUSH = LM7_PUSH,
LM7, LM4, CK = CYCLOTOMIC_KERNEL, P… = EXIT_ONE_TYPE, R4 = Revision 4 of the shape map.

## A. Index categories: exactness, totality, amenability

1. **Duality.** For M: A → Ab, lim^i over A^op of Hom(M, R/Z) = Hom(T_i(M), R/Z). So colim_A is exact iff lim¹ over
   A^op vanishes on diagrams of compact abelian groups. **[P]** intake (I1), second reader: Dérivateurs expert;
   adopted by the shape-map agent. Standard.
2. **C_δ is total and not exact.** T₁(Q_R) ≅ R for every ring R ≠ 0, for the three vertex arrows V → W.
   Rows T A.1, A.21, A.24, A.30–A.34. **[R]** intake (effort high, every step); the Dérivateurs successor at effort
   max (reported in NEXT_PROMPT_ITEMS.md: A.21, A.24, A.30–A.34, C.25–C.28 all correct; its review file not read by
   the drafter).
3. **filtered ⊊ exact ⊊ total ⊊ quasi-filtered**, witnesses Δ_inj, C_δ, K*. Rows T D.1, A.34, C.28. **[R]** as in 2.
4. **Each class is an exactness property of colim_A for one kind of coefficients**: filtered for diagrams of
   categories or groups; exact for abelian groups (⟺ Aff_Z(A) filtered, Isbell–Mitchell); total for sets or
   simplicial sets; quasi-filtered for the same up to π₁. Rows PRETOT F.4, TOTASPH C.5, TOTEX A.4, B.5–B.6.
   **[P]** Dérivateurs expert, from those rows; no second reader in the conference. Isbell–Mitchell **[Lit]**, not
   opened.
5. **A is total iff A is non-empty, connected, and every connected presheaf on A^op is aspherical.** Hence B a weak
   test category ⟹ B^op not total; Δ° is not total. **[P]** Dérivateurs expert ("an unfolding of definitions").
6. **Three compact-limit properties of an index A with common successors.**
   - (CH) every A^op-diagram of non-empty compact Hausdorff spaces has a point ⟺ finite-pattern Ramsey. Row T A.13.
     **[R]** intake.
   - (CAb) lim¹ over A^op vanishes on compact abelian groups ⟺ exact. Line 1.
   - (CC) every A^op-diagram of non-empty compact convex sets with affine maps has a point.
   - (CH) ⟹ (CAb): rows T A.6, A.14. **[R]** intake.
   - (CC) ⟹ the Reiter property (R). **[P]** Dérivateurs expert (Sion's minimax); second reader: intake ("I agree
     with it").
   - (R) ⟹ (CC). **[P]** intake, a sketch with the convolution step named; unwritten; no second reader.
   - (CC) ⇏ (CAb): BZ; FI over Z. **[P]** Dérivateurs expert.
7. **T A.18 is the failure of (R) for C_δ, with gap 1**, uniformly in the target. **[R]** intake. **Aut(M_δ) is not
   amenable.** **[P]** intake; second reader: Dérivateurs expert ("complete as written and I checked each step").
   Independently R4 2.3 (minimax and Moore's condition with two colourings; the drafter's, no second reader; it
   needs the closed embeddings made into embeddings by an expansion of the language).
8. **FI (finite sets, injections): Q-exact; F_p-exact for no p; not total, with El_FI(2-subsets) ≃ B(Z/2).**
   **[P]** three derivations that agree: shape-map agent (p = 2), Dérivateurs expert (every p), confirmed by the
   intake; R4 L1 gives the general form (line 12).
9. **BZ has the Reiter property and H₁(Z; R) ≠ 0.** So (R) does not give Q-exactness without finite hom-sets.
   **[P]** Dérivateurs expert; conceded by the intake and by the shape-map agent.
10. **"colim_A exact iff Aut(M) amenable" (N2, P1 (b)) is false over Z as written.** From 8. Agreed by the
    Dérivateurs expert, the intake, the shape-map agent and R4.
11. **Finite extensions of pointwise stabilizers.** If G_F ⊴ U with Γ = U/G_F finite, then T_{G/U} ≅ A(F, −)/Γ and
    El_A(T_{G/U}) ≃ BΓ. **[P]** Dérivateurs expert (round 2); no second reader. Conditional consequence, granted the
    intake's statement that sheafification is homotopy final and weak elimination of imaginaries: total ⟺ every
    open subgroup is a pointwise stabilizer ⟺ quasi-filtered.
12. **R4 L1.** If an object B has an automorphism of prime order p acting freely on every A(B, C), colim_A is not
    exact over F_p. **[P]** drafter; no second reader. It is the Dérivateurs expert's pair (id, p-cycle) for a
    general index. So a Z-exact age with monic arrows consists of rigid structures.
13. **R4 L2.** Under the extension property for partial automorphisms every finite parallel family has a rational
    affine equalizer (average over Aut(c) for an EPPA-witness c). **[P]** drafter; no second reader. The same
    conclusion is Lead 5 (a) of the drafted FRAISSE_EXACT prompt (Dérivateurs successor).
14. **R4 L3.** For the age K_E of finite sets with an equivalence relation and an independent linear order: the
    arrows α₁ = (x₁, y₁), α₄ = (y₁, x₂) from two inequivalent points to x₁ < y₁ < x₂ < y₂ (x's equivalent, y's
    equivalent) have no affine equalizer over any ring in which 2 is not invertible; colim is not exact over Z or
    F₂. **[P]** drafter; no second reader. The age is rigid. That its group is amenable and not extremely amenable
    is from memory of the Kechris–Pestov–Todorcevic theory. Q-exactness: a sketch only.
    - It is the candidate the Dérivateurs expert named as the test of C1; it does not refute C1.
    - It is a rigid amenable age that is not Z-exact; the intake's open test 3 (not Q-exact) is not decided by it.
15. **The literature behind 6 and 7, now opened.** Kechris–Pestov–Todorcevic: for an order class, Aut(M) is
    extremely amenable iff the class is Ramsey. Moore: Aut(M) is amenable iff the age has the convex Ramsey
    property, in six equivalent forms, one with finitely many colourings. Evans–Hubička–Nešetřil 1801.01165: for
    Hrushovski's sparse graphs Aut(M₀) and Aut(M_F) are not amenable and have no precompact Ramsey expansion, and
    the paper says the same holds for general predimension constructions. **[Lit]** opened by the drafter (R4 1,
    2.3), statements only. In round 2 these were "from memory for all three of us".
16. **Finality, truncated.** A functor with n-connected comma categories induces isomorphisms on π_i (i ≤ n) and on
    lim^k (k ≤ n) and an injection on lim^{n+1}. For an inclusion of directed posets the comma categories are empty
    or contractible: if none is empty every lim^k agrees; if one is empty lim⁰ already differs. **[P]** Dérivateurs
    expert (round 2); no second reader.
17. **"Invisible to sizes" is two statements.** (S-a) Boundedness kills the class: T A.20 (|M(a)| ≤ N over a
    quasi-filtered index), PUSH F.3, L F.20. (S-b) The sizes of the stages do not determine the class: PUSH F.4.
    **[P]** shape-map agent (round 2), as a reading; (S-a) rows **[R]** intake (A.20), drafter (F.3). (S-b) over C_δ
    is open (floor shape_map_Q1).

## B. Towers and derived limits (La Longue Marche)

1. **LM7 E.32.** H²_cts(G_Q, Z₃(2)) ≅ ℛ/dℛ, d = diag(q − 1) on families tending to zero; a pair of Kummer classes
   has a class-two section iff the corrections c_q are integral and tend to zero; the obstruction can vanish at
   every finite coefficient level and every place and be non-zero. **[R]** shape-map agent (the whole proof,
   Revision 1); statement re-read by the drafter.
2. **L F.15.** H¹_cts(G, lim P_n) → lim H¹_cts(G, P_n) is onto always, bijective for compact P_n and for rational
   BCH towers; it fails for Z ⊕ Z/2ⁿ, with H¹ = Z₂/Z = lim¹(2ⁿZ). **[R]** intake; the drafter (surjectivity and the
   compact case).
3. **L F.21.** H²_cts(G_Q, Z₅(2)) = 𝒞(I)/D𝒞(I), D = diag(5^{e_q}); a cup product that is zero at every finite level
   and non-zero integrally obstructs an actual pair of sections. **[R]** intake (with the eight primes recomputed).
4. **PUSH F.1–F.3, the vanishing criterion.** For a finite-rank Z_ℓ-lattice M unramified outside S:
   lim¹ H¹(G_L, M/ℓⁿ) = 0 ⟺ the tower P_n is Mittag-Leffler ⟺ the valuations of the non-zero Smith entries of
   D_v = Frob_v − 1 on M(−1) are bounded ⟺ the residue invariants modulo their divisible parts have bounded
   orders. **[R]** drafter (R4 2.2 a: every step followed, no gap found; not a referee's check). The LM7 reviewer
   had it at statement level.
5. **PUSH F.4** (Z₃(1)² and Z₃(1) ⊕ Z₃(2): the same orders, different lim¹) and **PUSH C.7** (the phantom group is
   torsion-free, and the class survives every finite extension because cor ∘ res is the degree). **[R]** drafter.
6. **R4 2.2 (b).** lim¹ H¹(G_L, M/ℓⁿ) = 0 iff G_L acts on M(−1) through a finite group. **[P]** drafter, from line 4
   and Chebotarev; no second reader. It agrees with PUSH F.5 and with the LM7 reviewer's reason for compactness
   (ramification at q ≠ 3 needs a kernel of Frob_q − 1 on M(−1), that is weight −2).
7. **Where E.23's lim¹ lives.** Over the coefficient tower n ↦ M/3ⁿM at one fixed nilpotency class, M = gr_r; the
   index is the pair (n, S) with a colimit over the ramification sets S inside; for each fixed S there is none.
   Along the nilpotency tower r there is none (line 2). Agreed in round 2 by the LM7 reviewer, the shape-map agent
   and, by its question being answered, the intake; R4 2.2 (e). This closes conflict 2 of the round-1 minutes.
8. **Compactness of E.23's section sets, class by class.** Classes one and two: not compact (Kummer coordinates;
   LM7 E.24, E.36). Class r ≥ 3: each non-empty fibre is a torsor under a finitely generated Z₃-module (LM7 E.40);
   the total sets are not compact. With ramification in a finite S everything is compact (LM7 E.34).
   **[C]** LM7 reviewer, from register statements, with a reason of its own.
9. **Descent along the cyclotomic tower.** For finite 3-primary M_n: H²(G_Q, M_n) = H¹(Γ, H¹(Δ₃, M_n)), the
   Γ-coinvariants, with Δ₃ = G_{Q(μ_{3^∞})}, Γ = Gal(Q(μ_{3^∞})/Q). **[P]** LM7 reviewer (sketch); second
   derivation: drafter (R4 2.2 d), from cd₃ Δ₃ ≤ 1 (Serre, CG II §3.3, **[Lit]** not opened) and
   Hochschild–Serre. The limit statement (the lim¹ class is the non-Hausdorff part of the coinvariants of
   X = lim X_n; X is not finitely generated over Z₃[[Γ]] when all ramification is allowed) is the reviewer's,
   unwritten: open.
10. **Class two selects nothing geometric; selection begins at class three and locally.** LM7 E.37, E.38, E.43,
    E.44, E.61, E.66; PUSH A.3–A.6, A.8, A.11, B.2, B.4. **[C]** LM7 reviewer, statements only.
11. **No finite-precision procedure decides the vanishing** (PUSH A.11, A.12). **[C]**.

## C. Prime mixing: pro-p against profinite

1. **L A.22.** F̂₂/F̂₂″ has a non-inner pure peripheral involution with multiplier one, acting on F′/F″ by 1 − 2e,
   e the idempotent of a Z₅[ζ₃]-component; e maps to 0 in every pro-ℓ quotient. **[R]** intake (re-derived).
2. **It commutes with the geometric 𝔖₃ in Out(F̂/F̂″)**; more generally the outer classes trivial on the
   abelianization form (1 + I)^×/F̂^ab, and conjugation by 𝔖₃ acts on the multiplier λ. The pentagon is not
   addressed. The three special directions of weight 5 are reached through the principal block, not through e.
   **[P]** intake (round 2; "conventions on units unchecked"); no second reader.
3. **The form of the failure for elements and automorphisms: degree zero.** The family of maximal pro-ℓ quotients
   is not final among the finite quotients; the missing part is a block (ℓ, χ) with χ of order prime to ℓ. Agreed:
   intake, LM7 reviewer (its lemma R13: limits of finite sets have no lim¹), R4 2.4; the invariant is an empty
   comma category (A 16).
4. **The form for sections: a twisted H¹.** At the order-75 quotient Q = V ⋊ C₃: the image of N is V; every section
   modulo V lifts; the lifts of a section with cocycle c are a principal homogeneous set under H¹(G_k, E_c[5]),
   E_c the cubic twist of the j = 0 curve y³ = x(1 − x), and this group is not zero; over L = k(E_c[5]) it is the
   block e of class field theory. So both readings hold: first-derived over k, degree zero over L, and for
   sections the twisted H¹ carries the open statements. **[P]** intake (`shape_map_Q3_answer_intake.md`); by hand;
   no second reader; the identification of the cover and of V with E[5] is marked unchecked there. It answers
   floor question shape_map_Q3 and closes conflict 3 of the round-1 minutes, subject to sign-off.
   - The LM7 reviewer's answer agrees on the two levels: for automorphisms of the order-75 group the object is a
     unit of the equivariant endomorphism ring of F₂₅ (outer automorphisms over C₃: F₂₅^×/μ₃, of order 8; the
     involution is −1 = 1 − 2e), and H¹(C₃, F₂₅) = H²(C₃, F₂₅) = 0; the twisted H¹ is the right form when a section
     or an element is lifted (CK D15, L G.20). **[P]** LM7 reviewer, from memory; "unsure" on whether L A.22's
     involution acts by −1 on the order-75 quotient.
   - For PUSH E.2's open survival of the CM shadows the reviewer says neither reading applies as stated: the coprime
     layers are passed automatically (PUSH E.20, LM7 D.28); what is open is at the primes 2 and 3 beyond class two
     over non-nilpotent bases (LM7 D.32, D.45), a class with values in the relative kernel over PSL₂(Z/12). And
     PUSH C.11 is a pro-3 statement with no second prime, so it is not the smallest case of Q3. **[P]** LM7
     reviewer; the degree bookkeeping is marked unsure.
5. **LM4 D.26–D.30.** A torsion-free extension of F̂₃ by C₂ with multiplier −1 at the prime 3 and +1 elsewhere, with
   an invariant type (0,4) marking (D.29), and a closed genus-2 analogue (D.30): full profinite recognition is
   refuted, discrete and pro-p recognition proved. An endomorphism of F̂₂ that is an automorphism of every maximal
   pro-p quotient and is not surjective (image of order 3 in a quotient A₅). **[C]** drafter (report), LM7 reviewer
   (statements D.29–D.30).
6. **LM4 update (13:47Z): D.63–D.65.** For the full once-punctured-torus peripheral outer group Ω and a negative
   involution b: the centralizer has characters (σ, λ) with homology matrix (σ/2)((1 + λ)I + (1 − λ)A) (D.63); for
   the two standard negative involutions the centralizer is C₂² and equals the normalizer, and the multiplier takes
   only the values ±1 (D.64, D.65); c^r g is a square in Ĝ_n iff r ≡ 0 or −1 mod n (D.65b). The return does not
   assert that the two standard orbits exhaust the negative involutions. **[C]** drafter (statement heads only).
   Bearing: in type (1,1) these centralizers contain no mixed-prime multiplier, in contrast with D.29 in type
   (0,4). C.62 (the prefix-interval step behind C.12) does not touch the floor questions.
7. **The CM coset.** None of the twelve recorded extra shadows is genuine (LM7 D.27, PUSH E.9); each extra matrix
   pair has an affine space of shadows above it (PUSH E.10); they survive every relative quotient of order prime to
   six (PUSH E.11–E.16, E.20); LM7 D.46 is the surviving candidate. **[C]** LM7 reviewer. If the CM coordinates are
   a homomorphism on GT̂₀ (LM2 C.d4, to be confirmed), GT̂₀ reaches the extra coset at multiplier one iff it contains
   any element outside the Galois image. **[P]** LM7 reviewer; conditional; no second reader.
8. **"Is the class missed by every pro-ℓ quotient zero after inverting the orders?"** As an obstruction from the
   finite groups in the index: yes, after inverting 6 nothing obstructs. As a prime-mixing class: no, inverting the
   orders exposes it (the idempotent exists because the order is invertible). **[P]** LM7 reviewer (round 2).

## D. Germs, limits of topoi, exit paths

1. **L E.10, E.11.** The covering germs of a puncture are Z-sets with the tangent rays as fibre functors; the
   2-limit of the sheaf topoi of shrinking punctured discs is the empty topos. **[R]** intake; EXIT reviewer (step
   by step).
2. **A.** lim Sh(V_n ∖ Z) = Sh(K ∖ Z): the limit of sheaf topoi sees only the intersection. **B.** With compact
   stages the limit is right: lim Sh(τ⁻¹N_n) = Sh(τ⁻¹(x)). **[P]** EXIT reviewer; no second reader.
3. **E.11 on two levels (wording agreed in round 2 by the intake, the EXIT reviewer and the shape-map agent).**
   E.11 is first-derived at the level of the models of the stages and Mittag-Leffler at the level of their
   invariants: lim_n C_•(V_n ∖ D) = 0, R lim = lim¹[−1], and H_{j+1}(lim¹ C_•) = H_j((S¹)^{I(x)}); for topoi and
   cochains there is no class. **[P]** EXIT reviewer; checked by the shape-map agent (round 2) and accepted by the
   intake, which withdrew "degree zero, no class". The duality of A 1 does not give it on the nose (intake).
4. **The germ and i*Rj_*.** For F locally constant on U: i_x*Rj_*F = colim_n RΓ(V_n ∖ D, F) = RΓ(τ⁻¹(x), F) =
   RΓ(Λ_x, F_u). **[P]** EXIT reviewer. For a tower regarded as a sheaf on N ∪ {∞}: i*Rj_* = R lim, so lim¹ is H¹ of
   the boundary defect at the point at infinity of the tower. **[P]** drafter (R4 2.5); no second reader.
5. **The henselian case** needs two hypotheses: coherent stages with affine transition maps for the limit topos to
   be right; a closed point of a regular curve in residue characteristic 0 for it to be the classifying topos of
   Ẑ(1). **[Lit]** EXIT reviewer, from memory (SGA 4 VI 8.7, VII 5.7; numbering unsure); not opened.
6. **For the topological tower the homotopy limit is the common homotopy type**: holim_n Sing(V_n ∖ D) ≃
   Sing(τ⁻¹(x)); a tangential base point is a point of the homotopy limit. **[P]** shape-map agent (round 2); no
   second reader in round 2; in round 3 the EXIT reviewer answers "True" with grounds (polydiscs, the Milnor
   sequence, cofinality; from memory) and names the first check (the map on π₁ by winding numbers).
   - Arithmetic form (shape_map_Q2, statement 2): at a K-rational cusp c the continuous homotopy fixed points of
     G_K on the geometric punctured henselian neighbourhood, of type BẐ(1), have π₀ = the sections of
     D_c → G_K modulo inertia, a torsor under H¹(G_K, Ẑ(1)) = lim K^×/K^{×n}, with no lim¹ and with trivial π₁;
     the rational tangent vectors are the K^×-subtorsor, dense and strictly smaller. That these are the cuspidal
     sections needs the injectivity of packets (Stix, arXiv:0809.0017; Nakamura; Esnault–Hai). "True", on π₀, with
     these precisions: EXIT reviewer and LM7 reviewer, both from memory; **[Lit]** not opened in this round.
   - Statement 3: as worded it is true and empty (section classes are π₀ of the homotopy fixed points of the étale
     homotopy type; Quick's formalism, from memory). As intended it is the section conjecture with cusps: open in
     the full profinite type over a number field; **false** for the pro-3 completed type of the Fermat cubic minus
     its cusps over Q (LM7 E.34; PUSH B.2, B.5) **[C]** LM7 reviewer, statements; true for ramified local sections
     at v ∤ 3 (LM7 E.61, E.66) **[C]**; true over the reals **[Lit]** from memory.
7. **The two-level principle.** In discrete form it is in EXIT_ONE_TYPE: P5b1, P5c1, P5b2, P5b4. **[R]** EXIT
   reviewer. The profinite form is open (EXIT_TOWER Part D (c)). In the literature: Bakalov–Kirillov, the complex
   of decompositions with its moves and relations is connected and simply connected. **[Lit]** opened by the
   drafter (abstract only).
8. **Discrete against profinite.** H^q(Ĝ, M) → H^q(G, M) is bijective for q ≤ 1 and injective for q = 2 (Serre, CG
   I.2.6). **[Lit]** EXIT reviewer, not opened.

## E. The central statement of the shape map, as amended

1. **Statement.** The discrepancy between the objectwise data and the global object is carried by the cone of the
   comparison between the underived and the derived functor; the class is its lowest non-zero degree, fixed by the
   index and the coefficients. Over a tower, or for a module of projective dimension one, that degree is one; over
   K* with set coefficients it is two (T C.28); for exit paths it is r + 1 when the mapping spaces are
   (r − 1)-connected (P1d3). Proposed by the intake; adopted by the shape-map agent, the EXIT reviewer, the
   Dérivateurs expert and R4.
2. **Two coordinates** (shape-map agent, round 1, with D 3 added):

   | | compact coefficients | non-compact coefficients |
   |---|---|---|
   | directed index | no class (L F.15) | lim¹ = closure(im d)/im d (F.15's example, L F.21, LM7 E.32, PUSH A.1–A.4; E.11 on chains) |
   | non-directed index | a class with uniform gap: T₁ = R (T A.24) | not met in the returns |

3. **Four kinds of obstruction (R4 6).** A: a phantom class closure(im)/im along a one-parameter direction acting
   without a gap. B: a robust class of a non-directed index. C: degree zero, a non-final family or another block.
   D: honest finite-level classes (the real place; the tame and finite-depth obstructions; CK E3 against L G.10).
   **[P]** drafter, as a classification of the rows above; kind C is the LM7 reviewer's and the intake's finding.
4. **Rows where no class has been found, by the routes checked:** Weil positivity as λ → ∞ (positivity passes to
   the limit; Revision 2, B3); the Navier–Stokes force budget (Proj¹ of the restriction spectrum vanishes;
   Revision 2, A3); sums of squares after descent (H¹ of the deck group vanishes by averaging; Revision 1b).
   **[P]** shape-map agent.
5. **Each class is the image of a connecting map** (Milnor; the column D of T A.24; the Tate complex; the
   Bockstein; ∂π₂(X^log, τ⁻¹x)). **[P]** shape-map agent (round 2), following the EXIT reviewer's P1b1.

## F. From Revision 4, outside the five fields

1. **The obstruction in 't Hooft form.** A section of π₁(X) → G_k is a lift of the outer Galois action on the
   geometric group to an action; layer by layer the obstruction is a class in H². **[P]** drafter. Kapustin–Sopenko's
   anomaly index of a spin chain is the Eilenberg–MacLane obstruction for a homomorphism to automorphisms modulo
   inner ones. **[Lit]** opened by the drafter.
2. **Yang–Mills.** The committee's assessment of 10 November reports an ultraviolet limit at fixed volume, an
   infinite-volume limit along subsequences only, a decomposition into component theories, and Euclidean invariance
   by a symmetric gauge fixing, a Ward identity and decay of the stress-energy flux at infinity; uniqueness and the
   mass gap are open. **[Lit]** opened by the drafter (Part I). It bears on the conference only through E 3: the
   mass-gap question is of kind A for the time-translation group (Guichardet's criterion, not opened).
