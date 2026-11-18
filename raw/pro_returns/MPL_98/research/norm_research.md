# MPL 98: norm sections, categorical axioms, and primary comparisons

Research memorandum by ChatGPT, GPT-6 Astra Pro (inherited effort setting not exposed), run **MPL98**, research agent `norm_research`. Prepared after the root agent's reported transcription freeze, **2026-11-18 01:36:35 UTC**. This agent did not view manuscript images, read page transcriptions, or read the combined transcription. Its manuscript locations are **context leads only**: Hua's page *p* corresponds to archive scan *p* + 1 according to the supplied context. The root agent must decide what the frozen manuscript actually says.

## 1. Executive findings and disposition of the supplied claim

The supplied **Hua, findings register, `98-axiomatic-norms-can-section`**, at `context/notes/RESULTS_STATE.md:460`, has status **conjecture (unsearched), Lean card partly proved**. The modernization's G-set proofs and finite-free permutation-basis argument belong to Hua's project. The present run independently checks those elementary arguments, supplies the algebraic compatibilities, and identifies qualifications. It does **not** certify the absent Lean source or turn an axiom list into an existence theorem for arbitrary categories.

| Check ID | Finding | Status of this run |
|---|---|---|
| MPL98-NORM01 | The top alternating image in a rank-*n* projective module's tensor power is stable under symmetric tensor endomorphisms over every commutative ring. Inverting *n*! is unnecessary. | Independent proof below; a claim that factorial inversion is necessary is refuted in this scope. |
| MPL98-NORM02 | A finite locally free rank-*r* morphism has a determinant-norm section into its relative symmetric power, including ramified morphisms. | Independent construction and base-change check. |
| MPL98-NORM03 | For permutation actions on tensor factors, quotient degree is `card(E^n/H)`, and formation commutes with arbitrary base change. | Independently rechecked Hua's stated orbit-basis argument. |
| MPL98-NORM04 | Norm sections satisfy normalization, disjoint-sum compatibility and transitivity. | Independent algebraic checks; exact published comparator located. |
| MPL98-NORM05L / 05R | A single natural-number degree function with all the displayed axioms conflicts with the empty target. A degree predicate or rank function repairs this issue. | Literal formulation refuted; refined formulation checked. |
| MPL98-NORM06 | The G-set construction satisfies the refined axioms; principal covering-space torsors transport the construction. | Independent finite-fibre proof. No Lean execution or general analytic proof. |
| MPL98-NORM07 | The Hilbert–Chow link suggested by Hua can land in `Sym`, even for a nonflat ambient space. Divided powers give the target with unrestricted base-change compatibility. | Published construction checked; scope clarified. |
| MPL98-NORM08 | The symmetric-operation construction applies when the operation descends through the relevant quotient. SGA 4's sheaf trace theorem has an explicit descent hypothesis. | Targeted source and construction check. |
| MPL98-NORM09 | SGA 6 XI cannot be cited as an inspected published proof: the 1971 preface says the exposé was not written and would not be published. | Original publisher front matter checked. |

The finite locally free scheme and finite-fibre G-set cases therefore substantially support the mathematical content of Hua's finding **after the stated refinements**. Its phrase “in any category with finite sums” describes an axiomatic package of additional structure, not a theorem deriving that structure merely from finite sums. The manuscript's exact axioms, proof claims, and punctuation remain the root agent's separate evidence question.

## 2. MPL98-NORM01: the alternating-image argument is integral

**Context lead.** Hua's modernization, §I, “Le déterminant comme loi multiplicative (page 2),” lines 275–314, says the anti-invariant description is correct when *n*! is invertible, then says that in general one must pass through Roby's polynomial laws. Its warning about the full sign-eigenspace is correct. Necessity of abandoning the integral alternating-image argument is the point corrected here; the footnote does not literally state an “if and only if” criterion involving *n*!.

**Independent proof.** Let *A* be a commutative ring and *M* free of rank *n*, with basis `e_1,…,e_n`. Write

