import json
from pathlib import Path
page='149_scan132'
boxes={
'P01':[1030,65,1167,131], 'P02':[1230,226,1644,372], 'P03':[320,380,736,491],
'P04':[591,526,1538,748], 'P05':[968,969,1554,1091], 'P06':[282,1096,1632,1225],
'P07':[887,1220,1030,1304], 'P08':[1011,1293,1654,1458], 'P09':[278,1457,1157,1609],
'P10':[395,1598,1034,1691], 'P11':[958,1661,1324,1777], 'P12':[534,1717,1655,1926],
'P13':[792,1901,1644,2024], 'P14':[290,2000,1613,2151], 'P15':[295,2168,1599,2303],
'P16':[17,1670,535,2190], 'P17':[17,2297,109,2347], 'P18':[1424,81,1504,122],
'P19':[1158,336,1290,435]}
def crop(p): return f'crops/{page}_{p}.png'
changes=[]
def add(id,place,c,h,final,evidence,p,confidence,kind,ac,ah,mh,con,cat):
 changes.append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=crop(p),box=boxes[p],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=mh,consequential=con,error_category=cat))
add('P01','L1 à propos des', 'des','de','des',
 'After the looped d and low e there is a separate terminal curled/downturned s, not just the open e termination. The plural is retained from C.',
 'P01','high','misread word',False,True,False,False,2)
add('P03a','L4 before ou',r'(ou',r'\struck{associés} \uncertain{ou plutôt}',r'ou \deleted{\unsure{associés}} plutôt',
 'The line begins with the two low connected strokes of ou; the blank to their left contains no opening parenthesis. The cancelled word lies below ou and before plutôt. Its internal strokes remain partly covered, so its C doubt is retained.',
 'P03','high','text not on the page',True,False,True,False,9)
add('P04a','L6 et me convaincre du',r'et me \unsure{convaincre} du',r'et une connaissance de','et me convaincre du',
 'The short word has an initial two-hump m followed by e. The next word begins with an open c and o, has the v turn and dotted i centrally, and ends in the compact cre sequence; it is not the longer connaissance. The following d has its tall ascender and the next low letter is u. This resolves the C confidence mark on convaincre.',
 'P04','high','misread word',True,True,False,False,2)
add('P04b','L6 apparent opening curve before et',r'\inserted{pour $x$ variable,} et',r'\add{pour $x$ variable,} (et',r'\inserted{pour $x$ variable,} et',
 'The large curve to the left of et continues upward into a long leader ending beside the inserted pour x variable; it is a continuous insertion leader, not a separate parenthesis.',
 'P04','high','insertion or placement',False,True,False,False,6)
add('P05','L9 ce qu’on vient d’',r"ce qu'on vient d'",r"ce qui vient d'",r"ce qu'on vient d'",
 'The q descender is followed by a low u, a detached apostrophe, and a separate low on group before vient; the source does not end the relative expression at qui.',
 'P05','high','misread word',False,True,False,False,2)
add('P06a','L10 verb after vient d’',r'\unsure{énoncer|annoncer}',r'\uncertain{être} \uncertain{présumé}',r'\unsure{énoncer|annoncer}',
 'There is one short word consisting of low connected strokes, then a dash. It has no tall t/r word followed by a separate présumé; H’s two-word reading exceeds the ink. The weak initial vowel and compressed middle still do not distinguish énoncer from annoncer securely, so C’s alternatives remain.',
 'P06','medium','misread word',False,True,True,False,2)
add('P06b','L10 after justement',r'justement, à sous-groupes',r'justement, à \uncertain{conjugaison} — et \uncertain{à} \uncertain{sous-groupes}',r'justement, à sous-groupes',
 'After the comma there is one accented à followed immediately by the short sous- group at the right end of this line. No intervening conjugaison, second dash, et, or second à is present.',
 'P06','high','text not on the page',False,True,True,True,9)
add('P07','L11 struck tout',r'\deleted{\unsure{tout}}',r'\uncertain{tout}',r'\deleted{\unsure{tout}}',
 'A broad horizontal cancellation crosses the compact word and returns diagonally beneath it; the first tall t and final t-like tip survive, but not all middle letters. The deletion state is certain, the lexical doubt is retained.',
 'P07','high','deletion state (struck given live or live given struck)',False,True,True,False,7)
