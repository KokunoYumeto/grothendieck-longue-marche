#!/usr/bin/env python3
"""Work in progress: exact exponent-three, class-three Fermat boundary group.

H is the literal rank-ten Schreier subgroup from de_fermat_schreier.
The quotient is H/(gamma_4(H) H^3), not the unrestricted degree-three
free Lie algebra.  Its coordinates (v,z,t) have lengths 10,45,120.
v,z are exactly the E33 BCH coordinates.  For i<j<k, t_ijk is the
Magnus coefficient of X_i X_j X_k minus that of X_j X_i X_k.

The final coordinates kill the complete central cube span.  The code
retains literal based substitutions, with no diagonal replacement.
Existing checkpoint05 certificates are read only.
"""
from pathlib import Path
from functools import cached_property
from itertools import combinations, permutations, product
import json,time
import numpy as np
import de_fermat_schreier as f
import bc_fermat_class_two as old

HERE=Path(__file__).resolve().parent
P=3
PAIRS=list(combinations(range(10),2))
PAIR_INDEX={p:i for i,p in enumerate(PAIRS)}
PI,PJ=np.array(PAIRS,dtype=np.int64).T
TRIPLES=list(combinations(range(10),3))
TI,TJ,TK=np.array(TRIPLES,dtype=np.int64).T
TIJ=np.array([PAIR_INDEX[i,j] for i,j,k in TRIPLES])
TIK=np.array([PAIR_INDEX[i,k] for i,j,k in TRIPLES])
TJK=np.array([PAIR_INDEX[j,k] for i,j,k in TRIPLES])
DIM=175
ZERO=np.zeros(DIM,dtype=np.int64)
GENERATORS=np.eye(DIM,dtype=np.int64)[:10]

def multiply(g,h):
    v,z,t=g[:10],g[10:55],g[55:]
    w,u,s=h[:10],h[10:55],h[55:]
    out=g+h
    out[10:55]+=2*(v[PI]*w[PJ]-v[PJ]*w[PI])
    out[55:]+=(2*(v[TI]*w[TJ]-v[TJ]*w[TI])*w[TK]
                +v[TI]*u[TJK]-v[TJ]*u[TIK]+2*z[TIJ]*w[TK])
    return out%3

def inverse(g):
    v,z=g[:10],g[10:55]
    out=-g
    out[55:]+=v[TI]*z[TJK]-v[TJ]*z[TIK]+2*z[TIJ]*v[TK]
    return out%3

def power(g,n):
    n=int(n)%3
    return ZERO.copy() if n==0 else g.copy() if n==1 else multiply(g,g)

def commutator(g,h):
    return multiply(multiply(multiply(g,h),inverse(g)),inverse(h))

def canonical_triple(v,z):
    """Triple coordinate of prod eta_i^v_i prod [eta_i,eta_j]^b_ij.

    Here b_ij=z_ij-2*v_i*v_j, and digits v_i are taken in {0,1,2}.
    """
    return (v[TI]*v[TJ]*v[TK]+v[TI]*z[TJK]-v[TJ]*z[TIK])%3

def collect_signed(word):
    out=ZERO.copy()
    for letter in word:
        k=abs(int(letter))-1
        sign=1 if letter>0 else -1
        mask=TK==k
        out[55:][mask]+=2*sign*out[10:55][TIJ[mask]]
        out[10:55]+=2*sign*(out[:10][PI]*(PJ==k)-out[:10][PJ]*(PI==k))
        out[k]+=sign
        out%=3
    return out

def collect_f(word):
    q=(0,0);signed=[]
    for letter in word:
        qn=f.step(q,letter)
        edge=f.EDGES[q,letter] if letter>0 else -f.EDGES[qn,-letter]
        if edge:signed.append(edge)
        q=qn
    return q,collect_signed(signed)

def literal(word):
    q,g=collect_f(word)
    assert q==(0,0)
    return g

def exterior_three(a):
    columns=[]
    for i,j,k in TRIPLES:
        columns.append(a[TI,i]*(a[TJ,j]*a[TK,k]-a[TJ,k]*a[TK,j])
             -a[TI,j]*(a[TJ,i]*a[TK,k]-a[TJ,k]*a[TK,i])
             +a[TI,k]*(a[TJ,i]*a[TK,j]-a[TJ,j]*a[TK,i]))
    return np.stack(columns,axis=1)%3

