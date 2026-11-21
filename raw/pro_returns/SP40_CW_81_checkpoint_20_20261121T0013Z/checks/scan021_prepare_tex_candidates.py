"""Index the released scan021 TeX candidates without selecting manuscript ink.

Text sources only. This script performs source-offset bookkeeping and byte hashes;
it does not open images, compute geometry, compile, render or check mathematics.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "out/checks/scan021_tex_candidates.json"
sha = lambda b: hashlib.sha256(b).hexdigest()


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def ref(path, value):
    source = read(path)
    assert source.count(value) == 1, (path, source.count(value), value[:100])
    a = source.index(value)
    b = a + len(value)
    return {
        "path": path, "manifest": path,
        "char_start": a, "char_end": b,
        "byte_start": len(source[:a].encode("utf-8")),
        "byte_end": len(source[:b].encode("utf-8")),
        "line_start": source.count("\n", 0, a) + 1,
        "line_end": source.count("\n", 0, b - 1) + 1,
        "excerpt": value, "literal_sha256_utf8": sha(value.encode("utf-8")),
        "source_sha256_utf8": sha(source.encode("utf-8")),
    }


def candidate(reader, metadata_path, pointer, group, value):
    return {
        "id": group["id"], "reader": reader,
        "full_source": ref(f"out/readers/021/{reader}/reading.tex", value),
        "original_metadata": {
            "path": metadata_path, "json_pointer": pointer,
            "source_sha256_utf8": sha((ROOT / metadata_path).read_bytes()),
            "value": group,
        },
        "lexical_parent_groups": [],
        "selected": None,
        "main_approved": False,
    }


groups = []
files = ["out/PREAMBLE.tex", "packets/021/C.tex", "packets/021/H.tex"]

path = "out/readers/021/A/source_audit.json"
for index, group in enumerate(json.loads(read(path))["groups"]):
    groups.append(candidate("A", path, f"/groups/{index}", group, group["exact_source"]))
files.extend([path, "out/readers/021/A/groups.json", "out/readers/021/A/reading.tex"])

path = "out/readers/021/B/source_audit.json"
audit = json.loads(read(path))
for key in ["groups", "nested_local_groups"]:
    for index, group in enumerate(audit[key]):
        groups.append(candidate("B", path, f"/{key}/{index}", group, group["exact_source"]))
files.extend([path, "out/readers/021/B/source_groups.json", "out/readers/021/B/reading.tex"])

path = "out/readers/021/C/graphical_groups.json"
for index, group in enumerate(json.loads(read(path))):
    groups.append(candidate("C", path, f"/{index}", group, group["reading_tex_exact_excerpt"]))
files.extend([path, "out/readers/021/C/source_audit.json", "out/readers/021/C/reading.tex"])

for group in groups:
    s = group["full_source"]
    for other in groups:
        t = other["full_source"]
        if group["id"] != other["id"] and s["path"] == t["path"]:
            if t["char_start"] <= s["char_start"] and s["char_end"] <= t["char_end"]:
                group["lexical_parent_groups"].append(other["id"])

a_path = "out/readers/021/A/reading.tex"
c_path = "out/readers/021/C/reading.tex"
c_lines = read(c_path).splitlines(keepends=True)
blank_line_refs = []
for line_number in [25, 47, 65, 84, 96, 134, 154, 255]:
    a = sum(map(len, c_lines[:line_number-1]))
    b = a + len(c_lines[line_number-1])
    assert c_lines[line_number-1].strip() == ""
    blank_line_refs.append({
        "path": c_path, "line": line_number,
        "char_start": a, "char_end": b,
        "literal": c_lines[line_number-1],
    })

manifest = {
    "schema": "scan021-unselected-tex-candidates-v1",
    "status": "All three readers released; no source content selected by this index.",
    "main_adjudicated": False,
    "main_approved": False,
    "offset_convention": "zero-based Unicode code points and explicit UTF-8 bytes; ends exclusive",
    "selection_authority": "Root alone; out/checks/scan021_main_decisions.md",
    "source_files": {p: {"sha256_utf8": sha((ROOT/p).read_bytes())} for p in files},
    "graphic_groups": groups,
    "ownership_scope": "Source containment only. Lexical parents are not additional visible copies. No geometric overlap computation.",
    "pending_selected_source_syntax_repairs": [
        {
            "id": "A021-SOURCE-01",
            "source": ref(a_path, "$overset{"),
            "proposed_selected_literal": "$\\overset{",
            "status": "Original untouched. Apply only in selected source containing this exact locus.",
            "root_authority": "Root initial assembler brief and later source messages.",
            "main_approved": False,
        },
        {
            "id": "C021-SOURCE-01",
            "sources": blank_line_refs,
            "proposed_selected_literal": "",
            "status": "Original untouched. Remove physical paragraph blanks only when their containing display is selected.",
            "root_authority": "Root instruction to assembler; source-record brief v03 exact assembly section.",
            "main_approved": False,
        },
    ],
    "validation_scope": "Exact source identity and source-containment bookkeeping only. No image, render, geometry or mathematical validation.",
}
TARGET.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "path": str(TARGET.relative_to(ROOT)),
    "sha256_utf8": sha(TARGET.read_bytes()),
    "candidate_groups": len(groups),
    "by_reader": {r: sum(g["reader"] == r for g in groups) for r in "ABC"},
    "selected_draft_created": False,
}, ensure_ascii=False))
