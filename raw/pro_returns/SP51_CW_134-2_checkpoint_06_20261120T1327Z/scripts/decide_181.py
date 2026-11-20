from decision_helpers import *
import copy
r=load_reports(181)
diffs=[row(r,'C',i) for i in range(23)]
cm={0:'main/01_type_quote.jpg',1:'C/01_prefix_p.png',2:'C/02_partition_p.png',3:'A/L10_incarnerait.png',4:'A/L10_incarnerait.png',5:'A/L11_ou_n_loc.png',6:'A/L11_ou_n_loc.png',7:'C/05_via_inductive.png',8:'C/14_tous_underline.png',9:'C/16_point_connaissance.png',10:'B/L14_faint_point.png',11:'C/07_point_dans.png',12:'C/17_point_right_of_un.png',13:'C/15_theoremes_underline_left.png',14:'C/08_cohomologique.png',15:'C/09_ou_homotopique.png',16:'C/09_ou_homotopique.png',17:'main/02_des_types.jpg',18:'B/L20_ordinaire.png',19:'C/11_element.png',20:'B/L22_polyedres.png',21:'B/L22_polyedres.png',22:'C/13_barred_m.png'}
for i,p in cm.items():diffs[i]['crop']='crops/scan181/'+p
diffs[0]['evidence']='The complete quoted phrase has two short raised strokes at each boundary. Neither boundary has angular guillemets. The wording and singular fin remain as written.'
diffs[1]['evidence']+=' Root inspected the opening/prefix crop and separately the closing paired strokes after homotopie in crops/scan181/main/03_types_quote_close.jpg. The prefix is inside the quoted expression.'
diffs[3]['evidence']='The raised fin has paired high quotation ticks and a guide descending into the gap before the baseline incarnerait. The opening ticks touch as a small fork; the closing strokes are distinct.'
diffs[6].update(final=r'\unsure{loc.|loc}',differs_C=True,differs_H=True,confidence='medium',kind='other',evidence='Root selects A’s retained stop/no-stop doubt against B/C’s resolved unpunctuated loc. At the lower right of c, a small dark horizontal terminal mark is separated from the preceding exit by a pale interval. This favours a stop, but a broken c-exit remains possible at the source resolution. H’s preferred loc. agrees with the first candidate; its difference is certainty only.')
diffs[7].update(final=r'\inserted{(via un passage à la limite \unsure{inductive})}',differs_C=False,differs_H=True,confidence='medium',kind='other',evidence='The full guided parenthesis is preserved before la connaissance. Root retains A/C-witness uncertainty against B/C readers’ resolution: inductive is the strongest reading, but the compressed final t/i/v/e sequence is not securely separated in the crop and some upper ascender tips are clipped. The guide beneath the phrase is continuous and returns before la; it is not an emphasis underline. No replacement crop was made.')
diffs[8]['evidence']+=' Root selects C’s literal covered-letter span over A/B’s whole-word underline. The t shaft and its lower end lie left of the rule start. The broader intended emphasis is unassigned.'
diffs[10]['evidence']='The saved crop shows a small compact point in the gap after fonctoriellement, clearly below the low level of the adjoining t/de strokes. Root selects B/C’s graphic off-line representation over A’s literal inline period. The spot has a coherent dark centre, but neither its origin nor any punctuation role is established.'
diffs[13]['evidence']+=' Root selects C’s physical span over A/B’s whole-word start: the rule starts after the two tall initial th strokes, within é. The independently inspected right endpoint is in crops/scan181/C/08_cohomologique.png. Intended semantic emphasis is not inferred.'
diffs[17]['evidence']='The crop shows a looped d followed by the low e movement and a long hooked s; types likewise ends in a separate low rightward run with a downward s hook. Both nouns are plural in the written des types, unlike H’s du type.'
diffs[17]['consequential']='Against H: des types d’homotopie fin restores the explicitly plural types where H has du type. The source’s singular fin is retained; no additional quantifier or claim is inferred.'
diffs[18].update(final=r'\unsure{ordinaire|ordïnaire}',differs_C=False,evidence='The final re movement ends before a wide gap, without a plural s. Three compact dark components occupy the first-i region: two higher spots and a shorter lower one. Root retains A’s diaeresis alternative alongside preferred ordinaire; B/C retained only the preferred word with uncertainty. The spot count is documented, without declaring a deliberate diaeresis. This enriches C’s already uncertain preferred reading rather than changing it.',confidence='medium')
diffs[20]['evidence']='Root retains B/C’s acute/grave doubt against A’s resolved acute. The small thick accent rises predominantly to the right but has a hooked upper part and too few source pixels to rule out the grave alternative. Acute remains preferred; standard spelling is not used as evidence.'
diffs[21]['evidence']='Both quotation boundaries were inspected in the same saved phrase crop: two short raised opening ticks before polyédres and two raised closing ticks after finis. No rule underlines this phrase.'
comparisons=[
 {'place':'L11 loc ending','A':'loc. / loc','B':'loc resolved','C':'loc resolved','decision':'Select A’s uncertainty, preferring loc. A small dark terminal mark has a pale separating interval; a broken c exit remains supported. Crop A/L11_ou_n_loc.png.'},
 {'place':'L12a inductive','A':'inductive uncertain','B':'inductive resolved','C':'inductive resolved','decision':'Retain A’s one-reading uncertainty. The final joined strokes remain compressed and some ascender tips are clipped in C/05_via_inductive.png; no second crop is made.'},
 {'place':'L12 underline','A':'whole tous underlined','B':'whole tous underlined','C':r't\uline{ous}','decision':'Select C’s literal stroke extent, starting within o after the t shaft and its lower end (C/14_tous_underline.png). No semantic scope is assigned.'},
 {'place':'L16 underline','A':'whole théorèmes de finitude underlined','B':'whole théorèmes de finitude underlined','C':r'th\uline{éorèmes de finitude}','decision':'Select C’s literal start after initial th, within é. The rule ends after finitude and before cohomologique (C/15_theoremes_underline_left.png and C/08_cohomologique.png).'},
 {'place':'L20 first-i marks in ordinaire','A':'ordinaire / ordïnaire','B':'ordinaire uncertain','C':'ordinaire uncertain','decision':'Retain A’s supported alternative with ordinaire first. Two higher points and a shorter lower mark are visible; they do not compel deliberate diaeresis. Singular ending is secure (B/L20_ordinaire.png).'},
 {'place':'L22 polyédres accent','A':'polyédres resolved','B':'polyédres / polyèdres','C':'polyédres / polyèdres','decision':'Retain B/C’s acute-first uncertainty. The thick short hooked accent does not settle its direction (B/L22_polyedres.png).'},
 {'place':'Detached-point coverage and representation','A':'two sites: after fonctoriellement as a literal period, below Dans as a drawing','B':'three off-line points: connaissance, fonctoriellement, Dans','C':'four off-line points: those three plus right of d’un','decision':'Select C’s union of four visibly distinct compact points. Root inspected every site once and selects B/C’s graphic treatment of the point below/right of fonctoriellement. Presence and approximate position are recorded; origin/function uncertainty is retained in notes and inventory, not made a doubtful word.'},
 {'place':'Remaining-doubts scope','A':'four lexical/alphabet doubts plus two point-origin entries','B':'three lexical/alphabet doubts plus three point-origin entries','C':'three lexical/alphabet doubts plus four origin and two semantic-emphasis entries','decision':'Final unresolved text has five entries: P alphabet, loc stop, inductive, ordinaire/ordïnaire, polyédres/polyèdres. Physically clear point positions and underline endpoints are recorded independently of unassigned origin or semantic emphasis.'}
]
unresolved=[
 {'place':'L7a first partition capital','reading':r'\mathcal{P}','alternatives':['P'],'confidence':'medium','reason':'The long left-returning oval favours the calligraphic family; a cursive capital does not uniquely identify the printed alphabet. Both page occurrences inspected separately.','crop':'crops/scan181/C/01_prefix_p.png'},
 {'place':'L11 loc ending','reading':'loc.','alternatives':['loc'],'confidence':'medium','reason':'A small separated terminal mark favours a stop, but may be a broken c exit.','crop':'crops/scan181/A/L11_ou_n_loc.png'},
 {'place':'L12a inserted parenthesis','reading':'inductive','alternatives':[],'confidence':'medium','reason':'Preferred word retained; compressed final t/i/v/e strokes and partly clipped ascender tips prevent full certainty.','crop':'crops/scan181/C/05_via_inductive.png'},
 {'place':'L20','reading':'ordinaire','alternatives':['ordïnaire'],'confidence':'medium','reason':'Compressed first-i region has three dark components, including two higher spots; deliberate diaeresis versus incidental additional marks remains unresolved. No terminal s.','crop':'crops/scan181/B/L20_ordinaire.png'},
 {'place':'L22 accented vowel','reading':'polyédres','alternatives':['polyèdres'],'confidence':'medium','reason':'The short thick hooked accent favours acute but does not securely exclude grave.','crop':'crops/scan181/B/L22_polyedres.png'}
]
review=[]
qmaps={1:[1,2],2:[7],3:[18],4:[19],5:[20],6:[22],7:[1],8:[3,4,5,6,8],9:[13,14,15,16],10:[17],11:[19,20,21,22]}
for i,q in enumerate(r['C']['C_doubt_review'],1):
 final=q['final_reading'];ev=q['ink_evidence'];status=q['decision']
 if i==2:final=diffs[7]['final'];ev=diffs[7]['evidence'];status='retained'
 if i==3:final=diffs[18]['final'];ev=diffs[18]['evidence']
 if i==5:ev=diffs[20]['evidence']
 if i==8:final=r'non des seuls faisceaux ou \inserted{$n$-}champs \unsure{loc.|loc} constants; t\uline{ous}';ev='All three half readings confirm the full baseline phrase. '+diffs[5]['evidence']+' '+diffs[6]['evidence']+' '+diffs[8]['evidence'];status='partly retained'
 ev+=' Main inspected '+', '.join(dict.fromkeys(diffs[j]['crop'] for j in qmaps[i]))+'.'
 review.append({'place':q['question'],'earlier':q['question'],'decision':status+': '+final,'evidence':ev})
