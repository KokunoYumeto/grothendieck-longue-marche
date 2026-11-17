"""Capture checkpoint14 at its hourly review after every writer has paused."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,14,49,30,tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_14.zip').exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the review.'
while remaining>0:
    time.sleep(min(0.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
metrics=json.loads((ROOT/'records/checkpoint14_metrics.json').read_text())
assert metrics['statements']==247 and metrics['task_rows']==49
assert metrics['statuses']=={'Known':6,'Proved':206,'Refuted':16,'Open':19}
assert metrics['bibliography_entries']==99 and metrics['pages']==320
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==metrics['pdf_sha256']
qa=(ROOT/'records/checkpoint14_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa

review=f'''# Fourteenth-hour progress review

Scheduled review:2026-11-16 14:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. We continue because A80-A81
remove an actual remaining normalization and ordinary-realization
restriction from the finite-action obstruction, and B81 plus the
ordered-family work change the exact whole-source normality problem.
This is not another passing scalar tower or a finite-group census.
The complete hour is documented in
records/fourteenth_hour_research_report.md.

A80 constructs involutions on actual odd relation-module quotients
and proves the cusp-centralizer detector needed to exclude full
negative involutions with arbitrary cusp and frame choices. A81
further constructs such actions at infinitely many eligible fresh
primes which pass their actual first source-central refinement and
admit ordinary full positive lifts. No full negative involution
induces those finite actions. The proof identifies the actual
p-central model, removes the exact cusp discrepancy through compact
anti-symplectic homology, matches every other central prime, and
applies the ordinary full lifting criterion. Twelve exact symbolic
identities independently verify the new class-two algebra. No
numerical fresh prime or giant coefficient matrix is claimed.
All-iterated central compatibility is not asserted for this new
family; A79 retains that separate assertion for its earlier action.
The surviving W=0 actions and universal conjugacy decisions stay Open.
After the formal freeze, a complete independently reviewed argument
also closes the actual dyadic augmentation-module gap: prescribed
involution classes give all finite-coefficient H1 restriction
surjectivity, and the actual R2 is free of rank two over Z2[[E]].
The exact primary input and auxiliary cover were opened and checked.
This proof is retained as research in14, with formal integration
reserved for the next cycle. It does not construct the missing
finite tree or marked reflection generators.

B81 proves an actual covering comparison to F7 semidirect F6 and
full filling-kernel intersections in two rank-five free factors and
two tangency rank-two factors, discretely and after completion. All
based actions, inverse actions, source words, and whole-strip
certificates are retained and independently checked. No normality
of the entire source image is inferred from those intersections.

The proposed restricted moving-family orbit equality is false:
a verified order-eight quotient detects a missing ordered-fiber
direction. That separator does not survive the actual omitted
even-source action alpha1 squared. The full partial-source kernel
has eleven even base actions and four literal opposite-family
source inner actions, now retained in its exact operator description.
The alternate ordered projection also records the correct ordinary
triple/node collision types. These are concrete corrections to the
remaining full-source problem, not a claimed centralizer decision.
The marginal whole-kernel gate and later joint-source gate stay Open.

All49 task/lead rows remain. The paper has {metrics['pages']} pages,
247 numbered statements:206 Proved,16 Refuted,19 Open,6 Known;
99 bibliography records, each with an explicit verification status.
Two older notes were given their missing literal verified labels,
using their already retained direct-reading records. No mathematical
statement changed in that final bibliography pass. A bibliography-only
entry-spacing adjustment removed the two-line final page; all311
pre-bibliography pages retain identical text and the reviewed proof
renderings are unchanged. The final build
has zero overfull boxes, warnings, undefined references, and errors.
Final PDF SHA256:{metrics['pdf_sha256']}.
The completed visual review and exact page list are recorded in
records/checkpoint14_typesetting.txt.

Every earlier archive remains unchanged. The next progress review
and checkpoint are scheduled for15:49:30 UTC. We resume substantive
work immediately after immutable capture.
'''
(ROOT/'records/progress_review_14h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Fourteenth-hour progress review\n' not in s
s+=f'''\n## Fourteenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. A80-A81 give an actual
finite-action obstruction independent of all full cusp and frame
choices, while separately proving first-central compatibility and
ordinary full positive realization. B81 gives the exact smaller
bundle and whole filling-kernel intersections. The restricted
ordered-family separator is correctly limited and is destroyed by
an actual full-source action; all missing source operators are now
retained. Both main decisions remain Open. See
records/progress_review_14h.md and
records/fourteenth_hour_research_report.md. The next review and
checkpoint are at15:49:30 UTC.
'''
p.write_text(s)
p=ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual fourteenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_14h.md.
Every writer is paused for immutable capture. Release writers as
soon as the ZIP is complete. Independent verification and saving
then proceed without altering that archive. Both main full decisions
remain Open. Next review/checkpoint:2026-11-16 15:49:30 UTC.
''')
print('Timed fourteenth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],
                   stdout=stream,check=True)
retention=json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==13 and retention['archive_entries']==19727
assert retention['omissions']==0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'14'],check=True)
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
