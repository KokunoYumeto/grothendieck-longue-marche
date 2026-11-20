#!/usr/bin/env python3
"""Write Reader C's page-only second reading of 143_scan029.

This script assembles already observed readings and performs static checks only.
It does not read or transform image pixels, OCR, compile TeX, or edit accepted files.
"""
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parent
KEY = "143_scan029"
PACKET = json.loads((BASE / "reader_packets" / f"{KEY}.json").read_text())
ACCEPTED_PATH = ROOT / "pages" / f"{KEY}.tex"
REPORT_PATH = ROOT / "reviews" / f"{KEY}_accepted.json"
accepted_bytes = ACCEPTED_PATH.read_bytes()
report_bytes = REPORT_PATH.read_bytes()
accepted = accepted_bytes.decode()
prior = json.loads(report_bytes)
candidate = accepted


def crop(suffix):
    return f"crops/{KEY}_{suffix}.png"


BOXES = {
    "A_opening_M": [410, 270, 590, 410],
    "A_deleted_un": [1080, 455, 1285, 545],
    "A_associated_clause": [540, 770, 1650, 1000],
    "main_notion_proche": [275, 900, 670, 1005],
    "A_first_formula": [315, 1000, 1645, 1205],
    "A_explanation": [310, 1170, 1630, 1515],
    "A_second_formula": [385, 1925, 1655, 2045],
    "A_last_formula": [375, 2150, 1665, 2300],
    "A_diagonal_margin": [15, 1490, 400, 2265],
    "A_structure": [700, 2005, 1655, 2155],
    "A_stricts_orientes": [330, 2065, 705, 2190],
    "main_exponent_statement": [275, 1435, 1660, 1790],
}
VIEW_ORDER = list(BOXES)

# Only the surviving compact stem/return graph is drawn. Its crossing is supplied
# by the existing deleted macro, and uncertainty encloses that deleted state.
# No letter name is assigned to the graph and no illegible formula slot remains.
RESIDUAL_GRAPH = (
    r"\begin{tikzpicture}[baseline=0pt,x=.45em,y=.4em,line width=.45pt,line cap=round,line join=round]"
    r"\draw (0,.12) .. controls (.08,.18) and (.25,.56) .. (.27,.91)"
    r" -- (.21,.19) .. controls (.19,.02) and (.33,.11) .. (.39,.34)"
    r" -- (.66,1.05) .. controls (.62,.70) and (.58,.16) .. (.64,-.08)"
    r" .. controls (.66,-.14) and (.76,.18) .. (.80,.26) -- (1.28,.20) -- (1.30,.10);"
    r"\end{tikzpicture}"
)
CROSSED_GRAPH = r"\unsure{\deleted{" + RESIDUAL_GRAPH + "}}"
ANNOTATION = r"\overset{" + CROSSED_GRAPH + "}{=}"

findings = []


def finding(*, place, before, after, reason, confidence, suffix, C, H,
            against_C, against_H, kind="misread symbol or index",
            consequential=False, marks=(), certainty_only=False,
            metadata_only=False, **extra):
    global candidate
    assert before in accepted, (place, "before absent")
    if not metadata_only:
        assert candidate.count(before) == 1, (place, candidate.count(before))
        candidate = candidate.replace(before, after, 1)
    assert after in candidate, (place, "after absent")
    row = dict(
        place=place, before=before, after=after, reason=reason,
        confidence=confidence, crop=crop(suffix), box=BOXES[suffix],
        against_C=against_C, against_H=against_H, C=C, H=H,
        kind=kind, consequential=consequential, marked_in_H=False,
        decision_updates=list(marks), certainty_only=certainty_only,
        metadata_only=metadata_only,
    )
    row.update(extra)
    findings.append(row)


