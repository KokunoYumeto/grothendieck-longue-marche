from pathlib import Path
import json,re
base=Path('out/readers/C123-02_123_scan040/R2')
C=Path('packets/C123-02_123_scan040/C.tex').read_text()
H=Path('packets/C123-02_123_scan040/H.tex').read_text()
R=(base/'reading.tex').read_text()
source='source/SP57_CW_97+123+162-1+162-6_scans/C123-02_123_scan040.jpg'
cp='readers/C123-02_123_scan040/R2/crops/'
boxes={
1:('01_top_deleted',[400,16,890,61]),2:('02_exprime',[620,42,910,99]),3:('03_lims',[1075,46,1436,100]),4:('04_top_initial',[240,14,425,151]),5:('05_closes',[995,239,1258,339]),6:('06_margin',[19,252,287,443]),7:('07_directe_map',[420,313,687,410]),8:('08_contre',[541,628,785,671]),9:('09_nest',[1001,625,1210,672]),10:('10_epi_punct',[278,813,424,891]),11:('11_deleted_clause',[648,830,1193,885]),12:('12_transforme',[1101,1019,1410,1098]),13:('13_presence',[878,1082,1234,1161]),14:('14_section',[272,1125,408,1172]),15:('15_f_map',[1318,1114,1514,1159]),16:('16_U',[274,1193,432,1244]),17:('17_properties',[1248,1153,1590,1234]),18:('18_long_deletion',[550,1258,1649,1310]),19:('19_qui_une',[1129,1463,1300,1591]),20:('20_boxes',[910,1720,1501,1821]),21:('21_quotes',[436,1897,618,1945]),22:('22_final_g',[1458,1968,1664,2025]),23:('23_bottom_line',[80,2021,1652,2097]),24:('24_bottom_article',[983,2070,1189,2116]),25:('25_bottom_end',[109,2093,725,2125])}
def segment(t,a,b):
 i=t.index(a);return t[i:t.index(b,i)]
def tikz(marker):
 start=R.index(marker)
 pattern=re.compile(r'\\(begin|end)\{tikzpicture\}')
 depth=0
 for m in pattern.finditer(R,start):
  depth+=1 if m.group(1)=='begin' else -1
  if depth==0:return R[start:m.end()]
 raise ValueError(marker)
def cropinfo(n=None,bbox=None):
 if n:return cp+boxes[n][0]+'.jpg',boxes[n][1]
 return None,bbox
D=[]
def d(place,c,h,reading,evidence,kind='other',conf='high',cc=False,hc=True,n=None,bbox=None,marked=False):
 crop,box=cropinfo(n,bbox)
 D.append(dict(id=f'R2-D{len(D)+1:02}',place=place,C=c,H=h,reading=reading,evidence=evidence,confidence=conf,kind=kind,marked_in_H=marked,c_changed=cc,h_changed=hc,crop=crop,bbox=box,bbox_source=source))
