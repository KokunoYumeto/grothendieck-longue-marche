from pathlib import Path
import hashlib
import json
import re

ROOT = Path("/workspace/scratch/94548b74fbe0")
OUT = ROOT / "out/checks"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source(path):
    p = ROOT / path
    raw = p.read_bytes()
    return {"path": path, "sha256": sha(raw), "byte_length": len(raw),
            "text": raw.decode("utf-8")}


sources = {
    "A": source("out/readers/019/A/reading.tex"),
    "B": source("out/readers/019/B/reading.tex"),
    "C": source("out/readers/019/C/reading.tex"),
    "current_C": source("packets/019/C.tex"),
    "H": source("packets/019/H.tex"),
}
reports = {
    r: json.loads((ROOT / f"out/readers/019/{r}/report.json").read_text())
    for r in ("A", "B", "C")
}


def span(witness, start, end):
    s = sources[witness]["text"]
    assert 0 <= start <= end <= len(s)
    raw = s[start:end]
    return {
        "path": sources[witness]["path"],
        "source_sha256": sources[witness]["sha256"],
        "start_char": start, "end_char": end,
        "start_byte": len(s[:start].encode("utf-8")),
        "end_byte": len(s[:end].encode("utf-8")),
        "start_line": s.count("\n", 0, start) + 1,
        "end_line": s.count("\n", 0, max(start, end - 1)) + 1,
        "text": raw, "text_sha256": sha(raw.encode("utf-8")),
    }


def lines(witness, first, last):
    s = sources[witness]["text"]
    ls = s.splitlines(keepends=True)
    assert 1 <= first <= last <= len(ls)
    return span(witness, sum(map(len, ls[:first-1])),
                sum(map(len, ls[:last])))


def literal(witness, text, occurrence=0):
    s = sources[witness]["text"]
    matches = [m.start() for m in re.finditer(re.escape(text), s)]
    assert len(matches) > occurrence, (witness, text, matches)
    start = matches[occurrence]
    return span(witness, start, start + len(text))


def command(witness, name, within, argument_count=1):
    s = sources[witness]["text"]
    start = s.index("\\" + name, within["start_char"], within["end_char"])
    opening = s.index("{", start, within["end_char"])
    end = None
    for arg in range(argument_count):
        depth = 0
        for i in range(opening, within["end_char"]):
            if s[i] == "{" and (i == 0 or s[i - 1] != "\\"):
                depth += 1
            elif s[i] == "}" and (i == 0 or s[i - 1] != "\\"):
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        assert end is not None, (witness, name, arg)
        if arg + 1 < argument_count:
            opening = s.index("{", end, within["end_char"])
    return span(witness, start, end)


def report_ref(reader, record_id):
    d = reports[reader]["differences"]
    indices = [i for i, row in enumerate(d) if row["id"] == record_id]
    assert len(indices) == 1, (reader, record_id)
    return {
        "path": f"out/readers/019/{reader}/report.json",
        "pointer": f"/differences/{indices[0]}",
        "row_id": record_id,
    }