finding(
    place="Map (1): inner fundamental-group graph",
    before=r"\unsure{\Pi|\pi}_1(\overline X\setminus",
    after=r"\pi_1(\overline X\setminus",
    reason="Both local pi graphs have a broad almost flat cap and two descending legs. The inner right leg has a small curved foot, while the outer graph also has a straight left leg and bent right foot. Size and cap width do not establish a different letter case. The common pi identification is supported by this local comparison and the supplied shared hand comparison; it restores the preferred letter in both witnesses.",
    confidence="medium", suffix="A_first_formula",
    C=r"\pi_1(\overline X\setminus", H=r"\pi_1(\overline{X} \smallsetminus",
    against_C=False, against_H=False,
    existing_difference_rows=[19], restores_C_preferred=True,
    collation_disposition="Remove accepted row 19 from material C/H differences; preserve this audit finding as the record of the changed accepted preference.",
)
finding(
    place="Map (2): inner fundamental-group graph",
    before=r"\unsure{\Pi|\pi}_1(X\setminus",
    after=r"\pi_1(X\setminus",
    reason="The inner graph has a flat cap, two descending legs and an oblique retracing across the left part. Its cap and legs belong to the same locally visible pi family as the outer graph; the retracing supplies no separate capital/lowercase distinction. Read pi at medium confidence. The independently clear absence of a bar on X is not changed by this letter decision.",
    confidence="medium", suffix="A_second_formula",
    C=r"\pi_1(X\setminus", H=r"\pi_1(\overline{X} \smallsetminus",
    against_C=False, against_H=False,
    existing_difference_rows=[44], restores_C_preferred=True,
    collation_disposition="Remove accepted row 44 as an independent case difference; H's X-bar error remains in accepted row 43.",
)
finding(
    place="Map (2 bis): inner fundamental-group graph",
    before=r"\mathrm{extlac}^{\circ\circ}\unsure{\Pi|\pi}_1(X^{an}",
    after=r"\mathrm{extlac}^{\circ\circ}\pi_1(X^{an}",
    reason="The final graph has a heavily covered left leg, a broad cap and a descending right leg. The left-domain pi on the same line has the same flat-cap family, and the two preceding inner graphs do not show a secure case contrast. Read pi by that local comparison and the supplied shared notation, without treating the overtraced stroke as a clear contrary capital. The low 1 and the two analytic letters remain separate physical marks.",
    confidence="medium", suffix="A_last_formula",
    C=r"\Pi_1", H=r"\pi_1(X \smallsetminus",
    against_C=True, against_H=False,
    existing_difference_rows=[57],
    collation_disposition="Revise accepted row 57 to C-only, final pi_1, medium confidence, non-consequential; remove the earlier certainty-only Pi-confidence item.",
)
finding(
    place="Map (2): full-height reduced basepoint",
    before=r"\overline M_{g,\nu};\unsure{j|\xi}",
    after=r"\overline M_{g,\nu};\xi",
    reason="The crop shows an undotted, tall stem with a short upper turn; its lower return was independently visible in the native second half. This is a reduction of the full looped xi seen in map (1) and the following prose, compatible with the shared comparison supplied by main. No dot or other local stroke establishes a distinct j. The graph remains at the main-letter height after the semicolon, outside the lower g,nu subscript.",
    confidence="medium", suffix="A_second_formula",
    C=r"\overline M_{g,\nu};\unsure{\xi|j}", H=r"\overline{M}_{g,\nu;\xi}",
    against_C=False, against_H=True, consequential=True, marks=["M0723"],
    existing_difference_rows=[41], restores_C_preferred=True,
    collation_disposition="Revise accepted row 41's final/evidence/confidence to xi; keep only the existing H basepoint-height difference, no new C letter row. Supersede the earlier j-first preference item.",
)
finding(
    place="Map (2 bis): full-height reduced basepoint",
    before=r"M_{g,\nu}^{an};\unsure{j|\xi}",
    after=r"M_{g,\nu}^{an};\xi",
    reason="The final basepoint has an undotted long shaft, a small angular turn at its top and a leftward lower hook. It repeats the reduced second-map graph, while the first map and prose provide the fuller xi family. The supplied common notation therefore identifies this ambiguous compressed graph as xi at medium confidence. It is not a clearly written contrary j, and its full height is independently distinct from the low indices.",
    confidence="medium", suffix="A_last_formula",
    C=r"\unsure{\xi|j}", H=r"M_{g,\nu;\xi}",
    against_C=False, against_H=True, consequential=True, marks=["M0727"],
    existing_difference_rows=[55], restores_C_preferred=True,
    collation_disposition="Revise accepted row 55 to final xi at medium confidence; retain the existing H placement difference. Supersede the earlier j-first preference item; no C letter difference remains.",
)
finding(
    place="Map (2 bis): crossed symbolic residue above equality",
    before=r"\overset{\deleted{\illegible{1}}}{=}", after=ANNOTATION,
    reason="The existing last-formula crop shows a compact pair of rising stems with low or angled returns and a short rightward exit. The long brace stroke crosses this compact graph directly above the equals. No sequence of prose letters or named mathematical symbol can be secured. Its position is mathematical, so the formula-symbol illegible placeholder is replaced by a literal approximation of the surviving strokes, explicitly uncertain and deleted. The equality, short brace endpoints and lower T label remain in their original relative positions.",
    confidence="medium", suffix="A_last_formula",
    C=r"\deleted{\illegible{1}}=",
    H="le signe\nsous l'accolade de $(***)$ est précédé d'un mot biffé illisible",
    against_C=True, against_H=True, kind="drawing or diagram",
    existing_difference_rows=[60, 61],
    identification_confidence="low",
    collation_disposition="Update the rendering in row 60 and revise row 61's final, kind and evidence; do not add a duplicate location row. The residual graph is not identified as a word or a letter.",
)
finding(
    place="M0718: genus preference is a material C-only difference",
    before=r"\unsure{g|0}", after=r"\unsure{g|0}",
    reason="The genus graph has a small upper compartment and an elongated sloping lower oval. Those physical parts favor g, while retracing still permits 0, so the accepted local uncertainty is retained at low confidence. The preferred first character differs from C's 0-first reading. Reordering those alternatives changes the preferred reading and must be counted as a C-only material difference, not as certainty alone.",
    confidence="low", suffix="A_explanation",
    C=r"\unsure{0|g}", H=r"de genre $g$",
    against_C=True, against_H=False, consequential=True, marks=["M0718"],
    metadata_only=True,
    collation_disposition="Restore the existing excluded Genus glyph after de genre row as a material C-only row. Remove/supersede Genus preference only in certainty_resolutions and the exclusion_reason saying alternative order is certainty only.",
)

# An exact row-number map preserves auditability without renumbering accepted rows.
change_updates = {
    19: dict(action="remove from material collation", final=r"\pi_1(\overline X\setminus", against_C=False, against_H=False,
             confidence="medium", ink=findings[0]["reason"]),
    44: dict(action="remove from material collation", final=r"\pi_1(X\setminus", against_C=False, against_H=False,
             confidence="medium", ink=findings[1]["reason"]),
    57: dict(action="revise existing material row", final=r"\pi_1", against_C=True, against_H=False,
             confidence="medium", consequential=False, ink=findings[2]["reason"]),
    41: dict(action="revise existing H placement row", final=r"\overline M_{g,\nu};\xi", against_C=False, against_H=True,
             confidence="medium", ink=findings[3]["reason"]),
    55: dict(action="revise existing H placement row", final=r"M_{g,\nu}^{an};\xi", against_C=False, against_H=True,
             confidence="medium", ink=findings[4]["reason"]),
    60: dict(action="update literal final to match candidate", final=None, ink=prior["changes"][59]["ink"] + " The crossed residue is now a locally uncertain literal drawing; the two brace endpoints themselves are unchanged."),
    61: dict(action="revise existing placement/rendering row", final=ANNOTATION, against_C=True, against_H=True,
             kind="drawing or diagram", confidence="medium", ink=findings[5]["reason"]),
}
change_updates[60]["final"] = prior["changes"][59]["final"].replace(r"\unsure{\Pi|\pi}_1", r"\pi_1").replace(r"\overset{\deleted{\illegible{1}}}{=}", ANNOTATION)

# Four prior guide rows used editorial placeholders instead of witness excerpts.
# Repair the audit copy's snippets without changing their reading or flags.
guide_literals = {
    65: (r"\inserted{sur $\mathbf Q$}", r"(sur $\mathbb{Q}$)"),
    66: (r"\inserted{relatives}", r"(relatives)"),
    67: (r"\inserted{(sur $\overline{\mathbf Q}$)}", r"(sur $\overline{\mathbb{Q}}$)"),
    68: (r"\inserted{$\in M_{g,\nu}(\overline{\mathbf Q})$}", r"\ill{} $M_{g,\nu}(\overline{\mathbb{Q}})$"),
}
for n, (c, h) in guide_literals.items():
    change_updates[n] = dict(action="replace editorial placeholders with literal witness excerpts only", C=c, H=h)

