#!/usr/bin/env python3
"""Rebuild a compact, read-only context-search audit of the current research notes.

Only the named notes file and the five allowlisted supplied context texts are read.
Only context_search_ledger.json and context_search_ledger_summary.md are written.
No source is a proof oracle: these are reproducible lexical searches, not verification.
"""

from __future__ import annotations

import argparse
import bisect
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import unicodedata


RECORDS = Path(__file__).resolve().parent
WORK = RECORDS.parent
ROOT = WORK.parent
DEFAULT_NOTES = WORK / "MPL_12_051-098_notes.md"
SOURCE_PATHS = {
    "README": "context/README.md",
    "CT": "context/MPL_16+47+54+44_transcription.tex",
    "CN": "context/MPL_16+47+54+44_notes.md",
    "RS": "context/notes/RESULTS_STATE.md",
    "HU": "context/hua_project/12.modern.tex",
}
FAMILIES = ("Q", "N", "B", "SF", "W", "C", "T", "RQ")
DEFINITION = re.compile(r"^(Q\d{2,}|N\d{3,}|(?:B|SF|W|C|T|RQ)\d{2,})\b")
FIELDS = ("Kind", "Witness", "Context search", "Context", "RS")
GREEK = {
    "ℓ": "ell", "π": "pi", "ρ": "rho", "α": "alpha", "β": "beta",
    "γ": "gamma", "Γ": "Gamma", "ξ": "xi", "ζ": "zeta", "λ": "lambda",
    "φ": "varphi", "Φ": "Phi", "ε": "varepsilon", "δ": "delta",
    "∞": "infty", "≥": "ge", "≤": "le", "⊗": "otimes", "⊕": "oplus",
    "−": "-", "’": "'", "‘": "'", "–": "-", "—": "-", " ": " ",
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def stamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def fold(text: str) -> str:
    text = "".join(GREEK.get(c, c) for c in text)
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c)).casefold()


