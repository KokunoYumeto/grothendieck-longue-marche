"""Save the completed scan023 second reading; static checks only."""
from pathlib import Path
import copy
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/8f839dff4bf0')
WORK = ROOT / 'SP74_C13_143+145_work'
KEY = '143_scan023'
packet = json.loads((ROOT/'reader_packets'/f'{KEY}.json').read_text())
page_path = WORK/'pages'/f'{KEY}.tex'
prior_path = WORK/'reviews'/f'{KEY}_accepted.json'
accepted = page_path.read_text()
prior_bytes = prior_path.read_bytes()
prior = json.loads(prior_bytes)

edits = [
    ('automatiquement à\n', 'automatiquement \\unsure{à|:}\n'),
    (r'\text{à }\widetilde\Pi', r'\text{\unsure{à|:} }\widetilde\Pi'),
]
candidate = accepted
for before, after in edits:
    assert candidate.count(before) == 1
    candidate = candidate.replace(before, after)

crop_names = [
    '143_scan023_A_first-map.png',
    '143_scan023_A_diagram-target.png',
    '143_scan023_A_interlinear-isom.png',
    '143_scan023_A_lower-indices.png',
    '143_scan023_A_est.png',
    '143_scan023_A_closing.png',
    '143_scan023_main_rev_constant.png',
    '143_scan023_main_objects.png',
    '143_scan023_main_sends.png',
    '143_scan023_main_arrows_condition.png',
    '143_scan023_main_desig.png',
    '143_scan023_main_lower_domain.png',
    '143_scan023_main_par.png',
]
viewed = {'crops/'+name for name in crop_names}
boxes = {row['crop']:row['box'] for row in prior['changes']}
first_crop = 'crops/143_scan023_A_first-map.png'
target_crop = 'crops/143_scan023_A_diagram-target.png'

reasons = [
    'The reduced graph has a small upright or slanted upper mark and a fuller dark lower body. The lower body is less point-like than the two marks of the following Phi colon, which favors à. Its reduction nevertheless leaves a colon possible. Retain à first and restore the explicit alternative instead of claiming a secure word reading.',
    'The mark on the line before tilde Pi consists of a small bent upper stroke and a compact lower body, matching the reduced introduction before the first map. The fuller/bent form favors à but does not securely exclude a colon. The preceding word égaux is separately clear: accented initial vowel, long g descender and aux ending. Its high confidence must not be transferred to this small following mark.',
]
findings = [
    {
        'id': KEY+'-auditC-F1',
        'place': 'After automatiquement, before the first displayed map',
        'before': edits[0][0], 'after': edits[0][1],
        'reason': reasons[0], 'confidence':'medium',
        'crop':first_crop, 'box':boxes[first_crop],
        'against_C':False, 'against_H':True,
        'C':'automatiquement à',
        'H':'automatiquement\n\\ill{} : \\ill{}',
        'kind':r'readable ink left as \ill{}',
        'consequential':False, 'marked_in_H':False,
        'decision_updates':[], 'certainty_only':True,
        'existing_change_row':1,
        'preferred_reading_unchanged':True,
    },
    {
        'id': KEY+'-auditC-F2',
        'place': 'Lower functor target, mark between égaux and tilde Pi',
        'before': edits[1][0], 'after': edits[1][1],
        'reason': reasons[1], 'confidence':'medium',
        'crop':target_crop, 'box':boxes[target_crop],
        'against_C':False, 'against_H':True,
        'C':'égaux à', 'H':r'\ill{} ($\widetilde{\Pi}$ ;',
        'kind':r'readable ink left as \ill{}',
        'consequential':False, 'marked_in_H':True,
        'decision_updates':[], 'certainty_only':True,
        'existing_change_row':26,
        'preferred_reading_unchanged':True,
        'separate_word_confidence':{'word':'égaux','confidence':'high'},
    },
]
updated_rows = {}
for number, new_final, reason in [
    (1, r'\unsure{à|:}', reasons[0]),
    (26, 'égaux}\\\\\n\\text{\\unsure{à|:} }', reasons[1]),
]:
    row = copy.deepcopy(prior['changes'][number-1])
    row['final'] = new_final
    row['ink'] = reason
    row['confidence'] = 'medium'
    if number == 26:
        row['word_confidence'] = {'égaux':'high'}
        row['following_mark_confidence'] = 'medium'
    updated_rows[number] = row

