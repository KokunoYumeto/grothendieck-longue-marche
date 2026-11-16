"""Capture the authorized ninth hourly checkpoint at its scheduled time.

All research writers acknowledged the brief snapshot pause.  Earlier
archives are read only; package_checkpoint.py refuses to overwrite.
"""
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
deadline=datetime(2026,11,16,9,49,30,tzinfo=timezone.utc)
assert not (ROOT.parent/'LM4_SUCCESSOR_checkpoint_09.zip').exists()
while True:
    remaining=(deadline-datetime.now(timezone.utc)).total_seconds()
    if remaining<=0:
        break
    time.sleep(min(0.5,remaining))
now=datetime.now(timezone.utc)
review=f'''# Ninth-hour progress review

Scheduled review: 2026-11-16 09:49:30 UTC.
Actual review record: {now.isoformat()}.
Decision: CONTINUE.

The user's progress rule asks whether current work advances a main
question or an open item, rather than filling detail away from it.
The current work passes that test. Both main decisions remain Open.

For A, the formal paper now proves the actual six-cup extension,
changes the discretionary affine data to solve its complete frames,
and proves relative perfectness of its entire scalar source kernel
at every integral exponent. The resulting action and frames have
a full positive realization; full negative order and cofinality are
not inferred. Current research has then reached an actual class-three
extension, found its nonzero scalar resonance, and repaired the first
new norm obstruction by changing old affine choices. The complete
ordinary action-square gate has408 zero values among all524288 free
actions. A new zero-action tuple passes the old, lower-six, and
ordinary-sixteen action and s-frame equations. The remaining concrete
gates are the four coupled UT4 frame equations and the actual scalar
cover. This directly attacks the next full-source lifting obstruction.

For B, the full cyclic rigid test is now proved noninjective by an
actual nontrivial source word with trivial faithful Artin image. Its
completed kernel is identified, and the single joint rigid/symplectic
comparison is shown still to admit the exact common principal image.
The new all-conjugate discrete intersection theorem separates the
source groups throughout the discrete ambient group. Work has moved
to a faithful common-involution quotient retaining its branch points;
the decorated seven-point map is faithful on the completed cyclic
source. Matching the two lifts in the full ambient completion remains
the exact unresolved step. This is a change of method at that step,
not another metabelian or representation census.

The regular-pants unit argument also reaches actual nonsolvable wreath
quotients, with a precise counterexample to using the unit head alone
for arbitrary quotients. No quotient-generation result is promoted to
generation of the full free profinite group.

The formal ninth-hour paper has258 pages,222 numbered statements,
86 bibliography entries, and49 task rows. Its final build is clean;
55 rendered pages and all seven contacts were inspected, with four
critical pages also inspected in full. The late research above is
retained as checked notes/programs/stdout, not unreviewed formal claims.

The next progress review and checkpoint are scheduled for10:49:30 UTC.
We resume substantive research immediately after immutable capture.
'''
(ROOT/'records/progress_review_09h.md').write_text(review)
p=ROOT/'LM4_SUCCESSOR_report.md'
s=p.read_text()
assert '## Ninth-hour progress review\n' not in s
s+=f'''\n## Ninth-hour progress review

At {now.isoformat()} we recorded CONTINUE. The actual next source
extension, repaired higher frame equations, and faithful full ambient
comparison advance the main questions. Both full decisions remain Open.
The exact assessment is records/progress_review_09h.md. The next
scheduled review and checkpoint are at 10:49:30 UTC.
'''
p.write_text(s)
p=ROOT/'records/continuation_state.md'
s=p.read_text()+f'''\n## Actual ninth-hour review

CONTINUE recorded at {now.isoformat()}. See progress_review_09h.md.
The checkpoint is now being captured with every agent writer paused.
Release the agents immediately after immutable ZIP capture; upload and
independent verification follow without modifying that archive.
Next checkpoint/review: 2026-11-16 10:49:30 UTC.
'''
p.write_text(s)
print('Timed ninth-hour review:',now.isoformat(),'CONTINUE',flush=True)
subprocess.run([sys.executable,str(ROOT/'code/refresh_computation_inventory.py')],check=True)
with (ROOT/'records/checkpoint_version_retention_run.out').open('w') as f:
    subprocess.run([sys.executable,str(ROOT/'code/preserve_checkpoint_versions.py')],stdout=f,check=True)
subprocess.run([sys.executable,str(ROOT/'code/package_checkpoint.py'),'9'],check=True)
print('Immutable capture completed:',datetime.now(timezone.utc).isoformat(),flush=True)