def canonical(text: str) -> str:
    """Typography only: no translation, semantic expansion, or stemming."""
    text = fold(text)
    text = re.sub(r"\\(?:mathbb|mathbf|mathcal|mathfrak|mathrm|mathit|mathsf|mathtt|"
                  r"operatorname|textbf|textit|emph|underline|overline|widehat|"
                  r"boldsymbol|check|hat|text)\b\s*", "", text)
    text = re.sub(r"\\[\(\)\[\]]|\$", "", text)
    text = re.sub(r"\\(?:quad|qquad|enspace|thinspace)\b|\\[,;!:]|~", " ", text)
    text = re.sub(r"\\(?:left|right|big|bigl|bigr)\b", "", text)
    text = re.sub(r"\\([a-z]+)", r"\1", text)
    text = re.sub(r"\b(?:geq|geqslant)\b", "ge", text)
    text = re.sub(r"\b(?:leq|leqslant)\b", "le", text)
    text = re.sub(r"q_\s*l\b", "q_ell", text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("_", "").replace("^", "")
    text = re.sub(r"(?<=[a-z])[-]+(?=[a-z])", "", text)
    text = text.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


def short(text: str, length: int = 180) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= length else text[:length - 1] + "…"


def split_top(text: str, delimiters: str) -> list[str]:
    """Split query lists, retaining commas and pipes inside TeX/math brackets."""
    result, part, depth, math = [], [], 0, False
    i = 0
    while i < len(text):
        pair = text[i:i + 2]
        if pair == r"\(":
            math = True
        elif pair == r"\)":
            math = False
        c = text[i]
        if c in "{[":
            depth += 1
        elif c in "}]":
            depth = max(0, depth - 1)
        if c in delimiters and not math and depth == 0:
            result.append("".join(part).strip(" .;,“”\"`"))
            part = []
        else:
            part.append(c)
        i += 1
    result.append("".join(part).strip(" .;,“”\"`"))
    return list(dict.fromkeys(x for x in result if x))


def terms(text: str) -> list[str]:
    return split_top(text, ";" if ";" in text else ",")


def local_refs(text: str) -> list[str]:
    refs = []
    pattern = r"\b([NQ])(\d{2,3})(?:\s*[–—-]\s*([NQ])?(\d{2,3}))?\b"
    for m in re.finditer(pattern, text):
        prefix, first, second_prefix, last = m.groups()
        width = 3 if prefix == "N" else 2
        a, b = int(first), int(last or first)
        if second_prefix and second_prefix != prefix or b < a or b - a > 300:
            refs.append(f"{prefix}{a:0{width}d}")
            continue
        refs.extend(f"{prefix}{n:0{width}d}" for n in range(a, b + 1))
    return list(dict.fromkeys(refs))


def parse_notes(text: str) -> tuple[dict, list]:
    lines = text.splitlines()
    items, errors = {}, []
    headers = [i for i, line in enumerate(lines) if re.match(r"^#{1,6} ", line)]
    header_end = {start: (headers[n + 1] if n + 1 < len(headers) else len(lines))
                  for n, start in enumerate(headers)}
    section = ""
    for i, line in enumerate(lines):
        if line.startswith("## "):
            section = line[3:]
        heading = re.match(r"^### ((?:Q\d{2,}|N\d{3,}))\s*[—–-]\s*(.*)", line)
        cells = None
        if heading:
            item_id, title = heading.groups()
            block = "\n".join(lines[i + 1:header_end[i]])
            metadata = {}
            for field in FIELDS:
                m = re.search(r"\*\*" + re.escape(field) + r":\*\*\s*(.*?)"
                              r"(?=\s*\*\*[A-Za-z][A-Za-z ]*:\*\*|\n\s*\n|\Z)",
                              block, re.S)
                metadata[field] = m.group(1).strip() if m else ""
            missing = [f for f in FIELDS if not metadata[f]]
            own = [(t, "explicit Context search") for t in terms(metadata["Context search"])]
            inherit = []
        elif line.startswith("|"):
            # The manuscript's alternatives can contain raw | within a cell.
            cells = re.split(r"\s+\|\s+", line.strip().strip("|").strip())
            match = DEFINITION.match(cells[0])
            if not match or match.group(1).startswith(("Q", "N")):
                continue
            item_id = match.group(1)
            family = re.match(r"[A-Z]+", item_id).group()
            title = cells[0][len(item_id):].strip(" —–-") or short(cells[1], 100)
            block = " | ".join(cells[1:])
            inherit = local_refs(block)
            search_parts = re.findall(r"\b(?:Context\s+)?[Ss]earch:\s*([^;|]+)", block)
            own = [(t, "explicit table search") for p in search_parts for t in terms(p)]
            inherited_kind = {
                "B": "unpursued implication", "SF": "self-flagged",
                "W": "withdrawn in the same text", "T": "unpursued implication (documentary)",
                "RQ": "reading question",
            }
            kind = title if family == "C" else inherited_kind.get(family, "")
            metadata = {"Kind": kind, "Witness": cells[1] if len(cells) > 1 else "",
                        "Context search": "; ".join(search_parts),
                        "Context": cells[-1], "RS": cells[-1]}
            missing = []
            expected = {"B": 5, "SF": 4, "W": 4, "C": 3, "T": 5, "RQ": 5}[family]
            if len(cells) != expected:
                errors.append({"item": item_id, "line": i + 1, "type": "table_column_count",
                               "actual": len(cells), "expected": expected})
            if family == "T" and len(cells) > 2:
                quotations = re.findall(r"“([^”]+)”|\"([^\"]+)\"", cells[2])
                quoted = [a or b for a, b in quotations] or [cells[2]]
                for phrase in quoted:
                    own.append((phrase, "section rule: quoted heading"))
                    # Section 6 explicitly permits distinctive title words.
                    stop = {"avec", "dans", "pour", "sur", "cette", "celle", "leurs", "toute",
                            "tous", "quelconque", "precedente", "type", "base", "points"}
                    for word in re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ-]{4,}", phrase):
                        if fold(word) not in stop:
                            own.append((word, "section rule: distinctive heading word"))
            if family == "RQ" and len(cells) > 2:
                # Section 7 directs searching words/math objects in the reading columns.
                own.extend((m.group(), "section rule: frozen-reading mathematical object")
                           for m in re.finditer(r"\\\(.*?\\\)", cells[2]))
                own.extend((a or b, "section rule: frozen-reading quotation")
                           for a, b in re.findall(r"“([^”]+)”|\"([^\"]+)\"", cells[2]))
        else:
            continue
        if item_id in items:
            errors.append({"item": item_id, "line": i + 1, "type": "duplicate_definition"})
            continue
        family = re.match(r"[A-Z]+", item_id).group()
        items[item_id] = {"family": family, "title": title, "line": i + 1,
                          "section": section, "metadata": metadata,
                          "own_terms": list(dict.fromkeys(own)), "inherits": inherit}
        if missing:
            errors.append({"item": item_id, "line": i + 1, "type": "missing_metadata",
                           "fields": missing})
    for item_id, item in items.items():
        unresolved = [ref for ref in item["inherits"] if ref not in items]
        if unresolved:
            errors.append({"item": item_id, "type": "unresolved_local_references", "refs": unresolved})
        if not item["own_terms"] and not item["inherits"]:
            errors.append({"item": item_id, "type": "no_search_terms_or_inheritance"})
    return items, errors


