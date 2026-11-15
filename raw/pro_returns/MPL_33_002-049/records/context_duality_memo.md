# Research support memo: cohomology, classes and duality

Prepared after the transcription freeze, from the frozen `.tex` files and the three supplied context files only. No scan image was read by this supporting agent, no transcription judgment was made, and no transcription, doubts, inventory, or progress file was changed. This memo proposes research-note items for the primary reader; it is not a replacement for that reader's notes.

## Evidence and status key

- **Later** below means the exact supplied file `same_cote_33/MPL_33_098-146_notes.md` (materialized under `context/`). Its N-numbers and scan references are citations to that first-pass research report, not to images independently seen by this agent.
- **Register** means the exact supplied file `notes/RESULTS_STATE.md`. Every listed `MPL_33_098-146` item is explicitly an **observation / first-pass lead**, not a reviewed result. The modern-source claims made inside Later have not been reverified by this memo.
- **S19** is the draft-to-print/Stacks comparison plan in `README.md`, “What our planning document asks.” It is a plan, not a theorem. The README's early “Only this README” statement is superseded by its dated addenda.
- `records/context_duality_searches.json` records an individual regex search of all three supplied context files for each proposed D-item, including exact matched file, line and text. Broad hits were reviewed for relevance; a shared word alone is not treated as a mathematical parallel.

The primary new contribution here is source-level linkage: the early outline and its unresolved tasks can now be set beside later same-cote reports. Nothing establishes the chronology of composition merely from scan order, and no same-point theorem in the supplied reviewed-results list settles these early assertions.

## Proposed individual notes

### D01 — The three-stage programme has a later continuation

**Primary:** cote 33, scan 002, opening paragraphs. **Kind:** unpursued implication. **Quote:** “la théorie des fonctions L”; “des coefficients l-adiques”.

The opening explicitly separates torsion formalism, an adic extension, and application to L-functions. Later reports the same formal priority on scan 122 (N20/N21), an incomplete inverse-limit passage on 128 (N24), and a proposed compatibility test on 128/132/146 (N40). These pages **add** an earlier-positioned programme statement and **restate** the linkage, without showing that the adic passage was completed or establishing composition dates.

**Context/register:** Later N20/N21 (122), N24 (128), N40 (128,132,146); Register `MPL_33_098-146 N20`, `N21`, `N40`, all first-pass leads; S19. **Search:** D01.

### D02 — Proper and smooth base change are separate inputs

**Primary:** scans 004–006, theorem at foot of 004 and opening/NB of 006. **Kind:** unproved claim. **Quote:** “commute à tt changement de base”; “sans hyp. de propreté si … lisse”.

The text states proper base change for torsion coefficients, then separately allows a smooth change of base with prime-to-residual-characteristic coefficients. Later uses proper base change in the projection proof and one-proper-factor Künneth argument (N12–N14, scans 114–120), so these pages **add** the explicitly separated inputs rather than proving the later canonical comparison maps. The two coefficient/properness regimes should not be merged.

**Context/register:** Later N12 (114), N13 (116), N14 (118,120); Register `MPL_33_098-146 §76` (comparison map; first-pass lead), plus S19. **Search:** D02.

### D03 — The analytic comparison and categorical GAGA margin remain unfinished

**Primary:** scan 006, comparison theorem and GAGA margin. **Kind:** self-flagged / unproved claim; the exact “à rédiger” reading is uncertain in the frozen source. **Quote:** “de type fini”; “équivalence de catégories”.

The displayed cohomological comparison is followed by a relative statement with “propre” cancelled in favour of “de type fini,” and the margin proposes a more complete categorical comparison. The supplied later notes have no corresponding étale/analytic GAGA theorem: their sole direct analytic-topic hit is the distinct operator-algebra reused source N42 on scan 099. Thus this material **adds** an analytic comparison branch to S19, while the intended algebraic-stratification scope of the categorical assertion still needs exact collation.

