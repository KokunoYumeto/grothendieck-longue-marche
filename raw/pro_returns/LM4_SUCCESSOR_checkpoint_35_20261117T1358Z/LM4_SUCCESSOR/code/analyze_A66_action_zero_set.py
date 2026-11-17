"""Exact translation symmetry of the saved exhaustive ordinary-square gate."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'work_CE/A66_ordinary_action_zero_set.json'
raw=path.read_bytes()
data=json.loads(raw)
zeros=set(data['zero_masks'])
assert len(zeros)==408 and 0 in zeros
translations=[x for x in sorted(zeros) if all(x^y in zeros for y in zeros)]


def echelon(values):
    p={}
    for v in values:
        while v:
            i=v.bit_length()-1
            if i not in p:
                p[i]=v
                break
            v^=p[i]
    return p


basis=echelon(translations)
assert len(basis)==3 and len(translations)==8
assert all(x^y in translations for x in translations for y in translations)
cosets={min(x^t for t in translations) for x in zeros}
assert len(cosets)==51
assert {x^t for x in cosets for t in translations}==zeros
linear=data['linear']
polar={(q['i'],q['j']):q['value'] for q in data['quadratic']}


def bilinear(x,y):
    out=0
    for (i,j),v in polar.items():
        if (((x>>i)&1)*((y>>j)&1))^(((x>>j)&1)*((y>>i)&1)):
            out^=v
    return out


def qval(x):
    out=0
    for i,v in enumerate(linear):
        if (x>>i)&1:
            out^=v
    for (i,j),v in polar.items():
        if (x>>i)&1 and (x>>j)&1:
            out^=v
    return out


assert all(qval(t)==0 and all(bilinear(t,1<<i)==0 for i in range(19))
           for t in translations)
out=dict(scope='Translation symmetry of the complete saved ordinary action-square gate only.',
         source_sha256=hashlib.sha256(raw).hexdigest(),
         zero_count=408,zero_span_dimension=len(echelon(zeros)),
         translation_dimension=3,translation_masks=translations,
         zero_coset_representatives=sorted(cosets),zero_cosets=51,
         quadratic_invariance_checked=True)
(ROOT/'records/A66_action_zero_set_symmetry.json').write_text(json.dumps(out,indent=2)+'\n')
print('Zero set:',len(zeros),'values; linear span dimension:',len(echelon(zeros)))
print('Exact translation stabilizer:',len(translations),'values; dimension:',len(basis))
print('All translations have zero quadratic value and annihilate every polar column: PASS')
print('Exact quotient by this3-dimensional symmetry:',len(cosets),'zero cosets')
print('No assertion about frame norms, scalar extensions, or full negative order.')
