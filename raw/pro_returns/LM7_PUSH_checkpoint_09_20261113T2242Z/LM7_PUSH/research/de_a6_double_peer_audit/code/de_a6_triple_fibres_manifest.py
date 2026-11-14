#!/usr/bin/env python3
"""Freeze the complete E60 source fibres and exact joint target package."""
from pathlib import Path
import ast,hashlib,json,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
EXT={'.py','.cpp','.hpp','.json','.npz','.out','.err','.input','.bin'}
EXCLUDE={'de_a6_triple_fibres_manifest.json','de_a6_triple_fibres_manifest.out',
         'de_a6_triple_fibres_manifest.err'}


def main():
    records={};queue=[];seen=set()
    def add(path,role):
        path=Path(path)
        if not path.is_file() or path.suffix not in EXT or path.name in EXCLUDE:return
        assert path.parent==HERE
        name=str(path.relative_to(ROOT))
        records.setdefault(name,{'roles':set()})['roles'].add(role)
        if path.suffix in {'.py','.json','.cpp','.hpp'} and path not in seen:queue.append(path)
    previous=json.loads((HERE/'de_a6_triple_source_manifest.json').read_text())
    for name,record in previous['records'].items():
        path=ROOT/name
        assert hashlib.sha256(path.read_bytes()).hexdigest()==record['sha256']
        add(path,'Unchanged separately root-replayed source/model dependency')
    add(HERE/'de_a6_triple_source_manifest.json','Prior frozen source manifest')
    prefixes=['de_a6_triple_signed','de_a6_triple_commutator',
              'de_a6_triple_query','de_a6_triple_deep_certificate',
              'de_a6_triple_target']
    for prefix in prefixes:
        for path in HERE.glob(prefix+'*'):
            role='Completed new E60 program, input, certificate, or independent replay'
            if 'failed' in path.name:role='Preserved unsuccessful attempt; excluded from successful claims'
            add(path,role)
    add(HERE/'de_a6_triple_fibres_manifest.py','This deterministic package collector')
    def named_dependencies(obj):
        if isinstance(obj,dict):
            for key,value in obj.items():
                if isinstance(value,str) and re.fullmatch('[0-9a-f]{64}',value):
                    add(HERE/Path(key).name,'Named hash dependency')
                else:named_dependencies(value)
        elif isinstance(obj,list):
            for value in obj:named_dependencies(value)
    while queue:
        path=queue.pop()
        if path in seen:continue
        seen.add(path)
        if path.suffix=='.json':
            try:named_dependencies(json.loads(path.read_text()))
            except json.JSONDecodeError:pass
            continue
        if path.suffix in {'.cpp','.hpp'}:
            for name in re.findall(r'#include\s+"([^"]+)"',path.read_text()):
                add(HERE/name,'Literal local C++ include')
            continue
        tree=ast.parse(path.read_text())
        for node in ast.walk(tree):
            modules=[]
            if isinstance(node,ast.Import):modules=[a.name.split('.')[0] for a in node.names]
            elif isinstance(node,ast.ImportFrom) and node.module:modules=[node.module.split('.')[0]]
            for module in modules:add(HERE/(module+'.py'),'Read-only local Python import; main not invoked')
            if isinstance(node,ast.Constant) and isinstance(node.value,str):
                value=node.value
                if '\n' in value or len(value)>180:continue
                name=Path(value).name
                if re.fullmatch(r'(?:de|bc|a|e)_[A-Za-z0-9_.-]+',name):
                    if (HERE/name).is_file():add(HERE/name,'Literal local data or support dependency')
                    elif '.' not in name:
                        for item in HERE.glob(name+'.*'):add(item,'Literal data-stem dependency')
    for name,record in records.items():
        data=(ROOT/name).read_bytes()
        record.update(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),
                      roles=sorted(record['roles']))
    documents={}
    for name in ['sections/E_a6_triple_agent.tex','research/DE_a6_triple_fibres.md',
                 'research/DE_a6_triple_fibres_replay.md',
                 'research/E60_before_completed_target.tex',
                 'research/DE_a6_triple_fibres_before_completed_target.md']:
        data=(ROOT/name).read_bytes()
        documents[name]={'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
    target=json.loads((HERE/'de_a6_triple_target_certificate.json').read_text())
    replay=json.loads((HERE/'de_a6_triple_target_complete_replay.json').read_text())
    assert target['status']=='PASS_COMPLETE_TRIPLE_SIGNED_TARGET_AND_MAXIMAL_SOLVABLE_MAP'
    assert replay['status']=='PASS_ALL_SIX_COMPLETE_TARGET_CHAIN_REPLAYS'
    assert target['all_actual_derived_indices']==[1,6,72,2304,20736,20736]
    out={'status':'FROZEN_COMPLETE_E60_CENTRAL_THREE_FIBRES_AND_TARGETS',
         'scope':'All79 source corrections; every retained E54 fibre and entire E57 boundary/congruence family; exact joint target maximal solvable map and generation',
         'replay_guide':'research/DE_a6_triple_fibres_replay.md',
         'prior_source_manifest':{'path':'code/de_a6_triple_source_manifest.json',
              'sha256':hashlib.sha256((HERE/'de_a6_triple_source_manifest.json').read_bytes()).hexdigest(),
              'all_members_unchanged':True},
         'whole_kernel_dimension':79,'new_C_preimage_abelianization_dimension':3,
         'stable_pairing_minor_determinant':4,
         'target_derived_indices':target['all_actual_derived_indices'],
         'specified_maximal_solvable_target_quotient_order':20736,
         'complete_new_target_relation_count':sum(r['complete_final_Schreier_relations'] for r in replay['rows']),
         'all_six_target_chains_freshly_recompiled_and_completely_replayed':True,
         'signed_full_relation_count_preserved':1159255,
         'signed_replay_shortcut':'All79 literal independent words plus the earlier root-replayed79-dimensional upper bound',
         'documents':documents,'records':dict(sorted(records.items())),
         'file_count':len(records),'total_bytes':sum(r['bytes'] for r in records.values()),
         'comparison':'Every mathematical JSON value and NPZ array exact; the replay guide types runtime/hash/discovery provenance and the exact final normality-gate count',
         'no_full_profinite_pentagon_existence_claim':True}
    (HERE/'de_a6_triple_fibres_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'records','documents'}},indent=2),flush=True)


if __name__=='__main__':main()
