from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
d={'cote':53,'scan':5,'sheet_kind':'text','hand':'his hand','replace':[
(r'\unsure{$C_1$|$C,$}','$C_1$'),
(r'\unsure{ou|des|aussi}','ou'),
(r'\unsure{\lim|\mathrm{lims}}',r'\lim'),
(r'\unsure{Dévissage|Déviss.ge}','Déviss.ge'),
(r'\unsure{qu. cpt|qu. cpct}',r'\unsure{qu. cpct|qu. cpt}'),
(r'\unsure{cpct|cpt}','cpct'),
(r'\unsure{radiciel|radiciels}','radiciels'),
(r'\unsure{prorad. f.|prorad.f.}','prorad.f.'),
(r'\unsure{Dév.|Déb.}','Dév.'),
(r'\unsure{tordus},',r'\unsure{tordus|$G_a$},'),
(r'\unsure{tore}','tore'),
(r'Structure\unsure{:|.} \unsure{cas|aux}',r'Structure. \unsure{aux|cas}'),
(r'\unsure{finis|près}','finis')
], 'review':'Personally inspected the whole page first and both overlapping halves, including the blank lower portion; read all words and symbols against C and H. Enlarged headings, the full marginal note, all diagram labels and bracket endpoints, every cancelled and inserted passage, and the concluding list. Crops range from 2× to 6×. Opaque hatching was inspected at the largest crop without recognition software. The long underline and each insertion position are retained.',
'decisions':[], 'inventory':[]}
def a(place,c,h,final,shows,conf='high',cc=False,hc=False,kind='other',marked='no',conseq=None):
 x=dict(place=place,c=c,h=h,final=final,shows=shows,confidence=conf,c_changed=cc,h_changed=hc,kind=kind,marked_in_H=marked)
 if conseq:x['consequential']=conseq
 d['decisions'].append(x)
