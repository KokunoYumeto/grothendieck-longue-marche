\subsection{All nonunit multiples of the first seventeen class}

\begin{statement}{E.111}{Proved}{The additional positional S-class towers and every nonzero first class on the seventeen line}
Choose compatible roots $\xi_j=\zeta_{3^j}$, with
$\xi_{j+1}^3=\xi_j$ and $\xi_1=\zeta$ as previously fixed.
For $j\ge2$ put
\[
 K_j=\mathbb Q(\xi_j),\qquad
 L_{m,j}=K_j(\beta_{m,j}),\qquad
 \beta_{0,j}=17\xi_j,\quad
 \beta_{m+1,j}^3=\beta_{m,j},\qquad m\ge0.
 \tag{E111.1}
\]
These roots may be taken literally as
$\beta_{m,j}=17^{1/3^m}\xi_{m+j}$, with the positive
compatible roots of seventeen used in E.110.
Let $S$ consist of the primes over three and seventeen.
There is one three-prime and three seventeen-primes in each
$L_{m,j}$. Every adjacent extension in $m$ is cyclic cubic
and totally ramified at these four places. All the S-class
groups and their ideal norm and extension maps are evaluated:
\[
 \operatorname{Cl}_S(L_{m,j})\{3\}=0
                    \quad(j\ge2,\ m\ge0).
 \tag{E111.2}
\]
In particular all these ideal maps on three-primary S-classes
are the unique maps between zero groups.

Here are the actual unit-norm maps behind (E111.2).
Write $U_{m,j}=\mathcal O_{L_{m,j},S}^{\times}$ and
$r_{m,j}=3^m\varphi(3^j)/2$. With arithmetic reciprocity and
the fixed root $\zeta$, define
\[
 \chi_{m,j,v}(u)=
     \log_\zeta(\beta_{m,j},u)_{v,3},\qquad
 \boldsymbol\chi_{m,j}:U_{m,j}\longrightarrow
 \mathcal H_3:=\{(c_0,c_1,c_2,c_3)\in\mathbb F_3^4:
                                   \textstyle\sum c_i=0\}.
 \tag{E111.3}
\]
The four coordinates are the three-place followed by the
three seventeen-places labeled in the proof. These maps are
onto and induce exact isomorphisms, also after completion,
\[
 \begin{gathered}
 U_{m,j}/N_{L_{m+1,j}/L_{m,j}}U_{m+1,j}
       \xrightarrow{\ \boldsymbol\chi_{m,j}\ }\mathcal H_3,
 \\
 \ker\!\left(N:\widehat U_{m+1,j,3}
                     \longrightarrow\widehat U_{m,j,3}\right)
       \simeq C_3\oplus\mathbb Z_3^{,2r_{m,j}}.
 \end{gathered}
 \tag{E111.4}
\]
The torsion column in this norm kernel is the literal $\mu_3$.
Every nonempty norm fiber is its translate. The proof gives
explicit three-column sections of the quotient (E111.3),
with inverse matrices, and proves that its zero condition
is sufficient for an S-unit preimage.

Retain $P_j$ and $\mathcal R(P_j)$ from (E110.2), with their
uniform multiplication-completion topology, and set
\[
 \mathcal X_j=\varprojlim_{m,N}\widehat{L_{m,j}^{\times}}_3,
 \qquad
 \mathcal U_j=\varprojlim_{m,N}\widehat U_{m,j,3}.
 \tag{E111.5}
\]
The actual outside-S divisor maps give split exact sequences
\[
 0\longrightarrow\mathcal U_j\longrightarrow\mathcal X_j
     \xrightarrow{\operatorname{div}_{\notin S}}
                \mathcal R(P_j)\longrightarrow0,
 \qquad \mathcal U_j\simeq\prod_{i\ge1}\mathbb Z_3.
 \tag{E111.6}
\]
For each $p\in P_j$, choose a coherent completed S-principal
generator $a_{j,p}$ of the unique surviving degree-one
prime chain over $p$. Such generators exist by the proof.
Then the actual splitting and inverse are
\[
 s_j(t)=\prod_{p\in P_j}a_{j,p}^{,t_p},\qquad
 x\longmapsto\bigl(x/s_j(\operatorname{div}_{\notin S}x),
                         \operatorname{div}_{\notin S}x\bigr).
 \tag{E111.7}
\]
The product converges uniformly in every positional
multiplication completion. For the compact isomorphism in
(E111.6), choose a basis of $\mathcal U_j^\vee[3]$, divide
its characters successively by three, and use exactly
(E110.7). Here the finite character representatives are
S-unit coordinate functionals, with transition maps the
transposes of the actual norm maps (E111.3)--(E111.4).
This gives the forward map and its inverse by their finite
character equations; the proof establishes their existence
and their product topology.

