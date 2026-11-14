#!/usr/bin/env python3
"""Actual solvable-even-top residual after the anabelian-even extension.

The complete source marking is A5^4 semidirect S4, with the indicated
canonical mod-four S4 top.  Schreier words for its rank-five top kernel
certify a full A5 projection and two unequal coordinate kernels.  The
primitive S4 block action then proves the entire A5^4 kernel.
"""
from pathlib import Path
from collections import deque
import json,time

OUT=Path(__file__).resolve().parent;started=time.time()
def cycles(n,*blocks):
    a=list(range(n))
    for b in blocks:
        for i,x in enumerate(b):a[x]=b[(i+1)%len(b)]
    return tuple(a)
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    out=[0]*len(a)
    for i,x in enumerate(a):out[x]=i
    return tuple(out)
def generated(gs):
    I=tuple(range(len(gs[0])));out=[I];seen={I}
    for a in out:
        for b in gs:
            c=mul(a,b)
            if c not in seen:seen.add(c);out.append(c)
    return out
def order(a):
    I=tuple(range(len(a)));b=a;k=1
    while b!=I:k+=1;b=mul(b,a)
    return k
I5=tuple(range(5));I4=tuple(range(4))
aa=cycles(5,(0,1),(2,3));bb=cycles(5,(0,2,4))
L=generated([aa,bb]);assert len(L)==60
st=cycles(4,(0,1));rt=cycles(4,(1,2,3))
top=[I4];ti={I4:0};words=[[]]
for q,w in zip(top,words):
    for a,g in [(0,st),(1,rt)]:
        h=mul(q,g)
        if h not in ti:ti[h]=len(top);top.append(h);words.append(w+[a])
assert len(top)==24
vs=[I5]*4;vs[2]=aa
vr=[I5]*4;vr[0]=bb
S=(tuple(vs),st);R=(tuple(vr),rt)
IDENT=((I5,)*4,I4)
def wm(a,b):
    v,q=a;w,h=b;iq=inv(q)
    return tuple(mul(v[i],w[iq[i]]) for i in range(4)),mul(q,h)
def wi(a):
    v,q=a;iq=inv(q)
    return tuple(inv(v[q[i]]) for i in range(4)),iq
assert wm(S,S)==IDENT and wm(wm(R,R),R)==IDENT
def evaluate(w):
    out=IDENT;gs=[S,R,wi(R)]
    for a in w:out=wm(out,gs[a])
    return out
def iw(w):return [0 if a==0 else 3-a for a in reversed(w)]
lifts=[evaluate(w) for w in words]
assert [q for v,q in lifts]==top
schreier=[]
for q,w,h in zip(top,words,lifts):
    for letter,g in [(0,S),(1,R)]:
        nxt=ti[mul(q,g[1])]
        sw=w+[letter]+iw(words[nxt])
        v,qt=evaluate(sw)
        assert qt==I4
        schreier.append({'top':ti[q],'letter':letter,'word':sw,'base':[list(z) for z in v]})
projected=[tuple(row['base'][0]) for row in schreier]
assert set(generated(projected))==set(L)
kernel_vectors=[tuple(tuple(v) for v in row['base']) for row in schreier]
projected_lifts={I5:((I5,)*4,[])};projected_queue=[I5]
separator=None
for h in projected_queue:
    vh,wh=projected_lifts[h]
    for row,v in zip(schreier,kernel_vectors):
        vv=tuple(mul(a,b) for a,b in zip(vh,v));k=vv[0]
        ww=wh+row['word']
        if k not in projected_lifts:
            projected_lifts[k]=(vv,ww);projected_queue.append(k)
        else:
            vp,wp=projected_lifts[k]
            difference=tuple(mul(a,inv(b)) for a,b in zip(vv,vp))
            if difference!=(I5,)*4:
                sw=ww+iw(wp)
                assert evaluate(sw)==(difference,I4) and difference[0]==I5
                separator={'word':sw,'base':[list(a) for a in difference]};break
    if separator is not None:break
assert separator is not None

# The top action is the actual canonical PSL2(Z/4) source marking.
MI=(1,0,0,1);MS=(0,1,3,0);MR=(0,3,1,3)
def canon(a):return min(a,tuple(-x%4 for x in a))
def mm(a,b):
    return canon(((a[0]*b[0]+a[1]*b[2])%4,(a[0]*b[1]+a[1]*b[3])%4,
                  (a[2]*b[0]+a[3]*b[2])%4,(a[2]*b[1]+a[3]*b[3])%4))
matmap={MI:I4};todo=[MI]
for q in todo:
    for m,p in [(MS,st),(MR,rt)]:
        z=mm(q,m);u=mul(matmap[q],p)
        if z in matmap:assert matmap[z]==u
        else:matmap[z]=u;todo.append(z)
assert len(matmap)==24 and set(matmap.values())==set(top)
assert all(matmap[mm(a,b)]==mul(matmap[a],matmap[b]) for a in todo for b in todo)

def word_order(a):
    q=a;k=1
    while q!=IDENT:k+=1;q=wm(q,a)
    return k
T=wm(S,R);X=wi(wm(T,T))
def action(a):
    v,q=a
    return tuple(5*q[block]+v[q[block]][i] for block in range(4) for i in range(5))
ps=action(S);pr=action(R)
assert order(ps)==2 and order(pr)==3
even_top=generated([rt,mul(mul(st,rt),st)])
assert len(even_top)==12
derived_top=generated([mul(mul(mul(a,b),inv(a)),inv(b)) for a in even_top for b in even_top])
assert len(derived_top)==4
assert len(generated([mul(mul(mul(a,b),inv(a)),inv(b)) for a in derived_top for b in derived_top]))==1
summary={
    'internal_simple_group':'A5','internal_simple_order':60,
    'top_group':'S4','top_order':24,'even_top_group':'A4','even_top_order':12,
    'even_top_derived_order':4,'even_top_second_derived_order':1,
    'canonical_mod4_to_S4_isomorphism_all576_products_checked':True,
    'source_s_top':list(st),'source_r_top':list(rt),
    'source_s_base':[list(v) for v in S[0]],'source_r_base':[list(v) for v in R[0]],
    'source_s_order':word_order(S),'source_r_order':word_order(R),
    'source_t_order':word_order(T),'source_x_order':word_order(X),
    'schreier_kernel_generators_checked':len(schreier),
    'kernel_first_coordinate_image_order':60,
    'different_coordinate_kernel_word':separator['word'],
    'different_coordinate_kernel_value':separator['base'],
    'top_action_is_full_S4_and_primitive':True,
    'actual_full_kernel_order':60**4,
    'actual_even_source_image_order':60**4*12,
    'actual_whole_source_image_order':60**4*24,
    'faithful_degree20_s':list(ps),'faithful_degree20_r':list(pr),
    'remaining_source_kernel_image':'A5^4',
    'scope':'Exact marked wreath source and canonical mod4 top. The anabelian-even completed extension and precise remaining-kernel image are proved in D44; no full profinite lift is asserted.',
    'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'A5_elements':[list(a) for a in L],
      'S4_elements':[list(a) for a in top],'S4_source_words':words,
      'Schreier_kernel_words_and_values':schreier,
      'canonical_mod4_isomorphism':[{'matrix':list(m),'permutation':list(matmap[m])} for m in todo]}
(OUT/'d_cm_anabelian_even.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
