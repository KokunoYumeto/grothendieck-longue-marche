# Parts B and C: coverage against the prompt

This is a coverage register, not a claim that the prompt is complete. Statements B.1–B.42 are in sections/B.tex. Statements C.1–C.12 are in the parent's sections/C.tex, and C.13–C.19 are in sections/C_extra.tex. References to Part F and Part A identify the separate contributors' proved comparison maps. Every unresolved request below remains **INCOMPLETE**.

The local point-section theorem used in B.7, B.15, B.19, B.29–B.30, B.32–B.33, B.35 and B.38–B.41 is the prompt-stipulated October 6, 2026 preprint. Its precise point of use and inspected proof chain are in B_readings.json. Its unrefereed provenance is retained. The universal-curve classification used in B.18 and B.23 is the supplied Luo–Watanabe claim, with its stated range retained. Neither input is presented as independently refereed in full.

## Manuscript anchors

The La Longue Marche passages below are all in **cote 140-2**, whose folios run from 1 to 292. A folio number on one scan also anchors the following continuation scan; the register does not invent recto/verso labels. The checked transcription files are in inputs/background/longue_marche.

| Topic | Section, folio and scan anchors | Package |
|---|---|---|
| Case III, sections and injectivity | §8, scans 61–65; folio 29 begins at scan 62 and folio 30 at scan 64 | LM_P07 |
| Cuspidal sections, uniformizers and tangents | §9, scans 72–79; folios 34, 35, 36, 37 begin at scans 72, 74, 76, 78 | LM_P08 |
| The groupoid/point formalism | §32, scans 395–410; folios 200–207 | LM_P040–LM_P041 |
| Equation (25) | §32, folio 207, scans 409–410; admissibility reservation on scan 408 | LM_P041 |
| Axioms ①–⑥ | §32, scans 412–421; folios 208–213; ⑤ on scan 418, ⑥ on scan 420, fixed-kernel discussion on scan 421 | LM_P042–LM_P043 |
| Withdrawn provisional admissibility statement | §32, folios 218–220, scans 431–436 | LM_P044 |
| Real structures and cusp placement | §33, folios 221–226, scans 437–448 | LM_P044–LM_P045 |
| Prediscretizations and complex conjugation | §29, folio 191, scans 377–378, equations (29)–(30) | LM_P038 |
| Direct admissibility criteria | §34, folio 243, scan 480; folio 247, scans 487–488 | LM_P048–LM_P049 |
| The discrete lattice of a rational point | §34, folio 248, scans 489–490 | LM_P049 |
| Teichmüller-tower avatars | cote 148, scan 43, table's algebraic-over-Qbar row | MPL_148_029-072_transcription.tex |
| Descent, point germs, inertia, coverings | cote 143, scans 2–12, with competing top/bottom foliation retained in the transcription | MPL_143+141_transcription.tex and pages_143 |

Editorial alternatives and their mathematical effect are recorded separately in B_C_editorial_readings.json. The source theorem audit is B_readings.json; it must not be confused with a new reading of manuscript images.

## B(a): cuspidal sections and tangential parameters

**Status: the local constructions, packet calculations and uniform global intrinsic recognition are proved; the narrower GT-automorphism-only formula remains INCOMPLETE.**

