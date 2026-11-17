"""Capture exactly one immutable checkpoint24 after the timed review."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 17, 0, 49, 30, tzinfo=timezone.utc)
archive = ROOT.parent/'LM4_SUCCESSOR_checkpoint_24.zip'
assert not archive.exists()
remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the timed review.'
while remaining > 0:
    time.sleep(min(0.5, remaining))
    remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
subprocess.run([sys.executable, str(ROOT/'code/check_checkpoint24_preconditions.py')], check=True)
m = json.loads((ROOT/'records/checkpoint24_metrics.json').read_text())
research = (ROOT/'records/twenty_fourth_hour_research_report.md').read_text()
computations = (ROOT/'records/checkpoint24_computation_audit_state.md').read_text()
review = f'''# Twenty-fourth-hour progress review

Scheduled review: 2026-11-17 00:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. This hour advances the actual
Main-B obstruction problem through three completely proved comparisons.
B115 excludes every extension of the actual prefix substitution whose
base image is ordinary and has odd geometric winding, discretely and in
full profinite completion. B116 computes two exact discrete regional
centralizers with abelianization ranks six and three, excluding every
regional automorphism extending that substitution. B117 identifies the
actual neck-plus-base subgroup as an ordinary regional retract and gives
its marked index-two tree graph presentation, retaining the actual branch
square word and proving full induced profinite topology.

The later actual boundary/corner and ordinary-cover derivations attack
the remaining cross relations. Their exact proven and unproved gates are
retained in the research report below. No regional comparison is silently
transferred through those cross relations; neither main decision is inferred.
This is progress on actual groups, maps and topologies, not a restarted
affine, metabelian or finite-depth census.

The final formal paper has {m['pages']} pages and 286 statements:
242 Proved, 19 Refuted, 19 Open and 6 Known. All 49 task/lead rows and
111 bibliography entries remain, with all 111 printed. The first combined
build is clean, with zero overfull boxes, warnings, undefined references
or errors. Fresh final visible QA covers 39 pages in five contact sheets
and 15 individual pages, including every mathematical page 352--361.
Complete review bindings are in checkpoint24_root_formal_reviews.json.

All 68331 logical entries of the twenty-three earlier checkpoints are
retained byte-exactly with zero omissions. Verification images and historical
PDFs use separately hashed standard TAR containers inside the ZIP; every
original path and byte remains in the logical manifest, and the current
main PDF remains a direct ZIP entry. No earlier archive is changed,
deleted, renamed or overwritten. Actual native TAR restoration of both
containers will be independently checked immediately after capture.

{research}

## Exact computation and late-research state at immutable capture

{computations}

Final PDF SHA-256: {m['pdf_sha256']}.
Next hourly review/checkpoint: 2026-11-17 01:49:30 UTC.
Resume substantive work immediately after immutable capture completes.
'''
(ROOT/'records/progress_review_24h.md').write_text(review)
p = ROOT/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Twenty-fourth-hour progress review\n' not in s
s += f'''\n## Twenty-fourth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B115--B117 prove the actual
ordinary-section obstruction, the two intrinsic regional centralizers,
and the actual neck-plus-base retract with its marked finite-index tree
graph group and full topology. The actual post-cross source centralizer,
other necks, global transfer and final joint-source comparison remain Open,
as do Main A's full decisions. Late boundary/corner and ordinary-cover
research is retained at its stated scope. There are 286 statements,
111 printed bibliography entries and 49 task/lead rows.
Complete records: records/progress_review_24h.md and
records/twenty_fourth_hour_research_report.md.
Next review/checkpoint: 2026-11-17 01:49:30 UTC.
'''
p.write_text(s)
p = ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-fourth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_24h.md.
All writers are paused for immutable capture. Release immediately after
the ZIP completes, then independently verify and save it. Both main full
decisions remain Open. No checkpoint24 archive byte may change after
capture. The reviewed formal baseline is 286 statements, 450 pages,
111 printed references and 49 task rows, with clean final QA. Exact later
research is scoped in the computation audit. Two standard TAR containers
preserve every original image and historical PDF path; current main PDF
is a direct ZIP entry. Next review/checkpoint: 2026-11-17 01:49:30 UTC.
''')
print('Timed twenty-fourth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT/'code/refresh_computation_inventory.py')], check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(ROOT/'code/preserve_checkpoint_versions.py')], stdout=stream, check=True)
retention = json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 23 and retention['archive_entries'] == 68331
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(ROOT/'code/package_checkpoint.py'), '24'], check=True)
assert archive.stat().st_size <= 536870912, 'Never mutate an already captured archive.'
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