**Context/register:** Later N42 (099) is **different in subject**, not a proof or contradiction; no same-point register theorem. **Search:** D03.

### D04 — Relative analytic GAGA and a rigid extension are explicit open tasks

**Primary:** scan 008, middle and slanted margin. **Kind:** self-flagged / conjecture (two distinct final notes are appropriate). **Quotes:** “À prouver que ce sont des isomorphismes”; “Devrait aussi se généraliser au contexte rigide-analytique”.

The two displayed relative comparison maps are expressly left to prove, while the rigid-analytic margin makes a further expectation rather than asserting that proof. The neighborhood-limit application below is conditional (“on trouverait alors”), and should stay dependent on the proposed comparison. No same-point analytic or rigid comparison is supplied by Later or the Register; this **adds** a substantive open branch, while Later N24's inverse-limit problem on 128 concerns traces and is only an analogy.

**Context/register:** Later N24 (128), **different object/problem**; Later N42 (099), unrelated analytic reused source; S19, no same-point result. **Search:** D04.

### D05 — Smooth proper specialization supplies a later example, not a general criterion

**Primary:** scan 010, opening; compare scan 048, middle. **Kind:** unpursued implication. **Quotes:** “propre et lisse”; “sont loc. libres”; “p.ex. f propre lisse!”.

The specialization theorem supplies an internal reason for the parenthetical example used in the duality application on 048. Later N19 (112/120) also isolates locally constant-cohomology hypotheses for an ordinary-direct-image comparison, but concerns projection rather than this specialization theorem. The early pages **add** a concrete source of such coefficients; they do not identify local constancy with finite Tor dimension or prove all of the later variant.

**Context/register:** Later N19 (112,120), with N08 (108,112) as coefficient warning; Register `MPL_33_098-146 N08`, first-pass lead; S19. **Search:** D05.

### D06 — Absolute dimension bounds and relative bounds have different scopes

**Primary:** scan 010, dimension section. **Kind:** unproved claim. **Quote:** “il y a un abaissement dans le cas affine”.

The page gives absolute cohomology bounds over a separably closed field and warns against reading the affine bound as a general topological-dimension rule. Later N09 (110) concerns finite **relative** dimension of ordinary direct image, while N32 (140/142) concerns a compact-support amplitude estimate. These pages **add** the absolute starting point and **differ in scope** from both later statements; neither later report can decide the frozen strict/non-strict inequality doubt on 010.

**Context/register:** Later N09 (110), N32 (140,142); Register `MPL_33_098-146 N30` and `§76`, first-pass leads; S19. **Search:** D06.

### D07 — Supported sections lead toward the later closed-immersion duality calculation

**Primary:** scan 012, supports and local Ext displays. **Kind:** unpursued implication. **Quote:** “Foncteurs dérivés”.

The identification of supported sheaves and the supported-Ext expressions isolate the closed-complement mechanism before the purity statement. Later N01 (098) reports a closed-immersion calculation within the claim that D “échange” the operations. The early page **adds** the elementary support-functor setup for that later programme, but the support identifications alone do not prove the full exchange identities.

**Context/register:** Later N01 (098); Register `MPL_33_098-146 N01`, first-pass lead; S19. **Search:** D07.

### D08 — Twists are not chosen constant coefficients

**Primary:** scan 014, Kummer and twist paragraph. **Kind:** unpursued implication. **Quote:** “Il n'faut surtout pas les confondre”.

The page makes dependence on a primitive-root choice explicit before introducing the orientation twists used in 032–036. Later's tensor/duality discussion (N29, 134/136) provides a structural comparison, but contains no same-point Kummer trivialization calculation. This **adds** a concrete descent/trivialization issue that should be retained when comparing the degreewise trace with later abstract contraction.

**Context/register:** Later N29 (134,136); Register `MPL_33_098-146 N29`, first-pass lead; no exact Kummer entry. **Search:** D08.

### D09 — Absolute purity is marked as a problem with qualifications

