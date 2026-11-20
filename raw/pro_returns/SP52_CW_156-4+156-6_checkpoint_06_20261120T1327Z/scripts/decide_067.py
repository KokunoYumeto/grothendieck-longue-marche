from pathlib import Path
import copy, json

O=Path(__file__).resolve().parents[1]
K='156-4_067'
R=[json.loads((O/'readers'/K/f'R{i}'/'report.json').read_text()) for i in (1,2,3)]
T=[(O/'readers'/K/f'R{i}'/'reading.tex').read_text() for i in (1,2,3)]
P=f'readers/{K}/R1/crops/'
Q=f'readers/{K}/R2/crops/'
S=f'readers/{K}/R3/crops/'
A=f'crops/{K}/'

def figure_at(text, n):
    starts=[]; pos=0
    while True:
        pos=text.find(r'\figure{',pos)
        if pos<0:break
        starts.append(pos);pos+=8
    start=starts[n];brace=text.index('{',start);depth=1;i=brace+1
    while depth:
        ch=text[i]
        # Escaped literal braces in the formula do not alter the TeX group.
        escapes=0;j=i-1
        while j>=0 and text[j]=='\\':escapes+=1;j-=1
        if escapes%2==0:
            if ch=='{':depth+=1
            elif ch=='}':depth-=1
        i+=1
    return start,i,text[start:i]

top=figure_at(T[2],0)[2].replace(r'disjoint \unsure{de|des}',r'disjoint de')
middle=figure_at(T[1],1)[2]
middle=middle.replace(r'\unsure{déterminent|determinent}',r'\unsure{determinent|déterminent}')
middle=middle.replace(r'\draw[->] (3.12,.16) -- (3.75,.26);',r'\node[anchor=east] at (3.75,.26) {$\unsure{\longrightarrow}$};')
lower=figure_at(T[1],2)[2].replace(r'\unsure{saturée|saturee}',r'\unsure{saturee|saturée}')
t=T[0]
for n,replacement in [(1,middle),(0,top)]:
    start,end,_=figure_at(t,n);t=t[:start]+replacement+t[end:]
t=t.replace(r'\unsure{\mathrm{tt}|\forall}',r'\unsure{\forall|\mathrm{tt}}')
t=t.replace(r'($\text{p. r. à }\mathcal F$). Partie',r'($\text{p. r. à }\mathcal F$)\unsure{-|.} Partie')
start=t.index(r'Partie \unsure{saturée|saturee}')
end=t.index('\n\\[',start)
t=t[:start]+'\n\n% Raised M_0 and its distinct oblique insertion leader.\n'+lower+t[end:]
filename='J156-4-09_156-4_scan067.tex'
(O/'pages'/filename).write_text(t)

