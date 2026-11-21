"""Assemble root-selected scan021 text with exact, unapproved source provenance.

Only text is opened. No image, geometry computation, compilation, rendering or
mathematical check is performed. Source-coordinate literals are copied unchanged.
"""
from pathlib import Path
import copy
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
FINAL = "out/checks/scan021_final_draft.tex"
MAP = "out/checks/scan021_final_source_map.json"
ATTACHMENT_PATH = "checks/scan021_final_draft.tex"
JOURNAL = "out/checks/scan021_main_decisions.md"
BASE = "out/readers/021/C/reading.tex"
sha = lambda b: hashlib.sha256(b).hexdigest()
source_texts = {}


def text(path):
    if path not in source_texts:
        source_texts[path] = (ROOT / path).read_text(encoding="utf-8")
    return source_texts[path]


def source_ref(path, a=0, b=None):
    t = text(path)
    b = len(t) if b is None else b
    assert 0 <= a < b <= len(t), (path, a, b)
    s = t[a:b]
    return dict(path=path, manifest=path, char_start=a, char_end=b,
                byte_start=len(t[:a].encode()), byte_end=len(t[:b].encode()),
                line_start=t.count("\n", 0, a)+1,
                line_end=t.count("\n", 0, b-1)+1,
                excerpt=s, literal=s, literal_sha256_utf8=sha(s.encode()),
                source_sha256_utf8=sha(t.encode()))


def locate(path, value, occurrence=0):
    t, start = text(path), 0
    for _ in range(occurrence+1):
        a = t.index(value, start)
        start = a + len(value)
    return source_ref(path, a, a+len(value))


def source_piece(ref):
    return dict(text=ref["excerpt"], source_path=ref["path"],
                source_char_start=ref["char_start"], source_char_end=ref["char_end"])


def syntax_piece(value, purpose):
    return dict(text=value, source_path=None, source_kind="root-authorized assembly syntax",
                purpose=purpose, authority=JOURNAL)


def slice_piece(p, a, b):
    q = dict(p)
    q["text"] = p["text"][a:b]
    if p["source_path"]:
        q["source_char_start"] = p["source_char_start"]+a
        q["source_char_end"] = p["source_char_start"]+b
    return q


def range_pieces(items, a, b):
    out, cursor = [], 0
    for p in items:
        end = cursor+len(p["text"])
        left, right = max(cursor, a), min(end, b)
        if left < right:
            out.append(slice_piece(p, left-cursor, right-cursor))
        cursor = end
    assert sum(len(p["text"]) for p in out) == b-a
    return out


def piece_provenance(p):
    if p["source_path"]:
        return source_ref(p["source_path"], p["source_char_start"], p["source_char_end"])
    return dict(path=None, source_kind=p["source_kind"], purpose=p["purpose"],
                authority=p["authority"], excerpt=p["text"], literal=p["text"],
                literal_sha256_utf8=sha(p["text"].encode()))


candidates = json.loads((OUT / "scan021_tex_candidates.json").read_text())
candidate_groups = {g["id"]: g for g in candidates["graphic_groups"]}
for p, h in candidates["source_files"].items():
    assert sha((ROOT / p).read_bytes()) == h["sha256_utf8"], p


def candidate_ref(gid):
    r = candidate_groups[gid]["full_source"]
    return source_ref(r["path"], r["char_start"], r["char_end"])


unit_transfers = []


def adapted(ref, old_units, new_units, parent, gid):
    """Copy literals; replace only the declared unit string under root section25."""
    value = ref["excerpt"]
    parts, a = [], 0
    while True:
        b = value.find(old_units, a)
        if b < 0:
            break
        if b > a:
            parts.append(source_piece(source_ref(ref["path"], ref["char_start"]+a, ref["char_start"]+b)))
        parts.append(syntax_piece(new_units,
            f"Transfer {gid} to {parent}'s existing full-scan coordinate units; all coordinate literals unchanged."))
        unit_transfers.append(dict(group=gid, parent=parent, old_literal=old_units,
            new_literal=new_units, source=source_ref(ref["path"], ref["char_start"]+b,
            ref["char_start"]+b+len(old_units)), root_journal_section="25",
            scope="Identical declared full-scan coordinate map; no metric or geometric calculation.",
            main_approved=False))
        a = b+len(old_units)
    if a < len(value):
        parts.append(source_piece(source_ref(ref["path"], ref["char_start"]+a, ref["char_end"])))
    assert a > 0, (gid, old_units)
    return parts


