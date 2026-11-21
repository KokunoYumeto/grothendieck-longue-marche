"""Exact frozen A source catalogue; source references are lossless lookups.

Reads textual sources only. This script draws no ink, decides no reading and
does not read any other reader directory.
"""
import copy
import hashlib
import json
import re
from pathlib import Path

BASE = Path('/workspace/scratch/94548b74fbe0')
ROOT = BASE / 'out/readers/026/A'
OUT = BASE / 'out/checks'
P = 'scan026_source_A_catalog_'
NAMES = ['reading.tex', 'reading.md', 'report.json', 'source_map.json', 'crop_manifest.json', 'frozen_hashes.json']
raw = {n: (ROOT / n).read_bytes() for n in NAMES}
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha(raw['reading.tex']) == 'c5079dace4d580a4695749bb745d382e3828681f98e8c037785fc6ac985b5513'
assert sha(raw['report.json']) == '1f4f9f23873d17e9bbd341c59f32b1739855a5e1e6fad2c28d3328283faeab56'
text = raw['reading.tex'].decode()
report = json.loads(raw['report.json'])
source_map = json.loads(raw['source_map.json'])
crops = json.loads(raw['crop_manifest.json'])
parsed = {n: json.loads(raw[n]) for n in NAMES if n.endswith('.json')}


def ref(name, pointer=''):
    return {'path': 'out/readers/026/A/' + name, 'sha256': sha(raw[name]), 'json_pointer': pointer}


def esc(key):
    return str(key).replace('~', '~0').replace('/', '~1')


def value_at(name, pointer):
    v = parsed[name]
    for bit in pointer.split('/')[1:]:
        key = bit.replace('~1', '/').replace('~0', '~')
        v = v[int(key)] if isinstance(v, list) else v[key]
    return v


def span(start, end):
    s = text[start:end]
    return {'path': 'out/readers/026/A/reading.tex', 'file_sha256': sha(raw['reading.tex']),
            'start_char': start, 'end_char_exclusive': end,
            'start_utf8_byte': len(text[:start].encode()), 'end_utf8_byte_exclusive': len(text[:end].encode()),
            'line_start': text.count('\n', 0, start) + 1,
            'line_end': text.count('\n', 0, max(start, end-1)) + 1,
            'span_sha256': sha(s.encode())}


