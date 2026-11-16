# Research review: the universal Chern ring and the gamma filtration

## Scope and evidential status

This review concerns cote 2, scans 021–023, 025, and 028–030. It uses the frozen page transcriptions, the two supplied context files, and the primary literature listed below; no manuscript image was opened by this research reviewer and no transcription was changed. Readings marked doubtful in the frozen transcription remain doubtful. In particular, the mathematical reconstructions below use the explicit vanishing condition on scan 028, not a resolution of the `=|\ne` doubt in scan 021, line 6.

The supplied context contains no earlier neighboring transcriptions, no matching settled result, and no matching open item of the user's own registers. Its two relevant Hua entries are AI-produced claims awaiting checking, not established results: **Hua, findings register, 2-chern-ring-gamma-comparison** and **Hua, findings register, 2-chern-ring-not-injective-pn**. Their exact local source is `context/notes/RESULTS_STATE.md`, lines 39 and 40 respectively; per-note searches and matches are recorded separately in `records/context_search_lambda.md`.

## Proposed register verdicts

| Context entry | Verdict of this review |
|---|---|
| **2-chern-ring-gamma-comparison** | Supported for the intended universal **lambda-homomorphism** problem, with positive-degree sign/index and target-product qualifications. The abbreviated Whitney/product/geometric relation list, interpreted as an exhaustive definition without lambda compatibility, is insufficient; Appendix A gives a countermodel with a nontorsion degree-one kernel. |
| **2-chern-ring-not-injective-pn** | Supported for the specified family generated geometrically by the line element $L$, for $n\geq3$. Appendix B supplies all homogeneous relations, checks lambda stability, proves the nonzero degree-$n$ torsion, and gives the exact $n=3$ ring; adjoining $nL-1$ changes the family and removes this particular obstruction. No novelty claim is made. |

## Individual notes

### L01 — The geometric family is part of the input

**Cote/scans:** 2/021, lines 4, 9, 45; 028, lines 6–45; 029, lines 28–32. **Kind:** unpursued implication. **Context:** bears on both Hua IDs; qualifies the formulation of the first and is essential to the second.

The phrase “plus la famille des $E_s$ est grande … plus $CK$ devient petit” on scan 029 makes the chosen family part of the universal problem. Closure under the indicated positive operations must be distinguished from replacement by every element that is algebraically geometric in $K$: the warning on scan 029 and the added $nL-1$ on scan 022 give a concrete difference. Consequently write $C(K,S)$ in a modern restatement, even though the manuscript usually abbreviates this to $CK$.

### L02 — The displayed relations do not by themselves enforce lambda compatibility

**Cote/scans:** 2/028, lines 33–35; 029, lines 6–13. **Kind:** own idea / counterexample to an overbroad restatement. **Context:** bears on **2-chern-ring-gamma-comparison**; contradicts a literal exhaustive reading of that entry's abbreviated relation list. **Confidence:** high, because the explicit countermodel is verified in Appendix A.

Scan 028 explicitly requires an “hom de $\lambda$-anneaux”, whereas the displayed list on scan 029 contains only unit, Whitney, product, and selected rank bounds. Those displayed relations alone admit an augmented ring map from $\mathbb Z[x,y,y^{-1}]$, with $\lambda^2x=y$, to the Chern ring of $\mathbb Z[\epsilon]/\epsilon^2$ sending $x\mapsto[2,1]$ and $y\mapsto[1,1+\epsilon]$, which is not a lambda homomorphism. The intended universal problem must retain lambda compatibility; the explicit gamma-compatibility relations in SGA 6, V, 6.14, p. 358, confirm the distinction (Berthelot, 1971).

### L03 — A sign changes between the proposition and its proof

**Cote/scans:** 2/021, lines 70–74; 022, lines 14, 18, 23, 27, 31, 39. **Kind:** withdrawn/corrected in the same text, with the qualification that the earlier line is not explicitly struck out. **Context:** **2-chern-ring-gamma-comparison** uses the proof's sign and omits this internal discrepancy.

