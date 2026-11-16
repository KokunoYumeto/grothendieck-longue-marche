#!/usr/bin/env python3
"""Record the actual canonical-divisor radical compositum and its maps."""
from pathlib import Path
import datetime
import json
w = Path(__file__).resolve().parents[1]
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M UTC')
p = w/'SECTIONS_OVER_Q_paper.tex'
s = p.read_text()
anchor = r'\input{sections/norm_relative_ray_repair_agent.tex}'
entry = r'\input{sections/norm_canonical_two_wreath_agent.tex}'
if entry not in s:
    assert anchor in s
    s = s.replace(anchor, anchor+'\n'+entry)
p.write_text(s)
p = w/'notes/register_metadata.json'
meta = json.loads(p.read_text())
meta['A.101'] = {
    'answers': 'A5; A15; L10; L14',
    'depends_on': 'A.44; A.77; A.95; A.99; A.100; Hoshi–Yamasaki2025 Theorems1.2,2.2,3.2; literal Kummer automorphisms and the canonical two-adic valuation matrix',
    'uses_local_theorem': 'no; finite weak approximation on a norm fibre, actual splitting fields, commutators and ramification maps',
    'manuscript_passages': 'cote149; scans56–58,79–85; L10 and L14 simultaneous norm compatibility',
    'notes': 'The canonical divisor at2 makes all conjugates of the norm representative independent at every three-power precision. The theorem constructs the actual split wreath group, its arithmetic action, the exact common b-radical field, and the full simultaneous arithmetic abelianization. The combined Kummer valuation lattice proves disjointness from the ray-Hilbert compositum over the A-root field. Permitted class-generating primes may therefore split all conjugate representative radicals and satisfy the prescribed exact v3(q−1). The still unresolved step is the local unit norm condition at new primes carrying the repaired divisor; no infinite compatible family is claimed.'
}
p.write_text(json.dumps(meta, indent=2, ensure_ascii=False)+'\n')
p = w/'SECTIONS_OVER_Q_report.md'
lines = p.read_text().splitlines()
extra = 'A.101 computes the actual simultaneous radical and ray-Hilbert intersections from a canonical divisor at2, allowing the class-generating primes also to split all conjugate representative radicals. New-support unit norm conditions remain to be solved.'
for i, line in enumerate(lines[:55]):
    if line.startswith(('| A5 |','| A15 |','| L10 |','| L14 |')):
        cols = line.split(' | ')
        if 'A.101' not in cols[1]:
            cols[1] += ', A.101'
        line = ' | '.join(cols)
        if extra not in line:
            line = line[:-2]+' '+extra+' |'
        lines[i] = line
s = '\n'.join(lines)+'\n'
heading = '## Simultaneous radical splitting from the canonical divisor at two'
if heading not in s:
    s += '\n'+heading+'\n\n'+stamp+': A.101 fixes the actual norm representative to have valuation1 at the unique degree-one branch over2 and0 at the others. Finite weak approximation on the opened norm-one torus supplies this local divisor, and the existing support repairs preserve it. In the normal closure its conjugates have a diagonal valuation matrix with three-adic unit diagonal. This proves full Kummer independence and permits literal cyclic and cyclotomic lifts on independent root generators.\n\nThe resulting wreath group computes the relative abelian field and the exact common b-radical with the boundary field. The simultaneous field is treated through its full fibre-product group, including that common subfield, and its arithmetic abelian field is exactly the specified cyclotomic base. The combined Kummer valuation lattice shows that every nontrivial three-primary subextension ramifies at some prime above2; this gives the exact ray-Hilbert intersection. The allowed class-generating primes can therefore split every conjugate representative radical while retaining the cyclotomic conditions. This removes a simultaneous-field restriction from the proposed recursion. It does not yet solve the local unit equations at primes where a repaired norm representative has acquired nonzero valuations.\n'
p.write_text(s)
audit = stamp+' root A101 audit: checked the unramified root algebra at2, unique degree-one factor, diagonal valuation matrix after cyclotomic base change, full Kummer degree, literal cyclic/cyclotomic lifts and their semidirect relation. Checked relative commutators, boundary intersection, simultaneous V-prime fibre product, translation coinvariants, action of−1, prime-to-three boundary factor and base-change abelianization. The combined Kummer lattice proves the ray-Hilbert intersection, and the original Frobenius-coset character argument retains class generators. Independently reopened Hoshi–Yamasaki2503.14365v5 Sections2–3 for finite weak approximation. Independent local_preprint audit and exact finite certificate pass. No new-prime unit norm or infinite convergence assertion is made.\n'
for name in ['notes/hour6_root_audits.md','notes/root_progress.md']:
    with (w/name).open('a') as out:
        out.write('\n'+audit)
output = 'A101 integrated: actual simultaneous radical groups, arithmetic abelianization and ray-Hilbert intersection; next unit norm step remains open.\n'
Path(__file__).with_name('integrate_a101_output.txt').write_text(output)
print(output, end='')
