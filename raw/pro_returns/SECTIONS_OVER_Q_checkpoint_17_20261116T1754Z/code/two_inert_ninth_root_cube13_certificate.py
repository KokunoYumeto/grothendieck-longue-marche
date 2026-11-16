#!/usr/bin/env python3
"""Independent rational cube and finite residue rank for a new M unit."""
from pathlib import Path
from fractions import Fraction as F
from math import lcm,gcd
from functools import reduce
import json,re,sys
import sympy as S
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parent;d=649;rad=3*d**6;N=54
raw=(B/'two_inert_ninth_root_cube13_coordinates_output.txt').read_text()
rr=[F(x.strip())for x in re.search(r'^NATURAL_ROOT (.*)$',raw,re.M)[1][1:-1].split(',')]
assert len(rr)==54
base=json.loads((B/'two_inert_zeta9_base_units_certificate_data.json').read_text())
nat=base['natural_unit_numerators']
us=[[F(x)for x in u['candidate']]for u in json.loads(
    (B/'two_inert_relative_unit_repair_certificate_data.json').read_text())['units']]
rs=[[F(x)for x in r]for r in json.loads(
    (B/'two_inert_level2_anti_cube_root_certificate_data.json').read_text())['roots']]
def normpair(v,den):
    g=reduce(gcd,[den]+v);return ([x//g for x in v],den//g)
def cv(cs):
    den=lcm(*(x.denominator for x in cs))
    return normpair([x.numerator*(den//x.denominator)for x in cs],den)
def mul(a,b):
    av,ad=a;bv,bd=b;c=[[0]*11 for _ in range(17)]
    for i,x in enumerate(av):
      if x:
       for j,y in enumerate(bv):
        if y:c[i//6+j//6][i%6+j%6]+=x*y
    for i in range(17):
      for j in range(10,5,-1):
       if c[i][j]:
        c[i][j-3]-=c[i][j];c[i][j-6]-=c[i][j]
    for i in range(16,8,-1):
      for j in range(6):c[i-9][j]+=rad*c[i][j]
    return normpair([c[i][j]for i in range(9)for j in range(6)],ad*bd)
one=([1]+[0]*53,1)
def prod(vs):
    r=one
    for v in vs:r=mul(r,v)
    return r
es=[]
for row in nat:
    a=[F(0)]*54
    for i,c in enumerate(row):a[3*(i//6)*6+i%6]=F(c,3*d**(2*(i//6)))
    es.append(cv(a))
uv=[]
for u in us:
    a=[F(0)]*54
    for i,c in enumerate(u):a[6*i]=c
    uv.append(cv(a))
r=cv(rr)
left=prod([r,r,r,es[2],es[5],es[8]])
right=prod([es[0],es[4],es[7],uv[1],uv[3]])
assert left==right
print('PASS: literal rational identity r^3*e3*e6*e9=e1*e5*e8*u2*u4 in M.',flush=True)
print('PASS: r and r^-1 are integral, by their monic cubic equations over certified units.',flush=True)

def ev(cs,t,p):
    out=0
    for c in reversed(cs):out=(out*t+c)%p
    return out
def red(cs,p):return [x.numerator*pow(x.denominator,-1,p)%p for x in cs]
rows=[];witnesses=[];ech={};count=0
for pp in S.primerange(19,20000):
 p=int(pp)
 if p%9!=1 or d%p==0 or any(c.denominator%p==0 for cs in us+rs+[rr]for c in cs):continue
 ts=S.nthroot_mod(rad%p,9,p,all_roots=True)
 if not ts:continue
 z0=pow(int(S.primitive_root(p)),(p-1)//9,p)
 um=[red(cs,p)for cs in us];rm=[red(cs,p)for cs in rs];root=red(rr,p)
 for t in map(int,ts):
  for z in [pow(z0,k,p)for k in (1,2,4,5,7,8)]:
   om=pow(z,3,p);alpha=pow(t,3,p)*pow(d*d,-1,p)%p
   mon=[pow(alpha,i,p)*pow(z,j,p)%p for i in range(3)for j in range(6)]
   vals=[sum(c*m for c,m in zip(row,mon))*pow(3,-1,p)%p for row in nat]
   for j in range(3):
    tj=t*pow(z,j,p)%p;aj=pow(tj,3,p)*pow(d*d,-1,p)%p
    w=pow(tj,5,p)*pow(d**3*(om-1),-1,p)%p
    pi=aj*aj*pow(om-1,-1,p)%p;tp=-om*pi%p
    v=(1+pi)*pow(1+pi*pi,-1,p)%p;tv=(1+tp)*pow(1+tp*tp,-1,p)%p
    vals += [ev(cs,tj,p)for cs in um]+[v*pow(tv,-1,p)%p]+[ev(cs,w,p)for cs in rm]
   rv=sum(root[6*i+j]*pow(t,i,p)*pow(z,j,p)for i in range(9)for j in range(6))%p
   assert rv and pow(rv,3,p)*vals[2]*vals[5]*vals[8]%p==vals[0]*vals[4]*vals[7]*vals[10]*vals[12]%p
   orbit=[sum(root[6*i+j]*pow(t*pow(z,k,p)%p,i,p)*pow(z,j,p)
              for i in range(9)for j in range(6))%p for k in range(9)]
   assert orbit[0]==rv and all(orbit)
   vals.extend(orbit);assert all(vals)
   powers=[1,om,om*om%p];row=[powers.index(pow(v,(p-1)//3,p))for v in vals]
   count+=1;v=row[:]
   for k,b in sorted(ech.items()):
    c=v[k]
    if c:v=[(x-c*y)%3 for x,y in zip(v,b)]
   k=next((i for i,x in enumerate(v)if x),None)
   if k is not None:
    iv=pow(v[k],-1,3);ech[k]=[x*iv%3 for x in v]
    rows.append(row);witnesses.append({'p':p,'t':t,'zeta9':z,'root_value':rv,'row':row})
    print('INDEPENDENT',len(rows),p,t,z,flush=True)
   if len(rows)>=27:break
  if len(rows)>=27:break
 if len(rows)>=27:break
print('RESULT: enlarged finite residue rank',len(rows),'after',count,'maps.',flush=True)
out={'natural_root_coefficients':[str(x)for x in rr],
     'root_cube_identity':'r^3*e3*e6*e9=e1*e5*e8*u2*u4',
     'new_units':'g^j(r), 0<=j<9, g(t)=zeta9*t and g(zeta9)=zeta9',
     'rank':len(rows),'matrix':rows,'witnesses':witnesses,'finite_maps_checked':count,
     'scope':'Exact new global unit and finite residue rank; no full unit lattice assertion.'}
(B/'two_inert_ninth_root_cube13_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
