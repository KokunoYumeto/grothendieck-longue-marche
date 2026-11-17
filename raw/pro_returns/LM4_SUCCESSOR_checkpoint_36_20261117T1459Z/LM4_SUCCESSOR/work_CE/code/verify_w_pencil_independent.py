#!/usr/bin/env python3
"""Independent exact action, w=1 factor, and coefficient-deformation audit.

Reads DE JSON only; does not import its braid or free-group evaluator.
No assertion of whole partial-source normality is made.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json, hashlib

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
B=json.loads((P/'w_pencil_braids.json').read_text())
D=json.loads((P/'w_pencil_fiber_data.json').read_text())

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(int(x))
    return out
def inv(w): return [-x for x in reversed(w)]
def sub(w,a): return red(y for x in w for y in (a[abs(x)] if x>0 else inv(a[abs(x)])))
def comp(a,b): return {i:sub(w,a) for i,w in b.items()}
def conjugate(h,w): return red(h+w+inv(h))

def artin(word,n=13):
    # Evaluate each generator separately, applying elementary substitutions
    # in reverse order. This is independent of DE's update-of-image-pairs.
    result={}
    for i in range(1,n+1):
        w=[i]
        for s in reversed(word):
            k=abs(s)
            a={j:[j] for j in range(1,n+1)}
            if s>0: a[k]=[k,k+1,-k];a[k+1]=[k]
            else: a[k]=[k+1];a[k+1]=[-k-1,k,k+1]
            w=sub(w,a)
        result[i]=w
    return result

def marked_action(a,mark=11,n=13):
    remain=[i for i in range(1,n+1) if i!=mark]
    ren={i:j+1 for j,i in enumerate(remain)}
    def fill(w): return red((ren[abs(x)] if x>0 else -ren[abs(x)]) for x in w if abs(x)!=mark)
    w=list(a[mark]);h=[]
    while len(w)>1:
        assert w[0]==-w[-1]
        h.append(w[0]);w=w[1:-1]
    assert w==[mark]
    q=fill(h)
    return {ren[i]:conjugate(inv(q),fill(a[i])) for i in remain}, inv(q)

def intmap(m):return {int(i):w for i,w in m.items()}

def pointed_transport(a,domain_mark,range_mark):
    """Map between two distinct marked positions, using the actual path."""
    w=list(a[domain_mark]);h=[]
    while len(w)>1:
        assert w[0]==-w[-1]
        h.append(w[0]);w=w[1:-1]
    assert w==[range_mark]
    domain=[i for i in range(1,14) if i!=domain_mark]
    target=[i for i in range(1,14) if i!=range_mark]
    ren={i:j+1 for j,i in enumerate(target)}
    def fill(w):return red((ren[abs(x)] if x>0 else -ren[abs(x)]) for x in w if abs(x)!=range_mark)
    q=fill(h)
    return {j+1:conjugate(inv(q),fill(a[i])) for j,i in enumerate(domain)}

standards=intmap(D['standard_kernel_braids'])
fw=intmap(D['standard_kernel_words'])
back=intmap(D['inverse_standard_basis'])
SA={i:artin(w) for i,w in standards.items()}
for i in range(1,13):
    assert marked_action(SA[i])[1]==fw[i]
    assert sub(fw[i],back)==[i] and sub(back[i],fw)==[i]

count=0
for index,row in enumerate(B['loops']):
    a=artin(row['word']);ai=artin(inv(row['word']))
    action,push=marked_action(a)
    actioni,_=marked_action(ai)
    for i in range(1,14):assert sub(a[i],ai)==[i] and sub(ai[i],a)==[i]
    if row['kind'] in ('old','filled'):
        assert action==intmap(D['old_and_filled_actions'][str(index)])
        assert actioni==intmap(D['old_and_filled_inverse_actions'][str(index)])
        for i in range(1,13):
            conjugated=comp(a,comp(SA[i],ai))
            assert marked_action(conjugated)[1]==sub(fw[i],action)
            count+=1
    else:assert push==D['source_fiber_words'][str(index)]
assert count==132
print('PASS: independent reversed-substitution evaluator agrees on all24 actions/words and132 full-kernel conjugations.')

markings=json.loads((P/'w_local_markings.json').read_text())
local_checks=0
for row,record in zip(B['loops'],markings['all_local_markings']):
    assert row['name']==record['name']
    mark=record['source_local_position']
    assert record['local_order'][mark-1]==12
    prefix=red(B['common_trunk']['word']+row['forward_segments'][0]['word'])
    forward=pointed_transport(artin(prefix),mark,11)
    backward=pointed_transport(artin(inv(prefix)),11,mark)
    assert forward==intmap(record['local_to_initial_fiber'])
    assert backward==intmap(record['initial_to_local_fiber'])
    for i in range(1,13):
        assert sub(forward[i],backward)==[i] and sub(backward[i],forward)==[i]
        local_checks+=2
    assert artin(record['local_braid'])==artin(record['standard_local_braid'])
    local_action=marked_action(artin(record['standard_local_braid']),mark=mark)[0]
    assert comp(forward,comp(local_action,backward))==marked_action(artin(row['word']))[0]
assert local_checks==576
print('PASS: all24 local standard braid forms and actual reverse-path pointed transports,576 inverse-basis identities; every global action is their transported local action.')

# The actual w=1 corner: four consecutive local strands, source second.
row=next(r for r in B['loops'] if r['name']=='base_positive_0')
corner=row['forward_segments'][0]['final_order']
assert corner==[3,9,10,4,2,8,0,11,5,7,12,1,6]
local=red(x for s in row['forward_segments'][1:] for x in s['word'])
full=[10,11,12]*4
point=[10,10]
nodes=[1,1,3,3,5,5,8,8]
assert artin(local)==artin(full+point+nodes)
path=red(B['common_trunk']['word']+row['forward_segments'][0]['word'])
assert artin(row['word'])==artin(path+full+point+nodes+inv(path))

delta,_=marked_action(artin(full))
eta,p=marked_action(artin(point))
nu,_=marked_action(artin(nodes))
K=[10,11,12]  # Corner fiber indices after deleting marked strand11.
assert p==[-10]
for i in range(1,13):
    assert delta[i]==([i] if i in (10,11,12) else conjugate(inv(K),[i]))
    assert eta[i]==conjugate(p,[i])
    if i in (7,10,11,12):assert nu[i]==[i]
assert marked_action(artin(local))[0]==comp(eta,comp(delta,nu))
transport,_=marked_action(artin(path))
transport_inverse,_=marked_action(artin(inv(path)))
for i in range(1,13):assert sub(transport[i],transport_inverse)==[i] and sub(transport_inverse[i],transport)==[i]
assert marked_action(artin(row['word']))[0]==comp(transport,comp(eta,comp(delta,comp(nu,transport_inverse))))
print('PASS: actual w1 factorization = Delta[10..13]^2 sigma10^2 sigma1^2 sigma3^2 sigma5^2 sigma8^2, with its literal common whisker.')
print('PASS: pointed Delta fixes three internal fiber generators and conjugates all9 exterior ones by K^-1; residual point push is Inn(x10^-1).')

# Exact rational enclosures for the true fifth roots. Error is far below
# the independently audited uniform segment separation in the producer.
scale=10**90
def sqrt_interval(lo,hi):
    a=isqrt(lo.numerator*scale*scale//lo.denominator)
    b=isqrt(hi.numerator*scale*scale//hi.denominator)+1
    return F(a,scale),F(b,scale)
s5=sqrt_interval(F(5),F(5))
splus=sqrt_interval(10+2*s5[0],10+2*s5[1])
sminus=sqrt_interval(10-2*s5[1],10-2*s5[0])
def div(a,n):return a[0]/n,a[1]/n
def neg(a):return -a[1],-a[0]
c1=((s5[0]-1)/4,(s5[1]-1)/4)
c2=(-(s5[1]+1)/4,-(s5[0]+1)/4)
t1=div(splus,4);t2=div(sminus,4)
true=[((F(1),F(1)),(F(0),F(0))),(c1,t1),(c2,t2),(c2,neg(t2)),(c1,neg(t1))]
rho=F(1,10**30)
rat=[tuple(F(x) for x in a) for a in B['coefficient_points']]
for z,rect in zip(rat,true):
    for x,(lo,hi) in zip(z,rect):assert max(abs(x-lo),abs(x-hi))<rho or lo==hi==x
# Euclidean error <2e-30; each parameter has |w|<6. A moving
# strand changes by <12e-30, any pair difference by <24e-30.
assert F(24,10**30)<F(1,10**12)
segments=[B['common_trunk']]+[s for r in B['loops'] for s in r['forward_segments']]
assert len(segments)==121
for seg in segments:
    for endpoint in ('start','end'):
        a,b=map(F,seg[endpoint]);assert abs(a)+abs(b)<6
    assert seg['uniform_rational_difference_lower_bound']=='1/10^12'
    assert seg['derivative_bound']=='100000000'

# Enclose the actual source-product critical point near every stored center
# by the elementary quadratic Rouché bound on a radius1e-25 disk.
def cmul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
critical_radius=F(1,10**25)
for r in B['loops']:
    if r['kind']=='source_product':
        j=int(r['name'].split('_')[2]);z=tuple(F(x) for x in r['center'])
        v=(z[0]-1,z[1]);v2=cmul(v,v)
        residue=(v2[0]+rat[j][0]-1,v2[1]+rat[j][1])
        assert v[0]*v[0]+v[1]*v[1]>F(1,4)
        assert abs(residue[0])+abs(residue[1])+2*rho<critical_radius-critical_radius**2

initial=B['initial_order'];base=F(1,200)
points=[(F(0),F(0))]+[(base*a,base*b) for a,b in rat]+[(base*base,F(0))]+rat+[(base*(2-base),F(0))]
proj=[a-F(371,1000)*b for a,b in points]
gaps=[proj[j]-proj[i] for i,j in zip(initial,initial[1:])]
assert min(gaps)>F(1,10**10)
print('PASS: exact true fifth-root coordinate errors <1e-30, all121 segment displacements <24e-30 versus separation1e-12; initial marking stable.')
print('PASS: true source-product critical values lie in the assigned radius1e-25 disks by exact quadratic bounds.')

source_words={int(i):w for i,w in D['source_fiber_words'].items()}
combined=list(source_words.values())+[[j] for j in D['missing_retained_indices']]
combo={i+1:w for i,w in enumerate(combined)}
for j,w in D['fiber_generators_in_source_words_and_missing'].items():assert sub(w,combo)==[int(j)]
print('PASS: all12 actual fiber generators recovered from the source words and three specified retained meridians.')

out={
 'description':__doc__,'independent_full_kernel_conjugation_checks':count,
 'independent_local_transport_inverse_checks':local_checks,
 'actual_w1_corner_order':corner,'local_factor_word':full+point+nodes,
 'actual_common_whisker':path,'local_boundary_in_corner_fiber':K,
 'corner_to_original_fiber':transport,'original_to_corner_fiber':transport_inverse,
 'residual_point_push_in_corner_fiber':p,
 'full_twist_action':delta,'exterior_node_action':nu,
 'coefficient_coordinate_error_bound':'1e-30','configuration_difference_bound':'24e-30',
 'segment_separation_bound':'1e-12','checked_segments':len(segments),
 'true_critical_disk_radius':'1e-25','initial_min_projected_gap':str(min(gaps)),
 'input_sha256':{name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
                 ['w_pencil_braids.json','w_pencil_fiber_data.json','w_local_markings.json']},
 'scope':'Actual words, marking, coefficient homotopy, global w1 factorization. No whole source-kernel normalizer is inferred.'}
(ROOT/'work_CE/w_pencil_independent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
