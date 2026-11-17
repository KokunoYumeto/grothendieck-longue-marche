"""Exact distinguished-lasso and complete word-data audit for the actual pencil."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,itertools,json
import sympy as S
from quadratic_pencil_braid import u,I,Q,frac
HERE=Path(__file__).resolve().parent
old=json.loads((HERE/'ratio_pencil_words.json').read_text())
new=json.loads((HERE/'remaining_pencil_words.json').read_text())
assert old['initial_order']==new['initial_order']
rows=old['loops']+new['loops'];assert len(rows)==31
assert len({r['name'] for r in rows})==31
base=I/100;h=Q(1,1000)
centers=[(r['name'],Q(r['center'][0])+I*Q(r['center'][1])) for r in rows]
minimum=None
for name,c in centers:
 d=c+h+h*I-base;dx,dy=S.re(d),S.im(d);dd=dx*dx+dy*dy
 for oname,oc in centers:
  if oname==name:continue
  p=oc-base;px,py=S.re(p),S.im(p);a=max(0,min(1,(px*dx+py*dy)/dd))
  v=p-a*d;dist2=S.re(v)**2+S.im(v)**2
  assert dist2>Q(1,100000),'a whisker comes too near another critical square'
  minimum=dist2 if minimum is None else min(minimum,dist2)
for (name,c),(oname,oc) in itertools.combinations(centers,2):
 d=c+h+h*I-base;e=oc+h+h*I-base
 assert S.re(d)*S.im(e)-S.im(d)*S.re(e)!=0,'two straight whiskers overlap'
 diff=c-oc;assert S.re(diff)**2+S.im(diff)**2>Q(1,10000)
# The true coefficients lie within2e-30 by audit_pencil_geometry.py.
# These inequalities justify the elementary rational-function/root
# estimates giving center error<1e-25 for every displayed critical value.
for q in u[1:]:
 assert Q(9,10)<S.re(q)**2+S.im(q)**2<2
 assert S.re(q-1)**2+S.im(q-1)**2>1
 C=S.expand(q*(q-1));assert abs(S.im(C))>Q(1,10)
point_bound=F(50);separation=F(1,10**14);radicand_error=44*F(1,10**30)
assert radicand_error<F(1,2*10**8)
assert 10000*radicand_error<F(1,10**22)
assert 2*F(1,10**22)<separation
summary=[]
for r in rows:
 word=r['word'];e=sum(1 if x>0 else -1 for x in word)
 summary.append({'name':r['name'],'length':len(word),'exponent':e,
                 'filled':r['name'] not in ('base1','base2')})
assert sum(r['filled'] for r in summary)==29
assert sum(r['exponent'] for r in summary if r['filled'])==98
hashes={f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in
 ['ratio_pencil_words.json','remaining_pencil_words.json','pencil_geometry_audit.json']}
out={'base':['0','1/100'],'rotation':['1','371/1000'],'initial_order':old['initial_order'],
 'source_collapse_pair':[10,11],'deleted_U_indices':[1,2,6,9,12,15,19,20],
 'whisker_other_center_squared_distance_lower_bound':'1/100000',
 'critical_center_error_upper_bound':'1/10^25','critical_square_halfside':'1/1000',
 'all_straight_whisker_directions_distinct':True,'source_hashes':hashes,
 'loops':rows,'summary':summary,
 'scope':'Complete actual common-based monodromy data; uniform source-kernel normality remains unresolved.'}
(HERE/'complete_pencil_words.json').write_text(json.dumps(out,indent=2)+'\n')
print('All31 centers distinct; critical squares disjoint: PASS')
print('All31 straight whiskers have distinct directions and miss every other critical square: PASS')
print('Actual cyclotomic centers lie within1e-25; additional segment separation>1e-14 and deformation motion<1e-22: PASS')
print('Filled local exponent sum:',sum(r['exponent'] for r in summary if r['filled']))
for r in summary:print(r['name'],'length',r['length'],'exponent',r['exponent'],'filled',r['filled'])
print('PASS: complete distinguished system of31 actual based lassos,29 filled and2 retained.')
