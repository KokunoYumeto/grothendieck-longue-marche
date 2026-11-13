#!/usr/bin/env python3
"""Attempt to extend the certified integral class12 Hall word by weight13 only.
A failure here is an obstruction for that particular lower jet, not for q7.
Exact sparse class13 matrix is read from the independent full-system checkpoint.
Uses python-flint0.9.0. HNF is limited to180 seconds by an OS alarm.
"""
from pathlib import Path
import json,gzip,time,signal
from math import lcm
from flint import fmpz_mat,nmod_mat
from e_hall_core import lyndon,Q,label,defects,plus,ev
base=Path(__file__).resolve().parent;start=time.time()
with gzip.open(base/'e_exceptional_matrix_13.json.gz','rt') as f:d=json.load(f)
u=[w for n in range(8,14) for w in lyndon(n)]
old=json.loads((base/'e_exceptional_jets_12.json').read_text())['stages'][-1]['combined_jet']['hall_coordinates']
old={w:int(v) for w,v in old.items()}
prefix=[old.get(label(w),0) for w in u if len(w)<13];nprev=len(prefix)
rowstart=d['nrows']-2*len(lyndon(13));nr=d['nrows']-rowstart;nc=len(u)-nprev
A=fmpz_mat(nr,nc);b=fmpz_mat(nr,1);origb=dict(d['rhs_sparse'])
for i in range(rowstart,d['nrows']):
    v=origb.get(i,0)
    for j,a in d['rows_sparse'][i]:
        if j<nprev:v-=a*prefix[j]
        else:A[i-rowstart,j-nprev]=a
    b[i-rowstart,0]=v
rr,rank=nmod_mat(A.transpose(),1000003).rref()
ids=[next(j for j in range(rr.ncols()) if rr[i,j]) for i in range(rank)]
assert A.rank()==rank
M=fmpz_mat([[A[i,j] for j in range(nc)] for i in ids]);y=fmpz_mat([[b[i,0]] for i in ids])
print('homogeneous weight13 matrix',nr,nc,'rank',rank,'seconds',time.time()-start,flush=True)
signal.signal(signal.SIGALRM,signal.SIG_DFL);signal.alarm(180)
H,T=M.transpose().hnf(transform=True)
signal.alarm(0)
H0=fmpz_mat([[H[i,j] for j in range(rank)] for i in range(rank)])
c=H0.transpose().solve(y);den=lcm(*[int(c[i,0].denominator) for i in range(rank)])
print('fixed class12 jet extension multiplier',den,'seconds',time.time()-start,flush=True)
ic=fmpz_mat([[int(den*c[i,0])] for i in range(rank)])
lift=fmpz_mat([[T[i,j] for i in range(rank)] for j in range(T.ncols())]);v=lift*ic
assert A*v==den*b
out={'class':13,'method':'Fixed certified class12 integral word; correction in homogeneous weight13 only','rank':rank,'rows':nr,'variables':nc,'minimum_multiplier_for_this_fixed_lower_jet':den,'full_q7_lifting_obstruction_claimed':False}
if den==1:
    coords=dict(Q)
    coords.update({w:old[label(w)] for w in u[:nprev] if label(w) in old})
    coords.update({w:int(v[i,0]) for i,w in enumerate(u[nprev:]) if v[i,0]})
    total=[{},{}]
    for j,(w,cw) in enumerate(coords.items()):
        for k,dd in enumerate(defects(w,13)):total[k]=plus(total[k],dd,cw)
        if j%50==0:
            ev.cache_clear();print('independent full-word verification',j,'/',len(coords),'seconds',time.time()-start,flush=True)
    assert not total[0] and not total[1]
    out.update({'minimum_leading_multiplier':1,'hall_coordinates':{label(w):v for w,v in coords.items()},'full_associative_two_cycle_defect':0,'full_associative_three_cycle_defect':0})
else:
    # Record the exact fractional image-lattice coordinate that obstructs
    # lifting this fixed lower jet without a denominator; no global claim.
    out['nonintegral_hnf_coordinates']={str(i):str(c[i,0]) for i in range(rank) if c[i,0].denominator!=1}
out['seconds']=round(time.time()-start,3)
(base/'e_exceptional_extend12.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',den,'seconds',out['seconds'],flush=True)
