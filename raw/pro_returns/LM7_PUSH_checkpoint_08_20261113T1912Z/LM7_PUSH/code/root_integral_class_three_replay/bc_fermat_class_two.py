#!/usr/bin/env python3
"""The literal quotient H/(gamma_3(H) H^3) and its exact B action.

B=<s,r | s^2=r^3=1>, x=(r^-1 s)^2, y=(s r^-1)^2,
F=<x,y>, H=ker(F -> (Z/3)^2).  The ten H generators are the
signed Schreier words in de_fermat_schreier.py.  Coordinates are
logarithmic: (v,z)(w,t)=(v+w,z+t+(v wedge w)/2), with 1/2=2 in F3.
No square or cube relation is discarded before passing to this
actual exponent-three, class-two quotient.
"""
from pathlib import Path
from functools import cache
import json,time
import numpy as np
import de_fermat_schreier as f

HERE=Path(__file__).resolve().parent
PAIR_I,PAIR_J=f.UP
ZERO=np.zeros(55,dtype=np.int64)
IDENTITY=np.eye(55,dtype=np.int64)

def wedge(v,w):
    return (v[PAIR_I]*w[PAIR_J]-v[PAIR_J]*w[PAIR_I])%3

def multiply(g,h):
    out=(g+h)%3
    out[10:]=(out[10:]+2*wedge(g[:10],h[:10]))%3
    return out

def inverse(g):
    return -g%3

def commutator(g,h):
    return np.r_[np.zeros(10,dtype=np.int64),wedge(g[:10],h[:10])]

def collect_signed(word):
    """Collect an H word by exact integer prefix sums before reduction."""
    letters=np.asarray(word,dtype=np.int64)
    if not len(letters):return ZERO.copy()
    ix=np.abs(letters)-1
    signs=np.where(letters>0,1,-1)
    columns=np.zeros((10,10),dtype=np.int64)
    ab=np.zeros(10,dtype=np.int64)
    for i in range(10):
        entries=signs*(ix==i)
        ab[i]=entries.sum()
        prefix=np.cumsum(entries)-entries
        for j in range(10):
            mask=ix==j
            columns[i,j]=prefix[mask]@signs[mask]
    return np.r_[ab,2*(columns-columns.T)[PAIR_I,PAIR_J]]%3

def collect_f(word):
    """Return h,q for the exact factorization word=h*x^a*y^b."""
    q=(0,0);signed=[]
    for letter in word:
        qn=f.step(q,letter)
        edge=f.EDGES[q,letter] if letter>0 else -f.EDGES[qn,-letter]
        if edge:signed.append(edge)
        q=qn
    return q,collect_signed(signed)

def literal(word):
    q,h=collect_f(word)
    assert q==(0,0)
    return h

def block_action(ab,johnson):
    out=np.zeros((55,55),dtype=np.int64)
    out[:10,:10]=ab
    out[10:,:10]=johnson
    out[10:,10:]=f.exterior(ab)
    return out%3

def substitute(word,images):
    expanded={1:images[0],2:images[1]}
    expanded[-1]=f.inverse_word(expanded[1])
    expanded[-2]=f.inverse_word(expanded[2])
    return [letter for source in word for letter in expanded[source]]

def substituted_action(images):
    columns=np.stack([literal(substitute(w,images)) for w in f.NWORDS],axis=1)
    return block_action(columns[:10],columns[10:])

S=substituted_action(([2],[1]))
R=substituted_action(([2],[-2,-1]))
assert np.array_equal(S@S%3,IDENTITY)
assert np.array_equal(R@R@R%3,IDENTITY)

@cache
def deck_action(q):
    ab,johnson,_=f.action(q)
    return block_action(ab,johnson)

@cache
def carry(q,t):
    qt=((q[0]+t[0])%3,(q[1]+t[1])%3)
    return literal(f.section(q)+f.section(t)+f.inverse_word(f.section(qt)))

