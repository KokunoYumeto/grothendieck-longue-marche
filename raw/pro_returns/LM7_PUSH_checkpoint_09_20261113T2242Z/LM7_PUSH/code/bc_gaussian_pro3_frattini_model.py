#!/usr/bin/env python3
"""A faithful small action detecting every Gaussian pro-3 abelian character.

The free kernel quotient is P/(gamma4(P) gamma2(P)^3 P^9), of order3^7.
Four literal UT4(F3) maps detect its four-dimensional centre. Induction
through the actual order-four automorphism gives a432-point triangle map.
"""
from pathlib import Path
from collections import deque
import itertools
import hashlib
import json
import time
import numpy as np

HERE=Path(__file__).resolve().parent
ZERO=(0,)*6


def umul(a,b):
    r,s,t,u,v,w=a;R,S,T,U,V,W=b
    return ((r+R)%3,(s+S)%3,(t+T)%3,(u+U+r*S)%3,
            (v+V+s*T)%3,(w+W+r*V+u*T)%3)


def uinv(a):
    r,s,t,u,v,w=a
    return (-r%3,-s%3,-t%3,(-u+r*s)%3,(-v+s*t)%3,
            (-w+r*v+u*t-r*s*t)%3)


def mul(a,b):return tuple(umul(x,y) for x,y in zip(a,b))
def inv(a):return tuple(uinv(x) for x in a)
ONE=(ZERO,)*4


def power(g,n):
    if n<0:g,n=inv(g),-n
    a=ONE
    while n:
        if n&1:a=mul(a,g)
        g=mul(g,g);n//=2
    return a


def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
CHAIN=(1,1,1,0,0,0)
X=(CHAIN,ZERO,(1,1,0,0,0,0),(1,0,0,0,0,0))
Y=(ZERO,CHAIN,(0,0,1,0,0,0),(0,1,1,0,0,0))


def collect(a,b,c,d,e,xx=X,yy=Y):
    cc=comm(xx,yy);dd=comm(cc,xx);ee=comm(cc,yy)
    ans=ONE
    for g,n in zip((xx,yy,cc,dd,ee),(a,b,c,d,e)):ans=mul(ans,power(g,n))
    return ans


def rank3(a):
    a=np.array(a,dtype=np.int64)%3;r=0
    for j in range(a.shape[1]):
        q=next((i for i in range(r,len(a)) if a[i,j]),None)
        if q is None:continue
        a[[r,q]]=a[[q,r]];a[r]=a[r]*pow(int(a[r,j]),-1,3)%3
        for i in range(len(a)):
            if i!=r:a[i]=(a[i]-a[i,j]*a[r])%3
        r+=1
    return r


