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
\subsection{The actual normalizer determines both upper class groups at fifty-three}

\begin{statement}{E.121}{Proved}{Full upper S-class groups, trace maps and unit defects}
Retain the compatible roots and prime labels of E.119:
\[
 \begin{gathered}
 \zeta=\zeta_3,\quad \xi=\zeta_9,\quad
 \alpha=53^{1/3},\quad
 \beta_1=\alpha\xi,\quad \beta_2^3=\beta_1,\\
 L_i=\mathbb Q(\beta_i),\quad B_i=L_i(\xi),\quad
 F=\mathbb Q(\xi),\quad
 A_D=\operatorname{Cl}_S(D)\{3\},\quad S=\{v:v\mid3\cdot53\}.
 \end{gathered}
 \tag{E121.1}
\]
The roots of positive rational numbers are positive, and the
roots of unity are the fixed compatible ones. On $B_2$ put
$g(\beta_2)=\xi\beta_2$, $g(\xi)=\xi$,
$h(\beta_2)=\beta_2$, $h(\xi)=\xi^4$, and $\sigma=g^3$.
The entire upper S-class groups are
\[
 A_{B_2}=C_9\oplus C_3^3,\qquad
 \sigma|A_{B_2}=1,\qquad
 A_{L_2}=C_9^2.
 \tag{E121.2}
\]
Use the E.119 Smith coordinates $x=(x_0,x_1,x_2,x_3)$ on
$A_{B_2}$, with moduli $(9,3,3,3)$, and write $e_i$ for their
positive coordinate generators. Set $u=N_{B_2/L_2}(e_0)$.
Choose $a\in A_{L_2}$ whose E.119 coinvariant coordinate is
$(1,1)\in C_9\oplus C_3$. Then $(u,a)$ is an actual basis of
$A_{L_2}$, both generators having order nine. Its precise
ambiguity is $a\mapsto a+3ku$, $k\in\mathbb Z/3$.

In these bases the full horizontal maps, with target rows reduced
by their displayed moduli, are
\[
 N_h=\begin{pmatrix}1&0&6&6\\0&3&6&3\end{pmatrix}
 :A_{B_2}\longrightarrow A_{L_2},\qquad
 j_h=\begin{pmatrix}0&3\\2&0\\2&0\\0&1\end{pmatrix}
 :A_{L_2}\longrightarrow A_{B_2}.
 \tag{E121.3}
\]
The lower bases of $A_{B_1}=C_3^2$ and $A_{L_1}=C_3^2$ remain
exactly those of E.119. The full vertical norm and extension
maps are
\[
 \begin{aligned}
 N_B&=\begin{pmatrix}0&0&0&2\\1&0&0&2\end{pmatrix},
 &j_B&=\begin{pmatrix}6&3\\0&0\\0&0\\0&0\end{pmatrix},\\
 N_L&=\begin{pmatrix}0&2\\2&0\end{pmatrix},
 &j_L&=\begin{pmatrix}0&6\\6&0\end{pmatrix}.
 \end{aligned}
 \tag{E121.4}
\]
Thus $\ker j_B=\langle(1,1)\rangle$, $\ker j_L=0$, and
$\ker j_h=3A_{L_2}\simeq C_3^2$. Every norm here is the
actual ideal norm, and every $j$ is actual ideal extension.
The upper positional action and its quotient map are
\[
 \sigma_L=\begin{pmatrix}1&3\\0&1\end{pmatrix},\qquad
 p_L=\begin{pmatrix}6&1\\2&1\end{pmatrix}
 :(\mathbb Z/9)^2\longrightarrow
        \mathbb Z/9\oplus\mathbb Z/3,\qquad
 \ker p_L=(\sigma_L-1)A_{L_2}=\langle3u\rangle.
 \tag{E121.5}
\]

