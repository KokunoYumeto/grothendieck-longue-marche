\subsection{The pure norm tower and the entire fixed-seventeen fiber}

\begin{statement}{E.110}{Proved}{All pure three-class groups, every positional divisor, and the complete fixed first Kummer class}
Choose the positive compatible roots
$\alpha_0=17$, $\alpha_{d+1}^3=\alpha_d$, and put
$F_d=\mathbb Q(\alpha_d)$ and $M_d=F_d(\zeta)$, where
$\zeta=\zeta_3$ is the root fixed throughout the paper.
All completions of multiplicative groups below mean
$\widehat{A}_3=\varprojlim_m A/A^{3^m}$ with their inverse-limit
topology. For an ordinary unit group this is its usual compact
$\mathbb Z_3$-module completion. The actual ideal and unit maps satisfy
\[
 \operatorname{Cl}(M_d)\{3\}=\operatorname{Cl}(F_d)\{3\}=0
       \quad(d\geq1),\qquad
 \frac{\widehat{\mathcal O_{M_d}^{\times}}_3}
      {N_{M_{d+1}/M_d}\widehat{\mathcal O_{M_{d+1}}^{\times}}_3}
       \simeq(\mathbb Z/3)^3,\qquad
 \frac{\widehat{\mathcal O_{F_d}^{\times}}_3}
      {N_{F_{d+1}/F_d}\widehat{\mathcal O_{F_{d+1}}^{\times}}_3}
       \simeq\mathbb Z/3 .
 \tag{E110.1}
\]
The first quotient is identified with the four local cubic characters
whose sum is zero; complex conjugation acts on that hyperplane by
negative permutation of the places. Its fixed line is the second
quotient. If $\delta_{d,3}$ is the normalized finite wild character
of E.65 and $\varepsilon=7\alpha_1-18$ is included into $F_d$,
the precise comparison to the fixed line is
$u\mapsto(0,c_d\delta_{d,3}(u),-c_d\delta_{d,3}(u),0)$, where
$c_d=2\,\delta_{d,3}(\varepsilon)^{-1}\in\mathbb F_3^\times$.
Its denominator is nonzero by the proof below.

For a set of rational primes $P$, write
\[
 \mathcal R(P)=
 \left\{(t_p)_{p\in P}\in\prod_{p\in P}\mathbb Z_3:
       \#\{p:t_p\notin3^m\mathbb Z_3\}<\infty
                          \text{ for every }m\right\},\qquad
 P_j=\{p\ne3,17:v_3(\operatorname{ord}_{\mathbb F_p^\times}(17))=j\}.
 \tag{E110.2}
\]
The topology on $\mathcal R(P)$ is defined by the subgroups
$3^m\mathcal R(P)$. Thus the quotients are direct sums of
$\mathbb Z/3^m$, including when $P$ is infinite.
Let
\[
 \mathcal X_F=\varprojlim_{d,N}\widehat{F_d^\times}_3,\qquad
 \mathcal J_F=\varprojlim_{d,N}
                   \widehat{\mathcal O_{F_d}^{\times}}_3 .
 \tag{E110.3}
\]
Number the two persistent three-prime chains in the pure tower by
$\mathfrak p_d^{\,0},\mathfrak p_d^{\,1}$ as in E.65. The first has
ramification index $3^{d-1}$ over $\mathbb Q_3$, and the second has
ramification index $2\cdot3^{d-1}$. Both have residue degree one.
The actual valuations give a split exact sequence of topological groups
\[
 0\longrightarrow\mathcal J_F\longrightarrow\mathcal X_F
   \xrightarrow{\operatorname{div}}
       \mathbb Z_3^3\oplus\mathcal R(P_0)\longrightarrow0,\qquad
 \mathcal J_F\simeq\prod_{i\ge1}\mathbb Z_3.
 \tag{E110.4}
\]
The three finite coordinates of the quotient are the valuations at
$\mathfrak p^{\,0},\mathfrak p^{\,1}$ and the prime over seventeen.
For coordinates $(B,C,e,t)$ its actual norm to $\mathbb Q$ is
\[
                N_{\mathcal X_F/\mathbb Q}
                 =3^{B+C}17^e\prod_{p\in P_0}p^{t_p}
                   \quad\text{in }\widehat{\mathbb Q^\times}_3 .
 \tag{E110.5}
\]
Here and below infinite products converge in the specified
multiplication completion.

