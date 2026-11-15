#!/usr/bin/env python3
"""Add all mod-three projective evaluations to the exact modular Hopf test."""
from pathlib import Path
import json,runpy
d=runpy.run_path(str(Path(__file__).with_name('pbc_modular_envelope.py')))
mm,mi,gm,gi=d['mm'],d['mi'],d['gm'],d['gi']
I=d['I'];S2=d['S2'];R2=d['R2']
def can(a):return min(a,tuple(-x%3 for x in a))
M=sorted({can((a,b,c,e)) for a in range(3) for b in range(3) for c in range(3) for e in range(3) if (a*e-b*c)%3==1})
assert len(M)==12
idx={a:i for i,a in enumerate(M)}
SX=(0,1,2,0);TY=(1,2,0,1)
def ev(w,x=SX,y=TY):
    a=I;gg={1:x,2:y,-1:mi(x,3),-2:mi(y,3)}
    for j in w:a=mm(a,gg[j],3)
    return can(a)
ps=[]
for modg,t in ((S2,1),(R2,2)):
    p=[0]*72
    for k,(a,w) in enumerate(d['cos']):
        j=d['ci'][mm(a,modg,2)]
        ret=gm(gm(w,(t,)),gi(d['cos'][j][1]))
        val=ev(d['words'][ret])
        for h,b in enumerate(M):p[k*12+h]=j*12+idx[can(mm(b,val,3))]+1
    ps.append(p)
full=[a+[288+j for j in b] for a,b in zip(d['perms'],ps)]
z=mi(mm(SX,TY,3),3)
from itertools import permutations
assert all(ev(d['outword'],a,b)==can(I) for a,b in permutations((SX,TY,z),2))
prefix='s:=PermList('+str(full[0])+');;\nr:=PermList('+str(full[1])+');;\nG:=Group(s,r);;\nx:=(r*s)^2;; y:=(s*r)^2;;\nf:='+d['gapword'](d['outword'])+';;\n'
body=Path(__file__).with_name('pbc_hopf_test.g').read_text().split('LoadPackage("polycyclic");',1)[1].replace('PBC_Tag:="mod4"','PBC_Tag:="joint"')
Path(__file__).with_name('pbc_hopf_joint.g').write_text(prefix+'LoadPackage("polycyclic");'+body)
record=dict(degree=360,mod3_projective_identity_verified=True,
            candidate_second_derived_word_length=len(d['outword']),
            gap_input='LM8_PUSH/code/pbc_hopf_joint.g',
            scope='Exact simultaneous finite source for the peripheral Hopf test')
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
