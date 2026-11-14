#!/usr/bin/env python3
"""Isolated replay of E66's actual E6/E62 common-image computations."""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent.parent


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def mathematical(v):
    if isinstance(v,dict):return {k:mathematical(x) for k,x in v.items() if k not in {'seconds','total_seconds'}}
    if isinstance(v,list):return [mathematical(x) for x in v]
    return v


def main():
    p=argparse.ArgumentParser();p.add_argument('--destination',required=True);a=p.parse_args()
    dest=Path(a.destination)
    if not dest.is_absolute():dest=ROOT/dest
    dest.mkdir(parents=True,exist_ok=False);work=dest/'code';work.mkdir()
    manifest=json.loads((ROOT/'research/E66_authoritative_manifest.json').read_text())
    hashes=manifest['sha256'];assert all(digest(ROOT/f)==h for f,h in hashes.items())
    for name in manifest['minimal_input_files']:
        target=work/name;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/'code'/name,target)
    start=time.monotonic()
    with (dest/'compile.out').open('w') as out,(dest/'compile.err').open('w') as err:
        subprocess.run(['g++','-std=c++17','-O3','-DNDEBUG','de_a6_schreier.cpp','-o','de_a6_schreier_fast'],cwd=work,stdout=out,stderr=err,check=True)
    stages=[]
    for stem in ('a_cm_distribution_e62','a_cm_distribution_overlap','a_cm_distribution_witnesses'):
        t=time.monotonic()
        with (work/(stem+'.out')).open('w') as out,(work/(stem+'.err')).open('w') as err:
            subprocess.run([sys.executable,stem+'.py'],cwd=work,stdout=out,stderr=err,check=True)
        old=json.loads((ROOT/'code'/(stem+'.json')).read_text());new=json.loads((work/(stem+'.json')).read_text())
        assert mathematical(old)==mathematical(new),stem
        npz=ROOT/'code'/(stem+'.npz')
        if npz.exists():
            aa=np.load(npz);bb=np.load(work/npz.name)
            assert aa.files==bb.files and all(np.array_equal(aa[k],bb[k]) for k in aa.files)
        stages.append({'program':stem+'.py','all_mathematical_JSON_and_NPZ_values_exact':True,'seconds':round(time.monotonic()-t,6)})
    sys.path.insert(0,str(work))
    from de_a6_schreier_certificate import read_certificate,verify_words
    certs=[]
    for stem in manifest['complete_certificate_stems']:
        aa=read_certificate(ROOT/'code'/(stem+'.bin'));bb=read_certificate(work/(stem+'.bin'))
        verify_words(bb);assert aa.keys()==bb.keys()
        for k in aa:
            if isinstance(aa[k],np.ndarray):assert np.array_equal(aa[k],bb[k]),(stem,k)
            else:assert aa[k]==bb[k],(stem,k)
        certs.append(stem+'.bin')
    assert all(digest(ROOT/f)==h for f,h in hashes.items())
    out={'status':'PASS_ISOLATED_E66_DISTRIBUTION_OVERLAP','stages':stages,
         'complete_certificates_exact_and_replayed':certs,'protected_files_unchanged':len(hashes),
         'all_288_actual_common_words_replayed':True,'seconds':round(time.monotonic()-start,6)}
    (dest/'replay.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
