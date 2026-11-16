"""Integrate accepted post-checkpoint10 results without changing open outcomes."""
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
           ('A.70', 'A.71', 'A.72', 'A.73', 'A.74', 'A.75', 'A.76', 'B.75'))


def append(task, ids, marker, text, obstruction=None, next_step=None):
    row = index[task]
    for sid in ids:
        if sid not in row['statement_ids'].split(';'):
            row['statement_ids'] += ';' + sid
    row['state'] = row['state'].split(marker)[0] + marker + text
    if obstruction is not None:
        row['obstruction'] = obstruction
    if next_step is not None:
        row['next_step'] = next_step


mixed = (
    'The actual source now retains all32 mixed free/binary ordinary cups. '
    'Their negative action and normalizer frames are constructed, including '
    'an explicit repair of a nonzero initial square in the regular half. '
    'The exact new scalar refinement is C2^576; with the retained128 '
    'directions its full scalar third subgroup has dimension704. The next '
    'scalar refinement is relatively perfect, with compatible integral '
    'transitions and earlier distinct-type families. A2631-variable '
    'rank890 system now solves the actual new576 action and simultaneous '
    'frame equations. The original704, independent full20 and independent '
    'all-free128 group laws verify the witness and common projections. '
    'Six exact constraints retain the forced integral halves; binary '
    'changes lift constantly. A full positive peripheral automorphism '
    'realizes the selected entire tower, with its literal initialC '
    'frames and older families. Discretionary higher old frames may '
    'change. Its full negative square and cofinality are still unproved. '
    'For the original stored A56 finite action and frame, every full '
    'positive lift fixing the cusp literally has a non-involutory '
    'negative companion. An actual finite source-central refinement '
    'nevertheless has the prescribed negative involution and both '
    'norm-one frames. The six-cup quotient is forced for every full '
    'candidate by transgression, and its exhaustive norm invariant '
    'excludes the original prescribed frame. Later reselected tuples '
    'are outside this obstruction.'
)
obstruction_a = (
    'A cofinal quotient construction and the full negative square '
    'remain unresolved for the reselected A75 tuple. The original '
    'A56 prescribed-frame tuple is excluded by A76, which does not '
    'exclude all possible frames. The '
    'mixed-multiplier actual central counterexample rules out an '
    'unrestricted equivariant central-lifting shortcut, but does not '
    'decide the required global-multiplier involution problem.'
)
next_a = (
    'Attack a correctly scoped equivariant embedding theorem or a '
    'genuinely noncentral source obstruction that can control arbitrary '
    'heads and cofinality. Preserve existential frame choice and all '
    'literal initial constraints; arbitrary prescribed equivariant '
    'conjugator lifting is false even on the actual central refinement.'
)
for task in ('Lead 3', 'A.4', 'A.5', 'A.6', 'A.8'):
    append(task, ['A.70', 'A.71', 'A.72', 'A.73', 'A.74', 'A.75', 'A.76'],
           ' Mixed ordinary refinement: ', mixed, obstruction_a, next_a)
append('Lead 2', ['A.70', 'A.72', 'A.73', 'A.74', 'A.75', 'A.76'],
       ' Equivariance scope after the mixed refinement: ',
       'The ordinary central-quotient lifting criterion remains proved. '
       'An exact13824-element actual source-central model disproves its '
       'unrestricted equivariant peripheral extension for mixed '
       'multipliers, even allowing a full lift of infinite order. A '
       'multiplier-one variant between different full actions is kept '
       'distinct from the same-action restriction. A separate binary '
       'icosahedral example disproves same-action multiplier-one '
       'equivariant lifting with prescribed conjugator frames, even '
       'with norm one and on the entire actual orientation-central '
       'refinement. Frame freedom and negative-cocycle existence are '
       'not refuted. The actual mixed source has exact576 new scalar '
       'directions, stable next refinement, and now a fully solved '
       'selected action/frame family throughout the integral tower. '
       'A76 further refutes normalized global-negative order preservation '
       'with the original prescribed finite action and frame, although '
       'the actual finite source-central refinement and both local '
       'normalizer norms pass. It leaves existential frame selection open.',
       '', next_a)
