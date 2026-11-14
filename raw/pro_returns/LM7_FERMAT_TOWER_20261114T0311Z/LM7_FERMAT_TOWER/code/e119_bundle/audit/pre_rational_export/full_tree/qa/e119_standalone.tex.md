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
\subsection{The next positional norm and class maps at fifty-three}

\begin{statement}{E.119}{Proved}{Complete lower class and unit maps, and the exact next coinvariants at $53$}
Fix $\zeta^2+\zeta+1=0$, $\xi^3=\zeta$, $\alpha^3=53$,
and compatible $\beta_d$ with
\[
 \begin{gathered}
 F=\mathbb Q(\xi),\quad M=\mathbb Q(\zeta,\alpha),\quad
 \beta_1=\alpha\xi,\quad \beta_{d+1}^3=\beta_d,\\
 L_d=\mathbb Q(\beta_d),\quad B_d=L_d(\xi),\quad
 S=\{\text{primes over }3,53\},\quad
 A(E)=\operatorname{Cl}_S(E)\{3\}.
 \end{gathered}
 \tag{E119.1}
\]
Thus $B_1=F(\alpha)$, $[B_1:\mathbb Q]=18$,
$[L_1:\mathbb Q]=6$, and $\beta_d^{3^d}=53\zeta$.
Write $\widehat U_E=\varprojlim_n
\mathcal O_{E,S}^{\times}/(\mathcal O_{E,S}^{\times})^{3^n}$.
The actual lower class groups are
\[
 \begin{gathered}
 A(B_1)=C_3^2,\qquad \operatorname{Cl}(B_1)\{3\}=C_9\oplus C_3^2,\\
 A(L_1)=C_3^2,\qquad \operatorname{Cl}(L_1)\{3\}=C_9\oplus C_3.
 \end{gathered}
 \tag{E119.2}
\]
Identify $A(B_1)$ with
$I=\{(e_0,e_1,e_2)\in\mathbb F_3^3:e_0+e_1+e_2=0\}$,
using the first two coordinates, and use the certified $L_1$ ideal
coordinates specified in the proof. The horizontal ideal maps are
\[
 \begin{aligned}
 N_{B_1/L_1}(e_0,e_1)&=(0,e_0+2e_1),&
 j_{B_1/L_1}(a,b)&=(a,a),\\
 \operatorname{Art}_{B_1/L_1}(a,b)&=2a,&
 \ker j_{B_1/L_1}&=\{(0,b):b\in\mathbb F_3\}.
 \end{aligned}
 \tag{E119.3}
\]
The complete horizontal unit maps have the explicit matrices and
inverse representatives (E119.15)--(E119.20). In particular
\[
 \begin{aligned}
 [\widehat U_M:N_{B_1/M}\widehat U_{B_1}]&=9,&
 \ker N_{B_1/M}&\simeq C_3\oplus\mathbb Z_3^8,\\
 N_{B_1/L_1}\widehat U_{B_1}&=\widehat U_{L_1},&
 \ker N_{B_1/L_1}&\simeq C_3\oplus\mathbb Z_3^{10}.
 \end{aligned}
 \tag{E119.4}
\]

Let $\sigma$ be the actual vertical automorphism
$\beta_2\mapsto\zeta\beta_2$, fixing $\xi$ on $B_2$.
The complete next coinvariants, their norms and the ideal-extension
maps followed by the quotient projection are
\[
 \begin{aligned}
 Q_B:=A(B_2)/(\sigma-1)A(B_2)&=C_9\oplus C_3^3,\\
 N_B(x_0,x_1,x_2,x_3)&=(2x_3,x_0+2x_3),&
 \overline j_B(a,b)&=(6a+3b,0,0,0),\\
 Q_L:=A(L_2)/(\sigma-1)A(L_2)&=C_9\oplus C_3,\\
 N_L(x,y)&=(-x,-x+y),&
 \overline j_L(a,b)&=(6a,0).
 \end{aligned}
 \tag{E119.5}
\]
The targets of $N_B,N_L$ are the respective $C_3^2$ in
(E119.2), so these formulas reduce their outputs modulo three.
Both norms are onto, with kernels $C_3^3$ and $C_3$, respectively.
Every coordinate map in (E119.5) is obtained from actual ideal Artin
maps by the retained integral Smith transformations and their inverses.
In particular, the actual capitulation kernels satisfy
\[
 \begin{gathered}
 K_B:=\ker\{A(B_1)\xrightarrow{j}A(B_2)\}
       \ \subseteq\ \{(a,a):a\in\mathbb F_3\},\\
 K_L:=\ker\{A(L_1)\xrightarrow{j}A(L_2)\}
       \ \subseteq\ \{(0,b):b\in\mathbb F_3\},\\
 [\widehat U_{B_1}:N\widehat U_{B_2}]=3^5|K_B|,\qquad
 [\widehat U_{L_1}:N\widehat U_{L_2}]=3|K_L|.
 \end{gathered}
 \tag{E119.6}
\]
The field-norm subgroups inside these two lower unit completions
have indices $9$ and $1$. Their quotients by actual completed
$S$-unit norms therefore have orders $3^3|K_B|$ and $3|K_L|$.

