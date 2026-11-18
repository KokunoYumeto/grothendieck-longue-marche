# Research notes — MPL_29_095–140

## Evidence, scope and principal findings

This package transcribes **31 supplied scans of cote 29**: 095–101, 103–112, 117–118, 124, 126, 129–133, 135, and 137–140. The manifest and explicit 31-page description govern the scope; the prompt's isolated reference to 46 pages is inconsistent with those inputs. The excluded earlier-run scans were not added, and no claim below treats their handwriting as inspected in this run.

The complete transcription was audited a second time, reconciled for recurring notation, and frozen at **2026-11-18 06:04:22 UTC**, before context was opened at **06:04:34 UTC**. Root alone performed every image reading and visual audit, in one sequential stream; ancillary research agents worked only with the frozen text and textual context after that freeze. These notes contain mathematical interpretations, questions and explicitly labelled independent arguments; they do not change the transcription or promote uncertain ink to a confident reading.

The most consequential findings are these:

| Finding | Notes | Evidence and limit |
|---|---|---|
| The broad minimality–injectivity claim fails for arbitrary admissible groups over a reduced singular base | N028–N033 | An explicit pointed α_p-torsor over the cusp is minimal but has identical pushforwards through distinct S-group maps; the proposed reduction is the nonflat normalization. The test uses the declared mathematical repair of the source's minimality formula and does not refute the letter's restricted exact-functor setting. |
| The author's uniqueness question for the infinitesimal kernel has a precise answer without reducedness | N025, N056 | Finite étale quotients and geometrically injective kernels suffice for uniqueness; the separate pointed-rigidity assertion fails if reducedness is dropped. |
| Arithmetic inertia need not be central | N001–N002 | A tame C₃⋊C₂ quotient of F₂((t)) refutes unrestricted centrality in Hua's contextual formulation; scan096 itself makes no such centrality assertion. |
| Several modernized statements lose source hypotheses or change their force | N027, N036–N041 | Direct checks separate the valid CRT implication from a false converse, prove the monic-factor claim with connectedness, and refute localization gluing with the inserted neighborhood condition omitted. These checks are scoped to the exact strengthened formulations. |
| Several major claims remain conjectures or unfinished arguments in the supplied evidence | N003, N005–N014, N020–N024, N031, N040, N042 | These include the homotopy sequence, the route to the abelian-variety formula, the Witt-module expectation, the Kummer–Chern comparison, and the relative representability/gluing programme. Contextual continuations and familiar mathematical identifications do not fill missing source text. |

None of the independently checked examples is advertised as new to the literature. No statement in the supplied RESULTS_STATE register is upgraded merely because it appears there, and no claim is made to have proved the full fundamental-group-scheme construction, the complete geometric local-monodromy theorem, or the complete formal-inertia classification.

## How the context is cited and searched

The context contains only `README.md`, `notes/RESULTS_STATE.md`, `hua_project/README.md`, and `hua_project/29.modern.tex`. The last is credited throughout as **Hua, modernised reading of cote 29**, with its subsection title; it is an AI-produced interpretation that explicitly changes notation and sometimes hypotheses, not the diplomatic source or this project's results. Its **page n corresponds to archive scan n+1**: for example, Hua p.95 is scan096, p.120 is scan121, p.139 is scan140, and p.140 is the unavailable scan141.

The three findings in RESULTS_STATE are credited to **Hua, findings register**, with their exact identifiers. Its ordinary statuses are earlier runs' claims unless an entry explicitly records a review; its intake “new to us” is not a mathematical verification. The underlying source registers for LM1 and the earlier returned-package notes are named but not included in this context, so their full proofs could not be reviewed here.

Every numbered item has same-word or same-object searches, a named contextual location or an explicit negative search result, a relation label, and the relevant register IDs when there is a real connection. `records/context_searches.tsv` and its JSON counterpart record the executed fixed-string searches and hit locations without copying the supplied context into this deliverable. The full modern file was read collectively across the research phase, with coverage recorded in the support files; this collective text work did not involve parallel visual readers.

**Check discipline:** a comparison of wording is not a mathematical check. The proof and counterexample records are in `records/notes_*_support.md`; their exact events are separately recorded in `CHECK_EVENTS.tsv`, including any subsequent proof review. A check of a local algebra example, a conditional cokernel, or a logical implication is not labelled as a proof or refutation of a larger geometric theorem.

## Standing question 1 — Steps the manuscript itself marks as unverified

The following table records the supplied words and their status, including visible doubt or an explicit intention to prove; it does not import self-flags from unsupplied context pages.

