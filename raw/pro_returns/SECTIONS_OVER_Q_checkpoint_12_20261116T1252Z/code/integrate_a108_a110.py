#!/usr/bin/env python3
"""Integrate the independently audited harmonic and finite norm-module results."""
from pathlib import Path
import datetime
import json

w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
entries = [
    ('A.108', 'harmonic_jacobian_descent.tex'),
    ('A.109', 'norm_torus_selmer_agent.tex'),
    ('A.110', 'norm_torus_cyclic_obstruction.tex'),
]
p = w / 'SECTIONS_OVER_Q_paper.tex'
source = p.read_text()
anchor = r'\input{sections/harmonic_tripod_bridge.tex}'
assert anchor in source
for ident, filename in entries:
    entry = '\\input{sections/' + filename + '}'
    if entry not in source:
        source = source.replace(anchor, anchor + '\n' + entry)
    anchor = entry
p.write_text(source)

records = {
    'A.108': {
        'answers': 'A9; A12; A15; L14; L20',
        'depends_on': 'A.88; A.96; explicit harmonic covers, Jacobian isogeny and Galois cocycle calculation',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans56–58,126–127; harmonic finite-coordinate comparison',
        'notes': 'Identifies the exact normalized Brauer class with pullback of the elliptic norm cocycle through C4→C2. Proves the degree16 Jacobian kernel and Galois descent, all rational two-torsion, signed-square and basepoint killed directions, and an explicit source norm quartic. Retains the possible kernel on H1; no global vanishing or obstruction is inferred from the Jacobian injection.'
    },
    'A.109': {
        'answers': 'A5; A9; A15; L10; L14; L20',
        'depends_on': 'A.77; A.101; A.103; Neftin Theorem2.1(c); Hoshi–Yamasaki Proposition3.1 and Theorem3.2',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans56–58,126–127; exact norm-torus approximation maps',
        'notes': 'Computes H1 of the actual finite norm-torus torsion and its Cartier dual at every3-power precision, proves finite-set approximation and split-prime detection, and identifies the actual norm-one Selmer image. Gives the exact scalar-shifted local graph for the next cubic norm condition and its Tate orthogonal. No all-new-prime ramification prescription follows.'
    },
    'A.110': {
        'answers': 'A5; A9; A15; L10; L14; L20',
        'depends_on': 'A.105; A.106; A.109; explicit equivariant alternating form; Milne ADT I2.3,I2.8,I4.10(c)',
        'uses_local_theorem': 'no',
        'manuscript_passages': 'cote149; scans56–58,126–127; scope of cyclic auxiliary norm repair',
        'notes': 'Refutes unrestricted prescribed local norm-one data with cyclic or scalar-shifted-graph auxiliary ramification using q271 and an explicit Brauer quadratic form. The same form detects the A106 multiplier. Its invariant is onto on the actual norm-one group at3, so that free local choice absorbs every value of this particular obstruction. Does not refute the actual coherent norm-chain problem.'
    },
}
p = w / 'notes/register_metadata.json'
meta = json.loads(p.read_text())
meta.update(records)
p.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + '\n')

