# Final research-note peer review: Part 3 and the gluing example

**Record prepared:** 2026-11-18 **02:34:10 UTC** (clock reading).

**Reviewer:** ChatGPT, GPT-6 Astra Pro; effort inherited/unspecified; agent `/root/norm_research`; run **MPL98**.

**Scope:** Mathematical and source-status review of the root's `research/note_entries_part3.json`, principally T02–T12, followed by an independent check of the root-proposed finite-topology example T13. Only research drafts and the primary references below were inspected. Manuscript images, page files and combined transcription were not inspected. Reported source quotations were treated as supplied data, without certifying their ink. The root reports applying the recommended revisions; this record does not claim a subsequent audit of the revised note draft. Individual earlier check times were not separately captured; the accompanying event dates are the actual UTC date of the checks, and the timestamp above records preparation of this final review record.

## 1. Recommendations returned to the root

| Item | Review result and recommended revision |
|---|---|
| T02 | State the saturation and openness/closedness hypotheses and the universal quantifier over subsets. A quotient map need not restrict to a quotient on every subspace. The precise criterion is proved below. |
| T03 | Overlap homeomorphisms alone do not ensure embeddings. For the usual compatible gluing construction, state the sufficient hypotheses as **all overlaps open in both pieces**, or **all overlaps closed in both pieces**. Arbitrary mixed or one-sided conditions are insufficient; T13 proves this. |
| T04–T05 | The original research-draft formulas were damaged during string escaping: T04 lost TeX command backslashes; T05 contained a tab and vertical-tab in the intended arrow and dual-variety notation. These are research-draft encoding defects, not manuscript readings. |
| T05 | Specify the zero-map criterion as `φ_L=0` iff `[L]∈Pic^0(A)`. It is distinct from the finite-kernel criterion. A finite scheme-theoretic kernel for `φ_L:A→A^∨` gives an isogeny because the varieties have equal dimension. |
| T06–T07 | The finite-dimensional flag and preceding-prefix rank-nullity repair are sound. Explicitly retain the nonzero finite-dimensional ambient space, injective expansion map and, for rationality, the ambient space and coefficient functionals defined over `K`. |
| T08 | The monomial-tail ideal check is valid in the formal power-series/local expansion ring when the enumeration is nondecreasing in total degree. Its intersection with a finite-dimensional function space is a vector-space flag; that intersection is not thereby an ideal of the whole ring. |
| T09 | The effective nondegenerate-to-ample comparison is supported by Milne's Proposition 9.1. Cite **Remark 7.3**, rather than Theorem 7.1, for a suitable power of a specified ample line bundle being very ample. Theorem 7.1 asserts projectivity of the variety. Retain the tangent-direction condition in the closed-immersion comparison. |
| T10 | Prefer “possible marginal query” to “possible self-flag”: the latter can suggest that the pencil annotator is the typescript's author, although neither hand nor authorship was identified. |
| T11–T12 | The proposed index-zero and divisor-operator repairs are conditional mathematical readings, not independently certified source corrections. Keep that distinction explicit. |

The Picard pullback identity in T04 is valid for `L∈Pic^0(A)`; it must not be generalized to arbitrary divisor classes. The review found no basis for assigning the reused typescript or pencil annotations to a particular author. Most of the draft's prose already preserved that distinction.

## 2. T02: precise quotient-subspace criterion and proof

Let `f:X→Y` be a quotient map, let `A⊂X`, and give `A` and `f(A)` their subspace topologies. Write `g=f|_A:A→f(A)`. A subset `B⊂A` is **relatively saturated** if

\[
B=g^{-1}(g(B))=A\cap f^{-1}(f(B)).
\]

The following conditions are equivalent:

1. `g` is a quotient map.
2. For every relatively saturated subset `B⊂A` that is open in `A`, its image `f(B)` is open in `f(A)`.
3. For every such `B`, there exists a saturated open subset `D⊂X` such that `B=A∩D`.

Each condition also has an equivalent version with **closed** replacing **open**. The image formulation in condition 3 is

\[
f(B)=f(A)\cap f(D),
\]

where `f(D)` is open in `Y` because `D` is saturated and open and `f` is a quotient map. Equivalently, `f(B)` is the trace on `f(A)` of an open subset of `Y`.

**Proof.** The restriction `g` is continuous and surjective. If it is quotient and `B` is relatively saturated, then `g^{-1}(f(B))=B`, so openness of `B` gives openness of `f(B)` in `f(A)`. This proves 1⇒2. Conversely, given `U⊂f(A)` whose inverse image under `g` is open, take `B=g^{-1}(U)`. It is relatively saturated and satisfies `f(B)=U`; condition 2 makes `U` open. Thus 2⇒1.

Assume condition 2. Choose an open subset `V⊂Y` with `f(B)=f(A)∩V`, and put `D=f^{-1}(V)`. Then `D` is saturated and open, and

\[
A\cap D=g^{-1}(f(B))=B.
\]