The full normalizer actions on $A_{B_2}$ are
\[
 G=\begin{pmatrix}
 1&0&0&0\\2&0&1&2\\2&2&2&2\\0&0&0&1
 \end{pmatrix},\qquad
 H=\begin{pmatrix}
 4&3&6&0\\2&2&2&0\\0&1&0&0\\1&0&0&1
 \end{pmatrix}.
 \tag{E121.6}
\]
In particular $(g-1)A_{B_2}=\langle(0,1,1,0)\rangle$.
The cyclic-nine genus construction over $F$ gives the actual
quotient
\[
 \begin{gathered}
 (A_{B_2})_g=C_9\oplus C_3^2,\qquad
 \pi_g=
 \begin{pmatrix}5&3&6&6\\1&1&2&1\\0&0&0&2\end{pmatrix},\\
 (A_{B_2})_h=C_9\oplus C_3,\qquad
 (A_{B_2})_{g,h}=C_3^2,\qquad
 \ker\pi_g=\langle(0,1,1,0)\rangle .
 \end{gathered}
 \tag{E121.7}
\]
These maps compare the groups through their actual class-field
and ideal maps. For example the projected horizontal norm
$Q_B\to Q_L$ of E.119 has image $3C_9\oplus C_3$, of index
three, even though $Q_{B,h}$ and $Q_L$ both have type
$C_9\oplus C_3$.

There is also a literal normal-closure comparison:
\[
 \begin{gathered}
 C=B_2\overline{B_2}
    =\mathbb Q(53^{1/9},\zeta_{27}),\qquad
 B_2\cap\overline{B_2}=B_1,\\
 C/B_2\text{ is cyclic cubic, unramified and S-split},\qquad
 \psi_C(x)=x_0+x_1+2x_2+x_3\pmod3.
 \end{gathered}
 \tag{E121.8}
\]
Here $\psi_C$ is the Artin character of that actual extension,
with the positive generator specified in the proof.

Write $U_D=\mathcal O_{D,S}^{\times}$, and put a hat with
subscript three for completion by multiplication by powers
of three. The following finite unit-norm groups and completed
norm kernels are determined:
\[
 \begin{array}{c|c|c|c}
 E/D&U_D/N U_E&
 (U_D\cap N E^\times)/N U_E&
 \ker(\widehat U_{E,3}\to\widehat U_{D,3})\\ \hline
 B_2/B_1&C_3^6&C_3^4&C_3\oplus\mathbb Z_3^{18}\\
 L_2/L_1&C_3&C_3&C_3\oplus\mathbb Z_3^6\\
 B_2/L_2&C_3&C_3&C_3\oplus\mathbb Z_3^{22}.
 \end{array}
 \tag{E121.9}
\]
The finite quotients and their actual defining norm subgroups
are unchanged by completion. Formula (E121.20) gives their
element-to-ideal comparison and inverse; no uncomputed upper
unit basis is assigned a numerical matrix.
This settles the full next lower positional transition at $53$.
It does not assign the same groups to subsequent levels.
The comparison to the global $H$-section norm system remains
E.46's literal root-evaluation and root-cubing Kummer--Shapiro
map, and the further intrinsic maps remain the quotients of
E.38. The manuscript anchor is \S51.16, scans172--178,
folios733v--736v, equations(371)--(379), and Part E(c),(d).
\end{statement}

\begin{proof}
\emph{Fields and the actual genus quotient over $F$.}
The polynomial $X^9-53\zeta$ is Eisenstein at each prime over
$53$ of $F$, so $[B_2:F]=9$ and $g$ is its specified generator.
The formulas for $h$ preserve $\beta_2^9=53\zeta$ and give
$hgh^{-1}=g^4$, $h^3=1$. Their restrictions to $B_1$ are
$g(\alpha)=\zeta\alpha$ and
$h(\alpha)=\zeta^{-1}\alpha$, $h(\xi)=\xi^4$.

The equality $v_3(53+1)=3$ places $53$ in the ninth powers
of $\mathbb Q_3^\times$: on $1+3\mathbb Z_3$ this follows
from the convergent logarithm and multiplication by nine,
and the sign has its compatible odd root. Thus the completion
of $B_2/F$ at three is
$\mathbb Q_3(\zeta_{27})/\mathbb Q_3(\xi)$, of degree three.
At the three primes over $53$ the local degree is nine.
There is no other finite ramification.

Let $\Gamma_F$ be the Galois group over $F$ of the maximal
subfield of $H^S_{B_2}$ abelian over $F$. The local-to-global
Artin quotient of E119.23, now over $F$, is generated in order
$(t_1,q_3,t_2,t_3)$ by local groups of orders $(9,3,9,9)$.
The local maps are induced by the proved cup-product norm
square of \cite[III,Theorem3.1]{E_MilneCFT}; their global product
is \cite[V,Proposition5.2,Theorems5.3 and5.5]{E_MilneCFT}.
Existence of the class field and its prescribed splitting
comes from those exact idelic subgroups.

