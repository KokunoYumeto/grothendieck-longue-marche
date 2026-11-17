# Research support: crosswalk from scans 001–045 to the returned notes for 127–176

## Scope, source order, and authority

This memo was prepared only after the current transcription freeze at **2026-11-17 15:15:39 UTC** and the authorized context opening at **15:15:45 UTC**. I read `context/notes/RESULTS_STATE.md` in full before reading `context/same_cote_154/MPL_154_127-176_notes.md` in full. I then consulted the current frozen page `.tex` files. I did not inspect scan images, change a page transcription, change the doubts file, or alter the inventory. This is research support, not a new reading pass.

**Notation for locators.** “Current 044:14” means scan 044, line 14 of `pages/MPL_154_001-045_154_scan044.tex`. A locator such as “later 171:280–309” is the locator **reported by the returned 127–176 research note**, not a line of a source transcription independently supplied or inspected here. “Later” and “earlier” refer to scan order only. They do not establish chronology: current 002 bears `18.1.84`, current 012 bears `23.12.83`, current 044 has the frozen alternative `31.11.83|31.12.83`, and the later note D02 reports `1.1.84` inside the wholly cancelled draft on scan 160.

The entire returned 127–176 note is a **first-pass research lead**. Its descriptions of manuscript claims, its own conditional arguments, its account of external papers, and its inherited register statuses must remain distinct. This memo does not independently certify the external literature cited there. The current `RESULTS_STATE.md` says that return statuses are the return's claims unless separately reviewed; the matching intake tags do not establish mathematical relevance.

Two especially important source limitations:

1. The earlier note repeatedly cites a `154-generisation-cube` entry in its own former RESULTS_STATE, plus `STATEMENTS_WITH_STATUS.md` entries. The current RESULTS_STATE has **no individual `154-generisation-cube` entry** and does not contain individual entries for **STRATA C.1/C.5, BISITE D.2/D.3/D.12, or RESIDUE G.3**. Their quoted statuses are reports from the earlier note, not current-register rows. The current register does contain **154-cyclic-order-determines-position** and **follow-ups @944**.
2. The earlier note had an Esquisse transcription and consulted published text that are not part of this subtask's inspected source set. Its Esquisse identification is a useful attributed lead. It must not be presented as my independent reading of that primary text.

## Principal conclusion

The strongest matches are concrete and internal to cote 154: **the K,L deployment and its numerical conditions; polygonal disk gluing with orientation transport; exceptional incidences and the need to retain extra contact data; and antipodal cyclic-order encodings**. Current 031–045 materially add to the later note's discussion of incomplete attachment data by giving an abstract gluing construction, an explicit flag action, corrections to transport, and a proposed exceptional completion. They do **not** by themselves settle the later endpoint construction, identify all five deployment variants, establish an extension-poset comparison, prove the cyclic-order injectivity claim, or supply the global move-generation and relation theorem sought in follow-ups @944.

No secure contradiction between the current packet and the later notes has been established. There are precise **tensions to test**—especially the claimed redundancy of a side choice in current 044, and the relation between contact-duplicated cells and unmarked relative positions—but their objects and hypotheses must first be matched. Several claims are revised or questioned **within the current text**; these are firmer evidence than a contradiction inferred merely from similar notation in separated passages.

## 1. Object and notation controls

