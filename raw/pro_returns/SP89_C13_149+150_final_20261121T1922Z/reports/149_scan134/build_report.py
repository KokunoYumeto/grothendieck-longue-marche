import json
from pathlib import Path
page='149_scan134'
boxes={'P01':[313,190,1053,344],'P02':[320,326,897,431],'P03':[925,319,1600,421],'P04':[1412,412,1580,490],'P05':[307,542,604,644],'P06':[1169,512,1267,583],'P07':[656,579,1521,774],'P08':[643,880,1648,1051],'P09':[298,1033,1657,1217],'P10':[600,1222,1047,1586],'P11':[287,1574,1657,1856],'P12':[233,1781,1345,2145],'P13':[277,2116,1612,2247],'P14':[276,2218,1620,2351],'P15':[14,2296,98,2348],'P16':[820,14,976,135]}
def cp(k): return f'crops/{page}_{k}.png'
changes=[]
def add(i,place,c,h,final,e,p,confidence,kind,ac,ah,mh,con,cat):
 changes.append(dict(id=i,place=place,c=c,h=h,final=final,evidence=e,crop=cp(p),box=boxes[p],confidence=confidence,kind=kind,against_c=ac,against_h=ah,marked_in_h=mh,consequential=con,error_category=cat))
add('P01a','L3 article before inserted début',r"c'est le \inserted{début de la suite d'homotopie du} fibré",r"c'est la \add{\uncertain{début} de la suite d'homotopie du} fibré",r"c'est le \inserted{début de la suite d'homotopie du} fibré",
 'The baseline article has a tall looped l and a small open terminal e, without an enclosed a bowl. The added phrase sits above the gap between this le and fibré; début, de la suite, d’homotopie, and du can each be followed across that added line.','P01','high','misread word',False,True,False,False,2)
add('P01b','L3 moralement',r'\unsure{moralement}',r'\uncertain{morale}',r'\unsure{moralement}',
 'After the tall l, the ink continues in a long low joined sequence to a raised t-like finish before the comma. H’s morale stops before that continuation. The highly compressed final syllables do not justify clearing C’s moralement doubt or silently expanding a possible contraction.','P01','medium','misread word',False,True,True,False,2)
add('P02','L4 disques sur D_J',r'disques sur $D_J$',r'disques \struck{\ill{}} sur $D_J$',r'disques sur $D_J$',
 'The dark retracing is confined to the opening s of sur, which joins directly to u and r. There is no separate word or separate cancellation bar in the gap after disques. The visible reading is one live sur.','P02','high','text not on the page',False,True,False,False,9)
add('P03','L4 lui-= parenthesis',r'(savoir $U_J$ lui-$=$)',r'(\uncertain{savoir} $U_J$ \uncertain{homotope} $=$ )',r'(savoir $U_J$ lui-$=$)',
 'After U_J, there is a tall looped l, a low u, and a dotted i, followed by a distinct short hyphen and two horizontal equality bars. There is no initial h or sequence matching homotope. The equals-sign abbreviation is retained exactly.','P03','high','misread word',False,True,True,False,2)
add('P05','L6 zéro à g',r'zéro à g',r'\uncertain{zéro} à \uncertain{gauche}',r'zéro à g',
 'After à, only one looped g with a long lower loop is present before the comma. There are no following auche letters and no separate abbreviation stop.','P05','high','abbreviation expanded or spelling modernised',False,True,True,False,8)
add('P06','L6 cancelled symbol after du',r'\deleted{\unsure{\pi|\mathcal E}}',r'\struck{\ill{}}',r'\deleted{\unsure{\pi|\mathcal E}}',
 'The cancelled ink still contains a roof-like horizontal stroke, a long descending left stroke, and looped/crossed material to its right. Those shapes support the stated pi/E alternatives, although the cancellation prevents choosing between them. It is not left as wholly unreadable.','P06','medium','readable ink left as \\ill{}',False,True,False,False,5)
add('P07','L7 identification below pi_1(fibre)',r'\underset{\substack{\Vert\\ T^J}}{\pi_1(\text{fibre})}',r'\pi_1(\text{fibre}) ; \note{sous « $\pi_1(\text{fibre})$ » est écrit « $= T^J$ ».}',r'\underset{\substack{\Vert\\ T^J}}{\pi_1(\text{fibre})}',
 'Two short vertical parallel strokes are immediately below the fibre fundamental group, and T with a raised J is below them. This written stacked identification belongs to the formula, not to an editorial explanatory note; its relation is vertical.','P07','high','omission',False,True,False,True,3)
add('P08a','L10 quotation around l’injection',r"``l'injection''",r'« l’injection »',r"``l'injection''",
 'Two raised short ticks stand at each end of l’injection. Neither end has an angled guillemet.','P08','high','other',False,True,False,False,10)
