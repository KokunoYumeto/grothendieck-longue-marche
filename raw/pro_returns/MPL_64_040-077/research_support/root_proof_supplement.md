# Proof and calculation supplement

Prepared after the transcription freeze, by GPT-6 Astra Pro, run `MPL_64_040-077/root`; the effort setting is not exposed. These arguments concern the research notes only. They do not change any frozen reading, establish an absent research-return proof, or claim novelty. Exact finite and symbolic checks are in `../scripts/research_checks.py` and `root_checks.json`; the last strengthening of that certificate ran at 2026-11-17 23:16:17 UTC.

## 1. The endomorphism decomposition on scans 042–043

Write matrices over the field with two elements and let the six invertible matrices act by conjugation. With

\[
a=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
b=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
c=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
\rho=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\]

the two subspaces in the manuscript are

\[
V'=\{0,a,b,c\},\qquad W=\{0,I,\rho,\rho^2\}.
\]

Here $a+b=c$, $\rho^2+\rho+I=0$, and the intersection is zero, so $M_2(\mathbb F_2)=V'\oplus W$. The three nonzero elements of $V'$ are the transpositions of the three nonzero vectors; associating to a vector its unique fixing transposition extends to a linear equivariant isomorphism $V\to V'$. The action is transitive on nonzero vectors, proving irreducibility in dimension two over this field. The certificate enumerates all sixteen matrices and checks these assertions, the trace orthogonality, and the trace-zero decomposition on scan 043.

The trace form on $V'$ is alternating and nondegenerate: it has value one on distinct nonzero vectors and zero on a vector paired with itself. On $W$ the form is nondegenerate and nonalternating. The invariant subspace $W^{\mathrm{GL}(V)}=\mathbb F_2 I$ has trace zero, so there is no invariant trace-one lift of the trivial quotient; this proves that the displayed module extension does not split. In particular, the phrase “son propre orthogonal” is correct for $\mathbb F_2 I$ **inside $W$**; its orthogonal in all of $M_2(\mathbb F_2)$ is the three-dimensional trace-zero space.

As an algebra, $W$ is the field with four elements. Its two elements $\rho,\rho^2$ outside $\mathbb F_2$ form a basis permuted by the sign quotient of $\mathfrak S_3$, so the underlying module is the permutation module on the two orientations of $J$; this explains the $\mathbb F_2^{\underline\omega}$ summand on scan 066. By contrast $a^2=I\notin V'$, so $V'$ is not an algebra under multiplication. This last observation does **not** show that the frozen scan 042 asserts it is one: Hua's footnote attributes a “commutative subalgebra” wording not present in the frozen reading, and that attribution remains a reading question.

## 2. Four points, the elliptic involution, and the almost-cartesian square

For four distinct marked points on a projective line over a base with 2 invertible, the three double transpositions extend to homographies. After identifying the four points with $0,1,\infty,t$, with $t$ and $t-1$ invertible, these are precisely the three transformations displayed in (34) on scan 064. Checking their action on the four points proves uniqueness and their Klein-four relations; the expressions are compatible with relabelling and hence with étale descent. This justifies the extension claim of scan 054 without treating a general permutation of the four points as extendible.

For the construction of scans 058–059, choose an origin locally in a genus-one torsor $E$. Then $\sigma(x)=a-x$, the fixed locus is $[2]^{-1}(a)$, and it is a torsor $I$ under $E_0[2]$. The contracted product $I\wedge_{E_0[2]}E_0$ reconstructs the pair $(E,\sigma)$; the map $x\mapsto2x-a$ descends to a canonical identification $E/E_0[2]\simeq E_0$, and its invariance under a change of chosen origin supplies the descent check. This is the elementary local proof of the manuscript's equivalence, not a proof of every relative category assertion later in the packet.

At a geometric branch point belonging to $D_J$ in the square (29), the two maps to the lower-right line have tame local models $w=u^2$ and $w=v^2$. Their fiber product has completed local ring

\[
k[[u,v]]/(v^2-u^2)=k[[u,v]]/((v-u)(v+u)).
\]

