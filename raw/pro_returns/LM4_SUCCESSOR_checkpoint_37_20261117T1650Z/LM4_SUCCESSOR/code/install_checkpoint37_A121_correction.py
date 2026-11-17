"""Install the completely reviewed A.121 algebraic repair, retaining history."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

root=Path(__file__).resolve().parents[1]
old='cfee9d27b7ec7c597e0bd03409dd8d326d546f4aa754163cbbed2f160e84673d'
new='a5588315f65bb6ae2ec331dcecac7b1fb7f12c3ee4cecf2e57b2859a2fbb5327'
source='work_DE/A121_corrected_cyclic_cancellation_proposed37.tex'
targets=['work_A/A121_elliptic_pentagon_cubic_proposed.tex','sections/a_elliptic_pentagon_cubic.tex']
reviews=['work_A/review_A121_complete_corrected_cancellation37.md',
         'work_A/review_A121_complete_corrected_cancellation37.json',
         'work_CE/review_A121_corrected_cancellation37.txt',
         'work_CE/review_A121_corrected_cancellation37.json']
def bind(rel):
    data=(root/rel).read_bytes()
    return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
assert bind(source)['sha256']==new
for rel in targets:
    assert bind(rel)['sha256']==old
    saved=root/'records/checkpoint37_before_A121_correction'/rel
    assert saved.read_bytes()==(root/rel).read_bytes()
for rel in reviews:
    if rel.endswith('.json'):
        item=json.loads((root/rel).read_text())
        assert item['result'].startswith('PASS') and item['source']['sha256']==new
for rel in targets:(root/rel).write_bytes((root/source).read_bytes())
stamp=datetime.now(timezone.utc).isoformat()
record={'recorded_at':stamp,'statement':'A.121','result':'PASS_COMPLETE_REPAIRED_PROOF_INSTALLED',
        'source':bind(source),'targets':[bind(rel) for rel in targets],
        'prior_sha256':old,'root_complete_source_and_diff_read_chunk':'4be6d2',
        'root_complete_peer_reviews_read_chunk':'5e8257',
        'independent_reviews':[bind(rel) for rel in reviews],
        'primary':'Enriquez, arXiv1003.1012v3, Proposition2.20(2), author-version pp16–17; root fresh references turn1272view0/turn1272view1.',
        'correction':'The last F argument and Ad(C)(tau squared) use n_minus; the final relation is Y2 inverse n_plus Y2=n_minus. Both argument conjugations and complete cubic cancellation are proved from the original presentation.',
        'status_change':False,'boundary_or_CM_conclusion':False}
record_path='records/checkpoint37_A121_correction_install.json'
with (root/record_path).open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
formal_path=root/'records/checkpoint37_root_formal_reviews.json'
formal=json.loads(formal_path.read_text())
formal['corrected_existing_sources']=[dict(statement='A.121',source=targets[0],target=targets[1],sha256=new)]
formal['existing_correction_record']=bind(record_path)
formal['independent_reviews'].update({rel:bind(rel)['sha256'] for rel in reviews})
formal_path.write_text(json.dumps(formal,indent=2)+'\n')
independent_path=root/'records/checkpoint37_independent_review_manifest.json'
independent=json.loads(independent_path.read_text())
independent['corrected_existing_source_hashes']={rel:new for rel in targets}
independent['reviews'].update({rel:bind(rel)['sha256'] for rel in reviews})
independent_path.write_text(json.dumps(independent,indent=2)+'\n')
report=root/'LM4_SUCCESSOR_report.md'
with report.open('a') as stream:
    stream.write('\n## Checkpoint37 correction to the complete A.121 cubic proof\n\n'
      'A fresh whole-group audit found three linked incorrect conjugation rows in the prior A.121 proof and in the opened author version of Enriquez, Elliptic associators, arXiv1003.1012v3, Proposition2.20(2), pp16–17. The two meridians n_plus=tau sigma² tau^-1 and n_minus=tau^-1 sigma² tau must remain distinct: Ad(sigma tau)(tau²)=n_minus, the final F word uses n_minus, and Y2^-1 n_plus Y2=n_minus. The revised A.121 prints a complete presentation-only derivation of the shifted adjacent mixed relation and both simultaneous argument conjugations. The full ordered cancellation proves the original pentagon-only cubic with no new hypothesis. Every prior source and review is retained as history; their validation of those three rows is explicitly superseded by complete fresh root/A/CE reviews. The result is a proof repair, not a refutation of the cubic or a boundary/CM conclusion. All corrected A.121 pages are mandatory in the new individual-page review. The inspected primary scope is the author version, not an unseen publisher edition.\n')
print(json.dumps({'result':record['result'],'sha256':new,'statement_status':'Proved','new_statement_count':0}))