add('P08b','L10 punctuation following U',r'$U_J\longrightarrow U$ ;',r'$U_J \to U$,',r'$U_J\longrightarrow U$ ;',
 'The punctuation has a separate upper dot and a lower curved comma stroke, so it is a semicolon, not a comma alone.','P08','high','other',False,True,False,False,10)
add('P08c','L10 cancelled added devrait above elle',r'\deleted{elle}\inserted{\deleted{devrait}}',r'\struck{\uncertain{elle}} ; \add{\uncertain{devrait}} [after devrait avoir]',r'\deleted{elle}\inserted{\deleted{devrait}}',
 'Elle is crossed on the original line; devrait is written above it, joined by a curved leader, and has its own horizontal cancellation through the word. The added word is therefore itself deleted and attached at this earlier position, not live beside the later replacement a.','P08','high','deletion state (struck given live or live given struck)',False,True,True,True,7)
add('P09','L11 replacement after on',r'on \deleted{devrait avoir}\inserted{a} un diagramme',r'on \struck{devrait avoir} \add{\uncertain{devrait}} un diagramme',r'on \deleted{devrait avoir}\inserted{a} un diagramme',
 'A single small rounded a is above the cancellation through devrait avoir. Its bowl and short terminal stroke are visible; it is not a multi-letter devrait. The separate cancelled devrait above elle is visible in P08.','P09','high','misread word',False,True,True,True,2)
add('P10a','First diagram left downward-arrow label',r'\unsure{\varepsilon|i}',r'i',r'\varepsilon',
 'The label has two joined curved lobes and a central notch. There is no detached dot above a simple upright stem, as would be required for i. The whole five-object diagram was inspected with this label.','P10','high','misread symbol or index',True,True,False,False,1)
add('P10b','First diagram homotopy-equivalence label',r"\text{équiv. d'homotopie}",r"\text{équiv.\ d'homotopie}",r"\substack{\text{équiv}\\\text{d'homotopie}}",
 'The upper label line ends in the v stroke. The nearby detached dots are over the i letters, and no independently visible low stop follows the v. The second line reads d’homotopie. The short form is kept without supplying a period.','P10','high','abbreviation expanded or spelling modernised',True,True,False,False,8)
add('P10c','First diagram side of upward-arrow label',r'D_J \arrow[u,"\text{équiv. d’homotopie}"]',r'D_J \arrow[u,"\text{équiv. d’homotopie}"’]',r'D_J \arrow[u,"{\substack{\text{équiv}\\\text{d’homotopie}}}"’]',
 'Both words of the two-line label are on the right of the upward arrow from D_J to X_J. The draft uses the swapped TikZ label side to preserve that location.','P10','high','drawing or diagram',True,False,False,False,4)
add('P11a','L18 punctuation after d’homotopie',r"d'homotopie,",r"d'homotopie —",r"d'homotopie,",
 'The continuation pie at the beginning of the next physical line is followed by a short descending comma. There is no independent long dash between the word and the cancelled relative.','P11','high','other',False,True,False,False,10)
add('P11b','L18 inserted de celle relative',r'\deleted{relative}\inserted{de celle relative}',r'\add{de cette relation} \struck{relative}',r'\deleted{relative}\inserted{de celle relative}',
 'The addition has de, then celle with two looped l ascenders, then relative with a dotted i and final ve. It is written immediately above the crossed-out relative and replaces that word. There are no crossed t stems of cette, and the last word does not end in -tion.','P11','high','misread word',False,True,False,True,2)
add('P11c','L18 colonne replacing ligne',r'\deleted{ligne}\inserted{colonne}',r'\struck{\uncertain{ligne}} \add{\uncertain{cohomologique}}',r'\deleted{ligne}\inserted{colonne}',
 'The short upper word begins c/o, has one tall l, then a compact onne ending. It has none of the additional homologi letters required by cohomologique. The lower ligne is crossed; its g descender remains below the cancellation.','P11','high','misread word',False,True,True,True,2)
add('P11d','L18–L19 dans celle relative à la seconde',r'dans celle relative à la seconde',r'dans cette relation : $T^J$ \uncertain{scindée}…',r'dans celle relative à la seconde',
 'Dans celle ends the upper line, with the paired l strokes visible in celle. The next text line begins relative à la and ends seconde, whose s/e/c sequence and tall d survive. T^J belongs to the diagram below and is not prose between these words. No trailing ellipsis is written after seconde.','P11','high','misread word',False,True,True,True,2)
add('P12a','Long diagram fibre term',r'\pi_1(\unsure{\bar G_m^{\times J}})',r'\pi_1(\overline{\mathbb{G}}_m^{\,J})',r'\pi_1(\bar G_m^{\times J})',
 'The capital G has a separate bar above it, m is below, and the superscript begins with two crossing strokes before the hooked J. The multiplication cross is actual ink and cannot be replaced by mere superscript spacing. The whole diagram was read and the C term doubt is resolved.','P12','high','misread symbol or index',True,True,False,True,1)
