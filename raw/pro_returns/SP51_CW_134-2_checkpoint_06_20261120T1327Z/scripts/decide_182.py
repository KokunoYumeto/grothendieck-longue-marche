from decision_helpers import *
import copy

r=load_reports(182)
diffs=[row(r,'C',i) for i in range(20)]
cm={0:'main/01_profinis_quotes.jpg',1:'C/L1_insertion.png',2:'A/02_espaces.png',3:'A/03_aborder.png',4:'main/02_car_no_stop.jpg',5:'main/03_separator.jpg',6:'C/L8_geometriques_punctuation.png',7:'C/L13_cancelled_label.png',8:'A/06_intrigu_ending.png',9:'main/04_linearisation_quotes.jpg',10:'C/L19_first_constant.png',11:'C/L19_second_constant.png',12:'C/L20_left_isolated_mark.png',13:'C/L20_first_H_overwrite.png',14:'C/L20_first_H_overwrite.png',15:'C/L20_connector.png',16:'C/L21_degree.png',17:'C/L22_right_isolated_mark.png',18:'C/L23_reconstituer_accent.png',19:'C/L24_question_overwrite.png'}
for i,p in cm.items():diffs[i]['crop']='crops/scan182/'+p
diffs[0]['evidence']='The opening has two short elevated strokes, and the closing has two parallel slanted elevated strokes. Neither is angular guillemets; both boundaries inspected together.'
diffs[1]['evidence']='The raised parenthesis is complete. Its closing curve is followed by blank space; the lower right upturn is continuous with the long curved attachment guide, which returns to the gap after profinis. There is no separate comma after the parenthesis.'
diffs[2]['evidence']='The crop shows initial e/s movements, a long descending p, compact oval a, and joined low c/e/s ending. The final s has a downward hook, comparable with the visible ending of tels. All three readers and root resolve C’s doubt from the strokes.'
diffs[3].update(final=r'\unsure{aborder}',differs_C=True,differs_H=False,confidence='medium',evidence='Root selects A’s retained one-reading doubt against B/C’s resolution. The first small oval and later d loop support aborder, but the tall second stroke turns into an angular shoulder without a securely separable b bowl, and the compressed o/r bodies remain malformed. H’s English comparison is not evidence. The preferred word is unchanged from H’s uncertain reading.')
diffs[4]['evidence']='The r exit continues faintly into the short dark terminal hook; after it there is a clear gap before p. No separate abbreviation stop is visible. The written car is retained locally, independently of the page’s other car. forms.'
diffs[5]['evidence']='One continuous slightly rising rule runs from about (688,719) to (976,714). It has no arrowhead, star or written heading. Its drawing is preserved; H mentions it only in an editorial note.'
diffs[6].update(final='géométriques,',confidence='medium',evidence='A separate light but coherent slanted tail lies below and to the right of the final s, with a gap from its lower hook. All three readers and root retain this comma, which C omitted.')
diffs[7]['evidence']='The closed low rounded letter body and rightward connection survive under several oblique cancellation strokes. Latin a is preferred, with alpha retained; the separate right parenthesis is secure. H’s entirely unreadable label is replaced by the supported partial reading, without resolving the letter.'
diffs[8]['evidence']='After the g descender and low u-like movement there is a detached horizontal end stroke, but no secure independent e body beneath it. Literal intrigu- remains preferred, with a compressed intrigué retained as alternative. The grammar does not supply e.'
diffs[9]['evidence']='Both boundaries of linéarisation have two elevated short strokes. The closing pair is irregular and staggered, but neither boundary forms guillemets.'
diffs[10]['evidence']='The first constant ends in an upright t, a cross-stroke and a low rightward foot; the following gap contains no extra s. The local ending is resolved without agreement from grammatical number.'
diffs[11]['evidence']='The second constant independently ends in a t upright with crossbar and right foot. The distinctly curled s at the end of the adjoining tordus contrasts with this uninflected ending. No s is added.'
diffs[12].update(final='A short bent vertical nontext stroke above structure, drawn in TikZ',evidence='A compact dark upright has a slight down-right bend and short foot near (271,1837), wholly separated from the beginning of structure. Its physical form is reproduced without assigning a word, punctuation function or hand.')
diffs[13].update(kind='omission',evidence='Two separate near-horizontal remnants project leftward at different levels from the first H downstroke. Their two-level arrangement favours an old equals sign, as all three readers report. Because the upper remnant partly coincides with the live H crossbar, plus remains supported. The live H and i are preserved; H omits the old layer.')
diffs[14]['evidence']='The same crop shows a compact dark oval point, separated by pale space from the first H’s crossbar and uprights, around (1024,1876). Root accepts C’s separately drawn physical point; A/B did not separately reproduce it. It may be associated with the overwritten site, but its origin and mathematical role are unassigned.'
diffs[15].update(final=r'\mathrel{\unsure{\dashv|\to|-}}',differs_C=True,confidence='medium',evidence='Root selects A’s expanded shape reading against B/C’s plain-line-first reading. The horizontal shaft meets a short nearly upright terminal stroke that extends above and slightly below its level. Two diagonal arrowhead branches are not resolved. A dashv-shaped glyph is the closest literal form; a deficient right arrow and a plain connector with a terminal flourish remain alternatives. No adjunction or other mathematical meaning is attributed to the glyph.',consequential='Against C/H: the product connector has a right terminal upright; dashv-shaped is preferred with arrow/plain-line alternatives. H’s resolved right arrow is not supported at that certainty. This is a graphic reading, not an assertion of an adjunction relation.')
diffs[16].update(final=r'H^{\unsure{i\cdot j|i+j|ij}}',differs_C=False,confidence='low',evidence='The first exponent letter has a separate high dot. Between its body and the long returning j lies a compact lower wedge, without a resolved crossing bar. Root retains dot first and plus second, and accepts A’s additional geometric possibility that the wedge is a left-displaced j dot, leaving no operator. The added alternative enriches C’s existing uncertainty without changing its preferred reading; it is not a separate change against C.',consequential='Against H: the degree sign is not securely plus. Preserve the ink-led preferred i·j with i+j and ij alternatives; the usual expected product grading does not decide the tiny mark.')
diffs[17]['evidence']='The short mark near (1619,2077) has an initial downstroke, a kink and a down-right branch. It is separated by a broad gap from est-il and by blank space from the page edge. Its position and shape are reproduced, with no textual role assigned.'
diffs[18].update(final=r'\unsure{réconstituer|rêconstituer}',differs_C=True,confidence='medium',kind='abbreviation expanded or spelling modernised',evidence='Root selects B’s acute/circumflex uncertainty against A/C’s resolved acute. A raised compact angled mark is unmistakably present over the first e, unlike H’s unaccented form. It has a hooked or roof-like top whose few source pixels do not settle an acute with a hook versus a small circumflex. Réconstituer remains first; no normalization is made.')
diffs[19].update(kind='omission',marked_in_H='no',evidence='Root retains A/C’s one-reading doubt against B’s resolution. Two superposed descending curves and displaced lower strokes are visible. The live question mark is secure; crossing at the upper junction prevents confidently assigning the whole older curve or its chronological order. The older question mark remains doubtful. H’s note describes an overwrite on another sign, without an explicit doubtful reading, and omits the older layer from its text.')
point=row(r,'A',12,crop='crops/scan182/C/L19_first_constant.png',kind='omission',evidence='Root selects A/B’s retention over C’s rejection as coloured grain. The RGB crop shows a compact dark, slightly olive point near (818,1807), with a coherent centre distinct from the surrounding lighter texture. It is drawn below the first constant. Its colour and shape do not establish manuscript origin or authorship; neither punctuation nor a coefficient is assigned.')
diffs.append(point)