row_observations = [
    "The circled 9 and two distinct underline rules are visible in the native first half. The title is live, not crossed out.",
    "Read the compact des ending in the first half; there is no separate x ending for deux.",
    "The reused opening-M crop separates the thick M from the thinner earlier cap and lower return; the earlier T-like letter remains low-confidence.",
    "The raised sur Q and its curved guide are visible above pour; there are no prose parentheses around this occurrence.",
    "The raised relatives sits above lisses and has a curved guide, not textual parentheses.",
    "The rule lies immediately below munies, not below de or the cancelled item.",
    "The existing deletion crop shows two covered clusters; the provisional un is not promoted to certainty or expanded.",
    "The native lines run from nu-uple to de nu sections without intervening ordonne.",
    "The first half reads sur chaque fibre; each word is a single group and no repeated deux/fibre sequence occurs.",
    "The final fibre stroke has no detached writing-weight period in the first half.",
    "The existing associated-clause crop shows the two reduced marks; retain à|: separately from clear associé and une.",
    "The reused notion-proche crop resolves the two left words; the associated-clause crop leaves only schemable's compressed interior uncertain.",
    "The first-formula crop has a gap after hom, with no separate dot before naturel.",
    "The short cancelled exterior group remains crossed and abbreviated; its ending is covered, so extér. stays explicitly unsure.",
    "The first label has a retraced vertical core and parentheses, supporting 1; no star count is transcribed.",
    "The separate first-map surcharge again has a heavy M covering a thin earlier cap and return; keep the earlier-letter doubt.",
    "The first xi reaches full main-letter height after the semicolon; g and nu sit lower. The lower indices are not extended to include xi.",
    "The l in lac rises from the operator baseline, and the single small ring sits above its end.",
    findings[0]["reason"],
    "The first puncture list contains one continuation shaft and a low comma on each side of it, not an ellipsis.",
    "The tuple contains one comma after x_1 and a single fine shaft before the final x_nu, without a second comma.",
    "The tuple arrow has its own head; le pt correspondant precedes the raised parenthesized sur Qbar and its guide before de genre.",
    "The crop shows the additional final low wave of associée after the accented ending; this source grammar is preserved.",
    "The membership sign and M(Qbar) are raised after the prose xi; g and nu remain low and the fine guide attaches there.",
    "The rounded O and short n remain visible under the crossing before the live L; no restoration to live text is made.",
    "The curved mark left of L'exposant belongs to the membership guide. The live capital L begins a sentence, not a parenthesized aside.",
    "The reused exponent-statement crop shows separate marque, le and the long crossed f of fait.",
    "Read prend les autom de across the line break; autom stays abbreviated with no invented stop or expansion.",
    "The negative n'échangent pas entre eux sequence is legible across the two main lines.",
    "The separate de, tall-l lacets and accented associés precede aux; no d'inertie group appears.",
    "The detached mark after x_i is elongated horizontally. Retain dash/period uncertainty and no closing prose parenthesis.",
    "The rotated existing margin crop has peut-être after il faut and a separate être before plus.",
    "Read commutation and the first separate two-point colon at the next short line; neither aux nor a long dash fills that place.",
    "Read des opérations and the independently separate second two-point colon before définies.",
    "The long f and reduced -inies ending support définies; no further tall t supports définition.",
    "The local S graph has an outer loop and inner return with low nu, followed by sur le. Shared identification is supplied by main's earlier comparison, not a new other-page inspection by C.",
    "Two question marks precede Il faut regarder surtout le cas and the written g=0,nu=3.",
    "There are four separate dark terminal dots in the upright margin crop. The adjacent long diagonal mark belongs to main text.",
    "The native second half reads Notons qu'on a aussi in four groups; no longer Notations word appears.",
    "The second label has a curled 2-like upper form and retraced lower return, not two separated stars.",
    findings[3]["reason"],
    "The second operator's lac stays on the baseline; two separately visible rings are raised above its end.",
    "The second-map X has clear empty upper space. Keep the source's unbarred X independently of the pi identification.",
    findings[1]["reason"],
    "The second puncture list contains one comma after x_1 and one shaft, with no independently visible comma before x_nu.",
    "The structure crop reads qu'on prend des autom; the short word groups do not support se borne aux.",
    "The existing stricts crop ends the word after the crossed t and small s; the single rule belongs immediately beneath it.",
    "The native second half and structure crop show compatibles avec la structure; the tall b/l/t strokes remain in those word groups.",
    "The structure colon consists of two points. The following flattened word remains locale|lacets at low confidence.",
    "A separate curved mark before i.e. remains possible opening parenthesis; no matching close is supplied.",
    "After the mathematical closing parenthesis, small points continue at the right edge; no reduction to a single stop.",
    "Aut. and the small orientés-like word are below the main continuation. Only stricts has a rule beneath it; the small word remains unsure.",
    "The final label has raised 2 with a compact bis-like continuation, not three separated stars.",
    "M has two short raised a/n marks to its right; they are not a centered bar. The low g and nu remain distinct.",
    findings[4]["reason"],
    "The final lac remains on the operator baseline. Splitting Aut and extlac only fixes the observed partial-brace position.",
    findings[2]["reason"],
    "The final list has a comma after x_1 and a fine shaft before x_nu, without a second comma.",
    "X has two separate upper-right analytic marks; the centered first-map bar is a visibly different feature.",
    "The last-formula crop shows the brace starting inside the operator and ending near the opening set brace before x_1, with a low central cusp. Its shortened span remains.",
    findings[5]["reason"],
    "The native bottom line begins dont on sait before the parenthesized théorie top. phrase.",
    "The bottom line continues que c'est un and stops without completing the sentence; no qui induit substitution is made.",
    "The pale lower-left digits are 28. No signature or other evidence identifies the pencil writer.",
    "The first half shows the sur Q guide curving down beside pour and running beneath the raised addition; its explicit TikZ representation is retained.",
    "The first half shows the relatives guide curving down before lisses and under the raised word; its explicit TikZ representation is retained.",
    "The explanation crop shows the long guide below the parenthesized field phrase, descending before de genre and turning upward at the other end.",
    "The explanation crop shows the membership guide descending after xi before the cancelled On and passing under the raised membership expression.",
]
assert len(row_observations) == 68

