#!/usr/bin/env python3
"""Search the supplied text context once for every research-note item.

This script never opens or changes a manuscript transcription page. It records
queries, hit counts, and bounded excerpts for reproducible research comparisons.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import argparse

ROOT = Path(__file__).resolve().parents[1]
CONTEXT = ROOT.parent / "context"

def search_memo(path, current_utc):
    content = path.read_text()
    items = re.split(r"(?m)(?=^### [A-Z]+\d+\b)", content)
    results = []
    for item in items:
        heading = re.match(r"### ([A-Z]+\d+)\s*[—–-]\s*(.+)", item)
        if not heading:
            continue
        query = re.search(r"\*\*Search terms:\*\*\s*(.+)", item)
        if not query:
            results.append({"id": heading[1], "title": heading[2],
                            "error": "No explicit Search terms metadata"})
            continue
        terms = [t.strip().strip(chr(96)) for t in query[1].split("|") if t.strip()]
        command = ["rg", "-n", "-i", "-F", "--glob", "*.md", "--glob", "*.tex"]
        for term in terms:
            command += ["-e", term]
        command += [str(CONTEXT)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode not in (0, 1):
            raise RuntimeError(result.stderr)
        lines = result.stdout.splitlines()
        hits, excerpts = {}, []
        for line in lines:
            p, number, excerpt = line.split(":", 2)
            relative = str(Path(p).relative_to(CONTEXT))
            hits[relative] = hits.get(relative, 0) + 1
            if hits[relative] <= 6:
                excerpts.append({"file": relative, "line": int(number),
                                 "excerpt": excerpt[:500]})
        results.append({"id": heading[1], "title": heading[2], "terms": terms,
                        "hit_counts": hits, "selected_search_excerpts": excerpts})
    out = {
        "memo": str(path.relative_to(ROOT)),
        "searched_utc": current_utc,
        "timestamp_source": "clock service, passed explicitly by the primary agent",
        "context_files": {
            str(p.relative_to(CONTEXT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(CONTEXT.rglob("*")) if p.suffix in (".md", ".tex")
        },
        "notes": results,
    }
    dest = ROOT / "records" / (path.stem + "_context_searches.json")
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "memo": path.name, "items": len(results),
        "missing_query": [x["id"] for x in results if "error" in x],
        "no_hits": [x["id"] for x in results if not x.get("hit_counts", {})],
        "record": str(dest.relative_to(ROOT))
    }, ensure_ascii=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--utc", required=True)
    parser.add_argument("memos", nargs="+")
    args = parser.parse_args()
    for arg in args.memos:
        search_memo(Path(arg).resolve(), args.utc)
