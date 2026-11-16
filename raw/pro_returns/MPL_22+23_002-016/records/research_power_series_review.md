# Post-freeze algebra review: the power-series obstruction and two field examples

This record concerns the frozen readings of cote 22, scans 023–025 and 027–029, and supports notes A20–A22, A25 and A28 in `research_algebra.md`. It does not change a page transcription. The fixed transcription freeze is 2026-11-16 23:06:31 UTC; the supplied context was first opened at 23:06:38 UTC. The calculations below are a research review of the displayed algebras, without a claim of novelty.

## 1. The two bases and the two maps on scan 024

The frozen proposition, lines 3–8 of `pages/MPL_22+23_002-016_22_scan024.tex`, reads with the existing reading marker:

> “sur $K$ \unsure{relativement} à $k$, et à fortiori n'est pas f$^t$ simple sur $k$.”

Its displayed algebra is $A=K[[t_1,\ldots,t_n]]$, with $n>0$ and $\dim_K\Omega_{K/k}$ infinite. Write $\mathfrak m=(t_1,\ldots,t_n)$ and use the actual maps

\[
k\longrightarrow K\xrightarrow{\iota}A\xrightarrow{\varepsilon}K,
\qquad
\iota(a)=a,
\qquad
\varepsilon\!\left(\sum_\nu a_\nu t^\nu\right)=a_0,
\qquad \varepsilon\iota=1_K.
\]

The map explicitly tested in the manuscript is

\[
\alpha:\Omega_{K/k}\otimes_KA\longrightarrow\Omega_{A/k},
\qquad da\otimes f\longmapsto f\,d_Aa.
\]

An $A$-linear left inverse to $\alpha$ is exactly a $k$-derivation $D:A\to\Omega_{K/k}\otimes_KA$ restricting to $d_{K/k}$ on $K$: the universal property sends a linear map $r$ to $r\circ d_A$, and the identity $r\alpha=1$ is the restriction condition. The manuscript's finite-dimensional quotient followed by its diagonal series disproves the existence of this $D$.

The lift being obstructed can be written without relying on the supplied edition's inconsistent arrow labels. Put $M=\Omega_{K/k}\otimes_KA$ and give $E=A\oplus M$ its square-zero multiplication $(a,m)(b,n)=(ab,an+bm)$ and its $K$-algebra structure $c\mapsto(c,d_{K/k}c\otimes1)$. The projection $E\to A$ has a $k$-algebra section $a\mapsto(a,0)$, and a $K$-algebra section would have the form $a\mapsto(a,D(a))$ with exactly the forbidden derivation. This is the relative $K/k$ lifting problem of `context/ega_fr/EGA_chap0_ega0-19.tex`, 0.19.9.1, and also an ordinary $K$-algebra lifting problem. It proves the failure over the coefficient field $K$ recorded in the Hua summaries.

The final phrase on scan 024 concerns the smaller base $k$. The following calculation proves that conclusion for this same $A$ by establishing that $\Omega_{A/k}$ is not projective. It supplies an additional projectivity argument beyond the manuscript's displayed computation of $\alpha$.

## 2. Exact residue-fibre isomorphism

Set $P=\Omega_{A/k}$, with universal derivation $d:A\to P$. The precise residue-fibre isomorphism is

\[
\Phi:P\otimes_AK\xrightarrow{\sim}\Omega_{K/k}\oplus K^n,
\qquad
df\otimes1\longmapsto
\bigl(d_{K/k}(a_0),a_{e_1},\ldots,a_{e_n}\bigr)
\tag{1}
\]

for $f=\sum_\nu a_\nu t^\nu$. On the right the $A$-action is through $\varepsilon$, and the last $n$ coordinate vectors are denoted by $dt_j$.

Here is a direct verification. Every $k$-derivation from $A$ into an $A$-module annihilated by $\mathfrak m$ kills $\mathfrak m^2$, since each term $D(uv)=uD(v)+vD(u)$ vanishes for $u,v\in\mathfrak m$. Thus it is determined by its restriction to $K$ and the $n$ values $D(t_j)$, with

\[
D(f)=D(a_0)+\sum_{j=1}^n a_{e_j}D(t_j).
\]