Proposition 2 on scan 021 writes $(-1)^i(i-1)!$, while the proof and conclusions on scan 022 consistently write $(-1)^{i-1}(i-1)!$. The latter is the sign supported by the calculation, and the degree-one case already distinguishes the two. Preserve both manuscript readings and record the change as an internal discrepancy; do not silently replace the proposition by its proof.

### L04 — Precise comparison, including the degree-zero exception

**Cote/scans:** 2/021–022; 029, lines 21–28; 030, lines 8–15. **Kind:** unpursued implication / narrowed claim. **Context:** **2-chern-ring-gamma-comparison**, supported with qualifications.

The corollary “Son noyau est un groupe de Torsion” follows degreewise from the two composites being $d_i\operatorname{id}$, where $d_i=(-1)^{i-1}(i-1)!$ and $i\geq1$. More precisely, for the intended lambda-theoretic universal ring, $\phi_i:C^i(K,S)\twoheadrightarrow\operatorname{gr}^i_\gamma K$ has kernel annihilated by $(i-1)!$, hence is an isomorphism for $i=1,2$ and after rationalization in every positive degree. Degree zero must be treated separately: for the stated $\mathbb Z$-augmentation and the universal graded ring generated in positive degrees it is $\mathbb Z\to\mathbb Z$, not an instance of a formula containing $(-1)!$.

### L05 — The return map lands in a ring with a different product

**Cote/scan:** 2/030, lines 8–10 and 15. **Kind:** unpursued implication. **Context:** qualifies the “map $\psi$ back” in **2-chern-ring-gamma-comparison**; no exact `A!` or `A^!` match occurs in the supplied context.

The marginal restriction “additivement … en degrés $\ne0$” is essential: the coefficient identification of $\operatorname{gr}_{\deg}\widetilde A$ with $A$ does not preserve the ordinary product. For $a\in A^i,b\in A^j$, $i,j>0$, its product is $a\star b=-\frac{(i+j-1)!}{(i-1)!(j-1)!}ab$, so $\psi$ is multiplicative into this modified ring and only a graded additive map when its target is identified with ordinary $A$. Appendix C checks the formula and the factorial composites; the formula is also SGA 6, V, (6.5.3), p. 349 (Berthelot, 1971).

### L06 — The free-ring reduction needs an integral filtration calculation

**Cote/scans:** 2/021, lines 11–40; 022, lines 29–39. **Kind:** unproved claim. **Context:** **2-chern-ring-gamma-comparison**; the manuscript adds the free-ring argument absent from the register summary.

The statements “comme on vérifie … facilement” and “$\varphi_B$ est bijectif” require an integral calculation, not merely a rational splitting argument. With $z_{s,i}=\gamma^i(X_s-n_s)$, the free finite-rank lambda ring has polynomial gamma coordinates, with the determinant units inverted, and its gamma filtration is the weight filtration $\operatorname{wt}z_{s,i}=i$. Appendix D explains why this identifies its associated graded with the polynomial ring and why a surjective augmented lambda map transports the filtration to $K$.

### L07 — Multiplicativity does not complete the lambda-homomorphism verification

**Cote/scans:** 2/021, lines 50–57; 023, lines 18–42. **Kind:** unproved claim. **Context:** **2-chern-ring-gamma-comparison**; no separate context result covers the verification.

“Vérification immédiate!” asserts that the completed natural Chern class is a lambda homomorphism, while scan 023 explicitly works through the multiplication formula and its lowest-weight term. A complete proof must additionally verify compatibility with iterated exterior/gamma operations; the multiplication calculation alone does not supply it. The full statement appears as SGA 6, V, Proposition 6.8, pp. 353–354 (Berthelot, 1971).

### L08 — The projective-space noninjectivity has a precise homogeneous witness

**Cote/scan:** 2/022, lines 41–56. **Kind:** own verification of the manuscript's counterexample. **Context:** **2-chern-ring-not-injective-pn**, supported and sharpened. **Confidence:** high, from the explicit universal calculation in Appendix B.