add('P08','L12 corrected relation after V',r'V\deleted{\unsure{\to}}\inserted{\in}\mathfrak X_{L/K}',r'V \in \mathfrak{X}_{L/K} \struck{\ill{}}',r'V\deleted{\unsure{\to}}\inserted{\in}\mathfrak X_{L/K}',
 'The live membership sign is above a cancelled horizontal relation between V and the calligraphic X. A bent right-end stroke supports the tentative arrow reading, but the crossing-out prevents clearing C’s doubt. The deleted ink is in this gap, not after the L/K subscript as H places its illegible deletion.',
 'P08','medium','insertion or placement',False,True,False,True,6)
add('P09','L13 inserted de',r'pas \inserted{de} centre',r'pas de centre',r'pas \inserted{de} centre',
 'The looped d and following e stand above the line between pas and centre. A curved leader descends immediately before centre, fixing the attachment of this added word.',
 'P09','high','insertion or placement',False,True,False,False,6)
add('P11','L15 l’ens. after de',r"de l'ens. fini",r"de \struck{l'}l'ens.\ fini",r"de l'ens. fini",
 'The l is heavily retraced, with a crossing at its upper loop and a dark basal return. There is only one visible apostrophe and no separately displaced second l’ sequence. I retain one l’ens.; the heavy retracing warrants blind review of H’s proposed extra deletion.',
 'P11','medium','text not on the page',False,True,False,False,9)
add('P12a','L16 equation numbering',r'\tag{36}',r'(nothing)',r'(nothing)',
 'The main display begins directly with D_J and carries no independent (36) tag. The only written (36) belongs to the oblique marginal sentence immediately following its intersection formula, as shown in P16. C duplicated that marginal reference as a display tag.',
 'P12','high','text not on the page',True,False,False,False,9)
add('P12b','L16 superscript on D_J',r'D_J^{\unsure{\circ}}',r'D_J^{*}',r'D_J^*',
 'The raised mark has several crossing dark strokes and projecting tips around a filled centre; it is not a hollow circular superscript. The whole display was inspected with this mark. C’s doubt is resolved to an asterisk.',
 'P12','high','misread symbol or index',True,False,False,True,1)
add('P12c','L16 brace label and right-hand closed intersection',r'\overbrace{\bigcap_{j\in J}D_j}^{\Delta_J}-\bigcup_{i\in I-J}\Delta_J\cap D_i',r'\overbrace{\bigcap_{j \in J} D_j}^{D_J} - \bigcup_{i \in I \setminus J} D_J \cap D_i',r'\overbrace{\bigcap_{j\in J}D_j}^{\Delta_J}-\bigcup_{i\in I\setminus J}\Delta_J\cap D_i',
 'Both occurrences are closed triangular signs with a diagonal left side, diagonal right side and horizontal base, followed by J. The D_j under the brace instead has an upright stem and rounded bowl. Thus both closed-intersection labels are Delta_J, not D_J.',
 'P12','high','misread symbol or index',False,True,False,True,1)
add('P12d','L16 union index',r'i\in I-J',r'i \in I \setminus J',r'i\in I\setminus J',
 'Between the upright I and J in the union index is a short descending diagonal slash. It differs from the long horizontal subtraction stroke between the two large terms, so it is transcribed as set difference.',
 'P12','high','misread symbol or index',True,False,False,False,1)
add('P12e','L16 end of first display',r'\Delta_J\cap D_i',r'D_J \cap D_i ,',r'\Delta_J\cap D_i',
 'The final raised dot belongs to the i of D_i. The paper to its right contains no separate low comma before the edge of the writing area.',
 'P12','high','text not on the page',False,True,False,False,9)
add('P13a','L17 parentheses around union expression',r'D_i\setminus\left(\bigcup_{j\ne i}\unsure{D_i\cap D_j}\right)',r'D_i \setminus \bigcup_{j \neq i} (D_i \cap D_j)',r'D_i\setminus\left(\bigcup_{j\ne i}\unsure{D_i\cap D_j}\right)',
 'A tall curved stroke is visible immediately after the slash and before the union, while the final closing curve is after the compressed D_i cap D_j group. I therefore retain C’s outer grouping. The compressed interior letters and indices remain uncertain; no missing star is supplied to the left-hand D_{i}.',
 'P13','medium','misread symbol or index',False,True,False,False,1)