**Primary:** scan 014, boxed problem and following lines; scan 026, listed purity settings. **Kind:** self-flagged / unproved claim. **Quotes:** “Pb Pureté ‘absolue’”; “pour bons premiers”; “Extension aux div. à croisements normaux”.

The source explicitly places absolute purity under a problem heading and attaches resolution/equal-characteristic/good-prime qualifications; the small smoothness-versus-regularity wording remains uncertain. Later N20 (122) proposes a curve route “sans résolution des singularités,” which **differs in object and scope** rather than contradicting the purity discussion. The early pages **add** the precise purity dependency and the normal-crossing extension request, neither of which is settled by the supplied register.

**Context/register:** Later N20 (122); Register `MPL_33_098-146 N20`, first-pass lead; S19. **Search:** D09.

### D10 — Proper constructibility and finite cohomology are inputs, not perfectness

**Primary:** scan 016, theorem and corollary. **Kind:** unproved claim. **Quote:** “les R^i f_*(F) … sont constr.”

Proper direct-image constructibility and finite cohomology over a separably closed field are stated without a proof here. Later N30 (136/140/142) treats pseudo-coherence as known but still asks for finite Tor dimension, so the early theorem **adds** a finiteness input without supplying the separate Tor bound. Register N25 already records a perfect-complex/nonprojective-cohomology test, and it should be cited as an existing lead instead of rediscovered as a new example.

**Context/register:** Later N25 (126–132), N30 (136,140,142); Register `MPL_33_098-146 N25`, `N30`, first-pass leads. **Search:** D10.

### D11 — The nonproper constructibility generalization has a proposed reduction

**Primary:** scans 016–018, final “Question” and opening continuation. **Kind:** self-flagged / unproved claim. **Quote:** “à des f de type fini au lieu de f propre”; “Se ramène au cas d'une imm. ouverte”.

The passage proposes reduction to an open immersion and invokes resolution plus purity, with difficult inserted qualifications preserved in the frozen transcription. Later N15 (118) proposes local duality for nonproper Künneth, and N20 (122) proposes a curve immersion route without resolution. These later leads **add related methods** but do not restate or settle the same constructibility question, so no contradiction or completed proof is established.

**Context/register:** Later N15 (118), N20 (122); Register `MPL_33_098-146 N15`, `N20`, first-pass leads. **Search:** D11.

### D12 — Independence of compactification is asserted before derived coherence

**Primary:** scans 018–020, compactification construction and opening continuation. **Kind:** unproved claim. **Quotes:** “quasi-triviale du th. de changement de base”; “indépendant du choix de la factor.”

The source defines the cohomological functors by extension by zero and proper direct image, and claims independence up to isomorphism from base change. Later N12 (114) expressly leaves functoriality in derived categories to verify for a subsequent comparison map. These pages **add** the earlier object-level construction; a proof of independence up to some isomorphism should not be silently promoted to all canonical coherence compatibilities.

**Context/register:** Later N11 (112), N12 (114); Register `MPL_33_098-146 §65` and `§76`, first-pass leads; S19. **Search:** D12.

### D13 — Identity-map test for the unqualified quasi-finite vanishing

**Primary:** scan 020, degree-zero display and item (v). **Kind:** own idea. **Quote:** “Si f quasi-fini … alors les R^i_! f_*(F)=0”.

Taken literally for i=0, the statement is contradicted by f=id and any nonzero F, because the same page identifies its degree-zero functor with f_!. This is a conditional scope test pointing to a missing or inherited positive-degree restriction, not permission to insert one into the transcription. **Confidence: high for the test, because the identity functor and the same-page degree-zero definition suffice; the intended quantification remains unresolved.**

**Context/register:** Later N01 (098) discusses a degree-zero closed-immersion mechanism but is not this assertion; no same-point result or counterexample in the supplied register. This **adds** an internal scope question to S19. **Search:** D13.

### D14 — Étale trace and covariance precede the general smooth trace

**Primary:** scan 020, trace and covariance displays; scans 032–034. **Kind:** unpursued implication. **Quote:** “Si f étale, on a un hom can.”

