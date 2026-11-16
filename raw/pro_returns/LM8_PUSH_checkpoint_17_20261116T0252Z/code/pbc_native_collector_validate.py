#!/usr/bin/env python3
"""Compare native exact positive collection with ORIGINAL GAP trace leaves."""
from collections import Counter
from pathlib import Path
import hashlib,json

base=Path(__file__).parent
meta=json.loads((base/'pbc_native_validation.inputs.json').read_text())
rows=[json.loads(s) for s in (base/'pbc_native_validation.jsonl').read_text().splitlines()]
assert len(rows)==meta['tasks']
target=Counter();checked=[]
for row in rows:
 if row['label'].startswith('target_'):
  target.update(dict(zip(row['tail'][::2],row['tail'][1::2])))
 else:
  assert row['tail']==meta['expected'][row['label']],row['label']
  checked.append(row['label'])
actual=[x for i,v in sorted(target.items()) if v for x in [i,v]]
assert actual==meta['expected']['target']
files=['pbc_positive_collector.cpp','pbc_positive_collector',
       'pbc_native_collector_input.py','pbc_native_validation.dat',
       'pbc_native_validation.jsonl','pbc_difference_hermite_validation_source.json',
       'pbc_difference_hermite_validation_trace.jsonl']
report={'status':'PASS','original_gap_leaf_normal_forms_checked':len(checked),
        'combined_positive_target_checked':True,'native_tasks':len(rows),
        'excluded_bilinear_exterior_rows':meta['excluded_exterior_bilinear_rows'],
        'coefficient_arithmetic':'Checked unsigned 64-bit positive coefficients, 128-bit intermediate, abort on overflow; signed differences printed exactly. Assertions enabled.',
        'compile_command':'g++ -std=c++17 -O3 LM8_PUSH/code/pbc_positive_collector.cpp -o LM8_PUSH/code/pbc_positive_collector',
        'hashes':{x:hashlib.sha256((base/x).read_bytes()).hexdigest() for x in files},
        'scope':'Equality of all original direct-collector rows in the retained C27 trace and its three-component target. Exterior bilinear rows are different combinations of original identities, already independently replayed in GAP, and are not equality tests for a single raw associativity word.',
        'development_corrections':'Initial generator input used j instead of i in a type1/2 associativity prefix and aborted at the first nontrivial triple. This was corrected before the complete comparison. The 656 type2 bilinear rows were then separated from direct word normal forms; all other rows and the combined target agreed.'}
(base/'pbc_native_validation_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
