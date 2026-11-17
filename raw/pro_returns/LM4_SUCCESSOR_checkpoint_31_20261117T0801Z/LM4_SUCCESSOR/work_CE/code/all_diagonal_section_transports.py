#!/usr/bin/env python3
"""Three actual four-strand bridges for all eight diagonal head kernels.

This is based transport of the complete B99 kernel, not an orbit search.
The v=u and w=u kernel equality uses the actual q-preserving swap on X0.
"""
from pathlib import Path
from fractions import Fraction
import json, hashlib, time
from retained_section_kernel_braids import Segment, S, u, art, sub, rmul, inv

ROOT=Path(__file__).resolve().parents[2]
CE=ROOT/'work_CE/next_symmetric_nodes'
DE=ROOT/'work_DE/next_marginal_source'
INPUT=CE/'retained_section_kernel_braids.json'
STATIC=DE/'old_lassos_far_cut_conversion.json'
PIVOTS=CE/'symmetric_G_augmentation_pivots.json'
D=json.loads(INPUT.read_text());ST=json.loads(STATIC.read_text())
pivots={tuple(r['node_index']):r['pivot_row'] for r in json.loads(PIVOTS.read_text())['pivots']}
old_to_cut={int(k):tuple(v) for k,v in ST['forward_old_to_far'].items()}
cut_to_old={int(k):tuple(v) for k,v in ST['inverse_far_to_old'].items()}
old_order=ST['far_cut_physical_old_indices']
reference={r['name']:r for r in D['loops']}
refops={name:{int(k):tuple(v) for k,v in reference[name]['geometric_push'].items()} for name in ('v0','v1')}
refinvs={name:{int(k):tuple(v) for k,v in reference[name]['geometric_pullback'].items()} for name in ('v0','v1')}
I4={i:(i,) for i in range(1,5)}
beta={1:(-1,),2:(4,),3:(5,),4:(2,),5:(3,)}
want={1:{1:(2,),2:(4,),3:(1,),4:(-1,3,1),5:(),6:()},
      2:{1:(2,),2:(4,),3:(),4:(1,),5:(),6:(3,)},
      3:{1:(2,),2:(4,),3:(3,),4:(),5:(-3,1,3),6:()},
      4:{1:(2,),2:(4,),3:(),4:(),5:(3,),6:(1,)}}
node0={1:0,2:8,3:12,4:16}
physical_to_label={1:2,2:0,3:3,4:1}
label_to_physical={v:k for k,v in physical_to_label.items()}

def aspoint(z):return [str(S.re(z)),str(S.im(z))]
def distance_checks(a,b):
    aa=tuple(Fraction(x) for x in aspoint(a));bb=tuple(Fraction(x) for x in aspoint(b))
    delta=tuple(bb[i]-aa[i] for i in range(2));norm=sum(x*x for x in delta)
    result=[]
    for critical in (-1,0,1):
        e=(aa[0]-critical,aa[1]);t=max(Fraction(0),min(Fraction(1),-sum(e[i]*delta[i] for i in range(2))/norm)) if norm else Fraction(0)
        d2=sum((e[i]+t*delta[i])**2 for i in range(2))
        assert d2>Fraction(1,10000)
        result.append({'critical':critical,'parameter':str(t),'distance_squared':str(d2)})
    return result

