#!/usr/bin/env python3
"""Source-only, reversible indexes for released scan024 textual sources.

This script reads no image and performs no image or mathematical computation.
All mutations are restricted to scan024_source_* files in out/checks.
"""
from pathlib import Path
import copy
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / "out/checks"
READER = "C"
RDIR = BASE / "out/readers/024" / READER


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source(path, role):
    raw = (BASE / path).read_bytes()
    text = raw.decode("utf-8")
    return {
        "source_path": path,
        "semantic_role": role,
        "sha256_utf8": sha(raw),
        "character_start": 0,
        "character_end_exclusive": len(text),
        "utf8_byte_start": 0,
        "utf8_byte_end_exclusive": len(raw),
        "line_start": 1,
        "line_end": len(text.splitlines()),
    }, text


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def put(name, obj):
    path = OUT / ("scan024_source_" + name)
    data = dumps(obj).encode("utf-8")
    path.write_bytes(data)
    return {"path": str(path.relative_to(BASE)), "sha256_utf8": sha(data), "bytes": len(data)}


def ptr_part(value):
    return str(value).replace("~", "~0").replace("/", "~1")


class JSONSpans:
    """Exact JSON value spans, retaining lexical bytes and JSON pointer identity."""

    def __init__(self, text):
        self.text = text
        self.spans = {}
        self.value, end = self.parse(0, "")
        assert text[end:].strip() == ""
        assert self.value == json.loads(text)

    def white(self, pos):
        while pos < len(self.text) and self.text[pos].isspace():
            pos += 1
        return pos

    def parse(self, pos, pointer):
        pos = self.white(pos)
        start = pos
        t = self.text
        if t[pos] == "{":
            value = {}
            pos = self.white(pos + 1)
            while t[pos] != "}":
                key, pos = json.decoder.scanstring(t, pos + 1, True)
                pos = self.white(pos)
                assert t[pos] == ":"
                child, pos = self.parse(pos + 1, pointer + "/" + ptr_part(key))
                assert key not in value
                value[key] = child
                pos = self.white(pos)
                if t[pos] == "}":
                    break
                assert t[pos] == ","
                pos = self.white(pos + 1)
            pos += 1
        elif t[pos] == "[":
            value = []
            pos = self.white(pos + 1)
            while t[pos] != "]":
                child, pos = self.parse(pos, pointer + "/" + str(len(value)))
                value.append(child)
                pos = self.white(pos)
                if t[pos] == "]":
                    break
                assert t[pos] == ","
                pos = self.white(pos + 1)
            pos += 1
        else:
            value, length = json.JSONDecoder().raw_decode(t[pos:])
            pos += length
        self.spans[pointer] = (start, pos)
        return value, pos


def ref(source_ref, text, start, end, pointer=None):
    item = dict(source_ref)
    item.update({
        "character_start": start,
        "character_end_exclusive": end,
        "utf8_byte_start": len(text[:start].encode("utf-8")),
        "utf8_byte_end_exclusive": len(text[:end].encode("utf-8")),
        "line_start": text.count("\n", 0, start) + 1,
        "line_end": text.count("\n", 0, end - 1) + 1 if end > start else text.count("\n", 0, start) + 1,
        "span_sha256_utf8": sha(text[start:end].encode("utf-8")),
    })
    if pointer is not None:
        item["json_pointer"] = pointer
    return item


