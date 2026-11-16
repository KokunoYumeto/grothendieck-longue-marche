# Part D / E.2 source and computation log

AI-produced research notes by GPT-6 Astra. No priority is claimed. Checked 16 November 2026.

## Primary sources opened

| Source | Exact material checked | Use / limit |
|---|---|---|
| Epstein (1966), *Curves on 2-manifolds and isotopies*, Acta Mathematica 115, 83–107, DOI 10.1007/BF02392203 | Full primary PDF; Theorem 6.4(b), printed pp.101–103; Appendix A4; definition of ambient isotopy. Warwick author repository metadata also opened. | The based homotopy-to-isotopy implication applies to noncompact surfaces without boundary; local orientation qualification for the open Möbius band checked. Supplies compact-open isotopy, not the required uniform tail. |
| Yagasaki (2000), *Homotopy types of homeomorphism groups of noncompact 2-manifolds*, Topology Appl.108(2),123–136, DOI 10.1016/S0166-8641(99)00130-3; arXiv:math/0010223 | Theorem1.1; Lemma2.1(i)–(ii) and proof; Theorem2.1/Corollary2.1. | Compact pointed aspherical surface groups contractible. Pointed plane is an S1 exception in the interior compact-open topology. Cannot transfer a noncompact contraction without tail control. |
| Yagasaki (2014), *Groups of uniform homeomorphisms of covering spaces*, JMSJ66(4),1227–1248, DOI10.2969/jmsj/06641227 | Published PDF, Theorem1.1, Corollary1.1, Theorem1.2, Definition2.1, proof's finite cover and uniform constants. | Compact base is explicit; Euclidean-end theorem has additional geometric hypotheses. Not an arbitrary-noncompact-base theorem. |
| Yagasaki (2018), *Local and end deformation theorems for uniform embeddings*, Topology Appl.239,191–225; arXiv:1301.3265v3 (2014) | Primary v3, introduction, Theorems1.1–1.3 and proper product-end hypotheses. Publication metadata in author's publication listing. | Theorem1.3 requires finitely many isolated proper product ends satisfying ED. The bounded metric d_Q need not be a proper end metric. Numbering cited follows v3. Publisher full text returned403. |
| Wengenroth (2025), *Effros' theorem on transitive group actions with a glimpse into descriptive set theory*, arXiv2512.00910v1 | Theorem4.1 and proof. | Gives open orbit maps for the Polish transitive action used in D.1. Original Effros paper not separately treated as opened. |
| Kerckhoff (1983), *The Nielsen realization problem*, Ann.Math117(2),235–265, DOI10.2307/2007076 | Primary PDF, Theorem5, §IV printed pp.255–256, especially cusps and orientation reversal. | Applies to finite subgroups of the extended five-puncture mapping class group. General Fuchsian extension is explicit, not inferred from closed genus≥2 theorem alone. |
| Stukow (2004), *Conjugacy classes of finite subgroups of certain mapping class groups*, Turk.J.Math28(2),101–110 | Primary arXivmath/0510214 text, Theorems3–4; publisher article metadata opened. | Independent check of seven orientation-preserving classes at five punctures. Does not classify the thirteen negative classes; those are proved separately. ArXiv posting is2005, publication2004. Publisher PDF403; preprint available. |
| Grothendieck, cote148, *Teichmüller (1983): notes manuscrites* | Original official Montpellier PDF downloaded, scans31–36 rendered, scans31,33,34,35,36 directly viewed; scan33 top rendered at300dpi. | Authority for manuscript readings. Supplied AI transcription not authority. |

Primary URLs are in references_DE.bib. The root agent must open web sources itself if it wishes to use web-reference tokens in chat. Useful tool refs available in this run: Epstein turn52view1/turn53view2; Yagasaki2000 turn52view0; Yagasaki2014 turn75view2; Yagasaki2018 turn58view0; Effros proof turn75view1; Kerckhoff turn52view2/turn58view1; Stukow turn75view0/turn77view0; Epstein metadata turn77view1. These IDs are not bibliographic references.

## Original manuscript audit

Official catalogue: https://grothendieck.umontpellier.fr/archives-grothendieck/
Official PDF: https://grothendieck.umontpellier.fr/148.pdf
Catalogue date1983,71 archival pages. PDF has72 pages including its cover.
Downloaded length35,287,128 bytes; SHA-256:
`e3c3052ebd840bed807f22192753c4853bc400d28ed9ab3afb066cecc3ebf599`.
Original is outside the deliverable tree at `/workspace/scratch/a50d05093ca1/sources/MPL_148_original.pdf`.

| PDF scan (one-based) | Printed archival page | Handwritten classification page | Audit |
|---:|---:|---:|---|
|31|30|—|Nine vertex families and local arrow degrees; total542. I4 is an oriented-square object.|
|32|31|—|Geometric sketches; no additional numerical assertion needed for census.|
|33|32|—|1620 total; lower family is written3×120; overwritten intermediate products remain awkward; word “orbites” following14 is visibly crossed out.|
|34|33|1|Holomorphic ν5,4,3 classification read directly.|
|35|34|2|ν2 calculation crossed out; square/tetrahedron discussion; false anti-order2 inference is uncancelled and clear.|
|36|35|3|Real-involution types1,3,5 and dimensions2; square-pyramid example; stable-tree counts1,10,15; decorated counts12,60,120,60,30,20.|

