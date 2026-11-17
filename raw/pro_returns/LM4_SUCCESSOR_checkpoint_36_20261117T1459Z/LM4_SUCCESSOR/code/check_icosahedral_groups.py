"""Exact finite checks for characteristic A5 quotient and binary cover."""
from itertools import product,permutations,combinations
from collections import Counter
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup,coset_enumeration_r
from pathlib import Path
import csv

def mul(a,b):
    A,B,C,D=a;E,F,G,H=b
    return ((A*E+B*G)%5,(A*F+B*H)%5,(C*E+D*G)%5,(C*F+D*H)%5)
I=(1,0,0,1)
def neg(a):return tuple(-x%5 for x in a)
def inv(a):
    A,B,C,D=a;return (D,-B%5,-C%5,A)
def psl(a):return min(a,neg(a))
def pmul(a,b):return psl(mul(a,b))
def closure(gens,operation,identity):
    ans={identity};todo=[identity]
    while todo:
        a=todo.pop()
        for b in gens:
            c=operation(a,b)
            if c not in ans:ans.add(c);todo.append(c)
    return ans
def order(a,operation,identity):
    b=a;k=1
    while b!=identity:b=operation(b,a);k+=1
    return k
def conjugate(a,b):return pmul(pmul(b,a),psl(inv(b)))

def main():
    SL={a for a in product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5==1}
    A={psl(a) for a in SL};e=psl(I)
    assert len(SL)==120 and len(A)==60
    s=(0,4,1,0);r=(0,4,1,1)
    assert closure([s,r],mul,I)==SL
    a=mul(s,r);b=inv(r);z=neg(I)
    assert order(a,mul,I)==10 and order(b,mul,I)==6
    def power(a,k):
        v=I
        for _ in range(k):v=mul(v,a)
        return v
    assert power(a,5)==power(b,3)==power(mul(a,b),2)==z
    print('SL(2,F5) order:',len(SL),'PSL(2,F5) order:',len(A))
    print('Binary generators a,b:',a,b)
    print('a^5=b^3=(ab)^2=-I: PASS')
    invol=[a for a in A if order(a,pmul,e)==2]
    cubic=[a for a in A if order(a,pmul,e)==3]
    counts=Counter()
    for a in invol:
        for b in cubic:
            H=closure([a,b],pmul,e)
            counts[(len(H),order(pmul(a,b),pmul,e))]+=1
    print('(generated subgroup order,product order):pair count',dict(sorted(counts.items())))
    assert all(o==5 for (size,o) in counts if size==60)
    assert counts[(60,5)]==120
    F,S,R=free_group('s,r')
    triangle=FpGroup(F,[S**2,R**3,(S*R)**5])
    ct=coset_enumeration_r(triangle,[],max_cosets=10000)
    ct.compress();ct.standardize()
    assert len(ct.table)==60
    print('Todd-Coxeter order <s,r|s^2,r^3,(sr)^5>:',len(ct.table))
    F,X,Y=free_group('a,b')
    binary=FpGroup(F,[X**5*Y**-3,Y**3*(X*Y)**-2])
    cb=coset_enumeration_r(binary,[],max_cosets=20000)
    cb.compress();cb.standardize()
    assert len(cb.table)==120
    print('Todd-Coxeter order <a,b|a^5b^-3,b^3(ab)^-2>:',len(cb.table))
    out=Path(__file__).resolve().parents[1]/'data';out.mkdir(exist_ok=True)
    for name,table in [('triangle_235_cosets.csv',ct.table),('binary_icosahedral_cosets.csv',cb.table)]:
        with (out/name).open('w',newline='') as f:
            wr=csv.writer(f);wr.writerow(['coset','a','a_inverse','b','b_inverse'])
            for i,row in enumerate(table):wr.writerow([i]+row)
    # Action on twelve cosets of a subgroup of order5.
    C5=closure([psl(mul(s,r))],pmul,e)
    assert len(C5)==5
    cosets=[];remaining=set(A)
    while remaining:
        x=min(remaining)
        C=frozenset(pmul(x,h) for h in C5)
        cosets.append(C);remaining-=C
    index={x:i for i,C in enumerate(cosets) for x in C}
    reps=[min(C) for C in cosets]
    acts={g:tuple(index[pmul(g,x)] for x in reps) for g in A}
    pairs=set(combinations(range(12),2));orbits=[]
    while pairs:
        v=min(pairs)
        O={tuple(sorted((p[v[0]],p[v[1]]))) for p in acts.values()}
        orbits.append(O);pairs-=O
    print('A5 pair-orbit sizes on12 vertices:',sorted(map(len,orbits)))
    assert sorted(map(len,orbits))==[6,30,30]
    print('Characteristic-zero or ell∤60 invariant H1 rank:3 pair orbits -1 vertex relation =2')
    print('All checks PASS')

if __name__=='__main__':main()
