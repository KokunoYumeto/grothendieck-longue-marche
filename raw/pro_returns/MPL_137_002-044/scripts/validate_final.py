#!/usr/bin/env python3
"""Check final artifact coverage and freeze integrity; never edit TeX."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
expected_scans = [n for n in range(2,45) if n != 6]
frozen = json.loads((ROOT / 'records/frozen_hashes.json').read_text())
assert len(frozen['hashes']) == 43
checks = []
for name, expected in frozen['hashes'].items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    assert actual == expected, (name, expected, actual)
    checks.append({'file': name, 'sha256': actual, 'unchanged': True})

log = (ROOT / 'progress.log').read_text()
done = [int(n) for n in re.findall(r'^137 scan (\d{3}) done ', log, re.M)]
audited = [int(n) for n in re.findall(r'^scan (\d{3}) audited ', log, re.M)]
assert done == expected_scans, ('done', done)
assert audited == expected_scans, ('audited', audited)
freeze_time = re.search(r'^transcription frozen (.+)$', log, re.M).group(1)
open_time = re.search(r'^context opened (.+)$', log, re.M).group(1)
assert open_time > freeze_time

rows = list(csv.DictReader((ROOT / 'MPL_137_002-044_inventory.csv').open()))
assert len(rows) == 833 and all(r['transcribed'] == 'yes' for r in rows)
notes = runpy.run_path(str(ROOT / 'scripts/build_notes.py'))['N']
ids = [n['id'] for n in notes]
assert ids == [f'R{n:03d}' for n in range(1,108)]
queries = json.loads((ROOT / 'records/context_searches.json').read_text())
assert [q['id'] for q in queries] == ids
assert all(q['hit_count'] == len(q['locations']) for q in queries)
locators = []
for n in notes:
    hits = []
    for scan in n['scans']:
        path = ROOT / 'pages' / f'MPL_137_002-044_137_scan{scan:03d}.tex'
        for line_no,line in enumerate(path.read_text().splitlines(),1):
            if n['anchor'] in line:
                hits.append({'scan':scan,'line':line_no})
                break
    assert hits, ('missing anchor', n['id'])
    assert n['body'] and n['kind'] and n['query']
    if 'own idea' in n['kind']:
        assert 'confidence' in (n['kind']+' '+n['body']).lower(),n['id']
    locators.append({'id':n['id'],'anchors':hits})

notes_text = (ROOT / 'MPL_137_002-044_notes.md').read_text()
for heading in ['Standing question 1','Standing question 2','References — external primary literature']:
    assert heading in notes_text
for p in ROOT.rglob('*'):
    if p.is_file():
        assert p.suffix.lower() not in {'.jpg','.jpeg','.png','.pdf','.zip'},p
report = {
    'utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    'result': 'PASS', 'page_count':42, 'inventory_rows':len(rows),
    'numbered_research_notes':len(notes), 'research_note_words':len(notes_text.split()),
    'per_note_context_searches':len(queries),
    'all_43_frozen_hashes_unchanged':True,
    'freeze_utc':freeze_time, 'context_opened_utc':open_time,
    'hash_checks':checks,'note_anchors':locators,
    'limitations':['Lexical/package verification is not TeX compilation.',
                   'This check does not resolve residual reading uncertainty.',
                   'Research-note sentence length and source-status fidelity received editorial review.']
}
(ROOT/'records/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in {'hash_checks','note_anchors'}},ensure_ascii=False))
