#!/usr/bin/env python3
"""Reusable exact Z[G] operations on the full root-path chain normal form.

No standard rectangle expansion. Actual retained action is the positive
basis permutation r_(g,i)->r_(t*g,i), with beta(t) on the B factor.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time

class Words:
    def __init__(self,nodes):
        self.nodes=[tuple(x) for x in nodes]
        self.index={(p,x):i for i,(p,x,_) in enumerate(self.nodes) if i}
    def append(self,p,x):
        if p and self.nodes[p][1]==-x:return self.nodes[p][0]
        key=p,x
        if key not in self.index:
            self.index[key]=len(self.nodes)
            self.nodes.append((p,x,self.nodes[p][2]+1))
        return self.index[key]
    def read(self,p):
        w=[]
        while p:p,x,_=self.nodes[p];w.append(x)
        return tuple(reversed(w))
    def word(self,w,start=0):
        for x in w:start=self.append(start,x)
        return start

class ChainModule:
    def __init__(self,data):
        self.T=Words(data['retained_word_DAG']);self.R=Words(data['R_word_DAG'])
        self.generators=[None]+[tuple(x) for x in data['common_R_generators'][1:]]
        self.generator_ids={x:i for i,x in enumerate(self.generators) if i}
        self.beta_letters={1:-1,2:4,3:5,4:2,5:3}
    def beta(self,t):
        return self.T.word((1 if x>0 else -1)*self.beta_letters[abs(x)] for x in self.T.read(t))
    def generator(self,head,slot):
        key=head,slot
        if key not in self.generator_ids:
            self.generator_ids[key]=len(self.generators);self.generators.append(key)
        return self.generator_ids[key]
    def shifted_generator(self,g,t):
        h,i=self.generators[g]
        return self.generator(self.T.word(self.T.read(h),t),i)
    def translator(self,u,t):
        memo={0:u};letters={}
        def translate(a):
            stack=[];at=a
            while at not in memo:stack.append(at);at=self.R.nodes[at][0]
            for k in reversed(stack):
                p,x,_=self.R.nodes[k]
                if abs(x) not in letters:letters[abs(x)]=self.shifted_generator(abs(x),t)
                memo[k]=self.R.append(memo[p],(1 if x>0 else -1)*letters[abs(x)])
            return memo[a]
        return translate
    def action(self,g,chain):
        u,v,t=g;bt=self.beta(t);A=self.translator(u,t);B=self.translator(v,bt)
        out=defaultdict(int);shifts={}
        for (a,b,j),n in chain.items():
            if j not in shifts:shifts[j]=self.shifted_generator(j,bt)
            aa,bb,jj=A(a),B(b),shifts[j]
            if aa:out[aa,bb,jj]+=n
            if u:out[u,bb,jj]-=n
        result={k:v for k,v in out.items() if v}
        assert len(result)<=2*len(chain)
        return result
    def multiply(self,g,h):
        u,v,t=g;x,y,s=h
        return self.translator(u,t)(x),self.translator(v,self.beta(t))(y),self.T.word(self.T.read(s),t)
    def inverse(self,g):
        u,v,t=g
        it=self.T.word(-x for x in reversed(self.T.read(t)))
        iu=self.R.word(-x for x in reversed(self.R.read(u)))
        iv=self.R.word(-x for x in reversed(self.R.read(v)))
        return self.translator(0,it)(iu),self.translator(0,self.beta(it))(iv),it
    @staticmethod
    def load_chain(c):
        return {(x['A_endpoint'],x['B_edge_start'],x['B_generator']):x['coefficient'] for x in c['rectangles']}

def main():
    root=Path(__file__).resolve().parents[2]
    p=root/'work_CE/next_symmetric_nodes/geometric_stabilizer_factored_chain.json'
    data=json.loads(p.read_text());M=ChainModule(data);start=time.monotonic()
    g=(M.R.word((1,)),M.R.word((2,)),M.T.word((1,2)))
    h=(M.R.word((3,-2)),M.R.word((-1,)),M.T.word((-2,3)))
    assert M.multiply(g,M.inverse(g))==M.multiply(M.inverse(g),g)==(0,0,0)
    rows=[]
    for c in data['circuits']:
        C=M.load_chain(c)
        assert M.action((0,0,0),C)==C
        gC=M.action(g,C)
        assert M.action(M.inverse(g),gC)==C
        assert M.action(h,gC)==M.action(M.multiply(h,g),C)
        rows.append({'name':c['name'],'input_terms':len(C),'g_action_terms':len(gC),
                     'identity_inverse_and_product_actions_verified':True})
        print('PASS',c['name'],'all full identity/inverse/product G actions;',len(C),'->',len(gC),'terms',flush=True)
    out={'scope':__doc__,'status':'PASS','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
         'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'checks':rows,'actual_edge_action':'tau_t(r_(g,i))=r_(tg,i), so each positive edge goes to one positive edge; B uses beta(t).',
         'general_action_bound':'at most two root-path terms per input term, for every actual G monomial',
         'elapsed_seconds':time.monotonic()-start,'no_rectangle_expansion':True}
    (root/'work_CE/next_symmetric_nodes/root_path_chain_operations_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS reusable exact G-module operations, elapsed',round(out['elapsed_seconds'],3),flush=True)

if __name__=='__main__':main()
