"""Exact mod-two central-square variation in the new free cusp basis.
Uses the executed integral affine preparation. Does not infer a norm
obstruction if this restricted variation has deficient rank.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):P=runpy.run_path(str(HERE/'prepare_Q6_integral_affine.py'))
G=P['G'];fm=G['fm'];fva=G['fva'];flin=G['flin'];kzero=(0,)*36
red=P['red'];JF=[tuple(red(x)for x in v)for v in P['JF']]
chars=G['chars'];idx={v:i for i,v in enumerate(chars)}
partner=[idx[G['sm'](6,v)]for v in chars]
vpairs=[(i,j)for i,j in enumerate(partner)if i<j]
assert len(vpairs)==18
zpairs=[(i,j)for i in range(4)for j in range(i+1,4)]
a=[flin(G['BETA'],tuple(red(x)for x in P['TCOR'][i]))for i in range(4)]
assert all(a[i]==flin(G['CV'],tuple(red(x)for x in P['TCOR'][i]))for i in range(4))
def pairing(v,w):
 z=0
 for p,q in vpairs:z^=fm(v[p],w[q])^fm(w[p],v[q])
 return z
def variation(u):
 return tuple(pairing(u[i],a[j])^pairing(u[j],a[i])for i,j in zpairs)
cols=[];labels=[]
for r in range(4):
 for j,v in enumerate(JF):
  u=[kzero]*4;u[r]=v;cols.append(variation(u));labels.append((r,j))
rk=G['frank'](cols)
print('Joint fixed scalar-vector dimension overF8:',len(JF))
print('Allowed doubled free-cusp corrections:',len(cols),'overF8')
print('Target new center Lambda2(F8^4) dimension:',len(zpairs))
print('Exact central-square variation rank overF8:',rk)
print('All transformed old t0 rows lie in the certified joint invariants: PASS')
print('Restricted correction images:',cols)
print('Scope: restricted homogeneous corrections only; deficient rank is not a norm obstruction.')
out={'rank_over_F8':rk,'target_dimension_F8':6,'source_dimension_F8':48,'labels':labels,'columns':cols,'a':a,'joint_fixed_basis':JF,'opposite_weight_pairs':vpairs}
(HERE.parent/'Q6_new_center_variation.json').write_text(json.dumps(out,indent=2))
# Additional doubled positive-inner variations. Keep the actual cusp
# commutator constraint at the new center, not merely head invariance.
TFk=[tuple(red(x)for x in v)for v in P['I']['TF']]
q=[tuple(red(x)for x in v)for v in P['QO']]
tau=[tuple(red(x)for x in P['app'](P['SO'],v))for v in P['RF']]
def commrows(u,v):return tuple(pairing(u[i],v[j])^pairing(u[j],v[i])for i,j in zpairs)
pcols=[];cuspcols=[];plabels=[]
for r in range(4):
 for j,v in enumerate(TFk):
  w=[kzero]*4;w[r]=v
  pcols.append(commrows(w,q));cuspcols.append(commrows(w,tau));plabels.append((r,j))
ck=G['fkernel'](cuspcols)
assert all(flin(cuspcols,v)==(0,)*6 for v in ck)
constrained=[flin(pcols,v)for v in ck]
print('Doubled positive tau-invariant source dimension:',len(pcols))
print('Positive norm variation rank before cusp constraint:',G['frank'](pcols))
print('Actual new-center cusp commutator rank:',G['frank'](cuspcols))
print('Cusp-preserving positive correction dimension:',len(ck))
print('Positive norm variation rank after cusp constraint:',G['frank'](constrained))
print('Combined s-frame + positive variation rank before/after cusp constraint:',G['frank'](cols+pcols),G['frank'](cols+constrained))
out.update({'positive_norm_columns':pcols,'positive_cusp_commutator_columns':cuspcols,'positive_cusp_kernel':ck,'positive_norm_after_cusp_columns':constrained,'positive_labels':plabels,'combined_rank_after_cusp':G['frank'](cols+constrained)})
(HERE.parent/'Q6_new_center_variation.json').write_text(json.dumps(out,indent=2))
combined=cols+constrained
ann=G['fkernel']([tuple(col[j]for col in combined)for j in range(6)])
print('Combined-image annihilator columns, center order(01,02,03,12,13,23):',ann)
out['combined_image_annihilator']=ann
(HERE.parent/'Q6_new_center_variation.json').write_text(json.dumps(out,indent=2))
