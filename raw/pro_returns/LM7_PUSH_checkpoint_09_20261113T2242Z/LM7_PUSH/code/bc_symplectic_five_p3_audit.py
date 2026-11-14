#!/usr/bin/env python3
"""Independent exact audit of the root's prime-three five-strand model.

The target order is obtained by exhaustive 4-by-4 matrix enumeration,
without a generic permutation-group order routine.  The complete source
order is certified by its 81-element N image and 576 disjoint Schreier
cosets.  Every saved array, compression intertwiner, and conjugator is
checked; all original inputs remain read only.
"""
from pathlib import Path
from collections import Counter,deque
from itertools import product
from hashlib import sha256
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
import de_ferrari_class2_model as E18

HERE=Path(__file__).resolve().parent

def inverse_matrix(a):
    a=np.asarray(a,dtype=np.int64).copy()%3;inv=np.eye(4,dtype=np.int64)
    for j in range(4):
        k=j+int(np.flatnonzero(a[j:,j])[0])
        a[[j,k]]=a[[k,j]];inv[[j,k]]=inv[[k,j]]
        scale=int(a[j,j]);a[j]=a[j]*scale%3;inv[j]=inv[j]*scale%3
        c=a[:,j].copy();c[j]=0
        a=(a-c[:,None]*a[j][None,:])%3
        inv=(inv-c[:,None]*inv[j][None,:])%3
    assert np.array_equal(a,np.eye(4,dtype=np.int64))
    return inv

def key(a):return np.asarray(a,dtype=np.uint8).tobytes()
def mul(a,b):return np.matmul(b,a)%3  # the specified right permutation convention
def mpower(a,n):
    if n<0:return mpower(inverse_matrix(a),-n)
    ans=np.eye(4,dtype=np.int64)
    while n:
        if n&1:ans=mul(ans,a)
        a=mul(a,a);n//=2
    return ans
def invword(w):return [-a for a in reversed(w)]
def mword(w,letters):
    ans=np.eye(4,dtype=np.int64)
    for a in w:ans=mul(ans,letters[a])
    return ans
def permword(w,letters):
    ans=np.arange(len(letters[0]),dtype=np.int64)
    for a in w:ans=letters[a][ans]
    return ans