class FExtension:
    """Exact F/(gamma_3(H)H^3), with its nine Schreier cosets."""
    def __init__(self):
        self.one=((0,0),ZERO.copy())
        self.letters={i:collect_f([i]) for i in (1,-1,2,-2)}
    @staticmethod
    def equal(g,h):
        return g[0]==h[0] and np.array_equal(g[1],h[1])
    @staticmethod
    def mul(g,h):
        q,a=g;t,b=h
        qt=((q[0]+t[0])%3,(q[1]+t[1])%3)
        c=multiply(multiply(a,deck_action(q)@b%3),carry(q,t))
        return qt,c
    @staticmethod
    def inv(g):
        q,a=g;qi=((-q[0])%3,(-q[1])%3)
        return qi,multiply(-carry(qi,q)%3,deck_action(qi)@(-a)%3)
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=self.one
        while n:
            if n%2:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def comm(self,g,h):
        return self.mul(self.mul(self.mul(g,h),self.inv(g)),self.inv(h))
    def conj(self,g,h):
        return self.mul(self.mul(g,h),self.inv(g))
    @staticmethod
    def word(word):
        return collect_f(word)

def norm_errors(g):
    """Logs of (s f)^2 and (f^-1 r)^3 for f in H."""
    first=multiply(S@g%3,g)
    inv=-g%3
    second=multiply(multiply(inv,R@inv%3),R@R@inv%3)
    return np.r_[first,second]

def main():
    started=time.time()
    rng=np.random.default_rng(332026)
    ext=FExtension()
    for word in f.NWORDS+list(f.CUSP_WORDS.values()):
        expected=np.r_[*f.literal(word)]
        assert np.array_equal(literal(word),expected)
    for _ in range(80):
        word=rng.choice([1,-1,2,-2],size=30).tolist()
        q,h=collect_f(word)
        closed=word+f.inverse_word(f.section(q))
        assert np.array_equal(h,np.r_[*f.literal(closed)])
        g=ext.word(word)
        assert ext.equal(ext.mul(g,ext.inv(g)),ext.one)
        assert ext.equal(ext.mul(ext.inv(g),g),ext.one)
    for _ in range(80):
        a,b,c=[rng.choice([1,-1,2,-2],size=12).tolist() for __ in range(3)]
        aa,bb,cc=map(ext.word,(a,b,c))
        assert ext.equal(ext.mul(aa,bb),ext.word(a+b))
        assert ext.equal(ext.mul(ext.mul(aa,bb),cc),ext.mul(aa,ext.mul(bb,cc)))
    # Actual B words for x,y agree with inner conjugation, including Johnson blocks.
    x_action=R@R@S@R@R@S%3
    y_action=S@R@R@S@R@R%3
    for i,act in ((1,x_action),(2,y_action)):
        actual=np.stack([literal([i]+w+[-i]) for w in f.NWORDS],axis=1)
        assert np.array_equal(act[:,:10],actual)
    for _ in range(20):
        g=rng.integers(0,3,size=55)
        h=rng.integers(0,3,size=55)
        for action in (S,R):
            assert np.array_equal(action@multiply(g,h)%3,
                                  multiply(action@g%3,action@h%3))
        assert np.array_equal(multiply(multiply(g,g),g),ZERO)
        assert np.array_equal(multiply(multiply(multiply(g,h),inverse(g)),inverse(h)),
                              commutator(g,h))
    result={
        "quotient":"B/(gamma_3(H) H^3), H=ker(F2->C3^2)",
        "H_rank":10,"H_abelian_dimension":10,"H_central_dimension":45,
        "B_over_H_order":54,"quotient_order":"54*3^55",
        "S_action":S.tolist(),"R_action":R.tolist(),
        "S_Johnson_rank":f.rank(S[10:,:10]),
        "R_Johnson_rank":f.rank(R[10:,:10]),
        "S_squared_and_R_cubed_identity":True,
        "literal_B_to_F_inner_action_checked":True,
        "mixed_group_carries_and_inverse_checked":True,
        "all_cubes_and_brackets_retained":True,
        "elapsed_seconds":round(time.time()-started,3)}
    (HERE/"bc_fermat_class_two.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two.npz",S=S,R=R,
                        deck_actions=np.stack([deck_action(q) for q in f.Q]),
                        carries=np.stack([[carry(q,t) for t in f.Q] for q in f.Q]))
    print(json.dumps({k:v for k,v in result.items() if k not in ("S_action","R_action")},indent=2))
    print("PASS: exact Schreier class-two quotient, B action, and every carry.")

if __name__=="__main__":main()
