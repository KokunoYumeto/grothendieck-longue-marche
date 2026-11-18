# Euler characteristics, conical ends, recycled sheets, and the loop-space leaf

Research contribution for **MPL_93_047-091**, covering cote **93, scans 055–070 and 083**. Written after the primary reader reported the transcription frozen at **2026-11-18 10:49:51 UTC** and the context opened at **10:49:56 UTC**. This contribution reads the frozen transcription and inventory, not the scan images, and changes none of the transcription, inventory, or doubts files.

## Scope and context conventions

The context's `README.md`, `notes/RESULTS_STATE.md`, and `hua_project/README.md` were read in full. Relevant sections of `same_cote_93/MPL_93_002-046_notes.md` and the full Euler/homotopy sections and contents map of `hua_project/93.modern.tex` were read; the supplied earlier notes and Hua's AI-produced interpretation remain **leads, not established results**. In particular, Hua's numbering is one lower than these scan numbers: his pages 54–67 are our scans 055–068, and his page 82 is our scan 083.

The state register contains no matching settled or open Euler-characteristic theorem. The explicit state identifiers used below are **MPL_93_002-046 O01**, **MPL_93_002-046 E26**, and **FINMON C2-CP2**; other references to earlier notes are references to the supplied notes file, not invented RESULTS_STATE entries. **S20** is the planning guess in `context/README.md`, not a matching register row.

For clarity in the research discussion only, χc denotes the frozen transcription's χ! and “finite total cohomology” means that the direct sum over all degrees is finite-dimensional over the chosen field. This report does not silently substitute sheaf cohomology for the manuscript's explicit singular-cohomology correction, nor turn Hua's mathematical repairs into manuscript readings.

`research_euler_context_search.tsv` records a targeted lexical search in each of the five context files for every EC note; exact substantive comparisons and matching or nonmatching state identifiers are stated in the notes below. `research_euler_events.tsv` distinguishes checked deductions, explicit computations, imported background, and conditional readings refuted by the countermodels.

## Itemized research notes

### EC01 — A separate Euler-characteristic dossier

**File/place:** 93/055, sole title. **Kind:** unpursued implication. **Quote:** “$χ$ et $χ_!$”.

The title introduces a coherent Euler-characteristic sequence whose mathematical leaves are 056, 058, 060, 062, 064, and 066; the intervening administrative typescripts belong to another text. This **adds** a distinct topological dossier to the separate orientation cluster recorded in `same_cote_93/MPL_93_002-046_notes.md`, O01, scans 027–031/033, and **confirms** Hua's `93.modern.tex`, V, title/contents identification (his p.54 = scan055). **RESULTS_STATE:** bears on **MPL_93_002-046 O01** and limits the README's S20 as an account of every sheet, without supplying a link to Gauss–Manin or Cartier.

### EC02 — The cohomology convention is explicitly revised

**File/place:** 93/056, definitions and margins. **Kind:** withdrawn in the same text. **Quote:** deleted “faisceautique”, replaced by “singulière”.

The change is substantive because the closed-set exact sequences subsequently invoked require comparison/excision hypotheses if the definitions are read literally in singular cohomology. Hua, `hua_project/93.modern.tex`, V “Les axiomes”, his p.55 = scan056, **differs** by interpreting compact-support cohomology as sheaf or Alexander–Spanier cohomology and asserting agreement in the eventual conical setting; that is a proposed mathematical repair, not this page's wording. **RESULTS_STATE:** no matching item; the earlier orientation notes O02/O04 in `same_cote_93/MPL_93_002-046_notes.md`, scans 028–033, provide a nearby sheaf/topology comparison but do not establish this comparison theorem.

### EC03 — Axiom (a): compact comparison

**File/place:** 93/056(a), restated 066(a). **Kind:** unproved claim. **Quote:** “Si $X$ compact”; “trivial”.

With compact-support cohomology defined as the direct limit of relative singular cohomology over compact subsets, the subset $K=X$ makes $H_c^*(X;k)=H^*(X;k)$, so both the finiteness equivalence and equality of characteristics follow. This **restates** the argument implicit in Hua, `hua_project/93.modern.tex`, V “Les axiomes”, scans056/066, while keeping the chosen theory explicit. **RESULTS_STATE:** no matching item.

### EC04 — Axiom (b): closed/open additivity

**File/place:** 93/056(b), restated 066(b). **Kind:** unproved claim. **Quote:** “résulte de suite ex. de cohomologie à supp. cpts”.

Once the asserted closed/open long exact sequence exists, its finite total dimensions prove both the two-out-of-three finiteness statement and $χ_c(X)=χ_c(Y)+χ_c(X\setminus Y)$ by cancellation of image dimensions. The unresolved hypothesis issue is the existence of that sequence in the literal singular theory on the initially unrestricted spaces, not the alternating-sum algebra. Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan056), **restates** the sequence argument after changing the cohomology convention; **RESULTS_STATE:** no matching item.

### EC05 — Axiom (c): closed Mayer–Vietoris needs its hypotheses

**File/place:** 93/056(c). **Kind:** unproved claim. **Quote:** “fermés dans $X$ de réunion $X$”.

The Euler identity and three-out-of-four finiteness follow from a Mayer–Vietoris long exact sequence, but closedness alone is not the usual singular-cohomology excision hypothesis; Hatcher's author-hosted text explicitly states the interior-cover condition and also treats CW subcomplex covers [EUL-S1, §2.2 and §3.1]. This **restates the cohomology caution** of Hua, `hua_project/93.modern.tex`, V “Les axiomes”, his p.55 = scan056, and **differs** by leaving its asserted locally conical repair conditional on checking the inclusions or a comparison with sheaf cohomology. **RESULTS_STATE:** no matching item.

### EC06 — The stronger bracketed finiteness claim

**File/place:** 93/056, bracket below (c). **Kind:** unproved claim. **Quote:** “Même”, followed by $X,X'\cap X''\in\mathcal E_χ$.

Under the same valid Mayer–Vietoris hypotheses, each degree of $H^*(X')\oplus H^*(X'')$ sits between a subquotient of $H^*(X)$ and one of $H^*(X'\cap X'')$, so finite total dimension of those two outer spaces does imply finite total dimension of both pieces. This **restates and checks the algebraic point** made in Hua, `hua_project/93.modern.tex`, V “Les axiomes”, footnote on scan056, while inheriting EC05's topological qualification. **RESULTS_STATE:** no matching item.

### EC07 — Axiom (d): domination gives finiteness, not equality of Euler numbers

**File/place:** 93/056(d), restated 066(d). **Kind:** unproved claim. **Quote:** inserted “dominé”; $ji\simeq\mathrm{id}_X$.

The maps split $H^*(X;k)$ off $H^*(X';k)$, proving the asserted finiteness under domination; equality of Euler numbers requires the subsequent homotopy-equivalence case, not domination alone. For example, a point is dominated by $S^1$ but their Euler numbers differ. Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan056), **restates the correctly restricted implication**; **RESULTS_STATE:** no matching item.

### EC08 — Axiom (e): point and empty-space normalization

**File/place:** 93/056(e), restated 066(e). **Kind:** unproved claim. **Quote:** $\chi(pt)=1$; $\chi(\varnothing)=0$.

The zero chain complex for the empty space and the degree-zero copy of $k$ for a point directly give these values; contractibility then follows from (d), explaining why the broader introductory phrase is deleted. Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan056), **restates** the normalization without treating the deletion as a rejected mathematical theorem. **RESULTS_STATE:** no matching item.