| Request | Result and exact comparison | Remaining scope |
|---|---|---|
| Uniformizer splitting; multiplication by a principal unit | B.3 constructs the compatible-root splitting of the henselian local Galois sequence and proves equality for multiplication by a unit congruent to 1 | Completed in the stated equal-characteristic-zero local setting |
| The H¹ torsor and geometric tangent subtorsor | B.3 identifies splittings modulo inertia with H¹(k,Zhat(1)) and the nonzero tangent line with its k× Kummer subtorsor; F.17 gives the relative line-bundle and extension formulation | Completed with the actual coordinate ambiguity retained |
| Comparison with Deligne and the 1983 packet | B.3 identifies the finite-cover fibre functor through normalized local covers and principal parts; Deligne §§15.13–15.26 and Stix Proposition 8 were read at this use | Completed |
| Ramified morphism and norm of forms | B.4 proves the packet map from t=a u^d(1+h), namely c↦a c^d, and states and proves the separate trace and determinant-norm formulas for logarithmic differentials | Completed |
| Every abelianized fibre | B.5 gives all positive-genus fibres, including collapse of an entire packet in the one-cusp case. B.6 gives genus zero: injectivity for at least four punctures; the three pairwise, distinct tripod collisions; the two full Gm packets; the genus-zero zero/one-puncture collapse | Completed for the rational-point and rational-cusp domain over the stated finitely generated characteristic-zero fields |
| Point and packet disjointness in the full group | B.3, B.7 and B.11 retain the actual decomposition-group maps and the full packet-injection theorem | Completed in the stated arithmetic ranges |
| Limits near a p-adic cusp | B.8 proves that the tangent parameters k× are dense in their packet and that the accumulation set of actual point sections with points approaching the cusp is the whole packet | Completed for finite extensions of Qp |
| Global local-place tests | F.19 computes the everywhere locally geometric subgroup K×·widehat(O_K×) and its quotient widehat(O_K×)/O_K×; F.20 refutes exhaustion by powers of one chosen unit; F.21–F.22 give the precise idelic range and its limitation | These exact local tests do not yet remove the unit-completion defect over general number fields |
| Global characterization by specialization | F.23 proves precisely the smooth marked-trait, uniformizer-specialization statement, with coefficient a and coordinate change a↦a b^(−d) | Completed with the trait and uniformizer data retained |
| Intrinsic equation selecting every geometric parameter in the single tripod | F.45 gives one relation using two open Hom maps from an open subgroup of the ambient arithmetic tripod, with local degrees one and two and equal section images. Their Kummer equations force the parameter to be a genuine field element. Marked Belyi supplies witnesses for every such element | Uniform global recognition is completed, including germs. The stricter request for a formula using only GT automorphisms remains open in F.24 |

The source assertion of scan 79 is therefore tested through its actual abelianization map. Distinct geometric centres in positive genus remain distinct, but the packet-to-abelianization map need not be injective within a one-cusp packet. The genus-zero collisions are explicit; no full-group collision is inferred from them.

## B(b): injectivity and failure outside the field range

**Status: proved.** B.1 proves the semi-abelian no-divisible-elements statement over finitely generated extensions of Q and the consequent injectivity of the point map into abelianized section classes. The false auxiliary assertion that G(K) itself is finitely generated when G has a torus is removed; the proof uses valuations for the torus, Mordell–Weil for the abelian quotient and finite torsion to pass through the semi-abelian extension.

B.2 computes the failure for P¹ and A¹, gives the two tripod points 2 and 3 over R in the same real component, and gives 2 and 2+t over the p-adically closed Hahn field Qp((t^Q)). The Hahn field is proved not sub-p-adic: an embedding into a finitely generated extension of Qp would preserve the infinitely divisible nonidentity element t, whereas the intersection of all power subgroups in such a field is {1}. This does not require the embedding to fix a previously selected copy of Qp. The example has no finite-generation claim and is not a counterexample to the separate B(d) request.

Cote 143 scans 4–5 are covered by the same B.1 proof after passing to a common finite field of definition. Equality of point-section germs means equality on one common open Galois subgroup, hence equality of the two points by that finite-field injectivity.

## B(c): all six axioms and the withdrawn provisional conclusions

**Status: geometric and specified local/descent cases proved; the full intrinsic implication diagram remains INCOMPLETE.** B.tex first types the axioms of scans 412–421 and the separate premises and conclusions of scans 431–433. The following table records their actual range.

