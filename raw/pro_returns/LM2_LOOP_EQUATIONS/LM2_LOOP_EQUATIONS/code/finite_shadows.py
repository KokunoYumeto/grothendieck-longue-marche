"""Finite, characteristic GT_0 shadows with completely explicit certificates.

S3: the universal characteristic envelope and actual cycle equations.
A5, PSL2(F7): Guillot Theorem 4.9, reimplemented by colored equivariant maps.
These are finite shadows. Surjectivity from global GT_0 is NOT presumed.
"""
import json,math
from collections import Counter
from pathlib import Path
from finite_groups import (Group,permutation_group,matrix_group,matmul,
                          orbit_pair_classes,universal_envelope)

HERE=Path(__file__).resolve().parent

def compose(a,b):return tuple(a[i] for i in b)

def order_perm(p):
    ans=1;seen=set()
    for i in range(len(p)):
        if i in seen:continue
        j=i;k=0
        while j not in seen:seen.add(j);j=p[j];k+=1
        ans=math.lcm(ans,k)
    return ans

def colored_centralizer(perms,colors):
    N=len(colors);unseen=set(range(N));orbits=[]
    while unseen:
        start=min(unseen);orb={start};todo=[start]
        for p in todo:
            for g in perms:
                q=g[p]
                if q not in orb:orb.add(q);todo.append(q)
        orbits.append(sorted(orb));unseen-=orb
    def maps(O,P):
        if len(O)!=len(P):return []
        ans=[]
        for q in P:
            if colors[O[0]]!=colors[q]:continue
            m={O[0]:q};todo=[O[0]];ok=True
            for a in todo:
                for g in perms:
                    b=g[a];v=g[m[a]]
                    if colors[b]!=colors[v] or (b in m and m[b]!=v):ok=False;break
                    if b not in m:m[b]=v;todo.append(b)
                if not ok:break
            if ok and len(set(m.values()))==len(P):ans.append(m)
        return ans
    unused=set(range(len(orbits)));blocks=[];gens=[];order=1
    while unused:
        i=min(unused);O=orbits[i];same=[j for j in sorted(unused) if maps(O,orbits[j])]
        autos=maps(O,O);a=len(autos);r=len(same)
        order*=a**r*math.factorial(r)
        blocks.append(dict(orbit_size=len(O),equivalent_orbits=r,self_maps=a))
        for j in same:
            for m in maps(orbits[j],orbits[j]):
                p=list(range(N))
                for k,v in m.items():p[k]=v
                if any(p[k]!=k for k in range(N)):gens.append(tuple(p))
        for j in same[1:]:
            m=maps(O,orbits[j])[0];p=list(range(N))
            for k,v in m.items():p[k]=v;p[v]=k
            gens.append(tuple(p))
        unused-=set(same)
    identity=tuple(range(N));elts={identity};todo=[identity]
    for p in todo:
        for g in gens:
            q=compose(p,g)
            if q not in elts:elts.add(q);todo.append(q)
    assert len(elts)==order
    for p in elts:
        assert all(colors[p[i]]==colors[i] for i in range(N))
        assert all(compose(p,g)==compose(g,p) for g in perms)
    return dict(order=order,blocks=blocks,generators=gens,
                element_orders=dict(sorted(Counter(order_perm(p) for p in elts).items())))

def simple_shadow(G,outer):
    reps,which=orbit_pair_classes(G)
    theta=tuple(which[(y,x)] for x,y in reps)
    delta=tuple(which[(G.inv[G.mul(x,y)],y)] for x,y in reps)
    out=tuple(which[(outer[x],outer[y])] for x,y in reps)
    colors=[(G.classes[x],G.classes[y]) for x,y in reps]
    r=colored_centralizer([theta,delta,out],colors)
    units=[k for k in range(G.exponent) if math.gcd(k,G.exponent)==1]
    rational_units=[k for k in units if all(G.classes[G.power(x,k)]==G.classes[x]
                                          for x in range(G.n))]
    r.update(name=G.name,group_order=G.n,generating_pairs=len(which),inner_pair_classes=len(reps),
             Aut_pair_classes=len(reps)//2,exponent=G.exponent,units=units,
             power_class_kernel=rational_units,
             full_GT_shadow_order=r['order']*len(units)//len(rational_units),
             pair_representatives=[[G.elements[x],G.elements[y]] for x,y in reps],
             theta=theta,delta=delta,outer=out)
    return r