add('P13b','L17 opening Si',r'\unsure{Si|Soit}',r'Si',r'Si',
 'There is a looped S followed by a short i with detached dot. The word has neither the rounded o nor the final tall crossed t required by Soit. This clears C’s Si/Soit doubt.',
 'P13','high','misread word',True,False,False,False,2)
add('P13c','L17 cardinality variable',r'd=\operatorname{card}J',r'\alpha = \operatorname{card} J',r'd=\operatorname{card}J',
 'The variable has a small rounded bowl and a separate high ascender on its right, the same d form as the subsequent codimension variable; an alpha has no such tall d stem here.',
 'P13','high','misread symbol or index',False,True,False,True,1)
add('P13d','L17 on after comma',r'\unsure{on}',r'on',r'on',
 'After the comma the short group has a shallow rounded entry and one low terminal n arch. No other tall or descending letter is present. This supports on and resolves C’s confidence mark, although the very cursive connecting stroke keeps confidence medium.',
 'P13','medium','misread word',True,False,False,False,2)
add('P14a','L17 preceding second display',r'de sorte que',r'(nothing)',r'de sorte que',
 'The left-hand continuation contains the looped d/e, then sorte with its tall t, then a q descending below its low ue strokes. These three source words precede the second display in the reading order.',
 'P14','high','omission',False,True,False,False,3)
add('P14b','L18 on voit que',r'voit',r'sait',r'voit',
 'The word starts with a low angular v and rounded o, followed by a dotted i and a tall final t. It does not begin with the s/a pair of sait.',
 'P14','high','misread word',False,True,False,False,2)
add('P14c','L18 de codim d',r'de codim $d$',r'de codim $\alpha$',r'de codim $d$',
 'The variable after codim again has a round low bowl with a tall upright ascender, matching the d in d=card J; the ascender is the distinguishing stroke.',
 'P14','high','misread symbol or index',False,True,False,True,1)
add('P14d','L19 empty-set glyph',r'\varnothing',r'\emptyset',r'\phi',
 'The small oval is crossed by a long stem that descends conspicuously below it. The source glyph is a crossed phi used for the empty set, not a regularized empty-set glyph. Parent independently inspected P14 and agreed with this glyph reading.',
 'P14','high','misread symbol or index',True,True,False,False,1)
add('P15','L20 simplexe quotation',r"``simplexe''",r'« simplexe »',r"``simplexe''",
 'The opening marks are two short raised ticks, and raised closing ticks follow the word. No angled French guillemets are drawn.',
 'P15','high','other',False,True,False,False,10)
add('P16a','Margin opening sentence',r'il vaut mieux définir',r'il \uncertain{vient} \uncertain{un nouveau} \uncertain{décrire}',r'il vaut mieux définir',
 'After il, the first word has the v entry and terminal t of vaut; mieux has its long m humps, dotted i, and final crossing x. Définir shows the initial d ascender, accent, and dotted i. The stated sequence is visible on the levelled marginal crop and does not have the extra words un nouveau.',
 'P16','high','misread word',False,True,True,False,2)
add('P16b','Margin underlined sous-schéma',r'\uline{sous-schéma}',r"\uncertain{l'ensemble}",r'\uline{sous-schéma}',
 'The underlined group visibly begins sous, has a separated short hyphen, then the tall sch sequence and final ma. The underline runs under this word, which cannot be reduced to l’ensemble.',
 'P16','high','misread word',False,True,True,True,2)
add('P16c','Margin second comme before intersection',r'\unsure{comme}',r'(nothing)',r'comme',
 'A separate open c starts the low o/mm/e sequence on the next oblique line before the intersection sign. It is a repeated written comme, not a continuation of sous-schéma. This resolves C’s single-word doubt.',
 'P16','high','misread word',True,True,False,False,2)
add('P16d','Margin intersection indices',r'\bigcap_{j\in J}D_j',r'\bigcap_{i \in J} D_i',r'\bigcap_{j\in J}D_j',
 'The index below the intersection has a lower descender and hook, and the subscript of the following D has the same hooked tail. These are j, unlike the short dotted i seen in the main union index.',
 'P16','high','misread symbol or index',False,True,False,False,1)
