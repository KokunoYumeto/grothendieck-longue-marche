#!/usr/bin/env python3
"""Complete actual one-family filling; no source-orbit truncation."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/m_star_relative_presentation27.json',
       ROOT/'work_CE/next_symmetric_nodes/m_star_relative_face27.json']
D,F=[json.loads(p.read_text()) for p in paths]

def red(w,cones=()):
    out=[]
    for x in w:
        if abs(x) in cones:x=abs(x)
        if out and (out[-1]==-x or (x in cones and out[-1]==x)):
            out.pop()
        else:out.append(x)
    return out
def inv(w):return [-x for x in w[::-1]]
def mul(*ws,cones=()):return red((x for w in ws for x in w),cones)
def sub(w,mp,cones=()):
    return mul(*(mp[abs(x)] if x>0 else inv(mp[-x]) for x in w),cones=cones)
def con(h,w,cones=()):return mul(h,w,inv(h),cones=cones)
def comm(a,b,cones=()):return mul(a,b,inv(a),inv(b),cones=cones)

# Actual ordinary free basis (r,s,q,a,b,d,e,a*,b*,d*,e*).
keep={1:1,2:2,3:3,4:4,8:5}
proj={i:[keep[i]] if i in keep else [] for i in range(1,12)}
ops={}
for name,mp in D['signed_source_operators'].items():
    projected={i:sub(mp[str(i)],proj) for i in range(1,12)}
    assert all(not projected[i] for i in range(1,12) if i not in keep)
    op={keep[i]:projected[i] for i in keep}
    for i in range(1,12):assert sub(mp[str(i)],proj)==sub(proj[i],op)
    ops[name]=op
delta={keep[i]:sub(D['selected_delta'][str(i)],proj) for i in keep}
for i in range(1,12):
    assert sub(D['selected_delta'][str(i)],proj)==sub(proj[i],delta)
for name in ('m','v'):
    for i in range(1,6):
        assert sub(ops[name][i],ops[name+'_inverse'])==[i]
        assert sub(ops[name+'_inverse'][i],ops[name])==[i]
for i in range(1,6):
    assert sub(delta[i],delta)==[i]
    for op in ops.values():assert sub(op[i],delta)==sub(delta[i],op)
print('PASS all44 signed whole ordinary quotient diagrams,11 delta diagrams,20 inverse and20 source/delta checks.')

# Independently retain the complete local orbifold tuple a,b,d,e,f,C,tau.
# Its quotient is Z(a)*Z(f)*C2(C)*C2(tau), numbered1,2,3,4.
P={1:[1],2:[],3:[],4:[],5:[2],6:[3],7:[4]}
cones=(3,4)
orbi={}
for name,mp in F['all_four_source_operators_local7'].items():
    projected={i:sub(mp[str(i)],P,cones) for i in range(1,8)}
    assert projected[2]==projected[3]==projected[4]==[]
    op={1:projected[1],2:projected[5],3:projected[6],4:projected[7]}
    for i in range(1,8):assert sub(mp[str(i)],P,cones)==sub(P[i],op,cones)
    orbi[name]=op
assert orbi['m']=={1:[1],2:[-2,3,2,3,2],3:[-2,3,2],4:[4]}
assert orbi['v']=={1:[-2,1,2],2:[4,2,4],3:[-2,3,2],4:[4]}
for name in ('m','v'):
    for i in range(1,5):
        assert sub(orbi[name][i],orbi[name+'_inverse'],cones)==[i]
        assert sub(orbi[name+'_inverse'][i],orbi[name],cones)==[i]
print('PASS all28 actual signed orbifold quotient diagrams and16 inverse checks; both complete coarse actions contain no a.')

ordinary_nodes=[]
for row in D['all40_based_node_relations']:
    w=sub(row['word'],proj)
    a=sub(row['first_factor'],proj);b=sub(row['second_factor'],proj)
    assert w==comm(a,b)
    ordinary_nodes.append({k:row[k] for k in ('side','name','sheet')}|
                          {'word':w,'first_factor':a,'second_factor':b})
surviving=[r for r in ordinary_nodes if r['word']]
assert len(surviving)==4 and all(r['name']=='diagonal_a' for r in surviving)
orbifold_nodes=[]
for row in F['all20_node_relations_local7']:
    w=sub(row['word_local7'],P,cones)
    orbifold_nodes.append({'side':row['side'],'name':row['name'],'word':w})
surviving_o=[r for r in orbifold_nodes if r['word']]
assert len(surviving_o)==2 and all(r['name']=='diagonal_a' for r in surviving_o)
minus=comm([1],[3,1,3],cones)
plus=comm([1],[4,1,4],cones)
assert surviving_o[0]['side']=='minus' and surviving_o[0]['word']==minus
h=mul([1],[4,-1,4],[-1],cones=cones)
assert surviving_o[1]['side']=='plus' and surviving_o[1]['word']==con(h,plus,cones)
print('PASS every40 ordinary and20 orbifold node word/factor: precisely two orbifold a-diagonals survive, with exact plus conjugator.')

# Coarse section and stabilizer section are literal before imposing nodes.
coarse={1:[],2:[2],3:[3],4:[4]}
for name,op in orbi.items():
    for i in (2,3,4):assert all(abs(x)!=1 for x in op[i])
assert con([2],orbi['v'][1],cones)==[1]
assert orbi['m'][1]==[1]
print('PASS literal coarse section Q=<f,C,tau,m,v> and a-stabilizing source section H=<m,fv>.')

contacts={name:sub(w,proj) for name,w in D['actual_contact_basis'].items()}
raw_sources=[]
for row in D['actual_six_sources']:
    # Preserve actual schema without inferring a raw contact equals its node-reduced norm.
    raw_sources.append(row)
out={'status':'PASS_COMPLETE_ACTUAL_ONE_FAMILY_INPUT',
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
     'ordinary_basis':['r','s','q','a','a_star'],
     'ordinary_projection':proj,'signed_source_operators':ops,'delta':delta,
     'orbifold_basis':['a','f','C','tau'],'orbifold_projection':P,
     'signed_orbifold_operators':orbi,'all40_ordinary_nodes':ordinary_nodes,
     'all20_orbifold_nodes':orbifold_nodes,
     'two_normal_generators':{'minus':minus,'plus':plus},
     'literal_plus_node_conjugator':h,'projected_corrected_contacts':contacts,
     'scope':'Exact one-family quotient with every signed source/deck translate retained. The graph-product and fixed-subgroup arguments are separate uniform proofs; no finite orbit closure or faithfulness for the original group is inferred.'}
(ROOT/'work_CE/next_symmetric_nodes/one_family_face28.json').write_text(json.dumps(out,indent=2)+'\n')
print('Ordinary signed operator total lengths', {name:sum(map(len,op.values())) for name,op in ops.items()})
print('PASS saved complete one-family certificate.')
