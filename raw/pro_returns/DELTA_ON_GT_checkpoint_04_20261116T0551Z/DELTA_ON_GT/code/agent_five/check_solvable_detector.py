"""Exact derived-series bounds for the finite CM frame detector.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_solvable_detector.py
"""
import json

def certificate(n, projective=False):
    I=(1,0,0,1)
    def canon(a):
        a=tuple(x%n for x in a)
        return min(a,tuple(-x%n for x in a)) if projective else a
    I=canon(I)
    def mul(a,b):
        return canon((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
    def inv(a):return canon((a[3],-a[1],-a[2],a[0]))
    def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
    def closure(gens):
        seen={I};todo=[I]
        while todo:
            a=todo.pop()
            for b in gens:
                c=mul(a,b)
                if c not in seen:seen.add(c);todo.append(c)
        return seen
    gens=[canon((1,1,0,1)),canon((1,0,-1,1))]
    H=closure(gens);sizes=[len(H)];minus=canon((-1,0,0,-1));minus_in=[]
    while len(H)>1:
        comms={comm(a,b)for a in H for b in gens}
        D=closure(comms)
        assert all(mul(mul(h,d),inv(h))in D for h in gens for d in D)
        sizes.append(len(D));minus_in.append(minus in D)
        H=D;gens=list(comms-{I})
    return {'modulus':n,'quotient_by_global_sign':projective,
            'derived_series_orders':sizes,
            'minus_identity_in_successive_derived_groups':minus_in}

results=[certificate(3),certificate(4),certificate(12,True)]
assert results[0]['derived_series_orders']==[24,8,2,1]
assert results[1]['derived_series_orders']==[48,12,4,1]
assert results[2]['derived_series_orders']==[576,96,8,1]
print(json.dumps({'group_certificates':results,
 'module_extension_derived_length_upper_bound':4,
 'characteristic_subdirect_product_derived_length_upper_bound':4,
 'multiplier_recording_quotient_B_over_FM_upper_bound':3,
 'scope':'The explicit normalized and outer finite detector of FP.23--29, including the existential finite multiplier table, can be chosen with solvable source quotient of derived length at most four. No minimality or full-image lifting assertion is made.'},indent=2))
