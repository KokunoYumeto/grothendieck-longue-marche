"""Crop-adjudicated scan015 decisions. Never rerun after commitment."""
import copy,json,re
from pathlib import Path
O=Path(__file__).resolve().parents[1]
p=O/'decisions/scan015.json'
if p.exists() and json.loads(p.read_text()).get('committed'):raise SystemExit('Already committed')
rs=[json.loads((O/f'readers/scan015/R{i}/report.json').read_text()) for i in range(1,4)]
a,b,c=[r['differences'] for r in rs]
rows=[]
for i,x in enumerate(b):
    r=copy.deepcopy(x);r['final']=r.pop('reading');r['mathematical']=False
    for k in ['crop_box','crop_source']:r.pop(k,None)
    r['readers']={'R1':a[i if i<29 else i-1]['reading'] if i!=29 else 'Canceled (1.32) attached to the Fig display; recognized in text, no separate discrepancy row.',
                  'R2':x['reading'],'R3':c[i if i<4 else i+1]['reading']}
    rows.append(r)
def rp(reader,name):return f'readers/scan015/{reader}/crops/{name}.jpg'
def main(name):return f'main_crops/scan015/{name}.jpg'
def put(i,**kw):rows[i].update(kw)
viewnotes={}
notes=(O/'working/scan015_main_crop_notes.md').read_text()
for rel,body in re.findall(r'^## \d+ — ([^\n]+)\n\n(.*?)(?=\n## |\Z)',notes,re.M|re.S):
    viewnotes[rel]=re.sub(r'^Recorded [^.]+\. ','',body.strip())
def evidence(i,crop,extra=''):
    put(i,crop=crop,evidence=viewnotes[crop]+(' '+extra if extra else ''))
evidence(0,rp('R3','01_opening_family_F'))
evidence(1,main('01_opening_de'))
for i in [2,3,4]:evidence(i,main('02_frame_gloss'))
put(3,against_H=False,evidence='The brace starts below the comma, to the right of the first relation sign, and extends under the start of telles. Its high cusp is near its right half. The gloss is below it. C centers the annotation under the relation pair; H explicitly describes the below-signs brace and is credited. Its typesetting of the gloss in-line is an editorial representation change, not an omitted annotation. The open-frame difference is recorded separately.')
for i in [5,6]:evidence(i,rp('R3','02_definit_and_cancelled_capital'))
for i in [7,8]:evidence(i,rp('R3','03_first_live_M'))
evidence(9,rp('R2','04_avec'))
for i in [10,11]:evidence(i,main('03_order_M_pair'))
for i in [12,13]:evidence(i,rp('R3','04_family_order_indices'))
put(13,final=r'\underset{\unsure{\mathcal{F}|\overline{f}}}{\ll}',against_C=False,confidence='medium')
evidence(14,main('04_second_inclusion'))
evidence(15,rp('R3','05_reference_after_L'))
put(15,mathematical='The literal reference is (1.25), resolving C’s 6/5 doubt to 5; the earlier L definition is labeled (1.26), but the reference is not silently corrected.')
evidence(16,main('05_first_domain_F'))
for i in [17,18]:evidence(i,rp('R2','07_powerset_first'))
evidence(19,rp('R3','08_cancelled_X_first_map'))
put(19,final=r'\mathord{\rlap{$\deleted{X}$}F}',against_H=False,
    mathematical='C’s doubtful first mapped-input X is now readable as a canceled X beneath live F; H’s explicit note is credited.')
evidence(20,rp('R3','09_deployment_operator'))
put(20,mathematical='The named operator is literally Dep, resolving C’s Dep/Def doubt and differing from H’s Dépl; no accent or final l is visible.')
for i in [21,22]:evidence(i,rp('R3','10_insertion_and_definie'))
evidence(23,main('06_definition_M'))
evidence(24,main('07_second_domain_F'))
evidence(25,main('08_second_target_M'))
evidence(26,rp('R3','12_cancelled_X_second_map'))
put(26,final=r'\unsure{F|\deleted{F}|\mathord{\rlap{$\deleted{X}$}F}}',
    mathematical='The second mapped input does not establish a complete earlier X. Preserve three alternatives: live F, canceled F, or canceled X overlapped by live F. Neither witness’s certain state is adopted.')
evidence(27,main('09_second_image_subscript_M'))
evidence(28,rp('R2','12_colon_after_14'))
for i in [29,30,31,32,33]:evidence(i,main('10_figure_definition_block'))
evidence(34,main('11_concluding_F'))
evidence(35,main('12_concluding_M'))
evidence(36,rp('R3','13_s_interprete'))
for i,r in enumerate(rows,1):r['id']=f'015-{i:02}'
parentheses=dict(place='H parentheses surrounding the gloss in (1.30)',
    readers={'R1':'No parentheses in reading.tex','R2':'No parentheses in reading.tex; no discrepancy row','R3':c[4]['reading']},
    final='No parentheses in diplomatic text; H’s supplied inline grouping is an editorial representation, excluded from substantive H-error counts.',
    crop=main('02_frame_gloss'),
    evidence='The already-inspected frame/gloss crop shows rel. d’ordre dans F without enclosing parentheses. H’s explicit note gives the words under the relation signs with a brace, and therefore explains its parenthesized inline group as editorial representation. R3-D05 is adjudicated here, not ignored or treated as an omitted gloss.')
