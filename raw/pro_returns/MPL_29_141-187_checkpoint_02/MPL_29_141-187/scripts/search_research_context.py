#!/usr/bin/env python3
"""Run explicit per-note rg queries against the already-opened supplied context.

This is research documentation, never a transcription aid. Query inputs are
TSV columns note_id and query. All matches are counted; at most 12 short match
excerpts per note are retained so the supplied context is not copied wholesale.
"""
import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path
import subprocess

p = argparse.ArgumentParser()
p.add_argument('context', type=Path)
p.add_argument('queries', type=Path)
p.add_argument('output', type=Path)
args = p.parse_args()
with args.queries.open(encoding='utf-8', newline='') as f:
    queries = list(csv.DictReader(f, delimiter='\t'))
args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['note_id', 'searched_utc', 'query', 'match_count', 'file', 'line', 'excerpt'])
    for q in queries:
        cmd = ['rg', '-n', '-i', '--no-heading', '--color', 'never', '--', q['query'], str(args.context)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode not in (0, 1):
            raise RuntimeError(f"rg failed for {q['note_id']}: {r.stderr}")
        hits = r.stdout.splitlines()
        stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        for hit in hits[:12]:
            path, line, excerpt = hit.split(':', 2)
            writer.writerow([q['note_id'], stamp, q['query'], len(hits), str(Path(path).relative_to(args.context)), line, excerpt[:190]])
        if not hits:
            writer.writerow([q['note_id'], stamp, q['query'], 0, '(no match)', '', ''])
print(f'Searched {len(queries)} note queries; wrote {args.output}')
