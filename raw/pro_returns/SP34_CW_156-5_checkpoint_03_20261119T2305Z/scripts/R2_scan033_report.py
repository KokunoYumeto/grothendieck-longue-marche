from pathlib import Path
from datetime import datetime,timezone
import json,re
b=Path('/workspace/scratch/4770596940a0');out=b/'out/readers/R2';crops=json.loads((out/'crops033.json').read_text())
D=[]
def row(id,place,C,H,reading,ink,confidence,kind,crop,against_C,against_H,marked_in_H=False):
 D.append(dict(id=id,place=place,C=C,H=H,reading=reading,ink=ink,confidence=confidence,kind=kind,crop=crop if isinstance(crop,list) else [crop],against_C=against_C,against_H=against_H,marked_in_H=marked_in_H))
row('D01','Before 1°)',r'\deleted{\unsure{R|P}}',r'\struck{Or}',r'\deleted{\unsure{R|P}}','Overlapping loop, upright and oblique cancellation survive; no secure separate initial O plus r. The rightward extension is recorded separately in D02.',.45,'C doubt retained / H difference','cancelled_initial',False,True)
row('D02','Immediately right of cancelled initial glyph','No distinct graphic','No distinct graphic','Rightward arrow-like extension, drawn in TikZ; function unresolved','Two roughly horizontal strokes extend right from the patch; a diagonal terminal gives an arrow-like head. It may belong to the old glyph/cancellation rather than be an independent implication.',.74,'omitted drawing','cancelled_initial',True,True)
row('D03','First F in 1°)',r'\unsure{F|\mathcal F}',r'F',r'\unsure{F|\mathcal F}','Upright, short middle arm, detached rounded upper arm; plain F preferred but alphabet distinction is not secure.',.70,'C doubt retained','initial_F',False,True)
row('D04','Sideways note, first word',r'\unsure{voir}',r'\uncertain{va se simplifier} [first word]','va','After clockwise rotation, short v-shaped scoop followed by a low closed a-like loop; no separate i/r strokes.',.85,'C doubt resolved / H uncertainty cleared',['margin_rotated','margin_first'],True,True,True)
row('D05','Sideways note, second word',r'\unsure{une|sa}',r'\uncertain{va se simplifier} [second word]','se','Compact angled s-like start and low e-like continuation, not the three-wave sequence expected for une.',.80,'C doubt resolved / H uncertainty cleared',['margin_rotated','margin_first'],True,True,True)
row('D06','Sideways note, long word',r'\unsure{simplification}',r'\uncertain{va se simplifier} [third word]','simplifier','Dotted initial region, descending/ascending pli group, tall f and short low terminal. Terminal does not supply a distinct cation sequence.',.80,'C doubt resolved / H uncertainty cleared',['margin_rotated','margin_first'],True,True,True)
row('D07','End of sideways note','cf plus bas',r'cf plus \ill{}','cf plus bas','Rotated view gives cf, p-descender/l-loop/u-s movement, and the final compressed bas.',.86,'H illegible resolved','margin_last',False,True,True)
row('D08','Long line beside left note','Sideways note comment, no explicit divider graphic','Note expressly describes long separating line','Continuous separating boundary, drawn with the margin text','Fine long stroke stands to the right of the sideways words and runs from beside 1°) to just above the cancelled draft. It does not strike through the note.',.95,'graphic inventory / C omission',['margin_rotated','case1','conclusion'],True,False,True)
row('D09','After initial set inclusion in 2°)',r'F\setminus G Soit',r'F\smallsetminus G. Soit',r'F\setminus G Soit','No distinct stop between G and Soit in the enlarged line.',.88,'H punctuation','case2',False,True)
row('D10','Bracketed pair, superscript after first unprimed A',r'\deleted{\unsure{\prime|\ast|?}}','Omitted',r'\deleted{\unsure{\prime|\ast|?}}','Small heavily retraced angular hook/fork, not a clear surviving prime; the crossing cannot be separated confidently.',.42,'C doubt retained / H deletion omitted',['bracket','superscript1'],False,True)
row('D11','Bracketed pair, superscript before circle after second A',r'\deleted{\unsure{\prime|\ast|?}}','Omitted',r'\deleted{\unsure{\prime|\ast|?}}','Separate small angular patch precedes the open circle; it is not part of the circle or the parenthesized F.',.45,'C doubt retained / H deletion omitted',['bracket','superscript2'],False,True)
row('D12','Under bracketed pair of inclusions','Underline with short upturned ends','Unmarked text','Long underbracket with upturned ends, reproduced in TikZ','Thin line spans both formulae, rising at both ends; distinct from the cancelled On a below.',.98,'H graphic omission','bracket',False,True)
row('D13','Relation in prouvons que A′ ... A',r'A\prime=A',r'A\prime=A',r"A'\deleted{\unsure{\in|\subset}}=A",'Focused 7x view separates two very heavy final horizontal bars from a thinner curved tip above, a left curved connection and a short interior bar. Final = is preferred; the earlier relation favours element-of, with subset weaker. Chronological layer interpretation remains less secure than the visible strokes.',.80,'overwritten relation omitted by C/H',['A_equals_A','relation_focused'],True,True)
D[-1]['initial_proposal']=r"A'\unsure{=|\in}A"
D[-1]['initial_proposal_saved_in']=str(out/'scan033.initial.tex')
D[-1]['recheck_note']='The initial TEX existed before the parent requested a focused recheck; no JSON existed then. Recheck changed the representation to final = plus an uncertain overwritten predecessor.'
row('D14','Parenthesis after prouvons que A′=A',r"d'où A\in F",r"d'où A'\in F",r"d'où A\in F",'A has no detached upper-right prime. Its crossbar/continuation runs toward the following membership sign at ordinary height.',.95,'C/H difference resolved to C','A_equals_A',False,True)
row('D15','Cancelled words at end of 2°) block',r'\deleted{On a}',r'\struck{Or}',r'\deleted{On a}','Large O, low joined material and a terminal a-like loop beneath the horizontal strike; resembles the earlier cancelled On a on this page.',.81,'H deleted wording','bracket',False,True)
row('D16','Cancelled word after donc A∈F′',r'\deleted{\unsure{et}}',r'\struck{et}',r'\deleted{et}','An e-loop and tall crossed t remain beneath the cancellation.',.88,'C doubt resolved','deleted_et',True,False)
row('D17','Interlinear insertion above cf lemme plus bas',r"il suffirait F'\ll F",r"i.e. sachant F'\ll F",r"il suffirait F'\ll F",'Dotted i and l are followed by s and two tall f strokes; short remainder and terminal t fit suffirait. Two independent angle tips give <<.',.90,'H insertion wording',['lemma_insertion','insertion_rotated'],False,True)
row('D18','Immediately after F′≼F before cf','Cancelled closing )','No cancellation recorded','Cancelled closing ) retained','Looped/crossed parenthesis lies at the left end of the insertion leader, before cf.',.85,'H deletion omission','lemma_insertion',False,True)
row('D19','After closing parenthesis of lemma reference',r'et \deleted{\unsure{bien}}',r"\uncertain{d'autre part}",r'et \deleted{\unsure{bien}}','Short et-like loop; next word has tall b-like stem and dotted/reduced ending. Low stroke crosses/underlies that ending. bien remains uncertain, and a mere underline rather than cancellation cannot be excluded.',.54,'C doubt retained / H wording and state','et_bien',False,True,True)
row('D20','Cancelled symbol before A,A′∈F′',r'\deleted{\unsure{F|\in}}',r'\struck{\exists}',r'\deleted{\unsure{F|\in}}','Left upright with upper and middle arms survives diagonal cancellation; lower curve prevents certain identification. No clear unambiguous right upright for an existential sign.',.47,'C doubt retained / H deleted symbol','cancelled_quantifier',False,True)
row('D21','Donc ... prouvé',r'\unsure{on a}','on a',r'\unsure{on a}','Two very faint low groups occur between Donc and prouvé. Preferred words fit traces, but their individual letters remain weak.',.57,'C doubt retained','Donc_on_a',False,True)
row('D22','Overwritten material under initial A′ in Donc statement',r'\deleted{\unsure{F|A}}','No overwritten predecessor recorded',r'\deleted{\unsure{F|A}}','Live A′ overlays a capped upright and extra horizontal/curved strokes. Earlier F or A cannot be separated securely.',.45,'C doubt retained / H revision omitted','overwritten_A',False,True)
row('D23','d’où ... qed parenthesis',r"(d'où A'\in F\setminus G\deleted{)}, qed)",r"d'où A'\in F\smallsetminus G (qed)",r"(d'où A'\in F\setminus G\deleted{)}, qed)",'Opening parenthesis before d’où is present; old closing parenthesis after G is crossed. No independent opening parenthesis before qed.',.91,'H punctuation and deletion','qed',False,True)
row('D24','Sentence following qed','Sinon on aurait','Si on avait','Sinon on aurait','After Si the compressed n/on material remains; a separate on precedes the longer aurait group with its internal low stroke.',.87,'H wording','Sinon',False,True)
row('D25','Above et in final live parenthesis, x775–930/y1575–1645','Omitted','Omitted','Pale left-pointing arrow-like trace, reproduced in TikZ; status and attachment uncertain','Near-horizontal pale shaft to the right, two angled arms meeting at the left, darker remnants near upper arm. The trace may be erased; no word or definite insertion target is assigned.',.77,'omitted drawing / state uncertain','pale_mark',True,True)
row('D26','Raised On suppose in cancelled draft','Insertion under same deletion','Full text in explanatory note, said cancelled with rest','On suppose b) i.e. φ induit F′\\G′ ≃→ F\\G, inserted and cancelled with block','Text is above the line, with a long curved leader beneath; diagonal hatch strokes cut the insertion as well as the draft.',.94,'retention review / insertion',['draft_insertion','cancelled_draft'],False,False,True)
row('D27','Before Soit in cancelled draft','No literal opening parenthesis','Literal ( before Soit','No literal opening parenthesis','Apparent left parenthesis continues rightward as the insertion leader under On suppose.',.91,'H punctuation / leader interpretation','cancelled_draft',False,True)
row('D28','After strate in cancelled draft','ouverte',r'\ill{}','ouverte','Rounded o and separate low u/verte sequence remain legible between diagonal hatch strokes.',.93,'H illegible resolved','draft_strate',False,True,True)
row('D29','Revision between ouverte and F′',r'\deleted{dans \unsure{la}} de','No deleted wording; de remains',r'\deleted{dans \unsure{la}} de','dans is readable under a crossing. Following patch is very heavily worked over; la remains a low-confidence candidate, with live de retraced in/after the patch.',.47,'C doubt retained / H revision omitted',['draft_strate','draft_old_la'],False,True,True)
row('D30','Underline in cancelled draft','Underline includes F′','No underline','Underline ends before F′','The straight underline terminates left of the live F′, after the revised de region.',.93,'underline extent','draft_strate',True,True)
row('D31','After l’unique élément',r'\deleted{de}','Omitted',r'\deleted{de}','Small d-loop plus low e crossed horizontally, before tel.',.93,'H deletion omission','draft_element',False,True)
row('D32','Final Prouvons formula in cancelled draft','Included in cancelled block','Included in cancelled block','Formula retained inside draft deletion, with scope uncertainty recorded','All direct diagonal hatch strokes end above this last line. Cancellation of this line is inferred from its association with the abandoned draft. Formula itself is clear; the apparent stroke after its left parenthesis group belongs to the q-descender in unique above.',.69,'deletion-extent review',['draft_deletion_extent','draft_last_formula','draft_element'],False,False,True)
row('D33','After soit U in final block','Comma','Period','Comma','Long curved descending comma follows U; it is not a round stop.',.96,'H punctuation','bottom',False,True)
row('D34','First I superscript in final block',r'\unsure{\ast|k|+}',r'*',r'\unsure{\ast|k|+}','Short stem with forked branches; stylized asterisk preferred, k/cross remain possible at the literal stroke level.',.63,'C doubt retained','bottom_sets',False,True)
row('D35','Overwritten operator between F′ and G′',r'\deleted{\unsure{\times|\setminus}}','No predecessor',r'\deleted{\unsure{\times|\setminus}}','Dense angular crossing patch; earlier multiplication cross or difference slash not separable.',.42,'C doubt retained / H revision omitted','bottom_sets',False,True)
row('D36','Live operator between F′ and G′',r'\unsure{\setminus}',r'\smallsetminus',r'\unsure{\setminus}','A descending diagonal is present in the patch; its live layer is not fully isolated, so difference remains a preferred uncertain reading.',.54,'C doubt retained','bottom_sets',False,True)
row('D37','Second I′ superscript in final block',r'\ast',r'*',r'\unsure{\ast|k|+}','The same forked stem/branch form as first superscript occurs here; the second occurrence does not independently remove its literal ambiguity.',.66,'new uncertainty','bottom_sets',True,True)
row('D38','Cancelled triangular glyph after I',r'\deleted{\unsure{A|\Delta}}','Omitted',r'\deleted{\unsure{A|\Delta}}','Two oblique sides and heavy cross/cancellation survive, insufficient to decide A versus Delta.',.47,'C doubt retained / H revision omitted',['bottom_ordernes','bottom_deleted_triangle'],False,True)
row('D39','ens before d’indices','ens','ens.','ens','No distinct stop between the terminal low s movement and following d’indices.',.87,'H punctuation','bottom',False,True)
row('D40','Outer parenthesis opened at parties','Left unclosed on this page','Closing parenthesis supplied after I′(=F′)','Leave outer parenthesis unclosed','After I′(=F′), only that inner closing parenthesis and the stop are visible, then On a.',.95,'H supplied punctuation','bottom',False,True)
row('D41','Orders around later-lemma reference',r"F'\preceq F; F'\ll F",r"F'\preccurlyeq F; F'\ll F",r"F'\preceq F; F'\ll F",'Heavily retraced curved order sign with lower stroke retained; insertion has two separate left angle tips. Macro spelling difference is not counted.',.88,'C notation-table review',['preceq','insertion_rotated'],False,False)
row('D42','Least-cell notation and two stratum superscripts',r"F^{A'}; A'^{\circ(F')}; A^{\circ(F)}",r"F^{A'}; A'^{\circ(F')}; A^{\circ(F)}",r"F^{A'}; A'^{\circ(F')}; A^{\circ(F)}",'A′ is raised above-right of F. Open rings and parenthesized F′/F are individually visible; far-right closing edge is tight/cropped.',.95,'C notation-table review',['case2','bracket','superscript2'],False,False)
row('D43','Lower arrows','Tilde above right arrow, then double bidirectional arrow','Same','Tilde above right arrow, then double bidirectional arrow','The insertion map has a single right arrow under a tilde; later b⇔c has two horizontal shafts and both heads.',.97,'C notation-table review',['draft_insertion','bottom'],False,False)

