from pathlib import Path
import json
base=Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
manifest=json.loads((base/'edition/reader_reports/145_scan015_crop_manifest.json').read_text())
crops={x['name']:x for x in manifest}
changes=[]
def ch(n,place,C,H,final,ink,kind,crop,c=False,h=True,mark='no',conf='high',cats=(10,),math=''):
    z=crops[crop]
    changes.append(dict(id=f's015-{n:02}',place=place,C=C,H=H,final=final,ink=ink,confidence=conf,kind=kind,c_changed=c,h_changed=h,marked_in_H=mark,crop=z['crop'],box=z['box'],error_category=list(cats),math_consequence=math))
ch(1,'Opening cancelled paragraph: word after groupe','envisagé',r'\uncertain{discret}','envisagé','The connected initial en/vi strokes continue into a low s, an a and a descending g, followed by the accented ending. The word is longer than discret and lacks its initial d shape.','misread word','opening_and_insertion',mark='yes',cats=(2,))
ch(2,'Opening insertion: locally cancelled word',r'\deleted{\unsure{stable}}',r'\struck{\ill{}}',r'\deleted{\unsure{stable}}','The small first curved stroke and tall t/b/l-like strokes are visible above the main line, but the dark transverse cancellation hides portions of the letters. Stable is retained tentatively; no full recovery is claimed.','deletion state','opening_and_insertion',mark='yes',conf='medium',cats=(5,7))
ch(3,'Opening: replacement fixed by rho and its attachment',r'\inserted{\deleted{\unsure{stable}} \unsure{fixé} par $\unsure{\rho|\varphi}$}',r'\marginal{\struck{\ill{}} fixé par $\rho$}',r'\inserted{\deleted{\unsure{stable}} fixé par $\rho$}','The raised fixé has a clear f, dotted i, crossing x and accented e; par and the looped, descending rho follow. A long curved guide brings this correction to the groupe envisagé phrase. It is an attached insertion, with its own cancelled trial, rather than an independent marginal sentence.','insertion or placement','opening_and_insertion',mark='yes',cats=(5,6,7))
ch(4,'Opening continuation after the insertion',', il',r"qu'il",', il','The final envisagé supplies the low descending loop before the correction guide. The following small dotted stroke and upright form il; there is no separate q/u sequence belonging to a following qu’il.','misread word','opening_and_insertion',cats=(2,9))
ch(5,'First underbrace: upper inserted trial',r'\inserted{\unsure{l_1l_\infty|l_\infty}}',r'\struck{l_1 \sigma_\infty}',r'\inserted{\deleted{l_{\unsure{1}}\sigma_\infty}}','The second glyph has a long horizontal top bar with a curved lower body, matching sigma rather than the looped l elsewhere in the same formula. Its infinity subscript is visible. A dark rising local stroke crosses this upper trial, independently of the thin page-wide cancellation. The crossed first index retains a local doubt.','misread symbol or index','expanded_product',c=True,h=False,mark='yes',conf='medium',cats=(1,7),math='The locally cancelled trial contains sigma_infinity, not a second l factor.')
ch(6,'First underbrace: lower cancelled trial retained in position',r'\deleted{l_1^{-1}l_\infty^{-1}\sigma_0}',r'\struck{l_1^{-1} l_\infty^{-1} \sigma_0}',r'\deleted{l_1^{-1}l_\infty^{-1}\sigma_0}','Both minus-one exponents, the first index 1, the infinity index and sigma-zero are legible beneath the first bracket. A separate dark line traverses this lower trial. H puts it only in an editorial note; the manuscript has it immediately below the first bracket.','insertion or placement','expanded_product',mark='yes',cats=(1,6,7))
ch(7,'Second and third underbraces: written substitution labels',r'l_\infty\underbrace{\sigma_1l_1}_{l_\infty^{-1}l_0^{-1}}l_0\underbrace{\sigma_\infty l_\infty}_{l_0^{-1}l_1^{-1}}=1',r'l_\infty\, \underbrace{\sigma_1\, l_1}\, l_0\, \underbrace{\sigma_\infty\, l_\infty} = 1',r'l_\infty\underbrace{\sigma_1l_1}_{l_\infty^{-1}l_0^{-1}}l_0\underbrace{\sigma_\infty l_\infty}_{l_0^{-1}l_1^{-1}}=1','Each of the two right brackets has two l factors below it. The second label has infinity and zero indices; the third has zero and one. All four superscripts are minus one. H describes these labels in an editorial note instead of retaining the source annotations under the brackets.','insertion or placement','expanded_product',cats=(1,3,6))
ch(8,'Right-margin reduction and OK',r'\margin{i.e. $l_\infty^{-1}l_0^{-1}l_1^{-1}=1$\quad OK}',r'\text{i.e.}\qquad l_\infty^{-1}\, l_0\, l_1^{-1}=1\quad\text{ok}',r'\margin{i.e. $l_\infty^{-1}l_0^{-1}l_1^{-1}=1$\quad OK}','The middle l-zero has a detached short minus and upright 1 above and to its right, just as the outer two factors do. The note stands at the right of the product, with capital OK below.','misread symbol or index','margin_relation',cats=(1,3,6),math='The middle factor is l_0^{-1}; H omits its inverse exponent.')
ch(9,'Cancelled prose before boxed identity','On a donc','On a bien','On a donc','The disputed word begins with the tall d stroke and low o, followed by n/c turns. There is no b loop followed by the dotted i required by bien.','misread word','on_a_donc',cats=(2,))
ch(10,'Cancelled prose introducing the sigma identities','on peut en tirer','On peut en déduire','on peut en tirer','The opening o is low rather than a separate large capital. After en, the tall crossed t and dotted i are followed by the short rer sequence. The manuscript reads tirer, not déduire.','misread word','on_peut_tirer',cats=(2,))
ch(11,'Cancelled sigma system: first two row endings',r'\begin{aligned}\sigma_0&=\varepsilon_\infty^{-1}\varepsilon_1\\\sigma_1&=\varepsilon_0^{-1}\varepsilon_\infty\\\sigma_\infty&=\varepsilon_1^{-1}\varepsilon_0\end{aligned}',r'\sigma_0 = \varepsilon_\infty^{-1} \varepsilon_1, \qquad \sigma_1 = \varepsilon_0^{-1} \varepsilon_\infty, \qquad \sigma_\infty = \varepsilon_1^{-1} \varepsilon_0',r'\begin{aligned}\sigma_0&=\varepsilon_\infty^{-1}\varepsilon_1\\\sigma_1&=\varepsilon_0^{-1}\varepsilon_\infty\\\sigma_\infty&=\varepsilon_1^{-1}\varepsilon_0\end{aligned}','The first row ends with the straight subscript 1; the second ends with the two-lobed infinity index. The blank spaces to their right contain no comma. H adds literal commas while arranging the three source rows horizontally.','text not on the page','sigma_relations',cats=(9,))
ch(12,'First live epsilon identity: row ending',r'\varepsilon_0&=\varepsilon_1\varepsilon_\infty\varepsilon_1^{-1}',r'\varepsilon_0 = \varepsilon_1\, \varepsilon_\infty\, \varepsilon_1^{-1},',r'\varepsilon_0&=\varepsilon_1\varepsilon_\infty\varepsilon_{\unsure{1}}^{-1}','The minus-one exponent is the final upper inscription and the blackened index is below the last epsilon. No separate comma follows the factor. The final index retains C-first 1 as a local certainty doubt, independently of the absent comma.','text not on the page','first_live_relation',cats=(9,))
ch(13,'Second live epsilon identity: row ending',r'\varepsilon_1&=\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-1}',r'\varepsilon_1 = \varepsilon_\infty\, \varepsilon_0\, \varepsilon_\infty^{-1},',r'\varepsilon_1&=\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-1}','The final infinity subscript and minus-one exponent are legible. No comma occurs to their right. A yellow/brown fleck between earlier factors is paper discoloration and is not transcribed.','text not on the page','second_live_relation',cats=(9,))
ch(14,'Short graphic divider before Critique',r'\figure{\begin{tikzpicture}\draw (0,0)--(.15,0);\draw (.25,0)--(.8,0);\end{tikzpicture}}','',r'\figure{\begin{tikzpicture}\draw (0,0)--(.15,0);\draw (.25,0)--(.8,0);\end{tikzpicture}}','There are two distinct dark, nearly horizontal strokes separated by a gap; the first is shorter. Their relative lengths and separation are represented by the existing C drawing. H omits the divider.','drawing or diagram','divider',cats=(3,4))
ch(15,'Critique paragraph: first article and noun','les groupes','le groupe','les groupes','The article has its low terminal s turn after the l/e connection. The noun has a final curved s stroke beyond the preceding e. Both forms are plural.','misread word','critique_firstlines',cats=(2,))
ch(16,'Critique paragraph: first discret adjective','discrets','discret','discrets','A separate rightward curved s follows the tall t of the first discrets, before the comma. It is not merely the t crossbar.','misread word','profinis',cats=(2,))
ch(17,'Critique paragraph: groups to be distinguished','des groupes','du groupe','des groupes','At the end of the upper line, the article has d/e/s connected turns rather than du. The next line’s noun ends with the low s hook. The two words read des groupes.','misread word','profinis',cats=(2,))
ch(18,'Critique paragraph: adjective before the dash','profinis','profini','profini','The word ends at a short dotted i. The following blank space continues to the separate dash; there is no terminal s after that i. The singular adjective is preserved after plural groupes.','misread word','profinis',c=True,h=False,cats=(2,9))
ch(19,'Final line: article and noun after pour','les groupes','le groupe','les groupes','The article and noun repeat the plural endings, with low terminal hooks visible after their e forms.','misread word','final_line',cats=(2,))
ch(20,'Final line: adjective before cancelled utiliser',r'\unsure{discrets}','discret','discret','The word ends at the tall t and its crossbar. There is no following s in the blank interval before the cancelled next word. This differs from the distinct terminal s in the earlier discrets.','misread word','final_line',c=True,h=False,cats=(2,9))
ch(21,'Final line: parenthetical continuation after the cancellation',r'(et $\unsure{\bar m|=}$',r'\ill{}',r'(et $\bar m$','An opening parenthesis and the connected e/t strokes precede a straight upper bar with a separate wavy two-humped lower letter. It is barred m, the abbreviation même, rather than two straight equality bars. The parenthesis remains open at the page break.','readable ink left as \\ill{}','final_line',mark='yes',cats=(3,5,8))
ch(22,'Final line: last article','les','le','les','The final small word has a looped l and a low e connection followed by a short dark downward s hook. The manuscript reads les.','misread word','final_line',cats=(2,))
ch(23,'Lower left manuscript page number',r'\mspage{14}','',r'\mspage{14}','A tall 1 with a long rising entry stroke is followed by the angled left arm, crossbar and tall right stem of 4. The complete handwritten number is 14, omitted from H.','omission','footer14',cats=(3,))

