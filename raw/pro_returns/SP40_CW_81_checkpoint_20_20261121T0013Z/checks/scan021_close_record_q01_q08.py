#!/usr/bin/env python3
"""Apply only the authorized scan021 Q01-Q08 record metadata closure.

No selected TeX, original reader, image, count, confidence or C outcome changes.
"""
from pathlib import Path
import copy
import hashlib
import json

BASE = Path('/workspace/scratch/94548b74fbe0')
OUT = BASE / 'out/checks'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda name: json.loads((OUT / name).read_text())
OLD_RECORD = 'f12eb52fa52759e4693dcaecf840f26779ea06bb9966dea281744db5e2bd3ca0'
OLD_MAP = '79e4b3af563b5ff38df37e3b7b317f7bad9c48f6b1151fe7c2f6046bd367dcf9'
NEW_MAP = 'f235a85c0e71d1dc1f519e72abe2db85a7ff2d2a9ee6460fb3c2435d551f0bc4'
TEX_SHA = '96772b7d5d36792f72827807deffaa39e746d1876f771e9dd498cbcf0238ddce'
AUDIT_SHA = 'c575c4567a76c9b588ebf5633e4ab87447d6b12cbcb9d2355ebae5ef79708ac1'
MAP_LOG_SHA = '2852226eac0220ae3dcd681261f62b0d53392595d1d86fc73466a6aa0ee8d40e'
REVIEW = 'out/checks/scan021_root_source_review.md'
LOG_NAME = 'scan021_record_bounded_repair_v01.json'
assert sha(OUT / 'scan021_record_draft.json') == OLD_RECORD
assert sha(OUT / 'scan021_qa_frozen_record_draft.json') == OLD_RECORD
assert sha(OUT / 'scan021_qa_frozen_final_source_map.json') == OLD_MAP
assert sha(OUT / 'scan021_final_source_map.json') == NEW_MAP
assert sha(OUT / 'scan021_final_draft.tex') == TEX_SHA
assert sha(OUT / 'scan021_source_audit.md') == AUDIT_SHA
assert sha(OUT / 'scan021_map_bounded_repair_v01.json') == MAP_LOG_SHA
old = load('scan021_qa_frozen_record_draft.json')
r = copy.deepcopy(old)
m = load('scan021_final_source_map.json')
by = {d['id']: d for d in r['decisions']}
inv = {i['element']: i for i in r['inventory']}
selected = {g['id']: g for g in r['selected_graphical_groups']}
new_selected = {g['id']: g for g in m['selected_groups']}
classification = {}


def classify(pointer, finding):
    classification[pointer] = finding


def didx(did):
    return next(i for i,d in enumerate(r['decisions']) if d['id'] == did)


def qidx(did):
    return next(i for i,d in enumerate(r['doubts']) if d['decision_id'] == did)


def locusidx(did):
    return next(i for i,d in enumerate(r['source_locus_coverage']) if d['root_decision_ids'] == [did])


# Q01: explicit local reverse associations; all existing complete scopes remain.
for gid, did, element in [('C021-G02a','L021-13','021.G04'),('B021-G03','L021-18','021.G08')]:
    assert selected[gid]['decision_ids'] == []
    assert new_selected[gid]['decision_ids'] == [did]
    selected[gid]['decision_ids'] = [did]
    by[did]['actual_final_group_ids'].append(gid)
    inv[element]['related_decision_ids'] = [did]
    inv[element]['root_decision_sources'] = [copy.deepcopy(by[did]['root_evidence_source'])]
    classify('/selected_graphical_groups/' + str(next(i for i,g in enumerate(r['selected_graphical_groups']) if g['id'] == gid)) + '/decision_ids','Q01')
    classify(f'/decisions/{didx(did)}/actual_final_group_ids','Q01')
    classify(f'/inventory/@{element}/related_decision_ids','Q01')
    classify(f'/inventory/@{element}/root_decision_sources','Q01')

# Q03: the public column concerns a local H doubt mark.
false_ids = ['L021-20'] + [f'L021-{i:02d}' for i in range(30,41)] + ['L021-45','L021-46','L021-68']
true_bases = {
 'L021-01': r"H writes \uncertain{on a} at the opening; the attached uncertainty marker supplies the local doubt flag.",
 'L021-14': r"H writes \struck{\ill{}} for the cancelled Sigma cluster; the enclosed \ill{} supplies the local doubt flag.",
 'L021-15': r"H's shared cancelled-Sigma source is \struck{\ill{}}; its \ill{} supplies this retained-reading child's local doubt flag within L021-14.",
 'L021-18': r"H's complete Or passage is Or \struck{\ill{}} \ill{} :; its cancelled and live \ill{} placeholders supply the whole-passage doubt flag.",
 'L021-19': r"H's live component after the cancelled Or group is \ill{}; this placeholder supplies the local doubt flag for the selected on a component under L021-18.",
}
for did in false_ids:
    assert by[did]['marked_in_H'] is True
    by[did]['marked_in_H'] = False
    classify(f'/decisions/{didx(did)}/marked_in_H','Q03')
