"""First non-nilpotent evaluation pairs in an odd-characteristic five-point target.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 16 November 2026.
Run: python -I -B check_burau_odd_pair.py
"""
import json
p=7;t=2
I=(1,0,0,0,1,0,0,0,1)
def norm(a):
    a=tuple(x%p for x in a)
    c=pow(next(x for x in a if x),-1,p)
    return tuple(c*x%p for x in a)
def linear_mul(a,b):return tuple(sum(a[3*i+k]*b[3*k+j]for k in range(3))%p for i in range(3)for j in range(3))
def mul(a,b):return norm(linear_mul(a,b))
def inv(a):
    z=[list(a[3*i:3*i+3])+[int(i==j)for j in range(3)]for i in range(3)]
    for j in range(3):
        k=next(i for i in range(j,3)if z[i][j]);z[k],z[j]=z[j],z[k]
        c=pow(z[j][j],-1,p);z[j]=[c*x%p for x in z[j]]
        for i in range(3):
            if i!=j:
                c=z[i][j];z[i]=[(x-c*y)%p for x,y in zip(z[i],z[j])]
    return norm(tuple(x for row in z for x in row[3:]))
def power(a,n):
    q=I
    for _ in range(n):q=mul(q,a)
    return q
def order(a):return next(n for n in range(1,1000)if power(a,n)==I)
def group(gens):
    H={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gens:
            z=mul(a,b)
            if z not in H:H.add(z);todo.append(z)
    return H
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def derived(H,gens):
    candidates={comm(h,g)for h in H for g in gens}
    D={I};dg=[]
    for x in sorted(candidates):
        if x not in D:dg.append(x);D=group(dg)
    assert all(mul(mul(g,h),inv(g))in D for h in D for g in gens)
    return D,dg
def derived_series(gens):
    H=group(gens);chain=[H]
    while len(H)>1:
        D,gens=derived(H,gens);chain.append(D)
        if D==H:break
        H=D
    return chain
raw=((1-t,t,0,1,0,0,0,0,1),(1,0,0,0,1-t,t,0,1,0),(1,0,-1,0,1,-1,0,0,-t))
a,b,c=map(norm,raw)
assert mul(mul(a,b),a)==mul(mul(b,a),b)
assert mul(mul(b,c),b)==mul(mul(c,b),c)
assert mul(a,c)==mul(c,a)
z=I
for g in raw*4:z=linear_mul(z,g)
assert z==(t,0,0,0,t,0,0,0,t)
X=(power(a,2),power(b,2),power(c,2),power(mul(mul(a,b),a),2),power(mul(mul(c,b),c),2))
records=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    chain=derived_series([X[i],X[j]])
    records.append({'pair':[i+1,j+1],'derived_series_orders':[len(h)for h in chain],
                    'generator_orders':[order(X[i]),order(X[j])], 'product_order':order(mul(X[i],X[j])),
                    'nontrivial_perfect_stable_derived_group':len(chain[-1])>1,
                    'second_derived_nonnilpotent':len(chain[-1])>1 and chain[min(2,len(chain)-1)]==chain[-1]})

def m2(a,b):return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
                    (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)
I2=(1,0,0,1);U=(1,1,0,1);L3=(1,0,-3%p,1)
UV=m2(U,L3);P=(UV[3],-UV[1]%p,-UV[2]%p,UV[0])
map45={I:I2};todo=[I]
while todo:
    h=todo.pop()
    for g,mg in ((X[3],U),(X[4],L3)):
        z=mul(h,g);mz=m2(map45[h],mg)
        if z in map45:assert map45[z]==mz
        else:map45[z]=mz;todo.append(z)
assert len(map45)==len(set(map45.values()))==336
map34={I:(0,I2)};todo=[I]
while todo:
    h=todo.pop()
    for g,cg,mg in ((X[2],1,P),(X[3],0,U)):
        z=mul(h,g);ch,mh=map34[h];mz=((ch+cg)%3,m2(mh,mg))
        if z in map34:assert map34[z]==mz
        else:map34[z]=mz;todo.append(z)
assert len(map34)==len(set(map34.values()))==1008
hstrip=next(g for g,v in map34.items()if v==(1,I2))
p0=mul(X[2],inv(hstrip))
assert map34[p0]==(0,P) and order(p0)==3 and order(mul(p0,X[3]))==7
print(json.dumps({'field':p,'chosen_primitive_cube_root':t,'linear_full_twist':z,
 'Xi_orders':[order(x)for x in X],'pair_certificates':records,
 'marked_H45_isomorphism':{'target':'SL2(F7)','X4':U,'X5':L3,'all_336_elements_checked':True},
 'marked_H34_isomorphism':{'target':'C3 x SL2(F7)','X3':[1,P],'X4':[0,U],
                         'central_C3_generator':hstrip,'stripped_p':p0,'all_1008_elements_checked':True},
 'main_strategy_boundary':'The perfect pair images escape the LI8 nilpotent-second-derived obstruction. A joint quotient with the finite frame detector is well-defined, but no annihilating pentagon/sign identity or compatible lift is produced by these group orders. The complete three-dimensional image and finite GT shadows were not enumerated.'},indent=2))