The norm to $\mathbb Q$ remains an explicit coordinate
map. Put $f_j=2\cdot3^{j-2}$. For $y\in\mathcal U_j$,
let $y_0$ be its coordinate in $\widehat{K_j^\times}_3$ and put
\[
 \nu_{j,3}(y)=v_{\mathfrak q_3}(y_0),\qquad
 \nu_{j,17}(y)=f_j\sum_{i=0}^2v_{\mathfrak t_i}(y_0).
 \tag{E111.8}
\]
For the chosen $a_{j,p}$ define $\rho_{j,p},\sigma_{j,p}\in
\mathbb Z_3$ by the same two valuations of its initial
coordinate. Then
\[
 N_{\mathcal X_j/\mathbb Q}(y s_j(t))
 =3^{,\nu_{j,3}(y)+\sum\rho_{j,p}t_p}
  17^{,\nu_{j,17}(y)+\sum\sigma_{j,p}t_p}
                      \prod_{p\in P_j}p^{t_p}.
 \tag{E111.9}
\]
All sums converge. These are valuation maps on a specified
finite initial field, not unspecified scalar parameters.
In particular at $K_2$, in the seven S-unit columns of
(E111.15) below they are respectively the coefficient of
$1-\xi_2$ and twice the sum of the three prime-generator
coefficients. At every $K_j$ the same formulas hold with
$1-\xi_j$ and the included three prime generators, replacing
two by $f_j$.

We now classify the entire global section set of the actual
$H$ of E.38 with first toric class $r\kappa_3(17)$, for
every nonzero $r\in\mathbb Z_3$. Write $r=3^k u$, where
$k\ge0$ and $u\in\mathbb Z_3^\times$. Its entire second
toric image is
\[
 \left\{B_3\kappa_3(3)+B_{17}\kappa_3(17)
       +\sum_{p\in\bigcup_{j=0}^{k+1}P_j}r_p\kappa_3(p):
       B_3,B_{17}\in\mathbb Z_3,\quad
       (r_p)\in\mathcal R\!\left(\bigcup_{j=0}^{k+1}P_j\right)
       \right\}.
 \tag{E111.10}
\]
There is no further global condition on these coefficients.
The following maps specify every fiber, including its
topology. First take $u=1$ and choose arbitrary
\[
 (b,z,B,k_F,k_L,(y_j)_{2\le j\le k+1})
 \in\mathbb Z_3^3\times\mathcal J_F\times\mathcal K_L
                              \times\prod_{j=2}^{k+1}\mathcal U_j.
 \tag{E111.11}
\]
All objects for the pure factor and the $j=1$ factor have
the exact origins of E.110. For $j\ge2$ set
\[
 \begin{split}
 t_j&=3(r_p)_{p\in P_j},\qquad x_j=y_j s_j(t_j),\\
 n_{j,3}&=\nu_{j,3}(y_j)+\sum_{p\in P_j}\rho_{j,p}t_{j,p},\qquad
 n_{j,17}=\nu_{j,17}(y_j)+\sum_{p\in P_j}\sigma_{j,p}t_{j,p},\\
 e&=3B_{17}-2b-\sum_{j=2}^{k+1}n_{j,17},\\
 C&=3B_3-3z+\sum_{p\in P_1}\ell_p r_p
                  -\sum_{j=2}^{k+1}n_{j,3}-B,\\
 x_F&=k_Fs_F(B,C,e,3r|_{P_0}),\qquad
 x_L=\beta^b e_L^z k_Ls_L^*(3r|_{P_1}).
 \end{split}
 \tag{E111.12}
\]
The tuple $(x_F,x_L,x_2,\ldots,x_{k+1})$ is placed in the
actual cofinal positional factors (E111.13) below, then
sent through E.46's Kummer--Shapiro inverse. This is the
unique section class with the coordinates (E111.11).
The inverse reads each $y_j=x_j/s_j(3r|_{P_j})$, the
complex $b,z,k_L$ coordinates of E.107, the first pure
three-prime coordinate $B$, and finally $k_F$ by E.110.
For $k=0$ the products and sums over $j\ge2$ are empty,
and these maps are precisely (E110.10).
For general $u$, apply the actual arithmetic-equivariant
automorphism $\Phi_u(a,v(T))=(ua,v(T^u))$, with inverse
$\Phi_{u^{-1}}$, retaining the second toric coordinate.
Every nonempty fiber is consequently the product in
(E111.11), with each $\mathcal U_j$ a countable product
of copies of $\mathbb Z_3$ as specified in (E111.6).

