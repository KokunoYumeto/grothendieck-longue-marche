#!/usr/bin/env python3
"""The exact orbit-two source quotient remaining after D.43's whole family.

The even marking uses two noninterchangeable A7 representations.  An
explicit short relation separating the two representations, its full
normal closure, and the two projections certify the full A7 squared
image without enumerating 6,350,400 pairs.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,time

OUT=Path(__file__).resolve().parent;started=time.time();n=7
I=tuple(range(n))
def cycles(*blocks):
    a=list(I)
    for b in blocks:
        for i,x in enumerate(b):a[x]=b[(i+1)%len(b)]
    return tuple(a)
def mul(a,b):return tuple(a[b[i]] for i in range(n))
def inv(a):
    out=[0]*n
    for i,x in enumerate(a):out[x]=i
    return tuple(out)
def parity(a):return sum(a[i]>a[j] for i in range(n) for j in range(i+1,n))%2
def order(a):
    b=a;k=1
    while b!=I:k+=1;b=mul(b,a)
    return k
a=cycles((0,3,6));b=cycles((0,1,2),(3,4,5))
assert order(a)==order(b)==3
gens=[a,b,inv(a),inv(b)]
L=[I];ix={I:0};words=[[]]
for g,w in zip(L,words):
    for j,h in enumerate(gens):
        k=mul(g,h)
        if k not in ix:
            ix[k]=len(L);L.append(k);words.append(w+[j])
assert len(L)==2520 and all(parity(g)==0 for g in L)
centralizers=[sum(mul(g,h)==mul(h,g) for g in L) for h in [a,b]]
assert centralizers==[36,9]
def inverse_word(w):return [(j+2)%4 for j in reversed(w)]
def evaluate(w,gg=gens):
    out=I
    for j in w:out=mul(out,gg[j])
    return out
swapgens=[b,a,inv(b),inv(a)]
second=[evaluate(w,swapgens) for w in words]
separating=None
for g,w,v in zip(L,words,second):
    for j,h in enumerate(gens):
        k=mul(g,h);kk=ix[k]
        vv=mul(v,swapgens[j])
        if vv!=second[kk]:
            separating=w+[j]+inverse_word(words[kk]);break
    if separating is not None:break
assert separating is not None and evaluate(separating)==I
z=evaluate(separating,swapgens);assert z!=I
conjugates=sorted({mul(mul(g,z),inv(g)) for g in L})
normal={I};queue=[I]
for g in queue:
    for h in conjugates:
        k=mul(g,h)
        if k not in normal:normal.add(k);queue.append(k)
assert normal==set(L)

# The paired subgroup therefore contains 1 x A7 and surjects the first
# A7.  These are explicit source words, not only an order guess.
def bword(w):
    blocks=[[1],[0,1,0],[2],[0,2,0]]
    return [x for j in w for x in blocks[j]]
separator_b=bword(separating)

# Semidirect coordinates are (g,h,epsilon), with s interchanging factors.
J1=(I,I,0)
def jm(x,y):
    g,h,e=x;u,v,f=y
    if e:u,v=v,u
    return mul(g,u),mul(h,v),(e+f)%2
def ji(x):
    g,h,e=x
    return (inv(h),inv(g),1) if e else (inv(g),inv(h),0)
S=(I,I,1);R=(a,b,0)
assert jm(S,S)==J1 and jm(jm(R,R),R)==J1
def jord(x):
    q=x;k=1
    while q!=J1:k+=1;q=jm(q,x)
    return k
T=jm(S,R);X=ji(jm(T,T))
def jmodel(w):
    q=J1;rr=ji(R)
    for v in w:q=jm(q,[S,R,rr][v])
    return q
assert jmodel(separator_b)==(I,z,0)
assert jmodel([0]+separator_b+[0])==(z,I,0)
assert jord(T)==14 and jord(X)==7
def action14(x):
    g,h,e=x;out=[]
    for k in range(14):
        block,i=divmod(k,7)
        block^=e
        out.append(7*block+(g[i] if block==0 else h[i]))
    return tuple(out)
ps=action14(S);pr=action14(R)
def perm_mul(a,b):return tuple(a[b[i]] for i in range(14))
assert perm_mul(ps,ps)==tuple(range(14))
assert perm_mul(perm_mul(pr,pr),pr)==tuple(range(14))
# Exhaust all factor pairs needed to verify the literal embedding rules.
for g in L:
    assert action14((g,I,0))[:7]==g
    assert action14((I,g,0))[7:]==tuple(7+x for x in g)
    assert jm(jm(S,(g,I,0)),S)==(I,g,0)
assert sum(ps[i]>ps[j] for i in range(14) for j in range(i+1,14))%2==1

summary={
    'even_simple_group':'A7','even_simple_order':len(L),
    'r_first_factor':list(a),'r_second_factor':list(b),
    'centralizer_orders_of_two_marked_generators':centralizers,
    'two_markings_cannot_be_interchanged_by_an_automorphism':True,
    'separating_even_word':separating,
    'separating_B_word':separator_b,
    'separating_word_B_length':len(separator_b),
    'first_projection_of_separating_word_is_identity':True,
    'second_projection_of_separating_word':list(z),
    'second_projection_conjugacy_class_size':len(conjugates),
    'second_projection_normal_closure_order':len(normal),
    'actual_even_pair_image_order':len(L)**2,
    'actual_whole_source_image_order':2*len(L)**2,
    's_order':jord(S),'r_order':jord(R),'t_order':jord(T),'x_order':jord(X),
    'faithful_degree14_s':list(ps),'faithful_degree14_r':list(pr),
    'involution_interchanges_the_two_simple_factors':True,
    'remaining_full_source_kernel_image':'A7 x A7',
    'scope':'Exact finite marked maps and an explicit kernel-separating word. The simultaneous whole-family extension and exclusion of this orbit-two quotient are proved in D43; no cofinality or full free-profinite lift is asserted.',
    'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'A7_elements':[list(g) for g in L],
      'A7_generator_words':words,
      'normal_closure_generators':[list(g) for g in conjugates],
      'all_factor_permutations_sha256':hashlib.sha256(bytes(v for g in L for v in g)).hexdigest()}
(OUT/'d_cm_simple_even_family.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
