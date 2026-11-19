import sys
sys.path.insert(0,'out/scripts');from work import commit
R=[
(r'\uline{Foncteurs \unsure{fibres|fibrés} motiviques, et gps fondamen\unsure{taux} motiviques.}',r'Fonc\uline{teurs fibres motiviques, et gps fondame}% word cut off by torn right edge; no further letters survive\n\uline{motiviques}.'),
(r'Conditions de Hodge-Riemann',r'Conditions \unsure{de|\uline{de}|\deleted{de}} Hodge-Riemann'),
(r'Extension du groupe',r'Extension \unsure{du|de} \unsure{groupe|groupes}'),
(r'\unsure{places arithmétiques|places antiques}',r'\unsure{pts motiviques|places arithmétiques|places antiques}'),
(r'\uline{Groupe fondamental motivique.}',r'Grou\uline{pe fondamental motivique}.'),
(r'Pb \unsure{motivique}',r'Pts motiviques'),
(r'\unsure{parties|positives} à \unsure{val.}',r'parties à val.'),
(r'Rôle du groupe fondamental motivique',r'Rôle \unsure{du|des} \unsure{gpe|groupe|gps} \unsure{fondamental|fondamentaux} motivique'),
(r'\text{des \unsure{Ch.|Coh.} de Hodge}',r'\text{dans Ch. de Hodge}'),
(r'\unsure{transcendant|transcendants}',r'transcendant'),
(r'\unsure{pr.|prov.} des places diff.',r'\unsure{pr.|prov.} \unsure{des|deux} places diff.'),
(r'\text{des Coh. $l$-adique}',r'\text{dans Coh. $l$-adique}'),
(r'\unsure{mes|les} \unsure{autres} \unsure{anciens|axiomes}',r'mes \unsure{notes|autres} \unsure{anciennes|anciens}'),
(r'Fonctions $L$',r'\unsure{Fonction|Fonctions} $L$'),
(r'\deleted{\unsure{7}}8)',r'\deleted{7}8)'),
(r'\unsure{éclatements}, ou variétés',r'éclatements, ou Variétés')]
R[0]=(R[0][0],R[0][1].replace(r'\n','\n'))
L=[]
def a(p,c,h,f,s,v='high',C=False,H=True,k='other',m='no',q=None):
 d=dict(place=p,c=c,h=h,final=f,ink=s,kind=k,confidence=v,against_c=C,against_h=H,marked_in_H=m)
 if q:d['consequential']=q
 L.append(d)
