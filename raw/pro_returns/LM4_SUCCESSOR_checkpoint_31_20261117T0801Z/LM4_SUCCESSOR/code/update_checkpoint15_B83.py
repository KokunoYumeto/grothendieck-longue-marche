"""Integrate the reviewed controlled subgroup result, retaining the full gates."""
from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
formal={r['id']:r['status'] for r in csv.DictReader(
    (root/'LM4_SUCCESSOR_results.csv').open())}
assert formal.get('B.83')=='Proved'
path=root/'task_coverage.csv'
with path.open() as stream:
    reader=csv.DictReader(stream)
    fields,rows=reader.fieldnames,list(reader)
assert len(rows)==49
index={r['task']:r for r in rows}
addition=(
    'B83 now controls all mixed words in the actual subgroup generated '
    'by two constant-family source meridians, three specified old source '
    'lifts, and the product-one meridian. Its complete constant-family '
    'and both-family filling kernels equal the selected source-kernel '
    'images, with quotients Z times F3 and Z squared, also for actual '
    'closed images in full completions. The proof uses correcting '
    'conjugators in an already controlled stage and actual winding/base '
    'detectors through the fillings. The other two constant meridians '
    'and three old source operators remain outside this induction.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    row=index[task]
    assert row['outcome']=='Open'
    if 'B.83' not in row['statement_ids'].split(';'):
        row['statement_ids']+=';B.83'
    if addition not in row['state']:
        row['state']+=' '+addition
    row['obstruction']=(
        'The rank-nine and controlled product-one subgroup kernel '
        'equalities do not prove normality of the entire partial '
        'source kernel. In the w presentation the remaining two '
        'constant meridians, three old source operators, and the other '
        'retained cluster directions are not controlled by the valid '
        'stage induction. A proposed relaxation replacing earlier-stage '
        'membership by membership in an eventual normalizer is false, '
        'with an explicit order384 finite witness; B82-B83 use the '
        'stronger valid hypothesis. The subsequent joint-source '
        'condition remains separate.'
    )
    row['next_step']=(
        'Extend the actual controlled subgroup theorem to the missing '
        'source directions using a valid whole-kernel mechanism, or '
        'prove an applicable relative geometric kernel comparison for '
        'the actual special line. Preserve all transported old-node '
        'and positive-triple relations. Then address the joint kernel '
        'and B75 uniform finite-cover condition.'
    )
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields)
    writer.writeheader();writer.writerows(rows)

paper=root/'LM4_SUCCESSOR_paper.tex'
s=paper.read_text()
old='''an ordered rank-nine free factor, discretely and after completion.
These intersections do not establish normality of the entire source
deletion kernel; the subsequent joint-source condition also remains
open.'''
new=r'''an ordered rank-nine free factor, discretely and after completion.
An actual subgroup enlarged by the product-one meridian has its full
two specified filling kernels detected, with quotients
\(\mathbb Z\times F_3\) and \(\mathbb Z^2\), and the corresponding
quotients for actual closed images in the full completion. Its proof
controls mixed source-operator words by a valid stage induction.
These restricted kernel equalities do not establish normality of the
entire source deletion kernel; the subsequent joint-source condition
also remains open.'''
assert old in s and new not in s
paper.write_text(s.replace(old,new,1))
print('B83 added to five main-B coverage rows and the abstract; all full gates stay Open.')