Together with E.47 for $r=0$, this evaluates the entire
first-coordinate line $\mathbb Z_3\kappa_3(17)$ in $H$.
The actual maps from the intrinsic metabelian and marked
groups remain the quotient maps of E.38; the theorem
classifies their target section set and does not replace
the equations for a lift through their kernels.
The manuscript anchor is \S51.16, scans172--178,
folios733v--736v, equations(371)--(379), and Part E(c),(d).
\end{statement}

\begin{proof}
\emph{The precise positional factors and their prime maps.}
For first cocycle $A=3^{k+1}\kappa_3(17)$, E.46 gives
$E_{A,n}=\mathbb Q[X_n]/(X_n^{3^n}-17^{3^{k+1}})$.
At the cofinal levels $n=m+k+1$ the factorization is
\[
 \begin{gathered}
 X^{3^{m+k+1}}-17^{3^{k+1}}
 =(X^{3^m}-17)\prod_{j=1}^{k+1}
      17^{\varphi(3^j)}\Phi_{3^j}(X^{3^m}/17),\\
 E_{A,m+k+1}\xrightarrow{\sim}
 F_m\times L_m\times\prod_{j=2}^{k+1}L_{m,j},
 \qquad X\longmapsto
       (\alpha_m,\beta_m,\beta_{m,2},\ldots,\beta_{m,k+1}).
 \end{gathered}
 \tag{E111.13}
\]
Over $K_j$, $X^{3^m}-17\xi_j$ is Eisenstein at every
prime over seventeen. Also $\xi_j=\beta_{m,j}^{3^m}/17$.
Thus its displayed rational factor has degree
$3^m\varphi(3^j)$ and is irreducible. Its literal polynomial is
$X^{2\cdot3^{m+j-1}}+17^{3^{j-1}}X^{3^{m+j-1}}
+17^{2\cdot3^{j-1}}$.
The transition $X_m\mapsto X_{m+1}^3$ sends each factor
to the factor with the same $j$ and gives precisely the
norms in (E111.1). The lower positional levels are recovered
uniquely by norm; hence (E111.13) is an isomorphism of the
actual inverse systems, including the total norm to $\mathbb Q$.

The order of seventeen modulo $3^j$ is
$2\cdot3^{j-2}$ for $j\ge2$. Indeed
$17^2-1=288$ has three-adic valuation two, and the
binomial expansion gives
$v_3(17^{2\cdot3^a}-1)=2+a$.
It follows that $K_j$ has exactly three seventeen-primes,
each of residue degree $f_j$. The unique three-prime is
generated by $1-\xi_j$.
The polynomial for $L_{m,j}/K_j$, shifted by $X=Y-1$,
is Eisenstein at this prime: its constant term is
$-1-17\xi_j=-18-17(\xi_j-1)$ of valuation one, and all
intermediate binomial coefficients are divisible by three.
Consequently the single three-prime and all three
seventeen-primes remain unique above their predecessors,
with residue degree one in the vertical tower. There is
no other ramification, by the discriminant of the defining
polynomial. Since $\mu_3\subset K_j$, each adjacent step
is cyclic with generator $\beta_{m+1,j}\mapsto
\zeta\beta_{m+1,j}$.

