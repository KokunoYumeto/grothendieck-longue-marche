import sys
sys.path.insert(0,'out/scripts')
from work import commit
R=[
(r'\unsure{commencé}', 'commencé'),
(r'\unsure{Théorémes|Théorèmes}', 'Théorémes'),
(r'\unsure{foncteurs}', 'foncteurs'),
(r'\unsure{noeth}', 'noeth'),
(r'\unsure{Mazur}', 'Mazur'),
(r'\unsure{en} train', 'en train'),
(r'\unsure{coefficients}', 'coefficients'),
(r'\unsure{noveaux|noyaux|nouveaux}', 'noveaux'),
(r"\unsure{Th's|Thés}", "Th's"),
(r'\unsure{Ths|Thés}', 'Ths'),
(r'\unsure{situation}', 'situation'),
(r'\unsure{résolu} par Raynaud \(\bigl[\)', 'résolu par Raynaud'),
(r'\unsure{passage}', 'passage'),
(r'\unsure{amplitude|amplitudes}', 'amplitude'),
(r'\inserted{``vrai\'\'}',r'\inserted{``vrai\'\'}'),
]
# The quote-sensitive replacement is written without a raw-single-quote escape.
R.pop()
R.append(("\\inserted{``vrai''}",r'''\tikz[baseline=(vr.base)]{\node[inner sep=1pt] (vr) {\inserted{``vrai''}};\draw ([xshift=-2pt]vr.south west) .. controls +(0,-.15) and +(-.2,0) .. ([yshift=-3pt]vr.south) -- ([yshift=-8pt]vr.south) -- ([xshift=2pt,yshift=-3pt]vr.south) .. controls +(.2,0) and +(0,-.15) .. ([xshift=2pt]vr.south east);}'''))
# Preserve the narrow retracing of the right bracket of item 16.
R.append((r'\draw (.75,1.65) -- (1,1.65) -- (.67,-.8) -- (.48,-.65);',r'\draw (.75,1.65) -- (1,1.65) -- (.67,-.8) -- (.48,-.65);\draw (.93,.65) -- (.61,-.93) -- (.43,-.72);'))
# Seven isolated ticks stand farther left than the item numbers.
for anchor,shape in [
('12)',r'\fill (0,0) circle (.018);'),
(r'\textcircled{\small 13}',r'\draw[line width=.7pt] (0,.02)--(.045,-.015);'),
('14)',r'\draw[line width=.7pt] (0,.015)--(.06,0);'),
(r'\textcircled{\small 15}',r'\draw[line width=.7pt] (0,0)--(.015,.045)--(.04,.04);'),
(r'\textcircled{\small 16}',r'\draw[line width=.7pt] (0,.035)--(.01,0);'),
(r'\textcircled{\small 18}',r'\draw[line width=.7pt] (0,.04)--(.03,0);'),
(r'\tikz[baseline=(num.base)]',r'\draw[gray!70,line width=.5pt] (0,0)--(.015,.04);'),
]:
 R.append((anchor,r'\llap{\tikz[baseline=-.2ex]{'+shape+r'}\hspace{1.3em}}'+anchor))
# Draw the three-line left bracket at the item, not as a character in its note.
R.append(('17)\\margin',r'\llap{\tikz[baseline=1.1cm]{\draw (.13,1.25)--(0,1.2)--(.03,0)--(.18,.03);}\hspace{.25em}}17)\margin'))
L=[]
def a(p,c,h,f,ink,conf='high',ac=False,ah=True,k='other',mh='no',cons=None):
 d=dict(place=p,c=c,h=h,final=f,ink=ink,confidence=conf,against_c=ac,against_h=ah,kind=k,marked_in_H=mh)
 if cons:d['consequential']=cons
 L.append(d)
