from pathlib import Path
import json,re
W=Path(__file__).resolve().parents[1];pg='151_scan005';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());co=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in co['results']};notes={};p=W/'pages'/f'{pg}.tex';s=p.read_text();finals={}
oldhead=r'''\[\deleted{\begin{array}{ccc}
p_0/p_1&p_{12}\quad p_{23}\quad p_{31}&\delta_1\quad\delta_2\quad\delta_3\\
\delta_0&\deleted{\unsure{\sigma p_{12}\quad\sigma p}}&\\
&p_{21}\quad p_{32}\quad p_{13}&
\end{array}}\]'''
newhead=r'''\[\begin{array}{ccc}
p_0/p_1&\deleted{p_{12}\quad p_{23}\quad p_{31}}&\deleted{\delta_1\quad\delta_2\quad\delta_3}\\
\delta_0&\deleted{\deleted{\unsure{\sigma p_{12}\quad\sigma p}}}&\\
&\deleted{p_{21}\quad p_{32}\quad p_{13}}&
\end{array}\]'''
assert oldhead in s;s=s.replace(oldhead,newhead);finals['B01']=b['B01']['first'].replace(oldhead,newhead)
oldE=r'\node at (527,221) {$E_2$};';newE=r'\node at (527,221) {$\overset{\unsure{\prime|\cdot}}{E}_2$};';assert oldE in s;s=s.replace(oldE,newE);finals['B03']=b['B03']['first'].replace(oldE,newE)
# Use the independently written outlines only after root has inspected every line.
old5=b['B05']['first'];new5=b['B05']['second'];assert old5 in s;s=s.replace(old5,new5);finals['B05']=new5
old6=b['B06']['first'];new6=b['B06']['second'].replace(r'\node at (-1.73,1.45) {\deleted{\illegible{1}}};',r'\node at (-1.73,1.45) {$\deleted{\unsure{\mathrm{id}}}$};');assert r'\illegible' not in new6;assert old6 in s;s=s.replace(old6,new6);finals['B06']=new6
old7=b['B07']['first'];new7=b['B07']['second'].replace(r'p_0\unsure{,}p_1',r'p_0\unsure{,|/}p_1')
# Keep the enclosing drawing in a box inside the deletion macro, rather than placing a display environment inside sout.
cut=new7.index('\n\\diagram',new7.index('\\end{tikzpicture}'))
upper=new7[:cut];lower=new7[cut+1:]
upper=upper.replace(r'\deleted{\diagram{',r'\diagram{\deleted{\mbox{',1);upper=upper[:-2]+'}}}'
new7='\\margin{'+upper+'\n'+lower+'}';assert old7 in s;s=s.replace(old7,new7);finals['B07']=new7
start=s.index('\\diagram{\\begin{tikzcd}[ampersand replacement',s.index(new7)+len(new7));end=s.index('\\end{tikzcd}}',start)+len('\\end{tikzcd}}');old8=s[start:end]
new8=b['B08']['second'];q=new8.index('\\node at (-1.95,1.25)');new8=r'\diagram{\begin{tikzpicture}[x=1cm,y=1cm]'+'\n'+new8[q:]
s=s[:start]+new8+s[end:]
# The upper formula fragment is included in the audit box but already belongs to the preceding central frame.
third=r'p_{12}('+r'\underset{\delta_2}{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=0pt](t){$\rho^2\delta_1$};\draw ([yshift=-1pt]t.south west)--([yshift=-3pt]t.south west)--([yshift=-3pt]t.south east)--([yshift=-1pt]t.south east);\end{tikzpicture}}'+r')=\mathrm{id}'
finals['B08']=third+'\n'+new8
old9=b['B09']['first'];new9=b['B09']['second'];new9=new9[new9.index('\\diagram{'):];new9=new9.replace(r'\unsure{G|\mathfrak S}_3',r'\mathcal G_3');new9='\n'.join(z for z in new9.splitlines() if not z.startswith('\\fill '));assert old9 in s;s=s.replace(old9,new9);finals['B09']=new9
old10=b['B10']['first'];new10=b['B10']['second'].replace(r'\sigma_{\unsure{3|1}}',r'\sigma_1').replace(r'\unsure{q|p}_1',r'\unsure{q_1|p_1}');new10='\n'.join(z for z in new10.splitlines() if not z.startswith('\\fill '));assert old10 in s;s=s.replace(old10,new10);finals['B10']=new10
old11=b['B11']['first'];new11='\\margin{'+b['B11']['second']+'}';assert old11 in s;s=s.replace(old11,new11);finals['B11']=new11
p.write_text(s);(W/'records'/p.name).write_text(s)
updates={'C13':new5,'C16':new6,'C20':upper,'C21':r'\begin{gathered}\sigma_1\delta_1=\delta_1\\p_{12}\sigma_3=\underbrace{\sigma p_{12}}_{p_{21}}\end{gathered}','C26':new9,'C31':new10,'C25':r'\unsure{3}'}
for x in r['changes']:
 if x['id'] in updates:x['final']=updates[x['id']]
 if x['id'] in ['C13','C16','C20','C21','C26']:
  x['against_C']=True;x['evidence']+=' Blind audit: the actual frame segments and pen gaps are now drawn rather than a continuous generic box.'
 if x['id']=='C20':x['evidence']+=' A short curved separator under the crossing favors a comma but a slash remains possible; use comma/slash doubt.';x['confidence']='medium'
 if x['id']=='C19':x['final']=third;x['against_C']=True;x['evidence']+=' The lower annotation has a flat middle and upturned ends, so a square-ended bracket replaces the brace.'
 if x['id']=='C25':x['evidence']+=' The tentative3 is placed at the oval outline, not asserted as an exponent attached to p31.'
 if x['id']=='C31':x['evidence']+=' The display frame has separate corner gaps; its underannotation is a flat square-ended bracket. This row records punctuation only; bracket/frame geometry is C41.'
