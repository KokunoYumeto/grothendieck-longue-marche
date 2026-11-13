#!/usr/bin/env python3
"""Explicit instantiation of the S3-core refinement in LM7 D.26.

The first two fundamental cycles in the independently reconstructed graph
basis map to two transpositions. The finite quotient is represented in
G6 together with the induced S3 wreath representation over Q. Its kernel
over G6 is an exact F3 module, never enumerated as a group.
"""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
v=d['d'];Q,unit,ss,rr=v['Q'],v['unit'],v['ss'],v['rr']
times,inverse=v['times'],v['inverse'];index=v['index'];nq=len(Q)
shift=np.array([[index[times(q,g)] for q in Q] for g in Q],dtype=np.int64)
eid=index[unit];sid=index[ss];rid=index[rr]
eone=np.ones(nq,dtype=np.int64);bzero=np.zeros(nq,dtype=np.int64)
one=(eid,eone,bzero)
def mul(a,b):
    qa,ea,ba=a;qb,eb,bb=b;ix=shift[qa]
    return index[times(Q[qa],Q[qb])],(ea*eb[ix])%3,(ba+ea*bb[ix])%3
def inv(a):
    qa,ea,ba=a;qi=index[inverse(Q[qa])];ix=shift[qi]
    return qi,ea[ix].copy(),(-ea[ix]*ba[ix])%3
def power(a,k):
    if k<0:return power(inv(a),-k)
    out=one
    while k:
        if k&1:out=mul(out,a)
        a=mul(a,a);k//=2
    return out
def conj(a,b):return mul(mul(a,b),inv(a))
def comm(a,b):return mul(conj(a,b),inv(b))
def eq(a,b):return a[0]==b[0] and np.array_equal(a[1],b[1]) and np.array_equal(a[2],b[2])

# A chord label is an affine permutation z -> e*z+b of F3.
pot_e=eone.copy();pot_b=bzero.copy()
pot_e[v['chords'][0]]=2;pot_e[v['chords'][1]]=2;pot_b[v['chords'][1]]=1
ir=shift[rid]
s=(sid,eone.copy(),bzero.copy())
r=(rid,(pot_e*pot_e[ir])%3,(pot_b-pot_e*pot_e[ir]*pot_b[ir])%3)
assert eq(power(s,2),one) and eq(power(r,3),one)
t=mul(s,r)
def evaluate(word,S=s,R=r):
    out=one;Ri=inv(R)
    for a in word:out=mul(out,S if a==0 else R if a==1 else Ri)
    return out
Nimages=[evaluate(w) for w in d['Nwords']]
assert all(a[0]==eid for a in Nimages)
assert [(int(a[1][eid]),int(a[2][eid])) for a in Nimages[:3]]==[(2,0),(2,1),(1,0)]

class LinearSpace:
    def __init__(self,n):self.n=n;self.rows={}
    def add(self,x):
        x=x.copy()%3
        for p,b in sorted(self.rows.items()):
            if x[p]:x=(x-x[p]*b)%3
        nz=np.flatnonzero(x)
        if not len(nz):return False
        p=int(nz[0]);x=x*int(x[p])%3
        # Keep reduced form, so projection to pivots is the coordinate map.
        for k,b in list(self.rows.items()):
            if b[p]:self.rows[k]=(b-b[p]*x)%3
        self.rows[p]=x;return True
    def matrix(self):return np.stack([self.rows[p] for p in sorted(self.rows)]) if self.rows else np.zeros((0,self.n),dtype=np.int64)
    def contains(self,x):
        x=x.copy()%3
        for p,b in sorted(self.rows.items()):
            if x[p]:x=(x-x[p]*b)%3
        return not np.any(x)
def action(g,x):return g[1]*x[shift[g[0]]]%3
M=LinearSpace(nq)
for i,a in enumerate(Nimages):
    for b in Nimages[i+1:]:
        c=comm(a,b);assert c[0]==eid and np.all(c[1]==1);M.add(c[2])
while True:
    before=len(M.rows)
    for row in M.matrix():M.add(action(s,row));M.add(action(r,row))
    if len(M.rows)==before:break
basis=M.matrix();pivots=sorted(M.rows);dim=len(pivots)
print('Exact kernel dimension over F3:',dim,flush=True)
assert dim>0
def coordinates(x):
    z=x[pivots]%3;assert np.array_equal(z@basis%3,x%3);return z
for a in Nimages:assert eq(power(a,6),one)
def mat(g):return np.stack([coordinates(action(g,row)) for row in basis],axis=1)
ct=power(t,72);assert ct[0]==eid and np.all(ct[1]==1)
cc=coordinates(ct[2]);print('Cusp order:',216 if np.any(cc) else 72,flush=True)
def solve(A,b):
    T=np.column_stack((A%3,b%3));nr,nc=A.shape;row=0;pv=[]
    for j in range(nc):
        nz=np.flatnonzero(T[row:,j])
        if not len(nz):continue
        k=row+int(nz[0]);T[[row,k]]=T[[k,row]];T[row]=T[row]*int(T[row,j])%3
        inds=np.flatnonzero(T[:,j]);inds=inds[inds!=row]
        T[inds]=(T[inds]-T[inds,j,None]*T[row])%3
        pv.append(j);row+=1
        if row==nr:break
    if np.any(T[row:,-1]):return None,None,row
    answer=np.zeros(nc,dtype=np.int64);answer[pv]=T[:row,-1]
    free=[j for j in range(nc) if j not in pv];ker=[]
    for j in free:
        z=np.zeros(nc,dtype=np.int64);z[j]=1;z[pv]=-T[:row,j]%3;ker.append(z)
    return answer,np.stack(ker) if ker else np.zeros((0,nc),dtype=np.int64),row

