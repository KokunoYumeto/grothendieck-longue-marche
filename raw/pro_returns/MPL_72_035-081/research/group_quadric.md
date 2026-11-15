# Rank-one automorphisms, invariant forms, and the characteristic-two checks

These are post-freeze calculations in the explicit coordinate frame of scans 048, 059, 061 and 073–074. Every comparison below leaves the diplomatic text unchanged. The exact prior-context entry is **Hua, findings register, 72-automorphisms-deform-gm-to-ga**, as excerpted in `context/notes/RESULTS_STATE.md`; its “partly proved” label is a prior-run claim. The polynomial and small-field checks are reproducible with `python3 research/group_quadric_checks.py`, which writes `group_quadric_checks_results.json`.

## A01. The group law and its coordinate identities

**72/038, “$\lambda+\lambda'+\lambda\lambda'\rho$”; kind: unpursued implication, verified calculation; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — supplies the explicit coordinate proof.** For a commutative ring $R$ and its recorded scalar $\rho$, the functor
\[
U_\rho(A)=\{t\in A:1+\rho t\in A^\times\},\qquad t*s=t+s+\rho ts
\]
has identity $0$, inverse $-t/(1+\rho t)$, and character $\chi(t)=1+\rho t$, because
\[
1+\rho(t*s)=(1+\rho t)(1+\rho s),\qquad
(t*s)*u=t*(s*u)=t+s+u+\rho(ts+tu+su)+\rho^2tsu.
\]
The coordinate maps $u=1+\rho t$ and $t=(u-1)/\rho$ give inverse group-scheme morphisms after the base change $R\to R[1/\rho]$, while $R\to R/(\rho)$ gives the additive law $t+s$. These formulas prove the two specializations cited in the Hua excerpt and identify the marked identity parameter exactly; the doubtful numeral “1” in scan 038 remains a reading question, with $0*1=1$ as a concrete check.

## A02. The Hopf algebra and the literature comparison

