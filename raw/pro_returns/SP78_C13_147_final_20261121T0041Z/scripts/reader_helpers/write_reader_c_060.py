from pathlib import Path
import json,re
packet=Path('/workspace/scratch/ea90d891106a/runtime/packets/147_scan060')
work=Path('/workspace/scratch/ea90d891106a/SP78_C13_147_work')
out=work/'reader_returns/147_scan060';out.mkdir(parents=True,exist_ok=True)
s=(packet/'C.tex').read_text()
s=s.replace(r'\Gamma\text{ \unsure{---} }',r'\Gamma\text{ --- }')
s=s.replace(r'\deleted{\unsure{\mathfrak S_{\alpha_0,\alpha_1}}}',r'\deleted{\unsure{\prod_{\alpha\in\{\alpha_0,\alpha_1\}}}}')
s=s.replace(r'\mathfrak S_{\deleted{\unsure{\widehat I}}(\widehat I_{\alpha_0}\amalg\widehat I_{\alpha_1})}',r'\mathfrak S_{\deleted{\unsure{\widehat I}}\bigl(\widehat I_{\alpha_0}\amalg\widehat I_{\alpha_1}}')
s=s.replace(r'\Gamma\longrightarrow\underbrace{\mathbf Z/2\mathbin{\cdot}(\mathfrak S_4\times\mathfrak S_4)}_{\text{prod. }\frac12\text{ direct}}',r'''\begin{array}{rcl}
\Gamma&\longrightarrow&\mathbf Z/2\mathbin{\cdot}(\mathfrak S_4\times\mathfrak S_4)\\
&&\text{prod. }\frac12\text{ direct}
\end{array}''')
s=s.replace("les ``cas nouveaux'' de (74)","les ``cas \\unsure{''|``}nouveaux'' de (74)")
s=s.replace('pour le cas des dim.',r'pour le cas \unsure{des|de} dim.')
s=s.replace(r'\pi_1',r'\Pi_1')
s=s.replace('donnerait la clef',r'\unsure{donnerait|donnera} la clef')
(out/'proposed.tex').write_text(s)
boxes={
'01':[25,28,172,540], '02':[385,118,1562,217], '03':[386,205,1688,389],
'04':[245,548,516,637], '05':[1345,502,1666,620], '06':[548,743,1625,923],
'07':[228,948,1675,1137], '08':[17,1198,210,1367], '09':[417,1115,1568,1336],
'10':[229,1363,1119,1463], '11':[565,1490,858,1578], '12':[491,1708,926,1812],
'13':[1414,1895,1635,1998], '14':[985,2029,1508,2136], '15':[217,1960,1337,2094],
'16':[34,2289,93,2339], '17':[390,1593,878,1701], '18':[899,24,985,84]}
changes=[]
def ch(place,C,H,final,evidence,crop,confidence,kind,error,against_C=False,against_H=True,marked=False,consequential=False):
 changes.append(dict(id=f'060-{len(changes)+1:02}',place=place,C=C,H=H,final=final,evidence=evidence,crop=f'147_scan060_place{crop}.png',box=boxes[crop],confidence=confidence,against_C=against_C,against_H=against_H,kind=kind,marked_in_H=marked,error_sheet_kind=error,consequential=consequential))
