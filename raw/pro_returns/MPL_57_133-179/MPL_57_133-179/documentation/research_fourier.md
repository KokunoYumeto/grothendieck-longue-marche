# Fourier witness research memo

Research owner: /root/fourier_witness_research. Date: 2026-11-18. The transcription was already frozen at 2026-11-18 08:54:59 UTC when this subtask began. This memo changes no transcription, scan reading, main note, or main check-event register.

## Result and scope

**No second manuscript witness completing cote 47's compatibility check was identified in the frozen current package.** The relevant current material is about a generalized-Jacobian torsor, its Kummer boundary, and descent of line bundles; it contains another expressly unfinished comparison, not the Poincaré direct-image comparison of cote 47. This is a bounded documentary conclusion about the supplied current text and the comparisons actually made here, not a statement about the whole Montpellier archive.

The task's exact RESULTS_STATE entry is **WG2 §2.4 #4**, under **“Questions of our planning document (the war game) for these folders”**: the question about a second witness of 47 with its compatibility check completed. **WG2 §1.1 #3** supplies the broader Picard/abelian-variety orientation. These are planning entries, not theorem IDs; the separate heading **“Orientation for this package (curated 17 Nov 2026 by Claude Opus 5.5 at effort max from our records; leads, unrefereed)”** explicitly says **“Our results to use and check: none for this cote.”** No direct theorem in that register settles the Fourier carry-question.

### Source keys and checks made

| Key | Actual source and checked location | Status retained |
| --- | --- | --- |
| P57 | Frozen pages/MPL_57_133-179_57_scanNNN.tex, particularly scans 142, 144, 145, 173, 174, 178, 179; all 43 page files searched for Fourier, Poincaré, convolution, compatibility, torsor and Kummer terminology | Current frozen transcription; this subtask did not reopen scans |
| CT | context/MPL_16+47+54+44_transcription.tex, cote 47 scans 3–11, especially scans 6–8 | Supplied previous transcription, not independently checked against its images here |
| CN | context/MPL_16+47+54+44_notes.md, section “Fourier transforms, determinant lines, and Chern coefficients,” F1–F9, especially F4 and F7–F8 | Previous run's claims and leads |
| RS | context/notes/RESULTS_STATE.md, read in full before preparing these notes | Status distinctions preserved |
| SN | context/same_cote_57/MPL_57_271-315_notes.md, section 1, F01–F03 | Earlier package's unreviewed research; its underlying scans were not supplied or checked here |
| HUA | context/hua_project/57.modern.tex, “Une obstruction pour une courbe épointée (pages 141 à 144),” lines 1753–1783; its README read first | Michel Hua's project's AI-produced interpretation, not another manuscript witness; only this subsection was compared in this subtask |
| L96 | Laumon, Transformation de Fourier généralisée (1996), §1.1 and printed p. 5, Theorem 1.2.4 and Lemma 1.2.5, https://arxiv.org/pdf/alg-geom/9603004 | Primary comparator; statement and proof-paragraph scope checked |

The Oda PDF was not used in this Fourier subtask; this memo makes no claim about the full contents of that work. Searching the current page files produced no Fourier, Poincaré or convolution passage; the term Weil at 57:149 belongs to a cohomology theory, and the other compatibility hits concern descent or different operations. The negative answer rests on this targeted search together with the explicit comparison of the pertinent current Picard passages and cote 47's actual map, rather than an archive-wide absence claim.

## Candidate notes for the main research notes

Each candidate below has one to four discussion sentences. The identifiers FW01–FW07 are proposed local IDs for this memo; the root agent may renumber them when incorporating them in the main notes.

### FW01 — The missing Fourier verification concerns one particular derived map

**Kind:** unpursued implication; bounded documentary comparison.  
**Current locator and short quote:** P57, 57:144:L21–32, “à vérifier ......”; 57:173:L6–29, “monomorphisme”; 57:179:L5, “une obstruction”.  
**RESULTS_STATE:** WG2 §2.4 #4; WG2 §1.1 #3; planning/orientation entries only, no direct theorem ID.  
**Context:** CT, 47:6–8, especially whole-file TeX lines 2296–2304, 2333–2393; CN F7–F8; SN F01, as an unchecked earlier comparison.

