#!/usr/bin/env python3
"""Main adjudication of scan 030 after three independent returns and 16 crops."""
from pathlib import Path
import copy,json
R=Path(__file__).resolve().parents[1]
D={r:json.loads((R/f'readers/scan030/{r}/report.json').read_text()) for r in ('r1','r2','r3')}
tex=(R/'readers/scan030/r1/reading.tex').read_text()
repl=[
 ('SGA 4 XVI 1.1',r'SGA \unsure{\deleted{V}4|\deleted{4}V} XVI 1.1'),
 ('par là au th. de changement',r'par là au th.\unsure{\handwritten{,}} de changement'),
 (r"l'\unsure{\deleted{E}e|\deleted{e}E}nvers",r"l'\unsure{\(\mathbb{e}\)|\deleted{E}e|\deleted{e}E}nvers"),
 (r'\unsure{-} ce sera','- ce sera'),
 ('les rappels. Avant',r'les rappels\unsure{.} Avant'),
 ('les définitions, pour','les définitions; pour'),
 (r'\draw[line width=.25pt] (255,213)--(251,240);',r'\draw[line width=.25pt] (309,158)--(305,170);'+'\n'+r'\draw[line width=.25pt] (255,213)--(251,240);'),
 (r'\unsure{si on utilise}\\ailleurs',r'\unsure{si on utilise} \unsure{un|en|on}\\ailleurs'),
 (r'\draw[line width=.25pt] (990,31)--(988,77);','\n'.join(r'\draw[line width=.25pt] '+s for s in ['(990,27)--(990,34);','(989,39)--(989,45);','(989,49)--(988,60);','(988,64)--(988,70);','(988,75)--(988,80);']))
]
for a,b in repl:
    assert a in tex,a
    tex=tex.replace(a,b)
C=copy.deepcopy(D['r1']['changes'])
m2={0:0,1:0,2:1,3:2,4:4,5:5,6:6,7:7,8:10,9:9,10:9,11:13,12:14,13:15,14:16,16:17,17:17,18:19,19:19,20:18,21:18,22:18,23:20,24:21,25:22}
m3={0:0,1:0,2:1,3:2,4:4,5:5,6:7,7:8,8:10,9:13,10:14,11:15,12:16,13:17,14:18,16:19,17:19,18:21,19:21,20:20,21:20,22:20,23:22,24:23,25:24}
for i,c in enumerate(C):
    c['readers']={'r1':c['reading']}
    for r,m in [('r2',m2),('r3',m3)]:
        if i in m:c['readers'][r]=D[r]['changes'][m[i]]['reading']
    c['mathematical_consequence']=''
