#!/usr/bin/env python3
"""Complete base centralizer calculation and actual lifts in the return cover."""
from collections import deque
from hashlib import sha256
from pathlib import Path
import argparse
import json
import time
import numpy as np
from bc_return_prime_model import ReturnModel,Element,Span,rank_mod

HERE = Path(__file__).resolve().parent


def solve_mod(a,b,p):
    a = np.asarray(a,dtype=np.int64)%p
    b = np.asarray(b,dtype=np.int64).reshape(a.shape[0],-1)%p
    aug = np.hstack([a,b]).copy()
    r,pivots = 0,[]
    for c in range(a.shape[1]):
        nz = np.flatnonzero(aug[r:,c])
        if not len(nz):
            continue
        j = r+int(nz[0]); aug[[r,j]] = aug[[j,r]]
        aug[r] = aug[r]*pow(int(aug[r,c]),-1,p)%p
        ids = np.flatnonzero(aug[:,c]); ids = ids[ids != r]
        if len(ids):
            aug[ids] = (aug[ids]-aug[ids,c,None]*aug[r])%p
        pivots.append(c); r += 1
        if r == a.shape[0]:
            break
    if aug[r:,a.shape[1]:].any():
        return None,None
    particular = np.zeros((a.shape[1],b.shape[1]),dtype=np.int64)
    for i,c in enumerate(pivots):
        particular[c] = aug[i,a.shape[1]:]
    free = [j for j in range(a.shape[1]) if j not in pivots]
    kernel = np.zeros((a.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        kernel[j,k] = 1
        for i,c in enumerate(pivots):
            kernel[c,k] = -aug[i,j]%p
    assert np.array_equal(a@particular%p,b)
    assert not (a@kernel%p).any()
    return particular,kernel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ell',type=int,default=5)
    parser.add_argument('--prime',type=int,default=7)
    args = parser.parse_args()
    start = time.time()
    m = ReturnModel(args.ell,args.prime)
    ell,p,d = m.ell,m.p,m.dim
    stem = f'bc_return_prime_l{ell}_p{p}_centralizers'
    model_stem = f'bc_return_prime_l{ell}_p{p}'
    old = json.loads((HERE/(model_stem+'.json')).read_text())
    old_npz = np.load(HERE/(model_stem+'.npz'))
    wbasis = old_npz['kernel_word_vectors']
    winv,_ = solve_mod(wbasis.T,np.eye(d,dtype=np.int64),ell)
    assert winv is not None
    def topkey(a):
        return tuple(a.perm)+tuple(a.c)
    def topone(a):
        return topkey(a) == topkey(m.one)
    def comm(a,b):
        return m.mul(m.mul(m.mul(a,b),m.inverse(a)),m.inverse(b))
    def paction(a):
        mat = np.zeros((6*ell,6*ell),dtype=np.int64)
        for i,j in enumerate(a.perm):
            for h in range(ell):
                mat[i*ell+h,int(j)*ell+(h-int(a.c[i]))%ell] = 1
        return mat
    # The entire finite quotient over the p-translation kernel is enumerated.
    reps = {topkey(m.one):([],m.one)}
    todo = deque(reps)
    while todo:
        key = todo.popleft()
        w,g = reps[key]
        for b in (0,1):
            h = m.mul(g,m.letters[b]); kh = topkey(h)
            if kh not in reps:
                reps[kh] = (w+[b],h); todo.append(kh)
    assert len(reps) == 6*ell**2
    pspan = Span(6*ell,p)
    schreier_count = 0
    for w,g in reps.values():
        for b in (0,1):
            h = m.mul(g,m.letters[b])
            v,t = reps[topkey(h)]
            rel = m.mul(h,m.inverse(t))
            assert topone(rel)
            word = w+[b]+m.data['binv'](v)
            if pspan.add(rel.n.reshape(-1),word):
                assert np.array_equal(m.word(word).n,rel.n)
            schreier_count += 1
    pbasis = np.array(pspan.originals,dtype=np.int64).T
    k = len(pspan)
    # Closure is independently checked against both literal source letters.
    for a in (m.letters[0],m.letters[1]):
        assert rank_mod(np.hstack([pbasis,paction(a)@pbasis%p]),p) == k
    assert k == 3*(ell-1)+2
    def pword(coeff):
        w = []
        for a,bw in zip(coeff,pspan.labels):
            w += bw*int(a)
        return w
    records,all_wcorrections = [],[]
    elements = [('s',m.letters[0]),('r',m.letters[1]),('tau',m.mul(m.letters[0],m.letters[1]))]
    for name,t in elements:
        pt = paction(t)
        equations = (np.eye(6*ell,dtype=np.int64)-pt)@pbasis%p
        zero,kernel = solve_mod(equations,np.zeros(6*ell,dtype=np.int64),p)
        assert zero is not None
        generators = []
        for j in range(kernel.shape[1]):
            w = pword(kernel[:,j]); h = m.word(w)
            assert topone(h)
            assert np.array_equal(h.n.reshape(-1),pbasis@kernel[:,j]%p)
            generators.append((w,h,{'kind':'p_kernel','index':j}))
        top_centralizers,base_centralizers = 0,0
        for w,g in reps.values():
            defect = comm(g,t)
            if not topone(defect):
                continue
            top_centralizers += 1
            sol,_ = solve_mod(equations,-defect.n.reshape(-1)%p,p)
            if sol is None:
                continue
            base_centralizers += 1
            correction_word = pword(sol[:,0])
            h = m.mul(m.word(correction_word),g)
            hh = comm(h,t)
            assert m.in_kernel(hh)
            generators.append((correction_word+w,h,{'kind':'top_coset','top_word':w,'p_coefficients':sol[:,0].tolist()}))
        A = m.action(t)
        centralizer_records = []
        for word,g,label in generators:
            defect = comm(g,t)
            assert m.in_kernel(defect)
            sol,_ = solve_mod(np.eye(d,dtype=np.int64)-A,-defect.v.reshape(-1)%ell,ell)
            assert sol is not None, (ell,p,name,label)
            v = sol[:,0]
            w = Element(m.one.perm,m.one.c,m.one.n,v.reshape(6,ell,m.f))
            lift = m.mul(w,g)
            assert m.equal(comm(lift,t),m.one)
            preimage = winv@v%ell
            assert np.array_equal(wbasis.T@preimage%ell,v)
            centralizer_records.append({'base_B_word':word,'base_label':label,
                                        'kernel_word_coefficients':preimage.tolist()})
            all_wcorrections.append(v)
        dimfixed = d-rank_mod(A-np.eye(d,dtype=np.int64),ell)
        records.append({'element':name,'top_centralizer_count':top_centralizers,
                        'top_cosets_with_base_centralizer_lift':base_centralizers,
                        'base_p_centralizer_dimension':kernel.shape[1],
                        'base_centralizer_order':str(base_centralizers*p**kernel.shape[1]),
                        'upper_kernel_centralizer_dimension':dimfixed,
                        'upper_to_base_centralizer_index':1,
                        'complete_base_centralizer_generators':centralizer_records})
    result = {'status':'PASS_COMPLETE_RETURN_PRIME_CENTRALIZER_UNION',
              'ell':ell,'prime':p,'field_degree':m.f,
              'actual_top_quotient_order':len(reps),'complete_Schreier_edge_count':schreier_count,
              'actual_base_p_kernel_rank':k,
              'actual_base_order':str(len(reps)*p**k),
              'p_kernel_basis_B_words':pspan.labels,
              'centralizers':records,
              'all_centralizer_lifts_verified_in_actual_induced_source':True,
              'all_lift_corrections_have_saved_literal_word_preimages':True,
              'full_ordinary_peripheral_fibre_count':str(ell**d),
              'full_ordinary_kernel_orbit_count':1,
              'tau_normalized_fibre_count':str(ell**(d//6)),
              'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in
                              ('bc_return_prime_model.py',model_stem+'.json',model_stem+'.npz')},
              'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/(stem+'.npz'),p_kernel_basis=pbasis,
                        centralizer_lift_corrections=np.array(all_wcorrections))
    (HERE/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    brief = {k:v for k,v in result.items() if k not in ('p_kernel_basis_B_words','centralizers')}
    brief['centralizers'] = [{k:v for k,v in r.items() if k != 'complete_base_centralizer_generators'} for r in records]
    print(json.dumps(brief,indent=2))


if __name__ == '__main__':
    main()
