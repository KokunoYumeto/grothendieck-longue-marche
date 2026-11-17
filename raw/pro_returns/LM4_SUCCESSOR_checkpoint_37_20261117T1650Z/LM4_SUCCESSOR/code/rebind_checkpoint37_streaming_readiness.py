"""Bind the actual current publisher and streaming dependencies after full review."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
def bind(rel):
    raw=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

target='records/checkpoint37_operational_source_review.json'
old=(ROOT/target).read_bytes()
retained=ROOT/'records/checkpoint37_before_streaming_readiness_binding'/target
assert retained.read_bytes()==old
record=json.loads(old)
pub='code/publish_checkpoint37_readiness.py'
new_pub=bind(pub)
assert new_pub['sha256']=='84e7027395e26ff3dff14fc86a7c477bfab583f05fe728565e7f06412049fc09'
peer='work_A/review_checkpoint37_readiness_streaming_addendum.json'
review=json.loads((ROOT/peer).read_text())
assert review['result']=='PASS_COMPLETE_SOURCE_AND_EXACT_DIFF'
assert review['source']==new_pub
for row in record['sources']:
    if row['path']==pub:row.update(new_pub)
    else:assert row==bind(row['path'])
assert len(record['sources'])==20
assert any(r['path']=='code/checkpoint37_streaming.py' for r in record['sources'])
for rel in ['work_A/review_checkpoint37_readiness_streaming_addendum.md',peer,
            'work_DE/review_checkpoint37_streamed_tar_zip_metadata.md',
            'work_DE/review_checkpoint37_streamed_tar_zip_metadata.json']:
    assert not any(r['path']==rel for r in record['independent_reviews'])
    record['independent_reviews'].append(bind(rel))
record['updated_at']=datetime.now(timezone.utc).isoformat()
record['streaming_readiness_addendum']={
 'root_complete_prior_publisher_read':'d86084',
 'root_entire_authored_exact_change':bind('records/checkpoint37_streaming_readiness_source.diff'),
 'source_change_record':bind('records/checkpoint37_streaming_readiness_source_change.json'),
 'root_complete_current_peer_addendum_and_metadata_review_read':'9ba9e7',
 'current_publisher':new_pub,
 'scope':'The mandatory publisher helper set explicitly includes code/checkpoint37_streaming.py; its current hash will enter runtime bindings and be rechecked by the capture preconditions. Every source/peer binding below is current. The running final size estimator has not been declared complete.'}
(ROOT/target).write_text(json.dumps(record,indent=2)+'\n')
out={'recorded_at':record['updated_at'],'result':'PASS_CURRENT_STREAMING_READINESS_SOURCE_BINDINGS',
     'root_source_review':bind(target),'sources':len(record['sources']),
     'independent_review_files':len(record['independent_reviews']),
     'publisher':new_pub,'publisher_peer':bind(peer),
     'no_runtime_readiness_published':True}
with (ROOT/'records/checkpoint37_streaming_readiness_binding.json').open('x') as stream:
    json.dump(out,stream,indent=2);stream.write('\n')
print(json.dumps(out,indent=2))