| Axiom | Exact content used | Proved coverage | Remaining intrinsic request |
|---|---|---|---|
| ① | Restriction of admissibility to an open subgroup | B.13: actual finite base change of curves and points; the converse written as a marginal question is not silently included | An arbitrary proposed class of intrinsic outer actions has not been characterized |
| ② | Filling a stable finite set of holes, with the resulting type hyperbolic | B.13: actual open immersion into the partial completion, equivariant for descent | The full abstract admissibility predicate is still unavailable |
| ③ | Trivial fixed subgroup for an effective admissible action | B.10 proves more: every full section and every open Galois subgroup has trivial geometric fixed group, over fields finitely generated over Q and finite extensions of Qp | Completed for these full section actions; it does not separate point and cusp packets |
| ④ | An admissible effective lift exists after an open restriction | B.13: a closed point of the actual curve provides the finite field extension and the lift | Existence for an arbitrary intrinsically specified outer action remains unproved |
| ⑤(a) | The deleted point's canonical filled class is excluded from the admissible image | B.13 on actual point classes; B.29 computes its entire full-section fibre as the new cusp packet | The word “admissible” cannot be erased: the full packet maps to the deleted point |
| ⑤(b) | The deletion map is injective on admissible classes | B.13 for actual points; B.29 gives singleton fibres over every surviving actual point and over each specified old cusp class | Fibres over unknown nongeometric filled classes are uncomputed |
| ⑤(c) | Every other admissible filled class lifts | B.13 for points; B.7 over finite Qp; B.29 for all opens of a proper number-field curve satisfying the stated finite-descent equality | The literal final sentence of scan 418 omits the excluded class P and conflicts with the display. The display-with-complement is tested. Unrestricted number-field point-surjectivity remains open |
| ⑥ | Descent of the punctured action extending a given action over an open subgroup and a compatible filled action | B.13 proves existence by actual finite-set descent and fixed-kernel uniqueness using the exact arithmetic pullback and relative Isom theorem, including unordered removed sets; both filled and punctured curves remain hyperbolic | B.12 refutes the implication from the one condition L^Γ′=1 alone. The further normalizer-surjectivity condition is exact; the general intrinsic existence assertion remains open |

For a finite extension of Qp, B.7 supplies the complete point/cusp classification for every hyperbolic curve, and therefore the deletion statements have no unknown section fibres. The field remains in the same class after finite extension. For a number-field proper curve X with X(A_k)_bullet^(f-cov)=X(k), B.29 supplies the complete point/cusp classification for all its hyperbolic open subcurves over that field. The germ/Γ-set version ranges over all finite extensions of k; a finite-descent equality assumed at k alone is not asserted at every such extension.

The manuscript's own scan 421 says that L^Γ′=1 implies uniqueness and that existence means surjectivity of the normalizer projection. B.12 agrees with that written distinction. Its finite S3 example refutes the stronger implication demanded in the prompt, not the manuscript's distinction.

| Provisional conclusion | Anchors and proof | Exact status |
|---|---|---|
| (a), full Γ-fixed group | Scans 432–433, folios 218–219; B.10 | Proved for every full section, whether point or cusp |
| (a), stronger cyclotomic-kernel guess | Scan 432's superscript is still doubtful; the 1983 statement identifies ker χ precisely. F.1 proves trivial cyclotomic centralizer for point germs and the inertia centralizer for cusp germs | Proved in the precise 1983 arithmetic formulation; the 1981 superscript is not editorially resolved |
| (b), distinguished point after filling one hole | Scan 433; B.13 and B.25 identify the filled rational point and its separation from the remaining cusps | Proved for realized marked curves; arbitrary intrinsic outer-action realization remains open |
| (c), filling an effective admissible action | Scan 433; the target π(i) versus R(i) remains doubtful. B.13/B.29 use the actual quotient by the filled inertia | Proved on point actions and in the complete local/descent ranges. No silent selection of the doubtful target |
| (d), injectivity and complement {P} | Scans 433–435; B.13/B.29 give the field-point version. B.16 gives the actual meeting diagonal and constant graphs and the exact disjointness correction | The asserted relative image-complement statement is withdrawn by the author and refuted in that unrestricted reading |

Other explicit requests in B(c):

