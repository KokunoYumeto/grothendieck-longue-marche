"""Reverse mixed primes: D3=C''(C')^3, full Fox chains over F4.

F4 is encoded a+2b for a+b*w, w^2+w+1=0. Every character
permutation and every fifth (augmentation) chain direction is retained.
"""
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT.parent/'agent_lifting/records/f5_nielsen_fox.json'
N,d=243,5
characters=np.array([[(k//3**j)%3 for j in range(d)] for k in range(N)],dtype=np.int16)
weights=3**np.arange(d,dtype=np.int16)
IP=np.arange(N,dtype=np.int16);IM=np.broadcast_to(np.eye(d,dtype=np.int16),(N,d,d)).copy();ONE=(IP,IM)
MUL=np.array([[((a%2)*(b%2)+(a//2)*(b//2))%2+2*(((a%2)*(b//2)+(a//2)*(b%2)+(a//2)*(b//2))%2) for b in range(4)] for a in range(4)],dtype=np.int16)
INV=np.array([0,1,3,2],dtype=np.int16);ROOTS=np.array([1,2,3],dtype=np.int16)
def mm(A,B):
    a0,a1=A%2,A//2;b0,b1=B%2,B//2
    return ((a0@b0+a1@b1)%2+2*((a0@b1+a1@b0+a1@b1)%2)).astype(np.int16)
def minv(A):
    shape=A.shape;a=A.reshape((-1,d,d)).copy();n=len(a);ii=np.arange(n)
    out=np.broadcast_to(np.eye(d,dtype=np.int16),(n,d,d)).copy()
    for j in range(d):
        good=a[:,j:,j]!=0;assert np.all(np.any(good,axis=1));p=j+np.argmax(good,axis=1)
        a[ii,j],a[ii,p]=a[ii,p].copy(),a[ii,j].copy();out[ii,j],out[ii,p]=out[ii,p].copy(),out[ii,j].copy()
        scale=INV[a[:,j,j]];a[:,j]=MUL[scale[:,None],a[:,j]];out[:,j]=MUL[scale[:,None],out[:,j]]
        for k in range(d):
            if k==j:continue
            factor=a[:,k,j].copy();a[:,k]^=MUL[factor[:,None],a[:,j]];out[:,k]^=MUL[factor[:,None],out[:,j]]
    assert np.array_equal(a,np.broadcast_to(np.eye(d,dtype=np.int16),a.shape))
    return out.reshape(shape)
def mul(g,h):return g[0][h[0]],mm(g[1][h[0]],h[1])
def inv(g):
    p=np.argsort(g[0]).astype(np.int16);return p,minv(g[1][p])
def eq(g,h):return np.array_equal(g[0],h[0]) and np.array_equal(g[1],h[1])
def prod(*args):
    g=ONE
    for h in args:g=mul(g,h)
    return g
def power(g,n):
    if n<0:g,n=inv(g),-n
    h=ONE
    while n:
        if n&1:h=mul(h,g)
        n//=2
        if n:g=mul(g,g)
    return h
def comm(g,h):return prod(g,h,inv(g),inv(h))
def fox_at(words,chars):
    out=np.zeros((len(chars),d,d),dtype=np.int16)
    for col,w in enumerate(words):
        prefix=np.zeros(len(chars),dtype=np.int16)
        for letter in w:
            row=abs(letter)-1
            if letter>0:out[:,row,col]^=ROOTS[prefix%3];prefix+=chars[:,row]
            else:prefix-=chars[:,row];out[:,row,col]^=ROOTS[prefix%3]
    return out
def generator(data,name):
    ni=name[:-4] if name.endswith('_inv') else name+'_inv'
    Ti=np.array(data['abelianization_matrices'][ni],dtype=np.int16)
    eta=characters@Ti%3;p=(eta@weights).astype(np.int16);m=fox_at(data['free_group_images'][name],eta)
    boundary=ROOTS[characters]^1
    assert np.array_equal(mm(boundary[p,None,:],m)[:,0,:],boundary)
    return p,m
def orbits(perms):
    todo=set(range(N));out=[]
    while todo:
        q=[min(todo)];seen=set(q)
        for h in q:
            for p in perms:
                r=int(p[h])
                if r not in seen:seen.add(r);q.append(r)
        todo.difference_update(seen);out.append(sorted(seen))
    return out
def bounded_order(g,bound=2**10*3**5):
    assert eq(power(g,bound),ONE)
    n=bound
    for p in (2,3):
        while n%p==0 and eq(power(g,n//p),ONE):n//=p
    return n
def primary3(g):
    n=bounded_order(g);m=n;q=1
    while m%3==0:m//=3;q*=3
    e=0 if q==1 else m*pow(m,-1,q)
    return power(g,e),n,e
def main():
    data=json.loads(INPUT.read_text());G={s:generator(data,s) for s in data['free_group_images']}
    a,b,c=[G[s] for s in ('a','b','c')]
    assert all(eq(mul(G[s],G[s+'_inv']),ONE) for s in ('a','b','c'))
    assert eq(prod(a,b,a),prod(b,a,b)) and eq(prod(b,c,b),prod(c,b,c))
    assert eq(mul(a,c),mul(c,a)) and eq(power(prod(a,b,c),4),ONE)
    X=[power(a,2),power(b,2),power(c,2),power(prod(a,b,a),2),power(prod(c,b,c),2)]
    rotation=prod(a,b,c);assert eq(prod(rotation,X[0],inv(rotation)),X[1]) and eq(prod(rotation,X[1],inv(rotation)),X[2])
    oo=orbits([a[0],b[0],c[0]])
    report={'field':'F2[w], w^2+w+1=0; encoding a+2b',
      'characters':243,'full_chain_dimension_per_character':5,'cover_free_rank':973,
      'all_six_Fox_boundary_identities':True,'all_L_relators_and_inverses':True,
      'harmonic_conjugacy_by_abc':True,'Xi_orders':[bounded_order(g) for g in X],
      'L_character_orbits':[{'representative':o[0],'character':characters[o[0]].tolist(),'size':len(o)} for o in oo],
      'scope':'Actual monomial source representation. No assumption of commuting character permutations or blockwise f-values.'}
    np.savez_compressed(ROOT/'ferrari_d3_fox.npz',characters=characters,
      generator_permutations=np.stack([a[0],b[0],c[0]]),generator_blocks=np.stack([a[1],b[1],c[1]]),
      X_permutations=np.stack([g[0] for g in X]),X_blocks=np.stack([g[1] for g in X]),boundary_rows=ROOTS[characters]^1)
    (ROOT/'ferrari_d3_fox.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
