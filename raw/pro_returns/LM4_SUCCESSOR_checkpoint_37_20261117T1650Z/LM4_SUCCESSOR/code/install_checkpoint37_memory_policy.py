"""Install the completely reviewed memory-release policy, without encoding."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OLD = '09388957e560ea6c3800d2b2f61febab64c12f89a307ceccfc12add31889cc64'
NEW = '120ee05572f01704d6fb23557af5ed8afbdaa896ce84f859e14d7945e25cc931'

def binding(rel):
    data = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}

target = ROOT / 'code/package_checkpoint.py'
proposal = ROOT / 'work_CE/package_checkpoint37_memory_proposed.py'
retained = ROOT / 'records/checkpoint37_before_memory_cleanup/package_checkpoint.py'
assert hashlib.sha256(target.read_bytes()).hexdigest() == OLD
assert retained.read_bytes() == target.read_bytes()
assert hashlib.sha256(proposal.read_bytes()).hexdigest() == NEW
review = json.loads((ROOT/'work_A/review_checkpoint37_memory_roundtrip.json').read_text())
assert review['result'] == 'PASS_COMPLETE_SOURCE_AND_DIFF_REVIEW'
assert review['complete_sources_read'] and review['complete_diffs_read']
for item in review['sources'] + review['diffs']:
    assert binding(item['path']) == item
receipt_path = ROOT/'records/checkpoint37_memory_policy_install.json'
assert not receipt_path.exists()
target.write_bytes(proposal.read_bytes())
assert hashlib.sha256(target.read_bytes()).hexdigest() == NEW
record = {
    'recorded_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'checkpoint': 37,
    'installed': binding('code/package_checkpoint.py'),
    'proposal': binding('work_CE/package_checkpoint37_memory_proposed.py'),
    'previous_version_retained': binding('records/checkpoint37_before_memory_cleanup/package_checkpoint.py'),
    'independent_review': binding('work_A/review_checkpoint37_memory_roundtrip.json'),
    'root_complete_source_read_chunk_id': '3c508d',
    'root_complete_diff_and_review_read_chunk_id': '3a14c3',
    'result': 'PASS_COMPLETE_SOURCE_REVIEW_AND_INSTALL',
    'encoders_run': 0,
    'archives_opened_or_created': 0,
}
with receipt_path.open('x', encoding='utf-8') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, indent=2))