def marked(gid, parts):
    return [syntax_piece(f"% BEGIN {gid}\n", "Label the complete selected nested source block.")] + parts + [syntax_piece(f"\n% END {gid}\n", "End selected block comment before adjoining source.")]


def a_node(gid, parent):
    group = candidate_groups[gid]["original_metadata"]["value"]
    x = group["source_origin"][0]
    baseline = group["baseline_y"]
    ref = candidate_ref(gid)
    return [syntax_piece(f"\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({x},{baseline}) {{$\n",
            f"Place {gid} at its copied source west/baseline anchor in {parent}.")] + adapted(ref,
            "x=.055mm,y=-.055mm", "x=.085mm,y=-.085mm", parent, gid) + [syntax_piece("$};\n", "Close the selected child node after the source block's existing newline, without adding visible ink.")]


pieces = [source_piece(source_ref(BASE))]
replacements = []


def current():
    return "".join(p["text"] for p in pieces)


def replace_at(a, b, new_pieces, rid, decisions, reason):
    global pieces
    before = current()
    old = before[a:b]
    removed = range_pieces(pieces, a, b)
    pieces = range_pieces(pieces, 0, a) + copy.deepcopy(new_pieces) + range_pieces(pieces, b, len(before))
    replacements.append(dict(id=rid, decision_ids=decisions, reason=reason,
        stage_char_start=a, stage_char_end=b, old_text=old,
        new_text="".join(p["text"] for p in new_pieces),
        stage_before_sha256_utf8=sha(before.encode()), stage_after_sha256_utf8=sha(current().encode()),
        removed_source_pieces=[piece_provenance(p) for p in removed],
        inserted_source_pieces=[piece_provenance(p) for p in new_pieces]))


def replace(old, new_pieces, rid, decisions, reason, occurrence=0, expected=1):
    before = current()
    assert before.count(old) == expected, (rid, before.count(old), expected, old[:100])
    start = 0
    for _ in range(occurrence+1):
        a = before.index(old, start)
        start = a+len(old)
    replace_at(a, a+len(old), new_pieces, rid, decisions, reason)


def D(*numbers):
    return [f"L021-{n:02d}" for n in numbers]


# Root sections01-08: C's first display and upper-display framework.
replace(r"\unsure{demonstration|démonstration}",
        [source_piece(locate(JOURNAL, r"d\unsure{è|é|e}monstration"))],
        "REP021-01", D(11), "Root-selected complete accent alternatives, with grave primary.")

c_node = r"\node at (520,555) {$U=X\setminus\bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+$};"
sigma = r"\widehat{\Sigma}_\alpha^+"
c_ref = locate(BASE, c_node)
s = c_node.index(sigma)
new = [source_piece(source_ref(BASE, c_ref["char_start"], c_ref["char_start"]+s)),
       syntax_piece(r"\phantom{", "Reserve the original text-node extent while the selected literal Sigma is placed once at its source anchor."),
       source_piece(source_ref(BASE, c_ref["char_start"]+s, c_ref["char_start"]+s+len(sigma))),
       syntax_piece("}", "Close the invisible original font placeholder."),
       source_piece(source_ref(BASE, c_ref["char_start"]+s+len(sigma), c_ref["char_end"])),
       syntax_piece("\n", "Separate complete selected source nodes.")] + a_node("A021G05", "C021-G02")
replace(c_node, new, "REP021-02", D(16), "Select A's complete upper Sigma while retaining C's U/complement/union/limit node.")

c_start = text(BASE).index("% Cancellation: literal underlying Sigma/alpha")
c_end = text(BASE).index("\\end{tikzpicture}\n% END C021-G02", c_start)
b_path = "out/readers/021/B/reading.tex"
b_start = text(b_path).index("% Complete cancelled lower group;")
b_ref = candidate_ref("B021-G02-cancelled-Sigma")
b_complete = source_ref(b_path, b_start, b_ref["char_end"])
replace(text(BASE)[c_start:c_end], marked("B021-G02-cancelled-Sigma", adapted(b_complete,
        "x=.006cm,y=-.006cm", "x=.085mm,y=-.085mm", "C021-G02", "B021-G02-cancelled-Sigma")),
        "REP021-03", D(14, 15), "Replace the complete cancelled group including its invisible deleted/qualified annotation and every literal old/crossing stroke.")

