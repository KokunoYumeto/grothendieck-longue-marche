#!/usr/bin/env python3
"""Root replay of all frozen D65 finite certificates and literal inputs."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess,sys,time

W=Path(__file__).resolve().parents[1]
R=W/'D65_EXPERIMENTS'
A=Path(__file__).resolve().parent
M=R/'ledger/d_divided_compact_source_manifest.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(M)=='a0912a250ef5a225f30471f02de19b569333813c81ed66adfa0af0be2b25cde1'
m=json.loads(M.read_text())
def check_frozen():
    for f in m['owned_files']:
        p=R/f['path']
        assert sha(p)==f['sha256'] and p.stat().st_size==f['bytes'],f['path']
    for f in json.loads((R/'input_manifest.json').read_text()):
        assert sha(W/f['source'])==sha(W/f['copied'])==f['sha256'],f
check_frozen()
work=A/'fresh'/'code';fresh=A/'fresh_outputs'
assert not work.exists() and not fresh.exists()
work.mkdir(parents=True);fresh.mkdir()
programs=['d_compact_projective_trace','d_compact_full_trace','d_compact_rigid_source',
          'd_compact_permutation','d_compact_integral','d_compact_divided_correction',
          'd_compact_integral_exterior','d_source_centralizer_norm']
inputs=json.loads((R/'input_manifest.json').read_text())
for f in inputs:shutil.copyfile(W/f['copied'],work/Path(f['copied']).name)
for n in programs:shutil.copyfile(R/'code'/(n+'.py'),work/(n+'.py'))
shutil.copyfile(M,A/'author_manifest.json')
shutil.copyfile(R/'sections/D_divided_compact_source.tex',A/'author_proof.tex')
def without_clock(d):
    z=json.loads(json.dumps(d));z['summary'].pop('elapsed_seconds');return z
def stdout_without_clock(t):
    return re.sub(r'("elapsed_seconds"\s*:\s*)[-+0-9.eE]+',r'\1<actual elapsed_seconds retained separately>',t)
rows=[]
for n in programs:
    t0=time.monotonic()
    with (fresh/(n+'.out')).open('wb') as out,(fresh/(n+'.err')).open('wb') as err:
        run=subprocess.run([sys.executable,str(work/(n+'.py'))],cwd=work,stdout=out,stderr=err)
    assert run.returncode==0,(n,run.returncode,(fresh/(n+'.err')).read_text())
    assert (fresh/(n+'.err')).stat().st_size==0,n
    j=work/(n+'.json');shutil.copyfile(j,fresh/j.name)
    actual=json.loads(j.read_text());expected=json.loads((R/'code'/j.name).read_text())
    assert without_clock(actual)==without_clock(expected),n+' complete JSON'
    assert stdout_without_clock((fresh/(n+'.out')).read_text())==stdout_without_clock((R/'code'/(n+'.out')).read_text()),n+' complete stdout'
    row={'program':n+'.py','source_sha256':sha(work/(n+'.py')),'exit_code':run.returncode,
         'complete_json_identity_after_projection_removing_only_summary_elapsed_seconds':True,
         'complete_stdout_identity_after_replacing_only_elapsed_seconds_value':True,
         'actual_elapsed_seconds':actual['summary']['elapsed_seconds'],
         'author_elapsed_seconds':expected['summary']['elapsed_seconds'],
         'root_elapsed_seconds':time.monotonic()-t0,
         'actual_fresh_json_sha256':sha(fresh/j.name),'actual_fresh_stdout_sha256':sha(fresh/(n+'.out')),
         'actual_fresh_stderr_bytes':0}
    rows.append(row);print(json.dumps(row),flush=True)
    # Only after whole-result equality, retain the exact declared dependency
    # hash for downstream programs. Every actual fresh output remains above.
    shutil.copyfile(R/'code'/j.name,j)
full=json.loads((work/'d_compact_full_trace.json').read_text())
assert all(c['full_projective_End_trace_rank']==0 and all(int(x,16)==0 for x in c['all512_columns']) for c in full['cases'])
rigid=json.loads((work/'d_compact_rigid_source.json').read_text())
assert all(c['rank']==16 and c['small_action_matches'] and c['isometry'] and c['pairing_error']=='0x0' for r in rigid['cases'] for c in r['cases'])
div=json.loads((work/'d_compact_divided_correction.json').read_text())
assert all(r['kernel_divided_norm_rank']==6 and r['coinvariant_dimension']==10 and r['source_s_image_rank']==4 and r['allowable_projective_trace_half_rank']==16 and r['source_s_image_equals_divided_norm_kernel'] for r in div['cases'])
check_frozen()
result={'status':'PASS','statement':'D.65','manifest_sha256':sha(M),
        'proof_sha256':sha(A/'author_proof.tex'),'frozen_owned_files_checked':len(m['owned_files']),
        'immutable_inputs_checked':inputs,'programs':rows,
        'excluded_JSON_paths':['/summary/elapsed_seconds'],
        'excluded_stdout_values':['elapsed_seconds'],
        'algebraic_fields_or_input_hashes_excluded':[],
        'downstream_policy':'An upstream frozen raw JSON is copied back only after the complete independently rebuilt result agrees under the displayed clock projection; all fresh bytes are separately retained.',
        'all_frozen_author_bytes_rechecked':True,
        'root_reading_scope':'All643 final proof lines and all1346 lines of the eight mathematical programs.'}
t=json.dumps(result,indent=2)+'\n';(A/'replay_audit.json').write_text(t);print(t,end='')