# H's first block is explicitly an editorial synopsis, not a diplomatic transcription.
hsyn=H[H.index('\\note{Feuillet'):H.index('\\marginal{les')].strip()
d('Own manuscript page number',r'\mspage{\handwritten{23}}',r'\page{39}',r'\mspage{\handwritten{23}}','The upper-right pen number reads 23; H gives its own page reference 39 but does not transcribe the manuscript number. These numbers have different functions.','omission',bbox=[1610,77,1668,133])
d('Opening typescript continuation',segment(C,'sent en termes','\n\\inserted'),hSyn if False else hsyn,segment(R,'sent en termes','\n\n% Slanted'),'Three typed lines begin with the visible fragment sent. H provides only a synopsis of the sheet and no direct transcription of this continuation. The last pen curve is separately reported.','omission',bbox=[274,137,1665,314])
d('Top continuation: fonctorielles','fonctorielles','fonctionnelles','fonctorielles','The crop shows f-o-n-c-t-o-r-i-e-l-l-e-s, including the r after to; H substitutes fonctionnelles.','misread word',n=1)
d('Top continuation: location of the cancelled word',r'fonctorielles \deleted{\illegible{1}} habituelles',r'opérations qui \struck{\ill{}}',r'fonctorielles \deleted{\illegible{1}} habituelles','The dense cancelled word sits between fonctorielles and habituelles on the first handwritten line. There is no corresponding cancelled word between qui and peuvent; H moves its explicit illegibility marker there.','insertion or placement',n=1,marked=True)
d('Top continuation: final correction in s\'expriment',r"s'exprime\deleted{nt}\unsure{r}","s'exprimer",r"s'exprime\deleted{nt}\unsure{r}",'The n/t region is heavily darkened. An r-like replacement is possible but its contour is not secure; the two old ending letters remain represented. H prints an unqualified infinitive and omits that correction state.','other',conf='low',n=2)
d('Top continuation: peuvent and its curved insertion leader',r'\inserted{peuvent}',"peuvent s'exprimer",tikz(r'\begin{tikzpicture}[baseline=(expr.base)]'),'Peuvent is above the line. Its low curved leader sweeps left to the beginning of s\'exprime, and turns up at the right. C marks insertion but omits the actual leader; H linearizes it.','drawing or diagram',cc=True,n=2)
d('Top continuation: raised les',r'les opérations','les opérations',tikz(r'\begin{tikzpicture}[baseline=(op.base)]'),'Les is above and slightly to the left of opérations at the upper edge, rather than on its baseline. The local layout retains that placement without adding a caret.','insertion or placement',cc=True,n=4)
d('Top continuation: first call mark and enclosing line',segment(C,'\\figure{\\begin{tikzpicture}','\n\n\\margin'),r'\note{en tête du feuillet, encadré, relié par un trait à l\'insertion' if False else segment(H,'\\note{en tête','\n\n\\marginal{De plus'),segment(R,'\\inserted{\\handwritten{\\figure','\n\nsent'),'The first call mark has a vertical shaft, a filled small upper loop and a separate open lower loop. C has only a single loop. The left and bottom enclosure, including its low step, is retained in TikZ. H mentions an enclosure editorially but draws none.','drawing or diagram',cc=True,n=4)
d('De plus addition: quote strokes and underline',r'``\uline{commute}\'\'' if False else "``\\uline{commute}''",'« commute »',"``\\uline{commute}''",'The half shows two pen quotation strokes on each side of commute and a separate low underline. H uses guillemets and omits the underline.','other',bbox=[1395,231,1555,264])
d('After inductives: pen curve and adjoining paragraph marks',r'inductives)\handwritten{)}.',r'limites inductives)',segment(R,'inductives\\begin{tikzpicture}','\n\n% Slanted'),'A typed closing parenthesis is followed by a distinct thin bowed pen stroke and the typed stop. The thin stroke joins or closely touches the insertion boundary at its upper end; its status as punctuation is uncertain. Both it and the heavy opposing paragraph marks are drawn, rather than calling the thin stroke a definite second parenthesis.','drawing or diagram',conf='medium',cc=True,n=5)
d('Left marginal instruction: wording and punctuation','à la ligne après : Quant au...','à la ligne, puis : Quant au …','à la ligne après : Quant au...','The rotated crop shows après with a descending p and an accent before final s. No comma follows ligne. A colon follows après and three separate points follow au.','misread word',n=6)
d('Left marginal instruction: physical arrangement',r'\node[align=left,text width=1.8cm,inner sep=3pt] (n) {à la ligne après : Quant au...};','à la ligne, puis : Quant au …',segment(R,'\\margin{\\handwritten{\\begin{tikzpicture}[rotate=12]','\n\\begin{tikzpicture}[baseline=(quant.base)]'),'There are two oblique rows, with après starting farther left than à la ligne. The three-sided enclosure is open at the left. C\'s single reflowing text node loses that arrangement.','insertion or placement',cc=True,n=6)
d('Quant au typescript paragraph: direct text absent from H',segment(C,'Quant au foncteur','\n\\inserted{\\handwritten{Par suite'),hsyn,segment(R,'foncteur image directe','\n\\inserted{\\handwritten{Par suite'),'H quotes the opening label and describes some insertions in an editorial note, but the continuous typescript paragraph, its exact wording, cancellations and qualifications are not directly transcribed. This is an omission of diplomatic text, not a claim that H\'s synopsis is a verbatim faulty quotation. The source includes bare épimorphisme twice, the cancelled e, ces propriétés, the added à and the closing parenthesis.','omission',bbox=[275,277,1667,1095])
d('Inserted : E to E-prime: curved leader',r"\inserted{$:\mathrm{E}\handwritten{\longrightarrow}\mathrm{E}'$}","« $: E \\to E'$ »",tikz(r'\begin{tikzpicture}[baseline=(direct.base)]'),'The source has ordinary single-contour typed E and E-prime, a pen right arrow, and a curved leader entering between u-star and the live baseline comma. C and H omit the curve. The comma remains in its own baseline node.','drawing or diagram',cc=True,n=7)
d('Par suite above toute: leader',r'\inserted{par suite}','« par suite »',tikz(r'\begin{tikzpicture}[baseline=(toute.base)]'),'The half shows the raised typed words and a pen curve that descends immediately before toute. Both the word toute and the leader are inside the corresponding TikZ layout.','drawing or diagram',cc=True,bbox=[1415,310,1624,390])
d('Exclusivement: leader',r'\inserted{exclusivement}','« exclusivement »',tikz(r'\begin{tikzpicture}[baseline=(telles.base)]'),'The raised typed word has a separate pen curve down to the opening parenthesis before telles; neither witness draws that curve.','drawing or diagram',cc=True,bbox=[1092,452,1390,538])
d('Cancelled dans under parmi',r'\deleted{dans}\inserted{parmi}','« parmi » remplace un mot biffé',r'\deleted{dans}\inserted{parmi}','The half shows d-a-n-s under the x cancellation and parmi immediately above it. H acknowledges an unidentified cancelled word editorially but does not transcribe it.','omission',bbox=[1211,541,1318,589])
d('Par contre: mixed f/c impression',r'\deleted{f}contre',hsyn,segment(R,'\\unsure{\\begin{tikzpicture}[baseline=(c.base)]','ontre,')+'ontre,','A tall f hook and stem coexist with an open c bowl. The crop establishes both contours but not which was struck first. C assigns a definite deleted f and final c. The reading preserves the overlap with a chronology doubt. H has no direct quotation at this locus.','other',conf='medium',cc=True,n=8)
d('Mark after second épimorphisme',r'\handwritten{\unsure{;|,}}',hsyn,segment(R,'\\handwritten{\\unsure{\\begin{tikzpicture}[baseline=-.2ex','\nc\'est d\'ailleurs'),'The mark has a dark low loop and tail, an ascending curved shaft and a detached small upper angled stroke. Semicolon or overwritten comma remains possible, but a conventional semicolon does not reproduce all the ink. The uncertain mark is drawn locally, with the following open parenthesis separate.','drawing or diagram',conf='low',cc=True,n=10)
d('Cancelled clause after c\'est d\'ailleurs',r'\deleted{\unsure{comme} nous le verrons au}',hsyn,r'\deleted{\unsure{comme} nous le verrons au}','The crop permits nous le verrons au individually through the x overtyping; comme remains partly covered. H\'s synopsis does not transcribe this deleted clause.','omission',conf='medium',n=11)
d('Cancelled clause: blank-cell x marks and pen stroke',r'\deleted{\unsure{comme} nous le verrons au}',hsyn,segment(R,'\\begin{tikzpicture}[baseline=(del.base)]','\nce défaut'),'One lowered x precedes comme; four more x impressions occupy the interword cells. A pen horizontal crosses the first part and a short ascending trace rises at the first x. C does not retain these marks separately.','drawing or diagram',cc=True,n=11)
d('Par suite addition versus section correction est en présenced\'',r"\inserted{\handwritten{Par suite, il ne \deleted{transforme pas}\inserted{s'étend pas}, en général,",r"\marginal{Par suite, il ne s'étend pas, en général, en présence d'}",segment(R,'\\inserted{\\handwritten{Par suite','\n\n\\deleted{2}'),'The handwritten line ends with en général and a call mark. Est présenced\' is a separate typed interlinear correction below, with en in pen. H incorrectly appends en présence d\' to the handwritten Par suite line.','insertion or placement',n=13)
d('Par suite addition: cancelled transforme and lower pas',r"\deleted{transforme pas}\inserted{s'étend pas}",r"« s'étend pas » au-dessus d'un mot biffé",tikz(r'\begin{tikzpicture}[baseline=(old.base)]'),'Transforme retains a t at the start, an f descender and parts of its other letters beneath dense strokes; its complete reading is tentative. The strong cancellation ends before most of the lower pas, which remains visibly formed. Since its cancellation extent is less certain than C suggests, the lower pas is given with live/deleted alternatives. The upper s\'étend pas is definite.','deletion state (struck given live or live given struck)',conf='medium',cc=True,n=12)
d('Section number correction',r'\deleted{2}\handwritten{3}.1.3.','3.1.3',r'\deleted{2}\handwritten{3}.1.3.','The initial typed 2 is crossed by a rounded pen 3. H has only the final section number in its editorial synopsis, omitting the correction state.','omission',n=14)
d('Section 3.1.3: opening prose and literal U notation',segment(C,'En pratique, lorsqu\'on','y compris l\'existence'),hsyn,segment(R,'En pratique, lorsqu\'on','y compris l\'existence'),'H summarizes this passage instead of quoting it. The crop of f:E to F shows ordinary typed E and F; the next line has a plain typed U with a detached underline, whereas the synopsis uses calligraphic U. That editorial normalization is not treated as a direct quoted glyph reading. The literal opening and its cancellation states are supplied.','omission',bbox=[277,1082,1649,1310])
d('Est en présenced\': attached leader and absence of a space before d\'',r"\deleted{se donne}\inserted{est \inserted{\handwritten{en}} présenced'}un",r"en présence d'",tikz(r'\begin{tikzpicture}[baseline=(un.base)]'),'The typed e of présence is immediately adjacent to d\'. En is above the gap after est. The curved leader descends immediately before the baseline un. C has the letters and missing space correctly, but no leader; H puts an expanded, separated version in the wrong handwritten passage.','drawing or diagram',cc=True,n=13)
d('Cancellation of se donne: x in the former word space',r'\deleted{se donne}',hsyn,r'\deleted{se}\tikz[baseline=(x.base)]{\node[inner sep=0pt] (x) {x};}\deleted{donne}','An x occupies the cell between se and donne, not merely the cells of those words. It is retained as a cancellation mark.','omission',cc=True,n=13)
d('Toutes before les: attached leader',r'\inserted{\handwritten{toutes}}',hsyn,tikz(r'\begin{tikzpicture}[baseline=(les.base)]'),'A pen curve beneath toutes bends down just left of les. C retains only the word, and H does not directly transcribe this addition. The layout anchors the curve to a node actually containing les.','drawing or diagram',cc=True,n=17)
d('Propriétés: two mixed t/é impressions',r'propri\deleted{t}é\deleted{é}tés',hsyn,segment(R,'propri\\unsure{\\begin{tikzpicture}',' d\'exactitude'),'The first crowded cell has both an e bowl/acute and a t stem; the next has a t and an e-like loop/acute. Their visible forms are preserved as two overlaps. The crop does not independently establish C\'s replacement chronology.','other',conf='medium',cc=True,n=17)
d('Long cancelled phrase after d\'exactitude',r"\deleted{y compris et de déterminer s'il admet un foncteur exact}",hsyn,r"\deleted{y compris et de déterminer s'il admet un foncteur exact}",'Each underlying word remains readable through the regular x overtyping, including the accent of déterminer and the apostrophe in s\'il. H\'s synopsis omits this abandoned formulation; it does not explicitly print it as live.','omission',n=18)
d('Long cancelled phrase: nine x impressions in interword spaces',r"\deleted{y compris et de déterminer s'il admet un foncteur exact}",hsyn,segment(R,'\\deleted{y}\\tikz','\ny compris l\'existence'),'The cancellation run fills every one of the nine spaces between the ten underlying words with an x. The reading draws these separate marks between the deleted words rather than dropping them.','drawing or diagram',cc=True,n=18)
d('Une replacing l\': attached leader',r"\deleted{l'}\inserted{une}intuition",hsyn,tikz(r'\begin{tikzpicture}[baseline=(intuition.base)]'),'The typed une is above the line. Its pen leader descends before the cancelled l\', touching the area before intuition. C has no curve. The preceding qui cancellation remains clear and is retained in the complete prose.','drawing or diagram',cc=True,n=19)
d('Section 3.1.3: remaining prose omitted by H',segment(C,'y compris l\'existence','\\begin{tikzpicture}[baseline=(n.base)]'),hsyn,segment(R,'y compris l\'existence','\\begin{tikzpicture}[baseline=(f.base)]'),'The source develops the geometrical interpretation and states a conditional about preservation of colimits and finite limits. H gives a compressed synopsis, not the continuous literal prose, including the cancelled qui, the l\' correction and the quotation wording.','omission',bbox=[284,1330,1664,1789])
d('f equals u-star: open-bottom enclosure',segment(C,'\\begin{tikzpicture}[baseline=(n.base)]','\noù'),'$f = u^*$',tikz(r'\begin{tikzpicture}[baseline=(f.base)]'),'The formula and its live comma lie inside a pen enclosure with a top and sides and small outward feet. C represents it; H\'s synopsis gives only the formula and omits the drawing. The typed letters have single contours; the high star is pen.','drawing or diagram',n=20)
d('u:F to E and est un: connected enclosure and two curves',segment(C,'où\n','\nmorphisme de topos'),r'$u \colon F \to E$',tikz(r'\begin{tikzpicture}[baseline=(u.base)]'),'The second open-bottom enclosure has a right side meeting the two arms of the curve around est un. C puts the est un curve in a separate picture, losing that attachment. The new drawing keeps both arms and the text in the same layout. H draws neither.','drawing or diagram',cc=True,n=20)
d('Application continue: duplicate opening quotation',"````application continue''",hsyn,"````application continue''",'The crop shows four distinct upright opening strokes: a lighter first pair and a darker second pair. One closing pair appears in the half. C correctly retains the duplication; H does not quote this literal phrase.','omission',n=21)
d('Final cancelled g and following blank-cell x',r"gauche,\deleted{$\mathrm{g}$}",hsyn,r"gauche,\deleted{$\mathrm{g}$}\tikz[baseline=(x.base)]{\node[inner sep=0pt] (x) {x};}",'A two-storey typed g is crossed by x, followed by a separate unoccupied cancellation x cell. C has the g but drops the following x. The preceding comma remains live.','omission',cc=True,n=22)
d('Footer continuation: en versus ou','en un foncteur','ou un foncteur','en un foncteur','The first short word has an e-like entry followed by the n shoulder, unlike the subsequent clearly looped ou before bigèbre. It reads en.','misread word',n=23)
d('Footer: uncertain mark after groupe','groupe, et','groupe et',r'groupe\unsure{,} et','A faint short low trace after groupe can be a comma, but its relation to the final letter flourish is not secure. C makes the comma definite; H omits it. The reading keeps the local comma candidate with doubt.','other',conf='low',cc=True,n=23)
d('Footer: cancelled article before module libre',r'\deleted{\unsure{le|de}}',r'que « module libre engendré »',r'\deleted{\unsure{le|de}}','The blob before the opening quote retains a loop and a short upright/oblique component, allowing le or de without deciding. H omits the cancellation entirely.','omission',conf='low',n=24)
d('Footer: quotation shape',"``module libre engendré''",'« module libre engendré »',"``module libre engendré''",'The local crop shows paired upright strokes at the opening; the half shows the closing pair. These are not guillemets.','misread symbol or index',n=24)
d('Footer: call sign and page-width separating line',segment(C,'\\figure{\\begin{tikzpicture}\n\\node[inner sep=6pt,text width=.88\\linewidth,align=left] (n) {\\tikz[baseline=-.3ex','\n\n\\deleted{2}'),r"appel d'une note de bas de page, de sa main",tikz('\\begin{tikzpicture}\n\\node[anchor=north west,inner sep=0pt,text width=.96\\linewidth'),'The low note has an upper-loop call sign with a long descending shaft and a page-width line immediately above it, with a raised jog at the left. The separator is now drawn relative to the final typescript and footer anchors. H only describes a footnote call editorially. C retains an approximation but relocates it inside the earlier insertion.','drawing or diagram',cc=True,bbox=[20,2003,1665,2125])

