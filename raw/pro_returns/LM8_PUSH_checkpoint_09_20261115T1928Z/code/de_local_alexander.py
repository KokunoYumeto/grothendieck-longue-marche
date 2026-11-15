#!/usr/bin/env python3
"""Finite exact checks of the affine orbit calculations used in D.42--D.43."""
from pathlib import Path
from fractions import Fraction
import json

def valuation(n):
    if n==0:
        return None
    a=0
    while n%5==0:
        n//=5
        a+=1
    return a

def orbit_lengths(Q,b,m):
    modulus=5**m
    seen=bytearray(modulus)
    lengths=[]
    for z in range(modulus):
        if seen[z]:
            continue
        x=z;length=0
        while not seen[x]:
            seen[x]=1;length+=1
            x=(Q*x+b)%modulus
        assert x==z
        lengths.append(length)
    return lengths

rows=[]
for Q,b in [(2,0),(11,0),(11,10),(11,1),(101,5)]:
    for m in range(1,7):
        lengths=orbit_lengths(Q,b,m)
        counts={str(n):lengths.count(n) for n in sorted(set(lengths))}
        if Q==11 and b==1:
            assert lengths==[5**m]
        if Q==101 and b==5:
            assert len(lengths)==5 and set(lengths)=={5**(m-1)}
        if Q==2 and b==0:
            assert sorted(lengths)==sorted([1]+[4*5**j for j in range(m)])
        rows.append({"Q":Q,"b":b,"modulus":5**m,"cycle_lengths":counts})

# Necessary boundedness obstruction on the identity component.
# A formal solution with augmentation alpha is alpha*t^(-b/(Q-1)).
examples=[]
for Q,b,alpha in [(11,1,5),(11,1,25),(101,1,25),(101,5,25)]:
    z=Fraction(-b,Q-1)
    coeff=Fraction(alpha)
    seq=[]
    first=None
    for n in range(1,8):
        coeff*=Fraction(z-(n-1),n)
        v=valuation(coeff.numerator)-valuation(coeff.denominator)
        seq.append({"degree":n,"coefficient":str(coeff),"v5":v})
        if first is None and v<0:
            first=n+1
    examples.append({"Q":Q,"b":b,"alpha":alpha,
                     "first_nonintegral_forced_weight":first,
                     "scope":"Necessary upper bound on a lifting stage, not a claim that every earlier full stage lifts.",
                     "coefficients":seq})
assert examples[0]["first_nonintegral_forced_weight"]==3
out={"status":"all exact affine-orbit checks passed","orbits":rows,
     "forced_integrality_examples":examples,
     "theorem_scope":"Finite checks illustrate the separately proved bounded-measure and compact cohomology arguments."}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
