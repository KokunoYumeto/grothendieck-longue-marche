#!/usr/bin/env python3
"""Bounded scan025 source-only QA inventory. Reads no image bytes.

The inventory records original file/JSON-pointer identities and literal source
offsets. It makes no selection, physical-count, image, or metric decision.
"""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out/checks'
DEC = json.JSONDecoder()


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode('utf-8')).hexdigest()


def json_value_digest(value):
    return digest(json.dumps(value, ensure_ascii=False, separators=(',', ':')))


def escape(part):
    return str(part).replace('~', '~0').replace('/', '~1')


def json_spans(text):
    """Record exact original JSON-value lexical spans, preserving source bytes."""
    spans = {}

    def ws(i):
        while i < len(text) and text[i].isspace():
            i += 1
        return i

    def scan(i, pointer):
        i = ws(i)
        start = i
        if text[i] == '{':
            i = ws(i + 1)
            if text[i] != '}':
                while True:
                    key, i = DEC.raw_decode(text, i)
                    i = ws(i)
                    assert text[i] == ':'
                    i = scan(i + 1, pointer + '/' + escape(key))
                    i = ws(i)
                    if text[i] == '}':
                        break
                    assert text[i] == ','
                    i = ws(i + 1)
            end = i + 1
        elif text[i] == '[':
            i = ws(i + 1)
            n = 0
            if text[i] != ']':
                while True:
                    i = scan(i, pointer + '/' + str(n))
                    n += 1
                    i = ws(i)
                    if text[i] == ']':
                        break
                    assert text[i] == ','
                    i = ws(i + 1)
            end = i + 1
        else:
            _, end = DEC.raw_decode(text, i)
        spans[pointer] = (start, end)
        return end

    end = scan(0, '')
    assert not text[end:].strip()
    return spans


def text_ref(path, text, start, end):
    return {
        'path': path, 'char_start': start, 'char_end_exclusive': end,
        'utf8_byte_start': len(text[:start].encode('utf-8')),
        'utf8_byte_end_exclusive': len(text[:end].encode('utf-8')),
        'line_start': text.count('\n', 0, start) + 1,
        'line_end': text.count('\n', 0, max(start, end - 1)) + 1,
        'literal_sha256_utf8': digest(text[start:end]),
    }


def json_ref(path, text, spans, pointer):
    start, end = spans[pointer]
    return dict(text_ref(path, text, start, end), json_pointer=pointer)


def walk(value, pointer=''):
    yield pointer, value
    if isinstance(value, dict):
        for k, v in value.items():
            yield from walk(v, pointer + '/' + escape(k))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from walk(v, pointer + '/' + str(i))


def reported_offsets(value):
    for a, b in [('start_char', 'end_char_exclusive'), ('char_start', 'char_end')]:
        if a in value and b in value:
            return (value[a], value[b])
    for k in ['char_offsets', 'reader_source_char_offsets', 'reader_source_offsets']:
        if k in value:
            return tuple(value[k])
    return None


def reported_bytes(value):
    if 'start_utf8_byte' in value and 'end_utf8_byte_exclusive' in value:
        return (value['start_utf8_byte'], value['end_utf8_byte_exclusive'])
    for k in ['byte_offsets_utf8', 'reader_source_byte_offsets_utf8']:
        if k in value:
            return tuple(value[k])
    return None


def literal_field(value):
    for k in ['literal_source', 'reader_source_excerpt', 'reader_source_quote']:
        if k in value:
            return k, value[k]
    return None, None


