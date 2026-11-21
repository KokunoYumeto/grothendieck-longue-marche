"""Manual blind adjudication of scan041."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan041';r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,decision,evidence,changed=False):dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b02','retain first','The first word has two tall t strokes separated by a low o, then a/l, supporting total; the low transverse belongs to the letter, not a deletion. After the p of pourrait the separated low shoulders support rr, with the final crossed t; pouvait would require a distinct v. The raised de X has its own curved leader.')
d('b03','retain first','The cropped extra pas, parentheses and se récupérer are already present immediately around the first box’s narrower reading. The insertion leader for K(pi,1) terminates between hypothèses and faites.')
d('b04','retain first','The crossed subscript has the same open crossing form as the neighboring capital X; reduced subscript size does not establish a new lowercase variable. Retain the recurring Y,X neighborhood notation and both stars.')
d('b05','retain first','The first diagramme ends with a low return comparable to the second occurrence, with no separate s. Both references, the comma after (7), and i.e without a final stop are visible.')
d('b06','retain first','The numeral 10, both parentheses and the separate period agree; only math delimiters differ.')
d('b07','qualify shorthand','The lower stroke is a returning loop followed by a long tail beneath an upper bar, rather than two plainly straight bars. Barred m is favored, with equals shorthand retained as an alternative. The following si is already on the page.',True)
d('b08','retain first','The F has a curved cap, stem and crossbar, but its printed alphabet remains unresolved. The second reader’s extra n’est is already in the line and does not remove that alphabet doubt.')
d('b09','mark word doubtful','The initial c/o and final crossed t are distinct, but the low central shoulders can be segmented as rr/ec or ur/an. Correct remains the preferred reading; courant is admitted rather than decided from the sentence alone.',True)
d('b10','retain S; qualify exponent and shorthand','The initial letter has a returning lower S stroke and lacks the straight descending stem needed for P. The small superscript has the cap and short downward return of the author’s 2, also 7-like; retain 2/7 uncertainty explicitly in the transcription. The low abbreviated sign can be equals or a very compressed barred m. The comma and following opening parenthesis are separate.',True)
d('b16','retain first','Both readers give (23) and a separate following point. Math delimiters alone differ.')
d('b18','retain first','The initial descender loops back into the short e of je. The next word has a low n/o onset, then a tall crossed t and final e return. It lacks a separate dotted i and the v onset needed for y voit. Retain je note.')
d('b19','retain first','The main word telles is crossed locally, and the raised sur des topos leader ends after gerbes before the one comma. At the right edge recolle- has two tall l strokes followed by a small low e return before the hyphen. The X at the upper edge belongs to the preceding line and is already transcribed.')
d('b21','retain first with existing insertion wrapper','This close crop shows the same K(pi,1) and the curved leader ending before faites as b03. Its insertion wrapper is already present in the page; the isolated first-box reading did not repeat it.')
t=t.replace("fondée, $=$ si",r'fondée, $\unsure{\overline m|=}$ si').replace("d'homotopie correct.",r"d'homotopie \unsure{correct|courant}.").replace(r'$S^2$, (qui est en $=$ temps',r'$S^{\unsure{2|7}}$, (qui est en $\unsure{=|\overline m}$ temps')
for row in r['changes']:
    if row['id']=='r06':row['final']=r'$\unsure{\overline m|=}$';row['diff_c']=True;row['confidence']='low';row['evidence']+=' Blind review: '+dec['b07']['evidence']
    if row['id']=='r07':row['final']=r'$\unsure{=|\overline m}$';row['confidence']='low';row['evidence']+=' Blind review: the lower stroke has a short returning onset, leaving equals / barred-m unresolved.'
for q in r['doubts']:
    if q['place']=='Main line 12, superscript on S':q['reading']=r'S^{\unsure{2|7}}';q['reason']='The cap and short downward return are 2-like but also permit 7; the retained doubt is now explicit in the page after blind review. P is excluded by the returning lower S stroke.'
r['doubts'] += [
 {'place':'Main line 7, after fondée','reading':r'$\unsure{\overline m|=}$','alternatives':'barred m / equals shorthand','confidence':'low','reason':dec['b07']['evidence']},
 {'place':'Main line 9, last word','reading':r'\unsure{correct|courant}','alternatives':'correct / courant','confidence':'medium','reason':dec['b09']['evidence']},
 {'place':'Main line 12, en ... temps','reading':r'$\unsure{=|\overline m}$','alternatives':'equals shorthand / barred m','confidence':'low','reason':'The lower short stroke has a returning onset but no distinct full m.'}]
r['notes'].append('scan041.N8 Blind review keeps total, pourrait, singular diagramme, je note and the final recolle- from their visible strokes. It qualifies correct/courant and the two short forms, and makes the existing 2/7 superscript uncertainty explicit in the page. The preferred S² reading still underlies the local H² check; that check does not itself establish the numeral’s ink. The alternative P¹ is rejected because the lower returning stroke belongs to S.')
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
finals={'b07':r'$\unsure{\overline m|=}$','b09':r'\unsure{correct|courant}.','b10':r'$S^{\unsure{2|7}}$, (qui est en $\unsure{=|\overline m}$ temps'}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'low'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
