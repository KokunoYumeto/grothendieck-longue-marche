"""Source-only index of the explicitly released B return and supplied witnesses.

Reads only the named text files below. No image access, rendering, coordinate
calculation, interpretation, selection, public counting, or source mutation.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/94548b74fbe0')
OUT = ROOT / 'out/checks'
B = 'out/readers/023/B/'
TEX = B + 'reading.tex'
REPORT = B + 'report.json'
MAP = B + 'source_map.json'
FILES = [
    'packets/023/C.tex', 'packets/023/H.tex', 'packets/023/C_doubts.txt',
    'packets/023/C_notes.txt', 'packets/023/C_inventory.json', 'packets/023/notation.md',
    'out/checks/scan023_C_doubt_catalog.json',
    'out/checks/scan023_H_marker_catalog.json', 'out/checks/scan023_S_scope.json',
] + [B + n for n in ['reading.tex', 'report.json', 'reading.md', 'source_map.json',
                     'source_check.json', 'view_audit.json', 'crop_plan.json',
                     'freeze_manifest.json']]
texts = {p: (ROOT / p).read_text(encoding='utf-8') for p in FILES}
data = {p: json.loads(t) for p, t in texts.items() if p.endswith('.json')}
hashes = {p: hashlib.sha256(t.encode('utf-8')).hexdigest() for p, t in texts.items()}
tex = texts[TEX]
report = data[REPORT]
source_map = data[MAP]
errors = []


def ref(path, start=0, end=None, literal=True):
    t = texts[path]
    if end is None:
        end = len(t)
    r = dict(path=path, sha256_utf8=hashes[path], char_start_zero_based=start,
             char_end_exclusive=end, utf8_byte_start=len(t[:start].encode('utf-8')),
             utf8_byte_end_exclusive=len(t[:end].encode('utf-8')),
             line_start_one_based=t.count('\n', 0, start) + 1,
             line_end_one_based=t.count('\n', 0, max(start, end - 1)) + 1)
    if literal:
        r['literal'] = t[start:end]
    return r


def json_spans(s):
    """Index JSON syntax spans, retaining exact original whitespace and values."""
    spans = {}
    decoder = json.JSONDecoder()

    def ws(i):
        while i < len(s) and s[i] in ' \t\r\n':
            i += 1
        return i

    def esc(k):
        return str(k).replace('~', '~0').replace('/', '~1')

    def value(i, pointer):
        i = ws(i)
        start = i
        if s[i] == '{':
            i = ws(i + 1)
            while s[i] != '}':
                k, j = decoder.raw_decode(s, i)
                i = ws(j)
                assert s[i] == ':'
                i = ws(value(i + 1, pointer + '/' + esc(k)))
                if s[i] == ',':
                    i = ws(i + 1)
                else:
                    assert s[i] == '}'
            i += 1
        elif s[i] == '[':
            i = ws(i + 1)
            n = 0
            while s[i] != ']':
                i = ws(value(i, pointer + '/' + str(n)))
                n += 1
                if s[i] == ',':
                    i = ws(i + 1)
                else:
                    assert s[i] == ']'
            i += 1
        else:
            _, i = decoder.raw_decode(s, i)
        spans[pointer] = (start, i)
        return i

    value(0, '')
    return spans


jspan = {p: json_spans(texts[p]) for p in data}


def jref(path, pointer, literal=False):
    start, end = jspan[path][pointer]
    r = ref(path, start, end, literal)
    r['json_pointer'] = pointer
    return r


def exact(s, path=TEX, within=None, occurrence=None):
    t = texts[path]
    low, high = (0, len(t)) if within is None else within
    positions = [m.start() + low for m in re.finditer(re.escape(s), t[low:high])]
    if occurrence is None:
        assert len(positions) == 1, (path, s, positions)
        start = positions[0]
    else:
        start = positions[occurrence]
    return ref(path, start, start + len(s))


def extent(first, last, path=TEX, first_occurrence=0, last_after=True):
    t = texts[path]
    starts = [m.start() for m in re.finditer(re.escape(first), t)]
    start = starts[first_occurrence]
    end = t.index(last, start + len(first) if last_after else start) + len(last)
    return ref(path, start, end)


groups = {}
for index, g in enumerate(source_map['groups']):
    span = g['source_span']
    s, e = span['char_start_zero_based'], span['char_end_exclusive']
    source_ref = ref(TEX, s, e)
    if g.get('complete_exact_source') is not None and g['complete_exact_source'] != tex[s:e]:
        errors.append({'type': 'map_literal_mismatch', 'group': g['id']})
    groups[g['id']] = dict(id=g['id'], raw=g, map_ref=jref(MAP, f'/groups/{index}'),
                           tex_ref=source_ref, source_selected=False)


def gr(name):
    return groups[name]['tex_ref']


named = {
    'opening': extent('Soit maintenant ', '=\\varnothing$.'),
    'upper_paragraph': extent('En effet, ', '% END B023-S01\n$,'),
    'continued_assertion': extent('je dis que si ', 'en fait\n'),
    'first_display': extent('\\[\n% BEGIN B023-G05', '\\]\n'),
    'margin': extent('\\reversemarginpar\\margin{\\begin{tikzpicture}', '\\normalmarginpar'),
    'upper_argument': extent('\\unsure{ce|} qui', 'Cela revient au'),
    'lemma_intro': extent('\\uline{Lemme}', 'tels que\n'),
    'lemma_condition': extent('\\[\n\\alpha\n', '\\]\n'),
    'lemma_hypothesis': extent('Soit $i\\in I\\setminus K$', '$, alors\n'),
    'lemma_endpoint': extent('$E_i\\subset\n% BEGIN B023-S08', '$.'),
    'unfinished': extent('Cela \\deleted{signifie que}', ' du\n'),
    'corollary_heading': extent('\\uline{Corollaire}', '% END B023-G08\n$'),
    'corollary_statement': gr('B023-G11'),
    'last_sentence': exact('Immédiat par récurrence sur $\\operatorname{card} K\\geq 0$.'),
    'archive_comment': exact('% archive sheet number: 22\n'),
}


def inside(s, scope, occurrence=None):
    v = named[scope]
    return exact(s, within=(v['char_start_zero_based'], v['char_end_exclusive']), occurrence=occurrence)


inventory_refs = {
    1: [named['opening']], 2: [gr('B023-G01')], 3: [named['upper_paragraph']],
    4: [exact('\\deleted{contient}')], 5: [exact('\\inserted{rencontre}')],
    6: [gr('B023-G02')], 7: [gr('B023-S01')], 8: [exact('\\deleted{\\unsure{donc si}}')],
    9: [named['continued_assertion']], 10: [gr('B023-G04')], 11: [gr('B023-M01')],
    12: [named['first_display']], 13: [gr('B023-G05')], 14: [named['margin']],
    15: [exact('\\deleted{\\illegible{1}}')], 16: [named['upper_argument']],
    17: [exact('\\uline{Lemme}')], 18: [named['lemma_intro']],
    19: [exact('\\deleted{tel que les}')], 20: [exact('\\deleted{et}')],
    21: [gr('B023-M02')], 22: [named['lemma_condition']], 23: [gr('B023-G06')],
    24: [gr('B023-S05')], 25: [gr('B023-S06')], 26: [named['lemma_hypothesis']],
    27: [gr('B023-S07')], 28: [gr('B023-G07')], 29: [gr('B023-G07')],
    30: [gr('B023-G07')], 31: [named['lemma_endpoint']], 32: [gr('B023-S08')],
    33: [named['unfinished']], 34: [exact('\\deleted{signifie que}')],
    35: [gr('B023-M03')], 36: [gr('B023-M04')], 37: [named['corollary_heading']],
    38: [gr('B023-G08')], 39: [gr('B023-G11')], 40: [gr('B023-G10')],
    41: [gr('B023-P01')], 42: [gr('B023-G09')], 43: [gr('B023-S10')],
    44: [gr('B023-S11')], 45: [named['last_sentence']], 46: [named['archive_comment']],
}
inventory = []
for i, raw in enumerate(report['inventory']):
    n = int(raw['element'].split('-I')[1])
    inventory.append(dict(id=raw['element'], raw=raw, source_ref=jref(REPORT, f'/inventory/{i}'),
                          complete_tex_refs=inventory_refs[n], selected_transcribed_status=None))

# These are complete local witness source spans, never substituted report values.
CW = 'packets/023/C.tex'
HW = 'packets/023/H.tex'
cscopes = {
    'opening': extent('Soit maintenant ', 'en fait', CW),
    'display': extent('\\[\nE_\\beta', '\\]\n', CW),
    'margin': extent('\\reversemarginpar', '\\normalmarginpar', CW),
    'upper': extent('ce qui ', '\\unsure{au}', CW),
    'lemma_intro': extent('\\uline{Lemme}', '\\unsure{tels} que', CW),
    'lemma_condition': extent('\\[\n\\alpha', '\\]\n', CW),
    'lemma_conclusion': extent('Soit $i\\in', '$.', CW),
    'unfinished': extent('Cela \\deleted', '\\unsure{du|des|sens}', CW),
    'corollary_heading': extent('\\uline{Corollaire}', '$,', CW),
    'corollary_statement': extent('\\noindent\\begin{tabular}', '\\end{tabular}', CW),
    'last': exact('Immédiat par récurrence sur $\\operatorname{card} K\\geq 0$.', CW),
}
hscopes = {
    'opening': extent('Soit maintenant ', 'on a en fait', HW),
    'display': extent('\\[\n  E_{\\beta}\\subset\\bigcup', '\\]\n', HW),
    'margin': exact("\\marginal{c'est trivial, du fait que les $E_{i}$ ($i\\in I$) sont disjoints}", HW),
    'upper': extent("qui prouve l'assertion", 'Cela résulte du', HW),
    'lemma_intro': extent('\\emph{Lemme}', 'tels que', HW),
    'lemma_condition': extent('\\[\n  \\alpha', '\\]\n', HW),
    'lemma_conclusion': extent('Soit $i\\in', '$.', HW),
    'unfinished': extent('Cela \\struck', '\\note{la phrase reste inachevée}', HW),
    'corollary_heading': extent('\\emph{Corollaire}', ')_{\\alpha\\in K}$,', HW),
    'corollary_statement': extent('la partition ', '\\note{la réunion est écrite avec le signe de réunion disjointe}', HW),
    'last': exact('Immédiat par récurrence sur $\\operatorname{card} K\\geqslant0$.', HW),
}
scope_by_difference = {}
for ns, scope in [([1,2,3,4,5,6,7], 'opening'), ([8], 'display'),
                  ([9,10,11], 'margin'), ([12,13,14,15], 'upper'),
                  ([16,17,36], 'lemma_intro'), ([18,19,20], 'lemma_condition'),
                  ([21,22,23,24], 'lemma_conclusion'), ([25,26,27], 'unfinished'),
                  ([28,29,30,37], 'corollary_heading'), ([31,32,33,34,35], 'corollary_statement')]:
    for n in ns:
        scope_by_difference[n] = scope

differences = []
for i, raw in enumerate(report['differences']):
    n = int(raw['id'].split('-D')[1])
    refs = [gr(raw['source_group'])] if raw.get('source_group') else []
    anchor = raw.get('reading_tex_anchor')
    if anchor:
        if n == 11:
            refs.append(inside(anchor, 'margin'))
        elif n == 23:
            refs.append(exact('\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (441,1621) {\\rlap{$\\exists\\alpha\\in K$ tel que}\\phantom{\\inserted{$\\exists\\alpha\\in K$ tel que}}};'))
        else:
            refs.append(exact(anchor))
    if n in [25,26]:
        refs.append(named['unfinished'])
    if n == 2:
        refs.append(gr('B023-G04'))
    scope = scope_by_difference[n]
    differences.append(dict(id=raw['id'], raw=raw, source_ref=jref(REPORT, f'/differences/{i}'),
                            own_tex_refs=refs,
                            actual_witness_contexts={'C': cscopes[scope], 'H': hscopes[scope]},
                            witness_context_note='Exact source context only. Raw reported C/H values are retained separately; context supplies no missing reading, local marker flag, selection or physical count.',
                            source_selected=False))
by_diff = {d['id']: d for d in differences}
doubts = [dict(id=r['id'], raw=r, source_ref=jref(REPORT, f'/doubts/{i}'),
               own_tex_refs=by_diff[r['id']]['own_tex_refs'], source_selected=False)
          for i, r in enumerate(report['doubts'])]

notation_refs = {
    'S01': [gr('B023-S01')], 'S02': [named['first_display']], 'S03': [named['upper_argument']],
    'S04': [named['lemma_intro']], 'S05': [gr('B023-S05')], 'S06': [gr('B023-S06')],
    'S07': [gr('B023-S07')], 'S08': [gr('B023-S08')], 'S09': [gr('B023-G08')],
    'S10': [gr('B023-S10')], 'S11': [gr('B023-S11')], 'N12': [gr('B023-P01')],
    'N13': [named['corollary_heading'], named['last_sentence']],
    'N14': [named['opening']], 'N15': [named['lemma_condition']],
    'N16': [gr('B023-G01'), gr('B023-G04')],
}
notation = [dict(id=r['id'], raw=r, source_ref=jref(REPORT, f'/notation/{i}'),
                 own_tex_refs=notation_refs[r['id']], source_selected=False)
            for i, r in enumerate(report['notation'])]

catalog_path = 'out/checks/scan023_C_doubt_catalog.json'
catalog = data[catalog_path]
original_rows = []
for i, raw in enumerate(report['C_doubt_source_rows']):
    c = next(x for x in catalog['rows'] if x['source_id'] == raw['id'])
    if raw['exact_source_row'] != c['literal']:
        errors.append({'type': 'actual_C_row_mismatch', 'id': raw['id']})
    original_rows.append(dict(id=raw['id'], canonical_parts=[p['part_id'] for p in c['source_parts']],
                              raw_B_return=raw, B_source_ref=jref(REPORT, f'/C_doubt_source_rows/{i}'),
                              canonical_root_catalog_row=c,
                              actual_C_source_ref=ref(c['source_path'], c['char_start'], c['char_end']),
                              selected_outcome=None))

# Exhaustive text partition: complete top-level marked groups and every interstice.
top = sorted([g for g in groups.values() if g['raw'].get('container') is None],
             key=lambda g: g['tex_ref']['char_start_zero_based'])
partition = []
cursor = 0
for g in top:
    s, e = g['tex_ref']['char_start_zero_based'], g['tex_ref']['char_end_exclusive']
    assert cursor <= s
    if cursor < s:
        partition.append(dict(id=f'B023-T{len(partition)+1:03}', kind='literal_interstice',
                              tex_ref=ref(TEX, cursor, s)))
    partition.append(dict(id=g['id'], kind='complete_graphical_group', tex_ref=g['tex_ref']))
    cursor = e
if cursor < len(tex):
    partition.append(dict(id=f'B023-T{len(partition)+1:03}', kind='literal_interstice',
                          tex_ref=ref(TEX, cursor, len(tex))))
assert ''.join(x['tex_ref']['literal'] for x in partition) == tex


def command_end(start):
    depth = 0
    i = start
    while i < len(tex):
        ch = tex[i]
        if ch == '%' and (i == 0 or tex[i-1] != '\\'):
            j = tex.find('\n', i)
            i = len(tex) if j < 0 else j + 1
            continue
        if ch in '{}':
            k = i - 1
            backslashes = 0
            while k >= 0 and tex[k] == '\\':
                backslashes += 1
                k -= 1
            if backslashes % 2 == 0:
                depth += 1 if ch == '{' else -1
        if ch == ';' and depth == 0:
            return i + 1
        i += 1
    raise AssertionError(('unterminated drawing command', start))


commands = []
for m in re.finditer(r'\\(draw|fill|path|coordinate|node)\b', tex):
    start, end = m.start(), command_end(m.start())
    # A command text in a %-comment is documentary; it remains in the source partition.
    line_start = tex.rfind('\n', 0, start) + 1
    if '%' in tex[line_start:start]:
        continue
    containers = [g for g in groups.values()
                  if g['tex_ref']['char_start_zero_based'] <= start and
                  end <= g['tex_ref']['char_end_exclusive']]
    containers.sort(key=lambda g: g['tex_ref']['char_end_exclusive'] - g['tex_ref']['char_start_zero_based'])
    commands.append(dict(id=f'B023-CMD{len(commands)+1:03}', command=m.group(1),
                         tex_ref=ref(TEX, start, end),
                         text_containment_groups=[g['id'] for g in containers],
                         narrowest_text_group=containers[0]['id'] if containers else None,
                         ownership_note='Text containment only; physical ownership follows the source comments and raw map.'))

component_records = []
for g in groups.values():
    for i, raw in enumerate(g['raw'].get('source_components', [])):
        start, end = raw['char_start_zero_based'], raw['char_end_exclusive']
        component_records.append(dict(owner=raw['owner'], enclosing_map_group=g['id'], raw=raw,
                                      source_map_ref=jref(MAP, g['map_ref']['json_pointer'] + f'/source_components/{i}'),
                                      tex_ref=ref(TEX, start, end)))

# Per-line reading.md entries retain distinct prose scopes and any scope wording.
md_entries = []
cursor = 0
for i, line in enumerate(texts[B+'reading.md'].splitlines(keepends=True)):
    if line.strip():
        md_entries.append(dict(line_one_based=i+1, source_ref=ref(B+'reading.md', cursor, cursor+len(line))))
    cursor += len(line)

freeze = data[B+'freeze_manifest.json']
released_names = {Path(p).name for p in FILES if p.startswith(B)}
freeze_text_entries = []
for i, entry in enumerate(freeze['files']):
    if entry.get('name') in released_names and entry.get('name') != 'freeze_manifest.json':
        path = B + entry['name']
        freeze_text_entries.append(dict(raw=entry, source_ref=jref(B+'freeze_manifest.json', f'/files/{i}'),
                                        observed_text_sha256_utf8=hashes[path],
                                        hash_matches=entry.get('sha256') == hashes[path]))

support = dict(
    scan='023', stage='B source extraction only', released_reader_scope=['B'],
    source_only=True, source_selected=False, main_adjudicated=False, main_approved=False,
    selected_counts=None, selected_record=None,
    method='Literal text preservation and source indexing. All coordinates and paths are copied source values; no coordinate or mathematical calculation, image inspection, rendering, or ink choice was performed.',
    process_deviation='During manifest-key inspection, one recorded PNG byte-count/hash entry was inadvertently printed from the text manifest. No image file was opened, statted, hashed or viewed. That entry is not reproduced or used in this extraction.',
    source_files=[dict(path=p, sha256_utf8=hashes[p], character_count=len(texts[p]),
                       utf8_byte_count=len(texts[p].encode('utf-8'))) for p in FILES],
    differences=differences, doubts=doubts, inventory=inventory, notation=notation,
    original_C_rows=original_rows, graphical_groups=list(groups.values()),
    graphical_component_records=component_records, exact_graphical_commands=commands,
    complete_TeX_partition=partition, named_complete_source_spans=named,
    reading_md_entries=md_entries,
    remaining_report_fields={k:dict(raw=v, source_ref=jref(REPORT, '/'+k))
                             for k,v in report.items() if k not in ['differences','doubts','inventory','notation','C_doubt_source_rows']},
    source_map_header={k:v for k,v in source_map.items() if k!='groups'},
    released_audit_files={n:dict(raw=data[B+n], source_ref=jref(B+n, ''))
                          for n in ['source_check.json','view_audit.json','crop_plan.json']},
    freeze_manifest_text_entries=freeze_text_entries,
    freeze_manifest_other_header={k:v for k,v in freeze.items() if k!='files'},
    report_silent_source_coverage='Every TeX byte occurs in complete_TeX_partition. Named scopes and all command bodies preserve report-silent words, marks, punctuation, local formula decorations and group declarations. No absent difference-list slot supplies a reading.',
    assembly_attention=[
        dict(id='B023-SRC01', subject='Repeated margin anchor', detail='The report D11 anchor also occurs in the upper paragraph. Its own_tex_refs here bind the occurrence within the complete marginal note.'),
        dict(id='B023-SRC02', subject='Repeated insertion annotation', detail='D23 is attached to the actual raised word node and complete G07. Invisible dimensional/state copies remain separately visible in the command table.'),
        dict(id='B023-SRC03', subject='Whole-region hand scope', detail='I09/I10 include G04 and its M01 child; the child reports undetermined hand. I39 G11 includes S10, whose I43 row separately reports local_uncertain_trace_hand as undetermined. Raw parent and child scopes remain unchanged.'),
        dict(id='B023-SRC04', subject='Reading.md wording and TeX scope', detail='The reading.md lemma-introduction line says cancelled et des; the exact TeX is \\deleted{et} des. Both raw sources are retained; no broader deletion scope has been chosen.'),
        dict(id='B023-SRC05', subject='Full recurring local roles', detail='S02/S03/S04 use ordinary math glyphs in actual TeX with local connection descriptions in notation. S07/S08/S09/S11 retain their own recorded head-role alternatives despite first-occurrence printing at S05. S06 and S10 retain their separate full sign/state candidates.'),
    ],
    source_verification=dict(errors=errors, source_map_literal_spans_match=not any(x['type']=='map_literal_mismatch' for x in errors),
                             complete_tex_partition_exact=True, actual_C_rows_match=not any(x['type']=='actual_C_row_mismatch' for x in errors),
                             released_text_freeze_hashes_match=all(x['hash_matches'] for x in freeze_text_entries),
                             no_public_count_calculation=True),
)

# Witness table sections are retained under their actual separate headings.
doubt_path = 'packets/023/C_doubts.txt'
dt = texts[doubt_path]
heads = list(re.finditer(r'^## .+$', dt, re.M))
sections = []
for i, m in enumerate(heads):
    end = heads[i+1].start() if i+1 < len(heads) else len(dt)
    rows = []
    at = m.start()
    for line in dt[m.start():end].splitlines(keepends=True):
        if line.startswith('| 23 |'):
            rows.append(ref(doubt_path, at, at+len(line.rstrip('\n'))))
        at += len(line)
    sections.append(dict(heading=m.group(), source_ref=ref(doubt_path, m.start(), end), rows=rows))
markers_path = 'out/checks/scan023_H_marker_catalog.json'
markers = []
for i, raw in enumerate(data[markers_path]['markers']):
    s, e = raw['char_start'], raw['char_end']
    assert texts[HW][s:e] == raw['literal']
    markers.append(dict(raw=raw, catalog_ref=jref(markers_path, f'/markers/{i}'), exact_H_source=ref(HW,s,e), selected_locus_attachment=None))
witness_support = dict(
    scan='023', source_only=True, selected_counts=None, source_selected=False,
    source_files=[dict(path=p, sha256_utf8=hashes[p]) for p in FILES if not p.startswith(B)],
    C_and_H_complete_text={p:ref(p) for p in [CW,HW]},
    C_and_H_named_contexts={'C':cscopes,'H':hscopes},
    actual_C_sections=sections,
    canonical_C_catalog=dict(raw=catalog, source_ref=jref(catalog_path,'')),
    C_notes=dict(source_ref=ref('packets/023/C_notes.txt'), scope='Entire supplied C_notes.txt'),
    C_inventory=[dict(raw=r, source_ref=jref('packets/023/C_inventory.json',f'/{i}')) for i,r in enumerate(data['packets/023/C_inventory.json'])],
    shared_notation=dict(source_ref=ref('packets/023/notation.md'), scope='Entire supplied Shared notation table; original row scopes retained. No local scan023 result is inferred from a prior-page row.'),
    H_markers=markers,
    H_apparatus=[exact('\\note{la phrase reste inachevée}',HW), exact('\\note{la réunion est écrite avec le signe de réunion disjointe}',HW)],
    S_scope=dict(raw=data['out/checks/scan023_S_scope.json'], source_ref=jref('out/checks/scan023_S_scope.json','')),
    source_scope_note='The 16 actual Doubtful readings rows preserve their 16 canonical -1 part identities. Notation and Slips kept as written retain separate supplied scopes. H markers and broad S scope are source metadata only.',
)

for name, value in [('scan023_B_source_coverage.json', support), ('scan023_witness_source_coverage.json', witness_support)]:
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

summary = {
    'B_source_coverage_path':'out/checks/scan023_B_source_coverage.json',
    'witness_source_coverage_path':'out/checks/scan023_witness_source_coverage.json',
    'B_source_coverage_sha256_utf8':hashlib.sha256((OUT/'scan023_B_source_coverage.json').read_bytes()).hexdigest(),
    'witness_source_coverage_sha256_utf8':hashlib.sha256((OUT/'scan023_witness_source_coverage.json').read_bytes()).hexdigest(),
    'source_text_counts':dict(differences=len(differences),doubts=len(doubts),inventory=len(inventory),notation=len(notation),
                              original_C_rows=len(original_rows),canonical_C_parts=sum(len(x['canonical_parts']) for x in original_rows),
                              graphical_groups=len(groups),component_map_records=len(component_records),
                              graphical_command_occurrences=len(commands),complete_TeX_partition_spans=len(partition)),
    'source_verification':support['source_verification'],
    'selected_counts':None,'source_selected':False,'main_approved':False,
}
(OUT/'scan023_B_source_extraction_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