d={k:copy.deepcopy(R[0][k]) for k in ['differences','c_doubts','inventory','remaining_doubts','abbreviations']}
d.update(key=K,cote='156-4',scan=67,folder='J156-4-09',their_page=66,filename=filename,brief_version='v03',check_events=[])
rows={i+1:x for i,x in enumerate(d['differences'])}
rows[8]['crop']=A+'a03_live_premise.jpg'
for n in (21,22,71,72):rows[n]['crop']=Q+'18_bottom_words_formula.jpg'
rows[73]['crop']=Q+'18_bottom_words_formula.jpg; '+A+'a02_final_stop.jpg'
rows[29].update(reading=r'\unsure{\varphi|\Phi}',change_c=True,crop=S+'02_top_right.jpg',scan_shows='The small loop sits on a descending stem with a curved rising exit, unlike the larger Phi above with its straight lower foot. Cursive varphi is preferred, while a reduced capital Phi remains possible.')
rows[30].update(reading=r'\unsure{\rbrace|)\rbrace}',change_h=True,crop=S+'02_top_right.jpg',confidence='medium',scan_shows='The large rounded upper lobe meets the small lower brace-like hook. One worked brace is preferred, but an overlapping parenthesis plus brace cannot be excluded. One group is represented with alternatives, not two certain independent marks.')
rows[26].update(reading=top,scan_shows='The inclusion is raised above the first set. A curved open enclosure runs beneath it and descends at the right; a separate short branch drops toward Phi. Both distinct strokes and all three formula labels are rendered once in the top TikZ group.')
rows[31].update(reading=top,scan_shows='The added third equality is below a long stroke coming from the second row at the right, turning left and downward before its equals sign. Its operator has one p. The final TikZ group preserves the continuation and the curved connector.')
rows[42].update(reading=r'\unsure{\longrightarrow}',crop=S+'05_left_note.jpg',confidence='medium',scan_shows='A short right-pointing or ticked terminal follows the slanted second line toward the brace. Its separation from the last letter stroke is not secure. The uncertain arrow is placed with the note in the common TikZ group, with no duplicated note text.')
rows[42]['c']='' # This row is scoped only to the separately drawn pointer.
rows[47].update(reading=middle,crop=S+'07_right_note.jpg',scan_shows='The phrase is underlined. Above it the separate family-prime has a bent underline with a rising right arm. Two additional curved strokes descend and continue under the phrase, one extending from farther left; the lower strokes diverge downward at the right. These strokes are reproduced with the marginal text once.')
rows[48]['crop']=A+'a01_upper_def.jpg; '+P+'09_middle_definitions.jpg'
rows[48]['scan_shows']='Both small labels have d-e-f strokes with no distinct accent over e. The complete head of the upper label is visible in the root crop; the long horizontal above it belongs to the adjacent note enclosure, not to an acute accent.'
rows[51]['c']=r'\unsure{Sup|Supp},'
rows[57]['scan_shows']='Two isolated dark points immediately follow the corrected M subscript, well below the operator and argument baseline. They slope slightly downward to the right. Their location is retained at subscript height, with two points versus a colon uncertain; no mathematical role is supplied.'
rows[59].update(reading=r'\unsure{\forall|\mathrm{tt}}',change_c=True,scan_shows='Two tall stems meet in an angular inverted-A-like form and share a cross stroke. That shape favours a universal sign, but compressed tt remains possible. The first alternative follows the visible angular connection, not the expected quantifier meaning.')
rows[67].update(reading=r'\unsure{saturee|saturée}',scan_shows='The word has a leading s, ascending t and flattened connecting strokes. No detached acute is securely visible, so the unaccented form is listed first; an accented reading remains possible.')

def add(place,c,h,reading,evidence,crop,kind='other',confidence='medium',mc=False):
    x=dict(id=f'A-067-D{len(d["differences"])+1:03d}',location=place,c=c,h=h,reading=reading,scan_shows=evidence,confidence=confidence,kind=kind,marked_in_h='no',change_c=True,change_h=True,crop=crop,math_consequential=mc)
    d['differences'].append(x);return x
accent=add('Slanted left note, accent in determinent','déterminent','déterminent',r'\unsure{determinent|déterminent}','The ascending initial d stroke is connected to the word. No securely separate acute can be isolated above the following small e-region in the upright crop; the accent state remains doubtful.',S+'05_left_note.jpg')
punct=add('Between first saturated definition and following Partie','.','.',r'\unsure{-|.}','The separate terminal mark is a short oblique horizontal stroke, not a round point. A short dash is preferred, with a drawn-out period retained as an alternative.',Q+'16_saturee_heading.jpg')
leader=add('Second saturated definition, M_0 insertion leader',r'\inserted{M_0}',r'\mathcal M_0',lower,'The live M_0 is raised above the gap before de. A separate long oblique arm descends leftward from its right edge toward the insertion gap. The leader and its text are reproduced once in TikZ.',P+'17_saturee_sentence.jpg',kind='drawing or diagram',confidence='high')

