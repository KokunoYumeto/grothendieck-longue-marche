from pathlib import Path
import json
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1];page='147_scan135'
p=root/'pages'/f'{page}.tex';t=p.read_text()
sub=[('de notations, en interver-',r'de \unsure{notations|notation}, en interver-'),
 (r'D^{\deleted{*}}',r'D^{\unsure{\deleted{*}}}'),
 ("d'espaces analytiques lisses",r"d'\unsure{espaces|espace} \unsure{analytiques|analytique} \unsure{lisses|lisse}"),
 (r'\unsure{ainsi|et}',r'\unsure{car il|ainsi|et}'),
 ('.. controls (1.6,0.55) and (4.65,0.65) .. (5.0,0.45)',r';'+'\n'+r'\draw (2.1,0.65) .. controls (3.0,0.45) and (4.65,0.65) .. (5.0,0.45)')]
for a,b in sub:
 assert a in t,(page,a)
 t=t.replace(a,b)
p.write_text(t)
f=root/'work'/f'{page}_final.json';r=json.loads(f.read_text())
for c in r['changes']:
 if c['id'].endswith('-11'):
  c['final']=c['final'].replace('de notations,',r'de \unsure{notations|notation},')
  c['evidence']+=' Blind audit separates the enclosing drawing into three open contour strokes: the upper-left parenthetical curve ends before the independent contour surrounding the right formula object. The compressed ending of notation(s) remains uncertain.'
  c['confidence']='medium';c['crop']=page+'_second_B08.png'
 if c['id'].endswith('-16'):
  c['final']=c['final'].replace(r'D^{\deleted{*}}',r'D^{\unsure{\deleted{*}}}')
  c['evidence']+=' Independent audit keeps the heavy upper star-like group, while marking whether its extra crossings are cancellation as uncertain.'
  c['confidence']='medium'
 if c['id'].endswith('-19'):
  c['final']=c['final'].replace(r'\unsure{ainsi|et}',r'\unsure{car il|ainsi|et}')
  c['differs_C']=True;c['confidence']='low'
  c['evidence']+=' The independent crop exposes a low open initial group and a separate taller final group, favouring car il among the candidates. The q-descender from analytiques above still interferes, so the alternatives remain explicit. The dotted final i in cancelled qui remains visible.'
  c['crop']=page+'_second_B12.png';c['box']=[312,1992,1648,2227]
for d in r['doubts']:
 if d['place']=='L17 insertion':d.update(reading=r'\unsure{car il|ainsi|et}',alternatives='car il; ainsi; et',reason='Two compact groups, the latter with a taller return, favour car il, but the descending q from the line above obstructs the last part.')
r['doubts'] += [dict(place='warning, notation(s)',reading=r'\unsure{notations|notation}',alternatives='notations; notation',confidence='medium',reason='A compressed low terminal run before the comma does not isolate a separate final s.'),dict(place='(223), star above left D',reading=r'\unsure{\deleted{*}}',alternatives='star crossed out; heavily retraced live star',confidence='medium',reason='Several extra dark strokes overlap the small star; their cancellation status remains uncertain.'),dict(place='L16, nominal phrase endings',reading=r"d'\unsure{espaces|espace} \unsure{analytiques|analytique} \unsure{lisses|lisse}",alternatives='each plural ending; corresponding singular ending',confidence='medium',reason='The low end strokes of all three words are compressed. The two readings disagree on final s; grammar is not used to resolve them.')]
for d in r['decisions']:
 if d['id']=='M0024':d.update(reading=r'\unsure{car il|ainsi|et}',evidence=d['evidence']+' The blind reading adds car il, now preferred from the two separate groups, while the obstruction leaves the mark undecided.')
for i in r['inventory']:
 if i['element']=='E23':i['first_words_or_objects']=r'\unsure{car il|ainsi|et}'
r['notes']+=' Blind audit restores three separate contours around the split warning and marks the notation(s) ending and the overwritten star’s cancellation status as uncertain. The lower insertion is now preferred car il with ainsi/et retained. The three plural/singular endings remain locally doubtful, without changing the preferred plural forms. No mathematical assertion was checked in this audit.'
f.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
comp=json.loads((root/'second'/f'{page}_comparison.json').read_text());ds={x['box']:x for x in comp['differences']}
ev={
'B01':('The crossed e after un has an open rounded eye. The preceding overwritten group has an apparent descending q-like stroke and unresolved middle; équiv. remains doubtful rather than replacing it with a definite épi. A baseline point follows ess and the t is raised. The live isomorphisme and underlines remain.', 'low'),
'B02':('The inserted seul sits above its leader. The first pose is struck across its middle, so its letters remain doubtful despite agreement on the proposed word.', 'medium'),
'B03':('The initial live e-loop and s/t strokes form est. The crossing diagonal marginal writing supplies nearby marks but no independent c-apostrophe is securely present.', 'high'),
'B04':('The three disputed greater-than signs have hooked or retraced lower legs, with no separate equality bars. The final signs provide local comparison. Retain the literal short separator and the cancelled/inserted phrase, with its existing doubt.', 'high'),
'B05':('The label is (221); only math-mode serialization differs.', 'high'),
'B07':('The exposed accent, f stem and two dotted i positions support définir; the diagonal margin crosses its initial part without cancelling it. Hom has no final point.', 'medium'),
'B08':('Two formula objects and one rightward arrow agree. The right terminal r has no separate prime. The annotation spans above and below the formula. Three separate open contours occur: an upper-left curved stroke, a surrounding right-object stroke, and a lower curved stroke. The earlier joined first two contours are separated. The compressed notation(s) ending remains locally doubtful.', 'medium'),
'B09':('De has no separate final s. The raised terminal t of strict.t survives. The first sentence has auquel and a p-descender followed by -arvient, then aussitôt; no separate première/simplif. groups appear. The later corresponding phrase has the longer -ant return before the colon. The two D objects and their arrow agree; existing on and punctuation doubts remain.', 'medium'),
'B10':('The two D objects and the right terminal r-prime are visible. The dense star-like mark over the left D has extra crossing strokes, but cancellation versus retracing is now marked uncertain. The literal separators retain their local doubt.', 'medium'),
'B11':('The short group before the star has low a/v/e/c-like strokes; avec remains supported. Locale is written above the end of immersion with its leader. The other text agrees.', 'medium'),
'B12':('All three word endings have compressed low strokes, so plural/singular alternatives are added with the earlier plurals first. The cancelled word has a dotted final i, supporting qui. The interlinear correction has two groups, a low open car-like run and a taller il-like group; car il is preferred with ainsi/et alternatives because the q-descender above crosses its right side.', 'low')}
choices=[]
for b,d in ds.items():
 final=d['first']
 for a,z in sub:final=final.replace(a,z)
 it=dict(box=b,choice='literal' if final!=d['first'] else 'first',changed=final!=d['first'],evidence=ev[b][0],confidence=ev[b][1])
 if it['choice']=='literal':it['final']=final
 choices.append(it)
(root/'work'/f'{page}_audit_choices.json').write_text(json.dumps(dict(reader='audit_b',choices=choices),ensure_ascii=False,indent=2)+'\n')
with (root/'work/root_views.tsv').open('a') as v:
 for b in ds:v.write(f'{datetime.now(timezone.utc).isoformat()}\t{page}_second_{b}.png\troot blind-audit adjudication\n')
