#!/usr/bin/env python3
"""One independent, source-only replay of scan025 stage1 and coverage inventory.

This QA helper writes only scan025_qa* artifacts. It never opens image files or
reader programs and never changes reader, source, authority, or draft files.
"""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json
import re

BASE=Path(__file__).resolve().parents[2]
OUT=BASE/'out/checks'
POOL=OUT/'scan025_source_pool_v01.json'
MANIFEST=OUT/'scan025_source_projection_manifest_v01.json'
INVENTORY=OUT/'scan025_qa_sourcecoverage_inventory.json'


def sha(value):
    return hashlib.sha256(value if isinstance(value,bytes) else value.encode('utf-8')).hexdigest()


def ptr(value,pointer):
    for item in pointer[1:].split('/') if pointer else []:
        key=item.replace('~1','/').replace('~0','~')
        value=value[int(key)] if isinstance(value,list) else value[key]
    return value


def encoded_strings(value):
    if isinstance(value,dict):
        if list(value)==['$s']:
            yield value['$s']
        else:
            for item in value.values():
                yield from encoded_strings(item)
    elif isinstance(value,list):
        for item in value:
            yield from encoded_strings(item)


def allowed_original(path):
    p=Path(path)
    reader=any(path.startswith(f'out/readers/025/{r}/') for r in 'ABC') and p.suffix in ['.tex','.md','.json','.txt']
    packet=path.startswith('packets/025/') and p.suffix in ['.tex','.md','.json','.txt']
    named=path in ['out/briefs/source_record_brief_v07.md']+[f'out/checks/scan025_{s}.json' for s in ['C_doubt_catalog','H_marker_catalog','S_scope','reader_fingerprints','pairwise_diff_manifest']]
    return reader or packet or named


