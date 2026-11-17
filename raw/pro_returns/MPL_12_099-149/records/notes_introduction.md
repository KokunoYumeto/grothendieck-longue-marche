# MPL_12_099–149 — Research notes

## 1. Evidence, scope, and reading conventions

These notes were written only after the 36 retained page fragments and their combined transcription were frozen at **2026-11-17 21:15:29 UTC**; the context archive was first opened at **21:15:42 UTC**. All reading disagreements raised by context or mathematics stay in these notes: the frozen transcription, its doubt apparatus, and its inventory have not been revised during research. The main note bodies contain one to four sentences; witness, classification, quotation, context relation, results-register status, and confidence are separate metadata.

**Source hierarchy.** The diplomatic fragments are the primary witness for this selection. The supplied earlier transcription and research return are contextual witnesses and leads, respectively; **Hua, modernised reading of cote 12** is an AI-produced interpretive account, not an independent diplomatic transcription, and its insights are credited explicitly. A theorem in the external literature is distinguished from a statement in a research run and from an argument reconstructed here; “own idea” means our present test or deduction, with no claim of novelty.

| Short locator | Exact supplied or delivered file | How to read its references |
|---|---|---|
| P, or 12/NNN | `pages/MPL_12_099-149_12_scanNNN.tex` | Cote 12 and PDF scan number; locations describe the paragraph, display, margin, or local file line. |
| CT | `context/MPL_16+47+54+44_transcription.tex` | Cote/scan within the earlier return; e.g. 16/049. |
| CN | `context/MPL_16+47+54+44_notes.md` | Exact section or note ID in the earlier, unreviewed research return. |
| CD | `context/MPL_16+47+54+44_doubts.md` | Earlier reading questions, not authority to alter the frozen text. |
| H or Hua | `context/hua_project/12.modern.tex` | Always credited as **Hua, modernised reading of cote 12**, with subsection title; Hua's page n corresponds to this package's PDF scan n+1. |
| Hua XIII | Same file, “XIII. Motifs lisses et isomotifs lisses (pages 138 à 141)” | Corresponds to scans 139–142, including the cover. |
| RS | `context/notes/RESULTS_STATE.md` | An ID plus its recorded status; a run's “Proved” label is not independently reviewed establishment. |
| README | `context/README.md` | The supplied planning and research questions, especially “This package in our plan” and “What our planning document asks of these folders.” |
| Oda | Supplied `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf` | Printed article pages and numbered results; Corollaries 5.11–5.12 were also inspected on printed p. 131. |

Each numbered research item has a same-term context search. Complete matching **locators**, query, and search time are retained in `records/research_searches/NOTE_ID.json`; source files themselves are excluded from this archive. A lexical hit does not establish a substantive match: each note separately states whether the present pages add, restate, differ, contradict, or leave no matching point, and the detailed manifests identify inspected passages. The unverified-steps section is an index back to those notes, while its fuller coverage register also records abbreviated proofs and cancellations.

**Weight conventions.** The cohomological convention is that geometric Frobenius on \(\mathbf Q_l(-1)\) is multiplication by \(q\), hence weight 2; the table's covariant Tate-module comparison expressly uses arithmetic Frobenius. “Hodge level” denotes \(\max|a-b|\) among the Hodge types of the weight-graded pieces, whereas the manuscript's geometric generation level, its dimension type on 12/125, and coniveau are distinct notions. The Hodge reconstruction of a level bound is not a proof of every geometric interpretation of that bound.

## 2. Answers to the package's research questions

