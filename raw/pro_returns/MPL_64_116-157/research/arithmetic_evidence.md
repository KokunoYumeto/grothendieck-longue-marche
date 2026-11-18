# Arithmetic and polynomial checks: detailed evidence

This appendix concerns the frozen transcription of cote 64, scans 154–157, with exact polynomial checks for scans 116–118 and 123–126. No scan image was viewed and no transcription file was modified for this research. All hypotheses and mathematical corrections below belong to the notes.

## Context and register scope

The supplied *hua_project/64.modern.tex* is **Michel Hua's project's modernised interpretation**, not an authoritative transcription. Its §VI already restricts the normality test to DVRs and gives the higher-dimensional counterexample; “Les involutions … et les points d'ordre 4” already identifies the radical signs; “Vers l'épinglage de Legendre” supplies the basis formulas. Those antecedents are credited, with independent checks below.

The supplied *notes/RESULTS_STATE.md* has no directly matching numbered quadratic-normality theorem. **LM4_SUCCESSOR B.38** and **EXIT_TOWER E.24** remain open in that snapshot and are not settled by local orders or level-four coordinate formulas. The boundary example A10 is a comparison input for **LM6 F.43**, not a proof of that result or an identification with the place at infinity announced in cote 149.

## A01–A02. The precise DVR normality criterion

Let $A$ be a DVR, $\mathfrak m=(\pi)$, $k=A/\mathfrak m$, and $B=A[S]/(S^2-a)$, $a\in A$. Normality here is normality as a ring: a normal algebra can be a product or a semilocal domain. Neither completeness, henselianity, nor perfection of $k$ is required.

1. If $a\in\mathfrak m$, then $B$ is normal exactly when $v(a)=1$.
2. If $a\in A^\times$ and $\operatorname{char}k\ne2$, then $B$ is finite étale and normal.
3. If $a\in A^\times$, $\operatorname{char}k=2$, and $\bar a\notin k^2$, then $B$ is a DVR with residue field $k(\sqrt{\bar a})$. This residue extension is purely inseparable; the normal algebra is not étale over $A$.
4. If $a\in A^\times$, $\operatorname{char}k=2$, and $\bar a=\bar\alpha^2$, set $b=\alpha^2-a\in\mathfrak m$. Then $B$ is normal exactly when $b\notin\mathfrak m^2$.

**Proof.** In case 1, $B$ is local with maximal ideal $(\pi,S)$. If $a=\pi u$ for a unit $u$, then $\pi=u^{-1}S^2$, so that ideal is principal and the one-dimensional local ring is a DVR. If $a\in\pi^2A$, the element $S/\pi$ belongs to the total quotient ring and is integral, since $(S/\pi)^2=a/\pi^2\in A$, but does not belong to the free $A$-module $A\oplus AS$; normality fails.

In case 2 the derivative $2S$ is a unit, since $S^2=a$ is a unit; the standard étale criterion applies. In case 3, the residue algebra is a field, the maximal ideal of the local algebra $B$ is $\pi B$, and dimension one again gives a DVR. This argument preserves the purely inseparable character of the residue extension.

For case 4, $T=S-\alpha$ gives $f=T^2+2\alpha T+b$. In the regular local ambient ring $C=A[T]_{(\pi,T)}$, of dimension two, the hypersurface $C/(f)=B$ is regular of dimension one exactly when $f\notin(\pi,T)^2$, equivalently $b\notin\mathfrak m^2$. One-dimensional local normality is equivalent to regularity. Changing $\alpha$ to $\alpha+m$ changes $b$ by $2\alpha m+m^2\in\mathfrak m^2$, proving independence of the obstruction class. The standard background is the Stacks Project Authors (n.d., Tags 00P7, 02GI, and 0AP2).

For $\operatorname{char}k\ne2$, the exact locality criterion is

$$
B\text{ local}\quad\Longleftrightarrow\quad
a\in\mathfrak m\ \text{or}\ \bar a\notin k^2.
$$

For a unit with square residue, the residue algebra has two distinct maximal ideals and so does $B$. Without henselianity this does not imply a product decomposition over $A$.

**Higher dimension.** Hua's modernised reading already gives $A=k[[x,y]]$, $a=xy\in\mathfrak m^2$. For $k=\mathbb Q$, the hypersurface $k[[x,y,S]]/(S^2-xy)$ has its only singularity at the closed point, hence is $R_1$; it is also Cohen–Macaulay and $S_2$, hence normal. The frozen phrase on scan 155 is “anneau jauge,” marked doubtful: this proof does not decide whether the handwriting specified a DVR or a broader regular local ring.

## A03. “Ordinary quadratic” requires an additional hypothesis

Suppose $\operatorname{char}k=2$, $\alpha\in A^\times$, and $b\in\pi^2A$. The quadratic initial form of $T^2+2\alpha T+b$ in the regular local ambient ring with parameters $(T,\pi)$ is