CD=[]
def cd(place,c,decision,evidence,conf='high',n=None,bbox=None):
 crop,box=cropinfo(n,bbox);CD.append(dict(place=place,C=c,decision=decision,evidence=evidence,crop=crop,bbox=box,bbox_source=source,confidence=conf))
cd('Top deleted word',r'\deleted{\illegible{1}}',r'\deleted{\illegible{1}}','The cancellation covers nearly all the letter bodies. A p-like descending trace survives, but neither a complete reading nor either trial word is established.',conf='low',n=1)
cd('End of s\'expriment',r"s'exprime\deleted{nt}\unsure{r}",r"s'exprime\deleted{nt}\unsure{r}",'The n/t ending is darkened and an r-like form may be superposed; the inserted peuvent is not used to prove that glyph.',conf='low',n=2)
cd('After inductives',r'\handwritten{)}','Retain the thin closing-shaped trace as an uncertain literal drawing, beside the definite typed close and stop.','The thin curve is separate from the typewritten parenthesis and meets or nearly meets the upper boundary stroke.',conf='medium',n=5)
cd('After second épimorphisme',r'\handwritten{\unsure{;|,}}','Retain a literal uncertain drawing; semicolon or overwritten comma remains possible.','The observed mark has an upper detached angle as well as a shaft and a lower loop/tail; it is more complex than ordinary punctuation.',conf='low',n=10)
cd('Cancelled phrase after c\'est d\'ailleurs',r'\deleted{\unsure{comme} nous le verrons au}',r'\deleted{\unsure{comme} nous le verrons au}','Nous le verrons au can be followed cell by cell; the first word remains partly obscured. The extra x cells and pen stroke are also retained.',conf='medium',n=11)
cd('Footer article before module libre',r'\deleted{\unsure{le|de}}',r'\deleted{\unsure{le|de}}','A small closed loop and a short upright survive the cancellation; they do not distinguish l from d securely.',conf='low',n=24)
cd('Opening fragment','sent','sent','The half has the four typed letters s-e-n-t at the beginning; no preceding letters are supplied.',bbox=[274,143,357,175])
cd('Interlinear section wording',r"est \inserted{\handwritten{en}} présenced'",r"est \inserted{\handwritten{en}} présenced'",'The e of présence touches the d cell without an intervening typewriter space; en is pen above the gap after est. The phrase belongs to the lower section.',n=13)
cd('Articles before épimorphisme','ne transforme pas en général épimorphisme en épimorphisme','ne transforme pas en général épimorphisme en épimorphisme','The typed line has no un, les or other article before either occurrence. The second occurrence continues as me on the next physical line.',bbox=[279,765,1668,881])
cd('Contre overprint',r'\deleted{f}contre','Preserve both f and c in an uncertain overlay, without deciding their order.','Both contours are visible, but their chronology does not follow from their black overlap.',conf='medium',n=8)
cd('Cancelled e in n\'est',r"n\deleted{e}'est",r"n\deleted{e}'est",'An e bowl survives beneath the x between n and apostrophe.',n=9)
cd('Propriétés overprints',r'propri\deleted{t}é\deleted{é}tés','Retain two local t/é overlays, with chronology uncertainty.','Both neighbouring crowded cells contain mixed contours. No separable overstrike edge determines which impression came first.',conf='medium',n=17)
cd('Opening quotations before application continue',"````application continue''","````application continue''",'There are four upright opening strokes, not merely two.',n=21)
cd('Final cancelled g',r"gauche,\deleted{$\mathrm{g}$}",r"gauche,\deleted{$\mathrm{g}$}\tikz[baseline=(x.base)]{\node[inner sep=0pt] (x) {x};}",'The g has a lower bowl below the cancellation x; another complete x follows it in a separate cell.',n=22)
cd('Own page and corrected section number',r'\mspage{\handwritten{23}}; \deleted{2}\handwritten{3}.1.3.','Retain own page 23 and 2 corrected to 3 in 3.1.3.','The upper-right 23 and the first numeral\'s pen 3 over typed 2 are visible. No date, title or total page count is present.',n=14)