Thus 2⇒3. Conversely, if `B=A∩D` with `D` saturated and open, saturation implies `f(A∩D)=f(A)∩f(D)`. Since `f(D)` is open in `Y`, `f(B)` is relatively open in `f(A)`. This proves 3⇒2. Taking complements proves the closed versions. ∎

The proof does **not** assert that the required `D` exists for every restriction of every quotient map. Its existence is precisely part of the criterion being tested. The root's proposed replacement of the self-referential trace base by `f(A)` is mathematically consistent with this criterion; this review does not establish that it was the typescript's intended wording.

## 3. T13: formal proof of the three-piece finite-topology counterexample

Take three initially disjoint spaces, using subscripts to distinguish copies:

\[
X_1=\{a_1,b_1\},\qquad
X_2=\{a_2,c_2\},\qquad
X_3=\{c_3,b_3\}.
\]

Give `X_1` the discrete topology, and set

\[
\begin{aligned}
\tau_2&=\{\varnothing,\{c_2\},\{a_2,c_2\}\},\\
\tau_3&=\{\varnothing,\{b_3\},\{c_3,b_3\}\}.
\end{aligned}
\]

Glue equal labels by `a_1∼a_2`, `c_2∼c_3` and `b_3∼b_1`. Each overlap is a singleton with its unique topology, so every overlap identification is a homeomorphism. No triple overlap is nonempty, and the inverse/cocycle compatibility conditions hold. Every equivalence class meets any one piece in at most one point.

The quotient set is `Q={a,c,b}`. By the definition of the quotient topology from the disjoint union, `U⊂Q` is open exactly when its inverse image in each `X_i` is open. The discrete first piece imposes no restriction. The second piece imposes

\[
a\in U\ \Longrightarrow\ c\in U,
\]

and the third imposes

\[
c\in U\ \Longrightarrow\ b\in U.
\]

Hence the complete list of quotient opens is

\[
\tau_Q=\{\varnothing,\{b\},\{b,c\},\{a,b,c\}\},
\]

the upper-set topology of the chain `a<c<b`. The induced topology on the image `{a,b}` of `X_1` is

\[
\{\varnothing,\{b\},\{a,b\}\}.
\]

In particular, `{a}` is not open in that subspace, although `{a_1}` is open in `X_1`. Thus the canonical map `X_1→Q` is continuous and injective but is **not** a homeomorphism onto its image. It is not an embedding. ∎

This verifies that compatible homeomorphisms of overlaps alone are insufficient. The example does not satisfy either uniform sufficient hypothesis from T03: not all overlaps are open in both pieces, and not all are closed in both pieces. In addition to the proof, an actual Python enumeration of all eight subsets of `Q` returned exactly the four opens and the three induced opens displayed above. That finite computation is recorded as such, not as a theorem-prover certificate.

## 4. T06: scope of the flag and rationality argument

For precision, let `V` be a nonzero finite-dimensional `K`-vector space injected into a formal expansion space, with coefficient functionals `c_j:V→K` separating its elements. Put

\[
V_s=\bigcap_{0\le j<s}\ker(c_j),\qquad V_0=V.
\]

Then each dimension drop is at most one, and `∩_s V_s=0`. A descending chain in a finite-dimensional vector space stabilizes, so some `V_s` is zero. If `m` is the first such index, `V_{m-1}` is nonzero and has dimension at most one, hence exactly one. It is a `K`-subspace and has a nonzero `K`-generator. When the original functions and basis are themselves defined over `K`, this gives the corresponding function over `K`.

A full-rank homogeneous system on `dim(V)` unknowns has zero kernel. If rows are added one at a time and the first full-rank prefix ends at index `s`, the immediately preceding prefix ending at `s−1` has rank `dim(V)−1`, hence one-dimensional kernel. This verifies the proposed mathematical repair without certifying the reported source indices. It also explains why injectivity of expansions and the `K`-structure must not be inferred merely from the dimension count.

## 5. Primary references actually checked in this review

- **Milne, J. S. (2022, January 2).** *Abelian varieties* [Corrected author version of the chapter originally published in 1986]. https://www.jmilne.org/math/xnotes/AVs.pdf . Checked version declaration; Proposition 8.1; Propositions 9.1–9.2 and the following Picard pullback/multiplication formulas; Theorem 7.1 and Remark 7.3. Cite as **Milne (1986/2022)** with these unchanged section numbers. The supporting references to Mumford were not independently inspected by this review.
- **Milne, J. S. (2008).** *Abelian varieties* (Version 2.0) [Course notes]. https://www.jmilne.org/math/CourseNotes/AV.pdf . Checked Chapter I §6, Definition 6.2 and Proposition 6.3, including the base-point-free hypothesis and separation of points and tangent directions. The cited Hartshorne sufficiency proof was not independently inspected.

No edits were made to the root's research-note draft, source ledger, transcription, or another agent's files while preparing this record.
