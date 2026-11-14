#!/usr/bin/env python3
"""Literal B extension, correction words, and the nilpotent comparison.

The old D23 maps are used as epimorphisms from B.  This program does
not assert invariance of their kernels under a proposed automorphism.
The accompanying common-source argument uses the actual N images.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_metabelian import Metabelian,rank,nullspace,rref
from de_ferrari_a6_abelian_compare import AbelianSource

HERE=Path(__file__).resolve().parent

class BMetabelian:
    """Elements (q,g) mean g times the saved literal B/F representative."""
    def __init__(self,M,d):
        self.M,self.d=M,d
        self.A=AbelianSource(d,120);self.table=self.A.table;self.e=self.A.e
        self.paths=self.A.paths;self.actions=[];self.xy=[];self.cocycle=[]
        for p in self.paths:
            action=M.I.copy()
            for letter in p:
                action=action@(M.S if letter==0 else M.R if letter==1 else M.R@M.R)%3
            self.actions.append(action)
            self.xy.append([M.word(d['fword'](p+w+d['binv'](p))) for w in (d['xword'],d['yword'])])
        for i,p in enumerate(self.paths):
            self.cocycle.append([M.word(d['fword'](p+r+d['binv'](self.paths[self.table[i,j]])))
                                 for j,r in enumerate(self.paths)])
        self.qinverse=[next(j for j in range(6) if self.table[i,j]==self.e) for i in range(6)]
        self.one=(self.e,M.one.copy())
        self.letters={a:self.literal([a]) for a in (0,1,-1)}
        self.s,self.r=self.letters[0],self.letters[1]
        assert self.equal(self.power(self.s,2),self.one)
        assert self.equal(self.power(self.r,3),self.one)
        for q in range(6):
            for r in range(6):
                qr=self.table[q,r];c=self.cocycle[q][r]
                for g in (M.x,M.y)+tuple(np.r_[0,0,M.I[:,j]] for j in range(9)):
                    assert np.array_equal(self.act(q,self.act(r,g)),M.conj(c,self.act(qr,g)))
                for t in range(6):
                    assert np.array_equal(M.mul(c,self.cocycle[qr][t]),
                        M.mul(self.act(q,self.cocycle[r][t]),self.cocycle[q][self.table[r,t]]))
    def act(self,q,g):
        M=self.M;x,y=self.xy[q]
        return M.mul(M.mul(M.power(x,int(g[0])),M.power(y,int(g[1]))),
                     np.r_[0,0,self.actions[q]@g[2:]%3])
    def mul(self,g,h):
        q,v=g;r,w=h
        return (int(self.table[q,r]),self.M.mul(self.M.mul(v,self.act(q,w)),self.cocycle[q][r]))
    def inv(self,g):
        q,v=g;r=self.qinverse[q]
        return (r,self.M.mul(self.M.inv(self.cocycle[r][q]),self.act(r,self.M.inv(v))))
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        h=self.one
        while n:
            if n&1:h=self.mul(h,g)
            g=self.mul(g,g);n//=2
        return h
    def equal(self,g,h):return g[0]==h[0] and np.array_equal(g[1],h[1])
    def literal(self,w):
        q=self.d['unit']
        for a in w:q=self.d['mul2'](q,self.d['s2'] if a==0 else self.d['r2'] if a==1 else self.d['r22'])
        j=self.A.qindex[q]
        return (j,self.M.word(self.d['fword'](w+self.d['binv'](self.paths[j]))))
    def word(self,w):
        g=self.one
        for a in w:g=self.mul(g,self.letters[a])
        return g

def correction_words(d):
    p=json.loads((HERE/'bc_cm_fermat_kernel_boundary.json').read_text())
    f=json.loads((HERE/'de_ferrari_a6_metafibres.json').read_text())
    basis=p['basis_F_prime_words_B'];out=[]
    for description in f['actual_correction_basis_descriptions']:
        rec=p['normal_relator_metadata'][description['relator_index']]
        # All six chosen independent relators are actual N commutators.
        assert rec['kind']=='N_commutator'
        i,j=rec['indices'];a,b=d['Nwords'][i],d['Nwords'][j]
        raw=a+b+d['binv'](a)+d['binv'](b)
        representative=[]
        for w,n in zip(basis,rec['image_coefficients']):representative+=d['bpower'](w,int(n))
        raw+=d['binv'](representative)
        conjugator=description['B_conjugator']
        raw=conjugator+raw+d['binv'](conjugator)
        # Squaring kills the whole binary K6 image.  It is a bijection
        # on the characteristic-three module image of these words.
        square=raw+raw
        out.append({'relator_index':description['relator_index'],
                    'B_conjugator':conjugator,'ternary_kernel_word_B':raw,
                    'D23_kernel_word_B':square,'D23_kernel_word_F':d['fword'](square)})
    return out

def main():
    start=time.time();M=Metabelian();d=load_data();B=BMetabelian(M,d)
    for w in d['Nwords']+[d['xword'],d['yword']]:assert B.equal(B.word(w),B.literal(w))
    words=correction_words(d);K=np.load(HERE/'de_ferrari_a6_metafibres.npz')['complete_correction_basis']
    for row,column in zip(words,K.T):
        g=M.word(row['D23_kernel_word_F']);assert not np.any(g[:2])
        assert np.array_equal(g[2:],column)
        assert all(sum(1 if a==j else -1 if a==-j else 0 for a in row['D23_kernel_word_F'])==0 for j in (1,2))
        row['module_value']=column.tolist()
    monomials=list(product(range(4),repeat=2))
    cyclic=np.column_stack([M.Xpow[i]@M.Ypow[j]@M.c%3 for i,j in monomials])
    annihilator=nullspace(cyclic);assert annihilator.shape==(16,7)
    assert not np.any(cyclic@annihilator%3)
    N=[M.word(d['fword'](w)) for w in d['Nwords']]
    commutators=np.column_stack([M.comm(N[i],N[j])[2:] for i in range(97) for j in range(i+1,97)])
    stable=np.c_[(M.Xpow[6]-M.I)@K,(M.Xpow[4]@M.Ypow[2]-M.I)@K]%3
    assert rank(K)==rank(commutators)==rank(np.c_[K,commutators])==6
    assert rank(stable)==rank(np.c_[stable,K])==6
    # Hence P'=[P,P']=... equals exactly the old-kernel image K.
    # The quotient P/K is abelian, and is the only possible common
    # N-quotient with the finite nilpotent old source.
    Hstable=np.c_[M.Xpow[3]-M.I,M.Ypow[3]-M.I]%3
    assert rank(Hstable)==9
    u=B.literal([-1,0]);v=B.literal([0,-1]);x=B.literal(d['xword']);y=B.literal(d['yword'])
    t=B.mul(B.s,B.r)
    assert B.equal(B.power(u,240),B.one)
    assert all(not B.equal(B.power(u,240//p),B.one) for p in (2,3,5))
    assert B.equal(B.power(u,2),x) and B.equal(B.power(v,2),y)
    candidates=json.loads((HERE/'de_ferrari_a6_metabelian.json').read_text())['complete_gentle_module_points']
    multipliers=[a for a in range(1,720,72) if a%5]
    checks=[]
    for lam in multipliers:
        U,V=B.power(u,lam),B.power(v,lam);m=(lam-1)//2
        for j,candidate in enumerate(candidates):
            fv=np.array(candidate['f_module_value'],dtype=np.int64);f=(B.e,np.r_[0,0,fv]);fi=B.inv(f)
            vp=B.mul(B.mul(fi,V),f);rp=B.mul(U,vp);sp=B.mul(rp,U)
            assert B.equal(B.power(sp,2),B.one) and B.equal(B.power(rp,3),B.one)
            assert B.equal(B.mul(sp,rp),B.power(t,lam))
            # The two actual B-hexagons, with the halved exponent retained.
            assert B.equal(rp,B.mul(B.mul(fi,B.r),B.power(x,-m)))
            assert B.equal(B.mul(vp,U),B.mul(B.mul(v,u),B.mul(B.power(y,-m),f)))
            xp,yp=B.power(U,2),B.power(vp,2)
            assert xp[0]==yp[0]==B.e
            cp=M.comm(xp[1],yp[1]);expected=(M.c+(M.X-M.I)@(M.Y-M.I)@fv)%3
            assert np.array_equal(cp,np.r_[0,0,expected])
            T=M.normalized_action(fv)
            assert not np.any((T@M.X-M.X@T)%3) and not np.any((T@M.Y-M.Y@T)%3)
            # Every defining cyclic-module relation is retained.
            image=np.column_stack([M.Xpow[a]@M.Ypow[b]@expected%3 for a,b in monomials])
            assert not np.any(image@annihilator%3)
            assert np.array_equal(M.power(xp[1],120),M.one) and np.array_equal(M.power(yp[1],120),M.one)
            assert candidate['surjective']==(rank(T)==9)
            checks.append([lam,j,rank(T)])
    assert len(checks)==8*27
    sizes=[len(row['D23_kernel_word_B']) for row in words]
    output={'status':'PASS','actual_B_quotient_order':6*120**2*3**9,
        'complete_nonabelian_extension_cocycle_checks':216,
        'literal_correction_words':words,'correction_word_lengths_B':sizes,
        'module_annihilator_monomials':[list(x) for x in monomials],
        'module_annihilator_basis':annihilator.tolist(),
        'complete_N_commutator_count':4656,'N_derived_image_rank':6,
        'N_stable_lower_central_image_rank':6,'N_stable_image_equals_D23_kernel_image':True,
        'N_image_mod_stable_commutator_is_abelian':True,'N_abelian_quotient_order':32400,
        'H_stable_commutator_image_rank':9,'actual_cusp_order':240,
        'all_compatible_joint_multiplier_residues_mod720':multipliers,
        'complete_hexagon_and_pure_endomorphism_checks':checks,
        'generation_argument':'The actual joint N image modulo its stable F3^6 factor is nilpotent. Its mod2 and mod3 Frattini quotients are the full N-ab modp quotients retained by D23; its mod5 quotient is the ordinary exponent C5^2. The saved old maps have rank97,97 and the new exponent map is multiplication by a unit.',
        'no_D23_kernel_invariance_assumed':True,
        'scope':'Only the actual metabelian A6 source quotient; not yet the full A6 target.',
        'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_metageneration.json').write_text(json.dumps(output,indent=2)+'\n')
    np.savez_compressed(HERE/'de_ferrari_a6_metageneration.npz',annihilator=annihilator,
        N_commutator_values=commutators,N_stable_commutator_values=stable,
        B_extension_actions=np.array(B.actions),B_extension_cocycle=np.array(B.cocycle))
    print(json.dumps({k:v for k,v in output.items() if k not in
        ('literal_correction_words','module_annihilator_basis','complete_hexagon_and_pure_endomorphism_checks')},indent=2),flush=True)

if __name__=='__main__':main()