append('A.7', ['A.70', 'A.71', 'A.74'],
       ' Full-source comparison tests: ',
       'The mixed-multiplier example has actual three-reflection source '
       'and complete central data, but no full equivariant peripheral '
       'lift. Every full peripheral automorphism of multiplier+1 or-1 '
       'preserves every residually absolutely irreducible SL2 coefficient '
       'kernel and acts on it by a GL2 conjugation. These tests do not '
       'supply full source generation. The norm-compatible prescribed '
       'frame counterexample is an actual failure of centralizer/frame '
       'lifting; it leaves freely selectable frames and the negative '
       'cocycle problem untouched.')

birman = (
    'An actual index-five C2*F3 source contains a section of the '
    'four-moving-point Birman extension. Its full completed kernel has '
    'the correct induced topology. The commutator with the second '
    'tetrahedral involution is a nonabelian cocycle whose exact completed '
    'zero set is the residual icosahedral centralizer. Triviality is '
    'equivalent to a uniform characteristic finite-cover condition. '
    'The cocycle is discretely injective, but this does not prove the '
    'uniform condition. The formulation is compared explicitly with '
    'the prior LM4 F.14-F.15 interaction-cocycle results.'
)
for task in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
    append(task, ['B.75'], ' Exact split Birman formulation: ', birman,
           'The uniform finite-cover separation condition for the '
           'actual Birman cocycle, equivalently the full source-closure '
           'intersection, remains open. Solved abstract cocycle '
           'corrections and proper forgetting images do not establish '
           'membership in the drilled source.',
           'Use the actual reconstructed marginal braid words and '
           'monodromy to prove or refute source membership, then '
           'address the joint interaction kernel; alternatively prove '
           'the exact uniform finite-cover condition of B.75.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

paper = root / 'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
abstract = r'''We study involutions of the full profinite three-cusp group and
the icosahedral centralizer in the full profinite mapping class group.
Both universal full decisions remain open.
The constructed integral quotient retains all free-cusp cubic terms
and all mixed free/binary ordinary cups. We determine its actual new
scalar kernel, of dimension 576, and its total scalar third subgroup,
of dimension 704. Its next scalar refinement is relatively perfect.
An explicit simultaneous system solves the mixed scalar action and
frame equations. Independent original group laws verify the witness,
and six exact constraints preserve its integral compatibility.
A full positive peripheral automorphism realizes the selected tower;
its full negative square and cofinality remain unresolved.
For the original stored finite action and cusp frame, however, every
full normalized positive lift has a non-involutory negative companion.
The actual finite source-central refinement and both local norm tests
pass, but a forced six-cup quotient obstructs full order preservation.
This conclusion keeps the prescribed-frame restriction explicit.
An exact finite source-central counterexample excludes unrestricted
equivariant peripheral lifting for mixed multipliers. A separate
binary icosahedral example excludes arbitrary prescribed equivariant
conjugator frames even with multiplier one and quotient norm one.
It does not exclude existential frame selection. A classical
three-trace argument, with finite-ring and inverse-limit proofs,
controls every residually irreducible rank-two matrix quotient for
the global multipliers (+1) and (-1).
For the icosahedral problem, faithful colored eight-point and decorated
seven-point comparisons retain the actual full sources. We determine
the full dihedral centralizer and its valid profinite comparison.
A split four-moving-point Birman model gives a nonabelian cocycle
whose exact completed zero set is the residual centralizer. Its
uniform finite-cover condition remains open. We distinguish this
condition from pointwise residual finiteness and from the abstract
interaction-cocycle solutions already present in the attached LM4.
The paper retains the earlier source audits, exact rigid kernels,
regular-pants comparison, torus and real-structure reductions,
noncompact comparisons, and corrected five-point census.
Every assertion has an explicit proof status. A gap in a published
proof is not a counterexample to its theorem. This work is incomplete;
no priority is claimed.'''
a, b = s.index('\\begin{abstract}'), s.index('\\end{abstract}')
paper.write_text(s[:a] + '\\begin{abstract}\n' + abstract + '\n' + s[b:])
print('Updated49 task rows with A70-A76 and B75; both main decisions remain Open.')
