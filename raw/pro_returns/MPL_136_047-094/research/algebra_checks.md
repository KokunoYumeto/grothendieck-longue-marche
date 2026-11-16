# Algebra checks after the transcription freeze

## Scope and status

This memo is research analysis, not a new reading of the manuscript. It uses the frozen LaTeX, principally scans 074–094, together with scans 048, 050, 060, 062 and 064 for the coefficient question. No image was consulted, and no change to a frozen reading is proposed. The calculations below are ours; they carry no claim of priority and do not automatically identify what Grothendieck intended at a doubtful place.

The context README and `notes/RESULTS_STATE.md` were read. The directly pertinent planning items are **README S11(i)**, the proposed ordinary integral cochain-model interpretation, and **WG2 §2.4 #5**, the proposed connection between integrality and divided powers. The other registered localizer/derivator results do not settle the algebraic questions below and are not used as established premises. Specific links with the supplied *Pursuing Stacks* text are recorded near the end.

## 1. The two gradings and the coefficient object

Use `p` for complementary degree and `q` for exterior/cochain degree, as in scans 074–080, and put `w=p+q`. Scan 081 changes to the pair **(total weight, exterior degree)**. Thus the weight-`w` complex is

\[
K_w^q=\Gamma_k^{w-q}\Phi\otimes_k\Lambda_k^q\Psi,
\qquad 0\le q\le w,
\qquad d:K_w^q\longrightarrow K_w^{q+1}.
\]

The inequality `j≤i` in the theorem on scan 081 means `q≤w`; it does not mean `q≤p`. The last term of a positive-weight complex has complementary degree zero, which matters for the acyclicity argument.

For an exact sequence

\[
0\longrightarrow L\longrightarrow\Phi\longrightarrow\Psi\longrightarrow0,
\]

the coefficient object resolved in weight `w` is `Γ^wL`. When a marked section trivializes `L≅k`, its distinguished generator is `T^{[w]}=γ_w(T)`, so `Γ^wL≅k`. Before such a trivialization, a locally free rank-one `L` gives the corresponding line coefficient `Γ^wL≅L^{⊗w}`; it should not silently be replaced by `k`.

The coefficient algebra in scans 080–083 is therefore `Γ_k(kT)=k{T}`, not just `k`. Already on the point topos, with `Φ=kT` and `Ψ=0`, the construction is `Γ_k(T)` in cochain degree zero. This example satisfies the relevant exactness/acyclicity requirements on a point and shows why the raw ungraded algebra is not an ordinary cochain model with `H^0=k`.

## 2. A proof of the algebraic resolution, with assumptions exposed

Here is a direct algebra argument. For a split sequence `Φ=L⊕P`, with `P` free, the complex is

\[
\Gamma_k(L)\otimes_k
\bigl(\Gamma_k(P)\otimes_k\Lambda_k(P),d\bigr),
\]

where `d` sends a generator of `P` in the divided-power factor to its exterior counterpart. In one variable `x`, each positive-weight summand is the two-term complex

\[
kx^{[n]}\xrightarrow{\;d\;}
kx^{[n-1]}dx,
\qquad d(x^{[n]})=x^{[n-1]}dx,
\]

whose differential is an isomorphism. For several variables, a fixed multidegree is a tensor product of these two-term complexes, with at least one contractible factor unless all the `P`-weights vanish. The surviving complex is `Γ_k(L)` in exterior degree zero; the same contraction survives tensoring with an arbitrary module. This is the elementary divided-power Poincaré-lemma mechanism; a general free-variable statement is also given by the Stacks Project, Lemma 60.20.1, Tag 07LB.

For modules over a ring, the nonsplit case with flat quotient `Ψ` reduces to that calculation. By Lazard's theorem, write `Ψ=colim_i P_i` with `P_i` finite free; form the pullback extensions `Φ_i=Φ×_ΨP_i`. Each extension `0→L→Φ_i→P_i→0` splits, and their filtered colimit is the original extension. Divided powers, exterior powers and finite tensor products commute with filtered colimits, which are exact in modules; consequently the weightwise complex resolves `Γ^wL`. This argument establishes the asserted exactness without treating a merely flat module as locally free. Lazard's theorem is the Stacks Project, Theorem 10.81.4, Tag 058G.

