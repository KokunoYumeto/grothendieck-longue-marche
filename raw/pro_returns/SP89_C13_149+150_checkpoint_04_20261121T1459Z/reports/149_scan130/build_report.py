from pathlib import Path
import json
root=Path('/workspace/scratch/8759b8008681')
out=root/'work/reports/149_scan130'
boxes=json.loads((out/'crop_boxes.json').read_text())
draft=r'''\scanpage{130}
se ramène à celle des hom composants.

À ce sujet, sous réserve de vérifications, je présume

$1^\circ)$ que l'hom $\mathcal E_{\tilde U_x}^{\bar L}\longrightarrow\mathcal E_U^{\bar L}$ est \uline{injectif}

--- ou ce qui revient au $=$, que sa partie géométrique
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\mathcal E_{\tilde U_x/K}^{\bar L}\arrow[r]\arrow[d,equal] & \pi_{U/K}^{\bar L}\\
I_x\simeq T^{(I(x))} &
\end{tikzcd}}
\margin{les deux lettres $I$ ne sont pas les mêmes}
est \uline{injective}.

\margin{C'est visiblement \uline{faux} \inserted{\uline{``en général''}} pour $\operatorname{card}I(x)\ne1$ comme on voit en \unsure{passant} à un autre modèle $X'$ déduit de $X$ en y faisant éclater un pt de $D$\ldots\ Mais y a-t-il un modèle ``minimal'' $X\supset U$, et pour un tel modèle \unsure{a-t-on} l'injectivité ???}

$2^\circ)$ que \deleted{l'hom} lorsque le corps résiduel de $V$ est alg $/K$ (i.e. $V$ correspondant à un pt de $\mathfrak X_{L/K}$ de dim zéro), alors l'hom
\[
 \mathcal E_{\tilde\eta}^{\bar L}=N_V\longrightarrow\mathcal E_{\tilde U_x}^{\bar L}
\]
\deleted{est injectif} \inserted{\unsure{a} une image} \deleted{surjectif} \inserted{ouverte} --- ce qui revient ici (puisque $k(V)$ \deleted{alg} \inserted{fini} sur $k(x)$ donc $\mathcal E_{k(V)}=N_V/I_V\hookrightarrow\mathcal E_{k(x)}$ \inserted{(sous-groupe ouv.)} $\simeq N_x/I_x$), que la partie géométrique
\[
 I_V\longrightarrow I_x=T^{I(x)}
\]
\deleted{est injective} \deleted{\inserted{\unsure{surjective}}} \inserted{a une image ouverte} \deleted{--- \unsure{je pense que} \illegible{3} \unsure{à un sous-groupe ouvert}.} \inserted{--- sans doute est-elle $=$ surjective.}

À noter que \unsure{la} question $2^\circ$ est purement
\margin{129}
'''
(out/'draft.tex').write_text(draft)
report={"page":"149_scan130","reader":"reader_a","line_count":20,"changes":[],"decisions":[],"inventory":[],"audit_boxes":[],"doubts":[],"notes":[],"check_events":[],"notation":[],"abbreviations":[],"hand":[],"diff_coverage":[],"deletion_insertion_review":[]}
def change(id,place,c,h,final,evidence,crop,confidence='high',kind='misread word',against_c=False,against_h=True,marked_in_h=False,consequential=False,error_category=2):
 report['changes'].append(dict(id=id,place=place,c=c,h=h,final=final,evidence=evidence,crop=f'crops/149_scan130_{crop}.png',box=boxes[crop],confidence=confidence,kind=kind,against_c=against_c,against_h=against_h,marked_in_h=marked_in_h,consequential=consequential,error_category=error_category))