for r in ['r2','r3']:C[15]['readers'][r]='Closing parenthesis and terminal period drawn in the source row; period lies to the right of the bent cancellation boundary.'
def p1(s):return f'readers/scan030/r1/crops/{s}.jpg'
def p3(s):return f'readers/scan030/r3/crops/{s}.jpg'
def pm(s):return f'crops/scan030/{s}.jpg'
block=p1('03_cancelled_block');margin=p1('05_diagonal_margin');roman=p3('05_roman_correction')
paths={0:pm('01_top_reference'),1:pm('01_top_reference'),2:pm('02_hand_arrow'),3:pm('03_coherent_quotes'),4:pm('04_deleted_reference'),5:pm('05_corps_de_call'),6:pm('06_left_tick'),7:p3('03_envers'),8:block,9:block,10:block,11:block,12:block,13:block,14:block,15:block,16:block,17:pm('07_deleted_enonces'),18:roman,19:roman,20:margin,21:margin,22:margin,23:pm('08_end_parenthesis'),24:p1('06_final_cancelled_line'),25:p3('07_final_tail')}
ev={
0:'Main crop 01 shows handwritten XVI between distinct upper and lower oblique bars. H acknowledges the reference in a note but its emphasis does not reproduce these bars.',
1:'The same main crop locates SGA 4 and the barred XVI to the left and above the typed VII 2. The left-margin placement is retained explicitly.',
2:'Main crop 02 shows a thick, slightly wavering continuous shaft and pen-drawn right head between ordinary typed X and S. Its handwritten state is retained.',
3:'Main crop 03 shows two separate upright quote strokes at each end of cohérent, rather than angled guillemets.',
4:'Main crop 04 shows the grave-accented à and all digits and points of 2.1.5 beneath typed x cancellation. H expressly excludes machine cancellations from its scope; the row records that declared omission.',
5:'Main crop 05 shows typed corps de between rows and the curved call descending immediately before base in changement de base. It does not point after au cas du on the previous row. H marks its alternative attachment as reserved; main preserves the observed later attachment.',
6:'Main crop 06 shows the separate light curved stroke in the LEFT margin beside en main and just above Cela. Its low left end curves downward slightly before rising to the right; no arrowhead is supplied.',
7:'Main inspected r3 crop 03: displaced rounded counter/bar components support a repeated e, while an E/e overprint remains possible. Main includes the same-letter alternative as r2/r3 and retains both unlike-letter strike orders; the crop does not establish chronology.',
8:'The main cancellation crop shows a short horizontal stub preceding ce, distinct from the much longer crossing stroke. Main resolves a dash, agreeing with r2/r3 and C; no separate semicolon dot or tail is established there.',
9:'The main cancellation crop shows the stepped left boundary, long row strikes, lower/right return and four long obliques around the complete text. Main uses r1’s common-coordinate graphic with semantic deletion wrappers and suppressed automatic lines, and adds the faint short stroke beside the raised 1-/l- that r2 alone drew. The actual local underlines and insertion calls remain separate from the cancellation.',
10:'The enclosing boundary and long obliques cross Au lieu de pro-lisse, the lisse alternative, and the entire asphericity condition. H leaves most of that proposal live and strikes only the example. Main retains its cancelled state, as all three readers observed.',
11:'The enlarged interlinear line has a low t followed by a full-height capital H and a period. It stands above suffit/de supposer; the nearby call is drawn. Main keeps tH. and the physical placement without moving it to H’s end-of-condition position.',
12:'The raised typed stem has a short upper flag/serif, a lower foot and a following hyphen. The impression does not distinguish 1- from l- securely; C’s doubt is retained. The addition is not underlined.',
13:'Three separate lower strokes lie beneath localement, L and asphérique, with a gap beneath the intervening hyphen. Main adopts r1/r3’s separate spans; r2’s single L-asphérique underline bridges that gap. H’s italic emphasis is a different state.',
14:'The cancelled example has paired upright typewriter quote strokes at both boundaries. The literal three dots and H’s ellipsis code do not themselves count as a difference.',
15:'The terminal period is to the right of the bent cancellation boundary beside the closing parenthesis. It remains outside the deleted run; the crop does not justify extending the visible cancellation over that dot.',
16:'The same enlarged block shows the separate x-cancelled les after live D’autre part. H expressly omits machine cancellations.',
17:'Main crop 07 shows all letters and both acute accents of énoncés under typed x strokes before the literal 2.12. H expressly omits machine cancellations.',
18:'Main inspected r3 crop 05: IV and the separately added V each have both upper and lower bars. The curved call rises from beside the crossed typed numeral toward ou V. No unidentified earlier glyph under IV is reconstructed.',
19:'The same crop preserves an upper horizontal, short left descent and lower bowl supporting typed 5 beneath the pen cancellation. Main resolves 5 at medium confidence with r1/r3; r2 retains 6/5. The numeral remains outside the handwritten wrapper.',
20:'The note occupies the lower LEFT margin in five lines slanting upward to the right. Main inspected r1’s uniquely rotated crop and retains a rotated left-margin text node.',
21:'In the rotated main-viewed crop, the first phrase is clipped and compressed; si on utilise remains tentative. A separated short word follows utilise, omitted by r1/r3 but seen by r2; un/en/on remain possible. The next line supports ailleurs through its rounded initial, dotted i and paired tall l strokes. Only the clipped initial c of canonique remains uncertain; factorisation, d’un and champ are legible. H explicitly marks the differing lexical loci as doubtful or illegible.',
22:'The rotated crop shows opening quote strokes at the clipped edge, a clear closing pair after champ, and a separate comma. H’s neighbouring lexical uncertainties do not mark doubt on these omitted punctuation marks.',
23:'Main crop 08 shows the closing parenthesis near the sheet edge and no following period. H’s added final stop is not reproduced.',
24:'Main inspected r1 crop 06: the entire x-cancelled sentence survives, ending in a d with ascender and bowl. There is no following e. H describes the line with an abridged quotation and ellipsis under its declared machine-cancellation scope; main transcribes all surviving ink.',
25:'Main inspected r3 crop 07 for the separate lower mark: it consists of five dark near-vertical segments with gaps, rather than an unbroken rule. Main retains those segments beneath the final row in a shared coordinate system, with no numeral or arrow interpretation.'}
for i,c in enumerate(C):c.update(crop=paths[i],evidence=ev[i])
C[7]['reading']=r"l'\unsure{\(\mathbb{e}\)|\deleted{E}e|\deleted{e}E}nvers"
C[8].update(reading='- ce sera',diff_c=False,confidence='medium')
C[9]['reading']=tex[tex.index(r'\begingroup'):tex.index('% END cancellation graphic')].strip()
C[19]['confidence']='medium'
C[20]['reading']=tex[tex.index(r'\reversemarginpar',tex.index('% END cancellation graphic')):tex.index(r'\deleted{énoncés} 2.12')].strip()
C[21]['reading']=r"\unsure{si on utilise} \unsure{un|en|on}\\ailleurs la\\``factorisation\\\unsure{c}anonique d'un\\champ'',"
C[21]['confidence']='medium'
C[25]['reading']='\n'.join(line for line in tex[tex.index('% BEGIN final cancelled line'):].splitlines() if line.startswith(r'\draw'))
C[5]['mathematical_consequence']='The insertion call qualifies the later base-change expression with corps de; H attaches these words to the earlier au cas du clause. This is an observed attachment difference, not a verification of the reduction.'
C[10]['mathematical_consequence']='The proposed replacement of pro-lisse/lisse by the asphericity condition belongs to the cancelled text; H presents most of that proposal as live.'
# Add the five distinct loci not separately reported by r1.
extra=[]
for idx in [3,6,9,11,12]:
    c=copy.deepcopy(D['r3']['changes'][idx]);c['mathematical_consequence']=''
    c['readers']={'r3':c['reading']}
    if idx==3:
        c['readers'].update(r1='SGA 4 XVI 1.1',r2=D['r2']['changes'][3]['reading'])
        c.update(crop=p3('01_sga_reference'),evidence='Main inspected r3 crop 01: a V-like oblique and upper-left serif remain distinct from the 4 crossbar and stem. Main adopts r2/r3’s overprint, retaining both strike orders; r1 reads an ordinary 4.',confidence='medium')
    elif idx==6:
        c['readers'].update(r1='th. de changement',r2='th. de changement')
        c.update(crop=p3('02_th_punctuation'),evidence='Main inspected r3 crop 02: a dark comma-shaped head with a faint tail lies below and right of the typed period. Main retains the uncertain handwritten comma as r3; intentional punctuation versus incidental ink remains unresolved.',confidence='low')
    elif idx==9:
        c['readers'].update(r1=r'\inserted{\handwritten{cf texte joint}} above the start of ce sera in the common-coordinate graphic',r2=D['r2']['changes'][8]['reading'])
        c.update(crop=block,evidence='The handwritten cf texte joint is physically above the beginning of ce sera, following the peut-être boundary. All three graphics place it there. C attaches it at the end of the longer cancelled instruction; H’s placement matches the source.')
    elif idx==11:
        c['readers'].update(r1='rappels.',r2=D['r2']['changes'][11]['reading'])
        c.update(crop=block,evidence='A thick short oblique crosses the punctuation cell after rappels. A separate complete point cannot be isolated securely from the crossing stroke. Main retains r2/r3’s uncertain period; r1, C and H give it certain.',confidence='low')
    elif idx==12:
        c['readers'].update(r1='définitions,',r2=D['r2']['changes'][12]['reading'])
        c.update(crop=block,evidence='A separate upper dot is visible above the horizontal cancellation after définitions, with a lower comma tail below it. Main resolves a semicolon with r3; r1 has a comma and r2 retains semicolon/comma.',confidence='medium')
    extra.append(c)
