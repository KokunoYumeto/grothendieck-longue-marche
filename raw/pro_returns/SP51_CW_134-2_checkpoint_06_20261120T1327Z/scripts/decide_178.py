from decision_helpers import *
import copy
r=load_reports(178)
a=[row(r,'A',i) for i in range(19)]
crop_map={0:'main/01_six_operations_quotes.jpg',2:'C/L08_ellipsis.png',3:'C/L08_ellipsis.png',7:'main/04_half_simpliciaux.jpg',10:'B/L18_overwritten_article.png',11:'B/L18_overwritten_article.png',12:'main/02_topologie_quotes.jpg',13:'C/L21_cancelled_parenthesis.png',14:'C/L21_cancelled_parenthesis.png'}
for i,p in crop_map.items():a[i]['crop']='crops/scan178/'+p
a[1].update(final=r'\unsure{autrement}',differs_C=False,differs_H=True,evidence='Initial au, tall t and the ending ment are readable, but the faint medial r/e strokes remain disconnected. Root retains B’s uncertainty over A/C’s resolution; the absence of a competing word does not make the weak ink certain.',confidence='medium')
a[7]['evidence']='The main crop shows a high 1, diagonal division stroke and low 2, followed by simpliciaux; no semi- is written at this occurrence. The earlier occurrence spells semi-simpliciaux.'
a[11]['evidence']+=' Root selects A/B over C’s retained des/les: the heavy bowl and ascender establish the live d separately from the older strokes.'
a[13].update(final=r'\deleted{(d\'un espace \unsure{modéré} \unsure{compact})}',evidence='The opening d bowl/stem, detached apostrophe and low un strokes survive; espace has its small e/s opening, distinct p descender and low ace trail. Root resolves those two words with A/C. The middle word modéré is interrupted by the zigzag. At the last word, a low co-like opening and final t survive, but the central letter strokes merge with the cancellation; root retains B/C’s doubt on compact instead of A’s resolution.',confidence='medium')
a[16]['evidence']+=' The opening pair was inspected separately in crops/scan178/main/03_espace_quote_open.jpg; the saved compact crop supplies the closing pair.'
a[18]['marked_in_H']='yes'
cat=row(r,'B',6)
a[13]['C']=r"\inserted{\deleted{(\unsure{d'un} \unsure{espace} \unsure{modéré} \unsure{compact})}}"
a[13]['final']=r"\inserted{\deleted{(d'un espace \unsure{modéré} \unsure{compact})}}"
a[13]['H']+= '; editorial note describes an interlinear addition, but no addition state is marked'
a[13]['evidence']+=' '+a[14]['evidence']
diffs=a[:7]+[cat]+a[7:14]+a[15:]
comparisons=[
 {'place':'L5 autrement','A':'resolved autrement','B':r'\unsure{autrement}','C':'resolved autrement','decision':'Retain B. The medial r/e strokes are faint and interrupted; a plausible unique word is still not fully recoverable (A/l05_autrement.png).'},
 {'place':'L12 cat and its points','A':'cat.','B':r'cat.\,.','C':r'cat.\,.','decision':'Select B/C. Two distinct compact black points follow the t in horizontal succession. Preserve both without deciding a second punctuation function (B/L12_cat_stops.png).'},
 {'place':'L18 live article','A':'des resolved','B':'des resolved','C':'des / les retained','decision':'Select A/B. The heavy left bowl joins the ascender; it is d, while older finer loops remain partly underneath. The underlying article retains les/des/ces uncertainty (B/L18_overwritten_article.png).'},
 {'place':'L21a cancelled parenthesis','A':'d’un espace and compact resolved; modéré doubtful','B':'all four words doubtful','C':'d’un espace resolved; modéré and compact doubtful','decision':'Select C. Opening d/apostrophe/un and espace’s p and low ending are traceable; the cancelled middle and final words are less secure. No grammatical completion is used (C/L21_cancelled_parenthesis.png).'},
 {'place':'Four isolated nontext points','A':'four: lower ellipsis, off-axis diagram, below passer, above fractions','B':'two: off-axis diagram, above fractions','C':'two: lower ellipsis, off-axis diagram','decision':'Select A’s union inventory. Root sees all four detached deposits. The tiny below-passer point is a compact dark oval distinct from the diffuse grain; the above-fractions point is larger and separate from f. Presence is recorded; origin and purpose are uncertain (C/L08_ellipsis.png, A/diagram.png, A/l16_point.png).'}
]
unresolved=copy.deepcopy(r['A']['unresolved'])
uc=['C/L08_ellipsis.png','B/L18_overwritten_article.png','C/L21_cancelled_parenthesis.png','A/l24_cancelled_fon.png','C/L08_ellipsis.png','A/diagram.png','A/l16_point.png','A/l16_point.png']
for u,p in zip(unresolved,uc):u['crop']='crops/scan178/'+p
unresolved.insert(0,{'place':'L5 autrement','reading':'autrement','alternatives':[],'confidence':'medium','reason':'Medial r/e strokes are pale and interrupted; no stronger alternative word is supplied.','crop':'crops/scan178/A/l05_autrement.png'})
unresolved.insert(4,{'place':'L21a cancelled final word','reading':'compact','alternatives':[],'confidence':'low','reason':'Opening co-like strokes and terminal t support compact, but the middle is entangled with the cancellation.','crop':'crops/scan178/C/L21_cancelled_parenthesis.png'})
review=[]
qc={1:'A/l05_autrement.png',2:'C/L08_ellipsis.png',3:'A/l08_apparaitra.png',4:'B/L18_overwritten_article.png',5:'B/L18_overwritten_article.png',6:'C/L21_cancelled_parenthesis.png',7:'C/L21_cancelled_parenthesis.png',8:'C/L21_cancelled_parenthesis.png',9:'C/L21_cancelled_parenthesis.png',10:'A/l22_strates.png',11:'A/l24_cancelled_fon.png',12:'main/01_six_operations_quotes.jpg',13:'A/diagram.png',14:'main/04_half_simpliciaux.jpg',15:'C/L21_cancelled_parenthesis.png'}
for i,q in enumerate(r['A']['C_doubt_review'],1):
 status=q['decision'];final=q['final'];ev=q['evidence']
 if i==1:status='retained';final=r'\unsure{autrement}';ev=a[1]['evidence']
 if i==9:status='retained';final=r'\unsure{compact}';ev=a[13]['evidence']
 if i in [6,7,8]:ev=a[13]['evidence']
 if i==14:ev+=' Root’s numeral crop confirms the literal fraction; the saved A/l16_point.png crop confirms fractions and its separate marks.'
 if i==15:ev+=' The root retains doubt on modéré and compact within the cancellation; the later compact is clear and separate.'
 review.append({'place':q['place']+'; '+q['question'],'earlier':q['question'],'decision':status+': '+final,'evidence':ev+' Main inspected crops/scan178/'+qc[i]+'.'})
