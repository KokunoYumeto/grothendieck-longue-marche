from decision_helpers import *
import copy
r=load_reports(177)
diffs=[row(r,'B',i) for i in range(26)]
crop_map={0:'main/01_pris_quotes.jpg',1:'main/02_moralement_quotes.jpg',2:'C/l02_tjrs.png',3:'C/l03_polies.png',4:'A/l03_dim.png',5:'main/03_fibration_quote_open.jpg',6:'main/04_fibration_quote_close_bracket.jpg',7:'C/l13_cat.png',10:'C/l14_p_first.png',11:'A/l15_equisinguliere.png',20:'C/l19_coeff.png',25:'C/l23_ai.png'}
for i,p in crop_map.items():diffs[i]['crop']='crops/scan177/'+p
for i in [0,1,4,6,11,20]:
 diffs[i]['evidence']=diffs[i]['evidence'].replace('The top half shows','The main crop shows').replace('The bottom half shows','The main crop shows').replace('In the bottom half,','In the main crop,')
diffs[5]['evidence']+=' Closing pair independently inspected in crops/scan177/main/04_fibration_quote_close_bracket.jpg.'
diffs[9]['evidence']+=' Root selects B/C over A: the earlier curled segment belongs to the terminal letter work; it does not establish an independent comma.'
diffs[14]['evidence']+=' Root selects B’s upper-before-lower order over A/C’s reordered running phrase. This preserves position and does not claim a certain semantic attachment.'
diffs[19]['evidence']+=' Root selects A/B over C’s retained en/et: the second letter has a right arch rather than an independent crossbar.'
diffs[21].update(final=r'\inserted{$X_0,X_1$ \deleted{$\unsure{\Delta|X}$}}',differs_C=False,evidence='A small triangular outline and low base survive at the right of the cancellation, favouring Delta. The left crossing strokes merge with the live l of reliés and the insertion guide, so root retains A/C’s X alternative rather than accepting B’s complete resolution. The cancellation lies on the same upper addition line as X_0,X_1; no independent comma follows it. H leaves recoverable mathematical ink as ill and puts the cancellation outside the addition.',confidence='low')
diffs[24].update(C=r'\unsure{(}F_1)',H=r'(F_1)',final=r'\unsure{(}F_1)',differs_C=False,differs_H=True,evidence='The left mark descends and returns sharply upward, meeting the F stem in a U-like shape. An opening parenthesis is the strongest reading, but its shape is unconventional and entangled with F; root retains A/C’s doubt over B’s resolution. This row concerns only the opening mark; the J/j choice is recorded separately.',confidence='low')
comparisons=[
 {'place':'L13 punctuation after n-champs','A':r'\unsure{,} \unsure{..|\ldots}','B':r'\unsure{..|\ldots}; no comma','C':r'\unsure{..|\ldots}; no comma','decision':'Select B/C. The terminal letter-work does not supply an independently identifiable comma; two low following marks are clearer than a possible third. Keep the point-count doubt (B/04_complexes_addition.png).'},
 {'place':'L18, ordinaires and parenthetical addition','A':'ordinaires live, then parenthesis','B':'parenthesis above/before live ordinaires; attachment uncertain','C':'ordinaires live, then parenthesis','decision':'Select B’s visible upper-before-lower order. The small parenthetical line lies between the underlined phrase and the baseline ordinaires; no guide fixes its logical attachment. Record that limit in a comment and doubts; do not infer writing chronology (B/07_qualification.png).'},
 {'place':'L19 en / et','A':'en resolved','B':'en resolved','C':'en / et retained','decision':'Select A/B. The high entry descends into a joined right arch; no separate crossbar establishes t. This is a stroke decision, not a grammatical inference (B/10_en.png).'},
 {'place':'L21a cancelled sign','A':'Delta / X retained','B':'Delta resolved; Delta/triangle alphabet marked earlier','C':'Delta / X retained','decision':'Select A/C. The right triangular form favours Delta, but left crossing strokes and the live l cannot be fully separated. Keep X as a secondary cancelled-shape alternative; no comma follows the cancellation (B/12_vertices_deletion.png).'},
 {'place':'L21 compatibilité ending','A':'compatibilité certain','B':'compatibilité / compatibilit','C':'compatibilité certain','decision':'Select B’s doubt. The last tall stroke and detached rising horizontal line do not securely distinguish a final é from the t ending; a separate acute/vowel is not resolved (B/15_compatibilite_ending.png).'},
 {'place':'L22 opening mark before F_1','A':'opening parenthesis doubtful','B':'opening parenthesis resolved','C':'opening parenthesis doubtful','decision':'Select A/C. The U-like descending/returning stroke runs into F and is not an ordinary clear parenthesis. Preserve it as a doubtful opening mark; correct mathematical typing does not settle its shape (B/13_formula.png).'},
 {'place':'Four isolated nontext marks','A':'three: right of underline, above/right of parenthesis, above prenant','B':'four: A’s three plus point below donnée','C':'two: above/right of parenthesis and above prenant','decision':'Select B’s complete inventory. Root sees a distinct compact point below donnée, an upright oval beyond the underline, a short tick above/right of the parenthesis, and a bent dark mark above prenant. Each is reproduced without lexical or mathematical function; origins remain uncertain (B/16_point_below_donnee.png, B/08_right_isolated_mark.png, B/07_qualification.png, B/11_interblock_mark.png).'}
]
unresolved=copy.deepcopy(r['B']['unresolved'])
umap={'crops/scan177/B/02_polies.png':'crops/scan177/C/l03_polies.png','crops/scan177/B/05_first_P.png':'crops/scan177/C/l14_p_first.png','crops/scan177/B/14_nai.png':'crops/scan177/C/l23_ai.png'}
for x in unresolved:
 x['crop']=umap.get(x.get('crop'),x.get('crop'));x.pop('additional_crop',None)