\emph{Seven actual S-units and their exact four characters.}
Put $\xi=\xi_2$. The small cyclotomic base calculation
certifies class number one with PARI's default
\texttt{bnfcertify} flag zero and return value one.
Its full ordinary-unit generators are
$-1,\xi,1+\xi,1+\xi^2$. The first is its own norm
in every odd-degree extension and vanishes after
multiplication-by-three completion.
The three principal seventeen-prime generators are
\[
 \begin{split}
 \pi_1&=2+\xi+\xi^2+\xi^3+2\xi^4,\\
 \pi_2&=2+\xi+\xi^3-\xi^4+\xi^5,\\
 \pi_3&=-1+\xi+\xi^2+\xi^3-\xi^4.
 \end{split}
 \tag{E111.14}
\]
Together with $\lambda_2=1-\xi$, these give the seven
columns
\[
             (\xi,1+\xi,1+\xi^2,\lambda_2,
                                      \pi_1,\pi_2,\pi_3).
 \tag{E111.15}
\]
The actual ideal valuations of the last three columns form
the identity matrix in PARI's prime order. All their
three-valuations are zero; $v_3(\lambda_2)=1$.
The retained certificate gives their maximal-order ideals,
unit basis, defining field and literal coefficient vectors.

For the reciprocity labeling use
$\mathbb F_{289}=\mathbb F_{17}[\zeta]/(\zeta^2+\zeta+1)$.
The three values of $\xi$ are, in that order,
$(2,8),(9,11),(6,15)$ in the basis $(1,\zeta)$.
The corresponding prime generators are respectively
$\pi_3,\pi_1,\pi_2$.
Lift these roots to modulus $17^2$ to read the unit part
of a generator having valuation one. For
$a=17^b\xi^c$ and $u=17^v u_0$, arithmetic reciprocity is
\[
        (a,u)_{17,3}
          =\left(\overline{\xi}^{,cv}
                                \overline{u_0}^{-b}\right)^{96}.
 \tag{E111.16}
\]
The omitted tame sign has order two and disappears in
this cubic symbol. The formula is calibrated by the
arithmetic Frobenius on the cube root of a residue unit.
The three-place character is the negative sum of the
other three, by global reciprocity: the columns are
S-units and all remaining local symbols are one.
The two required matrices, with the four places as rows,
are therefore
\[
 D^{(2)}=
 \begin{pmatrix}
 0&0&0&0&1&1&1\\
 1&2&1&2&2&2&1\\
 1&2&1&2&1&2&2\\
 1&2&1&2&2&1&2
 \end{pmatrix},\qquad
 D^{(>2)}=
 \begin{pmatrix}
 0&0&0&0&1&1&1\\
 0&0&0&0&0&0&2\\
 0&0&0&0&2&0&0\\
 0&0&0&0&0&2&0
 \end{pmatrix}.
 \tag{E111.17}
\]
They are the characters for radicands $17\xi$ and $\xi$,
respectively. Both have image exactly $\mathcal H_3$.
For a vector in that hyperplane, its first three entries
give the coefficients of a representative using
$\pi_1,\pi_2,\pi_3$ through the matrices
\[
 R_2=\begin{pmatrix}2&0&2\\0&1&1\\2&2&0\end{pmatrix},
 \qquad
 R_{>2}=\begin{pmatrix}0&0&2\\1&1&1\\0&2&0\end{pmatrix}.
 \tag{E111.18}
\]
The certificate checks both inverses, every vector of
$\mathcal H_3$, and every residue and division in (E111.16).

These are the actual characters at all subsequent fields.
For $j\ge3$ the local norm from $K_j$ to $K_2$ satisfies
\[
 N_{K_j/K_2}(17\xi_j)=17^{3^{j-2}}\xi,
 \qquad N_{L_{m,j}/K_j}(\beta_{m,j})=17\xi_j.
 \tag{E111.19}
\]
The first equality uses $N(\xi_{a+1})=\xi_a$ at every
cyclotomic cubic step; the second is the constant-term
norm in an odd-degree binomial. At each labeled place
the field norms are these local norms as well, because
there is exactly one place above the chosen predecessor.
For a base S-unit $u$ the cup-product projection formula
and the local invariant identity give
\[
 \operatorname{Cor}\bigl([a]\cup\operatorname{Res}[u]\bigr)
       =[N a]\cup[u],\qquad
       \operatorname{inv}\operatorname{Cor}=\operatorname{inv}.
 \tag{E111.20}
\]
Thus no local degree is multiplied into the character.
Since $17^{3^{j-2}}$ is a cube for $j\ge3$, the included
columns have matrix $D^{(>2)}$ there, and the included
columns at every $L_{m,2}$ have matrix $D^{(2)}$.
This is also a direct calibration of the wild three-place
column: its value is forced by the same four-place
product relation, not selected independently.
We use the proved cup and restriction/corestriction
identities of Milne III, Sections2--4
\cite{E_MilneCFT}; III Lemma3.2 by itself is not being
treated as a printed proof of these compatibilities.