The following choices give literal maps for both isomorphisms in
(E110.4). Choose coherent completed principal generators
$a_0,a_1\in\mathcal X_F$ of the two three-prime chains, and for
each $p\in P_0$ choose a coherent completed principal generator
$a_p$ of its unique surviving degree-one prime chain.
The sequence $\alpha=(\alpha_d)_d$ already generates the seventeen
chain. Then the splitting and its inverse are
\[
 \begin{split}
 s_F(B,C,e,t)&=a_0^B a_1^C\alpha^e
                         \prod_{p\in P_0}a_p^{t_p},\\
 x&\longmapsto
   \bigl(x\,s_F(\operatorname{div}x)^{-1},
                         \operatorname{div}x\bigr).
 \end{split}
 \tag{E110.6}
\]
Existence of each coherent generator, including the entire restricted
divisor splitting, is proved below using the actual norm maps.
For the compact factor let
$\mathcal J_F^\vee=\operatorname{Hom}_{\mathrm{cts}}
(\mathcal J_F,\mathbb Q_3/\mathbb Z_3)$.
The target here is discrete.
Choose a basis $(\chi_{i,1})_{i\ge1}$ of
$\mathcal J_F^\vee[3]$ over $\mathbb F_3$, and choose successive
divisions $3\chi_{i,n+1}=\chi_{i,n}$. Its coordinate map is
\[
 \begin{split}
 \Phi_F:\mathcal J_F&\longrightarrow\prod_{i\ge1}\mathbb Z_3,\\
 \chi_{i,n}(u)&=\frac{\Phi_F(u)_i\bmod3^n}{3^n}
                         \quad\text{in }\mathbb Q_3/\mathbb Z_3 .
 \end{split}
 \tag{E110.7}
\]
Every character here is represented at a finite pure level by an
ordinary-unit coordinate functional. The identifications among those
functionals are precisely the transposes of the actual norm matrices.
The inverse of (E110.7) is the unique element satisfying the displayed
finite character equations. This specifies the basis choices and
the exact morphism; the proof supplies existence, uniqueness and
continuity.

Now let $\mathscr S_{17}(H)$ denote the geometric-conjugacy classes
of global sections of the actual quotient $H$ in E.38 with first
toric Kummer class $\kappa_3(17)$. Use the origin and the
Kummer--Shapiro comparison of E.46, so its fixed first cocycle is
$A=3\kappa_3(17)$. Its entire second toric image is
\[
 \left\{
   B_3\kappa_3(3)+B_{17}\kappa_3(17)
       +\sum_{p\in P_0\cup P_1}r_p\kappa_3(p):
   B_3,B_{17}\in\mathbb Z_3,\ 
   r\in\mathcal R(P_0\cup P_1)
 \right\}.
 \tag{E110.8}
\]
Every fiber over an element of (E110.8) has the following complete
coordinates. Keep E.107's coherent complex three-unit
$e_L$ with initial value $\lambda^3$, its normalized divisor
splitting $s_L^*$, and its actual phase coefficients
$\ell_p\in\{0,\ldots,8\}$ for $p\in P_1$.
Write $\mathcal K_L=\{u\in\mathcal U_{L,\infty}:u_0=1\}$
for the complex unit kernel denoted
$\ker(\operatorname{pr}_0)$ in E.69 and E.107.
Its specified recursive coordinates give
$\mathcal K_L\simeq\prod_{d\ge0}\mathbb Z_3^{2\cdot3^d}$.
For arbitrary
\[
 (b,z,B,k_F,k_L)\in
     \mathbb Z_3^3\times\mathcal J_F\times\mathcal K_L
 \tag{E110.9}
\]
put
\[
 \begin{split}
 t_L&=3(r_p)_{p\in P_1},&
 t_F&=3(r_p)_{p\in P_0},\\
 e&=3B_{17}-2b,&
 C&=3B_3-3z+\sum_{p\in P_1}\ell_p r_p-B,\\
 x_L&=\beta^b e_L^z k_L s_L^*(t_L),&
 x_F&=k_F s_F(B,C,e,t_F).
 \end{split}
 \tag{E110.10}
\]
The pair $(x_F,x_L)$, placed at the actual positional levels of
E.46, is the unique section class with these coordinates.
The inverse reads the complex $b,z,k_L$ coordinates by E.107,
reads $B$ from the first pure three-prime valuation, and obtains
$k_F$ by (E110.6). It follows that each nonempty fiber is
homeomorphic, by these stated choices, to
\[
          \mathbb Z_3^3
               \times\prod_{i\ge1}\mathbb Z_3
               \times\prod_{d\ge0}\mathbb Z_3^{2\cdot3^d}.
 \tag{E110.11}
\]
Equations (E110.8)--(E110.11) classify the entire fixed first
class $\kappa_3(17)$ in $H$. The maps from the intrinsic
metabelian and marked quotients to this set remain the actual
quotient-induced maps of E.38.
For every $r\in\mathbb Z_3^\times$ the arithmetic-equivariant
automorphism
$\Phi_r(a,v(T))=(ra,v(T^r))$ of the actual
$H=3\mathbb Z_3\ltimes(3,T-1)\mathbb Z_3[[T-1]]$
has inverse $\Phi_{r^{-1}}$.
It carries this classification onto the entire first class
$r\kappa_3(17)$, preserving the second toric coordinate.

