# Context evidence ledger: canonical metrics, involutions, doubles

Prepared by the technical/context support agent after the transcription freeze, from the frozen page TEX and the supplied context TEX/Markdown only. No scan image was inspected and no transcription was altered. This is a source-comparison ledger, not an independent proof audit. Root owns mathematical calculations and final CHECK_EVENTS. Initial consolidation: 2026-11-18 01:01 UTC; targeted LM additions follow below.

## Sources and status scope

The manuscript references below mean `pages/MPL_67_002-052_67_scanNNN.tex`. All context paths are relative to `/workspace/scratch/445fa806e7fe/context/`. The page numbers in Hua's relevant section are one below the scan numbers here, as established by the matched text; manuscript foliation is separately stated. Hua's modernised reading is an attributed contextual interpretation, as required by `hua_project/README.md`, and supplies no authority to alter the frozen transcription.

Read for this ledger: `README.md`, `hua_project/README.md`, `notes/RESULTS_STATE.md`; frozen scans024–046; `hua_project/67.modern.tex` sections IV and XII and the leaf-order paragraph; LM §33 scans440–448, §34 scans463–466, §37 scans533–543 in `LM_140-2_text.tex`; LM §42 scans084–085 in `LM_140-3_text.tex`; LM §51 opening scan033 and §53 scans225–230,277–278 in `LM_140-4_text.tex`. Searches across the attached LM and MPL notes are recorded per item below. Results-register entries are cited at their actual supplied status. The verified supplement below supersedes the initially pending leads.

| Register ID | Supplied status and exact task scope | Permitted use here |
|---|---|---|
| `LM4_SUCCESSOR E.10` | Open, the return's claim. Six congruence-kernel computations: determine `K_c^tau` and nonabelian `H^1(C_2,K_c)` for `Ad(tau)`; five oval types enter the quotient-centralizer term. `notes/RESULTS_STATE.md`, row sourced to `LM4_SUCCESSOR_results.csv`, E.1. | Context for involution/cohomology questions. The manuscript's compact automorphism groups, metric choices and circle quotients do not by themselves compute these displayed kernel groups or pointed sets. No completion claim is made here. |
| `LM6 C.12` | Open, the return's claim. Classification and complete centralizers of all involutions above complex conjugation in the full profinite extended mapping class group, unfinished for genus at least 3; smallest uncompleted case `(3,0)`. Source locator: LM §33, folios222v–226v, `LM_140-2_text.tex`, scans440–448; return `LM6_POINTS_AS_SECTIONS_results.csv`. | Geometric models in scans034–044 can be compared through their explicit involutions and quotients. The row's profinite classification and centralizer demand remains recorded as open. |
| `LM4 C.12` | Open, the return's claim. Requested infinite-operator-group zero-level example; hyperbolic surface and kernel `pi_1(C_{A^0}(u(Gamma)),1)`. Source: LM §23, folios140–141, scans279–281; `LM4_FINITE_GROUP_ACTIONS_results.csv`. | Mention only when the actual centralizer/identity-component map is under discussion. A shared occurrence of “canonical metric” or “normalizer” does not identify this kernel. |
| `LM4 F.7` | Open, the return's claim. Nonsolvable centralizer comparison; a geometric `A_5` in the completion of a genus-zero oriented mapping class group. Source: LM §30, folios194–196, scans383–387; same return CSV. | Finite sphere automorphism actions provide geometric input via their specified actions. This ledger supplies no completion-centralizer equality. |
| `LM4_SUCCESSOR B.39` | Open, the return's claim; nonsolvable centralizer-comparison direction. | Same limited contextual use as F.7; no status promotion. |

The named full return CSVs are absent from the supplied context; only their register summaries were available. No reviewer verdict was attached to the rows above. Rank4 returns are expressly described by the context README as not yet included.

## M01. Leaf order and source units — scans024,027–046

**Manuscript.** Scan024 is the title “Métriques canoniques / sur surfaces conformes”. Scan027 starts manuscript page1; scan044 is page18. Scans045 and046 bear uncertain primed page-number readings. Scan046 ends with the multiplicative constant and scan029 starts with the area-one condition.

**Searches.** `ordre des feuillets`, `métriques canoniques`, `Corollaire 3`, `La constante multiplicative` in `hua_project/67.modern.tex`; title and page markers in the frozen pages.

**Exact comparison.** Hua, introduction, lines286–299, paragraph “L'ordre des feuillets sur les métriques canoniques”, explicitly reads the intercalary leaves and orders his pages26,44,27,45,28…43. These correspond to scans027,045,028,046,029…044 here. Hua quotes the seam “La constante multiplicative” / “déterminée par la condition que l'aire totale de X soit =1”.