| Object | Current frozen anchor | Matching later notes and cited scans | What may safely be identified |
|---|---|---|---|
| Fixed pseudoline system \(\underline\Sigma=(X,\Sigma)\) | 012:5; 034:11; 044:4 | P01/P04/G12/X03: 151:2–5, 153:153–165, 158 opening | The same broad relative-position problem. Neither source set fixes every convention about labels, ambient isotopies, or automorphisms. |
| Position graph \(\Gamma(\underline\Sigma)\), with positions as vertices | 012:25–31; 016:14; 017:6 | G02/G03: 151:2–9, 76–82; G11: 176:3–8 | Source/target, cyclic order, and transport are extra data. The later dual-edge description is not automatically this graph with the same variance. |
| Surface variants \(\mathcal X_0,\mathcal X_1,\mathcal X'_1,\mathcal X_2,\mathcal X_3\) | 002–010, especially 010:4–6 | P01/X01: 151:2–9; I01: 160:2–10 | The current packet explicitly offers several modifications; one must not equate each with the later \(X^*=\operatorname{Rel}(\underline\Sigma)\) without a map. |
| \(L\) as an added pseudoline or relative position | 034:11; 037–043, e.g. \(\Delta_L\) | P01/P05/X03 | This is different from the graph \(L\) in the K,L conditions. Matching letters alone is not an object identification. |
| \(K,L\) as cellular subgraphs of a deployment surface | 044:6–60; 045 | I02–I07/W10/Q06: 171:280–309 | Strong direct recurrence: four-valent K, even-valent L, side information, incidence multiplicities, common face sum \(2n\). Detailed hypotheses differ and have revisions. |
| Exceptional subgraph \(K_0\) | 044:14–20; 045:27 | I01/W07: cancelled 160:2–75 | Current text supplies a definition missing from the later note's local window. It does not validate the cancelled inverse-image formula. |
| \(\operatorname{Pol}(D)\), augmented/deployed polygons, \(\widetilde I\) | 018–026 | C05/X03/M04: 153:157–158, 154:31–44; 132:303–329 | Antipodal/orientation conventions matter. A cyclic-word comparison or a fuseau-bank invariant is not already the current injectivity theorem. |
| Repères and \(\sigma_0,\sigma_1,\sigma_2\) | 031–033 | U02/U03/M02/M06: 135–140 and 157 | The abstract cartographic operators and products recur. A formal action on current graph flags does not by itself supply the later geometric interpretation on fuseaux. |
| Contact datum \((D,s)\) | 043:3–5 | I01/I08/G03/X03: 160, 166, 151, 153–154 | Current completion changes the index set by duplicating exceptional positions. Forgetting the contact is an additional comparison step. |

## 2. Detailed crosswalk

### C127-01 — Classification: a concrete relative-position surface programme

**Current sources:** 012:5–31; 017:6, 45–47; 026:9; 044:4–6; 045:3–25. **Earlier-note matches:** **P01**, later 151:2 and 153–155; **P02**, later 151, 154–158, 171; **P03**, later 160 cancelled heading and 151/171; **P04**, later 151 opening and 158 opening. **Relation:** **adds concrete constructions and restates the subject**, with a bounded historical conclusion.

Current 012 explicitly starts “Structure sur l'ens des positions relatives”; current 017 names a “surface structurale”; current 026 describes disks obtained by removing a tubular neighborhood of a pseudoline; and current 044 titles a “Déploiement d'un syst. de pseudo-droites.” These strongly support the later note's identification of a combinatorial/topological relative-position project. P01 reports an explicit Esquisse §8 counterpart, the relative-position “surface modulaire”; P02 places this concrete problem within tame topology. That is a specific attributed contextual connection, not a deduction from generic words such as surface or form.

The current packet also sharpens P04's affinization interpretation. Current 003:11 and 004:3 discuss the system “Affinisé” by \(D_i\), but 009:8 expressly says that the supercritical faces of \(\mathcal X_3\) do **not** carry the same affinized representation as \(\mathcal X'_1\); they instead represent a pertinent portion of a tubular neighborhood. Thus “every deployment face is an affine presentation” would overstate the source.

**Register relation:** **MPL_154_127-176 P03** remains a first-pass lead. Neither the current dated passages nor the later cancelled heading establish a specific genealogical path to the 1986 geometry of forms. The strongest permitted conclusion remains the relative-position/tame-topology connection; an axiomatized tame theory and a precise 1986 precursor claim are unproved here.

### C127-02 — K,L conditions recur, while the current packet supplies missing definitions

**Current sources:** 044:6–60, 82–86; 045:3–27. **Earlier-note matches:** **I02**, later 171:280–284; **I04**, 171:290; **I05/I06/I07**, 171:280–309; **W10**, 171:280–309; **Q06**, same list. **Relation:** **restates the structural framework and adds an incidence dictionary**; no asserted equivalence of complete axiom lists.

Both passages concern a surface with cellular K and L and a common \(2n\) face count. Current 044 asserts order 4 along K, even order along L, limits L-vertices on a K-edge, distinguishes exceptional and ordinary K-edges, and supplies a weighted boundary count. Current 045 then indexes faces by nonsupercritical relative positions, ordinary edges by immediate specializations, other edges by sweeps near \(D_i\), ordinary vertices by specialization-triangle data, and exceptional vertices by repères/oriented edges/flags. The closing NB says these indications suffice to construct \((\mathcal X,K)\) as an incidence geometry. This is stronger **local specification** than the later note's statement that the intended source object is not specified in its scan-171 window (I07).

The condition lists must nevertheless remain separate. Current 044 has extensive cancellations and interlinear additions, an unfinished condition around (e), and a crossed-out definition of \(\varepsilon\) followed by its use in the marginal sum. Later Q06 records different reading uncertainties and a particularly consequential wording of its condition (f). One must not use the clearer wording of either list to repair the other frozen transcription. Nor does current 045's sufficiency declaration prove that every abstract K,L system satisfying later 171's list is realizable by a pseudoline arrangement.