tex=(O/'readers/scan015/R3/reading.tex').read_text()
assert 'par (1.20), avec les relations' in tex
tex=tex.replace('par (1.20), avec les relations',r'par (1.20), \unsure{avec} les relations')
assert r'\unsure{F|\deleted{X}F}' in tex
tex=tex.replace(r'\unsure{F|\deleted{X}F}',rows[26]['final'])
tex=tex.replace('% At the second map an extra diagonal crosses F; a canceled X is possible, not established.',
    '% At the second map an extra diagonal crosses F; live F, canceled F, and X overwritten by F remain possible.')
(O/'decisions/scan015_final.tex').write_text(tex)
cd=copy.deepcopy(rs[2]['c_doubts'])
links=[0,5,6,13,15,17,19,20,22,26,36]
for j,i in enumerate(links):
    r=rows[i]
    cd[j].update(reading=r['final'],evidence=r['evidence'],crop=r['crop'],disposition='resolved' if j in [1,2,4,6,7,8] else 'retained')
    if j==2:cd[j]['evidence']+=' The letter-identity doubt M/F is resolved; the distinct exact-alphabet uncertainty cal M/M remains.'
    for k in ['crop_box','crop_source']:cd[j].pop(k,None)
inv=copy.deepcopy(rs[2]['inventory'])
inv[14]['first_words_or_objects']+='; star retraced, no independently readable predecessor'
inv[20]['first_words_or_objects']+='; double star retraced, no independently readable predecessor'
inv[21]['first_words_or_objects']='Extra diagonal at F: live F, canceled F, or canceled X overlapped by live F; state explicitly uncertain'
inv.insert(16,dict(element='Live replacement F over first input X',kind='insertion',position='same position as the canceled X, x=1103–1148, y=1156–1210',first_words_or_objects='F superimposed on canceled X',sheet_kind='text',hand='his hand',transcribed='yes'))
notes=dict(content=' '.join(rs[2]['notes']['content']),
 math_reading_decisions=[
 'Eight family-F occurrences, thirteen M occurrences including the canceled M, and two power-set P occurrences have individual evidence rows. Their exact typeface uncertainties are marked at the first occurrence; ordinary F/G operands are not normalized to family letters.',
 'The four relation labels sit centered below their signs; the Fig subscripts sit lower right. The frame has three separate edges, two left gaps and no visible right vertical. Its brace and unparenthesized gloss are shifted right, and are drawn in TikZ.',
 'The literal reference is (1.25), although already committed scan013 labels its L definition (1.26). The local digit has an open lower return, not the loop of 6; the reference is retained without emendation.',
 'The first canceled input X is readable beneath F. The second input has only one separately recoverable diagonal, leaving live F, canceled F, and overwritten X/F alternatives. The star labels are retraced but have no independently readable predecessor.',
 'Dep has a p descender and no independent acute or final l. The prose has unaccented definit and definie, inserted alors, and a colon after (1.4). The final verb’s accent remains uncertain.',
 'Main actually proved the forward inclusion from (1.31), assuming transitivity of ≤: if F≤G and X∈tilde F then X≤F≤G, hence X∈tilde G. The reverse implication and the two asserted hook arrows were not proved from atelier axioms. This limited check never licenses changing the written equivalence.',
 'H’s explicit notes are credited for the below-signs brace, the first canceled X, and the retraced star labels. Its parentheses around the inline gloss are treated as supplied editorial grouping. Its joining of the two lower definitions is line wrapping, not a substantive reading difference. Its canceled (1.32), however, is attached to the prose baseline rather than the next display and is recorded as a placement difference.'
 ],author_doubts=[],
 titles_dates_counts='Manuscript page 14; live numbered labels (1.30), (1.31), final (1.32); earlier canceled (1.32); markers (*) and (**); references (1.20), (1.25) and (1.4). No independent title, calendar date, page count, archive pencil number, marginal note, or authorial question/check phrase was identified. Two separate single underlines mark relations and d’ordre.')
events=[]
for i,r in enumerate(rs,1):
    for e in r['check_events']:events.append(dict(e,who=f'GPT-6 Astra Pro; effort not exposed; scan015 R{i}'))
for sid in ['scan015-(1.30)-order-data','scan015-M-L-reference-definitions','scan015-(*)-injectivity','scan015-(**)-figure-map','scan015-(1.32)-reverse-implication']:
    events.append(dict(statement_id=sid,type='carried as background without fault found',outcome='Read as the author’s assertion; no mathematical verification of this claim was performed.',who='GPT-6 Astra Pro; effort not exposed; main reader; scan015'))
events.append(dict(statement_id='scan015-(1.31)-monotonicity',type='targeted proof check',outcome='Assume ≤ is transitive. If F≤G and X belongs to tilde F={X in M:X≤F}, then X≤F≤G, so X belongs to tilde G. This proves only forward inclusion. No proof of the reverse implication, either asserted injectivity, or their hypotheses from atelier axioms was performed. Working note: working/scan015_math_checks.md.',who='GPT-6 Astra Pro; effort not exposed; main reader; scan015'))
un=[]
for i in [0,6,9,13,17,26,36]:
    r=rows[i]
    un.append(dict(place=r['place'],reading=r['final'],alternatives='As explicitly marked in the transcription; no further candidate securely recovered.',confidence=r['confidence'],evidence=r['evidence']))
d=dict(scan=15,mspage='14',folder='J156-6-02',filename='J156-6-02_156-6_scan015.tex',brief='v007',committed=False,adjudicated_all=True,
       differences=rows,adjudications=[parentheses],c_doubts=cd,s_rows=[],inventory=inv,notes=notes,check_events=events,unresolved=un,abbreviations=rs[2]['abbreviations'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('scan015 draft:',len(rows),'loci;',sum(r['against_C'] for r in rows),'against C;',sum(r['against_H'] for r in rows),'against H;',len(inv),'inventory;',len(un),'doubts')