I=[]
def inv(element,kind,bbox,first,hand='typewritten'):
 I.append(dict(sheet_kind='typescript',hand=hand,element=element,kind=kind,position={'bbox':bbox,'bbox_source':source},first_words_or_objects=first,transcribed='yes'))
inv('Own page number','margin note',[1610,77,1668,133],'23','handwritten')
inv('Upper marginal continuation','text',[271,17,1664,137],'les opérations fonctorielles','handwritten')
inv('Raised les','insertion',[280,15,320,41],'les','handwritten')
inv('Upper call sign','drawing',[268,20,285,72],'shaft, filled upper loop, open lower loop','handwritten')
inv('Upper enclosure','drawing',[241,17,1665,143],'left and stepped lower line','handwritten')
inv('Upper cancelled word','deletion',[625,20,722,49],'one unreadable word','handwritten')
inv('Peuvent addition','insertion',[675,42,787,64],'peuvent','handwritten')
inv('Peuvent leader','drawing',[681,59,797,91],'curved insertion stroke','handwritten')
inv('Expriment ending correction','deletion',[815,58,868,83],'nt with doubtful r replacement','handwritten')
inv('Top limit operators','display',[1090,49,1438,99],'lim with right arrow; lim with left arrow','handwritten')
inv('Opening continuation prose','text',[273,138,1666,313],'sent en termes de limites','typewritten')
inv('Thin extra closing trace','drawing',[1059,263,1080,319],'closing-shaped pen curve','handwritten')
inv('Paragraph marks around stop and Quant','drawing',[1062,255,1251,341],'opposing bracket strokes','handwritten')
inv('De plus addition','insertion',[1090,232,1665,278],'De plus, le foncteur','handwritten')
inv('Commute underline','drawing',[1416,255,1536,264],'low underline under commute','handwritten')
inv('De plus call sign','drawing',[1649,238,1668,281],'loop at bottom of descending shaft','handwritten')
inv('De plus lower boundary','drawing',[1064,253,1665,291],'low curved line','handwritten')
inv('Marginal paragraph instruction','margin note',[20,285,279,390],'à la ligne / après : Quant au...','handwritten')
inv('Marginal instruction enclosure','drawing',[21,254,285,443],'three-sided oblique outline','handwritten')
inv('Quant au continuous prose','text',[275,278,1668,1095],'Quant au foncteur image directe','typewritten with pen signs')
inv('Direct image map addition','insertion',[473,317,627,350],': E to E-prime','typewritten letters and pen arrow')
inv('Direct image map leader','drawing',[464,326,662,404],'curve before live baseline comma','handwritten')
inv('Par suite addition','insertion',[1427,309,1609,344],'par suite','typewritten')
inv('Par suite leader','drawing',[1497,329,1621,386],'curve before toute','handwritten')
inv('Exclusivement addition','insertion',[1095,452,1354,484],'exclusivement','typewritten')
inv('Exclusivement leader','drawing',[1146,471,1389,538],'curve before (telles','handwritten')
inv('Cancelled dans','deletion',[1211,562,1307,589],'dans','typewritten x overtyping')
inv('Parmi replacement','insertion',[1213,542,1313,571],'parmi','typewritten')
inv('Mixed f/c cell','deletion',[628,633,656,666],'f and c contours; order uncertain','typewritten overlap')
inv('Cancelled e in nest','deletion',[1098,638,1125,665],'e','typewritten x overtyping')
inv('Stars on direct-image functors','insertion',[433,361,1058,954],'three low stars in u-star','handwritten')
inv('Tall trace after épimorphisme','drawing',[323,826,349,886],'loop, shaft, detached upper angle','handwritten')
inv('Large opening parenthesis','insertion',[346,832,371,892],'(','handwritten')
inv('Cancelled clause','deletion',[710,844,1183,882],'comme nous le verrons au','typewritten x overtyping')
inv('Clause cancellation x cells','drawing',[674,848,1183,882],'lowered x before comme and four interword x marks','typewritten cancellation marks')
inv('Pen cancellation over first words','drawing',[682,834,935,871],'horizontal and short rising trace','handwritten')
inv('Added à','insertion',[722,906,757,958],'à','handwritten')
inv('Closing parenthesis after suivant','insertion',[766,1033,791,1111],')','handwritten')
inv('Par suite lower addition','insertion',[812,1021,1653,1100],'Par suite, il ne','handwritten')
inv('Cancelled transforme','deletion',[1122,1054,1336,1093],'transforme','handwritten')
inv('Lower pas and uncertain cancellation extent','deletion',[1332,1055,1392,1094],'pas, live/deleted uncertainty','handwritten')
inv('Raised s\'étend pas','insertion',[1162,1024,1345,1063],"s'étend pas",'handwritten')
inv('Lower addition call sign','drawing',[1637,1030,1656,1097],'upper loop with descending shaft','handwritten')
inv('Section 3.1.3 main prose','text',[278,1121,1664,2016],'En pratique, lorsqu\'on','typewritten')
inv('First section numeral correction','deletion',[281,1128,313,1163],'2 changed to pen 3','typewritten and handwritten')
inv('Se donne cancellation','deletion',[909,1130,1067,1158],'se donne','typewritten x overtyping')
inv('Se donne space cancellation x','drawing',[949,1134,969,1156],'x in former space','typewritten cancellation mark')
inv('Est présenced\' addition','insertion',[890,1091,1162,1128],"est présenced'",'typewritten')
inv('En above est-présence gap','insertion',[946,1078,988,1103],'en','handwritten')
inv('Presence leader','drawing',[1062,1092,1224,1159],'curve before un','handwritten')
inv('f:E to F map','display',[1337,1121,1504,1157],'f:E to F','typed letters, pen arrow')
inv('Underlined U','display',[280,1200,309,1236],'underlined U-topos','typewritten')
inv('Toutes addition','insertion',[1262,1158,1359,1194],'toutes','handwritten')
inv('Toutes leader','drawing',[1267,1183,1388,1230],'curve before les','handwritten')
inv('First propriétés overlap','deletion',[1476,1194,1502,1227],'t and é in same cell','typewritten overlap')
inv('Second propriétés overlap','deletion',[1500,1193,1525,1227],'é and t in same cell','typewritten overlap')
inv('Long cancelled clause','deletion',[559,1270,1636,1304],"y compris et de déterminer s'il admet un foncteur exact",'typewritten x overtyping')
inv('Long clause space cancellation marks','drawing',[559,1270,1636,1304],'nine interword x impressions','typewritten cancellation marks')
inv('Qui cancellation','deletion',[1206,1478,1268,1513],'qui','typewritten x overtyping')
inv('L-apostrophe cancellation','deletion',[1187,1546,1229,1581],"l'",'typewritten x overtyping and pen')
inv('Une addition','insertion',[1146,1517,1219,1547],'une','typewritten')
inv('Une leader','drawing',[1171,1530,1252,1589],'curve before l\'intuition','handwritten')
inv('f equals u-star formula','display',[972,1750,1134,1804],'f=u-star,','typed letters; pen star')
inv('First formula enclosure','drawing',[906,1745,1160,1815],'open-bottom top and sides with feet','handwritten')
inv('u:F to E formula','display',[1211,1757,1368,1798],'u:F to E','typed letters; pen arrow')
inv('Second formula enclosure','drawing',[1186,1743,1394,1818],'open-bottom outline','handwritten')
inv('Connected est un curves','drawing',[1378,1737,1490,1803],'two curved arms around est un','handwritten')
inv('Duplicated opening quotation','text',[449,1907,503,1932],'four opening strokes before application','typewritten')
inv('Final cancelled g','deletion',[1581,1980,1608,2016],'g','typewritten x overtyping')
inv('Final extra x','drawing',[1607,1983,1632,2008],'x after g','typewritten cancellation mark')
inv('Footer separator','drawing',[20,2003,1665,2032],'page-width line with left raised jog','handwritten')
inv('Footer call mark','drawing',[76,2034,99,2116],'upper loop and descending shaft','handwritten')
inv('Footer continuation','text',[116,2039,1637,2125],'en un foncteur sur des objets','handwritten')
inv('Footer deleted article','deletion',[1101,2082,1147,2113],'le or de','handwritten')