a('item 12 margin',r'\unsure{commencé} par Raynaud','commencé par Raynaud','commencé par Raynaud','margin12_upright7x/−39 degrees: c/o/mm/e/n/c/é, including the final acute, are readable.','medium',True,False)
a('item 12 right marks','two near-vertical strokes','omitted','two near-vertical strokes','right12x10: two separate dark lines, the left one longer at both ends.','high',False,True,'drawing or diagram')
a('item 13 initial noun',r'\unsure{Théorémes|Théorèmes}','Théorèmes','Théorémes','th13accent12x: both accents rise toward the right; the second is flatter but not a descending grave.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 13 adjective',r'\unsure{assymptotiques|asymptotiques}','asymptotiques',r'\unsure{assymptotiques|asymptotiques}','asym13x10: compact joined strokes between a and y can be double s or a retraced s; the alternative remains.','low',False,True)
a('item 13 noun',r'\unsure{foncteurs}','foncteurs','foncteurs','thirteen1x5: f descender, o/n/c/t/e/u/r/s are individually discernible at the right edge.','medium',True,False)
a('item 13 abbreviated adjective',r'\unsure{noeth}','noethérien','noeth','thirteen2x5: n/o/e/t/h ends before complet; no érien and no abbreviation point.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 13 margin opening',"S'impose moins",r'\ill',"S'impose moins",'margin13_upright7x/−44 degrees: S, raised apostrophe, impose and moins are readable before depuis.','high',False,True,r'readable ink left as \ill{}','yes')
a('item 14 after fibres','....','…','....','fourteen2x5: four separate points before the closing parenthesis.','high',False,True,'misread symbol or index')
a('item 14 repeated champs','champs champs','champs. champs','champs champs','fourteen2x5/fourteen3x7: blank interval after first champs; no full stop.','high',False,True,'text not on the page')
a('item 14 terminal dots','....','…','....','fourteen3x7: four points after représentables.','high',False,True,'misread symbol or index')
a('item 14 right drawing','double hooked bracket','omitted','double hooked bracket','right14x8: two close sloping stems, short left hook at top and a doubled turned hook below.','high',False,True,'drawing or diagram')
a('item 15 opening noun',r'\unsure{Théorie|Théories}','Théories',r'\unsure{Théorie|Théories}','fifteen1x6/theories15x12: the last dark exit shape may include s, but it is not separable securely from the final e.','low',False,True)
a('item 15 old letter',r'\deleted{\unsure{g}}','omitted',r'\deleted{\unsure{g}}','type18x: a lower loop/descender is buried under the beginning of type; g remains a tentative reading.','medium',False,True,'omission')
a('item 15 homotopy index',r'\pi_{\unsure{i|\bullet|\cdot}}',r'\pi_i',r'\pi_{\unsure{i|\bullet|\cdot}}','pi18x: the point below-right is clear, but a separate i stem cannot be distinguished from the tail of the right pi leg.','low',False,True,'misread symbol or index')
a('item 15 cancelled word',r'\deleted{\unsure{coefficients}}',r'\struck{coefficients}',r'\deleted{coefficients}','coeff1x15/coeff2x18: coeffi at the upper line and cients at the next line remain readable across the two cancellation strokes.','medium',True,False)
a('item 15 following noun',r'\unsure{noveaux|noyaux|nouveaux}','morceaux','noveaux','noveaux15x: n/o/v/e/a/u/x; no y descender and no additional u between o and v.','medium',True,True,'misread word')
a('item 15 added theorem abbreviation',r"\unsure{Th's|Thés}",'Th.',"Th's",'hurwicz15x/fifteenadd6x: capital T, h, raised apostrophe and small s, without an é or a following abbreviation point.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 15 added name',r'\unsure{Hurwisz|Hurwicz}','Hurewicz',r'\unsure{Hurwisz|Hurwicz}','hurwicz15x: no e between r and w; the penultimate curve permits s or c before the descending final z.','low',False,True,'misread word')
a('item 15 comparison abbreviation',r'\unsure{Ths|Thés}','Th.','Ths','comparison10x: T/h/s without an accent or abbreviation point.','medium',True,True,'abbreviation expanded or spelling modernised')
a('item 15 comparison punctuation','comparaison,','comparaison.','comparaison,','comparison10x: following mark has a descending comma tail.','high',False,True,'misread symbol or index')
a('item 15 cancelled continuation',r'\deleted{de \unsure{spécialisation}.}',r'\struck{\ill}',r'\deleted{de \unsure{spécialisation}.}','oldspecial20x: de is readable; p descender, an acute and l/t ascenders support spécialisation, but the heavy horizontal stroke leaves doubt.','medium',False,True,r'readable ink left as \ill{}','yes')
a('item 15 addition placement','added Th’s … comparaison, cancelled continuation','inline continuation','added Th’s … comparaison, cancelled continuation','fifteenadd6x/comparison10x: smaller writing squeezed above the following entry, unlike the original broad main hand.','high',False,True,'insertion or placement')
a('item 15 margin name',r'\unsure{Mazur}-Artin',r'\uncertain{M. Artin}','Mazur-Artin','margin15_upright6x/−48 degrees: full M/a/z/u/r and connecting hyphen before Artin.','medium',True,True,'misread word','yes')
a('item 15 margin ending',r'Quillen \unsure{en} train','Quillen --- en train','Quillen en train','margin15_upright6x/−48 degrees: en has an e loop and n shoulder; no separating dash.','medium',True,True,'text not on the page')
a('item 16 margin continuation',r'\unsure{situation} peu engageante',r'schéma \ill','situation peu engageante','margin16_upright7x/−44 degrees: s/i/t/u/a/t/io/n is visible, followed by peu and the two g descenders of engageante.','medium',True,True,r'readable ink left as \ill{}','yes')
a('item 16 cancellation','main sentence struck','main sentence live','main sentence struck, insertion separately retained','sixteenx8x/sixteen1x6/sixteen2x6: a near-vertical black stroke and a crossing diagonal traverse the two-line entry.','high',False,True,'deletion state (struck given live or live given struck)',cons='H gives the cancelled specialization problem as live text.')
a('item 16 vrai addition',"inserted ``vrai'' without leader",'inline « vrai »',"inserted ``vrai'' with curved leader before groupe",'vrai16x: two pairs of raised strokes; curved lower brace with downward point reaches the gap before groupe. The added word is not itself crossed.','high',True,True,'insertion or placement')
a('item 16 right bracket','single hooked path','omitted','hooked path with second lower trace','right16x10: right stem is retraced toward the bottom, with two lower left hooks and a faint upper trace.','high',True,True,'drawing or diagram')
a('item 17 margin verb',r'\unsure{résolu}','résolu','résolu','margin17_upright7x/−48 degrees: r/é/s/o/l/u clear, including the acute.','medium',True,False)
a('item 17 left bracket','inline bracket after Raynaud','omitted','long left bracket alongside the three-line item','leftbracket17x9 and bottom half: bracket stands between the margin note and numeral/text; its lower hook points right at the third line.','high',True,True,'insertion or placement')
a('item 17 whole cancellation','struck','live except old word','struck throughout','seventeenx7x: long near-vertical and diagonal strokes cross all three lines; old word has its own local cancellation as well.','high',False,True,'deletion state (struck given live or live given struck)',cons='H misses cancellation of the entire representability item.')
a('item 17 preposition','de foncteurs','des foncteurs','de foncteurs','seventeen1x5: d and e only, followed by a wide blank before f.','high',False,True,'misread word')
a('item 17 separator',':',',',':','seventeen1x5: two vertically separated points after foncteurs.','high',False,True,'misread symbol or index')
a('item 17 correspondance ending','correspondance....','correspondances…','correspondance....','seventeen1x5: no independent final s; four separately written points below/right.','high',False,True,'misread word')
a('item 17 non représentabilité','non représentabilité','non-représentabilité','non représentabilité','seventeen2x6: a clear gap between the words, without a hyphen.','high',False,True,'text not on the page')
a('item 17 article before Pic','de','du','de','seventeen3x7: looped d plus e, not a u bowl.','high',False,True,'misread word')
a('item 17 dim abbreviation','dim','dim.','dim','seventeen3x7: after m comes a blank and the locally cancelled word; no intervening point.','high',False,True,'abbreviation expanded or spelling modernised')
a('item 17 locally cancelled word',r'\unsure{de|rel}',r'\ill',r'\unsure{de|rel}','oldrel25x: a tall loop and lower return support de; additional buried strokes leave rel possible under local and global cancellation.','low',False,True,r'readable ink left as \ill{}','yes')
a('item 18 noun',r'\unsure{passage}','passage','passage','eighteen1x6: p descender, joined a/ss/a, g descender and final e are visible.','medium',True,False)
a('item 18 case','artinien','arbitraire','artinien','eighteen1x6/right18x9: a/r/t/i/n/i/e/n, with t stem and two dotted i positions; no b ascender.','high',False,True,'misread word',cons='Restricts the passage-to-quotient question to the written Artinian case; H substitutes an arbitrary case.')
a('item 18 cancelled noun',r'\unsure{Construction|Constructions}','Construction',r'\unsure{Construction|Constructions}','eighteendeleted10x/ends18x13: final n/possible s merges with the lowest strike; singular favored but not secure.','low',False,True)
a('item 18 cancelled adjective',r'\unsure{générale|générales}','générale',r'\unsure{générale|générales}','ends18x13: final e/possible s shares a thick cancelled return; acute accents are visible.','low',False,True)
a('item 18 cancelled last word',r'\unsure{modules|variables}',r'\ill',r'\unsure{modules|variables}','modules20x: lower rounded bodies and a tall final l favor modules; upper letter bodies are partly covered by multiple strokes.','low',False,True,r'readable ink left as \ill{}','yes')
a('item 18 right drawing','double sloping bracket','omitted','double sloping bracket','right18x9: two long sloping strokes with an upper curl and lower doubled hook.','high',False,True,'drawing or diagram')
a('item 19 lower mark',r'\unsure{\times|*}','omitted',r'\unsure{\times|*}','nineteenmark15x: small crossed mark joins the lower oval boundary; the overlap prevents fixing its number of arms.','low',False,True,'drawing or diagram')
a('item 19 noun',r'\unsure{amplitude|amplitudes}','amplitude','amplitude','ampend14x: d has its own ascender, followed by a looped e and short terminal exit; no separate s body.','medium',True,False)
a('item-number circles','circled 13,15,16,18,19','parenthesized 13,15,16,18,19','circled 13,15,16,18,19','whole, thirteen1x5, fifteen1x6, sixteen1x6, eighteen1x6, nineteenmark15x: closed pen loops enclose these numerals.','high',False,True,'drawing or diagram')
a('seven far-left ticks','omitted','omitted','small isolated marks before items 12,13,14,15,16,18,19','ticks1–7 at18x: seven separate dark or gray short marks, distinct from the writing and in a recurring left column. Shapes are reproduced without assigning linguistic meaning.','medium',True,True,'drawing or diagram')
I=[]
def i(k,p,t):I.append(dict(kind=k,position=p,text=t))
i('drawing','far left of item 12','small dark dot')
i('text','item 12','Mise au point, et extensions diverses, de la théorie des modèles de Néron.')
i('margin note','left item 12, slanted','commencé par Raynaud')
i('drawing','right item 12','two near-vertical strokes')
i('drawing','far left of item 13','small oblique tick')
i('drawing','item 13 number','circle 13')
i('text','item 13','Théorémes assymptotiques|asymptotiques … anneau local noeth complet ou hensélien.')
i('margin note','left item 13, slanted',"S'impose moins depuis les résultats d'approximation d'Artin")
i('drawing','far left of item 14','short nearly horizontal tick')
i('text','item 14','Structures des Topos … Structure des champs champs représentables....')
i('drawing','right item 14','double sloping hooked bracket')
i('drawing','far left of item 15','short bent tick')
i('drawing','item 15 number','circle 15')
i('text','item 15',"Théorie|Théories du type d'homotopie des Topos … pi with uncertain index … noveaux infinitésimaux.")
i('deletion','item 15 before type','old g?')
i('deletion','item 15 across line break','coefficients')
i('insertion','item 15 after infinitésimaux',"Th's d'Hurwisz|Hurwicz. Suites exactes d'homotopie. Ths de comparaison,")
i('deletion','end item 15 addition','de spécialisation?.')
i('margin note','left item 15, slanted','fait partiellement par Mazur-Artin. Réflexions de Quillen en train')
i('drawing','far left of item 16','short vertical tick')
i('drawing','item 16 number','circle 16')
i('deletion','item 16 two-line main block','Théorie de spécialisation du groupe fondamental, pour une famille de courbes.; large crossed strokes')
i('insertion','item 16 before groupe',"``vrai''")
i('drawing','under vrai addition','curved brace and downward insertion point')
i('margin note','left item 16, slanted','contre-exemple de Artin, situation peu engageante')
i('drawing','right item 16','hooked bracket with narrow lower retracing')
i('deletion','item 17 three-line block','Séparation de foncteurs : classes de correspondance.... Cas de représentabilité et de non représentabilité de underlined Pic_X/S, X de dim relative 1 sur S.; large crossed strokes')
i('deletion','item 17 after dim','locally cancelled de|rel')
i('margin note','left item 17, slanted','résolu par Raynaud')
i('drawing','left item 17','long bracket open right alongside all three lines')
i('drawing','far left of item 18','short oblique tick')
i('drawing','item 18 number','circle 18')
i('text','item 18',"Question du passage au quotient dans cas artinien et de l'effectivité de données de descente plates.")
i('deletion','after item 18','Construction|Constructions générale|générales de corps de modules|variables.')
i('drawing','right item 18','double sloping bracket')
i('drawing','far left of item 19','short gray tick')
i('drawing','item 19 number','circle 19 with lower cross/asterisk')
i('text','item 19',"Théorie d'amplitude pour cycles de dim. quelconque.")
commit(66,3,dict(replace=R,changes=L,inventory=I,sheet_kind='text',hand='his hand',observations='Whole and both halves personally viewed before witnesses. All decision crops in crop66_003.py and upright margins personally viewed; adaptive accents, endings, seven ticks and left bracket enlarged. The mistaken bracket17 crop and incomplete plates18 crop were superseded by leftbracket17 and plates18full. All agreed text, plain X/S/1, underlined Pic, pi index, quotation marks, cancellations, punctuation, and margin positions checked. No watermark visible. Archive numeral 2 remains comment only. Not a second audit or a mathematical check.'))
