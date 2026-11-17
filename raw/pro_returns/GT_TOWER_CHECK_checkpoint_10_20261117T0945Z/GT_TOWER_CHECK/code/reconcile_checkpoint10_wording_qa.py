#!/usr/bin/env python3
"""Carry actual inspections only across byte-identical page images."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'notes/pdf_qa'
OLD=ROOT/'notes/tenth_wording_repair_before/pdf_qa'
manifest=json.loads((OUT/'manifest.json').read_text())
assignment=json.loads((OUT/'checkpoint10_assignments.json').read_text())
old_assignment=json.loads((OLD/'checkpoint10_assignments.json').read_text())
assert assignment['assignments']==old_assignment['assignments'],'Page selection changed: review before carrying observations.'
changed=[];unchanged=[]
for who in ('root','tower','centralizer','ghost'):
    data=json.loads((OLD/f'checkpoint10_{who}.json').read_text())
    data['previous_pdf_sha256']=data['pdf_sha256'];data['pdf_sha256']=manifest['pdf_sha256']
    for row in data['pages']:
        page=row['page'];name=f'page_{page:03d}.png'
        sha=hashlib.sha256((OUT/name).read_bytes()).hexdigest()
        assert row['png_sha256']==hashlib.sha256((OLD/name).read_bytes()).hexdigest()
        if sha==row['png_sha256']:
            row['inspection_carry']='Previously opened full-page PNG; byte-identical after wording repair, checked by SHA256.'
            unchanged.append(page)
        else:
            row['previous_png_sha256']=row['png_sha256'];row['png_sha256']=sha
            row['previous_observations']=row['observations']
            row['observations']='Pending actual reinspection after wording repair.'
            row['visually_inspected']=False
            changed.append({'page':page,'inspector':who})
    (OUT/f'checkpoint10_{who}.json').write_text(json.dumps(data,indent=2)+'\n')
record={'pdf_sha256':manifest['pdf_sha256'],'unchanged_pages':sorted(unchanged),'changed_pages':changed,
        'scope':'Only exact byte-identical PNGs retain prior inspections; changed pages remain pending.'}
(OUT/'checkpoint10_wording_repair_comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print('Exact unchanged pages:',len(unchanged));print('Changed pages requiring inspection:',changed)
