#!/usr/bin/env python3
"""Mechanical assembly only. Reads reader text/JSON; never opens an image."""
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out"
REPORTS = {x: json.loads((OUT / f"readers/004/{x}/report.json").read_text()) for x in "ABC"}
TEX = {x: (OUT / f"readers/004/{x}/reading.tex").read_text() for x in "ABC"}
ROWS = {x: {r["id"]: r for r in REPORTS[x]["differences"]} for x in "ABC"}
META = json.loads((ROOT / "packets/004/metadata.json").read_text())
AA = {int(r["id"].rsplit("-", 1)[1]): r for r in REPORTS["A"]["differences"]}

# Each named source is copied literally. Shared report rows remain shared;
# the source scope is explicit, rather than manufactured as a narrower reading.
BMAP = {
    1:1,2:2,3:3,4:4,5:16,6:20,7:22,9:23,10:25,11:26,12:27,13:32,
    15:31,16:35,21:[20,21],33:38,35:40,36:5,37:6,38:7,39:10,40:12,41:14,
    42:8,43:11,44:15,45:9,46:13,49:17,50:18,51:18,52:19,53:21,55:36,
    56:37,57:24,58:28,59:29,61:39,62:41,63:42,64:43,65:44,66:45,
    67:46,68:47,69:48,70:49,71:50,72:51,73:52,74:53,76:54,77:55,
    78:56,79:57,
}
CMAP = {
    1:"C01",2:"C02",3:"C03",4:"C04",5:"C05",6:"C06",7:"C07",8:"C07",
    9:"C08",10:"C09",11:"C10",12:"C11",13:"C12",15:"H38",
    21:["C06","H28"],33:"H01",35:"H06",36:"H10",37:"H11",38:"H12",
    39:"H15",40:"H17",41:"H19",42:"H13",43:"H16",44:"H20",45:"H14",
    46:"H18",48:"H21",49:"H25",50:"H26",51:"H26",52:"H27",53:"H28",
    54:"H30",55:"H32",56:"H33",57:"H36",58:"H39",59:"H40",61:"H42",
    62:"H03",63:"H04",64:"H05",65:"H07",66:"H08",67:"H09",68:"H22",
    69:"H23",70:"H24",71:"H31",72:"H34",73:"H35",74:"H37",76:"H43",
    77:"H44",78:"H45",79:"H46",80:"H02",81:"H29",82:"H37",83:"H41",
}

FALLBACK = {
    8: ("upper-right first case, live minus and cancelled predecessor",
        r"-\deleted{\unsure{a|0}}\eta_{i+1}"),
    14: ("below-box relation, abbreviation", r"\deg x"),
    17: ("left box first relation, first factor", r"e_i e_1&=0"),
    18: ("left box second relation, first factor", r"f_i e_1&=e_{i+1}"),
    19: ("left box first relation, second factor", r"e_i e_1&=0"),
    20: ("left box adjacent two-case relation, second factor", r"f_i f_1&="),
    22: ("below-box eta relation", r"\eta=e_{d-1}"),
    23: ("first displayed formula", r"f_{d-2}e_1&=-e_{d-2}f_1"),
    24: ("last displayed formula", r"f_{d-3}e_1."),
    25: ("left expansion first factor, lambda", r"\lambda"),
    26: ("upper-right linear combination, alpha", r"\alpha e_{i+1}+\beta f_{i+1}"),
    27: ("upper-right linear combination, beta", r"\alpha e_{i+1}+\beta f_{i+1}"),
    28: ("left top second line, delta", r"\delta(\eta)&=e_{d-2}"),
    29: ("bottom-left unfinished expression, delta", r"\delta(e_i e_j)="),
    30: ("descending chain, first vertical separator", r"\rotatebox{90}{$=$}"),
    31: ("descending chain, second vertical separator", r"\rotatebox{90}{$=$}"),
    32: ("descending chain, third vertical separator", r"\rotatebox{90}{$=$}"),
    34: ("left box, beginning of enclosing brace", "\\left\\{\\begin{aligned}\ne_i e_1&=0"),
    47: ("left expansion, both underbrackets", r"\underbrace{f_i e_1} / \underbrace{\deleted{e_i f_1}}"),
    48: ("independent e2/e3 block", r"\begin{aligned}e_2&=f_1e_1\\e_3&=f_2e_1\end{aligned}"),
    54: ("upper-right system, beginning of enclosing brace", "\\left\\{\\begin{aligned}\ne_i e_1&=0"),
    75: ("lower-right bound, complete line without comma", r"1\leq i\leq d-3\\"),
    80: ("left boxed block, range without prose lead-in", r"(1\leq i\leq d-2)\\"),
    81: ("upper-right block, range without prose lead-in", r"1\leq i\leq d-2\\"),
    82: ("lower-right bound without prose lead-in", r"1\leq i\leq d-3\\"),
    83: ("descending chain, first continuation without repeated left member", r"\rotatebox{90}{$=$}\\"),
}