comparisons=[
 {'place':'L3 aborder','A':'aborder uncertain','B':'aborder resolved','C':'aborder resolved','decision':'Select A: the tall second stroke and compressed o/r lack securely separable bodies. One-reading uncertainty remains; no English comparison used (A/03_aborder.png).'},
 {'place':'L20 product connector','A':r'\dashv / \to / -','B':r'- / \to','C':r'- / \to','decision':'Select A’s visually closest right-upright form and retain all three supported alternatives. No meaning is assigned to the glyph (C/L20_connector.png).'},
 {'place':'L21 target exponent','A':'i·j / i+j / ij','B':'i·j / i+j','C':'i·j / i+j','decision':'Retain A’s additional ij possibility: the compact mark could be a displaced j dot. Preferred i·j remains unchanged from C; no separate C change is counted solely for the additional alternative (C/L21_degree.png).'},
 {'place':'L23 first-vowel accent','A':'réconstituer resolved','B':'réconstituer / rêconstituer','C':'réconstituer resolved','decision':'Select B’s acute-first uncertainty; the raised mark is present but its hooked/roof-like top does not settle acute versus circumflex (C/L23_reconstituer_accent.png).'},
 {'place':'L24 overwritten punctuation','A':'underlying ? uncertain; live ? clear','B':'underlying ? resolved; chronology uncertain','C':'underlying ? uncertain; live ? clear','decision':'Retain A/C’s old-character doubt: the upper curves cross and their complete assignment is insecure (C/L24_question_overwrite.png).'},
 {'place':'Detached-point and stroke coverage','A':'point below constant; stroke above structure; right-margin stroke','B':'same three sites as A','C':'rejects constant point as grain; adds point below first H crossbar; retains both strokes','decision':'Preserve the union of four physical marks after inspecting each site. Select A/B on the compact coloured point below constant, and C on the distinct oval below H’s crossbar. Origin and function remain unassigned. The two strokes are common to all readers.'},
 {'place':'H note on final overwrite','A':'marked_in_H=false','B':'marked_in_H=true','C':'marked_in_H=false','decision':'Select A/C’s metadata: H says only that the live mark is superposed on another sign. It describes the state, without a reading doubt. The older layer is an omission from H’s main text, not old text given live.'}
]
unresolved=[]
amap={0:3,1:7,2:8,3:13,4:15,5:16,6:19}
for i,u in enumerate(r['A']['unresolved']):
 u=copy.deepcopy(u);u['crop']=diffs[amap[i]]['crop'];unresolved.append(u)
