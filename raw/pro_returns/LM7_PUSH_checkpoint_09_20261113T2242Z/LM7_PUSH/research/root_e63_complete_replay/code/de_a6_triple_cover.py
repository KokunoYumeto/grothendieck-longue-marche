#!/usr/bin/env python3
"""Exact central-three cover of the retained A6, from a PG2(F4) hyperoval.

The complete determinant-one stabilizer is enumerated in 3x3 matrices.
Its quotient is the actual six-point A6 from the saved model. Every
automorphism lift is constructed and checked on the complete Cayley graph;
no abstract multiplier identification is used.
"""
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from collections import Counter
import json, time
import numpy as np

HERE = Path(__file__).resolve().parent
STEM = 'de_a6_triple_cover'


def main():
    started = time.time(); old_path = HERE/'de_ferrari_a6_kernels.npz'
    digest = sha256(old_path.read_bytes()).hexdigest(); old = np.load(old_path)
    # F4 = F2[t]/(t^2+t+1), with codes 0,1,t,t+1 and addition XOR.
    field = np.zeros((4,4), dtype=np.uint8)
    for a in range(4):
        for b in range(4):
            c = 0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:
                        c ^= 1<<(i+j)
            if c&4:
                c ^= 7
            field[a,b] = c
    inverse = np.array([0,1,3,2], dtype=np.uint8)
    assert all(field[a,inverse[a]] == 1 for a in (1,2,3))
    codes = np.arange(4**9, dtype=np.uint32)
    matrices = ((codes[:,None] >> (2*np.arange(9))) & 3).astype(np.uint8).reshape(-1,3,3)
    def determinant(m):
        result = np.zeros(m.shape[:-2], dtype=np.uint8)
        for p in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)):
            result ^= field[field[m[...,0,p[0]],m[...,1,p[1]]],m[...,2,p[2]]]
        return result
    sl = matrices[determinant(matrices)==1]
    assert len(sl) == 60480
    hyperoval = np.array([[1,t,int(field[t,t])] for t in range(4)] + [[0,0,1],[0,1,0]],dtype=np.uint8)
    assert all(determinant(hyperoval[list(c)].T) != 0 for c in combinations(range(6),3))
    def canonical(v):
        out = v.copy(); first = np.argmax(v!=0, axis=-1)
        scale = inverse[np.take_along_axis(v,first[...,None],axis=-1)[...,0]]
        assert np.all(scale)
        return field[out,scale[...,None]]
    def vector_codes(v):
        return np.asarray(v,dtype=np.int64)@np.array([1,4,16])
    point_index = np.full(64,-1,dtype=np.int16)
    point_index[vector_codes(hyperoval)] = np.arange(6)
    images = np.zeros((len(sl),6,3),dtype=np.uint8)
    for k in range(3):
        images ^= field[sl[:,None,:,k],hyperoval[None,:,k,None]]
    permutations = point_index[vector_codes(canonical(images))]
    retain = np.all(permutations>=0,axis=1)
    cover = sl[retain]; action = permutations[retain]
    assert len(cover) == 1080 and action.shape == (1080,6)
    enc = lambda a: np.asarray(a,dtype=np.int64).reshape(a.shape[:-2]+(9,))@(4**np.arange(9))
    lookup = np.full(4**9,-1,dtype=np.int32)
    lookup[enc(cover)] = np.arange(1080)
    one = int(lookup[enc(np.eye(3,dtype=np.uint8))])
    z = int(lookup[enc(2*np.eye(3,dtype=np.uint8))])
    z2 = int(lookup[enc(3*np.eye(3,dtype=np.uint8))])
    prod = np.zeros((1080,1080,3,3),dtype=np.uint8)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                prod[:,:,i,j] ^= field[cover[:,None,i,k],cover[None,:,k,j]]
    multiplication = lookup[enc(prod)].astype(np.int16)
    assert np.all(multiplication>=0)
    inv = np.argmax(multiplication==one,axis=1).astype(np.int16)
    assert np.all(multiplication[np.arange(1080),inv]==one)
    assert np.all(multiplication[inv,np.arange(1080)]==one)
    assert multiplication[z,z] == z2 and multiplication[z,z2] == one
    old_index = {tuple(p):i for i,p in enumerate(old['A6_elements'])}
    quotient = np.array([old_index[tuple(p)] for p in action],dtype=np.int16)
    assert len(set(map(int,quotient))) == 360
    assert all(np.count_nonzero(quotient==j)==3 for j in range(360))
    assert np.array_equal(quotient[multiplication],
                          old['A6_multiplication'][quotient[:,None],quotient[None,:]])
    section = np.array([int(np.flatnonzero(quotient==j)[0]) for j in range(360)],dtype=np.int16)
    autone = int(old['Aut_one']); base = old['Aut_generator_pairs'][autone]
    generators = section[base]
    parent = np.full(1080,-1,dtype=np.int16); letter = np.full(1080,-1,dtype=np.int8)
    parent[one] = one; order = [one]; ab = np.zeros((1080,2),dtype=np.int8)
    for v in order:
        for j,g in enumerate(generators):
            w = int(multiplication[v,g])
            if parent[w]<0:
                parent[w]=v;letter[w]=j;ab[w]=ab[v];ab[w,j]=(ab[w,j]+1)%3;order.append(w)
    assert len(order)==1080
    centre = np.flatnonzero(np.all(multiplication[:,generators]==multiplication[generators,:].T,axis=1))
    assert set(map(int,centre)) == {one,z,z2}
    a,b = map(int,generators)
    comm = int(multiplication[multiplication[multiplication[a,b],inv[a]],inv[b]])
    conjugates = multiplication[multiplication[:,comm],inv]
    chosen = {}; 
    for g,v in enumerate(conjugates):
        chosen.setdefault(int(v),g)
    cg = sorted(chosen); dp = np.full(1080,-1,dtype=np.int16); dl=np.full(1080,-1,dtype=np.int16)
    dp[one]=one; todo=[one]
    for v in todo:
        for j,g in enumerate(cg):
            w=int(multiplication[v,g])
            if dp[w]<0:
                dp[w]=v;dl[w]=j;todo.append(w)
    assert len(todo)==1080
    def original_word(v):
        out=[]
        while v!=one:
            out.append(int(letter[v])+1);v=int(parent[v])
        return out[::-1]
    factors=[];v=z
    while v!=one:
        factors.append(chosen[cg[int(dl[v])]]);v=int(dp[v])
    central_word=[]
    for g in factors[::-1]:
        w=original_word(g)
        central_word += w+[1,2,-1,-2]+[-j for j in w[::-1]]
    value=one
    for j in central_word:
        value=int(multiplication[value,generators[j-1] if j>0 else inv[generators[-j-1]]])
    assert value==z
    assert all(sum((j==i)-(j==-i) for j in central_word)==0 for i in (1,2))
    print('Exact matrix cover, quotient and perfectness PASS; constructing every automorphism lift.',flush=True)

    # Cayley-graph relators retain every central correction to generator lifts.
    zlog = np.full(1080,-1,dtype=np.int8);zlog[[one,z,z2]]=np.arange(3)
    targets = multiplication[:,generators]
    D=np.empty((1080,2,2),dtype=np.int8)
    for j in range(2):
        unit=np.zeros(2,dtype=np.int8);unit[j]=1
        D[:,j]=(ab+unit-ab[targets[:,j]])%3
    D=D.reshape(-1,2)
    first=next(i for i,row in enumerate(D) if np.any(row));second=next(i for i,row in enumerate(D)
        if (int(D[first,0])*int(row[1])-int(D[first,1])*int(row[0]))%3)
    A=D[[first,second]].astype(np.int64);det=int(A[0,0]*A[1,1]-A[0,1]*A[1,0])%3
    Ainv=np.array([[A[1,1],-A[0,1]],[-A[1,0],A[0,0]]])*pow(det,-1,3)%3
    assert np.array_equal(A@Ainv%3,np.eye(2,dtype=np.int64))
    lifted_generators=section[old['Aut_generator_pairs']]
    candidate=np.empty((1440,1080),dtype=np.int16);candidate[:,one]=one
    for v in order[1:]:
        candidate[:,v]=multiplication[candidate[:,parent[v]],lifted_generators[:,letter[v]]]
    defects=np.empty((1440,1080,2),dtype=np.int8)
    for j in range(2):
        residual=multiplication[multiplication[candidate,lifted_generators[:,j,None]],inv[candidate[:,targets[:,j]]]]
        defects[:,:,j]=zlog[residual]
    assert np.all(defects>=0)
    defects=defects.reshape(1440,-1)
    shifts=(-defects[:,[first,second]].astype(np.int64)@Ainv.T)%3
    assert not np.any((defects+shifts@D.T)%3)
    twists=shifts@ab.T%3;zpower=np.array([one,z,z2],dtype=np.int16)
    automorphisms=multiplication[zpower[twists],candidate]
    assert np.array_equal(np.sort(automorphisms,axis=1),np.tile(np.arange(1080),(1440,1)))
    assert np.array_equal(quotient[automorphisms],old['Aut_maps'][:,quotient])
    for j,g in enumerate(generators):
        assert np.array_equal(automorphisms[:,multiplication[:,g]],
                              multiplication[automorphisms,automorphisms[:,g,None]])
    for i in range(1440):
        assert np.array_equal(automorphisms[old['Aut_multiplication'][i]][:,generators],
                              automorphisms[i,automorphisms[:,generators]])
    character=zlog[automorphisms[:,z]]
    assert set(map(int,character))=={1,2}
    assert np.array_equal(character[old['Aut_multiplication']],character[:,None]*character[None,:]%3)
    profile={}
    for k in range(4):
        values=set(map(int,character[old['Aut_outer_coordinates']==k]));assert len(values)==1
        profile[str(k)]=values.pop()
    assert profile['0']==1
    result={
        'status':'PASS_EXACT_CENTRAL_THREE_A6_COVER',
        'field_definition':'F2[t]/(t^2+t+1); codes0,1,t,t+1',
        'all_3x3_matrices_tested':4**9,'full_SL3_F4_order':60480,
        'hyperoval_points':hyperoval.tolist(),'all_twenty_triple_determinants_nonzero':True,
        'exact_determinant_one_hyperoval_stabilizer_order':1080,
        'specified_six_point_quotient_order':360,'central_kernel_order':3,
        'full_centre_exactly_scalar_matrices':True,'two_original_generators_generate_full_cover':True,
        'derived_normal_closure_order':1080,'cover_is_perfect':True,
        'original_cover_generator_indices':generators.tolist(),
        'original_A6_generator_indices':base.tolist(),
        'central_generator_index':z,'central_generator_matrix':cover[z].tolist(),
        'literal_central_commutator_word':central_word,
        'all_1440_A6_automorphisms_lifted':True,
        'complete_automorphism_Cayley_edge_checks':1440*1080*2,
        'all_1440_squared_compositions_checked_on_both_generators':True,
        'centre_action_by_exact_outer_V4_coordinate':profile,
        'all_generator_central_shifts_retained':True,
        'selected_two_relator_rows':[first,second],
        'selected_exponent_matrix_mod3':A.tolist(),
        'source_sha256':{'de_ferrari_a6_kernels.npz':digest},
        'no_Ferrari_fibre_lift_claim_in_this_model':True,
        'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/(STEM+'.npz'),field_multiplication=field,cover_matrices=cover,
        cover_multiplication=multiplication,cover_inverse=inv,cover_one=np.array(one),
        cover_central_generator=np.array(z),actual_six_point_action=action,A6_quotient=quotient,
        A6_section=section,cover_generators=generators,source_Cayley_parent=parent,
        source_Cayley_letter=letter,source_Cayley_abelianization_mod3=ab,
        all_lifted_automorphisms=automorphisms,automorphism_central_character=character,
        all_automorphism_generator_central_shifts=shifts,
        full_Cayley_relator_exponent_matrix_mod3=D)
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    assert sha256(old_path.read_bytes()).hexdigest()==digest
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':
    main()