The exact upper groups still occur in the sequences
\[
 \begin{aligned}
 0\longrightarrow(\sigma-1)A(B_2)\longrightarrow A(B_2)
       \longrightarrow Q_B\longrightarrow0,\\
 0\longrightarrow(\sigma-1)A(L_2)\longrightarrow A(L_2)
       \longrightarrow Q_L\longrightarrow0.
 \end{aligned}
 \tag{E119.7}
\]
No value of either left-hand term is assigned by this statement.
The maps (E119.1) identify $L_2\to L_1$ with the literal root-cubing
transition of the $j=1$ positional factor in E.46. Thus (E119.5)--(E119.7)
give an unconditional finite transition for the remaining $53$ norm
system, together with its precise remaining kernel.
The manuscript anchor is \S51.16, fols.~733v--736v,
scans~172--178, through the actual tower comparisons of E.46 and E.114.
\end{statement}

\begin{proof}
All ideal class groups below are taken in their three-primary parts
when a finite three-group is displayed. Completion of a finitely
generated multiplicative group means tensoring its free part with
$\mathbb Z_3$ and retaining its three-primary roots of unity. These
groups are compact. The completion of a whole field's multiplicative
group has the different, explicitly prodiscrete topology used in E.46;
the comparison there is induced by the literal inclusion of $S$-units.

\paragraph{The fields and their labeled local maps.}
The exact equations show that $L_1$ has polynomial
$X^6+53X^3+2809$ and that $B_1$ is the compositum of
$X^3-53$ and $\Phi_9(X)$. The actual primitive element
$x=\xi-\alpha$ has polynomial
\[
 x^{18}+321x^{15}+41505x^{12}+2826974x^9
 +112000083x^6+2393775690x^3+23467349647.
 \tag{E119.8}
\]
All tensor-coordinate calculations use
$(\alpha^r\xi^s)_{0\leq s\leq5,\,0\leq r\leq2}$ in this order.
The executed polynomial and basis identities verify each embedding.

Since $53=-1+54$, the logarithm on $1+3\mathbb Z_3$ gives
$53\in(\mathbb Q_3^\times)^9$. Let $a_0$ be its cube root
congruent to $-1$ modulo nine; $v_3(a_0+1)=2$ and $a_0$ is
itself a cube. The three primes $q_j$ of $B_1$ over three
are labeled by
$\alpha\mapsto a_0\zeta^j$, $j=0,1,2$, with $\xi$ fixed.
Their completions are $\mathbb Q_3(\xi)$.
There are three primes $t_i$ over $53$, all with residue field
$\mathbb F_{53^2}$. The extension $B_1/F$ is split at three
and totally ramified at these three $53$-primes; $B_1/M$ is
totally ramified at its three $3$-primes and split at $53$.
The extension $B_1/L_1$ is unramified and split at all $S$-primes.
Indeed its local map at three is already the equality
$L_{1,3}=\mathbb Q_3(\xi)$, and at $53$ the residue field
contains $\mu_9$ because $9\mid53^2-1$.

The vertical extension $B_2/B_1$ is totally ramified at all
six $S$-primes. At $53$ this follows from the valuation one
of $\beta_1$. At $q_j$, its Kummer equation is
$Z^3=a_0\xi^{1+3j}$ and its local field is
$\mathbb Q_3(\zeta_{27})$ over $\mathbb Q_3(\xi)$.
Here $\beta_1+1$ is an actual norm uniformizer: it is the
norm of $\beta_2+1$, and its local valuation is one.
The extension $L_2/L_1$ likewise has exactly two totally ramified
$S$-places. The displayed equations have discriminants supported
at $3,53$, which excludes any further ramification.

\paragraph{The entire first horizontal $S$-class group.}
The certified field $F$ has class number one. Its seven
complete $S$-unit generators are
\[
 \xi, 1+\xi, 1+\xi^2, -1+\xi^4,
 -4+\xi^4+\xi^5,
 3+2\xi+3\xi^2+3\xi^3-\xi^4+\xi^5,
 -4-\xi+\xi^2-\xi^4.
 \tag{E119.9}
\]
Every generator has zero cubic local character for $B_1/F$
at all three $53$-primes; the retained finite-field reductions
check the three rows separately. At three the extension is split.
The idele class quotient with local norm groups at $S$ and local
units outside $S$ is therefore $C_3^3$. Its restriction to
$\operatorname{Gal}(B_1/F)$ is the sum of its three coordinates.
To identify its kernel with class coinvariants, let
$H^S_{B_1}$ be the $S$-Hilbert three-class field. A decomposition
group above a totally ramified $53$-prime supplies a section of
$\operatorname{Gal}(H^S_{B_1}/F)\to C_3$, since that prime
splits completely in $H^S_{B_1}/B_1$.
Abelianizing this split extension identifies the kernel with
$A(B_1)/(g-1)A(B_1)$, where
$g(\alpha)=\zeta\alpha$ and $g(\xi)=\xi$.
Thus this coinvariant group is exactly $I$.

