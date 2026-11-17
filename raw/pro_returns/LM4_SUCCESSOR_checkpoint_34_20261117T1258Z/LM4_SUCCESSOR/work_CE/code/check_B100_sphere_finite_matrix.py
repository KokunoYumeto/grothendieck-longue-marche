#!/usr/bin/env python3
"""Independent bounded full-matrix check of the actual B100 sphere pair.

Uses explicit tuple group words, not the producers' persistent-DAG arithmetic.
The private node coefficient is(t^-1-1); multiplying by-t gives(t-1).
The two actual node rows are distinct. No full spherical-module vanishing.
"""
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
import json,hashlib,time

ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
FILES=[P/'actual_full21_Fox.json',P/'finite_even_boundary32.json',P/'finite_even_node_F2.json']
D,C,F2=[json.loads(p.read_text()) for p in FILES]
Tnodes=D['retained_word_DAG']+C['retained_word_DAG_append']+F2['retained_word_DAG_append']
Rnodes=D['R_word_DAG']+C['R_word_DAG_append']+F2['R_word_DAG_append']
rawgens=D['common_R_generators']+C['common_R_generators_append']+F2['common_R_generators_append']
rawG=D['group_elements']+C['group_elements_append']+F2['group_elements_append']


def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def read(nodes,p):
    out=[]
    while p:p,x,n=nodes[p];out.append(x)
    return tuple(reversed(out))
def mulword(a,b):return red((*a,*b))
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]


retlist=D['retained_paired_indices'];ret={j:i+1 for i,j in enumerate(retlist)}
beta={int(k):v[0] for k,v in D['retained_involution'].items()}
def bet(t):return tuple((1 if x>0 else-1)*beta[abs(x)] for x in t)
gens=[None]+[(read(Tnodes,g),i) for g,i in rawgens[1:]]
genindex={g:i for i,g in enumerate(gens) if i}
def gen(t,i):
    k=(tuple(t),i)
    if k not in genindex:genindex[k]=len(gens);gens.append(k)
    return genindex[k]
@lru_cache(None)
def unpack(g):
    a,b,t=rawG[g];return(read(Rnodes,a),read(Rnodes,b),read(Tnodes,t))
one=((),(),())
def shift(t,a):return tuple((1 if x>0 else-1)*gen(mulword(t,gens[abs(x)][0]),gens[abs(x)][1]) for x in a)
def multiply(a,b):
    u,v,t=a;x,y,s=b
    return(mulword(u,shift(t,x)),mulword(v,shift(bet(t),y)),mulword(t,s))
def Fg(g):a,b,t=g;return(b,a,bet(t))
def right(g,x):
    a,b,t=g;j=abs(x);sign=1 if x>0 else-1
    if j in ret:return(a,b,mulword(t,(sign*ret[j],)))
    if j<12:return(mulword(a,(sign*gen(t,j),)),b,t)
    return(a,mulword(b,(sign*gen(bet(t),j-10),)),t)
def evaluate(w):
    g=one
    for x in w:g=right(g,x)
    return g
def sub(w,images):return red(y for x in w for y in(images[x-1] if x>0 else inv(images[-x-1])))
def lift_t(t):return tuple((1 if x>0 else-1)*retlist[abs(x)-1] for x in t)
def representative(g):
    a,b,t=g;out=[]
    for side,w in [('A',a),('B',b)]:
        for x in w:
            h,i=gens[abs(x)];physical=h if side=='A' else bet(h)
            q=lift_t(physical);j=i if side=='A' else i+10
            out.extend(q);out.append((1 if x>0 else-1)*j);out.extend(inv(q))
    out.extend(lift_t(t));return red(out)


source=next(m for m in D['matrices'] if m['family']=='source' and m['name']=='old_0' and m['direction']=='push')
alpha=source['literal_F21_images']
si=next(r['index'] for r in C['source_generators'] if r['name']=='old_0')
assert si==1 and source['far_base_word']==[1]
@lru_cache(None)
def act(g):
    w=representative(g);assert evaluate(w)==g
    return evaluate(sub(w,alpha))


faces=C['faces'];nodes={(f['sheet'],tuple(f['node_index'])):i for i,f in enumerate(faces) if f['type']=='node'}
rect={(f['source_index'],f['paired_generator']):i for i,f in enumerate(faces) if f['type']=='source_rectangle'}
i=nodes[0,(6,3)];j=nodes[0,(6,7)]
r=tuple(faces[i]['literal_F21_word'])
assert r==(2,12,13,-12,-2,12,-13,-12)
assert sub(r,alpha)==r


