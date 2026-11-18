# Post-freeze projective-algebra checks

Run: MPL_93_047-091; checker: GPT-6 Astra Pro, inherited reasoning setting (no separate effort override exposed). These checks were made after the 10:49:51 UTC transcription freeze and do not amend it. The executable companion is `scripts/check_projective_algebra.py`; its exact-arithmetic output is `records/projective_algebra_certificate.json`. It is a symbolic calculation, not a proof-assistant formalization.

## A. Normalizations and the characteristic-two obstruction

Represent the three sections of `pgl_2` by

\[
e=E_{12},\qquad h=\operatorname{diag}(1,0)\pmod{\mathcal O I},\qquad f=E_{21}.
\]

Their brackets are `[e,h]=-e`, `[f,h]=f`, `[e,f]=2h`, exactly the normalization used on scan088. For `A=ae+bh+cf`, in the ordered basis `(e,h,f)`,

\[
\operatorname{ad}(A)=
\begin{pmatrix}b&-a&0\\-2c&0&2a\\0&c&-b\end{pmatrix}.
\]

The bracket identities and Jacobi identity were checked over the integers. The trace pairing of these adjoint matrices is

\[
K=\begin{pmatrix}0&0&4\\0&2&0\\4&0&0\end{pmatrix},\qquad\det K=-32.
\]

Thus, where 2 is invertible, the pairing is perfect and the orthogonal complement of `Oe` is `Oe+Oh`. This proves the conditional assertion on scan087, without using the modernized context as evidence.

The derivation equations `D[x,y]=[Dx,y]+[x,Dy]` are nine integral linear equations in the nine matrix entries of `D`. Their Smith diagonal is `(1,1,1,2,2,2,0,0,0)`; direct solution after inverting 2 gives

\[
D=\begin{pmatrix}-z&-u/2&0\\-2v&0&u\\0&v&z\end{pmatrix}
=\operatorname{ad}((u/2)e-zh+vf).
\]

The last expression works over every ring in which 2 is invertible, not only over a field. In characteristic two the solution space over a field instead has dimension six: `D(h)` can be any element of `W=span(e,f)` and `D|W` can be any two-by-two endomorphism. The specific map `D(e)=f`, `D(f)=D(h)=0` satisfies every derivation equation in characteristic two and is outer because an inner derivation has zero f-coordinate on e. This refutes the unqualified assertion on scan089 and supports the qualification on scan090.

The same map gives a bracket-compatible connection `d+D dt` on the trivial Lie bundle over `A^1` in characteristic two. It is flat because the base is a smooth curve, but it sends `e` to `f dt`, outside `(Oe+Oh)dt`; hence the unqualified filtration assertion also fails for arbitrary Lie-compatible connections. Connections induced on this Lie bundle by a `PGL_2`-bundle have inner differences and are not counterexamples to the corrected group-bundle formulation.

For `sl_2` use `E12,H=diag(1,-1),E21`; the bracket coefficients are `-2,+2,1`, agreeing with scan088. In characteristic two H is central in `sl_2`, whereas `pgl_2` has zero centre, so these Lie algebras are not isomorphic. Also, `ad(h)` is scalar on W in characteristic two: every line in W is normalized by h, so a Lie-theoretic claim that precisely two such lines are distinguished needs the characteristic restriction or the algebraic-group structure.

## B. Gluing and the question g/Omega = L-dual

For an upper triangular change of frame

\[
T=\begin{pmatrix}a&b\\0&1\end{pmatrix},\qquad a\text{ invertible},
\]

direct conjugation, projected modulo scalars, gives

\[
\operatorname{Ad}T=
\begin{pmatrix}a&-b&-b^2/a\\0&1&2b/a\\0&0&1/a\end{pmatrix}.
\]

The Borel submodule B with ordered basis `(e,h)` has upper-left transition matrix. On `g/Oe`, in basis `(h,f)`, the matrix is `[[1,2b/a],[0,1/a]]`; on `B^dual`, in basis `(h^dual,e^dual)`, it is `[[1,b/a],[0,1/a]]`. The Killing map is the intertwiner `diag(2,4)`, which is an isomorphism after inverting 2. This answers the margin's question under the page's good-characteristic condition.

There is also a global counterexample to dropping that condition. Take a smooth proper genus-one curve over an algebraically closed field of characteristic two and a nonsplit extension `0 -> O -> V -> O -> 0`. Such an extension exists because `H^1(O)` is one-dimensional. Its unipotent transition functions have a nonzero additive Cech cocycle b. The Borel bundle B has that nonzero extension class (up to sign), so `B^dual` is nonsplit; the displayed matrix shows `g/Oe` is split since `2b=0`. The two bundles are not isomorphic: the nonsplit extension has `h^0=1`, whereas `O^2` has `h^0=2`. This construction uses standard genus-one cohomology as background; the transition calculation and the cohomology exact-sequence argument were checked here.