def tex_heading(lines: list[str], i: int) -> str | None:
    if not re.match(r"\\(?:sub)*section\*?\{", lines[i]):
        return None
    text = " ".join(lines[i:i + 4])
    start = text.index("{") + 1
    depth = 1
    for n in range(start, len(text)):
        depth += (text[n] == "{") - (text[n] == "}")
        if depth == 0:
            return short(text[start:n], 230)
    return short(text[start:], 230)


def source_index(key: str, path: Path) -> dict:
    data = path.read_bytes()
    lines = data.decode("utf-8-sig").splitlines()
    locators, heading, pages, cote, scan = [], "", None, None, None
    heads = {}
    for i, line in enumerate(lines):
        md = re.match(r"^(#{1,6})\s+(.*)", line)
        if md:
            depth = len(md.group(1))
            heads = {k: v for k, v in heads.items() if k < depth}
            heads[depth] = md.group(2)
            heading = " / ".join(heads.values())
        if key == "CT":
            c = re.search(r"\\cotefile\{(\d+)\}", line)
            s = re.search(r"\\scanpage\{(\d+)\}", line)
            if c:
                cote, scan = int(c.group(1)), None
            if s:
                scan = int(s.group(1))
            loc = {"cote": cote, "scan": scan}
        elif key == "HU":
            p = re.match(r"\\pagerange\{(\d+)\}\{(\d+)\}", line)
            if p:
                pages = [int(p.group(1)), int(p.group(2))]
            h = tex_heading(lines, i)
            if h:
                heading = h
            page_phrase = re.search(r"\((pages? [^)]+)\)", heading)
            loc = {"cote": 12, "heading": heading or "TeX preamble",
                   "page_scope": page_phrase.group(1) if page_phrase else None,
                   "pagerange_macro": pages}
        else:
            loc = {"heading": heading or "Opening"}
            if key == "CN":
                c = re.search(r"(?:^| / )(\d+):(\d+):\d+", heading)
                if c:
                    loc.update(cote=int(c.group(1)), scan=int(c.group(2)))
            if key == "RS":
                e = re.match(r"- \*\*([^*]+)\*\*", line)
                if e:
                    loc["entry"] = e.group(1)
        locators.append(loc)
    # Search both actual Unicode/TeX text and a typography-normalized view.
    # Do not cross a scan/heading/page-scope boundary when matching a phrase.
    blocks = []
    first = 0
    for i in range(1, len(lines) + 1):
        if i < len(lines) and locators[i] == locators[first]:
            continue
        views = {}
        for name, function in (("folded_literal", fold), ("tex_typography", canonical)):
            normalized = [function(x) for x in lines[first:i]]
            offsets, offset = [], 0
            for line in normalized:
                offsets.append(offset)
                offset += len(line) + 1
            views[name] = ("\n".join(normalized), offsets)
        blocks.append({"start": first, "end": i, "locator": locators[first], "views": views})
        first = i
    return {"key": key, "path": str(path.relative_to(ROOT)), "sha256": sha(data),
            "bytes": len(data), "line_count": len(lines), "lines": lines,
            "locators": locators, "blocks": blocks}


