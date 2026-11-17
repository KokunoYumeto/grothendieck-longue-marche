#!/usr/bin/env python3
"""Exact old/source generator action on retained component-pair rows.

Extracts all conjugating heads from the actual F21 operators.  It certifies
the finite generators and checks the resulting row formula against all64
independently computed old-zero column incidences.  It does not enumerate
old-base orbits or infer a full-column relation from an incidence collision.
"""
from pathlib import Path
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_paired_fox_data.json',P/'symmetric_full_source_data.json',
       ROOT/'records/old0_retained_incidence18.json']
raw=[p.read_bytes() for p in paths]
D,S,C=map(json.loads,raw)
started=time.monotonic()

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(int(x))
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):
    return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
old=tuple(D['retained_paired_indices']); oi={x:i+1 for i,x in enumerate(old)}
slots=(2,3,5,6,7,8,10,11)
beta=mp(D['retained_involution']); F=mp(D['paired_involution'])
def fill(w):return red((1 if x>0 else -1)*oi[abs(x)] for x in w if abs(x) in oi)
def b(w):return sub(w,beta)
def conjugator(w,j):
    w=red(w);k=[]
    while len(w)>1 and w[0]==-w[-1]:k.append(w[0]);w=w[1:-1]
    assert w==(j,),(j,w)
    k=tuple(k)
    return k
def datum(name,A,phi,source):
    assert set(A)==set(range(1,22))
    assert all(fill(A[j])==phi[i+1] for i,j in enumerate(old))
    headsA={};headsB={};conjA={};conjB={}
    for i in slots:
        ka=conjugator(A[i],i);kb=conjugator(A[i+10],i+10)
        assert red(ka+(i,)+inv(ka))==A[i]
        assert red(kb+(i+10,)+inv(kb))==A[i+10]
        headsA[i]=fill(ka);headsB[i]=fill(kb);conjA[i]=ka;conjB[i]=kb
    psi={i:b(sub(b((i,)),phi)) for i in range(1,6)}
    if source:
        assert all(sub(F[j],A)==sub(A[j],F) for j in range(1,22))
        assert psi==phi
        assert all(headsB[i]==b(headsA[i]) for i in slots)
    return {'name':name,'source_normalized':source,'phi':phi,'psi':psi,
            'A_heads':headsA,'B_heads':headsB,
            'A_conjugators_F21':conjA,'B_conjugators_F21':conjB}

olddata=[];sourcedata=[]
for a in D['old_actions']:
    d=datum(a['name'],mp(a['geometric_push_paired']),mp(a['retained_push']),False)
    d['phi_inverse']=mp(a['retained_pullback'])
    d['psi_inverse']={i:b(sub(b((i,)),d['phi_inverse'])) for i in range(1,6)}
    olddata.append(d)
for a in S['old_source_generators']:
    d=datum(a['name'],mp(a['source_push_F21']),mp(a['source_push_F5']),True)
    d['far_base_word']=a['far_base_word']
    sourcedata.append(d)

def row_action(d,row):
    i,j,z=row
    return (i,j,red(inv(b(d['A_heads'][i]))+sub(z,d['psi'])+b(d['B_heads'][j])))
def unit_action(d,t,i):return red(sub(t,d['phi'])+d['A_heads'][i])
def row_inverse(d,row):
    i,j,z=row
    return (i,j,sub(red(b(d['A_heads'][i])+z+inv(b(d['B_heads'][j]))),d['psi_inverse']))

d=olddata[0]
checks=[]
for a in C['rows']:
    sr=(a['seed_row'][0],a['seed_row'][1],tuple(a['seed_row'][2]))
    got=row_action(d,sr)
    want=(a['old0_row'][0],a['old0_row'][1],tuple(a['old0_row'][2]))
    assert got==want
    predictedunit=unit_action(d,tuple(a['seed_unit']['F5_word']),sr[0])
    assert predictedunit==tuple(a['old0_unit']['F5_word'])
    assert a['seed_unit']['sign']==a['old0_unit']['sign']
    checks.append({'node_index':a['node_index'],'seed_row':sr,
                   'predicted_old0_row':got,'predicted_retained_unit':predictedunit})

# Verify the composition law on the finite generator pairs themselves.
# Heads are right cocycles: h_(alpha gamma)=phi_alpha(h_gamma) h_alpha.
# Every row transformation then composes literally in the displayed order.
rowtests=[(a['seed_row'][0],a['seed_row'][1],tuple(a['seed_row'][2])) for a in C['rows']]
inverse_checks=0
for d in olddata:
    for i in range(1,6):
        assert sub(d['phi'][i],d['phi_inverse'])==sub(d['phi_inverse'][i],d['phi'])==(i,)
    for row in rowtests:
        assert row_inverse(d,row_action(d,row))==row_action(d,row_inverse(d,row))==row
        inverse_checks+=1
source_far_checks=0
for d in sourcedata:
    for row in rowtests:
        got=row
        # Push is alpha_(uv)=alpha_v alpha_u.  Apply the listed geometric
        # letters in chronological order; the last one acts last.
        for letter in d['far_base_word']:
            op=olddata[abs(letter)-1]
            got=row_action(op,got) if letter>0 else row_inverse(op,got)
        assert got==row_action(d,row)
        source_far_checks+=1
composition_checks=0
for a in olddata:
    for c in olddata:
        comp={'phi':{i:sub(c['phi'][i],a['phi']) for i in range(1,6)},
              'psi':{i:sub(c['psi'][i],a['psi']) for i in range(1,6)},
              'A_heads':{i:red(sub(c['A_heads'][i],a['phi'])+a['A_heads'][i]) for i in slots},
              'B_heads':{i:red(sub(c['B_heads'][i],a['phi'])+a['B_heads'][i]) for i in slots}}
        for row in rowtests:
            assert row_action(comp,row)==row_action(a,row_action(c,row))
            composition_checks+=1

out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(x).hexdigest() for p,x in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'old_generators':olddata,'source_generators':sourcedata,
     'old0_full_incidence_and_unit_checks':checks,
     'old_generator_inverse_row_checks':inverse_checks,
     'actual_source_far_word_row_checks':source_far_checks,
     'old_generator_pair_row_composition_checks':composition_checks,
     'operator_order':'row_action(a,row_action(c,z)) is alpha_a after alpha_c, hence geometric base word c*a',
     'row_formula':'z -> beta(h_Ai)^(-1) (beta phi beta)(z) beta(h_Bj)',
     'source_row_formula':'z -> beta(h_i)^(-1) phi(z) h_j',
     'claims_excluded':['orbit exhaustion','row-stabilizer determination','full-column equality from augmented collision','global kappa value'],
     'elapsed_seconds':time.monotonic()-started}
(ROOT/'work_A/old_base_augmented_row_action.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:6 actual old generators and11 source-normalized generators;272 literal peripheral conjugators/heads.')
print('PASS:all11 source operators commute with F; paired heads and retained automorphisms obey the exact source formula.')
print('PASS:all64 independently computed old0 augmented rows and signed retained units agree.')
print('PASS:',inverse_checks,'old-generator inverse row checks and',source_far_checks,'actual source/far-word row comparisons.')
print('PASS:',composition_checks,'ordered old-generator pair row compositions.')
print('No all-word stabilizer or full-column collision relation is inferred.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
