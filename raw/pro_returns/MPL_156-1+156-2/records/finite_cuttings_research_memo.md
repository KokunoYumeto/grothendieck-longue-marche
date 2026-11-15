# Research memo: finite cuttings, pro-objects, and comparison literature

This memo was reconstructed from the preserved research analysis after the execution environment reset. Research was performed after the transcription freeze; no scan image was viewed and no transcription, inventory, or doubts file was changed. Manuscript references refer to the frozen transcription; the context consists of the supplied `README.md` and `notes/RESULTS_STATE.md`, whose register statuses are prior-run claims unless expressly reviewed there.

## Principal finding

The README's proposed identification of a form with a tame space recovered from a pro-object of finite cuttings is **not a definition or theorem in these 46 scans**. The pages give abstract segment/lieu structures, call a model satisfying the evolving F1–F6 axioms a réseau, develop geometric cutting and gluing of ficelles, and later construct Boolean rives and birives; they do not define a pro-category of cuttings, its bonding maps, cofilteredness, or a reconstruction comparison. This is a negative answer to the proposed reading of this folder, not a proof that no later or independently formulated pro-object reconstruction could exist. The strongest positive evidence is the equivalence between finitely many mutually disjoint cuts and an ordered finite list of actual pieces with actual end homeomorphisms (156-2/008–010).

Context check: `README.md`, “The guess,” states this was a title-based probe, while **WG2 B15 (§1.2)** and **WG2 §3.1 #2** are explicitly unchecked planning items. No result status should be changed on this evidence.

## Manuscript-specific implications

### FC1 — A finite cutting still has geometric coefficients

**Source:** 156-2/008–010, especially the final paragraph of 010. **Kind:** unpursued implication. The words “n+1 ficelles orientées” and “n homeo. de raccordement” show that a chain of cuts comes with its pieces, boundary spaces, and attaching homeomorphisms; forgetting these to an abstract finite chain loses data that the stated equivalence explicitly retains. **Context:** this adds a concrete cutting instance to **MPL_150_044-084 N18** (150/077, 081–084, attachment data), **STRATA C.8** (coherent gluing), and **EXIT_ONE_TYPE P4e** (149/133, coarse maquette does not determine a link), without re-proving or upgrading their register claims.

### FC2 — Directedness requires an additional choice

**Source:** 156-2/009–010. **Kind:** own idea, high confidence for the restricted statement below. A candidate indexing category whose objects are finite chains of literal embedded lieux and whose refinements only add cuts is not automatically directed: two crossing separating arcs in a square give valid one-cut objects that cannot both occur in one pairwise-disjoint chain. **Context:** the README and **WG2 B15 (§1.2)** propose refinement but specify no such category; this identifies a missing choice, not an obstruction to every possible refinement system. A full verification follows below.

### FC3 — Divisibility is not finiteness or completeness

**Source:** 156-1/006, 013–014, 024. **Kind:** unpursued implication / own idea, high confidence for the logical distinction. The manuscript itself records “\(\tilde I^\circ\) est infini” as a consequence of divisibility, and later separates divisible networks from reduced ones, so the initial data are not finite combinatorial data by definition. An additional theorem would be needed to identify these structures with particular tame topological spaces, or recover them from finite approximations; density of an order alone does not give Dedekind completeness or a chosen topology. **Context:** this limits the README conjecture and **WG2 B15 (§1.2)**; no supplied entry states an equivalence between the present F1–F6 structures and such a pro-category.

### FC4 — Finite posets differ from finite discrete spaces

**Source:** 156-2/010, as motivation for an external comparison. **Kind:** unpursued implication. McCord's Theorem 1 shows that finite spaces and finite simplicial complexes can realize the same weak homotopy types, so connectedness or higher homotopy does not rule out finite-poset models (McCord, 1966). **Context:** **STRATA A.4**, **STRATA A.12**, and **BISITE G.10** already concern finite-poset realization and exits; the present pages add possible geometric input but do not give a functor satisfying those hypotheses. Their “Proved” labels are register claims, not independently rechecked results in this memo.

### FC5 — A literal topological inverse limit requires care

