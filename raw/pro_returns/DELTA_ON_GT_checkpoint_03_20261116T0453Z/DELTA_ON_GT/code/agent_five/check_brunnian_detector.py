"""Exact Brunnian obstruction for the induced five-point detector.

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_brunnian_detector.py
"""
from fractions import Fraction
from itertools import product
import json

def red(w):
    s=[]
    for x in w:
        if s and s[-1]==-x:s.pop()
        else:s.append(x)
    return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def comm(a,b):return red(a+b+inv(a)+inv(b))
def subst(images,w):
    v=()
    for x in w:v=red(v+(images[abs(x)-1] if x>0 else inv(images[-x-1])))
    return v
def compose(a,b):return tuple(subst(a,w) for w in b)
def artin(n,w):
    ans=tuple((i,) for i in range(1,n+1))
    for x in w:
        i=abs(x);g=[(j,) for j in range(1,n+1)]
        if x>0:g[i-1],g[i]=(i,i+1,-i),(i,)
        else:g[i-1],g[i]=(i+1,),(-(i+1),i,i+1)
        ans=compose(ans,tuple(g))
    return ans

# Xi=(x12,x23,x34,x45,x51) in the label-five stabilizer B4/<z4>.
X=((1,1),(2,2),(3,3),(1,2,1)*2,(3,2,3)*2)
W=comm(comm(X[0],X[1]),comm(X[2],X[3]))
aw=artin(4,W)
assert aw!=tuple((i,) for i in range(1,5))
assert sum(1 if t>0 else -1 for t in W)==0

# q5 sends Xi to (x,y,x,1,1); every other q_i is a cyclic rotation.
pattern=((1,),(2,),(1,),(),())
f=comm((1,),(2,))  # a concrete 2-cycle word, used only to check substitutions.
assert subst(((2,),(1,)),f)==inv(f)
edges=((2,3),(4,0),(1,2),(3,4),(0,1))
forgetting=[]
for k in range(5):
    p=tuple(pattern[(j-k)%5] for j in range(5))
    values=[subst((p[i],p[j]),f) for i,j in edges]
    total=()
    for v in values:total=red(total+v)
    assert total==()
    nontrivial=[v for v in values if v]
    assert len(nontrivial)==2 and nontrivial[0]==inv(nontrivial[1])
    bw=comm(comm(p[0],p[1]),comm(p[2],p[3]))
    assert bw==()
    forgetting.append({'rotation':k,'pattern':p,'surviving_f_arguments':
                       [(p[i],p[j]) for i,j in edges if p[i] and p[j] and p[i]!=p[j]],
                       'pentagon_cancels_by_2_cycle':True,'brunnian_word_maps_to_one':True})

# Finite Burau specialization of B4/<z4> at t=2 in F5.
# Start with the unreduced 4-dimensional Burau action and quotient by
# its fixed vector (1,1,1,1), using e1,e2,e3 as quotient basis.
def mm(a,b,p):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%p for j in range(3))for i in range(3))
def mi(a,p):
    m=[[int(a[i][j])%p for j in range(3)]+[int(i==j) for j in range(3)] for i in range(3)]
    for j in range(3):
        r=next(i for i in range(j,3) if m[i][j]);m[j],m[r]=m[r],m[j]
        c=pow(m[j][j],-1,p);m[j]=[(x*c)%p for x in m[j]]
        for i in range(3):
            if i!=j:
                c=m[i][j];m[i]=[(x-c*y)%p for x,y in zip(m[i],m[j])]
    return tuple(tuple(row[3:]) for row in m)
I=((1,0,0),(0,1,0),(0,0,1))
def burau(p,t):
    return (((1-t,t,0),(1,0,0),(0,0,1)),((1,0,0),(0,1-t,t),(0,1,0)),((1,0,-1),(0,1,-1),(0,0,-t)))
def evalmat(g,w,p):
    a=I
    for i in w:a=mm(a,g[i-1] if i>0 else mi(g[-i-1],p),p)
    return a
g=burau(5,2)
assert evalmat(g,(1,2,1),5)==evalmat(g,(2,1,2),5)
assert evalmat(g,(2,3,2),5)==evalmat(g,(3,2,3),5)
assert evalmat(g,(1,3),5)==evalmat(g,(3,1),5)
assert evalmat(g,(1,2,3)*4,5)==I
BW=evalmat(g,W,5)
pentagon_comm=()
for i,j in edges:pentagon_comm=red(pentagon_comm+comm(X[i],X[j]))
PC=evalmat(g,pentagon_comm,5)
affine=(((1,1,0),(0,1,0),(0,0,1)),
        ((1,0,0),(-1,1,0),(0,0,1)),
        ((1,1,1),(0,1,0),(0,0,1)))
for p in (2,3):
    assert evalmat(affine,(1,2,1),p)==evalmat(affine,(2,1,2),p)
    assert evalmat(affine,(2,3,2),p)==evalmat(affine,(3,2,3),p)
    assert evalmat(affine,(1,3),p)==evalmat(affine,(3,1),p)
    assert evalmat(affine,(1,2,3)*4,p)==I
