#!/usr/bin/env python3
"""Direct fixed polynomial certificate; no search, jets, C, or Jacobian imports."""
from pathlib import Path
import json,hashlib,time

ROOT=Path(__file__).parent

class BinaryField:
    def __init__(self,e,mod,gen):
        self.q=1<<e;self.mod=mod;self.e=e
        seen=set();x=1
        for _ in range(self.q-1):
            assert x and x not in seen;seen.add(x);x=self.mul(x,gen)
        assert x==1 and len(seen)==self.q-1
    def mul(self,a,b):
        c=0
        while b:
            if b&1:c^=a
            a<<=1
            if a&self.q:a^=self.mod
            b>>=1
        return c
    def power(self,a,n):
        c=1
        while n:
            if n&1:c=self.mul(c,a)
            a=self.mul(a,a);n>>=1
        return c
    def inv(self,a):assert a;return self.power(a,self.q-2)

def trim(a):
    a=a[:]
    while a and not a[-1]:a.pop()
    return a
def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]^=x
    for i,x in enumerate(b):c[i]^=x
    return trim(c)
def multiply(a,b,F):
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]^=F.mul(x,y)
    return trim(c)
def evaluate(a,x,F):
    c=0
    for v in reversed(a):c=F.mul(c,x)^v
    return c

def main():
    start=time.time();path=ROOT/'A_F4_rank_one_witnesses.json';data=json.loads(path.read_text());out=[];covered=set()
    for r in data['witnesses']:
        F=BinaryField(r['field_degree_over_F2'],r['field_modulus'],r['field_generator'])
        alpha=r['alpha'];assert F.mul(alpha,alpha)^alpha==1
        vals=[0,1,alpha,F.mul(alpha,alpha)];key=tuple(r['F4_coefficients']);ac,bc=r['A'],r['B'];assert [ac,bc]==[vals[i] for i in key]
        t,y=r['point'];assert t and F.mul(y,y)^y==F.mul(ac,F.power(t,3))^F.mul(bc,t)^F.inv(t)
        n=r['exact_order'];d=(n-1)//2;assert n>1 and n%2
        a,b,c=r['numerator_A'],r['numerator_B'],r['norm_scalar'];assert len(a)<=d+1 and len(b)<=d-1 and c
        left=add(multiply([0,1],add(multiply(a,a,F),multiply(a,b,F)),F),multiply(multiply(b,b,F),[1,0,bc,0,ac],F))
        right=[c]
        for _ in range(n):right=multiply(right,[t,1],F)
        assert left==right
        assert evaluate(a,t,F)^F.mul(evaluate(b,t,F),y)==0
        assert evaluate(b,t,F) and evaluate(b,0,F)
        units={i for i in range(1,n) if __import__('math').gcd(i,n)==1};generated=set();j=1
        while j not in generated:
            generated.add(j);j=2*j%n
        generated|={(-j)%n for j in generated};assert generated==units
        conjugation={0:0,1:1,2:3,3:2};covered.add(key);covered.add(tuple(conjugation[x] for x in key))
        out.append({'F4_coefficients':key,'field_size':F.q,'annihilator':n,
                    'point':[t,y],'full_norm_identity':True,'sole_zero_and_pole_local_conditions':True,
                    'doubling_and_sign_generate_all_units':True})
    assert covered=={(a,b) for a in (1,2,3) for b in range(4)}
    result={'status':'PASS','fixed_witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'records':out,'geometric_F4_classes_covered':len(covered),
            'scope':'Exact norm identities prove nonzero odd theta torsion; A.C2.19 supplies the A1 implication after classification review.',
            'runtime_seconds':time.time()-start}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