def ids_for(x, n):
    m = BMAP if x == "B" else CMAP
    value = m.get(n)
    if value is None:
        return []
    value = value if isinstance(value, list) else [value]
    return [f"B004.{v:02d}" if x == "B" else v for v in value]

def exact_tex(x, context, excerpt):
    parts = excerpt.split(" / ") if context.endswith("both underbrackets") else [excerpt]
    if context == "left box adjacent two-case relation, second factor":
        # The relation shares the first aligned row, so its literal separator
        # is '=' rather than '&=' in every reader's text.
        excerpt = r"f_i f_1="
        parts = [excerpt]
    for part in parts:
        assert part in TEX[x], (x, context, part)
    return f"reading.tex ({context}; no separate report row): {excerpt}"

def reading(x, n):
    srcs = ids_for(x, n)
    if srcs:
        return " | ".join(f"{k}: {ROWS[x][k]['reading']}" for k in srcs)
    if n == 16 and x == "C":
        # Absence is stated as a source observation, never as a rejected mark.
        return "reading.tex (left box, lower cases): no paired-tick token transcribed; no report row at this locus"
    context, excerpt = FALLBACK[n]
    return exact_tex(x, context, excerpt)

def full_bbox(row):
    b = row.get("bbox")
    if not b:
        return None
    if isinstance(b, dict):
        box = list(b["xyxy"])
        if b.get("image") == "half b":
            box[0] += 1170
            box[2] += 1170
        return box
    return list(b)

def crop_path(x, name):
    if x == "root":
        return f"crops/004/{name}" if name else ""
    return f"readers/004/{x}/{name}" if name else ""

ALL_CROPS = []
for x, report in REPORTS.items():
    for c in report["crops"]:
        b = c.get("bbox")
        if isinstance(b, dict):
            b = full_bbox({"bbox":b})
        if isinstance(b, list):
            ALL_CROPS.append((x, c["path"], b))

def covers(outer, inner):
    return outer[0] <= inner[0] and outer[1] <= inner[1] and outer[2] >= inner[2] and outer[3] >= inner[3]

def choose_crop(n):
    a = AA[n]
    if a.get("readers_crop"):
        return crop_path("A", a["readers_crop"]), f"A report crop {a['readers_crop']}."
    box = full_bbox(a)
    candidates = [(x, name, b) for x, name, b in ALL_CROPS if box and covers(b, box)]
    if candidates:
        x, name, b = candidates[0]
        return crop_path(x, name), (
            f"Existing {x} crop {name} contains A's reported full-coordinate locus {box}; "
            "containment is a mechanical coordinate check, not a visual adjudication."
        )
    return "", f"ROOT CROP REQUIRED. A's reported full-coordinate locus is {box}; no retained crop fully contains it."