assert all(evalmat(affine,x,2)==I for x in X)
seen={I};todo=[I]
while todo:
    a=todo.pop()
    for b in affine:
        c=mm(a,b,3)
        if c not in seen:seen.add(c);todo.append(c)
assert len(seen)==216
AW=evalmat(affine,W,3)
AP=evalmat(affine,pentagon_comm,3)
assert AW==((1,0,0),(0,1,2),(0,0,1))
assert AP==((1,0,1),(0,1,1),(0,0,1))
X3m=[evalmat(affine,x,3)for x in X]
X4m=[evalmat(affine,x,4)for x in X]
assert all(mm(a,b,4)==mm(b,a,4)for a in X4m for b in X4m)
p3=((1,0,1),(0,1,0),(0,0,1))
t3=((2,0,0),(0,2,0),(0,0,1))
q3=((1,0,0),(0,1,1),(0,0,1))
assert X3m[3]==t3 and X3m[4]==mm(q3,t3,3)
h0=X3m[0]
assert mm(mm(p3,p3,3),h0,3)==X3m[2]
assert mm(h0,t3,3)==mm(t3,h0,3) and mm(h0,p3,3)==mm(p3,h0,3)
h=mm(mm(p3,p3,3),X3m[0],3)
assert mm(p3,h,3)==X3m[0]
assert mm(h,X3m[4],3)==mm(X3m[4],h,3)
v0=((1,0,0),(0,1,2),(0,0,1))
L2=evalmat(affine,(2,2),3);U2=evalmat(affine,(1,1),3)
assert mm(mm(v0,L2,3),mi(v0,3),3)==X3m[1]
assert mm(mm(v0,U2,3),mi(v0,3),3)==X3m[2]
vector_checks=[]
for k in (0,3,6,9,12):
    fw=f*k
    fpt=evalmat((p3,t3),fw,3)
    af=fpt[0][2]
    assert fpt==((1,0,af),(0,1,0),(0,0,1))
    assert evalmat((t3,mm(q3,t3,3)),fw,3)==I
    FF=evalmat((X3m[0],X3m[1]),fw,3)
    FI=mi(FF,3)
    total=I
    for i,j in edges:total=mm(total,evalmat((X3m[i],X3m[j]),fw,3),3)
    expected=((1,0,(af+FI[0][1])%3),(0,1,(FI[1][1]-1)%3),(0,0,1))
    assert total==expected
    vector_checks.append({'word':'[x,y]^'+str(k),'formula_checked':True})
for rho0 in range(3):
    FF=((1,rho0,0),(rho0,(1+rho0*rho0)%3,0),(0,0,1))
    FI=mi(FF,3)
    assert (FI[0][1],(FI[1][1]-1)%3)==((-rho0)%3,0)

def perm_comp(a,b):return tuple(a[b[i]] for i in range(5))
pi=tuple(range(5));generators=[]
for i in range(4):
    a=list(pi);a[i],a[i+1]=a[i+1],a[i];generators.append(tuple(a))
reverse_cycle=pi
for i in (3,2,1,0):reverse_cycle=perm_comp(reverse_cycle,generators[i])
rho=perm_comp(reverse_cycle,reverse_cycle)
orbit=[];j=4
for k in range(5):orbit.append(j+1);j=rho[j]
assert len(set(orbit))==5 and j==4

result={'five_forgetful_maps':forgetting,
 'brunnian_word':'[[x12,x23],[x34,x45]]',
 'word_length_in_B4_generators':len(W),
 'nontrivial_exact_Artin_images_lengths':[len(v) for v in aw],
 'zero_exponent_sum_rules_out_a_nonzero_central_power':True,
 'Burau_F5_t2_word_matrix':BW,
 'Burau_F5_t2_detects_word':BW!=I,
 'Burau_F5_t2_pentagon_of_commutator_matrix':PC,
 'pentagon_of_2_cycle_commutator_detected':PC!=I,
 'commutator_pair_warning':'f=[x,y] is a 2-cycle word, not asserted to satisfy the multiplier-one 3-cycle or be a GT0 pair',
 'cyclic_forgetting_permutation_rho':tuple(i+1 for i in rho),
 'orbit_of_forgotten_label_5':orbit,
 'affine_F3_image_order':len(seen),
 'affine_F3_brunnian_word_matrix':AW,
 'affine_F3_pentagon_of_commutator_matrix':AP,
 'affine_F2_kills_all_five_pure_generators':True,
 'affine_mod4_all_five_Xi_images_commute':True,
 'affine_pentagon_vector_substitution_checks':vector_checks,
 'R3_matrix_gives_vector_minus_rho_e1_for_all_three_residues':True,
 'interpretation':'Every induced quotient from the five forgetful maps annihilates the pentagon word of every normalized 2-cycle solution. The displayed nontrivial Brunnian word is invisible there.'}
print(json.dumps(result,indent=2))
