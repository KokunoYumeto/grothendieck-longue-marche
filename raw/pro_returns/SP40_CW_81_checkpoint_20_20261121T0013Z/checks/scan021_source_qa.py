"""One frozen-bundle source pass. No images, rendering, compilation or geometry work."""
from pathlib import Path
import collections
import hashlib
import json
import re
import shutil

BASE = Path('/workspace/scratch/94548b74fbe0')
CHECKS = BASE / 'out/checks'
EXPECTED = {
    'scan021_final_draft.tex': '96772b7d5d36792f72827807deffaa39e746d1876f771e9dd498cbcf0238ddce',
    'scan021_final_source_map.json': '79e4b3af563b5ff38df37e3b7b317f7bad9c48f6b1151fe7c2f6046bd367dcf9',
    'scan021_record_draft.json': 'f12eb52fa52759e4693dcaecf840f26779ea06bb9966dea281744db5e2bd3ca0',
}
errors = []
facts = {}
cache = {}
json_cache = {}
reference_keys = set()
reference_occurrences = collections.Counter()
approval_paths = []

def sha(s):
    return hashlib.sha256(s if isinstance(s, bytes) else s.encode('utf-8')).hexdigest()

def check(ok, label, detail=None):
    if not ok:
        errors.append({'check': label, 'detail': detail})

def resolve(value):
    p = Path(value)
    if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.tiff', '.tif', '.gif', '.webp', '.pdf'}:
        raise ValueError('Image/PDF access excluded: ' + value)
    if p.is_absolute():
        return p
    return (BASE if value.startswith(('out/', 'packets/', 'source/')) else BASE / 'out') / p

def read(value):
    p = resolve(value)
    key = str(p)
    if key not in cache:
        cache[key] = p.read_text(encoding='utf-8')
    return cache[key]

def pointer(value, ptr):
    cur = value
    for part in ptr.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur

def walk(value, loc):
    if isinstance(value, list):
        for i, child in enumerate(value):
            walk(child, loc + '/' + str(i))
        return
    if not isinstance(value, dict):
        return
    if 'main_approved' in value:
        approval_paths.append((loc, value['main_approved']))
    p = value.get('path')
    if isinstance(p, str) and 'char_start' in value and 'char_end' in value:
        s = read(p)
        start, end = value['char_start'], value['char_end']
        literal = value.get('excerpt', value.get('literal'))
        reference_occurrences[p] += 1
        key = (p, start, end, literal if isinstance(literal, str) else None)
        reference_keys.add(key)
        check(isinstance(start, int) and isinstance(end, int) and 0 <= start <= end <= len(s), 'source span bounds', loc)
        body = s[start:end]
        for k in ('excerpt', 'literal'):
            if isinstance(value.get(k), str):
                check(value[k] == body, 'source literal equality', [loc, k, p, start, end])
        if value.get('literal_sha256_utf8'):
            check(value['literal_sha256_utf8'] == sha(body), 'literal hash', loc)
        if value.get('source_sha256_utf8'):
            check(value['source_sha256_utf8'] == sha(s), 'source file hash', loc)
        if 'byte_start' in value:
            check(value['byte_start'] == len(s[:start].encode()), 'byte start', loc)
        if 'byte_end' in value:
            check(value['byte_end'] == len(s[:end].encode()), 'byte end', loc)
        if p in ('checks/scan021_final_draft.tex', 'out/checks/scan021_final_draft.tex'):
            for k in ('final_file_sha256', 'draft_sha256_utf8'):
                if k in value:
                    check(value[k] == EXPECTED['scan021_final_draft.tex'], 'selected attachment hash', [loc, k])
            if 'source_map_sha256' in value:
                check(value['source_map_sha256'] == EXPECTED['scan021_final_source_map.json'], 'record map binding', loc)
    if isinstance(p, str) and 'value' in value and ('json_pointer' in value or 'pointer' in value):
        if p not in json_cache:
            json_cache[p] = json.loads(read(p))
        ptr = value.get('json_pointer', value.get('pointer'))
        check(pointer(json_cache[p], ptr) == value['value'], 'source JSON value', [loc, p, ptr])
    if 'value' in value and isinstance(value.get('source'), dict):
        src = value['source']
        sp = src.get('path')
        ptr = src.get('pointer', src.get('json_pointer'))
        if sp and ptr and sp.endswith('.json'):
            if sp not in json_cache:
                json_cache[sp] = json.loads(read(sp))
            check(pointer(json_cache[sp], ptr) == value['value'], 'raw source value', [loc, sp, ptr])
    for k, child in value.items():
        walk(child, loc + '/' + k)

