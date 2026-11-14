\subsection*{The complete five-primary quartic class-two image}
\begin{statement}{E.115}{Proved}{Actual unramified descent, compact lifts, and every mixed support condition}
Put $R=\mathbb Z_5$, $S=\{2,5,\infty\}$, and retain the
plus quartic, every tangent and four-coset map of E.103--E.105,
and the actual class-two origin $S_5$.
Write $G=G_{\mathbb Q}$, $G_S=G_{\mathbb Q,S}$,
$V=T_5E_+$, $C=V^3$, $A=W\oplus j(C)$ with $j=j_*/4$,
and $B=\Lambda^2 A$.  Fix the actual cocycle $h$ representing
the E.103 generator of $H^1(G,V)=R$.

The full arithmetic extension with geometric free pro-five
kernel $N$ is the pullback of an extension over $G_S$.
The isomorphism and inverse are (E115.10) below.
The actual $S_5$, its class-two action, and $h$ descend through
this same map.  In particular the group of first coordinates
over $G_S$ is $R^{13}$, and every one of these coordinates
lifts to the actual intrinsic class-two extension over $G_S$.
With the specified coordinate choices the full geometric-
conjugacy space there is
\[
 \operatorname{Sect}_{G_S}(N/\gamma_3N)/N
       \simeq R^{13}\times R^{81}.
 \tag{E115.1}
\]
This is a homeomorphism with the actual inverse constructions
in the proof.  In particular every pure compact global input
$(0,r_1[h],r_2[h],r_3[h])$ lifts.

Here is the complete unrestricted image.  Express its input,
using the unchanged E.103 coefficient maps, as
\[
 [a]=[b]+[e_{\mathbf r}],\qquad
 b\in Z^1_{\rm cts}(G,W),\quad
 e_{\mathbf r}=j_{\mathbf r}h=\sum_{i=1}^3r_i j_i h,
 \quad\mathbf r=(r_1,r_2,r_3)\in R^3.
 \tag{E115.2}
\]
Any initial representative is aligned to this one by its actual
abelian coboundary and the BCH conjugation (E113.16).
At every rational prime $p\notin S$ choose an actual prolongation,
a tame pro-five generator $t_p$, and arithmetic Frobenius $F_p$,
with $F_pt_pF_p^{-1}=t_p^p$.
Use the corresponding Tate basis and put
\[
 \begin{gathered}
 v_p=b(t_p)\in W,\qquad
 u_p=(F_{E,p}-1)^{-1}h(F_p)\in V\otimes\mathbb Q_5,\\
 \overline u_p=u_p+V\in(V\otimes\mathbb Q_5/V)^{F_{E,p}},
 \qquad \operatorname{ord}(\overline u_p)=5^{m_p},\\
 c_p=v_p\wedge j_{\mathbf r}u_p\in
              (W\wedge j(C))\otimes\mathbb Q_5 .
 \end{gathered}
 \tag{E115.3}
\]
Here $m_p=0$ means that the class is zero.
The matrix $F_{E,p}-1$ is invertible over $\mathbb Q_5$.
Its class $\overline u_p$ is the actual local elliptic
Kummer class of $[h]$, with the explicit boundary map in
(E115.23).  Thus its phase is retained when an inverse lift
is constructed.  The integer $m_p$ is independent of the unit
choice of generator of $H^1(G,V)$.

The input (E115.2) has an intrinsic class-two lift exactly when
both of the following tests hold:
\[
 \begin{gathered}
 \text{all fifty-five peripheral tests (E108.4)--(E108.5)
       hold for $b$ at $\ell=5$,}\\
 c_p\in W\wedge j(C)\quad(p\notin S),\qquad
 c_p\longrightarrow0\quad\text{in its five-adic lattice.}
 \end{gathered}
 \tag{E115.4}
\]
There is a scalar form of the second test.  For a vector in
a finite free $R$-module let $\nu_5$ denote the largest power
of five dividing it, with $\nu_5(0)=\infty$.
If $\mathbf r\ne0$, put $t=\min_i\nu_5(r_i)$.
Replace $u_p$ by the representative of $\overline u_p$ whose
two coordinates lie in $\mathbb Z[1/5]\cap[0,1)$.
This changes $c_p$ by an integral restricted family.
Consequently (E115.4)'s mixed test is precisely
\[
 \nu_5(v_p)+t\ge m_p\quad(m_p>0),\qquad
 \nu_5(v_p)+t-m_p\longrightarrow+\infty
                         \quad\text{on $\{p:m_p>0\}$.}
 \tag{E115.5}
\]
For $\mathbf r=0$ the mixed test is empty.
All limits here mean that at each fixed coefficient exponent
only finitely many primes fail the indicated divisibility.
No closure is added to the denominator of the support quotient.

