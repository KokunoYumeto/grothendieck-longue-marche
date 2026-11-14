#!/usr/bin/env python3
"""Isolated replay of the entire E71 matrix/distribution fibre certificate."""
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
        return {k:mathematical(v) for k,v in value.items()
                if k not in {'seconds','total_seconds'}}
    if isinstance(value,list):return [mathematical(v) for v in value]
    return value


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--destination',required=True)
    parser.add_argument('--manifest',default='research/E71_authoritative_manifest.json')
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
    started=time.monotonic()
    for source,executable in [('de_a6_schreier.cpp','de_a6_schreier_fast'),
                              ('a_cm_fixed_base.cpp','a_cm_fixed_base')]:
        with (destination/(executable+'_compile.out')).open('w') as out,\
             (destination/(executable+'_compile.err')).open('w') as err:
            subprocess.run(['g++','-std=c++17','-O3','-DNDEBUG',source,'-o',executable],
                           cwd=work,stdout=out,stderr=err,check=True)
    generated_json={stem+'.json' for stem in manifest['mathematical_stage_stems']}
    stages=[]
    for stem in manifest['mathematical_stage_stems']:
        tick=time.monotonic()
        with (work/(stem+'.out')).open('w') as out,(work/(stem+'.err')).open('w') as err:
            subprocess.run([sys.executable,stem+'.py'],cwd=work,stdout=out,stderr=err,check=True)
        original=json.loads((ROOT/'code'/(stem+'.json')).read_text())
        replay=json.loads((work/(stem+'.json')).read_text())
        a,b=mathematical(original),mathematical(replay)
        # Every provenance hash is first checked against its actual input.
        # Only hashes of generated JSON, whose measured seconds vary, are
        # removed from the mathematical equality. All fixed hashes remain.
        for obj,base in ((a,ROOT/'code'),(b,work)):
            for name,value in list(obj.get('input_sha256',{}).items()):
                assert digest(base/name)==value,(stem,name,'input provenance')
                if name in generated_json:del obj['input_sha256'][name]
        assert a==b,(stem,'mathematical JSON')
        original_npz=ROOT/'code'/(stem+'.npz')
        if original_npz.exists():
            aa=np.load(original_npz);bb=np.load(work/(stem+'.npz'))
            assert aa.files==bb.files,(stem,'array names')
            for key in aa.files:assert np.array_equal(aa[key],bb[key]),(stem,key)
        stages.append({'program':stem+'.py','all_mathematical_JSON_and_NPZ_values_exact':True,
                       'seconds':round(time.monotonic()-tick,6)})
        print('Replayed',stem,stages[-1]['seconds'],flush=True)
    sys.path.insert(0,str(work))
    from de_a6_schreier_certificate import read_certificate,verify_words
    certificates=[]
    for stem in manifest['complete_certificate_stems']:
        a=read_certificate(ROOT/'code'/(stem+'.bin'))
        b=read_certificate(work/(stem+'.bin'));verify_words(b)
        assert a.keys()==b.keys()
        for key in a:
            if isinstance(a[key],np.ndarray):assert np.array_equal(a[key],b[key]),(stem,key)
            else:assert a[key]==b[key],(stem,key)
        for extension in ['.input','.base']:
            path=ROOT/'code'/(stem+extension)
            if path.exists():assert path.read_bytes()==(work/(stem+extension)).read_bytes()
        certificates.append(stem+'.bin')
    assert all(digest(ROOT/name)==value for name,value in protected.items())
    result={'status':'PASS_ISOLATED_COMPLETE_E71_FULL_K6_FPRIME_MATRIX_FIBRES',
            'stages':stages,'complete_certificates_exact_and_replayed':certificates,
            'protected_originals_unchanged':len(protected),
            'all_18432_literal_source_words_replayed':True,
            'entire_K6_intersect_Fprime_domain_retained':True,
            'seconds':round(time.monotonic()-started,6)}
    (destination/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
