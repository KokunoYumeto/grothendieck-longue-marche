#!/usr/bin/env python3
"""Exact fixed subgroup of the relative ternary kernel under the marked H.

This computes C_{N3^630}(H) from the actual geometric H source words.
It makes no assertion that the whole finite centralizer comes from the
ordinary geometric centralizer.
"""
from pathlib import Path
from collections import deque, Counter
import json
import hashlib
import numpy as np

HERE=Path(__file__).resolve().parent
INPUT=HERE/"check_sphere10_induced_capped.npz"
HINPUT=HERE/"check_sphere10_geometric_klein.npz"
data=np.load(INPUT);hdata=np.load(HINPUT)
table=data["capped_multiplication"];inverse=data["capped_inverse"]
normal=[int(i) for i in np.flatnonzero(data["capped_character"]==0)]
assert len(normal)==27
hp=hdata["geometric_H_permutations"];hw=hdata["geometric_H_weights"]


def product(left,right):
    p,w=left;q,v=right
    return q[p],table[w,v[p]]


identity=(np.arange(630),np.zeros(630,dtype=np.int64))
h=[identity,(hp[0],hw[0]),(hp[1],hw[1]),
   product((hp[0],hw[0]),(hp[1],hw[1]))]
for i in range(4):
    for j in range(4):
        answer=product(h[i],h[j])
        assert np.array_equal(answer[0],h[i^j][0])
        assert np.array_equal(answer[1],h[i^j][1])
seen=set();orbits=[];exponent=0
for representative in range(630):
    if representative in seen:continue
    orbit=sorted({int(p[representative]) for p,w in h})
    seen.update(orbit)
    stabilizer=[j for j,(p,w) in enumerate(h) if p[representative]==representative]
    allowed=[x for x in normal if all(table[x,h[j][1][representative]]
                                     ==table[h[j][1][representative],x]
                                     for j in stabilizer)]
    assert len(allowed) in (1,3,9,27)
    power={1:0,3:1,9:2,27:3}[len(allowed)]
    exponent+=power
    transporters={point:next(j for j,(p,w) in enumerate(h)
                            if p[representative]==point) for point in orbit}
    extensions=[]
    for x in allowed:
        values={}
        for point,j in transporters.items():
            weight=int(h[j][1][representative])
            values[point]=int(table[table[inverse[weight],x],weight])
        for point in orbit:
            for p,w in h:
                assert values[point]==table[table[w[point],values[int(p[point])]],inverse[w[point]]]
        extensions.append([values[point] for point in orbit])
    orbits.append({"representative":representative,"states":orbit,
                   "stabilizer_H_indices":stabilizer,
                   "allowed_representative_values":allowed,
                   "fixed_subgroup_order":len(allowed),
                   "transporters":[transporters[p] for p in orbit],
                   "all_fixed_orbit_vectors":extensions})
assert len(seen)==630
sizes=Counter(len(o["states"]) for o in orbits)
assert sizes=={1:6,2:24,4:144}
profile=Counter((len(o["states"]),o["fixed_subgroup_order"]) for o in orbits)
print("PASS actual H orbit decomposition:144 free,24 two-state,6 fixed states")
print("PASS all fixed Heisenberg tuples from exact stabilizers and transport maps")
print("orbit_size/fixed_order/count:",sorted((a,b,n) for (a,b),n in profile.items()))
print("relative_kernel_centralizer_order:3^%d"%exponent)

# Compute the actual E4 centralizer with the marked section, over Z/4.
base=json.loads((HERE/"check_sphere10_quaternary_extension.json").read_text())
actions=np.array(base["actions"],dtype=np.int64)
kappa=np.array(base["cocycle"],dtype=np.int64)
a,b=base["H_masks"];I=np.eye(35,dtype=np.int64)
xa,xb=hdata["geometric_E4_section_coordinates"]
matrix=np.vstack((I-actions[a],I-actions[b]))%4


