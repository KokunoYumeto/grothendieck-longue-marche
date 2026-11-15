#!/usr/bin/env python3
"""Synchronize the new proved rows after their complete TeX proofs exist."""
import json
from pathlib import Path

path=Path(__file__).resolve().parents[1]/'notes/pbc_results.json'
data=json.loads(path.read_text())
new=[
dict(id='B.27',statement='The cubic metabelian involution and entire cubic sign family have full gentle lifts',status='Proved',where_proved='sections/B.tex',depends_on='B.9; B.11; B.12; P.3; R25',answers='Task P.2; Task B.2; Task B.3; Lead 5; Lead 6; Lead 22; Lead 26(a)',notes='Actual modular-source Hopf centralization; unique pro-five central lift; Cartesian comparison away from five; retained peripheral frames. Every nontrivial full positive lift has infinite order, and phi0 fails pentagon.'),
dict(id='B.28',statement='The negative residue survives the order614400 detector and is already Galois-realized on Q75',status='Proved',where_proved='sections/B.tex; code/pbc_extraspecial_negative.py; code/pbc_negative_shadow.py',depends_on='B.19; MilneEC2021 V Proposition8.3 and Weil pairing',answers='Task B.4; Task B.5; Lead 23; Lead 26(b)',notes='Exactly four of20 finite candidates satisfy both negative peripheral equations and frame norms. Frobenius13 on y2=x3+16 has trace5, det13, hence its conjugate of c realizes the Q75 residue. No full involutive lift of the complete metabelian tau0 is claimed.'),
dict(id='B.29',statement='The metabelian negative involution phi0*c is not conjugate to c in the image of the full pure peripheral group',status='Proved',where_proved='sections/B.tex; code/pbc_negative_shadow.py',depends_on='B.7; B.17; B.27; Weil pairing',answers='Task B.4; Task B.5; Lead 23; Lead 26(b)',notes='Invariant triangle quotients Q75 and Q100 force opposite determinant square classes mod5 for a conjugator; both determinants equal the same multiplier by unitary full image and Galois pairing. All-multiplier normalized section removes inner ambiguity. Full involutive lifting of tau0 remains open.'),
dict(id='C.17',statement='Corrected classification p>=5 of prime-index subgroups and all three modular signatures',status='Proved',where_proved='sections/C.tex; code/pbc_resolvents.py',depends_on='Beauville2010 introduction and Proposition1.1',answers='Task C.10; Lead 27(a)',notes='Only5,7,11; explicit A4,S4,A5 generators; exact coset passports and genus-zero signatures. Literal unrestricted claim also has2,3.'),
dict(id='C.18',statement='Both degree-five resolvents have exact domain (-15/lambda)=1, minimal marked filling field Q(sqrt(-15)), and fix its Galois image',status='Proved',where_proved='sections/C.tex; code/pbc_resolvents.py',depends_on='C.1; C.12; C.17',answers='Task C.10; Lead 27(a)',notes='Explicit polynomial j=27t3(9t2+15t+40), retained roots b+- and affine filling; self-normalizing A4 removes outer ambiguity; determinant and root-generator character checked at every residue mod15. Pentagon fixedness, exceptional element values, and maps at7/11 remain open.'),
dict(id='C.19',statement='Zero parity does not imply pentagon: the full gentle kernel of Delta contains a lift of phi0 and the entire cubic sign family in its metabelian image',status='Proved',where_proved='sections/C.tex; code/pbc_negative_shadow.py',depends_on='B.27; B.2; B.9; R24 frame formula',answers='Task P.2; Task B.2; Task C.4; Task C.8; Task C.9; Lead 11; Lead 22; Lead 25',notes='Q12 has order576 and q(F'+'\u2032\u2032'+') central order2; it factors through E0,2, where B27 map is identity and both retained torsion frames trivial. Thus actual full lift has Delta0 but fails metabelian pentagon. Does not decide GT subset kerDelta.')
]
byid={r['id']:r for r in data}
for row in new:
    if row['id'] in byid:byid[row['id']].update(row)
    else:data.append(row)
for row in data:
    if row['id']=='B.3':
        row['notes'] += ' B.27 strengthens the unrestricted lift to the full gentle group.'
    elif row['id']=='C.10':
        row['notes']='Classification/signatures now C.17; both p5 maps, exact domain and Galois fixed field now C.18. Degree7/11 maps, pentagon fixedness, E58/D46 values and common fixed group remain open.'
    elif row['id'] in ('B.4','B.5'):
        row['notes'] += ' B.28 gives finite survival and a Galois Q75 shadow; B.29 gives a distinct negative metabelian conjugacy class, with actual full involutive lifting still open.'
path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print('Registered',len(data),'rows; added',','.join(r['id'] for r in new))