**Relationship.** Restates and adds an editorial reading order; the frozen deliverable retains scan order. No result-register claim is needed for this ordering observation.

## M02. Hyperbolicity statements and doubtful coefficient — scans027,045

**Manuscript.** Scan027 (ms1), theorem and Corollaries1–2, lists the exceptional surfaces and the finite-type inequality `\unsure{2|3}g+nu >=3`; the literal doubts remain. Scan045 (primed-page reading), Corollary3, writes the complement as `X\setminus X'` for an inclusion `X\subset X'`.

**Searches.** `Surfaces hyperboliques`, `2g`, `Corollaire 3`, `X'`, `X\setminus` in Hua IV and the frozen leaves; `hyperbolique`, `revêtement universel` in LM notes.

**Exact comparison.** Hua IV, subsection “Surfaces hyperboliques (pages26 et44)”, lines830–878: theorem at836–849; boundary/interior corollary and Hua's added argument at855–862; Corollary3 at864–870. Footnote869 expressly reports the manuscript's `X\setminus X'` and substitutes `X'\setminus X`. Hua prints coefficient2 in the finite-type expression.

**Relationship.** Restates the theorem after choosing the coefficient; differs by an explicit set-complement correction and adds an argument to the boundary-interior assertion. These choices are reading/commentary questions; this ledger makes no new theorem claim and leaves the frozen formula unchanged. No register status settles either diplomatic reading.

## M03. Nonorientable coverings and metric descent — scans028–031,046

**Manuscript.** Scan028 (ms2), opening, calls `P^1` and `C^*` “rev. universels hol.” of `RP^2` and its one-point deletion. Scan031 (ms5) associates the fixed-point-free antipodal involution with a spherical metric and normalizes the orientation double to area1 before descent. Scan046 and the seam into029 give the genus-one flat metric and area condition.

**Searches.** `universels`, `orientation`, `antipodisme`, `Klein`, `aire totale`, `E_a` in Hua IV; `antipod`, `orient` in LM/MPL notes.

**Exact comparison.** Hua IV, “Les surfaces non hyperboliques, et leurs métriques (pages27,45,28 à30)”, lines880–947. The footnote at889–894 calls the displayed maps orientation coverings and gives `C` as the universal covering of punctured `RP^2`, through the Möbius-band model. Lines896–900 compare the real elliptic model, with a separate reading comment on `E_a` versus the fuller page100 notation. Lines906–916 discuss metric normalization/descent; lines941–946 discuss `RP^2` and its orientation double.

**Relationship.** Hua differs from the literal word “universels” and supplies covering clarification. The concrete maps requiring comparison are `C -> C^*` through the exponential, followed by the fixed-point-free involution quotient, and `P^1 -> RP^2`. The notes should identify those maps rather than erase the manuscript wording. Later Hua page100 belongs to a continuation outside the frozen pages here.

## M04. Cylinder and affine metric normalization — scans029–031

**Manuscript.** Scan030 (ms4), first line, deletes `2pi` and inserts1 for the unit-circle length; margin uses `exp(2i pi z)` and the canonical Hermitian metric. Scan029 lists the cylinder automorphisms `z -> az` or `a/z`; scans030–031 give the affine metric class modulo positive scalar.

**Searches.** `2i`, `cercle unité`, `4\pi`, `affine`, `translation` in Hua IV and the frozen pages.

**Exact comparison.** Hua IV, lines917–926, prints the cylinder metric `|dz|^2/(4pi^2|z|^2)` and the unit-circle length1 normalization via `w -> exp(2pi i w)`. Lines927–940 discuss the affine metric class and note some reading choices.

**Relationship.** Restates the normalization and adds an explicit coordinate metric. Root can audit that coordinate formula against the displayed exponential; this support ledger does not record it as an independently performed calculation. No register entry is needed.

## M05. Compact group, Hermitian cone and normalizer — scan032

**Manuscript.** Scan032 (ms6): `X=P(V)`, complex dimension2; compact lift of `H^+` in `SL(V)`; invariant positive Hermitian form; a unique positive ray gives a normalized metric invariant under `Norm_G(H^+)`, hence under `H`.

**Searches.** `hermit`, `Norm`, `normalisateur`, `Schur`, `H^3`, `PSL` in Hua and the attached LM/MPL notes.

**Exact comparison.** Hua IV, “La sphère munie d'un groupe compact (pages30 à36)”, lines952–961, restates averaging and normalizer invariance. Lines1038–1050 explicitly add the linear-algebra/geometric translation: positive Hermitian forms modulo positive scalar, identified with `PSL_2(C)/PSU_2`, and the induced automorphism action. Hua marks this addition “elle est la nôtre”.