For completeness, the idele construction used here is the actual
global reciprocity map whose restriction to a local multiplicative
group is local reciprocity
\cite[V,Proposition5.2 and Theorems5.3 and5.5]{E_MilneCFT}.
For an abelian extension of $F$, pullback to $B_1$ is unramified
outside $S$ precisely when its local units outside $S$ are killed;
it splits at each place in $S$ precisely when the local norm
subgroup is killed. This proves both inclusions between that
idele quotient's class field and the maximal subfield of
$H^S_{B_1}$ abelian over $F$.

Now let $c$ be complex conjugation fixing $\alpha$.
Its fixed field is
$R=\mathbb Q(\alpha,\xi+\xi^{-1})$, of signature $(3,3)$.
The literal compositum gives the polynomial
\[
 X^9-9X^7+162X^6+27X^5+459X^4+7290X^3
       +1458X^2+51030X+156033.
 \tag{E119.10}
\]
The successful \texttt{bnfcertify(R,1)} gives a natural
class-presentation upper quotient $C_3$. Its five actual
$S$-prime classes in this quotient are $(1),(1),(0),(0),(0)$.
The certificate also retains and checks the full principal
ideal relation for each of these five coordinates and the
third power of the sole class generator.
Consequently the true $A(R)$ is zero. This conclusion uses exactly
the flag-one class-generation assertion; unit completeness is
proved separately below. The official flag-one contract is
\cite[\texttt{bnfcertify}, flag1]{E_PARICertifiedUnits}.
The actual quadratic maps satisfy $Nj=2$ and $jN=1+c$.
They give $1+c=0$ on $A(B_1)$, so $c=-1$.
The field identity $cgc=g^{-1}$ now gives $g=g^{-1}$ on this
three-group. Together with $g^3=1$ it gives $g=1$.
This proves $A(B_1)=I$, with the same ideal map used above.

\paragraph{A literal $S$-Hilbert field and the horizontal class maps.}
Set $h(\xi)=\xi^4$ and
\[
 \begin{aligned}
 \pi_0&=-1+3\xi-3\xi^2+3\xi^4,\\
 \pi_1&=-1-3\xi+3\xi^2+3\xi^5,\qquad
 \pi_2=-1-3\xi^4-3\xi^5,\\
 h(\pi_j)&=\pi_{j+1},\qquad \pi_0\pi_1\pi_2=53.
 \end{aligned}
 \tag{E119.11}
\]
Indices on $\pi_j$ are modulo three. Their valuation matrix
at the three $53$-primes is
$\left(\begin{smallmatrix}1&0&0\\0&0&1\\0&1&0\end{smallmatrix}\right)$.
At three put $\lambda=1-\xi$ and
$w=-1+2\lambda^2+\lambda^3$.
The exact polynomial calculation gives
$v_\lambda(w^3-\pi_0)=13>12=2v_\lambda(3w^2)$;
Hensel's lemma gives a local cube root. Conjugating by $h$
proves this for all three radicals. At every $53$-prime the
residue of $\pi_j/53^{v(\pi_j)}$ has cubic character zero.
Thus
\[
 \mathcal H=F(\gamma_0,\gamma_1,\gamma_2),\quad
 \gamma_j^3=\pi_j,\quad \gamma_0\gamma_1\gamma_2=\alpha,
 \qquad \mathcal H=H^S_{B_1}.
 \tag{E119.12}
\]
The independent prime valuations prove $[\mathcal H:F]=27$.
The local calculations prove that $\mathcal H/B_1$ is unramified
and $S$-split. Its degree nine equals $|A(B_1)|$, proving the
last equality by the class-field correspondence
\cite[V,Theorem3.6 and Example3.9]{E_MilneCFT}.
All $\pi_j$ are fixed by $c$; choose their real cube roots.
Then $c$ negates all Kummer phases, while $h$ cyclically permutes them.

The first two Kummer phases give the coordinates of $I$ used
in the statement. The actual prime data
\[
 \begin{array}{c|rrrr|c|c}
 p&\xi&\alpha&\beta_1&& (e_0,e_1,e_2)&[\mathfrak p]_{A(L_1)}\\ \hline
 163&53&6&155&& (0,2,1)&(0,1)\\
 163&40&6&77 && (0,1,2)&(0,2)\\
 163&38&6&65 && (2,0,1)&(0,2)
 \end{array}
 \tag{E119.13}
\]
give the norm row in (E119.3); every entry is a literal
residue in $\mathbb F_{163}$. The ideal norm sends each prime
to its contraction to the displayed residue-degree power, as
in the proved Frobenius square
\cite[V,Proposition3.3]{E_MilneCFT}.
The certified ordinary class coordinates of $L_1$ are
$C_9\oplus C_3$, with its $3$-prime $(6,0)$ and its
$53$-prime zero; reducing the first coordinate modulo three
gives $A(L_1)$. Two actual primes over seven have ordinary
coordinates $(1,0)$ and $(7,1)$. Both have residue degree one
and act on $\xi$ by $\xi\mapsto\xi^7$, giving the Artin
row $2a$ in (E119.3).

