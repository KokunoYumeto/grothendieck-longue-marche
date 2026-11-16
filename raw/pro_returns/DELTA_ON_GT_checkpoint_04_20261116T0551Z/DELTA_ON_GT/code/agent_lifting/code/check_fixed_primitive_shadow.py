#!/usr/bin/env python3
"""Necessary finite primitive test for the corrected fixed-D locus.

No surviving residue is asserted to lift to a full gentle element.
"""
from check_descent_evaluations import *
from array import array

def main():
    G=sorted(generated([S,U]));gi={g:i for i,g in enumerate(G)};n=len(G)
    L=(1,0,11,1);X0=power(U,2);Y0=power(L,2)
    Fq=sorted(generated([X0,Y0]))
    aa=S;bb=inv(U);cc=inv(mul(aa,bb))
    pairs=[(aa,bb),(bb,cc),(cc,aa),(bb,aa),(cc,bb),(aa,cc)]
    set_blocks(7)
    K7=PermutationGroup([as_perm([a for a,b in pairs]+[X0]),
                         as_perm([b for a,b in pairs]+[Y0])])
    ker=[h for h in Fq if K7.contains(as_perm([I]*6+[h]))]
    assert len(ker)==8
    cosets=[];coset={}
    for h in Fq:
        if h in coset:continue
        members={mul(k,h)for k in ker};idx=len(cosets)
        cosets.append(sorted(members))
        for v in members:coset[v]=idx
    assert len(cosets)==12
    ctrans=[[coset[mul(g,C[0])]for C in cosets]for g in (X0,Y0)]
    trans=[]
    for flip in (False,True):
        line=[]
        for A,B in pairs[:3]:
            left,right=(B,inv(A))if not flip else(A,inv(B))
            line.append([gi[mul(mul(left,v),right)]for v in G])
        trans.append(line)
    def code(co,co7):return (((gi[co[0]]*n+gi[co[1]])*n+gi[co[2]])*12+co7)
    data=json.loads((Path(__file__).resolve().parents[1]/'records'/'descent_evaluations.json').read_text())
    goals={};results=[]
    for record in data['records']:
        C=tuple(record['C']);H=tuple(record['H']);B=mul(inv(H),inv(C));a=record['a_mod6']
        betaD=mul(power(U,2*a),C)
        if a%2:betaD=tuple(-v%12 for v in betaD)
        # Complex conjugation acts by diag(1,-1).
        beta=(betaD[0],-betaD[1]%12,-betaD[2]%12,betaD[3])
        assert beta in coset
        idx=len(results)
        results.append(dict(delta=record['delta'],C=C,H=H,a=a,beta=beta,passes=False))
        goals.setdefault(code([C,B,H],coset[beta]),[]).append(idx)
    identity=code([I]*3,coset[I]);seen={identity};queue=array('Q',[identity]);head=0
    print('Seven-evaluation group',K7.order(),'kernel over six',len(ker),flush=True)
    print('Corrected fixed-frame targets',len(results),'distinct states',len(goals),flush=True)
    while head<len(queue) and goals:
        value=queue[head];head+=1
        if value in goals:
            for idx in goals.pop(value):results[idx]['passes']=True
        c=value%12;value//=12;h=value%n;value//=n;b=value%n;a=value//n
        for t in range(2):
            nxt=((trans[t][0][a]*n+trans[t][1][b])*n+trans[t][2][h])*12+ctrans[t][c]
            if nxt not in seen:seen.add(nxt);queue.append(nxt)
    counts=Counter((r['delta'],r['passes'])for r in results)
    print('Primitive orbit states examined',head,'discovered',len(seen),flush=True)
    print('Counts by (Delta,passes)',dict(counts),flush=True)
    out=dict(scope='necessary finite primitive test only; no full lift asserted',
             group_order=int(K7.order()),kernel_order=len(ker),
             examined=head,discovered=len(seen),orbit_exhausted=head==len(queue),
             all_targets_found=not goals,results=results)
    (Path(__file__).resolve().parents[1]/'records'/'fixed_primitive_shadow.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