add('P16e','Margin définir son support / sous-ouvert',r'définir son \uline{\unsure{support|sous-ouvert}}',r'\uncertain{décrire}',r'définir son \uline{\unsure{support|sous-ouvert}}',
 'Définir is followed by a separate son group and another underlined word. The underlined word has tall descending central strokes and a final t-like stroke, but the compressed joining of the middle letters does not securely distinguish support from sous-ouvert. H omits son and the whole underlined group; C’s unresolved alternatives are retained.',
 'P16','medium','omission',False,True,True,True,3)
add('P16f','Margin final set relation',r'I(x)\unsure{=|\supseteq}J',r'I(x) \supset J',r'I(x)=J',
 'Between the closing parenthesis and J there are two separate heavy horizontal bars of equal orientation. There is no right-facing curved or angular enclosure at their right ends. The complete marginal set formula was read; the equality is preserved despite the possible mathematical mismatch with a closed intersection.',
 'P16','high','misread symbol or index',True,True,False,True,1)
add('P16g','Margin comma after reference',r'(36), et',r'(36) \uncertain{et}',r'(36), et',
 'After the right parenthesis of (36), a short low comma stroke precedes the independently written et. The comma is retained.',
 'P16','high','omission',False,True,True,False,3)
add('P18','L1 four dots after I_V',r'I_V\ldots',r'$I_V$ …',r'I_V\ldots.',
 'The tight crop has four separately spaced ink dots on one horizontal level. The fourth is lighter but is an isolated round ink mark of comparable size and regular spacing. Both witnesses reduced the four points to a three-dot ellipsis.',
 'P18','high','omission',True,True,False,False,3)

# All ten packet marks are covered in packet order, including those not resolved.
markdata=[
('M0173','undecided',r'\unsure{\pi|\mathcal E}',
 'The top bar and two long descending strokes support pi, but the left side is overtraced into two loops that still admit a calligraphic E. This isolated leaf does not establish the overwritten symbol securely; retain both alternatives.','P02','medium'),
('M0174','first','convaincre',
 'Open initial c/o, an angular v in the middle, a dotted i, and compact terminal cre; no long s sequence.','P04','high'),
('M0175','undecided',r'\unsure{énoncer|annoncer}',
 'Only one low word is present, but its initial vowel and compressed central arcs are too weak to discriminate énoncer and annoncer.','P06','medium'),
('M0176','other','*',
 'Small raised crossed strokes with outward tips and a dark centre, rather than a hollow circle. Whole formula inspected.','P12','high'),
('M0177','undecided',r'\unsure{D_i\cap D_j}',
 'The whole second formula contains two compressed bowl/shaft groups with a central cap-like join; the small subscripts remain crowded under adjacent strokes. Retain the existing term doubt.','P13','medium'),
('M0178','first','Si',
 'Tall looped S and one dotted i; no o loop or final crossed t.','P13','high'),
('M0179','first','on',
 'One low rounded entry followed by a terminal n arch after the comma; the reading is supported but highly cursive.','P13','medium'),
('M0180','first','comme',
 'The separate lower-line c is open, followed by low omme humps before the intersection; it is a repeated comme.','P16','high'),
('M0181','undecided',r'\unsure{support|sous-ouvert}',
 'Underlined word has a low initial s/u-like sequence, deep central descending joins, and terminal t; those joins do not unambiguously distinguish pp from the longer sous-ouvert sequence.','P16','medium'),
('M0182','first','=',
 'Two independent parallel horizontal bars separate I(x) and J; no enclosing right-facing curve. The whole set formula is included in the crop.','P16','high')]
decisions=[dict(id=i,cote='149',scan='132',decision=d,reading=r,evidence=e,crop=crop(p),box=boxes[p],confidence=cf) for i,d,r,e,p,cf in markdata]

inventory=[]
def inv(n,kind,pos,words,hand='his hand'):
 inventory.append(dict(scan=page,sheet_kind='text',hand=hand,element=f'E{n:02}',kind=kind,position=pos,first_words_or_objects=words,transcribed='yes'))