The answer “Non” to “Est-ce que $\varphi_K$ est tjrs bijectif ???” is justified for $K=\mathbb Z[L]/(L-1)^n$, with only the family generated geometrically by $L$, when $n\geq3$. The complete relation is coefficientwise $P_n(\xi)=1$, where $P_n(z)=\prod_{j=0}^{n}(1+jz)^{(-1)^{n-j}\binom nj}$, and its first relation gives $C^n(K,\{L\})\cong\mathbb Z/(n-1)!$, whereas $\operatorname{gr}_\gamma K=\mathbb Z[\bar y]/\bar y^n$. In particular, for $n=3$, the exact ring is $\mathbb Z[\xi]/(2\xi^3,\xi^4)$, so the nonzero class $\xi^3$ is an explicit element of the kernel.

### L09 — Adjoining the tangent-class element really changes the chosen family

**Cote/scans:** 2/022, line 58; 029, lines 28–32. **Kind:** own verification / unpursued implication. **Context:** adds to **2-chern-ring-not-injective-pn** and qualifies **2-chern-ring-gamma-comparison**. **Confidence:** high, by the rank and coefficient arguments in Appendix B.

The margin “si on adjoint … $nL-1$” imposes $c^n(nL-1)=\xi^n=0$, because $c(nL-1)=(1+\xi)^n$, giving $C(K,\{L,nL-1\})=\mathbb Z[\xi]/\xi^n$. For $n\geq3$, $nL-1$ is geometric but is not generated from $L$ by the stated positive operations and inverses of rank-one elements; thus this is a genuine enlargement of the family. This also furnishes the example promised by scan 029: an admissible Chern theory for the smaller family can have a nonzero high Chern component on another geometric element.

### L10 — Finite exterior degree only forces factorial annihilation of high Chern components

**Cote/scan:** 2/025, lines 4–10. **Kind:** unproved claim, with a verifying example. **Context:** bears on both Chern-ring Hua IDs; the supplied context contains no separate entry for this proposition.

The replacement of the deleted $x^i=0$ by “$(i-1)!x^i=0$” records an important integral distinction. A finite exterior degree in $\widetilde A$ forces factorial annihilation of high Chern coefficients, not their vanishing in arbitrary torsion coefficient rings. Appendix B's $n=3$ example realizes the distinction: the image of $3L-1$ is geometric of rank two but has the nonzero coefficient $\xi^3$, killed by $2!$.

### L11 — The next-degree torsion criterion can be checked in a genuinely truncated ring

**Cote/scan:** 2/025, lines 12–16. **Kind:** own verification with a hypothesis clarification. **Context:** no exact context match for the truncated criterion; it bears on the torsion mechanism in **2-chern-ring-not-injective-pn**. **Confidence:** high under the explicit truncation stated here.

The assertion “il faut et il suffit … $n!x^{n+1}=0$” is valid for a graded ring with all components above $n+1$ zero, as the finite-difference calculation in Appendix E shows. Interpret the manuscript's $A^{n+2}=0$ as a degree-cutoff/filtration condition for this verification; vanishing of just one homogeneous component would be a weaker statement and is not substituted silently. The calculation isolates the first degree in which torsion can let a geometric element have a Chern coefficient above its rank.

### L12 — The live unshifted gamma expression needs a reading/meaning check

**Cote/scan:** 2/025, lines 20–35. **Kind:** reading question / literal counterexample. **Context:** no exact counterpart in the context; relevant to the hypotheses of **2-chern-ring-gamma-comparison**. **Confidence:** high for the counterexample under the package's standard gamma convention; no confidence judgment about the original ink is added here.

