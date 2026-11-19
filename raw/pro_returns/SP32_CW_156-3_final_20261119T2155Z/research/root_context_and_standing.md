# Context, source status, and the standing questions

## Source key and limits

**F** denotes the frozen consolidated transcription, `pages/J156-3-04_156-3_scan026.tex` through `pages/J156-3-05_156-3_scan041.tex`; a locator such as F 032:margin is a scan and the labelled position in that file. The manuscript folio is always the scan minus one. The complete transcription and all sixteen page files were frozen at **2026-11-19 21:31:14 UTC**, before the context was opened; mathematical corrections below are not changes to those files.

**E** denotes `SP32_CW_156-3_context/Esquisse_cote119_copy1_API_transcription.tex`. Its own `\scanpage{119/NN}` tags, rather than the PDF page number, identify the cited pages; the comments give a further PDF/site/typescript mapping. This is explicitly an API transcription not checked by eye, so the comparisons below concern the supplied text, not newly verified Esquisse ink.

**RS** denotes `SP32_CW_156-3_context/notes/RESULTS_STATE.md`, read in full before these notes were written. Its statuses are the earlier runs' claims except where the register explicitly reports a referee verdict. The underlying research returns named in that register were not supplied: a citation to an RS entry is not a claim to have reopened or checked the original return.

**S3**, **S5**, and **S7** denote `SP32_CW_156-3_sweep3/readings/156-3.md`, `156-5.md`, and `156-7.md`; **ST** denotes `SP32_CW_156-3_sweep3/STUDY.md`. They are research witnesses, not authorities. In particular S3 explicitly says that it viewed **no scan image** for cote 156-3: its corrections are mathematical proposals, even though the package's general description calls the CORRECTIONS rows decided readings. The present transcription's handling of those rows is separately documented in `SP32_CW_156-3_changes.md`.

**C04** and **C05** denote witness C's `J156-3-04_notes.md` and `J156-3-05_notes.md`. Every item in those two files is reviewed below. Context searches covered the words for the actual objects in each group: *bord/frontière*, *tronçon/interstitiel*, *modéré/constructible*, *Boole/complément/adhérence*, *composantes/spectre*, *drapeau/subdivision*, and *entre/caractérisation*, together with their English equivalents in RS.

The proofs and countermodels in `research/` are this run's mathematical work, using the stated hypotheses. They do not assert novelty. No external literature was fetched, no OCR was used, and no LaTeX compilation was performed; the final package validation is lexical and structural. Statements about scans outside 026–041 are attributed to the supplied context and were not checked against those images.

## Standing question 1: steps the manuscript marks as unverified

| ID | Scan and position | His words | Classification and disposition |
|---|---|---|---|
| SF-01 | 032, margin beside b–c | “Cette relation est-elle déductible de la relation d'ordre”; “ssi … existe ???” | An explicit mathematical question. Keep C04's item, distinguishing the proposed meet-existence test from the stronger question of reconstructing compatibility from the ordered set. The test has a counterexample; the stronger recognition question is not thereby answered. |
| SF-02 | 037, NB below *Composantes* | “On s'attend qu'il soit mod. avec … Y. S'il en est ainsi” | An explicit expectation and a conditional continuation. Keep C05, but the cancelled sign before Y must not be silently turned into a live universal quantifier; the intended universal centrality is an interpretation of the sentence's scope. A six-element countermodel shows that it is not a consequence of the abstract axioms 1–7. |
| SF-03 | 039, NB after part a | “Il suffit de voir ce qui se passe … en un … a …” followed by dots | Keep the unfinished endpoint argument as an **unproved claim/proof sketch**, correcting C05's classification if “unverified” means an explicit doubt. The page does not say “à vérifier”, and the surrounding argument does assert the result; its general validity nevertheless needs hypotheses. |
| SF-04 | 041, final paragraph | “J'ai commencé à faire l'exercice”; “de l'expliciter jusqu'au bout” | Keep C05: he explicitly leaves the full characterization unwritten. Recovering order from cut data in a known model and recognizing which abstract cut data come from such a model are distinct tasks. |
| SF-05 | 041, final paragraph | “Ça doit avoir été fait depuis longtemps (Hilbert ?)” | Keep C05 as a questioned historical attribution, not a proof or an identification of a specific theorem. The insertion “(et divisible)” matters to the reconstruction argument; the cited literature in S3 remains an unchecked lead in this run. |

The additional proof obligations “Immédiat” (028), injectivity (030), the unproved list 1–8 (033–034), and the finite subdivision assertion (040) are recorded in the page notes. They are not additional author-written expressions of doubt. Likewise, `\unsure{…}` in the transcription is editorial uncertainty about ink and must not be mistaken for a manuscript question mark.

### Exhaustive check of witness C's non-tabular remarks