For an explicit comparison with E.107's pure-component-$1$ locus,
its actual table has $\ell_7=8$ and $c_7=2$ in $\mathbb F_3$.
Taking $r_7=1$ and every other target coordinate zero, (E110.10)
with $b=z=B=0$ gives
\[
 x_F=a_1^8,\qquad x_L=s_L^*(3[7]),\qquad
 N(x_F)=3^8,\quad N(x_L)=7^3\,3^{-8}.
 \tag{E110.12}
\]
Their combined scaled toric image is
$(\kappa_3(17),\kappa_3(7))$.
The pure-component-$1$ equations of E.107 require
$\sum c_pr_p=0$ in $\mathbb F_3$ and exclude this coordinate;
(E110.12) displays the actual correction in the complete system.
The manuscript anchor is \S51.16, scans172--178,
folios733v--736v, equations(371)--(379), and Part E(c),(d).
\end{statement}

\begin{proof}
\emph{The fields, the four labeled places and the initial class group.}
Let $K=\mathbb Q(\zeta)$ and let $\rho\in\mathbb Q_3$ be the
unique cube root of seventeen, chosen with
$\rho\equiv23\pmod{27}$.
The field $M_1/K$ is cyclic cubic. At three the three embeddings
are $\alpha_1=\rho\zeta^j$, $j=0,1,2$; thus three splits completely.
The only ramified prime of $M_1/K$ is the prime over seventeen.
It is totally ramified by $X^3-17$, and has residue field
$\mathbb F_{17^2}$.
The units of $K$ are generated by $-1$ and $\zeta$.
The element $\zeta$ is a cube in this residue field because
$9\mid17^2-1$; in the tame totally ramified cubic extension the
residue unit norm is cubing, while the principal unit norm is onto.
At every other place these units are local norms as well.
The Hasse norm theorem therefore makes every unit of $K$ a field
norm. The Eisenstein integer ring has class number one, so the
ambiguous class number formula gives
$\operatorname{Cl}(M_1)\{3\}^{\operatorname{Gal}(M_1/K)}=0$.
A nonzero finite abelian three-group acted on by a three-group
has nonzero fixed points: on its elements of order dividing three,
an order-three operator has nilpotent difference from the identity.
Consequently $\operatorname{Cl}(M_1)\{3\}=0$.
We use the opened Hasse norm theorem
\cite[VIII, Theorem3.1 and its proof]{E_MilneCFT}
and the opened ambiguous-class formula with its complete
ideal/Herbrand proof
\cite[Theorem1, formulas(1),(2), and Proposition1]{E_LemmermeyerAmbiguous}.

