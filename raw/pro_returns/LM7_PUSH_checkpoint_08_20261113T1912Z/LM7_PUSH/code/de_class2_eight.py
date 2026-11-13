#!/usr/bin/env python3
"""Complete gentle fibres above the 24 new witnesses at exponent eight.

The kernel above exponent four is the same 4753-dimensional quadratic
module. Literal old witnesses are evaluated with integral Hall collection
modulo (8,4), including their recorded commutator adjustment. Every
retained solution is then substituted in both torsion/order equations,
which are equivalent to the complete hexagons in this normalization.
"""
from contextlib import redirect_stdout
from functools import cache
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np
import sympy as sp

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):g=runpy.run_path(str(here/'de_class2_two_gentle.py'))
d=g['d'];base=d['d'];v=d['v'];n=97;up=d['upper'];m=4753
records=json.loads((here/'de_fibre_crt_verify.json').read_text())['records']
ci={v['Q'][e]:j for j,e in enumerate(v['chords'])};one=v['unit']
ss,rr=v['ss'],v['rr'];rri=v['inverse'](rr)
offset=[i*(2*n-i-1)//2 for i in range(n)]
def zero():return np.zeros(n,dtype=np.int64),np.zeros(len(up[0]),dtype=np.int64)
def ncollect(w):
    a,z=zero()
    for letter in d['nword'](w):
        i=abs(letter)-1;s=1 if letter>0 else -1
        block=slice(offset[i],offset[i]+n-i-1)
        z[block]=(z[block]-s*a[i+1:])%4;a[i]=(a[i]+s)%8
    return a,z
@cache
def action(q):
    A=v['act'](q,v['C'])[v['chords']].astype(np.int64)
    w=base['Bpaths'][q];wi=base['binv'](w);tau=[]
    for i,t in enumerate(base['Nwords']):
        a,z=ncollect(w+t+wi);assert np.array_equal(a,A[:,i]%8);tau.append(z)
    tau=np.stack(tau,axis=1)
    # The streaming Schreier collector uses the spanning-tree section,
    # whereas Bpaths is the short-word section.  If Bpaths(q)=n(c)*s(q),
    # conjugation by s(q) is conjugation by Bpaths(q), followed by
    # conjugation by n(c)^{-1}.  This central correction is essential
    # at exponent eight; it vanished in the earlier central kernels.
    c=v['P'][q][v['chords']]
    tau=(tau-c[up[0],None]*A[up[1]]+c[up[1],None]*A[up[0]])%4
    return A,tau
def acted(q,a,z):
    A,tau=action(q);Z=np.zeros((n,n),dtype=np.int64);Z[up]=z;Z=Z-Z.T
    Z-=np.diag(a*(a-1)//2)+np.tril(np.outer(a,a),-1)
    return A@a%8,(tau@a+(A@Z@A.T)[up])%4
def collect(w):
    q=one;a,z=zero()
    for token in w:
        if isinstance(token,tuple):
            b,c=acted(q,*token);z=(z+c-np.outer(b,a)[up])%4;a=(a+b)%8
            continue
        qn=v['times'](q,ss if token==0 else rr if token==1 else rri)
        gen=[]
        if token:
            if q in ci:gen.append(ci[q]+1)
            if qn in ci:gen.append(-ci[qn]-1)
        for letter in gen:
            i=abs(letter)-1;s=1 if letter>0 else -1
            block=slice(offset[i],offset[i]+n-i-1)
            z[block]=(z[block]-s*a[i+1:])%4;a[i]=(a[i]+s)%8
        q=qn
    assert q==one
    return a,z
def kernel(w):
    a,z=collect(w);assert not np.any(a%4) and not np.any(z%2)
    return np.concatenate((a//4,z//2))%2
def bpower(w,e):return w*e if e>=0 else base['binv'](w)*(-e)
u=[-1,0];x=u*2;t=[0,1];prepared=[]
literal_checks=0
rng=np.random.default_rng(182026)
non_tree=max(v['Q'],key=lambda q:int(np.abs(v['P'][q][v['chords']]).sum()))
assert np.any(v['P'][non_tree][v['chords']])
for q in (ss,rr,non_tree,v['representative'](records[17]['beta'])):
    for trial in range(4):
        a,z=zero();w=[]
        active=sorted(rng.choice(n,size=3,replace=False).tolist())
        for i in active:
            a[i]=int(rng.choice((-2,-1,1,2)))
            w+=bpower(base['Nwords'][i],int(a[i]))
        i,j=active[:2];k=np.flatnonzero((up[0]==i)&(up[1]==j))[0]
        z[k]=int(rng.choice((-2,-1,1,2)))
        comm=base['Nwords'][i]+base['Nwords'][j]+base['binv'](base['Nwords'][i])+base['binv'](base['Nwords'][j])
        w+=bpower(comm,int(z[k]));path=base['Bpaths'][q]
        direct=ncollect(path+w+base['binv'](path));formula=collect(path+[(a,z)]+base['binv'](path))
        assert all(np.array_equal(c,d) for c,d in zip(direct,formula));literal_checks+=1
print('Exact normal-form action checked against',literal_checks,'literal conjugated words.',flush=True)
start=time.time()
for rec in records:
    a,z=zero()
    for i,c in rec['central_square_word_factors']:a[i]=c%8
    for i,j,c in rec['central_commutator_word_factors']:
        k=np.flatnonzero((up[0]==i)&(up[1]==j))[0];z[k]=c%4
    ja,jz=zero()
    for i,c in rec['commutator_adjustment_Jstar_word_factors']:ja[i]=c%8
    b=rec['base_beta_word_B'];cg=bpower(x,rec['integral_cusp_gauge'])
    # Undo the recorded cusp gauge before using the common S,R module.
    # Conjugation by x^{-g} fixes t.  The Jstar adjustment is transported
    # by that same inner conjugation; it is not dropped at this finer level.
    s0=b+[0]+base['binv'](b)+[(a,z)]+base['binv'](cg)+[(ja,jz)]+cg
    eS=kernel(s0*2);eR=[kernel((s0+t*(1+144*h))*3) for h in range(2)]
    prepared.append((s0,eS,eR))
    print('Collected exponent-eight errors for certificate',rec['certificate_index'],flush=True)
matrix=np.zeros((2*m+2,m+48),dtype=np.uint8);matrix[:,:m]=g['original']
for j,(s0,eS,eR) in enumerate(prepared):
    for h in range(2):matrix[:m,m+2*j+h]=eS;matrix[m:2*m,m+2*j+h]=eR[h]
piv=np.zeros(min(matrix.shape),dtype=np.int32)
rank=d['gf'](matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,
             piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
pp=piv[:rank].tolist();dom=[i for i in pp if i<m];ra=len(dom);result=[]
for j,(rec,(s0,eS,eR)) in enumerate(zip(records,prepared)):
    choices=[]
    for h in range(2):
        col=m+2*j+h;success=not np.any(matrix[ra:,col]);row={'lambda_mod288':1+144*h,'passes':success}
        if success:
            k=np.zeros(m,dtype=np.int64);k[dom]=matrix[:ra,col]
            rhs=np.concatenate((eS,eR[h],np.zeros(2,dtype=np.int64)))
            assert np.array_equal(g['original'].astype(np.int64)@k%2,rhs)
            K=(4*k[:n],2*k[n:]);S=s0+[K];R=[K]+s0+t*(1+144*h)
            assert all(not np.any(c) for c in collect(S*2))
            assert all(not np.any(c) for c in collect(R*3))
            row.update({'correction_kernel_sparse':{str(i):int(c) for i,c in enumerate(k) if c},
                        'both_complete_order_equations_directly_verified':True})
        choices.append(row)
    row={'certificate_index':j,'missing_coset':rec['missing_coset'],
         'some_lift_exists':any(a['passes'] for a in choices),'multiplier_choices':choices}
    result.append(row);print(json.dumps({k:row[k] for k in ('certificate_index','missing_coset','some_lift_exists')}),flush=True)
out={'refinement':'B/((gamma3(N_B) N_B^8) intersect (N_B-prime N_B^3))',
     'base_witnesses':'de_fibre_crt_verify.json','coefficient_rank':ra,'augmented_rank':rank,
     'pass_counts':[sum(r['some_lift_exists'] and r['missing_coset']==c for r in result) for c in (False,True)],
     'elapsed_seconds':round(time.time()-start,3),'block_actions_checked_against_literal_words':literal_checks,'records':result,
     'scope':'Exact complete finite gentle fibres over the 24 newly constructed exponent-four witnesses, with both multiplier lifts and exact commutator-image rows. These specified base fibres are not asserted exhaustive for each CM matrix pair.'}
(here/'de_class2_eight.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2),flush=True)
