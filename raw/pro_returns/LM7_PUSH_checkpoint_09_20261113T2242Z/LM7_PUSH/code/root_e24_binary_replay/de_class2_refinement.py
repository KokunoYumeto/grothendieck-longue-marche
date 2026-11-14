#!/usr/bin/env python3
"""Universal class-two exponent-three refinement of the N_B homology cover.

Tests the exact cusp obstruction in Lambda^2(F3^97), dimension 4656.
The dual coinvariants are computed using the Jordan blocks of r and an
independently checked bit-packed exact GF3 elimination routine.
"""
from contextlib import redirect_stdout
from pathlib import Path
from collections import Counter
import ctypes,io,json,runpy,subprocess,time
import numpy as np

here=Path(__file__).resolve().parent
library=here/'de_gf3.so'
subprocess.run(['cc','-O3','-shared','-fPIC',str(here/'de_gf3.c'),'-o',str(library)],check=True)
gf=ctypes.CDLL(str(library)).de_rref3
gf.argtypes=[ctypes.POINTER(ctypes.c_uint8),ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_int)];gf.restype=ctypes.c_int
def rref(a):
    a=np.ascontiguousarray(a%3,dtype=np.uint8);p=np.zeros(min(a.shape),dtype=np.int32)
    rank=gf(a.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*a.shape,p.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
    assert rank>=0
    return a.astype(np.int64),p[:rank].tolist()
def nullspace(a):
    R,p=rref(a);nc=a.shape[1];free=[j for j in range(nc) if j not in p]
    K=np.zeros((nc,len(free)),dtype=np.int64)
    for k,j in enumerate(free):K[j,k]=1;K[p,k]=-R[:len(p),j]%3
    assert not np.any(a@K%3)
    return K
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
v=d['d'];rng=np.random.default_rng(712026)
for shape in ((5,7),(12,9),(71,130),(70,129)):
    A=rng.integers(0,3,size=shape);R,p=rref(A);RR,pp=v['rref'](A,3)
    assert p==pp and np.array_equal(R,RR)
print('GF3 bit-plane routine agrees with independent Python elimination on four rectangular tests.',flush=True)
C,chords=v['C'],v['chords'];n=97
S=v['act'](v['ss'],C)[chords]%3;R=v['act'](v['rr'],C)[chords]%3
I=np.eye(n,dtype=np.int64);Z=(R-I)%3;Z2=Z@Z%3
assert np.array_equal(S@S%3,I) and not np.any(Z2@Z%3)
class Span:
    def __init__(self):self.rows={}
    def contains(self,x):
        x=x.copy()%3
        for p,b in sorted(self.rows.items()):x=(x-x[p]*b)%3
        return not np.any(x)
    def add(self,x):
        x=x.copy()%3
        for p,b in sorted(self.rows.items()):x=(x-x[p]*b)%3
        ix=np.flatnonzero(x);assert len(ix);p=int(ix[0]);x=x*int(x[p])%3;self.rows[p]=x
span=Span();chains=[]
for j in range(n):
    a=Z2[:,j]
    if not span.contains(a):
        chain=[a,Z[:,j],I[:,j]];chains.append(chain)
        for b in chain:span.add(b)
for a in nullspace(Z2).T:
    b=Z@a%3
    if not span.contains(b):
        chains.append([b,a]);span.add(b);span.add(a)
for a in nullspace(Z).T:
    if not span.contains(a):chains.append([a]);span.add(a)
P=np.column_stack([x for chain in chains for x in chain]);assert P.shape==(n,n)
Pinv,piv=rref(np.column_stack((P,I)));assert piv[:n]==list(range(n));Pinv=Pinv[:,n:]
assert np.array_equal(Pinv@P%3,I)
J=Pinv@R@P%3;SJ=Pinv@S@P%3
expected=I.copy();blocks=[];start=0
for chain in chains:
    k=len(chain);blocks.append(list(range(start,start+k)))
    for j in range(k-1):expected[start+j,start+j+1]=1
    start+=k
assert np.array_equal(J,expected)
print('Order-three Jordan blocks:',dict(Counter(map(len,chains))),flush=True)
upper=np.triu_indices(n,1);nw=len(upper[0]);assert nw==4656
forms=[]
for bi,ids in enumerate(blocks):
    for bj in range(bi,len(blocks)):
        js=blocks[bj];allids=ids if bi==bj else ids+js;kk=len(allids)
        local=J[np.ix_(allids,allids)]
        positions=[(i,j) for i in range(len(ids)) for j in range(i+1,len(ids))] if bi==bj else [(i,len(ids)+j) for i in range(len(ids)) for j in range(len(js))]
        if not positions:continue
        templates=[];cols=[]
        for i,j in positions:
            B=np.zeros((kk,kk),dtype=np.int64);B[i,j]=1;B[j,i]=2
            templates.append(B);cols.append((local.T@B@local-B).reshape(-1)%3)
        kernel=nullspace(np.column_stack(cols))
        for coeff in kernel.T:
            B=sum((c*b for c,b in zip(coeff,templates)),np.zeros((kk,kk),dtype=np.int64))%3
            sparse=[(allids[i],allids[j],int(B[i,j])) for i in range(kk) for j in range(i+1,kk) if B[i,j]]
            forms.append(sparse)
nr=len(forms);print('Alternating forms invariant under r:',nr,flush=True)
D=np.zeros((nw,nr),dtype=np.uint8)
for j,sparse in enumerate(forms):
    B=np.zeros((n,n),dtype=np.int64);difference=np.zeros((n,n),dtype=np.int64)
    for a,b,c in sparse:
        B[a,b]=c;B[b,a]=-c
        difference+=c*(np.outer(SJ[a],SJ[b])-np.outer(SJ[b],SJ[a]))
    D[:,j]=((difference-B)%3)[upper]
start_time=time.time();invariants=nullspace(D);ninv=invariants.shape[1]
print('Q-invariant alternating forms:',ninv,'elimination seconds:',round(time.time()-start_time,3),flush=True)
# Save the exact dual certificate, enough to verify all claimed zeros.
np.savez_compressed(here/'de_class2_linear_certificate.npz',S=S,R=R,P=P,Pinv=Pinv,D=D,invariants=invariants)

Q,unit,ss,rr=v['Q'],v['unit'],v['ss'],v['rr'];times=v['times'];rri=v['inverse'](rr)
ci={Q[e]:j for j,e in enumerate(chords)}
def nword(w):
    q=unit;out=[]
    for a in w:
        qn=times(q,ss if a==0 else rr if a==1 else rri)
        if a:
            if q in ci:out.append(ci[q]+1)
            if qn in ci:out.append(-ci[qn]-1)
        q=qn
    assert q==unit
    return out
for j,w in enumerate(d['Nwords']):assert d['freered'](nword(w))==(j+1,)
def class2pair(w):
    a=np.zeros(n,dtype=np.int64);z=np.zeros((n,n),dtype=np.int64)
    for t in nword(w):
        k=abs(t)-1;sign=1 if t>0 else -1
        z[:,k]=(z[:,k]+2*sign*a)%3;z[k,:]=(z[k,:]-2*sign*a)%3
        a[k]=(a[k]+sign)%3
    return a,z
def class2(w):
    a,z=class2pair(w);assert not np.any(a);return z
invariant_matrices=[]
for coeff in invariants.T:
    B=np.zeros((n,n),dtype=np.int64)
    for scalar,sparse in zip(coeff,forms):
        for a,b,c in sparse:B[a,b]+=scalar*c;B[b,a]-=scalar*c
    B=Pinv.T@(B%3)@Pinv%3
    assert np.array_equal(S.T@B@S%3,B) and np.array_equal(R.T@B@R%3,B)
    invariant_matrices.append(B)
def dual_values(z):return np.array([sum((B[upper]*z[upper]).tolist())%3 for B in invariant_matrices],dtype=np.int64)
tau_r=[];tau_s=[]
for j,w in enumerate(d['Nwords']):
    ar,zr=class2pair([1]+w+[-1]);ass,zs=class2pair([0]+w+[0])
    assert np.array_equal(ar,R[:,j]) and np.array_equal(ass,S[:,j])
    tau_r.append(dual_values(zr));tau_s.append(dual_values(zs))
fix_r=nullspace(R-I);fix_s=nullspace(S-I)
variation_r=np.stack(tau_r,axis=1)@fix_r%3
variation_s=np.stack(tau_s,axis=1)@fix_s%3
Vr,pvr=rref(variation_r);vs_rank=len(rref(variation_s)[1]);vr_rank=len(pvr)
print('Centralizer variation ranks, r and s:',vr_rank,vs_rank,flush=True)
assert vs_rank==0
def solve_variation(target):
    aug=np.column_stack((variation_r,target));RR,pp=rref(aug)
    if variation_r.shape[1] in pp:return None
    coeff=np.zeros(variation_r.shape[1],dtype=np.int64)
    coeff[pp]=RR[:len(pp),-1]
    assert np.array_equal(variation_r@coeff%3,target%3)
    return (fix_r@coeff%3).tolist()
cert=json.loads((here/'de_source/d_cm_shadow.json').read_text())['pairs'];records=[];counts=[0,0]
for j,rec in enumerate([a for a in cert if 'mod6_beta_cycles' in a]):
    A,beta=v['representative'](rec['A']),v['representative'](rec['beta']);wa=[];wb=[]
    for i,w in enumerate(d['Nwords']):
        wa+=w*rec['mod6_A_cycles'].get(str(i),0);wb+=w*rec['mod6_beta_cycles'].get(str(i),0)
    wa+=d['Bpaths'][A];wb+=d['Bpaths'][beta]
    error=wb+[0]+d['binv'](wb)+wa+[1]+d['binv'](wa)+[-1,0]
    E=class2(error);EJ=Pinv@E@Pinv.T%3
    values=np.array([sum(c*EJ[a,b] for a,b,c in sparse)%3 for sparse in forms],dtype=np.int64)
    obstruction=values@invariants%3;assert np.array_equal(obstruction,dual_values(E))
    passes=not np.any(obstruction);missing=bool(rec['missing_coset']);variation=solve_variation(obstruction)
    counts[int(missing)]+=variation is not None
    record={'certificate_index':j,'missing_coset':missing,'fixed_conjugator_cusp_obstruction_vanishes':passes,'obstruction_coordinates':obstruction.tolist(),'passes_with_centralizer_freedom':variation is not None,'r_centralizer_adjustment_in_V':variation}
    records.append(record);print(json.dumps(record),flush=True)
out={'refinement':'kernel of N_B -> (N_B/(gamma_3 N_B N_B^3)) x (N_B^ab/2)','kernel_over_G6':'Lambda^2(F3^97)','kernel_dimension':nw,'r_Jordan_block_counts':dict(Counter(map(len,chains))),'r_invariant_forms':nr,'Q_invariant_alternating_forms':ninv,'r_centralizer_variation_rank':vr_rank,'s_centralizer_variation_rank':vs_rank,'pass_counts_by_CM_coset':counts,'records':records,'scope':'Exact cusp obstruction including all order-three-generator centralizer freedom. Generation after any such lift follows from the exterior-square map of the invertible N_B-ab mod3 action.'}
(here/'de_class2_refinement.json').write_text(json.dumps(out,indent=2)+'\n')
print('Completed class-two refinement test:',counts,flush=True)