# Sections09-12: Or cluster, central point/trace, and right literal index.
replace(r"\unsure{comme}", [source_piece(candidate_ref("B021-G03")),
        syntax_piece("\n", "End B's source marker before the surviving literal words on a.")],
        "REP021-04", D(18, 19, 20), "Select B's complete retraced cluster; Or and on a remain outside.")
old = r"\unsure{comme|\deleted{co}comme|\deleted{car}comme}"
b_ann = locate(b_path, old)
prefix = r"\unsure{comme|"
replace(old, [source_piece(source_ref(b_path, b_ann["char_start"], b_ann["char_start"]+len(prefix))),
        source_piece(locate("out/readers/021/A/reading.tex", r"\deleted{co}mme")),
        syntax_piece("|", "Separate the complete root-selected invisible state alternatives."),
        source_piece(source_ref(b_path, b_ann["char_start"]+len(prefix), b_ann["char_end"]))],
        "REP021-05", D(18, 19), "Add A's complete deleted co plus live mme alternative to B's invisible state annotation.")
replace("% Complete alternatives for the three-part ink group: comme | deleted(co) comme | deleted(car) comme.",
        [syntax_piece("% Complete selected alternatives: comme | deleted(co) mme | deleted(co) comme | deleted(car) comme.",
        "Describe all root-selected complete alternatives in the nonprinting source comment.")],
        "SYNTAX021-OR-ANNOTATION", D(18,19), "Update the comment to match the complete selected invisible annotation.")

point_line = r"\fill[gray] (1154,855) circle[radius=.7];"
trace_line = r"\draw[gray,line width=.2pt] (1155,861)..controls(1153,864)and(1156,866)..(1155,869);"
replace(point_line, [source_piece(locate(BASE, point_line)), syntax_piece("\n", "Separate copied literal point and pale continuation."),
        source_piece(locate("out/readers/021/A/reading.tex", trace_line))],
        "REP021-06", D(24), "Merge A's pale continuation into C's qualified point-only child; both literal components occur once.")

font_index = r"\node at (1208,1168) {$\scriptstyle\unsure{\alpha_0|\alpha}$};"
replace(font_index, marked("B021-G05-index", adapted(candidate_ref("B021-G05-index"),
        "x=.006cm,y=-.006cm", "x=.085mm,y=-.085mm", "C021-G04", "B021-G05-index")),
        "REP021-07", D(25), "Replace the whole right font-index node with B's complete literal qualified index at B's declared full-scan anchor.")

# Sections13-14: A's full anchored margin group and the selected third row.
a_path = "out/readers/021/A/reading.tex"
a_margin_start = text(a_path).index("% independent right-margin group;")
a_margin_end = text(a_path).index("d'autre part", a_margin_start)
c_margin_start = text(BASE).index("% margin note: upright rows")
c_margin_end = text(BASE).index("d'autre part", c_margin_start)
replace(text(BASE)[c_margin_start:c_margin_end],
        [source_piece(source_ref(a_path, a_margin_start, a_margin_end))],
        "REP021-08", D(*range(28, 41)), "Select A's lead-in plus its complete anchored diagram, including both nested scope maps and each brace/sideways-label path.")

a_child = candidate_ref("A021D03")
outer_start = text(a_path).rfind("\\node[", 0, a_child["char_start"])
outer_end = text(a_path).index("$};", a_child["char_end"])+3
replace(text(a_path)[outer_start:outer_end], marked("B021-G06-middle-row", adapted(candidate_ref("B021-G06-middle-row"),
        "x=.006cm,y=-.006cm", "x=.055mm,y=-.055mm", "A021DG", "B021-G06-middle-row")),
        "REP021-09", D(31,35), "Replace the full third-row placement node with B's shared hook/dot/index group; preserve A's surrounding anchored parent.")
full_candidates = r"\Sigma_{i\alpha}\mid\Sigma_{i,\alpha}\mid\Sigma_{\dot\alpha}"
replace(r"\Sigma_{i\alpha}|\Sigma_{i,\alpha}",
        [source_piece(locate(a_path, full_candidates, occurrence=1))],
        "REP021-10", D(31), "Retain all three root-selected complete index readings in the invisible annotation.")