def main():
    start=time.monotonic();c=comm(X,Y);dx=comm(c,X);dy=comm(c,Y)
    for g in (X,Y):assert power(g,9)==ONE and power(g,3)!=ONE
    for g in (c,dx,dy):assert power(g,3)==ONE and g!=ONE
    for g in (dx,dy):assert comm(g,X)==comm(g,Y)==ONE
    coords=list(itertools.product(range(9),range(9),range(3),range(3),range(3)))
    elements=[collect(*q) for q in coords];at={g:i for i,g in enumerate(elements)}
    assert len(at)==2187
    # Exact generation and multiplication by the original generators.
    found={ONE};queue=deque([ONE])
    while queue:
        a=queue.popleft()
        for g in (X,Y):
            b=mul(a,g);assert b in at
            if b not in found:found.add(b);queue.append(b)
    assert len(found)==2187
    phi=np.array([at[collect(*q,xx=inv(Y),yy=X)] for q in coords],dtype=np.int64)
    assert sorted(phi)==list(range(2187))
    for i,g in enumerate(elements):
        for a,b in ((X,inv(Y)),(Y,X)):
            assert elements[phi[at[mul(g,a)]]]==mul(elements[phi[i]],b)
    assert np.array_equal(phi[phi[phi[phi]]],np.arange(2187))
    # The four actual central characters are recorded, not inferred
    # just from equality of two group orders.
    centres=[power(X,3),power(Y,3),dx,dy]
    central_matrix=[[g[j][5] for g in centres] for j in range(4)]
    assert rank3(central_matrix)==4
    centre=[g for g in elements if comm(g,X)==comm(g,Y)==ONE]
    assert len(centre)==81
    pts=list(itertools.product(range(3),repeat=3));pos={p:i for i,p in enumerate(pts)}
    def perm108(g):
        out=[]
        for j,a in enumerate(g):
            r,s,t,u,v,w=uinv(a)
            out.extend(27*j+pos[((x+r*y+u*z+w)%3,(y+s*z+v)%3,(z+t)%3)] for x,y,z in pts)
        return np.array(out,dtype=np.uint16)
    p108=np.array([perm108(g) for g in elements],dtype=np.uint16)
    assert len({p.tobytes() for p in p108})==2187
    for i,g in enumerate(elements):
        for a in (X,Y):assert np.array_equal(p108[at[mul(g,a)]],p108[at[a]][p108[i]])
    def induced(i,e):
        out=[];j=i
        for k in range(4):
            out.append(108*((k+e)%4)+p108[j]);j=int(phi[j])
        return np.concatenate(out)
    px=induced(at[X],1);py=induced(at[inv(Y)],2);pz=induced(at[ONE],1)
    one=np.arange(432,dtype=np.uint16)
    def ppower(a,n):
        p=one
        for _ in range(n):p=a[p]
        return p
    assert np.array_equal(pz[py[px]],one)
    assert np.array_equal(ppower(py,2),one) and np.array_equal(ppower(pz,4),one)
    assert np.array_equal(ppower(px,4),induced(at[comm(X,inv(Y))],0))
    # All six maps are literal substitutions in this one based action.
    pairs=[(px,py),(py,px),(pz,px),(px,pz),(py,pz),(pz,py)]
    F=np.array([np.concatenate([432*j+p[i] for j,p in enumerate(pairs)]) for i in range(2)])
    def word(w):
        a=np.arange(2592,dtype=np.uint16)
        letters={1:F[0],2:F[1],-1:np.argsort(F[0]),-2:np.argsort(F[1])}
        for t in w:a=letters[t][a]
        return a
    nwords=json.loads((HERE/'bc_cm_literal_words.json').read_text())['N_B_basis_in_F']
    N=np.array([word(w) for w in nwords],dtype=np.uint16)
    out={'status':'PASS_EXACT_GAUSSIAN_CLASS_THREE_FRATTINI_DETECTOR',
         'free_kernel_order':2187,'full_triangle_order':8748,
         'faithful_free_kernel_degree':108,'induced_triangle_degree':432,
         'six_evaluation_degree':2592,
         'actual_UT4_X':X,'actual_UT4_Y':Y,
         'UT4_coordinate_order':['01','12','23','02','13','03'],
         'Hall_coordinate_ranges':[9,9,3,3,3],
         'Hall_order':['X','Y','[X,Y]','[[X,Y],X]','[[X,Y],Y]'],
         'four_central_characters':central_matrix,
         'centre_order':81,'all_2187_Hall_elements_distinct':True,
         'actual_order_four_automorphism_checked_on_every_element':True,
         'right_permutation_convention':'p(gh)=p(h)[p(g)]',
         'all_97_literal_N_words':nwords,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{'bc_cm_literal_words.json':hashlib.sha256((HERE/'bc_cm_literal_words.json').read_bytes()).hexdigest()},
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'bc_gaussian_pro3_frattini_model.npz',
                        F_generator_permutations=F,N_generator_permutations=N,
                        triangle_generators=np.array([px,py,pz]),
                        P_elements=np.array(elements,dtype=np.uint8),
                        P_Hall_coordinates=np.array(coords,dtype=np.uint8),
                        deck_automorphism=phi.astype(np.uint16))
    (HERE/'bc_gaussian_pro3_frattini_model.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='all_97_literal_N_words'},indent=2))


if __name__=='__main__':main()
