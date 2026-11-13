#!/usr/bin/env python3
"""Independent full pentagon audit of published DLL targets N^(0),N^(1),N^(2).

The six permutation generators are extracted as data from the authors'
PackageGT (2022-03-16), using the current official download URL recorded
in e_dll_examples.json. No package code is imported or executed.
Products are functional composition, matching PackageGT's compAll;
this is opposite the raw SymPy multiplication convention.
"""
from pathlib import Path
from math import gcd,lcm
import json,time
from e_braid_core import Table
base=Path(__file__).resolve().parent;start=time.time()
raw=json.loads((base/'e_dll_examples.json').read_text())
qs=json.loads((base/'e_b3_quotients_complete.json').read_text())['quotients']
audit=json.loads((base/'e_b3_hexagons.json').read_text())['rows']

def mul(p,q):return tuple(p[v] for v in q)
def inv(p):
    a=[0]*len(p)
    for i,j in enumerate(p):a[j]=i
    return tuple(a)
def prod(*ps):
    r=tuple(range(len(ps[0])))
    for p in ps:r=mul(r,p)
    return r
def vmul(p,q):return tuple(mul(a,b) for a,b in zip(p,q))
def vinv(p):return tuple(inv(a) for a in p)
def closure(gs,I,op):
    todo=[I];seen={I}
    for v in todo:
        for g in gs:
            w=op(v,g)
            if w not in seen:seen.add(w);todo.append(w)
    return todo

def map_group(gs,targets,I,J,op,op2):
    # Checks every generator edge, hence every relation of the finite source.
    images={I:J};todo=[I]
    for v in todo:
        for g,t in zip(gs,targets):
            w=op(v,g);z=op2(images[v],t)
            if w in images:
                if images[w]!=z:return None
            else:images[w]=z;todo.append(w)
    if len(set(images.values()))!=len(images):return None
    return images

def pb4_check(g):
    x,y,z,u,v,w=g;c=prod(x,z,y)
    assert all(mul(c,t)==mul(t,c) for t in (x,y,z))
    assert prod(inv(x),u,x)==prod(u,v,u,inv(v),inv(u))
    assert prod(inv(x),v,x)==prod(u,v,inv(u))
    assert prod(inv(x),w,x)==w
    assert prod(inv(y),u,y)==u
    assert prod(inv(y),v,y)==prod(v,w,v,inv(w),inv(v))
    assert prod(inv(y),w,y)==prod(v,w,inv(v))
    assert prod(inv(z),u,z)==prod(u,w,u,inv(w),inv(u))
    h=prod(u,w,inv(u),inv(w))
    assert prod(inv(z),v,z)==prod(h,v,inv(h))
    assert prod(inv(z),w,z)==prod(u,w,inv(u))
    # Conjugation by each Artin generator must preserve the kernel.
    conjugates=[(x,prod(x,z,inv(x)),y,v,prod(x,u,inv(x)),w),
                (z,y,prod(y,x,inv(y)),u,w,prod(y,v,inv(y))),
                (x,v,u,prod(w,z,inv(w)),prod(w,y,inv(w)),w)]
    I=tuple(range(len(x)))
    for gg in conjugates:assert map_group(g,gg,I,I,mul,mul) is not None
    return len(closure(g,I,mul))

