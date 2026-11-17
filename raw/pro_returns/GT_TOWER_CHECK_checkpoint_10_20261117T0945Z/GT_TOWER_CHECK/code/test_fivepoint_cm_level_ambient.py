#!/usr/bin/env python3
"""Exhaust all framed multiplier-one shadows on an actual abelian cover.

Target: Gamma_0,5 / (N' N^6), N=ker(Gamma_0,5 -> SL2(Z/12)).
Source: F2/(J' J^6), where J is the kernel of the joint eight
pentagon/gentle insertion maps to that order-192 quotient.
The source has order 288*6^289. We enumerate its base residues and
solve all remaining equations over F2 and F3, including the finite
pure torsion-conjugator constraints which determine the CM bits.
No claim of a lift from a surviving residue to a profinite element
is made.
"""
import build_fivepoint_cm_level as C
from pathlib import Path
from collections import deque,Counter
import numpy as np
import json

def inverse(w):return tuple(-j for j in w[::-1])
def subst(w,gs):
    return tuple(z for j in w for z in (gs[j-1] if j>0 else inverse(gs[-j-1])))
I=C.I;mul=C.mul;inv=C.inv;Q=C.Q;idx=C.idx;table=C.table
assert C.complete and len(C.joint)==288
JQ=C.joint;ji=C.seen;JG=(C.X,C.Y);one=(0,)*8
def jmul(a,b):return tuple(int(table[x,y]) for x,y in zip(a,b))
def jinv(a):return tuple(C.inverses[x] for x in a)
jtable=np.array([[ji[jmul(a,b)] for b in JQ] for a in JQ],dtype=np.int16)
jinverse=[ji[jinv(a)] for a in JQ]
jgens=[ji[g] for g in JG]

# The actual derived image, rather than all 288 base residues.
comm=jmul(jmul(jmul(JG[0],JG[1]),jinv(JG[0])),jinv(JG[1]))
normal_generators=set()
for g in JQ:normal_generators.add(ji[jmul(jmul(g,comm),jinv(g))])
derived={0};todo=[0]
for q in todo:
    for g in normal_generators:
        v=int(jtable[q,g])
        if v not in derived:derived.add(v);todo.append(v)
print("Joint derived image:",len(derived),flush=True)

# Schreier free basis of J, of rank 289.
jparent={0:None};jpaths={0:()};jorder=[0];jtree=set()
for q in jorder:
    for k,g in enumerate(jgens):
        v=int(jtable[q,g])
        if v not in jparent:
            jparent[v]=(q,k);jpaths[v]=jpaths[q]+(k+1,)
            jorder.append(v);jtree.add((q,k))
jchords=[(q,k) for q in range(288) for k in range(2) if (q,k) not in jtree]
jloops=[jpaths[q]+(k+1,)+inverse(jpaths[int(jtable[q,jgens[k]])])
        for q,k in jchords]
assert len(jloops)==289
nv=len(jloops)

# Explicit Gamma_0,5 words for all insertion maps.
a,b,x,y,z=(1,),(2,),(3,),(4,),(5,)
x12=(-5,-4,-3,-2,-1);z0=inverse(x12+b)
pairwords=[(x12,b+y),(a+b,z),(b,z),(x12+a,y+z),(x12,b),
           (b,x12),(z0,x12),(b,z0)]
for w,(mx,my) in zip(pairwords,C.pairs):
    assert C.word_eval(w[0],C.gens)==mx
    assert C.word_eval(w[1],C.gens)==my
mappedloops=[[subst(w,pair) for w in jloops] for pair in pairwords]

def chain(start,w):
    row=np.zeros(len(C.chords),dtype=np.int16);q=start
    for j in w:
        if j>0:
            e=(q,j-1);q=int(table[q,C.ig[j-1]]);sgn=1
        else:
            q=int(table[q,C.inverses[C.ig[-j-1]]]);e=(q,-j-1);sgn=-1
        if e in C.chordidx:row[C.chordidx[e]]+=sgn
    return q,row
