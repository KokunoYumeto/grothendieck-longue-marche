"""Integrate the exact actual node/syzygy comparison, keeping all tasks Open."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root / 'task_coverage.csv'
with path.open() as stream:
    reader = csv.DictReader(stream)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {r['task']: r for r in rows}
addition = (
    'B92 identifies the actual free-node Tate image exactly with the source left '
    'ideal J_I and defines the remaining canonical syzygy map kappa into the '
    'source-coset augmentation module. Its exact inverse-coset membership '
    'criterion retains every relation among the transported node columns.'
)
for task in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
    row = index[task]
    assert row['outcome'] == 'Open'
    assert 'B.92' not in row['statement_ids'].split(';')
    row['statement_ids'] += ';B.92'
    row['state'] += ' ' + addition
    row['obstruction'] = (
        'B90 neutralizes the first centralized-intersection fixed-lift obstruction. '
        'B91/B92 reduce the full discrete Alexander-layer lift of r to whether '
        'r inverse I minus I lies in the image of the actual syzygy map '
        'kappa:H2(C2,Z2) to the augmentation module of F2[R/I]. The free-node '
        'contribution is exactly J_I, but the additional syzygy image is '
        'undetermined. Its vanishing is sufficient, not asserted necessary, '
        'for projected fixed-source equality at that layer. The nonlinear '
        'kernel [M,M], full compact coefficient comparison, whole source-kernel '
        'normality and subsequent joint-source condition remain Open.'
    )
    row['next_step'] = (
        'Finish and audit the actual common involution marking for all64 nodal '
        'Fox columns and six old-base actions, including every F5 deck translate. '
        'Determine the invariant syzygy transfer or an exact actual coset '
        'membership obstruction. Keep based transport conventions explicit. '
        'Then address nonlinear fixed lifting, the compact comparison and the '
        'separate joint-source and uniform-cover gates.'
    )
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
old = '''Fox presentation retains every node coefficient and gives an exact
diagonal Tate obstruction criterion. The relation-module image, deeper
nonabelian fixed-lift cocycles, projected fixed-source comparison, and
subsequent joint-source condition remain unresolved.'''
new = '''Fox presentation retains every node coefficient and gives an exact
diagonal Tate obstruction criterion. Equivariant node paths identify
the source-ideal contribution and isolate the residual syzygy map.
That map, deeper nonabelian lifting, projected fixed-source equality,
and the subsequent joint-source condition remain unresolved.'''
assert old in s
paper.write_text(s.replace(old, new, 1))

p = root / 'LM4_SUCCESSOR_report.md'
s = p.read_text()
marker = '### Exact equivariant node image and residual syzygies'
assert marker not in s
s += '''\n### Exact equivariant node image and residual syzygies

B92 proves that actual equivariant node whiskers identify the free-node
cohomology image with the source left ideal J_I. The fixed-source peripheral
tree extends to a complete critical-value tree; its local z^2-t^2 model
retains the actual source lasso and common nearby basepoint. The node
indices and E coefficients are distinct. Direct commutator expansion
shows that each fixed column differs from its actual source rectangle
by a coboundary. Thus every additional obstruction contribution is the
image of a canonical R-linear map kappa from H2 of the node-column kernel
to the source-coset augmentation module. The lift criterion is precisely
membership of r inverse I minus I in that image. Its vanishing is neither
proved nor asserted necessary for the projected-source equality.

Root and both independent reviewers read the complete proof. The three
private pages use the combined-paper geometry and passed visual inspection
and clean compilation. The combined integration has261 statements:
219 Proved,17 Refuted,19 Open,6 Known, with104 bibliography entries and
all49 task rows. Both full main decisions remain Open. Exact formal and
root audit records are work_A/B92_equivariant_node_syzygy.tex and
records/equivariant_node_root_review_17h.md.

The finite nodal computation has completed18 lassos and64 transported
Fox columns, using129 Schreier generators and2164 nonzero square terms.
Independent geometry, word, boundary and augmentation checks pass in
their stated convention. Six old-base actions have also been computed
with exact discriminant orders. A stronger common-marking check then
exposed a convention mismatch between the transported involution and
the first old-base action. Its failed data and output are preserved;
the finite arrays are not yet treated as a complete compatible involution
presentation. Resolving that mismatch precedes any use of them to
calculate kappa. The abstract B90--B92 proofs do not rely on the disputed
finite identification. See the detailed seventeenth-hour research report
for every comparison and limitation.
'''
p.write_text(s)
print('Integrated B92 coverage and abstract;49 task rows retained, both main decisions Open.')
