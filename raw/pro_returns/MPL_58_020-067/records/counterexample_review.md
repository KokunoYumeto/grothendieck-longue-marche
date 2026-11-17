# Independent checks of three research-note counterexamples

17 November 2026; research phase only, after the transcription freeze. This review read only the frozen textual transcriptions and supplied context. No manuscript image was opened and no transcription was edited. The diagnoses originate in **Michel Hua's project, modernised reading of cote 58**; the explicit choices and calculations below check or refine his examples. They are research commentary and must not be substituted into the diplomatic text.

## 1. Scan 58:23: connected generic fibre need not specialize to a connected fibre

**Verdict: the proposed example works, including the dimension bound.** It repairs a limitation of the zero-dimensional finite-cover example described in Hua's footnote.

**Sources:** pages/MPL_58_020-067_58_scan023.tex, Theorem 2; context_opened/hua_project/58.modern.tex, subsection **“Les fibres spéciales d'un morphisme propre (pages 22 à 26)”**, footnote following Theorem 2. Hua's page 22 is our scan 23. The frozen statement assumes ordinary connectedness in dimension at least $h$ for the generic fibre and has the uncertain size reading $h+1$ versus $h_0$. The following uses the ordinary $h+1$ reading.

Set

$$
R=\mathbf Z_{(5)},\qquad B=\operatorname{Spec}R,\qquad
D=R[T]/(T^2+1)=R[i],\qquad X=\mathbf P^1_D,
$$

and let $f:X\to B$ be the composite of the projective-line projection and the finite morphism $\operatorname{Spec}D\to B$. Take $h=0$ and let $b_0$ be the closed point of $B$.

| Hypothesis or claimed conclusion | Direct verification |
|---|---|
| Locally noetherian integral base | $R$ is a discrete valuation ring, hence noetherian and integral. |
| Geometrically unibranch at $b_0$ | $R$ is regular; its strict henselization is regular local and is a domain. In particular the base satisfies the stronger geometric reading of the bracketed hypothesis. |
| Proper morphism | $\mathbf P^1_D\to\operatorname{Spec}D$ is projective, and $\operatorname{Spec}D\to B$ is finite. Their composite is proper. |
| Dominance of all irreducible components of $X$ | $T^2+1$ is irreducible over $\mathbf Q$, so $D$ is a domain inside $\mathbf Q(i)$. Hence $X$ is integral and its unique component dominates $B$. |
| Generic component dimension at least $h+1=1$ | $X_\eta=\mathbf P^1_{\mathbf Q(i)}$, considered as a $\mathbf Q$-scheme, is integral of dimension one. |
| Generic connectedness in dimension at least $h=0$ | An integral nonempty space is connected. For $h=0$, the connectedness condition is ordinary connectedness. |
| Special component dimension at least one | Both components of the special fibre computed below are projective lines. |
| Special-fibre connectedness | **Fails:** the special fibre is the disjoint union of two projective lines. |

The special-fibre calculation is explicit:

$$
D/5D
=\mathbf F_5[T]/(T^2+1)
=\mathbf F_5[T]/((T-2)(T+2))
\simeq\mathbf F_5\times\mathbf F_5.
$$

The factors are coprime because $2\ne-2$ in $\mathbf F_5$. Consequently

$$
X_{b_0}\simeq
\mathbf P^1_{\mathbf F_5}\amalg\mathbf P^1_{\mathbf F_5}.
$$

There is no singularity or flatness loophole: $D/R$ is finite étale, since the derivative $2i$ is a unit. Thus $f$ is even smooth and flat of relative dimension one. The base is also excellent, so Hua's separately added excellence assumption does not remove this example.

The generic fibre is **not geometrically connected**: after extension from $\mathbf Q$ to an algebraic closure, $\mathbf Q(i)\otimes_{\mathbf Q}\overline{\mathbf Q}\simeq\overline{\mathbf Q}\times\overline{\mathbf Q}$. Its ring of global functions over the original generic field is $\mathbf Q(i)$, not $\mathbf Q$; globally, $f_*\mathcal O_X$ is the algebra associated to $D$, not $\mathcal O_B$. This identifies the precise missing distinction.

