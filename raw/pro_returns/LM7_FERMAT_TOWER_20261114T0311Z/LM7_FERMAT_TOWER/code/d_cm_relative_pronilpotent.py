#!/usr/bin/env python3
"""Exact marked common quotient for the D.41 PGL2(F7) residual.

Read the previously certified integral Bass--Serre graph, form its actual
order-54 relative-three quotient, and verify all quotient/homology maps
and the recorded D.39 odd conjugators over Z[1/2].  No prior executable
is imported, and no prior certificate is rewritten.
"""
from pathlib import Path
from collections import deque, Counter
import argparse, hashlib, json, time

ap = argparse.ArgumentParser()
ap.add_argument('--source-code', type=Path,
                default=Path(__file__).resolve().parents[2] / 'LM7_FERMAT_TOWER' / 'code')
args = ap.parse_args()
started = time.time()
OUT = Path(__file__).resolve().parent
D = json.loads((args.source_code/'d_cm_fermat_joint_base.json').read_text())
seed = json.loads((args.source_code/'d_cm_fermat_homology_seed.json').read_text())
Q = [tuple(q) for q in D['Q']]
LM = [tuple(sum(m, [])) for m in D['Q_linear_matrices']]
QI = {q:i for i,q in enumerate(Q)}
I = (1,0,0,1)
qi = QI[I]
def qm(a,b):
    v = ((a[0]*b[0]+a[1]*b[2])%12,
         (a[0]*b[1]+a[1]*b[3])%12,
         (a[2]*b[0]+a[3]*b[2])%12,
         (a[2]*b[1]+a[3]*b[3])%12)
    return min(v, tuple(-x%12 for x in v))
def qinv(q):
    return QI[min((q[3],-q[1]%12,-q[2]%12,q[0]),
                  (-q[3]%12,q[1],q[2],-q[0]%12))]
qt = [[QI[qm(a,b)] for b in Q] for a in Q]
O2Q = [i for i,q in enumerate(Q)
       if tuple(x%2 for x in q)==I
       and tuple(x%3 for x in qm(q,q)) in [(1,0,0,1),(2,0,0,2)]]
assert len(O2Q)==32
assert {qt[a][b] for a in O2Q for b in O2Q}==set(O2Q)
assert all(qt[qt[q][h]][qinv(Q[q])] in O2Q for q in range(576) for h in O2Q)
qcosets = []
qproj = [-1]*576
for q in [qi]+list(range(576)):
    if qproj[q]>=0:
        continue
    coset = sorted({qt[q][h] for h in O2Q})
    j = len(qcosets)
    qcosets.append(coset)
    for h in coset:
        assert qproj[h] in [-1,j]
        qproj[h]=j
assert len(qcosets)==18
q0t = [[qproj[qt[a[0]][b[0]]] for b in qcosets] for a in qcosets]
q0lm = [LM[a[0]] for a in qcosets]
assert all(LM[q]==q0lm[qproj[q]] for q in range(576))

oldstates = [tuple(h) for h in D['states']]
states=[]; lookup={}; projection=[]
for q,a,b in oldstates:
    key=(qproj[q],a%3,b%3)
    if key not in lookup:
        lookup[key]=len(states); states.append(key)
    projection.append(lookup[key])
assert states[0]==(0,0,0) and len(states)==54
def mul(a,b):
    q,u,v=states[a]; qq,x,y=states[b]; M=q0lm[q]
    return lookup[(q0t[q][qq],(u+M[0]*x+M[1]*y)%3,
                   (v+M[2]*x+M[3]*y)%3)]
table=[[mul(a,b) for b in range(54)] for a in range(54)]
inverse=[next(b for b in range(54) if table[a][b]==0) for a in range(54)]
s,r,t=(projection[D[k]] for k in ('s','r','t'))
assert table[s][s]==0 and table[table[r][r]][r]==0 and table[s][r]==t
rs=[row[s] for row in table]; rr=[row[r] for row in table]; rr2=[rr[a] for a in rr]
assert all(projection[D['right_s'][h]]==rs[projection[h]]
           and projection[D['right_r'][h]]==rr[projection[h]] for h in range(6912))
