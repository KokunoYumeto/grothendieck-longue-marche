#!/usr/bin/env python3
"""Complete compatible finite weight-nine shadow comparison, pure class ten.

Uses the actual split pure braid group PB4/Z = F3 semidirect F2.
The logarithmic derivations of the pure Artin action are computed from
literal free-group words to the two degrees needed for weights 9 and 10.
Thus the degree-ten calculation does not assume a homogeneous associator
identification of logarithms of pure braid generators.
"""
from contextlib import redirect_stdout
from functools import cache
from itertools import product
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):g=runpy.run_path(str(here/'de_gentle_weight9.py'))
d=g['d'];p=101;add,scale=d['add'],d['scale'];X=d['X'];split=d['split'];zeroD=({},{},{})
def mul(a,b,limit=10):
    r={}
    for w,c in a.items():
        for v,e in b.items():
            if len(w)+len(v)>limit:continue
            r[w+v]=(r.get(w+v,0)+c*e)%p
    return {w:c for w,c in r.items() if c}
def br(a,b,limit=10):return add(mul(a,b,limit),mul(b,a,limit),-1)
def deriv(q,D,limit=10):
    out={}
    for w,c in q.items():
        for i,a in enumerate(w):
            for v,b in D[a].items():
                if len(w)-1+len(v)>limit:continue
                t=w[:i]+v+w[i+1:];out[t]=(out.get(t,0)+c*b)%p
    return {w:c for w,c in out.items() if c}
half=pow(2,-1,p)
def logword(w):
    out={():1}
    for letter in w:
        i=abs(letter)-1;sgn=1 if letter>0 else -1
        exp={():1,(i,):sgn%p,(i,i):half,(i,i,i):(sgn*pow(6,-1,p))%p}
        out=mul(out,exp,3)
    out=add(out,{():1},-1)
    return add(add(out,scale(mul(out,out,3),-half)),scale(mul(mul(out,out,3),out,3),pow(3,-1,p)))
# a^-1 X_i a and b^-1 X_i b from the pure Artin action.
artin_inverse=(((1,2,1,-2,-1),(1,2,-1),(3,)),((1,),(2,3,2,-3,-2),(2,3,-2)))
Ds=[]
for words,expected in zip(artin_inverse,(d['Da'],d['Db'])):
    logs=[logword(w) for w in words];u2=[{w:c for w,c in q.items() if len(w)==2} for q in logs]
    u3=[{w:c for w,c in q.items() if len(w)==3} for q in logs];D=[]
    for i in range(3):
        assert {w:c for w,c in logs[i].items() if len(w)==1}==X[i]
        first=scale(u2[i],-1);assert first==expected[i]
        second=add(scale(u3[i],-1),scale(deriv(u2[i],u2,3),half));D.append(add(first,second))
    Ds.append(tuple(D))
Da,Db=Ds;lsum={}
for q in X:lsum=add(lsum,q)
for i in range(3):
    for j in range(i+1,3):lsum=add(lsum,br(X[i],X[j]),half)
assert not deriv(lsum,Da,3) and not deriv(lsum,Db,3)
log23_24=add(X[1],br(X[1],X[2]),half)
log24_34=add(X[1],X[2]);log24_34=add(log24_34,br(X[1],X[2]),half)
@cache
def DL(w):
    if len(w)==1:return (Da,Db)[w[0]]
    k=split(w);a,b=DL(w[:k]),DL(w[k:])
    return tuple(add(deriv(b[i],a),deriv(a[i],b),-1) for i in range(3))
@cache
def evalq(w,mode):
    if len(w)==1:
        args=(({},log23_24),(scale(lsum,-1),X[2]),({},X[2]),(scale(lsum,-1),log24_34))
        return args[mode][w[0]]
    k=split(w);u,v=w[:k],w[k:];a,b=evalq(u,mode),evalq(v,mode)
    if mode==0:du,dv=DL(u),DL(v)
    else:
        D,sgn=(Da,-1) if mode==1 else (Db,1) if mode==2 else (Db,-1)
        du=tuple(scale(e,sgn) for e in D) if u==(0,) else zeroD
        dv=tuple(scale(e,sgn) for e in D) if v==(0,) else zeroD
    return add(add(deriv(b,du),deriv(a,dv),-1),br(a,b))

W9,W10=g['W9'],g['W10'];rows10=list(product(range(3),repeat=10));index10={w:i for i,w in enumerate(rows10)}
P10=np.zeros((len(rows10),155),dtype=np.int16);start=time.time()
for i,w in enumerate(W9+W10):
    q=add(add(add(evalq(w,0),evalq(w,1)),evalq(w,2),-1),evalq(w,3),-1)
    for word,c in q.items():
        if len(word)==10:P10[index10[word],i]=c
    if i%10==9:print('Actual PB4 pentagon columns completed:',i+1,'of 155',flush=True)
K=g['K'];RR,pp=d['rref'](np.column_stack((d['basis'],K[:56])));assert pp[:4]==list(range(4))
coords=RR[:4,4:];assert np.array_equal(d['basis']@coords%p,K[:56])
P9K=d['P']@coords%p;K9=d['null'](P9K);T=K@K9%p;assert T.shape==(155,34)
P10T=P10.astype(np.int64)@T%p;K10=d['null'](P10T);full=T@K10%p
leading=full[:56];rank9=len(d['rref'](leading)[1]);metarank=len(d['rref'](d['M']@leading%p)[1])
assert rank9==1 and metarank==1
assert not np.any(g['A']@full%p) and not np.any(P10.astype(np.int64)@full%p)
image=d['M']@leading%p;gamma=np.array([d['comb'](9,i+1)%p for i in range(8)])
assert len(d['rref'](np.column_stack((image,gamma)))[1])==1
np.savez_compressed(here/'de_pentagon10_finite_certificate.npz',pentagon_degree10=P10,after_degree9_pentagon=T,full_shadow_logarithms=full)
out={'prime':101,'pure_class_three_strands':10,'pure_class_four_strands':10,'minimum_f_weight':9,
     'complete_gentle_stratum_dimension':37,'gentle_weight9_dimension':4,'gentle_weight9_metabelian_dimension':2,
     'after_degree9_pentagon_dimension':34,'complete_pentagon_stratum_dimension':full.shape[1],
     'pentagon_weight9_dimension':rank9,'pentagon_weight9_metabelian_dimension':metarank,
     'pentagon_metabelian_image_is_gamma_line':True,'all_hexagon_and_pentagon_coefficients_verified':True,
     'literal_Artin_inverse_words':artin_inverse,
     'full_shadow_logarithms':[{'degree9':{''.join('xy'[a] for a in w):int(full[i,j]) for i,w in enumerate(W9) if full[i,j]},
                               'degree10':{''.join('xy'[a] for a in w):int(full[56+i,j]) for i,w in enumerate(W10) if full[56+i,j]}}
                              for j in range(full.shape[1])],
     'elapsed_seconds':round(time.time()-start,3),
     'scope':'Complete lambda-one finite GT-shadow stratum f in gamma9 at compatible pure class10 exponent101 quotients on three and four strands; exact full pentagon there, with generation supplied by the Frattini argument.'}
(here/'de_pentagon10_finite.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='full_shadow_logarithms'},indent=2),flush=True)
