"""Exhaustive staged S3 test of the two actual marginal source images.

The input is the exact compact marginal braid data.  All evaluation is
finite permutation arithmetic with the Artin/erased-conjugator recurrence.
The geometric and based-map inputs remain staged pending peer audit.
"""

from pathlib import Path
from itertools import permutations, product
import hashlib
import json

import numpy as np

PERMS=list(permutations(range(3)))
INDEX={p:i for i,p in enumerate(PERMS)}
MULT=np.array([[INDEX[tuple(a[b[i]] for i in range(3))] for b in PERMS] for a in PERMS],dtype=np.uint8)
INVERSE=np.array([next(j for j in range(6) if MULT[i,j]==0 and MULT[j,i]==0) for i in range(6)],dtype=np.uint8)
TRANSPOSITIONS=[i for i in range(1,6) if MULT[i,i]==0]
THREE_CYCLES=[i for i in range(1,6) if i not in TRANSPOSITIONS]
FIXED_T=TRANSPOSITIONS[0]
POWERS=6**np.arange(7,dtype=np.int64)


def triangular(values):
    result=np.empty_like(values)
    suffix=np.zeros(len(values),dtype=np.uint8)
    for i in range(values.shape[1]-1,-1,-1):
        result[:,i]=MULT[MULT[INVERSE[suffix],INVERSE[values[:,i]]],suffix]
        suffix=MULT[values[:,i],suffix]
    return result


def braid_coordinate(braid,values,positive,action=False):
    initial=triangular(values) if positive else values
    x=np.column_stack([initial,np.zeros(len(values),dtype=np.uint8)])
    c=np.zeros_like(x)
    order=list(range(8))
    for crossing in braid:
        i=abs(crossing)-1
        left,right=x[:,i].copy(),x[:,i+1].copy()
        lc,rc=c[:,i].copy(),c[:,i+1].copy()
        if crossing>0:
            x[:,i]=MULT[MULT[left,right],INVERSE[left]]
            x[:,i+1]=left
            c[:,i]=MULT[left,rc]
            c[:,i+1]=lc
        else:
            x[:,i]=right
            x[:,i+1]=MULT[MULT[INVERSE[right],left],right]
            c[:,i]=rc
            c[:,i+1]=MULT[INVERSE[right],lc]
        order[i],order[i+1]=order[i+1],order[i]
    assert order==list(range(8))
    assert np.all(x[:,-1]==0)
    u=INVERSE[c[:,-1]]
    if not action:return u
    result=MULT[MULT[u[:,None],x[:,:7]],INVERSE[u][:,None]]
    return triangular(result) if positive else result


def candidate_tuples():
    old=list(product(range(6),repeat=3))
    new=list(product([0]+TRANSPOSITIONS,repeat=4))
    values=np.array([a+b for a in old for b in new],dtype=np.uint8)
    has_deleted_transposition=np.any(values[:,3:]!=0,axis=1)
    distinct_transpositions=sum(np.any(values==t,axis=1).astype(np.uint8) for t in TRANSPOSITIONS)
    has_three_cycle=np.any(np.isin(values,THREE_CYCLES),axis=1)
    generates=(distinct_transpositions>=2)|((distinct_transpositions>=1)&has_three_cycle)
    return values[has_deleted_transposition&generates]


def keys(values):return values.astype(np.int64)@POWERS


def one_sign(records,positive):
    sign=1 if positive else -1
    field="positive_braid" if positive else "negative_braid"
    values=candidate_tuples()
    initial_count=len(values)
    filters=[]
    for record in records[11:]:
        if int(record["label"].split("_")[2])!=sign:continue
        seed=braid_coordinate(record[field],values,positive)
        good=(seed==0)|(seed==FIXED_T)
        filters.append({"source":record["label"],"before":len(values),"after":int(good.sum())})
        values=values[good]
    good_keys=keys(values)
    index={int(key):i for i,key in enumerate(good_keys)}
    edges=[]
    target_keys=[]
    for record in records[:11]:
        transformed=braid_coordinate(record[field],values,positive,action=True)
        kk=keys(transformed)
        target_keys.append(kk.tolist())
        edges.append([index.get(int(key),-1) for key in kk])
    edges=np.array(edges,dtype=np.int64).T
    active=np.ones(len(values),dtype=bool)
    layers=[]
    while len(values):
        valid=edges>=0
        image_active=active[np.maximum(edges,0)]
        keep=active&np.all(valid&image_active,axis=1)
        removed=np.flatnonzero(active&~keep)
        if not len(removed):break
        layers.append(removed.tolist());active=keep
    survivors=np.flatnonzero(active)
    result={"sign":sign,"initial_possible_S3_failure_tuples":initial_count,
            "fixed_proper_subgroup":[0,FIXED_T],"seed_filters":filters,
            "seed_good_tuples":values.tolist(),"seed_good_keys":good_keys.tolist(),
            "source_generator_target_keys":target_keys,"source_generator_edges":edges.tolist(),
            "pruning_layers":layers,"surviving_indices":survivors.tolist(),
            "surviving_tuples":values[survivors].tolist(),
            "conclusion":"NO_PROPER_S3_IMAGE" if not len(survivors) else "PROPER_S3_IMAGE_CANDIDATES"}
    print(json.dumps({"sign":sign,"initial":initial_count,"seed_good":len(values),
                      "pruning_layers":[len(layer) for layer in layers],
                      "survivors":len(survivors),"conclusion":result["conclusion"]}),flush=True)
    return result


def main():
    producer=Path(__file__).resolve();folder=producer.with_name("full_cross_source_stage")
    source=folder/"marginal_braids.json"
    data=json.loads(source.read_text())
    # The involutive triangular substitution and coordinate identity are
    # checked directly on every finite tuple used in the exhaustive scan.
    candidates=candidate_tuples()
    assert np.array_equal(triangular(triangular(candidates)),candidates)
    results=[one_sign(data["records"],positive) for positive in (True,False)]
    output=folder/"marginal_s3_scan.json"
    record={"status":"EXHAUSTIVE_FINITE_STAGE_PENDING_GEOMETRIC_AUDIT",
            "producer_sha256":hashlib.sha256(producer.read_bytes()).hexdigest(),
            "input_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
            "permutations":[list(p) for p in PERMS],"multiplication":MULT.tolist(),
            "inverse":INVERSE.tolist(),"transpositions":TRANSPOSITIONS,
            "results":results}
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"output_sha256":hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=="__main__":main()
