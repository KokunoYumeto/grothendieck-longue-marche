"""Generate a separate replay of certificate leaves in the ORIGINAL source.

No Hermite basis or processed relation lattice is loaded.  The source
power/conjugate relations acquire independent central tail generators.
The program recomputes the actual boundary words and each used universal
associativity/power identity in that original presentation.
"""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser()
parser.add_argument("source", type=Path)
parser.add_argument("trace", type=Path)
parser.add_argument("expanded", type=Path)
parser.add_argument("--stem", type=Path, required=True)
args = parser.parse_args()
source = json.loads(args.source.read_text())
expanded = json.loads(args.expanded.read_text())
assert expanded["trace_sha256"] == hashlib.sha256(args.trace.read_bytes()).hexdigest()
claimed_source = expanded["source_header"][1]
if len(claimed_source) == 64 and all(c in "0123456789abcdef" for c in claimed_source):
    assert claimed_source == hashlib.sha256(args.source.read_bytes()).hexdigest()
used = {i for i, c in expanded["nonzero_leaf_coefficients"] if c}
leaves = []
for line in args.trace.read_text().splitlines():
    row = json.loads(line)
    if row[0] == "leaf" and row[1] in used:
        leaves.append(row)
assert len(leaves) == len(used)
n = len(source["relative_orders"])
if "conjugates_nested" in source:
    conjugates = source["conjugates_nested"]
else:
    conjugates = [[] for _ in range(n)]
    for i, j, word in source["conjugates"]:
        assert len(conjugates[i - 1]) == j - 1
        conjugates[i - 1].append(word)
data = {
    "orders": source["relative_orders"],
    "powers": source["powers"],
    "conjugates": conjugates,
    "s": source["s"],
    "r": source["r"],
    "bs": source["left_s_frame"],
    "br": source["left_r_frame"],
    "cs": source["s_centralizers"],
    "cr": source["r_centralizers"],
}
if "s_image" in source:
    data["s_image"] = source["s_image"]
    data["r_image"] = source["r_image"]
