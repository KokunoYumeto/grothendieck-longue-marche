"""Build draft scan-071 records from explicit root decisions, without reading images.

Inputs are the finalized root page, exact witness excerpts, and preserved reader
returns. Only decisions/156-4_071.json is written. No mathematical validation,
OCR, compilation, finalization, or consolidated-file rebuild is performed.
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re

O = Path(__file__).resolve().parents[1]
KEY = "156-4_071"
PACKET = O.parent / "page_packets" / KEY
FILENAME = "J156-4-09_156-4_scan071.tex"
C = (PACKET / "C.tex").read_text()
H = (PACKET / "H.tex").read_text()
T = (O / "pages" / FILENAME).read_text()
META = json.loads((PACKET / "metadata.json").read_text())
R = {n: json.loads((O / "readers" / KEY / n / "report.json").read_text())
     for n in ("R1", "R2", "R3")}
RT = {n: (O / "readers" / KEY / n / "reading.tex").read_text() for n in R}
DX = {n: {x["id"]: x for x in R[n]["differences"]} for n in R}


def macro(text, name, start=0):
    """Return one exact balanced macro excerpt; no TeX evaluation."""
    a = text.index("\\" + name + "{", start)
    i = a + len(name) + 2
    depth = 1
    while depth:
        if i >= len(text):
            raise ValueError("Unclosed macro excerpt")
        slash = 0
        j = i - 1
        while j >= 0 and text[j] == "\\":
            slash += 1
            j -= 1
        if slash % 2 == 0:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
        i += 1
    return text[a:i]


def line_starting(prefix):
    return next(s for s in T.splitlines() if s.startswith(prefix))


G = {k: macro(T, "figure", T.index("% " + k)) for k in ("G1", "G2", "G3", "G4", "G5")}
GREF = {k: line_starting("% " + k) for k in G}
PUNCT = macro(T, "unsure", T.index("{12.05") if "{12.05" in T else T.index("(12.05,-1.16)"))
FOLIO = r"\mspage{5\rlap{\deleted{\unsure{4|3}}}5}"
PHI = r"\unsure{\rlap{\ensuremath{\deleted{\mathcal F}}}\Phi|\rlap{\ensuremath{\deleted{F}}}\Phi|\Phi}"
DE = r"\unsure{\deleted{de}|de}"
INSERTED_F = r"\unsure{F|\mathcal F}"
REFERENCE = r"\unsure{pg|page|pge}"
CAP = r"\mathrel{\vdash\joinrel\dashv}"
INNER = r"\deleted{\unsure{ses|son}} \deleted{\unsure{p|par}}"
ARM = r"\draw (5.32,-0.04) .. controls (5.85,0.13) and (6.75,0.31) .. (7.08,0.54);"
ITOU_MARK = r"\draw (1.91,0.33)--(1.96,0.49)--(2.03,0.38);"
HIGH_POINT = r"\fill (1046,970) circle (2.0);"
LOW_POINTS = "\\fill (1663,972) circle (1.7);\n\\fill (1675,979) circle (1.7);"
for s in (FOLIO, PHI, DE, INSERTED_F, REFERENCE, CAP, INNER, ARM, ITOU_MARK, HIGH_POINT, LOW_POINTS):
    assert s in T, "Root text changed: " + s
assert "même support.\n\n\\unsure{Donnons nous}" in T

# This is the complete root-viewed evidence allowlist, not every reader crop.
ALLOWED_PREFIXES = {
    "R1": set(range(1, 15)),
    "R2": {2, 3, 10, 16, 19},
    "R3": {5, 7, 8, 16},
}
E = {}
for reader, numbers in ALLOWED_PREFIXES.items():
    for crop in R[reader]["crops"]:
        number = int(Path(crop["path"]).name[:2])
        if number not in numbers:
            continue
        value = deepcopy(crop)
        value["path"] = str(Path(crop["path"]).relative_to(O))
        E[reader.lower() + "_" + f"{number:02d}"] = value
for crop in json.loads((O / "crops" / KEY / "manifest.json").read_text()):
    tag = Path(crop["path"]).name[:3]
    if tag in {"a01", "a02", "a03"}:
        E[tag] = deepcopy(crop)
assert len(E) == 26, (len(E), sorted(E))
assert all((O / x["path"]).exists() for x in E.values())


def evidence(row, key):
    crop = E[key]
    row.update(crop=crop["path"], bbox=crop["bbox"], bbox_image=crop["source"],
               evidence_basis="Root viewed this existing crop or made and viewed this root crop.")


# R1's 47 semantic/occurrence loci are retained as the starting granularity.
D = deepcopy(R["R1"]["differences"])
for i, row in enumerate(D, 1):
    row["id"] = f"071-D{i:02d}"
    row["reader_source_ids"] = {"R1": [f"R1-D{i:02d}"]}
    row["decision"] = "Root retains the indicated reading from the local crop."
    row.pop("source", None)

EV = {
    1:"r1_01",2:"r1_01",3:"r1_02",4:"r1_02",5:"r1_03",6:"r2_03",
    7:"r1_04",8:"r1_04",9:"a03",10:"r3_05",11:"r1_06",12:"a01",
    13:"r1_06",14:"r3_07",15:"r1_06",16:"a02",17:"r3_08",18:"r1_08",
    19:"r3_08",20:"r3_08",21:"r3_08",22:"r2_10",23:"r1_13",24:"r1_09",
    25:"r1_09",26:"r1_14",27:"r1_10",28:"r1_10",29:"r1_10",30:"r1_10",
    31:"r1_10",32:"r1_10",33:"r1_10",34:"r2_16",35:"r1_11",36:"r1_11",
    37:"r1_11",38:"r1_11",39:"r1_12",40:"r1_12",41:"r1_11",42:"r1_11",
    43:"r1_12",44:"r1_12",45:"r1_12",46:"r2_19",47:"r1_14",
}
for i, row in enumerate(D, 1):
    evidence(row, EV[i])


def amend(number, **fields):
    D[number - 1].update(fields)


amend(1, marked_in_h="yes",
      h_excerpt_type="Exact H folio plus editorial surcharge note; the note is not manuscript text.",
      decision="Retain both digit-layer uncertainties; H explicitly qualifies its folio as overwritten.")
amend(5, reading=GREF["G1"],
      scope_note="G1's two margin-mark groups only; its neighbouring condition text is collated at D06.")
condition_c = next(s for s in C.splitlines() if s.startswith("Une autre façon"))
condition_h = next(s for s in H.splitlines() if s.startswith("Une autre façon"))
condition_a = G["G1"].index("Une autre façon")
condition_t = G["G1"][condition_a:G["G1"].index("};", condition_a)]
amend(6, c=condition_c, h=condition_h, reading=condition_t,
      scope_note="Punctuation of the condition only; final is an exact G1 text-node excerpt.")
amend(7, c="de", h=r"\struck{de}", reading=DE, change_c=True, change_h=True,
      confidence="low", location="corollary, state of de beneath the raised phrase",
      scan_shows="The long oblique stroke crosses de and continues beneath the addition; the same stroke can be cancellation or an insertion arm.",
      decision="Preserve one de position with deleted/live alternatives, deleted first.",
      scope_note="State of de only. Inserted-F alphabet is D08; the distinct long arm is D48.")
amend(9, scan_shows="The F after objet G has a distinct upper loop, returning left shoulder, long curved stem and midcrossbar.",
      decision="Calligraphic F is confirmed locally by root crop a03; this is separate from the uncertain raised F.")
amend(10, reading="seult", change_c=True, confidence="medium",
      scan_shows="The compressed run after l leads to an ascending final t; the separate R3/05 view supports the contraction seult.",
      decision="Resolve seult at medium confidence; do not expand the contraction.")
amend(11, change_h=False,
      decision="Resolve C's bowed-sign alternative to preceq. H's preccurlyeq is an equivalent encoding here; no H difference is counted.",
      consequence="The second order sign is distinguished from C's alternative sloping inequality; no mathematical claim is checked.")
amend(12, scan_shows="Root a01 fully frames ce qu'on appelle, including the two tall looped l strokes and terminal e run.",
      decision="The complete phrase supplies H's two adjacent unreadable placeholders once.")
amend(14, decision="Retain uncertain itou; do not add itout. The detached high mark is separately preserved and collated at D49.")
amend(16, scan_shows="Root a02 shows a horizontal cancellation through toute and live partie immediately following it.")
amend(22, reading=PUNCT, kind="drawing or diagram",
      scan_shows="The comma-like stroke, tall closing curve, hooked loop and short arm meet the right sheet edge; their character identities are unresolved.",
      decision="Preserve the entire group as the exact doubt-marked G4 drawing.",
      scope_note="Only the punctuation immediately after leq; no neighbouring text is counted again.")
amend(23, reading="cf " + REFERENCE + " $67$",
      scan_shows="Root's view of R1/13 shows a p-like arch/downstroke, a separately looped descending g-like form and a reduced ending; a full page spelling is not established.",
      decision="Retain pg/page/pge, pg first, without expanding from the reference's meaning.")
amend(26, reading=FOLIO, marked_in_h="yes",
      h_excerpt_type="Exact H editorial note; this row compares only its folio 55 and unspecified surcharge.",
      scan_shows="The inverted folio occupies two positions: a clear first 5 and a later second 5 over 4/3-like strokes. The broad cancellation strokes start below it.",
      decision="Use an overprint in the second position and remove the broad folio deletion; retain the older-digit doubt.",
      scope_note="Folio identity, two-position overprint and its cancellation state only. Draft-boundary geometry is D47.",
      supporting_crops=[E["r1_10"]["path"]])
amend(27, reading=PHI,
      scan_shows="The surviving Phi and F-like bars share one heavily worked position; a complete earlier F cannot be independently separated from retracing.",
      decision="Keep joint alternatives for Phi over calligraphic F, Phi over plain F, and a retraced Phi alone; overprint candidates occupy the same position.")
amend(34, reading="d'inclusion,", change_c=False, confidence="medium",
      scan_shows="R2/16 frames the terminal hooked comma that was incompletely framed in R1/11.",
      decision="Resolve the inclusion comma at medium confidence; the clipped R1 framing is not used as evidence of absence.")
amend(42, reading=CAP, change_c=True, confidence="high",
      scan_shows="The application-like horizontal has a short upright at each end; the right terminal has no pointed arrowhead.",
      decision="Resolve the capped horizontal from its terminals; the application context supplies no arrowhead.",
      consequence="The final glyph preserves the capped horizontal rather than H's mapsto; no bijection assertion is validated.")
amend(45, reading=INNER,
      decision="Retain two separately cancelled groups, ses/son and p/par. H's one internal unreadable placeholder covers the pair once.",
      scope_note="Only the two internal deleted groups; the adjacent high and low points are D50 and D51.")
amend(46, reading="Dém", confidence="medium",
      scan_shows="R2/19 shows a D loop, a raised accent and low m humps, with no separate terminal point.",
      decision="Resolve Dém at medium confidence and retain the absence of H's stop.")
amend(47, reading=GREF["G5"],
      h_excerpt_type="Exact H editorial description; only the boundary, orientation and long cancellation geometry are compared.",
      scan_shows="R1/14 shows the open continuous boundary and thirteen separate curved or oblique cancellation strokes across or beside the inverted text block.",
      decision="G5 reproduces the boundary, thirteen cancellation strokes and inverted relative placement with each text label once.",
      scope_note="Graphic boundary, long cancellation strokes and inversion only. Folio, text, paragraph starts and three detached points have separate rows.")

# Compact, locus-specific reader readings; source IDs retain traceability to full reports.
R2MAP = [1,2,3,4,5,[6,7],8,10,10,11,12,13,14,15,10,17,10,10,10,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,34,34,34,34,34,30,35,30,28,36,[37,38],25]
R3MAP = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,18,18,19,None,20,21,22,23,26,27,28,29,30,31,32,33,34,35,35,36,36,43,43,35,36,37,38,39,42,25]


def source_reading(reader, number):
    if number is None:
        return "saturée"
    numbers = number if isinstance(number, list) else [number]
    prefix = "R2-" if reader == "R2" else "D"
    ids = [prefix + f"{n:02d}" for n in numbers]
    return " / ".join(DX[reader][i]["reading"] for i in ids)


def short_reading(value):
    if len(value) > 300:
        if "Figure L" in value:
            return next(s for s in value.splitlines() if "Figure L" in s)
        if "R2-right-punctuation" in value:
            return "R2-right-punctuation: doubtful drawing"
        if r"\begin{tikzpicture}" in value:
            return "Explicit TikZ excerpt in the cited reader report."
    return value


for i, row in enumerate(D, 1):
    vals = {"R1": R["R1"]["differences"][i-1]["reading"],
            "R2": source_reading("R2", R2MAP[i-1]),
            "R3": source_reading("R3", R3MAP[i-1])}
    for reader, mapping in (("R2", R2MAP[i-1]), ("R3", R3MAP[i-1])):
        if mapping is not None:
            numbers = mapping if isinstance(mapping, list) else [mapping]
            prefix = "R2-" if reader == "R2" else "D"
            row["reader_source_ids"][reader] = [prefix + f"{n:02d}" for n in numbers]
    # A grouped report may be narrowed to the occurrence that this row compares.
    if i in (8,9,15,17,18,19):
        vals["R2"] = r"\mathcal F"
    if i in (9,15,17,18,19):
        vals["R3"] = r"\mathcal F"
    if i in (13,16,25):
        vals["R2"] = vals["R3"] = R["R1"]["differences"][i-1]["reading"]
    if i in (29,44):
        vals["R2"] = vals["R3"] = "ens" if i == 29 else "l'ens"
    if i in (31,41,43):
        vals["R2"] = vals["R3"] = "M"
    if i in (35,36,37,38,39,40):
        vals["R2"] = vals["R3"] = "x" if i in (36,37) else "A_x"
    if i == 42:
        vals["R2"] = vals["R3"] = CAP
    if i == 47:
        vals["R1"] = "Inverted group with boundary and thirteen cancellation strokes."
        vals["R2"] = "Inverted group with boundary and separately drawn cancellations."
        vals["R3"] = "Figure L4 separator; cancellation represented by ordinary deleted macros."
    row["reader_readings"] = vals
    row["readers"] = "; ".join(n + ": " + short_reading(v) for n,v in vals.items())


def add(location, c, h, reading, crop, shows, decision, kind="drawing or diagram",
        change_c=True, change_h=True, marked="no", confidence="high",
        reader_readings=None, **extra):
    row = dict(id=f"071-D{len(D)+1:02d}", location=location, c=c, h=h,
               reading=reading, scan_shows=shows, confidence=confidence, kind=kind,
               marked_in_h=marked, change_c=change_c, change_h=change_h,
               math_consequential=False, decision=decision)
    evidence(row, crop)
    vals = reader_readings or {n:"No separate report row at this narrow scope." for n in R}
    row["reader_readings"] = vals
    row["readers"] = "; ".join(n + ": " + v for n,v in vals.items())
    row.update(extra)
    D.append(row)


add("corollary, distinct long insertion/cancellation arm", "", "", ARM, "r1_04",
    "A long rising curved arm extends beyond the baseline de beneath the raised phrase.",
    "Preserve the arm in G2 while leaving de's cancellation state uncertain.",
    reader_readings={"R1":"Ordinary deletion and a prose comment; no distinct arm drawing.",
                     "R2":"Distinct arm drawn in R2-corollary-correction.",
                     "R3":"Distinct arm drawn in Figure L2."},
    scope_note="The arm alone; the labels and de state are excluded.")
add("Donc itou, detached high final stroke", "", "", ITOU_MARK, "r3_07",
    "A light caret-like stroke is detached above the final edge of the worked word.",
    "Preserve the stroke in G3 without assigning an accent, extra t, or word function.",
    reader_readings={"R1":"High tick noted within uncertain itou; not drawn separately.",
                     "R2":"High stroke drawn; itout also offered.",
                     "R3":"High terminal stroke noted within uncertain itou."},
    scope_note="The detached stroke alone; the word is D14.")
add("inverted draft, one high point after the second internal deletion", "", "", HIGH_POINT, "r3_16",
    "One detached point stands above and just beyond the second inner cancelled group.",
    "Preserve the point at its relative location in G5 with no assigned function.",
    reader_readings={"R1":"Not separately drawn.","R2":"Not separately drawn.","R3":"Figure L5 high point."},
    scope_note="One point only; internal words and the two low points are excluded.")
add("inverted draft, two low points beneath irréductibles", "", "", LOW_POINTS, "r1_12",
    "Two detached low points lie beneath irréductibles; the second is lower.",
    "Preserve the two points at their relative positions in G5 without turning them into punctuation.",
    reader_readings={"R1":"Not separately drawn.","R2":"Not separately drawn.","R3":"Figure L5 two low points."},
    scope_note="The two low points only; adjacent words and the high point are excluded.")

# Paragraph scopes are deliberately separate from the word and graphic rows.
layout_vals = {"R1":"Retains C's paragraph division.",
               "R2":"Retains C's division/relative block starts.",
               "R3":"Retains C's paragraph division."}
add("paragraph boundary before Donnons nous",
    "même support.\n\n\\unsure{Donnons nous} un support.",
    "même support. Donc \\ill{} un support.",
    "même support.\n\n\\unsure{Donnons nous} un support.", "r2_02",
    "Donnons nous is retained as C's separate paragraph; the physical line at a common left edge does not establish that C's division should be removed.",
    "Keep the C/all-reader paragraph division. Count only H's paragraph joining here.",
    kind="insertion or placement", change_c=False, confidence="medium",
    reader_readings=layout_vals,
    scope_note="Paragraph boundary only. Donnons/nous and H's unreadable placeholder are D04.")
add("paragraph boundary before Donc itou", ".\n\nDonc", ". Donc", GREF["G3"], "r3_07",
    "The Donc statement begins the separate block retained by C and the three readers.",
    "Retain that block start as G3; compare only H's paragraph joining.",
    kind="insertion or placement", change_c=False, reader_readings=layout_vals,
    scope_note="Paragraph boundary only; the exact final reference is G3, whose word and high mark have separate rows.")
add("paragraph boundary before En d'autres termes",
    ".\n\nEn d'autres termes,", ". En d'autres termes,", GREF["G4"], "a02",
    "The restatement begins the separate block retained by C and the three readers.",
    "Retain that block start as G4; compare only H's paragraph joining.",
    kind="insertion or placement", change_c=False, reader_readings=layout_vals,
    scope_note="Paragraph boundary only; G4 text and punctuation are separately collated.")
alors_node = next(s for s in T.splitlines() if r"{\deleted{Alors" in s)
dem_node = next(s for s in T.splitlines() if r"{\deleted{Dém" in s)
add("inverted draft, block start before Alors", ".}\n\n\\deleted{Alors",
    "(\\ill{}). Alors", alors_node, "r1_14",
    "Alors begins the next inverted block in C and the readers' paragraph/relative-position encodings.",
    "Preserve the corresponding G5 block start; compare only H's paragraph joining.",
    kind="insertion or placement", change_c=False, reader_readings=layout_vals,
    scope_note="Block/paragraph placement only; final is the exact Alors node, whose labels are not counted again.")
add("inverted draft, block start before Dém",
    "$\\Phi$.}\n\n\\deleted{\\unsure{Dém|Dire|Bien}", "$\\Phi$. Dém.",
    dem_node, "r1_14",
    "Dém begins the final indented block in C and the readers' paragraph/relative-position encodings.",
    "Preserve the corresponding G5 start; compare only H's paragraph joining.",
    kind="insertion or placement", change_c=False, reader_readings=layout_vals,
    scope_note="Block/paragraph placement only; final is the exact Dém node, whose lettering and stop are D46.")

# Preserve R3's explicit context-row mapping while applying the root decisions.
CD = deepcopy(R["R3"]["c_doubts"])
CD_E = {1:"r1_01",2:"r1_01",3:"r1_02",4:"r1_03",5:"r1_03",6:"r3_05",
        7:"r1_06",8:"r1_06",9:"r3_07",10:"r2_10",11:"r1_09",12:"r1_09",
        13:"r1_14",14:"r1_10",15:"r1_10",16:"r1_10",17:"r1_10",18:"r1_10",
        19:"r1_11",20:"r1_12",21:"r1_12",22:"r2_19",23:"r1_01",24:"r3_05",
        25:"r1_04",26:"r1_06",27:"r1_12",28:"a02",29:"r2_16"}
for i,row in enumerate(CD,1):
    row["id"] = f"071-C{i:02d}"
    evidence(row, CD_E[i])
    row.pop("source", None)


def cd(number, **fields):
    CD[number-1].update(fields)


cd(4, reading=GREF["G1"], scan_shows="The left segmented column and its offset low point are drawn literally; function remains unassigned.")
cd(5, reading=GREF["G1"], scan_shows="The second segmented column stands higher; its separate fragments are retained without a punctuation identity.")
cd(6, reading="seult", status="resolved",
   scan_shows="R3/05 supports the contracted run seult; root resolves it at medium confidence.")
cd(9, reading=r"\unsure{itou}", status="retained",
   scan_shows="The middle is retraced; the separate high stroke is drawn in G3 without supplying a final t.")
cd(10, reading=PUNCT, status="revised",
   scan_shows="The full comma/closing-curve/loop/arm group is drawn under a doubt mark at the edge.")
cd(13, c=r"\mspage{\deleted{\unsure{5\deleted{\unsure{4|3}}5}}}",
   reading=FOLIO, status="revised",
   location="Inverted folio, surface digits, overprint placement and broad cancellation state",
   scan_shows="Two surface positions read 55; the second overlays 4/3. Broad cancellation strokes begin beneath the folio.")
cd(15, c=r"\deleted{\unsure{\mathcal F|F}}\Phi", reading=PHI, status="revised",
   scan_shows="A prior F-like layer is possible but inseparable from retracing; the alternatives remain in one overprinted position.")
cd(19, reading=CAP, status="resolved",
   scan_shows="The shaft has two terminal uprights, without a pointed right head.")
cd(21, reading=r"\unsure{p|par}", status="revised",
   scan_shows="The p descender and shoulder are clearer than the struck continuation.")
cd(22, reading="Dém", status="resolved",
   scan_shows="R2/19 shows the D loop, raised accent and low m; root resolves Dém at medium confidence, without a stop.")
cd(23, c="$=$", reading="$=$",
   scan_shows="Both opening positions have paired horizontal strokes; the first is framed by R1/01 and the second by R1/02.",
   supporting_crops=[E["r1_02"]["path"]])
cd(25, reading=INSERTED_F, status="revised",
   scan_shows="The small raised F is angular and lacks a securely closed upper loop; later looped family-F occurrences are independent.")
cd(29, c=r"$\Phi$, muni", reading=r"$\Phi$, muni",
   scan_shows="The end of muni has the narrow i position without a separate final e.")


def remaining(location, reading, alternatives, confidence, reason):
    return dict(location=location, reading=reading, alternatives=alternatives,
                confidence=confidence, reason=reason)


RD = [
    remaining("running folio, underlying number",r"\unsure{69|79}",["69","79"],"low","Overlaid digit strokes and the extreme clipped upper edge do not separate the older layer."),
    remaining("running folio, surface number",r"\unsure{70|79}",["70","79"],"low","The loop and surviving descending stroke leave the last digit open."),
    remaining("Donnons nous",r"\unsure{Donnons nous}",["Donnons nous"],"medium","The reduced medial groups remain uncertain; no hyphen is supplied."),
    remaining("margin columns, function",GREF["G1"],["exclamation-like marks","vertical fragments","incidental marks"],"low","Their literal shapes are drawn; function and authorship are not assigned."),
    remaining("corollary de, cancellation state",DE,[r"\deleted{de}","de"],"low","One long stroke can be cancellation or a crossing insertion arm."),
    remaining("capital in raised dans phrase",INSERTED_F,["F",r"\mathcal F"],"low","The raised form has no securely closed upper loop; later occurrences are locally clear."),
    remaining("first sous-contrée",r"\unsure{contrée|contrie}",["contrée","contrie"],"medium","The short accented/dotted letter remains compressed."),
    remaining("Donc itou and high mark",r"\unsure{itou}",["itou"],"medium","The worked middle remains uncertain; the detached high stroke is separately drawn without assigning it a final t."),
    remaining("saturee/saturée",r"\unsure{saturee|saturée}",["saturee","saturée"],"low","A detached acute is not secure; a connected high return could carry it."),
    remaining("punctuation after the live order sign",PUNCT,[",) with a composite loop/arm",",);",",)}"],"low","The entire group is retained graphically; the sheet edge and overlapping returns prevent secure character segmentation."),
    remaining("reference word after cf",REFERENCE,["pg","page","pge"],"medium","A p-like group and looped descending g are visible; the intervening and terminal letters remain compressed."),
    remaining("automatic-word ending",r"\unsure{automatiquemt|automatiquement}",["automatiquemt","automatiquement"],"low","The end reduces to a joined run and rising final t."),
    remaining("cancelled loop before une",r"\deleted{\unsure{f}}",["f-like single form"],"low","The crossed tall loop is only approximately identifiable."),
    remaining("inverted folio, older second digit",r"\unsure{4|3}",["4","3"],"low","The older upper strokes are overprinted by the second surface 5."),
    remaining("inverted worked Phi, older layer",PHI,[r"\rlap{\ensuremath{\deleted{\mathcal F}}}\Phi",r"\rlap{\ensuremath{\deleted{F}}}\Phi",r"\Phi"],"low","The common worked position does not establish an independent complete earlier F."),
    remaining("inverted parenthetical",r"\unsure{(au --)|(ou --)|(en --)}",["(au --)","(ou --)","(en --)"],"low","A compressed vowel group precedes a separate dash."),
    remaining("first internal deleted group",r"\unsure{ses|son}",["ses","son"],"low","The horizontal cancellation masks the joins."),
    remaining("second internal deleted group",r"\unsure{p|par}",["p","par"],"low","The p is clearer than its struck continuation."),
]

DISPUTES = []


def dispute(location, r1, r2, r3, final, why, crop):
    DISPUTES.append(dict(location=location, r1=r1, r2=r2, r3=r3,
                         final=final, evidence=why + " [" + E[crop]["path"] + "]"))


dispute("de below the insertion",r"\deleted{de}",r"\deleted{de}",r"\unsure{de|\deleted{de}}",DE,
        "Root keeps the state open because the crossing arm is also an insertion leader.","r1_04")
dispute("raised F alphabet",INSERTED_F,r"\mathcal F",r"\unsure{\mathcal F|F}",INSERTED_F,
        "The raised small form lacks the secure upper loop found at later occurrences.","r1_04")
dispute("contracted seulement",r"\unsure{seult|seulemt}",r"\unsure{seult|seulemt}","seult","seult",
        "The separate R3/05 view supports seult at medium confidence.","r3_05")
dispute("itou and detached high stroke",r"\unsure{itou}; high tick noted",r"\unsure{itou|itout}; high stroke drawn",r"\unsure{itou}; high stroke noted",r"\unsure{itou}",
        "Root retains itou uncertain and draws the detached high stroke in G3 without treating it as a final t.","r3_07")
dispute("saturée accent",r"\unsure{saturee|saturée}",r"\unsure{saturee|saturée}","saturée",r"\unsure{saturee|saturée}",
        "The accent is not independently secure in the fully framed live-final crop.","r3_08")
dispute("crowded right-edge punctuation",r"\unsure{,)|,)\}|,) ;}","Doubt-marked TikZ group","Figure L3, identities open",PUNCT,
        "Root retains every component as the doubtful G4 drawing rather than choosing a punctuation type.","r2_10")
dispute("reference word",r"\unsure{page|pge}","page","page",REFERENCE,
        "The p-like group and looped g support pg as first candidate; the full word is unestablished.","r1_13")
old_folio = r"\mspage{\deleted{5\deleted{\unsure{4|3}}5}}"
dispute("inverted folio positions and broad cancellation state",old_folio,old_folio,old_folio,FOLIO,
        "Root supersedes all three: only two positions exist, and the broad cancellation begins below the folio.","r1_14")
dispute("worked Phi layer and same-position overprint",
        r"\unsure{\deleted{\mathcal F}\Phi|\deleted{F}\Phi|\Phi}",
        r"\unsure{\Phi|\deleted{\mathcal F}\Phi|\deleted{F}\Phi}",
        r"\deleted{\unsure{\mathcal F|F}}\Phi",PHI,
        "No complete older F is independently secure; the final alternatives use one overprinted position.","r1_10")
dispute("un after worked Phi","un",r"\unsure{un}","un","un",
        "Root retains the visible small u-curve and n-hump reading.","r1_10")
dispute("comma after inclusion",r"d'inclusion\unsure{,}; crop limitation",r"d'inclusion\unsure{,}","d'inclusion,","d'inclusion,",
        "R2/16 supplies the extent missing in R1/11; root resolves the comma at medium confidence.","r2_16")
dispute("application terminal",r"\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}",CAP,CAP,CAP,
        "Both terminal caps are retained; the expected application meaning supplies no arrowhead.","r1_11")
dispute("second internal deleted group",r"\unsure{p|par}",r"\unsure{p|par}",r"\unsure{par|p}",r"\unsure{p|par}",
        "The p is clearer than its cancelled continuation; keep both candidates with p first.","r1_12")
dispute("Dém certainty",r"\unsure{Dém}",r"\unsure{Dém|Dire}","Dém","Dém",
        "R2/19 supplies a D loop, raised accent and low m; root resolves Dém at medium confidence, without a stop.","r2_19")
dispute("long insertion/cancellation arm","No distinct drawing; ordinary deletion and comment","Arm drawn in correction figure","Arm drawn in Figure L2",ARM,
        "The distinct long arm is retained independently of the uncertain de state.","r1_04")
dispute("cancelled-draft geometry","Inverted group with boundary and thirteen cancellation strokes","Inverted group with its own drawn cancellation geometry","Separator Figure L4 and ordinary deletion macros",GREF["G5"],
        "Root adopts the continuous boundary and thirteen strokes with text labels once; the lower folio is excluded from the broad cancellation.","r1_14")
dispute("high point after the second internal deletion","Not separately drawn","Not separately drawn","Figure L5 high point",HIGH_POINT,
        "Root preserves the detached point without a linguistic function.","r3_16")
dispute("two low points beneath irréductibles","Not separately drawn","Not separately drawn","Figure L5 two low points",LOW_POINTS,
        "Root preserves both points at their relative heights without adding punctuation.","r1_12")

INV = []


def inv(element, kind, position, text, draft=False):
    INV.append(dict(element=element, kind=kind, position=position,
                    first_words_or_objects=text,
                    sheet_kind="cancelled_draft" if draft else "text",
                    hand="his hand", transcribed="yes"))


inv("running folio","text","top centre","70/79 over 69/79")
inv("older running-folio layer","deletion","top centre, under surface digits","69/79")
inv("opening paragraph","text","upper first two lines","Il revient au =")
inv("support paragraph","text","upper third line","Donnons nous un support")
inv("implication paragraph","text","upper block, G1","Une autre façon de dire")
inv("left marginal fragments","drawing","left of implication, G1","lower segmented column with offset point")
inv("right marginal fragments","drawing","beside the first column, G1","higher segmented column")
inv("corollary heading","text","left of corollary, G2","Corollaire, singly underlined")
inv("corollary body","text","middle upper block, G2","Le cosupport ... sous-contrée")
inv("raised phrase","insertion","above baseline de, G2","dans F/calligraphic F")
inv("possibly cancelled de","deletion","baseline beneath the raised phrase, G2","one de, deleted/live alternatives")
inv("long insertion/cancellation arm","drawing","through de and beneath raised phrase, G2","long curved rising arm")
inv("Donc paragraph","text","after corollary, G3","Donc itou pour toute partie")
inv("detached high itou mark","drawing","above right edge of itou, G3","short joined high stroke, function unassigned")
inv("restatement paragraph","text","last live paragraph, G4","En d'autres termes")
inv("cancelled toute","deletion","before partie, G4","toute")
inv("crowded punctuation group","drawing","right edge after leq, G4","comma-like curve, closing curve, loop and short arm")
inv("cancelled loop before une","deletion","last live line, G4","f-like single form")
inv("inverted folio","text","bottom centre in scan orientation, before G5","55 in two positions; no broad cancellation",True)
inv("overwritten second folio digit","deletion","same second position under surface 5","4/3",True)
inv("draft opening paragraph","text","first two inverted lines, G5","un ensemble, et Phi un ens",True)
inv("possible older layer beneath Phi","deletion","same position as first Phi, G5","possible calligraphic/plain F or no independent older glyph",True)
inv("draft assertion paragraph","text","middle inverted lines, G5","Alors Phi, muni ... objets irréductibles de Phi",True)
inv("first internal cancelled group","deletion","after l'ens des, G5","ses/son",True)
inv("second internal cancelled group","deletion","following the first group, G5","p/par",True)
inv("draft final paragraph","text","final inverted line, G5","Dém A_x est irréductible, car si ...",True)
inv("broad cancellation of draft text","deletion","entire G5 text block, excluding folio","un ensemble ... final union",True)
inv("continuous draft boundary","drawing","side and end of inverted text block, G5","open line with inward jog",True)
inv("thirteen long cancellation strokes","drawing","across and beside inverted text, G5","thirteen curved/oblique strokes",True)
inv("detached high point","drawing","above/right of second internal deletion, G5","one point",True)
inv("detached low points","drawing","beneath irréductibles, G5","two points at different heights",True)

LOWER_NOTE = next(s for s in H.splitlines() if s.startswith(r"\note{la moitié"))
UPPER_NOTE = next(s for s in H.splitlines() if s.startswith(r"\note{son numéro"))
REVIEWS = [
    dict(reference="H upper-folio editorial note",claim=UPPER_NOTE,
         decision="The surcharge is an explicit qualification, so D01 has marked_in_h=yes. The note is not literal manuscript text.",
         evidence="Root retains uncertain surface and underlying digits.",crop=E["r1_01"]["path"]),
    dict(reference="H lower-draft editorial note",claim=LOWER_NOTE,
         decision="Its folio/surcharge qualification is scoped at D26; its boundary/cancellation description is scoped at D47. Its prose is never counted as omitted manuscript writing.",
         evidence="The two-position folio is above the broad cancellation, while the draft has a drawn boundary and thirteen strokes.",crop=E["r1_14"]["path"]),
    dict(reference="H bowed-sign encoding",claim=r"\preccurlyeq",
         decision=r"Root confirms \preccurlyeq and \preceq as equivalent encodings of this bowed sign. D11 changes C's uncertainty only; change_h=false.",
         evidence="The selected final glyph has the bowed lower strokes. This is an encoding equivalence, not a mathematical validation.",crop=E["r1_06"]["path"]),
    dict(reference="C_context prior audit, extent of broad cancellation",
         claim="The long diagonal strokes were said to cross the whole block, including its folio.",
         decision="Superseded by root's local observation: broad strokes begin below the folio. Final folio retains only the local overwritten second digit.",
         evidence="The upper ends of the cancellation strokes sit below the two folio positions.",crop=E["r1_14"]["path"]),
    dict(reference="C_context application preference",
         claim="The application context favours mapsto.",
         decision="No head is supplied from context; the two terminal caps determine the final transcription.",
         evidence="The horizontal terminates in uprights without a pointed right head.",crop=E["r1_11"]["path"]),
]

NOTATION = [
    dict(sign="literal repetition signs",latex="=",appearance="Two unequal horizontal bars.",location="Opening, twice",alternatives=[]),
    dict(sign="raised F",latex=INSERTED_F,appearance="Angular reduced form without a secure upper loop.",location="Inserted dans phrase only",alternatives=["F",r"\mathcal F"]),
    dict(sign="later family F",latex=r"\mathcal F",appearance="Distinct looped head, returning shoulder and curved stem.",location="Five later live occurrences",alternatives=[]),
    dict(sign="order signs",latex=r"\leq;\preceq",appearance="First straight, second bowed below.",location="Corollary",alternatives=[]),
    dict(sign="Phi and inclusion",latex=r"\Phi\subset\mathcal F",appearance="Crossed oval and open inclusion.",location="Donc paragraph",alternatives=[]),
    dict(sign="worked Phi",latex=PHI,appearance="Several shared bars and oval strokes in one position.",location="Inverted opening",alternatives=["Phi over calligraphic F","Phi over plain F","retraced Phi alone"]),
    dict(sign="ambient M",latex="M",appearance="Plain two-peaked capital.",location="All three inverted occurrences",alternatives=[]),
    dict(sign="capped application-like horizontal",latex=CAP,appearance="Horizontal with an upright at each end; no pointed head.",location="Inverted application",alternatives=[]),
    dict(sign="x and union indices",latex=r"A_x;\bigcup_{i\in I} A_i",appearance="Reduced crossed x, dotted small i, barred I.",location="Inverted text and final formula",alternatives=[]),
    dict(sign="detached points",latex=HIGH_POINT+"\n"+LOW_POINTS,appearance="One high point and two low points at unequal heights.",location="G5 penultimate line",alternatives=["Function unassigned"]),
]
ABBREVIATIONS = [
    dict(form="disj.",expansion="disjoints"),
    dict(form="disj",expansion="disjoints"),
    dict(form="seult",expansion="seulement"),
    dict(form="cf",expansion="confer"),
    dict(form="pg / page / pge",expansion="page (uncertain written form; no expansion supplied in the transcription)"),
    dict(form="automatiquemt",expansion="automatiquement (abbreviated candidate)"),
    dict(form="ens",expansion="ensemble"),
    dict(form="Dém",expansion="Démonstration"),
    dict(form="au -- / ou -- / en --",expansion="Not securely established; retained without expansion"),
]

WORKFLOW = (
    "Three independent final returns under v07 are preserved unchanged. Root did not view the whole page or either original half; "
    "root successfully viewed 23 existing reader crops (all 14 R1; R2 02,03,10,16,19; R3 05,07,08,16) and made/viewed 3 root crops. "
    "The initially truncated R2/10 output was not seen and was successfully retried from the same file; it is counted once. "
    "Text-only record audit caught an uncovered later family-F occurrence, which root resolved with a03. "
    "A preliminary suspicion that Donnons should join the preceding paragraph was withdrawn after exact C comparison; "
    "the final retains C/all-reader paragraphing, and the rejected suspicion is not an ink correction. "
    "All counted differences cite root-viewed crops. No OCR, compiler, proof check, computation, or external-page research was performed for these records."
)

DECISION = dict(
    key=KEY, cote="156-4", scan=71, folder=META["folder"], their_page=META["their_page"],
    filename=FILENAME, brief_version="v07", review_status="draft — awaiting root review",
    record_builder="scripts/decide_071_records.py",
    record_basis="Explicit root decisions; exact finalized page; preserved independent reader returns.",
    final_text_sha256=hashlib.sha256(T.encode()).hexdigest(),
    differences=D, c_doubts=CD, disputes=DISPUTES, remaining_doubts=RD,
    h_placeholder_alignment=[
        dict(ordinal=1, source=r"Donc \ill{}", difference_id="071-D04",
             disposition=r"\unsure{Donnons nous}", scope="The complete two-group opening phrase, including H's Donc."),
        dict(ordinal=2, source=r"\ill{} \ill{}", difference_id="071-D12",
             disposition="ce qu'on appelle", scope="First of the adjacent pair; the pair is collated as one complete phrase."),
        dict(ordinal=3, source=r"\ill{} \ill{}", difference_id="071-D12",
             disposition="ce qu'on appelle", scope="Second of the adjacent pair; no second counted difference is created."),
        dict(ordinal=4, source=r"(\ill{})", difference_id="071-D33",
             disposition=r"\unsure{(au --)|(ou --)|(en --)}", scope="Inverted parenthetical only."),
        dict(ordinal=5, source=r"\struck{\ill{}}", difference_id="071-D45",
             disposition=INNER, scope="One H placeholder covering the two separate internal deleted groups; counted once."),
    ],
    inventory=INV, notation=NOTATION, abbreviations=ABBREVIATIONS,
    witness_reviews=REVIEWS, check_events=[],
    reader_crop_counts={n:len(R[n]["crops"]) for n in R},
    reader_report_counts={n:{k:len(R[n][k]) for k in ("differences","c_doubts","remaining_doubts","inventory")} for n in R},
    adjudicator_crop_count=3, adjudicator_existing_crop_views=23,
    adjudicator_successful_crop_views=26,
    root_viewed_crops=[E[k] for k in sorted(E)],
    workflow_note=WORKFLOW,
    administrative_audit="decisions/156-4_071_record_audit.md",
    notes=dict(
        summary="The live upright notes discuss cosupport and support, followed by a corollary and restatement. An inverted cancelled draft begins an assertion and an unfinished Dém. Five graphic groups preserve marginal marks, the insertion arm, the high itou mark, edge punctuation, and the draft's boundary/cancellations/points.",
        math_reading_decisions="Only local glyph comparisons were used: straight versus bowed order, terminal caps versus an arrowhead, and x/i/I size and placement. The apparent application or bijection meaning did not supply a missing arrowhead. No manuscript assertion was proved, computed, used as a checked result, or refuted; check_events is empty.",
        author_checks="Dém begins an unfinished proof in the cancelled draft, not an explicit completed author check. The uncertain state of de, unclosed quotation, compressed reference word and abbreviated endings are retained. Three detached points have no assigned function.",
        title_dates_pagination="No title or date. Running folio remains 70/79 over 69/79 without consulting adjacent pages. The inverted folio is 55 in two positions, with the second 5 over an uncertain 4/3; the broad draft cancellation does not cross it.",
    ),
)


def validate_records():
    """Necessary text/schema consistency only; does not examine or validate ink."""
    kinds = {"misread word","misread symbol or index","omission","text not on the page",
             "deletion state (struck given live or live given struck)","insertion or placement",
             "abbreviation expanded or spelling modernised",r"readable ink left as \ill{}",
             "drawing or diagram","other"}
    assert len(D) == 56 and len({x["id"] for x in D}) == 56
    allowed = {v["path"] for v in E.values()}
    for row in D:
        assert row["kind"] in kinds, row["id"]
        assert row["confidence"] in {"high","medium","low"}, row["id"]
        assert row["marked_in_h"] in {"yes","no"}, row["id"]
        assert all(type(row[x]) is bool for x in ("change_c","change_h","math_consequential")), row["id"]
        assert row["crop"] in allowed, row["id"]
        for key,source in (("c",C),("h",H),("reading",T)):
            assert not row[key] or row[key] in source, (row["id"],key,row[key])
    for row in CD:
        assert row["status"] in {"resolved","retained","revised"}
        assert row["reading"] in T, row["location"]
    assert set(range(1,26)) == {v for row in CD for v in row.get("context_rows",[])}, "C context coverage"
    assert len(list(re.finditer(r"\\unsure\{",C))) == 22
    assert H.count(r"\ill{}") == 5
    for row in RD:
        assert row["reading"] in T, row["location"]
    for row in INV:
        assert row["kind"] in {"text","display","diagram","drawing","margin note","insertion","deletion"}
        assert row["sheet_kind"] in {"text","reused_typed","typescript","letter","list","cancelled_draft","cover"}
        assert row["transcribed"] == "yes"
    assert all(R[n]["finished_utc"] for n in R)
    assert DECISION["check_events"] == []
    return dict(differences=len(D), changes_C=sum(x["change_c"] for x in D),
                changes_H=sum(x["change_h"] for x in D), c_doubts=len(CD),
                context_rows=25, c_unsure_occurrences=22, h_ill_placeholders=5,
                disputes=len(DISPUTES), remaining_doubts=len(RD), inventory=len(INV),
                root_existing_crop_views=23, root_new_crops=3, check_events=0)


if __name__ == "__main__":
    result = validate_records()
    DECISION["administrative_validation"] = result
    output = O / "decisions" / (KEY + ".json")
    output.write_text(json.dumps(DECISION,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(dict(output=str(output),**result),ensure_ascii=False))