start=time.monotonic();rows=[]
for exponent in range(1,5):
    endpoint=u[exponent]
    if exponent==2:
        segment=None;word=();order=D['initial_order'];push=pull=I4
    else:
        segment=Segment(u[2],endpoint).compute()
        word=tuple(segment['word']);order=segment['final_order']
        assert segment['initial_order']==D['initial_order']
        push=art(tuple(reversed(word)));pull=art(tuple(-x for x in word))
    for i in range(1,5):assert sub(push[i],pull)==sub(pull[i],push)==(i,)
    # End physical basis a(v),b(0),c(v²),d(1) -> end cut -> reference cut.
    end_cut_to_physical={j+1:(label_to_physical[label],) for j,label in enumerate(order)}
    physical_to_reference={i:pull[order.index(label)+1] for i,label in physical_to_label.items()}
    reference_to_physical={i:sub(push[i],end_cut_to_physical) for i in range(1,5)}
    for i in range(1,5):
        assert sub(physical_to_reference[i],reference_to_physical)==(i,)
        assert sub(reference_to_physical[i],physical_to_reference)==(i,)
    active={0:2,1:4,exponent+1:1,(2*exponent%5)+1:3}
    cut_filling={j+1:((active[label],) if label in active else ()) for j,label in enumerate(old_order)}
    pi={i:sub(w,cut_filling) for i,w in old_to_cut.items()}
    assert pi==want[exponent]
    physical_preimages={physical:cut_to_old[old_order.index(label)+1] for label,physical in active.items()}
    for i in range(1,5):assert sub(physical_preimages[i],pi)==(i,)
    to_reference={i:sub(w,physical_to_reference) for i,w in pi.items()}
    delta={1:(),2:(1,),3:(),4:(2,)}
    for i in range(1,5):assert sub(physical_to_reference[i],delta)==delta[i]
    transported={}
    for name in ('v0','v1'):
        action={i:sub(sub(physical_to_reference[i],refops[name]),reference_to_physical) for i in range(1,5)}
        inverse={i:sub(sub(physical_to_reference[i],refinvs[name]),reference_to_physical) for i in range(1,5)}
        for i in range(1,5):
            assert sub(action[i],inverse)==sub(inverse[i],action)==(i,)
            assert sub(action[i],delta)==sub(inverse[i],delta)==delta[i]
        transported[name]={'push':action,'pullback':inverse}
    r=sub((3,4,-3,-4),reference_to_physical)
    old_r=sub(r,physical_preimages)
    assert sub(old_r,to_reference)==(3,4,-3,-4)
    pair=[]
    for family in (0,1):
        node=(node0[exponent],family);row=pivots[node]
        assert row['A_slot']==row['B_slot']
        z=tuple(row['relative_retained_word'])
        assert rmul(sub(z,beta),z)==()
        pair.append({'family':'constant_v' if family==0 else 'constant_w',
                     'physical_A_label':(2+exponent if family==0 else 6+exponent),
                     'node_index':list(node),'slot':row['A_slot'],'row':row})
    # u_i² and the static root zeta^(2i) differ by less than 1e-28.
    square_difference=S.expand(endpoint*endpoint-u[2*exponent%5])
    assert S.re(square_difference)**2+S.im(square_difference)**2<S.Rational(1,10**56)
    result={'u_exponent':exponent,'base_v':aspoint(endpoint),'reference_base_v':aspoint(u[2]),
        'bridge_vertices':[aspoint(u[2]),aspoint(endpoint)],
        'critical_distance_checks':distance_checks(u[2],endpoint),
        'bridge_segment':segment,'chronological_braid':word,
        'geometric_push':push,'geometric_pullback':pull,'end_cut_physical_labels':order,
        'physical_basis_order':['a=q=u','b=q=0','c=q=u²','d=q=1'],
        'physical_to_reference':physical_to_reference,'reference_to_physical':reference_to_physical,
        'six_cut_filling':cut_filling,'old_to_physical_four':pi,'physical_four_preimages_in_old':physical_preimages,
        'old_to_reference_four':to_reference,'transported_retained_operators':transported,
        'transported_node_relator_physical_four':r,'transported_node_relator_old':old_r,
        'two_actual_diagonal_rows':pair}
    rows.append(result)
    print('PASS u=zeta^'+str(exponent),'bridge',list(word),'end order',order,
          'old->reference',to_reference,'node word',list(old_r),flush=True)

output={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (INPUT,STATIC,PIVOTS)},
 'reference_kernel':'N=normalclosure_F4 of the full signed <gamma0,gamma1> orbit of [c,d], as in B99.',
 'rows':rows,'swapping_map':'(v,q)->(q/v,q), or (v,w)->(w,v), an actual q-preserving involution of X and X0.',
 'whole_kernel_statement':'For each row at exponent i, ker(h_i|K)=Stab_K(row)=preimage of the same reference N under old_to_reference_four. Constant-v and constant-w rows at that exponent have identical kernels in the same based old B6.',
 'based_scope':'The geometric swap maps the pointed constant section to the pointed moving section with the identical q basepoint and identical old q lassos. Changing each fiber basepoint to the recorded actual peripheral whisker is an inner transport, so its zero kernel is unchanged; no literal equality of the two nonzero heads is asserted.',
 'claims_excluded':['literal equality of nonzero constant and moving heads','full-column monomiality','all overlap vanishing','kappa=0','I=R'],
 'elapsed_seconds':time.monotonic()-start}
(CE/'all_diagonal_section_transports.json').write_text(json.dumps(output,indent=2)+'\n')
print('PASS all eight marked diagonal K-row stabilizers transported to the complete B99 kernel; elapsed',round(output['elapsed_seconds'],3),flush=True)
