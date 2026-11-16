#!/usr/bin/env python3
"""Run and record each final research item's contextual query using ripgrep.

This operates only on supplied text context after freeze. It never reads images
or edits the transcription. The context folder is outside the deliverable root.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CTX = ROOT.parent / 'context'
SOURCES = [
    CTX / 'MPL_16+47+54+44_transcription.tex',
    CTX / 'MPL_16+47+54+44_notes.md',
    CTX / 'MPL_16+47+54+44_doubts.md',
    CTX / 'notes/RESULTS_STATE.md',
]
text = (ROOT / 'MPL_60_002-035_notes.md').read_text()
items = []
for m in re.finditer(r'(?ms)^#{3,4} ((?:F|C|RT)\d+) — ([^\n]+)\n(.*?)(?=^#{2,4} |\Z)', text):
    q = re.search(r'\*\*Context query:\*\* `([^`]+)`', m.group(3))
    if q is None:
        raise ValueError('Missing query for ' + m.group(1))
    items.append((m.group(1), m.group(2), q.group(1)))
assert len(items) == 129, len(items)

locations = {}
cote = scan = None
for n, line in enumerate(SOURCES[0].read_text().splitlines(), 1):
    c = re.search(r'\\cotefile\{([^}]+)\}', line)
    s = re.search(r'\\scanpage\{([^}]+)\}', line)
    if c:
        cote = c.group(1)
    if s:
        scan = s.group(1)
    locations[n] = f'{cote}/{int(scan):03d}' if cote is not None and scan is not None else 'preamble'

def run(item):
    ident, title, query = item
    proc = subprocess.run(['rg', '-n', '-i', '--with-filename', '--', query, *map(str, SOURCES)], text=True, capture_output=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError(f'{ident}: {proc.stderr}')
    hits = {str(p.relative_to(CTX)): [] for p in SOURCES}
    for line in proc.stdout.splitlines():
        path, n, fragment = line.split(':', 2)
        hits[str(Path(path).relative_to(CTX))].append(int(n))
    ct = hits[SOURCES[0].name]
    return {'id': ident, 'title': title, 'query': query,
            'ct_scans': list(dict.fromkeys(locations[n] for n in ct)),
            'matching_lines': hits}

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(run, items))
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(ROOT / 'records/item_context_searches.json').write_text(json.dumps({'searched_at': stamp, 'source_files': [str(p.relative_to(CTX)) for p in SOURCES], 'items': results}, ensure_ascii=False, indent=2)+'\n')
out = ['# Per-item context searches', '', f'Executed {stamp}, after the recorded freeze.', '',
       'Each query was applied case-insensitively with ripgrep to the full supplied CT, CN, CD, and RS text files. These are discovery hits, not endorsements of every match. The notes themselves identify the relevant witnesses and exclude unrelated matches. This log records every CT scan hit and up to the first twenty line numbers per other file; the accompanying JSON retains all line numbers.', '']
for r in results:
    out.extend([f"## {r['id']} — {r['title']}", '', f"Query: `{r['query']}`", '', 'CT scans: '+(', '.join(r['ct_scans']) or 'no matches')+'.', ''])
    for filename, lines in r['matching_lines'].items():
        if filename == SOURCES[0].name:
            continue
        label = ', '.join(map(str, lines[:20])) or 'none'
        if len(lines) > 20:
            label += f' (first 20 of {len(lines)})'
        out.append(f'- `{filename}`: {label}.')
    out.append('')
(ROOT / 'records/item_context_searches.md').write_text('\n'.join(out)+'\n')
print(f'Searched and logged {len(results)} item queries against all four context files')