def quotient_projection(p):
    A=(C.matrix%p).copy();r=0;pivots=[]
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[r:,col])
        if not len(nz):continue
        q=r+int(nz[0]);A[[r,q]]=A[[q,r]]
        A[r]=(A[r]*pow(int(A[r,col]),-1,p))%p
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=r]
        A[nz]=(A[nz]-A[nz,col,None]*A[r])%p
        pivots.append(col);r+=1
    free=[j for j in range(A.shape[1]) if j not in pivots]
    P=np.zeros((A.shape[1],len(free)),dtype=np.int16)
    P[free]=np.eye(len(free),dtype=np.int16)
    P[pivots]=-A[:r,free]
    P%=p
    assert np.all((C.matrix@P)%p==0)
    assert len(free)==102
    return P
projections={p:quotient_projection(p) for p in (2,3)}
raw_loop_cache={}
def loops_at(i,q):
    key=(i,q)
    if key not in raw_loop_cache:
        rows=[]
        for w in mappedloops[i]:
            end,row=chain(q,w);assert end==q;rows.append(row)
        raw_loop_cache[key]=np.array(rows,dtype=np.int16)
    return raw_loop_cache[key]

# A mixed expression consists of indices +/-1,...,+/-8 for f-values
# and tuples of signed Gamma_0,5 generators for fixed factors.
expressions={
 "pentagon":(1,2,-5,-4,-3),
 "two_cycle":(5,6),
 "three_cycle_plus":(7,8,5),
 "three_cycle_minus":(7,inverse(z0),8,inverse(b),5,inverse(x12))}
def expression_matrix(base,tokens,p):
    current=0;linear=np.zeros((nv,len(C.chords)),dtype=np.int32)
    constant=np.zeros(len(C.chords),dtype=np.int32)
    for token in tokens:
        if isinstance(token,tuple):
            current,row=chain(current,token);constant+=row;continue
        i=abs(token)-1
        w=subst(jpaths[base],pairwords[i])
        if token>0:
            linear+=loops_at(i,current)
            current,row=chain(current,w);constant+=row
        else:
            current,row=chain(current,inverse(w));constant+=row
            linear-=loops_at(i,current)
    if current!=0:return None
    P=projections[p]
    return ((linear@P).T%p,(-constant@P)%p)

# The finite modular source E0=(F2[Q/H2] + F3[Q/H3]) semidirect Q,
# Q=SL2(Z/12)/{+/-I}. It distinguishes the pure frame projections.
def canon(q):return min(q,tuple(-v%12 for v in q))
def bmul(a,b):return canon(mul(a,b))
def binv(a):return canon(inv(a))
S=canon((0,1,11,0));R=canon((0,11,1,11));BI=canon(I)
BQ=[BI];bi={BI:0}
for q in BQ:
    for g in (S,R):
        v=bmul(q,g)
        if v not in bi:bi[v]=len(BQ);BQ.append(v)
assert len(BQ)==576
btable=np.array([[bi[bmul(a,b)] for b in BQ] for a in BQ],dtype=np.int16)
binverses=[bi[binv(q)] for q in BQ]
bs,br=bi[S],bi[R]
bgs=(bs,br)
bcases={}
for p,h in ((2,S),(3,R)):
    subgroup=[BI];v=h
    while v!=BI:subgroup.append(v);v=bmul(v,h)
    which={};reps=[]
    for q in BQ:
        if q in which:continue
        k=len(reps);reps.append(q)
        for h0 in subgroup:which[bmul(q,h0)]=k
    permutations=np.array([[which[bmul(q,t)] for t in reps] for q in BQ],dtype=np.int16)
    bcases[p]=(which,reps,permutations)

