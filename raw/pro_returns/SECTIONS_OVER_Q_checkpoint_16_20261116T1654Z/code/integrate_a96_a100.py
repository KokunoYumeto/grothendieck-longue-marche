#!/usr/bin/env python3
"""Integrate the five independently audited sixth-hour results."""
from pathlib import Path
import datetime
import json

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
entries = {
    'A.96': {
        'file': 'quartic_tripod_initialization_agent.tex',
        'answers': 'A9; A12; L2',
        'depends_on': 'A.57; A.80; A.85; exact quartic root stabilizers and quadratic norm identities',
        'notes': 'Computes the common abelian field for arbitrary quartic radicands as the individual square-root field enlarged by sqrt(2r) for negative-square subset products -r^2. With two old finite coordinates every resulting cyclic class is explicitly constant. Thus a new puncture can be initialized at exponent four while lifting one prescribed ordinary point at each place of any finite set. No higher-exponent constancy or preservation of an infinite prescribed collection is asserted.',
        'uses_local_theorem': 'no; finite Galois equations, explicit norms, reciprocity and the A85 local-cover construction',
        'manuscript_passages': 'cote149; scans56–58,79–85; L2 puncture enlargement',
    },
    'A.97': {
        'file': 'own_coefficient_rigidity.tex',
        'answers': 'A5; A7; L9; L15',
        'depends_on': 'A.2; A.14; A.37; A.56; A.76; exact local primary-completion kernels and global valuation map',
        'notes': 'At a physical prime p, the own-p coefficient equalities of an ordinary pair with a rational pair already force equality of the local point, by an actual cyclotomic embedding and a norm identity on the complex unit circle. Density-one ordinary comparison fixes both completed global classes. One unchanged global coefficient component fixes an everywhere ordinary completed pair. A different labeled realized Selmer section differs on a nonempty Chebotarev class of global coefficient primes. The fixed-global-coefficient assertion retains all-place ordinariness; no passage from the finite H abelianization to that assertion is assumed.',
        'uses_local_theorem': 'no; ordinariness or the explicitly stipulated Selmer realization hypotheses are retained',
        'manuscript_passages': 'cote149; scans54–58; L9 and L15 coefficient and congruence comparisons',
    },
    'A.98': {
        'file': 'norm_representative_obstruction.tex',
        'answers': 'A5; A15; L10; L14',
        'depends_on': 'A.77; A.86; explicit field norms and the three Q61 factors of Q(cuberoot(3))',
        'notes': 'The element beta=(1-alpha)(4-alpha)^3/61, alpha^3=3, has norm -2 and valuations (2,-1,-1) at the three primes above61. Its completed class does not extend under the next cubic norm, even after the stated rational coefficient changes by61-units. Both norm fibres are nonempty and the family 1-3^(1/3^n) is compatible at every level. Hence this is an obstruction to the arbitrary representative recursion, while that rational pair has an explicit coherent family.',
        'uses_local_theorem': 'no; actual field inclusions, continuous completed norms and finite residue computations',
        'manuscript_passages': 'cote149; scans56–58,79–85; L10 and L14 norm compatibility',
    },
    'A.99': {
        'file': 'norm_ray_support_repair_agent.tex',
        'answers': 'A5; A15; L10; L14',
        'depends_on': 'A.92; A.95; Milne CFT V Theorems3.5–3.6; primary ray classes and exact norm-one squaring',
        'notes': 'At every specified finite odd-primary precision, an actual norm representative can be modified with exact rational norm unchanged and arbitrary controlled ray precision away from2. The visible auxiliary support is moved to fresh primes splitting the A-root closure and B-radical with prescribed cyclotomic Frobenius. The formula for every lower norm ratio is explicit. This assertion alone does not preserve a lower norm class; A100 supplies that refinement for an existing finite chain.',
        'uses_local_theorem': 'no; ray Artin maps, field intersections, divisors and rational norms',
        'manuscript_passages': 'cote149; scans56–58,79–85; L10 and L14 fixed-pair compatibility',
    },
    'A.100': {
        'file': 'norm_relative_ray_repair_agent.tex',
        'answers': 'A5; A15; L10; L14',
        'depends_on': 'A.92; A.95; A.99; Milne CFT VIII Theorem1.4; exact relative holomorph and unit-detecting ray maps',
        'notes': 'For one existing finite norm chain, the finite-precision support repair can preserve every lower norm class modulo ell^r. Split-prime divisors are taken above the same lower-field prime; finitely many unit-detecting places make the relative norm multiplier an actual ell^r-th-power unit. Its rational norm remains exactly one. This does not establish a new preimage for an arbitrarily fixed lower representative or an infinite compatible norm family.',
        'uses_local_theorem': 'no; finite relative Artin maps, odd-power local-global detection, and explicit norm formulas',
        'manuscript_passages': 'cote149; scans56–58,79–85; L10 and L14 lower-norm preservation',
    },
}
p = w / 'SECTIONS_OVER_Q_paper.tex'
s = p.read_text()
anchor = r'\input{sections/norm_hilbert_prime_allocation_agent.tex}'
for identifier, entry in entries.items():
    item = '\\input{sections/' + entry['file'] + '}'
    if item not in s:
        assert anchor in s
        s = s.replace(anchor, anchor + '\n' + item)
    anchor = item
