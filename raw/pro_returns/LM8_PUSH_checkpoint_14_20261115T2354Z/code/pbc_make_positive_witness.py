"""Avoid inverse completion of the inconsistent formal central presentation.

For each finite pc generator g_i, a positive word u_i representing its
inverse is computed in the already consistent finite quotient.  In the
source centralization, g_i u_i = k_i is central, so u_i k_i^-1 is an exact
inverse.  All formal collection then uses nonnegative finite exponents.
"""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
src = HERE / "pbc_hermite_data_witness.g"
s = src.read_text().replace(
    "PBC_HermiteDataWitness:=function", "PBC_HermitePositiveWitness:=function"
)
s = s.replace(
    "newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation;",
    "newLeaf,newOp,newNeg,basisproof,targetproof,currentRelation,"
    "basecoll,finiteInverse,inverseWords,iv,vv,ii;",
)
a = s.index(" inverse:=function(w)")
b = s.index(" coll:=FromTheLeftCollector", a)
s = s[:a] + r'''
 # The only inverse words used in the formal presentation are explicit
 # positive finite words followed by a central correction.  No inverse
 # power or inverse conjugation is completed in the formal presentation.
 inverse:=function(w)
  local out,ii,jj,ex;out:=[];
  for ii in [Length(w)-1,Length(w)-3..1] do
   if w[ii]>n then Append(out,[w[ii],-w[ii+1]]);
   else
    ex:=w[ii+1];Assert(0,ex>=0);
    for jj in [1..ex] do Append(out,inverseWords[w[ii]]);od;
   fi;
  od;
  return out;
 end;
 basecoll:=FromTheLeftCollector(n);
 for i in [1..n] do
  SetRelativeOrder(basecoll,i,orders[i]);SetPower(basecoll,i,data.powers[i]);
  for j in [1..i-1] do SetConjugate(basecoll,i,j,data.conjugates[i][j]);od;
 od;
 if IsBound(data.finite_inverse) then
  finiteInverse:=data.finite_inverse;
  basecoll![PC_COMMUTE]:=ListWithIdenticalEntries(n,n);
  SetFilterObj(basecoll,IsUpToDatePolycyclicCollector);
  for i in [1..n] do
   vv:=ListWithIdenticalEntries(n,0);vv[i]:=1;
   Assert(0,CollectWordOrFail(basecoll,vv,finiteInverse[i])<>fail);
   Assert(0,ForAll(vv,a->a=0));
  od;
 else
  UpdatePolycyclicCollector(basecoll);
  finiteInverse:=List([1..n],i->FromTheLeftCollector_Inverse(basecoll,[i,1]));
 fi;
 Assert(0,ForAll(finiteInverse,w->ForAll([2,4..Length(w)],i->w[i]>=0)));
 Print("consistent_finite_inverses_ready runtime ",Runtime(),"\n");
''' + s[b:]
s = s.replace(
    "SetFilterObj(coll,IsUpToDatePolycyclicCollector);FromTheLeftCollector_CompletePowers(coll);",
    "SetFilterObj(coll,IsUpToDatePolycyclicCollector);",
)
needle = " sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;"
assert needle in s
replacement = r'''
 inverseWords:=[];
 for i in [1..n] do
  iv:=finiteInverse[i];vv:=ShallowCopy(zero);vv[i]:=1;
  while CollectWordOrFail(coll,vv,iv)=fail do vv:=ShallowCopy(zero);vv[i]:=1;od;
  Assert(0,ForAll(vv{[1..n]},a->a=0));
  inverseWords[i]:=ShallowCopy(iv);
  for ii in [1..m] do
   if vv[n+ii]<>0 then Append(inverseWords[i],[n+ii,-vv[n+ii]]);fi;
  od;
  if i mod 20=0 then Print("formal_positive_inverses ",i," runtime ",Runtime(),"\n");fi;
 od;
 sw:=data.s;rw:=data.r;bsw:=data.bs;brw:=data.br;'''
s = s.replace(needle, replacement)
s = re.sub(
    r"CollectWordOrFail\(coll,(w[12]),(.*?)\);",
    r"Assert(0,CollectWordOrFail(coll,\1,\2)<>fail);",
    s,
)
dst = HERE / "pbc_hermite_positive_witness.g"
dst.write_text(s)
metadata = {
    "source": src.name,
    "source_sha256": hashlib.sha256(src.read_bytes()).hexdigest(),
    "output": dst.name,
    "output_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
    "inverse_identity": "g_i u_i=k_i central implies inverse(g_i)=u_i k_i^-1",
}
(HERE / "pbc_hermite_positive_generation.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
