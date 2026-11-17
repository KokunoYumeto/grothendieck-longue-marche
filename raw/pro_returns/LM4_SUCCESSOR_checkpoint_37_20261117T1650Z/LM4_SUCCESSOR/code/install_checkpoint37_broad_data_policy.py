"""Install only the completely reviewed lossless37 data-selection revision."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--peer', required=True)
args = parser.parse_args()
def bind(rel):
    raw = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

manifest_path = 'work_CE/checkpoint37_broad_data_proposal_manifest.json'
manifest = json.loads((ROOT / manifest_path).read_text())
assert manifest['status'] == 'SOURCE_ONLY_PROPOSAL_NOT_INSTALLED_OR_EXECUTED'
expected = [
 'a0c2a19f0c3c59dc1f487bb91e85a3c5a67ac639cd663f677200e869ee61ad40',
 '7db100dc8febe319482220710f5022c488caad36b663f21239eecfcfc4ae481d',
 '84f9b9dbf26e1779761f51d8ea1f32b3e59142873bb941a0f3c497721aa2426a',
]
assert [row['sha256'] for row in manifest['proposed_sources']] == expected
for row in manifest['proposed_sources'] + manifest['predecessors'] + manifest['diffs']:
    assert row == bind(row['path'])
assert manifest['final_stdout_precision'] == bind(manifest['final_stdout_precision']['path'])
peer_raw = (ROOT / args.peer).read_bytes()
peer = json.loads(peer_raw)
assert str(peer.get('result', peer.get('status', ''))).startswith('PASS')
assert all(sha.encode() in peer_raw for sha in expected), 'Peer must bind all final proposed sources'
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_37.zip').exists()
assert not (ROOT / 'records/checkpoint37_size_estimate.json').exists()
assert not (ROOT / 'records/checkpoint37_capture_ready.json').exists()

dest = ROOT / 'records/checkpoint37_before_broad_data_install'
dest.mkdir(exist_ok=False)
for old in manifest['predecessors'] + [bind('records/checkpoint37_operational_source_review.json')]:
    target = dest / old['path']
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / old['path'], target)
    assert target.read_bytes() == (ROOT / old['path']).read_bytes()

installed = []
for new, old in zip(manifest['proposed_sources'], manifest['predecessors']):
    (ROOT / old['path']).write_bytes((ROOT / new['path']).read_bytes())
    row = bind(old['path'])
    assert row['sha256'] == new['sha256'] and row['bytes'] == new['bytes']
    installed.append(row)
record = {
 'recorded_at': datetime.now(timezone.utc).isoformat(),
 'result': 'INSTALLED_REVIEWED_LOSSLESS_BROAD_DATA_POLICY',
 'sources': installed, 'proposal_manifest': bind(manifest_path), 'peer': bind(args.peer),
 'root_full_current_source_reads': ['875ca8', 'd3670c', '82f00d'],
 'root_exact_diff_and_final_manifest_reads': ['702e0e', '6fb177'],
 'preserved_predecessors': str(dest.relative_to(ROOT)),
 'scope': 'Explicit37+ selector with legacy default, unchanged standard codecs, direct current root/code/sections and current manifests, exact old payload migration witnesses, and fresh exact identity reuse of previously successful image/document workers with their outer cap failure explicit. No size success or archive is claimed.'
}
with (ROOT / 'records/checkpoint37_broad_data_install.json').open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
print(json.dumps(record, indent=2))
