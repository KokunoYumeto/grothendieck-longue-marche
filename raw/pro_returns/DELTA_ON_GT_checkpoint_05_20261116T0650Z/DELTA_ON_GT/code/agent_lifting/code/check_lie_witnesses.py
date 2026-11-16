#!/usr/bin/env python3
"""Exact free-associative certificates for degree 5, 7 and 9 witnesses.

No external packages. All calculations take place over Q in finite homogeneous
components. Standard Lyndon bracketing uses the longest proper Lyndon suffix.
The t_4 derivation action is written explicitly and all braid relations checked.
"""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json

def add(*polys):
    out={}
    for p in polys:
        for w,c in p.items():
            out[w]=out.get(w,0)+c
    return {w:c for w,c in out.items() if c}
def scale(p,c): return {w:c*v for w,v in p.items() if c*v}
def mul(p,q):
    out={}
    for u,a in p.items():
        for v,b in q.items():
            out[u+v]=out.get(u+v,0)+a*b
    return {w:c for w,c in out.items() if c}
def bracket(p,q): return add(mul(p,q),scale(mul(q,p),-1))
def var(x): return {x:1}
def lyndon(w): return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def split(w):
    assert len(w)>1 and lyndon(w),w
    for i in range(1,len(w)):
        if lyndon(w[i:]): return w[:i],w[i:]
@lru_cache(None)
def L(w):
    if len(w)==1: return var(w)
    u,v=split(w)
    return bracket(L(u),L(v))
def substitute(p,images):
    out={}
    for w,c in p.items():
        term={'':c}
        for x in w: term=mul(term,images[x])
        out=add(out,term)
    return out
def poly(coeff): return add(*(scale(L(w),c) for w,c in coeff.items()))
def apply_der(D,p):
    out={}
    for w,c in p.items():
        for i,x in enumerate(w):
            for t,a in D[x].items():
                v=w[:i]+t+w[i+1:]
                out[v]=out.get(v,0)+c*a
    return {w:c for w,c in out.items() if c}
def dadd(*Ds): return {x:add(*(D[x] for D in Ds)) for x in 'abc'}
def dscale(D,c): return {x:scale(D[x],c) for x in 'abc'}
def dbracket(D,E):
    return {x:add(apply_der(D,E[x]),scale(apply_der(E,D[x]),-1)) for x in 'abc'}
def inner(x): return {y:bracket(var(x),var(y)) for y in 'abc'}
def pair(i,j):
    out={x:{} for x in 'abc'}
    out[i]=bracket(var(i),var(j));out[j]=bracket(var(j),var(i))
    return out
def eval_der(coeff,D,E):
    cache={}
    def ev(w):
        if w not in cache:
            if len(w)==1: cache[w]=D if w=='x' else E
            else:
                u,v=split(w);cache[w]=dbracket(ev(u),ev(v))
        return cache[w]
    return dadd(*(dscale(ev(w),c) for w,c in coeff.items()))

q7_coeff={'xxxyxyy':3,'xxxyyxy':3,'xxyxyxy':1,
          'xxyxyyy':-3,'xxyyxyy':-3,'xxyyyxy':-3,'xyxyxyy':-1}
h9_twice={'xxxxxxyyy':2,'xxxxxyxyy':-18,'xxxxxyyxy':-24,
'xxxxxyyyy':-6,'xxxxyxxyy':18,'xxxxyxyxy':-12,
'xxxxyxyyy':19,'xxxxyyxxy':18,'xxxxyyxyy':48,
'xxxxyyyxy':49,'xxxxyyyyy':6,'xxxyxxxyy':-2,
'xxxyxxyxy':32,'xxxyxxyyy':-1,'xxxyxyxxy':20,
'xxxyxyxyy':17,'xxxyxyyxy':11,'xxxyxyyyy':-13,
'xxxyyxxyy':-20,'xxxyyxyxy':-12,'xxxyyxyyy':-43,
'xxxyyyxxy':-20,'xxxyyyxyy':-105,'xxxyyyyxy':-49,
'xxxyyyyyy':-2,'xxyxxyxyy':-41,'xxyxxyyxy':-72,
'xxyxxyyyy':-17,'xxyxyxxyy':59,'xxyxyxyxy':-18,
'xxyxyxyyy':-34,'xxyxyyxyy':-18,'xxyxyyyxy':-68,
'xxyxyyyyy':12,'xxyyxxyyy':-11,'xxyyxyxyy':-51,
'xxyyxyyyy':30,'xxyyyxyxy':-10,'xxyyyxyyy':40,
'xxyyyyxyy':60,'xxyyyyyxy':24,'xyxyxyxyy':6}

def metabelian(p):
    # For a Lie element h in [L,L], right-y Fox extraction has abelianization
    # XY times its coefficient of [x,y]. Count x/y after retaining words
    # ending in y. Remove the factor XY.
    out={}
    for w,c in p.items():
        if w.endswith('y'):
            key=(w.count('x')-1,w.count('y')-1)
            out[key]=out.get(key,0)+c
    return {str(k):str(c) for k,c in out.items() if c}