**Source:** 156-2/008–010 and the README conjecture. **Kind:** own explanatory deduction, high confidence under the stated interpretation. A directed inverse limit of finite T0 spaces is spectral, and if that limit is Hausdorff its compact-open basis consists of clopen sets; therefore a nontrivial connected Hausdorff space is not literally such a topological inverse limit (Stacks Project, Tag 09XV). This leaves untouched reconstruction by a quotient, a maximal-point subspace, a homotopy equivalence, or a pro-object with another realization functor. **Context:** this qualifies the README / **WG2 B15 (§1.2)** and is separate from the recorded finite-poset homotopy comparisons.

### FC6 — A genuine inverse-limit bridge has a different conclusion

**Source:** 156-2/010, as an external comparison. **Kind:** own idea, medium confidence for its usefulness here; the theorem itself is established literature. Clader's Theorem 1.1 constructs, for a finite simplicial complex, an inverse sequence of finite spaces whose limit is homotopy equivalent to the complex, with a quotient homeomorphic to its realization; the published erratum repairs the continuity proof and leaves the statements unchanged (Clader, 2009, 2016). This helps state exactly which reconstruction conclusion is desired, but it uses barycentric face-poset models rather than this manuscript's cutting category. **Context:** it supplies an external comparison for the README without replacing **STRATA A.4/A.12** or claiming that their register results settle a cutting construction.

### FC7 — Simple homotopy is a comparison target, not an established bridge

**Source:** 156-1/024–026 and 156-2/008–010. **Kind:** own idea, medium confidence. Barmak and Minian's Theorem 3.10 and Corollary 3.11 identify simple equivalence classes of finite T0 spaces with simple homotopy types of finite simplicial complexes, giving a precise setting for testing an eventual finite model of a cutting (Barmak & Minian, 2008). One must first define that model and prove the manuscript's permitted changes induce the required simple equivalences. **Context:** this offers a literature route for the README's proposed connection to *Les Dérivateurs* XVI ms. 87–96; the supplied context does not provide that comparison functor.

### FC8 — Retaining links is the relevant modern lesson

**Source:** 156-2/002–003, 012–014 and 008–010. **Kind:** unpursued implication / literature comparison. Conic links, restrictions on their topological type, and end-gluing maps suggest comparison with a stratified homotopy construction retaining link data. Ayala, Francis, and Rozenblyum identify exit morphism spaces using links and obtain a fully faithful exit functor for their conically smooth stratified homotopy theory; those hypotheses and the enriched conclusion are additional structure, not consequences of these pages (Ayala et al., 2019; author manuscript, Lemma 3.3.5 and Theorem 4.2.5). **Context:** this restates the caution behind **EXIT_ONE_TYPE P1a1**, **P1b1**, **P4e**, **STRATA F.3**, and **MPL_150_044-084 N39**, while adding explicit ficelle/cutting source locations.

### FC9 — General finite categories require a separate argument

**Source:** 156-2/008–010. **Kind:** own idea, medium confidence as a programmatic warning. A category of geometric cutting data is not thereby a finite category, and replacing an order by a category with arbitrary endomorphisms changes the problem. **Context:** **RESIDUE H.2** records an obstruction to an unmodified finite-poset realization assertion for finite categories with nonidentity idempotents, **STRATA B.1** records an EI criterion, and **PATHS D.13** records a rectification failure; these pages provide no hypotheses overcoming those recorded obstructions. The next question is which finite categories, morphisms, and realization equivalences are intended.

## Verified crossing-cut construction in a square

This is an independent compact polyhedral example, not a correction to manuscript text.

Let \(I=[0,1]\), \(X=I\times I\), \(A=\{0\}\times I\), and \(B=\{1\}\times I\). These are disjoint nonempty closed non-open sets. Both \(X\setminus A\) and \(X\setminus B\) are path connected, so their indicated quotients in Fic c) are connected. A closed collar \([0,\delta]\times I\) of \(A\), with \(A\) collapsed, is the closed cone on \(I\); removing its base gives an open subset of \(X/A\). The same holds at \(B\), verifying regular immersion in the exact conic-quotient sense of 156-2/002. Thus this is a ficelle under Fic a)–d).