$$
q(X,Y)=X^2+cXY+dY^2,\qquad
c=\overline{2\alpha/\pi},\quad d=\overline{b/\pi^2}.
$$

The cross coefficient is zero if $v(2)>1$, including equal characteristic two, where $v(2)=\infty$. Its polar derivatives are $cY,cX$; hence the tangent binary quadratic is geometrically nondegenerate precisely when $c\ne0$, equivalently $v(2)=1$. This is the ordinary-double-point condition in residual characteristic two (Stacks Project Authors, n.d., Tag 02DN). It holds for $\mathbb Z[T]_{(2)}$, the application's vertical DVR, but not for every DVR of residual characteristic two.

Explicit counterexamples to the unrestricted assertion are:

- **Equal characteristic:** $A=\mathbb F_2[[\pi]]$, $a=1+\pi^3$, $\alpha=1$. The completed ring is $\mathbb F_2[[\pi,T]]/(T^2+\pi^3)$, with doubled tangent line $T^2=0$ and normalization parametrized by $\pi=w^2,T=w^3$; this is a cusp.
- **Mixed characteristic:** $A=\mathbb Z_2[\pi]/(\pi^2-2)$, $a=5$, $\alpha=1$. Then $b=-4=-\pi^4$ and $f=T^2+\pi^2T-\pi^4$, again with doubled tangent line. The generic algebra is a field: writing $\sqrt5=x+y\sqrt2$ over $\mathbb Q_2$ would force $xy=0$, while $5$ is not a square modulo eight and $5/2$ has odd valuation.

The scratch calculation on scan 157 involving $T^2+\alpha\pi T+\beta\pi^2$ is relevant, but the frozen text does not explicitly impose the nonzero cross coefficient. This qualification concerns singularity type only; the DVR normality criterion above remains valid without $v(2)=1$.

## A04–A05. Full radicand, local tests, and global normality

Let $R=\mathbb Z[T]$ and $P=\varepsilon qQ$ as in scan 155: $\varepsilon=\pm1$, $q>0$ squarefree, and $Q\in R$ primitive, squarefree in $\mathbb Q[T]$, with positive leading coefficient. Assume the square class is nontrivial, so $L=\mathbb Q(T)(\sqrt P)$ is a quadratic field; the split case can instead be formulated using the total ring of fractions. Put $B=R[S]/(S^2-P)$.

At horizontal height-one primes the residue characteristic is zero and $P$ has valuation zero or one. At a vertical odd prime $p$, the same holds because $q$ is squarefree and $Q$ primitive. The DVR criterion proves normality at these primes. At $(2)$, failure of normality is equivalent to the **full signed radicand $P$** being square modulo four.

This test can be made in $(\mathbb Z/4)[T]$, not just in $R_{(2)}/4$. A polynomial square in $\mathbb F_2(T)$ has its unique square root in $\mathbb F_2[T]$; choose a polynomial lift $r$. Every local lift differs from $r$ by $2h$ and has the same square modulo four. Also $4R_{(2)}\cap R=4R$, since a polynomial not divisible by two is a nonzerodivisor modulo four. These facts prove the polynomial version.

Bare $Q$ is insufficient if the sign/content factors are omitted: $Q=1$ is square modulo four, but $P=3$ and $P=-1$ give normal dyadic orders. Scan 154's examples contain sign annotations, and scan 156 explicitly uses $\varepsilon Q$; this is therefore a qualification of a compressed or ambiguous notation, not a transcription amendment.

**Global sharpening.** As a hypersurface in the regular ring $\mathbb Z[T,S]$, $B$ is Cohen–Macaulay and $S_2$. Once its height-one localizations are normal, they are regular in dimension one, and Serre's criterion gives normality everywhere. Thus the finitely many possibly nonnormal closed points allowed in scan 154 form an empty set for this model. The weaker manuscript assertion is not contradicted (Stacks Project Authors, n.d., Tags 02JN and 031O).

## A06. Explicit normalization proves the deferred sufficiency

If $P=r^2+4h$ with $r,h\in R$, define

$$
u=\frac{S+r}{2},\qquad C=R[u]=R[U]/(U^2-rU-h).
$$

The equation is monic and $S=2u-r$, so $C$ is finite free of rank two over $R$, contains $B$, and has the same fraction field. Its discriminant is $P$. At odd or horizontal height-one primes $C=B$, since two is invertible; at $(2)$, $\bar r\ne0$ in $\mathbb F_2(T)$, and the derivative $2u-r$ is a unit, so $C_{(2)}$ is étale. Its hypersurface $S_2$ property and these $R_1$ checks make it normal globally, hence the full integral closure of $R$ in $L$.

