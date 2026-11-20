from pathlib import Path
import json

base=Path(__file__).resolve().parent
state=json.loads((base/'work_state.json').read_text())
source='/workspace/scratch/8db4dde48936/sp53_recovery/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan014.jpg'
compat=r'\mathrel{\tikz[baseline=0pt,x=1em,y=1em]{\draw (-.38,.62)--(.38,.25)--(-.43,-.10); \draw (.34,.62)--(-.32,.25)--(.38,-.10);}}'

def locator(crop=None, box=None):
    if crop:
        meta=json.loads((base/'crops'/f'{crop}.json').read_text())
        return {'crop':f'readers/scan014/R2/crops/{crop}.jpg','crop_box':meta['box'],'crop_source':meta['source']}
    return {'crop':None,'crop_box':box,'crop_source':source}

diffs=[]
def diff(id,place,c,h,reading,against_C,against_H,kind,marked_in_H,confidence,evidence,crop=None,box=None,mathematical=False):
    diffs.append(dict(id=id,place=place,c=c,h=h,reading=reading,against_C=against_C,against_H=against_H,kind=kind,marked_in_H=marked_in_H,confidence=confidence,evidence=evidence,**locator(crop,box),mathematical=mathematical))

diff('014-R2-D01','opening, after trouve','comme','trois','comme',False,True,'misread word','no','high','The word consists of low cursive joined strokes with no tall t; the upper half reads comme. Settled from half_a.',box=[608,140,862,205])
diff('014-R2-D02','opening adjective',r'\unsure{optima|optimes}','optimales',r'\unsure{optima|optimes}',False,True,'misread word','no','medium','The tail after the dotted i is a low sweep; no tall l is present. The final a versus compressed es cannot be separated securely.','01_optima')
diff('014-R2-D03','opening, before la structure',r'\unsure{definir|définir}','définir','definir',True,True,'abbreviation expanded or spelling modernised','no','high','Two separate i dots are visible; there is no detached acute above the e after d.','02_definir')
diff('014-R2-D04','opening, family capital after sur',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,'misread symbol or index','no','medium','The cap sweeps left, a single long stem ends in a closed returning foot, and a cross-arm extends right. Identity and family status are clear; the printed alphabet remains uncertain. This is the only family-F occurrence on this page. Use the supplied table’s existing mathcal/fraktur candidates.','03_family_F',mathematical=True)
diff('014-R2-D05','(1.28), first row','Soit par','soit par','Soit par',False,True,'misread word','no','high','The initial S is tall and capital; the next two row initials are distinctly smaller. Settled from half_a.',box=[470,333,566,404])
diff('014-R2-D06','(1.28), third row, compatibility sign',compat,r'\between',compat,False,True,'misread symbol or index','no','high','The two opposed zigzags retain a central open diamond and four free diagonal tips. The upper-left and lower legs are heavily retraced, with no independently readable old sign; no horizontal caps are inked. C’s geometry is retained.','04_compatibility_128',mathematical=True)
diff('014-R2-D07','right margin, subject after Non',r'\unsure{sa|ça}','ça',r'\unsure{sa|ça}',False,True,'misread word','no','medium','The initial letter has connected upper and lower returns but no separated cedilla. sa is the first ink-based candidate; ça remains possible.','05_right_margin')
diff('014-R2-D08','right margin, verb',r'\unsure{suffira|suffit}','suffit','suffira',True,True,'misread word','no','high','After the f strokes and dotted i there is a narrow r and a separate low terminal loop for a; the word does not stop at a terminal t.','05_right_margin')
diff('014-R2-D09','right margin, d’apres accent',"d'après","d'après",r"\unsure{d'apres|d'après}",True,True,'abbreviation expanded or spelling modernised','no','medium','The apostrophe is clear but a separate grave accent above the compressed e is not secure in the enlarged crop. Unaccented d’apres is first; the familiar accented reading is retained as an alternative, not silently supplied.','05_right_margin')
diff('014-R2-D10','(1.29), est after the initial ll','est',r'\add{est}','est',False,True,'insertion or placement','no','high','est is written at the normal baseline and spacing, with no caret or above-line placement. The darkened preceding ll is retraced; that does not make est an insertion.','06_definition_initial_sign',mathematical=True)
diff('014-R2-D11','(1.29), name of generated relation','préordre',r'\uncertain{préordre}','préordre',False,True,'other','yes','high','The p descender, r, marked e, rounded o, r, tall d and terminal re are visible. H’s uncertainty is removed by the crop, without a mathematical inference.','06_definition_initial_sign',mathematical=True)
diff('014-R2-D12','(1.29), words before equivalence','ou encore','donc on a','ou encore',False,True,'misread word','no','high','The half shows the two-word sequence ou encore. The first word has no d ascender; the following long word begins en. Settled from half_a.',box=[962,900,1304,965],mathematical=True)
diff('014-R2-D13','(1.29), left brace and scope','three braced lines including the verbal definition','verbal definition inline; only the equivalence displayed','three braced lines including the verbal definition',False,True,'insertion or placement','no','high','The tall left brace runs alongside the explanatory lines and the formula, with (1.29) to its left. This is an ordinary braced display, not a diagram. Settled from half_a.',box=[473,851,539,1076],mathematical=True)
diff('014-R2-D14a','slanted note, first line',r'Je \unsure{changerai|changeai}',r"J'ai \ill{}",'Je changerai',True,True,'readable ink left as \\ill{}','yes','high','The first word is Je, without apostrophe or ai. After the g loop there is a small r shoulder before the a and dotted final i; changerai is resolved.','07_slanted_margin')
diff('014-R2-D14b','slanted note, point of view and page reference',r'le \unsure{pt} de vue page 20,',r'le \ill{} de (1.29) \ill{} le 20,','le pt de vue page 20,',True,True,'readable ink left as \\ill{}','yes','high','The p descends and t rises from the baseline; pt has no point and is not superscripted. vue follows de. Faint page precedes 20, which has a rounded second digit. The nearby (1.29) is the main display label, not a token of this note.','07_slanted_margin')
diff('014-R2-D14c','slanted note, between 20 and plus que',r'et ne \unsure{supposerai} plus que',r'\ill{} plus que',r'et ne \unsure{supposerai} plus que',False,True,'readable ink left as \\ill{}','yes','medium','et ne is legible after the comma; the two p descenders and final i support supposerai, but its compressed faint middle remains uncertain. This contiguous H span is treated as one locus rather than assigning its ill token to invented separate positions.','07_slanted_margin')
diff('014-R2-D14d','slanted note, relation dependence and punctuation',r'$\ll$ soit déterminé ainsi en termes de $\leq,\preccurlyeq$, mais plutôt que $\preccurlyeq$ est déterminé par $\ll,\leq$',r'\ill{} \ill{} $\ll$ \ill{} $\leq$, $\preccurlyeq$ \ill{} $\ll$ \ill{} et \ill{}',r'$\ll$ soit déterminé ainsi en termes de $\leq,\preccurlyeq$ mais plutôt que $\preccurlyeq$ est déterminé par $\ll,\leq$',True,True,'readable ink left as \\ill{}','yes','medium','Upright reading gives the full continuous clause. Every visible order sign was checked: ll, then leq/preccurlyeq, then preccurlyeq, finally ll/leq. No distinct comma is discernible after the first pair’s final preccurlyeq before mais; no terminal point follows the final leq. The final est is a word, not H’s isolated et. H’s partly illegible residual span is kept together to avoid false token alignment.','07_slanted_margin',mathematical=True)
diff('014-R2-D15','paragraph below (1.29), opening','Cela correspond','[correspondant','Cela correspond',False,True,'misread word','no','high','The half shows capital Cela and the separate finite verb correspond. There is no opening square bracket before the C. Settled from the halves.',box=[266,1121,762,1214])
diff('014-R2-D16','paragraph below (1.29), after intuitif','intuitif,','intuitif],','intuitif,',False,True,'text not on the page','no','high','The long upright with bottom return is the descending terminal f of intuitif, followed by a separate comma. No additional closing square bracket is present. Settled from half_b.',box=[368,1224,651,1345])
diff('014-R2-D17','paragraph below (1.29), centre','centre',r'\uncertain{contexte}','centre',False,True,'misread word','yes','high','The middle of the word has a single t ascender and low r/e ending; no x/t sequence appears. Settled from the halves.',box=[937,1112,1106,1179])
diff('014-R2-D18','paragraph below (1.29), gravité','gravité',r'\ill{}','gravité',False,True,'readable ink left as \\ill{}','yes','high','The descender of g, r-a-v sequence and final t with marked e are readable. Settled from the halves.',box=[1204,1093,1414,1215])
diff('014-R2-D19','canceled adjective after gravité',r'\deleted{\unsure{conceptuel}}',r'\struck{\ill{}}',r'\deleted{conceptuel}',True,True,'readable ink left as \\ill{}','yes','high','The full-width horizontal strike is certain. Surviving con/c/e curves, the p descender and tall t and terminal l resolve conceptuel. H correctly records that this word is struck.','08_conceptuel_geometrique')
diff('014-R2-D20','replacement above conceptuel',r'\inserted{géométrique}',r'\add{\ill{}}',r'\inserted{\unsure{géometrique|géométrique}}',True,True,'readable ink left as \\ill{}','yes','medium','The replacement above the strike is readable as géometrique. A first acute is present; a separate second acute above the central compressed e is not secure. H correctly records an insertion but leaves its wording unread.','08_conceptuel_geometrique')
diff('014-R2-D21','before intuitif','et','omitted','et',False,True,'omission','no','high','A short e and rising t precede intuitif on the main prose line, distinct from the oblique margin’s par. Settled from half_b.',box=[267,1239,359,1318])
diff('014-R2-D22','qui est bien ... la notion','sur la','une','sur la',False,True,'misread word','no','high','Two short words occupy this position, with the tall loop of l in la. Settled from half_b.',box=[1091,1188,1266,1271])
diff('014-R2-D23','after plutôt and before celle','que sur',r'\ill{}','que sur',False,True,'readable ink left as \\ill{}','yes','high','The first word has a q descender; the second is a separate short sur before celle. H’s single ill token covers this span. Settled from half_b.',box=[992,1295,1265,1379])
diff('014-R2-D24','after pour ll, before amenait','cela','et ça','cela',False,True,'misread word','no','high','The line begins with one connected cela, including the tall l loop, and no preceding et. Settled from half_b.',box=[267,1716,361,1806])
diff('014-R2-D25','à mettre des axiomes','mettre','multiplier','mettre',False,True,'misread word','no','high','The word has the short me opening, double t strokes and low re tail; it lacks the long multiplier sequence. Settled from half_b.',box=[817,1678,993,1767])
diff('014-R2-D26','article before axiomes','des','les','des',False,True,'misread word','no','high','The initial loop-and-return is d, followed by the short es tail. Settled from half_b.',box=[1013,1675,1113,1747])
diff('014-R2-D27','following axiomes en','surnombre','nombre','surnombre',False,True,'omission','no','high','The next line begins with the separate sur sequence joined to nombre; the full written word is surnombre. Settled from half_b.',box=[264,1800,646,1906])
diff('014-R2-D28','il semblerait que ce soit ...','de partir','en partant','de partir',False,True,'misread word','no','high','The short de has a looped d, and the following word has the final dotted i/r ending of partir. Settled from half_b.',box=[1093,1845,1467,1959])
diff('014-R2-D29','after the lower pair leq,ll and before soit','qui','que','qui',False,True,'misread word','no','high','The short final dotted i belongs to qui. Settled from half_b.',box=[543,1988,650,2084])
diff('014-R2-D30','following suivre',r'\unsure{tantôt}','maintenant','tantôt',True,True,'misread word','no','high','The crop shows the initial t, low a/n group, medial t, separate circumflex over the reduced o and final crossed t. The darkened initial group does not establish a deletion.','09_tantot')
diff('014-R2-D31','last prose line pair, second compatibility sign',compat,r'\between',compat,False,True,'misread symbol or index','no','high','This separate occurrence has two thin opposed zigzags, an open central diamond and four unjoined outer ends, with no horizontal caps or extra upright. It was settled from half_b, so no crop was made.',box=[1329,2166,1395,2240],mathematical=True)
diff('014-R2-D32','page-ending punctuation after chose',',','.',',',False,True,'other','no','high','The final mark descends as a short comma after chose; it is not a round full point. Settled from half_b.',box=[1469,2264,1500,2320])

