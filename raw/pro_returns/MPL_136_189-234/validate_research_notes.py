"""Check research notes without touching the frozen transcription."""
from pathlib import Path
import csv
import re
from collections import Counter
from research_items import ITEMS
ROOT = Path(__file__).resolve().parent
notes = (ROOT/'MPL_136_189-234_notes.md').read_text(encoding='utf-8')
ids = {x['id'] for x in ITEMS}
assert len(ids) == len(ITEMS) == 94
assert len(re.findall(r'^### (?:R\d{3}|SF\d{2}|TC\d{2}) —',notes,re.M)) == 94
assert Counter(x['id'][:2] if not x['id'].startswith('R') else 'R' for x in ITEMS) == {'R':67,'SF':19,'TC':8}
for item in ITEMS:
    assert 1 <= len(item['sentences']) <= 4, item['id']
    assert item['queries'] and item['scans'] and item['anchor'], item['id']
    assert any('Context comparison:' in x for x in item['sentences']), item['id']
    if item['kind'] == 'own idea':
        assert item['confidence'] and any('because' in x for x in item['sentences']),item['id']
    if item['kind'] == 'withdrawn in same text':
        assert ',' in item['scans'] or '–' in item['scans'],item['id']
rows = list(csv.DictReader((ROOT/'context_search_log.csv').open(encoding='utf-8')))
assert {r['note_id'] for r in rows} == ids
for item in ITEMS:
    assert sum(r['note_id'] == item['id'] for r in rows) == len(item['queries'])*5,item['id']
for reference in re.findall(r'\b(?:R\d{3}|SF\d{2}|TC\d{2})\b',notes):
    assert reference in ids,reference
for author in ['Cartan','Cenkl','Dwyer','Ekedahl','Hatcher','Horel','Mandell','Miller','Scheerer','Stacks Project Authors','Toën']:
    assert re.search(r'^'+re.escape(author)+r'[, .]',notes,re.M),author
assert 'TODO' not in notes and 'TBD' not in notes
print(f'Validated {len(ITEMS)} items, sentence-block limits, own-idea reasons, cross-references, bibliography coverage, and {len(rows)} context-search rows.')