inv(1,'text','top through y1609','précédemment à propos des; first continuous paragraph')
inv(2,'deletion','x350–510, y444–478','associés, struck under ou / before plutôt')
inv(3,'insertion','x1170–1250, y350–386','π- above conjugaison; leader to prefix position')
inv(4,'insertion','x600–1020, y555–636','pour x variable,; leader after X\\U')
inv(5,'deletion','x898–1011, y1238–1291','tout, cancelled between près and au plus')
inv(6,'deletion','x1100–1300, y1340–1424','tentative right arrow cancelled after V')
inv(7,'insertion','x1160–1205, y1328–1366','membership sign above cancelled relation')
inv(8,'insertion','x361–396, y1504–1547','de, added between pas and centre')
inv(9,'deletion','x801–974, y1484–1545','X\\U, cancelled before live U')
inv(10,'deletion','x408–1018, y1604–1680',"Considérons d'abord les")
inv(11,'text','y1680–1770',"Soit J une partie de l'ens. fini I, et soit")
inv(12,'display','x550–1650, y1740–1913','D_J^* equality and overbraced closed intersection Δ_J')
inv(13,'text','x303–688, y1994–2077','de sorte que')
inv(14,'display','x806–1252, y1911–2021','D_{i} = D_i minus union')
inv(15,'text','x310–1640, y1910–2290','Si d=card J, on voit que; Si on appelle simplexe')
inv(16,'insertion','x840–1030, y2000–2080','régulier, added between est and de codim')
inv(17,'margin note','lower left oblique, x17–535, y1670–2190','il vaut mieux définir D_J comme sous-schéma')
inv(18,'margin note','lower left foot x17–109, y2297–2347','131','thin lighter foliation hand; attribution not established')

audit=[]
def ab(n,kind,box,reading): audit.append(dict(box=f'B{n:02}',kind=kind,xyxy=box,reading=reading))
ab(1,'C/H different words',[1040,76,1160,124],'des')
ab(2,'doubtful formula',[1230,226,1644,372],r'I_x\subset\unsure{\pi|\mathcal E}_{L/K}^{\bar L}')
ab(3,'struck passage; C/H different words',[320,380,736,491],r'ou \deleted{\unsure{associés}} plutôt,')
ab(4,'insertion',[1165,342,1263,391],r'\inserted{$\pi$-}')
ab(5,'insertion',[596,559,1020,638],r'\inserted{pour $x$ variable,}')
ab(6,'C/H different words',[748,630,1290,709],'me convaincre du')
ab(7,'C/H different words',[968,969,1554,1091],r"ce qu'on vient d'")
ab(8,'C/H different words',[282,1096,1632,1225],r'\unsure{énoncer|annoncer} --- que ce sont justement, à sous-')
ab(9,'struck passage',[887,1220,1030,1304],r'\deleted{\unsure{tout}}')
ab(10,'insertion; struck passage; doubtful formula',[1011,1293,1444,1458],r'V\deleted{\unsure{\to}}\inserted{\in}\mathfrak X_{L/K}')
ab(11,'insertion; struck passage',[278,1457,1157,1609],r'pas \inserted{de} centre dans $\deleted{X\setminus U}U\ldots$)')
ab(12,'struck passage',[395,1598,1034,1691],r"\deleted{Considérons d'abord les}")
ab(13,'struck passage; C/H different words',[1045,1670,1214,1757],r"l'ens.")
ab(14,'doubtful formula',[534,1739,1655,1926],r'D_J^*=\{x\in X\mid I(x)=J\}=\overbrace{\bigcap_{j\in J}D_j}^{\Delta_J}-\bigcup_{i\in I\setminus J}\Delta_J\cap D_i')
ab(15,'C/H different words',[290,1992,690,2079],'de sorte que')
ab(16,'doubtful formula',[792,1901,1242,2024],r'D_{\{i\}}=D_i\setminus\left(\bigcup_{j\ne i}\unsure{D_i\cap D_j}\right).')
ab(17,'C/H different words; less than high confidence departure',[1241,1901,1644,2000],r'Si $d=\operatorname{card}J$, on')
ab(18,'C/H different words',[303,2063,565,2145],'voit que')
ab(19,'insertion',[840,2000,1035,2078],r'\inserted{régulier,}')
ab(20,'C/H different words',[1000,2018,1250,2092],r'codim $d$')
ab(21,'C/H different words',[764,2190,1064,2280],r"``simplexe''")
ab(22,'margin note; doubtful formula; handwritten number; C/H different words',[17,1670,535,2190],r'il vaut mieux définir $D_J$ comme \uline{sous-schéma} comme $\bigcap_{j\in J}D_j$ (36), et définir son \uline{\unsure{support|sous-ouvert}} comme $\{x\in X\mid I(x)=J\}$')
ab(23,'handwritten number; margin note',[17,2297,109,2347],'131')
ab(24,'C/H different words',[1424,81,1504,122],'....')
ab(25,'doubtful formula',[1517,2080,1599,2170],r'\phi')

