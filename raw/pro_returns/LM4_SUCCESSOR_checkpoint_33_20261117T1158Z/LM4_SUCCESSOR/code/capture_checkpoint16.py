"""Capture checkpoint16 at the hourly review after every writer has paused."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,16,49,30,tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_16.zip').exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the review.'
while remaining>0:
    time.sleep(min(0.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
metrics=json.loads((ROOT/'records/checkpoint16_metrics.json').read_text())
assert metrics['statements']==258 and metrics['task_rows']==49
assert metrics['statuses']=={'Known':6,'Proved':216,'Refuted':17,'Open':19}
assert metrics['bibliography_entries']==104
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==metrics['pdf_sha256']
qa=(ROOT/'records/checkpoint16_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint16_writer_pause.md').exists()

review=f'''# Sixteenth-hour progress review

Scheduled review:2026-11-16 16:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. We continue because this hour
proves new actual global comparisons on the main B route, including
the full compact comparison for the symmetric deletion kernels. It
also proves an exact source nonmembership that closes one candidate
extension negatively. These results change the remaining obstruction;
the work has not become a finite census or detail away from the main
question. The complete research record is
records/sixteenth_hour_research_report.md.

B84 integrates the all-five-positive controlled source theorem with
literal source corrections and a valid mixed-word stage argument.
Its actual filling quotients are Z times F5 and Z squared, also for
the specified compact images. B85 integrates the selected tangential
Galois action, whose relative-curve construction and literal b-loop
orientation were checked against the primary construction. Six actual
winding characters prove that the arithmetic source enlargement is
proper. They kill the full constant-family source kernel and therefore
do not separate its arithmetic kernel enlargement from that kernel.

B86 couples the diagonal with all four retained product directions.
Its quantified Schreier argument controls arbitrary mixed words, using
both deleted and retained all-powers strips. The signed global diagonal
character identifies the exact source intersection in that actual
block. Only the stated deleted normal-closure containment is asserted;
whole-source-kernel normality is not inferred.

B87 proves that the actual source is exactly the fixed subgroup on the
both-family filled surface, discretely and in full completion. Its
actual product bundle and index-two source cover give the required
splitting. A finite mod-two detector tracks the two cone classes and
excludes outside-cover fixed elements. Explicit characteristic finite
quotients prove the fiber topology before the full profinite
free-product centralizer theorem is applied. This is a completed
global comparison for the actual source, not a convenient quotient.

B88 refutes the specific membership of a inverse b inverse z b a in
the actual source, also after completion. Two actual based rational
maps agreeing on the source give an epimorphism onto the order64
product of two order-eight Heisenberg groups. The source maps exactly
to its diagonal; the specified word differs between the two coordinates
by a nonidentity central element. All32 possible central-coordinate
assignments were checked. Both rational maps factor through the filled
surface, so the finite detector kills the whole ambient filling kernel
and does not refute the desired source-kernel equality.

B89 identifies the actual symmetric deletion-kernel intersection with
the mutual commutator, discretely and compactly. The discrete proof
uses the actual open cover: both one-sided complements and the filled
surface are free-by-free bundles, and their union removes only finitely
many points from a smooth real four-manifold. Its second homotopy group
is zero. The exact Brown–Loday lemma applies without requiring the
symmetric intersection to be aspherical; the primary crossed-module
identification was opened and checked.

The compact step is proved separately. Every finite-kernel extension
of the actual finitely generated free-by-free head separates its kernel
in a finite quotient. In the central case the lifted-action discrepancy
is killed by a characteristic exponent-and-commutator subgroup; a
general finite kernel is reduced to its center by its finite-index
centralizer. This proves the full induced topology on the actual fiber
product. A separate finite-index-coset argument proves density in the
compact fiber product. Consequently the closed intersection is the
closed mutual commutator and the closure of the discrete intersection.
No arbitrary closure/intersection swap or profinite excision theorem
is assumed. Root and both independent reviewers passed the proof.

The symmetric geometry is exact: all64 mixed divisor intersections
are transverse and avoid the retained boundary, eight lie on the
source, and the new critical product values number18. Local source
meridians have fixed lifts at the eight fixed nodes. The remaining
global requirement is neutrality of the actual nonabelian involution
cocycles in the now identified commutator kernel, together with the
projected fixed-source comparison after the critical fillings. These
two requirements are not implied by the intersection calculation.
The subsequent joint-source condition also remains separate.

After the formal freeze, a separately checked research proof neutralizes
the first actual centralized-intersection obstruction. The integral module
M/[M,K_s] is the signed module on disjoint lifted-component pairs. The
actual inherited discrete internal normal-generation theorem excludes all
singleton signed orbits, so its first C2 cohomology vanishes. Every fixed
target therefore lifts through Gamma/[M,K_s]. B87/B89 and compact density
give the corresponding actual completed fixed-lift statement without an
unproved identification of the entire completed coefficient module. Root
and both parallel reviewers checked the complete proof. It remains research
for the next formal cycle; the frozen register stays at258 statements.
The full nonabelian lift through M and projected fixed-source gate remain
Open. An independently checked finite perfect-kernel example shows why
an abstract extrapolation from the first layer would be invalid; it is
not asserted to be a quotient of the actual surface.

Two auxiliary countermodels prevent unrelated shortcuts: maximal
transverse intersections do not imply relative product injectivity,
and a general linear reflection with invariant retained line boundary
does not by itself prove source-kernel equality. Neither countermodel
is substituted for the actual mu5 arrangement. The source's eta-fiber
boundary degeneration and the old zero-operator limitation remain
recorded with their exact equations.

Main A remains at full marked generation and the actual Fox-unit
criterion. No new full involution or universal conjugacy theorem is
claimed. All49 task and lead rows remain. The frozen paper has
{metrics['pages']} pages and258 numbered statements:216 Proved,
17 Refuted,19 Open,6 Known;104 bibliography entries, all with explicit
verification status. Its final build has zero overfull boxes, warnings,
undefined references and errors. Final PDF SHA256:
{metrics['pdf_sha256']}.
The exact rendered and visibly inspected page lists are recorded in
records/checkpoint16_typesetting.txt. Earlier successful builds and
component diagnostics remain distinguishable.

All fifteen earlier archives remain unchanged, with every earlier
archived byte retained in the new package. The next hourly review
and checkpoint are scheduled for17:49:30 UTC. We resume substantive
research immediately after immutable capture.
'''
(ROOT/'records/progress_review_16h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Sixteenth-hour progress review\n' not in s
s+=f'''\n## Sixteenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B84–B86 extend actual
controlled kernels and specify the exact arithmetic-source scope.
B87 identifies the filled-surface source with the full fixed subgroup,
including in full completion. B88 refutes one exact zero-source-word
membership by an actual order64 quotient. B89 proves the actual
symmetric kernel intersection is the mutual commutator and proves
its full compact comparison by finite-extension and topology arguments.
The remaining fixed-lift cocycles and projected fixed-source comparison
are explicit; their neutrality or source equality is not inferred.
Both main decisions and the later joint-source condition remain Open.
See records/progress_review_16h.md and
records/sixteenth_hour_research_report.md. Next review/checkpoint:
2026-11-16 17:49:30 UTC.
'''
p.write_text(s)
p=ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual sixteenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_16h.md.
Every writer is paused for immutable capture. Release writers as soon
as the ZIP is complete, then independently verify and save it without
altering that archive. Both main decisions remain Open.
Next review/checkpoint:2026-11-16 17:49:30 UTC.
''')
print('Timed sixteenth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],
                   stdout=stream,check=True)
retention=json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==15 and retention['archive_entries']==26827
assert retention['omissions']==0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'16'],check=True)
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