The early degree-zero trace suggests a normalization comparison with the later relative-dimension-d trace. Later N29 and N37 (134/136/146) organize trace through contraction and symmetry rather than only through degreewise maps. These pages **add** a concrete special case for a future compatibility check, but the agreement of all three constructions is not proved on these leaves.

**Context/register:** Later N29 (134,136), N37 (146); Register `MPL_33_098-146 N29`, `N37`, first-pass leads. **Search:** D14.

### D15 — The divisor class is built from the Kummer boundary

**Primary:** scans 022–024, canonical beta and boundary construction. **Kind:** unproved claim. **Quote:** “dφ est une section canonique”.

The quotient by units supplies the claimed equation independence for a principal divisor, then the Kummer boundary gives the finite-coefficient class. No same-point fundamental-class construction appears in Later; N47 (123) concerns relative divisors in a different reused source and must not be treated as its continuation. This **adds** a separate local-class construction to S19 and a test case for the later trace formalism.

**Context/register:** Later N47 (123), **different source/problem**; no exact result-register match. **Search:** D15.

### D16 — Higher-codimension choice independence is a real proof obligation

**Primary:** scan 024, cup-product paragraph. **Kind:** unproved claim. **Quote:** “on prouve que cette section ne dépend pas du choix des Y_i”.

The text asserts independence of the local complete-intersection presentation and consequent global gluing, but gives no proof of changes of generators. Later N37 (146) makes the derived symmetry/sign rule explicit, which is a useful **additional comparison** for reordering even-degree classes, not a proof of full independence under arbitrary regular-sequence changes. A reconstruction must separately control units, replacements of generators and gluing.

**Context/register:** Later N37 (146); Register `MPL_33_098-146 N37`, first-pass lead; no same-point independence theorem. **Search:** D16.

### D17 — Coefficient compatibility is the first adic input, not the whole limit argument

**Primary:** scan 026, item (iv) and NB. **Kind:** unpursued implication. **Quotes:** “Compatibilité pour n variable”; “La ‘bonne’ classe”.

The page identifies the desired adic home for the class immediately after finite-coefficient compatibility. Later N24 (128) leaves the adic trace passage as an expectation, and N40 (128/132/146) asks for compatible perfect models. The early page **adds** an analogous finite-level input for cycle classes but concerns a different object, so it does not settle the later limit problem.

**Context/register:** Later N24 (128), N40 (128,132,146); Register `MPL_33_098-146 N40`, first-pass lead, beside N20/N21's adic programme. **Search:** D17.

### D18 — Point-class normalization is promised and partially compared with curves

**Primary:** scans 028–030, Example 1 and Kummer normalization. **Kind:** unproved claim. **Quotes:** “Il va résulter de le théor.”; “une base”; “ne dépend pas du choix de x”.

The independence and basis assertion in dimension d is promised from a theorem to come, while the curve case is described as already checked by the global Kummer normalization t(γ)=1. Later N20 (122) again treats curves as an entry to Lefschetz and L-functions, but that concerns singular coefficients and is not a proof of the present point-class statement. These pages **add** a concrete normalization target for the later trace programme.

**Context/register:** Later N20 (122), N29 (134,136); Register `MPL_33_098-146 N20`, `N29`, first-pass leads. **Search:** D18.

### D19 — The corrected route from local to relative global cohomology

**Primary:** scan 030, Example 2; scan 036, compatibility diagram. **Kind:** unpursued implication. **Quote:** “on a aussi un hom”.

The surviving route passes through supported global cohomology before reaching the relative proper-support sheaf, and 036 asks for compatibility with trace. Later N36 (144/146) also cancels and restarts a local-to-global pairing construction, but with cohomological correspondences and perfect-complex hypotheses. The early diagram **adds** a distinct local-class compatibility problem, not a completed instance of the later pairing theorem.

