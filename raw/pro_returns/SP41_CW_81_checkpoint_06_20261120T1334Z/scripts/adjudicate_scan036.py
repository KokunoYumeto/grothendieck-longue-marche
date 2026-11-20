"""Main-reader scan036 adjudication after all texts, returns and local crops."""
from pathlib import Path
import copy, json, re, datetime

w = Path(__file__).resolve().parents[1]
rs = [json.loads((w / f'readers/scan036/R{k}/return.json').read_text()) for k in (1, 2, 3)]
lookups = [{f['id']: f for f in r['findings']} for r in rs]
obs_text = (w / 'decisions/scan036_main_observations.md').read_text()
obs = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r'^([0-9]+)\. (.*?)(?=\n[0-9]+\. |\n\nThese decisions|\Z)', obs_text, re.M | re.S)}
map_r1 = [1, None, 22, 2, 3, 23, 4, 26, 28, 5, 29, 6, 6, 7, 8, 30, 31, 9, 10, 11, 12, 13, 14, 32, 15, 33, 16, 17, 18, 19, 20, 21]
map_r3 = [1, None, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 13, 14, 15, 16, 33, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
observation = [1, None, 2, 3, 3, 5, 6, 7, 8, 9, 10, 11, 11, 12, 13, 13, 14, 15, 15, 16, 16, 17, 17, 18, 18, 18, 19, 20, 19, 20, 20, 20]

def fid(k, n):
    return f'scan036-R{k}-F{n:02d}' if k == 3 else f'scan036-R{k}-F{n:03d}'

def add_reader(f, k, n, text=None):
    if n is None:
        f['readers'][f'R{k}'] = text
        f['reader_source_ids'][f'R{k}'] = ['reading.tex, same locus']
    else:
        source = lookups[k - 1][fid(k, n)]
        f['readers'][f'R{k}'] = source['reading']
        f['reader_source_ids'][f'R{k}'] = [source['id']]

d = {'scan': 36, 'folder': 'J81-05', 'their_page': 35, 'hua_has': 'text',
     'filename': 'J81-05_81_scan036.tex', 'status': 'decided', 'findings': []}
for i, raw in enumerate(rs[1]['findings'], 1):
    f = copy.deepcopy(raw)
    f['id'] = f'SP41-036-{i:03d}'
    f['readers'] = {}
    f['reader_source_ids'] = {}
    add_reader(f, 1, map_r1[i - 1], '$(18)$')
    add_reader(f, 2, i)
    add_reader(f, 3, map_r3[i - 1], '$(18)$')
    f['marked_in_H'] = 'yes' if f['marked_in_H'] else 'no'
    if f.get('crop'):
        f['crop'] = str(Path(f['crop']).relative_to(w))
    else:
        f['crop'] = ''
    if observation[i - 1]:
        f['evidence'] = 'Main reader, personally viewed local crop(s): ' + obs[observation[i - 1]]
    else:
        f['evidence'] = 'All three complete texts read (18). R1 and R3 notes and R2 finding explicitly report the upright 1 and two-loop 8 seen in their independent half readings. The main reader did not open the whole or half; this agreed reading adds no witness-change row.'
    f['main_adjudication'] = 'All three complete texts and all detailed returns, inventories, notes and metadata compared; see decisions/scan036_main_observations.md.'
    if not f.get('c_doubt_ids'):
        f['c_doubt_status'] = 'none'
    if i == 1:
        f['kind'] = r'readable ink left as \ill{}'
    if i == 3:
        f.update(crop='crops/scan036/main_ce_propos.png', bbox=[732,333,1272,442])
    if i in (4,5,6):
        f['crop'] = 'readers/scan036/R3/crops/02_hypothese_definition.png'
    if i == 5:
        f.update(reading=r'\deleted{\unsure{étant}}', against_C=False, c_doubt_status='retained', confidence='medium')
    if i == 7:
        f['reading'] = r'\unsure{\Sigma|\Sigma_2}^{+}'
        f['evidence'] += ' The superscript uncertainty is separately recorded at SP41-036-034. Factoring the common plus maps C’s ordered alternatives (Sigma-plus, Sigma2-plus) to (Sigma, Sigma2) with the same appended plus; appending the plus is the inverse map. That exact factoring adds no C editing count.'
    if i == 8:
        f.update(reading=r'\Sigma_1^+\unsure{\ne|=}\Sigma_2^-', bbox=[688,1051,733,1135])
        f['place'] = 'First comparison in (***) a)'
        f['consequential'] = 'The first relation retains a visibly crossed sign as ne first, with equality and final revision state still open. S’s proposed equality is not substituted.'
    if i == 9:
        f.update(crop='crops/scan036/main_shared_brace.png', bbox=[520,1030,850,1245])
    if i == 11:
        f.update(reading=r'\inserted{\unsure{-|a}), b)}', against_C=True, confidence='medium', crop='readers/scan036/R3/crops/06_relations_envisagees.png')
    if i == 12:
        f['confidence'] = 'medium'
    if i == 14:
        f['consequential'] = 'The extra low 2-shaped remnant after the live 1 is represented, with its cancellation state unresolved; H gives only 1.'
    if i == 18:
        f['kind'] = 'misread word'
    if i == 21:
        f.update(reading=r'\unsure{\deleted{E}}\Sigma_{12}', against_C=True, crop='readers/scan036/R3/crops/09_lower_right_revision.png')
    if i == 26:
        f.update(crop='crops/scan036/main_pas_lun.png', bbox=[1280,2010,1667,2115])
    if i == 30:
        f.update(reading=r'\unsure{du|des|de}', against_C=True)
    d['findings'].append(f)

def extra(number, k, source_number, mapping, evidence, **updates):
    f = copy.deepcopy(lookups[k - 1][fid(k, source_number)])
    f['id'] = f'SP41-036-{number:03d}'
    f['readers'] = {}
    f['reader_source_ids'] = {}
    for rk, (rn, text) in mapping.items():
        add_reader(f, rk, rn, text)
    f['marked_in_H'] = 'yes' if f['marked_in_H'] else 'no'
    f['crop'] = str(Path(f['crop']).relative_to(w)) if f.get('crop') else ''
    f['evidence'] = 'Main reader, personally viewed local crop(s): ' + evidence
    f['main_adjudication'] = 'All three complete texts and detailed returns compared; each source ID or exact-text locus is recorded.'
    f.update(updates)
    d['findings'].append(f)

extra(33, 1, 24, {1:(24,None),2:(None,r'\Pi_1'),3:(5,None)}, obs[4], crop='readers/scan036/R3/crops/02_hypothese_definition.png')
extra(34, 1, 25, {1:(25,None),2:(7,None),3:(7,None)}, obs[6], crop='readers/scan036/R2/02_second_sigma.png')
extra(35, 3, 9, {1:(27,None),2:(8,None),3:(9,None)}, obs[7], crop='readers/scan036/R2/03_row_a_relations.png', consequential='The second a) relation also retains ne first with equality and final revision state open; its exact witness strings are recorded separately from the first sign.')
extra(36, 3, 32, {1:(None,'à'),2:(None,'à'),3:(32,None)}, obs[20], crop='readers/scan036/R2/11_bottom_band.png')
extra(37, 1, 34, {1:(34,None),2:(None,r'$E_1=\Sigma_{12}$, on aurait'),3:(None,r'$E_1=\Sigma_{12}$, on aurait')}, 'The complete long curved comma follows the low 2 and drops below its baseline at the right margin. R1’s crop 09 retains its endpoint. All three complete texts include it. The exact H string has no comma at this position.', crop='readers/scan036/R1/crops/09_lower_revision_right.png')

# Every raw candidate has an explicit correspondence in the final record.
coverage = {}
for k in (1,2,3):
    used = {v for f in d['findings'] for v in f['reader_source_ids'][f'R{k}'] if v.startswith('scan036-')}
    expected = set(lookups[k - 1])
    assert used == expected, (k, expected - used, used - expected)
    coverage[f'R{k}'] = {'raw_findings':len(expected),'mapped_findings':len(used),'all_mapped':True}
d['reader_finding_coverage'] = coverage

d['inventory'] = copy.deepcopy(rs[0]['inventory'])
for e in d['inventory']:
    if e['element'] == 'raised-case-labels':
        e['first_words_or_objects'] = r'\unsure{-|a}), b)'
    if e['element'] == 'older-E-beneath-Sigma12':
        e['first_words_or_objects'] = r'\unsure{\deleted{E}}\Sigma_{12}'
    if e['element'] == 'clipped-final-sentence':
        e['first_words_or_objects'] = 'auquel cas le cardinal du/des/de … est égal :/à trois'

d['unresolved'] = copy.deepcopy(rs[1]['unresolved'])
for u in d['unresolved']:
    if u['place'] == 'Final line after cardinal':
        u['alternatives'] = ['des','de']
    if u['place'] == 'Old capital before live Sigma12':
        u['reading'] = r'\deleted{E}'
        u['alternatives'] = ['reinforcement or another older glyph; identity and state uncertain']
        u['reason'] = obs[16]
d['unresolved'].extend([
    {'place':'Cancelled étant','reading':'étant','alternatives':[],'confidence':'medium','reason':obs[3]},
    {'place':'First cancelled Pi','reading':r'\Pi','alternatives':[r'\pi'],'confidence':'medium','reason':obs[4]},
    {'place':'High sign after the second Sigma in puisque','reading':'+','alternatives':[r'\top'],'confidence':'medium','reason':obs[6]},
    {'place':'First raised branch reference','reading':'-','alternatives':['a'],'confidence':'medium','reason':obs[10]},
    {'place':'Separator after égal at the clipped edge','reading':':','alternatives':['à'],'confidence':'low','reason':obs[20]}
])
d['notation'] = [{'scan':36,'form':f['place'],'evidence':f['evidence'],'reading':f['reading']} for f in d['findings'] if int(f['id'].split('-')[-1]) in [7,8,10,11,14,15,16,19,21,24,25,27,28,29,31,33,34,35,36]]
d['abbreviations'] = copy.deepcopy(rs[1]['abbreviations'])
note_texts = [
    'This handwritten continuation has six mathematical display groups and a pencil archive number 35. No independent drawing, diagram, date, separate author page number, author question mark or verification instruction was observed. Proposition is the underlined internal heading. The formula labels are (*) through (****) and rewritten (20).',
    'The opening refers to the ens. (18), gives cardinal 4 and lists the four signed Sigma expressions. All three readers report the reference as 18 from their half readings. The prose reads A ce propos notons. Cancelled hypothèse and the following parenthesis are replaced by the interlinear définition. The cancelled ending étant retains uncertainty.',
    'After (*) and (**), the source describes the parts as disjointes and separately underlines non and vides. The second prose Sigma has no securely separate lower numeral, and its compact high sign retains plus/top uncertainty. The source refers to diagramme (14), without drawing that diagram on this sheet.',
    'In (***) a), both comparisons carry long, densely retraced crossing strokes. The text retains ne first and equality as an alternative at each sign; their final revision order remains open. The b) arrow retains uncertainty about its detached curved left head. The source then states that the two relations cannot hold simultaneously and cites (16) (c). This records the source argument without an independent proof check.',
    'S SA01-K81-05 records the crossed a) forms and proposes equalities. Its row identifies a reader who viewed no scan; the accompanying sweep narrative says that the later crop missed (***). The present local crop confirms the crossed visible forms, qualified by final-state uncertainty. S’s proposed equalities are not adopted as the diplomatic first reading. No claim about the validity of the proposed mathematical repair is made.',
    'In (****), the first right index has a clear 1 followed by a 2-shaped mark whose cancellation state remains open. The next capital has a readable live Sigma and additional crossed material retained as possible older X/E. Its live Sigma doubt is resolved without discarding the older layer. The source ends the display with i.e. Sigma12=X.',
    'The lower paragraph begins Ce cas and contains a cancelled phrase, the added Car/car si on avait en = temps, a cancelled equation and an uncertain older E under the next Sigma12. The two strokes of the written = are retained as an abbreviation. The older de/et and live ce before qui contredit (3) remain merged. A comma after the preceding live E1=Sigma12 is retained; H omits it.',
    'The proposition begins with capital Card and directly writes pas l’un. Its three displayed labels are a), a-prime), b); the first remains overtraced. The b) parenthesis begins d’où, now resolved. The label 20 retains an uncertain older 19/20; H acknowledges rewriting but does not give the older candidate. The closing line is physically cut and retains du/des/de, the brace/angular-mark alternatives, colon/à and trois.',
    'All twenty-one C doubt IDs have decisions: four resolved and seventeen retained. The complete text contains twenty-four local uncertainty macros, with twenty-four unresolved loci in the doubts record. All three complete texts and detailed returns, including inventories and workflow metadata, were compared. The main reader inspected eighteen local crops. These are source-account and ink-comparison notes; no mathematical proof check, OCR, external research or compilation was performed.'
]
d['notes'] = [{'id':f'scan036-note-{i:02d}','text':t} for i,t in enumerate(note_texts,1)]
d['check_events'] = [{'statement_id':n['id'],'date':'2026-11-20','who':'GPT-6 Astra Pro; inherited effort not exposed; main reader scan036','type':'carried as background without fault found','outcome':'Source-account and local ink/witness comparison only; no independent mathematical verification is claimed.'} for n in d['notes']]
d['sweep'] = [{'id':'SA01-K81-05 / 81/36','s':"Reported (***) a): (Sigma1-plus != Sigma2-minus) iff E1 != Sigma12; proposed correction uses equality at both places. The row’s decided_by states no scan viewed.",'decision':'The visibly crossed forms are confirmed as the first readings, with equality retained and revision order unresolved. The proposed equalities are not adopted as the diplomatic first reading.','evidence':'Main reader personally viewed readers/scan036/R2/03_row_a_relations.png. Both pairs of horizontal bars have extended, heavily retraced diagonal crossings. The sweep narrative itself says its crop missed (***).'}]
d['main_crop_views'] = {'R1':[9],'R2':list(range(1,12)),'R3':[2,6,9],'main_new':3,'total':18}
d['crop_counts'] = {'R1':11,'R2':11,'R3':14,'main':3,'total':39}
d['decided_utc'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
t = (w / 'decisions/drafts/scan036_main_draft.tex').read_text()
assert t.count(r'\unsure{') == 24
assert len(d['unresolved']) == 24
(w / 'pages' / d['filename']).write_text(t)
(w / 'decisions/scan036.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
print(json.dumps({'findings':len(d['findings']),'against_C':sum(f['against_C'] for f in d['findings']),'against_H':sum(f['against_H'] for f in d['findings']),'unresolved':len(d['unresolved']),'reader_coverage':coverage}))
