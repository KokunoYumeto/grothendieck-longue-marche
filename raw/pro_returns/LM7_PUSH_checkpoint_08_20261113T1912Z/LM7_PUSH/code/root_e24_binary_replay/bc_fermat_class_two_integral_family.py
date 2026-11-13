#!/usr/bin/env python3
"""Exact integral class-two values of all432 literal retained source words."""
from pathlib import Path
from unittest.mock import patch
from collections import Counter
import json,time
import numpy as np
import de_ferrari_two_family_words as family
import bc_fermat_class_two_integral_model as q
from bc_fermat_class_two_integral_extension import hall_coordinates

HERE=Path(__file__).resolve().parent
started=time.time()
with patch.object(Path,"write_text",return_value=0):data=family.load_data()
mod3=np.load(HERE/"bc_fermat_class_two_fibres.npz")["source_word_logs"]
mod4=np.load(HERE/"bc_fermat_class_two_four_fibres.npz")["source_word_values"]
old=json.loads((HERE/"bc_cm_fermat_odd_boundary.json").read_text())["records"]
lambda1=np.array([1,0,0,-1,-1,0,0,0,-11,0],dtype=np.int64)
lambda2=np.array([0,1,0,-11,0,0,0,-1,-1,0],dtype=np.int64)
values=[];records=[]
for index in range(24):
    for row in family.family_words(data,index,lam=1):
        value=q.literal(row["literal_F_word"]);position=len(values)
        assert np.array_equal(value[:10],old[position]["integral_H_abelianization"])
        assert np.array_equal(np.r_[value[:10]%3,2*value[10:]%3],mod3[position])
        hall=hall_coordinates(value)
        assert np.array_equal(np.r_[hall[:10]%4,hall[10:]%2],mod4[position])
        c1,c2=int(lambda1@value[:10]%4),int(lambda2@value[:10]%4)
        u0,v0=(c1-c2)%4,(c1-2*c2)%4
        assert (v0+3*(u0*u0+u0*v0+v0*v0))%4==0
        values.append(value)
        records.append({"certificate_index":index,"ternary_parameters":row["ternary_parameters"],
                        "binary_parameter":row["binary_parameter"],
                        "source_lambda_residues_mod4":[c1,c2],
                        "norm_torus_residue_mod4":[u0,v0]})
    print("Integral family row completed:",index,flush=True)
out={"records":records,"all_integral_and_two_finite_coordinate_comparisons_verified":True,
     "norm_torus_residue_distribution":{str(k):v for k,v in Counter(
         tuple(r["norm_torus_residue_mod4"]) for r in records).items()},
     "elapsed_seconds":round(time.time()-started,3)}
(HERE/"bc_fermat_class_two_integral_family.json").write_text(json.dumps(out,indent=2)+"\n")
np.savez_compressed(HERE/"bc_fermat_class_two_integral_family.npz",source_word_logs=np.stack(values))
print(json.dumps({k:v for k,v in out.items() if k!="records"},indent=2))
print("PASS: all432 exact integral source values and both complete finite comparisons.")