sign_ref = candidate_ref("A021D05")
sign_body_start = text(a_path).index("% A021D05 BEGIN", sign_ref["char_start"])
sign_body_end = text(a_path).index("% A021D05 END", sign_body_start)+len("% A021D05 END\n")
replace(sign_ref["excerpt"], [source_piece(source_ref(a_path, sign_body_start, sign_body_end))],
        "REP021-11", D(32), "Remove the selected sign's unsure wrapper after root resolution; all literal point/run paths remain.")
old_annotation = r"\rotatebox{-90}{$!$}\mid\text{ou}\mid-"
resolved_annotation = r"\rotatebox{-90}{$!$}"
for n in range(2):
    replace(old_annotation, [source_piece(locate(a_path, resolved_annotation, occurrence=1))],
            f"REP021-12-{n+1}", D(32), "Narrow only the resolved sign's invisible annotation to its selected shaft-and-point reading.", expected=2-n)

# Sections15-18: endpoint, exclusion, cancelled predecessor and conclusion.
replace("d'autre part $\\alpha_0\\in K_1$ signifie", [source_piece(locate(a_path,
        "d'autre part $\\alpha_0\\in K_1$ \\unsure{signifie|signifi}"))],
        "REP021-13", D(41), "Retain root's selected signifie primary with signifi alternative.")
replace(candidate_ref("C021-G06")["excerpt"], [source_piece(candidate_ref(g)) for g in ["A021G10", "A021G11", "A021G12"]],
        "REP021-14", D(42, 43, 44), "Select the complete A exclusion sequence, including the interrupted/pale right head pieces.")
replace(candidate_ref("C021-G07")["excerpt"], [source_piece(candidate_ref("B021-G08"))],
        "REP021-15", D(45, 46), "Select B's complete cancelled literal verb with both crossing runs; live signifie stays outside.")

# Sections19-24: C's lower-body framework; heading remains outside it.
pi_node = r"\node at (300,1915) {$V$ de $\Pi_I^{\unsure{\circ|0}}$, son expression};"
pi = r"\Pi_I^{\unsure{\circ|0}}"
pi_ref = locate(BASE, pi_node)
p = pi_node.index(pi)
replace(pi_node, [source_piece(source_ref(BASE, pi_ref["char_start"], pi_ref["char_start"]+p)),
        syntax_piece(r"\phantom{", "Reserve the original Pi font extent while A's complete literal Pi is placed once at its source anchor."),
        source_piece(source_ref(BASE, pi_ref["char_start"]+p, pi_ref["char_start"]+p+len(pi))),
        syntax_piece("}", "Close the invisible Pi placeholder; V de and the comma remain visible once."),
        source_piece(source_ref(BASE, pi_ref["char_start"]+p+len(pi), pi_ref["char_end"])),
        syntax_piece("\n", "Separate complete selected nodes.")] + a_node("A021G22", "C021-G09"),
        "REP021-16", D(51, 52), "Select A's complete Pi/head/stems/I/ring without duplicating V de, Pi, or the comma.")

replace(r"\node at (952,1986) {$\widehat{\Sigma}_\alpha^+$};", a_node("A021G15", "C021-G09"),
        "REP021-17", D(55), "Replace C's ordinary Sigma node with A's entire literal roof/head/body/alpha/plus group.")
replace(r"pr\unsure{é|ê}cédent", [source_piece(locate(JOURNAL,
        r"pr\unsure{ê|é|e}c\unsure{é|è|e}dent"))],
        "REP021-18", D(56, 57), "Apply both exact root-selected accent alternatives and primary orders.")

open_node = r"\node at (521,2281) {$K=\{\alpha\in I\mid\overline V\cap E_\alpha\ne\varnothing\quad\text{i.e.}\quad$};"
open_ref = locate(BASE, open_node)
open_pos = open_node.index(r"\{")
open_path = next(line for line in text(b_path).splitlines() if line.startswith(r"\draw[line width=.35pt] (689,2204)"))
replace(open_node, [source_piece(source_ref(BASE, open_ref["char_start"], open_ref["char_start"]+open_pos)),
        syntax_piece(r"\phantom{", "Keep the original node extent while replacing its visible generic set brace with the selected literal curve."),
        source_piece(source_ref(BASE, open_ref["char_start"]+open_pos, open_ref["char_start"]+open_pos+2)),
        syntax_piece("}", "Close invisible generic brace placeholder."),
        source_piece(source_ref(BASE, open_ref["char_start"]+open_pos+2, open_ref["char_end"])),
        syntax_piece("\n", "Separate literal curve from the word-bearing node.")] + marked("B021-G10-set-open", [source_piece(locate(b_path, open_path))]),
        "REP021-19", D(60), "Copy B's complete looped opening set-brace path under C's identical full-scan coordinate map.")