collation = []
for n, old in enumerate(prior["changes"], 1):
    r = deepcopy(old)
    upd = change_updates.get(n, {})
    for field in ("final", "C", "H", "against_C", "against_H", "confidence", "kind", "consequential", "ink"):
        if field in upd:
            r[field] = upd[field]
    r["accepted_row"] = n
    r["accepted_place"] = old["place"]
    r["audit_observation"] = row_observations[n-1]
    r["audit_status"] = upd.get("action", "confirmed unchanged")
    r["material_after_audit"] = bool(r["against_C"] or r["against_H"])
    r["audit_view"] = (r["crop"] if r.get("crop") in [crop(s) for s in VIEW_ORDER]
                       else "native half1" if n <= 12 or n in (65, 66) else "native half2")
    collation.append(r)

restored_genus = deepcopy(prior["excluded_certainty_only_changes"][0])
restored_genus.pop("exclusion_reason", None)
restored_genus["ink"] = findings[-1]["reason"]
restored_genus.update(accepted_row=None, source="excluded_certainty_only_changes[0]",
                     audit_status="restore to material collation", material_after_audit=True,
                     audit_view=crop("A_explanation"))

existing_difference_updates = []
for n, update in change_updates.items():
    existing_difference_updates.append(dict(
        accepted_row=n, accepted_place=prior["changes"][n-1]["place"],
        before={k: prior["changes"][n-1].get(k) for k in update if k != "action"},
        **update,
    ))

# Original packet MARKS only, each independently inspected.
decisions = deepcopy(prior["decisions"])
decision_evidence = {
    "M0716": "The left-end notion-proche crop resolves those words and the adjacent crop shows two equals bars. The last word's flattened interior remains insecure, so only schémable stays unsure.",
    "M0717": "The tuple is followed by a distinct rightward shaft/head, then le, a crossed pt abbreviation and correspondant. No est la courbe strokes occupy that position.",
    "M0718": findings[-1]["reason"],
    "M0719": "The rotated margin crop shows st-like high strokes, a dotted short i and a final t-like cross before the comma; strict remains medium.",
    "M0720": "The first pair in the diagonal note consists of two separate vertically placed points, not a connected accented a body.",
    "M0721": "The second line-leading pair is independently two separated points before définies.",
    "M0722": "The rotated crop shows the long f-descender and reduced dotted -inies sequence, without a second tall t.",
    "M0723": findings[3]["reason"],
    "M0724": "The word after the clear structure colon has flattened middle letters and a late high return; retain locale|lacets without settling it from the Tate explanation.",
    "M0725": "The marginal word begins with a small o-like mark and ends with a raised accent-like point, but its compressed middle is not secure. The nearby line belongs beneath stricts above it.",
    "M0726": "M's upper marks are separate a/n components to the right, not one centered bar; g and nu remain below.",
    "M0727": findings[4]["reason"],
    "M0728": "X has two separate short upper-right a/n components, unlike the centered first-map bar.",
}
for d in decisions:
    d["ink"] = decision_evidence[d["id"]]
    d["audit_status"] = "confirmed unchanged"
    if d["id"] in ("M0723", "M0727"):
        d.update(decision="first", reading=r"\xi", confidence="medium",
                 audit_status="resolved to original C first alternative")
    if d["id"] == "M0718":
        d["audit_status"] = "reading retained; preferred-reading accounting corrected to C-only material"

removed_doubt_names = {
    "First display inner Pi case": (r"\pi_1", findings[0]["reason"]),
    "Second display inner Pi case": (r"\pi_1", findings[1]["reason"]),
    "Third display Pi case": (r"\pi_1", findings[2]["reason"]),
    "Second display basepoint": (r"\xi", findings[3]["reason"]),
    "Third display basepoint": (r"\xi", findings[4]["reason"]),
}
remaining = []
doubt_disposition = []
for old in prior["remaining_doubts"]:
    if old["place"] in removed_doubt_names:
        reading, reason = removed_doubt_names[old["place"]]
        doubt_disposition.append(dict(accepted_place=old["place"], before=old["reading"],
                                      action="remove resolved local doubt", after=reading,
                                      confidence="medium", reason=reason))
    else:
        d = deepcopy(old)
        d["audit_status"] = "retained after independent local inspection"
        if d["place"] == "Genus glyph":
            d["reason"] = findings[-1]["reason"]
        remaining.append(d)
        doubt_disposition.append(dict(accepted_place=old["place"], before=old["reading"],
                                      action="retain", after=old["reading"], confidence=old["confidence"]))
remaining.append(dict(
    place="Cancelled compact graph above the equality in (2 bis)",
    reading=CROSSED_GRAPH,
    alternatives="No named letter or prose word secured; two rising stems, low/angled returns and a short rightward exit survive the crossing.",
    confidence="low", reason=findings[5]["reason"],
    crop=crop("A_last_formula"), box=BOXES["A_last_formula"],
    audit_status="new explicit doubt replacing an illegible mathematical-symbol placeholder",
))

