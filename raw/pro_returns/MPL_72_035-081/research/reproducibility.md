# Reproduction and validation

## Run location and dependencies

Extract the ZIP and run the following commands from its root, the directory containing the combined transcription and the research folder. The mathematical scripts use Python 3 and SymPy; the recorded environment used Python 3.12.14 and SymPy 1.14.0. The invariant-subspace enumerator, context-search audit and page/title counter use only the Python standard library.

| Command | Reproduces |
|---|---|
| python3 research/recompute_enumerations.py --max-n 12 --matrix-max-n 5 | Continuant and determinant calculations, matching lists, full matrix and vector tables, source-reading residuals, documentary lists and their catalogue. |
| python3 research/case_catalogue.py | The 31 numbered or indexed prose-case rows and their evaluated totals for dimensions 1–6. |
| python3 research/group_quadric_checks.py | The rank-one group law, common-kernel identities, quadratic forms, scan-045 pairings and concrete characteristic-two checks. |
| python3 research/invariant_subspaces.py | Every subspace and parameter choice in the six explicitly listed finite-field grids, exact classification comparisons and counterexamples to the literal minimum criterion. |
| python3 research/bridge_compute.py | The eleven levels 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15; marked matrix quotients, generator cycles, kernel, nilpotent and conic vertices, and odd-level geometric support fibres. |
| python3 research/split_clifford.py | The integral Clifford matrix presentation and rank-four Azumaya action basis. |
| python3 research/title_counts.py | Four cover-led scan runs and all 48 manuscript-number inscriptions across 47 scans. |
| python3 research/self_flags_scan.py | All ten literal question-mark occurrences, including their positions, uncertain/cancelled states and source hashes. |
| python3 research/context_search.py --context /path/to/unpacked/context | Per-item literal searches of the three supplied context files; their original hashes are recorded with the search manifest. |
| python3 scripts/freeze_verify.py --require-context --json | All 48 frozen SHA-256 values, page/combined consistency and the logged context-opening order. |
| python3 scripts/validate.py --mode final --json | Required deliverables, scan order, inventory fields and rows, recorded second readings, and static fragment constraints. |
| python3 scripts/static_tex_review.py | Additional static review of the custom-macro fragment and formula structure. |

Commands for the context audit require the supplied context ZIP to be unpacked separately. The original scans, input archives and context files are excluded from the returned ZIP. The mathematical calculation scripts use saved formulas and their explicit parameter lists; they do not process manuscript images.

## Exact scope of the computational evidence

The continuant program lists **609 individual matchings** for orders \(0,\ldots,12\), with **49 order/pair-size rows**, and all **374 exact checks** pass. Symbolic determinant comparisons run through order 7, and complete matrix, dual-basis, centre, vertex and norm tables run through dimensions 1–5, with 1,575 matrix entries, 270 dual-basis entries and 590 vector coefficients. Its JSON records every exact check and every literal-reading residual; a passing coherent polynomial identity does not erase a nonzero residual against a frozen source expression.

The invariant-subspace program enumerates all reduced-row-echelon subspaces for each of its six finite-field grids. It records **178 parameter choices**, **24,012 subspace tests**, zero failures of the proved candidate classification and exact count, and **24 failures of the literal scan-081 minimum criterion**. The accompanying proof establishes the stated general classification; the finite grids provide a separate, completely enumerated check.

The bridge program enumerates all determinant-one matrices at its eleven listed levels, quotients them by the single global sign subgroup, and verifies the marked cycles independently of the closed count formulas. It computes the adjoint kernel, column and nilpotent orbits, and projective conic points; at odd levels it also constructs the actual geometric support sets and flag triples. The manuscript-coordinate basis change has determinant \(-2\), so that particular identification is made over \(\mathbf Z[1/2]\), while the integral adjoint and conic formulas are computed on their separately stated bases.

The Clifford program records 11 exact checks, all 16 products of its four even generators, and all 16 matrix-unit actions. The documentary lists count literal entries, representation pairs and labelled fields, with the [name redacted]/[name redacted] line-break alternative specified as a separate extraction operation. No identity merge, handwriting date or unseen page is inferred by those counts.

## Transcription verification and limits

The primary transcriber read each whole scan and both supplied halves in order, wrote each page before proceeding, and carried out a second independent image comparison of all 47 pages before freezing. The inventory, notation comparison, second-reading timestamps, context-opening timestamp and 48 frozen hashes are in the delivered files. All mathematical research was performed after the freeze, and final verification checks that the 47 page hashes and the combined-fragment hash are unchanged.

The LaTeX deliverable is the requested fragment with the custom editorial macros, TikZ drawings and tikz-cd diagrams. Mechanical checks establish file presence, ordering, structural consistency and hash preservation; the task did not produce a successful compiled TeX preview because the available runtime lacked the required TeX formats and packages. The doubts file remains the authoritative record of uncertain readings, with the notation table and abbreviation list at its start.

The research directory also retains the independent review of the centralizer and invariant-form arguments, explicit context-search records, and all calculation outputs. The historical preparation scripts remain as documentation; the record-writing helper refuses writes after a freeze marker, and none is required to reproduce the mathematical calculations.