doubts=[
 dict(place='L3 containing group symbol',reading=r'\unsure{\pi|\mathcal E}',alternatives=r'\pi / \mathcal E',confidence='medium',reason='Overtraced left loops and crossed upper stroke; whole formula crop P02 does not settle the exact glyph.'),
 dict(place='L4 deleted associés',reading=r'\deleted{\unsure{associés}}',alternatives='associés, with internal letters obscured',confidence='medium',reason='Cancellation shares the baseline of several letters; not every letter is independently visible in P03.'),
 dict(place='L10 verb',reading=r'\unsure{énoncer|annoncer}',alternatives='énoncer / annoncer',confidence='medium',reason='Low pale initial and middle letter joins remain ambiguous in P06.'),
 dict(place='L11 cancelled tout',reading=r'\deleted{\unsure{tout}}',alternatives='tout; lexical middle obscured',confidence='medium',reason='Heavy cancelling stroke covers the middle letters in P07.'),
 dict(place='L12 cancelled relation',reading=r'\deleted{\unsure{\to}}',alternatives='right arrow / other cancelled relation',confidence='medium',reason='Arrow-like end remains, but underlying shaft and cancellation merge in P08.'),
 dict(place='L17 second display interior',reading=r'\unsure{D_i\cap D_j}',alternatives='D_i cap D_j, with cramped subscripts',confidence='medium',reason='Small subscripts and compact bowls overlap the enclosing parenthesis in P13.'),
 dict(place='margin underlined word after son',reading=r'\uline{\unsure{support|sous-ouvert}}',alternatives='support / sous-ouvert',confidence='medium',reason='Central descenders and low connecting strokes in P16 remain ambiguous; mathematical expectation was not used to replace the written reading.')]
notes=[
 dict(id='N01',text='English: This handwritten leaf continues a discussion of local inertia groups and their proposed independence from the model X. It defines the stratum D_J^* by I(x)=J, writes the closed intersection as Delta_J, and asserts regularity and codimension d=card J, allowing the empty set. Hypotheses on the divisors are not restated here and their geometric sufficiency was not checked.'),
 dict(id='N02',text='English: The marginal note says to define D_J as a sous-schéma by the intersection, then defines its uncertain underlined support/sous-ouvert by the visibly written equality I(x)=J. Conditional on I(x) meaning the set of divisor indices through x, the support of the full intersection is I(x) containing J, whereas equality removes points on extra divisors. This is a set-membership diagnostic only. Equality is retained as ink; the uncertain underlined noun may affect the intended reading. No theorem of regularity or model independence has been proved here.'),
 dict(id='N03',text='English: The only written (36) occurs inside the diagonal marginal sentence, immediately after its intersection expression. There is no independently written equation number at the main display. The bottom-left thin numeral 131 is retained as a foliation margin entry; its hand has not been attributed to the author.'),
 dict(id='N04',text='English: The source has no opening parenthesis before ou in the fourth line, although a closing parenthesis remains after de tels sous-groupes. It is not supplied. The large curve before et me convaincre is the leader from pour x variable. Four separate dots follow I_V in the first line.'),
 dict(id='N05',text='English: No diagram or drawing is present. The large overbrace in the main equality is mathematical notation and is transcribed with the formula. Line_count counts 20 main text/display rows plus five oblique marginal rows; separate interlinear additions and the folio are inventoried separately.')]
checks=[
 dict(statement_id=f'{page}.N01',type='carried as background without fault found',outcome='Reported the page’s claims as source content only; no proof of the geometric regularity or model-independence assertions was attempted.'),
 dict(statement_id=f'{page}.N02',type='targeted proof check',outcome='By direct set membership, x belongs to every D_j for j in J iff J is contained in I(x), assuming I(x) is the incidence-index set. Equality I(x)=J additionally excludes all extra divisors. The equality in the marginal ink was not corrected.')]