c_doubts=[]
def cd(place,c,reading,disposition,evidence,crop):
    c_doubts.append(dict(place=place,c=c,reading=reading,disposition=disposition,evidence=evidence,**locator(crop)))
cd('opening adjective',r'\unsure{optima|optimes}',r'\unsure{optima|optimes}','retained','No tall l supports optimales; the low final sweep does not securely distinguish a from es.','01_optima')
cd('opening definir',r'\unsure{definir|définir}','definir','resolved','Two i dots are separate, while no acute appears above the e after d.','02_definir')
cd('opening family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Family identity is clear from the cap and returning foot. Exact printed alphabet remains unresolved; the supplied table’s mathcal/fraktur alternatives are used.','03_family_F')
cd('right marginal subject',r'\unsure{sa|ça}',r'\unsure{sa|ça}','retained','Connected upper and lower returns lack a separately distinguishable cedilla.','05_right_margin')
cd('right marginal verb',r'\unsure{suffira|suffit}','suffira','resolved','A low a loop follows the r after the ff and dotted i.','05_right_margin')
cd('slanted note, changerai',r'\unsure{changerai|changeai}','changerai','resolved','A small medial r shoulder precedes the a and final dotted i.','07_slanted_margin')
cd('slanted note, pt',r'\unsure{pt}','pt','resolved','The p descender and tall baseline t are distinct; no expansion or superscript is supplied. The two duplicate context-table mentions are one locus.','07_slanted_margin')
cd('slanted note, supposerai',r'\unsure{supposerai}',r'\unsure{supposerai}','retained','The doubled p descenders and i support the reading, but internal faint strokes remain compressed after rotation and enlargement.','07_slanted_margin')
cd('canceled adjective',r'\deleted{\unsure{conceptuel}}',r'\deleted{conceptuel}','resolved','The horizontal cancellation crosses the word, but its p descender and tall t/l with preceding loops resolve conceptuel.','08_conceptuel_geometrique')
cd('after suivre',r'\unsure{tantôt}','tantôt','resolved','Both internal and terminal t forms and the separate circumflex are visible.','09_tantot')