| Request | Coverage |
|---|---|
| Equation (25), scans 409–410 | B.28 proves injectivity for actual distinct marked points over the stated fields. The configuration (0,1,∞,2,2+t), composed with a uniformizer splitting, refutes the unrestricted assertion for arbitrary moduli sections. The admissibility reservation on scan 408 remains part of the manuscript statement |
| Transcendental packets normalize a loop | B.11 proves this for every packet class, by the map into its cusp decomposition group, including classes outside the geometric tangent subtorsor |
| Pathological effective lifts and classification of all lifts | B.11 proves the centre-free Aut(Δ) pullback and its splitting classification by nonabelian H¹; a cusp packet gives the requested effective lifts of the same geometric outer action |
| Proper, affine and birational forms | B.7 and B.29 give the actual neighborhood/deletion maps. F.13 gives the exact function-field inverse-limit map and its centralizers. F.14 checks Bresciani's equivalence with universal birational liftability after every finitely generated base extension, including the necessary K(t) step |
| Full requested implication diagram without extra quantifiers | INCOMPLETE. Ordinary birational liftability at one field is not turned into the universal lifting hypothesis, and unrestricted number-field sections are not proved to supply rational pro-points |
| More than one removed point | B.30 proves that the fibre over pairwise distinct actual coordinate point classes in Conf_n(U) is exactly the actual configuration section; B.13 handles unordered descent and fixed-kernel uniqueness |

## B(d): the p-adic counterpart

**Status: finite local fields and all isotrivial hyperbolic curves over finitely generated Qp fields are completed using the stipulated theorem; the general nonisotrivial case remains INCOMPLETE.**

B.7 supplies the complete affine neighborhood proof, including cofinal finite étale neighborhoods with completion of genus at least two when the initial completion has genus zero or one. B.8 computes the packet as Zhat×O_k×, the tangent subgroup as Z×O_k×, the cokernel as Zhat/Z, and all point limits near a cusp. B.9 treats proper genus zero, including a pointless anisotropic conic with its unique section, and genus one. For an elliptic curve the quotient of H¹(k,TE) by E(k) is T H¹(k,E), noncanonically Z_p^[k:Qp]; the point image is closed. A genus-one torsor splits precisely when its class lies in the maximal divisible subgroup, with the actual degree-two obstruction written. B.10 and B.13 give the axiom coverage in the preceding table.

B.39 extends the open/trivial/cuspal geometric-image trichotomy to every sub-p-adic field by descending one compatible finite-gerbe tower to a countable coefficient field and embedding that field, with all its relations retained, into a finite p-adic extension. B.38 and B.40 then prove unramification for every proper hyperbolic curve spread over a smooth p-adic model, in every dimension. The actual cartesian generic-fibre comparison gives a bijection between its generic Galois sections and relative fundamental-group sections of the model, and these are point-theoretic on every finite-extension fibre.

B.41 completes the point-or-cusp dichotomy for every isotrivial hyperbolic curve over a finitely generated extension of Qp. The proper constant case uses unramification followed by the open Hom theorem or the local point theorem. Finite Galois descent retains the necessary centralizer calculation. The affine proof uses high-genus neighborhoods whose compactifications remain isotrivial by the actual finite-cover base-change equivalence. For affine curves the entire marked open curve must become constant; constancy of its compactification alone is not the hypothesis. The remaining general nonisotrivial problem is realization of the point-theoretic relative section. The inspected Saïdi theorem has a non-Tate cyclotomic hypothesis which fails for a p-adic Tate elliptic curve, and Bresciani's inspected theorem has number-field and global finiteness hypotheses. The earlier bare cyclotomic-normalizer route remains unavailable, but B.38–B.40 replace it for unramification with the actual tripod-to-Gm map and the proved trichotomy. B.42 proves that the finite-cover local-point principle in Saïdi Definition 0.2(vi) also fails over a finite p-adic base: a compatible Tate isogeny tower splits over every closed point but has no generic section. Its nonzero quotient to Zhat vanishes on every closed-point decomposition group. The inspected Nagamachi relative-realization theorem requires the generic-field section conjecture itself, so it does not fill this remaining step. The Hahn example in B.2 lies outside the finitely generated field class.

## B(e): relative sections and universal families

**Status: complete constant-family decomposition and several universal-family obstructions; the general relative classification remains INCOMPLETE.**

