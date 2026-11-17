"""Bind the two completely read final layout differences to preserved reviews."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
sha=lambda rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()
read=lambda rel:json.loads((root/rel).read_text())
layout=read('records/checkpoint35_layout_correction.json')
independent=read('work_CE/review_A112_A114_final_layout35.json')
assert independent['result']=='PASS' and independent['entire_diffs_and_correction_record_read']
extra={p:sha(p) for p in ['work_CE/review_A112_A114_final_layout35.txt','work_CE/review_A112_A114_final_layout35.json']}
for change in layout['changes']:
    assert sha(change['source'])==sha(change['target'])==change['after_sha256']
    assert sha(change['diff'])==change['diff_sha256']
    assert any(r['path']==change['source'] and r['sha256']==change['after_sha256'] for r in independent['sources'])
for rel in ['records/checkpoint35_independent_review_manifest.json','records/checkpoint35_root_formal_reviews.json','records/checkpoint35_formal_source_copies.json']:
    old='records/pdf_qa/checkpoint35_first_layout/'+rel
    assert (root/old).read_bytes()==(root/rel).read_bytes()
    data=read(rel)
    for change in layout['changes']:
        if 'source_hashes' in data:
            assert data['source_hashes'][change['source']]==change['before_sha256']
            data['source_hashes'][change['source']]=change['after_sha256']
        if 'copies' in data:
            rows=[r for r in data['copies'] if r['statement']==change['statement']]
            assert len(rows)==1 and rows[0]['sha256']==change['before_sha256']
            rows[0]['sha256']=change['after_sha256']
    if 'reviews' in data:data['reviews'].update(extra)
    if 'independent_reviews' in data:data['independent_reviews'].update(extra)
    data['layout_binding_update']=dict(recorded_at=datetime.now(timezone.utc).isoformat(),prior_record=old,
      prior_record_sha256=sha(old),changes=layout['changes'],independent_reviews=extra,
      scope='Root read both complete exact differences and the complete independent review/JSON. Only the A112 definition-line arrangement/punctuation and the conjunction between two identical A114 equation references change. Prior reviewed records remain byte-preserved.')
    (root/rel).write_text(json.dumps(data,indent=2)+'\n')
print('Bound both final layout corrections in all three preserved formal-review manifests.')
