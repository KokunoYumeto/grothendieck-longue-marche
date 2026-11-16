#!/usr/bin/env python3
"""Equivalent modular reduction with explicit unit normalization of pivots."""
import argparse
import hashlib
import json
from pathlib import Path

base=Path(__file__).parent
ap=argparse.ArgumentParser()
ap.add_argument('old_stem',type=Path)
ap.add_argument('new_stem',type=Path)
args=ap.parse_args()
old_routine=base/'pbc_hermite_modular_witness.g'
new_routine=base/'pbc_hermite_modular_unit_witness.g'
t=old_routine.read_text().replace('PBC_HermiteModularWitness','PBC_HermiteModularUnitWitness')
t=t.replace('baseCommute,zz,hh,modulus;', 'baseCommute,zz,hh,modulus,newMul;')
needle=' coll:=FromTheLeftCollector(n+m);'
insert=''' newMul:=function(u,a)
  traceId:=traceId+1;PrintTo(traceStream,"[\\\"mul\\\",",traceId,",",u,",",a,"]\\n");
  return traceId;
 end;
'''
assert needle in t
t=t.replace(needle,insert+needle)
t=t.replace('local reduced,idx,old,oldw,oldproof,ii;',
            'local reduced,idx,old,oldw,oldproof,ii,eg,u,step,tries,vv,ww,cc;')
needle='   w:=normalizeWeights(w);idx:=v[1];'
insert='''   # Multiplication by a unit of Z/N preserves the row module.
   # Normalize c to gcd(c,N) in one explicit, replayable operation.
   eg:=Gcdex(v[2],modulus);step:=modulus/eg.gcd;u:=eg.coeff1 mod modulus;
   tries:=0;
   while GcdInt(u,modulus)<>1 do
    u:=(u+step) mod modulus;tries:=tries+1;
    Assert(0,tries<=6);
   od;
   Assert(0,(u*v[2]) mod modulus=eg.gcd);
   if u<>1 then
    vv:=[];
    for ii in [1,3..Length(v)-1] do
     cc:=(u*v[ii+1]) mod modulus;if cc<>0 then Append(vv,[v[ii],cc]);fi;
    od;
    v:=vv;
    for ii in [2,4..Length(w)] do w[ii]:=u*w[ii];od;
    proof:=newMul(u,proof);
   fi;
'''
assert needle in t
t=t.replace(needle,insert+needle)
new_routine.write_text(t)
program=args.old_stem.with_suffix('.g').read_text()
program=program.replace(old_routine.name,new_routine.name)
program=program.replace('PBC_HermiteModularWitness','PBC_HermiteModularUnitWitness')
program=program.replace(str(args.old_stem)+'_trace',str(args.new_stem)+'_trace')
program=program.replace(str(args.old_stem)+'_certificate',str(args.new_stem)+'_certificate')
args.new_stem.with_suffix('.g').write_text(program)
report={'method':'Explicit unit normalization c -> gcd(c,N), preserving the original modular row span.',
        'proof_operation':['mul','new_node','unit','old_node'],
        'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                  (Path(__file__),old_routine,new_routine,args.old_stem.with_suffix('.g'),args.new_stem.with_suffix('.g'))}}
args.new_stem.with_suffix('.inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
