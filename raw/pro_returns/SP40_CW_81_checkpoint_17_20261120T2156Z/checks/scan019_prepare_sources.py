#!/usr/bin/env python3
"""Preserve explicitly released scan019 text sources; no ink/image operations."""
from pathlib import Path
import argparse
import copy
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return (BASE / path).read_text(encoding='utf-8')


def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def span(path, text, start=0, end=None, **extra):
    end = len(text) if end is None else end
    literal = text[start:end]
    return dict(path=path, manifest=path, char_start=start, char_end=end,
                offset_convention='zero-based Unicode code points; end exclusive',
                line_start=text.count('\n', 0, start) + 1,
                line_end=text.count('\n', 0, max(start, end - 1)) + 1,
                excerpt=literal, literal_sha256_utf8=sha(literal.encode()), **extra)


def json_spans(path, text):
    """Index untouched original JSON values by JSON Pointer and exact offsets."""
    decoder = json.JSONDecoder()
    result = {}

    def ws(i):
        while i < len(text) and text[i].isspace():
            i += 1
        return i

    def walk(i, pointer):
        i = ws(i)
        start = i
        value, end = decoder.raw_decode(text, i)
        result[pointer] = span(path, text, start, end, pointer=pointer)
        if isinstance(value, dict):
            i = ws(i + 1)
            while i < end and text[i] != '}':
                key, key_end = decoder.raw_decode(text, i)
                i = ws(key_end)
                assert text[i] == ':'
                escaped = key.replace('~', '~0').replace('/', '~1')
                i = ws(walk(i + 1, pointer + '/' + escaped))
                if text[i] != ',':
                    break
                i = ws(i + 1)
        elif isinstance(value, list):
            i = ws(i + 1)
            k = 0
            while i < end and text[i] != ']':
                i = ws(walk(i, pointer + '/' + str(k)))
                k += 1
                if text[i] != ',':
                    break
                i = ws(i + 1)
        return end

    walk(0, '')
    return result


def tex_index(path, text):
    """Lexical source groups and literal commands only; no geometry analysis."""
    blocks = []
    cursor = 0
    for i, match in enumerate(re.finditer(r'\\\[(.*?)\\\]', text, re.S)):
        if match.start() > cursor:
            blocks.append(dict(kind='complete inter-display source', source=span(path, text, cursor, match.start())))
        blocks.append(dict(id=f'display-{i + 1:02d}', kind='complete display source',
                           source=span(path, text, match.start(), match.end())))
        cursor = match.end()
    if cursor < len(text):
        blocks.append(dict(kind='complete trailing source', source=span(path, text, cursor, len(text))))
    comments = [span(path, text, m.start(), m.end()) for m in re.finditer(r'^%[^\n]*', text, re.M)]
    commands = []
    for i, match in enumerate(re.finditer(r'\\(?:draw|fill|path|node|coordinate)\b', text)):
        depth = 0
        end = None
        for k in range(match.start(), len(text)):
            char = text[k]
            if char in '{}' and (k == 0 or text[k - 1] != '\\'):
                depth += 1 if char == '{' else -1
            if char == ';' and depth == 0:
                end = k + 1
                break
        assert end is not None, (path, match.start())
        commands.append(dict(command_id=f'command-{i + 1:03d}',
                             kind=match.group()[1:], source=span(path, text, match.start(), end)))
    return dict(complete_blocks=blocks, complete_comment_lines=comments, literal_graphical_commands=commands)


