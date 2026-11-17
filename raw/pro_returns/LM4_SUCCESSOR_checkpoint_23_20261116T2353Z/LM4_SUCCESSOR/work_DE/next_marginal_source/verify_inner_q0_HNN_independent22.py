#!/usr/bin/env python3
"""Independent exact q0/HNN replay using a commuting-letter scan.

No CE oracle is imported.  In contrast to its dependence-piling engine,
this evaluator cancels inverse graph letters by scanning across precisely
the commuting suffix.  Coordinate-clique membership is then support.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'work_CE/next_symmetric_nodes'
paths = [P/'inner_bad_orbifold_words22.json',
         ROOT/'records/inner_bad_normalized22.json',
         ROOT/'records/inner_bad_hnn22.json', P/'inner_q0_HNN22.json']
D, N, H, CE = [json.loads(p.read_text()) for p in paths]

def red(w):
    a=[]
    for x in w:
        x=2 if abs(x)==2 else int(x)
        if a and (a[-1]==-x or a[-1]==x==2):a.pop()
        else:a.append(x)
    return tuple(a)
def inv(w):return red(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,A):return mul(*(A[abs(x)] if x>0 else inv(A[-x]) for x in w))

V=tuple(tuple(v) for v in H['base_vertices'])
edges={frozenset(map(tuple,e)) for e in H['base_edges']}
def commute(v,w):return v==w or frozenset((v,w)) in edges
def graph_reduce(letters):
    ans=[]
    for v,sign in letters:
        assert v in V and sign in (-1,1)
        removed=False
        for k in range(len(ans)-1,-1,-1):
            u,s=ans[k]
            if u==v:
                if s==-sign:
                    ans.pop(k);removed=True
                break
            if not commute(u,v):break
        if not removed:ans.append((v,sign))
    return tuple(ans)
def parse_base(word):
    parity=0;a=[]
    for x in word:
        assert abs(x)!=6
        if abs(x)==2:parity^=1
        else:a.append(((abs(x),parity),1 if x>0 else -1))
    return graph_reduce(a),parity
def bmul(*bs):
    parity=0;a=[]
    for letters,p in bs:
        a.extend((((v[0],v[1]^parity),sign) for v,sign in letters))
        parity^=p
    return graph_reduce(a),parity
def bword(b):
    letters,p=b;ans=[]
    for (i,side),sign in letters:
        ans.extend((2,sign*i,2) if side else (sign*i,))
    if p:ans.append(2)
    return red(ans)
def clique(b,vertices):
    letters,p=b
    if p or any(v not in vertices for v,sign in letters):return None
    return tuple(sum(sign for v,sign in letters if v==u) for u in vertices)
def coordinate(ex,vertices):
    return graph_reduce([(v,1 if n>0 else -1)
                         for v,n in zip(vertices,ex) for _ in range(abs(n))]),0

# The literal root stable letter obeys w p w^-1=e and
# w r w^-1=bar_b; it is the inverse of A's auxiliary stable letter.
src=((7,0),(8,0));dst=((5,0),(3,1))
def evaluate(word):
    bases=[];signs=[];piece=[]
    for x in word:
        if abs(x)==6:
            bases.append(parse_base(piece));piece=[]
            signs.append(1 if x>0 else -1)
        else:piece.append(x)
    bases.append(parse_base(piece));pinches=[]
    while True:
        found=None
        for k in range(len(signs)-1):
            if signs[k+1]!=-signs[k]:continue
            frm,to=(src,dst) if signs[k]>0 else (dst,src)
            ex=clique(bases[k+1],frm)
            if ex is not None:found=(k,frm,to,ex);break
        if found is None:break
        k,frm,to,ex=found
        pinches.append({'position':k,'sign':signs[k],
                        'middle':bword(bases[k+1]),'exponents':ex})
        bases[k:k+3]=[bmul(bases[k],coordinate(ex,to),bases[k+2])]
        signs[k:k+2]=[]
    blockers=[]
    for k in range(len(signs)-1):
        if signs[k+1]!=-signs[k]:continue
        vertices=src if signs[k]>0 else dst
        assert clique(bases[k+1],vertices) is None
        blockers.append({'position':k,'middle':bword(bases[k+1]),
                         'excluded_clique':vertices,
                         'parity':bases[k+1][1],
                         'outside_support':[v for v,s in bases[k+1][0] if v not in vertices]})
    return {'trivial':not signs and bases[0]==((),0),
            'stable_signs':signs,'base_words':[bword(b) for b in bases],
            'pinches':pinches,'Britton_blockers':blockers}

old_new={int(k):tuple(v) for k,v in N['old_in_new'].items()}
f_w={j:(j,) for j in range(1,7)}
f_w[6]=tuple(H['branch_f_in_new_generators'])
def convert(w):return sub(sub(w,old_new),f_w)
assert evaluate((6,7,-6,-5))['trivial']
assert evaluate((6,8,-6,2,-3,2))['trivial']
relations=[(l['name'],n['physical_labels'],n['relation'])
           for l in D['loops'][1:] for n in l['nodes']]
assert len(relations)==10
for name,labels,w in relations:assert evaluate(convert(w))['trivial']

rows=[]
for direction,field in [('positive','positive_push'),('negative','negative_pull')]:
    A={int(k):tuple(v) for k,v in D['loops'][0][field].items()}
    for name,labels,w in relations:
        image=sub(w,A);value=evaluate(convert(image))
        expected=next(r for r in CE['results']
                      if r['direction']==direction and r['loop_name']==name
                      and r['physical_labels']==labels)
        assert list(image)==expected['actual_raw_image']
        assert value['trivial']==expected['normal_form']['trivial']
        rows.append({'direction':direction,'loop_name':name,'physical_labels':labels,
                     'normal_form':value})
for direction in ('positive','negative'):
    selected=[r for r in rows if r['direction']==direction]
    assert sum(not r['normal_form']['trivial'] for r in selected)==9
witness=next(r for r in rows if r['direction']=='negative' and r['loop_name']=='beta_33')
assert len(witness['normal_form']['stable_signs'])==2
assert len(witness['normal_form']['pinches'])==3

out={'status':'PASS','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in paths},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'method':'Independent commuting-suffix graph reduction and exact coordinate-clique Britton reduction',
     'original_ten_relators_trivial':True,'twenty_actual_images':rows,
     'small_negative_beta33_witness':witness,
     'scope':'The actual q0 saturation strictly adds relations to this slit group. '
             'No failure of the annular fixed-source question is inferred.'}
Path(__file__).with_name('inner_q0_HNN_independent22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all10 original relators and all20 actual q0 signed images.')
print('PASS9 nontrivial images in each direction by exact Britton normal form.')
print('PASS negative beta33 has2 stable letters after3 pinches; slit-to-annulus kernel is nontrivial.')