change('P01','L5, au =',r'au $=$',r'au \uncertain{même}',r'au $=$','Two separate short horizontal strokes stand between au and the comma; no letters m/e follow au. This is the written lexical abbreviation, not an expansion.','P01',kind='abbreviation expanded or spelling modernised',marked_in_h=True,error_category=8)
change('P02','L5, sa partie','sa partie',r'\uncertain{son} partie','sa partie','After the initial s-like curve there is a compressed low a and terminal return; no separate final n arch follows it before the long p descender of partie.','P01',marked_in_h=True)
change('P03','Right marginal note, opening',r'C\textquotesingle est visiblement \uline{faux}',r"C'est \uncertain{sûrement} « \uncertain{en général} » \emph{faux}",r"C'est visiblement \uline{faux}",'The word after C\'est begins v with a dot over the following i; two tall stems belong to b and l, followed by a compressed -ement ending. The separate faux has a large looped f and terminal crossed x and an underline.','P03',marked_in_h=True,consequential=True)
# Use exact source text rather than an editorial apostrophe macro in the C field.
report['changes'][-1]['c']=r"C'est visiblement \uline{faux}"
change('P04','Right marginal note, interlinear en général',r'\inserted{\uline{« en général »}} pour $\operatorname{card}I(x)\ne1$',r'« \uncertain{en général} » \emph{faux} \add{pour $\operatorname{card} I(x) \neq 1$}',r"\inserted{\uline{``en général''}} pour $\operatorname{card}I(x)\ne1$",'The small phrase is on an interlinear baseline between visiblement and the faux/pour line, with an underline ending above pour. Its opening and closing quotation marks are paired short ticks, not double angle chevrons. The added phrase attaches after faux; pour card I(x) is on the regular marginal-note baseline.','P03',kind='insertion or placement',against_c=True,marked_in_h=True,error_category=6)
change('P05','Right marginal note, comme on voit en ... modèle',r'comme on voit en \unsure{passant} à un autre modèle',r'comme on voit en \uncertain{remplaçant} $X$ par un autre',r'comme on voit en \unsure{passant} à un autre modèle','After en the first visible stroke has a long p descender rather than the short initial r of remplaçant; the remaining minims are compressed, so passant stays doubtful. The next small accented loop is à, followed directly by un autre; there is no separate X par there. modèle has a round o, looped d and high l. The saved view is deskewed 45 degrees clockwise from the recorded original box.','P04',confidence='medium',marked_in_h=True)
change('P06','Right marginal note, X\' déduit de X en',r"$X'$ déduit de $X$ en",r"$X'$ dominant $X$, \uncertain{en éclatant}",r"$X'$ déduit de $X$ en",'Immediately after X\' are a looped d, accented é, a second looped d, low ui and the terminal t; a separate de follows before X. The gap following X contains the start of en without an independent comma.','P04',marked_in_h=True)
change('P07','Right marginal note, en y faisant éclater',r'en y faisant éclater',r'\uncertain{en éclatant} des \ill{} \uncertain{faisant}',r'en y faisant éclater','A short y descends before the large looped f of faisant; the next word starts with an accented é and then a tall l, with the t crossing near its end. These strokes give the order y faisant éclater. No separate des lies between en and faisant.','P04',marked_in_h=True)
change('P08','Right marginal note, un pt de D',r'un pt de $D$',r'un p\supplied{oin}t de $D$',r'un pt de $D$','The abbreviation has a p descender followed directly by a crossed t. There is no o, i or n between those two letters. The final D has a straight left stem and curved right bowl.','P04',kind='abbreviation expanded or spelling modernised',error_category=8)
change('P09','Right marginal note, question about minimal model',r'Mais y a-t-il un modèle « minimal » $X\supset U$',r'\textbf{Mais} \uncertain{est-il vrai} \uncertain{qu\textquotesingle on} \ill{} $X\supset U$',r"Mais y a-t-il un modèle ``minimal'' $X\supset U$",'After Mais a descending y and the short a-t-il sequence precede un. modèle has the same looped d and high l seen above. The following word has the low repeated minims of minimal and a high terminal l, bounded by pairs of quote ticks. X, the open superset sign and U stand on the next marginal baseline.','P05',against_c=True,marked_in_h=True,consequential=True)
report['changes'][-1]['h']=r"\textbf{Mais} \uncertain{est-il vrai} \uncertain{qu'on} \ill{} $X\supset U$"
change('P10','Right marginal note, end of question',r'et pour un tel modèle \unsure{a-t-on} l\textquotesingle injectivité ???',r'\uncertain{tel que} \ill{} \uncertain{localement} \emph{injectif}…',r"et pour un tel modèle \unsure{a-t-on} l'injectivité ???",'The note contains a separate et with a crossed t, then pour with a p descender, un and tel modèle. The short following group is compressed at the edge and a-t-on remains doubtful. In the final word the j descends, the -tivité ending continues beyond the f-shaped middle stroke, and terminal question hooks/dots replace an ellipsis.','P05',confidence='medium',marked_in_h=True,consequential=True)
report['changes'][-1]['c']=r"et pour un tel modèle \unsure{a-t-on} l'injectivité ???"
change('P11','L10, résiduel de V','résiduel de $V$',r'\uncertain{résiduel} \ill{} $V$','résiduel de $V$','After the long final l of résiduel the pale horizontal main-text baseline continues through a small looped d and low e before the next-line V. The darker diagonal strokes belong to the later marginal note.','P06',marked_in_h=True)
change('P12','L11, V correspondant',r'$V$ correspondant',r'$V$ correspond',r'$V$ correspondant','The word has a long medial p loop below the baseline; after the portion correspond the line continues through low a/n strokes to a distinct raised terminal t. It does not end at the d.','P07')
change('P13','L11, à un pt',r'à \unsure{un pt}',r'\uncertain{à un point}',r'à un pt','On the horizontal pale baseline, un has two low connected humps; the following abbreviation has a descending p and a separate tall crossed t. No intervening oint is written. This resolves C\'s certainty mark and rejects H\'s expansion.','P08',kind='abbreviation expanded or spelling modernised',against_c=True,marked_in_h=True,error_category=8)
change('P14','L12, parameter-space symbol',r'$\unsure{\mathfrak X_{L/K}|\mathcal Z_{L/K}}$',r'$\mathfrak{X}_{L/K}$',r'$\mathfrak X_{L/K}$','The main glyph has two upper arms meeting two lower curved arms at a central crossing, with a short transverse bar. It is X-shaped, with no Z-like top-to-bottom diagonal. The subscript is L / K. The whole short formula was read on the crop; this resolves C\'s alternative.','P09',kind='misread symbol or index',against_c=True,against_h=False,consequential=True,error_category=1)
change('P15','L13, first cancelled predicate',r'\deleted{est injectif}',r'\struck{est égal}',r'\deleted{est injectif}','Below the replacement the cancelled word includes a long j descender, then e/c, a tall crossed t, a dotted i and tall final f. This is the longer injectif, not égal; the single cancellation stroke crosses est and the whole predicate.','P10',kind='misread word',consequential=True)
change('P16','L14, revient ici','revient ici',r'revient à dire','revient ici','After revient the ink is a compact group with a short initial i, low c and final dotted i. There is no separate accented à or tall d/l required by à dire.','P11')
change('P17','L18, stacked cancelled and replacement predicates',r'\deleted{est injective} \deleted{\unsure{surjective}} \inserted{a une image ouverte}',r'\struck{soit \uncertain{à image} \ill{} \uncertain{ouverte}}',r'\deleted{est injective} \deleted{\inserted{\unsure{surjective}}} \inserted{a une image ouverte}','The lowest pale baseline has est and a long j descender in injective crossed by a horizontal cancellation. Above it surjective is a separate interlinear correction, also crossed; overlapping strokes prevent full certainty in that word. Between/alongside these layers a une image ouverte is not crossed. The draft records the cancelled insertion state of surjective explicitly.','P15',confidence='medium',kind='deletion state (struck given live or live given struck)',against_c=True,marked_in_h=True,consequential=True,error_category=7)
change('P18','L18, cancelled explanation, first part',r'\unsure{je pense que} \illegible{3}',r'\uncertain{ou plus} \ill{}',r'\unsure{je pense que} \illegible{3}','Under the long strike the initial letter has a j descender, and the next word begins with a p descender followed by visible e/n-like humps. Those strokes support C\'s tentative je pense que rather than ou plus, but the strike hides too much to remove the uncertainty or recover the three unreadable words.','P16',confidence='low',marked_in_h=True)
change('P19','L19, cancelled explanation, second part',r'\unsure{à un sous-groupe ouvert}.',r'\ill{} \uncertain{sous-groupe ouvert}.',r'\unsure{à un sous-groupe ouvert}.','The long cancelling line crosses pale sous-groupe ouvert; the g and p descenders and the final t extend below/above it. At the left, the initial small marks and low un are too compressed to settle the entire phrase, so C\'s full doubt is retained, not silently resolved.','P17',confidence='low',kind='readable ink left as \\ill{}',marked_in_h=True,error_category=5)
change('P20','L18–19, later dark-ink conclusion',r'\inserted{--- sans doute est-elle $=$ surjective.}',r'\add{\uncertain{soit}} surjective.',r'\inserted{--- sans doute est-elle $=$ surjective.}','Above the cancelled pencil sentence the darker ink reads sans (initial two-lobed s), doute (looped d and crossed t), est-elle (two high l stems) and two horizontal equals strokes. The continuation surjective. is dark and live on the following baseline, also visible in crop P17. The black horizontal line below the first part cancels the older pencil sentence, not the new dark words.','P16',kind='omission',marked_in_h=True,consequential=True,error_category=3)
change('P21','Lower-left foliation',r'\margin{129}','(nothing)',r'\margin{129}','Three thin sloping digits stand at the bottom left: 1 with a long entry stroke, 2 with a curved top and baseline return, 9 with a closed loop and descending tail. This small foliation has a different ductus from the main writing and is retained as a marginal number.','P20',kind='omission',error_category=3)
change('P22','Right marginal note, after card I(x) ≠ 1',r'$\operatorname{card}I(x)\ne1$,',r'$\operatorname{card} I(x) \neq 1$',r'$\operatorname{card}I(x)\ne1$','The terminal 1 is close to the page edge. No separate comma stroke can be distinguished after it; the next phrase begins on the following marginal baseline. I omit C\'s comma rather than supply a punctuation mark whose ink is not visible.','P03',confidence='medium',kind='text not on the page',against_c=True,against_h=False,error_category=9)
for id,decision,reading,evidence,crop,confidence in [
 ('M0167','undecided',r'\unsure{passant}','The p descender is visible, but the following minims remain too compressed to identify every letter securely; retain C\'s doubt.','P04','medium'),
 ('M0168','undecided',r'\unsure{a-t-on}','The small phrase after modèle contains the a/t-like strokes but its final group is compressed at the edge; retain the doubt.','P05','medium'),
 ('M0169','first','un pt','The horizontal pale text has two low humps for un and the adjacent p-descender/t-cross pair; no expanded point is written.','P08','high'),
 ('M0170','first',r'\mathfrak X_{L/K}','Four curved arms cross centrally; the glyph is X-shaped, not Z-shaped. The entire L/K subscript is visible.','P09','high'),
 ('M0171','undecided',r'\unsure{la}','A single open high loop and its short return can represent compressed la, but the two letters cannot be separated securely from this crop.','P18','medium')]:
 report['decisions'].append(dict(id=id,cote='149',scan='130',decision=decision,reading=reading,evidence=evidence,crop=f'crops/149_scan130_{crop}.png',box=boxes[crop],confidence=confidence))