for x in d['c_doubts']:
    loc=x['location']
    if loc in ['C.tex doubt 05, second final phi','C_context row 22']:
        x.update(reading=rows[29]['reading'],status='revised',scan_shows=rows[29]['scan_shows'],crop=rows[29]['crop'])
    if loc in ['C.tex doubt 06, second closing strokes','C_context row 06','C_context row 29']:
        x.update(reading=rows[30]['reading'],status='revised',scan_shows=rows[30]['scan_shows'],crop=rows[30]['crop'])
    if loc in ['C.tex doubt 20, tt/forall','C_context row 05','C_context row 15']:
        x.update(reading=rows[59]['reading'],status='revised',scan_shows=rows[59]['scan_shows'])
    if loc in ['C.tex doubt 24, second saturée','C_context row 19']:
        x.update(reading=rows[67]['reading'],status='revised',scan_shows=rows[67]['scan_shows'])
    if loc=='C_context row 02':x['crop']=rows[48]['crop']+'; '+P+'01_top_first.jpg'
    if loc=='C_context row 27':
        x.update(reading=r'\operatorname{cosup} at the single-descender occurrences; \operatorname{cosupp} in the repeated cancelled family-prime equation and live family-double-prime definition; \operatorname{supp} in both right-hand middle definitions',scan_shows='One-p and two-p forms differ locally: the cancelled repeated family equation and live family double-prime equation have two separate p descenders. The top three operators, lower cancelled operators, live M double-prime operator and lower cosupport display have one.',crop=P+'01_top_first.jpg; '+P+'02_top_second.jpg; '+P+'05_deleted_formulas.jpg; '+P+'09_middle_definitions.jpg; '+P+'13_lower_operators.jpg')

for x in d['remaining_doubts']:
    if x['location']=='Top second phi':x.update(reading=r'\varphi',alternatives=[r'\Phi'],reason=rows[29]['scan_shows'])
    if x['location']=='After disjoint de before Y':x.update(reading=r'\forall',alternatives=[r'\mathrm{tt}'],reason=rows[59]['scan_shows'])
    if x['location']=='Second saturée':x.update(reading='saturee',alternatives=['saturée'],reason=rows[67]['scan_shows'])
    if x['location']=='Two low marks following lower M subscript':x['reason']=rows[57]['scan_shows']
for place,reading,alts,reason in [
    ('Top second set closing strokes',r'\rbrace',[r')\rbrace'],rows[30]['scan_shows']),
    ('Left note, determinent accent','determinent',['déterminent'],accent['scan_shows']),
    ('Left note, possible pointer',r'\longrightarrow',[],rows[42]['scan_shows']),
    ('After first saturated definition','-',['.'],punct['scan_shows'])]:
    d['remaining_doubts'].append(dict(location=place,reading=reading,alternatives=alts,confidence='medium',reason=reason))

dis=[]
def dispute(place,a,b,c,final,evidence,crop):
    dis.append(dict(location=place,r1=a,r2=b,r3=c,final=final,evidence=evidence+' ['+crop+']'))
