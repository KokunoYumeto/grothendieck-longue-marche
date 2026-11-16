"""Intersect ordinary cubic and lower six-cup local s-frame gates.

Every candidate is evaluated in the actual class-two law with the stored
canonical-c source correction. No realizability of the finite local data
as a full profinite automorphism is inferred.
"""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
src=(HERE/'check_A66_W0_local_frames.py').read_text().split('records=[]')[0]
exec(compile(src,str(HERE/'check_A66_W0_local_frames.py'),'exec'))
ordinary=json.loads((HERE.parent/'A66_W0_local_frame_pairs.json').read_text())
cc=json.loads((HERE.parents[1]/'work_A/A63_zero_t_cross_cup_square.json').read_text())
pairs=[(i,j)for i in range(4)for j in range(i+1,4)]
B3=[tuple(pw(x,2)for x in col)for col in B]
C3=[tuple(pw(x,2)for x in col)for col in C]
ZZ=(zero,)*6
L=[row[:4]for row in cc['canonical_c_corrections']]
VC=tuple(tuple(row[8:])for row in cc['canonical_c_corrections'])
assert all(not any(row[4:8])for row in cc['canonical_c_corrections'])
def cup(a,b):
 return tuple(tuple(mul(x,y)for x,y in zip(a[i],b[j]))for i,j in pairs)
def j3(v):return tuple(pw(x,2)for x in v)
ONE=(AZ,ZZ,0)
B0=(wc,ZZ,1)
assert ca(ca(B0))==B0
baseline=gm(gi(B0),ca(gi(B0)))
assert baseline[0]==AZ and baseline[2]==0
print('Lower six-cup actual canonical-c baseline: PASS')
sp=[next(i for i,v in enumerate(col)if v)for col in S]
def vect(lam,bar,u,v):
 aa=[[0]*36 for _ in range(4)]
 for idx,vals in((lam,u),(bar,v)):
  for row,a in enumerate(vals):
   aa[row][idx]=a
   aa[row][sp[idx]]=mul(S[idx][sp[idx]],a)
 aa=tuple(map(tuple,aa))
 assert rowsop(S,aa)==aa and rowsop(B,rowsop(C,aa))==aa
 return aa
def local_norm(lam,bar,u,v):
 aa=vect(lam,bar,u,v)
 newB=gm(B0,(aa,ZZ,0))
 norm=gm(gi(newB),ca(gi(newB)))
 assert norm[0]==AZ and norm[2]==0
 return tuple((row[lam],row[bar],row[sp[lam]],row[sp[bar]])for row in norm[1])
records=[]
for rec in ordinary['records']:
 lam,bar=rec['lambda_weight'],rec['opposite_weight']
 allowed=[];rejected=[]
 for u,v in rec['right_corrections']:
  value=local_norm(lam,bar,u,v)
  (allowed if not any(any(row)for row in value)else rejected).append([u,v])
 print('Pair',lam,bar,'ordinary candidates',len(rec['right_corrections']),
       'joint lower+ordinary',len(allowed))
 records.append(dict(lambda_weight=lam,opposite_weight=bar,
   baseline_lower=[list(row)for row in local_norm(lam,bar,(0,)*4,(0,)*4)],
   right_corrections=allowed,rejected_by_lower=rejected))
partial=json.loads((HERE.parents[1]/'work_A/A66_zero_W_free_t_partial.json').read_text())
t=partial['normalized_cusp_frame_vectors'];tests=[]
for rec in records:
 lam,bar=rec['lambda_weight'],rec['opposite_weight']
 u=[row[bar]for row in t];v=[row[lam]for row in t]
 val=local_norm(lam,bar,u,v)
 good=[u,v]in rec['right_corrections']
 print('Partial tuple pair',lam,bar,'joint allowed',good,'lower norm',val)
 tests.append(dict(lambda_weight=lam,opposite_weight=bar,right_pair=[u,v],
                   joint_allowed=good,lower_norm=val))
out=dict(scope='Necessary simultaneous lower-six and ordinary-sixteen W0 local s-normalizer gates',
 records=records,partial_tuple_tests=tests,
 conversion='Actual t=p-wc is beta*u; beta swaps both displayed opposite pairs with scalar one',
 checks='Canonical-c source correction retained; each candidate evaluated in original lower law')
(HERE.parent/'A66_W0_joint_local_frame_pairs.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact simultaneous local gate: PASS')