def inv(element,kind,position,words,hand='his hand'):
 report['inventory'].append(dict(scan='149_scan130',sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inv('E01','text','top; 350,70–1650,400','se ramène à celle des hom composants. À ce sujet...')
inv('E02','text','upper main column; 345,399–1605,790',r"1°) que l'hom ... injectif — ou ce qui revient au =")
inv('E03','diagram','upper middle; 560,766–1100,1023',r'\mathcal E_{\tilde U_x/K}^{\bar L} → \pi_{U/K}^{\bar L}; vertical equality to I_x≃T^{(I(x))}')
inv('E04','margin note','left margin; 50,896–452,1147','les deux lettres I ne sont pas les mêmes')
inv('E05','margin note','right, oblique; 1168,630–1672,1450',"C'est visiblement faux ... Mais y a-t-il un modèle ...")
inv('E06','insertion','within right note; interlinear above faux/pour','``en général\'\' (underlined)')
inv('E07','text','middle; 320,1130–1667,1595',"2°) que ... lorsque le corps résiduel de V ... alors l'hom")
inv('E08','deletion','main text after 2°); 584,1155–794,1230',"l'hom")
inv('E09','display','middle; 743,1433–1215,1593',r'\mathcal E_{\tilde\eta}^{\bar L}=N_V→\mathcal E_{\tilde U_x}^{\bar L}')
inv('E10','deletion','middle right; 1248,1465–1607,1551','est injectif')
inv('E11','insertion','above preceding deletion; 1248,1421–1607,1477','a une image (a left uncertain)')
inv('E12','deletion','left continuation; 307,1637–588,1752','surjectif')
inv('E13','insertion','above surjectif; 307,1597–588,1652','ouverte')
inv('E14','text','lower middle; 321,1578–1666,1912','— ce qui revient ici (puisque k(V) ...), que la partie géométrique')
inv('E15','deletion','within k(V) phrase; 478,1751–584,1812','alg')
inv('E16','insertion','above alg; 551,1710–644,1774','fini')
inv('E17','insertion','below residue-field map; 1253,1722–1666,1822','(sous-groupe ouv.)')
inv('E18','display','lower middle; 574,1902–1208,2044',r'I_V→I_x=T^{I(x)}')
inv('E19','deletion','below display, stacked; 306,2011–843,2144','est injective; cancelled interlinear surjective')
inv('E20','insertion','among preceding cancelled alternatives; 306,2011–843,2144','a une image ouverte')
inv('E21','deletion','two lines at bottom; 309,2032–1650,2249','— je pense que [unreadable] à un sous-groupe ouvert.')
inv('E22','insertion','dark ink above cancelled sentence; 330,1977–1650,2204','— sans doute est-elle = surjective.')
inv('E23','text','bottom main line; 500,2197–1672,2321','À noter que la question 2° est purement')
inv('E24','margin note','lower-left corner; 20,2299–102,2344','129','thin sloping foliation, hand not confidently identified')
def audit(id,kind,xyxy,reading): report['audit_boxes'].append(dict(box=id,kind=kind,xyxy=xyxy,reading=reading))
audit('B01','handwritten number',[350,466,435,535],r'$1^\circ)$')
audit('B02','C/H different words',boxes['P01'],r'au $=$, que sa partie')
audit('B03','margin note',boxes['P02'],r'les deux lettres $I$ ne sont pas les mêmes')
audit('B04','margin note (oblique writing); insertion; handwritten number; C/H different words; less than high confidence departure',[1168,625,1677,1455],r"C'est visiblement \uline{faux} \inserted{\uline{``en général''}} pour $\operatorname{card}I(x)\ne1$ comme on voit en \unsure{passant} à un autre modèle $X'$ déduit de $X$ en y faisant éclater un pt de $D$\ldots\ Mais y a-t-il un modèle ``minimal'' $X\supset U$, et pour un tel modèle \unsure{a-t-on} l'injectivité ???")
audit('B05','handwritten number; struck passage',[315,1155,801,1273],r"$2^\circ)$ que \deleted{l'hom}")
audit('B06','C/H different words (horizontal pale writing)',boxes['P06'],'le corps résiduel de')
audit('B07','C/H different words',boxes['P07'],r'$V$ correspondant')
audit('B08','C/H different words (horizontal pale writing)',boxes['P08'],'à un pt')
audit('B09','doubtful formula',boxes['P09'],r'de $\mathfrak X_{L/K}$')
audit('B10','struck passage; insertion; C/H different words',boxes['P10'],r'\deleted{est injectif} \inserted{\unsure{a} une image}')
audit('B11','struck passage; insertion',boxes['P12'],r'\deleted{surjectif} \inserted{ouverte}')
audit('B12','C/H different words',boxes['P11'],'qui revient ici (puisque')
audit('B13','struck passage; insertion',boxes['P13'],r'\deleted{alg} \inserted{fini}')
audit('B14','insertion',boxes['P14'],r'\inserted{(sous-groupe ouv.)}')
audit('B15','struck passage; insertion; C/H different words; less than high confidence departure',boxes['P15'],r'\deleted{est injective} \deleted{\inserted{\unsure{surjective}}} \inserted{a une image ouverte}')
audit('B16','struck passage; insertion; C/H different words',boxes['P16'],r'\deleted{--- \unsure{je pense que} \illegible{3}} \inserted{--- sans doute est-elle $=$}')
audit('B17','struck passage; insertion; C/H different words',boxes['P17'],r'\inserted{surjective.} \deleted{\unsure{à un sous-groupe ouvert}.}')
audit('B18','handwritten number; less than high confidence departure',[788,2197,1672,2321],r'que \unsure{la} question $2^\circ$ est purement')
audit('B19','handwritten number',boxes['P20'],'129')
report['doubts']=[
 dict(place='Right marginal note, after en',reading=r'\unsure{passant}',alternatives='passant; exact internal minims not secure',confidence='medium',reason='Initial p is visible, but the body is compressed on the rising marginal baseline; M0167 remains undecided.'),
 dict(place='Right marginal note, after un tel modèle',reading=r'\unsure{a-t-on}',alternatives='a-t-on; small final group unclear',confidence='medium',reason='The short edge group cannot be separated confidently; M0168 remains undecided.'),
 dict(place='L13, insertion above est injectif',reading=r'\inserted{\unsure{a} une image}',alternatives='a une image; une image with an unseparated or absent initial a',confidence='medium',reason='The crop clearly shows une image; I cannot independently separate the initial a assumed by both witnesses. Added uncertainty only; parent should review this precise point.'),
 dict(place='L18, cancelled interlinear predicate',reading=r'\deleted{\inserted{\unsure{surjective}}}',alternatives='surjective; overlapped letters remain uncertain',confidence='medium',reason='The upper word is crossed and overlaps the live a une image insertion; not every letter can be distinguished.'),
 dict(place='L18–19, cancelled explanation',reading=r'\deleted{--- \unsure{je pense que} \illegible{3} \unsure{à un sous-groupe ouvert}.}',alternatives='Initial small mark of second line might be a compressed à or a two-stroke sign; no conjectural supplement adopted',confidence='low',reason='Two long cancellation strokes obscure the sentence. The recognizable p/g descenders do not justify removing the existing doubt marks or recovering the unreadable interval.'),
 dict(place='Bottom main line, before question',reading=r'\unsure{la}',alternatives='la; open loop not separable into two letters',confidence='medium',reason='The glyph resembles a single large open C-shaped loop; M0171 remains undecided.'),
 dict(place='Right note, punctuation after inequality',reading=r'$\operatorname{card}I(x)\ne1$',alternatives='No comma accepted; C supplies a comma',confidence='medium',reason='The terminal digit is close to the physical edge and no comma can be identified independently.')]
report['notes']=[
 dict(id='N01',text='English: This continuation first proposes injectivity of the local-to-global homomorphism and its geometric part. The later oblique note explicitly qualifies the proposal: “C\'est visiblement faux” and the inserted “en général”, with card I(x) ≠ 1 and a change of model by blowing up a point of D. It then asks whether a “minimal” model has injectivity. These are source assertions and questions; I have not independently verified a theorem or counterexample.'),
 dict(id='N02',text='English: Item 2 assumes the residue field of V is algebraic over K, with V corresponding to a zero-dimensional point of the written parameter space. The predicate is revised from injectivity/surjectivity to having open image, and the geometric map I_V → I_x = T^{I(x)} is treated similarly. The later dark conclusion says “sans doute est-elle = surjective.” The lexical = is retained. The claim remains conjectural in the source; no proof check was performed.'),
 dict(id='N03',text='English: The left marginal note explicitly warns that the two letters I are not the same. The diagram keeps the vertical pair of equality strokes under its left object; this is not a downward arrow. No drawings distinct from this diagram occur on the page.'),
 dict(id='N04',text='English: The small 129 at the lower left is separate foliation, retained as a margin note rather than asserted to be the author\'s own pagination. The line_count of 20 counts the principal text/display baselines, excluding marginal and interlinear additions. All agreed words were read on the supplied halves. Crops P04 and P05 are clockwise-deskewed views of their recorded original-image boxes; P08 was retargeted before a reading was decided. No OCR, external research or TeX compilation was used.')]
report['notation']=[
 dict(form='$=$ in prose',meaning='written abbreviation for même',evidence='au = before sa partie; est-elle = before surjective, crops P01 and P16'),
 dict(form=r'I_x and I(x)',meaning='different uses of the letter I, as explicitly warned in the left marginal note; no unstated definition supplied',evidence='Diagram plus “les deux lettres I ne sont pas les mêmes”, crop P02 and upper half'),
 dict(form=r'\mathfrak X_{L/K}',meaning='written parameter-space symbol; point of dimension zero mentioned, exact definition not supplied on this page',evidence='Four-armed X-shaped glyph and subscript L/K, crop P09'),
 dict(form=r'\parallel beneath \mathcal E_{\tilde U_x/K}^{\bar L}',meaning='vertical equality/identification with I_x ≃ T^{(I(x))}',evidence='Upper-half diagram shows two short upright strokes; neither has an arrowhead.')]
report['abbreviations']=[dict(form='hom',expansion='homomorphisme(s)'),dict(form='alg',expansion='algébrique'),dict(form='i.e.',expansion='id est'),dict(form='pt',expansion='point'),dict(form='dim',expansion='dimension'),dict(form='ouv.',expansion='ouvert'),dict(form='=',expansion='même, in the two prose contexts')]
report['hand']=[
 dict(habit='Many word interiors collapse to long low linking strokes; ascenders, descenders and dots carry more information than apparent letter count.',places='149_scan130: correspondant, visiblement, marginal passant',consistency='Observed throughout this page; not asserted for another page.',witness_errors='H reads correspond without the written final -ant; H surely/sûrement and remplaçant do not fit the distinctive stems as well as the retained readings.'),
 dict(habit='The local X-shaped parameter-space glyph has four curved arms and an extra central transverse stroke.',places='149_scan130 L12, crop P09',consistency='One occurrence on the assigned page.',witness_errors='C offered a Z alternative; resolved to the X-shaped reading also used by H.'),
 dict(habit='An open high l-loop with a compressed following vowel can resemble a large C.',places='149_scan130 footer la, crop P18',consistency='This particular occurrence remains uncertain; no blanket correction rule inferred.',witness_errors='C marks la doubtful, H gives it without a doubt mark.'),
 dict(habit='The lexical equals sign is two strokes with no alphabetic expansion.',places='149_scan130 L5 and later dark conclusion, crops P01 and P16',consistency='Both occurrences have the same two-stroke form.',witness_errors='H expands the first as même and loses the later phrase.'),
 dict(habit='Later corrections are darker and the slanted right note overlaps earlier pale main-text baselines.',places='149_scan130 right margin and lower cancelled conclusion',consistency='Layering is consistently visible in the recorded crops.',witness_errors='Several H misreadings conflate marginal or replacement material with the earlier text; no ink layer is omitted in the draft.')]
dispositions={
1:'macro-only: scan-page editorial marker, not source ink',2:'macro-only: same handwritten 1°)',3:'macro-only: C --- and H em dash represent the same dash',4:'P01',5:'P02',6:'macro/layout-only: same diagram objects and right arrow; vertical equality preserved',7:'macro/layout-only: same diagram formula',8:'placement-only in witness extraction: est injective follows the diagram',9:'same as row 8; est injective retained once',10:'P03 and P04',11:'P03/P04; faux belongs before the interlinear qualification',12:'P22',13:'P05; C doubt retained',14:'P05; modèle is written',15:'P06',16:'P06; no comma after X',17:'P07',18:'P07',19:'P08; source abbreviation pt retained',20:'macro-only: C \\ldots and H literal ellipsis represent the same three points',21:'P09',22:'P09',23:'P09/P10 for handwritten note; H editorial note is excluded, not source text',24:'P10 for handwritten note; H editorial note is excluded',25:'macro-only: same handwritten 2°)',26:'P11',27:'P12',28:'P13 / M0169',29:'P14 / M0170; full formula retained',30:'P15',31:'macro-only: same dash',32:'P16',33:'P17',34:'P18; cancelled explanation remains doubtful',35:'P18/P19/P20; distinguish cancellation from later insertion',36:'P20; H editorial note is not source text',37:'P20; H editorial note is not source text',38:'macro-only: same handwritten 2° in footer',39:'P21'}
for row in range(1,40): report['diff_coverage'].append(dict(row=row,disposition=dispositions[row]))
report['deletion_insertion_review']=[
 dict(text=r"\inserted{\uline{``en général''}}",scope_attachment='Interlinear qualification attaches after faux and before pour in the right note; pour card I(x) is not itself the added interlinear phrase.',evidence='P03, plus deskewed P04: small text above the faux/pour baseline and a separate underline.'),
 dict(text=r"\deleted{l'hom}",scope_attachment='Only l\'hom is cancelled after que in item 2; lorsque remains live.',evidence='P19: one horizontal stroke crosses the apostrophe group, tall h and final m; it ends before lorsque.'),
 dict(text=r'\deleted{est injectif} \inserted{\unsure{a} une image}',scope_attachment='The full predicate est injectif is struck; une image is above it. The initial a of the replacement remains doubtful.',evidence='P10: long j/f strokes belong to injectif below the cancellation; une image occupies the higher baseline.'),
 dict(text=r'\deleted{surjectif} \inserted{ouverte}',scope_attachment='surjectif at the start of the next main line is struck; ouverte above it supplies the ending of a une image.',evidence='P12: horizontal strike crosses surjectif, while ouverte is on a distinct untouched upper baseline.'),
 dict(text=r'\deleted{alg} \inserted{fini}',scope_attachment='Only alg is struck within the k(V) phrase; fini is inserted directly above it.',evidence='P13: alg has a clear strike, including its g descender; fini has a long f stem and two dotted i forms above.'),
 dict(text=r'\inserted{(sous-groupe ouv.)}',scope_attachment='Added below the residue-field inclusion, before the following ≃ N_x/I_x continuation.',evidence='P14 and lower half: parenthetical text lies directly under the quotient/inclusion formula; the long curved stroke is an attachment/enclosure, not a cancellation of the phrase.'),
 dict(text=r'\deleted{est injective} \deleted{\inserted{\unsure{surjective}}} \inserted{a une image ouverte}',scope_attachment='The original est injective and upper interlinear surjective are both cancelled; a une image ouverte is the live intervening replacement.',evidence='P15: two separate cancellation lines intersect the original and raised alternatives; the live replacement lacks such a stroke.'),
 dict(text=r'\deleted{--- \unsure{je pense que} \illegible{3} \unsure{à un sous-groupe ouvert}.}',scope_attachment='A cancelled pale sentence extends over two baselines, after the revised geometric predicate.',evidence='P16 and P17: long dark lines traverse the earlier pale sentence; surviving descenders belong to its words and are not diagrams.'),
 dict(text=r'\inserted{--- sans doute est-elle $=$ surjective.}',scope_attachment='The later dark words are live above the cancelled sentence; surjective. continues at the left on the next baseline.',evidence='P16 supplies the dark first segment; P17 supplies the live surjective. above the second cancellation. The strike is on the pale text below, not on the dark inserted sentence.')]
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('draft.tex and report.json saved')
print('changes',len(report['changes']),'marks',len(report['decisions']),'audit_boxes',len(report['audit_boxes']),'crops',len(boxes))
