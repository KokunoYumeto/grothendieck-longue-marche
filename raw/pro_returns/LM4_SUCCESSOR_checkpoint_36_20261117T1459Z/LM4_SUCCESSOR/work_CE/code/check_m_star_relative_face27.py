#!/usr/bin/env python3
"""Whole relative star input and an actual filled Z^3 face; no target search."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json',
       ROOT/'work_CE/next_symmetric_nodes/m_star_relative_presentation27.json',
       ROOT/'work_CE/B130_actual_source_commutator_proposed.tex']
S,D=[json.loads(p.read_text()) for p in paths[:2]]
def red(w,cones=()):
    out=[]
    for x in w:
        if abs(x) in cones:x=abs(x)
        if out and (out[-1]==-x or (x in cones and out[-1]==x)):out.pop()
        else:out.append(x)
    return out
def inv(w):return [-x for x in w[::-1]]
def mul(*ws,cones=()):return red((x for w in ws for x in w),cones)
def sub(w,mp,cones=()):return mul(*(mp[abs(x)] if x>0 else inv(mp[-x]) for x in w),cones=cones)
def conj(a,w,cones=()):return mul(a,w,inv(a),cones=cones)
def ab(w):return [sum(1 if x>0 else -1 for x in w if abs(x)==i) for i in range(1,12)]
CONES=(6,7)
local_in={int(i):w for i,w in S['minus_global_to_local'].items()}
local_out={int(i):w for i,w in S['minus_local_to_global'].items()}
far={nm:{int(i):w for i,w in op.items()} for nm,op in S['far_orbifold_actions'].items()}
corr=S['actual_source_v_correction_fiber7']
v={i:conj(corr,far['p'][i],CONES) for i in range(1,8)}
vi={i:sub(conj(inv(corr),[i],CONES),far['p_inverse'],CONES) for i in range(1,8)}
for i in range(1,8):
    assert sub(v[i],vi,CONES)==[i]
    assert sub(vi[i],v,CONES)==[i]
assert v[7]==vi[7]==[7]
local_ops={}
for name,op in [('m',far['m']),('m_inverse',far['m_inverse']),('v',v),('v_inverse',vi)]:
    local_ops[name]={i:sub(sub(local_out[i],op,CONES),local_in,CONES) for i in range(1,8)}
assert local_ops['m']=={1:[1],2:[2],3:[3],4:[4],5:[-5,6,5,6,5],6:[-5,6,5],7:[7]}
# All four full orbifold operators reproduce the independently compiled ordinary arrays.
old11_to7={int(i):w for i,w in S['ordinary_fiber11_to_fiber7'].items()}
new11_to_old={int(i):w for i,w in D['new_basis_in_old_F11'].items()}
new11_to_local7={i:sub(sub(w,old11_to7,CONES),local_in,CONES) for i,w in new11_to_old.items()}
for name,op in local_ops.items():
    for i in range(1,12):
        assert sub(new11_to_local7[i],op,CONES)==sub(D['signed_source_operators'][name][str(i)],new11_to_local7,CONES)
print('PASS all14 actual orbifold v inverses and44 whole ordinary/orbifold source diagrams.')
regional=[]
for row in S['all20_orbifold_node_relations']:
    w=sub(row['orbifold_fiber7'],local_in,CONES)
    if row['side']=='minus':assert all(abs(x)!=7 for x in w)
    regional.append({'side':row['side'],'name':row['name'],'word_local7':w})
assert len([r for r in regional if r['side']=='minus'])==10
assert len([r for r in regional if r['side']=='plus'])==10
print('PASS complete two regional lists; all10 minus nodes lie in the first cone factor.')

# Character certificate, not a word oracle for the already proved B130 norm block.
matrix={}
expected=[[int(i==j) for j in range(1,12)] for i in range(1,12)]
expected[0]=[-1,1]+[0]*9
for name in ('m','v'):
    matrix[name]=[ab(D['signed_source_operators'][name][str(i)]) for i in range(1,12)]
    assert matrix[name]==expected
for name in ('m','m_inverse','v','v_inverse'):
    for i in range(1,12):
        w=D['signed_source_operators'][name][str(i)]
        assert (ab(w)[3],ab(w)[7])==(int(i==4),int(i==8))
for i in range(1,12):
    w=D['selected_delta'][str(i)]
    assert (ab(w)[3],ab(w)[7])==(int(i==8),int(i==4))
for name in ('m','m_inverse'):
    assert D['signed_source_operators'][name]['4']==[4]
    assert D['signed_source_operators'][name]['8']==[8]
for row in D['all40_based_node_relations']:assert ab(row['word'])==[0]*11
contact_chars={name:[ab(w)[3],ab(w)[7],0] for name,w in D['actual_contact_basis'].items()}
assert contact_chars=={'A_s':[1,1,0],'B_s':[0,0,0],'D_s':[0,0,0],'E_s':[0,0,0]}
print('PASS actual m/v abelian matrices, all40 node characters, delta swap and four contact characters.')

# Universal direct-product calculation of the particular cross consequence.
# In F(V,A) x F(Vdelta,Adelta), a=V A^-1 V^-1 and delta(a)=Vdelta Adelta^-1 Vdelta^-1.
aa=[1,-2,-1];daa=[3,-4,-3]
cross=mul(aa,daa,inv(aa),inv(daa))
assert red(x for x in cross if abs(x)<=2)==[]
assert red((1 if x>0 else -1)*(abs(x)-2) for x in cross if abs(x)>2)==[]
print('PASS universal B130 cross consequence [a,delta(a)]=1; combined with literal m fixation gives Z^3 section.')

out={'status':'PASS_COMPLETE_RELATIVE_STAR_AND_ACTUAL_RETRACTED_FACE',
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
     'orbifold_local_basis':['a','b','d','e','f','C','tau'],
     'all_four_source_operators_local7':local_ops,
     'all20_node_relations_local7':regional,
     'm_v_abelian_matrices':matrix,
     'retraction_coordinates':['exponent(a)','exponent(tau_a_tau)','source_m_exponent'],
     'section_generators_new_F11_and_source':{'a':[4],'tau_a_tau':[8],'m':'m'},
     'contact_images':contact_chars,
     'scope':'The commutation [a,delta(a)] uses the fully proved actual B130 four-cross block. Character checks then prove an actual equivariant Z^3 retract. The entire remaining plus-node/v presentation is retained; no total centralizer equality.'}
(ROOT/'work_CE/next_symmetric_nodes/m_star_relative_face27.json').write_text(json.dumps(out,indent=2)+'\n')
