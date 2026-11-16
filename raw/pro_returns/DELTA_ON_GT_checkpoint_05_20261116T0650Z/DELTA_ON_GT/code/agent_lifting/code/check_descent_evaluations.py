#!/usr/bin/env python3
"""Exact common-word membership for six orbifold evaluations modulo12.

This tests necessary finite conditions. Survivors are not asserted to lift.
"""
from itertools import product
from collections import Counter
from sympy.combinatorics import Permutation, PermutationGroup
import json
from pathlib import Path

I=(1,0,0,1)
S=(0,1,11,0)
R=(0,11,1,11)
U=(1,1,0,1)

def mul(a,b,n=12):
    return tuple((a[2*i]*b[j]+a[2*i+1]*b[2+j])%n
                 for i in range(2) for j in range(2))
def inv(a,n=12):
    return(a[3],-a[1]%n,-a[2]%n,a[0])
def power(a,k,n=12):
    if k<0:return power(inv(a,n),-k,n)
    out=I
    for _ in range(k):out=mul(out,a,n)
    return out
def generated(gs):
    h={I};todo=[I]
    for a in todo:
        for g in gs:
            b=mul(a,g)
            if b not in h:h.add(b);todo.append(b)
    return h
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def red(a,n):return tuple(v%n for v in a)
def projective(a):return min(a,tuple(-v%12 for v in a))

blocks=[]
def set_blocks(count):
    blocks.clear()
    for n in (3,4):
        vectors=[(x,y) for x,y in product(range(n),repeat=2)
                 if (x,y)!=(0,0) and (n!=4 or x%2 or y%2)]
        index={v:i for i,v in enumerate(vectors)}
        for coord in range(count):blocks.append((n,coord,vectors,index))

def as_perm(coords):
    arr=[];offset=0
    for n,c,vectors,index in blocks:
        a,b,c0,d=coords[c]
        arr.extend(offset+index[((a*x+b*y)%n,(c0*x+d*y)%n)]
                   for x,y in vectors)
        offset+=len(vectors)
    return Permutation(arr)