for ident,place,C,H,final,box,why,kind,ec,ah in [
 ('C36','Unstruck left column beside canceled upper inventory',r'\deleted{p_0/p_1;\delta_0}',r'$p_0/p_1$ et $\delta_0$',r'p_0/p_1\quad\delta_0','B01','The long oblique strikes cross the middle lists and delta1–3 group. They do not touch the separate left p0/p1 or delta0. These remain live; an abandoned draft context does not itself make them deleted.','deletion state','7 struck state',False),
 ('C37','Detached mark above E2 in the main diagram',r'E_2',r'E_2',r'\overset{\unsure{\prime|\cdot}}{E}_2','B03','A short dark detached upright lies above the upper bar of E2. It is distinct from the retraced E stem and as dark as the diagram ink; retain it as prime/dot uncertain rather than omit it.','omission','3 omissions',True),
 ('C38','Middle relation, lower annotation geometry',r'\underbrace{\rho\delta_1}_{\delta_3}',r'\underbrace{\rho\delta_1}_{\delta_3}',r'\rho\delta_1\text{ with square-ended lower bracket labelled }\delta_3','B06','The underannotation is flat between two short upturned ends, without a central cusp. The canceled id-like draft above it remains separately doubtful.','drawing or diagram','4 drawings/diagrams',True),
 ('C39','Live p0,p1 oval closure','closed ellipse','circled list described in note',lower,'B07','The live oval has a short overlapping hooked closing stroke at its upper right. Preserve that return; the two p entries and comma are unchanged.','drawing or diagram','4 drawings/diagrams',True),
 ('C40','Generator ovals, including clipped primed-definition oval','three closed ellipse outlines','lists described in note; no drawn outlines',new8,'B08','The prime-definition enclosure is clipped at the right edge and has a gap at the upper left. The delta-list and six-p ovals have their actual relative positions; the latter has a separate3-like closing curl left doubtful. The left relation-frame gap and curved leader are preserved. The sigma p12 underannotation has a genuine central cusp and remains a brace.','drawing or diagram','4 drawings/diagrams',True),
 ('C41','Final relation bracket and interrupted frame',old10,r'\boxed{p_0\,p_{12}\,\sigma_3 = \underbrace{p_0\,p_{12}}_{p_1}}.',new10,'B10','The lower annotation has a straight middle and two short rising ends, with no central cusp. The enclosing four rules leave corner gaps. Its q1/p1 label remains uncertain; the live sigma index is the clear upright1.','drawing or diagram','4 drawings/diagrams',True),
 ('C42','Lower-right q-list oval outline','closed ellipse','circled g-list described in note',new11,'B11','The oval has a flattened right side, a short upper overlap and a small inward tick midway down that side. These are parts of the outline, not extra letters or punctuation. All q indices and commas agree.','drawing or diagram','4 drawings/diagrams',True)]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='medium' if ident in ['C37','C40'] else 'high',kind=kind,error_kind=ec,against_C=True,against_H=ah,consequential=ident=='C36',marked_in_H=False,phase='blind audit'))
# C38 final is supplied as actual TeX, never a prose substitute for its annotation.
x=next(x for x in r['changes'] if x['id']=='C38');x['final']=r'\underset{\delta_3}{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=0pt](t){$\rho\delta_1$};\draw ([yshift=-1pt]t.south west)--([yshift=-3pt]t.south west)--([yshift=-3pt]t.south east)--([yshift=-1pt]t.south east);\end{tikzpicture}}'
r['doubts'].append(dict(place='Detached mark above main-diagram E2',reading=r'\overset{\unsure{\prime|\cdot}}{E}_2',alternatives=['prime','dot'],confidence='low',reason='A distinct dark short upright is present above E; its exact identity is not settled.',crop=f'crops/{pg}_blind_B03.png',box=b['B03']['coordinates']))
r['doubts'].append(dict(place='Canceled p-pair separator',reading=r'p_0\unsure{,|/}p_1',alternatives=['comma','slash'],confidence='low',reason='A short curved stroke survives within the longer crossing return, so comma is preferred but slash is not excluded.',crop=f'crops/{pg}_blind_B07.png',box=b['B07']['coordinates']))
for x in r['doubts']:
 if x['place']=='Six-p oval, upper-right contour':x['reading']=r'\unsure{3}';x['reason']+=' It is positioned on the outline, not asserted as an exponent.'
