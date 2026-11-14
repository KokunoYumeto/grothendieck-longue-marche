#!/usr/bin/env python3
"""Isolated, provenance-aware replay of the four E69 programs."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
import numpy as np


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--directory')
    args=parser.parse_args();root=Path(__file__).resolve().parents[1]
    out=Path(args.directory).resolve() if args.directory else root/'research/E69_isolated_replay'
    if out.exists():raise RuntimeError('Choose a fresh isolated replay directory: '+str(out))
    out.mkdir(parents=True);code=out/'code';code.mkdir()
    manifest=json.loads((root/'research/E69_authoritative_manifest.json').read_text())
    protected={**manifest['files'],**manifest['inputs']}
    assert all(digest(root/p)==h for p,h in protected.items())
    for name in protected:
        if name.startswith('code/'):
            shutil.copy2(root/name,code/Path(name).name)
    results=[];start=time.monotonic()
    for name in manifest['replay_order']:
        then=time.monotonic()
        with (code/(name+'.out')).open('w') as stdout,(code/(name+'.err')).open('w') as stderr:
            p=subprocess.run([sys.executable,str(code/(name+'.py'))],cwd=code,
                             stdout=stdout,stderr=stderr)
        assert p.returncode==0,(name,p.returncode)
        old=json.loads((root/'code'/(name+'.json')).read_text())
        got=json.loads((code/(name+'.json')).read_text())
        provenance=[]
        for side,base,data in [('original',root/'code',old),('replay',code,got)]:
            for f,h in data.get('input_sha256',{}).items():
                assert digest(base/f)==h,(side,name,f)
                provenance.append([side,f,h])
        # Only elapsed time and byte-level provenance are removed after
        # the latter has been checked against every actual input file.
        def mathematical(data):
            return {k:v for k,v in data.items() if k not in ('seconds','input_sha256')}
        assert mathematical(old)==mathematical(got),name
        arrays=[]
        if (code/(name+'.npz')).exists():
            a=np.load(root/'code'/(name+'.npz'));b=np.load(code/(name+'.npz'))
            assert a.files==b.files
            for k in a.files:assert np.array_equal(a[k],b[k]),(name,k)
            arrays=a.files
        results.append({'program':name,'status':'PASS','seconds':round(time.monotonic()-then,6),
                        'all_mathematical_JSON_fields_identical':True,
                        'identical_NPZ_arrays':arrays,'verified_input_provenance':provenance})
        print(name,'PASS',results[-1]['seconds'],flush=True)
    assert all(digest(root/p)==h for p,h in protected.items())
    record={'status':'PASS_COMPLETE_ISOLATED_E69_REPLAY','seconds':round(time.monotonic()-start,6),
            'protected_originals_unchanged':len(protected),'results':results}
    (out/'replay.json').write_text(json.dumps(record,indent=2)+'\n')
    print(record['status'],record['seconds'],flush=True)


if __name__=='__main__':main()
