"""One targeted, text-only audit of the frozen scan023 assembly and record.

This script reads text sources only. It does not open crop files or crop metadata,
render, compile, inspect geometry, select ink, or mutate any selected artifact.
"""
from pathlib import Path
import collections
import copy
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/94548b74fbe0')
CHECKS = ROOT / 'out/checks'
BOUND = {
    'scan023_final_draft.tex': 'b9a1249d12916f42eb5694e4e2433f2c95d5435083078cdb5f71db5ea7b69a1f',
    'scan023_final_source_map.json': '5c11242ea3f4fe19b14b70a8fb5707f7e36a6911cbce6525850a3201d86c41e3',
    'scan023_record_draft.json': '93bcfd5b78435a3d62f7853de218e218db4ff7998203c9a7a3d10ec90bf1440e',
    'scan023_record_review.md': '01bfc974d888f4f525841e40ae2cf00bd0effe3e208a70cb2f55551cdeee6307',
    'scan023_root_assembly_plan.md': 'dbb078b74042d49eec9ca1cc404270513ed91c02c7be796bc88311c0f2004193',
    'scan023_main_decisions.md': 'e47c66e9ceb1a9823bfa73ee6544e6068d84def3a91dee1547ab2e83ab4f07af',
    'scan023_root_count_authorization_v2.json': 'b11587fc4e86d8a5f6e269eebf320ed59080a45d8ce15b6a8f0945dcdd429827',
    'scan023_root_scope_authorization.json': 'ab98ffb03ea44a0cfc6541f322c51a1571930a0e256633ed752bbccb269a7a03',
    'scan023_coverage_qa.json': 'da660ce7786cc1f22851160e2166b38ad3295c0978f4a71538795f2dd3ff5fd4',
    'scan023_coverage_qa.md': 'f0e32a2875fe93bb4222eee2b0b87078e7406ce9b0cc56a2603b9d01ae564030',
}

TEXT_CACHE = {}
FAILURES = []
STATS = {}

def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def text(path):
    path = str(path)
    assert Path(path).suffix in {'.tex', '.md', '.txt', '.json', '.tsv', '.py'}, path
    assert 'crop_audit' not in path and 'image_metadata' not in path, path
    if path not in TEXT_CACHE:
        TEXT_CACHE[path] = (ROOT / path).read_text(encoding='utf-8')
    return TEXT_CACHE[path]

def obj(name):
    return json.loads(text('out/checks/' + name))

def check(condition, pointer, detail):
    if not condition:
        FAILURES.append({'pointer': pointer, 'detail': detail})

def escape(value):
    return str(value).replace('~', '~0').replace('/', '~1')

def walk(value, pointer='', skip=frozenset()):
    yield pointer, value
    if isinstance(value, dict):
        for key, child in value.items():
            if key not in skip:
                yield from walk(child, pointer + '/' + escape(key), skip)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, pointer + '/' + str(index), skip)

def pointer_get(value, pointer):
    for token in pointer.lstrip('/').split('/') if pointer else []:
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value

def pointer_apply(value, pointer, operation, replacement=None):
    parent, _, token = pointer.rpartition('/')
    target = pointer_get(value, parent)
    token = token.replace('~1', '/').replace('~0', '~')
    if isinstance(target, list):
        token = int(token)
        if operation == 'add':
            target.insert(token, copy.deepcopy(replacement))
        elif operation == 'remove':
            target.pop(token)
        else:
            target[token] = copy.deepcopy(replacement)
    elif operation == 'remove':
        del target[token]
    else:
        target[token] = copy.deepcopy(replacement)

def actual_path(ref):
    path = ref.get('workspace_path') or ref.get('path')
    if not isinstance(path, str) or Path(path).suffix not in {'.tex', '.md', '.txt', '.json', '.tsv', '.py'}:
        return None
    if 'crop_audit' in path or 'image_metadata' in path:
        return None
    if not (ROOT / path).is_file() and path.startswith(('checks/', 'readers/', 'packets/', 'briefs/')):
        path = 'out/' + path
    if not (ROOT / path).is_file():
        return None
    return path

