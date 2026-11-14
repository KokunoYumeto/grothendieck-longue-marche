#!/usr/bin/env python3
"""Retain exact failed-run evidence and observed historical-source replays."""
from pathlib import Path
import hashlib,json,posixpath,shutil

R=Path(__file__).resolve().parent;B=R/'LM7_FERMAT_TOWER'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
enc=lambda x:json.dumps(x,indent=2)+'\n'
read=lambda p:json.loads(p.read_text())
ledger=B/'ledger/execution_status229.json'
assert not ledger.exists()
executions=[];copied=[];statuses=[]
def copy(p,q):
    q.parent.mkdir(parents=True,exist_ok=True)
    if q.exists():assert p.read_bytes()==q.read_bytes(),str(q)
    else:shutil.copy2(p,q)
    copied.append({'source':str(p.relative_to(R)),'archive':str(q.relative_to(B)),'sha256':sha(q)})
def status(p,d):
    q=p.with_name(p.stem+'_status.json')
    if q.exists():assert q.read_text()==enc(d),str(q)
    else:q.write_text(enc(d))
    statuses.append({'path':str(q.relative_to(B)),'sha256':sha(q)})

spec=[
 ('code/e123_bundle/audit/pre_uniform_branch/code/e53_positional_replay.py',
  'code/e123_bundle/audit/pre_uniform_branch/amendment.json','failed_replay_exit',
  'The original complete binary comparison exceeded the initial PARI stack.',None),
 ('code/e123_bundle/code/history/first_finite_checker/e53_positional_maps.py',
  'code/e123_bundle/code/history/first_finite_checker/amendment.json','initial_checker_exit',
  'The first checker expected JSON where the nf-only verifier emits literal PASS lines.',None),
 ('code/e123_bundle/code/history/primary_projection_initial/e53_positional_primary_amend.py',
  'code/e123_bundle/code/history/primary_projection_initial/provenance.json','exit_code',
  'The exact text-match assertion failed before the theorem was changed.',None),
 ('code/e124_bundle/history/component_modulus/e53_ordinary_genus.gp',
  'code/e124_bundle/history/component_modulus/provenance.json','process_exit_code',
  'GP reported an invalid vector modulus and skipped the source.', 'Mod: forbidden division'),
 ('code/e124_bundle/history/first_lower_input/code/e53_ordinary_kernel.gp',
  'code/e124_bundle/history/first_lower_input/provenance.json','process_exit_code',
  'The actual first binary input was the positional transition object rather than the six-prime object.', 'not a vector'),
 ('code/e124_bundle/history/prime_generator_assumption/e53_ordinary_genus.gp',
  'code/e124_bundle/history/prime_generator_assumption/provenance.json','GP_process_exit_code',
  'The dependent GP stage reported its missing generated input.', 'error opening input file'),
 ('code/e124_bundle/history/prime_generator_assumption/e53_ordinary_genus_chars.py',
  'code/e124_bundle/history/prime_generator_assumption/provenance.json','Python_exit_code',
  'The original prime-ideal assumption failed for a composite HNF ideal norm.',None),
 ('code/e124_bundle/history/vecsmall_serialization/e53_ordinary_summary.py',
  'code/e124_bundle/history/vecsmall_serialization/provenance.json','summary_exit_code',
  'The successful GP arithmetic printed Vecsmall syntax where the summary expected JSON.',None)]
pending=[]
for name,evidence,key,reason,marker in spec:
    p=B/name;ep=B/evidence;e=read(ep);exit_code=e[key]
    assert p.with_suffix('.out').read_bytes()==b''
    err=p.with_suffix('.err');assert err.stat().st_size
    row={'program':name,'source_sha256':sha(p),'exit_code':exit_code,
         'original_provenance':evidence,'original_provenance_sha256':sha(ep),
         'original_exit_field':key,'stderr':str(err.relative_to(B)),
         'stderr_sha256':sha(err),'reason':reason}
    executions.append(row)
    d={'status':'failed with interpreter-reported error' if marker else 'failed before result',
       'exit_code':exit_code,'source_sha256':sha(p),'reason':reason,
       'stderr_path':err.name,'stderr_sha256':sha(err),
       'original_provenance':evidence,'original_provenance_sha256':sha(ep)}
    if marker:
        assert exit_code==0 and marker in err.read_text() and '... skipping file ' in err.read_text()
        d.update(exact_error_marker=marker,execution_evidence='ledger/execution_status229.json',execution_record=row)
    else:assert exit_code==1
    pending.append((p,d))