For $\lambda=1-\xi$, the absolute norm of $\lambda$ is three.
The arithmetic local reciprocity characters, with the same
global $\xi$ at all three tame places, are
\[
 \begin{aligned}
 \chi_q(f)
   &=-\frac{N_{F_q/\mathbb Q_3}(f)/3^{v_q(f)}-1}{9}
                                                    \pmod3,\\
 \chi_{t_i}(f)
   &=-\log_{\bar\xi_i}
       \left(\overline{f/(53\zeta)^{v_{t_i}(f)}}\right)^{312}
                                                    \pmod9.
 \end{aligned}
 \tag{E121.10}
\]
The expression in the first numerator is in $1+9\mathbb Z_3$.
The norm uniformizers are $\lambda$ and $53\zeta$ respectively;
the latter is the norm of $\beta_2$ in the cyclic-nine extension.
Arithmetic reciprocity acts on cyclotomic roots by the inverse
unit norm, which fixes the first sign. The tame symbol gives
the second. Both are evaluated using actual residue fields,
not an unspecified relabeling of their roots of unity.

The complete three-completed S-unit basis of the class-number-one
field $F$, certified in E.119, is
\[
 \begin{gathered}
 \xi,\ 1+\xi,\ 1+\xi^2,\ \xi^4-1,\ 
 -4+\xi^4+\xi^5,\ 
 3+2\xi+3\xi^2+3\xi^3-\xi^4+\xi^5,\ 
 -4-\xi+\xi^2-\xi^4.\\
 C_F=\begin{pmatrix}
 0&0&0&0&0&0&0\\
 3&6&3&6&0&0&0\\
 3&6&3&6&0&0&0\\
 3&6&3&6&0&0&0
 \end{pmatrix}
 \quad\text{in row order }(q_3,t_1,t_2,t_3).
 \end{gathered}
 \tag{E121.11}
\]
Their S-valuation columns are zero for the first three and
the four standard basis columns for the last four. Thus all
global relations have been included. In the generator order
$(t_1,q_3,t_2,t_3)$ the relation HNF and restriction to
$\operatorname{Gal}(B_2/F)$ are
\[
 H_F=\begin{pmatrix}9&0&0&3\\0&3&0&0\\0&0&9&3\\0&0&0&3\end{pmatrix},
 \qquad \rho_F=(1,3,1,1).
 \tag{E121.12}
\]
Their full Smith maps give
$\Gamma_F=C_9^2\oplus C_3^2$ and
$\ker\rho_F=C_9\oplus C_3^2$.
For example the latter has the following explicit representatives
and inverse coordinates:
\[
 R_F=\begin{pmatrix}12&-3&-11\\0&1&0\\-2&0&1\\-1&0&1\end{pmatrix},
 \qquad
 P_F=\begin{pmatrix}0&0&-1&1\\0&1&0&0\\0&0&-1&2\end{pmatrix}.
 \tag{E121.13}
\]
One checks $P_FR_F=I_3$, $\rho_FR_F\equiv0\bmod9$, and the
relations of moduli $(9,3,3)$ in both directions. At a prime
over $53$, the decomposition group in $H^S_{B_2}/F$ has
order nine, because $H^S_{B_2}/B_2$ is split there. It gives
an actual section of the cyclic restriction. If $A=A_{B_2}$,
the commutator subgroup of $A\rtimes\langle g\rangle$ is
$(g-1)A$. Consequently $\ker\rho_F=A_g$ with its actual
quotient map.

\emph{Exact normalizer and horizontal maps before any upper class deduction.}
Let $\Gamma_B$, $H_B$, $\rho_B$, and the generators
$(E_1,\ldots,E_6,G_1,G_2,G_3)$ be precisely those of
E119.21--26. The wild generators have the analytic prime order
$(q_0,q_1,q_2)$; the original prime-list order is transported
by its retained exact permutation. The actions on the six
local generators are the permutations
$g:(3,1,2,4,5,6)$ and $h:(2,3,1,6,4,5)$.
Both normalizers commute with $\sigma$, so the coefficient
on each transported local generator is one.

