#!/usr/bin/env python3
"""Independent bit-vector verification of frozen D63's finite comparison maps.

This does not import or execute an author program.  It reconstructs the four
Hom equations and every cross-action/norm from the recorded marked matrices.
The separate integral/source argument is reviewed in audit.md.
"""
from pathlib import Path
import hashlib, json

HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'D63_EXPERIMENTS'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((SRC/'ledger/d_compact_orthogonal_cross_manifest.json').read_text())
verified=[]
for r in manifest['owned_files']+manifest['immutable_inputs']:
    p=SRC/r['path'];assert sha(p)==r['sha256'],r['path'];verified.append(r['path'])
def load(s):return json.loads((SRC/'code'/s).read_text())
D=load('d_arithmetic_A4_twisted.json')
S=load('d_compact_splitting_maps.json')
C=load('d_all_compact_cross_norm.json')
def field_mul(a,b):
    p=0
    for j in range(2):
        if b&(1<<j):p^=a<<j
    if p&4:p^=7
    return p
mul=[[field_mul(a,b) for b in range(4)] for a in range(4)]
bar=[mul[a][a] for a in range(4)]
def rank(columns):
    basis={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k not in basis:basis[k]=x;break
            x^=basis[k]
    return len(basis)
def lin(columns,x):
    y=0
    while x:
        t=x&-x;y^=columns[t.bit_length()-1];x^=t
    return y
def pack(v):return sum(a<<(2*i) for i,a in enumerate(v))
def real_columns(cols,flip):
    return [pack([mul[v][bar[z] if flip else z] for v in col])
            for col in cols for z in (1,2)]
def xor_columns(arrays):
    ans=[0]*len(arrays[0])
    for cols in arrays:
        ans=[a^b for a,b in zip(ans,cols)]
    return ans
rows=[];all_action_columns=all_norm_relations=0
for rec in S['cases']:
    char=rec['character'];actual=next(x for x in D['character_blocks'] if x['character']==char)
    cross=next(x for x in C['cases'] if x['character']==char)
    flips={str(a['q_state']):a['flip'] for a in actual['all_stabilizer_actions']}
    E=rec['all_extra_actions'];M=rec['all_complement_actions'];P=rec['all_small_compact_actions']
    gens=[str(g) for g in rec['ordered_stabilizer_generators']]
    hom=[]
    for a in range(32):
        for b in range(4):
            for z in (1,2):
                value=0
                for k,g in enumerate(gens):
                    assert not flips[g]
                    coeff=[0]*128
                    for r in range(32):coeff[4*r+b]^=mul[E[g][a][r]][z]
                    for j in range(4):coeff[4*a+j]^=mul[z][P[g][j][b]]
                    value|=pack(coeff)<<(256*k)
                hom.append(value)
    assert rank(hom)==256
    norm_ranks=[]
    for name,n,expected in [('all_extra_actions',64,rec['extra_Sylow_norm_rank']),
                            ('all_complement_actions',32,rec['complement_Sylow_norm_rank']),
                            ('all_cusp_actions',96,rec['cusp_Sylow_norm_rank'])]:
        mats=rec[name]
        cols=xor_columns([real_columns(mats[str(g)],flips[str(g)])
                          for g in rec['unordered_Sylow_states']])
        assert len(cols)==n and rank(cols)==expected
        norm_ranks.append(expected)
    cross_results=[]
    for block,stored in enumerate(cross['cross_modules']):
        expected_actions=stored['all_stabilizer_action_columns']
        actions={};relations=[]
        for g in sorted(E,key=int):
            cols=[]
            for a in range(8):
                ev=E[g][8*block+a][8*block:8*block+8]
                for b in range(16):
                    mv=M[g][b]
                    outer=[mul[ev[i]][bar[mv[j]]] for i in range(8) for j in range(16)]
                    for z in (1,2):
                        zz=bar[z] if flips[g] else z
                        cols.append(pack([mul[v][zz] for v in outer]))
            assert cols==[int(x,16) for x in expected_actions[g]],(char,block,g)
            assert rank(cols)==256
            actions[g]=cols
            relations.extend(v^(1<<j) for j,v in enumerate(cols))
            all_action_columns+=len(cols)
        norm=xor_columns(list(actions.values()))
        assert norm==[int(x,16) for x in stored['all_norm_columns']]
        codim=256-rank(relations);nr=rank(norm)
        assert codim==nr==stored['norm_rank']==stored['coinvariant_dimension']
        assert all(lin(norm,v)==0 for v in relations)
        all_norm_relations+=len(relations)
        assert all([lin(cols,v) for v in norm]==norm for cols in actions.values())
        cross_results.append({'coinvariants':codim,'norm_rank':nr,
                              'global_dimension':len(actual['orbit'])*256})
    rows.append({'character':char,'Hom_F2_rank':256,'Sylow_norm_ranks_E_M_cusp':norm_ranks,
                 'cross_blocks':cross_results})
result={'status':'PASS','proof_sha256':sha(SRC/'sections/D_compact_orthogonal_cross.tex'),
        'manifest_sha256':sha(SRC/'ledger/d_compact_orthogonal_cross_manifest.json'),
        'manifest_files_verified':len(verified),'Hom_systems_reconstructed':4,
        'cross_action_columns_reconstructed':all_action_columns,
        'norm_relations_checked':all_norm_relations,'cases':rows,
        'total_cross_dimension':sum(b['global_dimension'] for r in rows for b in r['cross_blocks']),
        'total_cross_coinvariants':sum(b['coinvariants'] for r in rows for b in r['cross_blocks']),
        'excluded_mathematical_fields':[],
        'scope':'Independent standard-library arithmetic from the actual frozen matrices, plus manifest identity. No author full-program replay and no computational substitute for the integral/source proof are claimed.'}
assert result['total_cross_dimension']==40960 and result['total_cross_coinvariants']==52
text=json.dumps(result,indent=2)+'\n'
(HERE/'focused_maps.json').write_text(text);print(text,end='')
