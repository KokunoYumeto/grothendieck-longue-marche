#!/usr/bin/env python3
"""Test whether original parity-frame separation survives a second pullback.

This retains a signed pure congruence map, not just its induced automorphism.
The GAP membership result is finite data; its full use requires the relative
lifting and actual-frame argument of C.23.
"""
from pathlib import Path
import json
import runpy

HERE=Path(__file__).parent
d=runpy.run_path(str(HERE/'pbc_iterated_descent.py'))
XX,YY=d['XX'],d['YY']

def mm(a,b,m):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))
def inv(a,m):return (a[3],-a[1]%m,-a[2]%m,a[0])
I=(1,0,0,1)
parts=[]
for mod in (3,4):
    mats=[(a,b,c,e) for a in range(mod) for b in range(mod) for c in range(mod) for e in range(mod) if (a*e-b*c)%mod==1]
    idx={a:i for i,a in enumerate(mats)}
    S=(0,1,mod-1,0)
    tau=(1,mod-1,0,1)
    # Exact old marking: y=tau^2 and x=s*y*s^{-1}.
    y=mm(tau,tau,mod)
    x=mm(mm(S,y,mod),inv(S,mod),mod)
    z=(mod-1,0,0,mod-1) if mod==3 else I
    parts.append([[idx[mm(a,g,mod)]+1 for a in mats] for g in (x,y,z)])

generators=[list(XX),list(YY),list(range(1,len(XX)+1))]
# Retain the first signed descent detector too; it need not factor through
# the second envelope because the original modular frame has a central ghost.
for mod in (3,4):
    mats=[(a,b,c,e) for a in range(mod) for b in range(mod) for c in range(mod) for e in range(mod) if (a*e-b*c)%mod==1]
    idx={a:i for i,a in enumerate(mats)}
    S=(0,1,mod-1,0)
    tau=(1,mod-1,0,1)
    triple=(S,tau,inv(mm(S,tau,mod),mod))
    for ai in range(3):
        for bi in range(3):
            if ai==bi:continue
            off=len(generators[0])
            for target,g in zip(generators,(triple[ai],triple[bi],I)):
                target.extend(off+idx[mm(a,g,mod)]+1 for a in mats)
detector_degree=len(generators[0])
DX,DY=generators[0].copy(),generators[1].copy()
for part in parts:
    off=len(generators[0])
    for g,p in zip(generators,part):g.extend(off+j for j in p)
header='\n'.join(f'{name}:=PermList({value});;' for name,value in zip(('PBC_ghost_x','PBC_ghost_y','PBC_ghost_target'),generators))
body=r'''
PBC_ghost_G:=Group(PBC_ghost_x,PBC_ghost_y);;
Print("joint_group_order ",Size(PBC_ghost_G),"\n");
PBC_ghost_D:=DerivedSubgroup(PBC_ghost_G);;
Print("ghost_member ",PBC_ghost_target in PBC_ghost_G," derived_member ",PBC_ghost_target in PBC_ghost_D,"\n");
PBC_ghost_P:=GroupHomomorphismByImages(PBC_ghost_G,Group(PBC_DX,PBC_DY),[PBC_ghost_x,PBC_ghost_y],[PBC_DX,PBC_DY]);;
Print("ghost_kernel_order ",Size(Kernel(PBC_ghost_P)),"\n");
Assert(0,PBC_ghost_target in PBC_ghost_D);
PrintTo("LM8_PUSH/code/pbc_iterated_ghost_certificate.json","{\n\"joint_order\":",Size(PBC_ghost_G),",\n\"detector_order\":",Size(Image(PBC_ghost_P)),",\n\"kernel_order\":",Size(Kernel(PBC_ghost_P)),",\n\"target_in_derived\":true,\n\"original_mod3_value\":\"-I\",\n\"original_mod4_value\":\"I\",\n\"first_and_second_detector_values\":\"identity\"\n}\n");
QUIT;
'''
prefix=f'PBC_DX:=PermList({DX});;\nPBC_DY:=PermList({DY});;\n'
(HERE/'pbc_iterated_ghost.g').write_text(prefix+header+'\n'+body)
print(json.dumps({'degree':len(generators[0]),'scope':'Exact original-frame kernel test after two pullbacks'},indent=2))