unresolved[3]['place']='D2 source'
unresolved.extend([
 {'place':'L21a, cancelled sign','reading':r'\Delta','alternatives':['X'],'confidence':'low','reason':'Right triangular outline survives, but left crossing strokes and the live l are entangled.','crop':'crops/scan177/B/12_vertices_deletion.png'},
 {'place':'L22 before F_1','reading':'(','alternatives':['unidentified descending/returning mark'],'confidence':'low','reason':'The U-like stroke touches F; an opening parenthesis remains the strongest but uncertain interpretation.','crop':'crops/scan177/B/13_formula.png'},
 {'place':'L18a, attachment of pro-types parenthesis','reading':'physical upper-before-lower order, preceding ordinaires','alternatives':['logical placement after ordinaires'],'confidence':'medium','reason':'No caret or guide settles attachment. The text preserves physical order, not an asserted chronology.','crop':'crops/scan177/B/07_qualification.png'}
])
for place,crop in [('below donnée','B/16_point_below_donnee.png'),('right of underline','B/08_right_isolated_mark.png'),('above/right of parenthesis','B/07_qualification.png'),('above prenant','B/11_interblock_mark.png')]:
 unresolved.append({'place':place,'reading':'visible nontext mark reproduced','alternatives':['incidental manuscript ink','later or reproduction mark'],'confidence':'low','reason':'Presence and shape are visible; origin and purpose cannot be identified.','crop':'crops/scan177/'+crop})
review=[]
review_crops={1:'C/l02_tjrs.png',2:'C/l03_polies.png',3:'C/l13_cat.png',4:'B/04_complexes_addition.png',5:'C/l14_p_first.png',6:'B/09_diagram.png',7:'B/09_diagram.png',8:'B/10_en.png',9:'C/l19_coeff.png',10:'B/12_vertices_deletion.png',11:'B/13_formula.png',12:'C/l23_ai.png',13:'C/l03_polies.png',14:'A/l03_dim.png',16:'B/07_qualification.png',17:'B/09_diagram.png',18:'B/12_vertices_deletion.png',19:'C/l23_ai.png'}
for i,q in enumerate(r['A']['C_doubt_review'],1):
 final=q['final'];status=q['decision'];e=q['evidence']
 if i==4:final=r'\unsure{..|\ldots}; no independent comma';e=diffs[9]['evidence']
 if i==8:e=diffs[19]['evidence']
 if i==9:e=diffs[20]['evidence']
 if i==10:e=diffs[21]['evidence']
 if i==11:e=diffs[24]['evidence']
 if i==16:final=r'guided de la cat and complexes d’iceux, ou; upper pro-types parenthesis before live ordinaires';e=diffs[14]['evidence']
 if i==18:e='Inserted endpoints and cancellation retained; hom unexpanded and undotted; both stars, indices and arrow confirmed. The opening parenthesis and cancelled symbol remain doubtful; final letters of compatibilité also remain doubtful.'
 if i in review_crops:e+=' Main inspected crops/scan177/'+review_crops[i]+'.'
 else:e+=' All three independent full-resolution half readings agree.'
 review.append({'place':q['question'],'earlier':q['question'],'decision':status+': '+final,'evidence':e})