def main():
    failures=[]
    check_counts=Counter()
    def check(kind,condition,**context):
        check_counts[kind]+=1
        if not condition:
            failures.append({'check':kind,**context})
        return condition

    pool_raw=POOL.read_bytes()
    manifest_raw=MANIFEST.read_bytes()
    inventory_raw=INVENTORY.read_bytes()
    pool=json.loads(pool_raw)
    manifest=json.loads(manifest_raw)
    inv=json.loads(inventory_raw)
    check('pool-manifest-hash',sha(pool_raw)==manifest['pool']['sha256_utf8'])
    check('pool-unapproved',pool['main_adjudicated'] is False and pool['main_approved'] is False)
    files={r['id']:r for r in pool['files']}
    by_path={r['path']:r for r in pool['files']}
    strings={r['id']:r for r in pool['strings']}
    spans={r['id']:r for r in pool['spans']}
    for name,entries,mapping in [('file',pool['files'],files),('string',pool['strings'],strings),('span',pool['spans'],spans)]:
        check('unique-'+name+'-ids',len(entries)==len(mapping))
    file_cache={}
    string_cache={}
    resolving=set()

    def resolve_string(sid):
        if sid in string_cache:
            return string_cache[sid]
        key=('string',sid)
        if key in resolving:
            raise ValueError('cyclic pooled string '+sid)
        resolving.add(key)
        entry=strings[sid]
        literal=entry['literal']
        if isinstance(literal,str):
            result=literal
        else:
            source=spans[literal['span_ref']]
            result=resolve_file(source['source_file'])[source['char_start']:source['char_end_exclusive']]
        check('pooled-string-hash',sha(result)==entry['sha256_utf8'],id=sid)
        check('pooled-string-length',len(result)==entry['characters'] and len(result.encode('utf-8'))==entry['utf8_bytes'],id=sid)
        string_cache[sid]=result
        resolving.remove(key)
        return result

    def decode(value):
        if isinstance(value,dict):
            if list(value)==['$s']:
                return resolve_string(value['$s'])
            return {k:decode(v) for k,v in value.items()}
        if isinstance(value,list):
            return [decode(v) for v in value]
        return value

    def serialize(tree,record):
        options=record['serialization']
        return json.dumps(decode(tree),ensure_ascii=options['ensure_ascii'],indent=options['indent'])+options['ending']

    def resolve_file(fid):
        if fid in file_cache:
            return file_cache[fid]
        key=('file',fid)
        if key in resolving:
            raise ValueError('cyclic pooled file '+fid)
        resolving.add(key)
        record=files[fid]
        if record['kind']=='text':
            result=''.join(resolve_string(piece['string_ref']) for piece in record['payload']['text_chunks'])
        else:
            result=serialize(record['payload'],record)
        file_cache[fid]=result
        check('pooled-file-hash',sha(result)==record['sha256_utf8'],id=fid,path=record['path'])
        check('pooled-file-length',len(result)==record['characters'] and len(result.encode('utf-8'))==record['utf8_bytes'],id=fid)
        resolving.remove(key)
        return result

    original_comparisons=[]
    restricted_origin_bindings=[]
    for fid,record in files.items():
        restored=resolve_file(fid)
        if allowed_original(record['path']):
            raw=(BASE/record['path']).read_bytes()
            equal=restored.encode('utf-8')==raw
            check('exact-source-file-bytes',equal,id=fid,path=record['path'])
            original_comparisons.append({'path':record['path'],'sha256_utf8':sha(raw),'exact':equal})
        else:
            # This role is authorized to read the supplied S_scope catalog,
            # and does not open the original external S TSV.
            s=json.loads((BASE/'out/checks/scan025_S_scope.json').read_text())
            bound=record['path']==s['source'] and sha(restored)==s['source_sha256']
            check('restricted-origin-catalog-digest',bound,id=fid,path=record['path'])
            restricted_origin_bindings.append({'path':record['path'],'method':'pooled reconstruction digest equals the authorized S_scope source_sha256; original external file not opened','exact_digest_binding':bound})
    for sid in strings:
        resolve_string(sid)
    frozen=json.loads((BASE/'out/checks/scan025_reader_fingerprints.json').read_text())['files']
    frozen_count=0
    for path,expected_hash in frozen.items():
        if path in by_path:
            frozen_count+=1
            check('frozen-reader-original-hash',sha(resolve_file(by_path[path]['id']))==expected_hash,path=path)

    for sid,entry in spans.items():
        text=resolve_file(entry['source_file'])
        a,b=entry['char_start'],entry['char_end_exclusive']
        check('span-character-boundaries',0<=a<=b<=len(text),id=sid)
        check('span-file-binding',entry['source_path']==files[entry['source_file']]['path'] and entry['source_sha256_utf8']==sha(text),id=sid)
        check('span-byte-boundaries',len(text[:a].encode('utf-8'))==entry['utf8_byte_start'] and len(text[:b].encode('utf-8'))==entry['utf8_byte_end_exclusive'],id=sid)
        check('span-line-boundaries',text.count('\n',0,a)+1==entry['line_start_1based'] and text.count('\n',0,max(a,b-1))+1==entry['line_end_1based'],id=sid)
        check('span-literal-hash',sha(text[a:b])==entry['literal_sha256_utf8'],id=sid)
        check('span-reconstruction-pointer',entry['literal']=={'file_slice':entry['source_file'],'char_start':a,'char_end_exclusive':b},id=sid)

    helper_path=OUT/'scan025_qa_source_inventory.py'
    spec=importlib.util.spec_from_file_location('scan025_qa_source_inventory',helper_path)
    helper=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    pointer_count=0
    for fid,record in files.items():
        if record['kind']!='json':
            continue
        text=resolve_file(fid)
        tree=json.loads(text)
        literal_index=helper.json_spans(text)
        declared=pool['json_pointer_spans'][fid]
        check('complete-json-pointer-index',set(literal_index)==set(declared),id=fid,missing=sorted(set(literal_index)-set(declared)),extra=sorted(set(declared)-set(literal_index)))
        for pointer,(a,b) in literal_index.items():
            pointer_count+=1
            if pointer not in declared:
                continue
            span=spans[declared[pointer]]
            check('exact-json-pointer-boundaries',span['source_file']==fid and (a,b)==(span['char_start'],span['char_end_exclusive']),id=fid,pointer=pointer)
            check('exact-json-pointer-value',json.loads(text[a:b])==ptr(tree,pointer),id=fid,pointer=pointer)

    pages=[]
    review_rows=[]
    for page in manifest['review_pages']:
        raw=(BASE/page['path']).read_bytes()
        check('projection-page-hash',sha(raw)==page['sha256_utf8'],path=page['path'])
        rows=[json.loads(line) for line in raw.decode('utf-8').splitlines()]
        check('projection-page-row-bounds',rows[0]['projection_row']==page['projection_row_start'] and rows[-1]['projection_row']==page['projection_row_end'],path=page['path'])
        pages.append({'path':page['path'],'sha256_utf8':sha(raw),'rows':len(rows)})
        review_rows.extend(rows)
    check('projection-row-sequence',[r['projection_row'] for r in review_rows]==list(range(1,len(review_rows)+1)))
    check('projection-row-count',len(review_rows)==manifest['review_rows'])
    trees={}
    seen_strings=set()
    seen_targets=set()

    def assign(tree,pointer,value):
        if not pointer:
            return value
        parts=[p.replace('~1','/').replace('~0','~') for p in pointer[1:].split('/')]
        target=tree
        for key in parts[:-1]:
            target=target[int(key)] if isinstance(target,list) else target[key]
        key=int(parts[-1]) if isinstance(target,list) else parts[-1]
        target[key]=value
        return tree

    for row in review_rows:
        fid=row['file']
        check('projection-source-identity',row['source_path']==files[fid]['path'],row=row['projection_row'])
        pointer=row.get('pointer','')
        target=(fid,pointer)
        check('projection-unique-target',target not in seen_targets,row=row['projection_row'],file=fid,pointer=pointer)
        seen_targets.add(target)
        if row['kind']=='document':
            val={k:None for k in row['ordered_children']} if row['root_type']=='dict' else [None]*len(row['ordered_children'])
            trees[fid]=val
            check('projection-document-hash',row['source_sha256_utf8']==files[fid]['sha256_utf8'],file=fid)
        else:
            check('projection-pointer-ref',pool['json_pointer_spans'][fid][pointer]==row['span_ref'],row=row['projection_row'])
            if row['kind']=='container':
                val={k:None for k in row['ordered_children']} if row['container_type']=='dict' else [None]*len(row['ordered_children'])
            else:
                val=row['value']
                new_ids=[]
                for entry in row['new_strings']:
                    sid=entry['id']
                    new_ids.append(sid)
                    check('projection-first-use-string-identity',sid not in seen_strings and all(entry.get(k)==v for k,v in strings[sid].items()),row=row['projection_row'],string=sid)
                    if isinstance(entry['literal'],dict):
                        check('projection-first-use-string-exact-span',entry.get('exact_source_span')==spans[entry['literal']['span_ref']],row=row['projection_row'],string=sid)
                referenced=set(encoded_strings(val))
                check('projection-first-use-string-completeness',set(new_ids)==referenced-seen_strings,row=row['projection_row'],missing=sorted(referenced-seen_strings-set(new_ids)),extra=sorted(set(new_ids)-(referenced-seen_strings)))
                seen_strings.update(new_ids)
            trees[fid]=assign(trees[fid],pointer,val)
    expected_json={fid for fid,r in files.items() if r['kind']=='json'}
    check('projection-all-json-documents',set(trees)==expected_json)
    for fid,tree in trees.items():
        check('projection-exact-document-bytes',serialize(tree,files[fid])==resolve_file(fid),file=fid,path=files[fid]['path'])

    # Independently prepared source rows bind to the original pool pointers.
    row_coverage=[]
    for row in inv['original_row_inventory']:
        ref=row['source_ref']
        fid=by_path[ref['path']]['id']
        encoded=ptr(files[fid]['payload'],ref['json_pointer'])
        val=decode(encoded)
        check('original-row-value',helper.json_value_digest(val)==row['decoded_value_sha256'],path=ref['path'],pointer=ref['json_pointer'])
        sid=pool['json_pointer_spans'][fid][ref['json_pointer']]
        span=spans[sid]
        exact=(span['char_start'],span['char_end_exclusive'],span['utf8_byte_start'],span['utf8_byte_end_exclusive'],span['literal_sha256_utf8'])==(ref['char_start'],ref['char_end_exclusive'],ref['utf8_byte_start'],ref['utf8_byte_end_exclusive'],ref['literal_sha256_utf8'])
        check('original-row-exact-reference',exact,path=ref['path'],pointer=ref['json_pointer'])
        row_coverage.append({'path':ref['path'],'pointer':ref['json_pointer'],'identity':row['identity'],'pool_span_ref':sid,'covered':exact})
    for meta in inv['qualification_and_hand_metadata']:
        ref=meta['source_ref']
        fid=by_path[ref['path']]['id']
        value=decode(ptr(files[fid]['payload'],ref['json_pointer']))
        check('original-qualification-hand-scope-value',value==meta['value'],path=ref['path'],pointer=ref['json_pointer'])
    for item in inv['literal_drawing_command_inventory']:
        ref=item['source_ref']
        text=resolve_file(by_path[ref['path']]['id'])
        a,b=ref['char_start'],ref['char_end_exclusive']
        check('literal-drawing-command-exact',sha(text[a:b])==ref['literal_sha256_utf8'],path=ref['path'],ordinal=item['ordinal0'])
    for reader in 'ABC':
        source_path=f'out/readers/025/{reader}/reading.tex'
        text=resolve_file(by_path[source_path]['id'])
        visible=[]
        for line in text.splitlines(keepends=True):
            comment=len(line)
            for i,char in enumerate(line):
                if char!='%':
                    continue
                backslashes=0
                k=i-1
                while k>=0 and line[k]=='\\':
                    backslashes+=1
                    k-=1
                if backslashes%2==0:
                    comment=i
                    break
            visible.append(line[:comment]+''.join('\n' if c=='\n' else ' ' for c in line[comment:]))
        all_command_starts={m.start() for m in re.finditer(r'\\(?:draw|filldraw|fill|path|node|coordinate|useasboundingbox)\b',''.join(visible))}
        inventoried_starts={entry['source_ref']['char_start'] for entry in inv['literal_drawing_command_inventory'] if entry['reader']==reader}
        check('all-literal-drawing-command-starts-covered',all_command_starts==inventoried_starts,reader=reader,missing=sorted(all_command_starts-inventoried_starts),extra=sorted(inventoried_starts-all_command_starts))

    # Source025's union/locus handoff is required before this script is run.
    union_result=check_union(check,pool,files,strings,spans,resolve_file,decode,inv,row_coverage)

    result={
        'scan':25,'source_only':True,'status':'passed' if not failures else 'concrete defects recorded',
        'scope':'One bounded independent source-reference, complete projection and original-row coverage replay. No image read, source mutation, ink choice, selected reading, physical count, mathematical inference, compilation, rendering or metric assertion.',
        'inputs':{'pool_sha256_utf8':sha(pool_raw),'projection_manifest_sha256_utf8':sha(manifest_raw),'independent_original_inventory_sha256_utf8':sha(inventory_raw),'qa_script_sha256_utf8':sha(Path(__file__).read_bytes()),'qa_inventory_helper_sha256_utf8':sha(helper_path.read_bytes())},
        'counts':{'pooled_files_reconstructed':len(files),'original_files_byte_compared':len(original_comparisons),'restricted_origin_digest_bindings':len(restricted_origin_bindings),'frozen_reader_hashes_compared':frozen_count,'strings':len(strings),'spans':len(spans),'json_pointer_spans':pointer_count,'projection_pages':len(pages),'projection_rows':len(review_rows),'json_documents_reconstructed_from_projections':len(trees),'original_rows_covered':len(row_coverage),'original_qualification_hand_scope_fields':len(inv['qualification_and_hand_metadata']),'literal_drawing_commands':len(inv['literal_drawing_command_inventory'])},
        'check_counts':dict(check_counts),'original_source_comparisons':original_comparisons,'restricted_origin_bindings':restricted_origin_bindings,
        'original_row_coverage':row_coverage,'union_replay':union_result,'concrete_defects':failures,
        'root_review_status':'Root performs its own complete source review and later selection review; no approval asserted.'
    }
    output=OUT/'scan025_qa_stage1_replay.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    summary={'path':str(output.relative_to(BASE)),'sha256_utf8':sha(output.read_bytes()),'status':result['status'],'counts':result['counts'],'failed_checks':len(failures),'concrete_defects':failures}
    (OUT/'scan025_qa_stage1_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


def check_union(check,pool,files,strings,spans,resolve_file,decode,inv,row_coverage):
    union_path=OUT/'scan025_source_union_v01.json'
    skeleton_path=OUT/'scan025_source_row_skeleton_v01.json'
    union_raw=union_path.read_bytes()
    skeleton_raw=skeleton_path.read_bytes()
    union=json.loads(union_raw)
    skeleton=json.loads(skeleton_raw)
    check('union-frozen-handoff-hash',sha(union_raw)=='d1625b378dc0ec91fd568b2ad6f65b8dfed5f84e8322aa3855e825df01143cb1')
    check('skeleton-frozen-handoff-hash',sha(skeleton_raw)=='9d1d92ab63a8950929a7a6147e4593d5d5d3820738918422e5bcf1f42f1b1c77')
    check('union-pool-binding',union['shared_pool']['sha256_utf8']==sha(POOL.read_bytes()))
    check('skeleton-union-binding',skeleton['source_union']['sha256_utf8']==sha(union_raw))
    check('union-unapproved',union['main_adjudicated'] is False and union['main_approved'] is False and union['selected_counts'] is None and union['selected_confidences'] is None and union['root_crop_journal'] is None)
    check('skeleton-unapproved',skeleton['main_adjudicated'] is False and skeleton['main_approved'] is False)
    by_path={entry['path']:entry for entry in files.values()}
    json_reference_keys=set()
    text_reference_keys=set()
    text_ref_count=0
    json_ref_count=0

    def visit(value,pointer=''):
        yield pointer,value
        if isinstance(value,dict):
            for k,v in value.items():
                yield from visit(v,pointer+'/'+str(k).replace('~','~0').replace('/','~1'))
        elif isinstance(value,list):
            for i,v in enumerate(value):
                yield from visit(v,pointer+'/'+str(i))

    def text_of(ref):
        return resolve_file(ref['source_file'])[ref['char_start']:ref['char_end_exclusive']]

    def json_value(ref):
        return decode(ptr(files[ref['file']]['payload'],ref['json_pointer']))

    for document_name,document in [('union',union),('skeleton',skeleton)]:
        for pointer,value in visit(document):
            if not isinstance(value,dict):
                continue
            if {'source_file','source_path','char_start','char_end_exclusive','literal_sha256_utf8'}<=set(value):
                text_ref_count+=1
                fid=value['source_file']
                text=resolve_file(fid)
                a,b=value['char_start'],value['char_end_exclusive']
                text_reference_keys.add((value['source_path'],a,b))
                check('union-text-ref-identity',value['source_path']==files[fid]['path'] and value['source_sha256_utf8']==files[fid]['sha256_utf8'],document=document_name,pointer=pointer)
                check('union-text-ref-boundaries',0<=a<=b<=len(text) and len(text[:a].encode('utf-8'))==value['utf8_byte_start'] and len(text[:b].encode('utf-8'))==value['utf8_byte_end_exclusive'],document=document_name,pointer=pointer)
                check('union-text-ref-lines',text.count('\n',0,a)+1==value['line_start_1based'] and text.count('\n',0,max(a,b-1))+1==value['line_end_1based'],document=document_name,pointer=pointer)
                check('union-text-ref-literal',sha(text[a:b])==value['literal_sha256_utf8'] and value['literal']=={'file_slice':fid,'char_start':a,'char_end_exclusive':b},document=document_name,pointer=pointer)
                existing=value.get('existing_pool_span')
                if existing:
                    original=spans[existing]
                    check('union-text-ref-pool-alias',(original['source_file'],original['char_start'],original['char_end_exclusive'])==(fid,a,b),document=document_name,pointer=pointer)
            if {'file','source_path','source_sha256_utf8','json_pointer','span_ref','value'}<=set(value):
                json_ref_count+=1
                fid=value['file']
                p=value['json_pointer']
                json_reference_keys.add((value['source_path'],p))
                check('union-json-ref-identity',value['source_path']==files[fid]['path'] and value['source_sha256_utf8']==files[fid]['sha256_utf8'],document=document_name,pointer=pointer)
                check('union-json-ref-pointer',pool['json_pointer_spans'][fid][p]==value['span_ref'] and value['value']=={'json_value':fid,'pointer':p},document=document_name,pointer=pointer)

    original_groups={entry['id']:entry for entry in inv['group_span_inventory']}
    groups=union['complete_own_groups']
    check('union-all-own-group-identities',set(groups)==set(original_groups))
    group_intervals={}
    for gid,entry in groups.items():
        expected=original_groups[gid]
        original=json_value(entry['raw_group'])
        ref=entry['complete_source']
        check('union-own-group-original-pointer',entry['raw_group']['source_path']==expected['map_row_ref']['path'] and entry['raw_group']['json_pointer']==expected['map_row_ref']['json_pointer'],group=gid)
        check('union-own-group-complete-literal',original['id']==gid and text_of(ref)==original['literal_source'] and ref['char_start']==expected['tex_ref']['char_start'] and ref['char_end_exclusive']==expected['tex_ref']['char_end_exclusive'],group=gid)
        check('union-own-group-reader',entry['reader']==expected['reader'],group=gid)
        check('union-own-group-unselected',entry['selected'] is None and entry['main_approved'] is False,group=gid)
        group_intervals[gid]=(entry['reader'],ref['char_start'],ref['char_end_exclusive'])
        for field,index in [('candidate_and_scope_fields',entry['candidate_and_scope_fields']),('original_component_fields',entry['original_component_fields'])]:
            for key,field_ref in index.items():
                check('union-own-group-field-role',field_ref['source_path']==entry['raw_group']['source_path'] and field_ref['json_pointer']==entry['raw_group']['json_pointer']+'/'+key.replace('~','~0').replace('/','~1') and json_value(field_ref)==original[key],group=gid,field=key)

    commands=union['literal_command_inventory']
    own_commands=inv['literal_drawing_command_inventory']
    expected_commands={(x['source_ref']['path'],x['source_ref']['char_start']):x for x in own_commands}
    actual_commands={(x['source']['source_path'],x['source']['char_start']):x for x in commands}
    check('union-all-command-identities',len(actual_commands)==len(commands) and set(actual_commands)==set(expected_commands),missing=sorted(set(expected_commands)-set(actual_commands)),extra=sorted(set(actual_commands)-set(expected_commands)))
    command_by_id={x['id']:x for x in commands}
    for key,entry in actual_commands.items():
        if key not in expected_commands:
            continue
        original=expected_commands[key]
        ref=entry['source']
        expected=original['source_ref']
        exact=(ref['char_end_exclusive'],ref['literal_sha256_utf8'],entry['command_token'])==(expected['char_end_exclusive'],expected['literal_sha256_utf8'],'\\'+original['command'])
        check('union-exact-command-boundary',exact,command=entry['id'],source_path=key[0],char_start=key[1],union_char_end=ref['char_end_exclusive'],qa_char_end=expected['char_end_exclusive'])
        all_groups=[gid for gid,(reader,a,b) in group_intervals.items() if reader==entry['reader'] and a<=ref['char_start'] and ref['char_end_exclusive']<=b]
        check('union-command-all-source-containment',set(entry['all_containing_groups'])==set(all_groups),command=entry['id'])
        smallest=min(all_groups,key=lambda gid:group_intervals[gid][2]-group_intervals[gid][1]) if all_groups else None
        check('union-command-smallest-source-containment',entry['smallest_complete_source_group']==smallest,command=entry['id'])
        check('union-command-no-physical-count',entry['physical_count'] is None,command=entry['id'])
    for gid,entry in groups.items():
        expected_ids=[row['id'] for row in commands if row['smallest_complete_source_group']==gid]
        check('union-group-command-reciprocity',entry['literal_command_ids']==expected_ids,group=gid)
        reader,a,b=group_intervals[gid]
        parents=[other for other,(r,s,e) in group_intervals.items() if other!=gid and r==reader and s<=a and b<=e]
        children=[other for other,(r,s,e) in group_intervals.items() if other!=gid and r==reader and a<=s and e<=b]
        check('union-group-source-containment',set(entry['containing_groups'])==set(parents) and set(entry['contained_groups'])==set(children),group=gid)

    partition_counts={}
    for reader,partition in union['complete_source_partitions'].items():
        parts=partition['parts']
        expected_path=f'out/readers/025/{reader}/reading.tex'
        original=resolve_file(by_path[expected_path]['id'])
        cursor=0
        literals=[]
        for i,part in enumerate(parts):
            ref=part['complete_source']
            check('union-partition-contiguous-source',ref['source_path']==expected_path and ref['char_start']==cursor,reader=reader,part=i)
            cursor=ref['char_end_exclusive']
            literals.append(text_of(ref))
        check('union-partition-full-source-replay',cursor==len(original) and ''.join(literals)==original,reader=reader)
        partition_counts[reader]=len(parts)

    original_main={(x['source_ref']['path'],x['source_ref']['json_pointer']):x for x in inv['original_row_inventory'] if x['section'] in ['differences','doubts','inventory'] and x['reader'] in 'ABC'}
    raw_rows=union['raw_row_correspondence']
    by_id={row['id']:row for row in raw_rows}
    mapped_keys={(row['raw']['source_path'],row['raw']['json_pointer']) for row in raw_rows}
    check('union-all-original-main-rows',len(raw_rows)==len(by_id)==len(mapped_keys)==len(original_main) and mapped_keys==set(original_main),missing=sorted(set(original_main)-mapped_keys),extra=sorted(mapped_keys-set(original_main)))
    for row in raw_rows:
        original=json_value(row['raw'])
        check('union-all-original-row-fields',list(row['all_original_fields'])==list(original),row=row['id'])
        for key,ref in row['all_original_fields'].items():
            check('union-original-row-field-role',ref['source_path']==row['raw']['source_path'] and ref['json_pointer']==row['raw']['json_pointer']+'/'+key.replace('~','~0').replace('/','~1') and json_value(ref)==original[key],row=row['id'],field=key)
        explicit=[]
        for key in ['source_groups','source_group','group_id']:
            val=original.get(key)
            if isinstance(val,list):explicit.extend(val)
            elif isinstance(val,str):explicit.append(val)
        check('union-original-explicit-groups',set(row['explicit_source_groups'])==set(explicit),row=row['id'],expected=explicit,actual=row['explicit_source_groups'])
        check('union-raw-row-unselected',row['selected'] is None,row=row['id'])

    loci=union['source_locus_union']
    locus_by_id={row['id']:row for row in loci}
    check('union-skeleton-exact-locus-mirror',skeleton['rows']==loci)
    check('union-skeleton-exact-canonical-mirror',skeleton['canonical_original_C_rows']==union['canonical_original_C_rows'])
    check('union-locus-identities-unique',len(locus_by_id)==len(loci))
    rows_seen=[]
    groups_seen=set()
    for locus in loci:
        lid=locus['id']
        check('union-locus-three-own-readers',set(locus['readers'])==set('ABC'),locus=lid)
        for field in ['final','alternatives','confidence','count_C','count_H','physical_count_parent','marked_in_H','root_evidence']:
            check('union-selected-role-pending',locus[field] is None,locus=lid,field=field)
        check('union-locus-unapproved',locus['main_adjudicated'] is False and locus['main_approved'] is False,locus=lid)
        for reader,entry in locus['readers'].items():
            frame=union['reader_frames'][entry['reading']['complete_frame_ref']]
            check('union-own-reader-frame-role',frame['reader']==reader and frame['complete_source']['source_path']==f'out/readers/025/{reader}/reading.tex',locus=lid,reader=reader)
            for group in entry['complete_own_groups']:
                groups_seen.add(group)
                check('union-own-reader-group-role',groups[group]['reader']==reader,locus=lid,reader=reader,group=group)
            for field,section in [('raw_report_differences','differences'),('raw_doubts','doubts'),('raw_inventory','inventory')]:
                for rid in entry[field]:
                    rows_seen.append(rid)
                    raw=by_id[rid]
                    check('union-locus-row-reciprocity',raw['reader']==reader and raw['section']==section and raw['locus']==lid,locus=lid,reader=reader,row=rid)
            check('union-report-silence-scope',entry['report_silent']==(len(entry['raw_report_differences'])==0),locus=lid,reader=reader)
            for ref in entry.get('candidate_scope_sources',[]):
                check('union-own-reader-candidate-source-role',ref['source_path'].startswith(f'out/readers/025/{reader}/'),locus=lid,reader=reader,pointer=ref['json_pointer'])
            for ref in entry.get('own_literal_companions',[]):
                check('union-own-reader-companion-source-role',ref['source_path']==f'out/readers/025/{reader}/reading.tex',locus=lid,reader=reader)
        for witness,entry in locus['witnesses'].items():
            # Absence claims use an inspected whole witness span at their own
            # source role; a chosen reader string never substitutes for it.
            for _,value in visit(entry):
                if isinstance(value,dict) and 'source_path' in value and 'source_file' in value:
                    check('union-witness-source-role',value['source_path']==f'packets/025/{witness}.tex',locus=lid,witness=witness)
    check('union-all-rows-attached-once',Counter(rows_seen)==Counter(by_id.keys()),missing=sorted(set(by_id)-set(rows_seen)),duplicates=[k for k,v in Counter(rows_seen).items() if v!=1])
    check('union-all-groups-attached',groups_seen==set(groups),missing=sorted(set(groups)-groups_seen))

    canonical=union['canonical_original_C_rows']
    catalog=decode(files[by_path['out/checks/scan025_C_doubt_catalog.json']['id']]['payload'])
    check('union-eight-actual-C-row-identities',[row['source_id'] for row in canonical]==[row['source_id'] for row in catalog['canonical_doubt_rows']])
    for i,row in enumerate(canonical):
        original=catalog['canonical_doubt_rows'][i]
        check('union-original-C-parts-and-literal',row['source_parts']==original['source_parts'] and text_of(row['original_source'])==original['literal'] and json_value(row['canonical_catalog_ref'])==original,id=row['source_id'])
        check('union-original-C-three-reader-scopes',set(row['reader_reported_scopes'])==set('ABC'),id=row['source_id'])
        for reader,ref in row['reader_reported_scopes'].items():
            original_reader=json_value(ref)
            identity=original_reader.get('id',original_reader.get('source_row_id'))
            check('union-original-C-own-report-scope',ref['source_path']==f'out/readers/025/{reader}/report.json' and identity==row['source_id'],id=row['source_id'],reader=reader)
    check('union-eight-notation-slip-rows',len(union['other_C_notation_and_slips_context'])==len(catalog['other_source_rows'])==8)
    for i,row in enumerate(union['other_C_notation_and_slips_context']):
        original=catalog['other_source_rows'][i]
        check('union-context-source-section-and-literal',row['original_section']==original['section'] and text_of(row['original_source'])==original['literal'] and row['original_doubt_row_identity'] is None,index=i)
    packet_inventory=decode(files[by_path['packets/025/C_inventory.json']['id']]['payload'])
    check('union-thirteen-packet-inventory-rows',len(union['original_C_inventory'])==len(packet_inventory)==13)
    for i,row in enumerate(union['original_C_inventory']):
        check('union-packet-inventory-identity',json_value(row['raw'])==packet_inventory[i] and row['original_element']==packet_inventory[i]['element'],index=i)
    all_json={entry['path'] for entry in files.values() if entry['kind']=='json'}
    metadata=union['all_metadata_coverage']
    check('union-all-complete-metadata-documents',{entry['source_path'] for entry in metadata}==all_json and len(metadata)==len(all_json))
    for entry in metadata:
        check('union-metadata-complete-root',entry['complete_source']['json_pointer']=='',path=entry['source_path'])
    inventory_scope_direct=0
    for meta in inv['qualification_and_hand_metadata']:
        ref=meta['source_ref']
        if ref['path'].endswith('/report.json') and ref['json_pointer'].startswith('/inventory/'):
            inventory_scope_direct+=1
            check('union-direct-inventory-hand-scope-reference',(ref['path'],ref['json_pointer']) in json_reference_keys,path=ref['path'],pointer=ref['json_pointer'])
    check('union-H-catalog-local-scope',json_value(union['H_marker_catalog'])==decode(files[by_path['out/checks/scan025_H_marker_catalog.json']['id']]['payload']))
    s_scope=decode(files[by_path['out/checks/scan025_S_scope.json']['id']]['payload'])
    check('union-seven-S-source-rows',len(union['S_source_only_rows'])==len(s_scope['row_scopes'])==7)
    for i,row in enumerate(union['S_source_only_rows']):
        check('union-S-identity-and-source-role',row['S_id']==s_scope['row_scopes'][i]['id'] and json_value(row['raw_scope_ref'])==s_scope['row_scopes'][i] and row['root_ink_choice_applied'] is False and row['local_ink_locus'] is None and row['counts_C_H'] is None,index=i)
    check('union-no-declared-mapping-gaps',union['mapping_gaps']==[] and skeleton['mapping_gaps']==[])
    return {'union_path':str(union_path.relative_to(BASE)),'union_sha256_utf8':sha(union_raw),'skeleton_path':str(skeleton_path.relative_to(BASE)),'skeleton_sha256_utf8':sha(skeleton_raw),'loci':len(loci),'groups':len(groups),'main_original_rows':len(raw_rows),'literal_command_spans':len(commands),'text_reference_instances':text_ref_count,'json_reference_instances':json_ref_count,'unique_text_references':len(text_reference_keys),'unique_json_references':len(json_reference_keys),'direct_inventory_hand_scope_fields_checked':inventory_scope_direct,'complete_source_partition_parts':partition_counts}


if __name__=='__main__':
    main()
