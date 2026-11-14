#!/usr/bin/env python3
"""Complete literal GL_2(F_3) group/automorphism/epikernel certificate.

This first GL23 batch preserves the frozen SL23 files.  Every automorphism
is obtained by testing all generating-pair images against every edge of a
fixed Cayley graph.  No identification with an abstract double cover is
used.  The determinant, SL2 inclusion/restriction and projective-line action
are actual tables, not character or isomorphism-type substitutions.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
import time
import numpy as np

HERE = Path(__file__).resolve().parent


class MatrixGL23:
    def __init__(self):
        self.elements = [a for a in product(range(3), repeat=4)
                         if (a[0]*a[3]-a[1]*a[2]) % 3]
        self.index = {a:i for i,a in enumerate(self.elements)}
        def mm(a,b):
            return tuple(x % 3 for x in
                         (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                          a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))
        def mi(a):
            d = pow((a[0]*a[3]-a[1]*a[2]) % 3,-1,3)
            return tuple(d*x % 3 for x in (a[3],-a[1],-a[2],a[0]))
        self.uid = self.index[(1,0,0,1)]
        self.size = len(self.elements)
        self.mul = np.array([[self.index[mm(a,b)] for b in self.elements]
                             for a in self.elements], dtype=np.int64)
        self.inv = np.array([self.index[mi(a)] for a in self.elements],dtype=np.int64)
        self.det = np.array([0 if (a[0]*a[3]-a[1]*a[2]) % 3 == 1 else 1
                             for a in self.elements], dtype=np.int64)
        assert self.size == 48
        assert np.array_equal(self.det[self.mul],
                              (self.det[:,None]+self.det[None,:]) % 2)
        assert all(np.array_equal(self.mul[self.mul[a],b],
                                  self.mul[a,self.mul[:,b]])
                   for a in range(48) for b in range(48))
        self.generating_pairs = [(g,h) for g in range(48) for h in range(48)
                                 if len(self.subgroup((g,h))) == 48]
        base = self.generating_pairs[0]
        self.tree_parent = np.full((48,2),-1,dtype=np.int64)
        order = [self.uid]
        for z in order:
            for j,g in enumerate(base):
                w = int(self.mul[z,g])
                if w != self.uid and self.tree_parent[w,0] == -1:
                    self.tree_parent[w] = [z,j]
                    order.append(w)
        assert len(order)==48
        automorphisms = []
        for pair in self.generating_pairs:
            image = np.full(48,-1,dtype=np.int64)
            image[self.uid] = self.uid
            for v in order[1:]:
                z,j = self.tree_parent[v]
                image[v] = self.mul[image[z],pair[j]]
            if all(np.array_equal(image[self.mul[:,g]],
                                  self.mul[image,image[g]]) for g in base):
                assert len(set(image)) == 48
                automorphisms.append(tuple(map(int,image)))
        self.auto = np.array(sorted(automorphisms),dtype=np.int64)
        ad = {tuple(a):i for i,a in enumerate(self.auto)}
        self.autone = ad[tuple(range(48))]
        self.am = np.array([[ad[tuple(a[b])] for b in self.auto]
                           for a in self.auto],dtype=np.int64)
        self.ai = np.array([ad[tuple(np.argsort(a))] for a in self.auto],dtype=np.int64)
        for a in self.auto:
            assert np.array_equal(a[self.mul],self.mul[a[:,None],a[None,:]])
            assert np.array_equal(self.det[a],self.det)
        self.kernel_representatives = []
        self.coordinate = {}
        for pair in self.generating_pairs:
            if pair in self.coordinate:
                continue
            j = len(self.kernel_representatives)
            self.kernel_representatives.append(pair)
            for a,mp in enumerate(self.auto):
                key = tuple(map(int,mp[list(pair)]))
                assert key not in self.coordinate
                self.coordinate[key] = (j,a)
        assert len(self.coordinate) == len(self.generating_pairs)
        self.tree_order = np.array(order,dtype=np.int64)
        self.tree_base_pair = base

    def subgroup(self, generators):
        seen = {self.uid}; order = [self.uid]
        for z in order:
            for g in generators:
                w = int(self.mul[z,g])
                if w not in seen:
                    seen.add(w);order.append(w)
        return order

    def comm(self,g,h):
        return int(self.mul[self.mul[self.mul[g,h],self.inv[g]],self.inv[h]])

    def element_order(self,g):
        x = self.uid
        for n in range(1,49):
            x = int(self.mul[x,g])
            if x == self.uid:return n
        raise AssertionError('Lagrange bound failed')


def main():
    started=time.time(); G=MatrixGL23()
    sl=np.flatnonzero(G.det==0)
    sl_index={int(g):j for j,g in enumerate(sl)}
    derived=G.subgroup(sorted({G.comm(g,h) for g in range(48) for h in range(48)}))
    assert set(derived)==set(map(int,sl))
    old=np.load(HERE/'a_cm_sl23_model.npz')
    assert np.array_equal(np.array(G.elements)[sl],old['SL2_elements'])
    assert np.array_equal(np.array([[sl_index[int(G.mul[g,h])] for h in sl]
                                    for g in sl]),old['SL2_multiplication'])
    sl_aut_index={tuple(a):i for i,a in enumerate(old['Aut_maps'])}
    restriction=np.array([sl_aut_index[tuple(sl_index[int(a[g])] for g in sl)]
                          for a in G.auto],dtype=np.int64)
    assert np.array_equal(restriction[G.am],
                          old['Aut_multiplication'][restriction[:,None],restriction[None,:]])
    inner=np.array([[G.mul[G.mul[g,h],G.inv[g]] for h in range(48)]
                    for g in range(48)])
    inner_set=set(map(tuple,inner))
    center=[g for g in range(48) if all(G.mul[g,h]==G.mul[h,g] for h in range(48))]
    twist=np.array([G.index[tuple(((-1 if G.det[g] else 1)*x)%3
                                  for x in a)] for g,a in enumerate(G.elements)])
    ad={tuple(a):i for i,a in enumerate(G.auto)}
    assert tuple(twist) in ad
    assert set(map(tuple,G.auto))==inner_set | {tuple(twist[a]) for a in inner}
    # Projective action: normalize the first nonzero coordinate to one.
    lines=[(1,0),(1,1),(1,2),(0,1)]
    def line(v):
        k=v[0] or v[1];return tuple(x*pow(k,-1,3)%3 for x in v)
    projective=np.array([[lines.index(line(((a[0]*v[0]+a[1]*v[1])%3,
                                            (a[2]*v[0]+a[3]*v[1])%3)))
                           for v in lines] for a in G.elements])
    for g in range(48):
        for h in range(48):
            assert np.array_equal(projective[G.mul[g,h]],projective[g][projective[h]])
    assert [g for g in range(48) if np.array_equal(projective[g],np.arange(4))]==center
    assert len(set(map(tuple,projective)))==24
    pair_profiles=Counter(tuple(map(int,G.det[list(p)])) for p in G.generating_pairs)
    orbit_profiles=Counter(tuple(map(int,G.det[list(p)])) for p in G.kernel_representatives)
    sl_aut_one=next(i for i,a in enumerate(old['Aut_maps'])
                    if np.array_equal(a,np.arange(24)))
    out={'status':'PASS_COMPLETE_LITERAL_GL2_F3_GROUP',
         'matrix_group_order':48,'derived_order':len(derived),
         'derived_equals_literal_SL2_F3':True,
         'center_matrices':[G.elements[g] for g in center],
         'element_order_distribution':dict(sorted(Counter(G.element_order(g) for g in range(48)).items())),
         'ordered_generating_pairs':len(G.generating_pairs),
         'complete_automorphism_count':len(G.auto),
         'inner_automorphism_count':len(inner_set),
         'all_automorphisms_are_inner_or_determinant_twist_inner':True,
         'determinant_twist_automorphism_index':ad[tuple(twist)],
         'SL2_restriction_image_size':len(set(restriction)),
         'SL2_restriction_kernel_size':int(np.count_nonzero(restriction==sl_aut_one)),
         'projective_line_image_order':len(set(map(tuple,projective))),
         'projective_line_kernel_is_actual_scalar_center':True,
         'exact_epimorphism_kernel_count':len(G.kernel_representatives),
         'kernel_representatives':G.kernel_representatives,
         'generating_pair_determinant_profiles':{str(k):v for k,v in sorted(pair_profiles.items())},
         'epikernel_determinant_profiles':{str(k):v for k,v in sorted(orbit_profiles.items())},
         'Cayley_base_generating_pair':G.tree_base_pair,
         'complete_Cayley_edge_maps_tested':len(G.generating_pairs),
         'no_abstract_double_cover_identification_used':True,
         'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'a_cm_gl23_group.npz',GL2_elements=np.array(G.elements),
        GL2_multiplication=G.mul,GL2_inverse=G.inv,GL2_one=np.array(G.uid),
        determinant=G.det,SL2_inclusion=sl,Aut_maps=G.auto,Aut_multiplication=G.am,
        Aut_inverse=G.ai,Aut_one=np.array(G.autone),SL2_Aut_restriction=restriction,
        projective_line_action=projective,generating_pairs=np.array(G.generating_pairs),
        kernel_representatives=np.array(G.kernel_representatives),
        Cayley_tree_parent=G.tree_parent,Cayley_tree_order=G.tree_order)
    (HERE/'a_cm_gl23_group.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
