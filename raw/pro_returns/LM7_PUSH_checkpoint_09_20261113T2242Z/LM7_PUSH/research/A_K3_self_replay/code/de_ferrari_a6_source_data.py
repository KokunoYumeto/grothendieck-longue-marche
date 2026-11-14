#!/usr/bin/env python3
"""Read-only modular and literal Schreier data for the A6 refinements.

This reconstructs the exact B=C2*C3, F=ker(B->SL2(F2)) and rank-97
N=ker(B->SL2(Z/12)/{+/-1}) words.  It does not execute, import or rewrite
the earlier finite-check main programs.  The resulting N basis is compared
word for word with the independently retained SL2(F5) source certificate.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def load_data():
    unit=(1,0,0,1)
    def multiply(a,b,m=12):
        return tuple(v%m for v in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                                  a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
    def representative(a):
        return min(tuple(a),tuple(-v%12 for v in a))
    def times(a,b):return representative(multiply(a,b))
    def inverse(a):return representative((a[3],-a[1]%12,-a[2]%12,a[0]))
    Q=sorted({representative(a) for a in product(range(12),repeat=4)
              if (a[0]*a[3]-a[1]*a[2])%12==1})
    ss=representative((0,1,11,0));rr=representative((0,11,1,11))
    rr2=times(rr,rr)
    assert len(Q)==576 and times(ss,ss)==times(rr2,rr)==unit
    def binv(w):return [0 if a==0 else -a for a in reversed(w)]
    def bpower(w,n):return list(w)*n if n>=0 else binv(w)*(-n)
    def bvalue(w):
        out=unit
        for a in w:out=times(out,ss if a==0 else rr if a==1 else rr2)
        return out
    sv={q:('s',min(q,times(q,ss))) for q in Q}
    rv={q:('r',min(q,times(q,rr),times(q,rr2))) for q in Q}
    adj={v:[] for v in set(sv.values())|set(rv.values())}
    for e,q in enumerate(Q):
        adj[sv[q]].append((rv[q],e,1));adj[rv[q]].append((sv[q],e,-1))
    root=sv[unit];paths={root:[]};tree=set();queue=deque([root])
    while queue:
        v=queue.popleft()
        for w,e,sign in adj[v]:
            if w not in paths:
                paths[w]=paths[v]+[(e,sign)];tree.add(e);queue.append(w)
    assert len(paths)==len(adj)==480
    chords=sorted(set(range(576))-tree);assert len(chords)==97
    def pathword(path):
        q=unit;word=[]
        for e,sign in path:
            qe=Q[e]
            if sign==1:
                if qe!=q:assert qe==times(q,ss);word.append(0)
            else:
                if qe==times(q,rr):word.append(1)
                elif qe==times(q,rr2):word.append(-1)
                else:assert qe==q
            q=qe
        if q!=unit:assert q==ss;word.append(0)
        return word
    Nwords=[pathword(paths[sv[Q[e]]]+[(e,1)]+
                         [(a,-b) for a,b in reversed(paths[rv[Q[e]]])]) for e in chords]
    assert all(bvalue(w)==unit for w in Nwords)
    old=json.loads((HERE/'de_ferrari_sl2_5_N.json').read_text())
    ordering=old['selected_original_N_indices']+old['extra_original_N_indices']
    assert sorted(ordering)==list(range(97))
    assert [Nwords[i] for i in ordering]==old['input_generator_literal_B_words']
    Bpaths={unit:[]};queue=deque([unit])
    while queue:
        q=queue.popleft()
        for letter,g in ((0,ss),(1,rr)):
            qg=times(q,g)
            if qg not in Bpaths:Bpaths[qg]=Bpaths[q]+[letter];queue.append(qg)
    assert len(Bpaths)==576
    def red2(a):return tuple(v%2 for v in a)
    def mul2(a,b):return multiply(a,b,2)
    Q2=sorted(set(map(red2,Q)));s2=red2(ss);r2=red2(rr);r22=mul2(r2,r2)
    assert len(Q2)==6
    sv2={q:('s',min(q,mul2(q,s2))) for q in Q2}
    rv2={q:('r',min(q,mul2(q,r2),mul2(q,r22))) for q in Q2}
    adj2={v:[] for v in set(sv2.values())|set(rv2.values())}
    for q in Q2:adj2[sv2[q]].append((rv2[q],q));adj2[rv2[q]].append((sv2[q],q))
    seen={sv2[unit]};tree2=set();queue=deque(seen)
    while queue:
        v=queue.popleft()
        for w,q in adj2[v]:
            if w not in seen:seen.add(w);tree2.add(q);queue.append(w)
    fc={q:i+1 for i,q in enumerate(sorted(set(Q2)-tree2))};assert len(fc)==2
    def freered(w):
        out=[]
        for a in w:
            if out and out[-1]==-a:out.pop()
            else:out.append(a)
        return tuple(out)
    def finv(w):return tuple(-a for a in reversed(w))
    def graphword(w):
        q=unit;out=[]
        for a in w:
            qn=mul2(q,s2 if a==0 else r2 if a==1 else r22)
            if a:
                if q in fc:out.append(fc[q])
                if qn in fc:out.append(-fc[qn])
            q=qn
        assert q==unit
        return freered(out)
    xword=[-1,0,-1,0];yword=[0,-1,0,-1]
    gx,gy=graphword(xword),graphword(yword)
    gimages={1:gx,-1:finv(gx),2:gy,-2:finv(gy)}
    expr={():()};queue=deque([()]);inverse_basis={}
    while queue and len(inverse_basis)<2:
        val=queue.popleft();word=expr[val]
        if val in ((1,),(2,)):inverse_basis[val[0]]=word
        if len(word)>=8:continue
        for a in (1,-1,2,-2):
            if word and word[-1]==-a:continue
            nxt=freered(val+gimages[a])
            if nxt not in expr:expr[nxt]=word+(a,);queue.append(nxt)
    assert len(inverse_basis)==2
    def fword(word):
        out=()
        for a in graphword(word):
            z=inverse_basis[abs(a)];out+=z if a>0 else finv(z)
        return freered(out)
    def to_B(word):
        out=[]
        for a in word:
            z=xword if abs(a)==1 else yword
            out+=z if a>0 else binv(z)
        return out
    # These literal identities in the free graph prove both coordinate
    # morphisms are inverse, before they are used by any finite target.
    assert fword(xword)==(1,) and fword(yword)==(2,)
    for j in (1,2):assert graphword(to_B(inverse_basis[j]))==(j,)
    assert all(graphword(to_B(fword(w)))==graphword(w) for w in Nwords)
    return dict(Q=Q,ss=ss,rr=rr,unit=unit,times=times,inverse=inverse,
                representative=representative,multiply=multiply,Bpaths=Bpaths,
                binv=binv,bpower=bpower,bvalue=bvalue,Nwords=Nwords,
                Q2=Q2,s2=s2,r2=r2,r22=r22,mul2=mul2,xword=xword,yword=yword,
                fword=fword,to_B=to_B,freered=freered,finv=finv)

if __name__=='__main__':
    d=load_data()
    print(json.dumps({'Q_order':len(d['Q']),'Q2_order':len(d['Q2']),
                      'N_basis_rank':len(d['Nwords']),
                      'all_literal_N_words_match_existing_certificate':True,
                      'read_only_reconstruction':True},indent=2))