p.write_text(s)
p = w / 'notes/register_metadata.json'
meta = json.loads(p.read_text())
for identifier, entry in entries.items():
    meta[identifier] = {key: value for key, value in entry.items() if key != 'file'}
p.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')

additions = [
    ({'A9', 'A12', 'L2'}, 'A.96', 'A.96 computes all quartic common characters and proves exact initialization at exponent four for two old finite punctures, preserving one prescribed local point at each of finitely many places.'),
    ({'A5', 'A7', 'L9', 'L15'}, 'A.97', 'A.97 proves own-coefficient rigidity and the fixed-global-coefficient criterion for ordinary completed pairs; every different labeled realized Selmer section differs from its rational coefficient pair on a nonempty Chebotarev class.'),
    ({'A5', 'A15', 'L10', 'L14'}, 'A.98–A.100', 'A.98 exhibits a nonextendible norm representative even for the rational point3, alongside an explicit compatible family for that point. A.99–A.100 repair auxiliary support at each fixed precision and preserve lower norm classes within an existing finite chain. An infinite coherent norm family for an ordinary ghost remains unconstructed.'),
]
p = w / 'SECTIONS_OVER_Q_report.md'
report = p.read_text()
lines = report.splitlines()
for index, line in enumerate(lines[:55]):
    for items, identifiers, explanation in additions:
        if any(line.startswith('| ' + item + ' |') for item in items):
            columns = line.split(' | ')
            if identifiers not in columns[1]:
                columns[1] += ', ' + identifiers
            line = ' | '.join(columns)
            if explanation not in line:
                line = line[:-2] + ' ' + explanation + ' |'
    lines[index] = line
report = '\n'.join(lines) + '\n'
heading = '## Quartic initialization, coefficient rigidity and relative norm support'
if heading not in report:
    report += '\n' + heading + '\n\n' + stamp + ': Five further results have been independently audited and integrated. A.96 obtains the full quartic common-field formula from the literal finite stabilizer equations. Every extra character is supplied by a negative-square subset product. With two old coordinates, the singleton and two-coordinate cases have displayed quadratic norm identities, so global reciprocity and A.85 solve the finite initialization problem. The finite prescription explicitly means one old local point per selected place. The example on three old coordinates remains in A.69 and A.90; no assertion at larger exponents is imported.\n\nA.97 retains both actual coefficient projections. The own-coefficient local kernel is mu_(p-1) for odd p and trivial for2; embedding the resulting finite cyclotomic field in C forces both roots of unity to be1. A.76 then treats density-one ordinary comparison. An equality at one global coefficient fixes all ordinary integer valuations; the exact kernel of the full valuation map is the two signs, and the unit equation fixes them. The Selmer refinement states precisely the density-one ordinary scope. The full congruence recognition problem keeps its actual finite abelian comparison and remains open.\n\nA.98 provides the explicit61-adic obstruction to extending an arbitrary chosen norm representative. The three valuations (2,-1,-1) cannot all be norms from the next cubic local factors, for any of the stated rational coefficient rescalings. The same rational pair has the compatible family1-3^(1/3^n), so the result does not assert a nonzero coherent obstruction for that pair. A.99 uses primary ray classes and norm-one squaring to repair auxiliary support modulo any fixed odd-prime power, retaining the exact lower-norm transition. A.100 refines the generators to differences above the same lower-field prime and adds finitely many unit-detecting ray places. Its relative norm multiplier is an actual ell^r-th-power unit. Both results concern an existing finite chain; they leave the next preimage and infinite convergence questions explicit.\n'
p.write_text(report)

audit = stamp + ' root audits A96–A100: read every saved assertion and proof. A96 finite lift congruences, positive-relation elimination, negative generators, exact singleton/product norm identities and affine map pass; clarified one prescribed point per place. A97 local primary kernels, complex field embedding, density detection, full valuation kernel, signs and Selmer cusp functions pass; own-coefficient and global-coefficient scopes are explicit. A98 arithmetic, Q61 product map, completed norm valuations, universal rational rescalings and compatible good family pass; added the two literal coefficient-comparison equalities. A99 ray field unramifiedness at2, allowed Frobenius coset, ideal norms, prime-to-ell correction, squaring and lower norm formula pass. A100 relative stabilizer subgroup, same-prime character generators, Milne VIII1.4 odd-power hypothesis, finite unit detectors, ray extension and exact lower power ratios pass. Independent audits are retained in the agent notes. No next-level preimage, infinite norm coherence, higher-exponent quartic constancy or unrestricted H recognition is inferred.\n'
for name in ('notes/hour6_root_audits.md', 'notes/root_progress.md'):
    with (w / name).open('a') as out:
        out.write('\n' + audit)
output = 'Integrated A.96–A.100 with exact finite initialization, coefficient rigidity, representative obstruction and relative finite-precision support repair. A1 and the coherent infinite norm construction remain open.\n'
Path(__file__).with_name('integrate_a96_a100_output.txt').write_text(output)
print(output, end='')
