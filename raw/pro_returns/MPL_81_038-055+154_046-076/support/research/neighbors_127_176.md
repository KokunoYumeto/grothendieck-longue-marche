# Comparison support: frozen 154/046–076 and the 127–176 neighbor notes

This is internal comparison support, not the final research notes. It was prepared after the transcription freeze reported by the parent (2026-11-17 14:06:11 UTC; context opened 14:06:15 UTC). The frozen page files and combined transcription were read but never edited; original scan images were not inspected. `context/README.md` and all of `context/notes/RESULTS_STATE.md` were read before drafting, as was all of `context/same_cote_154/MPL_154_127-176_notes.md`.

## Evidence and status conventions

- **New anchor** means a location in `deliver/pages/MPL_81_038-055+154_046-076_154_scanNNN.tex`; the numbers after a colon are frozen TeX line numbers, not original manuscript lineation. The manuscript-page offset in these new leaves is scan minus one.
- **Neighbor anchor** means a note ID in `context/same_cote_154/MPL_154_127-176_notes.md`, followed by the scan and any line numbers that that note itself reports. Its original scans and page files were not independently checked. All neighbor notes remain first-pass leads, including their confident statements and literature summaries.
- **RS** means the current supplied `context/notes/RESULTS_STATE.md`. “Proved” or “Known” below always means **the register return's own claim**, not certification by this comparison. No register status is changed.
- Relation labels compare the new frozen evidence with the named neighbor lead: **add**, **restatement**, **difference**, or **contradiction**. “Difference” is used when a possible conflict depends on identifying maps, loci, conventions, or cancelled drafts; no unconditional manuscript contradiction is certified here.
- “Later” below means **later scan number**, not established authorial chronology. The neighbor's wholly cancelled scan160 is dated 1.1.84 (D02), whereas new058 and065 are dated3.1.84, new061 begins4.1, and new048 has the uncertain date7.2.1984. These dates prohibit describing scan160 automatically as a subsequent correction to every lower-numbered leaf.

## Priority findings for the parent

1. New046:29 has `L=φ⁻¹(⋃D_i)` with `X₁` under the union and a K₀-neighborhood warning at046:31. Neighbor I01/W07, scan160:2–10, reports a **wholly cancelled** proposed correction `φ⁻¹(X₁^{a|0})=L∪K₀`, “et non =L !”. New074:33 and076:8 also use inverse-image descriptions of L. This is an excellent precise comparison, but the superscript, maps, and intended exceptional neighborhoods are not identified; it is not a clean refutation or a secure chronology of revision.
2. The three layers of orientation in new061–069 must remain distinct: orientation transported by polygon isomorphisms, orientation of an added pseudoline, and orientation transported through the glued surface. Neighbor M01/M03/W04, scans133,157–158,151, reinforce the need for marked sides and local orientation conventions. They do not prove an equality of the different torsors or dihedral surjectivity.
3. New058–059's broad monodromy conclusions are cancelled;058 has a later margin warning that the relevant supersingular positions are excluded from the `Pol(D)` game. New063:32 expressly repairs the crossing-parity rule by counting an exceptional crossing twice. Retained064 restates a half-turn translation with the opposite sign convention, `+n−1` in a specified orientation, expressly concludes surjectivity at064:18–20, and argues at064:22–33 that corrected path parity is the endpoint difference of singularity counts, hence that `χ_c=1` and `χ_𝒳=χ_X`. The register Hua entry must be assessed against this retained proof sketch as well as the cancelled trials; the geometric existence and descent obligations remain to be checked.
4. New065–071 records four gluing choices, with immersion versus edge-folding and a rejected circuit procedure; new075–076 asks whether a doubled construction is the intended surface or a ramified double cover. Neighbor U05/U06/G01/G03/G09, scan151:76–82, still reports the critical-endpoint/blocking problem. The new leaves add concrete gluing data and failures to **follow-ups @944**; they do not complete its surface or presentation proof.
5. New047 and055 are strong sources for an actual finite-reconstruction ambition; neighbor I02–I08, scan171 and166, gives complementary branch, side-cover, marked-boundary, and numerical constraints. Neither finite numeric data nor sign propagation is shown sufficient for reconstruction, and055 explicitly excludes exceptional faces from its verification.
6. The current RS has the Hua row **154-dihedral-monodromy-half-turn**. It does **not** have the **154-generisation-cube** row cited from an older state inside several neighbor notes. Do not cite that older row as if present in the current RS.