def build_map_projection():
    tex_ref, tex = source("out/readers/024/C/reading.tex", "reader_C_actual_complete_TeX")
    map_ref, map_text = source("out/readers/024/C/source_map.json", "reader_C_source_map_raw")
    parsed = JSONSpans(map_text)
    original = parsed.value
    assert original["sha256"] == tex_ref["sha256_utf8"]
    assert dumps(original) == map_text
    schema = ["character_start", "character_end_exclusive", "utf8_byte_start", "utf8_byte_end_exclusive", "line_start", "line_end", "exact_tex"]
    spans = []
    span_keys = {}
    locations = []
    issues = []

    def project(value, pointer=""):
        if isinstance(value, dict) and "exact_tex" in value:
            assert list(value) == schema, (pointer, list(value))
            a = value["character_start"]
            b = value["character_end_exclusive"]
            actual = tex[a:b]
            check = {
                "literal_matches_own_TeX": value["exact_tex"] == actual,
                "utf8_start_matches": value["utf8_byte_start"] == len(tex[:a].encode("utf-8")),
                "utf8_end_matches": value["utf8_byte_end_exclusive"] == len(tex[:b].encode("utf-8")),
                "line_start_matches": value["line_start"] == tex.count("\n", 0, a) + 1,
                "line_end_matches": value["line_end"] == tex.count("\n", 0, b - 1) + 1,
            }
            if not all(check.values()):
                issues.append({"json_pointer": pointer, "checks": check})
            assert check["literal_matches_own_TeX"], pointer
            key = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
            if key not in span_keys:
                span_keys[key] = len(spans)
                spans.append([value[k] for k in schema[:-1]] + [{"$own_TeX_slice": [a, b]}])
            n = span_keys[key]
            ma, mb = parsed.spans[pointer]
            locations.append({
                "map_json_pointer": pointer,
                "map_value_character_span": [ma, mb],
                "span_index": n,
                "literal_sha256_utf8": sha(actual.encode("utf-8")),
                "checks": check,
            })
            return {"$span": n}
        if isinstance(value, dict):
            return {k: project(v, pointer + "/" + ptr_part(k)) for k, v in value.items()}
        if isinstance(value, list):
            return [project(v, pointer + "/" + str(i)) for i, v in enumerate(value)]
        return value

    payload = project(original)
    document = {
        "format": "scan024-source-map-lossless-projection-v1",
        "source_only": True,
        "original_map": map_ref,
        "literal_authority": tex_ref,
        "reconstruction": "Replace each {$span:n} with the ordered object from span_columns and span_rows[n]; replace that row's {$own_TeX_slice:[a,b]} with the literal reader-C reading.tex character slice [a,b). Serialize ensure_ascii=False, indent=2 and one final LF. All other fields and values remain literal. This operation does not choose or rewrite any reading.",
        "span_columns": schema,
        "span_rows": spans,
        "payload": payload,
    }

    def restore(value):
        if isinstance(value, dict) and list(value) == ["$span"]:
            row = spans[value["$span"]]
            a, b = row[-1]["$own_TeX_slice"]
            return dict(zip(schema, row[:-1] + [tex[a:b]]))
        if isinstance(value, dict):
            return {k: restore(v) for k, v in value.items()}
        if isinstance(value, list):
            return [restore(v) for v in value]
        return value

    restored = restore(payload)
    rebuilt = dumps(restored).encode("utf-8")
    assert restored == original
    assert rebuilt == map_text.encode("utf-8")
    projection = put("C_map_projection.json", document)
    readable = OUT / "scan024_source_C_map_projection.jsonl"
    lines = [json.dumps({k: document[k] for k in document if k not in ["span_rows", "payload"]}, ensure_ascii=False)]
    for k, v in payload.items():
        if isinstance(v, list):
            for i, row in enumerate(v):
                lines.append(json.dumps({"section": k, "index": i, "value": row}, ensure_ascii=False, separators=(",", ":")))
        else:
            lines.append(json.dumps({"section": k, "value": v}, ensure_ascii=False, separators=(",", ":")))
    for i, row in enumerate(spans):
        lines.append(json.dumps({"span_index": i, "row": row}, ensure_ascii=False, separators=(",", ":")))
    readable.write_text("\n".join(lines) + "\n", encoding="utf-8")
    audit = {
        "scan": 24,
        "reader": "C",
        "source_only": True,
        "original_map": map_ref,
        "literal_authority": tex_ref,
        "projection": projection,
        "readable_projection": {"path": str(readable.relative_to(BASE)), "sha256_utf8": sha(readable.read_bytes())},
        "exact_semantic_reconstruction": restored == original,
        "exact_utf8_reconstruction": rebuilt == map_text.encode("utf-8"),
        "reconstructed_sha256_utf8": sha(rebuilt),
        "span_occurrences_verified": len(locations),
        "distinct_exact_source_spans": len(spans),
        "copied_source_section_sizes": {k: len(v) for k, v in original.items() if isinstance(v, list)},
        "issues": issues,
        "span_verifications": locations,
        "limits": "No image, crop, OCR, rendering, compilation, coordinate/image calculation or mathematical checking was performed. No count, confidence, reading, hand or root approval was chosen. Reader originals remain unchanged.",
    }
    audit_file = put("C_map_projection_audit.json", audit)
    print(json.dumps({"projection": projection, "readable": audit["readable_projection"], "audit": audit_file, "issues": issues}, ensure_ascii=False))