for d in r['decisions']:
    did = d['id']
    if did in true_bases:
        basis = true_bases[did]
    elif did == 'L021-20':
        basis = r"H writes a plain endpoint colon at this locus, with no local doubt marker. The separate Or \ill{} placeholders remain attached to parent L021-18."
    elif 30 <= int(did[-2:]) <= 40:
        basis = r"H's complete descriptive diagram \note{...} supplies this locus's source scope. That note contains no local uncertainty or illegibility marker; the diagram replacement count stays with L021-30."
    elif did in ['L021-45','L021-46']:
        basis = r"H writes \struck{implique} at this locus. The strike records the cancelled word; the source carries no uncertainty or illegibility marker here."
    elif did == 'L021-68':
        basis = r"H's corollary frame \note{...} describes the side rule and contains no local uncertainty or illegibility marker."
    else:
        basis = "The inspected local H source reading is " + d['H'] + ". This local reading carries no uncertainty or illegibility marker."
    d['marked_in_H_basis'] = basis
    classify(f'/decisions/{didx(did)}/marked_in_H_basis','Q03')
assert {d['id'] for d in r['decisions'] if d['marked_in_H']} == set(true_bases)

# Q04: selected right-hand exclusion Sigma and the exact independent source details.
d = by['L021-43']
d['evidence'] = ('The completed A021G12 group retains the short dark upper run, separate interrupted pale left extension and tiny pale point with the full Sigma body, i and plus. '
    'The head/retrace versus independent upper-rule role remains qualified, without an assigned overline operation.')
d['readers'] = {
 'A': 'A021G12 has a short dark head, a separate gray left extension and a tiny gray filled point, with the complete Sigma, i and plus; the local head/retrace | independent upper-rule role remains qualified.',
 'B': 'The inspected complete right-Sigma span in B021-G07 has a short dark head and a separate pale extension, with no corresponding point in that span. It retains the primary Sigma-i-plus reading.',
 'C': 'The inspected complete right-Sigma span in C021-G06 has one continuous head path and no separate pale extension or point. It retains the primary Sigma-i-plus reading with the local head/retrace | independent upper-rule qualification.',
}
q = r['doubts'][qidx(d['id'])]
q['reason'] = d['evidence']
q['readers'] = copy.deepcopy(d['readers'])
r['source_locus_coverage'][locusidx(d['id'])]['readers'] = copy.deepcopy(d['readers'])
inv['021.G24']['first_words_or_objects'] = 'Complete Sigma-i-plus with short dark upper run, separate interrupted pale left extension and tiny pale point; local upper-run-role doubt retained'
for pointer in [f'/decisions/{didx(d["id"])}/evidence',f'/decisions/{didx(d["id"])}/readers',
    f'/doubts/{qidx(d["id"])}/reason',f'/doubts/{qidx(d["id"])}/readers',
    f'/source_locus_coverage/{locusidx(d["id"])}/readers','/inventory/@021.G24/first_words_or_objects']:
    classify(pointer,'Q04')

# Q05: the selected C group is the supplied short pale upright, with V outside.
d = by['L021-53']
d['final'] = 'qualified detached short pale upright C021-M05 above V'
d['evidence'] = ('The completed C021-M05 group retains a detached short pale upright. V and the adjoining words remain outside the group. '
    'Role, hand, attachment and surface origin remain undetermined.')
d['readers'] = {
 'A': 'A021M03 draws a qualified small gray filled ellipse above V; its complete source leaves V and de outside and retains undetermined role, hand and surface origin.',
 'B': 'The inspected B021-G10-V-speck source draws a qualified detached short pale upright; the adjoining V and words are outside that nested trace group.',
 'C': 'C021-M05 draws the qualified detached short pale upright above V; V and the adjoining words remain outside the group, with role, hand, attachment and surface origin undetermined.',
}
q = r['doubts'][qidx(d['id'])]
q['reading'] = d['final']
q['reason'] = d['evidence']
q['readers'] = copy.deepcopy(d['readers'])
r['source_locus_coverage'][locusidx(d['id'])]['readers'] = copy.deepcopy(d['readers'])
inv['021.G28']['first_words_or_objects'] = 'Qualified detached short pale upright; V and adjoining words remain outside the group; role, hand, attachment and surface origin undetermined'
for pointer in [f'/decisions/{didx(d["id"])}/final',f'/decisions/{didx(d["id"])}/evidence',f'/decisions/{didx(d["id"])}/readers',
    f'/doubts/{qidx(d["id"])}/reading',f'/doubts/{qidx(d["id"])}/reason',f'/doubts/{qidx(d["id"])}/readers',
    f'/source_locus_coverage/{locusidx(d["id"])}/readers','/inventory/@021.G28/first_words_or_objects']:
    classify(pointer,'Q05')

