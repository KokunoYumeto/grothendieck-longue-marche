#!/usr/bin/env python3
"""Insert the checked census and standing-question registers into research notes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
notes_path = ROOT / "MPL_93_002-046_notes.md"
notes = notes_path.read_text()
census = (ROOT / "research" / "typed_census_review.md").read_text()
start = census.index("| Scan |")
end = census.index("\n\nTotals:", start)
table = census[start:end]
table = table.replace(
    "**F.** Foliation only recorded; inventory notes the typescript is inverted on the sheet.",
    "**F.** Foliation only as a separate annotation; mathematical symbols in the copied typescript include handwriting of unestablished authorship; sheet inverted.",
)

typed = r"""There are **33 typed or printed sheets: 24 reused_typed and 9 typed**. The other nine retained pages are seven handwritten text sheets (004, 018, 021, 023, 031, 033, 036) and two covers (027, 037); no retained sheet is classified as cancelled_draft.

The text identities used in the table are **A**, the Tate/Deligne elliptic-curve formulary (19 sheets); **B**, Wanderley's 1981 orientation offprint (3); **C**, the unidentified English operator/vector-measure typescript (2); and **D**, the folder's own Dieudonné/crystalline programme (9), with its published parallel identified in C01. “Own” in the inventory classification distinguishes the programme from reused texts by other authors; it does not deny that a published version exists.

**Annotation status:** **A** means substantive additions or corrections beyond foliation; **F** means only foliation is recorded as a separate added layer; **M** means foliation plus a nonverbal or doubtful marginal mark. The census was cross-checked against the frozen transcription and inventory after the primary reader's image audits. Underlining and handwritten mathematical symbols within a reproduced typescript do not by themselves establish a later annotation by Grothendieck; corrections also include overtyping, particularly on 044. The rubric on 003 explicitly attributes the G? correction convention to Grothendieck, but does not authenticate every marginal number or mark.

""" + table + r"""

The totals are **17 A, 14 F, and 2 M**. Substantive annotated/corrected sheets are 003, 005, 006, 010, 011, 015, 019, 022, and 038–046; the additional marks on 016 and 034 are kept separate. Every typed/printed sheet carries the marginal foliation recorded above, so “foliation only” does not mean wholly unmarked, and it does not assign that foliation to a particular hand. The two English sheets remain **unidentified** in this census; the Huff candidate in A01 is not promoted to an attribution.
"""

titles = r"""All scan references in this register are to cote 93. Printed pagination, marginal foliation, and a count inferred by the reader are kept distinct.

| Scan(s) | Title or identifying heading visible on the sheet | Pagination or page-count evidence |
|---|---|---|
| 003 | COURBES ELLIPTIQUES : FORMULAIRE; “d'après J. Tate”; “mis au goût du jour par P. Deligne” | Opening sheet has no encoded internal page numeral; marginal folio 2. Subsequent supplied formulary sheets carry internal pages 2–19, giving 19 supplied sheets including this opening, not a written “19 pages” declaration. |
| 004 | Formules utiles | Handwritten heading; folio 3; no written page total. |
| 018 | Question connexe | Handwritten heading; folio 17; no written page total. |
| 027 | Orientation, explicitly doubt-marked | A cover/title sheet; folio 26; no written page total. |
| 028–030 | Théorie axiomatique de l'orientation des variétés topologiques à bord, Marcus Wanderley | Printed pages 213, 214, 215; C. R. Acad. Sc. Paris 292, 19 January 1981; three supplied offprint pages, not a handwritten “3 pages” note. |
| 031 and 033 | “Une théorie de l'orientation …” within the handwritten definitions | Folios 30 and 32; no separate title sheet or total. The interposed reused English scan does not continue the orientation prose. |
| 032 and 034 | No author/title on either fragment | Internal page 6 on scan 032 and page 5 on scan 034; folios 31 and 33. Their textual order is 034→032, but the transcription correctly retains scan order. |
| 037 | Overlined and underlined V; Programme de la Théorie; (Cristaux) | A cover/title sheet; folio 36; no page-range or total declaration. |
| 038 | “1) Programme de la théorie de Dieudonné …”; marginal “Nouveau Chapitre” | First of nine supplied programme sheets, folios 37–45 on scans 038–046; no internal page numerals 1–9 are supplied by the encoding. |
| 044 | “2) Théorie de déformations pour les schémas abéliens.” | A section heading within the programme, not a new cover or independent page count. |

No explicit written package total such as “19 pages” or “Pages 1–67” was identified on the supplied sheets. The ranges 53–73, 33–52, and 33–39 in the margin of 003 are bibliographical page references, not pagination of the physical manuscript. The supplied README's 235-page figure concerns the larger, unprovided cote; the present package has exactly 42 retained scans, with 002, 026, and 035 omitted as blank by the input package.
"""

flags = r"""This register separates the author's explicit questions, reference requests, and qualifications from proof announcements. A promise to prove a claim later is not the same as an admission that it may be false. Doubt macros in the transcription record the reader's uncertainty and are not evidence of the author's own mathematical doubt.

