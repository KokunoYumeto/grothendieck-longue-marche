#!/usr/bin/env python3
"""Replay every used non-modulus leaf in the ORIGINAL source collector.

The GAP replay body is the independently retained standard-collector
routine. No Hermite basis, modular quotient collector, or processed
relation lattice is loaded. Modulus leaves were separately checked by
the exact DAG verifier and the Hopf-torsion comparison.
"""
import argparse
import ast
import hashlib
import json
import math
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('source',type=Path)
parser.add_argument('trace',type=Path)
parser.add_argument('expanded',type=Path)
parser.add_argument('--stem',type=Path,required=True)
args=parser.parse_args()
source=json.loads(args.source.read_text())
expanded=json.loads(args.expanded.read_text())
assert expanded['verified_original_modular_identity']
assert expanded['original_integer_residual_divisible_by_modulus']
assert expanded['forbidden_power_word_coefficients']==[0,0]
assert expanded['trace_sha256']==hashlib.sha256(args.trace.read_bytes()).hexdigest()
assert expanded['source_sha256']==hashlib.sha256(args.source.read_bytes()).hexdigest()
assert expanded['modulus']==math.prod(source['relative_orders'])
used=set(expanded['used_original_source_leaf_ids'])
leaves=[]
for line in args.trace.open():
    row=json.loads(line)
    if row[0]=='leaf' and row[1] in used:
        assert row[2]!='modulus'
        if row[2]=='extra':assert row[3][0]>=3
        leaves.append(row)
assert len(leaves)==len(used)
next_id=-1
for idx, proof in sorted(expanded['coordinate_bound_proofs'].items(), key=lambda kv:int(kv[0])):
    idx=int(idx)
    assert sum(r['coefficient']*r['value'] for r in proof['rows'])==proof['bound']
    for r in proof['rows']:
        leaves.append(['leaf',next_id,'identity',r['meta'],[idx,r['value']]])
        next_id-=1
n=len(source['relative_orders'])
if 'conjugates_nested' in source:
    conjugates=source['conjugates_nested']
else:
    conjugates=[[] for _ in range(n)]
    for i,j,word in source['conjugates']:
        assert len(conjugates[i-1])==j-1
        conjugates[i-1].append(word)
data=dict(orders=source['relative_orders'],powers=source['powers'],conjugates=conjugates,
          s=source['s'],r=source['r'],bs=source['left_s_frame'],br=source['left_r_frame'],
          cs=source['s_centralizers'],cr=source['r_centralizers'],
          s_image=source['s_image'],r_image=source['r_image'])
original=Path(__file__).with_name('pbc_replay_source_rows.py')
body=None
for node in ast.parse(original.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='body' for t in node.targets):
        assert body is None
        body=ast.literal_eval(node.value)
assert isinstance(body,str) and 'PBC_Replay:=function' in body
record='rec('+','.join(k+':='+json.dumps(v,separators=(',',':')) for k,v in data.items())+')'
gap=args.stem.with_suffix('.g')
gap.write_text('LoadPackage("polycyclic");;\n'+body+'\nPBC_data:='+record+';;\n'
               +'PBC_leaves:='+json.dumps(leaves,separators=(',',':'))+';;\n'
               +'Assert(0,PBC_Replay(PBC_data,PBC_leaves));\nQUIT;\n')
report=dict(source_sha256=expanded['source_sha256'],trace_sha256=expanded['trace_sha256'],
            modulus=expanded['modulus'],original_source_leaves=len(leaves),
            universal_identity_rows=sum(r[2]=='identity' for r in leaves),
            source_word_rows=sum(r[2]!='identity' for r in leaves),
            hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in (args.source,args.trace,args.expanded,original,Path(__file__),gap)},
            scope='Standard original-presentation collector replay; no processed relation lattice is loaded.')
args.stem.with_suffix('.inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
