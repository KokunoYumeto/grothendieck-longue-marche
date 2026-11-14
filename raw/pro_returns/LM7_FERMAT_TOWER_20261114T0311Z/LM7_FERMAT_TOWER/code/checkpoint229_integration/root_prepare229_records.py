#!/usr/bin/env python3
"""Preserve validated packaging guards and bind actual review executions."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

R=Path(__file__).resolve().parent
F=R/'root_archive_format'
O=R/'root_output_records229'
O.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2)+'\n'
records=[]
for p in sorted((R/'root_d66_audit/fresh_outputs').glob('*')):
    if p.suffix not in {'.out','.err'}:continue
    q=R/'root_d66_audit/fresh/code'/p.name
    assert not q.exists();shutil.copy2(p,q)
    assert p.read_bytes()==q.read_bytes()
    records.append({'actual_capture':str(p.relative_to(R)),
                    'source_companion':str(q.relative_to(R)), 'sha256':sha(q)})

silent=[]
for label,p,args in [
    ('author_exact',R/'research_e120/code/a_e120_exact.py',[]),
    ('author_smith',R/'research_e120/code/a_local_smith.py',['--help']),
    ('principal_exact',R/'root_e120_audit/principal_cubic_fresh/code/a_e120_exact.py',[])]:
    d=O/label;d.mkdir()
    before=sha(p)
    proc=subprocess.run([sys.executable,str(p),*args],cwd=p.parent,capture_output=True)
    assert proc.returncode==0 and not proc.stderr and sha(p)==before
    for suffix,b in [('.out',proc.stdout),('.err',proc.stderr)]:
        (d/(p.stem+suffix)).write_bytes(b)
    row={'source':str(p.relative_to(R)),'source_sha256':before,
         'arguments':args,'exit_code':proc.returncode,
         'stdout':str((d/(p.stem+'.out')).relative_to(R)),
         'stdout_sha256':hashlib.sha256(proc.stdout).hexdigest(),
         'stderr':str((d/(p.stem+'.err')).relative_to(R)),
         'stderr_sha256':hashlib.sha256(proc.stderr).hexdigest()}
    silent.append(row)
    if label=='principal_exact':
        for suffix in ['.out','.err']:shutil.copy2(d/(p.stem+suffix),p.with_suffix(suffix))
        status={'status':'silent module executed successfully','exit_code':0,
                'source_sha256':before,'reason':'The exact coefficient helper has no main procedure or print statement. This complete standalone execution returned empty stdout and stderr; the successful principal cubic-cover run imports and exercises it.',
                'importing_certificate':'a_principal_cubic_cover.py'}
        p.with_name(p.stem+'_status.json').write_text(enc(status))

# Keep the first prepared writer and its actual preparation result intact.
H=F/'history/pre_guard_restore229';H.mkdir(parents=True)
for name in ['package229.py','prepare229.out','prepare229.err']:
    shutil.copy2(F/name,H/(name+'.md' if name.endswith('.py') else name))
p=(F/'package229.py').read_text()
prior=(R/'LM7_FERMAT_TOWER/code/package.py').read_text()
a="            else:\n                assert status.get('status') == 'failed before result'"
z="                failed_empty_outputs.append(str(script.relative_to(BASE)))"
i=p.index(a);j=p.index(z,i)+len(z)
a2="            else:\n                error = status_path.parent / status['stderr_path']"
i2=prior.index(a2);j2=prior.index(z,i2)+len(z)
p=p[:i]+prior[i2:j2]+p[j:]
needle="            if status.get('status') == 'interrupted before result':"
assert p.count(needle)==1
block="""            if status.get('status') == 'silent module executed successfully':
                assert script.suffix == '.py' and status['exit_code'] == 0
                assert status['source_sha256'] == sha(script.read_bytes())
                stderr = script.with_suffix('.err')
                assert stderr in files and stderr.read_bytes() == b''
                consumer = script.parent / status['importing_certificate']
                assert consumer in files and consumer.with_suffix('.out') in files
                assert consumer.with_suffix('.out').stat().st_size > 0
                continue
"""
p=p.replace(needle,block+needle)
compile(p,'package229.py','exec');(F/'package229.py').write_text(p)
data={'status':'PASS','actual_capture_bindings':records,
      'actual_helper_executions':silent,
      'packager_sha256':sha(F/'package229.py'),
      'restored_guard':'Exact prior GP interpreter-error evidence guard, including actual process exit zero.',
      'added_guard':'Silent Python modules require their actual zero exit, whole source hash, empty stderr and a retained successful importing program.',
      'current_deliverable_modified':False}
(R/'root_output_bindings229.json').write_text(enc(data));print(enc(data),end='')
