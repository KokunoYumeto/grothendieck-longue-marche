#!/usr/bin/env python3
"""Pending exact binary quotient for the ten-point colored comparison.

Builds the actual sphere braid quotient from crossing coordinates modulo4,
then solves every V4 complement equation over the pure abelianization F2.
No algebraic complement is identified with a chosen geometric section.
"""
from itertools import combinations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
pairs=list(combinations(range(10),2)); edge_index={e:i for i,e in enumerate(pairs)}


def echelon(vectors):
    basis={}
    for row in vectors:
        while row:
            pivot=row.bit_length()-1
            if pivot in basis:
                row^=basis[pivot]
            else:
                basis[pivot]=row
                break
    return basis


def reduce_by(row,basis):
    for pivot in sorted(basis,reverse=True):
        if (row>>pivot)&1:
            row^=basis[pivot]
    return row


relations=[sum(1<<k for k,(a,b) in enumerate(pairs) if i in (a,b)) for i in range(10)]
relations.append((1<<45)-1)
relation_basis=echelon(relations)
assert len(relation_basis)==10
free=[j for j in range(45) if j not in relation_basis]
assert len(free)==35


def quotient(row):
    row=reduce_by(row,relation_basis)
    return sum(((row>>j)&1)<<i for i,j in enumerate(free))


def compose(p,q):
    return tuple(p[q[i]] for i in range(10))


def transpositions(ts):
    p=list(range(10))
    for a,b in ts:p[a],p[b]=p[b],p[a]
    return tuple(p)


generators=[transpositions([(0,1)]),transpositions([(2,3)]),
            transpositions([(4,5)]),transpositions([(6,7),(8,9)]),
            transpositions([(6,8),(7,9)])]
permutations=[]
for mask in range(32):
    p=tuple(range(10))
    for i,g in enumerate(generators):
        if (mask>>i)&1:p=compose(p,g)
    permutations.append(p)
assert len(set(permutations))==32
for i in range(32):
    for j in range(32):assert compose(permutations[i],permutations[j])==permutations[i^j]


def edge_permutation(p):
    return [edge_index[tuple(sorted((p[a],p[b])))] for a,b in pairs]


edge_perms=[edge_permutation(p) for p in permutations]


def permute_bits(row,p):
    return sum(((row>>i)&1)<<p[i] for i in range(45))


for p in edge_perms:
    assert all(quotient(permute_bits(r,p))==0 for r in relations)
actions=[[quotient(1<<p[j]) for j in free] for p in edge_perms]


def act(mask,row):
    result=0
    while row:
        bit=row&-row
        result^=actions[mask][bit.bit_length()-1]
        row^=bit
    return result


crossings=[]
for p in permutations:
    inverse=[p.index(i) for i in range(10)]
    crossings.append([int(inverse[a]>inverse[b]) for a,b in pairs])
