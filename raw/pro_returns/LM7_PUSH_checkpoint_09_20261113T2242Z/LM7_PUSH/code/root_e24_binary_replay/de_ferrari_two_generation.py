#!/usr/bin/env python3
"""Exact binary group collection and the five-generator Frattini comparison.

The coordinates are ordered by positive weight: unit degree d has
weight d, and an automorphism change in degree d+1 has weight d.
Products add in the first nonzero weight.  Squares and commutators
move to higher weight.  This produces an exact polycyclic collection
certificate in characteristic two, without logarithms.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo

here=Path(__file__).resolve().parent

class Collector:
    def __init__(self,H):
        self.H=H;self.rows={};self.basis=[];self.inverses=[];self.expressions=[];self.weights=[]
        self.coordinate_weights=[]
        for weight in range(1,H.algebra.degree+1):
            self.coordinate_weights += [weight]*(2**weight)
            if weight<H.algebra.degree:self.coordinate_weights += [weight]*(2**(weight+2))
    def vector(self,x):
        H=self.H;images=H.aut.images[int(x[-1])]
        assert np.array_equal(images[:,:2],np.eye(2,dtype=np.int16))
        coordinates=[]
        for weight in range(1,H.algebra.degree+1):
            coordinates.extend(x[H.algebra.blocks[weight]])
            if weight<H.algebra.degree:coordinates.extend(images[:,H.algebra.blocks[weight+1]].ravel())
        return np.array(coordinates,dtype=np.int64)%2
    def reduce(self,x):
        v=self.vector(x);coeff=[]
        for pivot,index in sorted(self.rows.items()):
            if v[pivot]:
                x=self.H.mul(x,self.inverses[index]);coeff.append(index);v=self.vector(x)
                assert all(v[p]==0 for p in self.rows if p<=pivot)
        return x,coeff
    def add(self,x,expression):
        y,coeff=self.reduce(x);v=self.vector(y);nz=np.flatnonzero(v)
        if not len(nz):
            assert np.array_equal(y,self.H.one);return False
        pivot=int(nz[0]);assert pivot not in self.rows
        index=len(self.basis);self.rows[pivot]=index;self.basis.append(y);self.inverses.append(self.H.inv(y))
        self.weights.append(self.coordinate_weights[pivot]);self.expressions.append({'start':expression,'right_inverse_factors':coeff})
        return True
    def close(self,generators,expressions=None):
        if expressions is None:expressions=[{'input_generator':i} for i in range(len(generators))]
        for g,e in zip(generators,expressions):self.add(g,e)
        at=0
        while at<len(self.basis):
            a=self.basis[at]
            self.add(self.H.power(a,2),{'square_of_basis':at})
            for j in range(at):self.add(self.H.comm(a,self.basis[j]),{'commutator_of_basis':[at,j]})
            at+=1
        return self
    def verify(self):
        powers=[];commutators=[]
        for i,a in enumerate(self.basis):
            residual,coeff=self.reduce(self.H.power(a,2));assert np.array_equal(residual,self.H.one)
            assert all(self.weights[j]>self.weights[i] for j in coeff)
            powers.append(coeff)
            for j,b in enumerate(self.basis[:i]):
                residual,coeff=self.reduce(self.H.comm(a,b));assert np.array_equal(residual,self.H.one)
                assert all(self.weights[k]>max(self.weights[i],self.weights[j]) for k in coeff)
                if coeff:commutators.append({'indices':[i,j],'right_reduction_factors':coeff})
        return powers,commutators
    def contains(self,g):return np.array_equal(self.reduce(g)[0],self.H.one)

def kernel_generators(H):
    return [H.xi1,H.xi2,H.power(H.a,2),H.power(H.b,2),H.power(H.mul(H.a,H.b),3)]

def main():
    start=time.time();low=FerrariTwo(2);lowgens=kernel_generators(low)
    lowC=Collector(low).close(lowgens);lowpowers,lowcomms=lowC.verify();assert len(lowC.basis)==8
    frattinigens=[low.power(g,2) for g in lowgens]
    frattinigens += [low.comm(a,b) for i,a in enumerate(lowgens) for b in lowgens[:i]]
    Phi=Collector(low).close(frattinigens);Phi.verify();assert len(Phi.basis)==3
    for g in lowgens:
        for k in Phi.basis:assert Phi.contains(low.conj(g,k))
    assert len(lowC.basis)-len(Phi.basis)==5
    H=FerrariTwo(6);generators=kernel_generators(H)
    literal_words=[[3,-1],[1,2,1,-3,-2,-1],[1,1],[2,2],[1,2]*3]
    C=Collector(H).close(generators,[{'literal_B4_word':w} for w in literal_words])
    powers,commutators=C.verify()
    for a in (H.a,H.b):
        for k in C.basis:assert C.contains(H.conj(a,k))
    for g in generators:assert C.contains(g)
    assert all(lowC.contains(H.to_lower(g,low)) for g in generators)
    order=6*2**len(C.basis)
    # Exact AGL2(F2) permutation comparison, in this order of four points.
    points=[(0,1),(1,1),(1,0),(0,0)];permutations=[]
    for g in (H.a,H.b,H.c):
        project=H.project(g);A=project[:4].reshape(2,2);b=project[4:]
        permutations.append([points.index(tuple((A@np.array(p)+b)%2)) for p in points])
    assert permutations==[[1,0,2,3],[0,2,1,3],[0,1,3,2]]
    inputs=json.loads(here.joinpath('de_ferrari_two_lift.json').read_text())['records'];rows=[]
    for rec in inputs:
        witness=rec['chosen_witness'];assert witness is not None
        images=[H.decode(a) for a in witness['actual_binary_braid_images']];H.check_braids(images)
        assert all(np.array_equal(H.to_lower(a,low),b) for a,b in zip(images,(low.a,low.b,low.c)))
        rows.append({'certificate_index':rec['certificate_index'],'missing_coset':rec['missing_coset'],
            'full_target_order':order,'same_degree_two_generators':True,
            'generation_by_five_dimensional_Frattini_comparison':True})
    out={'binary_degree':6,'normal_two_group_polycyclic_length':len(C.basis),
        'binary_four_strand_target_order':order,'degree_two_normal_two_group_order':2**len(lowC.basis),
        'degree_two_Frattini_subgroup_order':2**len(Phi.basis),'Frattini_quotient_rank':5,
        'standard_permutation_map_factors_through_binary_target':True,
        'standard_adjacent_transposition_images':permutations,
        'basis_pivots':list(C.rows),'basis_weights':C.weights,
        'literal_source_expression_DAG':C.expressions,
        'actual_polycyclic_basis':[H.encode(g) for g in C.basis],
        'square_collection_relations':powers,'nontrivial_commutator_collection_relations':commutators,
        'records':rows,'registered_automorphisms':H.aut.count,'elapsed_seconds':round(time.time()-start,3),
        'scope':'Exact positive-weight group collection; every current lift has unchanged degree-two generators and hence generates the whole higher binary target.'}
    here.joinpath('de_ferrari_two_generation.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','actual_polycyclic_basis','literal_source_expression_DAG','square_collection_relations','nontrivial_commutator_collection_relations')},indent=2),flush=True)

if __name__=='__main__':main()
