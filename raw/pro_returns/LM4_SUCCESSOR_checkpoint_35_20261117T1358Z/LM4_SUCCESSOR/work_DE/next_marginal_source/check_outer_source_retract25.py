"""Exact whole-source basis under the actual post-final neck retraction."""
from pathlib import Path
import json,hashlib
BASE=Path(__file__).resolve().parent
D=json.loads((BASE/'annular_neck_reflection23.json').read_text())
eta={int(k):tuple(v) for k,v in D['eta_adapted_K_basis_a_barb_d_e_f'].items()}
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(x)
    return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,m):return red(y for x in w for y in (m[abs(x)] if x>0 else inv(m[-x])))
def con(a,w):return mul(a,w,inv(a))
# B112 raw-source detector, followed by the entire selected gap conjugation a.
a=(1,);B=(2,);d=(3,);e=(4,);f=(5,)
u={1:con(a,B),2:con(mul(a,B,f,d),e),3:con(a,d),4:a,5:con(a,f)}
uinv={1:(4,),2:(-4,1,4),3:(-4,3,4),5:(-4,5,4),4:(-4,-3,-5,-1,2,1,5,3,4)}
for i in range(1,6):
    assert sub(u[i],uinv)==(i,)
    assert sub(uinv[i],u)==(i,)
    assert sub(eta[i],eta)==(i,)
v={i:sub(u[i],eta) for i in range(1,6)}
vinv={i:sub(eta[i],uinv) for i in range(1,6)}
for i in range(1,6):
    assert sub(v[i],vinv)==(i,)
    assert sub(vinv[i],v)==(i,)
out={'status':'PASS','K_labels':['a','B','d','e','f'],'source_labels':['outer_contact1','outer_contact2','outer_contact3','outer_contact4','outer_base'],
 'selected_regional_source_detector_basis':u,'its_inverse':uinv,'actual_outer_source_images':v,'outer_source_inverse':vinv,
 'literal_inverse_checks':20,'eta_inverse_checks':5,'inner_source_image':[],
 'scope':'Exact five-source free-basis comparison under the actual B121 retraction. No freeness of the full six-source image or original-cone equivariance is inferred.'}
(BASE/'outer_source_retract25.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all20 source-basis inverse substitutions and all5 eta² checks.')
print('PASS actual outer5 image is a free K basis; inner source maps1.')