Every nonempty fibre over (E115.2) is the entire torsor
\[
 R^{66}\oplus\mathcal R_{\mathcal P_{\mathbb Q}}(R)^6
 \oplus\mathcal R_{\{p:p\equiv1\ (4)\}}(R)^3
 \oplus\mathcal R_{\{p:p\equiv3\ (4)\}}(R)^3,
 \tag{E115.6}
\]
with the actual coefficient projections, cocycle sections and
inverse ratio maps of E.112.  No lower stabilizer is quotiented
out.  Formulas (E115.14), (E115.18), and (E115.22) give the
particular correction and its inverse, including the true
compact action and its E.109 inner corrections.

For $R=\mathbb Q_5$ the same theorem holds after scalar
extension.  In (E115.4) the mixed requirement is simply
$c_p\to0$ in the rational coefficient space, and the first
line uses E.108's rational test.
Formula (E115.5) retains only its limit requirement, allowing
integer-valued, possibly negative valuations of $v_p$ and
$\mathbf r$.
Every restricted module in (E115.6) is replaced by its rational
$c_0$ space, with one common bound on denominators.

The integral mixed test has nonzero obstructions.  The integers
$m_p$ are unbounded.  More precisely, for each $n\ge1$ there
are infinitely many primes satisfying
\[
 \begin{gathered}
 p\equiv1\pmod8,\qquad \nu_5(p-1)=n,\qquad
 2\in(\mathbb F_p^{\times})^{5^n},\qquad
 F_{E,p}\equiv1\pmod{5^n},\qquad m_p\ge n.
 \end{gathered}
 \tag{E115.7}
\]
They are the actual Chebotarev sets specified in the proof.
For each such prime the E.108 toric input $(p,1,1)$ lifts.
For every nonzero compact vector $\mathbf r$ and every one
of these primes with $n>\min_i\nu_5(r_i)$, the combined input
$((p,1,1),\mathbf r)$ does not lift.
Both of its separate toric and compact inputs do lift.
The resulting exclusion also holds in every geometric quotient
mapping to this actual class-two group.
This evaluates the five-primary class-two stage of E.23;
the maps to later intrinsic quotients retain their further
lifting conditions.
\end{statement}
\begin{proof}
\emph{The genuine unramified based action.}
Let $F=\mathbb Q(\zeta_8)$ and use exactly the cusp
$O=[\zeta_8:0:1]$, parameter $s=y/z$ and unit tangent of
E.105.  Over $\mathcal O_F[1/2]$ the plane quartic is smooth:
its partial derivatives are $4x^3,4y^3,4z^3$.
The twelve cusp sections are disjoint there.  Indeed their
parameters are the roots of $T^4+1$, whose discriminant is
a power of two, and sections in distinct coordinate lines
cannot meet on the quartic.
At $O$ the exact completed branch is
\[
       x/z=\zeta_8(1+s^4)^{1/4},\qquad y/z=s.
 \tag{E115.8}
\]
At every finite place not dividing $2\cdot5$ its coefficients
are integral, and the specified tangent is a unit.

Apply SGA1 XIII Corollary2.9 and construction2.10 to this
smooth proper curve and its relative normal-crossing divisor.
The construction identifies the prime-to-residue-characteristic
geometric cover categories of the generic and special fibres;
the last part of the proof of Corollary2.12 proves that this
specialization is an isomorphism.  Lemma2.11 identifies the
actual corresponding inertia subgroups
\cite[XIII,2.9--2.12 and their proofs]{E_SGA1}.
Here is the basepoint refinement used in this application.
Over the strict henselization at a good place, a tame branch
of a five-power cover at (E115.8) has the Kummer form
$z^{5^a}=s u(s)$ with $u(s)$ a unit, after an etale change.
Hensel's lemma supplies the roots of its leading unit and all
five-power roots of unity over that strict henselization.
Evaluating its Puiseux fibre at the fixed unit tangent thus
commutes with the specialization functor.
It gives an isomorphism of the cover categories with their
specified fibre functors, not just their unpointed categories.
Every based finite five-power quotient is consequently fixed
by arithmetic inertia.  Taking the inverse limit proves that
the actual tangential action on the full $N$ is trivial there.
The same conclusion for the closed normal subgroup generated
by these inertias follows from its being an action homomorphism.