## Comparison records

### N127-01 — Transport around the added pseudoline and later marked circuits

**New anchor:** 056:44–59,66–73,128–157;061:9–33;064:4–14. The component maps are written `σ_j(t)=ℓ_j−t`; their product is calculated as `(-1)^p(t−χ_p)`; for the specified even circuit the frozen text writes `λ(t)=t−(n−1)`. The retained061 passage defines polygon transport along a combinatorial path and writes a representation into `Aut(Pol(D))≃𝔻_{2n}`. Retained064 writes the half-turn translation as `n−1` in the direction of a stated orientation.

**Neighbor anchor:** M01/U01, scan133:125–139, simultaneous change of the bank ρ and orientation ω for the inverse circuit; M04/Q11, scan132:303–329 and scans137,143–150, marked cyclic words and distinct terminal exponents.

**Relation: add.** The new leaves give the explicit affine reflection/product calculation missing from those later circuit summaries. The inverse-circuit rule gives a plausible reason that a reversed loop or coordinate can replace the translation by its inverse, but it does not identify the exact loops or coordinates used at056 and064. Neither the sign discrepancy nor the later exponent discrepancy should be silently normalized.

**RS:** **154-dihedral-monodromy-half-turn** [Hua findings register, conjecture/unsearched; intake “new to us”]; **follow-ups @944** [open]. The calculation is strong textual support for the half-turn formula in a specified convention. It is not an independent proof that the combinatorial transport descends to the fundamental group of a completed surface in every allowed case, nor a proof of all move relations. **Confidence:** high on new textual anchors, medium on the exact circuit identification across windows.

### N127-02 — The cancelled surjectivity argument is not repaired by later frame algebra

**New anchor:** 058:4–42 and059:2–43 are enclosed in deletion markup;058:46 warns that “Ces … positions … sont exclues dans le jeu des Pol(D)”. New059:28 distinguishes supersingular bands of index `2(n−1)` from the ordinary `2n` situation. Retained060:23 asserts surjectivity again, but its proposed circuit continues into the cancelled opening of061:2–7. Retained064:14 argues from fixed points and orientation-reversing transport to finding all reflections, then064:18–20 displays the representation and expressly concludes “est surjectif. ouf!”. This is a retained positive assertion with an indicated argument, not an unfinished sentence or a cancelled claim.

**Neighbor anchor:** M02/M06, scans135–140 and157:9–13, cartographic generator formulas and the proposed finite action check; U02/U03,135:14,16,59–82;138:213–217;157:185–192, partial geometric interpretations and a remaining quotient question.

**Relation: difference.** A later cartographic presentation or local frame action is not a proof of the earlier polygon monodromy image: the acted-on sets, base spaces, and generators must first be identified. The cancelled exclusions are substantive limitations, even though cancellation alone does not refute the underlying algebraic possibility.

**RS:** **154-dihedral-monodromy-half-turn** [Hua conjecture/unsearched]; **follow-ups @944** [open]. The retained064 proof sketch supports Hua's account of a claimed full dihedral image, while no exact current RS entry independently establishes the geometric loops, descent, and full pseudoline frame action. The neighbor's Esquisse operator comparison is a lead, not independent completion of those obligations. **Confidence:** high that the new surjectivity passages have mixed documentary status and include a retained positive conclusion; medium on the precise meaning of each excluded locus.

### N127-03 — Three orientation transports and convention-sensitive duality

**New anchor:** 061:17–35 separates polygon transport and its orientation character;062:15–38 distinguishes α=α′ from β, the orientation transport on X, with equality conditioned on the number of operations. New067:8 calls an earlier identification an “erreur monumentale”;068:11–19 records two separate mistaken identifications. New069:8–16 distinguishes the orientation effect of gluing from transport of the pseudoline.

**Neighbor anchor:** M03/Q05,157:185–192 and158:23,119–120, `ω*=−α*∧β*` versus `ω=α∧β` and “non associés”; W04,133:139 and151:9, repairs to the local ambient orientation and left/right conventions; M01,133:125–139.

**Relation: add.** The new material supplies explicit reasons why apparently similar orientation statements can differ: they refer to different torsors and transition maps. The neighbor's duality minus sign should remain intact. It is not automatically the same sign as the gluing discrepancy in067–069, and neither is an error to repair from general expectations.