inventory=[]
def inv(element,kind,position,first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('authorial page number','text','top centre','13')
inv('opening continuation','text','top, two lines',r'on trouve comme possibilités ... sur \mathcal{F} :')
inv('choice display (1.28)','display','upper third, three braced rows',r'Soit par boxed leq,ll; soit par leq,preccurlyeq; soit par ll,compatibility sign; terminal point')
inv('right marginal caveat','margin note','right of second row of (1.28)','Non, sa/ça ne suffira pas, d’apres/d’après nouveau point de vue ...')
inv('introduction to former choice','text','below (1.28), two lines',r'Dans la première mouture, j’ai choisi leq,preccurlyeq')
inv('generated preorder (1.29)','display','middle, three braced lines',r'll est la relation de préordre ... ou encore; G ll F iff exists F-prime avec G leq F-prime preccurlyeq F')
inv('slanted change of viewpoint','margin note','left, oblique alongside (1.29) and first lower lines','Je changerai le pt de vue page 20, et ne supposerai plus que ...')
inv('explanation of the choices','text','lower half, continuing to bottom edge','Cela correspond au centre de gravité ... c’est plutôt une curiosité qu’autre chose,')
inv('canceled adjective','deletion','right end of first lower prose line','conceptuel')
inv('replacement adjective','insertion','above canceled conceptuel','géometrique/géométrique')
inv('emphasis in the difficulty claim','insertion','above de réflexivité, lower middle','surtout')

unresolved=[
 {'place':'opening adjective','reading':'optima','alternatives':['optimes'],'confidence':'medium','evidence':'Only a low terminal sweep follows the dotted i; no tall l. Crop 01.'},
 {'place':'opening family F','reading':r'\mathcal{F}','alternatives':[r'\mathfrak{F}'],'confidence':'medium','evidence':'Broad cap and looped returning foot identify a family capital without deciding the printed alphabet. Crop 03.'},
 {'place':'right note, subject','reading':'sa','alternatives':['ça'],'confidence':'medium','evidence':'Connected upper/lower curl with no detached cedilla. Crop 05.'},
 {'place':'right note, accent after d’apr','reading':"d'apres",'alternatives':["d'après"],'confidence':'medium','evidence':'No separately secure grave accent over the compressed e. Crop 05.'},
 {'place':'slanted note, future verb','reading':'supposerai','alternatives':[],'confidence':'medium','evidence':'Double descenders and dotted ending support it, but the faint internal sequence is not fully recoverable. Crop 07.'},
 {'place':'replacement adjective, second acute','reading':'géometrique','alternatives':['géométrique'],'confidence':'medium','evidence':'The first accent is visible; a separate second acute is not secure above the central compressed letter group. Crop 08.'}
]

notes={
 'content':[
  'The page continues an enumeration of possible pairs of relations for an atelier structure on a family F. It lists leq/ll, leq/preccurlyeq and ll/compatibility, with the first pair boxed.',
  'The author recalls choosing leq and preccurlyeq and defining ll as their generated preorder; the displayed existential formulation uses a single intermediate F-prime.',
  'He relates that choice to the geometric and intuitive emphasis on subdivision, says that deriving transitivity and especially reflexivity for ll required excess axioms, and tentatively prefers starting with leq and ll. The note announces a changed viewpoint on manuscript page 20.'
 ],
 'math_reading_decisions':[
  'Both intermediate capitals in the equivalence are F-prime. The three other F operands are ordinary capitals, with no added family-font ambiguity. Only the opening family F requires a font doubt.',
  'The compatibility symbol has open four-tip geometry in both occurrences; the first is retraced. No separate canceled mathematical symbol is recoverable from that retracing.',
  'The literal word in the difficulty claim is réflexivité. S’s proposed correction to antisymmetry is an interpretation requiring other-page context and has not been adopted or verified.',
  'No theorem or algebraic claim was verified in this reading run. The check-event entries explicitly record background assertions only.'
 ],
 'author_doubts':[
  r"“Non, \unsure{sa|ça} ne suffira pas, \unsure{d'apres|d'après} nouveau point de vue ...” is a marginal caveat, not a proof check.",
  r'“Je changerai le pt de vue page 20, et ne \unsure{supposerai} plus que $\ll$ soit déterminé ainsi en termes de $\leq,\preccurlyeq$ mais plutôt que $\preccurlyeq$ est déterminé par $\ll,\leq$” records a prospective change.',
  r'“il semblerait que ce soit de partir de $\leq,\ll$ qui soit le plus simple” is explicitly tentative.'
 ],
 'titles_dates_counts':[
  'Authorial page number 13; scan number 14. Display labels (1.28) and (1.29).',
  'The marginal 20 is preceded by page; it is a page reference, not an inked date. No title, calendar date, archive pencil sheet number, or page-count statement was found.'
 ]
}

report=dict(
 scan=14,reader='R2',status='incomplete',started_utc=state['started_utc'],finished_utc=None,
 view_log=state['views'],differences=diffs,c_doubts=c_doubts,
 s_rows=[dict(id='SA21-K6-02',disposition='partly confirmed',reading=r'de transitivité et \inserted{surtout} de réflexivité pour $\ll$',evidence='The lower half clearly has réflexivité, with surtout inserted above de. This confirms S’s literal quoted word only. The claim that it is a slip and should be replaced by antisymmetry is not established from this page; the context cited by S is outside the assigned reading and was not consulted. No emendation is made.',**locator(box=[273,1540,1606,1704]))],
 inventory=inventory,notes=notes,
 check_events=[
  {'statement_id':'SP53-156-6-014-1.28','type':'carried as background without fault found','outcome':'Read as the author’s proposed possibilities, with the marginal qualification; no mathematical verification performed.'},
  {'statement_id':'SP53-156-6-014-1.29','type':'carried as background without fault found','outcome':'Read as the author’s generated-preorder assertion and existential equivalence; no mathematical verification performed.'},
  {'statement_id':'SP53-156-6-014-reflexivite','type':'carried as background without fault found','outcome':'Read as the author’s assertion about deriving transitivity and reflexivity; no mathematical verification performed. S’s proposed slip is unverified.'}
 ],
 notation_proposals=[
  {'sign':'family F','latex':r'\unsure{\mathcal{F}|\mathfrak{F}}','ink':'Opening after sur: broad cap, long single stem, horizontal arm, returning looped foot. This occurrence was cropped individually.','alternatives':[r'\mathfrak{F}']},
  {'sign':'compatibility relation','latex':compat,'ink':'Two opposed zigzags enclose a central diamond and have four free diagonal tips. The (1.28) occurrence is darkly retraced; the last prose occurrence is thin. Neither has horizontal caps or a distinct extra upright.','alternatives':[]},
  {'sign':'curved subdivision order','latex':r'\preccurlyeq','ink':'Both the cusp and its lower rule are curved, including the smaller occurrences in the slanted margin.','alternatives':[]},
  {'sign':'intermediate F-prime','latex':"F'",'ink':'Each of the two intermediate Fs in (1.29) has a short upper-right prime stroke with no lower dot.','alternatives':[]}
 ],
 abbreviations=[{'form':'pt','expansion':'point'}],unresolved=unresolved,brief_feedback=[],
 crop_count=9,
 limitations=['The retained letter-ending and accent doubts remain explicit after the single allowed crop for each locus.','Only the assigned page and packet were consulted. No mathematical proof check or LaTeX compilation was attempted.']
)
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Wrote incomplete report: {len(diffs)} differences, {len(c_doubts)} C doubts, {len(inventory)} inventory rows, {len(unresolved)} unresolved loci.')
