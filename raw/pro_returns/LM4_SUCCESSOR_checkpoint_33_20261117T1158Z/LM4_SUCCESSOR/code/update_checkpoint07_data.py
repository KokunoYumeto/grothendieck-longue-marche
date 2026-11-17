"""Integrate the reconstructed seventh-hour results without changing open decisions."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root/'task_coverage.csv'
with path.open() as f:
    reader = csv.DictReader(f)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {r['task']: r for r in rows}
formal = {r['id']: r['status'] for r in csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open())}
required = ['A.55','A.56','A.57','B.65','B.66','C.41','C.42']
assert all(formal.get(k) == 'Proved' for k in required), {k:formal.get(k) for k in required}

def add(task, ids, state, obstruction=None, next_step=None):
    row = index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';'+sid
    marker = ' Seventh-hour extension: '
    row['state'] = row['state'].split(marker)[0] + marker + state
    if obstruction is not None:
        row['obstruction'] = obstruction
    if next_step is not None:
        row['next_step'] = next_step

scalar = ('The actual elementary-two exterior-square center is attained in A.55. '
          'The forced self-dual Q6 layer has an actual framed central cover with a verified negative action square and both frame norms in A.56. '
          'A.57 constructs the next simultaneous, genuinely nonsplit Bockstein quotient; it does not yet assert its next framed norm.')
for task in ['Lead 2','Lead 3','A.4','A.5','A.6','A.8']:
    add(task,['A.55','A.56','A.57'],scalar+
        (' The full involution-conjugacy decisions and cofinality remain Open.' if task!='Lead 2' else ''),
        None if task=='Lead 2' else 'The full negative norm and compatible retained frames at a cofinal family of actual quotients remain unresolved.',
        'Control the actual next Bockstein action, its literal frames, and the newly exposed central refinement; retain the full question.')

head = ('The first actual relative dyadic relation-module quotient excludes nonidentity fixed heads when the parameter vanishes there. '
        'Under the proved self-centralizer hypothesis, one dyadic homology step determines the canonical head from the actual enlarged finite data. '
        'This does not prove joint generation or the full third-cusp identity.')
for task in ['A.3','A.7','A.8']:
    row = index[task]
    old = row['state']
    for sid in ['C.41','C.42']:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';'+sid
    suffix = ' Canonical-head refinement: '
    row['state'] = old.split(suffix)[0]+suffix+head

rigid = ('The entire actual cyclic pure centralizer centralizes a dihedral D5. '
         'Its ten nonconstant rigid-seven maps have one common discrete/completed kernel, '
         'the kernel of an explicit six-generator homomorphism to PB6; the two constant maps are retained separately. '
         'Injectivity and the induced full profinite topology of that map remain unproved.')
rational = ('For every prime, an actual common rational prounipotent line with compatible source preimages survives all rigid tests. '
            'The unbounded-denominator issue prevents a compact pro-prime or full profinite conclusion.')
for task in ['B.4','B.4.a','B.4.b','B.4.c','B.4.h']:
    add(task,['B.65','B.66'],rigid+' '+rational,
        'The actual full kernel/embedded-closure comparison remains unresolved. Rational or representation-level common images do not produce a full centralizer element.',
        'Resolve the exact nonabelian Birman-kernel comparison and its induced profinite topology, or an actual joint quotient detecting it.')
for task in ['B.3','B.3.P6']:
    add(task,['B.66'],rational,
        'No uniform integral control or full profinite lift of the common rational line is proved.',
        'Retain the compact and full comparison as separate assertions.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)

paper = root/'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both universal full decisions remain open.
The canonical conjugator satisfies the full pentagon and all maximal
pro-prime tests. We prove additional actual finite-head and relative
dyadic detection statements, while retaining its unresolved full
third-cusp and generation conditions.
For finite abelian residual layers over the original relative
pronilpotent base, we control the depth of the actual scalar refinements.
We attain the elementary-two exterior-square center and construct a
forced self-dual layer with its prescribed frames and verified negative
norm. Its next simultaneous Bockstein quotient is genuinely nonsplit.
These constructions do not give a cofinal involutory family.
For the icosahedral problem, we determine the complete common triadic
image and reduce the nonconstant cyclic rigid tests to one explicit
six-strand braid homomorphism. A compatible nonzero common rational
prounipotent line survives every rigid test. The full kernel comparison
and the integral lifting problem remain unresolved.
We also retain the source audits, torus and real-structure reductions,
controlled noncompact comparisons, and corrected five-point census.
Every numbered assertion has an explicit proof status. A gap in a
published proof is not a counterexample to its theorem. This work is
incomplete, and no priority is claimed.'''
a,b = s.index('\\begin{abstract}'),s.index('\\end{abstract}')
paper.write_text(s[:a]+'\\begin{abstract}\n'+abstract+'\n'+s[b:])
print('Updated all 49 retained task rows; both main decisions remain Open.')