rows = []
used = {"A":set(), "B":set(), "C":set()}
pending_crop = []
for n, a in AA.items():
    if n == 60:
        # The report's distinction here consists of array/gathered typesetting.
        # All three actual transcriptions and the acknowledged placement remain
        # available in workflow metadata and the repeated-left-member locus.
        used["A"].add(a["id"])
        continue
    r = {k:copy.deepcopy(a[k]) for k in [
        "location","C","H","confidence","kind","diff_C","diff_H","C_doubt_status"
    ]}
    r.update(id=f"004-{n:02d}", final=a["reading"])
    r["readers"] = {"A":f"{a['id']}: {a['reading']}", "B":reading("B", n), "C":reading("C", n)}
    used["A"].add(a["id"])
    for x in "BC":
        used[x].update(ids_for(x,n))
    if n in [14,15,*range(17,33)]:
        r["C_doubt_status"] = None
    if n in [80,81,82,83]:
        r["diff_H"] = False
    cp, cp_note = choose_crop(n)
    r["crop"] = cp
    r["evidence"] = "Provisional A reading; root adjudication pending. A report: " + a["evidence"] + " " + cp_note
    r["marked_in_H"] = "no"
    if a.get("mathematical_consequence"):
        r["mathematical_consequence"] = a["mathematical_consequence"]
    if n in [80,81,82]:
        r["evidence"] += " Root directs that H's clearly descriptive orientation captions be treated as apparatus and excluded from difference counts."
    if n == 83:
        r["evidence"] += " H's note already describes the descending arrangement. Root directs that its duplicate left-member rendering be treated as layout representation and excluded from difference counts."
    if not cp:
        pending_crop.append(r["id"])
    rows.append(r)

def extra(n, source_reader, source_id, final, a_reading, b_reading, c_reading, diff_C, diff_H):
    src = ROWS[source_reader][source_id]
    r = {k:copy.deepcopy(src[k]) for k in ["location","C","H","confidence","kind","C_doubt_status"]}
    r.update(
        id=f"004-{n:02d}", final=final, diff_C=diff_C, diff_H=diff_H,
        readers={"A":a_reading,"B":b_reading,"C":c_reading},
        evidence=f"Root adjudication pending. Final field follows A provisionally. {source_reader} report: {src['evidence']}",
        crop=crop_path(source_reader, src["readers_crop"]), marked_in_H="no",
    )
    rows.append(r)
    used[source_reader].add(source_id)

extra(
    84, "B", "B004.34", r"\boxed{...}",
    "reading.tex (left enclosure): \\boxed; report inventory 004.36: frame with retraced/doubled lower and left edges",
    f"B004.34: {ROWS['B']['B004.34']['reading']}",
    "reading.tex (left enclosure): \\boxed; report inventory 004.36: rectangular enclosure with retraced lower boundary",
    False, False,
)
extra(
    85, "B", "B004.30", r"f_2",
    exact_tex("A", "end of cancelled first continuation", r"\beta f_2"),
    f"B004.30: {ROWS['B']['B004.30']['reading']}",
    exact_tex("C", "end of cancelled first continuation", r"\beta f_2"),
    False, True,
)
extra(
    86, "C", "N01", "",
    exact_tex("A", "isolated cancelled-token display, with no preceding dot token", r"\deleted{\deleted{xf_1}}"),
    exact_tex("B", "isolated cancelled-token display, with no preceding dot token", r"\deleted{\deleted{xf_1}}"),
    f"N01: {ROWS['C']['N01']['reading']}",
    False, False,
)
used["B"].add("B004.33")  # Whole-sheet state belongs in metadata; H explicitly records both strokes.

assert used["A"] == set(ROWS["A"])
assert used["B"] == set(ROWS["B"]), ("B missing", set(ROWS["B"]) - used["B"])
assert used["C"] == set(ROWS["C"]), ("C missing", set(ROWS["C"]) - used["C"])

BY_ID = {r["id"]:r for r in rows}
ROOT_APPLIED = set()
def root_choice(numbers, reader, crop, evidence, **changes):
    for n in numbers:
        key = f"004-{n:02d}"
        r = BY_ID[key]
        r.update(changes)
        r["crop"] = crop_path(reader,crop)
        r["evidence"] = "Root personally viewed this crop. " + evidence
        ROOT_APPLIED.add(key)

# Root's directly supplied crop decisions; no independent re-reading by clerk.
root_choice([1,2],"C","01_top_parenthesis.png",
            "The descended loop and extra brace-like stroke remain ambiguous. Retain eta/gamma and brace/blank.")
root_choice([3],"A","02_xf_equality.png",
            "Two horizontal strokes support equals; the diagonal crossing supplies no third bar.")
root_choice([4],"C","03_cancelled_xf.png",
            "The crossing x, long looped f and low 1 resolve the locally cancelled token as xf_1.")
root_choice([86],"C","03_cancelled_xf.png",
            "A dark round mark lies to the left of the cancelled token; its intention is uncertain. Retain C-reader's unsure dot.",
            final=ROWS["C"]["N01"]["reading"],diff_C=True,diff_H=True)
