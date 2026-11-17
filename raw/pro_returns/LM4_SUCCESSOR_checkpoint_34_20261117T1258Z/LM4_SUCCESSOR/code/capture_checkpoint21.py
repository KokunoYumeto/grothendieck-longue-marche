"""Capture checkpoint21 only after its timed hourly review and writer pause."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib,json,subprocess,sys,time

ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,21,49,30,tzinfo=timezone.utc)
archive=ROOT.parent/'LM4_SUCCESSOR_checkpoint_21.zip'
assert not archive.exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the timed review.'
while remaining>0:
    time.sleep(min(0.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
m=json.loads((ROOT/'records/checkpoint21_metrics.json').read_text())
assert m['statements']==276 and m['pages']==408 and m['task_rows']==49
assert m['statuses']=={'Known':6,'Proved':232,'Refuted':19,'Open':19}
assert m['bibliography_entries']==108
assert not m['overfull'] and not m['warnings'] and not m['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==m['pdf_sha256']
qa=(ROOT/'records/checkpoint21_typesetting.txt').read_text()
assert m['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint21_writer_pause.md').exists()
assert (ROOT/'records/checkpoint21_root_formal_reviews.json').exists()
computations=(ROOT/'records/checkpoint21_computation_audit_state.md').read_text()
review=f'''# Twenty-first-hour progress review

Scheduled review: 2026-11-16 21:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

Both main full decisions remain Open. This hour proves an actual
critical-filling comparison across an entire region of the main-B
surface, including nine physical critical base values. It also gives
an exact finite-cover equivalence for the global selected fixed-source
question and an actual one-neck amalgam with a detected common subgroup.
These change the main obstruction problem; they are not further affine,
metabelian, finite-group or finite-depth orbit tests. The full research
record is records/twenty_first_hour_research_report.md.

B106 identifies the actual free coordinate-swap quotient. Its projective
fiber coordinate turns the literal selected involution into t to -t.
Every deleted divisor, projective pole and the actual base point is
retained. The two fixed sources each have ten punctures; the selected
one has the actual nineteen-punctured source as a connected double
cover. The selected fixed-source equality is equivalent on these full
surfaces, discretely and in full profinite completion. The proof uses
finite-index topology and a two-coset argument, with no assumed source
injection. Exact collision factorizations and a separate rational
cyclotomic replay locate all eighteen physical critical base values,
nine in each region and sixteen quotient nodes in each.

B107 treats the whole punctured inner disk, with every actual critical
fiber inserted. The exact inverse-Blaschke norm identity separates all
moving punctures from the selected cone. A concrete collar shrinks
both with the base and toward the two retained punctures. Orbifold
van Kampen gives (C2 times Z) amalgam_Z R with an actual boundary
section and retraction, so its edge injections are proved. Retraction-
stable finite normal subgroups are cofinal. Every finite quotient
factors through (C2*K_N) semidirect D_N, and the reopened full-category
Herfort--Ribes centralizer theorem determines its cone centralizer.
Compatible coordinates prove the full completed equality, without
residual finiteness or asphericity of the unknown vertex group.
The exact local fixed-source equality transfers to the selected
component in the original double cover. The two components over this
restricted source are kept distinct. The outer mirror isolates the
other cone and its F-sigma lift, not the selected original F-source.

Both complete formal proofs passed root and independent reviews; the
completion argument has a separate full review. The genuine rational
checks have independent replays, including all twenty collision root
candidates and their two exact coincidences. The two failed initial
symbolic attempts, editing diagnostics and subsequent successful
outputs are retained. The final paper has {m['pages']} pages and
276 statements: 232 Proved, 19 Refuted, 19 Open and 6 Known. All 49
task/lead rows and 108 verified-status bibliography entries remain.

The final PDF log has zero overfull boxes, warnings, undefined
references and errors. Both complete builds have overfull counts 0/0,
including beyond 2pt. A cosmetic citation-spacing repair is documented.
We inspected four contact sheets for 35 rendered pages and eight
critical pages individually. Byte-identical final renderings justify
the explicitly listed inherited views; the repaired page and contact
sheet were displayed anew. All earlier draft bytes and renderings
remain retained. Exact QA is records/checkpoint21_typesetting.txt.

The subsequent global research does not assume the regional boundary
fiber maps inject. On the first unit-circle neck, a common five-puncture
disk lifts to exactly four A punctures and a branch puncture. The
ordinary one-family F7 bundle detects its F5 as a free factor with
full induced topology. Because filling B is not equivariant, the
detector is used only on the ordinary index-two subgroup, followed
by a finite-index core. A simply connected cut-base with this one
neck has a genuine discrete amalgam over F5. Its bad-vertex centralizer,
other necks and profinite amalgam comparison remain separate gates.

An unrestricted annular disk can realize any prescribed lift choices,
but common point pushes supported on the two actual sides have zero
cover character: the retained puncture forces their two windings to
agree on one side and one winding to vanish on the other. Thus that
simple all-neck extension fails. The latest actual mixed-neck
vanishing-arc work and its precise verification state are retained
below; no incidence-only RAAG or global normal-closure claim is made.

Main A's focused extra-section test is now known to be blind. The
actual canonical image already has exactly the three ambient section
classes, its coset space has the unique selected fixed point, and
its reduced dyadic coset module is Tate-acyclic. The complete proof
has independent review. Neither result makes that module zero or
proves the canonical Fox element a unit. The full marked generation
and third-cusp questions remain Open. No further realization census
was substituted for them.

The exact countable product-tree subcomplex theorem also passed full
reviews, but remains a criterion: the actual nodal complex cannot
be homotopy equivalent to a graph because B105 supplies nonzero H2.
An actual group-level comparison must retain redundant relations.

All entries of the twenty earlier checkpoints are preserved with
their exact bytes and zero omissions. Verification images use the
same standard nested TAR and standard hard links introduced in20;
every original logical path remains individually digest-verified.
All mathematical sources, PDFs, code, data, logs and reports are
retained. No earlier archive is overwritten or renamed.

Exact computation and late-proof state at immutable capture:

{computations}

Final PDF SHA-256: {m['pdf_sha256']}.
Next hourly review/checkpoint: 2026-11-16 22:49:30 UTC.
Resume substantive work as soon as immutable capture completes.
'''
(ROOT/'records/progress_review_21h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md';s=p.read_text()
assert '## Twenty-first-hour progress review\n' not in s
s+=f'''\n## Twenty-first-hour progress review

At {now.isoformat()} we recorded CONTINUE. B106--B107 prove the
actual free-quotient equivalence and the selected fixed-source
comparison across all inner critical fibers, including full profinite
completion. Subsequent one-neck geometry detects a genuine common
subgroup and isolates the remaining mixed-neck marking problem.
The global fixed-source, joint-source and Main A full marked-generation
decisions remain Open. All 49 task rows are retained. Complete records:
records/progress_review_21h.md and records/twenty_first_hour_research_report.md.
Next review/checkpoint: 2026-11-16 22:49:30 UTC.
'''
p.write_text(s)
p=ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual twenty-first-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_21h.md.
All writers are paused for immutable capture. Release immediately
after the ZIP completes, then independently verify and save it.
Both main full decisions remain Open. No checkpoint21 archive byte
may change after capture. The final formal baseline is276 statements,
408 pages, with clean final QA. New mixed-neck research remains in
its exact reviewed scope. Next review/checkpoint:
2026-11-16 22:49:30 UTC.
''')
print('Timed twenty-first-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],stdout=stream,check=True)
retention=json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==20 and retention['archive_entries']==50301
assert retention['omissions']==0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'21'],check=True)
assert archive.stat().st_size<=536870912,'Never mutate an already captured archive.'
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