observations = [
    'The two-part reduced graph favors à but also admits colon; uncertainty restored without changing the preferred reading.',
    'The map label has a large loop, central descending stem and lower return, followed by two colon points.',
    'The map domain has a curled flag top and lower return, distinct from the plain T in the target; keep tau/calligraphic-T alternatives.',
    'The endpoint is minutely angular and thickened, without the clarity of the lower arrow head. Keep the existing arrow-first/bare-shaft alternative at low confidence.',
    'Hom has a tall H and compressed om; gr is low. Parentheses enclose plain T, comma and lower-case pi.',
    'Hom in the prose has no detached point before du; checked in native half1.',
    'The first groupoid has single angle brackets, the repeated flag-top object glyph, comma and lower-case pi; checked in native half1.',
    'The abbreviation has r/e/v and a point, without ê or t; universels retains its complete ending.',
    'Constant has two t structures separated by low joins. No r-u-i sequence of construits is present.',
    'Objets has a long j descender and final s. The following words are et de valeur, without a final s on valeur or an explic. phrase.',
    'The descending q and dotted i lead into envoie, then the tall d and short final c of donc.',
    'The first ens ends at the line edge with its small s stroke, without a detached full stop.',
    'Flèches has a long f descender, tall l, accent and the joined ch/e/s ending.',
    'Qui is visibly between et and pour, with descending q and short u/i.',
    'The membership line preserves t, comma, t-prime, membership sign and the repeated flag-top object glyph, followed by a comma.',
    'Désignant has its d, accent and long g descender with compressed ending. The next-line par has a long p descender and low a/r exit; both existing crops checked.',
    'The insertion begins with a wavy upper stroke over a short straight lower stroke, supporting simeq rather than equality.',
    'The small Isom subscript has single angle brackets around the same reduced object glyph, comma and pi; its tiny form is not relabelled as another alphabet.',
    'The thin guide curls down after the main-line indexed pi, runs beneath the addition and turns back at its right end. The existing TikZ accounts for its extent and lack of head.',
    'The second l’ens has no detached period; the guide crossing near l/apostrophe is not punctuation or cancellation.',
    'The retraced est has a low body and raised pointed final return, matching the closing est. Its extra-looking stroke does not identify a separately cancelled word.',
    'Both index pairs show a lower descending comma joined to the first t and a higher return/prime at the second t. The lower comma is retained against H.',
    'Ce has an open C and small e rather than an L; foncteur follows. Checked in native half2.',
    'The lower groupoid has single brackets, the flag-top object glyph, comma and lower-case pi. Two isolated low points below the object’s left side have no secure punctuation/index attachment and are not promoted into text.',
    'The target repeats rev. with its point, without the additional letters of revêt.',
    'Égaux remains clear at high confidence; the next-line two-part à/colon graph is separately medium-confidence and explicitly uncertain.',
    'The clearly covered capital Pi precedes the next-line heavily retraced simeq and opening parenthesis. There is no preceding parenthesis or following semicolon as in H.',
    'The parenthesis reads un objet with no separate seul word.',
    'The compressed d’isom ends in a horizontal continuation stroke, not a detached period; retain the existing medium-confidence abbreviation.',
    'The lower pi is followed by the large closing curve; no ellipsis follows that parenthesis.',
    'The compressed upper closing line reads est évidemment compatible avec op. de. Its initial est matches the earlier retraced form; retain medium confidence.',
    'The rounded group letter has open rightward returns; retain the existing E/Sigma alternative, low confidence and non-consequential.',
    'Donc has a d and short open ending; no final accented e or added n establishes donné.',
    'Four separate dark points follow the final pi; the upper display has three. Preserve this local count difference.',
    'The final pi and four points end the text. Compatible belongs to the preceding closing line; H’s extra tail is not another manuscript phrase.',
    'The lower-left graphite number is 22; it was read in the original and native half2. No author is assigned to that hand.',
]
assert len(observations) == len(prior['changes']) == 36
collation_confirmation = []
for number, (row, observation) in enumerate(zip(prior['changes'],observations),1):
    effective = updated_rows.get(number,row)
    audit_evidence = row['crop'] if row['crop'] in viewed else ('half1' if number in (6,7) else 'half2')
    entry = {
        'accepted_change_row':number, 'place':row['place'],
        'C':row['C'], 'H':row['H'], 'reading':effective['final'],
        'status':'certainty/evidence revised; preferred reading retained' if number in updated_rows else 'confirmed without revision',
        'confidence':effective['confidence'], 'observation':observation,
        'audit_evidence':audit_evidence,
        'crop_reused_in_this_audit':row['crop'] in viewed,
        'prior_crop':row['crop'], 'new_material_change':False,
    }
    if number == 16:
        entry['additional_audit_evidence']='crops/143_scan023_main_par.png'
    if number == 26:
        entry['word_confidence']={'égaux':'high'}
    collation_confirmation.append(entry)