For every $G_i$ the program computes the literal ideal identity
$f(G_i)=(c_{f,i})\prod_jG_j^{C_{f,ji}}$ and verifies its full
prime factorization. In the class basis and local-character
basis just fixed, the matrices are
\[
 \begin{gathered}
 C_g=\begin{pmatrix}1&6&0\\1&1&0\\0&0&1\end{pmatrix},
 \quad C_h=\begin{pmatrix}4&3&3\\2&1&0\\2&0&1\end{pmatrix},\\
 X_g=\begin{pmatrix}0&1&0\\0&0&2\\1&2&1\\0&1&1\\0&0&1\\0&2&1\end{pmatrix},
 \quad
 X_h=\begin{pmatrix}2&0&2\\0&1&2\\2&2&2\\2&1&2\\1&2&0\\1&0&1\end{pmatrix},
 \qquad A_f=\begin{pmatrix}P_f&-X_f\\0&C_f\end{pmatrix}.
 \end{gathered}
 \tag{E121.14}
\]
The minus sign is the product formula for the principal idele
$c_{f,i}$. All its factors are literal algebraic elements,
and every rational prime in the factorization is proved prime.
The checks $H_B^{-1}A_fH_B\in M_9(\mathbb Z)$ and
$\rho_BA_f=\rho_B\bmod3$ prove descent and preservation
of the actual restriction kernel.

The actual ideal norm from $B_1$ to $L_1$ and ideal extension
back give the following maps on their idelic genus generators:
\[
 \begin{gathered}
 \mathcal N=
 \begin{pmatrix}
 1&1&1&0&0&0&-1&0&-1\\
 0&0&0&1&1&1&-1&-2&-2\\
 0&0&0&0&0&0&0&6&3\\
 0&0&0&0&0&0&1&0&0
 \end{pmatrix},\\
 \mathcal J=
 \begin{pmatrix}
 1&0&-2&-1\\1&0&0&-2\\1&0&-2&0\\
 0&1&0&0\\0&1&0&-2\\0&1&0&-1\\
 0&0&3&6\\0&0&1&0\\0&0&2&0
 \end{pmatrix}.
 \end{gathered}
 \tag{E121.15}
\]
For norms, every factor prime is contracted by evaluating the
actual embedded lower-field uniformizer at it; its exponent
is multiplied by the actual relative residue degree. For
extension, the embedded lower ideal generators generate the
upper ideal, whose full norm and principal correction are
verified. Hence these matrices are arithmetic maps.
Their unreduced identities are
$\mathcal N\mathcal J=3$ modulo the lower relation lattice and
$\mathcal J\mathcal N=1+A_h+A_h^2$ modulo the upper lattice.

The corresponding norm to the cyclic-nine presentation over
$F$ is
\[
 \mathcal P=
 \begin{pmatrix}
 0&0&0&3&0&0&-2&-3&-4\\
 1&1&1&0&0&0&-2&-2&-2\\
 0&0&0&0&3&0&-1&-3&-7\\
 0&0&0&0&0&3&-3&-3&-1
 \end{pmatrix}.
 \tag{E121.16}
\]
At three the local norm is the identity on each split
completion; at $53$ it includes $\langle g^3\rangle$ in
$\langle g\rangle$, giving the coefficient three.
The principal corrections of the three actual ideal norms
give the last three columns. Directly
$H_F^{-1}\mathcal PH_B$ is integral and
$\rho_F\mathcal P=3\rho_B\bmod9$.
Passing through the complete Smith maps gives exactly
(E121.6)--(E121.7), the projected norm
$\bar N(x)=(6x_0+3x_1+6x_2+3x_3,2x_0)$, and projected extension
$\bar j(r,s)=(3r,2r+s,2r+s,r)$.

All these calculations precede the conclusion about full
upper class groups. The ambient Smith forward formula is
$U_BK_B^{-1}$, integral on the actual lattice
$K_B\mathbb Z^9=\ker(\rho_B:\mathbb Z^9\to C_3)$.
The retained certificate encodes its ambient rational entries
exactly and verifies both inverse compositions. No division
in an ambient integer lattice is suppressed.

