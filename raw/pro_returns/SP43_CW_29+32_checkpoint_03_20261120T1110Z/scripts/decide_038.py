"""Main reader's explicit adjudication of scan 29/038, after crop inspection."""
from pathlib import Path
import json, copy
O=Path(__file__).resolve().parents[1]; s='C29-04_29_scan038'
r=json.loads((O/'readers'/s/'r1/report.json').read_text())
raw={d['id']:d for d in r['differences']}
ov={}
def change(k,**kw):
    ov.setdefault(k,{}).update(kw)
def readers(k,a,b,c): change(k,readers={'r1':a,'r2':b,'r3':c})
replacement=[
 ("% The second insertion's words are clear; its surrounding \\unsure marks attachment uncertainty only.\n",''),
 (r'\unsure{\inserted{locally(for étale topology)}}',r'\inserted{locally(for étale topology)}'),
 (r'\unsure{geometric}',r'\unsure{geometri}'),
 (r'\unsure{systems}',r'systems'),
 (r'\deleted{\unsure{r|-}}',r'\deleted{\unsure{-|r}}'),
 (r'\unsure{reallization|realization}',r're\unsure{l|a}\unsure{l|a}ization')]
change('D05',reading=r'what it means, \inserted{locally(for étale topology)} for',diff_C=False,evidence='The raised phrase begins above the end of means and its comma and extends over for; its closing parenthesis has no following comma. Immediate spatial attachment after means, is supported. Absence of a caret alone does not make this placement indeterminate.',confidence='medium')
readers('D05',r'means, \unsure{\inserted{locally(for étale topology)}} for',r'means, \inserted{locally(for étale topology)} for',r'means, \inserted{locally(for étale topology)} for')
change('D07',reading=r'\unsure{geometri}',diff_C=True,evidence='The visible sequence ends geometri at the black right edge. No contour of a final c is inspectable. The final text records the visible fragment, with uncertainty for the clipped termination, rather than completing a word from context.',confidence='high')
readers('D07',r'\unsure{geometric}',r'\unsure{geometric}',r'\unsure{geometri}')
readers('D11',r'\deleted{classified}',r'\deleted{\unsure{classified}}',r'\deleted{classified}')
change('D11',evidence='The c-l-a-s-s-i-f-i-e-d sequence remains distinguishable under the x row, including the dotted i cells, e opening/bar and terminal d ascender; classified is readable despite cancellation.',confidence='medium')
change('D12',reading=r'\deleted{systems (}',diff_C=True,evidence='The cancelled span retains s-y-s-t, a low e loop/bar, faint but identifiable m shoulders, final s and an opening parenthesis. These support systems ( without a doubt mark.',confidence='medium')
readers('D12',r'\deleted{\unsure{systems} (}',r'\deleted{systems (}',r'\deleted{systems (}')
change('D15',reading=r'\deleted{\unsure{-|r}}',diff_C=True,evidence='A short central horizontal survives beneath the x; a small shoulder-like residual also permits r. The horizontal is more conspicuous, so the hyphen candidate comes first, without a claim about correction order.',confidence='low')
readers('D15',r'\deleted{\unsure{r|-}}',r'\deleted{\unsure{-|r}}',r'\deleted{\unsure{-|r}}')
change('D16',reading=r're\unsure{l|a}\unsure{l|a}ization',diff_C=True,evidence='There are eleven typewriter cells, not twelve. After re, two adjacent cells each retain a tall l-like stroke and lower a-like contours; the following ization is clear. Cellwise alternatives record that visible superposition without inserting an extra cell or deciding a correction chronology.',confidence='medium')
readers('D16',r'\unsure{reallization|realization}',r'\unsure{realization|relaization|rellization}',r'\unsure{reallization|realization}')
readers('D17',r'\unsure{\c{\u{G}}}alois',r'\unsure{\c{\u{G}}|G}alois',r'\c{\u{G}}alois')
change('D17',evidence='G has a detached upward-open curved mark above and a detached lower curled/tilde-like mark below. Bare G omits visible ink. The breve/cedilla representation is only approximate and remains marked as uncertain.',confidence='medium')
readers('D18',r'\unsure{pocal|local}',r'\unsure{pocal|local}',r'\unsure{local|pocal}')
readers('D21',r'\unsure{s|f}\unsure{o|i}rmulation',r'\unsure{s|f}\unsure{o|i}rmulation',r'\unsure{f|s}\unsure{o|i}rmulation')
change('D21',evidence='The first cell retains an s-like lower curve and f-like upper stem/crossbar. The second contains an o oval together with an i dot, stem and lower serif. Both cells are uncertain; their superposition does not establish which typing was earlier.',confidence='medium')
for k,name in [('D04','m01_way_end'),('D08','m02_quotes_dash'),('D23','m03_blank_relation'),('D24','m04_convevient')]:
    change(k,source=f'crops/{s}/{name}.png')
