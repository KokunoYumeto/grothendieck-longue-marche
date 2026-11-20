"""Root approval of scan012 after its completed crop adjudication.

This operates on the root-approved text drafts only; no image or compiler use.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'out'
r = json.loads((OUT/'checks/scan012_record_draft.json').read_text())
mapping = json.loads((OUT/'checks/scan012_tex_mapping.json').read_text())
manifest = json.loads((OUT/'crops/012/manifest.json').read_text())
source = (BASE/'packets/012/C.tex').read_text()
page = (OUT/'checks/scan012_final_draft.tex').read_text()
page = page.replace('% Assembly draft only; final approval remains with the root reader.',
                    '% Consolidated scan012; all root crop decisions are recorded in the accompanying changes log.')
paths = re.findall(r'\\path\[fill=black,even odd rule\]\s*.*?;', source, re.S)
labels = re.findall(r'\\node\[inner sep=0pt[^\n]*;', source)
assert len(paths) == 68 and all(page.count(p) == 1 for p in paths)
assert len(labels) == 8 and all(page.count(p) == 1 for p in labels)
assert len(manifest) == 32 and all(x['viewed'] for x in manifest)
assert all(d['confidence'] in {'high','medium','low'} for d in r['decisions'])
assert all(d.get('final') is not None and d.get('evidence') for d in r['decisions'])
assert all(set(d['readers']) == {'A','B','C'} for d in r['decisions'])
assert all(d['confidence'] in {'high','medium','low'} for d in r['doubts'])
assert len({d['id'] for d in r['decisions']}) == len(r['decisions'])
assert sum(d.get('C_doubt_status') == 'retained' for d in r['decisions']) == 3
assert not any(d.get('C_doubt_status') == 'resolved' for d in r['decisions'])
assert not r['check_events']
for role in 'ABC':
    assert all(x['mapped'] for x in r['source_row_coverage'][role])
    assert all(x['mapped'] for x in r['source_doubt_coverage'][role])
assert not any(d.get('decision_id') == '012-D85' or d.get('id') == '012-D85' for d in r['doubts'])

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r['main_adjudicated'] = True
r['main_approved_utc'] = now
r['draft_status'] = 'Approved by root after all32 adjudication crops and text/source reconciliation.'
r['brief_version'] = 'v10'
r['root_page_source'] = 'pages/' + r['filename']
r['root_page_text_exact'] = page
r['root_crop_manifest'] = manifest
r.setdefault('coverage_status',{}).update({
    'root_completion_confirmation_pending':False,
    'root_ink_choice_pending':False,
    'root_inventory_attachment_pending':False,
    'root_review_complete':True,
})
r['root_final_count_instruction'] = (
    'Count each Boolean diff_C/diff_H locus once. Retained original C doubts '
    'create no C difference. D04 is a new C state qualification and a qualified '
    'H difference. Terminal, hook and faint-upright components share their '
    'physical cluster counts; A20/B015 is one patch, and R9 is an existing '
    'source component without a new difference. R11 is a zero-count child of N25. '
    'H physical-sketch parents include their local C additions.'
)
r['notes'] = (
    'A drawing sheet with four large upper ovals and two small alternatives, '
    'their crossing chords, heavy segments, open contacts and hatching; '
    'lower triangle/point, tripod, square and stemmed triangle; two left ovals '
    'and a parenthesized pair of miniatures; a central divided oval; lower '
    'quadrilateral with diagonal, looping mark and triangle with three inner '
    'spokes; and a right group of repeated rules, two oval outlines and long '
    'crossing curves. Four OK-family labels and four ou-family labels are '
    'preserved. The final upper OK/Ok and the compressed ou between the '
    'miniatures remain qualified. Archive numeral11 is recorded only in a '
    'comment; no title, date or manuscript-page number was recovered on this sheet.\n\n'
    'All three original C doubt rows remain. The lower-left overlaid zigzags '
    'retain cancellation as an alternative, and the whole right group retains '
    'live/cancelled uncertainty. No writing chronology is supplied. Faint rim '
    'intervals, terminal wisps, detached points and short strokes are reproduced '
    'at their observed positions with local shape confidence and unresolved '
    'hand, role and surface origin. A20/B015 identifies one patch; R9 was '
    'already a component of original C path68. All68 original contour blocks '
    'and eight lexical nodes remain literal components.\n\n'
    "H's rereading note already supplies four OK labels and limits its "
    "arrowhead claim to the horizontal axis. Its asserted whole-right-group "
    "cancellation remains an explicit alternative. Its final section and note "
    "expressly locate their wording on feuillet13 and are excluded from this "
    "scan's transcription and collation. The written ou labels present "
    "alternatives; no prose proof or formula is present to check. No mathematical "
    "computation, theorem verification or inferred identification of these "
    "drawings was performed. The OK labels supply no independent check event."
)
r['workflow_note'] = (
    'Three fresh independent readers each viewed the whole scan and both halves '
    'once; their crop counts were A11/B10/C17. Root inspected32 distinct '
    'adjudication crops:18 new and14 existing reader crops, without any whole '
    'or half view. An earlier own04 display and one two-image batch containing '
    'C16/C17 failed unseen; the identical files were displayed successfully '
    'afterward, with no recrop. All108 difference rows and91 reader doubt '
    'rows are mapped. The three actual C source doubts remain, with local '
    'subloci explicit. Physical-cluster counting preserves separately recorded '
    'component confidences. A20/B015 is one patch; R9 remains original path68. '
    'All68 original contour blocks and8 lexical nodes occur exactly once. '
    'Text-only clerks assembled source/records under the crop log, and an '
    'independent source reviewer checked coordinate wrappers. Structural '
    'validation only; no compiler, renderer, OCR, external research or '
    'mathematical check. Briefv11 records witness-boundary, component-mapping '
    'and image-display lessons.'
)
for a in r.get('abbreviations',[]):
    a['root_decided'] = True
locations = {
    '012-D50':'Detached point near (782,397), below upper second oval',
    '012-D66':'Lower-field pale oblique near (700,1853)',
    '012-D68':'Lower-field N25 point near (672.7,2002.6), with pale R11 below near (672.6,2007.4)',
    '012-D74':'Near bottom edge: short oblique near (686.5,2333.5)',
}
for d in r['decisions']:
    if d['id'] in locations:
        d['location'] = locations[d['id']]
    if d['id'] == '012-D11':
        d['C'] = 'Small triangle and separate large filled point; original C paths30 and31.'
        d['final'] = ('Small triangle with projecting apex-side strokes and its separate '
                      'large filled point; original C paths30 and31 retained. '
                      'The point has local component record012-D12. Approved local '
                      'additions:012-D43 and012-D44.')
for d in r['doubts']:
    key = d.get('decision_id') or d.get('id')
    if key in locations:
        d['location'] = locations[key]

# Root attaches every inventory element to the now-checked page source.
# Stable inventory IDs and all original reader mappings remain unchanged.
label_keys = {'label_top_ou':1,'label_second_OK':2,'label_third_OK':3,
              'label':4,'label_right_ou':5,'label_lower_OK':6,
              'label_parenthesis_ou':7,'ou':8}
path_map = {x['source_path']:x for x in mapping['source_paths']}
added_by_start = {x['draft_span']['line_start']:x for x in mapping['new_graphical_additions']}
for item in r['inventory']:
    key = item['physical_key']
    proposed = item.get('proposed_page_sources',[])
    bounds = []
    if key in label_keys:
        label = mapping['source_labels'][label_keys[key]-1]
        proposed = [{'path':r['root_page_source'],**label['draft'],
                     'source_label_number':label_keys[key]}]
        x,y = map(float,re.search(r'at \(([-.\d]+),([-.\d]+)\)',label['literal']).groups())
        bounds.append([x,y,x,y])
    elif key == 'archive':
        line = page[:page.index('% archive sheet number: 11')].count('\n')+1
        proposed = [{'path':r['root_page_source'],'line_start':line,'line_end':line,
                     'source_comment':'archive sheet number: 11'}]
        bounds.append([0,2361,0,2361])
    for entry in proposed:
        if entry.get('source_C_path'):
            bounds.append(path_map[entry['source_C_path']]['bbox_from_literal_vertices'])
        elif entry.get('line_start') in added_by_start:
            bounds.append(added_by_start[entry['line_start']]['bbox_full_pixels'])
    assert proposed and bounds, (item['element'],key)
    item['root_page_sources'] = []
    for entry in proposed:
        entry = dict(entry,path=r['root_page_source'])
        if entry not in item['root_page_sources']:
            item['root_page_sources'].append(entry)
    candidates = item.get('source_hand_candidates',[])
    if key == 'archive':
        item['hand'] = 'another unnamed hand (archive numeral)'
    elif 'undetermined hand' in candidates:
        item['hand'] = 'undetermined hand'
    else:
        assert set(candidates) <= {'Grothendieck','his hand'} and candidates, candidates
        item['hand'] = 'his hand'
    item['root_hand_decision_pending'] = False
    item['main_approval_pending'] = False
    item['transcribed'] = 'yes'
    item['transcribed_basis'] = 'Root-approved final page source attached; original reader flags remain in provenance.'
    item['sort_full_scan_xy'] = [min(b[0] for b in bounds),min(b[1] for b in bounds)]
    if key == 'lower_mini_right':
        # This inventory item is the lower portion of shared path34.
        item['sort_full_scan_xy'] = [216,805]
    for did in item.get('decision_ids',[]):
        if did in locations:
            item['position'] = locations[did]
    if key == 'lower_673':
        item['first_words_or_objects'] = 'N25 dark oval point and separate qualified pale R11 immediately below'
r['inventory'].sort(key=lambda x:(x['sort_full_scan_xy'][1],x['sort_full_scan_xy'][0],x['element']))
assert all(x['transcribed']=='yes' and x['hand'] and x['root_page_sources'] for x in r['inventory'])
for item in r.get('attention_items',[]):
    item['root_status'] = 'Resolved by the crop log and explicit final physical-group/source mapping.'
r['counts'] = dict(r.get('counts') or r.get('proposed_counts') or {})
r['counts'].update({
    'decision_loci':len(r['decisions']),
    'inventory_elements':len(r['inventory']),
    'remaining_doubt_or_graphic_uncertainty_loci':len(r['doubts']),
    'C_difference_loci':sum(bool(d.get('diff_C')) for d in r['decisions']),
    'H_difference_loci':sum(bool(d.get('diff_H')) for d in r['decisions']),
    'actual_C_doubts_retained':3,
    'actual_C_doubts_resolved':0,
    'check_events':0,
    'status':'root approved',
})
qa = OUT/'checks/scan012_geometry_source_qa.md'
assert qa.exists(), 'Independent source-coordinate QA must be available before approval'
r['source_coordinate_review'] = str(qa.relative_to(OUT))
destination = OUT/'pages'/r['filename']
destination.write_text(page)
validation_path = OUT/'scripts/validate.py'
ns = {'__file__':str(validation_path)}
exec(validation_path.read_text().split('records=')[0],ns)
result = ns['check_tex'](destination)
assert not result['errors'], result
(OUT/'records/scan012.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
approval = {'scan':12,'approved_utc':now,'page':str(destination.relative_to(OUT)),
            'sha256':hashlib.sha256(page.encode()).hexdigest(),
            'literal_source_paths':68,'literal_source_labels':8,
            'root_distinct_crops':32,'structural_result':result,'counts':r['counts']}
(OUT/'checks/scan012_root_approval.json').write_text(json.dumps(approval,ensure_ascii=False,indent=2)+'\n')
with (OUT/'progress.log').open('a') as f:
    f.write('scan012 root source/record approval '+now+';32 crops;68 C contours and8 labels preserved; structural checks passed; no compilation\n')
print(json.dumps(approval,ensure_ascii=False))