The live corollary has $\gamma^m(x)$, with the rank subtraction deleted, whereas its subsequently deleted proof uses $\gamma^m(X-n)$. Read literally with $n=\varepsilon(x)$, it fails for $K=\mathbb Z[L,L^{-1}],x=L,n=1,m=2$: $\gamma^2(L)=L$, while the higher exterior powers vanish and weight-at-least-three gamma terms lie in $(L-1)^3$. The shifted expression $\gamma^m(x-n)$ does belong to the ordinary ideal generated by $\lambda^j(x)$, $j>n$, directly from the generating-function identity in Appendix F; neither this observation nor the deleted proof authorizes a change to the frozen transcription.

### L13 — The determinant condition is redundant under the full definition

**Cote/scan:** 2/028, lines 25–43. **Kind:** self-flagged question, with a conditional answer. **Context:** no determinant match in the supplied context; bears on **2-chern-ring-gamma-comparison**.

The words “conséquence des autres??” are answered affirmatively when “the others” include the full lambda-homomorphism requirement and the selected rank bound. Indeed, if $c(E)=[n,1+a_1+\cdots+a_n]$, then $c(\lambda^nE)=\lambda^n c(E)=[1,1+a_1]$, giving $c^1(E)=c^1(\det E)$. This is SGA 6, V, Proposition 6.6.1(ii), pp. 350–351; it fails for the weaker relation list, as Appendix A shows (Berthelot, 1971).

### L14 — The filtration question has an answer under the stated generating hypothesis

**Cote/scan:** 2/029, line 30; compare 021, lines 4, 31–45, and 023, lines 12–16. **Kind:** self-flagged question / own verification. **Context:** **2-chern-ring-gamma-comparison** mentions the gamma filtration but does not record this question. **Confidence:** high, because Appendix D supplies a free-lambda-ring and quotient argument.

“À voir … [si les $E_s$ engendrent] ???” asks whether gamma monomials in all augmentation-zero elements can be replaced by gamma monomials in the chosen generators. For a special augmented lambda ring ring-generated by the stated finite-rank geometric $E_s$, the answer is yes: the canonical gamma filtration is the image of the free ring's weight filtration. This addresses the filtration only; it does not imply that enlarging the admissible geometric family leaves the universal Chern ring unchanged.

### L15 — The first possible prime obstruction follows from the comparison

**Cote/scans:** 2/022, lines 37–58. **Kind:** own idea / unpursued implication. **Context:** bears on both Hua IDs; the precise prime-by-degree bound has no matching context entry. **Confidence:** high, from the factorial annihilator and Appendix B.

The factorial comparison implies that the $p$-primary part of the kernel is zero in degrees $i\leq p$. The smaller-family example with $n=p+1$ has a nonzero $p$-primary kernel in degree $p+1$, since $C^{p+1}\cong\mathbb Z/p!$. This is a useful sharpness test for the degree bound in this family-dependent setting, not a claim of a new theorem.

### L16 — The unfinished proposition is explicitly withdrawn

**Cote/scan:** 2/022, line 60. **Kind:** self-flagged / withdrawn in the same text. **Context:** no exact context counterpart; related to both Hua IDs through the admissible-family issue.

The struck proposition begins “à prouver directement” and starts an equivalence concerning the chosen geometric family, but its second condition is not completed in the frozen text. It is evidence of an unfinished proof obligation and a withdrawn formulation. Do not reconstruct a theorem from it or use it to erase the family distinction subsequently made on scan 029.

## Standing questions within this block

The explicit checks/questions are scan 022's bijectivity question, answered “Non” on the same page; the struck “à prouver directement” proposition on scan 022; the determinant redundancy question on scan 028; and the “À voir” filtration question on scan 029. “Vérification immédiate!” on scan 021 and the easy-verification assertions on scan 022 are unexpanded proof claims, not explicit admissions of uncertainty. No title sheet or page-count statement occurs in the reviewed block; the marginal numerals are page numerals, not counts of pages in a text.

## Appendix A — Countermodel to the abbreviated relation list

This is the reviewer's construction, not a reading inserted into the manuscript. Let

\[
K=\mathbb Z[a^{\pm1},b^{\pm1}]^{\mathfrak S_2}
  =\mathbb Z[x,y,y^{-1}],\qquad x=a+b,\quad y=ab,
\]

