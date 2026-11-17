"""Capture checkpoint15 at its hourly review after every writer has paused."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,15,49,30,tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_15.zip').exists()
remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Start only within one minute of the review.'
while remaining>0:
    time.sleep(min(0.5,remaining))
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
now=datetime.now(timezone.utc)
metrics=json.loads((ROOT/'records/checkpoint15_metrics.json').read_text())
assert metrics['statements']==252 and metrics['task_rows']==49
assert metrics['statuses']=={'Known':6,'Proved':211,'Refuted':16,'Open':19}
assert metrics['bibliography_entries']==101
assert not metrics['overfull'] and not metrics['warnings'] and not metrics['errors']
assert hashlib.sha256((ROOT/'LM4_SUCCESSOR_paper.pdf').read_bytes()).hexdigest()==metrics['pdf_sha256']
qa=(ROOT/'records/checkpoint15_typesetting.txt').read_text()
assert metrics['pdf_sha256'] in qa and 'Visual review: PASS' in qa
assert (ROOT/'records/checkpoint15_writer_pause.md').exists()

review=f'''# Fifteenth-hour progress review

Scheduled review:2026-11-16 15:49:30 UTC.
Actual review record:{now.isoformat()}.
Decision:CONTINUE.

Both main full decisions remain Open. We continue because this hour
closes actual module-theoretic gaps in A and proves whole filling-kernel
equalities on a larger actual subgroup in B, with a valid mixed-word
induction and explicit compact detectors. These results change the
remaining main gates; they are not another passing finite census or
an unbounded list of local seed checks. The full record is
records/fifteenth_hour_research_report.md.

A82 proves the actual reflection augmentation module projective over
every Zp[[E]] and free over the full dyadic ring, of rank two for pure
pants and rank one for regular pants. The finite-coefficient embedding
argument preserves the required involution classes. Its induction
counit is split by projectivity; no invalid dyadic sign decomposition
is used. A83 proves the actual odd-head orientation-twisted G0 identity.
A84 upgrades it to an isomorphism even at modular finite heads and to
projective duality over the full completed group ring, at every prime.
The proof uses the opened Cartan-injectivity argument, descent to the
actual finite coefficient field, finite projective lifting and one
compatible compact system. Both independent reviews passed.

These are statements about the actual modules. They do not make the
selected incidence map surjective or rule out nonselfdual multiplicity
imbalances. The canonical full Fox-unit criterion and its twisted-fixed
equation were checked but do not produce the missing inverse. The main
involution classification is not settled by module freeness or duality.
Once that route stalled, the available source-audit effort moved to B.

B82 retains all actual ordered partial-source operators and proves
complete filling-kernel intersections in the specified rank-eight and
rank-nine free-factor settings. Its limitations on whole-subgroup
normality, including the D-squared direction, are explicit.

The actual w-pencil is now checked with true cyclotomic coefficients,
all24 based local models, all121 path segments, and whole twelve-generator
action and inverse-basis comparisons. Its global w=1 action retains the
full local cluster twist and every exterior node factor. In B83, the
two constant-family strips and three specified old source lifts yield
an actual subgroup enlarged by the product-one meridian. The corrected
stage induction controls every mixed word in that subgroup. Its two
whole filling kernels equal the selected source-kernel images, with
quotients Z times F3 and Z squared. The base projection and winding
of(vw-1)/(w-1)^2, together with winding(w-1) for the second filling,
factor through the actual target surfaces and detect those quotients.
The same argument proves the actual closed-image assertions in full
completions without assuming the induced full topology on the subgroup.
Root and the independent reviewer both passed the complete proof.

We rejected a proposed relaxation of the stage argument. The omitted
middle conjugation makes that proposed induction circular. An exact
free-group example and a verified order384 quotient refute the abstract
relaxation, including its compact version. No accepted theorem uses it.
B82 and B83 use the stronger valid earlier-stage hypothesis.

After the formal cutoff, two further complete research proofs passed
independent review. Exact source corrections extend the controlled
kernel to all five positive base operators and all four deleted Nielsen
seeds, with quotient Z times F5 and the same both-family Z squared
quotient. The abstract F9 used for those selected source words is not
assumed to embed as a free factor of the full source. Separately, an
explicit rational chart with F(0,q)=250 permits the exact relative
tangential construction of a selected Galois action preserving all
actual source-kernel images and acting cyclotomically on the literal
product-one meridian. The precise Deligne construction was opened by
all reviewers. These research proofs are retained for next-cycle formal
integration, without changing the252-row frozen paper.

An actual cross-ratio map also proves that the zero-base direction
cannot satisfy the current sufficient stage criterion, even after
source corrections that retain its zero winding. This bounds that
method; it does not refute whole-kernel normality. The next work must
couple retained directions or use a different actual geometric
comparison. The corrected diagonal-triple source operators supply
an active route toward those missing directions.

The other source directions, the whole ambient partial kernel, and the
later joint-source condition remain Open. The relative Lefschetz and
Zariski--van Kampen sources opened this hour do not apply to the actual
special source line under their stated hypotheses. We retain their
exact applicability boundaries rather than replacing the source by a
generic line. The distinction between accepted formal results and
reviewed post-cutoff research is explicit in the research record.

All49 task/lead rows remain. The paper has{metrics['pages']} pages,
252 numbered statements:211 Proved,16 Refuted,19 Open,6 Known;
101 bibliography records, each with an explicit verification status.
The final build has zero overfull boxes, warnings, undefined references,
and errors. Final PDF SHA256:{metrics['pdf_sha256']}.
The completed visible inspection and exact page list are in
records/checkpoint15_typesetting.txt. Initial and final PDFs, metrics,
and any diagnostic build outputs remain distinguishable.

Every earlier archive remains unchanged. The next progress review and
checkpoint are scheduled for16:49:30 UTC. We resume substantive work
immediately after immutable capture.
'''
(ROOT/'records/progress_review_15h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Fifteenth-hour progress review\n' not in s
s+=f'''\n## Fifteenth-hour progress review

At {now.isoformat()} we recorded CONTINUE. A82-A84 close actual
augmentation projectivity, dyadic freeness, modular-head duality and
full compact projective duality gaps, while retaining the incidence
and nonselfdual limitations. B82-B83 prove exact partial-source kernel
comparisons, including all mixed words in a specified actual subgroup
enlarged by the product-one meridian. Both filling quotients are
detected through the actual target surfaces, discretely and compactly.
An invalid normalizer relaxation was explicitly rejected and separated
by an order384 finite witness. The whole ambient and joint-source
gates, and both main full decisions, remain Open. See
records/progress_review_15h.md and
records/fifteenth_hour_research_report.md. The next review/checkpoint
is at16:49:30 UTC.
'''
p.write_text(s)
p=ROOT/'records/continuation_state.md'
p.write_text(p.read_text()+f'''\n## Actual fifteenth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_15h.md.
Every writer is paused for immutable capture. Release writers as
soon as the ZIP is complete. Independent verification and saving
then proceed without altering that archive. Both main full decisions
remain Open. Next review/checkpoint:2026-11-16 16:49:30 UTC.
''')
print('Timed fifteenth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as stream:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],
                   stdout=stream,check=True)
retention=json.loads((ROOT/'records/checkpoint_version_retention_summary.json').read_text())
assert retention['archives']==14 and retention['archive_entries']==23141
assert retention['omissions']==0
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'15'],check=True)
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
