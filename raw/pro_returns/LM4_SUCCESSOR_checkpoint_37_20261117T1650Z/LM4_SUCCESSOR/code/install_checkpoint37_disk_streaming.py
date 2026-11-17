"""Install the fully reviewed lower-memory sources, retaining all predecessors."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
def bind(rel):
    raw=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

changes=[
 ('work_CE/checkpoint37_streaming_proposed.py','code/checkpoint37_streaming.py',None,
  '65b3d069c83438838577f41046127c400d07de2cc1db3768feee3471c49dab17'),
 ('work_CE/package_checkpoint37_streamed_proposed.py','code/package_checkpoint.py',
  '120ee05572f01704d6fb23557af5ed8afbdaa896ce84f859e14d7945e25cc931',
  'be9d7c8798fff700d902ee0e8f2b9ac8324da201962e2ee90bfa15ab668581da'),
 ('work_CE/estimate_checkpoint37_size_streamed_proposed.py','code/estimate_checkpoint37_size.py',
  '6d001c5d77a7f8d18a7b00fb8906a1edc1b618f1783e6cc9883560418dc2b145',
  '22fd8f033dc077890953030316982ea5fb2a976709ce66b394d6c34bc7b43ba8')]
peer_path='work_A/review_checkpoint37_disk_streaming.json'
peer=json.loads((ROOT/peer_path).read_text())
assert peer['result']=='PASS_COMPLETE_SOURCE_ONLY_REVIEW'
assert {r['sha256'] for r in peer['sources']}=={r[3] for r in changes}
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_37.zip').exists()
assert not (ROOT/'records/checkpoint37_size_estimate.json').exists()
for src,target,old,new in changes:
    assert bind(src)['sha256']==new
    if old is None:assert not (ROOT/target).exists()
    else:assert bind(target)['sha256']==old
dest=ROOT/'records/checkpoint37_before_disk_streaming_install'
dest.mkdir(exist_ok=False)
review_path='records/checkpoint37_operational_source_review.json'
for rel in [r[1] for r in changes if r[2] is not None]+[review_path]:
    saved=dest/rel;saved.parent.mkdir(parents=True,exist_ok=True)
    with saved.open('xb') as stream:stream.write((ROOT/rel).read_bytes())
for src,target,old,new in changes:
    (ROOT/target).write_bytes((ROOT/src).read_bytes())
    assert bind(target)['sha256']==new
review=json.loads((ROOT/review_path).read_text())
paths=[r['path'] for r in review['sources']]
assert 'code/checkpoint37_streaming.py' not in paths
paths.append('code/checkpoint37_streaming.py')
review['sources']=[bind(rel) for rel in paths]
peer_paths=[r['path'] for r in review['independent_reviews']]
peer_paths += ['work_A/review_checkpoint37_disk_streaming.md',peer_path]
review['independent_reviews']=[bind(rel) for rel in peer_paths]
review['updated_at']=datetime.now(timezone.utc).isoformat()
review['disk_streaming_change']={
 'root_complete_helper_read':'6038f8','root_complete_packager_read':'bb92fe',
 'root_complete_final_estimator_read_parts':['d14481','db0e60'],
 'earlier_truncated_estimator_output_not_counted':'a47941',
 'root_current_snapshot_scope_diff_read':'5d71ee',
 'root_complete_peer_review_read':'a66179',
 'previous_actual_failed_estimate':bind('records/checkpoint37_failed_size_estimate_observed.json'),
 'scope':'All20 current source bindings include the new shared staging/streaming worker. Separate snapshot, encoder and full decoder processes; identical512/256/64MiB codec policy and complete logical-byte retention. The final current snapshot includes every added duplicate image path. No runtime success is inferred from this source review.'}
review['scope']='Complete root source review of the current20 helpers/dependencies, with retained predecessor reviews and exact current addenda. The streaming helper, new packager and final estimator were read completely. All listed bytes and current independent reviews are bound; runtime outcomes are separate.'
(ROOT/review_path).write_text(json.dumps(review,indent=2)+'\n')
record={'recorded_at':review['updated_at'],'result':'PASS_REVIEWED_DISK_STREAMING_INSTALLED',
 'canonical_sources':[bind(r[1]) for r in changes],
 'peer_review':bind(peer_path),'root_source_review':bind(review_path),
 'preserved_directory':str(dest.relative_to(ROOT)),
 'new_size_estimate_started_by_installer':False,'archive_created':False}
with (ROOT/'records/checkpoint37_disk_streaming_install.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
