#!/usr/bin/env python3
"""Replace only the original modular coefficient bound by the proved H2 bound."""
from pathlib import Path
import hashlib,json,math
B=Path(__file__).resolve().parent
source=B/'pbc_iterated_shortcut_v2_original_source.json';raw=json.loads(source.read_text());N=math.prod(raw['relative_orders'])
bound_path=B/'pbc_derived_h2_bound.json';bound=json.loads(bound_path.read_text());M=math.prod(e*e for e in bound['factor_exponents'])
assert M==bound['bound'] and bound['group_order']==N
assert N%M==0 and math.lcm(*bound['factor_exponents'])>1
assert [math.lcm(*v) for v in bound['abelian_invariants']]==bound['factor_exponents']
orders=bound['derived_orders'];assert orders[0]==N and orders[-1]==1
assert [orders[i]//orders[i+1] for i in range(len(orders)-1)]==[math.prod(v) for v in bound['abelian_invariants']]
old=B/'pbc_native_modular_iterated.dat';lines=old.read_text().splitlines(keepends=True);sh=hashlib.sha256(source.read_bytes()).hexdigest();i=lines.index(sh+'\n')
assert int(lines[i+1])==N;lines[i+1]=str(M)+'\n'
old_bounds=list(map(int,lines[i+3].split()));new_bounds=[M if d==N else d for d in old_bounds]
assert all(d>0 and M%d==0 for d in new_bounds)
lines[i+3]=' '.join(map(str,new_bounds))+'\n'
out=B/'pbc_native_smallmod_v1_iterated.dat';assert not out.exists();out.write_text(''.join(lines))
report={'original_source_sha256':sh,'original_group_order':N,'proved_homology_annihilator':M,
 'annihilator_certificate':'pbc_derived_h2_bound.json','annihilator_certificate_sha256':hashlib.sha256(bound_path.read_bytes()).hexdigest(),
 'old_input_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'new_input_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'unchanged_source_words_and_raw_target_and_frame_rows':True,'coordinate_changes':'Only the full modulus N is replaced by M; the independently proved proper bounds1,2,3 are unchanged.',
 'proper_coordinate_bounds':sum(d<N for d in old_bounds),'source_rows_unchanged':True,
 'program':'pbc_native_modular_v5','program_sha256':hashlib.sha256((B/'pbc_native_modular_v5').read_bytes()).hexdigest(),
 'program_source_sha256':hashlib.sha256((B/'pbc_native_modular_v5.cpp').read_bytes()).hexdigest(),
 'positive_gate':'notes/pbc_C31_small_annihilator.md; original-source DAG expansion and row replay still mandatory',
 'old_v5_basis':'preserved paused; this is a separate exact search'}
out.with_suffix('.inputs.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
