#!/usr/bin/env python3
"""Check deliverable coverage and provenance metadata, without judging readings."""
from pathlib import Path
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from package_tools import validate, verify_frozen

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'
notes = (ROOT / 'MPL_84_097-145_notes.md').read_text()
expected = {f'{prefix}{n:02}' for prefix, count in [('A',40),('B',26),('C',8),('D',24),('P',2)] for n in range(1,count+1)}
headings = list(re.finditer(r'^### ([ABCDP]\d{2}) — [^\n]+', notes, re.M))
ids = [m.group(1) for m in headings]
assert len(ids) == len(set(ids)) == 100
assert set(ids) == expected
missing_metadata = []
for index, match in enumerate(headings):
    end = headings[index+1].start() if index+1 < len(headings) else len(notes)
    item = notes[match.end():end]
    # End the item before any new structural section.
    next_section = re.search(r'^## ', item, re.M)
    if next_section:
        item = item[:next_section.start()]
    for token in ('**Source:**', '**Kind:**', '**Context'):
        if token not in item:
            missing_metadata.append((match.group(1), token))
    if '**Kind:** own idea' in item:
        assert '**Confidence:**' in item, match.group(1)
    filenames = re.findall(r'MPL_84_097-145_84_scan\d{3}\.tex', item)
    if 'pages/MPL_84_097-145_84_scanNNN.tex' in item:
        # The all-packet archival item explicitly cites every supplied fragment.
        packet_files = list((ROOT / 'pages').glob('MPL_84_097-145_84_scan???.tex'))
        assert len(packet_files) == 48, match.group(1)
        filenames.extend(p.name for p in packet_files)
    assert filenames, match.group(1)
    assert all((ROOT / 'pages' / f).exists() for f in filenames), match.group(1)
assert not missing_metadata, missing_metadata

logs = {
    'A': (RESEARCH / 'algebra_context_searches.md').read_text(),
    'B': (RESEARCH / 'extension_context_searches.md').read_text(),
}
root_queries = {r['item'] for r in json.loads((RESEARCH / 'root_context_searches.json').read_text())}
for item in expected:
    if item[0] in logs:
        assert re.search(r'^#{1,5}\s+' + re.escape(item) + r'\b', logs[item[0]], re.M), ('missing search heading', item)
    else:
        assert item in root_queries, ('missing search record', item)

catalog = json.loads((RESEARCH / 'enumerations.json').read_text())
assert len(catalog['items']) == 67
enumlog = (RESEARCH / 'enumeration_context_searches.md').read_text()
for item in catalog['items']:
    assert item['id'] in enumlog, ('missing enumeration search', item['id'])

rows = list(csv.DictReader((ROOT / 'MPL_84_097-145_inventory.csv').open()))
assert len(rows) == 1001 and all(r['transcribed'] == 'yes' for r in rows)
sheet_kinds = {}
for row in rows:
    scan = int(row['scan'])
    assert scan not in sheet_kinds or sheet_kinds[scan] == row['sheet_kind']
    sheet_kinds[scan] = row['sheet_kind']
assert Counter(sheet_kinds.values()) == Counter(text=36,cancelled_draft=1,reused_typed=11)
page_text = '\n'.join(p.read_text() for p in sorted((ROOT / 'pages').glob('*.tex')))
assert page_text.count('\\unsure{') == 474
assert page_text.count('\\illegible{') == 1
assert not validate(ROOT, complete=True)
verify_frozen(ROOT)

report = {
    'time_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'scope': 'Coverage, source-file links, search-record presence, inventory, and frozen-file hashes; not semantic certification or a TeX compilation.',
    'short_research_items': len(ids),
    'item_groups': dict(Counter(i[0] for i in ids)),
    'enumeration_records': len(catalog['items']),
    'inventory_elements': len(rows),
    'inventory_status': 'all yes',
    'sheet_categories': dict(Counter(sheet_kinds.values())),
    'doubt_occurrences': {'unsure':474,'illegible':1},
    'source_files_exist': True,
    'per_item_search_records_present': True,
    'frozen_hashes_unchanged': 49,
    'notes_whitespace_word_count': len(notes.split()),
    'full_tex_compilation': 'blocked by missing formats/packages, not claimed',
}
(RESEARCH / 'final_validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(report, ensure_ascii=False, indent=2))