rows=[]
for j in (0,1,2):
    gs=tuple(map(tuple,raw['examples'][j]));g12,g23,g13,g14,g24,g34=gs
    g4order=pb4_check(gs);I=(tuple(range(len(g12))),)*5
    # Five insertion/cabling maps in DLL, ordered 123;12,3,4;1,23,4;1,2,34;234.
    X=(g12,mul(g13,g23),mul(g12,g13),g12,g23)
    Y=(g23,g34,mul(g24,g34),mul(g23,g24),g34)
    Z=(g13,mul(g14,g24),g14,mul(g13,g14),g24)
    C=vmul(vmul(X,Z),Y)
    assert all(vmul(C,g)==vmul(g,C) for g in (X,Y,Z))
    H=closure([X,Y],I,vmul);P=closure([X,Y,C],I,vmul)
    found=[]
    for ordinal,q in enumerate(qs,1):
        if not q['kernel_contained_in_PB3'] or q['index']!=6*len(P):continue
        t=Table(q);a,b=t.a,t.b
        xx,yy,cc=t.pow(a,2),t.pow(b,2),t.pow(t.mul(a,b),3)
        mp=map_group([X,Y,C],[xx,yy,cc],I,0,vmul,lambda u,v:int(t.M[u,v]))
        if mp is not None and len(mp)==len(P):found.append((ordinal,t,mp))
    assert len(found)==1
    ordinal,t,mp=found[0];reverse={v:k for k,v in mp.items()}
    r=audit[ordinal-1];a,b=t.a,t.b;Xq,Yq=t.pow(a,2),t.pow(b,2)
    Zq=t.mul(b,Xq,int(t.inv[b]));Cq=t.pow(t.mul(a,b),3);Nord=r['N_ord']
    Hq=t.closure([Xq,Yq]);derived=set(t.closure([t.mul(h,t.mul(Xq,Yq,int(t.inv[Xq]),int(t.inv[Yq])),int(t.inv[h])) for h in Hq]))
    practical=[];charming=[];pentagon_tests=0
    for m in range(Nord):
        if gcd(2*m+1,Nord)!=1:continue
        ap=t.pow(a,2*m+1);bl=t.pow(b,2*m+1)
        h1=t.mul(a,b,t.pow(t.mul(Zq,Yq),m));h2=t.mul(b,a,t.pow(t.mul(Xq,Zq),m))
        for f in Hq:
            bp=t.mul(int(t.inv[f]),bl,f)
            if t.mul(ap,bp)!=t.mul(int(t.inv[f]),h1):continue
            if t.mul(bp,ap)!=t.mul(h2,f):continue
            if len(t.closure([t.pow(ap,2),t.pow(bp,2)]))!=len(Hq):continue
            ff=reverse[f];pentagon_tests+=1
            if prod(ff[4],ff[2],ff[0])!=prod(ff[3],ff[1]):continue
            practical.append([m,f+1])
            if f in derived:charming.append([m,f+1])
    expected_practical=(4,8,18)[j];expected_charming=(4,4,6)[j]
    assert len(practical)==expected_practical and len(charming)==expected_charming
    assert set(map(tuple,charming))<=set((m,f) for m,f,s in r['pairs_m_fpoint_sourcekernel'])
    known=set((m,f) for m,f,s in r['known_genuine_full_GT_pairs'])
    known_here=[v for v in charming if tuple(v) in known]
    if j in (0,1):assert len(known_here)==len(charming)
    out={'DLL_index':j,'PB4_quotient_order':g4order,'PB3_quotient_order':len(P),'B3_quotient_order':6*len(P),
         'matching_LINS_kernel':ordinal,'H_order':len(H),'H_derived_order':len(derived),
         'N_ord':Nord,'pure_abelianization_order':len(P)//len(derived),
         'original_PB4_relations_verified':True,'B4_normality_verified_on_all_Cayley_edges':True,
         'five_cabling_kernel_identification_verified':True,'pentagon_tests':pentagon_tests,
         'all_practical_shadows':practical,'all_charming_shadows':charming,
         'known_genuine_charming_shadows':known_here,
         'all_charming_are_genuine':len(known_here)==len(charming),
         'canonical_forgetful_refinement_B3_order':6*len(derived)*Nord**3}
    rows.append(out);print(out,flush=True)
result={'source':raw['source'],'source_file':raw['source_file'],'targets':[0,1,2],'bound_on_actual_B3_quotient_order':1000,
        'scope':'All practical and charming full-GT shadows for these three published arity-four targets. All charming shadows of targets0/1 are proved genuine; target2 has certified genuine sublist, no total genuineness claim.',
        'rows':rows,'seconds':round(time.time()-start,3)}
(base/'e_dll_pentagons.json').write_text(json.dumps(result,indent=2)+'\n')
print('COMPLETE seconds',result['seconds'],flush=True)
