#!/usr/bin/env python3
"""Freeze E63's entire binary/signed source and retained target package.

The concurrent E62 overlap work is explicitly excluded.  Prior source
hashes are checked; no imported legacy entry point is executed.
"""
from pathlib import Path
from hashlib import sha256
import ast,json,re

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
EXT={'.py','.cpp','.hpp','.json','.npz','.out','.err','.bin','.input','.txt'}
EXCLUDE={'de_a6_double_source_manifest.json','de_a6_double_source_manifest.out',
         'de_a6_double_source_manifest.err'}
PENDING=('e_a6_double_E62_','e_a6_double_binary_overlap_')


def main():
    records={};queue=[];seen=set()
    def add(path,role):
        path=Path(path)
        if not path.is_file() or path.suffix not in EXT or path.name in EXCLUDE:return
        if path.name.startswith(PENDING):return
        assert path.parent==HERE
        key=str(path.relative_to(ROOT))
        records.setdefault(key,{'roles':set()})['roles'].add(role)
        if path.suffix in {'.py','.cpp','.hpp','.json'} and path not in seen:queue.append(path)
    peer=json.loads((HERE/'de_a6_double_peer_audit.json').read_text())
    assert peer['all_originals_unchanged'] and peer['protected_original_count']==423
    for name,digest in peer['protected_sha256'].items():
        path=HERE/name
        assert sha256(path.read_bytes()).hexdigest()==digest,('prior protected dependency changed',name)
        add(path,'Prior binary-source or accepted old dependency; hash verified against independent peer replay')
    for prefix in ('de_a6_double_','a_cm_signed_common_','e_a6_double_target_',
                   'e_a6_double_triple_target_'):
        for path in HERE.glob(prefix+'*'):
            role='Completed E63 program, certificate, or literal replay'
            if any(t in path.name for t in ('failed','probe','initial')):
                role='Preserved preliminary attempt or partial bound; exact scope in replay guide'
            add(path,role)
    for name in ('de_a6_schreier_full_ordered.bin','de_a6_schreier_residual_derived.bin',
                 'de_a6_a5_common_source.bin','de_a6_gl_model.bin',
                 'de_a6_gl_central_model.bin','de_a6_double_source_manifest.py'):
        add(HERE/name,'Explicit replay command dependency')
    def hashed_dependencies(obj):
        if isinstance(obj,dict):
            for key,value in obj.items():
                if isinstance(value,str) and re.fullmatch('[0-9a-f]{64}',value):
                    add(HERE/Path(key).name,'Named hash dependency')
                else:hashed_dependencies(value)
        elif isinstance(obj,list):
            for value in obj:hashed_dependencies(value)
    while queue:
        p=queue.pop()
        if p in seen:continue
        seen.add(p)
        if p.suffix=='.json':
            try:hashed_dependencies(json.loads(p.read_text()))
            except json.JSONDecodeError:pass
            continue
        if p.suffix in {'.cpp','.hpp'}:
            for n in re.findall(r'#include\s+"([^"]+)"',p.read_text()):add(HERE/n,'Literal local C++ include')
            continue
        for node in ast.walk(ast.parse(p.read_text())):
            modules=[]
            if isinstance(node,ast.Import):modules=[a.name.split('.')[0] for a in node.names]
            elif isinstance(node,ast.ImportFrom) and node.module:modules=[node.module.split('.')[0]]
            for name in modules:add(HERE/(name+'.py'),'Read-only local import; legacy main not invoked')
            if isinstance(node,ast.Constant) and isinstance(node.value,str):
                value=node.value
                if '\n' in value or len(value)>180:continue
                name=Path(value).name
                if not re.fullmatch(r'(?:de|e|a|bc)_[A-Za-z0-9_.-]+',name):continue
                if (HERE/name).is_file():add(HERE/name,'Literal local data or support dependency')
                elif '.' not in name:
                    for item in HERE.glob(name+'.*'):add(item,'Literal stem dependency')
    for name,record in records.items():
        data=(ROOT/name).read_bytes()
        record.update(sha256=sha256(data).hexdigest(),bytes=len(data),roles=sorted(record['roles']))
    documents={}
    docnames=['sections/E_a6_double_agent.tex','sections/E_a6_double_target_root.tex',
              'sections/E_a6_double_triple_target_root.tex',
              'research/DE_a6_double_signed_bridge.md','research/DE_a6_double_source_replay.md',
              'research/DE_a6_double_signed_bridge_before_completed_source.md',
              'research/E63_initial_source_draft.tex','research/A_E63_full_proof_audit.md']
    docnames.extend(str(p.relative_to(ROOT)) for p in
                    (ROOT/'research/E63_candidate_incomplete_session').glob('*') if p.is_file())
    docnames.extend(str(p.relative_to(ROOT)) for p in
                    (ROOT/'research/E63_replay_before_explicit_input_hash_validation').glob('*') if p.is_file())
    for name in docnames:
        data=(ROOT/name).read_bytes();documents[name]={'sha256':sha256(data).hexdigest(),'bytes':len(data)}
    bridge=json.loads((HERE/'de_a6_double_bridge_replay.json').read_text())
    signed=json.loads((HERE/'de_a6_double_signed_replay.json').read_text())
    candidate=json.loads((HERE/'de_a6_double_candidate_replay.json').read_text())
    deep=json.loads((HERE/'de_a6_double_deep_words.json').read_text())
    assert bridge['relation_rank']==37 and bridge['whole_pullback_abelianization_dimension']==6
    assert signed['joint_kernel_dimension']==167 and signed['kernel_over_entire_old_signed_source_dimension']==125
    assert candidate['both_epimorphisms_and_maximality_proved'] and candidate['whole_common_quotient_order']==9331200000
    assert deep['all_six_actual_Q12_values_identity'] and deep['all15_complete_commutator_values_unchanged']
    out={'status':'FROZEN_COMPLETE_E63_BINARY_SIGNED_SOURCE_AND_NAMED_OLD_FIBRES',
         'replay_guide':'research/DE_a6_double_source_replay.md',
         'source_scope':'All125 correcting coordinates; every retained E54 finite point and full specified E57/E60 boundary, uniform and triple-cover system',
         'additional_E59_E62_source_overlap_included':False,
         'concurrent_root_paths_excluded':list(PENDING),
         'prior_peer_replay_originals_unchanged':423,
         'whole_X2_kernel_dimension':128,'whole_signed_joint_kernel_dimension':167,
         'old_J_identity_kernel_dimension':125,'perfect_common_kernel_dimension':122,
         'actual_common_quotient_order':9331200000,
         'complete_new_relator_counts':{'central':720615,'original_links':10,'signed_joint':1154659,
                                        'X2_candidate':865049,'GL_candidate':25965},
         'primary_citation':{'key':'DE_Steinberg1967','scope':'Section7 Theorem10 and Corollary2(b), actual universal SL2(F5) cover',
                             'root_opened_primary_and_verified':True},
         'documents':documents,'records':dict(sorted(records.items())),
         'file_count':len(records),'total_bytes':sum(r['bytes'] for r in records.values()),
         'no_full_profinite_pentagon_existence_claim':True}
    (HERE/'de_a6_double_source_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'records','documents'}},indent=2),flush=True)


if __name__=='__main__':main()
