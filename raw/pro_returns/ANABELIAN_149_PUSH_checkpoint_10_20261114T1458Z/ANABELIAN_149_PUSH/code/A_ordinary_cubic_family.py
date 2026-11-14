#!/usr/bin/env python3
"""Exact Frobenius survey of the order-three ordinary-elliptic auxiliaries over F16.

This is a finite survey, not a universal classification.  All fields, counts,
Newton identities, and determinants are exact.  The positive valuation test
is proved in audit/A_ordinary_auxiliary_packet.md.
"""
import json
from pathlib import Path
from A_ordinary_elliptic_obstruction import BinaryField
from A_genus4_prym_experiment import determinant_bareiss, matrix_mul


def valuation(n):
    assert n
    v=0
    while n%2==0:
        n//=2
        v+=1
    return v


def setup(d, modulus):
    k=BinaryField(d,modulus)
    root=next(z for z in range(k.q) if k.power(z,4)^z^1==0)
    powers=[k.power(root,i) for i in range(4)]
    embedding=[]
    for z in range(16):
        v=0
        for i in range(4):
            if (z>>i)&1: v^=powers[i]
        embedding.append(v)
    assert len(set(embedding))==16
    assert all(k.power(z,16)==z for z in embedding)
    inverses=[0]+[k.power(z,k.q-2) for z in range(1,k.q)]
    as_counts=[0]*k.q
    for y in range(k.q): as_counts[k.mul(y,y)^y]+=1
    assert set(as_counts)=={0,2}
    assert all(as_counts[z]==2*(1-k.trace(z)) for z in range(k.q))
    cubes=[k.power(z,3) for z in range(k.q)]
    return k,embedding,inverses,as_counts,cubes


def main():
    base=BinaryField(4,0x13)
    parameters=[]
    for b in range(2,16):
        a=base.power(base.mul(base.power(b,3),b^1),8)
        assert a and base.mul(a,a)==base.power(b,4)^base.power(b,3)
        parameters.append({'b_F16':b,'a_F16':a,'counts':[]})
    for d,mod in ((4,0x13),(8,0x11b),(12,0x1009)):
        k,emb,inv,asc,cubes=setup(d,mod)
        for row in parameters:
            a,b=emb[row['a_F16']],emb[row['b_F16']]
            e_count=2+sum(asc[x^k.mul(a,inv[x])] for x in range(1,k.q))
            count=1
            for cube in cubes:
                h=cube^b
                count+=1 if not h else asc[h^k.mul(a,inv[h])]
            row['counts'].append({'degree_over_F16':d//4,'E':e_count,'B':count})
    for row in parameters:
        sums=[r['E']-r['B'] for r in row['counts']]
        coeff=[1]
        for j in range(1,4):
            numerator=-sum(coeff[j-i]*sums[i-1] for i in range(1,j+1))
            assert numerator%j==0
            coeff.append(numerator//j)
        coeff += [16*coeff[2],16**2*coeff[1],16**3]
        row['prym_polynomial_high_to_low']=coeff
        low=list(reversed(coeff))
        companion=[[0]*6 for _ in range(6)]
        for i in range(5): companion[i+1][i]=1
        for i in range(6): companion[i][5]=-low[i]
        power=[[int(i==j) for j in range(6)] for i in range(6)]
        orders={}
        for n in range(1,7):
            power=matrix_mul(power,companion)
            order=determinant_bareiss([[power[i][j]-int(i==j) for j in range(6)] for i in range(6)])
            assert order>0
            orders[str(n)]={'order':order,'v2':valuation(order)}
        row['prym_orders']=orders
        row['proved_packet_weierstrass_by_valuation']=any(v['v2']==4 for v in orders.values())
    result={'scope':'All14 nonzero b!=1 over F16, a^2=b^3(b+1); exact order-three branch pair',
            'parameters':parameters,'positive_valuation_cases':[r['b_F16'] for r in parameters if r['proved_packet_weierstrass_by_valuation']],
            'all_passed':True}
    out=json.dumps(result,indent=2,sort_keys=True)+'\n'
    Path(__file__).with_suffix('.json').write_text(out)
    print(out,end='')


if __name__=='__main__': main()
