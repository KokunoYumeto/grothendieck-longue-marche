#!/usr/bin/env python3
"""Actual integral Hall group jets for the exceptional-prime q7 problem.

This uses the Magnus embedding x=1+X, y=1+Y, z=(xy)^(-1),
not BCH coordinates.  For truncation N<14, a product of Hall group
commutators of weights >=7 has expansion 1+sum a_w(C_w-1).
Both cycle equations are therefore exact linear equations in the
integral Hall exponents, including every exponent of weights 8..N.

Outputs exact rational p-integral group jets or local divisibility
certificates, always checking the full associative-word equations.
"""
from pathlib import Path
from functools import cache
from itertools import product
from fractions import Fraction as F
from math import gcd, lcm
import json, time, sys
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix

OUT=Path(__file__).resolve().parent
N=int(sys.argv[1]) if len(sys.argv)>1 else 10
assert 7<N<14
START=time.time()

def plus(a,b,k=1):
    c=dict(a)
    for w,v in b.items():
        c[w]=c.get(w,0)+k*v
        if not c[w]: del c[w]
    return c

def mul(a,b,n):
    c={}
    for u,x in a.items():
        for v,y in b.items():
            if len(u)+len(v)<=n:
                w=u+v;c[w]=c.get(w,0)+x*y
    return {w:x for w,x in c.items() if x}

def invdev(a,n):
    """Full inverse of 1+a, including its constant coefficient."""
    ans={():1}; t={():1}
    for _ in range(n+1):
        t=mul(t,a,n)
        if not t:break
        t={w:-v for w,v in t.items()}
        ans=plus(ans,t)
    return ans

@cache
def islyndon(w):
    return all(w<w[j:] for j in range(1,len(w)))

@cache
def lyndon(n):
    return tuple(w for w in product((0,1),repeat=n) if islyndon(w))

@cache
def ev(w,mode,n):
    """C_w(g,h)-1 through degree n, for the four cycle substitutions."""
    if len(w)>n:return {}
    if len(w)==1:
        letter=((0,1),(1,0),(2,0),(1,2))[mode][w[0]]
        if letter<2:return {(letter,):1}
        # (xy)^-1 = (1+Y)^-1(1+X)^-1, without constant term.
        return {(1,)*i+(0,)*j:(-1)**(i+j)
                for i in range(n+1) for j in range(n+1-i) if i+j}
    k=next(k for k in range(1,len(w)) if islyndon(w[k:]))
    u,v=w[:k],w[k:]
    a=ev(u,mode,n-len(v));b=ev(v,mode,n-len(u))
    d=plus(mul(a,b,n),mul(b,a,n),-1)
    # [1+a,1+b]-1=(ab-ba)(1+a)^-1(1+b)^-1.
    q=n-len(w)
    return mul(mul(d,invdev(a,q),n),invdev(b,q),n)

def label(w):return ''.join('x' if i==0 else 'y' for i in w)
def word(s):return tuple(0 if i=='x' else 1 for i in s)

Q={word(w):v for w,v in {
    'xxxyxyy':3,'xxxyyxy':3,'xxyxyxy':1,
    'xxyxyyy':-3,'xxyyxyy':-3,'xxyyyxy':-3,'xyxyxyy':-1}.items()}

def defects(w):
    v=ev(w,0,N)
    return plus(v,ev(w,1,N)),plus(plus(v,ev(w,2,N)),ev(w,3,N))

unknowns=[w for n in range(8,N+1) for w in lyndon(n)]
rowkeys=[(kind,w) for n in range(7,N+1) for kind in (0,1)
         for w in product((0,1),repeat=n)]
ri={key:i for i,key in enumerate(rowkeys)}
entries={};rhs={}
for w,c in Q.items():
    for kind,d in enumerate(defects(w)):
        for v,a in d.items():
            key=ri[kind,v];rhs[key]=rhs.get(key,0)-c*a
for j,w in enumerate(unknowns):
    for kind,d in enumerate(defects(w)):
        for v,a in d.items():entries[ri[kind,v],j]=a
    if j%50==0: print('Hall column',j,'/',len(unknowns),'elapsed',round(time.time()-START,2),flush=True)
rhs={i:v for i,v in rhs.items() if v}
assert all(len(rowkeys[i][1])>=8 for i in rhs)
A=sp.SparseMatrix(len(rowkeys),len(unknowns),entries)
b=sp.Matrix([rhs.get(i,0) for i in range(len(rowkeys))])
print('full matrix',A.shape,'nonzeros',len(entries),flush=True)