| Scan(s) | Brief manuscript words / mark | What is unverified, qualified, or deferred | Detailed note |
|---|---|---|---|
| 004 | “Question : h=… ? à l'∞” | Hasse-section normalization at the Tate cusp. | E05 |
| 005 | “réf”, twice | Supporting references for duality and cohomology/base-change assertions; these are annotations to the reused text. | E03 |
| 018 | “Question connexe”; “étude … à faire de j” | Formal deformation quotient and local behavior of j; the word between “étude” and “à faire” remains doubtful. | E13–E17 |
| 018 | “? semi direct …” | Wild automorphism-group interpretation, with a doubtful final quaternion letter. | E18–E19 |
| 019 | “[vrai seulement en faisceautisant !]” | Qualification of the statement about the two automorphisms. | E20 |
| 033 | “il sera vrai a posteriori” | Orientation on a connected space determined by its value at one point. | O05 |
| 038 | “On … définiraun foncteur”; “on prouve” | Construction of the Dieudonné functor and comparison with classical perfect-field theory are announced, not proved in these programme sheets. | C02–C04 |
| 039 | “Une question importante … que je n'ai pas résolue”; “Problème 1” | Full faithfulness and characterization of the essential image. | C05–C07 |
| 039 | “il me semble qu'il faudrait” | Proposed route through a finite-flat-group theory. | C08, C10 |
| 039 | “que je n'ai pas réussi à dégager encore”; “très probablement” | Unspecified additional structures, probably involving a filtered derived object. | C08 |
| 039 | “sans doute inutile si S₀ est parfait” | Tentative removal of the extra structures over a perfect base. | C09 |
| 040 | “Problème 2”; “devrait évidemment impliquer” | Finite-group anti-equivalence and its claimed implication for Problem 1 over a perfect base. | C10–C11 |
| 041 | “qui sera construit plus bas”; “définition à reporter” | Formal group and tangent/dual notation still depend on later or earlier generalities. | C12, C14 |
| 041 | Doubt-marked “formule inutile si … parfait” | A faint perfect-base qualification, not securely interchangeable with the note on 039. | C09 |
| 042 | “sera explicité plus bas”; “On … prouvera” | Hodge interpretation and the Barsotti–Tate deformation theorem. | C14 |
| 042 | Inserted “si S' est à p. div. nil ou …” | The preceding unqualified equivalence is narrowed; the dual-infinitesimal wording has a doubt mark. | C15 |
| 042–043 | “Si le … problème 1 avait une réponse affirmative” | The claimed classification on a p-nilpotent base is conditional on Problem 1. | C05–C06, C13–C15 |
| 043 | “Problème 3”; “j'ai un candidat” | Finite locally free p-group deformation variant; candidate not supplied. | C16 |
| 043 | “on prouvera mieux”; inserted “pour tout cristal de Dieud. M” | Exactness on all stated thickenings, including locally free kernels/images. | C17–C19 |
| 043–044 | “on montre”; “propriétés de fidélité” | Existence/uniqueness and descent of the canonical filtration. | C20–C21 |
| 044 | “d) Passage à la limite”; “e) … isogénies … Tate”; “f) Dualité” | Three undeveloped programme headings, not completed theorems. | C22–C24 |
| 045 | “théorème connu (cf. livre de Mumford …)” | Existence of an affine-base abelian lift is invoked with an imprecise reference. | C26 |
| 046 | “à charge de définir … un système transitif d'isomorphismes canoniques” | The comparison maps needed for a crystal remain to be constructed. | C30 |
| 046 | “on prouve”; “ma vieille lettre à Tate”; “sera exposée … dans la suite du séminaire” | Characteristic-zero rigidity, passage to general nil-thickenings, and the exponential construction are referred elsewhere. | C31–C33 |

Two additional incompletions should not be disguised as explicit doubt markers: the corollary on 021 has no completed conclusion, and 046 ends mid-sentence. The correction of a coefficient on 036 and the concern about Problem 1 on 043 are recorded as **withdrawn in the same text** in P02 and C35; the latter concern is answered immediately by a claim about the canonical filtration, not by a negative solution of Problem 1.

Conversely, the G? signs on the formulary follow the correction-marker rubric on 003 and are not automatically mathematical question marks. The labels “hyp. de …” on 031/033 classify axioms or induction roles rather than expressing doubt about them. Assertions and missing proofs in the Wanderley offprint and unidentified English typescript are attributed to those texts, not automatically to Grothendieck.
"""

for marker, value in [
    ("<!-- TYPED_CENSUS -->", typed),
    ("<!-- TITLES_AND_COUNTS -->", titles),
    ("<!-- SELF_FLAGGED_REGISTER -->", flags),
]:
    if marker not in notes:
        raise SystemExit(f"Missing insertion marker: {marker}; refusing to overwrite a completed section")
    notes = notes.replace(marker, value, 1)
notes_path.write_text(notes)
print("Inserted 33-sheet census, title/pagination register, and self-flagged-step register.")