def query_pattern(term: str, mode: str) -> re.Pattern | None:
    mathematical = bool(re.search(r"\\|[_^=<>]|[α-ωΓΦξζ]|^A\(|^B\(|^C\(|^D\(", term))
    value = fold(term) if mode == "folded_literal" else canonical(term)
    value = value.strip()
    if not value:
        return None
    if mode == "tex_typography" and mathematical:
        value = re.sub(r"\s+", "", value)
        pattern = r"\s*".join(re.escape(c) for c in value)
    else:
        pattern = r"\s+".join(re.escape(p) for p in re.split(r"\s+", value))
    # Avoid one-letter mathematical objects and 'sl' becoming substrings of prose.
    if mathematical or re.fullmatch(r"[a-z]{1,3}", value):
        pattern = r"(?<![a-z])" + pattern + r"(?![a-z])"
    return re.compile(pattern)


def search_query(term: str, source: dict) -> list[dict]:
    hits = {}
    for mode in ("folded_literal", "tex_typography"):
        pattern = query_pattern(term, mode)
        if pattern is None:
            continue
        for block in source["blocks"]:
            text, offsets = block["views"][mode]
            for match in pattern.finditer(text):
                a = block["start"] + bisect.bisect_right(offsets, match.start()) - 1
                b = block["start"] + bisect.bisect_right(offsets, max(match.start(), match.end() - 1)) - 1
                hit = hits.setdefault((a, b), {"source": source["key"], "line": a + 1,
                                               "line_end": b + 1, "locator": block["locator"],
                                               "modes": [], "term": term})
                if mode not in hit["modes"]:
                    hit["modes"].append(mode)
    return list(hits.values())


def number_set(text: str) -> set[int]:
    values = set()
    for m in re.finditer(r"(\d+)(?:\s*[–—-]\s*(\d+))?", text):
        a, b = int(m.group(1)), int(m.group(2) or m.group(1))
        if 0 <= b - a <= 200:
            values.update(range(a, b + 1))
    return values


def preferences(item: dict) -> dict:
    text = item["metadata"].get("Context", "")
    ct = defaultdict(set)
    for m in re.finditer(r"CT(\d+)/(\d+(?:[–—-]\d+)?(?:\s*(?:,|and|et)\s*\d+(?:[–—-]\d+)?)*)", text):
        ct[int(m.group(1))].update(number_set(m.group(2)))
    pages = set()
    for m in re.finditer(r"\bpp?\.?\s*(\d+(?:\s*[–—-]\s*\d+)?(?:\s*,\s*\d+(?:[–—-]\d+)?)*)", text):
        pages.update(number_set(m.group(1)))
    return {"ct": ct, "hu": pages, "rs": fold(item["metadata"].get("RS", ""))}


def rank_hit(hit: dict, pref: dict) -> tuple:
    loc, score = hit["locator"], 0
    if hit["source"] in ("CT", "CN"):
        cote, scan = loc.get("cote"), loc.get("scan")
        if cote in pref["ct"]:
            score += 50 + 150 * (scan in pref["ct"][cote])
    if hit["source"] == "HU":
        pages = number_set(loc.get("page_scope") or "")
        if not pages and loc.get("pagerange_macro"):
            a, b = loc["pagerange_macro"]
            pages = set(range(a, b + 1))
        if pages & pref["hu"]:
            score += 200
        if loc.get("heading") == "TeX preamble":
            score -= 500
    if hit["source"] == "RS" and loc.get("entry"):
        if fold(loc["entry"]).rstrip(":") in pref["rs"]:
            score += 200
    return (-score, -min(len(canonical(hit["term"])), 25), hit["line"])


def locator_label(key: str, loc: dict) -> str:
    if key == "CT":
        return f"CT{loc.get('cote')}/{loc.get('scan', 0):03d}" if loc.get("scan") else "CT opening"
    if key == "HU":
        page = loc.get("page_scope") or str(loc.get("pagerange_macro") or "unpaginated")
        return "HU " + page + "; " + short(loc.get("heading", ""), 90)
    if key == "RS" and loc.get("entry"):
        return "RS " + loc["entry"]
    return key + " " + short(loc.get("heading", ""), 120)


