# Context searches and source checks for S/H notes

All searches below were performed after the freeze, on 2026-11-17. No image was viewed. Paths are relative to MPL_64_116-157_context/, except the frozen source ../MPL_64_116-157_work/pages/.

## Required source reading

- README.md, notes/RESULTS_STATE.md, and hua_project/README.md were read before composing notes. RESULTS_STATE.md was read in full in the inherited research context; its orientation, P09/E14 rows, Hua summary, and relevant open-result rows were reread or searched locally.
- The entire 2,120-line hua_project/64.modern.tex was read in sequential segments. One oversized multi-output call was truncated, so lines 841–1100 and 1100–1420 were reread; no gap was treated as read.
- The inventory from rg --files contains no full cote-93 or cote-159 text/notes file. The MPL_93_002-046_notes.md path listed at the end of RESULTS_STATE.md points to an absent earlier return, not an available file.
- Frozen scans139,143,144,151,152,155,126 were read directly, with other frozen pages searched for exact anchors. An initial attempt to concatenate several larger frozen pages was truncated and was not used as evidence of reading them. No manuscript image was reopened.

## Per-item searches

| Notes | Search objects/words actually used | Context matches and exact locators | Relationship and limit |
|---|---|---|---|
| S01, S03–S05 | S20; Gauss.?Manin; Cartier; Picard.?Fuchs; Hasse.?Witt; p.?courbure; p.?curvature; connexion; connection; Schwarz; literal TeX nabla | README.md S20; SECTIONS_STATE.md, entries90–102/cote93 and158–160/cote159; RESULTS_STATE.md, Orientation and MPL_93_002-046 P09/E14/E16/C29 | Adds bounded analytic evidence and a modern test to an existing programme; does not establish historical unity. Broad English connection also retrieved irrelevant prose, which was excluded. |
| S01 | Same operator terms across all existing frozen page files | Zero matches in the frozen pages; positive anchors are143 local system,144 ratio,151 frame | Negative lexical evidence applies only to this selection. Initial explicit shell expansion mentioned omitted scans122/130; the search was repeated against the directory itself and found zero matches without missing-file errors. |
| S02 | rigidification différent; fibré tangent; système local; Hodge | Hua, “Approche transcendante — seconde mouture,” “La rigidification différentielle”; frozen143/151; RESULTS_STATE.md, P09 | Restates Hua's frame object and adds the rank/duality distinction. Other LM local systems retrieved by the broad search were not identified with this system. |
| S03 | Legendre; Torelli; système local; Picard.?Fuchs | LM_OVERVIEW.md §§34–37 summary; LM_140-2_text.tex, §37 title and level-two description; SECTIONS_STATE.md cote64/formulary entry; P09 | Uses the selection's explicit Legendre and period objects to propose a calculation; no current-page Picard–Fuchs operator was found. |
| S04–S05 | Cartier; Hasse; courbure; curvature | SECTIONS_STATE.md cote93 description; RESULTS_STATE.md P09; no current frozen-page matches | Adds distinctions and a computed example; cote93 itself remains unavailable. Unrelated effective Cartier divisor matches in cote149 notes were excluded. |
| S06 | uniformis; revêtement universel; M_{1,1}; projective connection | Frozen149 theorem, read in full; SECTIONS_STATE.md cote159 catalogue entry; RESULTS_STATE.md P09; Hua second draft theorem | Adds the distinction between uniformizing a moduli space, a parameter curve, and an individual fiber; no identification with the absent cote159 connection is made. |
| H01 | condition c; F_t; Dieu sait; Posons; Legendre | Hua, “Vers l'épinglage de Legendre,” “La droite F_t” and final footnote; frozen121/126; RESULTS_STATE.md “Cote64: the opening…” and P09 | Supports unfinished status and credits the linkage of loose sheets to Hua's project; no proof of conditionc found. |
| H02 | B_3; B3; tresses; boundary twist;467; extension centrale; rigidification | LM_140-2_notes.md467-5/467-7; LM_140-2_text.tex scan467 margin; Hua final differential-frame footnote | Restates the central-extension claim and adds Hua's elliptic frame realization. No dedicated B3 RESULTS_STATE ID exists; B1–B3 tally references there are unrelated. Earlier “known” status was not used as verification. |
| H03 | rang.*1; antiholomorphe; première mouture; Torelli | Hua first-draft theorem/rank footnotes; frozen139–140; RESULTS_STATE.md Orientation, EXIT_TOWER E.24/LM4_SUCCESSOR B.38 | Deliberate modern correction, not a reopened reading or solution to arithmetic-image/congruence problems; root supplies the analytic proof notes. |
| H04 | anneau jauge; régulier local; régulier.*dimension | Frozen155 uncertainty; Hua “Normalité de B=A[S]/(S²−a) (page154)” and footnote | Direct source-reading difference; no corresponding prior-result ID or independent corroborating reading occurs in supplied context. |
| H05 | 152 est blanche; M_{1,1}; M_{1,2}; section nulle; quadratiques | Hua differential-frame footnote; frozen152 ending and153 cover | Subscript/inventory difference; no detailed matching RESULTS_STATE row; later reading questions only. |
| H06 | invariant modulaire exceptionnel;1728; j=0; j = 0 | Hua Appendix “Exemple”; frozen156; LM_140-2_notes.md A14 scan535, B9 scan560, R10 scan514; RESULTS_STATE E14/P09 | Restates an interpretive lead; current wording does not supply j or the exponents. |
| H07 | octaèd; octaéd; octahedral; caractéristique.*5; characteristic.*5;120; PGL.*5 | Hua “II…1. Actions du groupe de Klein, configuration octaédrale”; LM_140-2_notes.md R09/C02 scan363; RESULTS_STATE Hua octahedron paragraph | Adds paired/unpaired distinction by independent enumeration; explicitly outside current manuscript range. A malformed regex with an unescaped TeX command failed and was replaced by the successful simpler word search. |