# Q06: only the attributed literal source-symbol correction is recorded.
by['L021-65']['mathematical_consequence'] = r'The final corollary line writes comp. de $X\setminus\Sigma_\alpha$; H gives comp. de $X\setminus E_\alpha$.'
classify(f'/decisions/{didx("L021-65")}/mathematical_consequence','Q06')

# Q08: complete parents retain their scoped writing/trace attribution.
mixed = {
 '021.G03': 'C021-M01, the two detached pale upper runs',
 '021.04': 'C021-M01, the two detached pale upper runs',
 '021.G10': 'C021-M03, the detached point and pale lower continuation',
 '021.08': 'C021-M03, the detached point and pale lower continuation',
 '021.G15': 'A021M04, the detached pale run beyond the outer marginal brace',
 '021.12': 'A021M04, the detached pale run beyond the outer marginal brace',
 '021.G27': 'C021-M05, the detached upright above V, and C021-M06, the detached point left of the rule',
 '021.17': 'C021-M05, the detached short pale upright above the first V',
}
for element, traces in mixed.items():
    inv[element]['hand'] = 'his hand for the main writing; undetermined hand for the detached trace(s)'
    inv[element]['hand_scope'] = ('The supplied main-writing attribution remains his hand. The hand of ' + traces +
        ' remains undetermined within this complete region; the corresponding individual trace entry retains that qualification.')
    classify(f'/inventory/@{element}/hand','Q08')
    classify(f'/inventory/@{element}/hand_scope','Q08')

# Q07: page-region interleaving uses the existing supplied ownership/position labels.
old_order = [item['element'] for item in r['inventory']]
new_order = [
 '021.01',
 '021.02','021.G01','021.G02',
 '021.03',
 '021.04','021.G03','021.G05','021.G06','021.G04','021.05','021.G07',
 '021.06',
 '021.07','021.G08',
 '021.08','021.G09','021.G10','021.G11',
 '021.09',
 '021.10','021.G12','021.G13',
 '021.11','021.G14',
 '021.12','021.G15','021.G16','021.G17','021.G18','021.G19','021.G20','021.G21',
 '021.13',
 '021.14','021.G22','021.G23','021.G24',
 '021.15','021.16','021.G25','021.G26',
 '021.17','021.G27','021.G36','021.G28','021.G30',
 '021.18','021.G31','021.G32',
 '021.19','021.G29',
 '021.20','021.G34','021.21','021.G33','021.G35',
 '021.ARCHIVE',
]
assert len(new_order) == len(old_order) == 58 and set(new_order) == set(old_order)
r['inventory'] = [inv[element] for element in new_order]
permutation = [dict(element=element,old_position=old_order.index(element)+1,new_position=new_order.index(element)+1)
    for element in old_order]

# Only current selected-map binding fields receive the new map hash. Raw source
# and assembly histories remain at their original values.
binding_roots = ['decisions','doubts','inventory','abbreviations','C_source_rows','original_reader_difference_coverage',
    'original_reader_doubt_coverage','selected_literal_component_ownership','selected_literal_path_ownership',
    'original_inventory_coverage','source_locus_coverage','selected_graphical_groups','complete_selected_source_blocks',
    'unresolved_leadin_abbreviation_exclusion','attributed_content_note','root_selected_content_note']
binding_count = 0


def rebind(value):
    global binding_count
    if isinstance(value,dict):
        for key, child in value.items():
            if key == 'source_map_sha256':
                assert child == OLD_MAP
                value[key] = NEW_MAP
                binding_count += 1
            else:
                rebind(child)
    elif isinstance(value,list):
        for child in value:
            rebind(child)


for root in binding_roots:
    rebind(r[root])
assert r['selected_source_map']['sha256'] == OLD_MAP
r['selected_source_map']['sha256'] = NEW_MAP