def drawing_commands(text):
    visible = []
    for line in text.splitlines(keepends=True):
        comment = len(line)
        for i, ch in enumerate(line):
            if ch != '%':
                continue
            backslashes = 0
            k = i - 1
            while k >= 0 and line[k] == '\\':
                backslashes += 1
                k -= 1
            if backslashes % 2 == 0:
                comment = i
                break
        visible.append(line[:comment] + ''.join('\n' if ch == '\n' else ' ' for ch in line[comment:]))
    visible = ''.join(visible)
    commands = []
    for m in re.finditer(r'\\(draw|filldraw|fill|path|node|coordinate|useasboundingbox)\b', visible):
        depth = 0
        i = m.start()
        while i < len(text):
            ch = visible[i]
            if ch == '\\' and i + 1 < len(visible) and visible[i + 1] in '{}%;':
                i += 2
                continue
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
            elif ch == ';' and depth == 0:
                commands.append((m.group(1), m.start(), i + 1))
                break
            i += 1
        else:
            raise ValueError('No semicolon for command at ' + str(m.start()))
    return commands


def main():
    bindings = {}
    rows = []
    groups = []
    text_spans = []
    commands = []
    checks = []
    findings = []
    counts = {}
    qualification_metadata = []
    readers = {}
    frozen = json.loads((BASE / 'out/checks/scan025_reader_fingerprints.json').read_text())['files']

    def load_text(path):
        raw = (BASE / path).read_bytes()
        text = raw.decode('utf-8')
        bindings[path] = {'sha256_utf8': digest(raw), 'bytes': len(raw), 'chars': len(text)}
        if path in frozen:
            ok = digest(raw) == frozen[path]
            checks.append({'check': 'frozen-file-hash', 'path': path, 'ok': ok})
            if not ok:
                findings.append({'kind': 'frozen_file_hash_mismatch', 'path': path})
        return text

    def add_row(path, raw, spans, section, i, value, reader=None):
        pointer = '/' + escape(section) + '/' + str(i) if section else '/' + str(i)
        entry = {
            'reader': reader, 'section': section or 'packet_inventory', 'ordinal0': i,
            'source_ref': json_ref(path, raw, spans, pointer),
            'decoded_value_sha256': json_value_digest(value),
        }
        if isinstance(value, dict):
            entry['identity'] = value.get('id', value.get('element', value.get('source_row_id', value.get('location', pointer))))
            for field in ['location', 'position', 'first_words_or_objects']:
                if field in value:
                    entry[field] = value[field]
            entry['original_field_names'] = list(value)
            entry['field_roles'] = {k: ('witness_C' if k == 'C' else 'witness_H' if k == 'H' else 'own_reader_reading' if k in ['reading','reader_complete_primary','reader_complete_alternatives','complete_alternatives','reader_complete_candidates','reader_source_qualification'] else 'own_reader_evidence' if k == 'evidence' else 'original_metadata') for k in value}
            for field, item in value.items():
                if re.search(r'(hand|scope|qualif|candidate|alternative|ownership|^owns$|^role|local_decisions|local_parts)', field):
                    p = pointer + '/' + escape(field)
                    qualification_metadata.append({'source_ref': json_ref(path, raw, spans, p), 'value': item})
        else:
            entry['identity'] = pointer
        rows.append(entry)
        return entry

    for reader in 'ABC':
        folder = 'out/readers/025/' + reader
        tex_path = folder + '/reading.tex'
        tex = load_text(tex_path)
        load_text(folder + '/reading.md')
        report_path = folder + '/report.json'
        map_path = folder + '/source_map.json'
        report_raw = load_text(report_path)
        map_raw = load_text(map_path)
        report = json.loads(report_raw)
        source_map = json.loads(map_raw)
        report_lex = json_spans(report_raw)
        map_lex = json_spans(map_raw)
        readers[reader] = {'report': report, 'source_map': source_map, 'tex': tex}
        counts[reader] = {k: len(report.get(k, [])) for k in ['differences', 'doubts', 'inventory', 'notation']}
        counts[reader]['groups'] = len(source_map['groups'])
        counts[reader]['text_spans'] = len(source_map['text_spans'])
        ckey = 'C_doubt_rows' if 'C_doubt_rows' in report else 'original_C_doubts'
        counts[reader]['original_C_rows'] = len(report[ckey])
        for section in ['differences', 'doubts', 'inventory', 'notation', ckey, 'slips_context']:
            for i, value in enumerate(report.get(section, [])):
                add_row(report_path, report_raw, report_lex, section, i, value, reader)

        group_intervals = []
        for section, output in [('groups', groups), ('text_spans', text_spans)]:
            for i, value in enumerate(source_map[section]):
                entry = add_row(map_path, map_raw, map_lex, section, i, value, reader)
                start, end = reported_offsets(value)
                literal = value['literal_source']
                ok = tex[start:end] == literal
                b = reported_bytes(value)
                byte_ok = b is None or tex.encode('utf-8')[b[0]:b[1]].decode('utf-8') == literal
                actual_bytes = (len(tex[:start].encode('utf-8')), len(tex[:end].encode('utf-8')))
                byte_boundaries_ok = b is None or b == actual_bytes
                output.append({
                    'reader': reader, 'id': value['id'], 'map_row_ref': entry['source_ref'],
                    'tex_ref': text_ref(tex_path, tex, start, end),
                    'literal_match': ok, 'utf8_literal_match': byte_ok,
                    'utf8_boundary_match': byte_boundaries_ok,
                    'preceding_character': tex[start-1:start] if start else '',
                    'following_character': tex[end:end+1],
                    'declared_offset_values': {k: value[k] for k in ['start_char','end_char_exclusive','start_utf8_byte','end_utf8_byte_exclusive','char_offsets','byte_offsets_utf8','start_line','end_line','line_start','line_end','line_range'] if k in value},
                    'ownership': value.get('ownership', value.get('owns')),
                    'original_metadata_fields': list(value),
                })
                checks.append({'check': 'map-literal-offsets', 'path': map_path, 'json_pointer': entry['source_ref']['json_pointer'], 'ok': ok and byte_ok and byte_boundaries_ok})
                if not(ok and byte_ok and byte_boundaries_ok):
                    findings.append({'kind': 'map_literal_offset_mismatch', 'path': map_path, 'id': value['id'], 'char_match': ok, 'byte_match': byte_ok, 'byte_boundaries_match': byte_boundaries_ok})
                if section == 'groups':
                    group_intervals.append((start, end, value['id']))
                    for j, component in enumerate(value.get('components', [])):
                        present = component in literal
                        checks.append({'check': 'component-in-group-literal', 'path': map_path, 'json_pointer': f'/groups/{i}/components/{j}', 'ok': present})
                        if not present:
                            findings.append({'kind': 'component_missing_from_group_literal', 'path': map_path, 'id': value['id'], 'component_index': j})

        # Every marker's exact identity is compared with the map, with no source rewrite.
        if reader in 'AB':
            starts = re.findall(r'(?m)% BEGIN ([ABC]025-[A-Z]\d+)[ \t]*$', tex)
            ends = re.findall(r'(?m)% END ([ABC]025-[A-Z]\d+)[ \t]*$', tex)
        else:
            starts = re.findall(r'(?m)^% ([ABC]025-[A-Z]\d+) begin\s*$', tex)
            ends = re.findall(r'(?m)^% ([ABC]025-[A-Z]\d+) end\s*$', tex)
        expected = [g['id'] for g in source_map['groups']]
        marker_ok = sorted(starts) == sorted(expected) and sorted(ends) == sorted(expected)
        checks.append({'check': 'all-group-marker-identities', 'path': tex_path, 'ok': marker_ok, 'begin_ids': starts, 'end_ids': ends, 'map_ids': expected, 'ordering_scope': 'Source order is retained literally. Map array order is retained separately; nested markers close within their parent.'})
        if not marker_ok:
            findings.append({'kind': 'group_marker_map_identity_or_order_mismatch', 'reader': reader, 'begins': starts, 'ends': ends, 'expected': expected})

        for n, (command, start, end) in enumerate(drawing_commands(tex)):
            owners = [gid for a,b,gid in group_intervals if a <= start and end <= b]
            commands.append({'reader': reader, 'ordinal0': n, 'command': command, 'source_ref': text_ref(tex_path, tex, start, end), 'group_ids': owners})
        counts[reader]['literal_drawing_command_rows'] = sum(x['reader'] == reader for x in commands)
        counts[reader]['drawing_commands_outside_declared_groups'] = sum(x['reader'] == reader and not x['group_ids'] for x in commands)

        # Inspect every stored reader span in both original JSON documents.
        for path, obj in [(report_path, report), (map_path, source_map)]:
            for pointer, value in walk(obj):
                if not isinstance(value, dict):
                    continue
                offsets = reported_offsets(value)
                key, literal = literal_field(value)
                if offsets is None or literal is None:
                    continue
                a,b = offsets
                use_utf8 = reader == 'B' and path == report_path and 'reader_source_offsets' in value
                ok = (tex.encode('utf-8')[a:b].decode('utf-8') if use_utf8 else tex[a:b]) == literal
                checks.append({'check': 'stored-reader-span', 'path': path, 'json_pointer': pointer, 'literal_field': key, 'offset_unit': 'UTF-8 bytes' if use_utf8 else 'Unicode characters', 'ok': ok})
                if not ok:
                    findings.append({'kind': 'stored_reader_span_mismatch', 'path': path, 'json_pointer': pointer, 'literal_field': key})

    # Packet rows keep their separate original section identities.
    c_doubts_path = 'packets/025/C_doubts.txt'
    c_doubts = load_text(c_doubts_path)
    packet_inventory_path = 'packets/025/C_inventory.json'
    inventory_raw = load_text(packet_inventory_path)
    inventory = json.loads(inventory_raw)
    inventory_lex = json_spans(inventory_raw)
    for i, value in enumerate(inventory):
        add_row(packet_inventory_path, inventory_raw, inventory_lex, '', i, value)
    for name in ['C.tex', 'H.tex', 'metadata.json', 'C_notes.txt']:
        load_text('packets/025/' + name)
    load_text('out/readers/025/C/unresolved_targets.md')

    catalog_path = 'out/checks/scan025_C_doubt_catalog.json'
    catalog_raw = load_text(catalog_path)
    catalog = json.loads(catalog_raw)
    catalog_lex = json_spans(catalog_raw)
    packet_rows = []
    for section in ['canonical_doubt_rows', 'other_source_rows']:
        for i, row in enumerate(catalog[section]):
            a,b = row['char_start'], row['char_end']
            ok = c_doubts[a:b] == row['literal']
            packet_rows.append({'section': section, 'identity': row.get('source_id', row.get('section') + '@line' + str(row['line']) if row.get('section') else str(i)), 'catalog_ref': json_ref(catalog_path, catalog_raw, catalog_lex, f'/{section}/{i}'), 'source_ref': text_ref(c_doubts_path,c_doubts,a,b), 'literal_match': ok})
            checks.append({'check': 'packet-row-catalog-span', 'section': section, 'ordinal0': i, 'ok': ok})
            if not ok:
                findings.append({'kind': 'packet_row_catalog_span_mismatch','section':section,'ordinal0':i})
    canonical_literals = {row['source_id']:row['literal'] for row in catalog['canonical_doubt_rows']}
    for reader, parts in readers.items():
        report=parts['report']
        crows=report.get('C_doubt_rows',report.get('original_C_doubts'))
        for row in crows:
            identity=row.get('id',row.get('source_row_id'))
            literal=next(row[k] for k in ['raw_source_row','literal_source_row','original_row_literal'] if k in row)
            ok=canonical_literals.get(identity)==literal
            checks.append({'check':'own-reader-original-C-row-identity-and-literal','reader':reader,'id':identity,'ok':ok})
            if not ok:
                findings.append({'kind':'reader_original_C_row_mismatch','reader':reader,'id':identity})
    for name in ['scan025_H_marker_catalog.json','scan025_S_scope.json','scan025_reader_fingerprints.json','scan025_pairwise_diff_manifest.json']:
        load_text('out/checks/'+name)

    result = {
        'scan': 25, 'stage': 'independent original source coverage inventory',
        'scope': 'Frozen reader text/JSON and scan025 packet/catalog text only. No image byte read, rendering, compilation, source mutation, ink selection, physical count or metric assertion.',
        'offset_convention': 'Zero-based Unicode character and UTF-8 byte offsets; end exclusive; one-based lines. Exact original JSON-value lexical spans retain original spelling, escape sequences and whitespace.',
        'source_bindings': bindings, 'source_counts': counts,
        'packet_counts': {'actual_C_doubt_rows':len(catalog['canonical_doubt_rows']),'other_C_table_rows':len(catalog['other_source_rows']),'C_inventory':len(inventory)},
        'original_row_inventory': rows,
        'group_span_inventory': groups,
        'text_span_inventory': text_spans,
        'literal_drawing_command_inventory': commands,
        'qualification_and_hand_metadata': qualification_metadata,
        'packet_table_row_inventory': packet_rows,
        'source_checks': checks, 'concrete_findings': findings,
        'projection_replay': {'status':'pending source025 stage1 handoff'},
    }
    output=OUT/'scan025_qa_sourcecoverage_inventory.json'
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    lines=['# Scan025 independent source coverage inventory','',
           'Source-only inventory; no source file was changed. All identities use their original file plus JSON pointer. Own-reader readings, witness C/H fields and any later selected fields retain their separate roles.','',
           '| Reader | Differences | Doubts | Inventory | Groups | Text spans | Literal drawing commands |','| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for r,c in counts.items():
        lines.append(f"| {r} | {c['differences']} | {c['doubts']} | {c['inventory']} | {c['groups']} | {c['text_spans']} | {c['literal_drawing_command_rows']} |")
    lines += ['',f"The source packet has {len(catalog['canonical_doubt_rows'])} actual C doubt rows, {len(catalog['other_source_rows'])} separately scoped notation/slip rows, and {len(inventory)} inventory rows.",
              '',f"Recorded {len(rows)} original row references, {len(groups)} complete group references, {len(text_spans)} text-span references, {len(commands)} literal drawing-command references, and {len(qualification_metadata)} original qualification/hand/scope metadata fields.",
              '',f"Source checks: {len(checks)}; failed checks: {sum(not c['ok'] for c in checks)}.",
              '', '## Concrete findings', '']
    if findings:
        lines += ['- '+json.dumps(x,ensure_ascii=False) for x in findings]
    else:
        lines += ['No exact source-reference or literal-offset defect was found in this bounded original-source inventory pass.']
    lines += ['', '## Required preservation points', '',
              '- Keep original C rows R01–R08 at their actual scope. A local_decisions and C local_parts remain attached to their original row identities.',
              '- Keep A inventory scope_note, B inventory local_hand_scopes, and C inventory compound hand values. Complete group metadata and candidate-specific hand scopes remain at their original source pointers.',
              '- Keep each complete graphical group, every node/word command, every drawing command, and adjoining text at the original source offset. Group and text-span boundaries are recorded literally.',
              '- Preserve source-silent own-reader material from complete TeX. C’s live et candidate remains in reader C’s source role; B’s que-plus-point group remains in reader B’s source role.',
              '- H marker catalog contains no uncertainty macro; supplied letters and the two note objects retain their local source spans. All later local marked_in_H choices belong to root review.',
              '- S_scope records seven source rows and an empty direct_page_25_reading_rows array; its exact scope statement is bound as original source metadata.',
              '', 'Stage1 source-pool/projection replay remains pending source025 handoff.']
    (OUT/'scan025_qa_sourcecoverage_inventory.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'inventory_path':str(output.relative_to(BASE)), 'sha256':digest(output.read_bytes()),'counts':counts,'original_rows':len(rows),'commands':len(commands),'metadata_fields':len(qualification_metadata),'checks':len(checks),'findings':findings},ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
