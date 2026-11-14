\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}\usepackage{lmodern}
\usepackage[a4paper,margin=27mm,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,graphicx}
\usepackage{xcolor,microtype,hyperref}
\setlength{\parindent}{1.3em}\setlength{\parskip}{.22em}
\setlength{\emergencystretch}{2em}\setcounter{secnumdepth}{0}
\allowdisplaybreaks[2]
\newenvironment{statement}[3]{\par\addvspace{1.1em}\noindent
\textbf{#1. #3}\quad\textsf{\small[#2]}\par\nobreak\smallskip\ignorespaces}
{\par\smallskip}
\begin{document}
\subsection{All vertical class actions in the lower fifty-three tower}

\begin{statement}{E.122}{Proved}{The stable positional fifty-three class tower and its actual unit-norm maps}
Keep the literal roots and fields of E.119 and E.121:
\[
 \zeta=\zeta_3,\quad \xi=\zeta_9,\quad
 \beta_d^{3^d}=53\zeta,\quad\beta_{d+1}^3=\beta_d,
 \quad B_d=\mathbb Q(\xi,\beta_d),\quad
 A_d=\operatorname{Cl}_S(B_d)\{3\},\quad S\mid\{3,53\}.
 \tag{E122.1}
\]
There are exactly three primes over three and three over fifty-three
in every $B_d$, $d\ge1$. Each vertical step is totally ramified
at all six of them and unramified elsewhere. For every $d\ge1$,
the actual vertical automorphism
$\sigma_d(\beta_{d+1})=\zeta\beta_{d+1}$, fixing $\xi$,
acts identically on the entire group $A_{d+1}$.
The actual ideal norms are onto and satisfy
\[
 N_d:A_{d+1}\twoheadrightarrow A_d,
 \qquad j_dN_d=3\operatorname{id}_{A_{d+1}},\qquad
 N_dj_d=3\operatorname{id}_{A_d}.
 \tag{E122.2}
\]
For $d\ge2$ let $g_d(\beta_{d+1})=\xi\beta_{d+1}$,
$g_d(\xi)=\xi$. This has order nine, fixes $B_{d-1}$,
has cube $\sigma_d$, and restricts to $\sigma_{d-1}$ on $B_d$.
Its entire class action satisfies
\[
       (g_d-1)^2A_{d+1}=0,
       \qquad 3(g_d-1)A_{d+1}=0.
 \tag{E122.3}
\]

Here are explicit local coordinates for every norm kernel in (E122.2).
Order the six places by the three coherent branches at three,
then the three fixed E.119 places at fifty-three. Put
$U_d=\mathcal O_{B_d,S}^{\times}$ and let
\[
 \chi_d:U_d\longrightarrow\mathbb F_3^6,
 \qquad
 u\longmapsto
 \bigl(\log_\zeta\bigl(\operatorname{Art}_v(u)
          (\beta_{d+1})/\beta_{d+1}\bigr)\bigr)_{v\in S}.
 \tag{E122.4}
\]
The positive arithmetic Artin convention and the radical in this
formula specify every sign. The actual local decomposition maps induce
\[
 \ker N_d\ \xleftarrow{\ \sim\ }\ 
 \ker\bigl(\textstyle\sum:\mathbb F_3^6\to\mathbb F_3\bigr)
             /\chi_d(U_d).
 \tag{E122.5}
\]
The restriction of $\chi_d$ to the included $U_1$ is exactly
$\chi_1$ and has rank two. Thus every kernel in (E122.2)
is an elementary three-group of rank at most three.
Equation (E122.5) retains the actual higher unit-character subgroup;
it does not assign that subgroup the value of its included rank-two
part.
More precisely, put $K_d=\ker N_d$. The literal ideal extensions
satisfy $K_d=j_dK_{d-1}$ for every $d\ge2$.
Consequently $K_d\subset3A_{d+1}$, and every actual norm induces
an isomorphism $A_{d+1}/3A_{d+1}\to A_d/3A_d$ for $d\ge2$.
These four-dimensional vector spaces all have the dimension computed
in E.121. The inverse class module and its exact filtration are
described in (E122.20)--(E122.21).
The explicit upper units in (E122.22) evaluate the first remaining
kernel: $K_2=0$. Hence every $K_d$, $d\ge2$, is zero. Put
$n_2=\operatorname{id}_{A_2}$ and, for $d>2$,
$n_d=N_2\cdots N_{d-1}:A_d\to A_2$. These are actual isomorphisms
and give
\[
 \begin{gathered}
 A_d\xrightarrow[\ n_d\ ]{\sim}C_9\oplus C_3^3\quad(d\ge2),
 \qquad n_dN_d=n_{d+1},\qquad n_{d+1}j_d=3n_d,\\
 \varprojlim_{d,N_d}A_d\xrightarrow[\mathrm{pr}_2\ ]{\sim}A_2,
 \qquad j_d=3N_d^{-1}\quad(d\ge2).
 \end{gathered}
 \tag{E122.22a}
\]
Here $N_d^{-1}$ is the inverse of the proved isomorphism, and all
coordinate maps and their compositions are specified. The actual
$g_d$ action is the identity for $d\ge2$. The horizontal action
fixing $\beta_d$ and sending $\xi$ to $\xi^4$ is E.121's matrix H
in the coordinates $n_d$.

The next longer cyclic extension $B_3/B_1$ is evaluated explicitly.
Its generator is $g_2$, and its degree is nine. The maximal subfield
of the $S$-Hilbert three-class field of $B_3$ that is abelian over
$B_1$ has group
\[
 \Gamma_9=C_9^2\oplus C_3^3,\qquad
 \ker\{\Gamma_9\longrightarrow\langle g_2\rangle\}
       =(A_3)_{g_2}=C_9\oplus C_3^3.
 \tag{E122.6}
\]
The complete nine-coordinate relation lattice, its Smith maps and
inverse maps are given in the certificate. In their four nontrivial
Smith coordinates, the literal norm to the full group in E.121 is
\[
 \begin{gathered}
 \overline N_2:(A_3)_{g_2}\xrightarrow{\sim}A_2,
       \qquad (x_0,x_1,x_2,x_3)\longmapsto(x_0,x_1,x_2,x_3),\\
 \overline j_2=3I_4,\qquad
 \ker N_2=(g_2-1)A_3.
 \end{gathered}
 \tag{E122.7}
\]
The first coordinate has modulus nine and the other three have modulus
three. The horizontal automorphism fixing $\beta_3$ and sending
$\xi$ to $\xi^4$ acts on this quotient by exactly E.121's matrix $H$,
transported by the displayed norm isomorphism. The subgroup on the
right of (E122.7) vanishes by the literal unit witnesses below.
The computation of this quotient is retained with its actual
comparison map as an independent finite check.
These are literal root-cubing and ideal-norm maps for the $j=1$
positional factor of E.46. The full embedded first unit-norm subgroup
is evaluated by (E122.23), and every later finite unit-norm defect
and completed kernel is evaluated by (E122.25). The actual higher
Hilbert90 maps specify their embedded subgroups. The maps from these
positional norm systems to the intrinsic section groups remain the
separate maps of E.46 and E.23.
The manuscript anchor is \S51.16, fols.~733v--736v, scans172--178,
through the exact root and Kummer--Shapiro comparisons of E.46.
\end{statement}

\begin{proof}
\emph{Six coherent places and their actual uniformizers.}
Let $a_0$ be the rational three-adic cube root of fifty-three
congruent to $-1$ modulo nine. Since $53=-1+54$, the logarithm
on $1+3\mathbb Z_3$ gives
$v_3(a_0+1)=2$. The three embeddings of $B_1$ over
$\mathbb Q_3(\xi)$ send
$\alpha=53^{1/3}$ to $a_0\zeta^j$, $j=0,1,2$, and hence send
$\beta_1$ to $a_0\xi^{1+3j}$. Normalize the valuation of
$F_3=\mathbb Q_3(\xi)$ by $v(1-\xi)=1$, so $v(3)=6$.
For $k=1,4,7$,
\[
       a_0\xi^k+1=(1-\xi^k)+(a_0+1)\xi^k,
       \qquad v(1-\xi^k)=1,\quad v(a_0+1)=12.
 \tag{E122.8}
\]
Thus $\beta_1+1$ is a uniformizer at each labeled place.
Whenever $\beta_d+1$ is a uniformizer, the polynomial
\[
       (Y-1)^3-\beta_d
       =Y^3-3Y^2+3Y-(\beta_d+1)
 \tag{E122.9}
\]
is Eisenstein there. It defines the unique next prime, with unchanged
residue field, and $\beta_{d+1}+1$ is its uniformizer. At each
fifty-three prime, $\beta_1$ has valuation one and
$X^3-\beta_d$ gives the same Eisenstein induction, with uniformizer
$\beta_{d+1}$. The initial number and residue degrees of these places
are E.119's literal splitting calculation. The defining polynomial
discriminants have support only at three and fifty-three. This proves
all the asserted local degrees, uniqueness of primes in each vertical
chain, and the absence of other ramification.

\emph{The class-field kernel with its decomposition generators.}
Write $D=B_d$, $E=B_{d+1}$ and let $H_E^S$ be the maximal abelian
three-extension of $E$ unramified everywhere and split at every place
of S. It is invariant under every automorphism of $E$ preserving S.
Put $\mathcal G=\operatorname{Gal}(H_E^S/D)$ and
$\Gamma=\mathcal G^{\rm ab}$. The actual ideal Artin maps identify
$A_E$ with $\operatorname{Gal}(H_E^S/E)$, and give
\[
 0\longrightarrow A_E/(\sigma_d-1)A_E
   \longrightarrow\Gamma\longrightarrow C_3\longrightarrow0.
 \tag{E122.10}
\]
Indeed $A_E$ is abelian, the quotient is cyclic, and the commutator
subgroup is exactly $(\sigma_d-1)A_E$. A decomposition group at any
S-place gives a section of the last map: its restriction to $E/D$
is an isomorphism, because $E/D$ is totally ramified and the place
splits in $H_E^S/E$.

There are two class-field inclusions to retain. Base change gives
$H_D^S E\subset H_E^S$, with the prescribed splitting at S.
Moreover $E\cap H_D^S=D$, since a nontrivial subextension of the
cyclic cubic $E/D$ is ramified at S. Restriction consequently gives
the actual onto ideal norm $A_E\to A_D$. The largest subfield of
$H_E^S$ that is abelian over D, unramified everywhere and split at S
is exactly $H_D^S$. Thus
\[
 0\longrightarrow I\longrightarrow\Gamma
       \longrightarrow A_D\longrightarrow0,
 \qquad
 I=\langle\text{the six S-decomposition images}\rangle.
 \tag{E122.11}
\]
These statements use the literal Frobenius norm square and the
trivial-modulus class-field correspondence
\cite[V,Proposition3.3, Theorem3.6 and Example3.9]{E_MilneCFT}.
The kernel description follows by killing these decomposition
groups: outside S the field is already unramified, and killing
the S-groups makes every S-prime split. Conversely $H_D^S$ is
contained by the first inclusion. Each generating group is cyclic
of order three and injects into $\operatorname{Gal}(E/D)$.

\emph{The all-level normalizer induction.}
The base case $A_2^{\sigma_1}=A_2$ is E.121's full class theorem.
For $d\ge2$, use the actual $g=g_d$ in the statement. Its restriction
to D is the preceding vertical automorphism, so it acts identically
on $A_D$ by induction. It fixes each S-prime of D, since the preceding
vertical step has a unique prime above each one. It also commutes
with $\sigma_d$. Consequently its action on every decomposition
image in (E122.11) is the identity: restriction embeds that image
into $\langle\sigma_d\rangle$, on which conjugation by $g$ is
the identity. Choice of a lift of $g$ to $H_E^S$ changes its action
on $\Gamma$ by an inner automorphism, hence does not change it.
For $T=g-1$ these actual comparisons give
\[
          T\Gamma\subset I,\qquad TI=0,\qquad T^2\Gamma=0.
 \tag{E122.12}
\]

On the entire still unknown finite group $A=A_E$, put
$s=g^3-1$ and $M=sA$. From (E122.10)--(E122.12) one has
$T^2A\subset M$. Actual norm of an ideal followed by extension is
the product of its conjugates, so
$jN=1+\sigma_d+\sigma_d^2=3+3s+s^2$ on A.
Because $g$ acts trivially on $A_D$, $TjN=0$. It follows that
\[
       3TA=-T(3+s)M,\qquad
       M=(3T+3T^2+T^3)A\subset(3,T)M.
 \tag{E122.13}
\]
For $3^eA=0$, the exact relation $(1+T)^9=1$ gives
$T^9\in3\mathbb Z_3[g]$. Every monomial $3^aT^b$ of total degree
$9e$ is therefore divisible by at least $3^{a+\lfloor b/9\rfloor}$,
and $a+\lfloor b/9\rfloor\ge e$. Hence $(3,T)^{9e}A=0$.
Iteration of (E122.13) proves $M=0$. This proves the entire vertical
action, not only its coinvariants. Now (E122.12) gives $T^2A=0$,
and $g^3=1$ on A gives $3T=0$. The ideal identities yield (E122.2).

\emph{Every remaining kernel as an actual unit-character quotient.}
The product of local reciprocity maps identifies the subgroup I in
(E122.11) with $\mathbb F_3^6/\chi_d(U_d)$: the local norm subgroup
is killed at S, local units are killed outside S, and the kernel
among S-ideles is precisely the diagonal S-unit image. This is the
idele sequence with its explicit local maps
\cite[V,Proposition5.2 and Theorems5.3 and5.5]{E_MilneCFT}.
Restriction to $E/D$ sends each positive local generator to
$\sigma_d$, and so is the sum of the six coordinates.
The global product formula puts $\chi_d(U_d)$ in its kernel.
Intersecting (E122.10) and (E122.11), now with $sA=0$, proves
(E122.5) and its stated inverse: form the corresponding product
of actual local Artin elements and read its class in $A_E$.

For $u\in U_1$ the local corestriction projection formula gives
\[
 \operatorname{Cor}\bigl([\beta_d]\cup\operatorname{Res}[u]\bigr)
     =[N_{B_{d,v}/B_{1,v_1}}\beta_d]\cup[u]
     =[\beta_1]\cup[u].
 \tag{E122.14}
\]
The norm is exactly $\beta_1$, from the odd-degree binomial minimal
polynomial and the Eisenstein local degree. The local invariant
composed with corestriction is the lower invariant, so there is
no factor of the local degree. This is the proved cup-product
Res/Cor compatibility of
\cite[III,Theorem3.1 and its proof]{E_MilneCFT}; it also follows
after taking a finite normal closure when the longer local extension
is not Galois. The fixed $\mu_3$ is transported by its literal
inclusion. Thus (E122.14) is exactly $\chi_d(u)=\chi_1(u)$.
E.119's complete rank-two matrix proves the bound in (E122.5).

\emph{Complete local ninth-norm characters at the next stage.}
Here $B_3/B_1$ is cyclic of degree nine, generated by $g_2$.
At a labeled three-prime it is
$F_3(\theta)/F_3$ with
$\theta^9=a_0\xi^{1+3j}$; $\theta+1$ is an Eisenstein
uniformizer. Let $\lambda=1-\xi$. The logarithm and exponential
show $1+\lambda^{16}\mathcal O_{F_3}\subset(F_3^\times)^9$:
division by nine lowers the $\lambda$-valuation by twelve and
leaves valuation at least four, in their inverse range.
The finite unit quotient modulo ninth powers therefore has seven
cyclic factors of order nine. The exact residue-ring generators used
by the program, in order, are
\[
 \begin{gathered}
 1+\xi,\quad-\xi-3\xi^2-3\xi^3-\xi^4,\quad3+\xi^3,\\
 -1+2\xi^2+2\xi^3+\xi^5,\quad-2\xi^2-2\xi^3-\xi^5,\quad
 1+3\xi,\quad2+2\xi+2\xi^3+\xi^4.
 \end{gathered}
 \tag{E122.15}
\]
Their exact residue-group orders and discrete-log inverse are
computed in $\mathcal O_{\mathbb Q(\xi)}/\lambda^{16}$, with
the official \texttt{idealstar}/\texttt{ideallog} maps
\cite[those function contracts]{E_PARICertifiedUnits}.

For each of the fifty-five indices
$1\le i\le80$, $3\nmid i$, and $i=81$, compute the literal norm
\[
 n_{j,i}=\operatorname{Res}_X
       \bigl((X-1)^9-a_0\xi^{1+3j},1+X^i\bigr).
 \tag{E122.16}
\]
These are norms of actual local units. The certificate proves that
their images generate a subgroup of index exactly nine in the
finite unit quotient. The local norm-index theorem proves that
the complete norm subgroup also has index nine, since this is a
totally ramified cyclic extension of degree nine. Inclusion and
the identical index prove equality; no completeness assertion about
the fifty-five upper units is required.
In the coordinates (E122.15) the three positive character rows are
\[
 \begin{pmatrix}
 3&6&7&3&0&3&0\\
 3&6&1&3&0&3&0\\
 3&6&4&3&0&3&0
 \end{pmatrix}\quad\bmod9.
 \tag{E122.17}
\]
The sign and generator are calibrated by the actual unit four.
For the rational factors $a_0,4$, naturality under complex conjugation
fixes both arguments and inverts $\mu_9$, so their odd-order Hilbert
symbol is one. On the radical of $\xi$, arithmetic local reciprocity
acts on $\zeta_{81}$ by the inverse of $N_{F_3/\mathbb Q_3}(4)=4^6$.
Since $4^{-6}=37\pmod{81}$, the resulting exponent is four
modulo nine. Thus the values on four are $4(1+3j)$, namely
$4,7,1$. These unit values specify each row uniquely.

The program uses an integer approximation to $a_0$ whose cubing
error has valuation at least twenty-four. Its ratio to the exact
$a_0$ is a ninth power by the same logarithmic calculation.
Multiplying $\theta$ by that literal local ninth root identifies
the approximate and exact Kummer fields and preserves the chosen
generator. When evaluating a lower global element, the recorded
coefficient and divisor bounds prove that its approximate normalized
local unit differs from the exact one by $1+\lambda^{109}\mathcal O$
or better. Thus all displayed characters are exact, not inferred
from agreement of two finite precisions.

At fifty-three normalize an element by its valuation power of
$\beta_1$. Its positive character is the negative logarithm to
the residue of $\xi$ of the normalized residue raised to
$(53^2-1)/9$. The full six-by-fifteen matrix on the actual complete
E.119 S-unit basis, each class-power principal correction, and each
S-prime principal correction is retained. Every column satisfies
the ninth product formula and reduces to the exact old cubic
column. The three outside-S class generators have ninth Frobenius
coordinates $(2,1,6)$. Consequently the field restriction row on
the nine-coordinate genus presentation is
\[
                  (1,1,1,1,1,1,2,1,6)\pmod9.
 \tag{E122.18}
\]
The relation HNF, with all forward and inverse Smith maps, is
computed from these actual principal ideals. Its full group has
orders $(9,9,3,3,3)$ and its restriction kernel has orders
$(9,3,3,3)$. The kernel is $(A_3)_{g_2}$ by the same actual
class-field argument as (E122.10), now of degree nine. This proves
(E122.6).

\emph{Literal reduction to the preceding genus field.}
The inclusion $H_{B_2}^S B_3\subset H_{B_3}^S$ is the actual base
change above. E.121 proves that $H_{B_2}^S/B_1$ is already abelian.
On the six local coordinates, restricting the ninth radical to
its cube is reduction modulo three; on the three fixed ideal
Frobenius coordinates it retains the same ideal. The ambient
nine-coordinate map is therefore the identity. The certificate
checks inclusion of the complete new relation lattice in the old
one, then transports this map through both restriction-kernel
lattices and Smith bases. Its four nontrivial coordinates are
literally $I_4$. All 243 elements and both finite inverse compositions
are independently checked. Naturality gives the stated horizontal
matrix, and the actual trace $j_2N_2=3$ gives $\overline j_2=3I_4$.
Since the induced norm on $g_2$-coinvariants is injective, its full
kernel is exactly $(g_2-1)A_3$, proving (E122.7).

\emph{The actual recursion of norm kernels.}
Fix $d\ge2$, $E=B_{d+1}$, $D=B_d$, and $D_0=B_{d-1}$.
The full field $H_E^S$ is Galois over $D_0$, because the cyclic-nine
extension $E/D_0$ preserves S. At each of its six S-places choose
the unique element $\gamma_i$ of the actual local decomposition
group that restricts to $g_d$ on E. That decomposition group is
cyclic of order nine, since the place splits over E. Fix one as
$\gamma_0$ and write $\gamma_i=\gamma_0a_i$ with $a_i\in A_E$.
Conjugation by $\gamma_0$ is the actual $g_d$ action. By (E122.3),
$1+g_d+g_d^2=3$ on $A_E$. The group law therefore gives
\[
 \gamma_i^3\gamma_0^{-3}=3a_i=j_dN_d(a_i),
 \qquad K_d=j_dK_{d-1}\subset3A_{d+1}.
 \tag{E122.19}
\]
Here is the exact restriction comparison giving the second equality.
The cubes $\gamma_i^3$ are the positive S-decomposition generators
in $\operatorname{Gal}(H_E^S/D)$; their differences from the
reference generate $K_d$ by (E122.5). Restriction through
$H_D^S\subset H_E^S$ sends $\gamma_i$ to the positive lower
decomposition generator in $\operatorname{Gal}(H_D^S/D_0)$.
Their differences are $N_d(a_i)$ by the ideal Frobenius norm square,
and generate $K_{d-1}$. Thus (E122.19) is equality of actual
subgroups, not only an order comparison. Changing a prolongation
conjugates $\gamma_i$ by an element of $A_E$ and changes $a_i$
by a value of $g_d-1$; its triple is zero by (E122.3).
Changing the reference replaces all differences by differences
from another generator and leaves both generated subgroups unchanged.
This records the choice ambiguity in the literal local maps.
The inclusion in (E122.19) and surjectivity of $N_d$ imply the
stated mod-three isomorphisms. The ranks of the elementary groups
$K_d$ are nonincreasing from the rank-three group $K_1$ of E.121.

\emph{An exact finite-rank inverse class module.}
Let $\mathcal A=\varprojlim_{d,N_d}A_d$, and put
$\mathcal B_d=\ker(\mathcal A\to A_d)$.
Every projection is onto, by compactness and the onto finite norms.
The actual kernel recursion gives
\[
 \mathcal B_{d+1}=3\mathcal B_d\quad(d\ge2),
 \qquad
 A_d=\mathcal A/3^{d-2}\mathcal B_2\quad(d\ge2),
 \qquad\mathcal B_2/3\mathcal B_2=K_2.
 \tag{E122.20}
\]
To check all limit steps, for $e>d$ put
$M_{e,d}=\ker(A_e\to A_d)$. The restricted top norm maps
$M_{e,d}$ onto $M_{e-1,d}$. Thus
$3M_{e,d}=j_{e-1}M_{e-1,d}$, by the actual trace identity.
Induction proves $3M_{e,d}=M_{e,d+1}$: its top norm image is
$M_{e-1,d+1}$ by the preceding induction step, and it contains
the entire top kernel $j_{e-1}K_{e-2}=K_{e-1}$ by (E122.19).
The initial case $e=d+1$ has both sides zero.
For any prescribed element of $\mathcal B_{d+1}$, the finite
sets of solutions of $3x=y$ in these compatible finite kernels
give nonempty closed subsets of the compact group $\mathcal B_d$.
Any finite intersection is nonempty by working at the largest level.
Compactness proves (E122.20) with no omitted inverse-limit term.

The group $\mathcal B_2$ is generated as a compact
$\mathbb Z_3$-module by at most three elements. Explicitly choose
lifts of a basis of $\mathcal B_2/3\mathcal B_2=K_2$; successive
reduction modulo $3^n\mathcal B_2$ writes every element as a
convergent $\mathbb Z_3$-linear combination of those lifts.
For each finite quotient the remainder tends to zero, since that
quotient has finite three-power exponent. This is the required
topological Nakayama argument. Since $\mathcal B_2$ has finite
index in $\mathcal A$, the actual limit satisfies
\[
 \mathcal A\text{ is a finitely generated }\mathbb Z_3\text{-module},
 \quad\operatorname{rank}_{\mathbb Z_3}\mathcal A\le3,
 \quad\mathcal A/3\mathcal A\simeq A_2/3A_2\simeq\mathbb F_3^4.
 \tag{E122.21}
\]
The last map is the actual projection: inverse limits of the finite
multiplication-by-three sequences are exact, and their mod-three
transition maps are the isomorphisms already proved. Neither the
rank nor the torsion exponents of this embedded limit module are
assigned by (E122.21). Equation (E122.20) retains its literal
finite-index submodule, rather than replacing it by an unspecified
isomorphism type.

\emph{Literal upper units that evaluate the remaining kernel.}
The compact witness file uses the exact relative field
$\mathbb Q[b,z]/(z^6+z^3+1,b^9-53z^3)$, with
$b=\beta_2$, $z=\xi$ and lower primitive element
$z-b^3/z$. The relative binomial is irreducible by the
fifty-three Eisenstein valuation. The file gives all rational
coefficients in the ordered basis $b^iz^j$, $0\le i<9$, $0\le j<6$.
It also gives ten literal elements of $\mathbb Q(b)$ and twenty-two
elements $v_1,\ldots,v_{22}$ of $B_2$. Each of the former has its
entire principal divisor verified to have support only at three
and fifty-three. Include the fifteen certified lower S-units and
the three $g_1$-conjugates of each of these ten elements, giving
forty-five actual S-units $w_i$ of $B_2$. Here $g_1$ denotes the
literal automorphism $b\mapsto\xi b$, $\xi\mapsto\xi$ of
$B_2/\mathbb Q(\xi)$; its cube is $\sigma_1$.
For every $v_k$ the certificate verifies the literal identity
$v_k^3=\prod_{i=1}^{45}w_i^{a_{ki}}$, with every integer $a_{ki}$
displayed. In particular every $v_k$ is an S-unit: outside S its
valuation is one third of a zero valuation. A separate rational
relative-ring program rechecks all twenty-two identities by
cross-multiplication, without a number-field library or a root search.

The same two programs verify every relative norm
$v_k\sigma_1(v_k)\sigma_1^2(v_k)$, its exact expression in the
complete lower S-unit basis, and its sign. The actual local norm
square sends the action on $\beta_3$ over $B_2$ to its action over
$B_1$. With $\zeta=\xi^3$, it therefore gives exactly
$\chi_9(N_1v_k)=3\chi_2(v_k)$, with the threefold map
$\mathbb F_3\to\mathbb Z/9$ specified by these roots.
Applying the already calibrated rows (E122.17) and the exact tame
residue formula proves all six characters of every witness. The
minimum proved approximation bound is $1+\lambda^{111}\mathcal O$.
For lower units $u_8,u_{10}$ in the fixed fifteen-column order and
the three roots $v_8,v_{14},v_{20}$ the actual character matrix is
\[
 \bigl(\chi_2(u_8),\chi_2(u_{10}),
        \chi_2(v_8),\chi_2(v_{14}),\chi_2(v_{20})\bigr)
 =\begin{pmatrix}
 0&1&2&0&2\\0&1&0&1&2\\0&1&1&2&1\\
 2&0&0&0&2\\2&0&1&0&1\\2&0&2&0&1
 \end{pmatrix}\pmod3.
 \tag{E122.22}
\]
Every column has sum zero and the first five rows have determinant
$-4$. Thus $\chi_2(U_2)$ is the entire product-formula hyperplane.
Equation (E122.5) proves $K_2=0$, and (E122.19) proves $K_d=0$
for every $d\ge2$. This proves all isomorphisms (E122.22a), including
their displayed inverses and compositions. Norm equivariance shows
that $g_d$ acts identically and that the horizontal matrix is H at
every level. It also evaluates the earlier inverse filtration:
$\mathcal B_2=0$ and $\mathcal A=A_2$ through the actual projection.
The preliminary finite-prime residue rank and the smaller-field
candidate lattice are retained as discovery records. Only the
literal cube, divisor, norm and positive-character identities enter
this conclusion; no completeness claim about an upper unit basis
or an upper BNF is used.

\emph{The full embedded first unit-norm subgroup and an inverse.}
The actual fifteen-column basis identifies $\widehat U_1$ with
$\mathbb Z_3^{15}/\mathbb Z_3(9,0,\ldots,0)$, the first column
being the literal root $\xi$. The index-nine inverse-image lattice
of $\ker\chi_1$ consists exactly of the lower S-units that are
field norms from $B_2$, by the cyclic Hasse norm theorem. E.121's
literal Hilbert90 divisor map identifies the quotient of those
field-norm units by actual S-unit norms with $A_2/j_1A_1=C_3^4$.
Thus the complete unit-norm subgroup has index $3^6$ in $\widehat U_1$.

Write $c_k\in\mathbb Z^{15}$ for the displayed norm-coordinate
column of $v_k$, and $s_k\in\{1,-1\}$ for its displayed sign, so
$N_1v_k=s_k\prod u_i^{(c_k)_i}$. The group generated by these
columns and $3I_{15}$ has exact HNF determinant $729$.
All columns are actual norms, since $N_1(s_kv_k)=\prod u_i^{(c_k)_i}$
and $N_1(u_i)=u_i^3$ for the included lower unit. Equality of the
proved indices shows that this is the entire completed norm subgroup.
Its literal congruence description is
\[
 \begin{gathered}
 N_1\widehat U_2=
 \{[x]\in\mathbb Z_3^{15}/\mathbb Z_3(9e_1):Qx=0\pmod3\},\\[-2pt]
 {\scriptsize Q=\begin{pmatrix}
 0&1&0&0&2&0&1&0&1&0&2&0&0&0&0\\
 0&0&1&0&1&0&2&0&1&0&2&0&2&1&0\\
 0&0&0&1&2&2&1&0&0&0&1&0&0&0&0\\
 0&0&0&0&0&0&0&1&2&0&0&0&0&0&0\\
 0&0&0&0&0&0&0&0&0&1&1&0&1&1&1\\
 0&0&0&0&0&0&0&0&0&0&0&1&0&0&0
 \end{pmatrix}.}
 \end{gathered}
 \tag{E122.23}
\]
The six coordinate columns numbered $2,3,4,8,10,12$ give a right
inverse to Q modulo three. For an actual preimage map on the norm
image, let M have first nine columns
$c_1,c_8,c_9,c_{10},c_{11},c_{12},c_{14},c_{15},c_{20}$ and last
six columns $3e_2,3e_3,3e_4,3e_8,3e_{10},3e_{12}$.
Its determinant is $94770=3^6\cdot130$. The certificate gives the
complete rational inverse and checks that its lattice over
$\mathbb Z_3$ is exactly (E122.23), in both directions.
For a representative x in that lattice, form $a=M^{-1}x\in\mathbb Z_3^{15}$
and take the corresponding product of the nine actual units $s_kv_k$
and the six included units $u_2,u_3,u_4,u_8,u_{10},u_{12}$,
with exponents a. Its norm is exactly $\prod u_i^{x_i}$.
Changing x by $9e_1$ changes this preimage by an actual norm-one
element. Every other preimage is its product with the completed
norm kernel evaluated in E.121. This specifies the entire fibre
and its torsion-coordinate ambiguity, rather than only an index comparison.

\emph{All later unit defects and their completed norm kernels.}
For every $d\ge2$, the local corestriction comparison (E122.14),
now starting at $B_2$, transports the five columns (E122.22)
unchanged to $\chi_d$. Hence its image has rank five. Set
$F_d=U_d\cap N_d(B_{d+1}^{\times})$. The literal maps are
\[
 \begin{gathered}
 U_d/F_d\xrightarrow[\chi_d]{\sim}\ker\Sigma\subset\mathbb F_3^6,
 \qquad
 F_d/N_dU_{d+1}\xrightarrow[\delta_d]{\sim}
       A_{d+1}/j_dA_d\xrightarrow[n_{d+1}]{\sim}A_2/3A_2,\\
 \delta_d(u)=[D_x]\pmod{j_dA_d},\qquad
 N_dx=u,\qquad
 \operatorname{div}_{\!S^c}(x)=(\sigma_d-1)D_x.
 \end{gathered}
 \tag{E122.24}
\]
In the divisor class take the canonical three-primary projection.
The precise Hilbert90 construction, its well-definedness under a
different x and D, and both kernel and surjectivity are the ideal
maps proved in E.121. Here all vertical class actions are trivial,
so its image is the entire displayed quotient. The actual class
transport $n_{d+1}$ evaluates that quotient as $C_3^4$.
These two maps describe the higher embedded norm subgroup exactly:
first $\chi_d(u)=0$, then $\delta_d(u)=0$.
Their completions retain the same finite quotients.

Every lower cube is the norm of the included element, so the full
cokernel is killed by three. Its order is $3^5\cdot3^4=3^9$.
For the torsion in the completed kernel, put $F=\mathbb Q(\xi)$.
At each fifty-three place of F, $X^{3^d}-53\zeta$ is Eisenstein,
so $B_d/F$ has a unique totally ramified prime there.
The extension $F(\mu_{27})/F$ splits completely at that place,
because $27\mid53^2-1$. Its inclusion in $B_d$ would, after tensoring
with that completion of F, inject a product of three fields into
the single field $B_{d,v}$, which is impossible. Thus
$\mu(B_d)\{3\}=\mu_9$ at every level. The actual norm on this
subgroup is cubing and has kernel the literal $\mu_3$.
Dirichlet's S-unit rank is $3^{d+1}+5$, since $[B_d:\mathbb Q]=6\cdot3^d$
and S has six places. The norm image has finite index, so
\[
 \widehat U_d/N_d\widehat U_{d+1}=C_3^9,\qquad
 \ker(N_d:\widehat U_{d+1}\to\widehat U_d)
       \simeq\mu_3\oplus\mathbb Z_3^{\,2\cdot3^{d+1}}
       \quad(d\ge2).
 \tag{E122.25}
\]
The last isomorphism has an actual construction: choose a
$\mathbb Z_3$-basis of the kernel modulo its literal torsion and
choose lifts $k_i$; send $(z,(a_i))$ to $z\prod k_i^{a_i}$.
The inverse reads quotient coordinates and then divides by that
product to obtain z. It is a continuous bijection between compact
groups, hence a homeomorphism. Changing the basis or its lifts
changes these coordinates by the corresponding invertible integral
matrix and by the stated $\mu_3$ factors. No numerical upper unit
basis is assigned by this choice. Equations (E122.23)--(E122.25)
preserve the actual norm subgroups and the exact class and divisor
maps required for the positional Kummer--Shapiro inverse systems.
\end{proof}
\begin{thebibliography}{9}
\bibitem{E_MilneCFT} J. S. Milne, \emph{Class Field Theory}, version4.03, 2020.
\bibitem{E_PARICertifiedUnits} The PARI Group, \emph{PARI/GP2.19.0 User's Guide}, official function contracts and implementation.
\end{thebibliography}\end{document}