It has two branches, and its normalization is the disjoint union of the two smooth branches; each maps étale to the $u$-line. This explains both why the fiber product is not already $E$ near $D_J$ and why normalization is the correct reconstruction over a field (or with suitable normality hypotheses). Away from $D_J$ the quotient cover is an étale $V$-torsor and the usual pullback square is cartesian. This local computation supports scan 062's proposed reconstruction; it does not silently assert a normalization theorem over an arbitrary nonnormal base.

The degree count in (27) is independent of these local coordinates: the contracted product has sixteen geometric points, removing $I$ leaves twelve, and the involution acts freely on those twelve. The quotient therefore has six geometric points; the frozen underbrace “degré 2” is not the degree of that quotient, although its quotient map has degree two.

## 3. An intrinsic construction answering scan 063

Let $X=\Sigma_J$, let $D_J$ be its marked étale divisor of degree three, and let $t$ be a section disjoint from $D_J$. The four-point divisor $D_J\amalg t$ has its canonical double-transposition subgroup $V$. Form the quotient $q_V:X\to Y=X/V$; its three branch values are labelled by the three nonidentity elements of $V$, equivalently by $J$. Identifying this marked three-point line $Y$ with $\Sigma_J$ gives the intrinsic degree-four map $f_2^t$ without first choosing an elliptic double cover.

The construction is local for the étale topology and descends because the Klein subgroup, its branch labels, and the isomorphism of three-pointed lines are canonical. In the split coordinates below the quotient exists as an everywhere-defined finite locally free degree-four map; the unit resultant and the fiberwise flatness criterion verify its good relative behavior on the stated base. Invariance under the three involutions gives an inclusion of the target algebra in the invariant direct summand of the pushforward, and averaging by $1/4$ makes formation of that summand commute with base change; its geometric fibers have rank one, so the inclusion is an isomorphism. This verifies the relative quotient even over a nonnormal base, without appealing to normalization. Thus this is a checked construction of the map requested on scan 063, not a claim that the manuscript already supplied its descent proof.

There is a necessary uniqueness qualification. Conditions (32) alone prescribe the images of six points, but do not prescribe the degree or their multiplicities; composing a solution with a higher-degree map fixing $0,1,\infty$ preserves those conditions. Scan 064's “avec multiplicité 2” and “degré quatre” remove that ambiguity: the two zero points and two pole points, each of multiplicity two, fix the function up to a scalar, and the third branch-value condition fixes that scalar.

## 4. Exact rational identities on scans 064–065

Work over $\mathbb Z[1/2,t,1/t,1/(t-1)]$ and put

\[
A=z^2-2z+t,\qquad B=z^2-2tz+t,\qquad C=z^2-t,
\qquad F_t(z)=t\frac{A^2}{B^2}.
\]

The certificate verifies, by exact polynomial arithmetic,

\[
\begin{aligned}
tA^2-B^2&=(t-1)C^2,\\
A^2-B^2&=4(t-1)z(z-1)(z-t),\\
\operatorname{Res}_z(A,B)&=4t(t-1)^2,\\
F_t'(z)&=-4t(t-1)\frac{AC}{B^3}.
\end{aligned}
\]

The homogeneous numerator and denominator are degree four with no common zero, including at infinity. The first identity gives $F_t-1=(t-1)C^2/B^2$; hence the three axes map to $0,1,\infty$, each with multiplicity two. Substitution also verifies invariance under all three homographies in (34). The three quadratics have nonzero discriminants, and their roots are mutually disjoint on the stated base; no exclusion of characteristic three or five is needed for this rational-map calculation.

The roots of $B$ are $t\pm\sqrt{t(t-1)}$. Substituting the frozen $t+\sqrt{t(1-t)}$ gives the nonzero residue $-2t(t-1)$, so the sign in the displayed radical is a mathematical error in the recorded formula; **Hua's modernization had already flagged it**. The scalar $c_t=t$ and formula (37) are correct. For $R=A/B$, the four values at $0,1,\infty,t$ are $1,-1,1,-1$, respectively, so scan 065's intermediate assertion of the value $1$ at $z=1$ is false while its squared conclusion $F_t(0)=F_t(1)=F_t(\infty)=F_t(t)=t$ remains correct.

