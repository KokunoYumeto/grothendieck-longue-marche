# Research notes — MPL_136_095-141

## Scope, evidence, and principal finding

These notes concern **cote 136, scans 095–141, excluding the omitted blank scan 122**: 46 supplied faces. The transcription was completed in a single ascending stream, audited against every supplied whole-page image and its halves, reconciled for notation, and frozen at **2026-11-15 16:47:48 UTC**; the context was opened at **16:48:20 UTC**. All interpretation and literature comparison below took place after that freeze. No subsequent reading proposal changes the transcription.

**The pages support an integral, functorial, bigraded divided-power construction, together with a program for extracting ordinary cohomology and comparing products. They do not supply a completed proof of the strongest unqualified ordinary-cochain-algebra claim.** The explicit aspirations, qualifications, and corrections are substantial mathematical evidence, not incidental drafting noise. A close published weighted comparison is available in Cartan’s account of Grothendieck’s lecture; its precise statement and identification limits are recorded in L01, with related multiplicative comparisons in L02–L04. The distinction between a weighted family, its extracted cohomology, and an ordinary integral PD algebra is indispensable (O01–O04).

“Unproved claim” below means **not proved in these surviving sheets**, or dependent on a referenced argument not supplied here. It does not mean that the claim is false, novel, or still open in the literature. “Self-flagged” identifies the author’s own reservation, admission, question mark, or explicit deferral. Researcher-generated arguments and links are labelled **own idea**, with confidence and reasons. The English donor sheet is not assigned to Grothendieck without provenance.

The context contains a preliminary README, a contents list, Chapters VI–VII of *Pursuing Stacks* (PS), a license, and `notes/RESULTS_STATE.md`. It **does not contain** the earlier cote-136 transcription/return, PS Chapter V §94, or the full research documents cited by the register. PS page numbers below are the text’s `\pspage` numbers, **not archive scan numbers**. Context line references are to the supplied files, identified by hashes in the search record.

## 1. Answers to the questions attached to the package

### 1.1 The proposed integral multiplicative cochain model

There are several claims to distinguish.

| Claim under examination | Evidence in cote 136 | Assessment for this package |
|---|---|---|
| A functorial construction on semisimplicial sets | Contravariant structured functors on 111; cosimplicial/dual coalgebra construction on 123–129; named PD chain/cochain functors on 133–135 | **Supported as an explicit construction**, subject to the marked local reading questions and asserted structural compatibilities (N17, N37–N54). |
| Integral coefficients and change of coefficient ring | The polynomial coefficient coalgebra on 131–133; the integral object and tensor formula on 135 | **Explicitly present**; this is not merely a rational analogy (N50, N52). |
| Ordinary integral cohomology of the entire unprocessed complex | Admissibility on 111–113 is expressed through `τ∞`; comparisons on 115 are desired isomorphisms; 117–119 impose eventual weight bounds and flasqueness | **Not established in this extract.** Its undefined earlier extraction and extra coefficient object cannot be suppressed (N18–N29, O02). |
| Cup products with their exact integral normalization | Algebra structures on 113; multiplicative structures on 135; Stokes comparison on 137–141 | **A real aim, with partial construction.** A product comparison must retain weights, coefficient pairings, and its level of coherence (N19, N54, N58, O03–O04, L01–L03). |
| Uniqueness of admissible theories | “On aimerait” on 119; connected/simply connected groupoid, “Conj.?” and fraction-calculus doubts on 121 | **Explicitly conjectural here** (N30–N36, O08). |
| Recovery of integral homotopy types or all mapping spaces | No such completed theorem in these handwritten pages | **A further assertion**, requiring additional structures and hypotheses; modern benchmarks are compared individually in L05–L11. |

The strong reading in which an ordinary integral differential algebra has differential-compatible divided powers on **every positive even cocycle** and recovers the ordinary cup ring fails the elementary `CP²` test in O01. This is not a refutation of the manuscript: its coefficient algebra, restricted operations, bigrading, and extraction may deliberately avoid that hypothesis. Conversely, simply observing the tensor formula on 135 does not prove a cohomology or homotopy comparison.

The positive published comparison in L01 matters just as much as the obstruction. It prevents mistaking the necessary qualifications for a claim that integral weighted de Rham theory is impossible. However, the published object’s coefficient algebra, finite-weight pieces, and comparison maps must be matched to the manuscript’s dual and completed objects; the historical parallel alone does not supply every missing axiom or proof in these sheets.

### 1.2 “Topos de De Rham” and “faisceautisation”

**No separately named “topos de De Rham” or specified associated-sheaf functor is defined in this extract.** What is visible is concrete: scan 113 regards the structured semisimplicial object as a sheaf on the topos `(Ss)`, gives its constant coaugmentation, and draws

