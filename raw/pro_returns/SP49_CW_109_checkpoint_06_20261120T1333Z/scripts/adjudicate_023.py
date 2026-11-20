"""Root adjudication of scan023; execute only after all three final returns."""
from common import *
R=load_page(23)
T={r:(W/f'readers/023/{r}/reading.tex').read_text() for r in 'ABC'}
ch={r:{x['id']:x for x in R[r]['changes']} for r in 'ABC'}
text=T['A']; Q=chr(96)*2; q=chr(96)
def repl(a,b):
 global text
 assert a in text,a
 text=text.replace(a,b,1)
repl(r'\deleted{8}3 of',r'\deleted{8}3\unsure{,|.} of')
repl(Q+"haven't''","haven't''")
repl(r'\deleted{'+Q+"now or never''}",Q+r"\deleted{now or never''}")
repl(r'\makebox[1.2cm][l]{164}line',r'\makebox[1.2cm][l]{164}\raisebox{0.7ex}{.}\,line')
repl(r'\deleted{\unsure{'+Q+'}} end',r'\deleted{\unsure{'+Q+'|'+q+'}} end')
viewed=json.loads((W/'records/root_023_viewed.json').read_text())
decisions=[]
def ap(n):return f'readers/023/A/crops/{n:02}.jpg'
def add(id,place,c,final,abc,evidence,crops,confidence='medium',kind='other',diff=True,consequential=None):
 d=dict(id='023-'+id,place=place,c=c,h=None,final=final,readers=dict(zip('ABC',abc)),evidence=evidence,crops=crops if isinstance(crops,list) else [crops],confidence=confidence,kind=kind,diff_c=diff,diff_h=False,marked_in_H=False)
 if consequential:d['consequential']=consequential
 decisions.append(d)
def a(id):return ch['A'][id]
def b(id):return ch['B'][id]
def cc(place):
 matches=[d for d in R['C']['changes'] if place.lower() in (d['place']+' '+d['id']).lower()]
 assert len(matches)==1,(place,[d['id'] for d in matches])
 return matches[0]

