"""One bounded audit of the scan022 textual source union and references."""
from pathlib import Path
import hashlib
import json
from scan022_source_support_prepare import BASE, OUT, read, digest, file_ref, json_object, write

ARTIFACTS = [
 'scan022_source_support_witness_catalog.json',
 'scan022_source_support_A_catalog.json',
 'scan022_source_support_B_catalog.json',
 'scan022_source_support_C_catalog.json',
 'scan022_source_support_fingerprints_ABC.json',
 'scan022_source_support_union.json',
]

def pointer(obj, ptr):
    for part in ptr.split('/')[1:] if ptr else []:
        part=part.replace('~1','/').replace('~0','~')
        obj=obj[int(part)] if isinstance(obj,list) else obj[part]
    return obj

def audit():
    failures=[]
    refs=set()
    source_spans=set()
    source_files={}
    parsed={}
    def visit(obj, context):
        if isinstance(obj,dict):
            p=obj.get('path')
            if isinstance(p,str) and p.startswith(('out/','packets/')) and ('sha256' in obj or 'json_pointer' in obj or 'body_sha256' in obj):
                if Path(p).suffix not in ['.json','.tex','.md','.txt','.py']:
                    failures.append({'scope':context,'reason':'Unexpected nontext reference','path':p})
                else:
                    try:
                        s=read(p)
                        sha=digest(s)
                        source_files[p]=sha
                        if 'sha256' in obj and obj['sha256']!=sha:
                            failures.append({'scope':context,'reason':'Whole-source hash mismatch','path':p})
                        if 'json_pointer' in obj:
                            if p not in parsed: parsed[p]=json.loads(s)
                            pointer(parsed[p],obj['json_pointer'])
                            refs.add((p,obj['json_pointer']))
                        if 'char_start' in obj and 'char_end' in obj:
                            a,b=obj['char_start'],obj['char_end']
                            assert 0<=a<=b<=len(s)
                            if 'body_sha256' in obj: assert digest(s[a:b])==obj['body_sha256']
                            if 'literal' in obj: assert s[a:b]==obj['literal']
                            source_spans.add((p,a,b))
                    except Exception as exc:
                        failures.append({'scope':context,'reason':type(exc).__name__+': '+str(exc),'path':p})
            for k,v in obj.items(): visit(v,context+'/'+str(k))
        elif isinstance(obj,list):
            for i,v in enumerate(obj): visit(v,context+'/'+str(i))
    artifacts={name:file_ref('out/checks/'+name) for name in ARTIFACTS}
    for name in ARTIFACTS:
        visit(json_object('out/checks/'+name),name)
    fingerprints=json_object('out/checks/scan022_source_support_fingerprints_ABC.json')
    manifest_checks=[]
    absent=[]
    for role,manifest_name in [('A','final_immutable.json'),('B','manifest.json'),('C','return_manifest.json')]:
        m=json_object(f'out/readers/022/{role}/{manifest_name}')
        # Entries are filtered by the explicit text fingerprint registry before
        # using declared hashes. Image entries remain outside this audit.
        byname={Path(entry['path']).name:entry for entry in m['files']}
        for key,entry in fingerprints['files'].items():
            if not key.startswith(role+'.'): continue
            name=Path(entry['path']).name
            if name in byname:
                okay=entry['sha256']==byname[name]['sha256']
                manifest_checks.append({'reader':role,'text_file':name,'matches_declared_manifest_hash':okay})
                if not okay: failures.append({'scope':'manifest text binding','reader':role,'path':entry['path']})
            else:
                absent.append({'reader':role,'text_file':name,'scope':'Fingerprint retained; this named text file has no entry in the return manifest.'})
    union=json_object('out/checks/scan022_source_support_union.json')
    coverage={}
    for role in 'ABC':
        report=json_object(f'out/readers/022/{role}/report.json')
        scope=union['reader_source_scopes'][role]
        assert [x['original_id'] for x in scope['every_difference_row']]==[x['id'] for x in report['differences']]
        assert [x['original_id'] for x in scope['every_doubt_row']]==[x['id'] for x in report['doubts']]
        assert [x['original_identity'] for x in scope['every_inventory_row_in_original_order']]==[x['element'] for x in report['inventory']]
        associations=union['graphical_source_associations'][role]
        assert all(x['aligned_union_ids'] for x in associations['all_groups'])
        assert all(x['aligned_union_ids'] for x in associations['inventory_to_source_in_original_order'])
        coverage[role]={'difference_records':len(report['differences']),'doubt_records':len(report['doubts']),
                        'inventory_records':len(report['inventory']),
                        'candidate_groups':len(associations['all_groups']),
                        'all_original_difference_ids_retained':True,
                        'all_original_doubt_ids_retained':True,
                        'all_original_inventory_ids_and_order_retained':True,
                        'all_graphical_groups_associated':True}
    assert [row['source_parts'][0]['part_id'] for row in union['original_C_source_rows']]==[f'C022-R{i:02d}-1' for i in range(1,8)]
    return {'scan':22,'scope':'One targeted textual source coverage and reference audit before root ink decisions.',
            'main_adjudicated':False,'main_approved':False,
            'artifacts':artifacts,'source_entry_coverage':coverage,
            'canonical_C_source_rows':7,'canonical_C_source_parts':7,
            'source_crosswalk_scopes':len(union['textual_locus_crosswalk']),
            'distinct_checked_json_references':len(refs),'distinct_checked_text_spans':len(source_spans),
            'manifest_text_checks':manifest_checks,'text_files_not_listed_in_manifest':absent,
            'reference_failures':failures,'passed':not failures,
            'separate_candidate_bank_audit':file_ref('out/checks/scan022_candidate_review.json'),
            'limits':'No image/hash access, crop, OCR, compilation, rendering, research, installation, mathematical proof or coordinate calculation. Existing reader values and declarations were copied with their source scopes. No root ink outcome or physical count was chosen.',
            'known_preserved_source_note':'C022-S08 stale G04 owner comment is preserved with the G06 references in the candidate bank. Root selected-source handling remains pending.',
            'awaiting':'Root journal for record drafting.'}

if __name__=='__main__':
    result=audit()
    ref=write('scan022_source_support_audit.json',result)
    print(json.dumps({'audit':ref,'passed':result['passed'],'reference_failures':result['reference_failures'],
                      'coverage':result['source_entry_coverage'],
                      'manifest_unlisted_text':result['text_files_not_listed_in_manifest']},ensure_ascii=False))
