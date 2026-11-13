#!/usr/bin/env python3
"""Exact integral Hall jets, using transformed integer Hermite normal form.

Requires python-flint==0.9.0.  The earlier e_exceptional_jets.py is an
independent rational/local elimination implementation using only SymPy.
This program retains every Hall variable in weights 8..N, N<14.
It computes a full integral image lattice by HNF, then checks every
associative-word coefficient of the resulting genuine group equations.
"""
from pathlib import Path
from math import lcm
from fractions import Fraction
import sys,json,time
from flint import fmpz_mat,nmod_mat
from e_hall_core import lyndon,ev,defects,label,Q,plus

N=int(sys.argv[1]) if len(sys.argv)>1 else 13
assert 7<N<14
OUT=Path(__file__).resolve().parent
start=time.time()
unknowns=[w for n in range(8,N+1) for w in lyndon(n)]
rowkeys=[(kind,w) for n in range(7,N+1) for kind in (0,1) for w in lyndon(n)]
index={key:i for i,key in enumerate(rowkeys)}
A=fmpz_mat(len(rowkeys),len(unknowns));b=fmpz_mat(len(rowkeys),1)
for w,c in Q.items():
    for kind,d in enumerate(defects(w,N)):
        for v,a in d.items():
            if (kind,v) in index:
                i=index[kind,v];b[i,0]-=c*a
for j,w in enumerate(unknowns):
    for kind,d in enumerate(defects(w,N)):
        for v,a in d.items():
            if (kind,v) in index:A[index[kind,v],j]=a
    if j%25==0:
        ev.cache_clear()
        print('column',j,'/',len(unknowns),'elapsed',round(time.time()-start,2),flush=True)
ev.cache_clear()
print('built Lyndon matrix',A.nrows(),A.ncols(),'elapsed',round(time.time()-start,2),flush=True)

# A modular row basis is certified complete by an independent exact rank.
rr,rank_mod=nmod_mat(A.transpose(),1000003).rref()
ids=[]
for i in range(rank_mod):
    ids.append(next(j for j in range(rr.ncols()) if rr[i,j]))
rank=A.rank()
assert rank==rank_mod
M=fmpz_mat([[A[i,j] for j in range(A.ncols())] for i in ids])
y=fmpz_mat([[b[i,0]] for i in ids])
print('exact rank',rank,'nullity',A.ncols()-rank,'elapsed',round(time.time()-start,2),flush=True)
import pickle
checkpoint_dir=OUT.parent.parent/'e_work'
checkpoint_dir.mkdir(exist_ok=True)
with (checkpoint_dir/f'exceptional_matrix_{N}.pkl').open('wb') as fh:
    pickle.dump({'N':N,'A':A.tolist(),'b':b.tolist(),'row_basis':ids,'rank':rank},fh,protocol=4)
print('saved exact matrix checkpoint',flush=True)


# Compute only the integer image lattice first.  Avoiding the full 1336x1336
# unimodular transform permits FLINT's fast modular HNF implementation.
H=M.transpose().hnf()
assert H.is_hnf()
H0=fmpz_mat([[H[i,j] for j in range(rank)] for i in range(rank)])
yprime=H0.transpose().solve(y)
minimum=lcm(*[int(yprime[i,0].denominator) for i in range(rank)])
print('minimum integral leading multiplier',minimum,'elapsed',round(time.time()-start,2),flush=True)
# Columns of R span Z^rank by the defining property of the row HNF.
Rrat=H0.transpose().solve(M)
assert all(Rrat[i,j].denominator==1 for i in range(rank) for j in range(M.ncols()))
R=fmpz_mat([[int(Rrat[i,j]) for j in range(M.ncols())] for i in range(rank)])
z=fmpz_mat([[int(minimum*yprime[i,0])] for i in range(rank)])
assert H0.transpose()*R==M and H0.transpose()*z==minimum*y
print('normalized saturated image coordinates','elapsed',round(time.time()-start,2),flush=True)
# A full-rank minor modulo p gives a rational solution with p-unit denominator.
# Repeating at a prime divisor of the gcd of existing denominators forces
# that gcd to drop, and eventually gives an integral Bezout combination.
from math import gcd

def egcd(a,b):
    if not b:return a,1,0
    g,x,y=egcd(b,a%b)
    return g,y,x-(a//b)*y

def smallest_prime(n):
    if n%2==0:return 2
    p=3
    while p*p<=n:
        if n%p==0:return p
        p+=2
    return n

certificates=[];D=0;combined=None;p=2
while D!=1:
    rr,rp=nmod_mat(R,p).rref()
    assert rp==rank
    pivs=[next(j for j in range(rr.ncols()) if rr[i,j]) for i in range(rank)]
    B=fmpz_mat([[R[i,j] for j in pivs] for i in range(rank)])
    v=B.solve(z)
    d=lcm(*[int(v[i,0].denominator) for i in range(rank)])
    assert gcd(d,p)==1
    vv=[0]*M.ncols()
    for j,k in enumerate(pivs):vv[k]=int(d*v[j,0])
    vi=fmpz_mat([[c] for c in vv])
    assert R*vi==d*z and A*vi==minimum*d*b
    if combined is None:D=d;combined=vi;weights=[1]
    else:
        Dnew,s,t=egcd(D,d)
        combined=s*combined+t*vi
        weights=[s*w for w in weights]+[t];D=Dnew
    certificates.append({'prime':p,'denominator':d,'columns':pivs})
    print('local minor prime',p,'denominator',d,'gcd',D,'elapsed',round(time.time()-start,2),flush=True)
    if D!=1:p=smallest_prime(D)
v=combined
assert A*v==minimum*b
old=[int(v[i,0]) for i in range(v.nrows())]
print('integral certificate maximum exponent',max(map(abs,old)),flush=True)
# Independent final verification in the complete truncated associative algebra.
total=[{},{}]
coords={w:minimum*a for w,a in Q.items()}
coords.update({w:a for w,a in zip(unknowns,old) if a})
for j,(w,cw) in enumerate(coords.items()):
    for kind,d in enumerate(defects(w,N)):total[kind]=plus(total[kind],d,cw)
    if j%50==0:
        ev.cache_clear()
        print('verified commutator',j,'/',len(coords),'elapsed',round(time.time()-start,2),flush=True)
assert not total[0] and not total[1]
result={'class':N,'field':'Z','minimum_leading_multiplier':minimum,
        'rows':len(rowkeys),'unknowns':len(unknowns),'rank':rank,
        'nullity':len(unknowns)-rank,'method':'Untransformed image HNF, saturated lattice coordinates, local minors, integral Bezout combination',
        'minor_certificates':certificates,'bezout_coefficients':weights,
        'hall_coordinates':{label(w):a for w,a in coords.items()},
        'full_associative_two_cycle_defect':0,'full_associative_three_cycle_defect':0,
        'max_abs_exponent':max(map(abs,old)),'seconds':round(time.time()-start,3)}
(OUT/f'e_exceptional_lattice_{N}.json').write_text(json.dumps(result,indent=2)+'\n')
print('COMPLETE',N,'minimum multiplier',minimum,'seconds',result['seconds'],flush=True)
