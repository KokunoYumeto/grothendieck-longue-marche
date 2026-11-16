# Proof checks for the quadratic and graded-algebra notes

These are **original calculations prepared for this report**, not quotations or claims attributed to Grothendieck or Laborde; “original” describes the present derivations, not a claim of mathematical priority. They support the indicated research-note identifiers and leave every frozen transcription unchanged. For a module or bundle $E$, write $H(E)=E\oplus E^\vee$ with quadratic form $(e,\varphi)\mapsto\varphi(e)$.

## W05 — Failure of exact-sequence additivity in the split quadratic group

**Hypotheses and source anchor:** $S=\mathbb P^1_{\mathbb C}$; $WG(S)$ means precisely the group completion under orthogonal sum from cote 133, scan 006, with no additional metabolic relations. Scan 007 asks whether the hyperbolic map from split $K_s(S)$ factors through exact $K_0(S)$.

For homogeneous coordinates $X,Y$, the maps
\[
0\longrightarrow\mathcal O(-1)
\xrightarrow{(-Y,X)}\mathcal O^2
\xrightarrow{(X,Y)}\mathcal O(1)\longrightarrow0
\]
form an exact sequence: the composite is zero, and on each of $D(X)$ and $D(Y)$ the final map is surjective with the displayed rank-one kernel. Hence exact $K_0$ imposes $[\mathcal O^2]=[\mathcal O(-1)]+[\mathcal O(1)]$.

For a quadratic bundle $(M,q)$ set
\[
I(M,q)=\dim_{\mathbb C}H^0(S,M\otimes\mathcal O(-1)).
\]
This finite integer is unchanged by isometry and additive under orthogonal sum, so it extends to a homomorphism $WG(S)\to\mathbb Z$. Since $H(\mathcal O^2)$ has underlying bundle $\mathcal O^4$, its invariant is zero. Each of $H(\mathcal O(-1))$ and $H(\mathcal O(1))$ has underlying bundle $\mathcal O(-1)\oplus\mathcal O(1)$, whose twist is $\mathcal O(-2)\oplus\mathcal O$ and has one section. The proposed equality therefore has invariants $0$ and $2$, proving that the hyperbolic map does not factor through exact $K_0$.

The invariant also excludes equality after adding the same quadratic bundle to both sides. This concerns the manuscript's split definition, not a Grothendieck–Witt group with further relations.

## W06 — An explicit affine hyperbolic isometry without dividing by two

**Hypotheses and source anchor:** $R$ is any commutative ring, $M$ is finite projective, and $q:M\to R$ is quadratic with nonsingular polar pairing $b(x,y)=q(x+y)-q(x)-q(y)$. This addresses cote 133, scans 007–008.

First choose a bilinear form $\beta$ satisfying $\beta(x,x)=q(x)$. Such a choice exists: embed $M$ as a direct summand of $R^N$ with projection $p$, extend $q$ to $\widetilde q=q\circ p$, and choose a basis $e_i$ of $R^N$. Define a bilinear form by
\[
\widetilde\beta(e_i,e_i)=\widetilde q(e_i),\qquad
\widetilde\beta(e_i,e_j)=b_{\widetilde q}(e_i,e_j)\ (i<j),\qquad
\widetilde\beta(e_i,e_j)=0\ (i>j).
\]
The quadratic expansion of $\widetilde q(\sum_i a_i e_i)$ proves that its diagonal is $\widetilde q$; restriction gives $\beta$. Equivalently, the quadratic form is represented in $\operatorname{Sym}^2(M^\vee)$ and admits a lift through $M^\vee\otimes M^\vee\twoheadrightarrow\operatorname{Sym}^2(M^\vee)$; the dual is essential here.

Define
\[
\Phi:M\oplus M\longrightarrow M\oplus M^\vee,
\qquad
\Phi(x,y)=\bigl(a=x-y,\ b(-,y)+\beta(-,a)\bigr).
\]
The hyperbolic value of the image is
\[
b(a,y)+\beta(a,a)=b(a,y)+q(a)=q(x)-q(y).
\]
Moreover, from $(a,\varphi)$ one recovers
\[
y=(b^\sharp)^{-1}\bigl(\varphi-\beta(-,a)\bigr),\qquad x=a+y,
\]
where $b^\sharp(y)=b(-,y)$ is invertible by nonsingularity. Thus $\Phi$ is an isometry $(M,q)\perp(M,-q)\simeq H(M)$ over $R$, with no use of $1/2$. The bilinear lift need not be equivariant or available globally on an arbitrary ringed topos; W07 tests precisely that limitation.

