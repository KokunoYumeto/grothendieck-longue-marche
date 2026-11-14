#!/usr/bin/env python3
"""E.39: exact cyclic-cubic witness for a local correction word."""
from pathlib import Path
import json

def character(value,q,zeta):
    residue=pow(value%q,(q-1)//3,q)
    return next(i for i in range(3) if pow(zeta,i,q)==residue)

rows=[]
for q,zeta in [(7,2),(7,4),(19,7),(19,11)]:
    lam=(1-zeta)%q
    row={'q':q,'zeta':zeta,'lambda':lam,
         'kappa2':character(2,q,zeta),
         'kappa_zeta':character(zeta,q,zeta),
         'kappa_lambda':character(lam,q,zeta),
         'kappa_zeta_lambda':character(zeta*lam,q,zeta)}
    assert row['kappa_zeta_lambda']==(row['kappa_zeta']+row['kappa_lambda'])%3
    rows.append(row)
assert [(r['kappa2'],r['kappa_zeta'],r['kappa_lambda']) for r in rows[:2]]==[(2,2,0),(1,2,2)]
solutions=[(a,b) for a in range(3) for b in range(3)
           if all((a*r['kappa_zeta']+b*r['kappa_lambda']-r['kappa2'])%3==0
                  for r in rows[:2])]
assert solutions==[(1,1)]
for r in rows[2:]:
    r['correction_character']=(r['kappa2']-r['kappa_zeta_lambda'])%3
assert rows[2]['correction_character']==2
assert rows[3]['correction_character']==1
result={'rows':rows,'unramified_character_coordinates':solutions[0],
        'specified_prime19_correction':2,'status':'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
for r in rows:
    print(r)
print('Restricted character kappa2 o s = kappa(zeta*lambda).')
print('At (-2+3*zeta), kappa2(h_19)=2, whereas kappa2(I_19)=0.')
print('PASS: exact finite residue and character computations.')
