"""Bind the three reviewed storage revisions while preserving every predecessor."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
def bind(rel):
    raw = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

target = 'records/checkpoint37_operational_source_review.json'
previous = (ROOT / target).read_bytes()
assert previous == (ROOT / 'records/checkpoint37_before_broad_data_install' / target).read_bytes()
record = json.loads(previous)
installation = json.loads((ROOT / 'records/checkpoint37_broad_data_install.json').read_text())
assert installation['result'] == 'INSTALLED_REVIEWED_LOSSLESS_BROAD_DATA_POLICY'
changed = {row['path']: row for row in installation['sources']}
peer_path = 'work_A/review_checkpoint37_broad_data_reuse.json'
peer = json.loads((ROOT / peer_path).read_text())
assert peer['result'] == 'PASS_ENTIRE_FINAL_PROPOSALS_AND_COMPLETE_DIFFS_SOURCE_ONLY'
assert len(changed) == 3
assert {row['sha256'] for row in changed.values()} == {row['sha256'] for row in peer['sources']}
for row in record['sources']:
    if row['path'] in changed:
        assert bind(row['path']) == changed[row['path']]
        row.update(changed[row['path']])
    else:
        assert row == bind(row['path'])
assert len(record['sources']) == 20
for row in record['independent_reviews']:
    assert row == bind(row['path'])
for rel in ['work_A/review_checkpoint37_broad_data_reuse.md', peer_path]:
    assert not any(row['path'] == rel for row in record['independent_reviews'])
    record['independent_reviews'].append(bind(rel))
record['updated_at'] = datetime.now(timezone.utc).isoformat()
record['install_receipts'].append(bind('records/checkpoint37_broad_data_install.json'))
record['broad_data_revision'] = {
 'root_complete_current_source_reads': ['875ca8', 'd3670c', '82f00d'],
 'root_complete_diff_and_final_delta_reads': ['702e0e', '6fb177'],
 'root_complete_peer_md_json_read': '988e69',
 'prior_actual_cap_failure': bind('records/checkpoint37_failed_size_cap_observed.json'),
 'proposal_manifest': bind('work_CE/checkpoint37_broad_data_proposal_manifest.json'),
 'actual_install_exit0_tool_chunk': '4b0e01',
 'running_final_estimator': {'session_id': 54149, 'launch_chunk': 'e61160',
                            'exit_not_yet_observed': True},
 'scope': 'Current20 exact source bindings, with all predecessor independent reviews retained and the complete final three-source addendum added. No codec, delivery cap, safety allowance, logical-byte retention or actual-success requirement has been weakened. Explicit37+ solid-data selection and exact freshly identical prior successful image/document worker reuse retain the actual prior outer cap failure.'
}
(ROOT / target).write_text(json.dumps(record, indent=2) + '\n')
result = {'recorded_at': record['updated_at'],
          'result': 'PASS_CURRENT_BROAD_DATA_SOURCE_BINDINGS',
          'sources': len(record['sources']),
          'independent_review_files': len(record['independent_reviews']),
          'source_review': bind(target), 'no_runtime_readiness_published': True}
with (ROOT / 'records/checkpoint37_broad_data_review_binding.json').open('x') as stream:
    json.dump(result, stream, indent=2)
    stream.write('\n')
print(json.dumps(result, indent=2))
