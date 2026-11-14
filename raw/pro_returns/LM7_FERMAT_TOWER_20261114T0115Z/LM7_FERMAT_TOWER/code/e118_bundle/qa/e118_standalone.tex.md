\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[a4paper,margin=27mm,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools}
\usepackage{array,booktabs,longtable,tabularx,enumitem,graphicx}
\usepackage{xcolor,microtype}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,
 urlcolor=blue!45!black,pdftitle={LM7: The Fermat tower in the metabelian approximation},
 pdfauthor={GPT-6 Astra, OpenAI, ChatGPT Pro mode}}
\urlstyle{same}
\setlength{\parindent}{1.3em}
\setlength{\parskip}{.22em}
\setlength{\emergencystretch}{2em}
\setlength{\LTpre}{.6em}
\setlength{\LTpost}{.6em}
\setlist{nosep}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{1}
\allowdisplaybreaks[2]
\newenvironment{statement}[3]{%
 \par\addvspace{1.1em}\phantomsection\label{st:#1}%
 \noindent\textbf{#1. #3}\quad\textsf{\small[#2]}\par\nobreak\smallskip\ignorespaces
}{\par\smallskip}
\newcommand{\statementref}[1]{\hyperref[st:#1]{#1}}
\newcommand{\Sha}{\mathop{\mathrm{Sh}}}
\begin{document}
\subsection{A numerical mixed quartic obstruction and its complete compact slice}

\begin{statement}{E.118}{Proved}{An explicit Kummer field and the index-$125$ compact slice at $3121$}
Retain the actual plus-quartic extension, its class-two origin,
the coefficient maps $A=W\oplus j(V^3)$, and its geometric
conjugacy convention from E.115. Here $V=T_5E_+$ for
$E_+:y^2=x^3+x$, $R=\mathbb Z_5$, and
$S=\{2,5,\infty\}$. We construct below an actual nonzero
class $h_1\in H^1(G_{\mathbb Q,S},E_+[5])$ by two explicit
algebraic units and corestriction. Its finite arithmetic image is
\[
 G_{\mathbb Q,S}\longrightarrow E_+[5]\rtimes
                \operatorname{Gal}(\mathbb Q(E_+[5])/\mathbb Q),
 \qquad g\longmapsto(h_1(g),\rho_5(g)),
 \quad |\operatorname{im}|=25\cdot32=800.
 \tag{E118.1}
\]
Its kernel fixes the explicitly specified Kummer field in
(E118.7). The integral generators $[h]\in H^1(G_{\mathbb Q,S},V)$
reducing to $h_1$ form one orbit under multiplication by
$1+5\mathbb Z_5$. Every such generator has exact local
Kummer order five at $p=3121$:
\[
  \#E_+(\mathbb F_{3121})=3200,
  \qquad E_+(\mathbb F_{3121})\{5\}=E_+[5],
  \qquad m_{3121}=1.
 \tag{E118.2}
\]
The chosen residue-field basis of $E_+[5]$ gives the
literal value $h_1(F_{3121})=(3,1)$ for arithmetic Frobenius.
The exact basis and the prolongation are specified below.

Put
\[
 b=\kappa_5(3121)\sum_{i=0}^{3}e_{A_i}\in Z^1(G_{\mathbb Q},W).
 \tag{E118.3}
\]
This is E.108's toric input $(3121,1,1)$ with its original
Kummer marking. The complete compact slice of the class-two
section image over $[b]$ is
\[
 \left\{\mathbf r\in R^3:
     [b]+\sum_{i=1}^3r_i j_i[h]\text{ lifts}\right\}=5R^3.
 \tag{E118.4}
\]
Thus this slice has index $125$ in the full compact input
lattice. Its toric input and every pure compact input separately
lift. In particular the combined input with
$\mathbf r=(1,0,0)$ has no class-two lift. Every nonempty
fibre in (E118.4) is the full torsor (E115.6), with its
coefficient maps and inverse ratio coordinates. The exclusion
passes through each actual higher quotient mapping to this
intrinsic class-two extension. Scalar extension of this lattice is
the isomorphism
\[
 (5R^3)\otimes_R\mathbb Q_5\longrightarrow\mathbb Q_5^3,
 \quad (5\mathbf s)\otimes\lambda\longmapsto5\lambda\mathbf s,
 \qquad
 \mathbf q\longmapsto\sum_{i=1}^3(5e_i)\otimes(q_i/5).
\]
The actual rational compact slice over the image of $[b]$
is all of $\mathbb Q_5^3$, as proved below using the correcting
cochains of E.115.

All field maps, both algebraic units and their inverses,
the residual group, the complete point count, the torsion
basis and the Weil pairing are checked by the attached
programs. The numerical witness uses the actual global
Kummer class. The manuscript anchor is \S51.16, folios
733v--736v, scans 172--178, equations (371)--(379), and
Part E(c),(d) and follow-up 4.
\end{statement}

\begin{proof}
\emph{Actual units and character fields.}
Let $K=\mathbb Q(i)$ and choose complex roots
\[
 a^4=-1-2i,\qquad b_0^4=-1+2i,\qquad
 a=\overline{b_0},\qquad t=ab_0=5^{1/4}>0.
 \tag{E118.5}
\]
The subscript on $b_0$ keeps this algebraic number separate
from the toric cocycle (E118.3). Put
$L=K(a,b_0)$. The exact point maps of E.112 identify
$L=\mathbb Q(E_+[5])$. For clarity we check them again:
\[
 \begin{gathered}
 y_+=\frac{1+i}{2-i}a,\quad
 y_-=\frac{1-i}{2+i}b_0,\qquad
 P_+=\left(\frac{5y_+^2}{4+2i},y_+\right),\quad
 P_-=\left(\frac{5y_-^2}{4-2i},y_-\right),\\
 [2]P_+=[i]P_+,\qquad [2]P_-=[-i]P_-.
 \end{gathered}
 \tag{E118.6}
\]
Both points have order five and give distinct eigenspaces;
therefore they are a basis. Their coordinates generate $a,b_0,i$:
the ratio $y_+^2/x_+=(4+2i)/5$ gives $i$, and the two
nonzero $y$ coordinates then give $a,b_0$. These are literal
inverse field maps. The compositum of
$X^8+2X^4+5$ and $X^4-5$ has degree $32$.
The certificate supplies the irreducible compositum polynomial
and all three inverse polynomials in $\theta=t-b_0$,
checking $\theta=ab_0-b_0$ after substitution.
It also checks all $32$ distinct field embeddings and
their three generating point actions.

On the degree-eight field $K(b_0)$ define the units
\[
 \begin{aligned}
 u={}&\tfrac14(b_0^7-4b_0^6-7b_0^5-2b_0^4
                  +9b_0^3+2b_0^2-11b_0-16),\\
 w={}&\tfrac14(3b_0^7-3b_0^6+3b_0^5-b_0^4
                  +5b_0^3-b_0^2-3b_0+9),\\
 u^c={}&u(a),\qquad
 \mathcal B=L(u^{1/5},(u^c)^{1/5}).
 \end{aligned}
 \tag{E118.7}
\]
Their exact monic polynomials are respectively
\[
 \begin{aligned}
 T^8+28T^7+170T^6-484T^5+892T^4
                -824T^3+314T^2+32T+1,\\
 T^8-20T^7+108T^6-4T^5+22T^4
                -44T^3+12T^2+4T+1.
 \end{aligned}
\]
Substitution modulo $X^8+2X^4+5$ proves both equations.
Their constant terms prove that the elements are units;
the full polynomial inverse of $u$ is also retained.
For $\tau_b(b_0)=ib_0$, $\tau_b(i)=i$, the exact identity is
\[
                       \tau_b(u)=w^5u^3.
 \tag{E118.8}
\]
This identity is checked twice, over exact rational
polynomial quotients by GP and independently by Python.

Let $\tau_a$ act by $a\mapsto ia$ and fix $b_0,i$.
On the ordered basis $(P_+,P_-)$ the three generators
$\tau_a,\tau_b,c$ act by
\[
 A=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad
 B=\begin{pmatrix}1&0\\0&3\end{pmatrix},\qquad
 C=\begin{pmatrix}0&1\\1&0\end{pmatrix}
                    \quad\text{over }\mathbb F_5.
 \tag{E118.9}
\]
They generate the actual order-$32$ group $\Gamma$.
The determinant is the action on
$\zeta=e_5(P_+,P_-)\in\mu_5(L)$.
Identity (E118.8) says that the unit class $[u]$ has
characters $1,3$ under $\tau_a,\tau_b$ respectively.
The class $[u^c]$ has characters $2,1$.
Indeed $c\tau_a c=\tau_b^{-1}$, and the exponent
inverse of three modulo five is two. All these maps
are on the actual fields (E118.5), with the displayed
point basis; no abstract character identification replaces them.

\emph{A global cocycle with an explicit finite field.}
The extension $L/\mathbb Q$ is unramified outside $2,5$
by E.112's actual division-field calculation. Both units
in (E118.7) have zero divisor. The equations adjoining
their fifth roots are etale away from five, so
$\mathcal B/\mathbb Q$ is unramified outside $S$.
Write $G_L=\operatorname{Gal}(\mathbb Q_S/L)$, where
$\mathbb Q_S$ is the maximal extension unramified outside $S$.
For chosen fifth roots, define the continuous Kummer logarithms
\[
 \frac{g(u^{1/5})}{u^{1/5}}=\zeta^{k_u(g)},\qquad
 \frac{g((u^c)^{1/5})}{(u^c)^{1/5}}=\zeta^{k_{u^c}(g)},
 \qquad
 H(g)=k_u(g)P_+-k_{u^c}(g)P_-\quad(g\in G_L).
 \tag{E118.10}
\]
They are homomorphisms on $G_L$, since $G_L$ fixes $\mu_5$
and the point basis. Changing either fifth root has no
effect on them. For $\tau_a$ the ordered logarithms on
$\tau_a^{-1}g\tau_a$ are $(3k_u(g),k_{u^c}(g))$;
for $\tau_b$ they are $(k_u(g),2k_{u^c}(g))$.
For $c$ they are $(-k_{u^c}(g),-k_u(g))$.
These assertions follow by dividing the unit character
by the cyclotomic character. Combining them with
(E118.9) proves $H(\gamma g\gamma^{-1})=\gamma H(g)$
for every $\gamma\in G_{\mathbb Q,S}$.

Here is a literal descent map. Choose left coset
representatives $t_1,\ldots,t_{32}$ for $G_L$ in
$G_{\mathbb Q,S}$. Write $gt_i=t_{j(g,i)}k(g,i)$,
with $k(g,i)\in G_L$, and put
\[
 h_1(g)=3\sum_{i=1}^{32}t_{j(g,i)}H(k(g,i)).
 \tag{E118.11}
\]
The coset multiplication identity proves the cocycle
identity term by term. On $G_L$ this equals $H$, because
$3\cdot32=1$ in $\mathbb F_5$ and $H$ is equivariant.
Its cohomology class is independent of the representatives.
For $t_i'=t_i\ell_i$, $\ell_i\in G_L$, put
$v=3\sum_i t_iH(\ell_i)$; direct substitution gives
$h_1'(g)-h_1(g)=gv-v$. Thus the ambiguity is exactly
this abelian coboundary. Equivalently, restriction and $3$ times
corestriction are inverse on these invariant classes;
averaging by $1/32$ proves the vanishing of all positive
$\Gamma$-cohomology with these coefficients.

The residue computation below proves $[u]\ne0$ in
$K(b_0)^\times/K(b_0)^{\times5}$. Its image in
$L^\times/L^{\times5}$ is also nonzero. In fact, for
$x\in L$ with $x^5=u$, the actual norm to $K(b_0)$
would give $(u/Nx)^5=u$, since $[L:K(b_0)]=4$.
This supplies the needed injectivity on this class.
Conjugation gives nonzero $[u^c]$. Their distinct
$\tau_a$ characters prove independence: applying
$\tau_a-1$ to a relation kills the $[u]$ coefficient
and preserves the $[u^c]$ coefficient by the unit
$2-1$. Kummer theory therefore gives
$\operatorname{Gal}(\mathcal B/L)\simeq C_5^2$,
with coordinates exactly (E118.10).
The displayed character maps and conjugation preserve
their span, so $\mathcal B/\mathbb Q$ is normal.
The homomorphism (E118.1) has this full translation
kernel and quotient $\Gamma$, proving its order and
surjectivity onto the stated semidirect product. Its
kernel is exactly $G_{\mathcal B}$.

By E.112, reduction identifies
$H^1(G_{\mathbb Q,S},V)/5$ with
$H^1(G_{\mathbb Q,S},E_+[5])\simeq\mathbb F_5$.
Thus (E118.11) lifts to an integral generator $[h]$.
For one such choice, every other lift is
$(1+5z)[h]$, $z\in\mathbb Z_5$, because the integral
group is free of rank one. This states the complete
choice ambiguity used in the theorem.

\emph{The exact prime and local order.}
Use the degree-one place of $L$ at $p=3121$ specified by
\[
 i\longmapsto79,\qquad a\longmapsto1285,\qquad
 b_0\longmapsto339\quad\text{in }\mathbb F_{3121}.
\]
These values satisfy every relation in (E118.5).
The prime splits completely in $L$: its decomposition
group fixes this degree-one residue field, and $L$
is Galois and unramified at $p$. At this place
\[
 \begin{gathered}
 P_+=(2413,1867),\qquad P_-=(2700,2101),\qquad
 e_5(P_+,P_-)=190,\\
 u\longmapsto1362,\quad u^c\longmapsto1576,\\
 1362^{624}=2163=190^3,\quad
 1576^{624}=2119=190^4\pmod{3121}.
 \end{gathered}
 \tag{E118.12}
\]
The nontrivial first fifth residue proves the nonzero
unit class used above. Arithmetic Frobenius on a fifth
root has ratio $u^{(p-1)/5}$ in this residue field;
therefore (E118.10)--(E118.11) give $(3,-4)=(3,1)$.
This value is independent of the cocycle representative,
since Frobenius acts identically on $E_+[5]$.
The chosen prolongation above $L$ can vary by its
abelian Kummer inertia-free decomposition group;
these two Frobenius logarithms remain the displayed ones.

An independent enumeration of all $3121$ possible
$x$ coordinates gives $3200$ points including infinity.
The two displayed points have order five and their
$25$ linear combinations are distinct. Thus the full
five-primary group has exponent five and order $25$.
The certificate computes the Weil pairing both by GP
and by an independent Miller line calculation with its
alternating sign. This fixes the normalization in
(E118.12).

For the actual integral Frobenius $F$, reduction is
$F\equiv1\pmod5$ and $\det(F-1)=\#E_+(\mathbb F_p)$.
Hence $F-1=5D$ with $D\in\mathrm{GL}_2(\mathbb Z_5)$.
The nonzero reduction $(3,1)$ proves that
$h(F)$ is primitive. Consequently
$(F-1)^{-1}h(F)=\tfrac15D^{-1}h(F)$ has exact denominator
five modulo $V$. This proves $m_p=1$ by the actual
boundary map of E115.23. The argument needs no value
for the uncomputed matrix $D$.

\emph{The entire mixed slice.}
Finally $3121\equiv1\pmod8$, $v_5(3120)=1$, and
$1623^5\equiv2\pmod{3121}$. The toric input (E118.3)
therefore satisfies all peripheral tests by the exact
tame-symbol calculation in the last paragraph of E.115.
Its outside-$S$ inertia is zero away from $3121$ and
is the primitive vector $\sum e_{A_i}$ there.
The scalar mixed criterion (E115.5) is consequently
$\min_i v_5(r_i)\ge1$ for a nonzero compact vector.
The zero compact vector also lifts. The restricted
convergence condition holds because the mixed support
is a single prime. This proves both directions of
(E118.4), its index, and every fibre statement through
the actual maps of E.115. The displayed tensor map sends
$(5e_i)\otimes1$ to $5e_i$, and composing it with the
displayed inverse in either order fixes this basis and all
scalars; hence both maps are inverse $\mathbb Q_5$-linear maps.
For every rational compact vector $\mathbf q\in\mathbb Q_5^3$,
the actual mixed correction is
$v_{3121}\wedge j_{\mathbf q}(F-1)^{-1}h(F)$ at $3121$
and zero at every other prime outside $S$. This family
has finite support and a common finite denominator. The
rational cochain inverse of E.115 therefore gives a lift for
each $\mathbf q$. This proves the asserted rational slice
through the actual coefficient-extension and correction maps.

The GP and Python certificates retain the exact unit
identities, full field inclusions, all residual group
products, complete point count, independently computed
pairing and both Kummer logarithms. The original
eigenunit search and its actual successful output are
preserved as the record of how this explicit input was found.
\end{proof}

\end{document}