notation=[
 dict(form=r'D_J^*',meaning='locally closed incidence stratum specified by I(x)=J',evidence='Main equality; raised mark is crossed/starred in P12.'),
 dict(form=r'\Delta_J',meaning='closed intersection of the divisors D_j for j in J',evidence='Triangular Delta_J label above the brace and same triangular sign after the union in P12.'),
 dict(form=r'd=\operatorname{card}J',meaning='cardinality variable used in the codimension assertion',evidence='Tall-stem lowercase d in both the cardinality and codimension positions, P13/P14.'),
 dict(form=r'\pi',meaning='group symbol intended in π-conjugaison; containing group glyph remains unresolved between pi and calligraphic E',evidence='Inserted prefix P19 is a flat roof with two upright legs; P02 group symbol has overtraced left loops.'),
 dict(form=r'\phi',meaning='empty set',evidence='A small oval crossed by a long descending stem in the regularity sentence, visible in half2 and P14; source glyph retained instead of regularizing it to an empty-set sign.')]
abbreviations=[dict(form="l'ens.",expansion="l'ensemble"),dict(form='codim',expansion='codimension'),dict(form='card',expansion='cardinal')]
hand=[
 dict(habit='Lowercase d has a rounded low bowl and a conspicuous high stem; a cursive alpha reading loses the ascender.',places='149_scan132: d=card J and de codim d',consistency='Both mathematical occurrences agree with looped d in the prose.',witness_errors='H reads alpha at both positions.'),
 dict(habit='Capital Delta is a closed triangle distinct from the rounded bowl and upright of D.',places='149_scan132: brace label and right-hand intersection term',consistency='Both Delta occurrences triangular; several neighbouring D letters rounded.',witness_errors='H reads D_J for both Delta_J labels.'),
 dict(habit='Long curved leaders may resemble opening parentheses.',places='149_scan132: pour x variable insertion; de before centre; régulier insertion',consistency='Leader path connects added words to their destinations on this page.',witness_errors='H introduces an opening parenthesis before et me convaincre.'),
 dict(habit='Inserted pi can have a flat horizontal roof and two straight legs.',places='149_scan132: prefix before conjugaison',consistency='The prefix is clear; the containing-group symbol is overtraced and cannot establish a universal shape convention on this single page.',witness_errors='No certain witness correction based on capitalization; containing-group doubt retained.'),
 dict(habit='Very low compressed o/n/e joins occur in ordinary prose.',places='149_scan132: me convaincre, ce qu’on, on voit, repeated comme in margin',consistency='Resolved only where adjacent ascenders/dots and word boundaries were visible.',witness_errors='H expands me convaincre du into une connaissance de and reads sait for voit.'),
 dict(habit='Superscript star is a small dense crossed mark, not a hollow ring.',places='149_scan132: D_J^*',consistency='Only one occurrence on the assigned leaf.',witness_errors='C offered a doubtful circular superscript.'),
 dict(habit='Ellipsis dot count can exceed three.',places='149_scan132: first line after I_V',consistency='Four regular points at this place; the lower paragraph end has three.',witness_errors='Both witnesses reduce the first set to three points.')]

