"""Capture checkpoint12 at its authorized hourly review, never off schedule.

Run within sixty seconds of the deadline after every writer has paused.
Earlier archives are read only. Packaging refuses an existing target.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 16, 12, 49, 30, tzinfo=timezone.utc)
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_12.zip').exists()
remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the review.'
while remaining > 0:
    time.sleep(min(0.5, remaining))
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
metrics = json.loads((ROOT / 'records/checkpoint12_metrics.json').read_text())
assert metrics['statements'] == 241 and metrics['task_rows'] == 49
assert metrics['statuses'] == {'Known': 6, 'Proved': 201, 'Refuted': 15, 'Open': 19}
assert metrics['bibliography_entries'] == 96
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == metrics['pdf_sha256']
qa = (ROOT / 'records/checkpoint12_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa

review = f'''# Twelfth-hour progress review

Scheduled review:2026-11-16 12:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. The current work continues to
attack their missing full-group implications. This hour gives a
finite noncentral obstruction with its exact frame scope, and a
complete actual based presentation of the marginal source problem.
The following algebraic work concerns that full presentation, not
another affine approximation to the original intersection.

For A, A77 proves the finite relation-module centralizer images and
detects A76's prescribed-frame negative-square obstruction in one
actual finite quotient. Every iterated scalar refinement still passes.
A78 retains the original finite action and changes its frame to pass
the six-cup gate, with independent original-law verification. This
prevents promoting A76 to an obstruction against all frames. The
actual involutory-action and cofinal-generation questions remain open.
A research proof also shows that every normalized negative companion
has square one on the entire characteristic metabelian quotient;
that whole quotient family therefore cannot decide full order.

For B, B76 refutes the broad relative special-fiber shortcut, including
its completed-image version. B77 identifies the four-triple partial
group exactly and separates a conjugated kernel element in S4. The
actual additional monodromies exclude that partial certificate. B78
computes all31 based20-strand lassos, including all29 filled values,
and gives the actual22-generator/620-listed-relation presentation.
The finite covers, literal source marking, and full-completion image
comparisons are proved. Equality of the actual closed deletion-kernel
images is exactly the remaining uniform b-normality condition.

Late research extracts eight retained half twists as explicit HNN
edge data, and rewrites the remaining filled relations in the source
generators. The edge subgroups remain proper and different; no
injectivity or normality is assumed after imposing the new relations.
A targeted zero-direction S4 tuple passes all29 original filled
relations but fails at depth one under the retained base1 action.
The exact translated special-node and fourth-triple relations are
now available and are being analyzed. This is direct full-presentation
work. The original joint-source gate remains separate even if the
marginal condition is solved.

Two further research results were completed after the final PDF was
frozen. The A working proof now obstructs every full normalized negative
involution inducing one specified old finite ACTION, even when all
peripheral frames may vary. Its actual ordinary sixteen-cup quotient,
complete cocycle comparison, centralizer-surjectivity argument, and
nonzero square have an independent full review and a fresh action-only
verification. This does not exclude other old actions and is retained
as research pending formal incorporation. The B sum pencil on the same
actual surface has all26 critical lassos computed, with exact collision
completeness and the common source-cluster marking checked. Its base is
the entire affine line. The local five-point variation center differs
from the actual source boundary product; the latter is recorded
literally. The remaining source-kernel normality question is Open.
All programs, genuine outputs, and working proofs are in this archive.

The bounded Grothendieck-pair literature audit has supplied no
counterexample satisfying all goodness and cohomological finiteness
hypotheses. Neither that search nor an invalid published argument
has been represented as a refutation of a published theorem.

The final paper has {metrics['pages']} pages,241 numbered statements,
201 Proved,15 Refuted,19 Open,6 Known,96 bibliography records and all
49 requested task rows. Its exact final PDF SHA256 is
{metrics['pdf_sha256']}.
Both complete builds have zero overflow, warning, undefined-reference
and error counts. Forty-two pages were rendered and visually reviewed,
with nine full-size critical pages. After one citation-spacing repair,
41 final page images are byte-identical to the reviewed images and
the changed final page108 was separately rechecked.

The next review and checkpoint are scheduled for13:49:30 UTC.
We resume substantive work immediately after immutable capture.
'''
(ROOT / 'records/progress_review_12h.md').write_text(review)
p = ROOT / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Twelfth-hour progress review\n' not in s
s += f'''\n## Twelfth-hour progress review

At {now.isoformat()} we recorded CONTINUE. A77-A78 resolve the exact
finite noncentral and frame-choice gates without deciding full
involution conjugacy. B76-B78 replace the invalid source shortcut
with a complete actual monodromy presentation and a precise uniform
normality condition. Work on its full transported relations continues.
Both main decisions remain Open. See records/progress_review_12h.md.
The next scheduled review and checkpoint are at13:49:30 UTC.
'''
p.write_text(s)
p = ROOT / 'records/continuation_state.md'
p.write_text(p.read_text() + f'''\n## Actual twelfth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_12h.md.
All writers are paused for immutable capture. Release them immediately
after the ZIP is complete; independent verification and upload follow
without changing that archive. Both main full decisions remain Open.
Next checkpoint/review:2026-11-16 13:49:30 UTC.
''')
print('Timed twelfth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT / 'code/refresh_computation_inventory.py')], check=True)
with (ROOT / 'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(ROOT / 'code/preserve_checkpoint_versions.py')],
                   stdout=stream, check=True)
retention = json.loads((ROOT / 'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 11 and retention['archive_entries'] == 13780
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(ROOT / 'code/package_checkpoint.py'), '12'], check=True)
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
