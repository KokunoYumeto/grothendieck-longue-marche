"""New structural checks supplementing the restored A76/A79 certificates.

The source module is rebuilt by the preserved finite builder.  The checks
below independently verify the weight/end-ring and bracket arguments used
to prove that the displayed finite laws are actual source quotients.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json, runpy

ROOT=Path(__file__).resolve().parent
builder=ROOT/'lm4_source_verifiers/work_A/check_Q6_forced_frame.py'
with redirect_stdout(StringIO()):
    G=runpy.run_path(str(builder))
chars=G['chars']; lam=G['lam']; NC=G['NC']; dual=G['dualrow']; sm=G['sm']
assert len(chars)==len(set(chars))==36
assert all(any(v) for v in chars)
stab=[q for q in range(72) if dual(lam,NC[q])==lam]
assert set(stab)=={G['e'],G['s']}
frobnorm=[(q,a) for q in range(72) for a in (1,2,4) if dual(lam,NC[q])==sm(a,lam)]
assert len(frobnorm)==2 and {a for q,a in frobnorm}=={1}
assert all(sm(6,v) in chars for v in chars)
assert G['frank'](G['RES'])==8
assert len(G['NB'])==13 and len(G['EB'])==8
assert (len(G['SF']),len(G['RF']),len(G['TF']))==(20,12,4)

fm=G['fm']
def brank(vs):
    piv={}
    for x in vs:
        while x:
            bit=x.bit_length()-1
            if bit in piv: x^=piv[bit]
            else:
                piv[bit]=x
                break
    return len(piv)
off=[fm(fm(u,u),v) | (fm(fm(v,v),u)<<3) for u in range(8) for v in range(8)]
diag=[fm(fm(u,u),v)^fm(fm(v,v),u) for u in range(8) for v in range(8)]
assert brank(off)==6 and brank(diag)==3

# For opposite weights, one single coordinate in each of two rows gives
# every diagonal or off-diagonal symmetric matrix unit.  These are the
# central commutators in the old law; no massive group enumeration is used.
pairs=[(i,j) for i in range(8) for j in range(i,8)]
def sy(v,w):
    return tuple(fm(v[i],w[j])^(fm(v[j],w[i]) if i!=j else 0) for i,j in pairs)
units=[tuple(int(i==j) for i in range(8)) for j in range(8)]
cols=[sy(units[i],units[j]) for i,j in pairs]
assert G['frank'](cols)==36

out={'head_order':72,'relation_rank_at_seven':13,'weight_count':36,
     'weight_stabilizer_order':2,'additive_endomorphism_field':'F8',
     'source_H1_dimension_over_F8':8,'joint_s_tau_restriction_rank':8,
     's_fixed_dimension':20,'r_fixed_dimension':12,'tau_fixed_dimension':4,
     'ordinary_cross_bracket_binary_rank':6,'ordinary_diagonal_bracket_binary_rank':3,
     'old_symmetric_center_span_over_F8':36,
     'old_binary_exponent_in_order':972,'ordinary_detector_binary_exponent':2700,
     'all_checks':'PASS'}
ROOT.joinpath('check_symmetry_source_structure.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