**Relationship.** Restates the manuscript construction; Hua adds a model for the action. Credit the added model to Hua. The normalizer-to-metric action is the concrete map available here. Neither `LM4 C.12`'s displayed fundamental-group kernel nor `LM4 F.7`'s completion centralizer is computed by this comparison.

## M06. Explicit self-flag on the two-pole assertion — scan033

**Manuscript.** Scan033 (ms7) opens “On vérifie aisément” and relates a non-ray cone of invariant positive Hermitian forms to two fixed points and a compact maximal torus. The margin reads **“à vérifier”**. For `H^+ !=1`, the leaf identifies the invariant metrics with torus-invariant metrics and parametrizes them by torus orbits away from the two poles.

**Searches.** `à vérifier`, `demi-droite`, `deux points`, `Schur`, `tore` in Hua IV; `pôles`, `équateur`, `antipod` in attached notes.

**Exact comparison.** Hua IV lines963–974: same cone/two-pole assertion and torus-orbit parameterization; footnote967–970 retains the flag and supplies a Schur-lemma interpretation.

**Relationship.** Restates the unverified source assertion and adds an interpretation. The author's flag must remain visible in the final notes even when a modern comparison is supplied. No register row supplies a proof of the full metric assertion.

## M07. Normalizer action and the author's reversal — scans034–036

**Manuscript.** Scan034 (ms8) assigns the action on the torus for antiholomorphic maps fixing/exchanging the poles, then annotates **“C'est l'inverse!”**. The leaf gives the two `H^2(C_2,T)` cases. Scans035–036 write the coordinate families `a\bar z` and `b/\bar z`, their squares and fixed-locus conditions.

**Searches.** `C'est l'inverse`, `central`, `H^2`, `bar z`, `normalisent`, `commutent`, `antipodisme` in Hua IV and the frozen leaves.

**Exact comparison.** Hua IV lines985–994 follows the marginal reversal and writes the conjugation computations. Lines996–1020 expand the central and noncentral cases. The source formulas, rather than a terminology-only contrast, give the maps on which a mathematical comparison can be based.

**Relationship.** Restates the author's correction and adds coordinate explanation. `LM4_SUCCESSOR E.10` is relevant as an open involution/cohomology programme, with its specified `K_c` action and pointed set; this `T` calculation is not asserted to determine that `K_c` calculation. `LM6 C.12` remains open in its stated profinite scope.

## M08. A precise Hua/frozen reading discrepancy — scan035

**Manuscript.** Scan035 (ms9), line containing the two antiholomorphic families, reads “ce sont les `\unsure{seconds|seuls}` qui **commutent** à T”.

**Searches.** `normalisent`, `centralisent`, `commutent` in Hua IV and frozen scan035.

**Exact comparison.** Hua IV, footnote at line1002, says “La page dit ‘normalisent’” and replaces that reading by centralization in the central case. The frozen reading already has “commutent”.

**Relationship.** Differs at the word level. Record both source readings as a question; do not silently import Hua's claimed source word into the frozen transcript. The surrounding explicit formulas allow root to discuss the mathematical action separately.

## M09. Proposition, two author flags, and scope of invariance — scan037

**Manuscript.** Scan037 (ms11) begins **“En résumé et sauf erreur”**. Part(a) states existence of a normalized compatible spherical metric; the frozen line does not expressly repeat `H`-invariance. Part(b) reads uniqueness iff `X^H` is empty. The margin reads **`à \unsure{rectifier|vérifier}`** and asks for a linear-algebra translation of an automorphism's action on a spherical metric.

**Searches.** `sauf erreur`, `rectifier`, `vérifier`, `unique`, `invariante`, `algèbre linéaire` in Hua IV and scans037–039.

**Exact comparison.** Hua IV lines1023–1035 restates the proposition; line1027 makes `H`-invariance explicit in(a). Lines1038–1050 give Hua's own positive-Hermitian-form/hyperbolic-space translation, explicitly attributed to his modern reading.

**Relationship.** Restates after making the intended invariance explicit; adds the requested linearization. Both manuscript qualifications remain material. This ledger does not resolve or strengthen the uniqueness assertion.

## M10. Repetition of the uniqueness criterion — scans038–039

**Manuscript.** Scan038 (ms12) repeats existence for relatively compact `H` and uniqueness iff `X^H` is empty. Scan039 (ms13) again invokes the no-common-fixed-point condition in the spherical case and gives a marginal description of the distinguished metric orbit.

**Searches.** `X^H`, `unique`, `relativement compact`, `R(X)`, `distinguées` in Hua IV and frozen pages.

