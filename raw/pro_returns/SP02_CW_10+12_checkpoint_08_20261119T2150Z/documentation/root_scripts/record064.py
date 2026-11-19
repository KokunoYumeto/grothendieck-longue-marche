import sys,json
from pathlib import Path
sys.path.insert(0,'SP02_CW_10+12/scripts')
from root_record import Record
r=Record('B10-04',10,64);ch=r.change
relation=r'\mathrel{\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.05cm]\draw[thin] (0,-.13)--(0,.15);\draw[thin] (0,0)--(.52,0).. controls (.57,0) and (.58,.03)..(.59,.08);\end{tikzpicture}}'
r.edit(r'\mathrel{\vert\! -\! -}',relation)
r.edit('en termes de',r'en \unsure{\deleted{e}t|\deleted{o}t|\deleted{t}e}ermes de')
r.edit(r'\unsure{m|n}',r'n')
r.edit(r'\unsure{\deleted{d}r|\deleted{r}d|r}',r'\unsure{\deleted{d}r|\deleted{r}d}')
r.edit("comme l'ensemble des éléments non",r"comme l'ensemble des éléme\unsure{nts} non")
hook=r'\begin{tikzpicture}[x=1cm,y=1cm,baseline=-.1cm]\draw[thin] (0,.12).. controls (.05,-.08) and (-.1,-.1)..(-.5,-.12)--(-1.6,-.12).. controls (-1.85,-.12) and (-1.95,-.28)..(-1.93,-.5);\end{tikzpicture}'
r.edit(r'\inserted{\handwritten{$K^{\mathrm{eff}}\subset K$}}',r'\inserted{\handwritten{$K^{\mathrm{eff}}\subset K$'+hook+'}}')
r.edit(r'\inserted{$\operatorname{End}(M_i)$,}',r'\inserted{$\operatorname{End}(M_i)$,'+hook+'}')
old=r'''\[
\begin{aligned}
\det_M f&=\deleted{\det}N_{Z/k}(\operatorname{Nr}_{K/Z}(f))^{n'/d}\\
\operatorname{Tr}_M f&=\operatorname{Tr}_{Z/k}(\operatorname{Trr}_{K/Z}(f))\ \frac{n'}{d}\\
\operatorname{Pol}_M(f,t)&=N_{Z/k}(\operatorname{Polr}_{K/Z}(f,t))^{n'/d}\quad\inserted{(n'/d=n/dr)}\ .
\end{aligned}
\]'''
new=r'''\diagram{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (0,0) {$\det_M f=\deleted{\det}N_{Z/k}(\operatorname{Nr}_{K/Z}(f))^{n'/d}$};
\node[anchor=west] at (0,-.75) {$\operatorname{Tr}_M f=\operatorname{Tr}_{Z/k}(\operatorname{Trr}_{K/Z}(f))\ \frac{n'}{d}$};
\node[anchor=west] at (0,-1.5) {$\operatorname{Pol}_M(f,t)=N_{Z/k}(\operatorname{Polr}_{K/Z}(f,t))^{n'/d}$};
\node[anchor=west] at (6.2,0) {$\inserted{(n'/d=n/dr)}$};
\draw[thin] (6.05,-.03).. controls (5.45,-.8) and (7.25,-.9)..(7.45,-1.5);
\draw[thin] (7.15,-1.56)--(7.45,-1.5)--(7.38,-1.24);
\draw[thin] (6.12,-1.46)--(6.32,-1.38);\fill (6.22,-1.45) circle (.035);
\node at (8.65,-1.52) {$.$};
\end{tikzpicture}}'''
r.edit(old,new)
ch('application relation',r'\unsure{\mathrel{\vert\! -\! -}|\mapsto}',r'\longmapsto','drawn bar, shaft and upturned end; mapsto alternative retained','The enlarged relation has a vertical left bar and continuous horizontal shaft with a short rounded upward end, without a distinct two-sided arrowhead.','mapsto','drawing or diagram','medium',True,True,False,True)
ch('rank codomain',r'\underline{Z}',r'\underline{\mathbb{Z}}',r'\underline{Z}','The typed Z has one diagonal, top and bottom serifs, and a separate underline. No doubled diagonal is visible.','top','misread symbol or index','high',False,True,False,True)
ch('cancelled semi-','semi-',r'\ill{}','semi-','The s outline, e bar, m uprights, dotted i and trailing hyphen can all be distinguished beneath the x overtyping.','semi','readable ink left as \\ill{}','high',False,True,True)
ch('cancelled fragment after tannakienne',r'\unsure{(i.e.}',r'\ill{}',r'\unsure{(i.e.}','The opening parenthesis and i/e outlines survive; cancellation crosses the tiny points, so the full fragment remains qualified.','ie','readable ink left as \\ill{}','low',False,True,True)
ch('effective-part quotes','opening typewriter pair only','opening and closing French guillemets','opening typewriter pair only','Two short raised strokes precede partie. There is no closing quotation mark after effective.','effective','text not on the page','high',False,True)
ch('effective multiplicities alphabet',r'\underline{N}',r'\underline{\mathbb{N}}',r'\underline{N}','The typed N has one diagonal and ordinary serifed uprights, with a separate underline; the handwritten Sigma is inside raised parentheses.','N','misread symbol or index','high',False,True,False,True)
ch('cancelled ces',r'\unsure{ces}','ces',r'\unsure{ces}','The old cells are heavily crossed in black and blue; the initial curved trace and final small curve permit ces without independently resolving all three letters.','ces','misread word','low')
ch('effective-part insertion bracket','omitted','omitted','long curved bracket in TikZ','The line below the added K-eff containment curves down into the gap after donnée and rises at its far end.','Keff','drawing or diagram','high',True,True)
ch('éléments ending','éléments','éléments',r'éléme\unsure{nts}','The last three letters run into the scan edge and overlap; the proposed n/t/s sequence cannot be separated as cleanly as the preceding éléme.','elements','misread word','medium',True,True)
ch('cancelled de before parenthesis','de',r'\ill{}','de','A tall d stem and the following e bowl are distinguishable under the two x strikes.','oldde','readable ink left as \\ill{}','high',False,True,True)
ch('termes initial overtyping','termes','termes',r'\unsure{\deleted{e}t|\deleted{o}t|\deleted{t}e}ermes','The initial cell combines a tall t stem and crossbar with a rounded lower outline and possible e bar. The layered impressions do not establish their order.','terms','misread word','low',True,True)
ch('End insertion comma',r'\operatorname{End}(M_i),',r'\operatorname{End}(M_i)',r'\operatorname{End}(M_i),','A distinct comma descends immediately after the closing parenthesis of the raised insertion.','Endinsert','omission')
ch('End insertion bracket','omitted','omitted','curved attachment in TikZ','A line runs beneath the added expression, bends down before correspondant and turns upward at the far right.','Endinsert','drawing or diagram','high',True,True)
ch('rank equality initial',r'\unsure{m|n}','n','n','The enlarged initial character has one arch and a doubled impression at its right upright; no separate second arch is visible.','m','misread symbol or index','medium',True,False,False,True)
ch('rank equality last cell',r'\unsure{\deleted{d}r|\deleted{r}d|r}','r',r'\unsure{\deleted{d}r|\deleted{r}d}','A complete tall d-like stem and lower bowl coexist with an r shoulder. The single unaltered-r alternative omits visible overtyping; order remains unresolved.','r','misread symbol or index','low',True,True,False,True)
ch('determinant old operator',r'\deleted{\det}','omitted',r'\deleted{\det}','The d ascender, rounded e and final t are crossed out immediately before the live N.','olddet','omission','high',False,True,False,True)
ch('parenthetical rank equality placement','after Pol row','beside determinant row','beside determinant row with curved arrow toward lower right','The equality is typed at the first formula height. A large curved pen arrow begins to its left and ends beside the lowest formula.','equality-arrow; formula','insertion or placement','high',True,False,False,True)
ch('large formula arrow','omitted','omitted','curved arrow in TikZ','The shaft bows left then runs down and right to a clear two-stroke arrowhead at the lowest formula level.','equality-arrow','drawing or diagram','high',True,True)
ch('small mark beneath equality','omitted','omitted','short rising stroke and dark lower blob in TikZ','A separate short diagonal with a dense descending middle lies below the equality and left of the arrowhead; it is not expanded into a character.','equality-arrow','drawing or diagram','high',True,True)
ch('comma after determinant formula','no comma','comma','no comma','No comma follows the first exponent before the separately positioned equality; the visible stop stands at the far right of the lowest formula.','formula; equality-arrow','text not on the page','high',False,True)
ch('marginal opening word',r'\unsure{Signaler}','Signaler',r'\unsure{Signaler}','The S, dotted i, g descender and later tall l-like stroke are visible, but the compressed central connection is not separately resolved.','margin; signaler','misread word','medium')
ch('marginal toute',r'\unsure{toute}','toute',r'\unsure{toute}','The tall t strokes and connected middle are visible after rotation, but the individual small joins remain weak.','margin','misread word','medium')
ch('marginal adjective','fonctorielle','fonctoriellement','fonctorielle','The final visible letters end with the two tall l strokes and e; no ment follows before en.','margin','abbreviation expanded or spelling modernised','high',False,True,False,True)
ch('marginal quotation shapes','paired strokes','French guillemets','paired strokes','The quotation marks are short paired pen strokes rather than angle-shaped guillemets.','margin','misread symbol or index','high',False,True)
for p,rd,alt,co in [('application relation','drawn bar and headless shaft',r'\mapsto','medium'),('cancelled fragment','(i.e.','','low'),('cancelled ces','ces','','low'),('éléments ending','nts','','medium'),('termes first cell',r'\deleted{e}t',r'\deleted{o}t; \deleted{t}e','low'),('rank equality last cell',r'\deleted{d}r',r'\deleted{r}d','low'),('marginal opening','Signaler','','medium'),('marginal quantifier','toute','','medium')]:r.doubt(p,rd,alt,co)
for id,pos,txt in [('Keff-hook','above donnée','curved insertion bracket'),('End-hook','above correspondant','curved insertion bracket'),('formula-arrow','right of three formulas','curved arrow from equality height toward lower right'),('formula-mark','below equality','short rising stroke with lower blob')]:
 r.r['inventory_extra'].append(dict(scan='10:064',sheet_kind='typescript',hand='his hand',element='064-'+id,kind='drawing',position=pos,first_words_or_objects=txt,transcribed='yes'))