| Witness C item | Verdict | Reason in the consolidated text |
|---|---|---|
| C04: one unverified step on scan 032 | Keep, with SF-01's distinction | The question and three question marks remain in the margin. No further explicit mathematical reservation was found on 026–033; the pages do contain claims without proof. |
| C05: scan 037 expectation | Keep | SF-02 retains both the expectation and its conditional sequel; its mathematical status is checked separately. |
| C05: scan 039 ellipsis | Correct classification | SF-03 is an incomplete endpoint proof, not an explicit “I am unsure” statement. |
| C05: scan 041 exercise left unfinished | Keep | SF-04. |
| C05: scan 041 Hilbert attribution questioned | Keep | SF-05. |
| C05: scans 034, 035, 040 have no explicit reservation | Keep | This does not certify their formulas or consequences; 034 has a cancelled NB and 035/040 contain literal expressions requiring mathematical qualification. |
| C05: the proof introduced on 036 ends with “OK.” | Correct scope | Several local “OK”s occur, but the proof of all seven relative axioms continues through 037:1–11 and ends there with an underlined “OK”. |
| C05: the two tasks on 038 are taken up on 039 | Keep | They are relative clopenness and connectedness. |
| C05: part a ends with “C'est immédiat” | Keep, qualify completeness | Those words occur, followed by the NB whose endpoint reasoning is not completed; a slogan of immediacy is not a separately supplied proof. |

## Standing question 2: titles, dates, folios, and page counts

There is **no separate title sheet, written date, or stated total page count in scans 026–041**. The numerals 25–40 are individual manuscript folios; they are not a sixteen-page extent statement written by the author. The package title and its date 8 June 1986 are catalogue/context metadata, not a date newly read on these sixteen leaves.

| Scan | Manuscript folio | Other inscription relevant to C's notes | C item verdict |
|---|---:|---|---|
| 026 | 25 | “Tronçons” / “Tronçon”, with final-s uncertainty | Keep C04's folio and heading doubt; this is an internal paragraph heading. |
| 027 | 26 | No independent title/date/extent statement | Keep C04. |
| 028 | 27 | Underlined “Prop” | Keep C04; a proposition label, not a document title. |
| 029 | 28 | Underlined “psTronçon interstitiel” | Keep C04 with the consolidated capitalization. |
| 030 | 29 | Crossed-out “Définition” | Keep C04; record the deletion state. |
| 031 | 30 | No independent title/date/extent statement | Keep C04. |
| 032 | 31 | Underlined “Propriétés” at the foot | Keep C04. |
| 033 | 32 | No independent title/date/extent statement | Keep C04. |
| 034 | 33 | No independent title/date/extent statement | Keep C05. |
| 035 | 34 | No independent title/date/extent statement | Keep C05. |
| 036 | 35 | No independent title/date/extent statement | Keep C05. |
| 037 | 36 | Underlined “Composantes” | Keep C05's separate heading item as well as the folio. |
| 038 | 37 | No independent title/date/extent statement | Keep C05. |
| 039 | 38 | No independent title/date/extent statement | Keep C05. |
| 040 | 39 | No independent title/date/extent statement | Keep C05. |
| 041 | 40 | “Caractérisation d'un intervalle ordonné, en … que réseau”; cancelled “réseau-interval” and “tant” | Keep C05's heading, specifying both cancellations instead of silently restoring ordinary French. |

Both of C's concluding “none” statements about separate title sheets, dates, and total counts are retained. Nothing has been dropped merely because it is a folio rather than a title: the table preserves every C04/C05 title/folio item, while explaining the distinction.

## Contextual notes beyond a single page

### CTX-01 — Scans 030–034; unpursued implication / terminology comparison

**Anchor:** “modérés”; “Mod fer”. **Context:** S7 §2.3, reporting 156-7/071; S3 §3 and correction SA21-K3-01. **RS:** no entry establishes this local terminological history; thematic relation to WG2 §3.1 #2.

S7 reports the author's later proposal to call the present closed moderate sets “modérées” and the present moderate sets “constructibles”; that **differs from** the vocabulary of the frozen pages without invalidating their local definitions. It is a later renaming, not a withdrawal within scans 026–041, and the image of 156-7/071 was not supplied here. The distinction helps compare the present Boolean operations with later closed supports, but it does not license replacing either word in the transcription.

### CTX-02 — Scans 033–040; own idea / comparison with later supports

**Anchor:** “alg. de Boole”; “S'il en est ainsi”. **Context:** S7 §§2.2–2.3, reporting 156-7/062–084; ST §2.5, reporting 156-4/066–069. **RS:** thematic WG2 §3.1 #2; no RS theorem identifies these particular partial algebras. **Confidence:** high for the structural comparison, limited for the later manuscripts' uninspected ink; the reason is the explicitly checked six-element model.