The supplied transcription assigns archival pages one smaller than the actual printed archival pages in this range. Its scan numbers are correct. The report must not turn the struck-out “orbites” into an unqualified assertion of14 orbits. Fourteen named families and sixteen S5-orbits give the consistent diagram census. The actual original order-two inference is refuted by explicit order6 and10 maps.

## Exact computations

1. `check_census.py`, standard library only. Executed with Python3. It constructs nine S5 coset sets, computes542 and nine orbits, models14 arrow families with1620 elements and16 orbits, constructs20 finite signed-permutation action models, checks their pairwise S5-conjugacy inequivalence, and checks exact orders6 and10 of the anti-Möbius examples. Output: `check_census.out`; structured data: `census_computation.json`, `census_finite_actions.csv`, `census_arrow_families.csv`.
2. `check_special_configurations.py`, SymPy1.14.0. For each of six exact algebraic five-sets, enumerates all60 possible images of an ordered triple, then verifies the remaining marks for both holomorphic and antiholomorphic candidates. Checks β values17/4,−2,−10/3,18,34,−14; positive orders2,4,6,10,2,2; all negative orders and involution fixed-mark counts. Checks harmonic factorization exactly. Output `check_special_configurations.out`; data `special_configurations.json`.

The finite incidence model certifies counts and stabilizers; it is not claimed to compute relations among geometric Teichmüller-groupoid arrows. No floating-point check is used.

## Search record relevant to the open uniform-tail line

Routine engine2 and stronger engine1 searches used combinations of “uniform homeomorphism groups surfaces vanishing displacement infinity contractible”, “equivariant disk centralizer discrete group contractible boundary fixed”, “Yagasaki Local and end deformation uniform”, and “homeomorphisms vanishing displacement group topology surface”. Located the2014 and2018 primary deformation theorems, the Whitney-topology work, and Černavskiĭ's majorant-topology theorem. The Whitney and majorant results do not have the topology required here. No novelty claim is made, and failure to locate a theorem is not treated as proof of openness in the literature.

## Items excluded or superseded in assembly

The files `C_12_source.txt`, `C_81_source.txt`, `C_88_source.txt`, `C_90_source.txt`, `C_91_source.txt`, `C_92_source.txt`, `B_4_source.txt`, `B_5_source.txt`, `B_26_source.txt` are copied excerpts of user attachments used for working reference. They should be omitted from checkpoints/final as duplicate attached source material; their independent audits are in section_D.tex and section_E2.tex. The scan PNGs and catalogue HTML are newly retrieved primary-source evidence; they can be retained as audit records or the report can name their omission if size requires it. The original35MB PDF need not be included when its authoritative URL, hash and audit crops are retained.

## Later controlled-topology lemma

D.13 is an independent planar argument: after a uniformly equivalent Euclidean disk metric, q Fill(A)=Fill(qA)⊂conv(qA), so filling hulls do not increase d_Q diameter. Each ball component is simply connected. A further approach replaces d_Q by the inner-diameter (Mazurkiewicz) metric: a based compact path family has uniform tails in this stronger metric because its own trajectories are small connected carriers. No theorem transferring a full controlled ambient isotopy to this setting has yet been verified. Searches for controlled equivariant isotopy and uniform contractibility returned compact-base and majorant-topology results, with the same hypothesis gap.

D.14 now proves this metric replacement precisely for compact connected locally path connected metric parameter spaces, and hence for every based positive homotopy group. Its disk-neighborhood form is Bρ(u,r) ⊂ U(u,r) ⊂ Bρ(u,2r), with U an open disk. This controls carriers, but does not make a continuous equivariant choice of ambient extension.

Additional primary sources opened while pursuing this step:

- Burago, Lu, and Ozuch, *How large isotopy is needed to connect homotopic diffeomorphisms (of T²)*, author's primary PDF https://www.mv.helsinki.fi/home/jinpeng/Burago-Lu-Ozuch.pdf (tool turn96view0), Main Theorem on PDF p.2 and discussion p.3. The theorem controls higher Hölder norms for diffeomorphisms of the compact flat torus; it does not establish the C₀ displacement control needed here. Publication metadata: Journal of Topology and Analysis12(4),1213–1222 (2020), DOI10.1142/S1793525320500028. No use as a proof of D.9.
- Černavskiĭ, *Local contractibility of the group of homeomorphisms of a manifold*, Math.USSR Sbornik8(3),287–333 (1969), primary translation PDF https://www.maths.gla.ac.uk/~mpowell/Cernavskii%20local%20contractibility.pdf (turn96view1), introduction and §§1.1–1.6. The text itself distinguishes compact-open, uniform, and majorant topologies and warns that ordinary layer isotopies need not be paths for the latter two. It is not a blanket theorem for this uniform subgroup.
- Hamstrom, *Homotopy in homeomorphism spaces, TOP and PL*, Bull.AMS80(2),207–230 (1974), primary PDF https://www.maths.gla.ac.uk/~mpowell/Hamstrom%20homotopy%20in%20homeomorphism%20spaces.pdf (turn96view2), §§0.1–0.2. The standing manifold convention is compact unless otherwise specified. The compact surface local-contractibility results surveyed here cannot silently be transferred.

The Le Roux Brouwer-homeomorphism papers were located in publisher search text; direct full-text requests returned403. The translation centralizer statement found there explicitly uses compact-open topology. It supplies no verified uniform-tail extension. Searches also tried “uniform Schoenflies”, “controlled Schoenflies”, “centralizer Brouwer homeomorphism contractible”, and “homeomorphism group vanishing at infinity”. These searches are recorded as attempted routes, not as evidence that the exact statement is unknown in the literature.
