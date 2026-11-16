# A source-compatible tangential Galois action on the literal product-one inertia

Research record, 2026-11-16, checkpoint 15. The local model was proposed by the
root; DE independently certified its precise based meridian. This note proves
the selected-action comparison. It does not prove whole marginal normality.

## 1. An explicit rational partial compactification

On the actual ordered surface

\[
Y=\{(v,w)\in(\mathbb C^*)^2:v,w\notin\mu _5,
v\ne w,\ vw\notin\mu _5\},
\]

put

\[
t=w-1,\qquad q=\frac{vw-1}{(w-1)^2}.
\]

Both denominators are invertible on \(Y\), and \(q\ne0\). Conversely,

\[
w=1+t,\qquad v=\frac{1+qt^2}{1+t}.
\]

Define polynomials

\[
\begin{aligned}
W(t)&=\frac{(1+t)^5-1}{t},\\
V(t,q)&=\frac{(1+qt^2)^5-(1+t)^5}{t},\\
D(t,q)&=-2+(q-1)t,\\
P(t,q)&=\frac{(1+qt^2)^5-1}{qt^2},\\
F(t,q)&=(1+t)(1+qt^2)W(t)V(t,q)D(t,q)P(t,q).
\end{aligned}
\]

The displayed quotients are polynomials. The equations defining the deleted
boundary give an exact rational isomorphism

\[
Y\cong\operatorname{Spec}\mathbb Q[q,q^{-1},t,t^{-1},F(t,q)^{-1}].
\]

In particular, this is not merely a formal change of variables. Since
\(F(0,q)=250\), the smooth relative curve

\[
U=\operatorname{Spec}\mathbb Q[q,q^{-1},t,F(t,q)^{-1}]
\longrightarrow B=\mathbb G_{m,q}
\]

contains the section \(S=\{t=0\}\cong B\), and \(Y=U\setminus S\).
Its relative normal line has the global parameter \(t\). Its punctured normal
bundle is therefore

\[
N^\times_{S/U}=\mathbb G_{m,q}\times\mathbb G_{m,n}.
\]

Geometrically this is the finite-\(q\) chart of two blowups at rational
centers. In coordinates \(x=vw-1\), the first blowup has \(x=tq_1\),
and the second has \(q_1=tq\). The second exceptional divisor has punctures
\(q=0\) from product one and \(q=\infty\) from the previous exceptional
divisor. The strict equations of the other two branches through the original
point are \(qt=1\) for \(v=1\) and \(qt=2+t\) for \(v=w\); they leave
every finite-\(q\) neighborhood as \(t\to0\).

The actual source satisfies

\[
v=2-w=1-t,\qquad vw=1-t^2,\qquad q=-1.
\]

Thus its normal vector toward the negative real \(t\)-axis is the rational
point \((q,n)=(-1,-1)\) of the punctured normal bundle.

## 2. Finite-étale specialization and the selected action

Apply the relative finite-étale normal-specialization construction of Deligne
(1989, §15.19) to the smooth relative curve \(U/B\) and the étale section
\(S/B\). A finite étale cover of \(Y\) is tamely ramified along \(S\),
since the residue characteristics here are zero. Normalizing across \(S\)
and taking the leading normal terms gives a finite étale cover of
\(N^\times_{S/U}\). This construction descends over \(\mathbb Q\), is
functorial for the source and the filling maps, and agrees with the local
topological normal construction after the chosen complex embedding.

Take the fiber at the rational point \((-1,-1)\). It supplies a rational
tangential fiber functor and hence a genuine selected action of
\(G_{\mathbb Q}\) on the geometric profinite fundamental group. On the
geometric fundamental group of the split normal torus,

\[
\pi _1(N^\times_{S/U,\overline{\mathbb Q}},(-1,-1))
\cong\widehat{\mathbb Z}(1)^2,
\]

the action is multiplication by the cyclotomic character on both factors.
This also follows directly from the two systems of Kummer covers of the
split torus. We do not need injectivity of its map into \(\pi _1(Y)\).

In fact injectivity can be checked here: the global unit map
\((q,t):Y\to\mathbb G_m^2\), followed on normal specializations, is
\((q,n)\mapsto(q,n)\). Thus its map on geometric fundamental groups is a
left inverse to the normal-torus map. The two actual local loops form a split
embedded \(\widehat{\mathbb Z}^{2}\). This observation only concerns this
two-generator subgroup; it gives no normality of the source image.

**Primary-source verification.** Deligne §15.17 establishes compatibility
with the classical construction, §15.18 gives descent over a field that need
not be algebraically closed, §15.19 gives the relative normal construction,
and §§15.22–15.26 give its formal interpretation. These passages were opened
and read in the author's primary PDF. The present application is to a
relative curve with one smooth section, so it does not require an unstated
higher-dimensional version of that theorem.

## 3. The actual based generator, including orientation

DE's certificate fixes the actual northeast corner

\[
w_c=1+10^{-4}+i10^{-4}
\]

