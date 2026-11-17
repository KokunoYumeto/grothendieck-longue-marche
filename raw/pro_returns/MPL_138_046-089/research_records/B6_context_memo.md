# B6 context evidence memo

Research-only auxiliary record, 17 November 2026. All locators below refer to the supplied text as it stood after the transcription freeze. No scan image was read, no handwriting was re-read, and no transcription or supplied context file was changed. The whole of `context/hua_project/138.modern.tex` (1,879 lines), both context READMEs, and `RESULTS_STATE.md` were read. No external source was consulted for this memo.

## 1. Source status and the question to be tested

`context/README.md`, lines 20–22, gives **Bridge B6** as the planning claim: a finite cartographic action gives a cover of the three-punctured line and a curve over Qbar; GT acts; the absolute Galois group acts faithfully already on regular maps. Lines 28 and 38 explicitly make planning guesses and prior-run outputs claims to check. B6 is a README label, **not a numbered proved result in RESULTS_STATE**.

The supplied *Esquisse* is a transcription of a primary text, but its API collation has **not been checked by eye** (`README.md`, line 36; repeated page headers in the TeX). The LM texts declare second passes. Hua is a **modern interpretation**, not a primary transcription or our result: `hua_project/README.md`, lines 3–10, and `138.modern.tex`, lines 1–13. Its own header says the October 2026 AI pass was unchecked against the pages by a human. References to what Hua says below must be credited as “Hua, modernised reading of cote 138,” with the subsection title.

## 2. Exact supplied primary-text counterparts for B6

The file in every row of this table is `context/Esquisse_cote119_copy1_API_transcription.tex`. “Scan” uses its `\scanpage{119/n}` marker; the typescript page is separately given by `\mspage`.

| B6 component | Section, scan / typescript page, lines | Evidence and precise scope |
|---|---|---|
| Cartographic presentation | §3, 119/12 / p10, 509–525 | Gives the flag-set description and the presentation of the nonoriented group with involutions `sigma_0,sigma_1,sigma_2` and `(sigma_0 sigma_2)^2=1`; then its oriented index-two subgroup. |
| Finite sets with an action | §3, 119/13 / p11, 539–547 | “un dictionnaire parfait” between compact maps / oriented compact maps and finite sets with operators `C_2` / `C_2^+`. Credits Malgoire–Voisin's 1976 DEA work. |
| Covers of the three-punctured line | Same scan, 549–571 | `C_2^+` is a **quotient** of the fundamental group of a three-punctured sphere. The extra relation `sigma^2=1` imposes ramification index **1 or 2 above 1**. Finite oriented maps correspond to these finite branched covers. Removing the branch fibres gives the unramified-cover formulation in B6. The ramification restriction should not disappear in a precise account. |
| Definition over Qbar | §3, 119/14 / p12, 582–595 | The resulting curves are defined over “la clôture algébrique … de Q dans C”; the map is recovered as the inverse image of `[0,1]`; vertices, edge centres, face centres lie over 0, 1, infinity. This is the **map-to-curve** direction. |
| Galois action on maps | §3, 119/15 / p13, 647–659 | Finite maps are covers over Qbar of a curve over Q, hence the Galois group acts naturally on their category. For spherical maps it applies the automorphism to coefficients of `P/Q`. |
| Relation to the profinite fundamental group | §3, 119/16 / p14, 675–698 | The exterior action on the completed oriented cartographic group is obtained by quotienting the canonical exterior action on `pi-hat_(0,3)`. The nearby modular-group description concerns triangulated maps. |
| Do **all** Qbar curves arise? | §3, 119/16 / p14, 701–708, then 119/17 / p15, 721–739 | First asks “les obtiendrait-on toutes”; then reports Bielyi's Helsinki announcement and the theorem that every curve over a number field is a cover of the projective line branched only at 0,1,infinity. Thus the retrospective text explicitly distinguishes the map-to-curve construction from its much deeper converse. |
| Faithfulness | §2, 119/6 / p4, 233–240 | Says the action on the Teichmüller tower is faithful already at `T-hat_(0,4)`, equivalently the exterior action on the profinite fundamental group of the three-punctured line is faithful. |
| Meaning of “regular” | §4, 119/20 / p18, 864–871 | Regular means the automorphism group acts transitively, hence simply transitively, on flags. In the oriented algebraic interpretation these are **Galois covers** of the projective line. |
| Faithfulness **on regular maps** | No such assertion located in these *Esquisse* passages | The regular-map definition above is not this strengthening. The only `González`/`Jaikin` occurrence in supplied context is `README.md:22`. No statement/proof of their theorem was supplied here. Treat it as the planning bibliography until externally verified by the root. |

