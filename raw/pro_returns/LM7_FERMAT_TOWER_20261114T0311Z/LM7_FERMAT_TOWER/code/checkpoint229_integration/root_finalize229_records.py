#!/usr/bin/env python3
"""Retain the observed administrative failure and completed status repair."""
from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parent;B=R/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
H=B/'code/packaging229_history/failed_status_input_scan';H.mkdir(parents=True)
for p in (R/'root_execution_status229_history/first_input_scan').iterdir():
    shutil.copy2(p,H/p.name)
p=H/'root_record_execution_status229.py';err=p.with_suffix('.err')
assert p.with_suffix('.out').read_bytes()==b'' and 'a_e120_exact_status.json' in err.read_text()
d={'status':'failed before result','exit_code':1,'source_sha256':sha(p),
   'reason':'The observed first bookkeeping run included its newly generated helper status JSON in a scan restricted to immutable arithmetic inputs. The corrected run skips only those generated status records; all source and output bytes remain unchanged.',
   'stderr_path':err.name,'stderr_sha256':sha(err)}
p.with_name(p.stem+'_status.json').write_text(json.dumps(d,indent=2)+'\n')
for name in ['root_record_execution_status229.py','root_record_execution_status229.out','root_record_execution_status229.err']:
    shutil.copy2(R/name,B/'code/checkpoint229_integration'/name)
q=json.loads((R/'root_record_execution_status229.out').read_text())
assert q['status']=='PASS' and not q['unexplained_empty_or_missing_outputs']
print(json.dumps({'status':'PASS','actual_failed_exit':1,
                  'failure_status_sha256':sha(p.with_name(p.stem+'_status.json')),
                  'completed_status_record_sha256':sha(R/'root_record_execution_status229.out')},indent=2))
