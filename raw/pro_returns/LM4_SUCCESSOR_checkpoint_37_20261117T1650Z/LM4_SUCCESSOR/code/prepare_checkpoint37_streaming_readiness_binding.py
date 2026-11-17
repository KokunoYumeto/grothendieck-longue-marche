"""Retain old readiness sources and explicitly bind the new streaming helper."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'records/checkpoint37_before_streaming_readiness_binding'
DEST.mkdir(exist_ok=False)
paths=['code/publish_checkpoint37_readiness.py','code/observe_checkpoint37_pre_capture.py',
       'records/checkpoint37_operational_source_review.json']
for rel in paths:
    dst=DEST/rel;dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('xb') as stream:stream.write((ROOT/rel).read_bytes())
pub=ROOT/paths[0];old=pub.read_text()
needle="        'code/package_checkpoint.py', 'code/checkpoint_data_tar.py', 'code/checkpoint_image_tar.py',"
replacement="        'code/package_checkpoint.py', 'code/checkpoint37_streaming.py',\n        'code/checkpoint_data_tar.py', 'code/checkpoint_image_tar.py',"
assert old.count(needle)==1
new=old.replace(needle,replacement)
pub.write_text(new)
diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),
             fromfile='previous/code/publish_checkpoint37_readiness.py',tofile='current/code/publish_checkpoint37_readiness.py'))
diff_path=ROOT/'records/checkpoint37_streaming_readiness_source.diff'
with diff_path.open('x') as stream:stream.write(diff)
observer=ROOT/paths[1];obs=observer.read_text()
old_peer='work_A/review_checkpoint37_readiness_publisher.json'
new_peer='work_A/review_checkpoint37_readiness_streaming_addendum.json'
assert obs.count(old_peer)==1
observer.write_text(obs.replace(old_peer,new_peer))
def bind(rel):
    raw=(ROOT/rel).read_bytes()
    return {'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
record={'recorded_at':datetime.now(timezone.utc).isoformat(),
 'result':'EXPLICIT_STREAMING_HELPER_READINESS_BINDING_PREPARED',
 'publisher':bind(paths[0]),'observer':bind(paths[1]),
 'diff':bind(str(diff_path.relative_to(ROOT))),
 'prior_root_complete_publisher_source_read':'d86084',
 'root_authored_entire_one_line_change':True,
 'independent_publisher_addendum_pending':True,
 'scope':'Add the new streaming helper to the explicit runtime helper set, so preconditions recheck its current hash. Keep the existing publisher peer receipt unchanged; the observer will bind a separate current-source addendum. No readiness or ZIP is published here.'}
with (ROOT/'records/checkpoint37_streaming_readiness_source_change.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
