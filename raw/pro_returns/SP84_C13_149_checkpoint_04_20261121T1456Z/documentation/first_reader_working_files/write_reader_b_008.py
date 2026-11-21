from pathlib import Path
import json
out=Path('edition/reviews');out.mkdir(parents=True,exist_ok=True)
boxes=json.loads(Path('/tmp/reader_b_008_boxes.json').read_text())
tex=r'''\scanpage{8}
des corps vers les proobjets idoines, \unsure{va|vont} avoir toutes les propriétés de fidélité du foncteur $K-B_K$, ou $K-\Pi_K$, ou $(K,\bar K)-\Gamma_{\bar K/K}$, \uline{restreint} aux corps \inserted{absolument} de type fini, auxquels nous allons par la suite nous borner, la plupart du temps. Mais il sera nécessaire, au cours du travail, de donner une description \inserted{purement} algébrique, p.ex., du pro-pro-groupe \unsure{fini} associé p.ex. à $\mathbb C$ (plus précisément, à $(\mathbb C,\mathbb C)$ !).

Le rôle dominant sera joué par le corps premier de car. $0$, $\mathbb Q$, donc par $B_{\mathbb Q}$ et $\Pi_{\mathbb Q}$, qui a un objet canonique, noté $\overline{\mathbb Q}_0$ -- la clôture alg. de $\mathbb Q$ dans $\mathbb C$. On pose.
\[
(5)\qquad \Gamma_{\mathbb Q}=E_{\overline{\mathbb Q}_0/\mathbb Q}
\]
\margin{et on écrira \inserted{souvent} $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ au lieu de $E_{\overline{\mathbb Q}/\mathbb Q}$, pour une clôture alg. quelq. $\overline{\mathbb Q}$ de $\mathbb Q$}
Pour tt corps $K$ de car. $0$ -- en particulier pour les corps $K$ de type fini sur $\mathbb Q$, aux-
\margin{7}
'''
(out/'149_scan008.tex').write_text(tex,encoding='utf-8')
def crop(k):return 'crops/149_scan008_'+k+'.png'
changes=[]
def ch(i,p,C,H,f,e,k,conf='high',ac=False,ah=True,kind='misread word',cat='Words',mh=False,math=False):
 changes.append(dict(id=i,place=p,C=C,H=H,final=f,evidence=e,crop=crop(k),box=boxes[k],confidence=conf,against_C=ac,against_H=ah,kind=kind,error_category=cat,marked_in_H=mh,mathematical=math))