kernel=[h for h in range(6912) if projection[h]==0]
assert len(kernel)==128 and all(oldstates[h][0] in O2Q for h in kernel)
assert Counter(projection)==Counter({h:128 for h in range(54)})
def closure(gens):
    seen={0};todo=[0]
    for a in todo:
        for g in gens:
            b=table[a][g]
            if b not in seen:seen.add(b);todo.append(b)
    return seen
assert len(closure([s,r]))==54
even=closure([r,table[table[s][r]][s]])
assert len(even)==27 and s not in even
def order(h):
    q=h;n=1
    while q:
        n+=1;q=table[q][h]
    return n
assert all(order(h) in [1,3,9,27] for h in even)
q0s=states[s][0];q0r=states[r][0]
q0even={states[h][0] for h in even}
assert len(q0even)==9 and all(q0t[a][b]==q0t[b][a] for a in q0even for b in q0even)
assert all(q0t[q0t[a][a]][a]==0 for a in q0even)
q0kernel=[h for h in range(54) if states[h][0]==0]
assert len(q0kernel)==3
comm=lambda a,b:table[table[table[a][b]][inverse[a]]][inverse[b]]
even_derived=closure([comm(a,b) for a in even for b in even])
assert even_derived==set(q0kernel)
center=[a for a in even if all(table[a][b]==table[b][a] for b in even)]
assert set(center)==set(q0kernel)
full_center=[a for a in range(54) if all(table[a][b]==table[b][a] for b in (s,r))]
assert full_center==[0]
q0center=[a for a in range(18) if all(q0t[a][b]==q0t[b][a] for b in range(18))]
assert len(q0center)==3 and all(a in q0even for a in q0center)
aa=r;bb=table[table[s][r]][s];cc=comm(aa,bb)
def power(h,n):
    out=0
    for _ in range(n):out=table[out][h]
    return out
heisenberg={}
for a in range(3):
    for b in range(3):
        for c in range(3):
            heisenberg[(a,b,c)]=table[table[power(bb,b)][power(aa,a)]][power(cc,c)]
assert set(heisenberg.values())==even
for (a,b,c),v in heisenberg.items():
    assert table[table[s][v]][s]==heisenberg[(b,a,(a*b-c)%3)]
    for (A,B,C),w in heisenberg.items():
        assert table[v][w]==heisenberg[((a+A)%3,(b+B)%3,(c+C+a*B)%3)]

# A literal integral Bass--Serre basis of the new kernel of rank ten.
v2=[(0,min(h,rs[h])) for h in range(54)]
v3=[(1,min(h,rr[h],rr2[h])) for h in range(54)]
vertices=sorted(set(v2)|set(v3));vi={v:i for i,v in enumerate(vertices)}
adj=[[] for _ in vertices]
for h in range(54):
    a=vi[v2[h]];b=vi[v3[h]]
    adj[a].append((b,h,1));adj[b].append((a,h,-1))
root=vi[v2[0]];paths={root:[]};queue=deque([root]);tree=set()
while queue:
    a=queue.popleft()
    for b,h,sgn in adj[a]:
        if b not in paths:
            paths[b]=paths[a]+[(h,sgn)];tree.add(h);queue.append(b)
chords=[h for h in range(54) if h not in tree]
assert len(vertices)==45 and len(chords)==10 and len(paths)==45
cycles=[]
for h in chords:
    c=[0]*54
    for e,a in paths[vi[v2[h]]]+[(h,1)]+[(e,-a) for e,a in paths[vi[v3[h]]]]:
        c[e]+=a
    cycles.append(c)
assert all(c[chords[k]]==int(j==k) for j,c in enumerate(cycles) for k in range(10))
def boundary(c):
    out=[0]*45
    for h,z in enumerate(c):out[vi[v2[h]]]-=z;out[vi[v3[h]]]+=z
    return out
assert all(not any(boundary(c)) for c in cycles)
def project(v):
    out=[0]*54
    for h,z in enumerate(v):out[projection[h]]+=z
    return out
homology_map=[]
for col in D['integral_cycle_columns']:
    v=[0]*54
    for h,z in col:v[projection[h]]+=z
    assert not any(boundary(v))
    coeff=[v[h] for h in chords]
    assert v==[sum(coeff[j]*cycles[j][h] for j in range(10)) for h in range(54)]
    homology_map.append(coeff)
