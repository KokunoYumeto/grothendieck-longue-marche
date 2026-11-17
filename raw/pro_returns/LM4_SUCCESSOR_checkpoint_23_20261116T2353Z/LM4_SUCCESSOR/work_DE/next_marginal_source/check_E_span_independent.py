#!/usr/bin/env python3
"""Independent replay and kernel audit for the actual128-column Z[E] span.

Every ordered noncommutative unit elimination is replayed. The ten final
columns have private rows with nonzero two-term unit binomials; finite
support and torsion-freeness prove their independence. The twelve pure-E
F-mate relations are checked as the entire kernel, including its actual
semilinear involution. No larger deck/base closure is claimed.
"""
from pathlib import Path
from collections import Counter
import json,hashlib,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
paths=[ROOT/'records/intrinsic_E_span18.json',ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',ROOT/'work_CE/next_symmetric_nodes/symmetric_F_node_matching.json']
raw=[p.read_bytes() for p in paths];D,P,M=map(json.loads,raw);started=time.monotonic()
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(int(x))
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def multiply(g,h):return red(g[0]+h[0]),red(g[1]+h[1])
def invert(g):return inv(g[0]),inv(g[1])
def plus(d,k,n):
    d[k]=d.get(k,0)+n
    if not d[k]:del d[k]
def convolution(a,b):
    c={}
    for g,m in a.items():
        for h,n in b.items():plus(c,multiply(g,h),m*n)
    return c
def subtract(c,q,p):
    for row,poly in p.items():
        target=c.setdefault(row,{})
        for g,n in convolution(q,poly).items():plus(target,g,-n)
        if not target:del c[row]
def copy(c):return {k:dict(v) for k,v in c.items()}
def parse(rows):
    out={}
    for r in rows:
        row=tuple(r['row']) if isinstance(r['row'],list) else r['row']
        out[row]={(tuple(t['A_word']),tuple(t['B_word'])):t['coefficient'] for t in r['terms']}
    return out
def ring(rows):return {(tuple(r['A_word']),tuple(r['B_word'])):r['coefficient'] for r in rows}
def seed(r):
    out={}
    for c in r['fox_cells']:
        key=c['A_generator'],c['B_generator'];g=tuple(c['A_vertex']),tuple(c['B_vertex'])
        plus(out.setdefault(key,{}),g,c['coefficient'])
    return {k:v for k,v in out.items() if v}
def flipchain(c):return {(j,i):{(b,a):-n for (a,b),n in q.items()} for (i,j),q in c.items()}
ONE=((),());first=[seed(r) for r in P['node_columns']]
original=first+[flipchain(c) for c in first]
active={i:copy(c) for i,c in enumerate(original)}
basis={i:{i:{ONE:1}} for i in active};removed={}
for step in D['elimination_steps']:
    j=step['pivot_column'];row=tuple(step['row']);pivot=active.pop(j)
    unit={tuple(tuple(v) for v in step['pivot_monomial']):step['sign']}
    assert pivot[row]==unit and abs(step['sign'])==1
    u=next(iter(unit));ui={invert(u):step['sign']}
    changed=set()
    for change in step['changes']:
        k=change['column'];q=ring(change['left_multiplier'])
        assert k in active and k!=j and k not in changed
        assert q==convolution(active[k][row],ui)
        subtract(active[k],q,pivot);subtract(basis[k],q,basis[j]);changed.add(k)
    assert all(row not in c for c in active.values())
    removed[j]=pivot
assert len(removed)==106
zeros={j for j,c in active.items() if not c}
rest={j:c for j,c in active.items() if c}
assert len(zeros)==12 and len(rest)==10
stored={r['original_column']:r for r in D['image_basis']+D['kernel_basis']+D['uneliminated']}
assert set(stored)==set(range(128))
for j,r in stored.items():
    assert basis[j]==parse(r['expression'])
    if j in removed:assert removed[j]==parse(r['chain'])
    elif j in rest:assert rest[j]==parse(r['chain'])
    else:assert j in zeros
# Each update was a reversible elementary source-basis operation.
# Thus the128 recorded vectors form a basis over the noncommutative ring.

support=Counter(row for c in rest.values() for row in c)
private=[]
for j,c in rest.items():
    row=next(row for row,p in c.items() if support[row]==1 and len(p)==2 and all(abs(v)==1 for v in p.values()))
    terms=list(c[row]);g,h=terms
    assert g!=h
    ratio=multiply(h,invert(g))
    nonzero=next(w for w in ratio if w)
    core=nonzero
    while len(core)>1 and core[0]==-core[-1]:core=core[1:-1]
    assert core
    private.append({'column':j,'row':row,'two_monomials':terms,'infinite_order_ratio':ratio,'nonempty_cyclic_core':core})
# If x*(eps*g+delta*h)=0, finite support of x is invariant under the
# infinite-order right translation h*g^-1. Hence x=0. The ten private
# rows therefore prove independence, while pivot rows separate the106
# preceding images. The kernel is exactly the twelve zero basis vectors.

labels={(r['loop_index'],r['local_node_index']):j for j,r in enumerate(P['node_columns'])}
pure=[r for r in M['rows'] if r['pure_E_coefficient']]
assert len(pure)==12
relations={};mates={};coefficients={}
def evaluate(v):
    ans={}
    for j,q in v.items():subtract(ans,{g:-n for g,n in q.items()},original[j])
    return ans
for r in pure:
    j=labels[tuple(r['node_index'])];m=labels[tuple(r['physical_F_mate_index'])]
    a=tuple(r['E_coefficient']['A_word']),tuple(r['E_coefficient']['B_word'])
    sign=r['A_first_orientation_signs'][0]*r['A_first_orientation_signs'][1]
    rel={64+j:{ONE:1},m:{a:sign}}
    assert not evaluate(rel)
    assert {k:q for k,q in rel.items() if k in zeros}=={64+j:{ONE:1}}
    relations[j]=rel;mates[j]=m;coefficients[j]={a:sign}
assert {64+j for j in relations}==zeros
for j in zeros:
    assert {k:q for k,q in basis[j].items() if k in zeros}=={j:{ONE:1}}
    assert basis[j]==relations[j-64]
# The relation basis is literally the replayed kernel basis, not merely
# an independent set of twelve relations.
def flipdomain(v):
    return {(j+64 if j<64 else j-64):{(b,a):n for (a,b),n in q.items()} for j,q in v.items()}
def scale(q,v):return {j:convolution(q,p) for j,p in v.items()}
cycles=[]
for j,rel in relations.items():
    fq={(b,a):n for (a,b),n in coefficients[j].items()}
    assert flipdomain(rel)==scale(fq,relations[mates[j]])
    assert convolution(fq,coefficients[mates[j]])=={ONE:1}
    cycles.append({'seed_column':j,'mate_seed_column':mates[j],'coefficient':[(a,b,n) for (a,b),n in fq.items()]})
fixed=[j for j in relations if mates[j]==j]
assert len(fixed)==4 and all(next(iter(coefficients[j].values()))==1 for j in fixed)

# Independently change coordinates for the actual F image of every one
# of the128 original-domain basis vectors. Reconstructing in the old
# basis checks the whole inverse transformation, including kernel terms.
def coordinates(v):
    ans=copy(v)
    for step in D['elimination_steps']:
        j=step['pivot_column']
        for change in step['changes']:
            k=change['column']
            if k not in ans:continue
            extra=convolution(ans[k],ring(change['left_multiplier']))
            target=ans.setdefault(j,{})
            for g,n in extra.items():plus(target,g,n)
            if not target:del ans[j]
    reconstructed={}
    for j,q in ans.items():subtract(reconstructed,{g:-n for g,n in q.items()},basis[j])
    assert reconstructed==v
    return ans
image_order=D['free_image_original_ids'];image_pos={j:i for i,j in enumerate(image_order)}
kernel_order=[r['original_column'] for r in D['kernel_basis']]
kernel_pos={j:i for i,j in enumerate(kernel_order)}
image_F=[parse(r) for r in D['F_matrix_in_free_image_basis']]
kernel_F=[parse(r) for r in D['F_matrix_in_kernel_basis']]
for i,j in enumerate(image_order):
    transformed=coordinates(flipdomain(basis[j]))
    assert {image_pos[k]:q for k,q in transformed.items() if k in image_pos}==image_F[i]
    rebuilt={}
    for k,q in image_F[i].items():
        target=removed.get(image_order[k],rest.get(image_order[k]))
        subtract(rebuilt,{g:-n for g,n in q.items()},target)
    assert rebuilt==flipchain(removed.get(j,rest.get(j)))
for i,j in enumerate(kernel_order):
    transformed=coordinates(flipdomain(basis[j]))
    assert not(set(transformed)&set(image_pos))
    assert {kernel_pos[k]:q for k,q in transformed.items()}==kernel_F[i]
def monomial_orbits(matrix):
    fixed_rows=[]
    for i,r in enumerate(matrix):
        assert len(r)==1
        j,q=next(iter(r.items()));assert len(q)==1
        g,n=next(iter(q.items()));assert abs(n)==1
        k,qq=next(iter(matrix[j].items()))
        assert k==i and convolution({(b,a):v for (a,b),v in q.items()},qq)=={ONE:1}
        if j==i:fixed_rows.append((i,g,n))
    return fixed_rows
image_fixed=monomial_orbits(image_F);kernel_fixed=monomial_orbits(kernel_F)
assert len(image_fixed)==4 and all(n==-1 for i,g,n in image_fixed)
assert len(kernel_fixed)==4 and all(n==1 for i,g,n in kernel_fixed)
assert [i for i,g,n in image_fixed]==[60,81,90,103]
assert [image_order[i] for i,g,n in image_fixed]==[61,1,37,49]
for i,g,n in image_fixed:
    j=image_order[i];assert basis[j]=={j:{ONE:1}} # unchanged actual raw columns
half_path=ROOT/'work_CE/next_symmetric_nodes/symmetric_F_cycles_and_fixed_chains.json'
half_raw=half_path.read_bytes();half=json.loads(half_raw)
half_by_node={tuple(r['node_index']):r for r in half['fixed_cell_anti_chains']}
fixed_source=[]
for i,g,n in image_fixed:
    j=image_order[i];label=tuple(D['column_labels'][j][:2]);h=half_by_node[label]
    x=tuple(h['E_half_translation']['A_word']);y=tuple(h['E_half_translation']['B_word'])
    assert multiply((y,x),g)==(x,y)
    fixed_source.append({'image_basis':i,'raw_column':j,'node':label,
                         'actual_source_ids':[(w['source_sheet'],w['critical_index'],w['power']) for w in h['source_left_ideal_zero_witnesses']]})
# The four half/source identities were separately expanded into actual
# F13 words by check_symmetric_F_cycles_independent.py. Here they are
# matched to precisely the unchanged negative fixed image generators.
out={'input_sha256':{p.name:hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'replayed_unit_pivots':106,'private_binomial_rows':private,'free_image_rank':116,'free_kernel_rank':12,
     'pure_E_relations_equal_full_kernel_basis':True,'F_kernel_cycles':cycles,
     'positive_fixed_kernel_summands':fixed,'exchanged_kernel_pairs':4,
     'original_domain_F_coordinate_reconstructions':128,
     'image_F_orbits':{'negative_fixed':4,'exchanged_pairs':56},
     'kernel_F_orbits':{'positive_fixed':4,'exchanged_pairs':4},
     'fixed_image_source_identifications':fixed_source,
     'half_source_certificate_sha256':hashlib.sha256(half_raw).hexdigest(),
     'scope':'full Z[E] span of64 seeds and their F-images only; no retained-deck or old-base orbit closure',
     'elapsed_seconds':time.monotonic()-started}
(HERE/'intrinsic_E_span_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:106 ordered reversible noncommutative unit pivots replayed; all128 domain vectors matched.')
print('PASS:10 private infinite-order unit-binomial rows prove free image rank116 and kernel rank12.')
print('PASS:12 actual pure-E F-mate relations are literally the entire kernel basis.')
print('PASS:kernel F action has4 positive fixed summands and4 exchanged pairs; no larger closure claimed.')
print('PASS:all128 F coordinate reconstructions, exact semilinear squares and both monomial matrices.')
print('PASS:image F has56 pairs and4 unchanged negative fixed columns, exactly the four source anti-chains.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
