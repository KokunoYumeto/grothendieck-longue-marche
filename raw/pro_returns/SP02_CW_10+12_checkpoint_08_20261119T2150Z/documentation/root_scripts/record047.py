import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-02',10,47);ch=r.change
r.edit(r'\handwritten{\unsure{(}}',r'\handwritten{(}')
r.edit(r'\mathbb{S}',r'\unsure{\mathbb{S}|S}')
r.edit(r'engendré par les $x_i$.}',r'engendré par les $x_i$\unsure{,|.}}')
def pic(text,path):return r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=(n.base)]\node (n) at (0,0) {'+text+r'};\draw '+path+r';\end{tikzpicture}'
r.edit(r'\handwritten{sur $S$}',r'\handwritten{'+pic('sur $S$',r'(-.65,.2)--(-.75,-.2)--(.55,-.2)--(.55,-.75)--(.9,.2)')+'}',3)
r.edit(r'\handwritten{, grâce au fait que $\mathcal{A}$ est plat !)}',r'\handwritten{, grâce au '+pic(r'fait que $\mathcal{A}$ est plat !)',r'(-2.05,-.65)--(-2.1,-.25)--(2.1,-.25) .. controls (2.3,-.25) and (2.3,-.1) .. (2.3,.1)')+'}')
r.edit(r'\handwritten{$\mathcal{F}$}',r'\handwritten{'+pic(r'$\mathcal{F}$',r'(.35,.2) .. controls (.25,-.15) and (-.15,-.3) .. (.02,-.6)')+'}')
r.edit(r'\handwritten{par exemple}',r'\handwritten{'+pic('par exemple',r'(-1.3,.5) .. controls (-1.3,.15) and (-1.75,-.2) .. (-1.45,-.3) .. controls (-1.05,-.45) and (1.4,-.45) .. (1.5,-.15) .. controls (1.7,.2) and (.8,.15) .. (-1.3,.15)')+'}')
ch('manuscript number','15','omitted','15','Tall initial 1 and open two-part 5 in upper left.','number','omission')
ch('opening A',r'\unsure{\mathcal{A}|a}',r'\mathcal{A}',r'\unsure{\mathcal{A}|a}','Low loop with upper return and right foot remains compatible with both alphabets.','top','misread symbol or index','medium')
ch('deleted G e',r'\deleted{\unsure{G e}}t',r'\struck{G} et',r'\deleted{\unsure{G e}}t','The cancellation covers a looped first character and the e region; the final t is visibly outside it.','delGe; top','deletion state (struck given live or live given struck)','low')
ch('amended sont',r'\deleted{son}\handwritten{soi}t',r'\struck{soit}',r'\deleted{son}\handwritten{soi}t','Typed son is crossed/retraced and handwritten soi overwrites it; the final typed t is live.','top','deletion state (struck given live or live given struck)')
ch('final s of plats',r'plat\deleted{s}','plats',r'plat\deleted{s}','A thick diagonal cancellation crosses the final s.','top','deletion state (struck given live or live given struck)')
ch('first E subscript',r'\unsure{o|0}','0',r'\unsure{o|0}','Small low round mark, shorter than full-height digits elsewhere; shape alone does not entirely settle o/0.','first','misread symbol or index','medium')
for locus in ['E in factorization source','E in canonical injection source','rho source and both E indices','rho before définit','E after opération de G','E after opération induite','E before est stable','E inside W']:
 ch(locus+' subscript','o','0','o','Small rounded low letter, consistently o-shaped; no full-height oval digit.','W' if 'W' in locus else 'first','misread symbol or index','medium')
ch('injectivity addition','grâce au',r'\ill{} on','grâce au','Connected g-r-â-c-e with circumflex and a-u at far right; the following line begins fait que.','first','readable ink left as \\ill{}','high',False,True,True)
ch('injectif placement','typed injectif with handwritten opening parenthesis','whole incise added','typed injectif with handwritten opening parenthesis','The letters injectif are typewriter impressions on the main line; the parenthesis and following explanation are handwritten.','first','insertion or placement')
ch('parentheses around induced-operation clause',r'(,\unsure{(} ... )',', ...',r'(,( ... )','A strong left curve precedes the comma and a second pale continuous curve follows it; final closing parenthesis is dark and clear.','secondparen; first','omission','medium',True,True)
for place,crop in [('opération induite','first'),('stable','first'),('entire lemma 11.8','lemma'),('entire proposition 11.9','proposition')]:
 ch('underline '+place,'underlined','italic or heading bold only','underlined','Pen lines run beneath the indicated text; both statements have a line beneath each typed line.',crop,'other')
