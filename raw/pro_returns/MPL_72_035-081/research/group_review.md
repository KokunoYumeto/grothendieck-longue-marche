# Review of the centralizer and invariant-quadratic calculations

This review uses the explicit chain model defined in `invariant_subspaces.md`, the frozen text of scans 038–043, 054–055 and 073–074, and the root's `group_quadric_checks.py`. No frozen file was changed. The directly relevant context entries are **Hua, findings register, 72-automorphisms-deform-gm-to-ga** (supplied in `context/notes/RESULTS_STATE.md`, referring to our scans 038–039) and **Hua, findings register, 72-invariant-subspaces-string**; their recorded statuses remain prior-run claims.

## GR1. The full linear centralizer calculation is valid over the stated ring

Take the free module $E=Ra_{-1}\oplus Ra_0\oplus\cdots\oplus Ra_n$, $n\ge1$, with the functionals $\phi_i$ of scan 059, $N_i=a_i\phi_i$, and $T_i=I+N_i$; the units $1+\mu_i$ give the displayed inverse of each $T_i$. Let $F$ commute with every $T_i$. Evaluating $FN_i=N_iF$ at $a_{i-1}$ gives

\[
 F(a_i)=c_i a_i,\qquad c_i=\phi_i(Fa_{i-1}),
\]

and the full equality then gives $\phi_iF=c_i\phi_i$, because the map $R\to E$, $r\mapsto ra_i$, is injective. For $i\ge1$, evaluation at $a_{i-1}$ yields $c_i=c_{i-1}$ through the unit entry $\phi_i(a_{i-1})=1$.

Thus $F-cI$ kills $V=\operatorname{span}(a_0,\ldots,a_n)$ and has the unique form $v\pi$, where $\pi(a_{-1})=1$ and $\pi(V)=0$. The equations $\phi_iF=c\phi_i$ give $\phi_i(v)=0$; the triangular unit minor in the functional matrix identifies this common kernel with $Rw$, where $w_n=1$. Consequently

\[
 \operatorname{End}_{(T_i)}(E)
 =\{cI+t w\pi:c,t\in R\}.
\]

This is an isomorphism of $R$-algebras from $R[A]/(A^2-\rho A)$ by $A\mapsto w\pi$, $\rho=\pi(w)$: the relation follows from evaluation, and linear independence of $I,w\pi$ follows by restriction to $V$ and then evaluation at $a_{-1}$.

The determinant is $c^{n+1}(c+\rho t)$. Its invertibility forces both $c$ and $c+\rho t$ to be units, so $u=t/c$ gives the exact group isomorphism

\[
 \mathbf G_m\times U_\rho
 \longrightarrow\operatorname{Aut}_{(T_i)}(E),
 \qquad (c,u)\longmapsto c(I+u w\pi),
\]

with $u*u'=u+u'+\rho uu'$ and inverse recovered from the unique coefficients $c,t$. This proves the linear part of the isomorphism asserted on scan 039 within the recorded frame, without a reduced-ring or field assumption.

## GR2. The projective centralizer also has a ring-level proof, with a dimension bound

Work in the fppf sheaf $\operatorname{PGL}(E)=\operatorname{GL}(E)/\mathbf G_m$, and centralize the ordered projective operators $[T_i]$. A projective centralizer element has local lifts $g\in\operatorname{GL}(E)$, with

\[
 gT_ig^{-1}=\epsilon_iT_i,\qquad \epsilon_i\in R^\times.
\]

Hence the rank-one matrix $gN_ig^{-1}$ equals

\[
 M=(\epsilon_i-1)I+\epsilon_iN_i.
\]

Number the basis positions $0,\ldots,n+1$, so $N_i$ has its unit entry in row $i+1$, column $i$. Choose a position $k$ different from $i,i+1$, which exists because $\operatorname{rank}E=n+2\ge3$. The minor of $M$ on rows $(i+1,k)$ and columns $(i,k)$ is $\epsilon_i(\epsilon_i-1)$; every two-by-two minor of the displayed outer product $gN_ig^{-1}$ vanishes, so $\epsilon_i=1$ over the actual ring, including its nilpotents.

The local lifts therefore belong to the linear centralizer in GR1. On overlaps they differ by a scalar, and their coefficients satisfy $(c,t)\mapsto(\lambda c,\lambda t)$, so $u=t/c$ agrees and descends; the global matrix $I+u w\pi$ represents the original projective element. This proves

\[
 U_\rho\xrightarrow{\sim}
 \operatorname{Cent}_{\operatorname{PGL}(E)}([T_0],\ldots,[T_n])
\]

for the specified model and $n\ge1$. The argument centralizes each labelled operator; it makes no statement about transformations permuting the labels. For a centred module $V$ of rank $n+1$, the rank threshold becomes $n\ge2$, matching the low-dimensional caveat on scan 076; the additional first-generator check is supplied in GR2b below.

The rank condition is essential. In dimension two over a field with $2$ invertible, a matrix exchanging the two eigenlines of $\operatorname{diag}(1,-1)$ conjugates that matrix to its negative, giving projective commutation with a scalar factor $-1$; this explicitly identifies the obstruction to applying the three-row minor argument there.

## GR2b. The centred first-generator check also works over rings with nilpotents

