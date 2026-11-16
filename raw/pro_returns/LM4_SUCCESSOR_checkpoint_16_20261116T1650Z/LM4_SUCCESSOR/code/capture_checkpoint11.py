"""Capture the authorized eleventh hourly checkpoint at its scheduled time.

Run within one minute of the deadline, after all writers acknowledge the
brief pause. Earlier archives are read only; packaging refuses overwrite.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 16, 11, 49, 30, tzinfo=timezone.utc)
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_11.zip').exists()
remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the review.'
while remaining > 0:
    time.sleep(min(0.5, remaining))
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
metrics = json.loads((ROOT / 'records/checkpoint11_metrics.json').read_text())
assert metrics['statements'] == 236 and metrics['task_rows'] == 49
assert metrics['statuses'] == {'Known': 6, 'Proved': 197, 'Refuted': 14, 'Open': 19}
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == metrics['pdf_sha256']
qa = (ROOT / 'records/checkpoint11_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa

review = f'''# Eleventh-hour progress review

Scheduled review: 2026-11-16 11:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. We continue because this hour
resolved actual action/frame gates and proved an obstruction to a
proposed main lifting mechanism. The current work still attacks the
main questions; we do not end the task at this checkpoint.

For A, A72-A73 determine the complete mixed ordinary extension and
its704-dimensional scalar third subgroup,576 directions beyond the
earlier128, with the next scalar refinement relatively perfect. A75
solves its actual action and frame equations through every integral
level, including the six required old integral constraints. Original
group laws and independent checks verify the complete witness. A full
positive peripheral lift realizes the selected tower. Its full negative
square and cofinality remain Open.

A76 proves an actual prescribed-frame failure of global-negative
order-preserving lifting. The original finite action and s-frame pass
the actual finite source-central refinement and both quotient norms,
but every full normalized positive lift retaining them has a negative
companion whose square is nontrivial. Natural transgression forces the
six-cup quotient for every candidate; the exhaustive norm invariant
is nonzero. This is distinct from A70's mixed-multiplier obstruction
and A74's fixed-action equivariant conjugator obstruction. A71 proves
the rank-two trace constraint with its finite-ring and inverse-limit
comparisons, without claiming it detects all full finite quotients.

Late reviewed research locates A76's failure in one explicit finite
noncentral quotient Pi/Phi2(L), where L is the kernel of its actual
six-cup head. An open-Kurosh relation-module argument controls the
image of the s-centralizer there. It also sharply tests the theorem's
scope: keeping the original action but releasing the old finite frame
does admit a verified frame passing the six-cup test. Thus the local
obstruction cannot simply be promoted to all frames. These proofs,
programs, independent reviews and outputs are retained separately
from the frozen236-statement paper. No full involution follows from
the repaired finite witness.

For B, B75 gives the exact completed zero set of an actual split Birman
cocycle and its equivalent uniform finite-cover condition. The full
source and kernel topology are proved, but uniform separation remains
unresolved. Fresh reconstruction of the19 positive marginal lassos
gives actual braid words and monodromy. The ratio-pencil approach now
lists the special tangent fiber and all additional collision values;
normality and transport of the relative kernel are still being proved.
An explicit algebraic product-chart counterexample now refutes the
general relative special-fiber shortcut: a retained-only collision
does not guarantee deletion-kernel surjectivity. Its finite S3 times S3
certificate also proves the completed failure. This does not refute
the actual marginal claim. A focused test on that actual source checks
2238 admissible representation pairs and finds no counterexample;
excluded-base monodromy remains an explicit part of the next step.
The attached LM4 source audit extends throughF33, preserving explicit
credit for its already solved interaction-cocycle and affine results.
No further affine test is claimed to settle the main centralizer.

The final paper has {metrics['pages']} pages and236 numbered statements:
197 Proved,14 Refuted,19 Open,6 Known. It has91 bibliography entries
and all49 requested task rows. Its exact final PDF hash is
{metrics['pdf_sha256']}.
All build overflow/warning/undefined-reference/error counts are zero.
We rendered and visually reviewed52 pages, with enlarged inspection
of15 critical pages. See checkpoint11_typesetting.txt for exact scope.

The next review and checkpoint are scheduled for12:49:30 UTC.
We resume substantive work immediately after immutable capture.
'''
(ROOT / 'records/progress_review_11h.md').write_text(review)
p = ROOT / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Eleventh-hour progress review\n' not in s
s += f'''\n## Eleventh-hour progress review

At {now.isoformat()} we recorded CONTINUE. The completed mixed scalar
action/frame construction and the prescribed-frame global-negative
obstruction directly advance the main involution problem. The late
finite noncentral detection and independently verified frame reselection
identify the exact next difficulty, rather than settling it by a finite
shadow. The Birman/source work retains its actual comparison maps and
unresolved uniform condition. Both main decisions remain Open.
See records/progress_review_11h.md. The next scheduled review and
checkpoint are at12:49:30 UTC.
'''
p.write_text(s)
p = ROOT / 'records/continuation_state.md'
p.write_text(p.read_text() + f'''\n## Actual eleventh-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_11h.md.
All writers are paused for immutable capture. Release them immediately
after the ZIP is complete; independent verification and upload follow
without changing that archive. Both main full decisions remain Open.
Next checkpoint/review: 2026-11-16 12:49:30 UTC.
''')
print('Timed eleventh-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT / 'code/refresh_computation_inventory.py')], check=True)
with (ROOT / 'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(ROOT / 'code/preserve_checkpoint_versions.py')],
                   stdout=stream, check=True)
retention = json.loads((ROOT / 'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 10 and retention['archive_entries'] == 11193
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(ROOT / 'code/package_checkpoint.py'), '11'], check=True)
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
