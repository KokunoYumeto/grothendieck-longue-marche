#!/usr/bin/env python3
"""Source-only scan018 manifest and pending record; no image/ink work."""
from pathlib import Path
import copy
import hashlib
import json
import re

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
RELEASE = 'out/checks/scan018_released_readers.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return (BASE / path).read_text(encoding='utf-8')


def jread(path):
    return json.loads(read(path))


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def span(path, text, start, end, **extra):
    literal = text[start:end]
    return dict(manifest=path, char_start=start, char_end=end,
                offset_convention='zero-based Unicode code points; end exclusive',
                line_start=text.count('\n', 0, start) + 1,
                line_end=text.count('\n', 0, max(start, end-1)) + 1,
                excerpt=literal, literal_sha256_utf8=sha(literal.encode('utf-8')), **extra)


def json_spans(path, text):
    """Index exact original JSON value slices without reserializing report rows."""
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
                key, keyend = decoder.raw_decode(text, i)
                i = ws(keyend)
                assert text[i] == ':'
                escaped = key.replace('~', '~0').replace('/', '~1')
                i = ws(walk(i + 1, pointer + '/' + escaped))
                if text[i] == ',':
                    i = ws(i + 1)
                else:
                    break
        elif isinstance(value, list):
            i = ws(i + 1)
            k = 0
            while i < end and text[i] != ']':
                i = ws(walk(i, pointer + '/' + str(k)))
                k += 1
                if text[i] == ',':
                    i = ws(i + 1)
                else:
                    break
        return end

    walk(0, '')
    return result


def raw_rows(path, value, pointer, index):
    rows = value
    for part in pointer.strip('/').split('/'):
        if part:
            rows = rows[int(part)] if isinstance(rows, list) else rows[part]
    return [dict(value=row, source=index[pointer + '/' + str(i)]) for i, row in enumerate(rows)]


def tex_blocks(path, text):
    """Keep complete named groups, including outer figure and nested pictures."""
    groups = []
    names = list(re.finditer(r'^%\s*((?:G|M|GUIDE)\d+)\s*:[^\n]*', text, re.M))
    for m in names:
        stack = []
        for t in re.finditer(r'\\(?:begin|end)\{tikzpicture\}', text[:m.start()]):
            if t.group().startswith(r'\begin'):
                stack.append(t.start())
            else:
                stack.pop()
        begin = stack[0] if stack else text.find(r'\begin{tikzpicture}', m.end())
        group_start = begin if stack else m.start()
        if begin < 0:
            continue
        next_named = next((n.start() for n in names if n.start() > m.start()), len(text))
        if begin > next_named:
            continue
        depth = 0
        end = None
        for token in re.finditer(r'\\(?:begin|end)\{tikzpicture\}', text[begin:]):
            depth += 1 if token.group().startswith(r'\begin') else -1
            if depth == 0:
                end = begin + token.end()
                if any(text[max(0, begin-9):begin].endswith(w) for w in [r'\figure{',r'\unsure{']):
                    assert text[end] == '}'
                    end += 1
                break
        assert end is not None
        groups.append(dict(id=m.group(1), source=span(path, text, group_start, end)))
    commands = []
    for i, m in enumerate(re.finditer(r'\\(?:draw|fill|path|node)\b', text)):
        depth = 0
        end = None
        for k in range(m.start(), len(text)):
            char = text[k]
            if char in '{}' and (k == 0 or text[k-1] != '\\'):
                depth += 1 if char == '{' else -1
            if char == ';' and depth == 0:
                end = k+1
                break
        assert end is not None
        command = text[m.start():end]
        groups_here = [g['id'] for g in groups if g['source']['char_start'] <= m.start() < g['source']['char_end']]
        commands.append(dict(command_id=f'command-{i+1:03d}',
                             kind=re.match(r'\\(\w+)', command).group(1),
                             role='declared bounding rectangle' if 'use as bounding box' in command else 'source command; physical role follows source report/root',
                             group_ids=groups_here, source=span(path, text, m.start(), end)))
    return groups, commands