kappa={}
for a in range(32):
    for b in range(32):
        permuted=[0]*45
        for i,j in enumerate(edge_perms[a]):permuted[j]=crossings[b][i]
        differences=[crossings[a][i]+permuted[i]-crossings[a^b][i] for i in range(45)]
        assert all(d%2==0 for d in differences)
        kappa[a,b]=quotient(sum(((d//2)%2)<<i for i,d in enumerate(differences)))
for a in range(32):
    for b in range(32):
        for c in range(32):
            assert kappa[a,b]^kappa[a^b,c] == act(a,kappa[b,c])^kappa[a,b^c]
print('PASS actual C2^5 crossing-cocycle extension with pure module F2^35',flush=True)


def braid_crossings(word):
    order=list(range(10));raw=[0]*45
    for letter in word:
        k=abs(letter)-1
        edge=edge_index[tuple(sorted((order[k],order[k+1])))]
        raw[edge]=(raw[edge]+(1 if letter>0 else -1))%4
        order[k],order[k+1]=order[k+1],order[k]
    return tuple(order),raw


sphere=list(range(1,9))+[9,9]+list(range(8,0,-1))
full=list(range(1,10))*10
for name,word in [('sphere',sphere),('full_twist',full)]:
    p,c=braid_crossings(word)
    assert p==tuple(range(10)) and all(x%2==0 for x in c)
    assert quotient(sum((x//2)<<i for i,x in enumerate(c)))==0
    pp,cc=braid_crossings([-letter for letter in word])
    assert pp==tuple(range(10)) and all(x%2==0 for x in cc)
    assert quotient(sum((x//2)<<i for i,x in enumerate(cc)))==0
print('PASS literal spherical and full-twist relation images',flush=True)

standard_argument_images=[]
for i in range(1,10):
    pp,cc=braid_crossings([i,i])
    assert pp==tuple(range(10)) and all(x%2==0 for x in cc)
    square=quotient(sum((x//2)<<j for j,x in enumerate(cc)))
    assert square==quotient(1<<edge_index[(i-1,i)]) and square!=0
    if i>1:
        yi=list(range(i-1,0,-1))+list(range(1,i))
        pp,cc=braid_crossings(yi)
        assert pp==tuple(range(10)) and all(x%2==0 for x in cc)
        image=quotient(sum((x//2)<<j for j,x in enumerate(cc)))
        standard_argument_images.append({'generator':i,'y_word':yi,'square':square,'y_image':image})
print('PASS all standard conjugator arguments are pure, and every braid generator has order4',flush=True)

# a fixes A0, b fixes B0.  Their other marked permutations are those
# of w->-w and w->1/w on A0,B0,C0 and the ordered regular orbit D0.
a=(1<<1)|(1<<2)|(1<<3)
b=(1<<0)|(1<<2)|(1<<4)
assert permutations[a]==(0,1,3,2,5,4,7,6,9,8)
assert permutations[b]==(1,0,2,3,5,4,8,9,6,7)


def linear_rows(images,outdim=35):
    return [sum(((image>>i)&1)<<j for j,image in enumerate(images)) for i in range(outdim)]


one_a=[(1<<i)^actions[a][i] for i in range(35)]
one_b=[(1<<i)^actions[b][i] for i in range(35)]
rows_a=linear_rows(one_a)
rows_b=linear_rows(one_b)
equations=[]
for row,rhs in [(rows_a,kappa[a,a]),(rows_b,kappa[b,b])]:
    offset=0 if row is rows_a else 35
    equations.extend((r<<offset,(rhs>>i)&1) for i,r in enumerate(row))
rhs=kappa[a,b]^kappa[b,a]
equations.extend((rows_b[i]|(rows_a[i]<<35),(rhs>>i)&1) for i in range(35))


def solve(equations,nvars):
    basis={}
    for row,rhs in equations:
        while row:
            pivot=row.bit_length()-1
            if pivot in basis:
                other,value=basis[pivot];row^=other;rhs^=value
            else:
                basis[pivot]=(row,rhs);break
        if not row:assert not rhs,'inconsistent complement equations'
    def lift(free_bits,affine):
        value=free_bits
        for pivot,(row,rhs) in sorted(basis.items()):
            bit=((row&value).bit_count()&1)^(rhs if affine else 0)
            if bit:value^=1<<pivot
        return value
    base=lift(0,True)
    kernel=[lift(1<<j,False) for j in range(nvars) if j not in basis]
    assert all(((row&base).bit_count()&1)==rhs for row,rhs in equations)
    assert all(not ((row&v).bit_count()&1) for row,rhs in equations for v in kernel)
    return base,kernel,len(basis)


base,kernel,rank=solve(equations,70)
coboundary=[one_a[i]|(one_b[i]<<35) for i in range(35)]
cobasis=echelon(coboundary)
invariants=35-len(cobasis)
h1_basis=echelon(reduce_by(v,cobasis) for v in kernel)
h1_dimension=len(h1_basis)
assert h1_dimension==len(kernel)-len(cobasis)
assert (rank,len(kernel),len(cobasis),h1_dimension,invariants)==(40,30,23,7,12)
print('PASS complement equations: rank',rank,'Z1',len(kernel),'B1',len(cobasis),
      'H1',h1_dimension,'invariant module',invariants,flush=True)

class_vectors=list(h1_basis.values())
classes=[]
class_index={}
for mask in range(1<<h1_dimension):
    value=0
    for i,row in enumerate(class_vectors):
        if (mask>>i)&1:value^=row
    value=reduce_by(value,cobasis)
    class_index[value]=len(classes)
    classes.append(value)
assert len(class_index)==128
class_actions=[]
for colored in range(32):
    row=[]
    for value in classes:
        section=base^value
        x,y=section&((1<<35)-1),section>>35
        xx=act(colored,x)^kappa[colored,a]^kappa[a,colored]
        yy=act(colored,y)^kappa[colored,b]^kappa[b,colored]
        value2=reduce_by((xx|(yy<<35))^base,cobasis)
        assert value2 in class_index
        row.append(class_index[value2])
    assert sorted(row)==list(range(128))
    class_actions.append(row)
for c in range(32):
    for d in range(32):
        assert all(class_actions[c][class_actions[d][i]]==class_actions[c^d][i] for i in range(128))
orbits=[];seen=set()
for i in range(128):
    if i in seen:continue
    orbit=sorted({class_actions[c][i] for c in range(32)})
    seen.update(orbit)
    orbits.append(orbit)
stabilizers=[[c for c in range(32) if class_actions[c][i]==i] for i in range(128)]
expected_stabilizer=[c for c in range(32) if ((c&7).bit_count()%2)==0]
expected_classes=[i for i,st in enumerate(stabilizers) if st==expected_stabilizer]
orbit_sizes={size:sum(len(orbit)==size for orbit in orbits) for size in sorted(set(map(len,orbits)))}
assert orbit_sizes=={2:64} and len(expected_classes)==128
print('PASS all128 complement classes and colored actions; orbit counts',orbit_sizes,
      'classes with geometric permutation stabilizer',len(expected_classes),flush=True)

# Every automorphism of the extension acting identically on its pure
# module and its colored quotient is exactly a1-cocycle of C2^5 in V.
# Compute the actual restriction map to the named H, not only dimensions.
colored_one=[]
for i in range(5):
    colored_one.append([(1<<j)^actions[1<<i][j] for j in range(35)])
colored_rows=[linear_rows(images) for images in colored_one]
colored_equations=[]
for i in range(5):
    colored_equations.extend((row<<(35*i),0) for row in colored_rows[i])
for i in range(5):
    for j in range(i+1,5):
        colored_equations.extend(((colored_rows[j][r]<<(35*i))|
                                  (colored_rows[i][r]<<(35*j)),0) for r in range(35))
zero,colored_kernel,colored_rank=solve(colored_equations,175)
assert zero==0


def cocycle_value(vector,mask):
    value=0;prefix=0
    for i in range(5):
        if (mask>>i)&1:
            generator_value=(vector>>(35*i))&((1<<35)-1)
            value^=act(prefix,generator_value)
            prefix^=1<<i
    return value


restrictions=[]
for vector in colored_kernel:
    restricted=cocycle_value(vector,a)|(cocycle_value(vector,b)<<35)
    assert all(not ((row&restricted).bit_count()&1) for row,rhs in equations)
    restrictions.append(reduce_by(restricted,cobasis))
restriction_basis=echelon(restrictions)
colored_coboundary=[sum(colored_one[i][j]<<(35*i) for i in range(5)) for j in range(35)]
colored_B1=len(echelon(colored_coboundary))
assert (len(colored_kernel),colored_B1,len(restriction_basis))==(54,27,7)
print('PASS exact restriction H1(C2^5,V)->H1(H,V): rank',len(restriction_basis),
      'source H1',len(colored_kernel)-colored_B1,flush=True)

# A full genus-zero mixed action also extends across the other adjacent
# transpositions.  Compute that stronger, exact restriction map too.
adjacent=[transpositions([(i,i+1)]) for i in range(9)]
adjacent_actions=[[quotient(1<<p[j]) for j in free]
                  for p in map(edge_permutation,adjacent)]


def apply_columns(images,row):
    result=0
    while row:
        bit=row&-row;result^=images[bit.bit_length()-1];row^=bit
    return result


adjacent_rows=[linear_rows([(1<<j)^images[j] for j in range(35)])
               for images in adjacent_actions]
symmetric_equations=[]
for i in range(9):
    symmetric_equations.extend((row<<(35*i),0) for row in adjacent_rows[i])
for i in range(9):
    for j in range(i+2,9):
        symmetric_equations.extend(((adjacent_rows[j][r]<<(35*i))|
                                    (adjacent_rows[i][r]<<(35*j)),0) for r in range(35))
for i in range(8):
    j=i+1;Ti,Tj=adjacent_actions[i],adjacent_actions[j]
    coeff_i=[(1<<r)^apply_columns(Ti,Tj[r])^Tj[r] for r in range(35)]
    coeff_j=[Ti[r]^(1<<r)^apply_columns(Tj,Ti[r]) for r in range(35)]
    ri,rj=linear_rows(coeff_i),linear_rows(coeff_j)
    symmetric_equations.extend(((ri[r]<<(35*i))|(rj[r]<<(35*j)),0) for r in range(35))
zero,symmetric_kernel,symmetric_rank=solve(symmetric_equations,315)
assert zero==0


def permutation_word(p):
    current=list(range(10));word=[]
    for i,target in enumerate(p):
        j=current.index(target)
        while j>i:
            current[j-1],current[j]=current[j],current[j-1]
            word.append(j-1);j-=1
    assert tuple(current)==p
    return word


arbitrary_action_cache={}


def arbitrary_action(p,row):
    if p not in arbitrary_action_cache:
        ep=edge_permutation(p)
        arbitrary_action_cache[p]=[quotient(1<<ep[j]) for j in free]
    return apply_columns(arbitrary_action_cache[p],row)


def symmetric_cocycle_value(vector,p):
    value=0;prefix=tuple(range(10))
    for letter in permutation_word(p):
        generator_value=(vector>>(35*letter))&((1<<35)-1)
        value^=arbitrary_action(prefix,generator_value)
        prefix=compose(prefix,adjacent[letter])
    assert prefix==p
    return value


symmetric_restrictions=[]
for vector in symmetric_kernel:
    restricted=symmetric_cocycle_value(vector,permutations[a])|(
                symmetric_cocycle_value(vector,permutations[b])<<35)
    assert all(not ((row&restricted).bit_count()&1) for row,rhs in equations)
    symmetric_restrictions.append(reduce_by(restricted,cobasis))
symmetric_restriction_basis=echelon(symmetric_restrictions)
symmetric_coboundary=[sum(((1<<j)^adjacent_actions[i][j])<<(35*i) for i in range(9))
                       for j in range(35)]
symmetric_B1=len(echelon(symmetric_coboundary))
mirror=sum(quotient(1<<edge_index[(i,i+1)])<<(35*i) for i in range(9))
assert all(not ((row&mirror).bit_count()&1) for row,rhs in symmetric_equations)
assert reduce_by(mirror,echelon(symmetric_coboundary))
assert len(echelon(symmetric_coboundary+[mirror]))==len(symmetric_kernel)==36
geometric_flip=classes[class_actions[4][0]]
assert all(classes[class_actions[4][i]]^classes[i]==geometric_flip for i in range(128))
flip_span=echelon([geometric_flip])
inside_flip=all(not reduce_by(row,flip_span) for row in symmetric_restriction_basis.values())
assert (len(symmetric_kernel),symmetric_B1,len(symmetric_restriction_basis))==(36,35,1)
assert inside_flip is True and geometric_flip != 0
print('PASS exact restriction H1(S10,V)->H1(H,V): rank',len(symmetric_restriction_basis),
      'source H1',len(symmetric_kernel)-symmetric_B1,
      'contained in geometric two-class direction',inside_flip,flush=True)
print('PASS flip-C0 translates every one of the128 classes by that same restriction direction',flush=True)
print('PASS all finite full-mixed identity-residue automorphisms are inner-V times the literal braid mirror',flush=True)

# Literal mirror beta(pi)=the inversion vector c_pi modulo spherical
# relations.  Its restriction agrees with the Coxeter cocycle and gives
# the unique nonzero H1 direction just computed.
mirror_values=[]
for mask,p in enumerate(permutations):
    value=quotient(sum(bit<<i for i,bit in enumerate(crossings[mask])))
    assert value==symmetric_cocycle_value(mirror,p)
    mirror_values.append(value)
mirror_H=mirror_values[a]|(mirror_values[b]<<35)
assert reduce_by(mirror_H,cobasis)==geometric_flip

# The correction for every section is an explicit affine formula.
# It is enough to verify the base point and all30 independent Z1
# directions.  The chosen half twist is sigma5, swapping C0=(4,5).
flip=4


def pair_action(mask,pair):
    return act(mask,pair&((1<<35)-1))|(act(mask,pair>>35)<<35)


flip_commutator=(kappa[flip,a]^kappa[a,flip])|(
                 (kappa[flip,b]^kappa[b,flip])<<35)
correction_rhs=base^pair_action(flip,base^mirror_H)^flip_commutator
correction_rows=linear_rows(coboundary,outdim=70)


def correct(rhs):
    solution,nullspace,co_rank=solve([(row,(rhs>>i)&1) for i,row in enumerate(correction_rows)],35)
    assert co_rank==23 and len(nullspace)==12
    actual=0
    for i,column in enumerate(coboundary):
        if (solution>>i)&1:actual^=column
    assert actual==rhs
    return solution


base_correction=correct(correction_rhs)
direction_corrections=[correct(vector^pair_action(flip,vector)) for vector in kernel]


def extension_mul(left,right):
    x,c=left;y,d=right
    return (x^act(c,y)^kappa[c,d],c^d)


def extension_inverse(element):
    x,c=element
    return (act(c,x^kappa[c,c]),c)


for direction,correction in [(0,0)]+list(zip(kernel,direction_corrections)):
    section=base^direction;w=base_correction^correction
    conjugator=(w,flip);conjugator_inverse=extension_inverse(conjugator)
    for mask,x in [(a,section&((1<<35)-1)),(b,section>>35)]:
        mirrored=(x^mirror_values[mask],mask)
        corrected=extension_mul(extension_mul(conjugator,mirrored),conjugator_inverse)
        assert corrected==(x,mask)
pure_basis_words=[]
for k,edge in enumerate(free):
    i,j=pairs[edge]
    word=list(range(j,i+1,-1))+[i+1,i+1]+[-r for r in range(i+2,j+1)]
    pp,cc=braid_crossings(word)
    assert pp==tuple(range(10)) and all(x%2==0 for x in cc)
    assert quotient(sum((x//2)<<r for r,x in enumerate(cc)))==1<<k
    pure_basis_words.append(word)
base_correction_word=[letter for i,word in enumerate(pure_basis_words)
                       if (base_correction>>i)&1 for letter in word]
pp,cc=braid_crossings(base_correction_word)
assert pp==tuple(range(10))
assert quotient(sum((x//2)<<i for i,x in enumerate(cc)))==base_correction
print('PASS literal mirror restriction and explicit pure correction for every affine section direction',flush=True)

# Separate array elimination, using ascending pivots, verifies all stated
# ranks independently of the packed-integer echelon implementation.
import numpy as np


def array_rank(rows,ncols):
    matrix=np.array([[(row>>j)&1 for j in range(ncols)] for row in rows],dtype=np.uint8)
    rank=0
    for j in range(ncols):
        possible=np.flatnonzero(matrix[rank:,j])
        if not len(possible):continue
        pivot=rank+int(possible[0]);matrix[[rank,pivot]]=matrix[[pivot,rank]]
        targets=np.flatnonzero(matrix[rank+1:,j])+rank+1
        matrix[targets]^=matrix[rank]
        rank+=1
        if rank==len(matrix):break
    return rank


assert array_rank([row for row,rhs in equations],70)==rank
assert array_rank(coboundary,70)==len(cobasis)
assert array_rank([row for row,rhs in symmetric_equations],315)==symmetric_rank
assert array_rank(symmetric_coboundary,315)==symmetric_B1==35
assert array_rank(symmetric_coboundary+[mirror],315)==36
print('PASS independent array ranks for H and S10 cocycles, coboundaries and mirror complement',flush=True)

result={
    'scope':'Exact sphere10 binary mixed extension and its V4 complement equations; no selected algebraic complement is identified with a chosen geometric subgroup.',
    'edge_order':pairs,'spherical_relation_rank':10,'pure_module_dimension':35,
    'quotient_basis_edges':free,'colored_permutations':permutations,
    'colored_generator_names':['flip_A','flip_B','flip_C','translate_D_a','translate_D_b'],
    'actions':actions,'cocycle':[[kappa[i,j] for j in range(32)] for i in range(32)],
    'H_masks':[a,b],'complement_equation_rank':rank,
    'base_complement_coordinates':[base&((1<<35)-1),base>>35],
    'Z1_basis':kernel,'B1_basis':list(cobasis.values()),'H1_basis':list(h1_basis.values()),
    'H1_dimension':h1_dimension,'module_invariant_dimension':invariants,
    'complement_classes':classes,'colored_class_actions':class_actions,
    'colored_class_orbits':orbits,'colored_orbit_counts':orbit_sizes,
    'class_stabilizers':stabilizers,
    'geometric_permutation_stabilizer':expected_stabilizer,
    'classes_with_geometric_permutation_stabilizer':expected_classes,
    'colored_Z1_basis':colored_kernel,'colored_Z1_dimension':len(colored_kernel),
    'colored_B1_dimension':colored_B1,'colored_H1_dimension':len(colored_kernel)-colored_B1,
    'restriction_H1_basis':list(restriction_basis.values()),
    'restriction_H1_rank':len(restriction_basis),
    'symmetric_Z1_basis':symmetric_kernel,'symmetric_Z1_dimension':len(symmetric_kernel),
    'symmetric_B1_dimension':symmetric_B1,
    'symmetric_H1_dimension':len(symmetric_kernel)-symmetric_B1,
    'symmetric_restriction_H1_basis':list(symmetric_restriction_basis.values()),
    'symmetric_restriction_H1_rank':len(symmetric_restriction_basis),
    'geometric_flip_direction':geometric_flip,
    'symmetric_restriction_in_geometric_flip_direction':inside_flip,
    'named_H_adjacent_transposition_words':[permutation_word(permutations[a]),permutation_word(permutations[b])],
    'H_complement_equations':equations,'S10_cocycle_equations':symmetric_equations,
    'S10_coboundary_columns':symmetric_coboundary,'mirror_cocycle':mirror,
    'standard_GT_pure_argument_images':standard_argument_images,
    'mirror_values_on_colored_group':mirror_values,'mirror_H_value':mirror_H,
    'mirror_flip_correction_base':base_correction,
    'mirror_flip_correction_directions':direction_corrections,
    'mirror_flip_correction_base_word':base_correction_word,
    'pure_module_basis_braid_words':pure_basis_words,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS complete finite binary-extension certificate',flush=True)
