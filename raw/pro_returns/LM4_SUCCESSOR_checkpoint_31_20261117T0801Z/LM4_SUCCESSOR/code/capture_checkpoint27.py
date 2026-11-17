"""Capture exactly one immutable checkpoint27 after the hourly review."""
from datetime import datetime,timezone
from pathlib import Path
import json,subprocess,sys,time

root=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,17,3,49,30,tzinfo=timezone.utc)
archive=root.parent/'LM4_SUCCESSOR_checkpoint_27.zip'
assert not archive.exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the scheduled review.'
while remaining>0:
    time.sleep(min(.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
subprocess.run([sys.executable,str(root/'code/check_checkpoint27_preconditions.py')],check=True)
m=json.loads((root/'records/checkpoint27_metrics.json').read_text())
research=(root/'records/twenty_seventh_hour_research_report.md').read_text()
audit=(root/'records/checkpoint27_computation_audit_state.md').read_text()
review=f'''# Twenty-seventh-hour progress review

Scheduled review: 2026-11-17 03:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. New actual Main-B progress resolves
the pre-cross full-topology gate for all six marked source generators.
The complete two-sheet construction identifies the exact ordinary base
kernel by an increasing matching union and the compact base kernel by an
independent finite-normal extension criterion. The earlier omitted-mirror
research identification was withdrawn before formal integration, with all
original attempts and reviews preserved. Neither a closed discrete-kernel
equality nor finite-stage stabilization is inferred.

The return to Main A establishes a stronger necessary description of the
actual canonical negative-GT0 Fox defect: all three nonidentity elements
of the actual Klein four group act freely off the base coset, and the
reduced compact coset module is induced over the constant finite-group
ring. This does not prove a full Lambda-linear splitting or vanishing.
The canonical Fox-unit/marked-generation implication remains Open.

The formal paper has {m['pages']} pages and 303 statements: 259 Proved,
19 Refuted, 19 Open and 6 Known. All 49 task/lead rows and 113 bibliography
entries remain; all 113 are printed. The final complete-source reviews,
visible QA and metrics are bound to PDF SHA-256 {m['pdf_sha256']}.
Every new mathematical page has been individually inspected. Both the
final combined log and actual final engine stdout were scanned
case-insensitively using the clean derived TeX environment.

All 89536 logical entries of the twenty-six earlier archives are retained
byte-exactly with zero omissions. Both standard TAR containers retain
every original image and historical/preview-PDF path and byte. The image
container now uses lossless ZIP_LZMA compression, as the document container
already did; the current main PDF remains directly in the ZIP. No earlier
archive is changed. Native restoration of both actual new containers is
independently verified immediately after capture.

{research}

## Exact computation and research state at immutable capture

{audit}

Next hourly review/checkpoint: 2026-11-17 04:49:30 UTC.
Resume substantive research immediately after immutable capture.
'''
(root/'records/progress_review_27h.md').write_text(review)
p=root/'LM4_SUCCESSOR_report.md';s=p.read_text()
assert '## Twenty-seventh-hour progress review\n' not in s
s+=f'''\n## Twenty-seventh-hour progress review

At {now.isoformat()} we recorded CONTINUE. B131--B134 prove actual
d-contact noncommutation, the actual free source pair with full topology,
the pre-cross free-six source with full topology, and the corrected
two-sheet edge pushout with separately proved ordinary and compact kernel
criteria. The actual Main-A V4 defect now has a complete constant-ring
induced-module description. Neither main decision is settled.
The formal baseline is 303 statements, {m['pages']} pages, 113 printed
references and 49 synchronized task/lead rows. See the complete review
and research report for exact remaining gates and preserved corrections.
Next review/checkpoint: 2026-11-17 04:49:30 UTC.
''';p.write_text(s)
p=root/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-seventh-hour review

CONTINUE recorded at {now.isoformat()}. All writers are paused for the
single immutable capture. Release all three immediately when it finishes,
then verify every archive entry and native TAR restoration, save and
deliver in commentary. Both main decisions remain Open. The reviewed
formal baseline is 303 statements, {m['pages']} pages, 113 printed references
and 49 task rows. Exact two-sheet source-kernel evaluation, fixed-source
comparison and the actual canonical Fox unit remain active.
Next review/checkpoint: 2026-11-17 04:49:30 UTC.
''')
print('Timed twenty-seventh-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(root/'code/refresh_computation_inventory.py')],check=True)
with (root/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(root/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention=json.loads((root/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==26 and retention['archive_entries']==89536
assert retention['omissions']==0
subprocess.run([sys.executable,str(root/'code/package_checkpoint.py'),'27'],check=True)
assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