add('P12b','Long diagram lower continuation marks',r'\unsure{\ldots|--}',r'\cdots',r'--',
 'At the lower left there are two short horizontal marks: the first shorter and the second longer. They are not three separate round dots like the top-left continuation. C’s alternative of two dashes is selected.','P12','high','misread symbol or index',True,True,False,False,1)
verticals=[
 ('P12v1','above the fibre term',r'\overset{\substack{T^J\\\wr}}{\pi_1(\unsure{\bar G_m^{\times J}})}',r'\pi_1(\overline{\mathbb G}_m^{\,J})\arrow[u,no head,"\wr"’]',r'\overset{\substack{T^J\\\wr\!\vert}}{\pi_1(\bar G_m^{\times J})}'),
 ('P12v2','above pi_1(U_J)',r'\overset{\substack{\mathcal E_{U_J}\\\wr}}{\pi_1(U_J)}',r'\pi_1(U_J)\arrow[u,no head,"\wr"’]',r'\overset{\substack{\mathcal E_{U_J}\\\wr\!\vert}}{\pi_1(U_J)}'),
 ('P12v3','above pi_1(X_J)',r'\overset{\substack{\mathcal E_{D_J}\\\wr}}{\pi_1(X_J)}',r'\pi_1(X_J)\arrow[u,no head,"\wr"’]',r'\overset{\substack{\mathcal E_{D_J}\\\wr\!\vert}}{\pi_1(X_J)}'),
 ('P12v4','below pi_1(U_barxi)',r'\underset{\substack{\wr\\\pi_{U/K}}}{\pi_1(U_{\bar\xi})}',r'\pi_1(U_{\overline\xi})\arrow[d,no head,"\wr"’]',r'\underset{\substack{\wr\!\vert\\\pi_{U/K}}}{\pi_1(U_{\bar\xi})}'),
 ('P12v5','below pi_1(U)',r'\underset{\substack{\wr\\\mathcal E_U}}{\pi_1(U)}',r'\pi_1(U)\arrow[d,no head,"\wr"’]',r'\underset{\substack{\wr\!\vert\\\mathcal E_U}}{\pi_1(U)}'),
 ('P12v6','below pi_1(xi)',r'\underset{\substack{\wr\\\mathcal E_{\unsure K}}}{\pi_1(\xi)}',r'\pi_1(\xi)\arrow[d,no head,"\wr"’]',r'\underset{\substack{\wr\!\vert\\\mathcal E_{\unsure{K|U}}}}{\pi_1(\xi)}')]
for i,place,c,h,final in verticals:
 add(i,'Long diagram vertical identification '+place,c,h,final,
  'This identification contains a curved upright stroke on the left and a distinct straight upright stroke beside it. Both are reproduced vertically as \\wr\\!\\vert; a lone \\wr omits the straight member. H’s separate no-head vertical rule plus curved label already represents the two-member orientation, so its different macro arrangement is not counted as a separate textual error.','P12','high','misread symbol or index',True,False,False,False,1)
add('P15','Bottom-left foliation',r'\margin{133}',r'(nothing)',r'\margin{133}',
 'The lower-left corner has three thin handwritten digits: one upright 1 followed by two separate double-bowled 3 forms. They are retained as foliation in a lighter hand, not promoted to an authorial page number.','P15','high','omission',False,True,False,False,3)

marks=[
('M0204','undecided',r'\unsure{moralement}','The ending continues beyond morale to a t-like terminal, but the low compressed strokes do not settle every syllable or exclude a contraction.','P01','medium'),
('M0205','first',r'\varepsilon','Two joined lobes and central notch; no separate dot above an upright i stem. Whole first diagram read.','P10','high'),
('M0206','first',r'\bar G_m^{\times J}','Distinct bar over G, lower m, raised two-stroke cross and J; all belong to the same fibre term. Whole exact-sequence diagram read.','P12','high'),
('M0207','alternative','--','Two short horizontal strokes, not three round points, at the lower left.','P12','high'),
('M0208','undecided',r'\unsure{-|\to}','The horizontal connector between pi_1(U) and pi_1(xi) thickens at the right, but does not yield two separately readable head strokes.','P12','medium'),
('M0209','undecided',r'\unsure{K|U}','The subscript is narrower than the U in the adjacent E_U and has an upright plus a possible fork/curved branch, favouring K. The compressed join also admits U, so the expected K is not imposed.','P12','medium'),
('M0210','undecided',r'\unsure{-|\to}','The complete T^J-to-pi_{U/K} formula has a short horizontal relation with only a slightly dark terminal and no secure arrowhead.','P14','medium'),
('M0211','undecided',r'\unsure{-|\to}','The complete pi_2(D_J)-to-T^J formula has a short horizontal relation ending in a small hook; dash versus abbreviated arrow remains unsettled.','P14','medium')]
decisions=[dict(id=i,cote='149',scan='134',decision=d,reading=r,evidence=e,crop=cp(p),box=boxes[p],confidence=c) for i,d,r,e,p,c in marks]

