#!/usr/bin/env python3
"""Isolated peer replay of the completed small binary-cover stages.

All root sources and saved outputs remain read-only.  The isolated copy
regenerates the seven Python certificates and compares every mathematical
JSON value, every NPZ entry, and the generated C++/binary model files.
"""
from pathlib import Path
from hashlib import sha256
import ast,json,re,shutil,subprocess,time
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
DEST=ROOT/'research/de_a6_double_peer_audit'


def mathematical(v):
    if isinstance(v,dict):
        return {k:mathematical(w) for k,w in v.items() if k not in {'seconds','input_sha256'}}
    if isinstance(v,list):return [mathematical(w) for w in v]
    return v


def main():
    started=time.time();assert not DEST.exists();(DEST/'code').mkdir(parents=True)
    programs=['e_a6_double_kernel_replay_root.py','e_a6_double_central_prepare_root.py',
              'e_a6_double_central_replay_root.py','e_a6_double_commutator_prepare_root.py',
              'e_a6_double_query_build_root.py','e_a6_double_commutator_replay_root.py',
              'e_a6_double_modular_basis_root.py']
    files={Path(k).name for k in json.loads((HERE/'de_a6_triple_fibres_manifest.json').read_text())['records']}
    files.update(p.name for p in HERE.glob('e_a6_double_*') if p.is_file() and
                 p.suffix in {'.py','.cpp','.hpp','.json','.npz','.bin','.out','.err','.input'})
    queue=list(files);seen=set()
    def add(name):
        p=HERE/Path(name).name
        if p.is_file() and p.name not in files:files.add(p.name);queue.append(p.name)
    while queue:
        name=queue.pop()
        if name in seen:continue
        seen.add(name);p=HERE/name
        if p.suffix=='.py':
            for node in ast.walk(ast.parse(p.read_text())):
                if isinstance(node,ast.Import):
                    for n in node.names:add(n.name.split('.')[0]+'.py')
                elif isinstance(node,ast.ImportFrom) and node.module:add(node.module.split('.')[0]+'.py')
                elif isinstance(node,ast.Constant) and isinstance(node.value,str):
                    v=node.value
                    if '\n' not in v and len(v)<180 and re.fullmatch(r'(?:de|e|a|bc)_[A-Za-z0-9_.-]+',Path(v).name):add(v)
        elif p.suffix in {'.cpp','.hpp'}:
            for n in re.findall(r'#include\s+"([^"]+)"',p.read_text()):add(n)
    protected={name:sha256((HERE/name).read_bytes()).hexdigest() for name in sorted(files)}
    for name in files:shutil.copyfile(HERE/name,DEST/'code'/name)
    rows=[]
    for program in programs:
        stem=Path(program).stem;begin=time.time()
        with (DEST/(stem+'.out')).open('w') as out,(DEST/(stem+'.err')).open('w') as err:
            subprocess.run(['python',program],cwd=DEST/'code',stdout=out,stderr=err,check=True)
        checked=[]
        for extension in ('.json','.npz'):
            p=DEST/'code'/(stem+extension);old=HERE/p.name
            assert p.exists() or extension=='.npz'
            if not p.exists():continue
            if extension=='.json':assert mathematical(json.loads(p.read_text()))==mathematical(json.loads(old.read_text())),p.name
            else:
                a,b=np.load(p),np.load(old);assert set(a.files)==set(b.files)
                for key in a.files:
                    assert a[key].shape==b[key].shape and a[key].dtype==b[key].dtype
                    assert np.array_equal(a[key],b[key]),(p.name,key)
            checked.append(p.name)
        row={'program':program,'status':'PASS','exact_outputs':checked,'seconds':round(time.time()-begin,3)}
        rows.append(row);print(json.dumps(row),flush=True)
    byte_names=['e_a6_double_central_root.cpp','e_a6_double_core_root.hpp',
                'e_a6_double_central_model_root.bin','e_a6_double_query_core_root.hpp',
                'e_a6_double_query_root.cpp','e_a6_double_commutator_queries_root.bin']
    for name in byte_names:assert (DEST/'code'/name).read_bytes()==(HERE/name).read_bytes(),name
    assert all(sha256((HERE/name).read_bytes()).hexdigest()==h for name,h in protected.items())
    result={'status':'PASS_ISOLATED_BINARY_SOURCE_CENTRAL_AND_CORRECTION_PEER_REPLAY',
            'programs':rows,'byte_identical_generated_models_and_sources':byte_names,
            'protected_original_count':len(protected),'all_originals_unchanged':True,
            'protected_sha256':protected,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_double_peer_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='protected_sha256'},indent=2),flush=True)


if __name__=='__main__':main()