# Physical order for the collation rows; nearby state rows remain distinct.
ordered=[]
for i,c in enumerate(C):
    ordered.append(c)
    if i==3:ordered.append(extra[0])
    if i==5:ordered.append(extra[1])
    if i==7:ordered.append(extra[2])
    if i==8:ordered.extend(extra[3:])
C=ordered
cd=copy.deepcopy(D['r2']['c_doubts'])
for q in cd:
    ids=q.get('c_mark_ids',[])
    if ids==['C001']:q.update(crop=p3('03_envers'),evidence=ev[7])
    elif ids==['C002']:q.update(crop=block,evidence=ev[12])
    elif ids==['C003']:q.update(decision='resolved',reading=r'\deleted{5}',crop=roman,evidence=ev[19])
    elif ids==['C004']:q.update(crop=margin,evidence='The initial phrase is clipped and compressed; si on utilise remains tentative. The separate following short word is retained independently as un/en/on.')
    elif ids==['C005']:q.update(crop=margin,evidence='Main agrees with r1/r2: the rounded initial, dotted i, paired tall l strokes and following cursive ending support ailleurs. r3 retains uncertainty.')
    elif ids==['C006']:q.update(crop=p1('06_final_cancelled_line'),evidence=ev[24])
    elif 'tH.' in q['locus']:q.update(crop=block,evidence=ev[11])
    elif '2.12' in q['locus']:q.update(crop=pm('07_deleted_enonces'),evidence='Main crop 07 confirms exactly 2.12: one point after 2 and none between 1 and 2; no reference is silently repaired.')