Put $I=\ker(G\to G_S)$.  Since $F/\mathbb Q$ ramifies only
at two, $I\subset G_F$, and it is also the kernel of
$G_F\to G_{F,S_F}$.  To check the last assertion, the Galois
closure over $\mathbb Q$ of an extension of $F$ unramified
outside $S_F$ is still unramified outside $S$.
Thus the preceding action is trivial on $I$.

Let $\mathcal E$ be the actual arithmetic extension with
geometric kernel $N$, and let $s_F$ be the specified tangent
section on $G_F$.  The group $N$ has rank
$2\cdot3+12-1=17$ and centre one.
For clarity the latter assertion follows integrally from its
Magnus embedding in $1+(X_1,\ldots,X_{17})
\mathbb F_5\langle\!\langle X_1,\ldots,X_{17}\rangle\!\rangle$.
The embedding is faithful: evaluation in the group algebra
of any finite five-group quotient is defined because its
augmentation ideal is nilpotent, and these quotients separate
the free pro-five group.  A power series commuting with $X_i$
contains only powers of $X_i$, by comparing its first letter
and moving initial $X_i$'s to the end.  Commuting with both
$X_1$ and $X_2$ therefore makes it constant.  Its augmentation
is one, proving the assertion.

Both $e s_F(i)e^{-1}$ and $s_F(gig^{-1})$, for $e$ above $g$,
centralize $N$.  They have the same arithmetic image, so their
ratio is in $N\cap C_{\mathcal E}(N)=Z(N)=1$.
It follows that the compact subgroup $s_F(I)$ is normal in
$\mathcal E$ and meets $N$ trivially.  Define
\[
 \mathcal E_S=\mathcal E/s_F(I),\qquad
 1\longrightarrow N\longrightarrow\mathcal E_S
      \longrightarrow G_S\longrightarrow1.
 \tag{E115.9}
\]
The exact pullback and inverse are
\[
 \begin{gathered}
 \mathcal E\longrightarrow\mathcal E_S\times_{G_S}G,
          \qquad e\longmapsto([e],\pi(e)),\\
 ([e],g)\longmapsto e\,s_F(\pi(e)^{-1}g).
 \end{gathered}
 \tag{E115.10}
\]
The second expression is independent of the lift $e$;
its displayed argument lies in $I$.
These are continuous inverse homomorphisms, as one checks
by the normality identity just proved.

Every construction of E.103 and E.105 commutes with this
quotient.  In particular the chosen four coset lifts map to
their actual images, their factors $h_i(g)$ map to the same
factors in $G_{F,S_F}$, and the formula
$B(e)=\sum_i e e_i s_F(h_i(g))^{-1}e_{g i}^{-1}$ maps
term by term to the identical sum in the quotient.
The roots of two occurring in the frame cochains are
unramified outside $2,5$.  Thus the subsequent toric
correction and the central four-coset construction also
descend.  This proves the assertion for the specified
$S_5$, its actual $D_g$ and its linear action.
Changes of coherent roots or coset lifts remain the actual
fixed geometric conjugations already specified in E.105.
They preserve this descent and are not set equal to zero.

\emph{The finite-base cohomology and literal compact primitives.}
At $p\notin S$, a $V$-cocycle has inertia vector in
$\ker(F_{E,p}-p)$.  Its determinant is
$p\#E_+(\mathbb F_p)\ne0$, so this vector is zero.
The cocycle $h$ itself therefore factors through $G_S$.
This agrees with the inverse inflation map proved in E.112.

Put $B_W=\Lambda^2W$, $M=W\wedge j(C)$, and retain
$B_{\rm T}$ and $U_{\rm CM}^3$ from (E113.20).
E.108 and E.112 prove at every finite coefficient exponent
\[
 H^2(G_S,(B_W\oplus M\oplus U_{\rm CM}^3)/5^a)=0,
 \quad H^3(G_S,-)=0,
 \quad H^1(G_S,-)\text{ finite}.
 \tag{E115.11}
\]
For $B_W$ this is the proved $K_2(\mathcal O_{F,S_F})/5^a=0$
comparison, followed by restriction/corestriction of degree four.
For $M$ the exact coefficient isomorphism is
$V(1)^{15}\oplus(V(1)\chi_2)^{18}$ from E.108.
The other three summands are precisely E.112's $U$.
The finite degree-one groups kill the derived inverse-limit
terms, so the continuous second groups in (E115.11) vanish.

