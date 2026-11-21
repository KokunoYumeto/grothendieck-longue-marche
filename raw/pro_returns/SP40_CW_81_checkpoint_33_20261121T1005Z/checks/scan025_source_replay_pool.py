#!/usr/bin/env python3
"""Replay exact source JSON/text and all pointer spans; never inspect images."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "out/checks"
pool_path = OUT / "scan025_source_pool_v01.json"
manifest_path = OUT / "scan025_source_projection_manifest_v01.json"
pool = json.loads(pool_path.read_text())
manifest = json.loads(manifest_path.read_text())
F = {x["id"]: x for x in pool["files"]}
S = {x["id"]: x for x in pool["strings"]}
P = {x["id"]: x for x in pool["spans"]}
cache, strings_cache = {}, {}


def sha(x):
    return hashlib.sha256(x.encode("utf-8") if isinstance(x, str) else x).hexdigest()


def resolve_string(k):
    if k in strings_cache:
        return strings_cache[k]
    v = S[k]["literal"]
    if isinstance(v, str):
        s = v
    else:
        p = P[v["span_ref"]]
        s = resolve_file(p["source_file"])[p["char_start"]:p["char_end_exclusive"]]
    assert len(s) == S[k]["characters"]
    assert len(s.encode("utf-8")) == S[k]["utf8_bytes"]
    assert sha(s) == S[k]["sha256_utf8"]
    strings_cache[k] = s
    return s


def decode(v):
    if isinstance(v, dict):
        if set(v) == {"$s"}:
            return resolve_string(v["$s"])
        return {k: decode(x) for k, x in v.items()}
    if isinstance(v, list):
        return [decode(x) for x in v]
    return v


def resolve_file(k):
    if k in cache:
        return cache[k]
    f = F[k]
    if f["kind"] == "text":
        s = "".join(resolve_string(x["string_ref"]) for x in f["payload"]["text_chunks"])
    else:
        ser = f["serialization"]
        s = json.dumps(decode(f["payload"]), ensure_ascii=ser["ensure_ascii"], indent=ser["indent"]) + ser["ending"]
    assert sha(s) == f["sha256_utf8"]
    assert len(s) == f["characters"]
    assert len(s.encode("utf-8")) == f["utf8_bytes"]
    assert s.encode("utf-8") == (ROOT / f["path"]).read_bytes()
    cache[k] = s
    return s


def pointer(v, ptr):
    if not ptr:
        return v
    for token in ptr[1:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        v = v[int(token)] if isinstance(v, list) else v[token]
    return v


for k in F:
    resolve_file(k)
for k in S:
    resolve_string(k)
span_count = 0
for p in P.values():
    s = resolve_file(p["source_file"])
    a, b = p["char_start"], p["char_end_exclusive"]
    assert sha(s) == p["source_sha256_utf8"]
    assert F[p["source_file"]]["path"] == p["source_path"]
    assert len(s[:a].encode("utf-8")) == p["utf8_byte_start"]
    assert len(s[:b].encode("utf-8")) == p["utf8_byte_end_exclusive"]
    assert s.count("\n", 0, a)+1 == p["line_start_1based"]
    assert s.count("\n", 0, max(a, b-1))+1 == p["line_end_1based"]
    assert sha(s[a:b]) == p["literal_sha256_utf8"]
    assert p["literal"] == {"file_slice": p["source_file"], "char_start": a, "char_end_exclusive": b}
    span_count += 1
pointer_count = 0
for fid, refs in pool["json_pointer_spans"].items():
    full = json.loads(resolve_file(fid))
    for ptr, ref in refs.items():
        p = P[ref]
        literal = resolve_file(fid)[p["char_start"]:p["char_end_exclusive"]]
        assert json.loads(literal) == pointer(full, ptr), (fid, ptr)
        pointer_count += 1

# Rebuild each JSON document from the bounded projections alone. This checks
# the reading projection's exact source tree, not only the pool's own copy.
review = []
for page in manifest["review_pages"]:
    p = ROOT / page["path"]
    assert sha(p.read_bytes()) == page["sha256_utf8"]
    review += [json.loads(line) for line in p.read_text().splitlines()]
assert [x["projection_row"] for x in review] == list(range(1, len(review)+1))
documents = {}
seen_strings = set()


def assign(doc, ptr, val):
    parts = ptr[1:].split("/") if ptr else []
    if not parts:
        return val
    target = doc
    for token in parts[:-1]:
        token = token.replace("~1", "/").replace("~0", "~")
        target = target[int(token)] if isinstance(target, list) else target[token]
    token = parts[-1].replace("~1", "/").replace("~0", "~")
    target[int(token) if isinstance(target, list) else token] = val
    return doc


for r in review:
    fid = r["file"]
    if r["kind"] == "document":
        documents[fid] = {k: None for k in r["ordered_children"]} if r["root_type"] == "dict" else [None] * len(r["ordered_children"])
    elif r["kind"] == "container":
        val = {k: None for k in r["ordered_children"]} if r["container_type"] == "dict" else [None] * len(r["ordered_children"])
        documents[fid] = assign(documents[fid], r["pointer"], val)
        assert pool["json_pointer_spans"][fid][r["pointer"]] == r["span_ref"]
    else:
        documents[fid] = assign(documents[fid], r["pointer"], r["value"])
        assert pool["json_pointer_spans"][fid][r["pointer"]] == r["span_ref"]
        for entry in r["new_strings"]:
            sid = entry["id"]
            assert sid not in seen_strings
            seen_strings.add(sid)
            assert all(entry[k] == v for k, v in S[sid].items())
for fid, tree in documents.items():
    assert tree == F[fid]["payload"], fid
    ser = F[fid]["serialization"]
    rebuilt = json.dumps(decode(tree), ensure_ascii=ser["ensure_ascii"], indent=ser["indent"]) + ser["ending"]
    assert rebuilt == resolve_file(fid), fid

fingerprints = json.loads((OUT / "scan025_reader_fingerprints.json").read_text())
for rel, expected in fingerprints["files"].items():
    assert sha((ROOT / rel).read_bytes()) == expected, rel

result = {
    "scan": 25, "source_only": True,
    "pool_sha256_utf8": sha(pool_path.read_bytes()), "manifest_sha256_utf8": sha(manifest_path.read_bytes()),
    "exact_source_files_reconstructed": len(F), "exact_json_documents_reconstructed_from_review_pages": len(documents),
    "unique_strings_replayed": len(S), "exact_spans_replayed": span_count,
    "json_value_pointer_spans_replayed": pointer_count, "bounded_review_pages": len(manifest["review_pages"]),
    "projection_rows": len(review), "frozen_reader_hashes_checked": len(fingerprints["files"]),
    "literal_role_substitutions": 0,
    "images_opened_or_read": 0, "ink_choices": 0,
    "all_checks_passed": True,
    "limits": "Exact source serialization, spans and bounded projection coverage only. Reader image observations remain attributed claims. No count, confidence, hand, state or ink outcome is adjudicated.",
}
p = OUT / "scan025_source_pool_replay_v01.json"
p.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(result, indent=2))