## W07 — An equivariant obstruction over $\mathbb F_2$

**Hypotheses and source anchor:** representations of the finite group $G=C_2$ over $k=\mathbb F_2$, with ordinary equivariant quadratic isometries; cote 133, scan 008.

Let $M=k^2$ with $q(x,y)=xy$, and let the generator interchange coordinates. Its polar form has matrix $\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, so it is nonsingular. Set $F=(M,q)\perp(M,q)$; here $q=-q$. The representation $M$ is the indecomposable block $J_2$, and
\[
F^G=\{((a,a),(b,b)):a,b\in k\},\qquad q_F|_{F^G}=a^2+b^2\ne0.
\]

If $F\simeq H(E)$, then $\dim E=2$. For any such representation, $(g-1)^2=0$, so its Jordan form is either the trivial representation $k^2$ or $J_2$. Since $g-1$ has rank two on $F$, the trivial possibility is excluded and $E\simeq J_2$.

Writing $v=(1,1)$ and $\ell(x,y)=x+y$, one has $E^G=kv$ and $(E^\vee)^G=k\ell$. Every fixed vector of $H(E)$ therefore has the form $(av,b\ell)$ and quadratic value $ab\ell(v)=0$. This contradicts the nonzero restriction on $F^G$, an invariant of equivariant isometry. After forgetting the action, $M$ itself is a hyperbolic plane, so $F$ is hyperbolic.

This proves **non-isometry to any equivariant hyperbolic object**. It does not, without another argument, prove a nonzero class in the cokernel defining the manuscript's $W(S)$, where stabilization and differences of hyperbolic classes must also be considered.

## W12 — The relevant real rank is two, not four

**Hypotheses and source anchor:** the analytic bundle associated with $L=\mathcal O(1)$ on $\mathbb P^1_{\mathbb C}$; cote 133, scan 004. This calculation is topological and does not assert a formula on every ringed topos.

Choose a Hermitian metric $h$, linear in its first variable, on $L$. Inside the complex orthogonal bundle
\[
E=H(L)=L\oplus L^\vee,\qquad q(v,\varphi)=\varphi(v),
\]
the vectors $(v,h(-,v))$ form a real rank-two subbundle $F$ on which $q=h(v,v)$ is positive definite. It is naturally the real plane underlying $L$, and its complexification is $E$. Thus $F$ is the real orthogonal reduction used to define the characteristic classes of this complex orthogonal bundle (Laborde, 1976, §I, p. 47; §II, pp. 48–49).

The standard realification identity gives
\[
w_2(F)=c_1(L)\bmod2\ne0;
\]
$c_1(\mathcal O(1))$ generates $H^2(\mathbb P^1(\mathbb C);\mathbb Z)$. The identity and the line-bundle example are recorded in Hatcher (2017, Proposition 3.8, p. 83).

In contrast, forgetting the complex structure on the entire complex rank-two bundle gives a real rank-four bundle $E_{\mathbb R}$, for which
\[
w_2(E_{\mathbb R})=c_1(E)\bmod2
=(c_1(L)+c_1(L^{-1}))\bmod2=0.
\]
These are different characteristic-class constructions; using the rank-four bundle would lose the intended quadratic-bundle test.

## W16 — A finite-group splitting in dimension two

**Hypotheses and source anchor:** $V^\vee=\mathbb F_2\{x,y\}$ and $G=\mathrm{GL}_2(\mathbb F_2)$; supplied `context/ps_chapters_VI_VII/ps6.tex`, §122, original p. 517, equation (18′).