gap_data = "rec(" + ",".join(
    f"{key}:={json.dumps(value,separators=(',',':'))}"
    for key, value in data.items()
) + ")"
body = r'''
PBC_Replay:=function(d,leaves)
 local n,m,base,coll,i,j,k,t,e,zero,finiteInv,invWords,vv,iv,
       posCollect,inv,tail,vector,difference,ps,abelStart,
       paircomm,exterior,leaf,w1,w2,w,expected,actual,meta,fam,a,
       centralDifference,sumTails;
 n:=Length(d.orders);m:=n*(n+1)/2;
 base:=FromTheLeftCollector(n);
 for i in [1..n] do
  SetRelativeOrder(base,i,d.orders[i]);SetPower(base,i,d.powers[i]);
  for j in [1..i-1] do SetConjugate(base,i,j,d.conjugates[i][j]);od;
 od;
 if not IsBound(d.s_image) then
  UpdatePolycyclicCollector(base);
  finiteInv:=List([1..n],i->FromTheLeftCollector_Inverse(base,[i,1]));
 fi;
 coll:=FromTheLeftCollector(n+m);t:=n;
 for i in [1..n] do
  SetRelativeOrder(coll,i,d.orders[i]);t:=t+1;
  e:=Concatenation(d.powers[i],[t,1]);SetPower(coll,i,e);
  for j in [1..i-1] do
   t:=t+1;e:=Concatenation(d.conjugates[i][j],[t,1]);
   SetConjugate(coll,i,j,e);
  od;
 od;
 coll![PC_COMMUTE]:=Concatenation(ListWithIdenticalEntries(n,n),[n+1..n+m]);
 SetFilterObj(coll,IsUpToDatePolycyclicCollector);
 zero:=ListWithIdenticalEntries(n+m,0);
 posCollect:=function(v,w)
  local backup,z;backup:=ShallowCopy(v);
  while CollectWordOrFail(coll,v,w)=fail do
   for z in [1..Length(v)] do v[z]:=backup[z];od;
  od;
 end;
 invWords:=[];
 if not IsBound(d.s_image) then
  for i in [1..n] do
   iv:=finiteInv[i];vv:=ShallowCopy(zero);vv[i]:=1;posCollect(vv,iv);
   Assert(0,ForAll(vv{[1..n]},a->a=0));invWords[i]:=ShallowCopy(iv);
   for j in [1..m] do if vv[n+j]<>0 then Append(invWords[i],[n+j,-vv[n+j]]);fi;od;
  od;
 fi;
 inv:=function(w)
  local out,z,c;out:=[];
  for z in [Length(w)-1,Length(w)-3..1] do
   if w[z]>n then Append(out,[w[z],-w[z+1]]);
   else
    Assert(0,w[z+1]>=0);
    for c in [1..w[z+1]] do Append(out,invWords[w[z]]);od;
   fi;
  od;return out;
 end;
 tail:=function(w)
  local v,out,z;v:=ShallowCopy(zero);posCollect(v,w);
  Assert(0,ForAll(v{[1..n]},a->a=0));out:=[];
  for z in [1..m] do if v[n+z]<>0 then Append(out,[z,v[n+z]]);fi;od;
  return out;
 end;
 vector:=function(w)
  local v,z;v:=ShallowCopy(zero);
  for z in [1,3..Length(w)-1] do v[w[z]]:=w[z+1];od;return v;
 end;
 difference:=function(v,w)
  local out,z;Assert(0,v{[1..n]}=w{[1..n]});out:=[];
  for z in [1..m] do if v[n+z]<>w[n+z] then Append(out,[z,v[n+z]-w[n+z]]);fi;od;
  return out;
 end;
 centralDifference:=function(a,b)
  local va,vb;va:=ShallowCopy(zero);vb:=ShallowCopy(zero);
  posCollect(va,a);posCollect(vb,b);return difference(va,vb);
 end;
 sumTails:=function(tails)
  local v,t,i,out;v:=ListWithIdenticalEntries(m,0);
  for t in tails do
   for i in [1,3..Length(t)-1] do v[t[i]]:=v[t[i]]+t[i+1];od;
  od;
  out:=[];for i in [1..m] do if v[i]<>0 then Append(out,[i,v[i]]);fi;od;
  return out;
 end;
 ps:=List([1..n],i->[]);
 for i in [1..n] do
  ps[i][i]:=GetPower(coll,i);
  for j in [1..i-1] do ps[i][j]:=Concatenation([j,1],GetConjugate(coll,i,j));od;
 od;
 paircomm:=List([1..n],i->List([1..i-1],j->d.conjugates[i][j]=[i,1]));
 abelStart:=n;
 while abelStart>1 and ForAll([abelStart..n],j->paircomm[j][abelStart-1]) do
  abelStart:=abelStart-1;
 od;
 exterior:=function(i,j,k)
  local acc,add,a,b,u,v,out,z,c,idx;
  Assert(0,j>=abelStart and k>j);
  acc:=ListWithIdenticalEntries(m,0);
  add:=function(l,h,c)
   local idx;if c=0 then return;fi;
   Assert(0,l>h and paircomm[l][h]);
   idx:=l*(l-1)/2+1+h;acc[idx]:=acc[idx]+c;
  end;
  add(k,j,1);u:=d.conjugates[k][i];v:=d.conjugates[j][i];
  for a in [1,3..Length(u)-1] do
   Assert(0,u[a]>=abelStart);
   for b in [1,3..Length(v)-1] do
    Assert(0,v[b]>=abelStart);c:=u[a+1]*v[b+1];
    if u[a]>v[b] then add(u[a],v[b],-c);
    elif u[a]<v[b] then add(v[b],u[a],c);fi;
   od;
  od;
  out:=[];for z in [1..m] do if acc[z]<>0 then Append(out,[z,acc[z]]);fi;od;
  return out;
 end;
 Print("original_source_replay_ready ",n," ",m," runtime ",Runtime(),"\n");
 for leaf in leaves do
  expected:=leaf[5];meta:=leaf[4];
  if leaf[3]="target" then
   if IsBound(d.s_image) then
    actual:=sumTails([
     centralDifference(Concatenation(d.bs,d.s),Concatenation(d.s_image,d.bs)),
     centralDifference(Concatenation(d.br,d.r),Concatenation(d.r_image,d.br)),
     centralDifference(Concatenation(d.s_image,d.r_image),Concatenation(d.s,d.r))]);
   else
    actual:=tail(Concatenation(d.bs,d.s,inv(d.bs),d.br,d.r,inv(d.br),inv(d.r),inv(d.s)));
   fi;
  elif leaf[3]="extra" then
   i:=meta[1];
   if i=1 then actual:=tail(Concatenation(d.s,d.s));
   elif i=2 then actual:=tail(Concatenation(d.r,d.r,d.r));
   elif i<=2+Length(d.cs) then
    a:=d.cs[i-2];
    if IsBound(d.s_image) then
     actual:=centralDifference(Concatenation(a,d.s),Concatenation(d.s,a));
    else actual:=tail(Concatenation(a,d.s,inv(a),inv(d.s)));fi;
   else
    a:=d.cr[i-2-Length(d.cs)];
    if IsBound(d.s_image) then
     actual:=centralDifference(Concatenation(a,d.r),Concatenation(d.r,a));
    else actual:=tail(Concatenation(a,d.r,inv(a),inv(d.r)));fi;
   fi;
  else
   Assert(0,leaf[3]="identity");fam:=meta[1];i:=meta[2];
   if fam=1 then
    j:=meta[3];k:=meta[4];Assert(0,i<j and j<k);
    w1:=ShallowCopy(zero);w1[k]:=1;posCollect(w1,ps[j][i]);
    w2:=vector(ps[k][j]);posCollect(w2,[i,1]);actual:=difference(w1,w2);
   elif fam=2 then j:=meta[3];k:=meta[4];actual:=exterior(i,j,k);
   elif fam=3 then
    j:=meta[3];Assert(0,i<j);
    w1:=ShallowCopy(zero);w1[j]:=d.orders[j]-1;posCollect(w1,ps[j][i]);
    w2:=vector(ps[j][j]);posCollect(w2,[i,1]);actual:=difference(w1,w2);
   elif fam=4 then
    k:=meta[3];Assert(0,i<k);
    w1:=ShallowCopy(zero);w1[k]:=1;posCollect(w1,ps[i][i]);
    w2:=vector(ps[k][i]);posCollect(w2,[i,d.orders[i]-1]);actual:=difference(w1,w2);
   else
    Assert(0,fam=5);
    w1:=vector(ps[i][i]);posCollect(w1,[i,1]);
    w2:=ShallowCopy(zero);w2[i]:=1;posCollect(w2,ps[i][i]);actual:=difference(w1,w2);
   fi;
  fi;
  if actual<>expected then Print("mismatched_leaf ",leaf[2]," ",leaf[3]," ",meta,"\n");fi;
  Assert(0,actual=expected);
 od;
 Print("original_source_identity_replay_verified ",Length(leaves)," leaves runtime ",Runtime(),"\n");
 return true;
end;;
'''
gap_path = args.stem.with_suffix(".g")
gap_path.write_text(
    'LoadPackage("polycyclic");;\n' + body
    + "\nPBC_data:=" + gap_data + ";;\n"
    + "PBC_leaves:=" + json.dumps(leaves, separators=(",", ":")) + ";;\n"
    + "Assert(0,PBC_Replay(PBC_data,PBC_leaves));\nQUIT;\n"
)
metadata = {
    "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
    "trace_sha256": hashlib.sha256(args.trace.read_bytes()).hexdigest(),
    "expanded_certificate_sha256": hashlib.sha256(args.expanded.read_bytes()).hexdigest(),
    "replay_program_sha256": hashlib.sha256(gap_path.read_bytes()).hexdigest(),
    "leaves": len(leaves),
    "purpose": "independent replay in original unprocessed source-tail presentation",
}
args.stem.with_suffix(".inputs.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
