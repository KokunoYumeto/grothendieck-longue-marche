"""Single-use scan013 visual adjudications."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1];ch={}
first={x['box']:x['reading'] for x in csv.DictReader((R/'second/149_scan013_first.tsv').open(),delimiter='\t')}
def c(k,e,final=None):
 ch[k]={'personally_inspected':True,'selection':'first' if final is None else 'custom','evidence':e,'changed':'no' if final is None else 'yes'}
 if final is not None:ch[k]['final']=final
c('b01','The dark numeral has a long upper entry and a closed lower curl: 6. The second omitted only the author-page wrapper.')
c('b03','The angular E, dotted i, est, angle above lower bar, n, plus and 2 agree. le/leq are equivalent TeX commands.')
c('b04','Two horizontal relation strokes with a crossing diagonal survive beneath additional cancellation strokes. A 4 would not independently account for the two parallel bars. Retain cancelled not-equal 2. The live variable has two separate low shoulders before the hyphen, unlike the single shoulder of the n in b03; retain m-torsion and the final comma.')
c('b06','The raised sign is looped and retraced. Its returning lower loop favors ell, but its tall stem and cross-like junction also allow t. Add t to the existing uncertainty without asserting an overstrike chronology. The ordinary E and complete barred-K/K index agree.',first['b06'].replace(r'\unsure{\ell}',r'\unsure{\ell|t}'))
c('b07','The joined leading stroke and angular final part permit 14 but remain K-like in outline; retain the existing label uncertainty without using consecutive numbering to resolve it. The first pi is smaller than the E and matches the indexed kernel forms on scans009–012. Retain lowercase pi. The two bounds, all barred-K/K indices, subscript ell, n+2, not-equal 2 and parenthetic ell nb premier agree. Dollars, prose/math wrappers and le/ne abbreviations are syntax.')
c('b08','The middle of sauf/s.f. is a short reduced run with a point-like mark, so separate vowels or abbreviation points remain uncertain. The vowel before nt in donnent/donnant is flattened and not decisively closed/open. Preserve both localized doubts. The other words, accented égalités, its independent underline, parentheses and comma agree; underline/uline are equivalent encodings.')
c('b09','The heading, accent marks, numeral 1 and independent underline are complete. Only underline/uline differs.')
c('b10','The final n has a long low return ending in one down-hook. There is no separate additional s body beyond it. Keep extension. The long curve underneath is an insertion leader, not punctuation or part of the word.')
c('b12','The glyph has two open rounded lobes and no straight stem or prime. It can be the manuscript’s script E or epsilon; a confident choice of alphabet is not established by this isolated shape. Retain the explicit alphabet doubt, with script E preferred.')
c('b13','The medial tall stroke has a crossbar and no d bowl, supporting t. After it an o-like turn is followed by a low u trough and terminal return; there are no two successive high m shoulders. Keep Itou rather than Idem or Item. The lower horizontal of I is its serif, not an underline.')
c('b14','The upper line has Gamma-prime, an open inclusion curve, Gamma and a second open inclusion curve placed low but to its right; that second curve is a relation, not an e/c subscript. Below it the hatched chain retains middle/lower bars of E-like letters, supporting doubtful E-prime subset E rather than Gamma-prime/Gamma-K. Keep its explicit uncertainty and separate cancellation. An additional baseline inclusion survives before the indexed Gamma. The following tall curve and raised tick begin the neighboring l’ of l’image, not a parenthesis and prime belonging to the formula. Retain the first scope, complete bar-Q/Q index and both physical levels.')
c('b15','Both readers give the same raised equality and Gamma with full barred-K/K index. Its curved leader attaches after baseline Gamma. The first also includes the visible ordinary E dans Gamma and qui context. No manuscript reading differs within the insertion.')
c('b16','The rounded letters have the same script-E/epsilon ambiguity as b12. A short upper mark by the first is prime-like, but the preceding larger line’s descenders overlap the small insertion; its independent ownership cannot be established securely. The second possible prime has the same overlap problem. Keep both alphabet and prime alternatives for each occurrence. The words, Gamma, centralisateur, dans and the physical conte- line break agree; the large curve is a leader, not an added parenthesis.')
c('b17','The final Gamma is unindexed. Its following small mark is dark and slightly slanted, but does not have a securely separated descending comma tail. Record point/comma uncertainty. The inserted nue continues conte-; le remains crossed by the old formula index, and all other words and Gamma-prime agree.',first['b17'].replace(r'$\Gamma$.',r'$\Gamma$\unsure{.|,}'))
c('b18','The crossed beginning has a large looped S, a short dotted i, a distinct descending g and an open membership sign before Gamma. It does not have the letter sequence fait que. Keep Si g in Gamma. The group after centralise is the unprimed two-lobed curved form, still script-E/epsilon. The image letter has two short upper arms meeting a descending loop, unlike the flat roof and upright of capital Gamma; keep lowercase gamma. The full index and remaining words agree; cancellation belongs to this large old row, separately from the small replacement.')
tail=r'\unsure{\deleted{$\unsure{\subset|\text{de}|\text{et}}\Gamma_{\mathbb Q}$}|$\unsure{\subset|\text{de}|\text{et}}\Gamma_{\mathbb Q}$}'
c('b19','The horizontal cancellation certainly crosses Gamma centralise Gamma-prime and ends before the final tail. The tail has an open curve and intervening oblique strokes; subset is favored, but de/et-like joined forms are not securely excluded. Those oblique strokes may extend the cancellation, but they do not prove that the whole final Gamma-Q is cancelled. Make both the tail’s reading and its deletion scope explicitly uncertain, retaining the first cancelled interpretation first. The final Gamma and doubled-Q index are visible.',r'\deleted{$\Gamma$ centralise $\Gamma\prime$}'+tail)
# Use the edition apostrophe spelling for prime.
ch['b19']['final']=ch['b19']['final'].replace(r'\Gamma\prime',"\\Gamma'")
(R/'documentation/149_scan013_audit_choices.json').write_text(json.dumps(ch,ensure_ascii=False,indent=2)+'\n')
p=R/'pages/149_scan013.tex';s=p.read_text().replace(r'^{\unsure{\ell}}',r'^{\unsure{\ell|t}}').replace(r"dans $\Gamma$.} \deleted{Si",r"dans $\Gamma$\unsure{.|,}} \deleted{Si")
old=r"$\Gamma$ centralise $\Gamma'\unsure{\subset}\Gamma_{\mathbb Q}$}"
new=r"$\Gamma$ centralise $\Gamma'$}"+tail
assert old in s;s=s.replace(old,new);p.write_text(s)
p=R/'reviews/149_scan013.json';r=json.loads(p.read_text());cs={x['id']:x for x in r['changes']}
def box(b):
 q=next(q for q in r['audit_boxes'] if q['box']==b);return[q[k] for k in ('x0','y0','x1','y1')]
for i,b in [('c04','b06'),('c14','b17'),('c17','b19')]:
 x=cs[i];x.update(evidence=ch[b]['evidence'],crop=f'crops/149_scan013_second_{b}.png',box=box(b),confidence='low')
cs['c04']['final']=cs['c04']['final'].replace(r'\unsure{\ell}',r'\unsure{\ell|t}')
cs['c14']['final']=cs['c14']['final'].replace(r'$\Gamma$.',r'$\Gamma$\unsure{.|,}')
cs['c17']['final']=tail;cs['c17']['against_C']=True;cs['c17']['against_H']=True
for x in r['decisions']:
 if x['id']=='M0982':x.update(reading=r'\unsure{\ell|t}',evidence=ch['b06']['evidence'],confidence='low',crop='crops/149_scan013_second_b06.png',box=box('b06'))
for x in r['doubts']:
 if x['place'].startswith('Opening final E expression'):x.update(reading=r'\unsure{\ell|t}',alternatives=[r'\ell','t'],confidence='low',reason=ch['b06']['evidence'])
 if x['place'].startswith('Second large struck line, relation'):x.update(reading=tail,alternatives=['cancelled inclusion and Gamma-Q','live inclusion and Gamma-Q','de','et'],confidence='low',reason=ch['b19']['evidence'])
r['doubts'].append({'place':'End of small interlinear replacement','reading':r'\unsure{.|,}','alternatives':['.',','],'confidence':'low','reason':ch['b17']['evidence']})
r['notes'].append('Independent audit: all16 differing boxes and61 token spans were inspected. The raised ell now also admits t; the small replacement’s terminal punctuation admits point/comma; and the last old-line tail is explicitly uncertain both in its relation/word reading and in cancellation scope. The crossed opening remains Si g in Gamma, the image letter remains lowercase gamma, the raised/baseline inclusion signs remain distinct, and Itou remains literal. The frozen second reading’s apparent parenthesis/prime after the indexed Gamma is neighboring l’ from l’image.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