def span(ref):
    return (ref.get('char_start', ref.get('char_start_zero_based')),
            ref.get('char_end', ref.get('char_end_exclusive')))

def check_refs(value, name):
    seen = set()
    occurrences = 0
    paths = set()
    for ptr, ref in walk(value, skip={'provenance', 'root_crop_audit'}):
        if not isinstance(ref, dict):
            continue
        start, end = span(ref)
        path = actual_path(ref)
        if path is None or not isinstance(start, int) or not isinstance(end, int):
            continue
        if not isinstance(ref.get('literal'), str):
            if not isinstance(ref.get('json_pointer'), str):
                continue
            full = text(path)
            raw = json.loads(full[start:end])
            check(raw == pointer_get(json.loads(full), ref['json_pointer']), name+ptr, 'JSON pointer and exact source text span differ.')
            ref = dict(ref, literal=full[start:end])
        occurrences += 1
        identity = (path, start, end, ref['literal'])
        if identity in seen:
            continue
        seen.add(identity)
        paths.add(path)
        full = text(path)
        at = name + ptr
        check(full[start:end] == ref['literal'], at, 'Exact text span differs from the referenced current text file.')
        for key in ['sha256', 'sha256_utf8', 'file_sha256_utf8']:
            if key in ref:
                check(ref[key] == digest(full), at + '/' + key, 'Referenced file hash differs.')
        for key in ['body_sha256', 'span_sha256_utf8']:
            if key in ref:
                check(ref[key] == digest(ref['literal']), at + '/' + key, 'Referenced literal hash differs.')
        for key in ['utf8_byte_start', 'start_byte_utf8']:
            if key in ref:
                check(ref[key] == len(full[:start].encode('utf-8')), at + '/' + key, 'UTF-8 text offset differs.')
        for key in ['utf8_byte_end_exclusive', 'end_byte_utf8']:
            if key in ref:
                check(ref[key] == len(full[:end].encode('utf-8')), at + '/' + key, 'UTF-8 text offset differs.')
    return {'reference_occurrences': occurrences, 'unique_exact_text_spans': len(seen), 'text_files': sorted(paths)}