SPECS = [
    {
        "reader": "A", "group": "G01", "locus": "first U of paired display",
        "container": (7, 15), "comments": (3, 6), "command": "mathord",
        "report_ids": ["A10"], "origin": [580, 535], "baseline": 60,
        "bounds": [0, 0, 120, 70], "scale": "0.008cm",
        "attachment": "The group ends before _{J,i}; the container also contains both paired terms.",
        "qualification": "Whole literal U is wrapped in unsure; cancelled-equality alternative is recorded in comments/report, absent from the printed group.",
    },
    {
        "reader": "A", "group": "G02", "locus": "point below l'une/l'un",
        "container": (16, 17), "comments": (17, 17), "inline": True,
        "report_ids": ["A11", "A15"],
        "attachment": "The inline formula includes the complete word l'une/l'un, the phantom l'un and one qualified cdot. Surrounding prose is outside the inline formula.",
        "qualification": "Word and dot have separate unsure wrappers; no TikZ origin or baseline is declared for this standard underset.",
    },
    {
        "reader": "A", "group": "G03", "locus": "first indexed footed union",
        "container": (23, 32), "comments": (20, 22), "command": "mathop",
        "report_ids": ["A03", "A04"], "origin": [895, 965], "baseline": 80,
        "bounds": [0, 0, 125, 90], "scale": "0.008cm",
        "attachment": "The group ends before limits; the container includes the J|j predecessor and the complete equality.",
        "qualification": "First union literal group has unsure; coprod/bigsqcup alternatives are retained in comment/report.",
    },
    {
        "reader": "A", "group": "G04", "locus": "second indexed footed union",
        "container": (45, 54), "comments": (42, 44), "command": "mathop",
        "report_ids": ["A16"], "origin": [820, 1605], "baseline": 80,
        "bounds": [0, 0, 95, 93], "scale": "0.008cm",
        "attachment": "The group ends before limits; the containing display includes the complete lower equality.",
        "qualification": "No local unsure wrapper is printed on this second occurrence; its independently reported coprod/bigsqcup doubt is attached to A16.",
    },
    {
        "reader": "B", "group": "G01", "locus": "first U of paired display",
        "container": (3, 15), "comments": (4, 7), "command": "mathord",
        "report_ids": ["B06"], "origin": [580, 540], "baseline": 54,
        "bounds": [0, 0, 118, 60], "scale": ".009cm",
        "attachment": "The group ends before _{J,i}; its unsure argument includes the literal alternate deleted-equality-plus-U.",
        "qualification": "Complete mathord/unsure group contains the full TikZ drawing and the printed alternative |deleted{=}U.",
    },
    {
        "reader": "B", "group": "G02", "locus": "two traces below l'une/l'un",
        "container": (16, 25), "comments": (17, 19), "command": "makebox",
        "report_ids": ["B07", "B08"], "origin": [1125, 790], "baseline": 0,
        "bounds": [0, 0, 40, 24], "scale": ".006cm",
        "attachment": "A terminal percent follows the word's unsure group. The zero-width right-aligned makebox attaches immediately to it; des deux follows the box.",
        "qualification": "The word has its own unsure wrapper; the entire two-fill TikZ group has one unsure wrapper.",
    },
    {
        "reader": "B", "group": "G03", "locus": "detached pair at lower equality endpoint",
        "container": (40, 53), "comments": (45, 46), "command": "mathord",
        "placement": (44, 52), "report_ids": ["B15"],
        "origin": [1616, 1680], "baseline": 0,
        "bounds": [0, 0, 18, 22], "scale": ".012cm",
        "attachment": "A qquad precedes the complete qualified pair inside the lower equality display. The full source container already contains that equality.",
        "qualification": "Both fills share the whole-group unsure wrapper; punctuation role remains unassigned.",
    },
    {
        "reader": "C", "group": "M01", "locus": "two traces below l'une/l'un",
        "container": (6, 16), "comments": (8, 9), "inline": True,
        "report_ids": ["D06", "D07"], "origin": [1124, 790],
        "baseline": "(0,0)", "bounds": [0, 0, 42, 23], "scale": "0.01cm",
        "attachment": "The full inline underset includes hspace{1.5em}, vcenter/hbox, both literal components, and the single complete l'une/l'un word group.",
        "qualification": "Two components share one unsure wrapper; the word has a separate unsure wrapper.",
    },
    {
        "reader": "C", "group": "M02", "locus": "high point and complete first union predecessor",
        "container": (19, 23), "comments": (22, 23), "command": "overset",
        "argument_count": 2, "report_ids": ["D10"], "reported_center": [989, 1047],
        "attachment": "The overset contains one qualified dot and the whole deleted J|jmath body; live K_0 follows outside this complete group.",
        "qualification": "Separate point/body unsure wrappers retain unresolved attachment. The j alternative is dotless jmath in this exact source.",
    },
    {
        "reader": "C", "group": "M03", "locus": "pale trace to left of brace",
        "container": (25, 41), "comments": (27, 28), "command": "vcenter",
        "placement": (26, 35), "report_ids": ["D12"], "origin": [488, 1276],
        "baseline": "(0,0)", "bounds": [0, 0, 28, 40], "scale": "0.01cm",
        "attachment": "The vcenter/hbox/unsure group is followed by quad and then the complete left brace. Its second draw command occupies two physical lines.",
        "qualification": "The full two-path group shares one unsure wrapper; character, role, hand and surface origin remain unassigned.",
    },
    {
        "reader": "C", "group": "M04", "locus": "detached pair at lower equality endpoint",
        "container": (43, 54), "comments": (46, 47), "command": "underset",
        "argument_count": 2, "placement": (45, 53), "report_ids": ["D15"],
        "origin": [1618, 1684], "baseline": "(0,0)",
        "bounds": [0, 0, 16, 19], "scale": "0.01cm",
        "attachment": "The complete underset contains both literal ellipses, vcenter/hbox and the vphantom{Sigma} second argument; qquad precedes it inside the full lower display.",
        "qualification": "Both points share one whole-group unsure wrapper; their role, hand and origin remain unresolved.",
    },
    {
        "reader": "C", "group": "M05", "locus": "point immediately before lower X",
        "container": (43, 56), "comments": (55, 56), "fragment": r"\unsure{\cdot}",
        "report_ids": ["D14"], "reported_center": [728, 1661],
        "attachment": "The exact qualified dot follows the equality and precedes the thin-space command and X; its containing display also holds M04.",
        "qualification": "Point is locally unsure; no operation is supplied in the source.",
    },
]