def rank_mod(rows,p):
    piv={}
    for row in rows:
        v=[x%p for x in row]
        for j in sorted(piv):
            if v[j]:
                a=v[j];v=[(x-a*y)%p for x,y in zip(v,piv[j])]
        if any(v):
            j=next(j for j,x in enumerate(v) if x)
            z=pow(v[j],-1,p);piv[j]=[(z*x)%p for x in v]
    return len(piv)
assert rank_mod(homology_map,3)==10

# Compute the exact normalized D.39 conjugators in Z[1/2]-paths here.
def model(w):
    h=0;P=[0]*54
    for a in w:
        if a==0:h=rs[h]
        else:
            k=rr[h] if a==1 else rr2[h]
            P[h]+=1;P[k]-=1;h=k
    return h,P
def act(P,h):
    out=[0]*54
    for e,z in enumerate(P):out[table[h][e]]+=z
    return out
def pairmul(a,b):
    v=act(b[1],a[0])
    return table[a[0]][b[0]],[x+y for x,y in zip(a[1],v)]
def invword(w):return [0 if a==0 else 3-a for a in reversed(w)]
xword=[2,0,2,0]
X=model(xword)
assert order(X[0])==3
t6=model([0,1]*6)
assert t6[0]==0 and not any(boundary(t6[1]))
t6coords=[t6[1][h] for h in chords]
assert any(z%3 for z in t6coords)
def corrected_twice(baseword,corr):
    h,p=model(baseword)
    out=[2*z for z in p]
    for z,col in zip(corr,homology_map):
        if z:
            for j,c in enumerate(col):
                if c:
                    for e,v in enumerate(cycles[j]):out[e]+=z*c*v
    return h,out
A=corrected_twice(seed['A_base_word'],seed['odd_A_correction_times2'])
beta=corrected_twice(seed['beta_base_word'],seed['odd_beta_correction_times2'])
g=model(invword(xword*6));g=(g[0],[2*z for z in g[1]])
A0=pairmul(g,A);beta0=pairmul(g,beta)
assert A0==(0,[0]*54)
assert beta0[0]==0 and not any(boundary(beta0[1]))
assert act(beta0[1],s)==beta0[1]
bc=[beta0[1][h] for h in chords]
assert beta0[1]==[sum(bc[j]*cycles[j][h] for j in range(10)) for h in range(54)]

# The actual joint source map to J=PGL2(F7) and H54.  Its kernel is
# M=N_J intersect L54, of index27 in N_J and free rank1513.
def pcanon(a,p):
    c=pow(next(x for x in a if x),-1,p)
    return tuple(c*x%p for x in a)
def pmul(a,b,p=7):
    return pcanon(((a[0]*b[0]+a[1]*b[2])%p,
                   (a[0]*b[1]+a[1]*b[3])%p,
                   (a[2]*b[0]+a[3]*b[2])%p,
                   (a[2]*b[1]+a[3]*b[3])%p),p)
js=(1,0,0,6);jr=(1,6,1,0)
JG=[I];JI={I:0}
for a in JG:
    for b in (js,jr):
        c=pmul(a,b)
        if c not in JI:JI[c]=len(JG);JG.append(c)
assert len(JG)==336
jrs=[JI[pmul(a,js)] for a in JG]
jrr=[JI[pmul(a,jr)] for a in JG]
assert len({min(h,jrs[h]) for h in range(336)})==168
assert len({min(h,jrr[h],jrr[jrr[h]]) for h in range(336)})==112
joint=[(0,0)];jindex={(0,0):0}
for a,b in joint:
    for aa,bb in ((jrs[a],rs[b]),(jrr[a],rr[b])):
        if (aa,bb) not in jindex:
            jindex[(aa,bb)]=len(joint);joint.append((aa,bb))
assert len(joint)==9072
assert {b for a,b in joint if a==0}==even
assert len({a for a,b in joint if b==0})==168
jsright=[jindex[(jrs[a],rs[b])] for a,b in joint]
jrright=[jindex[(jrr[a],rr[b])] for a,b in joint]
jr2right=[jrright[h] for h in jrright]
jv2=[(0,min(h,jsright[h])) for h in range(9072)]
jv3=[(1,min(h,jrright[h],jr2right[h])) for h in range(9072)]
jvertices=sorted(set(jv2)|set(jv3));jvi={v:i for i,v in enumerate(jvertices)}
jadj=[[] for _ in jvertices]
for h in range(9072):
    a=jvi[jv2[h]];b=jvi[jv3[h]]
    jadj[a].append((b,h,1));jadj[b].append((a,h,-1))
