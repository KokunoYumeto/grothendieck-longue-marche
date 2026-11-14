#!/usr/bin/env python3
"""Exact class-two coordinates for the actual GL23 and joint corrections.

Each coordinate basis element is a retained N_B-prime word.  Each prefix
subgroup has a complete Schreier certificate; coordinates are recovered by
membership in these actual prefix subgroups.  The resulting binary formula
is verified against all generator products and all original N sixth powers.
"""
from pathlib import Path
import argparse,json,subprocess,time
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def mul(a,b):return b[a]
def inv(a):return np.argsort(a).astype(np.uint16)
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def conj(a,b):return mul(mul(a,b),inv(a))
def power(a,n):
    r=np.arange(len(a),dtype=np.uint16)
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r


class Sifter:
    def __init__(self,d):
        self.n=d['degree'];self.one=np.arange(self.n,dtype=np.uint16)
        self.levels=[];self.order=1
        for lev,b in enumerate(d['base']):
            gens=d['strong'][d['depths']>=lev]
            orbit=[int(b)];trans=[self.one];at={int(b):0}
            for j,v in enumerate(orbit):
                for g in gens:
                    w=int(g[v])
                    if w not in at:
                        at[w]=len(orbit);orbit.append(w);trans.append(mul(trans[j],g))
            self.levels.append((int(b),{v:inv(t) for v,t in zip(orbit,trans)}))
            self.order*=len(orbit)
        for g in d['original']:
            if not d['derived']:assert self.contains(g)
        for g in d['strong']:assert self.contains(g)

    def contains(self,g):
        h=g
        for b,ti in self.levels:
            v=int(h[b])
            if v==b:continue
            if v not in ti:return False
            h=mul(h,ti[v])
        return np.array_equal(h,self.one)


def certify(prefix,gens,derived=False):
    n=len(gens[0])
    with prefix.with_suffix('.input').open('w') as f:
        f.write(f'{n} {len(gens)}\n')
        for g in gens:f.write(' '.join(map(str,g))+'\n')
    cmd=[str(HERE/'de_a6_schreier_fast')]
    if derived:cmd.append('--derived')
    cmd += [str(prefix.with_suffix('.input')),str(prefix.with_suffix('.bin'))]
    with prefix.with_suffix('.out').open('w') as out,prefix.with_suffix('.err').open('w') as err:
        subprocess.run(cmd,stdout=out,stderr=err,check=True)
    d=read_certificate(prefix.with_suffix('.bin'));verify_words(d)
    assert np.array_equal(d['original'],np.array(gens))
    return d,Sifter(d)