| Request | Coverage and proof map | Remaining scope |
|---|---|---|
| “Strictement distinctes” | B.16 proves that deletion retains exactly the geometric sections disjoint at every geometric point of the base | The naive complement of one global section class is refuted by actual meeting graphs |
| Constant-family raw surjectivity | B.16 gives an actual cusp splitting of Π_U×_GkΠ_S that is not the graph of a morphism | Refuted as an unrestricted full-section claim |
| Every constant-family section | B.33 proves the disjoint decomposition into dominant morphisms, noncuspidal field-section classes, and relative cusp torsors H¹(Π_S,Zhat(1)); the product-extension and cocycle maps are explicit | The number-field noncuspidal field-section term remains the original point-surjectivity problem |
| Relative cusp parameters | B.33 proves the identification with lim_n O(S)×/O(S)×n over a number field using Kummer and finite generation of Pic(S) | This is the displayed power completion; it is not asserted compact or identical to the completion for all finite-index subgroups |
| Proper constant fibre over a finite p-adic field | B.32 proves every section is the graph of a unique morphism, using all finite-extension point-theoretic tests and then the exact open Hom theorem | Completed for the stated hyperbolic source curve and proper hyperbolic fibre |
| Generic sections of a proper family over a smooth p-adic model | B.38–B.40 give the exact cartesian comparison, kill every divisorial inertia through the tripod-to-Gm map and proper-fibre trichotomy, and identify generic sections with relative fundamental-group sections | Unramification is completed in every dimension. The relative sections are point-theoretic, but their algebraic realization for nonisotrivial families remains incomplete |
| Isotrivial curves over finitely generated Qp extensions | B.41 proves the full point-or-cusp classification through the constant-family Hom comparison, finite Galois descent and the compactified neighborhood tower | Completed for the precise isotrivial marked-curve hypothesis |
| Dominant functoriality | The relative Hom map is A:relative-hom; B.26/B.32/B.33 apply it to h:Π_S→Π_U only when its image is open. F.29–F.31 supply the required infinite-index classification | No dominant-family theorem is applied to a nondominant graph without the extra argument |
| The printed Mochizuki–Tsujimura Theorem F(ii) | B.34 refutes its literal interior-point reflection for arbitrary dominant morphisms: filling the cusp 2 sends every member of that packet to the interior point 2. All local hypotheses and the actual source definitions are checked | The counterexample concerns this precise assertion, with no extrapolation to RNS Theorem A or Isom results |
| Correct dominant-morphism fibre over an actual point | B.35 computes the fibre as the rational interior points and all rational cusp packets over that point. Thus geometricity is reflected for noncuspidal source sections, and for all source sections under finite maps | Uses the stipulated local theorem and finite-support descent. The finite-etale special case is also proved directly without that theorem |
| Tautological complete classes after puncturing | B.17 proves non-liftability using the μ_m-gerbe of roots of the normal line, its Chern class and the test-curve degree | Completed even after arbitrary finite étale base cover; it does not classify all complete classes on that cover |
| Universal complete family, g≥3,n≥1 | B.18 uses the exact supplied Luo–Watanabe classification to obtain no section of the punctured family; the stated full symplectic level versions are retained | General open subgroups need not be covered by the quoted level range |
| Universal unpointed family, g≥3 | B.23 deduces nonsplitting by the one-pointed pullback and the diagonal-versus-constant comparison | Completed in the specified compatible level range |
| Low genus and étale multisections | B.24 constructs M0,4 multisections, nonzero torsion multisections over M1,1, and the six Weierstrass points over M2 | These examples refute a uniform no-multisection assertion; a complete classification for g≤2 is unfinished |
| General nonconstant family over a smooth number-field curve | B.17, B.30 and the source-image classification give constraints | INCOMPLETE: no argument obtained makes an arbitrary family section a geometric section |
| All open subgroups of the moduli fundamental group | B.17 still rules out lifts of tautological complete classes | INCOMPLETE: additional complete classes on arbitrary covers have not been classified |

## B(f): direct admissibility tests and moduli sections