\emph{The S-unit and S-class sequences, with their actual maps.}
First $\operatorname{Cl}(K_j)\{3\}=0$ for every $j$.
Starting with the Eisenstein integers, each cyclotomic
cubic step has exactly one ramified prime. The ordinary
ambiguous-class formula makes the three-part of its
ambiguous class number equal to the reciprocal of a
three-power unit norm index. It is an integer, so that
index is one and the ambiguous three-group is zero.
A nonzero finite three-group module for a three-group
has nonzero fixed points. Induction proves the assertion,
and then its S-class quotient is also zero. This is the
same exact ideal norm induction used in E.47
\cite[Theorem1 and its ideal proof]{E_LemmermeyerAmbiguous}.

Here is the full induction for the vertical tower; it
also proves the sufficiency in (E111.4). Write $E/F$ for
one vertical cubic and $G=\langle\sigma\rangle$.
All ramification belongs to S, so on divisors outside S
\[
 \operatorname{Div}_{\notin S}(E)^G
       =j\operatorname{Div}_{\notin S}(F),\qquad
 \ker N=(\sigma-1)\operatorname{Div}_{\notin S}(E).
 \tag{E111.21}
\]
For a split prime these are the sum and difference maps
on its three primes; for an inert prime the norm is
multiplication by three and both asserted kernels are
zero. This proves the identities on every summand.
Hilbert90 then gives the actual isomorphism
\[
 \ker(j:\operatorname{Cl}_S(F)\to\operatorname{Cl}_S(E))
  \longrightarrow H^1(G,U_E),\quad
 [D]\longmapsto\bigl(\sigma\mapsto\sigma(x)/x\bigr),
 \quad \operatorname{div}_{\notin S}(x)=jD.
 \tag{E111.22}
\]
Its inverse takes a Hilbert90 element, whose invariant
divisor is the extension of a unique lower divisor.
Changing that element by an S-unit changes a coboundary.
The kernel in (E111.22) is killed by three because
$Nj=3$. It is zero when the lower three-class group is
zero. Hence $H^1(G,U_E)=0$ at each induction step.

The S-unit Herbrand quotient is $3^3$. In its rational
logarithmic representation, each lower complex place
contributes a regular $G$-module, each of the four totally
ramified finite S-places contributes a trivial module,
and the product formula removes one trivial module.
The regular module has quotient one and a trivial
rank-one module has quotient three. Commensurable
lattices and finite torsion have quotient one in their
ratio. This is the logarithmic-lattice proof of Milne
VII Proposition3.1, with these actual four finite-place
summands included \cite{E_MilneCFT}. Therefore
\[
 [U_F:NU_E]=3^3|H^1(G,U_E)|=27.
 \tag{E111.23}
\]
The four characters already have image $\mathcal H_3$ of
order27. The cyclic Hasse norm theorem identifies their
kernel with $U_F\cap NE^\times$; units outside S are
local norms in every unramified completion, and there
are no real places. Hence
$[U_F:U_F\cap NE^\times]=27$, and (E111.23) proves
\[
                         NU_E=U_F\cap NE^\times.
 \tag{E111.24}
\]
This is the actual equality of unit norm images.
The Hasse theorem and its proof are
\cite[VIII, Theorem3.1]{E_MilneCFT}.

For completeness the S-class consequence follows by a
literal divisor map. For an invariant class $[D]$, write
$(\sigma-1)D=\operatorname{div}_{\notin S}(x)$ and send it
to $Nx$ in $(U_F\cap NE^\times)/NU_E$.
Changing the generator changes a unit norm; changing
$D$ by a principal divisor leaves its class unchanged.
Conversely (E111.21) constructs $D$ from any field norm
which is an S-unit. A zero class permits division by a
norm-one element, by Hilbert90, after which $D$ is
invariant as a divisor. Its class is an extended lower
class by (E111.21). Thus the exact sequence is
\[
 \operatorname{Cl}_S(F)\xrightarrow{j}
    \operatorname{Cl}_S(E)^G\longrightarrow
       (U_F\cap NE^\times)/NU_E\longrightarrow0.
 \tag{E111.25}
\]
The right group vanishes by (E111.24), and the left
group has no three-primary part by induction. The
invariant upper three-group is zero, so the finite
three-group fixed-point argument makes the whole upper
three-group zero. This proves (E111.2) at every level.
It also explains precisely why the old field
$K_2(\sqrt[3]{17})$ has a different norm calculation:
its three-prime splits, so the actual logarithmic
place module has Herbrand quotient nine rather than27.
The inclusion of that field is the old $B_1$ of E.86;
the maps in (E111.1) use the distinct radicand $17\xi$.