## C. The question about first jets of the vertical tangent

On a Brauer--Severi curve `f:P->X`, the relative principal-parts sequence for the line `t=T_{P/X}` is

\[
0\to\mathcal O_P\to P^1_{P/X}(t)\to t\to0.
\]

After pushing forward, `R^1f_*O_P=0`, checked étale locally on `P^1`, so this gives `0 -> O_X -> f_*P^1(t) -> g -> 0`. The universal first jet `d^1:t->P^1(t)` is `f^{-1}O_X`-linear, and therefore pushes forward to a canonical `O_X`-linear splitting: `f_*P^1(t)=O_X direct-sum g` as modules. If 2 is invertible, the reduced trace divided by 2 splits `0 -> O_X -> M -> g -> 0`, giving a canonical compatible module identification in that setting.

This is not an algebra identification. Nor does the argument give a canonical identification in characteristic two: already for the universal split two-dimensional representation, every conjugation-invariant linear functional on `End(V)` is a multiple of trace, and its value on I is zero in characteristic two. To check this last statement, invariance under diagonal matrices forces the off-diagonal coefficients to vanish and invariance under the transposition matrix equates the two diagonal coefficients. Thus there is no `PGL_2`-equivariant retraction to the scalar subrepresentation, while the pushed-forward first-jet extension is canonically split. The manuscript's word after the question is uncertain, so the negative conclusion is limited to such a canonical, structure-compatible reading of the question.

## D. Connections, filtration, and the characteristic-two margin

For a connection induced from the projective bundle, write it locally as `C=d+ad(A)` with the matrix in A. With `F1=Oe`, `F2=Oe+Oh`, `F3=g`, it raises filtration by at most one; the induced maps have coefficients `c12=-2c` and `c23=c`. Leibniz terms vanish in the next graded quotient, proving their `O_X`-linearity. Preservation of the whole flag is equivalent to `c=0`, the condition that the connection preserve the Borel reduction and the marked section.

The normal component is intrinsic: a change of frame preserving the marked section lies in the Borel, and its derivative term is Borel-valued. Consequently the quotient of the connection torsor by `B tensor omega` is canonically identified with `Omega^{-1} tensor omega`; its zero is the condition of preserving the section. A fixed normal component i leaves a torsor under `B tensor omega`. The restriction to `Omega` is a first-order differential operator with the displayed Leibniz symbol, and, at fixed i, its kernel of variation is `Omega tensor omega`.

The margin on scan090 does retain more information in characteristic two. In `C(e)=b e-2c h` the coefficient c disappears then, while the induced operator

\[
c^\Omega:g/\Omega\longrightarrow(g/B)\otimes\omega
\]

sends the class of h to `c f` and still detects it. The induced operator is well-defined because `C(Omega)` lies in `B tensor omega`; no identification of `g/Omega` with `B^dual` is needed. For 2 invertible its data `(b,c)` is equivalent to that of `C|Omega`; it still does not determine the missing coefficient a of a complete connection.

## E. Canonical restricted data on scan091

Put `omega=Omega^1_{X/S}` and suppose the line Omega is included in the rank-two extension B. Suppose `C_Omega:Omega->B tensor omega` has symbol the inclusion, and its composite `j:Omega->omega` is an isomorphism. In the manuscript's connection setting `j=-2i`, so its being invertible implies that 2 and i are invertible, locally and hence globally.

The universal property of first principal parts gives a unique linear map

\[
\phi:P^1_{X/S}(\Omega)\longrightarrow B\otimes\omega.
\]

It induces the identity on the kernel `Omega tensor omega` and j on the quotient Omega. It is therefore an isomorphism of short exact sequences. Use j, rather than i, to identify Omega with omega; functoriality of principal parts then identifies

\[
B\simeq P^1_{X/S}(\omega)\otimes\omega^{-1},
\qquad C_\Omega=d^1_\omega.
\]

This proves existence and uniqueness of the *restricted* triple under the stated line-bundle and 2-invertibility hypotheses. It does not assert that a global full connection extending the restricted triple exists over every base. Locally the remaining variation is `Omega tensor omega`, which identifies with `omega^{tensor 2}`; global extensions, if present, form a torsor under `H^0(X, omega^2)`, and their sheaf is a torsor under `omega^2`. The Hua text's `Omega^2 tensor omega = omega^2` in §VII is not the tensor calculation made here; under `Omega=omega`, that left-hand expression would have degree three.

The principal-parts exact sequence and universal property were compared with the Stacks Project, tags 09CN and 09CH. The modern oper comparison is only invoked in the scope actually stated by Beilinson--Drinfeld: smooth complex curves; it is not used as a theorem for arbitrary characteristic or a source for the diplomatic reading.
