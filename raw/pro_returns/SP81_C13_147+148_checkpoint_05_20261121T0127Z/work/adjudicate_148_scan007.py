from pathlib import Path
import json
r=Path('edition');page='148_scan007';p=r/'work'/f'{page}_final.json';q=json.loads(p.read_text());assert not q.get('audit')
d={x['box']:x for x in json.loads((r/'second'/f'{page}_comparison.json').read_text())['differences']}
pt=r/'pages'/f'{page}.tex';t=pt.read_text();final={k:v['first'] for k,v in d.items()}
final['B11']=final['B11'].replace('formant ',r'\unsure{formant|forment} ')
final['B13']=final['B13'].replace(r'\inserted{4}',r'\inserted{$4^{\unsure{\frown}}$}')
final['B17']=final['B17'].replace(r'\unsure{X}',r'\unsure{X|X_S}').replace(r'\unsure{S}',r'\unsure{S|2}')
final['B18']=final['B18'].replace('carrées',r'\unsure{carrées|carrés}')
# Local coordinate conversion for the observed angular projections: x=188+78.5u, y=183-72.5v.
projections=r'''% Short angular projections on the thick grid strokes; direction remains unassigned.
\draw[line width=.7pt] (188,121.375)--(182.505,121.375)--(188,133.7);
\draw[line width=.6pt] (190.355,72.075)--(195.85,73.525)--(190.355,64.1);
\draw[line width=.7pt] (198.205,182.275)--(208.41,186.625)--(207.625,179.375);
\draw[line width=.7pt] (280.63,182.275)--(286.125,190.25)--(291.62,180.1);
\draw[line width=.7pt] (239.025,109.05)--(250.015,112.675)--(238.24,115.575);
\draw[line width=.6pt] (262.575,130.8)--(257.08,137.325)--(263.36,143.125);
\draw[line width=.6pt] (262.575,58.3)--(257.865,54.675)--(263.36,48.15);
'''
final['B15']=final['B15'].replace('% Hatching, preserving the changing directions.',projections+'% Hatching, preserving the changing directions.')
final['B21']=final['B21'].replace(r'\eta\' ',r'\eta\' ')
final['B21']=final['B21'].replace(r"\unsure{\eta'^{\natural}|\eta'^{q}}",r"\unsure{\eta'^{\natural}|\eta'^{q}|\bar{\eta'}}").replace(r"\unsure{\eta''^{\natural}|\eta''^{q}}",r"\unsure{\eta''^{\natural}|\eta''^{q}|\bar{\eta''}}")
final['B22']=d['B22']['second'].replace('x=1.1cm,y=1.1cm','x=.55cm,y=.55cm').replace(r'\unsure{\natural|\flat}',r'\unsure{\natural|q}')
for k in ['B11','B13','B15','B17','B18','B21','B22']:
 assert d[k]['first'] in t,k
 t=t.replace(d[k]['first'],final[k])