### EC09 — Finite disjoint sums

**File/place:** 93/058, marginal item 1. **Kind:** unproved claim. **Quote:** $X'\amalg X''$.

For a finite disjoint union, both ordinary cohomology and compact-support cohomology split into the two summands, so the finiteness equivalence and additivity are valid in either convention. The finiteness of the union is essential to the total-dimension formulation and should not be silently extended to arbitrary coproducts. Hua, `hua_project/93.modern.tex`, V “Premières conclusions”, footnote (his p.57 = scan058), **restates** this marginal addition; **RESULTS_STATE:** no matching item.

### EC10 — Euclidean spaces, closed balls, and spheres

**File/place:** 93/058, item 2 and proof. **Kind:** unproved claim. **Quote:** “Conclusions provisoires”.

The displayed values follow in the usual tame setting from contractibility, compact comparison, the hemispherical decomposition, and $\mathbb R^n\cong S^n\setminus\{pt\}$; the hemisphere step uses an excisive enlargement or CW decomposition, not merely the bare word “closed”. These give $χ(\mathbb R^n)=1$, $χ_c(\mathbb R^n)=(-1)^n$, and $χ(S^n)=1+(-1)^n$, including the stated $n=0$ base case. This **restates and checks** Hua, `hua_project/93.modern.tex`, V “Premières conclusions” (scan058); **RESULTS_STATE:** no matching item.

### EC11 — A visible ordinary/compact-support mismatch remains frozen

**File/place:** 93/058, last displayed line of the proof. **Kind:** reading question. **Quote:** $\chi(R^n)=\chi(S^n)-\chi(pt)$.

The line uses ordinary $χ$ even though the preceding application is to compact-support additivity; for odd $n$ its result $(-1)^n$ disagrees with the earlier ordinary value $1$. Hua, `hua_project/93.modern.tex`, V “Premières conclusions” (scan058), **differs** by correcting this to $χ_c$ in its modernization; this report records the disagreement and leaves the frozen transcription unchanged. **RESULTS_STATE:** no matching item.

### EC12 — The cellular Euler formula needs a compatible filtration

**File/place:** 93/058, item 3. **Kind:** unproved claim. **Quote:** “filtration de l'espace $X$”.

The induction by (b) proves $\chi_c(X)=\sum_i(-1)^i f_i$ when the filtration stages are closed, the differences are the stated finite unions of cells, and the compact-support exact sequences apply. The frozen wording does not explicitly insert “closed” here, whereas Hua, `hua_project/93.modern.tex`, V “Premières conclusions” (scan058), **adds** that hypothesis in its modern statement and footnote. **RESULTS_STATE:** no matching item; this is a hypothesis question, not a transcription correction.

### EC13 — Axiom (f), ordinary product formula

**File/place:** 93/060(f), restated 066(f). **Kind:** unproved claim. **Quote:** “Künneth pour $H_*(X\times Y,k)$”.

Over a field, homological Künneth followed by duality with cohomology gives the claimed finite total dimension and multiplicativity when both factors have finite total ordinary cohomology. The use of homology is a useful way to avoid an unjustified dual-of-an-infinite-tensor-product step, even though the surviving homology groups are finite in the stated case. Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan060), **restates** the result; **RESULTS_STATE:** no matching item.

### EC14 — Axiom (f), compact-support product formula

**File/place:** 93/060(f), restated 066(f). **Kind:** unproved claim. **Quote:** “Künneth pour $H^*_!(X\times Y,k)$”.

The formal multiplication of finite alternating sums is sound once the compact-support Künneth comparison is available, but the manuscript does not spell out its topological and cohomological hypotheses. A finite cell-filtration setting proves the statement directly by multiplying cells; extension to the exact conical category should be checked through the chosen support theory. This **differs from the unqualified scope** of Hua's summary in `hua_project/93.modern.tex`, V “Les axiomes” (scan060); **RESULTS_STATE:** no matching item.

### EC15 — Axiom (g) is initially broad and subsequently narrowed

**File/place:** 93/060(g), compared with 066(g). **Kind:** withdrawn in the same text. **Quote:** “fibration loc. triviale de fibre $F$”; later “tout au moins si $Y$ est un polyèdre relatif”.

Scan060 initially states the ordinary and compact-support multiplicativity assertions on the cohomologically finite classes, while its margin already qualifies them and scan066 retains an explicit restriction on the base. The locally compact ordinary-cohomology countermodel in EC21 explains why cohomological finiteness by itself is insufficient; it does not refute the later conical/polyhedral statement. Hua, `hua_project/93.modern.tex`, V “Les axiomes” and “Espaces localement coniques” (scans060/066), **restates the same narrowing**; **RESULTS_STATE:** no matching item.

### EC16 — The spectral-sequence finiteness step is explicitly conditional

**File/place:** 93/060, proof of (g). **Kind:** self-flagged. **Quote:** “sous réserve”; “Il faut prouver”.

The author conditions the spectral-sequence Euler sum on finite total dimension of the $E_2$ terms and immediately isolates the finite-rank local-system lemma needed to establish it. Finite total cohomology with constant coefficients does not alone justify that step, as EC21 shows for ordinary coefficients. Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan060), **restates** the reduction, but the frozen formulas also contain ordinary/compact-support notation slips already identified in its footnote; **RESULTS_STATE:** no matching item.

### EC17 — The finite-cell proof of the compact-support local-system lemma

**File/place:** 93/060, lower lemma and cell sum. **Kind:** unproved claim. **Quote:** “Marche tout au moins”.

For a finite closed filtration with strata finite disjoint unions of $\mathbb R^d$, a rank-$b$ local system is constant on each cell, whose compact-support Euler contribution is $b(-1)^d$; additivity proves the lemma in this stated range. This is a check of the displayed finite-cell argument, not of the initial lemma on every $Y\in\mathcal E_{\chi!}$. Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan060), **restates this restricted proof**; **RESULTS_STATE:** no matching item.

### EC18 — Triangulability is replaced by a finite filtration

**File/place:** 93/060, line before the last calculation. **Kind:** withdrawn in the same text. **Quote:** deleted “triangulable”; inserted “admet filtration finie”.

The replacement records the actual finite combinatorial input used in the argument and is not merely a stylistic synonym for an arbitrary triangulation. It **adds a useful limitation** to Hua, `hua_project/93.modern.tex`, V “Les axiomes” (scan060), which presents the resulting filtration formulation but does not foreground this change of wording. **RESULTS_STATE:** no matching item.

### EC19 — The finite-cover alternative is not a completed proof

