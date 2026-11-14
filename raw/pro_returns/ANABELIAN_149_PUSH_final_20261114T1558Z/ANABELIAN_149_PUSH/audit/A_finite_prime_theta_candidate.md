# No fixed finite odd-prime support suffices for the abelian theta route

Status: accepted by root and the independent topos reviewer on 14 November 2026; integrated as A.C2.14 after checkpoint08. The historical candidate filename is retained.

Accepted result A.C2.14. This is a limitation of a specified strategy, not a counterexample to A1. It also gives a useful finite-support refinement of A.C2.12.

## 1. Finite-support fixed-field lemma

Let J/Fq be a genus-two Jacobian, and let Θ/Fq be a geometrically irreducible theta divisor. Let S be a nonempty finite set of odd primes different from the characteristic, and put L=∏(ell∈S)ell. Suppose σ is a power of Frobenius fixing J[L]. Then every point of Θ whose order is supported on S is fixed by σ.

### Proof

Take η∈Θ of order supported on S. On each J[ell^a], σ lies in the kernel of reduction from GL4(Z/ell^a) to GL4(Fell), which is an ell-group. Thus the length n of the σ-orbit of η has every prime divisor in S. Suppose n>1. Choose ell|n and put τ=σ^(n/ell). The τ-orbit of η has exact length ell.

For a distinct prime r∈S, the restriction of τ to the r-primary component of η has r-power order, but τ^ell fixes that component. Coprimality therefore implies that τ already fixes it. Hence

\[
 T=\tau\eta-\eta
\]

is ell-primary and nonzero. On T_ell J write τ=1+ell M. The integral operator

\[
 U=\frac{1+\tau+\cdots+\tau^{\ell-1}}{\ell}
  =1+\sum_{j=1}^{\ell-1}\binom{\ell}{j+1}\ell^{j-1}M^j
\]

is congruent to the identity modulo ell, including when ell=3. It is an automorphism of the ell-primary torsion group. Since τ^ell η=η, we have ell U T=0, so ell T=0. The operator τ fixes J[ell], hence τT=T. Its orbit on η is exactly

\[
 \eta,\eta+T,\ldots,\eta+(\ell-1)T.
\]

All these points lie in Θ and Θ−T. The two irreducible theta translates are distinct, since the translation stabilizer of a principal polarization is trivial. Their intersection number is Θ²=2, contradicting ell≥3. Thus n=1.

This is not an assertion that σ acts as a scalar, or that its reduction is semisimple. The proof deals with each primary component before applying the same integral operator as A.C2.12.

### Arithmetic consequence

Suppose the Frobenius of a genus-two curve over a finite field k satisfies, for every ell∈S,

\[
 \pi\equiv1\pmod\ell,\qquad
 (\pi-1)/\ell\in\operatorname{GL}(T_\ell J).
\]

Then \(J(k)[S^\infty]=J[L]\). Indeed \(\pi-1=\ell A_\ell\), with \(A_\ell\) an integral automorphism, has kernel exactly J[ell] on J[ell^∞]. The preceding lemma therefore implies

\[
 \Theta\cap J[S^\infty]\subseteq \Theta\cap J[L].
\]

In particular theta avoidance at the single squarefree level L implies avoidance at every order supported on S.

## 2. Uniform failure of every fixed finite-prime abelian tower

For every nonempty finite set S of odd primes there exists an ordinary smooth proper genus-two curve C over a finite field of characteristic two such that

\[
 \Theta_C\cap J_C[S^\infty](\overline{\mathbf F}_2)=\varnothing.
\]

Consequently every geometrically connected finite étale cover that is abelian over the original C and whose group order has all prime divisors in S is ordinary, and its nontrivial geometric deck group acts faithfully on geometric two-primary torsion. None of these covers supplies either a positive-dimensional two-rank-zero abelian target or the deck-kernel obstruction used in A.C2.7–8.

The field of definition and curve are allowed to depend on S. Nothing asserts one curve avoiding all odd-prime-supported torsion: that would contradict the known finite-field theta-density theorem.

### Step 1: a nonempty open locus avoiding J[L]

Put L=∏S. In the ordinary genus-two moduli stack in characteristic two, the condition

\[
 \Theta_C\cap J_C[L]=\varnothing
\]