We also need an injective map, rather than a vanishing
assertion, for the nine Tate lines:
\[
 H^2_{\rm cts}(G_S,B_{\rm T})
          \lhook\joinrel\longrightarrow H^2_{\rm cts}(G,B_{\rm T}).
 \tag{E115.12}
\]
Restrict to $F$; the nine characters become trivial and
restriction is injective by corestriction and division by four.
The class number of $F$ is one by E.103, so the Kummer
sequence on $\mathcal O_{F,S_F}$ has no Picard-group kernel.
Its degree-two map to $F$ is the injective map on Brauer
groups.  This proves injectivity at every finite exponent.
The finite $S_F$-unit groups modulo powers make $H^1$
finite and hence Mittag--Leffler.  On the unrestricted field
the Kummer $H^1$ transitions are surjective.
The same continuous-cochain comparison used in E.113 now
proves (E115.12), including its inverse-limit assertion.

The E.113 Weil cup therefore has a primitive $k_S$ on $G_S$.
For each $i$ the actual two-cocycle
$D_g j_i h(t)$ has zero class in every remaining summand
by (E115.11), and in the Tate lines by (E113.21) and
(E115.12).  Fix actual continuous cochains $p_i$ on $G_S$
with $dp_i(g,t)=D_gj_i h(t)$.
Here and below a primitive can be constructed by finite
linear equations: at each exponent its possible cochains
are a nonempty finite torsor under the finite group of
one-cocycles.  The inverse systems have the finite
intersection property, since any finite set of compatibility
requirements can be met at its largest exponent.
Their compact inverse limit supplies compatible cochains.
Fix orders on the finite sets and choose a compatible branch.
All arithmetic actions in these equations are the descended
actual actions just proved.

Define, with $e^{-1}:R(1)\to\Lambda^2V$ the actual inverse
Weil pairing,
\[
 \begin{gathered}
 \nu_{\mathbf r}=\tfrac12(\Lambda^2j_{\mathbf r})e^{-1}k_S,
 \qquad t_{\mathbf r}=\sum_i r_i p_i+\nu_{\mathbf r},\\
 dt_{\mathbf r}=\Omega_{e_{\mathbf r}},\qquad
 \Omega_a(g,t)=D_ga(t)+\tfrac12a(g)\wedge g a(t).
 \end{gathered}
 \tag{E115.13}
\]
This is a polynomial continuous choice in the three compact
scalars.  Changing from an earlier E.113 primitive $k$ to
$k_S$ changes the coordinates by the displayed central
one-cocycle involving $k-k_S$; no origin is changed.

\emph{The full E.109 contraction, with its inner terms.}
The preceding primitives may be chosen with a prescribed
compact projection, as follows.  Use $H=T_5J_C$, its
polarization $q$, $Z=\Lambda^2H/Rq$, and all maps $f,\Pi,J$
of E.109.  Write $c^C_g=D^C_g\rho_H(g)^{-1}$ and take the
actual cocycle $\beta_g=2\Pi c^C_g$.
All these cocycles factor through $G_S$ by (E115.10).
Inflation on degree-one cohomology is injective, so E.109's
equality of outer classes holds over this same source.
Lifting its zero-cochain in
$\mathcal D=\operatorname{Hom}(H,Z)/\operatorname{ad}H$
to $\operatorname{Hom}(H,Z)$, and then using the injective
inner map, gives actual $m_0$ and $u\in Z^1(G_S,H)$ with
$2c^C=f\beta+dm_0+\operatorname{ad}u$.
The coefficient quotient is free, as proved in E.109,
so the displayed lift exists integrally.
E.112 gives the unique cohomology scalars of $u$;
absorbing its coboundary into $m_0$ yields
\[
 2c^C_g=f(\beta_g)+(gm-m)
              +\operatorname{ad}_{\sum_i\lambda_i h_i(g)},
 \qquad h_i=j_i^C h,\quad\lambda_i\in R.
 \tag{E115.14}
\]
The constant $m$ and all $\lambda_i$ retain this actual
normalization; no value is assigned to them by a graded matrix.