**File/place:** 93/062, opening continuation, marked $(g_2|g'_2)$. **Kind:** unproved claim. **Quote:** “tels que les intersections”.

The proposed compact-base condition uses arbitrarily fine finite covers by closed or open sets whose nonempty intersections lie in the finite compact-support class; a proof must also relate those intersections and the local-system trivializations to a valid cover spectral sequence. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (his p.61 = scan062), **differs** by calling the labels $(\psi_1),(\psi_2)$ and saying they are missing from the conserved pages, whereas the frozen package supplies the preceding finite-filtration argument and leaves the actual label doubtful. **RESULTS_STATE:** no matching item; the context does not resolve the label or establish the proposed criterion.

### EC20 — The ordinary local-system lemma needs more than ordinary finiteness

**File/place:** 93/062, homological lemma. **Kind:** unproved claim. **Quote:** “on utilise la suite spectrale d'homologie”.

A finite CW model gives $\chi(Y;\mathcal R)=b\chi(Y)$ because its twisted cellular chain groups have $b$ times the ordinary cell ranks, but membership in $\mathcal E_\chi$ alone does not guarantee this result. The page itself appends a further hypothesis involving a homotopy equivalent $Y'$ satisfying the cover condition. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), **restates the homology route** without proving unrestricted validity; **RESULTS_STATE:** no matching item.

### EC21 — A locally compact countermodel to the unrestricted ordinary claims

**File/place:** 93/060(g), 062 local-system lemma. **Kind:** own idea. **Confidence:** high for the explicit ordinary-cohomology counterexample; it is deliberately outside the later conical-at-infinity category. **Anchor:** “Énoncé analogue”.

Let $Y$ be the locally finite mapping telescope of $\mathbb{RP}^2\hookrightarrow\mathbb{RP}^3\hookrightarrow\cdots$ and let $X$ be its two-sheeted cover, the telescope of the antipodal sphere covers; these are locally compact CW spaces with $Y\simeq K(C_2,1)$ and $X$ contractible, so over $\mathbb Q$ one has $\chi(Y)=\chi(X)=1$ but $\chi(\{1,2\})=2$. The sign rank-one local system on $Y$ has zero cohomology in every degree, hence Euler number $0\ne1$, giving the same obstruction directly to the ordinary local-system lemma (the construction and proof are detailed below; telescope facts are documented in [EUL-S1, §3F]). This **adds a counterexample**, absent from Hua, `hua_project/93.modern.tex`, V (scans060/062), and does not contradict his or the manuscript's finite-cell restriction. **RESULTS_STATE:** no matching item; refined statement **EC20** is the finite-CW version.

### EC22 — The homology index is an actual correction

**File/place:** 93/062, local-system display and underbrace. **Kind:** withdrawn in the same text. **Quote:** $H_{\inserted{p}}^{\deleted{p}}$; “le dual est $H^p(Y,\check{\mathcal R})$”.

The correction changes the displayed group from cohomological to homological indexing and pairs it with a dual local system, supporting the ordinary homology argument rather than an unrestricted self-duality of local systems. The alternating sum still displays groups rather than their dimensions, a separate notational shorthand that is retained in the transcription. This **adds the local correction** to Hua's summary in `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062); **RESULTS_STATE:** no matching item.

### EC23 — The recursive conical class needs a precise convention

**File/place:** 93/062(h), recursive definition. **Kind:** reading question. **Quote:** “classe”; “espaces loc. côniques”.

The intended induction appears to start with the empty link and compact conical neighborhoods, but the frozen link condition has the unresolved alternative $S\in\mathcal E_{n-1}|\mathcal C_{n-1}$, and the marginal notation uses $\mathcal E_n$. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), **differs by choosing $\mathcal C$ throughout** and thereby supplies a coherent modern definition; that choice cannot decide the frozen letters. **RESULTS_STATE:** no matching item; any general theorem below specifies the standard compact-Hausdorff recursive-cone interpretation separately.

### EC24 — The marginal “discrete spaces” cannot mean all discrete spaces in the finiteness claim

**File/place:** 93/062, marginal $\mathcal E_0$ line. **Kind:** own idea. **Confidence:** high for the elementary obstruction; low for identifying which notational convention was intended. **Anchor:** “espaces discrets”.

An infinite discrete space has infinitely many independent degree-zero cohomology classes and therefore cannot belong to the claimed finite-total-cohomology category; its one-point compactification also lacks a conical, locally contractible neighborhood at the accumulation point. Thus the margin must be read with a finiteness/compactness convention or as a different local class before it can be used with the subsequent proposition. This **adds a concrete consistency test** to Hua's global replacement of $\mathcal E_n$ by $\mathcal C_n$ in `hua_project/93.modern.tex`, V (scan062); **RESULTS_STATE:** no matching item.

### EC25 — Low-dimensional triangulation claims and the cancelled compact case

**File/place:** 93/062, marginal $\mathcal E_1$ through $\mathcal E_3$ list. **Kind:** withdrawn in the same text. **Quote:** deleted “ils sont triang. dans le cas cpt” after the dimension-three line.

The margin distinguishes local triangulability from compact global triangulability and cancels one explicit compact-case assertion, so that cancelled assertion should not be reported as a settled theorem written on this sheet. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), **differs** by summarizing compact triangulability through dimension three without preserving this cancellation. **RESULTS_STATE:** no matching Euler item; compare `same_cote_93/MPL_93_002-046_notes.md`, O06, scans028–030, for a separate low-dimensional hypothesis caution rather than a proof of this broader conical-space statement.

### EC26 — The dimension-four triangulation question has a later negative manifold example

**File/place:** 93/062, last marginal paragraph. **Kind:** self-flagged. **Quote:** “il n'est pas clair qu'ils sont triangulables”.

The compact topological four-manifold $E_8$ supplies a later negative example while still being locally conical, since manifold charts have spherical links; Moise's theorem concerns three-manifolds, not a general four-dimensional triangulation theorem [EUL-S3, §2.2]. This **restates the dimensional distinction** made by Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), while the frozen placement of “(Moïse)” is left untouched. **RESULTS_STATE:** no matching item; `same_cote_93/MPL_93_002-046_notes.md`, O06, scans028–030, discusses a different four-dimensional exception in orientation axioms and does not settle the question posed here.

### EC27 — Compact conical finiteness and the ANR route

**File/place:** 93/062, proposition and compact-case proof. **Kind:** unproved claim. **Quote:** “comme $X$ est loc. contractile”.

Under the standard compact-Hausdorff recursive-cone reading, induction supplies finite-dimensional metrizable local charts, and a finite subcover makes the compact space metrizable; local contractibility then gives the usual finite-dimensional ANR route. West's compact metric ANR theorem supplies finite CW homotopy type [EUL-S2, Corollary5.3], which is stronger than the required finite total cohomology, but its hypotheses and the interpretation of the recursive definition must be recorded. This **adds an explicit modern route** to the abbreviated argument in Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062); **RESULTS_STATE:** no matching item, and no independent proof of West's theorem is claimed.

### EC28 — Compact-support finiteness by deleting infinity

**File/place:** 93/062, noncompact case; 066(h), first identity. **Kind:** unproved claim. **Quote:** $\widehat X-\omega=X$.

If the compactification belongs to the compact finite-cohomology class and the closed/open exact sequence is valid, deleting its distinguished point yields $X\in\mathcal E_{\chi!}$ and $\chi_c(X)=\chi(\widehat X)-1$ immediately. This **restates and checks the conditional deduction** in Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scans062/066), without claiming the comparison hypotheses proved for arbitrary compacta. **RESULTS_STATE:** no matching item.

### EC29 — The truncated compact core must remain in the conical class

