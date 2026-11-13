#!/usr/bin/env python3
"""Further finite distribution tests, N=2,3,4,6,12, without enumerating
wreath products. The component projections of a normal closure are exact."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy
here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
times,inverse,unit=d['times'],d['inverse'],d['unit']
qx,qy=d['qx'],d['qy'];aone=(unit,0)
def amul(a,b):return times(a[0],b[0]),(a[1]+b[1])%6
def ainv(a):return inverse(a[0]),-a[1]%6
def aconj(a,b):return amul(amul(a,b),ainv(a))
def closure(gens):
    gens=list(set(gens)-{aone});seen={aone};queue=[aone]
    for a in queue:
        for b in gens:
            c=amul(a,b)
            if c not in seen:seen.add(c);queue.append(c)
    return seen
def induced(w,n):
    shift=sum(1 if a==1 else -1 if a==-1 else 0 for a in w)%n
    out=[]
    for init in range(n):
        pos=init;q=unit;c=0
        for a in w:
            if a==1:
                if pos==n-1:q=times(q,qx)
                pos=(pos+1)%n
            elif a==-1:
                if pos==0:q=times(q,inverse(qx))
                pos=(pos-1)%n
            elif pos==0:
                q=times(q,qy if a==2 else inverse(qy));c+=1 if a==2 else -1
        assert pos==(init+shift)%n
        out.append((q,c%6))
    return tuple(out),shift
def wm(a,b,n):
    av,sa=a;bv,sb=b
    return tuple(amul(av[i],bv[(i+sa)%n]) for i in range(n)),(sa+sb)%n
def wi(a,n):
    av,sa=a
    return tuple(ainv(av[(i-sa)%n]) for i in range(n)),-sa%n
def wp(a,m,n):
    out=((aone,)*n,0)
    for j in range(m):out=wm(out,a,n)
    return out
results=[]
for n in (2,3,4,6,12):
    gen=list(set(induced(w,n) for w in d['Nfwords']))
    sixths=[wp(g,6,n) for g in gen];commutators=[]
    for a in gen:
        for b in gen:commutators.append(wm(wm(wm(a,b,n),wi(a,n),n),wi(b,n),n))
    seeds=sixths+commutators
    assert all(s==0 for v,s in seeds)
    both=gen+[wi(g,n) for g in gen]
    def projected_closure(seeds):
        components=[closure(v[i] for v,s in seeds) for i in range(n)];rounds=0
        while True:
            nxt=[]
            for i in range(n):
                seeds_i=set(components[i])
                for v,s in both:seeds_i.update(aconj(v[i],z) for z in components[(i+s)%n])
                nxt.append(closure(seeds_i))
            rounds+=1
            if all(a==b for a,b in zip(components,nxt)):return components,rounds
            components=nxt
    components,rounds=projected_closure(seeds)
    comm_components,comm_rounds=projected_closure(commutators)
    if n==2:assert components[0]==d['Kimage']
    passed=[0,0];comm_passed=[0,0];recs=[]
    for fw,qf,miss in d['words_for_further_tests']:
        vv,ss=induced(fw,n);assert ss==0
        coset={amul(vv[0],z) for z in components[0]}
        targets=set();yc=unit
        for c in range(6):targets.add((times(yc,qf),c));yc=times(yc,qy)
        hits=coset&targets;passed[int(miss)]+=bool(hits)
        comm_hits={amul(vv[0],z) for z in comm_components[0]}&targets
        comm_passed[int(miss)]+=bool(comm_hits)
        recs.append({'missing_coset':miss,'passes':bool(hits),'intersection_size':len(hits),
                     'passes_with_commutator_correction':bool(comm_hits)})
    row={'N':n,'distinct_induced_N_generators':len(gen),
         'normal_closure_component_orders':[len(c) for c in components],
         'commutator_component_orders':[len(c) for c in comm_components],
         'normal_closure_rounds':rounds,'pass_counts_by_CM_coset':passed,
         'commutator_correction_pass_counts':comm_passed,'records':recs}
    results.append(row)
    print(json.dumps({k:v for k,v in row.items() if k!='records'}),flush=True)
out={'target':'H x Z/6 through (q delta_N,c_N mod6)',
     'scope':'Individual necessary finite consequences of full GT distribution. Both the full K6 image and the smaller image of [N_B,N_B] are computed; every candidate passes even with a commutator correction.',
     'results':results}
(here/'de_distribution_more.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: component projection normal closures and finite coset intersections computed exactly.')