On $D(P)$ its derivative $2u-r=S$ is a unit because $S^2=P$, so this normalization is finite étale there. This explicitly supplies “Cette condition est aussi suffisante” from scan 156. The certificate checks

$$
(2U-r)^2-P=4(U^2-rU-h).
$$

Generic étaleness over **every** rational prime is equivalent to $q=1$ and $\varepsilon Q$ square modulo four. Odd primes exclude odd divisors of $q$; $q=2$ is Eisenstein at two; for $q=1$, a normal naive dyadic order is either ramified or has inseparable residue extension, whereas the square-modulo-four case acquires the étale integral generator above. Thus the order $B$, its normalization $C$, and their characteristic-two fibres must be distinguished.

For fixed primitive $Q$, at most one sign works. If both $Q\equiv r^2$ and $-Q\equiv s^2\pmod4$, then $\bar r=\bar s$, so $r^2\equiv s^2\pmod4$ and $2Q\equiv0\pmod4$, contradicting primitivity. This is uniqueness of a working sign, not existence for every $Q$.

## A07–A08. The two-branch example and its infinity chart

For $P=T(T-\lambda)$, $\lambda\ne0$, a square root modulo four must reduce to $T$ modulo two and therefore has square congruent to $T^2$ modulo four. Hence

$$
T(T-\lambda)\text{ is square modulo }4
\quad\Longleftrightarrow\quad4\mid\lambda.
$$

The negative sign cannot work: its square-root reduction would still be $T$, whereas the coefficient of $T^2$ would be $3$ instead of $1$ modulo four. The weaker congruence $T(T-\lambda)\equiv T^2\pmod2$ is equivalent only to $2\mid\lambda$; $\lambda=2$ refutes an equivalence with $4\mid\lambda$. Hua's modernised interpretation already points to the useful modulo-four congruence.

Write $\lambda=4m$. On the affine chart the normalized algebra is

$$
\mathbb Z[T,U]/(U^2-TU+mT),\qquad S=2U-T.
$$

It is finite étale after inverting $T(T-\lambda)$. For the infinity chart put $x=1/T$, $\delta=S/T$, and $u=(1+\delta)/2=U/T$; then

$$
\delta^2=1-\lambda x,\qquad
C_\infty=
\mathbb Z[x,(1-\lambda x)^{-1},u]/(u^2-u+mx).
$$

Its discriminant $1-\lambda x$ is a unit, and $(2u-1)^2=1-\lambda x$, so this is finite étale over $\mathbb P^1_{\mathbb Z}\setminus\{0,\lambda\}$. The two charts agree by $U=Tu$.

The frozen last radicand on scan 156 is instead $\lambda x-1$. For $4\mid\lambda$ it is congruent to $-1\pmod4$ and defines a dyadically ramified order that is already normal. Concretely $\lambda=4,x=0$ gives $\mathbb Z[i]$, with reduction $\mathbb F_2[S]/((S+1)^2)$, so this opposite-sign expression cannot produce the asserted all-characteristic étale cover. This remains a mathematical reading question outside the transcription.

## A09. Completion: precise validity and one boundary case

For the local dyadic algebra $B=A[T]/(T^2+2\alpha T+b)$, Noetherian completion exactness gives

$$
B^{\wedge,(T)}=A[[T]]/(T^2+2\alpha T+b).
$$

If $b\ne0$, then $B/(T)=A/(b)$ has finite length; thus $(T)$ is primary for the maximal ideal of $B$ and the two adic topologies are cofinal. This is also the maximal-ideal completion, even when $A$ is not complete. In a genuine nonsquare quadratic-field extension $b=\alpha^2-a$ cannot vanish, so the displayed formula in scan 155 is valid in that application (Stacks Project Authors, n.d., Tag 0BNH, Lemma 10.97.1).

For the unrestricted split case take $A=\mathbb Z_{(2)}$, $a=\alpha=1$, $b=0$. The displayed ring $A[[T]]/(T(T+2))$, modulo $T$, is $A$, whereas the maximal-ideal completion modulo $T$ is $\mathbb Z_2$. Consequently one must specify topology in this boundary case, but noncompleteness of $A$ alone is not an objection.

## A10. A boundary calculation not pursued on the sheet

For the corrected model $u^2-u+mx=0$, the infinity fibre $x=0$ is $u(u-1)=0$, two disjoint $\mathbb Z$-sections. In characteristic two it is $u^2+u+\bar m x=0$, split for even $m$ and isomorphic to the connected Artin–Schreier affine-line double cover for odd $m$. These calculations do not identify this cover with cote 149's announced modular degeneration; the proposed Tate-cusp calculation in the supplied *MPL_149_091-136_notes.md*, RN099-03, concerns different monodromy data and remains a contextual lead here.

## L90–L91. Radical signs and the zero-root case

