#!/usr/bin/env python3
"""Independent three-bridge/static-filling audit; no CE producer imported."""
from pathlib import Path
import json, hashlib, time
H=Path(__file__).resolve().parent
R=H.parents[1]
# Reuse the owned independently derived rational quadratic crossing routine.
# Execute its definitions only, before its lasso evaluation or any output write.
defs=(H/'verify_retained_section_kernel_braids.py').read_text().split("for row in d['loops']:",1)[0]
exec(compile(defs,str(H/'verify_retained_section_kernel_braids.py'),'exec'))
p=R/'work_CE/next_symmetric_nodes/all_diagonal_section_transports.json'
data=json.loads(p.read_text())
st=json.loads((H/'old_lassos_far_cut_conversion.json').read_text())
old_to_cut=mp(st['forward_old_to_far'])
cut_to_old=mp(st['inverse_far_to_old'])
cut_labels=st['far_cut_physical_old_indices']
physical_label={1:2,2:0,3:3,4:1}
expected={1:((2,),(4,),(1,),(-1,3,1),(),()),
          2:((2,),(4,),(),(1,),(),(3,)),
          3:((2,),(4,),(3,),(),(-3,1,3),()),
          4:((2,),(4,),(),(),(3,),(1,))}
ref={row['name']:row for row in d['loops']}
I={j:(j,) for j in range(1,5)}
checks=[]
for row in data['rows']:
    n=row['u_exponent']
    if n==2:
        W=();A=B=I;order=d['initial_order']
    else:
        W=segment(row['bridge_segment'])
        A=push(W);B=push(iv(W));order=row['bridge_segment']['final_order']
    assert A==mp(row['geometric_push']) and B==mp(row['geometric_pullback'])
    # A is geometric forward push. End meridians pull back by B.
    back={i:B[order.index(label)+1] for i,label in physical_label.items()}
    endpoint={j+1:(next(i for i,label0 in physical_label.items() if label0==label),) for j,label in enumerate(order)}
    forward={i:sub(A[i],endpoint) for i in range(1,5)}
    assert back==mp(row['physical_to_reference'])
    assert forward==mp(row['reference_to_physical'])
    for i in range(1,5):assert sub(back[i],forward)==sub(forward[i],back)==(i,)
    kept={0:2,1:4,n+1:1,((2*n)%5)+1:3}
    filling={j+1:((kept[label],) if label in kept else ()) for j,label in enumerate(cut_labels)}
    phi={i:sub(old_to_cut[i],filling) for i in range(1,7)}
    assert tuple(phi[i] for i in range(1,7))==expected[n]
    assert phi==mp(row['old_to_physical_four'])
    allref={i:sub(phi[i],back) for i in range(1,7)}
    assert allref==mp(row['old_to_reference_four'])
    lifts={physical:cut_to_old[cut_labels.index(label)+1] for label,physical in kept.items()}
    for i in range(1,5):assert sub(lifts[i],phi)==(i,)
    delta={1:(),2:(1,),3:(),4:(2,)}
    for i in range(1,5):assert sub(back[i],delta)==delta[i]
    for name in ('v0','v1'):
        for key in ('geometric_push','geometric_pullback'):
            op=mp(ref[name][key])
            transported={i:sub(sub(back[i],op),forward) for i in range(1,5)}
            stored='push' if key=='geometric_push' else 'pullback'
            assert transported==mp(row['transported_retained_operators'][name][stored])
    node=sub((3,4,-3,-4),forward)
    oldnode=sub(node,lifts)
    assert oldnode==tuple(row['transported_node_relator_old'])
    assert sub(oldnode,allref)==(3,4,-3,-4)
    # Direct rational distance minimization; no producer bounds trusted.
    a,b=[tuple(map(Q,z)) for z in row['bridge_vertices']]
    v=add(b,sc(-1,a));vv=sum(x*x for x in v)
    for c in(-1,0,1):
        e=add(a,(-Q(c),Q(0)))
        x=max(Q(0),min(Q(1),-sum(e[j]*v[j] for j in range(2))/vv)) if vv else Q(0)
        assert sum((e[j]+x*v[j])**2 for j in range(2))>Q(1,10000)
    beta={1:(-1,),2:(4,),3:(5,),4:(2,),5:(3,)}
    for pr in row['two_actual_diagonal_rows']:
        rr=pr['row'];assert rr['A_slot']==rr['B_slot']
        z=tuple(rr['relative_retained_word']);assert mul(sub(z,beta),z)==()
    checks.append({'u_exponent':n,'independent_bridge_word':W,'static_filling':phi,
                   'end_to_reference':back,'old_to_reference':allref,'old_node_word':oldnode,
                   'both_Nielsen_directions':True,'critical_margin_strict':'1/100'})
    print('PASS independent bridge, physical pull, six-cut filling, operators, row condition:',n,flush=True)
out={'scope':'All eight diagonal zero-head kernels transported to B99; no literal nonzero-head equality or full-column claim.',
     'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'checks':checks,'independent_segment_checks':summ,'elapsed_seconds':time.monotonic()-start}
(H/'all_diagonal_section_transports_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all four static fillings and three exact polynomial bridges; seconds',round(out['elapsed_seconds'],3))
