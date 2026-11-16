"""Finite elementary simplicity check for the actual projective rigid image."""
from pathlib import Path
import json,time
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent
j=json.loads((HERE/'rigid_restrictions.json').read_text())
G=PermutationGroup([Permutation(r['permutation']) for r in j['families']['plus'].values()])
assert G.order()==25920
t=time.time();classes=G.conjugacy_classes();record=[]
assert sum(len(c) for c in classes)==G.order()
for c in classes:
    r=min(c,key=lambda a:tuple(a.array_form))
    if r.is_Identity:continue
    N=G.normal_closure([r]);n=N.order()
    assert n==G.order()
    record.append({'class_size':len(c),'representative':r.array_form,'element_order':int(r.order()),'normal_closure_order':int(n)})
    print('class',len(c),'order',r.order(),'normal closure',n,flush=True)
assert G.derived_subgroup().order()==G.order()
(HERE/'simple_certificate.json').write_text(json.dumps({'group_order':int(G.order()),'conjugacy_class_sizes':sorted(len(c) for c in classes),'nontrivial_class_representatives':record,'seconds':time.time()-t},indent=2)+'\n')
print('PASS every nontrivial conjugacy class normally generates the actual rigid image; it is nonabelian simple',flush=True)
print('elapsed',round(time.time()-t,3),flush=True)