def independent_rows(M):
    """A modular rank lower bound; exact completeness is checked separately."""
    p=1000003
    t=np.array(M.T.tolist(),dtype=np.int64)%p
    pos=0;ids=[]
    for col in range(t.shape[1]):
        nz=np.flatnonzero(t[pos:,col])
        if not len(nz):continue
        k=pos+int(nz[0]);t[[pos,k]]=t[[k,pos]]
        t[pos]=(t[pos]*pow(int(t[pos,col]),-1,p))%p
        for j in range(pos+1,t.shape[0]):
            if t[j,col]:t[j]=(t[j]-int(t[j,col])*t[pos])%p
        ids.append(col);pos+=1
        if pos==t.shape[0]:break
    return ids

def vp(a,p):
    a=F(a)
    if not a:return 10**9
    n,d=abs(a.numerator),a.denominator;k=0
    while n%p==0:n//=p;k+=1
    while d%p==0:d//=p;k-=1
    return k

def local_solve(M,y,p):
    """Exact DVR Gaussian elimination, retaining all free variables.

    A pivot of minimum p-valuation makes every row operation integral
    over Z_(p).  At each stage the pivot divides its whole trailing row.
    Thus the largest negative valuation in b_i/pivot_i is precisely the
    minimum power of p by which the fixed leading term must be scaled.
    """
    a=[[F(v) for v in row] for row in M.tolist()]
    b=[F(v) for v in y]
    nr,nc=M.shape;perm=list(range(nc))
    trans=[[F(int(i==j)) for j in range(nr)] for i in range(nr)]
    piv=[];rank=0
    for k in range(min(nr,nc)):
        best=None
        for i in range(k,nr):
            for j in range(k,nc):
                v=a[i][j]
                if not v:continue
                score=(vp(v,p),abs(v.numerator)+v.denominator)
                if best is None or score<best[0]:best=(score,i,j)
                if score==(0,2):break
            if best is not None and best[0]==(0,2):break
        if best is None:break
        _,i,j=best
        if i!=k:
            a[k],a[i]=a[i],a[k];b[k],b[i]=b[i],b[k];trans[k],trans[i]=trans[i],trans[k]
        if j!=k:
            perm[k],perm[j]=perm[j],perm[k]
            for row in a:row[k],row[j]=row[j],row[k]
        d=a[k][k]
        piv.append({'index':k,'pivot':str(d),'pivot_valuation':vp(d,p),
                    'rhs':str(b[k]),'rhs_valuation':None if not b[k] else vp(b[k],p)})
        for i in range(k+1,nr):
            if not a[i][k]:continue
            t=a[i][k]/d
            assert vp(t,p)>=0
            a[i][k]=F(0)
            for j in range(k+1,nc):
                if a[k][j]:a[i][j]-=t*a[k][j]
            b[i]-=t*b[k]
            for j in range(nr):
                if trans[k][j]:trans[i][j]-=t*trans[k][j]
        rank=k+1
        if k%40==0:print('p',p,'pivot',k,'/',min(nr,nc),'valuation',vp(d,p),'elapsed',round(time.time()-START,2),flush=True)
    assert all(not b[i] for i in range(rank,nr)), 'No rational solution'
    deficit=max([0]+[vp(a[i][i],p)-vp(b[i],p) for i in range(rank) if b[i]])
    scale=p**deficit
    x=[F(0)]*nc
    for i in range(rank-1,-1,-1):
        x[i]=(scale*b[i]-sum(a[i][j]*x[j] for j in range(i+1,nc)))/a[i][i]
        assert vp(x[i],p)>=0
    original=[F(0)]*nc
    for i,j in enumerate(perm):original[j]=x[i]
    xx=sp.Matrix([sp.Rational(v.numerator,v.denominator) for v in original])
    assert M*xx==scale*y
    witnesses=[]
    if deficit:
        for i in range(rank):
            if not b[i] or vp(a[i][i],p)-vp(b[i],p)!=deficit:continue
            # This linear combination of original equations has all left
            # coefficients divisible by p^k, but its right side is not.
            t=sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in trans[i]]])
            lhs=t*M;rr=(t*y)[0]
            assert rr==b[i]
            assert min([vp(v,p) for v in lhs if v])==vp(a[i][i],p)
            witnesses.append({'row_combination':{str(j):str(v) for j,v in enumerate(trans[i]) if v},
                              'lhs_min_valuation':vp(a[i][i],p),'rhs':str(rr),
                              'rhs_valuation':vp(rr,p)})
            break
    return original,{'prime':p,'rank':rank,'free_parameters':nc-rank,
                     'minimum_leading_scale_valuation':deficit,'leading_scale':scale,
                     'pivots':piv,'obstruction_certificates':witnesses}

def bezout(a,b):
    r0,r1,s0,s1,t0,t1=a,b,1,0,0,1
    while r1:
        q=r0//r1
        r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
    return r0,s0,t0

