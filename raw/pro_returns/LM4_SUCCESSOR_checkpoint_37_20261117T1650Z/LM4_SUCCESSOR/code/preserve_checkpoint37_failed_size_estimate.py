"""Retain the observed137 size-estimate attempt before any safer revision."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'records/checkpoint37_failed_size_estimate_137'
DEST.mkdir(exist_ok=False)
names=['code/estimate_checkpoint37_size.py','code/package_checkpoint.py',
       'code/checkpoint_image37_tar.py','code/checkpoint_document37_tar.py',
       'code/checkpoint_data_tar.py','code/checkpoint_standard_tar.py',
       'code/checkpoint_archive_io.py',
       'records/checkpoint37_size_estimate_run.out','records/checkpoint37_size_estimate_run.err',
       'records/checkpoint37_operational_source_review.json',
       'records/checkpoint37_memory_policy_install.json']
rows=[]
for rel in names:
    raw=(ROOT/rel).read_bytes();dst=DEST/rel
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('xb') as stream:stream.write(raw)
    rows.append({'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
                 'retained_as':str(dst.relative_to(ROOT))})
shell_output='/bin/bash: line 1:     3 Killed                  python code/estimate_checkpoint37_size.py > records/checkpoint37_size_estimate_run.out 2> records/checkpoint37_size_estimate_run.err\n'
with (DEST/'actual_tool_exit_output.txt').open('x') as stream:stream.write(shell_output)
record={'recorded_at':datetime.now(timezone.utc).isoformat(),
    'result':'PRESERVED_ACTUAL_SIZE_ESTIMATE_EXIT137',
    'session_id':12069,'initial_tool_chunk':'4324a9','actual_exit_code':137,
    'actual_exit_observation_tool_chunk':'c11211','actual_full_stdout_stderr_read_chunk':'df5f3f',
    'last_reported_image_input_bytes':504365056,'prospective_image_tar_bytes':624814080,
    'failure_scope':'The shell reported Killed and actual exit137 before any bundle-completion certificate or final size report. The simultaneous encoder, decoder and retained snapshot buffers create a memory-risk mechanism; no inaccessible cgroup/OOM cause is asserted as observed.',
    'size_report_exists':(ROOT/'records/checkpoint37_size_estimate.json').exists(),
    'archive37_exists':(ROOT.parent/'LM4_SUCCESSOR_checkpoint_37.zip').exists(),
    'failed_run_stderr_bytes':(ROOT/'records/checkpoint37_size_estimate_run.err').stat().st_size,
    'actual_shell_output_preserved_separately':str((DEST/'actual_tool_exit_output.txt').relative_to(ROOT)),
    'memory_observation':{'chunk':'df5f3f','mem_total_kib':10206472,
                          'mem_available_after_failure_kib':9524560,
                          'cgroup_limit_accessible':False},
    'retained_files':rows,
    'safer_next_direction':'Freeze exact logical bytes and deterministic TARs in temporary disk staging; release snapshot processes before a fresh streaming encoder; independent full decoding only after encoder exit. Keep dictionaries512/256/64MiB and all-byte identity checks.'}
assert record['size_report_exists'] is False and record['archive37_exists'] is False
with (ROOT/'records/checkpoint37_failed_size_estimate_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps({'result':record['result'],'files':len(rows),'actual_exit_code':137,'zip37_exists':False}))