**Register relation:** The finite-poset results **STRATA A.4** and **BISITE G.10** are **Proved (the return's claim)** for their stated minimum/least-vertex models. The recurrence of a finite incidence geometry is a candidate comparison object; it does not establish regularity or an equivalence with those models. This is the precise warning of later **G04**, 151:2,77 and 160:5–12,68–74.

### C127-03 — The side-choice issue is an exact place to test a claimed redundancy

**Current sources:** 044:20–24; also 031's \(\varphi_{\vec a}\) and 039:60,135,200. **Earlier-note matches:** **I03**, later 171:286; **G13/U06**, 151:81–82. **Relation:** **adds a claim that needs verification**, not a contradiction.

Current 044 first supplies a section of the band bundle for the ordinary normalized part \(K'_1\hookrightarrow\mathcal X\), then marginally says “cette donnée résulte en fait des autres” and calls for reconsidering the position of (e). Later I03 reports a possible section of a two-sheeted side cover and observes, conditionally, that a continuous global side choice needs trivial side monodromy. These fit a concrete question: **do the other current K,L constraints force the needed side monodromy to vanish, and if so do they select a unique section?**

The later note only reads “section” and “rev.” uncertainly; it does not establish that its cover is the current band bundle over \(K'_1\). Furthermore, its warning is about four-valence **alone**, whereas current 044 invokes other constraints. Consequently there is no demonstrated counterexample or contradiction. The precise addition is a redundancy claim to check after identifying the cover and the retained list of hypotheses. This concerns discrete two-sidedness/monodromy choices, not automatically a contractible space of all choices.

### C127-04 — K₀ and marked exceptional pieces: a direct antecedent to a cancelled correction

**Current sources:** 044:14–20; 045:23–27; 009:8; 041–043. **Earlier-note matches:** **I01**, later cancelled 160:2–10; **W07**, cancelled 160:12,68–75; **I08**, 166:244–248. **Relation:** **adds definitions and compatible geometric motivation**, without endorsing the withdrawn formula.

Later I01 reports the cancelled formula \(\varphi^{-1}(X_1^{a\mid0})=L\cup K_0\), “et non \(=L\) !”, while noting that K₀ is undefined in that window. Current 044 defines K₀ as the union of closures of exceptional K-edges, which contain no L-vertex, and states that this is a finite union of circles. Current 045 further claims that the components are indexed by I and canonically isomorphic to \(\widetilde D_i\), although its final sentence ends unfinished. This substantially improves the prospective dictionary.

Current 009 only says that the inverse image of X₁ under its \(\mathcal X_3\to X\) is “ce qu'il faut”; it does not print the earlier formula \(\varphi^{-1}(X_1)=L\). Therefore the cancelled later correction cannot be used as a direct refutation of a formula in the current packet. The map, its variant of \(\mathcal X\), and its subscript must be identified first.

Current 042 records overlapping exceptional generization arcs; 043 proposes replacing D by contacts \((D,s)\), yielding bigons or squares. That supplies explicit examples of the extra exceptional data which I08's marked-boundary/exceptional-edge correspondence would need to retain. A contact-to-boundary dictionary remains to be proved; colour or an unmarked edge alone is insufficient as an identification.

### C127-05 — Abstract gluing is explicit, but the intended relative-position object still needs identification

**Current sources:** 031–033; 034:5–9; 038:25–27,64,78; 039:60,135,200; 040:43; 041–043; 045:25. **Earlier-note matches:** **G01/G03/G04/G09**, later 151:2–9,76–82; **U05/U06**, 151:76–82; **G06**, 153:165–168; **X01**, 151 and 154:44. **Relation:** **adds a proposed construction and concrete repair data**, but does not settle the later endpoint issue or the surface comparison.

Current 031 supplies polygon structures around graph vertices and transport isomorphisms satisfying \(\varphi_{-\vec a}=\varphi_{\vec a}^{-1}\). Dual polygonal disks are glued along matched edges; corresponding disk orientations require the edge map to **reverse** induced boundary orientations. Current 032 then claims a compact boundaryless surface and describes its face orbits. Current 033 gives a truncated-disk variant with boundary components indexed by dihedral flag orbits. These are exact inputs for the finite reconstruction audit proposed in later G03, rather than merely a list of neighboring positions.

The application undergoes substantial repairs. Current 028 warns about artificial intersections after folding; 039 rejects the “évident” orientation transport in favor of its opposite; 040 declares the construction incomplete because supercritical positions were omitted; 042 finds overlap; and 043 duplicates contacts before claiming to have what is needed for a compact completion. Current 034:9 additionally says that a privileged corner type generally does not depend only on the vertex and therefore gives little hope of the stated decomposition into two dual graphs. Those qualifications should be retained in any modern reconstruction.

Later U05/U06 concern the critical endpoints of a semistable edge built from \((L,\omega_s)\) by “blocage,” with the two endpoints themselves questioned and several natural choices not known to work. Current 045's incidence recipe is relevant additional evidence, but the current edge-indexing conventions, contact refinements, and five variants have not been identified with that exact blocking construction. Hence neither “the later endpoint problem is solved already” nor “the later doubt disproves the current gluing construction” follows.

**Register relation:** **MPL_154_127-176 G09** is explicitly a first-pass lead; **EXIT_ONE_TYPE P1a1/P1d1** are **Proved (the return's claim)** in their specified normal-link/coherent-gluing settings. Current disks and flag transports are candidate inputs; no conical/stratified comparison or full flag coherence needed by those theorems is verified here. **EXIT_ONE_TYPE P4e**, also **Proved (the return's claim)**, supplies a useful warning that coarse data can lose links, not a theorem about the present pseudoline surface.

### C127-06 — Cartographic operators match algebraically; their geometric dictionaries remain separate

**Current sources:** 032, especially the three explicit \(\sigma_i\) formulas and final products; 033's orbit description. **Earlier-note matches:** **U02**, later 135:14,16,59; 138:213–217; 157:185–192; **U03**, 135:59–82 and 139:7–9; **M02**, 135–136 and 157:9–13; **M06**, 135–140 and 157; **W01/W03**, 135:3–5 and 140:8–23. **Relation:** **restates operator products and adds an explicit model**, not a completed interpretation of later quotient sets.

Current 032 specifies

\[
\sigma_0(\vec a,\omega_s)=(-\vec a,-\varphi_{\vec a}\omega_s),\quad
\sigma_2(\vec a,\omega_s)=(\vec a,-\omega_s),\quad
\sigma_1(\vec a,\omega_s)=(\rho_{\omega_s}(a),-\omega_s).
\]

It also writes the face product \(\rho_f=\sigma_1\sigma_0\) and \(\rho_{\rm som}\rho_f=\sigma_2\sigma_0=\sigma\); the earlier displayed subscript in the vertex product remains frozen as `1|4`. These strongly match M02's operator pattern. They give a specific finite permutation model for M06's proposed consistency test once a finite Γ and its transports are supplied.

Later U02 already records partial later progress on interpreting σ₀, so it should not be described as wholly unanswered. Current 032 still does not identify the later geometric repères with \((\vec a,\omega_s)\), interpret the quotient in U03, or reconstruct the incomplete map in U08 (later 136:24–40). Likewise the later explicitly rejected inverse guess for σ₀ (W01) is not a contradiction of the abstract formula here.

### C127-07 — Three orientations and variances must not be conflated

**Current sources:** 012:7,25–31; 016:14; 024:25; 031 final gluing paragraph; 039:60–200; 042:29–34. **Earlier-note matches:** **G02**, later 151:5–9,79–81 and 176:3–8; **M01/U01**, 133:125–139; **M03/Q05**, 157:185–192 and 158:18–23,119–120; **W04**, 133:139 and 151:4–9. **Relation:** **adds convention-sensitive formulas**, without equating different orientation operations.

Current 024 explicitly distinguishes arrows departing D (specialization) from those arriving D (generization). The edge identification in 031 reverses boundary orientations when the torsor orientations correspond. Current 039/042 instead choose the transport opposite to the tautological one in the geometric application. These are different kinds of direction: source/target, local surface or disk orientation, and orientation transport. Later M01's inverse circuit changes both bank and curve orientation; M03's projective duality has a minus sign and “non associés.” Neither can be normalized merely to match a familiar cartographic formula.

**Register relation:** **STRATA 0.1**, **Proved (the return's claim)**, concerns the opposite variance of geometric exits and the specified presheaf convention. It is an appropriate warning to formulate a functor's variance explicitly. It does not decide which current gluing map has the desired geometric meaning. The earlier note's separate BISITE D.3 status is not a current-register row.

### C127-08 — Local-system extension/restriction: strong current evidence, no exact later-note theorem

**Current sources:** 004:21–22; 007:3 and marginal 007:7; 009:8–10; 010:4–6; 019:47–49; 020–026; 028:10; 029:4–12. **Earlier-note matches:** **no direct 127–176 note about extension or restriction of the Pol(D) local system was found**. The nearest comparisons are **G09** (151:4–9,76–82), **I03** (171:286, a side cover), and **M06** (operator audit). **Relation:** **adds a genuinely specific obstruction and construction problem**, rather than restating a later result.

Current 004 says that polygon parallel transport on \(\mathcal X_0,\mathcal X_1,\mathcal X'_1\) is only defined away from the supercritical locus, described as an effective ramification locus. Current 007 claims a local system on \(\mathcal X_2\), contrasts ramification of index n on \(\mathcal X_0\), then expressly asks why the same argument would not falsely give a local system on \(\mathcal X_0\): “Il y a un pt qui en ce moment m'échappe.” Current 009 says \(\mathcal X_3\)'s supercritical faces do not have the same order, obstructing the intended **internal combinatorial interpretation** of the local system. It does not state that every possible local system on that surface is impossible. Current 010 claims associated principal \(D_{2n}\)-covers, ramified for the first three variants, while retaining doubt about the gluings near a supercritical face.

Current 025 gives an affirmative construction of transport from equal polygon order, the action on the two orientations, and the image of one marked vertex. Its final generalization has the exact written hypothesis that the “(vrais) sommets sont d'ordre 2,” with nonnegative edge weights and constant total incident weight. This must not be silently changed to order ≥2. Current 026 then explicitly reserves the supercritical specialization case for separate examination; 028–029 develop a segment/vis comparison there. Therefore the affirmative ordinary transport discussion does not already erase the ramification question at the omitted locus.

**Register relation:** **STRATA C.8**, **Proved (the return's claim)**, gives the claimed Cat∞ pullback description of locally constant enhanced coefficients **with equivalence gluing data**. It supplies a comparison framework after the relevant links, spaces, coefficients, and compatibilities are defined. It neither proves the current Pol(D) extension nor computes its local monodromy. **STRATA C.2**, **Known (the return's claim)**, and **EXIT_ONE_TYPE P1d1**, **Proved (the return's claim)**, are similarly conditional comparisons. I03's two-sheeted side-cover monodromy is a different cover until an explicit identification is supplied.

### C127-09 — Cyclic-order determination, transport determination, and fuseau determination are different assertions

**Current sources:** 018:5–11; 019:5–11,30–49; 020:7,21,53–57; 023–025; 035:34–37. **Earlier-note matches:** **M04**, later 132:303–329 and sequences 137,143–150; **C05**, 153:157–158 and 154:31–44; **C07/Q04/W05**, 153:142–168; **X03**, 151/153/154/158; **G06**, 153:165–168. **Relation:** **adds a precise candidate invariant and separate transport construction**, without proving a classification.

Current 018 constructs a \(2n\)-gon with antipody-compatible labelled edges indexed by oriented background pseudolines \(\widetilde I\). Current 019 excludes the supercritical positions from the resulting map and says “il ne devrait pas être difficile de montrer” that it is injective. This is an anticipated proof, not a completed proof in this packet. For a supercritical \(\Delta_{i_0}\), 019 instead has order \(2(n-1)\), with a bijection depending on an orientation of \(\Delta_{i_0}\) and changing by antipodism when that orientation is reversed.

The later cyclic-word proposal M04 is compatible but does not prove this exact invariant complete. The later qualified claim that banks determine a fuseau except in trivial cases concerns a different object and different equivalence data. Likewise current 025's determination of one polygon isomorphism from an orientation action and a marked vertex is not injectivity of the map from geometric positions to cyclic orders. Current 035 claims that its chord-system conditions suffice for a relative position for **some suitable Σ**; it does not supply realization over a particular fixed background arrangement or prove current 019's injectivity.

**Register relation:** **154-cyclic-order-determines-position**, credited to **Michel Hua's project**, is **conjecture (candidate: their search found no reference)**; the intake says **new to us**, not proved. The frozen current wording supports that status. The result remains separate from the former cube entry reported by the later note.

### C127-10 — Genericity, principal positions, and cube counts require different dictionaries

**Current sources:** 002:23; 003:3–27; 005:12; 013:16–29; 014:31–48; 015:23–29; 016:14–16; 017:8–28; 035–036; 040:20–24; 043:3. **Earlier-note matches:** **C01–C06/C10/U07**, later 154:31–44,75–78; **C07/Q04**, 153:153–168; **X01–X03**; **I02/I04/I07**, 171. **Relation:** **adds hypotheses and distinctions**; no proof or disproof of the cube model.

Current 013 defines a stable added position by \(|D\cap S|=0\), and a sous-stable one by \(|D\cap S|=1\). Current 014 then says an earlier count has a counterexample and repairs the graph by including the supercritical positions corresponding to the background pseudolines themselves. These are not automatically the later “positions principales”: later C10 expressly does not identify that word with membership in Σ, with a principal matroid extension, or with simple contact terminology.

There is also a separate genericity condition on the **background**. Current 002 says \(2(n-1)\) is correct only in the stable case and replaces it by \(2n_i\), where \(n_i\) counts vertices on \(D_i\). Current 043 distinguishes a simple contact (bigon) from the other case (square). Current 040 restricts uniqueness of a position through two nonaligned vertices to “cas (très) particuliers.” A generic-background or straight-line assumption cannot be silently imposed across the packet.

Later C02–C06 propose a **conditional local** model: independent detours in disjoint disks, with the curve fixed outside, give cube resolution states. The current polygonal stars, incidence graphs, and doubled exceptional contacts do not identify those states with the local strata of one surface point. The symbol ν has different recorded uses: current 015 counts vertices of a supercritical Δ, current 018 assigns multiplicities, and later 154's cube parameter is not explicitly equated with \(|S_D|\) in the earlier note's inspected window. Hence neither a count mismatch nor the degree of a cube graph supplies a contradiction until these data are matched. Later C04/X01 already distinguish indexing dimension and homotopy type from surface structure.

### C127-11 — Sweeps and specialization moves sharpen follow-ups @944 without settling it

**Current sources:** 012:25–31; 014:33–48; 015:25,29; 005:5; 036:3–25; 038:27,64,78; 045:5–13. **Earlier-note matches:** **P05**, later 133,155,156,176; **L01/L02**, 135,153,155,176; **Q10**, 155:18,37–38,66–67,103–106 and 156:183,185; **G11/Q09**, 176:3–9,225. **Relation:** **adds local definitions and distinctions**, not a presentation of all deformations.

Current 012 asks and answers the injectivity of the map from specialization triangles to source–target pairs under the nontriviality condition; it also records the strict increase in the set of arrangement vertices on the moving line. Current 015 corrects its initial classification by saying stable generizations of a supercritical line factor through sous-stable ones and so are not immediate. Current 005 introduces extra sweeps near a supercritical line with **weight 2**, explicitly saying they are not specialization arcs in the strict sense. Current 038 realizes generization by crossing strands, geometrically an antibalayage; current 045 incorporates immediate specializations and exceptional sweeps as different edge classes.

These details sharpen the generators and the object data required by **follow-ups @944**. They do not establish that every allowed deformation factors into these moves, that local short circuits generate all relations, or that the different deployment variants have the same deformation category. Later Q10 specifically retains local hypotheses in its criticality comparisons. A mixed specialization/generization circuit such as later 176 is not a directed specialization cycle and is not automatically a null-homotopy.

**Register relation:** **follow-ups @944 is Open**. Current 031–045 support its surface-construction part with candidate data; no genus/Euler enumeration or complete move-relation theorem is established here. **PATHS C.10** and **RESIDUE E.6** remain **Open (the return's claim)** and have substantially broader hypotheses; the current moves do not supply their comparison maps or pointed/ind refinements. **PATHS E.10**, **Refuted (the return's claim)**, reinforces that components of a marked subcategory do not suffice to compute general localization mapping spaces.

### C127-12 — Numerical constraints recur, but summing them needs incidence multiplicities

**Current sources:** 017:45–47; 019:30–41; 044:46–60. **Earlier-note matches:** **I05/I06/Q06**, later 171:280–309; **M05/Q08**, later 142:236–241, only as a separate count. **Relation:** **restates the constant total and adds its polygonal meaning**; no global enumeration follows.

Current 017 sets the total edge-plus-corner weight at a position equal to \(2n\); 018 gives the labelled \(2n\)-gon behind this count. Current 044 then interprets \(2n\) as the number of L-points on a K-face boundary, counted with reduced multiplicity, and supplies the marginal ordinary-face expression \(\sum_s(2\nu(s)+\varepsilon(s))+\sum_a\nu(a)\). This is a direct counterpart of the later 171 equation used in I05/I06.

I05's conditional parity check is appropriate once integer multiplicities and the incidence convention are fixed. I06's global summation assumes a closed surface, four distinct faces at each K-vertex, two distinct faces at each edge, and the intended number of boundary incidences. Neither packet has been shown here to satisfy all those assumptions. In particular a sum over cells lying in the closure of a face need not be the same as a sum over repeated boundary occurrences. The later quartic asymptotic in M05/Q08 concerns an unidentified counting expression and should not be supplied as the number of current K-vertices.

## 3. Self-marked uncertainty: exact current anchors and responsible cross-use

| Current anchor | Textual status in the current packet | Relevant later-note comparison | Consequence |
|---|---|---|---|
| 004:22; 007:3,7; 010:6 | “sauf erreur”; a point “m'échappe”; not fully convinced of boundary gluing | U05/U06/G13, later 151:76–82 | Related uncertainty about constructions; not the same unanswered question and not a general nonexistence theorem. |
| 012:27 | Injectivity question immediately followed by an affirmative argument | U01, later 133:125–139, likewise locally answered | Record as an answered local question with a proposed argument, not an expressly open question. |
| 013:16 → 014:31–48 → 016:14 | “je crois,” then a counterexample, then inclusion of omitted supercritical positions and revised polygon claim | W01/W02/W05 | A substantive repair within the current text. Do not report the initial argument as the final theorem. |
| 015:25,29 | Stable generizations are not immediate; count changes from including them to immediate ones only | C10/U07, later 154:34–37 | Preserve immediate-versus-general distinction; no answer to the later universal principal-specialization question. |
| 019:47 | “il ne devrait pas être difficile de montrer” injectivity | M04/C07/X03; Hua register candidate | Explicitly unproved in this packet. |
| 020:55 | `annulé; cf plus bas !` with reading uncertainty | W03/W08 | Withdrawn local formulation; later augmented polygons must be consulted, not used to erase the withdrawal. |
| 024:19–23 → 025:7,15–23 | “il faudrait” and question; affirmative “mais si !” / “Mais bien sûr” response | U02's partial resolution pattern | Local progress is real, but supercritical case is reserved again at 026:7. |
| 028:4,6 | Possible prohibitive artificial intersections; marginal “avec un grain de sel” is itself uncertain | G03/G04/I07 | Construction warning, with uncertain wording preserved; no new image reading made. |
| 031 final paragraph; 039:60,135,200 | Boundary-orientation reversal; rejection of evident transport in the application | M01/M03/W04/Q05 | Explicit sign/convention repairs must not be normalized away. |
| 040:43 → 042:36 → 043:3–5 | Incomplete construction; overlap; proposed multiplication into contacts and completion claim | U05/U06/G03/I08 | The proposed fix changes indexing data; it does not prove an unmarked Rel(Σ) comparison. |
| 044:22 | Section datum asserted to follow from others; instruction to revisit placement | I03/G13 | A concrete redundancy problem. No verified obstruction or automatic uniqueness yet. |
| 045:25–27 | Sufficiency declaration; subsequent canonical-isomorphism sentence unfinished | I07/G06/U08 | Distinguish a declaration of construction from a completed proof or the completion of an unfinished formula. |

The later note's **Q07** (131:47–55) is a useful methodological comparison: uncertain `?|!` is not secure authorial self-doubt. Likewise later Q03's uncertain disconnectedness wording is not a proved counterexample, and later Q09's uncertain Δ label is not a vanishing theorem. None supplies a reason to alter a current doubtful glyph.

## 4. Current RESULTS_STATE statuses and exact limits of relevance

| Current register ID | Exact status level | What the current packet contributes |
|---|---|---|
| **follow-ups @944** | **Open** (in the section of open research items from returned package notes) | Candidate gluing data, exceptional repairs, and generator distinctions. Surface comparison, enumeration, generation, and full relations remain unproved. |
| **154-cyclic-order-determines-position** | **conjecture (candidate: their search found no reference)**; intake “new to us”; credit Michel Hua's project | Current 018–019 supports the precise antipodal labelled invariant and its still-unproved injectivity. |
| **MPL_154_127-176 G09** | **research note of a returned package, first pass; a lead** | Current 031–043 gives actual proposed link/attachment data to examine. No promotion to a theorem. |
| **MPL_154_127-176 P03** | **research note of a returned package, first pass; a lead** | Current subject and dates support bounded historical classification; no 1986 genealogy established. |
| **STRATA C.8** | **Proved (the return's claim)** | Framework for enhanced local coefficients with equivalence gluing data; does not establish current Pol(D) extension. |
| **STRATA C.2** | **Known (the return's claim)** | Endpoint-compatible holink comparison for specified objects; manuscript objects/hypotheses unidentified. |
| **EXIT_ONE_TYPE P1a1** | **Proved (the return's claim)** | Normal-link mapping-space framework; no direct application proved. |
| **EXIT_ONE_TYPE P1d1** | **Proved (the return's claim)** | Coherent link gluing and constructible shapes; a bijection of isotopy classes or finite adjacency graph is not sufficient input. |
| **EXIT_ONE_TYPE P1b1** | **Proved (the return's claim)** | Ordinary-exit criterion needs asphericity and full normal-meridian injectivity; no such verification here. |
| **EXIT_ONE_TYPE P4e** | **Proved (the return's claim)** | Warning about loss of link, normal, and inertia data; not a theorem identifying this surface. |
| **STRATA A.4**, **BISITE G.10** | **Proved (the return's claim)** | Specified finite-poset realization dictionaries; regularity/face-incidence comparison still needed. |
| **STRATA 0.1** | **Proved (the return's claim)** | Explicit variance check is needed; source/target and local orientations alone do not define exit variance. |
| **STRATA B.1** | **Proved (the return's claim)** | EI-category and automorphism-group model; current arrangement equivalence and symmetry quotient are not fixed. |
| **WG2 B15 (§1.2)** | **question or plan item of the war game (round 2; unchecked)** | Possible finite test base. Does not solve unrestricted topology, even the real-line comparison cited there. |
| **PATHS C.10**, **RESIDUE E.6** | **Open (the return's claim)** | Move loops are examples at most; no general comparison or pointed/ind refinement. |
| **PATHS E.10** | **Refuted (the return's claim)** | Prevents inferring general localization mapping spaces from marked-subcategory components alone. |
| **EXIT_ONE_TYPE P3c-general** | **Open (the return's claim)** | Only a broad analogy of gluing/strata. Current topological disks do not supply smooth algebraic threefold good-NC completions or algebraic markings. |

The former **154-generisation-cube** status, cited repeatedly in the earlier note as “conjecture (unsearched),” must be explicitly attributed to that earlier note's reported register. Its present relevance is through the current **follow-ups @944** and the cube/surface comparison recorded in that lead; it is not a newly settled row.

## 5. Bounded research ideas supported by this crosswalk

These are proposals, not additions to the proved register.

### R127-A — Audit the surface using flags and boundary occurrences

**Sources:** current 031–033, 039–043, 045; earlier **G03/G04/M06**, later 151 and 135–140/157. **Confidence:** high that these are the right finite inputs; medium that every needed input is recoverable without further definitions.

Record the actual finite flag set, the three involutions, the orientation-transport table, every boundary occurrence of every disk edge, and the contact labels introduced at exceptional cells. Compute edge pairing and each vertex link before replacing the structure by a face poset. This makes the later G03 audit concrete using current formulas. An abstract polygon gluing passing these tests still needs a separate comparison to the intended space of relative positions and a proof that the position list is exhaustive.

### R127-B — Construct the forgetful map from contacts to original positions

**Sources:** current 042:36, 043:3–5, 002–010, 044–045; earlier **I01/I08/X03/G12**. **Confidence:** medium.

The current repair replaces a supercritical D by contacts (D,s), and different variants replace points by disks, antipodal identifications, or Möbius bands. A useful next object is an explicit cellular comparison between these variants and the unmarked position set. Record which cells and boundary incidences are identified by forgetting s, and whether fibers are points, intervals, circles, or more complicated pieces. This is the missing step between “a compact surface can be completed” and “this is the intended Rel(Σ).” It also supplies a precise place to locate K₀ in the cancelled later inverse-image correction without assuming that correction true.

### R127-C — Compute polygon holonomy around the exceptional locus

**Sources:** current 004:21, 007:3,7, 010:4–6, 025, 028–029, 031–032; earlier **M06/G09**, with **I03** kept as a different cover. **Confidence:** medium.

For each specified model, use the transport of an orientation and one marked polygon vertex to compute the composite around a small exceptional circuit. Compare the computed permutation with the asserted ramification index and with the proposed dihedral cover. This targets the exact uncertainty on current 007; the earlier note's generic coherent-gluing vocabulary cannot answer it. The computation should keep the supercritical polygon's order \(2(n-1)\) separate from the ordinary \(2n\)-gon, and should state how any missing labels are inserted or removed.

### R127-D — Test the redundancy of the band section and the face equation separately

**Sources:** current 044:20–22,46–60; earlier **I03/I05/I06/I07/Q06**, later 171. **Confidence:** high for separating the questions; medium for recoverability of the exact conditions.

After fixing a retained K,L condition list, test whether it forces trivial side monodromy on the normalized ordinary K-components. Independently check each weighted face equation using boundary incidences rather than sets of cells. A parity or global-count success is only a numerical filter and cannot establish side triviality or realizability. Conversely, a nontrivial side cover would refute the redundancy claim only if all the other intended conditions are satisfied and the cover has been matched to the manuscript's band bundle.

## 6. Explicit non-connections and negative search results

- **No direct extension/restriction theorem for Pol(D)** occurs in the returned 127–176 note. Searches for local systems, restriction, extension, and monodromy found one-element **matroid extensions**, a **side cover**, and general coherent-gluing comparisons. These are different problems. Current 004–010 and 025–029 add a specific local-system question of their own.
- **No current proof of the later cube dictionary.** Current polygon structures and the later cube index resolution data of different stated kinds; their ν, orientation, and exceptional conventions remain to be identified.
- **No current proof of the later fuseau bijection.** Current corridors and chord diagrams are relevant, but later C07/Q04 retain connected-component, critical-boundary, intersection, and trivial-case qualifications.
- **No automatic GT/tower connection.** Dihedral covers, repères, cells, and monodromy are not sufficient to invoke arithmetic GT reconstruction. Current D₂ₙ in 010, later Δ in Q09, and the arithmetic characters or deployed towers in the register have not been identified. In particular later Q09 explicitly rejects identifying its uncertain Δ label with LM7_PUSH E.65 merely by the letter.
- **No proof of EXIT_ONE_TYPE P3c-general.** Its algebraic threefold and NC-completion hypotheses are absent. The register's own “possibly” is a thematic lead only.
- **No finite-category minimum or localizer result is settled.** The coincidence of finite combinatorial inputs does not connect this packet to RESIDUE C.8, H.7, or the localizer/derivator questions without a specified functor or comparison.
- **No genus formula or enumeration is established by the current \(2n\) equation.** Later I06 is conditional, later M05/Q08 preserve an uncertain factor, and follow-ups @944 remains open.
- **No chronology is inferred from scan order or reused printed stock.** Later D02/D03 and current 002/012/044 concern different local manuscript dates; 1982 machine dates belong to the reused printout layer.

All relations above preserve the frozen current readings. Where the later returned note offers a clearer or different formulation, it is contextual evidence to compare, not permission to change the transcription.