# Formal marks only; nested C readings are documented in changes, doubts and notes.
def dec(i,answer,reading,ink,crop,conf='high'):
    z=crops[crop]
    return dict(id=i,decision=answer,reading=reading,ink=ink,crop=z['crop'],box=z['box'],confidence=conf)
decisions=[
 dec('M0808','other','discret','The final t has its own tall stroke and crossbar, followed by blank space before utiliser. No s follows, whereas the earlier discrets has a distinct s.','final_line'),
 dec('M0809','first',r'\bar m','The lower stroke has two curved humps; the straight upper bar is separate. This is the locally observed barred-m abbreviation, not an equality sign.','final_line'),
]
doubts=[
 dict(place='Opening insertion: cancelled stable',reading=r'\deleted{\unsure{stable}}',alternatives=['stable','partly obscured cancelled word'],confidence='low',reason='Dark transverse cancellation masks several small letter strokes; not every letter is plain.'),
 dict(place='Expanded product: first factor',reading=r"\unsure{l_1|l_1'}",alternatives=[r'l_1',r"l_1'"],confidence='medium',reason='A detached short oblique tick lies above/right of the initial factor. Its status as a prime is not decisive; the unprimed C reading remains first.'),
 dict(place='Upper cancelled first-underbrace trial: first index',reading=r'l_{\unsure{1}}\sigma_\infty',alternatives=['1','obscured first subscript'],confidence='medium',reason='The first l is traversed by the local cancellation; a dark lower stroke favors 1 but is partly merged with the crossing.'),
 dict(place='First live epsilon identity: last subscript',reading=r'\varepsilon_{\unsure{1}}^{-1}',alternatives=['1','blackened subscript'],confidence='medium',reason='The final subscript is heavily inked, with a vertical foot compatible with 1. Its upper portion is a dark blot and cannot be recovered more exactly.'),
 dict(place='Final line: cancelled word',reading=r'\deleted{\unsure{utiliser}}',alternatives=['utiliser','partly obscured cancelled ending'],confidence='medium',reason='The u/t/i/l/i sequence is visible; the later connected letters are traversed by the dark strike. The first reading utiliser is retained with local uncertainty.'),
]

