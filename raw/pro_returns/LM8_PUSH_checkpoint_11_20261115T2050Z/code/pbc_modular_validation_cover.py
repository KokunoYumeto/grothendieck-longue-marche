#!/usr/bin/env python3
"""Check a modular correction in the independent ORIGINAL complete C27 cover."""
from pathlib import Path
import hashlib
import json

b=Path(__file__).parent
cover_path=b/'pbc_hopf_difference_hermite_validation_certificate.json'
result_path=b/'pbc_modular_validation_certificate.json'
cover=json.loads(cover_path.read_text())
result=json.loads(result_path.read_text())
assert result['coefficients'][:2]==[0,0]
assert result['s_count']==cover['s_centralizer_generator_count']
def word(v):return [x for i,e in enumerate(v,1) if e for x in (i,e)]
def lit(x):return json.dumps(x,separators=(',',':'))
n=len(cover['relative_orders'])
code=['LoadPackage("polycyclic");;',f'c:=FromTheLeftCollector({n});;']
for i,p in enumerate(cover['relative_orders'],1):
    code += [f'SetRelativeOrder(c,{i},{p});;',f'SetPower(c,{i},{lit(word(cover["powers"][i-1]))});;']
for i,j,v in cover['conjugates']:
    code += [f'SetConjugate(c,{i},{j},{lit(word(v))});;']
code += ['UpdatePolycyclicCollector(c);;',f'zero:=ListWithIdenticalEntries({n},0);;',
'''normal:=function(w) local v,old,z;v:=ShallowCopy(zero);old:=ShallowCopy(v);
while CollectWordOrFail(c,v,w)=fail do v:=ShallowCopy(old);od;return v;end;;''',
'''inv:=function(w) local v,z,out;v:=normal(w);out:=[];
for z in [1..Length(v)] do if v[z]<>0 then Append(out,[z,v[z]]);fi;od;
return FromTheLeftCollector_Inverse(c,out);end;;''',
f's:={lit(word(cover["s"]))};;',f'r:={lit(word(cover["r"]))};;',
f'bs:={lit(word(cover["original_s_frame"]))};;',f'br:={lit(word(cover["original_r_frame"]))};;',
f'lifts:={lit([word(v) for v in cover["centralizer_lifts"]])};;',
f'coefficients:={lit(result["coefficients"][2:])};;',
f'scount:={cover["s_centralizer_generator_count"]};;',
'''for i in [1..Length(lifts)] do
 for j in [1..coefficients[i]] do
  if i<=scount then Append(bs,lifts[i]);else Append(br,lifts[i]);fi;
 od;
od;
defect:=normal(Concatenation(bs,s,inv(bs),br,r,inv(br),inv(r),inv(s)));;
Assert(0,defect=zero);
Print("modular_correction_verified_in_original_complete_central_cover true\\n");
Print("coefficients ",coefficients,"\\n");
QUIT;''']
out=b/'pbc_modular_validation_cover.g'
out.write_text('\n'.join(code)+'\n')
report={'original_cover_order':cover['order'],'original_cover_generators':n,
        'source_correction':result['coefficients'],
        'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (cover_path,result_path,Path(__file__),out)},
        'scope':'Independent verification in the retained complete C27 central cover, without loading the modular Hermite basis or proof DAG.'}
(b/'pbc_modular_validation_cover.inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
