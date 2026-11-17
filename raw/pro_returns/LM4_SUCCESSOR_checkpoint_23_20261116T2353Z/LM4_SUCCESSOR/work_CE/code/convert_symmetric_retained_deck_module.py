#!/usr/bin/env python3
"""Exact conversion to G=E semidirect F5 coefficients.

This incorporates ALL retained F5 deck translates, not a bounded orbit
sample. It certifies the free product-tree row basis, arithmetic, all64
F-mate relations, and the8 fixed-node coefficient-cocycle tests. It does
not prove independence of the64 resulting seed columns.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_paired_fox_data.json',P/'symmetric_F_node_matching.json']
raw=[p.read_bytes() for p in paths]
paired,matching=[json.loads(r) for r in raw]

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)

def inv(w):return tuple(-x for x in reversed(w))

def sub(w,A):
    return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))

beta={int(i):tuple(w) for i,w in paired['retained_involution'].items()}
meta={int(i):(tuple(r['retained_word']),r['paired_slot'])
      for i,r in matching['common_R_basis'].items()}
idx={v:i for i,v in meta.items()}

def bid(g,i):
    if (g,i) not in idx:
        k=max(meta,default=0)+1;idx[g,i]=k;meta[k]=(g,i)
    return idx[g,i]

def act(w,t):
    return red((1 if x>0 else -1)*bid(red(t+meta[abs(x)][0]),meta[abs(x)][1]) for x in w)

ONE=((),(),())

def gm(a,b):
    u,v,t=a;x,y,s=b
    return red(u+act(x,t)),red(v+act(y,sub(t,beta))),red(t+s)

def gi(a):
    u,v,t=a;s=inv(t)
    return act(inv(u),s),act(inv(v),sub(s,beta)),s

def gf(a):
    u,v,t=a
    return v,u,sub(t,beta)

def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]

def decode(rows):
    return {(tuple(r['A_vertex']),tuple(r['B_vertex']),r['A_generator'],r['B_generator']):r['coefficient']
            for r in rows}

def normalize(c):
    out=defaultdict(int)
    for (u,v,i,j),n in c.items():
        g,slot_i=meta[i];h,slot_j=meta[j]
        z=red(inv(sub(g,beta))+h)
        add(out,((slot_i,slot_j,z),(u,v,g)),n)
    return dict(out)

def expand(c):
    out=defaultdict(int)
    for ((i,j,z),(u,v,t)),n in c.items():
        ai=bid(t,i);bj=bid(red(sub(t,beta)+z),j)
        add(out,(u,v,ai,bj),n)
    return dict(out)

def Fchain_raw(c):return {(v,u,j,i):-n for (u,v,i,j),n in c.items()}

def Fchain(c):
    out=defaultdict(int)
    for ((i,j,z),a),n in c.items():
        row=(j,i,inv(sub(z,beta)))
        coeff=gm(gf(a),((),(),z))
        add(out,(row,coeff),-n)
    return dict(out)

def shift(c,a,sign=1):
    out=defaultdict(int)
    for (row,b),n in c.items():add(out,(row,gm(a,b)),sign*n)
    return dict(out)

def encode(c):
    return [{'row':{'A_slot':i,'B_slot':j,'relative_retained_word':z},
             'G_coefficient':{'A_word':u,'B_word':v,'retained_word':t},'coefficient':n}
            for ((i,j,z),(u,v,t)),n in sorted(c.items())]

TAU,TAU1=101,102

def einv(x):return x if x in (TAU,TAU1) else -x

def er(w):
    out=[]
    for x in w:
        if out and out[-1]==einv(x):out.pop()
        else:out.append(x)
    return tuple(out)

def ei(w):return tuple(einv(x) for x in reversed(w))

def eembed(w):
    out=[]
    for x in w:
        i=abs(x)
        q=(TAU1,TAU) if i==1 else ((i,) if i in (2,3) else (TAU,i-2,TAU))
        out.extend(q if x>0 else ei(q))
    return er(out)

start=time.monotonic()
nodes=paired['node_columns']
keys=[(r['loop_index'],r['local_node_index']) for r in nodes]
lookup={tuple(r['node_index']):r for r in matching['rows']}
base=[decode(r['fox_cells']) for r in nodes]
cols=[normalize(c) for c in base]
bykey=dict(zip(keys,cols))
for k,c,rawc in zip(keys,cols,base):
    assert expand(c)==rawc,('row inverse',k)
    assert Fchain(c)==normalize(Fchain_raw(rawc)),('F row normalization',k)
    assert Fchain(Fchain(c))==c,('F square',k)

relations=[];fixed=[];arithmetic_samples=[]
for k in keys:
    row=lookup[k];mu=tuple(row['physical_F_mate_index'])
    g=(tuple(row['E_coefficient']['A_word']),tuple(row['E_coefficient']['B_word']),
       tuple(row['retained_deck_F5']))
    mr=lookup[mu]
    gm_mu=(tuple(mr['E_coefficient']['A_word']),tuple(mr['E_coefficient']['B_word']),
           tuple(mr['retained_deck_F5']))
    delta=row['A_first_orientation_signs'][0]*row['A_first_orientation_signs'][1]
    assert gm(g,gi(g))==ONE and gm(gi(g),g)==ONE
    assert gf(gf(g))==g
    assert gm(gf(g),gm_mu)==ONE,('coefficient cycle',k)
    rhs=shift(bykey[mu],g,-delta)
    assert Fchain(bykey[k])==rhs,('whole G relation',k)
    # The semidirect action checked on each actual coefficient in this
    # entire transformed column, rather than on a few example letters.
    for (_,a),n in bykey[k].items():
        assert gf(gm(g,a))==gm(gf(g),gf(a))
        assert gm(gi(g),gm(g,a))==a
    relations.append({'node_index':k,'mate_index':mu,'delta':delta,
                      'G_coefficient':{'A_word':g[0],'B_word':g[1],'retained_word':g[2]},
                      'relation':'F(C_nu)=-delta*g_nu*C_mu',
                      'original_domain_relation':'f_nu+delta*g_nu*e_mu=0'})
    arithmetic_samples.append(g)
    if k==mu:
        t=g[2];tau_t=er((TAU,)+eembed(t))
        assert er(tau_t+tau_t)==()
        prefix=[];core=tau_t
        while len(core)>1 and core[0]==einv(core[-1]):
            prefix.append(core[0]);core=core[1:-1]
        assert core in ((TAU,),(TAU1,))
        if core==(TAU,):
            assert not t and g[1]==inv(g[0])
            half=((),inv(g[0]),())
            assert gm(gf(half),g)==half
            classification='neutral: explicit fixed coefficient basis point'
        else:
            half=None
            classification='nonneutral: retained involution lies in the other cone class'
        fixed.append({'node_index':k,'retained_cocycle':t,'retained_free_product_word':tau_t,
                      'retained_conjugating_prefix':prefix,'retained_cone_core':core,
                      'classification':classification,
                      'fixed_basis_point':None if half is None else {'A_word':half[0],'B_word':half[1],'retained_word':half[2]}})
assert len(fixed)==8
assert sum(r['fixed_basis_point'] is not None for r in fixed)==4

# Additional exact associativity/semidirect consistency on the64 actual
# coefficient triples, using adjacent cyclic triples, not random tests.
for i in range(64):
    a,b,c=(arithmetic_samples[(i+j)%64] for j in range(3))
    assert gm(gm(a,b),c)==gm(a,gm(b,c))

out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'group':'G=(R_A x R_B) semidirect F5',
     'multiplication':'(u,v,t)(x,y,s)=(u alpha_t(x),v alpha_beta(t)(y),ts)',
     'R_index_action':'alpha_t(g,slot)=(tg,slot)',
     'involution':'F(u,v,t)=(v,u,beta(t))',
     'row_normalization':'(u,v;(g,i),(h,j)) -> coefficient(u,v,g), row(i,j,beta(g)^-1 h)',
     'row_involution':'F(row(i,j,z))=-D_z row(j,i,beta(z)^-1)',
     'common_R_basis':{i:{'retained_word':g,'paired_slot':j} for i,(g,j) in meta.items()},
     'columns':[{'node_index':k,'raw_seed_column':i,'terms':encode(c)} for i,(k,c) in enumerate(zip(keys,cols))],
     'all64_G_relations':relations,'fixed_node_cocycles':fixed,
     'counts':{'seed_columns':64,'distinct_G_rows':len({row for c in cols for row,a in c}),
               'nonzero_seed_terms':sum(len(c) for c in cols),'R_dictionary_size':len(meta),
               'fixed_physical_nodes':8,'neutral_fixed_nodes':4,'other_cone_fixed_nodes':4},
     'claims_excluded':['independence of seed columns','full old-base translates','I=R'],
     'elapsed_seconds':time.monotonic()-start}
(P/'symmetric_retained_deck_module.json').write_text(json.dumps(out,indent=2)+'\n')
for r in fixed:print('PASS fixed node',r['node_index'],'core',r['retained_cone_core'],r['classification'])
print('PASS64 full G relations, row arithmetic and inverse expansion, all64 coefficient cycles; counts',out['counts'],
      'elapsed',round(out['elapsed_seconds'],3))