The dictionary in the arithmetic rows concerns **oriented** maps. The nonoriented analogue in *Esquisse* 119/14, lines 613–619, uses real algebraic curves and the quotient by complex conjugation. Also distinguish faithfulness of a map's own finite automorphism group on flags from faithfulness of the **absolute Galois group on classes of maps**.

## 3. What frozen scans 046–089 actually contribute

Per-page sources are `MPL_138_046-089/pages/MPL_138_046-089_138_scanNNN.tex`. The archive-foliation comments verify, within this package, **Hua page p = our scan p+1**. Do not substitute Hua's page numbers for scan numbers in notes.

| Frozen source | Direct evidence | Relationship to B6 |
|---|---|---|
| 046, lines 4–12; 047, lines 21–47 | `X=C_2`, a ramification divisor with splitting field Q(i); a tower with `x_n^n=x_1` and `u=1/2-(z+z^-1)/4`, ramification at 0,1,infinity and a dihedral group. | Concrete algebraic covering computations. They instantiate the bridge without stating a universal finite-map theorem. |
| 064, lines 19–46 | The `E^+`, `E^-`, `D_ij`, `S_i` diagram, three permutations with `rho_2^+ rho_1^+ rho_0^+=id`, and orbit identifications for the `S_i`. | Supplies the combinatorial permutation mechanism. The diagram itself does not state that every Qbar curve arises or that Galois acts faithfully. |
| 077, lines 34–77; 078, lines 6–12 and 44–58 | Incidence maps and commuting `sigma_0,sigma_2`; flags as a fibre product, orientation pieces, another double-pyramid diagram; separately a map between projective lines over Qbar and seven special points. | Concrete incidence data and geometric examples, not a written general equivalence theorem in this selection. |
| 080, lines 5–38; 081, lines 30–36; 082, lines 3–21 | Special profinite systems with free rank-nu groups and peripheral classes; projective line minus a finite set; fibre functors and the outer-automorphism torsor. | Makes the group-theoretic target and peripheral structure explicit. |
| 083, lines 6–24 | Galois transport of structure, a map to the twisted outer-automorphism group, the fundamental extension, Kummer–Tate character; explicit definition of Qbar as the closure of Q in C. | Direct arithmetic input for the bridge. The definition of Qbar here is not a theorem that every curve is a dessin. |
| 084–086; especially 086, lines 20–29, and 087, lines 3–23 | Dihedral compatibility; special choice `I={0,1,infinity}`; `Gamma x S_3`; boxed `Gamma -> T_2^(S_3)`. Then “On aurait envie de définir un iso can.”, a question mark, and desired comparison across nu. | Establishes the proposed outer-action framework and its compatibility constraints. It does **not** establish injectivity, characterize the complete arithmetic image, prove GT equals Galois, or prove the desired cross-rank isomorphisms. |
| 089, lines 40–61 | Inner automorphisms, character, quotient `A_nu/Lhat_nu=Gamma_nu`; “on veut élucider sa structure”. | An explicit remaining problem, not a solved recognition theorem. |

Searches of all frozen page TeX for `cartograph`, `fidèle/fidel`, `Bely/Biel`, `régulier`, and `toute ... courbe` found only the **functor** faithfulness criteria on scan059 among these terms. The bounded absence conclusion is: **no explicit general map-to-Qbar equivalence, converse for all Qbar curves, or Galois faithfulness statement was located in this 42-page selection**. The positive diagrammatic and outer-action evidence is substantial and should be described on its own terms.

## 4. Hua: full-file comparison and offsets

The whole modernized file has been read, including material before and after the package. Its “no findings … on these scans” description in `RESULTS_STATE.md:22` is only the digest's opening-based report; it is contradicted as a scope description by the supplied full file, whose §§5–11 explicitly cover this selection.