is open. More precisely, for the relative Frobenius-twisted curve and its Jacobian, the locally exact differential sheaf is a line bundle. The closed condition H0(B⊗Lχ)≠0 is upper semicontinuous on the finite étale L-torsion parameter scheme; its image in moduli is closed because that parameter map is finite. Taking the complement gives the asserted open. The origin is avoided on the ordinary locus.

This open is nonempty by the generic ordinariness theorem for abelian prime-to-p covers, in the exact form of Yang (2016), Proposition1.3, whose proof was opened. We use only this proposition, not its separately problematic primitive-character formulation for composite-order new parts. If the generic theta met a nonzero L-torsion point, the corresponding cyclic cover would have a Frobenius kernel on its new H1, contrary to generic ordinariness. There are only finitely many L-torsion points, so all are avoided on one common nonempty open.

The needed finite-level statement also has a complete compact-type proof, which we use to make extension and base change explicit. Let κ be an algebraic closure of F2 and form X0=E1∪E2 by joining two ordinary elliptic curves at one point. By Deligne–Mumford, Proposition1.5, the subsequent algebraization paragraph, and Theorem1.6 (printedpp.81–83), choose a projective regular smoothing f:X→Spec R, R=κ[[t]], with smooth genus-two generic fibre and local equation uv=t at the node. A smooth special point lifts to a section; it may be used to rigidify all line bundles.

The normalization sequence for units identifies Pic0(X0)=Pic0(E1)×Pic0(E2), since the dual graph is a tree. Hence X0 has exactly L^4 line-bundle classes killed by L. Every such line bundle, together with a trivialization of its L-th power, defines a μL-torsor. Since L is odd, this is finite étale. The proper henselian equivalence (Stacks Project, Lemma58.9.1, tag0A48, opened with its proof) extends the torsor and its action to X. Its character line M satisfies M^L=O_X. Full faithfulness preserves the group action, multiplication and torsor identity; thus this is an actual torsion line, not merely a class modulo a vertical correction.

Their geometric generic restrictions are distinct. If the quotient of two extended lines becomes trivial on the geometric generic fibre, proper cohomology and field base change make it trivial already over the generic field. On the regular surface X it is O_X(aE1+bE2), since a generic trivialization has a vertical divisor. The intersection numbers are E1·E2=1 and Ei²=−1, because E1+E2 is the principal total fibre. Its multidegrees are therefore (b−a,a−b). Torsion forces both to be zero, giving a=b, so the line is O_X(aX0)=O_X. Its special class was consequently trivial. These L^4 distinct generic classes exhaust the L-torsion of the smooth genus-two Jacobian. This explicitly supplies the usual fixed-level compact-type Picard extension, without assuming a theta line bundle on X0.

For an extended line M, write M_i=M|Ei. The normalization cohomology sequence is

\[
 0\longrightarrow H^0(X_0,M)\longrightarrow
 H^0(E_1,M_1)\oplus H^0(E_2,M_2)\longrightarrow M_{\rm node}
 \longrightarrow H^1(X_0,M)\longrightarrow
 H^1(E_1,M_1)\oplus H^1(E_2,M_2)\longrightarrow0.
\]

If both restrictions are nontrivial, their H0 and H1 vanish and H1(X0,M) is the one-dimensional node fibre. Frobenius from M to M² induces a nonzero semilinear map on that fibre. If exactly one restriction is trivial, its constant section maps isomorphically onto the node fibre, so H1(X0,M) identifies with the ordinary H1(O) of that elliptic component; Frobenius is again bijective. If both restrictions are trivial, the tree condition makes M|X0 trivial and H1(O_X0) is the direct sum of the two ordinary elliptic spaces. Thus the invariant Frobenius is bijective as well.

For each nontrivial line, H0 on the special and geometric generic fibres is zero, and H1 has constant dimension one by Riemann–Roch. Cohomology and base change therefore make R1f_*M a free R-module of rank one, and likewise for M². The absolute-Frobenius arrow linearizes to an R-linear map F_R^*(R1f_*M)→R1f_*(M²). Its special-fibre determinant is nonzero by the calculation above, hence a unit of R. The linearized map is an isomorphism, including on the geometric generic fibre. For O_X the same argument uses rank two. All L^4 arrows are handled simultaneously; they are a finite set. The generic smooth curve is ordinary and every nonzero L-torsion character arrow is bijective, so its Raynaud theta avoids J[L]. This proves the required open is nonempty. No assertion about a locally free Raynaud theta sheaf on the nodal curve is used.

