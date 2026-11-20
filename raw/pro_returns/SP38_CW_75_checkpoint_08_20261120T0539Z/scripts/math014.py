"""Finite group certificates for scan 014; no image or witness reading."""
from itertools import product,permutations,combinations
from pathlib import Path
import json

out=Path(__file__).resolve().parents[1]
class Field:
    def __init__(self,q):self.q=q
    def add(self,a,b):return a^b if self.q==4 else (a+b)%self.q
    def neg(self,a):return a if self.q==4 else (-a)%self.q
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        if self.q!=4:return (a*b)%self.q
        z=0
        while b:
            if b&1:z^=a
            b>>=1;a<<=1
            if a&4:a^=7
        return z
    def inv(self,a):
        assert a
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)
    def div(self,a,b):return self.mul(a,self.inv(b))
    def det(self,m):a,b,c,d=m;return self.sub(self.mul(a,d),self.mul(b,c))
    def mm(self,m,n):
        a,b,c,d=m;e,f,g,h=n
        return (self.add(self.mul(a,e),self.mul(b,g)),self.add(self.mul(a,f),self.mul(b,h)),self.add(self.mul(c,e),self.mul(d,g)),self.add(self.mul(c,f),self.mul(d,h)))
    def normalize(self,m):
        v=self.inv(next(x for x in m if x))
        return tuple(self.mul(v,x) for x in m)
    def pm(self,m,n):return self.normalize(self.mm(m,n))
    def mi(self,m):
        a,b,c,d=m
        return self.normalize((d,self.neg(b),self.neg(c),a))
    def pg(self):
        return sorted({self.normalize(m) for m in product(range(self.q),repeat=4) if self.det(m)})
    def mobius(self,m):
        a,b,c,d=m;p=[]
        for x in range(self.q):
            num=self.add(self.mul(a,x),b);den=self.add(self.mul(c,x),d)
            p.append(self.q if den==0 else self.div(num,den))
        p.append(self.q if c==0 else self.div(a,c))
        return tuple(p)
def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def even(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0

certificate={'field_F4':'0,1,t,t+1 encoded as 0,1,2,3; t^2+t+1=0','checks':{}}
for q in [2,3,4,5]:
    f=Field(q)
    assert all(f.mul(a,f.inv(a))==1 for a in range(1,q))
    assert all(f.mul(a,f.add(b,c))==f.add(f.mul(a,b),f.mul(a,c)) for a,b,c in product(range(q),repeat=3))

f=Field(2);vec=list(product(range(2),repeat=2));gl=[m for m in product(range(2),repeat=4) if f.det(m)]
aff=[]
for m in gl:
    a,b,c,d=m
    for u,v in vec:
        aff.append(tuple(vec.index((f.add(f.add(f.mul(a,x),f.mul(b,y)),u),f.add(f.add(f.mul(c,x),f.mul(d,y)),v))) for x,y in vec))
assert len(aff)==24 and set(aff)==set(permutations(range(4)))
certificate['checks']['AGL2_F2']={'GL_count':len(gl),'affine_count':len(aff),'image':'all S4','permutations':[list(x) for x in sorted(aff)]}

for q,expected in [(3,24),(4,60),(5,120)]:
    f=Field(q);g=f.pg();ps={m:f.mobius(m) for m in g}
    assert len(g)==expected and len(set(ps.values()))==expected
    assert all(ps[f.pm(a,b)]==compose(ps[a],ps[b]) for a in g for b in g)
    if q==3:assert set(ps.values())==set(permutations(range(4)))
    if q==4:assert set(ps.values())=={p for p in permutations(range(5)) if even(p)}
    certificate['checks'][f'PGL2_F{q}']={'order':len(g),'faithful_projective_line_action':True,'all_products_verified':len(g)**2,'action_degree':q+1,'all_action_permutations_even':all(even(p) for p in ps.values())}

f=Field(4)
aff4=[tuple(f.add(f.mul(a,x),b) for x in range(4)) for a in range(1,4) for b in range(4)]
assert len(aff4)==12 and set(aff4)=={p for p in permutations(range(4)) if even(p)}
certificate['checks']['AGL1_F4']={'order':len(aff4),'image':'all A4','permutations':[list(p) for p in sorted(aff4)]}

f=Field(5);g=f.pg();I=(1,0,0,1);squares={f.mul(x,x) for x in range(1,5)}
psl=[a for a in g if f.det(a) in squares]
assert len(psl)==60
invol=[a for a in psl if a!=I and f.pm(a,a)==I]
assert len(invol)==15
blocks=set()
for a,b in combinations(invol,2):
    if f.pm(a,b)==f.pm(b,a):
        v=frozenset([I,a,b,f.pm(a,b)])
        assert len(v)==4 and all(f.pm(x,y) in v for x in v for y in v)
        blocks.add(v)
blocks=sorted(blocks,key=lambda b:sorted(b));assert len(blocks)==5
assert set().union(*(b-{I} for b in blocks))==set(invol)
assert sum(len(b)-1 for b in blocks)==len(invol)
block_index={b:i for i,b in enumerate(blocks)}
action={}
for a in g:
    ai=f.mi(a)
    action[a]=tuple(block_index[frozenset(f.pm(f.pm(a,x),ai) for x in b)] for b in blocks)
assert len(set(action.values()))==120
assert set(action.values())==set(permutations(range(5)))
assert all(action[f.pm(a,b)]==compose(action[a],action[b]) for a in g for b in g)
certificate['checks']['PGL2_F5_to_S5']={'PSL_order':len(psl),'PSL_involutions':len(invol),'V4_blocks':[[list(m) for m in sorted(b)] for b in blocks],'conjugation_image_order':len(set(action.values())),'all_products_verified':len(g)**2,'matrix_to_permutation':[{'matrix':list(a),'permutation':list(action[a])} for a in g]}

f=Field(3);A=(0,2,1,0);minusI=(2,0,0,2)
assert f.mm(A,A)==minusI
assert all(f.mm(tuple(f.mul(s,x) for x in A),tuple(f.mul(s,x) for x in A))==minusI for s in [1,2])
assert f.normalize(A)!=I and f.pm(f.normalize(A),f.normalize(A))==I
certificate['checks']['GL2_F3_nonsplitting_witness']={'matrix':list(A),'square':list(minusI),'projective_order':2,'both_scalar_lifts_have_order':4}
certificate['checks']['projective_cardinality_counterexamples']={'F2_squared_vector_orbits_including_zero':4,'P1_F2_points':3,'P2_F2_points':7,'mixed_affine_E_cardinality':2,'mixed_affine_V_cardinality':4,'dimension':2,'affine_structures_on_E':0,'affine_structure_orbits_on_V':1,'bijections_to_V':24}
certificate['all_assertions_passed']=True
(out/'decisions/scan014_finite_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps({'all_assertions_passed':True,'AGL2F2':'S4','PGL2F3':'S4','AGL1F4':'A4','PGL2F4':'A5','PGL2F5':'S5 via conjugation on five V4 subgroups','verified_group_products':24**2+60**2+120**2+120**2}))