doubts = copy.deepcopy(prior['remaining_doubts'])
for finding in findings:
    doubts.append({'place':finding['place'],'reading':r'\unsure{à|:}','alternatives':'Reduced accented à; colon.','confidence':'medium','reason':finding['reason'],'crop':finding['crop'],'box':finding['box'],'certainty_only':True})

confirmed = [
    {'place':'Opening prose and first map','checked':'Read G, dash, lequel opère donc sur plain T, its period, Ceci donne naissance automatiquement and the introductory two-part mark. Phi, colon, the domain, connector, Hom/gr, target comma and lower-case pi, parentheses and exactly three continuation points were checked. The first arrow and object alphabet remain uncertain.','evidence':['original','half1',first_crop]},
    {'place':'Ceci dit paragraph through the value on objects','checked':'Read the full sentence and punctuation: hom without point, two groupoïde occurrences, rev. universels de capital Pi, constant sur les objets et de valeur covered capital Pi sur ceux-ci. The clear tilde here is distinguished from the uncertain closing overmark.','evidence':['half1','crops/143_scan023_main_rev_constant.png','crops/143_scan023_main_objects.png']},
    {'place':'Sending morphisms and the membership clause','checked':'Qui envoie donc l’ens des flèches dans lower-case pi, dash, et qui pour t,t-prime in the object set, then désignant par. Both ens and hom points supplied by H are absent. Accents, final s forms and the explicit qui are preserved.','evidence':['half1','half2','crops/143_scan023_main_sends.png','crops/143_scan023_main_arrows_condition.png','crops/143_scan023_main_desig.png','crops/143_scan023_main_par.png']},
    {'place':'Interlinear insertion and the inclusion statement','checked':'Read the first indexed pi, l’ens des lambda in pi, simeq Isom with groupoid subscript and (t,t-prime), and the full curved guide. Read tels que lambda t=t-prime, est l’inclusion de the second indexed pi dans pi, period, Ce foncteur. Both index commas/primes and both lambda graphs are retained. No cancelled undertext was independently identifiable.','evidence':['half2','crops/143_scan023_A_interlinear-isom.png','crops/143_scan023_A_est.png','crops/143_scan023_A_lower-indices.png']},
    {'place':'Lower functor diagram and right-side target block','checked':'Checked source bracket count and arguments, shaft direction and explicit pointed head, and all seven target lines: Cat des; rev. universels; de Pi égaux; reduced à/colon and covered Pi; simeq (un objet; et groupe d’isom with continuation stroke; lower-case pi and closing parenthesis. The two long leftward horizontal returns belong to the g descenders in égaux and groupe, not additional guides or underlines.','evidence':['half2','crops/143_scan023_main_lower_domain.png',target_crop]},
    {'place':'Closing compressed prose and M0703','checked':'Read est évidemment compatible avec op. de the rounded group letter, sur capital Pi with possible tilde, donc sur lower-case pi and exactly four points. The possible tilde is entangled with évidemment above, so M0703 remains undecided. No extra words follow the terminal points.','evidence':['half2','crops/143_scan023_A_closing.png']},
    {'place':'Entire sheet, margins and physical strokes','checked':'Read original and both existing native halves once. No extra top pagination, marginal block, cancelled passage or omitted insertion guide was found. The visible lower edge, compressed final lines and graphite 22 are included. The single insertion guide is already drawn in TikZ. The numeral’s hand remains unnamed.','evidence':['original','half1','half2']},
    {'place':'Every repeated glyph and witness agreement','checked':'All five object-set graphs retain tau/calligraphic-T uncertainty and remain distinct from the two plain T occurrences. The clearly capital, clearly lower-case and covered Pi forms were inspected individually. Agreement of C/H at the first indexed pi, membership clause, lambda condition, map targets and shared prose was checked against ink rather than treated as evidence by itself.','evidence':['original','half1','half2',first_crop,'crops/143_scan023_A_interlinear-isom.png','crops/143_scan023_A_lower-indices.png',target_crop,'crops/143_scan023_A_closing.png']},
]