pt.write_text(t)
e={
'B02':'The left 2, parentheses and X with a lowered curved S are exposed. The second transcription changes the font case of that lowered S; its ink form matches the broad-curved lower letter elsewhere on this page. First notation retained.',
'B03':'The crop gives Aut, parenthesized X with lowered S, a curved upper equivalence stroke above a straight bar, and the two doubled Z forms with /4 between. The terminal dark point is present. Macro and font-case differences retain the first notation.',
'B04':'The dotted i is followed by a separate d-e-f group above the equality; the latter is not all attached to the parenthesized X. The f-like upright crossing the upper parenthesis remains locally uncertain. The early curly-shaped glyph before the distinct separator is retained with uncertainty about its cancellation state. First complete formula retained.',
'B05':'Two oblique arms survive in the small canceled upper cluster, supporting X tentatively. The lower large loop is contextual writing at the start of La; the cancellation does not expose a separately secure lowered s. The original local doubt is retained.',
'B06':'The initial open c, small middle loop and long low hooked ending support can first, with ces still possible. There is no separate dark terminal point. The second reader agrees with the preferred letters but does not settle the compressed join.',
'B07':'The enlarged baseline exposes avec, the angular 1, sommet, e, deux arêtes and both commas. Both readings contain these same characters; math wrappers do not change the reading.',
'B08':'The first inserted word has the open c and compressed e-s ending. The next begins with a small dark a, then the rising r/ê/t group and low e-s terminal; comparison with the adjacent baseline arêtes supports the same sequence. The long brace beneath attaches both words before correspondant. First ces arêtes retained.',
'B10':'The raised identity glyphs are a dotted i and tall looped d; the 2 and lowered X with S are exposed. Both readings have the same symbols apart from font case. First retained.',
'B11':'The word after the opening parenthesis has a tall looped f and a compressed low connected run ending in a small tall return. Formant remains first; the low vowel before the ending also admits forment. Four, sommets, the parentheses and left-lowered 2 remain unchanged.',
'B12':'The struck word exposes a descending initial q and tall t, but the horizontal cancellation obscures the middle and final low strokes. Huit is clear above it. The first local doubt on quatre remains.',
'B13':'Two cancellation lines cross the opening parenthesis, underlined NB and tentative le. Above them, the angular 4 has a separate short downward-opening arc at its upper right. The arc is now retained as a doubtful raised drawn sign. Its identity remains unresolved; no closing parenthesis is supplied.',
'B14':'Both readings record two doubled Z forms with /4 and the curved-over-bar relation followed by mu with lowered 4 and parenthesized doubled C. The first mathematical serialization is retained.',
'B15':'The four exposed labels, eight thick grid half-segments, four broken half-segments, detached oblique runs and changing hatch directions are preserved. Several thick strokes have short angular projections, now drawn without assigning directions. The dense central cluster stays as its actual paths; its overlapping strokes do not settle the proposed xi/asterisk letter identity. First open joins and actual cluster are retained.',
'B16':'Le begins with the long L foot and small closed e. After mieux, the final compressed stroke run of the adjective leaves the extra terminal e uncertain. Adaptée remains first with adapté as alternative; the second reading does not resolve the final count.',
'B17':'The canceled leading X-like cluster includes an exposed low return, now allowing a lowered S alternative. The following tall E and looped letter with a low oval remain separate. The struck argument has two lobes and a low extension: S remains first, with the second reading 2 admitted. The whole original cancellation and live X_S/plus-minus-1 remain.',
'B18':'The crossed deux and raised faces with its attachment are clear. In carrées, the two crowded low loops following the tall/retraced r group leave the final-e count uncertain; carrées remains first and carrés is retained as an alternative. The comma is exposed.',
'B19':'The long horizontal strike crosses carré and leaves the small dark punctuation mark to its right. That mark has a short downward projection but no securely long comma tail. The first comma/full-stop uncertainty remains.',
'B20':'Each raised sign has an upper rising arm and a right-hand descending arm linked through an angular loop or crossbar. Natural remains first and q remains admissible. The long lower arm is on the right of the loop, so the blind flat candidate is not adopted. All four base letters, prime counts and commas are preserved.',
'B21':'Both drawings show four filled marks, two equatorial curves, the gapped outer contour and long cancellation strokes. The first paths retain the pale oblique continuations. The upper-left and lower-right crowded labels also expose horizontal bars; barred alternatives are added beside the first uncertain raised-sign readings. The upper-right bar-eta and lower-left bar-e remain.',
'B22':'The crop exposes four filled points, a continuous bowed front curve and a rear curve made of separate uneven strokes. The second geometry preserves the detached rear segments, retraced rim and three short inward ticks. It is adopted at the existing approximate size, retaining the first natural/q label alternatives supported by their two offset arms.'}
# Update existing witness loci only; same-preference uncertainty changes add no error-count rows.
link={'06':'B13','07':'B15','09':'B17','10':'B18','13':'B21','14':'B22'}
boxes={x['box']:[int(x[y]) for y in ('x0','y0','x1','y1')] for x in __import__('csv').DictReader((r/'second'/f'{page}_boxes.tsv').open(),delimiter='\t')}
for c in q['changes']:
 k=link.get(c['id'].rsplit('-',1)[-1])
 if k:
  c.update(final=final[k],evidence=e[k],crop=f'{page}_second_{k}.png',box=boxes[k])
  if k=='B13':c['differs_C']=True
  if k=='B18':c['confidence']='medium'
for item in q['inventory']:
 x=item['first_words_or_objects']
 x=x.replace('formant ',r'\unsure{formant|forment} ').replace(r'\unsure{X}\mathbb E',r'\unsure{X|X_S}\mathbb E').replace(r'(\unsure{S})',r'(\unsure{S|2})')
 if item['element']=='E16':x=r'$4^{\unsure{\frown}}$'
 if item['element']=='E25':x=x.replace('carrées',r'\unsure{carrées|carrés}')
 item['first_words_or_objects']=x
q['doubts'] += [dict(place='compressed word after 4 sommets',reading=r'\unsure{formant|forment}',alternatives='formant / forment',confidence='medium',reason=e['B11']),dict(place='short raised arc beside inserted 4',reading=r'4^{\unsure{\frown}}',alternatives='drawn downward-opening arc; character identity unresolved',confidence='low',reason=e['B13']),dict(place='ending of the adjective after inserted faces',reading=r'\unsure{carrées|carrés}',alternatives='carrées / carrés',confidence='medium',reason=e['B18'])]
for x in q['doubts']:
 if x['place']=='leading cancelled cluster of the quotient display':x.update(reading=r'\deleted{\unsure{X|X_S}}',alternatives='X / X with lowered S',reason=e['B17'])
 if x['place']=='parenthesized cancelled argument':x.update(reading=r'\unsure{S|2}',alternatives='S / 2',reason=e['B17'])
 if x['place']=='upper-left label of cancelled sphere':x.update(reading=r"\unsure{\eta'^{\natural}|\eta'^{q}|\bar{\eta'}}",alternatives='raised natural / raised q / bar over eta prime',reason=e['B21'])
 if x['place']=='lower-right label of cancelled sphere':x.update(reading=r"\unsure{\eta''^{\natural}|\eta''^{q}|\bar{\eta''}}",alternatives='raised natural / raised q / bar over eta double prime',reason=e['B21'])
q['notes']+=' Blind audit: a small raised arc beside the inserted 4 is retained; its identity is unresolved. Angular grid projections and uneven detached rear-sphere segments are reproduced. The canceled argument retains S/2 and the crowded adjective and connective endings retain alternatives. None of these decisions was supplied by an expected formula.'
p.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
choices=[dict(box=k,choice='literal' if final[k]!=d[k]['first'] else 'first',**({'final':final[k]} if final[k]!=d[k]['first'] else {}),changed=final[k]!=d[k]['first'],evidence=e[k],confidence='low' if k in ['B04','B05','B17'] else ('high' if k in ['B07','B10','B14'] else 'medium')) for k in d]
(r/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_a',choices=choices),ensure_ascii=False,indent=2)+'\n')