**Exact comparison.** Hua IV, “Récapitulation (pages37 et38)”, lines1052–1083; criterion at1065–1068, metric-orbit summary at1071–1081. The sphere metric space is described as three-dimensional. Hua's earlier model at1038–1050 is its explicitly added translation.

**Relationship.** Restates repeated manuscript claims. Repetition does not remove scan033's verification flag or scan037's qualified formulation. Root is responsible for any proof/counterexample calculation, and such a calculation needs its own genuine check record.

## M11. Cartographic marginal/application text — scan039

**Manuscript.** Scan039 (ms13), line4: “X est associé à une **carte**, et H est le groupe des autom. de cette carte, qui est fini”; it then says no point fixed by all of `H` means no **facette** fixed by `H`.

**Searches.** `carte`, `facette`, `conique`, `lacunaire`, `S_3` in Hua IV and LM §37; `A_5`, `centralizer`, `nonsolvable` in the results register.

**Exact comparison.** Hua IV lines1081–1083 reads “conique” and calls the note “trop lacunaire pour être restitué”. The frozen leaf supplies the cartographic words and the finite automorphism group statement. LM §37, `LM_140-2_text.tex`, scan535 (folio273), lines15493–15505, explicitly gives the `S_3` action on `P^1\setminus{0,1,infinity}`, its quotient and ramification signature. Its actual finite-group action provides a concrete comparison point.

**Relationship.** Adds recovered text relative to Hua's reading and differs from “conique”. The map available from the manuscript is the stated finite cartographic automorphism action `H -> Aut_conf(X)`. LM's `S_3` action is explicit geometric material. `LM4 F.7` and `LM4_SUCCESSOR B.39` retain their open completion-centralizer tasks; no claim identifying the unspecified `H` with their `A_5` is made.

## M12. Orientation double, quotient and LM §37 functor — scans040–041

**Manuscript.** Scan040 (ms14) writes the two assignments `X -> (X^or,sigma)` and `(X',sigma) -> X'/sigma`; the context is conformal surfaces with boundary and boundaryless holomorphic surfaces with anti-involution. It gives `chi(X^or)=2chi(X)` in the compact case and warns against confusing this hyperbolicity with that of the interior. Scan041 (ms15) descends the distinguished metric and makes the boundary geodesic.

**Searches.** `double`, `bord`, `involution`, `Rev`, `ramification`, `orientation locale`, `produit fibré`, `Legendre` in Hua IV and LM §37.

**Exact comparison.** Hua IV “Surfaces à bord (pages39 à43)”, lines1085–1151: double/quotient maps at1091–1093; modern Klein/Schottky terminology and a qualification concerning boundary-preserving morphisms at1095–1101; Euler characteristic and the closed-disc/interior example at1104–1110; descended metric at1112–1122. Hua cites Alling–Greenleaf, which is not supplied here.

LM §37, `LM_140-2_text.tex`:

- **scan533, folio272**, lines15420–15436: the proposition assumes a properly discontinuous discrete action and faithful point stabilizers that **preserve local orientation**; cyclic stabilizers determine the ramification function.
- **scan534**, lines15469–15474, formula(1): `X' -> Y'=X'/G` defines `Rev(X,G) -> Rev_d(Y)`. The stated quasi-inverse is normalized pullback `X x_Y Y'`.
- **scan535, folio273**, lines15483–15489, formula(3): `1 -> Pi_1(X,x) -> Pi_1((Y,d),y) -> G ->1`.
- **scan535**, lines15493–15505: `X=P^1\setminus{0,1,infinity}`, `G=S_3`; the quotient and the signature `2{1}+3{infinity}` are written explicitly.
- **scans536–537, folio274 on537**, lines15520–15560: based-path choices, the `Pi_{0,3}`/`Pi'_{0,3}` sequence and its arithmetic diagram.

**Relationship.** Hua restates and adds modern categorical terminology and a morphism qualification. LM provides a precise quotient/pullback functor with a written local-orientation hypothesis. The manuscript's anti-involution quotient and LM's ramified-cover functor must be compared through those actual maps and stabilizer actions; this ledger does not erase either source's hypotheses. `LM6 C.12` and `LM4_SUCCESSOR E.10` are relevant to the involution/oval direction only with their open profinite/congruence-kernel scope retained.

## M13. Half-plane and centralizer domain — scans042–043

**Manuscript.** Scan042 (ms16) studies `z -> a\bar z+b`, reduces by a fixed point to `a\bar z`, and identifies a real fixed line. Scan043 (ms17) identifies its quotient with the closed half-plane and describes the real affine group through the complex affine automorphisms commuting with conjugation.