def collect(released):
    assert all(r in 'ABC' for r in released)
    source_paths = [
        'out/briefs/source_record_brief_v01.md',
        *[p.relative_to(BASE).as_posix() for p in sorted((BASE / 'packets/019').iterdir()) if p.suffix in ('.tex', '.json', '.md', '.txt')],
        'out/checks/scan019_C_doubt_catalog.json',
    ]
    for optional in ['scan019_root_processing.md','scan019_main_decisions.md','scan019_root_crop_audit.json',
                     'scan019_root_graphics.tex','scan019_root_brace.tex','scan019_root_source_additions.json',
                     'scan019_tex_candidates.json']:
        if (OUT / optional).exists():
            source_paths.append('out/checks/'+optional)
    for r in released:
        # Enumerating only the explicitly released reader's own directory.
        source_paths.extend(p.relative_to(BASE).as_posix() for p in sorted((BASE / f'out/readers/019/{r}').rglob('*'))
                            if p.is_file() and p.suffix in ('.tex', '.json', '.md', '.txt', '.py'))
    sources = {}
    fingerprints = {}
    for path in source_paths:
        data = (BASE / path).read_bytes()
        text = data.decode('utf-8')
        fingerprints[path] = dict(sha256=sha(data), bytes=len(data))
        sources[path] = dict(complete_source=span(path, text))
        if path.endswith('.json'):
            sources[path]['value'] = json.loads(text)
            # Complete original JSON retained above; indices below hold every top-level row/value.
            indices = json_spans(path, text)
            sources[path]['top_level_sources'] = {k: v for k, v in indices.items() if k.count('/') == 1}
    readers = {}
    candidates = []
    cp = 'packets/019/C_inventory.json'
    ci = json_spans(cp, read(cp))
    for i, row in enumerate(json.loads(read(cp))):
        candidates.append(dict(reader='witness C', value=copy.deepcopy(row), source=ci[f'/{i}'],
                               selected=None, main_approved=False))
    for reader in released:
        rp = f'out/readers/019/{reader}/report.json'
        rt = read(rp)
        report = json.loads(rt)
        ri = json_spans(rp, rt)
        tp = f'out/readers/019/{reader}/reading.tex'
        tt = read(tp)
        raw = {}
        extra = {}
        for key, value in report.items():
            ptr = '/' + key.replace('~', '~0').replace('/', '~1')
            if isinstance(value, list):
                raw[key] = [dict(value=copy.deepcopy(row), source=ri[ptr + '/' + str(i)]) for i, row in enumerate(value)]
            else:
                extra[key] = dict(value=copy.deepcopy(value), source=ri[ptr])
        readers[reader] = dict(
            report_path=rp, complete_report=sources[rp]['complete_source'],
            complete_tex=sources[tp]['complete_source'],
            complete_prose_audit=sources[f'out/readers/019/{reader}/reading.md']['complete_source'],
            original_top_level_keys=list(report), raw_rows=raw, extra_source_fields=extra,
            tex_index=tex_index(tp, tt),
            original_report_flags_preserved=True,
            source_audits={p:sources[p] for p in source_paths if p.startswith(f'out/readers/019/{reader}/')
                           and p.endswith('.json') and ('audit' in p or 'check' in p)},
        )
        for row in raw.get('inventory', []):
            candidates.append(dict(reader=reader, **copy.deepcopy(row), selected=None, main_approved=False))
    catalog = json.loads(read('out/checks/scan019_C_doubt_catalog.json'))
    crosswalk = []
    for original in catalog['rows']:
        row = copy.deepcopy(original)
        ordinal = int(row['source_id'].split('R')[-1])
        short_id = f'R{ordinal:02d}'
        c_reader_id = f'C019.R{ordinal:02d}'
        row['reader_identifier_correspondence'] = dict(A=short_id, B=short_id, C=c_reader_id,
            basis='Exact ordered twelve source locations/readings in each original map; raw identifiers remain unchanged.')
        row['reader_original_maps'] = {}
        row['reader_difference_sources'] = {}
        for reader, source in readers.items():
            map_rows = []
            for field, items in source['raw_rows'].items():
                if field in ['differences','doubts','inventory','notation','crops','image_ledger','brief_feedback','graphics','check_events']:
                    continue
                for item in items:
                    value = item['value']
                    if isinstance(value, dict) and (value.get('id') in [short_id,c_reader_id] or value.get('source_ordinal') == ordinal
                            or value.get('source_row') == short_id or value.get('source_row_id') == short_id
                            or value.get('source_order') == ordinal):
                        map_rows.append(dict(source_field=field, **copy.deepcopy(item)))
            row['reader_original_maps'][reader] = map_rows
            row['reader_difference_sources'][reader] = [copy.deepcopy(item) for item in source['raw_rows'].get('differences', [])
                if item['value'].get('C_source_row') == short_id or item['value'].get('source_C_doubt_row') == c_reader_id]
        for part in row['source_parts']:
            part['reader_source_ids'] = {r:[item['value']['id'] for item in row['reader_difference_sources'].get(r, [])] for r in 'ABC'}
            part['root_status'] = None
            part['main_approved'] = False
        crosswalk.append(row)
    dp = 'packets/019/C_doubts.txt'
    dt = read(dp)
    heads = list(re.finditer(r'^## .*$', dt, re.M))
    categories = [dict(category=h.group()[3:], source=span(dp,dt,h.start(),heads[i+1].start() if i+1<len(heads) else len(dt)))
                  for i,h in enumerate(heads)]
    return dict(scan=19, scope='source-only; no image views, ink decisions, mathematical or coordinate computations',
                released_readers=released, pending_readers=[r for r in 'ABC' if r not in released],
                main_adjudicated=False, source_fingerprints=fingerprints, sources=sources,
                source_categories=categories, reader_sources=readers, C_doubt_crosswalk=crosswalk,
                candidate_inventory=candidates, root_decisions_applied=False,
                root_decision_source='out/checks/scan019_main_decisions.md',
                selection_status='pending root; raw source flags and statuses are proposals only')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--released', required=True, help='Only explicitly root-released readers, e.g. AB')
    parser.add_argument('--final-union', action='store_true')
    args = parser.parse_args()
    released = list(args.released)
    result = collect(released)
    if args.final_union:
        assert released == list('ABC'), 'Complete union awaits root release of all readers.'
        name = 'scan019_source_union.json'
    else:
        name = 'scan019_source_staging.json'
    write(name, result)
    if args.final_union:
        write('scan019_reader_fingerprints.json', dict(scan=19, released_readers=released,
            files={p:dict(path=p,**v) for p,v in result['source_fingerprints'].items() if p.startswith('out/readers/019/')},
            scope='All frozen released text/JSON/Python sources; images neither read nor hashed.'))
        write('scan019_source_fingerprints.json', dict(scan=19,
            source_fingerprints=result['source_fingerprints'],
            source_union=dict(path='out/checks/'+name,sha256=sha((OUT/name).read_bytes())),
            selected_draft=None, selected_map=None, record_stage='source-only pending',root_approval_flags=False))
    print(json.dumps(dict(output='out/checks/'+name,sha256=sha((OUT/name).read_bytes()),released=released,
                         pending=result['pending_readers'],reader_source_rows={r:{k:len(v) for k,v in x['raw_rows'].items()}
                             for r,x in result['reader_sources'].items()}),ensure_ascii=False))