ch('c01','Main line 1, after les','proobjets',r'\ill{}','proobjets','Initial p descends; compact r/o are followed by a tall b, a descending j, then e/t and a terminal s. The word is present and no internal hyphen is visible.','c01',kind=r'readable ink left as \ill{}',cat='Readable ink left as illegible',mh=True)
ch('c02','Main line 1 ending','va','vont',r'\unsure{va|vont}','The initial v and a low rounded following part are visible. The final crossing/return could belong to the a finish or to a very compressed nt; its sequence is not clean enough to settle va against vont. No independent strike through the entire word is visible.','c02',conf='medium')
ch('c03','Main line 3 opening','du foncteur','des foncteurs','du foncteur','The short article has a d ascender with a low u finish. The noun ends in the single r return with clear space before K; neither a final plural s nor a separate s in the article is present.','c03')
ch('c04','Main line 3, first map',r'$K\unsure{-|\longrightarrow}B_K$',r'$K\mapsto B_K$',r'$K-B_K$','The sign is one shallow horizontal shaft with a thick downward finish. There is no two-wing head and no initial upright; B and low K remain visible.','c03',kind='misread symbol or index',cat='Symbols and indices',math=True)
ch('c05','Main line 3, between maps','ou','(nothing)','ou','Between the comma after B_K and the next K there is a small separated o-like mark and a low curved u finish. These are a word, not part of either map shaft.','c03',kind='omission',cat='Omissions')
ch('c06','Main line 3, second map',r'$K\unsure{-|\longrightarrow}\Pi_K$',r'$K\mapsto\Pi_K$',r'$K-\Pi_K$','The second sign is an unheaded shaft, ending in a rounded dark tip. No left bar is present. Pi has a roof over two downstrokes.','c03',kind='misread symbol or index',cat='Symbols and indices',math=True)
ch('c07','Main line 4 opening','ou','(nothing)','ou','A small o-like beginning and extended low u occupy the opening of the row before the parenthesis. They match the preceding line’s small ou.','c04',kind='omission',cat='Omissions')
ch('c08','Main line 4, third map',r'$(K,\bar K)\unsure{-|\longrightarrow}\Gamma_{\bar K/K}$',r'$(K,\overline K)\mapsto\Gamma_{\overline K/K}$',r'$(K,\bar K)-\Gamma_{\bar K/K}$','The complete formula shows a bar on the second K in the pair and on the first subscript K. Its map sign is a slightly rising shaft with a small end thickening, without a discernible head or initial bar. Gamma has one descending stem under its roof.','c04',kind='misread symbol or index',cat='Symbols and indices',math=True)
ch('c09','Main line 4, underlined word',r'\uline{restreint}','restreints',r'\uline{restreint}','The word ends with a high angled t return; the area after it is clear before aux. There is no additional terminal s. A separate line under the word is an underline.','c04')
ch('c10','Main line 6, after borner,','la plupart','le plus souvent','la plupart','The article is a looped l with a small a finish. The following word has two p descenders separated by lu, then art; it is one word, with no separate souvent.','c05')
ch('c11','Main line 7, before cours','au','en','au','Two short low connected/adjacent curves precede cours; the initial lacks the interior loop of an e and the second has the low u form.','c06')
ch('c12','Insertion before algébrique',r'\inserted{purement}',r'\add{précisément}',r'\inserted{purement}','The insertion starts with p/u/r, followed by e and the compact ment ending. There is no accent or dotted i in the body; the word is much shorter than précisément. Its curved leader ends before algébrique and does not cancel either word.','c07')
ch('c13','Main line 9, article before pro-pro-groupe','du','des','du','A d loop/ascender joins a low u. No distinct terminal s is present before the first pro.','c08')
ch('c14','Main line 9, compound and final crowded adjective',r'pro-pro-groupe \unsure{fini}','pro-groupes profinis',r'pro-pro-groupe \unsure{fini}','Two clearly written pro components precede groupe, separated by short hyphens. Groupe has no visible plural s. A separate tall f begins the following word close to the paper edge; compressed low strokes and a last dot support fini, but the internal ni sequence is not completely separable, so C’s doubt remains. A tiny isolated point above the first hyphen is recorded in notes as an unassigned ink point rather than expanded into invented punctuation.','c08',conf='medium')
ch('c15','Main line 10 opening','associé','associés','associé','The final é has its detached accent and a low terminal finish, followed by blank space before p.ex. There is no plural s.','c09')
ch('c16','Main line 13 ending','donc','dont','donc','The d has a loop and ascender, followed by compact on; the terminal is a low open c-shaped curl, without the upright/cross of t.','c10')
ch('c17','Main line 14 opening','par','le','par','A long p descender precedes the low joined a/r segment. There is no tall l and no e-shaped loop.','c11')
ch('c18','Main line 16 ending','On pose','On posera','On pose.','After On, the word has p, low o, curved s and the final e; there is no following ra. A separate dark round stop stands to its right.','c12',ac=True)
ch('c19','Marginal note, after alg.',r'\unsure{quelc.|quelq.}','quelconque','quelq.','The abbreviated word starts with a long descending q, then u/e and a tall l. The terminal rounded letter has its own short descending stroke, supporting q rather than c; an independent final point follows. The full word quelconque is not written.','c13',ac=True,kind='abbreviation expanded or spelling modernised',cat='Abbreviations expanded, spelling modernised')
ch('c20','Bottom-left foliation',r'\margin{7}','(nothing)',r'\margin{7}','Small thin 7 with a long downstroke and a crossing bar at the lower-left paper edge. Its scale and hand are distinct from the main notes; retain as marginal foliation, not an authorial page heading.','c15',kind='omission',cat='Omissions')
ch('c21','Marginal note, small intervening word',r'\inserted{souvent}','souvent',r'\inserted{souvent}','Souvent sits as a smaller added line in the gap below écrira and above the first Gamma formula. Its position and reduced size mark insertion into et on écrira ... Gamma; there is no cancellation.','c13',kind='insertion or placement',cat='Insertions put in the wrong place')
decisions=[]
def dec(i,d,r,e,k,conf):decisions.append(dict(id=i,decision=d,reading=r,evidence=e,crop=crop(k),box=boxes[k],confidence=conf))
dec('M0969','first','-','First map shaft is unheaded, with no separate return wing or initial bar. Whole neighboring formula row inspected.','c03','high')
dec('M0970','first','-','Second map shaft has a rounded end, not an arrowhead. Capital Pi and its K index are visible.','c03','high')
dec('M0971','first','-','Third map’s slightly rising shaft ends in a downturned thickening; no formed arrowhead or mapsto bar is visible. Whole pair and target subscript inspected.','c04','high')
dec('M0972','undecided',r'\unsure{fini}','The f and compressed final dotted stroke are visible at the sheet edge. The internal short strokes cannot be separated firmly enough to resolve the whole word.','c08','medium')
dec('M0973','alternative','quelq.','The terminal rounded letter has a short descending stroke before the separate full stop; it is q rather than open c. The entire word is abbreviated.','c13','high')
inv=[]
def elem(i,kind,pos,first,hand='main manuscript hand'):inv.append(dict(scan=8,sheet_kind='text',hand=hand,element=i,kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
elem('e01','text','main lines 1–11, upper paragraph','des corps vers les proobjets idoines')
elem('e02','insertion','above line 5; attached before de type','absolument')
elem('e03','insertion','above line 9; attached before algébrique','purement')
elem('e04','text','main lines 12–16, middle paragraph','Le rôle dominant sera joué')
elem('e05','display','main line 17, formula (5)',r'(5) \Gamma_{\mathbb Q}=E_{\overline{\mathbb Q}_0/\mathbb Q}')
elem('e06','margin note','lower-right, beside formula (5), five principal lines','et on écrira')
elem('e07','insertion','between écrira and the first Gamma formula in the margin','souvent')
elem('e08','text','main lines 18–19, bottom paragraph fragment','Pour tt corps K de car. 0')
elem('e09','margin note','bottom-left foliation','7','another or uncertain hand; smaller, thin foliation')
margin=r'et on écrira \inserted{souvent} $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ au lieu de $E_{\overline{\mathbb Q}/\mathbb Q}$, pour une clôture alg. quelq. $\overline{\mathbb Q}$ de $\mathbb Q$'
audit=[]
def ab(i,k,b,r):audit.append(dict(box=i,kind=k,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=r))
ab('b01','different word / H illegible',boxes['c01'],'proobjets')
ab('b02','different word with retained doubt',boxes['c02'],r', \unsure{va|vont}')
ab('b03','complete formula row with two C marks and differing prose',boxes['c03'],r'du foncteur $K-B_K$, ou $K-\Pi_K$,')
ab('b04','complete formula with C mark, omitted ou and singular restreint',boxes['c04'],r'ou $(K,\bar K)-\Gamma_{\bar K/K}$, \uline{restreint} aux corps')
ab('b05','insertion and adjacent de type',[235,521,611,651],r'\inserted{absolument} de type')
ab('b06','different words',boxes['c05'],'la plupart du')
ab('b07','different word with following context',boxes['c06'],'au cours')
ab('b08','insertion and attachment before algébrique',boxes['c07'],r'\inserted{purement} algébrique')
ab('b09','different article/compound and unresolved C word',boxes['c08'],r'du pro-pro-groupe \unsure{fini}')
ab('b10','different word ending',boxes['c09'],'associé')
ab('b11','different word',boxes['c10'],'donc')
ab('b12','different word',boxes['c11'],'par')
ab('b13','different word and missing stop',boxes['c12'],'On pose.')
ab('b14','complete marginal note including both formulas and insertion',boxes['c13'],r'\margin{'+margin+'}')
ab('b15','separate small insertion in margin',[1396,1967,1598,2013],r'\inserted{souvent}')
ab('b16','whole display including handwritten 5 and subscript zero',boxes['c14'],r'(5)\qquad \Gamma_{\mathbb Q}=E_{\overline{\mathbb Q}_0/\mathbb Q}')
ab('b17','first inline handwritten characteristic zero',[865,1514,1188,1614],r'de car. $0$,')
ab('b18','named closure with handwritten zero index',[864,1774,1004,1871],r'$\overline{\mathbb Q}_0$')
ab('b19','second inline handwritten characteristic zero',[898,2184,1141,2256],r'de car. $0$')
ab('b20','thin smaller-hand foliation',boxes['c15'],r'\margin{7}')
coverage=[
(1,'editorial-only','','Scan 8 is metadata, not written source.'),
(2,'material','c01','The word proobjets is readable.'),
(3,'material','c02','va is favored, but the compressed terminal crossing keeps vont as an alternative.'),
(4,'material','c03','Singular du foncteur is written.'),
(5,'material','c04','First map is an unheaded shaft.'),
(6,'material','c05','The first ou is present.'),
(7,'material','c06','Second map is an unheaded shaft.'),
(8,'material','c07','The second ou is present.'),
(9,'material','c08','Third map is an unheaded shaft.'),
(10,'material','c09','Underlined singular restreint has no final s.'),
(11,'material','c10','The source reads la plupart.'),
(12,'material','c11','The word is au.'),
(13,'material','c12','Inserted purement is written.'),
(14,'material','c13','The article is du.'),
(15,'material','c14','The two pro components and singular groupe are written; fini remains doubtful. Singular associé is separately logged at c15.'),
(16,'material','c16','donc is written; following par is separately cropped and logged at c17.'),
(17,'material','c18','The word is pose, followed by a visible stop.'),
(18,'material','c19','The abbreviated form ends in descending q and a stop: quelq.'),
(19,'material','c20','Small foliation 7 is present.')]
obj=dict(scan=8,reader='/root/reader_b',lines_read=28,changes=changes,decisions=decisions,inventory=inv,
notes=[
 'Scan 008 begins in mid-sentence and ends with the literal broken word aux-. Its small bottom-left foliation is 7 in a thinner, smaller, another or uncertain hand. No date or title is present. Nineteen principal text/display lines, five marginal-note lines, three inserted lines, and the foliation were inspected (28 line units).',
 'The first paragraph discusses the fidelity properties expected for the construction restricted to absolutely finite-type fields and calls for a purely algebraic description of the pro-pro-group associated to C. These are statements being transcribed, not proof checks.',
 'The next paragraph gives the rational field a dominant role, names its algebraic closure inside C as Q-bar with subscript zero, and defines Gamma_Q by formula (5). The right margin says Gamma_{Q-bar/Q} will often replace E_{Q-bar/Q} for an arbitrary algebraic closure. The last paragraph begins the characteristic-zero case.',
 'Source singulars and abbreviations are preserved: du foncteur, restreint, du pro-pro-groupe, associé, tt and quelq. The opening verb stays va|vont because the terminal return is crowded; no grammatical inference settles it. The formula shafts are read by their ink, without supplying arrowheads from their intended mapping role.',
 'There are no definite cancellations. The crossing at the end of va/vont is not treated as a deletion because it cannot be isolated from the word’s terminal letter strokes. The leaders under absolument and purement attach the insertions before de type and algébrique respectively.',
 'At the right edge after pro-pro-groupe, the final adjective is compressed but some ink survives to a dotted terminal stroke. Fini remains a whole-word doubt rather than a silently completed edge word. A very small isolated point stands above the first compound hyphen; it has no secure letter or punctuation attachment and is left as an unassigned ink point, not transcribed as a new symbol.',
 'In formula (5) the Gamma stem is retraced with close parallel uprights; its right roof does not descend as Pi would. Plain Gamma agrees with its two other locally visible occurrences. This is a letter-shape comparison, not a mathematical verification.'
],checks=[],hand=[
 dict(habit='Map shafts can be written as short unheaded horizontal strokes ending in a downturned pen finish.',pages=[8],consistency='All three map signs on this leaf have the same form, without an initial upright or two-wing arrowhead.',misread='H supplies mapsto throughout; C marks each as dash/arrow.'),
 dict(habit='Low o/u can be reduced to a small point followed by a horizontal curved finish.',pages=[8],consistency='Both occurrences of ou between the maps.',misread='H omits both words.'),
 dict(habit='A curved leader below a small added word turns down at its left into the insertion point.',pages=[8],consistency='Both absolument and purement, with separate inserted souvent lacking this leader.',misread='No placement error found for the first two; H reads purement as précisément and leaves souvent without insertion state.'),
 dict(habit='The terminal q of the abbreviated quelq. has a short descending tail.',pages=[8],consistency='Only one abbreviation occurrence on this leaf, so no broader consistency claim.',misread='C has quelc.|quelq.; H expands to quelconque.'),
 dict(habit='Gamma can have a closely retraced stem, while Pi has two widely separated roof supports.',pages=[8],consistency='Gamma in formula (5) compared with the inline and marginal Gamma; Pi in both inline and lower-paragraph occurrences.',misread='No witness letter swap found; prevents misreading the retraced Gamma as Pi.'),
],notation=[
 dict(written='Gamma with subscript bar K/K',rendering=r'\Gamma_{\bar K/K}',meaning='group symbol in the third map expression',evidence='Main line 4; one stem and rightward roof; bar over first subscript K only.'),
 dict(written='Q-bar with low zero',rendering=r'\overline{\mathbb Q}_0',meaning='canonical algebraic closure of Q inside C, as stated',evidence='Main line 15 and formula (5).'),
 dict(written='Gamma_Q = E_{Q-bar-zero/Q}',rendering=r'\Gamma_{\mathbb Q}=E_{\overline{\mathbb Q}_0/\mathbb Q}',meaning='definition labeled (5)',evidence='Entire display crop c14, including both equality strokes and index zero.'),
 dict(written='Gamma_{Q-bar/Q}',rendering=r'\Gamma_{\overline{\mathbb Q}/\mathbb Q}',meaning='notation used often in place of E for an arbitrary algebraic closure',evidence='Explicit wording in the right margin.'),
],abbreviations=[
 dict(form='p.ex.',expansion='par exemple',place='main lines 9 and 10'),
 dict(form='car.',expansion='caractéristique',place='main lines 13 and 18'),
 dict(form='alg.',expansion='algébrique',place='main line 15 and marginal note'),
 dict(form='quelq.',expansion='quelconque',place='marginal note'),
 dict(form='tt',expansion='tout',place='main line 18'),
],doubts=[
 dict(place='main line 1 ending',reading='va',alternatives=['vont'],confidence='medium',reason='Compressed final crossing/return does not cleanly separate a from nt.'),
 dict(place='main line 9 at right paper edge',reading='fini',alternatives=[],confidence='medium',reason='Tall f and dotted terminal stroke visible, but internal short strokes crowded; C whole-word doubt retained.'),
],audit_boxes=audit,diff_coverage=[dict(row=n,classification=c,change_id=i,reason=r) for n,c,i,r in coverage])
(out/'149_scan008.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote 008 TEX/JSON:',len(changes),'changes,',len(decisions),'marks,',len(audit),'audit boxes,',len(coverage),'difference rows.')