inventory_observations = [
    "Pale pencil 15 at top right; writer unnamed.",
    "Circled 9, live title, two separate underline portions; no title cancellation.",
    "Full opening paragraph read through fibre; des, de plus crossed material, nu-uple, and sur chaque fibre preserved.",
    "Thick live M over thin cap/return; the covered prior letter is still doubtful.",
    "Interlinear sur Q retained without textual parentheses.",
    "Fine curved sur Q guide retained explicitly in TikZ, attached before pour.",
    "Interlinear relatives retained.",
    "Fine curved relatives guide retained explicitly in TikZ, attached before lisses.",
    "Two dark crossed clusters before nu-uple; underlying un remains provisional.",
    "Every exception numeral/equality and the final notion proche = phrase read; reduced à/: and schémable remain local doubts.",
    "On a un hom naturel read; hom has no stop.",
    "Short exterior abbreviation remains cancelled and uncertain.",
    "Map (1), exterior full xi, inner pi, individual low indices, one circle, X bar, arrowhead and first list's two commas checked.",
    "First-map prior graph is separately covered by M; uncertainty retained.",
    "Entire explanatory paragraph read; tuple arrow, feminine associée, nonexchange condition and terminal mark preserved.",
    "Parenthesized sur Qbar raised before de genre; bar and parentheses present.",
    "Long curved field-insertion guide retained, with no supplied arrowhead.",
    "Raised membership expression after xi; each index and field mark checked.",
    "Curved membership guide retained before the cancelled On.",
    "Crossed On remains deletion, followed by live capital L.",
    "Entire rotated marginal block read, including both colons, S_nu, pi_1, two question marks, g=0,nu=3 and four terminal dots.",
    "Notons qu'on a aussi read in main text, independent of margin placement.",
    "Map (2): M bar, full-height reduced xi, two circles, inner pi, unbarred X, one list shaft and only left comma.",
    "Double-circle explanation read through Tate(Qbar) and terminal points; structure colon and remaining word/parenthesis doubts preserved.",
    "Underlined stricts retains the sole rule; no additional insertion guide is visible at this word.",
    "Aut. and unsure orientés remain marginal and are not assigned a second underline.",
    "Map (2 bis): analytic M/X exponents, exterior xi, inner pi, two circles, individual indices, partial brace and Teichmüller label checked.",
    "Compact crossed symbolic residue above = is represented by uncertain literal strokes in deleted state, without an illegible formula slot.",
    "Full last line read through un; source continuation remains unfinished.",
    "Pale pencil 28 at lower left; writer unnamed.",
]
assert len(inventory_observations) == len(prior["inventory"]) == 30
inventory_confirmation = []
for item, observation in zip(prior["inventory"], inventory_observations):
    inventory_confirmation.append(dict(element=item["element"], kind=item["kind"],
                                       position=item["position"], checked=True,
                                       observation=observation))
inventory_updates = [
    dict(element="E23", field="first_words_or_objects", before=prior["inventory"][22]["first_words_or_objects"],
         after="(2), Mbar with full-height exterior xi; two operator circles; inner pi_1; X without bar"),
    dict(element="E27", field="first_words_or_objects", before=prior["inventory"][26]["first_words_or_objects"],
         after="(2 bis), M^{an}; exterior xi, operator with two circles, inner pi_1, X^{an}, physically short underbrace, T_{g,nu} (Teichmüller)"),
    dict(element="E28", field="first_words_or_objects", before=prior["inventory"][27]["first_words_or_objects"],
         after="compact crossed symbolic residue: two rising stems with low/angled returns and short rightward exit, directly above equals, drawn literally under uncertainty in deleted state", parent="E27"),
]

# All raw differences receive a page-specific disposition, including parser noise.
raw_comments = [
    "C's scan 29 is apparatus. The sheet's pencil 15 is visible, but H's author attribution is not established.",
    "Circled 9 and the live two-part underlined title are visible; H's editorial author note is not source text.",
    "The written inequality is present in both witness macros; geq/geqslant is rendering only.",
    "Read des from the short final s; no deux ending.",
    "sur Q is above the line with a physical guide; there is no opening textual parenthesis here.",
    "No closing textual parenthesis surrounds the first sur Q insertion.",
    "relatives is above lisses; the left curve is its guide, not an opening textual parenthesis.",
    "No closing textual parenthesis follows relatives.",
    "Live de precedes the short crossed material; unsure un remains deleted, without grammar repair.",
    "No ordonné appears between nu-uple and the next line's de nu sections.",
    "The source reads sur chaque fibre, with no duplicated deux or fibre.",
    "H's explanatory note is not copied as prose; the opening surcharge and two insertions are fully represented.",
    "Read associé and une; preserve the intervening reduced à|: uncertainty.",
    "notion proche is resolved by the existing left-end crop; it is no longer one wholly doubtful phrase.",
    "Only schémable remains unsure; the equals sign is two clear bars.",
    "There is no detached stop after hom.",
    "The short crossed extér.-like abbreviation remains unsure and unexpanded.",
    "The first left label is retraced 1, not an asterisk.",
    "The operator's lac is on the baseline, with one raised circle.",
    "The same physical left-hand label 1 is rendered by tag; no second label is supplied.",
    "Parenthesized sur Qbar is raised after correspondant and attached before de genre.",
    "A headed arrow followed by le pt correspondant is visible. The est la courbe alternative has no local strokes.",
    "The looped genus graph remains g|0, low. Its preferred g differs materially from C's preferred 0, so restore a C-only row.",
    "The main line reads avec nu pts marqués associée à xi; the membership expression is separately interlinear.",
    "Membership placement, feminine associée, the small point, cancelled On and live L'exposant are retained separately.",
    "Read marque le fait rather than indique.",
    "Read prend les autom de; preserve the short autom form.",
    "The negative n'échangent pas entre eux sequence is visible across the main lines.",
    "Read de lacets associés, not d'inertie.",
    "No closing prose parenthesis follows x_i; its terminal dash/period uncertainty remains.",
    "The complete diagonal note belongs in the left margin, followed in main text by Notons qu'on a aussi; H's ordering is editorial.",
    "The second left label is 2 rather than two stars.",
    "The second basepoint is identified as reduced xi at medium confidence, restoring C's first alternative; H's separate subscript-placement difference remains.",
    "The second operator's lac is on the baseline, with two separate circles.",
    "The same second physical label is rendered as tag 2.",
    "Read qu'on prend des autom, without H's se borne aux substitution.",
    "Read stricts and compatibles avec la structure, the colon, locale|lacets and the possible parenthesis before i.e.; preserve the one underline and do not expand stricts.",
    "Marginal Aut. is present, including its point.",
    "The following compressed orientés-like word remains unsure and has no separate underline.",
    "The last left label is 2 bis, not three stars.",
    "M has two upper-right an components, distinct from low g and nu; no centered overbar.",
    "The final basepoint is reduced xi at medium, full height after the semicolon. C's preferred xi is restored and H's lower placement remains a separate row.",
    "The final operator has baseline lac; its split in TeX only represents the partial brace.",
    "H's backslash-comma is spacing syntax, with no manuscript punctuation difference.",
    "X has two raised an components. Independently, the final inner group is pi by the locally checked flat-cap hand; this is C-only versus its Pi.",
    "The 1 in illegible{1} is editorial counting, not an ink numeral. Replace that mathematical slot by the uncertain deleted residual-stroke drawing directly above =.",
    "The same visible final label is 2 bis.",
    "The last line starts dont on sait before théorie top.",
    "The final words are que c'est un; the sentence remains unfinished on this page.",
    "Pencil 28 is separately inventoried; the diagonal note retains its actual marginal position and is not appended as bottom prose.",
]
assert len(raw_comments) == len(PACKET["differences"]) == 50
raw_difference_checks = [dict(number=n, packet_difference=deepcopy(d), disposition=comment, checked=True)
                         for n, (d, comment) in enumerate(zip(PACKET["differences"], raw_comments), 1)]

