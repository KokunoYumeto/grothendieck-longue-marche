"""Preserve the actual complete streaming size run rejected only by the cap."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'records/checkpoint37_failed_size_cap'
DEST.mkdir(exist_ok=False)
report_path = ROOT / 'records/checkpoint37_size_estimate.json'
report = json.loads(report_path.read_text())
assert report['estimated_before_allowance'] == 545978789
assert report['estimated_total_with_allowance'] == 550978789
assert report['estimated_headroom_bytes'] == -14107877
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_37.zip').exists()
for name, row in report['prospective_bundles'].items():
    assert row['encoder_process_exit_code'] == row['decoder_process_exit_code'] == 0
    assert row['full_roundtrip']['input'] == row['full_roundtrip']['roundtrip']
    assert row['full_roundtrip']['decoder_eof'] is True
    assert row['full_roundtrip']['unused_bytes'] == 0

paths = list(report['source_bindings']) + [
    'records/checkpoint37_size_estimate.json',
    'records/checkpoint37_size_estimate_run.out',
    'records/checkpoint37_size_estimate_run.err',
    'records/checkpoint37_operational_source_review.json',
    'code/publish_checkpoint37_readiness.py',
    'code/observe_checkpoint37_pre_capture.py',
    'code/write_checkpoint37_computation_audit.py',
]
rows = []
for rel in paths:
    source = ROOT / rel
    raw = source.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if rel in report['source_bindings']:
        assert report['source_bindings'][rel] == {'bytes': len(raw), 'sha256': sha}
    target = DEST / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    assert target.read_bytes() == raw
    rows.append({'path': rel, 'retained_path': str(target.relative_to(ROOT)),
                 'bytes': len(raw), 'sha256': sha})

observation = {
    'recorded_at': datetime.now(timezone.utc).isoformat(),
    'session_id': 41501, 'initial_tool_chunk': '7e6a0c',
    'actual_exit_code': 1, 'actual_exit_tool_chunk': '96b054',
    'complete_stdout_stderr_read_tool_chunk': '503227',
    'scope': 'All three separate encoder and decoder workers actually exited0 and completed exact full length/SHA256/CRC32, EOF and no-tail checks. The outer estimator actually exited1 only at its final size-cap assertion. No ZIP was opened. Successful worker certificates are retained without presenting the failed outer producer as successful.',
    'estimated_total_with_allowance': report['estimated_total_with_allowance'],
    'delivery_cap_bytes': report['delivery_cap_bytes'],
    'files': rows,
}
observed = ROOT / 'records/checkpoint37_failed_size_cap_observed.json'
with observed.open('x') as stream:
    json.dump(observation, stream, indent=2)
    stream.write('\n')
# The retained report has been byte-checked before the canonical result slot is
# released. Its exact old contents remain present under the retained path.
assert (DEST / 'records/checkpoint37_size_estimate.json').read_bytes() == report_path.read_bytes()
report_path.unlink()
print(json.dumps({'result': 'COMPLETE_FAILED_CAP_RUN_RETAINED',
                  'files': len(rows), 'outer_exit_code': 1,
                  'verified_bundle_workers': 6, 'creates_zip': False}))