ch('lemma O base S',r'\mathbb{S}','S',r'\unsure{\mathbb{S}|S}','The subscript S has heavy inner patches; separate alphabet strokes cannot be distinguished from overprinting.','lemmaS','misread symbol or index','medium',True,True)
ch('cancelled plat A',r'\unsure{plat} \mathcal{A}',r'\ill{}',r'\unsure{plat} \mathcal{A}','p stem and bowl and subsequent tall/short letter remnants remain under x overstrikes; A loop at right is clearer, plat remains doubtful.','platA','readable ink left as \\ill{}','low',False,True,True)
ch('cancelled et contient x.','et contient x.','omitted','et contient x.','The typed e-t, contient and x with dot remain visible beneath the slanting cancellation and above-line replacement.','lemma','omission')
ch('lemma underline terminal flourish','TikZ flourish','omitted','TikZ flourish','Short dark blue looped pen stroke continues the right end of the last underline.','lemma','drawing or diagram')
ch('deleted proof-opening punctuation','.', '.',r'\unsure{,|.}','The small mark after x_i tapers down and left, suggesting comma; its outline is too soft to exclude a damaged dot.','deleted-period','other','medium',True,True)
ch('corrected last x index in rho formula','i','j','i','Dotted short upright with rightward foot, unlike nearby j with long descending hook.','index; proof','misread symbol or index','high',False,True,True,True)
ch('cancelled l after nous',r'\unsure{l}','omitted',r'\unsure{l}','Dark vertical with small horizontal foot and additional overstrike remains between nous and le; underlying l is not fully separable.','deletedl','omission','low')
ch('cancelled reference word',r'\deleted{l\text{’}exposé}',r'\ill{}',r'\deleted{l\text{’}exposé}','Initial l, p descender and terminal s-é survive the central cancellation, with earlier rounded letter remnants.','cancel-exp','readable ink left as \\ill{}','medium',False,True,True)
ch('XXV bars','bar above and below','plain XXV','bar above and below','Separate horizontal strokes extend over and under all three Roman letters.','proposition','omission')
ch('module replacement',r'\deleted{module} Module',r'\struck{Module}',r'\deleted{module} Module','Small typed lowercase word is cancelled; large handwritten capital M and remaining letters are live above it.','proposition','deletion state (struck given live or live given struck)')
for i,(place,shape,crop) in enumerate([('first sur S','angular lower bracket and diagonal insertion stroke','top-surS'),('lemma sur S','angular lower bracket and diagonal insertion stroke','lemma'),('proposition sur S','angular lower bracket and diagonal insertion stroke','proposition'),('fait que addition','long lower bracket with descending left anchor','first'),('inserted F','curved diagonal insertion stroke','lemma'),('par exemple','rounded enclosure with upper-left joining stroke','proposition')],34):
 ch(place+' marks','omitted','omitted','TikZ '+shape,'Visible '+shape+'.',crop,'drawing or diagram','high',True,True)
 r.r['inventory_extra'].append(dict(scan='10:047',sheet_kind='typescript',hand='his hand',element=f'047-{i:02d}',kind='drawing',position=place,first_words_or_objects=shape,transcribed='yes'))
for p,rd,alt,co in [('first A',r'\mathcal{A}','a','medium'),('cancelled opening group','G e','','low'),('first E index','o','0','medium'),('lemma base S',r'\mathbb{S}','S','medium'),('cancelled plat','plat','','low'),('deleted proof punctuation',',','.','medium'),('cancelled l','l','','low')]:r.doubt(p,rd,alt,co)
r.r['crops']=json.loads(Path('work/crops047.json').read_text())
r.r['inspection_note']='Root read whole then both halves and every line, all formula signs and indices, every deletion and insertion. Enlargements include full mathematical paragraphs and each doubt. The repeated first subscript remains o-like; final corrected x index i is visibly distinct from adjacent typed j. Agreed Soient and unmatched relation) retained. No mathematics checked.'
r.notation('corrected handwritten i',r'i','10/047 rho(x_i) formula: separate dot, short upright and right foot; nearby j has long descender')
r.save('work/record047.json')
