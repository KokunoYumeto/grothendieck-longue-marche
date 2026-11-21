"""Root's manual image adjudication of the ten differing blind boxes."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
p='149_scan029'
rp=R/'records'/f'{p}.json'; r=json.loads(rp.read_text())
pp=R/'pages'/f'{p}.tex'; s=pp.read_text()
cmp={x['box']:x for x in json.loads((R/'second'/f'{p}_comparison.json').read_text())}
finals={k:v['first'] for k,v in cmp.items()}
repl=[
 (r'$\pi_1(X)$ a un centre trivial. En car.',r'$\pi_1(X)$ \illegible{1} un centre trivial. \unsure{En} car.'),
 (r"notons qu'il suffit de travailler avec les groupes fondamentaux premiers à",r"notons qu'il \unsure{suffit} de \unsure{travailler} \unsure{avec} les groupes \unsure{fondamentaux} \unsure{premiers} à"),
 (r'des groupes fondamentaux.}',r'des \unsure{groupes} \unsure{fondamentaux}.}'),
 (r'\deleted{Choisissons une}',r'\deleted{\unsure{Choisissons} une}'),
 (r"\deleted{\unsure{des $k$ l'}}",r"\deleted{\unsure{des $k$ l'|des $f_k\,\ell$}}"),
 (r'\unsure{déduite|déduits}',r'déduite'),
 (r'On a donc $\pi_1(\overline f)$, $\pi_1(\overline g)$',r'On a donc $\pi_1(\overline f)\ne\pi_1(\overline g)$'),
 (r'Mais ces hypothèses',r'Mais ces \unsure{hypothèses|hyp. mises}'),
 (r'ainsi que les hom.',r'ainsi que les hom'),
]
for old,new in repl:
 assert old in s,old
 s=s.replace(old,new,1)
for b in ['B01','B05','B07','B08','B10','B11','B13']:
 f=finals[b]
 for old,new in repl:
  if old in f:f=f.replace(old,new)
 if b=='B10':f=f.replace(r'$\pi_1(\overline f)$, $\pi_1(\overline g)$',r'$\pi_1(\overline f)\ne\pi_1(\overline g)$')
 finals[b]=f
assert finals['B10']!=cmp['B10']['first']
pp.write_text(s)
r['rows'][0]['final']=r"notons qu'il \unsure{suffit}"
r['rows'][0]['scan_shows']+=' Blind audit: the terminal t is suggested, but the cancellation hides medial letter parts; suffit is now locally doubtful. This certainty change is not another material row.'
r['rows'][5]['final']=repl[4][1]
r['rows'][5]['scan_shows']+=' Blind B07: a looped f-like upright and low attached cluster permit f_k followed by a tall looped ell as an alternative; the crossing prevents a secure choice. This does not resolve the old k/l reading.'
r['rows'][7].update(final='déduite',confidence='high',scan_shows='Blind B08: after the tall crossed t the final stroke makes a closed low oval with a rightward exit, matching e; it lacks the open curl of s. The inserted X,Y has a separate trailing comma. The added first-phase doubt is resolved; C already read déduite, so no new C change is counted.')
def row(place,C,H,final,kind,category,ink,b,consequential=False):
 return dict(place=place,C=C,H=H,final=final,against_C=True,against_H=True,kind=kind,error_category=category,scan_shows=ink,crop=f'crops/{p}_second_{b}.jpg',box=next(x['coords'] for x in r['audit_boxes'] if x['box']==b),confidence='high',marked_in_H=False,consequential=consequential)
r['rows'].append(row('relation between the two base-changed maps, blind B10',r'$\pi_1(\overline f)$, $\pi_1(\overline g)$',r'$\pi_1(\overline f),\pi_1(\overline g)$',r'$\pi_1(\overline f)\ne\pi_1(\overline g)$','misread symbol or index','Symbols and indices','The sign has two distinct short horizontal bars and one long crossing stroke that continues below them. It is a narrow not-equal sign, not a comma. The full formula and the small sign detail were both viewed; mathematical expectation did not decide the relation.','B10',True))
r['rows'].append(row('hom before the lower pair of induced maps, blind B13','hom.','hom.','hom','text not on the page','Abbreviations expanded, spelling modernised','The contracted h-o-m has a continuous terminal return; the following gap contains no independent ink stop. Both witnesses supplied a period.','B13'))
r['doubts']=[d for d in r['doubts'] if d['place']!='next line initial verb']
for d in r['doubts']:
 if d['place']=='cancelled phrase after dans k':
  d.update(alternatives=r'des $f_k\,\ell$',reason='The middle has a looped upright with a low attached cluster and a following tall loop; the strike prevents choosing k/l-prime against f_k/ell.')
new_doubts=[('cancelled opening after pi_1(X)','one obscured word','a','The heavy diagonal covers the word body; a is the former proposed reading, not securely readable ink.'),('cancelled opening before car.','En','','The n survives but the E is crossed.'),('cancelled opening after qu’il','suffit','','The broad strike merges parts of the short letter sequence.'),('cancelled opening after de','travailler','','Several medial strokes are covered by the crossing.'),('cancelled opening before les groupes','avec','','The crossing masks part of the low letter chain.'),('cancelled opening first occurrence','fondamentaux','','The cancellation runs through medial strokes.'),('cancelled opening before à p','premiers','','The central sequence is partly covered.'),('cancelled opening last line','groupes','','The cancellation crosses the low letters.'),('cancelled opening last word','fondamentaux','','The crossing masks the medial word body.'),('cancelled replacement opening','Choisissons','','The terminal letter chain merges with its horizontal strike.'),('second paragraph after ces','hypothèses','hyp. mises','After hyp the small rounded mark could be a collapsed o or a stop; the following tall joined strokes permit th or an m-like reading. The alternatives are not silently expanded or regularised.')]
for place,reading,alts,reason in new_doubts:r['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence='low' if place.startswith('cancelled opening') else 'medium',reason=reason))
r['notes']=r['notes'].replace('Keep the e-like déduite ending primary; do not force grammatical agreement.','The blind B08 crop resolves the closed terminal e in déduite; no grammatical agreement is imposed.').replace('The heavy separator between pi_1(fbar) and pi_1(gbar) is retained as a comma: its main stroke descends below the text rather than forming a symmetric plus.','Blind B10 corrects the separator between pi_1(fbar) and pi_1(gbar) to a narrow not-equal sign: two horizontal bars are crossed by a long descending stroke. This changes the written relation; no inference from the surrounding reconstruction argument was used to make the correction.')
r['notes']+='\n\n[Blind audit] The obscured opening word after pi_1(X) and several crossed words are now locally doubtful. The compressed hypothèses / hyp. mises outline remains unresolved. The hom abbreviation before the induced maps has no visible stop. The cancelled old field symbol and old (X),(Y) remain cancelled, while the final source K remains resolved. All ten differing boxes were viewed by the main reader.'
for h in r['hand_log']:
 if h['habit']=='Small terminal loop after t can look like e or s':h.update(scope='Resolved locally by the blind B08 crop.',witness_errors='The final closed oval supports C’s e; H’s s is rejected.')
r['hand_log'].append(dict(habit='A narrow not-equal sign can resemble a retraced comma',places='149_scan029, between pi_1(fbar) and pi_1(gbar), B10',scope='Two horizontal bars and the long crossing stroke are visible in this occurrence.',witness_errors='Both witnesses and the first consolidated reading treated it as a comma.'))
for a in r['abbreviations']:
 if a['form']=='hom.':a['form']='hom'
r['notation'].append(dict(form=r'\pi_1(\overline f)\ne\pi_1(\overline g)',meaning='The literal relation in the reduction paragraph.',evidence='Blind B10 and its sign detail show two bars crossed by a descending stroke.'))
inks={
'B01':'O-P-S has a single upper P bowl, and the pi index is the small 1 hook. The heavy crossing obscures the one word after pi_1(X), so it is now illegible locally; En and seven partly crossed words receive local doubts. The low s-u-r and tall l-es after the shorthand remain sur les, not avec la; the initial tall l/oca/l outline excludes cohomologie. Keep localisations/localisés and the barred-m/equality alternatives. The paragraph remains wholly cancelled.',
'B05':'The horizontal strike merges the terminal letters of Choisissons, now doubtful. The raised field letter has the two angular right arms of K; a retraced loop does not establish a Q alternative. Keep une and the insertion placement.',
'B06':'A separate stroke crosses the old barred symbol, so its deleted state stays. Its K/Q ambiguity remains; the scan does not justify a double-struck alphabet. The following de belongs to the adjacent baseline and is not removed because the tight blind box omitted it.',
'B07':'The old initial d and low es survive; the middle has a looped upright with a low attached cluster and the next stroke is tall and looped. Add f_k ell as an alternative to the old doubtful k/l-prime reading without resolving it. A horizontal cancellation crosses the final s-initial word at the raised subject’s height, so retain nested deleted sur/se within the insertion.',
'B08':'The terminal e is a closed low oval after the tall t, not an open s curl. Resolve the added first-phase doubt to déduite. The raised X,Y is followed by a separate dark descending comma, retained inside the insertion.',
'B09':'The surviving source letter has the tall upright and two angular K arms despite its round underlying trace; retain resolved K. The destination has a clear bar and K. The sentence period shown by the second reader is already present immediately after this snippet in the page.',
'B10':'The separator has two distinct short horizontal bars and a long crossing stroke, visible again in the saved sign detail; correct the comma to not-equal. The full formula is read with both index-1 marks and bars. The word after pi_1(Xbar) has no detached accent stroke: retain a, not à. The remainder agrees.',
'B11':'The small mark after hyp is round enough to be a collapsed o but also stop-like, and the following joined tall strokes can be th or m-like. The image does not securely decide the expanded word against the split form; retain both as hypothèses / hyp. mises. Ces remains plain; no grammar-based completion is made.',
'B12':'The crossed X has two diagonals and the crossed Y a fork plus downward stem, each within parentheses; retain them without new doubt. The small barred K has the same narrow K form as both X/K and Y/K labels; lower-case k is not established. Inline math grouping alone is typographic. The baseline de and all replacement attachments stay.',
'B13':'No separate period follows the continuous final return of hom: remove the supplied stop. A detached pale acute-shaped mark sits over the initial e of réconstruits and remains. Extérieure has a visible tall t, dotted i and low ending; the added blind doubt is unnecessary. Commas, pi indices/bars, baseline de and the raised list remain; math grouping differences are formatting only.'}
reviews=[]
for b,x in cmp.items():
 if not x['different']:continue
 changed=finals[b]!=x['first']
 reviews.append(dict(box=b,decision=('correct' if b in ['B08','B10','B13'] else 'mark doubt') if changed else 'keep',final=finals[b],ink=inks[b],changed=changed))
(R/'second'/f'{p}_review.json').write_text(json.dumps({'box_reviews':reviews},ensure_ascii=False,indent=2)+'\n')
rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
