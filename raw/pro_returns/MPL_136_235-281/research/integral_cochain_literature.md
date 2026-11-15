# Integral cochain models: verified literature and limits of comparison

Research memorandum, 15 November 2026. Prepared after the transcription freeze. No manuscript images were consulted for this memorandum; references to its cancelled draft are conditional on the principal reader’s report. External sources establish mathematical comparisons, not the identity, date, or intended final theorem of these manuscript leaves.

## 1. The distinctions needed for S11(i)

The planning question S11(i) in the supplied `context/README.md` asks whether the complex is a functorial integral cochain algebra computing cohomology with products. Three claims require separate evidence:

1. A complex computes the integral cohomology **groups**.
2. Its multiplication corresponds directly to the ordinary cup product.
3. Its enhanced algebraic structure determines a homotopy type, or the mapping spaces between such types.

None of these assertions automatically supplies the next. A further distinction is essential: a bigraded collection with products between different weights need not give a cup-product-preserving algebra after selecting one weight. The literature below should therefore guide an audit of the actual constructions and comparison maps, rather than replace that audit.

## 2. Source-specific results

### Cartan (1976), §§2, 6–7, especially pp. 268–271

Cartan’s §7 explicitly attributes its example to Grothendieck’s IHÉS lecture of 12 December 1975, while qualifying the account as his understanding. For every simplicial set $X$, the weight decomposition gives

\[
H^n(Gr^{*,r}(X))=0\quad(r<n),\qquad
H^n(Gr^{*,r}(X))\cong H^n(X;\mathbb Z)\quad(r\ge n).
\]

Under these identifications, multiplication of weights $r,s$, for $r\ge p,s\ge q$, induces

\[
\mu_{r,s}(a,b)=\binom{r+s}{r}(a\smile b).
\]

All weights recover cup products by the stated gcd argument. Each $Gr^n$ has $\pi_n\cong\mathbb Z$, other homotopy groups zero: §6 uses weakened axiom (b′), not §2’s contractibility axiom (b). This is a weighted integral comparison, not an unweighted integral PD algebra with ordinary cup product.