for q in r['C']['C_note_review']:
 review.append({'place':'Earlier note: '+q['supplied_note'],'earlier':q['supplied_note'],'decision':q['decision'],'evidence':q['evidence']+' All three independent complete returns agree; conditional wording is not a proof claim.'})
inv=copy.deepcopy(r['C']['inventory'])
order=[1,0,3,4,5,6,7,8,9,10,2]
inv=[inv[i] for i in order]
inv[1]['details']+=' The final loc stop, inductive, ordinaire/ordïnaire and polyédres/polyèdres remain uncertain as recorded in the decision.'
inv[5]['first_words_or_objects']=r'(via un passage à la limite \unsure{inductive})'
notes=r'''**S181-notes.** The continuing proposal says that the discussion should be paraphrasable for excellent schemes using étale tubular neighbourhoods. In the two settings, a “type d’homotopie fin” **“se définirait”** by passage to a limit from the homotopy types associated with increasingly fine equisingular stratifications whose strata are nonsingular. The written first limit is not called inverse on this page. The raised partition prefix lies inside the quotation marks.

The proposed fine type **“incarnerait”** knowledge beyond the locally constant sheaves or n-champs, namely knowledge of tous, with the full parenthetical addition **“(via un passage à la limite inductive)”** attached before la connaissance. The word inductive remains textually uncertain. The author then says it **“dépendrait, en un sens convenable, fonctoriellement de X.”** These are conditional and qualified source formulations. They were read, not independently proved.

For a finite-type scheme over an algebraically closed field, the author writes that the strongest cohomological or homotopical finiteness theorems **“s’exprimeraient précisément”** in terms of the fine homotopy types and **“diraient”** that their ordinary constituent types are essentially finite polyhedra, and barred-m compact manifolds with boundary. The page ends **“ou de façon plus précise,”**. This is an unfinished formulation. The prose retains des types, singular cohomologique and homotopique, singular élément with surrounding plural words, and singular fin. No grammatical or mathematical repair is introduced. The accent in polyédres/polyèdres and the first-i marks in ordinaire/ordïnaire remain doubtful.

Root retains loc./loc because a small dark terminal mark is separated from the c exit by a pale interval, and retains inductive because the final joined strokes and clipped ascender tips do not settle its complete form. The two partition capitals were independently inspected and assigned the same preferred calligraphic family, with the alphabet doubt marked at the first. The lower stroke of barred m has a bowl and hump, so the equals alternative is resolved from the letter shape. Reading these signs and conditional statements involved no targeted proof, re-proof, computation, certificate, or independent mathematical recheck. All three reader check_events arrays are empty.

The short underline begins within o of tous, encoded t\uline{ous}; the long underline begins within é after the initial th of théorèmes and stops after finitude, encoded th\uline{éorèmes de finitude}. These record the physical spans. Whether the intended emphasis embraced the whole initial word is unassigned. Four compact off-line points are drawn below connaissance, below/right of fonctoriellement, below Dans, and below/right of d’un. Root inspected all four, including the last site reported only by C. Their presence is distinct from their unknown origin and function; none is asserted to be a sentence stop. All four quotation pairs retain high ticks rather than guillemets.

The page has 23 main baselines, four guided additions, two underlines and four detached points in one continuing paragraph. There is no cancelled text, independent marginal prose, displayed formula, mathematical diagram, heading, date, closing or signature. Author page **36** is at top centre, and archive pencil **181** is separate at lower left. H’s page-number note is editorial and agrees. Its claim that the sentence continues in another lot is not manuscript text; only the visible final comma is accepted at this stage. No English version or external source was consulted.
'''
text=(ROOT/'records/scan181/C/reading.tex').read_text()
text=text.replace('champs loc constants',r'champs \unsure{loc.|loc} constants')
text=text.replace('à la limite inductive)',r'à la limite \unsure{inductive})')
text=text.replace(r'\unsure{ordinaire}',r'\unsure{ordinaire|ordïnaire}')
abbr=copy.deepcopy(r['C']['abbreviations'])
abbr[2]['written']=r'\unsure{loc.|loc}'
viewed=(ROOT/'records/scan181/main_viewed_crops.txt').read_text().splitlines()
d=write_decision(181,'C',[],diffs,comparisons,unresolved,inv,notes,abbr,review,viewed,brief='briefs/brief_v12_scan181.md',workflow_note='Three fresh independent readers read whole/a/b exactly once, all 23 main baselines, four additions, all 11 supplied question rows and both earlier-note topics. A made 13 crops, B 14, C 17. Main read all fields of all three completed returns before image adjudication. It reused 17 saved crops and made three new crops for uncropped witness differences or a separate closing quotation boundary. All 20 root image inspections succeeded; no failed display or recropping occurred. A text-report output was truncated and reread in smaller complete chunks before any image adjudication. Physical underline spans, point coverage/representation, lexical uncertainty and accent alternatives were explicitly compared. No TeX engine or render was used.',text_override=text)
by={c['path']:c.get('bbox') for rep in r.values() for c in rep['crops']}
for x in d['differences']:
 cp=x['crop'];m=(ROOT/cp).with_suffix('.json');box=json.loads(m.read_text()).get('bbox') if m.exists() else by.get(cp)
 if box:
  if x.get('bbox')!=box:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=box
