#!/usr/bin/env python3
"""Exact image of the two quartet motions and geometric H in the actual L.

First census the two-motion E4 image.  Every Schreier edge gives an
actual relative-kernel word.  The kernel is collected in the exact
class-two exponent-three coordinates of C_{N3^630}(H).
"""
from pathlib import Path
from collections import deque
from itertools import combinations
import json
import hashlib
import numpy as np

HERE=Path(__file__).resolve().parent
idata=np.load(HERE/"check_sphere10_induced_capped.npz")
mdata=np.load(HERE/"check_sphere10_centralizer_motion.npz")
fdata=json.loads((HERE/"check_sphere10_geometric_fixed_kernel.json").read_text())
base=json.loads((HERE/"check_sphere10_quaternary_extension.json").read_text())
table=idata["capped_multiplication"];inverse=idata["capped_inverse"]
normal=[int(i) for i in np.flatnonzero(idata["capped_character"]==0)]
mp=mdata["motion_permutations"];mw=mdata["motion_weights"]
mx=mdata["E4_motion_coordinates"];mm=mdata["E4_colored_masks"]
actions=np.asarray(base["actions"]);kappa=np.asarray(base["cocycle"])


def e4_key(mask,coordinate):return bytes([mask])+np.asarray(coordinate,dtype=np.uint8).tobytes()


states=[(0,np.zeros(35,dtype=np.int64))]
state_indices={e4_key(*states[0]):0};words=[()]
representative_p=[np.arange(630)];representative_w=[np.zeros(630,dtype=np.int64)]
edges=[];position=0
while position<len(states):
    mask,x=states[position];p=representative_p[position];w=representative_w[position]
    row=[]
    for generator in range(2):
        target_mask=int(mask^mm[generator])
        target_x=(x+actions[mask]@mx[generator]+kappa[mask,mm[generator]])%4
        key=e4_key(target_mask,target_x)
        target_p=mp[generator,p];target_w=table[w,mw[generator,p]]
        if key not in state_indices:
            state_indices[key]=len(states);states.append((target_mask,target_x))
            words.append(words[position]+(generator+1,))
            representative_p.append(target_p);representative_w.append(target_w)
        target=state_indices[key]
        assert np.array_equal(target_p,representative_p[target])
        row.append(target)
    edges.append(row);position+=1
assert len(states)<=4**5*4
base_order=len(states)
assert base_order==4096
assert base_order and base_order&(base_order-1)==0
base_exponent=base_order.bit_length()-1
edges=np.asarray(edges);representative_p=np.asarray(representative_p)
representative_w=np.asarray(representative_w)
print("PASS actual two-motion E4 image order2^%d = %d"%(base_exponent,base_order),flush=True)


def mul(*xs):
    value=0
    for x in xs:value=int(table[value,x])
    return value


def comm(x,y):return mul(x,y,inverse[x],inverse[y])


center=[x for x in normal if all(table[x,y]==table[y,x] for y in normal)]
x=next(x for x in normal if x not in center)
y=next(y for y in normal if comm(x,y)!=0)
z=comm(x,y)
powers=lambda x:[0,x,mul(x,x)]
xp,yp,zp=powers(x),powers(y),powers(z)
coordinates={}
for i in range(3):
    for j in range(3):
        for k in range(3):coordinates[mul(xp[i],yp[j],zp[k])]=(i,j,k)
assert set(coordinates)==set(normal)
for a in normal:
    i,j,k=coordinates[a]
    for b in normal:
        u,v,w=coordinates[b]
        assert coordinates[int(table[a,b])]==((i+u)%3,(j+v)%3,(k+w-j*u)%3)
orbits=fdata["orbits"]
full_orbits=[i for i,o in enumerate(orbits) if o["fixed_subgroup_order"]==27]
central_orbits=[i for i,o in enumerate(orbits) if o["fixed_subgroup_order"]==3]
assert len(full_orbits)==168 and len(central_orbits)==6
assert all(set(orbits[i]["allowed_representative_values"])==set(center) for i in central_orbits)
reps=np.array([o["representative"] for o in orbits])
full_position={orbit:i for i,orbit in enumerate(full_orbits)}
linear_dimension=2*len(full_orbits);central_dimension=len(orbits)


def lie_vector(weights):
    values=np.array([coordinates[int(weights[point])] for point in reps],dtype=np.int64)
    result=np.zeros(linear_dimension+central_dimension,dtype=np.int64)
    for orbit,i in full_position.items():result[2*i:2*i+2]=values[orbit,:2]
    assert not values[central_orbits,:2].any()
    result[linear_dimension:]=(values[:,2]+2*values[:,0]*values[:,1])%3
    return result


schreier_weights=[];schreier_lie=[];schreier_words=[]
for i in range(base_order):
    for generator in range(2):
        j=int(edges[i,generator])
        p=representative_p[i]
        product_weight=table[representative_w[i],mw[generator,p]]
        weight=table[product_weight,inverse[representative_w[j]]]
        assert all(int(v) in coordinates for v in weight)
        # Validate the compressed orbit coordinates against all fixed vectors.
        for orbit in orbits:
            values=weight[orbit["states"]].tolist()
            assert values in orbit["all_fixed_orbit_vectors"]
        schreier_weights.append(weight);schreier_lie.append(lie_vector(weight))
        schreier_words.append(list(words[i]) + [generator+1] + [-v for v in reversed(words[j])])