ch('Rotated upper-left marginal insertion',r'\widehat M_G',r'\widetilde M_G',r'\widehat M_G','The accent over M is a pointed two-stroke roof. The broad curved strokes around the formula are its insertion guide and do not form a tilde over M.','01','high','misread symbol or index','symbols and indices')
ch('Rotated margin, alleged illegible matter after dimension 2','no extra illegible word',r'\ill{} after de dim 2','no extra illegible word','The second written baseline ends with the clear 2. The remaining lower ink consists of the inserted hat-M_G and its guide; there is no independent word occupying the alleged illegible slot.','01','high','text not on the page','text not on page')
ch('Rotated margin, placement of inserted hat-M_G',r'modulaires \inserted{$\widehat M_G$} de dim $2$',r'modulaires de dim $2$ \ill{} $\widetilde M_G$',r'modulaires \inserted{$\widehat M_G$} de dim $2$','The guide rises from around hat-M_G to the gap after the end of modulaires and before de. Its apex fixes the insertion point; it does not attach after the digit 2.','01','high','insertion or placement','insertions put in wrong place')
ch('Display (74), cancelled object before the live S in row 3',r'\deleted{\unsure{\mathfrak S_{\alpha_0,\alpha_1}}}','No cancelled formula in the array; editorial note reports a struck symbol and a possible alpha-in surcharge',r'\deleted{\unsure{\prod_{\alpha\in\{\alpha_0,\alpha_1\}}}}','A broad horizontal top bar and two long upright remnants survive the cross-hatching, favouring a product sign rather than a looped S. Below it the leftmost alpha-shaped loop and an epsilon/in-shaped sign are visible. The following braces and alpha indices are largely crossed; the entire proposed product and index remain explicitly doubtful. The crop contains both complete adjacent rows, so no isolated glyph has been inferred without its formula.','03','low','misread symbol or index','symbols and indices',against_C=True,marked=True)
ch('Display (74), row 3, cancelled start of the live S subscript',r'\deleted{\unsure{\widehat I}}','omitted',r'\deleted{\unsure{\widehat I}}','Before the live opening parenthesis is a separate small crossed group with an I-like upright/base and a roof-like stroke. Its cancellation is distinct from the larger cancelled product to the left. The hat-I reading stays doubtful under those strokes.','03','medium','omission','struck text')
ch('Display (74), row 3, opening parenthesis in live union subscript','opening ( before hat-I_alpha0','no parenthesis',r'\bigl( before \widehat I_{\alpha_0}','A long curved stroke descends immediately before the first live hat-I, to the right of the small crossed-out subscript. It is a visible opening parenthesis and is retained.','03','high','omission','symbols and indices')
ch('Display (74), row 3, end of live union subscript','closing ) after hat-I_alpha1','no closing parenthesis','no closing parenthesis','After the second I and its alpha_1 subscript there is no separate closing curve. The next visible signs are the higher simeq and S_8. C supplies a balancing parenthesis unsupported by the ink. The proposed text deliberately preserves the unmatched opening, using bigl( without a paired left/right construct.','03','high','text not on the page','text not on page',against_C=True,against_H=False)
ch('Display (74), row 4, small cancelled superscript beside S',r'\deleted{\unsure{4|*}}','not transcribed in the array',r'\deleted{\unsure{4|*}}','A compact dark overdrawn glyph sits above the right-hand end of S. There are intersecting short strokes, but they do not certify 4 or an asterisk. Its presence and deletion are retained without resolving the C doubt.','03','low','omission','struck text',marked=True)
ch('NB, small cancelled item before Dans',r'\deleted{\unsure{à}}','omitted',r'\deleted{\unsure{à}}','There is a distinct heavily retraced group between the underlined NB and the capital D. A lower closed loop survives, but the upper strokes conceal whether it is à. It remains a doubtful deletion, rather than being omitted.','04','low','omission','struck text')
ch('Unnumbered display below NB, label under the product',r'\underbrace{\mathbf Z/2\mathbin{\cdot}(\mathfrak S_4\times\mathfrak S_4)}_{\text{prod. }\frac12\text{ direct}}',r'\underbrace{\mathbb Z/2\cdot(\mathfrak S_4\times\mathfrak S_4)}_{\text{prod. }\tfrac12\text{ direct}}',r'\begin{array}{rcl}\Gamma&\longrightarrow&\mathbf Z/2\mathbin{\cdot}(\mathfrak S_4\times\mathfrak S_4)\\&&\text{prod. }\frac12\text{ direct}\end{array}','The entire space between the group formula and the lower words is visible and blank. The lower label prod. 1/2 direct is written independently; there is no bracket or brace joining it to the formula. Both witnesses add an underbrace.','06','high','drawing or diagram','drawings and diagrams',against_C=True)
ch('Unnumbered display below NB, terminal punctuation','no full stop','full stop','no full stop','A short isolated horizontal dark tick occurs far to the right of the closing parenthesis. Its separation and dash-like shape do not establish that it is the displayed formula\'s full stop. The proposed text keeps C\'s absence of punctuation and records the tick as an unresolved punctuation question.','06','low','other','other')
ch('Beginning of paragraph above (75)',r'par rapport aux',r"pour l'essentiel, les",r'par rapport aux','After que the ink has the p descender and short ar group, then a long r/pp/ort sequence with two descenders, then the low aux ending. There is no tall l apostrophe group or sequence corresponding to essentiel.','07','high','misread word','words')
ch('Second line above (75), first noun',r'schémas modulaires',r'\add{seules} \struck{\ill{}} multiplicités ... modulaires',r'schémas modulaires','The next physical line begins with the s/c/h sequence and tall h before the low émas ending. It is one live word, schémas, followed by modulaires. There is no separate interlinear seules or cancelled block at that location.','07','high','misread word','words')
ch('Second line above (75), attachment of hat-M_G',r'modulaires \inserted{$\widehat M_G$} de dim $1$',r'multiplicités \add{$\widehat M_G$} modulaires de dim $1$',r'modulaires \inserted{$\widehat M_G$} de dim $1$','The small hat-M_G is written above the gap following modulaires, with a curved guide descending to that gap immediately before de. It does not precede modulaires.','07','high','insertion or placement','insertions put in wrong place')
ch('Second line above (75), cancelled words after dim 1',r'\deleted{\unsure{qui sont}}',r'\struck{\ill{}}',r'\deleted{\unsure{qui sont}}','A descending q-like initial stroke and the i dot survive, followed by low segments compatible with sont. The horizontal cancellation crosses the bodies, so the complete words remain doubtful; nevertheless the visible traces should not be replaced by a wholly illegible block.','07','medium','readable ink left as \\ill{}','readable ink left as illegible')
ch('Interlinear replacement above the preceding cancellation',r'\inserted{ils sont deux :}',r'\uncertain{nouvelles} sont :',r'\inserted{ils sont deux :}','The upper replacement has a short initial ils group, the s/on/t strokes of sont, and a separate d-led deux group before the two vertically spaced colon dots. The lower crossed line is distinct; H\'s nouvelles does not match the short initial group.','07','high','misread word','words',marked=True)
ch('Slanted margin note beside display (75)',r'(cas élémentaires!)',r'(cas élémentaires)',r'(cas élémentaires!)','The note ends with a separate upright and lower dot before its curved closing parenthesis. The exclamation point is dark and distinct from the parenthesis.','08','high','omission','omissions')
ch('Display (75), first object',r'\widehat M^!_{0,4}',r'M^!_{0,4}',r'\widehat M^!_{0,4}','A pointed angular roof is plainly present above the first M, just as above the second row\'s M. The raised upright-plus-dot is the exclamation exponent and is separate from that roof.','09','high','misread symbol or index','symbols and indices')
ch('Display (75), lower row action word','trivialt','trivialement','trivialt','After trivial the word ends in a compact terminal t-shaped stroke, followed immediately by the comma. There is no written ement sequence. The shortened form is retained rather than expanded.','09','high','abbreviation expanded or spelling modernised','abbreviations expanded spelling modernised')
ch('Quoted phrase immediately below (75)',"les ``cas nouveaux''",'les « cas nouveaux »',"les ``cas \\unsure{''|``}nouveaux''",'Three separate dark quotation groups are visible: before cas, between cas and nouveaux, and after nouveaux. Both witnesses omit the middle group. The mark is not pale paper noise. Its opening/closing direction cannot be certified, so the extra quotation pair is preserved with that local doubt. The outer marks are paired high ticks, not guillemets.','10','medium','omission','omissions',against_C=True)
ch('Word preceding the reference (74) below (75)','de','dans','de','The d has a high loop followed by a single long low e-shaped continuation ending in a hook. There are no separate a/n/s humps before the opening parenthesis.','10','high','misread word','words')
ch('Opening of the last paragraph','en tous','en tout','en tous','The final letter of tous curves downward at the right, without the upright and cross stroke of t. The first t in the same word supplies a direct comparison. The manuscript\'s tous is retained despite the usual spelling of the expression.','11','high','misread word','words')
ch('Last paragraph, phrase le cas ... dim. modulaires','des','de',r'\unsure{des|de}','The word begins with the looped d and has a long low continuation ending in a descending terminal hook. That can support the compressed s in C\'s des, but the final s is not cleanly isolated from the e-tail. The disagreement remains explicit rather than being settled from grammar.','12','medium','misread word','words')
ch('Last paragraph, fundamental-group symbol',r'\pi_1',r'\Pi_1',r'\Pi_1','The letter has a long straight horizontal top bar over two tall straight uprights. It has neither the lower-case pi curve nor short lower-case proportions. The small separate subscript 1 is also visible.','13','high','misread symbol or index','symbols and indices',against_C=True,against_H=False,consequential=True)
ch('Last paragraph, verb before la clef','donnerait','donnera',r'\unsure{donnerait|donnera}','The d loop and several low separate strokes of donner- are visible. The final strokes are compressed and do not provide a plainly separate i-dot and tall t, but neither can the ending be certified letter by letter. C\'s conditional and H\'s future remain alternatives in place.','14','low','misread word','words')
ch('Interlinear qualifier after Pi_1',r'\inserted{discrets (i.e. dans le contexte analytique)}','same words printed as continuous base text',r'\inserted{discrets (i.e. dans le contexte analytique)}','The qualifier occupies a smaller separate baseline in the gap between the Pi_1 line and the line beginning impliqués. It starts further left and runs underneath the preceding text. Its physical insertion state is visible.','15','high','insertion or placement','insertions put in wrong place')
ch('Light pencil foliation in lower-left corner',r'\margin{59}','omitted',r'\margin{59}','The first pencil figure has the upper stroke and descending bowl of 5; the second has a closed upper loop and descending tail of 9. They are much lighter than the manuscript ink and are retained as separate margin foliation.','16','high','omission','omissions')
ch('Quotation marks around élémentaires in the last paragraph',"``élémentaires''",'« élémentaires »',"``élémentaires''",'The two flanking groups are paired high strokes. They are not chevron-shaped guillemets. The crossing stroke within élémentaires belongs to its t; no separate cancellation of the word is present.','17','high','other','other')

