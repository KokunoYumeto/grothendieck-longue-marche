# Independent check of the parent's prefix-tower counterexample, scan 183

Checker: GPT-6 Astra Pro, `/root/research_finite`; effort setting not exposed. Date: 2026-11-18. The example was proposed by `/root`; this file records a mathematical review and one strengthening. No scan image was opened. Sources read: the frozen fragment `pages/MPL_29_141-187_29_scan183.tex`, and Hua's project, `context/hua_project/29.modern.tex`, “Quand un foncteur est pro-représentable” under “Foncteurs semi-cosimpliciaux, et le van Kampen” (their page 182 = our scan 183). Hua repeats the sufficiency claim; it is not treated as established. Actual context-search matches are appended to `research_finite_context_search.tsv` under `RF183-review`.

## Statement under review

Scan 183 says that left exactness, preservation of filtered intersections of subsets, strict pro-representability, and surjectivity of all projections from the inverse limit suffice for $F(J)=C(K,J)$ with $K$ given the inverse-limit topology of discrete stages. The displayed phrase is “Ces conditions sont néc et suffisantes”. The parent's construction is

$$X_n=\mathbb N^n,\qquad F(J)=\varinjlim_n\operatorname{Hom}(X_n,J),\qquad K=\varprojlim_nX_n=\mathbb N^{\mathbb N},$$

with coordinates numbered $0,1,2,\ldots$ and transition maps deleting the last coordinates. Include $n=0$ if desired; this does not affect the argument. Every transition map is surjective, so precomposition gives an injection between the corresponding Hom-sets. An element of $F(J)$ is exactly a function on $K$ depending on a bounded finite prefix.

## Condition (a): left exactness

$F(1)$ is a singleton. Given finitely many functions representing elements of $F(J_i)$, pass to one common stage $n$; their product is represented by the map into the finite product at that stage. If two such product representatives have the same coordinates in the colimit, pass again to a common stage witnessing those finitely many equalities. Thus $F$ preserves finite products.

For maps $a,b:J\rightrightarrows L$, an element represented by $u:X_n\to J$ lies in the equaliser of $F(a),F(b)$ precisely when $au$ and $bu$ agree after precomposition by some surjective truncation $X_m\to X_n$. Surjectivity then implies $au=bu$, so $u$ already lands in the set-theoretic equaliser of $a,b$. This proves preservation of equalisers and therefore finite limits directly, without relying on an external interchange theorem.

**Outcome:** (a) holds.

## Condition (b): in fact all intersections are preserved

Let $A_\alpha\subseteq J$ be any family, with no filteredness assumption. If $[u]\in F(J)$, represented by $u:X_n\to J$, lies in the image of every $F(A_\alpha)$, then for each $\alpha$ some map into $A_\alpha$ becomes equal to $u$ at a later stage. All transition maps are surjective, so the image of $u$ is unchanged at every later stage. It follows that $u(X_n)\subseteq A_\alpha$ for all $\alpha$, and therefore $u$ factors through $\bigcap_\alpha A_\alpha$. The reverse inclusion is automatic.

**Outcome:** $F(\bigcap A_\alpha)=\bigcap F(A_\alpha)$ for arbitrary intersections, stronger than (b).

## Strictness and condition (c)

The given presentation is a strict inverse system, since every truncation is surjective. For any prefix $x\in X_n$, append infinitely many zeros to obtain a member of $K$ projecting to $x$. Thus every $K\to X_n$ is surjective, exactly as required in (c).

The natural map $F(J)\to C(K,J)$ is injective: if two finite-prefix maps agree on $K$, take a common stage and use the surjectivity of $K\to X_n$ to see that their stage maps agree.

## A continuous map missing from the colimit

Define the parent's map

$$g(x)=x_{x_0+1}.$$

At a point $x$ with first coordinate $m$, fixing the first $m+2$ coordinates fixes $g$, so $g:K\to\mathbb N$ is continuous for the discrete target. For any fixed prefix length $n$, choose $m\geq\max(n,1)$ and two sequences with $x_0=m$, identical first $n$ coordinates, but different $(m+1)$st coordinates. Their values under $g$ differ, so $g$ does not factor through $X_n$ for any $n$.

One can strengthen the witness to the finite target $\{0,1\}$:

$$h(x)=x_{x_0+1}\pmod 2.$$

The same continuity and nonfactorisation argument applies, choosing the selected coordinate to be $0$ and $1$. Thus even $F(\{0,1\})\to C(K,\{0,1\})$ is not surjective. This is a concrete clopen subset of the inverse-limit space which is not determined by a bounded finite prefix.

**Outcome:** the sufficiency assertion for the specified inverse-limit topology is refuted.

## Strengthening: no alternative topological space represents this functor

Suppose there were a natural isomorphism $F(J)\simeq C(L,J)$ for some topological space $L$, with all targets discrete. The universal element $[\operatorname{id}_{X_n}]\in F(X_n)$ gives a continuous map $q_n:L\to X_n$, and naturality gives the compatibility of the $q_n$ with truncation.

Each $q_n$ must be surjective. Indeed, let $A=q_n(L)\subseteq X_n$; because the target is discrete, $q_n$ factors continuously through $A$. Naturality would place $[\operatorname{id}_{X_n}]$ in the image of $F(A)\to F(X_n)$, which is impossible for a proper subset $A$: equality at any later stage would require a surjective truncation into $X_n$ to have image contained in $A$.

Now define $h_L$ by using the first coordinate of $q_1$ to choose the coordinate in $q_{m+2}$ and then taking its parity. On the clopen set $q_1^{-1}(m)$ this is a coordinate of a continuous map to a discrete finite product, so $h_L:L\to\{0,1\}$ is continuous. By the supposed representation it has the form $v\circ q_n$ for some map $v:X_n\to\{0,1\}$. Choose $m\geq\max(n,1)$ and two prefixes in $X_{m+2}$ with first coordinate $m$, equal first $n$ entries, and selected-coordinate parities $0$ and $1$; surjectivity of $q_{m+2}$ supplies two points of $L$ witnessing a contradiction.

**Outcome:** no topological space $L$ represents this $F$ by all continuous discrete-valued functions. This strengthening does not require $L$ to be totally separated. It also distinguishes the counterexample from a mere choice of an inconvenient inverse system.

## Limits of this review

This check does not refute the separate abstract equivalence between an appropriate small left-exact intersection-preserving functor and a strict pro-object; the counterexample is itself a strict pro-object. It does not refute the compact finite-stage case, where compactness supplies a uniform finite-coordinate bound. It makes no claim about the manuscript's final statement involving $\pi_0(L)$ or the cited Bourbaki proposition.