close_node = r"\node at (1506,2251) {$\cap\dot V\ne\varnothing\}$};"
close_ref = locate(BASE, close_node)
close_pos = close_node.index(r"\}")
close_path = next(line for line in text(b_path).splitlines() if line.startswith(r"\draw[line width=.35pt] (1655,2171)"))
replace(close_node, [source_piece(source_ref(BASE, close_ref["char_start"], close_ref["char_start"]+close_pos)),
        syntax_piece(r"\phantom{", "Replace the visible generic closing brace while preserving the existing following node extent."),
        source_piece(source_ref(BASE, close_ref["char_start"]+close_pos, close_ref["char_start"]+close_pos+2)),
        syntax_piece("}", "Close invisible generic brace placeholder."),
        source_piece(source_ref(BASE, close_ref["char_start"]+close_pos+2, close_ref["char_end"])),
        syntax_piece("\n", "Separate complete literal closing curve.")] + marked("B021-G10-set-close", [source_piece(locate(b_path, close_path))]),
        "REP021-20", D(60), "Copy B's complete right closing set-brace path once; no extra mathematical word or punctuation is added.")

c_rule = next(line for line in text(BASE).splitlines() if line.startswith(r"\draw (260,1818)"))
a_rule = candidate_groups["A021G25"]["original_metadata"]["value"]["path_commands"][0]
replace(c_rule, marked("A021G25-selected-path", [source_piece(locate(a_path, a_rule))]),
        "REP021-21", D(68), "Select A's one complete side-rule path under the C lower-parent coordinate map; no adjacent word is owned.")
replace("% Continuous left rule, slightly bent, reaches the physical bottom margin.",
        [syntax_piece("% Selected complete A side-rule path; its lower endpoint stops before the physical paper boundary.",
        "Describe the selected endpoint as recorded in root journal section24.")],
        "SYNTAX021-RULE-COMMENT", D(68), "Update nonprinting selected-source wording after replacing the original C side-rule path.")

# Section25: source-only paragraph-break repair, after all complete replacements.
display = False
blank_ranges = []
cursor = 0
for line in current().splitlines(keepends=True):
    if r"\[" in line:
        display = True
    if display and not line.strip():
        blank_ranges.append((cursor, cursor+len(line)))
    if r"\]" in line:
        display = False
    cursor += len(line)
for n, (a, b) in enumerate(reversed(blank_ranges), 1):
    replace_at(a, b, [], f"SYNTAX021-DISPLAY-BLANK-{n:02d}", [],
        "Remove a physical paragraph blank inside a selected display; original C source remains unchanged (root section25).")

header = "% Root-selected scan021 assembly; pending root approval.\n% Exact source and all selected literal components are mapped in scan021_final_source_map.json.\n"
replace_at(0, 0, [syntax_piece(header, "Identify this assembled draft without changing manuscript content.")],
        "SYNTAX021-HEADER", [], "Add a nonprinting pending-approval provenance header.")

final_text = current()
final_sha = sha(final_text.encode())
(ROOT / FINAL).write_text(final_text, encoding="utf-8")


def final_ref(a, b, attachment_id=None):
    s = final_text[a:b]
    return dict(path=ATTACHMENT_PATH, workspace_path=FINAL,
        manifest="checks/scan021_final_source_map.json", workspace_manifest_path=MAP,
        char_start=a, char_end=b,
        byte_start=len(final_text[:a].encode()), byte_end=len(final_text[:b].encode()),
        line_start=final_text.count("\n", 0, a)+1,
        line_end=final_text.count("\n", 0, b-1)+1,
        excerpt=s, literal=s, literal_sha256_utf8=sha(s.encode()),
        body_sha256=final_sha, final_file_sha256=final_sha, draft_sha256_utf8=final_sha,
        attachment_id=attachment_id)


