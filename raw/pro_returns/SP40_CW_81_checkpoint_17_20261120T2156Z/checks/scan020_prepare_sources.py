#!/usr/bin/env python3
"""Index released scan020 text sources without images or ink decisions."""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re
import sys
sys.dont_write_bytecode = True
# Source-span and JSON-pointer helpers only; no prior-page selections are used.
from scan019_prepare_sources import span, json_spans

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
READER_FILES = {
    'A': ('reading.tex', 'report.json', 'reading.md', 'image_audit.json', 'source_checks.json', 'source_check_history.json'),
    'B': ('reading.tex', 'report.json', 'reading.md', 'image_audit.json', 'source_audit.json'),
    'C': ('reading.tex', 'report.json', 'reading.md', 'image_audit.json', 'source_audit.json'),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return (BASE / path).read_text(encoding='utf-8')


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def object_at(value, pointer):
    for key in pointer.strip('/').split('/') if pointer else []:
        key = key.replace('~1', '/').replace('~0', '~')
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def text_index(path, text):
    # Purely lexical source spans. Coordinates and declarations remain verbatim.
    blocks = []
    cursor = 0
    for i, match in enumerate(re.finditer(r'\\\[(.*?)\\\]', text, re.S)):
        if match.start() > cursor:
            blocks.append(dict(kind='complete inter-display source', source=span(path, text, cursor, match.start())))
        blocks.append(dict(id=f'display-{i+1:02d}', kind='complete display source', source=span(path, text, match.start(), match.end())))
        cursor = match.end()
    if cursor < len(text):
        blocks.append(dict(kind='complete trailing source', source=span(path, text, cursor, len(text))))
    comments = [span(path, text, m.start(), m.end()) for m in re.finditer(r'^%[^\n]*', text, re.M)]
    commands = []
    for i, match in enumerate(re.finditer(r'\\(?:draw|fill|path|node|coordinate|useasboundingbox)\b', text)):
        depth = 0
        for k in range(match.start(), len(text)):
            char = text[k]
            if char in '{}' and (k == 0 or text[k-1] != '\\'):
                depth += 1 if char == '{' else -1
            if char == ';' and depth == 0:
                commands.append(dict(command_id=f'command-{i+1:03d}', kind=match.group()[1:], source=span(path, text, match.start(), k+1)))
                break
        else:
            raise AssertionError((path, match.start(), 'unterminated literal command'))
    environments = []
    stack = []
    for match in re.finditer(r'\\(begin|end)\{tikzpicture\}', text):
        if match[1] == 'begin':
            stack.append(match.start())
        else:
            assert stack, (path, match.start())
            start = stack.pop()
            environments.append(dict(depth=len(stack), source=span(path, text, start, match.end())))
    assert not stack, path
    environments.sort(key=lambda row: row['source']['char_start'])
    return dict(complete_blocks=blocks, complete_comment_lines=comments,
                literal_graphical_commands=commands, complete_tikz_environments=environments,
                indexing_scope='Literal source boundaries only; no coordinate arithmetic or rendering.')


def collect(released):
    assert all(r in 'ABC' for r in released) and len(set(released)) == len(released)
    paths = ['out/briefs/source_record_brief_v02.md']
    paths += [p.relative_to(BASE).as_posix() for p in sorted((BASE/'packets/020').iterdir()) if p.suffix in ('.tex','.json','.md','.txt')]
    paths += ['out/checks/scan020_C_doubt_catalog.json']
    for reader in released:
        paths += [f'out/readers/020/{reader}/{name}' for name in READER_FILES[reader]]
    sources, fingerprints, indices, parsed = {}, {}, {}, {}
    for path in paths:
        data = (BASE/path).read_bytes()
        text = data.decode('utf-8')
        fingerprints[path] = dict(sha256=sha(data), bytes=len(data))
        sources[path] = dict(complete_source=span(path, text))
        if path.endswith('.json'):
            parsed[path] = json.loads(text)
            indices[path] = json_spans(path, text)
            sources[path].update(value=parsed[path], top_level_sources={k:v for k,v in indices[path].items() if k.count('/')==1})
    readers, candidates = {}, []
    cp = 'packets/020/C_inventory.json'
    for i, row in enumerate(parsed[cp]):
        candidates.append(dict(reader='witness C', value=copy.deepcopy(row), source=indices[cp][f'/{i}'], selected=None, main_approved=False))
    for reader in released:
        rp = f'out/readers/020/{reader}/report.json'
        tp = f'out/readers/020/{reader}/reading.tex'
        report = parsed[rp]
        raw, extra = {}, {}
        for key, value in report.items():
            ptr = '/' + key.replace('~','~0').replace('/','~1')
            if isinstance(value, list):
                raw[key] = [dict(value=copy.deepcopy(row), source=indices[rp][f'{ptr}/{i}']) for i,row in enumerate(value)]
            else:
                extra[key] = dict(value=copy.deepcopy(value), source=indices[rp][ptr])
        # Nested original maps retain their original field and JSON-pointer identity.
        map_pointer = '/notes/C_source_doubt_map' if reader == 'C' else '/C_doubt_source_map'
        original_maps = [dict(value=copy.deepcopy(row), source=indices[rp][f'{map_pointer}/{i}'])
                         for i,row in enumerate(object_at(report,map_pointer))]
        readers[reader] = dict(report_path=rp, complete_report=sources[rp]['complete_source'],
            complete_tex=sources[tp]['complete_source'],
            complete_prose_audit=sources[f'out/readers/020/{reader}/reading.md']['complete_source'],
            original_top_level_keys=list(report), raw_rows=raw, extra_source_fields=extra,
            original_C_doubt_maps=original_maps,
            tex_index=text_index(tp,read(tp)),
            report_json_pointer_index=indices[rp], original_report_flags_preserved=True,
            source_audits={path:sources[path] for path in paths if path.startswith(f'out/readers/020/{reader}/') and path.endswith('.json') and ('audit' in path or 'check' in path)})
        for row in raw.get('inventory',[]):
            candidates.append(dict(reader=reader,**copy.deepcopy(row),selected=None,main_approved=False))
    catalog_path='out/checks/scan020_C_doubt_catalog.json'
    catalog=parsed[catalog_path]
    crosswalk=[]
    for i, original in enumerate(catalog['rows']):
        row=copy.deepcopy(original)
        row['catalog_source']=copy.deepcopy(indices[catalog_path][f'/rows/{i}'])
        row['reader_original_maps']={}
        row['reader_difference_sources']={}
        row['reader_identifier_correspondence']={}
        for reader, reader_source in readers.items():
            original_map=reader_source['original_C_doubt_maps'][i]
            value=original_map['value']
            # Source matching is exact location/reading and ordinal identity; no ink inference.
            if reader=='C':
                assert value['raw_row']==original['literal']
            else:
                raw_fields=[x.strip() for x in original['literal'].strip('|').split('|')]
                explicit_location_spelling={('A',8):'beside membership sign before pi_0'}
                explicit_reading_spelling={('A',3):'Sigma_i',('B',3):r'\Sigma_i',('A',8):'Rightarrow'}
                assert value['source_location']==explicit_location_spelling.get((reader,i),raw_fields[1]),(reader,i,value['source_location'],raw_fields[1])
                assert value['source_reading']==explicit_reading_spelling.get((reader,i),raw_fields[2]),(reader,i)
                row.setdefault('exact_identifier_basis',{})[reader]=dict(
                    source_row_ordinal=i+1,reader_original_id=value['id'],
                    actual_source_location=raw_fields[1],reader_recorded_source_location=value['source_location'],
                    actual_source_reading=raw_fields[2],reader_recorded_source_reading=value['source_reading'],
                    scope='Exact ordered source row and explicitly listed original spellings; original fields are preserved without rewriting.')
            row['reader_original_maps'][reader]=[copy.deepcopy(original_map)]
            row['reader_identifier_correspondence'][reader]=value['id']
            id_values=[]
            if reader=='C': id_values=[item['difference_id'] for item in value['local_decisions']]
            elif reader=='A': id_values=value['local_reports']
            else: id_values=value['local_records']
            # Map values may contain exact IDs or richer original local-record objects.
            id_values=[v if isinstance(v,str) else v.get('id',v.get('difference_id')) for v in id_values]
            row['reader_difference_sources'][reader]=[copy.deepcopy(item) for item in reader_source['raw_rows']['differences'] if item['value']['id'] in id_values]
            assert len(row['reader_difference_sources'][reader])==len(id_values),(reader,i,id_values)
        for part_i,part in enumerate(row['source_parts']):
            part['original_decision_status']=part['decision_status']
            part['reader_source_ids']={reader:[item['value']['id'] for item in row['reader_difference_sources'][reader]] for reader in released}
            if i==0:
                for reader in released:
                    # Each released original map lists the three occurrences in physical order.
                    part['reader_source_ids'][reader]=[row['reader_difference_sources'][reader][part_i]['value']['id']]
            part['root_status']=None
            part['main_approved']=False
        crosswalk.append(row)
    dp='packets/020/C_doubts.txt'; dt=read(dp)
    heads=list(re.finditer(r'^## .*$',dt,re.M))
    categories=[dict(category=h.group()[3:],source=span(dp,dt,h.start(),heads[i+1].start() if i+1<len(heads) else len(dt))) for i,h in enumerate(heads)]
    ht=read('packets/020/H.tex')
    placeholder= r'\struck{\ill{}}'
    placeholders=[dict(id=f'H020-ILL-{i+1:02d}',source=span('packets/020/H.tex',ht,m.start(),m.end()),
        enclosing_line=span('packets/020/H.tex',ht,ht.rfind('\n',0,m.start())+1,ht.find('\n',m.end()) if '\n' in ht[m.end():] else len(ht)),
        count_parent=None,main_approved=False) for i,m in enumerate(re.finditer(re.escape(placeholder),ht))]
    return dict(scan=20,scope='Source-only bookkeeping; no image view, ink decision, rendering or optional mathematical/coordinate computation.',
        released_readers=released,pending_readers=[r for r in 'ABC' if r not in released],main_adjudicated=False,
        source_fingerprints=fingerprints,sources=sources,source_categories=categories,
        witness_tex_indices={r:text_index(f'packets/020/{r}.tex',read(f'packets/020/{r}.tex')) for r in 'CH'},
        H_shared_ill_placeholders=placeholders,reader_sources=readers,C_doubt_crosswalk=crosswalk,
        canonical_C_catalog=dict(path=catalog_path,sha256=fingerprints[catalog_path]['sha256'],actual_rows=11,primary_parts=13),
        candidate_inventory=candidates,root_decisions_applied=False,root_decision_source='out/checks/scan020_main_decisions.md',
        clerk_preparation_history=['The initial invocation sought A/source_audit.json and stopped before any output write; A uses source_checks.json and source_check_history.json. The explicit final-source list was corrected to those observed names. No reader source changed.',
            'The next invocation stopped before output because an exact source-spelling assertion encountered A R04 Sigma_i for source Σ_i. Explicit original spelling correspondences were added for A R04/R09 and B R04; every original field remains literal.'],
        selection_status='Pending root; raw source flags and statuses are historical reader proposals.')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--released',required=True)
    parser.add_argument('--final-union',action='store_true')
    args=parser.parse_args()
    released=list(args.released)
    if args.final_union: assert released==list('ABC')
    result=collect(released)
    name='scan020_source_union.json' if args.final_union else 'scan020_source_staging.json'
    write(name,result)
    if args.final_union:
        write('scan020_reader_fingerprints.json',dict(scan=20,released_readers=released,
            files={p:dict(path=p,**v) for p,v in result['source_fingerprints'].items() if p.startswith('out/readers/020/')},
            scope='Released final text/JSON returns and their actual named source audits. Image paths are provenance strings only; no image bytes read or hashed.'))
        write('scan020_source_fingerprints.json',dict(scan=20,source_fingerprints=result['source_fingerprints'],
            source_union=dict(path='out/checks/'+name,sha256=sha((OUT/name).read_bytes())),selected_draft=None,
            selected_map=None,record_stage='Complete released source union; ink/count choices pending root.',root_approval_flags=False))
    print(json.dumps(dict(output='out/checks/'+name,sha256=sha((OUT/name).read_bytes()),released=released,
        pending=result['pending_readers'],reader_source_rows={r:{k:len(v) for k,v in s['raw_rows'].items()} for r,s in result['reader_sources'].items()}),ensure_ascii=False))