x=a('first-reference-digit')
add('old-digit',x['place'],x['c'],x['reading'],[x['reading'],r'\deleted{\unsure{8|9}}3',r'\deleted{8}3'],'Root adopts A/C at medium confidence: the older sign has a separately closed lower loop and a faint upper loop remnant under the larger3. Its lower contour closes rather than ending in an open descending tail. B retained8/9 because the upper junction is overwritten; that limitation is recorded, while the two-level loop structure supports8.',ap(1))
x=b('p156-low-mark')
add('low-punctuation',x['place'],r'3 of',r'3\unsure{,|.} of',['3 of',r'3\unsure{,|.} of','3 of'],'Root confirms a detached dark pointed mark below/right of3. Its left edge descends, favouring comma, but the short blunt shape also allows a stop. This is separate from the overwritten digit; it remains represented with uncertainty.',ap(1),'low')
x=b('p158-no-opener')
add('havent-opener',x['place'],x['c'],x['reading'],[x['c'],x['reading'],x['c']],'Root adopts B against A/C. The space before the tall initial h is blank at quotation height; the descending trace higher/left belongs to the preceding line. The closing pair after t is present. No opening pair is supplied.',ap(2),'high','text not on the page')
x=a('squarable')
add('squarable',x['place'],x['c'],x['reading'],[x['reading']]*3,'Root confirms the q bowl and long descending return, followed by an independent u, rather than e plus p. The remaining arable is legible. The writer’s question about the spelling remains in the text.',ap(3),'high','misread word')
old=r'\deleted{'+Q+"now or never''}"; new=Q+r"\deleted{now or never''}"
add('now-never-opening-scope','p161 line8, opening quotes beside cancellation',old,new,[old]*3,'Root finds the opening pair above-left of the first zigzag, with a clear gap from every cancellation stroke. The words and the closing group lie within the zigzag, including its final return. All three readers included the opening pair in the deletion; the final leaves that visibly separate pair live while preserving the crossed phrase and closer.',ap(5),'high','deletion state (struck given live or live given struck)')
point=r'\raisebox{0.7ex}{.}\,line'
add('raised-point','164, immediately before line -11','line',point,['line','line',point],'Root confirms the isolated compact dark point above the writing baseline. C reproduces it; A/B omit it, B judging its textual status insecure. The final records the visible raised point without assigning a punctuation function or expanding it into a word.','readers/023/B/crops/13_p164_initial_dot.jpg','medium','drawing or diagram')
x=a('round-superscripts')
add('round-superscripts',x['place'],x['c'],x['reading'],[x['reading']]*3,'All three readers and root find each raised oval independently compatible with0 or lowercase o. Neither later occurrence has a distinguishing stroke. The separate codomain prime, colon, ordinary capitals and right arrow are clear; no mathematical convention is used to choose the ovals.',ap(6),'medium','misread symbol or index',consequential='The domain and codomain acquire their own0/o uncertainty marks; the f superscript was already marked. All three raised signs remain unresolved, without changing the clear prime or rightward arrow.')
x=a('right-note-geometry')
add('margin-geometry',x['place'],x['c'],x['reading'],[x['reading'],b('margin-geometry')['reading'],cc('margin')['reading']],'Root confirms the curved left return, long upper rule and separate rising short stroke. The multiplication note lies below the right part of the first line. A’s geometry is adopted; B/C encode the same arrangement with slightly different approximate dimensions.',ap(7),'high','drawing or diagram')
x=a('left-arrow')
add('left-arrow',x['place'],x['c'],x['reading'],[x['reading'],b('arrow-left-side')['reading'],cc('arrow')['reading']],'Root’s tight crop shows the entire curved arrow left of the reference column. It starts beside184, curves upward around185 and points right into the gap above185. A’s left-margin control is adopted; physical text order stays185 then184.','crops/023/01_left_arrow.jpg','high','insertion or placement')
x=a('lowered-cancelled-clusters')
add('lowered-clusters',x['place'],x['c'],x['reading'],[x['reading'],x['c'],x['c']],'Root confirms that both small crossed groups sit distinctly lower than the body of whatever. A’s lowering is adopted. Their interior letters remain tentative a and s; placement confidence does not resolve the buried letters.',ap(12),'high','insertion or placement')
old=r'\deleted{\unsure{'+Q+'}}';new=r'\deleted{\unsure{'+Q+'|'+q+'}}'
add('cancelled-opener-alternatives','p188 line5, cancelled high mark',old,new,[old,old,new],'The small high cluster has two lobes fused by an oblique crossing. A pair is favoured, but a single broad bent quote also fits the surviving contour. Root adopts C’s explicit alternative; no cancelled character is omitted.',ap(13),'low')
x=a('last-opener-alternatives')
add('last-opener',x['place'],x['c'],x['reading'],[x['reading']]*3,'Root sees the high heavy curved mark with a shallow notch. A fused pair is favoured; one thick quote cannot be excluded. All readers retain the mark live and widen its alternatives.',ap(15),'low')
x=a('cancelled-parenthesis')
add('cancelled-parenthesis',x['place'],x['c'],x['reading'],[x['reading']]*3,'Root follows a continuous right-bowing arc under the angular crossings. The upper and lower slants belong to the cancellation; no separate question-mark dot survives. The closing parenthesis is resolved with medium confidence because the crossings remain heavy. It stays cancelled, and no live replacement closer is supplied.',ap(16),'medium')
for aid,num,part in [('long-left-rule',2,0),('long-right-rule',3,1)]:
 x=a(aid)
 # Each reader’s full geometry is preserved; these two rows concern distinct rules.
 crule=ch['C']['left-rule' if num==2 else 'right-rule']['reading']
 add(aid,x['place'],'',x['reading'],[x['reading'],b('long-rules')['reading'],crule],'Root confirms the long near-vertical stroke on a narrow crop, rotated only for inspection. '+x['evidence']+' The drawing records the visible rule without assigning it an editorial purpose.','crops/023/'+('02_left_rule.jpg' if num==2 else '03_right_rule.jpg'),'high','drawing or diagram')

