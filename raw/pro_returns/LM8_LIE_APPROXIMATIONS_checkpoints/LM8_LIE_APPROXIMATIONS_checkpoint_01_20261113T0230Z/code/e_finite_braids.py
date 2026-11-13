"""Finite B3-action audit on all SL2(Z/n) of order <=1000.

We enumerate all lambda in (Z/exponent(G))* and f in the derived subgroup
of <A^2,B^2>, then test both the braid relation and descent to an
automorphism of the PARTICULAR quotient G.  These are finite candidates,
not certified GT-shadows: no arity-four pentagon is silently assumed.
All cyclic quotients C_n, n<=1000, are handled separately and exhaustively.
"""
from collections import deque,Counter
from itertools import product
from math import gcd,lcm
from pathlib import Path
import json,time

def audit(n):
    def mul(a,b):
        x,y,z,w=a;X,Y,Z,W=b
        return ((x*X+y*Z)%n,(x*Y+y*W)%n,(z*X+w*Z)%n,(z*Y+w*W)%n)
    def inv(a):x,y,z,w=a;return (w%n,-y%n,-z%n,x%n)
    I=(1,0,0,1);A=(1,1,0,1);B=(1,0,n-1,1)
    elems=sorted(a for a in product(range(n),repeat=4) if (a[0]*a[3]-a[1]*a[2])%n==1)
    if len(elems)>1000:return None
    ix={a:i for i,a in enumerate(elems)};N=len(elems);ii=ix[I]
    # Full multiplication table makes all later checks finite table lookups.
    table=[[ix[mul(a,b)] for b in elems] for a in elems]
    inverses=[ix[inv(a)] for a in elems]
    a,b=ix[A],ix[B]
    def power(x,k):
        if k<0:x=inverses[x];k=-k
        y=ii
        while k:
            if k&1:y=table[y][x]
            x=table[x][x];k>>=1
        return y
    def closure(gens):
        S={ii};q=deque([ii])
        while q:
            v=q.popleft()
            for g in gens:
                w=table[v][g]
                if w not in S:S.add(w);q.append(w)
        return S
    assert len(closure([a,b]))==N
    exponent=1
    for x in range(N):
        y=x;k=1
        while y!=ii:y=table[y][x];k+=1
        exponent=lcm(exponent,k)
    x,y=power(a,2),power(b,2);H=closure([x,y])
    c=table[table[table[x][y]][inverses[x]]][inverses[y]]
    conjugates={table[table[h][c]][inverses[h]] for h in H}
    derived=sorted(closure(list(conjugates)))
    # Fixed spanning tree and all two-generator Cayley edges certify descent.
    tree=[];seen={ii};q=deque([ii])
    while q:
        v=q.popleft()
        for genidx,g in enumerate([a,b]):
            w=table[v][g]
            if w not in seen:seen.add(w);q.append(w);tree.append((v,genidx,w))
    def is_auto(ap,bp):
        imgs=[-1]*N;imgs[ii]=ii;gs=[ap,bp]
        for v,k,w in tree:imgs[w]=table[imgs[v]][gs[k]]
        if len(set(imgs))!=N:return False
        return all(imgs[table[v][g]]==table[imgs[v]][gs[k]] for v in range(N) for k,g in enumerate([a,b]))
    bylambda=[];total_braid=total_auto=0
    for lam in range(exponent):
        if gcd(lam,exponent)!=1:continue
        ap=power(a,lam);bl=power(b,lam);cb=ca=0
        for f in derived:
            bp=table[table[inverses[f]][bl]][f]
            if table[table[ap][bp]][ap]!=table[table[bp][ap]][bp]:continue
            cb+=1
            if is_auto(ap,bp):ca+=1
        total_braid+=cb;total_auto+=ca
        bylambda.append([lam,cb,ca])
    tate_checks=0
    for lam in [1,exponent-1]:
        for k in range(n):
            q8=power(a,-8*k)
            ap=power(a,lam);bp=table[table[q8][power(b,lam)]][inverses[q8]]
            assert is_auto(ap,bp)
            tate_checks+=1
    return {'modulus':n,'order':N,'exponent':exponent,'pure_image_order':len(H),
      'pure_derived_order':len(derived),'candidate_pairs':len(bylambda)*len(derived),
      'braid_solutions':total_braid,'quotient_automorphism_solutions':total_auto,
      'counts_by_lambda':[{'lambda':l,'braid':c,'automorphism':d} for l,c,d in bylambda],
      'identity_complex_conjugation_Tate_checks':tate_checks}

def main():
    start=time.time();rows=[]
    for n in range(2,12):
        row=audit(n)
        if row:
            rows.append(row);print({k:v for k,v in row.items() if k!='counts_by_lambda'},flush=True)
    # In C_n both Artin generators have the same image; all f vanish.
    cyc=[]
    for n in range(1,1001):
        units=[l for l in range(n) if gcd(l,n)==1]
        assert all(len({l*x%n for x in range(n)})==n for l in units)
        cyc.append({'order':n,'automorphisms':len(units)})
    out={'scope':'all cyclic B3 quotients of orders 1..1000 and all SL2(Z/n) of order <=1000; not every finite quotient',
        'congruence':rows,'cyclic':cyc,'cyclic_action_count':sum(r['automorphisms'] for r in cyc),
        'seconds':round(time.time()-start,3)}
    Path(__file__).with_name('e_finite_braids.json').write_text(json.dumps(out,indent=2)+'\n')
    print('cyclic',len(cyc),'actions',out['cyclic_action_count'],'seconds',out['seconds'])
if __name__=='__main__':main()