The adjacent extension $M_{d+1}/M_d$ is cyclic cubic, generated by
$\alpha_{d+1}\mapsto\zeta\alpha_{d+1}$.
At seventeen every layer is Eisenstein and the residue field
remains $\mathbb F_{289}$.
At the place of $M_1$ labeled $j$ the defining equation for $M_d$ is
\[
       X^{3^{d-1}}=\rho\zeta^j,\qquad j=0,1,2.
 \tag{E110.13}
\]
For $j=0$, the polynomial shifted by $X=Y-1$ has constant
term $-1-\rho$ of valuation two in $K_3=\mathbb Q_3(\zeta)$.
For $j=1,2$ that valuation is one.
All intermediate coefficients lie strictly above the segment
joining this constant term to the leading coefficient:
the three-adic valuations of the binomial coefficients give this
directly, since $3^{d-1}$ is a power of three.
The Newton segment has denominator $3^{d-1}$ in lowest terms
in each case. Thus the three local degrees are each
$3^{d-1}$ and each extension is totally ramified.
There are exactly three places over three at every $M_d$.
Their restrictions to $F_d$ are the two places stated in the theorem:
complex conjugation fixes the $j=0$ place and interchanges
$j=1,2$. The local degrees over $\mathbb Q_3$ are respectively
$3^{d-1}$ and $2\cdot3^{d-1}$.
This also proves that the labels persist under every actual norm.
The discriminant of the defining radical polynomials permits
ramification only over three and seventeen, so these four places
are exactly the ramified places in every adjacent $M$-extension.

\emph{Three explicit units and their actual characters.}
Put $a=\alpha_1$ and set
\[
 \begin{split}
 u_0&=\zeta,\\
 u_1&=\frac{(1-4\zeta)a^2+(11+13\zeta)a-35-7\zeta}{3},\\
 u_2&=\frac{(5+\zeta)a^2+(13+2\zeta)a+35+7\zeta}{3}.
 \end{split}
 \tag{E110.14}
\]
The characteristic-zero certificate computes their multiplication
matrices in the basis
$(1,a,a^2,\zeta,a\zeta,a^2\zeta)$.
For $u_1,u_2$ the resulting monic polynomials are
\[
 \begin{split}
 X^6+63X^5+1071X^4+1618X^3+1071X^2+63X+1,\\
 X^6-63X^5+1071X^4-1618X^3+1071X^2-63X+1.
 \end{split}
 \tag{E110.15}
\]
Thus they are algebraic-integer units, independently of a
class-group computation. Their norms to $K$ are
$\zeta^2$ and $-\zeta^2$.
Also $u_1c(u_1)=18-7a$.
The separate small PARI computation certifies the full
class number of $M_1$ as one and verifies the two free unit
coordinates and the primitive three-primary torsion coordinate.
The proof of the three-primary assertions uses the preceding
exact unit identities and the displayed local matrix.