notes=r'''**S177-notes.** The opening continuation describes p″ as “pris à la lettre” an inclusion and “moralement” still a fibration. Its bracketed description mentions finite dimension and nonsingular varieties and contrasts this with the quoted Cartan–Serre fibration slogan. Those are source assertions, not proofs performed here. The adjective is preserved as polies/jolies; no English version or alleged prior wording was consulted.

The author calls the last diagram “susceptible d’une construction directe, purement algébrique” for schemes, conditional on “lorsque l’on a développé la construction du voisinage tubulaire étale”. He relates constructible sheaves, complexes and n-champs for an equisingular stratification to a span of homotopy types, with a parenthetical pro-types qualification for the étale topology. The parenthesis is physically above ordinaires with no attachment guide. The consolidated text preserves that order and records the unresolved logical attachment; ordinaires is live baseline writing.

All three readers performed only the narrow check **S177-local-span-typing**: with p from the triangular source to X_0 and J from that source to X_1, the inverse images p^*F_0 and J^*F_1 both lie over the common source. A compatibility morphism between them is therefore locally well-typed. This does not prove a category equivalence, the geometric fibration claim, or the proposed algebraic construction. The type check prompted inspection of stars, indices, arrow directions and the unusual opening mark before F_1. It does not decide J/j, Delta/triangle or the parenthesis shape; those uncertainties remain tied to ink.

The explicit qualification “Ce serait un exercice amusant (que je n’\unsure{ai} pas encore fait) de” records an unperformed exercise. The page ends at the complete word de; no continuation is supplied. The ai is an editorial reading doubt, not an authorial question mark. The source provides no title, date, closing or signature here. Author page **32** and archive pencil **177** are present. There are 23 main baselines, four diagram rows and five additions; Le point begins a new indented paragraph and the diagram interrupts that paragraph.

Root resolves tjrs, cat, en and coeff and confirms dim without a stop. The live (ou and n-champs are not cancelled or added; only complexes d’iceux, ou is the guided addition between them. The small cancelled triangular sign remains doubtful against X, and the final letters of compatibilité remain doubtful against compatibilit. Four isolated dark marks are drawn with no inferred textual function or authorship. H’s external-English assertion about Delta is excluded as evidence; its note about the parenthesis being physically above ordinaires is supported, although its running text orders them differently.
'''
text=(ROOT/'records/scan177/B/reading.tex').read_text()
text=text.replace('% C original page filename: H134-05_134-2_scan177.tex\n','')
text=text.replace(r'\deleted{$\Delta$}',r'\deleted{$\unsure{\Delta|X}$}')
text=text.replace(r'J^*(F_1)',r'J^*\unsure{(}F_1)')
inv=copy.deepcopy(r['B']['inventory'])
inv=[inv[i] for i in [0,1,2,3,4,5,13,6,14,7,15,8,16,9,10,11,12,17]]
for x in inv:
 if x['element']=='cancelled triangular sign':x['first_words_or_objects']=r'\unsure{\Delta|X}';x['details']='Triangular right outline preferred; crossing and the live l leave X possible. Cancellation remains inside the addition.'
 if x['element']=='inline compatibility formula':x['first_words_or_objects']=r'p^*(F_0)\to J^*\unsure{(}F_1)';x['details']='Both raised stars, low indices and rightward arrow clear. Second opening mark remains doubtful.'