def build_general_projection(reader, filename):
    """Losslessly replace supplied literal-span objects by exact own-source refs."""
    path = f"out/readers/024/{reader}/{filename}"
    raw_ref, raw_text = source(path, f"reader_{reader}_{filename}_raw")
    parsed = JSONSpans(raw_text)
    original = parsed.value
    assert dumps(original) == raw_text
    authorities = {}
    authority_texts = {}
    for key, p, role in [
        (f"reader_{reader}", f"out/readers/024/{reader}/reading.tex", f"reader_{reader}_actual_complete_TeX"),
        ("witness_C", "packets/024/C.tex", "public_witness_C_literal"),
        ("witness_H", "packets/024/H.tex", "public_witness_H_literal"),
    ]:
        authorities[key], authority_texts[key] = source(p, role)
    schemas = []
    schema_lookup = {}
    records = []
    record_lookup = {}
    verified = []
    issues = []

    def project(v, pointer=""):
        if isinstance(v, dict) and "exact_tex" in v:
            a = v.get("char_start", v.get("character_start"))
            b = v.get("char_end_exclusive", v.get("character_end_exclusive"))
            authority = f"reader_{reader}"
            if "path" in v:
                matches = [k for k, r in authorities.items() if r["source_path"] == v["path"]]
                assert len(matches) == 1, (pointer, v["path"])
                authority = matches[0]
            text = authority_texts[authority]
            inferred_scope = None
            if a is None or b is None:
                own_map = json.loads((BASE / f"out/readers/024/{reader}/source_map.json").read_bytes())
                matches = [g for g in own_map["groups"] if g.get("id") == v.get("id") and g["source_span"]["exact_tex"] == v["exact_tex"]]
                assert authority == f"reader_{reader}" and len(matches) == 1, pointer
                own_span = matches[0]["source_span"]
                a = own_span.get("char_start", own_span.get("character_start"))
                b = own_span.get("char_end_exclusive", own_span.get("character_end_exclusive"))
                inferred_scope = {"source_map_path": f"out/readers/024/{reader}/source_map.json", "group_id": v["id"], "basis": "Same exact group id and complete exact_tex; the original report object supplied no offset fields."}
            excerpt = text[a:b]
            checks = {"literal_matches_own_source": excerpt == v["exact_tex"]}
            for field, expected in [
                ("utf8_byte_start", len(text[:a].encode("utf-8"))),
                ("utf8_byte_end_exclusive", len(text[:b].encode("utf-8"))),
                ("line_start", text.count("\n", 0, a) + 1),
                ("line_end", text.count("\n", 0, b - 1) + 1),
            ]:
                if field in v:
                    checks[field + "_matches"] = v[field] == expected
            if not all(checks.values()):
                issues.append({"json_pointer": pointer, "checks": checks})
            assert checks["literal_matches_own_source"], (pointer, authority)
            schema = tuple(v)
            if schema not in schema_lookup:
                schema_lookup[schema] = len(schemas)
                schemas.append(list(schema))
            row = [schema_lookup[schema], [({"$literal_slice": [authority, a, b]} if k == "exact_tex" else project(z, pointer + "/" + ptr_part(k))) for k, z in v.items()]]
            key = json.dumps(row, ensure_ascii=False, separators=(",", ":"))
            if key not in record_lookup:
                record_lookup[key] = len(records)
                records.append(row)
            index = record_lookup[key]
            oa, ob = parsed.spans[pointer]
            verified.append({"json_pointer": pointer, "original_value_character_span": [oa, ob], "record_index": index, "literal_authority": authority, "literal_character_span": [a, b], "literal_sha256_utf8": sha(excerpt.encode("utf-8")), "checks": checks, "offset_basis_when_absent": inferred_scope})
            return {"$source_record": index}
        if isinstance(v, dict):
            return {k: project(z, pointer + "/" + ptr_part(k)) for k, z in v.items()}
        if isinstance(v, list):
            return [project(z, pointer + "/" + str(i)) for i, z in enumerate(v)]
        return v

    payload = project(original)

    def restore(v):
        if isinstance(v, dict) and list(v) == ["$source_record"]:
            schema, row = records[v["$source_record"]]
            return dict(zip(schemas[schema], [restore(z) for z in row]))
        if isinstance(v, dict) and list(v) == ["$literal_slice"]:
            key, a, b = v["$literal_slice"]
            return authority_texts[key][a:b]
        if isinstance(v, dict):
            return {k: restore(z) for k, z in v.items()}
        if isinstance(v, list):
            return [restore(z) for z in v]
        return v

    restored = restore(payload)
    rebuilt = dumps(restored).encode("utf-8")
    assert restored == original
    assert rebuilt == raw_text.encode("utf-8")
    stem = f"{reader}_{Path(filename).stem}"
    document = {
        "format": "scan024-source-literal-record-lossless-projection-v1",
        "source_only": True,
        "original_source": raw_ref,
        "literal_authorities": authorities,
        "reconstruction": "Replace {$source_record:n} with the ordered object specified by record_schemas[record_rows[n][0]] and record_rows[n][1]. Recursively replace {$literal_slice:[key,a,b]} with literal_authorities[key]'s exact UTF-8 text character slice [a,b). Serialize ensure_ascii=False, indent=2, one final LF. Every field value/order is retained; identical literal bytes in different source roles retain their own authority key. No reading is selected or rewritten.",
        "record_schemas": schemas,
        "record_rows": records,
        "payload": payload,
    }
    pinfo = put(stem + "_projection.json", document)
    readable = OUT / ("scan024_source_" + stem + "_projection.jsonl")
    lines = [json.dumps({k: v for k, v in document.items() if k not in ["record_rows", "payload"]}, ensure_ascii=False, separators=(",", ":"))]
    for k, v in payload.items():
        if isinstance(v, list):
            for i, row in enumerate(v):
                lines.append(json.dumps({"section": k, "index": i, "value": row}, ensure_ascii=False, separators=(",", ":")))
        else:
            lines.append(json.dumps({"section": k, "value": v}, ensure_ascii=False, separators=(",", ":")))
    for i, row in enumerate(records):
        lines.append(json.dumps({"record_index": i, "row": row}, ensure_ascii=False, separators=(",", ":")))
    readable.write_text("\n".join(lines) + "\n", encoding="utf-8")
    audit = {
        "scan": 24, "reader": reader, "source_only": True,
        "original_source": raw_ref, "literal_authorities": authorities,
        "projection": pinfo,
        "readable_projection": {"path": str(readable.relative_to(BASE)), "sha256_utf8": sha(readable.read_bytes()), "lines": len(lines)},
        "exact_semantic_reconstruction": restored == original,
        "exact_utf8_reconstruction": rebuilt == raw_text.encode("utf-8"),
        "reconstructed_sha256_utf8": sha(rebuilt),
        "literal_record_occurrences_verified": len(verified),
        "distinct_exact_records": len(records),
        "issues": issues,
        "verifications": verified,
        "limits": "Source text only. No image access, image/coordinate or mathematical computation, compilation or rendering. Raw reader/witness fields remain in their own roles. No final reading, count, confidence or approval supplied.",
    }
    ainfo = put(stem + "_projection_audit.json", audit)
    print(json.dumps({"projection": pinfo, "readable": audit["readable_projection"], "audit": ainfo, "issues": issues}, ensure_ascii=False))


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        build_general_projection(sys.argv[1], sys.argv[2])
    else:
        build_map_projection()