with $a,b$ line elements, $\varepsilon(x)=2,\varepsilon(y)=1$. Thus $\lambda^2x=y$. Choose as the geometric family the classes of finite-dimensional algebraic representations of $GL_2$ over a characteristic-zero field; it contains $x,y,y^{-1}$, is closed under the positive operations, and ring-generates $K$.

Set $A=\mathbb Z[\epsilon]/\epsilon^2$, with $\deg\epsilon=1$. For this target the completed Chern ring has underlying elements $[r,1+u]$, $u\in A^1$, and multiplication

\[
[r,1+u]\,[s,1+v]=[rs,1+su+rv].
\]

There is therefore a unique augmented ring map $f:K\to\widetilde A$ with

\[
f(x)=[2,1],\qquad f(y)=[1,1+\epsilon],\qquad
f(y^{-1})=[1,1-\epsilon].
\]

Explicitly, for a Laurent polynomial $P(x,y)$, $f(P)=[P(2,1),1+\partial_yP(2,1)\epsilon]$. The positive-family closure and this countermodel were independently checked by a second research reviewer.

Its coefficient functions satisfy the unit, Whitney, and product equations. Every nonzero member of the positive geometric family has rank at least one, so all above-rank conditions hold automatically because $A^{\geq2}=0$. But

\[
f(\lambda^2x)=f(y)=[1,1+\epsilon]
\ne [1,1]=\lambda^2f(x).
\]

In the gamma associated graded of $K$,

\[
\gamma^2(x-2)=y-x+1\in F^2_\gamma K,
\]

so the natural degree-one Chern classes of $x$ and $y$ coincide. In the ring defined only by the abbreviated equations, their difference maps to $\epsilon$ under $f$, which has infinite additive order. Thus the literal weakened presentation cannot have the claimed factorial-annihilated kernel even in degree one. This does not refute the manuscript's lambda-homomorphism universal problem; it explains why that requirement must remain explicit.

## Appendix B — Complete verification of the projective-space example

### B1. The quotient really is a special lambda ring

Let $R=\mathbb Z[L,L^{-1}]$, with $L$ a line element, and $J=((L-1)^n)$. Its quotient is $\mathbb Z[y]/y^n$, $y=L-1$, because $1+y$ is invertible modulo $y^n$; in particular it is free over $\mathbb Z$. Adams operations satisfy $\Psi^r(L)=L^r$, so they preserve $J$, since $L^r-1$ is divisible by $L-1$. For every $a\in J$, Newton's identities imply

\[
m\lambda^m(a)=\sum_{r=1}^{m}(-1)^{r-1}\lambda^{m-r}(a)\Psi^r(a)\in J.
\]

The torsion-freeness of $R/J$ now gives $\lambda^m(a)\in J$. This explicitly supplies the integral step that Adams stability alone would not justify for an arbitrary quotient with torsion.

### B2. The universal coefficient ideal includes all relations

An admissible image of $L$ has the form $[1,1+\xi]$. This is a line element of $\widetilde A$, so it determines a unique lambda homomorphism $R\to\widetilde A$. The image of $(L-1)^n$ has rank zero and total Chern series

\[
P_n(\xi)=\prod_{j=0}^{n}(1+j\xi)^{(-1)^{n-j}\binom nj}.
\]

Consequently

\[
C(K,\{L\})=\mathbb Z[\xi]/I_n,\qquad
I_n=(a_{n,m}\xi^m:m\geq1),\qquad
P_n(z)-1=\sum_{m\geq1}a_{n,m}z^m.
\]

This is an ideal generated by **all homogeneous coefficients**, not one inhomogeneous relation with unspecified higher terms. Once the generator $(L-1)^n$ maps to zero, all its ordinary ideal multiples map to zero because the map is a ring homomorphism; compatibility with lambda operations is already built into the map from the free line ring and the verified lambda quotient. There are no additional unnoticed conditions from those multiples.

The finite-difference identity

