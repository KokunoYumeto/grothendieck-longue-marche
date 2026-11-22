from pathlib import Path
import json
W=Path(__file__).resolve().parents[1];pg='150_scan087';rp=W/'records'/f'{pg}.json';r=json.loads(rp.read_text());c=json.loads((W/'second'/f'{pg}_comparison.json').read_text());b={x['box']:x for x in c['results']};notes={}
oldexp=r'\Sigma_{J,I\'-J}^{\deleted{\unsure{\flat}}}'
newexp=r'\Sigma_{J,I\'-J}^{\deleted{\unsure{I\'-J|I\'\setminus J}}}'
oldmark=r'\unsure{\uparrow}';newmark=r'\unsure{\uparrow|\rotatebox{-90}{$\in$}}'
oldT=r"\dot T_{\Sigma_J\Sigma_{I'}}";newT=r"\unsure{T_{\Sigma_J\Sigma_{I'}}^*|\dot T_{\Sigma_J\Sigma_{I'}}}"
oldbr=r"\underbrace{\mathring T_{\overset{\deleted{-}}{J}'}}_{\displaystyle\bigcup_{\deleted{\unsure{\forall}}j\in\overset{\deleted{-}}{J}'}\mathring T_j}"
br=r'''\underset{\displaystyle\bigcup_{\deleted{\unsure{\forall}}j\in\overset{\deleted{-}}{J}'}\mathring T_j}{\begin{tikzpicture}[baseline=(term.base)]
\node[inner sep=1pt] (term) {$\mathring T_{\overset{\deleted{-}}{J}'}$};
\draw ([yshift=.5pt]term.south west)--([yshift=-1.5pt]term.south west)--([yshift=-1.5pt]term.south east)--([yshift=.5pt]term.south east);
\end{tikzpicture}}'''
# The apostrophes in the raw Python literals above are ordinary TeX primes.
oldexp=oldexp.replace("\\'", "'");newexp=newexp.replace("\\'", "'")
reps=[("mais en général c'est différent", "mais en général - c'est différent"),(oldexp,newexp),(oldmark,newmark),(oldbr,br),(oldT,newT)]
p=W/'pages'/f'{pg}.tex';s=p.read_text()
for a,z in reps:assert s.count(a)==(3 if a==oldmark else 1),(a,s.count(a));s=s.replace(a,z)
p.write_text(s);(W/'records'/p.name).write_text(s)
ch={x['id']:x for x in r['changes']}
ch['C04']['final']=ch['C04']['final'].replace(oldmark,newmark)
ch['C05'].update(final=r"^{\deleted{\unsure{I'-J|I'\setminus J}}}",against_C=True,confidence='medium',evidence='The crossed superscript extends across three groups: a tall I-like form with a separate prime, an intervening stroke, and a right-hand J with a lower hook. It is wider than one flat/natural glyph. The middle separator remains obscured; retain I-prime minus/slash J alternatives under the deletion.',crop=f'crops/{pg}_blind_B05.png',box=b['B05']['coordinates'])
ch['C20']['final']=ch['C20']['final'].replace(oldT,newT)
for ident,place,C,H,final,box,why,kind,ek in [
 ('C23','Marginal note attached to75, dash after général',"mais en général c'est différent", "mais en général c'est différent", "mais en général - c'est différent",'B03','A separate short horizontal stroke follows the final l return of général with a clear white gap. It is not continuous with the letter and is restored as a dash.','omission','3 omissions'),
 ('C24','(77), inner lower bracket under the open-T term',oldbr,'annotation by the inner union',br,'B07','The inner annotation line has a flat base with upward ends, no middle cusp. The wider outer annotation below has a distinct central cusp. Preserve the difference between the square-ended inner bracket and the outer brace.','drawing or diagram','4 drawings/diagrams')]:
 r['changes'].append(dict(id=ident,place=place,C=C,H=H,final=final,evidence=why,crop=f'crops/{pg}_blind_{box}.png',box=b[box]['coordinates'],confidence='high',kind=kind,error_kind=ek,against_C=True,against_H=True,consequential=False,marked_in_H=False,phase='blind audit'))
for d in r['doubts']:
 if 'separately cancelled exponent' in d['place']:d.update(reading=r"\deleted{\unsure{I'-J|I'\setminus J}}",alternatives=["I'-J",r"I'\setminus J"],reason=ch['C05']['evidence'])
 if 'three lower upward marks' in d['place']:d.update(reading=newmark,alternatives=['upward arrow','quarter-turned membership'],reason='Each sign has an outer arch and a central stroke; these can be either an upward arrow with curved head or quarter-turned membership. Cancellation prevents resolving their construction, so both readings are explicit.')