inventory=[]
def inv(n,kind,pos,text,hand='his hand'):
 inventory.append(dict(scan=page,sheet_kind='text',hand=hand,element=f'E{n:02}',kind=kind,position=pos,first_words_or_objects=text,transcribed='yes'))
inv(1,'text','top first line','et on choisit un plongement')
inv(2,'insertion','top edge x840–930, y20–86','L- added before plongement')
inv(3,'text','x315–1630, y160–610','C’est par cela que (37); discussion of fibre and possible zero on the left')
inv(4,'insertion','x365–1040, y211–269','début de la suite d’homotopie du, before fibré')
inv(5,'deletion','x1188–1242, y530–565','cancelled pi/E after à cause du')
inv(6,'display','x675–1497, y586–748','pi_2(bar D_J) to pi_1(fibre), vertical identification T^J and (?)!')
inv(7,'text','x327–1080, y727–783','Mais considérons l’hom')
inv(8,'display','x655–1033, y823–937','E_{U_J}^{tilde U_J} to E_U^{bar L}')
inv(9,'text','x320–1660, y947–1200','induit par l’injection; heuristiquement on a un diagramme commutatif')
inv(10,'deletion','x1458–1546, y951–988','elle')
inv(11,'insertion','x1450–1631, y887–962','devrait, added above elle with leader and itself cancelled')
inv(12,'deletion','x1470–1630, y891–925','the added devrait is crossed out')
inv(13,'deletion','x885–1288, y1048–1088','devrait avoir')
inv(14,'insertion','x1088–1127, y1035–1059','a above cancelled devrait avoir')
inv(15,'deletion','x327–670, y1100–1141','induit par')
inv(16,'diagram','x600–1047, y1222–1586','U_J to U over X_J to Spec K=xi; D_J below X_J')
inv(17,'text','x300–1657, y1580–1843','d’où un hom. de suites exactes d’homotopie; first/second column discussion')
inv(18,'deletion','x448–624, y1685–1730','relative')
inv(19,'insertion','x390–680, y1646–1685','de celle relative, replacing relative')
inv(20,'deletion','x1135–1290, y1666–1730','ligne')
inv(21,'insertion','x1125–1283, y1637–1673','colonne above cancelled ligne')
inv(22,'diagram','x233–1345, y1781–2145','two exact sequences with four downward arrows and stacked identifications')
inv(23,'text','x279–1620, y2135–2347','qui montre que; conditional injectivity argument')
inv(24,'insertion','x536–767, y2126–2189','le composé, after que and before the first displayed inline composite')
inv(25,'margin note','x14–98, y2296–2348','133','thin lighter foliation hand; authorial attribution not established')

# Read the two source-faithful diagram blocks from the just-written assigned-page draft.
draft=(Path('work/reports')/page/'draft.tex').read_text()
def diagram_blocks(s):
 out=[];at=0
 while True:
  a=s.find('\\diagram{',at)
  if a<0:return out
  b=a+len('\\diagram{');level=1;k=b
  while level:
   if s[k]=='{':level+=1
   elif s[k]=='}':level-=1
   k+=1
  out.append(s[a:k]);at=k
figs=diagram_blocks(draft)
audit=[]
def ab(n,kind,box,reading):audit.append(dict(box=f'B{n:02}',kind=kind,xyxy=box,reading=reading))
ab(1,'insertion',[820,14,976,135],r'\inserted{$L$-}')
ab(2,'handwritten number',[962,153,1082,223],'(37)')
ab(3,'insertion; C/H different words',[313,202,1053,344],r"le \inserted{début de la suite d'homotopie du} fibré, \unsure{moralement},")
ab(4,'struck passage; C/H different words',[568,333,706,417],'sur')
ab(5,'C/H different words',[925,319,1600,421],r'(savoir $U_J$ lui-$=$)')
ab(6,'struck passage; C/H different words',[1412,412,1580,490],r'\unsure{un|\deleted{les}}')
ab(7,'handwritten number; C/H different words',[307,542,604,644],'zéro à g,')
ab(8,'struck passage; doubtful formula',[1169,512,1267,583],r'\deleted{\unsure{\pi|\mathcal E}}')
ab(9,'handwritten number; doubtful formula',[656,579,1521,758],r'\pi_2(\bar D_J)\longrightarrow\underset{\substack{\Vert\\T^J}}{\pi_1(\text{fibre})}\qquad (?)!')
ab(10,'insertion; struck passage; C/H different words',[643,880,1648,1051],r"``l'injection'' $U_J\longrightarrow U$ ; \deleted{elle}\inserted{\deleted{devrait}}")
ab(11,'insertion; struck passage; C/H different words',[869,1032,1300,1095],r'\deleted{devrait avoir}\inserted{a}')
ab(12,'struck passage',[320,1090,681,1147],r'\deleted{induit par}')
ab(13,'doubtful formula; C/H different words',[600,1222,1047,1586],figs[0])
ab(14,'insertion; struck passage; C/H different words',[380,1638,689,1745],r'\deleted{relative}\inserted{de celle relative}')
ab(15,'insertion; struck passage; C/H different words',[1115,1633,1311,1739],r'\deleted{ligne}\inserted{colonne},')
ab(16,'C/H different words',[1331,1666,1607,1734],'dans celle')
ab(17,'C/H different words',[302,1769,906,1844],'relative à la seconde')
ab(18,'handwritten number; doubtful formula',[233,1781,1345,2145],figs[1])
ab(19,'insertion',[528,2117,772,2195],r'\inserted{le composé}')
ab(20,'handwritten number; doubtful formula',[756,2136,1311,2222],r'\pi_2(D_J)\longrightarrow T^J\longrightarrow\pi_{U/K}')
ab(21,'handwritten number; doubtful formula',[862,2220,1265,2348],r'T^J\unsure{-|\to}\pi_{U/K}; \pi_2(D_J)\unsure{-|\to}T^J')
ab(22,'handwritten number; margin note',[14,2296,98,2348],'133')