\[
\sum_{j=0}^{n}(-1)^{n-j}\binom njj^m=0\ (m<n),
\qquad
\sum_{j=0}^{n}(-1)^{n-j}\binom njj^n=n!
\]

applied to $\log P_n(z)$ gives

\[
P_n(z)=1+(-1)^{n-1}(n-1)!z^n+O(z^{n+1}).
\]

There are no lower-degree relations, and higher homogeneous relations cannot create a degree-$n$ relation. Hence $C^n(K,\{L\})=\mathbb Z/(n-1)!$. The gamma filtration of $K$ is the $y$-adic filtration, so $\operatorname{gr}_\gamma K=\mathbb Z[\bar y]/\bar y^n$; the degree-$n$ class just exhibited lies in the kernel and is nonzero precisely when $n\geq3$.

For $n=3$,

\[
P_3(z)=\frac{(1+z)^3(1+3z)}{(1+2z)^3},\qquad
(1+z)^3(1+3z)-(1+2z)^3=2z^3+3z^4.
\]

Multiplication by the integral formal unit $(1+2z)^3$ does not change the ideal generated by all homogeneous coefficients. Thus $I_3=(2\xi^3,3\xi^4)=(2\xi^3,\xi^4)$. Equivalently, the first series coefficients are $2,-9,30,-88$ in degrees $3,4,5,6$; the first two already force the displayed ideal.

### B3. Positive closure and the additional geometric element

Starting with $L$, closure under addition, multiplication, exterior powers, and inversion of rank-one elements produces nonnegative Laurent sums $\sum a_kL^k$, $a_k\geq0$. If $nL-1$ were such a sum in $K$, for $n\geq3$, comparison of coefficients of $1,y,y^2$ would give

\[
\sum a_k=n-1,\qquad \sum ka_k=n,\qquad
\sum \binom{k}{2}a_k=0.
\]

For every integer $k$, $\binom{k}{2}\geq0$, with equality only at $0,1$; the last equation therefore contradicts the first two. Thus adjoining $nL-1$ is not just repeating this closure.

Nevertheless $nL-1$ is geometric: $\lambda_t(nL-1)=(1+Lt)^n/(1+t)$ is a polynomial of degree at most $n-1$ because $(1-L)^n=0$, and its top coefficient is $L^n$, a unit. The added rank bound imposes $c^n(nL-1)=\xi^n=0$, and all previous coefficient relations then vanish, yielding exactly $\mathbb Z[\xi]/\xi^n$. In the smaller-family target the same element is geometric while its $n$-th Chern coefficient is nonzero factorial torsion; this proves the distinction made in scans 025 and 029.

## Appendix C — Modified multiplication, comparison maps, and degree zero

Put $A^!=\operatorname{gr}_{\deg}\widetilde A$. In positive degrees its additive group is $A^i$, whereas degree zero comes from the rank ring $\mathbb Z$. For an element beginning with $1+a_i$, the leading rational Chern-character term is $(-1)^{i-1}a_i/(i-1)!$. Multiplying two such terms and comparing the leading coefficient in degree $i+j$ gives

\[
a_i\star b_j=-\frac{(i+j-1)!}{(i-1)!(j-1)!}a_ib_j.
\]

The coefficient is integral; the computation can be made in the torsion-free universal polynomial ring and then specialized, so it is not an argument that discards torsion in the target. Let $d_i=(-1)^{i-1}(i-1)!$. Then $d_ia\star d_jb=d_{i+j}ab$, explaining why the degreewise factorial rescaling is compatible with the modified multiplication.

For the intended universal lambda theory, the natural gamma Chern classes define a surjective graded-ring map $\phi:C(K,S)\to\operatorname{gr}_\gamma K$. The universal Chern map is filtered for the degree filtration on its completed target and hence induces a graded-ring map $\psi:\operatorname{gr}_\gamma K\to C(K,S)^!$. On the underlying positive-degree groups the two composites are multiplication by $d_i$: one uses the leading gamma identity on $F^i_\gamma K$, the other uses that identity on the universal Chern generators together with the displayed product rule. The conclusions concerning torsion, rational isomorphism, and degrees one and two therefore concern the intended lambda-compatible object, not Appendix A's weaker ring.