**Context/register:** Later N36 (144,146), N37 (146); Register `MPL_33_098-146 N36`, `N37`, first-pass leads. **Search:** D19.

### D20 — Locally variable dimension needs a componentwise comparison

**Primary:** scan 032, orientation twist paragraph. **Kind:** unpursued implication. **Quote:** “sur ses divers morceaux”.

The page defines the twist componentwise for locally variable relative dimension, then restricts the trace discussion to pure dimension d. Later N31 (138/140) distinguishes pointwise finite bounds from one uniform interval, so this early flexibility should not be mistaken for a global uniform bound. The pages **add** a useful quantifier distinction for comparing the orientation construction with later Tor-amplitude estimates.

**Context/register:** Later N31 (138,140), N32 (140,142); Register `MPL_33_098-146 N30` and `§76`, first-pass leads; no exact orientation result. **Search:** D20.

### D21 — Connected versus geometrically connected fibres: a conditional test

**Primary:** scan 034, property (v); compare 028's explicit “géom. connexe”. **Kind:** own idea. **Quote:** “fibres conn. non vides”.

If this means ordinary scheme-theoretic connectedness, the finite étale morphism Spec(C)→Spec(R) has connected nonempty fibre and relative dimension zero, but after a geometric base change the direct-image stalk has two copies of A rather than one, so the trace cannot be an isomorphism for nonzero finite A. The contrast with the explicit geometric connectedness on 028 makes the hypothesis worth checking in any later collation. **Confidence: high for the conditional rank/cardinality test; whether the wording already uses geometric fibres by convention remains open.**

**Context/register:** Later N14 (118/120) and N32 (140/142) explicitly track geometric-fibre/field scopes but contain no same-point connected-fibre trace assertion; no result-register status changes. This **adds** a scope question. **Search:** D21.

### D22 — A derived formulation is demanded by the local/global compatibility problem

**Primary:** scan 036, bottom paragraph. **Kind:** unpursued implication. **Quote:** “s'énonce sous forme plus complète”.

The page itself explains why the derived-category section follows: the class/trace compatibility should have a fuller derived formulation. Later N01 (098) organizes the four operations by duality, and N29/N37 (134/136/146) organize trace through contraction and symmetry. The early page **adds** a stated motivation for those later reported structures, without proving that they complete this exact diagram or establishing a drafting chronology.

**Context/register:** Later N01 (098), N29 (134,136), N37 (146), N41 (130–146); Register entries with those exact IDs are all first-pass leads. **Search:** D22.

### D23 — The promised flat resolutions have a reported later development

**Primary:** scan 038, nonflat paragraph. **Kind:** unproved claim, later continuation. **Quote:** “dans la suite de ces notes … des résolutions plates”.

Later N02 (100) reports flat generators and resolutions, N03 (102) records the general-topos question, and N04 (104/106) reports the nonflat extension and composition. They **add a concrete later continuation** of this promise, while N06/N07 (106) still distinguish a corrected injective argument from full local compatibility. No claim that every check was completed follows simply from the promise having a later construction.

**Context/register:** Later N02–N07 (100–106); Register `MPL_33_098-146 §65` and `§76`, first-pass leads. **Search:** D23.

### D24 — Flatness of the topos morphism is distinct from coefficient perfectness

**Primary:** scans 038 and 044. **Kind:** unpursued implication. **Quotes:** “Tor-dim. finie”; “tous les morphismes de topoi annelés envisagés sont plats”.

The exact pullback furnished by constant coefficient sheaves concerns the morphism of ringed topoi, not finite projective dimension of every coefficient module. Later N08/N10 (108/112) already give the finite-ring obstruction, and N25 (126–132) separately shows why a perfect object may have nonprojective cohomology. These pages **add** a place where those distinctions matter; the existing examples should be cited rather than re-presented as new discoveries.

**Context/register:** Later N08/N10 (108,112), N25 (126–132); Register `MPL_33_098-146 N08`, `N25`, first-pass leads. **Search:** D24.

### D25 — External/internal Hom requires separate existence and convergence checks