physical_indices = deepcopy(prior["physical_indices"])
physical_update_map = {
    "Map (1): inner fundamental-group graph": (r"\pi", findings[0]["reason"]),
    "Map (2): inner fundamental-group graph": (r"\pi", findings[1]["reason"]),
    "Map (2 bis): right fundamental-group symbol": (r"\pi", findings[2]["reason"]),
    "Map (2): basepoint": (r"\xi", findings[3]["reason"]),
    "Map (2 bis): basepoint": (r"\xi", findings[4]["reason"]),
}
physical_index_updates = []
for n, p in enumerate(physical_indices, 1):
    p["audit_checked"] = True
    p["audit_observation"] = "The listed physical mark, including its separate height and attachment, was checked in the original/native halves and the reused local crop where needed."
    if p["place"] in physical_update_map:
        new, reason = physical_update_map[p["place"]]
        physical_index_updates.append(dict(accepted_entry=n, place=p["place"], before=p["form"], after=new,
                                          confidence="medium", evidence=reason))
        p.update(form=new, evidence=reason, confidence="medium", audit_observation=reason)

existing_note_updates = [
    dict(id="143_scan029-N5", before=prior["notes"][4]["text"], after=(
        "The locally checked later basepoints are identified as reduced xi at medium confidence, and all three inner group graphs as pi, using the shared notation only where the ink admits that identification. Bars and analytic an pairs remain separate physical marks. The short brace, four single continuation strokes and their individual comma patterns, uncertain prior modular capitals, and absent matching prose parenthesis are preserved. The crossed compact graph above equals is reproduced literally under uncertainty in deleted state; it is not assigned a letter or a prose-word reading.")),
    dict(id="143_scan029-N7", before=prior["notes"][6]["text"], after=(
        "The different-reader audit confirms the four single continuation strokes and local commas, shortened brace, four insertion guides, literal source grammar and terminal dash/period doubt. It resolves the two later basepoints as xi and the three inner groups as pi at medium confidence. The crossed item above equals remains unidentified but is drawn literally as a deleted uncertain graph. The genus remains g|0. Preferred-reading changes are material even when an alternative was previously listed: the genus preference against C's 0 needs a C-only row, and final pi against C's Pi needs a C-only row; restored xi matches C's preferred letter while the independent H placement differences remain.")),
]

certainty_dispositions = [
    dict(accepted_place="Third Pi: confidence lowered", action="supersede", reason="Final preferred pi now differs from C's Pi; accepted row 57 becomes C-only material, not certainty-only."),
    dict(accepted_place="Genus preference only", action="remove from certainty-only list", reason="Preferred g differs from C's preferred 0 despite retaining both alternatives. Restore its excluded material row."),
    dict(accepted_place="Second display: exterior basepoint shape and placement (preference only)", action="supersede", reason="Final xi restores C's preferred reading. Record the local resolution at medium; keep the independent H placement row."),
    dict(accepted_place="Third display: basepoint independently inspected (preference only)", action="supersede", reason="Final xi restores C's preferred reading. Record the local resolution at medium; keep the independent H placement row."),
]

notes = [
    dict(id="143_scan029-auditC-N1", text="Reader C independently read only this sheet's original, two native halves and twelve reused existing crops. The title is live and underlined, while the exterior abbreviation, prior modular graphs, On and final compact graph retain their deletion/overwriting states. Every original MARK, existing inventory element, raw C/H difference and listed physical index was checked."),
    dict(id="143_scan029-auditC-N2", text="The two full xi graphs in the first display and prose and the two reduced later stems were checked locally. Main's already completed cross-page comparison, reported in the supplied notation table, supports the shared xi identification. C did not inspect other pages during this audit. All three inner flat-capped group graphs were also compared locally with the outer pi signs; none demonstrates a clear contrary capital."),
    dict(id="143_scan029-auditC-N3", text="The final compact crossed graph cannot safely be called a prose word or a named mathematical symbol. The two rising stems, low/angled returns and short rightward exit are drawn under uncertainty, in deleted state above the equals. This changes the representation of already inventoried E28; it adds no hypothetical missing symbol and does not alter the short brace extent."),
    dict(id="143_scan029-auditC-N4", text="The source's genus remains g|0 at low confidence on its actual looped ink. The preferred g is a material C-only difference against 0-first; the fact that C listed g as an alternative does not make the preferred-reading change certainty-only. Final pi in the last display is likewise C-only, while the first two inner pi choices restore both witnesses. Final xi restores C in both later domains, with H's independent placement differences retained."),
    dict(id="143_scan029-auditC-N5", text="The local exception-paragraph à|: remains low, and only schémable is doubtful in the notion proche = phrase. Other continuing doubts include both covered modular capitals, the crossed un/extér. groups, locale|lacets, possible opening parenthesis, orientés and the terminal dash/period. No prose completion, automatic X bar, additional list comma, guide or punctuation is supplied."),
    dict(id="143_scan029-auditC-N6", text="The accepted report's N6 integer-inequality check belongs to the main reader, as explicitly stated in that report. Reader C performed no proof or calculation check here. The modular-topos, monodromy, Tate and Teichmüller claims were carried as transcription background, and were not used to repair clear ink."),
    dict(id="143_scan029-auditC-N7", text="Four inherited guide rows used bracketed editorial descriptions instead of literal witness excerpts. The audit supplies exact C/H snippets for rows 65–68 without changing their drawing readings or adding differences. Pencil 15 and 28 remain assigned to an unnamed pencil hand."),
]