for fn, expected in EXPECTED.items():
    p = CHECKS / fn
    actual = sha(p.read_bytes())
    check(actual == expected, 'frozen input hash', [fn, expected, actual])
    shutil.copyfile(p, CHECKS / ('scan021_qa_frozen_' + fn.removeprefix('scan021_')))
facts['frozen_inputs'] = EXPECTED
draft = read('out/checks/scan021_final_draft.tex')
m = json.loads(read('out/checks/scan021_final_source_map.json'))
r = json.loads(read('out/checks/scan021_record_draft.json'))
u = json.loads(read('out/checks/scan021_source_union.json'))
sources = json.loads(read('out/checks/scan021_source_fingerprints.json'))
for p, rec in sources['source_fingerprints'].items():
    check(sha(read(p)) == rec['sha256'], 'immutable source fingerprint', p)
check(sha(read(sources['source_union']['path'])) == sources['source_union']['sha256'], 'source union fingerprint')
facts['immutable_source_fingerprints'] = len(sources['source_fingerprints'])
walk(m, 'map')
walk(r, 'record')
facts['source_reference_occurrences'] = sum(reference_occurrences.values())
facts['unique_exact_source_references'] = len(reference_keys)

position = 0
assembled = []
for seg in m['source_segments']:
    final, src = seg['final'], seg['source']
    check(final['char_start'] == position, 'source segment continuity', seg['id'])
    position = final['char_end']
    check(final['literal'] == src['literal'], 'source segment correspondence', seg['id'])
    assembled.append(src['literal'])
check(position == len(draft) and ''.join(assembled) == draft, 'complete source segment reconstruction')
facts['contiguous_source_segments'] = len(m['source_segments'])

stage = read(m['base_source'])
for rep in m['replacements']:
    check(sha(stage) == rep['stage_before_sha256_utf8'], 'replacement before hash', rep['id'])
    start, end = rep['stage_char_start'], rep['stage_char_end']
    check(stage[start:end] == rep['old_text'], 'replacement old source', rep['id'])
    check(''.join(x['literal'] for x in rep['removed_source_pieces']) == rep['old_text'], 'replacement removed-piece equality', rep['id'])
    check(''.join(x['literal'] for x in rep['inserted_source_pieces']) == rep['new_text'], 'replacement inserted-piece equality', rep['id'])
    stage = stage[:start] + rep['new_text'] + stage[end:]
    check(sha(stage) == rep['stage_after_sha256_utf8'], 'replacement after hash', rep['id'])
check(stage == draft, 'complete literal replacement replay')
facts['literal_replacements_replayed'] = len(m['replacements'])

groups = {g['id']: g for g in m['selected_groups']}
for g in m['selected_groups']:
    check(g['selected_exact_source'] == g['final_source_attachment']['literal'], 'selected group final literal', g['id'])
    check(''.join(p['literal'] for p in g['exact_source_pieces']) == g['selected_exact_source'], 'selected group source-piece reconstruction', g['id'])
    for component in g['literal_components']:
        check(''.join(p['literal'] for p in component['exact_source_pieces']) == component['final_source_attachment']['literal'], 'literal component source-piece reconstruction', g['id'])
facts['selected_groups'] = len(groups)

def span(x):
    a = x['final_source_attachment']
    return a['char_start'], a['char_end']

components = r['selected_literal_component_ownership']
paths = r['selected_literal_path_ownership']
check(len(set(span(x) for x in components)) == len(components), 'unique component ownership')
check(len(set(span(x) for x in paths)) == len(paths), 'unique draw/fill ownership')
all_group_components = {span(x) for g in m['selected_groups'] for x in g['literal_components']}
check(all_group_components == {span(x) for x in components}, 'complete group/component ownership coverage')
draw_starts = {match.start(1) for match in re.finditer(r'^\s*(\\(?:draw|fill)\b[^\n]*)', draft, re.M)}
path_starts = {x['final_source_attachment']['char_start'] for x in paths}
check(draw_starts == path_starts, 'all selected draw/fill commands owned', {'unmapped': sorted(draw_starts-path_starts), 'extra': sorted(path_starts-draw_starts)})
check(all(x['literal_command_kind'] in ('draw','fill') for x in paths), 'draw/fill ownership types')
facts['unique_literal_components'] = len(components)
facts['unique_draw_fill_commands'] = len(paths)

