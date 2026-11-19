from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
d={'cote':53,'scan':7,'sheet_kind':'text','hand':'his hand','replace':[
(r'\unsure{\Updownarrow|\updownarrow}',r'\Updownarrow'),
(r'\unsure{Ex :|i.e. :}','Ex :'),
(r'\unsure{ess.} de t. f. sur $S$','ess. de t. f. sur $S$'),
(r'\unsure{ext:|est:}','ext:'),
(r'\deleted{\unsure{\forall}}',r'\deleted{\forall}'),
(r'\unsure{k,|k\'|\bar k}',r'\unsure{k,|k\'}'),
(r'B/\unsure{\mathfrak m|m}B','B/mB'),
(r'\unsure{seulement}','seulement'),
(r'\unsure{k|k\'}',r'k'),
(r'\unsure{faits|suits}','faits'),
(r'\unsure{rég.|Alg.} class',r'\unsure{Alg.|rég.} clos'),
(r'U_{\unsure{u|v|\smile}}',r'U_u'),
(r'{\unsure{\mathbb E|E}}^{\unsure{n|h}}_k',r'\mathbb E^n_k'),
], 'review':'Personally read the whole page, both halves, all lines against both witnesses, and enlarged every block, cancellation, insertion and critical formula. Broad crops were viewed at 2×; doubts and differing details at 4–5×. The entire left margin was rotated clockwise 90° and enlarged 3×, including its smaller final note; a second detail was viewed at 5×. Coordinates below refer to the original 1732×2235 image. Crops that accidentally missed a target were replaced and are not relied on. No context was opened.', 'decisions':[], 'inventory':[]}
# Literal primes are represented without a Python escape in the replacement list.
d['replace']=[(a.replace("\\'", "'"),b.replace("\\'", "'")) for a,b in d['replace']]
def a(place,c,h,final,shows,conf='high',cc=False,hc=False,kind='other',marked='no',conseq=None):
 x=dict(place=place,c=c,h=h,final=final,shows=shows,confidence=conf,c_changed=cc,h_changed=hc,kind=kind,marked_in_H=marked)
 if conseq:x['consequential']=conseq
 d['decisions'].append(x)
