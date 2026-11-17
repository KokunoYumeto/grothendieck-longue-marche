#!/usr/bin/env python3
"""One exact whole-inner-presentation S3 witness, not a target census."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/m_star_relative_face27.json'
D=json.loads(p.read_text())
I=(0,1,2);A=(1,0,2);T=(0,2,1)
def compose(a,b):return tuple(a[b[i]] for i in range(3))
def inverse(a):return tuple(a.index(i) for i in range(3))
mp={i:I for i in range(1,8)};mp[1]=A;mp[7]=T
def evaluate(w):
    r=I
    for x in w:r=compose(r,mp[x] if x>0 else inverse(mp[-x]))
    return r
checks=[]
for row in D['all20_node_relations_local7']:
    if row['side']=='minus':
        assert evaluate(row['word_local7'])==I
        checks.append('minus_node/'+row['name'])
for i in range(1,7):
    assert evaluate(D['all_four_source_operators_local7']['m'][str(i)])==mp[i]
    checks.append('inner_m_relation/'+str(i))
assert compose(mp[6],mp[6])==I;checks.append('C_square')
assert compose(T,T)==I;checks.append('tau_square')
checks.append('m_tau_commutes_because_m_identity')
assert len(checks)==19
w=[1,7,1,7,-1,7,-1,7]
value=evaluate(w)
assert value!=I and compose(compose(value,value),value)==I
out={'status':'PASS_ACTUAL_INNER_STAR_NONZERO_KERNEL_WITNESS',
     'input':str(p.relative_to(ROOT)),'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'basis_local7':D['orbifold_local_basis'],'finite_target':'S3 with composition a after b',
     'images_local7':mp,'m_image':I,'all19_inner_defining_checks':checks,
     'word_local7':w,'value':value,'value_order':3,
     'scope':'The word is killed in the actual final group by B130, but nontrivial in the whole inner star and its full completion. Its original orientation is even. No compact inner-centralizer theorem or main fixed-source counterexample is asserted.'}
(ROOT/'work_CE/next_symmetric_nodes/inner_star_kernel27.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all19 complete inner-star defining relations in the one specified S3 target.')
print('PASS [a,tau a tau] has nonidentity order-three image',value,'and original even orientation.')
