"""Root adjudication of all nineteen blind token disagreements."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan049';r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,e,changed=False):dec[b]={'decision':'retain first with local doubt' if changed else 'retain first','changed':'yes' if changed else 'no','evidence':e}
d('b01','The joined upright and curved two form the authorial 12; the wrapper records its role without changing the digits.')
d('b02','The whole map has the source r prime, target r and one heavily retraced single arrow; all tokens agree apart from math delimiters.')
d('b03','The whole coordinate formula agrees. The underbrace covers only alpha*(i*), with two vertical equality strokes below and unaccented def to their right, then i* composed with alpha. The alternative array/substack syntax is representational.')
d('b05','Both Delta subscripts are starred, the relation is a subset, and the final separate dot is dark. The only difference is delimiters.')
d('b06','The final dark round blob is separated by a tiny pale gap from the lighter end of the underline. It can be a stop but could be an endpoint dab. Preserve the point with an explicit doubt rather than silently remove it.',True)
d('b07','The initial g has a long looped descender; the middle tall l and successive contracted s/e/n/t strokes support generalisent. The final small first body with low following return supports au, not a distinct e-n sequence. This agrees with the next-line cas.')
d('b08','The first word begins with an open c followed by a small joined a oval and a terminal return; the middle word has a small o body and a long u return with a detached accent. Cas ou on is supported; en a en does not account for the first c and the middle o/u structure.')
d('b09','The raised phrase and its leader ending before I agree. Curly versus straight apostrophe is only encoding.')
d('b10','The raised glyph has a closed upper curl and broad lower C bowl. Calligraphic C remains preferred with the plain-C alternative, consistent with b12. Its slanting leader and separate comma are retained.')
d('b11','A capital X with crossed diagonals stands on the left; the arrow has a left bar and right head; X_i stands on the right. Mapsto length and delimiters change no reading. The literal X is not corrected to the expected index variable.')
d('b12','The same curled category symbol as b10 has a single-shaft arrow to categorie. Preserve the same alphabet doubt at both occurrences.')
d('b13','Three separate compact points are followed by a fourth elongated dark mark with a lobed body. That last mark can be a long point or short dash. Keep the point preferred, now with dash explicit; do not reduce the four physical marks to a three-point ellipsis alone.',True)
d('b16','The cancellation crosses the trial i≤j and overlaps the terminal parallel strokes. Equality/iff remains explicitly doubtful. Added spacing is not a reading difference.')
d('b17','The two-headed double-shaft equivalence, unaccented def above it, both literal ≤ signs and terminal dot agree. Only math delimiters differ.')
d('b18','The insertion leader ends before I and is independent of the word. The crossed final t joins a low curved return which favors a final e, but the e body is not separately closed. Retain croissante with croissant as an explicit alternative; no parenthesis is added.',True)
d('b19','After the small ce body is a separate contracted s/o/i run with a tall final t and its return. Retain ce soit, not c est. The long lower stroke under plongement is continuous with its g descender; it is not an underline.')
d('b20','Both stops of i.e., the apostrophe in l-on and ait agree; the apostrophe encoding differs only.')
d('b21','The full formula has literal ≤ on both sides and a two-shaft right implication between them, with no terminal dot. Spacing and delimiters differ only.')
d('b22','The reference visibly contains 1, one prime, b, two closing parentheses and a terminal dot. The prime command and delimiters are equivalent encoding.')
t=t.replace(r'\uline{Remarques}.',r'\uline{Remarques}\unsure{.}').replace('\n....\n','\n...\\unsure{.|-}\n').replace(r"\inserted{l'appl. croissante}",r"\inserted{l'appl. \unsure{croissante|croissant}}")
for b,place,reading,alt in [('b06','heading Remarques, end of underline','.','underline endpoint'),('b13','after inclusions, fourth continuation mark','.','-'),('b18','inserted l-appl. croissante','croissante','croissant')]:
 r['doubts'].append({'place':place,'reading':reading,'alternatives':alt,'confidence':'medium','reason':dec[b]['evidence']})
for q in r['changes']:
 if q['id']=='r16':q['evidence']='The word ends with a crossed t and a low return favoring e, now explicitly doubtful. No separate closing curved mark follows it. The long line beneath the phrase is an insertion leader with a small terminal turn, not a parenthesis.'
r['notes'].append('scan049.N10. Blind adjudication retains the literal X indexing slip, vertical definition annotation, two script-C preferences and cancelled relation doubt. It now marks three small ambiguities: the dark point at the underline endpoint after Remarques, the fourth elongated continuation mark (point or dash), and the final e of inserted croissante. These qualify the certainty of N7-N8 without altering the preferred lexical readings. Ce soit and the wrapped au cas remain supported by their strokes.')
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
finals={'b06':r'\uline{Remarques}\unsure{.}','b13':r'...\unsure{.|-}','b18':r"que \inserted{l'appl. \unsure{croissante|croissant}} $I\longrightarrow\text{ens. des parties}$"}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'medium'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