**RS:** **154-dihedral-monodromy-half-turn** [unchecked Hua row], **MPL_154_127-176 G09** [first-pass lead], **follow-ups @944** [open]. No current RS statement identifies these orientation torsors. **Confidence:** high for the distinctions and retained corrections; medium for connecting a particular later duality sign to one of the earlier transport conventions.

### N127-04 — Exceptional crossings change the parity count

**New anchor:** 063:29–45 defines the combinatorial character and records the margin correction: count an exceptional-side crossing “pour deux”, or decompose it into two operations. The boxed relation is `χ_𝒳=χ_{o|X}χ_c`; a further marginal note asserts `χ_c=1` with an uncertain reference to the next page. Retained064:22–33 supplies that next-page argument: corrected path parity is congruent modulo two to `sing_D′−sing_D`, so it vanishes on closed paths, and the text concludes `χ_𝒳=χ_X`. The reasoning reduces to checking each allowed elementary transition, with exceptional sweeps counted twice. New062's ordinary step-parity comparison therefore cannot be repeated without the exceptional convention.

**Neighbor anchor:** G02,151:5–9,79–81 and176:3–8, distinguishes a geometric edge direction from specialization/generization and categorical variance; Q09/G11,176:3–9, records a mixed specialization/generization cycle, not a directed specialization cycle; Q10,155:18,37–38,66–67,103–106 and156:183,185, retains local hypotheses for elementary sweeps.

**Relation: add.** Counting arrows in a drawn cycle is not sufficient to calculate the corrected character: the type of crossing and its elementary decomposition matter. This is a direct reason to keep the later move labels and hypotheses rather than deriving parity from the unlabeled graph.

**RS:** **154-dihedral-monodromy-half-turn** [unchecked Hua row]; **follow-ups @944** [open]; **MPL_154_127-176 G09** [first-pass lead]. The current RS's refereed LM7_PUSH character Δ is unrelated without object-identifying evidence. **Confidence:** high on the explicit parity correction and the endpoint-difference proof sketch; medium that every allowed exceptional transition satisfies the asserted local rule. The formal coboundary conclusion follows if that local rule holds. It does not make the unweighted transition graph bipartite when some edges have corrected weight two.

### N127-05 — Orientation and side-cover data require a global comparison

**New anchor:** 048:22–30 prescribes signs of chosen sides and transition rules. New075:6–17 considers a Möbius ribbon and its twofold orientation cover, explicitly asking whether it is twisted by `ω(D)`;076:4 asks about a double cover ramified at centers before proposing the quotient by antipodisms.

**Neighbor anchor:** I03,171:286, “une section du rev. à deux feuillets” with both decisive words uncertain; I02,171:280–284, normalization of K; G13,151:81–82, unsettled natural choices.

**Relation: add.** The new Möbius-band discussion makes the global two-sheeted structure a manuscript issue, rather than merely an external warning supplied by I03. Nevertheless, the orientation cover in075 and the possible cover of local sides in171 have not been identified. A choice of local signs, a twofold cover, a section of that cover, and a branched double cover of a cellular surface are distinct data.

**RS:** **154-dihedral-monodromy-half-turn** [unchecked Hua row]; **follow-ups @944** [open]; **EXIT_ONE_TYPE P1d1** [Proved, return claim about coherent reconstruction in a different setup]. The latter is a conditional comparison framework only. **Confidence:** high that the new passage leaves a cover comparison open; medium on the intended cover interpretation in171. No claimed triviality or canonical section follows.

### N127-06 — Four gluing schemes supply a concrete attachment-data problem

**New anchor:** 065:40–44 counts eight standard choices and identifies antipodal pairs to leave four surface cases. New069 gives A1/A2;070 gives B1/B2. A1 has the intended immersion;A2 folds back along shared boundaries;B cases lack the proposed natural map to X. These descriptions depend on the bank chosen to represent generization and on the gluing isomorphism.

**Neighbor anchor:** G03/G04,151:2–9,76–82 and160:5–12,68–74, finite boundary/link audit and regularity requirement; G12,151:2–4 and153:165, fixed arrangement versus symmetry quotient; I07,171:(a)–(h), local realization conditions.

**Relation: add.** This is direct new evidence that a transition graph without gluing isomorphisms and bank conventions can underdetermine the intended geometry. The eight-to-four count is the author's claim under his antipodal identifications, not an independently verified classification of all possible surfaces. The distinction between embedding a marked red curve and forgetting it is already explicit at065.

