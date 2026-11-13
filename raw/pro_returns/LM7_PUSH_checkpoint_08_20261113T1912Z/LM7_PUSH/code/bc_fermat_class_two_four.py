#!/usr/bin/env python3
"""The literal exponent-four H-class-two quotient, retaining every square.

Hall coordinates are eta_1^v1 ... eta_10^v10 times ordered commutators.
The abelian exponents lie in Z/4 and the 45 commutators in F2.
In a class-two exponent-four group, [a,b]^2=1 follows from
(ab)^4=a^4 b^4 [b,a]^6 and [a,b]^4=1.  Conversely the multiplication
below has exponent four and gives all independent collected words.
"""
from pathlib import Path
from functools import cache
import json,time
import numpy as np
import de_fermat_schreier as f

HERE=Path(__file__).resolve().parent
I,J=f.UP
ZERO=np.zeros(55,dtype=np.int64)

def multiply(g,h):
    return np.r_[(g[:10]+h[:10])%4,(g[10:]+h[10:]-g[J]*h[I])%2]

def inverse(g):
    return np.r_[-g[:10]%4,(g[10:]+g[I]*g[J])%2]

def power(g,n):
    return np.r_[n*g[:10]%4,(n*g[10:]-(n*(n-1)//2)*g[I]*g[J])%2]

def commutator(g,h):
    return np.r_[np.zeros(10,dtype=np.int64),
                 (g[I]*h[J]-g[J]*h[I])%2]

def collect_signed(word):
    letters=np.asarray(word,dtype=np.int64)
    if not len(letters):return ZERO.copy()
    ix=np.abs(letters)-1;signs=np.where(letters>0,1,-1)
    a=np.zeros(10,dtype=np.int64);columns=np.zeros((10,10),dtype=np.int64)
    for i in range(10):
        entries=signs*(ix==i);a[i]=entries.sum()
        prefix=np.cumsum(entries)-entries
        for j in range(10):
            mask=ix==j;columns[i,j]=prefix[mask]@signs[mask]
    return np.r_[a%4,-columns[J,I]%2]

def collect_f(word):
    deck=(0,0);signed=[]
    for letter in word:
        nxt=f.step(deck,letter)
        edge=f.EDGES[deck,letter] if letter>0 else -f.EDGES[nxt,-letter]
        if edge:signed.append(edge)
        deck=nxt
    return deck,collect_signed(signed)

def literal(word):
    deck,h=collect_f(word);assert deck==(0,0)
    return h

def substitute(word,images):
    image={1:images[0],2:images[1]}
    image[-1]=f.inverse_word(image[1]);image[-2]=f.inverse_word(image[2])
    return [letter for a in word for letter in image[a]]

class Action:
    def __init__(self,images):
        self.images=np.asarray(images,dtype=np.int64)
        self.ab=self.images[:10]
        self.johnson=self.images[10:]
        self.square=(self.ab[J]*self.ab[I])%2
        self.cross=np.stack([(self.ab[J,i]*self.ab[I,j])%2
                             for i,j in zip(I,J)],axis=1)
        self.wedge=np.stack([(self.ab[I,i]*self.ab[J,j]-self.ab[J,i]*self.ab[I,j])%2
                             for i,j in zip(I,J)],axis=1)
    def __call__(self,g):
        v=g[:10];low=v%2
        z=(self.johnson@low+self.square@((v*(v-1)//2)%2)+
           self.cross@(low[I]*low[J])+self.wedge@g[10:])%2
        return np.r_[self.ab@v%4,z]

def substituted_action(images):
    return Action(np.stack([literal(substitute(w,images)) for w in f.NWORDS],axis=1))

S=substituted_action(([2],[1]))
R=substituted_action(([2],[-2,-1]))

@cache
def deck_action(deck):
    word=f.section(deck)
    return Action(np.stack([literal(word+w+f.inverse_word(word)) for w in f.NWORDS],axis=1))

@cache
def carry(deck,other):
    total=tuple((a+b)%3 for a,b in zip(deck,other))
    return literal(f.section(deck)+f.section(other)+f.inverse_word(f.section(total)))

class FExtension:
    def __init__(self):self.one=((0,0),ZERO.copy())
    @staticmethod
    def equal(g,h):return g[0]==h[0] and np.array_equal(g[1],h[1])
    @staticmethod
    def mul(g,h):
        a,x=g;b,y=h;ab=tuple((i+j)%3 for i,j in zip(a,b))
        return ab,multiply(multiply(x,deck_action(a)(y)),carry(a,b))
    @staticmethod
    def inv(g):
        a,x=g;ai=tuple(-i%3 for i in a)
        return ai,multiply(inverse(carry(ai,a)),deck_action(ai)(inverse(x)))
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=self.one
        while n:
            if n%2:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def conj(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def comm(self,g,h):return self.mul(self.conj(g,h),self.inv(h))
    @staticmethod
    def word(w):return collect_f(w)

def norm_errors(g):
    first=multiply(S(g),g)
    inv=inverse(g)
    second=multiply(multiply(inv,R(inv)),R(R(inv)))
    return np.r_[first,second]

def central_vector(g):
    assert not np.any(g[:10]%2)
    return np.r_[g[:10]//2,g[10:]]

def central_element(g):
    return np.r_[2*g[:10]%4,g[10:]%2]

def main():
    start=time.time();ext=FExtension();rng=np.random.default_rng(4342026)
    for i,word in enumerate(f.NWORDS):
        target=ZERO.copy();target[i]=1
        assert np.array_equal(literal(word),target)
        assert np.array_equal(S(S(target)),target)
        assert np.array_equal(R(R(R(target))),target)
    for _ in range(80):
        a,b,c=[np.r_[rng.integers(0,4,size=10),rng.integers(0,2,size=45)] for __ in range(3)]
        assert np.array_equal(multiply(multiply(a,b),c),multiply(a,multiply(b,c)))
        assert np.array_equal(multiply(a,inverse(a)),ZERO)
        assert np.array_equal(power(a,4),ZERO)
        assert np.array_equal(power(a,2),multiply(a,a))
        assert np.array_equal(commutator(a,b),multiply(multiply(multiply(a,b),inverse(a)),inverse(b)))
        for act in (S,R):
            assert np.array_equal(act(multiply(a,b)),multiply(act(a),act(b)))
        assert np.array_equal(S(S(a)),a) and np.array_equal(R(R(R(a))),a)
    for _ in range(40):
        a,b=[rng.choice([1,-1,2,-2],size=20).tolist() for __ in range(2)]
        assert ext.equal(ext.mul(ext.word(a),ext.word(b)),ext.word(a+b))
        assert ext.equal(ext.mul(ext.word(a),ext.inv(ext.word(a))),ext.one)
    for i,word in enumerate(f.NWORDS):
        g=ZERO.copy();g[i]=1
        assert np.array_equal(R(R(S(R(R(S(g)))))),literal([1]+word+[-1]))
        assert np.array_equal(S(R(R(S(R(R(g)))))),literal([2]+word+[-2]))
    central_actions=[]
    for act in (S,R):
        central_actions.append(np.stack([central_vector(act(central_element(e)))
                                        for e in np.eye(55,dtype=np.int64)],axis=1))
    result={"quotient":"B/(gamma_3(H)H^4)","H_order":"2^65",
            "H_abelian_group":"(Z/4)^10","H_commutator_group":"(Z/2)^45",
            "H_Frattini_group":"(Z/2)^55",
            "all_squares_retained":True,"literal_B_and_F_actions_checked":True,
            "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_two_four.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_two_four.npz",
                        S_images=S.images,R_images=R.images,
                        S_central_action=central_actions[0],
                        R_central_action=central_actions[1])
    print(json.dumps(result,indent=2))
    print("PASS: exact exponent-four Hall collector, all squares, and literal B action.")

if __name__=="__main__":main()