For \(C=\{1/2\}\times I\), the complement has connected pieces \([0,1/2)\times I\) and \((1/2,1]\times I\), containing \(A\) and \(B\) respectively, and the corresponding quotients by those ends are connected. The closed strip \([1/2-\delta,1/2+\delta]\times I\), with \(C\) collapsed, is the closed cone on \(I\amalg I\). An explicit quotient homeomorphism sends \((t,\sigma,r)\), with \(t\in I\), \(\sigma\in\{-1,+1\}\), \(r\in[0,1]\), to \((1/2+\sigma\delta r,t)\), identifying all points with \(r=0\). The two outer sides are the base and their removal is open in \(X/C\). The closures of the two complementary pieces are rectangles with the same end-collar property, so the component ficelles and Li c) are verified.

For \(0<\varepsilon<1\), set \(f(t)=1/2+\varepsilon(t-1/2)\) and \(D=\{(f(t),t):t\in I\}\). A homeomorphism preserving the second coordinate and fixing \(A,B\) pointwise is

\[
h_f(x,t)_1=\begin{cases}
2f(t)x,&0\le x\le1/2,\\
f(t)+2(1-f(t))(x-1/2),&1/2\le x\le1.
\end{cases}
\]

It sends \(C\) to \(D\), transporting every verified property. Yet \(C\cap D=\{(1/2,1/2)\}\), so they cannot belong to one chain of mutually disjoint cuts. Their union has four complementary regions, rather than the two required for a lieu.

**Exact conclusion:** the poset of finite mutually compatible collections of literal embedded cuts, ordered by retaining old cuts and adding new ones, has no common upper bound for \(\{C\}\) and \(\{D\}\). This is a failure for this indexing choice, not for constructions allowing isotopy, replacements, subdivisions of crossing pieces, or another class of cuttings.

## A stronger distinction on a circle: set-disjoint cuts need not be compatible

Take \(X=S^1\) with distinct ends \(A=\{a\}\), \(B=\{b\}\). Parametrize each of the two closed \(a\)-to-\(b\) arcs by \([0,1]\), oriented from \(a\) to \(b\). Let \(C\) have coordinate \(1/3\) on the first arc and \(2/3\) on the second, while \(D\) has coordinates \(2/3\) and \(1/3\) respectively. Each is a two-point closed subset whose deletion leaves exactly two connected components, one containing each end. Collapsing such a two-point set in disjoint small closed interval neighborhoods produces the cone on a four-point compact set, so the regular-immersion condition holds. Thus both are lieux; the original circle is a ficelle because deletion of either end is connected and each end has a two-point conic link.

Although \(C\cap D=\varnothing\), one point of \(D\) lies in the \(a\)-side of \(C\) and the other lies in the \(b\)-side. Hence \(D\) is not a lieu in either component ficelle cut along \(C\); the two cuts are not “disjoints” in the manuscript's defined sense and are not comparable in its order. No compatible chain retaining both is possible. This example warns against replacing his defined relation by set-theoretic disjointness.

## Why the literal-limit caution is compatible with McCord and Clader

A finite T0 space is sober: an irreducible closed set is a finite union of closures of its points, hence equals one of them, uniquely by T0. Tag 09XV applies to a directed inverse system of these spaces. If its limit is Hausdorff, each compact open is closed, and its spectral compact-open basis becomes a clopen basis. Therefore the raw limit cannot be a nontrivial connected Hausdorff space. McCord concerns weak homotopy equivalence; Clader's potentially non-Hausdorff limit has a quotient homeomorphic to the polyhedron and a homotopy equivalence. Neither asserts that an arbitrary compact polyhedron is homeomorphic to that raw limit. For finite discrete spaces the stronger classical characterization is Tag 08ZY: profinite spaces are exactly compact Hausdorff totally disconnected spaces.

## Context status and scope

Searches in the supplied context used `pro-object`, `finite cuttings`, `refinement`, `finite poset`, `simple homotopy`, `links`, `recollement`, `incidence`, `normal`, `idempotents`, and `EI`; related entries are named above. The context ZIP supplies an index with abbreviated entries, not the full papers/returns listed in its source section, so this memo does not pretend to have read those missing source files. Older file/scan anchors are reported only when supplied. None of the nine listed open register items is solved; in particular this manuscript does not establish the normal-crossing threefold zigzag required by **EXIT_ONE_TYPE P3c-general**, or the localization and higher-category claims in the other open rows.