**File/place:** 93/064(a), after the definition of $X'$. **Kind:** self-flagged. **Quote:** “On vérifie”; margin “vérifier”.

The assertion $X'\in\mathcal C_\infty$ requires checking neighborhoods on the new boundary of the removed smaller cone, where local models are products of a link neighborhood and a half-interval. A cone/join or collar argument should establish the appropriate closure property under a precise inductive definition, but that argument is not supplied here. This **restates the membership assertion and adds the verification flag** omitted from Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (his p.63 = scan064); **RESULTS_STATE:** no matching item.

### EC30 — The punctured cone retracts radially onto the compact core

**File/place:** 93/064(b). **Kind:** self-flagged. **Quote:** $X'\sim X=\widehat X-\omega$; “vérifier”.

In a genuine cone chart with radial coordinate $r>0$, the homotopy $r\mapsto(1-t)r+t\max(r,1/2)$, extended by the identity outside the chart, gives the required deformation retraction onto the complement of the open half-cone. This checks the homotopy step once the stated cone neighborhood is available and distinct from the unproved closure assertion EC29. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan064), **restates this equivalence**; **RESULTS_STATE:** no matching item.

### EC31 — Axiom (h): the defect is the Euler characteristic of the end link

**File/place:** 93/064, boxed identity; 066(h). **Kind:** unproved claim. **Quote:** “structure locale de $X$ à l'infini”.

For an excisive decomposition $\widehat X=X'\cup T$ with $T$ contractible and $X'\cap T=S_\omega$, Mayer–Vietoris gives $\chi(X')=\chi(\widehat X)-1+\chi(S_\omega)$; combining EC28 and EC30 proves $\chi(X)-\chi_c(X)=\chi(S_\omega)$. Thus the calculation is conditional on the compact-core/excision setup, but its alternating-sum step is complete. This **restates and checks** Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scans064/066); **RESULTS_STATE:** no matching item.

### EC32 — The end-link formula has immediate diagnostic examples

**File/place:** 93/064/066(h). **Kind:** own idea. **Confidence:** high for the finite-dimensional examples. **Anchor:** $\chi(X)-\chi_!(X)=\chi(S_\omega)$.

For $X=\mathbb R^n$, the defect $1-(-1)^n$ equals $\chi(S^{n-1})$, while for the interior of a compact manifold with collared boundary it becomes the familiar difference between the Euler numbers of the core and of its boundary-relative complex. The first check **restates** Hua's explicit example in `hua_project/93.modern.tex`, V (scan064); the collared-core interpretation **adds** a test of the geometric meaning without asserting that arbitrary ends are conical. **RESULTS_STATE:** no matching item.

### EC33 — The complement letter in the final axiom (b)

**File/place:** 93/066(b). **Kind:** reading question. **Quote:** $\chi_!(\unsure{Y|X}-Y)$.

The first frozen alternative produces an empty complement rather than $X\setminus Y$, whereas scan056(b) and the proof of the later compactification identity use $X-Y$. Hua, `hua_project/93.modern.tex`, V “Les axiomes” and final theorem (scans056/066), **differs by choosing the mathematically coherent complement $X-Y$**; this comparison is recorded as a reading question, without altering the frozen alternative order. **RESULTS_STATE:** no matching item.

### EC34 — The final axiom (c) omits the covering condition

**File/place:** 93/066(c), compared with 056(c). **Kind:** reading question. **Quote:** “$X',X''$ fermés dans $X$”.

The final formulation omits the explicit condition $X=X'\cup X''$ present on scan056; without it, even $X=S^1$ and $X'=X''=\{pt\}$ give the false numerical equation $0=1$. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan066), **differs by supplying that condition in a footnote**, confirming a gap in the literal summary rather than a reason to repair the transcription. **RESULTS_STATE:** no matching item; refined statement **EC05** retains the cover and excision conditions.

### EC35 — Axiom (d) treats the two invariances differently

**File/place:** 93/066(d). **Kind:** unpursued implication. **Quote:** $X\sim X'$ versus $X\simeq X'$.

The ordinary characteristic is assigned homotopy invariance, while the compact-support characteristic is attached to the stronger equivalence sign used here; it must not be promoted to arbitrary homotopy invariance, since $\mathbb R\simeq_{\mathrm{htpy}}pt$ but $\chi_c(\mathbb R)=-1\ne1$. This **adds an explicit distinction to** Hua, `hua_project/93.modern.tex`, V (scan066), implicit in its two invariant definitions. **RESULTS_STATE:** no matching item; the exact sign convention remains governed by the frozen notation table.

### EC36 — Uniqueness on relative polyhedra

**File/place:** 93/066, final paragraph. **Kind:** unproved claim. **Quote:** “uniquement déterminées par les propriétés a à e”.

For finite polyhedral pairs, point normalization, compact comparison, and closed/open additivity reduce $\chi_c$ to the finite cell sum, while a compact core and homotopy invariance determine the ordinary value. The finiteness and compatibility of the chosen polyhedral decomposition must be part of the interpretation; an unrestricted infinite triangulation is insufficient for this argument. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan066), **restates the restricted uniqueness result**; **RESULTS_STATE:** no matching item.

### EC37 — The author does not claim unrestricted fibration multiplicativity on the final class

**File/place:** 93/066, margin beside (g). **Kind:** self-flagged. **Quote:** “j'ignore si c'est vrai sans telle restriction”.

The explicit question is whether the relative-polyhedral base restriction can be removed within the final locally conical-at-infinity setting, not merely whether the earlier cohomologically finite version is valid. EC21 refutes the earlier unrestricted ordinary statement but does not answer this narrower question, because its telescope has no finite conical end. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan066), **restates this qualification**; **RESULTS_STATE:** no matching item.

### EC38 — The author leaves global axiomatic uniqueness open

**File/place:** 93/066, bottom margin. **Kind:** self-flagged. **Quote:** “j'ignore si $\chi$ et $\chi_!$ sont caractérisés par a) à e) sur tout $\mathcal E_\infty$”.

The marginal question separates existence of the two cohomological functions from characterization by the first five axioms on the whole conical category. Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan066), **restates the question**, but its footnote's claim that the theorem itself says “deux fonctions uniques” is not supported by the frozen main sentence, which says “on peut trouver deux fonctions numériques”. **RESULTS_STATE:** no matching item; the possible modern completion is deliberately separated in EC39.

### EC39 — A conditional modern route to the uniqueness question

**File/place:** 93/062–066, especially 066 bottom margin. **Kind:** own idea. **Confidence:** medium for translation of the manuscript's category; high for the stated reduction once the ANR and cone hypotheses hold. **Anchor:** “caractérisés par a) à e)”.

Under the compact-Hausdorff recursive-cone interpretation, West's finite-CW result [EUL-S2, Corollary5.3] applies to compact members and to the compact ANR core obtained by radial truncation, so both $X$ and $\widehat X$ have finite-polyhedral homotopy models. Axioms (d)/(e) and compact polyhedral additivity determine $\chi(X)$ and $\chi(\widehat X)$, and (a)/(b) then force $\chi_c(X)=\chi(\widehat X)-1$, giving a route to uniqueness without requiring a triangulation of $X$ itself. This **adds a conditional completion**, absent from Hua, `hua_project/93.modern.tex`, V (scans062–066); **RESULTS_STATE:** no matching item, and no unconditional theorem for every interpretation of the shorthand category is claimed.