def build(notes_path: Path, sample_limit: int) -> tuple[dict, str]:
    started = stamp()
    notes_data = notes_path.read_bytes()
    items, diagnostics = parse_notes(notes_data.decode("utf-8-sig"))
    sources, source_records = {}, {}
    for key, relative in SOURCE_PATHS.items():
        path = ROOT / relative
        if not path.is_file():
            source_records[key] = {"path": relative, "status": "missing"}
            diagnostics.append({"source": key, "type": "missing_allowlisted_context_file", "path": relative})
            continue
        source = source_index(key, path)
        sources[key] = source
        source_records[key] = {k: source[k] for k in ("path", "sha256", "bytes", "line_count")}
        source_records[key]["status"] = "searched"
    queries, results = {}, {}
    for item_id, item in items.items():
        bindings = defaultdict(set)
        own = item.pop("own_terms")
        all_terms = [(t, origin, item_id) for t, origin in own]
        for ref in item["inherits"]:
            if ref in items:
                raw = items[ref]["metadata"].get("Context search", "")
                all_terms.extend((t, "inherited Context search", ref) for t in terms(raw))
        for term, origin, owner in all_terms:
            query_id = "q_" + sha(fold(term).encode())[:12]
            if query_id not in queries:
                queries[query_id] = {"term": term, "canonical": canonical(term), "items": [], "sources": {}}
                results[query_id] = {key: search_query(term, source) for key, source in sources.items()}
            bindings[query_id].add((origin, owner))
            if item_id not in queries[query_id]["items"]:
                queries[query_id]["items"].append(item_id)
        item["queries"] = [{"query": q, "origins": [{"kind": a, "item": b} for a, b in sorted(v)]}
                           for q, v in bindings.items()]
        if not bindings:
            diagnostics.append({"item": item_id, "type": "no_resolved_queries"})
    hits = {}

    def retain(hit: dict) -> str:
        # Do not reproduce the supplied context. The matched query is already
        # recorded elsewhere; exact coordinates are sufficient for inspection.
        identity = f"{hit['source']}:{hit['line']}:{hit['line_end']}"
        hit_id = "h_" + sha(identity.encode())[:12]
        hits.setdefault(hit_id, {"source": hit["source"], "line": hit["line"],
                                 "line_end": hit["line_end"], "locator": hit["locator"]})
        return hit_id

    for query_id, query in queries.items():
        for key, found in results[query_id].items():
            examples = sorted(found, key=lambda h: (h["locator"].get("heading") == "TeX preamble", h["line"]))
            query["sources"][key] = {"hit_spans": len(found),
                                     "matched_modes": sorted({m for h in found for m in h["modes"]}),
                                     "examples": [retain(h) for h in examples[:sample_limit]]}
    for item_id, item in items.items():
        pref = preferences(item)
        item["coverage"] = {}
        query_ids = [q["query"] for q in item["queries"]]
        item["zero_hit_queries"] = [q for q in query_ids if not any(results[q].values())]
        for key in sources:
            candidates = [(q, h) for q in query_ids for h in results[q][key]]
            candidates.sort(key=lambda qh: rank_hit(qh[1], pref))
            chosen, seen = [], set()
            for query_id, hit in candidates:
                line_key = (hit["line"], hit["line_end"])
                if line_key in seen:
                    continue
                seen.add(line_key)
                if len(chosen) < sample_limit:
                    chosen.append({"query": query_id, "hit": retain(hit)})
            item["coverage"][key] = {
                "matching_queries": sum(bool(results[q][key]) for q in query_ids),
                "distinct_hit_spans": len(seen), "examples": chosen,
            }
        if not any(c["matching_queries"] for c in item["coverage"].values()):
            diagnostics.append({"item": item_id, "type": "all_queries_zero_hit",
                                "meaning": "No lexical match; not proof of no thematic relationship."})
        item["metadata"] = {k: short(v, 700) for k, v in item["metadata"].items()}
    final_notes_hash = sha(notes_path.read_bytes())
    changed = final_notes_hash != sha(notes_data)
    if changed:
        diagnostics.append({"type": "notes_changed_during_run", "action": "Rerun against the final notes."})
    family_counts = dict(Counter(i["family"] for i in items.values()))
    report = {
        "schema": "mpl-context-search-ledger-v1", "started_utc": started, "completed_utc": stamp(),
        "notes": {"path": str(notes_path.relative_to(ROOT)), "sha256": sha(notes_data),
                  "sha256_at_completion": final_notes_hash, "bytes": len(notes_data),
                  "changed_during_run": changed},
        "sources": source_records,
        "method": {
            "scope": "Only the five allowlisted supplied text files; no scans, OCR, PDFs, web, or other returns.",
            "matching": "Accent/case-folded literal search plus declared TeX/Unicode typography normalization; phrase whitespace may span lines within one locator; no translation or semantic expansion.",
            "terms": "Q/N explicit metadata; tables inherit named Q/N ranges and slash references; table Search/search clauses retained; T title quotations/words and RQ frozen-reading quotations/formulas follow section rules.",
            "short_terms": "Math objects and alphabetic terms of at most three letters use alphabetic token boundaries; explicitly truncated longer words remain substring searches.",
            "counts": "Counts are distinct matched line spans, merging the two search modes; examples are capped and do not enumerate every occurrence.",
            "sampling": "Global query examples follow source order; per-item examples prefer the item's declared CT scans, HU page scopes, and RS IDs, then longer queries.",
            "non_reproduction": "No context snippets or source bodies are emitted. Only query terms, source hashes, match counts, and text/scan/page-scope/heading coordinates are retained; original sources remain in the user's attachments.",
            "locators": "CT scan locators are exact; HU locators are the synthesis's declared page scope/heading, not an independently verified unique manuscript page; both HU heading and pagerange macro are retained when they differ.",
            "caution": "A lexical hit verifies neither the manuscript reading nor the mathematical claim; a zero-hit term does not exclude a thematic match. CT/CN and RS remain unreviewed supplied leads; HU remains Hua's credited interpretation.",
            "examples_per_query_source_and_item_source": sample_limit,
            "subordinate_rows": "S15a-h belong to Q10 and are not additional numbered Q/N/B/SF/W/C/T/RQ definitions; bibliography and RS crosswalk rows are not duplicate items.",
        },
        "counts": {"items": len(items), "families": family_counts, "unique_queries": len(queries),
                   "retained_hit_locations": len(hits), "zero_hit_queries": sum(not any(results[q].values()) for q in queries)},
        "diagnostics": diagnostics, "items": items, "queries": queries, "hits": hits,
    }
    return report, make_summary(report)


