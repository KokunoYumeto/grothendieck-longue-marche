# Research notes: plans, chapter assignments, titles and pagination

These notes use the frozen transcription and the supplied context. No page file or combined transcription was edited during this research. Context quotations and locators refer to the supplied textual edition; its `oldpage` numbers are printed EGA page numbers, while `22/020` and similar locators mean archive cote/scan. The exact searches are recorded in `research_plans_searches.txt`.

## P01. The available plan witnesses

**Kind: reading question — which plan is actually witnessed? Location: 22/019–021, headings and question numbers; 23/002–003 and 008–009, titles.** The 44 pages carry “Questions,” “Questions ouvertes,” “EGA IV, Calcul diff. (Compléments),” “Discriminant etc,” and “Exponentielle,” together with the local statement numbers in the algebra text; their chapter evidence is the explicit “IV” on 23/002 and the internal references to Chapters III and IV on 22/010 and 021. A chapter-by-chapter treatise plan is supplied by `context/ega_fr/EGA_I_introduction_plan_of_the_treatise.tex`, printed p. 6, while the README only names the other witnesses “CSG U90d,” cotes 26 and 48, without supplying their texts. The side-by-side comparison therefore has one complete numbered column here, with the other columns recorded as unavailable rather than reconstructed from the subject matter. **Context / state:** `context/README.md`, “What our planning document asks”; `RESULTS_STATE.md`, **WG2 §2.1 #2** [unchecked planning item], whose quoted extract supplies no additional complete chapter list; no matching settled register entry.

## P02. The thirteen chapters announced in EGA I

**Kind: reading question — exact chapter numbering. Location: current package 23/002, title “EGA IV”; comparison witness: EGA I introduction, printed p. 6.** The following is the complete list in the supplied EGA I witness; **1960** is the shared date given for that plan in the prompt and README, rather than thirteen separately dated inscriptions. The source explicitly calls the plan “sujet à modifications ultérieures” and treats chapters as open to later additions, so the list supplies a dated comparison witness for subsequent archive plans. **Context / state:** `context/ega_fr/EGA_I_introduction_plan_of_the_treatise.tex`, printed p. 6, paragraph “A titre informatif” and following table; **WG2 §2.1 #2** [unchecked plan], with no settled numbering concordance in the supplied state register.

| Chapter number in the 1960 witness | Exact title in the supplied French text | Plan date | Number/title in the 44 current pages |
|---|---|---:|---|
| Premier / I | Le langage des schémas. | 1960 | No corresponding chapter-list entry on these sheets |
| II | Étude globale élémentaire de quelques classes de morphismes. | 1960 | No corresponding chapter-list entry on these sheets |
| III | Cohomologie des faisceaux algébriques cohérents. Applications. | 1960 | Internal “Chap III” reference on 22/010 |
| IV | Étude locale des morphismes. | 1960 | Cover: “EGA IV, Calcul diff. (Compléments)” on 23/002; “Cf IV” reference on 22/021 |
| V | Procédés élémentaires de construction de schémas. | 1960 | No chapter-list entry on these sheets |
| VI | Technique de descente. Méthode générale de construction des schémas. | 1960 | No chapter-list entry on these sheets |
| VII | Schémas de groupes, espaces fibrés principaux. | 1960 | No chapter-list entry on these sheets |
| VIII | Étude différentielle des espaces fibrés. | 1960 | No chapter-list entry on these sheets |
| IX | Le groupe fondamental. | 1960 | No chapter-list entry on these sheets |
| X | Résidus et dualité. | 1960 | No chapter-list entry on these sheets |
| XI | Théories d'intersection, classes de Chern, théorème de Riemann-Roch. | 1960 | No chapter-list entry on these sheets |
| XII | Schémas abéliens et schémas de Picard. | 1960 | No chapter-list entry on these sheets |
| XIII | Cohomologie de Weil. | 1960 | No chapter-list entry on these sheets |

The twelve-chapter **CSG U90d** list, the chapter lists in **cotes 26 and 48**, and their dates remain untranscribed comparison columns because those witnesses are absent from both supplied archives; the README's reported cardinalities alone cannot specify a permutation or a merger of named chapters.

## P03. Subjects after IV: what this package actually contributes

These are chapter-assignment reading notes, each tied to a visible formula or stated question. The chapter titles are the 1960 titles above. The local question list appears separately in P04, because its author does not assign those four questions to numbered Chapters V–XIII.