inventory_obs = [
    'All opening words and punctuation retained; introductory à now explicitly admits colon while remaining preferred.',
    'Phi map, Hom/gr target, disputed endpoint and three points checked without preferred-reading change.',
    'All prose from Ceci dit through désignant read; no omitted word or additional cancelled passage found.',
    'Par, indexed pi, l’ens des lambda in pi, and their physical relation to the addition checked.',
    'Inserted simeq Isom expression, its small groupoid subscript and both t arguments checked.',
    'Guide is a thin unheaded curve running under the addition, down at left and back at right; accepted drawing retained.',
    'Lambda equation, retraced live est, inclusion wording, second indexed pi and Ce foncteur checked.',
    'Single source brackets, comma, lower-case pi and clear right arrow checked.',
    'All target words remain; égaux high confidence, the following reduced à/colon medium and now explicitly uncertain.',
    'Simeq, un objet without seul, et groupe d’isom continuation, lower-case pi and closing parenthesis checked.',
    'Both compressed lines retained; possible Pi tilde and E/Sigma unresolved; final four points confirmed.',
    'Pencil 22 present at bottom-left, unnamed hand.',
]
assert len(inventory_obs) == len(prior['inventory']) == 12
inventory_confirmation = [{'element':item['element'],'position':item['position'],'status':'checked','observation':obs} for item,obs in zip(prior['inventory'],inventory_obs)]

