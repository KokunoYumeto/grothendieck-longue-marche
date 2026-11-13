#!/usr/bin/env python3
"""Exploratory monodromy of the specified seven-point A4 orbit map.

Projection crossings are initially numerical; an observed kernel word still
requires exact crossing certification before it is a proved result.
"""
import contextlib
import io
import json
from pathlib import Path
from itertools import combinations
import numpy as np
from numpy.polynomial import polynomial as pol
import sympy as sp

with contextlib.redirect_stdout(io.StringIO()):
    import a5_centralizer_permutations as a


def canon(M):
    M=tuple(sp.sympify(v) for v in M)
    c=next(v for v in M if v!=0)
    return tuple(sp.simplify(v/c) for v in M)


def mm(A,B):
    x,y,z,w=A;u,v,r,s=B
    return canon((x*u+y*r,x*v+y*s,z*u+w*r,z*v+w*s))


def invword(w):return [-x for x in w[::-1]]


def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out


def subst(w,aut):
    out=[]
    for x in w:
        image=aut[x-1] if x>0 else invword(aut[-x-1])
        for y in image:
            if out and out[-1]==-y:out.pop()
            else:out.append(y)
    return out


def compose(f,g):return [subst(w,f) for w in g]


def braid_aut(w,n=7):
    aut=[[i+1] for i in range(n)]
    for k in w:
        j=abs(k)-1
        elementary=[[i+1] for i in range(n)]
        if k>0:
            elementary[j]=[j+1,j+2,-j-1]
            elementary[j+1]=[j+1]
        else:
            elementary[j]=[j+2]
            elementary[j+1]=[-j-2,j+1,j+2]
        aut=compose(aut,elementary)
    return aut


def sphere_aut(w):
    aut=braid_aut(w)
    filling=[[i+1] for i in range(6)]+[[-6,-5,-4,-3,-2,-1]]
    return [subst(aut[i],filling) for i in range(6)]


def cyclic_core(w):
    u=[]
    while len(w)>1 and w[0]==-w[-1]:
        u.append(w[0]);w=w[1:-1]
    return u,w


def outer_identity(aut):
    u,c=cyclic_core(aut[0])
    if c!=[1]:return False
    adjusted=[red(invword(u)+w+u) for w in aut]
    v,c=cyclic_core(adjusted[1])
    if c!=[2] or any(abs(x)!=1 for x in v):return False
    return all(red(invword(v)+w+v)==[i+1] for i,w in enumerate(adjusted))


def outer_equal(f,g):
    """Compare pure outer automorphisms without expanding inverse composites."""
    u,fc=cyclic_core(f[0]);v,gc=cyclic_core(g[0])
    assert fc==gc==[1]
    ff=[red(invword(u)+w+u) for w in f]
    gg=[red(invword(v)+w+v) for w in g]
    p,fc=cyclic_core(ff[1]);q,gc=cyclic_core(gg[1])
    assert fc==gc==[2]
    def first_power(w):
        j=n=0
        while j<len(w) and abs(w[j])==1:
            n+=w[j];j+=1
        return n,w[j:]
    pn,pt=first_power(p);qn,qt=first_power(q)
    if pt!=qt:return False
    k=pn-qn
    prefix=[1]*k if k>=0 else [-1]*(-k)
    return all(red(prefix+w+invword(prefix))==target for w,target in zip(gg,ff))