The whole group $\operatorname{Gal}(\mathcal H/L_1)$ is
\[
 \{(e,b)\in\mathbb F_3^3\rtimes\mathbb F_3:
           e_0+e_1+e_2+b=0\},\qquad
 (e,b)(f,d)=(e+h^bf,b+d).
 \tag{E119.14}
\]
Here $h^b$ acts by cyclic permutation and
$\tau=(-e_0,1)$ fixes $\beta_1=\alpha\xi$.
Its cube is the phase $-(1,1,1)$.
The transfer from this group to $I$ is zero on $I$, since
$1+h+h^2$ kills $I$, and sends $\tau$ to $\tau^3$.
The Artin coordinate of $\tau$ is one, hence its first
$L_1$ coordinate is two. This gives exactly
$j(a,b)=(a,a)$, including its sign.
The inclusion/transfer square follows from the proved
restriction/corestriction compatibility of the reciprocity
cup product \cite[III,Theorem3.1 and its proof]{E_MilneCFT};
the calculation here specifies the actual transfer on every element.
More explicitly, on $\widehat H^{-2}(G,\mathbb Z)=G^{\rm ab}$,
restriction to a subgroup is group transfer and corestriction is
the map induced by subgroup inclusion. On
$\widehat H^0(G,E^\times)$, the corresponding maps are field
inclusion and field norm. Cupping with the fundamental class
therefore gives inclusion--transfer and norm--restriction for
the compatible local Artin maps. The product of these local maps
in V,Proposition5.2 gives the stated global ideal maps.

\paragraph{Complete units, divisors and inverse norm coordinates.}
Let $U_1,\ldots,U_{15}$ be the literal elements in the
\texttt{tensor\_unit\_columns} table of
\texttt{e53\_horizontal\_norm\_matrix.out}.
This table consists of eighteen rational coefficients per
element in the tensor basis following (E119.8); it is part
of the retained certificate. In particular
$U_1=\xi$, $U_2=-1+\xi-\xi^3$,
$U_3=-1-\xi^3+\xi^4$, and $U_{12}=-1+\xi^4$.
The proof uses every full principal ideal, checked against its
displayed $S$-divisor. It does not use the candidate upper
BNF's class number or unit completeness.

In the analytic order $(q_0,q_1,q_2,t_1,t_2,t_3)$,
the only nonzero $S$-valuation columns are
$v(U_{10})=(0,0,3,0,0,0)$,
$v(U_{11})=(0,3,0,0,0,0)$,
$v(U_{12})=(1,1,1,0,0,0)$ and
$v(U_{12+i})=e_{3+i}$, $1\leq i\leq3$.
The analytic order of the $3$-primes is $(3,2,1)$ in the
retained PARI prime list.
Use the complete certified $M$ basis from E.116,
$(\zeta,f_1,f_2,q_1,q_2,q_3,\alpha)$, where the $q_i$
are the literal principal $3$-prime generators in that
PARI order. The complete norm matrix is
\[
 N_M=\left(\begin{array}{*{15}{r}}
 1&2&2&2&0&1&2&2&2&1&1&1&1&1&1\\
 0&0&0&0&0&0&0&1&0&2&2&2&0&0&0\\
 0&0&0&0&0&0&0&1&1&1&1&1&0&0&0\\
 0&0&0&0&0&0&0&0&0&0&0&1&0&0&0\\
 0&0&0&0&0&0&0&0&0&3&0&1&0&0&0\\
 0&0&0&0&0&0&0&0&0&0&3&1&0&0&0\\
 0&0&0&0&0&0&0&0&0&0&0&0&1&1&1
 \end{array}\right).
 \tag{E119.15}
\]
The first row is modulo three; the other rows lie in
$\mathbb Z_3$. Multiplication by $-1$ disappears under this
completion by its literal compatible odd roots. Before completion,
the retained PARI objects contain the full signed algebraic norms.

Here is an independent proof that the matrix gives the entire
norm image and that the listed elements are complete.
For a cyclic extension $E/D$ unramified outside $S$, the map
\[
 H^1(\langle\sigma\rangle,\mathcal O_{E,S}^{\times})
 \longrightarrow\ker\{\operatorname{Cl}_S(D)\to
                         \operatorname{Cl}_S(E)\},
 \quad [\sigma x/x]\longmapsto[D_0],\quad
 \operatorname{div}_{\notin S}(x)=jD_0
 \tag{E119.16}
\]
is an isomorphism. Indeed Hilbert 90 supplies $x$; its divisor
is invariant, and outside $S$ every invariant divisor is an
extended base divisor, because there is no ramification.
Changing $x$ by a base element changes $D_0$ by a principal
divisor; changing its cocycle by a unit coboundary does the same.
Conversely a principal extended divisor supplies $x$ and its
unit cocycle. These constructions are mutual inverses.
This is the explicit outside-$S$ version of the ideal/Hilbert90
maps in \cite[Proposition1 and full ideal proof]{E_LemmermeyerAmbiguous}.

