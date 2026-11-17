"""Run and record the context searches attached to every research-note item."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re
import subprocess
from collections import Counter, defaultdict

root = Path('/workspace/scratch/89f8415d3ab0')
notes = root / 'deliver/MPL_81_038-055+154_046-076_notes.md'
context = root / 'context'
sources = [
    'README.md', 'notes/RESULTS_STATE.md', 'STATEMENTS_WITH_STATUS.md',
    'Esquisse_cote119_copy1_API_transcription.tex',
    'same_cote_154/MPL_154_077-126_notes.md',
    'same_cote_154/MPL_154_127-176_notes.md',
    'hua_project/README.md', 'hua_project/154.modern.tex',
]
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
records = []
hits_csv = []
for match in re.finditer(r'^### ([CABDOQT]\d{2}) — (.*?)(?=^### |^## |\Z)', notes.read_text(), re.M|re.S):
    ident = match.group(1)
    block = match.group(0)
    query_match = re.search(r'\*\*Search terms:\*\* ([^\n]+)', block)
    if not query_match:
        raise RuntimeError('Missing explicit query terms for ' + ident)
    terms = [t.strip().rstrip('.') for t in query_match.group(1).split(',') if t.strip()]
    patterns = [(r'\b' + re.escape(t) + r'\b') if len(t) <= 2 and t.isalnum() else re.escape(t) for t in terms]
    cmd = ['rg', '-n', '-i', '--no-heading']
    for pattern in patterns:
        cmd += ['-e', pattern]
    cmd += sources
    result = subprocess.run(cmd, cwd=context, text=True, capture_output=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(f'{ident}: {result.stderr}')
    counts = Counter()
    selected = defaultdict(list)
    for line in result.stdout.splitlines():
        filename, lineno, excerpt = line.split(':', 2)
        counts[filename] += 1
        if len(selected[filename]) < 12:
            row = {'item': ident, 'context_file': filename, 'line': int(lineno),
                   'excerpt': excerpt[:320] + (' […]' if len(excerpt)>320 else ''), 'query_utc': stamp}
            selected[filename].append(row)
            hits_csv.append(row)
    records.append({'id': ident, 'title': block.splitlines()[0], 'utc': stamp,
                    'terms': terms, 'regex_patterns': patterns,
                    'command_argv': cmd, 'exit_code': result.returncode,
                    'counts_by_file': dict(counts), 'total_matching_lines': sum(counts.values()),
                    'samples': dict(selected), 'sample_limit_per_file': 12,
                    'interpretation': 'The main note gives the assessed relation; lexical hits alone are not mathematical matches.'})

destination = root / 'deliver/records'
destination.mkdir(exist_ok=True)
(destination/'context_queries.json').write_text(json.dumps({'scope': 'Post-freeze research only; original images and frozen transcription untouched.',
        'source_files': sources, 'items': records}, ensure_ascii=False, indent=2)+'\n')
with (destination/'context_searches.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['item','context_file','line','excerpt','query_utc'])
    writer.writeheader(); writer.writerows(hits_csv)
summary = {
    'utc': stamp, 'items': len(records), 'sampled_matching_lines': len(hits_csv),
    'zero_hit_items': [r['id'] for r in records if not r['total_matching_lines']],
    'low_hit_items': {r['id']:r['total_matching_lines'] for r in records if r['total_matching_lines'] < 10},
    'coverage': {r['id']: {'matches':r['total_matching_lines'],'files':len(r['counts_by_file'])} for r in records},
}
(destination/'context_search_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='coverage'},ensure_ascii=False))