inv=[]
def inventory(i,kind,pos,reading,box):
    inv.append(dict(element=f'I{i:02}',kind=kind,position=pos,first_words_or_objects=reading,box=box,sheet_kind='text',hand='his hand',transcribed='yes'))
inventory(1,'deletion','Large crossed block from opening through sigma product','d’ordre fini … sigma_infinity sigma_1 sigma_0=1',[269,15,1654,1285])
inventory(2,'text','First two cancelled baselines','d’ordre fini dans le groupe envisagé … il faudrait donc avoir',[271,15,1654,215])
inventory(3,'insertion','Upper right, attached by curved guide to groupe envisagé',r'\inserted{\deleted{\unsure{stable}} fixé par $\rho$}',[1300,15,1654,135])
inventory(4,'deletion','Inside the upper-right insertion',r'\deleted{\unsure{stable}}',[1300,15,1438,70])
inventory(5,'display','First epsilon product in the crossed block',r'\varepsilon_0\varepsilon_1\varepsilon_\infty=1',[650,211,962,274])
inventory(6,'text','Cancelled introduction to expanded product',r'i.e. en termes des $l_i,\sigma_i$',[279,328,989,390])
inventory(7,'display','Expanded product and three annotated brackets',r"\unsure{l_1|l_1'}\sigma_0l_0\cdots=1",[398,410,1065,650])
inventory(8,'insertion','Upper line under the first bracket',r'\inserted{\deleted{l_{\unsure{1}}\sigma_\infty}}',[466,529,584,589])
inventory(9,'deletion','Local cancellation through upper first-bracket trial',r'\deleted{l_{\unsure{1}}\sigma_\infty}',[466,529,584,589])
inventory(10,'deletion','Lower first-bracket trial',r'\deleted{l_1^{-1}l_\infty^{-1}\sigma_0}',[464,582,659,640])
inventory(11,'margin note','Right of expanded product, with OK below',r'i.e. $l_\infty^{-1}l_0^{-1}l_1^{-1}=1$ OK',[1199,420,1638,559])
inventory(12,'text','Cancelled words before boxed formula','On a donc',[269,644,575,711])
inventory(13,'display','Boxed identity in cancelled block',r'\boxed{\varepsilon_0\varepsilon_1\varepsilon_\infty=1}',[660,666,952,767])
inventory(14,'text','Cancelled prose introducing sigma system','on peut en tirer de plus jolies expressions pour les sigma_i',[295,789,1658,890])
inventory(15,'display','Three cancelled sigma equations',r'\sigma_0=\varepsilon_\infty^{-1}\varepsilon_1;\ \sigma_1=\varepsilon_0^{-1}\varepsilon_\infty;\ \sigma_\infty=\varepsilon_1^{-1}\varepsilon_0',[550,885,890,1110])
inventory(16,'text','Cancelled line after sigma equations','donc aussi la relation inattendue',[278,1118,1230,1192])
inventory(17,'display','Last relation in crossed block',r'\sigma_\infty\sigma_1\sigma_0=1',[590,1216,963,1285])
inventory(18,'text','Live revision on one baseline',r'Sans doute $\varepsilon_0\varepsilon_1\varepsilon_\infty=\sigma_1$',[325,1330,1010,1435])
inventory(19,'text','Left of first live epsilon equation','i.e.',[234,1477,327,1520])
inventory(20,'display','Three live epsilon equations',r'\varepsilon_0=\varepsilon_1\varepsilon_\infty\varepsilon_{\unsure{1}}^{-1};\ \varepsilon_1=\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-1};\ \varepsilon_\infty=\varepsilon_0\varepsilon_1\varepsilon_0^{-1}',[655,1450,1033,1718])
inventory(21,'drawing','Two short strokes before final paragraph','short horizontal stroke, gap, longer horizontal stroke',[260,1787,403,1834])
inventory(22,'text','Five-line final paragraph','Critique des notations et de l’approche. Les éléments … (et barred m pour les',[230,1835,1629,2339])
inventory(23,'deletion','Final line, after discret',r'\deleted{\unsure{utiliser}}',[990,2233,1184,2311])
inventory(24,'text','Lower-left manuscript number','14',[15,2280,105,2356])

