#!/usr/bin/env python3
"""Exact nonabelian comb-basis rewrite in N_gen, before node fillings.

The basis element c(a,b,x)=b[a,x]b^-1 is indexed by a!=1, b in R_B,
and a positive B generator x. This computes actual free words, not
their abelianizations. Existing128 nodes and the existing geometric
stabilizer image only; no orbit-depth or simultaneous-basis search.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib,time

ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
FINITE=P/'finite_even_boundary32.json';FULL=P/'actual_full21_Fox.json'
FACTORED=P/'geometric_stabilizer_factored_chain.json'
D=json.loads(FULL.read_text());C=json.loads(FINITE.read_text());B=json.loads(FACTORED.read_text())


class Trie:
    def __init__(self):self.nodes=[(0,0,0)];self.index={}
    def append(self,p,x):
        if p and self.nodes[p][1]==-x:return self.nodes[p][0]
        k=(p,x)
        if k not in self.index:
            self.index[k]=len(self.nodes);self.nodes.append((p,x,self.nodes[p][2]+1))
        return self.index[k]
    def read(self,p):
        w=[]
        while p:p,x,n=self.nodes[p];w.append(x)
        return tuple(reversed(w))
    def word(self,w):
        p=0
        for x in w:p=self.append(p,x)
        return p


T,R=Trie(),Trie();gens=[None];gindex={};Ngens=[None];Nindex={}
retained={j:i+1 for i,j in enumerate(D['retained_paired_indices'])}
beta={int(k):v[0] for k,v in D['retained_involution'].items()}
def gen(t,i):
    key=(t,i)
    if key not in gindex:gindex[key]=len(gens);gens.append(key)
    return gindex[key]
def n_gen(a,b,x):
    assert a!=0 and x>0
    key=(a,b,x)
    if key not in Nindex:Nindex[key]=len(Ngens);Ngens.append(key)
    return Nindex[key]
def append_word(w,x):
    if w and w[-1]==-x:w.pop()
    else:w.append(x)
def inverse(w):return tuple(-x for x in reversed(w))
def abelian(w):
    c=defaultdict(int)
    for x in w:
        c[abs(x)]+=1 if x>0 else-1
        if not c[abs(x)]:del c[abs(x)]
    return dict(c)


def rewrite(word,name,expand_check):
    a=b=t=bt=0;nword=[];schreier=[];Bsteps=0
    for letter in word:
        j=abs(letter);sign=1 if letter>0 else-1
        if j in retained:
            k=retained[j];t=T.append(t,sign*k);bt=T.append(bt,sign*beta[k]);continue
        if j<12:
            g=gen(t,j);a=R.append(a,sign*g)
            append_word(schreier,sign*(2*g-1))
        else:
            g=gen(bt,j-10);bn=R.append(b,sign*g)
            if a:append_word(nword,sign*n_gen(a,b if sign>0 else bn,g))
            b=bn;Bsteps+=1;append_word(schreier,sign*2*g)
    assert(a,b,t,bt)==(0,0,0,0),name
    # Expand only the existing short128 node words. The119780-letter
    # image uses the exact prefix identity, not a67-million rectangle
    # or conjugator expansion.
    if expand_check:
        result=[]
        for letter in nword:
            av,bv,x=Ngens[abs(letter)]
            A=tuple((1 if y>0 else-1)*(2*abs(y)-1) for y in R.read(av))
            Bw=tuple(2*y for y in R.read(bv));X=(2*x,)
            c=Bw+A+X+inverse(A)+inverse(X)+inverse(Bw)
            if letter<0:c=inverse(c)
            for y in c:append_word(result,y)
        assert result==schreier,('entire nonlinear expansion',name)
    counts=Counter(map(abs,nword));singleton=next((k for k,v in counts.items() if v==1),None)
    witness=None
    if singleton is not None:
        position=next(i for i,x in enumerate(nword) if abs(x)==singleton)
        sign=1 if nword[position]>0 else-1
        witness={'basis_generator':singleton,'position':position,'sign':sign,
                 'left_length':position,'right_length':len(nword)-position-1,
                 'inverse_rule':'x->L^-1*x*R^-1' if sign>0 else 'x->R*x^-1*L',
                 'scope':'This individual word is primitive; no simultaneous free-factor claim.'}
    return {'name':name,'literal_F21_word':word,'input_length':len(word),
            'nonlinear_N_word':nword,'nonlinear_length':len(nword),
            'B_letter_count':Bsteps,'abelianization':[[k,v] for k,v in sorted(abelian(nword).items())],
            'entire_small_word_expansion_verified':expand_check,
            'single_occurrence_primitive_witness':witness}


started=time.monotonic();records=[]
for f in C['faces']:
    if f['type']=='node':
        rec=rewrite(f['literal_F21_word'],f"sheet{f['sheet']}_node{tuple(f['node_index'])}",True)
        rec['sheet']=f['sheet'];rec['node_index']=f['node_index'];records.append(rec)
big=rewrite(B['circuits'][1]['literal_F21_word'],'geometric_stabilizer_image',False);records.append(big)

# Compare BOTH exact abelianizations with the already audited B103
# root-path dictionaries, translating all canonical word indices.
def oldread(nodes,p):
    w=[]
    while p:p,x,n=nodes[p];w.append(x)
    return tuple(reversed(w))
oldgen={i:gen(T.word(oldread(B['retained_word_DAG'],t)),slot)
        for i,(t,slot) in enumerate(B['common_R_generators'][1:],1)}
def oldR(p):return R.word((1 if x>0 else-1)*oldgen[abs(x)] for x in oldread(B['R_word_DAG'],p))
small=next(r for r in records if r.get('sheet')==0 and r.get('node_index')==[8,0])
for rec,circuit in [(small,B['circuits'][0]),(big,B['circuits'][1])]:
    target={}
    for q in circuit['rectangles']:
        key=n_gen(oldR(q['A_endpoint']),oldR(q['B_edge_start']),oldgen[q['B_generator']])
        target[key]=q['coefficient']
    assert abelian(rec['nonlinear_N_word'])==target

out={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in(FINITE,FULL,FACTORED)},
 'retained_word_DAG':T.nodes,'common_R_generators':gens,'R_word_DAG':R.nodes,
 'N_free_generators':Ngens,
 'N_basis_semantics':'Generator(a,b,x) is b*[a,x]*b^-1 in the free product R_A*R_B, with a!=1 and x a positive B generator. A uses a_R_word, B uses b_R_word.',
 'prefix_invariant':'Every original pairedF21 prefix equals n*b*a*t in the actual free group W. A letters update a; retained letters update t; a positive B letter appends c(a,b,x), a negative one appends c(a,b*x^-1,x)^-1. Tree edges at a=1 append nothing.',
 'records':records,'all128_entire_nonlinear_expansions_verified':True,
 'both_B103_abelianizations_equal':True,
 'counts':{'node_words':128,'node_primitive_singleton_witnesses':sum(r['single_occurrence_primitive_witness'] is not None for r in records[:128]),
           'node_total_nonlinear_letters':sum(r['nonlinear_length'] for r in records[:128]),
           'geometric_image_nonlinear_letters':big['nonlinear_length'],
           'geometric_image_abelian_terms':len(big['abelianization'])},
 'claims_excluded':['simultaneous free basis for the relator family','normal closure only of a finite block','main kernel equality or nonlinear fixed lifting','large conjugator expansion'],
 'elapsed_seconds':time.monotonic()-started}
(P/'nonlinear_comb_rewrite.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS all128 entire nonlinear free-word rewrites; exact comb prefix invariant')
print('PASS both complete B103 abelianizations; no expansion of large image generators')
print('COUNTS',out['counts']);print('DONE elapsed',round(out['elapsed_seconds'],3))
