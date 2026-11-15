# Supporting research memo: Boolean rives and a relative cutting model

This memo was reconstructed after the execution-environment reset. All mathematical readings were taken from the already frozen transcription; no scan was delegated or reinterpreted here, and no page file was edited. The comprehensive item notes are B34–B51 in `records/research_parts/B_notes.md`; the discussion below supplies a precise model and the proof obligations behind those notes, without claiming that the manuscript explicitly specifies this model or that the observations are new.

## 1. What the manuscript actually defines

On cote 156-2, scan 015, `Comp(Z)` is the algebra of continuous maps to the discrete field with two elements, equivalently all clopen subsets. For $A$ closed in $X$, $U=X\setminus A$, and $i:U\hookrightarrow X$, the algebra of rives is

$$
R=\operatorname{Riv}(A,X)
=\mathop{\mathrm{colim}}_{V\supset A}\operatorname{Clop}(V\setminus A)
=\mathop{\mathrm{colim}}_{V\supset A}\Gamma(V,i_*\mathbb F_{2,U}).
$$

Neighborhoods are ordered by shrinking, with restriction maps. Addition is symmetric difference, multiplication is intersection, and $1+\rho$ is complement; a birive is the unordered complementary pair $\{\rho,1+\rho\}$. These definitions do not identify a rive with a single connected component, do not assert finiteness, and do not make every nontrivial birive a maille.

The relative-spectrum notation on scan 015 is underspecified: it literally assigns `Spec` of a sheaf on $X$ to $\widetilde A$, without writing restriction to $A$. This remains a reading question. The following is a consistent modern formalization, not an emendation.

## 2. A base-preserving spectrum

Let $\mathcal B=i_*\mathbb F_{2,U}$ and equip $X$ with the constant sheaf of fields $\mathbb F_{2,X}$. Gillam's relative-spectrum construction for sheaves of algebras over a locally ringed space provides a model with point set

$$
S=\{(x,\mathfrak p):x\in X,\ \mathfrak p\in\operatorname{Spec}(\mathcal B_x)\}
$$

and basic open subsets

$$
D_W(b)=\{(x,\mathfrak p):x\in W,\ b_x\notin\mathfrak p\},
\qquad b\in\mathcal B(W).
$$

The projection $p:S\to X$ has fiber $\operatorname{Spec}(\mathcal B_x)$; this is the construction checked in Gillam (2011, §2.2, Proposition 1, and §3.3). Every stalk is Boolean, so these fibers are Stone spaces, possibly empty where the stalk is the zero ring. The application of this construction to the manuscript is our interpretation, not something quoted from Gillam about Grothendieck's 1986 pages.

### Elementary checks in this Boolean specialization

**Unchanged complement.** On $U$, the sheaf $\mathcal B$ is $\mathbb F_{2,U}$, whose stalk spectrum is a single point. The basic-open description therefore identifies $p^{-1}(U)$ homeomorphically with $U$. At an interior point of $A$ the stalk is zero, so the full spectrum can have an empty fiber there; the later partial pushout is what adds two whole copies of $A$.

**Recovery of the Boolean sheaf.** Evaluation in the prime quotients gives a sheaf map

$$
\mathcal B\longrightarrow p_*\mathbb F_{2,S}.
$$

It is injective because a Boolean ring is reduced and its prime ideals separate its elements. To prove local surjectivity, take a locally constant binary function on $p^{-1}(W)$ and fix $x\in W$: compactness of the Stone fiber gives finitely many basic opens on which the function is constant and which cover that fiber. After shrinking the common base neighborhood, the Boolean join of the corresponding sections is $1$, because this equality holds in the stalk at $x$. Sections belonging to opposite function values have zero product, so the Boolean join of those with value $1$ represents the function on the smaller neighborhood. Thus the displayed sheaf map is an isomorphism; this paragraph is an elementary verification in the chosen model, not a separately cited theorem about the manuscript.

**Restriction to the boundary.** Put $S_A=p^{-1}(A)$. Applying the same construction to the inverse-image sheaf $\mathcal B|_A$ gives the same relative spectrum over $A$, because locally its sections come from sections on $X$. Consequently

$$
\operatorname{Clop}(S_A)\cong\Gamma(A,\mathcal B|_A).
$$

The canonical map from the neighborhood colimit $R$ is injective by equality of germs. For closed $A$ in paracompact Hausdorff $X$, the neighborhood-section theorem makes it surjective as well; Schapira (2023, Definition 10.1.1(ii) and Proposition 10.1.2(iii), printed p. 176) verifies precisely these hypotheses for sheaves of modules, which suffice here. The general sheaf-of-sets extension uses the same local gluing argument, but that generalization is not needed for this Boolean-ring application.

**Closed projection.** The projection $p$ is closed and has compact fibers: if a closed subset of $S$ misses the whole fiber over $x$, cover that fiber by finitely many basic opens in its complement. Their Boolean join equals $1$ in the stalk at $x$, hence on a neighborhood of $x$, whose entire preimage therefore misses the closed subset. This deduction explains why a point-set cutting construction can be made precise; it does not establish the additional regular-immersion assertions in scan 017.

## 3. The partial cutting and its limits

