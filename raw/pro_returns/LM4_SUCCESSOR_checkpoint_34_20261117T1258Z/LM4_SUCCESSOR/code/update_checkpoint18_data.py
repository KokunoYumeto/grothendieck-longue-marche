"""Integrate the four exact transported-module results without closing a task."""
from pathlib import Path
from collections import Counter
import csv
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
inputs = [
    'work_A/B93_intrinsic_seed_module.tex',
    'work_A/B94_retained_deck_module.tex',
    'work_DE/B95_old_zero_overlap.tex',
    'work_CE/B96_old_translate_cohomology.tex',
]
part = root / 'sections/part_B.tex'
s = part.read_text()
for rel in inputs:
    assert (root / rel).exists(), rel
    line = '\\input{' + rel + '}'
    assert line not in s, ('Already integrated', rel)
    s += line + '\n'
part.write_text(s)
subprocess.run([sys.executable, str(root/'code/assemble_register.py')], check=True)
rows = list(csv.DictReader((root/'LM4_SUCCESSOR_results.csv').open()))
assert len(rows) == 265
assert dict(Counter(r['status'] for r in rows)) == {
    'Known': 6, 'Proved': 223, 'Refuted': 17, 'Open': 19}
assert all(next(r for r in rows if r['id'] == sid)['status'] == 'Proved'
           for sid in ('B.93', 'B.94', 'B.95', 'B.96'))

path = root/'task_coverage.csv'
with path.open() as stream:
    reader = csv.DictReader(stream)
    fields, coverage = reader.fieldnames, list(reader)
assert len(coverage) == 49
index = {r['task']: r for r in coverage}
addition = (
    'B93 computes the entire seed/F-image module over Z[R times R]. '
    'B94 proves independence over the full generic-fiber quotient group ring '
    'and determines its involution cohomology. B95 determines the exact '
    'intersection with one old-zero translate and its zero excess Tate image. '
    'B96 treats every individual old-base translate uniformly: each has '
    'source-ideal Tate image, and their individual images sum exactly to J_I. '
    'All additional values are isolated in the H2 of the actual orbit-sum kernel.'
)
for task in ('B.4', 'B.4.a', 'B.4.b', 'B.4.c', 'B.4.h'):
    row = index[task]
    assert row['outcome'] == 'Open'
    for sid in ('B.93', 'B.94', 'B.95', 'B.96'):
        assert sid not in row['statement_ids'].split(';')
        row['statement_ids'] += ';' + sid
    row['state'] += ' ' + addition
    row['obstruction'] = (
        'The complete generic-fiber coefficient block and every individual '
        'old-base translate contribute only J_I. B96 identifies the remaining '
        'intrinsic excess U/J_I with the image of H2(C2,K_old), where K_old is '
        'the kernel of the actual direct-sum-of-translates map to Lbar. '
        'Intersections with the whole preceding sum, or the equivalent '
        'full-column action of exact augmented-row stabilizers, remain '
        'undetermined. Pairwise overlap data and augmentation-adic source '
        'approximations do not settle this map. The nonlinear kernel [M,M], '
        'full compact coefficient comparison, projected fixed-source equality, '
        'whole source-kernel normality and subsequent joint-source condition '
        'remain Open.'
    )
    row['next_step'] = (
        'Determine the exact all-word row stabilizers in the actual filled '
        'free-by-free group and their full transported-column action, or '
        'compute the whole-overlap cohomology with a certified source-coset '
        'value. Use the proved two-coset reduction for individual translates; '
        'do not replace full overlap control by finite depth stabilization. '
        'Then address nonlinear fixed lifting, actual compact comparison, '
        'projected-source equality and the separate joint-source gate.'
    )
with path.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(coverage)

