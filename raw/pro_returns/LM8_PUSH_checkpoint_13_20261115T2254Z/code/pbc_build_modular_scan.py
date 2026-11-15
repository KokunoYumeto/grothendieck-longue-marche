#!/usr/bin/env python3
"""Remove sorted-set queue overhead from the triangular modular reducer.

Every term created while reducing pivot i has index strictly greater than i.
A forward scan therefore visits precisely the same nonzero pivots in the
same order as the former sorted active set, without repeated list shifts.
"""
import argparse
import hashlib
import json
from pathlib import Path

base=Path(__file__).parent
ap=argparse.ArgumentParser()
ap.add_argument('old_stem',type=Path)
ap.add_argument('new_stem',type=Path)
args=ap.parse_args()
old=base/'pbc_hermite_modular_unit_witness.g'
new=base/'pbc_hermite_modular_scan_witness.g'
t=old.read_text().replace('PBC_HermiteModularUnitWitness','PBC_HermiteModularScanWitness')
start=t.index(' reduce:=function(')
end=t.index(' insert:=function(',start)
routine=''' reduce:=function(v,w,proof)
  local acc,ii,idx,row,d,q,ww,out,coef,pr,first;
  if Length(v)=0 then return [v,w,proof];fi;
  acc:=[];ww:=ShallowCopy(w);pr:=proof;first:=v[1];
  for ii in [1,3..Length(v)-1] do acc[v[ii]]:=v[ii+1];od;
  for idx in [first..m] do
   if not IsBound(acc[idx]) or acc[idx]=0 or not IsBound(basis[idx]) then continue;fi;
   coef:=acc[idx];row:=basis[idx];d:=row[2];q:=(coef-(coef mod d))/d;
   if q=0 then continue;fi;
   acc[idx]:=coef-q*d;
   for ii in [3,5..Length(row)-1] do
    Assert(0,row[ii]>idx);
    if not IsBound(acc[row[ii]]) then acc[row[ii]]:=0;fi;
    acc[row[ii]]:=(acc[row[ii]]-q*row[ii+1]) mod modulus;
   od;
   ww:=normalizeWeights(PBC_SparseAdd(ww,basisweights[row[1]],-q));
   pr:=newOp(pr,q,basisproof[row[1]]);
  od;
  out:=[];
  for idx in [first..m] do
   if IsBound(acc[idx]) and acc[idx]<>0 then Append(out,[idx,acc[idx]]);fi;
  od;
  return [out,ww,pr];
 end;
'''
t=t[:start]+routine+t[end:]
new.write_text(t)
program=args.old_stem.with_suffix('.g').read_text().replace(old.name,new.name)
program=program.replace('PBC_HermiteModularUnitWitness','PBC_HermiteModularScanWitness')
program=program.replace(str(args.old_stem)+'_trace',str(args.new_stem)+'_trace')
program=program.replace(str(args.old_stem)+'_certificate',str(args.new_stem)+'_certificate')
args.new_stem.with_suffix('.g').write_text(program)
report={'method':'Exact same triangular pivot order; replace sorted active queue by forward coordinate scan.',
        'new_row_index_assertion':'Every introduced coordinate is strictly greater than the current pivot.',
        'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                  (Path(__file__),old,new,args.old_stem.with_suffix('.g'),args.new_stem.with_suffix('.g'))}}
args.new_stem.with_suffix('.inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