release = jread(RELEASE)
released = release['released_readers']
assert all(r in ['A', 'B', 'C'] for r in released)
pending = [r for r in ['A', 'B', 'C'] if r not in released]
source_paths = [
    'out/briefs/source_record_brief_v01.md', 'out/briefs/brief_v16_scan018.md',
    'packets/018/C.tex', 'packets/018/H.tex', 'packets/018/metadata.json',
    'packets/018/C_doubts.txt', 'packets/018/C_notes.txt', 'packets/018/C_inventory.json',
    'packets/018/notation.md', 'packets/018/S_rows.json',
    'out/checks/scan018_C_doubt_catalog.json', RELEASE,
]
sources = {}
fingerprints = {}
for path in source_paths:
    text = read(path)
    fingerprints[path] = dict(sha256=sha((BASE/path).read_bytes()), bytes=(BASE/path).stat().st_size)
    sources[path] = dict(complete_source=span(path, text, 0, len(text)))
    if path.endswith('.json'):
        sources[path]['value'] = json.loads(text)

catalog = jread('out/checks/scan018_C_doubt_catalog.json')
canonical_A_map = {
    'C018-R01-1': ['A01'], 'C018-R02-1': ['A02'], 'C018-R03-1': ['A03'],
    'C018-R04-1': ['A04'], 'C018-R05-1': ['A07'], 'C018-R06-1': ['A09'],
    'C018-R06-2': ['A08'], 'C018-R07-1': ['A12'], 'C018-R08-1': ['A14'],
    'C018-R09-1': ['A19'], 'C018-R09-2': ['A23'], 'C018-R09-3': ['A24'],
    'C018-R10-1': ['A25'], 'C018-R11-1': ['A27'], 'C018-R12-1': ['A31'],
    'C018-R13-1': ['A33'], 'C018-R13-2': ['A34'], 'C018-R14-1': ['A20'],
}
canonical_C_map = {
    'C018-R01-1': ['D01'], 'C018-R02-1': ['D02'], 'C018-R03-1': ['D03'],
    'C018-R04-1': ['D04'], 'C018-R05-1': ['D05'], 'C018-R06-1': ['D06a'],
    'C018-R06-2': ['D06b'], 'C018-R07-1': ['D07'], 'C018-R08-1': ['D08a'],
    'C018-R09-1': ['D09a'], 'C018-R09-2': ['D09b'], 'C018-R09-3': ['D09c'],
    'C018-R10-1': ['D10'], 'C018-R11-1': ['D11'], 'C018-R12-1': ['D12'],
    'C018-R13-1': ['D13a'], 'C018-R13-2': ['D13b'], 'C018-R14-1': ['D14'],
}
canonical_B_map = {
    'C018-R01-1': ['B01'], 'C018-R02-1': ['B02'], 'C018-R03-1': ['B03'],
    'C018-R04-1': ['B04'], 'C018-R05-1': ['B08'], 'C018-R06-1': ['B09'],
    'C018-R06-2': ['B10'], 'C018-R07-1': ['B13'], 'C018-R08-1': ['B15'],
    'C018-R09-1': ['B20'], 'C018-R09-2': ['B24'], 'C018-R09-3': ['B25'],
    'C018-R10-1': ['B26'], 'C018-R11-1': ['B28'], 'C018-R12-1': ['B33'],
    'C018-R13-1': ['B35'], 'C018-R13-2': ['B36'], 'C018-R14-1': ['B21'],
}
source_categories = []
cdpath = 'packets/018/C_doubts.txt'
cdtext = read(cdpath)
heads = list(re.finditer(r'^## .*$', cdtext, re.M))
for i, h in enumerate(heads):
    end = heads[i+1].start() if i+1 < len(heads) else len(cdtext)
    source_categories.append(dict(category=h.group()[3:], source=span(cdpath, cdtext, h.start(), end)))

reader_sources = {}
all_raw_rows = {}
candidate_inventory = []
cipath = 'packets/018/C_inventory.json'
citext = read(cipath)
ci = json_spans(cipath, citext)
for raw in raw_rows(cipath, json.loads(citext), '', ci):
    candidate_inventory.append(dict(reader='witness C', original=raw, selected=None, main_approved=False))

