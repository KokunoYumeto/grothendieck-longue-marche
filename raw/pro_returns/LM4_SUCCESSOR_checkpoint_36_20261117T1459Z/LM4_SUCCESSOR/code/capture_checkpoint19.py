"""Capture the nineteenth hourly checkpoint only after review and writer pause."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,19,49,30,tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_19.zip').exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60, 'Start only within one minute of the review.'
while remaining>0:
    time.sleep(min(0.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
metrics=json.loads((ROOT/'records/checkpoint19_metrics.json').read_text())
assert metrics['statements']==269 and metrics['task_rows']==49
assert metrics['statuses']=={'Known':6,'Proved':225,'Refuted':19,'Open':19}
assert metrics['bibliography_entries']==108
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==metrics['pdf_sha256']
qa=(ROOT/'records/checkpoint19_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint19_writer_pause.md').exists()
computations=(ROOT/'records/checkpoint19_computation_audit_state.md').read_text()

review=f'''# Nineteenth-hour progress review

Scheduled review:2026-11-16 19:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. This hour determines an actual
all-word augmented-row stabilizer for the main B relation problem and
refutes two specific proposed shortcuts by complete counterexamples.
These change the unresolved fixed-lifting route; they are not a further
affine/metabelian census or detail detached from the main question.
The exact two-sheet relation block is also now established over the
full coefficient ring. The complete report of this hour is retained in
records/nineteenth_hour_research_report.md.

B97 proves that the two actual source-sheet modules form a free
rank128 direct sum over Z[G]. It supplies a general augmentation-row
parity argument, while explicitly proving that this parity does not
grade the complete columns. The separated integral augmentation
filtration proves independence without inverting a matrix. Its full
positive involution cohomology has eight actual source generators and
zero H2. Its returned-source orbit generates all Lbar, and the sum of
the individual cohomology images is exactly J_I. Whole overlaps remain
a different question from this direct two-block calculation.

B98 gives an explicit beta-twisted embedding G into F13 times F13 and
a complete bi-order/domain proof. The proposed implication from an
unchanged augmented row to a full group-unit column relation is false
on actual old-zeta/node(16,1) data. Its full592-letter relator image
has553 coefficient terms and a specified nonzero coefficient in a
new row; independent opposite-edge reconstruction verifies every term
and the printed factored witness. All16 tested zero-head pairs are
independent over the entire integral coefficient ring. The exact
two-column cohomology has source image only, without any conclusion
about full64-column block intersections. The Kim--Rolfsen2003 source
was read at its full order proof; the particular embedding and domain
argument required here are included in full.

B99 determines the full selected constant-section head kernel and
augmented diagonal-row stabilizer, with no word length cutoff. After
the actual four q-root fibers are filled, projecting X0 to v leaves
one allowed finite collision at v=-1. The extending far section kills
exactly its base meridian, and the generic F4 kernel is the normal
closure of the actual commutator[c,d] under two explicit automorphisms
and their inverses. The old six-generator map is literally(b,d,1,a,1,c).
Its pullback is precisely the desired head kernel and row stabilizer.
The17 exact path segments, both operators, all inverse/boundary
identities, algebraic-base margins and common source connector have
independent checks. The proof never assumes postfilling fiber
injectivity or identifies the unfilled injective section with the
filled kernel. The full-column action is still distinct and unresolved.

B100 proves that the actual symmetric complement Z is not aspherical.
The two literal node meridians p2 and p12 p13 p12 inverse commute,
and the actual old0 far lift fixes both. Three explicit global regular
units have winding matrix I3, exhibiting a split Z3 subgroup of
pi1(Z). The complement is a closed smooth affine surface after the
explicit embedding sD(v,w)=1 in C3. Milnor1963 Theorems7.1--7.2
and their full proof were opened and read in text and in the actual
rendered scan. They give a two-dimensional CW model. Any map of the
torus2-skeleton using the three loops and commutator disks has a
nonzero remaining attaching sphere: an extension would induce degree
one on torusH3 through the zero group H3(Z). The sphere has infinite
order. Hatcher2002 Proposition4.1 and Theorem4.32 were opened at the
complete proofs; the resulting universal2CW chain calculation also
proves nonzero H2 with F2 coefficients. Thus even mod2 acyclicity of
the universal cover is false. None of these geometric classes is
silently identified with B92's particular syzygy kernel or with a
nonzero value of kappa. The aspherical bundles X,Y,V remain unaffected.

All four complete proofs passed root and independent reviews. The
actual computed inputs have separate independent checkers and retain
their full words, coefficient arrays, path data, hashes and outputs.
Earlier failed paths and the interrupted giant expansion remain
documented. The final paper has{metrics['pages']} pages and269 statements:
225 Proved,19 Refuted,19 Open,6 Known. It has108 bibliography records
with explicit verification status and all49 task and lead rows.

Main A remains at full marked generation and the actual Fox-unit gate.
Its finite graph-of-finite-groups realization route was checked against
the earlier exact source audit: available hypotheses do not supply
the required arbitrary full profinite realization or marked inertia
transfer. This is not reopened as an assertion from an abstract or
pro-p theorem.

The next main B work uses the exact geometric stabilizer presentation
to control full transported columns and whole source-orbit sums.
The actual equivariant2-complex/E-cover comparison and all eight head
stabilizers have now passed independent review as late research, retained
separately from the269-row formal build. A complete root-path integral
basis computes the large geometric stabilizer column and refutes its
signed-G-unit monomiality. Ordinary Brown--Loday calculations forget the E action;
Smith/Tate comparisons cannot discard the actual H2 or infer vanishing
from fixed-locus dimension. The remaining obstruction U/J_I, nonlinear
fixed lifting, compact coefficient comparison, projected fixed-source
equality and subsequent joint-source condition remain separate gates.

The exact computation state at immutable capture follows:

{computations}

Final PDF SHA256:
{metrics['pdf_sha256']}.
The final log has zero overfull boxes, warnings, undefined references
and errors. Before/after layout counts, all build passes and the actual
visible page inspections are recorded in records/checkpoint19_typesetting.txt.
All eighteen earlier archives remain unchanged. Every earlier archived
entry is retained byte-exactly by the version-retention comparison.
Next hourly review/checkpoint:2026-11-16 20:49:30 UTC. We resume the
substantive work after immutable capture.
'''
(ROOT/'records/progress_review_19h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Nineteenth-hour progress review\n' not in s
s+=f'''\n## Nineteenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. B97--B100 prove the exact
two-sheet coefficient block and selected all-word stabilizer, refute an
actual augmented-column shortcut, and prove that the actual symmetric
surface has a Z3 retract and nonzero second homotopy. Its universal
cover is not even mod2 acyclic. These settle intermediate gates of the
actual main B fixed-lifting route while retaining its unresolved full
column, whole-overlap, nonlinear, compact and joint-source questions.
Both main full decisions remain Open. All49 task rows remain tracked.
The exact review and research records are records/progress_review_19h.md
and records/nineteenth_hour_research_report.md. Next review/checkpoint:
2026-11-16 20:49:30 UTC.
'''
p.write_text(s)
p=ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual nineteenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_19h.md.
All writers are paused for immutable capture. Release them as soon as
the ZIP is complete, then independently verify and save that archive.
Both main full decisions remain Open. No checkpoint19 bytes may change
after capture. Next review/checkpoint:2026-11-16 20:49:30 UTC.
''')
print('Timed nineteenth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention=json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==18 and retention['archive_entries']==39895
assert retention['omissions']==0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'19'],check=True)
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