remaining=[
 dict(place='Top cancelled word',reading=r'\deleted{\illegible{1}}',alternatives=['No complete alternative is established; one p-like descender survives.'],confidence='low'),
 dict(place="Ending of s'expriment",reading=r"s'exprime\deleted{nt}\unsure{r}",alternatives=['r-like replacement','unresolved retouching over the old ending'],confidence='low'),
 dict(place='Thin curve after inductives',reading='literal closing-shaped pen trace',alternatives=['second closing parenthesis','insertion-boundary component'],confidence='medium'),
 dict(place='Contre mixed cell',reading='c/f overlay',alternatives=['c written over f','f written over c; chronology unproved'],confidence='medium'),
 dict(place='After second épimorphisme',reading='literal loop/shaft/upper-angle drawing',alternatives=['semicolon','overwritten comma or other punctuation trace'],confidence='low'),
 dict(place='First cancelled word after ailleurs',reading=r'\unsure{comme}',alternatives=['No other complete word established'],confidence='medium'),
 dict(place='Cancelled handwritten transforme',reading=r'\deleted{\unsure{transforme}}',alternatives=['Middle letters concealed; no competing complete word established'],confidence='medium'),
 dict(place='Lower pas under raised s\'étend pas',reading=r'\unsure{pas|\deleted{pas}}',alternatives=['pas remains live','pas belongs to the cancellation despite weak crossing'],confidence='medium'),
 dict(place='Two propriétés cells',reading='two mixed é/t overlays',alternatives=['C\'s t-to-é then é-to-t chronology','reverse or simultaneous overlapping impressions'],confidence='medium'),
 dict(place='After footer groupe',reading=r'\unsure{,}',alternatives=['comma','terminal flourish of preceding letter'],confidence='low'),
 dict(place='Footer cancelled article',reading=r'\deleted{\unsure{le|de}}',alternatives=['le','de'],confidence='low')]
