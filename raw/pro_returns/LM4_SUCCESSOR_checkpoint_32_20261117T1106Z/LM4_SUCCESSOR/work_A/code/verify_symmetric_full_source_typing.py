#!/usr/bin/env python3
"""Independent projection/orientation audit of the actual 19-source certificate.
Reads final data only, without importing or executing its producer.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_full_source_data.json','symmetric_paired_fox_data.json',
       'symmetric_node_words_pullback_corrected.json']
raw={n:(P/n).read_bytes() for n in names}
D,B,N=[json.loads(raw[n]) for n in names]

def red(w):
    r=[]
    for a in w:
        if r and r[-1]==-a:r.pop()
        else:r.append(a)
    return tuple(r)
def inv(w):return tuple(-a for a in reversed(w))
def sub(w,A):return red(b for a in w for b in (A[a] if a>0 else inv(A[-a])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}

start=time.monotonic();F=mp(B['paired_involution'])
cut=mp(B['paired_basis_forward_in_nodal_cut_basis'])
keep=D['first_family_F13_kept_paired_indices'];old=B['retained_paired_indices']
assert keep==sorted(set(old)|set(B['deleted_right_slots'])) and len(keep)==13
f13={j:((keep.index(j)+1,) if j in keep else ()) for j in range(1,22)}
f5={j:((old.index(j)+1,) if j in old else ()) for j in range(1,22)}
f135=mp(D['F13_to_retained_F5'])
assert all(sub(f13[j],f135)==f5[j] for j in range(1,22))

rows=[]
for row in D['old_source_generators']:
    A,Ai=mp(row['source_push_F21']),mp(row['source_pullback_F21'])
    A13,A13i=mp(row['source_push_F13']),mp(row['source_pullback_F13'])
    A5,A5i=mp(row['source_push_F5']),mp(row['source_pullback_F5'])
    h=tuple(row['h_paired']);k=tuple(row['k_paired'])
    assert red(sub(h,F)+inv(h))==k
    for j in range(1,22):
        assert sub(A[j],F)==sub(F[j],A)
        assert sub(A[j],f13)==sub(f13[j],A13)
        assert sub(Ai[j],f13)==sub(f13[j],A13i)
        assert sub(A[j],f5)==sub(f5[j],A5)
        assert sub(Ai[j],f5)==sub(f5[j],A5i)
    for j in range(1,14):
        assert sub(A13[j],f135)==sub(f135[j],A5)
        assert sub(A13i[j],f135)==sub(f135[j],A5i)
    for j in range(1,6):
        assert sub(A5[j],A5i)==(j,)==sub(A5i[j],A5)
    rows.append({'name':row['name'],'all21_F_commutations':True,
                 'all_filling_squares':True,'all5_inverse_pairs':True})
print('PASS all11 source actions: literal F-commutation, both actual filling diagrams, and F5 inverse pairs.')

deleted={j for j,w in f135.items() if not w};cores=set();seeds=[]
for row in D['source_peripheral_generators']:
    h=tuple(row['positive_source_word_F21']);h13=sub(h,f13)
    assert h13==tuple(row['positive_source_word_F13']) and not sub(h,f5)
    v=h13;c=[]
    while len(v)>1 and v[0]==-v[-1]:c.append(v[0]);v=v[1:-1]
    assert v==(row['F13_positive_core'],) and tuple(c)==tuple(row['F13_conjugator'])
    assert v[0] in deleted;cores.add(v[0])
    ab=Counter()
    for a in sub(h,cut):ab[N['initial_order'][abs(a)-1]]+=1 if a>0 else -1
    ab={j:n for j,n in sorted(ab.items()) if n}
    assert ab=={int(j):n for j,n in row['physical_abelianization'].items()}
    assert len(ab)==2 and set(ab.values())=={1}
    tags=[N['labels'][j] for j in ab]
    assert {x['kind'] for x in tags}=={'A','B'}
    assert tags[0]['index']==tags[1]['index']
    assert {x['branch'] for x in tags}==({'w'} if row['sheet']==0 else {'v'})
    seeds.append({'sheet':row['sheet'],'critical_index':row['critical_index'],
                  'positive_F13_core':v[0],'F13_word_length':len(h13),
                  'physical_labels':ab,'coefficient_index':tags[0]['index'],
                  'branch':tags[0]['branch']})
    print('PASS source meridian',row['sheet'],row['critical_index'],
          'positive F13 core',v[0],'branch',tags[0]['branch'],'index',tags[0]['index'])
assert len(seeds)==8 and cores==deleted
for row in D['all36_returned_nodal_lifts']:
    h=tuple(row['h_F21'])
    assert sub(h,f13)==tuple(row['h_F13']) and not sub(h,f5)
    if not row['is_source_puncture']:assert not sub(h,f13)
assert len(D['old_source_generators'])==11 and len(D['all36_returned_nodal_lifts'])==36
assert sum(not x['is_source_puncture'] for x in D['all36_returned_nodal_lifts'])==28
assert 1+2*(24-1)==47 and 47-28==19 and 19-8==11
out={'scope':__doc__,'input_sha256':{n:hashlib.sha256(v).hexdigest() for n,v in raw.items()},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'source_actions':rows,'source_meridians':seeds,
     'exact_deleted_F13_indices':sorted(deleted),'regular_nodal_lifts':28,
     'elapsed_seconds':time.monotonic()-start,
     'claims_excluded':['source injection','source image equality','kappa vanishing','nonlinear fixed lifting']}
(ROOT/'work_A/symmetric_full_source_typing_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all36 nodal typings; eight cores are exactly all eight deleted F13 generators.')
print('Elapsed seconds',round(out['elapsed_seconds'],6))