root_choice([36],"B","04_expansion_factors.png",
            "The first f index is a dotted i.")
root_choice([37],"B","04_expansion_factors.png",
            "No separate dot is securely visible at the first e index. Retain B's i/1 alternatives.",
            final=ROWS["B"]["B004.06"]["reading"],confidence="low",diff_C=True)
for n, token in [(38,r"f_i f_1"),(39,r"e_i e_1"),(40,r"f_i e_1"),(41,r"e_i f_1")]:
    root_choice([n],"B","05_expansion_annotations.png",
                f"Root confirmed the i index separately in the RHS product {token}; the following factor retains subscript 1.")
root_choice([42,43,44],"B","05_expansion_annotations.png",
            "The recorded local strikes through the RHS products are confirmed separately from the whole-sheet cancellation.")
root_choice([46,47],"B","05_expansion_annotations.png",
            "The two underbrackets and lower annotations are retained. The first product's lower f_{i+1} extent is still pending a separate root crop at 004-45.")
root_choice([5],"B","05_expansion_annotations.png",
            "Retain the locally cancelled lower annotation and its minus/no-independent-minus uncertainty.")
root_choice([49,50,51,52],"B","06_upside_down_note.png",
            "The entire inverted three-line note is confirmed: locally cancelled e_1 f_d; e_i e_1=0 with 1≤i≤d−2; and unfinished f_i f_1=.")
root_choice([6,53],"A","06_delta_zero.png",
            "Both bottom-left delta starts are confirmed. The first is locally cancelled and its terminal 0 remains unsure; the second ends with an unfinished equals.")
root_choice([7,8],"A","07_upper_right_cancel.png",
            "The crop supports a superposed inserted minus above the cancelled a/0. Retain the cancelled-character doubt and the higher minus placement.")
root_choice([9],"A","09_underlined_cancel.png",
            "A tall looped f and a short lowered 1 remain discernible through the strike. Resolve the cancelled factor as f_1 at medium confidence.",
            final=r"\deleted{f_1}",confidence="medium",diff_C=True,C_doubt_status="resolved")
root_choice([10],"A","10_lower_brace_cancel.png",
            "Retain the unsure cancelled -e_i before the lower brace.")
root_choice([11],"C","12_right_second_case.png",
            "A horizontal minus and separate right-hand 1 are visible; no vertical crossing is seen. Resolve the eta index as i−1 at medium confidence.",
            final=r"\eta_{i-1}",confidence="medium",diff_C=True,C_doubt_status="resolved",
            mathematical_consequence="The lower even-case eta factor reads i−1; H supplies i+1 and the following written result retains i+2. Root's crop reading governs the index.")
root_choice([12],"C","12_right_second_case.png",
            "The following factor has a looped e with low 1. Resolve e_1 at medium confidence.",
            final=r"e_1",confidence="medium",diff_C=True,C_doubt_status="resolved")
root_choice([58],"C","12_right_second_case.png",
            "Preserve the local strike through the added e_{i+1}e_1 product.")
root_choice([59],"B","13_lower_struck_tail.png",
            "The entire crossed tail is confirmed. The detached upper stroke survives at its final f_2; retain B's bar/arrow/plain-f uncertainty, recorded separately at 004-85.",
            final=ROWS["B"]["B004.29"]["reading"])
root_choice([85],"B","13_lower_struck_tail.png",
            "A detached short upper stroke survives above the final f_2. Retain bar/arrow/plain f_2 alternatives.",
            final=ROWS["B"]["B004.30"]["reading"],diff_C=True)
root_choice([13,78],"A","12_initials.png",
            "Retain QPhiS/QDS/QPS/QFS. No punctuation precedes the initials.")
root_choice([16],"A","13_box_marks.png",
            "Two dark separated short marks support the unsure paired quotation-like ticks.")
root_choice([84],"B","16_box_lower_rules.png",
            "Two distinct near-horizontal strokes form the lower boundary. Include the second lower box rule.",
            final=r"\underline{\boxed{...}}",diff_C=True,diff_H=True)

# Root's second and final supplied batches. The clerk still opens no images.
root_choice([33],"C","14_left_bound.png",
            "The range parentheses and both less-than-or-equal signs are confirmed.")