### EC40 — Coefficient-field independence in the controlled range

**File/place:** 93/056 “$k$ corps”; 058/066 Euler sums. **Kind:** own idea. **Confidence:** high for finite polyhedral pairs; conditional for the broader conical class. **Anchor:** $\chi_!(X)=\sum(-1)^i f_i$.

The finite cell formula is integral and independent of the field, so the Euler numbers in that range do not depend on the initial choice of $k$ even though the individual Betti numbers can. The same conclusion would follow on the precisely defined conical class from the compact-core route in EC39, but this should not be conflated with field-independent membership in the original broad cohomologically finite classes. This **adds an implication** to Hua, `hua_project/93.modern.tex`, V (scans056/058/066); **RESULTS_STATE:** no matching item.

### EC41 — A limited connection with finite-category homotopy models

**File/place:** 93/062, compact-conical proposition. **Kind:** own idea. **Confidence:** high conditional on the finite-polyhedron homotopy model in EC27. **Anchor:** “espaces loc. côniques”.

A finite simplicial model has a finite face poset whose nerve is its barycentric subdivision, so the compact conical spaces covered by EC27 also have finite-category models. This **adds a thematic connection** to **RESULTS_STATE: FINMON C2-CP2**, but gives no bound on the minimum number of arrows and settles none of that entry's minimization question. Hua, `hua_project/93.modern.tex`, V (scan062), does not pursue this category-theoretic consequence; the earlier file `same_cote_93/MPL_93_002-046_notes.md`, O01, scans027–033, only identifies the adjacent topological cluster.

### EC42 — The theme list is evidence of breadth, not a demonstrated arithmetic bridge

**File/place:** 93/068, isolated list. **Kind:** unpursued implication. **Quote:** “rel. entre $\pi_1$ et th. de Galois”; “Conj. de Weil”.

The list puts orientation, embeddings, homology/Euler characteristic, covering spaces, complex-variable functions, and Galois/Weil themes on one leaf, but supplies no construction relating the Euler axioms to Cartier or projective connections. Hua, `hua_project/93.modern.tex`, V, final paragraph (his p.67 = scan068), **restates the list**; it **adds programmatic breadth** to `same_cote_93/MPL_93_002-046_notes.md`, O01 and E26, scans027–033 and023–024, without upgrading the README's S20 from a hypothesis to a proved unity. **RESULTS_STATE:** bears on **MPL_93_002-046 O01** and **MPL_93_002-046 E26**, neither used here as an established mathematical result.

### EC43 — Six interleaved sheets belong to an administrative research-policy text

**File/place:** 93/057,059,061,063,065,067. **Kind:** reading question. **Quote:** “La politique de recherche des établissements”; “D.E.S.U.R.”.

The headings and internal pagination identify a continuous, reversed-order administrative discussion of university research policy, funding, and evaluation, not the Euler manuscript; its full title and author are absent from these sheets. This **adds a typed-sheet census** not supplied by Hua, `hua_project/93.modern.tex`, V (the intervening reverse-side pages), and parallels the source-separation method in `same_cote_93/MPL_93_002-046_notes.md`, §3, scans032/034 and other reused texts. **RESULTS_STATE:** bears on **MPL_93_002-046 §3** as a first-pass inventory lead, not a result; annotation evidence and uncertain attribution are separated in the table below.

### EC44 — The research-policy questions are not Grothendieck's mathematical conjectures

**File/place:** 93/067, §3.2; 057, §5.2. **Kind:** reading question. **Quote:** “Les établissements ont-ils des missions de recherche ?”.

The further question about separating teaching from research and the warning on scan057 about an automated numerical allocation of funds belong to the unidentified administrative typescript's argument. Their presence is worth registering, but neither authorship nor agreement by Grothendieck follows from physical reuse of the sheets. This **adds an attribution caution** absent from Hua, `hua_project/93.modern.tex`, V (scans057/067), and **restates the methodological distinction** in `same_cote_93/MPL_93_002-046_notes.md`, §5, concerning third-party text; **RESULTS_STATE:** no matching mathematical item.

### EC45 — The corrected budget total has a direct arithmetic check

**File/place:** 93/061, 1976 total. **Kind:** own idea. **Confidence:** high for the arithmetic; no confidence claim about the correcting hand. **Anchor:** $275+79$ and the inserted middle digit in the total.

The six column totals agree with the two recorded budget rows, and the 1976 sum is $354$, agreeing with the inserted $5$ rather than the cancelled uncertain digit. The calculation supports the correction's numerical sense but cannot authenticate its author or date the mathematical notes; the administrative text itself speaks of the already-distributed 1976 budget. This **adds an explicit check** to the uncensused reverse sheets in Hua, `hua_project/93.modern.tex`, V, and to the reused-sheet comparison in `same_cote_93/MPL_93_002-046_notes.md`, §3; **RESULTS_STATE:** no matching item.

### EC46 — The name/address cover remains an unidentified textual layer

**File/place:** 93/069–070. **Kind:** reading question. **Quote:** doubtful “Thévenet|Théorème” and “Contre-Conière|Contre-Courant”.

The cover contains a name list, a doubtful short heading, and a reverse-side address, with no unambiguous mathematical title or written page total. The possible name resemblance to the orientation offprint's author does not establish identity or a mathematical connection, and no personal-identification search was made. This **adds material not analyzed** in Hua, `hua_project/93.modern.tex`, its transition from V to VI; **RESULTS_STATE:** only the thematic comparator **MPL_93_002-046 O01**, scans027–033, is relevant, and it does not resolve the names.

### EC47 — The loop-space leaf asks a question rather than presenting a proof

**File/place:** 93/083, first display and upper diagram. **Kind:** self-flagged. **Quote:** $X=\Omega Y$ and $\overset{?}{=}0$.

The page sketches a low Postnikov invariant and possible successive desuspensions but supplies no conclusion or proof of vanishing. Hua, `hua_project/93.modern.tex`, VI “Une page étrangère” (his p.82 = scan083), **restates the question** and correctly treats the leaf as separate from the surrounding projective-differential calculations. **RESULTS_STATE:** no matching Postnikov item; the general homotopy/finite-model programme is contextual background only.

### EC48 — Vanishing of the class and vanishing of its ambient group are different readings

**File/place:** 93/083, uppermost row. **Kind:** reading question. **Quote:** $k_1\in H^3(\pi_1(X),\pi_2(X))\overset{?}{=}0$.

The frozen arrangement places the question-marked equality after the cohomology group, whereas Hua, `hua_project/93.modern.tex`, VI “Une page étrangère” (scan083), **differs by interpreting it as a question about the particular class $k_1$**. Those are mathematically different assertions, so the research discussion keeps both possible readings visible and does not alter the transcription. **RESULTS_STATE:** no matching item.

### EC49 — Ambient-group vanishing fails even for an infinite loop space

**File/place:** 93/083, question-marked zero. **Kind:** own idea. **Confidence:** high, with the finite normalized-cochain calculation recorded in the accompanying script. **Anchor:** $H^3(\pi_1(X),\pi_2(X))$.