\[
R\Gamma(X,S_k)\longrightarrow R\Gamma(X,C_*^{**})
\longleftarrow C^{**}(X)=\Gamma(X,C_*^{**}).
\]

Scans 115–119 ask for suitable isomorphisms after `τ∞`, with resolution and quasi-flasqueness conditions. Thus the extract supports a sheaf-theoretic treatment and a comparison of ordinary with derived sections; it does not justify inventing the objects, covers, or universal property of another site (N20–N28, N67).

The nearest supplied PS discussions are the functor/flat-sheaf topos of §110, p. 443, and the warning about taking sections in §127, pp. 536–538 (`ps6.tex`, lines 34–47, 4730–4783, 4831–4844). They are useful comparisons, not definitions of the requested historical terminology. The exact retrospective advertised in the contents, §94, lies in **missing Chapter V** (`PURSUING_STACKS_CONTENTS.md`, line 120). These negative findings are bounded to the supplied material and do not assert absence from all of cote 136 or all of PS.

### 1.3 “Constructions universelles”

The extract exhibits several actual universal or representability constructions, rather than defining one uniquely named construction:

1. **Free and standard models, 096–106.** A PD/exterior construction from an extension and distinguished element, an evaluation/right-adjoint calculation, and canonical comparison zigzags. The proposed derived equivalences retain the flasqueness condition, and the primed categories admit more morphisms (N01–N11).
2. **Representing coefficient objects, 123–127 and 131–133.** Dual coalgebra/affine-functor presentations, the PD quotient by the simplex relation, a completed dual, and the specific polynomial coefficient coalgebra with coefficient-extraction functional (N37–N43, N50–N51).
3. **Extension from simplices, 127–129.** A chain object assembled by colimits over simplices, dual to the cochain construction, with functoriality and coefficient variation (N44–N48). Its ordinary categorical universal property does not itself prove homotopy invariance (O12).

PS §111, pp. 450–451, supplies a later universal polynomial map into a completed divided-power object; §120, pp. 506–507, discusses universal operations through analyzers (`ps6.tex`, lines 370–404, 3131–3197). These are related constructions, not proof that one phrase in the planning document names precisely one of them. In particular, the uniqueness problems on 106 and 119–121 remain visible.

### 1.4 Reconstructable sequence of the lecture material

This is an **editorial reconstruction from the surviving headings and argument sequence**, not a recovered authorial table of contents or a statement about the missing opening pages.

| Scans | Function in the surviving handwritten sequence | Status and note pointers |
|---|---|---|
| 096, 098, 100, 102, 104, handwritten addition on 105, 106 | Compare categories of special DR algebras with free/standard models; enlarge the morphisms and investigate their localized groups | Conditional flasqueness argument; explicit correction and unfinished group computation, N01–N12 |
| 108 | Determine explicit homomorphisms | Exceptionally faded; formulas cannot support confident independent conclusions, N13 |
| 111, 113, 115, 117, 119, 121 | Formulate generalized theories, extracted cohomology, sheaf/derived comparisons, local criteria, and uniqueness | Several desired implications and conjectures, N17–N36, N67–N68 |
| 123, 125, 127, 129, 131, 133 | Construct dual coefficient data and chain/cochain functors, then specialize to an integral PD model | Explicit construction with asserted compatibility and exactness steps, N37–N51 |
| 135 | Integral base change and general coefficients | Multiplicative structures asserted, N52–N54 |
| Live lower part of 137, then 139 and 141 | Dualize Stokes, identify the algebraic target, calculate normalized simplex coefficients | Draft signs and indexing still under revision, N55–N66; independent checks O05–O07 |

### 1.5 Abelian varieties, Chern classes, and Fourier transforms

**Abelian schemes, Jacobians, and abeloid families do occur among the supplied faces, but in the reused monodromy/analytic-group typescript.** Representative locations are 103 (Jacobians), 107 (abeloïds), 112–116 (abelian schemes, biextensions, Néron–Severi classes and polarizations), and 124 (elliptic curves). The numbering and text identify these sheets with SGA 7 I, Exposé IX, *Modèles de Néron et monodromie* (Grothendieck & Raynaud, 1972); exact version differences remain to be collated (R35), and the source distinction is tracked in R01–R35.

No handwritten statement in these lecture sheets names those objects as examples of the PD construction. **No Chern-class or Fourier-transform example was located in the supplied scans.** Neither term occurs in the supplied PS chapters or contents; the README contains the question, not evidence for the proposed example. The handwritten DR diagram on the donor sheet 105 belongs to the lecture sequence, but it does not convert the surrounding analytic proof into a lecture example.

