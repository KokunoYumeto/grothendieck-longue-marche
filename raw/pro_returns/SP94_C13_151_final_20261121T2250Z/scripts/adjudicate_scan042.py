"""Root adjudication after viewing every differing blind crop."""
from pathlib import Path
import csv,json
W=Path(__file__).resolve().parents[1];p='151_scan042';r=json.loads((W/'reports'/f'{p}.json').read_text());t=(W/'pages'/f'{p}.tex').read_text();dec={}
def d(b,decision,evidence,changed=False):dec[b]={'decision':decision,'changed':'yes' if changed else 'no','evidence':evidence}
d('b01','retain first','The page opens with the continuation ment, then two closing strokes and évidente ending in nte. There is no initial moins or pair of opening quotes.')
d('b02','retain first','The raised words have the d loop, two n shoulders and accented ending of donnée, not domine. The old qu-like fragment remains doubtful; the following live d of d\'une is not absorbed into a hypothetical quand.')
d('b03','retain first','The long lower loop identifies scripted G; extra braces are equivalent syntax, and sur belongs to the following baseline already transcribed.')
d('b04','retain first with ending doubt','The comma and lower body plus accent of à remain. The final short return after gerbe is compressed enough that singular/plural cannot be certified; keep gerbes first, mark gerbe as alternative.',True)
d('b05','retain first','The raised crossing beside X is part of the subscript X-star; no independent struck word is visible. The scripted G has its full lower loop.')
d('b06','retain first','Both open-bowled scripted symbols, Y-comma-X indices and terminal comma agree. Only optional macro braces differ.')
d('b07','retain first','The local strike crosses the lower iso. while leaving enough of i, curved s and o plus its point; the upper équiv. and its q descender are separate. No new doubt is required.')
d('b08','broaden unresolved ending','The reco beginning and two tall l stems survive; the low end is merged with the horizontal strike. Neither m and its stop nor e/r can be separately certified, so retain the first abbreviation and add the blind alternatives.',True)
d('b09','retain first','The full display shows crossed, multi-directional superscript marks in the V positions. The smaller mark beside X belongs to the same star notation. The two restriction bars, simeq and final dot are clear; neither plus nor times creates a distinct local notation.')
d('b10','retain first','The cap projects left of the first leg and the right leg curves at its foot, matching the lowercase pi written after extension on this page. This is the generic pi in K(pi,1); capital Pi elsewhere has longer straight legs.')
d('b11','retain first','The final n ends with one low return, without a separate s body. The underline is independent of the letters. Singular extension remains.')
d('b12','add doubtful punctuation','The cancelled relation must remain symbolic and doubtful, not an illegible-word placeholder. A small dark oblique mark below/right of S-squared could be a comma; its separation from the cancellation is uncertain, so it is marked doubtful.',True)
d('b13','retain first','The first live d has an isolated apostrophe, not a following baseline e. After the struck une ext there is a d loop, low eu sequence and terminal crossed knot supporting deux. The long final return of extensions is retained; no independent extra de is inserted.')
d('b14','retain first','Both Pi forms have a broad cap and tall legs. The small dense superscript by X repeats the crossed star family, rather than a separate plus notation.')
d('b15','retain first','The low mark after déduisent has an angular loop and tail, less regular than the clear commas elsewhere; the existing comma doubt is retained.')
d('b17','retain first','An opening parenthesis precedes a low lowercase cette. The disputed word has a tall h after low marc-like strokes and a terminal e; vaut/valide do not account for that ascender.')
d('b18','retain symbols; reopen noun','The prime after X has one hooked stroke, unlike the neighbouring crossed V-star, and Pi_2 has a broad straight cap. The quoted noun has compressed low middle strokes and no clearly separable accent; pièces is plausible but pierres/pavés cannot be excluded by these bodies alone.',True)
d('b19','retain first','Both Pi signs repeat the tall broad-capped family, and the lower superscript is a dense crossed star. D has exactly one rightward and one downward arrow, each with one shaft and head; spacing options are nontextual.')
repl=[('de gerbes $\\mathcal G_{X^*}$',r'de \unsure{gerbes|gerbe} $\mathcal G_{X^*}$'),(r'\unsure{recollem.}',r'\unsure{recollem.|recolle|recoller}'),(r'$X\deleted{{}\unsure{\simeq} S^2}$ revient',r'$X\deleted{{}\unsure{\simeq} S^2}$\unsure{,} revient'),("``pièces''",r"``\unsure{pièces|pierres|pavés}''")]
for a,b in repl:
 assert a in t,a;t=t.replace(a,b)