hand_log = [
    dict(habit="Full and reduced xi in one notation", pages=[KEY], places="map (1), following prose, maps (2) and (2 bis)", scope="All four local occurrences inspected; later undotted stems have short top turns and lower returns.", misreadings="The accepted j-first alternatives in the last two maps are resolved to xi at medium using the local full forms and main's supplied shared-hand comparison; no other page was viewed by C."),
    dict(habit="Flat-capped pi with straighter legs", pages=[KEY], places="all three domain pi signs, all three inner group graphs, the prose pi and diagonal pi", scope="Every local occurrence checked; cap width and scale alone do not establish case.", misreadings="Resolve all three inner graphs as pi, medium. This restores C/H in maps (1)/(2), and changes C's Pi in (2 bis) while agreeing with H's group letter."),
    dict(habit="Thin earlier letter under heavy M", pages=[KEY], places="opening declaration and map (1)", scope="Both overwritten graphs separately inspected.", misreadings="Prior cap and curved return remain T-like but uncertain, not supplied from the modular role."),
    dict(habit="Full-height basepoint outside low indices", pages=[KEY], places="all three map domains", scope="Every g,nu pair, semicolon and following basepoint checked independently.", misreadings="H's three M subscripts include xi, although each source basepoint rises to the main-letter line."),
    dict(habit="Genus g/0 loop ambiguity", pages=[KEY], places="de genre after the field insertion", scope="One unresolved local graph.", misreadings="Small upper compartment favors g above a long oval; retain g|0, low, and count preferred g against C's preferred 0 materially."),
    dict(habit="Plain X forms with distinct upper marks", pages=[KEY], places="first display, tuple, second display, final display", scope="All four local X occurrences and their upper space checked.", misreadings="Centered bar only in map (1), no bar in map (2), an pair in (2 bis); no automatic mathfrak conversion or restored missing bar."),
    dict(habit="Baseline lac and separately raised circles", pages=[KEY], places="three Autextlac operators", scope="All three inspected, with circle counts one/two/two.", misreadings="H's subscript lac is a placement difference, not supported by the manuscript baseline."),
    dict(habit="Single continuation shafts and local commas", pages=[KEY], places="four puncture lists", scope="Each list checked independently.", misreadings="Every ellipsis becomes one shaft; only the first map has commas on both sides. Tuple and later maps lack the final comma."),
    dict(habit="Reduced à versus literal point pairs", pages=[KEY], places="after associé, both diagonal colons, after structure", scope="Each local mark checked.", misreadings="Only the associated-clause mark remains à|:. The three literal colons are not normalized into accented words."),
    dict(habit="Single underline between stacked words", pages=[KEY], places="stricts above marginal orientés", scope="One rule in existing crop.", misreadings="Do not give both words the same underline; keep the small orientés reading provisional."),
    dict(habit="Physical insertion guides distinct from punctuation", pages=[KEY], places="sur Q, relatives, parenthesized sur Qbar, membership insertion", scope="All four visible guide strokes checked against explicit TikZ.", misreadings="Guide curves do not become prose parentheses or arrowheads; the membership curve does not open L'exposant as an aside."),
    dict(habit="Short brace and compact crossed symbolic residue", pages=[KEY], places="(2 bis)", scope="Both endpoints, cusp, residual stems, equality and T label checked in the existing last-formula crop.", misreadings="No full-expression brace normalization and no illegible formula-symbol placeholder; residual graph is drawn under uncertainty in deleted state."),
    dict(habit="Pencil digits without identifying signature", pages=[KEY], places="15 top right, 28 bottom left", scope="Both examined in whole/native views.", misreadings="H's author attribution is not inherited; hand remains unnamed."),
]

confirmed = [
    "Original once, native half1 once and half2 once, read line by line; no new all-page or enlarged-half image.",
    "Live title, circled item number, both independent underlines and both unnamed-pencil page numbers.",
    "All opening words, exceptions, cancelled/overwritten material, accents, short forms and punctuation, including witness agreements.",
    "Three displayed arrows and the tuple arrow, their heads/directions, all individual low indices, exterior basepoint heights, X/M/Q bars, analytic superscripts and circle counts.",
    "All four insertion texts and four separately drawn guide strokes, the underlined stricts, marginal Aut. word and their physical attachments.",
    "Complete diagonal marginal block, two colons, S_nu and pi_1, question marks, written case and four terminal points.",
    "Four puncture-list shafts and their nonuniform comma patterns; no dots or extra comma added by convention.",
    "Final short brace, crossed compact graph, equality, T_{g,nu} label and incomplete bottom sentence.",
    "All 13 original packet MARKS; 68 inherited collation rows; all 50 packet raw differences; all 30 inventory elements; all 55 separately listed physical-index entries.",
]

