#!/usr/bin/env python3
"""Independent exhaustive controls for the lifted Schreier presentation.

These controls enumerate every element of each actual small group and
compare its kernel with the complete lifted presentation.  The A4
control needs the normal closure of an extra lift; the Heisenberg
control needs a relator which is invisible in the quotient.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io, json, time
import numpy as np
from sympy.combinatorics import Permutation
from de_lifted_schreier_extra import lifted_kernel

here=Path(__file__).resolve().parent

class SmallGroup:
    def __init__(self, kind):
        self.kind=kind
        self.one=np.zeros(3,dtype=np.int64)
        self.R=np.array([[0,1],[1,1]],dtype=np.int64)
    def mul(self,a,b):
        if self.kind=='A4':
            M=np.linalg.matrix_power(self.R,int(a[2]))%2
            return np.r_[(a[:2]+M@b[:2])%2,(int(a[2])+int(b[2]))%3]
        return np.array([(a[0]+b[0])%2,(a[1]+b[1])%2,
                         (a[2]+b[2]+a[1]*b[0])%2],dtype=np.int64)
    def inv(self,a):
        if self.kind=='A4':
            i=-int(a[2])%3
            return np.r_[np.linalg.matrix_power(self.R,i)@a[:2]%2,i]
        return np.array([a[0],a[1],(a[2]+a[1]*a[0])%2],dtype=np.int64)
    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))
    def vector(self,a):
        if self.kind=='A4':
            assert a[2]==0
            return a[:2].copy()
        assert not np.any(a[:2])
        return a[2:].copy()
    def element(self,v):
        return np.r_[v,0] if self.kind=='A4' else np.r_[0,0,v]
    def permutation(self,a):
        if self.kind=='A4':return Permutation([(j+int(a[2]))%3 for j in range(3)])
        return Permutation([j^(int(a[0])+2*int(a[1])) for j in range(4)])

def exhaustive(H,gens):
    values=[H.one];seen={tuple(H.one)}
    for a in values:
        for g in gens:
            b=H.mul(a,g);key=tuple(b)
            if key not in seen:seen.add(key);values.append(b)
    for a in values:
        assert np.array_equal(H.mul(a,H.inv(a)),H.one)
        for b in values:
            assert H.permutation(H.mul(a,b))==H.permutation(a)*H.permutation(b)
    return values

def main():
    start=time.time();records=[]
    for kind in ('A4','Heisenberg_F2'):
        H=SmallGroup(kind)
        if kind=='A4':
            gs=[np.array([0,0,1],dtype=np.int64)]
            extra=[np.array([1,0,0],dtype=np.int64)];width=2;order=12
        else:
            gs=[np.array([1,0,0],dtype=np.int64),np.array([0,1,0],dtype=np.int64)]
            extra=[];width=1;order=8
        values=exhaustive(H,gs+extra)
        assert len(values)==order
        with redirect_stdout(io.StringIO()) as log:
            G,V,info=lifted_kernel(H,gs,[H.permutation(g) for g in gs],
                H.vector,H.element,width,extra_lifts=[(H.permutation(g),g) for g in extra],
                normalizers=gs)
        identity=H.permutation(H.one)
        exact={tuple(H.vector(g)) for g in values if H.permutation(g)==identity}
        generated={tuple(np.zeros(width,dtype=np.int64))}
        for v in V.basis:
            generated|={tuple((np.array(w)+v)%2) for w in list(generated)}
        assert generated==exact and int(G.order())*len(exact)==order
        assert info['all_saved_relator_words_independently_replayed']
        records.append({'group':kind,'exhaustive_order':order,'quotient_order':int(G.order()),
            'kernel_dimension':len(V.basis),'all_actual_kernel_elements_compared':len(exact),
            'extra_lifts':len(extra),'complete_lifted_Schreier_matches_exhaustive':True,
            'normal_closure_additions':info['normal_closure_additions'],
            'Schreier_relation_count':info['Schreier_relation_count']})
        print(log.getvalue(),end='')
    out={'records':records,'seconds':round(time.time()-start,3)}
    here.joinpath('de_lifted_schreier_control.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
    print('PASS: exhaustive kernels equal the complete lifted presentation kernels.')

if __name__=='__main__':main()