Take $X=K(C_2,1)\times K(C_2,2)$, which is an infinite loop space with zero first Postnikov class, but $H^3(C_2;C_2)=C_2\ne0$. Thus a claim that the ambient group always vanishes is false even under arbitrarily many deloopings, independently of the subtler class-vanishing question. This **adds a counterexample to the literal group reading** absent from Hua, `hua_project/93.modern.tex`, VI (scan083); **RESULTS_STATE:** no matching item, with refined distinction **EC48**.

### EC50 — One delooping gives one cohomology-suspension lift

**File/place:** 93/083, dashed arrow from $k'_1$ and the lower diagrams. **Kind:** unproved claim. **Quote:** $\exists\,k'_1\in H^4(K(\pi_1(X),2),\pi_2(X))$.

For a connected loop space of CW type, the expected relation is cohomology suspension of the delooping's Postnikov class; Arlettaz states this explicitly in Lemma7.4 [EUL-S4]. This **restates the proposed relation in** Hua, `hua_project/93.modern.tex`, VI “Une page étrangère” (scan083), but it does not manufacture a second delooping from the first. **RESULTS_STATE:** no matching item.

### EC51 — Two deloopings do force the first class to vanish

**File/place:** 93/083, $k''_1$ row and continuing tower. **Kind:** unpursued implication. **Quote:** $H^5(K(\pi_1(X),3),\pi_2(X))$.

Arlettaz's Proposition7.5 identifies the double cohomology suspension from this degree-five group to the displayed degree-three group as zero, and Theorem7.6 consequently proves vanishing of the first Postnikov class for connected double loop spaces [EUL-S4]. This **adds a precise later theorem** to Hua's unresolved account in `hua_project/93.modern.tex`, VI (scan083), while retaining the extra delooping hypothesis. **RESULTS_STATE:** no matching item; the source's short deduction was checked, not the entire background computation independently reproved.

### EC52 — A checked algebraic model with nonzero first class after one delooping

**File/place:** 93/083, possible $k_1=0$ reading. **Kind:** own idea. **Confidence:** high for the algebra and cocycle; realization uses the cited theorem rather than a new proof. **Anchor:** $X=\Omega Y$.

The reduced quadratic module $M=\mathbb Z$, $L=\mathbb Z\oplus C_4$, $\partial(m,b)=2m$, and $w(x,y)=(0,xy\bmod4)$ has associated action $(m,b)^x=(m,b+2mx)$, cokernel $C_2$, and kernel $C_4$, and its normalized crossed-module cocycle has value $2\in C_4$ on $(1,1,1)$, which is not a coboundary. The realization/looping correspondence of Baues–Conduché [EUL-S5, §§4.5–4.7] therefore supplies a connected single-loop 2-type with nonzero first class, answering that unrestricted class-vanishing reading negatively; the explicit algebra and finite quotient certificate are detailed below. This **adds a checked countermodel**, absent from Hua, `hua_project/93.modern.tex`, VI (scan083); **RESULTS_STATE:** no matching item, and the refined positive statement is **EC51**.

### EC53 — The higher rows require compatible additional deloopings

**File/place:** 93/083, last upper row. **Kind:** unproved claim. **Quote:** $H^{5+r}(K(\pi_1(X),3+r),\pi_2(X))$ (the exponent letter is doubt-marked in the transcription).

The continuation suggests a stable-range approach, but a lift into this tower is additional structure, not a consequence of $X=\Omega Y$ alone. Once two compatible suspension lifts exist, EC51 already kills the first class, so the higher rows are relevant to the mechanism rather than needed for that first vanishing conclusion. This **restates the stable continuation** interpreted in Hua, `hua_project/93.modern.tex`, VI “Une page étrangère” (scan083); **RESULTS_STATE:** no matching item.

### EC54 — Splitting the 2-type need not be natural

**File/place:** 93/083, implied zero-class branch. **Kind:** own idea. **Confidence:** high for the cited distinction; no claim it is discussed on the sheet. **Anchor:** $k_1$.

Even where the double-loop first class vanishes and the 2-type splits as a product of Eilenberg–MacLane spaces, Baues–Conduché show that the splitting cannot generally be chosen naturally in the delooped space [EUL-S5, Introduction and Theorem1.9]. This **adds a caution about functorial strengthening**, not present in Hua, `hua_project/93.modern.tex`, VI (scan083), and should not be confused with failure of the objectwise vanishing theorem. **RESULTS_STATE:** no matching item.

### EC55 — The one-dimensional marginal identification

**File/place:** 93/062, marginal $\mathcal E_1$ line. **Kind:** unproved claim. **Quote:** “1-complexes topologiques”.

Under the compact recursive-cone convention of EC23, with the cone on the empty link interpreted as a point, the zero-dimensional compact links are finite and their cones are finite-valence stars, giving the claimed local graph structure. Compactness then reduces such a compact graph to finitely many graph charts; this checks that restricted interpretation, not an identification of every possible noncompact $\mathcal E_1$ convention. This **adds an explicit conditional check** to Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (his p.61 = scan062), which compresses the low-dimensional marginal list. **RESULTS_STATE:** no matching item.

### EC56 — The local two-dimensional triangulation claim

**File/place:** 93/062, first clause of the marginal $\mathcal E_2$ line. **Kind:** unproved claim. **Quote:** “espaces loc. triangulables de dim $\le2$”.

If the compact one-dimensional links have the finite graph interpretation in EC55, their cones have finite simplicial models of dimension at most two, supplying the local triangulations asserted here. This establishes only the local cone-chart implication and does not by itself glue those charts into a global triangulation. It **adds the local/global distinction** to Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), while **restating** its conditional low-dimensional description. **RESULTS_STATE:** no matching item.

### EC57 — The retained compact two-dimensional triangulation claim

**File/place:** 93/062, bracket in the marginal $\mathcal E_2$ line. **Kind:** unproved claim. **Quote:** “ils sont triangulables dans le cas cpt”.

This compact-case assertion is retained in the frozen text, unlike the analogous clause on the following dimension-three line, and needs a global triangulation argument beyond the local cone-chart calculation. No independent proof of that general compact two-dimensional assertion has been completed in this run. This **restates the retained claim but differs in proof status** from Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), which summarizes compact triangulability through dimension three without a proof. **RESULTS_STATE:** no matching item; the neighboring orientation note O06, scans028–030, is not a substitute triangulation theorem.

### EC58 — The retained local three-dimensional triangulation claim

**File/place:** 93/062, first clause of the marginal $\mathcal E_3$ line. **Kind:** unproved claim. **Quote:** “espaces loc. triangulables de dim $\le3$”.

