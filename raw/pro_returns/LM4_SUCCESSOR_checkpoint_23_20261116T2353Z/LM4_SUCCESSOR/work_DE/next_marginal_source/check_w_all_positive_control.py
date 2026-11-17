"""All five positive source lifts with exact corrections and four deleted seeds.

Research extension of B83; no zero-base or arbitrary retained-source
normalization is asserted.
"""
from pathlib import Path
import json
from weighted_stallings import multiply as m,inverse as inv,substitute as sub
P=Path(__file__).resolve().parent
d=json.loads((P/'w_source_adapted_basis.json').read_text())
fourth=json.loads((P/'w_fourth_strip_correction.json').read_text())
A={i:{int(j):tuple(w) for j,w in d['actions_in_new'][str(i)].items()} for i in range(6)}
Ai={i:{int(j):tuple(w) for j,w in d['inverse_actions_in_new'][str(i)].items()} for i in range(6)}
sw={int(j):tuple(w) for j,w in d['all_source_words_in_new'].items()}
z,c1,c2,c3,c4,p1,p2,p3,p4,a,diag,b=[(j,) for j in range(1,13)]
T=m(b,a,diag,b);C3=m(inv(c4),inv(c3),c4)
k=m(inv(b),c4,b);assert sub(c4,Ai[2])==k
v3=m(inv(sw[17]),inv(k),sw[17],k)
v4=tuple(fourth['correction']);C2=tuple(fourth['normalized_deleted_core'])
assert tuple(fourth['local_pair_boundary'])==m(C2,b)
assert sub(fourth['exact_source_expression'],{j+1:tuple(r['word']) for j,r in enumerate(fourth['source_generators'])})==v4
# A literal abstract F19 source word: old lifts0..5 become1..6,
# thirteen source crossing meridians11..23 become7..19.
def source_lift(index,operator=None):
    out=(index-4,)
    if operator is not None:
        i,kind=operator;g=i+1 if kind=='actions_in_new' else -(i+1)
        out=m((g,),out,(-g,))
    return out
source_v4=sub(fourth['exact_source_expression'],{j+1:source_lift(r['source_index'],r['operator']) for j,r in enumerate(fourth['source_generators'])})
source_v3=m(inv(source_lift(17)),(-3,),inv(source_lift(15)),(3,),source_lift(17),(-3,),source_lift(15),(3,))
# Exact source witness for the fourth deleted Nielsen generator.
source_C2=m(inv(m(source_lift(11),source_lift(14),source_lift(15))),(-2,),inv(source_lift(18)),inv(source_lift(13)),source_lift(18),(2,),source_lift(11),source_lift(14),source_lift(15))
actual_C2=m(inv(m(z,c3,c4)),sub(m(inv(p2),inv(c2),p2),Ai[1]),z,c3,c4)
assert actual_C2==C2
kill_constant={j:(() if j in [8,9,10,11] else (j,)) for j in range(1,20)}
kill_both={j:(() if j in [3,4,5,6,8,9,10,11] else (j,)) for j in range(1,20)}
assert not sub(source_v3,kill_constant)
assert not sub(source_C2,kill_constant)
assert not sub(source_v4,kill_both)
print('PASS literal source words: v3,c2star lie in constant source kernel; v4 lies in both-family source kernel')
correction={1:(),2:(),3:v3,4:v4,5:()}
new={};new_inverse={}
for i in range(1,6):
    v=correction[i]
    new[i]={j:m(inv(v),A[i][j],v) for j in range(1,13)}
    new_inverse[i]={j:sub(m(v,(j,),inv(v)),Ai[i]) for j in range(1,13)}
    for j in range(1,13):assert sub(new[i][j],new_inverse[i])==(j,) and sub(new_inverse[i][j],new[i])==(j,)
for i,C in [(3,C3),(4,C2)]:
    K=m(C,b)
    assert new[i][12]==m(K,b,inv(K)) and sub(C,new[i])==m(K,C,inv(K))
forward={1:(),2:inv(c4),3:C3,4:C2,5:m(b,inv(c1),inv(b))}
backward={1:(),2:m(inv(b),c4,b),3:m(inv(b),inv(C3),b),4:m(inv(b),inv(C2),b),5:c1}
for i in range(1,6):
    assert new[i][12]==m(forward[i],b,inv(forward[i]))
    assert new_inverse[i][12]==m(backward[i],b,inv(backward[i]))
print('PASS all120 corrected whole-basis inverse identities and all10 literal b-conjugators')
# The c2 replacement is a partial-conjugation/inversion Nielsen map,
# with conjugating word independent of c2; verify both inverses anyway.
h=m(inv(c4),inv(c3),inv(z),T)
assert C2==m(h,inv(c2),inv(h)) and 3 not in map(abs,h)
replacement={j:(C2 if j==3 else (j,)) for j in range(1,13)}
inverse_replacement={j:(m(inv(h),(-3,),h) if j==3 else (j,)) for j in range(1,13)}
for j in range(1,13):assert sub(replacement[j],inverse_replacement)==(j,) and sub(inverse_replacement[j],replacement)==(j,)
print('PASS all24 inverse Nielsen substitutions for c2star')
out={'description':__doc__,'deleted_seed_words':[c1,C2,c3,c4],'v3':v3,'v4':v4,'source_v3_F19':source_v3,'source_v4_F19':source_v4,'source_c2star_F19':source_C2,'constant_source_killed_generators':[8,9,10,11],'both_source_killed_generators':[3,4,5,6,8,9,10,11],'corrected_actions':new,'corrected_inverse_actions':new_inverse,'b_conjugators':forward,'inverse_b_conjugators':backward,'nielsen_replacement':replacement,'inverse_nielsen_replacement':inverse_replacement,'scope':'Exact inputs for the restricted all-positive stage theorem. The full source has the zero operator and retained source inner operators as additional unproved normalization directions.'}
(P/'w_all_positive_control.json').write_text(json.dumps(out,indent=2)+'\n')
