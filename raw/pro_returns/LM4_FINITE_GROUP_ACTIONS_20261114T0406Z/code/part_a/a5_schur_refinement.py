#!/usr/bin/env python3
"""The characteristic SL(2,5) refinement of the universal A5 quotient.

Checks the normalized order-two and both GT_0 cycle equations exactly.
No surviving finite automorphism is asserted to lift to the full group.
"""
from itertools import product
from collections import Counter, deque
from pathlib import Path
import json
import a5_involution_quotient as a

MOD = 5
I = (1, 0, 0, 1)
NEG = (4, 0, 0, 4)


def mul(x, y):
    aa, b, c, d = x
    e, f, g, h = y
    return ((aa*e+b*g)%5, (aa*f+b*h)%5,
            (c*e+d*g)%5, (c*f+d*h)%5)


def det(x):
    return (x[0]*x[3]-x[1]*x[2])%5


def inv(x):
    z = pow(det(x), -1, 5)
    return tuple(z*v%5 for v in (x[3],-x[1],-x[2],x[0]))


def neg(x):
    return tuple(-v%5 for v in x)


def project(x):
    return min(x, neg(x))


def glproject(x):
    c = next(v for v in x if v)
    ci = pow(c, -1, 5)
    return tuple(ci*v%5 for v in x)


def conjugate(g, x):
    return mul(mul(g, x), inv(g))


SL = [m for m in product(range(5), repeat=4) if det(m)==1]
PSL = sorted({project(m) for m in SL})
PGL = sorted({glproject(m) for m in product(range(5), repeat=4) if det(m)})
assert len(SL)==120 and len(PSL)==60 and len(PGL)==120
PI = project(I)


def pmul(x, y):
    return project(mul(x, y))


def porder(x):
    z=PI
    for n in range(1,61):
        z=pmul(z,x)
        if z==PI:
            return n
    raise AssertionError


def aisomorphism():
    """Explicit A5 -> PSL(2,5), verified against all multiplication pairs."""
    aa = next(x for x in range(60) if a.order(x)==2)
    bb = next(y for y in range(60)
              if a.order(y)==3 and a.order(a.MUL[aa][y])==5)
    xx = next(x for x in PSL if porder(x)==2)
    yy = next(y for y in PSL if porder(y)==3 and porder(pmul(xx,y))==5)
    mapping={a.ID:PI}
    queue=[a.ID]
    for z in queue:
        for ag,pg in ((aa,xx),(bb,yy)):
            az=a.MUL[z][ag]
            pz=pmul(mapping[z],pg)
            if az in mapping:
                assert mapping[az]==pz
            else:
                mapping[az]=pz
                queue.append(az)
    assert len(mapping)==60 and len(set(mapping.values()))==60
    assert all(mapping[a.MUL[x][y]]==pmul(mapping[x],mapping[y])
               for x in range(60) for y in range(60))
    glconj={}
    for gi,con in enumerate(a.CONJ):
        gs=[g for g in PGL if project(conjugate(g,xx))==mapping[con[aa]]
            and project(conjugate(g,yy))==mapping[con[bb]]]
        assert len(gs)==1
        g=gs[0]
        assert all(project(conjugate(g,mapping[x]))==mapping[con[x]]
                   for x in range(60))
        glconj[gi]=g
    return mapping,glconj


