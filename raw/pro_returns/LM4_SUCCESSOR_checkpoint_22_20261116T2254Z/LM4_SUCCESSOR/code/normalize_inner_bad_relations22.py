"""Exact marked Nielsen change for the complete rational regional relation data.

This algebra does not supply the separate deformation-to-cyclotomic proof.
Words are in C2(x2)*F(x1,x3,x4,x5,x6); x2 has order two.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json'
D = json.loads(SOURCE.read_text())
assert D['status'] == 'PASS' and D['cone_generator'] == 2

def red(word):
    out = []
    for a in word:
        a = 2 if abs(a) == 2 else a
        if out and (out[-1] == -a or out[-1] == a == 2):
            out.pop()
        else:
            out.append(a)
    return tuple(out)

def mul(*words):
    return red(a for word in words for a in word)

def inv(word):
    return red(-a for a in reversed(word))

def conj(g,w):
    return mul(g,w,inv(g))

def sub(word,images):
    return mul(*(images[abs(a)] if a>0 else inv(images[abs(a)]) for a in word))

def comm(a,b):
    return mul(a,b,inv(a),inv(b))

def cyclic(word):
    out = list(red(word))
    conjugator = []
    while len(out)>1 and (out[0] == -out[-1] or out[0] == out[-1] == 2):
        conjugator.append(out.pop(0))
        out.pop()
    return tuple(conjugator),tuple(out)

def peripheral(word):
    g,w = cyclic(word)
    assert len(w)==1
    return g,w[0]

old = {i:(i,) for i in range(1,7)}
# New labels retain the old physical positions: 1=A1, 2=cone,
# 3=A4, 4=A2, 5=A3, 6=retained branch.
new_in_old = {
    1:(1,), 2:(2,),
    3:conj((-1,),(3,)),
    4:conj((2,1,2,3),(4,)),
    5:conj((-1,3),(5,)),
    6:(6,)
}
old_in_new = {1:(1,),2:(2,),6:(6,)}
old_in_new[3] = conj((1,),(3,))
old_in_new[4] = conj(mul(inv(old_in_new[3]),(2,-1,2)),(4,))
old_in_new[5] = conj(mul(inv(old_in_new[3]),(1,)),(5,))
for i in range(1,7):
    assert sub(new_in_old[i],old_in_new) == (i,)
    assert sub(old_in_new[i],new_in_old) == (i,)
for i in (1,3,4,5,6):
    g,k=peripheral(new_in_old[i])
    assert sum(abs(a)==2 for a in g)%2==0, 'Chosen peripheral changes the lift sheet'

rows=[]
for loop in D['loops']:
    if loop['name']=='q0':
        continue
    for node in loop['nodes']:
        raw = tuple(node['relation'])
        new = sub(raw,old_in_new)
        whole_conjugator,cyclic_new = cyclic(new)
        a,b = [sub(w,old_in_new) for w in node['meridians']]
        row = dict(name=loop['name'],kind=node['kind'],physical_labels=node['physical_labels'],
                   old_relation=raw,new_relation=new,whole_conjugator=whole_conjugator,
                   cyclic_new=cyclic_new,new_meridians=[a,b])
        if node['kind']=='cone_contact':
            cone,p = (a,b) if node['physical_labels'][0]==0 else (b,a)
            g,k = peripheral(cone)
            assert k==2
            normalized_p = conj(inv(g),p)
            expected_index = {2:1,3:4,4:5,5:3}[next(x for x in node['physical_labels'] if x)]
            if normalized_p == (2,expected_index,2):
                g=mul(g,(2,))
                normalized_p=conj(inv(g),p)
            assert normalized_p == (expected_index,),(loop['name'],normalized_p)
            expected = comm(normalized_p,conj((2,),normalized_p))
            assert conj(inv(g),new)==expected
            row.update(cone_conjugator=g,normalized_peripheral=normalized_p,
                       normalized_cone_relation=expected)
        else:
            ga,ka=peripheral(a)
            aa=(ka,)
            bb=conj(inv(ga),b)
            ga2,cyclic_b=cyclic(bb)
            assert len(cyclic_b)==1
            gb,kb=ga2,cyclic_b[0]
            row.update(common_conjugator=ga,first_core=ka,relative_conjugator=gb,
                       second_core=kb,normalized_pair_relation=comm(aa,bb))
            assert conj(inv(ga),new)==row['normalized_pair_relation']
        rows.append(row)

out={'status':'PASS','scope':__doc__,
     'source':str(SOURCE.relative_to(ROOT)),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
     'new_in_old':new_in_old,'old_in_new':old_in_new,
     'two_sided_generator_inverses':'PASS','all_four_cone_relations':'PASS',
     'all_five_peripheral_conjugators_preserve_cover_character':'PASS',
     'relations':rows}
(ROOT/'records/inner_bad_normalized22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS two-sided marked generator substitution and four exact cone normalizations')
for row in rows:
    if row['kind']=='ordinary_node':
        print(row['name'],'pair',row['first_core'],row['second_core'],
              'relative conjugator',row['relative_conjugator'])
