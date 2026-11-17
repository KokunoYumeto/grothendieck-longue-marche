#!/usr/bin/env python3
"""Independent full retained-deck normalization and augmentation certificate.

No producer is imported. Residual free generators are represented by their
literal (F5 head, peripheral slot), not by the producer's integer labels.
All raw paired Fox cells are normalized afresh and expanded back. The finite
certificate proves the diagonal-unit input to the separated-augmentation
injectivity argument; it does not invert an augmentation-one matrix.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/n for n in ['symmetric_paired_fox_data.json',
                     'symmetric_F_node_matching.json',
                     'symmetric_retained_deck_module.json',
                     'symmetric_G_augmentation_pivots.json',
                     'symmetric_F_cycles_and_fixed_chains.json']]
raw=[p.read_bytes() for p in paths]
paired,matching,data,pivots,halves=[json.loads(x) for x in raw]
start=time.monotonic()

def tred(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x: ans.pop()
        else: ans.append(int(x))
    return tuple(ans)
def tinv(w): return tuple(-x for x in reversed(w))
beta={int(k):tuple(v) for k,v in paired['retained_involution'].items()}
def tbeta(w):
    return tred(y for x in w for y in (beta[abs(x)] if x>0 else tinv(beta[abs(x)])))
assert beta=={1:(-1,),2:(4,),3:(5,),4:(2,),5:(3,)}

# A signed residual generator is (sign, retained_head, paired_slot).
def rred(w):
    out=[]
    for a in w:
        if out and out[-1]==(-a[0],a[1],a[2]): out.pop()
        else: out.append(a)
    return tuple(out)
def rinv(w): return tuple((-s,h,j) for s,h,j in reversed(w))
def ract(t,w): return rred((s,tred(t+h),j) for s,h,j in w)
def metadata(key):
    return {int(k):(tuple(v['retained_word']),v['paired_slot']) for k,v in key.items()}
metaraw=metadata(paired['finite_used_common_R_basis'])
metamatch=metadata(matching['common_R_basis'])
meta=metadata(data['common_R_basis'])
assert all(meta[k]==v for k,v in metaraw.items())
assert all(meta[k]==v for k,v in metamatch.items())
assert len(meta)==len(set(meta.values()))
def rw(w,md=meta):
    return rred((1 if x>0 else -1,*md[abs(x)]) for x in w)

ONE=((),(),())
def gm(a,b):
    u,v,t=a; x,y,s=b
    return rred(u+ract(t,x)),rred(v+ract(tbeta(t),y)),tred(t+s)
def gi(a):
    u,v,t=a; ti=tinv(t)
    return ract(ti,rinv(u)),ract(tbeta(ti),rinv(v)),ti
def gf(a): return a[1],a[0],tbeta(a[2])
def decode_g(a):
    return rw(a['A_word']),rw(a['B_word']),tuple(a['retained_word'])
def add(out,k,n):
    out[k]+=n
    if not out[k]: del out[k]
def rawchain(rows):
    out=defaultdict(int)
    for x in rows:
        a,b=metaraw[x['A_generator']],metaraw[x['B_generator']]
        key=(rw(x['A_vertex'],metaraw),rw(x['B_vertex'],metaraw),a,b)
        add(out,key,x['coefficient'])
    return dict(out)
def normalize(c):
    out=defaultdict(int)
    for (u,v,(g,i),(h,j)),n in c.items():
        z=tred(tinv(tbeta(g))+h)
        add(out,((i,j,z),(u,v,g)),n)
    return dict(out)
def expand(c):
    out=defaultdict(int)
    for ((i,j,z),(u,v,t)),n in c.items():
        add(out,(u,v,(t,i),(tred(tbeta(t)+z),j)),n)
    return dict(out)
def decode_column(col):
    out=defaultdict(int)
    for x in col['terms']:
        r=x['row']; row=(r['A_slot'],r['B_slot'],tuple(r['relative_retained_word']))
        add(out,(row,decode_g(x['G_coefficient'])),x['coefficient'])
    return dict(out)
def fchain(c):
    out=defaultdict(int)
    for ((i,j,z),a),n in c.items():
        add(out,((j,i,tinv(tbeta(z))),gm(gf(a),((),(),z))),-n)
    return dict(out)
def shift(c,a,sign=1):
    out=defaultdict(int)
    for (row,b),n in c.items(): add(out,(row,gm(a,b)),sign*n)
    return dict(out)
def augment(c):
    out=defaultdict(int)
    for (row,a),n in c.items(): add(out,(row,a[2]),n)
    return dict(out)

nodes=paired['node_columns']
assert len(nodes)==len(data['columns'])==64
keys=[(x['loop_index'],x['local_node_index']) for x in nodes]
cols=[]; augmented=[]
for i,(node,col) in enumerate(zip(nodes,data['columns'])):
    assert col['raw_seed_column']==i and tuple(col['node_index'])==keys[i]
    old=rawchain(node['fox_cells']); new=normalize(old)
    assert new==decode_column(col) and expand(new)==old
    assert expand(fchain(new))=={(v,u,b,a):-n for (u,v,a,b),n in old.items()}
    assert fchain(fchain(new))==new
    aug=augment(new); assert len(aug)==1
    (row,t),n=next(iter(aug.items())); assert n in (-1,1)
    declared=pivots['pivots'][i]
    r=declared['pivot_row']; unit=declared['diagonal_unit_lift']
    assert row==(r['A_slot'],r['B_slot'],tuple(r['relative_retained_word']))
    assert decode_g(unit)==((),(),t) and unit['coefficient']==n
    cols.append(new); augmented.append((row,t,n))
assert len({r for r,t,n in augmented})==64
slotpairs={(r[0],r[1]) for r,t,n in augmented}
slots=set(paired['deleted_right_slots'])
assert len(slots)==8 and slotpairs=={(i,j) for i in slots for j in slots}

# Select the 64 original rows, then augment the actual full entries.
rowindex={r:i for i,(r,t,n) in enumerate(augmented)}
matrix=defaultdict(int)
for j,c in enumerate(cols):
    for (r,a),n in c.items():
        if r in rowindex: add(matrix,(rowindex[r],j,a[2]),n)
assert dict(matrix)=={(i,i,t):n for i,(r,t,n) in enumerate(augmented)}

bykey=dict(zip(keys,cols))
rels={tuple(x['node_index']):x for x in data['all64_G_relations']}
match={tuple(x['node_index']):x for x in matching['rows']}
fixed=[]; count_terms=0
for k in keys:
    r=rels[k]; m=match[k]; mate=tuple(r['mate_index'])
    assert mate==tuple(m['physical_F_mate_index'])
    a=decode_g(r['G_coefficient'])
    expected=(rw(m['E_coefficient']['A_word'],metamatch),
              rw(m['E_coefficient']['B_word'],metamatch),tuple(m['retained_deck_F5']))
    assert a==expected
    sign=m['A_first_orientation_signs'][0]*m['A_first_orientation_signs'][1]
    assert sign==r['delta'] and sign in (-1,1)
    assert fchain(bykey[k])==shift(bykey[mate],a,-sign)
    am=decode_g(rels[mate]['G_coefficient'])
    assert gm(gf(a),am)==ONE and gm(a,gi(a))==gm(gi(a),a)==ONE
    for row,b in bykey[k]:
        assert gf(gm(a,b))==gm(gf(a),gf(b))
        assert gm(gi(a),gm(a,b))==b
        count_terms+=1
    if k==mate:
        assert sign==1
        fixed.append((k,a))
assert len(fixed)==8

# Independent normal forms in C2(tau)*C2(tau1)*F(s2,s3).
TAU,TAU1=101,102
def einv(x): return x if abs(x) in (TAU,TAU1) else -x
def er(w):
    out=[]
    for x in w:
        assert x not in (-TAU,-TAU1)
        if out and out[-1]==einv(x): out.pop()
        else: out.append(x)
    return tuple(out)
def ei(w): return tuple(einv(x) for x in reversed(w))
def embed(w):
    ims={1:(TAU1,TAU),2:(2,),3:(3,),4:(TAU,2,TAU),5:(TAU,3,TAU)}
    return er(y for x in w for y in (ims[abs(x)] if x>0 else ei(ims[abs(x)])))
for j in range(1,6):
    assert er((TAU,)+embed((j,))+(TAU,))==embed(beta[j])

savedfixed={tuple(x['node_index']):x for x in data['fixed_node_cocycles']}
savedhalves={tuple(x['node_index']):x for x in halves['fixed_cell_anti_chains']}
classifications=[]
for k,a in fixed:
    t=a[2]; word=er((TAU,)+embed(t)); assert er(word+word)==()
    core=word; prefix=[]
    while len(core)>1 and core[0]==einv(core[-1]):
        prefix.append(core[0]); core=core[1:-1]
    assert core in ((TAU,),(TAU1,))
    decl=savedfixed[k]
    assert tuple(decl['retained_free_product_word'])==word
    assert tuple(decl['retained_cone_core'])==core
    assert tuple(decl['retained_conjugating_prefix'])==tuple(prefix)
    assert er(tuple(prefix)+core+ei(prefix))==word
    neutral=core==(TAU,)
    assert neutral==(k[1]==1)
    if neutral:
        assert not t and a[1]==rinv(a[0])
        half=((),rinv(a[0]),())
        assert decode_g(decl['fixed_basis_point'])==half
        assert gm(gf(half),a)==half
        oldhalf=savedhalves[k]['E_half_translation']
        assert half==(rw(oldhalf['A_word']),rw(oldhalf['B_word']),())
        assert fchain(shift(bykey[k],half))==shift(bykey[k],half,-1)
    else:
        assert decl['fixed_basis_point'] is None
    classifications.append({'node':k,'cone_core':core,'neutral':neutral,
                            'retained_word':t,'prefix_length':len(prefix)})
assert sum(x['neutral'] for x in classifications)==4

out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'canonical_residual_letters':'(sign,F5 head,paired slot); no producer arithmetic imported',
     'raw_columns_reconstructed':64,'raw_two_chain_terms':sum(len(c) for c in cols),
     'distinct_augmentation_rows':64,'physical_pairs':'all8x8 once',
     'selected_augmented_matrix':'diagonal64x64 with exact group units',
     'F_word_relations':64,'F_coefficient_cycles':64,
     'semidirect_coefficient_checks':count_terms,'fixed_node_classes':classifications,
     'claims_excluded':['matrix invertibility','old-base orbit closure','I=R','full kappa vanishing'],
     'elapsed_seconds':time.monotonic()-start}
(HERE/'symmetric_G_span_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:64 raw paired columns independently normalized and expanded with canonical F5-head/slot words.')
print('PASS:all64 E-augmented columns are distinct units; selected64x64 matrix is diagonal; all8x8 slot pairs occur.')
print('PASS:64 full G-valued F relations/cycles and all2680 coefficient-semilinearity comparisons.')
print('PASS:eight retained involution cone classes:four neutral actual source half-chains, four nonneutral opposite-cone classes.')
print('Scope:finite exact inputs to full retained-deck injectivity/Tate proof; no old-base closure.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))
