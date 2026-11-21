from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];page='148_scan005'
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text());p=root/'pages'/f'{page}.tex';t=p.read_text()
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());ds={d['box']:d for d in comp['differences']}
subs=[('combinatoires orientés',r'\unsure{combinatoires} orientés'),(r'\text{algébriques de }',r'\text{algébriques \unsure{dans|de} }'),(r'i.e. groupe des unités de $\mathbb Z[i]$',r'i.e. groupe des unités \unsure{dans|de} $\mathbb Z[i]$'),('(anneau des entiers',r'(\unsure{anneau} des entiers'),(r'\deleted{axes de}',r'\deleted{\unsure{axes} de}'),(r'\unsure{lattice}',r'\unsure{lattice|entier}')]
for a,b in subs:
 assert a in t,a
 t=t.replace(a,b)
# Preserve the exposed gaps in the canceled three-sided frame.
a=r'\draw (-1,-.7)--(-1,.65)--(.6,.65)--(.6,-.7);'
b=r'\draw (-1,-.7)--(-1,.58);'+'\n'+r'\draw (-.94,.65)--(.55,.65);'+'\n'+r'\draw (.62,.58)--(.6,-.7);'
assert a in t;t=t.replace(a,b)
# Actual short projecting returns, without assigning them arrow direction.
upper_extra=r'''
\draw[thick] (-.55,-.36)--(-.50,-.40)--(-.47,-.48);
\draw[thick] (.88,.02)--(.98,-.01)--(.91,.08);
\draw[thick] (-.22,-.76)--(-.11,-.88)--(-.23,-.82);'''
t=t.replace('% UPPER-DRAWING-END', '% UPPER-DRAWING-END')
end=t.index('\\end{tikzpicture}',t.index('% UPPER-DRAWING-BEGIN'));t=t[:end]+upper_extra+'\n'+t[end:]
live_extra=r'\draw[thin] (-1.43,-.05)--(-1.29,-.09);'
t=t.replace('% LIVE-DRAWING-END',live_extra+'\n% LIVE-DRAWING-END')
lower_extra=r'''
\draw[thick] (-.60,0)--(-.46,0);
\draw[thick] (.40,.01)..controls(.45,-.07)and(.52,-.07)..(.59,.01);
\draw[thin] (-.17,-.93)--(-.08,-.98)--(-.16,-1.00);'''
end=t.index('\\end{tikzpicture}',t.index('% LOWER-DRAWING-BEGIN'));t=t[:end]+lower_extra+'\n'+t[end:]
p.write_text(t)
for section in ('changes','decisions','doubts'):
 for row in r[section]:
  for key in ('final','reading'):
   if key in row:
    for x,y in subs:row[key]=row[key].replace(x,y)
for c in r['changes']:
 if c['id'].endswith('-02'):
  c['place']='right marginal note, opening parenthesis and unclosed ending';c['evidence']+=' Blind comparison withdraws certainty in the retraced initial letters of anneau; the same candidate remains in place. The preposition before Z[i] is handled at its separate word locus.'
 if c['id'].endswith('-05'):
  c['final']=c['final'].replace(r'\end{tikzpicture}',upper_extra+'\n'+r'\end{tikzpicture}');c['evidence']+=' Three short angular projections along the lower-left inner corner and outer right/lower-left contour are now drawn as exposed returns. Eight clear filled locations and the separate lower dot remain; the round center label stays 0/o.'
 if c['id'].endswith('-09'):
  c['final']=c['final'].replace(a,b).replace('% LIVE-DRAWING-END',live_extra+'\n% LIVE-DRAWING-END');c['evidence']+=' The blind crops expose short gaps at the upper corners of the canceled three-sided frame, now preserved. The live drawing retains its lower-right gap and gains the small return at the far-left end of the transverse line. The projections are drawn without imposing an arrow direction.'
 if c['id'].endswith('-12'):c['evidence']+=' Entier is added as the independent candidate beneath the same cancellation; the tall initial loop and two middle ascenders keep lattice preferred, with the covered letters unresolved.'
 if c['id'].endswith('-14'):
  c['final']=c['final'].replace(r'\end{tikzpicture}',lower_extra+'\n'+r'\end{tikzpicture}');c['evidence']+=' The two dark patches on the central horizontal are now placed explicitly as a short thick stroke and a small curved thickening. Together with the seven separately marked locations they account for the second reader’s nine dark marks; they are not assigned additional mathematical roles. A short return at the lower-left side’s endpoint is also reproduced.'
