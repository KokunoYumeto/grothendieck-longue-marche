"""Capture exactly one immutable checkpoint26 after the hourly review."""
from datetime import datetime,timezone
from pathlib import Path
import json
import subprocess
import sys
import time

root=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,17,2,49,30,tzinfo=timezone.utc)
archive=root.parent/'LM4_SUCCESSOR_checkpoint_26.zip'
assert not archive.exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the scheduled review.'
while remaining>0:
    time.sleep(min(.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
subprocess.run([sys.executable,str(root/'code/check_checkpoint26_preconditions.py')],check=True)
m=json.loads((root/'records/checkpoint26_metrics.json').read_text())
research=(root/'records/twenty_sixth_hour_research_report.md').read_text()
audit=(root/'records/checkpoint26_computation_audit_state.md').read_text()
review=f'''# Twenty-sixth-hour progress review

Scheduled review:2026-11-17 02:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. This hour advances the actual
Main-B comparison through seven completely proved propositions.
The actual free-six source map is noninjective in both categories;
its explicitly commuting source words generate a retracted Z2 and
Zhat2. The final four-prefix filling kills a specified nontrivial
element of the completed intermediate centralizer. The exact actual
compact family module and a continuous free-two retract prove nonlinear
nonlifting while preserving the remaining fixed-source equality as
Open. These are actual-group comparisons, not finite-depth evidence.

The formal paper has {m['pages']} pages and299 statements:255 Proved,
19 Refuted,19 Open and6 Known. All49 task/lead rows and112 bibliography
entries remain; all112 are printed. The final complete-source reviews,
visible QA and metrics are bound to PDF SHA-256 {m['pdf_sha256']}.
Every new mathematical page has been individually inspected. Both
the final combined log and actual final engine stdout were scanned
case-insensitively in the clean derived TeX environment.

All82029 logical entries of the twenty-five earlier archives are
retained byte-exactly with zero omissions. Both standard TAR containers
retain every original image and historical/preview-PDF path and byte;
the current main PDF remains directly in the ZIP. The newly authored
initial B128 PDF is explicitly retained. No earlier archive is changed.
Native restoration of both actual new containers will be independently
verified immediately after capture.

{research}

## Exact computation and research state at immutable capture

{audit}

Next hourly review/checkpoint:2026-11-17 03:49:30 UTC.
Resume substantive research immediately after immutable capture.
'''
(root/'records/progress_review_26h.md').write_text(review)
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Twenty-sixth-hour progress review\n' not in s
s+=f'''\n## Twenty-sixth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B124--B130 prove the actual
outer source retraction and exact source abelianizations, proper
ordinary-parity star, completed corner face and discrete axes, whole
Schreier kernel and actual compact module, nonlinear nonlifting, and
the actual source commutator with its Z2/Zhat2 retract. The actual
completed intermediate centralizer also has a specified nontrivial
element killed by the final filling. The unfilled fixed-source equality,
other necks, global transfer and final joint-source condition remain
Open. Both main decisions remain Open. The formal baseline is299
statements,{m['pages']} pages,112 printed references and49 task/lead rows.
See records/progress_review_26h.md and the complete research report.
Next review/checkpoint:2026-11-17 03:49:30 UTC.
'''
p.write_text(s)
p=root/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-sixth-hour review

CONTINUE recorded at {now.isoformat()}. All writers are paused for the
single immutable capture. Release all three immediately when it finishes,
then verify all archive entries and native TAR restorations, save and
deliver in commentary. Both main decisions remain Open. The reviewed
formal baseline is299 statements,{m['pages']} pages,112 printed references
and49 task rows. The source map is now proved noninjective; the actual
fixed-source equality remains Open. Final proof bindings and visible QA
are in the checkpoint26 records.
Next review/checkpoint:2026-11-17 03:49:30 UTC.
''')
print('Timed twenty-sixth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(root/'code/refresh_computation_inventory.py')],check=True)
with (root/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(root/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==25 and retention['archive_entries']==82029
assert retention['omissions']==0
subprocess.run([sys.executable,str(root/'code/package_checkpoint.py'),'26'],check=True)
assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
