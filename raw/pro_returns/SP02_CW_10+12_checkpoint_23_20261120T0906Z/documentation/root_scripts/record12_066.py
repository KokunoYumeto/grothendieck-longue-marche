from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('SP02_CW_10+12/scripts').resolve()))
from root_record import Record
r=Record('B12-01',12,66,'cancelled_draft')
H='[No H text supplied.]'
def ch(place,C,final,shows,crop,kind='other',confidence='high',against_C=False,consequential=False):
 r.change(place,C,H,final,shows,crop,kind,confidence,against_C,False,False,consequential)
cor=r'cor\rlap{l}ollaire'; ab=r"\rlap{\(B\)}A'/\underline{p}\rlap{\(B\)}A'"; last=r'\unsure{\rlap{\(u\)}h|h}'
r.edit('corollaire',cor)
libre=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {\deleted{projectif}};
\node[anchor=south,inner sep=0,yshift=.08cm] at (base.north) {\inserted{libre}};
\end{tikzpicture}}'''
r.edit(r'\deleted{projectif}\inserted{libre}',libre,count=2)
formula=r"\underline{p}=\underline{p}'\unsure{\quad|\cap}A'"
stack=r'''\mbox{\begin{tikzpicture}[baseline=(base.base)]
\node[inner sep=0] (base) {$\deleted{\underline{p}=\underline{p}'\unsure{\quad|\cap}A'}$};
\path (base.north west) -- coordinate[pos=.60] (ins) (base.north east);
\node[anchor=south,inner sep=0,yshift=.10cm] at (ins) {\inserted{$x$}};
\end{tikzpicture}}'''
r.edit(r"$\deleted{\unsure{\underline{p}=\underline{p}'\cap A|\underline{p}=\underline{p}'\,A}}\inserted{x}$",stack)
r.edit(r"\unsure{\deleted{B}A|\deleted{A}B}'/\underline{p}\deleted{B}A'",ab)
r.edit(r'h\quad A-\underline{p}',last+r'\quad A-\underline{p}')
ch('Lemme parenthesis, second o of corollaire','corollaire',cor,'The second o has a full oval crossed by a vertical stem with a left top serif and broad basal foot, matching the adjacent l impressions. Both o and l are preserved in one cell; chronology is not asserted.','corollaire','misread word','high',True)
for loc,crop in [('lemma line6','libre1'),('proof line14','libre2')]:
 ch(loc+', projectif/libre',r'\deleted{projectif}\inserted{libre}',libre,'The nine letters of projectif remain readable under typed x cancellation. Libre is typed immediately above the middle of that word, without a leader; the two vertical levels are reproduced.',''+crop,'insertion or placement','high',True)
ch('proof, deleted formula after Soit',r"\deleted{\unsure{\underline{p}=\underline{p}'\cap A|\underline{p}=\underline{p}'\,A}}",r'\deleted{'+formula+'}',"The two p descenders and their underlines, equality bars and the prime after the second p survive the x overstrikes. A separate raised apostrophe is visible after A, above the final cancellation x; C omits it in both alternatives. In the middle cell only the cancellation x is secure: no arch of an intersection sign can be isolated, so a blank is the first qualified reading and cap remains an alternative.",'cancelform; cancelformA; cancelmiddleA; cancelendA','misread symbol or index','medium',True,True)
ch('inserted x over deleted formula',r'\inserted{x} after the canceled formula',stack,"The lower-case x is typed on the line above, over the right-central part of the deleted formula, approximately the p-prime/next-cell area. No caret or leader occurs. It is placed above the surviving formula rather than appended to its baseline.",'insertx; cancelformA','insertion or placement','high',True)
ch('proof, numerator and denominator A/B cells',r"\unsure{\deleted{B}A|\deleted{A}B}'/\underline{p}\deleted{B}A'",ab,'Each capital cell has the two rounded right bowls of B and the diagonal legs/crossbar of A in the same space. There is no separate deletion stroke assigning an order to these impressions. Both overlaps and both following primes are clear; C macro/table doubt about chronology is resolved by preserving the simultaneous appearance.','overAB','deletion state','high',True,True)
ch('support equality, final handwritten round glyph',r'\handwritten{\unsure{\varnothing|\phi}}',r'\handwritten{\unsure{\varnothing|\phi}}','The final oval is taller than the preceding phi oval, with shorter projecting slash ends; the two forms remain close enough that the empty-set/phi distinction is unresolved. C doubt is retained from these stroke proportions, without using the expected mathematics.','suppempty','other','medium')
ch('last line, h cell','h',last,'A tall left stem/top serif and right shoulder give h, but a further leftward serif at x height and a low joining curve are also present. Compared with the clean h above and u/n in annulé, a u/h overlap is a possible reading; fused strokes prevent a secure decomposition. The new doubt records the extra ink without assigning typing order.','hAlast; hbottomB; hcontrolA; annuleB; ncontrolB','misread symbol or index','low',True)
for loc,s,desc,crop in [
 ('opening line','sympatique','No h occurs between t and i; all letters of sympatique are legible.','sympatique'),
 ('second line','varésulter','The a and r occupy consecutive typewriter cells with no intervening word-space; acute on é is visible.','varesulter'),
 ('lemma localized modules',r'B_h ... A_h','The first capital has two rounded bowls, the second has diagonal legs and crossbar. Each lowered letter is h; neither capital carries a prime. The literal B/A distinction is retained.','Bh; Ah'),
 ('proof ending','annulé','The final e has an acute and no following e before par. The masculine ending is retained.','annule; annuleB')]:
 ch(loc,s,s,desc,crop)
r.doubt('support equality, final hand glyph',r'\varnothing',r'\phi','medium','Tall oval and relatively short slash projections favor empty set, but the handwritten phi form is very similar.')
r.doubt('canceled formula, cell between p-prime and A-prime',r'\quad',r'\cap','low','Only cancellation x is secure in this cell; cap cannot be isolated. Both neighboring primes are visible.')
r.doubt('last line, h overprint',r'\rlap{\(u\)}h','h','low','Extra left serif at x height and low joining curve; possible u/h overlap, with no secure chronological reading.')
r.notation('A/B typewriter overlap',ab,'12:066 proof quotient. Both A and B outlines in both cells; no chronology/deletion order inferred.')
r.notation('blank membership positions',r'h\quad B-(0); qualified h\quad A-\underline p','12:066 lemma and final line. The gaps contain no visible membership sign; they are not filled.')
r.notation('handwritten phi and empty-set forms',r'\phi; \unsure{\varnothing|\phi}','12:066 all eight phi occurrences enlarged separately, including two with lowered underlined p; final support-equality oval remains qualified.','uncertain')
r.notation('tensor typed as O with x overprint',r'B\otimes_A A prime','12:066 lemma; oval and crossing diagonals visible, lowered A underneath.')
r.notation('primes and localized ideals',r"A',B',F',u',x',\underline p'; A'_{\underline p}; g^{-1}(x)",'12:066 every occurrence individually enlarged. Raised compact apostrophes have no exclamation dots; minus-one is raised, p indices lowered and underlined.')
r.notation('typed h overlap',last,'12:066 final line; clean h in lemma used as control.','uncertain')
for a,e in [('néc','nécessairement'),('i.e.','id est'),('supp','support'),('Spec','spectre')]:r.r.setdefault('abbreviations',[]).append(dict(abbreviation=a,expansion=e,attestations='12:066'))
r.r['inventory_overrides']={'066-12':dict(first_words_or_objects="p = p-prime [blank/cap uncertain] A-prime"),'066-14':dict(kind='text',first_words_or_objects='A/B overlapping type impressions, twice; chronology unspecified')}
for i,(s,t,p,h) in enumerate([('l/o overlap in corollaire','text','lemma parenthesis','typewriter'),('qualified u/h overlap','text','last line h cell','typewriter'),('Lemme underline','text','lemma heading','typewriter'),('archive sheet number 65 retained as comment','margin note','bottom-left corner','another unnamed hand')],1):
 r.r['inventory_extra'].append(dict(scan='12:066',sheet_kind='cancelled_draft',hand=h,element=f'066-R{i:03d}',kind=t,position=p,first_words_or_objects=s,transcribed='yes'))
r.r['crops']=json.loads(Path('work/crops12_066.json').read_text())+json.loads(Path('work/fine12_066.json').read_text())
r.r['inspection_note']='Root alone viewed whole066 and both actual supplied halves before C/H, then all three macro doubts, three doubts-table rows, four slips, two abbreviation rows and all20 C inventory elements. H supplies no text; no H collation rows are made. All64 crop recipes were viewed; xloc/overAB from a truncated call were re-viewed before counting them. The acontrolA exploratory crop missed its target and is not evidence for a letter reading; the subsequent annuleB crop supplies the visible control letters. Every mathematical sign, index, overprint, cancellation, insertion and C doubt was enlarged; no slanted verbal annotation occurs. The three global cancellation strokes were followed to their endpoints. Both supplied halves were reread line by line after the crops; line-break hyphens in contraire and également are joined. Archive65 remains a comment only. Context is sealed; this is first-pass collation, not the ordered audit or a mathematical check.'
r.save('work/record12_066.json')