decisions = []
for reader in released:
    prefix = f'out/readers/018/{reader}/'
    rp = prefix + 'report.json'
    report_text = read(rp)
    report = json.loads(report_text)
    report_spans = json_spans(rp, report_text)
    tp = prefix + 'reading.tex'
    tex = read(tp)
    groups, commands = tex_blocks(tp, tex)
    rs = dict(report_path=rp, report_sha256=sha(report_text.encode('utf-8')),
              complete_report=span(rp, report_text, 0, len(report_text)),
              complete_tex=span(tp, tex, 0, len(tex)),
              complete_graphical_groups=groups, literal_tex_commands=commands,
              original_top_level_keys=list(report), extra_source_fields={})
    raw = {}
    for field in ['differences','doubts','inventory','notation','check_events','crops']:
        vals = report.get(field, [])
        if isinstance(vals, list):
            raw[field] = raw_rows(rp, report, '/' + field, report_spans)
    for key in report:
        if key not in raw:
            rs['extra_source_fields'][key] = dict(value=report[key], source=report_spans['/'+key.replace('~','~0').replace('/','~1')])
    for optional in ['reading.md','crop_manifest.json','crops_manifest.json','make_crops.py','write_report.py','build_report.py','source_check.json']:
        path = prefix + optional
        if (BASE/path).exists():
            value = read(path)
            fingerprints[path] = dict(sha256=sha(value.encode('utf-8')), bytes=(BASE/path).stat().st_size)
            if optional == 'reading.md':
                rs['complete_prose_audit'] = span(path, value, 0, len(value))
    for path, value in [(rp,report_text),(tp,tex)]:
        fingerprints[path] = dict(sha256=sha(value.encode('utf-8')), bytes=(BASE/path).stat().st_size)
    rs['raw_rows'] = raw
    reader_sources[reader] = rs
    all_raw_rows[reader] = raw
    for item in raw.get('inventory', []):
        candidate_inventory.append(dict(reader=reader, original=item, selected=None, main_approved=False))
    for item in raw.get('differences', []):
        row = item['value']
        readers = {r: [] for r in ['A','B','C']}
        readers[reader] = [row['reading']]
        proposals = {r: [] for r in ['A','B','C']}
        proposals[reader] = [copy.deepcopy(row)]
        provenance = {r: [] for r in ['A','B','C']}
        provenance[reader] = [item['source']]
        cmap = {'A':canonical_A_map,'B':canonical_B_map,'C':canonical_C_map}[reader]
        mapped_parts = [p for p, ids in cmap.items() if row['id'] in ids]
        decisions.append(dict(
            id=f'PENDING-{reader}-{row["id"]}', original_reader=reader, original_id=row['id'],
            location=row['location'], C=row.get('C'), H=row.get('H'), final=None,
            readers=readers, readers_report_only=copy.deepcopy(readers), reader_provenance=provenance,
            reader_proposals=proposals, evidence=None, confidence=None, confidence_status='pending root',
            kind=row['kind'], kind_status='source proposal; pending root', diff_C=None, diff_H=None,
            count_status='pending root', C_doubt_status=None, source_C_doubt_parts=mapped_parts,
            marked_in_H=False, marked_in_H_basis='Complete packets/018/H.tex has no editorial uncertain/ill placeholder; manuscript struck/add states remain in source provenance.',
            main_approved=False, final_source_attachment=[], physical_count_parent=None,
            reader_mapping_status='Source-row staging; pending cross-reader union and exact local TeX supplements',
            original_raw_source=item['source']))

crosswalk = []
for row in catalog['rows']:
    r = copy.deepcopy(row)
    r['reader_original_maps'] = {}
    if 'A' in reader_sources:
        ordinal = int(row['source_id'].split('R')[-1])
        m = reader_sources['A']['extra_source_fields']['C_source_doubt_map']['value'][ordinal-1]
        r['reader_original_maps']['A'] = copy.deepcopy(m)
    if 'C' in reader_sources:
        ordinal = int(row['source_id'].split('R')[-1])
        m = reader_sources['C']['extra_source_fields']['C_doubt_source_rows']['value'][ordinal-1]
        r['reader_original_maps']['C'] = copy.deepcopy(m)
    if 'B' in reader_sources:
        ordinal = int(row['source_id'].split('R')[-1])
        m = reader_sources['B']['extra_source_fields']['C_doubt_source_map']['value'][ordinal-1]
        r['reader_original_maps']['B'] = copy.deepcopy(m)
    for p in r['source_parts']:
        p['reader_source_ids'] = {'A': canonical_A_map.get(p['part_id'], []),
                                  'B': canonical_B_map.get(p['part_id'], []) if 'B' in released else [],
                                  'C': canonical_C_map.get(p['part_id'], []) if 'C' in released else []}
        p['root_status'] = None
        p['main_approved'] = False
    if row['source_id'] == 'C018-R08':
        r['additional_inspected_recurrence'] = dict(location='final U subscript',
            reader_source_ids={'A':['notation/4'], 'B':['B37'] if 'B' in released else [], 'C':['D08b'] if 'C' in released else []},
            scope='The original place names the added U; the context mentions final U. Readers B/C interpret the row as covering both. Preserve both interpretations, B retained/C resolved recurrence statuses, and C mixed raw status without increasing the canonical 18 primary parts.',
            canonical_primary_part=False,root_status=None,main_approved=False)
    crosswalk.append(r)