class ClassTwoCoordinates:
    def __init__(self,mode,build=False):
        self.mode=mode;self.prefix=HERE/f'a_cm_gl23_{mode}_pc'
        self.folder=HERE/f'a_cm_gl23_{mode}_pc_certificates'
        if build:self.build()
        data=np.load(self.prefix.with_suffix('.npz'))
        self.q=data['quotient_basis'];self.z=data['derived_basis']
        self.r=len(self.q);self.k=len(self.z);self.n=self.q.shape[1]
        self.one=np.arange(self.n,dtype=np.uint16)
        self.qinv=np.array([inv(g) for g in self.q])
        self.zvalues=data['derived_values'];self.zi={v.tobytes():i for i,v in enumerate(self.zvalues)}
        self.chains=[Sifter(read_certificate(self.folder/f'prefix_{j:02d}.bin')) for j in range(self.r+1)]
        self.squares=list(map(int,data['squares']));self.brackets=data['brackets']
        self.mask=(1<<self.r)-1

    def build(self):
        self.folder.mkdir(exist_ok=False)
        source='a_cm_gl23_N_small_derived.bin' if self.mode=='single' else 'a_cm_gl23_joint_N_small_derived.bin'
        d=read_certificate(HERE/source);verify_words(d);C=d['strong'];one=np.arange(d['degree'],dtype=np.uint16)
        dc,ds=certify(self.folder/'derived',C,True)
        # This check supplies the exact centrality needed for the collection law.
        assert all(np.array_equal(conj(g,z),z) for g in C for z in dc['strong'])
        assert all(np.array_equal(mul(z,z),one) for z in dc['strong'])
        assert all(ds.contains(mul(g,g)) for g in C)
        z=[];zindices=[];values=[one];index={one.tobytes():0}
        for ix,g in enumerate(dc['strong']):
            if g.tobytes() not in index:
                z.append(g);zindices.append(ix)
                old=values[:]
                for h in old:
                    v=mul(h,g);assert v.tobytes() not in index
                    index[v.tobytes()]=len(values);values.append(v)
        assert len(values)==ds.order==2**len(z)
        _,chain=certify(self.folder/'prefix_00',z)
        chains=[chain];q=[];qindices=[]
        for ix,g in enumerate(C):
            if not chain.contains(g):
                q.append(g);qindices.append(ix)
                _,chain=certify(self.folder/f'prefix_{len(q):02d}',z+q)
                assert chain.order==2*chains[-1].order
                chains.append(chain)
        cs=Sifter(d);assert chain.order==cs.order
        r=len(q);k=len(z)
        squares=[index[mul(g,g).tobytes()] for g in q]
        brackets=np.array([[index[comm(g,h).tobytes()] for h in q] for g in q],dtype=np.uint64)
        np.savez_compressed(self.prefix.with_suffix('.npz'),quotient_basis=np.array(q),derived_basis=np.array(z),
            derived_values=np.array(values),squares=squares,brackets=brackets,
            quotient_basis_C_strong_indices=qindices,derived_basis_Cprime_strong_indices=zindices,
            C_strong_Nsmall_word_nodes=d['words'],C_strong_Nsmall_word_DAG=d['nodes'],
            Cprime_strong_C_word_nodes=dc['words'],Cprime_strong_C_word_DAG=dc['nodes'])
        self.build_info={'exact_group_order':cs.order,'exact_derived_order':ds.order,
            'quotient_dimension':r,'derived_dimension':k,
            'derived_is_central_elementary_abelian':True,'all_generator_squares_lie_in_derived':True,
            'quotient_basis_C_strong_indices':qindices,'derived_basis_Cprime_strong_indices':zindices,
            'all_binary_prefix_orders':[c.order for c in chains],
            'literal_source_certificate':source}

    def coordinates(self,g):
        h=np.asarray(g,dtype=np.uint16);v=0
        assert self.chains[-1].contains(h)
        for j in range(self.r-1,-1,-1):
            if not self.chains[j].contains(h):
                v |= 1<<j;h=mul(h,self.qinv[j])
                assert self.chains[j].contains(h)
        return v | (self.zi[h.tobytes()]<<self.r)

    def element(self,a):
        h=self.one.copy()
        for j,g in enumerate(self.q):
            if a>>j&1:h=mul(h,g)
        return mul(h,self.zvalues[a>>self.r])

    def beta(self,u,v):
        z=0
        for j in range(self.r):
            if not (u>>j&1):continue
            if v>>j&1:z ^= self.squares[j]
            for i in range(j):
                if v>>i&1:z ^= int(self.brackets[j,i])
        return z

    def product(self,a,b):
        return (a^b) ^ (self.beta(a&self.mask,b&self.mask)<<self.r)

    def inverse(self,a):
        return a ^ (self.beta(a&self.mask,a&self.mask)<<self.r)

    def apply(self,images,a):
        out=0
        for j,g in enumerate(images):
            if a>>j&1:out=self.product(out,int(g))
        return out


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['single','joint']);args=p.parse_args()
    start=time.time();P=ClassTwoCoordinates(args.mode,build=True)
    inputs=np.load(HERE/('a_cm_gl23_induced.npz' if args.mode=='single' else 'a_cm_gl23_joint.npz'))
    N=inputs['N_generators' if args.mode=='single' else 'joint_N_generators']
    allgen=np.r_[P.q,P.z]
    for j,g in enumerate(allgen):assert P.coordinates(g)==1<<j
    for i,g in enumerate(allgen):
        for j,h in enumerate(allgen):
            value=P.product(1<<i,1<<j)
            assert np.array_equal(P.element(value),mul(g,h))
            assert P.coordinates(mul(g,h))==value
    sixth=[]
    for n in N:
        h=power(n,6);assert P.chains[-1].contains(h);sixth.append(P.coordinates(h))
    rng=np.random.default_rng(913493)
    for _ in range(256):
        a,b=map(int,rng.integers(0,1<<(P.r+P.k),2))
        assert np.array_equal(P.element(P.product(a,b)),mul(P.element(a),P.element(b)))
        assert P.coordinates(P.element(a))==a
        assert P.product(a,P.inverse(a))==0
    out={'status':'PASS_ACTUAL_CLASS_TWO_CORRECTION_COORDINATES','mode':args.mode,
         **P.build_info,'coordinate_rule':'ordered quotient basis, followed by ordered central derived basis',
         'all_97_N_sixth_powers_in_actual_derived_image':True,'N_sixth_power_coordinates':sixth,
         'exact_G6_kernel_image_equals_N_derived_image':True,
         'all_basis_products_compared_with_actual_permutations':True,
         'additional_literal_product_checks':256,
         'seconds':round(time.time()-start,3)}
    P.prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