# x=(sr)^-2 and y=s*x*s, with s^2=r^3=1.
bx=(-2,1,-2,1);by=(1,)+bx+(1,)
def b_eval(w,p):
    which,reps,perms=bcases[p]
    v=np.zeros(len(reps),dtype=np.int16);q=0
    for j in w:
        typ=abs(j)-1;g=bgs[typ]
        active=(p==2 and typ==0) or (p==3 and typ==1)
        if j>0:
            if active:v[perms[q,0]]+=1
            q=int(btable[q,g])
        else:
            q=int(btable[q,binverses[g]])
            if active:v[perms[q,0]]-=1
    return q,v%p
bloopimages={}
for p in (2,3):
    rows=[]
    for w in jloops:
        q,v=b_eval(subst(w,(bx,by)),p);assert q==0;rows.append(v)
    bloopimages[p]=np.array(rows,dtype=np.int16)

def push(v,q,p):
    perm=bcases[p][2][q]
    ans=np.empty_like(v);ans[...,perm]=v
    return ans
def cycle_sums(q,p,v):
    perm=bcases[p][2][q];seen=set();sums=[]
    for k in range(len(perm)):
        if k in seen:continue
        cyc=[];j=k
        while j not in seen:seen.add(j);cyc.append(j);j=int(perm[j])
        sums.append(v[...,cyc].sum(axis=-1)%p)
    return np.stack(sums,axis=-1)

def crt_signed(q3):
    return tuple(next(v for v in range(12) if v%4==I[j]%4 and v%3==q3[j]%3)
                 for j in range(4))
def matpow(g,n):
    out=I
    for _ in range(n):out=mul(out,g)
    return out
def neg(q):return tuple(-v%12 for v in q)
T3=[(sgn,k,tuple(sgn*v%3 for v in matpow((0,11,1,11),k)))
    for sgn in (1,-1) for k in range(3)]
W3=[(j,tuple(v%3 for v in matpow((0,1,11,0),j))) for j in range(4)]
frames=[]
for rho in range(3):
    V=matpow(C.U,8*rho)
    qf=(1,-8*rho%12,-8*rho%12,(1+64*rho*rho)%12)
    for sg,k,t in T3:
        T=crt_signed(t)
        for j,w in W3:
            W=crt_signed(w)
            qb=bi[canon(mul(V,inv(W)))]
            qa=bi[canon(mul(V,inv(T)))]
            frames.append({"rho":rho,"T_sign":sg,"T_R_power":k,"W_power":j,
                           "parity":int(sg==-1)^(j%2),
                           "qf":qf,"qb":qb,"qa":qa})
assert len(frames)==72

def frame_equations(base,frame,p):
    qf,vf=b_eval(subst(jpaths[base],(bx,by)),p)
    assert BQ[qf]==canon(frame["qf"])
    h2=int(btable[bs,qf]);h3=int(btable[binverses[qf],br])
    qb,qa=frame["qb"],frame["qa"]
    assert int(btable[btable[qb,bs],binverses[qb]])==h2
    assert int(btable[btable[qa,br],binverses[qa]])==h3
    dim=len(bcases[p][1]);es=np.zeros(dim,dtype=np.int16);er=es.copy()
    if p==2:es[0]=1
    else:er[0]=1
    L=bloopimages[p]
    # (1-h2)b = es+s*vf-qb*es
    # (1-h3)a = -qf^-1*vf+qf^-1*er-qa*er
    As=cycle_sums(h2,p,push(L,bs,p)).T
    cs=cycle_sums(h2,p,es+push(vf,bs,p)-push(es,qb,p))
    Ar=cycle_sums(h3,p,-push(L,binverses[qf],p)).T
    cr=cycle_sums(h3,p,-push(vf,binverses[qf],p)
                  +push(er,binverses[qf],p)-push(er,qa,p))
    return np.vstack((As,Ar))%p,np.concatenate((-cs,-cr))%p