raw_map = [[],[1,2],[3,4,5],[4,5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[],[24],[],[25],[26],[27],[28],[29],[30,31,32],[33],[34,35,36]]
assert len(raw_map) == len(packet['differences']) == 33
special = {
    1:'Scanpage locator is editorial markup, not an additional manuscript numeral.',
    2:'Map introduction and Phi read locally; the à/colon change is certainty-only. Tikzcd/options are markup.',
    3:'The raw alignment mixes object letters, arrow syntax and Hom. Each physical component was checked separately.',
    4:'The target and tiny connector were checked locally; the token alignment does not change their physical positions.',
    18:'H describes the insertion guide in an editorial note; the guide is drawn and the editorial prose is not transcribed.',
    23:'Tikzcd environment name is markup only.',
    24:'Environment options are markup; the source object glyph is independently checked.',
    25:'Arrow/gathered markup differs; the actual lower arrow has a clear rightward head and is retained.',
    27:'Égaux remains high confidence; uncertainty is restored only on its following reduced mark.',
    31:'Diagram wrappers are markup. Target-ending punctuation, closing prose and group glyph were checked in the appropriate crops.',
    32:'M0703 remains undecided; the separate donc/donné difference is confirmed as donc.',
    33:'Pencil 22 and four final points retained. No additional compatibles/illegible tail is present after the final pi.',
}
raw_checks = [{'packet_difference_number':n,'raw':copy.deepcopy(row),'accepted_change_rows':refs,'status':'checked','disposition':special.get(n,'Literal difference checked against ink; accepted preferred reading retained as detailed in referenced row(s).')} for n,(row,refs) in enumerate(zip(packet['differences'],raw_map),1)]

notes = [
    {'id':KEY+'-auditC-N1','text':'The opening action statement and Phi map into Hom of groups were checked as written. Its tiny connector remains arrow-first/bare-shaft uncertainty; the plain T arguments remain distinct from the object-set letter. The two reduced à/colon graphs now carry explicit alternatives with à preferred, as independently agreed by main.'},
    {'id':KEY+'-auditC-N2','text':'The source describes a groupoid homomorphism, constant on objects, with value the covered Pi. The indexed pi definition, lambda condition, inclusion and inserted Isom description are retained. The visible insertion relation is simeq and the thin physical guide is already reproduced. No proof of the stated construction or inclusions was performed.'},
    {'id':KEY+'-auditC-N3','text':'The seven-line lower target and parenthetical description are retained. Égaux is clear; only its following reduced mark gains uncertainty. The long horizontal returns from égaux and groupe are continuous g descenders and are not added as separate guides or rules. The two isolated low points below the left side of the lower object glyph have no unambiguous punctuation/index attachment and are not supplied as text.'},
    {'id':KEY+'-auditC-N4','text':'The closing compatibility assertion is retained with its group-letter uncertainty and M0703 Pi/covered-Pi uncertainty. The possible tilde remains entangled with évidemment on the line above. Four terminal points are visible, distinct from the first display’s three. The statement’s mathematics was not used to decide the tilde.'},
    {'id':KEY+'-auditC-N5','text':'No preferred source reading changes in this audit. Two certainty-only additions revise existing collation rows 1 and 26 rather than create new material rows. All eight existing doubts remain, plus the two à/colon doubts. The only original MARK, M0703, stays undecided. No new source crop, recrop, research, OCR or TeX compilation was used.'},
]

hand_log = [
    {'habit':'Reduced accented à can resemble two punctuation points.','places':'First-map introduction and lower target before covered Pi.','scope':'Both existing crops viewed once and compared with the definite colon after Phi.','misreadings':'Fuller/bent lower bodies favor à, but colon remains possible; both preferred readings stay unchanged with explicit alternatives.'},
    {'habit':'The curled flag-top object letter differs from plain capped T.','places':'All five object-set occurrences and both plain T occurrences on this page.','scope':'Every occurrence checked in the native halves, with local crops where needed.','misreadings':'Keep tau/calligraphic-T alternatives; no new alphabet-only material row.'},
    {'habit':'Small t cross-strokes can join a low comma or high prime, yielding h-like shapes.','places':'Both indexed pi sets and the inserted Isom arguments.','scope':'Existing interlinear and lower-indices crops viewed once.','misreadings':'The comma missing from H’s lower subscript remains present; no index regularization.'},
    {'habit':'Capital Pi has tall relatively straight legs; lower-case pi has a shorter curled right leg.','places':'Universal-covering targets, value on objects, map/groupoid arguments and closing line.','scope':'Every occurrence inspected; the closing overmark is a separate question.','misreadings':'Do not replace the final lower-case pi with capital Pi or settle M0703 from context.'},
    {'habit':'Retracing does not alone establish deletion.','places':'Est before l’inclusion, closing est and lower simeq.','scope':'The corresponding existing crops were compared within this page.','misreadings':'No independent cancelled undertext was recovered or supplied.'},
    {'habit':'Long g descenders can look like rules or physical guides.','places':'Désignant, égaux and groupe.','scope':'Existing desig and diagram-target crops viewed once; their descenders remain continuous with letters.','misreadings':'No separate underline or insertion guide is added for those returns.'},
    {'habit':'The actual short forms and continuation counts vary locally.','places':'Hom/gr, hom, both rev., both ens, d’isom continuation, op., upper three points and final four.','scope':'All listed occurrences checked in halves/crops.','misreadings':'Do not add H’s periods or expanded revêt.; do not reduce four final points to three.'},
    {'habit':'A possible overmark can overlap writing on the preceding line.','places':'M0703 below évidemment.','scope':'Existing closing crop viewed once; no recrop.','misreadings':'Bare Pi and covered Pi remain alternatives, bare first.'},
    {'habit':'Pencil pagination is not attributable from numeral shape alone.','places':'Bottom-left 22.','scope':'Only page numeral observed in original and halves.','misreadings':'Retained with an unnamed hand.'},
]

report = {
    'key':KEY,'reader':'C','stage':'second reading','first_reader':'A',
    'image_views':['original','half1','half2'],
    'image_view_details':[
        {'view':'original','path':packet['image'],'successful_views':1},
        {'view':'half1','path':packet['halves'][0],'box':packet['half_boxes'][0],'successful_views':1},
        {'view':'half2','path':packet['halves'][1],'box':packet['half_boxes'][1],'successful_views':1},
    ],
    'existing_crop_views':[{'crop':'crops/'+name,'box':boxes.get('crops/'+name),'successful_views':1} for name in crop_names],
    'existing_crop_metadata_note':'The accepted report gives no native box for its existing main_par crop; its path is recorded without inventing coordinates. All other reused boxes are copied from this page’s accepted evidence metadata.',
    'new_crops':[],
    'findings':findings,'confirmed':confirmed,
    'collation_confirmation':collation_confirmation,
    'existing_difference_updates':[{'accepted_change_row':n,'reason':'Certainty-only revision, no new material row; preferred reading and witness flags retained.','replacement':row} for n,row in updated_rows.items()],
    'remaining_doubts':doubts,
    'remaining_doubt_disposition':[{'existing_place':d['place'],'status':'retained unchanged'} for d in prior['remaining_doubts']],
    'decisions':copy.deepcopy(prior['decisions']),
    'mark_confirmations':[dict(copy.deepcopy(d),audit_status='confirmed unchanged',audit_reader='C') for d in prior['decisions']],
    'inventory_confirmation':inventory_confirmation,'inventory_additions':[],
    'inventory_updates':[
        {'element':'E01','change':'Record introductory à/colon uncertainty while retaining all words and the preferred à.'},
        {'element':'E09','change':'Keep égaux high confidence and record its following à/colon mark separately as medium-confidence uncertainty.'},
    ],
    'raw_difference_checks':raw_checks,'notes':notes,
    'check_events':[
        {'statement_id':notes[0]['id'],'type':'carried as background without fault found','outcome':'Reader C visually checked the action statement and map; no construction or homomorphism property was proved.','checked_by':'Reader C, second reading'},
        {'statement_id':notes[1]['id'],'type':'carried as background without fault found','outcome':'Reader C checked the groupoid account, indices, Isom addition and inclusion wording without proving them.','checked_by':'Reader C, second reading'},
        {'statement_id':notes[2]['id'],'type':'carried as background without fault found','outcome':'Reader C checked the target category wording and parenthetical comparison without a mathematical equivalence proof.','checked_by':'Reader C, second reading'},
        {'statement_id':notes[3]['id'],'type':'carried as background without fault found','outcome':'Reader C read the compatibility statement; its target tilde remains visually uncertain, with no mathematical check used to decide it.','checked_by':'Reader C, second reading'},
    ],
    'prior_check_event_attribution':'All prior accepted check events are background-only readings; none is represented as a new proof by this auditor.',
    'hand_log':hand_log,
    'main_consultation':'Main independently inspected the existing first-map and diagram-target crops and agreed to à-first/colon-alternative uncertainty at both loci. Main requested revision of existing H rows rather than new material rows, and separate confidence for clear égaux and its reduced following mark.',
    'accepted_fragment_sha256_before':hashlib.sha256(accepted.encode()).hexdigest(),
    'accepted_report_sha256_before':hashlib.sha256(prior_bytes).hexdigest(),
    'counts':{'material_findings':0,'certainty_only_findings':2,'prior_collation_rows_checked':36,'prior_rows_unchanged':34,'prior_rows_revised_only_in_certainty_or_evidence':2,'packet_difference_rows_checked':33,'original_marks_checked':1,'inventory_elements_checked':12,'remaining_doubts':10,'existing_crops_reused':13,'new_crops':0},
}

# Static validation only; no source image is opened here.
for f in findings:
    assert f['before'] in accepted and f['after'] in candidate
    assert f['C'] in packet['witness_C'],f
    assert f['H'] in packet['witness_H'],f
for row in collation_confirmation:
    assert row['C']=='[no witness]' or row['C'] in packet['witness_C'],row
    assert row['H']=='[no witness]' or row['H'] in packet['witness_H'],row
    assert row['reading'] in candidate,row
assert {d['id'] for d in report['decisions']} == {m['id'] for m in packet['marks']}
for crop in viewed: assert (WORK/crop).is_file(),crop
assert candidate.count(r'\unsure{à|:}') == 2
assert candidate.count(r'\scanpage{') == candidate.count(r'\mspage{') == 1
depth=0
i=0
while i<len(candidate):
    char=candidate[i]
    if char=='%':
        end=candidate.find('\n',i)
        i=len(candidate) if end<0 else end+1
        continue
    if char=='\\':
        i+=1
        if i<len(candidate) and candidate[i].isalpha():
            while i<len(candidate) and candidate[i].isalpha():i+=1
        else:i+=1
        continue
    if char=='{':depth+=1
    if char=='}':
        depth-=1
        assert depth>=0
    i+=1
assert depth==0
stack=[]
for match in re.finditer(r'\\(begin|end)\{([^{}]+)\}',candidate):
    if match.group(1)=='begin':stack.append(match.group(2))
    else:assert stack.pop()==match.group(2)
assert not stack
assert page_path.read_text()==accepted and prior_path.read_bytes()==prior_bytes
report['validation']={'literal_C_H_excerpts':'passed','literal_before_after':'passed','original_MARKS_coverage':'passed','balanced_braces_and_environments':'passed','existing_crop_paths':'passed','accepted_files_unchanged':'passed','tex_compilation':'not performed','new_crops_or_recrops':'none','ocr_or_external_research':'not performed'}
tex_out=WORK/'reviews'/f'{KEY}_auditC.tex'
json_out=WORK/'reviews'/f'{KEY}_auditC.json'
tex_out.write_text(candidate)
json_out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'tex':str(tex_out),'report':str(json_out),'counts':report['counts'],'validation':report['validation']},ensure_ascii=False,indent=2))