doubts=[
 dict(place='L3 moralement',reading=r'\unsure{moralement}',alternatives='moralement; possibly compressed contraction, not safely separable',confidence='medium',reason='Final low strokes are extremely compressed; P01 shows continuation beyond morale but does not settle the whole ending.'),
 dict(place='L5 word before zéro',reading=r'\unsure{un|\deleted{les}}',alternatives='un live / les cancelled',confidence='medium',reason='P04 has a tall loop at the left and dark retracing through the low joins. This does not securely separate C’s un from H’s cancelled les; no certainty is claimed.'),
 dict(place='L6 cancelled symbol',reading=r'\deleted{\unsure{\pi|\mathcal E}}',alternatives=r'\pi / \mathcal E',confidence='medium',reason='P06 contains overlapping roof, stem, and loop strokes beneath cancellation; the lexical symbol cannot be resolved.'),
 dict(place='Long diagram top incoming connector',reading=r'\unsure{-|\to}',alternatives='dash / right arrow',confidence='medium',reason='P12 shows a short downturned terminal but no secure complete arrowhead; added uncertainty only, not counted as a correction.'),
 dict(place='Long diagram lower incoming connector',reading=r'\unsure{-|\to}',alternatives='dash / right arrow',confidence='medium',reason='P12 shows a slightly bent dark right end comparable to the upper lead-in; a complete head is not separately readable.'),
 dict(place='Long diagram pi_1(U) to pi_1(xi)',reading=r'\unsure{-|\to}',alternatives='dash / right arrow',confidence='medium',reason='The terminal thickening does not yield clear two-sided arrowhead strokes; C’s doubt remains.'),
 dict(place='Long diagram lower-right group subscript',reading=r'\mathcal E_{\unsure{K|U}}',alternatives='K / U',confidence='medium',reason='Narrow upright-plus-branch favours K, but its compressed join is also U-like. The adjacent E_U is fuller; the expected mathematical label is not used to force certainty.'),
 dict(place='Final paragraph injectivity formula',reading=r'T^J\unsure{-|\to}\pi_{U/K}',alternatives='dash / right arrow',confidence='medium',reason='P14 retains a short horizontal stroke with a weak dark terminal, not a secure head.'),
 dict(place='Last-line vanishing formula',reading=r'\pi_2(D_J)\unsure{-|\to}T^J',alternatives='dash / right arrow',confidence='medium',reason='P14 shows a short horizontal stroke and small return at its right end; the head is not sufficiently distinct.')]