E.116 gives $A(M)=0$. For $B_1/M$, (E119.16) therefore has
zero three-primary part. The $S$-unit Herbrand quotient is
$3^3/3=9$, since exactly the three $3$-places have local degree
three; see the complete lattice proof in
\cite[VII,Proposition3.1]{E_MilneCFT}.
Thus the true completed unit-norm index is nine.
Adjoining the torsion relation $3e_1$ to (E119.15) gives
an image HNF of determinant nine. Every column is an actual
norm, so the candidate image is the entire image.
At each $3$-place the relative residue degree is one, hence
the norm preserves its normalized valuation. It follows that
the full principal $S$-divisor lattice of $B_1$ is exactly
\[
 \{(a_0,a_1,a_2,b_1,b_2,b_3)\in\mathbb Z_3^6:
                    a_0\equiv a_1\equiv a_2\pmod3\}.
 \tag{E119.17}
\]
The valuation columns already listed give its converse inclusion.

The first nine elements are ordinary units, including $\xi$.
Their nine residue-character rows at the actual prime labels
\[
 \begin{gathered}
 (7,1,3),(7,2,3),(7,3,3),(7,4,3),(7,5,3),\\
 (11,1,6),(163,1,1),(163,2,1),(397,1,1)
 \end{gathered}
\]
have determinant $-17$.
The labels mean rational prime, actual prime-list index,
and residue degree. Both the matrix and its full inverse
modulo three are retained. The ordinary unit rank is eight;
the three-primary roots of unity are exactly $\mu_9$.
Indeed $\mu_{27}\subset B_1$ would force the degree-eighteen
field $B_1$ to equal $\mathbb Q(\zeta_{27})$, contradicting
its ramification at $53$. Thus the determinant proves that
these nine classes form a basis modulo cubes of the full
ordinary unit group. Nakayama's lemma on its finite-rank
completion proves completeness. With (E119.17), all fifteen
columns give
$\widehat U_{B_1}=C_9\oplus\mathbb Z_3^{14}$.