ids = {d['id'] for d in r['decisions']}
by_id = {d['id']: d for d in r['decisions']}
check(len(ids) == len(r['decisions']) == 71, 'decision identities')
check(len(r['doubts']) == 39 and len(r['inventory']) == 58, 'selected doubt/inventory totals')
allowed_kinds = {'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
conf = {w: collections.Counter(d['confidence'] for d in r['decisions'] if d['diff_'+w]) for w in 'CH'}
check(conf == {'C': {'high':4,'medium':8,'low':33}, 'H': {'high':5,'medium':8,'low':11}}, 'physical witness/confidence counts', conf)
facts['counts'] = {w:dict(conf[w]) for w in 'CH'}
facts['decision_doubt_inventory_totals'] = [71,39,58]
for d in r['decisions']:
    check(d['kind'] in allowed_kinds, 'allowed collation kind', d['id'])
    check(type(d['marked_in_H']) is bool, 'explicit H doubt Boolean', d['id'])
    check(set(d['readers']) == set('ABC'), 'complete public reader fields', d['id'])
    check(d['main_approved'] is False, 'selected decision pending approval', d['id'])
    check(d['final_source_attachment'] and d['root_authorization_sources'], 'selected decision attachments/authority', d['id'])
    for role in 'ABC':
        p = d['reader_provenance'][role]
        check(p['actual_complete_tex_sources'], 'actual reader TeX source supplied', [d['id'],role])
        check(all(s['path'] == f'out/readers/021/{role}/reading.tex' for s in p['actual_complete_tex_sources']), 'reader source identity', [d['id'],role])
for q in r['doubts']:
    check(all(k in q for k in ['location','reading','alternatives','confidence','reason']), 'doubt builder fields', q['decision_id'])
    check(q['decision_id'] in ids and by_id[q['decision_id']]['remaining_doubt'], 'remaining doubt identity', q['decision_id'])
    check(q['confidence'] == by_id[q['decision_id']]['confidence'], 'remaining doubt confidence', q['decision_id'])
    check(q['final_source_attachment'] and q['main_approved'] is False, 'remaining doubt source/pending status', q['decision_id'])
for inv in r['inventory']:
    check(all(k in inv for k in ['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']), 'inventory CSV fields', inv['element'])
    check(inv['transcribed'] == 'yes' and inv['selected'] is True and inv['main_approved'] is False, 'selected inventory state', inv['element'])
    check(bool(inv['final_source_attachment']), 'selected inventory attachment', inv['element'])
for parent in r['source_counting_constraints']:
    for w in 'CH':
        for child in parent[w+'_children']:
            check(by_id[child]['diff_'+w] is False and by_id[child][w+'_count_parent'] == parent['parent'], 'single physical count parent', [w,child,parent['parent']])

resolved = {'C021-R02','C021-R03','C021-R07','C021-R11','C021-R13','C021-R14'}
rows = {x['source_id']:x for x in r['C_source_rows']}
check(len(rows) == 15 and set(rows) == {f'C021-R{x:02}' for x in range(1,16)}, 'canonical original C rows')
for row_id, row in rows.items():
    check(len(row['source_parts']) == 1, 'canonical C part count', row_id)
    part = row['source_parts'][0]
    check(part['part_id'] == row_id+'-1', 'canonical C part identity', row_id)
    check(part['root_status'] == ('resolved' if row_id in resolved else 'retained'), 'canonical C outcome', row_id)
    check(part['decision_status'] == part['original_decision_status'] == part['original_source_decision_status'] == 'pending ink adjudication', 'original C pending history', row_id)
    check(part['main_approved'] is False and part['final_source_attachment'], 'selected C part pending/source', row_id)
facts['canonical_C'] = {'rows':15,'parts':15,'resolved':sorted(resolved),'retained':sorted(set(rows)-resolved)}

coverage_counts = {}
for role in 'ABC':
    report = json.loads(read(f'out/readers/021/{role}/report.json'))
    raw = r['reader_raw_rows'][role]
    for key, wrapped in raw.items():
        check([v['value'] for v in wrapped] == report[key], 'original reader raw rows preserved', [role,key])
    coverage = r['original_reader_difference_coverage'][role]
    check(set(coverage) == {d['id'] for d in report['differences']}, 'complete reader difference coverage', role)
    for key, item in coverage.items():
        check(bool(item['root_decision_ids']) and set(item['root_decision_ids']) <= ids and item['final_source_attachment'], 'reader difference selected coverage', [role,key])
    doubts = r['original_reader_doubt_coverage'][role]
    check([x['original_value'] for x in doubts] == report['doubts'], 'complete original reader doubts', role)
    for item in doubts:
        check(bool(item['root_decision_ids']) and set(item['root_decision_ids']) <= ids and item['final_source_attachment'], 'original doubt selected coverage', [role,item['original_identity']])
    silent = r['original_report_silent_source_coverage'][role]
    check([x['original_record'] for x in silent] == u['reader_sources'][role]['reported_silent_choices_with_complete_TeX'], 'complete report-silent source preservation', role)
    coverage_counts[role] = {'differences':len(coverage),'doubts':len(doubts),'silent_spans':len(silent)}
check(r['candidate_inventory'] == u['candidate_inventory'], 'candidate inventory provenance preserved')
check(r['candidate_graphical_groups'] == u['candidate_graphical_groups'], 'candidate graphics provenance preserved')
check(len(r['original_inventory_coverage']['rows']) == 161, 'original inventory coverage total')
for item in r['original_inventory_coverage']['rows']:
    check(item['selected_inventory_elements'] and item['root_decision_ids'] and item['final_source_attachment'], 'original inventory selected coverage', [item['reader'],item['original_element']])
check(len(r['original_graphical_group_coverage']) == 74, 'original graphics coverage total')
for item in r['original_graphical_group_coverage']:
    check(item['overlapping_source_scope_decision_ids'], 'original graphic decision coverage', item['original_group_id'])
check(len(r['source_locus_coverage']) == 71 and all(x['root_decision_ids'] and x['final_source_attachment'] for x in r['source_locus_coverage']), 'selected source-locus coverage')
facts['reader_coverage'] = coverage_counts
facts['raw_inventory_and_graphics_coverage'] = [161,74]

check(r['check_events'] == [], 'no invented mathematical check events')
check({a['form'] for a in r['abbreviations']} == {'i.e','i.e.','cqfd.','comp.'}, 'literal abbreviation forms')
check(all(a['expansion'] and a['final_source_attachment'] and a['main_approved'] is False for a in r['abbreviations']), 'abbreviation fields and sources')
s = by_id['L021-70']
check(s['S_id'] == 'SA01-K81-06' and s['S_status'] == 'no quoted example matched; existing marks retained', 'public S identity/status')
check(s['root_source_audit_choice_applied'] is True and s['root_ink_choice_applied'] is False and not s['diff_C'] and not s['diff_H'], 'source-only zero-count S disposition')
check(r['attributed_content_note']['mathematical_checks_performed'] is False and r['root_selected_content_note']['mathematical_checks_performed'] is False, 'attributed unverified content note')
check(r['main_adjudicated'] is False and r['main_approved'] is False, 'current root approval pending')
check(not r['pending_root_decision_ids'] and not r['pending_root_confidence_ids'], 'all ink/count choices supplied')
check(all(v is False for _,v in approval_paths), 'all stored main approvals pending', [(p,v) for p,v in approval_paths if v is not False])
facts['approval_path_prefix_counts'] = dict(collections.Counter('/'.join(p.split('/')[:2]) for p,_ in approval_paths))

plain_lines = [re.split(r'(?<!\\)%', line, maxsplit=1)[0] for line in draft.splitlines()]
math = []
blank_lines = []
for i, (raw, line) in enumerate(zip(draft.splitlines(), plain_lines), 1):
    if not raw.strip() and math:
        blank_lines.append(i)
    for token in re.findall(r'\\[\[\]()]|(?<!\\)\$', line):
        if token in (r'\[', r'\('):
            math.append(token)
        elif token in (r'\]', r'\)'):
            opening = {r'\]':r'\[',r'\)':r'\('}[token]
            check(bool(math) and math[-1] == opening, 'math delimiter nesting', [i,token])
            if math:
                math.pop()
        else:
            if math and math[-1] == '$':
                math.pop()
            else:
                math.append('$')
check(not math, 'all selected math delimiters closed', math)
check(not blank_lines, 'no selected physical math paragraph blanks', blank_lines)
check('$overset{' not in draft, 'unselected A missing-backslash issue absent')
facts['selected_math_blank_lines'] = blank_lines
facts['original_A_overset_disposition'] = m['pending_original_source_issue_not_selected']

expected_true_H = {'L021-01','L021-14','L021-15','L021-18','L021-19'}
facts['H_doubt_mark_true_current'] = [d['id'] for d in r['decisions'] if d['marked_in_H']]
facts['H_doubt_mark_true_required'] = sorted(expected_true_H)
facts['H_doubt_flag_repairs'] = [d['id'] for d in r['decisions'] if d['marked_in_H'] != (d['id'] in expected_true_H)]
facts['selected_group_empty_reverse_links'] = [g['id'] for g in m['selected_groups'] if not g['decision_ids']]
facts['required_explicit_reverse_links'] = {'C021-G02a':['L021-13'],'B021-G03':['L021-18']}
facts['unit_transfer_wording'] = [{k:v for k,v in x.items() if k != 'source'} for x in m['selected_unit_transfers']]
facts['scope'] = 'Exact source text, fingerprints, current record fields, coverage and literal replacement replay only. No images were opened or hashed; no rendering, compilation, geometry fitting, coordinate computation, research or mathematical check.'

result = {'frozen_single_pass': True, 'mechanical_errors':errors, 'facts':facts, 'manual_semantic_review':'See scan021_source_audit.md; named repairs only after this frozen pass.'}
(CHECKS / 'scan021_source_qa_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'mechanical_errors':errors,'facts':facts},ensure_ascii=False,indent=2))