un=[
 {'locus':'First SGA reference, overprint','reading':extra[0]['reading'],'alternatives':[r'\deleted{V}4',r'\deleted{4}V'],'confidence':'medium','reason':'Both components survive; their chronological order is not established.'},
 {'locus':'After second th., low mark','reading':r'\unsure{\handwritten{,}}','alternatives':['Intentional handwritten comma','Incidental ink'],'confidence':'low','reason':'Comma-shaped head and faint tail are visible, but their intentional punctuation status is unresolved.'},
 {'locus':'Initial of envers','reading':r'\unsure{\(\mathbb{e}\)|\deleted{E}e|\deleted{e}E}','alternatives':[r'\mathbb{e}',r'\deleted{E}e',r'\deleted{e}E'],'confidence':'medium','reason':'Displaced rounded contours and a possible capital stem/bar do not establish the underlying letters or strike order uniquely.'},
 {'locus':'Period after cancelled rappels','reading':r'rappels\unsure{.}','alternatives':['.'],'confidence':'low','reason':'The short oblique cancellation obscures the stop cell.'},
 {'locus':'Raised addition above L-asphérique','reading':r'\unsure{1-|l-}','alternatives':['1-','l-'],'confidence':'medium','reason':'Upper flag/serif and lower foot are compatible with both impressions.'},
 {'locus':'First marginal phrase','reading':r'\unsure{si on utilise}','alternatives':['si on utilise'],'confidence':'medium','reason':'Initial clipping and compressed cursive leave the phrase tentative.'},
 {'locus':'Separated word after utilise','reading':r'\unsure{un|en|on}','alternatives':['un','en','on'],'confidence':'low','reason':'A separate short cursive word is visible; its rounded initial and final arch are not uniquely discriminated.'},
 {'locus':'Marginal canonique, initial only','reading':r'\unsure{c}anonique','alternatives':['canonique'],'confidence':'medium','reason':'The initial curve meets the physical sheet edge; following anonique is clear.'}
]
inv=copy.deepcopy(D['r2']['inventory'])
for q in inv:
    s=q['first_words_or_objects']
    if s=='6|5':q['first_words_or_objects']='Typed 5, resolved, cancelled by pen'
    if s.startswith('- ce sera'):q['first_words_or_objects']='- ce sera dans les rappels [period uncertain]. Avant même de donner ces'
    if 'définitions;|,' in s:q['first_words_or_objects']=s.replace('définitions;|,','définitions;')
    if s.startswith('Underlined localement'):q['first_words_or_objects']='Separate underlines beneath localement, L and asphérique; cancelled example, followed by live terminal period'
    if s=='Isolated vertical ink stroke':q['first_words_or_objects']='Five detached near-vertical ink segments'