def main():
    G=generated([S,U]);c=comm(S,U)
    Gprime=sorted(generated([mul(mul(g,c),inv(g)) for g in G]))
    print('SL2(Z/12) order',len(G),'derived order',len(Gprime),flush=True)
    aa=S;bb=inv(U);cc=inv(mul(aa,bb))
    pairs=[(aa,bb),(bb,cc),(cc,aa),(bb,aa),(cc,bb),(aa,cc)]
    set_blocks(6)
    X=as_perm([a for a,b in pairs]);Y=as_perm([b for a,b in pairs])
    K=PermutationGroup([X,Y])
    print('Six-evaluation group order',K.order(),flush=True)
    D=K.derived_subgroup()
    print('Six-evaluation derived order',D.order(),flush=True)
    # For every component, express the other two arguments in its cyclic
    # equation as a simultaneous conjugate of one of the six pairs.
    # Signs of individual arguments do not affect a commutator word.
    def lookup(A,B):
        for j,(a,b)in enumerate(pairs):
            for M in sorted(G):
                Mi=inv(M)
                if (projective(mul(mul(M,a),Mi))==projective(A)
                    and projective(mul(mul(M,b),Mi))==projective(B)):
                    return j,M
        raise AssertionError(('missing conjugacy lookup',A,B))
    cycle_lookups=[]
    for A,B in pairs:
        Z=inv(mul(A,B))
        cycle_lookups.append((lookup(Z,A),lookup(B,Z)))
    Rs=[red(power(R,j),2)for j in range(3)]
    Ss=[red(power(S,j),3)for j in range(4)]
    C4=[red(I,4),red(tuple(-x%12 for x in power(U,2)),4)]
    signs=[red(I,3),red(power(S,2),3)]
    counts=Counter();records=[]
    for C,H in product(Gprime,repeat=2):
        if red(C,2)!=red(I,2) or red(C,4)not in C4:continue
        a2=C4.index(red(C,4))
        if red(C,3)not in Ss:continue
        j=Ss.index(red(C,3));CH=mul(C,H)
        if red(CH,3)not in signs or red(H,2)not in Rs:continue
        bit=signs.index(red(CH,3));l=Rs.index(red(H,2))
        a=next(k for k in range(6)if k%2==a2 and k%3==l)
        A=mul(mul(mul(power(U,2*a),C),H),power(R,-l))
        if a%2:A=tuple(-v%12 for v in A)
        if red(A,4)!=red(I,4):continue
        lhs=mul(S,mul(mul(H,R),inv(H)))
        rhs=mul(mul(inv(C),mul(S,R)),C)
        if projective(lhs)!=projective(rhs):continue
        delta=(a2+bit+j)%2
        counts[f'raw_delta_{delta}']+=1
        B=mul(inv(H),inv(C))
        coords=[C,B,H,inv(C),inv(B),inv(H)]
        if not D.contains(as_perm(coords)):continue
        counts[f'common_word_delta_{delta}']+=1
        def value(t):
            j,M=t
            return mul(mul(M,coords[j]),inv(M))
        if not all(mul(mul(value(ts[0]),value(ts[1])),v)==I
                   for ts,v in zip(cycle_lookups,coords)):continue
        counts[f'all_cycles_delta_{delta}']+=1
        records.append(dict(C=C,H=H,a_mod6=a,l=l,
                            C_exponent_mod4=j,CH_sign=bit,delta=delta))
    six_order=int(K.order());six_derived=int(D.order())
    # Add the original inclusion j(x)=U^2,j(y)=L^2. At a fixed point,
    # R3 and rho_D congruent to a modulo3 give the indicated last value.
    L=(1,0,11,1)
    pairs7=pairs+[(power(U,2),power(L,2))]
    set_blocks(7)
    K7=PermutationGroup([as_perm([a for a,b in pairs7]),
                         as_perm([b for a,b in pairs7])])
    D7=K7.derived_subgroup()
    print('Seven-evaluation group order',K7.order(),flush=True)
    print('Seven-evaluation derived order',D7.order(),flush=True)
    for record in records:
        C=tuple(record['C']);H=tuple(record['H']);a=record['a_mod6']
        B=mul(inv(H),inv(C))
        f_original=(1,-8*a%12,-8*a%12,(1+64*a*a)%12)
        coords=[C,B,H,inv(C),inv(B),inv(H),f_original]
        record['passes_fixed_original_evaluation']=D7.contains(as_perm(coords))
        record['original_f']=f_original
        if record['passes_fixed_original_evaluation']:
            counts[f'fixed_original_delta_{record["delta"]}']+=1
        # For the corrected old fixed locus D_P(Phi)=c Phi c, the source
        # rho has the opposite sign: rho_original=-a modulo3.
        twisted_f=(1,8*a%12,8*a%12,(1+64*a*a)%12)
        twisted_coords=coords[:-1]+[twisted_f]
        record['passes_twisted_fixed_evaluation']=D7.contains(as_perm(twisted_coords))
        record['twisted_original_f']=twisted_f
        if record['passes_twisted_fixed_evaluation']:
            counts[f'twisted_fixed_delta_{record["delta"]}']+=1
    print(json.dumps(dict(counts),sort_keys=True),flush=True)
    print('First survivor of each parity:',flush=True)
    for bit in (0,1):
        print(bit,next((r for r in records if r['delta']==bit),None),flush=True)
    out=dict(group_order=six_order,derived_order=six_derived,
             seven_group_order=int(K7.order()),
             seven_derived_order=int(D7.order()),
             cycle_lookups=cycle_lookups,counts=dict(counts),records=records)
    path=Path(__file__).resolve().parents[1]/'records'/'descent_evaluations.json'
    path.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