## Primary-source web verification

Routine system2 queries found Katz/Hain; system1 queries verified authoritative sources and bibliography. URLs were opened and relevant theorem/definition passages read, rather than inferred from snippets.

| Source | Material actually read | Checked point | Boundary |
|---|---|---|---|
| Katz1968, https://www.numdam.org/article/PMIHES_1968__35__71_0.pdf | Introduction, printed71–74; Numdam metadata | Differentiation of periods; Legendre hypergeometric/Picard–Fuchs example; Hasse polynomial | C1/C2 independently calculate formulas used; no whole-paper proof audit. |
| Katz1970, https://www.numdam.org/item/PMIHES_1970__39__175_0.pdf | Theorem5.1,5.10,7.4/Corollary7.5,10.0 and introduction | Zero p-curvature in Cartier descent versus nilpotent Gauss–Manin p-curvature; applicable hypotheses | General proofs carried as published background. |
| Hain2014v3, https://arxiv.org/pdf/0812.1803 | Proposition5.16, Proposition8.2, Corollary8.3, Remark8.4 and adjacent arguments | Tangent/Hodge duality; discriminant complement; B3; central-square kernel | Versionv3 dated2014; do not silently cite the later2021 revision's pagination. |
| Hain bibliography, https://arxiv.org/abs/0812.1803 and https://scholars.duke.edu/publication/1025733 | Version dates and Duke's APA record | arXivv3:2014; book chapter:2010, Ji/Yau, volume16,95–166,HigherEducationPress | Metadata only. |

Useful web reference IDs for the root to reopen if rendered citations are needed: Hain PDF turn417785465view1; B3 passages turn873665411view0/turn873665411view1; Hodge duality turn873665411view2; Katz1968 turn417785465view0 and Legendre/Hasse excerpt turn873665411view3; Katz1970 turn806205847view0; Duke metadata turn417785465view3. These are retrieval handles, not the citations used in the notes, which use APA references and URLs.

## Checks performed

- C1 exact-differential residual: zero by symbolic rational simplification; Schwarzian formula: exact rational equality.
- C2 p-curvature recurrence modulo3: explicit nonzero matrix; square, trace, determinant vanish. Outer-product factorization explains square-zero.
- C3 full central-kernel assertion checked in Hain Remark8.4; elementary matrix identities independently evaluated in the certificate run.
- C4 exhaustive projective transformations modulo5:120 distinct permutations;24 preserve opposite pairs.
- None of these checks establishes S20's historical identification, conditionc, a congruence kernel, an arithmetic image, or disputed manuscript wording.
- Follow-up: frozen153 was read directly and the H05 heading's inaccurate preliminary cover title corrected to “normalité des ext. quadratiques”; no diplomatic text changed.
- Follow-up: Katz1970 (7.3.3), Theorem7.4(7.4.1), and Corollary7.5 were reread. S smooth over a field has flat absolute Frobenius; H¹ has only bidegrees(0,1),(1,0), so the exponent-two bound follows. The report now explicitly states that base hypothesis.
- The four code blocks are also saved as connections_certificates.py and were executed standalone; their observed output is connections_certificates_output.txt, ending ALL FOUR CERTIFICATES PASS.
- Review response to structural_validation: S05/C2 now distinguish the period/solution companion ∂−A from the de Rham coefficient-column connection ∂+Aᵀ in the cyclic basis (ω,∇ω). The added C2 recurrence directly checks ψ_dR=−ψ_solᵀ and square-zero modulo3; standalone script and observed output were synchronized. This clarifies convention without adding a new exploratory claim, and S05 retains four sentences.
