"""Idempotently record the fifth-hour scoped results without changing open decisions."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / 'task_coverage.csv'
with path.open() as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 49
index = {r['task']: r for r in rows}
formal_a = {r['id']: r['status'] for r in csv.DictReader((root/'work_A/A_results.csv').open())}
mixed = formal_a.get('A.49') == 'Proved'

def update(task, ids, state, obstruction=None, next_step=None, approaches=None):
    row = index[task]
    row['statement_ids'] = ids
    row['state'] = state
    for key, value in [('obstruction', obstruction), ('next_step', next_step), ('approaches', approaches)]:
        if value is not None:
            row[key] = value

tower = 'the regular perfect affine tripod refinements, orbit-one simple quotients, and their actual central refinements'
if mixed:
    tower += ', together with the explicit nonperfect mixed AGL1(F7) layer and its actual Clifford refinement'
tower_ids = 'A.40–A.41;A.43;A.47–A.48' + (';A.49' if mixed else '')
update('Lead 2', 'A.3;A.34;A.43;A.47–A.48' + (';A.49' if mixed else ''),
       'The closed-normal central-quotient lifting criterion is proved. Its actual refinement is identified and the required next scalar stage is controlled for the specified enlarged towers. No unrestricted finite-order lifting theorem is asserted.')
for task, prefix in [('Lead 3','A.12;A.16–A.35;'), ('A.5','A.7–A.8;A.12;A.23–A.35;'), ('A.6','A.13;A.19;A.25–A.35;')]:
    state = 'A single full parity-one negative element has compatible involutory images through the congruence tower and ' + tower + '. No cofinal family or full order-two lift is proved.'
    if task == 'A.5':
        state = 'The full cohomology set already has continuum cardinality among standard conjugates. ' + state
    if task == 'A.6':
        state += ' The full framed correction kernel contains Z2, and parity on all full involutions remains undecided.'
    update(task, prefix+tower_ids, state,
           'A general noncentral finite layer may have nontrivial retained head action; the full framed norm equation is unresolved.',
           'Treat a genuinely new finite head action or prove a cofinal extension theorem.',
           'Exact relative residual images; perfect and nonperfect finite kernels; actual central refinements; prescribed frames; compatible compact lift sets.')

generation = ('The canonical substitution is automorphic on every relative pro-p quotient over C2²; for GT0 involutions it also passes every A4 third-cusp test and is automorphic on the relative pro-two quotient over C3². These relative automorphisms are not asserted to preserve the full relative third cusp.')
update('A.3','A.4–A.8;A.15;A.37–A.39;A.42;A.44–A.46;C.29–C.36',
       'The prescribed multiplier-one third cusp is false. For a GT involution the canonical word satisfies the full pentagon and every maximal pro-p conjugacy test. Its universal-dihedral value defines a full unit d; only the global pair ±d can solve the full third cusp. ' + generation)
update('A.4','A.9–A.10;A.12;A.17;A.23–A.35;A.38;A.40–A.48;C.35–C.36'+(';A.49' if mixed else ''),
       'Odd-prime results and all maximal pro-p canonical GT conjugators are proved. The parity-one tower now includes '+tower+'. '+generation,
       'General relative dyadic peripheral conjugacy and cofinal marked conjugacy are still unproved.',
       'Compare the actual third-cusp equation at further mixed finite bases.')
update('A.7','A.11;A.22;A.27;A.29;A.37–A.39;A.42;A.44–A.46;C.29–C.36',
       'The all-level generation and reflection criteria are proved. The exact full conjugacy condition is now the third-cusp equation at the explicitly determined dihedral unit d (equivalently at -d). '+generation,
       '', 'Completed scoped criterion; universal existence remains task A.8.')
update('A.8','A.6;A.14;A.36–A.48;C.28–C.36'+(';A.49' if mixed else ''),
       'All three universal full involution-conjugacy decisions remain open. Every existing peripheral conjugator to a GT involution is in GT. The canonical word satisfies the pentagon, all maximal pro-p tests, the full A4 tests, and the stated relative generation results. Its dihedral unit d fixes the only possible multiplier pair. The enlarged parity-one tower remains noncofinal.',
       'The full third-cusp equation at d is unproved; all quotient involutions still need not give a full involution.',
       'Prove that fixed full equation or continue the parity-one construction through a cofinal family.',
       'Fixed associator; finite-cover boundary homology; integral Magnus identities; binary tetrahedral symmetry; relative Frattini modules; actual central refinements.')

class3 = ('Explicit distinct words in the two actual subgroups have the same nonzero class-three image, with degree-two coordinate5091840w, and this image dies in all twelve rigid-seven class-three tests. Their common completed quotient image contains Zhat; no full centralizer element is constructed.')
for task, ids in [
    ('B.4','B.7;B.18–B.35;B.42–B.61'),
    ('B.4.c','B.28;B.35;B.46–B.49;B.52;B.58–B.61'),
    ('B.4.h','B.20;B.40;B.42–B.45;B.54–B.55;B.58–B.61')]:
    start = ('K=1 remains undecided. The unrefined product, all abelian refinements, and the specified class-two refinements are closed. K has zero ambient abelianization and its class-two image lies on the primitive line Zhatw. ')
    if task == 'B.4.h':
        start = 'Universal braid-constrained R2 is false at U=K and prime7. The complete relative images, including at2,3,5, remain open. K has zero ambient abelianization and at most the indicated primitive class-two direction. '
    update(task, ids, start+class3,
           'Compatible class-three representatives do not give compatible representatives at every finite quotient or a full intersection element.',
           'Use a stronger finite quotient or a genuine all-level compatibility argument.',
           'Actual11-strand monodromy at a common algebraic marking; exact Magnus and BCH arithmetic; integral correction words; independent full-coordinate evaluation.')
update('B.4.a','B.13;B.19;B.56;B.58–B.61',
       'The actual thirteen-generator rigid monodromy and its discrete/completed-test kernels are determined as stated; their embedded-closure comparison remains open. '+class3,
       'The completed kernel need not be the embedded closure; vanishing in finite nilpotent truncations is not actual rigid-test vanishing.',
       'Control the full monodromy-image topology or find a nonnilpotent obstruction.')

assert index['A.8']['outcome'] == index['B.4']['outcome'] == 'Open'
with path.open('w') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print('Updated49 task rows; A49 included:', mixed, '; both main decisions remain Open')