Primary sources: [publisher record](https://link.springer.com/article/10.1007/BF01390140); [GDZ article scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0035/LOG_0030.pdf). Printed and publisher pagination: 261–271; catalogue pagination: 261–272.

### Miller (1978) and Garvín et al. (1998), §§3–4

Miller’s author, title, journal, pages, and DOI were verified against publisher-deposited Crossref metadata; his full article was not obtained. Consequently, no exact endpoint theorem is attributed here directly to Miller.

Garvín et al. extend the fixed-length construction to arbitrary simplicial sets over a commutative unital ring $R$. A length-$q$ complex $A^{*,q}$ is a differential graded **module**; multiplication changes length. Proposition 3.1 gives the simplex Poincaré lemma. Proposition 3.2 proves extendability in form degrees $p<q$; Remark 3.3 gives a volume-form obstruction at $p=q$. Theorem 4.2 explicitly states

\[
q!\!\int:A^{*,q}(K)\longrightarrow C^*(K;R),\qquad
H^p(q!\!\int)\text{ is an isomorphism for }p<q.
\]

The prose phrase “up to degree $q$” in their introduction/Theorem 4.3 must not silently replace this strict inequality. Cartan’s stronger endpoint statement is separately recorded above.

Primary sources: [Miller DOI](https://doi.org/10.1016/S0040-9383(78)90025-3); [Garvín et al. article](https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf).

### Dwyer (1979); precise formulation checked in Scheerer and Tanré (1991), pp. 376–377

Dwyer’s original publisher record verifies the bibliographic identification; its full text was not obtained. The primary follow-up by Scheerer and Tanré specifies $r\ge3$ and increasing subrings $R_j\subset\mathbb Q$, each containing $1/k$ when $2k-3\le j$. Tame weak equivalences of $r$-reduced simplicial sets induce isomorphisms on

\[
\pi_{r+j}(-)\otimes R_j;
\]

the corresponding Lie-algebra equivalences are detected by $H_{r-1+j}(-)\otimes R_j$. Simplicial Lazard algebras mediate the equivalence of homotopy categories. This retains degree-dependent localized information, not unrestricted integral homotopy. In particular, the least permitted system already inverts 2 at $j=1$. It supplies no general rectification of integral cochains to a strict PD DGA.

Primary sources: [Dwyer publisher page](https://www.sciencedirect.com/science/article/pii/0040938379900235); [Scheerer–Tanré article](https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf).

### Mandell (2001), Main Theorem and Appendix A, Theorems A.1–A.2

For connected, $p$-complete, nilpotent spaces of finite $p$-type, cochains over $\overline{\mathbb F}_p$ give a contravariant equivalence with a full subcategory of the homotopy category of $E_\infty$ algebras. This includes $p=2$. The algebraic closure cannot casually be replaced by $\mathbb F_p$: over a finite field $\mathbb F_q$, Theorem A.2 identifies algebra maps with homotopy classes of maps into the **free loop space** of the target. The additional operations and homotopy coherence are essential features of this theorem; it does not assert a strictly commutative integral de Rham model.

Primary source: [author’s archived submitted version](https://mmandell.pages.iu.edu/papers/einffinal.pdf). The [author’s publication list](https://mmandell.pages.iu.edu/papers/) warns about journal copyediting and provides this archival version.

### Mandell (2006), Main Theorem and Theorems 0.1–0.2

Finite-type nilpotent spaces are weakly equivalent exactly when their integral singular cochains are quasi-isomorphic as $E_\infty$ algebras. The cochain functor is faithful but not full. Theorem 0.1 gives a natural retraction on homotopy classes of maps; its extra compatibility with cohomology assumes the source also has finite type. Theorem 0.2 computes the derived realization as

\[
\mathbb U C^*(Y)\simeq
Y\mathop{\times}^{h}_{\widehat Y}L\widehat Y,
\]

where $\widehat Y$ is finite completion. Consequently, distinguishing spaces is weaker than a fully faithful algebraic model. Neither result discards the $E_\infty$ structure in favor of a strict PD differential graded algebra.

Primary sources: [journal archive record](https://www.numdam.org/item/?id=PMIHES_2006__103__213_0); [article text](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mandell-cochains.pdf).

### Ekedahl (2002), Theorems 2.9 and 3.2

For connected nilpotent simplicial sets with finitely generated homology in every degree, Theorem 2.9 constructs a special minimal numerical model and gives its uniqueness up to numerical homotopy in the stated sense. Its degreewise objects are finite-rank free abelian groups, but face and degeneracy maps are **integer-valued rational polynomial maps**, not necessarily homomorphisms. Thus these are not ordinary simplicial abelian groups. Numerical cochains compute cohomology. For special models, Theorem 3.2 controls extension to coefficient rings; $R\subset\mathbb Q$ gives localization and $R=\mathbb Z_p$ gives completion. The model uses numerical/cosimplicial structure, not an unrestricted PD structure on positive-degree cochains.

Primary source: [author’s preprint](https://arxiv.org/pdf/math/0107004), v2, 20 August 2001; [published DOI](https://doi.org/10.4310/HHA.2002.v4.n2.a9).

### Toën (2020), Theorem 0.1; §1; Definition 2.1

For **simply connected finite-type** $X$, the affine homotopy type

\[
(X\otimes\mathbb Z)^{\mathrm{uni}}
=\operatorname{RSpec}(C^*(X;\mathbb Z))
\]

uses a cosimplicial commutative ring and derived mapping spaces. Its homotopy sheaves are $\pi_i(X)\otimes\mathbb H$, where $\mathbb H=\operatorname{Spec}(\operatorname{Int}(\mathbb Z))$ is the Hilbert additive group. Theorem 0.1 gives a functorial retraction on integral points, faithfulness, and injectivity on equivalence classes; it does not state full faithfulness. Rational points recover rationalization; algebraically closed characteristic-$p$ points recover $p$-completion. The introduction explicitly leaves a proposed general filtration for future work. These conclusions do not prove the manuscript’s filtration or strict PD assertions.

Primary source: [published article](https://epiga.episciences.org/6822/pdf), with [journal record](https://epiga.episciences.org/6822).

### Horel (2024), Theorems 5.4, 6.1, 7.3; Remark 8.5

Cosimplicial **binomial rings**, localized at quasi-isomorphisms, model connected finite-type nilpotent spaces fully faithfully: the derived unit $X\to\mathbf R\operatorname{Map}(\mathbb Z^X,\mathbb Z)$ is an equivalence. For connected finite-type spaces generally it is Bousfield–Kan $\mathbb Z$-completion. Evaluation at $\mathbb Z_p$ gives $\mathbb F_p$-completion, with no exclusion of $p=2$. Binomial operations $\binom{x}{n}$ in degreewise torsion-free rings are not the PD operations $x^n/n!$ on positive-degree cocycles. Remark 8.5 distinguishes binomial realization from Toën’s affinization. The current arXiv v2 is dated 23 March 2025; the stated main theorems were also checked in v1, dated 4 November 2022. The journal publication is 2024.

Primary sources: [2024 publisher record](https://www.degruyterbrill.com/document/doi/10.1515/crelle-2024-0039/html); [v1](https://arxiv.org/pdf/2211.02349v1); [current version](https://arxiv.org/abs/2211.02349).

## 3. Two independent mathematical audits

The following are elementary deductions made for this research note, not theorems attributed to the preceding papers.

### 3.1. Conditional obstruction from $\mathbb{CP}^2$

Suppose a differential graded algebra $A$ has a graded-ring isomorphism

\[
H^*(A)\cong H^*(\mathbb{CP}^2;\mathbb Z)
=\mathbb Z[u]/(u^3),\qquad |u|=2.
\]

The cohomology-ring computation is Hatcher (2002, Theorem 3.19, p. 220), with theorem numbering taken from the [linked 2015-reprint text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). Assume a PD ideal contains every positive even cochain and satisfies, for a degree-two element $a$,

\[
a^2=2\gamma_2(a),\qquad d\gamma_2(a)=a\,da.
\]

Choose a cocycle representing $u$. Then $\gamma_2(a)$ is a cocycle and

\[
u^2=2[\gamma_2(a)]\in H^4(A).
\]

This contradicts the primitivity of $u^2$ in $H^4(\mathbb{CP}^2;\mathbb Z)\cong\mathbb Z$. Functoriality, extendability, and a homotopy-type classification theorem are unnecessary for this contradiction. Nor must one prove divided powers descend to every cohomology class: the displayed identity for one closed representative suffices.

According to the principal reader, the cancelled draft on scan 247 places $A^+$ in the PD ideal and writes the relevant differential compatibility. This makes the calculation a conditional audit of that **cancelled draft**. It is not evidence that all live constructions on the later leaves assert the contradicted statement. A restricted PD ideal, weight-dependent comparison, or changed coefficients changes the hypotheses. Assuming also $d\gamma_p(a)=\gamma_{p-1}(a)\,da$, the same argument over $\mathbb Z_{(p)}$ uses $H^2(\mathbb{CP}^{p})$ and $a^p=p!\gamma_p(a)$, giving an obstruction at any prime.

### 3.2. PD-filtration completion versus $p$-adic completion

Take the canonical divided powers on $I=(p)\subset\mathbb Z_p$, and let $F^r_{\mathrm{PD}}$ be the usual ideal generated by products of divided powers of total index at least $r$. Since

\[
\gamma_n(p)=\frac{p^n}{n!},\qquad
v_p\!\left(\frac{p^n}{n!}\right)
=n-\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor
=\frac{(p-2)n+s_p(n)}{p-1},
\]

where $s_p(n)$ is the sum of the base-$p$ digits of $n$, for $p>2$ one has

\[
p^r\mathbb Z_p\subseteq F^r_{\mathrm{PD}}
\subseteq p^{\lceil (p-2)r/(p-1)\rceil}\mathbb Z_p.
\]

These filtrations are cofinal. The estimate applies to products because their valuations add and their total indices are at least $r$.

For $p=2$, however, $v_2(2^n/n!)=s_2(n)\ge1$, with equality for the unbounded sequence $n=2^a$. Every $F^r_{\mathrm{PD}}$, $r\ge1$, therefore contains an element of valuation one and is contained in $2\mathbb Z_2$. Consequently,

\[
F^r_{\mathrm{PD}}\mathbb Z_2=2\mathbb Z_2\quad(r\ge1),
\qquad
\operatorname{gr}^0_{\mathrm{PD}}=\mathbb F_2,
\qquad
\operatorname{gr}^{r}_{\mathrm{PD}}=0\quad(r>0),
\]

and

\[
\varprojlim_r\mathbb Z_2/F^r_{\mathrm{PD}}=\mathbb F_2,
\]

whereas ordinary $2$-adic completion is $\mathbb Z_2$. A modern theorem involving $p$-completion of spaces does not identify these two algebraic completions. A proof using the filtration must state separatedness, completeness, and the exact comparison of filtrations it needs.

## 4. How to use the nonflasque $K(k,n)$ warning

If the manuscript’s $t=0$ specialization has degree-$n$ coefficient object (K(k,n)), for $k\ne0$, then that object is not contractible. Its nonzero $\pi_n$ obstructs extending a representative over a bounding simplex; consequently the usual degreewise extendability argument cannot be invoked unchanged. This does not itself prove that every global cohomology comparison fails. A weakened representability theorem, altered coefficient object, weight decomposition, or derived replacement requires its own proof. In particular, checking a simplex Poincaré lemma alone does not verify the global restriction/extension hypothesis.

This is the correct level at which to connect the arithmetic and modern homotopy literature with S11: identify the precise coefficient algebra, grading, multiplication, domain of divided powers, and completion before concluding that the ordinary integral cup-product algebra has been recovered. No cited modern theorem identifies these manuscript leaves or repairs an unspecified missing argument.

## 5. APA bibliography

Cartan, H. (1976). Théories cohomologiques. *Inventiones mathematicae, 35*, 261–271. https://doi.org/10.1007/BF01390140

Dwyer, W. G. (1979). Tame homotopy theory. *Topology, 18*(4), 321–338. https://doi.org/10.1016/0040-9383(79)90023-5

Ekedahl, T. (2002). On minimal models in integral homotopy theory. *Homology, Homotopy and Applications, 4*(2), 191–218. https://doi.org/10.4310/HHA.2002.v4.n2.a9

Garvín, A., Lechuga, L., Murillo, A., Muñoz, V., & Viruel, A. (1998). An extension of Miller’s version of the de Rham theorem with any coefficients. *Banach Center Publications, 45*(1), 169–176. https://doi.org/10.4064/-45-1-169-176

Hatcher, A. (2002). *Algebraic topology* (2015 reprint consulted). Cambridge University Press. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf

Horel, G. (2024). Binomial rings and homotopy theory. *Journal für die reine und angewandte Mathematik, 813*, 283–305. https://doi.org/10.1515/crelle-2024-0039

Mandell, M. A. (2001). $E_\infty$ algebras and $p$-adic homotopy theory. *Topology, 40*(1), 43–94. https://doi.org/10.1016/S0040-9383(99)00053-1

Mandell, M. A. (2006). Cochains and homotopy type. *Publications Mathématiques de l’IHÉS, 103*, 213–246. https://doi.org/10.1007/s10240-006-0037-6

Miller, E. Y. (1978). Derham cohomology with arbitrary coefficients. *Topology, 17*(2), 193–203. https://doi.org/10.1016/S0040-9383(78)90025-3

Scheerer, H., & Tanré, D. (1991). Exploring W. G. Dwyer’s tame homotopy theory. *Publicacions Matemàtiques, 35*, 375–402. https://doi.org/10.5565/publmat_35291_05

Toën, B. (2020). Le problème de la schématisation de Grothendieck revisité. *Épijournal de Géométrie Algébrique, 4*, Article 14. https://doi.org/10.46298/epiga.2020.volume4.6060

## 6. Source inspection record

All inspection below took place on 15 November 2026. The distinction between metadata verification and full-text verification is intentional.

| Source | Actually inspected | Limit |
|---|---|---|
| Cartan | Publisher metadata; original GDZ scans of pp. 261–264 and 267–271, visually read | No identification with the manuscript inferred |
| Miller | Publisher-deposited Crossref metadata; bibliographic notices in Cartan and Garvín et al. | Original full text unavailable in this session |
| Garvín et al. | Full eight-page PDF, extracted text; especially Props. 3.1–3.2, Remark 3.3, Thms. 4.1–4.3 | Exact endpoint cited from displayed theorem |
| Dwyer | Original publisher metadata | Original full text unavailable in this session |
| Scheerer–Tanré | Full-text searchable article; p. 376 visually checked for the non-strict inequality | Used explicitly as primary follow-up |
| Mandell 2001 | Author’s submitted PDF, Main Theorem and Appendix A; Crossref metadata | Not silently equated with finite-field full faithfulness |
| Mandell 2006 | Published article PDF, introduction and Thms. 0.1–0.2 | Finite-type/nilpotence restrictions retained |
| Ekedahl | arXiv v2 full text, introduction and Thms. 2.9, 3.2; Crossref metadata | DOI is **a9**, not a8 |
| Toën | Journal’s 21-page PDF, introduction, Thm. 0.1, §1, Def. 2.1 | Only verified simply connected theorem used |
| Horel | Publisher record/abstract; arXiv v1 and current v2 theorem statements | Version dates distinguished |
| Hatcher | Author’s linked 2015-reprint PDF of the 2002 book, Theorem 3.19, printed p. 220 | Numbering follows this reprint; supports the projective-space ring computation |

Source PDFs and temporary rendered research images are outside the deliverable package, under `integral_literature_tmp/`. No source paper is reproduced in this memorandum.
