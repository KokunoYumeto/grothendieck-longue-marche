#!/usr/bin/env python3
"""Exact retained-q0 comparison in the proved regional HNN extension.

This uses the actual positive/negative q0 operators, both marked changes,
the full twelve-vertex graph-group word problem and Britton's lemma.
Every pinch records its actual coordinate-clique exponent pair.  No
finite subgroup or bounded orbit membership heuristic is involved.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
D=json.loads((P/'inner_bad_orbifold_words22.json').read_text())
N=json.loads((ROOT/'records/inner_bad_normalized22.json').read_text())
H=json.loads((ROOT/'records/inner_bad_hnn22.json').read_text())
def red(w):
 out=[]
 for x in w:
  x=2 if abs(x)==2 else int(x)
  if out and (out[-1]==-x or out[-1]==x==2):out.pop()
  else:out.append(x)
 return tuple(out)
def mul(*ws):return red(x for w in ws for x in w)
def inv(w):return red(-x for x in reversed(w))
def sub(w,A):return mul(*(A[abs(x)] if x>0 else inv(A[-x]) for x in w))
old_new={int(k):tuple(v) for k,v in N['old_in_new'].items()}
new_hnn={i:(i,) for i in range(1,7)};new_hnn[6]=tuple(H['branch_f_in_new_generators'])
def convert(w):return sub(sub(w,old_new),new_hnn)
V=tuple(tuple(v) for v in H['base_vertices']);ED={frozenset(map(tuple,e)) for e in H['base_edges']}
NON={v:tuple(u for u in V if u!=v and frozenset((u,v)) not in ED) for v in V}
def raag_normal(letters):
 stacks={v:[] for v in V}
 for v,sgn in letters:
  if stacks[v] and stacks[v][-1]==-sgn:
   stacks[v].pop()
   for u in NON[v]:assert stacks[u] and stacks[u].pop()==0
  else:
   stacks[v].append(sgn)
   for u in NON[v]:stacks[u].append(0)
 rev=[]
 while any(stacks.values()):
  v=next(v for v in V if stacks[v] and stacks[v][-1]!=0)
  s=stacks[v].pop();rev.append((v,s))
  for u in NON[v]:assert stacks[u] and stacks[u].pop()==0
 return tuple(reversed(rev))
def base_from_word(w):
 p=0;a=[]
 for x in w:
  assert abs(x)!=6
  if abs(x)==2:p^=1
  else:a.append(((abs(x),p),1 if x>0 else -1))
 return (raag_normal(a),p)
def base_mul(*vals):
 a=[];p=0
 for letters,q in vals:
  a.extend((((i,b^p),s) for (i,b),s in letters));p^=q
 return (raag_normal(a),p)
ONE=((),0)
def base_word(g):
 letters,p=g;w=[]
 for (i,b),s in letters:w.extend((2,s*i,2) if b else (s*i,))
 if p:w.append(2)
 return red(w)
def clique(g,vertices):
 letters,p=g
 if p or any(v not in vertices for v,s in letters):return None
 return tuple(sum(s for v,s in letters if v==x) for x in vertices)
src=((7,0),(8,0));dst=((5,0),(3,1))
def coordinate(vals,vertices):
 return (raag_normal([(v,1 if n>0 else -1) for n,v in zip(vals,vertices) for _ in range(abs(n))]),0)
def evaluate(word):
 bases=[];signs=[];w=[]
 for x in word:
  if abs(x)==6:bases.append(base_from_word(w));w=[];signs.append(1 if x>0 else -1)
  else:w.append(x)
 bases.append(base_from_word(w));steps=[]
 while True:
  choice=None
  for i in range(len(signs)-1):
   if signs[i+1]!=-signs[i]:continue
   frm,to=(src,dst) if signs[i]>0 else (dst,src)
   ex=clique(bases[i+1],frm)
   if ex is not None:choice=(i,ex,frm,to);break
  if choice is None:break
  i,ex,frm,to=choice;image=coordinate(ex,to)
  steps.append({'stable_position':i,'stable_sign':signs[i],
    'intervening_base_word':base_word(bases[i+1]),'clique_vertices':frm,
    'exponents':ex,'replacement_base_word':base_word(image)})
  merged=base_mul(bases[i],image,bases[i+2])
  bases[i:i+3]=[merged];signs[i:i+2]=[]
 assert len(bases)==len(signs)+1
 # Explicitly verify that every remaining opposite adjacent pair is
 # outside its relevant coordinate clique, the exact Britton gate.
 remaining=[]
 for i in range(len(signs)-1):
  if signs[i+1]!=-signs[i]:continue
  frm=src if signs[i]>0 else dst
  assert clique(bases[i+1],frm) is None
  remaining.append({'stable_position':i,'base_word':base_word(bases[i+1]),'excluded_clique':frm})
 return {'trivial':not signs and bases[0]==ONE,'stable_signs':signs,
  'base_words':[base_word(g) for g in bases],'pinches':steps,
  'remaining_nonmembership_certificates':remaining}

# Check both HNN identifications and coordinate-base inputs independently.
assert evaluate((6,7,-6,-5))['trivial']
assert evaluate((6,8,-6,2,-3,2))['trivial']
for e in ED:
 a,b=sorted(e);aa=base_word((((a,1),),0));bb=base_word((((b,1),),0))
 assert evaluate(mul(aa,bb,inv(aa),inv(bb)))['trivial']
started=time.monotonic();results=[]
rels=[(l['name'],n['physical_labels'],tuple(n['relation'])) for l in D['loops'][1:] for n in l['nodes']]
for name,labels,r in rels:assert evaluate(convert(r))['trivial'],('original relator did not vanish',name,labels)
q0=D['loops'][0]
for direction,field in [('positive','positive_push'),('negative','negative_pull')]:
 A={int(k):tuple(v) for k,v in q0[field].items()}
 for name,labels,r in rels:
  image=sub(r,A);word=convert(image);nf=evaluate(word)
  results.append({'direction':direction,'loop_name':name,'physical_labels':labels,
    'actual_raw_image':image,'HNN_word':word,'normal_form':nf})
  print(direction,name,labels,'TRIVIAL' if nf['trivial'] else 'NONTRIVIAL',
        'input',len(word),'stable',len(nf['stable_signs']),'pinches',len(nf['pinches']),flush=True)
out={'status':'PASS','elapsed_seconds':time.monotonic()-started,
 'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [P/'inner_bad_orbifold_words22.json',ROOT/'records/inner_bad_normalized22.json',ROOT/'records/inner_bad_hnn22.json']},
 'all_original_ten_relators_checked':True,'results':results,
 'positive_preserves_all_ten':all(r['normal_form']['trivial'] for r in results if r['direction']=='positive'),
 'negative_preserves_all_ten':all(r['normal_form']['trivial'] for r in results if r['direction']=='negative'),
 'scope':'Exact single retained-operator normal-form test. Nontrivial output proves an additional annular relation, not failure of the global main theorem.'}
(P/'inner_q0_HNN22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete twenty-image comparison',round(out['elapsed_seconds'],6),'seconds',flush=True)