\emph{The finite-module argument closes the entire $B_2$ kernel.}
On the actual finite three-group $A=A_{B_2}$ put
$T=g-1$, $s=\sigma-1$, and $M=sA$.
The computed action on $A/M$ has $(G-I)^2=0$, hence
$T^2A\subset M$. The lower $g$-action on $A_{B_1}$ is trivial:
E.119 proves this using its actual quadratic norm/extension
and $cgc=g^{-1}$, and (E121.14) independently checks it on
the generating genus columns.
Functoriality of actual ideal norm and extension therefore gives
\[
 \begin{gathered}
 T(1+\sigma+\sigma^2)A=Tj_BN_BA=0,\qquad
 3TA=-T(3+s)M,\\
 M=(T^3+3T^2+3T)A
      \subset TM+3M+T(3+s)M\subset(3,T)M.
 \end{gathered}
 \tag{E121.17}
\]
Here $j_BN_B=1+\sigma+\sigma^2$ is the literal product of
the conjugate ideals, not an abstract module identification.
Choose $e$ with $3^eA=0$. Since $g^9=1$,
$T^9\in3\mathbb Z_3[g]$. Every monomial of total degree
$9e$ in $(3,T)$ is consequently divisible by
$3^{a+\lfloor b/9\rfloor}$ with $a+b=9e$, and that exponent
is at least $e$. Thus $(3,T)^{9e}A=0$.
Iterating (E121.17) gives $M=0$. This proves the full
$A_{B_2}$ assertion, with all E.119 quotient maps now
the full class maps. In particular $j_B$ has exactly the
diagonal kernel stated above. The matrices $G,H$ are now
the full actual normalizer actions.

\emph{The positive connecting class determines $A_{L_2}$.}
The cubic $B_2/L_2$ is unramified and split at S.
Indeed it adjoins $\xi$; at three $L_2$ already has its
$\mathbb Q_3(\zeta_{27})$ completion, and at $53$ the
residue field contains $\mu_9$.
Thus $B_2\subset H^S_{L_2}\subset H^S_{B_2}$.
The maximal subfield of $H^S_{B_2}$ abelian over $L_2$
is exactly $H^S_{L_2}$, by these actual local conditions.
For a cyclic quotient generated by a lift of $h$, the
commutator subgroup is $(h-1)A_{B_2}$. The ideal
norm/Frobenius square of \cite[V,Proposition3.3]{E_MilneCFT}
therefore gives the exact sequence
\[
 0\longrightarrow(A_{B_2})_h
   \xrightarrow{\,N_h\,} A_{L_2}
   \xrightarrow{\operatorname{Art}_{B_2/L_2}}C_3
   \longrightarrow0,\qquad |A_{L_2}|=3\cdot27=81.
 \tag{E121.18}
\]
On the E.119 quotient $Q_L$ its last map is the first
coordinate modulo three. This is also the restriction of
the actual $B_1/L_1$ character, whose lower idele row is
$(0,0,2,0)$ in E.119.

For the connecting class choose the actual inertia lift
$\sigma_0$ at the first $53$-prime in $H^S_{B_2}/B_1$.
It has order three and its image in $\Gamma_B$ is $E_4$.
Let $h_0$ lift $h$ while fixing $L_2$. With commutator
$[x,y]=xyx^{-1}y^{-1}$, the image of
$[\sigma_0,h_0]$ in $\Gamma_B$ is
$E_4-A_hE_4=E_4-E_6$.
Its exact Smith coordinate is $(3,0,0,0)$.
Changing either lift changes the class by $(h-1)A_{B_2}$
or $(\sigma-1)A_{B_2}$, which are precisely the subgroups
being quotiented. Thus the homology connecting map sends
the positive $\sigma\otimes h$ to $[3e_0]$.
This element is nonzero in $(A_{B_2})_h$.

Write $u=N_h(e_0)$. The relations from $(H-I)A_{B_2}$ are
$e_2=-3e_0-e_1$ and $e_3=-3e_0-2e_1$, so $u$ has order
nine. Since $\sigma=1$ on $A_{B_2}$, the image in
(E121.18) is fixed by $\sigma$. The quotient $Q_L$ has order
$27$, so $(\sigma-1)A_{L_2}$ has order three.
The connecting calculation gives exactly
$(\sigma-1)A_{L_2}=\langle3u\rangle$.
Its square is zero and it is killed by three.
Consequently the actual vertical trace is
$1+\sigma+\sigma^2=3$ on $A_{L_2}$.
As $A_{L_1}$ has exponent three, $j_LN_L=3$ implies
$9A_{L_2}=0$.
Furthermore $(\sigma-1)A_{L_2}\subset3A_{L_2}$, so
$A_{L_2}/3A_{L_2}\simeq Q_L/3Q_L$ has dimension two.
These order, exponent and generator constraints prove
$A_{L_2}=C_9^2$.

