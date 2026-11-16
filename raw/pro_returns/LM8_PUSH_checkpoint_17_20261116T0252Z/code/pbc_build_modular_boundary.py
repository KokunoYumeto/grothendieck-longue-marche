#!/usr/bin/env python3
"""Prioritize the actual two-generator action on the elementary abelian suffix.

This is a positive-certificate search. It inserts original exterior rows
for the first two source generators before other triples. Other suffix
exterior rows are omitted from this search; a nonzero remainder is not
reported as a mathematical nonlifting obstruction.
"""
import argparse,hashlib,json
from pathlib import Path
base=Path(__file__).parent
ap=argparse.ArgumentParser()
ap.add_argument('old_stem',type=Path)
ap.add_argument('new_stem',type=Path)
args=ap.parse_args()
old=base/'pbc_hermite_modular_coordinates_witness.g'
new=base/'pbc_hermite_modular_boundary_witness.g'
t=old.read_text().replace('PBC_HermiteModularCoordinatesWitness','PBC_HermiteModularBoundaryWitness')
needle=' for i in [n,n-1..1] do\n  for j in [n,n-1..i+1] do'
prefix=''' # First impose the ORIGINAL wedge relations for the two source
 # generators. This targets the normal elementary-abelian suffix directly.
 for i in [1,2] do
  for j in [n,n-1..abelStart] do for k in [n,n-1..j+1] do
   currentRelation:=[2,i,j,k];exteriorRelation(i,j,k);
   if found then return result;fi;
  od;od;
 od;
 Print("boundary_exterior_prefix_complete ",relcount," target_support ",Length(target)/2," runtime ",Runtime(),"\\n");
'''
assert t.count(needle)==1
t=t.replace(needle,prefix+needle)
oldline='if j>=abelStart then currentRelation:=[2,i,j,k];exteriorRelation(i,j,k);if found then return result;fi;continue;fi;'
assert oldline in t
t=t.replace(oldline,'if j>=abelStart then continue;fi;')
t=t.replace('witness_complete_nonzero_remainder','positive_search_nonzero_remainder_not_a_nonlifting_claim')
new.write_text(t)
program=args.old_stem.with_suffix('.g').read_text().replace(old.name,new.name)
program=program.replace('PBC_HermiteModularCoordinatesWitness','PBC_HermiteModularBoundaryWitness')
program=program.replace(str(args.old_stem)+'_trace',str(args.new_stem)+'_trace')
program=program.replace(str(args.old_stem)+'_certificate',str(args.new_stem)+'_certificate')
args.new_stem.with_suffix('.g').write_text(program)
meta={'method':'Original exterior rows for source generators 1,2 first; all certificate leaves replayed.',
      'negative_scope':'A nonzero final remainder is not claimed to prove nonlifting.',
      'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                (Path(__file__),old,new,args.old_stem.with_suffix('.g'),args.new_stem.with_suffix('.g'))}}
args.new_stem.with_suffix('.inputs.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