**Caveat and credit:** Hua diagnoses the need to strengthen generic connectedness and describes a split-prime number-field cover. That finite cover alone has generic dimension zero and misses the stated $h+1$ bound at $h=0$. Passing to $\mathbf P^1_D$ is our explicit refinement that meets this bound. The calculation disproves the ordinary-connectedness formulation; it does not by itself prove every part of Hua's amended higher-dimensional theorem.

## 2. Scan 58:41: $H^1/H^2$ vanishing does not imply categorical faithfulness

**Verdict: the proposed example works. It does not refute the statement about Picard groups.**

**Sources:** pages/MPL_58_020-067_58_scan041.tex, lemma before “Théorèmes de permanence”; context_opened/hua_project/58.modern.tex, subsection **“Composantes connexes, groupe fondamental, groupe de Picard (pages 37 à 40)”**, footnote to the lemma on its page 40. The frozen text says “pl. fidèle” under $H^1$ vanishing and “équiv. de catégories” after adding $H^2$ vanishing.

Let

$$
X=\operatorname{Spec}k[[t]],\qquad
Y=V(t)=\operatorname{Spec}k,\qquad
\widehat X=\operatorname{Spf}k[[t]].
$$

Here $Y$ is an effective Cartier divisor, its ideal is $J=(t)$, and

$$
J^n/J^{n+1}\simeq k,\qquad
H^1(Y,J^n/J^{n+1})=H^2(Y,J^n/J^{n+1})=0
\quad(n\ge1).
$$

Thus all the displayed vanishing assumptions hold. Nevertheless, multiplication by $1+t$ and multiplication by $1$ are distinct automorphisms of $\mathcal O_{\widehat X}$ whose restrictions to $Y$ are both the identity. The first is an automorphism because its inverse is the formal series $\sum_{j\ge0}(-t)^j$. Therefore the restriction functor is **not faithful**, whether “line-bundle category” means the groupoid of line bundles and isomorphisms or the category allowing all module homomorphisms. In the latter interpretation, multiplication by $t$ also gives a nonzero morphism that restricts to zero.

Both Picard groups are zero: every line bundle on the one-point formal scheme $\widehat X$ is free, as is every line bundle on $Y$. Hence the map on isomorphism classes is a bijection. The example isolates precisely the categorical overstatement instead of challenging the Picard-group conclusion.

The missing phenomenon is visible already in

$$
H^0(Y,J^n/J^{n+1})=k:
$$

these groups provide infinitesimal automorphism freedom. The $H^1/H^2$ hypotheses concern lifting and classes; they do not eliminate these automorphisms.

**Caveat:** a proposed repaired categorical criterion must distinguish automorphisms from arbitrary homomorphisms. For the latter, the successive kernels involve $H^0(Y,L_0^{-1}\otimes M_0\otimes J^n/J^{n+1})$ for the line bundles concerned, not only the untwisted $H^0$ groups. This review asserts no complete necessary-and-sufficient repair. If a proper ambient example is desired, the completion of $\mathbf P^1_k$ along a $k$-rational point yields the same formal disc and the same counterexample to the lemma.

## 3. Scan 58:58: positive graded finite generation does not force negative-twist vanishing

**Verdict: the proposed example works. Specify a rational point to obtain the literal answer $k$ and a cyclic graded module.**

**Sources:** pages/MPL_58_020-067_58_scan056.tex, setup and questions; pages/MPL_58_020-067_58_scan058.tex, final equivalence in the $B_n$ chain; context_opened/hua_project/58.modern.tex, subsection **“Les questions, et la dualité (pages 55 à 58)”**, footnote to $B_n$. Hua supplies the skyscraper-sheaf diagnosis; the explicit coordinates and regularity check below refine it.

Let $r\ge1$ and choose

