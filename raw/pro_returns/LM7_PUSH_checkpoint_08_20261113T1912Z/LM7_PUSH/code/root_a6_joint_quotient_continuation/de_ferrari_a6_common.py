#!/usr/bin/env python3
"""Exact old-kernel image and the cubic Kummer comparison for full A6.

The target scalar is the literal c2 coefficient for the double cover.
No comparison with a matrix-defined extension on full GT is used.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_solvable import SolvableF,word_interfaces,evaluate_dag
from de_ferrari_a6_metabelian import Metabelian,rank,nullspace
from de_ferrari_a6_metafibres import Span
from de_ferrari_a6_source_data import load_data
from de_ferrari_two_core import rref2

HERE=Path(__file__).resolve().parent
BITS=((np.arange(64)[:,None]>>np.arange(6))&1).astype(np.int64)

class DoubleCover:
    # (x parity,c0,c1), retaining the actual positive y-loop labels.
    def __init__(self):self.one=np.zeros(3,dtype=np.int64);self.x=np.array([1,0,0]);self.y=np.array([0,1,0])
    def mul(self,a,b):return np.r_[(a[0]+b[0])%2,(a[1:]+(b[1:] if a[0]==0 else b[:0:-1]))%3]
    def inv(self,a):return np.r_[a[0],-(a[1:] if a[0]==0 else a[:0:-1])%3]
    def conj(self,a,b):return self.mul(self.mul(a,b),self.inv(a))
    def comm(self,a,b):return self.mul(self.conj(a,b),self.inv(b))

class WordDAG:
    def __init__(self,d):self.d=d;self.nodes=[['one']];self.grade=[99];self.cache={('one',):0};self.N=[self.node('N',j) for j in range(97)]
    def node(self,op,*args):
        key=(op,)+tuple(map(int,args))
        if key in self.cache:return self.cache[key]
        j=len(self.nodes);self.cache[key]=j;self.nodes.append(list(key))
        if op=='N':g=1
        elif op=='comm':g=self.grade[args[0]]+self.grade[args[1]]
        elif op in ('inv','power'):g=self.grade[args[0]]
        elif op=='mul':g=min(self.grade[args[0]],self.grade[args[1]])
        elif op=='conj':g=self.grade[args[1]]
        else:raise AssertionError(op)
        self.grade.append(g);return j
    def word(self,j,cache=None):
        if cache is None:cache={}
        if j in cache:return cache[j]
        rec=self.nodes[j];op=rec[0]
        if op=='one':w=[]
        elif op=='N':w=self.d['Nwords'][rec[1]]
        elif op=='inv':w=self.d['binv'](self.word(rec[1],cache))
        elif op=='power':w=self.d['bpower'](self.word(rec[1],cache),rec[2])
        elif op=='mul':w=self.word(rec[1],cache)+self.word(rec[2],cache)
        elif op=='comm':
            a,b=self.word(rec[1],cache),self.word(rec[2],cache);w=a+b+self.d['binv'](a)+self.d['binv'](b)
        elif op=='conj':
            a,b=self.word(rec[1],cache),self.word(rec[2],cache);w=a+b+self.d['binv'](a)
        else:raise AssertionError(op)
        cache[j]=w;return w

def independent_bits(values,words):
    selected=[];nodes=[];matrix=np.zeros((6,0),dtype=np.int64)
    for v,w in zip(values,words):
        if len(rref2(np.c_[matrix,BITS[v]])[1])>len(selected):
            selected.append(v);nodes.append(w);matrix=np.c_[matrix,BITS[v]]
    return selected,nodes

def main():
    start=time.time();F=SolvableF();E=F.E;M=Metabelian();d=load_data();dag=WordDAG(d)
    N=[F.word(d['fword'](w)) for w in d['Nwords']]
    V=Span();vb=[];vn=[];wb=[];wn=[];probes=0
    def add(g,node):
        nonlocal wb,wn
        coeff,inside=V.coordinates(g[:9])
        if not inside:
            V.add(g[:9],node);vb.append(g.copy());vn.append(node);return True
        rep=E.one.copy();rn=0
        for a,h,hn in zip(coeff,vb,vn):
            if a:rep=E.mul(rep,E.power(h,int(a)));rn=dag.node('mul',rn,dag.node('power',hn,int(a)))
        w=E.mul(E.inv(rep),g);assert not np.any(w[:9])
        before=len(wb);wb,wn=independent_bits(wb+[int(w[9])],wn+[dag.node('mul',dag.node('inv',rn),node)])
        return len(wb)>before
    for i in range(97):
        for j in range(i+1,97):
            probes+=1;g=F.comm(N[i],N[j]);assert not np.any(g[:2])
            add(g[2:],dag.node('comm',dag.N[i],dag.N[j]))
            if len(vb)==len(wb)==6:break
        if len(vb)==len(wb)==6:break
    while len(wb)<6:
        before=(len(vb),len(wb))
        for g,node in list(zip(vb,vn)):
            add(E.power(g,3),dag.node('power',node,3))
            for h,hn in list(zip(vb,vn)):add(E.comm(g,h),dag.node('comm',node,hn))
            for j,n in enumerate(N):add(F.conj(n,np.r_[0,0,g])[2:],dag.node('conj',dag.N[j],node))
        assert (len(vb),len(wb))!=before
    assert len(vb)==len(wb)==6
    levels=[{'lower_central_grade':2,'binary_rank':6,'word_nodes':wn.copy(),'binary_values':wb.copy()}]
    for grade in (3,4,5):
        values=[];nodes=[]
        for w,node in zip(wb,wn):
            pure=np.r_[0,0,np.zeros(9,dtype=np.int64),w]
            for j,n in enumerate(N):
                c=F.comm(n,pure);assert not np.any(c[:-1])
                values.append(int(c[-1]));nodes.append(dag.node('comm',dag.N[j],node))
        wb,wn=independent_bits(values,nodes);assert len(wb)==6
        assert all(dag.grade[j]>=grade for j in wn)
        levels.append({'lower_central_grade':grade,'binary_rank':6,'word_nodes':wn.copy(),'binary_values':wb.copy()})
    cache={};literal=[dag.word(j,cache) for j in wn]
    for w,value in zip(literal,wb):
        actual=F.word(d['fword'](w));assert not np.any(actual[:-1]) and actual[-1]==value
    K=np.load(HERE/'de_ferrari_a6_metafibres.npz')['complete_correction_basis']
    Q=nullspace(K.T).T;assert Q.shape==(3,9)
    p=json.loads((HERE/'bc_cm_fermat_kernel_boundary.json').read_text())
    k6=np.column_stack([M.word(d['fword'](w))[2:] for w in p['basis_F_prime_words_B']])
    assert rank(k6)==6 and not np.any(Q@k6%3)
    # The exact coefficient map is independently evaluated on the nine
    # actual F-prime basis words, in the two-coset Schreier group.
    cover=DoubleCover();nodes,targets,_,_=word_interfaces()
    ci=evaluate_dag(cover,nodes,targets,[cover.x,cover.y])
    assert not np.any(ci[:,0]) and not np.any((ci[:,1]+ci[:,2])%3)
    h=ci[:,1];assert h.tolist()==[1,2,2,1,2,1,2,2,2]
    assert int(h@M.c%3)==2
    assert not np.any((h@M.X+h)%3) and not np.any((h@M.Y-h)%3)
    assert not np.any(h@K%3)
    norm=np.vstack((M.I+M.S,M.I+M.R+M.R@M.R))%3
    normkernel=nullspace(norm);qnorm=Q@normkernel%3
    scalar=h@normkernel%3;line=np.array([2,1,0],dtype=np.int64)
    assert rank(qnorm)==1 and np.array_equal(qnorm,line[:,None]*scalar[None,:]%3)
    old=json.loads((HERE/'de_ferrari_a6_metafibres.json').read_text())['records'];oldcounts=[0,0,0]
    for row in old:
        v=np.array(row['original_f_module_value'],dtype=np.int64);c=int(h@v%3)
        assert np.array_equal(Q@v%3,line*c%3);oldcounts[c]+=1
    assert oldcounts==[288,288,288]
    # Stable lower-central image in P/C: its ternary quotient is V6,
    # while the complete binary kernel is reached at every displayed
    # depth.  The already certified perfect C is contained at every depth.
    stable=np.c_[(M.Xpow[6]-M.I)@K,(M.Xpow[4]@M.Ypow[2]-M.I)@K]%3
    assert rank(stable)==rank(np.c_[stable,K])==6
    out={'status':'PASS','actual_F_prime_over_N_prime_order':27,
        'exact_quotient_matrix_F3':Q.tolist(),'double_cover_coefficient_row_F3':h.tolist(),
        'norm_quotient_line_generator':line.tolist(),'norm_quotient_equals_line_times_c2':True,
        'K6_intersect_F_prime_killed_in_quotient':True,
        'complete_retained_scalar_counts':oldcounts,
        'literal_N_commutator_probes_for_initial_full_image':probes,
        'N_prime_mod_perfect_residual_order':3**6*64,
        'stable_N_lower_central_image_equals_N_prime':True,
        'source_word_DAG':dag.nodes,'source_word_lower_central_grades':dag.grade,
        'N_basis_words_B':d['Nwords'],'binary_lower_central_levels':levels,
        'literal_gamma5_words_B':literal,'literal_gamma5_word_lengths':list(map(len,literal)),
        'exact_D23_preserving_solvable_correction_image_order':3**6*64,
        'galois_comparison':'Nakamura-Schneps equation(2.4) and Lemma2.3: c2(f_sigma)=-A_sigma(-1,1)=kappa2(sigma).',
        'no_full_GT_matrix_coefficient_identification_used':True,
        'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_common.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'de_ferrari_a6_common.npz',quotient_matrix=Q,c2_row=h,
        gamma5_binary_basis=BITS[np.array(wb)].T,initial_N_derived_ternary_basis=np.column_stack([g[:9] for g in vb]))
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('source_word_DAG','source_word_lower_central_grades','N_basis_words_B','literal_gamma5_words_B')},indent=2),flush=True)

if __name__=='__main__':main()