# Existing pending-approval views remain unchanged. The following entry records
# the bounded processing authority and preserved first-pass bundle only.
r['bounded_source_metadata_repair'] = dict(scope='Q01-Q08 current metadata and mechanically necessary current map-hash bindings only.',
    root_authorization=dict(path=REVIEW,sha256=sha(BASE/REVIEW)),
    first_pass_audit=dict(path='out/checks/scan021_source_audit.md',sha256=AUDIT_SHA),
    frozen_before=dict(record_path='out/checks/scan021_qa_frozen_record_draft.json',record_sha256=OLD_RECORD,
        map_path='out/checks/scan021_qa_frozen_final_source_map.json',map_sha256=OLD_MAP,
        tex_path='out/checks/scan021_qa_frozen_final_draft.tex',tex_sha256=TEX_SHA),
    current_map_sha256=NEW_MAP,selected_tex_sha256=TEX_SHA,
    map_repair_log=dict(path='out/checks/scan021_map_bounded_repair_v01.json',sha256=MAP_LOG_SHA),
    record_repair_log_path='out/checks/' + LOG_NAME,
    script=dict(path='out/checks/scan021_close_record_q01_q08.py',sha256=sha(OUT/'scan021_close_record_q01_q08.py')),
    original_reader_files_changed=False,selected_TeX_changed=False,counts_or_confidences_changed=False,
    proof_checks_performed=False,geometry_computations_performed=False,broad_source_audit_rerun=False,
    closure_status='Exact authorized repairs applied; bounded independent closure and final root approval pending.')
classify('/bounded_source_metadata_repair','bounded repair provenance')

# Compare only authorized metadata fields, current bindings and the inventory
# permutation. List identities allow exact before/after field diffs without
# treating page-order movement as a content rewrite.
changes = []


def escape(key):
    return str(key).replace('~','~0').replace('/','~1')


def finding(pointer):
    if pointer.endswith('/source_map_sha256') or pointer == '/selected_source_map/sha256':
        return 'current map binding'
    candidates = [(prefix, label) for prefix,label in classification.items() if pointer == prefix or pointer.startswith(prefix+'/')]
    assert candidates, ('unclassified changed field',pointer)
    return max(candidates,key=lambda item:len(item[0]))[1]


def difference(before, after, old_pointer='', new_pointer='', identity_pointer=''):
    if type(before) is not type(after):
        changes.append(dict(finding=finding(identity_pointer),identity_pointer=identity_pointer,
            old_pointer=old_pointer,new_pointer=new_pointer,before=before,after=after))
    elif isinstance(before,dict):
        for key in sorted(set(before)|set(after)):
            op=old_pointer+'/'+escape(key);np=new_pointer+'/'+escape(key);ip=identity_pointer+'/'+escape(key)
            if key not in before or key not in after:
                changes.append(dict(finding=finding(ip),identity_pointer=ip,old_pointer=op,new_pointer=np,
                    before_present=key in before,after_present=key in after,before=before.get(key),after=after.get(key)))
            else:
                difference(before[key],after[key],op,np,ip)
    elif isinstance(before,list):
        if identity_pointer == '/inventory':
            old_items={item['element']:(i,item) for i,item in enumerate(before)}
            for j,item in enumerate(after):
                i,prior=old_items[item['element']]
                difference(prior,item,old_pointer+'/'+str(i),new_pointer+'/'+str(j),identity_pointer+'/@'+item['element'])
        elif len(before) != len(after):
            changes.append(dict(finding=finding(identity_pointer),identity_pointer=identity_pointer,
                old_pointer=old_pointer,new_pointer=new_pointer,before=before,after=after))
        else:
            for i,(prior,current) in enumerate(zip(before,after)):
                difference(prior,current,old_pointer+'/'+str(i),new_pointer+'/'+str(i),identity_pointer+'/'+str(i))
    elif before != after:
        changes.append(dict(finding=finding(identity_pointer),identity_pointer=identity_pointer,
            old_pointer=old_pointer,new_pointer=new_pointer,before=before,after=after))


difference(old,r)
assert r['counts'] == old['counts']
assert r['C_doubt_resolution_counts'] == old['C_doubt_resolution_counts']
for prior,current in zip(old['decisions'],r['decisions']):
    for field in ['diff_C','diff_H','confidence','C_count_parent','H_count_parent','physical_count_parent','C_doubt_status','source_C_doubt_rows','source_C_doubt_parts']:
        assert prior[field] == current[field], (prior['id'],field)
for field in ['reader_raw_rows','reader_extra_source_fields','candidate_inventory','candidate_graphical_groups',
    'original_source_issues','S_source_rows','original_graphical_group_coverage','original_report_silent_source_coverage','processing_provenance']:
    assert r[field] == old[field],field