All S-unit groups are finitely generated. The quotient
in (E111.4) is killed by three, since the norm of an
included base unit is its cube; completion preserves
this finite quotient and its explicit characters.
The free S-unit ranks are $r_{m,j}+3$, so their norm
kernel has free rank $2r_{m,j}$. There are exactly
$\mu_{3^j}$ as three-power roots of unity in $L_{m,j}$:
adjoining $\mu_{3^{j+1}}$ would give a nontrivial
unramified extension at seventeen, contrary to the
total ramification of every subextension of
$L_{m,j}/K_j$. Norm on the retained roots is cubing,
whose kernel is $\mu_3$. This proves the second line
of (E111.4), with its actual torsion map.

\emph{Surviving outside-S divisors and coherent principal generators.}
For $p\ne3,17$, take the prime-to-three and three-primary
parts of seventeen in $\mathbb F_p^\times$:
$17=\omega_p v_p$, with $\omega_p$ of three-power order
and $v_p$ of order prime to three. If $p\in P_j$ then
$\omega_p$ has order exactly $3^j$; it gives the unique
degree-one embedding of $K_j$ relevant here by
$\xi_j\mapsto\omega_p^{-1}$. In that embedding
$17\xi_j\mapsto v_p$, whose compatible cube roots are
the unique roots of order prime to three. They define
a unique degree-one prime chain in (E111.1).

These are all the surviving divisor coordinates.
One can check the assertion on the actual positional
root sets, avoiding any assumption of surjective ideal
norms. For a rational Frobenius its action is affine,
$x\mapsto px+A_p$ on $\mathbb Z_3$ as in E.46.
A finite orbit would satisfy
$(p^n-1)(x+A_p/(p-1))=0$ in $\mathbb Q_3$;
therefore its sole possible point is the fixed point.
On the complement the pro-three part of the closed
Frobenius group acts freely. In each nonfixed compact
orbit neighborhood, refining the positional level
partitions a cell into arbitrarily many $3^a$ translates.
An invariant $\mathbb Z_3$-valued measure must give that
cell a value divisible by every $3^a$, hence zero.

The comparison with ideal norms is exact: a prime
corresponds to a finite Frobenius orbit; send its divisor
coefficient to the constant orbit sum in the permutation
module. Positional pushforward multiplies that
coefficient by the ratio of orbit lengths, precisely
the residue degree in the ideal norm. Thus the inverse
limit of outside-S divisor modules is the restricted
module on the fixed chains, namely $\mathcal R(P_j)$.
The fixed point lies in this factor exactly when the
three-primary residue of seventeen has order $3^j$,
as the preceding explicit root construction shows.

At a finite field level, (E111.2) makes the completed
outside-S divisor map onto. To see exactness directly,
the group of principal outside-S divisors is free and
has finite index in the full divisor group, with no
three-part in that index. Its inclusion therefore
induces an isomorphism of multiplication-by-three
completions. The kernel is the compact completed
S-unit group: the original exact sequence splits
over the free principal divisor group before taking
completions. Each prescribed divisor has consequently
a nonempty compact fiber.

For a compatible infinite divisor system, every finite
collection of norm equations is soluble: choose an
element over the largest field occurring, then take
its actual norms downward. These choices lie in the
specified compact fibers. The finite intersection
property in their countable product gives a coherent
preimage. This proves surjectivity in (E111.6), in
particular the existence of every $a_{j,p}$.
Restricted exponents in (E111.7) then give a convergent
product: modulo each $3^a$ only finitely many factors
are nontrivial at every fixed positional level.
The splitting is continuous and its inverse is the
displayed divisor and unit map. Replacing $a_{j,p}$
by $a_{j,p}u_{j,p}$ changes the unit coordinate exactly
by $y\mapsto y\prod_pu_{j,p}^{-t_p}$; this product also
converges. These are the full choice ambiguities.

