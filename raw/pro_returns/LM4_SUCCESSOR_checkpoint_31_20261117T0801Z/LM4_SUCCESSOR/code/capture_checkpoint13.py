"""Capture checkpoint 13 at its hourly review after all writers have paused."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 16, 13, 49, 30, tzinfo=timezone.utc)
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_13.zip').exists()
remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the review.'
while remaining > 0:
    time.sleep(min(0.5, remaining))
    remaining = (deadline - datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
metrics = json.loads((ROOT / 'records/checkpoint13_metrics.json').read_text())
assert metrics['statements'] == 244 and metrics['task_rows'] == 49
assert metrics['statuses'] == {'Known': 6, 'Proved': 203, 'Refuted': 16, 'Open': 19}
assert metrics['bibliography_entries'] == 97 and metrics['pages'] == 309
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT / 'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == metrics['pdf_sha256']
qa = (ROOT / 'records/checkpoint13_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa

review = f'''# Thirteenth-hour progress review

Scheduled review:2026-11-16 13:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. We continue because the new
work changes the exact full-group problems, rather than extending
already passing affine tests or noncofinal towers. The complete hour
is documented in records/thirteenth_hour_research_report.md.

A79 proves a finite-action obstruction with every peripheral frame
allowed. Every full positive peripheral lift of the specified A64
action, fixing the literal cusp, has a negative image of exact order
four in an actual finite quotient. All iterated actual source-central
refinements nevertheless admit compatible involutory negative data.
The complete cocycle comparison and centralizer-surjectivity argument
remove the former frame restriction. Other finite actions, including
the later zero-cusp-inner-term choices, remain available. No full
parity-one involution or universal conjugacy decision is claimed.

B79 supplies a second complete actual presentation of the marginal
source problem: 23 fiber generators, all 26 critical lassos, 82 local
relation normal generators, and no retained base loops. The local
source boundary is different from the local central element. The
remaining condition is normalization of the whole source deletion
kernel by three specified retained directions. B80 refutes a proposed
general one-exceptional-tangency shortcut by an actual degree-eight
cover, with source and ambient kernel images C2 and V4. It does not
refute the fifth-root marginal, whose internal normal-generation
property supplies an additional hypothesis.

The reviewed product-one filling comparison localizes any marginal
failure to the original product-one filling kernel. A further actual
double-cover comparison now expresses the same kernel problem in
F7 semidirect F6, with four source meridians and six explicitly based
automorphisms. The geometry, complete collision list, inverse actions,
source-word marking and filling maps are recorded. This reduces the
whole-kernel normality question to a substantially smaller exact group.
Internal normality would suffice by LM4 F21, but it has not been proved.

The bounded finite-domain outcomes and their exact limitations are
recorded in the hour report and genuine solver outputs. An UNKNOWN
answer is never represented as an exclusion. The second encoding is
justified by the new exact smaller group, not by a larger degree census.
No additional nilpotent or scalar-affine test was run: existing proved
comparison results already cover those families. The pair-weight
acyclic-coefficient attempt on A has reached its stated finite scope
and stops; no conclusion beyond that scope is drawn. The alternate
full-profinite recognition route still lacks its module/tree step.

All 49 task/lead rows remain. The full product-closedness/fixed-complex
task B.4.c is correctly labelled Open; earlier proved finite-target
reductions remain Proved. Every old archive remains unchanged.

The final paper has {metrics['pages']} pages, 244 numbered statements:
203 Proved, 16 Refuted, 19 Open, 6 Known; 97 bibliography records.
PDF SHA256: {metrics['pdf_sha256']}.
The failed first TeX build and its exact source are retained. After
eleven missing display closers were repaired, the successful complete
build has zero overfull boxes, warnings, undefined references and errors.
We viewed all five contact sheets for 43 rendered pages and 12 critical
pages at full size. No further layout repair was required.

The next review and checkpoint are scheduled for14:49:30 UTC.
We resume substantive work immediately after immutable capture.
'''
(ROOT / 'records/progress_review_13h.md').write_text(review)
p = ROOT / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Thirteenth-hour progress review\n' not in s
s += f'''\n## Thirteenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. A79 excludes all frame
choices over one specified finite action. B79 gives the complete sum
pencil, and B80 refutes the proposed general one-tangency shortcut.
The reviewed product-one filling comparison and the smaller actual
F7 semidirect F6 model directly address the remaining full marginal
normality problem. Both main decisions remain Open. The exact review
is records/progress_review_13h.md; the full hour synthesis is
records/thirteenth_hour_research_report.md. The next scheduled review
and checkpoint are at14:49:30 UTC.
'''
p.write_text(s)
p = ROOT / 'records/continuation_state.md'
p.write_text(p.read_text() + f'''\n## Actual thirteenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_13h.md.
All writers are paused for immutable capture. Release them immediately
after the ZIP is complete; independent verification and upload follow
without changing that archive. Both main full decisions remain Open.
Next checkpoint/review:2026-11-16 14:49:30 UTC.
''')
print('Timed thirteenth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT / 'code/refresh_computation_inventory.py')], check=True)
with (ROOT / 'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(ROOT / 'code/preserve_checkpoint_versions.py')],
                   stdout=stream, check=True)
retention = json.loads((ROOT / 'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 12 and retention['archive_entries'] == 16647
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(ROOT / 'code/package_checkpoint.py'), '13'], check=True)
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
