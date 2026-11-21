"""Manual root adjudication of all differing blind crops."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan044';r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,decision,evidence,changed=False):dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b01','retain first','The elevated paired strokes are double quotation marks; the first TSV already uses the required backtick/apostrophe convention.')
d('b02','reopen noun, prefer pierres','Two angular low shoulders after the initial pi/e strokes resemble rr rather than one open c; the initial dot belongs to i, with no separate grave accent securely visible. The local outline favors pierres, while pièces remains possible. Both opening and closing quote pairs are visible.',True)
d('b03','retain existing doubt order','The right leg bends outward and the cap projects to the left as in the other generic K(pi,1) form; lowercase remains first, with capital already an explicit alternative.')
d('b04','retain wording with doubt','The lower cancellation exposes c, looped l, d and final tall t, favoring cela devrait over cet abaissement. Several low letter bodies coincide with the strike, so the whole cancelled wording is now explicitly unsure. The raised tels stays live.',True)
d('b06','retain existing alternatives','The clear l is followed by densely retraced low strokes; neither the u/r sequence nor its absence is secure. Both les and leurs are already represented.')
d('b07','retain first','After tubulaires a descending p, low a/r/m sequence and isolated i dot support parmi. The word is longer than pour and lacks its final r-only ending. The insertion is live throughout.')
d('b08','retain first','The disputed word has initial reduced a and two s strokes, o loop, c, dotted i and e/r ending. Neither précise nor espaces accounts for that sequence. Grâce has a descender and accent, followed by reduced à and leurs.')
d('b10','retain first','The end of souvent rises to a distinct t loop; sommes would not account for this ascender. The compressed preceding ou/v/en strokes and the following à are retained.')
d('b14','retain first','Both pairs of raised quote strokes surround d\'intégration. Plain double-quote characters are equivalent reading but not the required transcription convention.')
d('b15','retain first','The word has the b and tall l stems of nébuleusement, followed by the reduced euse/ment run. There is no separate word cet; the final strokes belong to the ending of the long adverb.')
d('b16','retain first','The a loop is followed by a low u ending with a return; no separate crossing or x body follows it. Au remains.')
d('b17','retain first','The detached curved final mark is the s of relatives, continuing the preceding reduced e form; it is not a new comma after the word. The opening parenthesis remains.')
d('b19','retain words, correct final punctuation','Justiciable ends with e and one return, not a separate s. The half sign is followed by a distinct short hyphen at the line end; standart ends in crossed t. At the bottom the mark after suite is a short horizontal dash, not a round full stop.',True)
d('b20','adopt dash','The ending after suite is a dark, visibly elongated horizontal stroke with a slightly slanted tail; it is distinct from the round point after standart. Adopt a dash, with no hyphen between là and dessus.',True)
d('b21','retain first','The thin pale digits read 43, already retained as other-hand marginal foliation. The added wrapper in the second reading does not change the numeral.')
t=t.replace("``pièces''",r"``\unsure{pierres|pièces}''",1).replace(r'\deleted{cela devrait}',r'\deleted{\unsure{cela devrait}}').replace('par la suite.','par la suite -')
for q in r['changes']:
 if q['id']=='r05':q['final']=r'\deleted{\unsure{cela devrait}}';q['confidence']='medium';q['evidence']+=' Blind audit: low bodies under the strike are not all distinct, so the wording remains preferred but explicitly doubtful.'
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
for rid,b,place,c,h,final,kind,cat,conf in [('r32','b02','first quoted construction noun','pièces','pièces',r'\unsure{pierres|pièces}','misread word',2,'medium'),('r33','b20','final punctuation after suite','.','.', '-', 'other',10,'high')]:
 r['changes'].append({'id':rid,'place':place,'c':c,'h':h,'final':final,'evidence':dec[b]['evidence'],'confidence':conf,'kind':kind,'error_category':cat,'diff_c':True,'diff_h':True,'marked_h':False,'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'consequential':''})
r['doubts'] += [{'place':'first quoted noun','reading':'pierres','alternatives':'pièces','confidence':'medium','reason':dec['b02']['evidence']},{'place':'cancelled phrase before tels','reading':'cela devrait','alternatives':'low internal letter bodies under strike','confidence':'medium','reason':dec['b04']['evidence']}]
r['notes'].append('scan044.N11: Blind adjudication prefers pierres with pièces retained as alternative at the first quoted noun, and reopens the cancelled cela devrait without inventing an alternative from the crossing. The final punctuation is a dash, not the point both witnesses supplied. The separate hyphen after the half sign and the detached s of relatives remain. This note supersedes the former count of three uncertainties in N5.')
finals={'b02':r"``\unsure{pierres|pièces}''",'b04':r'\deleted{\unsure{cela devrait}}\inserted{tels}','b19':comp['b19']['first']+' [bottom context: par la suite -]','b20':'faudra revenir là dessus par la suite -'}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'medium' if b in ('b02','b04') else 'high'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