**Primary:** scan 040, boxed identity and spectral sequences. **Kind:** unproved claim. **Quote:** “lié au précédent par”.

The displayed RΓ/internal-Hom relation and Ext spectral sequences are stated without specifying all boundedness and convergence hypotheses on this sheet. Later N05 (104) records a global finite-cohomological-dimension qualification and a bounded-below second argument for internal Hom, while N34 (144) raises a separate H-zero-versus-whole-complex issue. The early page **adds** the starting formulas; the later notes **qualify related scope**, but do not decide the frozen G/C glyph ambiguity.

**Context/register:** Later N05 (104), N34 (144); Register `MPL_33_098-146 §76`, first-pass lead; S19. **Search:** D25.

### D26 — The unbounded proper-support extension changes its hypothesis

**Primary:** scan 042, Remarque and final sentence. **Kind:** withdrawn in the same text / unproved claim. **Quotes:** cancelled “f est à fibres de dim bornée”; inserted “Y est quasi compact”.

The surviving hypothesis is quasi-compactness of the base, while the justification still invokes finite cohomological dimension for a proper compactification with bounded fibre dimensions. Later N09 (110) concerns the more difficult ordinary nonproper relative functor, and N30/N32 (136/140/142) give a compact-support Tor-bound programme. These pages **add** an explicit hypothesis revision and a proof dependency; the later ordinary-direct-image question is not contradicted by this compact-support claim.

**Context/register:** Later N09 (110), N30 (136,140,142), N32 (140,142); Register `MPL_33_098-146 N30` and `§65`, first-pass leads. **Search:** D26.

### D27 — Proper base change detects an isomorphism after the comparison is built

**Primary:** scan 044, derived comparison and final paragraph. **Kind:** unproved claim. **Quote:** “puisque on sait que les (*_i) le sont”.

The source reduces the isomorphism assertion for the derived comparison to the known cohomology-sheaf maps. Later N12 (114) explicitly separates checking functoriality in derived categories from checking that a comparison is an isomorphism on fibres. These pages **restate the isomorphism-detection strategy** and **add** an earlier construction target, but do not by themselves discharge the later naturality/resolution-independence task.

**Context/register:** Later N12 (114); Register `MPL_33_098-146 §65`, first-pass lead; S19. **Search:** D27.

### D28 — The global-duality cover states a programme, not its proof

**Primary:** scan 046, whole sheet. **Kind:** reading question / source accounting. **Quote:** “énoncé général pour un morphisme lisse compactifiable”.

This title-only sheet states the intended general smooth compactifiable duality theorem but contains neither its statement in formulas nor a proof. Later N17 (120) reports an attribution involving global duality, and N01/N29/N37 report related operational/trace formalism; those are useful **comparisons**, not evidence that the missing general statement appears on 046. This **adds** an actual title sheet to the inventory, whereas Later T01/T02 report no cover or explicit page total in scans 098–146.

**Context/register:** Later N17 (120), N01 (098), T01/T02 (098–146); Register `MPL_33_098-146 N01`, `§1`, `§65`, first-pass leads; README placement. **Search:** D28.

### D29 — Duality is used as a transport of finiteness

**Primary:** scan 048, field and relative examples. **Kind:** unproved claim / unpursued implication. **Quotes:** “On retrouve le th. de finitude de Artin”; replacement “constructibilité”.

The page moves from compact-support cohomology to ordinary cohomology of a dual and then proposes the relative constructibility consequence under local constancy. Later N01's exchange programme (098) **restates the organizing principle**, while N30 (136/140/142) supplies a different finiteness problem needed for complex-theoretic traces. The early page **adds** a concrete intended application, without settling all hypotheses needed for that transport or the later perfectness requirement.

**Context/register:** Later N01 (098), N19 (112,120), N30 (136,140,142); Register `MPL_33_098-146 N01`, `N30`, first-pass leads. **Search:** D29.

### D30 — The ordinary/proper-support distinction survives the corrections

