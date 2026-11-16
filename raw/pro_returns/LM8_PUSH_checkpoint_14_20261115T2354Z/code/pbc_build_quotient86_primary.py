#!/usr/bin/env python3
"""Prepare the actual G26 quotient and RECOLLECT all target/frame words.

This is ONLY a two-primary QUOTIENT test.  The original-to-G86 H2 map is
surjective with possible kernel C2^2; no full target conclusion is claimed.
Raw central tail vectors are never truncated.
"""
from pathlib import Path
from collections import defaultdict, Counter
import hashlib, json, math, subprocess, sys
from pbc_source_coordinate_bounds import coordinate_bounds

CODE=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=CODE/'pbc_iterated_shortcut_v2_original_source.json'
original=json.loads(source.read_text())
bound=CODE/'pbc_three_h2_layer_bound.json'
b=json.loads(bound.read_text())
assert b['status']=='PASS' and b['original_source_sha256']==sha(source)
assert b['full_three_primary_annihilator']==9
cut=86
def word(w):
    return [a for i,e in zip(w[::2],w[1::2]) if i<=cut for a in (i,e)]
assert all(all(k>cut for k in w[::2]) for i,j,w in original['conjugates'] if i>cut)
q=dict(order=math.prod(original['relative_orders'][:cut]),
       relative_orders=original['relative_orders'][:cut],
       powers=[word(w) for w in original['powers'][:cut]],
       conjugates=[[i,j,word(w)] for i,j,w in original['conjugates'] if i<=cut],
       quotient_of_sha256=sha(source), normal_suffix_start=cut+1,
       normal_suffix_order=original['order']//math.prod(original['relative_orders'][:cut]),
       homology_comparison_certificate_sha256=sha(bound),
       scope='Actual original-generator quotient. The two-primary H2 map is surjective with kernel a quotient of C2^2; a zero quotient target does not settle the original target.')
for k in ('s','r','f','left_s_frame','left_r_frame','s_image','r_image'):
    q[k]=word(original[k])
for k in ('s_centralizers','r_centralizers'):
    q[k]=[word(w) for w in original[k]]
dest=CODE/'pbc_quotient86_original_source.json'
dest.write_text(json.dumps(q,separators=(',',':'))+'\n')
collector_input=CODE/'pbc_quotient86_initial_validate.dat'
with (CODE/'pbc_quotient86_initial_validate.inputs.out').open('w') as out:
    subprocess.run([sys.executable,str(CODE/'pbc_native_collector_input.py'),str(dest),str(collector_input)],stdout=out,check=True)
collector_rows=CODE/'pbc_quotient86_initial_validate.jsonl'
with collector_rows.open('w') as out, (CODE/'pbc_quotient86_initial_validate.out').open('w') as err:
    subprocess.run([str(CODE/'pbc_positive_collector'),str(collector_input)],stdout=out,stderr=err,check=True)
rows={r['label']:r['tail'] for r in map(json.loads,collector_rows.read_text().splitlines())}
sc,rc=len(q['s_centralizers']),len(q['r_centralizers'])
assert len(rows)==3+sc+rc+2 and (sc,rc)==(71,9)
total=defaultdict(int)
for name in ('target_s','target_r','target_product'):
    for i,a in zip(rows[name][::2],rows[name][1::2]): total[i]+=a
target=[a for i,v in sorted(total.items()) if v for a in (i,v)]
extras=[rows[f'extra_{i+1}'] for i in range(sc+rc+2)]
initial=dict(source_sha256=sha(dest),target=target,extras=extras,
             scope='Every target component and every original correction word collected directly in the actual quotient presentation. No central tail truncation.')
initial_path=CODE/'pbc_quotient86_actual_initial_rows.json'
initial_path.write_text(json.dumps(initial,separators=(',',':'))+'\n')
modulus=2**14
old_bounds,proofs=coordinate_bounds(q)
coordinates=[math.gcd(v,modulus) for v in old_bounds]
data=CODE/'pbc_quotient86_primary2.dat'
def emit(f,w): f.write(' '.join(map(str,[len(w)]+w))+'\n')
with data.open('w') as f:
    f.write(str(cut)+'\n'+' '.join(map(str,q['relative_orders']))+'\n')
    for w in q['powers']: emit(f,w)
    for i,j,w in q['conjugates']: emit(f,w)
    f.write(sha(dest)+'\n'+str(modulus)+'\n'+f'{sc} {rc}\n'+' '.join(map(str,coordinates))+'\n')
    emit(f,target)
    for w in extras: emit(f,w)
report=dict(status='Prepared and actual words recollected; no search result',
            original_source_sha256=sha(source),quotient_source_sha256=sha(dest),
            homology_comparison_certificate_sha256=sha(bound),
            original_order=original['order'],quotient_order=q['order'],
            kernel_order=q['normal_suffix_order'],quotient_generators=cut,
            central_tail_coordinates=cut*(cut+1)//2,primary_modulus=modulus,
            coordinate_counts=dict(Counter(coordinates)),target_support=len(target)//2,
            actual_word_collection_tasks=len(rows),s_centralizer_words=sc,r_centralizer_words=rc,
            permitted_search_corrections='Only the71 genuine original s-centralizer commutators; all r and power-word coefficients zero',
            input_sha256=sha(data),actual_initial_rows_sha256=sha(initial_path),
            collector_source_sha256=sha(CODE/'pbc_positive_collector.cpp'),
            collector_executable_sha256=sha(CODE/'pbc_positive_collector'),
            actual_collection_output_sha256=sha(collector_rows),
            search_executable='code/pbc_quotient86_native_search',
            search_executable_sha256=sha(CODE/'pbc_quotient86_native_search'),
            scope='Only a quotient of the two-primary component. Exact original-row replay and the possible two-dimensional top-kernel obstruction remain mandatory; C31 Open.')
(CODE/'pbc_quotient86_preparation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
