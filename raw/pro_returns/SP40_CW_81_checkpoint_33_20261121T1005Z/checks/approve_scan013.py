"""Root approval after the forty completed scan013 crop decisions.

Text/source checks only. This script never opens an image or invokes a compiler.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib
import json

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

r = json.loads((OUT/'checks/scan013_record_draft.json').read_text())
m = json.loads((OUT/'checks/scan013_tex_mapping.json').read_text())
crop_audit = json.loads((OUT/'checks/scan013_root_crop_audit.json').read_text())
draft_path = OUT/'checks/scan013_final_draft.tex'
draft = draft_path.read_text()
assert digest(draft_path) == m['draft_sha256']
assert m['root_log_sha256'] == digest(OUT/'checks/scan013_main_decisions.md')
assert not m['pending_root_actions'] and not m['structural_validation']['errors']
assert m['counts'] == dict(differences=106, doubts=78, inventories=218,
                          packet_inventory=48, C_source_doubts=13,
                          source_top_level_statements=482, physical_groups=140,
                          selected_groups=82, pending_groups=0)
for role, fingerprints in m['fingerprints'].items():
    for name, key in [('reading.tex','reading_tex_sha256'),
                      ('report.json','report_json_sha256'),
                      ('reading.md','reading_md_sha256')]:
        assert digest(OUT/'readers/013'/role/name) == fingerprints[key]
assert crop_audit['successful_distinct_crops'] == 40
assert not crop_audit['root_full_or_half_viewed']
for item in crop_audit['images']:
    assert digest(OUT/item['path']) == item['sha256']
    assert item['successful_display_count'] == 1
assert len(r['decisions']) == 43 and len(r['inventory']) == 72
assert len(r['doubts']) == 35 and len(r['root_choices_recorded']) == 43
assert not r['check_events'] and r['hua_has'] == 'nothing'
assert sum(bool(x['diff_C']) for x in r['decisions']) == 40
assert not any(x['diff_H'] for x in r['decisions'])
assert {x['source_row'] for x in r['actual_C_doubt_map']
        if x['root_source_row_status']=='resolved'} == {1,2,5,7,10,11,12}
assert {x['source_row'] for x in r['actual_C_doubt_map']
        if x['root_source_row_status']=='retained'} == {3,4,6,8,9,13}
assert sum(len(x['local_subloci']) for x in r['actual_C_doubt_map']) == 14
assert len(r['source_row_coverage']) == 106
assert len(r['source_doubt_coverage']) == 78
assert all(x['decision_ids'] for x in r['source_row_coverage'])
assert all(x['decision_ids'] for x in r['source_doubt_coverage'])
assert (OUT/'checks/scan013_independent_source_audit.md').is_file()

page = draft.replace(
    '% Text-only scan013 assembly draft under the explicit root decisions.',
    '% Consolidated scan013; root crop decisions and exact source maps accompany this page.',1)
assert page != draft and '% crop-candidate:' not in page
page_sha256 = hashlib.sha256(page.encode()).hexdigest()
comment_delta = len(page)-len(draft)
def final_attachment(proposed):
    entry = dict(proposed,path='pages/'+r['filename'],sha256=page_sha256)
    if 'char_start' in entry:
        before = draft[proposed['char_start']:proposed['char_end']]
        assert hashlib.sha256(before.encode()).hexdigest() == proposed['body_sha256']
        assert proposed['line_start'] > 2
        entry['char_start'] += comment_delta
        entry['char_end'] += comment_delta
        assert page[entry['char_start']:entry['char_end']] == before
    return entry
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r.update(main_adjudicated=True, main_approved_utc=now, brief_version='v11',
         draft_status='Root approved after forty distinct crop inspections and complete source reconciliation.',
         root_page_source='pages/'+r['filename'], root_page_text_exact=page,
         root_crop_audit='checks/scan013_root_crop_audit.json',
         root_crop_count=40, root_actions_required=[])
r['root_log_snapshot_fingerprint'] = digest(OUT/'checks/scan013_main_decisions.md')
r['root_source_review'] = 'checks/scan013_independent_source_audit.md'
r['root_tex_mapping'] = 'checks/scan013_tex_mapping.json'
r['coverage_status'].update(main_adjudication_complete=True,
                            final_page_attachment_complete=True,
                            root_review_complete=True)
for decision in r['decisions']:
    assert decision['root_decided'] and decision['confidence'] in {'high','medium','low'}
    assert set(decision['readers']) == {'A','B','C'}
    assert decision['final'] and decision['evidence']
    decision['reader_reading_lists'] = decision['readers']
    decision['readers'] = {role:'; '.join(values) if isinstance(values,list) else values
                           for role,values in decision['readers'].items()}
    decision.update(main_approval_pending=False, main_counting_decision_pending=False,
                    pending_fields=[], root_crop_requirement='Completed; see the forty-crop audit.')
    if decision['id'] in {'013-D28','013-D29'}:
        decision['log_decision'] = True
    proposed = decision.get('proposed_page_sources', [])
    assert proposed, decision['id']
    decision['root_page_sources'] = [final_attachment(p) for p in proposed]

# The final clerical attachment pass must be complete before root runs this script.
for item in r['inventory']:
    assert item.get('proposed_page_sources'), item['element']
    assert item.get('sort_full_scan_xy') is not None, item['element']
    item['sheet_kind'] = 'list'
    item['sheet_kind_status'] = 'Root approved for the enumerated title/reference list; original cover labels retained in provenance.'
    if item['physical_key'] in {'source_01','source_02','source_10','source_11','source_32','source_34',
                                'source_35','source_36','archive'} or item['kind']=='drawing':
        item['hand'] = 'undetermined hand'
    item['hand_status'] = 'Root attribution from reader agreement and local crop decisions; uncertain residual attribution preserved.'
    item['transcribed'] = 'yes'
    item['transcribed_basis'] = 'Every selected component and label attached to the approved final page source.'
    item['main_approval_pending'] = False
    item['root_page_sources'] = [final_attachment(p) for p in item['proposed_page_sources']]
r['inventory'].sort(key=lambda x:(x['sort_full_scan_xy'][1],x['sort_full_scan_xy'][0],x['element']))
for a in r['abbreviations']:
    a['root_decided'] = True
for doubt in r['doubts']:
    assert all(k in doubt for k in ['location','reading','confidence'])
    doubt['main_approval_pending'] = False
    doubt['root_page_sources'] = [final_attachment(p) for p in doubt.get('proposed_page_sources',[])]
for item in r.get('attention_items',[]):
    item['root_status'] = 'Completed in root crop log, source map and final page attachment.'

r['notes'] = (
    'A six-column title/reference list headed Notes 1, 5, 7, 15, 20, 23, with '
    'main letters A, B, C, D, E, E and dates 1976/77, 1978/79, 1979/80, 1980, '
    '1981, 1981. The main titles are Découverte de la Méditation; Réveil en '
    'Cascades; Die Eltern (Les parents); Das Kind (L\'enfant); Der Baumeister '
    '(Le Bâtisseur); Le Bâtisseur. Secondary titles are Envol; Vers un plus '
    'long Voyage; Bild und Wahrheit (Image et Réalité); Der Wolf (Le Loup); '
    'Spiel- und Sucht (Jeu - et Fringale); Le ``Maître\'\'. The footer records '
    'M 1976 with a baseline star, M 1979, HS I, Sch I, Sch with barred VI, '
    'and Sch with barred IX. No expansion for M, HS or Sch is supplied on '
    'this sheet. An earlier A (1976/77) is struck near the top.\n\n'
    'Two manuscript question marks, the cancelled subdivisions, displaced '
    'pale forms, margin arrows, irregular rules and all ten surviving '
    'right-edge groups are preserved. The crossed B form is read (ii) '
    'from its own uprights and feet. The crossed last-column form remains '
    '(iii|iv), with low confidence. The readable pale A and pale (i) forms '
    'retain separate cancellation/live uncertainty. Faint residual strokes '
    'retain local shape qualifications without a supplied word, origin or '
    'writing chronology. Seven of thirteen original C doubtful-reading rows '
    'are resolved; six remain, including the compound final row with two '
    'local subloci. Archive numeral 12 is recorded in a comment with '
    'undetermined hand.\n\n'
    'The page supplies titles, dates and references. No mathematical '
    'statement was checked, used or refuted in reading it, and no check '
    'event is claimed. H supplies no text for this scan. Witness S '
    'SA01-K81-06 covers scans15–22 and supplies no reading for this sheet.'
)
r['workflow_note'] = (
    'Three fresh independent readers viewed the whole and each supplied half '
    'once; A made24 crops, B25 and C30. Root inspected40 distinct crops '
    '(10 own,5 A,24 B,1 C), without viewing a whole or half. The initial '
    'own01 display failed unseen and the identical image was displayed '
    'successfully once. All106 reader differences,78 reader doubts,218 '
    'reader inventory items and48 C inventory items are mapped. The13 '
    'original C source rows retain their identity across14 local subloci. '
    'Text-only clerks assembled82 selected contested groups and56 common '
    'text groups;482 literal top-level source statements and their local '
    'components have an explicit map. Independent source review found '
    'three provenance/count-wording issues, all recorded and corrected. '
    'Fixed origins and exact coordinate/dimension maps preserve selected '
    'paths. Full-rule references are context for the two local wedges. '
    'The A Réveil source has five commands containing six disconnected '
    'components. Structural source checks only; no OCR, research, compiler, '
    'renderer or mathematical check. Briefv12 records the resulting lessons.'
)
r['counts'].update(C=40,H=0,count_status='root approved',main_decision_groups=43,
                   inventory_items=72,provisional_doubt_groups=35,
                   remaining_doubts_status='root approved',
                   actual_C_doubts_resolved=7,actual_C_doubts_retained=6)

destination = OUT/r['root_page_source']
destination.write_text(page)
validation_path = OUT/'scripts/validate.py'
ns = {'__file__':str(validation_path)}
exec(validation_path.read_text().split('records=')[0],ns)
result = ns['check_tex'](destination)
assert not result['errors'],result
(OUT/'records/scan013.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
source_map_path = OUT/'checks/scan013_source_map.json'
source_map = json.loads(source_map_path.read_text())
source_map.update(status='Root approved: thirteen actual C rows mapped to fourteen local subloci; seven rows resolved and six retained.',
                  root_record='records/scan013.json',root_decisions='checks/scan013_main_decisions.md')
source_map_path.write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+'\n')
approval = dict(scan=13,approved_utc=now,page=r['root_page_source'],
                sha256=digest(destination),root_distinct_crops=40,
                structural_result=result,counts=r['counts'],
                C_confidences=dict(Counter(x['confidence'] for x in r['decisions'] if x['diff_C'])))
(OUT/'checks/scan013_root_approval.json').write_text(json.dumps(approval,ensure_ascii=False,indent=2)+'\n')
with (OUT/'progress.log').open('a') as f:
    f.write('scan013 root source/record approval '+now+';40 distinct crops; all source rows and final inventory attached; structural checks passed; no compilation\n')
print(json.dumps(approval,ensure_ascii=False))