Set $r=\zeta_i,u=\zeta_\lambda,v=\zeta_\mu$, and

$$
a_1=-(r+u+v),\qquad a_2=ru+rv+uv,\qquad a_3=-ruv.
$$

The exact identities are

$$
f'(r)=(r-u)(r-v)=r^2-a_2+2uv
=-(a_1r+2a_2-3uv).
$$

For $r\ne0$ this is also $-r^{-1}(a_1r^2+2a_2r+3a_3)$, the main expression in scans 116 and118. The bracket $-(a_1r+2a_2+3uv)$ on scan 118 differs by $-6uv$. The marginal right-hand side $2rz_i-(a_2+2uv)$ differs from the correct $2rz_i-a_2+2uv$ by $-4uv$. Hua's project already flags both signs; this run independently checks the exact identities and the example $(r,u,v)=(1,2,3)$, where the correct radical is $2$ and the bracket is $-34$.

The undivided involution matrix satisfies

$$
M=\begin{pmatrix}r&uv-r(u+v)\\1&-r\end{pmatrix},
\qquad M^2=(r-u)(r-v)I.
$$

It extends to $r=0$: the involution is $z\mapsto uv/z$ and the fixed-point equation is $z_i^2=uv$, nonzero for distinct roots. This resolves the algebraic zero-root concern without giving a numerical meaning to $0/0$ or modifying a reading. The elliptic interpretation retains the distinct-root and characteristic-unequal-to-two assumptions.

## L92. Basis identities and their limited consequence

Let $\Delta_0=(r-u)(u-v)(v-r)\ne0$. Set

$$
f_1=\Delta_0^{-1}(u-v,v-r,r-u),\qquad
f_2=-\Delta_0^{-1}(r(u-v),u(v-r),v(r-u)).
$$

The certificate verifies all three cyclic identities

$$
\zeta_i f_1+f_2=\frac{e_j-e_k}{\zeta_j-\zeta_k}
$$

and the kernel equations $\sum\lambda_i=0$, $\sum\lambda_i\zeta_i=0$ for $\lambda=(u-v,v-r,r-u)$. Thus the positive sign of $\Delta_0f_1$ and negative sign of $\Delta_0f_2$ follow from the system; the uncertain sign mark on scan 126 remains a reading issue. Hua's “Vers l'épinglage” gives these formulas and their attachment to condition b), but they do not determine the square-normalization condition c) deferred on scan 121. The determinant expansion in scans 117–118 was also checked, without claiming that this elementary algebra alone proves the elliptic group-law interpretation.

## Computation record and limits

The file *arithmetic_certificate.py* ran with SymPy 1.14.0 and returned **PASS**; its complete output is in *arithmetic_certificate_output.txt*. It verifies polynomial identities, representative modulo-four arithmetic, tangent polynomials, and counterexample substitutions. It is not a formal certificate for normality, completion, or étaleness as scheme properties: those conclusions use the explicit arguments above and the primary commutative-algebra results below.

## Primary references (APA form)

Stacks Project Authors. (n.d.). *Around Krull–Akizuki* (Tag 00P7, Lemma 10.119.7). The Stacks Project. https://stacks.math.columbia.edu/tag/00P7

Stacks Project Authors. (n.d.). *Cohen–Macaulay rings* (Tag 02JN, Lemma 10.104.2). The Stacks Project. https://stacks.math.columbia.edu/tag/02JN

Stacks Project Authors. (n.d.). *Completion for Noetherian rings* (Tag 0BNH, Lemma 10.97.1). The Stacks Project. https://stacks.math.columbia.edu/tag/0BNH

Stacks Project Authors. (n.d.). *Étale morphisms* (Tag 02GI, Definition 29.37.1). The Stacks Project. https://stacks.math.columbia.edu/tag/02GI

Stacks Project Authors. (n.d.). *Permanence of properties under étale maps* (Tag 0AP2, Lemma 15.45.4). The Stacks Project. https://stacks.math.columbia.edu/tag/0AP2

Stacks Project Authors. (n.d.). *Serre's criterion for normality* (Tag 031O, Lemma 10.157.4). The Stacks Project. https://stacks.math.columbia.edu/tag/031O

Stacks Project Authors. (n.d.). *Singularities* (Tag 02DN, Remark 111.14.2). The Stacks Project. https://stacks.math.columbia.edu/tag/02DN

## Supplied interpretation credited

Hua, M., project. (2026). *Cote 64: Modernised reading* [AI-produced interpretation; supplied hua_project/64.modern.tex, revised October 18, 2026, according to its metadata]. Sections “Les involutions … et les points d'ordre 4,” “Vers l'épinglage de Legendre,” and “VI. Appendice : normalité des extensions quadratiques.” Attribution identifies the supplied project's contribution and does not certify its other readings or results.