Cote 47:7 constructs the specific morphism \(c:\mathbf Rp_*W\longrightarrow e_*\tau_{B^\vee}[-n]\), using top-degree base change and \(R^nq_*\mathcal O_B\simeq\bigwedge^nR^1q_*\mathcal O_B\simeq\tau_{B^\vee}\), and 47:8 leaves its derived restriction at a zero-section point with “à faire une vérification de compatibilité.....”. In this formulation, the required check is that \(\mathbf Li_{e(s)}^*c\) is an isomorphism, after reduction to an algebraically closed field; the admitted vanishing lemma only treats points off the zero section. This is the lemma needed for the anti-diagonal composition kernel at 47:6 and the inversion-and-shift formula at 47:5, rather than merely an equality of dimensions or an assertion that a Picard object exists. The current torsor and descent passages do not supply that map or its verification, so this package adds no identified completed second witness for WG2 §2.4 #4.

### FW02 — The current “à vérifier” is a Kummer-boundary comparison

**Kind:** unproved claim of the manuscript; interpretation compared with a credited prior project.  
**Current locator and short quote:** P57, 57:142:L12–18, L27–45; 57:144:L9–32, “torseur canonique” and “à vérifier ......”; 57:145:L3–7.  
**RESULTS_STATE:** WG2 §2.4 #4 and WG2 §1.1 #3; no direct theorem ID for this comparison.  
**Context:** CT, 47:3 and 47:6–8; HUA, “Une obstruction pour une courbe épointée (pages 141 à 144),” lines 1753–1783.

The current construction gives \(E=\operatorname{Pic}^0_{Z/S}\), a degree-one torsor \(P=\operatorname{Pic}^1_{Z/S}\) with class \(\eta\in H^1(S,E)\), and the proposed identity \(\xi_n=\delta_n(\eta)\) in \(H^2(S,E[n])\), with \(\delta_n\) the boundary for multiplication by \(n\). Here \(P\) denotes a torsor, while the Fourier argument uses a Poincaré/Weil line bundle on a product of dual abelian schemes; neither the objects nor the comparison maps are the same. Michel Hua's modernised reading, in the cited subsection, correctly preserves the manuscript's explicit unfinished status, and its numbering 141–144 corresponds here to scans 142–145. The useful connection is through Picard objects and their descent data, but the source does not identify this Kummer class with the Fourier comparison or prove either missing compatibility.

### FW03 — Rigidification is a positive link to the Poincaré kernel

**Kind:** unpursued implication.  
**Current locator and short quote:** P57, 57:173:L25–29; 57:174:L7–19, “tout automorphisme ... est trivial”; 57:178:L5–13; 57:179:L3–5, “à valeurs dans un \(H^2(S,\mathbf G_m)\)”.  
**RESULTS_STATE:** WG2 §1.1 #3; WG2 §2.4 #4; planning entries only, no direct theorem ID.  
**Context:** CT, 47:3, especially whole-file TeX lines 2086–2098 and 2142–2150; 47:6–8; CN F1.

The current sheets distinguish actual line bundles modulo pullback from the base, their locally defined classes, and the flat-descent Picard functor, and they isolate rigidification along a section as a way to remove line-bundle automorphisms. Cote 47:3 uses precisely a rigidified, fibrewise algebraically trivial line bundle and its classification by a map to the dual abelian scheme, so the current discussion explains part of the foundational input needed to specify that kernel canonically. The \(H^2(S,\mathbf G_m)\) obstruction discussed at 57:174 and 179 belongs to realizing or descending Picard classes as line bundles; it is not the \(H^2(S,E[n])\) boundary at 57:144. These are genuine Picard-theoretic connections, without a construction here of the derived direct-image comparison at 47:7–8.

### FW04 — The earlier proof plan and exterior-power calculation do not complete the map check

**Kind:** status clarification of supplied earlier research; no new theorem claim.  
**Current locator and short quote:** P57, 57:144:L21–32, “à vérifier ......”; 57:174:L17–19, “déterminé à isom. unique près”.  
**RESULTS_STATE:** WG2 §2.4 #4; exact planning heading identified above; no direct theorem ID.  
**Context:** CN F7 and F8; CT, 47:7–8, whole-file TeX lines 2350–2393; SN F01, only as a lead.