\[
T=M^{\otimes_A n},\qquad
\operatorname{Alt}=\sum_{\sigma\in\mathfrak S_n}\operatorname{sgn}(\sigma)\sigma.
\]

On a basis tensor with repeated indices the summands cancel in pairs, including in characteristic two. A basis tensor with all indices distinct maps to a signed copy of

\[
a=\sum_{\sigma\in\mathfrak S_n}\operatorname{sgn}(\sigma)
e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(n)}.
\]

Thus `im(Alt)=Aa`. The coefficient of `e_1⊗⋯⊗e_n` in *a* is 1, so this line is free and a direct summand of the underlying module. The canonical alternating map

\[
j:\Lambda^n M\longrightarrow T
\]

is injective and has precisely that image. If `q:T→Λ^nM` is the usual quotient, then `Alt=j q`. Every endomorphism of *T* commuting with the symmetric-group action commutes with `Alt`, hence preserves both its image and its kernel. It therefore induces an endomorphism of the line `Λ^nM`. No division has occurred. The construction is basis independent; localization gives the same conclusion for every finite projective module of constant rank *n*.

For finite projective *M*, the canonical identification

\[
\operatorname{End}_A(M)^{\otimes n}\simeq
\operatorname{End}_A(M^{\otimes n})
\]

identifies permutation-invariant tensors with operators commuting with the permutations. Restriction to `im(j)` gives a unital algebra homomorphism

\[
\bigl(\operatorname{End}_A(M)^{\otimes n}\bigr)^{\mathfrak S_n}
\longrightarrow \operatorname{End}_A(\Lambda^n M)\simeq A.
\]

It sends `u^{⊗n}` to `det(u)`. This realizes the determinant polynomial law integrally.

**Counterexample to the different, stronger identification.** For `M=F_2^2`, the sign character is trivial, so the entire sign-eigenspace in `M⊗M` is the three-dimensional symmetric subspace, including `e_1⊗e_1` and `e_2⊗e_2`. The alternating image is only the one-dimensional line generated by `e_1⊗e_2+e_2⊗e_1`. Consequently, equating the exterior power with **all** sign-eigenvectors is false here; identifying it with the image of antisymmetrization is valid. Also `Alt^2=n! Alt` does not make the image vanish when *n*! vanishes.

**Published comparison.** Deligne (1973), SGA 4 XVII §6.3.1, has no characteristic restriction; its following N.B. gives a direct quotient argument when 2 is invertible. Neither condition is necessary for the image argument above.

## 3. MPL98-NORM02: determinant law and the canonical section

Let `f:X→Y` be finite locally free of constant rank *r*. Work locally on `Y=Spec(A)`, with `X=Spec(B)` and *B* projective of rank *r*. For every *A*-algebra *R*, multiplication by `b∈B⊗_A R` gives

\[
N_R(b)=\det_R(m_b:B\otimes_A R\longrightarrow B\otimes_A R).
\]

Determinants commute with scalar extension; this family is natural in *R*, homogeneous of degree *r*, and multiplicative because `m_{bc}=m_b m_c`. It is therefore a multiplicative homogeneous polynomial law. Ferrand (1998), §§2.2.4, 2.5.1 and 3.1.1–3.1.2, gives its representing algebra homomorphism

\[
\Gamma_A^r(B)\longrightarrow A.
\]

For locally free *B*, the canonical map `Γ_A^r(B)→TS_A^r(B)` is an isomorphism, where `TS_A^r(B)=(B^{⊗r})^{S_r}`. This can also be seen on a basis: divided monomials correspond exactly to orbit sums in the tensor basis. The same algebra homomorphism follows directly from §2 by letting the invariant tensors in `B^{⊗r}` act by multiplication on `B^{⊗r}` and restricting to its top alternating line. Hence

\[
\operatorname{Can}_{X/Y}:Y\longrightarrow
\operatorname{Spec}_A\operatorname{TS}_A^r(B)
=\operatorname{Sym}_Y^r(X)
\]

