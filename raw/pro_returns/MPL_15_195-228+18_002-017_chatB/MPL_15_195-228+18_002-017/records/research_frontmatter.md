# Research notes — MPL_15_195-228+18_002-017

## Scope, evidence, and reading conventions

These notes concern the **49 retained scans**: cote 15, scans 195–228, followed by cote 18, scans 2–7 and 9–17. The transcription was frozen at **2026-11-15 14:05:01 UTC** before the supplied context was opened. All comparisons, calculations, proposed interpretations, and source questions below belong to the research notes; none changes the frozen transcription.

There are **78 atomic notes** with stable identifiers: R01–R38, PG01–PG20, RL01–RL08, B01–B08, and O01–O04. Each has a short body, a source location, a kind, a context comparison, and the relevant results-register status; the longer proofs and source audits follow as supporting calculations. A note's confidence concerns the stated calculation or reading, with any uncertainty about its application to the manuscript recorded separately.

| Source label used below | Exact supplied file or current source |
|---|---|
| Current cote/scan; P15/… or P18/… | The corresponding frozen `pages/MPL_15_195-228+18_002-017_C_scanNNN.tex`; scan numbers refer to the archive PDF, not printed internal pagination. |
| [C-T], C-TEX, or C followed by cote/scan | `MPL_16+47+54+44_transcription.tex` in the supplied context. |
| [C-N], C-NOTES, or N | `MPL_16+47+54+44_notes.md` in the supplied context. |
| C-DOUBTS | `MPL_16+47+54+44_doubts.md` in the supplied context. |
| [C-STATE], C-STATE, or R in the Lefschetz source audit | `notes/RESULTS_STATE.md` in the supplied context. |
| C-README | `README.md` in the supplied context. |
| C-ODA | `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`; Oda citations use printed pagination. |

The supplied context has these six files. It contains excerpts from a results register, not the full cote 14 returns, cotes 12–13, or the LM source returns named there. **Known, Proved, Refuted, and Open retain the register's reported status** unless a reviewed status is expressly recorded; first-pass archive notes remain leads, and WG/WG2 items remain unchecked plans. A newly checked published theorem is attributed to its own source and scope. No status of an absent return has been silently changed.

The context searches are recorded in `records/context_searches.jsonl`, `records/research_root_oda_searches.json`, `records/research_periods_context_searches.json`, `records/research_bridges_oda_searches.json`, and the Lefschetz search audit. The phrase “no match” describes the supplied files and recorded search terms. PDF searches use embedded text extraction; the manuscript scans were read visually without OCR.

## Answers to the specific archival questions

| Question | Finding and exact comparison |
|---|---|
| Written period conjecture | **18/011 explicitly boxes** “Conj. de transcendance forte” and \(\operatorname{trdeg}_k k(\alpha,\beta)=g+u\), with a question mark. PG01–PG05 retain the three comparison maps and their fields. Calculation P-A tests a specified canonical Hodge model and isolates the unresolved definition of \(\beta\); the boxed conjecture is recorded with that scope question. |
| Elliptic period questions | 18/013(a) asks for degrees \(4\) and \(2\); PG12 records the checked modern CM result and the remaining non-CM genericity question. For (b), PG13 and Calculation P-B construct \(\Omega=Ha\) from the translated locus and apply KSV Proposition 3.1 and Theorem 5.13(ii) to one elliptic curve. The inclusion \(Z\hookrightarrow\Omega\) states the remaining relation to (a). |
| Arithmetic motivic exact sequence over \(\mathbf Q\) | The retained text has the extension by \(\pi\) on 18/006, but supplies no identification of this \(\pi\) with \(\Gamma_{\mathbf Q}\). PG16 and Calculation P-C give the external sequence and its actual maps: base change induces \(G_{\overline{\mathbf Q}}\to G_{\mathbf Q}\), and restriction to Artin motives induces \(G_{\mathbf Q}\to\underline{\Gamma}_{\mathbf Q}\); the groups have rational coefficients. PG17 records the corrected connectedness qualification, and R38 checks the character dependency in 18/006 itself. |
| Lefschetz rings and a category of motives | C 16/3–18 gives projectors and an operator ring. RL01 and L2 give correspondence composition, the corners \(qfp\), idempotent completion, and Tate twists, including \(\operatorname{Corr}^r(X,X)=\operatorname{Hom}(h(X),h(X)(r))\). The historical construction in the absent cotes 12–13 and full cote 14 returns remains uninspected. |
| The Lefschetz \(\mathfrak{sl}_2\), motivic group, and grading | RL02–RL03 and L3 calculate the maps on \(h(\mathbf P^1)\): \(\rho(t)=\operatorname{diag}(1,t)\), \(\rho E\rho^{-1}=tE\), \(\rho F\rho^{-1}=t^{-1}F\), \(w(s)=j(s^2)\), and \(h(s)=s^{-1}w(s)\). The bracket calculation proves that every \(\mathfrak{sl}_2\to\operatorname{Lie}(\mathbf G_m)\) homomorphism is zero. Beauville's explicit \(\mathrm{SL}_2\to\operatorname{Corr}^{*}(A)\) is recorded in RL08/L3.2. |
| Draft A–D letters | RL05/L4 audit all relevant occurrences in C 16/42–50. **Draft \(C_\ell\) matches the algebraic-Lefschetz-inverse content of published \(B\)**. Draft \(A\) has compatible operational evidence; complete standalone definitions of draft \(B,D\) are absent from the supplied block, so a full permutation is not established. |
| Singular hypersurfaces in cote 14 | C 16/47 expressly asks for a singular reformulation. RL06/L5.2 record that programme, the negative `singul\|hypersurf` search in the supplied register, and the absence of the full cote 14 returns; those excerpts do not establish execution of the programme. |
| S15, Nori, Ayoub, and semisimplicity | R37 supplies the checked pure rational Nori–André equivalence through its functor on motivated correspondences. PG18 records the inverse Hopf maps relating Nori and Ayoub and Kahn's Nori descent sequence. RL07/L5.1 give the homological-to-numerical quotient and its kernel, while PG20 identifies period relations with the kernel of evaluation at the comparison point. These are the specified maps supporting the comparison. |

## Linear statement, nonlinear statement

The four requested rows below state the connecting maps and the setting of each cited result. Notes B01–B08 and calculations S1–S4 give the examples and proofs.