**RS:** **follow-ups @944** [open]; **MPL_154_127-176 G09** [first-pass lead]; **STRATA A.4**, **BISITE G.10** [Proved, return claims for their specified finite-poset realization]; **EXIT_TOWER D.16** [Proved, return claim for a full deployed face/collar diagram of a complex normal-crossings pair]. The new gluing choices explain why supplying the correct diagram is prior to applying any such reconstruction claim; their hypotheses are not established for these pseudoline surfaces. **Confidence:** high on the four written alternatives, medium on a global realization for each.

### N127-07 — Immersion, edge folding, and double folding belong to different constructions

**New anchor:** 046:9–23 describes `φ:X→Y`, facewise isomorphisms, edge “folding” and vertex “double folding”. New066:6–16 modifies disks and proposes `𝒳→X` as an immersion;069:10 calls A1 an immersion while069:16 calls A2 facewise immersive with a “rebroussement” along a common boundary. New074:31 and076:8 again describe an immersion in the stable-only constructions.

**Neighbor anchor:** I02/I04/I07,171:280–309, branch pairing, even valence, and realization data; I01/W07,160, exceptional-facet draft; I08,166:244–248, marked boundary correspondence.

**Relation: difference.** The new window itself distinguishes map types, so a later statement about an immersed normalized curve or a folded structural map cannot be substituted for another merely because φ or X is reused. The fold loci, source surface, target arrangement, and whether exceptional pieces were removed must be fixed before comparing inverse images or local normalizations.

**RS:** **follow-ups @944** [open]; **MPL_154_127-176 G09** [first-pass lead]. No current RS entry settles these particular immersions. **EXIT_TOWER A.8** concerns a different moduli-space immersion and supplies no theorem here. **Confidence:** high on the distinction of map types, medium on identifying them across nonconsecutive leaves.

### N127-08 — The L versus L∪K₀ correction is a precise but conditional conflict

**New anchor:** 046:27–35 explicitly writes `L=φ⁻¹(X₁)` and warns, in uncertain wording, about neighborhoods around components of K₀. New074:33 writes `L=φ⁻¹(X₁)` for the stable-face immersion;076:8 gives another inverse-image interpretation of L.

**Neighbor anchor:** I01,160:2–10, the cancelled formula `φ⁻¹(X₁^{a|0})=L∪K₀`, followed by “et non =L !”; W07,160:12,68–75; D02,160 date1.1.84 inside the wholly cancelled block.

**Relation: difference; conditional contradiction only.** If the same map, same locus X₁, and same treatment of K₀ were established, the two formulas would conflict whenever K₀ is not contained in L. Those identifications are not supplied. The new046 neighborhood qualification could matter; the superscript in160 is uncertain;074's map type is different; and160 is a cancelled draft. This is a candidate comparison to preserve, not a repaired formula or a proved contradiction.

**RS:** **follow-ups @944** [open]; **MPL_154_127-176 G09** [first-pass lead]; **EXIT_ONE_TYPE P4e** [Proved, return claim that a coarse maquette in a different setting loses link data]. P4e is at most a warning about information loss, not evidence deciding this locus. **Confidence:** high on the two distinct reported formulas and the cancellation; low to medium on their common geometric scope.

### N127-09 — Privileged banks and exceptional boundary markings are reconstruction data

**New anchor:** 046:39–54 uses a marked, privileged side to bulge a face boundary and identify the relative polygon. The margin replaces “suffit” by the uncertain retained “faut”, so the branch-recrossing condition is not to be promoted to a sufficient criterion. New046:70 distinguishes stable/unstable exceptional sides;047:3 invokes exceptional symmetry;052:55 replaces “principale” with “privilégié”.

**Neighbor anchor:** W07,160:12,68–75, cancelled privileged-bank and principal-branch prescriptions; I08,166:244–248, correspondence between marked blue boundaries and unstable exceptional edges; W05/C07,153:142–168, bank data determine a fuseau only outside stated trivial cases.

**Relation: add.** The new source explains geometrically why a privileged side and boundary marking cannot be dropped from a finite encoding: it affects which contour is used and how a face represents a relative position. The later correspondence is a precise continuation of the same type of data, but the cancelled160 prescriptions cannot fill missing hypotheses in either046 or166.

**RS:** **follow-ups @944** [open]; **MPL_154_127-176 G09** [first-pass lead]; **EXIT_TOWER D.16** [Proved return claim, conditional analogy about retaining full attachment data]. No exact RS theorem proves these privileged-bank rules. **Confidence:** high on their presence and relevance; medium on identifying all exceptional categories across the windows.

