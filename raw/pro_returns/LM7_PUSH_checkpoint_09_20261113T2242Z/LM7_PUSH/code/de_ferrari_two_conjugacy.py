#!/usr/bin/env python3
"""Complete conjugacy by exact central-filtration lifting in binary Ferrari U.

U is the collected kernel of the map to SL2(F2).  Unit degree d and
automorphism increment degree d+1 have weight d.  At each layer the
full current centralizer is retained, as the kernel of an exact
commutator homomorphism to an elementary abelian layer.  No division,
logarithm, selected-conjugator-only inference, or truncated fibre is used.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_generation import Collector,kernel_generators
from de_ferrari_two_core import solve2,rref2

class Conjugacy:
    def __init__(self,H,x):
        self.H=H;self.x=x;self.U=Collector(H).close(kernel_generators(H))
        self.U.verify();self.weights=np.array(self.U.coordinate_weights)
        # Enumerate the six actual cosets via the linear action, retaining
        # literal representatives in the original braid generators.
        reps=[H.one];words=[[]];lookup={self.linear_key(H.one):0}
        for j,g in enumerate(reps):
            for i,a in enumerate((H.a,H.b),1):
                h=H.mul(g,a);key=self.linear_key(h)
                if key not in lookup:lookup[key]=len(reps);reps.append(h);words.append(words[j]+[i])
        assert len(reps)==6
        self.charts=[]
        for ix,g in enumerate(reps):
            x0=H.conj(g,x);C=self.U;layers=[]
            for weight in range(1,H.algebra.degree+1):
                mask=self.weights==weight;lower=self.weights<weight
                ordered=[C.basis[j] for p,j in sorted(C.rows.items())]
                columns=[]
                for c in ordered:
                    v=self.U.vector(H.comm(c,x0));assert not np.any(v[lower]);columns.append(v[mask])
                L=np.array(columns,dtype=np.int64).T if columns else np.zeros((sum(mask),0),dtype=np.int64)
                _,piv=rref2(L);rank=len(piv)
                zero=np.zeros(sum(mask),dtype=np.int64);solution=solve2(L,zero);assert solution is not None
                _,kernel=solution
                # RREF rows have distinct first nonzero polycyclic
                # coordinates.  Their actual products lie in ker L.
                KR,kp=rref2(kernel.T);kernel_rows=KR[:len(kp)]
                generators=[]
                for coeff in kernel_rows:
                    c=self.multiply(ordered,coeff)
                    v=self.U.vector(H.comm(c,x0));assert not np.any(v[self.weights<=weight])
                    generators.append(c)
                nextC=Collector(H).close(generators);nextC.verify()
                # The homomorphism image has order2^rank; this exact
                # subgroup order proves that no centralizer lifts were lost.
                assert len(nextC.basis)==len(C.basis)-rank
                for c in nextC.basis:
                    assert C.contains(c)
                    assert not np.any(self.U.vector(H.comm(c,x0))[self.weights<=weight])
                layers.append({'weight':weight,'basis':ordered,'matrix':L,
                               'centralizer_log2_before':len(C.basis),
                               'commutator_image_rank':rank,'centralizer_log2_after':len(nextC.basis)})
                C=nextC
            assert all(np.array_equal(H.comm(c,x0),H.one) for c in C.basis)
            self.charts.append({'coset':ix,'representative':g,'representative_word':words[ix],
                                'x0':x0,'layers':layers,'final_centralizer':C})
    def linear_key(self,x):
        return tuple(self.H.aut.images[int(x[-1]),:,:2].ravel())
    def multiply(self,basis,coeff):
        out=self.H.one.copy()
        for a,c in zip(basis,coeff):
            if c:out=self.H.mul(out,a)
        return out
    def conjugator(self,y):
        H=self.H
        if self.linear_key(y)!=self.linear_key(H.one):return None
        failures=[]
        for chart in self.charts:
            h=H.one.copy();history=[];failed=False
            for layer in chart['layers']:
                weight=layer['weight'];delta=H.mul(y,H.inv(H.conj(h,chart['x0'])))
                v=self.U.vector(delta);assert not np.any(v[self.weights<weight])
                rhs=v[self.weights==weight];solution=solve2(layer['matrix'],rhs)
                if solution is None:
                    failures.append({'coset':chart['coset'],'first_failed_weight':weight,
                                     'rhs':rhs.tolist()});failed=True;break
                coeff,_=solution;c=self.multiply(layer['basis'],coeff);h=H.mul(h,c)
                residual=self.U.vector(H.mul(y,H.inv(H.conj(h,chart['x0']))))
                assert not np.any(residual[self.weights<=weight])
                history.append(coeff.tolist())
            if not failed:
                g=H.mul(h,chart['representative'])
                assert np.array_equal(H.conj(g,self.x),y) and self.U.contains(h)
                return {'conjugator':g,'U_factor':h,'outer_coset':chart['coset'],
                        'outer_word':chart['representative_word'],'layer_coefficients':history}
        return None
    def metadata(self):
        return [{'outer_coset':c['coset'],'outer_word':c['representative_word'],
                 'layer_ranks':[l['commutator_image_rank'] for l in c['layers']],
                 'centralizer_log2':[l['centralizer_log2_before'] for l in c['layers']]+[len(c['final_centralizer'].basis)]}
                for c in self.charts]

def audit_small():
    start=time.time();H=FerrariTwo(2);x=H.power(H.mul(H.mul(H.a,H.b),H.c),2);C=Conjugacy(H,x)
    seen={tuple(H.one)};elements=[H.one]
    for g in elements:
        for a in (H.a,H.b,H.c):
            y=H.mul(g,a);key=tuple(y)
            if key not in seen:seen.add(key);elements.append(y)
    assert len(elements)==1536
    orbit={tuple(H.conj(g,x)) for g in elements}
    for y in elements:assert (C.conjugator(y) is not None)==(tuple(y) in orbit)
    out={'degree':2,'target_order':1536,'exact_conjugacy_class_size':len(orbit),
         'all1536_elements_compared_with_complete_enumeration':True,'centralizer_charts':C.metadata(),
         'seconds':round(time.time()-start,3)}
    Path(__file__).with_name('de_ferrari_two_conjugacy_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':audit_small()