class Action:
    """The genuine homomorphism specified by ten generator images."""
    def __init__(self,images,name=""):
        self.images=np.asarray(images,dtype=np.int64)%3
        assert self.images.shape==(10,DIM)
        self.name=name
        self.ab=self.images[:,:10].T
        self.comm=np.stack([commutator(self.images[i],self.images[j])
                            for i,j in PAIRS],axis=1)
        assert not np.any(self.comm[:10])
        self.triple=exterior_three(self.ab)
        self.bases={}
    def base(self,v):
        key=tuple((v%3).tolist())
        if key not in self.bases:
            out=ZERO.copy()
            for coefficient,g in zip(key,self.images):
                if coefficient:out=multiply(out,power(g,coefficient))
            self.bases[key]=out
        return self.bases[key]
    def __call__(self,g):
        v,z,t=g[:10],g[10:55],g[55:]
        b=(z-2*v[PI]*v[PJ])%3
        c=(t-canonical_triple(v,z))%3
        out=multiply(self.base(v),self.comm@b%3)
        out[55:]=(out[55:]+self.triple@c)%3
        return out

def substituted_action(images,name=""):
    return Action([literal(old.substitute(w,images)) for w in f.NWORDS],name)

S=substituted_action(([2],[1]),"s")
R=substituted_action(([2],[-2,-1]),"r")

def norm_errors(g):
    first=multiply(S(g),g)
    inv=inverse(g)
    second=multiply(multiply(inv,R(inv)),R(R(inv)))
    return np.r_[first,second]

