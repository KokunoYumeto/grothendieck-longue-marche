"""Exact cross-ratio degree audit and explicit common-kernel free words.

No symbolic limit is used. The free words are also separated in a finite
permutation group constructed directly from their reduced edge paths.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import gzip, hashlib, json
import sympy as s

OUT=Path(__file__).resolve().parent
z=s.symbols('z'); I=s.I

def normal(m):
    entries=list(m)
    first=next(x for x in entries if x!=0)
    return tuple(s.simplify(x/first) for x in entries)

def mul(a,b): return normal(s.Matrix(2,2,a)*s.Matrix(2,2,b))
identity=(s.Integer(1),s.Integer(0),s.Integer(0),s.Integer(1))
generators=[(-1,0,0,1),(0,1,1,0),(1,I,1,-I)]
group=[identity]; seen={identity}
for a in group:
    for b in generators:
        c=mul(a,b)
        if c not in seen: seen.add(c); group.append(c)
assert len(group)==12
orders=[]
exceptional=s.Poly(1,z,domain=s.QQ_I)
infinity=False
for g in group[1:]:
    a,b,c,d=g
    f=s.Poly(c*z*z+(d-a)*z-b,z,domain=s.QQ_I)
    if f.degree()>=1: exceptional=s.lcm(exceptional,f.monic()).monic()
    if c==0: infinity=True
    h=identity
    for k in range(1,13):
        h=mul(h,g)
        if h==identity: orders.append(k); break
assert exceptional.degree()==13 and infinity
assert Counter(orders)=={2:3,3:8}

def diff(g,h):
    a,b,c,d=g; e,f,k,l=h
    return s.Poly(s.expand((a*z+b)*(k*z+l)-(e*z+f)*(c*z+d)),z,domain=s.QQ_I)

hist=Counter(); records=[]
for ids in combinations(range(12),4):
    a,b,c,d=[group[k] for k in ids]
    num=diff(a,c)*diff(b,d)
    den=diff(a,d)*diff(b,c)
    gcd=s.gcd(num,den); num=num.exquo(gcd);den=den.exquo(gcd)
    degree=max(num.degree(),den.degree())
    assert degree<=4
    hist[int(degree)]+=1
    finite_boundary=s.Poly(1,z,domain=s.QQ_I)
    for f in (num,den,num-den):
        if not f.is_zero and f.degree()>=1:
            finite_boundary=s.lcm(finite_boundary,f.sqf_part().monic()).monic()
    assert exceptional.rem(finite_boundary).is_zero
    # Infinity maps to 0, 1 or infinity exactly in these leading-term cases.
    infinity_boundary=(num.degree()!=den.degree() or num.LC()==den.LC())
    used=finite_boundary.degree()+int(infinity_boundary)
    assert used<=12 and used<14
    records.append({'labels':ids,'degree':int(degree),'boundary_points_used':int(used),
                    'boundary_points_killed':int(14-used)})
(OUT/'root_a4_crossratio_degrees.json').write_text(json.dumps(records,indent=2))
print(json.dumps({'A4_order':12,'element_orders':dict(Counter(orders)),
    'exceptional_affine_polynomial':str(exceptional.as_expr()),
    'exceptional_points':14,'four_subsets':len(records),'degree_histogram':dict(hist),
    'minimum_killed_punctures':min(r['boundary_points_killed'] for r in records)}),flush=True)

def reduce_word(word):
    out=[]
    for x in word:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return out
def inverse(w):return [-x for x in reversed(w)]
def comm(a,b):return reduce_word(a+b+inverse(a)+inverse(b))
def substitute(w, images):
    out=[]
    for x in w:
        out.extend(images[abs(x)] if x>0 else inverse(images[-x]))
    return reduce_word(out)

def witness(punctures):
    rank=punctures-1
    peripheral=[[i] for i in range(1,rank+1)]+[list(range(-rank,0))]
    word=peripheral[0]
    for c in peripheral[1:]: word=comm(word,c)
    assert word
    for i in range(1,rank+1):
        images={j:([j] if j!=i else []) for j in range(1,rank+1)}
        assert substitute(word,images)==[]
    images={j:[j] for j in range(1,rank)}
    images[rank]=list(range(-(rank-1),0))
    assert substitute(word,images)==[]

    degree=len(word)+1
    partial=[{} for _ in range(rank)]
    for k,x in enumerate(word):
        source,target=(k,k+1) if x>0 else (k+1,k)
        data=partial[abs(x)-1]
        assert source not in data or data[source]==target
        data[source]=target
    permutations=[]; inverses=[]
    for data in partial:
        assert len(set(data.values()))==len(data)
        dom=[x for x in range(degree) if x not in data]
        used_range=set(data.values())
        ran=[x for x in range(degree) if x not in used_range]
        data.update(zip(dom,ran))
        perm=[data[x] for x in range(degree)]
        inv=[0]*degree
        for x,y in enumerate(perm):inv[y]=x
        permutations.append(perm);inverses.append(inv)
    image=0
    for x in word:image=(permutations if x>0 else inverses)[abs(x)-1][image]
    assert image==degree-1 and image!=0
    path=OUT/f'root_crossratio_word_{punctures}.json.gz'
    with gzip.open(path,'wt') as f:
        json.dump({'punctures':punctures,'rank':rank,'word':word,
                   'permutations':permutations,'image_of_zero':image},f)
    return {'punctures':punctures,'rank':rank,'reduced_word_length':len(word),
            'finite_permutation_degree':degree,'image_of_zero':image,
            'every_peripheral_filling_kills_word':True,
            'certificate':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

for n in (14,7):print(json.dumps(witness(n)),flush=True)