Use arithmetic local reciprocity, and define
$\chi_{d,v}(u)\in\mathbb F_3$ by
\[
 \operatorname{rec}_v(u)(\alpha_{d+1})/\alpha_{d+1}
      =\zeta^{\chi_{d,v}(u)}.
 \tag{E110.16}
\]
The common root $\zeta$ fixes the sign at every place.
In the order $j=0,1,2$, seventeen, the matrix on
$(u_0,u_1,u_2)$ is
\[
 \bigl(\chi_{1,v}(u_i)\bigr)_{v,i}=
 D=
 \begin{pmatrix}
  2&2&2\\
  2&2&0\\
  2&0&2\\
  0&2&2
 \end{pmatrix}.
 \tag{E110.17}
\]
Here is the calibration and a fully finite verification of this
particular matrix. In $K_3$ put $\pi=1+\rho\zeta$ and work in
\[
  R=\mathbb Z/27[\pi]\big/
       \bigl((\pi-1)^2+\rho(\pi-1)+\rho^2,\ \pi^5\bigr),
       \qquad \rho=23\bmod27 .
 \tag{E110.18}
\]
The unique normalized character vanishing on cubes and on the
unit norms from
$\Pi^3-3\Pi^2+3\Pi-\pi=0$
has coefficients $(1,2,0,0)$ on
$1+\pi,\ldots,1+\pi^4$, by the exact determinant norm computation
of E.65, recomputed here.
Its value at $\zeta$ is two.
The cyclotomic character for $K_3(\zeta_9)/K_3$ is
\[
 \chi_\zeta(y)
    =\frac{N_{K_3/\mathbb Q_3}(y)^{-1}-1}{3}\pmod3
                    \quad(y\in\mathcal O_{K_3}^{\times}).
 \tag{E110.19}
\]
In particular $\chi_\zeta(\rho)=1$ and
$\chi_\zeta(\zeta)=0$.
The Hilbert symbol is skew-symmetric; hence the arithmetic
character for the radicand $\rho\zeta$ takes value two on $\zeta$.
This fixes its identification with the normalized finite character.
For the radicand $\rho\zeta^j$ its character on $y$ is
$\chi_{\rho\zeta}(y)+(j-1)\chi_\zeta(y)$.
Evaluating the literal units (E110.14) at
$a=\rho\zeta^j$ gives the first three rows of (E110.17).
At seventeen the arithmetic character is
$-\log_\zeta(\bar u^{96})$ in $\mathbb F_{289}^{\times}$,
which gives the last row. The certificate checks all twenty-seven
mixed unit products with the actual finite ring multiplication.
It also records the polynomial reductions before dividing
denominators, so the fractions in (E110.14) are evaluated with the
required extra three-adic precision.
The local Artin and Hilbert-symbol conventions are the opened
cup-product constructions and their proofs in
\cite[III, Theorems3.1,4.4 and the intervening norm compatibility]{E_MilneCFT}.

\emph{The norm square at every height and the class induction.}
At each of the four labeled places the local extension
$(M_d)_v/(M_1)_{v_1}$ has the full global degree
$3^{d-1}$, and the literal field norm of $\alpha_d$ is $\alpha_1$.
The sign is positive because that degree is odd.
For an included $u\in M_1^\times$ the precise cohomological
comparison is
\[
 \begin{split}
 \operatorname{Cor}_{(M_d)_v/(M_1)_{v_1}}
   \bigl([\alpha_d]\cup\operatorname{Res}[u]\bigr)
       &=[N\alpha_d]\cup[u]=[\alpha_1]\cup[u],\\
 \operatorname{inv}_{(M_1)_{v_1}}\operatorname{Cor}
       &=\operatorname{inv}_{(M_d)_v},\\
                 \chi_{d,v}(u)&=\chi_{1,v_1}(u).
 \end{split}
 \tag{E110.20}
\]
The first line is the projection formula, with the Kummer
corestriction identified with the actual multiplicative norm.
The second is the proved local invariant formula
\cite[III, Section2, formulas(29),(30), and Theorem3.1]{E_MilneCFT}.
It applies to these completions even when their full relative
extension is not Galois. Thus no local-degree multiplier is
inserted in the last line.

The columns of $D$ span the entire hyperplane
$H=\{(x_0,x_1,x_2,x_{17}):\sum x_v=0\}$:
its first three rows have determinant $-8$, a three-adic unit.
Every ordinary unit at height $d$ has local character sum zero
by global reciprocity and is a local norm at every unramified
place. The included units and (E110.20) therefore show that its
field-norm index is exactly $|H|=27$ at every height.
The ambiguous-class formula, with four totally ramified places,
now gives
\[
 |\operatorname{Cl}(M_{d+1})\{3\}^{\operatorname{Gal}(M_{d+1}/M_d)}|
       =|\operatorname{Cl}(M_d)\{3\}|\,
                               \frac{3^4}{3\cdot27}.
 \tag{E110.21}
\]
Starting from the proved initial class group, the finite
three-group fixed-point argument proves the first assertion
of (E110.1) for every $M_d$.
Extension of ideals from $F_d$ to $M_d$ followed by norm is
multiplication by two. It is injective on the three-primary class
group, proving the corresponding assertion for $F_d$ with its
actual ideal maps.