is a section. Naturality glues the local construction.

**Base change.** The orbit-basis argument in §4 shows that `TS^r(B)` commutes with arbitrary base change in this situation. The determinant does too, giving the asserted compatibility of `Can` as a morphism of schemes, including infinitesimal base changes.

**Exact finiteness hypothesis.** Finite locally free is equivalent to finite, flat and locally of finite presentation; over a locally Noetherian base, finite flat suffices. The rank is locally constant, so a single *r* describes a constant-rank component or a stipulated constant-rank morphism. These are Stacks Project, Tag 02K9, Definition 29.49.1 and Lemmas 29.49.2–29.49.5. The determinant construction and arbitrary base-change compatibility are also stated in Tag 0BD2, Lemma 31.18.6.

**Étaleness is unnecessary.** For `B=A[ε]/(ε^2)`, multiplication by `a+bε` has matrix `[[a,0],[b,a]]`, so its norm is `a^2`. This is a finite locally free ramified example covered by the construction.

**Finite with constant fibre length is insufficient.** Let `Y=Spec(k[η]/η^2)` and `X=Spec(k)` with its reduced closed immersion. This is finite and its unique geometric fibre has length 1, but it is not flat. For every `r≥1`, the relative tensor power of *X* over *Y*, and consequently its symmetric quotient, equals *X*. A *Y*-section `Y→X` would give an `A=k[η]/η^2`-algebra homomorphism `k→A`, forcing the nonzero element *η* of *A* to vanish. Thus no such section exists. This explicitly rules out replacing local freeness by constant geometric-fibre cardinality or length.

## 4. MPL98-NORM03: quotient degree and base change

**Context credit.** Hua's modernization, “Trois exemples,” lines 537–553, supplies the following argument as its own addition, not as a proof read from the manuscript. This run independently rechecks it.

Take *B* free of rank *r* with basis indexed by `E={1,…,r}`. For `H⊂S_n`, the tensor power `B^{⊗n}` has a basis indexed by `E^n`, and *H* permutes that basis. An invariant vector has equal coefficients at all indices in each orbit. Therefore

\[
\left(B^{\otimes n}\right)^H
=\bigoplus_{O\in E^n/H} A\left(\sum_{e\in O}e\right).
\]

This is a free module of rank `#(E^n/H)`. The expression remains the identical orbit-sum basis after any ring homomorphism `A→A'`; in particular