viewed=['C/l02_tjrs.png','C/l03_polies.png','B/04_complexes_addition.png','A/l03_dim.png','C/l13_cat.png','C/l14_p_first.png','A/l15_equisinguliere.png','B/07_qualification.png','B/08_right_isolated_mark.png','B/16_point_below_donnee.png','B/11_interblock_mark.png','B/09_diagram.png','B/10_en.png','C/l19_coeff.png','B/12_vertices_deletion.png','B/15_compatibilite_ending.png','B/13_formula.png','C/l23_ai.png','main/01_pris_quotes.jpg','main/02_moralement_quotes.jpg','main/03_fibration_quote_open.jpg','main/04_fibration_quote_close_bracket.jpg']
d=write_decision(177,'B',[],diffs,comparisons,unresolved,inv,notes,r['B']['abbreviations'],review,['crops/scan177/'+p for p in viewed],brief='briefs/brief_v08_scan177.md',workflow_note='Three fresh independent readers completed whole/a/b once, 23 main baselines, four diagram rows, five additions, one cancellation and page numbers. A made 15 crops, B 16, C 15. Main read all three complete returns before adjudication, reused 18 saved crops and made four quote-boundary crops, for 22 successful crop inspections. One attempted batch containing A/l03_dim.png, C/l13_cat.png and C/l14_p_first.png failed to display because context output was truncated; none was counted as inspected then. The identical saved files later displayed successfully once, with no replacement crops. All readers observed the no-TeX rule. Interlinear order, four nontext marks and three retained dissenting doubts are explicitly recorded.',text_override=text)
for e in d['check_events']:
 if e['statement_id'] in ['S177-local-span-typing','scan177-local-pullback-typing','177-M1']:e['statement_id']='S177-local-span-typing'
for x in d['differences']:
 for k in ['C','H','final']:
  x[k]=x[k].replace("\\'", "'")
# Align each consolidated crop rectangle with the saved image actually inspected.
by={}
for rep in r.values():
 for c in rep['crops']:by[c.get('path',c.get('crop',''))]=c.get('bbox')
for x in d['differences']:
 cp=x['crop'];m=(ROOT/cp).with_suffix('.json')
 box=json.loads(m.read_text()).get('bbox') if m.exists() else by.get(cp)
 if box:
  if x.get('bbox')!=box:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=box
(ROOT/'records/scan177/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Undotted span/pullback letter',r'\unsure{J|j}, then J^*','177 D1/L22: tall undotted stem and broad left-returning foot; each occurrence inspected independently. Case remains uncertain.'),
 ('Triangular source and cancellation',r'\unsure{\Delta|\triangle}; cancelled \unsure{\Delta|X}','177 D2/L21a: source is a retraced triangular outline, with no separate index. The cancelled sign has additional crossing and live-letter interference; its X alternative is distinct from the source alphabet doubt.'),
 ('Recurring partition capital',r'\unsure{\mathcal P|P}, then \mathcal P','177 L14: long returning oval, same family independently seen at both occurrences by all three readers; print alphabet remains uncertain.'),
 ('Abbreviation stops','tjrs; dim; cat; top.; coeff; loc.; hom','177: detached stops after top and loc; no stops after the other five forms. Preserve each local spelling.'),
 ('Unguided interlinear parenthesis','physical upper line before lower baseline; attachment comment','177 L18a: pro-types parenthesis above ordinaires, without a caret. Physical order preserved; logical attachment remains explicitly uncertain.')
])
register_note_statements(177,[
 {'place':'L1–L7; notes paragraph 1','statement':'The manuscript calls p double-prime literally an inclusion but morally a fibration and describes finite-dimensional/nonsingular fibres.'},
 {'place':'L6–L7; notes paragraph 1','statement':'The quoted Cartan–Serre slogan says every continuous map is equivalent to a fibration.'},
 {'place':'L8–L11; notes paragraph 2','statement':'The last diagram is said to admit a direct algebraic construction once the étale tubular-neighbourhood construction is developed.'},
 {'place':'L12–L22; notes paragraphs 2–3','statement':'Constructible sheaves, complexes or n-champs are related to a span of homotopy or pro-homotopy types with local systems and compatibility maps.','status':'source assertion not proved; only local pullback typing checked separately as S177-local-span-typing'},
 {'place':'L22–L23; notes paragraph 4','statement':'The author introduces an exercise which he explicitly says he has not yet performed; its object is beyond this page.'}
])