idx=next(i for i,q in enumerate(inv) if q['first_words_or_objects']=='Light curved tick')
inv.insert(idx,{'sheet_kind':'letter','hand':'his hand','element':'new','kind':'insertion','position':'After the second th., low right of its typed stop','first_words_or_objects':'Uncertain handwritten comma-shaped mark','transcribed':'yes'})
idx=next(i for i,q in enumerate(inv) if q['first_words_or_objects']=='1-|l- with nearby fine call traces')
inv.insert(idx+1,{'sheet_kind':'letter','hand':'his hand','element':'new','kind':'drawing','position':'Beside raised 1-/l- and below L, within the cancellation graphic','first_words_or_objects':'Two separate fine short pen strokes','transcribed':'yes'})
for i,q in enumerate(inv,1):q['element']=f'030-{i:02d}'
notes=[
 {'id':'s030-note01','text':'Typescript letter-like sheet headed VII 2, with an upper-left SGA 4 XVI reference, handwritten corrections and marginal marks. No salutation, signature or date is present. The pencilled archive number 29 is retained only in a comment. H has a textual witness for page 29 and explicitly excludes machine x cancellations from its scope.','basis':'All three complete page readings and inventories; main top-reference crop.'},
 {'id':'s030-note02','text':'The first paragraph says that 2.1.1 reduces to affine X, calls affine X quasi-compact and quasi-separated, and relates the assertion to a base-change theorem and reductions through 2.1.5 and transcendence degree one. These reductions and the cited numbered theorem are reported as source assertions. Their complete statements are absent from this sheet, so they have not been verified here.','basis':'Unanimous first-paragraph wording, with local ink adjudications for the reference and insertion.'},
 {'id':'s030-note03','text':'The phrase et qui est essentiellement is an unfinished typed insertion and is not completed. The corps de call points before base in the later base-change phrase. The source says s’il ne l’est déjà and je n’ai pas les textes en main, expressly recording the writer’s uncertainty about whether 2.1.1 was already stated. It proposes a future presentation in a re-edition; the note does not establish what any edition eventually contained.','basis':'All three readings, prior C questions, and main corps de crop; documentary observation.'},
 {'id':'s030-note04','text':'The second paragraph proposes grouping 2.1.1 and 2.1.7 and treating 2.1.5 as a corollary. The following instruction and proposed pro-lisse/lisse replacement by an asphericity condition are cancelled within a stepped, obliquely crossed graphic. Their cancellation is preserved without inferring whether they were rejected mathematically or merely rewritten. The terminal example period lies outside the visible cancellation.','basis':'Main cancellation crop and all three full readings.'},
 {'id':'s030-note05','text':'The literal tH., 2.12 and il sont are retained. The initial dash and the semicolon after définitions are resolved from their separate strokes, while the stop after rappels and the raised 1-/l- remain uncertain. Main preserves three separate underlines and the two fine local pen traces rather than merging them with the cancellation outline.','basis':'Main cancellation and énoncés crops; explicit outcomes for prior C questions.'},
 {'id':'s030-note06','text':'The marginal note remains partly uncertain: si on utilise is tentative, a separate un/en/on follows, ailleurs is resolved, and only the clipped initial c of canonique is marked. Its quotes, final comma and diagonal left placement are retained. The lower reference has barred IV and an inserted barred V; its crossed typed numeral is resolved as 5. The cancelled final line ends with d and is not completed.','basis':'Main uniquely rotated margin crop, Roman-correction crop and final-line crop.'},
 {'id':'s030-note07','text':'The first SGA reference has V/4 overprint components with unresolved strike order. The envers initial may be repeated e or an E/e correction in either order. A small comma-shaped mark after the second th. is retained uncertainly, and the detached lower mark is drawn as five near-vertical segments without textual interpretation.','basis':'Main enlarged overprint, punctuation and lower-stroke crops; these are ink decisions, not mathematical corrections.'},
 {'id':'s030-note08','text':'A targeted check confirms the limited implication used in the opening: an affine scheme X=Spec A is quasi-compact and quasi-separated. Refining an open cover by principal opens gives elements generating the unit ideal, and a finite expression for 1 supplies a finite subcover. The absolute diagonal is induced by the surjective multiplication A tensor_Z A to A, hence is a closed immersion and quasi-compact. This checks only that implication, not any numbered reduction or base-change theorem in the letter.','basis':'Actual main-reader argument in decisions/scan030_math_work.md, connected to the unanimous observed opening sentence.','event_type':'targeted proof check','event_outcome':'Passed for affine X: finite principal-open subcover and closed absolute diagonal establish quasi-compactness and quasi-separatedness. No other source theorem or reduction checked.'},
 {'id':'s030-note09','text':'The principal-open basis, existence of maximal ideals above proper ideals, affine product and closed-immersion descriptions, and the diagonal criterion for quasi-separatedness are standard background used in the targeted argument. They were not independently reproved in this run.','basis':'Explicit assumptions of decisions/scan030_math_work.md.','event_type':'carried as background without fault found','event_outcome':'These standard algebraic-geometric facts are background assumptions for the limited affine implication; no independent proof of those foundations claimed.'}
]
nt=copy.deepcopy(D['r3']['notation'])
nt.append({'sign':'Separate underline spans','latex':r'\uline{localement} \uline{$L$}-\uline{asphérique}','locus':'Lower row of cancelled block','evidence':'Main crop shows a gap under the hyphen and no underline under the raised 1-/l-.','alternatives':'None for these spans.'})
viewed=[p3(s) for s in ['01_sga_reference','02_th_punctuation','03_envers','05_roman_correction','07_final_tail']]+[p1(s) for s in ['03_cancelled_block','05_diagonal_margin','06_final_cancelled_line']]+[pm(s) for s in ['01_top_reference','02_hand_arrow','03_coherent_quotes','04_deleted_reference','05_corps_de_call','06_left_tick','07_deleted_enonces','08_end_parenthesis']]
assert len(viewed)==len(set(viewed))==16
for c in C:assert set(c['readers'])=={'r1','r2','r3'},c['locus']
cfg=dict(approved_by_main_reader=True,scan=30,base_reader='r1',brief_version='v011',complete_tex=tex,changes=C,c_doubts=cd,unresolved=un,inventory=inv,notes=notes,notation=nt,abbreviations=D['r1']['abbreviations'],main_crop_count=len(viewed),main_viewed_crops=viewed,adjudications=[],workflow_observation='Three fresh independent readers used v011 and the cumulative notation snapshot. Main compared all three complete readings, reports and inventories, and inspected eight existing tight reader crops plus eight new tight main crops. Each delivered crop was viewed once. An attempted four-image tool result was truncated before any image was delivered; those unseen files were subsequently displayed in bounded pairs and counted only on that successful delivery. No whole or half source was reopened, no settled locus was recropped, and no OCR or external research was used.',adjudication_note='r1 supplies the graphic geometry, semantic cancellation wrappers, separate underlines and rotated marginal placement. Main adds the r2/r3 SGA and envers overprint alternatives, the r3 uncertain low comma and semicolon, the r2 extra marginal word and faint short stroke, the r2/r3 uncertain period after rappels, and the r3 broken lower stroke. Main resolves the initial dash and typed 5, retains all source errors and incomplete text, and records every C mark. Mathematical checking is explicitly limited to the affine implication.')
(R/'decisions/approved_scan030_config.json').write_text(json.dumps(cfg,ensure_ascii=False,indent=2)+'\n')
mathfile=R/'decisions/scan030_math_work.md'
mathtext=mathfile.read_text().replace('Prepared from the supplied letter text while the independent readers inspect\nthe ink. The connection to the finally read first paragraph must be confirmed\nbefore this check is entered in the consolidated notes.','Prepared from the supplied letter text while the independent readers inspected\nthe ink. Main subsequently compared all three complete readings: each confirms\nexactly the affine implication in the opening sentence. The limited argument\nis connected to that observed wording in s030-note08; it changes no reading.')
mathfile.write_text(mathtext)
print(json.dumps({'changes':len(C),'inventory':len(inv),'unresolved':len(un),'c_marks':sum(len(q.get('c_mark_ids',[])) for q in cd),'main_views':len(viewed)},indent=2))