| Question | Finding and precise boundary | Detailed notes |
|---|---|---|
| Linear / non-linear comparison | Tate–Faltings Hom, anabelian Hom, semisimplicity, centre-freeness, polarization, real sections, and cyclotomic normalization require different hypotheses and retain different information; the full four-pair table follows below. | LN01–LN07 |
| Is the construction built from the Lefschetz correspondence rings of cote 16? | The structural connection is supported by CT 16/018 and 049, but scans 143–149 provide only the abstract completion and tensor-extension stage; the actual geometric example is in Hua's next subsection, beyond the supplied selection. | M02–M15 |
| Is Lefschetz \(\mathfrak{sl}_2\) inside the motivic Galois group, with its grading the weight cocharacter? | There is no such general identification: the already registered \(\mathbf P^1\) test separates degree-changing Lefschetz operators from tensor automorphisms preserving the unit and the Tate weight decomposition. | M16, M25 |
| Actual A–D versus printed letters | Draft A ≈ printed A and draft C = printed B are supported operationally; draft B ≈ printed D and draft D ≈ printed C remain provisional without the missing defining witness, especially the RS lead to 14/117. | M17 and its lettering table |
| Does cote 14 resume 16/047's singular-hypersurface programme? | The supplied selection contains related singular-cohomology work, but supplies no cote 14 primary witness for the proposed resumption. | M18 |
| Motivic Galois exact sequence over \(\mathbf Q\) | No such sequence is written in this selection; for rational Nori motives and compatible \(\mathbf Q\)-valued Betti fibre functors, the descent comparison is \(1\to G_{\mathrm{mot}}(\overline{\mathbf Q})\to G_{\mathrm{mot}}(\mathbf Q)\to\Gamma_{\mathbf Q}\to1\), using the filtered 2-colimit over finite extensions, with connectedness and splitting separate (Kahn, 2025, §5.8, Theorems 5.10 and 10.2). | M19–M20 |
| Period conjecture | No statement is found here or in the full supplied Hua reading; RS's 18/059 “conjecture de transcendance N° 1” is an exact retrieval lead only, while the modern period-torsor statement is given separately (André, 2010, §1.4). | M21–M22 |
| Nori and Ayoub | The pure Nori–André comparison and the Nori–Ayoub group comparison are precise later theorems, and neither identifies motivated cycles with algebraic cycles or proves the standard conjectures (Arapura, 2013, Theorem 6.4.1; Choudhury & Gallauer, 2017, Theorem 9.1). | M23–M25 |
| Most consequential local proof issues | Varying elliptic coefficients refute the sharper weight bounds; the double blowup refutes unconditional survival of a top-weight \(E_2\) term; mixed-characteristic purity counterexamples answer the unrestricted abelian-scheme extension question. | W13–W14, R04, W25, SM13–SM15 |

### Results-register status and what this package adds

The supplied RS orientation lists no curated “Our results to use and check” entries. The following ledger preserves its distinctions; citing a reviewed external theorem below does not retrospectively upgrade an internal return.

| RS ID or locator | Recorded status / evidence class | Use here |
|---|---|---|
| LM6 A.22 | Open, run claim | Weight obstructions do not detect a procyclic subgroup lying in all the tested abelian kernels. |
| LM6 A.50 | Proved, run claim | The recorded finite-cover character-descent result is cited as a lead, without rederiving or certifying it. |
| LM7 C.1 | Known, run claim | The Fermat Picard 1-motive / generalized-Jacobian interpretation distinguishes graded weights from extensions. |
| LM7 C.5 | Proved, run claim | The marked-divisor extension class and its exact finite-level order are extra data; no uniform tower exponent is inferred. |
| LM7 C.8 | Refuted, run claim | The identification with all weight splittings is not reused as a theorem. |
| LM7 E.23 | Open, run claim | The depth-two/metabelian section problem is not solved by the present linear bounds. |
| FLAGGED_149 B9 | Open, run claim | The prime-to-p point-detection question remains distinct from cohomological purity. |
| ANABELIAN_SUCCESSOR A.3 | Newer claimed result, partly checked according to RS | Its headline does not silently close B9 or identify the two scopes. |
| LM1 A.8 | Refuted, run claim | The recorded determinant-inverse twist \(\theta(g)=\det(g)^{-1}g\) fixes \(\mathrm{SL}_2\) pointwise and warns against inferring a unique symmetry from invariant tensors alone; no reconstruction assertion here depends on the refuted claim. |
| `12-immersion-level-bound` | Hua candidate; intake “new to us,” not reviewed | The constant-coefficient level question is retained, its dimension-zero exception recorded, and its coefficient extension tested separately. |
| WG2 §1.1 #2–#3; §2.3 #2/#7; §2.4 #3; §3.2 #7 | Unchecked planning questions | Documentary shape, Lefschetz algebra, semisimplicity, motives, and six-operation questions organize the comparisons. |
| MPL_11_043-058+56 N031; MPL_14_087-132 M01/M04/M23; MPL_15_087-138 L01/L07/T26 and §111/§127 | First-pass returned-package leads; underlying pages absent here | They point to projector constructions, the notation table, the \(\mathbf P^1\) obstruction, and period/SL₂ questions; none is cited as a newly inspected manuscript witness. |
| MPL_15_195-228+18_002-017 B03/B04/M07/S15; MPL_18_018-062 MB10 and §§2–3; MPL_60_002-035 F21–F22; MPL_131 RN038 | First-pass leads | They locate real-structure, cusp-weight, modern-motive, parity, period, and extension questions without replacing the supplied evidence. |

