#!/usr/bin/env python3
"""Source-only lossless representation of the released scan025 text inputs.

No image is read, no reader script is run, and no reading is selected.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import bisect
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
PREFIX = "scan025_source"


def sha(s):
    return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()


def ptrjoin(p, k):
    return p + "/" + str(k).replace("~", "~0").replace("/", "~1")


class JsonSpans:
    def __init__(self, s):
        self.s, self.i, self.spans = s, 0, {}
        self.decoder = json.JSONDecoder()
        self.value = self.parse("")
        self.ws()
        assert self.i == len(s)

    def ws(self):
        while self.i < len(self.s) and self.s[self.i].isspace():
            self.i += 1

    def parse(self, ptr):
        self.ws()
        a = self.i
        c = self.s[self.i]
        if c == "{":
            self.i += 1
            ans = {}
            self.ws()
            if self.s[self.i] != "}":
                while True:
                    self.ws()
                    k, self.i = self.decoder.raw_decode(self.s, self.i)
                    self.ws()
                    assert self.s[self.i] == ":"
                    self.i += 1
                    assert k not in ans, ("duplicate key", ptr, k)
                    ans[k] = self.parse(ptrjoin(ptr, k))
                    self.ws()
                    if self.s[self.i] == "}":
                        break
                    assert self.s[self.i] == ","
                    self.i += 1
            self.i += 1
        elif c == "[":
            self.i += 1
            ans = []
            self.ws()
            if self.s[self.i] != "]":
                while True:
                    ans.append(self.parse(ptrjoin(ptr, len(ans))))
                    self.ws()
                    if self.s[self.i] == "]":
                        break
                    assert self.s[self.i] == ","
                    self.i += 1
            self.i += 1
        else:
            ans, self.i = self.decoder.raw_decode(self.s, self.i)
        self.spans[ptr] = (a, self.i)
        return ans


def strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)
    elif isinstance(x, dict):
        for v in x.values():
            yield from strings(v)


files = []
for r in "ABC":
    p = ROOT / f"out/readers/025/{r}"
    for name in ["reading.tex", "reading.md", "report.json", "source_map.json", "view_audit.json"]:
        files.append(p / name)
    for name in ["crop_manifest.json", "crops.json", "source_audit.json", "final_audit.json", "freeze.json", "final_manifest.json", "unresolved_targets.md"]:
        if (p / name).exists():
            files.append(p / name)
for name in ["C.tex", "H.tex", "C_doubts.txt", "C_notes.txt", "C_inventory.json", "metadata.json", "notation.md"]:
    files.append(ROOT / "packets/025" / name)
for name in ["scan025_reader_fingerprints.json", "scan025_C_doubt_catalog.json", "scan025_H_marker_catalog.json", "scan025_S_scope.json", "scan025_pairwise_diff_manifest.json"]:
    files.append(OUT / name)
files.append(ROOT / "out/briefs/source_record_brief_v07.md")
s_scope = json.loads((OUT / "scan025_S_scope.json").read_text())
files.append(ROOT / s_scope["source"])

source = {}
parses = {}
byte_positions = {}
line_starts = {}
file_ids = {}
file_records = []
for n, p in enumerate(files, 1):
    rel = p.relative_to(ROOT).as_posix()
    data = p.read_bytes()
    s = data.decode("utf-8")
    assert s.encode("utf-8") == data
    source[rel] = s
    file_ids[rel] = f"F{n:03d}"
    bp, b = [0], 0
    for ch in s:
        b += len(ch.encode("utf-8"))
        bp.append(b)
    byte_positions[rel] = bp
    line_starts[rel] = [0] + [m.end() for m in re.finditer("\n", s)]
    rec = {"id": file_ids[rel], "path": rel, "sha256_utf8": sha(data), "characters": len(s), "utf8_bytes": len(data)}
    if p.suffix == ".json":
        parse = JsonSpans(s)
        assert parse.value == json.loads(s)
        parses[rel] = parse
        profiles = []
        for ascii_flag in [False, True]:
            for indent in [2, 4, None]:
                for ending in ["\n", ""]:
                    if json.dumps(parse.value, ensure_ascii=ascii_flag, indent=indent) + ending == s:
                        profiles.append({"ensure_ascii": ascii_flag, "indent": indent, "ending": ending})
        assert profiles, (rel, "no exact serialization profile")
        rec.update(kind="json", serialization=profiles[0])
    else:
        rec.update(kind="text")
    file_records.append(rec)

string_records = []
string_index = {}
span_records = []
span_index = {}
json_node_refs = {}


def span(rel, a, b):
    assert 0 <= a <= b <= len(source[rel]), (rel, a, b)
    key = (rel, a, b)
    if key not in span_index:
        sid = f"P{len(span_records)+1:06d}"
        ls = line_starts[rel]
        rec = {
            "id": sid, "source_path": rel, "source_file": file_ids[rel],
            "source_sha256_utf8": sha(source[rel]),
            "char_start": a, "char_end_exclusive": b,
            "utf8_byte_start": byte_positions[rel][a], "utf8_byte_end_exclusive": byte_positions[rel][b],
            "line_start_1based": bisect.bisect_right(ls, a),
            "line_end_1based": bisect.bisect_right(ls, max(a, b-1)),
            "literal": {"file_slice": file_ids[rel], "char_start": a, "char_end_exclusive": b},
            "literal_sha256_utf8": sha(source[rel][a:b]),
        }
        span_index[key] = sid
        span_records.append(rec)
    return span_index[key]


def add_string(s, base=False):
    # Only plain source files may back string slices. No JSON projection can
    # depend on itself. Whole base text chunks always store their literal.
    if s in string_index:
        return string_index[s]
    sid = f"S{len(string_records)+1:06d}"
    rec = {"id": sid, "characters": len(s), "utf8_bytes": len(s.encode("utf-8")), "sha256_utf8": sha(s)}
    match = None
    if not base and len(s) >= 24:
        for rel in source:
            if rel in parses or not (rel.endswith(".tex") or rel.endswith("C_doubts.txt")):
                continue
            a = source[rel].find(s)
            if a >= 0:
                match = span(rel, a, a + len(s))
                break
    if match:
        rec["literal"] = {"span_ref": match}
    else:
        rec["literal"] = s
    string_index[s] = sid
    string_records.append(rec)
    return sid


# Text is stored once, in bounded source chunks. Each chunk is on a line
# boundary except a possible single source line longer than the bound.
for rec in file_records:
    if rec["kind"] != "text":
        continue
    rel = rec["path"]
    s = source[rel]
    chunks, a = [], 0
    while a < len(s):
        b = min(a + 10000, len(s))
        if b < len(s):
            e = s.rfind("\n", a, b)
            if e >= a:
                b = e + 1
        chunks.append({"string_ref": add_string(s[a:b], base=True), "span_ref": span(rel, a, b)})
        a = b
    rec["payload"] = {"text_chunks": chunks}

freq = Counter(s for parse in parses.values() for s in strings(parse.value))


def encode(x):
    if isinstance(x, str):
        if len(x) > 96 or "\n" in x or (len(x) >= 24 and freq[x] > 1):
            return {"$s": add_string(x)}
        return x
    if isinstance(x, list):
        return [encode(v) for v in x]
    if isinstance(x, dict):
        assert "$s" not in x, "reserved exact-string codec key collision"
        return {k: encode(v) for k, v in x.items()}
    return x


for rec in file_records:
    if rec["kind"] != "json":
        continue
    rel = rec["path"]
    rec["payload"] = encode(parses[rel].value)
    json_node_refs[rec["id"]] = {ptr: span(rel, a, b) for ptr, (a, b) in parses[rel].spans.items()}

pool = {
    "scan": 25, "schema": "scan025-source-lossless-pool-v01", "source_only": True,
    "status": "unadjudicated source representation; no ink, counts, confidence or selected reading assigned",
    "offset_convention": "Zero-based Unicode-codepoint and UTF-8-byte half-open offsets; lines are one-based inclusive through the last included character.",
    "codec": {
        "json_strings": "An object with sole key $s resolves to the exact decoded string with that ID. Other objects, key order, arrays and scalar types remain as supplied.",
        "text": "Concatenate exact decoded text_chunks in order.",
        "json_bytes": "Decode payload, then Python json.dumps with the stored ensure_ascii and indent, followed by the exact stored ending. Equality to the original UTF-8 bytes is verified.",
        "span_literal": "Resolve its file_slice source file by that file's payload and serialization, then take the declared character interval. All byte offsets and literal hashes are independently checkable.",
        "pool_string_span": "Only a plain TeX or C_doubts source file backs an indirect pooled string; these files contain direct text chunks. The reference graph is acyclic.",
        "roles": "Pooling identical literals shares bytes only. Each source file and JSON pointer retains its original field role; no shared literal authorizes a role substitution.",
    },
    "files": file_records, "strings": string_records, "spans": span_records, "json_pointer_spans": json_node_refs,
    "main_adjudicated": False, "main_approved": False,
}


def dump(name, x):
    p = OUT / name
    p.write_text(json.dumps(x, ensure_ascii=False, indent=2) + "\n")
    return {"path": p.relative_to(ROOT).as_posix(), "sha256_utf8": sha(p.read_bytes()), "bytes": p.stat().st_size}


pool_record = dump(PREFIX + "_pool_v01.json", pool)

# Complete review projection: every JSON top-level property and every array
# item is retained at its exact pointer. Oversized containers split further.
# New non-TeX strings print once; repeated occurrences keep the shared ID.
file_byid = {r["id"]: r for r in file_records}
strings_byid = {r["id"]: r for r in string_records}
spans_byid = {r["id"]: r for r in span_records}
seen = set()
review_rows = []


def refs(x):
    if isinstance(x, dict):
        if set(x) == {"$s"}:
            yield x["$s"]
        else:
            for v in x.values():
                yield from refs(v)
    elif isinstance(x, list):
        for v in x:
            yield from refs(v)


def emit(rec, ptr, val):
    if len(json.dumps(val, ensure_ascii=False)) > 16000 and isinstance(val, (dict, list)) and val:
        items = list(val.items()) if isinstance(val, dict) else list(enumerate(val))
        review_rows.append({"kind": "container", "file": rec["id"], "source_path": rec["path"], "pointer": ptr,
                            "span_ref": json_node_refs[rec["id"]][ptr], "container_type": type(val).__name__,
                            "ordered_children": [k for k, _ in items]})
        for k, v in items:
            emit(rec, ptrjoin(ptr, k), v)
        return
    new = []
    for sid in refs(val):
        if sid in seen:
            continue
        seen.add(sid)
        row = dict(strings_byid[sid])
        if isinstance(row["literal"], dict):
            row["exact_source_span"] = spans_byid[row["literal"]["span_ref"]]
            row["review_basis"] = "Exact substring of the complete source text; no alternate wording or inference is substituted."
        new.append(row)
    review_rows.append({"kind": "value", "file": rec["id"], "source_path": rec["path"], "pointer": ptr,
                        "span_ref": json_node_refs[rec["id"]][ptr], "value": val, "new_strings": new})


for rec in file_records:
    if rec["kind"] != "json":
        continue
    val = rec["payload"]
    if isinstance(val, dict):
        items = list(val.items())
    elif isinstance(val, list):
        items = list(enumerate(val))
    else:
        items = [(None, val)]
    review_rows.append({"kind": "document", "file": rec["id"], "source_path": rec["path"], "source_sha256_utf8": rec["sha256_utf8"],
                        "root_type": type(val).__name__, "ordered_children": [k for k, _ in items], "serialization": rec["serialization"]})
    for key, value in items:
        ptr = "" if key is None else ptrjoin("", key)
        if isinstance(value, list) and value:
            review_rows.append({"kind": "container", "file": rec["id"], "source_path": rec["path"], "pointer": ptr,
                                "span_ref": json_node_refs[rec["id"]][ptr], "container_type": "list", "ordered_children": list(range(len(value)))})
            for i, sub in enumerate(value):
                emit(rec, ptrjoin(ptr, i), sub)
        else:
            emit(rec, ptr, value)

review_pages = []
page_rows, page_bytes = [], 0
for row_no, row in enumerate(review_rows, 1):
    row = {"projection_row": row_no, **row}
    line = json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n"
    if page_rows and page_bytes + len(line.encode("utf-8")) > 28000:
        review_pages.append(page_rows)
        page_rows, page_bytes = [], 0
    page_rows.append(line)
    page_bytes += len(line.encode("utf-8"))
if page_rows:
    review_pages.append(page_rows)
page_records = []
for i, lines in enumerate(review_pages, 1):
    name = PREFIX + f"_review_{i:02d}.jsonl"
    p = OUT / name
    p.write_text("".join(lines))
    first, last = json.loads(lines[0])["projection_row"], json.loads(lines[-1])["projection_row"]
    page_records.append({"path": p.relative_to(ROOT).as_posix(), "sha256_utf8": sha(p.read_bytes()), "bytes": p.stat().st_size,
                         "projection_row_start": first, "projection_row_end": last})

manifest = {
    "scan": 25, "source_only": True, "pool": pool_record,
    "review_projection_schema": "Each document/container records exact ordered child keys; each value records an original source pointer and its entire losslessly encoded subtree. Rebuild from the document/container declarations and value subtrees, resolving $s through the shared pool. No source property is omitted.",
    "review_instruction": "Read pages in numeric order. Every first-use pooled non-TeX string appears in full under new_strings. Exact TeX substrings use a pool span with source path/hash/character/UTF-8/line bounds and a literal reconstruction rule; the complete reader TeX was already read by root. Candidate qualifications, hand scopes, flags, views and surface-origin wording remain in their original fields. A later $s refers to exactly the same previously exposed string, without assigning the same semantic role.",
    "source_files": [{k: v for k, v in r.items() if k != "payload"} for r in file_records],
    "review_pages": page_records, "review_rows": len(review_rows),
    "counts": {"files": len(file_records), "json_documents": len(parses), "unique_strings": len(string_records), "exact_spans": len(span_records)},
    "frozen_reader_manifest": "out/checks/scan025_reader_fingerprints.json",
    "assembly_status": "not started; root crop journal absent from this source stage",
    "main_adjudicated": False, "main_approved": False,
}
manifest_record = dump(PREFIX + "_projection_manifest_v01.json", manifest)
print(json.dumps({"pool": pool_record, "manifest": manifest_record, "review_pages": len(review_pages), "counts": manifest["counts"]}, indent=2))