For sheaves on a space, or the relevant presheaf topoi, this can be checked at a conservative family of points/evaluations, provided the divided-power and exterior constructions are formed in the usual sheaf sense. An arbitrary topos without enough points requires the corresponding internal/local argument; this memo does not replace that argument by an assertion that every flat sheaf is locally free. Flatness of the terms and purity of the augmentation are a separate issue from their being acyclic for a sections functor.

## 3. What global sections compute, weight by weight

Assume the augmented weight-`w` sheaf complex

\[
0\longrightarrow kT^{[w]}\longrightarrow K_w^0\longrightarrow\cdots
\longrightarrow K_w^w\longrightarrow0
\]

is exact, and that `K_w^q` is `Γ(X,−)`-acyclic for `q<w`. These are the exact hypotheses needed here; the last term need not be acyclic. The hypercohomology spectral sequence

\[
E_1^{a,b}=H^b(X,K_w^a)
\Longrightarrow H^{a+b}(X,kT^{[w]})
\]

has no entries with `b>0` in columns `a<w`. Therefore its edge map is an isomorphism through total cohomological degree `w`. Equivalently,

\[
H^q\Gamma(X,K_w)\simeq H^q(X,k)T^{[w]}
\quad(0\le q\le w),
\qquad H^q\Gamma(X,K_w)=0\quad(q>w).
\]

The endpoint `q=w` is included: possible positive-cohomology contributions from the final sheaf begin only in total degree `w+1`. In derived-category language, the comparison identifies the weight-`w` global complex with `τ_{≤w}RΓ(X,k)` after fixing its coefficient generator. The analogous assertion for `f_*` requires acyclicity for that functor, not an unspecified use of the word flasque.

This proves precisely the triangular range stated in scans 081–082, under the stated assumptions. The phrase on scan 082, “un certain, tronqué du second”, is mathematically substantive. Each weight is a finite truncation; an individual positive weight is not a subalgebra, since products add weights.

All assertions above are componentwise in the weight grading. Interchanging global sections or derived global sections with an infinite ungraded direct sum needs an additional commutation hypothesis; the componentwise statement itself does not need that interchange.

## 4. Product compatibility includes binomial coefficients

The divided-power coefficient algebra satisfies

\[
T^{[w]}T^{[v]}=\binom{w+v}{w}T^{[w+v]}.
\]

This is the defining multiplication in a divided-power polynomial algebra (Stacks Project, Section 23.5, Tag 07H4). If the comparison to derived sections is taken with its natural multiplicative structure, and the flatness hypotheses justify the ordinary tensor products used to represent it, then for `q≤w` and `r≤v` the product is identified with

\[
(aT^{[w]})(bT^{[v]})
=\binom{w+v}{w}(a\smile b)T^{[w+v]},
\quad a\in H^q(X,k),\ b\in H^r(X,k).
\]

The target remains in the computed range because `q+r≤w+v`. Thus it is reasonable to speak of compatibility with products in the **weighted coefficient algebra**. It is inaccurate to replace this formula by an unqualified identification with ordinary cup multiplication on a single copy of `H^*(X,k)`.

Over a rational algebra, the alternative basis `T^w=w!T^{[w]}` removes the binomial coefficient. Integrally, that change of basis is not invertible. Multiplication by the marked `T` takes the weight-`w` copy to the weight-`w+1` copy by multiplication by `w+1`, rather than by an integral stabilization isomorphism.

## 5. Two decisive tests of the ordinary-model interpretation

These are tests of a stronger interpretation, not counterexamples to the weighted construction.

### 5.1 Strict alternation and real projective space

Assume a cochain DGA over `F₂` is strictly alternating, in the explicit sense that every odd-degree element squares to zero. Every odd cohomology class then has square zero. Since