change('D08',reading="``\\unsure{geometri} realization'' ... faithful - not",evidence='Opening paired quote strokes are visible in reader crop c05; this main crop shows two closing raised strokes and a short one-cell hyphen after faithful. There are no guillemets or long dash. Clipping of the preceding word is separately recorded at D07.')
readers('D08',"``\\unsure{geometric} realization'' ... faithful - not","``\\unsure{geometric} realization'' ... faithful - not","``\\unsure{geometri} realization'' ... faithful - not")
add=[]
for n,place,reading,h,crop,evidence in [
 (25,'L2: colon after M',r'some $M$: it',r'some $M$ : it','m05_M_colon','The colon occupies the next typewriter cell after M; no blank cell separates them.'),
 (26,'L4: semicolon after way','way; and','way ; and','m06_way_semicolon','The semicolon immediately follows y; the word space is after the semicolon.'),
 (27,'L11: comma after Z_i',r'$Z_i$ ,',r'$Z_i$,','m07_Zi_comma','A blank typewriter interval is visible after the lower i and before the comma.'),
 (28,'L15: semicolon after H',r'under $H$;',r'under $H$ ;','m08_H_semicolon','The semicolon is in the cell immediately adjacent to H; no intervening blank cell.'),
 (29,'L16: comma after Hom quotient',r'$\operatorname{Hom}(G_i,H)/H$ ,',r'$\operatorname{Hom}(G_i,H)/H$,','m09_Hom_comma','One blank typewriter interval separates the final H from the comma.')]:
    add.append(dict(id=f'D{n:02}',place=place,C=reading,H=h,reading=reading,diff_C=False,diff_H=True,kind='other',marked_in_H='no',evidence=evidence,source=f'crops/{s}/{crop}.png',confidence='high',mathematical=False,readers={x:reading for x in ['r1','r2','r3']}))
cd=copy.deepcopy(r['c_doubts'])
updates={
 'Interline above L2: second insertion anchor':('resolved',ov['D05']['reading'],'D05'),
 'L8 right edge: geometric':('changed',ov['D07']['reading'],'D07'),
 'L12: cancelled systems':('resolved',ov['D12']['reading'],'D12'),
 'L18: cancelled r or hyphen':('changed',ov['D15']['reading'],'D15'),
 'L18: reallization/realization':('changed',ov['D16']['reading'],'D16')}
for d in cd:
    if d['place'] in updates:
        status,reading,k=updates[d['place']];d.update(status=status,reading=reading,evidence=ov[k]['evidence'],confidence=ov[k]['confidence'])
    if d['place'].startswith('L23: blank'):d.update(source=f'crops/{s}/m03_blank_relation.png',evidence='The main crop confirms a wholly blank interval; the raised prime and final comma are distinct, and no inequality is present.')
un=[]
for u0 in r['unresolved']:
    u=copy.deepcopy(u0)
    if u['id'] in ['U01','U05']:continue
    links={'U03':'D07','U06':'D15','U07':'D16'}
    if u['id'] in links:
        d=ov[links[u['id']]];u.update(reading=d['reading'],evidence=d['evidence'],confidence=d['confidence'])
    if u['id']=='U03':u['alternatives']=['visible geometri fragment; terminal ink beyond the scan cannot be recovered']
    if u['id']=='U06':u['alternatives']=['-','r']
    if u['id']=='U07':u['alternatives']=['two separately mixed l/a cells after re; no correction chronology assigned']
    un.append(u)