cert=json.loads((here/'de_source/d_cm_shadow.json').read_text())['pairs']
gauges=json.loads((here/'de_verify_cm.json').read_text())['certificates']
gauged={(v['representative'](a['A']),v['representative'](a['beta'])):a['integral_gauge_k'] for a in gauges}
records=[];counts=[0,0];cusp_counts=[0,0];rng=np.random.default_rng(20261113)
for j,rec in enumerate([a for a in cert if 'mod6_beta_cycles' in a]):
    a,b=v['representative'](rec['A']),v['representative'](rec['beta'])
    wa=[];wb=[]
    for i,w in enumerate(d['Nwords']):
        wa+=w*rec['mod6_A_cycles'].get(str(i),0)
        wb+=w*rec['mod6_beta_cycles'].get(str(i),0)
    wa+=d['Bpaths'][a];wb+=d['Bpaths'][b]
    A,Beta=evaluate(wa),evaluate(wb)
    S,R=conj(Beta,s),conj(A,r)
    error=mul(mul(S,R),inv(t));assert error[0]==eid and np.all(error[1]==1)
    rhs=-coordinates(error[2])%3;Sm,Rm=mat(S),mat(R)
    L=np.column_stack((np.eye(dim,dtype=np.int64)-Sm,Sm@(np.eye(dim,dtype=np.int64)-Rm),-cc))%3
    z,ker,rank=solve(L,rhs);missing=bool(rec['missing_coset']);cusp_counts[int(missing)]+=z is not None
    record={'certificate_index':j,'missing_coset':missing,'cusp_solvable':z is not None,'cusp_rank':rank}
    success=False
    if z is not None:
        for attempt in range(16):
            zz=z if attempt==0 else (z+rng.integers(0,3,size=len(ker))@ker)%3
            cb,ca,h=zz[:dim]@basis%3,zz[dim:2*dim]@basis%3,int(zz[-1])
            BB=mul((eid,eone,cb),Beta);AA=mul((eid,eone,ca),A)
            SS,RR=conj(BB,s),conj(AA,r)
            assert eq(mul(SS,RR),power(t,1+72*h))
            # The image of K6 under the proposed homomorphism is generated
            # by these commutators, closed under its two braid images.
            NN=[evaluate(w,SS,RR) for w in d['Nwords']];image=LinearSpace(dim)
            for ii,a0 in enumerate(NN):
                assert eq(power(a0,6),one)
                for b0 in NN[ii+1:]:image.add(coordinates(comm(a0,b0)[2]))
            AS,AR=mat(SS),mat(RR)
            while True:
                before=len(image.rows)
                for row in image.matrix():image.add(AS@row%3);image.add(AR@row%3)
                if len(image.rows)==before:break
            record['last_generation_rank']=len(image.rows)
            if len(image.rows)==dim:
                success=True
                gauge=gauged[a,b];X=evaluate(d['xword']);Bnew=mul(power(X,gauge),BB)
                ff=mul(mul(mul(s,Bnew),s),inv(Bnew));U=inv(t);V=mul(mul(s,U),s)
                lam=1+72*h;m=36*h
                assert eq(mul(mul(mul(power(U,lam),inv(ff)),power(V,lam)),ff),mul(mul(inv(ff),r),power(X,-m)))
                Y=power(V,2)
                assert eq(mul(mul(mul(inv(ff),power(V,lam)),ff),power(U,lam)),mul(mul(V,U),mul(power(Y,-m),ff)))
                record.update({'attempts':attempt+1,'h':h,'lambda':lam,'m':m,'beta_correction':zz[:dim].tolist(),'A_correction':zz[dim:2*dim].tolist(),'gauge':gauge,'hexagons_verified':True})
                break
    record['generation_certificate_found']=success;counts[int(missing)]+=success;records.append(record)
    print(json.dumps({k:v for k,v in record.items() if not k.endswith('_correction')}),flush=True)
output={'quotient':'B/core_B(ker(N_B -> S3) intersect K6)','N_basis':'fundamental cycles in de_verify_cm.py chord order','first_two_N_words':d['Nwords'][:2],'kernel_dimension_over_F3':dim,'cusp_order':216 if np.any(cc) else 72,'cusp_pass_counts':cusp_counts,'certified_shadow_counts':counts,'records':records,'scope':'Exact fixed finite S3-core refinement; failure to find generation in 16 trials is not a proof of impossibility.'}
(here/'de_s3_core.json').write_text(json.dumps(output,indent=2)+'\n')
print('Completed finite S3-core test:',counts,flush=True)
