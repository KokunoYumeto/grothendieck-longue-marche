#!/usr/bin/env python3
"""Independent word-substitution verification of stored symmetric braids.
Does not import or execute the crossing producer.
"""
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'next_symmetric_nodes'
inp=P/(sys.argv[1] if len(sys.argv)>1 else 'symmetric_node_words.json')
D=json.loads(inp.read_text());n=len(D['labels'])
def reduce(w):
 stack=[]
 for x in w:
  if stack and stack[-1]+x==0:stack.pop()
  else:stack.append(x)
 return tuple(stack)
def inverse(w):return tuple(-x for x in reversed(w))
def local_image(x,g):
 j=abs(g)
 if g>0:
  v=(j,j+1,-j) if abs(x)==j else (j,) if abs(x)==j+1 else (abs(x),)
 else:
  v=(j+1,) if abs(x)==j else (-j-1,j,j+1) if abs(x)==j+1 else (abs(x),)
 return v if x>0 else inverse(v)
def braid_on_word(beta,w):
 for g in reversed(beta):w=reduce(y for x in w for y in local_image(x,g))
 return w
def subst(w,images):return reduce(y for x in w for y in (images[abs(x)] if x>0 else inverse(images[abs(x)])))
rows=[]
for row in D['loops']:
 b=tuple(row['word']);W=tuple(row['whisker']);std=tuple(row['standard_local_braid'])
 expected=W+std+inverse(W)
 A={i:braid_on_word(b,(i,)) for i in range(1,n+1)}
 Ai={i:braid_on_word(inverse(b),(i,)) for i in range(1,n+1)}
 Wh={i:braid_on_word(W,(i,)) for i in range(1,n+1)}
 for i in range(1,n+1):
  assert A[i]==braid_on_word(expected,(i,))
  assert subst(A[i],Ai)==(i,)==subst(Ai[i],A)
 assert subst(tuple(range(1,n+1)),A)==tuple(range(1,n+1))
 for node in row['nodes']:
  j,k=node['local_positions']
  aa,bb=Wh[j],Wh[k]
  assert aa==tuple(node['meridians'][0]) and bb==tuple(node['meridians'][1])
  assert reduce(aa+bb+inverse(aa)+inverse(bb))==tuple(node['commutator'])
  for v,c,core in zip((aa,bb),node['conjugators'],node['cores']):
   assert reduce(tuple(c)+(core,)+inverse(c))==v
  tags=[D['labels'][x] for x in node['physical_labels']]
  assert {t['kind'] for t in tags}=={'A','B'}
  assert node['physical_labels']==[D['initial_order'][x-1] for x in node['cores']]
 perm=list(D['initial_order']);cross={}
 for g in b:
  j=abs(g)-1;key=tuple(sorted(perm[j:j+2]));cross[key]=cross.get(key,0)+(1 if g>0 else -1)
  perm[j:j+2]=reversed(perm[j:j+2])
 assert perm==D['initial_order']
 assert {k:v for k,v in cross.items() if v}=={tuple(x['labels']):x['crossing_sum'] for x in row['pair_linking_twice']}
 assert sum(1 if g>0 else -1 for g in b)==row['expected_exponent']==2*len(row['nodes'])
 rows.append({'index':row['index'],'basis_images_checked':n,'node_transports_checked':len(row['nodes']),
  'word_length':len(b),'exponent':row['expected_exponent']})
 print('PASS independent substitution, inverse, boundary, transports, linking:',row['index'],flush=True)
out={'input':str(inp.relative_to(ROOT.parent)),'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
 'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':rows,
 'scope':'Independent discrete braid-word check; geometric interval and coefficient-deformation certificates are separate.'}
(P/(inp.stem+'_independent_verification.json')).write_text(json.dumps(out,indent=2)+'\n')
print('PASS all',len(rows),'stored nodal braids; total node transports',sum(r['node_transports_checked'] for r in rows),flush=True)