groups = []
for spec in SPECS:
    r = spec["reader"]
    container = lines(r, *spec["container"])
    if spec.get("inline"):
        s = sources[r]["text"]
        start = s.index("\\(", container["start_char"], container["end_char"])
        end = s.index("\\)", start, container["end_char"]) + 2
        group = span(r, start, end)
    elif "fragment" in spec:
        s = sources[r]["text"]
        start = s.index(spec["fragment"], container["start_char"], container["end_char"])
        group = span(r, start, start + len(spec["fragment"]))
    else:
        group = command(r, spec["command"], container, spec.get("argument_count", 1))
    item = {
        "id": r + "_" + spec["group"], "reader": r,
        "reader_group": spec["group"], "locus": spec["locus"],
        "report_refs": [report_ref(r, row) for row in spec["report_ids"]],
        "complete_container": container, "complete_group": group,
        "comments": lines(r, *spec["comments"]),
        "prefix_in_container": span(r, container["start_char"], group["start_char"]),
        "suffix_in_container": span(r, group["end_char"], container["end_char"]),
        "attachment": spec["attachment"], "qualification": spec["qualification"],
        "literal_components": [], "structural_components": [],
    }
    for name in ("origin", "baseline", "bounds", "scale", "reported_center"):
        if name in spec:
            item["declared_" + name] = spec[name]
    if "placement" in spec:
        item["placement_with_leading_spacing"] = lines(r, *spec["placement"])
    s = sources[r]["text"]
    for m in re.finditer(r"\\(draw|fill|path|node|coordinate)\b.*?;", group["text"], re.DOTALL):
        start = group["start_char"] + m.start()
        component = span(r, start, start + len(m.group(0)))
        component["command"] = m.group(1)
        field = "literal_components" if m.group(1) in ("draw", "fill") else "structural_components"
        component["id"] = item["id"] + "_" + m.group(1) + "_" + str(1 + len(item[field]))
        item[field].append(component)
    for dot_index, m in enumerate(re.finditer(r"\\cdot\b", group["text"]), 1):
        start = group["start_char"] + m.start()
        component = span(r, start, start + len(m.group(0)))
        component["id"] = item["id"] + "_standard_dot_" + str(dot_index)
        component["command"] = "cdot"
        item["literal_components"].append(component)
    groups.append(item)

attention = []