$$
X=U=\mathbf P^r_k,\qquad
S=k[x_0,\ldots,x_r],\qquad
Y=V(x_0),\qquad
p=[1:0:\cdots:0],\qquad F=i_*k
$$

for the closed immersion $i:\{p\}\hookrightarrow X$. The complement $Z=X-U$ is empty, which is a finite closed set and is allowed by the setup.

The section $x_0$ does not vanish at $p$ and identifies every twist of $F$ with $F$. In particular,

$$
H^0(U,F(m))\simeq k\quad\text{for every }m\in\mathbf Z.
$$

Choosing the basis in each degree using $x_0$ gives the graded $S$-module identification

$$
\bigoplus_{m\ge0}H^0(U,F(m))
\simeq S/(x_1,\ldots,x_r)
\simeq k[x_0].
$$

It is cyclic, generated in degree zero. Every tail $m\ge M$ is also finitely generated, generated by $x_0^M$. Thus either retained lower-bound reading in the frozen scan, $m\ge0$ or $m\gg0$, satisfies the finite-generation condition. But

$$
H^0(U,F(-m))\simeq k\ne0
\quad\text{for every }m\ge0.
$$

The failure is already at $n=0$. All higher cohomology of this skyscraper sheaf vanishes, so including additional nonnegative cohomological degrees does not rescue the reverse implication.

Multiplication by the hyperplane equation,

$$
x_0:F(-1)\longrightarrow F,
$$

is an isomorphism, hence injective: $x_0$ is $F$-regular in the nonzerodivisor sense used in the displayed exact sequence. Its cokernel is zero because $\operatorname{Supp}F$ is disjoint from $Y$.

**Caveats and useful strengthening:**

- The positive truncation matters. The two-sided module $\bigoplus_{m\in\mathbf Z}H^0(U,F(m))\simeq k[x_0,x_0^{-1}]$ is not finitely generated over $S$. The example does not refute a claim about that two-sided module.
- If a convention for “regular” additionally requires a nonzero quotient, use $F'=\mathcal O_X\oplus k(p)$. Then $x_0$ is injective, $F'/x_0F'=\mathcal O_Y\ne0$, and the positive module is $S\oplus S/(x_1,\ldots,x_r)$, still finitely generated. Negative $H^0$ still contains the nonzero $k(p)$ summand.
- If a nonempty $Z$ is demanded, remove another point $q\notin Y\cup\{p\}$ from $X$. The same calculations for $F$ survive unchanged.
- Because $\widehat F=0$, the map $H^0(U,F)=k\to H^0(\widehat X,\widehat F)=0$ is not injective. With $Z=\varnothing$, the maps $\alpha_i$ from local cohomology supported on $Z$ have zero source and are injective. Thus this same example also confirms Hua's separate warning that the condition labelled $(*)$ alone does not imply the $n=0$ formal-comparison conclusion at the bottom of scan 58; the stronger negative-vanishing condition is needed for that argument.

## 4. Attribution and status for the main notes

Credit all three diagnoses to **Hua, modernised reading of cote 58**, citing the subsection titles above. State that the present research independently checks explicit examples and, in case 1, strengthens the supplied example to meet the fibre-dimension hypothesis. These calculations refute the indicated literal implications under the retained textual readings; they neither resolve uncertain handwriting nor establish all corrected theorems. The assertions belong in research notes, leaving the frozen statements intact.

## 5. Additional check: the unrestricted quotient functor is not full

**Verdict: Hua's example and its two endomorphism rings are correct. It lies outside the separate depth-at-least-two assertion.**

**Sources:** pages/MPL_58_020-067_58_scan046.tex, the quotient category and subsequent depth restriction; context_opened/hua_project/58.modern.tex, subsection **“Une forme locale (pages 45 à 51)”**, footnote after the Hom comparison. This example and diagnosis belong to Hua's project. The rational-function argument and explicit series below are our independent verification.

Set

$$
A=k[[x,y,z]],\quad X'=\operatorname{Spec}A\setminus\{(x,y,z)\},
\quad Y'=V(x)\cap X',\quad C=V(y)\cap X',
\quad F=\mathcal O_C.
$$