In a symplectic CM basis $e_i,f_i$ of $H$ the map $f$
sends $\Lambda^3H^+$ evaluated on $H^-$ into
$\Lambda^2H^+$, and sends $\Lambda^3H^-$ evaluated on
$H^+$ into $\Lambda^2H^-$; both other evaluations are zero.
Thus its contraction lies in the actual rank-six submodule
$U_{\rm CM}^3$ of $Z$.  Equation (E115.11) gives cochains
$n_i$ in that submodule with
$dn_i(g,t)=f(\beta_g)(g h_i(t))$.
These primitives concern the contraction of the specified
nonzero E.109 class.  They do not change that action class.

Set
$Q_h=-h\otimes h/2+k_S(e\otimes f-f\otimes e)/2$
in any Weil basis of $V$.
Direct expansion gives $dQ_h=h\otimes gh$.
Let $K_i$ be the image of
$\sum_j\lambda_j(j_j^C\otimes j_i^C)Q_h$ under wedge and
the quotient to $Z$.  Evaluating (E115.14) on $g h_i(t)$
therefore gives
\[
 t_i^C=\tfrac12(n_i+m h_i+K_i),\qquad
 dt_i^C(g,t)=D^C_g h_i(t).
 \tag{E115.15}
\]
The full filling map is still
$(x,z)\mapsto(px,p_Bz+Jx)$.
In particular $p_Bp_i-Jj_i h$ and $t_i^C$ have the same
differential.  Their difference is an actual central
one-cocycle.
The coefficient map $p_B$ has the following equivariant
section: represent $z\in Z$ in $\Lambda^2H$, replace it by
$z-q\langle z\rangle/3$, and apply $\Lambda^2j$.
Here $\langle q\rangle=3$, so the replacement is independent
of the representative.  Denote this section by $\sigma_Z$.
Replace $p_i$ by
$p_i+\sigma_Z(t_i^C-p_Bp_i+Jj_i h)$, an addition of an
actual one-cocycle.
Then, literally,
\[
                 p_Bp_i-Jj_i h=t_i^C.
 \tag{E115.16}
\]
This proves the asserted actual compact/affine transport,
including its source splitting, its inner correction and
the filling term $J$.

\emph{The exact obstruction reduction and its inverse.}
Let $P_W:B\to B$ be the actual exterior projection onto
$B_W$, followed by its given inclusion in $B$.
For a toric cocycle $b$, E.105 gives
$(1-P_W)\Omega_b|_{G_F}=0$ as a cochain.
Push out the pulled-back extension over $bS_5$ to
$\ker P_W$.  Its section on $G_F$ has central coordinate
zero.  Apply the same four-coset construction to that section.
If $B_b(e)$ denotes its literal four-term sum, the resulting
section has central coordinate $-B_b((0,g))/4$.
Consequently
\[
 U_b(g)=B_b((0,g))/4,\qquad
        dU_b=(1-P_W)\Omega_b.
 \tag{E115.17}
\]
It is a continuous cochain given by four actual group products;
it depends continuously, and polynomially in BCH coordinates,
on the fixed cocycle $b$.

Expanding the two first-cocycle identities gives
$d(b\wedge e)=-b\wedge ge+e\wedge gb$.
Equations (E115.13) and (E115.17) therefore give the inverse
cochain maps
\[
 \begin{gathered}
 z\longmapsto
 \widetilde z=z+t_{\mathbf r}+\tfrac12 b\wedge e_{\mathbf r}+U_b,
 \qquad
 d\widetilde z=-P_W\Omega_b-b\wedge g e_{\mathbf r},\\
 z=\widetilde z-t_{\mathbf r}
                  -\tfrac12 b\wedge e_{\mathbf r}-U_b.
 \end{gathered}
 \tag{E115.18}
\]
The two terms on the right lie in the distinct specified
coefficient summands $B_W$ and $M$.
Restriction to $G_F$ of the first term is exactly the
fifty-five cochains of E.108.  Restriction/corestriction of
degree four proves both directions of its stated test.
For an initially changed abelian representative use the
literal $\Gamma_m$ of (E113.16); the transformed central
coordinate changes by $\Gamma_m$ and by the difference
of the displayed added cochains.  This is the full gauge
map and its inverse, without identifying different origins.