The local statement would follow by coning finite triangulations of the compact two-dimensional links, so it depends on the preceding compact-link issue EC57 under the recursive interpretation. Moise's manifold theorem alone does not verify an assertion about every possibly singular conical link, and the cancelled compact three-dimensional clause remains separately recorded in EC25. This **restates the local claim with an explicit dependency**, absent from Hua's compressed discussion in `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062). **RESULTS_STATE:** no matching item.

### EC59 — The local four-dimensional claim is distinct from the compact question

**File/place:** 93/062, marginal $\mathcal E_4$ line. **Kind:** unproved claim. **Quote:** “esp. loc. $\cdots$ dim $\le4$ (Moïse)”.

Interpreting the ellipsis as local triangulability, this line would require suitable triangulations of compact three-dimensional links; the immediately preceding compact-case claim is deleted, so the dependency cannot simply be declared established on the sheet. The later nontriangulable compact four-manifold in EC26 refutes a global triangulation assertion, not the local manifold charts, and therefore does not by itself refute this local line. This **differs from an unqualified reading** of Hua, `hua_project/93.modern.tex`, V “Espaces localement coniques” (scan062), by preserving that distinction and the unfinished link issue. **RESULTS_STATE:** no matching item.

### EC60 — The compact-comparison axiom label in the provisional proof

**File/place:** 93/058, first paragraph of the proof. **Kind:** reading question. **Quote:** “comme $\overline{R}^n,B^n$ compacts, par b)”.

The deduction from ordinary finite cohomology to compact-support finite cohomology for these compact spaces uses axiom (a), whereas the frozen proof cites (b). Hua, `hua_project/93.modern.tex`, V “Premières conclusions” (scan058), **differs by using (a)** in its corresponding sentence; this is a cross-reference discrepancy separate from the missing compact-support subscript in EC11. **RESULTS_STATE:** no matching item, and no frozen text was changed.

## Typed-sheet census in this range

All six sheets below are `reused_typed` in the frozen inventory. The identifying text is a D.E.S.U.R. administrative discussion of higher-education research policy and funding; no full title or author is supplied. “Addition encoded” means a correction/insertion is represented in the frozen record, **not** that its hand has been authenticated as Grothendieck's.

| Scan | Internal page as frozen | Sections / identifying words | Addition beyond the typescript encoded in the frozen record | Context comparison |
|---:|---|---|---|---|
| 057 | 10. | §5.2 Evaluation de la politique de recherche des établissements; §5.3 La responsabilité de la D.E.S.U.R. | No substantive insertion/deletion/marginal-note element recorded; underlining alone does not authenticate a later hand. | Adds a reused-sheet identification absent from Hua V; compare earlier notes §3 on separating reused texts. |
| 059 | 9. | §4.3 La politique de recherche des établissements; §5 / §5.1 La politique “recherche” de la D.E.S.U.R. | No substantive insertion/deletion/marginal-note element recorded. | Same unidentified administrative text as057, continuing into it. |
| 061 | 8. | 1971–1976 budget table; operating/equipment allocation | Inventory061.03–04: cancelled uncertain middle digit and inserted5 in total354; handwriting attribution unestablished. | Arithmetic checked in EC45; no source attribution supplied by Hua. |
| 063 | `1.\|7.` uncertain | §4 Comment faire de la recherche dans un établissement d'enseignement supérieur; §4.1; §4.2 | No substantive insertion/deletion/marginal-note element recorded. | Content follows065 and leads into061, but order does not resolve the frozen numeral. |
| 065 | 6. | §3.3.1–3.3.4 research objectives: knowledge, research, training, regional activity | Inventory065.08–10: three inserted commas; writer unestablished. | Beginning of063 continues the unfinished final phrase; this is textual continuity, not an attribution. |
| 067 | 5. | §3.2 Les missions d'enseignement et les missions de recherche | Inventory067.09: inserted comma after “chercheurs” in boxed paragraph; writer unestablished. | Precedes065 in internal text order; questions are attributed to the typescript, not automatically to Grothendieck. |

The visible sequence comprises **six supplied sheets**, internally numbered 5,6, uncertain1/7,8,9,10 in textual order; it is not a written declaration that the original document had six or ten pages. The 1976 budget reference belongs to the reused document and does not date the mathematical writing.

## Title sheets and written page counts in this range

| Scan | Exact title/heading evidence | Count or pagination evidence |
|---:|---|---|
| 055 | `$\chi$ et $\chi_!$` | A cover/title only; no written page total. |
| 057/059/061/063/065/067 | Administrative section headings listed above | Printed/typewritten internal page numerals, not Grothendieck manuscript page numbers; no original total declared. |
| 058 | “Conclusions provisoires” | An internal mathematical heading, not a new title sheet or a page count. |
| 068 | Theme list ending “Conj. de Weil” | No title-sheet page total. |
| 069 | Doubt-marked short heading alongside names | Cover classification; heading unresolved; no written total. |
| 070 | Address on the reverse cover | No mathematical title or page count. |
| 083 | Loop-space/Postnikov formulas | No title or written total. |

No “19 pages” or “Pages 1–67” type total appears in these frozen pages. The archival foliation comments are excluded from manuscript pagination.

## Authorial self-flags, qualifications, and withdrawals

Reader uncertainty macros are not counted as authorial doubt. In particular, doubtful letters in a macro do not create an authorial question where the sheet has no question mark.

| Scan | Exact recorded words/mark | What remains open or qualified | Notes |
|---:|---|---|---|
| 058 | “Conclusions provisoires” | The section is explicitly provisional; this is a general qualification rather than a question attached to each example. | EC10–12 |
| 060 | Doubt-marked “cum\|avec” / “léger” followed by “grain de sel” | The initial fibration formula is qualified; preserve uncertainty in the precise marginal wording. | EC15 |
| 060 | “sous réserve” | Finite total dimension of the spectral-sequence terms. | EC16 |
| 060 | “Il faut prouver” | Finite-rank local-system Euler lemma. | EC17 |
| 060 | “Marche tout au moins” | Proof established only under the finite-filtration condition then given. | EC17–18 |
| 062 | “Cela marche pourvu qu'on fasse l'hyp.” | Ordinary version requires the extra homotopy/cover hypothesis. | EC19–20 |
| 062 | “il n'est pas clair qu'ils sont triangulables” | Compact global triangulability in the higher-dimensional marginal discussion. | EC25–26 |
| 064 | “On vérifie” and marginal “vérifier” | Membership of the truncated core and its homotopy equivalence with the punctured compactification. | EC29–30 |
| 066 | “j'ignore si c'est vrai sans telle restriction” | Removing the relative-polyhedral base restriction in the final fibration theorem. | EC37 |
| 066 | “j'ignore si ... caractérisés par a) à e) sur tout $\mathcal E_\infty$” | Global axiomatic uniqueness. | EC38–39 |
| 083 | Actual `?` above `=0` | Group-vanishing versus class-vanishing reading, and possible successive deloopings. | EC47–53 |

Withdrawals with mathematical or interpretive significance are separately recorded at056 (cohomology convention; domination wording),060 (finite filtration replacing triangulability),062 (homology index and cancelled compact triangulation clause), and060→066 (restriction of the initial fibration statement). No result is labelled refuted merely because a word was deleted.

## Reproducible checks and proof details

### EC21: the telescope counterexample

Take finite real projective spaces with their standard compatible CW structures and form the telescope of the inclusions $\mathbb{RP}^n\to\mathbb{RP}^{n+1}$ for $n\ge2$. A compact subset lies in a bounded-height segment of this telescope; each bounded segment is built from finitely many compact mapping cylinders, so the resulting CW space is locally compact. The compatible antipodal covers give a two-sheeted cover $X\to Y$ with $X=\operatorname{Tel}(S^n)$.

Every map of a finite-dimensional sphere into $X$ is homotopic into a finite telescope segment and then into a sufficiently high-dimensional sphere, where it is null-homotopic; thus $X$ is weakly contractible and, being a CW complex, contractible. The same argument identifies $Y$ as a $K(C_2,1)$, and its rational cellular or group homology is $\mathbb Q$ in degree0 and zero otherwise. Consequently the ordinary Euler numbers of $X$ and $Y$ both exist and equal1, although the fibre has Euler number2.

For the sign local system, the standard periodic $\mathbb Q[C_2]$ resolution alternates the operators $g-1=-2$ and $1+g=0$. Its cochain complex is acyclic, including degree0, so the twisted Euler number is0. This is an independent elementary calculation of the particular countermodel; it uses standard telescope/CW facts documented by Hatcher [EUL-S1] and is not a counterexample inside the finite conical-at-infinity class.

### EC52: a free quadratic module and its cocycle

Write the groups additively and set

\[
M=\mathbb Z,\qquad L=\mathbb Z\oplus\mathbb Z/4,
\qquad \partial(m,b)=2m,\qquad w(x,y)=(0,xy\bmod4).
\]

The reduced quadratic-module identities are immediate: $\partial w=0$ since $M$ is abelian; $w(\partial(m,b),x)+w(x,\partial(m,b))=(0,4mx)=0$; and $w(2m,2n)=(0,4mn)=0$, matching the zero commutator in $L$. The induced crossed-module action is

\[
(m,b)^x=(m,b+2mx\bmod4).
\]

It has $\pi_1=\operatorname{coker}\partial=C_2$ and $\pi_2=\ker\partial=C_4$, with trivial induced action on $\pi_2$. Choose the section $s(0)=0,s(1)=1$ of $\mathbb Z\to C_2$ and the lift $v(1,1)=(1,0)$ of its carry2, with the other normalized values zero. The standard crossed-module associator gives

\[
k(a,b,c)=s(a)\cdot v(b,c)-v(a+b,c)+v(a,b+c)-v(a,b),
\qquad k(1,1,1)=(0,2).
\]

All sums in the arguments are in $C_2$. A normalized two-cochain on $C_2$ with trivial coefficients in $C_4$ is determined by $f(1,1)$, and its coboundary at $(1,1,1)$ is always zero; the displayed nonzero class therefore cannot be a coboundary. Its cocycle equation at $(1,1,1,1)$ is $2+2=0\bmod4$, and all normalized equations are checked by `scripts/check_euler_postnikov.py`.

For a finite certificate, quotient to $M=C_4$, $L=C_8$, $\partial a=2a\bmod4$, $w(x,y)=2xy\bmod8$, and $a^x=a+4ax\bmod8$. The morphism from the free model sends $x\mapsto x\bmod4$ and $(m,b)\mapsto m+2b\bmod8$, inducing the same kernel and cokernel; the script exhausts the finite reduced-quadratic and crossed-module identities and the normalized cochain calculations. The separate **topological realization** is the theorem used from Baues–Conduché [EUL-S5, §§4.5–4.7], whose hypotheses match this reduced quadratic module; the script does not prove that theorem.

The stable quadratic-module identity fails because $w(1,1)+w(1,1)=(0,2)\ne0$. This algebraic distinction is consistent with the extra double-delooping requirement in EC51 and is not a newly claimed classification theorem.

### EC49: the ambient cohomology group

With trivial coefficients $C_2$, a normalized three-cochain on $C_2$ is determined by its value on $(1,1,1)$. Both values0 and1 satisfy the cocycle equation, and every normalized two-coboundary vanishes there, giving $H^3(C_2;C_2)=C_2$. The product $K(C_2,1)\times K(C_2,2)$ has zero Postnikov class by construction and admits repeated Eilenberg–MacLane deloopings, so the nonzero ambient group persists even in the strongest delooping example used here.

### EC39: exact scope of the modern uniqueness route

The deduction is conditional on interpreting the compact conical hierarchy as compact Hausdorff spaces with the usual finite recursive cone neighborhoods. Induction then yields metrizable finite-dimensional cone charts, and compactness gives a finite chart cover; shrinking a cone chart contracts it at its vertex, producing local contractibility. With the standard ANR criterion supplied, West gives finite CW homotopy models for compact members; radial truncation yields a compact core whose boundary neighborhoods are products with a half-interval, to which the same ANR argument applies. The first five Euler axioms therefore determine the values on the finite models, then on $X$ by homotopy invariance, and finally on $X$ with compact supports by deleting the compactification point.

This checks the logical reduction and distinguishes homotopy finiteness from actual triangulability. It is **not** a proof that every possible reading of the manuscript's $\mathcal E/\mathcal C$ notation satisfies those hypotheses, nor an independent re-proof of the ANR criterion or West's theorem. Similarly, extending the compact-support fibration formula would require a compatible local-system/excision argument on the truncated core; this report does not announce that extension as established.

## Primary-source register

No web text is used to repair a frozen reading. All external comparisons below are mathematical source comparisons; the independent computations are distinguished above.

| ID | Primary/author source and exact location used | URL |
|---|---|---|
| EUL-S1 | Allen Hatcher, *Algebraic Topology*, author-hosted text: §2.2/§3.1 Mayer–Vietoris; §3F mapping telescopes; §3H local coefficients. | [https://pi.math.cornell.edu/~hatcher/AT/AT.pdf](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) |
| EUL-S2 | James E. West, *Mapping Hilbert cube manifolds to ANR's: A solution of a conjecture of Borsuk*, Annals 106 (1977), 1–18, Corollary 5.3; metric/local-compactness convention on p.2. | [https://webhomes.maths.ed.ac.uk/~v1ranick/papers/west.pdf](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/west.pdf) |
| EUL-S3 | Ciprian Manolescu, *Lectures on the triangulation conjecture*, §2.2; distinguishes dimension-three Moise from dimension-four Casson/$E_8$. | [https://web.stanford.edu/~cm5/Gokova.pdf](https://web.stanford.edu/~cm5/Gokova.pdf) |
| EUL-S4 | Dominique Arlettaz, *Algebraic K-theory of rings from a topological viewpoint*, Publicacions Matemàtiques 44 (2000), §7, Lemma 7.4, Proposition 7.5, Theorem 7.6. | [https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v44(1)/FileName:44100_01.pdf](https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v44(1)/FileName:44100_01.pdf) |
| EUL-S5 | Hans-Joachim Baues and Daniel Conduché, *On the 2-type of an iterated loop space*, MPI 95-112: §§4.1–4.7, §5.3; Theorem 1.9 for the naturality caution. | [https://archive.mpim-bonn.mpg.de/id/eprint/624/1/preprint_1995_112.pdf](https://archive.mpim-bonn.mpg.de/id/eprint/624/1/preprint_1995_112.pdf) |

The original Arlettaz paper is cited bibliographically by the primary sources as *The first k-invariant of a double loop space is trivial*, Arch. Math.54 (1990), 84–92, DOI10.1007/BF01190672; its DOI target was inaccessible in this run, so the checked theorem/proof comparison uses the accessible author survey instead. Moise's original article metadata is *Affine Structures in 3-Manifolds: V. The Triangulation Theorem and Hauptvermutung*, Annals56 (1952), 96–114, DOI10.2307/1969769; its full text was not retrieved, so no claim of checking that original proof is made.
