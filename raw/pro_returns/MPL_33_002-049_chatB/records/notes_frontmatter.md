# Research notes — MPL_33_002-049

## I. Scope, sources, and evidentiary status

These notes concern **cote 33, scans 002–049**, all 48 supplied scan pages. The manuscript source is the diplomatic transcription in this package: 48 individual page files and their combined fragment, frozen at **2026-11-15 13:20:32 UTC**, before the context archive was opened. The root reader personally completed the ordered visual transcription, cross-page notation check, and second visual audit; research assistance began only after the freeze. No image was subjected to OCR. The final progress log records verification of the same 49 SHA-256 hashes.

Line references below identify the **exact lines of the individual frozen `.tex` page files**, providing stable locators even where paragraphs have been joined or diagrams occupy several code lines. They are not claimed to be physical manuscript line numbers. Short quotations reproduce the source’s wording; a quoted doubtful reading is still doubtful, and mathematical symbols used in an analysis are not alternative transcriptions. In particular, the recurrent local-class glyph remains `\unsure{\gamma|\sigma}` in the source, even where the research discussion refers generically to “the class.”

The foreground handwritten sequence develops étale sites and base change, analytic comparison, purity, compact support, local fundamental classes, geometric trace, and derived duality. It substantially confirms the supplied README’s **SGA 4/5 and S19 draft-to-print comparison** placement. These particular leaves do not present a developed SGA 7 monodromy argument, nor do the reused root-system, formal-group, sheafification, or commutative-algebra sheets become parts of that handwritten programme merely by sharing a cote. Their authorship and source identity are assessed separately.

The research notes distinguish a statement left unproved on a sheet from a currently open mathematical problem. Several literal readings admit concrete scope tests: unrestricted nonproper analytic comparison (N37), fixed-ring freeness in proper smooth specialization (N38), unqualified ordinary connectedness in the trace statement (N31), a stronger interpretation of the partial-range duality ending (N50), and the reused product-stalk Hom assertion (N68). These calculations claim no historical priority or novelty; their hypotheses and their limits are part of each item. Cancellation is treated as documentary withdrawal of a written presentation unless the source actually retracts the mathematical assertion.

### Supplied context and search method

All three supplied documents were read after the freeze:

- `README.md`: preliminary placement, standing questions, and S19 comparison plan. Its initial “Only this README” description is superseded by its dated additions listing the two further files.
- `notes/RESULTS_STATE.md`: the register of claims, open items, intake readings, and planning hunches.
- `same_cote_33/MPL_33_098-146_notes.md`: first-pass, unreviewed research leads for later scans of this same cote.

Every numbered research item was searched separately against all three files using literal alternatives with `rg -n -i -F`. The reproducible queries, matching lines, and manually assessed relationships are in `records/research_context_searches.json`; a word match alone is never treated as a mathematical match. Each item states its corresponding file and scan, or explicitly states that there is no same-point match. References to a neighboring note such as “N25” are always qualified by the package name when they could be confused with the present note numbering.

The supplied register’s statuses remain **the earlier runs’ claims**, except for the specifically named referee-reviewed entries. Its general referee paragraph does not upgrade every row: in particular, it does not mark LM7_PUSH C.6 reviewed. The complete underlying LM results and the other packages named in the register were not supplied; truncated register excerpts are not silently expanded into full theorems. No earlier example is re-derived merely because it can be repeated: the new tests identify what the present scans add.

### Disposition of every supplied results-register entry