def s3_shadow():
    S=permutation_group(3)
    G,x,y,pairs=universal_envelope(S)
    theta=G.map_from_generators(x,y,y,x)
    z=G.inv[G.mul(x,y)]
    rho=G.map_from_generators(x,y,y,z)
    delta=G.map_from_generators(x,y,z,y)
    assert theta and rho and delta
    comm=G.mul(G.mul(G.mul(x,y),G.inv[x]),G.inv[y])
    derived=sorted(G.generated([c[comm] for c in G.conj]))
    N=G.exponent
    # Characteristic core guarantees cyclic and swapping substitutions descend.
    cycle=[];auto_classes={};identity=tuple(range(G.n))
    def outer_key(h):
        a,b=h[x],h[y]
        return min((c[a],c[b]) for c in G.conj)
    for lam in range(2*N):
        if math.gcd(lam,2*N)!=1:continue
        m=(lam-1)//2
        for f in derived:
            if G.mul(theta[f],f)!=G.e:continue
            val=G.e
            for a in [rho[rho[f]],G.power(z,m),rho[f],G.power(y,m),f,G.power(x,m)]:
                val=G.mul(val,a)
            if val!=G.e:continue
            a=G.power(x,lam);b=G.mul(G.mul(G.inv[f],G.power(y,lam)),f)
            if len(G.generated([a,b]))!=G.n:continue
            h=G.map_from_generators(x,y,a,b)
            assert h and len(set(h))==G.n
            key=outer_key(h);auto_classes[key]=h
            cycle.append(dict(lambda_mod_2exponent=lam,f_index=f,
                              f_coordinates=[S.elements[v] for v in G.elements[f]],
                              outer_class=list(key),automorphism_order=order_perm(h)))
    # Direct definition of finite GT(G), independent of cycle enumeration.
    direct={};direct1={}
    for k in range(N):
        if math.gcd(k,N)!=1:continue
        b=G.power(y,k)
        for a in {c[G.power(x,k)] for c in G.conj}:
            if len(G.generated([a,b]))!=G.n:continue
            h=G.map_from_generators(x,y,a,b)
            assert h
            if all(outer_key(compose(h,t))==outer_key(compose(t,h)) for t in [theta,delta]):
                direct[outer_key(h)]=h
                if k==1:direct1[outer_key(h)]=h
    conj=G.map_from_generators(x,y,G.inv[x],G.inv[y])
    assert conj and len(set(conj))==G.n
    print("S3 conjugation is inner:",outer_key(conj)==outer_key(identity),flush=True)
    assert len(direct)==2 and len(direct1)==2
    assert set(auto_classes)==set(direct)
    return dict(group_order=S.n,envelope_order=G.n,envelope_factors=len(pairs),
                exponent=N,derived_order=len(derived),cycle_solution_count=len(cycle),
                cycle_outer_image=len(auto_classes),GT_shadow_order=len(direct),
                GT1_shadow_order=len(direct1),Galois_outer_image_order=2,
                identity_outer=list(outer_key(identity)),
                conjugation_outer=list(outer_key(conj)),solutions=cycle,
                finite_GT_element_orders={'1':1,'2':1})

def main():
    results={'S3':s3_shadow()}
    print('S3 done:',{k:v for k,v in results['S3'].items() if k!='solutions'},flush=True)
    A=permutation_group(5,even=True)
    p=(1,0,2,3,4)
    outer=tuple(A.index[tuple(p[a[p[i]]] for i in range(5))] for a in A.elements)
    results['A5']=simple_shadow(A,outer)
    print('A5 done:',{k:v for k,v in results['A5'].items() if k not in
          ['pair_representatives','theta','delta','outer','generators']},flush=True)
    G=matrix_group(7,projective=True)
    d=(3,0,0,1);di=(5,0,0,1)
    canon=lambda a:min(a,tuple(-v%7 for v in a))
    outer=tuple(G.index[canon(matmul(matmul(d,a,7),di,7))] for a in G.elements)
    results['PSL2F7']=simple_shadow(G,outer)
    print('PSL2F7 done:',{k:v for k,v in results['PSL2F7'].items() if k not in
          ['pair_representatives','theta','delta','outer','generators']},flush=True)
    assert results['A5']['order']==1
    assert results['PSL2F7']['order']==512
    (HERE/'finite_shadows.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':main()