unresolved.insert(6,{'place':'L23, first vowel of réconstituer','reading':'réconstituer','alternatives':['rêconstituer'],'confidence':'medium','reason':'The raised compact angled accent is present but its hooked/roof-like top does not securely distinguish acute from circumflex.','crop':diffs[18]['crop']})

review=[]
qmap={1:[2],2:[7],3:[8],4:[10,11],5:[15],6:[13],7:[16],8:[19],9:[0,1,2],10:[5],11:[7,8],12:[10,11,13],13:[15,16],14:[18,19]}
for i,q in enumerate(r['C']['C_doubt_review'],1):
 final=q['final'];ev=q['evidence'];status=q['decision']
 if i in [5,6,7,8]:final=diffs[qmap[i][0]]['final'];ev=diffs[qmap[i][0]]['evidence'];status='retained'
 if i==13:final=r'H^i(X,M)\times H^j(X,N)\mathrel{\unsure{\dashv|\to|-}}H^{\unsure{i\cdot j|i+j|ij}}(X,M\otimes N)';ev=diffs[15]['evidence']+' '+diffs[16]['evidence'];status='retained'
 if i==14:final=diffs[18]['final']+r' … entièrement \deleted{\unsure{?}}?';ev=diffs[18]['evidence']+' '+diffs[19]['evidence'];status='retained'
 ev+=' Main inspected '+', '.join(dict.fromkeys(diffs[j]['crop'] for j in qmap[i]))+'.'
 review.append({'place':q['question'],'earlier':q['question'],'decision':status+': '+final,'evidence':ev})
review.append({'place':'H doubt: aborder','earlier':r'\uncertain{aborder}','decision':r'retained: \unsure{aborder}','evidence':diffs[3]['evidence']+' Main crop '+diffs[3]['crop']+'.'})
for q in r['A']['notes']['C_earlier_notes_review']:
 review.append({'place':'Earlier C note: '+q['note'],'earlier':q['note'],'decision':q['decision'],'evidence':'All three complete page readings agree on the current-page source wording. References to other pages or English wording were not used as ink evidence.'})

