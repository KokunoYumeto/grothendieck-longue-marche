"""Capture one immutable checkpoint23 after the timed review and writer pause."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026,11,16,23,49,30,tzinfo=timezone.utc)
archive = ROOT.parent/'LM4_SUCCESSOR_checkpoint_23.zip'
assert not archive.exists()
remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the timed review.'
while remaining > 0:
    time.sleep(min(0.5,remaining))
    remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
subprocess.run([sys.executable,str(ROOT/'code/check_checkpoint23_preconditions.py')],check=True)
assert (ROOT/'records/checkpoint23_writer_pause.md').exists()
m = json.loads((ROOT/'records/checkpoint23_metrics.json').read_text())
research = (ROOT/'records/twenty_third_hour_research_report.md').read_text()
computations = (ROOT/'records/checkpoint23_computation_audit_state.md').read_text()
review = f'''# Twenty-third-hour progress review

Scheduled review: 2026-11-16 23:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. This hour advances the actual
Main-B obstruction problem. B112 proves the actual annular bad-region
centralizer and its full topology. B113 transfers both fixed-source
comparisons to the whole inner/outer regions, including the selected
original outer cover. B114 proves the exact actual one-neck quotient
with two independently nontrivial cross relations. The selected lift,
entire common marking and both geometric base loops are retained.

Subsequent exact research supplies the actual nonabelian mirror map,
the whole nine-generator/thirty-six-relator presentation and its
eight-generator/twenty-four-relator mirror extension. The true coarse
bundle and its complete height kernel correct a failed zero-translate
simplification. These are actual geometric/group comparisons, not a
new affine, metabelian or finite-depth census. The precise unresolved
post-quotient centralizer remains an active substantive gate.

The final formal paper has {m['pages']} pages and283 statements:
239 Proved,19 Refuted,19 Open and6 Known. All49 task/lead rows
and111 verified-status bibliography entries remain. The final PDF
has zero overfull boxes,warnings,undefined references anderrors.
Fresh visible QA is in records/checkpoint23_typesetting.txt; complete
proof-review bindings are in checkpoint23_root_formal_reviews.json.

All61931 logical entries of the twenty-two earlier checkpoints are
retained byte-exactly with zero omissions. Standard TAR hardlinks retain
every original verification-image path. No earlier archive is changed,
deleted,renamed or overwritten.

{research}

## Exact computation and late-research state at immutable capture

{computations}

Final PDF SHA-256: {m['pdf_sha256']}.
Next hourly review/checkpoint: 2026-11-17 00:49:30 UTC.
Resume substantive work immediately after immutable capture completes.
'''
(ROOT/'records/progress_review_23h.md').write_text(review)
p = ROOT/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Twenty-third-hour progress review\n' not in s
s += f'''\n## Twenty-third-hour progress review

At {now.isoformat()} we recorded CONTINUE. B112--B114 prove the actual
annular regional centralizers,whole-region and selected-cover transfer,
and the exact one-neck quotient by two independent cross commutators.
The actual post-quotient source centralizer,other necks,global source
and final joint-source comparisons remain Open,as do Main A's full
decisions. The late exact mirror and coarse-bundle comparisons are
retained as research at their stated scope. There are283 statements,
111 bibliography entries and49 task/lead rows.
Complete records:records/progress_review_23h.md and
records/twenty_third_hour_research_report.md.
Next review/checkpoint:2026-11-17 00:49:30 UTC.
'''
p.write_text(s)
p = ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-third-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_23h.md.
All writers are paused for immutable capture. Release immediately
after the ZIP completes,then independently verify and save it.
Both main full decisions remain Open. No checkpoint23 archive byte
may change after capture. The reviewed formal baseline is283 statements,
{m['pages']} pages,111 bibliography entries and49 task rows,with clean
final QA. Exact later research is scoped in the computation audit.
Next review/checkpoint:2026-11-17 00:49:30 UTC.
''')
print('Timed twenty-third-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention = json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 22 and retention['archive_entries'] == 61931
assert retention['omissions'] == 0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'23'],check=True)
assert archive.stat().st_size <= 536870912, 'Never mutate an already captured archive.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