\[
H^*(\mathbb{RP}^{\infty};\mathbb F_2)=\mathbb F_2[\alpha],
\quad |\alpha|=1,
\]

such a DGA cannot have its cohomology ring identified with the ordinary cup ring of this space. Graded commutativity alone in characteristic two is not enough for this argument; the odd-square-zero condition is essential. The projective-space ring calculation is Hatcher (2002, §3.2; Theorem 3.19 in the author's revised online section).

The weighted model avoids the contradiction. For a class `a_w` corresponding to `αT^{[w]}`, its square maps to

\[
\binom{2w}{w}\alpha^2T^{[2w]}=0
\quad\text{in characteristic two, for }w>0.
\]

But different-weight representatives need not have zero product: `a_1a_2` maps to `3α²T^{[3]}=α²T^{[3]}`. This is a concrete, nontrivial product test for the interpretation of scans 080–083. It also shows why identifying all weight copies before accounting for their transition maps would be destructive.

### 5.2 Divided powers and complex projective space

Assume an integral cochain DGA has compatible divided powers on an ideal containing every positive-degree cochain, with `dγ₂(x)=x·dx` for an even-degree element `x`. If a degree-two cocycle represents `u∈H²`, then `γ₂(x)` is closed and

\[
u^2=2[\gamma_2(x)].
\]

However, in `H^*(CP²;Z)=Z[u]/(u³)`, the element `u²` generates `H⁴≅Z` and is not divisible by two. Hence a single ordinary DGA with this divided-power-ideal hypothesis cannot reproduce that ordinary cup ring. Again the weighted formula has the required integer divisibility and is not refuted. This is an elementary consequence of the standard projective-space ring computation, not a novelty claim.

## 6. Setting the divided-power variable equal to one

Let `R=Γ_Z(T)`. The identity `T^n=n!T^{[n]}` implies that in `R/(T−1)` every factorial is invertible. Consequently every positive integer is invertible. Conversely the assignments `T^{[n]}↦1/n!` respect multiplication and define a map to `Q`; every generator of the quotient is forced to have precisely this value. Thus, as ordinary unital rings,

\[
\Gamma_{\mathbb Z}(T)/(T-1)\simeq\mathbb Q.
\]

There is no unital `Z`-algebra map to `Z` carrying `T` to `1`; already `1=2γ₂(T)` would be impossible. More generally, a nonzero ring receiving a divided-power element specialized to a unit must be a rational algebra. In characteristic `p`, `T^p=p!T^{[p]}=0`, so imposing `T=1` produces the zero ring.

For the **direct sum** of the global weight complexes, quotienting by `T−1` has a further transparent interpretation. As a complex of abelian groups it is the filtered colimit of the weight complexes under multiplication by `T`; filtered colimits are exact. On `H^q`, once `w≥q`, the transitions are `G→G`, multiplication by `w+1`, where `G=H^q(X,k)`. Therefore

\[
H^q\bigl((\bigoplus_w\Gamma(X,K_w))/(T-1)\bigr)
\simeq H^q(X,k)\otimes_{\mathbb Z}\mathbb Q.
\]

The multiplicative identification sends the weight-`w` class represented by `aT^{[w]}` to `a/w!`; the binomial coefficients then give ordinary multiplication of these rationalized classes. This does not, without a commutation theorem, identify the result with `H^q(X,k⊗Q)`. For infinitely many discrete points, `(∏Z)⊗Q` has a common denominator for every element, whereas `∏Q` need not: coefficient extension and global sections already differ in degree zero.

Completion changes this calculation. In the weight-completed ring `∏_{w≥0}Z·T^{[w]}`, the series `Σ_{n≥0}T^n` is a valid inverse of `1−T`; hence the completed quotient by `T−1` is zero. This is one reason not to import the completed divided-power construction of *Pursuing Stacks* §111 into the manuscript's graded algebra without a separate argument.

## 7. The withdrawal on scan 075 and the global degree-zero exception

Scan 074 ends by proposing multiplicative/divided-power structures; scan 075 immediately marks compatibility “est faux”. This is a withdrawal in the same text and must be retained as such. It does not by itself refute the subsequent explicit `ΓΦ⊗ΛΨ` construction in scans 080–083.

Two algebraic distinctions explain what must be checked, without purporting to reconstruct the author's reason for the withdrawal. Put `ε=dT` and `C=ΓΦ⊗ΛΦ`. The image `εC` has zero inherited products, so the map `a↦εa` cannot preserve the inherited multiplication: `u(1)²=ε²=0`, whereas `u(1)=ε` is nonzero. A different product can be transported from the quotient `C/(ε)` to the shifted image; this gives the familiar `ΓΦ⊗Λ(Φ/kT)` algebra, but it is not the inherited ideal product.

There is also a literal sign test for the displayed bimodule identities. Over `Z`, take `Φ=ZT⊕Zx`, let `ε=dT`, `η=dx`, and use the transported unital quotient product on `DR`. Then `i(1)=ε`, while the two unsigned identities of scans 075–076 would require `i(u(η))=εη` and also `i(u(η))=ηε=−εη`. Since `2εη≠0`, those identities cannot both hold with those explicit conventions. This is our consistency test; it does not authorize adding a sign to the transcription or identify which convention was intended.

The global-sections exception is independent of this sign issue. At complementary degree zero, `DR_*^{0,0}=k_*`; it need not be flasque in the sense required to make sections exact over every object. Here the sections functor is the one on the chosen slice over `X`, or equivalently the functor represented by `X`, rather than just absolute sections of the simplicial topos. From `0→k→Φ→Ψ→0`, with `Φ` acyclic for that sections functor, one obtains

\[
\operatorname{coker}\bigl(\Gamma(X,\Phi)\to\Gamma(X,\Psi)\bigr)
\simeq H^1(X,k).
\]

Thus the `p≥0` flasqueness claim on scan 075 cannot be used without qualification. The restriction “épi si p≠0” on scan 076 reflects the necessary exception. Under the analogous acyclicity hypotheses on the exterior powers of `Φ`, the degree-`q` failure of global surjectivity at `p=0` records `H^q(X,k)` for `q≥1`; the map in degree `q=0` is already an isomorphism onto the kernel. These are precisely the positive-degree classes for which scans 076–077 say that extra product/divided-power data remain to be specified.

## 8. Scan 064: exactness, universal acyclicity and variance

The source explicitly marks “à vérifier ce point”. Three claims must be separated:

1. Tensoring the augmented sheaf complex with `F` remains exact.
2. Its terms remain acyclic for sections after this tensoring.
3. Its global sections coincide with previously defined simplexwise cochains with coefficients.

Flatness or a pointwise contraction can prove the first claim. It does not prove the second. The third has an additional variance issue: for a face map `σ∘θ→σ`, a presheaf supplies `F(σ)→F(σ∘θ)`, whereas the usual cochain transport needs the reverse direction. In a local system the maps are invertible, but an arbitrary presheaf supplies no such inverses. Scan 062 explicitly distinguishes contravariant systems for chains from covariant systems for cochains; this is relevant to the assertion on scan 060 as well as to scan 064.

### Absolute acyclicity is weaker than the slice condition

For the simplicial topos `SS=Set^(Δ^op)`, absolute global sections of an abelian presheaf `M` are simply `M_0`. Indeed, `[0]` is terminal in `Δ`, so it is initial in `Δ^op`; a compatible family is determined by its value at `[0]` through the unique maps from that initial object. Evaluation is exact in a functor category. Consequently every abelian presheaf on `SS` is acyclic for **absolute** global sections, and the same is true of every tensor product there. This weak condition alone cannot carry the universal force used on scan 075.

For a simplicial set `X`, the slice is instead `SS/X≃Set^((Δ/X)^op)`, with sections the limit over its category of simplices. It need not have exact global sections. Sections of the restriction of `M` to this slice identify with `Hom_SS(X,M)`; their derived functors agree in this presheaf setting because restriction has an exact left adjoint, computed by direct sums over the simplices above each degree. Thus the passage to `Hom(X_*,-)` for **every** `X_*` on scan 075 requires acyclicity on the relevant slices. A relative comparison for `f_*` on scans 081–082 likewise requires `f_*`-acyclicity, not just vanishing of the absolute higher global sections of the source topos.

There are further distinct quantifiers: tensoring by all modules on the base topos, restricting to every slice, and tensoring by all modules intrinsic to each slice. Arbitrary slice coefficients need not be restrictions of base coefficients. The counterexample below concerns an arbitrary module on one specified slice. It therefore refutes the literal arbitrary-coefficient assertion on scan 064 in that setting, but it does **not** by itself refute the asserted De Rham condition of scan 091, whose precise use of “flasque” and tensor universality must first be fixed. None of the conditional weightwise theorems above requires deciding that terminology: each explicitly names the functor for which its terms must be acyclic.

### A full simplicial counterexample under the arbitrary-presheaf interpretation

Let `X=Δ¹/∂Δ¹`, let `v` be its unique nondegenerate vertex and `e` its unique nondegenerate edge, and let `C=Δ/X`. Work in the abelian category `Fun(C^op,Vect_k)` for a field `k`. This is the category of `k`-module objects in the presheaf slice topos over `X`; its global sections are compatible families, namely the limit of the contravariant diagram.

Every simplex of `X` is either a degeneracy of `v` or a degeneracy of `e`. Define

\[
F(\sigma)=
\begin{cases}k&\sigma\text{ is vertex-degenerate},\\
0&\sigma\text{ is edge-degenerate}.
\end{cases}
\]

Use identity maps between vertex-degenerate objects, and zero maps whenever the source module of a restriction is zero. This is a valid presheaf. The vertex-degenerate objects form a sieve in `C`: an arrow into one cannot start at an edge-degenerate object, because composing a constant simplex with an ordinal map stays constant. Thus no composite through an edge object can contradict an identity restriction between vertex objects.

Let `I` be the right adjoint to evaluation at the object `v`, applied to `k`. It has

\[
I(\sigma)=\prod_{\operatorname{Hom}_C(v,\sigma)}k=k^{n+1}
\quad\text{for an }n\text{-simplex }\sigma,
\]

with coordinate-selection restriction maps. Evaluation is exact and `k` is injective as a vector space, so `I` is injective in this presheaf category. Embed `F→I` by the diagonal `k→k^{n+1}` on vertex-degenerate simplices and by zero on edge-degenerate simplices; the maps are natural.

Put `Q=I/F`. Then `ΓI=k`, represented by the same scalar at every vertex coordinate, and `ΓQ=k²`. To verify the latter assertion explicitly, `Q(v)=0`, so compatibility with each degeneracy map to `v` forces the section on every vertex-degenerate simplex to be zero. A section on `e` is an arbitrary pair `(a,b)`. Every edge-degenerate simplex has a unique degeneracy map to `e`, so its section is forced to be the corresponding repeated-coordinate vector. Restricting such a vector to a vertex-degenerate face gives a constant vector, which vanishes in the diagonal quotient defining `Q` there. These are all the compatibility conditions.

The map `ΓI→ΓQ` is therefore the diagonal `k→k²`. The long exact sequence of `0→F→I→Q→0` gives

\[
\Gamma F=0,
\qquad H^1(X,F)\simeq k^2/\Delta(k)\simeq k\ne0.
\]

On the other hand, for **any** presheaf `A` on `C`, one has `Γ(A⊗F)=0`. A global section is zero on `e` because `F(e)=0`; either vertex face of `e` then forces its value at `v` to vanish. Every other simplex is a degeneracy of `v` or `e`, so its value is forced to vanish too. In particular,

\[
\Gamma(X,C_X^q\otimes F)=0\quad\text{for every }q,
\]

and the global tensor complex in scan 064 is zero, despite `H¹(X,F)=k`.

For the standard simplexwise cochain sheaf described on scan 050, the augmented complex `F→C_X^*⊗F` is nevertheless exact: at each simplex it is the usual augmented cochain complex of a simplex, tensored with either `k` or zero. Thus this example directly separates exactness of the tensor resolution from acyclicity of its terms. One can see the latter failure in degree zero: `C_X^0=I`; if `G=I⊗F`, then `G` equals `I` on vertex-degenerate simplices and is zero on edge-degenerate simplices. The same injective-quotient argument gives `H¹(X,G)=k`, so this term is not acyclic.

**Conclusion and limit.** Under the literal arbitrary-presheaf interpretation, this is a counterexample to the cohomological comparison on scan 064, not merely a variance objection. It does not refute the locally constant case, and it does not by itself identify the precise meaning of flasque or the unspoken scope of any other construction. In particular, one must not infer from it a blanket refutation of all the conditional theorems on scans 080–094. For hypercohomology of an unbounded coefficient complex, a further totalization/K-acyclicity argument would be needed even after fixing the coefficient scope.

## 9. Context comparisons and limits of the connections

- **`context/README.md`, S11(i).** The weights, truncations and coefficient algebra qualify the planning assertion directly. These pages support a functorial weighted structure with integral information in a triangular range; they do not support silently replacing it by one ordinary strictly alternating PD cochain algebra with ordinary cup multiplication.
- **`notes/RESULTS_STATE.md`, WG2 §2.4 #5.** The binomial-factor and `CP²` tests bear on the proposed integrality/divided-power connection. They do not settle the specific Lefschetz-ring or `δ′` questions named in that planning entry.
- **`ps_chapters_VI_VII/ps6.tex`, §111, manuscript pp. 450–451.** The supplied context explicitly replaces an infinite divided-power exponential by the completed product `∏Γ^i`. This is a different construction; the completion calculation above shows why it must not be substituted for the graded direct-sum object without argument.
- **`ps6.tex`, §119, manuscript pp. 500–503.** The failure of the proposed discrete/schematic linearization comparison is illustrated there by the polynomial central-extension equation and its missing integral splitting. That later failure is not a refutation of the weightwise de Rham theorem here: the two uses of divided powers and the comparison claims are different. It does reinforce the need to distinguish polynomial, divided-power, binomial and completed constructions.
- **`ps6.tex`, §124, manuscript pp. 521–522.** The text explicitly distinguishes the de Rham approach from the unipotent-schematic approach, questions a proposed right adjoint, and discusses complications with coefficient extension. This adds context for caution about homotopy-theoretic reconstruction and extension of coefficients; it supplies no missing proof of the arbitrary-presheaf assertion on scan 064.

The context search used the terms `divided`, `puissances`, `Rham`, `Cartan` and `altern`. No direct registered result in `RESULTS_STATE.md` settles the new coefficient example above; its correct status is our explicitly proved conditional test of the interpretation, not a recycled register theorem.

## 10. Short note candidates for the main research notes

Each item below is at most four sentences. Confidence concerns the mathematical implication under its stated assumptions, not confidence in a new handwriting reading.

**A01 — scans 080–082; unpursued implication / own analysis; bears on README S11(i).** The phrase “un certain, tronqué du second” can be made precise: with total weight `w`, the global complex is `τ≤wRΓ(X,k)` if its positive-complementary-degree terms are acyclic. The endpoint `q=w` follows from the hypercohomology spectral sequence, although the last term need not be flasque. **Confidence: high**, by the explicit spectral-sequence argument above.

**A02 — scans 080–083; unpursued implication; bears on WG2 §2.4 #5 and README S11(i).** The coefficient basis `T^[w]` makes multiplication equal to `binom(w+v,w)` times ordinary cup product between weights `w` and `v`. Thus compatibility with products is a weighted assertion, and replacing it by an ordinary integral ring identification discards a necessary coefficient. **Confidence: high**, from the multiplicative augmentation and divided-power multiplication law.

**A03 — scans 080–083; own idea; ordinary-model test.** On a point with `Φ=kT` and `Ψ=0`, the construction has `H⁰=Γ_k(T)`, rather than `k`. This elementary test already prevents identifying the raw ungraded algebra with ordinary cochains. **Confidence: high**, by direct computation; relevant to README S11(i).

**A04 — scans 083, 094; own idea; proposed main-note R062.** A single integral DGA with differential-compatible divided powers on every positive-degree element cannot reproduce the ordinary ring of `CP²`: a cocycle for its degree-two generator would make the indivisible degree-four generator equal to `2γ₂(x)`. The weighted algebra avoids this obstruction through its binomial factors. **Confidence: high**, under the explicit PD-ideal hypothesis; bears on README S11(i) and WG2 §2.4 #5.

**A05 — scans 081, 083, 094; own idea; proposed main-note R063.** Over `F₂`, strict alternation rules out the ordinary cup ring of `RP∞`, but the weighted model has no such contradiction because every same-weight square carries the even coefficient `binom(2w,w)`. Different-weight representatives can recover nonzero products: the weight-one and weight-two copies of the degree-one class multiply nontrivially in weight three. **Confidence: high**, from the stated ring calculation and the weighted product formula; relevant to README S11(i).

**A06 — scans 080–081, 094; own implication; bears on WG2 §2.4 #5.** Imposing `T=1` in the integral divided-power coefficient algebra gives `Q`, not `Z`, because `1=n!γ_n(T)` makes all factorials invertible. In characteristic `p` the same specialization is zero. **Confidence: high**, by the two-sided universal-ring calculation above.

**A07 — scans 080–082; own idea / context link.** For a direct sum of weights, specialization at `T=1` rationalizes the already computed cohomology groups through the transitions `×(w+1)`. It need not commute with coefficient extension before global sections, and in the completed divided-power product the quotient is instead zero. **Confidence: high**, with the direct-sum convention explicit; compare context §111, pp. 450–451, and §124, pp. 521–522.

**A08 — scans 074–077; withdrawn in the same text / own consistency test.** The proposed structural compatibility at the end of scan 074 is immediately marked “est faux” on scan 075. The square-zero inherited product on `εC` must be distinguished from the quotient product transported from `C/(ε)`, and the two unsigned bimodule identities fail the rank-two integral test given above. **Confidence: high** for those algebraic tests, without claiming they explain the author's withdrawal or changing the frozen signs.

**A09 — scans 075–077; unproved claim / own check.** The claim of flasqueness for `p≥0` encounters `DR_*^{0,0}=k_*`, and global surjectivity of `ΓΦ→ΓΨ` can fail by `H¹(X,k)`. The restriction “épi si p≠0” on scan 076 preserves this boundary phenomenon. **Confidence: high**, from the long exact sequence; no directly settled register item applies.

**A10 — scans 060, 062, 064; self-flagged and own counterexample; proposed main-note R061.** The arbitrary-presheaf extension beside “à vérifier ce point” fails for the explicit coefficient system on `Δ/(Δ¹/∂Δ¹)` constructed above: its tensor-cochain global sections all vanish, while `H¹(F)=k`. The tensor resolution remains exact pointwise, so the failure lies in universal acyclicity; the local-system/cofaisceau comparison has an additional variance requirement already visible on scan 062. **Confidence: high** under the specified presheaf interpretation, with the full injective-quotient proof in §8.

**A11 — scans 083–085; unpursued implication.** Without the marked trivialization of the kernel line `L`, weight `w` resolves `Γ^wL` rather than the constant coefficient `k`. For a line bundle this is the corresponding tensor-power coefficient, with divided-power multiplication still retaining its binomial factors. **Confidence: high**, by local trivialization and the algebraic resolution; this qualifies README S11(i).

**A12 — scans 064, 075, 081 and 091; own proof-obligation note.** Absolute sections on the simplicial topos are evaluation in degree zero and hence exact, whereas sections on arbitrary simplicial slices need not be. The passage to `Hom(X_*,-)` for every `X_*`, and the relative `f_*` theorem, therefore require stronger acyclicity than absolute global sections alone. **Confidence: high**, from the initial-object calculation and the explicit slice counterexample; it qualifies the De Rham-condition interpretation in README S11(i) without declaring the scan 091 example false.

## 11. Review of the main research notes

The mathematical introduction and items **R027–R051** of `MPL_136_047-094_notes.md` were reviewed after this memo's calculations were completed. No concrete mathematical error was found in their stated conditional assertions. The following checks delimit that assessment; they are not claims to have supplied every proof left unfinished in the manuscript.

| Items | Check and retained qualification |
|---|---|
| Introduction; R027–R031 | The conversion to total weight is correct; the comparison includes the endpoint because only earlier terms need acyclicity. The product assertion is appropriately conditional on multiplicative compatibility, and the relative statement correctly asks for the relevant `f_*`-acyclicity. |
| R032–R038 | The distinction between chain maps, isomorphisms after localization, and enhanced coherence is preserved. Scan 083 indeed allows a general flat kernel before imposing a line condition. Tensor-universal monomorphisms should retain their purity/base-change interpretation. |
| R039–R044 | These correctly report assertions and definitions without making the examples unconditional theorems. The special-cohomology vanishing needs the stated positive-exterior-degree qualification, and the strict flasque range matches the truncation argument. Acyclicity on the base versus on slices remains the explicit qualification detailed in §8 above. |
| R045–R047 | These are identified as source discrepancies and reading questions; no mathematical expectation is used to alter the frozen symbols. |
| R048–R050 | The ordinary quotient `T=1`, the factorial transition colimit, and the strictly alternating characteristic-two obstruction are correct with their stated assumptions. The normalized bar complex of `C₂` gives the claimed polynomial cup ring: one nondegenerate tuple in each degree, zero differential over `F₂`, and concatenation cup products. |
| R051 | Cenkl (1989), §5, Theorem 2, pp. 31–33, was checked in the published paper. The listed naturality, unit-compatible commutative multiplication, model-acyclicity and all-spaces cohomological comparison hypotheses correctly delimit the obstruction; the theorem concludes that each coefficient square is divisible by two. This is a separate statement from the elementary strict-alternation test and from the weighted theorem. |

The later added R061–R064 were also checked against the constructions in this memo. In particular, R064 correctly qualifies the constant-corner obstruction by **universal acyclicity on simplicial slices**. The main introduction's use of “under the manuscript's exactness and flasqueness hypotheses” is defensible provided that scope is retained; the absolute-versus-slice observation is a useful additional note, not a reason to withdraw the conditional comparison.

## References and retrieval record

Cenkl, B. (1989). Cohomology operations from higher products in the de Rham complex. *Pacific Journal of Mathematics, 140*(1), 21–33. https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf

Hatcher, A. (2002). *Algebraic topology*. Cambridge University Press. Author's revised §3.2, Theorem 3.19, p. 220: https://pi.math.cornell.edu/~hatcher/AT/ATch3.2.pdf

The Stacks Project Authors. (2026a). *Divided power polynomial algebras* (Section 23.5, Tag 07H4). https://stacks.math.columbia.edu/tag/07H4

The Stacks Project Authors. (2026b). *Divided power Poincaré lemma* (Section 60.20, especially Lemma 60.20.1, Tag 07LB). https://stacks.math.columbia.edu/tag/07LB

The Stacks Project Authors. (2026c). *Lazard's theorem* (Theorem 10.81.4, Tag 058G). https://stacks.math.columbia.edu/tag/058G

All five external sources were opened on 16 November 2026. Browser retrieval references for the parent reader: `turn21view1` (07H4), `turn21view0` (07LB), `turn27view0` (058G), `turn21view2` / `turn25view0` (Hatcher), and `turn31view0` (Cenkl). The parent must open the URLs in its own context before using web-source citations in the final answer. The supplied *Pursuing Stacks* files are cited by their internal section and manuscript-page markers; they were read from the supplied context, not used to change any transcription.