a('title fibres accent','unsure fibres/fibrés','fibres','fibres','fibres: no accent appears over the low e; the only dot belongs to i and the tall loop to b.','medium',True,False,k='misread word')
a('title abbreviation','gps','groupes','gps','title: two descending letter strokes with a short final s form gps, without the written letters rou/e of groupes. H title located immediately before its page169 marker.',k='abbreviation expanded or spelling modernised')
a('title torn word','fondamen unsure taux','fondamentaux','fondame followed by torn-edge comment','title_end: the last surviving pale loop is e at the physical tear; no n/t/a/u/x survives after it. Neither witness completion is inserted.','high',True,k='text not on the page')
a('title underlining extent','whole title including initial letters and final period underlined','whole title underlined per note','Fonc plain, remainder underlined; final period outside underline','title_underline and title: first rule begins beneath t, after Fonc; second rule stops before the final black point.','medium',True,k='other')
a('oval in item0','drawn oval around à la Weil','text encadré description','oval retained as drawing','zero and zero_upright: a pale, slightly tilted closed oval encloses the three words, with extra retracing at left.',k='drawing or diagram')
a('associées in item0','unsure associées','associées','unsure associées retained','associees: compressed central strokes and final returning hook leave the sequence of e/e/s uncertain; the accent-like mark is separate from the i dot.','low',k='misread word')
a('impairs in item0','impairs','impair','impairs','zero: after the i/r sequence a separate terminal descending s hook precedes sur.',k='misread word')
a('after sur in item0','no further surviving text','ill{}','no added unreadable word','zero: sur reaches the torn right edge; there is no surviving ink for an extra word after it.',k='text not on the page',m='illegible')
a('de in inserted Conditions','de','de','unsure live de/underlined de/deleted de','conditions_de: a second dark rule crosses or runs beneath the low body of de; retracing, underlining and cancellation cannot be securely separated.','low',True,k='deletion state (struck given live or live given struck)')
a('article in item1','du','de','unsure du/de','one_du: the raised initial d stroke is clear, but the following long, low ink does not resolve u versus e.','low',True,k='misread word')
a('groupe ending in item1','groupe','groupes','unsure groupe/groupes','one_groupe: a small shoulder and terminal downstroke follow the p; they do not securely distinguish e from es.','low',True,k='misread word')
a('définie ending in item1','unsure définie/définies/défini','définie','same C uncertainty retained','definie: two i dots are visible, but the thick final loop and departing stroke do not settle the ending.','low',k='misread word')
a('final phrase item1','unsure places arithmétiques/places antiques','pts motiviques','unsure pts motiviques/places arithmétiques/places antiques','places compared with Pb, motivique and other_places: first descender/loop/s cluster can be the abbreviation pts; following t, i dots and q match motiviques. Compression prevents rejecting the older alternatives altogether.','low',True,k='misread word',q='The primary reading of item1 is pts motiviques, retained as an explicit doubt rather than C’s places arithmétiques.')
a('heading below item1','Groupe fondamental motivique. wholly underlined','ill{} gpe fondamental motivique.','Grou plus underlined pe fondamental motivique, period outside','groupe_underline and one: a large open G followed by r/ou and p/e is one word, not an unreadable preceding word. The rule begins under p and stops before the period.','medium',True,k='readable ink left as \\ill{}',m='illegible')
a('spectre in item3','spectre','uncertain spectre','spectre','three: s, descending p, low ec, crossed t and final re are all legible.','high',False,True,k='misread word',m='yes')
a('abbreviation item3','Pb','Pts','Pts','Pb: tall t has its own rightward crossbar; a separate small s curves below it. There is no closed b bowl.','high',True,False,k='misread word',q='Item3 reads Pts motiviques, not Pb motivique.')
a('motivique ending item3','unsure motivique','motiviques','motiviques','motivique: m cups, t, separate i dots, q descender and terminal es return remain visible at the edge.','medium',True,False,k='misread word')
a('word before à val. in item3','unsure parties/positives','ill{}','parties','parties: p, compressed ar, tall crossed t, then dotted i and an e/s ending are present; no extra dotted i occurs before t.','medium',True,k='readable ink left as \\ill{}',m='illegible')
a('val. abbreviation','unsure val.','val.','val.','val: low v followed by an a/l arch ends with a separate dot.','medium',True,False,k='other')
a('article after Rôle','du','des','unsure du/des','four_des: a d loop and one long low sequence remain compatible with either reading.','low',True,k='misread word')
a('group word in item4','groupe','groupes','unsure gpe/groupe/gps','four_gps: two descenders identify g/p with a very short final stroke; the compressed middle may be an abbreviation or a joined fuller word.','low',True,k='abbreviation expanded or spelling modernised')
a('fondamental ending item4','fondamental','fondamentaux','unsure fondamental/fondamentaux','four_fond: the last two tall turns do not securely identify al versus aux; no grammatical completion is imposed.','low',True,k='misread word')
a('Hodge row initial word','des','dans','dans','dans1: following d, a small a-like return and extended n stroke precede the terminal s turn.','medium',True,False,k='misread word')
a('Hodge row abbreviation','unsure Ch./Coh.','Coh.','Ch.','coh: C meets the tall h directly, with no intervening o; a full point follows.','high',True,k='abbreviation expanded or spelling modernised')
a('first transcendant ending','unsure transcendant/transcendants','transcendants','transcendant','trans_full: the final tall crossed t descends to a single short terminal foot; there is no separate s after it. The middle is tightly joined.','medium',True,k='misread word')
a('abbreviation before places diff.','unsure pr./prov.','pour','unsure pr./prov. retained','pr: one descending p and low horizontal sequence end in a distinct point; the unabbreviated pour of H does not represent that final stop.','low',k='abbreviation expanded or spelling modernised')
a('article before places diff.','des','deux','unsure des/deux','other_places: the last mark after d/e is a short separate dark stroke; it is insufficient to settle s against a compressed ux.','low',True,k='misread word')
a('réseau after et','unsure réseau/réseaux','réseau','unsure réseau/réseaux retained','reseau: the final heavy turn could include an x or end at u; no clear crossing is separable.','low',k='misread word')
a('l-adic row initial word','des','dans','dans','dans2: d/a followed by a long n and a separate terminal s are visible.','medium',True,False,k='misread word')
a('network comparison layout','array with outer brackets and two vertical dividers','prose with colons and semicolon; note describes vertical traits','drawn table layout retained','four: one outer left bracket and right bracket enclose two rows; each has its own long vertical divider. H description is not a reproduction.',k='drawing or diagram',m='descriptive note')
a('inserted de4 punctuation','de 4','de 4)','de 4','insert4: right curving mark continues into the long lower insertion guide and central caret, rather than forming a separate closing parenthesis.',k='text not on the page')
a('mes in item5','unsure mes/les','mes','mes','mes: three low rounded turns lead to the final s hook; there is no tall initial l.','high',True,False,k='misread word')
a('word after mes','unsure autres','ill{}','unsure notes/autres','autres and five_nine: a low initial cup, separate tall crossed t and final es sequence suggest notes, but the first strokes also permit autres.','low',True,k='readable ink left as \\ill{}',m='illegible')
a('last word item5','unsure anciens/axiomes','anciennes','unsure anciennes/anciens','anciens: a distinct c and dotted i rule against axiomes; repeated late humps favor anciennes but the ending remains compressed.','low',True,k='misread word')
a('Fonction ending item6','Fonctions','Fonction','unsure Fonction/Fonctions','fonction: final heavy joined stroke can be n or ns; no confident plural is imposed.','low',True,k='misread word')
a('Structures adjective','unsure pratiques/positives/p-adiques','positives','same C uncertainty retained','structures: first p, central tall t and following dot are visible; the intervening flattened strokes do not decide the alternatives.','low',k='misread word')
a('old item number before8','deleted unsure7','overwritten digit noted without reading','deleted7','seven: straight top bar and descending right arm of 7 remain distinct above the superposed loops of 8.','medium',True,k='omission',m='editorial note')
a('mettre in item8','mettre','uncertain coeff.','mettre','five_nine: two short m turns precede the joined tt stems/crossbars and final re; coeff would require an absent c and f pair.',k='misread word',m='yes')
a('marks after Z','four dashes','ellipsis','four dashes','five_nine and ZZ: four separate short horizontal strokes follow the doubled diagonal Z.',k='misread symbol or index')
a('marks after Riemann','unsure ??','??','unsure ?? retained','Riemann_q: first hooked curve and second large arch lack clearly separated dots; interrogative reading remains plausible, not certain.','low',k='misread symbol or index')
a('lower note éclatements','unsure éclatements','récurrence','éclatements','eclatements and margin_upright: acute e, c/l, crossed t and the ements sequence can be followed individually; no initial r precedes e.','high',True,k='misread word',q='The lower note proposes éclatements, not récurrence.')
a('lower note ou','ou','ill{}','ou','margin_ou and margin_upright: a low open o and separate horizontal u follow the comma; no longer unreadable word is present.',k='readable ink left as \\ill{}',m='illegible')
a('lower note Variétés de drapeaux','variétés de drapeaux','uncertain variétés de drapeaux','Variétés de drapeaux','margin and margin_ou: the first V is full capital height; the rest of the phrase has distinct t, d and descending p with terminal x.','medium',True,k='misread word',m='yes')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('text','title, two lines','Fonc underlined teurs fibres motiviques, et gps fondame / underlined motiviques.')
i('text','list heading','À examiner :')
i('text','item0','VA … associées aux motifs purs de poids impairs sur')
i('drawing','within item0','oval around à la Weil')
i('insertion','between0 and1','Conditions de Hodge-Riemann …; de stroke status uncertain')
i('drawing','item1 numeral','circled1')
i('margin note','left of1','OK and star')
i('text','item1','Extension du/de groupe(s) définie(s) par des pts motiviques / places …')
i('text','heading below1','Grou underlined pe fondamental motivique, period')
i('drawing','item2 numeral','circled2')
i('text','item2','Relations avec le corps de classes')
i('margin note','left of3','OK')
i('drawing','item3 numeral','circled3')
i('text','item3','Cas du spectre d’un corps fini. Pts motiviques')
i('text','item3 continuation','parties à val. dans mathbb R ???')
i('margin note','left of4','star')
i('text','item4 heading','Rôle du/des gpe/groupe/gps fondamental/fondamentaux motiviques pour la comparaison des réseaux canoniques')
i('diagram','item4 comparison','outer brackets; dans Ch. de Hodge, two alternatives beside divider; dans Coh. l-adique, 2 réseaux transcendants beside divider')
i('text','item5','Relations … avec mes notes/autres anciennes/anciens')
i('insertion','item5 via bracket-like guide and caret','de4')
i('text','item6','Fonction(s) L : équation fonctionnelle')
i('margin note','left of7','OK')
i('text','item7','Structures pratiques/positives/p-adiques …')
i('deletion','number8','old7 overwritten by8')
i('text','item8','Topologie à mettre sur mathbb Z, four dashes')
i('text','item9','Hyp. de Riemann, uncertain two question marks')
i('margin note','lower separate four lines','Positivité à la Hodge en se ramenant à des questions de underlined diviseurs par éclatements, ou Variétés de drapeaux ??')
commit(15,170,dict(replace=R,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole image and both halves personally read before witnesses. Every line, C doubt, mathematical letter, marginal sign, title tear, overwriting and insertion enlarged. Long lower note and item0 interline inspected in rotated upright views; OK marks separately rotated. H title located before page169, not treated as absent. The first pts/places cluster remains uncertain after comparison with both later Pts and places, although the primary reading changes. No context consulted.'))