| Hua subsection / lines | Hua pages | Current scan correspondence / use |
|---|---|---|
| §5, “La tour diédrale,” 948–967; “Les endomorphismes de la conique,” 969–1004 | 45–46; 48–54 | Scans046–047;049–055, with intervening nonmathematical sheets. Context for concrete covers, not the universal theorem. |
| §7, “La double pyramide,” 1098–1128 | 63 | Scan064. Hua identifies the permutation mechanism and names Jones–Singerman1978 in his own footnote. |
| §10, “Quelques problèmes spéciaux : les drapeaux,” 1228–1247 | 75–77 | Scans076–078. Hua explicitly declines to restore all overloaded flag indices. |
| §11, “Définition,” 1251–1296 | 79–80 | Scans080–081. Distinguish his mathematical normalization from the frozen literal formulas. |
| §11, “L'action de Galois,” 1298–1410 | 81–86 | Scans082–087. Exact B6-adjacent outer action and S3 centralizer discussion. |
| §11, “Le groupe de Teichmüller discret et son complété,” 1412–1464 | 88–90 | Only the opening page corresponds to present scan089; later pages are outside the selection. |
| §13, “I) Précartes, et la catégorie des cartes co-épinglées,” 1504–1549 | 97–98 | **Outside the selection**. Nominal +1 offset would be scans098–099; those primary scans were not inspected here. |
| §13, “II–III) Le schéma de modules, et l'action de Galois,” 1551–1614 | 99–102 | **Outside the selection**. Gives the cover/moduli/Qbar correspondence in Hua's interpretation; cannot be silently attributed to scans046–089. |
| §15, “Ce qu'est une opération,” 1717–1782; “Cartes holomorphes,” 1810–1854 | 121–127;128–130 | **Outside the selection**. Includes normal finite-index subgroups and regular maps (1740–1748), and the holomorphic/three-branch-value description. |

Three specific cautions are essential:

1. **T-to-Gamma normalization.** Hua's comments lines 36–41, conventions 235–239, and footnote 1332–1335 explicitly replace the manuscript's cursive `T` on pp83–86 with `Gamma`, reserving `T` for the later discrete Teichmüller group. Our scans084–087 preserve `mathcal T`. This is an intentional modernizing convention, not evidence that the handwriting said Gamma.
2. **Corrected reversal.** Lines 1354–1367 give Hua's replacement for p84 (=scan085). His defect computation assumes `g_i=lambda_0...lambda_(i-1)` and obtains `lambda_0 lambda_1^-1 lambda_0^-1 lambda_1`. Frozen scan085:22 retains `lambda_{\unsure{0|1}}`, and line26 retains “vérifier ?”. His algebra is a credited comparison conditional on that reading; it cannot settle the frozen ambiguity. He also says neither formula has been geometrically derived from inversion because the basepoint moves.
3. **Later theorem and moduli amendments.** Hua's summary says “Elle est fidèle à grande échelle” (132), but footnote 1401–1410 explicitly places injectivity after Belyi and labels Drinfeld/GT as later interpretation, saying the page does not contain it. For the out-of-scope moduli discussion, lines1523–1533 restrict rigidity to genus0 and give his torus counterexample;1564–1574 restrict representability and say the page supplies no proof;1598–1614 identify the algebraic points with maps and correct the blanket nontriviality assertion. Credit these to Hua rather than treating his corrected exposition as a verbatim manuscript theorem.

## 5. LM and RESULTS_STATE connections, with status preserved

An especially direct counterweight occurs in `context/LM_140-2_text.tex`, **scan312, lines9396–9399** (located by the root and then read for this memo). It specifies `U=P1_Q minus {0,1,infinity}`, `G=S_3`, and `Gamma=Gal(Qbar/Q)`, then says: **“Je n'ai pas vérifié que … soit injectif”**, allowing calculations to remain heuristic. This is primary textual evidence that an arithmetic outer homomorphism must not automatically be upgraded to faithfulness. Scans313–314, lines9405–9424, then explain collisions in the Gamma notation and reserve script T for Teichmüller groups, Gamma for Galois groups, G for geometric actions, and script G for mixed groups. Those later explicit conventions are a comparator, not permission to rewrite cote138's frozen notation.

The further actual LM sequel is **§35**, scans491–502 of that file:

- Lines14331–14339, scan491: title “L'injectivité de Gamma_Q -> Autext_lac(Pihat_0,3)” and Theorem1 explicitly assert injectivity, with margin “démontré modulo le lemme 2 plus bas”.
- Lines14346–14350, same scan, invoke **Белый** and require a map defined over Q. Scan494,14378, expressly warns that finite image alone does not give trivial action. Scan495,14397–14410, detects the kernel on algebraic boundary points and concludes `K=(1)` under the cited lemmas.
- Scan496,14426–14427: “Finalement je cale sur a)” about centrelessness, followed by consultation of Deligne. Scan497,14458–14465, distinguishes presumed faithfulness for any anabelian curve from the stated corollary after shrinking. Scan498,14470–14477, invokes Белый again and flags further verifications. Scan502,14543–14571, presents a stronger faithfulness statement as something that “devrait” hold.
- Earlier scan479,14111–14113, mentions the Russian result relayed by Deligne and the desired algebraic characterization of the image. Do not turn that tentative formulation into a proof identifying the whole GT group with Galois.