inv=copy.deepcopy(r['C']['inventory'])
new=copy.deepcopy(r['A']['inventory'][9])
new['hand']='uncertain mark origin; no hand assigned'
new['details']='Compact point retained after root RGB crop inspection; coloured appearance does not establish manuscript origin.'
inv= [inv[i] for i in [0,2,3,4,5,6,7]]+[new]+[inv[i] for i in [10,8,9,11,12,13,1]]
for x in inv:
 if x['element']=='multiplicative formula within running prose':x['first_words_or_objects']=r'H^i(X,M) × H^j(X,N) \unsure{\dashv|\to|-} H^{\unsure{i·j|i+j|ij}}(X,M⊗N)'
 if x['element']=='isolated mark above structure':x['first_words_or_objects']='short bent upright with a small foot';x['hand']='uncertain mark origin; no hand assigned'
 if x['element']=='point below first H crossbar':x['hand']='uncertain association with overwritten site; no separate hand assigned'
 if x['element']=='isolated stroke right of est-il':x['hand']='uncertain mark origin; no hand assigned'

notes=r'''**S182-notes.** The page continues with the “complétés profinis” prime to p, qualified by the raised **“(au sens d’Artin-Mazur)”**, of the spaces under discussion. The characteristic parenthesis closes after k. No extra predicate is supplied from H’s English editorial comparison. The author says the programme is approachable in characteristic zero, while **“on prévoit de l’amusement supplémentaire, voire du mystère”** in positive characteristic for varieties refusing even birational lifting to characteristic zero. These source assertions were read, not proved.

After a single drawn separator, the author explicitly limits what he can formulate: **“je ne saurais à l’heure actuelle tirer un programme précis de développement de structures algébriques adéquates pour les exprimer.”** He will make a few marginal remarks. The comma after géométriques is faint but separately visible; no comma follows the raised Artin–Mazur parenthesis.

The new paragraph asks how much cohomological information, with variable coefficients, multiplication and possibly other cohomological operations, is needed to recover an ordinary homotopy type entirely. The source asks **“combien d’information cohomologique”** and **“est-il nécessaire d’avoir pour réconstituer le type d’homotopie entièrement”**; it is an open question, not a theorem checked in this work. The written first-vowel accent in réconstituer/rêconstituer remains doubtful. The page ends **“(disons,”**, leaving the qualification open. C’s earlier note quotes a later page, which was not imported into this page’s reading.

The product formula prompted inspection of its small signs. The overwritten sign beneath the first H favours equals over plus. The connector has a nearly upright right terminal stroke, best represented graphically by dashv, with right-arrow and plain-line alternatives. This notation asserts no adjunction or other mathematical relation. The target exponent has a compact mark without a secure crossbar: i·j is preferred, with i+j and ij retained, the latter because the mark might be a displaced j dot. The expected product grading did not determine the transcription. The H letters, i and j, argument delimiters, multiplication cross and tensor sign were independently read by all three readers. These were visual decisions; no mathematical deduction, computation, proof check or re-proof was performed, and all three reader check_events arrays are empty.

The two constant occurrences both visibly lack a final s; constant ou constant tordus is preserved. Aborder remains a one-reading doubt because of malformed b/o/r bodies. The cancelled a/alpha label and the intrigu-/intrigué ending remain uncertain. At the foot two superposed question-like curves are present; the old question mark and their exact chronology remain insecure. H’s description of an overwritten sign is not an explicit reading doubt, and its main text omits the old layer.

Four physical nontext marks are drawn: a small dark, slightly coloured point below the first constant around (818,1807); a short bent upright above structure around (271,1837); a compact oval below the first H crossbar around (1024,1876); and a kinked down-right stroke at the right of the est-il line around (1619,2077). Root accepts A/B’s compact point below constant and C’s point inside H after inspecting each saved crop. Colour does not settle origin, and the H point may belong to the overwritten site. None is assigned punctuation, a coefficient, a hand, or another mathematical role. Their physically clear positions are separate from uncertainty of origin or function.

The sheet has 24 main baselines, one raised guided addition, three prose paragraphs, one separator, one cancelled label and two overwritten sites. The formula runs in prose across two baselines. There is no independent display, mathematical diagram, verbal marginal note, author underline, heading, date, closing or signature. The author page is **37**; archive pencil **182** is separate. H’s historical and English notes remain editorial, and only this page’s two numbers were verified here. No external text was consulted.
'''