def solve_mod4(source,rhs):
    source=source.copy()%4;rhs=rhs.copy()%4
    mat=source.copy();value=rhs.copy();rank=0;piv=[]
    for j in range(mat.shape[1]):
        options=np.flatnonzero(mat[rank:,j]%2)
        if not len(options):continue
        k=rank+int(options[0])
        mat[[rank,k]]=mat[[k,rank]];value[[rank,k]]=value[[k,rank]]
        unit=int(mat[rank,j]);mat[rank]=mat[rank]*unit%4;value[rank]=value[rank]*unit%4
        for row in range(len(mat)):
            if row==rank:continue
            coefficient=int(mat[row,j])
            mat[row]=(mat[row]-coefficient*mat[rank])%4
            value[row]=(value[row]-coefficient*value[rank])%4
        piv.append(j);rank+=1
    free=[j for j in range(mat.shape[1]) if j not in piv]
    assert not (mat[rank:]%2).any()
    if (value[rank:]%2).any():return None,rank,None
    binary=mat[rank:,free]//2;bv=value[rank:]//2;two_rank=0;bpiv=[]
    for j in range(len(free)):
        options=np.flatnonzero(binary[two_rank:,j])
        if not len(options):continue
        k=two_rank+int(options[0])
        binary[[two_rank,k]]=binary[[k,two_rank]];bv[[two_rank,k]]=bv[[k,two_rank]]
        for row in range(len(binary)):
            if row!=two_rank and binary[row,j]:
                binary[row]^=binary[two_rank];bv[row]^=bv[two_rank]
        bpiv.append(j);two_rank+=1
    if bv[two_rank:].any():return None,rank,two_rank
    free_value=np.zeros(len(free),dtype=np.int64)
    for row,j in enumerate(bpiv):free_value[j]=bv[row]
    solution=np.zeros(35,dtype=np.int64);solution[free]=free_value
    for row,j in enumerate(piv):solution[j]=(value[row]-mat[row,free]@free_value)%4
    assert np.array_equal(source@solution%4,rhs)
    return solution,rank,two_rank


zero,unit_rank,two_rank=solve_mod4(matrix,np.zeros(70,dtype=np.int64))
assert (unit_rank,two_rank)==(23,1)
module_order_exponent=2*(35-unit_rank)-two_rank
assert module_order_exponent==23
centralizer_lifts=[]
for mask in range(32):
    rhs=np.concatenate(((I-actions[mask])@xa+kappa[a,mask]-kappa[mask,a],
                        (I-actions[mask])@xb+kappa[b,mask]-kappa[mask,b]))%4
    solution,rank,rank2=solve_mod4(matrix,rhs)
    expected=(bin(mask&7).count("1")%2==0)
    assert (solution is not None)==expected
    if solution is not None:
        for hmask,xh in ((a,xa),(b,xb)):
            assert np.array_equal((solution+actions[mask]@xh+kappa[mask,hmask])%4,
                                  (xh+actions[hmask]@solution+kappa[hmask,mask])%4)
        centralizer_lifts.append({"colored_mask":mask,"pure_coordinate":solution.tolist()})
assert len(centralizer_lifts)==16
print("PASS E4 invariant module has Smith factors1^23,2^1,0^11 and order2^23")
print("PASS exactly16 colored permutations lift to the actual E4 centralizer, with explicit lifts")
print("E4_centralizer_order:2^27")
out={"scope":"Exact fixed subgroup of N3^630 under the actual marked geometric H; no ordinary-centralizer image assertion.",
     "input_sha256":hashlib.sha256(INPUT.read_bytes()).hexdigest(),
     "H_input_sha256":hashlib.sha256(HINPUT.read_bytes()).hexdigest(),
     "orbit_size_profile":dict(sizes),"fixed_group_exponent":exponent,"orbits":orbits,
     "E4_pure_invariant_matrix":matrix.tolist(),"E4_unit_rank":unit_rank,
     "E4_two_rank":two_rank,"E4_pure_invariant_order_exponent":module_order_exponent,
     "E4_colored_centralizer_lifts":centralizer_lifts,"E4_centralizer_order_exponent":27}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