second=[]
def box(n,kind,coords,reading):
    second.append(dict(box=f'B{n:02}',kind=kind,coords=coords,reading=reading))
box(1,'Cancelled opening, lexical disagreements and nested insertion/deletion',[271,15,1654,215],r"\deleted{d'ordre fini dans le groupe envisagé \inserted{\deleted{\unsure{stable}} fixé par $\rho$}, il faudrait donc avoir}")
box(2,'Complete cancelled numerical display',[650,211,962,274],r'\deleted{\[\varepsilon_0\varepsilon_1\varepsilon_\infty=1\]}')
box(3,'Cancelled introduction to numerical product',[279,328,989,390],r'\deleted{i.e. en termes des $l_i,\sigma_i$}')
box(4,'Complete expanded product: every numeric index/exponent, bracket, inserted/cancelled trial and prime doubt',[398,410,1065,650],r"\deleted{\[\unsure{l_1|l_1'}\underbrace{\sigma_0l_0}_{\substack{\inserted{\deleted{l_{\unsure{1}}\sigma_\infty}}\\\deleted{l_1^{-1}l_\infty^{-1}\sigma_0}}}l_\infty\underbrace{\sigma_1l_1}_{l_\infty^{-1}l_0^{-1}}l_0\underbrace{\sigma_\infty l_\infty}_{l_0^{-1}l_1^{-1}}=1\]}")
box(5,'Complete margin note and inverse-exponent disagreement',[1199,420,1638,559],r'\margin{i.e. $l_\infty^{-1}l_0^{-1}l_1^{-1}=1$\quad OK}')
box(6,'Cancelled donc disagreement and complete boxed numerical identity',[269,644,969,774],r'\deleted{On a donc\[\boxed{\varepsilon_0\varepsilon_1\varepsilon_\infty=1}\]}')
box(7,'Cancelled tirer disagreement and full introducing sentence',[295,789,1658,890],r'\deleted{on peut en tirer de plus jolies expressions pour les $\sigma_i$}')
box(8,'All three cancelled sigma equations, numeric indices/exponents and H comma additions',[550,885,890,1110],r'\deleted{\[\begin{aligned}\sigma_0&=\varepsilon_\infty^{-1}\varepsilon_1\\\sigma_1&=\varepsilon_0^{-1}\varepsilon_\infty\\\sigma_\infty&=\varepsilon_1^{-1}\varepsilon_0\end{aligned}\]}')
box(9,'End of crossed block and complete last numerical relation',[278,1118,1230,1285],r'\deleted{donc aussi la relation inattendue\[\sigma_\infty\sigma_1\sigma_0=1\]}')
box(10,'Authorial Sans doute and complete numerical revision; H sigma_1 uncertainty',[325,1330,1010,1435],r'Sans doute $\varepsilon_0\varepsilon_1\varepsilon_\infty=\sigma_1$')
box(11,'All live epsilon equations, every numeric index/exponent, blackened index and H comma additions',[234,1450,1033,1718],r'i.e.\[\begin{aligned}\varepsilon_0&=\varepsilon_1\varepsilon_\infty\varepsilon_{\unsure{1}}^{-1}\\\varepsilon_1&=\varepsilon_\infty\varepsilon_0\varepsilon_\infty^{-1}\\\varepsilon_\infty&=\varepsilon_0\varepsilon_1\varepsilon_0^{-1}\end{aligned}\]')
box(12,'Graphic divider omitted by H',[260,1787,403,1834],r'\figure{\begin{tikzpicture}\draw (0,0)--(.15,0);\draw (.25,0)--(.8,0);\end{tikzpicture}}')
box(13,'Opening of critique paragraph and first plural nouns',[230,1835,1609,2064],r"Critique des notations et de l'approche. Les éléments $l_i,\sigma_i,\varepsilon_i,\rho\ldots$ sont dans les groupes")
box(14,'First discrets, des groupes and singular profini disagreements',[232,2050,1540,2240],r"discrets, qu'il faudrait distinguer des groupes profini --- de plus il faudrait")
box(15,'Final lexical endings, resolved C marks, cancelled utiliser and unclosed parenthesis',[231,2230,1629,2339],r'pour les groupes discret \deleted{\unsure{utiliser}} (et $\bar m$ pour les')
box(16,'Handwritten page number omitted from H',[15,2280,105,2356],r'\mspage{14}')