**72/038, “$\operatorname{Spec}\ \mathcal O_S[T]_{(1+\rho T)}$”; kind: unpursued implication, explicit morphism; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — connects the recorded family to a published construction.** Its Hopf algebra is
\[
R[t,(1+\rho t)^{-1}],\quad
\Delta(t)=t\otimes1+1\otimes t+\rho t\otimes t,\quad
\epsilon(t)=0,\quad S(t)=-t/(1+\rho t).
\]
The substitution $\lambda\mapsto\rho$, $X\mapsto t$ identifies this presentation with the one-dimensional $\mathcal G^\lambda$ family in Mézard–Romagny–Tossici, *Sekiguchi–Suwa theory revisited*, §2.2 and §3.3 ([primary paper](https://imag.umontpellier.fr/~romagny/articles/SS_theory.pdf)). This is an equality of the displayed coordinate constructions, and makes no historical-priority claim about the manuscript.

## A03. The common fixed line in the recorded frame

**72/048, 059, 061, “$\langle a_i,a'_j\rangle$”; kind: unpursued implication, proved coordinate construction; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga and Hua, findings register, 72-invariant-subspaces-string — gives their shared matrix model.** Put
\[
E=Ra_{-1}\oplus Ra_0\oplus\cdots\oplus Ra_n,\quad
V=\bigoplus_{i=0}^nRa_i,\quad \pi=a_{-1}^*,\quad
T_i=I+a_i\phi_i,
\]
where $\phi_i(a_{i-1})=1$, $\phi_i(a_i)=\mu_i$, $\phi_i(a_{i+1})=\beta_i$ for $i<n$, and the other entries are zero, with $1+\mu_i$ a unit as required by the invertibility of $T_i$. The recurrence
\[
w_n=1,\quad w_{n+1}=0,\quad
w_{i-1}=-\mu_iw_i-\beta_iw_{i+1}\quad(0\le i\le n)
\]
uses the final term only for $i<n$ and gives $w=\sum_{j=-1}^nw_ja_j$, $\bigcap\ker\phi_i=Rw$, and $\rho=\pi(w)=w_{-1}$. The coefficient $1$ on every predecessor makes this solution unique from $w_n$, and the reflection specialization $\mu_i=-2$ gives exactly the continuant recurrence of scan 052.

## A04. The complete linear centralizer

**72/039, “sont des iso.”; kind: unproved manuscript claim with a proof supplied for the recorded frame; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — verifies the linear claim in this frame.** Commutation of an endomorphism $B$ with $N_i=a_i\phi_i$ and evaluation on $a_{i-1}$ give $B(a_i)=c_i a_i$ and $\phi_iB=c_i\phi_i$, and evaluation of the latter on $a_{i-1}$ for $i\ge1$ gives $c_i=c_{i-1}$. Consequently
\[
B=cI+v\pi,\qquad\phi_i(v)=0\ (0\le i\le n),\qquad
\operatorname{End}_{(T_i)}(E)=\{cI+t\,w\pi:c,t\in R\}.
\]
Since $\det(cI+t\,w\pi)=c^{n+1}(c+\rho t)$, its units are precisely the image of
\[
\mathbf G_m\times U_\rho\longrightarrow\operatorname{Aut}_{(T_i)}(E),\qquad
(c,u)\longmapsto c(I+u\,w\pi),
\]
with inverse $(c,t)\mapsto(c,t/c)$; $c$ is a unit because $c^{n+1}(c+\rho t)$ is a unit and $n+1\ge1$.

## A05. Projectivization and the full projective centralizer

**72/039, “en passant au quotient”; kind: unproved manuscript claim with an explicit descent proof; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — verifies the projective claim for $n\ge1$ in the recorded frame.** Lift a projective centralizer element fppf-locally to $g\in\operatorname{GL}(E)$ and write $gT_ig^{-1}=\varepsilon_iT_i$; the matrix
\[
gN_ig^{-1}=(\varepsilon_i-1)I+\varepsilon_iN_i
\]
has all $2\times2$ minors zero, and its minor on rows $(i+1,k)$ and columns $(i,k)$, with $k\notin\{i,i+1\}$, is $\varepsilon_i(\varepsilon_i-1)$. Invertibility of $\varepsilon_i$ forces $\varepsilon_i=1$, so A04 applies and the scalar quotient has the explicit coordinate $u=t/c$, which is unchanged by a different lift and therefore descends. Thus $u\mapsto[I+u\,w\pi]$ is the required group-scheme isomorphism onto the projective centralizer; the predecessor entry $N_i(i+1,i)=1$ and dimension $n+2\ge3$ are the precise ingredients in the argument.

## A06. Transpose notation

**72/039, “contragrédientes” deleted and “transposées” inserted; kind: reading question; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — refines the tensor typing.** For $A(x)=\pi(x)w$ the dual operator is $A^t(\ell)=\ell(w)\pi$, whereas the contragredient group action uses $(I+tA)^{-t}$. The two tensor strings in the frozen scan 039 are identical although the targets are $\mathcal E$ and $\mathcal E'$, so the explicit maps $x\mapsto\pi(x)w$ and $\ell\mapsto\ell(w)\pi$ identify the target information that the subsequent research comparison must retain. Neither tensor string has been changed in the transcription.

## A07. A projective-line model for the torsor

**72/039–040, “$D_0^{**}$ est un torseur”; kind: unpursued implication, explicit model; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — adds a coordinate realization.** On $\mathbf P^1_R$ take the sections $d=[1:0]$, $c=[1:-\rho]$, and the open complement of their supports, which is represented on $Y\ne0$ by $R[t,(1+\rho t)^{-1}]$ through $t\mapsto[t:1]$. The matrices
\[
M(u)=\begin{pmatrix}1+\rho u&u\\0&1\end{pmatrix},\qquad
M(u)M(v)=M(u*v),\qquad M(u)[t:1]=[u*t:1]
\]
fix the two sections and give the left-translation torsor with marked point $[0:1]$. This realizes the stated two-section geometry, including their coincidence over $\rho=0$; identifying its chosen homogeneous coordinates with a particular manuscript pinning is part of the frame data, rather than an assertion that a coordinate choice is canonical without that data.

## A08. The invariant quadratic form as an explicit module

**72/073, “un $\mathcal O_S$-Module loc libre de rg $1$”; kind: unproved manuscript claim with a coordinate proof; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga and README calculation brief — supplies the form underlying the centralizer calculation.** Work on the centred reflection chart over $R[1/\rho]$, where $\mu_i=-2$ and the matrix of the restricted functionals $\phi_i|_V$ is invertible; its determinant is $(-1)^{n+1}\rho$. For a quadratic form $q$ with polar form $b_q$, the identity $q(T_ix)=q(x)$ is
\[
\phi_i(x)\bigl(q(a_i)\phi_i(x)+b_q(x,a_i)\bigr)=0,
\]
and changing coordinates by this invertible functional matrix makes $\phi_i(x)$ a polynomial variable, so cancellation is valid over this arbitrary coefficient ring. Symmetry then gives
\[
q(a_i)=\beta_{i-1}q(a_{i-1}),\qquad
b_q(a_i,a_j)=0\ (|i-j|>1),\qquad
b_q(a_i,a_{i+1})=-\beta_iq(a_i),
\]
which proves that evaluation $q\mapsto q(a_0)$ is an isomorphism from the invariant-form module to $R[1/\rho]$, with inverse $r\mapsto r f_V$ for the displayed form.

## A09. A single polynomial controls the orthogonal part of the automorphism group

**72/040–043, “$\lambda(\sigma+\lambda\widetilde\sigma\widetilde\rho)=0$”; kind: unpursued implication, exact calculation; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — adds the subgroup scheme preserving the form.** In the reflection frame put $c_{-1}=1$, $c_i=\beta_0\cdots\beta_i$ and
\[
f(x)=\sum_{i=0}^nc_{i-1}x_i^2-x_{-1}x_0-\sum_{i=0}^{n-1}c_i x_ix_{i+1},
\]
so $\Psi(w)=-\sigma\pi$ and $f(w)=-\widetilde\sigma\widetilde\rho$ give
\[
f((I+t\,w\pi)x)-f(x)
=-\pi(x)^2\bigl(t\sigma+t^2\widetilde\sigma\widetilde\rho\bigr).
\]
The preserving subgroup therefore has coordinate algebra
\[
R[t,(1+\rho t)^{-1}]/(t\sigma+t^2\widetilde\sigma\widetilde\rho),
\]
and the whole $U_\rho$ preserves $f$ exactly when both coefficients vanish, because localization by $1+\rho t$ is injective on $R[t]$ (compare successive coefficients starting with the constant term). The homogeneous ideal $(f)$ is saturated with respect to the irrelevant ideal: the equation is monic of degree two in $x_0$, so its quotient is free with basis $1,x_0$ over $R[x_{-1},x_1,\ldots,x_n]$ and multiplication by $x_{-1}$ is injective, which also holds for its transform because the coefficient of $x_0^2$ remains $1$. Equality of the projective quadric subschemes therefore gives equality of these saturated ideals and a unit multiplier between their degree-two generators; evaluation at the fixed vector $a_0$, where $f(a_0)=1$, forces that multiplier to be $1$ and proves the same preserving-subgroup formula for the projective quadric.

## A10. The parity formulas are integral polynomial identities

**72/041–043, 051–055, “Donner un énoncé commun”; kind: self-flagged request with a verified algebraic answer; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — resolves the equation-level comparison.** Define the editorial parity-normalized continuant $L'_m=L_m$ for even $m$ and $L'_m=L_m/2$ for odd $m$ in the integer polynomial ring, where the matching formula proves the required coefficient divisibility before any base change. With $\rho=L_{n+1}$, $\sigma=L_n$, $\rho'=L'_{n+1}$, $\sigma'=L'_n$, the identities are
\[
(\rho,\sigma)=
\begin{cases}(2\rho',\sigma')&n\text{ even},\\(\rho',2\sigma')&n\text{ odd},\end{cases}
\qquad 2f(w)=-\rho\sigma,\quad f(w)=-\rho'\sigma'.
\]
They give $t\sigma'(1+\rho't)$ in the even case and $t\sigma'(2+\rho't)$ in the odd case, exactly identifying the two displayed equations with A09 through the explicit substitutions. These polynomial definitions explain the characteristic-two computations without dividing an element by $2$ inside a characteristic-two ring.

