#!/usr/bin/env python3
"""Record each A-note's keyword query across the entire supplied context.

Only research records are written. No transcription, scan, ZIP, or freeze log
is opened or changed. Matches document a search, not completeness or novelty.
"""
from pathlib import Path
import csv
import datetime
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
CONTEXT = HERE.parents[1] / 'context'
NOTES = HERE / 'notes_019-032.md'
files = sorted(p for p in CONTEXT.rglob('*') if p.is_file())
text = NOTES.read_text(encoding='utf-8')
blocks = re.findall(r'^### (A\d+) — (.*?)\n(.*?)(?=^### A\d+ —|\Z)', text, re.M | re.S)
queries = []
matches = []
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
for item_id, title, body in blocks:
    found = re.search(r'\*\*Search:\*\* `([^`]+)`', body)
    if not found:
        raise SystemExit(f'{item_id}: missing recorded query')
    pattern = found.group(1)
    run = subprocess.run(['rg', '--json', '-i', '-e', pattern, str(CONTEXT)],
                         text=True, capture_output=True)
    if run.returncode not in (0, 1):
        raise SystemExit(f'{item_id}: rg failed: {run.stderr}')
    counts = {str(p.relative_to(CONTEXT)): 0 for p in files}
    start = len(matches)
    for line in run.stdout.splitlines():
        event = json.loads(line)
        if event['type'] != 'match':
            continue
        data = event['data']
        relative = str(Path(data['path']['text']).relative_to(CONTEXT))
        counts[relative] += 1
        matches.append([item_id, pattern, relative, data['line_number'],
                        data['lines']['text'].rstrip('\r\n')])
    context = re.search(r'\*\*Context and relation:\*\* (.*?)(?=\*\*Register:)', body, re.S)
    register = re.search(r'\*\*Register:\*\* (.*?)(?:\n\n|\Z)', body, re.S)
    queries.append({'id': item_id, 'title': title, 'query': pattern,
                    'searched_at_utc': stamp, 'all_supplied_context_files': list(counts),
                    'match_counts_by_file': counts, 'total_matches': len(matches)-start,
                    'selected_context_and_relation': context.group(1).strip() if context else None,
                    'results_state_status': register.group(1).strip() if register else None,
                    'interpretation_limit': 'Keyword/object search only; no completeness or novelty inference.'})
with (HERE / 'searches_019-032.tsv').open('w', encoding='utf-8', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t')
    writer.writerow(['item_id', 'query', 'context_file', 'line', 'matched_text'])
    writer.writerows(matches)
(HERE / 'search_plan_019-032.json').write_text(json.dumps(queries, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
print(json.dumps({'notes': len(queries), 'context_files_per_note': len(files),
                  'matched_lines': len(matches), 'written_at_utc': stamp}))