def write(name, value):
    (OUT / (P + name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


# Every report field is represented through an exact ordered reference list.
# The displayed source fields are literal copies checked below; no field is
# silently filled from another source, and no missing field gains a value.
display_keys = {'id', 'location', 'reading', 'alternatives', 'complete_candidates', 'confidence',
                'kind', 'diff_C', 'diff_H', 'C_doubt_status', 'physical_cluster', 'physical_clusters',
                'source_group', 'local_parts', 'local_recurrences', 'H_count_parent', 'hand',
                'candidate_specific_hand', 'role', 'attachment', 'element', 'position',
                'first_words_or_objects', 'bbox', 'readers_crop', 'crop', 'C', 'H', 'qualification',
                'status', 'scope_note', 'source_annotation_note'}
records = []
for section, entries in report.items():
    if not isinstance(entries, list):
        continue
    for index, entry in enumerate(entries):
        pointer = '/' + esc(section) + '/' + str(index)
        if not isinstance(entry, dict):
            records.append({'section': section, 'index': index, 'raw_ref': ref('report.json', pointer), 'display': entry})
            continue
        fields = [{'key': k, 'ref': ref('report.json', pointer + '/' + esc(k))} for k in entry]
        display = {k: copy.deepcopy(v) for k, v in entry.items() if k in display_keys}
        reconstructed = {field['key']: value_at('report.json', field['ref']['json_pointer']) for field in fields}
        assert json.dumps(reconstructed, ensure_ascii=False) == json.dumps(entry, ensure_ascii=False)
        assert all(display[k] == entry[k] for k in display)
        records.append({'section': section, 'index': index, 'raw_ref': ref('report.json', pointer),
                        'ordered_field_references': fields, 'display': display})

groups = []
for i, group in enumerate(source_map['local_groups']):
    start, end = group['source_char_start'], group['source_char_end_exclusive']
    assert text[start:end] == group['source_excerpt']
    assert sha(text[start:end].encode()) == group['source_excerpt_sha256']
    parents = [g['id'] for g in source_map['local_groups']
               if g['source_char_start'] <= start and end <= g['source_char_end_exclusive'] and g['id'] != group['id']]
    item = {k: copy.deepcopy(v) for k, v in group.items() if k != 'source_excerpt'}
    item['raw_ref'] = ref('source_map.json', '/local_groups/' + str(i))
    item['exact_source_span'] = span(start, end)
    item['enclosing_source_groups'] = parents
    item['literal_source_commands'] = [line for line in group['source_excerpt'].splitlines()
                                      if re.match(r'\\(?:draw|fill|node|path|coordinate|mathord|mathrel|unsure|deleted|inserted|overset|raisebox)\b', line)]
    item['declared_crop_metadata_refs'] = [ref('crop_manifest.json', '/' + str(k)) for k, c in enumerate(crops) if c['path'] == group['crop']]
    restored = {k: (text[start:end] if k == 'source_excerpt' else item[k]) for k in group}
    assert json.dumps(restored, ensure_ascii=False) == json.dumps(group, ensure_ascii=False)
    groups.append(item)

partition = []
cursor = 0
for i, part in enumerate(source_map['complete_source_partition']):
    assert part['start'] == cursor and part['text'] == text[part['start']:part['end']]
    cursor = part['end']
    out = {k: copy.deepcopy(v) for k, v in part.items() if k != 'text'}
    out['raw_ref'] = ref('source_map.json', '/complete_source_partition/' + str(i))
    out['exact_source_span'] = span(part['start'], part['end'])
    if part['kind'] == 'ordinary source':
        out['exact_text'] = part['text']
    partition.append(out)
assert cursor == len(text)
assert ''.join(text[p['start']:p['end']] for p in partition) == text

# Literal qualifier/source-state macros, with exact enclosing macro and group
# spans. Comment text is excluded only from this token listing and stays in the
# complete source partition.
comment = [False] * len(text)
for m in re.finditer(r'(?m)(?<!\\)%[^\n]*', text):
    comment[m.start():m.end()] = [True] * (m.end()-m.start())


def argument_end(opening):
    depth = 0
    i = opening
    while i < len(text):
        if comment[i]:
            i += 1
            continue
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i+1
        i += 1
    raise AssertionError('unclosed macro source')


tokens = []
for m in re.finditer(r'\\(unsure|deleted|inserted|uline|uuline|overline|phantom)\s*\{', text):
    if comment[m.start()]:
        continue
    opening = m.end()-1
    end = argument_end(opening)
    tokens.append({'macro': m.group(1), 'start': m.start(), 'end': end, 'exact_source_span': span(m.start(), end), 'literal': text[m.start():end]})
for token in tokens:
    token['enclosing_macro_spans'] = [
        {'macro': other['macro'], 'start': other['start'], 'end': other['end']}
        for other in tokens if other['start'] < token['start'] and token['end'] <= other['end']]
    token['enclosing_group_ids'] = [g['id'] for g in groups if g['source_char_start'] <= token['start'] and token['end'] <= g['source_char_end_exclusive']]

# Thirty-seven individually mapped groups, and the two exact lower diagram
# label tokens. Catalogue ordinals 15/16 do not pretend A supplied local ids.
sigmas = []
for n in range(1, 40):
    ident = 'A026-S%02d' % n
    matching = [g for g in groups if g['id'] == ident]
    if matching:
        g = matching[0]
        sigmas.append({'occurrence_ordinal': n, 'source_supplied_group_id': ident, 'group_ref': g['raw_ref'],
                       'complete_candidates': g['complete_candidates'], 'evidence': g['evidence'],
                       'hand': g['hand'], 'role': g['role'], 'owns': g['owns'],
                       'exact_source_span': g['exact_source_span'], 'literal_source_commands': g['literal_source_commands'],
                       'enclosing_source_groups': g['enclosing_source_groups']})
    else:
        assert n in (15, 16)
        g = next(g for g in groups if g['id'] == 'A026-D01')
        needle = '\\Sigma^{-}' if n == 15 else '\\Sigma^{+}'
        hits = [m.start() for m in re.finditer(re.escape(needle), text[g['source_char_start']:g['source_char_end_exclusive']])]
        assert len(hits) == 1
        start = g['source_char_start'] + hits[0]
        sigmas.append({'occurrence_ordinal': n, 'source_supplied_group_id': None, 'enclosing_source_group': 'A026-D01',
                       'group_ref': g['raw_ref'], 'exact_label_token': needle, 'exact_source_span': span(start, start+len(needle)),
                       'local_scope_note': 'A supplies this generic Sigma label in the complete diagram node. The diagram complete candidates and hand/role scopes remain at the cited raw group; no independent literal head/body/roof description or local id is supplied for this label.'})
assert len(sigmas) == 39

manifest = {'source_only': True, 'scope': 'A-only frozen source catalogue. No ink interpretation or root decision.',
            'source_files': {n: {'path': 'out/readers/026/A/' + n, 'bytes': len(b), 'sha256': sha(b)} for n, b in raw.items()},
            'reference_inverse': 'Each ordered field reference dereferences its frozen file and JSON pointer; fields are reassembled in recorded key order. Group excerpts are recovered by exact character slices of the frozen TeX. Both maps are checked on every listed record. Raw referenced files remain required inputs.',
            'report_top_level_key_order': list(report),
            'report_nonarray_refs': {k: ref('report.json', '/' + esc(k)) for k,v in report.items() if not isinstance(v,list)},
            'source_map_top_level_refs': {k: ref('source_map.json', '/' + esc(k)) for k in source_map},
            'counts': {'report_array_records': len(records), 'local_groups': len(groups), 'source_partition_pieces': len(partition),
                       'sigma_occurrences': len(sigmas), 'qualifier_state_macro_occurrences': len(tokens), 'crop_metadata_records': len(crops)},
            'diagram_hand_scope': {'raw_parent_inventory': ref('report.json', '/inventory/15'),
                                   'raw_group_hand': ref('source_map.json', '/local_groups/17/hand'),
                                   'candidate_specific_hand': ref('source_map.json', '/local_groups/17/complete_candidates'),
                                   'scope_note': 'The parent his hand and every separate_point undetermined hand candidate scope are retained independently; neither field overwrites the other.'}}
write('manifest_v01', manifest)
write('report_records_v01', records)
write('groups_v01', groups)
write('partition_v01', partition)
write('sigma_v01', sigmas)
write('qualifiers_v01', tokens)
write('crops_v01', {'raw_ref': ref('crop_manifest.json'), 'records': crops})
write('replay_v01', {'source_only': True, 'all_ordered_report_record_refs_exact': True, 'all_group_source_spans_exact': True,
                     'all_group_roundtrips_exact_in_key_order': True, 'partition_reconstructs_complete_TeX_bytes': ''.join(text[p['start']:p['end']] for p in partition).encode() == raw['reading.tex'],
                     'all_39_sigma_occurrences_separate': len(sigmas)==39,
                     'input_files_unchanged': all((ROOT/n).read_bytes()==b for n,b in raw.items()),
                     'images_read': 0, 'reader_B_or_C_files_read': 0, 'root_decisions': 0})
print(json.dumps(manifest['counts'], indent=2))
