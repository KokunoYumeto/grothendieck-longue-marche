"""Integrate tenth-hour results without changing any requested task outcome.

Use --all-integral-frames only after the complete A.69 proof and the
actual mod-four frame certificate have both been accepted.
"""
from pathlib import Path
import argparse
import csv

arg = argparse.ArgumentParser()
arg.add_argument('--all-integral-frames', action='store_true')
opts = arg.parse_args()
root = Path(__file__).resolve().parents[1]
path = root / 'task_coverage.csv'
with path.open() as f:
    reader = csv.DictReader(f)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {row['task']: row for row in rows}
formal = {row['id']: row['status'] for row in csv.DictReader(
    (root / 'LM4_SUCCESSOR_results.csv').open())}
required = ['A.66', 'A.67', 'A.68', 'A.69', 'B.73', 'B.74']
assert all(formal.get(k) == 'Proved' for k in required), required


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


frame_scope = (
    'The complete scalar action and both involutory normalizer frames extend '
    'compatibly through the entire integral tower: an actual mod-four norm '
    'calculation solves the only new binary compatibility condition, and '
    'higher central corrections reduce to zero modulo two. '
    if opts.all_integral_frames else
    'The complete scalar action and both involutory normalizer frames are '
    'proved at the first integral level. Extension of these particular new '
    'frames through every higher integral level is not asserted here. '
)
new_a = (
    'The actual integral cusp construction now has all six lower cups, four '
    'coupled class-three terms, and sixteen ordinary Frobenius cups. The '
    'initial scalar resonance is real. Its complete actual scalar kernel '
    'is C2^128, not a coordinatewise trace quotient; the next refinement '
    'is relatively perfect, at every integral level and in the inverse limit. '
    'The canonical negative action is lifted with the retained old center. '
    'A saved1119-variable rank234 system and independent original group-law '
    'checks solve the simultaneous new scalar and lower frame norms. '
    + frame_scope +
    'The selected action and frames have a full positive peripheral '
    'realization retaining the initial C-data and earlier families. '
    'The square of the full negative companion and cofinality remain open.'
)
remaining_a = (
    'The actual twenty-factor source quotient and its full128-dimensional '
    'scalar refinement are handled in the stated scope. There is still no '
    'cofinal construction or proof that the full negative square is one.'
)
next_a = (
    'Attack a general equivariant finite-embedding theorem or the next '
    'genuinely noncentral source obstruction, retaining the literal '
    'peripheral frames; alternatively find a full negative-norm obstruction.'
)
prefixes = {
    'Lead 3': 'The full parity-one involution remains undecided. ',
    'A.4': 'The arbitrary dyadic and mixed-level classification remains open. ',
    'A.5': 'The full pointed cohomology set, parity map, and conjugacy count remain undetermined. ',
    'A.6': 'Parity on all full involutions of GT0 and GT remains undecided. ',
    'A.8': 'All three universal full involution-conjugacy assertions remain open. ',
}
for task, prefix in prefixes.items():
    # Preserve the independently proved regular-pants comparison on A.8.
    old = index[task]['state']
    marker = ' Regular-pants Alexander refinement: '
    regular = marker + old.split(marker, 1)[1] if marker in old else ''
    update(task, ['A.66', 'A.67', 'A.68', 'A.69'],
           prefix + new_a + regular, remaining_a, next_a)
update('Lead 2', ['A.66', 'A.67', 'A.68', 'A.69'],
       'The exact closed-normal central-quotient criterion is proved. '
       'For the actual noncentral twenty-factor quotient, the complete '
       'new scalar kernel is C2^128 and the next scalar refinement is '
       'relatively perfect at every integral level and in the limit. '
       'This computation uses actual finite extensions, original-base '
       'cohomology, odd-weight averaging, Hall-Witt, and an attained '
       '128-dimensional source cover. ' + frame_scope,
       '', next_a)

new_b = (
    'The common involution identifies the actual completed intersection '
    'faithfully inside a colored eight-point mapping class group. Its '
    'pure-lift subgroup has index32; the decorated seven-point comparison '
    'is injective on the completed cyclic source, but equality with a '
    'seven-point intersection is not asserted. The full dihedral '
    'centralizer is C2*Z, with the actual pure H5 normal of index10. '
    'Its full profinite centralizer comparison follows from the valid '
    'prime-five theorem and the canonical direct product '
    'C_Gamma(C5)=C5 times C_Gamma(D5). This group embeds in the larger '
    'colored eight-point group and intersects its ordinary-label-fixing '
    'subgroup exactly in H5. These faithful comparisons do not settle '
    'the refined-product closure condition or supply a common full '
    'ambient element.'
)
for task in ['B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h']:
    old = index[task]['state'].split(' Faithful common-involution refinement: ')[0]
    update(task, ['B.73', 'B.74'],
           old + ' Faithful common-involution refinement: ' + new_b,
           'The intersection of the two actual source closures in the '
           'faithful colored ambient completion remains undetermined. '
           'All discrete conjugate intersections are trivial, and the '
           'unrefined product is closed; arbitrary finite-index refined '
           'products and simultaneous lift matching remain unresolved.',
           'Use the faithful eight-point comparison, the decorated '
           'seven-point cyclic embedding, and the full dihedral '
           'parameter orbifold to attack the ambient topology. '
           'Do not infer a virtual ambient retraction from the '
           'infinite-index centralizer retraction.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
integral_abstract = (
    'An actual mod-four compatibility calculation extends the new scalar '
    'frames through the entire integral tower. '
    if opts.all_integral_frames else
    'The new scalar frames are proved at the first integral level. '
)
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both universal full decisions remain open.
An actual integral cusp construction now retains six lower cups, four
coupled class-three terms, and sixteen ordinary Frobenius cups.
We compute its complete new scalar kernel as an elementary abelian
group of dimension 128, and prove that the next refinement is
relatively perfect at every integral level and in the inverse limit.
An explicit central cochain lifts the canonical negative action;
simultaneous linear equations and independent original group laws
verify the peripheral frame norms. ''' + integral_abstract + r'''
The action and frames have a full positive peripheral realization,
while its full negative square and cofinality remain undecided.
For the icosahedral problem, a common involution gives a faithful
colored eight-point ambient comparison. A decorated seven-point map
is faithful on the completed cyclic source. We determine the full
dihedral centralizer, its canonical direct-factor splitting, its
parameter orbifold, and its valid full profinite comparison.
The two discrete source groups have trivial intersection under every
ambient conjugation, but the corresponding completed intersection
and refined-product closure condition remain unresolved.
The full cyclic rigid map is noninjective; its completed kernel and
the exact common joint rigid/symplectic image are retained, with no
inference of a common full ambient lift.
We retain the regular-pants relative conjugacy, source audits, torus
and real-structure reductions, noncompact comparisons, and corrected
five-point census. Every numbered assertion has an explicit proof
status. A gap in a published proof is not a counterexample to its
theorem. This work is incomplete; no priority is claimed.'''
a, b = s.index('\\begin{abstract}'), s.index('\\end{abstract}')
paper.write_text(s[:a] + '\\begin{abstract}\n' + abstract + '\n' + s[b:])
print('Updated all49 task rows; both main decisions remain Open; '
      'all-integral scalar frames:', opts.all_integral_frames)
