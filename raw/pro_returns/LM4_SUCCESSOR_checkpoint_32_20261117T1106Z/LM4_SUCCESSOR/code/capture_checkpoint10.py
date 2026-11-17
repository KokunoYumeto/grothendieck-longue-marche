"""Capture the authorized tenth hourly checkpoint at its scheduled time.

Run only after every writer acknowledges the brief snapshot pause.
Earlier archives are read only; packaging refuses any overwrite.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 16, 10, 49, 30, tzinfo=timezone.utc)
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_10.zip').exists()
while True:
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
    if remaining <= 0:
        break
    time.sleep(min(0.5, remaining))
now = datetime.now(timezone.utc)
metrics = json.loads((ROOT / 'records/checkpoint10_metrics.json').read_text())
assert metrics['statements'] == 228 and metrics['task_rows'] == 49
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
review = f'''# Tenth-hour progress review

Scheduled review:2026-11-16 10:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. We continue because the current
work directly attacks their lifting and full-topology obstructions.
We do not end the task at this checkpoint.

For A, the actual twenty-factor source quotient is complete, including
its coupled class-three terms and both peripheral normalizer frames.
The full scalar refinement has dimension128 and the next refinement
is relatively perfect. Its canonical action and simultaneous frames
have now been proved through the entire integral tower, with an actual
mod-four compatibility witness and independent original group-law
checks. A full positive automorphism realizes these data. The square
of its full negative companion and cofinality remain unresolved.
Current work moves to actual mixed ordinary cups involving the binary
s-cohomology rows; the first16 mixed cups have passed source, action,
square and s-frame gates. Their complete scalar refinement remains
under investigation. This is an actual-source extension problem,
not an inference from a graded or pro-prime shadow.

The unrestricted equivariant central-lifting shortcut is separately
refuted by the explicit perfect-kernel M10 extension. Its tempting
negative peripheral heads fail the actual central spin condition,
so they do not refute the source-specific criterion. That failed
stronger route is retained with its exact limitation, and the next
counting question keeps existing source epimorphisms and local
reflection conditions explicit.

For B, the full colored common-involution comparison and the full
dihedral centralizer are now formal, with the actual pure-lift indices,
canonical splitting, and valid prime-order completed comparisons.
The overlapping branch-ordered embeddings are explicitly attributed
to attached LM4 F12/F14, and the pure D5/noninjective rigid results
are compared with LM4 F11. The new four-moving-point Birman cocycle
has an exact completed zero set K, but it has not bypassed LM4 F15's
source-membership condition or F18-F29's drilled-source obstruction.
The current target is uniform finite-cover separation or actual source
membership beyond that already-proved correction step. No discrete
injectivity result is promoted to a completed intersection theorem.

The final formal paper has{metrics['pages']} pages and228 numbered
statements:189 Proved,14 Refuted,19 Open,6 Known. It has87 bibliography
entries and all49 requested task rows. Its exact final PDF hash is
{metrics['pdf_sha256']}.
All build overflow/warning/undefined-reference/error counts are zero.
The final rendered visual QA is recorded in checkpoint10_typesetting.txt;
earlier QA versions and the final attribution comparison are retained.

The next review and checkpoint are scheduled for11:49:30 UTC.
We resume substantive work immediately after immutable capture.
'''
(ROOT / 'records/progress_review_10h.md').write_text(review)
p = ROOT / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Tenth-hour progress review\n' not in s
s += f'''\n## Tenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. The completed actual cubic
scalar tower and the current mixed-source extension work advance the
main involution problem. The full-topology work retains its exact
source-membership obstruction and now explicitly distinguishes the
attached LM4 results from the current refinements. Both main full
decisions remain Open. See records/progress_review_10h.md.
The next scheduled review and checkpoint are at11:49:30 UTC.
'''
p.write_text(s)
p = ROOT / 'records/continuation_state.md'
s = p.read_text() + f'''\n## Actual tenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_10h.md.
The checkpoint is now being captured with every writer paused.
Release the agents immediately after immutable ZIP capture; upload
and independent verification follow without changing that archive.
Next checkpoint/review:2026-11-16 11:49:30 UTC.
'''
p.write_text(s)
print('Timed tenth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT / 'code/refresh_computation_inventory.py')], check=True)
with (ROOT / 'records/checkpoint_version_retention_run.out').open('w') as f:
    subprocess.run([sys.executable, str(ROOT / 'code/preserve_checkpoint_versions.py')],
                   stdout=f, check=True)
subprocess.run([sys.executable, str(ROOT / 'code/package_checkpoint.py'), '10'], check=True)
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
