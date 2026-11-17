"""Preserve the complete actual failed128 size estimate and its observed exit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root=Path(__file__).resolve().parents[1]
dest=root/'records/checkpoint36_first_size_estimate'
dest.mkdir(exist_ok=False)
expected={
 'checkpoint36_size_estimate.json':'005b64fab4b5cf9dfd302ca5c837b053b3b06045765012b187fb1d2ac2436d28',
 'checkpoint36_size_estimate_run.out':'d7cb7b33115f3b480381c34118926941c5e1a8eadc84d23a87aed119a67749c4',
 'checkpoint36_size_estimate_run.err':'2eed86b0fb215d2fefdd9e4c07d77201aaebdfac70b4e3b5297332c7b1f479f5',
}
for name,digest in expected.items():
    data=(root/'records'/name).read_bytes()
    assert hashlib.sha256(data).hexdigest()==digest
    with (dest/name).open('xb') as stream:stream.write(data)
def bound(rel):
    p=root/rel
    return dict(path=rel,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
record=dict(recorded_at=datetime.now(timezone.utc).isoformat(),
 actual_tool_result_observed=True,session_id=26477,initial_tool_chunk='15f6e4',
 actual_completion_tool_chunk='00e3f0',actual_exit_code=1,
 source=bound('code/estimate_checkpoint36_size.py'),
 report=bound('records/checkpoint36_first_size_estimate/checkpoint36_size_estimate.json'),
 stdout=bound('records/checkpoint36_first_size_estimate/checkpoint36_size_estimate_run.out'),
 stderr=bound('records/checkpoint36_first_size_estimate/checkpoint36_size_estimate_run.err'),
 complete_stdout_stderr_and_report_read=True,
 reading_chunks=['789841','12e83c'],
 scope='Root actually observed completed session26477 exit1 in00e3f0. All three component compressions completed and the full report was written; the sole failure is the final unchanged delivery-cap assertion. Complete genuine stdout/stderr/report, including all22 predicted historical rows, were read. The active originals are still unchanged; these exact copies must survive the later same-input accounting step. No archive was created.')
assert record['source']['sha256']=='293e093f5d0cdc7ed8d841182b2c33e09f0c38bde414724891ea7a3d50bc0e47'
with (root/'records/checkpoint36_first_size_observed.json').open('x') as stream:
    json.dump(record,stream,indent=2);stream.write('\n')
print(json.dumps(record,indent=2))
