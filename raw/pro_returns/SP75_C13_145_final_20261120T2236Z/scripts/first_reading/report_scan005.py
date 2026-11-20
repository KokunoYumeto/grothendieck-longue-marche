from pathlib import Path
import json,csv
r=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
out=r/'edition/reader_reports'
tex=r'''\scanpage{5}
[C]\qquad\textcircled{1}\qquad\mspage{1}

Automorphismes extérieurs du groupe à lacets \deleted{\unsure{P|$\Pi$}} profini $\unsure{\hat\pi=\hat\pi_{0,3}|\hat\Pi=\hat\Pi_{0,3}}$
\margin{\uline{et structure d'extensions de $\mathcal E=\mathcal E_{0,3}$}}
\margin{$\unsure{\partial|\delta}$}

On prend la présentation par les générateurs $l_0,l_1,l_\infty$ liés par
\[
l_0l_1l_\infty=1
\]
Un endomorphisme de $\unsure{\pi_{0,3}|\Pi_{0,3}}$ est donc donné par des éléments $l_0',l_1',l_\infty'$ satisfaisant la $\bar m$ relation --- sauf erreur ce sera un autom. s'ils engendrent $\pi$ (topologiquement).

Soit $\rho$ l'automorphisme défini par la permutation circulaire
\[
\rho(l_0)=l_1,\quad\rho(l_1)=l_\infty,\quad\rho(l_\infty)=l_0
\]
(donc on a $\rho^3=\mathrm{id}$). Considérons aussi la transposition

\deleted{On s'intéresse aux}
\[
\sigma_\infty(l_0)=l_1,\quad\sigma_\infty(l_1)=l_0,\qquad
\sigma_\infty(l_\infty)=(l_1l_0)^{-1}=l_0^{-1}l_1^{-1}
\]
\inserted{$(=\operatorname{int}(\deleted{\unsure{l_0}}l_0^{-1})\cdot l_\infty)$}

on a évidemment $\sigma_\infty^2=\mathrm{id}$. On définit de $\bar m$ $\sigma_0,\sigma_1$ \inserted{(échangeant $l_1$ et $l_\infty$ resp. $l_\infty$ et $l_0$)}, de sorte qu'on a
\[
\rho\sigma_i\rho^{-1}=\sigma_{\rho(i)}
\]
en désignant par $\rho$ aussi la permutation circulaire sur $0,1,\infty$. On considère $\rho$ et les $\sigma_i$ comme des éléments du groupe \inserted{$\unsure{\mathfrak S_3|\mathcal S_3}$} des permutations de l'ens. $\{0,1,\infty\}$, puis on se propose de le faire opérer sur $\unsure{\pi|\pi''}$, en respectant la structure des lacets (avec \inserted{caractère} multiplicateur $1$). On a bien une \inserted{vraie} représentation du ss-groupe $\unsure{\mathfrak S_3^+|\mathcal S_3^+}\simeq\mathbb Z/3\mathbb Z$ engendré
\mspage{4}
'''
(out/'145_scan005.tex').write_text(tex)
boxes=json.loads((r/'edition/crops/145_scan005_crop_boxes.json').read_text())
boxes['145_scan005_14_pi_adjacent_marks']=[740,2015,890,2100]
boxes['145_scan005_15_header']=[48,22,776,123]
(r/'edition/crops/145_scan005_crop_boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
def cp(n):
 return next(k for k in boxes if k.startswith(f'145_scan005_{n:02d}_'))
def loc(n):
 k=cp(n);return {'crop':'crops/'+k+'.png','box':boxes[k]}
changes=[]
def ch(i,place,C,H,final,ink,confidence,kind,c,h,n=None,cat=[2],math='',marked='no',box=None):
 x=dict(id=f's005-{i:02d}',place=place,C=C,H=H,final=final,ink=ink,confidence=confidence,kind=kind,c_changed=c,h_changed=h,marked_in_H=marked,error_category=cat,math_consequence=math)
 x.update(loc(n) if n else {'crop':'','box':box});changes.append(x)
ch(1,'head, upper left',r'[C]\qquad\textcircled{1}',r'',r'[C]\qquad\textcircled{1}','Square brackets enclose a clear C; beside them a single upright 1 is surrounded by an oval. These are source marks, unlike H’s editorial header. The separate central 1 is also preserved.', 'high','omission',False,True,15,[3])
ch(2,'two-line title',r'Automorphismes extérieurs \unsure{du groupe|des groupes} à lacets \deleted{\unsure{P|$\Pi$}} \unsure{profini|profinis} $\hat\pi=\hat\pi_{0,3}$',r'',r'Automorphismes extérieurs du groupe à lacets \deleted{\unsure{P|$\Pi$}} profini $\unsure{\hat\pi=\hat\pi_{0,3}|\hat\Pi=\hat\Pi_{0,3}}$','The title is entirely present. The article has a looped d followed by u, not e-s; groupe has no final s. The final i in profini has a dot and no following s. The struck initial glyph remains ambiguous. Both hatted group signs have a long horizontal head and two descending stems; π versus Π is not securely determined from this page alone.','high','omission',False,True,1,[3],math='The omitted title identifies the profinite loop group and its (0,3) index.')
ch(3,'slanting upper-left margin',r"\margin{\uline{et structure d'extensions de $\mathcal E=\mathcal E_{0,3}$}}",r"\marginal{et structure d'extension de $\mathcal{E} = \mathcal{E}_{0,3}$}",r"\margin{\uline{et structure d'extensions de $\mathcal E=\mathcal E_{0,3}$}}",'After extension the line continues into a separate terminal curved s. All three slanting lines have their own underline; H omits this underlining. The E symbols and indices are present.','high','misread word',False,True,2,[2,3])
ch(4,'left margin below the title note',r'\margin{\unsure{$\partial$}}',r'',r'\margin{$\unsure{\partial|\delta}$}','A dark isolated sign has a lower closed oval and a rising oblique stem with a small hooked head. It is certainly an inscription, but partial versus delta is not distinguishable confidently without a local definition.','low','omission',False,True,3,[3,1])
ch(5,'Un endomorphisme de …',r'\pi_{0,3}',r'\Pi_{0,3}',r'\unsure{\pi_{0,3}|\Pi_{0,3}}','The glyph has a curved top, a dark left stem, and a merging right stem/low continuation. The 0 and 3 are visible, but the joining comma and case are cramped. Its graphic size alone does not distinguish lower- and upper-case pi.','low','misread symbol or index',False,False,4,[1],math='No case choice is imposed; the witnesses disagree on the group symbol.')
ch(6,'satisfaisant la … relation',r'\unsure{\bar m|=}',r'même',r'\bar m','The lower stroke rises and falls in a cursive m shape; a separate horizontal bar lies above it. There are no letters ê-m-e after it.','high','abbreviation expanded or spelling modernised',False,True,5,[8])
ch(7,'ce sera un …',r'autom.',r'automorphisme',r'autom.','The ink ends after a-u-t-o-m with a distinct full stop. No suffix or continuation is written.','high','abbreviation expanded or spelling modernised',False,True,6,[8])
ch(8,'parenthesis below the rho display',r'donc on a',r'donc aussi',r'donc on a','Following donc are a low o-n cluster and then a separate small a. There is no tall/dotted sequence for aussi at this position. The lower line On s’intéresse aux is independently struck through.','high','misread word',False,True,7,[2])
ch(9,'interlinear insertion below the last sigma formula',r'\inserted{$(=\operatorname{int}(\deleted{\unsure{l_0}}l_0^{-1})\cdot l_\infty)$}',r'\bigl(= \mathrm{int}(l_0^{-1}).\, l_\infty\bigr)',r'\inserted{$(=\operatorname{int}(\deleted{\unsure{l_0}}l_0^{-1})\cdot l_\infty)$}','The parenthesized expression is written below the last equality, not on the main display line. The operand after int contains dark overlapping/reworked strokes. The struck l_0 suggested by C is not legible letter for letter and remains unsure; no deletion is silently removed. The live exponent has a long horizontal stroke and a separate 1; the central retracing warrants root review of the layering.','medium','deletion state',False,True,8,[7,6],math='The deletion-layer reading remains provisional; the live inner-conjugation operand is retained as l_0^{-1}.')
ch(10,'On définit de …',r'\unsure{\bar m|=}',r'même',r'\bar m','As in the earlier occurrence, the lower stroke is a low wavy m under a horizontal bar. It is neither a plain equals sign nor the written-out word même.','high','abbreviation expanded or spelling modernised',False,True,9,[8])
ch(11,'above sigma_0, sigma_1 and de sorte',r'\inserted{(échangeant $l_1$ et $l_\infty$ resp. $l_\infty$ et $l_0$)}',r'(échangeant $l_1$ et $l_\infty$ resp. $l_\infty$ et $l_0$)',r'\inserted{(échangeant $l_1$ et $l_\infty$ resp. $l_\infty$ et $l_0$)}','The parenthesis is above the main line. A long curved insertion guide begins immediately after sigma_1 and runs below the inserted phrase. The l_1 is heavily retraced but the subscript 1 and all subsequent indices are visible.','high','insertion or placement',False,True,9,[6])
ch(12,'de sorte … before the conjugation display',r"qu'on a",r'que',r"qu'on a",'The long-descending q is followed by low joined strokes, an apostrophe, n, and a separate final a. The expression extends well beyond a possible que.','high','omission',False,True,9,[3])
ch(13,'comme des éléments du …',r'gr.',r'groupe',r'groupe','After the descending g and short r there are further low letters and a separate long descender for p, followed by e. Thus the word is fully written; the apparent dot in C’s gr. is part of the following low strokes.','high','misread word',True,False,10,[2,8])
ch(14,'inserted symmetric-group name above groupe des',r'\inserted{$\unsure{\mathfrak S_3|\mathcal S_3}$}',r'$\mathfrak{S}_3$',r'\inserted{$\unsure{\mathfrak S_3|\mathcal S_3}$}','The S-like sign and 3 are placed above the main line with a curved guide into the interval between groupe and des. The rounded outer stroke and inner loop do not securely distinguish a calligraphic from a Fraktur convention; C’s font doubt remains.','medium','insertion or placement',False,True,10,[6,1])
ch(15,"after l'ens. {0,1,infinity}",r"\unsure{qu'on|puis on}",r"qu'on",r'puis on','The first letter has a descending p-type stem rather than a closed q bowl. A separate dot over the medial i and a short following s precede the o-n cluster. This supports the two words puis on.','high','misread word',True,True,11,[2])
ch(16,'se propose de … faire opérer',r'le',r'',r'le','At the right end of this line a separate ascending loop for l joins a low e after de. The word le is present.','high','omission',False,True,11,[3])
ch(17,'structure … across the next line break',r'des lacets',r'locale',r'des lacets','The end of the upper line contains des. The next line begins with a looped l, a-c-e, a tall crossed t, and terminal s. These are lacets, not locale.','high','misread word',False,True,12,[2])
ch(18,'small insertion before multiplicateur',r'\inserted{caractère}',r'\marginal{\uncertain{correction}}',r'\inserted{caractère}','The small line reads c-a-r-a-c-t-è-r-e, with a clear tall crossed t and an accent above the following e. A curved insertion guide enters before multiplicateur. There is no long double-r/correction sequence or terminal ion.','high','misread word',False,True,12,[2,6],marked='yes')
ch(19,'above représentation at the final line start',r'\inserted{vraie}',r'\marginal{vraie}',r'\inserted{vraie}','The word vraie is written immediately above représentation. A curved insertion guide returns to the beginning of that word; it is not an independent margin comment. All letters are visible in the bottom half.','high','insertion or placement',False,True,None,[6],box=[190,2187,573,2290])
ch(20,'bottom-left pagination',r'\mspage{4}',r'',r'\mspage{4}','A handwritten 4 is visible alone at the lower left. H’s page-identification 4 is editorial and does not transcribe this physical bottom-margin position.','high','omission',False,True,None,[3],box=[38,2268,87,2330])

decisions=[]
def de(id,decision,reading,ink,n,confidence):
 x=dict(id=id,decision=decision,reading=reading,ink=ink,confidence=confidence);x.update(loc(n));decisions.append(x)
de('M0765','first','du groupe','Looped d then low u; no e-s sequence and no s after groupe.',1,'high')
de('M0766','first','profini','The final i has a dot and short stem; no following s is written. The preceding struck glyph remains separately unresolved.',1,'high')
de('M0767','undecided',r'$\unsure{\partial|\delta}$','The isolated loop-and-stem sign could be partial or delta; no page-local definition fixes it.',3,'low')
de('M0768','first',r'\bar m','A genuinely wavy cursive lower stroke is surmounted by a separate bar.',5,'high')
de('M0769','first',r'\bar m','The same barred wavy m is repeated at the next paragraph.',9,'high')
de('M0770','undecided',r'\unsure{\mathfrak S_3|\mathcal S_3}','The S-shaped sign is rounded and looped; its precise alphabet remains doubtful. The 3 and insertion position are clear.',10,'medium')
de('M0771','alternative','puis on','Descending p-type initial, dotted medial i, short s, then an o-n group; there is no matching q bowl/apostrophe pair.',11,'high')
de('M0772','undecided',r'\unsure{\mathfrak S_3^+|\mathcal S_3^+}','The same rounded S-like sign recurs; the superscript is a clear plus. The low 3 has a hooked lower stroke, comparable to the denominator 3 in the same formula.',13,'medium')

doubts=[
 {'place':'struck glyph in the title before profini','reading':r'\deleted{\unsure{P|$\Pi$}}','alternatives':['P',r'$\Pi$'],'confidence':'low','reason':'The glyph is heavily retraced and crossed. Not all pre-cancellation strokes can be separated, and the boundary from the initial of profini may warrant review; retain the deletion doubt rather than resolving a struck letter from context.'},
 {'place':'title hatted-group equality','reading':r'\unsure{\hat\pi=\hat\pi_{0,3}|\hat\Pi=\hat\Pi_{0,3}}','alternatives':[r'\hat\pi=\hat\pi_{0,3}',r'\hat\Pi=\hat\Pi_{0,3}'],'confidence':'low','reason':'Both signs have a long horizontal head and two nearly straight stems. Their size and strokes on this page do not reliably fix case.'},
 {'place':'isolated left-margin sign','reading':r'$\unsure{\partial|\delta}$','alternatives':[r'\partial',r'\delta'],'confidence':'low','reason':'The isolated closed oval with hooked oblique stem admits both signs; no local definition settles its function.'},
 {'place':'endomorphisme de group symbol','reading':r'\unsure{\pi_{0,3}|\Pi_{0,3}}','alternatives':[r'\pi_{0,3}',r'\Pi_{0,3}'],'confidence':'low','reason':'H and C disagree on the case. The low right stroke merges with the index region, so the crop does not separate the two forms confidently.'},
 {'place':'struck operand inside the inserted int expression','reading':r'\deleted{\unsure{l_0}}','alternatives':[r'l_0','unseparated overwritten strokes'],'confidence':'low','reason':'Several dark strokes overlap the live operand. They do not yield a fully plain struck l and subscript 0. The deletion hypothesis is retained from C but requires root adjudication of the ink layering.'},
 {'place':'first inserted symmetric-group name','reading':r'\unsure{\mathfrak S_3|\mathcal S_3}','alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'The symbol is a rounded S with a hooked upper-right stroke and closed lower loop; this page alone does not define its typographic alphabet.'},
 {'place':'last occurrence of pi, before en respectant','reading':r'\unsure{\pi|\pi\prime\prime}','alternatives':[r'\pi',r'\pi\prime\prime'],'confidence':'low','reason':'A targeted crop shows two small, separate, very dark points diagonally above-right of pi, followed by a normal comma much lower and farther right. Neither point is an elongated prime. They may be ink points rather than an inscription; the unprimed first reading is retained and the possibility is exposed for root review, not silently converted to a prime.'},
 {'place':'final symmetric-group formula','reading':r'\unsure{\mathfrak S_3^+|\mathcal S_3^+}','alternatives':[r'\mathfrak S_3^+',r'\mathcal S_3^+'],'confidence':'medium','reason':'Same unresolved alphabet distinction as the inserted group name. The superscript plus and the isomorphism sign are plain.'}
]

inventory=[]
def inv(i,kind,pos,words,box,hand='main cursive hand',sheet='handwritten sheet'):
 inventory.append(dict(element=f'005-{i:02d}',kind=kind,position=pos,first_words_or_objects=words,box=box,sheet_kind=sheet,hand=hand,transcribed='yes'))
inv(1,'margin note','upper-left header','[C]',[50,22,154,120])
inv(2,'margin note','left above title',r'\textcircled{1}',[221,43,277,121])
inv(3,'margin note','top centre','1',[725,29,769,91],'pagination hand, attribution indeterminate')
inv(4,'text','top two lines','Automorphismes extérieurs du groupe',[265,78,1538,263])
inv(5,'deletion','title second line',r'\unsure{P|$\Pi$}',[523,177,577,249])
inv(6,'margin note','slanting upper-left, three underlined lines',"et structure d’extensions de E=E0,3",[20,130,250,445])
inv(7,'margin note','left below slanted note',r'\unsure{\partial|\delta}',[22,445,77,510])
inv(8,'text','first paragraph, two lines','On prend la présentation',[253,273,1575,428])
inv(9,'display','below first paragraph',r'l_0l_1l_\infty=1',[584,450,882,524])
inv(10,'text','four lines below first display','Un endomorphisme de',[249,537,1643,872])
inv(11,'text','two lines above rho display',r'Soit \rho l’automorphisme',[246,878,1515,1065])
inv(12,'display','first rho display',r'\rho(l_0)=l_1,\rho(l_1)=l_\infty,\rho(l_\infty)=l_0',[486,1071,1184,1149])
inv(13,'text','line below rho display','(donc on a',[204,1137,1651,1209])
inv(14,'deletion','between transposition line and sigma display',"On s’intéresse aux",[243,1184,798,1247])
inv(15,'display','middle of page',r'\sigma_\infty(l_0)=l_1,\sigma_\infty(l_1)=l_0,\sigma_\infty(l_\infty)=(l_1l_0)^{-1}=l_0^{-1}l_1^{-1}',[486,1238,1585,1327])
inv(16,'insertion','below rightmost part of sigma display',r'(=\operatorname{int}(\deleted{\unsure{l_0}}l_0^{-1})\cdot l_\infty)',[1340,1301,1654,1381])
inv(17,'deletion','within the inserted int operand',r'\unsure{l_0}',[1477,1311,1531,1369])
inv(18,'text','two main lines around exchange insertion','on a évidemment',[213,1356,1595,1548])
inv(19,'insertion','above sigma_0, sigma_1 and de sorte',r'(échangeant l_1 et l_\infty resp. l_\infty et l_0)',[412,1405,1107,1478])
inv(20,'display','below de sorte qu’on a',r'\rho\sigma_i\rho^{-1}=\sigma_{\rho(i)}',[614,1560,953,1663])
inv(21,'text','bottom paragraph, seven main lines','en désignant par',[196,1667,1647,2302])
inv(22,'insertion','above groupe des',r'\unsure{\mathfrak S_3|\mathcal S_3}',[1179,1805,1275,1883])
inv(23,'insertion','above multiplicateur','caractère',[513,2083,699,2145])
inv(24,'insertion','above représentation','vraie',[190,2184,319,2241])
inv(25,'margin note','bottom-left','4',[38,2268,87,2330],'pagination hand, attribution indeterminate')

second=[]
def sb(i,kind,coords,reading):second.append(dict(box=f'B{i:02d}',kind=kind,coords=coords,reading=reading))
sb(1,'handwritten header labels and page number',[48,22,776,123],r'[C]\qquad\textcircled{1}\qquad\mspage{1}')
sb(2,'title omitted by H; title deletion; C doubts and hatted formula',[255,75,1535,263],r'Automorphismes extérieurs du groupe à lacets \deleted{\unsure{P|$\Pi$}} profini $\unsure{\hat\pi=\hat\pi_{0,3}|\hat\Pi=\hat\Pi_{0,3}}$')
sb(3,'marginal note, underline and lexical disagreement',[20,130,250,445],r"\margin{\uline{et structure d'extensions de $\mathcal E=\mathcal E_{0,3}$}}")
sb(4,'isolated marginal sign with unresolved C doubt',[22,445,77,510],r'\margin{$\unsure{\partial|\delta}$}')
sb(5,'C/H symbol case disagreement',[840,527,1105,626],r'de $\unsure{\pi_{0,3}|\Pi_{0,3}}$')
sb(6,'barred-m C doubt and written abbreviation versus H expansions',[241,695,1642,800],r'$\bar m$ relation --- sauf erreur ce sera un autom.')
sb(7,'lexical disagreement and struck passage',[195,1128,828,1249],r"(donc on a $\rho^3=\mathrm{id}$). \deleted{On s'intéresse aux}")
sb(8,'formula with doubtful deletion and interlinear insertion',[1070,1230,1655,1376],r'$\sigma_\infty(l_\infty)=(l_1l_0)^{-1}=l_0^{-1}l_1^{-1}$ \inserted{$(=\operatorname{int}(\deleted{\unsure{l_0}}l_0^{-1})\cdot l_\infty)$}')
sb(9,'interlinear exchange parenthesis, barred-m doubt, rewritten indices and lexical disagreement',[208,1410,1130,1550],r"$\bar m$ $\sigma_0,\sigma_1$ \inserted{(échangeant $l_1$ et $l_\infty$ resp. $l_\infty$ et $l_0$)}, de sorte qu'on a")
sb(10,'full word versus abbreviation, inserted group symbol with C doubt',[885,1775,1380,1940],r'du groupe \inserted{$\unsure{\mathfrak S_3|\mathcal S_3}$} des')
sb(11,'puis on and le lexical disagreements',[780,1920,1580,2036],r', puis on se propose de le')
sb(12,'lexical disagreements, caractere insertion and newly doubtful points beside pi',[200,2005,1660,2200],r'faire opérer sur $\unsure{\pi|\pi\prime\prime}$, en respectant la structure des lacets (avec \inserted{caractère} multiplicateur $1$). On a bien une')
sb(13,'vraie insertion and entire last-line formula carrying a C doubt',[189,2180,1636,2305],r'\inserted{vraie} représentation du ss-groupe $\unsure{\mathfrak S_3^+|\mathcal S_3^+}\simeq\mathbb Z/3\mathbb Z$ engendré')
sb(14,'handwritten bottom page number',[38,2268,87,2330],r'\mspage{4}')

coverage=[]
sub={1:1,2:2,3:3,4:4,13:6,15:7,16:8,19:9,22:10,23:12,26:13,27:15,28:16,29:17,30:18,32:20}
explanations={
5:'Tokenization across l_0 l_1 juxtaposition; both witnesses give the same product and indices.',
6:'Tokenization across l_1 l_infinity juxtaposition; both give the same product.',
7:'Equivalent placement of prime before or after the subscript in LaTeX.',
8:'Continuation of the equivalent prime/subscript tokenization.',
9:'Equivalent placement of prime before or after the subscript in LaTeX.',
10:'Continuation of the equivalent prime/subscript tokenization.',
11:'Equivalent placement of prime before or after the subscript in LaTeX.',
12:'Continuation of the equivalent prime/subscript tokenization; all three primes are visible.',
14:'ASCII triple-hyphen versus Unicode dash; an actual horizontal dash is present after relation.',
17:'Tokenization of juxtaposed l_1 l_0; no lexical or mathematical difference.',
18:'Display delimiter only; the placement/deletion differences of the following parenthesis are logged at s005-09.',
20:'TeX multiplication-point/spacing syntax only: a point is written before l_infinity.',
21:'Display delimiter only; the actual insertion placement is logged at s005-09.',
24:'TeX thinspace command tokenized as a comma; no source punctuation disagreement.',
25:'TeX thinspace command tokenized as a comma; no source punctuation disagreement.',
31:'Certainty/alphabet alternatives alone; M0772 remains unresolved and is recorded in decisions and doubts.'}
rows=list(csv.DictReader((r/'packets/145_scan005/differences.tsv').open(),delimiter='\t'))
for i,row in enumerate(rows,1):
 if i in sub:
  x={'row':i,'status':'substantive','change_id':f's005-{sub[i]:02d}'}
  if i==1:x['explanation']='The scan/page markers are editorial, but the source [C] label and circled 1 are absent in H.'
  if i==26:x['explanation']='The word groupe is the principal lexical difference; the adjacent group-symbol insertion is separately s005-14, and its uncertainty is M0770.'
  coverage.append(x)
 else:coverage.append({'row':i,'status':'macro/editorial','explanation':explanations[i]})
assert len(rows)==32
report={
'scan':5,'reader':'/root/reader_b','lines_read':36,
'layout':'Portrait handwritten sheet, 1681 × 2368 pixels. [C] and a circled 1 stand at upper left, with a separate 1 at top centre. Two-line title; a slanted three-line underlined note and isolated sign occupy the upper-left margin. Four main displayed equations/collections of equations divide the prose. There are five interlinear additions (the inner-conjugation parenthesis, exchange parenthesis, symmetric-group symbol, caractère and vraie) and three cancellation loci including the doubtful title glyph and int operand. A 4 stands at bottom left. No diagram or drawing. The 36-line count includes the header, three marginal-note lines, isolated margin sign, interlinear lines, crossed line and bottom number; overlapping halves were not double-counted.',
'changes':changes,'decisions':decisions,'doubts':doubts,'inventory':inventory,'second_boxes':second,
'notation':[
 {'observation':r'\bar m stands in prose for même; its lower component is a cursive wavy m, not a second straight equals stroke.','places':['satisfaisant la … relation','On définit de …'],'qualification':'Both occurrences on this page were cropped. H expands each to même.'},
 {'observation':r'The group symbols in the title, endomorphism sentence and later prose use pi-like head-and-two-stem forms.','places':['title equality','Un endomorphisme de','engendrent pi','faire opérer sur pi'],'qualification':'Case is unresolved in the title and subscripted occurrence. The last occurrence also has two small adjacent dark points, whose status is unresolved.'},
 {'observation':r'An S-like rounded symbol with subscript 3 names the permutation group; it recurs with a superscript +.','places':['insertion after groupe','final formula'],'qualification':'The relative glyph shapes agree on this page; Fraktur versus calligraphic alphabet is not securely established.'},
 {'observation':r'The generators are l_0, l_1, l_infinity, and the cyclic automorphism is rho.','places':['presentation','rho display','sigma display','conjugation display'],'qualification':'All visible occurrences were read. No uniform claim about other pages or intended corrections is made.'},
 {'observation':r'The quotient is written with a slash and two doubled-stroke Z symbols.','places':['last-line S_3^+ formula'],'qualification':'Retained as mathbb Z/3 mathbb Z; no alternate quotient construction is inferred.'}
],
'hand':[
 {'habit':'The short cursive m is very low and wavy; with a separate overbar it can resemble an equals sign.','places':['M0768','M0769'],'universal_on_this_page':'Both observed barred-m occurrences match.','witness_misreadings':'C leaves = as an alternative; H expands the abbreviation.'},
 {'habit':'A cursive g has a very long descending loop and a small upper loop, while the p descender later in groupe remains distinct.','places':['title groupe','bottom prose groupe'],'universal_on_this_page':'Both words have a long g descender; only the bottom one caused a witness abbreviation.','witness_misreadings':'C reads the fully written bottom groupe as gr.'},
 {'habit':'Low word strokes can collapse to horizontal waves; dotted i and separated word gaps remain diagnostic.','places':['puis on','qu’on a','on a'],'universal_on_this_page':'Not asserted for every word.','witness_misreadings':'H reads puis on as qu’on, and donc on a as donc aussi; C had puis on only as an alternative.'},
 {'habit':'The digit 3 can have a very attenuated upper curve and a prominent hooked lower stroke.','places':['subscript in final S_3^+','denominator 3 in Z/3Z','earlier inserted S_3'],'universal_on_this_page':'The clearest earlier 3 has two lobes; the final small 3s are more attenuated.','witness_misreadings':'None demonstrated; retained as a caution for the fresh reader.'},
 {'habit':'Inserted phrases use long curved guide strokes; these are placement guides rather than underlining.','places':['échangeant parenthesis','S_3 insertion','caractère','vraie'],'universal_on_this_page':'Four text/symbol additions have such guides; the inner-conjugation parenthesis is placed directly under its target formula.','witness_misreadings':'H flattens some additions into the line and renders caractère/vraie as independent marginal comments.'}
],
'abbreviations':[
 {'form':r'\bar m','expansion':'même','place':'two prose occurrences'},
 {'form':'autom.','expansion':'automorphisme','place':'endomorphism paragraph'},
 {'form':'resp.','expansion':'respectivement','place':'exchange parenthesis'},
 {'form':"l’ens.",'expansion':"l’ensemble",'place':'bottom paragraph'},
 {'form':'ss-groupe','expansion':'sous-groupe','place':'final line'},
 {'form':'id','expansion':'identité','place':'rho^3 and sigma_infinity^2 formulas'},
 {'form':'int','expansion':'automorphisme intérieur','place':'interlinear inner-conjugation formula'}
],
'notes':[
 'The author introduces exterior automorphisms of the profinite loop group indexed by (0,3), with an underlined marginal addition about the extension structure of E=E_{0,3}. He chooses generators l_0, l_1 and l_infinity with product 1, then describes endomorphisms through triples satisfying the same relation. This is a transcriptional account of his statements, not a verification of them.',
 'The author’s explicit caution is “sauf erreur” before the assertion that the endomorphism is an automorphism when its images generate pi topologically. No date occurs on the sheet. The source contains [C], a circled 1, a separate upper-centre 1 and a lower-left 4; the relation of the two uncirculated pagination numbers is not inferred.',
 'The page defines a cyclic permutation rho of the three generators, a transposition sigma_infinity and analogous sigma_0, sigma_1, and writes the conjugation relation rho sigma_i rho^{-1}=sigma_{rho(i)}. It then proposes an action respecting the structure of the loops with multiplier character 1 and states that there is already a true representation of the cyclic subgroup S_3^+ isomorphic to Z/3Z. The final sentence continues beyond this sheet.',
 'No mathematical proof or group computation was performed in this reading. Mathematical context was used only to recognize the defined permutation-group notation and to flag difficult indices; it did not replace uncertain strokes with an expected symbol. In particular the Pi/pi case and the style of S are deliberately left open.',
 'The three C deletion loci were separately examined: the title glyph remains unsure; the full line On s’intéresse aux is visibly struck through and remains deleted; the alleged l_0 deletion inside int is entangled with retracing and remains unsure. The exact layering of that last operand and the boundary between the struck title glyph and profini deserve root review. Neither was resolved merely because the live expression is mathematically familiar.',
 'All five C insertion loci were checked for attachment. The int parenthesis is below the final sigma equality; the exchange parenthesis attaches after sigma_1; the S_3 attaches after groupe; caractère attaches immediately before multiplicateur; vraie attaches immediately before représentation. No additional diagram, drawing, date or marginal sentence was found.',
 'An agreed unprimed pi in the final prose has two tiny dark points above-right, identified only during the detailed crop reading. A separate tight crop records them. They are round rather than elongated, so accidental ink is the preferred first reading, but the transcript exposes a possible double-prime alternative for adjudication. The ordinary comma after the symbol is distinct and undisputed.',
 'The first-pass images were consulted exactly once each: page.jpg for layout, top.png and bottom.png line by line. Fifteen first-reading crops were made, each for a distinct target or tightly related group; no OCR, external research, other scan, or other reader report was consulted. No TeX compilation was run.'
],
'check_events':[],
'diff_coverage':coverage
}
(out/'145_scan005.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(out/'145_scan005.json'),'tex':str(out/'145_scan005.tex'),'crops':len(boxes),'changes':len(changes),'decisions':len(decisions),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(coverage)}))
