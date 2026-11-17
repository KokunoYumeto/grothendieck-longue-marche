#!/usr/bin/env python3
"""Replay all auxiliary B6 substitutions without the producing module."""
from pathlib import Path
import json, hashlib
H=Path(__file__).resolve().parent;R=H.parents[1];CE=R/'work_CE/next_symmetric_nodes'
p=CE/'diagonal_kernel_substitution_presentations.json';data=json.loads(p.read_text())
bridges=json.loads((CE/'all_diagonal_section_transports.json').read_text())
st=json.loads((H/'old_lassos_far_cut_conversion.json').read_text())
refs=json.loads((CE/'retained_section_kernel_braids.json').read_text())
def red(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x:ans.pop()
        else:ans.append(x)
    return tuple(ans)
def inv(w):return tuple(-x for x in w[::-1])
def sub(w,A):return red(x for k in w for x in(A[k] if k>0 else inv(A[-k])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
otc=mp(st['forward_old_to_far']);cto=mp(st['inverse_far_to_old'])
delta={1:(1,),2:(2,),3:(),4:(),5:(),6:()}
references={r['name']:mp(r['geometric_push']) for r in refs['loops']}
checks=[]
for row,bridge in zip(data['presentations'],bridges['rows']):
    assert row['u_exponent']==bridge['u_exponent']
    fill=mp(bridge['six_cut_filling']);pi=mp(bridge['old_to_reference_four'])
    active={v[0]:j for j,v in fill.items() if v};inactive=[j for j,v in fill.items() if not v]
    killed=[cto[j] for j in inactive]
    assert list(map(tuple,row['inactive_meridians_in_old_basis']))==killed
    sec={i:(active[i],) for i in range(1,5)}
    for name,actual in row['signed_substitution_automorphisms_on_old_B6'].items():
        fwd=mp(actual['push']);back=mp(actual['pullback'])
        for key,A in [('push',fwd),('pullback',back)]:
            op=mp(bridge['transported_retained_operators'][name][key])
            cutop={j:(sub(op[v[0]],sec) if v else (j,)) for j,v in fill.items()}
            expected={i:sub(sub(otc[i],cutop),cto) for i in range(1,7)}
            assert A==expected
            for w in killed:assert sub(w,A)==w
            for i in range(1,7):assert sub(A[i],delta)==delta[i]
        for i in range(1,7):
            assert sub(fwd[i],back)==sub(back[i],fwd)==(i,)
            assert sub(fwd[i],pi)==sub(pi[i],references[name])
    assert sub(tuple(row['iterated_relator_in_old_basis']),pi)==(3,4,-3,-4)
    checks.append({'u_exponent':row['u_exponent'],'inactive_old_words':killed,
                   'all_four_six_generator_arrays_reconstructed':True,
                   'both_inverse_compositions_and_factor_diagrams':True})
    print('PASS independently reconstructed four signed B6 substitutions; exponent',row['u_exponent'])
out={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'checks':checks,'scope':'Auxiliary free-group substitutions only; no full-surface monodromy claim.'}
(H/'diagonal_substitutions_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all eight complete row-kernel substitution descriptions.')