**Status: necessary tests, uniqueness, all stable-boundary non-admissibility including closure, and finite p-adic DM-curve classification proved; global sufficiency and general outer realization remain INCOMPLETE.**

B.25 types the tests of scans 480 and 487–488 through the actual filling maps. The distinguished filled points are pairwise distinct for a marked curve; on the genus-zero four-point space the cross-ratio gives the explicit isomorphism M0,4≅P¹−{0,1,∞}. The Isom theorem identifies two already realized marked curves when their outer actions agree. No second realization of an arbitrary outer action is supplied by that injectivity statement.

B.19 proves the full point/cusp statement for the relevant hyperbolic Deligne–Mumford curves over a finite extension of Qp, including M1,1 and the S3 quotient of the tripod. The characteristic subgroup N is chosen inside a geometric scheme-cover subgroup; N·s(G_k) is then a scheme neighborhood over k itself. Automorphism groups are retained in the groupoid statement. Steklov's exact curve-neighborhood and full-faithfulness steps were checked where used.

The global sufficiency test for M0,4 is exactly the unrestricted tripod noncuspidal section-surjectivity problem and remains unfinished. The number-field surjectivity statement for M1,1 remains unfinished. B.28 gives one explicit boundary-collision moduli section violating the distinctness test, and B.17 gives the exact normal-line obstruction for tautological puncturing.

B.36–B.37 now prove the full stable-boundary non-admissibility statement over number fields. A packet is the image of the punctured henselian neighborhood of a rational boundary residual gerbe; this retains the finite stabilizer in a stack. Each node gives the explicitly injected kernel (a,−a,0) of the local map (a,b,d)↦(a+b,d), with cyclotomic action after accounting for the finite node and branch permutations. Finitely many stable multicurve types and the compact inverse image of the procongruence group in Aut(Δ) give a compact space of pro-simple tuples. The permutation/±χ incidence condition is closed; its projection is closed, so it contains the closure of the entire packet union. An actual smooth peripheral realization would put one of these nonperipheral procyclic groups in a cusp inertia group by the cyclotomic-normalizer theorem, a contradiction. This excludes every boundary packet and its closure even as a germ over finite extensions. It does not claim that all boundary sections violate every one of the manuscript's preliminary distinctness tests: in some limiting types those tests impose no condition.

Carlson–Corwin's actual theorem was read in its scheme scope: the closure is independent of a normal-crossings compactification. For the DM stack B.37 explicitly constructs the local finite quotient and uses its canonical stable compactification. No arbitrary-stack compactification theorem is attributed to that source. The stable-boundary exclusion uses no stipulated p-adic section theorem.

For realized finite-p-adic hyperbolic curves, B.7 proves that normalizing no cusp inertia is exactly the point alternative, so no additional Frobenius test is needed for those section classes. Over number fields B.11 and F.1 identify the cusp and zero-cyclotomic-centralizer alternatives but do not establish point-surjectivity for the latter. No sufficient Frobenius condition or intrinsic outer-action realization criterion has been produced. These parts remain **INCOMPLETE**.

## B(g): the lattice

**Status: proved.** B.20 gives the elementary tripod argument, and B.31 completes every hyperbolic type with the exact Hoshi–Mochizuki archimedean intersection theorem. A specified complex embedding and rational base point produce the discrete lattice in the full profinite geometric group. The actual based Galois action permutes these lattices; the stabilizer of the lattice is the decomposition group of the archimedean place, hence either trivial or generated by its complex conjugation. The oriented lattice has trivial stabilizer. The passage from an outer intersection statement to the actual based subgroup is written. A rational point does not erase the required embedding and orientation data.

## Added Part B tasks