schreier_lie=np.asarray(schreier_lie,dtype=np.int64)
print("PASS all%d actual Schreier edges lie in the named fixed-kernel coordinates"%len(schreier_lie),flush=True)


def row_basis(matrix):
    matrix=np.asarray(matrix,dtype=np.int64).copy()%3
    rank=0;pivots=[]
    for column in range(matrix.shape[1]):
        options=np.flatnonzero(matrix[rank:,column])
        if not len(options):continue
        row=rank+int(options[0]);matrix[[rank,row]]=matrix[[row,rank]]
        matrix[rank]=matrix[rank]*int(matrix[rank,column])%3
        selected=np.flatnonzero(matrix[:,column]);selected=selected[selected!=rank]
        matrix[selected]=(matrix[selected]-matrix[selected,column,None]*matrix[rank])%3
        pivots.append(column);rank+=1
        if rank==len(matrix):break
    return matrix[:rank],pivots


basis,pivots=row_basis(schreier_lie)
linear_rank=sum(p<linear_dimension for p in pivots)
assert pivots[:linear_rank] and all(p<linear_dimension for p in pivots[:linear_rank])
initial_central=basis[linear_rank:,linear_dimension:]
central_basis,central_pivots=row_basis(initial_central)
assert linear_rank==198 and len(central_basis)==98
print("initial Lie ranks:",linear_rank,"noncentral,",len(central_basis),"central",flush=True)


def add_central(vector):
    global central_basis,central_pivots
    vector=vector.copy()%3
    for row,pivot in zip(central_basis,central_pivots):
        coefficient=int(vector[pivot])
        if coefficient:vector=(vector-coefficient*row)%3
    positions=np.flatnonzero(vector)
    if not len(positions):return False
    pivot=int(positions[0]);vector=vector*int(vector[pivot])%3
    central_basis=np.vstack((central_basis,vector))
    central_pivots.append(pivot)
    # Existing pivots need not be ordered: each subsequent row is zero
    # at all previous pivot positions, which suffices for reduction.
    return True


bracket_witnesses=[]
for i,j in combinations(range(linear_rank),2):
    left=basis[i,:linear_dimension].reshape(-1,2)
    right=basis[j,:linear_dimension].reshape(-1,2)
    bracket=np.zeros(central_dimension,dtype=np.int64)
    bracket[full_orbits]=(left[:,0]*right[:,1]-left[:,1]*right[:,0])%3
    if add_central(bracket):bracket_witnesses.append([i,j])
central_rank=len(central_basis)
kernel_rank=linear_rank+central_rank
assert central_rank==104 and len(bracket_witnesses)==6 and kernel_rank==302
print("PASS exact class-two Lie closure: noncentral rank%d,central rank%d,total%d"%
      (linear_rank,central_rank,kernel_rank),flush=True)
print("two_motion_image_order:2^%d * 3^%d"%(base_exponent,kernel_rank),flush=True)
print("ordinary_centralizer_image_with_H_order:2^%d * 3^%d"%(base_exponent+2,kernel_rank),flush=True)
assert base_exponent+2<=27 and kernel_rank<=510
result={
    "scope":"Exact joint finite image of two specified quartet motions and actual H; source identification with ordinary N is supplied by the separate path proof.",
    "input_motion_sha256":hashlib.sha256((HERE/"check_sphere10_centralizer_motion.npz").read_bytes()).hexdigest(),
    "E4_motion_image_order":base_order,"E4_motion_image_two_exponent":base_exponent,
    "E4_states":[[int(m),v.tolist()] for m,v in states],"E4_representative_words":words,
    "E4_generator_edges":edges.tolist(),
    "heisenberg_generators":[x,y,z],"heisenberg_coordinates":{str(k):v for k,v in coordinates.items()},
    "full_orbit_indices":full_orbits,"central_orbit_indices":central_orbits,
    "Schreier_words":schreier_words,
    "initial_Lie_pivots":pivots,"noncentral_rank":linear_rank,
    "initial_central_rank":len(initial_central),"central_rank":central_rank,
    "bracket_witnesses":bracket_witnesses,"kernel_three_exponent":kernel_rank,
    "ordinary_image_two_exponent":base_exponent+2,"ordinary_image_three_exponent":kernel_rank,
    "finite_centralizer_two_exponent":27,"finite_centralizer_three_exponent":510,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(Path(__file__).with_suffix(".npz"),schreier_weights=np.array(schreier_weights),
                    schreier_lie=schreier_lie,initial_lie_basis=basis,
                    final_central_basis=central_basis,E4_edges=edges,
                    E4_representative_permutations=representative_p,
                    E4_representative_weights=representative_w)
print("PASS complete ordinary-image census certificate",flush=True)
