#!/usr/bin/env python3
"""Independent focused E108 identities, without importing the author program."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib, json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
x,y,k,X,Y,K,c,p,q=s.symbols('x y k X Y K c p q')
dx=x+c*X;dy=y+c*Y;dk=k+c*K
phi=lambda a,b,t: a*b/2+q*t*a+p*q*t*t/2
boundary=s.expand(c*c*phi(X,Y,K)-phi(dx,dy,dk)+phi(x,y,k))
omega=-q*k*c*X+p*k*c*Y+(x*c*Y-y*c*X)/2
assert s.expand((x+p*k)*c*(Y+q*K)+boundary-omega)==0
chars=[(1,1,1,1),(1,-1,1,-1),(1,-1,-1,1),(1,1,-1,-1)]
columns=[0]*2+[1]*3+[2]*3+[3]*3
wedge=Counter(tuple(a*b for a,b in zip(chars[columns[i]],chars[columns[j]]))
              for i,j in combinations(range(11),2))
assert [wedge[ch] for ch in chars]==[10,15,15,15]
assert sum(wedge[ch] for ch in chars if ch[-1]==-1)==30
t=s.symbols('t')
eps=1+t-t**3
assert s.rem(t**6*eps**2*(1-t)**4-2,t**4+1,t)==0
# Derive the actual class-two root-change formula directly in dimension three.
b=s.Matrix(s.symbols('b0:3'));m=s.Matrix(s.symbols('m0:3'))
def wedge3(u,v): return s.Matrix([u[0]*v[1]-u[1]*v[0],u[0]*v[2]-u[2]*v[0],u[1]*v[2]-u[2]*v[1]])
z=s.Matrix(s.symbols('z0:3'));Lm=s.Matrix(s.symbols('L0:3'))
u1=-m+b;zz1=z+wedge3(-m,b)/2
zz2=zz1+c*k*Lm+wedge3(u1,c*m)/2
assert all(s.expand(a)==0 for a in zz2-z-c*k*Lm+(1+c)*wedge3(m,b)/2)
sources={}
for fn in ['GuoQinSong_tame_zeta8.pdf','Kahn_descentegaloisienne.pdf']:
    path=ROOT/'research_e108'/'sources'/fn
    sources[fn]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'size':path.stat().st_size}
out={'status':'PASS','shifted_cup_identity':True,'character_multiplicities':[10,15,15,15],
     'odd_character_free_rank':30,'literal_norm_two_identity':True,
     'BCH_representative_transport':True,'source_files_read':sources,
     'scope':'Focused proof/source audit and independent identities; no author certificate replay.'}
(HERE/'check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