The English minimal-model sheet 109, headed `N27`, is another donor text, and remains **bibliographically unattributed**. Its rational/real claims and explicit uncertainty about the non-simply-connected case are recorded in N14–N16; they must not be silently presented as Grothendieck’s own lecture assertions.

## 2. Standing question: steps the text itself marks as unverified

This register collects explicit signals, including admitted or deferred steps on reused sheets. A condition imposed as a hypothesis is not automatically a conjecture; the table states its actual role.

| Scan(s) | Brief words or marks on the page | Step or reservation | Notes |
|---|---|---|---|
| 098, carried through 100–104 | “Supposons que ceci implique”; “si on suppose” | Preservation of universal flasqueness under positive divided powers | N04–N05 |
| 099, reused | “Nous admettrons ici la définition” | Analytic exponential construction | R03 |
| 100 | “faux tel quel, à arranger”; “non, projectif” | Flat/flasque-to-contractible argument rejected as written | N05–N06 |
| 102 | “qui semble … économique de toutes” | Economy of the standard model is tentative | N08 |
| 106 | “que nous nous proposons de déterminer” | The two localized groups still need calculation | N11 |
| 109, reused | “not yet completely understood except in a philosophical way” | General non-simply-connected interpretation of the minimal model | N16 |
| 115 | “On … voudrait”; deleted “signifie”, inserted “implique” | Desired comparison isomorphisms and weakened logical implication | N21–N22 |
| 117 | “On suspecte … $\lambda$ indépendant de $n$” | Uniformity in simplex dimension | N24 |
| 119 | “donc …” | The resolution argument stops at an ellipsis | N25 |
| 119 | “et sans doute équivalente” | Necessity of the proposed flasqueness condition | N27 |
| 119 | “On peut … affaiblir (4)” | Partly unreadable weakening in the margin | N28 |
| 119 | “On aimerait prouver un th. d’unicité” | Uniqueness goal, despite the parenthetical existence claim | N29–N31 |
| 121 | “connexe et simplement connexe ?”; “Conj.?”; large marginal “?” | Groupoid uniqueness, common refinement, and equalization | N33–N35 |
| 121 | “calcul de fractions à droite ???” | Uncertainty about the appropriate fraction calculus | N36 |
| 116, reused | “vérifications étant laissé au lecteur” | Formal properties of monodromy pairings | R13 |
| 114, 116, 124, 138, reused | “on va préciser”; “qui sera traité”; references to 10.4 | Deferred integrality/positivity and its consequences | R14, R16 |
| 124, reused | “On peut se demander s’il est à valeurs dans $\mathbb Z_K$” | Integrality after potentially semistable reduction | R17 |
| 126, reused | “sous réserve de la validité du théorème de TATE” | Reconstruction from the Barsotti–Tate pro-group | R20 |
| 128, reused | “La vérification … est alors laissée au lecteur” | Equality of two definitions of the pairing | R22 |
| 130, reused | “devrait être valable”; “il devrait en être ainsi” | Removing the characteristic restriction via Tate’s theorem | R23 |
| 130, reused | “On peut donner une autre démonstration” | Alternative good-reduction proof sketched with missing references | R24 |
| 132, reused | “Nous laissons au lecteur le soin d’étendre” | Extension to a regular connected one-dimensional base | R25 |
| 134, reused | “Nous laissons au lecteur le soin de vérifier” | Compatibility of finite-level pairings with projective transitions | R26 |
| 134, reused | “qui ne sera pas utilisé dans la suite” | An unused proposition, whose proof partly survives | R27 |
| 137 | Cancelled competing Stokes formula and revised degree labels | Chain-map variance and sign checking | N57 |
| 141 | “$\gamma_{0,0,\ldots,0}\overset?=1$” in the displayed normalization | Zero-index coefficient and simplex volume | N64 |
| 141 | Cancelled outer sign; inserted $C_{\lambda,\ldots}$ | Stokes recurrence still being corrected | N65–N66 |

The cancellation register also includes the direct augmentation requirement on 113 (N67), the modal weakening on 111 (N68), and the cancelled upper draft on 137 (N55). These are local reformulations or abandonments, not a blanket retraction of the whole lecture.

## 3. Standing question: title sheets, numbering, and page counts

There is **no freestanding cover/title sheet and no authorial total lecture-page count** in these 46 supplied faces. Internal headings and inherited page numbers must be distinguished from a count of the lecture.

