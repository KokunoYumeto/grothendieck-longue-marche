"""Integrate reviewed B84-B87 while keeping every main and lead row."""
from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
formal={r['id']:r['status'] for r in csv.DictReader(
    (root/'LM4_SUCCESSOR_results.csv').open())}
assert len(formal)==256
assert all(formal.get(sid)=='Proved' for sid in ('B.84','B.85','B.86','B.87'))
path=root/'task_coverage.csv'
with path.open() as stream:
    reader=csv.DictReader(stream)
    fields,rows=reader.fieldnames,list(reader)
assert len(rows)==49
index={r['task']:r for r in rows}

state=(
    'The faithful configuration and split Birman comparisons retain the '
    'actual residual centralizer. B81-B82 give exact whole-kernel '
    'intersections in specified free-factor and partial-source settings. '
    'B83-B84 now control all five corrected positive source lifts and '
    'four deleted Nielsen generators under the product-one meridian, '
    'with actual constant and both-family quotients Z times F5 and Z '
    'squared, also for closed images. B85 constructs a selected '
    'source-compatible tangential Galois action with literal b cyclotomy; '
    'six characters prove that its controlled arithmetic source '
    'enlargement is proper, without separating the corresponding '
    'kernel subgroups. B86 controls the whole normal closure of one '
    'deleted direction under arbitrary mixed diagonal and four retained '
    'product words and identifies that block\'s exact source intersection. '
    'B87 identifies the actual source on the both-family filled surface '
    'with the fixed subgroup of an explicit rational involution, '
    'discretely and in full completion, using the actual bundle and a '
    'finite cone-class detector. The full marginal and subsequent '
    'joint-source comparisons, and the main centralizer decision, '
    'remain Open.'
)
obstruction=(
    'The controlled blocks do not yet yield normalization of the entire '
    'source deletion kernel under all retained directions and the old '
    'zero source operator. The valid stage proof requires correctors '
    'inside an already controlled stage; the weaker arbitrary-normalizer '
    'version is false. The rho map excludes the current single-b '
    'criterion for a source direction with nonzero zero-base winding. '
    'For the actual symmetric deletion, the fiber-product map is '
    'surjective but fixed images need not automatically have fixed '
    'lifts through the intersection of its two kernels. The projected '
    'fixed-source comparison after critical fillings is also unproved. '
    'Neither the64 transverse mixed nodes nor B87 on the filled surface '
    'alone supplies these two comparisons. The later joint-source '
    'condition remains separate.'
)
next_step=(
    'Resolve the actual symmetric-deletion fixed-lift cocycles and the '
    'projected fixed-subgroup comparison after the18 critical product '
    'fibers, or prove the missing mixed-direction whole-kernel '
    'normalization directly. Use the actual source and compact images; '
    'do not replace fixed lifting by a general relative product '
    'injectivity assertion. Then address the joint-source kernel and '
    'B75 uniform finite-cover condition.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    row=index[task]
    assert row['outcome']=='Open'
    for sid in ('B.84','B.85','B.86','B.87'):
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids']+=';'+sid
    row['state']=state
    row['obstruction']=obstruction
    row['next_step']=next_step
index['B.4.c']['state']=(
    'The required refined product closedness and global profinite '
    'fixed-complex conclusion remain Open. '+state)

fox=(
    'The actual marked Fox criterion is now explicit: full generation '
    'is equivalent to a unit in the full completed group ring, and its '
    'twisted-fixed equation has been derived. That equation does not '
    'supply an inverse; a generic fixed augmentation-one nonunit only '
    'refutes the proposed ring shortcut, not the actual involution '
    'claim. The unit/generation gate remains Open.'
)
for task in ('A.7','A.8'):
    if fox not in index[task]['state']:
        index[task]['state']+=' '+fox
assert all(index[t]['outcome']=='Open' for t in ('A.8','B.4','B.4.c','C.2'))
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

paper=root/'LM4_SUCCESSOR_paper.tex'
s=paper.read_text()
start=s.index('For the icosahedral problem, faithful configuration comparisons')
end=s.index('The paper retains the published-proof audits',start)
replacement=r'''For the icosahedral problem, faithful configuration comparisons and a
split Birman extension identify an exact completed nonabelian cocycle
condition. Actual marginal pencils and a tangent-line bundle retain
the based source. Whole filling-kernel intersections are proved in
specified free-factor settings. A larger actual subgroup controls all
five corrected positive source lifts under the product-one meridian;
its two filling quotients are \(\mathbb Z\times F_5\) and
\(\mathbb Z^2\), also for actual closed images. A selected tangential
Galois action preserves the source kernels and makes that meridian
literally cyclotomic. Six winding characters show that the controlled
arithmetic source enlargement is proper, without separating its kernel
from the full source kernel. A diagonal block controls a whole deleted
normal closure under arbitrary mixed retained-product words. Finally,
on the both-family filled surface the actual source is exactly the
fixed subgroup of an explicit rational involution, discretely and in
full completion. The proof retains the actual fiber topology and a
finite cone-class detector. These results do not supply the fixed-lift
comparison after symmetric deletion, whole source-kernel normality,
or the subsequent joint-source condition. A degree-eight cover refutes
a general special-source shortcut with one exceptional retained
tangency, without refuting the actual marginal. '''
paper.write_text(s[:start]+replacement+s[end:])
p=root/'LM4_SUCCESSOR_report.md'
s=p.read_text()
old='records/fifteenth_hour_research_report.md'
new='records/sixteenth_hour_research_report.md'
assert old in s and new not in s[:s.index('## Scope and principal decisions')+1000]
p.write_text(s.replace(old,new,1))
print('Updated49 task rows and abstract for B84-B87; both main full decisions Open.')