\emph{Finite support before the derived limit.}
For $M=W\wedge j(C)$, localization at a finite set of primes
outside $S$, at coefficient exponent $5^a$, has support
term $\bigoplus_p R\Gamma(\mathbb F_p,(M/5^a)(-1))[-1]$.
Take the filtered direct limit in the finite set first.
Purity identifies its two-term complexes with
\[
 [M/5^a\xrightarrow{\ d_p\ }M/5^a],\qquad
             d_p=p^{-1}F_{M,p}-1.
 \tag{E115.19}
\]
These are the actual etale/Galois and inertia maps
\cite[II.0.1(f), II.1.7(b), II.2.9]{E_MilneADT}.
Both direct-sum coefficient transitions are onto.
Their derived inverse limit is thus the literal complex
$[\mathcal R(M)\xrightarrow d\mathcal R(M)]$, where
$\mathcal R(M)=\{(x_p):x_p\in M,\ x_p\to0\}$.
The finite-base second and third groups vanish by (E115.11),
and its finite first groups kill the adjacent derived limit.
The continuous-cochain comparison consequently gives
\[
 H^2_{\rm cts}(G,M)
       \simeq\mathcal R(M)/d\mathcal R(M).
 \tag{E115.20}
\]
Here $d\mathcal R(M)$ is its image, with no closure.
These are precisely the inverse-limit maps of
\cite[Proposition1.6 and Theorem2.2]{E_JannsenContinuous}.

The eigenvalues of $p^{-1}F_{M,p}$ have complex absolute
value $\sqrt p$, since $W$ has eigenvalues $p$ times roots
of unity and $C$ has the elliptic eigenvalues.
Hence every $d_p$ is invertible over $\mathbb Q_5$.
This proves that the candidate support correction is unique.

\emph{The literal mixed localizer and its compact-point inverse.}
In the central extension for the ordered cup
$\omega(g,t)=b(g)\wedge g e_{\mathbf r}(t)$, use the law
$(z,g)(w,t)=(z+gw+\omega(g,t),gt)$.
The compact cocycle is zero on inertia, so the central-zero
lifts $t_p^a\mapsto(0,t_p^a)$ are a homomorphism.
Multiplying the three factors of $F_pt_pF_p^{-1}$ gives
the central defect
\[
 \epsilon_p=-p\,v_p\wedge e_{\mathbf r}(F_p),\qquad
 \epsilon_p\longmapsto\epsilon_p+(F_{M,p}-p)z_p
 \quad\text{under }t_p\mapsto(z_p,t_p).
 \tag{E115.21}
\]
For example the two nonzero cup contributions are
$+b(F_p)\wedge e(F_p)$ and
$-(b(F_p)+p v_p)\wedge e(F_p)$.
The support map divides the defect by $p$, as it compares
the value at $t_p^p$ with the chosen value at $t_p$.
Thus (E115.20) sends this cup to
$[(-v_p\wedge e_{\mathbf r}(F_p))_p]$ and its unique
correcting family is
\[
 z_p=d_p^{-1}\bigl(v_p\wedge e_{\mathbf r}(F_p)\bigr).
 \tag{E115.22}
\]
The input family is restricted: each reduction of $b$ gives
a finite extension ramified at only finitely many primes,
so $v_p\to0$, and $h(F_p)$ is integral and uniformly bounded.

