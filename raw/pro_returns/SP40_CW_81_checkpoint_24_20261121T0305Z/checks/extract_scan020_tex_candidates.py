"""Source-only extraction for scan020; no image, geometry or TeX execution."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"


def sha(data):
    return hashlib.sha256(data).hexdigest()


paths = {r: f"out/readers/020/{r}/reading.tex" for r in "ABC"}
paths.update(C_packet="packets/020/C.tex", H="packets/020/H.tex")
texts = {r: (ROOT / p).read_text(encoding="utf-8") for r, p in paths.items()}
reports = {r: json.loads((ROOT / f"out/readers/020/{r}/report.json").read_text()) for r in "ABC"}
sources = {}
for p in [*paths.values(), "out/PREAMBLE.tex", "out/briefs/source_record_brief_v02.md",
          "out/checks/scan020_C_doubt_catalog.json", "packets/020/C_doubts.txt",
          "packets/020/C_inventory.json", "packets/020/S_rows.json"] + [
          f"out/readers/020/{r}/{name}" for r in "ABC" for name in
          ("report.json", "reading.md", "image_audit.json")
          ] + ["out/readers/020/A/source_checks.json", "out/readers/020/B/source_audit.json",
               "out/readers/020/C/source_audit.json"]:
    b = (ROOT / p).read_bytes()
    sources[p] = {"path": p, "sha256_utf8": sha(b), "utf8_byte_length": len(b),
                  "unicode_character_length": len(b.decode("utf-8")), "immutable_input": True}


def scope(r, start, end):
    t = texts[r]
    assert 0 <= start <= end <= len(t)
    return {"path": paths[r], "source_sha256_utf8": sources[paths[r]]["sha256_utf8"],
            "char_start": start, "char_end": end,
            "utf8_byte_start": len(t[:start].encode("utf-8")),
            "utf8_byte_end": len(t[:end].encode("utf-8")),
            "line_start": t.count("\n", 0, start) + 1,
            "line_end": t.count("\n", 0, max(start, end-1)) + 1,
            "literal": t[start:end]}


def literal(r, s, occurrence=0, after=None):
    t = texts[r]
    pos = 0 if after is None else t.index(after) + len(after)
    for _ in range(occurrence + 1):
        start = t.index(s, pos)
        pos = start + len(s)
    return scope(r, start, start + len(s))


def between(r, first, following, occurrence=0, include_following=False):
    s = literal(r, first, occurrence)["char_start"]
    e = texts[r].index(following, s + len(first))
    if include_following:
        e += len(following)
    return scope(r, s, e)


def statement_end(t, pos):
    depth = 0
    i = pos
    while i < len(t):
        ch = t[i]
        escaped = i > 0 and t[i-1] == "\\"
        if ch == "{" and not escaped:
            depth += 1
        elif ch == "}" and not escaped:
            depth -= 1
        elif ch == ";" and depth == 0:
            return i+1
        i += 1
    raise ValueError("Unterminated source statement")


def brace_end(t, opening):
    depth = 0
    for i in range(opening, len(t)):
        if t[i] == "{" and (i == 0 or t[i-1] != "\\"):
            depth += 1
        elif t[i] == "}" and (i == 0 or t[i-1] != "\\"):
            depth -= 1
            if depth == 0:
                return i+1
    raise ValueError("Unterminated source macro")


def commands_in(r, sp, names, terminated=True):
    t = texts[r]
    found = []
    pat = r"\\(" + "|".join(names) + r")\b"
    for m in re.finditer(pat, sp["literal"]):
        a = sp["char_start"] + m.start()
        # All candidate drawing commands begin after a newline or a TeX command,
        # while comment-only mentions are retained in full_source, not counted.
        line_start = t.rfind("\n", 0, a) + 1
        if "%" in t[line_start:a]:
            continue
        if terminated:
            b = statement_end(t, a)
        else:
            opening = t.index("{", a)
            b = brace_end(t, opening)
        assert b <= sp["char_end"]
        q = scope(r, a, b)
        q["command"] = m.group(1)
        found.append(q)
    return found


group_specs = [
    ("A", "A020-G01", "% A020-G01:", "\n$U_{J,i}$", [],
     "Cancelled Sigma/index and both cancellation runs; following U is outside."),
    ("A", "A020-G02", "% A020-G02:", "\nde $", [],
     "Point only; voisinage and de remain outside."),
    ("A", "A020-G03", "% A020-G03:", "\n$(n-1)", ["tout|est"],
     "Cancelled word and its two crossing runs; en and the class count remain outside."),
    ("A", "A020-G04", "% A020-G04:", "\n\\unsure{dém.", [],
     "Point only; la and the abbreviation remain outside."),
    ("A", "A020-G05", "% A020-G05:", "\noù $K$", [],
     "Complete X setminus generic bigcup formula, parenthesized body, hatted label, and two literal brace paths; de la forme and où remain outside."),
    ("A", "A020-G06", "% A020-G06:", "\net\n", ["non vide", "de $I$,"],
     "Inserted/cancelled non vide plus adjoining de I,; partie and et remain outside."),
    ("A", "A020-G07", "% A020-G07:", "\n\\pi_0", [],
     "Relation paths and overlay phantom complete-state annotation; Sigma and pi_0 remain outside."),
    ("B", "B_G01", "% B_G01:", "\n$U_{J,i}$", [],
     "Cancelled Sigma/index and two cancellation runs; following U is outside."),
    ("B", "B_G02", "% B_G02:", "\n\\unsure{dèm.", ["la"],
     "la and qualified inner point group; adverb and abbreviation remain outside. Inner origin translation is literal (66,18)."),
    ("B", "B_G03", "% B_G03:", "\noù $K$", [],
     "Transplant block includes $X\\setminus\\text{...}$; inner TikZ owns literal union, qualified index, parenthesized body, hatted label, and brace. X setminus is outside the inner TikZ but inside this full source block."),
    ("B", "B_G04", "% B_G04 contains", "\n% slanted;", ["partie", "non vide", "de $I$, et"],
     "partie, inserted/cancelled non vide, and de I, et; une remains outside."),
    ("B", "B_G05", "% B_G05 literal", "\n\\pi_0", [],
     "Relation paths followed by formal complete-state alternatives visibly inside the same unsure wrapper; Sigma and pi_0 remain outside."),
    ("B", "B_MARGIN", "% slanted;", "\n$\\forall", [r"$K$ est $\ne\varnothing$", r"si $I\ne\varnothing$"],
     "Complete slanted margin note; the source supplies a TikZ node rotate=19 with base-west anchor, but no source origin, fixed rectangle or explicit baseline declaration."),
    ("C", "C_G01--G02", "% G01--G02:", "\noù $K$", [],
     "Complete X, setminus, literal union and qualified index, parenthesized body, hatted label, and brace; adjoining French words remain outside."),
    ("C", "C_G03--G04", "% G03--G04:", "\net\n", ["partie", "de $I$,", "non vide"],
     "partie, de I, with its comma, and inserted/cancelled non vide; et remains outside."),
]
groups = []
by_id = {}
for r, gid, first, following, words, boundary in group_specs:
    sp = between(r, first, following)
    raw = reports[r].get("graphics", reports[r].get("graphic_groups", reports[r]["notes"].get("graphic_groups", [])))
    report_group = None
    report_pointer = None
    root_key = "graphics" if "graphics" in reports[r] else "graphic_groups" if "graphic_groups" in reports[r] else "notes/graphic_groups"
    for i, g in enumerate(raw):
        if g.get("id", g.get("group")) == gid or "C_" + g.get("group", "") == gid:
            report_group, report_pointer = g, f"/{root_key}/{i}"
            break
    decl = []
    options = []
    for m in re.finditer(r"(?m)^.*$", sp["literal"]):
        line = m.group()
        if line.startswith("%"):
            decl.append(scope(r, sp["char_start"] + m.start(), sp["char_start"] + m.end()))
        if "\\begin{tikzpicture}" in line:
            options.append(scope(r, sp["char_start"] + m.start(), sp["char_start"] + m.end()))
    q = {"id": gid, "reader": r, "status": "candidate_only_no_root_ink_choice",
         "full_source": sp, "complete_word_bearing_boundary": boundary,
         "word_bearing_contents": words, "source_comments": decl,
         "tikz_declaration_lines": options,
         "literal_draw_fill_commands": commands_in(r, sp, ["draw", "fill"]),
         "bounding_source_commands": commands_in(r, sp, ["path", "useasboundingbox"]),
         "node_source_commands": commands_in(r, sp, ["node"]),
         "phantom_annotations": commands_in(r, sp, ["phantom"], False),
         "rlap_visible_payloads": commands_in(r, sp, ["rlap"], False),
         "raw_report_group": report_group,
         "raw_report_reference": {"path": f"out/readers/020/{r}/report.json", "json_pointer": report_pointer},
         "root_ink_choice_applied": False}
    groups.append(q)
    by_id[gid] = q


def G(gid):
    return by_id[gid]["full_source"]


loci = []


def add(lid, label, readings, parts=(), notes=()):
    assert set(readings) >= set("ABC")
    loci.append({"id": lid, "location": label, "readers": {r: readings[r] for r in "ABC"},
                 "witnesses": {r: readings[r] for r in readings if r not in "ABC"},
                 "C_source_part_ids": list(parts), "source_only_notes": list(notes),
                 "root_ink_choice_applied": False, "root_selection": None})


add("TEX020-01", "Opening Pi_I superscript",
    {r: literal(r, r"\Pi_I^{\unsure{\circ|0}}") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H", r"\Pi_I^0")}, ["C020-R01-1"])
add("TEX020-02", "Opening Pi_J superscript",
    {r: literal(r, r"\Pi_J^\circ") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H", r"\Pi_J^0")}, ["C020-R01-2"],
    ["All three readers print only the recurring primary; the reader reports retain their local circle/zero doubts."])
add("TEX020-03", "Overwritten Pi/U after distinctes de",
    {r: literal(r, r"$\deleted{\Pi}U_{J,i}$,") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H", r"$U_{J,i}$,")})
add("TEX020-04", "Word and terminal point before parmi",
    {r: between(r, "et de plus les", " parmi", include_following=True) for r in texts},
    ["C020-R02-1"],
    ["A and B print clas.|deux. with the terminal point inside each candidate. C prints deux|clas with one terminal point outside the wrapper. C_packet includes the point only in clas.; H prints deux without a point."])
add("TEX020-05", "Complete first paired display and first Sigma index order",
    {r: between(r, "\\[", "\\]", include_following=True) for r in texts}, ["C020-R03-1"],
    ["A orders j|deleted J i|i. B and C order deleted J i|j|i. Preserve the actual source spacing macros with whichever full source is chosen."])
add("TEX020-06", "Cancelled Sigma/index and its cancellation source",
    {"A":G("A020-G01"), "B":G("B_G01"), "C":literal("C", r"$\deleted{\Sigma_{\unsure{j|i}}}$"),
     "C_packet":literal("C_packet", r"\deleted{$\unsure{\Sigma_i|\Sigma_j}$}"), "H":literal("H", r"\struck{\ill{}}")},
    ["C020-R04-1"],
    ["A qualifies the index inside Sigma; B qualifies complete Sigma_j/Sigma_i candidates. Both use a visible rlap payload, invisible deletion annotation and two literal crossing commands. C uses the generic deleted macro."])
add("TEX020-07", "voisinage through de E and et; small-point source scope",
    {r: between(r, "$U_{J,i}$ est un voisinage", ", et", include_following=True) for r in ["A","B","C","C_packet"]} |
    {"H":literal("H", r"$U_{J,i}$ est un voisinage de $E_i$ et")}, ["C020-R05-1"],
    ["A includes the separate qualified A020-G02 point. B and C contain no TikZ/draw/fill command within their exact supplied phrase scopes. A/B qualify i|j on E; C prints E_i. The three reader sources all retain deleted Sigma before E and the comma."])
add("TEX020-08", "Complete two barred nonemptiness formulas",
    {r: between(r, "\\[", "\\]", occurrence=1, include_following=True) for r in ["A","B","C","C_packet"]} |
    {"H":between("H", r"$\overline{\Sigma_i^+}", " On voit")},
    notes=["The two overline commands occur in all current C/H source scopes. This extraction supplies no visual confirmation or correction count."])
add("TEX020-09", "Verb after On and live en before cancelled word",
    {r:literal(r,"On sait donc que le nb des classes est en") for r in "ABC"} |
    {"C_packet":literal("C_packet",r"On \unsure{voit|sait} donc que le nb des classes est en"),
     "H":literal("H","On voit donc que le nb des\nclasses est")}, ["C020-R10-1"])
add("TEX020-10", "Cancelled tout/est after en",
    {"A":G("A020-G03"), **{r:literal(r,r"\deleted{\unsure{tout|est}}") for r in ["B","C","C_packet"]},
     "H":literal("H",r"\struck{\ill{}}",occurrence=1)}, ["C020-R06-1"],
    ["A uses a visible unsure word, phantom deletion annotation and two literal runs. B/C use the generic deleted macro."])
add("TEX020-11", "Written class count",
    {r:literal(r,r"$(n-1)+2=n+1=\operatorname{card} I+1$") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H",r"$(n-1)+2 = n+1 = \operatorname{card}I+1$")},
    notes=["Exact written statement only; no arithmetic or mathematical verification."])
add("TEX020-12", "Parenthesis opening ce qui achève and adverb",
    {r:literal(r,r"(ce qui achève \unsure{aussi|ainsi}") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H","(ce qui achève aussi")}, ["C020-R11-1"])
add("TEX020-13", "la and adjoining small-mark source scope",
    {"A":between("A",r"\unsure{aussi|ainsi} la",r"\unsure{dém.|dem.}"),
     "B":G("B_G02"), "C":literal("C",r"\unsure{aussi|ainsi} la \unsure{dèm.|dém.|dem.}"),
     "C_packet":literal("C_packet",r"\unsure{aussi|ainsi} la \unsure{dém.|dem.}"),
     "H":literal("H",r"aussi la dém.\ par")},
    notes=["A's graphical group owns only the point; la remains outside. B's complete graphical group owns la and a translated nested point picture. C's exact inspected phrase contains la and no separate point command."])
add("TEX020-14", "Abbreviation accent candidates and following par/p",
    {"A":literal("A",r"\unsure{dém.|dem.} \unsure{par|p} récurrence sur le nb des classes)."),
     **{r:literal(r,r"\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).") for r in "BC"},
     "C_packet":literal("C_packet",r"\unsure{dém.|dem.} par récurrence sur le nb des classes)."),
     "H":literal("H","dém.\\ par\nrécurrence sur le nb des classes).")}, ["C020-R07-1"],
    ["A retains acute/unaccented candidates and qualifies par|p with no point on p. B/C retain grave/acute/unaccented candidates and print par unqualified."])
add("TEX020-15", "Lemma Pi_I superscript and adjoining heading",
    {r:literal(r,r"\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H",r"\emph{Lemme} Toute classe de $\Pi_I^0$ est de la forme")}, ["C020-R01-3"])
add("TEX020-16", "Complete union/brace/formula candidate blocks",
    {"A":G("A020-G05"), "B":G("B_G03"), "C":G("C_G01--G02"),
     "C_packet":scope("C_packet",texts["C_packet"].index(r"$X\setminus"),texts["C_packet"].index("$ où")+1),
     "H":between("H",r"\[" , r"\]", occurrence=1,include_following=True)},
    ["C020-R08-1"],
    ["A uses a generic bigcup plus two literal brace paths; B has three union and three brace commands; C has two union and two brace commands. These counts describe source commands only.",
     "B full transplant source includes X setminus outside its inner TikZ. C comment mentions an operator annotation, while the complete inspected group contains no phantom or bigcup annotation command."])
add("TEX020-17", "Union index predecessor/state candidates",
    {"A":literal("A",r"\alpha\in\deleted{I}K"),
     **{r:literal(r,r"\alpha\in\unsure{\deleted{I}K|K}") for r in "BC"},
     "C_packet":literal("C_packet",r"\alpha\in\deleted{\unsure{I}}K"),
     "H":literal("H",r"\alpha\in K")}, ["C020-R08-1"])
add("TEX020-18", "Cancelled non vide with guide and adjoining words",
    {"A":G("A020-G06"), "B":G("B_G04"), "C":G("C_G03--G04"),
     "C_packet":literal("C_packet",r"où $K$ est une partie \inserted{\deleted{non vide}} de $I$, et"),
     "H":literal("H",r"où $K$ est une partie \add{\uncertain{non vide}} de $I$, et")},
    notes=["A owns non vide and de I, only. B owns partie, non vide and de I, et. C owns partie, non vide and de I, with et outside.",
           "A's rlap includes inserted{non vide}; A's phantom includes inserted{deleted{non vide}}. B/C place inserted outside a visible rlap and a phantom{deleted{non vide}}. Preserve the exact selected wrapper."])
add("TEX020-19", "Slanted margin-note source construction",
    {r:between(r,r"\reversemarginpar",r"\normalmarginpar",include_following=True) for r in ["A","B","C","C_packet"]} |
    {"H":literal("H",r"\marginal{$K$ est $\neq\emptyset$ si $I\neq\emptyset$}")},
    notes=["A uses rotatebox{19} inside a makebox; B uses a TikZ node rotate=19; C uses rotatebox{23} inside a makebox. These literal source constructions are preserved without geometric evaluation."])
add("TEX020-20", "Cancelled on a and preceding quantifier",
    {r:literal(r,r"$\forall\alpha\in K$, \deleted{on a}") for r in ["A","B","C","C_packet"]} |
    {"H":literal("H",r"$\forall\alpha\in K$, \struck{\ill{}}")})
add("TEX020-21", "Reworked relation before pi_0",
    {"A":G("A020-G07"), "B":G("B_G05"),
     "C":literal("C",r"\unsure{\deleted{\Rightarrow}\in|\deleted{\rightarrow}\in|\in}"),
     "C_packet":literal("C_packet",r"\deleted{\unsure{\Rightarrow}}\in"),
     "H":literal("H",r"\Sigma_\alpha^+\in\pi_0")}, ["C020-R09-1"],
    ["A's complete-state candidates appear in its comment and overlay phantom; only locally qualified paths occupy the graphic payload. B prints the drawing and pipe-separated formal candidates inside one unsure wrapper. C prints only three formal candidates, using rightarrow rather than the to macro in A/B. Exact macro identity is retained."])
add("TEX020-22", "Lower E_alpha predecessor/state inside pi_0 argument",
    {"A":literal("A",r"\pi_0(X\setminus{\unsure{E|\deleted{\Sigma}E}}_\alpha)"),
     **{r:literal(r,r"\pi_0(X\setminus E_\alpha)") for r in ["B","C","C_packet","H"]}},
    notes=["A qualifies E versus deleted-Sigma-plus-E. The other four inspected exact scopes contain E_alpha and no deleted predecessor macro."])
add("TEX020-23", "Final quantified hatted condition and parenthetical relation",
    {r:between(r,"tels que", "\n% archive") for r in ["A","B","C","C_packet"]} |
    {"H":between("H","tels que","\n\\marginal")},
    notes=["All final text and displayed relations remain author-attributed transcription; this extraction performs no proof check."])

catalog = json.loads((ROOT / "out/checks/scan020_C_doubt_catalog.json").read_text())
risks = [
    "No root ink choice, confidence, correction count, original C outcome, or approval is supplied by this extraction.",
    "Word-bearing group boundaries differ. Transplanting a selected group requires deleting its own overlapping prose exactly once, particularly B_G02 la and A/B/C non-vide groups.",
    "A and B cancelled-Sigma groups carry invisible deletion annotations with different qualifier scopes; C uses a generic deleted macro. Retaining generic cancellation beside selected literal crossing commands would duplicate the source treatment.",
    "A alone has a graphical cancelled tout/est group, a detached point after voisinage, a par|p qualifier, and a lower E/deleted-Sigma-E qualification.",
    "B's relation alternatives follow the graphic as visible qualifier content; A stores complete states in an overlay phantom; C supplies formal alternatives. Moving between these exact sources requires a root-selected qualifier/annotation strategy.",
    "The C union comment says an annotation identifies the operator, but the inspected complete source block has no such phantom/bigcup annotation command. This is a source-comment discrepancy, awaiting root handling.",
    "Source origins, baselines, scales, rectangles, translations and path coordinates are copied literally. No image correspondence, metric result or rendered validation is asserted.",
    "A/B source point groups at la must not be combined with a separately retained copy of la when the selected complete group already owns that word.",
    "Final source-map attachments must bind the exact final draft hash and use checks/scan020_final_draft.tex relative to out, with out/checks/scan020_final_draft.tex retained as the workspace-relative alias."
]
result = {"scan":20, "status":"candidate_extraction_complete_pending_root_choices",
          "scope":"Source-only current-page extraction. No images, OCR, web, compilation, rendering, installation, delegation, mathematical computation or coordinate calculation.",
          "offset_convention":"Zero-based half-open Unicode character offsets; UTF-8 byte offsets are additionally recorded. Literal spans include their original whitespace.",
          "sources":sources, "graphic_groups":groups, "textual_and_qualifier_loci":loci,
          "original_C_doubt_catalog":{"path":"out/checks/scan020_C_doubt_catalog.json",
                                     "sha256_utf8":sources["out/checks/scan020_C_doubt_catalog.json"]["sha256_utf8"],
                                     "actual_source_rows":catalog["actual_source_rows"],
                                     "primary_parts":catalog["primary_parts"],
                                     "identity_map":[{"source_id":x["source_id"],"part_ids":[p["part_id"] for p in x["source_parts"]]} for x in catalog["rows"]]},
          "raw_reader_graphic_metadata_preserved":True,
          "source_command_totals":{r:sum(len(g["literal_draw_fill_commands"]) for g in groups if g["reader"]==r) for r in "ABC"},
          "unresolved_source_risks":risks,
          "main_adjudicated":False, "main_approved":False}

# One lexical extraction audit: every stored exact scope resolves to the unchanged source.
checked = 0
def walk(x):
    global checked
    if isinstance(x,dict):
        if {"path","char_start","char_end","literal"} <= x.keys():
            p = ROOT / x["path"]
            t = p.read_text(encoding="utf-8")
            assert t[x["char_start"]:x["char_end"]] == x["literal"]
            assert sha(p.read_bytes()) == x["source_sha256_utf8"]
            checked += 1
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(result)
result["extraction_audit"]={"scope":"Exact source-span and source-hash checks only", "exact_spans_checked":checked,
                            "all_exact_spans_resolve":True, "original_reader_files_modified":False,
                            "images_opened":0,"rendering_performed":False,"coordinate_calculation_performed":False}
dest = OUT / "scan020_tex_candidates.json"
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

md = ["# Scan020 exact TeX candidates", "", "Status: candidate extraction complete; every ink, uncertainty, count and final selection remains with root.", "",
      result["offset_convention"], "", "No image or graphical metric was inspected or calculated. All geometry below is literal source.", "",
      "## Source risks", ""]
md += [f"- {x}" for x in risks]
md += ["", "## Complete graphical candidate blocks", ""]
for g in groups:
    sp = g["full_source"]
    md += [f"### {g['id']}", "", g["complete_word_bearing_boundary"], "",
           f"Source: `{sp['path']}` characters `[{sp['char_start']},{sp['char_end']})`; lines {sp['line_start']}–{sp['line_end']}. UTF-8 SHA-256: `{sp['source_sha256_utf8']}`.", "",
           f"Draw/fill commands: {len(g['literal_draw_fill_commands'])}. Phantom annotations: {len(g['phantom_annotations'])}. Full node and literal path spans are individually indexed in the JSON.", "",
           "```tex",sp["literal"],"```",""]
md += ["## Textual and qualifier crosswalk", ""]
for l in loci:
    md += [f"### {l['id']} — {l['location']}", ""]
    if l["C_source_part_ids"]:
        md += ["Original C parts: " + ", ".join(f"`{x}`" for x in l["C_source_part_ids"])+".", ""]
    for n in l["source_only_notes"]: md += [n, ""]
    for r,sp in (l["readers"] | l["witnesses"]).items():
        md += [f"**{r}** — `{sp['path']}` characters `[{sp['char_start']},{sp['char_end']})`.", "",
               "```tex",sp["literal"],"```",""]
md += ["## Extraction audit", "", f"All {checked} exact stored source spans resolve, with unchanged input hashes. No reader file was modified.", "",
       "Original C catalog: 11 actual rows, 13 primary parts. Its original row/part IDs remain intact in the JSON.", ""]
(OUT / "scan020_tex_candidates.md").write_text("\n".join(md),encoding="utf-8")
print(json.dumps({"json":str(dest.relative_to(ROOT)),"markdown":"out/checks/scan020_tex_candidates.md",
                  "groups":len(groups),"loci":len(loci),"exact_spans_checked":checked,
                  "source_command_totals":result["source_command_totals"],"json_sha256_utf8":sha(dest.read_bytes())},indent=2))
