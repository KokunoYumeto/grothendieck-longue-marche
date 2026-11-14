"""Exhaustive staged A4 test of the two F22 marginal source images."""

from pathlib import Path
from itertools import permutations, product
import hashlib
import json

import numpy as np
import marginal_s3_source_stage as engine


def even(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0


PERMS=[p for p in permutations(range(4)) if even(p)]
INDEX={p:i for i,p in enumerate(PERMS)}
MULT=np.array([[INDEX[tuple(a[b[i]] for i in range(4))] for b in PERMS] for a in PERMS],dtype=np.uint8)
INVERSE=np.array([next(j for j in range(12) if MULT[i,j]==0 and MULT[j,i]==0) for i in range(12)],dtype=np.uint8)
ORDER3=[i for i in range(1,12) if MULT[MULT[i,i],i]==0]
C3=sorted({tuple(sorted({0,i,int(MULT[i,i])})) for i in ORDER3})
FIXED=C3[0]
engine.MULT=MULT
engine.INVERSE=INVERSE
engine.POWERS=12**np.arange(7,dtype=np.int64)


def closure(generators):
    group={0};todo=[0]
    while todo:
        a=todo.pop()
        for b in generators:
            c=int(MULT[a,b])
            if c not in group:group.add(c);todo.append(c)
    return tuple(sorted(group))


def subgroup_certificate():
    known={(0,)};todo=[(0,)]
    while todo:
        subgroup=todo.pop()
        for g in range(12):
            bigger=closure(subgroup+(g,))
            if bigger not in known:known.add(bigger);todo.append(bigger)
    data=[]
    for subgroup in sorted(known,key=lambda x:(len(x),x)):
        normal_generators={int(MULT[MULT[g,h],INVERSE[g]]) for g in range(12) for h in subgroup}
        normal=closure(tuple(normal_generators))
        abelian=all(MULT[a,b]==MULT[b,a] for a in subgroup for b in subgroup)
        if len(subgroup)<12:assert abelian
        if len(normal)==12 and len(subgroup)<12:assert subgroup in C3
        data.append({"elements":list(subgroup),"normal_closure":list(normal),"abelian":abelian})
    return data


def one_sign(records,positive):
    sign=1 if positive else -1
    field="positive_braid" if positive else "negative_braid"
    old=np.array(list(product(range(12),repeat=3)),dtype=np.uint8)
    new=np.array(list(product([0]+ORDER3,repeat=4))[1:],dtype=np.uint8)
    seed_records=[r for r in records[11:] if int(r["label"].split("_")[2])==sign]
    survivors=[];counts=[0]*9
    batch_size=32
    for start in range(0,len(old),batch_size):
        batch=old[start:start+batch_size]
        values=np.column_stack([np.repeat(batch,len(new),axis=0),np.tile(new,(len(batch),1))])
        counts[0]+=len(values)
        for i,record in enumerate(seed_records):
            image=engine.braid_coordinate(record[field],values,positive)
            values=values[np.isin(image,FIXED)]
            counts[i+1]+=len(values)
        proper=np.zeros(len(values),dtype=bool)
        for subgroup in C3:proper|=np.all(np.isin(values,subgroup),axis=1)
        values=values[~proper]
        if len(values):survivors.append(values)
        if start%(6*batch_size)==0:
            print(json.dumps({"sign":sign,"old_triples_processed":start+len(batch),
                              "raw_candidates_processed":counts[0],
                              "seed_good_generating_accumulated":sum(len(v) for v in survivors)}),flush=True)
    values=np.concatenate(survivors,axis=0) if survivors else np.empty((0,7),dtype=np.uint8)
    kk=engine.keys(values);index={int(key):i for i,key in enumerate(kk)}
    edges=[];target_keys=[]
    for record in records[:11]:
        transformed=engine.braid_coordinate(record[field],values,positive,action=True)
        target=engine.keys(transformed);target_keys.append(target.tolist())
        edges.append([index.get(int(key),-1) for key in target])
    edges=np.array(edges,dtype=np.int64).T
    active=np.ones(len(values),dtype=bool);layers=[]
    while len(values):
        keep=active&np.all((edges>=0)&active[np.maximum(edges,0)],axis=1)
        removed=np.flatnonzero(active&~keep)
        if not len(removed):break
        layers.append(removed.tolist());active=keep
    remaining=np.flatnonzero(active)
    result={"sign":sign,"raw_candidates":counts[0],
            "initial_possible_A4_failure_tuples":counts[0]-4*(3**3)*(3**4-1),
            "fixed_proper_subgroup":list(FIXED),"successive_seed_filter_counts":counts,
            "seed_good_generating_tuples":values.tolist(),"seed_good_keys":kk.tolist(),
            "source_generator_target_keys":target_keys,"source_generator_edges":edges.tolist(),
            "pruning_layers":layers,"surviving_indices":remaining.tolist(),
            "surviving_tuples":values[remaining].tolist(),
            "conclusion":"NO_PROPER_A4_IMAGE" if not len(remaining) else "PROPER_A4_IMAGE_CANDIDATES"}
    print(json.dumps({"sign":sign,"seed_good_generating":len(values),
                      "pruning_layers":[len(layer) for layer in layers],"survivors":len(remaining),
                      "conclusion":result["conclusion"]}),flush=True)
    return result


def main():
    producer=Path(__file__).resolve();folder=producer.with_name("full_cross_source_stage")
    source=folder/"marginal_braids.json";data=json.loads(source.read_text())
    subgroups=subgroup_certificate()
    results=[one_sign(data["records"],positive) for positive in (True,False)]
    record={"status":"EXHAUSTIVE_FINITE_STAGE_PENDING_GEOMETRIC_AUDIT",
            "producer_sha256":hashlib.sha256(producer.read_bytes()).hexdigest(),
            "input_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
            "permutations":[list(p) for p in PERMS],"multiplication":MULT.tolist(),
            "inverse":INVERSE.tolist(),"subgroups":subgroups,"results":results}
    output=folder/"marginal_a4_scan.json";output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"output_sha256":hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=="__main__":main()
