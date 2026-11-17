# Finite complete modules over a complex analytic local algebra

Research-only supplement, written after the transcription was frozen. This is our reconstruction of a standard algebraic step needed by the Picard comparison proof, **not a claim of novelty**, not a statement that the manuscript contains this proof, and not an independent verification of all other analytic comparison inputs.

## Conclusion and hypotheses

**Lemma.** Let

\[
(A,\mathfrak m)=\bigl(\mathbb C\{z_1,\ldots,z_N\}/I,\mathfrak m\bigr)
\]

be a complex analytic local algebra, where `I` is a proper ideal, and let `M` be a finitely generated `A`-module. Write

\[
\widehat M=\varprojlim_n M/\mathfrak m^{n+1}M.
\]

Then the following conditions are equivalent:

1. The natural map `M→M̂` is surjective.
2. The natural map `M→M̂` is an isomorphism.
3. `M` has finite length over `A`.

No reducedness, normality, irreducibility, or regularity assumption on **A** is needed. In particular, nilpotents in the local analytic algebra do not invalidate the argument. Finite generation, the convergent complex analytic origin of **A**, and completion at its maximal ideal are essential to the statement being proved.

## Primary references checked

The following are author/official sources actually opened during this follow-up; no secondary exposition is used as an authority.

| Key | Source and exact location | Input used |
|---|---|---|
| D | Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, version21June2012, [author PDF](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf), ChapterII §2, Theorem2.7, p81; Theorem2.10, pp82–83; §4, Local parametrization theorem4.19, p95 (PDF page95, zero-based94), with construction preceding it on pp93–94 | `O_d=C{t_1,…,t_d}` is Noetherian and factorial; a domain `O_N/J`, `J` prime, admits a finite integral inclusion `O_d→O_N/J` after choosing coordinates. |
| C | The Stacks Project, [Lemma10.97.1, Tag00MA](https://stacks.math.columbia.edu/tag/00MA), especially(2) | Maximal-ideal completion preserves short exact sequences of finite modules over a Noetherian ring. |
| K | The Stacks Project, [Lemma10.51.4, Tag00IP](https://stacks.math.columbia.edu/tag/00IP) | Krull intersection: finite modules over a Noetherian local ring are separated for the maximal-ideal topology. |
| P | The Stacks Project, [Lemma10.62.1, Tag00L0](https://stacks.math.columbia.edu/tag/00L0) | A finite module over a Noetherian ring has a finite filtration with factors `A/p_i`, `p_i` prime. |
| T | The Stacks Project, [Lemma10.161.8, Tag032L, proof](https://stacks.math.columbia.edu/tag/032L) | For a normal domain **B** and a finite separable field extension of its fraction field, the field trace of an element integral over **B** lies in **B**. |

Demailly's older `ujf-grenoble.fr` URL timed out; the current author URL above opened successfully. The successful PDF is explicitly dated21June2012 on its title page. The theorem text was checked by PDF text retrieval and focused searches; no manuscript OCR or source-page transcription was involved.

**Final reference alignment:** the primary reader independently checked the matching [university-hosted copy](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf) after the author URL intermittently timed out. The final notes cite ChapterII, Proposition4.8 and the finite-extension construction4.12–4.13, pp92–94, which supply the algebraic input preceding Theorem4.19, together with Theorems2.7 and2.10, pp81–83. This is the same analytic finite-normalization input used below; the p95 theorem citation records the additional direct check made during this agent's research.

## Proof

### 1. Finite length suffices; surjectivity is already bijectivity

The ring **A** is Noetherian by D. Krull intersection K gives

\[
\ker(M\longrightarrow\widehat M)=\bigcap_{n\geq0}\mathfrak m^{n+1}M=0.
\]

Thus(1) and(2) are equivalent. If **M** has finite length, some power of `m` kills it: in a composition series, multiplication by `m` kills each simple factor, and iterating through the series kills **M**. Its quotients by powers of `m` are therefore eventually **M** itself, proving(3)⇒(2).

### 2. Completeness passes to finite submodules and quotients

Suppose **M** is complete and

\[
0\longrightarrow N\longrightarrow M\longrightarrow Q\longrightarrow0
\]

is exact with finite modules. Completion gives an exact bottom row by C; all natural vertical maps to completions are injective by K. For `q̂∈Q̂`, lift it to `m̂∈M̂`, then use completeness of **M** to obtain `m∈M`; its image in **Q** maps to `q̂`, so **Q** is complete. For `n̂∈N̂`, its image in `M̂=M` is an element `m` whose class in **Q** maps to zero in `Q̂`; separatedness of **Q** forces that class to vanish, so `m∈N`, proving **N** complete.

Apply P to **M**. Each submodule and successive quotient in a prime filtration is complete by the preceding argument. If every prime factor were `A/m`, the filtration would be a finite composition series, and **M** would have finite length. Consequently, if **M** does not have finite length, there is a prime factor

\[
R=A/\mathfrak p,\qquad \mathfrak p\ne\mathfrak m,
\]

which is a complete complex analytic local domain and is not a field. This is where arbitrary nilpotents in **A** disappear legitimately: no reducedness assumption is inserted into the original statement.

### 3. Analytic normalization and normalized trace force a convergent power-series ring to be complete

Write `R=C{z_1,…,z_N}/J` with **J** prime. By D, choose a finite integral inclusion

\[
B=\mathbb C\{t_1,\ldots,t_d\}\hookrightarrow R.
\]

Here `d>0`: if `d=0`, **R** is a finite domain over the algebraically closed field **C**, hence **R=C**, contradicting the choice that **R** is not a field. Let `n` be the maximal ideal of **B**, and `r` that of **R**. Since **R** is a finite local **B**-algebra with both residue fields **C**, `R/nR` is a finite-dimensional local **C**-algebra, so its maximal ideal is nilpotent; thus `r^c⊂nR` for some **c**, and

\[
\mathfrak r^{cn}\subseteq\mathfrak n^nR\subseteq\mathfrak r^n
\qquad(n\geq1).
\]

The two filtrations are cofinal, so completeness of **R** for `r` implies completeness of **R** as a **B**-module for `n`.

Set `K=Frac(B)`, `L=Frac(R)`, and `q=[L:K]`. The extension is finite and separable because the characteristic is zero, and **B** is normal since it is factorial by D. Every element of **R** is integral over **B**, so T gives `Tr_{L/K}(R)⊂B`. Therefore

\[
\rho:R\longrightarrow B,\qquad r\longmapsto\frac1q\operatorname{Tr}_{L/K}(r)
\]

is a **B**-linear retraction of the inclusion `B→R`: for `b∈B`, the trace is `qb`. It follows that `R=B⊕ker ρ` as finite **B**-modules. Completion commutes with this finite direct sum, and its natural map is block diagonal; hence completeness of **R** implies completeness of **B**.

### 4. Positive-dimensional convergent power series are not complete

The polynomials

\[
s_N(t_1)=\sum_{j=0}^{N}j!t_1^j
\]

define compatible elements of `B/n^{N+1}` and therefore an element of the completion of **B**. If it came from an element of **B**, restricting that convergent germ to the `t_1` axis would give a convergent one-variable series with coefficients **j!**. Its radius of convergence is zero, since `((j+1)!r^{j+1})/(j!r^j)=(j+1)r→∞` for every **r>0**, a contradiction.

Thus **B** is not complete for `d>0`. This contradicts Step3, excludes the prime factor in Step2, and proves(2)⇒(3). ∎

## Exact relation to the manuscript

For P57 scans254–258, suppose the exact exponential-comparison rows, the identification of the integral-cohomology terms, and injectivity of coherent completion are granted. With `M=(R^if_*O_X)_y`, the diagram chase gives

\[
\ker(w^i)=0,\qquad \operatorname{coker}(w^i)\cong\widehat M/M.
\]

The lemma above then proves that `w^i` is an isomorphism exactly when **M** has finite length. In the Picard case `i=1`, this supplies the analytic-module step behind the necessity asserted in227(iii) and258(iii), as a **modern proof supplied in the research notes**. The sufficiency direction is already explicitly attempted in Corollary1.6 on256.

This conclusion remains distinct from the manuscript's finite-image claim. In particular, it does **not** justify the lower bubble on256 asserting surjectivity `M→H^i(X_n,O_Xn)` at every finite **n**. Nor does it prove the unwritten proper GAGA bridge in228/266, the topological finite-generation reference marked “cf ?” on254, or every regularity/divisor-lattice comparison in268–270.

The analytic hypothesis is essential to the lemma: for `A=C[[t]]`, the finite module **M=A** is complete but has infinite length. Likewise, for the constant elliptic curve over this complete formal base, proper formal existence can give Picard comparison without finite-length `H^1`; this is consistent with Grothendieck's restriction of the formal analogue on228 to(i),(i bis).

## Suggested short final-note wording

**File/scan:** P57,227(iii),256(D)/Corollary1.6,258(iii). **Kind:** own idea (standard proof supplied here). **Quote:** “it is nec and suff”. **Confidence:** high, with the exact algebraic inputs checked in DemaillyII.4.19 and Stacks Tags00MA,00IP,00L0,032L. **Bears on:** Hua **57-analytic-pic-completion-criterion**. **Context search:** `longueur finie|finite length|artinien|Krull|completion-criterion`.

The comparison diagram reduces surjectivity to completeness of the finite analytic module `M=(R^1f_*O_X)_y`. A prime filtration, analytic Noether normalization, and normalized trace show that a positive-dimensional complete prime factor would force `C{t_1,…,t_d}` to be complete, contradicted by a divergent formal series; hence **M** is complete iff it has finite length. This supplies the converse algebraic step left implicit in Hua's **“§1. Le théorème analytique”** and the manuscript's theorem, without changing the frozen transcription or treating the separate finite-level-surjectivity line as verified.

## Search/verification record

- Web search for author-level analytic Noether normalization led to Demailly's author PDF; exact theorem4.19 and factorial theorem2.10 were checked in that source.
- Official Stacks pages for00MA,00IP,00L0,032L were opened and their statements/proofs checked; the normalized-trace argument uses the integral-trace assertion in the **proof** of032L, not that lemma's finiteness-of-normalization conclusion.
- The proof was checked for arbitrary proper ideals **I**, for **M=0**, for zero-dimensional nonreduced algebras, for the distinction between the two maximal-ideal topologies, and for the finite direct-summand argument. None requires **A** to be reduced or normal.
- No novelty claim or general literature-status claim has been made.