The compact group $\mathcal U_j$ is metrizable and has
no torsion. Indeed a torsion coherent element would
lie in $\mu_{3^j}$ at every level, while passage across
$a$ levels raises it to $3^a$; every fixed coordinate
is therefore one. Its dual is a countable divisible
three-primary torsion group. Divisibility follows by
extending a finite continuous character from $3\mathcal U_j$
to $\mathcal U_j$, since multiplication by three is
injective. A basis of its elements killed by three,
with successive divisions, gives a direct sum of
copies of $\mathbb Q_3/\mathbb Z_3$; induction on the
order of a character proves both independence and
spanning. Dualizing gives the claimed product map
and its inverse by finite character equations.
Every such character factors through a finite-level
S-unit group and extends from its compact image;
hence the norm-transpose specification after (E111.7)
is an actual coordinate construction.

There are infinitely many of these coordinates.
At each $L_{m,j}$ there is one place above three.
Apply Kato Theorem1.1(2) to the extension obtained by
adjoining all three-power roots of unity and all
three-power roots of seventeen. This is the same
false-Tate field containing the literal tower (E111.1).
Kato's definition is the image of the compatible norm
system, so restricting that system to (E111.1) gives
actual elements of $\mathcal U_j$. Its projection to
the three-unit group of $L_{m,j}$ has finite index
and rank $r_{m,j}$, which tends to infinity.
Thus the countable product is infinite. We use
\cite[Theorem1.1(2), the definition preceding it,
and its complete proof in Sections4--5]{E_KatoUniversalNorms}.
This application evaluates the compact group's rank;
it does not assert that every finite S-unit is an
initial coordinate of a coherent system.

For (E111.9), the residue degree of the three-prime
in $K_j/\mathbb Q$ is one, and those of its three
seventeen-primes are $f_j$. Outside S the generator
has only the indicated degree-one prime. A rational
completed multiplicative class is determined by all
these valuations; its rational unit sign has zero
three-primary Kummer class. This proves (E111.9)
exactly. The included $\pi_i$ are still principal
seventeen-prime generators in $K_j$, since the
cyclotomic extensions at seventeen are unramified
with a unique prime above each predecessor.
Together with $1-\xi_j$ they give the finite valuation
coordinates stated after (E111.9).

\emph{The complete section fibers and their toric inverse.}
E.46 identifies the whole fixed-first section set with
the compatible norm systems whose total rational norm
is a cube. The actual factorization (E111.13) is a
product decomposition of those systems. The pure and
$j=1$ components are exactly E.110's factors. For every
new $j$, (E111.6)--(E111.9) give all its coordinates.

The outside-S prime sets $P_j$ are disjoint. A cube
total norm must therefore have the coordinate $3r_p$
on its unique surviving component for each rational
prime. This proves necessity of precisely the support
in (E111.10). There are no other surviving outside-S
coordinates. Conversely, for any such target, (E111.12)
makes the seventeen exponent of the total norm
$e+2b+\sum n_{j,17}=3B_{17}$ and its three exponent
$B+C+3z-\sum\ell_pr_p+\sum n_{j,3}=3B_3$.
Every other exponent is $3r_p$ by construction.
All scalar coordinates are integral, with no
restriction on the chosen $y_j$. This proves sufficiency
and the exact scaled toric target using (E46.7).

The inverse in the statement reads independent factor
coordinates and then uses these two literal equations;
thus it is both injective and onto. All valuations,
restricted products and finite sums are continuous;
the inverse maps already proved for each factor show
the asserted homeomorphism. In particular the norm
values in (E111.8) need no separate ordinary-class or
universal-unit projection computation: they are read
on an arbitrary chosen coherent S-unit, and the pure
component changes by the displayed integral amounts.

For example $17$ has order nine modulo nineteen,
so $19\in P_2$. With $k=1$, choose $x_2=a_{2,19}^3$,
$x_L=1$ and
$x_F=s_F(-3\rho_{2,19},0,-3\sigma_{2,19},0)$.
Their total rational norm is exactly $19^3$.
The resulting section has toric pair
$(3\kappa_3(17),\kappa_3(19))$.
For the first class $\kappa_3(17)$, (E110.8) excludes
that second coordinate. This is a comparison through
the actual two positional factorizations and the
compensating pure norm, without assigning an
intrinsic lift to either section class.
Finally the law of $H$ verifies $\Phi_u$ and its inverse
directly, including their commutation with the
cyclotomic action. This transports the complete
classification from $3^k\kappa_3(17)$ to every nonzero
$r\kappa_3(17)$ as asserted.
\end{proof}