## Primary references and verification scope

- Ayala, D., Francis, J., & Rozenblyum, N. (2019). A stratified homotopy hypothesis. *Journal of the European Mathematical Society, 21*(4), 1071–1178. https://doi.org/10.4171/JEMS/856. Publisher metadata: https://ems.press/journals/jems/articles/15935. Inspected author manuscript: https://math.montana.edu/dayala/documents/Striation.pdf, Lemma 3.3.5 and Theorem 4.2.5; numbering is for that version.
- Barmak, J. A., & Minian, E. G. (2008). Simple homotopy types and finite spaces. *Advances in Mathematics, 218*(1), 87–104. https://doi.org/10.1016/j.aim.2007.11.019. Inspected primary PDF: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/barmak3.pdf, Theorem 3.10 and Corollary 3.11. Institutional metadata: https://bibliotecadigital.exactas.uba.ar/greenstone3/exa/collection/paper/document/paper_00018708_v218_n1_p87_Barmak.
- Clader, E. (2009). Inverse limits of finite topological spaces. *Homology, Homotopy and Applications, 11*(2), 223–227. https://doi.org/10.4310/HHA.2009.v11.n2.a11. Inspected primary PDF: https://math.uchicago.edu/~may/FINITE/OtherUndergradPapers/CladerToo.pdf, Theorem 1.1 and §§2–3; use with the erratum.
- Clader, E. (2016). Erratum to “Inverse limits of finite topological spaces.” *Homology, Homotopy and Applications, 18*(1), 25–26. https://doi.org/10.4310/HHA.2016.v18.n1.a2. Inspected publisher PDF: https://www.intlpress.com/site/pub/files/_fulltext/journals/hha/2016/0018/0001/HHA-2016-0018-0001-a002.pdf.
- McCord, M. C. (1966). Singular homology groups and homotopy groups of finite topological spaces. *Duke Mathematical Journal, 33*(3), 465–474. https://doi.org/10.1215/S0012-7094-66-03352-7. Inspected primary PDF: https://www.maths.ed.ac.uk/~v1ranick/papers/mccord1.pdf, Theorems 1–4.
- The Stacks Project Authors. (n.d.). *Profinite spaces*, Lemma 5.22.2 (Tag 08ZY). Retrieved November 14, 2026, from https://stacks.math.columbia.edu/tag/08ZY.
- The Stacks Project Authors. (n.d.). *Spectral spaces*, Lemma 5.23.12 (Tag 09XV). Retrieved November 14, 2026, from https://stacks.math.columbia.edu/tag/09XV.

### Additional source checked for the reconstructed P section

- Grothendieck, A. (1997). Esquisse d'un Programme. In L. Schneps & P. Lochak (Eds.), *Geometric Galois actions 1: Around Grothendieck's Esquisse d'un Programme* (London Mathematical Society Lecture Note Series, Vol. 242, pp. 7–48). Cambridge University Press. https://doi.org/10.1017/CBO9780511758874.003. French text inspected: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf, §5, printed pp. 25–27 and 31–32, and §6, printed pp. 34–35. The comparison used below is the retention of geometric attaching maps and isotopy/higher-isotopy data, not a claim that the Esquisse gives the present folder's missing definition of a pro-object or workshop.

### Bibliographic leads not needed for the conclusions

- Artin, M., & Mazur, B. (1969). *Etale homotopy* (Lecture Notes in Mathematics, Vol. 100). Springer. https://doi.org/10.1007/BFb0080957. Only publisher metadata and contents were inspected; no detailed theorem is relied on here.
- Sorkin, R. D. (1991). Finitary substitute for continuous topology. *International Journal of Theoretical Physics, 30*, 923–947. https://doi.org/10.1007/BF00673986. Only publisher abstract and metadata were inspected; it is a later comparison, not evidence of influence on June 1986, and no exact reconstruction theorem from it is used.
