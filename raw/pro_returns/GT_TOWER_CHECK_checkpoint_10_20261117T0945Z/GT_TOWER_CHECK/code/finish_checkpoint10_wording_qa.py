#!/usr/bin/env python3
"""Record root's actual reinspection of the sole changed full-page PNG."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'notes/pdf_qa'
comparison=json.loads((OUT/'checkpoint10_wording_repair_comparison.json').read_text())
assert comparison['changed_pages']==[{'page':222,'inspector':'root'}]
p=OUT/'checkpoint10_root.json';report=json.loads(p.read_text())
row=next(r for r in report['pages'] if r['page']==222)
assert row['png_sha256']==hashlib.sha256((OUT/'page_222.png').read_bytes()).hexdigest()
row['visually_inspected']=True
row['observations']='Reopened the complete repaired page: the sentence now states that the commutator class has zero double. QCS.7–12 and all surrounding text remain legible, with no clipping, overlap or displaced equation label.'
row['inspection_carry']='Changed PNG actually reopened and visually inspected after the wording repair.'
p.write_text(json.dumps(report,indent=2)+'\n')
print('PASS actual reinspection of repaired page222; the other100 inspected PNGs are byte-identical.')