def tensor_comm(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            out[u+v]=(out.get(u+v,0)+x*y)%3
            out[v+u]=(out.get(v+u,0)-x*y)%3
    return {w:a for w,a in out.items() if a}

def lyndon(w):
    return all(w<w[i:]+w[:i] for i in range(1,len(w)))

def lyndon_bracket(w):
    if len(w)==1:return {w:1}
    split=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return tensor_comm(lyndon_bracket(w[:split]),lyndon_bracket(w[split:]))

def tensor_projection(tensor):
    return np.array([(tensor.get((i,j,k),0)-tensor.get((j,i,k),0))%3
                     for i,j,k in TRIPLES],dtype=np.int64)

def cube_tensor(v):
    return {w:int(v[w[0]]*v[w[1]]*v[w[2]])%3
            for w in product(range(10),repeat=3)
            if v[w[0]]*v[w[1]]*v[w[2]]%3}

def add_tensors(*terms):
    out={}
    for coefficient,tensor in terms:
        for w,a in tensor.items():out[w]=(out.get(w,0)+coefficient*a)%3
    return {w:a for w,a in out.items() if a}

def cube_span_certificate():
    # The ordinary Hall/Lyndon degree-three basis has triangular leading terms.
    words=[w for w in product(range(10),repeat=3) if lyndon(w)]
    assert len(words)==330
    expansions=[lyndon_bracket(w) for w in words]
    assert all(min(e)==w and e[w]==1 for w,e in zip(words,expansions))
    basis=[];cube_preimages=[]
    eye=np.eye(10,dtype=np.int64)
    for i in range(10):
        basis.append(cube_tensor(eye[i]));cube_preimages.append([[1,eye[i].tolist()]])
    for i,j in PAIRS:
        p=cube_tensor(eye[i]+eye[j]);m=cube_tensor(eye[i]-eye[j])
        ci,cj=cube_tensor(eye[i]),cube_tensor(eye[j])
        # Repeated-index symmetrizations, each an explicit sum of cubes.
        a=add_tensors((2,p),(1,m),(0,ci),(2,cj))
        b=add_tensors((2,p),(2,m),(2,ci),(0,cj))
        expected_a={w:1 for w in set(permutations((i,i,j)))}
        expected_b={w:1 for w in set(permutations((i,j,j)))}
        assert a==expected_a and b==expected_b
        assert a==tensor_comm({(i,):1},tensor_comm({(i,):1},{(j,):1}))
        assert b==tensor_comm({(j,):1},tensor_comm({(j,):1},{(i,):1}))
        basis.extend([a,b])
        cube_preimages.extend([[[2,(eye[i]+eye[j]).tolist()],[1,(eye[i]-eye[j]).tolist()],
                                [2,eye[j].tolist()]],
                               [[2,(eye[i]+eye[j]).tolist()],[2,(eye[i]-eye[j]).tolist()],
                                [2,eye[i].tolist()]]])
    for i,j,k in TRIPLES:
        terms=[(1,cube_tensor(eye[i]+eye[j]+eye[k]))]
        terms +=[(-1,cube_tensor(eye[a]+eye[b])) for a,b in ((i,j),(i,k),(j,k))]
        terms +=[(1,cube_tensor(eye[a])) for a in (i,j,k)]
        tensor=add_tensors(*terms)
        assert tensor=={w:1 for w in permutations((i,j,k))}
        aa=tensor_comm({(i,):1},tensor_comm({(j,):1},{(k,):1}))
        bb=tensor_comm({(j,):1},tensor_comm({(i,):1},{(k,):1}))
        assert tensor==add_tensors((1,aa),(1,bb))
        assert np.array_equal(tensor_projection(aa),np.eye(120,dtype=np.int64)[TRIPLES.index((i,j,k))])
        basis.append(tensor)
        cube_preimages.append([[1,(eye[i]+eye[j]+eye[k]).tolist()]]+
             [[-1,(eye[a]+eye[b]).tolist()] for a,b in ((i,j),(i,k),(j,k))]+
             [[1,eye[a].tolist()] for a in (i,j,k)])
    assert len(basis)==220
    assert len(set().union(*[set(b) for b in basis]))==1000
    # Supports are disjoint multisets, proving independence without a rank guess.
    assert sum(len(b) for b in basis)==1000
    assert all(not np.any(tensor_projection(b)) for b in basis)
    return {"ordinary_Lie_dimension":330,"restricted_cubes_dimension":10,
            "complete_cube_span_dimension":220,"remaining_triple_dimension":120,
            "triangular_Lyndon_basis_checked":True,"cube_preimages":cube_preimages}

def main():
    start=time.time();rng=np.random.default_rng(2026111303)
    certificate=cube_span_certificate()
    identity=Action(GENERATORS,"identity")
    for i,j,k in TRIPLES:
        expected=ZERO.copy();expected[55+TRIPLES.index((i,j,k))]=1
        assert np.array_equal(commutator(GENERATORS[i],commutator(GENERATORS[j],GENERATORS[k])),expected)
    for _ in range(100):
        a,b,c=[rng.integers(0,3,size=DIM) for __ in range(3)]
        assert np.array_equal(multiply(multiply(a,b),c),multiply(a,multiply(b,c)))
        assert np.array_equal(multiply(a,inverse(a)),ZERO)
        assert np.array_equal(multiply(multiply(a,a),a),ZERO)
        assert np.array_equal(identity(a),a)
        assert np.array_equal(multiply(a,b)[:55],old.multiply(a[:55],b[:55]))
        for action,oldaction in ((S,old.S),(R,old.R)):
            assert np.array_equal(action(multiply(a,b)),multiply(action(a),action(b)))
            assert np.array_equal(action(a)[:55],oldaction@a[:55]%3)
        assert np.array_equal(S(S(a)),a)
        assert np.array_equal(R(R(R(a))),a)
    for word in f.NWORDS+list(f.CUSP_WORDS.values()):
        assert np.array_equal(literal(word)[:55],old.literal(word))
    for _ in range(30):
        signed=rng.choice(np.r_[np.arange(1,11),-np.arange(1,11)],size=40).tolist()
        g=collect_signed(signed)
        direct=ZERO.copy()
        for letter in signed:direct=multiply(direct,power(GENERATORS[abs(letter)-1],1 if letter>0 else 2))
        assert np.array_equal(g,direct)
        fword=[l for token in signed for l in
               (f.NWORDS[token-1] if token>0 else f.inverse_word(f.NWORDS[-token-1]))]
        for action,images in ((S,([2],[1])),(R,([2],[-2,-1]))):
            assert np.array_equal(action(g),literal(old.substitute(fword,images)))
    for letter,actions in ((1,[S,R,R,S,R,R]),(2,[R,R,S,R,R,S])):
        for generator,word in zip(GENERATORS,f.NWORDS):
            g=generator.copy()
            for action in actions:g=action(g)
            assert np.array_equal(g,literal([letter]+word+[-letter]))
    result={"status":"work in progress; exact representation certified",
            "quotient":"B/(gamma_4(H) H^3)","B_over_H_order":54,
            "H_dimensions":[10,45,120],"quotient_order":"54*3^175",
            "coordinates":"(E33 v,z; t_ijk=Magnus_ijk-Magnus_jik, i<j<k)",
            "actual_s_r_generator_substitutions":[[[2],[1]],[[2],[-2,-1]]],
            "literal_based_action_and_B_to_F_comparison":True,
            "all_cubes_killed_by_explicit_complete_central_cube_span":True,
            "exact_projection_to_E33":True,
            "ordinary_Lie_dimension":certificate["ordinary_Lie_dimension"],
            "complete_cube_span_dimension":certificate["complete_cube_span_dimension"],
            "triple_labels":[[i+1,j+1,k+1] for i,j,k in TRIPLES],
            "cube_span_preimages":certificate["cube_preimages"],
            "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_burnside.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_burnside.npz",S_images=S.images,
                       R_images=R.images,S_triple=S.triple,R_triple=R.triple,
                       pair_labels=np.array(PAIRS),triple_labels=np.array(TRIPLES))
    print(json.dumps({k:v for k,v in result.items() if k not in ("triple_labels","cube_span_preimages")},indent=2))
    print("PASS: actual exponent-three class-three quotient, complete cube span, and based B action.")

if __name__=="__main__":main()
