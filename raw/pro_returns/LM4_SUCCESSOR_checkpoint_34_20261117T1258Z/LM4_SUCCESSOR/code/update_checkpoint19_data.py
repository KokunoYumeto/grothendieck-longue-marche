"""Integrate the four reviewed main-B results; retain all full-task Open rows."""
from pathlib import Path
from collections import Counter
import csv
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
inputs = [
    'sections/b_cross_sheet_block.tex',
    'sections/b_coefficient_domain_counterexample.tex',
    'work_CE/B99_section_head_kernel.tex',
    'sections/b_symmetric_nonasphericity.tex',
]
part = root/'sections/part_B.tex'
s = part.read_text()
for rel in inputs:
    assert (root/rel).exists(), rel
    line = '\\input{' + rel + '}'
    assert line not in s, ('Already integrated', rel)
    s += line + '\n'
part.write_text(s)
subprocess.run([sys.executable, str(root/'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 269
assert dict(Counter(r['status'] for r in rows)) == {
    'Known':6, 'Proved':225, 'Refuted':19, 'Open':19}
for sid, status in [('B.97','Proved'), ('B.98','Refuted'),
                    ('B.99','Proved'), ('B.100','Refuted')]:
    assert next(r for r in rows if r['id'] == sid)['status'] == status

path = root/'task_coverage.csv'
with path.open() as stream:
    reader = csv.DictReader(stream)
    fields, coverage = reader.fieldnames, list(reader)
assert len(coverage) == 49
index = {r['task']:r for r in coverage}
addition = (
    'B97 proves the exact rank128 two-sheet block and its full source orbit. '
    'B98 proves a domain theorem for the actual integral coefficient ring and '
    'refutes the augmented-row-to-group-unit shortcut on complete actual words. '
    'B99 determines the entire selected head-kernel/row stabilizer by a '
    'two-operator orbit-normal-closure presentation. B100 proves an actual '
    'Z3 retract and a nonzero torus attaching sphere in the symmetric '
    'surface, refuting its proposed asphericity.'
)
for task in ('B.4','B.4.a','B.4.b','B.4.c','B.4.h'):
    row = index[task]
    assert row['outcome'] == 'Open'
    for sid in ('B.97','B.98','B.99','B.100'):
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';' + sid
    row['state'] += ' ' + addition
    row['obstruction'] = (
        'The exact selected all-word augmented-row stabilizer is known, but '
        'its full-column action and intersections with the entire preceding '
        'source-orbit sum remain undetermined. Actual zero-head operators can '
        'send a column to one independent over all Z[G], so augmented row '
        'equality does not imply a full relation. The symmetric surface is '
        'provably nonaspherical; a contractible-cover shortcut is false. '
        'Neither its nonzero sphere nor an ordinary Brown--Loday coinvariant '
        'calculation determines the full E-coefficient obstruction. The '
        'residual image U/J_I, nonlinear kernel [M,M], actual compact '
        'coefficient comparison, projected fixed-source equality and the '
        'subsequent joint-source condition remain Open.'
    )
    row['next_step'] = (
        'Transport the exact constant-section kernel presentation to the '
        'other diagonal slots with actual bridges; determine the full-column '
        'action of these stabilizers or the cohomology of whole preceding '
        'sums. Construct the actual equivariant two-complex/E-cover comparison '
        'before using geometric homology in the syzygy map. Preserve all '
        'coefficients and do not infer kappa vanishing from fixed-locus '
        'dimension or bounded/augmentation-adic tests. Then address the '
        'separate nonlinear, compact and joint-source steps.'
    )
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(coverage)

paper = root/'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
old = '''source ideal. All additional values lie in the cohomology of the kernel
of the orbit-sum map. That overlap contribution, deeper nonabelian
lifting, projected fixed-source equality and the subsequent joint-source
condition remain unresolved.'''
new = '''source ideal. The two source sheets form a free rank-128 block.
An exact two-operator presentation determines one entire transported-row
stabilizer, while actual complete words refute a proposed passage from
equal augmented rows to full-column relations. The symmetric complement
has an explicit $\\mathbb Z^3$ retract and a nonzero torus attaching sphere,
so it is not aspherical. All additional Tate values still lie in the
cohomology of the kernel of the orbit-sum map. That overlap contribution,
deeper nonabelian lifting, projected fixed-source equality and the
subsequent joint-source condition remain unresolved.'''
assert old in s
paper.write_text(s.replace(old,new,1))

report = root/'LM4_SUCCESSOR_report.md'
s = report.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '## Nineteenth-hour research: exact stabilizer and a nonaspherical surface'
assert marker not in s
s += '''\n## Nineteenth-hour research: exact stabilizer and a nonaspherical surface

B97 proves that the two actual source-sheet blocks are a direct sum of
rank128 over the full integral group ring. Its parity proof concerns
the E-augmented rows only; the complete columns themselves can contain
both parities. The separated augmentation filtration proves independence
without a matrix inverse. The full positive involution cohomology has
eight source generators and zero H2. All returned-source translates of
this two-sheet block generate the actual full relation module, and the
sum of their individual cohomology images is exactly J_I. No assertion
about overlaps of those further translates is inferred.

B98 supplies an explicit embedding of the actual coefficient group in
F13 times F13, with the required beta twist retained. A complete Magnus
bi-order argument proves its integral group ring has no zero divisors.
The actual old-zeta action on node(16,1) gives a complete counterexample
to the proposed augmented-row shortcut: the original column has one
term, its592-letter transported relator has a553-term chain, and a
specified factored coefficient in a new row is exactly minus one.
Independent opposite-edge reconstruction checks the whole chain and the
literal printed conjugators. All16 matching zero-head column pairs are
independent over the whole ring. Their two-column cohomology is fully
determined, but the surrounding64-column intersections remain distinct
questions. Kim and Rolfsen2003 was opened at the complete order proof;
the exact group embedding and domain argument needed here are supplied.

B99 determines a whole actual augmented-row stabilizer, without a word
length bound. Fill the four inactive q-root fibers to obtain X0 and
project X0 to v. The sole allowed finite collision is at v=-1, where
the q punctures1 and v squared meet. A global continuous far section
extends across it. The generic F4 kernel is the normal closure of the
actual commutator[c,d] under two explicitly computed operators and their
inverses. Its pullback under the literal old six-generator filling
(b,d,1,a,1,c) is exactly the selected head kernel and diagonal-row
stabilizer. All17 path segments and both compact operator forms have
independent exact checks. The cyclotomic deformation margins and the
empty original-source connector are explicit. The proof distinguishes
the injective unfilled constant section from its kernel after filling.

B100 refutes asphericity of the actual symmetric complement Z itself.
The actual node(6,3) commutes a=p2 with b=p12 p13 p12 inverse, and
the actual old0 far lift t fixes both literally. The three global units
v-zeta, vw+(zeta^4-1)v-zeta^4, and q=vw have winding matrix I3 on(a,b,t).
They therefore exhibit a split Z3 subgroup of pi1(Z). The complement
embeds as the closed smooth surface sD(v,w)=1 in C3. Milnor1963,
Theorems7.1--7.2, was opened and its full proof on printed39--41 was
read in text and actually inspected in the rendered original scan.
It gives a two-dimensional CW homotopy type. The three commuting loops
and any three commutator nullhomotopies define a map of the2-skeleton
of the3-torus. Its remaining attaching sphere cannot be null: an
extension would give a map through Z inducing degree one on H3 of the
torus, whereas H3(Z)=0. This is an actual nonzero pi2 class.

The old aspherical spaces X,Y,V used in B89 are unaffected. No geometric
sphere is silently identified with B92's particular syzygy kernel.
Ordinary Brown--Loday tensor-kernel calculations discard the E action
needed by the actual obstruction, and the geometric-to-presentation
comparison is still under investigation. The nonzero sphere by itself
does not prove a nonzero kappa value or decide the original centralizer.

All four complete proofs have independent reviews. The integrated
register has269 statements:225 Proved,19 Refuted,19 Open and6 Known.
All49 task and lead rows remain. Both main full decisions stay Open.
The selected all-word stabilizer is now determined; its action on full
columns, all whole-sum overlaps, the nonlinear fixed-lifting problem,
the compact coefficient comparison and the final joint-source condition
remain separate gates. The next research combines the exact geometric
stabilizer presentation with actual equivariant cover topology. Main A
remains at full marked generation and its actual Fox-unit criterion.
'''
report.write_text(s)
subprocess.run([sys.executable,str(root/'code/update_checkpoint_report.py')],check=True)
print('Integrated B97--B100:269 statements,49 task rows; both main decisions Open.')