coverage={
1:'Macro/editorial page marker only: scanpage{132} is the edition scan marker.',
2:'P01: des retained against H de.',
3:'P18: both witnesses normalized four handwritten dots; retain four.',
4:'M0173/P02: uncertainty-only difference; pi/calligraphic E remains undecided, not a change row.',
5:'P03a: no opening parenthesis; deletion alignment reviewed.',
6:'Same struck word associés in both; preserve C local reading order below ou before plutôt; uncertainty retained and crop P03 inspected.',
7:'P04b: curve is insertion leader, not opening parenthesis.',
8:'P04a: et me convaincre du.',
9:'P05: ce qu’on.',
10:'P06a and M0175: retain one doubtful verb énoncer/annoncer, reject H être présumé.',
11:'P06b: no additional à conjugaison — et.',
12:'P08: cancelled relation under inserted membership sign is retained in its written position.',
13:'Macro-only ellipsis comparison at paragraph end; three dots visible in P09, both content readings agree.',
14:'P11: one heavily retraced l’ens.; no separately readable extra struck l’.',
15:'P12a: remove uninscribed main-display tag; (36) occurs in margin.',
16:'P12b and M0176: star rather than circle.',
17:'Macro spacing only: H uses \\, inside opening set brace, not an ink comma.',
18:'Macro spacing only: H uses \\, inside closing set brace, not an ink comma.',
19:'P12c: triangular Delta_J label above brace.',
20:'P12d: diagonal set-difference slash in union index.',
21:'P12c: triangular Delta_J in right-hand term.',
22:'P12e: no separate comma after final D_i.',
23:'P14a: de sorte que is present.',
24:'P13a: retain C enclosing parenthesis before union.',
25:'P13a: no new opening parenthesis after the union index; whole formula remains partly doubtful.',
26:'P13b/P13c: Si and Latin d; C Si/Soit mark resolved.',
27:'P14b: voit, not sait.',
28:'P14c: Latin d, not alpha.',
29:'P15: raised double ticks, not guillemets.',
30:'P16a: il vaut mieux définir.',
31:'P16b/P16c: sous-schéma followed by repeated comme.',
32:'P16d: j under intersection.',
33:'P16d: j on D_j.',
34:'P16g: comma after (36).',
35:'P16e: définir son and underlined doubtful support/sous-ouvert retained.',
36:'P16f/M0182: two horizontal bars, equality.',
37:'Actual handwritten 131 retained and inspected in P17; H’s explanatory note is editorial, not source text.'}
review=[
 dict(text=r'\deleted{\unsure{associés}}',scope_attachment='Only the word below ou / immediately before plutôt is cancelled; no strike continues through plutôt.',evidence='P03: dark horizontal cancellation spans the low word; top-line plutôt remains uncrossed.'),
 dict(text=r'\inserted{$\pi$-}',scope_attachment='Prefix attached to conjugaison, not to the preceding classes.',evidence='P19: small prefix above the start of conjugaison and curved descending leader.'),
 dict(text=r'\inserted{pour $x$ variable,}',scope_attachment='Inserted after x in X\\U and its comma, before et me convaincre.',evidence='P04 and half1: long leader curves left/down into that gap.'),
 dict(text=r'\deleted{\unsure{tout}}',scope_attachment='Only tout is cancelled; près and au plus are live.',evidence='P07 and half2: strike has compact word length and does not extend to neighbours.'),
 dict(text=r'\deleted{\unsure{\to}}\inserted{\in}',scope_attachment='Membership sign replaces the cancelled relation between V and calligraphic X.',evidence='P08: new membership sign is above the original relation; original relation remains under the strike.'),
 dict(text=r'\inserted{de}',scope_attachment='Added between pas and centre.',evidence='P09: word above the gap with a leader down to the start of centre.'),
 dict(text=r'\deleted{X\setminus U}U',scope_attachment='Only first X\\U is crossed; the following U and trailing three dots are live.',evidence='P09: multiple bars end at the old U; next U is clear to their right.'),
 dict(text=r"\deleted{Considérons d'abord les}",scope_attachment='Complete one-line abandoned beginning, all three textual units struck.',evidence='P10: a continuous rising stroke crosses from Considérons through les.'),
 dict(text=r"l'ens.",scope_attachment='No extra deletion accepted here; the l is retraced but only one l’ group is separately legible.',evidence='P11: one apostrophe and one following ens. group; review this contested retracing independently.'),
 dict(text=r'\inserted{régulier,}',scope_attachment='Added after est and before de codim.',evidence='P14: added word lies above est/de and the leader drops at their gap; the comma belongs to the insertion.'),
 dict(text='Oblique marginal note',scope_attachment='Comment on the main stratum/intersection definition; it remains a separate margin block rather than an inline continuation.',evidence='P16: five diagonal lines with underlined sous-schéma and the second uncertain noun; embedded (36) stays in this note.')]
report=dict(page=page,reader='reader_c',line_count=25,changes=changes,decisions=decisions,inventory=inventory,audit_boxes=audit,doubts=doubts,notes=notes,check_events=checks,notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=[dict(row=i,disposition=coverage[i]) for i in range(1,38)],deletion_insertion_review=review)
out=Path('work/reports')/page/'report.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(out),'changes':len(changes),'marks':len(decisions),'audit_boxes':len(audit),'crops':len(boxes),'diff_rows':len(coverage),'doubts':len(doubts)},ensure_ascii=False))