notes=[
 dict(id='N01',text='English: The page chooses an L-embedding into the algebraic closure and comments on the construction numbered (37). The author describes a fibre heuristically as a product of discs and writes “j’ai eu un peu peur d’y mettre un zéro à g”, followed by a boundary map pi_2(bar D_J) to pi_1(fibre), identified vertically with T^J, and the explicit question/exclamation “(?)!”. These are the author’s doubts, not editorial conclusions. The construction (37) itself is outside this assigned page.'),
 dict(id='N02',text='English: A five-object diagram is used to motivate a morphism between homotopy exact sequences. The source identifies pi_2(xi) with zero and concludes that the composite pi_2(D_J) to T^J to pi_{U/K} is zero. It then states conditionally that injectivity of T^J to pi_{U/K} implies the first boundary map is zero. The formal diagram implication is valid once the displayed commutative morphism of sequences and the stated identifications exist: naturality gives g composed with delta equal to delta-prime composed with a, and a has zero target. If g is injective, delta is zero. No geometric existence of the fibrations, comparison theorem, or asserted injectivity is verified by this formal check.'),
 dict(id='N03',text='English: The lower-right group label is not normalized to the mathematically expected E_K: the draft retains K|U because the compressed subscript admits both shapes. The six other stacked identification signs contain a curved upright beside a straight upright; they are encoded consistently as wr plus a vertical stroke, while the two pi_2 identifications and the earlier fibre identification use two straight vertical strokes. None is turned into a horizontal equality.'),
 dict(id='N04',text='English: The opening article is le; the added beginning-of-homotopy-sequence phrase attaches before fibré. The first failed reformulation after the injection has both elle and the added devrait cancelled; the later devrait avoir is replaced by a. Relative is replaced by de celle relative, and ligne by colonne. These local revision states are retained individually.'),
 dict(id='N05',text='English: There are two genuine commutative diagrams and no separate drawing. The light bottom-left 133 is retained as foliation of unestablished hand. Line_count counts 26 principal text/display/object rows; interlinear revisions, individual arrow-only levels, and foliation are inventoried separately. The word before zéro and several arrowheads remain open for independent reading.')]
checks=[
 dict(statement_id=f'{page}.N01',type='carried as background without fault found',outcome='Recorded the author’s description and explicit concern; neither the external construction (37) nor the geometric fibration was established in this reading.'),
 dict(statement_id=f'{page}.N02',type='targeted proof check',outcome='Checked the formal commutative-square implication: with a:pi_2(D_J) to pi_2(xi)=0 and g delta = delta-prime a, the composite g delta is zero. If g is injective, delta is zero. This is conditional on the source diagram and identifications, not a proof of their geometric validity.')]
notation=[
 dict(form=r'\mathcal E_{U_J}^{\tilde U_J}\longrightarrow\mathcal E_U^{\bar L}',meaning='homomorphism induced by the stated injection U_J to U',evidence='Central displayed group map and immediately following prose.'),
 dict(form=r'T^J',meaning='group identified with the fundamental group of the fibre and with pi_1(bar G_m^{times J})',evidence='First displayed vertical identity in P07 and upper fibre-column identification in P12.'),
 dict(form=r'\varepsilon',meaning='label of U_J to X_J in the first diagram',evidence='P10 has a two-lobed epsilon shape to the left of the downward arrow.'),
 dict(form=r'\Vert',meaning='two straight vertical strokes identifying stacked objects',evidence='Under pi_1(fibre), between the two upper pi_2 terms, and between pi_2(xi) and 0.'),
 dict(form=r'\wr\!\vert',meaning='curved upright plus straight upright used for the six other stacked identifications; vertical analogue of an isomorphism sign',evidence='P12 shows the two separate members at every non-leftmost identification; both stroke count and vertical orientation retained.'),
 dict(form=r'\mathcal E_{\unsure{K|U}}',meaning='lower-right group identified with pi_1(xi); exact written subscript uncertain',evidence='P12 compressed narrow letter with possible fork, compared to adjacent fuller U.'),
 dict(form='lui-=',meaning='lui-même; author’s equals-sign abbreviation for même',evidence='P03 clearly has lui, a hyphen, and two horizontal bars.')]
abbreviations=[dict(form='g',expansion='gauche'),dict(form='hom',expansion='homomorphisme'),dict(form='hom.',expansion='homomorphisme'),dict(form='équiv',expansion='équivalence'),dict(form='lui-=',expansion='lui-même')]
hand=[
 dict(habit='Epsilon may be a very small pair of joined lobes; it lacks the separate dot of i.',places='149_scan134, first diagram left vertical label',consistency='Only one labelled epsilon here; neighbouring i dots are detached.',witness_errors='H reads i; C’s epsilon/i doubt is resolved to epsilon.'),
 dict(habit='A curved upright beside a straight upright is the author’s vertical isomorphism convention.',places='149_scan134, all six non-leftmost stacked identifications in the long diagram',consistency='Each inspected occurrence has the two members; the leftmost pi_2 pairs are both straight.',witness_errors='C’s lone wr suppresses the straight member; H’s separate no-head rule plus wr already expresses both members.'),
 dict(habit='A simple g can be an unpunctuated abbreviation rather than the full word gauche.',places='149_scan134, zéro à g',consistency='Only this occurrence on the assigned leaf.',witness_errors='H expands to gauche.'),
 dict(habit='Equals sign stands for même after lui-.',places='149_scan134, parenthesis savoir U_J lui-=',consistency='Two clear horizontal bars after the separate hyphen.',witness_errors='H misreads lui- as homotope.'),
 dict(habit='Insertion leaders can curl back toward a cancelled word and the addition itself may also be cancelled.',places='149_scan134, added devrait above elle',consistency='The long curved leader and separate horizontal strike are distinguishable.',witness_errors='H moves this added devrait to the later verb replacement and does not retain its cancelled state.'),
 dict(habit='Small K may compress into an upright and curved branch resembling U.',places='149_scan134, lower-right group label',consistency='Not sufficiently established to settle the subscript; the larger K in Spec K and in pi_{U/K} is clearer.',witness_errors='No certain correction made; K|U retained instead of silently normalizing.'),
 dict(habit='Connector tips can be a darkened end or short return, without a complete visible head.',places='149_scan134, two incoming sequence connectors, one internal lower connector, final two formulas',consistency='Both clear chevrons and these weak terminals occur on the page; they are not made uniform.',witness_errors='H supplies definite arrows at uncertain places; C itself already marks three of them doubtful.')]