# Only the packet's indexed MARKS item is entered in decisions.
decisions=[dict(id='M1033',cote=147,scan=60,decision='first',reading='---',ink='A long horizontal repetition stroke occupies the text column after Gamma, with small pen thickenings along it. It has no legible letter ascenders/descenders. The two lower rows have corresponding separated dashes in the same column. The full second-row formula, including both M indices and the group on the right, was read on this crop; the mark is retained as the manuscript\'s dash/ditto stroke, not expanded to words.',crop='147_scan060_place02.png (385,118,1562,217)',confidence='high')]

inventory=[]
def inv(i,kind,position,first,hand='his hand'):
 inventory.append(dict(scan=60,sheet_kind='text',hand=hand,element=f'{i:02}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv(1,'text','Top centre, y35','29')
inv(2,'margin note','Upper-left margin, rotated clockwise for reading','[deleted] multiplicités modulaires ... de dim 2')
inv(3,'insertion','Below the rotated marginal note','hat-M_G')
inv(4,'display','Top, five rows grouped by a left brace','(74), M-hat!_{0,5}; M-hat!_{1,2}; three products and Gamma actions')
inv(5,'deletion','Display (74), row 3 before the live S','Doubtful product with lower alpha-in index')
inv(6,'deletion','Display (74), row 3 subscript of the live S','Doubtful hat-I before the opening parenthesis')
inv(7,'deletion','Display (74), row 4, above S','Doubtful 4 or *')
inv(8,'text','Two lines y550–710','NB Dans le cas 3°) ... dans S_8 par l\'intermédiaire de')
inv(9,'deletion','After NB and before Dans','Doubtful à')
inv(10,'deletion','After Gamma at right of NB first line','opère')
inv(11,'insertion','Above the cancelled opère','s\'envoie')
inv(12,'display','Unnumbered two-level display, y755–905','Gamma arrow Z/2 dot (S_4 times S_4), lower label prod. 1/2 direct')
inv(13,'text','Two lines y985–1110','On peut considérer que par rapport aux schémas modulaires ...')
inv(14,'insertion','Above modulaires/de near y1030','hat-M_G')
inv(15,'deletion','After dim 1 near y1080','qui sont, doubtful')
inv(16,'insertion','Above that cancellation','ils sont deux :')
inv(17,'margin note','Slanted left note beside (75)','(cas élémentaires!)')
inv(18,'display','Two rows, y1130–1320','(75), M-hat!_{0,4}, M-hat!_{1,1}, Gamma actions')
inv(19,'text','One line y1360–1445','les quoted cas, extra quote, nouveaux, de (74) ...')
inv(20,'text','Eight main baselines y1500–2320','Cela fait en tous essentiellement quatre cas ... cas général.')
inv(21,'insertion','Interlinear baseline y2010–2080','discrets (i.e. dans le contexte analytique)')
inv(22,'text','Lower-left corner','59','lighter pencil hand; attribution not established')

doubts=[
 dict(place='Start of rotated upper-left note',reading=r'\deleted{\illegible{1}}',alternatives='No physically complete word recovered',confidence='low',reason='Dense short crossing strokes at the start overlap the following writing; the underlying deleted word cannot be read in full.'),
 dict(place='Display (74), large cancelled row-3 object and lower index',reading=r'\deleted{\unsure{\prod_{\alpha\in\{\alpha_0,\alpha_1\}}}}',alternatives=r'C: \mathfrak S_{\alpha_0,\alpha_1}; H editorial possibility: alpha-in surcharge',confidence='low',reason='The top bar and uprights favour a product, and alpha plus an in-shaped mark survive below. Most of the remaining index is covered by diagonal cancellation. The full formula is proposed with a doubt, not certified by its mathematical plausibility.'),
 dict(place='Display (74), small cancelled subscript before live parenthesis',reading=r'\deleted{\unsure{\widehat I}}',alternatives='No further definite glyph proposed',confidence='medium',reason='The small group is crossed through its upright and lower bar; the roof-like mark is visible but not every stroke is separable.'),
 dict(place='Display (74), row-4 cancelled superscript',reading=r'\deleted{\unsure{4|*}}',alternatives='4 or asterisk',confidence='low',reason='Repeated short overdrawings make both the original glyph and its exact shape uncertain.'),
 dict(place='NB, cancelled item before Dans',reading=r'\deleted{\unsure{à}}',alternatives='No complete alternative',confidence='low',reason='The closed lower loop is visible, but overdrawings conceal the top and any accent.'),
 dict(place='Below NB, isolated far-right tick',reading='No punctuation transcribed after the formula',alternatives='H treats the dark far-right tick as a full stop',confidence='low',reason='The tick is short and horizontal, with a large blank gap from the formula. Its role as punctuation is not established.'),
 dict(place='Before (75), cancelled words after dim 1',reading=r'\deleted{\unsure{qui sont}}',alternatives='H leaves the span wholly illegible',confidence='medium',reason='The initial descender and i-dot survive but the horizontal strike covers the low bodies of most letters.'),
 dict(place='Between cas and nouveaux below (75)',reading=r"\unsure{''|``}",alternatives='Closing or opening double quotation marks',confidence='medium',reason='A third dark high quotation group is clearly present, but its two-stroke direction is not decisive.'),
 dict(place='Final paragraph, le cas des/de dim.',reading=r'\unsure{des|de}',alternatives='des or de',confidence='medium',reason='The descending terminal hook may be the compressed s of des or merely the tail of de.'),
 dict(place='Final paragraph, verb before la clef',reading=r'\unsure{donnerait|donnera}',alternatives='donnerait or donnera',confidence='low',reason='The last strokes are isolated and very compressed; no plainly separate it ending can be certified. Grammar does not settle the ink.')]

# Exact proposed TeX, not descriptions, is supplied for blind rereading boxes.
second=[]
def sb(n,kind,box,reading):
 second.append(dict(box=f'B{n:02}',kind=kind,x0=box[0],y0=box[1],x1=box[2],y1=box[3],reading=reading))
margin=s[s.index(r'\margin{'):s.index('\n\\[')]
displays=re.findall(r'\\\[\n(.*?)\n\\\]',s,re.S)
assert len(displays)==3
nb=s[s.index(r'\uline{NB}'):s.index('\n\\[',s.index(r'\uline{NB}'))]
on=s[s.index('On peut considérer'):s.index('\n\\margin{(cas')]
newcases=s[s.index("les ``cas"):s.index('\n\nCela')]
sb(1,'margin note',boxes['01'],margin)
sb(2,'doubtful formula',[184,22,1689,471],r'\mspage{29}'+'\n'+r'\['+'\n'+displays[0]+'\n'+r'\]')
sb(3,'struck passage',[245,502,1667,734],nb)
sb(4,'handwritten number',boxes['06'],r'\['+'\n'+displays[1]+'\n'+r'\]')
sb(5,'insertion',[228,948,1675,1125],on)
sb(6,'margin note',boxes['08'],r'\margin{(cas élémentaires!)}')
sb(7,'handwritten number',[202,1124,1570,1336],r'\['+'\n'+displays[2]+'\n'+r'\]')
sb(8,'word disagreement',[228,1338,1670,1467],newcases)
sb(9,'word disagreement',boxes['11'],'en tous')
sb(10,'word disagreement',boxes['17'],"``élémentaires''")
sb(11,'handwritten number',[228,1687,1670,1812],r"pour le cas \unsure{des|de} dim. modulaires $\leq2$. J'ai")
sb(12,'handwritten number',[1478,1912,1596,1999],r'$\Pi_1$')
sb(13,'insertion',[217,2008,1510,2175],r'\inserted{discrets (i.e. dans le contexte analytique)} impliqués dans ces cas, \unsure{donnerait|donnera} la clef')
sb(14,'handwritten number',boxes['16'],r'\margin{59}')
sb(15,'handwritten number',boxes['18'],r'\mspage{29}')

report=dict(scan=60,reader='reader_c',physical_lines_read=33,changes=changes,decisions=decisions,inventory=inventory,doubts=doubts,
notes=[
'The manuscript lists five displayed modular-multiplicity cases of dimension 2 in (74), with the written Gamma actions through permutation groups in the first four rows and a trivial action in the last. The products and superscript exclamation marks are transcribed as written. This summary reports manuscript claims; the group-action assertions were not independently proved.',
'The NB states that the third case maps into S_8 through the written Z/2 dot (S_4 times S_4), labelled prod. 1/2 direct. The label is physically below the formula without a brace. The likely mathematical interpretation is a semidirect product with two four-element blocks; that interpretation helps locate the indices but is not substituted for the literal dot or the worded label.',
'The manuscript compares the dimension-2 list with two dimension-1 elementary cases (75), calls M-hat!_{0,5} and M-hat!_{1,2} the new cases, and suggests that understanding the discrete Pi_1 groups of four elementary cases might give the key to the general case. This is the author\'s stated expectation, not a proof established in this reading.',
'The cancelled row-3 object is proposed as a doubtful product with a lower alpha-in index because of surviving ink, but neither its complete index nor its mathematical appropriateness is certified. The live disjoint-union subscript has an opening parenthesis without a visible closing one; the imbalance is retained rather than repaired. Literal expression en tous is also retained.',
'Physical-line count 33: five rows in (74); two NB prose baselines plus its one interlinear replacement; the unnumbered formula and its separate lower label; two prose baselines above (75) plus two interlinear additions; two rows in (75); one line beginning les cas nouveaux; eight main baselines of the final paragraph plus its inserted qualifier; three baselines in the rotated upper-left note including inserted hat-M_G; two in the slanted note beside (75); and two separate numbers, author\'s ink 29 and lighter pencil 59. Array indices and accents are read as part of their rows, not counted as extra text lines.',
'Every C insertion/deletion was checked on the native halves and its crop: initial marginal deletion and hat-M_G insertion; all three cancelled formula groups in (74); cancelled item after NB; opère replaced by s\'envoie; hat-M_G above modulaires; qui sont replaced by ils sont deux; and discrets (i.e. dans le contexte analytique). The line across the t in élémentaires is part of the letter, not an extra deletion.',
'18 original places were cropped exactly once, with autocontrast, LANCZOS enlargement to 2600 pixels wide and modest sharpening; all 18 were viewed. The upper-left note was rotated -90 degrees and the slanted note -35 degrees. No OCR, internet research or TeX compilation was used.',
'Only M1033 from the supplied MARKS table appears in decisions. Other unresolved cancelled material is recorded in doubts. The H notes identifying the author\'s page and commenting on repetitions/cancellations are editorial and have not been transcribed as ink.',
'The exact first readings in second_boxes contain TeX for whole formulas, including the cancelled row-3 product and all proposed index ink. The large (74) formula box includes the physically adjacent page number 29. The files are a proposed reader return for parent review, not final pages.'
],
check_events=[dict(statement_id='147-060-N1',date='2026-11-20 21:12:39 UTC',who='reader_c; GPT-6 Astra Pro; effort not separately exposed',type='carried as background without fault found',outcome='Used the visible pairing of two four-index factors and S_8 to locate the live union subscript and the lower product label. Did not independently prove the classification of dimension-2 cases, the Gamma actions, the semidirect-product claim, or the final expectation about fundamental groups. The interpretation did not supply the absent closing parenthesis or resolve the obscured cancelled index.')],
notation=[
 dict(sign=r'\Pi_1',reading='capital Pi with subscript 1',evidence='Long straight top bar over two tall separate uprights, crop place13.',scope='Last paragraph; a capital letter is preserved despite C\'s lowercase pi.'),
 dict(sign=r'\widehat M^!',reading='hat-M with an exclamation superscript',evidence='Each M roof is separate from the raised upright and detached dot at its right. Checked throughout both numbered displays and the inline formulas.',scope='All displayed and inline modular-multiplicity symbols on scan 60.'),
 dict(sign=r'\Gamma\text{---}',reading='Gamma followed by a repetition/ditto line in the action-text column',evidence='Row 2 has a continuous low horizontal stroke; rows 3 and 4 use separate short dashes at the same position.',scope='Rows 2–4 of (74); not expanded into opère via.'),
 dict(sign=r'\mathbf Z/2\mathbin{\cdot}(\mathfrak S_4\times\mathfrak S_4)',reading='Z/2, a centred dot, and the parenthesized product',evidence='The dot is separate from the two Z strokes and from the parenthesis; a slash followed by 2 is written. The lower words say prod. 1/2 direct without a brace.',scope='Unnumbered display below NB. The integer-Z font convention alone is not counted as a witness reading difference.'),
 dict(sign=r'\bigl(',reading='visible unmatched opening parenthesis',evidence='A long curve precedes the first live hat-I in row 3; no matching curve follows alpha_1.',scope='Live S subscript in row 3 of (74).'),
 dict(sign=r'\widehat M_G',reading='hat, not tilde, above M; capital G subscript',evidence='Pointed roofs and curved insertion guides are separate ink strokes in both interlinear occurrences.',scope='Rotated upper-left note and prose above (75).')],
hand_log=[
 dict(habit='A capital Pi is drawn with a broad straight top and two long independent legs.',pages=[60],all_occurrences='One clear live Pi in the last paragraph; a possibly related product form appears under heavy cancellation in (74). The cancelled form is not treated as fully resolved from the live one.',witness_misreadings='C reads lowercase pi_1 at the live occurrence; corrected to capital Pi_1.'),
 dict(habit='Repeated action wording can be indicated by one continuous horizontal line or a series of short dashes.',pages=[60],all_occurrences='All three repetitions in rows 2–4 of (74) checked. Their different ink segmentation is noted; no words are inserted.',witness_misreadings='C doubts the row-2 line; resolved as a repetition stroke, consistent with the lower two rows.'),
 dict(habit='Final low cursive letter groups can end in one short hook without separating every letter.',pages=[60],all_occurrences='Checked the contested de/dans, tous/tout, des/de and donnerait/donnera groups. The first two are proposed as de and tous; the latter two remain doubtful.',witness_misreadings='H reads dans and tout where the inspected groups support C\'s de and tous; the other differences stay open.'),
 dict(habit='An insertion guide can arch around a small formula and resemble its decoration if read without orientation.',pages=[60],all_occurrences='Both inserted hat-M_G groups checked with the surrounding words and the guide endpoints.',witness_misreadings='H reads the rotated formula as tilde-M_G and places it after dimension 2; the pointed hat and guide support C\'s reading and position.'),
 dict(habit='The terminal abbreviation trivialt stops before the letters ement.',pages=[60],all_occurrences='One abbreviated occurrence in (75); the full trivialement in (74) was read separately for comparison.',witness_misreadings='H expands the abbreviated lower-row word to trivialement.'),
 dict(habit='High paired quotation marks are distinct from guillemets and may occur in an unmatched sequence.',pages=[60],all_occurrences='Three groups in les cas nouveaux and two around élémentaires checked. The direction of the extra middle group remains uncertain.',witness_misreadings='Both C and H omit the middle group between cas and nouveaux; H changes the outer groups to guillemets.')],
abbreviations=[dict(written='dim',expansion='dimension'),dict(written='dim.',expansion='dimensions, in the phrase dim. modulaires'),dict(written='NB',expansion='nota bene'),dict(written='prod.',expansion='produit'),dict(written='1/2 direct',expansion='semi-direct, as the author\'s label; the written numeric form is retained'),dict(written='trivialt',expansion='trivialement'),dict(written='i.e.',expansion='id est')],
second_boxes=second,
unresolved=[
'Initial deleted marginal word remains illegible.',
'Cancelled product in (74): likely product sign, but complete lower index is not certified.',
'Small cancelled hat-I and cancelled 4/* in (74) remain doubtful.',
'Cancelled item after NB and cancelled qui sont remain doubtful.',
'Far-right dark tick after the unnumbered formula may be punctuation but is not transcribed as a certain stop.',
'Extra quotation group between cas and nouveaux is present, with opening/closing direction uncertain.',
'Final paragraph des/de and donnerait/donnera remain unresolved.'
],
witness_comparison='C is substantially closer in the central prose (par rapport aux schémas modulaires and ils sont deux), preserves the abbreviation trivialt, the exclamation in the slanted note and more of the cancelled material. H correctly preserves capital Pi_1. Both add an uninked underbrace and omit the middle quotation group below (75). C\'s row-3 cancelled S is less consistent with the surviving top bar and uprights than a doubtful product, and C supplies a closing parenthesis not visible in the live subscript. The final tense and the des/de ending remain open instead of being settled from either witness.')
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
# Structural checks, not compilation.
assert [d['id'] for d in decisions]==['M1033']
assert len(list((work/'crops').glob('147_scan060_place*.png')))==18
assert all((work/'crops'/c['crop']).is_file() for c in changes)
assert all(i['transcribed']=='yes' for i in inventory)
assert r'\margin{59}' in s and r'\mspage{29}' in s
assert r'\underbrace' not in s and r'\pi_1' not in s
assert len(re.findall(r'\\inserted\{',s))==5
assert len(re.findall(r'\\deleted\{',s))==7
print('Wrote',out/'proposed.tex')
print('Wrote',out/'report.json')
print('Counts:',report['physical_lines_read'],'physical lines;',len(changes),'change rows;',len(decisions),'MARK decision;',len(inventory),'inventory elements;',len(second),'second boxes; 18 crops.')