r['notes']+='''\n### Blind crop adjudication\n\nThe left p0/p1 and delta0 of the upper inventory are physically unstruck and are now live. The middle lists and delta1–3 group are crossed; the small separately canceled sigma-like draft remains uncertain, and both commas after the crossed delta0 composites remain live. A distinct dark upright above main-diagram E2 is retained as prime/dot uncertain. The direct delta0 arrow, curved delta1 arrow, live G2/G3 letters and the shouldered frame agree.\n\nThe central rho-delta and rho-squared-delta annotations, and the final p0p12 underannotation, have square-ended brackets. The sigma p12 annotation in the side relation box has a genuine central cusp and remains a brace. Common-frame scope is unchanged, while separate corner strokes, pen gaps and the doubled upper-left return of the central frame are drawn. The primed-definition oval is kept open at its clipped right edge, the six-p closing curl remains3-like uncertain on its outline, and both smaller list ovals retain their closing returns. The canceled p-pair separator remains comma/slash uncertain. The final sigma index remains1 on its visible upright; no equation is repaired from expected algebra.\n'''
for k in ['deletion_insertion_review','inventory','notation','hand_log']:
 def upd(v):
  if isinstance(v,str):return v.replace(r'\unsure{{}^3}',r'\unsure{3}')
  if isinstance(v,list):return [upd(z) for z in v]
  if isinstance(v,dict):return {a:upd(z) for a,z in v.items()}
  return v
 r[k]=upd(r[k])
evidence={
'B01':'The upper rows and all oblique strokes were viewed. The left p0/p1 and delta0 are not crossed; remove their deletion state. The middle and right blocks are crossed, including the separately struck small sigma-like draft, whose complete reading remains uncertain. Both commas after the crossed delta0 composites are outside the oblique strikes and stay live. Neighboring G/arrow/frame fragments belong to B03.',
'B02':'The numeral has the curved head, diagonal descent and broad lower foot of2, within an enclosing circle whose pen closure is open at the top. Both readings identify the same circled author number; retain the mspage convention.',
'B03':'All three objects, both G letters and four arrows were inspected. The dark detached short upright above the E2 top rule is independent of the retraced E stem; preserve it as prime/dot uncertain. The direct delta0 arrow, bowed delta1 arrow and shouldered frame agree. The id,sigma fragment to the upper left belongs to the preceding line, already transcribed.',
'B04':'The full delta1 p12 has one crossing horizontal stroke; all letter/index bodies agree. Display versus inline deletion syntax does not change the reading.',
'B05':'Both E0 identities share one frame. All four frame strokes stop separately before the adjacent corners; preserve these pen gaps instead of a continuous box. Letters and indices agree.',
'B06':'The first caption is literally(involution without a closing parenthesis; the second(idempotent) is closed. Both lower annotations have straight middles and upturned ends. The canceled upper id-like draft remains tentative, not replaced by an illegible symbol inside mathematics. The frame has a doubled upper-left return and a gap to its top rule; all three equations agree.',
'B07':'The upper p-pair is canceled within its box. A short curved separator favors comma but remains comma/slash uncertain under the looping strike. The lower live p0,p1 oval has a hooked overlapping closure at its upper right, now preserved.',
'B08':'The whole local cluster was read. The left first sigma index is1, and sigma p12 has a real central-cusped underbrace labelled p21. The delta oval has a curved leftward leader. All six p labels agree, with a3-like outline curl remaining uncertain. All primed delta definitions agree; their enclosing oval is clipped at the right and interrupted at its upper-left join. The partly shown central third equation belongs to B06 and is not duplicated in the page.',
'B09':'Both invariant statements share a wide interrupted frame. The final group glyph has the same open G bowl and inward return as the diagram, not a certified S. The small isolated lower-left dot is not sentence punctuation. The p21 and p-list fragments above belong to the preceding cluster.',
'B10':'The full final formula has a short upright sigma index1 without two separate3 lobes. The overtraced lower label remains q1/p1. Its annotation is a flat square-ended bracket, and the frame has separate corner gaps. Two small displaced dots below the label are not added as punctuation.',
'B11':'The three letters have left bowls and long right descenders, agreeing with q1,q2,q3. The flattened oval right side, top overlap and small inward tick are outline strokes rather than another letter. Preserve that contour.'}
for k,why in evidence.items():
 notes[k]=dict(viewed=True,evidence=why)
 if k in finals:notes[k].update(changed=True,final=finals[k])
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('005: all11 differing boxes viewed; nine changed; live/canceled scope and diagram details corrected.')