Use the centred basis $(a_0,\ldots,a_n)$ with $n\ge2$ and the invertible restricted pairing matrix $B$. The matrix $N_0$ has only its first row nonzero, namely $(\mu_0,\beta_0,0,\ldots,0)$; the identity $BB^{-1}=I$ gives $(\mu_0,\beta_0)=R$. Put $\delta=\epsilon-1$ and $M=\epsilon T_0-I=\delta I+\epsilon N_0$, where $\epsilon$ is a unit and $M$ has vanishing two-by-two minors.

Number rows and columns from zero. The following three actual minors give

\[
\begin{array}{c|c|c}
\text{rows}&\text{columns}&\text{minor}\\\hline
(1,2)&(1,2)&\delta^2=0\\
(0,1)&(0,1)&\delta^2+\epsilon\mu_0\delta=0\\
(0,2)&(1,2)&\epsilon\beta_0\delta=0.
\end{array}
\]

Since $\epsilon$ is invertible, these equations give $\mu_0\delta=\beta_0\delta=0$. Choose $r,s\in R$ with $r\mu_0+s\beta_0=1$, obtained explicitly from the first column of $B^{-1}$; multiplication by $\delta$ now gives $\delta=0$. For every $i\ge1$, the predecessor entry is already $1$, and the unit-entry minor from GR2 applies with a third basis position.

Thus scalar factors in projective commutation disappear for every centred generator in this localized model, including over nonreduced rings. The same calculation applies to two scalar-related lifts whose differences from the identity have vanishing two-by-two minors, and proves the scalar-lift uniqueness at $n\ge2$. The existence claim on scan 076 still calls for its asserted local lifting construction; these equations establish the uniqueness step without inverting $2$.

## GR3. The centred quadratic-form argument is valid after inverting the pairing determinant

On the reflection chart $\mu_i=-2$, take $V=\bigoplus_{i=0}^nRa_i$ over the localization where $\rho$ is invertible. The restricted pairing matrix $B=(\phi_i(a_j))$ is invertible, since $\det B=(-1)^{n+1}\rho$. The coordinate change $y=Bx$ sends every $\phi_i(x)$ to a coordinate variable, so multiplication by $\phi_i(x)$ is injective in the polynomial ring even over a ring with zero divisors.

For a quadratic form $q$, let $b_q$ denote its polar bilinear form. The exact expansion

\[
 q(T_ix)-q(x)
 =\phi_i(x)\bigl(b_q(a_i,x)+\phi_i(x)q(a_i)\bigr)
\]

therefore gives $b_q(a_i,-)=-q(a_i)\phi_i$ for invariant $q$. Symmetry, evaluated at $a_i,a_{i+1}$, gives

\[
 q(a_{i+1})=\beta_iq(a_i),
\]

and all nonadjacent polar coefficients vanish. The diagonal equations use $b_q(a_i,a_i)=2q(a_i)$ and $\mu_i=-2$, with no division by $2$.

Put $B_0=1$ and $B_i=\beta_0\cdots\beta_{i-1}$. The explicit quadratic form

\[
 q_V(x)=\sum_{i=0}^nB_ix_i^2-
          \sum_{i=0}^{n-1}B_{i+1}x_ix_{i+1}
\]

satisfies $b_{q_V}(a_i,-)=-B_i\phi_i$ and hence $q_V(T_ix)=q_V(x)$ by the same expansion. Every invariant form is $q(a_0)q_V$, and $q_V(a_0)=1$; thus evaluation at $a_0$ is the claimed module isomorphism to $R$.

The determinant localization supplies the cancellation step. Outside that locus, the example $n=1$, $R=\mathbf F_2$, $\beta_0=0$ has $T_0|V=I$ and the nontrivial transvection $T_1|V$; both $x_0^2$ and $x_1^2+x_0x_1$ are invariant and linearly independent. This provides an explicit boundary case for the scope of the rank-one module assertion on scan 073.

## GR4. The characteristic-two reading checks are correct and admit scheme-level explanations

For scan 043's $n=1$ example over $\mathbf F_2$ with $\beta_0=1$, the parameters are $\rho=1$, $\sigma=0$, and $\widetilde\sigma=1$. The recorded preservation equation is $t^2=0$; under the exact character $v=1+t$, its group scheme is $\mu_2$, and every geometric point has $t=0$. Consequently no locally defined section can be nonidentity on every geometric fibre, even though the group scheme retains a nilpotent infinitesimal direction; the root's geometric-section objection to the literal example is therefore valid beyond the rational-point count, while the later condition involving the unit $\sigma\widetilde\rho$ excludes this tuple.

For scan 054 in the same tuple, $o'=2w/\rho=0$ and $\underline a=-I+o'\pi=I$ in characteristic two. Its fixed subscheme is all of $E$, and its projective fixed subscheme is all of $\mathbf P(E)$; the seven versus three $\mathbf F_2$-point counts in `group_quadric_checks.py` give a concrete witness. The manuscript's own margin already records “$o'=0$ d'où $\underline a=\mathrm{id}$,” so the later blanket fixed-locus sentence should be noted as an internal qualification or reading issue alongside that marginal observation.

## Review disposition

The root's two proposed proofs are valid with the explicit model, the units $1+\mu_i$, and the centred determinant localization stated as above. The projective equality follows from the additional unit-minor and descent argument in GR2; it should not be inferred merely from the linear quotient without that argument. These calculations support and qualify **Hua, findings register, 72-automorphisms-deform-gm-to-ga** in the recorded frame and supply exact counterexamples for the two characteristic-two reading questions, while preserving the prior-run status of the supplied register entry.