def check_special(name,coeff):
    h=poly(coeff);x=var('x');y=var('y');z=add(scale(x,-1),scale(y,-1))
    hz_y=substitute(h,{'x':z,'y':y})
    hz_x=substitute(h,{'x':z,'y':x})
    hy_z=substitute(h,{'x':y,'y':z})
    vals={
      'antisymmetry':add(h,substitute(h,{'x':y,'y':x})),
      'cabling':add(bracket(x,h),scale(bracket(add(x,y),hz_y),-1)),
      'special':add(bracket(h,y),bracket(hz_x,add(x,y))),
      'cycle':add(h,hy_z,hz_x)}
    for label,v in vals.items():
        assert not v,(name,label,len(v))
    D={'x':{},'y':bracket(h,y)}
    # The two geometric involutions are self-inverse.  Compare their
    # conjugated derivations with the explicit inner terms.
    inner_checks={}
    for label,images,w in (
        ('swap',{'x':y,'y':x},scale(h,-1)),
        ('cable',{'x':z,'y':y},add(hz_y,scale(h,-1)))):
        for gen in 'xy':
            conjugated=substitute(apply_der(D,images[gen]),images)
            error=add(conjugated,scale(D[gen],-1),
                      scale(bracket(w,var(gen)),-1))
            assert not error,(name,label,gen,error)
            inner_checks[label+'_'+gen]=len(error)
    print(name,'associative support',len(h),'identities', {k:len(v) for k,v in vals.items()})
    print(name,'explicit S3 inner-conjugator checks',inner_checks)
    print(name,'metabelian',metabelian(h))
    return h

def check_braid():
    T={(1,2):pair('a','b'),(1,3):pair('a','c'),(2,3):pair('b','c'),
       (1,4):inner('a'),(2,4):inner('b'),(3,4):inner('c')}
    def t(i,j): return T[tuple(sorted((i,j)))]
    checks=0
    for i,j in combinations(range(1,5),2):
        for k in range(1,5):
            if k in (i,j):continue
            v=dbracket(t(i,j),dadd(t(i,k),t(j,k)))
            assert all(not p for p in v.values());checks+=1
        remaining=[k for k in range(1,5) if k not in (i,j)]
        v=dbracket(t(i,j),t(*remaining))
        assert all(not p for p in v.values());checks+=1
    print('t4 defining relations verified',checks)
    return t

def pentagon(coeff,t):
    terms=[eval_der(coeff,t(1,2),dadd(t(2,3),t(2,4))),
           eval_der(coeff,dadd(t(1,3),t(2,3)),t(3,4)),
           dscale(eval_der(coeff,t(2,3),t(3,4)),-1),
           dscale(eval_der(coeff,dadd(t(1,2),t(1,3)),dadd(t(2,4),t(3,4))),-1),
           dscale(eval_der(coeff,t(1,2),t(2,3)),-1)]
    return dadd(*terms)

def main():
    q7=check_special('q7',q7_coeff)
    h9=check_special('h9',{w:Q(c,2) for w,c in h9_twice.items()})
    x=var('x');y=var('y');xy=add(x,y)
    h5=[{'xxxxy':1,'xxxyy':-1,'xxyxy':2},
        {'xxxyy':-1,'xxyxy':Q(-1,2),'xxyyy':1,'xyxyy':Q(3,2)},
        {'xxyyy':1,'xyxyy':-1,'xyyyy':-1}]
    k5=[{'xxxyy':-1,'xxyxy':2},{'xxyyy':1,'xyxyy':Q(3,2)},{'xyyyy':-1}]
    for i,(hc,kc) in enumerate(zip(h5,k5),1):
        h=poly(hc);k=poly(kc)
        assert not add(bracket(h,y),scale(bracket(k,xy),-1))
        print('h5',i,'special verified; metabelian',metabelian(h))
    t=check_braid()
    defect=pentagon(q7_coeff,t)
    target='aaaaabcb'
    coefficient=defect['a'].get(target,0)
    print('q7 pentagon support by generator',{k:len(v) for k,v in defect.items()})
    print('q7 pentagon coefficient on a ->',target,':',coefficient)
    assert abs(coefficient)==16
    print('q7 pentagon nonzero modulo every prime ell >= 5: YES')
    output={'conventions':{'bracket':'uv-vu','pentagon':
      'q(t12,t23+t24)+q(t13+t23,t34)-q(t23,t34)-q(t12+t13,t24+t34)-q(t12,t23)'},
      'q7_coeff':q7_coeff,'h9_twice':h9_twice,
      'pentagon_defect':{k:{w:str(c) for w,c in sorted(v.items())} for k,v in defect.items()}}
    dest=Path(__file__).resolve().parent.parent/'records'/'lie_witnesses_exact.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__':main()