def run_checks():
    for name, expected in BOUND.items():
        check(digest(text('out/checks/' + name)) == expected, name, 'Frozen text binding differs.')
    r, m, u, a = (obj(name) for name in ['scan023_record_draft.json', 'scan023_final_source_map.json', 'scan023_source_union.json', 'scan023_root_count_authorization_v2.json'])
    dmap = {d['id']: d for d in r['decisions']}
    gmap = {g['group_id']: g for g in r['selected_graphical_groups']}
    imap = {i.get('source_inventory_identity', i['element']): i for i in r['inventory']}
    umap = {x['locus_id']: x for x in u['loci']}
    for key, count in [('decisions',69), ('doubts',40), ('inventory',57), ('selected_graphical_groups',26), ('source_locus_coverage',62), ('C_source_rows',16)]:
        check(len(r[key]) == count, '/' + key, 'Expected count ' + str(count))
    check(len(dmap) == 69 and len(gmap) == 26 and len(imap) == 57, '/', 'Current identities must be unique.')
    for row in a['rows']:
        d = dmap[row['locus_id']]
        for rk, ak in [('diff_C','diff_C'),('diff_H','diff_H'),('physical_count_parent','count_parent'),('confidence','confidence')]:
            check(d[rk] == row[ak], d['id'] + '/' + rk, 'Root count/confidence authorization mismatch.')
    for who, total in [('C',33),('H',37)]:
        counted = [d for d in r['decisions'] if d['diff_' + who]]
        check(len(counted) == total, '/counts/' + who, 'Physical count differs.')
        check(len({d['physical_count_parent'] for d in counted}) == total, '/counts/' + who, 'Repeated counted physical parent.')
    expected_h = {'U023-08':['H023-ILL01'], 'U023-41':['H023-UNC01'], 'U023-42':['H023-ILL02']}
    for index, d in enumerate(r['decisions']):
        ptr = '/decisions/' + str(index)
        check(d['marked_in_H'] == (d['id'] in expected_h), ptr+'/marked_in_H', 'Local H marker flag differs.')
        check(d['H_marker_ids'] == expected_h.get(d['id'], []), ptr+'/H_marker_ids', 'Local H marker identities differ.')
        check(set(d['readers']) == {'A','B','C'} and all(d['readers'].values()), ptr+'/readers', 'Missing reader field.')
        for gid in d['selected_group_ids']:
            check(d['id'] in gmap[gid]['decision_ids'], ptr+'/selected_group_ids', 'Decision/group reciprocity failure.')
        for iid in d['inventory_ids']:
            check(d['id'] in imap[iid]['decision_ids'], ptr+'/inventory_ids', 'Decision/inventory reciprocity failure.')
        if d['id'].startswith('U'):
            check(d['reader_source_details'] == umap[d['id']]['readers'], ptr+'/reader_source_details', 'Original own-reader detail differs from the frozen union.')
        else:
            check(not d['diff_C'] and not d['diff_H'] and not d['root_ink_choice_applied'] and d['root_source_audit_choice_applied'], ptr, 'S row exceeds source-only authority.')
    for gid, g in gmap.items():
        for did in g['decision_ids']:
            check(gid in dmap[did]['selected_group_ids'], gid+'/decision_ids', 'Group/decision reciprocity failure.')
        for iid in g['inventory_ids']:
            check(gid in imap[iid]['selected_group_ids'], gid+'/inventory_ids', 'Group/inventory reciprocity failure.')
    for iid, i in imap.items():
        for did in i['decision_ids']:
            check(iid in dmap[did]['inventory_ids'], iid+'/decision_ids', 'Inventory/decision reciprocity failure.')
        for gid in i['selected_group_ids']:
            check(iid in gmap[gid]['inventory_ids'], iid+'/selected_group_ids', 'Inventory/group reciprocity failure.')
        for field in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']:
            check(isinstance(i[field],str) and bool(i[field]), iid+'/'+field, 'Inventory output field is empty.')
        check(i['transcribed'] == 'yes', iid+'/transcribed', 'Selected inventory entry not recorded as transcribed.')
    check([x['page_order'] for x in r['inventory']] == list(range(1,58)), '/inventory', 'Inventory order differs from the selected interleaving.')
    for index, lc in enumerate(r['source_locus_coverage']):
        d = dmap[lc['locus_id']]
        for lk, dk in [('readers','readers'),('reader_source_details','reader_source_details'),('reading','final'),('alternatives','alternatives'),('evidence','evidence'),('qualification','qualification'),('confidence','confidence'),('physical_count_parent','physical_count_parent')]:
            check(lc[lk] == d[dk], '/source_locus_coverage/'+str(index)+'/'+lk, 'Current decision/locus mirror differs.')
    statuses = []
    for index, row in enumerate(r['C_source_rows']):
        check(len(row['source_parts']) == 1, '/C_source_rows/'+str(index), 'Canonical C row part count differs.')
        part = row['source_parts'][0]
        statuses.append(part['selected_status'])
        check(part['selected_status'] == part['outcome'] == a['C_outcomes'][row['source_id']], '/C_source_rows/'+str(index)+'/source_parts/0', 'Canonical C outcome differs from root authority.')
        check('root_outcome' not in part, '/C_source_rows/'+str(index)+'/source_parts/0', 'Historical root outcome remains in a current part.')
    check(collections.Counter(statuses) == {'retained':12,'resolved':4}, '/C_source_rows', 'Canonical C totals differ.')
    for ptr, value in walk(r, skip={'provenance','root_crop_audit','reader_source_details'}):
        if ptr.endswith('/main_approved'):
            check(value is False, ptr, 'Approval must remain false.')
    check(r['check_events'] == [], '/check_events', 'Unexpected mathematical check event.')
    # Validate record evidence against the unchanged journal, without opening a crop.
    views = r['root_viewing_scope']['viewed_once']
    journal_paths = re.findall(r'Viewed `([^`]+)` once\.', text('out/checks/scan023_main_decisions.md'))
    check(len(views) == len(journal_paths) == len(set(journal_paths)) == 31, '/root_viewing_scope', 'The exact journal crop-reference set differs.')
    check({v['path'] for v in views} == set(journal_paths), '/root_viewing_scope/viewed_once', 'Crop references differ from the journal.')
    views_by_path = {v['path']:v for v in views}
    evidence_count = 0
    for index, d in enumerate(r['decisions'][:62]):
        for evidence in d['root_crop_evidence']:
            evidence_count += 1
            check(evidence['successful_display_count'] == 1, '/decisions/'+str(index)+'/root_crop_evidence', 'Display count differs.')
            check(evidence['journal'] == views_by_path[evidence['crop']]['journal'], '/decisions/'+str(index)+'/root_crop_evidence', 'Evidence journal span does not match the exact once-viewed crop entry.')
            check(evidence['observation'] in d['evidence'], '/decisions/'+str(index)+'/evidence', 'Actual observation omitted from public evidence.')
            check(evidence['crop'] in d['evidence'], '/decisions/'+str(index)+'/evidence', 'Exact crop reference omitted from public evidence.')
    check([d['id'] for d in r['decisions'][:62] if not d['root_crop_evidence']] == ['U023-19','U023-40','U023-62'], '/decisions', 'Source-only composition loci differ.')
    # Current selected source/map attachment and ownership checks, all literal text.
    check(m['groups'] == m['selected_groups'], '/groups', 'Map group alias differs.')
    check(len(m['selected_groups']) == 26 and len(m['exact_command_ownership']) == 166 and len(m['exact_wrapper_ownership']) == 112 and len(m['layout_contexts']) == 37, 'source-map', 'Selected structural inventory differs.')
    for g in m['selected_groups']:
        current = gmap[g['group_id']]
        for key in ['parent_group','child_group_ids','direct_command_ids','contained_command_ids','wrapper_ids','context_ids','entry_parent_context_id','physical_ownership']:
            check(current[key] == g[key], g['group_id']+'/'+key, 'Selected record group field differs from current source map.')
        for rk,mk in [('workspace_path','path'),('sha256','sha256_utf8'),('char_start','char_start_zero_based'),('char_end','char_end_exclusive'),('body_sha256','span_sha256_utf8'),('literal','literal')]:
            check(current['selected_source'][rk] == g['selected_source'][mk], g['group_id']+'/selected_source/'+rk, 'Selected source attachment field mapping differs.')
    commands = {c['command_id']:c for c in m['exact_command_ownership']}
    owned = [cid for g in m['selected_groups'] for cid in g['direct_command_ids']]
    check(len(commands) == len(owned) == len(set(owned)) == 166 and set(owned) == set(commands), '/exact_command_ownership', 'Direct command ownership is incomplete or duplicated.')
    for g in m['selected_groups']:
        for cid in g['direct_command_ids']:
            check(commands[cid]['selected_group_id'] == g['group_id'], g['group_id'], 'Command owner differs from direct group declaration.')
    parts = m['complete_selected_source_partition']
    check(len(parts) == 35, '/complete_selected_source_partition', 'Source partition size differs.')
    ctext = text('out/readers/023/C/reading.tex')
    dtext = text('out/checks/scan023_final_draft.tex')
    check(''.join(p['source']['literal'] for p in parts) == ctext, '/complete_selected_source_partition', 'Original C source is not completely covered once by the partition.')
    check(''.join(p['selected_source']['literal'] for p in parts) == dtext, '/complete_selected_source_partition', 'Selected source is not completely covered once by the partition.')
    for lc in m['source_locus_coverage']:
        d = dmap[lc['locus_id']]
        check([(x['char_start'],x['char_end'],x['literal']) for x in d['source_attachments']] == [(x['char_start_zero_based'],x['char_end_exclusive'],x['literal']) for x in lc['selected_source_spans']], lc['locus_id']+'/source_attachments', 'Record attachment differs from selected map locus spans.')
    STATS['record_exact_references'] = check_refs(r, 'record')
    STATS['map_exact_references'] = check_refs(m, 'map')
    STATS['journal_crop_reference_count'] = len(views)
    STATS['decision_observation_attachments'] = evidence_count
    # Preserve and replay bounded history in memory only.
    closure = obj('scan023_record_bounded_closure.json')
    original = obj('scan023_record_initial_draft.json')
    replay = copy.deepcopy(original)
    for change in closure['forward_changes']:
        if change['op'] != 'add':
            check(pointer_get(replay,change['path']) == change['before'], 'record-closure'+change['path'], 'Forward history before-value mismatch.')
        pointer_apply(replay,change['path'],change['op'],change.get('after'))
    check(replay == r, 'record-closure', 'Recorded bounded forward changes do not reconstruct the frozen record.')
    inverse = copy.deepcopy(r)
    for change in reversed(closure['forward_changes']):
        op = {'add':'remove','remove':'add','replace':'replace'}[change['op']]
        pointer_apply(inverse,change['path'],op,change.get('before'))
    check(inverse == original, 'record-closure', 'Recorded bounded inverse changes do not reconstruct the initial record.')
    scl = obj('scan023_source_assembly_bounded_closure.json')
    snaps = [obj('scan023_source_assembly_initial_snapshot.json'), obj('scan023_source_assembly_alternate_scope_snapshot.json')]
    current_files = {name:{'literal_utf8':text('out/checks/'+name)} for name in snaps[0]['files']}
    for name, body in current_files.items():
        body['sha256_utf8'] = digest(body['literal_utf8'])
    stages = [snaps[0]['files'],snaps[1]['files'],current_files]
    for stage_index, stage in enumerate(stages):
        for name, body in stage.items():
            check(digest(body['literal_utf8']) == body['sha256_utf8'], 'source-history/'+str(stage_index)+'/'+name, 'Historical text literal hash differs.')
    for index, transition in enumerate(scl['transitions']):
        old, new = stages[index], stages[index+1]
        for name, binding in transition['files'].items():
            check(binding['old_sha256_utf8'] == old[name]['sha256_utf8'] and binding['new_sha256_utf8'] == new[name]['sha256_utf8'], 'source-closure/'+transition['transition']+'/'+name, 'Bounded transition file hashes differ.')
        draft_replay = old['scan023_final_draft.tex']['literal_utf8']
        for change in sorted(transition['draft_exact_text_changes'], key=lambda x:x['old']['char_start_zero_based'], reverse=True):
            before,after=change['old'],change['new']
            start,end=before['char_start_zero_based'],before['char_end_exclusive']
            check(draft_replay[start:end] == before['literal'], 'source-closure/'+transition['transition'], 'Draft before-literal differs.')
            draft_replay = draft_replay[:start] + after['literal'] + draft_replay[end:]
        check(draft_replay == new['scan023_final_draft.tex']['literal_utf8'], 'source-closure/'+transition['transition'], 'Draft edits do not reconstruct the next exact text.')
        for key,name in [('map_exact_field_changes','scan023_final_source_map.json'),('gate_exact_field_changes','scan023_source_assembly_gate.json')]:
            replay=json.loads(old[name]['literal_utf8'])
            for change in transition[key]:
                if change['operation'] != 'add':
                    check(pointer_get(replay,change['json_pointer']) == change['old'], 'source-closure/'+transition['transition']+change['json_pointer'], 'Source history before-value differs.')
                pointer_apply(replay,change['json_pointer'],change['operation'],change.get('new'))
            check(replay == json.loads(new[name]['literal_utf8']), 'source-closure/'+transition['transition']+'/'+name, 'Source field edits do not reconstruct the next exact object.')
    STATS['record_history_changes_replayed'] = len(closure['forward_changes'])
    STATS['source_history_transitions_replayed'] = len(scl['transitions'])
    STATS['counts'] = r['counts']
    STATS['frozen_text_bindings'] = BOUND
    STATS['checked_text_source_hashes'] = {path:digest(body) for path,body in sorted(TEXT_CACHE.items())}
    return {'mechanical_failures':FAILURES, 'checks':STATS}

if __name__ == '__main__':
    print(json.dumps(run_checks(), ensure_ascii=False, indent=2))