root_choice([34,62,64],"root","01_left_brace_relations.png",
            "The enclosing left brace is confirmed. No commas follow the left e_i e_1=0 or f_i e_1=e_{i+1} relations.")
root_choice([63],"root","02_left_case_ends.png",
            "No comma follows the left cases.")
root_choice([35,65,66],"root","03_below_box_eta.png",
            "The eta lines stand at the upper right of the xf relation, with no comma or semicolon.")
root_choice([14,67],"root","04_below_box_condition.png",
            "The words deg x pair are confirmed, with no following punctuation.")
root_choice([45],"root","05_lower_annotation_extent.png",
            "The complete lower f_{i+1} annotation is confirmed, including its lower ink. This resolves the extent left outside the earlier reader crops.")
root_choice([48,69,70],"root","06_e2_e3_block.png",
            "The e_2/e_3 equations form an independent two-line block. There is no comma after the first equation and no period after the second.")
root_choice([54,71],"root","07_upper_right_brace.png",
            "The large upper-right brace is confirmed, with no comma after the first zero.")
root_choice([55,56,72],"root","08_upper_right_case_labels.png",
            "Both si labels are confirmed. No comma follows the cases.")
root_choice([73],"root","09_right_linear_end.png",
            "No comma follows the right linear combination.")
root_choice([57,74],"root","10_rule_identity_end.png",
            "A single underline continues beneath the identity. No semicolon follows its last term.")
root_choice([75],"root","11_lower_bound.png",
            "No comma follows the lower bound.")
root_choice([30,31,32,83],"root","12_vertical_chain.png",
            "Three rotated equality signs descend under the first member. Root chooses A's array alignment; the layout-only difference and H's repeated-member rendering remain excluded from counts.")
root_choice([15],"root","13_lower_case_labels.png",
            "The first lower case reads i imp, unexpanded and without a terminal dot.")
root_choice([61,76,77],"root","14_circled_result.png",
            "The circle around beta=0 is confirmed. There is no comma after beta=0 or alpha=±1.")
root_choice([79],"root","15_foot_eta_delta.png",
            "The final eta and delta identities occupy separate lines. There is no comma after the first, and the final full stop is retained.")
root_choice([68],"root","16_expansion_terminal_punctuation.png",
            "The closing parenthesis is clear, with blank space to its right and no comma. Root gives full-scan bbox [1180,1220,1295,1410].")
BY_ID["004-05"]["diff_C"] = False
BY_ID["004-05"]["evidence"] += " Root sets diff_C=false: the doubtful minus is unchanged, with its blank alternative made explicit."

pending_crop = [r["id"] for r in rows if not r["crop"]]

doubts = []
for d in REPORTS["A"]["doubts"]:
    source_number = next(n for n,a in AA.items() if a["location"] == d["location"])
    decision = BY_ID[f"004-{source_number:02d}"]
    if decision["C_doubt_status"] == "resolved":
        continue
    e = copy.deepcopy(d)
    e["crop"] = decision["crop"]
    e["reason"] = decision["evidence"]
    doubts.append(e)
for x, sid, final_n, alt in [
    ("B","B004.06",37,["1"]),
    ("B","B004.30",85,[r"\vec f_2",r"f_2"]),
    ("C","N01",86,["unassigned incidental dot"]),
]:
    s = ROWS[x][sid]
    decision = BY_ID[f"004-{final_n:02d}"]
    doubts.append({
        "location":s["location"], "reading":s["reading"], "alternatives":alt,
        "confidence":s["confidence"],
        "reason":decision["evidence"],
        "crop":decision["crop"],
    })

# Root directs that reported prose positions be retained. Source text is copied;
# full-scan row/crop coordinates supply ordering only, not replacement positions.
inventory = copy.deepcopy(REPORTS["A"]["inventory"])
for source_reader, element in [("C","004.35"),("C","004.37"),("B","004.B36")]:
    source = next(r for r in REPORTS[source_reader]["inventory"] if r["element"] == element)
    e = copy.deepcopy(source)
    e["element"] = f"004-extra-{source_reader}-{element.rsplit('.',1)[1]}"
    inventory.append(e)
for r in inventory:
    r["sheet_kind"] = "cancelled_draft"
    assert r["kind"] in {"text","display","diagram","drawing","margin note","insertion","deletion"}