CN F7 proposes testing the cone of the Fourier comparison on derived residue-field fibres, and CN F8 computes the cohomology of the derived restriction of its proposed target as \(\bigwedge^{n-i}T^\vee\otimes\det T\simeq\bigwedge^iT\), where \(T=\operatorname{Lie}(B^\vee)\). F8 expressly stops short of proving that the actual morphism from 47:7 induces those identifications, so neither earlier note may be promoted to a checked completion of the author's missing step. The present notes on uniqueness of rigidified line bundles concern a different category and do not supply the omitted comparison on all fibre cohomology groups.

### FW05 — A small complex shows why dimensions and a top-degree identity are insufficient

**Kind:** own idea; elementary diagnostic calculation.  
**Current locator and short quote:** P57, 57:144:L23–25, the boxed identity followed by “à vérifier ......”; the point is to preserve, not erase, the distinction between an asserted comparison and its verification.  
**RESULTS_STATE:** WG2 §2.4 #4; no direct theorem ID; relates to CN F7–F8 rather than a registered theorem.  
**Context:** CT, 47:7–8; CN F8, “top cohomology and derived restriction to the unit.”  
**Editorial confidence:** high for the explicit algebra calculation; it is a diagnostic example, not a model asserted to be the Poincaré direct image.

Over \(R=k[[x]]\), let \(K=[R\xrightarrow{x^2}R]\) and \(Q=[R\xrightarrow{x}R]\), both in degrees 0 and 1, with chain map \(c=(x,1):K\to Q\). The chain condition is \(x\cdot x=x^2\), and after tensoring with the residue field both differentials vanish, so source and target have identical one-dimensional cohomology in each degree while \(c\) induces \(0\) in degree 0 and \(1\) in degree 1. Thus an identity in top-degree fibre cohomology and matching dimensions in all degrees still do not make the given map an isomorphism. This confirms the precise logical limitation of using CN F8 alone and says nothing against the actual Fourier theorem.

### FW06 — The two-row obstruction setup needs nonempty boundary fibres

**Kind:** own idea; hypothesis check, with an explicit degenerate test.  
**Current locator and short quote:** P57, 57:142:L12–19, “0 sauf si \(q=1,2\)”; 57:145:L9–11, “si \(Y\longrightarrow S\) surjectif”.  
**RESULTS_STATE:** WG2 §1.1 #3; WG2 §2.4 #4 only as a boundary on the comparison; no direct theorem ID.  
**Context:** HUA, “Une obstruction pour une courbe épointée (pages 141 à 144),” compared with the explicit surjectivity insertion in P57; CT, 47:7–8 as the separate Fourier problem.  
**Editorial confidence:** high for the degenerate-fibre test; no general proof of \(\xi_n=\delta_n(\eta)\) is claimed.

The assertion that only \(R^1_!\) and \(R^2_!\) survive requires the puncture set to be nonempty on every geometric fibre: if \(Y=\varnothing\) over a geometric point and \(n>1\) is invertible, then \(U=X\) is proper and connected, so \(H_c^0(X,\mu_n)=H^0(X,\mu_n)=\mu_n\ne0\). The manuscript's later insertion “si \(Y\longrightarrow S\) surjectif” supplies the corresponding nondegeneracy condition for its torus sequence and should also be retained when stating the two-row setup. This correction of scope neither proves the boxed Kummer comparison nor contributes the unit-section check of cote 47.

### FW07 — A primary comparator states the theorem but abbreviates this proof

**Kind:** primary-reference and proof-scope check.  
**Current locator and short quote:** P57, 57:144:L25, “à vérifier ......”; compare the separate unfinished step of CT, 47:8.  
**RESULTS_STATE:** WG2 §2.4 #4; planning entry only, no direct theorem ID.  
**Context:** CN F4; CT, 47:5–8; L96, §1.1 and printed p. 5, Theorem 1.2.4 and Lemma 1.2.5.

