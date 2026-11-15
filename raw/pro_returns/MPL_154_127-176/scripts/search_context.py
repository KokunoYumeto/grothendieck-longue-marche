#!/usr/bin/env python3
"""Record a per-note search of the supplied, unfrozen research context.

This script never opens or changes manuscript transcription files.
The context lives outside the deliverable directory and is not packaged.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, subprocess, hashlib

p = argparse.ArgumentParser()
p.add_argument('note_id')
p.add_argument('patterns', nargs='+')
p.add_argument('--ledger', default='root_context_searches.jsonl')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
context = root.parent / 'context'
files = sorted(q for q in context.rglob('*') if q.suffix in {'.md', '.tex'})
cmd = ['rg', '-n', '-i', '--no-heading']
for pattern in a.patterns:
    cmd += ['-e', pattern]
cmd += [str(q) for q in files]
proc = subprocess.run(cmd, text=True, capture_output=True)
if proc.returncode not in (0, 1):
    raise SystemExit(proc.stderr)
hits = proc.stdout.replace(str(context) + '/', '').splitlines()
record = {
    'note_id': a.note_id,
    'searched_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'patterns_regex_case_insensitive': a.patterns,
    'files_searched': [str(q.relative_to(context)) for q in files],
    'context_sha256': {str(q.relative_to(context)): hashlib.sha256(q.read_bytes()).hexdigest() for q in files},
    'matched_lines': hits,
    'absence_scope': 'A zero result is absence from the supplied context only, not from the archive or literature.',
}
ledger = root / 'records' / a.ledger
with ledger.open('a', encoding='utf-8') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(f"{a.note_id}: {len(hits)} matching lines; recorded in {ledger.name}")
for hit in hits[:5]:
    print(hit[:240])
if len(hits) > 5:
    print(f"Full {len(hits)}-line result retained in ledger.")
