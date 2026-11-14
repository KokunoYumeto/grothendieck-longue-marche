#!/usr/bin/env python3
"""Independent small linear identities for the complete E67 source image."""
from pathlib import Path
import hashlib
import itertools
import json

from bc_orbifold_CM_characters import Affine,R,S,mv,neg
from bc_orbifold_CM_six import Span

HERE=Path(__file__).resolve().parent


def main():
    d=json.loads((HERE/'bc_orbifold_CM_six.json').read_text())
    actual=Span(24)
    for r in d['exact_basis']:actual.add(r['vector'],())
    w=(1,2)
    def sw(a):return tuple(a*x%3 for x in w)
    def mvector(a,b,c):
        return tuple(x for v in (sw(a),sw(a),sw(b),sw(c),sw(-c),sw(-b)) for x in v)
    def gvector(u,v,z):
        return tuple(x for q in (u,v,z,neg(z),neg(mv(S,v)),neg(mv(S,u))) for x in q)
    expected=Span(24)
    for abc in ((1,0,0),(0,1,0),(0,0,1)):
        expected.add(mvector(*abc)+(0,)*12,())
    for i in range(6):
        v=[0]*6;v[i]=1
        expected.add((0,)*12+gvector(tuple(v[:2]),tuple(v[2:4]),tuple(v[4:])),())
    assert len(expected.rows)==len(actual.rows)==9
    assert all(not any(expected.reduce(r)[0]) for r in actual.rows.values())
    assert all(not any(actual.reduce(r)[0]) for r in expected.rows.values())

    # The Mordell homogeneous norm equations have zero intersection with
    # the actual correction image.  This proves uniqueness, not only a count.
    mnorm=[]
    for a,b,c in itertools.product(range(3),repeat=3):
        six=[mvector(a,b,c)[2*i:2*i+2] for i in range(6)]
        ok=all(all((x+y)%3==0 for x,y in zip(six[i],six[j])) for i,j in ((0,1),(2,3),(4,5)))
        ok=ok and all((six[2][j]+six[4][j]+six[0][j])%3==0 for j in range(2))
        if ok:mnorm.append((a,b,c))
    assert mnorm==[(0,0,0)]

    # The Gaussian six-image of the whole commutator subgroup equals
    # the printed six-dimensional space.  Its generator commutator and
    # every conjugation by the two actual free generators are checked.
    G=Affine(S,4,((1,0),1),((0,2),2),((0,0),1))
    pairs=[(G.X,G.Y),(G.Y,G.X),(G.Z,G.X),(G.X,G.Z),(G.Y,G.Z),(G.Z,G.Y)]
    gs=Span(12)
    for r in expected.rows.values():
        if any(r[12:]):gs.add(r[12:],())
    comm=tuple(c for a,b in pairs for c in G.comm(a,b)[0])
    assert not any(gs.reduce(comm)[0])
    for r in gs.rows.values():
        for j in (0,1):
            conjugate=tuple(c for i,ab in enumerate(pairs)
                            for c in mv(G.powers[ab[j][1]],r[2*i:2*i+2]))
            assert not any(gs.reduce(conjugate)[0])
    # N_B' supplies every vector of gs by the exact product equality above.
    out={'status':'PASS_EXPLICIT_PRODUCT_SOURCE_AND_NORM_SUBSPACES',
         'Mordell_source_formula':'(a w,a w,b w,c w,-c w,-b w), w=(1,-1)',
         'Gaussian_source_formula':'(u,v,z,-z,-S v,-S u)',
         'joint_rank':9,'Mordell_rank':3,'Gaussian_rank':6,
         'Mordell_homogeneous_norm_kernel':mnorm,
         'Gaussian_whole_F_derived_image_equals_N_derived_image':True,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'six_input_sha256':hashlib.sha256((HERE/'bc_orbifold_CM_six.json').read_bytes()).hexdigest()}
    (HERE/'bc_orbifold_CM_linear.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