def add_attention(identity, locus, fragments, reporting, note):
    item = {"id": identity, "locus": locus, "sources": {},
            "reporting_scope": reporting, "assembly_attention": note}
    for witness, text in fragments.items():
        item["sources"][witness] = literal(witness, text)
    attention.append(item)


add_attention(
    "L01", "opening abbreviation",
    {"A": "Dém.", "B": r"D\unsure{é|è}m.", "C": "Dém.", "current_C": "Dém.", "H": "Dém."},
    {"A": "No opening-accent row in differences; complete TeX line 2 supplies Dém.",
     "B": report_ref("B", "B01"),
     "C": "No opening-accent row in differences; complete TeX line 2 supplies Dém."},
    "Preserve the selected local acute/grave qualification; a reader's absent difference row supplies no alternate reading.")
add_attention(
    "L02", "cardinality inequality",
    {"A": r"\geqslant 3", "B": r"\geq 3", "C": r"\geq 3", "current_C": r"\geq 3", "H": r"\geq 3"},
    {"A": "No separate differences row; report /notation/0 and reading.md line audit name geqslant.",
     "B": "Complete TeX line 2 and report /notation/0 supply geq.",
     "C": "Complete TeX line 2 and report /notation/0 supply geq."},
    "A's exact macro choice requires an explicit selected-source decision; no ink or count conclusion is assigned here.")
add_attention(
    "L03", "Au before ordinal",
    {"A": r"\deleted{Soit} Au", "B": r"\deleted{Soit} Au", "C": r"\deleted{Soit} Au",
     "current_C": r"\deleted{Soit} Au", "H": r"\struck{Soit} \uncertain{Au}"},
    {"A": "No separate Au difference row; A13 addresses the next word.",
     "B": "No separate Au difference row; B16 addresses the next word.",
     "C": "No separate Au difference row; D16 addresses the next word and its evidence states that Au is readable."},
    "Exact excerpts preserve Soit state as context and the firm/qualified Au source states; counts remain root-owned.")
add_attention(
    "L04", "first overwritten union index",
    {"A": r"\deleted{\unsure{J|j}}K_0", "B": r"\deleted{\unsure{J}}K_0",
     "C": r"\overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}K_0",
     "current_C": r"\deleted{\unsure{J}}K_0", "H": r"\alpha\in K_0"},
    {"A": report_ref("A", "A04"), "B": report_ref("B", "B11"), "C": report_ref("C", "D10")},
    "This adjacent index lies in A G03's complete equality container but outside its literal graphical group.")
add_attention(
    "L05", "complete On a state before donc",
    {"A": r"\unsure{On a|\deleted{On}On a} donc",
     "B": r"\unsure{On a|\deleted{O}On a|\deleted{On}On a} donc",
     "C": r"\unsure{On a|\deleted{On}On a} donc",
     "current_C": r"\unsure{On a} donc",
     "H": r"\struck{On} \uncertain{On a} donc"},
    {"A": report_ref("A", "A05"), "B": report_ref("B", "B13"), "C": report_ref("C", "D13")},
    "Keep all selected complete-state alternatives within one group; do not append another On.")
add_attention(
    "L06", "ordinal after Au",
    {"A": r"\unsure{dernier|deuxième}", "B": r"\unsure{deuxième|dernier}",
     "C": r"\unsure{deuxième|deuxieme|dernier}",
     "current_C": "Au deuxième", "H": r"\uncertain{dernier}"},
    {"A": report_ref("A", "A13"), "B": report_ref("B", "B16"), "C": report_ref("C", "D16")},
    "Candidate order differs in the exact sources.")
add_attention(
    "L07", "sign between borner and sommer",
    {"A": r"borner \unsure{à|:} sommer", "B": r"borner \unsure{:|à} sommer",
     "C": r"borner \unsure{à|:} sommer",
     "current_C": r"borner à \unsure{sommer}", "H": r"borner : \ill{}"},
    {"A": report_ref("A", "A14"), "B": report_ref("B", "B18"), "C": report_ref("C", "D18")},
    "The preceding sign and the sommer word occupy separate loci; each source excerpt preserves their adjacency.")