## 5. Iteration and the necessary divisor multiplicities

Let $q:E\to E/\{\pm1\}=\Sigma_J$ send the elliptic origin to $t$, and let $m=2^n$ with $n\ge1$. The quotient map $F_m$ of $[m]$ satisfies $F_m\circ q=q\circ[m]$. Since $q^*(t)=2[0]$ and $[m]$ is étale, pullback gives

\[
q^*F_m^*(t)=2\sum_{P\in E[m]}[P].
\]

The map $q$ is ramified of index two at the four points of $E[2]$ and étale at the other torsion points. It follows, as an equality of divisors, that

\[
F_m^*(t)=q_*[E[m]].
\]

Its coefficient is one at each image of a two-torsion point and two at each image of a pair $\{P,-P\}$ with $P\notin E[2]$. Thus its degree is $m^2$, whereas its reduced support has degree

\[
4+\frac{m^2-4}{2}=\frac{m^2}{2}+2.
\]

For $m=2$ these are both four; for $m\ge4$ the scheme-theoretic fiber is nonreduced at the other torsion images. The scheme-theoretic image of the finite étale torsion subscheme under $q$ is its reduced quotient on geometric fibers, so it is not that nonreduced fiber. Consequently scan 065's sentence about an “image inverse” being the “image ... du sous-schéma” is correct as a statement about support, but requires the displayed divisor refinement if interpreted scheme-theoretically.

As a completely explicit check, the reduced rational expression for $F_t(F_t(z))-t$ has numerator

\[
16t(t-1)z(z-1)(z-t)A^2B^2C^2
\]

and a denominator which is the square of a monic polynomial of degree eight (recorded in the JSON certificate). At $t=2$ the numerator and denominator are coprime, the six roots of $ABC$ are distinct and avoid $0,1,2$, and infinity is the fourth simple point of the fiber. This gives degree sixteen with only ten geometric support points and provides a concrete counterexample to a reduced-image interpretation of the entire fiber.

## 6. Tangent powers: leading jets and the local norm

For a tame local model $x=u y^n$, where $u$ is a unit pulled back from the target and $n$ is invertible, the leading pullback on conormal lines is

\[
C_x\longrightarrow C_y^{\otimes n},\qquad \bar x\longmapsto u\,\bar y^{\otimes n}.
\]

Dualizing defines the leading-jet map $\kappa_{\rm jet}:T_y^{\otimes n}\to T_x$ with coefficient $u$. Its behavior under changes of parameters is exactly the tensor-power rule, so it is intrinsic. The determinant convention for the norm, checked against the primary reference [Stacks Project, Tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2), gives

\[
N(y)=(-1)^{n-1}\frac{x}{u}.
\]

This follows for all $n$ from the constant term of $Y^n-x/u$, independently of the finite checks for $2\le n\le8$. If one takes the norm's induced map $C_y^{\otimes n}\to C_x$, inverts it and dualizes, the resulting tangent map is

\[
\kappa_{\rm norm}=(-1)^{n-1}\kappa_{\rm jet}.
\]

In degree two the two conventions therefore differ by a minus sign. Scan 071 explicitly says “via l'hom norme locale,” so this is a convention to keep visible when comparing formulas, **not** an assertion that its norm-defined map is wrong. If the unit is instead an arbitrary source-unit $u(y)$, the exact polynomial expression above is replaced by the leading conormal identity $[N(y)]=(-1)^{n-1}u_0^{-1}[x]$, with $u_0=u|_{t'}$; the same tangent-line sign follows, but $Y^n-x/u(y)$ is not asserted to be a polynomial over the target ring. The Stacks reference was opened on 2026-11-17 and is used only for the determinant definition and its base-change compatibility, not as a source for the entire cover classification asserted on scans 072–074.

## 7. A missing compatibility in the unrestricted cover-data category

The target data on scan 073 list an arbitrary monomorphism $i:\mu_n\hookrightarrow G$ and a punctured-cover class of ramification order $n$. To reconstruct a pointed $G$-cover, the image and character of $i$ must agree with the actual inertia of that class at the chosen branch. This is not a consequence merely of their having the same order.