r['doubts'].append(dict(place='(79), small T decoration in the vertical-arrow label',reading=newT,alternatives=['star','dot'],confidence='medium',reason='The tiny raised mark has several angular projections, unlike the round filled dots in75–78, but its size and retracing prevent distinguishing a star from a rough dot with certainty. The subscripts have no separating comma.',crop=f'crops/{pg}_blind_B10.png',box=b['B10']['coordinates']))
for x in r['inventory']:
 if 'first_words_or_objects' in x:
  for a,z in reps:x['first_words_or_objects']=x['first_words_or_objects'].replace(a,z)
r['notes']+='\n### Blind reading corrections\n\nThe small note attached to (75) includes a detached dash after général. The separately canceled superscript in the right-hand note to (76) is a multi-character I-prime–J expression, with its separator still uncertain; it is not adequately represented by a single flat. The three lower signs in the discarded construction of (76) remain uncertain between upward arrows and quarter-turned membership signs. The inner annotation in (77) has a square-ended bracket, whereas the larger outer annotation is a cusp brace. The tiny raised T decoration in the vertical label of (79) is now marked star/dot; the adjacent Sigma subscripts still have no separating comma. The recurring Sigma exponent in77–79 remains unresolved as to both glyph and cancellation state. No new proof is claimed.\n'
def put(box,why,changed=False):
 notes[box]=dict(viewed=True,evidence=why)
 if changed:
  f=b[box]['first']
  for a,z in reps:f=f.replace(a,z)
  notes[box].update(changed=True,final=f)
put('B02','The second union has two successive j-like traces: an old lower one crossed by short strokes, followed by the live j. Keep their distinct states. The barred capital has an upright with bilateral horizontal strokes, favouring I, but its retraced lower end still leaves J possible. The complete75 formula was reread; tag placement and display wrappers do not alter its text.')
put('B03','The leader runs upward toward the equality in75, so the marginal attachment remains there. A detached horizontal stroke lies after général, separated from the final l by white paper; restore it as a dash. The words mais, en général, c’est différent and three final dots are otherwise clear.',True)
put('B04','The full exact crop was viewed at2600 pixels. The limit label has its small a as a low dot-like join before p. Both prose conditions, singular terms, I-prime and differences agree. The old sign after the parenthesis remains a heavily crossed arch, not a secure i0 or equals. Each of the three lower signs has a curved outer arch and central stroke; add quarter-turned membership as an alternative to upward arrow. No separate J under the live d can be detached confidently from the surrounding cancellation return; preserve only the clear right J and middle I-prime-minus-J labels.',True)
put('B05',ch['C05']['evidence']+' The live lower index remains J,I-prime minus J; the two parentheses and77 agree.',True)
put('B06','The initial verb is partly clipped at the lower edge, but its p descender is visible and continues in the overlapping top of B07. Keep On pose rather than note. Rappelons-le has two long p descenders and the separate hyphen; the full parenthesis is preserved.')
put('B07','The recurring leading superscript has crossed upper strokes and a lower bowl; the crop does not settle flat/natural or whether an independent strike is present, so all four existing alternatives remain. Both cancellations over J-prime affect only the bars; the primes stay live. The old character before j is too crossed to distinguish forall/i/j. The inner lower bracket is flat with raised ends; only the outer annotation has a central cusp. All formula terms and both unions were reread.',True)
put('B08','The NB, two I-prime Sigma terms, slash, intersection and open T with a clean overbar on J-prime agree. A centered mathring and the blind circle superscript represent the same visible small circle. No punctuation is added.')
put('B09','The repeated exponent remains uncertain in identity and deletion state, as in77. The small middle a-like join in Drap is present before its p. Both bound clauses are singular, the limit has one headed rule, and there is no final stop. Differences in tag and limit macros do not alter this reading.')
put('B10','The rightward link has a left hook and one pointed right head; the downward link has one head. Inclusion canonique is below the horizontal shaft, and induit par is at left. The tiny T decoration has angular projections and is now star/dot uncertain. The two small Sigma subscripts are adjacent with no separate comma. The leading exponent retains the same glyph/state doubts as77–78, and On a at the top is fully preserved.',True)
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'second'/f'{pg}_root_crop_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('087: all9 differing boxes observed; five changed boxes.')
