"""Independent all-generator Birman-action check for the actual tangent bundle.

This evaluator composes elementary Artin substitutions from the opposite
direction to the producing script.  No producer is imported or executed.
All six actions and inverses are tested on all seven standard pure braids.
"""
from pathlib import Path
import hashlib, json, time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source/tangent_bundle_fiber_data.json'
D=json.loads(P.read_text())
started=time.monotonic()

def reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)

def inverse(w):return tuple(-x for x in reversed(w))

def substitute(w,images):
    return reduce(x for a in w for x in (images[a] if a>0 else inverse(images[-a])))

def artin(braid,n=8):
    # Left substitutions, reading the braid backwards, independently of
    # the producer's two-column right-composition implementation.
    current={i:(i,) for i in range(1,n+1)}
    for b in reversed(braid):
        k=abs(b)
        elementary={i:(i,) for i in range(1,n+1)}
        if b>0:
            elementary[k]=(k,k+1,-k);elementary[k+1]=(k,)
        else:
            elementary[k]=(k+1,);elementary[k+1]=(-k-1,k,k+1)
        current={i:substitute(w,elementary) for i,w in current.items()}
    return current

def fiber_word(braid):
    last=artin(braid)[8]
    left=[]
    while len(last)>1:
        assert last[0]==-last[-1]
        left.append(last[0]);last=last[1:-1]
    assert last==(8,)
    # The inverse last-meridian conjugator is the actual homomorphism.
    return inverse(reduce(x for x in left if abs(x)!=8))

def delete_source(braid):
    labels=list(range(1,9));out=[]
    for b in braid:
        k=abs(b)-1
        if 8 not in labels[k:k+2]:
            j=sum(x!=8 for x in labels[:k])+1
            out.append(j if b>0 else -j)
        labels[k],labels[k+1]=labels[k+1],labels[k]
    assert labels[-1]==8
    return tuple(out)

standard=[]
for i in range(1,8):
    w=tuple(range(7,i,-1))+(i,i)+tuple(range(-i-1,-8,-1))
    assert list(w)==D['standard_pure_generators'][i-1]
    assert artin(delete_source(w),7)=={j:(j,) for j in range(1,8)}
    standard.append(w)
fibers=[fiber_word(w) for w in standard]
assert fibers==[tuple(range(-7,-i,1))+(-i,)+tuple(range(i+1,8)) for i in range(1,8)],fibers
# These are a triangular Nielsen basis, not the unwhiskered meridians.
recovered={}
for i in range(7,0,-1):
    tail=tuple(range(i+1,8))
    recovered[i]=reduce(tail+inverse(fibers[i-1])+inverse(tail))
    assert recovered[i]==(i,)
rows=[]
for k in range(6):
    w=tuple(D['source_braids'][k])
    for sign,key in ((1,'old_actions'),(-1,'old_inverse_actions')):
        v=w if sign==1 else inverse(w)
        A={int(i):tuple(a) for i,a in D[key][str(k)].items()}
        for i,test in enumerate(standard,1):
            conjugated=v+test+inverse(v)
            actual=fiber_word(conjugated)
            expected=substitute(fibers[i-1],A)
            assert actual==expected,(k,sign,i,actual,expected)
            rows.append({'base':k,'sign':sign,'fiber':i,'result_length':len(actual)})
    print('Base',k,': all seven standard generators, both signs PASS',flush=True)
for k in range(6,10):
    w=tuple(D['source_braids'][k])
    assert artin(delete_source(w),7)=={j:(j,) for j in range(1,8)}
    assert fiber_word(w)==tuple(D['new_fiber_words'][str(k)])
fill={int(i):tuple(v) for i,v in D['filling'].items()}
for key in ('old_actions','old_inverse_actions'):
    for k,A in D[key].items():
        for i in D['killed_basis']:assert not substitute(A[str(i)],fill)
for seed in D['new_fiber_words'].values():assert not substitute(seed,fill)
out={'scope':__doc__,'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
     'standard_fiber_words':fibers,'all_action_checks':rows,
     'four_actual_cross_seed_checks':True,'actual_filling_checks':True,
     'elapsed_seconds':time.monotonic()-started}
(ROOT/'work_CE/tangent_bundle_all_action_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 84 independently evaluated action comparisons, four literal seed words, and filling.',flush=True)