Laumon’s stated relative theorem has the required normalization, but the inspected proof paragraph gives only the map’s construction. The reference therefore supplies a comparator, not a second manuscript witness or a detailed fibre-compatibility proof checked in this run.

## What a positive answer would have to contain

A successful second-witness claim should point to a different manuscript passage constructing or identifying the same Poincaré direct-image map, and show its derived restriction at the unit to be an isomorphism with the shift and determinant line retained. It would not be enough to find the words “compatibility,” “Picard,” or “Poincaré”; an existence theorem for a Picard scheme, a torus extension, the vanishing away from the identity, or a comparison of vector-space dimensions has a different logical role. The present current pages leave the Kummer comparison open and give useful rigidification/descent context, but do not satisfy that positive criterion.

## Proposed CHECK_EVENTS.tsv chunk

This is a proposal for the root agent's main register, not an edit to it. The documentary checks below are explicitly limited to text and attribution; they are not recorded as independent proofs of the manuscript's theorems. Rows about prior notes concern their stated scope, not a second pass on their source scans.

~~~tsv
statement_id	date	who	type	outcome
WG2 §2.4 #4	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	carried as background without fault found	Planning question used to orient the comparison; no direct theorem ID in RESULTS_STATE settles it.
WG2 §1.1 #3	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	carried as background without fault found	Picard and abelian-variety orientation used; no archive-wide or theorem-level conclusion drawn.
FW01; CT 47:7–8	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	used and rechecked in this run	Documentary comparison of CT TeX2350–2393 with current57:142,144–145,173–174,178–179 and targeted search of all current page files identified no completed second witness; no proof of the Fourier theorem claimed and no source scans reopened.
FW02; P57 57:144:L9–32	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	used and rechecked in this run	Compared the actual torsor, cohomology groups, multiplication-by-n boundary and explicit unfinished flag with CT47:6–8; verified these are different comparison problems, without proving either identity.
HUA Une obstruction pour une courbe épointée; FW02	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	used and rechecked in this run	Localized textual comparison of Hua's credited subsection with frozen57:142,144–145 confirms it retains the à vérifier flag; not a proof check of Hua's full cote interpretation.
FW03; P57 57:173–174,178–179	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	used and rechecked in this run	Compared rigidification and Picard-descent objects with CT47:3 and separated the G_m obstruction from the E[n] Kummer boundary; documentary and type comparison only.
CN F7; FW04	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	carried as background without fault found	Read and used as an explicitly labelled proof plan; the missing induced maps at the unit were not checked in this run.
CN F8; FW04	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	carried as background without fault found	Read and used only as an object-level exterior-power calculation with its stated limitation; no completion of the actual comparison map is attributed to it.
FW05	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	targeted proof check	Checked the chain equation for (x,1):[R--x²→R]→[R--x→R] and residue-fibre maps (0,1); equal dimensions and a top-degree identity do not imply that this map is an isomorphism.
FW06	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	targeted proof check	Tested the missing-boundary case over a geometric point: for n>1 invertible, Y empty gives H_c⁰(X,μ_n)=μ_n≠0; this bounds the stated two-row assertion but does not verify the Kummer comparison.
CN F4; FW07; Laumon 1996 Lemma 1.2.5	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	used and rechecked in this run	Primary-reference scope inspected; see FW07 in the final notes; no independent re-proof or second manuscript witness.
SN F01–F03	2026-11-18	GPT-6 Astra Pro; effort inherited, not separately stated; MPL_57_133-179/fourier_witness_research	carried as background without fault found	Used only as earlier bounded comparisons and leads; scans 271–315 and their mathematical claims were not checked in this subtask.
~~~

## Exact reference for the primary comparator

Laumon, G. (1996). *Transformation de Fourier généralisée*. arXiv:alg-geom/9603004, §1.1, Theorem 1.2.4 and Lemma 1.2.5, printed pp. 2–5. [Primary PDF](https://arxiv.org/pdf/alg-geom/9603004).

The base hypotheses occur at the beginning of §1.1 on printed p. 2; the theorem, lemma and abbreviated proof occur on printed p. 5. The stable primary URL above permits those passages to be checked independently.