cd=doubt_decisions(R['A'],23,'A')
cd[8].update(reading=r'\deleted{\unsure{'+Q+'|'+q+'}}',decision='Retained and widened: fused double opener or single broad quote; cancelled state certain.',evidence='Root adopts reader C’s extra single-stroke alternative because the crossing joins the two lobes. Crop: '+ap(13))
cd[10]['confidence']='medium'
cd[19]['evidence']=cd[19]['evidence'].replace('all five quoted words','the complete four-word phrase')
doubts=copy.deepcopy(R['A']['remaining_doubts'])
doubts[6].update(reading=r'\deleted{\unsure{'+Q+'|'+q+'}}',alternatives='double opening pair; single opening stroke',reason='The crossed high cluster has joined lobes; their original stroke count remains uncertain.')
doubts.insert(0,dict(place='p156 after corrected line reference3',reading=r'\unsure{,|.}',alternatives='comma; period',confidence='low',reason='The detached low point has a blunt descending edge; its punctuation form remains uncertain.'))
inventory=copy.deepcopy(R['A']['inventory'])
inventory[9]['first_words_or_objects']='now or never and closing quotation group cancelled; opening pair remains live outside zigzag'
inventory[62]['first_words_or_objects']='tentative cancelled double/single opening quote'
pointrow=dict(sheet_kind='list',hand=inventory[0]['hand'],element='15a',kind='drawing',position='p164, above baseline immediately before line',first_words_or_objects='isolated raised point, function unassigned',transcribed='yes')
inventory.insert(15,pointrow)
# Put long sheet rules first and keep the nested entries in physical top-to-bottom order.
rules=[x for x in inventory if x['element'] in ['71','72']]
inventory=rules+[x for x in inventory if x['element'] not in ['71','72']]
for i,d in enumerate(inventory,1):d['reader_element']='A'+d['element'];d['element']=f'{i:02}'
notes=copy.deepcopy(R['B']['notes'])
notes.append('The absent opener before haven’t is not supplied. The p161 opening pair is outside the cancellation and remains live; the words and closing group remain crossed. The detached low mark after the first corrected reference stays doubtful between comma and stop. An isolated raised point before the p164 correction is reproduced without assigning it a textual function.')
notes.append('The two cancelled clusters adjoining whatever are lowered as on the page. The parenthesis after manyfold is resolved as a cancelled closer, with no live replacement. The three round superscripts are separate ink doubts; the isolated so is mapping lacks its antecedent and assumptions here, so this sheet supplies no substantive mathematical verification event.')
notation=copy.deepcopy(R['B']['notation'])
notation[-1].update(reading='Raised isolated point reproduced without a punctuation interpretation.',evidence='Root adopts the visible point after inspecting B crop13; its position does not establish its function.')
notation.append(dict(sign=r'\deleted{8}3\unsure{,|.}',location='first corrected line reference',reading='Old8 overwritten by3; separate low punctuation remains comma/stop.',evidence='A crop01: closed lower old loop plus upper loop remnant; detached pointed mark below/right.'))
notation.append(dict(sign=Q+r"\deleted{now or never''}",location='p161 line8',reading='Opening pair live, phrase and closing group cancelled.',evidence='A crop05: opening pair stands clear above-left of the zigzag, while the final return encloses the closing strokes.'))
coverage='All three full readings, literal changes, doubt/context decisions and inventories compared. Root inspected18 existing reader crops and3 new geometry crops; each reader/witness and reader/reader disagreement was decided on a crop. Re-displays of existing crops are not counted as new crops. All74 inventory elements are represented, including nested states, the reference column, both long rules, bracket and detached stroke, left arrow and isolated point. H has description only, so no H rows. No OCR, outside research or compilation; the isolated mapping is not counted as a proof check.'
write_record(23,'A','brief_v08.md',text,decisions,cd,doubts,notes,coverage,viewed=viewed,inventory=inventory,notation=notation)
print('Scan023:',len(decisions),'C changes;',len(doubts),'doubt loci;',len(inventory),'inventory rows.')
