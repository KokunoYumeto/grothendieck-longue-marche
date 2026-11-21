"""Manual blind-crop adjudication, preserving the two independent TSVs."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan038'
r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b, decision, evidence, changed=False):dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b05','retain first','Both readers retain the same F alphabet doubt, equivalence sign and plain C with a hat; the only difference is the math delimiter.')
d('b06','retain first','The initial d loop is followed by connected low a/n strokes and a final return: dans is supported. The later inserted dans has the same compressed outline. The cancelled du and the raised où dans le remain in their distinct layers.')
d('b07','retain first','The low replacement has a short connected ou body and a detached accent, supporting où rather than three letters on a. The short curved pi is retained against the straighter large Pi below. Parts of réduit à and the braced 1 survive under the strike; the whole old phrase remains unsure, rather than being replaced by three illegible words. The final curved stroke starts low beside the formula and descends as a comma; no second stop is added after (19).')
d('b08','mark doubt on X exponent; retain iso','The raised X mark is thick and has a short returning arm; a compressed star and a looped ell cannot be securely separated. The surrounding notation favors star but does not erase the ambiguity. After the formula there is a distinct dotted i followed by joined s/o, reading iso, and then a closing parenthesis. The double-shaft implication and the single arrow with tilde are clear.',True)
d('b09','retain first','The cancelled word has surviving onset and returns sufficient for the provisional alors, but stays unsure. The final i of défini is dotted; an extra e is not securely separable, so the existing ending doubt stays. The {a,b} seen at the bottom of this box belongs to the next line and is transcribed there.')
d('b10','retain first','The braces enclose a,b above the struck somme and attach at its place, with a comma at right. Extra crossed words at the bottom edge are separately included in b11 and the page; they are not duplicated here.')
d('b11','retain first','The long strikes conceal the central words; the existing illegible span and explicit doubts remain. The initial f/l ascenders of flèches and the final catégorie survive; the lower line retains objets, groupoïdes and composants. The reduced insertion has figurer-like descending strokes and en la followed by locally crossed une. Its provisional reading is retained without claiming every letter resolved. Extra top-line context in the second reading is already transcribed.')
d('b12','retain first within outer deletion','The looped d and return of de precede (8), with no 1 before 8. This fragment already lies inside the page’s large outer deleted block; the second reader adds that wrapper locally, so there is no deletion-state change.')
d('b13','retain first within outer deletion','The isolated crossed sign retains a descending stem but the side marks merge with the hatching; p stays unsure and an independent subscript star is not established. A= is raised before the tall Pi formula and retains its insertion status. The global cancellation is already present around the whole passage.')
d('b14','retain first within outer deletion','The old V, star-like remnant and forked overstroke overlap; both old starred/unstarred readings and the uncertain Y replacement remain explicitly open. The low curved mark after the indexed expression is retained as the written comma; it does not establish an additional full-height argument parenthesis. The outer cancellation is already encoded.')
d('b15','broaden old formula and word-ending doubts','The locally crossed V has a raised star-like remnant beside the clear replacement X-star. The old formula now allows starred as well as unstarred V. The low compressed end of définies does not securely isolate an e before the final return, so définies/définis stays open. The whole passage remains globally cancelled.',True)
d('b16','retain first within outer deletion','Two separate points after flèches form a colon. The long diagonal crosses the gap but does not create those points. The outer deleted wrapper is already present.')
d('b17','retain first within outer deletion','The locally blackened sign has a surviving loop and long descender, so provisional varphi stays unsure instead of using illegible for a formula symbol. Both p and j have distinct descending stems and lower stars. The right edge preserves the closing parenthesis and a dark low stop. All of this is already inside the global deletion.')
d('b18','mark cancelled actuel doubtful','The local stroke crosses the middle of actuel; the initial a, tall stem and terminal l survive, but not every interior letter can be separated. Retain the word under an unsure mark. Both surviving commas remain outside the local strike; the global cancellation is separate.',True)
d('b19','retain block with the local qualifications above','The two long diagonal strokes and left boundary cancel the lower version. The short horizontal and hatched strokes record additional local revisions within it. This agrees with the original outer deletion. On the final line the word starts with low m humps and has a p descender followed by the h/ismes sequence, supporting morphismes rather than applications. The B/C and actuel qualifications from b15/b18 are carried into the page; no duplicated edge text or extra illegible mathematics is added.',True)
old_v=r'\deleted{\unsure{\mathcal V_{Y,X}}}\inserted{X^*}'
new_v=r'\deleted{\unsure{\mathcal V_{Y,X}|\mathcal V^*_{Y,X}}}\inserted{X^*}'
repls=[(r'\pi_1(X^*)$ iso)',r'\pi_1(X^{\unsure{*|\ell}})$ iso)'),(old_v,new_v),('définies comme étant',r'\unsure{définies|définis} comme étant'),(r'\deleted{actuel}',r'\deleted{\unsure{actuel}}')]
for a,b in repls:t=t.replace(a,b)
for row in r['changes']:
    if row['id']=='r19':row['final']=row['final'].replace(old_v,new_v);row['evidence']+=' Blind crop b15 also allows a star on the old locally cancelled V.'
    if row['id']=='r22':row['final']=row['final'].replace(r'\deleted{actuel}',r'\deleted{\unsure{actuel}}');row['evidence']+=' Blind review leaves the interior letters of actuel uncertain under its local stroke.'
for q in r['doubts']:
    if q['place']=='former argument in C definition':q['reading']=new_v;q['alternatives']='old V with or without a star; former subscript partly obliterated'
r['doubts'] += [
 {'place':'inserted implication, exponent on X','reading':r'\pi_1(X^{\unsure{*|\ell}})','alternatives':'star / ell','confidence':'low','reason':dec['b08']['evidence']},
 {'place':'cancelled lower block, before comme étant','reading':r'\unsure{définies|définis}','alternatives':'définies / définis','confidence':'medium','reason':'Compressed low ending does not distinctly separate an e.'},
 {'place':'lower line Dans le cas','reading':r'\deleted{\unsure{actuel}}','alternatives':'Interior letters hidden by local strike.','confidence':'low','reason':dec['b18']['evidence']}]
r['notes'].append('scan038.N11 Blind review retains the lower block as globally cancelled and preserves its local revisions. It opens a star/ell doubt on the inserted X exponent, admits a star in the earlier crossed C-argument, qualifies the compressed définies/définis ending, and marks locally crossed actuel uncertain. The final word morphismes is supported by its low m onset, descending p and following h/ismes strokes. These are readings from the crops, not repairs to the mathematics.')
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
r['second_changes']=[]
for b in ['b08','b15','b18','b19']:
    v=comp[b]['first']
    for a,z in repls:v=v.replace(a,z)
    r['second_changes'].append({'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'low'})
(W/'pages'/f'{p}.tex').write_text(t)
(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
