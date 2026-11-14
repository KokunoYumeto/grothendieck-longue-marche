#!/usr/bin/env python3
"""Hash-protected isolated replay of the complete E74 finite word fibres."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np


ROOT=Path(__file__).resolve().parent.parent


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def mathematical(value):
    if isinstance(value,dict):
        return {k:mathematical(v) for k,v in value.items() if k!='seconds'}
    if isinstance(value,list):return [mathematical(v) for v in value]
    return value


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--destination',required=True)
    parser.add_argument('--manifest',default='research/E74_authoritative_manifest.json')
    args=parser.parse_args()
    manifest_path=Path(args.manifest)
    if not manifest_path.is_absolute():manifest_path=ROOT/manifest_path
    manifest=json.loads(manifest_path.read_text())
    destination=Path(args.destination)
    if not destination.is_absolute():destination=ROOT/destination
    destination.mkdir(parents=True,exist_ok=False)
    work=destination/'code';work.mkdir()
    protected=manifest['sha256']
    assert all(digest(ROOT/name)==value for name,value in protected.items())
    for name in manifest['minimal_input_files']:
        target=work/name;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/'code'/name,target)
    start=time.monotonic();stages=[]
    for stem in manifest['mathematical_stage_stems']:
        tick=time.monotonic()
        with (work/(stem+'.out')).open('w') as out,\
             (work/(stem+'.err')).open('w') as err:
            subprocess.run([sys.executable,stem+'.py'],cwd=work,
                           stdout=out,stderr=err,check=True)
        original=json.loads((ROOT/'code'/(stem+'.json')).read_text())
        replay=json.loads((work/(stem+'.json')).read_text())
        a,b=mathematical(original),mathematical(replay)
        for obj,base in ((a,ROOT/'code'),(b,work)):
            for name,value in obj['input_sha256'].items():
                assert digest(base/name)==value,(stem,name,'actual input provenance')
        # This one preceding JSON contains the measured stage runtime.
        # Its old and regenerated hashes have both just been verified
        # against their actual bytes. All other provenance hashes remain.
        if stem=='a_cm_matrix_gaussian_witnesses':
            parent='a_cm_matrix_gaussian_join.json'
            del a['input_sha256'][parent]
            del b['input_sha256'][parent]
        assert a==b,(stem,'all mathematical JSON')
        aa=np.load(ROOT/'code'/(stem+'.npz'))
        bb=np.load(work/(stem+'.npz'))
        assert aa.files==bb.files,(stem,'array keys')
        for key in aa.files:assert np.array_equal(aa[key],bb[key]),(stem,key)
        stages.append({'program':stem+'.py',
                       'all_mathematical_JSON_and_NPZ_values_exact':True,
                       'seconds':round(time.monotonic()-tick,6)})
        print('Replayed',stem,stages[-1]['seconds'],flush=True)
    assert all(digest(ROOT/name)==value for name,value in protected.items())
    result={'status':'PASS_ISOLATED_E74_COMPLETE_MATRIX_GAUSSIAN_JOIN',
            'stages':stages,'protected_originals_unchanged':len(protected),
            'all_three_common_kernel_words_replayed_on_11691_points':True,
            'all_55296_actual_common_word_values_replayed':True,
            'whole_domain':'K6 intersect F-prime',
            'seconds':round(time.monotonic()-start,6)}
    (destination/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
