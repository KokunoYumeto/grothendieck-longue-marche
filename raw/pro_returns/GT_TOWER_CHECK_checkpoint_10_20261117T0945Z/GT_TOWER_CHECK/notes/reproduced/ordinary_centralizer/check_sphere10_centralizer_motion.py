#!/usr/bin/env python3
"""Two literal H-equivariant regular-quartet motion generators.

Six branch-fixed points stay stationary.  The two paths are
 z=2 exp(i theta) and z=5/4+(3/4)exp(i theta), 0<=theta<=pi.
Their four moving points are z,-z,1/z,-1/z.  Every crossing
is certified by exact rational polynomial root intervals.
"""
from itertools import combinations
from pathlib import Path
from math import gcd
import json
import hashlib
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
marking_data=json.loads((HERE/"check_sphere10_geometric_klein.json").read_text())
B=marking_data["marking_braid_word"]
initial_order=marking_data["initial_horizontal_order"]
t=sp.Symbol("t");Q=sp.Rational
E=sp.Matrix([114,-130,27]);F=sp.Matrix([123,90,-86]);P=sp.Matrix([50,75,150])
base=[(0,0,1,0),(1,0,0,0),(1,0,1,0),(-1,0,1,0),(0,1,1,0),(0,-1,1,0)]


def fraction(x):return [int(x.p),int(x.q)]


