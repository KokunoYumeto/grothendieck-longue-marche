#!/usr/bin/env python3
"""Exact finite matrix implication using the 18 retained CM centralizer residues.

The geometric finite square and the centralizer lifting census are proved
separately. This checks their final signed matrix consequence, for both
integral CM marking signs, without replacing the two residues by one exponent.
"""
from itertools import product
from collections import Counter
from pathlib import Path
import json

I=(1,0,0,1);R=(0,-1,1,1);Rp=(0,1,-1,1);S=(0,1,-1,0)
def red(a,n):return tuple(v%n for v in a)
def mm(a,b,n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n
                 for i in range(2) for j in range(2))
def power(a,k,n):
    z=I
    for _ in range(k%6):z=mm(z,a,n)
    return z
def crt(a3,a4):
    return tuple(next(k for k in range(12) if k%3==a%3 and k%4==b%4)
                 for a,b in zip(a3,a4))
def mv(a,v,n):return ((a[0]*v[0]+a[1]*v[1])%n,(a[2]*v[0]+a[3]*v[1])%n)
def cartan(a,n):
    return sorted(g for g in product(range(n),repeat=4)
                  if (g[0]*g[3]-g[1]*g[2])%n==1 and mm(g,a,n)==mm(a,g,n))
c3=cartan(Rp,3);c4=cartan(Rp,4);s3=cartan(S,3)
assert set(c3)=={power(Rp,j,3) for j in range(6)}
assert set(c4)=={power(Rp,i,4) for i in range(6)}
assert len(s3)==4
centralizer_residues=[{'i':i,'j':j,'matrix':crt(power(Rp,j,3),power(Rp,i,4))}
                      for i in range(6) for j in range(6) if i%2==j%2]
assert len({tuple(v['matrix']) for v in centralizer_residues})==18
Ts=[crt(t,I) for t in c3];Ws=[crt(w,I) for w in s3]
N3=tuple((a+b)%3 for a,b in zip(R,I))
assert mm(N3,N3,3)==(0,0,0,0)
M3s=[tuple((a+c*b)%3 for a,b in zip(I,N3)) for c in range(3)]
markings={-1:(1,0,1,1),1:(1,0,0,-1)}
records=[];counts=Counter()
for sign,C in markings.items():
    assert mm(C,R,12)==mm(power(Rp,sign,12),C,12)
    for T in Ts:
        tv=mv(T,(1,2),3);assert tv in ((1,2),(2,1))
        bit3=int(tv==(2,1))
        for W in Ws:
            sw=I;exponent=None
            for k in range(4):
                if sw==red(W,3):exponent=k
                sw=mm(sw,S,3)
            assert exponent is not None
            bit2=exponent%2
            solutions=[]
            for m3 in M3s:
                for ell in (0,2,4):
                    m4=power(R,ell+3*bit2,4);M=crt(m3,m4)
                    for q in centralizer_residues:
                        i,j=q['i'],q['j']
                        pass4=mm(T,C,4)==mm(mm(power(Rp,i,4),C,4),M,4)
                        pass3=mm(T,C,3)==mm(mm(power(Rp,j,3),C,3),M,3)
                        if pass4 and pass3:
                            assert bit2==i%2 and bit3==j%2 and bit2==bit3
                            solutions.append({'M':M,'i':i,'j':j,'source_even_exponent':ell})
            assert bool(solutions)==(bit2==bit3)
            counts[(sign,bit3,bit2,len(solutions))]+=1
            records.append({'marking_sign':sign,'C':C,'T':T,'W':W,
                            'cubic_bit':bit3,'harmonic_bit':bit2,'solutions':solutions})
out={'scope':'Exact paired-exponent finite CM parity implication; no independent claim of geometric covariance or genuine-source enumeration.',
     'centralizer_residue_count':18,'marking_signs':[-1,1],
     'matrix_pairs':len(records),'residues':centralizer_residues,'records':records,
     'counts':[{'sign':k[0],'cubic_bit':k[1],'harmonic_bit':k[2],
                'solutions':k[3],'pairs':v} for k,v in sorted(counts.items())],
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS both signed CM markings; 18 coupled centralizer residues; 48 signed frame pairs.')
for k,v in sorted(counts.items()):print('sign,cubic,harmonic,solutions',k,'pairs',v)
print('PASS the two finite matrix equations force equal CM parities in every retained case.')