| Cote / scan | Source words or mark | Status in these leaves | Notes |
|---|---|---|---|
| 29 / 098 | “sans doute”; uncertain negative clause about being “abélien fini”; “??” | Arithmetic speculation whose wording and mathematical scope remain uncertain | N006 |
| 29 / 098 | “Mais qu'est Π₂ᵗ(X₀/D′₀)” followed by “???” | Explicit unresolved arithmetic second-homotopy question | N005 |
| 29 / 100 | “Il faut prouver que I est premier aux car. résiduelles”; “Commutation des Iᵢ” | Two remaining local steps; the latter stops mid-phrase | N007 |
| 29 / 101 | “On veut prouver” before the Chern-class equality | Explicit proof target, followed by undeveloped variants | N008–N009 |
| 29 / 107 | “On doit prouver un th. de descente”; “déterminer certains hom. canoniques” (abbreviations partly uncertain) | The local descent theorem and maps are still to be supplied | N051 |
| 29 / 110 | “petite vérification”; final “on voit que c'est vrai sur les” | A verification is named; the written existence argument does not finish | N037–N038 |
| 29 / 126 | Conditions (v),(vi) “ont une sale gueule” and are “essentiellement provisoires” | The author marks restrictions of the construction as provisional | N017, N019, N056 |
| 29 / 129 | “conjecture” inserted over deleted “hypothèse”; “sans la notion de corps de base, c'est plus obscur” | Exact homotopy-sequence formulation is conjectural | N020–N021 |
| 29 / 129–130 | “Il est hors de doute”; “Cartier doit l'avoir fait”; “facile de vérifier”; “devrait … fournir” | Witt-module construction and its hoped-for uniform application are not proved here | N023 |
| 29 / 130 | “J'espère”; “Sauf difficultés imprévues ou enlisement” | Programme and timetable, not a mathematical proof | N024 |
| 29 / 131 | “est-il représentable??”; uncertain “Cas fini??”; “[cas à fibres finies]” | Relative representability and its finite-group scope are explicitly questioned | N042, N049 |
| 29 / 137 | “[pour cette assertion, l'hypothèse ‘S réduit’ est-elle nécessaire?]”; margin “S réduit?” | A question about uniqueness of the infinitesimal kernel, separate from rigidity | N025, N056 |
| 29 / 139 | Possible marginal “Sans rigueur”, marked uncertain | A possible self-flag only; not a confidently read withdrawal | N030 |

The cancelled scan104 proof, the incomplete criterion on scan133, and the terminal comma on scan140 are additional visible draft boundaries, even where no phrase such as “à vérifier” accompanies them. The words “Je ne suis pas [sûr] de mon raisonnement” quoted by Hua for scan135 are **not** the frozen reading and are therefore excluded from the source-authored self-flags above; N048 records that discrepancy. Whole-page or local cancellation is recorded as documentary state and is not, by itself, treated as a mathematical counterexample or a proven retraction.

## Standing question 2 — Title sheets and page counts

| Cote / scan | Visible title or pagination | What can be concluded |
|---|---|---|
| 29 / 112 | “Notes pour SGA 7” | A title/cover sheet; no total page count is written on it. |
| 29 / 124 | “Vrai” groupe fondamental; faint bracketed subtitle transcribed with `ensembles\|schémas` alternatives | A title/cover sheet; no total page count. Hua's “[feuilles anciennes]” is a contextual reading question, not a replacement. |
| 29 / 117 | “Comportement fonctoriel des groupes d'inertie.” | Heading of the folder's own typescript; no total page count on this face. |
| 29 / 109 | “Ad majorem fonctori gloriam” | Heading of a separate reused typescript; no date, signature, or total count on this face. |
| 29 / 096, 098 | Text pagination 5,6 | A local numbered sequence for the formal-inertia discussion; not a statement that the package has six pages. |
| 29 / 126, 129, 130 | Text pagination 2,5,6 | Selected letter continuations; pages1,3,4 are not supplied here. |
| 29 / 106 | “- IV- 878 -”, with 878 marked uncertain | An internal typescript page/header indicator, not a count of this dossier. |
| 29 / 132 | “I-6”; section heading “5. Conjugates” | Internal numbering of the reused English typescript, not a continuation of the adjacent handwritten foliation. |

No cover in the supplied set states a total such as “19 pages” or “Pages1–67.” Archival foliation is kept in TeX comments and is not promoted to the author's page numbering. The inventory distinguishes **17 handwritten text faces, 4 folder typescript faces, 7 reused typescript faces, 1 cancelled draft, and 2 covers**; the reused diagonalizable-group sheets, EGA sheet, Bourbaki note, cancelled typed fragment and English sheet are transcribed in full rather than absorbed into a continuous mathematical narrative.