def make_summary(report: dict) -> str:
    items, queries, hits = report["items"], report["queries"], report["hits"]
    counts = report["counts"]
    out = ["# Context-search ledger: summary", "", f"Generated: {report['completed_utc']}", "",
           f"Notes: `{report['notes']['path']}`", "", f"Notes SHA-256: `{report['notes']['sha256']}`", "",
           f"**{counts['items']} items; {counts['unique_queries']} distinct query strings; "
           f"{counts['zero_hit_queries']} query strings with no match in the searched text.**", "",
           "This is a lexical search audit. A hit is not verification of an assertion; a zero-hit exact term does not imply absence of a thematic match. The JSON links each item to its own/inherited queries, per-source counts, and exact text/scan/page-scope/heading coordinates. **No context snippets or source bodies are reproduced**; the original sources remain in the user's attachments and are not part of these deliverables.", "",
           "## Definition coverage", "", "| Family | Defined items |", "|---|---:|"]
    out += [f"| {family} | {counts['families'].get(family, 0)} |" for family in FAMILIES]
    out += ["", "S15a–h are subordinate to Q10, not extra numbered definitions. IDs and inheritance are parsed afresh on every run.", "",
            "## Searched sources", "", "| Key | Supplied text | Lines | Status | SHA-256 |", "|---|---|---:|---|---|"]
    for key, source in report["sources"].items():
        out.append(f"| {key} | `{source['path']}` | {source.get('line_count', '—')} | {source['status']} | `{source.get('sha256', '—')}` |")
    out += ["", "No other context files, images, OCR, PDFs, external pages, or named prior returns were searched. Cote 13/14/15/18 original leaves and the full returns referenced by RS are not supplied as direct text within this allowlist; their mentions are register/context leads. Oda's supplied PDF is outside this text-search ledger and remains a separate published-source check.", "",
            "## Metadata and missing-context diagnostics", ""]
    if report["diagnostics"]:
        for problem in report["diagnostics"]:
            out.append("- `" + json.dumps(problem, ensure_ascii=False, sort_keys=True) + "`")
    else:
        out.append("No missing allowlisted file, duplicate definition, malformed table width, missing required Q/N metadata field, unresolved local query reference, or queryless item was detected.")
    out += ["", "The page locator for HU is a declared scope in the modernized synthesis. Its headings sometimes include nonconsecutive pages or differ from its pagerange macro; the JSON retains both without inventing a unique-page assignment.", "",
            "## Zero-hit query strings", "", "Exact absence below is a search result, not a mathematical or documentary conclusion.", "",
            "| Query as written/derived | Items using it |", "|---|---|"]
    zero = [q for q in queries.values() if not any(s["hit_spans"] for s in q["sources"].values())]
    for q in zero:
        escaped = q["term"].replace("|", "\\|")
        out.append(f"| {escaped} | {', '.join(q['items'])} |")
    if not zero:
        out.append("| None | — |")
    out += ["", "## Per-item search coverage", "",
            "Each source count is the number of that item's query strings with a hit, not the number of proven claims. Detailed source-specific zeroes and capped located matches are in JSON.", "",
            "| Item | Notes line | Queries | Inherits | README / CT / CN / RS / HU | Zero-hit terms |", "|---|---:|---:|---|---|---|"]
    for item_id, item in items.items():
        coverage = " / ".join(str(item["coverage"].get(k, {}).get("matching_queries", 0)) for k in SOURCE_PATHS)
        z = "; ".join(queries[q]["term"] for q in item["zero_hit_queries"]).replace("|", r"\|")
        out.append(f"| {item_id} | {item['line']} | {len(item['queries'])} | {', '.join(item['inherits']) or '—'} | {coverage} | {z or '—'} |")
    out += ["", "## Reading the compact JSON", "",
            "- `items[ID].queries` gives query IDs and their precise own/inherited origin.",
            "- `queries[query_id].sources` gives per-source hit-span totals and sample hit IDs.",
            "- `items[ID].coverage` gives additional samples ranked toward that item's declared context locators.",
            "- `hits[hit_id]` supplies source key, exact text line span, and CT scan/HU page-scope/RS heading or entry; `sources[key].path` resolves the file. No source passage is copied.",
            "- The source and notes hashes identify the searched snapshot. If the notes change, rerun; no earlier reading or research status is overwritten by a hit.", "",
            "## Rerun", "", "```bash", "python3 MPL_12_051-098_work/records/context_search_ledger.py", "```", "",
            "Run from the workspace root. The script also resolves its default paths from its own location, so that same absolute script path works from another directory. It writes only the two context-search-ledger outputs beside itself.", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--samples-per-source", type=int, default=2)
    args = parser.parse_args()
    notes = args.notes.resolve()
    if notes != DEFAULT_NOTES.resolve():
        parser.error("Only the designated current notes file is allowed.")
    if not 1 <= args.samples_per_source <= 5:
        parser.error("--samples-per-source must be between 1 and 5.")
    report, summary = build(notes, args.samples_per_source)
    json_path = RECORDS / "context_search_ledger.json"
    summary_path = RECORDS / "context_search_ledger_summary.md"
    for path, content in ((json_path, json.dumps(report, ensure_ascii=False, separators=(",", ":")) + "\n"),
                          (summary_path, summary)):
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(path)
    print(json.dumps({"outputs": [str(json_path), str(summary_path)], "counts": report["counts"],
                      "diagnostics": report["diagnostics"], "notes_sha256": report["notes"]["sha256"]},
                     ensure_ascii=False, indent=2))
    return 3 if report["notes"]["changed_during_run"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