result = {
    "schema": "scan019-source-candidates-v1",
    "status": "A/B/C released candidates; no selected draft",
    "scope": "Source-only exact spans. No image access, ink adjudication, count assignment, geometry calculation, compilation or rendering.",
    "offset_convention": "Zero-based half-open character and UTF-8 byte offsets; one-based inclusive line numbers.",
    "sources": {
        k: {key: value for key, value in v.items() if key != "text"}
        for k, v in sources.items()
    },
    "preamble": {key: value for key, value in source("out/PREAMBLE.tex").items() if key != "text"},
    "groups": groups,
    "source_attention": attention,
    "assembly_overlap_attention": [
        "A G02's inline group already includes l'une/l'un; B G02's makebox follows its separately qualified word. A selected word/group attachment must preserve the word once.",
        "A G04 and B G03 have containing displays for the same complete lower equality. B G03's exact placement span begins with qquad and contains only its point group/comments; copying both full display containers would repeat the equality.",
        "A G03's complete equality includes J|j, while B's complete equality has J. The graphical group ends before limits, allowing the selected adjacent predecessor to be tracked as its own literal replacement.",
        "A G01's printed unsure group has a drawing primary only; B G01's printed unsure group additionally contains |deleted{=}U. Preserve the root-selected complete group."
        ,
        "C M01 already includes the complete l'une/l'un word. Its hspace/underset/vcenter/hbox and the chosen word must travel together.",
        "C M02 contains the whole predecessor plus one point; selecting M02 together with another complete predecessor would duplicate that body and may duplicate the j dot.",
        "C M03's second draw command spans two source lines; its quad and following brace placement are separately captured.",
        "C M04 and M05 share one containing lower display. Each has its own exact local group; M04's placement includes qquad and vphantom{Sigma}."
    ],
    "processing_provenance": {
        "transient_read_failure": "One initial three-call text-read batch failed before delivery with exec-server transport disconnected. A narrow H.tex read then succeeded; allowed text reads resumed. No image requests occurred.",
        "release_rule": "Independent reader C inspected only after root explicitly released its complete frozen return.",
    },
}

out_json = OUT / "scan019_tex_candidates.json"
out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
md = [
    "# scan019 source-only TeX candidates",
    "",
    "A/B/C are released. Root owns every ink selection and count. Exact complete groups, containing blocks, literal commands and UTF-8 offsets are in scan019_tex_candidates.json.",
    "",
    "| Group | Exact source lines | Literal components | Declared origin / baseline | Attachment |",
    "| --- | --- | --- | --- | --- |",
]
for g in groups:
    x = g["complete_group"]
    origin = str(g.get("declared_origin", "standard TeX placement"))
    baseline = str(g.get("declared_baseline", "not declared"))
    commands = ", ".join(c["command"] for c in g["literal_components"])
    md.append(f"| {g['id']} | {x['path']}:{x['start_line']}–{x['end_line']} | {commands} | {origin} / {baseline} | {g['attachment']} |")
md += ["", "## Report-silent or adjacent source choices", ""]
for a in attention:
    md.append(f"- {a['id']} — {a['locus']}: {a['assembly_attention']}")
md += ["", "## Overlap attention", ""]
md += ["- " + s for s in result["assembly_overlap_attention"]]
md += [
    "",
    "The map preserves every literal draw/fill and the separate bounding-box, node or coordinate source commands. Declared coordinates and scales are copied from source. No rendered or metric validation is claimed.",
    "",
    "Current preamble is recorded by hash and remains unchanged. No final draft has been assembled.",
]
(OUT / "scan019_tex_candidates.md").write_text("\n".join(md) + "\n")
print(json.dumps({"json": str(out_json), "sha256": sha(out_json.read_bytes()),
                  "groups": len(groups), "source_attention": len(attention),
                  "literal_components": sum(len(x["literal_components"]) for x in groups)},
                 ensure_ascii=False))