| Task and anchor | Coverage | Status |
|---|---|---|
| Cote 148, scan 43, algebraic-over-Qbar tower entry | B.21 proves that a finite-type curve and an algebraic point have a common finite field of definition, hence a point-section germ in the sense of scans 61–65. The stronger universal-Q-model reading is refuted by an elliptic curve with j=√2 | The meaningful point-germ statement is proved; the two doubtful parenthetical fragments remain provisional |
| Cote 143, scan 2, constants and descent | B.21 gives the constants-preserving absolute-automorphism map, its kernel, its open image, and the partial splitting from a field of definition. In the hyperbolic-curve range it also proves effectivity of continuous semilinear splittings by finite Galois descent | Proved in this precise geometric formulation; arbitrary effective descent is not inferred solely from an outer action |
| Cote 143, scans 4–5, point determined by germ | B.1, using the actual restriction to a common finite extension and semi-abelian Kummer injection | Proved under the manuscript's semi-abelian embedding hypothesis |
| Cote 143, scans 6–8, Kummerian boundary structure | B.22 gives the inertia maps, path dependence and cyclotomic equivariance in dimension one | Proved |
| Crossing of boundary components | B.22 keeps the actual map Zhat(1)^r→π1(U); the example P² minus two lines gives (a,b)↦b−a with diagonal kernel | Proved; injectivity of the local inertia map is refuted in general |
| Cote 143, scan 12, passage to a finite étale cover | B.22 gives the double-coset description and the induced inertia/germ maps | Proved; the entire “Programme” of intrinsic reconstruction of G_Q is not claimed complete |
| Added GT₀ stabilizer task, cote 143 scans 29–31 | Owned by Part A: A:two-section-stabilizer and A:root-orbit-stabilizer. The exact ambient action on section-image subgroups includes their arithmetic domains. For one chosen root the stabilizer is G_Q(√−3); for the orbit of both roots it is G_Q | Parent should cite A's full statements and proofs. This task is deliberately not duplicated in B.tex |

## C(a)–C(d): base coverage

| Task | Manuscript anchors | Results and exact status |
|---|---|---|
| C(a), discrete real sections and fixed groups | §33, scans 440–445, folios 222–225 | C.3 identifies components with discrete section classes and centralizers 1 or Z |
| C(a), profinite real sections and fixed groups | Same, with the explicit completion map from finite equivariant covers | C.4 proves the section bijection and centralizers 1 or Zhat in every hyperbolic curve genus, by the verified finite-subgroup and centralizer comparison |
| C(a), real packet and cusp placement | Margin of scan 437, folio 221 | C.5 computes the two local torsor elements and shows their map to global section classes can have a nontrivial fibre; C.6 proves the flagged incidence-graph reconstruction of real cusps, their components and cyclic order |
| C(b), prediscretizations | §29, scans 377–378, folio 191 | C.7 proves the explicit map to conjugates of complex conjugation and the archimedean-place quotient P_a/±1, using the faithful arithmetic quotient |
| C(c), localization and tripod formulas | §29 comparison and §33 real sections | C.8 proves the actual restriction along the real decomposition group, lists the three involution classes and all six tangent identifications; C.9 adds the explicit class-two obstruction |
| C(d), discrete moduli types and centralizer index | Scans 437–448, folios 221–226 | C.1 proves the corrected count g+2+floor(g/2). C.10 proves the effective-lift orbit and the index of the image of the centralizer map. C.11 treats labelled real points, unordered markings and conjugate pairs |
| C(d), full profinite moduli statement in genus≥3 | The requested extension of scans 445–448 | C.12 records the initial gap. C.13–C.19 below prove injectivity and further exact reductions, but the requested surjectivity and full centralizers remain INCOMPLETE |

At a real cusp, H¹(R,Zhat(1))=Z/2 is a two-element local torsor. Its two maps to global section classes need not have different images: C.5 uses E:y²=x³+x with its origin removed and connected real locus. C.6 retains the two local flags even in that case; this is necessary for the subsequent cyclic-order comparison.

The compact-surface count on scan 439 initially counts only nonorientable quotient surfaces; the margin adds orientable quotients. C.1 proves both quotient-double constructions and therefore their exact relationship. In scan 447 the map of effective centralizers has kernel Z, so C.10 computes the index of its image, not an index of the unembedded source group. When there are no real components there is no selected effective lift and the corresponding index assertion is vacuous.

## New C.13–C.19 and the exact remaining genus-three cases