def main():
    started=time.time()
    protected_paths=sorted(set(
        list(HERE.glob('e_symplectic_five*p3*root*.npz'))+
        list(HERE.glob('e_symplectic_five*p3*root*.json'))+
        list(HERE.glob('e_symplectic_five*p3*root*.out'))+
        [HERE/n for n in ('e_symplectic_five_model_root.py','e_symplectic_five_source_root.py',
            'e_symplectic_five_subgroups_root.py','e_symplectic_five_p3_fibres_root.py',
            'e_hurwitz_five_source_root.py','de_ferrari_a6_source_data.py',
            'de_ferrari_class2_model.py','de_ferrari_fibres.json','de_ferrari_two_lift.json',
            'de_ferrari_degree6_kernel.json','de_ferrari_two_degree6_module.json')]))
    hashes={p.name:sha256(p.read_bytes()).hexdigest()for p in protected_paths}
    saved=np.load(HERE/'e_symplectic_five_p3_model_root.npz')
    J=np.zeros((4,4),dtype=np.int64)
    for i in range(3):J[i,i+1]=1;J[i+1,i]=-1
    A=np.stack([np.eye(4,dtype=np.int64)+np.outer(np.eye(4,dtype=np.int64)[i],J[i])
                for i in range(4)])%3
    points=np.array([v for v in product(range(3),repeat=4)if any(v)],dtype=np.int64)
    def to_perm(a):
        images=points@a.T%3
        return images@np.array([27,9,3,1],dtype=np.int64)-1
    assert np.array_equal(J,saved['J'])and np.array_equal(A,saved['matrices'])
    assert np.array_equal(points,saved['points'])
    assert all(np.array_equal(a.T@J@a%3,J%3)for a in A)
    sigma=np.stack([to_perm(a)for a in A]);assert np.array_equal(sigma,saved['sigma'])
    letters={i+1:a for i,a in enumerate(A)}
    letters.update({-i-1:inverse_matrix(a)for i,a in enumerate(A)})
    one=np.eye(4,dtype=np.int64)
    for i in range(1,4):
        assert np.array_equal(mword([i,i+1,i],letters),mword([i+1,i,i+1],letters))
    for i in range(1,5):
        assert np.array_equal(mpower(letters[i],3),one)
        for j in range(i+2,5):assert np.array_equal(mword([i,j],letters),mword([j,i],letters))
    # Exhaustive generated matrix group, also retaining actual word preimages.
    matrices=[one];indices={key(one):0};parents=[-1];last=[0]
    for at,a in enumerate(matrices):
        for j,b in enumerate(A):
            c=mul(a,b);k=key(c)
            if k not in indices:
                indices[k]=len(matrices);matrices.append(c);parents.append(at);last.append(j+1)
    assert len(matrices)==80*27*8*3==51840
    def literal_matrix_word(a):
        at=indices[key(a)];w=[]
        while parents[at]>=0:w.append(last[at]);at=parents[at]
        w.reverse();assert np.array_equal(mword(w,letters),a);return w
    delta=mword([1,2,3,4],letters);epsilon=mword([1,1,2,3,4],letters)
    assert np.array_equal(mpower(delta,5),-one%3)
    assert np.array_equal(mpower(epsilon,4),-one%3)
    assert np.array_equal(to_perm(delta),saved['delta'])
    assert np.array_equal(to_perm(epsilon),saved['epsilon'])
    pure={}
    for i in range(1,5):
        for j in range(i+1,6):
            h=list(range(j-1,i,-1));pure[i,j]=mword(h+[i,i]+invword(h),letters)
    p=lambda i,j:pure[i,j]
    pairs=[(p(1,2),mul(p(2,3),p(2,4))),(mul(p(1,3),p(2,3)),p(3,4)),
           (p(2,3),p(3,4)),(mul(p(1,2),p(1,3)),mul(p(2,4),p(3,4))),
           (p(1,2),p(2,3))]
    for i in range(2,5):
        pairs.append((mword(list(range(i-1,0,-1))+list(range(1,i)),letters),mpower(A[i-1],2)))
    X=np.stack([a for a,b in pairs]);Y=np.stack([b for a,b in pairs])
    assert np.array_equal(np.stack([to_perm(a)for a in X]),saved['x'])
    assert np.array_equal(np.stack([to_perm(a)for a in Y]),saved['y'])
    fl={1:X,2:Y,-1:np.stack([inverse_matrix(a)for a in X]),-2:np.stack([inverse_matrix(a)for a in Y])}
    def fword(w):
        ans=np.broadcast_to(one,(8,4,4)).copy()
        for a in w:ans=np.matmul(fl[a],ans)%3
        return ans
    # Reconstruct all six induced cosets directly, independently of Source.
    d=load_data();Q=sorted(d['Q2']);index={q:i for i,q in enumerate(Q)}
    section={d['unit']:[]};pending=deque(section)
    while pending:
        q=pending.popleft()
        for a,g in ((0,d['s2']),(1,d['r2'])):
            qn=d['mul2'](q,g)
            if qn not in section:section[qn]=section[q]+[a];pending.append(qn)
    source_letters={}
    for a,g in ((0,d['s2']),(1,d['r2'])):
        blocks=[]
        for q in Q:
            qn=d['mul2'](q,g);word=section[q]+[a]+d['binv'](section[qn])
            values=fword(d['fword'](word))
            for i,value in enumerate(values):blocks.append(80*(8*index[qn]+i)+to_perm(value))
        source_letters[a]=np.concatenate(blocks)
    raw=np.load(HERE/'e_symplectic_five_p3_source_root_generators.npz')
    assert np.array_equal(source_letters[0],raw['s'])and np.array_equal(source_letters[1],raw['r'])
    metadata=json.loads((HERE/'e_symplectic_five_p3_source_root.json').read_text())
    reps=metadata['retained_original_canonical_orders'];new=[[],[]];offset=0
    for order in reps:
        inverse={v:i for i,v in enumerate(order)}
        for j,a in enumerate((0,1)):new[j].extend(offset+inverse[int(source_letters[a][v])]for v in order)
        offset+=len(order)
    covered=[]
    for rec in metadata['orbit_correspondences']:
        old=rec['original_canonical_order'];rep=reps[rec['retained_orbit_index']]
        assert len(old)==len(rep);mapping=dict(zip(old,rep));covered.extend(old)
        for a in (0,1):
            assert all(mapping[int(source_letters[a][v])]==int(source_letters[a][mapping[v]])for v in old)
    assert sorted(covered)==list(range(3840))and len(new[0])==558
    compressed=np.load(HERE/'e_symplectic_five_p3_source_root_compressed.npz')
    s,r=np.asarray(new,dtype=np.int64)
    assert np.array_equal(s,compressed['s'])and np.array_equal(r,compressed['r'])
    bl={0:s,1:r,-1:r[r]};ident=np.arange(len(s),dtype=np.int64)
    assert np.array_equal(s[s],ident)and np.array_equal(r[r[r]],ident)
    ngens=np.stack([permword(w,bl)for w in d['Nwords']])
    subgroup=np.load(HERE/'e_symplectic_five_p3_subgroups_root.npz')
    assert np.array_equal(ngens,subgroup['N_images'])
    assert all(np.array_equal(g[g[g]],ident)for g in ngens)
    assert all(np.array_equal(g[h],h[g])for g in ngens for h in ngens)
    nvalues=[ident];nkeys={ident.astype(np.uint16).tobytes()};basis_indices=[]
    for no,g in enumerate(ngens):
        if g.astype(np.uint16).tobytes()in nkeys:continue
        basis_indices.append(no);powers=[ident,g,g[g]]
        nvalues=[p[h]for p in powers for h in nvalues]
        nkeys={a.astype(np.uint16).tobytes()for a in nvalues}
        assert len(nkeys)==len(nvalues)==3**len(basis_indices)
    assert len(nvalues)==81 and len(basis_indices)==4
    # Certify the complete source by 576 disjoint N cosets and their edges.
    path={q:permword(d['Bpaths'][q],bl)for q in d['Q']}
    invpath={q:np.argsort(a)for q,a in path.items()}
    allkeys=set()
    for q,a in path.items():
        for n in nvalues:allkeys.add(a[n].astype(np.uint16).tobytes())
        for letter,g in ((0,d['ss']),(1,d['rr'])):
            qn=d['times'](q,g)
            residue=invpath[qn][bl[letter][a]]
            assert residue.astype(np.uint16).tobytes()in nkeys
    assert len(allkeys)==81*576==46656
    del allkeys
    # The literal E18 map, with all 648*3 edges and all images retained.
    old_images={E18.one:one};queue=[E18.one]
    for old in queue:
        for a,b in zip((E18.a,E18.b,E18.c),A[:3]):
            nxt=E18.mul(old,a);value=mul(old_images[old],b)
            if nxt in old_images:assert np.array_equal(old_images[nxt],value)
            else:old_images[nxt]=value;queue.append(nxt)
    assert len(queue)==len({key(v)for v in old_images.values()})==648
    fibres=np.load(HERE/'e_symplectic_five_p3_fibres_root.npz')
    assert np.array_equal(np.array(queue),fibres['E18_elements'])
    assert np.array_equal(np.stack([to_perm(old_images[a])for a in queue]),fibres['E18_images'])
    rows=json.loads((HERE/'de_ferrari_two_lift.json').read_text())['records']
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    ternary=json.loads((HERE/'de_ferrari_degree6_kernel.json').read_text())['F_prime_basis_words']
    binary=json.loads((HERE/'de_ferrari_two_degree6_module.json').read_text())['F_prime_basis_words']
    assert len(ternary)==6 and len(binary)==7
    killed=[v['chosen_witness']['literal_B_old_correction_word']for v in rows]+ternary+binary
    assert all(np.array_equal(permword(w,bl),ident)for w in killed)
    root_fibres=json.loads((HERE/'e_symplectic_five_p3_fibres_root.json').read_text())
    simultaneous=[];array_values=[];periodic_checks=0
    for no,rec in enumerate(origins):
        values=fword(rec['actual_commutator_word_f'])
        arrays=np.stack([to_perm(a)for a in values]);array_values.append(arrays)
        assert np.array_equal(mul(values[0],values[1]),mul(mul(values[2],values[3]),values[4]))
        changed=[A[0]]+[mul(mul(inverse_matrix(values[i+4]),A[i]),values[i+4])for i in range(1,4)]
        # A direct global inner comparison strengthens the order check.
        vectors=np.column_stack([one[:,0]]+[values[i+4][:,i]for i in range(1,4)])%3
        gram=vectors.T@J@vectors%3;signs=[1]
        for i in range(3):
            assert int(gram[i,i+1])in (1,2)
            signs.append(signs[-1]*int(gram[i,i+1])%3)
        P=vectors*np.array(signs)[None,:]%3
        assert np.array_equal(P.T@J@P%3,J%3)
        assert all(np.array_equal(v,P@a@inverse_matrix(P)%3)for a,v in zip(A,changed))
        word=literal_matrix_word(P)
        nd=one.copy()
        for a in changed:nd=mul(nd,a)
        ne=mul(changed[0],nd)
        assert np.array_equal(mpower(nd,5),-one%3)and np.array_equal(mpower(ne,4),-one%3)
        for lam in (1,73):
            record=root_fibres['literal_periodic_conjugators'][str(lam)][no]
            for name,base,target in (('delta',delta,nd),('epsilon',epsilon,ne)):
                K=mword(record[name+'_conjugator_word'],letters)
                assert np.array_equal(K@mpower(base,lam)@inverse_matrix(K)%3,target)
                periodic_checks+=1
        cg=d['bpower'](d['xword'],rec['integral_cusp_gauge']);beta=rec['base_beta_word_B']
        baseword=[0]+cg+beta+[0]+d['binv'](beta)+d['binv'](cg)
        assert np.array_equal(permword(baseword,bl),permword(d['to_B'](rec['actual_commutator_word_f']),bl))
        simultaneous.append({'row':no,'matrix':P.tolist(),'literal_braid_word':word})
    assert np.array_equal(np.stack(array_values),fibres['all24_eight_evaluation_values'])
    distinct={key(np.array(v['matrix']))for v in simultaneous};assert len(distinct)==3
    assert all(sha256(p.read_bytes()).hexdigest()==hashes[p.name]for p in protected_paths)
    out={'status':'PASS_INDEPENDENT_SYMPLECTIC_P3_FIVE_STRAND_AUDIT',
         'target_order_by_exhaustive_matrix_enumeration':51840,
         'symplectic_basis_count':80*27*8*3,
         'complete_induced_source_degree':3840,'faithfully_compressed_degree':558,
         'all104_compression_intertwiners_checked':len(metadata['orbit_correspondences'])==104,
         'N_image_order':81,'N_basis_original_indices':basis_indices,
         'source_order_by_disjoint_cosets_and_1152_edges':46656,
         'all97_N_cubes_and9409_commutations_checked':True,
         'specified_E18_generator_edges_checked':648*3,
         'all24_eight_evaluation_arrays_identical':True,
         'all37_literal_correction_words_killed':len(killed)==37,
         'all864_values_follow_the_exact_literal_family_factorization':True,
         'all24_changed_quadruples_simultaneously_inner_conjugate':True,
         'number_of_distinct_simultaneous_conjugators':3,
         'simultaneous_conjugators':simultaneous,
         'literal_periodic_conjugacies_replayed':periodic_checks,
         'permutation_convention':'p*q=q[p]; a stored column matrix A corresponds to right row matrix A^t, or to A^(-1) in the usual column-group convention',
         'protected_originals_unchanged':True,'input_sha256':hashes,
         'seconds':round(time.time()-started,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(__file__).with_suffix('.npz'),
        simultaneous_matrices=np.array([v['matrix']for v in simultaneous]),
        independently_reconstructed_evaluation_arrays=np.stack(array_values),
        N_basis_images=ngens[basis_indices])
    print(json.dumps({k:v for k,v in out.items()if k not in ('input_sha256','simultaneous_conjugators')},indent=2))
    print('PASS: exact target/source maps, all arrays, full fibres, and literal simultaneous inner conjugators.')

if __name__=='__main__':main()