A birive in $R$ maps to complementary sections on $A$, producing a clopen partition $S_A=S_\rho\amalg S_{\rho'}$. Because $A$ is closed, these are closed subsets of $S$. Form the topological pushout

$$
\overline X
=S\amalg_{S_\rho} A_\rho
\amalg_{S_{\rho'}}A_{\rho'},
$$

where the maps to the two copies of $A$ are the restricted projections. In this model the copies $A_\rho,A_{\rho'}$ remain disjoint closed embedded copies, because a pushout along a closed inclusion preserves the other summand as a closed embedded subspace. The complement of their union is $S\setminus S_A\cong X\setminus A$, and the projection to $X$ is induced by $p$ and the two inclusions of $A$. These statements verify the elementary topology requested by the maps displayed on scan 017, conditional on the chosen relative-spectrum interpretation.

The construction does **not** prove that the two sides are nonempty at every stalk, that their projections separately surject onto $A$, or that the resulting marked space is a ficelle. Indeed, for two points $A=\{p,q\}\subset\mathbb R^2$, the two global rives may simply separate the neighborhoods of $p$ and $q$; one side then has no fiber at the other point. Grothendieck's maille conditions on scans 017–018 impose additional connectivity and regular-immersion requirements, and the marginal possible converse remains unproved in the supplied manuscript.

Contracting $A$ itself never changes its deleted complement: $(X/A)\setminus\{a\}\cong X\setminus A$. It can change connectivity of the ambient space or of a side that still contains another contracted subset. This distinction is essential when reducing disconnected node sets to points in the two-maille symmetry problem.

## 4. Three different constructions in a product example

For $X=S^1\times[-1,1]$ and $A=S^1\times\{0\}$, the boundary Boolean sheaf is the constant ring sheaf with stalk $\mathbb F_2^2$.

| Construction | Result in this example | Information retained |
|---|---|---|
| Relative Stone spectrum over $A$ | Two copies of $S^1$ | The base point and the two local sides |
| Étale space of ring elements | Four copies of $S^1$ | Each of the four stalk elements |
| Ordinary spectrum of the global Boolean algebra | Two points | Global clopen-side choices, without the base circle |

This proves that the three meanings cannot be interchanged in the cutting formula. The full relative boundary is generally not itself a Stone space when $A$ has positive-dimensional topology, even though each fiber is Stone.

## 5. The genuine profinite conclusion

For any Boolean ring $R$, each prime quotient is the two-element field, so every prime is maximal. The Stacks Project's Lemma 10.26.5 (Tag 00ER) identifies its spectrum as profinite, and Lemma 5.22.2 (Tag 08ZY) describes it as an inverse limit of finite discrete quotients arising from finite clopen partitions. Equivalently, the finite Boolean subalgebras of $R$ form a filtered union, and their finite spectra give the inverse system. This is the positive assertion of B51.

It does not reconstruct the whole cut space or the ambient form. Cones on $S^1$ and $S^2$ have identical rive algebra $\mathbb F_2$ at their vertices, while a cone on a Cantor set has an infinite rive algebra despite its compact link. The first example tests loss of link topology; the second separates compactness from finiteness. Neither claims that all enriched cuttings of these spaces coincide.

## 6. Endpoint scope after the interval counterexample

The literal ficelle definition does not require connected endpoints, as scan 005 itself emphasizes and scan 011 later proposes only as a reasonable restriction. Consequently the example $([0,1],\{0,1\},\{1/2\})$ refutes the asserted classification of all interval ficelles by terminal subintervals. The proof and the corrected connected-end classification are in `records/ficelle_interval_counterexample.md`.

Exactly two oriented equivalence classes under coordinatewise endpoint inclusion have been identified for the **connected-end interval subfamily**: the two orientations have the common minimal endpoint pairs $(\{0\},\{1\})$ and $(\{1\},\{0\})$, respectively. This exact count is not asserted for unrestricted disconnected endpoints. It is also separate from B52–B53, which prove existence and the arc uniqueness exception for **reduced** ficelles on connected nontrivial finite polyhedra.

## 7. Verified references and source scope

- Gillam, W. D. (2011). Localization of ringed spaces. *Advances in Pure Mathematics, 1*(5), 250–263. https://doi.org/10.4236/apm.2011.15045. Checked mathematical text: https://arxiv.org/pdf/1103.2139, §2.2, Proposition 1, §3.3. The retrieved PDF carries the original arXiv header and an internal compilation date of November 26, 2024; the section numbering stated here refers to that retrieved PDF. Publisher metadata verified volume, issue, pages, author, and DOI.
- Schapira, P. (2023, October 1). *An introduction to categories and sheaves* [Lecture notes]. Sorbonne Université. https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/CatShv.pdf. Checked Definition 10.1.1(ii), formula (10.1.2), and Proposition 10.1.2(iii), printed p. 176, PDF page index 175.
- The Stacks Project Authors. (n.d.-b). *Irreducible components of spectra* (Tag 00ER, §10.26). Retrieved November 14, 2026, from https://stacks.math.columbia.edu/tag/00ER. The relevant result is Lemma 10.26.5.
- The Stacks Project Authors. (n.d.-c). *Open and closed subsets of spectra* (Tag 04PN, §10.21). Retrieved November 14, 2026, from https://stacks.math.columbia.edu/tag/04PN. Checked Lemmas 10.21.1–10.21.3.
- The Stacks Project Authors. (n.d.-d). *Lemma 5.22.2: Profinite spaces* (Tag 08ZY). Retrieved November 14, 2026, from https://stacks.math.columbia.edu/tag/08ZY.

The letter suffixes match the main notes bibliography. Stone's 1936 paper was located through the AMS but its PDF returned HTTP 403, so it is a historical lead rather than a fully inspected proof source here. Search results at third-party textbook mirrors, nLab, and MathOverflow were used only as leads; the cited sheaf theorem was verified in the author-hosted Schapira text. No external source is used to change the frozen handwriting readings.