The ring $A$ is $x$-adically complete. Put $B=A/(y)=k[[x,z]]$. Then
$C=\operatorname{Spec}B\setminus\{(x,z)\}$ and $C\cap Y'$ consists of the single point $p=(x)$ of $\operatorname{Spec}B$. Let $\mathcal T$ be the Serre subcategory of coherent sheaves on $X'$ supported on closed sets disjoint from $Y'$.

### 5.1 Endomorphisms in the Serre quotient

The sheaf $F$ has no nonzero subsheaf in $\mathcal T$, because it is the structure sheaf of the integral scheme $C$ and a nonzero subsheaf has the generic point of $C$ in its support. Hence quotient endomorphisms can be represented by maps

$$
F_0\longrightarrow F,\qquad F_0\subset F,\qquad F/F_0\in\mathcal T.
$$

At the generic point of $C$, such a map is multiplication by a rational function $r\in\operatorname{Frac}B$. Because $p\in Y'$, one has $(F_0)_p=F_p=B_{(x)}$, so $rB_{(x)}\subset B_{(x)}$, or $r\in B_{(x)}$. The generic rational function determines the map: a map into this torsion-free target that vanishes generically is zero.

Conversely, let $r=a/b\in B_{(x)}$, with $a,b\in B$ and $b\notin(x)$. Multiplication by $b$ is injective on $F$. The quotient $F/bF$ is supported on $V_C(b)$, a closed subset of $X'$ disjoint from $Y'$ since $b$ is a unit at $p$. Therefore

$$
bF\longrightarrow F,\qquad bs\longmapsto as
$$

defines the desired quotient endomorphism. Its generic function is $a/b$. Composition corresponds to multiplication of fractions, proving

$$
\operatorname{End}_{\operatorname{Coh}(X')/\mathcal T}(F)=B_{(x)}.
$$

### 5.2 Formal endomorphisms and strict containment

The whole intersection $C\cap Y'$ lies in $D(z)$. Completing there along $x$ gives

$$
\operatorname{End}(\widehat F)
=\varprojlim_n B[1/z]/(x^n)
=\varprojlim_n k((z))[x]/(x^n)
=k((z))[[x]].
$$

This is also the $x$-adic completion of the discrete valuation ring $B_{(x)}$. The natural map is injective and is not surjective. To prove strictness explicitly, consider

$$
u=\sum_{n\ge0}z^{-n^2}x^n\in k((z))[[x]].
$$

Suppose $u=a/b$ with $a,b\in B$ and $b\notin(x)$. Write
$a=\sum a_n(z)x^n$, $b=\sum b_n(z)x^n$, and put $d=\operatorname{ord}_z b_0(z)\ge0$. For any series $a/b=\sum c_n(z)x^n$, coefficient comparison gives

$$
b_0c_n=a_n-\sum_{j=1}^n b_jc_{n-j}.
$$

Since all $a_n,b_j$ have nonnegative $z$-valuation, induction yields
$\operatorname{ord}_z c_n\ge-(n+1)d$. But the coefficient of $x^n$ in $u$ has valuation $-n^2$, contradicting this linear bound for large $n$. Thus $u$ is a formal endomorphism absent from the quotient endomorphism ring, and the unrestricted functor is not full.

### 5.3 Depth caveat

At the point $q=(y,z)$ of $X'$, which is closed in $X'$ and lies outside $Y'$ because $x\notin q$,

$$
F_q=(A/(y))_q=B_{(z)}.
$$

This is a discrete valuation ring and has depth one, both as a module over itself and as an $A_q$-module. Thus $F$ fails the required depth-at-least-two hypothesis. More generally, at every closed point of $C\setminus Y'$ the same height-one localization of the regular two-dimensional ring $B$ gives depth one. Consequently this example refutes unrestricted fullness, **not** the restricted comparison for sheaves satisfying the stated depth bound. The frozen margin and subsequent Hom assertion must retain their qualifications.
