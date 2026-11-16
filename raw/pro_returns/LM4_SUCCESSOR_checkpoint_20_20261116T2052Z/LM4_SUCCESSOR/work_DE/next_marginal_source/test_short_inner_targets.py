"""Exact finite source-orbit witnesses for short canonical filling-kernel words.

The test seeks alpha_l^-1(target) in the already certified finite radius1
Stallings subgroup.  Success proves only the listed word's membership in
the actual source orbit group, not its invariance under arbitrary inners.
"""
from pathlib import Path
import json,itertools,time
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'positive_fiber_data.json').read_text())
P=json.loads((HERE/'stallings_orbit_radius1.json').read_text())
graph={int(a):{int(c):b for c,b in e.items()} for a,e in P['final_graph'].items()}
acts={int(k)+1:{int(i):tuple(w) for i,w in v.items()} for k,v in D['old_actions'].items()}
acts.update({-int(k)-1:{int(i):tuple(w) for i,w in v.items()} for k,v in D['old_inverse_actions'].items()})
def red(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return tuple(out)
def inv(w):return tuple(-a for a in w[::-1])
def mul(*ww):return red(itertools.chain.from_iterable(ww))
def sub(w,A):return mul(*(A[a] if a>0 else inv(A[-a]) for a in w))
def member(w):
    at=0
    for a in w:
        if a not in graph[at]:return False
        at=graph[at][a]
    return at==0
order=sorted(acts,key=lambda a:sum(map(len,acts[a].values())))
Q=[()]+[(a,) for i in D['retained_basis'] for a in(i,-i)]
targets=[(q,j,mul(q,(j,),inv(q))) for q in Q for j in D['killed_basis']]
found=[];missing=[];start=time.time()
for q,j,w in targets:
    witness=None
    if member(w):witness=((),w)
    if witness is None:
        for a in order:
            v=sub(w,acts[-a])
            if member(v):witness=((a,),v);break
    if witness is None:
        for a in order:
            v=sub(w,acts[-a])
            for b in order:
                if b==-a:continue
                vv=sub(v,acts[-b])
                if member(vv):witness=((a,b),vv);break
            if witness:break
    if witness:
        l,v=witness
        check=v
        for a in reversed(l):check=sub(check,acts[a])
        assert check==w and member(v)
        found.append({'q':q,'j':j,'target':w,'source_conjugator':l,'Stallings_member':v})
        print('FOUND',q,j,'source',l,'member_length',len(v),'elapsed',round(time.time()-start,2),flush=True)
    else:
        missing.append({'q':q,'j':j,'target':w})
        print('NOT FOUND at radius2',q,j,'elapsed',round(time.time()-start,2),flush=True)
    (HERE/'short_inner_target_witnesses.json').write_text(json.dumps({'found':found,'not_found_at_bound':missing,
        'scope':'Finite membership witnesses only; no full subgroup-invariance claim.'},separators=(',',':'))+'\n')
print('Complete',len(found),'of',len(targets),'short targets have exact finite source-orbit witnesses.',flush=True)
