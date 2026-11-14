#!/usr/bin/env python3
"""Exact exponent-three Heisenberg quotient of the Gaussian triangle.

New research after E67.  This constructs actual finite group maps and
exhausts their framed peripheral automorphisms.  It does not assert
that an individual target lifts to a full profinite GT element.
"""
from pathlib import Path
from collections import deque
import hashlib
import itertools
import json

from bc_orbifold_CM_characters import S,Affine,mv,add,neg,centralizer,det

HERE=Path(__file__).resolve().parent


def wedge(v,w):return (v[0]*w[1]-v[1]*w[0])%3


class Gaussian:
    def __init__(self):
        self.old=Affine(S,4,((1,0),1),((0,2),2),((0,0),1))
        self.powers=self.old.powers
        self.one=(0,0,0,0)
        self.X=(1,0,0,1);self.Y=(0,2,0,2);self.Z=(0,0,0,1)
        self.C=(0,0,1,0)
        self.all=tuple(itertools.product(range(3),range(3),range(3),range(4)))
        self.H=tuple(g for g in self.all if g[3]==0)

    def mul(self,a,b):
        av=a[:2];bv=mv(self.powers[a[3]],b[:2])
        v=add(av,bv)
        return v+( (a[2]+b[2]+2*wedge(av,bv))%3,(a[3]+b[3])%4)

    def inv(self,a):
        return neg(mv(self.powers[-a[3]%4],a[:2]))+(-a[2]%3,-a[3]%4)

    def power(self,a,n):
        if n<0:a,n=self.inv(a),-n
        v=self.one
        while n:
            if n&1:v=self.mul(v,a)
            a=self.mul(a,a);n//=2
        return v

    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))
    def comm(self,a,b):return self.mul(self.conj(a,b),self.inv(b))
    def projected(self,a):return (a[:2],a[3])

    def word(self,w,X=None,Y=None):
        X=self.X if X is None else X;Y=self.Y if Y is None else Y
        letters={1:X,2:Y,-1:self.inv(X),-2:self.inv(Y)};v=self.one
        for a in w:v=self.mul(v,letters[a])
        return v

    def check_map(self,xi,yi):
        mapping={self.one:self.one};todo=deque([self.one])
        for g in todo:
            pass
        todo=deque([self.one])
        while todo:
            a=todo.popleft()
            for x,y in ((self.X,xi),(self.Y,yi)):
                b=self.mul(a,x);z=self.mul(mapping[a],y)
                if b in mapping:
                    if mapping[b]!=z:return None
                else:mapping[b]=z;todo.append(b)
        assert len(mapping)==108
        return mapping if len(set(mapping.values()))==108 else None


def main():
    G=Gaussian()
    assert G.mul(G.mul(G.X,G.Y),G.Z)==G.one
    assert G.power(G.Y,2)==G.power(G.Z,4)==G.one
    assert G.power(G.X,4)==G.inv(G.C)
    k1=G.mul(G.power(G.X,2),G.Y);k2=G.mul(G.power(G.Z,2),G.Y)
    assert k1==(1,0,0,0) and k2==(0,1,0,0)
    assert G.comm(k1,k2)==G.C
    for a in G.all:
        assert G.mul(a,G.inv(a))==G.mul(G.inv(a),a)==G.one
        if a[3]%2==0:assert G.power(a,6)==G.one
        for b in G.all:
            assert G.projected(G.mul(a,b))==G.old.mul(G.projected(a),G.projected(b))
    # Associativity is checked on every triple, independently of the
    # bilinear-cocycle construction of the law.
    table=[[G.all.index(G.mul(a,b)) for b in G.all] for a in G.all]
    for a in range(108):
        for b in range(108):
            for c in range(108):assert table[table[a][b]][c]==table[a][table[b][c]]

    records=[];automorphisms={}
    for hy in G.H:
        yi=G.conj(hy,G.Y)
        for hz in G.H:
            zi=G.conj(hz,G.Z)
            if G.mul(G.mul(G.X,yi),zi)!=G.one:continue
            autom=G.check_map(G.X,yi)
            if autom is None or autom[G.Z]!=zi:continue
            B=tuple(zip(autom[k1][:2],autom[k2][:2]))
            assert B in centralizer(S) and det(B)==1 and autom[G.C]==G.C
            six=(G.inv(hy),hy,hz,G.inv(hz),G.mul(G.inv(hz),hy),G.mul(G.inv(hy),hz))
            assert all(G.mul(six[i],six[j])==G.one for i,j in ((0,1),(2,3),(4,5)))
            assert G.mul(G.mul(six[2],six[4]),six[0])==G.one
            p=tuple(G.all.index(autom[g]) for g in G.all)
            automorphisms[p]=B
            records.append({'B':B,'y_frame':hy,'z_frame':hz,
                            'six_absolute_values':six,'automorphism_permutation':p})
    assert len(automorphisms)==4
    assert len(records)==36
    assert all(sum(r['B']==B for r in records)==9 for B in centralizer(S))
    # These four actual actions are the inner automorphisms by powers
    # of x.  Their deck-zero frames were separately retained above.
    for j in range(4):
        p=tuple(G.all.index(G.conj(G.power(G.X,j),g)) for g in G.all)
        assert p in automorphisms
    out={'status':'PASS_EXACT_GAUSSIAN_HEISENBERG_QUOTIENT_AND_FRAMED_ACTIONS',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'order':108,'normal_Heisenberg_order':27,'field':3,'BCH_half':2,
         'coordinate_order':['v1','v2','central','deck_mod4'],
         'literal_generators':{'x':G.X,'y':G.Y,'z':G.Z,'k1':k1,'k2':k2,'commutator':G.C},
         'primitive_cusp_identity':'x^4=[k1,k2]^-1',
         'all_associativity_triples':108**3,
         'deck_even_subgroup_exponent_divides_six':True,
         'four_actual_actions_are_inner_x_powers':True,
         'finite_framed_targets':len(records),'actual_automorphisms':len(automorphisms),
         'records':records,
         'scope':'Exact finite triangle quotient and exhaustive deck-zero frames. '
                 'No old-source correction fibre or full-GT realization is asserted yet.'}
    (HERE/'bc_gaussian_heisenberg_model.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','order','normal_Heisenberg_order',
                     'all_associativity_triples','finite_framed_targets','actual_automorphisms']},indent=2))


if __name__=='__main__':main()