Choose $a$ with $p_L(a)=(1,1)$. Its Artin value is one,
so $\sigma a=a+3u$. The two classes $u,a$ are independent
modulo three: $u$ is primitive of order nine and has Artin
value zero, whereas $a$ has value one. They therefore give
the claimed basis. Put $v=N_h(e_1)$. From the projected
maps, $v=3ku+3a$ for some $k\bmod3$.
The actual identity $N_hj_h(a)=3a$, with
$j_h(a)=(3,0,0,1)$, now gives
$-6ku+3a=3a$ and hence $k=0$.
Thus the two exact power relations are
\[
 3a=N_h(e_1),\qquad
 \sigma a-a=3u.
 \tag{E121.19}
\]
They prove all full horizontal matrices in (E121.3).
The lower norm square gives $N_L(u)=(0,2)$.
Applying the actual projected norm of E.119 to
$p_L(a)=(1,1)$ gives $N_L(a)=(2,0)$.
It is onto; alternatively, onto-ness follows directly from
E.119's onto quotient norm. Its kernel is $3A_{L_2}$:
the target has exponent three, while both $\ker N_L$ and
$3A_{L_2}$ have order nine.
The actual trace identity gives the precise rule
$j_L(b)=3a$ for any lift $a$ with $N_L(a)=b$.
Changing that lift by $3A_{L_2}$ changes $3a$ by zero,
since $9A_{L_2}=0$. This rule yields (E121.4), and its
kernel is zero. All norm/extension squares and both
compositions are verified on the full finite groups.
The ambiguity $a\mapsto a+3ku$ gives the literal coordinate
shear $(r,s)\mapsto(r+3ks,s)$; it leaves every displayed
map unchanged with its stated source and target moduli.

\emph{The normal closure and its Artin character.}
Put $\alpha_2=53^{1/9}$ and $\eta=\zeta_{27}$, so
$\beta_2=\alpha_2\eta$. The literal inverse formulas
$\alpha_2=(\beta_2\overline{\beta_2})^5/53$ and
$\eta=\beta_2/\alpha_2$ identify the compositum in (E121.8).
Its degree is $162$, by the $53$-valuation and the cyclotomic
degree. On $C$, use
$a_0(\alpha_2)=\xi\alpha_2$, $a_0(\eta)=\eta$, and
$b_0(\alpha_2)=\alpha_2$, $b_0(\eta)=\eta^4$.
Both have order nine and $b_0a_0b_0^{-1}=a_0^4$.
The subgroup fixing $B_2$ is generated by
$a_0^{-3}b_0^3$, and the conjugate subgroup is generated
by $a_0^3b_0^3$. Their intersection is trivial and the group
they generate fixes $B_1$. These literal subgroup maps
prove the intersection assertion. They also show exactly
why complex conjugation does not act on $B_2$ itself.

The completions of $C$ and $B_2$ agree at each place of S:
at three they are the stated cyclotomic completion, and
at $53$ the residue field contains $\mu_{27}$ because
$v_3(53^2-1)=3$. The discriminants have no other finite
ramification, so $C/B_2$ is unramified and S-split.
In the presentation (E121.12) its map to
$\operatorname{Gal}(C/F)=C_9\oplus C_3$ is
$(t_1,q_3,t_2,t_3)\mapsto(t_1+t_2+t_3,q_3)$.
Restriction to $B_2$ is $(A,B)\mapsto A+3B\bmod9$.
On its kernel the positive generator is
$a_0^{-3}b_0^3$ and the character is $B$.
Composing this actual map with (E121.16) and the E.119
Smith representatives gives exactly $\psi_C$ in (E121.8).

\emph{Actual unit norm subgroups and completion.}
For any of the three cyclic extensions $E/D$ here, write
$\tau$ for its positive generator. Outside S the extension
is unramified. For $u=Nx\in U_D$, choose an outside-S divisor
$D_x$ with
$\operatorname{div}_{\notin S}(x)=(\tau-1)D_x$.
Such a divisor exists orbit by orbit from the zero norm of
the divisor of $x$. The literal map is
\[
 \frac{U_D\cap N E^\times}{N U_E}
 \xrightarrow{\ \nu\ }
 \frac{A_E^\tau}{jA_D},\qquad
 Nx\longmapsto\operatorname{pr}_3[D_x]\bmod jA_D.
 \tag{E121.20}
\]
Here $\operatorname{pr}_3$ is the canonical projection of the finite
S-class group to its three-primary subgroup. On its prime-to-three
part, an invariant class is extended from the base because
$jN=1+\tau+\tau^2=3$ there and multiplication by three is
invertible. Hence the omitted invariant quotient is zero.
Changing $x$ by a norm-one element uses Hilbert90 and changes
$D_x$ by a principal divisor and an extended base divisor.
Conversely an invariant ideal class supplies a representative
$D$ for which $(\tau-1)D$ is principal; a generator $x$
has $Nx\in U_D$. These constructions are inverse.
This is the actual ideal/Hilbert90 map of
\cite[Proposition1 and its full ideal proof]{E_LemmermeyerAmbiguous},
with the splitting convention at S retained.