dispute('Top enclosure and third-row connector','Simplified curved enclosure and connector','Two upper branches and long lower connector','Anchored curved enclosure, branch and lower connector',top,rows[26]['scan_shows']+' '+rows[31]['scan_shows'],P+'01_top_first.jpg; '+P+'02_top_second.jpg; '+S+'02_top_right.jpg')
dispute('Second disjoint article','de',r'\unsure{de|des}',r'\unsure{de|des}','de',rows[28]['scan_shows'],rows[28]['crop'])
dispute('Second top small phi',r'\unsure{\Phi|\varphi}',r'\unsure{\varphi|\Phi}',r'\unsure{\varphi|\Phi}',rows[29]['reading'],rows[29]['scan_shows'],rows[29]['crop'])
dispute('Second top closing strokes',r'\}',r'\unsure{)\}|\}}',r'\unsure{\rbrace|)\rbrace}',rows[30]['reading'],rows[30]['scan_shows'],rows[30]['crop'])
dispute('Left note accent','déterminent',r'\unsure{déterminent|determinent}',r'\unsure{déterminent|determinent}',accent['reading'],accent['scan_shows'],accent['crop'])
dispute('Left note pointer','definite drawn arrow','definite drawn arrow',r'\unsure{\longrightarrow}',rows[42]['reading'],rows[42]['scan_shows'],rows[42]['crop'])
dispute('Right note enclosure','Bent arm and two additional curves','Bent arm and two additional curves','Bent arm and one additional enclosing curve',middle,rows[47]['scan_shows'],rows[47]['crop'])
dispute('Stable par spelling',r'\unsure{Sup|Supp}',r'\unsure{Supp|Sup}',r'\unsure{Sup|Supp}',r'\unsure{Sup|Supp}',rows[51]['scan_shows'],rows[51]['crop'])
dispute('After passage',r'\unsure{:|à}',':',r'\unsure{à|:}',r'\unsure{:|à}',rows[53]['scan_shows'],rows[53]['crop'])
dispute('Low marks after corrected M subscript',r'_{M\unsure{..|:}}',r'_{M}\unsure{:}',r'_{M}\unsure{\ldotp\ldotp|:}',rows[57]['reading'],rows[57]['scan_shows'],rows[57]['crop'])
dispute('Before Y',r'\unsure{\mathrm{tt}|\forall}',r'\unsure{\mathrm{tt}|\forall}',r'\unsure{\forall|\mathrm{tt}}',rows[59]['reading'],rows[59]['scan_shows'],rows[59]['crop'])
dispute('Conclusion verb',r'\unsure{ramené|revenu}',r'\unsure{ramené|revenu}','ramené',rows[60]['reading'],rows[60]['scan_shows'],rows[60]['crop'])
dispute('Old heading M',r'\deleted{\unsure{M}}',r'\deleted{M}',r'\deleted{\unsure{M}}',r'\deleted{\unsure{M}}',rows[63]['scan_shows'],rows[63]['crop'])
dispute('First saturated definition terminal punctuation','.',r'\unsure{-|.}','.',punct['reading'],punct['scan_shows'],punct['crop'])
dispute('Second saturée accent',r'\unsure{saturée|saturee}',r'\unsure{saturée|saturee}',r'\unsure{saturee|saturée}',rows[67]['reading'],rows[67]['scan_shows'],rows[67]['crop'])
dispute('M_0 leader','Insertion macro only','Insertion plus separate drawn leader','Insertion macro only',lower,leader['scan_shows'],leader['crop'])
dispute('Final mutuellement',r'\unsure{mutuellement}',r'\unsure{mutuellement}','mutuellement',rows[69]['reading'],rows[69]['scan_shows'],rows[69]['crop'])
d['disputes']=dis

for x in d['inventory']:
    if x['element']=='I16':x['first_words_or_objects']=r'Ainsi, M′ et ℱ′ se \unsure{determinent|déterminent} \unsure{mutuellement}'
    if x['element']=='I17':x['first_words_or_objects']=r'\unsure{\longrightarrow}: pointer or final-letter continuation'
    if x['element']=='I20':x['first_words_or_objects']='Bent underline under ℱ′; two curved enclosing strokes below the underlined Stable par Sup.'
    if x['element']=='I32':x['first_words_or_objects']=r'Partie saturée … cosupport (p. r. à ℱ)\unsure{-|.}'
    if x['element']=='I35':x['first_words_or_objects']=r'Partie \unsure{saturee|saturée} de M : égale au cosupport de son support (dans M).'
