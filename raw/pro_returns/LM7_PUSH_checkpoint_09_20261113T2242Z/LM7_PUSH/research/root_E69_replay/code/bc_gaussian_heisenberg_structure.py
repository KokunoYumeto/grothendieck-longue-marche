#!/usr/bin/env python3
"""Exact graph, abelianization and framed fibres of the E69 source image."""
from pathlib import Path
import hashlib
import itertools
import json
import numpy as np

from bc_orbifold_CM_characters import Affine,R,S,mv
from bc_gaussian_heisenberg_model import Gaussian
from bc_gaussian_heisenberg_source import bracket
from bc_orbifold_CM_six import Span

HERE=Path(__file__).resolve().parent


class Evaluations:
    def __init__(self):
        self.M=Affine(R,6,((0,0),1),((1,0),3),((1,0),2))
        self.G=Gaussian()
        pairs=lambda T:[(T.X,T.Y),(T.Y,T.X),(T.Z,T.X),
                        (T.X,T.Z),(T.Y,T.Z),(T.Z,T.Y)]
        self.maps=[(T,a,b) for T in (self.M,self.G) for a,b in pairs(T)]
        self.one=tuple(T.one for T,a,b in self.maps)

    def word(self,w):return tuple(T.word(w,a,b) for T,a,b in self.maps)
    def mul(self,a,b):return tuple(T.mul(x,y) for (T,_,_),x,y in zip(self.maps,a,b))
    def inv(self,a):return tuple(T.inv(x) for (T,_,_),x in zip(self.maps,a))
    def comm(self,a,b):return self.mul(self.mul(self.mul(a,b),self.inv(a)),self.inv(b))
    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))
    def vector(self,a):
        assert all(g[1]==0 for g in a[:6]) and all(g[3]==0 for g in a[6:])
        return tuple(c for v,e in a[:6] for c in v)+tuple(c for g in a[6:] for c in g[:3])
    def element(self,v):
        return tuple((tuple(v[2*i:2*i+2]),0) for i in range(6))+tuple(
            tuple(v[12+3*i:15+3*i])+(0,) for i in range(6))


def A(g):
    a,b,c,e=g;assert e==0
    return (-a%3,-b%3,(c+a+b)%3,0)


def B(g):
    a,b,c,e=g;assert e==0
    u,v=mv(S,(a,b))
    return (-u%3,-v%3,(c+a+b)%3,0)


def gaussian_graph(u,v,t):return (u,v,t,A(t),B(v),B(u))


def mordell_graph(a,b,c):
    return tuple((k%3,-k%3) for k in (a,a,b,c,-c,-b))


def graph_vector(a,b,c,u,v,t):
    return tuple(x for pair in mordell_graph(a,b,c) for x in pair)+tuple(
        x for g in gaussian_graph(u,v,t) for x in g[:3])


def main():
    E=Evaluations();G=E.G
    for f in (A,B):
        assert len({f(g) for g in G.H})==27
        for g in G.H:
            for h in G.H:assert f(G.mul(g,h))==G.mul(f(g),f(h))
    saved=json.loads((HERE/'bc_gaussian_heisenberg_source.json').read_text())
    basis=[r['vector'] for r in saved['exact_basis']]
    source=Span(30)
    for r in basis:source.add(r,())
    graph=Span(30);graphbasis=[]
    for i in range(12):
        coords=[0]*12;coords[i]=1
        a,b,c=coords[:3];u=tuple(coords[3:6])+(0,)
        v=tuple(coords[6:9])+(0,);t=tuple(coords[9:12])+(0,)
        row=graph_vector(a,b,c,u,v,t);graphbasis.append(row);graph.add(row,())
    assert len(source.rows)==len(graph.rows)==12
    assert all(not any(source.reduce(r)[0]) for r in graphbasis)
    assert all(not any(graph.reduce(r)[0]) for r in basis)
    derived=Span(30)
    for a in graphbasis:
        for b in graphbasis:derived.add(bracket(a,b),())
    assert len(derived.rows)==3
    projection=list(range(12))+[12+3*i+j for i in range(6) for j in range(2)]
    assert all(not any(r[j] for j in projection) for r in derived.rows.values())
    assert saved['old_E67_projection_rank']==9

    targets=json.loads((HERE/'bc_gaussian_heisenberg_model.json').read_text())['records']
    allowed=[]
    for i,row in enumerate(targets):
        six=tuple(tuple(g) for g in row['six_absolute_values'])
        in_graph=six==gaussian_graph(*six[:3])
        hy,hz=row['y_frame'],row['z_frame']
        explicit=(hz[2]-hz[0]-hz[1])%3==0
        assert in_graph==explicit
        if in_graph:allowed.append(i)
    assert len(allowed)==12
    for row in saved['records']:
        assert [v['Gaussian_framed_target_index'] for v in row['allowed']]==allowed

    # The original source F' also has precisely the same Gaussian image:
    # one commutator and conjugation by both actual free generators suffice.
    Fspan=Span(18)
    fg=[E.word([1]),E.word([2])]
    first=E.vector(E.comm(*fg))[12:];Fspan.add(first,())
    changed=True
    while changed:
        changed=False
        for row in list(Fspan.rows.values()):
            element=E.element([0]*12+list(row))
            for g in fg:
                if Fspan.add(E.vector(E.conj(g,element))[12:],()):changed=True
            for other in list(Fspan.rows.values()):
                if Fspan.add(bracket([0]*12+list(row),[0]*12+list(other))[12:],()):changed=True
    assert len(Fspan.rows)==9
    Gspan=Span(18)
    for r in graphbasis:Gspan.add(r[12:],())
    assert all(not any(Fspan.reduce(r)[0]) for r in Gspan.rows.values())
    assert all(not any(Gspan.reduce(r)[0]) for r in Fspan.rows.values())

    out={'status':'PASS_EXACT_GAUSSIAN_GRAPH_ABELIANIZATION_AND_FRAMED_FIBRES',
         'actual_source_image':'C3^3 times Heisenberg(3)^3',
         'complete_source_dimension':12,'Gaussian_dimension':9,'Mordell_dimension':3,
         'derived_dimension':3,'actual_abelianization_is_E67_projection':True,
         'A':'(a,b,c) -> (-a,-b,c+a+b)',
         'B':'(a,b,c) -> (-b,a,c+a+b)',
         'six_graph':'(u,v,t,A(t),B(v),B(u))',
         'exact_graph_basis':graphbasis,
         'exact_derived_basis':[derived.rows[p] for p in sorted(derived.rows)],
         'Gaussian_F_derived_image_equals_N_derived_image':True,
         'allowed_framed_target_indices':allowed,
         'exact_frame_equation':'hz.central = hz.v1 + hz.v2; hy.central arbitrary',
         'old_Gaussian_actions':4,'central_lifts_per_action':3,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in
             ['bc_gaussian_heisenberg_model.py','bc_gaussian_heisenberg_model.json',
              'bc_gaussian_heisenberg_source.py','bc_gaussian_heisenberg_source.json']}}
    (HERE/'bc_gaussian_heisenberg_structure.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
