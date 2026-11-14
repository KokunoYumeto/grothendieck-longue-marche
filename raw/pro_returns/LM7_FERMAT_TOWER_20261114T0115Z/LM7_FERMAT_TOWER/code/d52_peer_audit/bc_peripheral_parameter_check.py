#!/usr/bin/env python3
"""Independently check D52's actual pair-space and derivation kernels."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
source=HERE.parent/"D52_EXPERIMENTS/code/d_cm_full_class2_search.py"
program=source.read_text()
prefix=program.split("# Reconstruct literal marked B words",1)[0]
ns={"__file__":str(source),"__name__":"bc_d52_prefix"}
exec(compile(prefix,str(source),"exec"),ns)
W=ns["W"];act=ns["act"];rank=ns["rank"];s=ns["s"];r=ns["r"]
combine=ns["combine"];bsolve=ns["bsolve"];vc=ns["vc"]
cycles=ns["cycles"];size=ns["size"]
scols=[w^act(w,s) for w in W]
rcols=[w^act(w,r) for w in W]
paircols=[];derivcols=[];homcols=[]
for w in W:
    b=combine(W,bsolve(act(w^act(w,r),s)));a=w^b
    assert ns["cusp"](a,b)==0
    paircols.append(vc(a)|(vc(b)<<181))
    derivcols.append(vc(b^act(b,s))|(vc(a^act(a,r))<<181))
    translates=[act(w,g) for g in range(size)]
    homcols.append(sum(vc(combine(translates,c))<<(181*j)
                       for j,c in enumerate(cycles)))
out={
    "status":"PASS",
    "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
    "moving_dimension":len(W),
    "s_difference_rank":rank(scols),
    "r_difference_rank":rank(rcols),
    "s_fixed_dimension":len(W)-rank(scols),
    "r_fixed_dimension":len(W)-rank(rcols),
    "peripheral_pair_space_rank":rank(paircols),
    "actual_derivation_image_rank":rank(derivcols),
    "actual_homology_derivation_image_rank":rank(homcols),
    "pair_to_derivation_kernel_dimension":len(W)-rank(derivcols),
}
assert out["peripheral_pair_space_rank"]==120
assert out["actual_derivation_image_rank"]==18
assert out["actual_homology_derivation_image_rank"]==18
assert out["pair_to_derivation_kernel_dimension"]==102
snull=ns["solver"](scols)[2]
rnull=ns["solver"](rcols)[2]
assert len(snull)==64 and len(rnull)==38
kernel_parameters=[]
for aa,bb in [(combine(W,a),0) for a in rnull]+[(0,combine(W,b)) for b in snull]:
    assert aa==act(aa,r) and bb==act(bb,s)
    mask=ns["wsolve"](aa^bb)
    assert combine(derivcols,mask)==0
    assert combine(homcols,mask)==0
    kernel_parameters.append(mask)
assert rank(kernel_parameters)==102
assert rank(ns["solver"](derivcols)[2]+kernel_parameters)==102
out["exact_kernel_parameter_basis"]=[hex(x) for x in kernel_parameters]
out["kernel_map"]="(a,b) in W^r x W^s maps to w=a+b; pair reconstruction is D52.8"
(HERE/"bc_peripheral_parameter_check.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