for d in r['decisions']:
 if d['id']=='M0067':
  d.update(decision='undecided',reading=r'\unsure{anneau}',confidence='low',evidence='The initial group is densely retraced. The following low nneau run supports anneau, but the letter centres and any earlier state cannot be recovered securely. The independent crop leads to retaining the candidate with doubt rather than treating every letter as settled.',crop=page+'_second_B05.png [1104,580,1621,700]')
for d in r['doubts']:
 if d['place']=='line 14, canceled word':d['alternatives']='lattice; entier';d['reason']+=' The blind reader supplies entier; neither crossed word is securely recovered throughout.'
r['doubts'] += [dict(place='line 4, start of combinatoires',reading=r'\unsure{combinatoires}',alternatives='combinatoires; overwritten initial letter group unresolved',confidence='medium',reason='The initial group is dense and retraced, while the later binatoires run is exposed.'),dict(place='line 6, preposition before Q[i]',reading=r'\unsure{dans|de}',alternatives='dans; de',confidence='medium',reason='The d-loop is followed by a long low run and terminal down-hook; dans is preferred, with the short alternative retained.'),dict(place='right marginal note, before Z[i]',reading=r'\unsure{dans|de}',alternatives='dans; de',confidence='medium',reason='The d and following low run are separated, with a final downward s-like hook; the pattern matches the same local dans form before V_S.'),dict(place='right marginal note, first word inside parenthesis',reading=r'\unsure{anneau}',alternatives='anneau; overwritten initial group unresolved',confidence='low',reason='The opening letters are crowded and retraced; the preferred word is unchanged but its prior resolution is withdrawn.'),dict(place='line 13, canceled axes',reading=r'\deleted{\unsure{axes} de}',alternatives='axes; covered internal letters unresolved',confidence='medium',reason='The horizontal cancellation crosses the middle of the word; the exposed a-like beginning and final low ending remain compatible with axes.')]
newrows=[('18','main comparison formula, preposition before Q[i]',r'algébriques de $\mathbb Q[i]$',r'algébriques de $\mathbf Q[i]$',r'algébriques \unsure{dans|de} $\mathbb Q[i]$', 'B04',[603,430,1621,618], 'The d has its clear upper loop and is followed by an extended low run ending in a down-hook. The independent dans reading accounts for that run; de remains an alternative because the middle letters are compressed.'),('19','right marginal note, preposition before Z[i]',r'unités de $\mathbb Z[i]$',r'unités de $\mathbf Z[i]$',r'unités \unsure{dans|de} $\mathbb Z[i]$','B05',[1104,580,1621,700], 'After the d-loop the remaining strokes extend through a low run with a terminal down-hook, comparable to the local dans before V_S. Dans is preferred to the two drafts’ de, with the latter retained as an explicit alternative.')]
for num,place,C,H,final,box,coords,evidence in newrows:r['changes'].append(dict(id=page+'-'+num,place=place,C=C,H=H,final=final,crop=page+'_second_'+box+'.png',box=coords,evidence=evidence,confidence='medium',kind='misread word',error_sheet_kind='Words',differs_C=True,differs_H=True,marked_in_H=False,consequential=False))
r['notes']+=' Blind audit prefers dans at the two unit-group prepositions, with de retained as an alternative. It withdraws certainty in the overwritten starts of combinatoires and anneau, and retains lattice/entier beneath the cancellation. The drawing audit adds exposed endpoint returns, gaps in the canceled frame and the two dark patches on the central horizontal of the lower drawing. Insertion leaders remain encoded by the insertion macros and their documented attachment. The prose beside the inline drawings, outside the neutral boxes, contains no required second-reading target: its unchanged wording was checked in the complete first reading. No mathematical claim was checked in this audit.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
ev={
'B01':('The underline lies along the main Courbes/de type baseline, while exceptionnelles is raised with a curved insertion leader. The numeral 1 is separate above/right. The first reading preserves that placement and underline scope.','high'),
'B02':('The baseline Courbe and anharmonique de type carré are underlined; ell. is raised, with its own terminal dot and a curved leader. The insertion itself is outside the baseline underline.','high'),
'B03':('The initial combinatoires group is retraced and now marked uncertain, while the following binatoires sequence is visible. The final word has connected low sous strokes and a short final return; sous remains preferred to sur. The other words agree.','medium'),
'B04':('The two simeq signs, Z/4Z, mu_4(C) and two-line unit-group term agree. The final preposition has a long low run after d and a down-hook; dans is now preferred, with de retained.','medium'),
'B05':('The marginal abbreviation has its internal and terminal points. The preposition before Z[i] has the longer low run of dans, now preferred with de as alternative. The parenthesis is exposed; anneau’s retraced beginning now retains doubt.','low'),
'B06':('The final marginal baseline reads des entiers de Q[i] with the square bracket. No closing parenthesis is exposed. The margin wrapper and math delimiters change only serialization.','high'),
'B07':('The added S has parentheses and a descending attachment contour after torseur. The complete definition formula has E-l, lower zero, def over simeq, C/Z[i], and et trouver. The two readings agree in ink.','high'),
'B08':('Both E-l expressions have lower zero; the first has argument S. The wedge’s Z/4Z label is below it, and the final S is on the baseline. Only display serialization differs.','high'),
'B09':('The drawing has eight clear filled locations and a detached lower dot, a broken outer frame, dashed diamond, two transverse strokes and an inner square with retraced upper edge. Three short angular projections are now drawn directly. The center’s 0/o alternatives remain.','medium'),
'B10':('The raised euclidien and V_S each have their own descending attachment. The baseline reads comme carré without an extra un, then plan euclidien (canoniquement), de centre. Line breaks and math wrappers account for the difference.','high'),
'B11':('The isolated loop with upper return remains compatible with 0 or o; its comma is distinct. The blind numeral reading does not remove the existing graphic ambiguity.','low'),
'B12':('The canceled drawing has three exposed frame sides with small gaps at both upper corners and overlapping slanted/looped crossing paths. The frame gaps are now retained; the cancellation strokes remain directly drawn.','high'),
'B13':('The live drawing has four sides with a lower-right gap, two projecting transverse strokes and short spurs near the top and left. The small far-left terminal return is added. No arrow direction is assigned to these incomplete projecting forms.','medium'),
'B14':('The full parenthesis and V_S agree. The loop after via keeps 0/o alternatives. The first crossed word retains axes but its covered middle is now explicitly doubtful; de remains in the crossed span.','medium'),
'B16':('The initial loop and two middle ascenders favor lattice, but the strike covers several bodies. Entier is added as the independent candidate. The raised réseau and its replacement state are clear.','low'),
'B17':('Gamma has lower S, followed by dans V_S and the opening sous-groupe discret de. All words and indices agree; math wrappers differ.','high'),
'B18':('Rang is followed by the curved-top digit 2, a closing parenthesis and et. Extra math parentheses in serialization do not change the reading.','high'),
'B19':('The entire overworked E-l expression, neighboring X_S and V_S and quotient were rechecked. The oblique/2-like mark keeps its existing alternatives, and the final lower Gamma index retains the visible hook-shaped r with S alternative. The enclosure is open below, with outward feet, and the terminal point lies inside.','low'),
'B20':('The dashed grid trajectories, four diamond sides, central vertical, seven separately marked locations, two detached upper dashes and two dark patches on the central horizontal are visible. The horizontal patches and lower endpoint return are now placed explicitly. The thick upper central segment occupies about half the radius.','medium'),
'B21':('The complete target baseline reads dans X_S un élément d’ordre 2 canonique; no lexical or index difference survives the math-wrapper comparison.','high'),
'B22':('The raised glyph has eta’s upright, arch and long lower return, with low S. Its three-armed attachment contour joins the gap after canonique. The existing insertion macro retains that content and placement; the graphic wrapper changes presentation only.','high'),
'B23':('Stable par automorphismes, the two other abbreviated él., both order-2 wording and the generator i are visible. Both readings give the same words and digits, with a physical line break after d’.','high'),
'B24':('The full mu_4(C) comparison is retained, with X_S’s low S still merged near the parenthesis. The opening parenthesis, underlined NB, eta_S and peut donc être défini agree; no closing parenthesis is supplied.','low')}
choices=[]
for d in comp['differences']:
 box=d['box'];final=d['first']
 for x,y in subs:final=final.replace(x,y)
 if box=='B04':final=final.replace(r'\text{groupe des unités algébriques de }',r'\text{groupe des unités algébriques \unsure{dans|de} }')
 if box=='B05':final=final.replace('(anneau',r'(\unsure{anneau}')
 if box=='B09':final=final.replace(r'\end{tikzpicture}',upper_extra+'\n'+r'\end{tikzpicture}')
 if box=='B12':final=final.replace(a,b)
 if box=='B13':final=final.replace(r'\end{tikzpicture}',live_extra+'\n'+r'\end{tikzpicture}')
 if box=='B20':final=final.replace(r'\end{tikzpicture}',lower_extra+'\n'+r'\end{tikzpicture}')
 it=dict(box=box,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[box][0],confidence=ev[box][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_b',choices=choices),ensure_ascii=False,indent=2)+'\n')
