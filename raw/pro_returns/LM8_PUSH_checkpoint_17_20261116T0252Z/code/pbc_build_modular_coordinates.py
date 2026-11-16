#!/usr/bin/env python3
"""Use proved original power bounds as coordinate moduli.

Proper coordinate bounds are gcds of exact one-coordinate original power
identities. Only untouched coordinates use |G| and its Hopf-torsion gate.
"""
import argparse,hashlib,json
from pathlib import Path

base=Path(__file__).parent
ap=argparse.ArgumentParser()
ap.add_argument('old_stem',type=Path)
ap.add_argument('new_stem',type=Path)
args=ap.parse_args()
old=base/'pbc_hermite_modular_scan_witness.g'
new=base/'pbc_hermite_modular_coordinates_witness.g'
t=old.read_text().replace('PBC_HermiteModularScanWitness','PBC_HermiteModularCoordinatesWitness')
t=t.replace('modulus,newMul;', 'modulus,newMul,coordinateModuli;')
oldheader=' PrintTo(traceStream,"[\\\"source\\\",\\\"",data.source_sha256,"\\\",",n,",",m,",",modulus,"]\\n");'
assert oldheader in t
t=t.replace(oldheader,'')
needle=' coll:=FromTheLeftCollector(n+m);'
init=''' coordinateModuli:=ListWithIdenticalEntries(m,modulus);
 for i in [1..n] do for j in [i+1..n] do
  if data.conjugates[j][i]<>[j,1] then continue;fi;
  zz:=j*(j-1)/2+1+i;
  if Length(data.powers[j])=0 then
   coordinateModuli[zz]:=GcdInt(coordinateModuli[zz],orders[j]);
  fi;
  if Length(data.powers[i])=0 then
   coordinateModuli[zz]:=GcdInt(coordinateModuli[zz],orders[i]);
  fi;
 od;od;
 PrintTo(traceStream,"[\\\"source\\\",\\\"",data.source_sha256,"\\\",",n,",",m,",",modulus,",",coordinateModuli,"]\\n");
'''
assert needle in t
t=t.replace(needle,init+needle)
t=t.replace('(acc[row[ii]]-q*row[ii+1]) mod modulus',
            '(acc[row[ii]]-q*row[ii+1]) mod coordinateModuli[row[ii]]')
t=t.replace('eg:=Gcdex(v[2],modulus);step:=modulus/eg.gcd;',
            'eg:=Gcdex(v[2],coordinateModuli[v[1]]);step:=coordinateModuli[v[1]]/eg.gcd;')
t=t.replace('(u*v[2]) mod modulus=eg.gcd',
            '(u*v[2]) mod coordinateModuli[v[1]]=eg.gcd')
t=t.replace('(u*v[ii+1]) mod modulus',
            '(u*v[ii+1]) mod coordinateModuli[v[ii]]')
oldinit='''  basis[i]:=[i,modulus];basisweights[i]:=[];
  basisproof[i]:=newLeaf("modulus",[i],[i,modulus]);'''
newinit='''  basis[i]:=[i,coordinateModuli[i]];basisweights[i]:=[];
  if coordinateModuli[i]=modulus then
   basisproof[i]:=newLeaf("modulus",[i],[i,modulus]);
  else
   basisproof[i]:=newLeaf("coordinate",[i],[i,coordinateModuli[i]]);
  fi;'''
assert oldinit in t
t=t.replace(oldinit,newinit)
new.write_text(t)
program=args.old_stem.with_suffix('.g').read_text().replace(old.name,new.name)
program=program.replace('PBC_HermiteModularScanWitness','PBC_HermiteModularCoordinatesWitness')
program=program.replace(str(args.old_stem)+'_trace',str(args.new_stem)+'_trace')
program=program.replace(str(args.old_stem)+'_certificate',str(args.new_stem)+'_certificate')
args.new_stem.with_suffix('.g').write_text(program)
meta={'method':'Coordinate moduli from explicit original one-coordinate power identities; original row replay remains required.',
      'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                (Path(__file__),old,new,args.old_stem.with_suffix('.g'),args.new_stem.with_suffix('.g'))}}
args.new_stem.with_suffix('.inputs.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
