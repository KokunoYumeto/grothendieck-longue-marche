# Post-freeze research review record

The primary agent transcribed and visually audited all supplied pages in one stream. The separate research reviewers began only after the transcription freeze, used the frozen text and context for research, and did not inspect manuscript images or alter a page file. Their checks are internal mathematical and quotation QA; they do not confer an external referee verdict on this report or on RESULTS_STATE.md.

## Independent checks of the most consequential calculations

The motives reviewer independently checked the Deuring memorandum's D04 and Constructions A, C and D against the stated hypotheses. The matrix-algebra example in D04, the ramified quaternion invertible-bimodule example in A, and the normal-base/Azumaya-open example in C survived that check. Construction D required a narrower claim: the target categories admit tensoring by every invertible A-module, whereas the manuscript's margin asks only for tensoring by norm lines. The full construction and final D28 now state that restriction and leave the general semisimple-centre and base-change claims unproved.

The Deuring reviewer independently checked FF13 and FF22. For FF13, categorical dimension and trace force the two real Frobenius eigenspaces to have dimensions 2 and 2, which is incompatible with nonzero Hamilton-quaternion modules; mere Q-linear faithfulness would not suffice. For FF22, root extraction proves the Galois-equivariant identification of the explicitly p-integral Weil-number quotient with the germ group, the weight splitting survives modulo roots of unity, and Milne's finite-stage and continuous-protorus results provide the specified uniqueness. The final note distinguishes existence for the specified fundamental local classes from existence for arbitrary local tuples.

## Quotations and mathematical scope checked against frozen text

### Motives

All M01–M27 and original RQ1–RQ5 scan and local-line anchors were checked against the frozen page text. RQ1–RQ5 are M28–M32 in the assembled report.

- The frontmatter now says “Tensor structure and realizations” at 12/152–154; it does not claim that those pages already construct a tensor automorphism group.
- M07 uses the pseudo-colimit notation rather than quoting an editorial “pseudo-lim”.
- M11 quotes only the unambiguous portion after the doubtful multiplication/multiplicative word.
- M12–M13 typeset the check and hat notation, rather than quoting editorial pronunciation.
- M14 keeps the final superscript uncertain and tests the formula only with the dual interpreted by the preceding explicit definition.
- M15 and the revision index retain the uncertainty of the inserted “épim.”.

### Finite-field notes

All FF01–FF22 brief quotations were located in their specified frozen scans. Their most precise page-file anchors are:

| Note | Anchor |
|---|---|
| FF01 | 15/003:L30 |
| FF02 | 15/003:L5 |
| FF03 | 15/005:L2,L9–12 |
| FF04 | 15/013:L3–4; 15/005:L15–17 |
| FF05 | 15/013:L21; 15/014:L34 |
| FF06 | 15/005:L37,L39 |
| FF07 | 15/013:L24 |
| FF08 | 15/013:L27–32 |
| FF09 | 15/009:L19,L23 |
| FF10 | 15/009:L6,L8–12; 15/007:L18–24 |
| FF11 | 15/009:L31 |
| FF12 | 15/011:L2 |
| FF13 | 15/011:L4 |
| FF14 | 15/009:L33; 15/011:L6 |
| FF15 | 15/013:L41 |
| FF16 | 15/013:L39,L46,L48 |
| FF17 | 15/014:L21–22; 15/013:L35–36 |
| FF18 | 15/014:L3–4 |
| FF19 | 15/003:L5; 15/013:L29 |
| FF20 | 15/011:L4 |
| FF21 | 15/003:L7–13,L24,L28; 15/007:L24 |
| FF22 | 15/009:L33; 15/011:L2; 15/014:L3–13 |

- FF03 avoids assuming whether Z-positive includes zero and preserves the uncertain membership sign.
- FF07 uses “group of multiplicative type” and quotients of finite type.
- FF12 and FF22 specify strict countable systems and continuous protorus cohomology.
- FF13 incorporates the independent tensor-trace argument.
- FF16 explicitly restricts the splitting conclusion to ell different from p and retains the opposite-algebra sign for contravariant degree-one motives.
- FF22 assigns the torsion kernel to the map from W(p), before passing to its quotient.
- References to scans 007 and 009, or 009 and 011, do not imply that an intervening reused typescript is part of the argument.
- The frontmatter preserves the conditionality of the commutative band on 15/003.

### Deuring notes

The Deuring reviewer checked all D01–D30 brief quotations and scan anchors against the frozen page text.

- D06 retains both cancellation and uncertainty of the old subscript 0.
- D11 retains the uncertainty of “rg”; D12 of “ass.”; D15 of “pas décomposé”; D24 of “commute”; D30 of both tentative words.
- D20 quotes the written ell-indexed formula and its separate ell=2 condition instead of presenting a specialized formula as a literal quotation.
- D24 quotes the frozen dash in the base-change expression.
- D05 refers to Constructions A–B, D09 to B, D13 to C, D26 to A, and D28 to D, all explicitly in records/research_deuring.md.
- The frontmatter correctly locates D04's argument in D04 itself and states the restriction on Construction D.

## Status of working memoranda

The original research memoranda are preserved as working records. The assembled notes are the reviewed deliverable and incorporate the corrections above through records/assemble_notes.py. The assembler writes only the notes and their manifest; it never writes a frozen transcription file.

Context-search records preserve the queries, source-file hashes, bounded excerpts and hit counts for every numbered item. These searches are evidence of what was compared, not a claim that absence of a literal search term establishes absence of an implicit mathematical idea.