abloops=np.array([[sum(1 if j==k else -1 if j==-k else 0 for j in w)
                   for k in (1,2)] for w in jloops],dtype=np.int16).T
def solve_many(A,B,p):
    A=(A%p).copy();B=(B%p).copy();rank=0
    for col in range(A.shape[1]):
        nz=np.flatnonzero(A[rank:,col])
        if len(nz)==0:continue
        q=rank+int(nz[0])
        A[[rank,q]]=A[[q,rank]];B[[rank,q]]=B[[q,rank]]
        scale=pow(int(A[rank,col]),-1,p)
        A[rank]=(A[rank]*scale)%p;B[rank]=(B[rank]*scale)%p
        nz=np.flatnonzero(A[rank+1:,col])+rank+1
        fac=A[nz,col,None].copy()
        A[nz]=(A[nz]-fac*A[rank])%p
        B[nz]=(B[nz]-fac*B[rank])%p
        rank+=1
        if rank==A.shape[0]:break
    assert not np.any(A[rank:])
    good=~np.any(B[rank:],axis=0)
    return rank,good

records=[];base_records=[]
for base in sorted(derived):
    qf=Q[JQ[base][4]]
    fs=[fr for fr in frames if fr["qf"]==qf]
    if not fs:continue
    results={}
    valid=True
    for p in (2,3):
        As=[];bs0=[]
        for name,tokens in expressions.items():
            result=expression_matrix(base,tokens,p)
            if result is None:valid=False;break
            A0,b0=result;As.append(A0);bs0.append(b0)
        if not valid:break
        abbase=np.array([sum(1 if j==k else -1 if j==-k else 0 for j in jpaths[base])
                         for k in (1,2)],dtype=np.int16)
        As.append(abloops%p);bs0.append(-abbase%p)
        firstA,firstb=frame_equations(base,fs[0],p)
        As.append(firstA)
        A=np.vstack(As)
        fixed_rhs=np.concatenate(bs0)
        Bs=[]
        for fr in fs:
            Af,bf=frame_equations(base,fr,p);assert np.array_equal(Af,firstA)
            Bs.append(np.concatenate((fixed_rhs,bf)))
        rank,good=solve_many(A,np.stack(Bs,axis=1),p)
        results[p]={"rank":rank,"good":good.tolist(),"rows":len(A)}
    if not valid:continue
    base_records.append({"base":base,"base_word":jpaths[base],
                         "qf":qf,"ranks":{str(p):results[p]["rank"] for p in (2,3)},
                         "rows":{str(p):results[p]["rows"] for p in (2,3)}})
    for j,fr in enumerate(fs):
        good=all(results[p]["good"][j] for p in (2,3))
        if good:
            rec=dict(fr);rec["base"]=base
            rec["free_dimensions"]={str(p):nv-results[p]["rank"] for p in (2,3)}
            records.append(rec)
    print("base",base,"word",jpaths[base],"ranks",
          [results[p]["rank"] for p in (2,3)],
          "surviving frame residues",sum(all(results[p]["good"][j] for p in (2,3))
                                        for j in range(len(fs))),flush=True)

hist=Counter(r["parity"] for r in records)
print("Complete framed finite residue enumeration:",dict(hist),flush=True)
print("Actual target order = 192 * 6^102",flush=True)
print("Actual finite source word quotient order = 288 * 6^289",flush=True)
print("Every source fiber is counted by its explicit affine F2 and F3 solution spaces.",flush=True)
out={"scope":"Complete necessary framed multiplier-one finite-shadow enumeration; surviving shadows are not asserted to lift.",
     "target_quotient":"Gamma_0,5/(N' N^6), N=ker(signed SL2(Z/12) representation)",
     "target_order":"192*6^102","source_quotient":"F2/(J' J^6)",
     "source_order":"288*6^289","source_derived_image_order":len(derived),
     "base_records":base_records,"surviving_residues":records,
     "frame_residue_parity_counts":dict(hist)}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
