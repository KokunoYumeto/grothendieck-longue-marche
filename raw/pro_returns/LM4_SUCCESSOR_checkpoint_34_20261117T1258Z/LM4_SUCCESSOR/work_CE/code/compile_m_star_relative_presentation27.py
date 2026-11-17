#!/usr/bin/env python3
"""Exact whole-input basis conversion; no orbit cutoff or quotient oracle."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json',
       ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json']
S,F=[json.loads(p.read_text()) for p in paths]

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return out

def inv(w): return [-x for x in w[::-1]]
def mul(*ws): return red(x for w in ws for x in w)
def sub(w,mp): return mul(*(mp[abs(x)] if x>0 else inv(mp[-x]) for x in w))
def comm(a,b): return mul(a,b,inv(a),inv(b))

# Original basis: a,B,d,e,f,bar-a,bar-B,bar-d,bar-e,g,x.
a,B,d,e,f,aa,BB,dd,ee,g,x=([i] for i in range(1,12))
new_names=['r','s','q','a','b','d','e','tau_a_tau','tau_b_tau','tau_d_tau','tau_e_tau']
z=mul(x,inv(aa),a)
p=mul(x,inv(aa),a,f)
q=mul(inv(a),aa,g,inv(x))
r=mul(x,g,inv(x))
s=mul(p,q)
b=mul(inv(a),aa,BB,inv(aa),a)
at=mul(x,aa,inv(x))
bt=mul(x,inv(aa),a,B,inv(a),aa,inv(x))
dt=mul(x,dd,inv(x));et=mul(x,ee,inv(x))
new_to_old=dict(enumerate([r,s,q,a,b,d,e,at,bt,dt,et],1))
assert mul(z,q)==r

# Simultaneous inverse, derived from the actual tau-Schreier basis.
r,s,q,a,b,d,e,at,bt,dt,et=([i] for i in range(1,12))
z=mul(r,inv(q));p=mul(s,inv(q))
x=mul(at,z,inv(a))
f=mul(inv(z),p);g=mul(inv(x),r,x)
aa=mul(inv(x),at,x)
BB=mul(inv(aa),a,b,inv(a),aa)
B=mul(inv(a),aa,inv(x),bt,x,inv(aa),a)
dd=mul(inv(x),dt,x);ee=mul(inv(x),et,x)
old_to_new=dict(enumerate([a,B,d,e,f,aa,BB,dd,ee,g,x],1))
for i in range(1,12):
    assert sub(new_to_old[i],old_to_new)==[i], ('new_inverse',i)
    assert sub(old_to_new[i],new_to_old)==[i], ('old_inverse',i)
print('PASS all22 literal basis inverse compositions.')

ops={}
for name,op in S['source_ordinary_actions'].items():
    op={int(i):w for i,w in op.items()}
    ops[name]={i:sub(sub(w,op),old_to_new) for i,w in new_to_old.items()}
for positive,negative in [('m','m_inverse'),('v','v_inverse')]:
    for i in range(1,12):
        assert sub(ops[positive][i],ops[negative])==[i]
        assert sub(ops[negative][i],ops[positive])==[i]
expected={i:[i] for i in range(1,12)};expected[1]=[-1,2]
expected_inverse={i:[i] for i in range(1,12)};expected_inverse[1]=[2,-1]
assert ops['m']==expected
assert ops['m_inverse']==expected_inverse
print('PASS complete actual m(r)=r^-1 s, with other10 fixed; all44 signed operator inverses.')

delta_old={int(i):w for i,w in S['selected_plus_involution'].items()}
delta={i:sub(sub(w,delta_old),old_to_new) for i,w in new_to_old.items()}
delta_expected={1:[3,-1,2,-3],2:[3,2,-3],3:[2,-3],
                4:[8],5:[9],6:[10],7:[11],8:[4],9:[5],10:[6],11:[7]}
assert delta==delta_expected
for i in range(1,12):
    assert sub(delta[i],delta)==[i]
    for name,op in ops.items():
        assert sub(delta[i],op)==sub(op[i],delta),(name,i)
print('PASS actual selected delta formula, delta^2 and all44 exact source/delta comparisons.')

node_rows=[]
for node in S['all20_orbifold_node_relations']:
    for sheet,w in enumerate(node['ordinary_two_sheets']):
        row=next(r for r in F['all40_node_factor_pairs']
                 if r['side']==node['side'] and r['name']==node['name'] and r['sheet']==sheet)
        first=row['first_factor']['word_F11'];second=row['second_factor']['word_F11']
        assert comm(first,second)==w
        nw=sub(w,old_to_new);nf=sub(first,old_to_new);ns=sub(second,old_to_new)
        assert comm(nf,ns)==nw
        assert sub(nw,new_to_old)==w
        node_rows.append({'side':node['side'],'name':node['name'],'sheet':sheet,
                          'word':nw,'first_factor':nf,'second_factor':ns,
                          'input_length':len(w),'output_length':len(nw)})
assert len(node_rows)==40
print('PASS all40 complete based node words/factor pairs/round trips.')

source=[]
for row in S['actual_six_source_normal_forms']:
    w=sub(row['fiber11'],old_to_new)
    assert sub(w,new_to_old)==row['fiber11']
    source.append({'name':row['name'],'fiber_word':w,'source_head':row['source_head']})
raw=[row['fiber_word'] for row in source[:4]]
A=mul(raw[0],inv(raw[3]),inv(raw[0]));B=mul(inv(A),inv(raw[0]),A)
D=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]));E=inv(raw[1])
contact_basis=dict(zip(('A_s','B_s','D_s','E_s'),(A,B,D,E)))

# The exact generic orbifold input is retained in its marked free-product basis.
# Global ordinary free11 to orbifold7 gives an independent diagram for the new basis.
o7={int(i):w for i,w in S['ordinary_fiber11_to_fiber7'].items()}
def orb_red(w):
    out=[]
    for x in w:
        if abs(x) in (6,7): x=abs(x)
        if out and (out[-1]==-x or (x in (6,7) and out[-1]==x)): out.pop()
        else: out.append(x)
    return out
def orb_mul(*ws): return orb_red(x for w in ws for x in w)
def orb_sub(w,mp): return orb_mul(*(mp[abs(x)] if x>0 else inv(mp[-x]) for x in w))
local={int(i):w for i,w in S['minus_local_to_global'].items()}
assert len(local)==7
# local7 is (a,b,d,e,f,C,tau), with selected tau fixed.
la,lb,ld,le,lf,C,tau=(local[i] for i in range(1,8))
u=orb_mul(C,lf)
oz=orb_mul(tau,C);op=orb_mul(tau,u);oq=orb_mul(u,tau)
orb_expected=[orb_mul(oz,oq),orb_mul(op,oq),oq,la,lb,ld,le,
              orb_mul(tau,la,tau),orb_mul(tau,lb,tau),
              orb_mul(tau,ld,tau),orb_mul(tau,le,tau)]
for i in range(1,12):
    assert orb_sub(new_to_old[i],o7)==orb_expected[i-1],('orb_diagram',i)
print('PASS all11 actual orbifold/ordinary marking diagrams and all6 source round trips.')

out={'status':'PASS_COMPLETE_M_STAR_RELATIVE_PRESENTATION',
     'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
     'new_basis_names':new_names,'new_basis_in_old_F11':new_to_old,
     'old_basis_in_new_F11':old_to_new,'signed_source_operators':ops,
     'selected_delta':delta,'all40_based_node_relations':node_rows,
     'actual_six_sources':source,'actual_contact_basis':contact_basis,
     'scope':'Exact entire input conversion. N remains the normal closure of all40 nodes under every signed word in m,v. No orbit truncation, filled graph-product claim, or new quotient.'}
dst=ROOT/'work_CE/next_symmetric_nodes/m_star_relative_presentation27.json'
dst.write_text(json.dumps(out,indent=2)+'\n')
for side in ('minus','plus'):
    rows=[r for r in node_rows if r['side']==side]
    print(side,'node lengths',[(r['name'],r['sheet'],r['output_length']) for r in rows])
print('Signed operator total lengths',{name:sum(map(len,op.values())) for name,op in ops.items()})
print('Actual contact lengths',{name:len(w) for name,w in contact_basis.items()})