The formula on the right side of (1) is itself a $k$-derivation with that residue-field action: the constant and linear coefficients of a product satisfy the Leibniz rule. It induces $\Phi$. Its inverse sends $d_{K/k}a$ to $d_Aa\otimes1$ and the $j$th standard basis vector to $dt_j\otimes1$; the equality $f-a_0-\sum_j a_{e_j}t_j\in\mathfrak m^2$ verifies both compositions. In particular, the classes of $d_AK$ span an infinite-dimensional subspace of $P/\mathfrak mP$.

## 3. Finite free coordinates and the diagonal series

We prove that a free-module representation $P=\bigoplus_{i\in I}Ae_i$ is impossible. In such a representation the finitely many elements $dt_1,\ldots,dt_n$ together have support in a finite subset $S\subset I$. Let

\[
q:P\longrightarrow F=\bigoplus_{i\in I\setminus S}Ae_i
\]

be the projection deleting these coordinates, and put $\delta=q\circ d$. Then $\delta(t_j)=0$ for every $j$. By (1), the $K$-span of the image of $\delta(K)$ in $F/\mathfrak mF$ is infinite-dimensional: passage through $q$ removes at most $|S|$ dimensions from the residue fibre.

For each $i\in I\setminus S$, write $\delta_i:A\to A$ for the coordinate derivation. It kills all parameters. Every element of $\mathfrak m^N$ is a finite sum of expressions $t^\nu g_\nu$ with $|\nu|=N$, and

\[
\delta_i(t^\nu g_\nu)=t^\nu\delta_i(g_\nu),
\qquad
\delta_i(\mathfrak m^N)\subset\mathfrak m^N.
\tag{2}
\]

Equation (2), derived from the Leibniz rule, supplies the continuity needed below. There is no assumption that an arbitrary derivation on a series algebra can be applied to an infinite sum term by term.

Choose $a_r\in K$ and $i_r\in I\setminus S$ recursively. At stage $r$, the supports of $\delta(a_0),\ldots,\delta(a_{r-1})$ form a finite set $S_r$. The infinite-dimensional residue image supplies $a_r$ and a coordinate $i_r\notin S_r$ with

\[
u_r:=\varepsilon(\delta_{i_r}(a_r))\ne0.
\tag{3}
\]

Each $i_r$ is new, because every earlier $i_s$ belongs to the support of $\delta(a_s)$. For the actual element

\[
f=\sum_{r\ge0}a_rt_1^r\in A,
\]

the truncation remainder after term $r$ lies in $\mathfrak m^{r+1}$. Using (2), the vanishing of all earlier $\delta_{i_r}(a_s)$ by the choice of $i_r$, and (3), gives

\[
\begin{aligned}
\delta_{i_r}(f)
&\equiv\sum_{s=0}^{r}t_1^s\delta_{i_r}(a_s)
\equiv t_1^r\delta_{i_r}(a_r)
\equiv u_rt_1^r
\not\equiv0\pmod{\mathfrak m^{r+1}}.
\end{aligned}
\tag{4}
\]

Thus $\delta(f)$ has infinitely many nonzero coordinates, contradicting $\delta(f)\in F$, a direct sum. This proves that $P$ is not free.

The ring $A$ is local, so Kaplansky's freeness result for projective modules, checked in the Stacks Project, Theorem 10.85.4, [Tag 0593](https://stacks.math.columbia.edu/tag/0593), now excludes projectivity of $P$. The projectivity requirement for the differentials of a discretely formally smooth algebra is stated in the supplied `EGA_chap0_ega0-20.tex`, 0.20.4.9, and its discrete specialization follows directly from `EGA_chap0_ega0-19.tex`, Definition 0.19.2.1, by taking the open ideal $0$. It is also stated in Stacks Proposition 10.138.8(6), [Section 00TH](https://stacks.math.columbia.edu/tag/00TH). Therefore the algebra on scan 024 fails discrete formal smoothness over $k$.

There is also an explicit ordinary $k$-algebra lifting problem at this last step. Let $G=\bigoplus_{a\in A}Ae_a$ and $\rho:G\twoheadrightarrow P$ send $e_a$ to $da$. For the square-zero algebras, the surjection

\[
A\oplus G\longrightarrow A\oplus P,
\qquad (a,g)\longmapsto(a,\rho(g))
\]

and the $k$-algebra map $A\to A\oplus P$, $a\mapsto(a,da)$, form a lifting problem. A lift would have the form $a\mapsto(a,D(a))$ with $\rho D=d$, and the universal property of $P$ would supply an $A$-linear section of $\rho$, contradicting the established nonprojectivity. This records the actual obstructed morphism over the smaller base.