| Register ID and exact locus | Supplied status | Contribution / limit of current package |
|---|---|---|
| **EXIT_TOWER E.24**, `RESULTS_STATE.md:17,356` | **Open (return's claim)**; full cited source is `EXIT_TOWER_results.csv`; cote143 §9,folios15–17,scans29–33 | Closest B6 register connection: arithmetic image among outer automorphisms preserving boundary inertia and centralizing relabelling. Scans080–087 provide an earlier explicit peripheral/S3 target, but no image computation or witness test. Status unchanged. |
| **EXIT_TOWER E.39**, line396 | **Proved (return's claim)**, not one of the explicitly refereed rows in lines7–8 | Claimed GT action on the full completed exit system. The excerpt supplies no proof to verify here; scans046–089 do not prove this tower assertion. |
| **MPL_144_062-121 §9**, line434 | **Observation, first-pass research-note lead** | Register excerpt reports reconstruction from inverse image of `[0,1]` and 0/1/infinity fibres on cote144/062. The actual note file is absent from this context, so cite as a register lead only. |
| **LM4_SUCCESSOR B.38**, lines16,359 | **Open (return's claim)** | K5 and levels7/11 remain unresolved. The present examples and diagrams give no congruence-kernel determination. Adjacent to B6, not a consequence of it. |
| **LM4 D.12**, lines18,349 | **Open (return's claim)** | Torsion/conjugacy in full GT0 is not resolved by these dihedral symmetries or the S3 compatibility. |

The status policy is `RESULTS_STATE.md:7–8`. The orientation itself says no already-established result was named in its digest for these scans (line20). No register status should be changed by this memo.

## 6. Dating evidence and its limits

**Primary frozen anchors.** The selection contains a cluster of documents dated June 1978, not just the Mumford letter. All rows were read in the frozen TeX, not on scan images.

| Frozen scan / lines | Document date and content |
|---|---|
| 048:32–43,57 | Rector's order dated **27 June 1978**, effective dates 26/27 June 1978, with a reference to an older order of 15 December 1977. The reference is not this document's date. |
| 050:11,21–30 | Defence notice dated **8 June 1978**, for a planned 1 July 1978 defence. |
| 052:30,34–47,68–70 | Mumford letter dated **10 June 1978**; Zariski's 80th birthday “will take place on April 24th, 1979”; planned 1979 journal issues. Its 460-page capacity (lines54–55) concerns the journal issue allocation, not this manuscript's extent. |
| 056:11,21–28 | Defence notice dated **15 June 1978**, for a planned 3 July 1978 defence. |
| 067:4,13–23 | Defence notice dated **28 June 1978**, for a planned 13 July 1978 defence. |
| 069:4,13–21 | Defence notice dated **26 June 1978**, for a planned 13 July 1978 defence. |

These documents are consistent with the catalogue **[vers 1976–1978]**, reproduced in `context/README.md:9`. The narrower question-marked title “(1976, 77 ?)” is not an exhaustive date for the dossier's contents.

**Hua's provenance comment.** “Le fil du dossier, et les conventions,” lines263–270, says several sheets use backs of typed 1977/1978 letters and defence notices, and says those documents are omitted from his reading. He guesses the 1976/77 wording came from a folder. These are his supplied observations/guess, not independent physical-sheet verification by this text-only memo. His header line11 expressly omits his p51, which matches our scan052's archive foliation51.

**Retrospective chronology.** *Esquisse* §3,119/13,546–547, credits the 1976 DEA;569 says the discovery still strikes him “huit ans après”. §4,119/21,920–927, places cube/icosahedron courses in 1977 and 1978;119/22,947–951, mentions the 1977/78 DEA on polygons. These corroborate the research period, not exact dates of particular cote138 leaves.

**Necessary limit.** Dated inserted/retained documents do not by themselves date all undated mathematics, prove which adjacent image is a given document's verso, or impose a global terminus ante quem. A terminus post quem for mathematics on an actual reused reverse requires the leaf relationship to be established. This memo did not inspect it. Also, *Esquisse*119/17,721–727, reports the theorem's Helsinki announcement; the bibliography's 1979 publication date alone cannot establish that every 1978 leaf predates knowledge of the theorem.

## 7. Search record

Terms included `cartograph`, `fidèle/fidel`, `régulier/regular`, `Bely/Bielyi/Белый`, `González`, `Jaikin`, `toute ... courbe`, `Qbar`/TeX Qbar forms, `1976/1977/1978/1979`, `Mumford`, and `Zariski`. Negative findings are limited to supplied files and the frozen selection, not the archive as a whole. The strongest positive B6 evidence in this package is the progression from explicit covers and flag permutations to special profinite systems and the boxed S3-compatible Galois homomorphism. The universal converse and faithfulness belong to the separately identified later context.