For a target
$\zeta^z f_1^x f_2^y q_1^{a_1}q_2^{a_2}q_3^{a_3}\alpha^w$
with $a_1\equiv a_2\equiv a_3\pmod3$, put
$r=a_1$, $s=(a_2-a_1)/3$, $t=(a_3-a_1)/3$,
$d=r+s+t$, $x'=x-2d$, $y'=y-d$.
An actual inverse representative and the full kernel are
\[
 \begin{gathered}
 U_{12}^{r}U_{10}^{s}U_{11}^{t}U_8^{x'}U_9^{y'-x'}U_{13}^{w}
            \xi^{[z-2y'-d-w]_3},\\
 \ker N_M=\langle\xi^3\rangle\ \oplus\
 \langle U_2\xi^{-2},U_3\xi^{-2},U_4\xi^{-2},U_5,
 U_6\xi^{-1},U_7\xi^{-2},U_{14}/U_{13},U_{15}/U_{13}\rangle_{\mathbb Z_3}.
 \end{gathered}
 \tag{E119.18}
\]
Here $[z]_3$ means the representative $0,1,2$ of the torsion
coordinate, and every other exponent is three-adic. Reading
the eight free nonpivot coordinates and then the exponent
of $\xi^3$ gives the inverse kernel coordinates. This is a
continuous coset representative; the map $C_3\to C_9$ taking
these digits has its actual carry in $\langle\xi^3\rangle$.

The complete $L_1$ unit basis is
$(\zeta,u_1,u_2,q,\beta_1)$, where
\[
 \begin{aligned}
 u_1&=-7+\beta_1^2-(32/53)\beta_1^3
                  +(7/53)\beta_1^4-(1/53)\beta_1^5,\\
 u_2&=-7+7\beta_1+\beta_1^2-(32/53)\beta_1^3
                                      +(2/53)\beta_1^5,\\
 q&=3600+1116\beta_1+199\beta_1^2+(3777/53)\beta_1^3
                          +(411/53)\beta_1^4-(91/53)\beta_1^5.
 \end{aligned}
 \tag{E119.19}
\]
Its two $S$-valuation columns are $(3,0)$ and $(0,1)$.
In this basis the actual horizontal norm matrix is
\[
 N_L=\left(\begin{array}{*{15}{r}}
 1&2&2&1&2&0&1&0&0&2&1&2&0&1&1\\
 0&0&0&1&2&2&1&0&-1&2&1&2&0&1&-1\\
 0&0&0&2&1&1&2&-1&-1&2&3&2&-1&1&0\\
 0&0&0&0&0&0&0&0&0&1&1&1&0&0&0\\
 0&0&0&0&0&0&0&0&0&0&0&0&1&1&1
 \end{array}\right).
 \tag{E119.20}
\]
For a target $(z,x,y,c,d)$, set $x'=x-2c$,
$y'=y-2c+d$. The representative
$U_{10}^cU_{13}^dU_9^{-x'}U_8^{x'-y'}\xi^{[z-2c]_3}$
maps exactly to that target. Subtracting this representative
from the ten nonpivot source generators
$U_2,\ldots,U_7,U_{11},U_{12},U_{14},U_{15}$ gives
a free kernel basis; $\xi^3$ gives its $C_3$ summand.
The forward and inverse integer matrices are retained.
They prove both topological isomorphisms in (E119.4).

The divisor lattice (E119.17) has index nine, so the subgroup
of $\operatorname{Cl}(B_1)\{3\}$ generated by $S$ has order
nine. Together with $A(B_1)=C_3^2$ this proves that the ordinary
three-class group has order $81$. Three literal ideals
$G_1,G_2,G_3$, moved outside $S$ by retained exact principal
corrections, satisfy the verified relations
$G_1^9=(f_1)$, $G_2^3=(f_2)$, $G_3^3=(f_3)$.
Their full HNF ideals, principal factors and factor-prime proofs
are retained. Their Kummer genus columns and the actual $S$-prime
coordinates are
\[
 \begin{pmatrix}1&0&2\\0&0&2\\2&0&2\end{pmatrix},
 \qquad
 \begin{pmatrix}3&0&6&0&0&0\\1&1&1&0&0&0\\0&0&0&0&0&0\end{pmatrix}.
 \tag{E119.21}
\]
The $S$ columns here are in the original prime-list order.
The first matrix spans $A(B_1)$, and the second shows that
the generated subgroup contains the entire $S$-prime subgroup.
It has order at least $81$; the three principal power relations
bound its order by $9\cdot3\cdot3=81$.
This proves its generation and exact type in (E119.2).
The attempted upper BNF certification terminated by timeout;
its source and actual exit output are retained. None of the
order, generation or saturation deductions above uses its success.

\paragraph{Six actual local characters at the next level.}
Let $\chi_v(u)$ be the exponent on a cube root of $\beta_1$
under arithmetic local reciprocity of $u$.
At $q_j$, write $v=v_{q_j}(u)$. The actual cyclotomic norm square
gives
\[
 \begin{aligned}
 \chi_{q_j}(u)&=-\frac{
  N_{\mathbb Q_3(\xi)/\mathbb Q_3}
       (u/(\beta_1+1)^v)-1}{9}\pmod3,\\
 \chi_{t_i}(u)&=-\log_\zeta
       \left(\overline{u/\beta_1^{v_{t_i}(u)}}^{(53^2-1)/3}\right).
 \end{aligned}
 \tag{E119.22}
\]
For the first formula, $\beta_1=a_0\xi^{1+3j}$ locally;
a cube root of $a_0$ is already in $\mathbb Q_3$.
Arithmetic reciprocity on cyclotomic units raises roots of unity
to the inverse absolute norm. On the root of $\xi^{1+3j}$,
the factor $1+3j$ is one modulo three. This gives the first
sign and the denominator nine. The chosen norm uniformizer
has character zero. The second formula is the tame symbol
with first argument $u$, second argument $\beta_1$;
the local uniformizer is again a norm. Both formulas use
the same global $\zeta$ and the same local reciprocity normalization.
The norm/inclusion square used in these statements follows from
the proved cup-product compatibility in
\cite[III,Theorem3.1]{E_MilneCFT}.

On the complete fifteen columns the first three character rows
are all $c_q$ and the last three are all $c_t$, where
\[
 \begin{aligned}
 c_q&=(0,0,0,0,0,0,0,0,0,1,1,0,1,1,1),\\
 c_t&=(0,0,0,0,0,0,0,2,1,0,0,0,0,0,0).
 \end{aligned}
\]
Their rank is exactly two and their column sums are zero.
All entries are retained with their local valuation corrections
and the checked three-adic precision. Since units at unramified
places are local norms, the cyclic Hasse norm theorem, including
its injectivity proof \cite[VIII,Theorem3.1]{E_MilneCFT}, identifies
the common kernel with the field-norm subgroup inside the
completed $S$-units. Its index is $3^2=9$.
This also proves the completion assertion: the quotient is
killed by three, so the finite character map has the identical
kernel after completion and its image remains unchanged.

\paragraph{The actual next genus group over $B_1$.}
Let $\Gamma_B$ be the Galois group over $B_1$ of the maximal
subfield of $H^S_{B_2}$ abelian over $B_1$.
The same local-to-global Artin maps as above identify it with
the three-primary part of
\[
 J_{B_1}\Big/
 B_1^\times\left(\prod_{v\in S}N(B_{2,w}^\times)\right)
              \left(\prod_{v\notin S}\mathcal O_{B_{1,v}}^\times\right).
 \tag{E119.23}
\]
Every $S$-place is totally ramified, so the local factors have
order three. The exact sequence from $S$-units to these six
factors and then to $A(B_1)$ gives
$|\Gamma_B|=3^{6-2}\cdot9=729$.
This is an actual idelic quotient, with ideals mapped by their
uniformizer ideles. It therefore retains all class-extension
information needed to distinguish exponent nine from exponent three.

Choose the six local generators so that each restricts to the
fixed generator of $\operatorname{Gal}(B_2/B_1)$, followed by
the three outside-$S$ ideal generators $G_i$ in (E119.21).
For $G_i^{n_i}=(f_i)$ the relation is
$n_iG_i+\sum_v\chi_v(f_i)E_v=0$.
For $Q_v=(f_v)\prod_iG_i^{c_{iv}}$ it is
$\sum_i c_{iv}G_i-\sum_w\chi_w(f_v)E_w=0$.
These signs follow by applying the global product formula to
the principal ideles $f_i,f_v$; the former have divisor
$n_iG_i$ outside $S$, whereas the latter have divisor
$-\sum_i c_{iv}G_i$ outside $S$.

Thus an integral presentation matrix is
\[
 R_B=
 \begin{pmatrix}
 3I_6&C_{\rm ord}&R_c&R_s\\
 0&0&\operatorname{diag}(9,3,3)&C_s
 \end{pmatrix},\quad
 R_c=\begin{pmatrix}0&1&0\\0&1&0\\0&1&0\\0&0&1\\0&0&1\\0&0&1\end{pmatrix},
 \tag{E119.24}
\]
where $C_{\rm ord}$ is the first nine character columns,
$C_s$ is the second matrix in (E119.21), and
\[
 R_s=\begin{pmatrix}
 -2&-2&-1&-1&-1&-1\\
 0&0&-2&-1&-1&-1\\
 -2&-2&-1&-1&-1&-1\\
 -1&0&-1&0&0&0\\
 -2&0&0&0&0&0\\
 0&0&-2&0&0&0
 \end{pmatrix}.
 \tag{E119.25}
\]
All principal factors defining these columns are retained as
products of literal algebraic numbers; equality of their ideals
is checked by exact prime-valuation cancellation. Every rational
prime used in those cancellations is proved prime by the program.
Factored generators avoid an expansion that overflowed the stack
in a preserved earlier run; the exact factorized equality supplies
the same principal divisor map.

The HNF of (E119.24) is
\[
 H_B=\begin{pmatrix}
 3&0&1&0&0&0&0&0&0\\
 0&3&1&0&0&0&0&2&0\\
 0&0&1&0&0&0&0&0&0\\
 0&0&0&3&0&1&2&0&0\\
 0&0&0&0&3&1&1&0&0\\
 0&0&0&0&0&1&0&0&0\\
 0&0&0&0&0&0&3&0&0\\
 0&0&0&0&0&0&0&1&0\\
 0&0&0&0&0&0&0&0&3
 \end{pmatrix},\qquad
 \rho_B=(1,1,1,1,1,1,2,1,0).
 \tag{E119.26}
\]
The row $\rho_B$ is the actual restriction to $B_2$.
Its last three entries are the cubic residue symbols of
$\beta_1$ on the actual factors of $G_1,G_2,G_3$.
It annihilates every relation modulo three.
The retained unimodular Smith maps give
$\Gamma_B=C_9\oplus C_3^4$.

For an entirely specified inverse to the kernel coordinates,
put $K_B^{\rm lat}e_1=3e_1$ and
$K_B^{\rm lat}e_j=e_j-\rho_{B,j}e_1$ for $2\leq j\leq9$.
Its image is the full inverse image in $\mathbb Z_3^9$ of
$\ker\rho_B$. With $H'_B=(K_B^{\rm lat})^{-1}H_B$, the
retained unimodular matrices $P_B,Q_B'$ satisfy
\[
 P_BH'_BQ_B'=\operatorname{diag}(9,3,3,3,1,1,1,1,1),
 \quad
 z\longmapsto K_B^{\rm lat}P_B^{-1}z,\quad
 x\longmapsto P_B(K_B^{\rm lat})^{-1}x.
 \tag{E119.27}
\]
The displayed maps are mutual inverses modulo the actual relation
lattices. The executable certificate checks both compositions for
all $243$ kernel classes and all $729$ classes of $\Gamma_B$.

To identify this kernel with the exact group in (E119.5), use
a decomposition group of $H^S_{B_2}/B_1$ above any totally ramified
$S$-prime. Its restriction to $B_2$ is an isomorphism onto $C_3$,
because the next extension is $S$-split. Hence
$\operatorname{Gal}(H^S_{B_2}/B_1)=A(B_2)\rtimes C_3$.
Its abelianization has kernel $A(B_2)/(\sigma-1)A(B_2)$.
This gives exactly the first quotient map of (E119.7).
Norm to $A(B_1)$ kills the six local generators and sends
$G_i$ to the first two rows of (E119.21).
Composing that matrix with (E119.27) gives $N_B$ in (E119.5).
Extension to coinvariants sends an ideal generator to three times
its lifted idele class: in the split semidirect product this is
the transfer followed by abelianization. Different lifts differ
by local elements of exponent three, so this map is independent
of the lift. Lifting $(a,b)\in A(B_1)$ by
$G_1^{a-b}G_3^{2b}$ and applying (E119.27) gives
$\overline j_B(a,b)=(6a+3b,0,0,0)$.
These maps satisfy $N_B\overline j_B=3$ and
$\overline j_BN_B=3$, in their respective groups.

\paragraph{The direct positional transition.}
For $L_2/L_1$, the two characters on every one of the five
complete $S$-unit generators (E119.19) are zero.
The wild formula is (E119.22) with the exact global norm
$N_{L_1/\mathbb Q}(u)$ divided by
$2757^{v_3(u)}$; here $2757=53^2-53+1$ is the norm of
$\beta_1+1$. The tame formula is unchanged.
The certified two ordinary ideal generators of orders nine and
three have zero class-power characters. Their outside-$S$
Frobenius characters are both one. The $S$-prime relations
have lower class columns $(6,0),(0,0)$ and negative local
character columns $(-1,-2),(0,0)$.
The resulting presentation, restriction and norm-kernel lattice are
\[
 \begin{gathered}
 R_L=\begin{pmatrix}
 3&0&0&0&-1&0\\0&3&0&0&-2&0\\
 0&0&9&0&6&0\\0&0&0&3&0&0
 \end{pmatrix},\quad
 \rho_L=(1,1,1,1),\\
 H_L=\begin{pmatrix}3&0&1&0\\0&3&2&0\\0&0&3&0\\0&0&0&3\end{pmatrix},\quad
 K_L^{\rm lat}=\begin{pmatrix}3&-1&-1&-1\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
 \end{gathered}
 \tag{E119.28}
\]
The same actual idelic and decomposition-group maps identify
$\Gamma_L=C_9\oplus C_3^2$ and its kernel
$Q_L=C_9\oplus C_3$. The Smith transformations of
$(K_L^{\rm lat})^{-1}H_L$ have diagonal $(9,3,1,1)$.
Composing their inverse with the projection to the two ideal
coordinates gives $N_L(x,y)=(-x,-x+y)$; composing their forward
map with three times the two lifted ideal generators gives
$\overline j_L(a,b)=(6a,0)$.
All $27$ kernel classes and all $81$ full classes, with both
inverse maps, are checked. The explicit norm kernels are
$\{(3r,x_1,x_2,0)\}\simeq C_3^3$ for $B$ and
$\{(3r,0)\}\simeq C_3$ for $L$.

\paragraph{The retained unit defect and tower comparison.}
The actual class norm is onto in both vertical extensions.
One proof with its precise map is to intersect the lower
$S$-Hilbert three-class field with the cyclic upper field.
That intersection is trivial over the base: the latter is
ramified at $S$, while the former is split there. For any
lower class, Chebotarev applied to their compositum gives a
prime with that class and trivial upper Frobenius. Its degree-one
upper prime has that exact ideal norm. Equivalently, the norms
in (E119.5) already give all nine lower classes.
The full ideal-extension map followed by the quotient in
(E119.7) is the displayed $\overline j$; therefore its actual
kernel injects into the two lines in (E119.6).

Apply the explicit isomorphism (E119.16) to these two vertical
extensions. Their $S$-unit Herbrand quotients are $3^6/3=3^5$
and $3^2/3=3$, respectively. This proves the two exact index
formulas in (E119.6). Tensoring the finite-rank unit sequences
with $\mathbb Z_3$ is exact, and finite cyclic group cohomology
commutes with this flat tensor product; hence these are the
stated completed indices as well. The field-norm indices follow
from the complete local character matrices and the cyclic Hasse
norm theorem. Dividing the two indices proves the asserted
orders of the remaining unit defects. This retains the actual
capitulation map instead of replacing a unit norm by a field norm.

Finally the evaluation-at-a-root Kummer--Shapiro map of E.46
identifies the root-cubing pushforward with
$N_{L_2/L_1}$, using the literal embeddings
$\beta_1=\beta_2^3$ in (E119.1). Its extension to the auxiliary
field is induced by $L_d\hookrightarrow B_d$; horizontal norms
commute with the vertical norms by the tower identity for
the product of conjugates. On divisors these are the maps
$\mathfrak P\mapsto\mathfrak p^{f(\mathfrak P/\mathfrak p)}$;
on classes and units they are the maps computed above.
The obstruction to replacing the exact upper class group by
its evaluated coordinates is precisely the left term of
(E119.7). Evaluating that term and the resulting actual
capitulation is the remaining step before these finite
transition formulas can be iterated as a full positional
norm-system classification.
\end{proof}
\begin{thebibliography}{9}
\bibitem{E_MilneCFT} J. S. Milne, \emph{Class Field Theory}, version4.03, 2020.
\bibitem{E_LemmermeyerAmbiguous} F. Lemmermeyer, \emph{The Ambiguous Class Number Formula Revisited}, arXiv:1309.1071, 2013.
\bibitem{E_PARICertifiedUnits} The PARI Group, \emph{PARI/GP2.19.0 User's Guide}, \texttt{bnfcertify}, and official source \texttt{buch3.c}.
\end{thebibliography}\end{document}
