"""Express every initial central error by positive-word differences.

If a,b are chosen lifts of the finite images of s,r, define
  k_s = (b_s s)(a b_s)^-1,
  k_r = (b_r r)(b b_r)^-1,
  k_p = (a b)(s r)^-1.
Each is central; the actual cusp discrepancy is k_s k_r k_p.
Similarly [c,s] is the difference of the collections of c s and s c.
No formal inverse word or inverse-power completion is needed.
"""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
src = HERE / "pbc_hermite_data_witness.g"
s = src.read_text().replace(
    "PBC_HermiteDataWitness:=function", "PBC_HermiteDifferenceWitness:=function"
)
s = s.replace(
    "newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation;",
    "newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation,centralDifference;",
)
a = s.index(" inverse:=function(w)")
b = s.index(" coll:=FromTheLeftCollector", a)
s = s[:a] + s[b:]
s = s.replace(
    "SetFilterObj(coll,IsUpToDatePolycyclicCollector);FromTheLeftCollector_CompletePowers(coll);",
    "SetFilterObj(coll,IsUpToDatePolycyclicCollector);",
)
needle = " sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;"
assert needle in s
s = s.replace(needle, r'''
 centralDifference:=function(a,b)
  local va,vb,tail,ii;
  va:=ShallowCopy(zero);vb:=ShallowCopy(zero);
  while CollectWordOrFail(coll,va,a)=fail do va:=ShallowCopy(zero);od;
  while CollectWordOrFail(coll,vb,b)=fail do vb:=ShallowCopy(zero);od;
  Assert(0,va{[1..n]}=vb{[1..n]});tail:=[];
  for ii in [1..m] do
   if va[n+ii]<>vb[n+ii] then Append(tail,[ii,va[n+ii]-vb[n+ii]]);fi;
  od;
  return tail;
 end;
 sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;''')
s = s.replace(
    "for a in cs do e:=a;Add(extras,centralTail(Concatenation(e,sw,inverse(e),inverse(sw))));od;",
    'for a in cs do e:=a;Add(extras,centralDifference(Concatenation(e,sw),Concatenation(sw,e)));od;',
)
s = s.replace(
    "for a in cr do e:=a;Add(extras,centralTail(Concatenation(e,rw,inverse(e),inverse(rw))));od;",
    'for a in cr do e:=a;Add(extras,centralDifference(Concatenation(e,rw),Concatenation(rw,e)));od;',
)
old = "target:=centralTail(Concatenation(bsw,sw,inverse(bsw),brw,rw,inverse(brw),inverse(rw),inverse(sw)));"
new = r'''target:=centralDifference(Concatenation(bsw,sw),Concatenation(data.s_image,bsw));
 Print("positive_s_frame_error_ready runtime ",Runtime(),"\n");
 target:=PBC_SparseAdd(target,centralDifference(Concatenation(brw,rw),Concatenation(data.r_image,brw)),1);
 Print("positive_r_frame_error_ready runtime ",Runtime(),"\n");
 target:=PBC_SparseAdd(target,centralDifference(Concatenation(data.s_image,data.r_image),Concatenation(sw,rw)),1);'''
assert old in s
s = s.replace(old, new)
s = re.sub(
    r"CollectWordOrFail\(coll,(w[12]),(.*?)\);",
    r"Assert(0,CollectWordOrFail(coll,\1,\2)<>fail);",
    s,
)
assert "inverse(" not in s
dst = HERE / "pbc_hermite_difference_witness.g"
dst.write_text(s)
metadata = {
    "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
    "output_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
    "initial_words": "positive-word differences only",
    "identity": "cusp_error=k_s*k_r*k_p; each factor is central in the original source",
}
(HERE / "pbc_hermite_difference_generation.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
