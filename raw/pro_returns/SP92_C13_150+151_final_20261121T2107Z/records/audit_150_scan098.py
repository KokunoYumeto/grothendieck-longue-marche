from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan098';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
def bracket(term,under):
 return r'\underset{'+under+r'}{\begin{tikzpicture}[baseline=(term.base)]\node[inner sep=0pt] (term) {$'+term+r'$};\draw ([yshift=-1pt]term.south west) -- ([yshift=-3pt]term.south west) -- ([yshift=-3pt]term.south east) -- ([yshift=-1pt]term.south east);\end{tikzpicture}}'
old106=r'\underbrace{V_J\cap X_L^*}_{\substack{\Vert\\V_J^{X_L^*}\text{ avec}\\\text{notation }(102)}}'
new106=bracket(r'V_J\cap X_L^*',r'\substack{\Vert\\V_J^{X_L^*}\text{ \unsure{avec|en}}\\\text{notation }(102)}')
old107=r'\underbrace{V_j\cap V_l}_{V_{j,l}}';new107=bracket(r'V_j\cap V_l',r'V_{j,l}')
reps=[(r'\unsure{et}',r'\unsure{et|Et}'),(old106,new106),(old107,new107),(' au lieu de ',r' \unsure{au|$\mathord{-}$} \unsure{lieu|lien} de ')]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==1,(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
for x in r['changes']:
 for a,z in reps:x['final']=x['final'].replace(a,z)
 if x['id']=='C06':x.update(final=r'\unsure{avec|en}',confidence='medium',evidence='The short low group after the lower V has three compressed strokes. They permit avec or en; individual letter boundaries are not secure enough to certify avec.')
for ident,place,C,H,final,box in [('C39','Lower annotation bracket in106',old106,'Underbrace below V_J intersection X_L*',new106,'B03'),('C40','Lower annotation bracket in107',old107,'Underbrace below V_j intersection V_l',new107,'B05')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence='The lower stroke runs horizontally between two short rising ends. It has no central cusp, so preserve a square-ended lower bracket rather than a brace.',crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind='drawing or diagram',error_kind='4 drawings/diagrams',against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for x in r['doubts']:
 if x['place']=='cancelled word below (105)':x.update(reading=r'\deleted{\unsure{et|Et}}',alternatives=['et','Et'],reason='The crossed looping body does not securely distinguish uppercase E from lowercase e.')
for place,reading,alts,box,why in [
 ('Word before notation102',r'\unsure{avec|en}',['avec','en'],'B03','The small low run does not expose enough separate letter bodies to choose between the two short words.'),
 ('Suggestion, group before lieu/lien',r'\unsure{au|$\mathord{-}$}',['au','horizontal rule'],'B04','A short horizontal mark with a thick left return may be compressed au or a literal rule.'),
 ('Suggestion, word before de',r'\unsure{lieu|lien}',['lieu','lien'],'B04','Tall l, dotted i and the following low connected ending are clear, but the final u/n return is merged.')]:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='medium',reason=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates']))
r['notes']+='\n### Blind reading corrections\n\nThe lower annotations in106 and107 use straight brackets with short rising ends, without central cusps; these replace the brace shapes. The word before notation102, the short group before lieu/lien in the Suggestion, and the canceled initial et/Et remain uncertain. The canceled >=2-indexed limit, the literal capital L in the canceled union bound, and the incomplete edge word remain as written. The lower108 limit retains a plain rule, unlike the visibly headed marginal limit.\n'
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B01','The entire visible105 display has one upright and one wavy vertical stroke, with a separate (h), rather than an arrowhead or a two-rule rotated simeq. The lower V continues at the crop boundary and was fully read in the first pass; do not supply a new isolated V without d. Parentheses enclose the lower annotation, and a plain side leader crosses the right parenthesis to the condition. The lim endpoint remains uncertain as already recorded.')
put('B02','The crossed looping body permits et or Et; its exact case is not secure. Preserve the cancellation and broaden only this local case doubt.',True)
put('B03','The full106 display and revisions were viewed. The comma before the canceled lower L remains live; a separate old angular superscript follows the live upper L and is still flat/natural uncertain. The relation retains subset/equality ambiguity. The right superscript has the visible X_L* over the crossed old Z; do not omit the replacement. The lower annotation line has two short upturned ends and no central cusp, so use a square-ended bracket. Its following short word remains avec/en doubtful. Overlapping left-margin material belongs to the Suggestion in B04.',True)
put('B04','Both angular superscripts remain flat/natural uncertain. Before the tall dotted li-group there is a short horizontal mark; au/rule remains uncertain, and the terminal u/n in lieu/lien is merged. All three continuation rules, the i_n-1 index and the final starred X_i_n agree.',True)
put('B05','The entire107 expression, three lower unions and canceled union agree, including literal capital L after j<= in the old bound. The lower annotation has a flat middle and short rising ends without a central cusp; restore its bracket shape. Plain l versus ell is font encoding here, not a new letter.',True)
put('B06','The marginal limit has a distinct right arrowhead. The full index has d-in-Drap(J union L), both nonempty conditions with phi, comma and final V_d. Subscript versus underset encoding is immaterial.')
put('B07','The whole old equality and directed limit are crossed. The small >=2 group survives below Drap and is retained; the entire dense index remains doubtful rather than silently dropping that qualifier. The rightward limit head is still visible under the cancellation. Neighboring live J-prec-L belongs to B08.')
put('B08','The relation has two curved branches meeting at the left, matching prec on the previous page. There is no independent lower equality rule. The full donc si... et J et L des bandes is live, while the crossed material above is already recorded in B07.')
put('B09','The whole108 formula was inspected. Its lower limit stroke ends bluntly, without the separately turned arrowhead of B06, so keep underline-lim. Both phi signs, all union indices and the j/l ordering agree. The marginal fragments at the sides are already transcribed in their own notes and are not added again here.')
put('B10','The right page edge ends the noun at drapea plus an uncertain u; there is no surviving final x. The next word has q-descender and the t/i/o/n ending of question, not prenant. The overwritten middle chain group remains i-beta/revision uncertain, rather than a confident i1. Only NB is underlined. The first segm has no certified stop, the second does. The remaining memberships, initial/final words and star agree.')
put('B11','The short word after deux has the compact segm shape and a final stop, not the longer drapeaux. The set has one point and one rule with no extra comma after the rule. The crossed la-like group precedes the separate live est, whose e/s and upright t remain visible. Both phi signs and the three terminal dots agree; initial La/la remains uncertain.')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('098: all11 differing boxes viewed; four changed boxes.')
