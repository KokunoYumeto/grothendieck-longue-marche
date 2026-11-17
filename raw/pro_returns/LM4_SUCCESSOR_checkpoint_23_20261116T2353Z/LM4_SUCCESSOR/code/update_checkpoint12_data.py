"""Integrate the reviewed twelfth-hour results; preserve every task outcome."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root / 'task_coverage.csv'
with path.open() as stream:
    reader = csv.DictReader(stream)
    fields, rows = reader.fieldnames, list(reader)
assert len(rows) == 49
index = {row['task']: row for row in rows}
formal = {row['id']: row['status'] for row in csv.DictReader(
    (root / 'LM4_SUCCESSOR_results.csv').open())}
assert all(formal.get(sid) == 'Proved' for sid in
           ('A.77', 'A.78', 'B.77', 'B.78'))
assert formal['B.76'] == 'Refuted'


def update(task, ids, state=None, obstruction=None, next_step=None):
    row = index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';' + sid
    if state is not None:
        row['state'] = state
    if obstruction is not None:
        row['obstruction'] = obstruction
    if next_step is not None:
        row['next_step'] = next_step


a_current = (
    'The selected integral construction retains all free-cusp cubic and '
    'mixed free/binary ordinary cups, with a 704-dimensional scalar third '
    'subgroup and relatively perfect next scalar refinement. The actual '
    'action and both frame norms are solved compatibly; a full positive '
    'peripheral automorphism realizes the selected tower. Its full '
    'negative square and cofinality remain unproved. The original A56 '
    'finite action with its prescribed s-frame is excluded by A76. A77 '
    'detects that failure in one actual finite noncentral relation-module '
    'quotient, although every iterated scalar refinement still passes. '
    'A78 keeps the original action fixed and reselects its frame to pass '
    'the six-cup test, verified independently. Thus the original '
    'prescribed-frame obstruction does not exclude every frame.'
)
a_obstruction = (
    'No cofinal compatible negative involution has been constructed, '
    'and no obstruction excludes every allowed frame/action at a '
    'sufficient full finite head. The six-cup obstruction is restricted '
    'to the original prescribed frame; the original action itself '
    'admits a different frame at that gate. Neither the global '
    'c-invariant Z4 lift of delta nor full peripheral reflection '
    'recognition has been decided.'
)
a_next = (
    'Control actual involutory actions on full finite relation modules '
    'with free choice of frames, or prove the full marked reflection '
    'recognition theorem. Do not substitute another scalar tower or '
    'one-prime family for cofinal full-source generation.'
)
prefixes = {
    'Lead 3': 'The full parity-one involution remains undecided. ',
    'A.4': 'The arbitrary dyadic and mixed-level classification remains open. ',
    'A.5': 'The full pointed cohomology set and involution conjugacy classes remain undetermined. ',
    'A.6': 'The parity of all full involutions in GT0 and GT remains undecided. ',
    'A.8': 'The full involution-conjugacy decisions for P, GT0, and GT remain Open. ',
}
for task, prefix in prefixes.items():
    update(task, ['A.77', 'A.78'], prefix + a_current,
           a_obstruction, a_next)
update('Lead 2', ['A.77', 'A.78'],
       'The ordinary closed-normal central-quotient lifting criterion is '
       'proved. Its unrestricted equivariant versions are false: the '
       'actual mixed-multiplier source and the multiplier-one prescribed '
       'binary-icosahedral frame give distinct counterexamples. A76 '
       'further excludes global negative order for one specified finite '
       'action/frame although its finite source-central refinement and '
       'both local norms pass. A77 detects that obstruction in one '
       'finite noncentral relation module while every scalar iteration '
       'passes. A78 retains the original action but chooses a different '
       'frame passing the six-cup gate. Existential negative-action '
       'lifting remains open; ordinary positive lifting is not refuted.',
       '', a_next)
update('A.7', ['A.77'],
       index['A.7']['state'].split(' Finite relation-module extraction: ')[0] +
       ' Finite relation-module extraction: A77 proves exact finite '
       's- and r-centralizer images over any finite head injecting the '
       'two cyclic factors. It extracts the unique normalized finite '
       'frames when an involutory action preserving the head exists; '
       'it does not supply that action or full peripheral generation.')

b_current = (
    'The faithful colored eight-point and decorated seven-point '
    'comparisons and split Birman cocycle retain the actual full '
    'sources. The completed cocycle zero set is exactly the residual '
    'centralizer; its uniform finite-cover condition remains open. '
    'B76 refutes a proposed general relative special-fiber shortcut '
    'by an explicit product-chart example with finite S3 x S3 '
    'separation. B77 shows that the four actual missing-meridian '
    'triples alone fail to normalize the whole source kernel, with '
    'an S4 certificate; actual additional monodromies exclude this '
    'partial certificate. B78 gives the complete based 20-strand '
    'pencil presentation with all 31 lassos, 29 filled values, and '
    'the two finite-cover kernel comparisons. Equality of the actual '
    'closed kernel images is exactly the remaining uniform '
    'b-normality condition. That condition and the later joint-source '
    'comparison remain unresolved.'
)
b_obstruction = (
    'The actual closed source-kernel image must be normalized by the '
    'missing retained meridian under the complete presentation. '
    'Normalizing only eight peripheral generators or four pair '
    'subgroups is insufficient. Even a marginal solution must then '
    'pass the joint interaction-kernel/source-membership gate.'
)
b_next = (
    'Use all 29 actual filled relations, with the retained base actions '
    'and the common marking, to prove uniform kernel normality or '
    'produce a finite quotient separating an actual conjugate. Keep '
    'the finite covers and actual completion images throughout; then '
    'address the joint interaction kernel or the equivalent uniform '
    'finite-cover condition of B75.'
)
for task in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
    update(task, ['B.76', 'B.77', 'B.78'], b_current,
           b_obstruction, b_next)
update('B.6', [],
       index['B.6']['state'].split(' Grothendieck-pair audit: ')[0] +
       ' Grothendieck-pair audit: the bounded primary-source search '
       'has not supplied a counterexample satisfying all goodness and '
       'cohomological finiteness hypotheses. The free-by-free examples '
       'with larger completed cohomological dimension fail goodness; '
       'no generic separability failure is promoted to a counterexample.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both main full decisions remain open.
For the involution problem, we construct an integral quotient retaining
all free-cusp cubic terms and mixed free/binary ordinary cups. Its
704-dimensional scalar third subgroup, the stable next refinement,
and compatible action and frame equations are determined explicitly.
A full positive peripheral automorphism realizes the selected tower;
its full negative square and cofinality remain unresolved.
The original prescribed finite action and frame have a genuine
obstruction to global negative order preservation. One actual finite
noncentral relation module detects this obstruction, although every
iterated scalar refinement passes. Keeping that original action but
reselecting its finite frame does pass the six-cup gate. We therefore
retain the distinction between a prescribed-frame counterexample and
an obstruction to every possible full involution.
Separate finite examples delimit equivariant central lifting, and a
three-trace argument controls residually irreducible rank-two quotients
without claiming full-source detection.
For the icosahedral problem, faithful colored configuration comparisons
and an actual split Birman extension give a nonabelian cocycle whose
completed zero set is the residual centralizer. We now compute a
complete common-based twenty-strand pencil presentation for an actual
marginal source: thirty-one lassos include all twenty-nine filled
critical values and both retained base actions. Exact rational
certificates establish the braid words and the finite-cover comparisons.
An explicit example refutes a general special-fiber shortcut. A separate
finite certificate shows that four local triple relations alone do not
give uniform source-kernel normality; additional actual monodromies
exclude that partial certificate. Uniform normality under the complete
presentation and the joint-source comparison remain open.
The paper retains the published-proof audits, rigid-kernel and torus
results, real-structure reductions, noncompact comparisons, and
corrected five-point census. Every assertion has an explicit proof
status. A gap in a published proof is not a counterexample to its
theorem. This work is incomplete; no priority is claimed.'''
a, b = s.index('\\begin{abstract}'), s.index('\\end{abstract}')
paper.write_text(s[:a] + '\\begin{abstract}\n' + abstract + '\n' + s[b:])
print('Updated49 task rows and abstract with A77-A78 and B76-B78; main decisions Open.')