## Appendix D — The filtration generated by the selected elements

Let $B$ be the free special lambda ring on geometric generators $X_s$ of ranks $n_s$, with their top exterior powers inverted. Set $z_{s,i}=\gamma^i(X_s-n_s)$, $1\leq i\leq n_s$. As an ordinary ring,

\[
B=\mathbb Z[z_{s,i},(1+z_{s,1}+\cdots+z_{s,n_s})^{-1}]_{s\in S}.
\]

Embed it in the Laurent polynomial ring on independent line roots $L_{s,j}$, putting $u_{s,j}=L_{s,j}-1$. Each $z_{s,i}$ becomes the elementary symmetric polynomial of degree $i$ in the corresponding $u$'s. The inverse determinant factors have constant term one, so intersection with powers of the roots' augmentation ideal is exactly the weight filtration $\operatorname{wt}z_{s,i}=i$.

In the line-root ring, every augmentation-zero element is an integral sum of differences $M-1$ for Laurent monomials $M$, and $\gamma_t(M-1)=1+(M-1)t$. Its $i$-th gamma operation therefore has augmentation order at least $i$; this proves that the canonical gamma filtration of $B$ is contained in the weight filtration. The reverse inclusion follows because the $z_{s,i}$ themselves are gamma generators, proving equality integrally.

The augmented lambda map $B\twoheadrightarrow K$ exists and is surjective under the manuscript's ring-generating hypothesis. Every augmentation-zero element of $K$ has an augmentation-zero lift, so every defining gamma monomial lifts; hence the gamma filtration on $K$ is the image of that on $B$. Its pieces are therefore generated by the weighted monomials in $\gamma^i(E_s-\varepsilon E_s)$, which answers scan 029's question under these hypotheses. This argument does not identify the selected geometric family with all geometric elements.

## Appendix E — The truncated next-degree criterion

Assume $A^{>n+1}=0$, and let $x=[n,1+a_1+\cdots+a_n+a]$, $a\in A^{n+1}$. Write $x=X+y$ in the additive law of the Chern ring, with $X=[n,1+a_1+\cdots+a_n]$ and $y=[0,1+a]$; cross terms with $a$ vanish by the cutoff. The element $X$ has exterior degree at most $n$.

On the top-degree square-zero subgroup, the universal lambda identities give

\[
\lambda^k(y)=(-1)^{k-1}k^n y\quad(k\geq1).
\]

This identity is first calculated over the universal torsion-free square-zero coefficient ring, then specialized. In multiplying $\lambda_t(X)\lambda_t(y)$, only the ranks $\binom nj$ of the coefficients of $\lambda_t(X)$ act on $y$. Thus, for $k>n$, the $y$-coefficient of $\lambda^k(x)$ is

\[
(-1)^{k-1}\sum_{j=0}^{n}(-1)^j\binom nj(k-j)^n
 =(-1)^{k-1}n!.
\]

Therefore all $\lambda^k(x)$, $k>n$, vanish if and only if $n!a=0$. The statement is about an actual truncation; this proof does not replace it by the vanishing of a single graded component.

## Appendix F — The shifted gamma identity and the deleted proof

For $n\geq0$,

\[
\gamma_t(x-n)=(1-t)^n\lambda_{t/(1-t)}(x)
 =\sum_{j\geq0}\lambda^j(x)t^j(1-t)^{n-j}.
\]

When $m>n$, the coefficient of $t^m$ receives no contribution from $j\leq n$, and consequently $\gamma^m(x-n)$ is an integral linear combination of $\lambda^j(x)$, $n<j\leq m$. This proves membership in the ordinary ideal for that shifted expression without any quotient construction. If a quotient lambda ring is then used, stability of its defining ideal is a separate obligation; it is established explicitly for Appendix B's ideal and can also be proved for the higher-exterior-power ideal by specialization of the free lambda ring to $n$ line roots.