**Searches.** `demi-plan`, `affine`, `commut`, `centralisateur`, `modulo celle-ci` in Hua IV and the frozen leaves.

**Exact comparison.** Hua IV lines1129–1139: affine anti-involution and half-plane; lines1135–1136 add “modulo celle-ci” in a formulation using the full conformal centralizer.

**Relationship.** Restates the model while changing the displayed group domain/quotient wording. A useful final note should specify the map induced on `C/<conj>` and whether the domain is holomorphic affine maps or the full conformal centralizer. This ledger records the reading and the exact comparison; root owns any kernel/isomorphism calculation. `LM4 C.12` names another explicitly displayed centralizer kernel in its register row; no equality between the two kernels has been established here.

## M14. Disc choice and exceptional metric orbits — scan044

**Manuscript.** Scan044 (ms18) takes `P^1` modulo an inversion, obtains the disc, and uses an interior point to choose the distinguished metric. It lists the four exceptional surfaces: plane and closed half-plane with a metric ray; sphere and disc with metric-orbit dimensions3 and2.

**Searches.** `disque`, `point intérieur`, `dimension`, `exception`, `demi-plan` in Hua IV and frozen scans040,044.

**Exact comparison.** Hua IV lines1140–1151 restates the disc/interior-point construction and the four exceptions. The earlier closed-disc versus open-interior comparison at1104–1110 supplies the concrete model for scan040's warning.

**Relationship.** Restates and clarifies the dependence on the double and its anti-involution. No abstract disjointness claim between “hyperbolic” uses is needed: the compared objects are the written double and the written interior of this example.

## M15. Loose lattice/cohomology leaf — scan026

**Manuscript.** The isolated leaf displays `0 -> \unsure{Pi|pi} -> V -> E ->0`, then `H^1(\unsure{<sigma>|sigma},E) ->~ \unsure{H^2|H^1}(sigma,\unsure{Pi|pi}) ~= \unsure{Pi|pi}^sigma/(1+sigma)(\unsure{Pi|pi})`, and the exponential `z -> exp(2i pi z)`. All alternatives remain frozen.

**Searches.** `cohomologie`, `H^1`, `H^2`, `réseaux`, `1+`, `sigma`, `elliptiques réelles` in Hua IV and XII; `K_c`, `H^1(C_2`, `E.10` in the results register.

**Exact comparison.** Hua IV lines825–828 identifies this isolated page25 as a lattice/cohomology calculation, writes the `H^2` interpretation, and explicitly refers the reader to his section XII, “Les courbes elliptiques réelles”. The arithmetic support agent covers scans048–051 and confirmed that scan026 remains within this ledger's remit. The precise XII comparison is M22 below.

**Relationship.** Hua chooses a degree and notation and proposes a later contextual placement. Those choices remain attributed. `LM4_SUCCESSOR E.10` involves a named nonabelian pointed set for a congruence kernel; scan026 displays a lattice/elliptic exact sequence. The exact comparison requires an action and a map relating those displayed coefficients; no such map is claimed by this ledger.

## Search coverage and missing references

Broad context terms actually used include `métrique`, `hermit`, `normalis`, `centralis`, `antipod`, `inversion`, `pôles`, `équateur`, `orientation`, `bord`, `double`, `conjugaison`, `unique`, `Legendre`, and the exact register IDs above. The broad search output led to the targeted Hua IV and LM §37 readings recorded here. Some broad output was capped, so it is not an exhaustive negative-result search.

Targeted readings completed after the first consolidation: LM §33 scans440–448; LM §34 scans463–466; `MPL_146_001-099_notes.md` R057; `MPL_142_001-093_notes.md` N044.1–N044.2 and the cited LM_140-3 scans084–085; LM §51 opening and §53 passages. The supplementary entries below give the actual maps and locators. The earlier MPL146 scan016 search hit was not needed as an additional source after R057 and its primary LM passage were read.

Missing/unconsulted sources: the full result-return CSVs named above; rank4 returns expressly absent from the context; `MPL_152+120 Q1-07` and its source/search ledger cited by the results register; planning source documents not included in the attachment; the Alling–Greenleaf book cited by Hua. No external source was silently substituted for any of these.

## Verified supplement and final-note crosswalk

### M16. The five equivalent-data formulations — scan025; draft N25

**Searches.** `Données équivalentes`, `antipodisme`, `inversion`, `torique`, `orbite`, `pôles` in Hua IV; `tau z`, `équateur`, `mu_n` in LM §34.

