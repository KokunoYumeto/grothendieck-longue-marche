"""Capture checkpoint18 at the hourly review after all writers have paused."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
deadline = datetime(2026, 11, 16, 18, 49, 30, tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_18.zip').exists()
remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60, 'Start only within one minute of the review.'
while remaining > 0:
    time.sleep(min(0.5, remaining))
    remaining = (deadline-datetime.now(timezone.utc)).total_seconds()
now = datetime.now(timezone.utc)
metrics = json.loads((ROOT/'records/checkpoint18_metrics.json').read_text())
assert metrics['statements'] == 265 and metrics['task_rows'] == 49
assert metrics['statuses'] == {'Known':6, 'Proved':223, 'Refuted':17, 'Open':19}
assert metrics['bibliography_entries'] == 105
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest() == metrics['pdf_sha256']
qa = (ROOT/'records/checkpoint18_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint18_writer_pause.md').exists()
computations = (ROOT/'records/checkpoint18_computation_audit_state.md').read_text()

review = f'''# Eighteenth-hour progress review

Scheduled review:2026-11-16 18:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. This hour removes the arbitrary
generic-fiber coefficient gate and the individual old-base transport gate
from the actual main B Alexander-layer comparison. It also proves exact
overlaps and replaces the remaining ambiguity by a specified orbit-sum
kernel. These are changes to the actual fixed-lifting problem, not a
further affine/metabelian finite-quotient census or detail away from it.
The complete research record is records/eighteenth_hour_research_report.md.

B93 computes the entire128-column seed/F-image module over Z[E]. Its
image is free of rank116 and kernel free of rank12. The exact algorithm
uses106 reversible unit pivots and ten private binomial rows, with a
finite-support proof of injectivity. The full F action is monomial, with
56 exchanged pairs and four negative fixed generators. Actual source
calibration gives exactly the four first-sheet source differences and
their entire F2[R] left ideal; H2 is zero. An induced common refinement
compares intrinsic anti-chains to B92 without identifying incompatible
relation kernels. All exact computations have independent full replay.

B94 incorporates every retained-fiber deck coefficient through the
actual generic-fiber quotient G. The64 nodal columns are free over Z[G].
An exact signed diagonal-unit augmented minor and a proved separated
augmentation filtration establish independence. No matrix inversion or
augmentation-one unit shortcut is used. The filtration proof handles
the full integral coefficient ring by finite2-group separation. The
Magnus1935 original source was opened at the relevant theorem and its
proof, with publisher metadata checked; the needed argument is included
in full. The literal node matching and its two cone classes determine
the whole H1 image as J4 and H2 as zero.

B95 determines the intersection with one actual old-zero translate.
All four augmented collisions have complete word and G-unit witnesses.
The intersection is free of rank4, the sum free of rank124; the overlap
has two exchanged F-pairs and no positive C2 cohomology. Therefore the
sum contributes exactly J4 plus its actual old-zero source image, all
inside J_I. Its60 additional columns show that the translated module
is not contained in the original. The Tate-target naturality is proved
using right defects, so no literal free-factor preservation is assumed.
This is one overlap, not an invariance or iteration assertion.

B96 proves a uniform result for every individual old-base translate.
The actual source double cover and its eleven returned operators reduce
all words to two cosets with the correct geometric-push order. The exact
odd representative exchanges the selected cone classes and supplies the
four second-sheet source differences, with positive push and pullback
related by the actual branch-square source operator. Thus every
individual translated module has four F2[R] H1 generators, H2 zero and
source-ideal image. The sum of all individual images is exactly J_I.
Their algebraic direct sum maps onto actual Lbar, and H2 of its kernel
has a canonical map with image U/J_I. This exact overlap kernel is not
identified with B92's differently marked relation kernel. The result
does not commute cohomology with a sum of submodules.

All four complete proofs passed root and independent reviews, and all
finite actual input calculations have independent checkers. The final
paper has{metrics['pages']} pages and265 statements:223 Proved,17 Refuted,
19 Open,6 Known;105 bibliography records with explicit verification
status; all49 task and lead rows. Main A remains at full marked
generation and the actual Fox-unit criterion. No new full involution,
conjugacy or icosahedral-centralizer decision is claimed.

The remaining main B gate is whole-overlap cohomology, equivalently the
specified residual orbit-sum map. The exact old-base augmented-row action
and its cocycle-section stabilizers are now written down, including the
opposite-operator convention. Four old generators have literally trivial
retained action, giving a structural reduction for stabilizer analysis.
An augmented collision alone does not prove full-column equality. A
whole-sum overlap theorem, or an actual source-coset obstruction, is still
needed. Nonlinear lifting, actual compact coefficient comparison,
projected fixed-source equality and the joint-source condition remain
separate requirements. Finite-depth or augmentation-adic stabilization
is not substituted for those statements.

The exact continuing computation state at immutable capture follows:

{computations}

The final PDF SHA256 is
{metrics['pdf_sha256']}.
The final log has zero overfull boxes, warnings, undefined references
and errors. The exact before/after counts, complete build directories,
rendered pages and visible inspection record are in
records/checkpoint18_typesetting.txt. Component attempts and their
repaired layout/format failures remain separately documented. Every
earlier archived byte is retained by the version-retention comparison.

All seventeen earlier checkpoint archives remain unchanged. The next
hourly review and checkpoint are scheduled for19:49:30 UTC. We resume
substantive research immediately after immutable capture.
'''
(ROOT/'records/progress_review_18h.md').write_text(review)
p = ROOT/'LM4_SUCCESSOR_report.md'
s = p.read_text()
assert '## Eighteenth-hour progress review\n' not in s
s += f'''\n## Eighteenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B93--B96 determine the full
seed module, every generic-fiber coefficient, one exact old-zero overlap
and every individual old-base translate. Their individual Tate images
sum exactly to J_I; the residual intrinsic excess is the image of H2 of
the actual orbit-sum kernel. This advances the main B fixed-lifting route.
All-word full-column stabilizers and whole-overlap cohomology remain
under study. Neither main full decision is closed. The nonlinear,
compact, projected-source and joint-source gates remain separate.
All49 task outcomes remain tracked. See records/progress_review_18h.md
and records/eighteenth_hour_research_report.md. Next review/checkpoint:
2026-11-16 19:49:30 UTC.
'''
p.write_text(s)
p = ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual eighteenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_18h.md.
Every writer is paused for immutable capture. Release writers as soon
as the ZIP is complete, then independently verify and save it without
altering that archive. Both main decisions remain Open.
Next review/checkpoint:2026-11-16 19:49:30 UTC.
''')
print('Timed eighteenth-hour review:', now.isoformat(), 'CONTINUE', flush=True)
subprocess.run([sys.executable, str(ROOT/'code/refresh_computation_inventory.py')], check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable, str(ROOT/'code/preserve_checkpoint_versions.py')],
                   stdout=stream, check=True)
retention = json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives'] == 17 and retention['archive_entries'] == 35161
assert retention['omissions'] == 0
subprocess.run([sys.executable, str(ROOT/'code/package_checkpoint.py'), '18'], check=True)
print('Immutable capture completed:', datetime.now(timezone.utc).isoformat(), flush=True)
