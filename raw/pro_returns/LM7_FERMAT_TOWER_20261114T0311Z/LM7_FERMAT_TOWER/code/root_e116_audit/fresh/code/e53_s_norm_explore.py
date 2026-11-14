#!/usr/bin/env python3
"""Actual S-unit characters for the first pure-53 norm; no upper BNF."""
from pathlib import Path
from fractions import Fraction as F
import json

HERE=Path(__file__).resolve().parent
data=[json.loads(x) for x in (HERE/'e_small_inert_units.out').read_text().splitlines() if x.startswith('{')]
rec=next(x for x in data if x.get('type')=='unit_coordinates' and x['ell']==53)
prime_records=[json.loads(x) for x in (HERE/'e53_prime_columns.out').read_text().splitlines() if x.startswith('{')]
raw_columns=rec['columns_in_1_a_a2_z_za_za2']+[x['coordinates'] for x in prime_records if x['type']=='prime_generator']+[['0','1','0','0','0','0']]
cols=[[F(a) for a in x] for x in raw_columns]
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def scale(a,b):return (a[0]*b,a[1]*b)
def powr(a,n):
    y=(1,0)
    while n:
        if n&1:y=mul(y,a)
        a=mul(a,a);n//=2
    return y
def modf(x,p):
    x=F(x);return x.numerator*pow(x.denominator,-1,p)%p
def ev(c,a):
    a2=mul(a,a)
    return add(add((c[0],c[3]),mul((c[1],c[4]),a)),mul((c[2],c[5]),a2))
def mpow(a,n,p):
    y=(1,0)
    while n:
        if n&1:y=tuple(x%p for x in mul(y,a))
        a=tuple(x%p for x in mul(a,a));n//=2
    return y

b=-1
for n in range(3,13):
    q=((53-b**3)//3**n*pow(b*b,-1,3))%3
    b+=q*3**(n-1)
    assert (b**3-53)%3**(n+1)==0
assert (b+1)%9==0
wild=[];actual_norm_residues=[]
for i in range(3):
    aa=scale(powr((0,1),i),b)
    row=[];norms=[]
    for c in cols:
        x,y=ev(c,aa)
        nnq=x*x-x*y+y*y
        vv=0
        while nnq.numerator%3==0:nnq/=3;vv+=1
        while nnq.denominator%3==0:nnq*=3;vv-=1
        assert vv>=0
        nn=modf(nnq,9)
        assert nn%3==1
        norms.append(nn)
        row.append(i*((pow(nn,-1,9)-1)//3)%3)
    wild.append(row);actual_norm_residues.append(norms)
tame=[];residues=[]
for index,c in enumerate(cols):
    if index==6:
        tame.append(0);residues.append('literal uniformizer alpha; alternating symbol zero');continue
    z=tuple(modf(a,53) for a in ev(c,(0,0)))
    test=mpow(z,(53**2-1)//3,53)
    ex=[i for i in range(3) if mpow((0,1),i,53)==test]
    assert len(ex)==1
    tame.append(-ex[0]%3);residues.append(z)
matrix=wild+[tame]
assert all(sum(matrix[i][j] for i in range(4))%3==0 for j in range(7))
def rank3(M):
    a=[[x%3 for x in r] for r in M];r=0
    for c in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        q=pow(a[r][c],-1,3);a[r]=[x*q%3 for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                q=a[k][c];a[k]=[(x-q*y)%3 for x,y in zip(a[k],a[r])]
        r+=1
    return r
out={'statement':'E116 lower-53 exploration','status':'PASS',
     'field':'M1=Q(zeta3,cuberoot53)',
     'next_field':'M2=Q(zeta3,ninthroot53)',
     'rational_cubic_root_mod_3pow12':b%(3**12),
     'S_unit_columns':raw_columns,
     'quadratic_local_norms_mod9_at_three_places':actual_norm_residues,
     'ell_unit_residues':residues,
     'S_unit_cubic_character_matrix':matrix,
     'S_unit_character_rank':rank3(matrix),
     'scope':'The first row is the split three-prime. The remaining wild characters are evaluated from the actual cyclotomic local Artin action on zeta9, and the ell character is arithmetic tame reciprocity. No upper class group or stabilization is inferred unless the proved ambiguity formula yields it.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'e53_s_norm_explore.json').write_text(text);print(text,end='')