(ROOT/'records/scan181/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Partition P family',r'\unsure{\mathcal P|P}, then \mathcal P','181 L7a/L9: both new forms separately show long left-returning oval and upper-right bowl; first alphabet doubt retained.'),
 ('Partial physical underlines',r't\uline{ous}; th\uline{éorèmes de finitude}','181 L12/L16: starts fall within o and é respectively; no semantic whole-word emphasis inferred. Long rule stops before cohomologique.'),
 ('Local abbreviation stop',r'\unsure{loc.|loc}','181 L11: small separated dark terminal mark, but a broken c-exit remains possible. Earlier resolved loc/loc. forms do not decide this occurrence.'),
 ('Barred m',r'\overline m','181 L22: lower bowl and returning hump beneath separate straight bar; equals alternative resolved locally.'),
 ('First-i marks','ordinaire / ordïnaire','181 L20: three compact components, two higher and one lower; preferred ordinary spelling and supported diaeresis alternative retained without assigning deliberate function.')
])
register_note_statements(181,[
 {'place':'L1–L9; notes paragraph 1','statement':'The author conditionally proposes a fine homotopy type from a limit over increasingly fine equisingular stratifications in moderate and excellent-scheme settings.'},
 {'place':'L10–L14; notes paragraph 2','statement':'The proposed fine type would encode all sheaves or n-champs via the inserted inductive-limit qualification and depend functorially on X in a suitable sense.'},
 {'place':'L15–L23; notes paragraph 3','statement':'The author conditionally phrases strong finiteness statements through ordinary constituent types that are essentially finite polyhedra and compact manifolds with boundary; the formulation continues after this page.'}
])
