"""Commit root-approved source decisions after all seventeen crop inspections."""
from pathlib import Path
from datetime import datetime, timezone
import json
R = Path(__file__).resolve().parents[1]
r = json.loads((R/'checks/scan010_record_draft.json').read_text())
assert len(r['decisions']) == 28
assert all(d.get('final') is not None and d.get('evidence') is not None for d in r['decisions'])
r['main_adjudicated'] = True
r['brief_version'] = 'v08'
r['main_approved_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
r['draft_status'] = 'Root approved after personal crop inspection, independent-return comparison, and inventory reconciliation.'
r['approval_followups'] = []
for d in r['decisions']:
    d['main_approval_pending'] = False
    d['root_decided'] = True
    d['diff_C'] = d['id'] not in ['010-D03','010-D04','010-D08','010-D09']
    d['diff_H'] = False
    d['H'] = None
    d['marked_in_H'] = 'no'
    if d.get('C_doubt_source_row') is not None:
        d['C_doubt_status'] = 'retained'
    d['evidence'] = d['evidence'].replace('Root supplied decision: ', 'Root crop inspection: ').replace('root-supplied', 'root-approved')
    if d['crop'].startswith('out/'):
        d['source_crop_path'] = d['crop']
        d['crop'] = d['crop'][4:]
    assert (R/d['crop']).is_file()
dec = {d['id']:d for d in r['decisions']}
dec['010-D01']['qualification'] = 'Qualified primary reversal: the former filled primary remains an explicit alternative.'
dec['010-D10']['qualification'] = 'The original filled reading survives as an alternative; the pale centre supports the open primary.'
dec['010-D11']['qualification'] = 'The original filled primary is retained with an added open alternative; this is a qualified reading, not a conclusively displaced glyph.'
dec['010-D03']['evidence'] = 'The crop shows a descending dark/pale trace crossing the small horizontal graph, a thick lower bend, and a very pale continuation rising to the right with darker fragments.'
dec['010-D04']['evidence'] = 'The crop shows a shallow heavy lower V-shaped course, pale rising ends and dark fragments along the right ascent.'
dec['010-D05']['evidence'] = 'Repeated diagonal returning strokes cross the underlying chords and oval outline. Their cancellation/hatching qualification is retained. The visible paths are reproduced once; the generic horizontal strike is absent from the observed ink.'
dec['010-D08']['evidence'] = 'The crop shows a pale curved course bending down and returning toward the left, with two darker small pieces near the lower return.'
dec['010-D09']['evidence'] = 'Two small detached dark flecks lie diagonally one above-right of the other, separated by light paper.'
for d in r['doubts']:
    d['crop'] = dec[d['decision_id']]['crop']
    d['reason'] = dec[d['decision_id']]['evidence'] + ' ' + (dec[d['decision_id']].get('qualification') or '')
    if d['decision_id'] == '010-D15':
        d['alternatives'].append('Longer upper course toward (1559,895), proposed by reader B; its continuation remains unresolved.')
for i in r['inventory']:
    i['transcribed'] = 'yes'
    if i['element'] == '010.I42':
        i['first_words_or_objects'] = 'repeated diagonal strokes; cancellation primary, hatching alternative'
assert r['check_events'] == []
r['notes'] = r'''The sheet contains three rows of disk/oval drawings, with nine upper forms including the parenthesized variant, seven middle forms and five lower forms. Twelve small spot-and-stroke diagrams accompany them. The five literal OK labels, the ou in the upper-right parenthesis, the heavy question mark above the overdrawn lower disk, grouping braces and enclosing ovals are retained. The lower-left archive9 remains a comment. No title or manuscript date is supplied by the independent readings.

The original five C doubt-table rows remain qualified. Two compound source rows cover separately located marks; their nine local subloci are mapped without inflating the original row count. The first lower-left endpoint changes to open primary with filled alternative. The lower-middle first endpoint also has open primary, while the upper seventh middle vertex and final lower first vertex retain filled primary with open alternative. Each choice rests on the local light centre, rim or hook seen in its crop. No graph-theoretic interpretation selects a fill.

The lower second disk retains cancellation primary and hatching alternative, with the uncertainty marked in place. Its actual repeated diagonal paths are reproduced and the generic additional horizontal strike is removed. The projecting trace above the final middle disk is broken into dark pieces with pale intervening portions. Newly retained material includes the middle-disk spot, variant-disk fragments, two pale gap traces, the faint left continuation of an interior dash, the lower disk pendant and near-vertical trace, a far-right irregular patch, and small traces/spots around the angular foot marks. Their role, hand or surface origin remains unassigned where the ink provides only a shape.

The inner diagonal of the right angular foot group has a supported short course; B's longer upper continuation remains an unresolved alternative extent. The crop above upper disk4 approaches a faint lower continuation at its boundary, so the reproduced course stops at the supported portion. These limits are recorded without recropping settled loci.

The final lower disk's inventory description is corrected to four major interior runs. All four already occur in the witness and reader TeX paths; this correction supplies no transcription-change count. The same root crop reveals a small detached dark trace below the broad heavy segment near the lower-right rim, which is added as D28. The three reader proposals and witness C have no separate path there.

The page's OK and question-mark labels are authorial marks. No mathematical claim was checked, proved or refuted on this page, and CHECK_EVENTS receives no event for it. H supplies only a description, so the page contributes no H text-collation rows. The final TikZ remains a source-based approximation, with structural validation only.'''
r['workflow_note'] = 'Three fresh independent readers each viewed the whole scan once and both halves once. A/B/C-reader made15/13/13 local crops. Root personally inspected17 distinct crops:15 reader crops and2 new root crops; no whole or half view. One failed B/c05 display was context-truncated and unseen, followed by one successful view of the same existing crop. All reader/witness disagreements and all5 original C doubt rows were adjudicated; all5 remain qualified. Compound source rows map to9 local subloci. The final lower disk inventory count was checked on a new crop and its already-present four paths retained; the crop also supplied the newly added D28 trace. No OCR, research, compiler invocation or mathematical check occurred. Structural checks passed. Mechanical assembly saw no images. Brief v09 records the graphic-state, compound-row and inventory-wording lessons.'
r['root_page_text_exact'] = (R/'pages'/r['filename']).read_text()
r['root_crop_manifest'] = 'crops/010/manifest.json'
r['root_adjudication_log'] = 'checks/scan010_main_decisions.md'
r['counts'].update({'decision_loci':28,'C_difference_loci':24,'H_difference_loci':0,'actual_C_doubt_source_rows':5,'actual_C_doubt_local_subloci':9,'actual_C_doubts_retained':5,'actual_C_doubts_resolved':0,'remaining_doubt_or_graphic_uncertainty_loci':len(r['doubts']),'inventory_elements':len(r['inventory']),'check_events':0})
(R/'records/scan010.json').write_text(json.dumps(r, ensure_ascii=False, indent=2)+'\n')
print(r['counts'])