A=R/'research_e120';src=A/'audit/history_status'
assert sha(src/'status.json')=='4b066e6420962241f63c54bed319cf65d128ceb6ea34610dbcb334dfb3979782'
h=read(src/'status.json');assert h['status']=='PASS'
T=B/'code/e120_frozen229'
for p in sorted(src.rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts:
        assert p.suffix in {'.py','.json','.out','.err','.txt'},str(p)
        copy(p,T/p.relative_to(A))
for row in h['failed_history_replays']:
    for key in ['historical_source','historical_stdout','historical_stderr','replay_stdout','replay_stderr']:
        r=row[key];assert sha(T/r['path'])==r['sha256'] and (T/r['path']).stat().st_size==r['bytes']
    assert row['original_exit_artifact'] is None and row['observed_replay_exit_code']==1
    p=T/row['historical_source']['path']
    d={'status':'historical failure with observed source replay','original_exit_code':None,
       'observed_replay_exit_code':1,'source_sha256':sha(p),
       'reason':'The original empty stdout and exact traceback are retained. The unchanged historical source was separately replayed with observed exit1; the original process exit was not separately recorded.',
       'historical_source_path':row['historical_source']['path'],
       'evidence':'code/e120_frozen229/audit/history_status/status.json',
       'evidence_sha256':sha(T/'audit/history_status/status.json'),
       'evidence_root':'code/e120_frozen229',
       'stderr_path':p.with_suffix('.err').name,'stderr_sha256':sha(p.with_suffix('.err'))}
    status(p,d)
    q=T/row['replay_cwd']/row['replay_command'][-1]
    assert sha(q)==row['historical_source']['sha256']
    copy(T/row['replay_stdout']['path'],q.with_suffix('.out'))
    copy(T/row['replay_stderr']['path'],q.with_suffix('.err'))
    status(q,{'status':'failed before result','exit_code':1,'source_sha256':sha(q),
              'reason':'Actual observed isolated execution of the unchanged historical source.',
              'stderr_path':q.with_suffix('.err').name,'stderr_sha256':sha(q.with_suffix('.err')),
              'execution_evidence':d['evidence'],'historical_source_path':d['historical_source_path']})

# Bind helpers in the isolated replay trees to their actually executed,
# byte-identical standalone records. The final importing mathematics is
# retained at its native source path in the same frozen bundle.
helper=read(R/'root_output_bindings229.json')['actual_helper_executions'][:2]
for directory in sorted(p for p in (T/'audit/history_status').iterdir() if p.is_dir()):
    for row in helper:
        p=directory/Path(row['source']).name;assert sha(p)==row['source_sha256']
        copy(R/row['stdout'],p.with_suffix('.out'));copy(R/row['stderr'],p.with_suffix('.err'))
        consumer=T/'code'/('a_elliptic_tor_symbol.py' if not row['arguments'] else 'a_theta_principal_distribution.py')
        status(p,{'status':'silent module executed successfully' if not row['arguments'] else 'help entry point executed; arithmetic exercised by importing certificate',
                  'exit_code':0,'source_sha256':sha(p),'reason':'Exact copy of the actual standalone output for this byte-identical helper; complete mathematical consumers and their outputs remain retained.',
                  'importing_certificate':posixpath.relpath(consumer,p.parent),'actual_execution':row})
    for p in directory.glob('*.json'):
        if p.name.endswith('_status.json'):continue
        assert p.read_bytes()==(A/'code'/p.name).read_bytes(),str(p)

# This ledger is the exact process evidence referenced by the GP statuses.
data={'status':'PASS','executions':executions,'additional_exact_files':copied,
      'history_source_replay_evidence_sha256':sha(T/'audit/history_status/status.json'),
      'original_E120_process_exits_not_invented':True}
ledger.write_text(enc(data));lh=sha(ledger)
for p,d in pending:
    if d['status']=='failed with interpreter-reported error':d['execution_evidence_sha256']=lh
    status(p,d)

p=B/'code/package.py';old=p.read_bytes();hist=B/'code/packaging229_history/pre_history_status/package.py.md'
hist.parent.mkdir(parents=True);assert not hist.exists();hist.write_bytes(old)
s=old.decode();needle="            if status.get('status') == 'silent module executed successfully':"
assert s.count(needle)==1
block="""            if status.get('status') == 'historical failure with observed source replay':
                assert status['original_exit_code'] is None
                assert status['observed_replay_exit_code'] == 1
                assert sha(script.read_bytes()) == status['source_sha256']
                evidence = BASE / status['evidence']
                assert evidence in files and sha(evidence.read_bytes()) == status['evidence_sha256']
                rows = json.loads(evidence.read_text())['failed_history_replays']
                matched = [r for r in rows if r['historical_source']['path'] == status['historical_source_path']]
                assert len(matched) == 1
                row = matched[0]
                assert row['original_exit_artifact'] is None and row['observed_replay_exit_code'] == 1
                assert row['historical_source']['sha256'] == sha(script.read_bytes())
                for key in ['historical_stdout','historical_stderr','replay_stdout','replay_stderr']:
                    item = row[key]
                    path = BASE / status['evidence_root'] / item['path']
                    assert path in files and len(path.read_bytes()) == item['bytes']
                    assert sha(path.read_bytes()) == item['sha256']
                assert row['historical_stderr']['bytes'] > 0 and row['replay_stderr']['bytes'] > 0
                failed_empty_outputs.append(str(script.relative_to(BASE)))
                continue
"""
s=s.replace(needle,block+needle);compile(s,str(p),'exec');p.write_text(s)

unexplained=[]
for p in sorted((B/'code').rglob('*')):
    if p.suffix not in {'.py','.gp'}:continue
    out=p.with_suffix('.out')
    if not out.exists():unexplained.append(str(p.relative_to(B)))
    elif not out.stat().st_size and not p.with_name(p.stem+'_status.json').exists():
        registry=read(B/'ledger/execution_snapshot_outputs.json')
        if str(p.relative_to(B)) not in registry:unexplained.append(str(p.relative_to(B)))
assert not unexplained,unexplained
print(enc({'status':'PASS','new_status_records':statuses,'new_exact_file_count':len(copied),
           'process_evidence_sha256':lh,'packager_sha256':sha(p=B/'code/package.py'),
           'original_process_exits_invented':0,'unexplained_empty_or_missing_outputs':unexplained}),end='')