def item(kind,position,words):return dict(element='',kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes')
# Insert additional separately visible elements in their spatial order.
idx=next(i for i,x in enumerate(d['inventory']) if x['element']=='I30')
d['inventory'].insert(idx,item('text','after corrected lower M subscript',r'\unsure{..|:} at subscript height'))
idx=next(i for i,x in enumerate(d['inventory']) if x['element']=='I37')
d['inventory'].insert(idx,item('drawing','descending left from raised M_0','Distinct oblique insertion leader'))
for i,x in enumerate(d['inventory'],1):x['element']=f'I{i:02d}'

d['notes']={
 'summary':'Manuscript page 66 defines cosupports of a family in the figure family and in M, then gives a braced relationship between them, with marginal notes on mutual determination and closed parts. It defines a second cosupport, naming it support, and asserts inclusion of the original family and stability under Sup and passage to a subfigure. A union of barred H_i is introduced, followed by equalities intended to reduce the construction to M. The bottom defines saturated parts: the first definition says cosupport of its cosupport; the second literally says cosupport of its support. It ends with two corresponding set equations, the last using barred F. These are the manuscript’s assertions, not mathematical results validated in this run.',
 'math_reading_decisions':[
  'Membership was expected after the first H_i, but its upright and single rightward bar support the literal vdash sign. The second top relation is a curved membership sign; the occurrences are not normalized.',
  'The repeated definitions prompted inspection of the single/double p spellings. Top operators and the M double-prime definition have cosup; the cancelled repeated family definition and live family double-prime definition have cosupp. The spellings remain local.',
  'The expected parallel form in the two saturated definitions prompted inspection of the second noun. Its ink begins directly with s, with no co prefix: son support is retained. The notes do not repair or prove that statement.',
  'The final set-builder has a distinct bar over F; H omits that bar. The bar is consequential and is retained.',
  'The lower two-stem sign before Y is angular and can be forall or compressed tt; the graphic form favours forall, while the doubt remains. The two detached points beside the altered M subscript are kept at their low written level without assigning a meaning.'
 ],
 'author_checks':[
  'Visible revisions include the cancelled Donc draft with its repeated equation, the cancelled contient Phi, altered operator subscripts, overwritten M-like forms, and raised inclusion, continuation, F_0 and M_0 additions.',
  'No explicit à vérifier or sauf erreur is legible on this page. The terminal narrow two-loop mark after dans M. is a section sign, not a question mark.',
  'The first braced equation and the two final equations are transcribed as stated; no proof of their equivalence or the saturation assertions was attempted.'
 ],
 'title_dates_pagination':'Manuscript page 66 at the top centre; archive scan 67. Partie saturée introduces the lower definitions. No date or separate page-count statement is present.'
}
d.update(reader_crop_counts={'R1':18,'R2':18,'R3':16},adjudicator_crop_count=3,
 workflow_note='Three fresh isolated v03 readers completed whole/halves once each and their own crops. Root inspected 25 existing reader crops (all 18 R1; R2 07,16,18; R3 02,05,07,08) and three new tightly targeted crops, never a whole or half page. Three root crops were needed because existing reader framing cut off the upper def head, the live premise family head, or the space beyond the final brace. A first attempt to show R3 crop02 and root a01 was truncated; neither was counted until successfully displayed later from the same files. R3 disclosed two crops without a complete adjacent line; that was recorded rather than recropped. A text-only administrative audit cross-checked the union of reports and C-context dispositions. No OCR, outside research, compilation or mathematical proof check occurred. The next brief clarifies framing target extremities and retaining distinct insertion leaders and doubtful accents.')

def clean(x):
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items() if k not in ['bbox_image','source']}
    if isinstance(x,list):return [clean(v) for v in x]
    if isinstance(x,str):return x.replace(str(O)+'/', '')
    return x
d=clean(d)
(O/'decisions'/f'{K}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':K,'differences':len(d['differences']),'C_doubts':len(d['c_doubts']),'disputes':len(dis),'remaining':len(d['remaining_doubts']),'inventory':len(d['inventory'])}))
