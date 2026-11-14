#!/usr/bin/env python3
"""Literal lifts and exact Magnus data for the full degree-seven pentagon.

Retains every saved post-mod9 candidate direction and the true kernel in
Zassenhaus degrees six and seven.  All tensors are denominator-free overF3.
"""
from pathlib import Path
from functools import cache
from itertools import product
import importlib.util,json,contextlib,io
import numpy as np

HERE=Path(__file__).resolve().parent
def load(name):
    spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
    obj=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
    return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge')
MAX=7

def add(p,q,s=1):
    out=dict(p)
    for w,c in q.items():out[w]=(out.get(w,0)+s*c)%3
    return {w:c for w,c in out.items() if c}
def mul(p,q):
    out={}
    for w,c in p.items():
        for v,d in q.items():
            if len(w)+len(v)>MAX:continue
            z=w+v;out[z]=(out.get(z,0)+c*d)%3
    return {w:c for w,c in out.items() if c}
def mag(word):
    p={():1}
    for l in word:
        if l>0:q={():1,(l-1,):1}
        else:q={(abs(l)-1,)*i:(-1)**i%3 for i in range(MAX+1)}
        p=mul(p,q)
    return p
MON=[w for n in range(MAX+1) for w in product(range(2),repeat=n)]
INDEX={w:i for i,w in enumerate(MON)}
def vector(p):
    out=np.zeros(len(MON),dtype=np.int64)
    for w,c in p.items():out[INDEX[w]]=c
    return out
def encode(p):return [[list(w),int(c)] for w,c in sorted(p.items(),key=lambda a:(len(a[0]),a[0]))]
def comm(a,b):return f.free_reduce(a+b+f.inverse_word(a)+f.inverse_word(b))
def literal(fa,fz):
    word=[]
    for a,w in zip(fa,f.NWORDS):word+=w*int(a)
    correction=(np.asarray(fz)-2*np.outer(fa,fa)[f.UP])%3
    for a,i,j in zip(correction,*f.UP):
        word+=comm(f.NWORDS[i],f.NWORDS[j])*int(a)
    word=f.free_reduce(word)
    aa,zz=f.literal(word)
    assert np.array_equal(aa,fa%3) and np.array_equal(zz,fz%3)
    # Exact F'-lift: the F-ab counts are multiples of9, hence these corrections
    # do not change the degree<=7 Magnus tensor or the finite Fermat element.
    ab=[sum((1 if l==i else -1 if l==-i else 0) for l in word) for i in (1,2)]
    assert not any(a%9 for a in ab)
    for i,a in enumerate(ab,1):word+=([-i]*a if a>=0 else [i]*(-a))
    return f.free_reduce(word)

gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
rows=json.loads((HERE/'a_ihara_mod9.json').read_text())
K=np.array(gt['central_kernel'],dtype=np.int64)
base=rows[0];ba=np.array(base['fa'],dtype=np.int64);bz=np.array(base['fz'],dtype=np.int64)
bword=literal(ba,bz);bmag=mag(bword);binv=mag(f.inverse_word(bword))
records=[];diffs=[]
for rr,r in enumerate(rows):
    fa=np.array(r['fa'],dtype=np.int64);fz=np.array(r['fz'],dtype=np.int64)
    old=np.array(r['old_parameter_kernel'],dtype=np.int64)
    candidates=[fz]+[(fz+K@col)%3 for col in old.T]
    for jj,zz in enumerate(candidates):
        word=literal(fa,zz);mm=mag(word)
        dd=add(mul(mm,binv),{():1},-1)
        lead=min(map(len,dd)) if dd else None
        records.append({'branch':rr,'basis_index':jj,'fa':fa.tolist(),'fz':zz.tolist(),
                        'literal_word':word,'magnus':encode(mm),'difference_leading_degree':lead})
        diffs.append(vector(dd))
print('Canonical exact F-prime base word length:',len(bword))
print('Candidate lift count:',len(records))
print('Candidate leading difference degrees:',[r['difference_leading_degree'] for r in records])
VV=np.stack(diffs,axis=1)
print('Magnus difference span through degree7:',f.rank(VV))
assert all(r['difference_leading_degree'] is None or r['difference_leading_degree']>=3 for r in records)

def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@cache
def tree(w):
    if len(w)==1:return w[0]
    for i in range(1,len(w)):
        if lyndon(w[i:]):return tree(w[:i]),tree(w[i:])
@cache
def word(t):
    return [t+1] if isinstance(t,int) else comm(word(t[0]),word(t[1]))

fil=json.loads((HERE/'a_ihara_filtration_exact.json').read_text())
corrections={}
for degree in (6,7):
    words=[word(tree(w)) for w in product(range(2),repeat=degree) if lyndon(w)]
    labels=[list(w) for w in product(range(2),repeat=degree) if lyndon(w)]
    if degree==6:words.append([1,2,-1,-2]*3);labels.append('cube_of_commutator')
    imgs=np.stack([np.concatenate(f.literal(w)) for w in words],axis=1)
    after=np.array(fil['gamma_bases'][str(degree+1)],dtype=np.int64)
    rel=g.kernel(np.hstack((imgs,-after)))[:len(words),:]
    _,piv=g.rref(rel)
    rel=rel[:,piv]
    rank=f.rank(rel)
    corrections[str(degree)]={'labels':labels,'literal_words':words,
                             'leading_kernel_basis':rel.tolist(),
                             'Fermat_group_images':imgs.tolist()}
    print('Degree',degree,'restricted Lie dimension',len(words),'leading kernel dimension',rank)
out={'maximum_Magnus_degree':MAX,'base_word':bword,'base_fa':ba.tolist(),'base_fz':bz.tolist(),
     'base_magnus':encode(bmag),'candidate_records':records,'kernel_corrections':corrections,
     'scope':'Literal representatives, degree<=7 Magnus tensors and leading kernel directions only.'}
(HERE/'a_ihara_pentagon_inputs.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS')