started=time.monotonic()
# z=(t^-1-1)c_i - sum_j alpha(v_j)c_(t,j), v=Fox(r).
z=defaultdict(int);add(z,(i,one,-si),1);add(z,(i,one,0),-1)
for row,g,sw,n in faces[i]['boundary32']:
    assert sw==0
    add(z,(rect[si,row],act(unpack(g)),0),-n)


def boundary(chain):
    out=defaultdict(int)
    for(face,g,w),n in chain.items():
        for row,h,sw,m in faces[face]['boundary32']:
            b=unpack(h);v=-sw # finite matrix table sw means s_sw^-1
            if w==0:product=multiply(g,b);base=v
            else:
                assert w==-si and v==0
                product=multiply(g,act(b));base=w
            add(out,(row,product,base),n*m)
    return dict(out)
assert not boundary(z)

# Exact actual two-face action, from the separately certified physical
# conjugators and source-rectangle reversal, with no arbitrary lifting.
face_action={}
for a in C['source_face_F']:
    face_action[rect[a['source_index'],a['paired_generator']]]=(rect[a['source_index'],a['target_paired_generator']],unpack(a['coefficient_G_id']),a['sign'])
for a in F2['records']:
    face_action[a['face_index']]=(a['mate_face_index'],unpack(a['coefficient_G_id']),a['raw_cell_sign'])
assert len(face_action)==359
def Fchain(chain):
    out=defaultdict(int)
    for(face,g,w),n in chain.items():
        target,h,sign=face_action[face]
        if w==0:product=multiply(Fg(g),h)
        else:
            assert w==-si
            product=multiply(Fg(g),act(h))
        add(out,(target,product,w),n*sign)
    return dict(out)
fz=Fchain(z);assert not boundary(fz)
assert Fchain(fz)==dict(z)

znodes={face for(face,g,w) in z if faces[face]['type']=='node'}
fznodes={face for(face,g,w) in fz if faces[face]['type']=='node'}
assert znodes=={i} and fznodes=={j} and i!=j
h=face_action[i][1]
assert face_action[i][0]==j and face_action[i][2]==1
assert evaluate((12,-14,-12))==h
assert{(g,w):n for(face,g,w),n in z.items() if face==i}=={(one,-si):1,(one,0):-1}
assert{(g,w):n for(face,g,w),n in fz.items() if face==j}=={(act(h),-si):1,(h,0):-1}


def pack(chain):
    return [{'face_index':face,'G_coefficient':{'A_word':a,'B_word':b,'retained_word':t},
             'source_word':[] if not w else[w],'coefficient':n}
            for(face,(a,b,t),w),n in sorted(chain.items())]
out={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in FILES},
 'common_R_basis':{str(k):{'retained_word':g,'paired_slot':s} for k,(g,s) in enumerate(gens[1:],1)},
 'actual_relator':r,'source_name':'old_0','source_index':si,
 'sphere_formula':'z_minus=(t^-1-1)c_i - sum alpha(v_j)c_(t,j), v=Fox_G(r_i), alpha(r_i)=r_i literally',
 'positive_private_coefficient_version':'-t*z_minus has private coefficient(t-1)',
 'node_index':[6,3],'mate_index':[6,7],'mate_conjugator_F21':[12,-14,-12],
 'raw_F_sign':1,'z':pack(z),'Fz':pack(fz),
 'entire_boundary_z_zero':True,'entire_boundary_Fz_zero':True,'F_squared_z':True,
 'private_node_rows_distinct':True,
 'free_pair_proof':'A finite coefficient satisfying a*(t^-1-1)=0 is invariant under right multiplication by infinite-order t, hence zero. The other private row has coefficient(t^-1-1)*h, with h a group unit. Distinct private node rows therefore give a freeLambda rank2 pair. F exchanges z,Fz semilinearly, so its underlying integral C2-module is induced and all its Tate cohomology vanishes.',
 'claims_excluded':['all of S_sph is this pair','all spherical Tate classes vanish','kappa vanishes on all syzygies','full centralizer equality'],
 'counts':{'z_terms':len(z),'Fz_terms':len(fz)},'elapsed_seconds':time.monotonic()-started}
(P/'B100_sphere_finite_matrix.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS actual fixed relator, complete z/Fz32-row boundaries and F^2')
print('PASS distinct private node rows(6,3)/(6,7), actual h=p12*p14^-1*p12^-1')
print('COUNTS',out['counts']);print('DONE elapsed',round(out['elapsed_seconds'],3))