| Register ID | Supplied status / source locus | Relationship of these scans |
|---|---|---|
| **LM7 E.23** | Open run claim; §51.16, folios733v–736v, scans172–178 in its cited source; cote not specified in this excerpt | No section-map calculation for geometric metabelian or marked depth-two quotients of $U_3/\mathbb Q$ occurs here. The Galois-action example on002 and formal-group sheet009 do not advance this open item. |
| **LM4 D.12** | Open run claim; locator “25 bis,” folios157v–160, scans312–317; locator “30,” folio194v, scan384; these are not identified as archive cotes in the supplied excerpt | Finite Coxeter/Weyl groups on the reused leaves are different objects from full profinite $GT_0$ or low-type mapping-class torsion. No bearing on the open conjugacy question is established. |
| **LM4 F.7** | Open run claim; §30, folios194–196, scans383–387 | The reused root-system automorphism calculations do not supply the nonsolvable $A_5$ centralizer/completion comparison. No status change. |
| **LM7_PUSH C.6** | Proved run claim; locatorC.3; not among the explicitly referee-reviewed IDs | No class-two germ/residue-complex argument appears here. Formal-group vocabulary on009 does not identify its bracket computation with this arithmetic classification. |
| **INTAKE LM7_CONTINUED §?** | Intake reading, explicitly not a referee verdict; E.23-related rows includingE.37 | No new integrality, residue, or fiber calculation for that section map is supplied by002–049. |
| **MPL_33_098-146 §1** | First-pass scope/source observation, scans098–146 | Current source separation and the title/pagination inventory add an earlier 48-scan block; see N52, N64, N74, N79 and sectionVIII. |
| **MPL_33_098-146 §3** | First-pass register-disposition method | The present table restates its evidentiary discipline and adds the current scan-specific negative and positive dispositions. |
| **MPL_33_098-146 §65** | First-pass self-flagged-step index, scans098–146 | SectionVII adds the actual doubts, promises, conditions, and editorial tasks in002–049. Their existence does not prove the later steps. |
| **MPL_33_098-146 §76** | First-pass S19 comparison map, chiefly100–146 | SectionIX adds analytic comparison, purity, geometric trace, early derived constructions, and separate reused-source comparison targets. |
| **MPL_33_098-146 §78** | First-pass verified-Stacks-locator list | The present bibliography and comparison map supply independently inspected additional locators. The earlier list is a retrieval lead, not borrowed verification. |
| **MPL_33_098-146 N01** | First-pass exchange/duality lead, scan098 | N12, N26, N33, N46 and N83 add support, purity and geometric-trace antecedents; no claim that the later exchange proof is completed. |
| **MPL_33_098-146 N08** | First-pass finite-ring/unbounded-resolution lead, scans108/112 | N40–N43 and N48 distinguish flatness, resolution choices, exact finite-ring duality, and perfectness. Its finite-ring infinite-Tor example is not repeated. |
| **MPL_33_098-146 N15** | First-pass nonproper Künneth expectation, scan118 | N04 and N17–N18 add base-change and constructibility coefficient restrictions; the punctured-curve Artin–Schreier test is a different construction from the earlier mixed-plane example. |
| **MPL_33_098-146 N20** | First-pass curve/L-function expectation, scan122 | N01, N15 and N27 add the opening programme, the resolution/purity problem, and curve point-class normalization. They do not prove the later resolution-free expectation. |
| **MPL_33_098-146 N21** | First-pass priority-of-formalism observation, scan122 | N01 restates that priority and adds the explicit three-part programme on002. Scan order alone does not date the sheets. |
| **MPL_33_098-146 N23** | First-pass integral-coefficient objective, scan126 | N14, N24, N38 and N48 add twists, geometric compatibility, a nonfree geometric cohomology example, and exact duality over $\mathbb Z/n$. |
| **MPL_33_098-146 N25** | First-pass perfect-complex/nonprojective-cohomology example, scans126–132 | N38 adds a proper smooth sign-local-system example; N48 explains why nonprojectivity does not obstruct this particular coefficient duality. The earlier two-term complex is cited, not recalculated. |
| **MPL_33_098-146 N29** | First-pass categorical trace/contraction lead, scans134–136 | N27, N30 and N33 supply geometric integration and normalization, a different trace construction to be linked through duality. |
| **MPL_33_098-146 N30** | First-pass global finite-Tor requirement, scans136/140/142 | N17, N28, N44–N45, N49–N51 and N82/N85 add geometric scope and uniformity tests; they do not remove the later finiteness obligation. |
| **MPL_33_098-146 N36** | First-pass cancelled local-pairing/restart observation, scans144–146 | N05, N34 and N35 add separate cancellation/reordering episodes, without turning cancellation into theorem retraction. |
| **MPL_33_098-146 N37** | First-pass local trace/symmetry-sign claim, scan146 | N13, N22, N27, N30 and N33 add local classes and trace compatibility; no proof of the later sign convention is claimed. |
| **MPL_33_098-146 N40** | First-pass finite-level matrix-trace compatibility proposal, scans128/132/146 | N24 and N32 add a geometric Kummer-class/integration tower test; no duplicate supertrace calculation or completed adic passage is asserted. |
| **MPL_33_098-146 N41** | First-pass perfect-trace comparison, scans130–146 | N29 and N40–N48 add earlier geometric and derived formalism. The comparison remains a mathematical destination, not a dating proof. |
| **MPL_33_098-146 N54** | First-pass reused-source étale-criterion counterexample, scan145 | N68 offers a different literal reused-source counterexample; N02 adds a field/topos convention question. Neither re-derives the dual-number example. |
| **MPL_142_001-093 §316** | First-pass bibliographic/verification-limits observation; exact manuscript scans not supplied in this row | The present notes restate the method of distinguishing inspected primary content from metadata and inaccessible sources; no substantive theorem connection is evidenced. |
| **MPL_14_002-044 §107** | First-pass register-comparison observation; quoted grading/correspondence/Lefschetz excerpt truncated, exact scans unavailable | N63 distinguishes the reused Hilbert-series page from the separate grading-projector programme. No unseen proposition is inferred. |
| **MPL_91_099-143 §68** | First-pass Greenberg–Néron planning comparison; the excerpt names title124 and conditions126/128 | No Greenberg/Néron thickness or approximation construction occurs in the present scans. |
| **WG H9** | Unchecked planning hunch about cote44, Mordell–Weil lattices and a Hodge-index reduction in codimension$m$ | Local cycle classes here are relevant vocabulary but supply neither the conjectured lattice formula nor its reduction. N23 records this difference. |
| **WG2 §2.1 #2** | Unchecked plan; cotes16/54/37 named, manuscript pp.1–16 and scans3–18 in a truncated entry without a unique cote assignment | The graded polynomial algebra on011 does not construct the stated Lefschetz grading projectors or universal operators. N63 records the negative comparison. |

The referee-reviewed IDs listed in the register—LM4 D.32/D.34 and LM7_PUSH D.44/D.50/E.58/E.61/E.62/E.64/E.65/E.67—are not silently substituted for the open or differently numbered rows above. These leaves contain no identified proof or counterexample for those specific claims either.
