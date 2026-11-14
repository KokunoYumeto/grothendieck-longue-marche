"""Exact reduced-domain central gauge and rank certificate for E98."""
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--source-code',type=Path,default=HERE if (HERE/'e_wild_layers.json').exists() else HERE.parents[1]/'LM7_FERMAT_TOWER/code')
BASE=ap.parse_args().source_code.resolve()
spec=importlib.util.spec_from_file_location('e98_central_smith',BASE/'e_cusp_local_smith.py')
smith=importlib.util.module_from_spec(spec);spec.loader.exec_module(smith)
mat=lambda A:s.Matrix([[s.Rational(x) for x in row] for row in A])
enc=lambda A:[[str(x) for x in row] for row in A.tolist()]
integral=lambda A:all(s.Rational(x).q%3 for x in A)
layers=json.loads((BASE/'e_wild_layers.json').read_text())['layers']
T,J=[mat(layers['1'][k]) for k in ['input_tau','input_c']]
pairs=list(combinations(range(10),2))
wedge=lambda a,b:s.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in pairs])
ext=lambda A:s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in pairs] for i,j in pairs])
I=s.eye(10)
Vp=s.Matrix.hstack((I+J)*I[:,0]/2,I[:,3]-I[:,4],I[:,6]-I[:,7],I[:,8]-I[:,9])
Wm=s.Matrix.hstack(I[:,2],I[:,5],I[:,3]+I[:,4],I[:,6]+I[:,7],I[:,8]+I[:,9])
Vm=((I-J)*I[:,1]/2).row_join(Wm)
SV=Vp.row_join(Vm);SVi=SV.inv()
assert integral(SV) and integral(SVi) and J*Vp==Vp and J*Vm==-Vm
ordered=[(i,j) for i,j in pairs if (i<4)==(j<4)]+[(i,j) for i,j in pairs if (i<4)!=(j<4)]
SM=s.Matrix.hstack(*[wedge(SV[:,i],SV[:,j]) for i,j in ordered]);SMi=SM.inv()
Mp=SM[:,:21];B,J2=ext(T),ext(J)
assert integral(SMi) and J2*Mp==Mp
central=(s.eye(45)-B)*Mp
print('START exact Smith on the 45 by21 integral central gauge',flush=True)
cs=smith.local_smith(central.tolist())
assert cs['valuations']==[0]*7+[1]*9+[2]*5 and cs['free_rank']==24
print('PASS exact central Smith and all four inverse-pair products',flush=True)
data=json.loads((HERE/'e_global_split7_explore.json').read_text())
Q,S,D,Di=[mat(data[k]) for k in ['quotient_map','quotient_section','local_matrix','local_inverse']]
w=s.Matrix(data['primitive_w']);differential=B/7-s.eye(45)
assert Q*S==s.eye(44) and Q*w==s.zeros(44,1)
assert differential*w==s.zeros(45,1)
assert (differential*S)[1:,:]==D and D*Di==Di*D==s.eye(44)
print('PASS exact rank44 certificate via primitive kernel and full 44 by44 inverse',flush=True)
L,Li,R,DD=[mat(cs[k]) for k in ['left','left_inverse','right','diagonal_matrix']]
round_trips=0
for n in range(40):
    coord=s.Matrix([0 if i<7 else ((n*(i+3)+i*i)%(3**cs['valuations'][i]) if i<21 else n-i) for i in range(45)])
    h=s.Matrix([s.Rational(n+2*i-9,2**(i%3)) for i in range(21)])
    raw=Li*coord+central*h
    z=L*raw
    def mod(x,k):
        x=s.Rational(x);return int(x.p)*pow(int(x.q),-1,k)%k
    got=s.Matrix([0 if i<7 else (mod(z[i],3**cs['valuations'][i]) if i<21 else z[i]) for i in range(45)])
    assert got==coord
    repair=R*s.Matrix([(got[i]-z[i])/DD[i,i] for i in range(21)])
    assert integral(repair) and raw+central*repair==Li*got
    round_trips+=1
print('PASS all40 exact central coordinate and conjugator inverse round trips',flush=True)
out={'status':'PASS','Vplus':enc(Vp),'Vminus':enc(Vm),'Vsplit_inverse':enc(SVi),
     'Mplus':enc(Mp),'Msplit':enc(SM),'Msplit_inverse':enc(SMi),
     'central_gauge':enc(central),'central_gauge_smith':smith.encode(cs),
     'tame_differential_rank':44,'central_round_trips':round_trips,
     'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
                    [BASE/'e_cusp_local_smith.py',BASE/'e_wild_layers.json',HERE/'e_global_split7_explore.json']}}
(HERE/'e_global_split7_central.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL E98 CENTRAL CHECKS PASS',flush=True)