Write $F_{W,p}=pP_p$, where $P_p$ is the actual permutation
operator on the peripheral quotient.  The first-cocycle tame
relation gives $P_pv_p=v_p$.  Therefore
$d_p(v_p\wedge j_{\mathbf r}u)
=v_p\wedge j_{\mathbf r}(F_{E,p}-1)u$.
Since $\det(F_{E,p}-1)=\#E_+(\mathbb F_p)\ne0$,
(E115.22) is exactly $c_p$ in (E115.3).
The short exact sequence $0\to V\to V\otimes\mathbb Q_5
\to V\otimes\mathbb Q_5/V\to0$ over the unramified
local source has the explicit boundary
\[
 \overline u\longmapsto
       [F_p\longmapsto(F_{E,p}-1)u],\qquad
 H^1_{\rm unr}(\mathbb Q_p,V)=V/(F_{E,p}-1)V.
 \tag{E115.23}
\]
Both invariants and first cohomology of the rational
two-dimensional coefficient vanish here because $F_{E,p}-1$
is invertible.  This proves the identification and its inverse.
Under good reduction it is the actual finite group
$E_+(\mathbb F_p)[5^\infty]$.
Thus $m_p\le\nu_5(\#E_+(\mathbb F_p))$.
It can be read at that finite coefficient exponent by applying
the actual Frobenius and the corresponding finite cocycle
$h_a$ from E.112 to the quotient in (E115.23).
This retains the arithmetic Frobenius marking at every level.

Changing $h$ by $dh_0$ changes $u_p$ by the same integral
$h_0$; replacing its generator by a unit does not change
$m_p$.  Replacing $u_p$ by its displayed fractional
representative changes it by an integral vector, uniformly
bounded for all $p$.  The resulting change in $c_p$ is
therefore integral and restricted, since $v_p\to0$.
Changing a tame basis changes both tensor factors by the
corresponding inverse units.  An inertia translate of Frobenius
does not change $h(F_p)$, since $h$ is unramified.
These are the actual representative maps proving independence
of all tests.
In the fixed tensor lattice, valuation of a nonzero pure tensor
is the sum of the valuations of its factors.
The fractional representative has valuation exactly $-m_p$
when $m_p>0$, and is zero when $m_p=0$.
This proves (E115.5), including its convergence requirement.

If the tests hold, (E115.20) gives a global primitive with
the prescribed restricted inertia corrections.
Here is its compatible construction.  At each finite exponent
the corrections have finite support.  Exactness of localization
gives a primitive; the surjective degree-one residue map, whose
next term is the zero finite-base $H^2$ of (E115.11), adjusts
its inertia values to the prescribed ones.
The remaining choices are a finite torsor under unramified
one-cocycles.  All finite compatibility conditions can be met
at their largest exponent, so their compact inverse limit
gives an actual continuous primitive.
Use the same proved construction of E.108 for the peripheral
summand and then (E115.18) for its literal class-two inverse.
Conversely any lift supplies these corrections by its tame
relation, so both tests are necessary.

\emph{All fibres and the finite-base coordinates.}
The abelian module $A$ has no global invariants: at a good
Frobenius its weights are one and two, so none of its
eigenvalues is one.  Thus the aligning abelian conjugator
is unique.  The difference of two lifted central coordinates
is exactly a $B$-valued one-cocycle, and a geometric central
conjugator adds its ordinary coboundary.
This proves the full fibre assertion and inverse ratio map;
substitution of E.112 gives (E115.6).

For specificity all finite-base input coordinates are units
with actual Kummer maps.  Set $\epsilon=1+\sqrt2$,
$\varpi=1-\zeta_8$, and $\pi_\pm=2\pm i$.
The two primes of $F$ over five have these generators and
norm $25$; $N\varpi=2$, $N\epsilon=1$.
In each of the first two factors of (E108.1), the four
independent $S_F$-unit coordinates are
$\epsilon,\varpi,\pi_+,\pi_-$.
The norm-one third factor has the two coordinates
$\epsilon,\pi_+/\pi_-$, since its norm matrix in the
two rational unit coordinates $2,5$ is
$\left(\begin{smallmatrix}0&1&0&0\\0&0&2&2\end{smallmatrix}\right)$.
Together with the three compact coordinates this gives the
literal $R^{13}$ in (E115.1).

The first $66$ central coordinates remain those of E.112.
Each of its six Tate lines has the two $S$-unit coordinates
$2,5$.  Each of its three $\chi_{-1}$ Tate lines has the
norm-one Gaussian coordinate $(2+i)/(2-i)$.
There are no inert-prime residue coordinates in $S$.
Thus the full central group over $G_S$ is $R^{81}$.
For the particular section, choose the thirteen fixed
input cocycles just displayed.  Its obstruction is a polynomial
of degree at most two in their coordinates.  Every coefficient
has a primitive: use (E115.11) in the remaining summands,
(E115.12) and E.113 in the Tate summands, and polarization
over $R$ to separate the coefficients.  Fix these finitely
many primitives.  Their polynomial sum is a continuous
particular section for every input.
Subtracting it and reading the $81$ central coordinates gives
the inverse of (E115.1).
At finite coefficient level the relevant section sets are
finite by arithmetic cohomological finiteness and the central
extension sequences.  Their inverse limits and their compact
geometric quotients give exactly this topology.

For rational coefficients every continuous cochain on the
compact source has a common denominator bound.
Scalar extension therefore commutes with the cochain complex.
The preceding maps, tests and inverses rationalize literally.
A sequence tending to zero in $\mathbb Q_5$ is bounded, which
is precisely the denominator convention in the statement.

\emph{Actual mixed nonlifting and unbounded local orders.}
Let $L_n=\mathbb Q(E_+[5^n])$, and let $\Gamma_n$ be its
actual Tate image.  The closed image of $G_{\mathbb Q(i)}$
is diagonal in the two CM lines.  E.112's residual element
$g_{2,2}$ is $-I$ modulo five.  Any lift has both eigenvalues
in $-1+5R$; its successive $5^k$th powers converge to $-I$.
Closedness proves that $-I$ belongs to the actual Tate image,
and hence is central in every $\Gamma_n$.
For a one-cocycle on $\Gamma_n$ with coefficients $V/5$,
commuting an element with this scalar shows directly that
the cocycle is a coboundary, since $-2$ is a unit.
This is the elementary Sah calculation, with its actual scalar.

The reduction $h_1$ is nonzero by E.112, so its restriction
to $\ker(G_S\to\Gamma_n)$ is nonzero by inflation--restriction.
The residual representation is irreducible: E.112's diagonal
characters have distinct eigenspaces, and complex conjugation
interchanges them.  The image of $h_n$ on that kernel is
therefore onto modulo five, and Nakayama's lemma gives the
whole $V/5^n$.  Consequently the actual finite quotient
\[
 g\longmapsto(h_n(g),\rho_n(g))
 \quad\text{has image }(V/5^n)\rtimes\Gamma_n.
 \tag{E115.24}
\]
This also specifies its exact field and its translation kernel.

The five-Sylow subgroup of $\Gamma_n$ lies in the two
diagonal CM unit groups and has exponent at most $5^{n-1}$.
It cannot have the cyclotomic quotient of order $5^n$;
hence $\mu_{5^{n+1}}$ is not contained in $L_n$.
Adjoining $F$, of degree a power of two, preserves that fact.
Over $L_nF$, the Kummer extension generated by $2^{1/5^n}$
has cyclic five-kernel with conjugation character $\chi$.
It has no common degree-five quotient with the next
cyclotomic extension, whose conjugation character is trivial.
The characters are distinct modulo five.
Thus there is an automorphism of their compositum fixing
$L_nF$ and $2^{1/5^n}$ but acting nontrivially on
$\mu_{5^{n+1}}$.

The additional extension over $L_n$ just used has five-primary
composition factors with characters $1$ and $\chi$, and a
prime-to-five part.  Its common quotient with the translation
extension (E115.24) is trivial: every nonzero quotient of the
latter translation module has the irreducible $V/5$ as a
composition factor, which has dimension two.
All these statements concern the actual normal field
extensions and their conjugation actions over $\mathbb Q$.
We may therefore prescribe simultaneously the preceding
automorphism and a primitive translation in (E115.24).
Chebotarev applied to its conjugacy class gives infinitely
many primes with all properties in (E115.7)
\cite[VIII,Theorem7.4 and proof]{E_MilneCFT}.
Primitivity is preserved under conjugation.
Since $F_{E,p}-1$ is divisible by $5^n$ and $h(F_p)$ is
primitive, (E115.3) gives $m_p\ge n$.

Finally the input $(p,1,1)$ is
$b=\kappa_p\sum_{i=0}^3e_{A_i}$.
This is a primitive rational Tate line in $W$.
Each of its E.108 peripheral cups is a scalar multiple of
$\kappa_2\cup\kappa_p$; the two self-cups vanish because
two is invertible.  At primes over $p$ the residue field is
$\mathbb F_p$, and the whole five-primary tame symbol is
zero because $2$ is a $5^n$th power and $\nu_5(p-1)=n$.
At the prime above two its residue-unit group is trivial.
There are no other supports.  Thus the toric input lifts by
E.108.  Its mixed inertia vector at $p$ is primitive, so
(E115.5) fails whenever $n>\min_i\nu_5(r_i)$.
This proves all stated nonlifting assertions through the
actual projection to the intrinsic class-two group.

The certificate checks the symplectic contraction and its
pure-CM image, both tensor/cochain signs, the full tame word
and correction map, the actual $S_F$ norm coordinates,
the residual irreducibility and character separation, and
the finite tensor-valuation and inverse-coordinate identities.
Its finite computations supplement the preceding source,
localization and infinite-limit proofs; no numerical values
for an uncomputed higher Frobenius word are substituted.
\end{proof}
