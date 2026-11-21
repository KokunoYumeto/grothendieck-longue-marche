"""Manual adjudication following inspection of all differing blind crops."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan043';r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,decision,evidence,changed=False):dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b02','retain first','The authorial 9 is separate from the line. The leader attaches de (23) after S², before the comma and on. Math delimiters and page-number wrapper differ only.')
d('b04','retain first','The reduced à has a lower angled body and separate oblique accent; the apostrophe shape is the only token difference.')
d('b05','retain first','The long upper and lower horizontals and doubled oblique support double-struck Z. The interior crossing could suggest A, but no independently separable old A or cancellation layer is secure, so no speculative deleted A is added. The crossed sur remains unsure and the final A is plain.')
d('b06','mark reduced sign doubtful','The sign after donc has only a tiny lower body and a detached upper mark. The lower body is too reduced to distinguish accented à from two punctuation points with confidence. Retain à first and colon as an alternative.',True)
d('b07','retain first','The Z has one thick diagonal whose possible doubled trace cannot be separated; the existing double-struck/plain doubt remains. Both A letters, parentheses, one-wave equivalence and comma agree.')
d('b08','retain first','A has a clear final triangular body and right leg over the old diagonal/horizontal Z remnants. Keep the old Z alphabet doubtful within deletion and the replacement A explicit. The second reader’s wider unsure wrapper does not require removing the visible replacement.')
d('b09','retain first','The apparent dark stroke in des follows the loop and retracing of its d. There is no independent cancellation extending across the whole word and no second live les. Retain des live.')
d('b10','retain uncertain words; qualify terminal comma','The cancelled words have recognizable tall l/t and inductives strokes but low bodies merge with the cancellation, so their doubt stays. A short dark oblique descends at the right end beyond the final letter returns; a cancelled comma is possible, though its meeting with the strike prevents certainty. Record it as unsure. The inserted capital Lim has a distinct arrowhead below it.',True)
d('b11','retain first','Both readings preserve des/de uncertainty and the same words; the curly versus straight apostrophe is typographical.')
d('b12','retain first','The compressed onset has an isolated low mark and joined returns; avec remains favored, but the crop does not resolve the existing ou alternative. Do not remove the doubt from the independent reader’s certainty alone.')
d('b13','mark reduced sign doubtful','The first sign is reduced to a short slanted lower stroke and a detached upper mark, comparable to b06. Keep à/colon unresolved; la and underlined van Kampen, including its final comma, are clear.',True)
d('b14','retain underline','The lower stroke has a single downward return at its right end, without the second converging flank of an arrowhead. It differs from the true arrow below the inserted Lim in b10. Retain capital underlined Lim.')
d('b15','retain first','The two tiny points below the end of Topos are far below the writing baseline and have no stable punctuation placement; they are not added as a colon. The final short word has an e onset and compressed s before the terminal t return, supporting est. Both capital T forms and the ordinary quotation strokes remain.')
d('b16','retain underline','The right end of the lower stroke turns down once; it does not form two converging arrowhead strokes. Retain the underline, consistently with b14 and in contrast with the clear arrow in b10.')
t=t.replace('donc à un élément',r'donc \unsure{à|:} un élément').replace(r'\deleted{\unsure{limites inductives}}',r'\deleted{\unsure{limites inductives}\unsure{,}}').replace(r'théorème à la \uline',r'théorème \unsure{à|:} la \uline')
for row in r['changes']:
    if row['id']=='r05':row['final']=r'\unsure{à|:}';row['confidence']='low';row['evidence']+=' Blind review: '+dec['b06']['evidence']
    if row['id']=='r10':row['final']=r'\deleted{\unsure{limites inductives}\unsure{,}}';row['diff_c']=True;row['diff_h']=True;row['confidence']='low';row['evidence']+=' Blind review: '+dec['b10']['evidence']
    if row['id']=='r14':row['final']=r'\unsure{à|:} la van';row['confidence']='low';row['evidence']+=' Blind review: '+dec['b13']['evidence']
r['doubts'] += [
 {'place':'after donc, before un élément','reading':r'\unsure{à|:}','alternatives':'à / colon','confidence':'low','reason':dec['b06']['evidence']},
 {'place':'right end of cancelled limites inductives','reading':r'\unsure{,}','alternatives':'comma / end of cancellation stroke','confidence':'low','reason':dec['b10']['evidence']},
 {'place':'before la van Kampen','reading':r'\unsure{à|:}','alternatives':'à / colon','confidence':'low','reason':dec['b13']['evidence']}]
r['notes'].append('scan043.N11 Blind review retains the two lower Lim underlines: their single downward terminal hooks differ from the explicit arrowhead beneath the first inserted Lim. It marks two very reduced à/colon forms and a possible comma under the end of the cancelled phrase. The tiny low points after Topos are not promoted to punctuation. The dense Z does not establish a separate underlying A layer.')
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
finals={'b06':r'donc \unsure{à|:} un élément de','b10':comp['b10']['first'].replace(r'\deleted{\unsure{limites inductives}}',r'\deleted{\unsure{limites inductives}\unsure{,}}'),'b13':r'\unsure{à|:} la \uline{van Kampen},'}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'low'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
