#!/usr/bin/env python3
"""Literal cone normalization of the complete inner regional presentation.

All rewrites are in C2*F5.  The five ordinary initial generators retain
their actual first-neck marking.  A later triangular basis change is
explicit and is NOT asserted to preserve that subgroup.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
path=P/'inner_bad_orbifold_words22.json';D=json.loads(path.read_text());C=2
def inverse(w):return tuple(C if abs(x)==C else -x for x in reversed(w))
def red(w):
 out=[]
 for x in w:
  x=C if abs(x)==C else int(x)
  if out and (out[-1]==-x or out[-1]==x==C):out.pop()
  else:out.append(x)
 return tuple(out)
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,A):return mul(*(A[abs(x)] if x>0 or abs(x)==C else inverse(A[-x]) for x in w))
def comm(a,b):return mul(a,b,inverse(a),inverse(b))
def peel(w):
 w=list(red(w));h=[]
 while len(w)>1 and inverse([w[0]])[0]==w[-1]:h.append(w.pop(0));w.pop()
 return tuple(h),tuple(w)
def cyclic(w):
 h,r=peel(w);assert mul(h,r,inverse(h))==red(w);return h,r
def ordinary(w):
 positions={1:1,4:2,5:3,3:4,6:5};at=0;out=[]
 for x in red(w):
  if abs(x)==C:at^=1
  else:out.append((1 if x>0 else -1)*(positions[abs(x)]+5*at))
 assert at==0
 r=[]
 for x in out:
  if r and r[-1]==-x:r.pop()
  else:r.append(x)
 return tuple(r)
def lift_ordinary(w):
 positions={1:1,2:4,3:5,4:3,5:6}
 out=[]
 for x in w:
  j=(abs(x)-1)%5+1;e=int(abs(x)>5);a=positions[j]*(1 if x>0 else -1)
  out.extend([C,a,C] if e else [a])
 return red(out)

# New generator order is unchanged: A1,c,A4,A2,A3,P.
new_in_old={1:(1,),2:(2,),3:(-1,3,1),
 4:(2,1,2,3,4,-3,2,-1,2),5:(-1,3,5,-3,1),6:(6,)}
old_in_new={1:(1,),2:(2,),3:(1,3,-1),
 4:(1,-3,-1,2,-1,2,4,2,1,2,1,3,-1),5:(1,-3,5,3,-1),6:(6,)}
for j in range(1,7):
 assert sub(new_in_old[j],old_in_new)==(j,)
 assert sub(old_in_new[j],new_in_old)==(j,)

def fred(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def candidate_normal_form(w):
 """Exact normal form in (F(A1..4) x F(B1..4))*F(P,Q)."""
 stack=[]
 for x in w:
  kind='branch' if abs(x) in (5,10) else 'product'
  if not stack or stack[-1][0]!=kind:
   stack.append((kind,(),()) if kind=='product' else (kind,()))
  item=stack.pop()
  if kind=='branch':
   z=fred(item[1]+(x,))
   if z:stack.append((kind,z))
  else:
   a,b=item[1:]
   if abs(x)<5:a=fred(a+(x,))
   else:b=fred(b+(x,))
   if a or b:stack.append((kind,a,b))
 return stack

rows=[];normalized_cones={}
for L in D['loops'][1:]:
 for n in L['nodes']:
  original=red(n['relation']);changed=sub(original,old_in_new)
  h,core=cyclic(changed);ow=ordinary(core)
  assert lift_ordinary(ow)==core
  record={'loop_index':L['index'],'loop_name':L['name'],'physical_labels':n['physical_labels'],
   'kind':n['kind'],'original_relation_mod_cone_square':original,
   'new_relation':changed,'cyclic_conjugator':h,'cyclic_core':core,
   'ordinary_core':ow,'ordinary_labels':['A1','A2','A3','A4','P','B1','B2','B3','B4','Q'],
   'product_free_branch_candidate_normal_form':candidate_normal_form(ow)}
  if n['kind']=='cone_contact':
   a,b=n['meridians'];cone,p=(a,b) if n['physical_labels'][0]==0 else (b,a)
   d,cone_core=peel(cone);assert cone_core==(C,)
   qp=mul(inverse(d),p,d);g,p_core=peel(qp)
   if sum(abs(x)==C for x in g)%2:qp=mul((C,),qp,(C,))
   physical=next(x for x in n['physical_labels'] if x!=0)
   j=D['initial_physical_order'].index(physical)+1
   assert qp==new_in_old[j],(physical,qp,new_in_old[j])
   normalized_cones[j]=qp
   record['normalized_deleted_meridian']=qp
   record['standard_new_relation']=comm((j,),(C,j,C))
   assert candidate_normal_form(ordinary(changed))==[]
  rows.append(record)
assert len(rows)==10 and len(normalized_cones)==4
out={'status':'PASS','input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'cone_generator':C,'new_generators_in_old':new_in_old,'old_generators_in_new':old_in_new,
 'both_inverse_substitutions':12,'relations':rows,
 'scope':'Exact complete regional relation normalization; a failed naive product test only concerns this specified normalized marking.'}
(P/'inner_bad_normalized_relations22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:12 inverse substitutions;10 complete based relations;4 normalized cone contacts.')
for r in rows:
 print(r['loop_name'],r['physical_labels'],'ordinary',r['ordinary_core'],
       'candidate',r['product_free_branch_candidate_normal_form'])