inv=copy.deepcopy(r['A']['inventory'])
inv=[inv[i] for i in [0,1,6,2,3,4,5,7,8,9,10,11,12,13,14,15,16]]
for x in inv:
 if 'parenthesis' in x['element'].lower():x['first_words_or_objects']=r"(d'un espace \unsure{modéré} \unsure{compact})"
notes=r'''**S178-notes.** This page continues the exercise announced at the preceding foot: to express the “6 opérations” on sheaves over X or a union of its strata in the proposed dictionary and to check the known formalism again. The author's restriction is “dans le cas disons de strates non singulières”. The parenthesis mentions difficulties with dualizing complexes otherwise and the wish “dont on aimerait qu'ils appartiennent à notre catégorie”. These are source statements, not demonstrations performed in this transcription.

“Mais il apparaitra probablement que” introduces the proposed need to take a category of diagrams of semi-simplicial sets first and then pass to a homotopy category of fractions. The ink alternates the spelled semi-simpliciaux with the numeric 1/2 simpliciaux; it also writes two separate points after cat. The little diagram has one visible source point and two outgoing arrows, with no written terminal objects or labels. H adds two terminal bullets despite its own editorial explanation that points were supplied. No mathematical construction or proof of the claimed comparison is supplied here.

The author says “J'ai plus ou moins explicité dernièrement” while considering foundations of “topologie modérée”, parenthetically eliminating wild phenomena. He begins a statement that an equisingular stratification with “à strates non singulières disons” of a compact moderate space canonically gives a diagram of spaces. The statement continues beyond this page; nothing is supplied from that continuation. The smaller parenthesis after équisingulière is inserted and cancelled, while compact is separately inserted later after the quoted espace modéré. The earlier cancelled d'un espace is recoverable; modéré and compact remain doubtful. The later compact and its following comma are clear.

No surrounding mathematical assertion was proved or refuted. A and B labelled their tracing of the two shafts as a local incidence check; the consolidated event register classifies that activity as visual reading carried as background. C correctly reported no mathematical check event. Following ink to distinguish heads and the off-axis point is not a proof or independent mathematical verification. The diagram and source/target questions prompted crop inspection; the empty targets are chosen from the ink alone. The raw reader event labels remain preserved in their reports.

Four isolated points are reproduced without inferred punctuation or mathematical function. Their origins remain uncertain. Root retains B's uncertainty on autrement, selects A/B's live des rather than les, selects B/C's literal two points after cat, and retains C's level of doubt on the cancelled parenthesis. The three quoted phrases have paired upper ticks, not guillemets. No external English version or other-page text was consulted. There is no title, date, closing, signature or authorial underlining on this sheet. It carries author page **33** and archive pencil **178**, with 24 main baselines, two diagram rows, five additions and three deletion regions; J'ai begins a new indented paragraph. The foot ends d'espaces, with its comma.
'''
text=(ROOT/'records/scan178/A/reading.tex').read_text().replace('% C original page filename: H134-06_134-2_scan178.tex\n','')
text=text.replace('(autrement,',r'(\unsure{autrement},').replace('la cat. des',r'la cat.\,. des')
text=text.replace(r"(d'un espace \unsure{modéré} compact)",r"(d'un espace \unsure{modéré} \unsure{compact})")
abbr=copy.deepcopy(r['A']['abbreviations']);abbr[0]['written']='cat..'
viewed=['A/l05_autrement.png','C/L08_ellipsis.png','A/l08_apparaitra.png','A/diagram.png','B/L12_cat_stops.png','A/l16_point.png','B/L18_overwritten_article.png','C/L21_cancelled_parenthesis.png','A/l22_strates.png','A/l23_compact_comma.png','A/l24_cancelled_fon.png','main/01_six_operations_quotes.jpg','main/02_topologie_quotes.jpg','main/03_espace_quote_open.jpg','main/04_half_simpliciaux.jpg']
d=write_decision(178,'A',[],diffs,comparisons,unresolved,inv,notes,abbr,review,['crops/scan178/'+p for p in viewed],brief='briefs/brief_v09_scan178.md',workflow_note='Three fresh independent readers each viewed whole/a/b once, then A 10, B 11 and C 10 crops. Main read all three complete returns and all 15 C-question reviews before adjudication. A text-output batch was truncated; B and the missing A tail were then read completely. Main reused 11 saved crops and made four quote/fraction crops, 15 successful crop inspections total. One attempted image batch (A/diagram.png, B/L12_cat_stops.png, A/l16_point.png) failed to display because context output was truncated; those exact saved files later displayed successfully once, without recropping. Reader disagreements over autrement, live article, cancelled words, double points and the four detached marks were decided explicitly. No TeX or external source was used. Visual arrow tracing was not promoted to a mathematical check in the consolidated events.',text_override=text)
for e in d['check_events']:
 if e['statement_id'] in ['scan178.D1','178-D-incidence']:
  e['statement_id']='S178-diagram-reading';e['type']='carried as background without fault found'
  e['outcome']='Visual inspection only: source point, shafts, arrowheads, empty targets and detached point were read from ink. No mathematical assertion was proved or independently checked. Original reader classification retained in its report. '+e['outcome']