**Exact sources.** Frozen scan025 lists a compatible antipodism/inversion pair; a spherical metric and great circle; a circle with a compatible toric structure; a compact torus and an orbit outside its fixed set; and a pole pair with an orbit of the torus fixing it. Hua IV, “Données équivalentes sur une sphère conforme”, lines803–828, restates the list at810–819 and adds the coordinate discussion at821–824: poles0 and infinity, equator `|z|=r`, and rotation group `z -> tz`, `|t|=1`. LM §34's explicit model is M18 below.

**Relationship.** Restates and adds coordinate realization. The literal toric/realification words and the deleted/replaced fixed-point wording remain as frozen. `LM4_SUCCESSOR E.10` supplies an open involution programme; the displayed sphere data supply concrete geometric representatives, with no asserted evaluation of its congruence-kernel groups.

### M17. LM §33: fixed locus, splitting classes, and centralizer maps — drafts N26,N40,N45,N62

**Searches.** `antiinvolution`, `Sc`, `pi_0`, `Centr`, `scindage`, `bord`, plus the register's exact scans440–448 locator.

**Primary source.** `LM_140-2_text.tex`, §33, scans440–448, folios222v–226v:

| Exact locator | Short source passage or displayed map | Use in the comparison |
|---|---|---|
| scan440, folio222v, lines12894–12900 | “Nous montrerons (on l'espère!)”; “On admettra le Lemme”; universal-cover extension of `Z/2` by `pi` | Preserve these source qualifications. The involution lift construction is explicitly introduced. |
| scan441, folio223, formulas(5)–(6), lines12914–12935 | `U^sigma -> Sc(E,Z/2)` and `pi_0(U^sigma) ~= Sc(E,Z/2)` | The source maps fixed-locus components to conjugacy classes of splittings. This is a concrete route from the real-locus/quotient discussion in cote67 to a group extension. |
| scan442, folio223v, lines12949–12960 | `varphi_i: Z -> pi`, `n -> g_i^n`; image displayed as `pi^{sigma_i}` | The source connects a circle component's loop with the fixed subgroup. |
| scans443–445, folios224–225, formula(14) at445, lines13047–13075 | `T_i=Aut(tilde Z_i/Z_i)` and `varphi_i:T_i ->~ pi_i^{sigma_i}` | An actual homomorphism is provided, not just a shared centralizer term. The source includes a proof discussion; this support agent has read it but has not independently rechecked it. |
| scans446–448, folios225v–226v, formulas(15)–(16) | `u'_i=h u_i h^-1`; the diagram from automorphism centralizers to mapping-class centralizers and its stabilizer explanation | These are the precise discrete/geometric maps underlying the register locator. |

**Relationship.** Adds an explicit fixed-component-to-splitting comparison to the metric/quotient material of cote67. `LM6 C.12` expressly concerns the full profinite extended group and remains open for its stated types. `LM4_SUCCESSOR E.10` expressly asks for `K_c^tau` and `H^1(C_2,K_c)`. The source maps displayed above describe the geometric/discrete input; this ledger supplies no passage computing those profinite fibres. No new proof event should be inferred from this contextual read.

### M18. LM §34: the same coordinate antipodism and equator — drafts N25,N34–N36

**Searches.** `antipod`, `pôles`, `équateur`, `zeta`, `diagonales`, `commute`, `normalise`.

**Primary source.** `LM_140-2_text.tex`, §34:

- **scan463, folio234**, formulas(47)–(48), lines13681–13697: “la sphère de Riemann … par le choix de l'antipodisme”; `tau z=-1/bar z`, poles0 and infinity, equator `|z|=1`, and `u_{zeta,alpha}(z)=zeta z^alpha`.
- **scan464, folio234v**, lines13702–13728: the source adjoins antipodism, gives `z ->1/bar z` as the equatorial reflection, and says that `tau` reverses orientation and must be used with care for transport of structure.
- **scan465, folio235**, formulas(49)–(50), lines13751–13784: antipodal pairs index the handles; the written transport formula is `u tau_{I'} u^-1=tau_{u(I')}`, and the chosen `tau_g` commutes with the dihedral action.
- **scan466, folio235v**, lines13792–13819: the source discusses a choice between extensions of the sphere antipodism, displaying the local tube action `(z,t) ->(z,-t)` and the product involving the twist action.

**Secondary lead checked.** `MPL_146_001-099_notes.md`, **R057**, scans046–047, repeats the two-pole/dihedral comparison and attributes the later handle-gluing data to LM scans463–465. It remains that prior note's comparison; the primary formulas above were separately read here.

**Relationship.** Restates the coordinate antipodism/equator models used in scans034–036, and adds the explicit handle transport action. The formulas give the concrete comparison. `LM4_SUCCESSOR E.10` remains an open congruence-kernel question; no result-status change follows from matching these coordinates.

### M19. LM §42: finite sphere action and fixed great circles — draft N39

**Searches.** `carte`, `facette`, `conique`, `S_3`, `tau`, `grands cercles`, `antipodisme`.

**Primary source.** `LM_140-3_text.tex`, **§42, scans084–085, folio331–331v**, lines3563–3681:

- scan084, formula(1), displays the extension by `Pi_{0,3}` with quotient `S_3 x Z/2`; lines3593–3611 identify the conformal action on `P^1\setminus{0,1,infinity}` and write its six Möbius transformations.
- scan085, formula(5), writes `tau(z)=bar z`; formula(7) writes the three other anti-involutions `bar z/(bar z-1)`, `1/bar z`, `1-bar z`; formula(9) lists their real circles/lines.
- scan085, line3681, describes the reflections in the corresponding great circles and the two poles `-bar j,-j`.

**Secondary lead checked.** `MPL_142_001-093_notes.md`, **N044.1–N044.2**, cites those same LM scans for the marked-triple automorphism group and an orientation-torsor formulation. This ledger uses the explicit primary formulas, not an unreviewed status upgrade of that prior note.

**Relationship.** Restates a concrete finite conformal sphere action and supplies explicit reflection loci for comparison with the compact-group metric material. Cote67 scan039 adds the cartographic `carte/facette` application relative to Hua, whose lines1081–1083 instead read “conique” and call the passage too lacunary to restore. Draft N39's former wording that Hua repeats the map-automorphism application should be replaced by this adds/differs comparison. Root was notified of this exact draft issue.

### M20. LM §37, §51: exact elliptic and quotient locators — drafts N26,N45,N62

**Searches.** `Legendre`, `M_{1,1}`, `M_{0,4}`, `gerbe`, `GL`, `tour de Fermat`, `Pi_0`, `M`, `Aut(E`.

The quotient-covering portion of **LM §37 scans533–537** is documented in M12. Its actual elliptic modular continuation lies at:

- `LM_140-2_text.tex`, **scan538, folio274v**, lines15572–15595: `U_{0,3}=M^!_{0,4}` and `M_{1,1}[2]'`, with `M_{1,1}[2]` described as a `Z/2`-gerbe. The source calls the earlier identification “un peu vaseusement” and discusses level2 automorphisms.
- **scan539, folio275**, formulas(9)–(10), lines15599–15623: the level-`n` marking `(Z/nZ)^2_S -> {}_n E`, its `GL(2,Z/nZ)` action, and the written modular quotient. The margin explicitly insists on `GL`.
- **scans540–541, folios275v–276**, formulas(11)–(14), lines15636–15681: the map to primitive roots of unity and the level-change kernel `K_{nn'}`; the source separately describes the coarse quotients at the small levels.
- **scans542–543, folios276v–277**, formula(15), lines15689–15706: `Aut(E_x) ~= (Gamma_n)_x` and the displayed universal `±id` automorphisms. This is the concrete automorphism-to-stabilizer link for comparison with Hua's real elliptic models.

The requested **LM §51** source starts in `LM_140-4_text.tex`, **scan033, folio664**, lines1448–1520, “Exemple: La ‘tour’ de Fermat”. It writes the quotient of `G_0=GL(2,Z)` by `[Pi_0,Pi_0]`; formula(1) identifies `M=Pi_{0,ab}` with the free module on `(0),(1),(infinity)` modulo the diagonal; formula(2) displays the resulting extension, followed by generators and relations in(3). This is an exact located quotient map. The examined passage does not identify this `Pi_0` or its abelianization with the lattice `Pi` of cote67 scan026. Such an identification is not claimed here.

**Relationship.** LM §37 adds the specified modular markings, quotient maps and automorphism stabilizers; Hua XII supplies the direct real-lattice comparison. LM §51's located opening is planning context and an actual group quotient, without an asserted identification of its coefficient module with scan026's. The applicable involution rows `E.10` and `LM6 C.12` remain open. The register's separate `LM7 E.23` and `LM6 E.21` rows point to **§51.16, scans172–178, folios733v–736v**; those later passages were not independently read for this metrics ledger, and their arithmetic tasks belong to the other research support scope.

### M21. LM §53: circle lifts, orientation action, and the hyperbolic exception list — drafts N27,N30,N62

**Searches.** `demi-droites`, `orientation`, `exp`, `métrique`, `conforme`, `involution`, `centralis`, `homotop`, `contrac`, `2g` in `LM_140-4_text.tex` from the located §53 heading onward.

**Primary locators and maps.**

- **§53.1, scans225–227, folios760–761**, lines10008–10076: the source assigns the tangent-ray circle `S_i` and universal cover `tilde S_i`; a diffeomorphism induces `u_S`; the lift group consists of pairs `(u,tilde u)`. Formula(6) is `1 -> T_0^I -> tilde G -> G ->1`. The scan226 margin says “G opère sur T_0^I via le caractère … d'orientation”. Formula(7) on227 is the map of this extension to the special Teichmüller extension.
- **§53.2, scan228, folio761v**, formulas(8)–(10): determinant-`±1` real linear maps act on the ray circle by `z -> R^+z`. The source transcription's normalized-vector denominator in(10) is printed `|z|`; this ledger does not repair it.
- **scan229, folio762**, formulas(11)–(14), lines10112–10159: `t -> exp(2i pi t)` explicitly models the circle cover; a lift is specified by an argument of `u(1)` using `u(1)/|u(1)|`; the displayed extensions of `GL(2,R)^{±1}` and `SL(2,R)` have kernel`Z`.
- **scan230, folio762v**, formula(15) and Corollary2, lines10175–10223: the inclusion of the unit circle in `SL(2,R)` is the source's homotopy comparison; orientation reversal acts on the written central generator by inversion.
- **scan277, folio786**, formulas(137)–(140), lines12172–12194: `A=Aut_top(X,S)`, the exact type list `(0,0),(0,1),(0,2),(1,0)`, and `2g-2+nu>0`, equivalently `2g+nu>=3`. The source states contractibility of `A^0` in that range and gives the special Teichmüller extension of `A/A^0`.
- **scan278, folio786v**, formula(141), lines12206–12230: the action map `G -> A` and the induced map `pi_0(G) -> pi_0(A)` form the displayed square; the lift extension is described as pullback along `G -> T`.

**Relationship.** The actual circle cover restates the exponential convention of cote67 scan030; the orientation-character action gives another explicit sign convention. The numerical list restates the exception list of scan027 with coefficient2 in the context source. The displayed `G -> A -> pi_0(A)` map is available for operator-group comparisons. `LM4 C.12` asks for `pi_1(C_{A^0}(u(Gamma)),1)`; no result about that centralizer's fundamental group is inferred here from the cited source statement about `A^0`. Root's explicit proof checks, when present, remain separately recorded.

### M22. Hua XII: the exact connecting formula and real elliptic models — drafts N26,N45

**Searches.** `Courbes elliptiques réelles`, `Période, points réels, torseurs`, `H^1`, `H^2`, `1 +`, `Pi`, `E_a`, `Klein`.

**Exact source.** `hua_project/67.modern.tex`, **§XII**, lines1922–2133:

- “Modules munis d'une involution (pages90,91 et99)”, lines1927–1992, supplies the positive/negative eigensublattice model. Its footnote attributes a Lean verification to the external project; this support agent has not run or verified that claim.
- “Deux familles (page92)”, lines1994–2020, specifies `(Pi,sigma,c)` and the quotient `Pi_R/Pi`, then the two lattice families `E_a,E'_a`.
- “Période, points réels, torseurs (pages98 à100)”, **lines2107–2126**, explicitly writes `gamma=Gal(C/R)`, `0 -> Pi -> V -> E(C) ->0`, and at2114–2115 `H^1(R,E)=H^1(gamma,E(C)) ~= H^2(gamma,Pi) ~= Pi^gamma/(1+sigma)Pi`.
- **lines2117–2126** give Hua's claimed two values and the nontrivial torsor notation `E_a^!`, followed by the quotient by complex conjugation and the Klein-bottle identification. At2127–2133 his footnote discusses a reading of “sans bord”.

**Relationship.** Restates the norm quotient of scan026 after selecting the uncertain degree; adds the precise later coefficient/action notation and supplies the contextual meaning of `E_a^!` in scan028. These are Hua's readings of continuation pages outside this packet. The frozen uncertainty is retained, and no continuation scan was inspected. Root may cite the direct sequence and quotient with this exact locator while keeping E.10/LM6 C.12 at their supplied open scope. The full external Hua Lean source and N. Alling's cited *Real elliptic curves* (1981) were not consulted here.

## Draft quote/relationship review sent to root

The draft `records/assemble_research.py` entries N25–N45 and N62 were read as research-note drafts. One concrete relationship correction was sent to root: **N39 must describe the carte/facette text as adds/differs relative to Hua's conique/lacunary reading**, rather than as a repetition by Hua. The self-flags in N33,N35,N38 match the frozen page wording already recorded above. N26's connecting-degree alternative is preserved. N37 should credit Hua's own Hermitian-ray/hyperbolic-space translation at1038–1050, while separately attributing any new explicit formulas and actual calculations to root's genuine check records. No manuscript, combined transcription, doubt index, inventory, audit event or freeze hash was modified in making this ledger.