coverage=[]
def dc(n,status,ids=None,explanation=''):
    d=dict(row=n,status=status)
    if ids:d['change_id']=ids[0] if len(ids)==1 else ids
    if explanation:d['explanation']=explanation
    coverage.append(d)
dc(1,'macro/editorial',explanation='The 15 is C’s editorial scan identifier, not a handwritten header number.')
dc(2,'substantive',['s015-01','s015-02','s015-03','s015-04'])
dc(3,'substantive',['s015-03','s015-04'],'The rho/phi alternative is a certainty marker, resolved to rho. The source il is separately distinguished from H’s qu’il.')
for n in [4,5,6]:dc(n,'macro/editorial',explanation='H comma token is the TeX thin-space command \\, between factors, not literal punctuation.')
dc(7,'substantive',['s015-05'],'The upper first-bracket trial contains sigma_infinity and is locally deleted; it is not either C l-factor alternative.')
dc(8,'substantive',['s015-05','s015-06','s015-07','s015-08'],'Token alignment spans the main product, labels moved to H’s editorial note, and the right-margin relation.')
dc(9,'substantive',['s015-06','s015-07'])
dc(10,'substantive',['s015-07'])
dc(11,'macro/editorial',explanation='Alignment artifact caused by the relocated annotations: the main product’s =1 and following i.e. occur in both witnesses.')
dc(12,'substantive',['s015-08'],'The right-margin formula differs at the middle inverse exponent; H’s prose commentary is editorial.')
dc(13,'macro/editorial',explanation='H comment about the location of OK is editorial; the source note is preserved in the margin.')
dc(14,'substantive',['s015-09'])
for n in [15,16]:dc(n,'macro/editorial',explanation='H comma token is \\, spacing within the boxed product.')
dc(17,'substantive',['s015-10'])
dc(18,'macro/editorial',explanation='aligned versus horizontally arranged equations is TeX layout syntax.')
dc(19,'substantive',['s015-11'],'This H comma is literal punctuation after the first sigma equation, unlike its \\, factor spacing.')
dc(20,'substantive',['s015-11'],'Literal H comma after the second sigma equation; absent from the source row ending.')
dc(21,'macro/editorial',explanation='End of the aligned environment only.')
dc(22,'macro/editorial',explanation='The relation itself agrees; the apparent duplicated span comes from H’s editorial cancellation note and thin-space tokens.')
dc(23,'macro/editorial',explanation='H describes the large cancellation in an editorial note; C records that source state with the enclosing deletion macro.')
dc(24,'macro/editorial',explanation='Inline versus display placement of the same Sans doute formula.')
dc(25,'macro/editorial',explanation='Display boundaries; no source text differs at this row. The sigma_1 is readable on its crop.')
dc(26,'macro/editorial',explanation='Display/aligned syntax and placement of i.e. only.')
for n in [27,28]:dc(n,'macro/editorial',explanation='H \\, factor-spacing token, not a comma inscription.')
dc(29,'substantive',['s015-12'],'Literal comma after the first live epsilon equation; absent from the ink.')
for n in [30,31]:dc(n,'macro/editorial',explanation='H \\, factor-spacing token, not a comma inscription.')
dc(32,'substantive',['s015-13'],'Literal comma after the second live epsilon equation; absent from the ink.')
for n in [33,34]:dc(n,'macro/editorial',explanation='H \\, factor-spacing token, not a comma inscription.')
dc(35,'macro/editorial',explanation='End of aligned environment only.')
for n in [36,37,38,39]:dc(n,'substantive',['s015-14'],'C records the two source divider strokes, which H omits. H’s discussion of sigma_1, conjugacy and its added section heading is editorial, not manuscript text.')
dc(40,'macro/editorial',explanation='C \\ldots and H ellipsis represent the same visible trailing dots/dash after rho.')
dc(41,'substantive',['s015-15','s015-16'])
dc(42,'substantive',['s015-17','s015-18'],'The ink combines plural des groupes with singular profini; neither witness supplies the full literal combination.')
dc(43,'substantive',['s015-19','s015-20'],'The ink combines plural les groupes with singular discret; M0808 resolves to that singular.')
dc(44,'substantive',['s015-21'])
dc(45,'substantive',['s015-22','s015-23'],'The final les and the handwritten footer 14 are separate source loci; the number omission is not an editorial marker.')

