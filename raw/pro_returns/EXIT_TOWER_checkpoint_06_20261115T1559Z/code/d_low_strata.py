#!/usr/bin/env python3
"""Strata of depths 1,2,3 in five requested types, grouped by label permutation.
Uses the complete independent stable-graph lists of a_graphs.py.
"""
from collections import Counter
from itertools import permutations
from math import factorial
from pathlib import Path
import json
P=Path(__file__).resolve().parent

def signature(G):
    gen,legs,edges=G;v=len(gen);lc=Counter(legs)
    ans=[]
    for pp in permutations(range(v)):
        at={old:new for new,old in enumerate(pp)}
        ans.append((tuple(gen[i] for i in pp),tuple(lc[i] for i in pp),tuple(sorted(tuple(sorted((at[a],at[b]))) for a,b in edges))))
    return min(ans)

def autorder(G):
    gen,legs,edges=G;v=len(gen);ec=Counter(map(tuple,edges));a=0
    for pp in permutations(range(v)):
        if any(gen[pp[i]]!=gen[i] for i in range(v)):continue
        if any(pp[i]!=i for i in legs):continue
        if Counter(tuple(sorted((pp[x],pp[y]))) for x,y in edges)==ec:a+=1
    for (x,y),m in ec.items():a*=factorial(m)*(2**m if x==y else 1)
    return a

def run(g,n):
    D=json.loads((P/f'a_graphs_{g}_{n}.json').read_text());gg=D['graphs'];out=[]
    for q in range(1,min(3,3*g-3+n)+1):
        groups={}
        for i,G in enumerate(gg):
            if len(G[2])==q:groups.setdefault(signature(G),[]).append(i)
        for sig,indices in sorted(groups.items()):
            G=gg[indices[0]];gen,legs,edges=G;val=Counter(legs)+Counter(x for e in edges for x in e)
            ty=sorted((gen[i],val[i]) for i in range(len(gen)))
            out.append({'q':q,'orbit_size':len(indices),'genera':sig[0],'leg_counts':sig[1],'edges':sig[2],'component_types':ty,'aut_order':autorder(G),'graph_indices':indices})
    print(f'{(g,n)} depths: '+str({q:sum(r['orbit_size'] for r in out if r['q']==q) for q in range(1,min(3,3*g-3+n)+1)}))
    for r in out:print(json.dumps({k:r[k] for k in ('q','orbit_size','genera','leg_counts','edges','component_types','aut_order')}))
    return {'type':[g,n],'rows':out}
A=[run(g,n) for g,n in [(0,5),(0,6),(1,2),(1,3),(2,0)]]
(P/'d_low_strata.json').write_text(json.dumps(A,indent=2)+'\n')
tex=[]
for a in A:
    tex += [r'\paragraph{Type $('+','.join(map(str,a['type']))+r')$.}',r'\begin{longtable}{c|r|l|l|l|r}',r'$q$ & labelled number & genera; leg counts & edge multiset & cut types & $|\operatorname{Aut}G|$\\\hline']
    for r in a['rows']:
        gs=','.join(map(str,r['genera']));ls=','.join(map(str,r['leg_counts']));es=','.join(str(x)+str(y) for x,y in r['edges']);ty=','.join(f'({g},{n})' for g,n in r['component_types'])
        tex.append(f"{r['q']} & {r['orbit_size']} & $({gs});({ls})$ & $\\{{{es}\\}}$ & ${ty}$ & {r['aut_order']}"+r'\\')
    tex.append(r'\end{longtable}')
(P/'d_low_strata_table.tex').write_text('\n'.join(tex)+'\n')
