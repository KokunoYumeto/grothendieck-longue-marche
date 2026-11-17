"""Integrate the two actual fixed-lifting module results without closing the tasks."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
formal = {r['id']: r['status'] for r in csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open())}
assert len(formal) == 260
assert formal['B.90'] == formal['B.91'] == 'Proved'
path = root / 'task_coverage.csv'
with path.open() as stream:
    reader = csv.DictReader(stream)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {r['task']: r for r in rows}
addition = (
    'B90 proves fixed lifting after the first relative centralization of the actual '
    'symmetric intersection, both discretely and in the actual compact quotient. '
    'B91 gives the full discrete intersection Alexander module with all transported '
    'node coefficients and an exact right-defect Tate criterion over F2[R]. '
    'It retains the relation-kernel cohomology term and proves only inclusion of '
    'the source left ideal, not its equality with the obstruction submodule.'
)
for task in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
    row = index[task]
    assert row['outcome'] == 'Open'
    for sid in ('B.90', 'B.91'):
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';' + sid
    assert addition not in row['state']
    row['state'] += ' ' + addition
    row['obstruction'] = (
        'The first centralized-intersection fixed-lift obstruction vanishes by B90. '
        'For the full discrete abelianized intersection, B91 leaves the exact '
        'submodule U=image H1(C2,relation image) inside the augmentation ideal F2[R] '
        'to determine; a target r lifts exactly when r inverse minus1 lies in U. '
        'The actual transported node columns and their relation-kernel H2 term '
        'cannot be replaced by the incidence matrix. The full nonabelian fixed '
        'lift, projected fixed-source equality, and actual completed coefficient '
        'comparison at this stronger stage remain Open. Whole source-kernel '
        'normality and the subsequent joint-source condition are not established.'
    )
    row['next_step'] = (
        'Compute the actual transported node columns in a common marking, with '
        'all old-base and deck translates; determine their Tate image while '
        'retaining relation dependencies. Prove the necessary source-ideal '
        'comparison or exhibit an actual target with a certified nonzero '
        'obstruction. Independently address the nonlinear kernel and the '
        'projected-source gate, then the joint-source and uniform-cover steps.'
    )
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
old = r'''specified free-factor settings. A larger actual subgroup controls all
five corrected positive source lifts under the product-one meridian;
its two filling quotients are \(\mathbb Z\times F_5\) and
\(\mathbb Z^2\), also for actual closed images. A selected tangential
Galois action preserves the source kernels and makes that meridian
literally cyclotomic. Six winding characters show that the controlled
arithmetic source enlargement is proper, without separating its kernel
from the full source kernel. A diagonal block controls a whole deleted
normal closure under arbitrary mixed retained-product words. Finally,
on the both-family filled surface the actual source is exactly the'''
new = r'''specified free-factor settings, including all five corrected positive
source operators and arbitrary mixed diagonal/product words. A selected
tangential Galois action preserves the source kernels with literal
meridian cyclotomy. Six winding characters prove its controlled source
enlargement proper, without separating the corresponding kernels.
On the both-family filled surface the actual source is exactly the'''
assert old in s
s = s.replace(old, new, 1)
old = '''zero-direction source word. The remaining nonabelian fixed-lift
cocycles, projected fixed-source comparison, whole source-kernel
normality and subsequent joint-source condition remain unresolved.'''
new = '''zero-direction source word. The first relative centralization of the
intersection has surjective fixed-element lifting, also in the actual
compact quotient. For its full discrete abelianization, a transported
Fox presentation retains every node coefficient and gives an exact
diagonal Tate obstruction criterion. The relation-module image, deeper
nonabelian fixed-lift cocycles, projected fixed-source comparison, and
subsequent joint-source condition remain unresolved.'''
assert old in s
paper.write_text(s.replace(old, new, 1))

p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '## Seventeenth-hour research: actual fixed-lift modules'
assert marker not in s
s += '''\n## Seventeenth-hour research: actual fixed-lift modules

B90 formalizes the completely checked first relative-centralization
result preserved as research in checkpoint16. It computes the actual
signed disjoint-lifted-component module and uses the inherited internal
discrete normal-generation theorem to exclude its singleton sign orbits.
Its integral first involution cohomology vanishes. Fixed lifting follows
in the stated discrete quotient; a separate density argument gives the
actual compact fixed-lift conclusion without an unproved completed
coefficient identification.

B91 retains the full two-factor action on the abelianized intersection.
Its locally finite van Kampen presentation is proved by pulling back the
actual finite nodal model to the old-fiber cover, then exhausting the
simply connected base. The product of Cayley trees identifies the free
intersection module with a tensor product of augmentation ideals. Each
actual transported node supplies its unique finite two-chain, including
both independent conjugating words. Paired peripheral paths give literal
negative swap. The unrestricted first involution cohomology is the
augmentation ideal over F2[R]; its second cohomology is zero. With the
right-defect convention, a diagonal target r lifts after abelianizing M
exactly when r inverse minus1 belongs to the image U of the actual
relation-submodule cohomology. The source left ideal is contained in U.
Their equality, the relation-kernel H2 contribution, the stronger compact
coefficient comparison and nonlinear lifting remain unproved.

Both new formal sources passed root and two independent complete proof
reviews. Their private components compiled cleanly and all seven pages
were visually inspected. The combined build and its own visual inspection
are recorded separately when complete. The register has260 statements:
218 Proved,17 Refuted,19 Open,6 Known, with104 bibliography entries.
All49 task/lead rows remain; neither main full decision is closed.
The developing exact finite-lasso producer is separate from the theorem:
no full transported Fox matrix or nonzero obstruction is claimed merely
from the existence of this presentation. Detailed ongoing research is in
records/seventeenth_hour_research_report.md.
'''
p.write_text(s)
print('Integrated B90/B91 coverage and abstract:260 statements; all49 tasks retained.')
