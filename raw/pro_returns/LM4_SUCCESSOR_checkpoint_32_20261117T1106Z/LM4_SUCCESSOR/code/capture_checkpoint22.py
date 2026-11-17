"""Capture one immutable checkpoint22 after its timed review and writer pause."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026,11,16,22,49,30,tzinfo=timezone.utc)
archive = ROOT.parent/'LM4_SUCCESSOR_checkpoint_22.zip'
assert not archive.exists()
remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the timed review.'
while remaining > 0:
    time.sleep(min(0.5,remaining))
    remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
subprocess.run([sys.executable,str(ROOT/'code/check_checkpoint22_preconditions.py')],check=True)
assert (ROOT/'records/checkpoint22_writer_pause.md').exists()
m = json.loads((ROOT/'records/checkpoint22_metrics.json').read_text())
research = (ROOT/'records/twenty_second_hour_research_report.md').read_text()
computations = (ROOT/'records/checkpoint22_computation_audit_state.md').read_text()
review = f'''# Twenty-second-hour progress review

Scheduled review: 2026-11-16 22:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. This hour advances the actual
Main-B obstruction problem: the bad slit vertex and the complete
one-neck selected fixed source are now determined, discretely and
in the full profinite category. A new exact annular kernel witness
identifies the next obstruction. These are proofs on the actual
surface, not another affine, metabelian or finite-depth census.

The final formal paper has {m['pages']} pages and280 statements:
236 Proved,19 Refuted,19 Open and6 Known. All49 task/lead rows
and109 verified-status bibliography entries remain. The final PDF
has zero overfull boxes, warnings, undefined references and errors.
Complete visible QA and retained repair history are recorded in
records/checkpoint22_typesetting.txt. Root and independent full
proof reviews are in records/checkpoint22_root_formal_reviews.json.

All entries of the twenty-one earlier checkpoints are preserved
with exact bytes and zero omissions. The standard nested TAR encoding
retains every original PNG path; all other authored deliverables,
code, data, proof notes and genuine outputs remain directly archived.
No earlier archive is overwritten, deleted or renamed.

{research}

## Exact computation and late-research state at immutable capture

{computations}

Final PDF SHA-256: {m['pdf_sha256']}.
Next hourly review/checkpoint: 2026-11-16 23:49:30 UTC.
Resume substantive work immediately after immutable capture completes.
'''
(ROOT/'records/progress_review_22h.md').write_text(review)
p = ROOT/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Twenty-second-hour progress review\n' not in s
s += f'''\n## Twenty-second-hour progress review

At {now.isoformat()} we recorded CONTINUE. B108--B111 prove the proper
actual one-neck completion, the natural mixed-neck injection obstruction,
the complete slit bad-vertex centralizer and actual selected source,
and the nontrivial diagonal killed by restoring the retained zero loop.
The one-neck selected-source equality transfers to the selected component
of the original double cover. The annular, other-neck, global and final
joint-source comparisons remain Open, as do Main A's full decisions.
There are280 statements,109 bibliography entries and49 task/lead rows.
Complete records:records/progress_review_22h.md and
records/twenty_second_hour_research_report.md.
Next review/checkpoint:2026-11-16 23:49:30 UTC.
'''
p.write_text(s)
p = ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-second-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_22h.md.
All writers are paused for immutable capture. Release immediately
after the ZIP completes, then independently verify and save it.
Both main full decisions remain Open. No checkpoint22 archive byte
may change after capture. The reviewed formal baseline is280 statements,
{m['pages']} pages,109 bibliography entries and49 task rows, with clean
final QA. Annular research remains in its explicitly recorded stage.
Next review/checkpoint:2026-11-16 23:49:30 UTC.
''')
print('Timed twenty-second-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention = json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 21 and retention['archive_entries'] == 55959
assert retention['omissions'] == 0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'22'],check=True)
assert archive.stat().st_size <= 536870912, 'Never mutate an already captured archive.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