### N127-10 — Sign propagation is stated, but exceptional verification is postponed

**New anchor:** 055:3–9 says the signs on one face determine the adjacent face and hence, by connectedness, every face. At055:12 the author explicitly states that the verification implicitly excluded exceptional faces and that they require separate examination. At055:15 the proposed recovery from the map `(X,K,S_K)` without critical arcs or L is qualified by “Cela semble”.

**Neighbor anchor:** I03,171:286, possible global side-cover section; I07/Q06,171:280–309, incomplete realization hypotheses and uncertain conditions; I01/W07,160, exceptional-facet corrections.

**Relation: add.** The new claim is a direct candidate for reducing the required finite data, but its own exception clause prevents treating the reduction as completed. Moreover, propagation along paths in a connected adjacency graph is different from showing that independently prescribed signs extend consistently around every cycle. In an existing geometric object the signs may already supply consistency; in reconstruction from arbitrary finite input that is a separate condition.

**RS:** **follow-ups @944** [open]; **154-dihedral-monodromy-half-turn** [unchecked Hua row, relevant to cycle transport]; **MPL_154_127-176 G09** [first-pass lead]. **Confidence:** high on the textual restriction, high on the logical distinction between uniqueness of extension and existence/consistency, medium on the author's intended input class. No contradiction with the later side-cover requirement is established.

### N127-11 — Local criticality transport has explicit exceptions

**New anchor:** 052:33–60 compares critical vertices under `σ_a`; the summary explicitly removes exceptional cases s,t and possible newly critical points from the broad equivalence. It records `N′∈{N−1,N,N+1}` and distinguishes one privileged face. New054–055 continues the sign comparison under local cases.

**Neighbor anchor:** Q10/W09,155:18,37–38,66–67,103–106 and156:183,185, local sweep configurations with “1 n'est pas critique” or “1 est critique ssi2 l'est”; C07/W05,153:153–168, critical-boundary restrictions and trivial fuseau exceptions.

**Relation: restatement at the level of qualified local behavior; add for explicit transition exceptions.** Both windows support case-dependent criticality statements. Neither authorizes a theorem that every elementary sweep preserves criticality. Before equating the cases, one must identify the added curve, crossed vertex, and whether the transition is a reflection across a grand side, specialization, or a full sweep.

**RS:** **follow-ups @944** [open]; no exact current RS row proves these criticality rules. The absent older Hua cube row is not a substitute. **Confidence:** high on the presence of exceptions, medium on a one-to-one matching of the drawn local cases.

### N127-12 — Local good circuits do not imply a complete move presentation

**New anchor:** 070:8 reports failure of B2 to follow/close the desired circuit;071:6 says A1,A2,B_{1|3} give the good supersingular circuits, qualified by “sauf erreur” and an admission of checking errors. At071:8 the A1 circuits are still not understood. New074:42 describes circuits as sterile/trivial;074:44 obtains good supersingular circuits for the opposite gluing;075:4 says general circuits remain mysterious.

**Neighbor anchor:** P05,155 heading and133,156,176 local sequences; U04,137:259–263 questioned closure `D20 ?= D_{6|0}`; U01/M01,133:125–139, the locally answered inverse-circuit question; G11/Q09,176:3–9, mixed move cycle.

**Relation: add.** The earlier-scanned tests sharpen the later notes' warning: success near supersingular positions is a special circuit test and coexists with explicit failure or uncertainty for general circuits. Conversely, the answered inverse question at133 should not be grouped with questions expressly left unresolved. “Good circuit”, closure, inverse description, null homotopy, generation, and completeness of relations are separate claims.

**RS:** **follow-ups @944** [open, direct target]; **EXIT_TOWER E.38** [Proved return claim about endpoint actions and transported smoothing diamonds in another exit-category construction]. E.38 suggests what a complete presentation would need but transfers no result to the pseudoline moves. **Confidence:** high on documentary limits, medium on the intended standard for “bons circuits”.

### N127-13 — Stable-only doubling must retain the directed transition labels

**New anchor:** 072:4–15 returns specifically to a surface built from stable positions. At072:21 the author reduces eight gluing possibilities using a claimed necessary temporal symmetry: the written excluded pairs are `(a,b′)` and `(b,a′)`, and the retained pairs are `(a,b)` and `(a′,b′)`. The second excluded pair has its factors in the opposite order to the preceding Cartesian product, which must remain a reading/typing issue rather than be silently changed. New075:6 contrasts polygons of order n on D with those of order2n on its lift. New076:4–19 distinguishes the two oriented arrows for adjacent stable positions and defines oriented edges as `(D,a)` for a specialization arc or its antipode.