## A11. Two concrete characteristic-two preserving subgroups

**72/041–043, “peut être nulle en certains pts”; kind: unpursued implication, computed specialization; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — supplies a precise degeneration test.** At $n=2$, over $\mathbf F_2$, with $(\beta_0,\beta_1)=(0,1)$, the values are $(\rho,\rho',\sigma)=(0,1,1)$ and the preserving algebra is $\mathbf F_2[t]/(t^2+t)$, with its two distinct roots $0,1$ and additive law. At $n=1$, over $\mathbf F_2$, with $\beta_0=1$, the values are $(\rho,\sigma,\widetilde\sigma)=(1,0,1)$ and the preserving algebra is $\mathbf F_2[t]/(t^2)$, identified with $\mu_2$ by $u=1+t$. Both specializations are computed from the same polynomial in A09, so the recorded loss of a nonidentity geometric section is exhibited by an explicit algebra map rather than inferred from group names.

## A12. The low-dimensional example and fixed-locus statements need qualifications

**72/043 and 054–055, “$\exists!$ … partout $\ne1$” and “se réduit à $P(V)$ en car. $2$”; kind: reading question with exact counterexamples to the literal unqualified wording; context: Hua, findings register, 72-automorphisms-deform-gm-to-ga — adds the endpoint qualifications.** In A11's $n=1$, $\beta_0=1$ specialization, $\rho$ is invertible but the preserving polynomial is $t^2$, so every geometric point of the preserving subgroup has $t=0$; this is a direct check on scan 043's example after the visible deletion of the extra factor $2$, while its later proposition requiring $\sigma\widetilde\rho$ invertible does not include this example. The vector $o'=2w/\rho$ is zero and the recorded antipodism is the identity, hence it fixes all seven points of $\mathbf P^2(\mathbf F_2)$, compared with the three points of $\mathbf P(V)(\mathbf F_2)$. Scan 054's own margin already records the $o'=0$ exception and scan 055 repeats the identity behavior, so this is an internal qualification to carry into a proof, not an editorial change to the page.

## A13. Binary restrictions and the tangency calculation

**72/054–055, “rev. étale de longueur $2$” and “tangente”; kind: unpursued implication, direct polynomial verification; context: README quadrics calculation brief — adds the scheme multiplicities.** On the stated locus $D(\sigma')$, the even-case binary polynomial $-\sigma'\mu(\lambda+\rho'\mu)$ defines the two sections $[1:0]$ and $[-\rho':1]$ of the parameter projective line; their homogeneous determinant is $1$, so they remain disjoint over that base. The odd-case characteristic-two specialization with $\sigma'\rho'=1$ is $\mu^2$, giving one support point with length $2$, and the script computes this double root and its support. The coefficients exhibit the two-root and tangent behavior directly, while the manuscript's claims concerning the ambient quadric still carry its smoothness and frame conditions.

## A14. A source-local change of sigma notation

**72/048 and 052–053, “$f(c')=\sigma$” and “$\sigma=\zeta_0$”; kind: reading question resolved as an explicit relation between the recorded quantities; context: README calculation brief — records a necessary comparison map.** Denote the first quantity editorially by $\sigma_{[048]}=f(c')$ and the later one by $\sigma_{[052]}=\zeta_0$, retaining $\rho=\zeta_{-1}$; the source itself supplies
\[
2\sigma_{[048]}=-\rho\sigma_{[052]}.
\]
The parity-normalized prime in scan 053 and the left-end cofactor prime in scan 061 also have explicit formulas: the latter is obtained from the right-end cofactor by the polynomial-ring involution $\beta_i\mapsto\beta_{n-1-i}$, while the former uses the integral parity normalization of A10. These maps are stated in the notes so that no silent identification of similarly written symbols is needed.

## A15. The trigonometric line has a concrete numerical discrepancy

**72/036, “$\beta_i=\alpha_i+2$” and “$4\cos2\theta_i$”; kind: reading question with an exact calculation; context: README calculation brief — supplies a direct check of a literal equality.** At $\theta_i=\pi/3$ the written value $\alpha_i=4\cos^2\theta_i$ is $1$, so $\alpha_i+2=3$, whereas $4\cos(2\theta_i)=-2$. The script evaluates both exact values, and the transcription retains the plus signs seen during both readings. The scan's separate reconstruction of the reflection from neighboring fixed spaces still requires its stated invertibility assumptions and does not follow from this numerical line.

## A16. Why the small-dimensional lift caveat is concrete

**72/076–077, “Pour $n\geq2$”; kind: unpursued implication, explicit lift comparison; context: README definition brief and Hua, findings register, 72-automorphisms-deform-gm-to-ga — explains the stated dimension restriction.** On a rank-two module the matrices $D=\operatorname{diag}(1,-1)$ and $-D=\operatorname{diag}(-1,1)$ have the same projective image, and each is a reflection with its own rank-one fixed direction over $\mathbf Q$. On the centred chart of A08, set $\delta=\varepsilon-1$ for a scalar relating two lifts; for $i\ge1$ the predecessor-entry minor of A05 gives $\delta=0$, while for $i=0$ the three minors displayed below give $\delta^2=\mu_0\delta=\beta_0\delta=0$, and invertibility of the functional matrix gives $(\mu_0,\beta_0)=R$, hence $\delta=0$. This proves uniqueness of these centred lifts in rank at least three and exhibits the dimension-two ambiguity by explicit matrices; the existence and global gluing claims still require the source's stated frame and descent data.

For the first centred generator, $N_0$ has only its first row nonzero, namely $(\mu_0,\beta_0,0,\ldots)$, and the rank-at-most-one matrix $M=\delta I+\varepsilon N_0$ has minors $\delta^2$, $\delta^2+\varepsilon\mu_0\delta$, and $\varepsilon\beta_0\delta$ on rows/columns $(1,2)/(1,2)$, $(0,1)/(0,1)$, and $(0,2)/(1,2)$ respectively, using zero-based indices; their vanishing, the unit $\varepsilon$, and the unimodular first row of the invertible functional matrix give the asserted equations and the required unit ideal.

## A17. The centred-chart condition has an explicit boundary example

**72/073, “loc libre de rg $1$”; kind: unpursued implication, computed boundary example; context: README definition brief and Hua, findings register, 72-automorphisms-deform-gm-to-ga — makes the determinant condition in A08 testable.** Over $\mathbf F_2$, take $n=1$, $\mu_0=\mu_1=0$, and $\beta_0=0$, so $\rho=0$, $T_0=I$ on $V$, and $T_1(x_0,x_1)=(x_0,x_1+x_0)$. Both $x_0^2$ and $x_1^2+x_0x_1$ are invariant, as substitution gives $(x_1+x_0)^2+x_0(x_1+x_0)=x_1^2+x_0x_1$, and their distinct coefficients make them linearly independent. This locates the rank-one invariant-form calculation on its stated $\rho$-invertible chart by a direct comparison of the two invariant spaces.

## Reproduction and scope

`group_quadric_checks.py` verifies associativity, identity, inverse, the character and projective-line matrices symbolically; constructs the general common-kernel vector and commutator identities in dimensions $n=1,2,3,4,5$; and checks the reflection quadratic forms and centre identities in those dimensions. Its source-045 pairing tables have $(n+2)(n+1)$ vertex/edge cells, with $2(n+1)$ generically nonzero entries and $n(n+1)$ identically zero entries; the JSON retains every entry so the structural counts can be recomputed. The proof above, rather than this finite dimension sample, supplies the general centralizer and invariant-form arguments. This appendix establishes the calculations in the explicit recorded frame and does not certify unprovided earlier definitions or later pages of cote 72.