jroot=jvi[jv2[0]];jpaths={jroot:[]};jq=deque([jroot]);jtree=set()
while jq:
    a=jq.popleft()
    for b,h,z in jadj[a]:
        if b not in jpaths:
            jpaths[b]=jpaths[a]+[(h,z)];jtree.add(h);jq.append(b)
jchords=[h for h in range(9072) if h not in jtree]
assert len(jvertices)==7560 and len(jchords)==1513
omega=[];jcycle_sparse=[]
for h in jchords:
    edges={}
    for e,z in jpaths[jvi[jv2[h]]]+[(h,1)]+[(e,-z) for e,z in jpaths[jvi[jv3[h]]]]:
        edges[e]=edges.get(e,0)+z
    edges={e:z for e,z in edges.items() if z}
    assert edges.get(h)==1 and all(e==h or e in jtree for e in edges)
    v=[0]*54
    for e,z in edges.items():v[joint[e][1]]+=z
    assert not any(boundary(v))
    c=[v[e] for e in chords]
    assert v==[sum(c[j]*cycles[j][e] for j in range(10)) for e in range(54)]
    omega.append(c);jcycle_sparse.append(sorted(edges.items()))
assert rank_mod(omega,3)==10
summary={
    'Q_order':576,'O2_Q_order':32,'Q0_order':18,
    'original_H_order':6912,'O2_H_order':128,'marked_relative_three_base_order':54,
    'even_subgroup_order':27,'even_element_order_counts':dict(sorted(Counter(order(h) for h in even).items())),
    'even_center_order':len(center),'even_commutator_order':len(even_derived),
    'H54_center_order':len(full_center),
    'H54_is_actual_Heisenberg27_semidirect_swap':True,
    'projection_to_Q0_kernel_order':3,'free_kernel_rank':10,
    'cusp_order':order(t),'x_order':order(X[0]),
    'cusp_sixth_power_is_primitive_at3':True,
    'all_6912_generator_projection_equations_checked':True,
    'all_1153_integral_cycle_projection_equations_checked':True,
    'homology_projection_rank_mod3':10,
    'exact_odd_normalized_A_is_identity':True,
    'exact_odd_normalized_beta_is_s_centralizer':True,
    'normalized_beta_coordinates_times2':bc,
    'normalized_beta_is_identity':not any(bc),
    'new_PGL_kernel_rank':57,
    'joint_PGL_H54_order':len(joint),
    'joint_kernel_index_in_PGL_kernel':27,
    'joint_free_kernel_rank':1513,
    'all_1513_new_integral_cycle_projection_equations_checked':True,
    'new_pro3_kernel_map_to_Z3_10_rank':10,
    'scope':'Exact common relative-three homology quotient and recorded conjugator comparison. The full profinite source is not asserted to lift.',
    'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'Q_O2_indices':O2Q,'Q0_cosets':qcosets,
             'Q_to_Q0':qproj,'states':states,'table':table,'s':s,'r':r,'t':t,
             'H_to_H54':projection,'H54_O2_kernel_indices':kernel,
             'cycle_chords':chords,'cycle_columns':cycles,
             'Heisenberg_coordinate_map':[[*a,h] for a,h in heisenberg.items()],
             'cusp_sixth_power_coordinates':t6coords,
             'homology_projection_columns':homology_map,
             'normalized_beta_path_times2':beta0[1],
             'PGL2F7_elements':JG,'PGL_H54_joint_states':joint,
             'joint_cycle_chords':jchords,'joint_cycle_sparse_columns':jcycle_sparse,
             'omega_homology_columns':omega,
             'input_sha256':{name:hashlib.sha256((args.source_code/name).read_bytes()).hexdigest()
                             for name in ['d_cm_fermat_joint_base.json','d_cm_fermat_homology_seed.json']}}
(OUT/'d_cm_relative_pronilpotent.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
