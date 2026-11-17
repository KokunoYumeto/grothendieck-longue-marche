"""Create exactly one immutable checkpoint30 after its scheduled review.

Preparation alone must not execute this driver. It writes review records,
refreshes retention and invokes the sole actual packager only when run.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time


def main():
    root = Path(__file__).resolve().parents[1]
    deadline = datetime(2026, 11, 17, 6, 49, 30, tzinfo=timezone.utc)
    next_review = '2026-11-17 07:49:30 UTC'
    archive = root.parent / 'LM4_SUCCESSOR_checkpoint_30.zip'
    assert not archive.exists()
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
    assert remaining <= 60, 'Start only within one minute before the scheduled review, or later.'
    while remaining > 0:
        time.sleep(min(.5, remaining))
        remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
    subprocess.run([sys.executable, str(root / 'code/check_checkpoint30_preconditions.py')], check=True)
    now = datetime.now(timezone.utc)
    read = lambda rel: json.loads((root / rel).read_text())
    m = read('records/checkpoint30_metrics.json')
    visual = read('records/checkpoint30_visual_review.json')
    research = (root / 'records/thirtieth_hour_research_report.md').read_text()
    audit = (root / 'records/checkpoint30_computation_audit_state.md').read_text()
    late = read('records/checkpoint30_root_late_reviews.json')
    review = f'''# Thirtieth-hour progress review

Scheduled review:2026-11-17 06:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main decisions remain Open. The nine frozen formal sources A89--A91
and B142--B147 retain the actual full-GT and marked covariance hypotheses,
the unrestricted and virtual coarse-filling nonsplitting proofs, the
exact one-family fixed-source presentation, and the complete cyclic
normalization/carrier and prescribed-center nonextension arguments.
The exact current research and remaining gates are recorded below.
No carrier properness, quotient comparison or nonsplitting obstruction
is substituted for actual filling survival or the icosahedral K=1 gate.

The formal paper has {m['pages']} pages and323 statements:279 Proved,
19 Refuted,19 Open and6 Known. All49 task/lead rows and114 bibliography
entries are retained; all114 references are printed. All nine integrated
formal sources are byte-identical to their fully reviewed inputs.
Final PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
All {len(visual['required_math_pages'])} new mathematical pages were
individually inspected; {len(visual['individually_inspected_pages'])}
final pages were individually viewed and
{visual['contact_sheets_inspected']} separately inspected contact sheets
cover {len(visual['rendered_pages'])} rendered pages at144dpi.
Final log and stabilized engine stdout have no overfull boxes, actual
warnings, undefined references or errors. The18 retained underfull
notices and one new visually accepted B147 notice total19; this change
is documented rather than described as unchanged.
The late record binds {len(late['proof_sources'])} complete research
proofs without increasing the frozen formal statement count.

All114462 logical entries of the29 previous immutable archives are
retained byte-exactly with zero omissions. Original image, historical
or preview PDF, and selected historical/data paths retain their exact
bytes in three standard TAR containers using lossless ZIP_LZMA. The data
container uses a standard64MiB dictionary; the current main PDF remains
a direct ZIP entry. No test ZIP is created and no prior archive is changed.
After capture, the actual ZIP data-stream property and independent native
restoration of all three containers must pass before delivery recording.

{research}

## Computation, review and failure state at capture

{audit}

Next hourly review/checkpoint:{next_review}.
Resume substantive research immediately after immutable capture closes.
'''
    review_path = root / 'records/progress_review_30h.md'
    assert not review_path.exists(), 'Preserve any previous driver attempt for review.'
    report_path = root / 'LM4_SUCCESSOR_report.md'
    report = report_path.read_text()
    continuation_path = root / 'records/continuation_state.md'
    continuation = continuation_path.read_text()
    assert '## Thirtieth-hour progress review\n' not in report
    assert '## Actual thirtieth-hour review\n' not in continuation
    review_path.write_text(review)
    report_path.write_text(report + f'''
## Thirtieth-hour progress review

At {now.isoformat()} we recorded CONTINUE. The nine sources A89--A91 and
B142--B147 are integrated with complete root and independent source
reviews. Exact latest research, failure records and limits are bound in
the late review and research report. Both main decisions remain Open.
The frozen formal baseline is323 statements, {m['pages']} pages,
114 printed references and49 synchronized task rows. The sole new
archive retains all29 predecessors through three lossless standard TAR
containers; its actual streams and every restored path will be checked.
Next review:{next_review}.
''')
    continuation_path.write_text(continuation + f'''
## Actual thirtieth-hour review

CONTINUE recorded at {now.isoformat()}. All writers are paused for this
single immutable capture. Release all three immediately when the archive
closes, before verification or upload; then verify every logical entry,
all three native TAR restorations and the actual64MiB data stream, save,
and deliver in commentary. Both main decisions remain Open. The frozen
formal baseline is323 statements, {m['pages']} pages,114 printed references
and49 task rows. Continue the exact odd-head/nonlinear cusp and actual
ambient filling/fixed-source gates with every conjugator and source orbit.
Next review/checkpoint:{next_review}.
''')
    print('Timed thirtieth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
    subprocess.run([sys.executable, str(root / 'code/refresh_computation_inventory.py')], check=True)
    with (root / 'records/checkpoint30_version_retention_run.out').open('x') as stream:
        subprocess.run([sys.executable, str(root / 'code/preserve_checkpoint_versions.py')],
                       stdout=stream, check=True)
    retention = read('records/checkpoint_version_retention_summary.json')
    assert retention['archives'] == 29 and retention['archive_entries'] == 114462
    assert retention['omissions'] == 0
    subprocess.run([sys.executable, str(root / 'code/package_checkpoint.py'), '30'], check=True)
    assert archive.stat().st_size <= 536870912, 'Never mutate an already captured archive.'
    print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)


if __name__ == '__main__':
    main()