cd_values=[r'R|P',r'F|\mathcal F','voir','une|sa','simplification',r'\prime|\ast|?',r'\prime|\ast|?','et','bien',r'F|\in','on a','F|A','la',r'\ast|k|+',r'\times|\setminus',r'\setminus',r'A|\Delta']
cd_ids=['D01','D03','D04','D05','D06','D10','D11','D16','D19','D20','D21','D22','D29','D34','D35','D36','D38']
resolved={3,4,5,8}
cd=[]
for i,(val,di) in enumerate(zip(cd_values,cd_ids),1):
 rr=next(x for x in D if x['id']==di)
 cd.append({'occurrence':i,'C_doubt':val,'difference_id':di,'status':'resolved/replaced' if i in resolved else 'retained','reading':rr['reading'],'crop':rr['crop']})

I=[]
def inv(kind,position,first,crop,state='live',notes=''):
 I.append({'id':f'I{len(I)+1:02d}','kind':kind,'position':position,'first_words_or_objects':first,'state':state,'crop':crop if isinstance(crop,list) else [crop],'notes':notes})
inv('text','top centre','32.','case1',notes='Manuscript foliation is 32.; archive scan is 33. Whole image supplies foliation.')
inv('deletion','top left before 1°)','uncertain R/P','cancelled_initial','cancelled')
inv('drawing','beside cancelled initial','rightward arrow-like extension','cancelled_initial','function uncertain')
inv('text','upper three lines','1°) F\\G⊂F′\\G′; Tout A…','case1')
inv('deletion','third upper line after donc','A∈','case1','cancelled')
inv('margin note','left edge, bottom-to-top','va se simplifier, cf plus bas',['margin_rotated','margin_first','margin_last'])
inv('drawing','left divider from beside 1° to above cancelled draft','long thin separating rule',['case1','margin_rotated','conclusion'])
inv('text','2°), first and second lines','F′\\G′⊂F\\G; Soit A′… prouvons…','case2')
inv('deletion','second line of 2°)','On a','case2_deleted1','cancelled')
inv('text','2°), third line','Soit A le plus petit él. de F^{A′} donc','case2')
inv('display','right side of third line, bracketed','A′⊂A…; A′°(F′)⊂A°(F)','bracket')
inv('deletion','first A exponent in bracket','small cancelled prime/star-like sign','superscript1','cancelled, identity uncertain')
inv('deletion','second A exponent in bracket before circle','small cancelled prime/star-like sign','superscript2','cancelled, identity uncertain')
inv('drawing','under paired inclusions','underbracket with upturned ends','bracket')
inv('text','following line','prouvons que A′=A (d’où A∈F)','A_equals_A')
inv('deletion','under final = in prouvons que','earlier ∈/⊂-like relation','relation_focused','overwritten; earlier identity uncertain')
inv('deletion','end of same line','On a','bracket','cancelled')
inv('text','Je dis, first three lines','Je dis que A∈F\\G… absurde','jedis1')
inv('deletion','after first absurde','Mais','jedis1','cancelled')
inv('text','next line','Donc A∈F\\G, donc A∈F′','jedis2')
inv('deletion','after donc A∈F′','et','deleted_et','cancelled')
inv('display','same line right','A°(F)=A°(F′)','jedis2')
inv('text','parenthetical line','car F′≼F… cf lemme plus bas','jedis2')
inv('insertion','above that parenthesis','il suffirait F′≪F',['lemma_insertion','insertion_rotated'],'inserted')
inv('drawing','under il suffirait','curved insertion leader','lemma_insertion',notes='Leader and crossed old parenthesis are distinguishable; insertion macro and TikZ leader record placement.')
inv('deletion','before cf','old closing parenthesis','lemma_insertion','cancelled')
inv('text','after new closing parenthesis','et','et_bien')
inv('deletion','after et','uncertain bien','et_bien','cancellation preferred; underline alternative remains')
inv('deletion','before A,A′','uncertain F/∈','cancelled_quantifier','cancelled')
inv('text','next two lines','A,A′∈F′ tels que… ce qui prouve A=A′','jedis2')
inv('text','Donc summary line','Donc on a prouvé que A′∈F′\\G′','Donc')
inv('deletion','under first A′ of summary','uncertain F/A','overwritten_A','overwritten')
inv('display','next line left','⇒ A′∈F','Donc')
inv('text','following live lines','Prouvons qu’on a A′∉G (d’où…qed)','qed')
inv('deletion','after F\\G before qed','closing parenthesis','qed','cancelled')
inv('text','same line right and next line','Sinon on aurait A′∈G, on aurait A′⊂|G|=|G′|',['Sinon','conclusion'])
inv('drawing','above et in last live parenthesis','pale left-pointing arrow-like trace','pale_mark','possibly erased; function/attachment uncertain')
inv('text','last live parenthetical line','comme A′∈F′ et G′≤F′) A′∈G′, absurde','conclusion')
inv('deletion','lower draft as a block','b)⇒c), Soit…Prouvons…',['cancelled_draft','draft_deletion_extent'],'diagonally hatched; last-line scope inferred')
inv('insertion','above cancelled draft first line','On suppose b) i.e. φ induit F′\\G′ ≃→F\\G','draft_insertion','inserted then cancelled with draft')
inv('drawing','under raised draft insertion','long curved leader','draft_insertion','within cancelled block')
inv('text','cancelled draft first two lines','Soit A∈F\\G, prouvons que A°(F) est une strate ouverte…','cancelled_draft','cancelled')
inv('deletion','within underlined phrase','dans, uncertain la','draft_old_la','locally cancelled before whole draft cancellation')
inv('text','underlined phrase and following F′','strate ouverte [revision] de F′','draft_strate','cancelled with draft',notes='Underline ends before F′; strate has very reduced/dot-like a.')
inv('text','next draft line','Soit A′∈F′\\G′ l’unique élément…φ(A′)=A','draft_element','cancelled')
inv('deletion','after élément','de','draft_element','local cancellation')
inv('display','last draft line','Prouvons A′°(F′)=A°(F)','draft_last_formula','block cancellation inferred; no direct hatch across this line')
inv('text','new lower argument','b⇔c','bottom')
inv('deletion','after b⇔c','Posons','bottom','cancelled')
inv('display','next phrase','On a |F|\\|G|=|F′|\\|G′|, soit U,','bottom')
inv('text','penultimate/last lines','Posons F\\G=I*, F′\\G′=I′* (parties ouvertes…','bottom_sets')
inv('deletion','between F′ and G′','crossing operator patch','bottom_sets','overwritten/cancelled predecessor uncertain')
inv('text','last two lines','des ens d’indices ordonnés I,… (=F), I′(=F′). On a','bottom')
inv('deletion','after I','A/Delta-like triangle','bottom_deleted_triangle','cancelled')