## 4. Consequences for the two Hua power-series leads

`context/notes/RESULTS_STATE.md` labels **Hua, findings register, `22-power-series-discrete-obstruction`** as conjectural, with a reference-search claim and an intake “new to us”; it labels **`22-p23-proposition-reconstruction`** unsearched/conjectural with a partly proved Lean card. Those are the register's recorded statuses, not independent certification.

The first lead's specific coefficient field is $K=\mathbb Q(x_i\mid i\in I)$ and its base for absolute field differentials is $\mathbb Q$. In the manuscript's no-extension calculation, deleting the finitely many $dx_i$-coordinates occurring in $D(t)$ leaves infinitely many coordinates $i_r$ and the explicit test $f=\sum_r x_{i_r}t^r$. Truncation and $D_i(t)=0$ give $D_{i_r}(f)=t^r$, which contradicts finite support. The square-zero problem in §1 proves the discrete failure over the coefficient field $K$, while the usual-topology power-series lifting is supplied by `EGA_chap0_ega0-19.tex`, 0.19.3.4. Thus the first lead's actual assertion is supported; §§2–3 prove additionally the manuscript's stronger failure over $\mathbb Q$ for that same example.

For the general proposition in the second lead, the finite-dimensional space $V$ containing all $D(t_j)$ is removed by choosing finitely many $a_1,\ldots,a_s\in K$ whose differentials span a space **containing** $V$. There is no need for this span to equal $V$. The transitivity quotient $\Omega_{K/k}\to\Omega_{K/k(a_1,\ldots,a_s)}$ kills $V$ and removes only a finite-dimensional span, so its target remains infinite-dimensional. The manuscript's series argument then proves the claimed absence of a left inverse to $\alpha$, and §§2–3 verify its final smaller-base conclusion by the additional projectivity calculation. Confidence is high in both verifications because the base maps, the finite quotient, the residue isomorphism and the nonzero components are explicit. No claim of novelty or alteration of the historical register statuses is made.

## 5. Checks on the characteristic-two examples in A25 and A28

### 5.1. Three transcendental generators

For A25 take $K=\mathbb F_2(x,b,c)$ with $x,b,c$ independent, $a=b^2$, $y=b^2x+c^2$ and $k=\mathbb F_2(x,y)$. The inclusion $\mathbb F_2[X,A,Y]\to\mathbb F_2[x,b,c]$ given by $(X,A,Y)\mapsto(x,b^2,b^2x+c^2)$ is injective: in a nonzero polynomial viewed as a polynomial in $Y$, the leading $Y^d$ term produces the nonzero leading $c^{2d}$ coefficient obtained by substituting $(X,A)=(x,b^2)$. This proves the algebraic independence of $x,a,y$, and hence $a\notin\mathbb F_2(x,y)$.

The absolute differential space of $K$ has basis $dx,db,dc$, and $dy=a\,dx$. For $f\in k\cap K^2$, the equality $df=0$ gives

\[
0=(\partial_xf+a\partial_yf)dx.
\]

Both partial derivatives lie in $k$, and $a\notin k$ forces both to vanish. The basis $1,x,y,xy$ of $k$ over $k^2=\mathbb F_2(x^2,y^2)$ writes $f=f_{00}+f_{10}x+f_{01}y+f_{11}xy$ with coefficients in $k^2$; its partial derivatives are $f_{10}+f_{11}y$ and $f_{01}+f_{11}x$. Their vanishing gives $f_{10}=f_{11}=f_{01}=0$, proving $f\in k^2$ and therefore $k\cap K^2=k^2$.

The map at issue is explicitly

\[
\Omega_{k/(k\cap K^2)}\otimes_kK
=K\,dx\oplus K\,dy
\longrightarrow K\,dx\oplus K\,db\oplus K\,dc,
\qquad (u,v)\longmapsto(u+av,0,0).
\]

Its kernel is $K(-a,1)$, a line. A nonzero vector of this line with coordinates in $k$ would have nonzero second coordinate and ratio $-a\in k$, impossible. Thus the example proves both the advertised failure of injectivity and the margin's absence of a basis defined over $k$.

### 5.2. The final algebraic-coefficient variant

