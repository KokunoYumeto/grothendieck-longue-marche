"""Capture exactly one immutable checkpoint25 after the hourly review."""
from datetime import datetime,timezone
from pathlib import Path
import json
import subprocess
import sys
import time

root=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,17,1,49,30,tzinfo=timezone.utc)
archive=root.parent/'LM4_SUCCESSOR_checkpoint_25.zip'
assert not archive.exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the scheduled review.'
while remaining>0:
    time.sleep(min(.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
subprocess.run([sys.executable,str(root/'code/check_checkpoint25_preconditions.py')],check=True)
m=json.loads((root/'records/checkpoint25_metrics.json').read_text())
research=(root/'records/twenty_fifth_hour_research_report.md').read_text()
audit=(root/'records/checkpoint25_computation_audit_state.md').read_text()
review=f'''# Twenty-fifth-hour progress review

Scheduled review: 2026-11-17 01:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. This hour advances the actual
Main-B source/centralizer problem through six completely proved
comparisons. The actual final neck survives all cross and prefix
relations as an ordinary retract with full profinite topology. The
intermediate completed cone centralizer is exactly the closure of its
discrete centralizer. The whole family-unfilled ordinary group has an
exact F11/two-source-operator presentation retaining all forty node
seeds and every signed translate, with an exact discrete/full remaining
fixed-kernel gate. These are actual-group results, not a restarted
finite-depth or metabelian census.

The formal paper has {m['pages']} pages and 292 statements:248 Proved,
19 Refuted,19 Open and6 Known. All49 task/lead rows and112 bibliography
entries remain; all112 are printed. Final visible QA and exact metrics
are bound to PDF SHA-256 {m['pdf_sha256']}.

The final combined log is checked case-insensitively. Earlier Warning-only
counts missed lowercase engine font-map warnings in the logs listed in
checkpoint25_fontmap_warning_audit.json. Those original files remain
unaltered; the new derived map comments only nine malformed headings.
The correction is explicit and separate from the unchanged overfull
box counts.

All74969 logical entries of the twenty-four earlier archives are retained
byte-exactly with zero omissions. Both standard TAR containers preserve
every original image/historical-PDF path and byte; the current main PDF
remains directly in the ZIP. No earlier archive is overwritten, renamed,
deleted or modified. Native restoration of both actual new containers
will be independently checked immediately after capture.

{research}

## Exact computation and research state at immutable capture

{audit}

Next hourly review/checkpoint:2026-11-17 02:49:30 UTC.
Resume substantive research immediately after immutable capture.
'''
(root/'records/progress_review_25h.md').write_text(review)
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Twenty-fifth-hour progress review\n' not in s
s+=f'''\n## Twenty-fifth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B118--B123 prove the actual
boundary and completed-neck intersection, retained filled fixed group,
proper intermediate completed amalgam, final ordinary-neck retraction,
intermediate completed centralizer closure, and exact whole two-operator
family-kernel reduction. The actual unfilled fixed-source equality,
remaining necks, global transfer and final joint-source condition remain
Open, as do Main A's full decisions. The formal baseline is292 statements,
{m['pages']} pages,112 printed references and49 task/lead rows.
See records/progress_review_25h.md and the complete research report.
Next review/checkpoint:2026-11-17 02:49:30 UTC.
'''
p.write_text(s)
p=root/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-fifth-hour review

CONTINUE recorded at {now.isoformat()}. All writers are paused for the
single immutable capture. Release all three immediately when it finishes,
then verify every archive entry and native TAR restoration, save and
deliver. Both main decisions remain Open. The reviewed formal baseline
is292 statements,{m['pages']} pages,112 printed references and49 taskrows.
Source bindings and final visible QA are in the checkpoint25 records.
Next review/checkpoint:2026-11-17 02:49:30 UTC.
''')
print('Timed twenty-fifth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(root/'code/refresh_computation_inventory.py')],check=True)
with (root/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(root/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==24 and retention['archive_entries']==74969
assert retention['omissions']==0
subprocess.run([sys.executable,str(root/'code/package_checkpoint.py'),'25'],check=True)
assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