material_rows = [r for r in collation if r["material_after_audit"]] + [restored_genus]
report = dict(
    key=KEY, reader="C", stage="second reading", first_reader="A",
    image_views=["original", "half1", "half2"],
    image_view_details=[
        dict(view="original", path=PACKET["image"], count=1),
        dict(view="half1", path=PACKET["halves"][0], native_box=PACKET["half_boxes"][0], count=1),
        dict(view="half2", path=PACKET["halves"][1], native_box=PACKET["half_boxes"][1], count=1),
    ],
    existing_crop_views=[dict(path=crop(s), native_box=BOXES[s], count=1,
                              rotation_degrees=(-45 if s == "A_diagonal_margin" else 0)) for s in VIEW_ORDER],
    new_crops=[], findings=findings, confirmed=confirmed,
    collation_confirmation=collation,
    existing_difference_updates=existing_difference_updates,
    restored_material_rows=[restored_genus],
    certainty_resolution_dispositions=certainty_dispositions,
    raw_difference_checks=raw_difference_checks,
    decisions=decisions,
    mark_confirmations=[dict(id=d["id"], status=d["audit_status"], reading=d["reading"], confidence=d["confidence"], evidence=d["ink"]) for d in decisions],
    inventory_confirmation=inventory_confirmation, inventory_additions=[], inventory_updates=inventory_updates,
    physical_indices=physical_indices, physical_index_updates=physical_index_updates,
    remaining_doubts=remaining, doubt_dispositions=doubt_disposition,
    existing_note_updates=existing_note_updates, notes=notes,
    notation_updates=[
        dict(accepted_form=r"\xi;\ \unsure{j|\xi}", form=r"\xi", confidence="medium",
             evidence="All four local occurrences checked: two full looped forms and two reduced undotted stems. Main's supplied shared comparison settles the ambiguous reduced graphs; no contrary dotted j is established."),
        dict(form=r"\pi_1", confidence="medium", scope="all three inner groups, alongside the already pi domain/prose/marginal occurrences",
             evidence="All local flat-capped graphs checked; the observed size/retracing variations do not demonstrate a capital/lowercase contrast."),
        dict(form=r"\mathcal T_{g,\nu}", confidence="medium", status="unchanged rendering convention", evidence="The looped capital below the last brace retains the distinct modular/Teichmüller T convention; no font-only material row."),
        dict(form="cancelled compact residual graph", confidence="low", status="unidentified but drawn", evidence="Two rising stems with low/angled returns survive at the brace crossing above equality; no prose-word classification is secured."),
    ],
    check_events=[
        dict(statement_id="143_scan029-N1", who="Reader C", type="carried as background without fault found", outcome="Read the definition and exceptional integer pairs for transcription; no proof or numerical check performed in this audit."),
        dict(statement_id="143_scan029-N2", who="Reader C", type="carried as background without fault found", outcome="Read the displayed map and nonexchange claim; no construction/proof checked and no mathematical genus value supplied to the doubtful graph."),
        dict(statement_id="143_scan029-N3", who="Reader C", type="carried as background without fault found", outcome="Read the entire marginal query; no commutation condition proved. S_nu identification is inherited from main's supplied comparison and locally verified as matching the looped graph."),
        dict(statement_id="143_scan029-N4", who="Reader C", type="carried as background without fault found", outcome="Tate/Teichmüller statements and incomplete final claim carried as background. Physical notation, brace and symbolic residue checked without mathematical completion."),
    ],
    inherited_check_event_attribution=dict(statement_id="143_scan029-N6", performed_by="main reader as recorded in the accepted report", audit_reader_performed=False, disposition="Keep the prior targeted integer proof attribution; do not count it as a new Reader C check."),
    hand_log=hand_log,
    workflow=dict(assigned_page_only=True, original_views=1, native_half_views=dict(half1=1, half2=1),
                  reused_existing_crops=len(VIEW_ORDER), new_crops=0, recrops=0,
                  no_OCR=True, no_external_research=True, no_TeX_compilation=True,
                  shared_guidance_read=["reader_packets/audit_contract.md", "reader_packets/reading_guidelines.md", "notation.md", "workflow/audit_focus_notes.md"],
                  other_page_images_viewed=False, accepted_files_edited=False),
    accepted_input_hashes=dict(tex_sha256=sha256(accepted_bytes).hexdigest(), report_sha256=sha256(report_bytes).hexdigest()),
    counts=dict(original_marks=13, findings=len(findings), candidate_text_changes=6, metadata_only_findings=1,
                inherited_collation_rows=68, inherited_raw_differences=50, inventory_checked=30,
                physical_index_entries_checked=55, existing_crops_reused=12, new_crops=0,
                prior_doubts=16, removed_doubts=5, added_doubts=1, remaining_doubts=len(remaining),
                proposed_material_rows=len(material_rows),
                proposed_against_C=sum(bool(r["against_C"]) for r in material_rows),
                proposed_against_H=sum(bool(r["against_H"]) for r in material_rows)),
    created_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
)


def control_sequence_safe_braces(text):
    """Lex backslash control symbols so escaped braces and \\ do not nest."""
    depth = 0
    i = 0
    while i < len(text):
        c = text[i]
        if c == "%":
            end = text.find("\n", i)
            i = len(text) if end < 0 else end + 1
            continue
        if c == "\\":
            i += 1
            if i < len(text) and (text[i].isalpha() or text[i] == "@"):
                while i < len(text) and (text[i].isalpha() or text[i] == "@"):
                    i += 1
            else:
                i += 1
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            assert depth >= 0, "negative brace depth"
        i += 1
    assert depth == 0, ("unbalanced braces", depth)


assert set(d["id"] for d in decisions) == set(m["id"] for m in PACKET["marks"])
assert len(decisions) == len(set(d["id"] for d in decisions)) == 13
for row in findings + collation + [restored_genus]:
    for w in ("C", "H"):
        assert row[w] == "[no witness]" or row[w] in PACKET["witness_" + w], (row.get("place"), w, row[w])
for f in findings:
    assert f["before"] in accepted
    assert f["after"] in candidate
    assert (ROOT / f["crop"]).exists()
for s in VIEW_ORDER:
    assert (ROOT / crop(s)).exists()
assert r"\illegible" not in candidate, "no unreadable formula-symbol placeholder permitted"
assert r"\unsure{j|\xi}" not in candidate
assert r"\unsure{\Pi|\pi}" not in candidate
assert candidate.count(r"\unsure{g|0}") == 1
control_sequence_safe_braces(candidate)
env_stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", candidate):
    action, name = match.groups()
    if action == "begin":
        env_stack.append(name)
    else:
        assert env_stack and env_stack.pop() == name, "environment mismatch"
assert not env_stack
assert ACCEPTED_PATH.read_bytes() == accepted_bytes
assert REPORT_PATH.read_bytes() == report_bytes
assert len(remaining) == 12
assert len(material_rows) == 67
report["validation"] = dict(
    literal_C_H_excerpts=True, all_finding_before_after_substrings=True,
    original_MARK_ids_complete_and_unique=True, crop_paths_exist=True,
    static_braces_and_environments_balanced=True, no_illegible_formula_placeholder=True,
    accepted_tex_unchanged=True, accepted_report_unchanged=True,
    no_compilation=True,
)
(ROOT / "reviews" / f"{KEY}_auditC.tex").write_text(candidate)
(ROOT / "reviews" / f"{KEY}_auditC.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(dict(key=KEY, files=[f"reviews/{KEY}_auditC.tex", f"reviews/{KEY}_auditC.json"],
                      counts=report["counts"], validation=report["validation"]), ensure_ascii=False))
