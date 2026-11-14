#!/usr/bin/env python3
"""Fresh isolated replay of the unnumbered K3 source-map certificate.

The authoritative source/results are read-only. A fresh destination is
mandatory; the original failed attempt remains part of the protected
provenance but is not deliberately repeated.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent.parent


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def mathematical(x):
    if isinstance(x,dict):
        return {k:mathematical(v) for k,v in x.items() if k != 'seconds'}
    if isinstance(x,list):
        return [mathematical(v) for v in x]
    return x


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--destination',required=True)
    args=ap.parse_args()
    destination=Path(args.destination)
    if not destination.is_absolute():
        destination=ROOT/destination
    destination.mkdir(parents=True,exist_ok=False)
    manifest=json.loads((ROOT/'research/A_K3_authoritative_manifest.json').read_text())
    protected=manifest['sha256']
    assert all(digest(ROOT/p)==h for p,h in protected.items())
    work=destination/'code'
    work.mkdir()
    for name in manifest['minimal_input_files']:
        shutil.copy2(ROOT/'code'/name,work/name)
    start=time.monotonic()
    stages=[]
    command=['g++','-std=c++17','-O3','-DNDEBUG','de_a6_schreier.cpp','-o','de_a6_schreier_fast']
    with (destination/'compile.out').open('w') as out,(destination/'compile.err').open('w') as err:
        subprocess.run(command,cwd=work,stdout=out,stderr=err,check=True)
    for name in ('a_cm_kummer3_probe','a_cm_kummer3_orbit','a_cm_kummer3_core'):
        t=time.monotonic()
        with (work/(name+'.out')).open('w') as out,(work/(name+'.err')).open('w') as err:
            subprocess.run([sys.executable,name+'.py'],cwd=work,stdout=out,stderr=err,check=True)
        original=json.loads((ROOT/'code'/(name+'.json')).read_text())
        replay=json.loads((work/(name+'.json')).read_text())
        assert mathematical(original)==mathematical(replay),name
        stages.append({'program':name+'.py','mathematical_JSON_exact':True,
                       'seconds':round(time.monotonic()-t,6)})
    original=np.load(ROOT/'code/a_cm_kummer3_core.npz')
    replay=np.load(work/'a_cm_kummer3_core.npz')
    assert set(original.files)==set(replay.files)
    assert all(np.array_equal(original[k],replay[k]) for k in original.files)
    sys.path.insert(0,str(work))
    from de_a6_schreier_certificate import read_certificate,verify_words
    checks=[]
    for name in manifest['complete_certificate_stems']:
        a=read_certificate(ROOT/'code'/(name+'.bin'))
        b=read_certificate(work/(name+'.bin'))
        verify_words(b)
        assert a.keys()==b.keys()
        for k in a:
            if isinstance(a[k],np.ndarray):
                assert np.array_equal(a[k],b[k]),(name,k)
            else:
                assert a[k]==b[k],(name,k)
        checks.append({'certificate':name+'.bin','all_literal_arrays_exact':True})
    assert all(digest(ROOT/p)==h for p,h in protected.items())
    result={'status':'PASS_ISOLATED_K3_SOURCE_MAP_BATCH',
            'stages':stages,'complete_certificates':checks,
            'all_NPZ_arrays_exact':True,
            'protected_files_unchanged':len(protected),
            'scope':'Finite source maps and same-domain Goursat comparison only; no full-GT character value.',
            'seconds':round(time.monotonic()-start,6)}
    (destination/'replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