**Neighbor anchor:** G02,151:5–9 and176:3–8, three arrow conventions; X03/C05,151:2–5,153:153–165,154:31–44,158 opening, projective versus lifted/oriented contacts; G12,151:2–4 and153:165, coarse equivalence and symmetry choices.

**Relation: add.** The new passage supplies an explicit reason why forgetting antipodes or identifying the two directed transitions can change the constructed object. The hypothetical double-cover relationship in076 is a question before it becomes a proposed quotient description. It should not be collapsed into a predetermined identification with a projective extension space.

**RS:** **follow-ups @944** [open]; **154-dihedral-monodromy-half-turn** [unchecked Hua row]; **MPL_154_127-176 G09** [first-pass lead]. No current RS establishes the orientation quotient, branch locus, or equivalence of the two surfaces. **Confidence:** high on directed-edge data, medium on how the doubled graph's polygonalization relates to the earlier stable/unstable graph.

### N127-14 — The finite reconstruction proposal is explicit, with numeric identifications still missing

**New anchor:** 047:36–41 proposes indexing the sections of L by `\widetilde I` and “Reconstitution de Σ” from K and its constants: `i(s)∈½ℤ`, `ν(s)∈ℕ`, and edge indices `ν(a)`, distinguishing ordinary and exceptional sides. The exceptional formulas have unresolved `=|≥` readings. New048:16,39 fixes polygon orders2n/4n after the indicated subdivision. New055:15 hopes to discard L from the input.

**Neighbor anchor:** I05/I06/I07/Q06/W10,171:280–309, K,L conditions and the face sum `Σ_s(2ν_s+ε_s)+Σ_aν_a=2n`, with n independent of F; I08,166:244–248, marked-boundary correspondence.

**Relation: add.** These are precise links between an explicit reconstruction ambition and a later-scan candidate list of finite input constraints. The later integer-plus-indicator expression may be worth comparing to the earlier half-integer index, but no text here proves `i(s)=ν_s+ε_s/2` or identifies the two ν conventions. Likewise `2n` versus `4n` can reflect the red/black subdivision and must not be treated as a contradiction without a common counting unit.

**RS:** **follow-ups @944** [open]; **MPL_154_127-176 G09** [first-pass lead]; **STRATA A.4**, **BISITE G.10** [Proved return claims for explicitly supplied finite-poset data]. No current RS proves necessity or sufficiency of this numerical reconstruction system. **Confidence:** high on explicit reconstruction intent, medium on common data types, low on an exact cross-page index dictionary.

### N127-15 — Embedded cyclic order and branch pairing survive any finite reduction

**New anchor:** 046:23 refers to the two branches of K at a vertex;046:54 imposes a recrossing condition on branches of L along a face boundary. New048 introduces valence-two subdivision vertices while retaining the older valence-four vertices and dual cyclic subdivisions of face boundaries. New047:63 gives local involutions at edges meeting a vertex.

**Neighbor anchor:** I02,171:280–284, normalization of the four-valent graph; I04,171:290, even valence of L; G03/G04,151:2–9,76–82, cyclic face words and repeated incidence warning.

**Relation: restatement of the need for geometric incidence; add for concrete boundary and branch constraints.** The new source makes an embedded/cyclicly ordered graph more plausible as the intended input than a bare abstract graph. Its valence-two subdivision also shows why numerical vertices cannot be identified indiscriminately with original crossing vertices. Even valence does not by itself choose how L's branches are paired, nor does an abstract incidence poset retain repeated boundary occurrences.

**RS:** **follow-ups @944** [open]; **STRATA A.4**, **BISITE G.10** [Proved return claims for their particular realizations]; **MPL_154_127-176 G09** [first-pass lead]. The comparison identifies data to retain before invoking a finite-poset model; it does not refute those register statements. **Confidence:** high on the conditional graph distinction and the explicit subdivision, medium on the complete intended source object.

### N127-16 — Adjacent involutions and cartographic generators should not be merged by notation

**New anchor:** 047:44–63 proposes local edge symmetries with an explicitly tentative opening and commuting restrictions at a common vertex. New048:44 writes the inverse transition relation. New073:54–62 writes `N=4n`, `σ_i²=1`, `ρ_i=σ_{i−1}σ_i`, and that adjacent σ_i commute iff the corresponding ρ_i is involutive.

