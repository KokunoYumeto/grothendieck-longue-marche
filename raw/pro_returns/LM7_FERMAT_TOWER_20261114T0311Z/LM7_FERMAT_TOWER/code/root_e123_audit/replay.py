"""Root full-manifest check and fresh source-only replay for frozen E123."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
AUTHOR = ROOT/'research_e123'
GP = ROOT/'research_e52/vendor/pari-2.19.0/Olinux-x86_64/gp-dyn'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    manifest_path = AUTHOR/'ledger/e_fiftythree_positional_manifest.json'
    raw = manifest_path.read_bytes()
    assert sha(raw) == 'f375db968bbce03f11ca1ea434a9c52f7998cc87a6426ea69e9183909336224a'
    manifest = json.loads(raw)
    assert manifest['statement']=='E.123' and manifest['status']=='FROZEN'
    assert len(manifest['owned_files'])==304 and len(manifest['immutable_inputs'])==8

    def check_author():
        for item in manifest['owned_files']+manifest['immutable_inputs']:
            data = (AUTHOR/item['path']).read_bytes()
            assert len(data)==item['bytes'] and sha(data)==item['sha256'], item

    check_author()
    (BASE/'author_manifest.json').write_bytes(raw)
    shutil.copy2(AUTHOR/manifest['proof'], BASE/'author_proof.tex')
    assert sha((BASE/'author_proof.tex').read_bytes())=='70a7e93c7a7466069c375505991bb9a273e2c7bebf95164e2734a17a3c2908a4'
    replay_tree = BASE/'replay_tree'
    replay_tree.mkdir()
    code = replay_tree/'code'
    code.mkdir()
    inputs = replay_tree/'inputs'
    inputs.mkdir()
    for item in manifest['immutable_inputs']:
        relative = Path(item['path'])
        destination = replay_tree/relative
        destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(AUTHOR/relative,destination)
    names = ['e53_positional_unit.py','e53_positional_verify.gp',
             'e53_positional_genus_pivots.gp','e53_positional_presentation.gp',
             'e53_positional_lower_export.gp','e53_positional_make_ideals.py',
             'e53_positional_ideals.gp','e53_positional_maps.py']
    for name in names:
        script = AUTHOR/'code'/name
        shutil.copy2(script,code/name)
        for suffix in ['.out','.err','.json','.bin']:
            file = script.with_suffix(suffix)
            if file.exists(): shutil.copy2(file,code/file.name)
    driver = code/'e53_positional_replay.py'
    shutil.copy2(AUTHOR/'code'/driver.name,driver)
    command = [sys.executable,str(driver),'--gp',str(GP),'--label','root_fresh']
    run = subprocess.run(command,cwd=replay_tree,capture_output=True,timeout=120)
    driver.with_suffix('.out').write_bytes(run.stdout)
    driver.with_suffix('.err').write_bytes(run.stderr)
    assert run.returncode==0 and run.stderr==b'',(run.returncode,run.stderr.decode())
    replay = json.loads((replay_tree/'audit/root_fresh/verification.json').read_text())
    assert replay['status']=='PASS' and replay['excluded_fields']==[]
    assert len(replay['steps'])==8
    assert all(r['exit_code']==0 and r['stdout_byte_identity'] and r['stderr_byte_identity'] for r in replay['steps'])
    assert replay['JSON_byte_identity']==['e53_positional_unit.json','e53_positional_maps.json']
    assert replay['generated_standalone_source_byte_identity']
    assert len(replay['complete_binary_comparisons'])==2
    assert all(r['complete_GEN_identity'] for r in replay['complete_binary_comparisons'])
    assert [r['components'] for r in replay['complete_binary_comparisons']]==[4,13]
    standalone = replay_tree/'audit/root_fresh/fresh/code/e53_positional_ideals.out'
    lines = [json.loads(line) for line in standalone.read_text().splitlines() if line.startswith('{')]
    assert lines[-1]['status']=='PASS'
    assert lines[0]['upper_ideal_equalities']==7 and lines[0]['lower_ideal_equalities']==2
    assert lines[0]['unconditional_maximal_orders']
    check_author()
    result = {
        'status':'PASS','frozen_manifest_sha256':sha(raw),
        'owned_files_checked_before_and_after':304,'immutable_inputs_checked_before_and_after':8,
        'whole_proof_sha256':manifest['proof_sha256'],
        'full_replay_exit_code':run.returncode,'full_replay_stderr_bytes':len(run.stderr),
        'final_mathematical_stages':8,
        'complete_stdout_and_stderr_byte_identity':True,
        'complete_JSON_byte_identity':replay['JSON_byte_identity'],
        'generated_standalone_source_byte_identity':True,
        'complete_binary_comparisons':replay['complete_binary_comparisons'],
        'binary_serialization':replay['binary_serialization'],
        'standalone_nf_only_ideal_equalities':9,
        'unconditional_maximal_order_checks':2,
        'excluded_fields':[],'author_sources_modified':False,
        'checked_utc':datetime.now(timezone.utc).isoformat()}
    (BASE/'replay_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