\[
\left(B^{\otimes n}\right)^H\otimes_A A'
\xrightarrow{\sim}
\left((B\otimes_A A')^{\otimes n}\right)^H.
\]

The affine quotient `Spec((B^{⊗n})^H)` is finite locally free of that rank. Localization gives the result for finite locally free *B*. There is no assumption that `|H|` is invertible. For `H=S_n` this rank is `binom(r+n-1,n)` for positive *r*; the orbit-count form handles all degrees with the usual empty-power conventions.

**Boundary of the argument.** This is a permutation-module assertion, not a general theorem that finite-group invariants commute with arbitrary base change. For `B=Z[ε]/ε^2` and the involution `ε↦−ε`, the invariant algebra is `Z`. After reduction modulo 2 the action becomes trivial, and the invariant algebra is `F_2[ε]/ε^2`, whereas the base change of `B^H` is only `F_2`. Thus a general invariant-quotient base-change claim would be false even for a finite free algebra.

## 5. MPL98-NORM04: normalization, sum and transitivity

### 5.1 Normalization and disjoint sums

For a rank-one identity algebra `B=A`, the norm is the identity and the section is the identity. For `B=B_1×B_2` of ranks *r₁,r₂*, multiplication matrices are block diagonal, so

\[
N_{B/A}(b_1,b_2)=N_{B_1/A}(b_1)N_{B_2/A}(b_2).
\]

Decomposing the tensor product by the choices of summand identifies the relative symmetric power of `X_1⊔X_2` with

\[
\coprod_{i+j=r}\operatorname{Sym}_Y^i(X_1)
\times_Y\operatorname{Sym}_Y^j(X_2).
\]

The norm section lands in the `(r_1,r_2)` component and is the pair of the two norm sections. The statement follows either on the orbit-sum algebra basis or from the universal polynomial law; it is not necessary to divide by binomial coefficients.

### 5.2 An independent determinant proof of transitivity

For `A→B→C` finite locally free of constant ranks *s* and *r*, respectively, one needs

\[
N_{C/A}=N_{B/A}\circ N_{C/B}.
\tag{T}
\]

Here is a direct integral argument. First suppose *B* is free over *A* and `U∈M_r(B)`. Denote by `ρ_r(U)` its block matrix on the underlying *A*-module. We claim

\[
\det_A\rho_r(U)=N_{B/A}(\det_B U).
\tag{D}
\]

Induct on *r*. The assertion for `r=1` is the definition of the norm. For the induction step replace the upper-left entry *u* of *U* by `u+t` over `A[t]`. The polynomial `q(t)=N_{B[t]/A[t]}(u+t)` is monic of degree *s*, hence a nonzerodivisor. Inverting *q* makes `u+t` invertible in `B[t,1/q]`, by the adjugate identity for its multiplication matrix (equivalently its characteristic polynomial). Block Gaussian elimination reduces both determinants in (D) to the norm of `u+t` times the corresponding determinant of the Schur complement of size `r−1`. The induction hypothesis and multiplicativity of the norm prove (D) after inverting *q*. The injection `A[t]→A[t,1/q]` gives the identity already over `A[t]`; specializing `t=0` proves (D) for *U* over *A*.

For projective *B,C*, localize *A* at any prime. Then *B* is free over local *A*; being finite over a local ring, *B* is semilocal, and a projective *B*-module of constant rank *r* is free. Apply (D) to the *B*-linear multiplication matrix of any `c∈C`. These local equalities glue to (T). The same proof applies after every base change, so (T) is an identity of polynomial laws, not merely of values on geometric points.

The equality of canonical sections under the usual flattening map follows: composing the two laws corresponds to composing the two symmetric-power sections and flattening an *s*-tuple of *r*-tuples to an *rs*-tuple. Equality of polynomial laws determines equality of the representing algebra maps. One can see this without evaluating only on ordinary *A*-points: take a universal element `Σt_i e_i` over a polynomial ring; its tensor-power coefficients are the orbit sums that form a basis. Agreement after all base changes determines the entire algebra map. This is necessary over nonreduced bases, where agreement on geometric fibres alone would not suffice.

**Exact published comparator.** Deligne (1973), XVII: Lemma 6.3.3 (transitivity by commuting blocks), 6.3.4.2 (section), 6.3.5 (additivity), 6.3.7.1 (base change), and 6.3.15(v) (trace composition).

## 6. MPL98-NORM05L/05R and NORM06: the categorical assertion

### 6.1 Axioms are additional data

A category with finite coproducts need not have the required fibre products, symmetric quotients, compatible quotient base changes, or distributivity identities. The modernization **assumes** existence and stability of the relevant products and quotients, **assigns** degrees, and **assigns** sections satisfying compatibility diagrams. This is a definition of an enhanced structure. The scheme and G-set examples provide models; the definition alone does not prove every finite-coproduct category possesses a model. The diagram for transitivity additionally uses canonical quotient comparison and flattening maps, whose existence and compatibility must be justified in a proposed category.

### 6.2 Literal global-degree problem and repair

The displayed modernization writes a single function `deg:𝒩→N`, requires `deg(id_X)=1`, closure under sums, and arbitrary base-change invariance. In schemes and G-sets, pullback along the empty target is strict. If `u:X→Y` has degree *r*, its pullback along `∅→Y` is `id_∅`, forcing `r=1`. On any nonempty *Y*, the coproduct of two identity arrows has degree 2 by additivity and degree 1 by that pullback, a contradiction.

The refinement **MPL98-NORM05R** is to use either (a) a predicate `hasDeg(u,r)` expressing that every fibre has cardinality/rank *r*, or (b) a locally constant rank function on the target. Over the empty target the predicate is true for every *r*, whereas a rank function is the unique empty function; neither creates contradictory numerical equalities. The numerical product formula is retained on constant-rank pieces; genuinely variable ranks require the appropriate fibrewise rank sum for composition. One can also work with degree-indexed arrows or expressly restrict the targets and base changes. This is a defect of the literal single-function formulation in these examples, not a refutation of the useful norm construction.

Hua's Lean footnote uses the predicate name `hasDeg`. Its reported proof may already avoid the ambiguity. **No Lean file was supplied or inspected here**, and no claim about successful formal verification is made.

### 6.3 Independent G-set verification

For an equivariant map `u:X→Y` whose fibres all have *r* elements, let `Can(y)` be the multiset consisting of every element of `u^{-1}(y)` once. This is invariant under ordering and equivariant under the group action. Pullback replaces a fibre by a canonically bijective copy, so it preserves the multiset. Disjoint sum concatenates the two fibre multisets. For a composite `X→Y→Z`, the fibre over *z* is the disjoint union of the fibres over the elements of `Y_z`; flattening those multisets lists each element of `X_z` exactly once. Identity normalization is immediate. Finally the fibre of `(X_Y^n)/H→Y` is the orbit set of *n*-tuples in `X_y`; any bijection `X_y≅E` gives cardinality `#(E^n/H)`.

These arguments prove the refined degree and section axioms directly. They overlap the proof reported by Hua's modernization and must not be presented as a newly discovered theorem or as a re-run of his Lean proof.

For a principal covering-space torsor `P→S` under a discrete group `G`, the associated space `P×^G E` is locally `U×E` on a trivializing cover. Every finite-fibre operation above is then performed fibrewise and glues, giving the covering-space example. This statement uses an actual locally trivial principal covering. General “free and proper” language depends on the topological conventions; no claim is made here for arbitrary pathological spaces or for every analytic category. Hua explicitly labels parts of his topological interpretation and quotient argument as added explanation.

## 7. MPL98-NORM07: the Hilbert–Chow connection and nonflat ambient spaces

**Context credit.** Hua's “Les stations,” lines 216–222, expressly presents the Hilbert–Chow connection as his reading's proposed link, not as an explicit link found on the pages. It is mathematically justified under representability hypotheses.

For separated algebraic spaces `X/S`, Rydh (2008b), Definition 4.3.1, constructs

\[
\operatorname{Hilb}^r(X/S)\longrightarrow
\operatorname{Sym}^r(X/S)\longrightarrow\Gamma^r(X/S).
\]

For a family `Z↪X_T` finite locally free of rank *r* over *T*, its norm section lands in `Sym_T^r(Z)`. The composite `Z→X` induces a morphism from that symmetric power to `Sym_S^r(X)`, and gives the required *T*-point. Here it is **Z/T**, rather than the ambient **X/S**, that is flat. Thus failure of ambient flatness does not invalidate the first arrow.

Rydh (2008b), Proposition 4.1.1, identifies `Sym→Γ` as a universal homeomorphism with trivial residue-field extensions, an isomorphism when `X/S` is flat or *S* is a scheme over `Q`. His Corollary 4.1.2 and examples following it describe the base-change issue. Divided powers commute with arbitrary base change, whereas symmetric powers need not. Rydh (2008a), §6, calls the Hilbert-to-divided-power morphism the Grothendieck–Deligne norm map and relates it to the determinant construction.

Accordingly, retain Hua's proposed Hilbert–Chow link, credit it, specify a separated representable setting (algebraic spaces suffice), and distinguish existence of the map to `Sym` from replacing `Sym` by `Γ` in arbitrary base-change statements. This does not establish an archival dating or priority assertion.

## 8. MPL98-NORM08: symmetric operations and trace hypotheses

For finite locally free `T→S` of rank *r*, a symmetric morphism `φ:G^r_S→G'`, and `α:T→G`, the composite `φ∘α^r:T^r_S→G'` factors through `Sym_S^r(T)` whenever the latter is the categorical quotient for the chosen targets. Compose that factorization with `Can_{T/S}`. This constructs the operation without requiring `Sym_S^r(G)` to exist. Multiplication recovers the norm of functions; addition recovers trace. The resulting operations inherit base change, sums and transitivity when their defining operations and quotient maps satisfy the corresponding diagrams.

For arbitrary sheaf-valued targets, quotient descent is a real hypothesis. Deligne (1973), XVII 6.3.13.1, explicitly imposes it on a big-fppf abelian sheaf; 6.3.14 gives representable sheaves, pullbacks of étale sheaves, and quasi-coherent modules as cases. Proposition 6.3.15 proves the trace compatibilities, and 6.3.18 identifies `G_a` and `G_m` with ordinary trace and norm. Thus the contextual slogan “every norm and trace” is useful motivation within the stated construction, not a theorem about arbitrary operations or all sheaves without hypotheses.

## 9. MPL98-NORM09: SGA 6 is not the missing published proof

The **original publisher front matter** of SGA 6, preface dated June 1971, says that Ferrand's planned exposé XI on determinants of perfect complexes had not been written and would not be published. The table of contents likewise labels XI “Non rédigé.” This matters because SGA 4's prospective references to “SGA 6 XI” can otherwise look like an available proof. The current run checked the preface itself, not only a later bibliography. SGA 6 X's determinant discussion is separate; no theorem of that section is used to justify the norm-section theorem here. The exact available comparator is SGA 4 XVII §6.3, supplemented by Ferrand's published polynomial-law treatment.

## 10. Context search and limits of the check

Actual context search in this run:

```text
rg -n '98-axiomatic|determin|détermin|norme|symétrique|stations|finite sums|sommes finies|divisées|transitiv|quotient' context/README.md context/hua_project/README.md context/notes/RESULTS_STATE.md context/hua_project/98.modern.tex
```

Relevant matches were `RESULTS_STATE.md` lines 18, 20 and 460; the modernization's station link 216–222, determinant discussion 275–314, norm operation 331–383, transitivity 385–441, axioms 443–506, and examples 508–591. Read the two READMEs and the supplied RESULTS_STATE context; its status labels were treated as claims or leads, not independently verified research. Its open arithmetic/group-theoretic entries do not become resolved by these elementary norm constructions. This memorandum provides no new result on the named open items `LM7 E.23`, `FLAGGED_149 B9`, `LM1 D.11`, `LM4 D.12`, or `LM4 F.7`.

Scope limits: no manuscript text was adjudicated by this agent; no image was opened; no Lean source or certificate was checked; no broad novelty search or archival chronology was established; no complete analytic-category construction was verified. Roby's metadata was checked, but his full paper was not independently read in this run. Ferrand's paper was checked at the sections below; a text search did not locate a passage explicitly headed by transitivity, so it is not represented as the inspected direct proof of that point. The present independent determinant proof supplies the algebraic check.

## 11. Primary references, exact locations and retrieval evidence

1. **Deligne, P. (1973).** Cohomologie à supports propres (Exposé XVII). In M. Artin, A. Grothendieck, & J.-L. Verdier (Dirs.), *Théorie des topos et cohomologie étale des schémas. Tome 3* (Lecture Notes in Mathematics, Vol. 305, pp. 250–480). Springer. https://doi.org/10.1007/BFb0070723
   - Publisher chapter metadata independently checked: https://link.springer.com/chapter/10.1007/BFb0070723 . The encompassing volume DOI is https://doi.org/10.1007/BFb0070714 . Publisher chapter pagination includes the appendix; the IAS author bibliography gives pp. 250–461 for Deligne's part.
   - Author's IAS bibliography: https://publications.ias.edu/deligne/paper/350
   - Original author-hosted PDF linked there: https://publications.ias.edu/sites/default/files/Number4.pdf (retrieval exceeded tool size limit; not the text witness used).
   - Text actually checked, mathematical retypesetting: https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf
   - Exact locations: XVII 6.3.1; Lemma 6.3.3; 6.3.4.2; 6.3.5; 6.3.7.1; 6.3.13–6.3.15; 6.3.18. Original printed pagination approximately 431–449; section numbering governs because retypeset pagination differs. The retypeset front title is not a reliable volume label; the exposé text and numbering are the comparison witness.

2. **Ferrand, D. (1998).** Un foncteur norme. *Bulletin de la Société Mathématique de France, 126*(1), 1–49. https://doi.org/10.24033/bsmf.2319
   - Official record: https://www.numdam.org/articles/10.24033/bsmf.2319/
   - Full paper: https://www.numdam.org/article/BSMF_1998__126_1_1_0.pdf
   - Checked §§2.2.4 (universal polynomial law), 2.5.1 (multiplicative laws), 3.1.1–3.1.2 (determinant norm and representing map), approximately pp. 9, 14, 16–17. No factorial inversion is used for this construction.

3. **Rydh, D. (2008a, April 11).** *Families of zero cycles and divided powers: II. The universal family* [Preprint]. https://davidrydh.se/papers/famzerocyclesII-20080411.pdf
   - Checked introduction and §6, “The Grothendieck–Deligne norm map”; the finite-flat family is also described in §3.

4. **Rydh, D. (2008b).** *Hilbert and Chow schemes of points, symmetric products and divided powers* [Thesis paper III, KTH]. https://people.kth.se/~dary/thesis/thesis-paperIII.pdf
   - Checked Proposition 4.1.1, Corollary 4.1.2, examples after them, and Definition 4.3.1 (printed pp. 27–31; PDF pp. 26–30). Author's paper listing: https://davidrydh.se/papers .

5. **The Stacks Project Authors. (n.d.).** *Finite locally free morphisms* (Tag 02K9). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/02K9
   - Definition 29.49.1 and Lemmas 29.49.2–29.49.5 in the retrieved numbering. Stable tag preferred over changing chapter numbering.

6. **The Stacks Project Authors. (n.d.).** *Lemma 31.18.6* (Tag 0BD2). Retrieved November 18, 2026, from https://stacks.math.columbia.edu/tag/0BD2
   - Determinant norm for finite locally free morphisms and arbitrary base change.

7. **Berthelot, P., Grothendieck, A., & Illusie, L. (Dirs.). (1971).** *Théorie des intersections et théorème de Riemann–Roch: Séminaire de Géométrie Algébrique du Bois Marie 1966/67 (SGA 6)* (Lecture Notes in Mathematics, Vol. 225). Springer. https://doi.org/10.1007/BFb0066283
   - Original front matter actually checked: https://link.springer.com/content/pdf/bfm:978-3-540-36936-3/1 (PDF p. 4 preface; p. 9 table of contents).
   - Publisher metadata/contents: https://link.springer.com/book/10.1007/BFb0066283 . The retypeset preface at https://geotoppos.org/divers/SGA6.pdf agrees, but the publisher's original is the preferred evidence.

8. **Roby, N. (1963).** Lois polynomes et lois formelles en théorie des modules. *Annales scientifiques de l'École normale supérieure, 3e série, 80*(3), 213–348. https://doi.org/10.24033/asens.1124
   - Official record checked: https://www.numdam.org/articles/10.24033/asens.1124/ . This is a bibliographic lead supporting the lineage named by Hua and the later sources; the present run does not claim to have inspected its full proof.

**Source-status note.** The current Stacks pages and primary-author research papers supply present authoritative formulations, while SGA 4 and Ferrand supply the classical proofs. No secondary exposition is used as the authority for a technical assertion. Academic-hosted retypesetting of SGA 4 is explicitly identified as the text witness used. A source comparison establishes mathematical correspondence, not that an undated manuscript precedes or directly caused a publication.
