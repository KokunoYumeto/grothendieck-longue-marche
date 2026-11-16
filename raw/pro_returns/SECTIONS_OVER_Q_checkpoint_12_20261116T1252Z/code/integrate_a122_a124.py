#!/usr/bin/env python3
"""Integrate the fully audited cyclic-image and ray-at-three theorems."""
from pathlib import Path
import datetime
import json
import subprocess

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p = w / 'SECTIONS_OVER_Q_paper.tex'
s = p.read_text()
for anchor, entry in [
    (r'\input{sections/eighth_common_field.tex}',
     r'\input{sections/relative_cyclic_repair_agent.tex}'),
    (r'\input{sections/harmonic_eighth_full_initialization.tex}',
     r'\input{sections/ray_three_intersection_agent.tex}')]:
    assert anchor in s
    if entry not in s:
        s = s.replace(anchor, anchor + '\n' + entry, 1)
p.write_text(s)

p = w / 'notes/register_metadata.json'
meta = json.loads(p.read_text())
meta['A.122'] = {
    'answers': 'A5; A9; A15; L10; L14; L20',
    'depends_on': 'A.109; A.115; A.117; exact Poitou–Tate support annihilators; Schmidt–Wingberg Theorem13',
    'uses_local_theorem': 'no; actual relative norm module and primary published cohomological theorems',
    'manuscript_passages': 'cote149; scans56–58,126–127; global relative norm repair with cyclic auxiliary Kummer images',
    'notes': 'Computes the exact old-local image of mod-three classes whose new ramification splits any prescribed finite Galois field and has cyclic image. It is the unrestricted constrained-support image cut out by all equivariant alternating reciprocity sums. A literal auxiliary cyclic generator makes the cocycle field disjoint over the splitting field; transported corestriction distributions and their full affine annihilator supply the exact input to Schmidt–Wingberg Theorem13. Actual local torus data yield a global relative norm-one element. The assertion retains mod-three precision and does not supply a compatible norm tower.'
}
meta['A.124'] = {
    'answers': 'A5; A9; A15; L10; L14; L20',
    'depends_on': 'A.99; A.100; A.101; A.105; actual ordinary permutation restriction embedding and scalar relative norm map',
    'uses_local_theorem': 'no; explicit finite Galois and local unit-group maps',
    'manuscript_passages': 'cote149; scans56–58,126–127; ray support repair preserving the actual lower norm chain',
    'notes': 'Proves that the normal closure of any abelian three-extension of the pure root field has trivial intersection with every deeper root step over the old normal field after cyclotomic base change. The kernel embeds in an ordinary permutation module; its translation invariants are fixed by complex conjugation, contradicting the inverted next cubic kernel. Thus the simultaneous splitting and Artin generators permit arbitrary ray depth at three while retaining the restriction away from two. At relative degree three an explicit scalar unit correction changes the finite-precision lower norm into exact equality, preserving divisors and arbitrarily deep local-three congruence. No new norm preimage or infinite compatibility is asserted.'
}
p.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')

p = w / 'SECTIONS_OVER_Q_report.md'
lines = p.read_text().splitlines()
items = {'A5', 'A9', 'A15', 'L10', 'L14', 'L20'}
detail = ('A.122 gives the exact mod-three cyclic auxiliary repair image through all relative alternating reciprocity sums. '
          'A.124 permits arbitrary ray precision at three and makes the existing cubic lower-norm transition exact by an explicit scalar correction. '
          'One compatible infinite norm chain remains unresolved.')
changed = 0
for i, line in enumerate(lines[:55]):
    if not line.startswith('| '):
        continue
    cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
    if len(cells) != 3 or cells[0] not in items:
        continue
    for identifier in ['A.122', 'A.124']:
        if identifier not in cells[1]:
            cells[1] += ', ' + identifier
    if detail not in cells[2]:
        cells[2] += ' ' + detail
    lines[i] = '| ' + ' | '.join(cells) + ' |'
    changed += 1
heading = '## Exact cyclic repair and ray conditions at three'
if heading not in lines:
    lines.extend(['', heading, '',
        stamp + ': A.122 identifies the complete old-local image of classes with cyclic new ramification at primes splitting a prescribed finite Galois field. The image consists exactly of the unrestricted constrained-support local image satisfying every alternating reciprocity sum. A new split prime with a cyclic module generator gives the literal direct-product field needed for the dual calculation. Distributing the unramified corrections among all conjugate primes yields the exact transported pairing, including its cyclotomic scalar. The full affine annihilator consists of all equivariant bilinear forms, which the actual relative module calculation proves alternating. Poitou–Tate then supplies the precise unramified input to Schmidt–Wingberg Theorem13. This gives actual global relative norm-one classes for local torus prescriptions. The statement is at mod-three precision; it does not assert higher-power or infinite norm compatibility.', '',
        'A.124 removes the restriction at three from the pure-radical intersection needed in the support repair. The actual restriction maps embed the abelian normal kernel in an ordinary permutation module. A power of a lift of the root translation is fixed by complex conjugation, whereas every nonzero next cubic kernel is inverted; this proves the intersection at every deeper level after cyclotomic base change. The simultaneous representative and boundary fields still require the ray modulus to avoid two, and now permit arbitrary depth at three. For an existing relative cubic norm chain, the displayed scalar unit correction turns the lower norm from a prescribed three-power unit error into exact equality. It retains the divisor and finite Kummer class, and the compact local unit power map preserves arbitrarily deep congruence at three. Existence of the next norm preimage and convergence of an infinite chain remain open.', ''])
p.write_text('\n'.join(lines) + '\n')

audits = [
    'A122 full saved-source audits passed root and local_preprint. Verified the generic restricted-support Poitou–Tate annihilator; auxiliary full cocycle image and literal field direct product; rational split-prime detection over the splitting field; transported corestriction and cyclotomic scalar; every affine annihilator and quadratic cross term; all hypotheses of the opened Schmidt–Wingberg Theorem13; actual torus Kummer realization. Root independently reran the certificate: complete dimensions at n1 and n2,6561 exhaustive first-depth affine systems and768 exact second-depth systems, all passed.',
    'A124 full saved-source audits passed root and local_preprint. Verified every restriction and coset-lift choice, ordinary permutation action with nontrivial original-field intersection, stable subgroup after cyclotomic base change, lift-power contradiction at every deeper step, retained away-two condition and simultaneous radical intersections, exact scalar lower-norm correction, unchanged divisors and Kummer classes, and the compact-injective local unit power inverse at three. Root reran the ray certificate:1089 fixed vectors,195 norm maps,1690 cyclotomic actions,45 lift powers and108 deeper inclusions, all passed.'
]
for name in ['notes/hour8_root_audits.md', 'notes/root_progress.md']:
    p = w / name
    s = p.read_text() if p.exists() else ''
    for audit in audits:
        if audit not in s:
            s += '\n' + stamp + ' ' + audit + '\n'
    p.write_text(s)

result = subprocess.run(['python', str(w / 'code/build_register.py')],
                        check=True, text=True, capture_output=True)
output = ('Integrated A122 between A121/A123 and A124 immediately after A123.\n'
          f'Updated {changed} parsed first-table outcome rows, exact metadata and both audit logs.\n'
          + result.stdout + 'No manuscript build was run. Both A1 assertions and the coherent infinite norm chain remain open.\n')
Path(__file__).with_name('integrate_a122_a124_output.txt').write_text(output)
print(output, end='')
