#!/usr/bin/env python3
"""Freeze the completed 3.A6 source gate, excluding continuing fibres."""
from pathlib import Path
import ast,hashlib,json,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
EXT={'.py','.cpp','.hpp','.json','.npz','.out','.err','.input','.bin'}
EXCLUDE={'de_a6_triple_source_manifest.json','de_a6_triple_source_manifest.out',
         'de_a6_triple_source_manifest.err'}


def main():
    records={};queue=[];seen=set()
    def add(path,role):
        path=Path(path)
        if not path.is_file() or path.suffix not in EXT or path.name in EXCLUDE:return
        assert path.parent==HERE
        name=str(path.relative_to(ROOT))
        records.setdefault(name,{'roles':set()})['roles'].add(role)
        if path.suffix in {'.py','.json'} and path not in seen:queue.append(path)
    stems=['de_a6_triple_affine','de_a6_triple_base','de_a6_triple_modular',
           'de_a6_triple_kernel','de_a6_triple_central','de_a6_triple_source_certificate']
    for stem in stems:
        for p in HERE.glob(stem+'*'):add(p,'Completed new source program, input, result, or preserved incomplete log')
    for name in ['de_a6_triple_core.hpp','de_a6_triple_source_manifest.py',
                 'de_a6_schreier.cpp','de_a6_schreier_certificate.py']:
        add(HERE/name,'Complete collector, engine, or independent word support')
    models=json.loads((HERE/'de_a6_triple_models_manifest.json').read_text())
    for name,r in models['records'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==r['sha256']
        add(HERE/name,'Unchanged separately root-replayed cover and target model')
    add(HERE/'de_a6_triple_models_manifest.json','Prior frozen model manifest')
    def dependencies(obj):
        if isinstance(obj,dict):
            for k,v in obj.items():
                if isinstance(v,str) and re.fullmatch('[0-9a-f]{64}',v):add(HERE/Path(k).name,'Named hash dependency')
                else:dependencies(v)
        elif isinstance(obj,list):
            for v in obj:dependencies(v)
    while queue:
        path=queue.pop()
        if path in seen:continue
        seen.add(path)
        if path.suffix=='.json':
            try:dependencies(json.loads(path.read_text()))
            except json.JSONDecodeError:pass
            continue
        tree=ast.parse(path.read_text())
        for node in ast.walk(tree):
            modules=[]
            if isinstance(node,ast.Import):modules=[a.name.split('.')[0] for a in node.names]
            elif isinstance(node,ast.ImportFrom) and node.module:modules=[node.module.split('.')[0]]
            for module in modules:add(HERE/(module+'.py'),'Read-only transitive Python import; main not invoked')
            if isinstance(node,ast.Constant) and isinstance(node.value,str):
                value=node.value
                if '\n' in value or len(value)>180:continue
                name=Path(value).name
                if re.fullmatch(r'(?:de|bc|a|e)_[A-Za-z0-9_.-]+',name):
                    if (HERE/name).is_file():add(HERE/name,'Literal data or support dependency')
                    elif '.' not in name:
                        for p in HERE.glob(name+'.*'):add(p,'Literal data-stem dependency')
    assert not any('de_a6_triple_signed' in name for name in records)
    for name,r in records.items():
        data=(ROOT/name).read_bytes()
        r.update(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),roles=sorted(r['roles']))
    documents={}
    for name in ['research/DE_a6_triple_source.md','research/DE_a6_triple_source_replay.md']:
        data=(ROOT/name).read_bytes();documents[name]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    out={'status':'FROZEN_EXACT_TRIPLE_SOURCE_AND_PERFECT_RESIDUAL',
         'scope':'Actual A6/affine=joint Q12 base, full ternary kernel79, C-preimage abelianization3 and perfect derived kernel76; no whole CM/pentagon fibre result yet',
         'replay_guide':'research/DE_a6_triple_source_replay.md',
         'complete_new_relation_counts':{'base':873463,'central':720615,'central_original_links':10},
         'excluded_continuing_prefix':'de_a6_triple_signed',
         'documents':documents,'records':dict(sorted(records.items())),
         'file_count':len(records),'total_bytes':sum(r['bytes'] for r in records.values()),
         'comparison':'Exact mathematical JSON and every array; ignore elapsed time and dependent regenerated provenance hashes only',
         'prior_model_hashes_all_unchanged':True}
    (HERE/'de_a6_triple_source_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('records','documents')},indent=2),flush=True)


if __name__=='__main__':main()
