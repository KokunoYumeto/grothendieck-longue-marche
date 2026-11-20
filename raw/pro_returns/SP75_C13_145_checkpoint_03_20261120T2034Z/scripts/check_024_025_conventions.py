"""Small exact certificates for the conditional algebra on scans024--025.

No recognition or transcription code. Finite permutations and freely reduced
words only. General statements are proved in the accompanying reading notes;
these checks expose order errors and give a counterexample to a left/right slip.
"""
from pathlib import Path
from itertools import permutations
import json

def mul(p,q): return tuple(p[q[i]] for i in range(3))
S=list(permutations(range(3))); one=(0,1,2)
center=[p for p in S if all(mul(p,q)==mul(q,p) for q in S)]
assert center==[one]
centralizer=[(p,e) for p in S for e in (0,1)
             if all(mul(p,q)==mul(q,p) for q in S)]
assert centralizer==[(one,0),(one,1)]

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in w[::-1])
def cat(*ws):return red(sum((tuple(w) for w in ws),()))
def conj(g,x):return cat(g,x,inv(g))
a=(1,);b=(2,);h=(3,);x=(4,)
checks={
 'right_loop_factor_preserves_conjugation':conj(cat(b,a),a)==conj(b,a),
 'left_loop_factor_does_not_in_general':conj(cat(a,b),a)!=conj(b,a),
 'inner_postcomposition_uninverted':conj(h,conj(b,x))==conj(cat(h,b),x),
 'inner_postcomposition_inverted':conj(h,conj(inv(b),x))==conj(inv(cat(b,inv(h))),x),
 'composition_uninverted':conj(b,conj(h,x))==conj(cat(b,h),x),
 'composition_inverted':conj(inv(b),conj(inv(h),x))==conj(inv(cat(h,b)),x),
 'kernel_direct_product_coordinate':cat(conj(h,cat(b,a)),cat(h,a))==cat(h,b,a,a),
}
assert all(checks.values())
out={'scope':'S3 x C2 centralizer inside that finite subgroup only; free-word convention checks, not a proof of profinite centralizers or geometric identifications.',
     'S3_center':center,'centralizer_in_S3_times_C2':centralizer,
     'free_word_checks':checks,
     'counterexample':{'unmodified_g_b_l_a':conj(b,a),'left_modified_g_ab':conj(cat(a,b),a),'right_modified_g_ba':conj(cat(b,a),a)},
     'letters':{'1':'loop a','2':'conjugator b','3':'inner postconjugator h','4':'arbitrary element x'}}
dest=Path(__file__).resolve().parents[1]/'reader_reports/145_scans024_025_algebra_check.json'
dest.write_text(json.dumps(out,indent=2))
print(json.dumps(out))