Denote the resulting nonempty open stack by U. It is geometrically irreducible, since the genus-two moduli stack is smooth and geometrically irreducible and the ordinary locus is a nonempty open.

When working relatively, Θ lives on the Jacobian of the Frobenius twist. This causes no level-structure or arithmetic ambiguity: relative Frobenius gives a canonical Galois-equivariant isomorphism on all odd torsion. Thus the Frobenius conditions below transfer to the Jacobian carrying Θ.

### Step 2: full mixed-level connectedness, without an independence assumption

Put N=L²≥9. Choose a finite field k0 of characteristic two containing μN. Deligne–Mumford (1969), Theorem5.15, states that the geometric fibres of the moduli scheme of genus-g curves with symplectic Jacobi level-N structure, over the cyclotomic base, are connected. The required level is invertible in the characteristic and N≥3 makes this a scheme. The scheme is smooth, so connectedness gives irreducibility. Its restriction over U is consequently geometrically irreducible and nonempty.

This is a theorem for the complete composite level N, not an inference that separate ell-adic monodromies are independent. In particular there is no omitted Goursat or common-quotient argument.

To eliminate stack inertia and the hyperelliptic central automorphism from the pointwise Frobenius bookkeeping, use tricanonical rigidification. Let T→U be the scheme of curves with a basis of H0(C,ω_C^3). Its fibres over objects of U are GL5, since h0(ω_C^3)=5 in genus two. It is smooth with geometrically connected fibres and has a universal curve. The construction and the surjection on geometric fundamental groups are explicitly given in Achter–Pries (2008), Section5.1 and Lemma5.2. This is the reason for using a rigidification rather than pretending that the coarse level moduli space is a free Sp4-torsor.

Let Y→T be the scheme of symplectic level-N bases of the universal Jacobian, for the fixed primitive root of unity. It is a genuine finite étale torsor under

\[
 G=\operatorname{Sp}_4(\mathbf Z/N).
\]

The pullback Y→U[N] of T→U has the same connected GL5 fibres. Since U[N] is geometrically irreducible, Y is geometrically irreducible. The schemes may be taken quasi-projective, using the tricanonical Hilbert construction and the finite level cover. All the data are defined over a finite extension of k0.

### Step 3: a prescribed first congruence of Frobenius

For each ell∈S, let uell=1+ell in (Z/ell²)^*. Relative to the standard symplectic form with two upper and two lower coordinates, set

\[
 g_\ell=\operatorname{diag}
  (u_\ell,u_\ell,u_\ell^{-1},u_\ell^{-1})
  \in\operatorname{Sp}_4(\mathbf Z/\ell^2).
\]

Then gell has exact order ell,

\[
 g_\ell\equiv1\pmod\ell,\qquad
 (g_\ell-1)/\ell\equiv
             \operatorname{diag}(1,1,-1,-1)\pmod\ell,
\]

and the displayed derivative matrix is invertible. The Chinese remainder theorem gives g∈G of exact order L with these components.

The group action is defined over k0 after the preceding finite extension. Twist Y/k0 by the cocycle sending arithmetic Frobenius to right multiplication by g^−1. This is ordinary finite Galois descent: over an extension of degree L the cocycle becomes trivial, and quasi-projective descent is effective. The twisted scheme Y^(g) is geometrically isomorphic to Y, hence geometrically irreducible.

Lang–Weil gives a point on Y^(g) over k0^m for every sufficiently large integer m. Choose such an m with m≡1 modL. Under the geometric identification with Y this point is a level basis y satisfying

\[
 \operatorname{Frob}_{k_0}^{m}(y)=y\cdot g^m=y\cdot g.
\]

Its projection t lies in T(k0^m) and supplies an actual genus-two curve C/k0^m. Because T rigidifies the curve and Y is the actual level-basis torsor, this equation says that arithmetic Frobenius on J_C[N] has matrix g in the chosen basis (an inverse convention yields g^−1, which has the same invertibility property and changes nothing). The Weil-pairing multiplier is consistent: k0 contains μN, so its Frobenius multiplier is one modulo N.

