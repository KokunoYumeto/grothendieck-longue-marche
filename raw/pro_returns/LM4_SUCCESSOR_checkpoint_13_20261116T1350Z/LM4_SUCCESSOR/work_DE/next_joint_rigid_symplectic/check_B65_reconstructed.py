"""Fresh exact B65 certificate after the 2026-11-16 environment replacement.

Inputs are verified checkpoint-06 files.  This program does not reconstruct
old stdout: its output and certificate are newly computed.
"""
from pathlib import Path
import itertools, json

HERE=Path(__file__).resolve().parent
geom=json.loads((HERE.parent/'rigid7_subsets.json').read_text())
data=json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
previous=json.loads((HERE/'rigid_restrictions.json').read_text())
I=tuple(range(12));d=tuple(geom['D_permutation'])
T={tuple(x) for x in geom['T_permutations']}
r=list(I)
for a,b in [(1,3),(2,5),(6,8),(12,10),(9,11),(4,7)]:
    r[a-1],r[b-1]=b-1,a-1
r=tuple(r)
def comp(a,b):return tuple(a[b[i]] for i in range(12))
def power(a,k):
    out=I
    for _ in range(k):out=comp(out,a)
    return out
def closure(gens):
    seen={I};queue=[I]
    while queue:
        a=queue.pop()
        for g in gens:
            b=comp(g,a)
            if b not in seen:seen.add(b);queue.append(b)
    return seen
J=closure([d,r]);A5=closure(list(T)+[d,r])
assert r in T and len(T)==12 and len(J)==10 and len(A5)==60
assert T&J=={I,r}
assert comp(comp(r,d),r)==power(d,4)
print('Actual r belongs to T; |J|=10; T intersection J=<r>; |<T,J>|=60: PASS')
allsets={tuple(s) for s in geom['rigid7']}
def image(a,S):return tuple(sorted(a[i-1]+1 for i in S))
stable={s for s in allsets if image(d,s)==s}
assert stable=={(1,2,3,4,6,9,12),(1,3,5,7,8,10,11)}
plus=(1,2,4,5,6,10,11);minus=(2,3,4,7,10,11,12)
transports=[]
for refl in (False,True):
    for k in range(5):
        a=comp(power(d,k),r if refl else I)
        row={'power':k,'reflection':refl,'permutation':a,
             'subset':image(a,plus),'image_of_2':a[1]+1}
        transports.append(row)
assert {tuple(x['subset']) for x in transports}==allsets-stable
assert len({tuple(x['subset']) for x in transports})==10
a=comp(power(d,2),r)
assert image(a,plus)==minus and a[1]+1==11
print('All twelve rigid sets split as two D-stable sets and a regular J orbit of ten: PASS')
print('Transport d^2 r sends S+ to S- and omitted label 2 to label 11: PASS')
initial=data['initial_order_labels'];keep=set(plus)-{2}
order=[x for x in initial if x in keep]
assert order==[4,11,5,1,10,6]
def delete(w):
    state=initial[:];out=[]
    for a in w:
        j=abs(a)-1
        if state[j] in keep and state[j+1] in keep:
            q=sum(x in keep for x in state[:j])+1
            out.append(q if a>0 else -q)
        state[j],state[j+1]=state[j+1],state[j]
    assert state==initial
    return out
def links(w):
    state=order[:];L={p:0 for p in itertools.combinations(sorted(order),2)}
    for a in w:
        j=abs(a)-1;p=tuple(sorted(state[j:j+2]))
        L[p]+=1 if a>0 else -1
        state[j],state[j+1]=state[j+1],state[j]
    assert state==order and all(v%2==0 for v in L.values())
    return {','.join(map(str,p)):v//2 for p,v in L.items()}
records=[]
for i,w in sorted(data['C5'].items(),key=lambda z:int(z[0])):
    b=delete(w);L=links(b)
    assert b==previous['families']['plus'][i]['braid']
    assert L['4,6']==0
    records.append({'index':int(i),'braid':b,'length':len(b),
                    'exponent_sum':sum(1 if a>0 else -1 for a in b),'linking':L})
assert [x['length'] for x in records]==[36,34,22,30,54,32]
assert [x['exponent_sum'] for x in records]==[12,-10,4,-8,-8,4]
fulltwist=list(range(1,6))*6
assert links(fulltwist)['4,6']==1
print('Six fresh deletions equal the archived checkpoint-06 six-strand words: PASS')
print('Finite order:',order)
print('Unreduced lengths:',[x['length'] for x in records])
print('Exponent sums:',[x['exponent_sum'] for x in records])
print('All six braids pure; fixed-pair linking(4,6)=0; full-twist linking=1: PASS')
cert={'provenance':'Fresh reconstruction and computation against verified checkpoint-06 data',
      'r':r,'J_order':len(J),'A5_order':len(A5),'intersection':sorted(T&J),
      'stable_sets':sorted(stable),'transports':transports,'finite_order':order,'source_images':records}
(HERE/'B65_reconstructed_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
(HERE/'cyclic_rigid_braid_words.json').write_text(json.dumps({'finite_order':order,'basis':records},indent=2)+'\n')
print('PASS B65 finite permutation, exact word deletion, and central-factor certificates')