def main():
    pmap, glconj = aisomorphism()
    # Verify perfection and every lift of the nineteen generating pairs.
    commutators={mul(mul(mul(x,y),inv(x)),inv(y)) for x in SL for y in SL}
    derived={I}; queue=[I]
    for x in queue:
        for y in commutators:
            z=mul(x,y)
            if z not in derived:
                derived.add(z);queue.append(z)
    assert len(derived)==120
    reps,lookup=[],{}
    for x in range(60):
        for y in range(60):
            if (x,y) in lookup or a.generated(x,y)!=60:
                continue
            i=len(reps)
            reps.append((x,y))
            for gi,co in enumerate(a.CONJ):
                lookup[co[x],co[y]]=(i,gi)
    assert len(reps)==19 and len(lookup)==2280
    X=[pmap[x] for x,y in reps]
    Y=[pmap[y] for x,y in reps]
    Z=[inv(mul(x,y)) for x,y in zip(X,Y)]
    checked_pair_lifts=0
    for x,y in zip(X,Y):
        for sx,sy in product((0,1),repeat=2):
            xx=neg(x) if sx else x
            yy=neg(y) if sy else y
            generated={I}; queue=[I]
            for z in queue:
                for w in (xx,yy):
                    zw=mul(z,w)
                    if zw not in generated:
                        generated.add(zw);queue.append(zw)
            assert len(generated)==120
            checked_pair_lifts+=1
    theta=[lookup[y,x] for x,y in reps]
    omega=[lookup[y,a.INV[a.MUL[x][y]]] for x,y in reps]
    delta=[lookup[a.INV[x],a.INV[y]] for x,y in reps]
    for name,acts,targets in [('theta',theta,(Y,X)),
                             ('omega',omega,(Y,Z)),
                             ('delta',delta,([inv(x) for x in X],[inv(y) for y in Y]))]:
        # The central characters making the named word substitution exact.
        for i,(j,gi) in enumerate(acts):
            for generators,target in zip((X,Y),targets):
                c=mul(target[i],inv(conjugate(glconj[gi],generators[j])))
                assert c in (I,NEG)

    orbits=[]
    used=set()
    for i in range(19):
        if i in used:
            continue
        orb={i}; queue=[i]
        for j in queue:
            for act in (theta,omega):
                k=act[j][0]
                if k not in orb:
                    orb.add(k);queue.append(k)
        used.update(orb)
        orbits.append(sorted(orb))

    def act(values,acts,i):
        j,gi=acts[i]
        return conjugate(glconj[gi],values[j])

    rows=[]
    for orb in orbits:
        allowed={i:[t for t in range(60) if a.MUL[t][t]==a.ID
                    and a.MUL[a.MUL[t][reps[i][0]]][a.INV[t]]==a.INV[reps[i][0]]]
                 for i in orb}
        total=triangle=liftable=triangle_liftable=0
        lifted_pairs=triangle_lifted_pairs=0
        histogram=Counter()
        component_examples=[]
        for choices in product(*(allowed[i] for i in orb)):
            ts=dict(zip(orb,choices))
            # Exact base second symmetry; all base equations checked in D38.
            if any(a.CONJ[omega[i][1]][ts[omega[i][0]]] !=
                   a.MUL[a.INV[reps[i][1]]][a.CONJ[theta[i][1]][ts[theta[i][0]]]]
                   for i in orb):
                continue
            total+=1
            istriangle=all(ts[i] not in (a.ID,reps[i][0]) for i in orb)
            triangle+=istriangle
            tt={i:pmap[ts[i]] for i in orb}
            f0={i:mul(act(tt,theta,i),inv(tt[i])) for i in orb}
            good=0
            for signs in product((0,1),repeat=len(orb)):
                ff={i:(neg(f0[i]) if signs[j] else f0[i]) for j,i in enumerate(orb)}
                # First symmetry and actual order-two norm on the derived factors.
                if any(mul(act(ff,theta,i),ff[i]) != I or
                       mul(ff[i],conjugate(tt[i],ff[i])) != I for i in orb):
                    continue
                of={i:act(ff,omega,i) for i in orb}
                oof={i:act(of,omega,i) for i in orb}
                if any(mul(mul(mul(mul(mul(oof[i],inv(Z[i])),of[i]),
                                       inv(Y[i])),ff[i]),inv(X[i])) != I for i in orb):
                    continue
                # Construct the actual order-two automorphism on SL^orb x C2^2.
                # Its perfect-factor restriction is Inn(tt), with two named
                # central characters correcting the images of the free generators.
                for i in orb:
                    cx=mul(inv(X[i]),inv(conjugate(tt[i],X[i])))
                    target_y=mul(mul(inv(ff[i]),inv(Y[i])),ff[i])
                    cy=mul(target_y,inv(conjugate(tt[i],Y[i])))
                    assert cx in (I,NEG) and cy in (I,NEG)
                    assert mul(tt[i],tt[i]) in (I,NEG)
                    assert mul(cx,cx)==I and mul(cy,cy)==I
                    assert mul(conjugate(tt[i],X[i]),cx)==inv(X[i])
                    assert mul(conjugate(tt[i],Y[i]),cy)==target_y
                good+=1
            histogram[good]+=1
            lifted_pairs+=good
            if good:
                liftable+=1
                triangle_liftable+=istriangle
                triangle_lifted_pairs+=istriangle*good
            if len(component_examples)<2:
                component_examples.append({'t':{str(i):a.cycles(a.A5[ts[i]]) for i in orb},
                                           'triangle':istriangle,'central_f_lifts':good})
        rows.append({'orbit':orb,'base_tuples':total,'triangle_base_tuples':triangle,
                     'liftable_base_tuples':liftable,'liftable_triangle_tuples':triangle_liftable,
                     'lifted_pairs':lifted_pairs,'lifted_triangle_pairs':triangle_lifted_pairs,
                     'central_lift_histogram':dict(sorted(histogram.items())),
                     'examples':component_examples})
    from math import prod
    ans={'finite_quotient':'SL(2,F5)^19 x (C2)^2',
         'SL2_order':120,'A5_order':60,'PGL2_order':120,
         'SL2_derived_order':len(derived),
         'A5_generating_pairs':len(lookup),'SL2_generating_pairs':4*len(lookup),
         'SL2_epimorphism_kernels':4*len(reps),
         'generating_pair_lifts_directly_checked':checked_pair_lifts,
         'orbits':rows,
         'counts':{k:prod(row[k] for row in rows) for k in
                   ('base_tuples','triangle_base_tuples','liftable_base_tuples',
                    'liftable_triangle_tuples','lifted_pairs','lifted_triangle_pairs')},
         'scope':'Exact finite normalized automorphism and cycle/norm equations. No full lift asserted.'}
    target=Path(__file__).with_name('a5_schur_refinement_output.json')
    target.write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps(ans,indent=2))


if __name__=='__main__':
    main()