of the stored \(w=1\) lasso and holds \(t=w_c-1\) constant. Moving the
source along

\[
q:-1\longrightarrow-i\longrightarrow1\longrightarrow i\longrightarrow-1
\]

gives the positive conventional \(q\)-meridian. Four exact polynomial/Sturm
segments give the local braid \(\sigma_{10}^2\). With the stored
inverse-conjugator convention its fiber word is \(x_{10}^{-1}\), and after
the already certified common source whisker its adapted word is exactly
\(b^{-1}\). There is no additional conjugating word.

Certificate paths:

- `work_DE/next_marginal_source/check_w1_local_q_meridian.py`
- `work_DE/next_marginal_source/check_w1_local_q_meridian.out`
- `work_DE/next_marginal_source/w1_local_q_meridian.json`

We transport the entire pointed source/filling diagram from the rational
tangential functor to the original base using this same geometric source
whisker, extended locally along \(q=-1\) to the normal direction \(-1\).
The extension is inside the punctured local \(t\)-disc. Its ambiguity is a
power of the normal loop; that loop commutes with the \(q\)-loop in the
punctured normal torus. Consequently it does not alter the literal based
\(q\)-meridian identification.

No Galois-invariant global path is asserted or needed. We transport a selected
action by an isomorphism of geometric fiber functors. This action at the old
base need not equal the action attached to that old rational point's own
section. The same source path is used for every map, which is what preserves
the actual based diagram.

It follows, with DE's sign retained, that the transported action satisfies

\[
\rho(\sigma)(b^{-1})=b^{-\chi(\sigma)},
\qquad\rho(\sigma)(b)=b^{\chi(\sigma)}.
\]

The normal source loop is acted on cyclotomically as well. This is stronger
than preservation of the conjugacy class of \(b\), but it is a statement
about this selected source-compatible action.

## 4. Source kernels and permitted consequences

The source, the constant-family filling, and the moving-family filling are
defined over \(\mathbb Q\): the four nonidentity fifth roots form a Galois
stable set. Their tangential basepoints are the compatible images of the same
one above. Thus the actual closed source image \(H\), both actual source
kernel images \(J_c,J_m\), and \(I=J_cJ_m\) are preserved by \(\rho\).

For the actual source inertia \(c_j\) at \(w=2-\zeta _5^j\), the usual
pointed inertia functoriality gives

\[
\rho(\sigma)(c_j)
=h_{\sigma,j}\,c_{\bar\chi(\sigma)j}^{\chi(\sigma)}h_{\sigma,j}^{-1},
\qquad h_{\sigma,j}\in H,
\]

where indices are taken modulo 5. This is an \(H\)-conjugacy statement; the
conjugators are not suppressed. In particular an element sending
\(\zeta _5\) to \(\zeta _5^2\) carries the inertia classes indexed by
\(1,4\) to those indexed by \(2,3\).

If a **closed** subgroup \(K\subset J_c\) is normalized by \(b\), then
\(\rho(\sigma)K\subset J_c\) is normalized by \(b^{\chi(\sigma)}\),
and hence by \(b\), since \(\chi(\sigma)\) is a full profinite unit. This
applies to a proved controlled subgroup such as the one in B83.

It does not prove that the whole \(J_c\) is \(b\)-normal. The transported
inertia elements may have nontrivial \(H\)-conjugators, and conjugating a
\(b\)-normalized subgroup by an arbitrary element of \(H\) need not preserve
\(b\)-normalization. The other actual source directions remain part of the
unresolved whole-subgroup condition.

## Reference

Deligne, P. (1989). Le groupe fondamental de la droite projective moins trois
points. In Y. Ihara, K. Ribet, & J.-P. Serre (Eds.), *Galois groups over
\(\mathbb Q\)* (MSRI Publications, Vol. 16, pp. 79–297). Springer.
Verified primary source, §§15.17–15.26:
<https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf>.


## 5. Post-capture arithmetic closure and its proper source scope

B83 gives H_* = ker(chi_b restricted to T), so b normalizes H_* itself.
Literal cyclotomy therefore makes every rho_sigma(H_*) and rho_sigma(J_*)
b-normal. Their closed generated subgroups are b-normal; the closed normal
closure of the latter inside the former is b-normal as well. This needs no
new stage induction. Root and CE independently accepted this argument.

The six actual winding characters of v, w, and vw-u (u in mu5 except 1)
vanish on H_* and also on B84's stronger corrected source subgroup. Their
common kernel is Galois stable. On the actual source, the positive meridians
at w=2, w=0, and one simple root of each w(2-w)=u give the identity 6-by-6
winding matrix. Hence the arithmetic source enlargement is strictly proper
in H, with an explicit quotient separation H -> Zhat^6. The same characters
factor through Y_c and kill J_c, so they do not decide whether the arithmetic
kernel enlargement equals J_c. Exact algebraic verifier and genuine stdout:
work_A/code/check_tangential_arithmetic_scope.py/.out.