report=dict(scan=15,reader='/root/reader_a',lines_read=28,
 layout='Upright handwritten sheet with no handwritten number at the head. A large crossed calculation occupies the upper portion, including two opening baselines, a top-right insertion with an earlier cancelled word, epsilon and sigma displays, three lower bracket annotations, and a right-margin i.e. reduction with OK below. Two local first-bracket trials are separately cancelled. A live Sans doute revision and three epsilon equations follow. A two-stroke divider precedes a five-line critique paragraph with one cancelled word and an unfinished parenthesis. Handwritten 14 sits at the lower left. The count includes twenty-four main text/formula baselines, two marginal baselines, the raised opening insertion line and the footer numeral.',
 changes=changes,decisions=decisions,doubts=doubts,inventory=inv,second_boxes=second,
 notation=[
  dict(observation='The product-underbrace upper trial has sigma_infinity, not l_infinity.',places=['First underbrace, upper inserted and locally cancelled line'],qualification='The long horizontal top bar and curved lower body match the page’s sigma forms. The preceding crossed subscript remains uncertain.'),
  dict(observation='Rho is loop-headed with a descending stem.',places=['Opening fixé par rho insertion','Final list l_i, sigma_i, epsilon_i, rho'],qualification='The opening rho/phi choice is resolved from the saved crop; this observation is local to the two occurrences here.'),
  dict(observation='Barred m abbreviates même.',places=['Unfinished final parenthesis'],qualification='The lower letter has two curved humps and is separate from the straight overbar; M0809 resolves to the first alternative.'),
  dict(observation='Sigma and epsilon have visibly different upper forms.',places=['Cancelled sigma system','Sans doute right member','Live epsilon equations'],qualification='Sigma has a broad top bar with a lower curve; epsilon has two curved lobes. The Sans doute right member is clearly sigma_1.'),
  dict(observation='A zero index can join the lower foot of epsilon.',places=['Second cancelled sigma equation','Third cancelled sigma equation'],qualification='The closed round index remains distinguishable from the two-lobed infinity indices on this page.'),
 ],
 hand=[
  dict(habit='A short detached slant near an l can resemble a prime.',places=['First factor of expanded product'],universal_on_page='No; a local ambiguity only.',witness_effect='Both witnesses omit the tick. C-first unprimed l_1 is retained with a possible-prime alternative.'),
  dict(habit='Dark local cancellations must be separated from thin page-wide crossing strokes.',places=['Both first-underbrace trials','Opening stable'],universal_on_page='Observed in these loci.',witness_effect='C omits the upper first-bracket trial’s local deletion; H describes two locally struck trials.'),
  dict(habit='Final singular adjectives can follow visibly plural nouns.',places=['des groupes profini','les groupes discret'],universal_on_page='Two clear local agreement breaks; the earlier discrets is plural.',witness_effect='C supplies s to both later adjectives; H singularizes surrounding nouns and articles as well.'),
  dict(habit='Retracing can blacken a small numeric index.',places=['Last index of first live epsilon equation'],universal_on_page='No; local to the inspected dark subscript.',witness_effect='Both witnesses read 1 without a local ink caveat; the proposed reading retains 1 with uncertainty.'),
 ],
 abbreviations=[
  dict(form='i.e.',expansion='id est',place='Before expanded product, in its right-margin reduction, and before live epsilon equations.'),
  dict(form='OK',expansion='OK',place='Below the right-margin reduction; capitals retained.'),
  dict(form=r'\bar m',expansion='même',place='Final unclosed parenthesis.'),
 ],
 notes=[
  'The upper calculation is cancelled as a block. It first proposes epsilon_0 epsilon_1 epsilon_infinity = 1, expands that expression using l_i and sigma_i, gives bracket substitutions and a marginal inverse-product reduction, then derives three sigma expressions and the claimed unexpected relation sigma_infinity sigma_1 sigma_0 = 1. These are the author’s cancelled calculations; they are preserved rather than presented as established facts.',
  'The subsequent live text begins Sans doute and writes epsilon_0 epsilon_1 epsilon_infinity = sigma_1, followed by three conjugacy-shaped epsilon relations. The right-hand sigma_1 is clear on the crop despite H’s uncertainty. No mathematical inference was used to supply it or the blackened final index of the first following equation.',
  'The final paragraph criticizes the notation and approach because the listed elements belong to discrete groups that should be distinguished from profinite groups. The actual later phrases are des groupes profini and les groupes discret. Both visible agreement breaks are preserved; no s is supplied from grammar. The last parenthesis remains unclosed at the page end.',
  'The C nested uncertainty fixé and the rho/phi alternative in the opening are resolved on the opening crop. Stable remains doubtful under its strike. The first-underbrace upper trial is read l_1 sigma_infinity with a local doubt on the crossed first index and an explicit local deletion; the lower trial l_1^{-1} l_infinity^{-1} sigma_0 is readable and independently struck.',
  'All supplied C deletions and insertions were inspected. The proposed page retains the large cancellation, its opening insertion and cancelled stable, the lower first-bracket cancellation, and the final cancelled utiliser; it adds the separate local cancellation of the upper first-bracket insertion. The final utiliser reading is retained with a new local certainty doubt because its ending is crossed.',
  'The only explicit authorial tentative phrase is Sans doute. No date is present. The manuscript number is 14 at the lower left; it has its own H-omission row and crop. The editorial scan identifier 15 is not source text. The two short divider strokes are reproduced in TikZ.',
  'The source has no commas after the first two sigma equations or after the first two live epsilon equations. H’s four literal equation-separating commas are logged separately from its \\, spacing commands, which are macro differences. H’s explanatory notes and additional section heading are excluded from the source transcription.',
  'The whole sheet and both original-resolution halves were read once, followed by fourteen saved first-reading crops. The last two crops concern previously uncropped equation rows needed to document H’s literal punctuation additions. Every numerical display, insertion, marginal note, cancellation, lexical disagreement and remaining doubt has second-reading box coverage. No OCR, external research, other page, TeX compilation or mathematical check was used.',
 ],check_events=[],diff_coverage=coverage)
out=base/'edition/reader_reports/145_scan015.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'path':str(out),'changes':len(changes),'C_changed':sum(x['c_changed'] for x in changes),'H_changed':sum(x['h_changed'] for x in changes),'decisions':len(decisions),'doubts':len(doubts),'inventory':len(inv),'second_boxes':len(second),'diff_rows':len(coverage),'crops':len(manifest)},ensure_ascii=False))