text=(ROOT/'records/scan182/C/reading.tex').read_text()
text=text.replace('comment aborder',r'comment \unsure{aborder}')
text=text.replace(r'\unsure{-|\to}H^{i\unsure{\cdot|+}j}',r'\mathrel{\unsure{\dashv|\to|-}}H^{\unsure{i\cdot j|i+j|ij}}')
text=text.replace('pour réconstituer',r'pour \unsure{réconstituer|rêconstituer}')
pointtex=r'''constant%
% Compact detached point near (818,1807), below the first constant; physical presence retained, origin unassigned.
\raisebox{0pt}[0pt][0pt]{\parbox{0pt}{\figure{\begin{tikzpicture}[overlay,x=1pt,y=1pt]
\fill (-28,-7) circle[radius=0.35pt];
\end{tikzpicture}}}} ou constant'''
text=text.replace('constant ou constant',pointtex)
text=text.replace(r'(0.16,0) -- (0.17,-0.06);',r'(0.16,0) -- (0.17,-0.04) -- (0.17,-0.06) -- (0.18,-0.06);')
viewed=(ROOT/'records/scan182/main_viewed_crops.txt').read_text().splitlines()
d=write_decision(182,'C',[],diffs[:12]+[diffs[20]]+diffs[12:20],comparisons,unresolved,inv,notes,r['C']['abbreviations'],review,viewed,brief='briefs/brief_v13_scan182.md',workflow_note='Three fresh independent readers each inspected whole/a/b once, all 24 main baselines, the one raised insertion, all 14 supplied C questions and the earlier-note topics. A made 16 crops, B 15, C 17. Main read every field and complete reading of all three returns before any image adjudication. One textual C-report display was aborted and a second exceeded context capacity; the remaining fields were then read fully in small chunks before images. Main reused 15 saved reader crops and made four new crops for uncropped witness differences: both quotation expressions, local car punctuation, and the separator. All 19 main inspections succeeded, with no failed image display or recropping. Root decided all reader and witness differences, including the union of four detached marks, connector and exponent alternatives, accent shape and old punctuation. Static text checks only; no TeX engine or render was used.',text_override=text)
by={c['path']:c.get('bbox') for rep in r.values() for c in rep['crops']}
for x in d['differences']:
 cp=x['crop'];m=(ROOT/cp).with_suffix('.json');box=json.loads(m.read_text()).get('bbox') if m.exists() else by.get(cp)
 if box:
  if x.get('bbox')!=box:x['reader_report_bbox']=x.get('bbox')
  x['bbox']=box
(ROOT/'records/scan182/decision.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
add_notation([
 ('Connector with right upright',r'\unsure{\dashv|\to|-}','182 L20: horizontal shaft ending in a short upright; graphic preference only, no adjunction meaning inferred.'),
 ('Tiny target degree',r'H^{\unsure{i\cdot j|i+j|ij}}','182 L21: compact wedge between letters, no resolved crossbar; possible displaced j dot explicitly retained.'),
 ('Local characteristic abbreviation','car. / car','182 L1/L3/L7 have stops; L5 car before p>0 has a continuous exit and no detached stop.'),
 ('Raised acute or circumflex',r'\unsure{réconstituer|rêconstituer}','182 L23: compact hooked/roof-like mark over first e, secure presence but uncertain shape; no unaccented normalization.')
])
register_note_statements(182,[
 {'place':'L1–L7; notes paragraph 1','statement':'The author anticipates an approachable characteristic-zero programme and additional difficulty or mystery in positive characteristic for varieties refusing even birational lifting.'},
 {'place':'L8–L12; notes paragraph 2','statement':'The author explicitly says he cannot presently formulate a precise programme of adequate algebraic structures from these geometric considerations.'},
 {'place':'L13–L24; notes paragraph 3','statement':'The author asks how much cohomological information with variable coefficients, multiplication and other operations is needed to recover an ordinary homotopy type; the question continues beyond this page.'}
])
