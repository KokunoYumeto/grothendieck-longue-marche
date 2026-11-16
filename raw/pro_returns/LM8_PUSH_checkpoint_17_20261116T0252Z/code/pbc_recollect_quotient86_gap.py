#!/usr/bin/env python3
"""Recollect the retained G86 identity templates with the standard GAP collector.

This is a fresh independent source computation after a raw-normal-form
mismatch.  The old search, failed replay, input and archive recipe are
unchanged.  No mismatch is silently accepted as a relation.
"""
from pathlib import Path
import ast,gzip,hashlib,json
CODE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
compact=lambda v:json.dumps(v,separators=(',',':'))
source=CODE/'pbc_quotient86_original_source.json';s=json.loads(source.read_text())
trace=CODE/'pbc_quotient86_primary2_trace.jsonl.gz';leaves=[]
for line in gzip.open(trace,'rt'):
    if line.startswith('["leaf",'):
        r=json.loads(line)
        if r[2] in ('target','identity','extra'):leaves.append(r)
initial=json.loads((CODE/'pbc_quotient86_actual_initial_rows.json').read_text())
seen={r[3][0] for r in leaves if r[2]=='extra'}
for i,row in enumerate(initial['extras'],1):
    if i not in seen:leaves.append(['leaf',-i,'extra',[i],row])
old=CODE/'pbc_replay_source_rows.py';body=None
for node in ast.parse(old.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='body' for t in node.targets):body=ast.literal_eval(node.value)
assert isinstance(body,str)
oldcheck='''  if actual<>expected then Print("mismatched_leaf ",leaf[2]," ",leaf[3]," ",meta,"\\n");fi;
  Assert(0,actual=expected);'''
newcheck='''  PBC_recollect_count:=PBC_recollect_count+1;
  if actual<>expected then PBC_recollect_mismatches:=PBC_recollect_mismatches+1;fi;
  if PBC_recollect_count>1 then AppendTo(PBC_recollect_path,",\\n");fi;
  AppendTo(PBC_recollect_path,"[",leaf[2],",\\\"",leaf[3],"\\\",",meta,",",actual,",",String(actual=expected),"]");
  if PBC_recollect_count mod 250=0 then
    Print("STANDARD_GAP_RECOLLECTED ",PBC_recollect_count," mismatches ",PBC_recollect_mismatches," runtime ",Runtime(),"\\n");
  fi;'''
assert body.count(oldcheck)==1;body=body.replace(oldcheck,newcheck)
body=body.replace('original_source_identity_replay_verified','standard_original_source_templates_recollected')
n=len(s['relative_orders']);con=[[] for _ in range(n)]
for i,j,w in s['conjugates']:assert len(con[i-1])==j-1;con[i-1].append(w)
data=dict(orders=s['relative_orders'],powers=s['powers'],conjugates=con,
          s=s['s'],r=s['r'],bs=s['left_s_frame'],br=s['left_r_frame'],
          cs=s['s_centralizers'],cr=s['r_centralizers'],s_image=s['s_image'],r_image=s['r_image'])
gap=CODE/'pbc_quotient86_standard_recollection.g'
path='LM8_PUSH/code/pbc_quotient86_standard_recollection.json'
gap.write_text('LoadPackage("polycyclic");;\nPBC_recollect_count:=0;; PBC_recollect_mismatches:=0;;\n'
               +'PBC_recollect_path:='+compact(path)+';;\nPrintTo(PBC_recollect_path,"[\\n");\n'
               +body+'\nPBC_data:=rec('+','.join(k+':='+compact(v) for k,v in data.items())+');;\n'
               +'PBC_leaves:='+compact(leaves)+';;\nAssert(0,PBC_Replay(PBC_data,PBC_leaves));\n'
               +'AppendTo(PBC_recollect_path,"\\n]\\n");\n'
               +'Print("STANDARD_RECOLLECTION_COMPLETE ",PBC_recollect_count," mismatches ",PBC_recollect_mismatches,"\\n");\nQUIT;\n')
report=dict(status='Prepared fresh standard original-source recollection; not yet completed',
            source_sha256=sha(source),original_trace_sha256=sha(trace),
            original_replay_routine_sha256=sha(old),generator_sha256=sha(__file__),
            generated_gap_sha256=sha(gap),source_templates=len(leaves),
            source_identity_templates=sum(r[2]=='identity' for r in leaves),
            scope='The first native raw target did not match standard GAP. This fresh computation retains every actual standard result and all mismatch counts; it does not approve the old quotient identity.')
(CODE/'pbc_quotient86_standard_recollection_inputs.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