a('top small label',r'\unsure{C_1|C,}','omitted','C_1','Small straight upright below and right of C, without a comma hook. Heading (192,122,972,292), 3×.','medium',True,True,'omission')
a('title deleted word',r'\deleted{\unsure{variés|varié}}',r'\struck{\ill{}}','C retained','The strike leaves a v-like start and low loops, but not a secure final s. Heading, 3×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('top-right main marginal text',r'Sont des lim-leftarrow de groupes radiciels','Structure des uncertain types de groupes radiciels','Sont des lim-leftarrow de groupes radiciels','Initial S and compact ont, low des, and tall l followed by im are visible. A left-pointing arrow is below lim. Margin (1093,136,1557,346), 3×.',hc=True,kind='misread word',marked='yes')
a('top-right inserted phrase',r'affines,\unsure{ou|des|aussi}',r'\ill{}','affines, ou','Affines is above the line; after the comma a small round o leads into a low u. The long curved guide attaches this before des. Margin, 3×.','medium',True,True,r'readable ink left as \ill{}')
a('top-right limit abbreviation',r'\unsure{\lim|lims}','uncertain types',r'\lim','No extra s follows the final m; the left arrow is separate below. Margin, 3×.','high',True)
a('heading above chain',r'\unsure{Dévissage|Déviss.ge}','Données','Déviss.ge','The long word has v/ss shapes, then a separate dot before ge; the g descends below the line. Dev (271,398,1004,501), 3×.','high',True,True,'misread word')
a('chain reduced suffix','red','réd','red','No acute is written above the reduced suffix. Chain (110,569,1697,797), 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
a('chain compactness abbreviations',r'\unsure{qu. cpt|qu. cpct}; \unsure{cpct|cpt}','qu.-cpt; cpt',r'\unsure{qu. cpct|qu. cpt}; cpct','The right abbreviation has a small additional curved join between p and t; the left is more compressed. No hyphen follows qu. Compactness (1105,586,1690,667), 4×.','medium',True,True,'abbreviation expanded or spelling modernised')
a('chain first lower label',r'\unsure{groupe|groupes} prolisse','groupe uncertain lisse','C retained','The second word begins with a p descender followed by ro before lisse. Final e/s of the first word remains compressed. Chain, 2×.','medium',hc=True,kind='misread word',marked='yes')
a('chain second lower label',r'\unsure{radiciel|radiciels}',r'radiciel','radiciels','After the tall l there is a distinct final curved s. Chain, 2×.','high',True,True,'misread word')
a('chain third-line abbreviation',r'\unsure{prorad. f.|prorad.f.}',r'\ill{}','prorad.f.','Each portion pro-rad-f is readable, with dots after d and f. Chain, 2×.','high',True,True,r'readable ink left as \ill{}')
a('chain third lower label',r'loc.\unsure{cptés|cpts|cpctés} sép.','loc. cpts sép.','C retained','The joined middle strokes and mark above the ending do not settle the fuller contraction. Chain, 2×.','low')
a('chain bracket geometry','three bracket/arrow groups','described as three braces','C diagram retained','The first is a bent horizontal right arrow from below e; the middle is a heavy squared bracket, the last a thin squared bracket. Chain, 2×.',hc=True,kind='drawing or diagram')
a('cancelled list first quotient',r'\unsure{\mathbb Z/\ell\mathbb Z|\mathbb Z/p\mathbb Z}',r'\ill{}','C retained','Z forms and the slash are visible under diagonal hatching; the intervening character remains crossed. Deleted symbols (169,865,586,957), 4×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('cancelled list mu',r'\unsure{\mu_p|\mathbb H_p}',r'\mu_p','C retained','The long parallel left strokes are traversed by cancellation; main letter remains uncertain. Deleted symbols, 4×.','low')
a('smooth connected structure ending','connu','connue','connu','The word ends with a long u-like stroke, without a separately formed e. Middle (164,867,1659,1166), 2×.',hc=True,kind='abbreviation expanded or spelling modernised')
a('smooth connected structure abbreviation',r'\unsure{Dév.|Déb.}','Déc.','Dév.','The final short low stroke is v-like and has no b loop or open c bowl. (1370,956,1512,1013), 4×.','medium',True,True,'misread word')
a('smooth connected structure barred words',r'\illegible{2}\unsure{décomposé}',r'\ill{}','C retained','Dense oblique hatching obscures the first two word spaces at 6×; later d and a p descender support only the tentative décomposé. (490,1028,1097,1085), 6×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('cancelled original tore','tore, deleted','tore, live','tore, deleted','The full horizontal cancellation runs through tore and continues through the following overwritten entry. Hidden entry (1014,1007,1450,1092), 5×.',hc=True,kind='deletion state (struck given live or live given struck)')
a('cancelled entry after original tore',r'\unsure{tordus}','ill.',r'\unsure{tordus|$G_a$}','A large loop and lower joined strokes remain beneath ss-groupes and a heavy bar; a letter sequence and a G with low a cannot be distinguished securely. Hidden entry, 5×.','low',True,True,r'readable ink left as \ill{}')
a('inserted tore',r'\unsure{tore}','tore','tore','The crossed t, o loop, r shoulder and terminal e are distinct. (569,1074,1054,1153), 4×.','high',True)
a('inserted tordus ending',r'\unsure{tordus|tordu}','tordu',r'\unsure{tordus|tordu}','The last long descending join may be a final s; retained as uncertain. Inserted tore crop, 4×.','low')
a('inserted torus placement and underline',r'\inserted{\uline{tore G_m^r} tordus}','interlinear tore G_m^r tordu ...','C retained','The new tore and G_m^r sit below the barred list, with a long underline; the later tordus (?) is separately below G_a^s. Middle 2×; inserted tore 4×.',hc=True,kind='insertion or placement')
a('cancelled ss-groupes',r'\unsure{ss-groupes|ss groupes}',r'\ill{} groupes','C retained','Small double-s forms are above the crossed earlier term, followed by groupes; the joining stroke may be a hyphen or pen join. (1211,1006,1422,1091), 4×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('radicial structure cancelled draft',r'\unsure{finis}\illegible{2}\unsure{pf|f}\unsure{alg}','ill.','C retained','Looped f and the final alg descender survive, but the middle hatching remains opaque and the pf/f strokes overlap. (980,1144,1563,1294), 5×.','low',hc=True,kind=r'readable ink left as \ill{}')
a('radicial structure cancelled upper insertion',r'\unsure{d’ordre|ordre}','omitted','C retained','A small overwritten initial mark precedes readable ordre above the main cancelled phrase; d versus the cancellation itself is uncertain. Deleted group crop, 5×.','low',hc=True,kind='omission')
a('radicial structure replacement','inserted radiciels, no colon','radiciels:','inserted radiciels','The replacement is below the cancelled word group. No colon is separately present after it. Lower (182,1137,1672,1528), 2×.',hc=True,kind='insertion or placement')
a('height-one paragraph cancelled lead-in',r'\deleted{\unsure{Se}}','omitted','C retained','The terminal e is clear, while the S is overstruck. (519,1293,593,1345), 5×.','low',hc=True,kind='omission')
a('height-one paragraph verb','dévissent','dévissage','dévissent','The ending is the joined ent sequence, followed by en; there is no descending g. Lower, 2×.',hc=True,kind='misread word')
a('height-one paragraph classification','classifiés','décrits','classifiés','The initial cl and tall f are visible in the long word. Lower, 2×.',hc=True,kind='misread word',conseq='The manuscript says the groups are classified, not merely described.')
a('height-one p-algebra ending',r'\unsure{p-algèbres|p-algèbre}','p-algèbres','C retained','Final joined stroke is too compressed to resolve the plural independently. (1145,1342,1670,1412), 4×.','low')
a('height-one Lie abbreviation',r'\unsure{rest.|restr.}','uncertain resp.',r'\unsure{rest.|restr.}','The ending has a tall t-like stroke followed by a low join; there is no clear p descender. Lie crop, 4×.','medium',hc=True,kind='misread word',marked='yes')
a('discrete-group heading punctuation',r'Structure\unsure{:|.}','Structure','Structure.','A single detached mark follows the final e; no second colon dot is visible. (211,1430,1295,1516), 3×.','high',True,True,'omission')
a('discrete-group heading connective',r'\unsure{cas|aux}','des',r'\unsure{aux|cas}','A rounded first loop followed by joined low strokes favors aux; cas remains possible in the compressed hand. Structure crop, 3×.','low',True,True,'misread word')
a('discrete-group parenthesis',r'\unsure{finis|près}','finis','finis','Tall f, short i stroke, n and final s are visible; no initial p loop. Structure crop, 3×.','high',True)
a('last heading','Cas abélien','Cas abéliens','Cas abélien','The word ends at n, with no final s, above the underline. Last (189,1560,1492,1675), 3×.',hc=True,kind='misread word')
a('last quotient',r'\mathbb Z/\ell\mathbb Z',r'\mathbb Z/n\mathbb Z',r'\mathbb Z/\ell\mathbb Z','The intervening character is a looped vertical ell, not the two shoulders of n; both Z letters have doubled diagonals. Last, 3×.',hc=True,kind='misread symbol or index',conseq='The quotient parameter is ell, not H’s n.')
d['unresolved']='Deleted title variés/varié; first compactness abbreviation qu. cpct/qu. cpt; groupe/groupes and loc. cptés/cpts/cpctés; deleted quotient ell/p and mu/outlined H; opaque cancelled word groups, tentative décomposé and overwritten tordus/G_a; tordus/tordu, ss-groupes spacing; cancelled finis, pf/f, alg and d’ordre/ordre; Se; p-algèbres/p-algèbre, rest./restr.; connective aux/cas.'
d['inventory']=[
['margin note','top center','C_1'],
['text','title','3) Groupes radiciels'],
['deletion','title','variés/varié'],
['margin note','upper right','Sont des lim de groupes radiciels'],
['insertion','upper-right above line','affines, ou'],
['text','above chain','Déviss.ge (k parfait)'],
['diagram','upper-middle chain','e subset G_red^0 subset G^0 subset G'],
['text','right of chain','G qu. cpct iff G/G^0 cpct'],
['text','under first bracket','groupe/groupes prolisse'],
['text','under middle bracket','radiciels; prorad.f.'],
['text','under last bracket','loc. cptés/cpts/cpctés sép.'],
['deletion','middle first line','Z/ell Z or Z/p Z; mu_p; alpha_p; Cas commutatif'],
['text','middle structure paragraph','Structure cas lisse connexe assez bien connu'],
['deletion','after VA,SS','two illegible words; décomposé; tore; tordus/G_a'],
['insertion','below cancelled torus term','underlined tore G_m^r; tordus/tordu'],
['deletion','above crossed entry','ss-groupes/ss groupes'],
['text','end of list','G_a^s'],
['insertion','below additive term','tordus (?)'],
['text','lower structure paragraph','Structure des groupes'],
['deletion','after des','radiciels'],
['deletion','after groupes','finis; two illegible words; pf/f; alg'],
['deletion','above cancelled group qualifiers','d’ordre/ordre'],
['insertion','below qualifiers','radiciels'],
['deletion','before dévissent','Se'],
['text','height-one paragraph','dévissent en groupes de hauteur 1'],
['text','next line','qui sont classifiés par des p-algèbres de Lie rest.'],
['text','discrete groups','Structure. aux/cas groupes discrets (finis)'],
['text','last line','Cas abélien; VA; G_a; G_m; Z/ell Z; mu_p; alpha_p']
]
runpy.run_path(str(root/'scripts/review.py'))['commit'](d)