p = w / 'SECTIONS_OVER_Q_report.md'
report = p.read_text()
lines = report.splitlines()
updates = {
    'A5': ('A.109–A.110', 'The exact finite norm-torus and dual modules have finite-set approximation at every3-power precision. Arbitrary local prescriptions with cyclic auxiliary ramification are refuted by an explicit Brauer pairing; its invariant is onto at the free coefficient-place3. The actual norm-chain repair remains unresolved.'),
    'A9': ('A.108–A.110', 'The harmonic Brauer comparison now has an explicit elliptic norm cocycle and Jacobian pullback. The norm-tower repair retains its finite approximation and quadratic reciprocity conditions.'),
    'A12': ('A.108', 'The harmonic joint character factors through a specific elliptic norm cocycle; its rational torsion, signed-square and basepoint directions are proved to vanish after the exact Jacobian pullback.'),
    'A15': ('A.108–A.110', 'The harmonic Jacobian comparison and the exact quadratic reciprocity obstruction for unrestricted norm repair are proved, including their local-three scope.'),
    'L10': ('A.109–A.110', 'Finite-set norm-torus approximation is proved, and the stronger unrestricted cyclic-new-ramification prescription is refuted. A free local multiplier at3 absorbs the displayed invariant.'),
    'L14': ('A.108–A.110', 'The actual elliptic-to-Jacobian cocycle map and norm-torus half-cup Brauer map are explicit; their kernels and local freedom are retained.'),
    'L20': ('A.108–A.110', 'The harmonic joint symbol has an exact norm-cocycle comparison. Coupled norm-chain repair still requires more than finite-set weak approximation.'),
}
for i, line in enumerate(lines[:55]):
    for item, (ids, detail) in updates.items():
        if line.startswith('| ' + item + ' |'):
            parts = line.split(' | ')
            if ids not in parts[1]:
                parts[1] += ', ' + ids
            line = ' | '.join(parts)
            if detail not in line:
                line = line[:-2] + ' ' + detail + ' |'
            lines[i] = line
report = '\n'.join(lines) + '\n'
heading = '## Exact harmonic descent and norm-torus reciprocity'
if heading not in report:
    report += '\n' + heading + '\n\n' + stamp + ': A.108 identifies the actual Jacobian pullback C4→C2 and the uniform Galois cocycle for every harmonic negative-triple character, including dependent quadratic fields. It proves the precise killed directions and the source norm quartic, while retaining the possible kernel on H1. A.109 computes the two finite norm-torus H1 groups at every3-power precision, obtains finite-set approximation, and identifies both the actual norm-one Selmer image and the auxiliary local norm graph. A.110 refutes unrestricted prescribed local data with cyclic or scalar-shifted auxiliary graphs by a concrete order3 Brauer invariant at271. The same invariant is surjective on actual local norm-one classes at3, so this counterexample does not settle the norm-chain construction. Both principal A1 assertions remain open.\n'
p.write_text(report)

audit = (stamp + ' root audits A108–A110: checked the harmonic finite maps and all degrees, the branch-character kernel and degree16 isogeny, rational elliptic factor and exact C4→C2 pullback, all four Galois sign cases, torsion primitives, both coordinates of the1+i division point, squareclass quotient, and source norm quartic. Checked both all-precision holomorph H1 vanishings, minimal splitting-field inflation, split-prime detection, norm-one Kummer/Hasse comparison, Tate orthogonal graphs and the scalar-shifted tame norm equation. Checked all A110 arithmetic and equivariance data, normalized half-cup and reciprocity, exact radical at3, invariant and Euler-characteristic dimensions, quadratic surjectivity and both cubic local norms. Root reran both finite certificates successfully. Local agent independently passed A109/A110; the harmonic proof has independent Legendre review.\n')
for name in ['notes/hour7_root_audits.md', 'notes/root_progress.md']:
    with (w / name).open('a') as out:
        out.write('\n' + audit)
sources = (stamp + ' source verification: reopened Neftin author PDF https://neftin.net.technion.ac.il/files/2015/10/20-6-12.pdf, Theorem2.1(c), Proposition2.2 and Corollary2.3; only finite prescribed sets are supplied. Reopened Milne ADT second edition https://www.jmilne.org/math/Books/ADTnot.pdf, I Corollary2.3 printed28 and Theorem2.8 printed31, for finite characteristic-zero local modules including residue-characteristic torsion. Reopened Hoshi–Yamasaki2503.14365v5, Proposition3.1 and its exact norm-torus weak-approximation conclusion, with the actual holomorph Schur multiplier and stabilizer hypotheses checked. No all-new-prime cyclic ramification theorem is imported.\n')
with (w / 'notes/root_source_continuation.md').open('a') as out:
    out.write('\n' + sources)
output = 'Integrated A108–A110 with exact scopes; finite certificates and primary-source passages verified. Both A1 assertions remain open.\n'
Path(__file__).with_name('integrate_a108_a110_output.txt').write_text(output)
print(output, end='')
