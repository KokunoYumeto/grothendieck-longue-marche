#!/usr/bin/env python3
"""One actual geometric stabilizer word at node(8,0), with explicit budgets.

Uses the literal positive geometric word[6,2,-6,-2], never an orbit search.
The two meridians are transported first; their commutator then defines the
whole product-tree chain and the full G-normalized column.  A budget exit
is recorded as incomplete and never promoted to a membership conclusion.
"""
from pathlib import Path
from collections import defaultdict
import hashlib, json, time, sys

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
data_path=P/'symmetric_paired_fox_data.json'
raw=data_path.read_bytes();D=json.loads(raw);started=time.monotonic()
key=(8,0);node=next(n for n in D['node_columns']
                    if (n['loop_index'],n['local_node_index'])==key)
word=(6,2,-6,-2);max_intermediate_length=200000
max_generated_letters=4000000;max_rectangles=5000000
stats={'generated_letters':0,'rectangles':0}

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)

def inv(w):return tuple(-x for x in reversed(w))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
def sub(w,A):
    out=[]
    for x in w:
        for y in (A[abs(x)] if x>0 else inv(A[-x])):
            stats['generated_letters']+=1
            if stats['generated_letters']>max_generated_letters:
                raise RuntimeError('explicit generated-letter budget exceeded')
            if out and out[-1]==-y:out.pop()
            else:out.append(y)
            if len(out)>max_intermediate_length:
                raise RuntimeError('explicit intermediate-word budget exceeded')
    return tuple(out)
def comm(a,b):return red(a+b+inv(a)+inv(b))
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]

beta=mp(D['retained_involution']);F=mp(D['paired_involution'])
retained=D['retained_paired_indices'];head_id={j:i+1 for i,j in enumerate(retained)}

def plain_sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[-x])))
def rr(w):
    out=[]
    for x in w:
        if out and out[-1]==(-x[0],x[1],x[2]):out.pop()
        else:out.append(x)
    return tuple(out)
def split(w):
    head=();out=[]
    for x in w:
        j,sign=abs(x),1 if x>0 else -1
        if j in head_id:head=red(head+(sign*head_id[j],))
        elif j<12:out.append((0,(sign,head,j)))
        else:out.append((1,(sign,plain_sub(head,beta),j-10)))
    assert not head
    return out
def chain(w):
    a=b=();out=defaultdict(int);edges=defaultdict(int)
    for side,x in split(w):
        if side==0:
            an=rr(a+(x,));add(edges,(0,a if x[0]>0 else an,b,x[1:]),x[0]);a=an
        else:
            bn=rr(b+(x,));bv=b if x[0]>0 else bn
            add(edges,(1,a,bv,x[1:]),x[0]);u=()
            for y in a:
                stats['rectangles']+=1
                if stats['rectangles']>max_rectangles:
                    raise RuntimeError('explicit rectangle budget exceeded')
                un=rr(u+(y,));av=u if y[0]>0 else un
                add(out,(av,bv,y[1:],x[1:]),y[0]*x[0]);u=un
            b=bn
    assert not a and not b
    boundary=defaultdict(int)
    for (u,v,i,j),n in out.items():
        add(boundary,(0,u,v,i),n);add(boundary,(0,u,rr(v+((1,*j),)),i),-n)
        add(boundary,(1,rr(u+((1,*i),)),v,j),n);add(boundary,(1,u,v,j),-n)
    assert dict(boundary)==dict(edges)
    return dict(out)
def normalize(c):
    out=defaultdict(int)
    for (u,v,(g,i),(h,j)),n in c.items():
        z=red(inv(plain_sub(g,beta))+h)
        add(out,((i,j,z),(u,v,g)),n)
    return dict(out)
def augment(c):
    out=defaultdict(int)
    for (r,g),n in c.items():add(out,(r,g[2]),n)
    return dict(out)
def encode(c):
    return [{'row':r,'G_coefficient':{'A_word':u,'B_word':v,'retained_word':t},'integer':n}
            for (r,(u,v,t)),n in sorted(c.items())]

out={'scope':__doc__,'input_sha256':hashlib.sha256(raw).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'old_word':word,'node_index':key,'stages':[],
     'budgets':{'intermediate_letters':max_intermediate_length,
                'generated_letters':max_generated_letters,'rectangles':max_rectangles},
     'status':'running'}
target=P/'geometric_stabilizer_column.json'
def checkpoint():
    out['statistics']=dict(stats);out['elapsed_seconds']=time.monotonic()-started
    target.write_text(json.dumps(out,indent=2)+'\n')

try:
    p,q=map(tuple,node['paired_meridians']);original=comm(p,q)
    assert original==tuple(node['paired_relator'])
    previous=original
    for letter in word:
        action=mp(D['old_actions'][abs(letter)-1][
            'geometric_push_paired' if letter>0 else 'based_pullback_paired'])
        p,q=sub(p,action),sub(q,action)
        now=comm(p,q);assert now==sub(previous,action)
        out['stages'].append({'letter':letter,'meridian_lengths':[len(p),len(q)],
                              'relator_length':len(now),'generated_letters':stats['generated_letters']})
        previous=now;checkpoint()
        print('PASS exact action stage',letter,'meridians',len(p),len(q),'relator',len(now),flush=True)
    out['transformed_meridians_F21']=[p,q];out['transformed_relator_F21']=previous
    checkpoint()
    if '--words-only' in sys.argv:
        out['status']='complete_words_only';checkpoint()
        print('PASS complete literal words retained; product-tree chain remains separate.',flush=True)
        sys.exit(0)
    c=chain(original);d=chain(previous)
    Fc=chain(plain_sub(previous,F))
    assert Fc=={(v,u,j,i):-n for (u,v,i,j),n in d.items()}
    C,G=normalize(c),normalize(d)
    assert augment(C)==augment(G)
    cr,gr={r for r,a in C},{r for r,a in G}
    newrows=sorted(gr-cr);lostrows=sorted(cr-gr)
    out.update({'original_relator_F21':original,'original_full_G_column':encode(C),
                'transformed_full_G_column':encode(G),'original_terms':len(C),
                'transformed_terms':len(G),'identical_augmentation':True,
                'new_full_rows':newrows,'lost_full_rows':lostrows,
                'full_F_chain_identity':True,'status':'complete'})
    if newrows:
        r=min(newrows,key=lambda x:(sum(rr==x for rr,a in G),x))
        out['private_row']=r
        out['collected_nonzero_private_row']=[x for x in encode(G) if tuple(x['row'])==r]
        out['two_column_consequence']='Rank-two directness over Z[G] by the proved domain property; no whole-block overlap conclusion.'
    out['claims_excluded']=['all stabilizer words','whole64-column overlap','global kappa','I=R']
    checkpoint()
    print('PASS actual full G action; terms',len(C),len(G),'new rows',len(newrows),
          'lost rows',len(lostrows),'elapsed',round(out['elapsed_seconds'],3),flush=True)
except Exception as e:
    out['status']='incomplete';out['error']=repr(e);checkpoint();raise
