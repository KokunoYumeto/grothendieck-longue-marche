#!/usr/bin/env python3
"""Assign every rendered full page once; this does not certify inspection."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
directory=ROOT/'notes/pdf_qa'
manifest=json.loads((directory/'manifest.json').read_text())
sha=hashlib.sha256((ROOT/'GT_TOWER_CHECK_paper.pdf').read_bytes()).hexdigest()
assert sha==manifest['pdf_sha256']
people=('root','tower','centralizer','ghost')
assignments={who:[] for who in people}
for i,row in enumerate(manifest['pages']):assignments[people[i%4]].append(row['page'])
record={'pdf_sha256':sha,'assignments':assignments,
        'instructions':'Open every listed full-page PNG and inspect it visually. Record actual observations and each PNG SHA256. Rendering alone is not inspection.'}
(directory/'checkpoint08_assignments.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