coverage={
1:'Macro/editorial scanpage marker only; no source-text difference.',
2:'Same dash in different TeX/Unicode spelling; not a source-text difference.',
3:'P01a: le retained, not la.',
4:'P01b/M0204: moralement remains doubtful; visible continuation excludes the shorter morale reading.',
5:'P03: lui-=, preserving the author’s abbreviation.',
6:'Same dash, macro/Unicode spelling only.',
7:'P04 inspected; unresolved un / cancelled les. Added uncertainty only, recorded in doubts and audit B06, not counted as a correction.',
8:'P05: g is not expanded to gauche.',
9:'P06: cancelled pi/E alternatives retained; no certainty claimed.',
10:'P07: T^J restored to its written vertical identification in the formula.',
11:'Macro spacing only: H’s \\, is not a written comma.',
12:'P07: H’s explanatory note is editorial; its described source ink is transcribed within the displayed formula.',
13:'P08a: raised ticks, not guillemets.',
14:'P08b: semicolon has upper dot plus lower comma.',
15:'P08c: added devrait is itself cancelled above elle.',
16:'P09: the live replacement is a.',
17:'TikZ row/column spacing parameters only.',
18:'P10a/M0205: epsilon resolved against i.',
19:'P10c: upward-arrow label belongs on its right; side is corrected, not treated as cosmetic.',
20:'P11a: comma after homotopie; deletion of relative preserved as also present in H elsewhere.',
21:'P11b: de celle relative, not de cette relation.',
22:'P11c: colonne, not cohomologique.',
23:'P11d: dans celle relative à la seconde; T^J is the following diagram label.',
24:'TikZ row-spacing syntax only.',
25:'TikZ diagram organization only; source objects are collated in their actual positions.',
26:'The incoming top connector now has an explicit dash/arrow doubt. C/H head disagreement remains unresolved; added uncertainty only.',
27:'Same upper identification objects, organized by overset in C and separate row in H; no omission once layout is compared.',
28:'Same vertical straight pair for pi_2; different row/arrow macro arrangement only.',
29:'T^J is present in both source readings, with different serialization order.',
30:'P12a/M0206: actual multiplication cross before J; H’s spacing macro is not that ink.',
31:'P12v1: retain two-member curved-plus-straight vertical relation; H’s rule-plus-label is a macro variant.',
32:'E_{U_J} is the same source object in different diagram serialization order.',
33:'P12v2: both vertical members retained.',
34:'E_{D_J} is the same source object in different serialization order.',
35:'P12v3: both vertical members retained.',
36:'P12b/M0207: two short horizontal continuation marks in the lower row.',
37:'Incoming lower connector remains dash/arrow uncertain; added uncertainty only.',
38:'0 is present below pi_2(xi) in both diagram encodings; no content omission.',
39:'P12v4: lower fibre identification retained vertically; pi_{U/K} is present in both witnesses.',
40:'P12v5: lower E_U identification retained vertically; same source object in both.',
41:'Diagram organization only: downward annotation row versus underset.',
42:'M0208: central lower connector retains the dash/arrow uncertainty; source head not securely readable.',
43:'M0208: same unresolved dash/arrow place.',
44:'TikZ description/label syntax only at the same unresolved relation.',
45:'M0209: subscript remains uncertain as K|U; no source correction counted for adding the alternative.',
46:'P12v6: final lower vertical relation retains both members; different macro arrangement in H.',
47:'Same four lower identification objects, different serialization order.',
48:'Same prose dash, macro/Unicode spelling only.',
49:'M0210: final injectivity-formula connector remains dash/arrow uncertain.',
50:'M0211: final boundary-map connector remains dash/arrow uncertain.',
51:'P15: actual handwritten foliation 133 retained.'}
review=[
 dict(text=r'\inserted{$L$-}',scope_attachment='Prefix before plongement, following un.',evidence='P16: L and short hyphen above the word; curved leader descends at the p.'),
 dict(text=r"\inserted{début de la suite d'homotopie du}",scope_attachment='Added between le and fibré.',evidence='P01: long leader begins in that gap and extends beneath the full added phrase.'),
 dict(text='sur after disques',scope_attachment='No separate deletion accepted; the heavy strokes belong to the s of the live sur.',evidence='P02: the dark loop joins immediately to u/r and is not crossed by an independent cancelling line.'),
 dict(text=r'\unsure{un|\deleted{les}}',scope_attachment='One unresolved word immediately before zéro; possible cancellation is included in the doubt rather than assumed.',evidence='P04: tall initial loop and dense low retracing; blind rereading requested through audit B06.'),
 dict(text=r'\deleted{\unsure{\pi|\mathcal E}}',scope_attachment='Only the single incomplete symbol after du is cancelled.',evidence='P06: compact overlapping bars/loops; no adjacent prose word is crossed.'),
 dict(text=r'\deleted{elle}\inserted{\deleted{devrait}}',scope_attachment='Elle on the baseline is deleted; the added devrait above it, linked by a curved leader, is also deleted.',evidence='P08: two separate horizontal cancellation strokes at the two text levels.'),
 dict(text=r'\deleted{devrait avoir}\inserted{a}',scope_attachment='The later two-word predicate is cancelled and replaced by a above it.',evidence='P09: one cancellation crosses the full devrait avoir; the small rounded a stands above its middle.'),
 dict(text=r'\deleted{induit par}',scope_attachment='Two-word abandoned modifier before commutatif; commutatif itself is live on the following line.',evidence='P09: strike spans only induit par, ending before the line of commutatif.'),
 dict(text=r'\deleted{relative}\inserted{de celle relative}',scope_attachment='One original relative is replaced by the added three-word phrase above it.',evidence='P11: lower relative has a horizontal crossing; upper phrase is uncrossed and directly aligned with it.'),
 dict(text=r'\deleted{ligne}\inserted{colonne}',scope_attachment='Colonne replaces ligne after première; the following comma remains live.',evidence='P11: lower g descender survives the strike; the upper short word is colonne.'),
 dict(text=r'\inserted{le composé}',scope_attachment='Added after qui montre que and before the composite pi_2(D_J) to T^J to pi_{U/K}.',evidence='P13: leader curves beneath le composé and terminates in the gap before the formula; it does not cancel que.')]
