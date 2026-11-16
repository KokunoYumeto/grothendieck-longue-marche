#!/usr/bin/env python3
"""Integrate A68 after explicit full root and DE approval; keep all candidates."""
from pathlib import Path
import hashlib,json,shutil,sys
r=Path(__file__).resolve().parents[1]
assert '--root-approved' in sys.argv
assert (r/'notes/de_A68_audit.md').exists()
assert (r/'notes/de_A68_intermediate_audit.json').exists()
assert json.loads((r/'notes/fgh_C8_compact_type_certificate.json').read_text())['status']=='PASS'
assert json.loads((r/'notes/fgh_A68_intermediate_certificate.json').read_text())['status']=='PASS'
name='A_dihedral_eight_fixed'
s=(r/'notes/fgh_A68_draft.tex').read_text()
s=s.replace('% A.68 candidate: notes only, unregistered pending independent audits.',
 '% A.68: full root and DE proof/source/exact-certificate audits PASS, including every intermediate.')
s=s.replace(r'\begin{statement}{A.68}{Open}{Candidate: the nonstable dihedral genus-seven covers have cusp fixed groups}',
 r'\begin{statement}{A.68}{Proved}{The nonstable genus-seven dihedral covers and their intermediates}')
s=s.replace('the fixed geometric pro-\\(\\ell\\) subgroup is exactly the selected\ncusp inertia.',
 'the fixed geometric pro-\\(\\ell\\) subgroup is exactly the selected\ncusp inertia. The same conclusion holds for every actual intermediate\ncover of either degree-sixteen dihedral closure.')
s=s.replace('we obtain\n', 'we obtain\n')
s=s.replace('D\\k{a}browski--Sadek, equation (3),',
 '\\cite[equation (3), p.3]{fghDabrowskiSadek},')
s=s.replace('The standard conversion\n',
 'The standard conversion in \\cite{fghSageIgusa}\n')
s=s.replace('The exact certificate also reproduces the official PARI example\n',
 'The exact certificate also reproduces the official PARI example\n\\cite{fghPARIHyperelliptic}\n')
s=s.replace("Liu, \\emph{Courbes stables de genre 2 et leur sch\\'ema de modules},\nTheorem 1 on printed page 204,",
 '\\cite[Theorem 1, printed p.204]{fghLiu1993Stable}')
add=(r/'notes/fgh_A68_intermediate_addendum.tex').read_text()
add='\n'.join(line for line in add.splitlines() if not line.startswith('%'))+'\n'
anchor='All finite identities used here are checked in the retained program'
assert s.count(anchor)==1
s=s.replace(anchor,add+'\nAll finite identities used here are checked in the retained programs')
s=s.replace(r'\path{notes/fgh_C8_compact_type_certificate.py};',
 r'\path{code/a_dihedral_eight_fixed.py},'+ '\n'+
 r'\path{code/a_dihedral_eight_maps.py}, and'+ '\n'+
 r'\path{code/a_dihedral_eight_intermediates.py};')
assert s.count('\\[')==s.count('\\]')
assert '{A.68}{Open}' not in s and 'Candidate:' not in s
(r/f'sections/{name}.tex').write_text(s)
for source,dest in [('fgh_C8_compact_type_certificate','a_dihedral_eight_fixed'),
                    ('fgh_C8_frontier','a_dihedral_eight_maps'),
                    ('fgh_A68_intermediate_certificate','a_dihedral_eight_intermediates')]:
    for ext in ('.py','.json','.out'):
        shutil.copy2(r/f'notes/{source}{ext}',r/f'code/{dest}{ext}')
p=r/'sections/A.tex';s=p.read_text();anchor=r'\input{sections/A_tetrahedral_covers.tex}'
assert s.count(anchor)==1 and name not in s
p.write_text(s.replace(anchor,anchor+'\n'+rf'\input{{sections/{name}.tex}}'))
row={'id':'A.68','statement':'The two nonstable genus-seven dihedral covers and every intermediate have both all-prime cusp assertions',
 'status':'Proved','where_proved':f'sections/{name}.tex',
 'depends_on':['A.37','A.40','A.41','A.42','A.59'],'answers':['Task A.5'],
 'notes':'Registered after full root and DE proof/source/exact-certificate audits PASS. Actual maps decompose J_C8 as J_C4 times the square of a genus-two Jacobian. Exact normalized Igusa invariants and original Liu Theorem1(V*)/(V) give two supersingular elliptic components at2; all cusp differences are killed by8 via actual principal divisors. Every actual intermediate inherits good two-rank-zero Jacobian reduction and cusp torsion by norm. Its cusp count is [D16:HI]>=2 for every proper H because inertia I=<r²> is the Frattini subgroup. A41–42 give all full fixed subgroups; A59 gives all normalizers. No universal Task A5 or arbitrary higher dihedral claim is made.'}
(r/'notes/fgh_A68_row.json').write_text(json.dumps(row,indent=2)+'\n')
p=r/'notes/a_results.json';rows=json.loads(p.read_text());assert not any(x['id']=='A.68' for x in rows);rows.append(row);p.write_text(json.dumps(rows,indent=2)+'\n')
p=r/'sections/A_general_cover_frontier.tex';s=p.read_text();anchor='pullbacks: their three-adic dual graph can have cycles.';assert s.count(anchor)==1
s=s.replace(anchor,anchor+'\n\n'+r'''A.68 completes the two nonstable genus-seven dihedral covers
\(v^2=w^{16}\pm6w^8+1\), and every actual intermediate
of their degree-sixteen closures, at all coefficient primes.
An actual genus-two quotient, exact Igusa invariants and Liu's
residue-two criterion give potential good Jacobians of
\(2\)-rank zero. Explicit principal divisors kill every cusp
difference by eight; norm maps and the Frattini inertia calculation
carry the rational-path criterion to each intermediate.
This does not settle arbitrary higher two-power dihedral covers.
''');p.write_text(s)
p=r/'notes/root_cover_frontier_results.json';rows=json.loads(p.read_text())
for x in rows:
    if x['id']=='A.45':
        assert x['status']=='Open'
        if isinstance(x['depends_on'],list):
            if 'A.68' not in x['depends_on']:x['depends_on'].append('A.68')
        else:x['depends_on']+='; A.68'
        x['notes']+=' A68 completes both nonstable genus-seven D16 closures and all their actual intermediates by an explicit genus-two quotient, Liu residue-two invariants, eight-torsion cusp divisors and Frattini inertia. Arbitrary higher dihedral and universal covers remain outside this assertion.'
p.write_text(json.dumps(rows,indent=2)+'\n')
with (r/'notes/fgh.md').open('a') as f:
    f.write('\n\n## A68: nonstable genus-seven dihedral covers and intermediates\n\nIntegrated after full root and DE proof/source/certificate PASS. The actual genus-two quotient B:W²=(T+2)(T⁴−4T²−4), T=w²+w^-2, gives J_C~J_C4×J_B². Exact Igusa J=(24,−24,1248,7344,−256) and original Liu Thm1 show two supersingular elliptic components at2. Four explicit principal divisors kill all cusp differences by8. Norm and I=Phi(D16) prove every proper intermediate has the same rational-companion-path hypothesis. Both cusp assertions hold at every prime; universal A45 remains Open. Original candidates, source verification, exact finite certificates and all independent audit outputs remain retained.\n')
print('A68 integrated; canonical section/input, one owner row and narrow A45 update; no assembled register/PDF rebuilt.')