def main():
    ag=a.a;rg=a.cycle(1,2,3)
    AM=canon((-1,0,0,1));RM=canon((1,sp.I,1,-sp.I))
    matrices={a.one:canon((1,0,0,1))};queue=[a.one]
    for g in queue:
        for h,H in ((ag,AM),(rg,RM)):
            gh=a.mul(g,h);M=mm(matrices[g],H)
            if gh in matrices:assert matrices[gh]==M
            else:matrices[gh]=M;queue.append(gh)
    assert len(matrices)==12
    assert all(mm(matrices[g],matrices[h])==matrices[a.mul(g,h)]
               for g in a.A4 for h in a.A4)
    I=min(a.seven_point_sets,key=lambda s:sorted(s))
    orbit={frozenset(a.vertex_action(g)[i] for i in I) for g in a.A4}
    assert orbit==a.seven_point_sets and len(orbit)==12
    labels=sorted(I)
    Ms=[matrices[a.group_labels[i]] for i in labels]
    Mc=[tuple(complex(sp.N(v,17)) for v in M) for M in Ms]
    z=sp.Symbol('z')
    poles=[]
    for hi,H in enumerate(a.cyclic_subgroups):
        g=min(H-{a.one});aa,b,c,d=matrices[g]
        eq=sp.expand(c*z*z+(d-aa)*z-b)
        roots=sp.solve(eq,z)
        if c==0:roots.append(sp.oo)
        assert len(roots)==2
        for root in roots:
            if root!=sp.oo:
                poles.append({'stabilizer_index':hi,'stabilizer_order':len(H),
                              'exact':str(root),'point':complex(sp.N(root,17))})
    assert len(poles)==13
    poles.sort(key=lambda r:(r['point'].real,r['point'].imag))
    projection=1+0.173j
    def positions(p):
        return [projection*(aa*p+b)/(c*p+d) for aa,b,c,d in Mc]
    def ordering(p):return sorted(range(7),key=lambda i:positions(p)[i].real)
    cache={}
    def segment(p,q):
        if (p,q) in cache:return cache[p,q]
        if (q,p) in cache:return invword(cache[q,p])
        events=[]
        dp=q-p
        for i,j in combinations(range(7),2):
            aa,b,c,d=Mc[i];ee,f,g,h=Mc[j]
            ni=np.array([aa*p+b,aa*dp]);di=np.array([c*p+d,c*dp])
            nj=np.array([ee*p+f,ee*dp]);dj=np.array([g*p+h,g*dp])
            num=pol.polysub(pol.polymul(ni,dj),pol.polymul(nj,di))
            den=pol.polymul(di,dj)
            coeff=np.real(projection*pol.polymul(num,np.conjugate(den)))
            scale=max(abs(coeff))
            assert scale>1e-15
            while len(coeff)>1 and abs(coeff[-1])<1e-12*scale:coeff=coeff[:-1]
            for root in pol.polyroots(coeff):
                if abs(root.imag)>1e-7 or not 1e-8<root.real<1-1e-8:continue
                t=float(root.real)
                eps=min(1e-6,t/2,(1-t)/2)
                before=pol.polyval(t-eps,coeff)
                after=pol.polyval(t+eps,coeff)
                if before*after>=0:continue
                events.append((t,i,j))
        events.sort()
        order=ordering(p);word=[]
        for t,i,j in events:
            oi,oj=order.index(i),order.index(j)
            assert abs(oi-oj)==1,(p,q,t,i,j,order,events)
            vals=positions(p+t*dp)
            left=i if oi<oj else j
            right=j if oi<oj else i
            sign=1 if vals[left].imag>vals[right].imag else -1
            assert abs(vals[i].imag-vals[j].imag)>1e-7
            word.append(sign*(min(oi,oj)+1))
            order[oi],order[oj]=order[oj],order[oi]
        assert order==ordering(q),(p,q,order,ordering(q))
        cache[p,q]=red(word)
        return cache[p,q]
    base=5+4j;r=.027
    words=[]
    for row in poles:
        c=row['point']
        bl=c-r-r*1j;br=c+r-r*1j;tr=c+r+r*1j;tl=c-r+r*1j
        top=complex(c.real-r,4)
        path=[base,top,bl,br,tr,tl,bl,top,base]
        word=[]
        for p,q in zip(path,path[1:]):word+=segment(p,q)
        word=red(word)
        words.append(word)
        row['braid_word']=word
        row['braid_word_length']=len(word)
        row['point']=[c.real,c.imag]
        print('Meridian',len(words),'length',len(word),flush=True)
    autos=[sphere_aut(w) for w in words]
    inverses=[sphere_aut(invword(w)) for w in words]
    assert all(outer_identity(compose(f,g)) for f,g in zip(autos,inverses))
    lengths=[sum(map(len,f)) for f in autos]
    print('Automorphism lengths',lengths,flush=True)
    relations=[]
    for i,j in combinations(range(13),2):
        if outer_equal(compose(autos[i],autos[j]),compose(autos[j],autos[i])):
            relations.append({'type':'commutator','source_meridians':[i+1,j+1]})
            print('COMMUTING MERIDIAN IMAGES',i+1,j+1,flush=True)
        if outer_equal(autos[i],autos[j]):
            relations.append({'type':'equal_images','source_meridians':[i+1,j+1]})
            print('EQUAL MERIDIAN IMAGES',i+1,j+1,flush=True)
    ans={'seven_point_subset':labels,'A4_orbit_size':len(orbit),
         'Mobius_matrices':[[str(v) for v in M] for M in Ms],
         'projection_multiplier':[1,.173],'domain_basepoint':[5,4],
         'square_half_width':r,'meridians':poles,
         'automorphism_lengths':lengths,'potential_kernel_relations':relations,
         'scope':'Exact group and word operations, with numerical crossing extraction not yet certified.'}
    Path(__file__).with_name('seven_point_braid_explore_output.json').write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps(ans,indent=2))


if __name__=='__main__':main()