**Primary:** scan 048, two main relative formulas and the intervening parenthesis. **Kind:** reading question. **Quote:** the live parenthesis “les R^{-i}_! f_*(DF)”.

The main right-hand ! marks are deleted, while the intervening parenthetical ! is retained, so the page does not present a uniform notation change. Later N18 (120) and N30 (136/140/142) explicitly distinguish ordinary and proper-support operations and give reasons not to transfer statements between them. This **adds** a substantive reading/scope question; the context cannot authorize changing any one of the frozen support signs.

**Context/register:** Later N18 (120), N30 (136,140,142); Register `MPL_33_098-146 N30`, first-pass lead. **Search:** D30.

### D31 — A partial-range duality consequence should be checked with its direction intact

**Primary:** scan 048, final sentence. **Kind:** unproved claim. **Quote:** “i≤i_0 … j≥2d-i_0”.

The final sentence proposes a one-sided consequence of the degree reversal j=2d−i. Later N32/N33 (140/142) carefully distinguish cohomological from homological indexing in a compact-support amplitude estimate. These pages **add** a different range statement whose direction is consistent with that written reversal, but the later Tor-amplitude proof does not establish its local-constancy or constructibility hypotheses.

**Context/register:** Later N32/N33 (138–142); Register `MPL_33_098-146 N30` and `§76`, first-pass leads. **Search:** D31.

## Standing-question extraction for the primary reader

The principal handwritten self-marked or deferred steps are: scan 006's doubtful “à rédiger” margin; scan 008's explicit “À prouver” and rigid-analytic “Devrait”; scan 012's “Donner définition de la classe fondamentale … locale” (with the reading doubt preserved); scan 014's boxed “Pb Pureté ‘absolue’” and extension line; scans 016–018's “Question de la généralisation” and conditional resolution/purity reduction; scan 024's “on prouve” independence/gluing assertion; scans 028–030's promised point-class theorem and recalled curve verification; scan 036's request for a fuller derived formulation; and scan 038's explicit later flat-resolution promise. The finitude/constructibility claims on 048 are assertions/applications, not authorial doubt markers merely because no proof is supplied there. The revised hypothesis on 042 is a same-page withdrawal with an inserted replacement, and the cancelled paired expressions on 048 are local revisions rather than wholesale retractions of duality.

## Results-register boundaries: avoid false relevance and repeated work

No argument in these even-numbered pages addresses **LM7 E.23** (continuous section classes), **LM4 D.12** (profinite GT torsion), or **LM4 F.7** (nonsolvable centralizer completion); their Open statuses remain unchanged. The appearance of Gal on 002 is not evidence of a solution to those questions. **LM7_PUSH C.6** is marked Proved by its return but concerns class-two arithmetic germs; this memo neither rederives it nor uses it as a purity/duality theorem. **INTAKE LM7_CONTINUED §?** is an intake reading, not a referee verdict, and supplies no matching cohomological statement here.

The explicitly refereed paragraph in RESULTS_STATE lists LM4 D.32/D.34 and several LM7_PUSH D/E rows; it does not upgrade the unrelated C.6 row or the `MPL_33_098-146` observations. **WG H9** concerns a Lefschetz-pencil/Hodge-index/Mordell–Weil question and is different from the fixed-point/trace and purity uses here; **WG2 §2.1 #2** concerns graded Lefschetz operators and is likewise not settled by these pages. `MPL_14_002-044 §107` is only a truncated register lead about correspondences and Lefschetz; its full note and exact scan references are not supplied, so an exact comparison remains unavailable.

Already-present examples that should not be rediscovered as new: Later N10's infinite-Tor module at a point; N25's perfect complex with nonprojective cohomology; N31's nonuniform stalkwise amplitudes; N35's infinite-free-module trace scope test; N38's unbounded contractible representative; and N40's compatible finite-projective-model test. They remain first-pass leads in the supplied context, but the new package should add the present scan linkage rather than duplicate their derivations.