source_segments = []
cursor = 0
for n, p in enumerate(pieces, 1):
    end = cursor+len(p["text"])
    if end > cursor:
        source_segments.append(dict(id=f"SEG021-{n:04d}", final=final_ref(cursor, end), source=piece_provenance(p)))
    cursor = end
assert cursor == len(final_text)


def exact_pieces(a, b):
    return [piece_provenance(p) for p in range_pieces(pieces, a, b)]


def find_group(gid):
    if gid == "A021DG":
        a = final_text.index("% A021DG BEGIN")
        end = "% A021DG END"
    elif gid.startswith("A021") and "-" not in gid:
        a = final_text.index(f"% {gid} BEGIN")
        end = f"% {gid} END"
        # Qualified A groups preserve the complete immediately preceding wrapper.
        pre = final_text.rfind("\\unsure{", 0, a)
        if pre >= 0 and "\n" not in final_text[pre:a].rstrip("\n"):
            a = pre
    else:
        a = final_text.index(f"% BEGIN {gid}\n")
        end = f"% END {gid}"
    m = re.search(re.escape(end)+r"(?:\n|$)", final_text[a:])
    assert m, gid
    b = a+m.end()
    if gid.startswith("A021") and final_text[a:].startswith("\\unsure{"):
        assert final_text[b:b+2] == "}\n", gid
        b += 2
    return a, b


group_decisions = {
    "C021-G01": D(3,4,5,6,7,8), "C021-G01a": D(4,8),
    "C021-G02": D(12,13,14,15,16,17), "C021-G02a": D(13), "C021-M01": D(17),
    "A021G05": D(16), "B021-G02-cancelled-Sigma": D(14,15),
    "B021-G03": D(18,19,20), "C021-M02": D(21),
    "C021-G03": D(22,23,24), "C021-M03": D(24),
    "C021-G04": D(25,26,27), "B021-G05-index": D(25),
    "A021G20": D(28,29), "A021DG": D(*range(30,41)),
    "A021D01": D(33), "A021D02": D(34), "B021-G06-middle-row": D(31,35),
    "A021D04": D(36), "A021D05": D(32), "A021M04": D(37),
    "A021G10": D(42), "A021G11": D(44), "A021G12": D(43),
    "B021-G08": D(45,46), "C021-G08": D(48,49,50),
    "C021-G09": D(*range(51,67),68,69), "C021-M05": D(53), "C021-M06": D(69),
    "A021G22": D(51,52), "C021-G09a": D(54), "A021G15": D(55),
    "C021-G09b": D(59), "B021-G10-set-open": D(60), "B021-G10-set-close": D(60),
    "A021G25-selected-path": D(68),
}
selected_groups = []
for gid, decisions in group_decisions.items():
    a, b = find_group(gid)
    original_gid = "A021G25" if gid == "A021G25-selected-path" else gid
    if gid.startswith("B021-G10-set-"):
        original_gid = "B021-G10"
    original = candidate_groups[original_gid]
    fragment = final_text[a:b]
    literal_components = []
    pos = a
    for line in fragment.splitlines(keepends=True):
        if re.match(r"\s*\\(?:draw|fill|path|useasboundingbox|coordinate|node)\b", line):
            literal_components.append(dict(final_source_attachment=final_ref(pos, pos+len(line)),
                exact_source_pieces=exact_pieces(pos, pos+len(line))))
        pos += len(line)
    selected_groups.append(dict(id=gid, decision_ids=decisions,
        source=original["full_source"], source_metadata=original["original_metadata"],
        final_source_attachment=final_ref(a,b,gid), selected_exact_source=fragment,
        exact_source_pieces=exact_pieces(a,b), literal_components=literal_components,
        source_comments=[line for line in fragment.splitlines() if line.lstrip().startswith("%")],
        tikz_declaration_lines=[line for line in fragment.splitlines() if any(x in line for x in
            [r"\begin{tikzpicture}", r"\begin{tikzcd}", r"\begin{scope}", r"\coordinate", "baseline=", "shift=", "cm="])],
        source_modification_ids=[r["id"] for r in replacements if set(decisions).intersection(r["decision_ids"])],
        lexical_parent_groups=[], main_approved=False))
for group in selected_groups:
    s = group["final_source_attachment"]
    for other in selected_groups:
        t = other["final_source_attachment"]
        if group["id"] != other["id"] and t["char_start"] <= s["char_start"] and s["char_end"] <= t["char_end"]:
            group["lexical_parent_groups"].append(other["id"])