results=[]
for n in range(8,N+1):
    rows=[i for i,(kind,w) in enumerate(rowkeys) if len(w)<=n]
    cols=[j for j,w in enumerate(unknowns) if len(w)<=n]
    full=A[rows,cols];bb=b[rows,:]
    # Below degree 14, every cycle defect is primitive in the Magnus
    # Hopf algebra (Delta X=X tensor 1+1 tensor X+X tensor X).
    # Its first nonzero homogeneous term is therefore an ordinary free
    # Lie element.  Its Lyndon-word coefficients detect that term.
    # Induction on degree shows these rows already detect the full defect.
    lrows=[i for i,j in enumerate(rows) if islyndon(rowkeys[j][1])]
    lmat=full[lrows,:];lb=bb[lrows,:]
    selected0=independent_rows(lmat.row_join(lb))
    selected=[lrows[i] for i in selected0]
    M=full[selected,:];y=bb[selected,:]
    # Rational completeness check: the chosen row subsystem gives the
    # entire affine solution set, not merely congruence-consistent rows.
    rr,piv=DomainMatrix.from_Matrix(M.row_join(y)).convert_to(sp.QQ).rref()
    rr=rr.to_Matrix();assert full.cols not in piv
    free=[j for j in range(full.cols) if j not in piv]
    particular=sp.zeros(full.cols,1);K=sp.zeros(full.cols,len(free))
    for j,f in enumerate(free):K[f,j]=1
    for i,pivot in enumerate(piv):
        particular[pivot]=rr[i,full.cols]
        for j,f in enumerate(free):K[pivot,j]=-rr[i,f]
    assert full*particular==bb
    assert lmat*K==sp.zeros(lmat.rows,len(free))
    if n<=10: assert full*K==sp.zeros(full.rows,len(free))
    print('class',n,'variables',full.cols,'exact rank',len(piv),'free',len(free),flush=True)
    stage={'class':n,'variables':full.cols,'equations':full.rows,
           'rank':len(piv),'free_parameters':len(free),
           'selected_equations':[{'cycle':rowkeys[rows[i]][0]+1,'word':label(rowkeys[rows[i]][1])} for i in selected],
           'local_results':[]}
    integer_vectors=[]
    for p in (2,3,7):
        sol,answer=local_solve(M,y,p)
        v=sp.Matrix([sp.Rational(c.numerator,c.denominator) for c in sol])
        assert full*v==answer['leading_scale']*bb
        answer['hall_coordinates']={label(unknowns[cols[j]]):str(c) for j,c in enumerate(sol) if c}
        answer['coefficient_denominator_lcm']=lcm(*[c.denominator for c in sol])
        answer['full_associative_word_verification']=True
        stage['local_results'].append(answer)
        if answer['leading_scale']==1:
            den=answer['coefficient_denominator_lcm']
            integer_vectors.append((den,[int(den*c) for c in sol]))
        print('class',n,'p',p,'minimum leading scale',answer['leading_scale'],
              'denominator',answer['coefficient_denominator_lcm'],flush=True)
    if integer_vectors:
        common,ivec=integer_vectors[0]
        for den,vec in integer_vectors[1:]:
            gg,aa,bbz=bezout(common,den)
            ivec=[aa*u+bbz*v for u,v in zip(ivec,vec)];common=gg
        if common==1 and n<=10:
            # Shorten the certificate by subtracting an integer kernel
            # vector.  This changes neither leading term nor equations.
            ib=[]
            for j in range(K.cols):
                den=lcm(*[int(v.q) for v in K[:,j]])
                ib.append([int(den*v) for v in K[:,j]])
            basis=sp.Matrix(ib).lll().tolist()
            orth=[]
            for row in basis:
                v=list(map(F,row))
                for u in orth:
                    c=sum(a*b for a,b in zip(v,u))/sum(a*a for a in u)
                    v=[a-c*b for a,b in zip(v,u)]
                orth.append(v)
            for row,u in reversed(list(zip(basis,orth))):
                c=round(sum(F(a)*b for a,b in zip(ivec,u))/sum(a*a for a in u))
                ivec=[a-c*int(b) for a,b in zip(ivec,row)]
        assert full*sp.Matrix(ivec)==common*bb
        stage['combined_jet']={'denominator':common,
            'hall_coordinates':{label(unknowns[cols[j]]):str(F(c,common)) for j,c in enumerate(ivec) if c},
            'integral_over_Z':common==1,'full_associative_word_verification':True}
        print('class',n,'combined exact jet denominator',common,flush=True)
    results.append(stage)
    (OUT/f'e_exceptional_jets_{N}.json').write_text(json.dumps({
        'method':'Exact integral Hall group commutators in Magnus coordinates; all group equations through the specified class',
        'q7':{label(w):v for w,v in Q.items()},'maximum_class':N,
        'group_commutator':'g h g^-1 h^-1','z':'(xy)^-1',
        'equations':['f(y,x)f(x,y)=1','f(z,x)f(y,z)f(x,y)=1'],
        'stages':results,'infinite_lift_claimed':False},indent=2))
print('FINISHED',round(time.time()-START,3),'seconds',flush=True)
