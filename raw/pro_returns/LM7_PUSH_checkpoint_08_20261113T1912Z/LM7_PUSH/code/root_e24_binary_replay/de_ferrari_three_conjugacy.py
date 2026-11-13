#!/usr/bin/env python3
"""Complete conjugacy above the exact 648-element Ferrari quotient.

Only the already-certified class-two exponent-three kernel is logged.
Its full centralizer fibre is retained at both stages.  Every base
conjugator is enumerated, and every successful lift is an actual group
element with an independently evaluable literal B4 word.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix
from de_ferrari_mod9_lift import Span,solve,rref
import de_ferrari_class2_model as old

here=Path(__file__).resolve().parent

def inverse_word(w):return [-t for t in w[::-1]]

def reduce_word(w):
    out=[]
    for t in w:
        if out and out[-1]==-t:out.pop()
        else:out.append(int(t))
    return out

def braid_word(H,w):
    images={1:H.a,2:H.b,3:H.c}
    images.update({-i:H.inv(g) for i,g in list(images.items())})
    out=H.one.copy()
    for t in w:out=H.mul(out,images[t])
    return out

class Conjugacy:
    def __init__(self,H,x):
        self.H=H;self.x=x
        lowgens=[tuple(int(t) for t in H.project(g)) for g in (H.a,H.b,H.c)]
        self.base=[old.one];self.section=[H.one.copy()];self.section_words=[[]]
        lookup={old.one:0};self.K=Span(367)
        for i,q in enumerate(self.base):
            for letter,(g,lg) in enumerate(zip((H.a,H.b,H.c),lowgens),1):
                qn=old.mul(q,lg);element=H.mul(self.section[i],g)
                word=self.section_words[i]+[letter];j=lookup.get(qn)
                if j is None:
                    lookup[qn]=len(self.base);self.base.append(qn)
                    self.section.append(element);self.section_words.append(word)
                else:
                    k=H.mul(element,H.inv(self.section[j]))
                    self.K.add(H.log_kernel(k),reduce_word(word+inverse_word(self.section_words[j])))
        assert len(self.base)==648
        # Include every actual commutator required for BCH closure.
        at=0
        while at<len(self.K.basis):
            a=H.exp_kernel(self.K.basis[at]);aw=self.K.words[at]
            for j,b in enumerate(list(self.K.basis)):
                bw=self.K.words[j]
                self.K.add(H.log_kernel(H.comm(a,H.exp_kernel(b))),
                           reduce_word(aw+bw+inverse_word(aw)+inverse_word(bw)))
            at+=1
        assert len(self.K.basis)==30
        saved=np.load(here/'de_ferrari_degree6_generation_certificate.npz')['target_kernel_Lie_basis']
        assert saved.shape==(367,30)
        for v in saved.T:self.K.coordinates(v)
        self.M=self.K.matrix();self.elements=[H.exp_kernel(v) for v in self.K.basis]
        self.Z=Span(30)
        for i,a in enumerate(self.elements):
            assert np.array_equal(H.power(a,3),H.one)
            assert np.array_equal(braid_word(H,self.K.words[i]),a)
            for j,b in enumerate(self.elements):
                z=self.coordinates(H.comm(a,b));aw,bw=self.K.words[i],self.K.words[j]
                self.Z.add(z,reduce_word(aw+bw+inverse_word(aw)+inverse_word(bw)))
        assert len(self.Z.basis)==18
        for z in self.Z.basis:
            ze=self.element(z)
            for a in self.elements:assert np.array_equal(H.comm(ze,a),H.one)
        self.ZM=self.Z.matrix()
        free=[j for j in range(30) if j not in self.Z.rows]
        self.Q=np.column_stack([self.Z.reduce(e)[0][free] for e in np.eye(30,dtype=np.int64)])
        assert self.Q.shape==(12,30) and not np.any(self.Q@self.ZM%3)
        self.A=np.column_stack([self.coordinates(H.conj(x,a)) for a in self.elements])
        L=np.eye(30,dtype=np.int64)-self.A
        self.first=self.Q@L%3
        _,self.C1=solve(self.first,np.zeros(12,dtype=np.int64))
        self.second=L@self.C1%3
        assert not np.any(self.Q@self.second%3)
        for v in self.C1.T:
            # This exact substitution also certifies the sign of I-Ad(x).
            assert np.array_equal(self.coordinates(H.comm(self.element(v),x)),L@v%3)
        _,C2=solve(self.second,np.zeros(30,dtype=np.int64));self.C2=self.C1@C2%3
        for v in self.C2.T:assert np.array_equal(H.comm(self.element(v),x),H.one)
        self.by_base={}
        xbar=tuple(int(t) for t in H.project(x))
        for i,q in enumerate(self.base):
            ybar=old.mul(old.mul(q,xbar),old.inv(q))
            self.by_base.setdefault(ybar,[]).append(i)
        self.cache={};self.failed_certificates={}

    def coordinates(self,x):return self.K.coordinates(self.H.log_kernel(x))
    def element(self,v):return self.H.exp_kernel(self.M@np.array(v,dtype=np.int64)%3)

    def word_from_log(self,v):
        H=self.H;v=np.array(v,dtype=np.int64)%3;out=H.one.copy();word=[]
        for c,g,w in zip(v,self.elements,self.K.words):
            if c:out=H.mul(out,H.power(g,int(c)));word+=w*int(c)
        error=self.coordinates(H.mul(self.element(v),H.inv(out)))
        z=self.Z.coordinates(error)
        for c,w in zip(z,self.Z.words):
            if c:word+=w*int(c)
        word=reduce_word(word)
        assert np.array_equal(braid_word(H,word),self.element(v))
        return word

    def conjugator(self,y):
        H=self.H;key=bytes(np.asarray(y,dtype=np.int64))
        if key in self.cache:return self.cache[key]
        ybar=tuple(int(t) for t in H.project(y));failures=[]
        for i in self.by_base.get(ybar,[]):
            g0=self.section[i];target=H.conj(H.inv(g0),y)
            delta=self.coordinates(H.mul(target,H.inv(self.x)))
            first=solve(self.first,self.Q@delta%3)
            if first is None:
                failures.append({'base_coset':i,'failed_stage':1,'rhs':(self.Q@delta%3).tolist()});continue
            u,_=first;h0=self.element(u)
            error=self.coordinates(H.mul(target,H.inv(H.conj(h0,self.x))))
            assert not np.any(self.Q@error%3)
            second=solve(self.second,error)
            if second is None:
                failures.append({'base_coset':i,'failed_stage':2,'rhs':error.tolist()});continue
            coeff,_=second;v=self.C1@coeff%3
            h=H.mul(h0,self.element(v));g=H.mul(g0,h)
            assert np.array_equal(H.conj(g,self.x),y)
            word=reduce_word(self.section_words[i]+self.word_from_log(u)+self.word_from_log(v))
            assert np.array_equal(braid_word(H,word),g)
            out={'base_coset':i,'first_log_coordinates':u.tolist(),
                 'second_log_coordinates':v.tolist(),'literal_B4_conjugator':word,
                 'conjugator':H.encode(g),'all_previous_base_failures':failures}
            self.cache[key]=out;return out
        self.cache[key]=None;self.failed_certificates[key]=failures;return None

    def metadata(self):
        return {'base_quotient_order':648,'kernel_log_dimension':30,
                'kernel_central_derived_dimension':18,
                'first_commutator_rank':len(rref(self.first)[1]),
                'first_centralizer_log_dimension':self.C1.shape[1],
                'second_commutator_rank':len(rref(self.second)[1]),
                'full_kernel_centralizer_log_dimension':self.C2.shape[1],
                'base_conjugacy_class_size':len(self.by_base),
                'base_conjugator_fibre_sizes':sorted(set(map(len,self.by_base.values())))}

def audit_class_two():
    """Exhaustive independent check of both lifting stages in a 243-group.

    J is the free class-two exponent3 group on three generators
    modulo the central relation [b,c]=1 (order3^5).
    An order3 automorphism acts nontrivially on J/Jprime.  Every target
    in its fixed quotient coset is compared with all 243 conjugators.
    """
    # The actual group J has coordinates (a,b,c,z_ab,z_ac), with
    # [b,c]=0.  A cycles b->b+c->b+2c and fixes a, inducing
    # z_ab->z_ab+z_ac.  The class-two BCH product is exact at p=3.
    def bracket(u,v):
        out=np.zeros(5,dtype=np.int64)
        out[3]=(u[0]*v[1]-u[1]*v[0])%3
        out[4]=(u[0]*v[2]-u[2]*v[0])%3
        return out
    def mul(u,v):return (u+v+2*bracket(u,v))%3
    A=np.eye(5,dtype=np.int64);A[2,1]=1;A[4,3]=1
    assert np.array_equal(np.linalg.matrix_power(A,3)%3,np.eye(5,dtype=np.int64))
    vectors=[np.array(v,dtype=np.int64) for v in product(range(3),repeat=5)]
    orbit={tuple(mul(u,-A@u%3)) for u in vectors}
    L=(np.eye(5,dtype=np.int64)-A)%3;first=L[:3]
    _,C1=solve(first,np.zeros(3,dtype=np.int64));second=L@C1%3
    decisions=[]
    for y in vectors:
        sol=solve(first,y[:3]);passed=False
        if sol is not None:
            u,_=sol
            current=mul(u,-A@u%3)
            error=mul(y,-current%3)
            assert not np.any(error[:3])
            sol2=solve(second,error)
            if sol2 is not None:
                v=C1@sol2[0]%3;h=mul(u,v)
                assert np.array_equal(mul(h,-A@h%3),y);passed=True
        assert passed==(tuple(y) in orbit);decisions.append(passed)
    out={'exact_group_order':243,'complete_conjugacy_class_size':len(orbit),
         'all243_targets_compared_with_all243_conjugators':True,
         'first_stage_rank':len(rref(first)[1]),'second_stage_rank':len(rref(second)[1])}
    here.joinpath('de_ferrari_three_conjugacy_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':audit_class_two()