def strip_comments(t):
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in t.splitlines())


clean = strip_comments(final_text)
brace_stack = []
for m in re.finditer(r"(?<!\\)[{}]", clean):
    if m.group() == "{":
        brace_stack.append(m.start())
    else:
        assert brace_stack, ("unmatched closing brace", m.start())
        brace_stack.pop()
assert not brace_stack, ("unmatched opening braces", brace_stack)
env_stack = []
for m in re.finditer(r"\\(begin|end)\{([^}]+)\}", clean):
    if m.group(1) == "begin":
        env_stack.append(m.group(2))
    else:
        assert env_stack and env_stack.pop() == m.group(2), ("environment", m.group())
assert not env_stack
assert clean.count("$") % 2 == 0
assert clean.count(r"\[") == clean.count(r"\]")
assert "$overset{" not in final_text
inside = False
inline_parity = 0
for line in final_text.splitlines():
    source_line = re.split(r"(?<!\\)%", line, maxsplit=1)[0]
    if r"\[" in line:
        inside = True
    assert not ((inside or inline_parity) and not line.strip()), "physical paragraph blank inside math"
    inline_parity = (inline_parity + len(re.findall(r"(?<!\\)\$", source_line))) % 2
    if r"\]" in line:
        inside = False

source_map = dict(schema="scan021-root-selected-source-map-v1", status="Selected source assembled; pending record attachments and root approval.",
    main_adjudicated=False, main_approved=False,
    scope="Source-only exact-byte assembly; no image work, geometry computation, compilation, rendering or mathematical validation.",
    offset_convention="zero-based Unicode code points and explicit UTF-8 bytes; ends exclusive",
    final_path=FINAL, attachment_path_relative_to_out=ATTACHMENT_PATH,
    final_sha256=final_sha, draft_sha256_utf8=final_sha, final_sha256_utf8=final_sha,
    base_source=BASE, base_sha256=sha(text(BASE).encode()),
    source_files={p: dict(sha256_utf8=sha(t.encode())) for p,t in source_texts.items()},
    source_segments=source_segments, replacements=replacements, selected_groups=selected_groups,
    final_blocks=[dict(id=g["id"],final_source_attachment=g["final_source_attachment"]) for g in selected_groups],
    selected_unit_transfers=unit_transfers,
    attachments_by_decision={}, attachments_by_source_locus={}, original_inventory_source_attachments={},
    attachments_by_inventory_source_group={}, selected_graphic_inventory_source_attachments={},
    archive_inventory_source_attachment=[], original_C_doubt_attachments={}, original_C_doubt_part_attachments={},
    root_authorizations={}, root_journal=dict(path=JOURNAL,sha256_utf8=sha(text(JOURNAL).encode())),
    preamble=dict(path="out/PREAMBLE.tex",sha256_utf8=sha((ROOT/"out/PREAMBLE.tex").read_bytes())),
    component_count_scope="Selected nested groups overlap their parents as provenance; each physical component is emitted once. Record021 owns all C/H counts.",
    pending_original_source_issue_not_selected=dict(id="A021-SOURCE-01",literal="$overset{",
        disposition="A's corollary prose wrapper was not selected. The selected independent V trace is C021-M05; no overset repair was needed."),
    processing_provenance=["All original A/B/C sources remain byte-identical to the released candidate fingerprints.",
        "Root journal sections01-27 authorize all selected ink choices and source-only transfers.",
        "C's selected physical display blanks were removed only after full group replacement.",
        "Literal full-scan coordinate values were copied; nested units follow the parent map, without metric fitting or rendered validation."],
    assembly_audit=dict(type="source-only", balanced_braces=True, balanced_environments=True,
        even_inline_math_delimiters=True, matched_display_delimiters=True, no_blank_display_lines=True, no_blank_inline_math_lines=True,
        missing_overset_sequence_absent=True, selected_groups=len(selected_groups), source_segments=len(source_segments),
        physical_display_blanks_removed=len(blank_ranges), main_approved=False))
(ROOT / MAP).write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(draft=FINAL,draft_sha256_utf8=final_sha,map=MAP,map_sha256_utf8=sha((ROOT/MAP).read_bytes()),
    selected_groups=len(selected_groups),replacements=len(replacements),status=source_map["status"]),ensure_ascii=False))