The exact ambiguous/strongly-ambiguous sequence in
Lemmermeyer's Proposition1 identifies
$(E_d\cap N M_{d+1}^{\times})/N E_{d+1}$ with a quotient of
the ambiguous class group. Its three-primary part is zero.
Since the norm quotient of units is killed by three, its actual
unit-norm index is therefore also $27$.
This gives the first unit quotient in (E110.1).
After completion, complex conjugation on its local character
coordinates is $-\!P$, where $P$ fixes the first and last places
and exchanges the middle two. This follows from
$c\zeta=\zeta^{-1}$ and the functoriality of (E110.16).
The fixed line in $H$ is
$\{(0,t,-t,0):t\in\mathbb F_3\}$.
Taking fixed modules is exact because two is invertible in
$\mathbb Z_3$; inclusion of pure units has inverse
$N_{M_d/F_d}^{1/2}$ on the fixed subgroup.
Norm commutes with these maps. Hence the fixed line is exactly
the pure unit quotient, proving the final assertion of (E110.1).
The unit $7\alpha_1-18$ has characters $(0,2,1,0)$ and supplies
an explicit nonzero element in it at every height.
Both its local arithmetic character and E.65's normalized finite
character have the exact local norm group as kernel. They differ
by a nonzero scalar; evaluating the included $\varepsilon$ gives
the scalar $c_d$ stated above and proves its denominator nonzero.
For example the actual first pure unit norm row is
$(0,3,0,0)$, while the next wild character on those four source
units is $(0,2,0,0)$, as recomputed in the certificate.

\emph{Completed principal divisors and coherent lifts.}
For each finite field $F_d$ the ordinary principal-divisor sequence,
completed for multiplication by powers of three, is
\[
 0\longrightarrow\widehat{\mathcal O_{F_d}^{\times}}_3
  \longrightarrow\widehat{F_d^\times}_3
  \longrightarrow
     \mathcal R(\{\text{finite primes of }F_d\})
  \longrightarrow0 .
 \tag{E110.22}
\]
Here the last group is the multiplication completion of the free
divisor group. To check exactness, the finite class group has no
three-primary part, so its order is a unit in $\mathbb Z_3$.
If a prime ideal has class order $h$, choose
$(a)=\mathfrak p^h$ and take the completed element $a^{1/h}$.
These elements split the completed divisor map by convergent
restricted products. The kernel is exactly the completed unit
group: the unit subgroup has its induced power filtration because
a power root of a unit has zero valuations. This proves (E110.22)
without compactness of the divisor group.

The prime-chain calculation of E.72 gives the inverse limit of
the last groups in (E110.22). Away from three and seventeen,
the action on compatible radical roots is the actual affine
Frobenius
$x\mapsto px+\kappa_3(17)(\operatorname{Frob}_p)$.
Its unique integral fixed point exists precisely for $p\in P_0$.
It gives one degree-one prime chain. On every other orbit the
three-parts of the finite orbit lengths grow without bound;
an invariant $\mathbb Z_3$-valued measure then has all its masses
divisible by arbitrarily high powers of three and is zero.
This is the actual divisor norm calculation, with residue degrees
as its transition coefficients. At three there are the two
degree-one chains from (E110.13), and at seventeen the single
totally ramified degree-one chain. This proves that the inverse
limit of divisor modules is exactly the quotient in (E110.4).

