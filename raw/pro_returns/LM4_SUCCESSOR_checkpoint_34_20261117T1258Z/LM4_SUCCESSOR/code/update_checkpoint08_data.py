"""Integrate eighth-hour actual results while retaining every requested task."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root / 'task_coverage.csv'
with path.open() as f:
    reader = csv.DictReader(f)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {row['task']: row for row in rows}
formal = {row['id']: row['status'] for row in csv.DictReader((root / 'LM4_SUCCESSOR_results.csv').open())}
required = {'A.58':'Proved','A.59':'Proved','A.60':'Proved','A.61':'Proved','A.62':'Proved','B.67':'Refuted','B.68':'Proved','C.43':'Proved'}
assert all(formal.get(k) == v for k,v in required.items()), {k:formal.get(k) for k in required}

def add(task, ids, state, obstruction=None, next_step=None):
    row = index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';' + sid
    marker = ' Eighth-hour extension: '
    row['state'] = row['state'].split(marker)[0] + marker + state
    if obstruction is not None: row['obstruction'] = obstruction
    if next_step is not None: row['next_step'] = next_step

scalar = ('A.58 identifies the exact exterior-square scalar center for every finite abelian residual layer under the stated actual hypotheses. '
          'A.59 computes the additional Bockstein center C4^18 times C2^90 and its stable18-dimensional kernel. '
          'A.60 proves the actual integral negative action square. A.61 supplies both literal involutory normalizers after refining the newest A.56 central frame choices, while retaining all older prescribed families. '
          'A.62 constructs the actual nested all-2^n integral cusp tower and compatible involutory images with simultaneous frames by compactness; its inverse-limit kernel is relatively perfect. '
          'The exact stored A.56 frame is not asserted to extend. No cofinal family or full negative involution is constructed.')
for task in ['Lead 2','Lead 3','A.4','A.5','A.6','A.8']:
    add(task, ['A.58','A.59','A.60','A.61','A.62'], scalar,
        None if task == 'Lead 2' else 'The cofinal full-quotient norm and compatible literal-frame problem remain unresolved; the specified Bockstein refinement is now handled in its stated existential scope.',
        'Move beyond the specified class-two integral tower to a cofinal finite-quotient construction, or a genuine full obstruction; keep all three main conjugacy decisions open.')

regular = ('C.43 proves self-centralizing sections for regular pants involutions and the inherited first-dyadic finite-head detection. '
           'The common full-normalizer transporter is unique when it exists. This does not recognize a free product, prove generation, or solve the third cusp; finite r-normalizers remain variable.')
for task in ['A.3','A.7','A.8','C.2','C.4']:
    row = index[task]
    if 'C.43' not in row['statement_ids'].split(';'): row['statement_ids'] += ';C.43'
    marker = ' Regular-pants refinement: '
    row['state'] = row['state'].split(marker)[0] + marker + regular

braid = ('B.67 explicitly refutes the intermediate Q=Z2*Z2*Z injection into PB5. '
         'The word [(ae)^(-1)f(ae),c] has a nontrivial finite S3 image in Q but a trivial actual PB5 image. '
         'Its actual PB6 image is nonidentity, so it does not settle the full six-strand rigid kernel or the embedded profinite comparison.')
for task in ['B.4','B.4.a','B.4.b','B.4.c','B.4.h']:
    add(task, ['B.67'], braid,
        'The full theta5 kernel and its induced profinite topology remain unresolved. The refuted intermediate presentation cannot supply injectivity.',
        'Analyze the actual surviving Birman fiber and its full source action; keep rational, discrete and full profinite conclusions separate.')

if formal.get('B.68') == 'Proved':
    for task in ['B.4','B.4.a','B.4.c']:
        row = index[task]
        if 'B.68' not in row['statement_ids'].split(';'): row['statement_ids'] += ';B.68'
        marker = ' Filling-word refinement: '
        row['state'] = row['state'].split(marker)[0] + marker + ('B.68 certifies that the surviving full Birman fiber word is filling and its point-push is pseudo-Anosov. This is a discrete classification, with no completed-centralizer inference.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader(); writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both universal full decisions remain open.
We determine actual finite-head restrictions on the canonical conjugator,
while retaining its unresolved full third-cusp and generation conditions.
For finite abelian residual layers over the original relative pronilpotent
base, we identify the exact exterior-square scalar center and bound its
refinement depth. A forced self-dual layer has a verified framed negative
action. Its next genuinely nonsplit Bockstein quotient and exact stable
central refinement also admit an involutory negative action and both
peripheral normalizers, after refining the newest central frame choices
while preserving the earlier prescribed families. The construction extends
to an actual compatible tower at every two-power exponent, with a relatively
perfect inverse-limit kernel. This tower is not proved cofinal.
For the icosahedral problem, we determine the complete common triadic
image and reduce the nonconstant cyclic rigid tests to one explicit
six-strand braid homomorphism. A compatible nonzero common rational
prounipotent line survives every rigid test. We refute a proposed
intermediate braid injection by an exact word, whose full lift is a
certified filling point push and hence pseudo-Anosov. The full kernel
comparison and integral lifting problem
remain unresolved.
We retain the source audits, torus and real-structure reductions,
controlled noncompact comparisons, and corrected five-point census.
Every numbered assertion has an explicit proof status. A gap in a
published proof is not a counterexample to its theorem. This work is
incomplete, and no priority is claimed.'''
a,b = s.index('\\begin{abstract}'),s.index('\\end{abstract}')
paper.write_text(s[:a]+'\\begin{abstract}\n'+abstract+'\n'+s[b:])
print('Updated all49 task rows; A.8 and B.4 remain Open.')