report=dict(page='C123-02_123_scan040',reader='R2',viewed={'whole':source,'a':source[:-4]+'_a.jpg','b':source[:-4]+'_b.jpg'},reading_file='out/readers/C123-02_123_scan040/R2/reading.tex',differences=D,c_doubts=CD,inventory=I,remaining_doubts=remaining,
notes=[
'This is a typescript sheet with extensive handwritten corrections and marginal continuations. Whole image dimensions are 1684 x 2141 pixels; a is 1684 x 1150, b is 1684 x 1151. The b half starts at whole-image y=990. The whole and both halves were each viewed once.',
'The upper continuation says that inverse image commutes with familiar functorial constructions in terms of colimits and finite limits, giving free objects and tensor products as examples. Its deleted word and corrected infinitive ending remain uncertain.',
'The main paragraph says direct image respects algebraic structures definable exclusively by projective limits, but in general is not right exact and need not preserve epimorphisms. It connects that failure with the cohomological properties to be treated in the following exposé.',
'The lower handwritten addition says the direct-image functor does not generally extend to objects such as comodules, bialgebras or torsors and does not generally commute with free-module and tensor-product constructions. Its text resumes in the bottom margin through a repeated call mark.',
'Section 3.1.3 advises stating all exactness and adjoint properties of a functor between topoi in order to understand its geometric nature. It gives the conditional inverse-image interpretation f=u-star and starts a further sentence about preservation of arbitrary projective limits.',
'The source contains qualifications such as "en général" and "s\'il s\'avère que". These are not admissions of a missing proof. I found no explicit proof hesitation such as an authorial question or "not proved" note on this sheet.',
'The visible own page is 23, the archive number is inverted 39 at upper left, and the source section number has typed 2 corrected to pen 3 in 3.1.3. There is no date, title sheet or total page count.',
'H begins with an editorial synopsis and directly transcribes mainly the handwritten additions. Its paraphrase is not treated as a verbatim rendering of the typescript or as proof that a cancelled word was printed live. Omissions of literal text and drawings are nevertheless recorded.',
'The cross-page references in the source, including § 6 and the previous footnote, were transcribed without consulting any other page. No OCR, recognition, web or external edition was used.',
'All source curves, enclosure lines, loop calls, detached punctuation trace, and preserved cancellation-space x impressions mentioned in the report have corresponding TikZ content in reading.tex. The extra x marks are cancellation ink, not reconstructed underlying words.'
],notation=[
{'place':'Inserted direct-image map','visible':'Single-contour typed E and E-prime; pen arrow to the right; pen low star on u','reading':r"\mathrm{u}_{\handwritten{*}} : \mathrm{E}\longrightarrow\mathrm{E}'",'candidates':['ordinary roman E, not script or double-struck'],'evidence_crop':cp+'07_directe_map.jpg'},
{'place':'Main body E after objets','visible':'Ordinary serifed typewriter E without a detached underline','reading':r'\mathrm{E}','candidates':['ordinary roman E'],'evidence':'a half, [1521,415,1551,445]'},
{'place':'Section f:E to F','visible':'Ordinary single typed E and F with a handwritten right arrow','reading':r'\mathrm{f}:\mathrm{E}\longrightarrow\mathrm{F}','candidates':['ordinary roman E and F'],'evidence_crop':cp+'15_f_map.jpg'},
{'place':'U-topos','visible':'Single-contour typed U and independent low rule','reading':r'\underline{\mathrm{U}}','candidates':['underlined roman U'],'evidence_crop':cp+'16_U.jpg'},
{'place':'Lower interpretation formulas','visible':'Ordinary typed f,u,F,E, typed equality and colon, pen high star and right arrow','reading':r'\mathrm{f}=\mathrm{u}^{*};\quad\mathrm{u}:\mathrm{F}\longrightarrow\mathrm{E}','candidates':['ordinary roman letters'],'evidence_crop':cp+'20_boxes.jpg'},
{'place':'Top limit operators','visible':'lim with a separate right arrow below; lim with a separate left arrow below','reading':r'\varinjlim,\varprojlim','candidates':['right-directed and left-directed limits'],'evidence_crop':cp+'03_lims.jpg'},
{'place':'Call marks','visible':'Top pair uses descending shafts/lower loops; lower pair uses an upper loop and descending shaft','reading':'literal TikZ marks','candidates':['linking marks, not assigned an alphabetic or set-theoretic identity']},
{'place':'Mixed overprints','visible':'c/f and two é/t cells have distinct superposed letter contours','reading':'local uncertain TikZ overlays','candidates':['chronology unresolved; not double striking of a single letter']}
],abbreviations=[
{'form':'p.ex.','expansion':'par exemple (editorial expansion only)'},
{'form':'cf.','expansion':'confer / compare (editorial expansion only)'},
{'form':'etc.','expansion':'et cetera (editorial expansion only)'},
{'form':'i.e.','expansion':'id est / that is (editorial expansion only)'},
{'form':'§','expansion':'section (editorial expansion only)'}
],math_checks=[
{'check':'Domain and codomain of the lower inverse-image interpretation','performed':True,'result':'I checked the directions locally: f:E to F and u:F to E make u-star:E to F, so the stated f=u-star has matching source and target. This is only a direction/type check, not a proof of existence of u.'},
{'check':'Limit-arrow distinction in the upper addition','performed':True,'result':'I compared the actual arrows: the first points right and the second left. They support varinjlim then varprojlim, respectively. No general preservation theorem was proved.'},
{'check':'Claims about exactness, colimits and adjoints','performed':False,'result':'These were read as claims and conditional statements of the sheet. I did not prove the assertions about right exactness, epimorphisms or existence of adjoints, and did not use expected mathematics to settle the corrected letters.'}
],crop_count=25,workflow_feedback='Read all required packet and brief files; whole/a/b viewed once each. All 25 preselected local crops were produced with out/scripts/crop.py and viewed once; none was recropped. Complete reading.tex was saved before report.json. No other reader files, root decisions, other-page images, OCR, research or further agents were used. A text-only brace/environment check of the saved reading found balanced braces and 21 matched TikZ picture environments. No compilation was performed.')
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Saved report.json:',len(D),'differences;',len(CD),'C doubts;',len(I),'inventory elements;',len(remaining),'remaining doubts.')
