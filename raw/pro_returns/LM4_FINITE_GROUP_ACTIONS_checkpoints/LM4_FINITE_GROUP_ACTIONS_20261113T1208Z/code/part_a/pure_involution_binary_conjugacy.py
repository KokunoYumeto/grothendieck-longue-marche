#!/usr/bin/env python3
"""Conjugator equations in the characteristic SL(2,5) refinement.

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

    units=[m for m in range(60) if __import__('math').gcd(m,60)==1]
    unit_full=(1<<len(units))-1
    classid={}
    for v in SL:
        if v not in classid:
            cc={conjugate(g,v) for g in SL}
            label=min(cc)
            for w in cc:
                classid[w]=label
    reverse_pmap={v:k for k,v in pmap.items()}
    def spower(v,n):
        z=I
        for _ in range(n%60):
            z=mul(z,v)
        return z
    conjugator_cache={}
    def conjugator_mask(i,t,f):
        key=(i,t,f)
        if key in conjugator_cache:
            return conjugator_cache[key]
        # This is the exact first D35 equation in the specified refinement.
        hs=[h for h in SL if mul(mul(inv(h),conjugate(t,h)),inv(f))==I]
        assert len(hs)==4
        mask=0
        automask=0
        for bit,mu in enumerate(units):
            xp,yp,wp=spower(X[i],mu),spower(Y[i],mu),spower(mul(X[i],Y[i]),mu)
            for h in hs:
                newy=conjugate(h,yp)
                if classid[mul(xp,newy)]==classid[wp]:
                    mask|=1<<bit
                    # Verify that the candidate substitution also descends to
                    # an actual automorphism of the characteristic quotient.
                    pp=(reverse_pmap[project(xp)],reverse_pmap[project(newy)])
                    if pp in lookup and lookup[pp][0]==i:
                        automask|=1<<bit
        conjugator_cache[key]=(mask,automask)
        return mask,automask
    def joint_first_symmetry(orb,tt,ff,mu=None):
        sets={i:[] for i in orb}
        for i in orb:
            for h in SL:
                if mul(mul(inv(h),conjugate(tt[i],h)),inv(ff[i]))!=I:
                    continue
                if mu is not None:
                    xp,yp,wp=spower(X[i],mu),spower(Y[i],mu),spower(mul(X[i],Y[i]),mu)
                    newy=conjugate(h,yp)
                    pp=(reverse_pmap[project(xp)],reverse_pmap[project(newy)])
                    if classid[mul(xp,newy)]!=classid[wp] or pp not in lookup or lookup[pp][0]!=i:
                        continue
                sets[i].append(h)
        seen=set()
        for i in orb:
            if i in seen:
                continue
            j,gi=theta[i]
            g=glconj[gi]
            if i==j:
                if not any(mul(h,conjugate(g,h))==I for h in sets[i]):
                    return False
            else:
                if not any(conjugate(inv(g),inv(h)) in sets[j] for h in sets[i]):
                    return False
            seen.update((i,j))
        return True
    gtunits=[mu for mu in range(120) if __import__('math').gcd(mu,120)==1]
    gtfull=(1<<len(gtunits))-1
    def second_symmetry_mask(orb,tt,ff,automask):
        if not automask:
            return 0
        hs={i:[h for h in SL if mul(mul(inv(h),conjugate(tt[i],h)),inv(ff[i]))==I]
            for i in orb}
        blockchoices=[]
        seen=set()
        for i in orb:
            if i in seen:
                continue
            j,gi=theta[i]
            g=glconj[gi]
            choices=[]
            for h in hs[i]:
                hj=conjugate(inv(g),inv(h))
                if i==j:
                    if hj==h:
                        choices.append({i:h})
                elif hj in hs[j]:
                    choices.append({i:h,j:hj})
            assert choices
            blockchoices.append(choices)
            seen.update((i,j))
        answer=0
        for bit,mu in enumerate(gtunits):
            mu60=mu%60
            if not automask>>units.index(mu60)&1:
                continue
            m=(mu-1)//2
            for choices in product(*blockchoices):
                hh={}
                for choice in choices:
                    hh.update(choice)
                pure=True
                for i in orb:
                    xp,yp,wp=spower(X[i],mu),spower(Y[i],mu),spower(mul(X[i],Y[i]),mu)
                    newy=conjugate(hh[i],yp)
                    pp=(reverse_pmap[project(xp)],reverse_pmap[project(newy)])
                    if classid[mul(xp,newy)]!=classid[wp] or pp not in lookup or lookup[pp][0]!=i:
                        pure=False;break
                if not pure:
                    continue
                kk={i:inv(hh[i]) for i in orb}
                ok={i:act(kk,omega,i) for i in orb}
                ook={i:act(ok,omega,i) for i in orb}
                if all(mul(mul(mul(mul(mul(ook[i],spower(Z[i],m)),ok[i]),
                                       spower(Y[i],m)),kk[i]),spower(X[i],m))==I for i in orb):
                    answer|=1<<bit
                    break
        return answer
    rows=[]
    for orb in orbits:
        allowed={i:[t for t in range(60) if a.MUL[t][t]==a.ID
                    and a.MUL[a.MUL[t][reps[i][0]]][a.INV[t]]==a.INV[reps[i][0]]]
                 for i in orb}
        total=triangle=liftable=triangle_liftable=0
        lifted_pairs=triangle_lifted_pairs=0
        histogram=Counter()
        masks=Counter()
        automasks=Counter()
        firstsym=Counter()
        firstsymmasks=Counter()
        secondmasks=Counter()
        localbase=Counter()
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
            baseplus=baseminus=baseboth=0
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
                mask=automask=unit_full
                for i in orb:
                    cm,ca=conjugator_mask(i,tt[i],ff[i])
                    mask &= cm
                    automask &= ca
                masks[mask]+=1
                automasks[automask]+=1
                first_ok=joint_first_symmetry(orb,tt,ff)
                firstsym[first_ok]+=1
                fmask=0
                if first_ok:
                    for bit,mu in enumerate(units):
                        if automask>>bit&1 and joint_first_symmetry(orb,tt,ff,mu):
                            fmask|=1<<bit
                firstsymmasks[fmask]+=1
                smask=second_symmetry_mask(orb,tt,ff,automask)
                secondmasks[smask]+=1
                plus=bool(smask>>gtunits.index(1)&1)
                minus=bool(smask>>gtunits.index(7)&1)
                baseplus+=plus
                baseminus+=minus
                baseboth+=plus and minus
            histogram[good]+=1
            if good:
                localbase[baseplus,baseminus,baseboth]+=1
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
                     'D35_conjugator_unit_masks':dict(sorted(masks.items())),
                     'actual_automorphism_unit_masks':dict(sorted(automasks.items())),
                     'first_symmetry_pass_counts':dict(sorted(firstsym.items())),
                     'first_symmetry_conjugator_unit_masks':dict(sorted(firstsymmasks.items())),
                     'second_symmetry_conjugator_unit_masks':dict(sorted(secondmasks.items())),
                     'base_conjugator_coordinate_patterns':[
                         {'plus':v[0],'minus':v[1],'both':v[2],'base_tuples':count}
                         for v,count in sorted(localbase.items())],
                     'examples':component_examples})
    from math import prod
    def combine(field):
        chosenunits=gtunits if field=='second_symmetry_conjugator_unit_masks' else units
        states={(1<<len(chosenunits))-1:1}
        for row in rows:
            new=Counter()
            for old,count in states.items():
                for mask,multiplicity in row[field].items():
                    new[old&mask]+=count*multiplicity
            states=new
        return {str(mask):{'units':[mu for j,mu in enumerate(chosenunits) if mask>>j&1],
                           'coordinate_pairs':count} for mask,count in sorted(states.items())}
    basestates={(1,1,1):1}
    for row in rows:
        nxt=Counter()
        for v,n in basestates.items():
            for local in row['base_conjugator_coordinate_patterns']:
                nxt[v[0]*local['plus'],v[1]*local['minus'],v[2]*local['both']]+=n*local['base_tuples']
        basestates=nxt
    basehist=Counter()
    for (plus,minus,both),n in basestates.items():
        basehist[plus+minus-both]+=n
    assert basehist=={0:2531250,4:2531250}
    ans={'admissible_f_coordinates_per_base_tuple':dict(sorted(basehist.items())),
         'second_symmetry_conjugator_final_masks':combine('second_symmetry_conjugator_unit_masks'),
         'conjugator_units_mod_120':gtunits,
         'first_symmetry_surviving_pairs':prod(row['first_symmetry_pass_counts'].get(True,0) for row in rows),
         'first_symmetry_conjugator_final_masks':combine('first_symmetry_conjugator_unit_masks'),
         'units_mod_60':units,
         'D35_conjugator_final_masks':combine('D35_conjugator_unit_masks'),
         'actual_automorphism_final_masks':combine('actual_automorphism_unit_masks'),
         'finite_quotient':'SL(2,F5)^19 x (C2)^2',
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
    target=Path(__file__).with_name('pure_involution_binary_conjugacy_output.json')
    target.write_text(json.dumps(ans,indent=2)+'\n')
    print(json.dumps(ans,indent=2))


if __name__=='__main__':
    main()