**Neighbor anchor:** M02/M06,135–140 and157:9–13, cartographic relations; U02,135/138/157, geometric interpretation of σ₀ andσ₁; W01,135:3–5, rejected inverse guess for σ₀; W03,140:8–23, corrected exchange and cancelled equivalent-looking formula.

**Relation: add, with a required difference of indexing systems.** The new cyclic family of `4n` indexed involutions is not automatically the later three cartographic generators σ₀,σ₁,σ₂. The algebraic fact about a product of two involutions is immediate, but assigning it the correct geometric permutations requires specifying the acted-on frame set, indices, and action convention. A finite permutation check is useful only once those data are fixed.

**RS:** **follow-ups @944** [open]; no exact current RS row proves this pseudoline generator dictionary. **BISITE G.10** is a separate finite-poset dictionary, not support for these equations. **Confidence:** high on the formal distinction and displayed identities, medium on a common geometric realization of the different generator families.

### N127-17 — Endpoint and link data remain a barrier to the surface claim

**New anchor:** 067:4 explicitly lacks a geometric interpretation of the holes or filled-in vertices in terms of Σ. New075:17–076:4 asks whether the glued surface is the same cellular surface or a ramified double cover. The four gluing cases in065–071 provide transition data but do not supply a full vertex-link verification for all cases.

**Neighbor anchor:** U05/U06/G01/G03/G09/G13,151:76–82, accessible face circuits but questioned incident endpoints and an unsettled blocking construction; G06,153:165–168, isotopy-class bijection versus coherent choices.

**Relation: add.** The new leaves locate an antecedent form of the same attachment difficulty: interpreting completed boundary circuits as the correct vertices, rather than merely attaching disks by an abstract rule. The later-scan blocking problem is not resolved by the new tentative double-cover description. Existence of choices, identification up to isotopy, and contractibility/coherence of all choices must remain separate.

**RS:** **follow-ups @944** [open, strengthened but not settled]; **MPL_154_127-176 G09** [first-pass lead]; **EXIT_ONE_TYPE P1a1/P1d1** [Proved return claims concerning normal links and coherent gluing in their own setting]; **EXIT_ONE_TYPE P3c-general** [open, a different normal-crossings threefold problem]. The new source supplies a concrete incidence test, not a proof or counterexample for P3c-general. **Confidence:** high on the explicit gaps, medium on identifying the exact same intended vertex model across these leaves.

### N127-18 — Finite equations and extension-poset results cannot replace a surface audit

**New anchor:** 047:39–41 and055:3–15 concern recovery from K, numerical data, and signs;065–076 preserves different gluings and unresolved vertex/circuit interpretations.

**Neighbor anchor:** I05/I06/I07,171:280–309, conditional parity/global counts and sufficiency problem; G04/G10,151, regularity and finite-base warnings; X01/X02,151/154, extension-poset homotopy versus the intended cellular surface.

**Relation: difference.** The finite numerical constraints are plausible necessary filters. They do not decide disk closures, boundary identifications, vertex links, global side monodromy, or uniqueness of the reconstructed arrangement. The neighbor's external rank-three extension-poset theorem is a literature lead whose hypotheses and identification with the manuscript object still require an independent comparison; even a homotopy-sphere statement would not by itself prove this particular glued object is a surface.

**RS:** **follow-ups @944** [open and explicitly already records the homotopy-versus-surface distinction]; **WG2 B15 (§1.2)** [unchecked planning question]; **STRATA A.4/BISITE G.10** [Proved return claims for specified finite minimum-vertex models]. These pages do not settle the unrestricted open-test realization question over ℝ or identify the geometric surface with an Alexandrov base. **Confidence:** high on the logical limitation, medium on the eventual best finite model. The cited modern theorem was not independently rechecked by this child agent and should not be cited as independently verified from this support file.

## Classification constraints

### N127-19 — Tame-topology branch: supported as a concrete relative-position program

**New anchor:** 047:38–41 (“Reconstitution de Σ”),061:9–31 (polygon transport on relative-position faces),065–076 (polygonal surfaces, stable positions, immersion into X, antipodal gluing), especially072:4 (“faire une surface avec les p.r. stables”) and076:10–19 (“Description combinatoire”).

