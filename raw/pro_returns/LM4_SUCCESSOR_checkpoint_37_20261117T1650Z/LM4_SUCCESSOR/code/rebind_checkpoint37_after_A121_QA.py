"""Refresh only the two reviewed A.121 QA bindings; preserve the first record."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
path=root/'records/checkpoint37_operational_source_review.json'
old=root/'records/checkpoint37_before_A121_correction/records/checkpoint37_operational_source_review.json'
assert path.read_bytes()==old.read_bytes()
record=json.loads(path.read_text())
def bind(rel):
    data=(root/rel).read_bytes()
    return {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
peer='work_CE/review_checkpoint37_A121_QA_helpers.json'
review=json.loads((root/peer).read_text())
assert review['result'].startswith('PASS') and review['entire_sources_read'] and review['entire_diffs_read']
changed={row['path']:row for row in review['sources']}
for rel,row in changed.items():assert bind(rel)==row
record['sources']=[changed.get(row['path'],row) for row in record['sources']]
for row in record['sources']:assert bind(row['path'])==row
record['independent_reviews'] += [bind('work_CE/review_checkpoint37_A121_QA_helpers.txt'),bind(peer)]
record['updated_at']=datetime.now(timezone.utc).isoformat()
record['A121_QA_change']={'manifest':bind('records/checkpoint37_A121_QA_source_changes.json'),
                         'root_prior_complete_source_read_chunk':'635403',
                         'root_authored_entire_exact_changes':True,
                         'root_complete_peer_review_read_chunk':'5e8257',
                         'scope':'Require the complete actual corrected A.121 interval individually; all existing new-proof, hash, reviewer and contact checks retained.'}
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'result':'PASS_COMPLETE_SOURCE_REVIEW','changed_sources':list(changed),'total_sources':len(record['sources'])}))