inv=copy.deepcopy(r['inventory'])
for row in inv:
    if row['element']=='L08':row['first_words_or_objects']='condition (This description makes a sense whenever the functor "geometri [right edge clipped]'
    if row['element']=='L18':row['first_words_or_objects']='"geometric[hyphen/r deleted]re[l/a][l/a]ization -functor" to be fully faithful on the category'
    if row['element']=='X05':row['first_words_or_objects']='hyphen or r between geometric and re[l/a][l/a]ization'
# The detached marks on the G are an independently inventoried visible addition.
gmark=dict(scan='29/038',sheet_kind='typescript',hand='another unnamed hand',element='I03',kind='insertion',position='L19, above and below initial G; x285–321, y1441–1514',first_words_or_objects='Detached upper breve-like and lower curled marks around G; technique/maker not identified',transcribed='yes')
at=next(i for i,x in enumerate(inv) if x['element']=='L19');inv.insert(at+1,gmark)
checks=[]
for rid in ['r1','r2']:
    rr=json.loads((O/'readers'/s/rid/'report.json').read_text())
    for x in rr['checks']:
        checks.append(dict(statement_id='29.038.N1.torsor-actions',date='2026-11-20',who=f'GPT-6 Astra Pro; effort inherited, not exposed; independent reader /root/p038_{rid}',type=x['type'],outcome=x['outcome']+f' Evidence: readers/{s}/{rid}/report.json.'))
mc=[str(p.relative_to(O)) for p in sorted((O/'crops'/s).glob('*.png'))]
rv=[str(p.relative_to(O)) for p in sorted((O/'readers'/s/'r1/crops').glob('*.png'))]
data=dict(stem=s,base='r1',brief='brief_v03.md',agents={r:'/root/p038_'+r for r in ['r1','r2','r3']},replacements=replacement,overrides=ov,add_differences=add,c_doubts=cd,unresolved=un,inventory=inv,checks=checks,main_crops=mc,main_views=rv+mc,
 notes='Typescript continuation: 26 baseline lines in two paragraphs, two interlinear clauses, six cancellation locations (five spans), a separately underlined R, detached marks around G, and archive number 37. No title, date, signature, authorial pagination, display, diagram or drawing. The page describes local inertia representations and compatibility for coverings; states an analogous description of Galois coverings by commuting G_i/H actions with E an H-torsor; gives Hom(G_i,H)/H; and claims an étale-local reduction of a full-faithfulness criterion. The final paragraph acknowledges the Kummer example 3 and explicitly names divisibility as the intended order. The mixed G/H cell and the n-prime/n interval were checked because of this mathematical context; the context did not settle either glyph. The latter interval is blank, so H’s inequality is removed. N1: the algebraic classification of commuting actions on a nonempty right H-torsor was directly checked by the main reader and independently by readers 1 and 2; choose a base point to obtain a homomorphism, and change the point to conjugate it. Finite E forces finite H. These limited checks do not verify the geometric category equivalence, the unprovided criterion or the interpretation of example 3. Proof record: adjudication_inputs/29_038_mathematical_check.md and CHECK_EVENTS.tsv. Literal makes a sense, stricly and convevient are preserved; interior automorphism remains singular. There is no written question mark or explicit authorial doubt annotation. Reader doubt remains on mixed cells, approximate extra marks and clipping. The second quoted word has eleven cells; two separate mixed cells are represented without the twelfth letter implicit in reallization. The right-clipped first geometric is recorded as visible geometri, without completing invisible ink. The first insertion follows E.; the second follows means, by immediate spatial alignment; no caret is present. No external research or LaTeX compilation was used.',
 slips=['makes a sense; stricly; convevient; interior automorphism (singular); mixed typewriter cells preserved without correction chronology.'],
 abbreviations=[dict(form='i.e.',expansion='id est / that is',evidence='29/038 L7'),dict(form='mod.',expansion='modulo',evidence='29/038 L16')],
 adjudication='All three readings and inventories compared; 29 local difference records adjudicated using 17 existing reader crops and nine new main crops, 26 effective crop inspections total. All 19 C questions accounted for. Two images accompanied by a large text response overflowed the available context; neither was relied on, and the same two files were redisplayed alone, without recropping. Reader files remain unchanged. The separate inventory row for the exterior G marks supplements all reader inventories.')
(O/'adjudication_inputs'/f'{s}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Wrote explicit decisions:',s)