In the three cases its right side is respectively
$A_{B_2}/\langle3e_0\rangle=C_3^4$,
$A_{L_2}^{\sigma}/3A_{L_2}=C_3$,
and $A_{B_2}^{h}/j_hA_{L_2}=C_3$.
Explicit quotient coordinates are
$(x_0\bmod3,x_1,x_2,x_3)$ in the first,
$r\bmod3$ on a fixed class $(r,3s)$ in the second, and
$r-s\bmod3$ on a fixed class $(3r,t,t,s)$ in the third.
E.119 evaluates the first field-norm index as nine and the
second as one. In the unramified S-split horizontal extension
every S-unit is a local norm, hence a field norm by the
complete cyclic Hasse norm theorem
\cite[VIII,Theorem3.1]{E_MilneCFT}.
Multiplying these exact indices proves (E121.9).
Each finite quotient is killed by three because the included
base unit has norm its cube. Its order therefore gives the
stated elementary abelian type.

For comparison, the capkernel/unit-Herbrand maps of E119.16
give the same indices: the S-unit Herbrand quotients are
$3^5$, $3$, and $1/3$, and the actual capitulation orders
are $3$, $1$, and $9$. The precise lattice quotient is
\cite[VII,Proposition3.1]{E_MilneCFT}.
These are compatible checks of the same norm subgroup.

The completed unit ranks are $14,32,4,10$ for
$B_1,B_2,L_1,L_2$ respectively. Their three-primary roots
of unity are $\mu_9,\mu_9,\mu_3,\mu_3$:
$\mu_{27}\not\subset B_2$ by the actual cubic compositum,
and $\mu_9\not\subset L_2$ because $[B_2:L_2]=3$.
The vertical root norms are cubing. Horizontally
$N_h(\xi)=\xi^{1+4+7}=\zeta$.
Thus every completed kernel has exactly the displayed
literal $\mu_3$ torsion and the rank difference in (E121.9).
For each of these actual kernels $K$, choose a $\mathbb Z_3$-basis
of the free quotient $K/\mu_3$ and lifts $k_1,\ldots,k_r\in K$.
The displayed direct-sum isomorphism is the continuous map
$(z,(a_i))\mapsto z\prod_i k_i^{a_i}$.
Its inverse reads the quotient-basis coordinates $(a_i)$ and
then divides the input by $\prod_i k_i^{a_i}$ to obtain
$z\in\mu_3$. These two constructions compose to the identity.
A different quotient basis is an actual $\mathrm{GL}_r(\mathbb Z_3)$
coordinate change; a different lift multiplies $k_i$ by
a specified element of $\mu_3$ and changes the torsion coordinate
by the inverse product of those elements to the powers $a_i$.
Thus the choice ambiguity is explicit without assigning an
uncomputed numerical upper unit basis.
Finite-rank unit groups complete exactly, and all norm
images have the proved finite index, so the same finite
quotients and actual images persist under completion.

The five GP stages use only the immutable, already certified
E.119 lower-field objects. They prove each ideal relation,
local character and prime contraction; the separate exact
Python certificate verifies every Smith inverse, all finite
class maps, the positive connecting class and the complete
field subgroup comparison. No upper BNF certification is
used. The retained earlier interrupted attempts supply no
additional class-group assertion.
\end{proof}
\begin{thebibliography}{9}
\bibitem{E_MilneCFT} J. S. Milne, \emph{Class Field Theory}, version4.03, 2020.
\bibitem{E_LemmermeyerAmbiguous} F. Lemmermeyer, \emph{The Ambiguous Class Number Formula Revisited}, arXiv:1309.1071, 2013.
\bibitem{E_PARICertifiedUnits} The PARI Group, \emph{PARI/GP2.19.0 User's Guide}, \texttt{bnfcertify}, and official source \texttt{buch3.c}.
\end{thebibliography}\end{document}
