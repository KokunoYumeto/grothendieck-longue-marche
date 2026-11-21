"""Exact selected-source assembly for scan019; root owns ink and count choices."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path("/workspace/scratch/94548b74fbe0")
OUT = ROOT / "out/checks"
SELECTIONS_COMPLETE = True


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


source_paths = {
    "A": "out/readers/019/A/reading.tex",
    "B": "out/readers/019/B/reading.tex",
    "C": "out/readers/019/C/reading.tex",
    "ROOT-G01": "out/checks/scan019_root_graphics.tex",
    "ROOT-G02": "out/checks/scan019_root_brace.tex",
}
sources = {key: (ROOT / path).read_bytes().decode("utf-8") for key, path in source_paths.items()}
candidate_map = json.loads((OUT / "scan019_tex_candidates.json").read_text())
candidate_groups = {row["id"]: row for row in candidate_map["groups"]}
for reader in ("A", "B", "C"):
    assert digest(sources[reader]) == candidate_map["sources"][reader]["sha256"]
assert digest(sources["ROOT-G01"]) == "acaf3e641f2d281dbda6380ff5a5a4e8eb48b0f6a99fb75348a69b8910cb490a"
assert digest(sources["ROOT-G02"]) == "f5b5d7aab26a284f1c0dad18eeeedf7a0b1eacf4b8f5ccc4446a5e6c2fdea797"


def raw_piece(source_id, char_start=0, char_end=None):
    text = sources[source_id]
    if char_end is None:
        char_end = len(text)
    assert 0 <= char_start <= char_end <= len(text)
    return {"source_id": source_id, "source_char_start": char_start,
            "source_char_end": char_end, "text": text[char_start:char_end]}


def structural_piece(text, reason):
    return {"source_id": None, "structural_reason": reason, "text": text}


def source_literal(source_id, literal, occurrence=0):
    text = sources[source_id]
    positions = [m.start() for m in re.finditer(re.escape(literal), text)]
    assert len(positions) > occurrence, (source_id, literal, positions)
    start = positions[occurrence]
    return raw_piece(source_id, start, start + len(literal))


def source_lines(source_id, first, last):
    lines = sources[source_id].splitlines(keepends=True)
    return raw_piece(source_id, sum(map(len, lines[:first-1])),
                     sum(map(len, lines[:last])))


def candidate_piece(group_id, field="complete_group"):
    row = candidate_groups[group_id][field]
    reader = candidate_groups[group_id]["reader"]
    piece = raw_piece(reader, row["start_char"], row["end_char"])
    assert piece["text"] == row["text"]
    assert digest(piece["text"]) == row["text_sha256"]
    return piece


pieces = [raw_piece("B")]
replacements = []


def current_text():
    return "".join(piece["text"] for piece in pieces)


def slice_pieces(start, end):
    result = []
    cursor = 0
    for piece in pieces:
        stop = cursor + len(piece["text"])
        left, right = max(cursor, start), min(stop, end)
        if left < right:
            copy = dict(piece)
            offset = left - cursor
            copy["text"] = piece["text"][offset:offset + right - left]
            if copy["source_id"] is not None:
                copy["source_char_start"] += offset
                copy["source_char_end"] = copy["source_char_start"] + len(copy["text"])
            result.append(copy)
        cursor = stop
    assert "".join(p["text"] for p in result) == current_text()[start:end]
    return result


def replace_literal(identity, old_text, new_pieces, decision_ids):
    global pieces
    text = current_text()
    positions = [m.start() for m in re.finditer(re.escape(old_text), text)]
    assert len(positions) == 1, (identity, len(positions), old_text)
    start = positions[0]
    end = start + len(old_text)
    removed = slice_pieces(start, end)
    replacement_text = "".join(p["text"] for p in new_pieces)
    replacements.append({
        "id": identity, "decision_ids": decision_ids,
        "stage_char_start": start, "stage_char_end": end,
        "old_text": old_text, "new_text": replacement_text,
        "removed_source_pieces": removed,
        "inserted_source_pieces": new_pieces,
    })
    pieces = slice_pieces(0, start) + new_pieces + slice_pieces(end, len(text))
    assert current_text() == text[:start] + replacement_text + text[end:]


# L019-03 replaces only the second cardinality operator. Its I=2 continuation
# comes from the unchanged B source and remains outside the complete graphic.
second_card = source_literal("B", r"$\operatorname{card} I=2$")
start = second_card["source_char_start"]
operator_start = start + 1
operator_end = operator_start + len(r"\operatorname{card}")
replace_literal(
    "ROOT-G01-second-card", second_card["text"],
    [raw_piece("B", start, operator_start),
     structural_piece("\n", "Physical line boundary before the exact root source comments; no paragraph blank."),
     raw_piece("ROOT-G01"),
     raw_piece("B", operator_end, second_card["source_char_end"])],
    ["L019-03"],
)
replace_literal("L019-06-inequality", r"\geq 3",
                [source_literal("A", r"\geqslant 3")], ["L019-06"])

# The selected complete C_M01 inline word-and-mark group occurs once.
replace_literal(
    "C_M01-word-and-two-traces", source_lines("B", 16, 25)["text"],
    [source_lines("C", 6, 16)], ["L019-09", "L019-10", "L019-11"],
)

# First operator and its adjacent predecessor are selected separately.
replace_literal(
    "A_G03-first-operator", r"\mathop{\unsure{\coprod|\bigsqcup}}",
    [candidate_piece("A_G03")], ["L019-13"],
)
first_prefix = source_literal("B", "\\[\n" + r"U_{J,i}=X\setminus")
replace_literal(
    "A_G03-source-comments", first_prefix["text"],
    [candidate_piece("A_G03", "comments"), first_prefix], ["L019-13"],
)
replace_literal(
    "C_M02-predecessor-and-point", r"\deleted{\unsure{J}}",
    [candidate_piece("C_M02")], ["L019-14", "L019-15"],
)
first_tail = source_literal("B", r"K_0}\widehat{\Sigma}_\alpha^+" + "\n\\]\n")
replace_literal(
    "C_M02-source-comments", first_tail["text"],
    [first_tail, candidate_piece("C_M02", "comments")], ["L019-14", "L019-15"],
)

# C_M03's adjacent quad is retained. ROOT-G02 replaces the standard brace;
# all original aligned condition source lines remain in the piece table.
replace_literal(
    "C_M03-and-ROOT-G02-brace", r"\left\{",
    [candidate_piece("C_M03", "placement_with_leading_spacing"), raw_piece("ROOT-G02")],
    ["L019-17", "L019-18"],
)
replace_literal("remove-invisible-brace-delimiter", r"\right.", [], ["L019-18"])

# The second recurring operator keeps A's unqualified complete graphical
# group. Its literal limits command is copied from the same source.
replace_literal(
    "A_G04-second-operator", r"\coprod_{\alpha\in K_0}",
    [candidate_piece("A_G04"), source_literal("A", r"\limits_{\alpha\in K_0}")],
    ["L019-20"],
)
second_prefix = source_literal("B", "\\[\n% The later footed join")
replace_literal(
    "A_G04-source-comments", second_prefix["text"],
    [candidate_piece("A_G04", "comments"), second_prefix], ["L019-20"],
)
pre_x = source_literal("B", r"U=U_{J,i}\cap\Sigma_i^-=X")
pre_x_without_x = raw_piece("B", pre_x["source_char_start"], pre_x["source_char_end"] - 1)
replace_literal(
    "C_M05-point-before-X", pre_x["text"],
    [pre_x_without_x, source_literal("C", r"\unsure{\cdot}\,"),
     raw_piece("B", pre_x["source_char_end"] - 1, pre_x["source_char_end"])],
    ["L019-21"],
)

replace_literal(
    "C_M04-complete-endpoint-pair",
    candidate_piece("B_G03", "placement_with_leading_spacing")["text"],
    [candidate_piece("C_M04", "placement_with_leading_spacing")],
    ["L019-22"],
)
lower_close = source_literal("B", "\\]\n" + r"\deleted{Soit}")
close_end = lower_close["source_char_start"] + len("\\]\n")
replace_literal(
    "C_M05-source-comments", lower_close["text"],
    [raw_piece("B", lower_close["source_char_start"], close_end),
     candidate_piece("C_M05", "comments"),
     raw_piece("B", close_end, lower_close["source_char_end"])],
    ["L019-20", "L019-21"],
)
replace_literal(
    "L019-24-complete-ordinal", r"\unsure{deuxième|dernier}",
    [source_literal("C", r"\unsure{deuxième|deuxieme|dernier}")],
    ["L019-24"],
)
replace_literal(
    "L019-26-borner-sign", r"\unsure{:|à}",
    [source_literal("C", r"\unsure{à|:}")], ["L019-26"],
)

# Remaining root loci will be added here before this flag is released.
if not SELECTIONS_COMPLETE:
    raise SystemExit("Root selections remain pending; no final draft or map written.")

FINAL_REL = "out/checks/scan019_final_draft.tex"
MAP_REL = "out/checks/scan019_final_source_map.json"
final_text = current_text()
final_sha = digest(final_text)


def final_span(start, end, identity=None):
    assert 0 <= start <= end <= len(final_text)
    text = final_text[start:end]
    result = {
        "path": FINAL_REL, "manifest": MAP_REL,
        "char_start": start, "char_end": end,
        "byte_start": len(final_text[:start].encode("utf-8")),
        "byte_end": len(final_text[:end].encode("utf-8")),
        "line_start": final_text.count("\n", 0, start) + 1,
        "line_end": final_text.count("\n", 0, max(start, end - 1)) + 1,
        "excerpt": text, "literal_sha256_utf8": digest(text),
        "final_file_sha256": final_sha,
    }
    if identity:
        result["attachment_id"] = identity
    return result


def find_final(literal, identity=None, within=None, occurrence=None):
    start, end = (0, len(final_text)) if within is None else within
    matches = [start + m.start() for m in re.finditer(re.escape(literal), final_text[start:end])]
    if occurrence is None:
        assert len(matches) == 1, (identity, literal, matches)
        index = matches[0]
    else:
        assert len(matches) > occurrence, (identity, literal, matches)
        index = matches[occurrence]
    return final_span(index, index + len(literal), identity)


def original_span(piece):
    if piece["source_id"] is None:
        return {"kind": "structural separator", "reason": piece["structural_reason"],
                "excerpt": piece["text"], "literal_sha256_utf8": digest(piece["text"])}
    source_id = piece["source_id"]
    text = sources[source_id]
    start, end = piece["source_char_start"], piece["source_char_end"]
    assert text[start:end] == piece["text"]
    return {
        "source_id": source_id, "path": source_paths[source_id],
        "source_file_sha256": digest(text),
        "char_start": start, "char_end": end,
        "byte_start": len(text[:start].encode("utf-8")),
        "byte_end": len(text[:end].encode("utf-8")),
        "line_start": text.count("\n", 0, start) + 1,
        "line_end": text.count("\n", 0, max(start, end - 1)) + 1,
        "excerpt": text[start:end], "literal_sha256_utf8": digest(text[start:end]),
    }


piece_map = []
cursor = 0
for number, piece in enumerate(pieces, 1):
    end = cursor + len(piece["text"])
    piece_map.append({
        "id": f"SEG019-{number:03d}",
        "final": final_span(cursor, end, f"SEG019-{number:03d}"),
        "source": original_span(piece),
    })
    cursor = end
assert cursor == len(final_text)

group_decisions = {
    "ROOT-G01": ["L019-03"],
    "B_G01": ["L019-08"],
    "C_M01": ["L019-09", "L019-10", "L019-11"],
    "A_G03": ["L019-13"],
    "C_M02": ["L019-14", "L019-15"],
    "C_M03": ["L019-17"],
    "ROOT-G02": ["L019-18"],
    "A_G04": ["L019-20"],
    "C_M05": ["L019-21"],
    "C_M04": ["L019-22"],
}
component_count_parents = {
    "ROOT-G01": "L019-03", "B_G01": "L019-08",
    "C_M01": "L019-10", "A_G03": "L019-13",
    "C_M02": "L019-14", "C_M03": "L019-17",
    "ROOT-G02": "L019-18", "A_G04": "L019-20",
    "C_M05": "L019-21", "C_M04": "L019-22",
}
selected_groups = []
for group_id, decisions in group_decisions.items():
    if group_id.startswith("ROOT-"):
        s = sources[group_id]
        begin = r"\mathop" if group_id == "ROOT-G01" else r"\vcenter"
        start = s.index(begin)
        end = len(s) - int(s.endswith("\n"))
        source_piece = raw_piece(group_id, start, end)
        metadata = {
            "root_source_file": original_span(raw_piece(group_id)),
            "source_group_id": group_id,
            "accepted_exact_file_sha256": digest(s),
        }
        components = []
        for command_index, match in enumerate(re.finditer(r"\\(draw|fill)\b.*?;", source_piece["text"], re.DOTALL), 1):
            component_start = start + match.start()
            components.append({
                "id": f"{group_id}_{match.group(1)}_{command_index}",
                "command": match.group(1),
                "source": original_span(raw_piece(group_id, component_start, component_start + len(match.group(0)))),
            })
    else:
        candidate = candidate_groups[group_id]
        source_piece = candidate_piece(group_id)
        metadata = {"candidate_manifest": "out/checks/scan019_tex_candidates.json",
                    "candidate_group_id": group_id,
                    "source_group_id": candidate["reader_group"],
                    "reader": candidate["reader"],
                    "declared_source_fields": {
                        key: value for key, value in candidate.items()
                        if key.startswith("declared_")
                    },
                    "qualification": candidate["qualification"],
                    "attachment_scope": candidate["attachment"]}
        components = [{
            "id": component["id"], "command": component["command"],
            "source": original_span(raw_piece(
                candidate["reader"], component["start_char"], component["end_char"])),
        } for component in candidate["literal_components"]]
    if group_id == "C_M05":
        anchor = find_final(source_piece["text"] + r"\,X", "C_M05-following-X")
        final_group = final_span(anchor["char_start"],
                                 anchor["char_start"] + len(source_piece["text"]), group_id)
    else:
        final_group = find_final(source_piece["text"], group_id)
    final_group["source_group_id"] = group_id
    final_group["decision_ids"] = decisions
    row = {
        "id": group_id, "decision_ids": decisions,
        "source": original_span(source_piece),
        "final_source_attachment": final_group,
        "source_metadata": metadata,
        "literal_components": [],
        "structural_components": [],
    }
    group_scope = (final_group["char_start"], final_group["char_end"])
    for component in components:
        local = find_final(component["source"]["excerpt"], component["id"], group_scope)
        local["source_group_id"] = group_id
        local["component_id"] = component["id"]
        component["final_source_attachment"] = local
        component["visible_source_component"] = True
        component["root_physical_count_parent"] = component_count_parents[group_id]
        row["literal_components"].append(component)
    for command_index, match in enumerate(re.finditer(r"\\(path|node|coordinate)\b.*?;", source_piece["text"], re.DOTALL), 1):
        component_start = source_piece["source_char_start"] + match.start()
        structural_id = f"{group_id}_support_{command_index}"
        structural_source = original_span(raw_piece(
            source_piece["source_id"], component_start, component_start + len(match.group(0))))
        row["structural_components"].append({
            "id": structural_id, "command": match.group(1),
            "source": structural_source,
            "final_source_attachment": find_final(match.group(0), structural_id, group_scope),
        })
    if group_id == "ROOT-G01":
        row["annotation_support"] = [{
            "source": original_span(source_literal("ROOT-G01", r"\phantom{\cdot}")),
            "final_source_attachment": find_final(r"\phantom{\cdot}", "ROOT-G01-invisible-qualifier-anchor", group_scope),
            "visible_source_component": False,
            "note": "Invisible local-qualifier support; root explicitly states that this creates no second visible point.",
        }]
    if group_id == "C_M04":
        row["annotation_support"] = [{
            "source": original_span(source_literal("C", r"\vphantom{\Sigma}")),
            "final_source_attachment": find_final(r"\vphantom{\Sigma}", "C_M04-invisible-placement-support", group_scope),
            "visible_source_component": False,
            "note": "Invisible second underset argument retained exactly with the selected complete group.",
        }]
    if group_id == "ROOT-G02":
        row["reported_run_scope"] = "Root specifies four draw commands in three visible runs; the last two meet at their declared (48,172) endpoint. Copied as source provenance; no geometry computation."
    selected_groups.append(row)
selected_groups.sort(key=lambda row: row["final_source_attachment"]["char_start"])
groups_by_id = {row["id"]: row for row in selected_groups}

display_matches = list(re.finditer(r"\\\[(.*?)\\\]", final_text, re.DOTALL))
assert len(display_matches) == 5
blocks = []
cursor = 0
for index, match in enumerate(display_matches, 1):
    if cursor < match.start():
        blocks.append({"id": f"PROSE019-{index:02d}",
                       "final_source_attachment": final_span(cursor, match.start(), f"PROSE019-{index:02d}")})
    blocks.append({"id": f"DISPLAY019-{index:02d}",
                   "final_source_attachment": final_span(match.start(), match.end(), f"DISPLAY019-{index:02d}")})
    cursor = match.end()
if cursor < len(final_text):
    blocks.append({"id": "TRAILER019", "final_source_attachment": final_span(cursor, len(final_text), "TRAILER019")})

attachments = {}


def attach_literal(decision_id, literal, group=None):
    scope = None
    if group:
        target = groups_by_id[group]["final_source_attachment"]
        scope = (target["char_start"], target["char_end"])
    obj = find_final(literal, decision_id, scope)
    if group:
        obj["source_group_id"] = group
    attachments[decision_id] = [obj]


def attach_group(decision_id, group_id, component=None):
    row = groups_by_id[group_id]
    objects = [dict(row["final_source_attachment"])]
    if component:
        matching = [c for c in row["literal_components"] if c["command"] == component]
        assert len(matching) == 1, (decision_id, group_id, component)
        objects.append(dict(matching[0]["final_source_attachment"]))
    attachments[decision_id] = objects


attach_literal("L019-01", r"D\unsure{é|è}m.")
attach_literal("L019-02", "Le cas")
attach_group("L019-03", "ROOT-G01", "fill")
attach_literal("L019-04", r"I=0,1$")
attach_literal("L019-05", r"\unsure{avec}")
attach_literal("L019-06", r"\geqslant")
attach_literal("L019-07", "les ens.")
attach_group("L019-08", "B_G01")
attach_literal("L019-09", r"\unsure{l'une|l'un}", "C_M01")
attach_group("L019-10", "C_M01", "fill")
attach_group("L019-11", "C_M01", "draw")
attach_literal("L019-12", r"\unsure{on a}")
attach_group("L019-13", "A_G03")
attach_group("L019-14", "C_M02")
attach_group("L019-15", "C_M02", "cdot")
attach_literal("L019-16", r"\deleted{\Sigma_{\unsure{\alpha|0}}}K_0")
attach_group("L019-17", "C_M03")
attach_group("L019-18", "ROOT-G02")
attach_literal("L019-19", r"\unsure{On a|\deleted{O}On a|\deleted{On}On a}")
attach_group("L019-20", "A_G04")
attach_literal("L019-21", r"\unsure{\cdot}\,")
attach_group("L019-22", "C_M04")
attach_literal("L019-23", r"\deleted{Soit} Au")
attach_literal("L019-24", r"\unsure{deuxième|deuxieme|dernier}")
attach_literal("L019-25", r"\deleted{\unsure{somme|réunion}}")
attach_literal("L019-26", r"\unsure{à|:}")
attach_literal("L019-27", "sommer")
attach_literal("L019-28", "cet ens., donc")
attach_literal("L019-29", "tels que")
attach_literal("L019-30", "% archive sheet number: 18")
hat_matches = list(re.finditer(r"\\widehat\{\\Sigma\}(?:_\\alpha|_i)\^\+", final_text))
assert len(hat_matches) == 9
attachments["L019-31"] = []
for index, match in enumerate(hat_matches, 1):
    obj = final_span(match.start(), match.end(), f"L019-31-hat-{index:02d}")
    obj["hat_occurrence"] = index
    obj["S_id"] = "SA01-K81-06"
    attachments["L019-31"].append(obj)
attach_literal("L019-32", r"\scanpage{19}")

original_c_to_decision = {
    "R01": "L019-07", "R02": "L019-12", "R03": "L019-13",
    "R04": "L019-14", "R05": "L019-19", "R06": "L019-25",
    "R07": "L019-27", "R08": "L019-28",
    "R09": "L019-05", "R10": "L019-08", "R11": "L019-09",
    "R12": "L019-16",
}
block_map = {row["id"]: row["final_source_attachment"] for row in blocks}
aligned_start = sources["B"].index(r"\begin{aligned}")
aligned_end = sources["B"].index(r"\end{aligned}", aligned_start) + len(r"\end{aligned}")
aligned_literal = sources["B"][aligned_start:aligned_end]
lower_paragraph_start = final_text.index(r"\deleted{Soit}")
inventory_scopes = {
    "019.01": [final_span(final_text.index(r"D\unsure{é|è}m."), display_matches[0].start(), "019.01")],
    "019.02": [block_map["DISPLAY019-01"]],
    "019.03": [groups_by_id["B_G01"]["final_source_attachment"]],
    "019.04": [find_final(source_lines("C", 6, 16)["text"], "019.04")],
    "019.05": [find_final(source_lines("B", 27, 27)["text"], "019.05")],
    "019.06": [block_map["DISPLAY019-02"]],
    "019.07": [groups_by_id["C_M02"]["final_source_attachment"]],
    "019.08": [find_final("où", "019.08")],
    "019.09": [find_final(aligned_literal, "019.09")],
    "019.10": attachments["L019-16"],
    "019.11": [find_final(source_lines("B", 39, 39)["text"], "019.11")],
    "019.12": [block_map["DISPLAY019-04"]],
    "019.13": [find_final(r"\deleted{Soit}", "019.13")],
    "019.14": [final_span(lower_paragraph_start, display_matches[4].start(), "019.14")],
    "019.15": attachments["L019-25"],
    "019.16": [find_final(r"\deleted{$\Sigma$}", "019.16")],
    "019.17": [block_map["DISPLAY019-05"]],
}
journal_text = (OUT / "scan019_main_decisions.md").read_bytes().decode("utf-8")
journal_ids = re.findall(r"^(L019-\d{2})\s", journal_text, re.MULTILINE)
assert len(journal_ids) == len(set(journal_ids)) == 32
assert set(journal_ids) == set(attachments)

manifest = {
    "schema": "scan019-exact-selected-source-v1",
    "status": "pending root final source approval",
    "main_adjudicated": False, "main_approved": False,
    "scope": "Source-only assembly and structural verification; root supplies all ink, confidence and physical count decisions.",
    "offset_convention": "Unicode characters and UTF-8 bytes are zero-based half-open; line numbers are one-based inclusive.",
    "final_path": FINAL_REL, "final_sha256": final_sha,
    "draft_sha256_utf8": final_sha,
    "base_source": source_paths["B"], "base_sha256": digest(sources["B"]),
    "source_files": {key: {"path": path, "sha256": digest(sources[key])} for key, path in source_paths.items()},
    "source_segments": piece_map,
    "replacements": replacements,
    "selected_groups": selected_groups,
    "final_blocks": blocks,
    "attachments_by_decision": attachments,
    "original_inventory_source_attachments": inventory_scopes,
    "selected_graphic_inventory_source_attachments": {
        row["id"]: [row["final_source_attachment"]] for row in selected_groups
    },
    "archive_inventory_source_attachment": attachments["L019-30"],
    "original_C_doubt_attachments": {
        row: {"decision_id": decision, "final_source_attachment": attachments[decision]}
        for row, decision in original_c_to_decision.items()
    },
    "root_journal": {
        "path": "out/checks/scan019_main_decisions.md",
        "sha256": hashlib.sha256((OUT / "scan019_main_decisions.md").read_bytes()).hexdigest(),
    },
    "preamble": candidate_map["preamble"],
    "component_count_scope": "Draw/fill/dot totals describe literal source components only. Physical C/H counts and shared parents are supplied by the root journal and record; no new physical counts are assigned by assembly.",
    "processing_provenance": [
        "Initial released-reader text batch failed before delivery because the executor transport disconnected; a narrow source retry succeeded. No image was requested.",
        "Root-G01 was initially described with mathord in a source discussion; the exact accepted file uses mathop. Root read that complete file and accepted its SHA256, superseding the earlier wrapper wording.",
        "The initial assembly locator for C_M05 found the same qualified-dot substring in both C_M02 and C_M05. Its locator was narrowed to the selected following thin-space and X. No selected TeX bytes changed; scan019_assembly_attempt_v01.json preserves this bounded pre-audit repair.",
    ],
}


def remove_comments(text):
    result = []
    for line in text.splitlines(keepends=True):
        stop = len(line)
        for index, char in enumerate(line):
            if char == "%":
                backslashes = 0
                cursor = index - 1
                while cursor >= 0 and line[cursor] == "\\":
                    backslashes += 1
                    cursor -= 1
                if backslashes % 2 == 0:
                    stop = index
                    break
        result.append(line[:stop] + ("\n" if stop < len(line) and line.endswith("\n") else ""))
    return "".join(result)


errors = []
clean = remove_comments(final_text)
brace_depth = 0
for index, char in enumerate(clean):
    if char not in "{}":
        continue
    backslashes = 0
    cursor = index - 1
    while cursor >= 0 and clean[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    if backslashes % 2:
        continue
    brace_depth += 1 if char == "{" else -1
    if brace_depth < 0:
        errors.append("Closing brace without a matching opening brace.")
        break
if brace_depth:
    errors.append(f"Final brace depth {brace_depth}.")
stack = []
for match in re.finditer(r"\\(begin|end)\{([^}]+)\}", clean):
    action, name = match.groups()
    if action == "begin":
        stack.append(name)
    elif not stack or stack.pop() != name:
        errors.append("Environment order mismatch at " + match.group(0))
if stack:
    errors.append("Unclosed environments: " + repr(stack))
for pattern in (r"\\\[(.*?)\\\]", r"\\\((.*?)\\\)"):
    for match in re.finditer(pattern, final_text, re.DOTALL):
        if any(not line.strip() for line in match.group(1).splitlines()[1:-1]):
            errors.append("Physical paragraph blank inside a math delimiter pair.")
if clean.count(r"\[") != 5 or clean.count(r"\]") != 5:
    errors.append("Expected five complete display pairs.")
if clean.count(r"\(") != 1 or clean.count(r"\)") != 1:
    errors.append("Expected one complete word-bearing inline pair.")
if clean.count("$") % 2:
    errors.append("Odd number of dollar delimiters.")
preamble_bytes = (ROOT / "out/PREAMBLE.tex").read_bytes()
if hashlib.sha256(preamble_bytes).hexdigest() != candidate_map["preamble"]["sha256"]:
    errors.append("Preamble differs from the frozen source fingerprint.")
allowed_names = set()
for source_id in ("A", "B", "C"):
    allowed_names.update(re.findall(r"\\([A-Za-z]+)", remove_comments(sources[source_id])))
allowed_names.update(re.findall(r"\\(?:newcommand|renewcommand)\{\\([A-Za-z]+)\}", preamble_bytes.decode("utf-8")))
used_names = set(re.findall(r"\\([A-Za-z]+)", clean))
unknown_names = sorted(used_names - allowed_names)
if unknown_names:
    errors.append("Commands absent from released sources/current preamble: " + repr(unknown_names))
for literal, expected in [
    (r"\scanpage{19}", 1),
    (r"\cotefile", 0),
    (r"\operatorname{card}", 3),
    (r"\text{\unsure{l'une|l'un}}", 1),
    (r"\overset{\unsure{\cdot}}{\deleted{\unsure{J|\jmath}}}", 1),
    (r"U=U_{J,i}\cap\Sigma_i^-=", 1),
    (r"\left\{", 0),
    (r"\right.", 0),
]:
    actual = clean.count(literal)
    if actual != expected:
        errors.append(f"Literal occurrence mismatch for {literal}: {actual} versus {expected}.")
visible_components = [component for group in selected_groups for component in group["literal_components"]]
visible_draw_fill = sum(component["command"] in ("draw", "fill") for component in visible_components)
visible_standard_dot = sum(component["command"] == "cdot" for component in visible_components)
if len(re.findall(r"\\(?:draw|fill)\b", clean)) != visible_draw_fill:
    errors.append("Whole-file draw/fill count differs from selected component attachments.")
if visible_standard_dot != 2:
    errors.append("Expected two selected visible standard-dot components; the root phantom remains support only.")
for group_id, following in [
    ("ROOT-G01", "\n I=2$"),
    ("B_G01", r"_{J,i}"),
    ("A_G03", r"\limits"),
    ("A_G04", r"\limits"),
    ("C_M02", r"K_0"),
]:
    end = groups_by_id[group_id]["final_source_attachment"]["char_end"]
    if not final_text[end:].startswith(following):
        errors.append("Unexpected adjoining source after " + group_id)

(ROOT / FINAL_REL).write_bytes(final_text.encode("utf-8"))
(ROOT / MAP_REL).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
map_sha = hashlib.sha256((ROOT / MAP_REL).read_bytes()).hexdigest()
audit = {
    "scope": "One targeted final source pass over exact selected coverage, source identities, group bytes, attachments, structural delimiters and unchanged preamble.",
    "source_only": True, "images_opened": 0,
    "compiled": False, "rendered": False, "metric_validation": False,
    "main_adjudicated": False, "main_approved": False,
    "final_path": FINAL_REL, "final_sha256": final_sha,
    "map_path": MAP_REL, "map_sha256": map_sha,
    "assembly_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "selected_group_count": len(selected_groups),
    "literal_draw_fill_commands": visible_draw_fill,
    "visible_standard_dot_components": visible_standard_dot,
    "invisible_phantom_dot_support_components": 1,
    "display_pairs": len(display_matches),
    "source_segment_coverage": "Every selected character covered by an exact source slice or the declared one-line structural separator.",
    "preamble_sha256": hashlib.sha256(preamble_bytes).hexdigest(),
    "errors": errors, "passed": not errors,
}
version = 1
while (OUT / f"scan019_tex_assembly_audit_v{version:02d}.json").exists():
    version += 1
audit_path = OUT / f"scan019_tex_assembly_audit_v{version:02d}.json"
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
(OUT / "scan019_tex_assembly_audit.json").write_bytes(audit_path.read_bytes())
print(json.dumps({
    "draft": FINAL_REL, "draft_sha256": final_sha,
    "map": MAP_REL, "map_sha256": map_sha,
    "audit": str(audit_path.relative_to(ROOT)),
    "audit_sha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(),
    "errors": errors,
}, ensure_ascii=False))
if errors:
    raise SystemExit(1)