| Note / kind | Chapter and planned subject from the 1960 witness | Current page evidence and explicit connection | Context locator; state linkage |
|---|---|---|---|
| P03-V — reading question | V: elementary construction of schemes | 23/004 begins “\(P=P(E)\) fibré projectif associé” and constructs \(J\) from maps \(g^*(M_d)(-d)\to J\), followed by \(\coprod f^*(M_d)(-d)\xrightarrow{\sim}J/J^2\); 23/006 uses the section \(\varphi:S\to\Phi^k(P^r)\) and its hypersurface. These are concrete projective construction data for comparison, while the cover places this material under “EGA IV.” | EGA I introduction p. 6, V; `ega2-indexes-and-contents-fr.tex`, II §§2–4, especially 3.6 and 4.1–4.4, printed pp. 213–214. `RESULTS_STATE`: **WG2 §2.1 #2**, unchecked planning status. |
| P03-VI — reading question | VI: descent and general construction methods | 22/018, lower paragraph, asks to “se ramener à ce cas … par descente comme dans 4.11,” after constructing a complete \(B\) with a prescribed special fibre \(B_0\); the comparison object is the local map \(A\to B\) and the isomorphism of its reduction with \(B_0\). This supplies a specific descent passage to collate with the planned construction chapter. | EGA I introduction pp. 6, 8–9; `EGA_chap0_ega0-19.tex`, 19.0.2 III and 19.7.2. **MPL_131 10** [first-pass lead] reports descent/representable functors in a separate package, whose full note and scans are not included; **WG2 §2.1 #2** remains an unchecked plan. |
| P03-VII — reading question | VII: group schemes and principal bundles | 23/013 writes \(\pi_0(U\otimes\Lambda)\underset{\log}{\stackrel{\exp}{\rightleftarrows}}\gamma_0(U\otimes_k\Lambda)\), and 23/016 states the infinitesimal automorphism/derivation correspondence for \(A\otimes_k\Lambda\), with the group law given by “Hausdorff-Campbell.” These explicit maps provide the package's group-theoretic link; 23/013 also writes the marginal “Cor Un groupe alg. en car 0 … toujours lisse,” with its reading doubts preserved. | EGA I introduction p. 6, VII; `EGA_chap0_ega0-20.tex`, 20.1–20.3 on derivations and their functorial/topological properties. State register has no settled item about this exponential construction. |
| P03-VIII — reading question | VIII: differential study of fibre spaces | 23/004 gives the Euler sequence \(0\to\Omega^1_{P/S}\to g^*E(-1)\to O_P\to0\), then the conormal map \(J/J^2\to\Omega^1_{P/S}\otimes O_X\) and its determinant isomorphism; 23/005 carries the calculation to an elliptic cubic. This is direct differential material on the displayed projective bundle \(P(E)\to S\). | EGA I introduction p. 6, VIII; `ega4-backmatter-contents-fr.tex`, IV 16.1–16.6 and 17.12, printed pp. 341–342; `EGA_chap0_ega0-20.tex`, 20.5. No matching settled register item. |
| P03-IX — reading question | IX: fundamental group | The current titles and numbered questions provide no chapter-IX programme, covering-space construction, or fundamental-group calculation; the nearest supplied context is the introduction's explicit use of Chapter IX as an example of formal-to-algebraic methods. The retained evidence is thus the local-ring/formal-method discussion on 22/010–018, without assigning it an unwritten Chapter IX heading. | EGA I introduction pp. 6, 8–9; `ega4-backmatter-contents-fr.tex`, IV 18.1–18.3 “Revêtements étales” and “Algèbres finies et étales,” printed p. 342. **MPL_142_001-093 §316** is only a first-pass bibliography lead in the supplied state register. |
| P03-X — reading question | X: residues and duality | 23/004–005 records the determinant isomorphism relating \(\Omega^n_{X/S}\), \(\bigwedge^p(J/J^2)\), and \(f^*(\bigwedge^{r+1}E)(-r-1)\); 22/028 and 030 provide trace/norm maps on répartitions, idèles and divisors, including \(D'(N(I))=N(D(I))\). Those displayed morphisms and identities give precise comparison points for the planned “Résidus et dualité,” while these sheets do not label them as a Chapter X plan. | EGA I introduction p. 6, X; `ega2-indexes-and-contents-fr.tex`, II 6.4–6.5; `ega4-backmatter-contents-fr.tex`, IV 21.4–21.5 and 21.9–21.10, printed p. 343. No matching settled register item. |
| P03-XI — reading question | XI: intersections, Chern classes and Riemann–Roch | The words “intersection complète” on 23/004 are accompanied by the map from the graded generators to \(J/J^2\), and 23/005 computes its top exterior power with twist \(-\sum\alpha_i d_i\). This supplies an explicit conormal/determinant calculation for comparison with the planned intersection subject; the current pages supply no Chern-class or Riemann–Roch statement. | EGA I introduction p. 6, XI; `ega4-backmatter-contents-fr.tex`, IV 19.1–19.3, printed p. 342; `EGA_chap0_ega0-16.tex`, regular sequences, and `EGA_chap0_ega0-20.tex`, 20.5. No matching settled register item. |
| P03-XII — reading question | XII: abelian schemes and Picard schemes | 23/005, lower half, names a “courbe elliptique lisse sur S” and ends with \(M\xrightarrow{\sim}\mathcal L^{\otimes6}\); the preceding displayed isomorphism \(\check{\mathcal L}\xrightarrow{\sim}\mathcal L^{\otimes5}\otimes\check M\) is the concrete link to its line-bundle calculation. The supplied material reaches this elliptic example and does not provide a representability statement for a Picard functor. | EGA I introduction p. 6, XII; `ega2-indexes-and-contents-fr.tex`, II 4.1–4.4, projective bundles; IV contents 21.2–21.3, invertible fractional ideals and linear equivalence. No matching settled register item. |
| P03-XIII — reading question | XIII: Weil cohomology; the request also asks about étale cohomology | The exact announced title is “Cohomologie de Weil,” and the introduction p. 9 describes its motivation through Weil's conjectures; the 44 current sheets supply no chapter-XIII outline or étale-cohomology construction. The supplied IV contents list étale morphisms and étale coverings (17.1–18.3), which provides a documented adjacent heading without changing the 1960 chapter title. | EGA I introduction pp. 6, 9; `ega4-backmatter-contents-fr.tex`, IV 17–18, printed pp. 341–342. **MPL_147_138-190 §143** [first-pass bibliography lead] names SGA 4, but its full research note is absent here. |

## P04. The open problems actually listed

**Kind: conjecture / question inventory. Location: 22/020–021, numbered 1–4, heading “Questions ouvertes.”** The four explicit questions ask about (1) formal simplicity and universal regularity for noetherian local algebras/local maps, (2) passage from the habitual to the discrete topology, (3) openness of the fibrewise formally simple locus, with a related localisation question, and (4) openness of the flat locus of a noetherian ring map. The list carries its own qualifications and later annotations, including “OK” by (1), the positive/zero-characteristic expectation in (2), “bons anneaux” in (3), and the generic-flatness reduction written under (4); their exact wording and uncertain margin attachment must govern any resolution claim. **Context / state:** `EGA_chap0_ega0-19.tex`, 19.0.2 and 19.7; `EGA_chap0_ega0-22.tex`, 22.5.8 and introduction; IV contents 17.5, 17.8 and 17.14; **WG2 §2.1 #2** [unchecked plan] is answered by this actual question inventory, while the three Hua entries in `RESULTS_STATE.md` attach specifically to the later 22/023–029 developments.

## P05. Limits of the requested archive-wide comparison

**Kind: reading question — missing witnesses. Location: current 22/018 “par descente”; 23/002 “Compléments”; context README planning list.** Cotes 127 and 128, Deligne's notes, cote 91, and the open list in cote 26 are not part of these 44 pages or the supplied context files; the current source therefore supplies no textual basis for reporting their statements, proof lengths, chapter assignments or dates. The particular descent passage on 22/018 and the projective maps on 23/004–006 are the concrete evidence that this package adds to the broader planning question. **Context / state:** `README.md`, “What our planning document asks,” including “127 and 128,” “Hom functors by non-projective methods (91),” and “what 26 lists as open”; **MPL_131 10** [first-pass lead] and **WG2 §2.1 #2** [unchecked planning item], with no matching settled register entry.

## P06. Title sheets, source headings and stated lengths

**Kind: reading question — title and extent inventory.** Every title below is quoted from the frozen source; dates in the date column come from the identified inscriptions, while “undated” reports the absence of a date on that title sheet. The observed scan runs are counts of the retained material, and the page labels are reported in P07. **Context / state:** compare `README.md`, “This package in our plan”; **MPL_33_147-181+34_002-017 8.3** [first-pass lead] likewise distinguishes manuscript numerals from a total count, but the underlying source and full note are not included here.

| Cote / scan and approximate position | Exact title or heading | Date written with the text | Extent evidence |
|---|---|---|---|
| 22/002, printed header/title | “Étude différentielle des anneaux locaux réguliers : applications.” | Header: “13 novembre 1963”; note on 22/004: “Séance du 4 novembre 1963.” | Printed journal range “p. 2948–2950”; offprint text occupies scans 002–004, followed by printer page 005. |
| 22/006, printed header/title | “Sur les modules de différentielles.” | Header: “Séance du 21 janvier 1963”; note on 22/008: “Séance du 14 janvier 1963.” | Printed journal range “p. 842-844”; offprint text occupies scans 006–008, followed by printer page 009. |
| 22/019, title sheet | “Questions” | Undated | Sheet label 18; the following heading and four numbered questions occupy 020–021, with developments on 022–025. |
| 22/020, top heading | “Questions ouvertes” | Undated | Four explicit items, continued on 021; no total-page declaration. |
| 22/026, title sheet | Deleted “Différentielles” | Undated | Sheet label 25; handwritten calculation on 027 and 029, with reused typed pages 028 and 030. |
| 23/002, title sheet | “EGA IV, Calcul diff.” / “(Compléments)” | Undated | Sheet label 1; 15 retained pages in this cote segment, scans 002–016. |
| 23/003, title sheet | “Discriminant etc” | Undated | Sheet label 2; handwritten calculations on scans 004–006. |
| 23/008, title sheet | “Exponentielle” | Undated | Sheet label 7; exponential notes continue through scans 009–016. |
| 23/009, top heading | Underlined “Suite\|Suites sur l'exponentielle” | Undated | The singular/plural reading remains doubtful; sheet label 8 and a circled 1 begin the numbered discussion. |
| 22/018, lower paragraph | Proposed redaction “en deux pages ou trois” | Undated | This is the author's desired length for a rewrite of the results around 4.13, rather than an inscribed count of the surviving unit. |

There is no title-sheet declaration of the form “19 pages” or “Pages 1–67” in the frozen 44-page text. The numbers 29 and 15 are the retained scan counts supplied by the task, and the sequential labels below are the page evidence within the images.

## P07. All page-number sequences in this package

**Kind: reading question — competing pagination. Location: every retained sheet, visible numerals.** The lower-label run in cote 22 is 1–29 across scans 002–030, with the label 4 on 005 still doubtful, and the cote 23 run is 1–15 across scans 002–016. Several sheets also carry a second number belonging to an internal typed or printed sequence, which is preserved below; the repeated 27 on 22/028 and the 29/26 pair on 22/030 remain separate source observations. **Context / state:** `README.md`, supplied scan ranges; **MPL_33_147-181+34_002-017 8.3** [first-pass pagination lead], used only as a comparison question, with no inherited numbering supplied for these cotes.

| Cote and scan(s) | Visible labels preserved in transcription | Source position / qualification |
|---|---|---|
| 22/002–004 | 1, 2, 3 | Offprint unit; printed centred (2), (3) also appear on 003–004. |
| 22/005 | `4` doubtful | Printer sheet. |
| 22/006–009 | 5, 6, 7, 8 | Second offprint unit; printed centred (2), (3) on 007–008. |
| 22/010–018 | Upper/internal 24–32; lower 9–17 | Nine annotated typed sheets; both number series preserved. |
| 22/019–027 | 18–26 | Includes the two title sheets and mathematical/reused sheets. |
| 22/028 | 27, 27 | Two locations, one adjacent to the typed text and one at the foot. |
| 22/029 | 28 | Handwritten continuation. |
| 22/030 | 29, 26 | Two source labels; do not sort the archive sequence by the second one. |
| 23/002–006 | 1–5 | Covers and discriminant calculations. |
| 23/007 | 3, 6 | Reused English typescript's internal page 3 and separate sheet label 6. |
| 23/008–016 | 7–15 | Exponential cover and eight continuation sheets. |

## P08. Date evidence and chronology limits

**Kind: reading question — dating a plan or unit. Location: 22/002, 004, 006, 008, printed dating; 23/002–016, source titles.** The explicit 1963 dates belong to the two Jouanolou offprints and their session footnotes, and the 1940 date on 22/015 belongs to the cited MacLane paper; these inscriptions date the identified publications. The catalogue ranges “1963-[vers 1967][20]” for cote 22 and “1966-1968” for cote 23 come from the supplied README, while the selected handwritten title sheets themselves carry no date. Consequently the present record supports the exact offprint dates and catalogue ranges, with the individual manuscript plan/title dates left undetermined. **Context / state:** `README.md`, “This package in our plan”; no matching settled chronology item in `RESULTS_STATE.md`.

## P09. The two context tables of contents

**Kind: reading question — comparison witness, not a newly recovered archive plan. Location: 23/002 “EGA IV,” compared with the supplied EGA tables of contents.** `ega2-indexes-and-contents-fr.tex`, printed pp. 213–215, gives Chapter II “Étude globale élémentaire de quelques classes de morphismes” and closes with “Reçu le 22 juillet 1960”; `ega4-backmatter-contents-fr.tex`, printed pp. 341–343, gives Chapter IV “Étude locale des schémas et des morphismes de schémas (fin)” and §§16–21. These are useful later chapter-title and contents witnesses beside the 1960 introduction's shorter IV title “Étude locale des morphismes,” but the supplied IV contents excerpt has no date inscription. **Context / state:** the two named files at their printed contents pages; **WG2 §2.1 #2** [unchecked planning item], with no settled correspondence table.