The sequence has maps $\ell\mapsto\ell^2$ and polarization, with
\[
\pi(x^2)=\pi(y^2)=0,\qquad \pi(xy)=x\wedge y.
\]
It is exact by these formulas and the dimensions $2,3,1$. Put $Q=x^2+xy+y^2$. Substitution gives $Q(y,x)=Q(x,y)$ and $Q(x+y,y)=Q(x,y)$, so $Q$ is invariant under generators of $G$. Also $\pi(Q)=x\wedge y$, and $G$ acts trivially on $\Lambda^2V^\vee$ because $\mathbb F_2^\times=\{1\}$. Therefore $x\wedge y\mapsto Q$ is a $G$-equivariant section.

This contradicts the supplied context's dimension-two nonsplitting claim for the finite automorphism group. It neither settles higher dimensions nor gives a group-scheme section: diagonal matrices over larger characteristic-two fields do not preserve the line spanned by $Q$ with its required determinant action.

## P02 — A grading-preserving automorphism requiring an odd implementer

**Hypotheses and source anchor:** ordinary associative superalgebras over $k=\mathbb Q$, with parity-preserving homomorphisms; cote 133, scan 012, printed p. 448, Theorem 1.

Take $A=B=\operatorname{End}_k(k^{1|1})$, with diagonal even part and off-diagonal odd part. These are split central simple superalgebras. For
\[
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
f=\mathrm{id},\qquad g(a)=SaS^{-1},
\]
$g$ preserves parity, since conjugation by the homogeneous odd unit changes degree by $1+1=0$. But $g(e_{11})=e_{22}$, and every even unit $s$ is diagonal. Thus $s^{-1}g(e_{11})s=e_{22}\ne e_{11}=f(e_{11})$, excluding the asserted even conjugator.

Elduque and Villa's parity-sensitive formulation distinguishes even and odd implementers (2008, §2.2, Proposition 8 and Remark 10; checked in the 2007 preprint, pp. 4–5). Their signed inner-automorphism convention is not needed for the explicit matrix contradiction above.

## P03 — Failure of cancellation for graded tensor products

**Hypotheses and source anchor:** finite-dimensional super vector spaces over $k=\mathbb Q$, with the Koszul graded tensor product; cote 133, scan 013, printed p. 449, Theorem 3.

For homogeneous endomorphisms, the rule
\[
(a\widehat\otimes b)(v\widehat\otimes w)
=(-1)^{|b||v|}av\widehat\otimes bw
\]
gives a graded-algebra isomorphism
$\operatorname{End}(V)\widehat\otimes\operatorname{End}(W)\simeq\operatorname{End}(V\widehat\otimes W)$: composition gives exactly the Koszul multiplication sign, and matrix units give a bijection.

Set $A=C=\operatorname{End}(k^{1|1})$ and $B=\operatorname{End}(k^{2|0})$. Both $k^{1|1}\widehat\otimes k^{1|1}$ and $k^{2|0}\widehat\otimes k^{1|1}$ have superdimension $2|2$, so
\[
A\widehat\otimes C\simeq\operatorname{End}(k^{2|2})
\simeq B\widehat\otimes C.
\]
Nevertheless $\dim_k A_1=2$ and $\dim_k B_1=0$, excluding a graded isomorphism $A\simeq B$. All three algebras are split graded Azumaya algebras over the semilocal ring $\mathbb Q$. The contradiction concerns isomorphism cancellation; it says nothing against the group structure on Brauer–Wall equivalence classes.

## References and checked versions

Elduque, A., & Villa, O. (2008). The existence of superinvolutions. *Journal of Algebra, 319*(10), 4338–4359. [https://doi.org/10.1016/j.jalgebra.2007.10.044](https://doi.org/10.1016/j.jalgebra.2007.10.044). Technical locator checked in [arXiv:0704.3127v1, April 24, 2007](https://arxiv.org/pdf/0704.3127), §2.2, pp. 4–5.

Hatcher, A. (2017). *Vector bundles & K-theory* (Version 2.2, November 2017). [Author's PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf). Proposition 3.8, numbered p. 83.

Laborde, O. (1976). Classes de Stiefel-Whitney en cohomologie étale. *Bulletin de la Société mathématique de France. Mémoire, 48*, 47–51. [https://doi.org/10.24033/msmf.201](https://doi.org/10.24033/msmf.201). [Primary PDF](https://www.numdam.org/article/MSMF_1976__48__47_0.pdf), §§I–II, pp. 47–49.