For any compatible completed divisor sequence, its preimage at
each finite level is a nonempty torsor under a compact completed
unit group, by (E110.22).
Consider the product of these compact torsors. Each adjacent norm
equation is closed. Every finite set of these equations is soluble:
choose an arbitrary preimage at its highest level and norm it
down. The resulting divisors are the specified lower divisors
by compatibility. Compactness and the finite intersection property
therefore give an entire compatible multiplicative sequence.
This proves surjectivity in (E110.4).
In particular the coherent generators used in (E110.6) exist.
For a restricted family $(t_p)$, the product in (E110.6) converges
at every positional level modulo every $3^m$ because all but
finitely many exponents lie in $3^m\mathbb Z_3$.
This proves its convergence uniformly in each multiplication
quotient and proves continuity in the topology (E110.2).
Valuations and the displayed inverse are continuous as well.
All residue degrees in these surviving chains are one, proving
the literal norm formula (E110.5).
The ambiguity of the chosen generators also has an explicit map.
If $s_F'$ is a second such splitting, put
$u(D)=s_F'(D)s_F(D)^{-1}\in\mathcal J_F$.
It is the convergent product of the ratios of the chosen
generators with the exponents in $D$. The two coordinate systems
are related by $(k,D)\mapsto(k\,u(D)^{-1},D)$.
The inverse uses $u(D)$, so this is a continuous isomorphism
over the unchanged actual divisor map.

\emph{The entire compact unit kernel.}
The group $\mathcal J_F$ is compact, metrizable and torsion-free:
it is a closed subgroup of the countable product of the finite-free
compact modules
$\widehat{\mathcal O_{F_d}^{\times}}_3\simeq
\mathbb Z_3^{r_d}$, $r_d=(3^d-1)/2$.
Its character group is countable, and is the direct limit
of the finite-level character groups
$(\mathbb Q_3/\mathbb Z_3)^{r_d}$ under the transposes of the
actual norm matrices. To see this equality directly, a continuous
finite-valued character of the inverse limit factors through a
finite positional quotient. Extend that character from the image
subgroup to the finite abelian quotient of the entire level,
using the divisibility of $\mathbb Q_3/\mathbb Z_3$.
Two such finite-level characters agree on the inverse limit
precisely when they agree after a sufficiently high pullback:
their finite images form a descending finite system.
This proves the asserted direct-limit comparison and the finite
meaning of every character in (E110.7).

The character group is divisible. Equivalently, a character
$\chi$ on $\mathcal J_F$ defines a character on $3\mathcal J_F$
by $3x\mapsto\chi(x)$; this is well-defined and continuous by
torsion-freeness and compactness. It extends to $\mathcal J_F$
by first passing to a finite quotient and extending there.
The extension is a three-division of $\chi$.
Choose a basis of its elements killed by three and successive
divisions. The resulting direct sum of copies of
$\mathbb Q_3/\mathbb Z_3$ is the whole character group:
for an element of order $3^n$, subtract an appropriate combination
of the chosen $n$th divisions so that its order drops, and induct.
This also proves independence by multiplying any finite relation
by a suitable power of three.
The finite equations in (E110.7) are therefore jointly onto
every finite product of cyclic groups. Otherwise a nonzero
character of that finite product would give a relation among
the chosen characters. Compactness gives their simultaneous
inverse for every full tuple, and characters separate points.
Thus (E110.7) is a topological isomorphism onto a product of
copies of $\mathbb Z_3$.

There are countably infinitely many factors. Here is an
unconditional rank argument specifying the comparison theorem
that is needed. For base $F_d$, the full extension
\[
       \mathcal F=F_d(\mu_{3^\infty},
                            \alpha_d^{1/3^\infty})
                =\mathbb Q(\mu_{3^\infty},17^{1/3^\infty})
 \tag{E110.23}
\]
contains every higher pure field. Kato's Theorem1.1(1) identifies
the coherent universal three-unit norms from this full extension
as a finite-index subgroup of the coherent cyclotomic
universal norms at $F_d$.
The rank calculation in his Section3.2, proved there from
the torsion cyclotomic Iwasawa module and the invariant/kernel
calculation, gives rank
$(r_d+2)-(2-1)=r_d+1$ for that subgroup.
This use is Theorem1.1(1), which allows the two places over three;
the exact coherent definition and the proofs in Sections2,
4 and5 have been opened and checked
\cite[Theorem1.1(1), Section3.2, Proposition4.2,
and Sections5.4--5.5]{E_KatoUniversalNorms}.
Restrict a coherent system to the actual fields $F_n$, $n\ge d$,
and norm down for lower indices.
Intersecting its image at $F_d$ with the kernels of its two
three-valuations leaves rank at least $r_d-1$.
Since these two prime chains never split above $F_d$ and every
residue-degree norm is one, zero valuations at that level force
zero valuations at every higher pure level.
The restricted system is consequently an ordinary-unit system.
Thus the actual projection of $\mathcal J_F$ to level $d$
has rank at least $r_d-1$, which is unbounded.
The product in (E110.7) has infinitely many factors, and
countability was already proved. This argument establishes the
full compact product and its actual character maps; it needs no
identification of a finite projection with a single observed
unit norm image.

