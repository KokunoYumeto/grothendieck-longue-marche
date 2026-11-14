"""Compact exact marginal braid data for the F22 source-image maps.

The finite braid words and the erased-conjugator recurrence retain the
actual automorphisms without expanding long intermediate free words.
This stage remains subject to independent geometric/based-map audit.
"""

from pathlib import Path
import hashlib
import json


def red(word):
    result=[]
    for letter in word:
        if result and result[-1]==-letter:result.pop()
        else:result.append(letter)
    return result


def inv(word):return [-letter for letter in reversed(word)]


def delete_strands(braid,n,deleted):
    order=list(range(1,n+1));result=[]
    for crossing in braid:
        i=abs(crossing)-1
        if order[i] not in deleted and order[i+1] not in deleted:
            position=sum(label not in deleted for label in order[:i])+1
            result.append(position if crossing>0 else -position)
        order[i],order[i+1]=order[i+1],order[i]
    assert order==list(range(1,n+1))
    return red(result)


def linking(braid,n):
    order=list(range(1,n+1));counts={}
    for crossing in braid:
        i=abs(crossing)-1
        pair=tuple(sorted(order[i:i+2]))
        counts[pair]=counts.get(pair,0)+(1 if crossing>0 else -1)
        order[i],order[i+1]=order[i+1],order[i]
    assert order==list(range(1,n+1))
    assert all(value%2==0 for value in counts.values())
    return {f"{a},{b}":value//2 for (a,b),value in counts.items() if value}


def main():
    producer=Path(__file__).resolve();folder=producer.with_name("full_cross_source_stage")
    geometry=json.loads((folder/"summary.json").read_text())
    based=json.loads((folder/"basepath_comparison.json").read_text())
    chart=based["chart_path_braid"]
    records=[]
    for row in geometry["meridians"]:
        assert hashlib.sha256((folder/row["file"]).read_bytes()).hexdigest()==row["sha256"]
        full=red(chart+row["based_braid"]+inv(chart))
        plus=delete_strands(full,9,{9});minus=delete_strands(full,9,{8})
        base=delete_strands(full,9,{8,9})
        positive_linking=linking(plus,8);negative_linking=linking(minus,8)
        if row["label"].startswith("cross"):
            _,j,eps,_=row["label"].split("_");j=int(j);eps=int(eps)
            old_index={0:4,2:5,3:6,4:7}[j]
            assert base==[]
            assert (minus if eps==1 else plus)==[]
            assert (positive_linking if eps==1 else negative_linking)=={f"{old_index},8":-1}
        records.append({"index":row["index"],"label":row["label"],
                        "standard_based_braid":full,"old_braid":base,
                        "positive_braid":plus,"negative_braid":minus,
                        "positive_linking":positive_linking,"negative_linking":negative_linking})
    record={"status":"PASS_COMPACT_MARGINAL_STAGE_PENDING_GEOMETRIC_AUDIT",
            "producer_sha256":hashlib.sha256(producer.read_bytes()).hexdigest(),
            "geometry_summary_sha256":hashlib.sha256((folder/"summary.json").read_bytes()).hexdigest(),
            "basepath_comparison_sha256":hashlib.sha256((folder/"basepath_comparison.json").read_bytes()).hexdigest(),
            "standard_old_labels":["0","1","v_zeta","v_1","v_zeta2","v_zeta3","v_zeta4"],
            "positive_basis":"geometric meridians; Artin coordinates via involutive triangular tau7",
            "negative_basis":"Artin erased-conjugator coordinates as in F22",
            "orientation_calibration":"With the retained projection-height crossing convention, every counterclockwise simple holomorphic source collision has linking -1 on its selected old/new pair. The F22 basis generator defined by beta_i has linking +1; the source meridians retain their measured inverse orientation in that braid basis.",
            "finite_recurrence":"At initial values x_i and conjugators c_i=1, sigma_j replaces (x_j,x_j1,c_j,c_j1) by (x_j*x_j1*x_j^-1,x_j,x_j*c_j1,c_j); sigma_j^-1 replaces it by (x_j1,x_j1^-1*x_j*x_j1,c_j1,x_j1^-1*c_j). Use initial x_8=1. For a pure eight-strand braid u=c_8^-1 and alpha(X_i)=x_i for i<=7. Its conjugation action on the point-pushing coordinate is X_i -> u*x_i*u^-1. Positive geometric coordinates conjugate this action by tau7. A collision seed has coordinate u, with tau7 applied on evaluation for the positive geometric basis.",
            "records":records}
    output=folder/"marginal_braids.json";output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"source_meridians":len(records),
                      "signed_collision_meridians":16,
                      "output_sha256":hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=="__main__":main()
