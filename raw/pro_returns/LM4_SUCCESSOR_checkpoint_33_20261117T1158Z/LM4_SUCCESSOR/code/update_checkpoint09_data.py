"""Integrate ninth-hour results and keep all49 requested outcome rows."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root / 'task_coverage.csv'
with path.open() as f:
    reader = csv.DictReader(f)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {row['task']: row for row in rows}
formal = {row['id']: row['status'] for row in csv.DictReader(
    (root / 'LM4_SUCCESSOR_results.csv').open())}
required = {'A.63': 'Proved', 'A.64': 'Proved', 'A.65': 'Proved',
            'B.69': 'Refuted', 'B.70': 'Proved', 'B.71': 'Proved',
            'B.72': 'Proved', 'C.44': 'Proved'}
assert all(formal.get(k) == v for k, v in required.items()), required


def update(task, ids, state, obstruction=None, next_step=None):
    row = index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';' + sid
    row['state'] = state
    if obstruction is not None:
        row['obstruction'] = obstruction
    if next_step is not None:
        row['next_step'] = next_step


cup = ('The actual all-2^n integral cusp tower now has six independent nonsplit '
       'cross-cup directions beyond it. The original fixed affine tuple has a genuine '
       's-frame obstruction, but an explicit changed affine tuple has zero cusp-frame '
       'differences and passes every actual action-square and s/r norm equation. '
       'Jacobi and the exact old exterior-square center prove that the actual new '
       'kernel is relatively perfect at every integral level and in the inverse limit. '
       'The scalar lifting criterion therefore supplies a full positive lift with these '
       'quotient actions and frames, retaining the original C-data and earlier families. '
       'The negative companion is involutory on this enlarged tower; its full square '
       'and cofinality remain unresolved.')
remaining_a = ('No cofinal full-quotient construction or full negative norm solution '
               'is proved. The chosen noncentral six-cup scalar refinement and its '
               'specified quotient frame norms are now completely handled.')
next_a = ('Attack the next noncentral source quotient or a general equivariant '
          'finite-embedding theorem; alternatively prove an obstruction to the full '
          'negative norm. Keep the three full conjugacy decisions open.')
update('Lead 2', ['A.63', 'A.64', 'A.65'],
       'The exact closed-normal central-quotient criterion for a peripheral lift is '
       'proved. A.58 determines the scalar center for all finite abelian residual '
       'layers under its stated actual hypotheses. A.65 also computes zero additional '
       'scalar kernel for the specified noncentral six-cup extension at every integral '
       'level; it uses the original-base cohomology and the actual Jacobi relation, '
       'without assuming automatic acyclicity after arbitrary base changes.', '', next_a)
for task in ['Lead 3', 'A.4', 'A.5', 'A.6', 'A.8']:
    prefix = {
        'Lead 3': 'The full parity-one involution remains undecided. ',
        'A.4': 'The proved odd-prime and finite-head results remain in force; the '
               'complete arbitrary dyadic and mixed-level classification remains open. ',
        'A.5': 'The complete pointed set for H, its parity map, and the full '
               'involution-conjugacy count remain undetermined; the earlier '
               'cohomology-cardinality statements retain their stated group scopes. ',
        'A.6': 'Parity on all full involutions of GT0 and GT remains undecided. ',
        'A.8': 'All three universal full involution-conjugacy assertions remain open. ',
    }[task]
    update(task, ['A.63', 'A.64', 'A.65'], prefix + cup, remaining_a, next_a)

regular = ('For every regular negative pants involution normalized at z, the unique '
           'solution of sigma(g)g^-1=z has a full-unit image in F/<<z>>=Zhat. '
           'The substitution x->g,z->z gives an actual conjugacy on F/O^p(<<z>>) '
           'for every prime p and on F/R_nil(<<z>>). This conjugacy is in the '
           'automorphism group of that relative quotient; original peripheral '
           'marking and generation of full F are not asserted.')
for task in ['A.3', 'A.7', 'A.8', 'C.2', 'C.4']:
    row = index[task]
    old = row['state'].split(' Regular-pants refinement: ')[0]
    old = old.split(' Regular-pants Alexander refinement: ')[0]
    update(task, ['C.44'], old + ' Regular-pants Alexander refinement: ' + regular)

braid = ('The full six-strand cyclic rigid map is noninjective: the explicit '
         'ten-letter word w0=[f5^-1 f1^-1 f0^-1 f2^-1,f1] has nontrivial S3 '
         'image in the source but trivial actual PB6 image. Both its discrete '
         'kernel and its completed-map kernel are free of countably infinite rank, '
         'with the convergent-basis convention in the profinite case. Equality of '
         'the completed kernel with the closure of the discrete kernel is open. '
         'The actual rigid-kernel source closures still have the full three-dimensional '
         'principal Eichler group as their common image in the joint product of all '
         'full rigid tests and the entire integral3-adic symplectic representation. '
         'That exact joint-quotient intersection supplies no common full ambient lift.')
prefix_b = {
    'B.4': 'The full icosahedral centralizer decision K=1 remains open. ',
    'B.4.a': 'The tetrahedral rigid kernels and explicit monodromy remain proved. ',
    'B.4.b': 'All495 cross-ratio pairs are written and checked, and a false-positive '
             'pair is known; their complete solution set remains undetermined. ',
    'B.4.c': 'The unrefined product is closed. Arbitrary finite-index refinements '
             'remain equivalent to the unresolved full centralizer decision; the '
             'earlier specified open refinements remain proved. ',
    'B.4.h': 'Universal braid-constrained R2 is false in the stated prime7 example; '
             'the complete requested relative images remain open. ',
}
for task, prefix in prefix_b.items():
    update(task, ['B.69', 'B.70', 'B.71'], prefix + braid,
           'The induced profinite kernel topology and a common lift in the full '
           'ambient completion remain unresolved. The complete rigid tests together '
           'with the entire integral3-adic representation still do not separate the '
           'two source closures.',
           'Use the faithful common-involution quotient or another full ambient '
           'topology/finite-subgroup argument; do not promote quotient intersections '
           'or separate source preimages to a common ambient element.')

for task in ['B.4', 'B.4.c']:
    row = index[task]
    update(task, ['B.72'], row['state'] +
           ' Moreover H_T intersect g H_5 g^-1 is trivial for every discrete '
           'ambient g, by the exact one/five-curve cusp types and the finite '
           'symmetry kernel of a pseudo-Anosov centralizer. No corresponding '
           'intersection or density assertion is proved in the full completion.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both universal full decisions remain open.
For finite abelian residual layers over the original relative pronilpotent
base, we identify the exact exterior-square scalar center and its bounded
refinement depth. A compatible integral cusp tower with involutory negative
images extends by six independent, genuinely nonsplit cross-cup directions.
An explicit changed affine frame solves every new quotient norm equation.
Jacobi and the complete old scalar center prove that the actual enlarged
kernel is relatively perfect at every integral level and in the limit.
Thus full positive peripheral lifts realize the enlarged quotient actions
and both frames. Their full negative square and cofinality remain undecided.
For regular pants involutions, an exact compact Alexander equation proves
that the canonical conjugator has full-unit procyclic image and gives actual
relative pronilpotent conjugacy, without asserting full generation or the
original peripheral marking.
For the icosahedral problem, we explicitly refute injectivity of the full
six-strand cyclic rigid map. Both its discrete kernel and its completed-map
kernel have countably infinite free rank in their respective categories;
their closure comparison remains open. Actual rigid-kernel source closures
still have the complete common principal Eichler group in the joint quotient
formed by all full rigid tests and the entire integral triadic symplectic
representation. The two discrete source groups have trivial intersection
under every ambient conjugation, but no completed analogue is inferred.
These results supply no common element in the full ambient group.
We retain the source audits, torus and real-structure reductions, controlled
noncompact comparisons, and corrected five-point census. Every numbered
assertion has an explicit proof status. A gap in a published proof is not a
counterexample to its theorem. This work is incomplete; no priority is claimed.'''
a, b = s.index('\\begin{abstract}'), s.index('\\end{abstract}')
paper.write_text(s[:a] + '\\begin{abstract}\n' + abstract + '\n' + s[b:])
print('Updated all49 task rows; both main decisions remain Open.')
