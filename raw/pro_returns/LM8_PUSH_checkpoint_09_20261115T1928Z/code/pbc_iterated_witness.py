#!/usr/bin/env python3
"""Combine the verified source presentation and cached full centralizers."""
from pathlib import Path
import json,hashlib
P=Path(__file__).parent
C=json.loads((P/'pbc_iterated_centralizers_kernel.json').read_text())
S=json.loads((P/'pbc_iterated_s3_map.json').read_text())
assert S['all_pc_relations_verified'] and [i+1 for i,v in enumerate(S['sign']) if v]==[2]
assert [[i+1,v] for i,v in enumerate(S['rotation']) if v]==[[4,1]]
s=(P/'pbc_hopf_iterated_joint_cached.g').read_text();s=s[:s.index('PBC_Tag:=')]
s=s.replace('Fg:=Subgroup(G,[x,y]);;', 'Fg:=SubgroupByIgs(G,PBC_cache_gens{Filtered([1..Length(PBC_cache_gens)],i->not i in [2,4])});;')
s+='\nAssert(0,Size(Fg)*6=Size(G));;\n'
s+=f'PBC_wcs:=List({C["s_generators"]},PBC_cache_eval);;\n'
s+=f'PBC_wcr:=List({C["r_generators"]},PBC_cache_eval);;\n'
s+=r'''
Assert(0,ForAll(PBC_wcs,g->Comm(g,s)=One(G) and g in Fg));
Assert(0,ForAll(PBC_wcr,g->Comm(g,r)=One(G) and g in Fg));
Assert(0,bs^-1*s*bs=s*f^-1 and br^-1*r*br=f*r);
Print("cached_pure_centralizers_verified ",Length(PBC_wcs)," ",Length(PBC_wcr)," runtime ",Runtime(),"\n");
Read("LM8_PUSH/code/pbc_hermite_mod_witness.g");;
PBC_witness:=PBC_HermiteWitnessMod(P,ps,pr,bs^-1,br^-1,PBC_wcs,PBC_wcr);;
Print("targeted_witness_success ",PBC_witness.success,"\n");
if PBC_witness.success then
 PrintTo("LM8_PUSH/code/pbc_iterated_hermite_mod_certificate.json","{\n\"success\":true,\n\"coefficients\":",PBC_witness.coefficients,",\n\"relations\":",PBC_witness.relations,",\n\"pivots\":",PBC_witness.pivots,",\n\"s_count\":",PBC_witness.s_count,",\n\"r_count\":",PBC_witness.r_count,",\n\"initial_target\":",PBC_witness.initial_target,",\n\"initial_extras\":",PBC_witness.initial_extras,"\n}\n");
fi;
QUIT;
'''
(P/'pbc_iterated_witness.g').write_text(s)
R={'source_sha256':hashlib.sha256((P/'pbc_iterated_joint_pc.json').read_bytes()).hexdigest(),
   'centralizers_sha256':hashlib.sha256((P/'pbc_iterated_centralizers_kernel.json').read_bytes()).hexdigest(),
   's3_quotient_sha256':hashlib.sha256((P/'pbc_iterated_s3_map.json').read_bytes()).hexdigest(),
   's_generators':len(C['s_generators']),'r_generators':len(C['r_generators']),
   'scope':'Exact integer source-centralization membership; no full-lift claim before success and audit'}
(P/'pbc_iterated_witness_inputs.json').write_text(json.dumps(R,indent=2)+'\n')
print(json.dumps(R,indent=2))
