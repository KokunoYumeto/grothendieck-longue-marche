"""Capture checkpoint17 at the hourly review after all writers have paused."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 16, 17, 49, 30, tzinfo=timezone.utc)
assert not (ROOT.parent / 'LM4_SUCCESSOR_checkpoint_17.zip').exists()
remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the review.'
while remaining > 0:
    time.sleep(min(0.5, remaining))
    remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
metrics = json.loads((ROOT/'records/checkpoint17_metrics.json').read_text())
assert metrics['statements'] == 261 and metrics['task_rows'] == 49
assert metrics['statuses'] == {'Known':6, 'Proved':219, 'Refuted':17, 'Open':19}
assert metrics['bibliography_entries'] == 104
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == metrics['pdf_sha256']
qa = (ROOT/'records/checkpoint17_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint17_writer_pause.md').exists()
computations = (ROOT/'records/checkpoint17_computation_audit_state.md').read_text()

review = f'''# Seventeenth-hour progress review

Scheduled review:2026-11-16 17:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. We continue because this hour
proves three actual comparisons on the main B route and supplies the
first completely marked node/operator inputs for their remaining
obstruction. These are changes to the actual source-kernel and fixed-lift
problem, not a census of more finite quotients or detail away from it.
The full research record is records/seventeenth_hour_research_report.md.

B90 computes the actual integral first relative-centralization module
M/[M,K_s]. Its basis consists of disjoint lifted divisor-component pairs,
with negative interchange. The inherited discrete internal-normal-
generation theorem is transferred through the actual marginal and cover
maps, and forces every lifted A component to meet the selected fixed
source. Therefore no singleton sign orbit survives, and its first C2
cohomology is zero. Fixed targets lift in Gamma/[M,K_s]. A separate compact
density argument proves the corresponding actual compact fixed-lift
surjectivity, without an unproved completed coefficient identification.
Neither nonlinear fixed lifting nor projected-source equality follows.

B91 gives the full discrete intersection Alexander module P/Lbar, where
P is the tensor of the two actual free-group augmentation ideals. Its
covering-local van Kampen proof retains both transported meridians of
every actual node and all old-fiber deck translates, then exhausts the
universal base. The product of Cayley trees gives each exact Fox column
as a unique finite two-chain. The action is literal negative swap in a
proved paired basis. H1(C2,P) is the augmentation ideal over F2[R], and
H2(C2,P)=0. The right-defect convention gives the exact criterion that
r inverse minus1 belong to the actual relation-image submodule U.
The source left ideal J_I is contained in U; equality is not assumed.

B92 proves that the free-node contribution is exactly J_I and isolates
every remaining contribution through a canonical R-linear syzygy map
kappa:H2(C2,Z2) to the augmentation submodule of F2[R/I]. Its image is
U/J_I. Actual equivariant finite-family transports, a complete critical-
value tree, and the nearby z^2-t^2 local model retain all based whiskers.
The source meridians generate I as a subgroup. A direct commutator
expansion shows that each fixed-node column differs from its actual
source rectangle by a coboundary. The exact lift test is membership of
r inverse I minus I in image(kappa). Vanishing is sufficient for the
projected source equality at this discrete layer, but neither proved
nor asserted necessary. The nonlinear kernel [M,M] and full compact
comparison remain separate unresolved gates.

All three formal proofs were read completely by root and both parallel
reviewers. Their component builds and pages were checked before combined
integration. The final paper has{metrics['pages']} pages and261 statements:
219 Proved,17 Refuted,19 Open,6 Known;104 bibliography entries, each with
explicit verification status. All49 task and lead rows remain. Main A
is still at full marked generation and the actual Fox-unit criterion;
no new full involution or conjugacy decision is claimed.

The new finite computation exposed and repaired an actual convention
failure. A stronger based involution check rejected the initial
transport arrays. Exact one- and two-half-twist geometry proved the
chronological push/pull correction, and the arrays were regenerated
from the unchanged certified crossing paths. Independent all-generator
checks now pass. The original failure, source arrays and outputs remain
preserved and explicitly superseded. A bounded retrospective audit
proved that B81--B86 used a consistent intrinsic Birman marking already;
its full groupoid, local-prefix, source-action and orientation checks
pass, so no accepted earlier word or winding assertion is changed.

The detailed computation state at immutable capture follows verbatim.
It distinguishes completed exact inputs from any continuing research:

{computations}

The final PDF SHA256 is
{metrics['pdf_sha256']}.
Its build has zero overfull boxes, warnings, undefined references and
errors. The initial combined B90/B91 display overflowed19.57776pt; we
viewed that page, split the display, and rebuilt with zero overflow.
The final B92 integration is also clean. Before/after overfull counts
are1/0, including beyond2pt. We viewed all five contact sheets for40
rendered final pages and14 critical pages individually, including every
new proof page and the repaired display. Exact logs and page lists are
in records/checkpoint17_typesetting.txt. The overflowing diagnostic
preview is excluded as transient; its source, logs, metrics and image
remain. Every earlier archived byte is retained.

All sixteen earlier checkpoint archives remain unchanged. The next
hourly review and checkpoint are scheduled for18:49:30 UTC. We resume
substantive research immediately after immutable capture.
'''
(ROOT/'records/progress_review_17h.md').write_text(review)
p = ROOT/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Seventeenth-hour progress review\n' not in s
s += f'''\n## Seventeenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B90 proves actual fixed
lifting at the first relative centralization, including its compact
comparison. B91 retains the full discrete transported intersection
module and right-defect Tate criterion. B92 identifies the exact source
left-ideal contribution and isolates the residual source-coset syzygy
map. Its value, nonlinear lifting, projected-source equality and the
later joint-source condition remain Open. The actual node/operator
computation now retains all based conventions, a repaired transport
failure, and the completed retrospective Birman audit. Both main full
decisions and all49 task outcomes remain explicitly tracked. See
records/progress_review_17h.md and
records/seventeenth_hour_research_report.md. Next review/checkpoint:
2026-11-16 18:49:30 UTC.
'''
p.write_text(s)
p = ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual seventeenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_17h.md.
Every writer is paused for immutable capture. Release writers as soon
as the ZIP is complete, then independently verify and save it without
altering that archive. Both main decisions remain Open.
Next review/checkpoint:2026-11-16 18:49:30 UTC.
''')
print('Timed seventeenth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT/'code/refresh_computation_inventory.py')], check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(ROOT/'code/preserve_checkpoint_versions.py')],
                   stdout=stream, check=True)
retention = json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 16 and retention['archive_entries'] == 30798
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(ROOT/'code/package_checkpoint.py'), '17'], check=True)
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