INV = {r["element"]:r for r in inventory}
INV["004.07"]["first_words_or_objects"] = "(f_i+lambda e_{i|1})(f_1+lambda e_1); first e-index remains uncertain"
INV["004.28"]["first_words_or_objects"] = next(r for r in REPORTS["B"]["inventory"] if r["element"] == "004.28")["first_words_or_objects"]
INV["004.36"]["first_words_or_objects"] = next(r for r in REPORTS["B"]["inventory"] if r["element"] == "004.B34")["first_words_or_objects"]

inventory_order = [
    "004.01", "004.35", "004.20", "004.02", "004.21", "004.36", "004.03",
    "004.22", "004.23", "004.32", "004.34", "004.24", "004.25", "004.05",
    "004.26", "004.04", "004.27", "004.06", "004.28", "004-extra-B-B36",
    "004-extra-C-35", "004.07", "004.12", "004.08", "004.10", "004.15",
    "004.33", "004.29", "004.11", "004.13", "004.14", "004.09", "004.16",
    "004.30", "004-extra-C-37", "004.18", "004.19", "004.17", "004.31",
]
assert set(inventory_order) == {e["element"] for e in inventory}
inventory.sort(key=lambda e: inventory_order.index(e["element"]))

check_events = [
    {
        "statement_id":"004-lambda-expansion",
        "date":"2026-11-20 09:40:10 UTC",
        "who":"GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root",
        "type":"computation or formal certificate",
        "outcome":"In the free associative algebra over Z[lambda,alpha,beta] with central displayed parameters, expansion of (f_i+lambda e_i)(f_1+lambda e_1) minus (f_i f_1+lambda^2 e_i e_1+lambda(f_i e_1+e_i f_1)) returned residual 0. Written factor order was retained. Source: checks/scan004_algebra.md and scripts/check_scan004_algebra.py.",
    },
    {
        "statement_id":"004-even-coefficient",
        "date":"2026-11-20 09:40:10 UTC",
        "who":"GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root",
        "type":"computation or formal certificate",
        "outcome":"Expansion of (-alpha e_next-beta f_next)+e_next minus ((1-alpha)e_next-beta f_next) returned residual 0. This records the coefficient arithmetic. Source: checks/scan004_algebra.md and scripts/check_scan004_algebra.py.",
    },
]
assert REPORTS["A"]["check_events"] == [] and REPORTS["B"]["check_events"] == []
assert len(REPORTS["C"]["check_events"]) == 1
ce = REPORTS["C"]["check_events"][0]
check_events.append({
    "statement_id":"004-even-coefficient",
    "date":"2026-11-20",
    "who":"GPT-6 Astra Pro; effort inherited, separately verifiable setting not exposed; run /root/scan004_c",
    "type":"computation or formal certificate",
    "outcome":f"Reported {ce['type']} at {ce['location']}: {ce['result']} Exact check time was not recorded. Source: readers/004/C/report.json, check_events[0].",
})

notes = (
    "Scan 004 corresponds to H page 3. Two long diagonal strokes cross both columns of this landscape algebra draft. "
    "The left column contains the top identities, a framed system, the xf_1 relation and adjacent eta formulas, a lambda expansion with lower annotations and local cancellations, "
    "a separate e_2/e_3 block, an upside-down marginal start and two bottom-left delta starts. "
    "The right column contains a braced system, an underlined identity, lower cases and descending equalities, a circled beta=0, alpha=±1, a signed delta-eta result, joined initials and two final identities. "
    "No title, date or author page number is established. The archive numeral 3 is retained only as a comment.\n\n"
    "All twelve actual witness-C doubt loci remain represented in decisions. The settled notation and abbreviation table entries carry no C doubt status. "
    "Root's supplied crop decisions resolve the cancelled f_1, the lower eta index as i−1 and its following e_1. "
    "The first expansion e-index retains i/1; the final f_2 in the cancelled tail retains bar/arrow/plain alternatives. "
    "The unsure paired ticks, isolated dot and second lower box rule are included. Root supplied crop decisions for all ink differences; unchanged notation rows remain available for root's retention decision. "
    "Root inspected A's faint-surface crops 14 and 15 and found no secure token; comments alone are retained. "
    "Root also confirmed (1−alpha) in A crop 08. H's initial note explicitly describes the page-wide crossing strokes; local cancellation rows remain separate. "
    "H note prose is apparatus. Root directs that H's clearly descriptive body captions and duplicate left-member rendering be excluded from difference counts; their exact reader mappings remain in this draft.\n\n"
    "Root's two recorded calculations at 2026-11-20 09:40:10 UTC each returned residual 0: the factor-order-preserving lambda expansion and the coefficient collection producing (1-alpha). "
    "Reader C reports a separate explicit coefficient substitution and collection on 2026-11-20, without an exact time. "
    "Readers A and B report no proof checks. No check event certifies the written beta=0 or alpha=±1 conclusions. "
    "The root-read lower eta index i−1 and written final f_{d-3}e_1 are retained."
)

