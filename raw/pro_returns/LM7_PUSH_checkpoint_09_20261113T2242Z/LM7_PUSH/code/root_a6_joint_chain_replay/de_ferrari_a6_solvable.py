#!/usr/bin/env python3
"""Exact collection in the full maximal solvable A6 source quotient.

The perfect kernel is the certified actual normal subgroup C.  Its
quotient has pure normal forms x^a y^b e_v w, with a,b modulo120,
v in F3^9, and w in F2^6.  All extension data are extracted from
actual permutation sifts in de_a6_binary_module.cpp.
"""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_metabelian import Metabelian
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_abelian_compare import AbelianSource
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent

class EGroup:
    def __init__(self):
        self.raw=json.loads((HERE/'de_a6_binary_module.json').read_text())
        self.vraw=json.loads((HERE/'de_a6_module.json').read_text())
        assert self.raw['status']==self.vraw['status']=='PASS'
        self.weights=3**np.arange(9,dtype=np.int64)
        self.digits=(np.arange(3**9)[:,None]//self.weights[None,:])%3
        self.negcodes=((-self.digits)%3)@self.weights
        columns=np.array(self.raw['binary_conjugation_columns'],dtype=np.int64)
        self.wact=np.zeros((13,64),dtype=np.int64)
        for j in range(6):self.wact^=((np.arange(64)[None,:]>>j)&1)*columns[:,j,None]
        assert all(sorted(row.tolist())==list(range(64)) for row in self.wact)
        for a in self.wact[4:]:
            assert np.array_equal(a[a[a]],np.arange(64))
            for b in self.wact[4:]:assert np.array_equal(a[b],b[a])
        self.plus=np.empty((3**9,64),dtype=np.int64);self.plus[0]=np.arange(64)
        for k in range(1,3**9):
            j=int(np.flatnonzero(self.digits[k])[0]);self.plus[k]=self.wact[4+j,self.plus[k-int(self.weights[j])]]
        self.minus=self.plus[self.negcodes]
        self.one=np.zeros(10,dtype=np.int64)
        self.Vmat=np.array(self.vraw['conjugation_matrices'],dtype=np.int64)
        self.twist=[];self.vmap=[]
        twists=np.array(self.raw['complement_conjugation_binary_twists'],dtype=np.int64)
        for t in range(4):
            image=np.c_[self.Vmat[t].T,twists[t]]
            powers=np.stack((np.zeros_like(image),image,self.mul(image,image)))
            out=np.zeros((3**9,10),dtype=np.int64)
            for j in range(9):out=self.mul(out,powers[self.digits[:,j],j])
            assert np.array_equal(out[:,:9],self.digits@self.Vmat[t].T%3)
            self.twist.append(out[:,9]);self.vmap.append(out[:,:9]@self.weights)
        self.twist=np.array(self.twist);self.vmap=np.array(self.vmap)
        for t,n in ((0,2),(1,3)):
            codes=np.arange(3**9);h=np.zeros(3**9,dtype=np.int64);w=np.arange(64)
            for _ in range(n):h=self.twist[t,codes]^self.wact[t,h];codes=self.vmap[t,codes];w=self.wact[t,w]
            assert np.array_equal(codes,np.arange(3**9)) and not np.any(h) and np.array_equal(w,np.arange(64))
        self.powV=[];self.powH=[];self.powW=[]
        for t in (2,3):
            codes=[np.arange(3**9)];h=[np.zeros(3**9,dtype=np.int64)];w=[np.arange(64)]
            for n in range(120):
                h.append(self.twist[t,codes[-1]]^self.wact[t,h[-1]])
                codes.append(self.vmap[t,codes[-1]]);w.append(self.wact[t,w[-1]])
            assert np.array_equal(codes[-1],codes[0]) and not np.any(h[-1]) and np.array_equal(w[-1],w[0])
            self.powV.append(np.array(codes));self.powH.append(np.array(h));self.powW.append(np.array(w))
        self.powV=np.array(self.powV);self.powH=np.array(self.powH);self.powW=np.array(self.powW)
        self.complement=np.c_[np.eye(9,dtype=np.int64),np.zeros(9,dtype=np.int64)]
        self.original=self.complement.copy();self.original[:,9]=self.raw['complement_basis_corrections']
        self.Wbasis=np.zeros((6,10),dtype=np.int64);self.Wbasis[:,9]=1<<np.arange(6)
        self.c=np.r_[self.raw['commutator_x_y_complement_V'],self.raw['commutator_x_y_binary_coordinate']]
    def code(self,g):return np.asarray(g)[...,:9]@self.weights
    def mul(self,g,h):
        g=np.asarray(g);h=np.asarray(h)
        return np.concatenate(((g[...,:9]+h[...,:9])%3,
            (self.minus[self.code(h),g[...,9]]^h[...,9])[...,None]),axis=-1)
    def inv(self,g):
        g=np.asarray(g)
        return np.concatenate(((-g[...,:9])%3,self.plus[self.code(g),g[...,9]][...,None]),axis=-1)
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=np.zeros_like(g)
        while n:
            if n&1:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def comm(self,g,h):return self.mul(self.mul(self.mul(g,h),self.inv(g)),self.inv(h))
    def conj(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def act(self,t,g):
        g=np.asarray(g);code=self.code(g)
        return np.concatenate((self.digits[self.vmap[t,code]],
            (self.twist[t,code]^self.wact[t,g[...,9]])[...,None]),axis=-1)
    def act_power(self,axis,n,g):
        n%=120;g=np.asarray(g);code=self.code(g)
        return np.concatenate((self.digits[self.powV[axis,n,code]],
            (self.powH[axis,n,code]^self.powW[axis,n,g[...,9]])[...,None]),axis=-1)

class SolvableF:
    def __init__(self):
        self.E=EGroup();E=self.E
        self.one=np.zeros(12,dtype=np.int64)
        self.x=self.one.copy();self.x[0]=1;self.y=self.one.copy();self.y[1]=1
        self.db=[E.one.copy()]
        d1=E.act_power(1,-1,E.act_power(0,-1,E.inv(E.c)))
        for b in range(120):self.db.append(E.mul(E.act_power(1,-1,self.db[-1]),d1))
        assert not np.any(self.db[120])
        self.cross=np.zeros((120,121,10),dtype=np.int64)
        for c in range(120):self.cross[:,c+1]=E.mul(np.array(self.db[:120]),E.act_power(0,-1,self.cross[:,c]))
        assert not np.any(self.cross[:,120])
        self.letters={1:self.x,2:self.y,-1:self.inv(self.x),-2:self.inv(self.y)}
        assert np.array_equal(self.comm(self.x,self.y),np.r_[0,0,E.c])
        for e in list(E.complement)+list(E.Wbasis):
            lhs=E.act(2,E.act(3,e));rhs=E.conj(E.c,E.act(3,E.act(2,e)))
            assert np.array_equal(lhs,rhs)
    def mul(self,g,h):
        a,b=map(int,g[:2]);c,d=map(int,h[:2]);E=self.E
        mid=E.mul(self.cross[b,c],E.act_power(0,-c,g[2:]))
        return np.r_[(a+c)%120,(b+d)%120,E.mul(E.act_power(1,-d,mid),h[2:])]
    def inv(self,g):
        a,b=map(int,g[:2]);c,d=(-a)%120,(-b)%120;E=self.E
        mid=E.mul(self.cross[b,c],E.act_power(0,-c,g[2:]))
        return np.r_[c,d,E.inv(E.act_power(1,-d,mid))]
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=self.one.copy()
        while n:
            if n&1:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def conj(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def comm(self,g,h):return self.mul(self.conj(g,h),self.inv(h))
    def word(self,w):
        out=self.one.copy()
        for a in w:out=self.mul(out,self.letters[a])
        return out
    def forget_W(self,g):return np.asarray(g)[...,:11]

class SolvableB:
    def __init__(self,F,d):
        self.F,self.d=F,d;self.A=AbelianSource(d,120);self.e=self.A.e;self.table=self.A.table;self.paths=self.A.paths
        self.xy=[];self.cocycle=[]
        for p in self.paths:self.xy.append([F.word(d['fword'](p+w+d['binv'](p))) for w in (d['xword'],d['yword'])])
        for i,p in enumerate(self.paths):self.cocycle.append([F.word(d['fword'](p+q+d['binv'](self.paths[self.table[i,j]]))) for j,q in enumerate(self.paths)])
        self.qinverse=[next(j for j in range(6) if self.table[i,j]==self.e) for i in range(6)]
        self.one=(self.e,F.one.copy());self.letters={a:self.literal([a]) for a in (0,1,-1)}
        self.s,self.r=self.letters[0],self.letters[1]
        assert self.equal(self.power(self.s,2),self.one) and self.equal(self.power(self.r,3),self.one)
        for q in range(6):
            for r in range(6):
                qr=self.table[q,r];c=self.cocycle[q][r]
                for e in [F.x,F.y]+[np.r_[0,0,e] for e in list(F.E.complement)+list(F.E.Wbasis)]:
                    assert np.array_equal(self.act(q,self.act(r,e)),F.conj(c,self.act(qr,e)))
                for t in range(6):assert np.array_equal(F.mul(c,self.cocycle[qr][t]),F.mul(self.act(q,self.cocycle[r][t]),self.cocycle[q][self.table[r,t]]))
    def act(self,q,g):
        F=self.F;e=g[2:]
        for a in reversed(self.paths[q]):
            if a==0:e=F.E.act(0,e)
            elif a==1:e=F.E.act(1,e)
            else:e=F.E.act(1,F.E.act(1,e))
        x,y=self.xy[q]
        return F.mul(F.mul(F.power(x,int(g[0])),F.power(y,int(g[1]))),np.r_[0,0,e])
    def mul(self,g,h):
        q,v=g;r,w=h
        return int(self.table[q,r]),self.F.mul(self.F.mul(v,self.act(q,w)),self.cocycle[q][r])
    def inv(self,g):
        q,v=g;r=self.qinverse[q]
        return r,self.F.mul(self.F.inv(self.cocycle[r][q]),self.act(r,self.F.inv(v)))
    def power(self,g,n):
        if n<0:return self.power(self.inv(g),-n)
        out=self.one
        while n:
            if n&1:out=self.mul(out,g)
            g=self.mul(g,g);n//=2
        return out
    def conj(self,g,h):return self.mul(self.mul(g,h),self.inv(g))
    def equal(self,g,h):return g[0]==h[0] and np.array_equal(g[1],h[1])
    def literal(self,w):
        q=self.d['unit']
        for a in w:q=self.d['mul2'](q,self.d['s2'] if a==0 else self.d['r2'] if a==1 else self.d['r22'])
        j=self.A.qindex[q];return j,self.F.word(self.d['fword'](w+self.d['binv'](self.paths[j])))
    def word(self,w):
        g=self.one
        for a in w:g=self.mul(g,self.letters[a])
        return g

def ancestors(nodes,targets):
    known=set(map(int,targets));todo=list(known)
    while todo:
        j=todo.pop();op,a,b=map(int,nodes[j]);parts=[] if op<2 else [a] if op==3 else [a,b]
        for k in parts:
            if k not in known:known.add(k);todo.append(k)
    return sorted(known)

def evaluate_dag(group,nodes,targets,original):
    values={}
    for j in ancestors(nodes,targets):
        op,a,b=map(int,nodes[j])
        if op==0:v=group.one.copy()
        elif op==1:v=original[a].copy()
        elif op==2:v=group.mul(values[a],values[b])
        elif op==3:v=group.inv(values[a])
        elif op==4:v=group.comm(values[a],values[b])
        elif op==5:v=group.conj(values[a],values[b])
        else:raise AssertionError('word operation')
        values[j]=v
    return np.array([values[int(j)] for j in targets])

def word_interfaces():
    d=read_certificate(HERE/'de_a6_schreier_Fprime.bin')
    p=json.loads((HERE/'de_a6_schreier_Fprimecompact_input.json').read_text())
    v=json.loads((HERE/'de_a6_module.json').read_text())
    targets=[int(d['words'][p['source_indices'][j]]) for j in v['selected_original_indices']]
    w=read_certificate(HERE/'de_a6_schreier_Fprimeprime.bin')
    b=json.loads((HERE/'de_a6_binary_module_basis.json').read_text())
    return d['nodes'],targets,w['nodes'],b['selected_source_word_nodes']

def main():
    start=time.time();F=SolvableF();d=load_data();B=SolvableB(F,d);M=Metabelian()
    nodes,targets,wnodes,wtargets=word_interfaces()
    ei=evaluate_dag(F,nodes,targets,[F.x,F.y]);assert not np.any(ei[:,:2])
    assert np.array_equal(ei[:,2:],F.E.original)
    w=evaluate_dag(F.E,wnodes,wtargets,list(F.E.original))
    assert np.array_equal(w,F.E.Wbasis)
    for g in (F.x,F.y,F.inv(F.x),F.inv(F.y))+tuple(np.r_[0,0,e] for e in F.E.original):
        assert np.array_equal(F.mul(g,F.inv(g)),F.one) and np.array_equal(F.mul(F.inv(g),g),F.one)
        for h in (F.x,F.y,F.comm(F.x,F.y)):
            assert np.array_equal(F.forget_W(F.mul(g,h)),M.mul(F.forget_W(g),F.forget_W(h)))
    assert np.array_equal(F.power(F.x,120),F.one) and np.array_equal(F.power(F.y,120),F.one)
    out={'status':'PASS','actual_source_quotient_order':6*120**2*3**9*64,
         'pure_normal_form':['a mod120','b mod120','v in F3^9','w in F2^6'],
         'literal_original_E_basis_word_ancestors':len(ancestors(nodes,targets)),
         'literal_W_basis_word_ancestors':len(ancestors(wnodes,wtargets)),
         'all_original_E_and_W_words_replayed':True,
         'complete_B_extension_cocycle_checks':216,
         'literal_projection_to_previous_metabelian_model':True,
         'cyclic_E_complement_order':3**9,'binary_normal_kernel_order':64,
         'scope':'Actual maximal solvable quotient G/C; equations and source lifting are computed separately.',
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_solvable.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'de_ferrari_a6_solvable.npz',E_binary_actions=F.E.wact,
        E_complement_twists=F.E.twist,ordinary_F_collection_cross_terms=F.cross,
        actual_B_extension_cocycle=np.array(B.cocycle),original_E_basis=F.E.original)
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