Therefore on every T_ell J_C, Frobenius minus one is ell times an integral automorphism: its reduction after division by ell is the invertible displayed matrix. The curve lies in U, so its theta avoids J[L]. Step1's finite-support lemma now gives complete avoidance of J[S^∞].

Lang–Weil is used only to produce points on one fixed geometrically irreducible finite-type scheme over finite extensions in the progression m≡1 modL. It is not an unproved assertion that the finite base field is Hilbertian.

### Step 4: the whole abelian S-tower

Let D→C be geometrically connected, finite étale and abelian, with deck group an S-group. Over the algebraic closure its direct-image algebra decomposes into the distinct torsion line bundles indexed by its characters. Every nontrivial character bundle has order supported on S and hence lies outside Θ. The genus-two H1 character spaces have dimension one, and every Frobenius arrow is an isomorphism. The invariant part is ordinary because C is. Thus D is ordinary.

All nontrivial characters survive in the geometric two-primary representation (up to duality, which only inverts the characters), so the deck action is faithful. Any quotient abelian variety of J_D is ordinary. A nonconstant morphism D→A generates a positive-dimensional quotient of J_D inside A; therefore A cannot have two-rank zero. These are exactly the claimed limitations of this tower.

## 3. What this result does and does not settle

Here an abelian tower means the collection of covers whose composite cover is abelian over the original C; it does not include arbitrary iterations of abelian covers with a nonabelian composite group. The construction rules out a uniform proof of A1 based only on finitely many fixed odd primes and this abelian theta/deck-kernel mechanism. It does not rule out an adaptive sequence of odd primes, nonabelian covers supported on those primes, or a different separating construction. It supplies no pair of colliding point sections.

The curve in A.C2.13 gives a fully explicit small illustration: its entire abelian three-primary tower is ordinary, yet degree seven succeeds. The present theorem makes the finite-prime limitation uniform, with the curve allowed to vary.

## 4. Opened primary sources and exact locations

- Deligne, P., & Mumford, D. (1969). The irreducibility of the space of curves of given genus. Publications Mathématiques de l'IHÉS,36,75–109. Theorem5.15 and its proof, printedpp.108–109, with Lemma5.16 and the preceding Jacobi-level definition. Primary PDF https://www.numdam.org/item/PMIHES_1969__36__75_0.pdf ; opened refs turn629view0, turn630view0–1. Supplied local PDF background/literature/deligne_mumford_1969_PMIHES36.pdf. This is the exact mixed-level connectedness input.
- Achter, J.D., & Pries, R. (2008). Monodromy of the p-rank strata of the moduli space of curves. International Mathematics Research Notices,2008,rnn053. https://doi.org/10.1093/imrn/rnn053 . Author PDF https://www.math.colostate.edu/~achter/math/prm0508.pdf , Section5.1 and Lemma5.2, printedpp.17–18, opened ref turn636view0. The tricanonical rigidification is representable, has connected fibres, and surjects on fundamental groups. Theorem4.5 was also opened (turn621view0); no independence of its separate prime-adic representations is assumed.
- Yang, Y. (2016). Abelian coverings of curves over Fp which are not new ordinary. RIMS1844. Proposition1.3 and its proof, printedp.3, primary https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1844.pdf ; opened refs turn619view0, turn620view0. Only generic prime-to-p abelian-cover ordinariness is used here. The primitive-versus-all-character ambiguity in Proposition2.2 for composite n is not imported.
- Poonen, B. (2017). Rational points on varieties. Graduate Studies in Mathematics,186. American Mathematical Society. Theorem7.7.1(ii)–(iii), printedp.222/PDF zero-based235, primary author PDF https://math.mit.edu/~poonen/papers/Qpoints.pdf ; opened refs turn632view0–2. It gives points on a geometrically irreducible finite-type scheme over all sufficiently large finite extensions, exactly the needed Lang–Weil consequence.


Additional opened extension source: Stacks Project, Lemma58.9.1, tag0A48, https://stacks.math.columbia.edu/tag/0A48 (turn652view0), full proper henselian equivalence with proof. The stable smoothing source was reopened at Deligne–Mumford Proposition1.5 and its algebraization paragraph (turn654view1), Theorem1.6 (turn654view0), and the complete level theorem5.15 (turn654view2). The independent reviews are audit/A_finite_prime_theta_root_review.md and audit/A_finite_prime_theta_topos_review.md.