For A28 let $a\in\mathbb F_4\setminus\mathbb F_2$ satisfy $a^2+a+1=0$, put $b=a^2$ and take $K=\mathbb F_4(x,c)$ with $x,c$ independent, $y=ax+c^2$, and $k=\mathbb F_2(x,y)$. The same leading-$c$-degree argument proves that $x,y$ are algebraically independent over $\mathbb F_4$. The identity $a=f(x,y)/g(x,y)$ with $f,g\in\mathbb F_2[X,Y]$ and $g\ne0$ would force the polynomial $a g-f$ to vanish; coefficient comparison at a nonzero coefficient of $g$ would put $a$ in $\mathbb F_2$. This proves $a\notin k$ directly.

The element $b=a^2$ generates $\mathbb F_4$ over $\mathbb F_2$, satisfies $b^2=a$ and has separable degree two, so $k(b)=\mathbb F_4(x,y)$ has degree two over $k$. In $\mathbb F_4(x,y)$, the derivation $\partial/\partial y$ annihilates every square and takes $y-ax$ to $1$; hence $y-ax$ is not a square. Adjoining its square root $c$ has degree two and is purely inseparable. The displayed tower gives $[K:k]=4$ exactly. Its differential map is $(u,v)\mapsto(u+av,0)$ in the basis $dx,dc$, and the preceding calculation again gives $k\cap K^2=k^2$ and kernel $K(dy-a\,dx)$.

These calculations independently verify the phenomenon in **Hua, findings register, `22-differentials-kernel-counterexample`**, whose supplied status is unsearched/conjectural with a partly proved Lean card. They instantiate the frozen source's “Voici un contre” on scan 027 and “On peut aussi prendre” on scan 029. The exact constants $\mathbb F_2,\mathbb F_4$ are this review's choices, not a proposed replacement of the source wording.

## 6. Source locators and review limits

The local context searches are appended per note to `records/research_algebra_searches.txt`. Exact relevant context files are `context/ega_fr/EGA_chap0_ega0-19.tex`, 0.19.2.1, 0.19.3.4, 0.19.9.1; `context/ega_fr/EGA_chap0_ega0-20.tex`, 0.20.4.9, 0.20.5.7, 0.20.7.2; and `context/ega_fr/EGA_chap0_ega0-21.tex`, 0.21.1.9, 0.21.2.5, 0.21.4–6. The local EGA edition is explicitly an AI transcription and has no archive-scan numbering; its labels are comparison locators. Subsequent direct inspection of the original EGA IV-1, printed pp. 131, 147–148 and 204, confirmed A29's supplied-context transcription errors and established that A27's displayed-field discrepancy is present in the original printing itself; updated notes A27/A29 record the exact maps and printed locators.

The following primary reference pages were reopened for this calculation on 2026-11-16:

- Stacks Project, Theorem 10.85.4, [Tag 0593](https://stacks.math.columbia.edu/tag/0593), tool reference `turn22view0`: projective modules over local rings are free.
- Stacks Project, [Section 00TH](https://stacks.math.columbia.edu/tag/00TH), Proposition 10.138.8(6), tool reference `turn22view1`: formal smoothness includes projectivity of the differential module; Lemma 10.138.7 gives the split conormal presentation and Lemma 10.138.9 gives the coefficient-map consequence for a formally smooth top map.

Only these familiar projectivity facts are taken from those web pages; the residue map, the direct-sum contradiction, the square-zero obstruction and the finite field calculations are the explicit calculations given above. All manuscript reading markers and unusual endings remain in the frozen transcription.


## 7. Independent check of A30's coefficient adjunction

The characteristic-two substitution in A30 has relation \(w^2=X+Z^2Y\) and inverse \(x=Y,b=Z,c=w\). The triples \((y,x,b)\) and \((x,y,c)\) are algebraically independent: respectively, \(c^2=y+b^2x\) and \(b^2=(y+c^2)/x\) exhibit the three-variable rational field \(K\) as an algebraic extension of the corresponding three-generator subfield. In the target basis \((dx,db,dc)\), the second differential map has matrix
\[
\begin{pmatrix}1&b^2&0\\0&0&0\\0&0&1\end{pmatrix}
\]
relative to the intermediate basis \((dx,dy,dc)\). Its composite with the first two coordinate vectors has kernel \(K(dy-b^2dx)\), confirming the exact link in A30 without attributing an emendation to the historical author.