| Statement | Proved advance | Comparison map and residual question |
|---|---|---|
| C.13 | Distinct actual real topological types remain distinct after passage to Out of the full profinite surface group | The exact centre-free pullback recovers the real extension, section classes recover the number of ovals, and their unique mod-two centralizer classes recover the dividing invariant. All six genus-three actual types remain distinct |
| C.14 | The same injectivity with labelled real markings and unordered real/conjugate markings, including cyclic-order and reversal data | The actual finite real cover diagrams and flagged cycle-cover maps identify centralizer monodromy. They force exponent +1 or −1, not an arbitrary profinite unit. In the dividing case the integral oval relation forces a common sign |
| C.15 | The complete fibre and centralizer formulas for P→Q with kernel K | Fibres are C_Q(bar τ)-orbits in H¹(C2,K); the centralizer image is the stabilizer of the selected cohomology class. The action is explicitly g·[k]=[gkα(g)^(−1)] |
| C.16 | Every reflection and its centralizer inside the closed genus-three hyperelliptic mapping-class subgroup | The subgroup embeds in the full completion by the verified hyperelliptic congruence theorem. Goodness is proved for that subgroup. Six explicit curve equations realize all six actual real types |
| C.17 | The entire congruence centralizer for each of the five genus-three types with a real oval | For C the discrete positive centralizer, its closure in P maps isomorphically to C_Q(bar τ). The full centralizer is K^τ semidirect that closure. The value of K^τ is not computed |
| C.18 | An explicit automorphism-group comparison for the remaining fixed-point-free genus-three type | The quotient is N4. Automorphisms of its completed group preserving the orientation cover and the stated congruence action, modulo inner automorphisms, identify with C_(Q±)(τ)/〈τ〉 and then C_Q(τ). The unique positive discrete lift identifies Mod(N4) with the discrete centralizer; density of its image in the displayed profinite group is unresolved |
| C.19 | The finite-index hyperelliptic route for N4 is refuted | An explicit connected orientation double of a two-pants decomposition gives three independent signed double twists. Any positive finite-order class centralizing a finite-index lifted subgroup fixes the six curves and four pants, hence lies in the torsion-free twist kernel and is identity |

For C.17 the five nonempty-real types are nondividing with 1, 2 or 3 ovals, and dividing with 2 or 4 ovals. Cutting along the ovals gives respectively the verified genus-at-most-two components: S_(2,2), S_(1,4), S_(0,6), two S_(1,2), or two S_(0,4). The proof uses the faithful procongruence Birman pullback, the entire multicurve stabilizer and its injected full twist group, low-genus congruence theorems and goodness of those cut stabilizers. No goodness assertion for the whole genus-three mapping class group is inserted.

The smallest unresolved unmarked ambient case remains **genus three**. Three precise tasks remain:

1. Determine whether every negative involution in the ambient congruence image is conjugate to one of the six actual real types, and evaluate the C_Q-orbit set in H¹(C2,K) over each such type. The actual-type injectivity proved in C.13–C.14 does not evaluate these fibres.
2. Compute K^τ for the five actual types with real points. C.17 computes their congruence centralizers and supplies an exact semidirect product, but the full profinite centralizer cannot be declared equal to the discrete closure until this fixed kernel is evaluated.
3. In the fixed-point-free type, establish or refute the density equality for Mod(N4) in C.18's explicit automorphism group, and then determine the corresponding full-completion kernel and cohomology fibres. C.16 still computes the hyperelliptic intersection in this type.

All higher-genus ambient surjectivity and full-centralizer questions requested in C(d) also remain incomplete. The verified genus≤2 theorems and the inspected real étale-homotopy results are used with their actual comparison targets; no orientation-preserving theorem is substituted for the required orientation-reversing full-completion statement.

## Completion check

There is at least one numbered result for each B(a)–B(g) and C(a)–C(d) task. This satisfies the coverage format, not the prompt's demand that every mathematical question be solved. The unresolved entries above, B.27, F.24 and C.12/C.15/C.18 remain explicit failures to complete those requests. Actual new code and its output are under code/B; it certifies finite examples and the separate exact E.13–E.14 density calculation, not the unresolved infinite section or moduli problems.