manifest = dict(scan=18, scope='source-only; no image views, ink choices, mathematical or geometry calculations',
                released_readers=released, pending_readers=pending, release_source=RELEASE,
                main_adjudicated=False, sources=sources, source_fingerprints=fingerprints,
                source_categories=source_categories, reader_sources=reader_sources,
                C_doubt_crosswalk=crosswalk, candidate_inventory=candidate_inventory,
                root_decision_source='out/checks/scan018_main_decisions.md',
                root_decisions_applied=False)
write('scan018_source_union.json', manifest)
meta = jread('packets/018/metadata.json')
record = dict(scan=18, folder=meta['folder'], their_page=meta['their_page'], hua_has=meta['hua_has'],
              filename=Path(meta['codex_file']).name, brief_version='v16', main_adjudicated=False,
              released_readers=released, pending_readers=pending,
              decisions=decisions, doubts=[], inventory=[], candidate_inventory=candidate_inventory,
              notes='Source-only pending draft. Root has supplied no selected ink outcomes to this preparation stage.',
              abbreviations=[dict(form=f, expansion=e, source='packets/018/C_doubts.txt, Abbreviations', selected=None)
                             for f,e in [('card','cardinal'),('ens','ensemble'),('i.e.','id est'),('OK','okay')]],
              C_source_rows=crosswalk, source_union_manifest='out/checks/scan018_source_union.json',
              source_union_sha256=sha((OUT/'scan018_source_union.json').read_bytes()),
              reader_raw_rows=all_raw_rows,
              source_counting_constraints=[
                  dict(raw_ids=['A25'], issue='Same primary choisi retained; added alternative alone supplies no new C count.', status='pending root'),
                  dict(raw_ids=['A16','A17'], issue='Guide/hook context; preserve both raw identities and paths.', status='pending root'),
                  dict(raw_ids=['A25','A26'], issue='Word/cancellation plus two endpoint points; preserve components; parent supplied by root.', status='pending root'),
                  dict(raw_ids=['A31','A32'], issue='A explicitly supplies one H correction/placement parent.', status='pending root'),
                  dict(raw_ids=['A35','A36'], issue='One final-OK state/path cluster.', status='pending root')],
              counts=dict(status='pending root', C=None,H=None),
              C_doubt_resolution_counts=dict(actual_rows=14,primary_parts=18,resolved=None,retained=None,mixed=None,pending=18),
              mechanical_verification=dict(status='source preparation only',no_image_viewed_by_clerk=True,
                  numerical_geometry_checks_by_clerk=0,mathematical_theorem_checks=0,
                  raw_difference_rows_preserved=sum(len(x.get('differences',[])) for x in all_raw_rows.values()),
                  raw_doubt_rows_preserved=sum(len(x.get('doubts',[])) for x in all_raw_rows.values()),
                  raw_inventory_rows_preserved=len(candidate_inventory),
                  recorded_prior_coordinate_event_rerun=False,all_ink_choices_supplied_by_root=False),
              source_attachment_status='pending root selections and complete A/B/C local reading union',
              S_source_rows=jread('packets/018/S_rows.json'),
              S_public_candidates=[dict(S_id='SA01-K81-06',S_status='pending root; no local matching example inferred from broad source range',main_approved=False)])
write('scan018_record_draft.json', record)
write('scan018_reader_fingerprints.json',dict(scan=18,released_readers=released,pending_readers=pending,
    files={path:dict(path=path,sha256=value['sha256']) for path,value in fingerprints.items()
           if path.startswith('out/readers/018/')},scope='Exact released reader text and JSON/script source fingerprints; no image opening.'))
write('scan018_source_fingerprints.json', dict(scan=18,source_fingerprints=fingerprints,
       prepared_files={p:dict(sha256=sha((OUT/p).read_bytes())) for p in ['scan018_source_union.json','scan018_record_draft.json','scan018_source_attention.md']},
       selected_draft=None, selected_map=None, record_stage='source-only pending',
       root_approval_flags=False))
print(json.dumps(dict(released=released,pending=pending,raw_differences=len(decisions),
                     C_original_rows=len(crosswalk),C_primary_parts=sum(len(r['source_parts']) for r in crosswalk),
                     inventory_source_rows=len(candidate_inventory),
                     outputs=['scan018_source_union.json','scan018_record_draft.json','scan018_source_fingerprints.json']),ensure_ascii=False))
