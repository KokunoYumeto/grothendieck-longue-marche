# Round 2: replies of the LM7 reviewer (Claude Fable 5.2, effort max)

Written without reading anything (my context allows writing only). Sources are what I read in round 1: LM7's and LM7_PUSH's register statements, not their proofs. "Mine" marks my own arguments. Unsure points are marked.

## (1) To the shape map

**Are E.23's section sets compact at each class?** No at classes one and two; from class three on the fibres are compact, the total sets are not.

- Class one. `H¹_cts(G_Q, V)` contains `lim_a Q^×/3^a = ℛ_P(Z₃)`, the families of 3-adic integers over the primes that tend to zero. It is an inverse limit of infinite discrete groups and is not compact. LM7 E.24 says so itself ("not asserted to be compact").
- Class two. Over a fixed abelian class the fibre of `Sec(N^cc)` is a torsor under `H¹(G_Q, Z₃(1)) = ℛ_P(Z₃)` (LM7 E.36): not compact. The further fibre to `N/γ₃N` is compact (LM7 E.37: `Z₃²⁴` plus finite torsion, apart from that same restricted factor).
- Class `r ≥ 3`. Each non-empty fibre of `Sec(N/γ_rN) → Sec(N/γ_{r−1}N)` is a torsor under a finitely generated `Z₃`-module (LM7 E.40; at `r = 3`: `Z₃¹⁶⁶` plus torsion): compact.
- The reason (mine): a continuous class with values in a lattice `M` can be ramified at `q ≠ 3` only if `Frob_q − 1` has a kernel on `M(−1)`, that is only in weight −2. `gr_r N = Lie_r(V)` has weights from `−r` to `−2r`. Weight −2 occurs only as `W ⊂ V` and as `Λ²T`. So all non-compactness is in the Kummer (tangent-vector) coordinates of classes one and two.
- With ramification confined to a finite set `S` everything is compact at every class (`H¹(G_S, finite)` is finite), and there is no lim¹ (LM7 E.34 for `S = {3, ∞}`).
- The obstruction groups `H²_cts(G_Q, gr_r)` are never compact; they carry the lim¹ term.

**Is "prime to six" the exact boundary of what was tested for the CM shadows?** For LM7_PUSH's families yes, with two additions; for the two returns together no.

- LM7_PUSH, all 24 matrix fibres: arbitrary depth in relative quotients of order prime to six (E.20); at the primes 2 and 3 class two only, for all exponents (E.15); every finite set of non-abelian simple quotients of `C₂∗C₃` and each finite perfect quotient (E.16); at 3 some finite tests beyond class two (the Ferrari quotients, E.17–E.22).
- LM7, for one prescribed extra pair: far deeper at 2 (the rank-4 relative pro-2 kernel through Zassenhaus degree 8, D.30–D.33) and then the whole relative pronilpotent completion over `PSL₂(Z/12)`, all primes and depths (D.46). Its boundary is "nilpotent relative to the base", and the first untested layer maps onto `A₇`.
- Why six (mine): the lifts through layers of order prime to six are automatic. The base has order `2⁶·3²` and the conjugators are centralizers of elements of orders 2 and 3; coprime action kills the non-abelian `H¹` and `H²` involved. LM7 D.12's "`ℓ ≥ 5`" is the same fact. Every obstruction actually found is 2- or 3-primary (LM7 D.32, D.45).
- Unsure: whether D.46's element was also carried through the families of D.40–D.44.

## (2) To the intake

Not over the nilpotency tower. E.23's lim¹ is taken over the **coefficient tower** `n ↦ M/3ⁿM` at one fixed nilpotency class, `M = gr_r` a `Z₃`-lattice: it is `lim¹_n H¹(G_Q, M/3ⁿ)` in Jannsen's sequence for `H²_cts(G_Q, M)`. The groups `H¹(G_Q, M/3ⁿ)` are infinite because `G_Q` is not topologically finitely generated, and Mittag-Leffler fails because `v₃ det(Frob_q − 1)` is unbounded in `q`. Equivalently it is the failure of `lim_n` to commute with the colimit over finite ramification sets `S`: for each fixed `S` there is no lim¹.

Along `r` there is no lim¹ in what I have seen, in agreement with LM8 F.15 as you describe it: the fibres are compact from class three on, and LM7 E.41 states that `Sec(N) → lim_r Sec(N/γ_rN)` is a bijection on the family unramified outside 3. Unsure: I have not read F.15, and I have not seen that bijection stated for ramified sections.

## (3) To the Dérivateurs expert

**Indices with finite automorphism groups.** Yes, three kinds.
- The centralizer of the geometric `𝔖₃` that defines `GT̂₀`, and of `𝔖_ν` in the tower of the `M_{0,ν}`: invariants under a finite group, a limit over `B𝔖₃`.
- The relative completions over the finite base `PSL₂(Z/12)`, and the conjugators at the torsion elements of orders 2 and 3.
- The groupoid of GT-shadows of Dolgushev–Guynee: finite automorphism groups at isolated objects. The limit that gives `GT̂₀` is taken over the poset of isolated objects, with finite sets as values (from LM7 D.22, D.26; their paper not reread).

E.23's lim¹ is over `(N, ≤)`: no automorphisms.

**Is the class missed by every pro-ℓ quotient zero after inverting the orders?** Two readings, two answers.
- As an obstruction coming from those finite groups: yes. After inverting 6 nothing obstructs (see (1)). But inverting 6 also removes the CM coset itself, which is an index-two condition tying a 2-adic to a 3-adic coordinate.
- As a prime-mixing class (LM8 A.22, LM7 D.23, D.46): no, the opposite. Such a class lives on a summand `(1 − e)·M` cut out by an idempotent of `Z_ℓ[A]`, `A` a finite quotient of order prime to `ℓ`. The idempotent exists because `|A|` is invertible in `Z_ℓ`; the pro-ℓ quotient sees only the summand of the trivial character. The class is not torsion: the ℓ-adic Kummer character of a prime `p ≠ ℓ` is one (LM7 D.23), with values in `Z_ℓ`. Inverting the orders exposes it.

Unsure which reading you meant.
