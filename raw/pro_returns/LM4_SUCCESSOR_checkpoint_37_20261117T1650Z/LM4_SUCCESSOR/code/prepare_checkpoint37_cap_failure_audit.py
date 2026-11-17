"""Retain and clarify the final audit/observer after the actual cap failure."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
retained = ROOT / 'records/checkpoint37_failed_size_cap'
paths = ['code/write_checkpoint37_computation_audit.py',
         'code/observe_checkpoint37_pre_capture.py']
for rel in paths:
    assert (ROOT / rel).read_bytes() == (retained / rel).read_bytes()

audit = (ROOT / paths[0]).read_text()
anchor = 'The actual completed replacement estimates\n'
addition = '''The second exact streaming run, session41501, actually exited1
(96b054) only at the final delivery-cap assertion. All three encoders and
all three independent decoders had already actually exited0 and fully
verified their streams. Its estimate was545978789bytes before the
unchanged5000000-byte allowance, and550978789bytes with it, exceeding
the536870912-byte cap. Its complete stdout and traceback were read
(503227), and the entire report, source dependencies and logs were
retained by the successful preservation helper (fcc3ed). The failed
outer producer is never presented as successful.

The subsequent reviewed revision preserves every logical byte and
widens solid data storage to supporting text while retaining current
root deliverables, code and formal sections as direct entries. It
keeps all three dictionary sizes unchanged. Freshly staged image and
document TARs may reuse those actual successful worker measurements
only after exact full SHA256, CRC32 and length identity and unchanged
codec/staging bindings have been checked. The retained earlier outer
exit1 remains explicit. The revised data TAR is actually encoded and
independently decoded in separate processes. No unmeasured compression
saving, discarded history, test ZIP, or changed allowance is used.

The actual completed final estimator reports
'''
assert audit.count(anchor) == 1
audit = audit.replace(anchor, addition)
audit = audit.replace('All three actual prospective\nstreams have full length/SHA256/CRC32 identity, real method14 headers,',
                      'All three actual prospective\nstreams are bound to full length/SHA256/CRC32 identity, real method14 headers,')
(ROOT / paths[0]).write_text(audit)

observer = (ROOT / paths[1]).read_text()
anchor = "ag ents=[]".replace(' ', '')
addition = '''failed.append(operation('second_size_estimate_delivery_cap','96b054',[
 'records/checkpoint37_failed_size_cap_observed.json',
 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate.json',
 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate_run.out',
 'records/checkpoint37_failed_size_cap/records/checkpoint37_size_estimate_run.err',
 'records/checkpoint37_failed_size_cap/code/estimate_checkpoint37_size.py'],
 41501,'7e6a0c',exit_code=1,
 scope='All three encoders and separate decoders actually exited0 and fully verified their streams. The outer process actually exited1 solely at its final size-cap assertion:550978789bytes with the unchanged5MB allowance exceeded536870912. Complete source, report and logs retained. Exact later identity reuse does not convert this failed outer run into a successful run.'))
agents=[]'''
assert observer.count(anchor) == 1
observer = observer.replace(anchor, addition)
(ROOT / paths[1]).write_text(observer)

rows = []
for rel in paths:
    raw = (ROOT / rel).read_bytes()
    rows.append({'path': rel, 'bytes': len(raw),
                 'sha256': hashlib.sha256(raw).hexdigest()})
record = {'recorded_at': datetime.now(timezone.utc).isoformat(),
          'result': 'PREPARED_ONLY_NOT_EXECUTED', 'sources': rows,
          'predecessors': 'records/checkpoint37_failed_size_cap/code/',
          'earlier_patch_attempts': [
              'apply_patch failed before mutation: unmatched replacement stages exact frozen logical bytes',
              'apply_patch failed before mutation: unmatched copies and the pending-reason record are retained with a separate'],
          'scope': 'Adds the real sixth failed producer and correctly distinguishes exact prior successful worker certificates from its failed outer estimate. Neither final writer is run here.'}
with (ROOT / 'records/checkpoint37_cap_failure_audit_preparation.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, indent=2))