now=datetime.now(timezone.utc).isoformat();start=(out/'start033.txt').read_text().strip()
check=[{'statement_id':'R2.scan033.nonempty_strata_inclusion_implies_equal_cells','date':now,'who':'R2; model inherited/not otherwise exposed; effort inherited; run scan033','type':'targeted proof check','outcome':'Conditional local inference checked: if the strata S(B), B in F′, are nonempty and pairwise disjoint, then S(A′) subset S(A) forces A′=A. Choose a point of nonempty S(A′); it lies in both strata, contradicting disjointness unless labels coincide. This checks the last inference after A,A′∈F′ and the stated stratum inclusion. It does not establish the earlier common-cell stratum equality, the existence of the least cell, or the whole 1°)/2°) proof. The later lemma was not opened.'}]
report={
'scan':'033','manuscript_page':'32.','reader':'R2','effort':'inherited','start_utc':start,'end_utc':now,
'sources':{'whole':str(b/'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033.jpg'),'C':str(b/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan033.tex'),'H':str(b/'working/H/scan033.tex'),'C_doubts':str(b/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_doubts.md'),'C_notes':str(b/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/J156-5-04_notes.md'),'S':str(b/'source/SP34_CW_156-5_sweep3/readings/156-5_CORRECTIONS.tsv')},
'independence':{'other_readers_or_root_decisions_consulted':False,'later_pages_opened':False,'OCR_used':False,'image_reading':'Whole image, then _a and _b; C/H consulted after that; all words inspected, including agreed words. All 40 listed crops actually emitted and viewed. The earlier attempted whole-image call that returned a context-truncation message was not counted; the whole image was re-emitted and read.'},
'images_viewed':[{'order':1,'path':str(b/'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033.jpg')},{'order':2,'path':str(b/'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033_a.jpg')},{'order':3,'path':str(b/'source/SP34_CW_156-5_scans/J156-5-04_156-5_scan033_b.jpg')}]+[{'path':x['path'],'crop_id':x['id']} for x in crops],
'crops':crops,'differences':D,'C_doubt_resolutions':cd,
'C_other_reviews':[{'source_row':'notation table 33, 1° line 1','difference_ids':['D03']},{'source_row':'notation table 33, 2° line 3','difference_ids':['D10','D11','D42']},{'source_row':'notation table 33, Je dis lines 4–5','difference_ids':['D41']},{'source_row':'notation table 33, bottom two blocks','difference_ids':['D43']},{'source_row':'notation table 33, last paragraph line 2','difference_ids':['D34','D37']},{'source_row':'doubts prose-vs-math row 33, d’où A∈F','difference_ids':['D14']}],
'C_notes_review':{'cf_lemme_plus_bas':'Read as written. No later page opened to supply or verify the lemma.','cf_plus_bas':'Sideways reference ends cf plus bas.','ending':'New b⇔c argument ends On a, without supplying continuation.'},
'S_row_decisions':[{'scan':'033','rows_found':0,'decision':'No scan033 correction row in the provided S correction table; no S-driven replacement.'}],
'inventory':I,
'notation':{'families':'Plain F/G preferred throughout; initial F retains F/mathcal F uncertainty. G has an inward lower terminal. Primes are individually retained.','orders':r'G\leq F and G′\leq F′ have angle plus lower line; F′\preceq F is heavily retraced; F′\ll F has two separate tips.','supports_and_strata':'Vertical bars denote supports in the transcription. Raised open circles followed by parenthesized F/F′ are transcribed literally; the cancelled draft equality has no extra prime after the parenthesis—the nearby stroke belongs to unique above.','indices':'F^{A′} has a raised A′. Both I/I′ superscripts preserve asterisk/k/cross ambiguity.','revision_layers':'Overwritten signs are serialized using deleted macros before their live successor; this records the layers without pretending they occupied separate manuscript positions.'},
'remaining_doubts':[{'difference_id':x,'issue':next(d for d in D if d['id']==x)['reading']} for x in ['D01','D02','D03','D10','D11','D13','D19','D20','D21','D22','D25','D29','D32','D34','D35','D36','D37','D38']],
'notes_while_reading':['Margin was rotated clockwise 90 degrees; reading va se simplifier emerged from the rotated ink, replacing C’s three uncertain words.','The pale mark was first noticed as a faint angular trace in the live conclusion. A dedicated crop, requested without any supplied reading, established its arrow-like shape; its status and target remain open.','The focused A′/A relation recheck was likewise supplied without another reading. Initial TEX remains saved; later report distinguishes heavy = from thinner predecessor strokes.','The terminal circle/prime groups and the underbracket were checked at the page edge. No missing right-edge letter was invented.','Last Prouvons line of the draft is below the hatch endpoints. The surrounding draft association supports retaining its cancellation, but this is a scope inference, not a visible crossing through that line.','No attempt was made to make the manuscript proof true by changing the ink. In particular d’où A∈F remains unprimed despite the mathematical temptation to write A′.'],
'check_events':check,
'visual_checks':['All three source images viewed in required order.','All 40 crop recipes correspond to actual emitted images.','Every one of 17 C unsure occurrences has its own decision; C notation and prose-versus-math rows are additionally covered.','Each H difference, including punctuation, omitted revisions and uncertainty-state changes, is represented.','Small pale mark and heavily traced relation received focused source-only rechecks.'],
'syntax_checks':[],
'not_performed':['No OCR.','No LaTeX compilation.','No independent re-proof of the page or its invoked later lemma.','No comparison with other readers or root decisions.','No later page opened.'],
'flag_convention':'against_C/against_H compares proposed wording, uncertainty candidate/state and insertion/deletion state, including omitted drawings; equivalent macro spellings and spacing do not count. marked_in_H denotes a local uncertainty/illegible marker or an explicit relevant H note, not merely ordinary strikethrough.',
'counts':{'differences_and_reviews':len(D),'C_doubts':len(cd),'C_doubts_resolved_or_replaced':len(resolved),'C_doubts_retained':len(cd)-len(resolved),'inventory_items':len(I),'crops_viewed':len(crops),'mathematical_check_events':len(check)},
'proposed_tex':str(out/'scan033.tex'),'initial_tex_snapshot':str(out/'scan033.initial.tex')}
# Structural validation only; no TeX engine is run.
s=(out/'scan033.tex').read_text();body='\n'.join(l.split('%',1)[0] for l in s.splitlines())
balance=0
for k,ch in enumerate(body):
 if ch in '{}':
  n=0;j=k-1
  while j>=0 and body[j]=='\\':n+=1;j-=1
  if n%2==0:
   balance+=1 if ch=='{' else -1
   assert balance>=0
assert balance==0
assert body.count('$')%2==0
for env in ['tikzpicture','scope']:
 assert body.count('\\begin{'+env+'}')==body.count('\\end{'+env+'}')
assert len(cd)==17 and len(set(x['id'] for x in D))==len(D)
ids={x['id'] for x in crops}
for d in D:
 assert all(c in ids for c in d['crop'])
 assert all(isinstance(d[f],bool) for f in ['against_C','against_H','marked_in_H'])
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in I)
report['syntax_checks']=[{'type':'structural syntax check','outcome':'Balanced unescaped braces, paired dollars, paired tikzpicture/scope environments; no compilation.'},{'type':'report schema check','outcome':'17 C doubt decisions present; difference IDs unique; all crop IDs resolve; comparison flags boolean; inventory kinds restricted to permitted values.'}]
(out/'scan033.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False));print('end_utc',now)
