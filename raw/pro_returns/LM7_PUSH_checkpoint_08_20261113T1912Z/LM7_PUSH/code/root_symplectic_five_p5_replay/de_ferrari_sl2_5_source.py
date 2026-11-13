#!/usr/bin/env python3
"""Complete elementary-abelian kernel of the induced SL2(F5) source."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_degree4_lift import InducedCombined
from de_lifted_schreier_kernel import lifted_kernel

here=Path(__file__).resolve().parent

class Source:
    def __init__(self):
        with redirect_stdout(io.StringIO()):self.d=runpy.run_path(str(here/'de_distribution_test.py'))
        self.H=FerrariSL2Five();self.W=InducedCombined(self.H,self.d)
        compression=json.loads((here/'de_ferrari_a5_source_compressed.json').read_text())
        self.keep=np.array([x for orbit in compression['retained_original_canonical_orders'] for x in orbit],dtype=np.int64)
        self.renumber=np.full(6840,-1,dtype=np.int64);self.renumber[self.keep]=np.arange(len(self.keep))
        self.points=[(0,0),(1,0),(0,1),(1,1)]
    def affine_permutation(self,e):
        H=self.H;out=[]
        for q in range(6):
            for i in range(6):
                inverse=H.inv(e[1][q,i]);M=inverse[76:80].reshape(2,2);t=inverse[99:]
                p=[self.points.index(tuple((M@np.array(v)+t)%2)) for v in self.points]
                out.extend(4*(6*int(e[0][q])+i)+np.array(p))
        return Permutation([int(t) for t in out])
    def permutation(self,e):
        H=self.H;out=[];a5=H.project_a5(e[1])
        for q in range(6):
            for i in range(6):
                p=H.old.permutation(a5[q,i]).array_form
                out.extend(190*(6*int(e[0][q])+i)+np.array(p))
        compressed=self.renumber[np.array(out,dtype=np.int64)[self.keep]]
        assert np.all(compressed>=0)
        affine=self.affine_permutation(e).array_form
        return Permutation(compressed.tolist()+[len(self.keep)+j for j in affine])
    def vector(self,e):
        assert np.array_equal(e[0],self.W.id)
        return self.H.relative_kernel_vector(e[1]).ravel()
    def element(self,v):return self.W.id,self.H.relative_kernel_element(v.reshape(6,6,57))

def main():
    start=time.time();model=Source();H,W=model.H,model.W
    gs=[W.letters[0],W.letters[1]];ps=[model.permutation(g) for g in gs]
    for a in (W.letters[0],W.letters[1],W.letters[-1]):
        for b in gs:assert model.permutation(W.mul(a,b))==model.permutation(a)*model.permutation(b)
    compressed=np.load(here/'de_ferrari_a5_source_compressed.npz')
    assert np.array_equal(np.array(ps[0].array_form)[:1980],compressed['s'])
    assert np.array_equal(np.array(ps[1].array_form)[:1980],compressed['r'])
    Aff=PermutationGroup([model.affine_permutation(g) for g in gs]);afforder=int(Aff.order())
    print('exact affine source image order',afforder,flush=True)
    G,S,info=lifted_kernel(W,gs,ps,model.vector,model.element,36*57)
    oldorder=json.loads((here/'de_ferrari_a5_source.json').read_text())['induced_B_image_order']
    assert info['base_order']%oldorder==0
    out={**info,'faithful_base_permutation_degree':2124,
         'old_A5_source_order':oldorder,'affine_source_order':afforder,
         'base_index_over_A5_source':info['base_order']//oldorder,
         'base_common_quotient_order':oldorder*afforder//info['base_order'],
         'actual_source_kernel_elementary_abelian':True,
         'all36_induced_evaluation_coordinates_retained':True,
         'total_seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_sl2_5_source.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_sl2_5_source.npz',full_kernel_basis=S.matrix(),
                        s=np.array(ps[0].array_form),r=np.array(ps[1].array_form),
                        base_strong_generators=np.array([p.array_form for p in G.strong_gens]))
    print(json.dumps({k:v for k,v in out.items() if k not in ('literal_word_DAG','kernel_basis_word_nodes')},indent=2),flush=True)

if __name__=='__main__':main()