for row in r['changes']:
 if row['id']=='r04c':row['final']=r'de \unsure{gerbes|gerbe}';row['evidence']+=' Blind audit: the noun ending is compressed; singular is now an explicit alternative.';row['confidence']='medium'
 if row['id']=='r08':row['final']=r'\deleted{\unsure{recollem.|recolle|recoller}}';row['evidence']+=' Blind audit also admits recolle/recoller at the obscured end.'
 if row['id']=='r18a':row['final']=r"``\unsure{pièces|pierres|pavés}''";row['confidence']='medium';row['evidence']+=' Blind audit reopens the noun itself: the middle strokes are reduced, and an independent accent is not secure.'
with (W/'second'/f'{p}_comparison.tsv').open() as f:comp={q['box']:q for q in csv.DictReader(f,delimiter='\t')}
with (W/'second'/f'{p}_boxes.tsv').open() as f:boxes={q['box']:[int(q[k]) for k in ('x0','y0','x1','y1')] for q in csv.DictReader(f,delimiter='\t')}
r['changes'].append({'id':'r12c','place':'after cancelled S-squared','c':'no comma','h':'no comma','final':r'\unsure{,}','evidence':dec['b12']['evidence'],'confidence':'low','kind':'omission','error_category':3,'diff_c':True,'diff_h':True,'marked_h':False,'crop':f'crops/second_{p}_b12.jpg','box':boxes['b12'],'consequential':''})
for q in r['doubts']:
 if q['place']=='struck word before gerbes':q['reading']=r'\unsure{recollem.|recolle|recoller}';q['alternatives']='recolle or recoller; terminal letters and stop hidden by strike'
r['doubts'] += [{'place':'first de gerbes','reading':'gerbes','alternatives':'gerbe','confidence':'medium','reason':dec['b04']['evidence']},{'place':'after cancelled S-squared','reading':r'\unsure{,}','alternatives':'incidental short mark associated with deletion','confidence':'low','reason':dec['b12']['evidence']},{'place':'quoted noun in last paragraph','reading':'pièces','alternatives':'pierres; pavés','confidence':'medium','reason':dec['b18']['evidence']}]
r['notes'].append('scan042.N11: The blind audit reopens the final quoted noun, the first gerbe(s) ending and the struck recollem. ending. A small dark mark below/right of cancelled S² is retained as a doubtful comma. The prime in the last list remains clear; the second reader\'s star does not account for its single hooked stroke.')
finals={'b04':comp['b04']['first'].replace('de gerbes',r'de \unsure{gerbes|gerbe}'),'b08':comp['b08']['first'].replace(r'\unsure{recollem.}',r'\unsure{recollem.|recolle|recoller}'),'b12':comp['b12']['first'].replace('$ revient',r'$\unsure{,} revient'),'b18':comp['b18']['first'].replace("``pièces''",r"``\unsure{pièces|pierres|pavés}''")}
r['second_changes']=[{'box_id':b,'place':'blind box '+b,'first':comp[b]['first'],'second':comp[b]['second'],'final':v,'evidence':dec[b]['evidence'],'crop':f'crops/second_{p}_{b}.jpg','box':boxes[b],'confidence':'low' if b in ('b08','b12') else 'medium'} for b,v in finals.items()]
(W/'pages'/f'{p}.tex').write_text(t);(W/'reports'/f'{p}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');(W/'audit'/f'{p}_adjudication.json').write_text(json.dumps(dec,ensure_ascii=False,indent=2)+'\n')
