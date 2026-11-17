"""Create exactly one immutable checkpoint31 after its scheduled review.

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
    deadline = datetime(2026, 11, 17, 7, 49, 30, tzinfo=timezone.utc)
    next_review = '2026-11-17 08:49:30 UTC'
    archive = root.parent / 'LM4_SUCCESSOR_checkpoint_31.zip'
    assert not archive.exists()
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
    assert remaining <= 60, 'Start only within one minute before the scheduled review, or later.'
    while remaining > 0:
        time.sleep(min(.5, remaining))
        remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
    subprocess.run([sys.executable, str(root / 'code/check_checkpoint31_preconditions.py')], check=True)
    now = datetime.now(timezone.utc)
    read = lambda rel: json.loads((root / rel).read_text())
    m = read('records/checkpoint31_metrics.json')
    visual = read('records/checkpoint31_visual_review.json')
    research = (root / 'records/thirty_first_hour_research_report.md').read_text()
    audit = (root / 'records/checkpoint31_computation_audit_state.md').read_text()
    late = read('records/checkpoint31_root_late_reviews.json')
    review = f'''# Thirty-first-hour progress review

Scheduled review:2026-11-17 07:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main decisions remain Open. The ten frozen formal sources A92--A94 and B148--B154 retain the actual
common-word and canonical comparison hypotheses, the marked stabilizer
and remaining-contact presentations, the complete one-sided filling and
mirrored-neck comparisons, and the direct compact stabilizer and finite-
permutation proof of the completed fixed section.
The exact current research and remaining gates are recorded below.
No carrier properness, quotient comparison or nonsplitting obstruction
is substituted for actual filling survival or the icosahedral K=1 gate.

The formal paper has {m['pages']} pages and333 statements:289 Proved,
19 Refuted,19 Open and6 Known. All49 task/lead rows and114 bibliography
entries are retained; all114 references are printed. All ten integrated
formal sources are byte-identical to their fully reviewed inputs.
Final PDF bytes:{m['pdf_bytes']}; SHA-256:{m['pdf_sha256']}.
All {len(visual['required_math_pages'])} new mathematical pages were
individually inspected; {len(visual['individually_inspected_pages'])}
final pages were individually viewed and
{visual['contact_sheets_inspected']} separately inspected contact sheets
cover {len(visual['rendered_pages'])} rendered pages at144dpi.
Final log and stabilized engine stdout have no overfull boxes, actual
warnings, undefined references or errors. The final notice count is {len(visual['final_log_and_stdout_audits'][0]['underfull_notices'])};
the complete accepted scope is recorded explicitly:
{visual['underfull_scope']}.
The late record binds {len(late['proof_sources'])} complete research
proofs without increasing the frozen formal statement count.

All123532 logical entries of the30 previous immutable archives are
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
    review_path = root / 'records/progress_review_31h.md'
    assert not review_path.exists(), 'Preserve any previous driver attempt for review.'
    report_path = root / 'LM4_SUCCESSOR_report.md'
    report = report_path.read_text()
    continuation_path = root / 'records/continuation_state.md'
    continuation = continuation_path.read_text()
    assert '## Thirty-first-hour progress review\n' not in report
    assert '## Actual thirty-first-hour review\n' not in continuation
    review_path.write_text(review)
    report_path.write_text(report + f'''
## Thirty-first-hour progress review

At {now.isoformat()} we recorded CONTINUE. The ten sources A92--A94 and
B148--B154 are integrated with complete root and independent source
reviews. Exact latest research, failure records and limits are bound in
the late review and research report. Both main decisions remain Open.
The frozen formal baseline is333 statements, {m['pages']} pages,
114 printed references and49 synchronized task rows. The sole new
archive retains all30 predecessors through three lossless standard TAR
containers; its actual streams and every restored path will be checked.
Next review:{next_review}.
''')
    continuation_path.write_text(continuation + f'''
## Actual thirty-first-hour review

CONTINUE recorded at {now.isoformat()}. All writers are paused for this
single immutable capture. Release all three immediately when the archive
closes, before verification or upload; then verify every logical entry,
all three native TAR restorations and the actual64MiB data stream, save,
and deliver in commentary. Both main decisions remain Open. The frozen
formal baseline is333 statements, {m['pages']} pages,114 printed references
and49 task rows. Continue the exact odd-head/nonlinear cusp and actual
ambient filling/fixed-source gates with every conjugator and source orbit.
Next review/checkpoint:{next_review}.
''')
    print('Timed thirty-first-hour review:', now.isoformat(), 'CONTINUE', flush=True)
    subprocess.run([sys.executable, str(root / 'code/refresh_computation_inventory.py')], check=True)
    with (root / 'records/checkpoint31_version_retention_run.out').open('x') as stream:
        subprocess.run([sys.executable, str(root / 'code/preserve_checkpoint_versions.py')],
                       stdout=stream, check=True)
    retention = read('records/checkpoint_version_retention_summary.json')
    assert retention['archives'] == 30 and retention['archive_entries'] == 123532
    assert retention['omissions'] == 0
    subprocess.run([sys.executable, str(root / 'code/package_checkpoint.py'), '31'], check=True)
    assert archive.stat().st_size <= 536870912, 'Never mutate an already captured archive.'
    print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)


if __name__ == '__main__':
    main()
