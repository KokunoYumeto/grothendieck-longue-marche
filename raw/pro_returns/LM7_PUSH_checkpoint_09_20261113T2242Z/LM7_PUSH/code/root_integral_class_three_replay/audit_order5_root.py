#!/usr/bin/env python3
"""Independent isolated replay of the complete D36 finite certificate.

The original inputs and authoritative outputs are read-only.  The ten
minimal files regenerate every new finite dependency in an isolated
directory, including exhaustive proper-image subtraction and both
opposite corrected boundary patterns.  Absolute source-file provenance
is compared by identical basename and the verified surface-file hash.
"""
from pathlib import Path
from hashlib import sha256
import json,shutil,subprocess,sys,time

HERE=Path(__file__).resolve().parent
def digest(p):return sha256(p.read_bytes()).hexdigest()
def main():
    start=time.time();manifest_path=HERE/'a_peripheral_order5_manifest.json'
    manifest=json.loads(manifest_path.read_text())
    protected={n:digest(HERE/n) for n in manifest['sha256']}
    assert protected==manifest['sha256']
    protected['a_peripheral_order5_manifest.json']=digest(manifest_path)
    protected['../sections/D_order5_agent.tex']=digest(HERE/'../sections/D_order5_agent.tex')
    replay=HERE/'root_order5_replay'
    replay.mkdir(exist_ok=False)
    for name in manifest['minimal_replay_files']:shutil.copy2(HERE/name,replay/name)
    with (replay/'root_replay.out').open('w') as out:
        proc=subprocess.run([sys.executable,str(replay/'a_peripheral_order5_replay.py')],
            cwd=replay,stdout=out,stderr=subprocess.STDOUT)
    assert proc.returncode==0
    result=json.loads((replay/'a_peripheral_order5_manifest.json').read_text())
    assert result['status']==manifest['status']=='PASS_COMPLETE_D36_REPLAY'
    comparisons=[]
    for name in manifest['sha256']:
        if name in manifest['minimal_replay_files']:
            assert digest(replay/name)==protected[name]
            continue
        old=json.loads((HERE/name).read_text());new=json.loads((replay/name).read_text())
        path_comparison=None
        if 'source_surface_file' in old:
            oldpath,newpath=Path(old.pop('source_surface_file')),Path(new.pop('source_surface_file'))
            assert oldpath.name==newpath.name
            assert digest(HERE/oldpath.name)==digest(replay/newpath.name)
            path_comparison={'surface_filename':oldpath.name,'exact_surface_hash_equal':True}
        assert old==new,name
        comparisons.append({'file':name,'all_mathematical_records_equal':True,
                            'source_file_comparison':path_comparison})
    for key in ('minimal_replay_files','steps','kernel_counts','no_flip_kernel_counts','positive_excess'):
        assert result[key]==manifest[key],key
    unchanged=all(digest(HERE/name)==h for name,h in protected.items())
    assert unchanged
    out={'all_passed':True,'isolated_driver_exit_code':proc.returncode,
         'minimal_input_files':len(manifest['minimal_replay_files']),
         'regenerated_authoritative_JSON_files':len(comparisons),
         'comparisons':comparisons,'kernel_counts':result['kernel_counts'],
         'opposite_no_flip_counts':result['no_flip_kernel_counts'],
         'positive_excess':result['positive_excess'],
         'original_artifacts_unchanged':unchanged,'protected_sha256':protected,
         'seconds':round(time.time()-start,3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='protected_sha256'},indent=2))
    print('ROOT_ORDER5_COMPLETE_REPLAY_PASS')

if __name__=='__main__':main()