For an explicit counterexample to the unrestricted list, take $S=\operatorname{Spec}\mathbb C$, $X=\mathbb A^1_x$, $t=0$, and $G=(\mathbb Z/2)^2$. Let

\[
Y=\mathbb A^1_y\times\{0,1\},\qquad x=y^2,
\qquad (a,b)(y,c)=((-1)^a y,c+b).
\]

Over $X^*=\mathbb G_m$ this is a $G$-torsor and its class $\xi$ has tame ramification order two. Every point over $t$ has stabilizer the **first** factor of $G$. Choose $i$ to be the inclusion of the **second** factor, and choose any line $T$ with an isomorphism $T^{\otimes2}\simeq T_{X,0}$. These choices meet the independently listed conditions on scan 073 but cannot come from a pointed cover with this $\xi$ and this $i$: normalizing $X$ in the fixed punctured torsor recovers $Y$, and its inertia cannot be changed to the other factor by conjugation in an abelian group.

The refined assertion must restrict the target category to inertia-compatible data and specify the morphisms and descent conditions. The example refutes only the unrestricted list as literally stated; it does not refute the intended quadratic application, where $G=\mu_2$ and the nontrivial inertia subgroup is forced. A full equivalence over arbitrary $S$ is not independently proved in this report.

There is also an automorphism qualification to “à isom unique près.” The object $(T,\kappa:T^{\otimes n}\simeq T_x)$ has automorphisms $\mu_n$, and the local Kummer cover has the corresponding deck transformations. A morphism inducing a *specified* isomorphism of the tangent-root objects can be unique; a bare object with its $n$th-power relation is not an object with trivial automorphism group. This is compatible with the groupoid language subsequently used on scan 075.

## 8. The orientation twist and what Legendre pinning adds

Let $V_J=\ker(\mathcal O^J\xrightarrow{\sum}\mathcal O)$. Permuting $J$ acts on $\det V_J$ by the sign character, so this determinant line is the line associated with the orientation double cover $\omega(J)$. On the projective bundle of lines in $V_J$, with universal line $L$ and quotient line $Q$, the relative tangent bundle is

\[
T_{\mathbb P(V_J)/S}=\operatorname{Hom}(L,Q)
=L^{-2}\otimes\det V_J.
\]

This is the identity $T_\Sigma\simeq\mathcal O(2)(\omega)$ on scan 075 with the corresponding projective-bundle convention. With the quotient convention the determinant is dualized, which yields the same sign line; the convention should be stated when comparing trivializations. No inverse of three is used: the trace/sum map on a split three-element étale cover is surjective even in characteristic three.

Twisting a line by a $\mu_2$-torsor leaves its square canonically unchanged. Twisting by a $\mu_4$-torsor $Q_0$ changes the square by the associated $\mu_2$-torsor $D_{Q_0}=Q_0/\{\pm1\}$; an identification with $\omega(J)$ supplies the missing orientation factor. This proves the line-level mechanism of scans 076–077, but does not construct the promised standard $Q_0$ on these pages.

At fixed $(J,t,Q_0,\alpha)$, the sheaf of compatible isomorphisms $\kappa:T_0\to T_{E,0}$ is a $\mu_2$-torsor. It has two elements over an algebraically closed field, as assumed at the start of scan 075, but need not have a global section over an arbitrary base. Elliptic inversion acts as minus one on $T_{E,0}$, and therefore changes the pinning, although it acts trivially on the four-pointed quotient and preserves the Weil pairing. This supplies the precise sign-sensitive refinement relevant to the earlier quotient construction; it is not by itself a proof of the fine-moduli theorem summarized in Hua's finding.

## Limits of the checks

- The computations are exact finite enumerations and polynomial identities; they are not OCR and did not produce readings.
- The field-level normalization model, the inertia counterexample over $\mathbb C$, and the line-bundle calculations have their stated hypotheses; no unsupported extension to a general nonnormal base is made.
- The rational-map correction and the characteristic-five correction discussed elsewhere must be credited to Hua where his supplied modernization already makes them.
- The full fine-moduli finding, the all-level congruence returns, the normal-crossings result LM6 F.43, and the unavailable cote93/159 statements have not been proved by these local checks.
