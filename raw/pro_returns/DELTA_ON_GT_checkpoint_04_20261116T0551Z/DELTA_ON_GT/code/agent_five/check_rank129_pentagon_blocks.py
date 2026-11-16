"""Exact four-dimensional character equations for the rank129 pentagon.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import numpy as np,json
ROOT=Path(__file__).resolve().parent
F=np.load(ROOT/'ferrari_rank129_blocks.npz');D=np.load(ROOT/'ferrari_rank129_boundary.npz')
perms=F['x_permutations'];offset=F['offsets'];ranks=D['boundary_ranks'];basechar=1
def orbit(ii,jj):
    seen={basechar};todo=[basechar]
    for m in todo:
        for p in (perms[ii],perms[jj]):
            r=int(p[m])
            if r not in seen:seen.add(r);todo.append(r)
    return sorted(seen)
def m2(a,b):
    aa,bb,cc,dd=a;e,f,g,h=b
    return((aa*e+bb*g)%3,(aa*f+bb*h)%3,(cc*e+dd*g)%3,(cc*f+dd*h)%3)
def i2(a):
    aa,b,c,d=a;z=(aa*d-b*c)%3
    return(z*d%3,-z*b%3,-z*c%3,z*aa%3)
reports=[]
for ii,jj in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    orb=orbit(ii,jj);n=len(orb);I=tuple(range(n))+(1,0,0,1)*n
    assert all(ranks[m]==2 for m in orb)
    def mul(g,h):
        p,q=g[:n],h[:n];z=[]
        for j in range(n):z.extend(m2(g[n+4*q[j]:n+4*q[j]+4],h[n+4*j:n+4*j+4]))
        return tuple(p[q[j]]for j in range(n))+tuple(z)
    def inv(g):
        p=g[:n];q=tuple(p.index(j)for j in range(n));z=[]
        for j in range(n):z.extend(i2(g[n+4*q[j]:n+4*q[j]+4]))
        return q+tuple(z)
    def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
    def closure(gens):
        G=[I];seen={I}
        for g in G:
            for h in gens:
                z=mul(g,h)
                if z not in seen:seen.add(z);G.append(z)
            if len(G)>100000:raise RuntimeError('Stop: unexpectedly large block image')
        return G
    boundary_gens=[];proper_gens=[]
    for k in (ii,jj):
        p=[];B=[];P=[]
        for m in orb:
            r=int(perms[k,m]);p.append(orb.index(r));a,b=offset[m];c,d=offset[r]
            block=D['X'][k,c:d,a:b]
            assert not np.any(block[2:,:2])
            B.extend(map(int,block[:2,:2].ravel()));P.extend(map(int,block[2:,2:].ravel()))
        boundary_gens.append(tuple(p)+tuple(B));proper_gens.append(tuple(p)+tuple(P))
    H=closure(boundary_gens);lower=[len(H)];K=H
    while len(K)>1:
        cg=list({comm(k,h)for k in K for h in boundary_gens});K=closure(cg);lower.append(len(K))
        if len(lower)>10:break
    P=closure(proper_gens);derived=[len(P)];gg=proper_gens
    while len(P)>1:
        gg=list({comm(k,h)for k in P for h in gg});P=closure(gg);derived.append(len(P))
        if len(derived)>8:break
    reports.append({'pair':[ii+1,jj+1],'character_orbit':orb,
                    'boundary_lower_central_series':lower,
                    'proper_derived_series':derived,
                    'boundary_killed_by_all_gentle_H_f':len(lower)<=3,
                    'boundary_generators':boundary_gens,'proper_generators':proper_gens})
print(json.dumps({'fixed_character':basechar,'pentagon_factor_order':[[3,4],[5,1],[2,3],[4,5],[1,2]],
 'pair_block_reports':reports,
 'typed_equation':'For each factor write its invariant-character block as [[B_i,C_i],[0,P_i]]. The pentagon requires product(B_i)=I, product(P_i)=I, and sum_i (B_1...B_{i-1}) C_i (P_{i+1}...P_5)=0.',
 'scope':'These are literal same-word f-evaluations. No independence of factors or GT lifting of arbitrary block values is assumed.'},indent=2))