The horizontal sum countermodel to the scan-037 expectation has the same six-element ordered/complemented structure that S7 calls MO₂ in its support counterexample. This **adds** an early local obstruction to the context's later concern about distributivity: Boolean behavior inside each compatible family does not imply one Boolean algebra containing every clopen or support. It does not re-prove S7's assertion that its example satisfies every later atelier axiom; that is a different verification with additional data.

### CTX-03 — Scans 030, 040–041; unpursued implication / register comparison

**Anchor:** “drapeaux”; “subdivision”; “en … que réseau”. **Context:** E §5, scans 119/036–037, on Drap(I), local retractions, embeddings, and proper fibrations. **RS:** MPL_121_049-073+153+155 R121-08; MPL_150_044-084 N18 and N35; EXIT_ONE_TYPE P4e.

These pages **add** a concrete one-dimensional cut model to the Esquisse's flag-indexed reconstruction programme, but their use of the same word *drapeau* does not identify the constructions. E's flags carry spaces and gluing maps, whereas F 030 uses a finite chain of separated pieces to specify a subset, and F 041 retains actual equivalence classes of cuts on a fixed set of lieux. The cited RS leads and P4e warn against replacing all attachment and link information by bare incidence; this packet supplies no comparison functor to the registered exit constructions.

### CTX-04 — Scans 034, 040; unpursued implication / bounded comparison with tame theories

**Anchor:** “dim 1”; “subdivision”. **Context:** E §5, scans 119/032–034, and §6, scan 119/042. **RS:** MPL_150_001-043 Q4b; MPL_151_032-075 Q4-02 and Q4-03; MPL_121_001-048 Q4.2 and Q4.3; MPL_150_044-084 T05.

The finite endpoint description **adds** an elementary one-dimensional model of tameness, whereas E asks for stability and comparison statements for spaces and mapping spaces in all dimensions. Nothing in F 026–041 proves triangulation, the compact Hauptvermutung, a simple-homotopy comparison, or an equivalence of isotopy categories. The RS items are bibliographic and research leads concerning those stronger comparisons; their theorem locators were not externally verified in this no-external-research task.

### CTX-05 — Scans 030, 038–040; unpursued implication / variance and realization warning

**Anchor:** “mais pas pour la top canonique”; “composantes connexes”. **Context:** E §5, scan 119/041, separating π₀ from full homotopy types. **RS:** STRATA 0.1, A.4, A.12; BISITE G.10; PATHS E.10; STRATA F.3.

The explicit warning on scan 030 **differs from** the geometric connectedness and exit hypotheses in the register: a rational interval can be one tame component while its order-topological connected components are singletons. Consequently no passage from the present cut classes to geometric exit paths follows simply by naming them components, and the finite-poset dictionary's variance conventions must be fixed before attempting such a passage. The RS statements are carried as background rather than re-proved; this comparison supplies no new proof of their general assertions.

### CTX-06 — Scans 035–037; unpursued implication / relative constructions

**Anchor:** “relativiser”; “fermés dans A”. **Context:** E §5, scans 119/035–036, discussing relative neighborhoods and reconstruction with extra structures. **RS:** STRATA D.2; BISITE F.9; RESIDUE J.2 and J.3.

The formulas for the relative complement and closure **add** a precise elementary restriction mechanism, but it is an operation in a partially Boolean ordered set, not an open–closed recollement of categories. Thus the similarity with the registered open–closed formalism is a structural analogy, and the scans do not settle the missing lax-comma or base-change statements in RESIDUE J.2/J.3. This negative scope conclusion prevents a terminological connection from being reported as progress on those open results.

## Relation to all nine open RS entries

| RS open item | Bearing of these sixteen scans |
|---|---|
| LM4 C.12 | No operator-group action or centralizer comparison occurs here; component language alone gives no information about its level-zero kernel. |
| RESIDUE E.6 | No relative-category comparison map J or all-endpoint stabilization theorem is constructed; cut reconstruction is a different problem. |
| EXIT_ONE_TYPE P3c-general | No threefold, normal-crossing completion, or stratal zigzag is considered. |
| PATHS C.10 | No pointed ind-category or stabilized full-path construction occurs. |
| RESIDUE C.8 | The six-element partial Boolean countermodel is not a category-with-pullbacks example for the register's minimum problem. |
| RESIDUE F.6 | No total presheaf or composition of the stated sieves is considered. |
| RESIDUE I.7 | No accessible-localizer classification or operation on all derivators is provided. |
| RESIDUE J.2 | CTX-06 records only an analogy; there is no walking-2-cell recognition theorem here. |
| RESIDUE J.3 | CTX-06 records only an analogy; no universal pullback-preservation or lax-comma base-change theorem is checked here. |

The relevant positive planning connection is **WG2 B15 (§1.2)**: finite quotients from cuts may be useful test objects for its passage from finite posets to the real line. An inverse-system proposal, without a specified category, bonding maps, topology, and comparison theorem, is not a solution of B15.