| Scan | Visible title, heading, date, or quantity | Interpretation |
|---|---|---|
| 108 | “Détermination des hom.”, with uncertain following material | A faded internal heading; not a secure full title |
| 109 | `N27` | Inherited page marker on the English donor typescript; not a 27-page lecture count |
| 110 | Pencil `109` | Archival foliation only; no readable independent title or mathematical block |
| 111 | “Foncteurs de De Rham généralisés” | Secure internal section title |
| 118 | “Liebe Gertrud,”; unfinished “Von einer dreiwöch” | German letter fragment; no page count |
| 120 | “Massy, le 14.9.1971”; “une trentaine de pages de texte environ” | Reused typewriter-complaint letter; the quantity concerns machine use, not manuscript length, and its date does not date the lecture |
| 123 | “Complexes de données de De Rham à p.d.” | Boxed internal construction title |
| 137 | “Dualisation des hom de Stokes”, with the title’s key words doubtful | Internal live heading below a cancelled draft |
| 103, reused | §13, links with the transcendental theory / complex analytic case | SGA donor section heading |
| 101, reused | §13.3, analytic Raynaud extension | SGA donor subsection heading |
| 107, reused | §13.2, formal completion along a fibre | SGA donor subsection heading |
| 116, reused | §10, monodromy pairing; integrality and positivity theorem | SGA donor section heading |

The reused French mathematical typescript has the following inherited printed pagination; these numbers are retained at their locations and are not rearranged into source order in the transcription.

| Archive scan | Printed page | Archive scan | Printed page | Archive scan | Printed page |
|---:|---:|---:|---:|---:|---:|
| 095 | 169 | 097 | 156 | 099 | 167 |
| 101 | 171 | 103 | 166 | 105 | 170 |
| 107 | 168 | 112 | 123 | 114 | 122 |
| 116 | 121 | 124 | 120 | 126 | 119 |
| 128 | 118 | 130 | 117 | 132 | 116 |
| 134 | 115 | 136 | 114 | 138 | 137 |
| 140 | 135 | — | — | — | — |

Nineteen faces carry this SGA mathematical typescript. Together with the English donor 109, the nearly blank reverse 110, and the reused letter 120, the inventory has **22 `reused_typed` faces**; it has **23 `text` faces** (including the German fragment 118), **one `cancelled_draft` face** (137, with surviving live material below), and **zero `cover` faces**. These are the required coarse inventory categories, not claims that every face has only one textual layer. Later pencil foliation and the typed source pages are different numbering systems.

## 4. Supplied-context status and research-register connections

The entire `RESULTS_STATE.md` was read before these notes were authored. Its statuses are previous runs’ claims unless the register explicitly records review. No directly settled result about this particular PD de Rham complex is supplied. The relevant entries are:

| Register ID | Location and stated status | What these pages contribute |
|---|---|---|
| **WG2 §2.4 #5** | `notes/RESULTS_STATE.md`, line 124; unchecked question/plan, described there as “A thread, not a statement” | Concrete integral PD/cochain material and definite comparison gaps; no proved bridge to the integral Lefschetz ring of cote 16 scan 14 or the δ′-divisibility lead of cote 47 scan 9 |
| **WG H6** | Same file, line 125; unchecked hunch, displayed statement truncated | Comparisons to schematization must retain higher information and exact algebraic structures; O09 tests only the displayed truncation |
| **WG2 §Week #3** | Same file, line 126; unchecked organizational plan | Helps locate the planned R-SCHEM dossier; it supplies no mathematical theorem |
| **PATHS A.5** | Same file, line 99; claimed ordinary-colimit/homotopy-colimit counterexample in a different setting | A caution relevant to N46/O12, not a theorem transferred to this construction or rederived here |

Every individual note below has its own case-insensitive regular-expression search across **all six supplied context files**. The query, complete matching lines and offsets, input hashes, and explicit no-match/error distinctions are retained in `records/note_context_searches.json`; a compact overview is in `records/note_context_searches.md`. A lexical hit is not treated as a mathematical match. Each note therefore also names a reviewed contextual locus, or states the absence of a direct counterpart, and says whether the new material adds, restates, differs, or contradicts. No archive scan number is fabricated for the typed PS excerpts.

The most consequential contextual distinction is in PS §119: its rejected derived-Γ expectation and its continuing discussion of PD de Rham linearization are separate statements (L12). Likewise PS §124’s module-forgetting objection is different from the explicit scalar extension on 135 (L13). The notes preserve those distinctions rather than treating a shared operation name as a proof or counterexample.

## 5. Individual research notes

Each entry has a one-to-four-sentence analytical body. Textual cues quote brief fragments from the frozen reading; LaTeX state macros and alternatives are shown literally when needed. Ellipses in cues mark editorial omission, not additional manuscript text. The complete diplomatic context remains in the page files. The context-location and search fields document the separate cross-check required for each item.
