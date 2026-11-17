"""Create exactly one immutable checkpoint28 after the scheduled hourly review."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time

root = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 17, 4, 49, 30, tzinfo=timezone.utc)
archive = root.parent / 'LM4_SUCCESSOR_checkpoint_28.zip'
assert not archive.exists()
remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the scheduled review.'
while remaining > 0:
    time.sleep(min(.5, remaining))
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
subprocess.run([sys.executable, str(root / 'code/check_checkpoint28_preconditions.py')], check=True)
m = json.loads((root / 'records/checkpoint28_metrics.json').read_text())
research = (root / 'records/twenty_eighth_hour_research_report.md').read_text()
audit = (root / 'records/checkpoint28_computation_audit_state.md').read_text()
review = f'''# Twenty-eighth-hour progress review

Scheduled review:2026-11-17 04:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main decisions remain Open. We have new actual full-topology and
overlap results, complete discrete and profinite one-family fixed-source comparisons,
and an exact marked three-cycle/canonical-frame reduction of the Main-A
cusp obstruction. These resolve concrete intermediate gates while
retaining the remaining full-word, ambient-kernel and global comparisons.
We do not count formalization alone as a new main-question resolution.

The formal paper has530 pages and308 statements:264 Proved,19 Refuted,
19 Open and6 Known. All49 task/lead rows and113 bibliography entries are
retained; all113 references are printed. The five new frozen formal
sources are byte-identical to their fully reviewed inputs. Final combined
PDF SHA-256:{m['pdf_sha256']}.
All21 new mathematical pages were individually inspected;26 final pages
in total were individually viewed, and four separate contact sheets cover
35 rendered pages. Final log and actual stabilized engine stdout have no
overfull boxes, actual warnings, undefined references or errors. Their18
pre-existing underfull notices are byte-identical by multiset to the
previous combined build.

All97426 logical entries of the27 previous immutable archives are retained
byte-exactly with zero omissions. Every original image and historical or
preview PDF path and byte is retained in standard TAR containers using
lossless ZIP_LZMA. The current main PDF remains a direct ZIP entry.
We create no test ZIP and modify no earlier archive. Independent native
restoration of both actual new containers follows capture.

{research}

## Computation, review and failure state at capture

{audit}

Next hourly review/checkpoint:2026-11-17 05:49:30 UTC.
Resume substantive research immediately after immutable capture closes.
'''
(root / 'records/progress_review_28h.md').write_text(review)
p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Twenty-eighth-hour progress review\n' not in s
s += f'''
## Twenty-eighth-hour progress review

At {now.isoformat()} we recorded CONTINUE. A85/A86 and B135--B137
are integrated with complete root and independent proof reviews. The
separate new research proves one actual translated ordinary overlap,
full compact whole-edge embeddings and their trivial intersection,
and discrete and profinite fixed-source equality in the exact one-family quotient, and supplies the genuine
three-cycle formulation of the remaining Main-A cusp gate. No result is
transferred to a stronger category or to the restored final ambient
group without its missing comparison. Both main decisions remain Open.
The formal baseline is308 statements,530 pages,113 printed references
and49 synchronized task rows. Next review:2026-11-17 05:49:30 UTC.
'''
p.write_text(s)
p = root / 'records/continuation_state.md'
p.write_text(p.read_text() + f'''
## Actual twenty-eighth-hour review

CONTINUE recorded at {now.isoformat()}. All writers are paused for this
single immutable capture. Release all three immediately when the archive
closes, before verification or upload; then verify all entries and both
native TAR restorations, save, and deliver in commentary. Both main
decisions remain Open. The frozen formal baseline is308 statements,
530 pages,113 printed references and49 task rows. Continue the actual
marked cusp/frame comparison, remaining fixed-kernel equality, translated
filling interactions and ambient kappa-kernel/source comparison.
Next review/checkpoint:2026-11-17 05:49:30 UTC.
''')
print('Timed twenty-eighth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(root / 'code/refresh_computation_inventory.py')], check=True)
with (root / 'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(root / 'code/preserve_checkpoint_versions.py')], stdout=stream, check=True)
retention = json.loads((root / 'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 27 and retention['archive_entries'] == 97426
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(root / 'code/package_checkpoint.py'), '28'], check=True)
assert archive.stat().st_size <= 536870912, 'Never mutate an already captured archive.'
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