r.r['inventory_extra'].append(dict(scan='10:064',sheet_kind='typescript',hand='typewriter',element='064-termes-layer',kind='deletion',position='termes first cell',first_words_or_objects='overlapping t and e|o; order uncertain',transcribed='yes'))
r.r['inventory_overrides']={'064-004':{'first_words_or_objects':'sigma followed by drawn bar and headless shaft, mapsto alternative'},'064-031':{'first_words_or_objects':r'\unsure{\deleted{d}r|\deleted{r}d}'},'064-035':{'position':'right of determinant line; curved arrow extends to Pol level'}}
r.notation('typed integer alphabets',r'\underline{Z}; \underline{N}','10/064 rank codomain and effective multiplicities','read: single strokes with separate underlines')
r.notation('application sign','left bar, horizontal shaft, rounded upturn; mapsto alternative','10/064 item 3','unresolved arrowhead intention')
r.notation('rank-equality overwritten cell',r'\deleted{d}r | \deleted{r}d','10/064 rank calculation','overtyping certain; order unresolved')
r.r['abbreviations']=[dict(abbreviation='car. num.',expansion='caractères numériques',attestations='10/064 margin'),dict(abbreviation='alg.',expansion='algébriquement',attestations='10/064 last paragraph'),dict(abbreviation='car.',expansion='caractéristique',attestations='10/064 car. 0')]
r.r['crops']=json.loads(Path('work/crops064.json').read_text())
r.r['inspection_note']='Whole scan and both halves read before source comparison. All agreed text, formulas, typewritten capitals, indices, primes and handwritten insertions were checked in enlarged blocks. Every C doubt and C/H difference was enlarged; the left note was also viewed rotated. The first rank-equality character was judged by its single arch, without correcting the formula from mathematics. The marginal opening and quantifier remain qualified. The equality is at determinant-row height and its arrow reaches the Pol-row level; its physical placement is preserved without deciding its mathematical scope. The partly clipped éléments ending and previously unrecorded termes overtyping are marked. No OCR, later page or sealed context used.'
r.save('work/record064.json')
