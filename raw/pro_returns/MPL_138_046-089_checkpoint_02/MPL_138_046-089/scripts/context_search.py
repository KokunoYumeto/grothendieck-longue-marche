#!/usr/bin/env python3
"""Read-only context search with scan/page anchors. Never touches transcription.

Usage: python3 context_search.py PATTERN [filename-substring] [maximum-hits]
All searches are appended to research_searches.log with UTC timestamps.
Supplied context files themselves are never copied into the deliverable.
"""
from pathlib import Path
import datetime, re, sys

root = Path(__file__).resolve().parents[1]
context = root.parent / 'context'
pattern = sys.argv[1]
filter_name = sys.argv[2] if len(sys.argv) > 2 else ''
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 25
rx = re.compile(pattern, re.I)
rows = []
total = 0
for path in sorted(context.rglob('*')):
    if not path.is_file() or path.suffix not in {'.tex', '.md', '.txt'}:
        continue
    rel = str(path.relative_to(context))
    if filter_name and filter_name not in rel:
        continue
    scan = folio = modern = '-'
    for line_no, line in enumerate(path.read_text(errors='replace').splitlines(), 1):
        m = re.search(r'\\scanpage\{([^}]+)\}', line)
        if m: scan = m.group(1)
        m = re.search(r'\\mspage\{([^}]+)\}', line)
        if m: folio = m.group(1)
        m = re.search(r'\\pagerange\{([^}]+)\}\{([^}]+)\}', line)
        if m: modern = '-'.join(m.groups())
        if rx.search(line):
            total += 1
            if len(rows) < limit:
                rows.append(f'{rel}:{line_no} [scan {scan}; ms {folio}; modern pp {modern}] {line[:330]}')
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
out = f'\n## {stamp}\nQuery: {pattern}\nFile filter: {filter_name or "all supplied context"}\nHits: {total}; shown: {len(rows)}\n' + '\n'.join(rows) + '\n'
with (root / 'research_searches.log').open('a') as f:
    f.write(out)
print(out)