report=dict(page=page,reader='reader_c',line_count=26,changes=changes,decisions=decisions,inventory=inventory,audit_boxes=audit,doubts=doubts,notes=notes,check_events=checks,notation=notation,abbreviations=abbreviations,hand=hand,diff_coverage=[dict(row=i,disposition=coverage[i]) for i in range(1,52)],deletion_insertion_review=review)
out=Path('work/reports')/page/'report.json'
quote_fixes={'P07': {'h': '\\note{sous « $\\pi_1(\\text{fibre})$ » est écrit « $= T^J$ ».}'}, 'P08a': {'h': "« l'injection »"}, 'P08c': {'c': '\\deleted{elle}\\inserted{\\deleted{devrait}} heuristiquement on \\deleted{devrait avoir}\\inserted{a}', 'h': '\\struck{\\uncertain{elle}} heuristiquement on \\struck{devrait avoir} \\add{\\uncertain{devrait}}', 'final': '\\deleted{elle}\\inserted{\\deleted{devrait}} heuristiquement on \\deleted{devrait avoir}\\inserted{a}'}, 'P10c': {'c': 'D_J \\arrow[u,"\\text{équiv. d\'homotopie}"]', 'h': 'D_J \\arrow[u, "\\text{équiv.\\ d\'homotopie}"\']', 'final': 'D_J \\arrow[u,"{\\substack{\\text{équiv}\\\\\\text{d\'homotopie}}}"\']'}, 'P12v1': {'h': '\\pi_1(\\overline{\\mathbb{G}}_m^{\\,J}) \\arrow[u, no head, "\\wr"\']'}, 'P12v2': {'h': '\\pi_1(U_J) \\arrow[u, no head, "\\wr"\']'}, 'P12v3': {'h': '\\pi_1(X_J) \\arrow[u, no head, "\\wr"\']'}, 'P12v4': {'h': '\\pi_1(U_{\\overline{\\xi}}) \\arrow[r] \\arrow[d, no head, "\\wr"\']'}, 'P12v5': {'h': '\\pi_1(U) \\arrow[r] \\arrow[d, no head, "\\wr"\']'}, 'P12v6': {'c': '\\underset{\\substack{\\wr\\\\\\mathcal E_{\\unsure{K}}}}{\\pi_1(\\xi)}', 'h': '\\pi_1(\\xi) \\arrow[r] \\arrow[d, no head, "\\wr"\']'}}
for item in report['changes']:
 if item['id'] in quote_fixes: item.update(quote_fixes[item['id']])
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'report':str(out),'changes':len(changes),'marks':len(decisions),'audit_boxes':len(audit),'crops':len(boxes),'diff_rows':len(coverage),'doubts':len(doubts)},ensure_ascii=False))
