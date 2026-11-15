#!/usr/bin/env python3
"""Insert easy ORIGINAL power identities before dense target corrections.

If two base generators commute and the higher generator's relative
power is trivial, source family 3 is exactly order(j)*tail(j,i).
If the lower generator's relative power is trivial, family 4 is
-order(i)*tail(j,i). These are original identities, not added hypotheses.
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
old=base/'pbc_hermite_modular_scan_witness.g'
new=base/'pbc_hermite_modular_torsion_witness.g'
t=old.read_text().replace('PBC_HermiteModularScanWitness','PBC_HermiteModularTorsionWitness')
needle=' for i in [3..Length(extras)] do insert(extras[i],[i,1],newLeaf("extra",[i],extras[i]));od;'
prefix=''' # Commuting base generators with trivial relative powers give
 # one-coordinate ORIGINAL power identities. Install these before the
 # dense correction rows. Every used leaf is independently replayed.
 for i in [1..n] do for j in [i+1..n] do
  if baseconjs[j][i]<>[j,1] then continue;fi;
  zz:=j*(j-1)/2+1+i;
  if Length(data.powers[j])=0 then
   e:=[zz,orders[j]];relcount:=relcount+1;
   insert(e,[],newLeaf("identity",[3,i,j],e));
  fi;
  if Length(data.powers[i])=0 and
    (Length(data.powers[j])<>0 or orders[i]<>orders[j]) then
   e:=[zz,-orders[i]];relcount:=relcount+1;
   insert(e,[],newLeaf("identity",[4,i,j],e));
  fi;
 od;od;
 Print("original_simple_power_identities ",relcount," pivots ",pivots," runtime ",Runtime(),"\\n");
'''
assert needle in t
t=t.replace(needle,prefix+needle)
new.write_text(t)
program=args.old_stem.with_suffix('.g').read_text().replace(old.name,new.name)
program=program.replace('PBC_HermiteModularScanWitness','PBC_HermiteModularTorsionWitness')
program=program.replace(str(args.old_stem)+'_trace',str(args.new_stem)+'_trace')
program=program.replace(str(args.old_stem)+'_certificate',str(args.new_stem)+'_certificate')
args.new_stem.with_suffix('.g').write_text(program)
report={'method':'Prepend exactly computed one-coordinate original source power identities.',
        'source_families':{'3':'order(j) * tail(j,i) if powers[j]=[] and generators commute',
                           '4':'-order(i) * tail(j,i) if powers[i]=[] and generators commute'},
        'hashes':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in
                  (Path(__file__),old,new,args.old_stem.with_suffix('.g'),args.new_stem.with_suffix('.g'))}}
args.new_stem.with_suffix('.inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