paper = root/'LM4_SUCCESSOR_paper.tex'
s = paper.read_text()
old = '''diagonal Tate obstruction criterion. Equivariant node paths identify
the source-ideal contribution and isolate the residual syzygy map.
That map, deeper nonabelian lifting, projected fixed-source equality,
and the subsequent joint-source condition remain unresolved.'''
new = '''diagonal Tate obstruction criterion. We compute the full generic-fiber
coefficient block, one exact old-base overlap, and every individual
old-base translate. Their individual Tate images sum exactly to the
source ideal. All additional values lie in the cohomology of the kernel
of the orbit-sum map. That overlap contribution, deeper nonabelian
lifting, projected fixed-source equality and the subsequent joint-source
condition remain unresolved.'''
assert old in s
paper.write_text(s.replace(old, new, 1))

report = root/'LM4_SUCCESSOR_report.md'
s = report.read_text()
assert s.splitlines()[0] == 'INCOMPLETE'
marker = '## Eighteenth-hour research: complete individual transported modules'
assert marker not in s
s += '''\n## Eighteenth-hour research: complete individual transported modules

B93 replaces the bounded integer anti-chain tests by an exact computation
over the full noncommutative group ring Z[E], E=R times R. Its128 actual
seed and F-image columns have a free image of rank116 and a free kernel
of rank12. The proof retains106 reversible group-unit pivots and ten
private binomial rows whose finite-support injectivity is proved directly.
The literal involution has56 paired image generators and four negative
fixed generators. Their full cohomology image is precisely the left ideal
generated by the four first-sheet source differences. An induced common
refinement also gives a rigorous comparison with B92's original kernel.

B94 allows every element of the actual generic-fiber quotient G as a
coefficient. The64 nodal columns are free over Z[G]. A selected diagonal
minor is a signed group-unit matrix after E-augmentation; a separated
augmentation filtration proves injectivity without inverting that matrix.
The separation proof is complete, including finite2-group quotients and
integral coefficients. The actual F matching and its cone classes give
four source cohomology generators and zero H2. Magnus1935 was opened in
its original scan at the relevant argument and its publisher metadata
was verified; the paper cites it for context and gives its own required
proof. The bibliography now contains105 records with explicit status.

B95 computes the exact first old-zero overlap over that full group ring.
Four literal word/G-unit identities account for every augmented-row
coincidence. The intersection is free of rank4, the sum is free of
rank124, and the overlap consists of two exchanged F-pairs. Therefore
its positive involution cohomology vanishes and the sum adds no value
outside J_I. The translated module is not contained in the original one.
The induced action on the Tate target is justified by naturality of
right defects, without assuming that monodromy preserves the chosen
free factors literally. No higher iterate is inferred from this result.

B96 treats every old-base word by the actual two-sheeted source cover.
Its eleven returned operators commute with F and preserve I. Exact
full-word odd-sheet computations supply the four second-sheet source
classes, with push/pull and branch-square directions retained. Every
individual old-base translate has H1 isomorphic to F2[R]^4, H2 zero,
and Tate image inside J_I. The sum of all individual images is exactly
J_I because these are the actual eight peripheral source orbits. The
direct sum of the translated modules maps onto the full relation image;
the H2 of its actual kernel carries a canonical residual map with image
exactly U/J_I. This kernel is not identified with B92's differently
marked kernel. Pairwise intersections do not control intersections with
the whole preceding sum. The residual map remains undetermined.

All four proofs were read completely by root and independent reviewers,
and their finite input calculations have separately written checkers.
Component and combined typesetting records are retained separately.
The integrated register has265 statements:223 Proved,17 Refuted,19 Open
and6 Known. All49 task and lead rows remain. Neither main full decision
is closed. The next exact gate is the action of all old-base row
stabilizers on the full columns, or equivalent whole-overlap cohomology.
The nonlinear, compact, projected-source and joint-source comparisons
remain separate requirements. The research record and proof reviews
are in records/eighteenth_hour_research_report.md and
records/transported_module_root_review_18h.md.
'''
report.write_text(s)
subprocess.run([sys.executable, str(root/'code/update_checkpoint_report.py')], check=True)
print('Integrated B93--B96:265 statements;105 bibliography entries;49 task rows.')
