"""Exact marginal words extracted from the staged nine-strand certificate."""

from pathlib import Path
import hashlib
import json

import joint_kernel_presentation_f22 as words

red, inv, subst, artin = words.red, words.inv, words.subst, words.artin


def delete_strands(braid, n, deleted):
    order = list(range(1,n+1))
    result = []
    for crossing in braid:
        i = abs(crossing)-1
        left,right = order[i:i+2]
        if left not in deleted and right not in deleted:
            position = sum(label not in deleted for label in order[:i])+1
            result.append(position if crossing>0 else -position)
        order[i],order[i+1]=order[i+1],order[i]
    assert order==list(range(1,n+1))
    return red(result)


def erased_conjugator(braid,n):
    images=artin(braid,n)
    c=words.pure_conjugator(images[-1],n)
    erase=lambda w:red([letter for letter in w if abs(letter)!=n])
    return inv(erase(c)), [erase(w) for w in images[:-1]], images


def marginal(braid,positive):
    b8=delete_strands(braid,9,{9 if positive else 8})
    u,alpha,images=erased_conjugator(b8,8)
    triangular=words.triangular_basis(7)
    if positive:
        seed=subst(u,triangular)
        action=[subst(red(u+subst(t,alpha)+inv(u)),triangular) for t in triangular]
    else:
        seed=u
        action=[red(u+image+inv(u)) for image in alpha]
    return {"braid":b8,"point_coordinate":seed,"conjugation_action":action,
            "base_automorphism":alpha,"artin_images":images}


def fill_deleted_old(word):
    return red([letter for letter in word if abs(letter)<=3])


def main():
    producer=Path(__file__).resolve()
    folder=producer.with_name("full_cross_source_stage")
    geometry=json.loads((folder/"summary.json").read_text())
    based=json.loads((folder/"basepath_comparison.json").read_text())
    chart=based["chart_path_braid"]
    records=[]
    for row in geometry["meridians"]:
        full=red(chart+row["based_braid"]+inv(chart))
        positive=marginal(full,True)
        negative=marginal(full,False)
        inverse_positive=marginal(inv(full),True)
        inverse_negative=marginal(inv(full),False)
        for sign,data,inverse_data in ((1,positive,inverse_positive),(-1,negative,inverse_negative)):
            for i in range(7):
                assert subst(data["conjugation_action"][i],inverse_data["conjugation_action"])==[i+1]
                assert subst(inverse_data["conjugation_action"][i],data["conjugation_action"])==[i+1]
                words.pure_conjugator(data["conjugation_action"][i],i+1)
            for i in range(3,7):
                assert fill_deleted_old(data["conjugation_action"][i])==[]
            data["inverse_conjugation_action"]=inverse_data["conjugation_action"]
        if row["label"].startswith("cross"):
            _,j,eps,root=row["label"].split("_")
            eps=int(eps)
            assert positive["base_automorphism"]==[[i] for i in range(1,8)]
            assert negative["base_automorphism"]==[[i] for i in range(1,8)]
            expected_old_index={0:4,2:5,3:6,4:7}[int(j)]
            if eps==1:
                assert negative["artin_images"]==[[i] for i in range(1,9)]
                center=positive["point_coordinate"][:]
                while len(center)>1 and center[0]==-center[-1]:center=center[1:-1]
                assert center==[expected_old_index],(row["label"],center)
                assert fill_deleted_old(positive["point_coordinate"])==[]
            else:
                assert positive["artin_images"]==[[i] for i in range(1,9)]
                center=negative["point_coordinate"][:]
                while len(center)>1 and center[0]==-center[-1]:center=center[1:-1]
                assert center==[-expected_old_index],(row["label"],center)
                assert fill_deleted_old(negative["point_coordinate"])==[]
        records.append({"index":row["index"],"label":row["label"],
                        "standard_based_braid":full,"positive":positive,"negative":negative})
        print(json.dumps({"processed":row["index"],"label":row["label"],
                          "positive_coordinate_length":len(positive["point_coordinate"]),
                          "negative_coordinate_length":len(negative["point_coordinate"])}),flush=True)
    record={"status":"PASS_EXACT_MARGINAL_STAGE_PENDING_GEOMETRIC_AUDIT",
            "producer_sha256":hashlib.sha256(producer.read_bytes()).hexdigest(),
            "geometry_summary_sha256":hashlib.sha256((folder/"summary.json").read_bytes()).hexdigest(),
            "basepath_comparison_sha256":hashlib.sha256((folder/"basepath_comparison.json").read_bytes()).hexdigest(),
            "standard_old_labels":["0","1","v_zeta","v_1","v_zeta2","v_zeta3","v_zeta4"],
            "positive_coordinate_basis":"geometric positive point-pushing basis, inverse triangular Artin substitution",
            "negative_coordinate_basis":"Artin erased-conjugator point-pushing coordinate retained in F22",
            "records":records}
    output=folder/"marginal_words.json"
    output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"source_meridians":len(records),
                      "output_sha256":hashlib.sha256(output.read_bytes()).hexdigest()},indent=2))


if __name__=="__main__":main()
