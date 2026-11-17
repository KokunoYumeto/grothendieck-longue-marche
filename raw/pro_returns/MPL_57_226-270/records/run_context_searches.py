"""Record the stated context search for every numbered research note.

Read-only with respect to all transcription and supplied context files.
The main notes supply the actual comparisons; hit counts are not proof.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import json
import re
import subprocess

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent
CONTEXT = ROOT / 'context'
FILES = sorted(p for p in CONTEXT.rglob('*') if p.suffix in ('.md', '.tex'))
notes = (BASE / 'MPL_57_226-270_notes.md').read_text(encoding='utf-8')
blocks = re.split(r'(?=^### [A-Z]\d{2} — )', notes, flags=re.M)[1:]
rows = []
for block in blocks:
    heading = block.splitlines()[0]
    note_id = re.match(r'### ([A-Z]\d{2})', heading).group(1)
    query = re.search(r'\*\*Search:\*\* ([^\n]+)', block)
    if not query:
        raise ValueError(f'{note_id}: missing search terms')
    terms = [s.strip() for s in query.group(1).split('|') if s.strip()]
    argv = ['rg', '--json', '--ignore-case', '--fixed-strings']
    for term in terms:
        argv += ['-e', term]
    argv += [str(p) for p in FILES]
    proc = subprocess.run(argv, text=True, capture_output=True, encoding='utf-8')
    if proc.returncode not in (0, 1):
        raise RuntimeError(f'{note_id}: {proc.stderr}')
    hits = defaultdict(list)
    matched_forms = set()
    for line in proc.stdout.splitlines():
        result = json.loads(line)
        if result['type'] != 'match':
            continue
        data = result['data']
        file = str(Path(data['path']['text']).relative_to(ROOT))
        hits[file].append({'line': data['line_number'],
                           'excerpt': data['lines']['text'].strip()[:480]})
        for submatch in data['submatches']:
            matched_forms.add(submatch['match']['text'].casefold())
    rows.append({
        'note_id': note_id,
        'title': heading.removeprefix('### '),
        'searched_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        'method': 'rg --json --ignore-case --fixed-strings; terms combined by OR',
        'terms': terms,
        'terms_with_no_literal_hit': [t for t in terms if t.casefold() not in matched_forms],
        'searched_files': [str(p.relative_to(ROOT)) for p in FILES],
        'matched_line_count': sum(len(v) for v in hits.values()),
        'matches': {file: {'count': len(found),
                           'lines': [v['line'] for v in found],
                           'first_examples': found[:3]}
                    for file, found in sorted(hits.items())},
        'scope': 'Supplied textual context only; Oda PDF inspected separately. '
                 'Literal hit counts do not establish relevance or absence of a theorem.'
    })
ids = [r['note_id'] for r in rows]
assert len(ids) == len(set(ids))
(BASE / 'records/context_searches.jsonl').write_text(
    ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
out = ['# Per-note context-search register', '',
       'Every numbered note was searched against all eight supplied textual context files. '
       'These literal searches supplement the section-by-section research recorded in the '
       'notes and the other research records; they do not replace conceptual comparison. '
       'The supplied Oda PDF was inspected separately, using its printed text and page images.', '',
       'The JSONL record retains each query, searched file list, every matching line number, '
       'and the first three short examples in each matching file. A term with no literal hit '
       'may still have a relevant synonym or a mathematical equivalent.', '',
       '| Note | Matching lines | Files with hits | Literal terms without hits |',
       '|---|---:|---:|---|']
for row in rows:
    missing = ', '.join('`' + t.replace('|', '/') + '`' for t in row['terms_with_no_literal_hit']) or '—'
    out.append(f"| {row['note_id']} | {row['matched_line_count']} | {len(row['matches'])} | {missing} |")
out += ['', f'Total: **{len(rows)} notes**, **{len(FILES)} textual context files**.', '',
        'An empty literal result is bounded to this packet. No search of the unsupplied archive '
        'or of other personal files is claimed.', '']
(BASE / 'records/context_search_summary.md').write_text('\n'.join(out), encoding='utf-8')
print(json.dumps({'notes': len(rows), 'files': len(FILES), 'ids': ids}, ensure_ascii=False))
