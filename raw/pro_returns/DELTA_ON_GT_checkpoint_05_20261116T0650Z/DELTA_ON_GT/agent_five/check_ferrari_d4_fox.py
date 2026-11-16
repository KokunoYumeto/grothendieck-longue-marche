"""Full Fox-chain character representation for D4=C''(C')^4.

The field F9 is encoded by a+3*b for a+b*i, i^2=-1.  Character
indices use base-four digits in the exact cube-Schreier F5 basis.
All five chain coordinates are retained; no homology restriction is used.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parent
INPUT = ROOT.parent / 'agent_lifting' / 'records' / 'f5_nielsen_fox.json'
N, d = 1024, 5
characters = np.array([[(k >> (2*j)) & 3 for j in range(d)] for k in range(N)], dtype=np.int16)
weights = 4 ** np.arange(d, dtype=np.int16)
IP = np.arange(N, dtype=np.int16)
IM = np.broadcast_to(np.eye(d, dtype=np.int16), (N,d,d)).copy()
ONE = (IP, IM)
ADD = np.array([[(a%3+b%3)%3+3*((a//3+b//3)%3) for b in range(9)] for a in range(9)], dtype=np.int16)
NEG = np.array([(-a%3)%3+3*((-(a//3))%3) for a in range(9)], dtype=np.int16)
MUL = np.array([[((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3) for b in range(9)] for a in range(9)], dtype=np.int16)
INV = np.array([0]+[int(np.flatnonzero(MUL[a]==1)[0]) for a in range(1,9)], dtype=np.int16)
ROOTS = np.array([1,3,2,6], dtype=np.int16)

def mm(A,B):
    a0,a1=A%3,A//3
    b0,b1=B%3,B//3
    return ((a0@b0-a1@b1)%3+3*((a0@b1+a1@b0)%3)).astype(np.int16)

def minv(A):
    # A may be one matrix or an arbitrary batch of square matrices.
    shape=A.shape
    a=A.reshape((-1,d,d)).copy(); n=len(a); ii=np.arange(n)
    out=np.broadcast_to(np.eye(d,dtype=np.int16),(n,d,d)).copy()
    for j in range(d):
        good=a[:,j:,j]!=0
        assert np.all(np.any(good,axis=1))
        pivot=j+np.argmax(good,axis=1)
        a[ii,j],a[ii,pivot]=a[ii,pivot].copy(),a[ii,j].copy()
        out[ii,j],out[ii,pivot]=out[ii,pivot].copy(),out[ii,j].copy()
        scale=INV[a[:,j,j]]
        a[:,j]=MUL[scale[:,None],a[:,j]]
        out[:,j]=MUL[scale[:,None],out[:,j]]
        for k in range(d):
            if k==j:continue
            factor=a[:,k,j].copy()
            a[:,k]=ADD[a[:,k],NEG[MUL[factor[:,None],a[:,j]]]]
            out[:,k]=ADD[out[:,k],NEG[MUL[factor[:,None],out[:,j]]]]
    assert np.array_equal(a,np.broadcast_to(np.eye(d,dtype=np.int16),a.shape))
    return out.reshape(shape)

def mul(g,h):
    # First h, then g: source chi -> h(chi) -> g(h(chi)).
    return (g[0][h[0]],mm(g[1][h[0]],h[1]))

def inv(g):
    p=np.argsort(g[0]).astype(np.int16)
    return p,minv(g[1][p])

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
            if letter>0:
                out[:,row,col]=ADD[out[:,row,col],ROOTS[prefix%4]]
                prefix+=chars[:,row]
            else:
                prefix-=chars[:,row]
                out[:,row,col]=ADD[out[:,row,col],NEG[ROOTS[prefix%4]]]
    return out

def generator(data,name):
    inverse_name=name[:-4] if name.endswith('_inv') else name+'_inv'
    Ti=np.array(data['abelianization_matrices'][inverse_name],dtype=np.int16)
    eta=characters@Ti%4
    p=(eta@weights).astype(np.int16)
    m=fox_at(data['free_group_images'][name],eta)
    boundary=ADD[ROOTS[characters],NEG[1]]
    assert np.array_equal(mm(boundary[p,None,:],m)[:,0,:],boundary)
    return p,m

def orbits(perms):
    todo=set(range(N));out=[]
    while todo:
        seed=min(todo);orb={seed};queue=[seed]
        for q in queue:
            for p in perms:
                r=int(p[q])
                if r not in orb:orb.add(r);queue.append(r)
        todo.difference_update(orb);out.append(sorted(orb))
    return out

def bounded_order(g,bound=2**10*3**4):
    assert eq(power(g,bound),ONE),'order has a prime other than 2,3 or exceeds the declared bound'
    n=bound
    for p in (2,3):
        while n%p==0 and eq(power(g,n//p),ONE):n//=p
    return n

def primary3(g):
    n=bounded_order(g);n3=1;n2=n
    while n2%3==0:n3*=3;n2//=3
    exponent=0 if n3==1 else n2*pow(n2,-1,n3)
    return power(g,exponent),n,exponent

def main():
    data=json.loads(INPUT.read_text())
    generators={name:generator(data,name) for name in data['free_group_images']}
    a,b,c=[generators[name] for name in ('a','b','c')]
    assert all(eq(mul(generators[x],generators[x+'_inv']),ONE) for x in ('a','b','c'))
    assert eq(prod(a,b,a),prod(b,a,b))
    assert eq(prod(b,c,b),prod(c,b,c))
    assert eq(mul(a,c),mul(c,a))
    assert eq(power(prod(a,b,c),4),ONE)
    X=[power(a,2),power(b,2),power(c,2),power(prod(a,b,a),2),power(prod(c,b,c),2)]
    commuting=[[bool(np.array_equal(mul(g,h)[0],mul(h,g)[0])) for h in X] for g in X]
    orb=orbits([a[0],b[0],c[0]])
    report={'field':'F3[i], i^2=-1; encoding a+3b',
            'basis_input':str(INPUT),'characters':N,'chain_dimension_per_character':5,
            'source_to_target_permutations':True,
            'all_six_Fox_boundary_identities':True,'all_L_relators':True,
            'pure_character_permutation_commuting_table':commuting,
            'L_character_orbits':[{'representative':o[0],'character':characters[o[0]].tolist(),'size':len(o),
                                   'primitive_order4':bool(np.any(characters[o[0]]%2))} for o in orb],
            'Xi_orders':[bounded_order(g) for g in X]}
    np.savez_compressed(ROOT/'ferrari_d4_fox.npz',characters=characters,
       generator_permutations=np.stack([a[0],b[0],c[0]]),generator_blocks=np.stack([a[1],b[1],c[1]]),
       X_permutations=np.stack([g[0] for g in X]),X_blocks=np.stack([g[1] for g in X]),
       boundary_rows=ADD[ROOTS[characters],NEG[1]])
    (ROOT/'ferrari_d4_fox.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