a('abandoned top line',r'X \unsure{loc.} de type fini sur',r'\struck{\ill{}}','C retained, deleted','X and de type fini sur are readable under the cancellation. The small loc. has a visible looped l but its remainder is crossed. (144,180,789,253), 3×; (271,188,356,241), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('first proposition old qualifiers',r'\deleted{\unsure{localement|loc. noeth}} \deleted{\unsure{noethérien}}',r'\struck{\ill{}}','C retained','Two independently crossed groups precede the inserted régulier. Their fine internal strokes remain obscured. (619,237,780,301), 5×; prop1 (151,208,1713,515), 2×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('first proposition inserted régulier','inserted régulier','described in a note','C retained','The uncancelled word is written above the old qualifiers, with an insertion guide. Prop1, 2×.',hc=True,kind='insertion or placement')
a('first proposition deleted de',r'\deleted{\unsure{de}}',r'\struck{\ill{}}','C retained','The crossed loop and small low stroke do not securely settle the short word. (1069,252,1145,305), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('first proposition abandoned les ann','deleted les ann',r'\struck{\ill{}}','C retained','les and the following a-n-n strokes survive the horizontal cancellation before X soit. Prop1, 2×.',hc=True,kind=r'readable ink left as \ill{}')
a('first corollary equivalence sign',r'\unsure{\Updownarrow|\updownarrow}','omitted',r'\Updownarrow','Two shafts run between the upper and lower arrowheads beside the corollary. Cor1 (149,538,1658,751), 2×.','high',True,True,'misread symbol or index')
a('first corollary hypothesis replacement',r"k' deleted est unsure loc.; inserted ou A",r"k' tensor A uncertain ess.",'C retained','ou A is above the old est loc.; its first letter is a rounded o, followed by u, not a tensor cross. The cancelled loc. remains obscured. Cor1, 2×; (537,634,685,687), 5×.','low',hc=True,kind='insertion or placement',marked='yes',conseq='The alternative is k′ or A of finite type, not a tensor-product hypothesis.')
a('first corollary struck sur',r'\deleted{\unsure{sur}}','sur live','C retained','The small word before k has its own heavy overstrike. (847,633,896,677), 5×.','low',hc=True,kind='deletion state (struck given live or live given struck)')
a('first corollary discarded alternative',r'\deleted{\unsure{ou|{}} A est de t. f. sur k}',r'\struck{A \ill{} de t.f. \ill{}}','C retained','A est de t. f. sur k remains readable under the long strike; the tiny lead-in may be a lost ou or only crossing ink. Cor1, 2×; (989,634,1090,664), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('long left margin opening',r'NB Ne supposons pas X \unsure{ess.|loc.} de t. f. sur k','fragmentary ill. loc. de t.f.','C retained','The upright reading gives Ne supposons pas; the next compact abbreviation has an overwritten loop and two s-like joins. Full margin (17,545,276,1661), clockwise 90°, 3×.','low',hc=True,kind=r'readable ink left as \ill{}',marked='yes')
a('long left margin rewritten condition','deleted Il reste vrai que; inserted Alors si','omitted','C retained','The old phrase is crossed on its baseline; Alors si is written immediately above it. Full rotated margin, 3×.',hc=True,kind='omission')
a('long left margin extension','tt extension inserted finie; deleted de la base; corps de base','fragmentary extensions radicielles','C retained','finie is a small interlinear insertion. The old de la base is struck; corps de base remains on the following baseline. No radicielles is written in this note. Full rotated margin, 3×.',hc=True,kind='misread word')
a('long left margin second condition',r'deleted alors; pour tt Y \unsure{ess.} de t. f. sur S','omitted','deleted alors; pour tt Y ess. de t. f. sur S','The second ess. has separate low e-s-s strokes and a dot. The base letter is a clear capital S. Full rotated margin, 3×.','medium',True,True,'omission')
a('long left margin conclusion','Y régulier implies X×_kY régulier; On dit que X est géom régulier','ill.; tensor with k prime','C retained','The product sign is a cross with subscript k and following Y, and the underlined régulier and final naming sentence are readable. Full rotated margin, 3×.',hc=True,kind=r'readable ink left as \ill{}',conseq='The marginal conclusion concerns X×_kY; its hypotheses and terminology are retained in full.')
a('small left margin label',r'\unsure{Ex :|i.e. :}','omitted','Ex :','A large E and separate x are followed by two dots. (179,1235,246,1604), clockwise 90°, 5×.','high',True,True,'omission')
a('small left margin last word',r'ext. de corps underlined \unsure{alg.|sép.}','omitted','C retained','The short final word is underlined; the superposed loops and descending final stroke do not distinguish alg. from sép. securely. Same rotated crop, 5×.','low',hc=True,kind='omission')
a('second proposition inserted qualification','ess loc de t. f.','ess. loc. de t.f.','C retained','The inserted ess loc is compact, without the added terminal periods after these two words. Equiv (152,772,1665,1130), 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
a('second proposition unusual repeated k',r'k, k, \unsure{ext:|est:} parfait','k, k ext. uncertain parfait','k, k, ext: parfait','The middle letter consists of two crossing strokes, followed by a tall t and two vertically separated dots. The repeated k is retained. (677,812,807,857), 5×.','high',True,True,'misread word','yes')
a('condition c deleted quantifier',r'\deleted{\unsure{\forall}}',r'\struck{\forall}',r'\deleted{\forall}','Both sloping legs and the crossbar of the quantifier survive its cancellation. (273,1000,317,1047), 5×.','high',True)
a('condition c base subscript',r'\unsure{k,|k\'|\bar k}',r'\bar k',r'\unsure{k,|k\'}','A k is followed by a separate low comma-like stroke; no bar appears above it. Its low position still leaves k-comma versus a displaced prime uncertain. (365,1019,404,1068), 5×.','low',True,True,'misread symbol or index',conseq='The base subscript is left doubtful; the ink does not support H’s certain barred k.')
a('condition d deleted extension letter',r'\deleted{\unsure{k\'}}',r'\struck{\ill{}}','C retained','The large k-like strokes and a raised diagonal remain crossed densely. (586,1072,638,1113), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('conditions implication diagram','a→b, b→c and bent b→d, all double arrows, left grouping curve','described in a note','C diagram retained','All three heads, the bent right path from b to d and the separate grouping curve are visible in the enlarged conditions. Equiv, 2×; full rotated margin, 3×.',hc=True,kind='drawing or diagram')
a('proof first arrow and hom abbreviation',r'b)\to a); hom raised t','b) implies a); hom.','C retained','The b-to-a arrow has one shaft. A small raised t stands after hom. Proofdef (196,1126,1710,1303), 2×.',hc=True,kind='misread symbol or index')
a('proof quotient ideal letter',r'B/\unsure{\mathfrak m|m}B',r'B/\mathfrak m B','B/mB','The handwritten m is a plain two-humped letter, with no doubled or angular gothic strokes. (1450,1131,1521,1171), 5×.','medium',True,True,'misread symbol or index')
a('proof added conclusion',r'inserted \Rightarrow B régulier','ellipsis only','C retained','The double right arrow and B régulier are written between the first and second proof lines. Proofdef, 2×.',hc=True,kind='omission',conseq='The first local flatness argument has its written conclusion B regular.')
a('proof second local rings','m over A and n over B','A and B without local ideal labels','C retained','Small m and n are positioned directly above the respective ring letters. Proofdef, 2×.',hc=True,kind='omission')
a('proof second flatness hypothesis','hom local plat','hom. local uncertain fid. plat','C retained','There is no intervening fid. between local and plat; the crowded interlinear text above is the preceding inserted conclusion. Proofdef, 2×.',hc=True,kind='text not on the page',marked='yes')
a('proof short connective',r'\unsure{ds|des}',r'\ill{}','C retained','The ascender and final s-like stroke are visible, but the middle join could conceal a compressed e. (1296,1171,1359,1217), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('proof limit phrase',r'par \unsure{principe} de limite','uncertain par passage à la limite','C retained','The first word after par starts prin... and ends with compact raised strokes; de limite is legible. It is not the long word passage. (637,1206,722,1251), 5×; proofdef 2×.','low',hc=True,kind='misread word',marked='yes')
a('definition cancellation state and est','On dit alors que X est géom. régulier','On dit deleted alors que X géom. régulier','C retained','alors que remains on its own baseline. The apparent overlying stroke is the d⇒c proof written above, not a cancellation through these words. est appears between X and géom. Proofdef, 2×; (436,1219,845,1261), 4×.',hc=True,kind='deletion state (struck given live or live given struck)')
a('first consequence deleted subscript',r'X\deleted{\unsure{{}_k|{}_x}}','X only','C retained','A small crossed group lies at the lower right of X; its original k/x is still unclear. (222,1333,281,1375), 5×.','low',hc=True,kind='omission')
a('first consequence intermediate lisse','deleted géom régulier, deleted lisse, inserted géom régulier','deleted géom régulier then inserted géom régulier','C retained','The earlier lisse is written above the crossed original wording and is itself struck. Middle (198,1306,1700,1739), 2×.',hc=True,kind='omission')
a('first consequence parenthesis',r'ou \unsure{seulement} pour tt X=Spec k prime','on uncertain prenant X=Spec k prime','ou seulement pour tt X=Spec k prime','The line begins ou, then the sequence seul...ment, and the separate pour tt before X. (909,1353,1050,1389), 4×; middle 2×.','medium',True,True,'misread word','yes')
a('base change earlier terminology','deleted géom rég; deleted lisse; inserted géom rég','deleted lisse; inserted géom rég','C retained','The original géom rég on the baseline is crossed as well as the smaller lisse above it. Middle, 2×.',hc=True,kind='omission')
a('product assertion beginning','X et Y','deleted Si X et Y','C retained','The line starts with X; there is no Si to its left. Middle, 2×.',hc=True,kind='text not on the page')
a('product assertion older terminology','deleted géom réguliers; deleted lisse; inserted géom rég','deleted lisses; inserted géom rég','C retained','The longer original wording is still visible under the line. The smaller lisse has no separately visible final s. Middle, 2×.',hc=True,kind='omission')
a('pointwise definition heading','X ...','NB X ...','C retained','The NB is at the right margin beside the next statement, not a heading before this X. Middle, 2×.',hc=True,kind='insertion or placement')
a('pointwise definition deleted word',r'\deleted{\unsure{lisse}}',r'\struck{\ill{}}','C retained','The initial tall loop and final small strokes are overlapped by dense cancellation. (282,1680,334,1718), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('pointwise definition base',r'\unsure{k|k\'}','k','k','The k after the slash has a looped tall stem and low right branch, with blank space above and to the right: no prime. (588,1665,670,1721), 5×.','high',True)
a('pointwise facts sentence',r'\unsure{faits|suits} analogues aux précédents','uncertain résultats analogues au précédent','faits analogues aux précédents','The word has a short f, rounded a, dotted i and crossed t; aux and the plural ending of précédents are visible. (342,1719,492,1756), 4×; middle 2×.','high',True,True,'misread word','yes')
a('cancelled theorem open locus','est ouvert',r'est \ill{}','C retained','The o-u-v-e-r-t strokes remain visible above and below the single horizontal cancellation. Theorem (202,1718,1680,1869), 2×.',hc=True,kind=r'readable ink left as \ill{}')
a('cancelled theorem parenthesis and deleted X',r'(On ... où \deleted{\unsure{$X$}} k ...)',r'[On ... où k ...]','C retained','Round opening and closing parentheses surround the explanation. A dense independently crossed X-like group precedes k. (759,1796,821,1857), 5×; theorem 2×.','low',hc=True,kind='omission')
a('cancelled theorem i.e. fragment',r'\unsure{(i.e.|(}',r'(\ill{}','C retained','The opening curve is clear; a few low traces remain on the heavy strike before the equality sign, insufficient to settle i.e. (1108,1791,1259,1858), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('cancelled theorem final words',r'\unsure{rég.|Alg.} class','alg. clos',r'\unsure{Alg.|rég.} clos','The first group has a large loop and descending g-like stroke, favoring Alg. but still crossed. The following word has c, tall l, low o and final s, not a second a. (1253,1788,1477,1868), 5×.','low',True,True,'misread word')
a('Jacobian criterion label','inserted (Critère jacobien)','uncertain (Critère jacobien) inline','C retained','The parenthetical label is written above the proposition heading and is readable throughout. Criterion (201,1841,1662,2101), 2×.',hc=True,kind='insertion or placement',marked='yes')
a('Jacobian criterion live est','est deleted géom régulier inserted lisse','deleted est géom régulier inserted lisse','C retained','The stroke above est is the curved insertion guide for loc de t f sur k; the separate cancellation starts at géom and crosses that phrase. (359,1873,745,1952), 5×.',hc=True,kind='deletion state (struck given live or live given struck)')
a('Jacobian criterion point','en x in X','en x','C retained','The membership sign and second X are written as a small raised addition next to x. Criterion, 2×.',hc=True,kind='omission')
a('Jacobian criterion inserted integer','inserted entier n≥0 et','inserted uncertain voisinage ouvert U et un','C retained','The insertion reads entier, then n≥0, then et; the inequality and 0 are clear. Criterion and theorem crops, 2×.',hc=True,kind='misread word',marked='yes',conseq='The insertion specifies an integer n≥0; it does not insert another neighbourhood U.')
a('Jacobian criterion source subscript',r'U_{\unsure{u|v|\smile}}','U',r'U_u','The small character below U has an upright left and rounded rising right side, a u rather than a v or bare smile. (328,1992,355,2027), 5×.','medium',True,True,'omission')
a('Jacobian criterion target',r'{\unsure{\mathbb E|E}}^{\unsure{n|h}}_k','E^n_k',r'\mathbb E^n_k','The E has a second parallel left stroke; the raised letter has one arch with no ascender, n. Subscript k is clear. (431,1941,516,2019), 5×.','high',True,True,'misread symbol or index')
a('Jacobian criterion étale quotes','double quotation strokes','guillemets','C retained','Two short strokes at each side of étale, with no angled guillemet form. Criterion, 2×.',hc=True,kind='other')
a('Jacobian criterion presentation phrase','loc. en prés. finie','loc. de prés. finie','C retained','The small word has an e-loop and final n, with no tall d stem. Criterion, 2×.',hc=True,kind='misread word')
d['unresolved']='Abandoned loc.; first proposition old local/noetherian qualifiers and de; cancelled corollary loc., sur and possible ou; first marginal ess./loc. and final alg./sép.; condition c low comma/prime and condition d cancelled k′; proof ds/des and compressed principe; deleted X subscript; pointwise cancelled lisse; cancelled theorem X, (i.e./( and Alg./rég. The marginal S and the repeated k, ext: are preserved as written.'
d['inventory']=[
['deletion','top abandoned line','X loc. de type fini sur'],
['text','first proposition','Prop Soit X schéma'],
['deletion','first proposition old qualifier','localement/loc. noeth'],
['deletion','first proposition second qualifier','noethérien'],
['insertion','above first proposition','régulier'],
['deletion','before parfait','de'],
['deletion','before X soit','les ann'],
['display','beside first corollary','double vertical equivalence arrow'],
['text','first corollary','Soit A un anneau local régulier'],
['deletion','first corollary hypothesis','est loc.'],
['insertion','above hypothesis','ou A'],
['deletion','first corollary before k','sur'],
['deletion','first corollary discarded alternative','ou A est de t. f. sur k'],
['margin note','left sideways','NB Ne supposons pas X ess./loc.'],
['deletion','left margin old connective','Il reste vrai que'],
['insertion','left margin replacement','Alors si'],
['insertion','left margin extension','finie'],
['deletion','left margin base phrase','de la base'],
['deletion','left margin before pour tt','alors'],
['margin note','left small sideways','Ex : ext. de corps alg./sép.'],
['text','second proposition','X schéma ... Conditions équivalentes'],
['insertion','above second proposition','ess loc de t. f.'],
['diagram','conditions a to d','universal Y; extensions k prime; c base index; finite radicial extensions'],
['deletion','condition c','forall'],
['deletion','condition d','k prime'],
['text','proof first implication','Dém b→a'],
['insertion','proof first homomorphism','plat'],
['insertion','between proof lines','implies B régulier'],
['text','proof second implication','c implies b'],
['text','proof third implication','d implies c par principe de limite'],
['text','definition','On dit alors que X est géom. régulier'],
['text','first consequence','X ... implies X régulier'],
['deletion','first consequence X subscript','k/x'],
['deletion','first consequence original wording','géom régulier'],
['deletion','first consequence intermediate wording','lisse'],
['insertion','first consequence final wording','géom régulier'],
['display','base change equivalence','X géom rég/k iff X_k prime géom régulier'],
['deletion','base change original wording','géom rég'],
['deletion','base change intermediate wording','lisse'],
['insertion','base change final wording','géom rég'],
['display','product consequence','X et Y ... implies X×_kY'],
['deletion','product original wording','géom réguliers'],
['deletion','product intermediate wording','lisse'],
['insertion','product final wording','géom rég'],
['text','pointwise definition','X géom. régulier/k en un point'],
['deletion','pointwise definition','lisse'],
['insertion','right above pointwise definition','ou underlined O_X,x est géom rég'],
['text','following pointwise definition','On a les faits analogues aux précédents'],
['margin note','right of pointwise definition','NB Si k(x) est séparable sur k'],
['deletion','cancelled theorem and explanation','L’ens des pts de X ... ouvert'],
['deletion','inside cancelled explanation','X'],
['text','Jacobian criterion','Prop X ... est lisse'],
['insertion','above proposition heading','Critère jacobien'],
['insertion','above criterion hypothesis','loc de t f sur k'],
['deletion','criterion original terminology','géom régulier'],
['insertion','criterion replacement','lisse'],
['insertion','criterion morphism','entier n≥0 et'],
['display','criterion map','f:U_u→double-stroked E^n_k'],
['text','criterion map qualification','U vois. ouvert de x ... fibres étales'],
['text','final corollary','L’ens des pts où X est lisse'],
['deletion','final corollary','géom'],
]
runpy.run_path(str(root/'scripts/review.py'))['commit'](d)