def integer_polynomial(expr):
    poly=sp.Poly(sp.expand(expr),t,domain=sp.QQ)
    if poly.is_zero:return poly
    denominator=sp.ilcm(*([1]+[c.q for c in poly.all_coeffs()]))
    coefficients=[int(c*denominator) for c in poly.all_coeffs()]
    common=0
    for c in coefficients:common=gcd(common,abs(c))
    return sp.Poly.from_list([c//common for c in coefficients],t)


def interval_polynomial(poly,interval):
    value=(Q(0),Q(0))
    for coefficient in poly.all_coeffs():
        values=[a*b for a in value for b in interval]
        value=(min(values)+coefficient,max(values)+coefficient)
    return value


def sign(interval):
    assert interval[0]>0 or interval[1]<0,interval
    return 1 if interval[0]>0 else -1


def chart_paths(ar,ai,br,bi):
    values=base+[(ar,ai,br,bi),(-ar,-ai,br,bi),
                 (br,bi,ar,ai),(-br,-bi,ar,ai)]
    charts=[]
    for a,c,b,d in values:
        vector=sp.Matrix([2*(a*b+c*d),2*(c*b-a*d),a*a+c*c-b*b-d*d])
        denominator=sp.expand(a*a+c*c+b*b+d*d)
        # Remove only the explicitly positive common factor1+t².
        while sp.rem(denominator,1+t*t,t)==0 and all(sp.rem(v,1+t*t,t)==0 for v in vector):
            denominator=sp.div(denominator,1+t*t,t)[0]
            vector=sp.Matrix([sp.div(v,1+t*t,t)[0] for v in vector])
        du=sp.Poly(sp.expand(175*denominator-P.dot(vector)),t)
        nu=sp.Poly(sp.expand(E.dot(vector)),t)
        nv=sp.Poly(sp.expand(F.dot(vector)),t)
        assert du.eval(0)>0 and du.count_roots(0,sp.oo)==0
        charts.append((nu,nv,du))
    return charts


def motion(name,charts,permutation):
    events=[];records=[]
    for i,j in combinations(range(10),2):
        ui,vi,di=charts[i];uj,vj,dj=charts[j]
        horizontal=integer_polynomial((ui*dj-uj*di).as_expr())
        vertical=integer_polynomial((vi*dj-vj*di).as_expr())
        assert not horizontal.is_zero and horizontal.eval(0)!=0
        assert horizontal.degree()==di.degree()+dj.degree()
        positives=[]
        for (left,right),multiplicity in sp.polys.polytools.intervals(horizontal,eps=Q(1,10**24)):
            if right<=0:continue
            assert left>0 and multiplicity==1
            assert (left==right and horizontal.eval(left)==0) or (
                left<right and horizontal.eval(left)*horizontal.eval(right)<0)
            assert horizontal.count_roots(left,right)==1
            interval=(left,right)
            derivative=interval_polynomial(horizontal.diff(),interval)
            height=interval_polynomial(vertical,interval)
            crossing_sign=-sign(derivative)*sign(height)
            events.append({"pair":[i,j],"interval":[fraction(left),fraction(right)],
                           "horizontal_coefficients":[int(c) for c in horizontal.all_coeffs()],
                           "vertical_coefficients":[int(c) for c in vertical.all_coeffs()],
                           "derivative_interval":[fraction(c) for c in derivative],
                           "vertical_interval":[fraction(c) for c in height],
                           "crossing_sign":crossing_sign,"_interval":interval})
            positives.append([fraction(left),fraction(right)])
        assert len(positives)==horizontal.count_roots(0,sp.oo)
        records.append({"pair":[i,j],"horizontal_coefficients":[int(c) for c in horizontal.all_coeffs()],
                        "vertical_coefficients":[int(c) for c in vertical.all_coeffs()],
                        "positive_root_intervals":positives})
    events.sort(key=lambda e:e["_interval"][0])
    assert all(a["_interval"][1]<b["_interval"][0] for a,b in zip(events,events[1:]))
    order=initial_order.copy();word=[]
    for event in events:
        left,right=sorted(order.index(i) for i in event["pair"])
        assert right==left+1,(name,event,order)
        letter=event["crossing_sign"]*(left+1)
        event["source_order"]=order.copy();event["artin_letter"]=letter
        word.append(letter)
        order[left],order[right]=order[right],order[left]
        del event["_interval"]
    assert order==[permutation[i] for i in initial_order]
    for i,(u,v,d) in enumerate(charts):
        expected=marking_data["projected_coordinates"][permutation[i]]
        assert u.degree()==v.degree()==d.degree()
        assert Q(u.LC(),d.LC())==Q(*expected[0])
        assert Q(v.LC(),d.LC())==Q(*expected[1])
    source=B+word+[-j for j in reversed(B)]
    print("PASS exact",name,"motion:",len(word),"crossings,",len(source),"marked source letters",flush=True)
    return source,{"name":name,"physical_word":word,"source_word":source,
                   "endpoint_permutation":permutation,"all_pair_polynomials":records,
                   "crossing_certificates":events,
                   "chart_polynomials":[[[int(c) for c in p.all_coeffs()] for p in row] for row in charts]}


first_perm=[0,1,2,3,4,5,7,6,9,8]
second_perm=[0,1,2,3,4,5,8,9,6,7]
first_charts=chart_paths(2*(1-t*t),4*t,1+t*t,0)
second_charts=chart_paths(4+t*t,3*t,2*(1+t*t),0)
first,first_record=motion("outer ellipse",first_charts,first_perm)
second,second_record=motion("inner meridian",second_charts,second_perm)
INPUT=HERE/"check_sphere10_induced_capped.npz"
data=np.load(INPUT)
table=data["capped_multiplication"];inverse=data["capped_inverse"]
gp=data["generator_permutations"];gw=data["generator_weights"]
ip=np.argsort(gp,axis=1);iw=np.array([inverse[gw[i,ip[i]]] for i in range(9)])


def evaluate(word):
    p,w=np.arange(630),np.zeros(630,dtype=np.int64)
    for letter in word:
        j=abs(letter)-1;rp=gp[j] if letter>0 else ip[j];rw=gw[j] if letter>0 else iw[j]
        p,w=rp[p],table[w,rw[p]]
    return p,w


def invert(word):return [-j for j in reversed(word)]


motion_images=[evaluate(first),evaluate(second)]
for word in (first,second):
    for hword in marking_data["source_H_words"]:
        p,w=evaluate(word+hword+invert(word)+invert(hword))
        assert np.array_equal(p,np.arange(630)) and not w.any()
print("PASS both actual quartet motions commute with both actual geometric H words in all630 states",flush=True)

# Exact E4 coordinates in the pre-existing fixed quotient basis.
qdata=json.loads((HERE/"check_sphere10_quaternary_extension.json").read_text())
pairs=[tuple(e) for e in qdata["edge_order"]];ei={e:i for i,e in enumerate(pairs)}
rows=np.array(qdata["reduced_relation_rows"]);pivots=qdata["relation_unit_pivots"];free=qdata["quotient_basis_edges"]


def e4_section(word,permutation):
    order=list(range(10));raw=np.zeros(45,dtype=np.int64)
    for letter in word:
        k=abs(letter)-1;edge=tuple(sorted((order[k],order[k+1])))
        raw[ei[edge]]+=1 if letter>0 else -1
        order[k],order[k+1]=order[k+1],order[k]
    assert [order.index(i) for i in range(10)]==permutation
    inv=[permutation.index(i) for i in range(10)]
    c=np.array([int(inv[i]>inv[j]) for i,j in pairs])
    assert not ((raw-c)%2).any()
    value=(raw-c)//2%4
    for row,pivot in zip(rows,pivots):value=(value-value[pivot]*row)%4
    return value[free]


sections=np.array([e4_section(first,first_perm),e4_section(second,second_perm)])
result={"scope":"Two actual H-equivariant quartet motion words and exact finite images; full ordinary-image census is separate.",
        "marking_source":"check_sphere10_geometric_klein.json",
        "input_sha256":hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "motion_records":[first_record,second_record],
        "finite_motion_permutations":[p.tolist() for p,w in motion_images],
        "finite_motion_weights":[w.tolist() for p,w in motion_images],
        "E4_motion_coordinates":sections.tolist(),"E4_colored_masks":[8,16]}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(Path(__file__).with_suffix(".npz"),
                    motion_permutations=np.array([p for p,w in motion_images]),
                    motion_weights=np.array([w for p,w in motion_images]),
                    E4_motion_coordinates=sections,E4_colored_masks=np.array([8,16]))
print("PASS complete two-motion path and finite-source certificate",flush=True)