workflow = (
    "Provisional mechanical assembly by /root/record004; no images opened and no ink decisions made. "
    "The report backbone is A's 83 rows. A004-060 is retained here as metadata only: A uses array alignment, while B and C use gathered; "
    "the notation-only macro difference generates no collation row. The physical body repetition is exposed separately at 004-83. "
    "All 57 B and 59 C-reader rows are mapped to decisions or named metadata, with complete TeX excerpts where a reader has no separate report row. "
    "B004.33 reports diff_H=true for whole-sheet deletion, while A and C acknowledge H's initial note; the root's instruction sets the global H difference to false. "
    "Added rows 004-84, 004-85 and 004-86 isolate B's second lower rule, B's f_2 upper mark and C-reader's dot. "
    "Root's supplied crop-adjudication decisions have been applied at " + ", ".join(sorted(ROOT_APPLIED)) + ". "
    "The source reader files are unchanged. All readers report one whole-page view and one view of each supplied half; retained crop counts are A 15, B 16 and C 14. "
    "Crop paths are relative to out. A half-b coordinate [x1,y1,x2,y2] maps to [x1+1170,y1,x2+1170,y2] in the full scan, as specified by the B/C reports; half-a coordinates are unchanged. "
    "Existing-crop containment was checked arithmetically. Root's crop 05 confirms the complete first lower annotation at 004-45, including the extent omitted by A crop 04 and B crop 05. "
    "Root personally viewed 19 existing reader crops: C01,C03,C12,C14; A02,A06,A07,A08,A09,A10,A12,A13,A14,A15; B04,B05,B06,B13,B16. Root also personally viewed all 16 new crops under crops/004. "
    "An earlier oversized tool response did not display the images; root re-emitted the actual chosen crops before recording these decisions. "
    "A mechanical comparison with root's out/pages/J81-01_81_scan004.tex confirmed eleven remaining unsure loci and the root-selected standard underline around the box. "
    "Unchanged notation or zero-count apparatus rows without an attached retained crop: " + ", ".join(pending_crop) + ". "
    + "Root directed that reported prose inventory positions be kept; the inventory is ordered top to bottom using the reported locus bounds where available, with the archive numeral at the upper paper edge. "
    + "All supplied root choices are applied. Main approval remains pending; main_adjudicated is false."
)
draft = {
    "scan":4,
    "folder":META["folder"],
    "their_page":int(META["their_page"]),
    "hua_has":META["hua_has"],
    "filename":"J81-01_81_scan004.tex",
    "brief_version":"v03",
    "main_adjudicated":False,
    "decisions":rows,
    "doubts":doubts,
    "inventory":inventory,
    "notes":notes,
    "abbreviations":[
        {"form":r"\deg","expansion":"degré"},
        {"form":"imp","expansion":"impair"},
        {"form":r"Q\Phi S / QDS / QPS / QFS","expansion":"uncertain"},
    ],
    "check_events":check_events,
    "workflow_note":workflow,
}
dest = OUT / "checks/scan004_record_draft.json"
dest.write_text(json.dumps(draft,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({
    "draft":str(dest),"decisions":len(rows),"union_doubts":len(doubts),
    "inventory":len(inventory),"check_events":len(check_events),
    "root_crop_required":pending_crop,"source_rows_covered":{x:len(used[x]) for x in "ABC"},
    "inventory_positions":"source prose retained under root instruction",
    "root_crop_decisions_applied":len(ROOT_APPLIED),
},ensure_ascii=False))