**Neighbor anchor:** P01,151 opening and153–155, `X*=Rel(Σ)`; P02,151,154–158,171, relative positions, sweeps, dual projective planes; P05,155–156. P01 reports the specific Esquisse §8 counterpart at cote119/50, manuscript48, lines2212–2223 and published1997§8p41.

**Relation: add.** The new window supplies unusually concrete evidence for the first classification option: combinatorial reconstruction of pseudoline systems through a cellular space of relative positions, with immersed-curve and gluing questions. “Curves in the plane” alone is too narrow: doubled projective pseudolines, local orientation systems, cellular surfaces, and immersion/folding distinctions are essential. This remains a problem-driven branch of tame topology; the window does not state a general axiomatization of a tame category.

**RS:** **MPL_154_077-126 C01** [first-pass classification lead]; **follow-ups @944** [open and explicitly identifies the Esquisse §8 relative-position program]; **WG2 B15 (§1.2)** [unchecked plan item]. **Confidence:** high for the concrete subject, medium-high for the archival-program identification conditional on the parent's independent check of the supplied Esquisse passage. This child reports the neighbor's exact primary-source lead rather than independently verifying its published citation.

### N127-20 — The 1986 precursor hypothesis is not established by shared reconstruction language

**New anchor:** 047 reconstruction,055 possible elimination of L,065–076 geometric assembly. New048 has an uncertain7.2.1984 date;058/065 have3.1.84 and0614.1. No text in the examined new window expressly identifies a 1986 geometry-of-forms program or cote156.

**Neighbor anchor:** P03,160 cancelled date/heading and151/171 construction; D02/D03,160 and reused printout dates; P01/P02 for the more precise relative-position identification.

**Relation: restatement of the bounded historical conclusion; add for earlier concrete reconstruction evidence.** Shared concern with assembling geometry from finite data makes a comparison to later work reasonable, but does not establish a specific genealogy, common axioms, or a passage from this construction to the1986 project. The “neither” option is too strong if it denies the well-supported relative-position/tame-topology connection; it remains possible only if the alternatives are defined much more narrowly than the source evidence warrants.

**RS:** **MPL_154_127-176 P03**, **MPL_154_077-126 C03**, and **MPL_156-1+156-2 P11** [all first-pass leads]; **WG2 §3.1 #2** [unchecked planning item]. P11's summary of equivalence-of-categories/cutting passages at156-2/008–010,015–017 is only an additional comparison lead; no actual cote156 text was provided to or checked in this child task. **Confidence:** high that these sources do not establish the genealogy; medium for the broader historical relation. An absence claim is restricted to this window, not the whole archive.

## Suggested finite research audit, not a claim of completion

The strongest next test supported by both windows is to specify, for one small labelled arrangement, the entire finite data set before any theorem is claimed: stable and unstable position states; the chosen doubled/projective convention; oriented transition arcs and antipodes; the actual polygon bijections; side signs and exceptional crossings counted with their corrected multiplicity; boundary words with repeated occurrences retained; completed vertices and their links; and the map to the ambient projective surface. This combines new047–055,061–076 with neighbor G03/M06/I02–I08, rather than discarding the difficult data.

Such a test has three separate outputs: consistency of the local reflection/sign formulas, verification that the assembled object is a surface of the intended type, and proof that it represents the desired relative positions and their admissible deformations. A successful first output alone would not settle **follow-ups @944** or Hua's full monodromy formulation. This is an own proposed research organization, medium confidence, not work performed or an additional register result.

## Context-source boundary

Neighbor notes cite numerous entries from their own older RESULTS_STATE and STATEMENTS files, including `MPL_150_044-084 N18/Q2`, `STRATA C.1/C.5`, `BISITE D.2/D.3`, and Hua `154-generisation-cube`. Those citations are accurately part of the neighbor's reports, but several do not occur in the **current** RS supplied for this package. This support file has therefore used current identifiable RS IDs and has not promoted an absent older entry to a current or independently verified result. It also has not imported original source-page readings from the neighbor notes into the frozen transcription.

## Correction to this support report after review

The initial transient reading aid incorrectly skipped prose after a one-line TikZ block. An audit found exactly two affected page files,064 and072. Both have now been read directly without the filter. The earlier sentence that064 stops after “donc” was false:064:18–20 concludes surjectivity, and064:22–33 gives the singularity-parity argument. Those passages are now reflected in the priority findings and N127-02/N127-04; the temporal-symmetry paragraph at072:21 is now included in N127-13. The frozen transcription was never changed. This correction concerns the support analysis only.