assert r['main_adjudicated'] is False and r['main_approved'] is False
assert len([c for c in changes if c['identity_pointer'].endswith('/marked_in_H')]) == 15


def write(name,value):
    (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


# Current companion outputs carry the same repaired map bindings. Their previous
# byte-identical versions are retained as bounded-closure snapshots.
companion_results = []
for name, value in [
    ('scan021_attributed_content_note.json',r['attributed_content_note']),
    ('scan021_C_doubt_outcomes.json',dict(scan=21,original_catalog=load('scan021_source_union.json')['canonical_C_catalog'],
        root_journal=r['root_journal'],counts=r['C_doubt_resolution_counts'],rows=r['C_source_rows'],main_adjudicated=False)),
]:
    source=OUT/name
    prior_sha=sha(source)
    snapshot=OUT/(source.stem+'_pre_Q01_Q08'+source.suffix)
    assert not snapshot.exists()
    snapshot.write_bytes(source.read_bytes())
    write(name,value)
    companion_results.append(dict(path='out/checks/'+name,before_sha256=prior_sha,after_sha256=sha(source),
        preserved_before_path='out/checks/'+snapshot.name,scope='Current selected-map bindings only; original text/outcomes unchanged.'))

write('scan021_record_draft.json',r)
new_record_sha=sha(OUT/'scan021_record_draft.json')
log=dict(scan=21,scope='Authorized Q01-Q08 bounded source metadata closure; no second broad source audit.',
    authorization=r['bounded_source_metadata_repair']['root_authorization'],
    initial_source_audit_sha256=AUDIT_SHA,
    record_before=dict(path='out/checks/scan021_qa_frozen_record_draft.json',sha256=OLD_RECORD),
    record_after=dict(path='out/checks/scan021_record_draft.json',sha256=new_record_sha),
    map_before_sha256=OLD_MAP,map_after_sha256=NEW_MAP,selected_TeX_sha256=TEX_SHA,
    map_repair_log=r['bounded_source_metadata_repair']['map_repair_log'],
    field_changes=changes,field_change_count=len(changes),
    inventory_order_change=dict(finding='Q07',old_order=old_order,new_order=new_order,permutation=permutation,
        scope='Existing supplied page-region labels and parent/child ownership; identities and exact source attachments retained.'),
    source_map_hash_binding_updates=binding_count,companion_output_changes=companion_results,
    preserved_counts=copy.deepcopy(r['counts']),preserved_C_outcomes=copy.deepcopy(r['C_doubt_resolution_counts']),
    all_selected_approvals_false=True,bounded_closure_status='Awaiting independent Q01-Q08 closure.')
write(LOG_NAME,log)

fp=OUT/'scan021_source_fingerprints.json'
fingerprint_before=sha(fp)
snapshot=OUT/'scan021_source_fingerprints_pre_Q01_Q08.json'
assert not snapshot.exists()
snapshot.write_bytes(fp.read_bytes())
fingerprints=load('scan021_source_fingerprints.json')
fingerprints['selected_map']['sha256']=NEW_MAP
for name in ['scan021_record_draft.json','scan021_C_doubt_outcomes.json','scan021_attributed_content_note.json',LOG_NAME,'scan021_close_record_q01_q08.py']:
    fingerprints['prepared_files'][name]=dict(sha256=sha(OUT/name))
fingerprints['bounded_record_closure']=dict(previous_manifest_sha256=fingerprint_before,
    preserved_previous_manifest='out/checks/scan021_source_fingerprints_pre_Q01_Q08.json',
    record_sha256=new_record_sha,map_sha256=NEW_MAP,tex_sha256=TEX_SHA,
    repair_log=dict(path='out/checks/'+LOG_NAME,sha256=sha(OUT/LOG_NAME)),
    root_authorization=r['bounded_source_metadata_repair']['root_authorization'])
fingerprints['record_stage']='Q01-Q08 corrected selected record frozen for bounded source closure and final root review.'
write('scan021_source_fingerprints.json',fingerprints)

print(json.dumps(dict(record_sha256=new_record_sha,map_sha256=NEW_MAP,tex_sha256=TEX_SHA,
    repair_log_path='out/checks/'+LOG_NAME,repair_log_sha256=sha(OUT/LOG_NAME),
    field_change_count=len(changes),current_map_hash_bindings=binding_count,
    finding_field_counts={key:sum(c['finding']==key for c in changes) for key in sorted({c['finding'] for c in changes})},
    inventory_entries=len(new_order),true_H_flags=sorted(true_bases),physical_counts=dict(C=45,H=24),
    source_fingerprints_sha256=sha(fp),approval=False),ensure_ascii=False))