by={}
for rep in r.values():
 for c in rep['crops']:by[c.get('path',c.get('crop',''))]=c.get('bbox')
for x in d['differences']:
 for k in ['C','H','final']:x[k]=x[k].replace("\\'", "'")
 cp=x['crop'];m=(ROOT/cp).with_suffix('.json');box=json.loads(m.read_text()).get('bbox') if m.exists() else by.get(cp)
 if box:
  if x.get('bbox')!=box:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=box
(ROOT/'records/scan178/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Numeric shorthand',r'$1/2$ simpliciaux','178 L15: high 1, diagonal stroke and low 2; earlier L13 spells semi-simpliciaux. Do not expand the numeral in the text.'),
 ('Repeated abbreviation points',r'cat.\,.','178 L12: two separate black points follow the t, preserved literally; distinct from the undotted cat on 177.'),
 ('Faint future ending and accent','apparaitra','178 L8: low r/a continues after t; compact i-dot, no visible circumflex. This local form is not inferred from grammar.'),
 ('Unlabelled corner diagram','one source point; two outgoing arrows; empty written targets','178 D1–D2: separate lower/right point is off-axis and has no assigned role.')
])
register_note_statements(178,[
 {'place':'L1–L8; notes paragraph 1','statement':'The proposed exercise is to express six operations in the dictionary and reverify their formalism, restricting to nonsingular strata.'},
 {'place':'L5–L8; notes paragraph 1','statement':'The author anticipates problems with dualizing complexes for singular strata and wishes them to belong to the category.'},
 {'place':'L8–L16; notes paragraph 2','statement':'The author probabilistically proposes taking diagrams before forming a homotopy category of fractions.'},
 {'place':'L17–L24; notes paragraph 3','statement':'The author reports partial recent work on moderate topology and begins a canonical diagram construction for an equisingular stratification of a compact moderate space; the statement continues beyond this page.'}
])