\emph{The combined positional system and every toric fiber.}
E.46 identifies the fixed-first section classes with pairs of
pure and complex norm systems whose combined rational norm is
a cube. Its scaled toric map takes the cube root of that norm
in $\widehat{\mathbb Q^\times}_3$.
E.107 gives, with its specified phase normalization,
\[
 \begin{split}
 x_L&=\beta^b e_L^z k_Ls_L^*(t),\\
 N(x_L)&=17^{2b}
          3^{\,3z-\sum_{p\in P_1}\ell_pt_p/3}
                                      \prod_{p\in P_1}p^{t_p}.
 \end{split}
 \tag{E110.24}
\]
Its divisor parameters satisfy the two mod-three class equations
of E.88; these are automatically satisfied by $t=3r$.
The two surviving prime sets $P_0,P_1$ are disjoint by their
definitions and by the actual divisor calculation.
Therefore a cube combined norm forces the off-$S$ pure and
complex exponents separately to be divisible by three.
It also permits no rational-prime coordinate outside their union.
This proves necessity of (E110.8).

Conversely take any target there. The sum
$\sum\ell_pr_p$ converges in $\mathbb Z_3$ because the coefficients
are bounded and $r$ is restricted.
Insert (E110.10) into (E110.5) and (E110.24).
The seventeen exponent is $e+2b=3B_{17}$, the three exponent is
$B+C+3z-\sum\ell_pr_p=3B_3$, and every other exponent is
$3r_p$. Thus the combined rational norm is exactly the cube of
the prescribed second Kummer class.
Every pair gives an actual section through the proven
Kummer--Shapiro map. Conversely the complex coordinates are
unique by E.107, the pure divisor coordinates are unique by
(E110.4), and the two displayed rational norm equations determine
$e,C$ from $b,z,B$ and the target. Finally (E110.6) determines
$k_F$ uniquely. This proves bijectivity, the inverse formulas
and all the fiber assertions.
The maps are continuous: this follows from the previously proved
restricted product continuity, the continuous compact unit
coordinates, and the continuous phase sum.
The same statements give continuity of the inverse.
The explicit seven-prime comparison (E110.12) follows from the
retained literal value $\ell_7=8$.
For the final unit-multiple comparison, substitution $T\mapsto T^r$
is an automorphism of the completed group ring and preserves
augmentation. In the actual law
$(a,v)(b,w)=(a+b,v+T^aw)$ it gives
$v(T^r)+T^{ra}w(T^r)$, which proves the homomorphism assertion
for $\Phi_r$. It commutes with the arithmetic action
$(a,v)\mapsto(\chi a,\chi v(T^\chi))$.
It therefore gives the stated bijection on sections and their
geometric conjugacies, and on the toric map it is
$(a/3,\operatorname{aug}(v)/3)\mapsto
(ra/3,\operatorname{aug}(v)/3)$.

\emph{Executed certificate.}
The retained small PARI source supplies its literal primitive
element, field maps, all three units, unconditional certification
with default flag zero and return value one, and every prime
over three and seventeen. The self-contained Python certificate
independently recomputes the characteristic-zero multiplication
matrices, the finite wild determinant norms, the four-character
matrix and its inverse on all twenty-seven elements, the actual
conjugation matrix and its fixed line, and all mixed-unit products.
It retains the genuine first pure unit norm and next-character
rows. It also checks compatible degree-one radical roots at
every eligible prime below one thousand and the literal
full positional inverse on all retained finite test inputs,
including all three values of the complex phase modulo three.
The code keeps the three-primary class induction and the compact
inverse-limit proof as the exact arguments above; its finite
checks supply their arithmetic inputs and normalization checks.
\end{proof}
