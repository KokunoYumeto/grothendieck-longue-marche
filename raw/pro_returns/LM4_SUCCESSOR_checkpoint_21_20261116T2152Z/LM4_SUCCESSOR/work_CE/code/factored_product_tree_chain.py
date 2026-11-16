#!/usr/bin/env python3
"""Exact linear-size product-tree chain circuits for literal F21 relators.

No full rectangle expansion is performed for the large input. Each term
is path_A(1,a) times one positive B edge, with its integer coefficient.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
WORDS=P/'geometric_stabilizer_column.json'
DATA=P/'symmetric_paired_fox_data.json'
raw=json.loads(WORDS.read_text());data=json.loads(DATA.read_text())

class Trie:
    def __init__(self):self.nodes=[(0,0,0)];self.index={}
    def append(self,p,x):
        assert x
        if p and self.nodes[p][1]==-x:return self.nodes[p][0]
        k=(p,x)
        if k not in self.index:
            self.index[k]=len(self.nodes)
            self.nodes.append((p,x,self.nodes[p][2]+1))
        return self.index[k]
    def read(self,p):
        w=[]
        while p:
            p,x,_=self.nodes[p];w.append(x)
        return tuple(reversed(w))
    def word(self,w):
        p=0
        for x in w:p=self.append(p,x)
        return p

T=Trie();R=Trie();generators=[None];gen_index={}
retained={j:i+1 for i,j in enumerate(data['retained_paired_indices'])}
beta={int(k):tuple(v) for k,v in data['retained_involution'].items()}
assert all(len(v)==1 for v in beta.values())

def add(c,k,n):
    c[k]+=n
    if not c[k]:del c[k]
def generator(head,slot):
    k=(head,slot)
    if k not in gen_index:gen_index[k]=len(generators);generators.append(k)
    return gen_index[k]

def compile_chain(word,name):
    head=betahead=a=b=0;rect=defaultdict(int)
    expected_A_potential=defaultdict(int);actual_B=defaultdict(int)
    deleted=0;expanded_cost=0
    for letter in word:
        j=abs(letter);sg=1 if letter>0 else -1
        if j in retained:
            k=retained[j];head=T.append(head,sg*k)
            betahead=T.append(betahead,sg*beta[k][0]);continue
        deleted+=1
        if j<12:
            g=generator(head,j);an=R.append(a,sg*g)
            add(expected_A_potential,(an,b),1);add(expected_A_potential,(a,b),-1)
            a=an
        else:
            g=generator(betahead,j-10);bn=R.append(b,sg*g)
            bv=b if sg>0 else bn
            if a:add(rect,(a,bv,g),sg)
            add(actual_B,(a,bv,g),sg)
            expanded_cost+=R.nodes[a][2];b=bn
    assert (head,betahead,a,b)==(0,0,0,0),(name,head,betahead,a,b)
    # Exact compressed boundary: rectangle gives two A-prefix paths,
    # the actual B edge, and its projection to the A=1 tree.
    potential=defaultdict(int);B_boundary=defaultdict(int)
    for (a,v,g),n in rect.items():
        vg=R.append(v,g)
        add(potential,(a,v),n);add(potential,(a,vg),-n)
        add(B_boundary,(a,v,g),n);add(B_boundary,(0,v,g),-n)
    # H(1,b)=0. Erase those symbols in both expressions.
    potential={k:v for k,v in potential.items() if k[0]}
    expected={k:v for k,v in expected_A_potential.items() if k[0]}
    assert potential==expected,(name,'A telescoping')
    assert dict(B_boundary)==dict(actual_B),(name,'B telescoping')
    return {'name':name,'literal_F21_word':word,'input_length':len(word),
            'deleted_letter_count':deleted,
            'rectangles':[{'A_endpoint':a,'B_edge_start':v,'B_generator':g,'coefficient':n}
                          for (a,v,g),n in sorted(rect.items())],
            'factored_term_count':len(rect),'uncollected_expansion_cost':expanded_cost,
            'retained_endpoint':0,'A_endpoint':0,'B_endpoint':0,
            'compressed_A_boundary_symbols':len(expected),'B_boundary_edges':len(actual_B),
            'full_compressed_boundary_verified':True}

started=time.monotonic()
node=next(r for r in data['node_columns'] if (r['loop_index'],r['local_node_index'])==(8,0))
circuits=[compile_chain(tuple(node['paired_relator']),'original_node_8_0'),
          compile_chain(tuple(raw['transformed_relator_F21']),'geometric_commutator_image')]

# Expand ONLY the original 124-letter calibration and compare all 117
# previously independently audited product-tree coefficients.
expanded=defaultdict(int)
for term in circuits[0]['rectangles']:
    av=0
    for x in R.read(term['A_endpoint']):
        an=R.append(av,x);start=av if x>0 else an
        add(expanded,(start,term['B_edge_start'],abs(x),term['B_generator']),
            term['coefficient']*(1 if x>0 else -1));av=an
oldgens={}
for k,r in data['finite_used_common_R_basis'].items():
    oldgens[int(k)]=generator(T.word(tuple(r['retained_word'])),r['paired_slot'])
def convert_old_word(w):return R.word((1 if x>0 else -1)*oldgens[abs(x)] for x in w)
want=defaultdict(int)
for c in node['fox_cells']:
    add(want,(convert_old_word(c['A_vertex']),convert_old_word(c['B_vertex']),
              oldgens[c['A_generator']],oldgens[c['B_generator']]),c['coefficient'])
assert dict(want)==dict(expanded) and len(expanded)==117

out={'scope':__doc__,'status':'complete_factored_full_chains',
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (WORDS,DATA)},
 'old_word':[6,2,-6,-2],'node_index':[8,0],
 'retained_word_DAG':T.nodes,'common_R_generators':generators,'R_word_DAG':R.nodes,
 'DAG_convention':'Node0 is empty; node(parent,signed_letter,length) is the freely reduced parent word followed by signed_letter. R generators are (retained_DAG_id,paired_slot); B uses beta of the actual retained head.',
 'circuit_semantics':'(a,v,j,n) denotes n times path_A(1,a) cross the positive B edge v->v*j, expanded with signed A path edges. This is the complete product-tree 2-chain.',
 'boundary_semantics':'d(path(1,a) cross edge(v,j)) = H(a,v)-H(a,v*j)+edge_B(a,v,j)-edge_B(1,v,j), where H(a,v) is the whole A path at B vertex v.',
 'G_normalization':'For every expanded cell with A vertex u, B vertex v, A generator(g,i), B generator(h,j), the exact G coefficient is (u,v,g) and the row is (i,j,beta(g)^-1*h); multiply by the signed path coefficient.',
 'circuits':circuits,'original_117_coefficient_calibration':True,
 'claims_excluded':['uncollected expansion is performed','full-column equality or independence','whole-module overlap decision','kappa conclusion'],
 'elapsed_seconds':time.monotonic()-started}
(P/'geometric_stabilizer_factored_chain.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
for c in circuits:print('PASS',c['name'],'letters',c['input_length'],'factored terms',c['factored_term_count'],'unexpanded cost',c['uncollected_expansion_cost'],flush=True)
print('PASS complete retained/R DAGs, both full telescoping boundaries, original117 calibration; elapsed',round(out['elapsed_seconds'],3),flush=True)
