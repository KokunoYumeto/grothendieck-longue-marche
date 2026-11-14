#!/usr/bin/env python3
"""Universal class-two exponent-four refinement at 2, retaining N_ab/3.
Exact cusp obstruction, finite centralizer freedom, and multiplier 1/73.
The source of the kernel module is the free class-two exponent-four group,
whose squares and commutators give dimension 97+binomial(97,2)=4753.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,subprocess,time
import numpy as np

here=Path(__file__).resolve().parent;library=here/'de_gf3.so'
subprocess.run(['cc','-O3','-shared','-fPIC',str(here/'de_gf3.c'),'-o',str(library)],check=True)
gf=ctypes.CDLL(str(library)).de_rref2
gf.argtypes=[ctypes.POINTER(ctypes.c_uint8),ctypes.c_int,ctypes.c_int,ctypes.POINTER(ctypes.c_int)];gf.restype=ctypes.c_int
def rref(a):
    a=np.ascontiguousarray(a%2,dtype=np.uint8);p=np.zeros(min(a.shape),dtype=np.int32)
    rank=gf(a.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*a.shape,p.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
    assert rank>=0;return a,p[:rank].tolist()
def nullspace(a):
    RR,p=rref(a);free=[j for j in range(a.shape[1]) if j not in p];K=np.zeros((a.shape[1],len(free)),dtype=np.uint8)
    for k,j in enumerate(free):K[j,k]=1;K[p,k]=RR[:len(p),j]
    assert not np.any(a@K%2);return K
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
v=d['d'];rng=np.random.default_rng(812026)
for shape in ((5,7),(12,9),(71,130),(70,129)):
    A=rng.integers(0,2,size=shape);RR,p=rref(A);R2,p2=v['rref'](A,2);assert p==p2 and np.array_equal(RR,R2)
print('GF2 routine independently checked on four rectangular matrices.',flush=True)
C,chords=v['C'],v['chords'];n=97;I=np.eye(n,dtype=np.uint8)
S=(v['act'](v['ss'],C)[chords]%2).astype(np.uint8);R=(v['act'](v['rr'],C)[chords]%2).astype(np.uint8)
upper=np.triu_indices(n,1);nw=n+len(upper[0]);assert nw==4753
print('Constructing Q-invariant quadratic forms, dimension',nw,flush=True)
D=np.zeros((2*nw,nw),dtype=np.uint8)
for k,A in enumerate((S,R)):
    block=D[k*nw:(k+1)*nw]
    block[:n,:n]=A.T
    for i in range(n):block[i,i]^=1
    for col,(i,j) in enumerate(zip(*upper),n):
        block[:n,col]=A[i]*A[j]
        block[n:,col]=(np.outer(A[i],A[j])+np.outer(A[j],A[i]))[upper]%2
        block[col,col]^=1
start=time.time();invariants=nullspace(D);ni=invariants.shape[1]
print('Q-invariant quadratic forms:',ni,'elimination seconds:',round(time.time()-start,3),flush=True)
np.savez_compressed(here/'de_class2_two_certificate.npz',S=S,R=R,D=D,invariants=invariants)
Q,unit,ss,rr=v['Q'],v['unit'],v['ss'],v['rr'];times=v['times'];rri=v['inverse'](rr);ci={Q[e]:j for j,e in enumerate(chords)}
def nword(w):
    q=unit;out=[]
    for a in w:
        qn=times(q,ss if a==0 else rr if a==1 else rri)
        if a:
            if q in ci:out.append(ci[q]+1)
            if qn in ci:out.append(-ci[qn]-1)
        q=qn
    assert q==unit;return out
def kernel_coordinate(w):
    a=np.zeros(n,dtype=np.int64);z=np.zeros((n,n),dtype=np.uint8)
    for t in nword(w):
        k=abs(t)-1;z[k,k+1:]^=(a[k+1:]%2).astype(np.uint8);a[k]=(a[k]+(1 if t>0 else -1))%4
    assert not np.any(a%2)
    return np.concatenate(((a//2).astype(np.uint8),z[upper]))
def obstruction(w):return kernel_coordinate(w)@invariants%2
def from_v(a):
    out=[]
    for i,c in enumerate(a):out+=d['Nwords'][i]*(3*int(c))
    return out
fix_s=nullspace(S-I);fix_r=nullspace(R-I);var_s=[];var_r=[]
for a in fix_s.T:
    w=from_v(a);var_s.append(obstruction(w+[0]+d['binv'](w)+[0]))
for a in fix_r.T:
    w=from_v(a);var_r.append(obstruction(w+[1]+d['binv'](w)+[-1]))
var_s=np.stack(var_s,axis=1);var_r=np.stack(var_r,axis=1);cusp=obstruction([0,1]*72)
print('Centralizer ranks s,r and multiplier column:',len(rref(var_s)[1]),len(rref(var_r)[1]),int(np.any(cusp)),flush=True)
assert not np.any(var_r)
variation=np.column_stack((var_s,var_r,cusp));vr=len(rref(variation)[1]);print('Combined variation rank:',vr,flush=True)
def solve(b):
    RR,p=rref(np.column_stack((variation,b)))
    if variation.shape[1] in p:return None
    sol=np.zeros(variation.shape[1],dtype=np.uint8);sol[p]=RR[:len(p),-1]
    assert np.array_equal(variation@sol%2,b);return sol.tolist()
cert=json.loads((here/'de_source/d_cm_shadow.json').read_text())['pairs'];records=[];counts=[0,0]
for j,rec in enumerate([a for a in cert if 'mod6_beta_cycles' in a]):
    A,beta=v['representative'](rec['A']),v['representative'](rec['beta']);wa=[];wb=[]
    for i,w in enumerate(d['Nwords']):wa+=w*rec['mod6_A_cycles'].get(str(i),0);wb+=w*rec['mod6_beta_cycles'].get(str(i),0)
    wa+=d['Bpaths'][A];wb+=d['Bpaths'][beta]
    error=wb+[0]+d['binv'](wb)+wa+[1]+d['binv'](wa)+[-1,0]
    ob=obstruction(error);sol=solve(ob);missing=bool(rec['missing_coset']);counts[int(missing)]+=sol is not None
    row={'certificate_index':j,'missing_coset':missing,'obstruction':ob.tolist(),'passes_peripheral_cusp_test':sol is not None,'variation_solution':sol};records.append(row);print(json.dumps(row),flush=True)
out={'refinement':'B / ((gamma3(N_B) N_B^4) intersect (N_B-prime N_B^3))','kernel_over_G6_dimension_F2':nw,'Q_invariant_quadratic_forms':ni,'s_centralizer_rank':len(rref(var_s)[1]),'r_centralizer_rank':len(rref(var_r)[1]),'combined_variation_rank':vr,'cusp_order_bound':144,'pass_counts_by_CM_coset':counts,'records':records,'scope':'Peripheral cusp-lift test. Arbitrary finite gentle shadows need not preserve the r and s conjugacy classes; no unqualified full finite-shadow-image claim.'}
(here/'de_class2_two.json').write_text(json.dumps(out,indent=2)+'\n');print('Completed exponent-four refinement:',counts,flush=True)
