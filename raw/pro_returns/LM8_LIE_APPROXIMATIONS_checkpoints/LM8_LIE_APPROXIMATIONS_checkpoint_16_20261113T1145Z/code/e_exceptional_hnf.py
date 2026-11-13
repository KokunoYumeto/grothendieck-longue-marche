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

# H=T M^t, T unimodular. The nonzero rows H0 are a basis of the
# integer row lattice; the bottom rows of T are a saturated kernel.
H,T=M.transpose().hnf(transform=True)
assert H.is_hnf()
assert all(not H[i,j] for i in range(rank,H.nrows()) for j in range(H.ncols()))
H0=fmpz_mat([[H[i,j] for j in range(rank)] for i in range(rank)])
c=H0.transpose().solve(y)
den=lcm(*[int(c[i,0].denominator) for i in range(rank)])
ic=fmpz_mat([[int(den*c[i,0])] for i in range(rank)])
lift=fmpz_mat([[T[i,j] for i in range(rank)] for j in range(T.ncols())])
v=lift*ic
assert M*v==den*y
assert A*v==den*b
print('minimum integral leading multiplier',den,'elapsed',round(time.time()-start,2),flush=True)

# A kernel check certifies that all choices of the omitted free exponents
# remain available, and records a second exact rank certificate.
K=fmpz_mat([[T[i,j] for i in range(rank,T.nrows())] for j in range(T.ncols())])
assert (A*K).is_zero()
assert K.rank()==A.ncols()-rank

# LLL reduction of the augmented coset lattice is only certificate
# shortening; the subsequent exact equations independently validate it.
kernel_rows=K.transpose().tolist()
old=[int(v[i,0]) for i in range(v.nrows())]
if kernel_rows:
    aug=fmpz_mat([list(map(int,row))+[0] for row in kernel_rows]+[old+[1]])
    reduced=aug.lll()
    choices=[]
    for i in range(reduced.nrows()):
        sign=int(reduced[i,reduced.ncols()-1])
        if abs(sign)==1:
            vv=[sign*int(reduced[i,j]) for j in range(A.ncols())]
            choices.append(vv)
    if choices:
        old=min(choices+[old],key=lambda a:sum(x*x for x in a))
        v=fmpz_mat([[x] for x in old])
        assert A*v==den*b
print('integral certificate maximum exponent',max(map(abs,old)),flush=True)

# Final verification does not retain or reuse the coefficient matrix.
# It expands all substituted group commutators again and accumulates
# every associative word in the two cycle defects.
total=[{},{}]
coords=dict(Q)
coords={w:den*a for w,a in coords.items()}
coords.update({w:a for w,a in zip(unknowns,old) if a})
for j,(w,cw) in enumerate(coords.items()):
    for kind,d in enumerate(defects(w,N)):total[kind]=plus(total[kind],d,cw)
    if j%50==0:
        ev.cache_clear()
        print('full-word check',j,'/',len(coords),'elapsed',round(time.time()-start,2),flush=True)
assert not total[0] and not total[1]
answer={
    'method':'Transformed integral Hermite normal form; exact regenerated full associative-word verification',
    'class':N,'variables':A.ncols(),'lyndon_equations':A.nrows(),
    'rank':rank,'free_parameters':A.ncols()-rank,
    'minimum_integral_leading_multiplier':den,
    'q7':{label(w):a for w,a in Q.items()},
    'group_commutator':'g h g^-1 h^-1','z':'(xy)^-1',
    'equations':['f(y,x)f(x,y)=1','f(z,x)f(y,z)f(x,y)=1'],
    'hall_coordinates':{label(w):a for w,a in zip(unknowns,old) if a},
    'hermite_coordinates':{str(i):str(c[i,0]) for i in range(rank) if c[i,0]},
    'selected_rows':[{'cycle':rowkeys[i][0]+1,'word':label(rowkeys[i][1])} for i in ids],
    'full_associative_word_verification':True,'infinite_lift_claimed':False,
    'elapsed_seconds':time.time()-start,
    'dependency':'python-flint 0.9.0; hnf(transform=True), rref, rank, exact integer multiplication',
}
(OUT/f'e_exceptional_hnf_{N}.json').write_text(json.dumps(answer,indent=2))
print('FINISHED',round(time.time()-start,3),'seconds; both group cycles identically zero.',flush=True)