By contrast, for the live unshifted expression on scan 025, $\gamma^2(L)=\lambda^2(L+1)=L$. In the free line ring, the weight-at-least-three terms in gamma operations of $L-1$ generate $(L-1)^3$, which does not contain $L$. The deleted proof on scan 025 is recorded as deleted evidence for a possible intended shift, not as an intact proof or a license to amend the transcription.

## Primary literature and citation locators

Mackall's Proposition 2.1 includes rank bounds for every finite-rank bundle and injectivity under projective-bundle pullback; his $B(X)$ is therefore not automatically $C(K,S)$ for a smaller chosen family. Theorem 4.1 gives the two factorial composites for $i>0$, and Example 3.9 computes the Grassmannian cases, including projective space. These are comparisons, not novelty evidence for the manuscript's smaller-family example. **Bibliographic caution:** arXiv v1, p. 8, displays a gamma-Chern convention using $\gamma^i(\operatorname{rk}F-[F^\vee])$; taken literally, a line-bundle test conflicts with the stated rank bound, so the convention used in this review is the directly checked SGA 6, V, (6.7.1), not that display. The journal PDF was not checked for a correction.

- Berthelot, P. (1971). Généralités sur les $\lambda$-anneaux. In P. Berthelot, A. Grothendieck, & L. Illusie (Eds.), *Théorie des intersections et théorème de Riemann–Roch (SGA 6)* (Lecture Notes in Mathematics, Vol. 225, pp. 297–364). Springer. https://doi.org/10.1007/BFb0066289
- Mackall, E. (2020). Universal additive Chern classes and a GRR-type theorem. *Journal of Algebra, 560*, 1173–1189. https://doi.org/10.1016/j.jalgebra.2020.06.018 . Author preprint: https://arxiv.org/abs/2006.14664 ; full text: https://arxiv.org/pdf/2006.14664

The following original SGA 6 printed pages were visually inspected from the SLMath archive, rather than from a modern reconstruction or translation:

| Original locator | Verified use | Stable original-page URL  |
|---|---|---|
| V, (6.5.3), p. 349 | Modified product | https://library.slmath.org/nonmsri/sga/sga/6/6t_349.html  |
| V, 6.6.1(ii), pp. 350–351 | Determinant's first Chern coefficient | https://library.slmath.org/nonmsri/sga/sga/6/6t_350.html  |
| V, 6.6.4, p. 352 | Leading factorial gamma coefficient | https://library.slmath.org/nonmsri/sga/sga/6/6t_352.html  |
| V, (6.7.1), 6.8, pp. 353–354 | Rank-subtracted gamma classes; completed lambda homomorphism | https://library.slmath.org/nonmsri/sga/sga/6/6t_353.html ; https://library.slmath.org/nonmsri/sga/sga/6/6t_354.html  |
| V, 6.9, pp. 354–355 | Sign and factorial comparison | https://library.slmath.org/nonmsri/sga/sga/6/6t_354.html ; https://library.slmath.org/nonmsri/sga/sga/6/6t_355.html  |
| V, 6.13–6.14, pp. 358–360 | Universal lambda-compatible Chern theory and explicit gamma relations | https://library.slmath.org/nonmsri/sga/sga/6/6t_358.html ; https://library.slmath.org/nonmsri/sga/sga/6/6t_359.html  |
| Mackall, Proposition 2.1; Theorem 4.1 | Distinct universal problem; positive-degree factorial composites | https://arxiv.org/pdf/2006.14664  |
| Mackall, Example 3.9 | Grassmannian comparison | https://arxiv.org/pdf/2006.14664  |
| Mackall, journal metadata | Volume, pages, DOI | https://www.sciencedirect.com/science/article/pii/S0021869320303161  |

Original literature images used for inspection are temporary reference material and are not part of the deliverable. The source transcriptions and combined fragment remain unchanged.
