from pathlib import Path
import json

base=Path('out/readers/H162-01_162-1_scan004/R2')
C=Path('packets/H162-01_162-1_scan004/C.tex').read_text(encoding='utf-8')
H=Path('packets/H162-01_162-1_scan004/H.tex').read_text(encoding='utf-8')
R=(base/'reading.tex').read_text(encoding='utf-8')

def line(text,start):
    return next(x for x in text.splitlines() if x.startswith(start))
def block(text,start,end):
    a=text.index(start)
    b=text.index(end,a)+len(end)
    return text[a:b]
def rl(start): return line(R,start)
def cl(start): return line(C,start)
def hs(start,end='}'):
    return block(H,start,end)

crop_boxes={
1:[735,35,1150,139],2:[525,178,875,242],3:[501,450,946,520],4:[506,520,889,575],5:[511,633,861,686],6:[932,686,1229,752],7:[520,748,1223,805],8:[519,807,855,875],9:[692,876,812,930],10:[1126,907,1398,974],11:[232,992,1108,1083],12:[233,1057,455,1165],13:[525,1089,901,1173],14:[1438,1070,1620,1126],15:[1126,1121,1329,1194],16:[521,1171,1212,1249],17:[515,1234,613,1275],18:[544,1251,954,1313],19:[925,1224,1301,1289],20:[540,1374,1410,1476],21:[550,1547,760,1611]}
crop_names={1:'01_mumford',2:'02_artin',3:'03_monsky',4:'04_lettres_hartshorne',5:'05_lettres_quillen',6:'06_infinitesimales',7:'07_cancelled_notes',8:'08_r_wood',9:'09_cot_mark',10:'10_pour_omega_tail',11:'11_borel_separator',12:'12_deligne',13:'13_serre_coh',14:'14_p_relation',15:'15_monodromy_tail',16:'16_letter',17:'17_qui',18:'18_weil_jacobiennes',19:'19_intermediaires',20:'20_lichtenbaum',21:'21_harder'}
def cp(n):
    return None if n is None else f'readers/H162-01_162-1_scan004/R2/crops/{crop_names[n]}.jpg'

differences=[]
def d(place,c,h,reading,evidence,kind='other',confidence='high',marked=False,cc=False,hc=True,n=None,bbox=None):
    differences.append(dict(id=f'R2-D{len(differences)+1:02d}',place=place,C=c,H=h,reading=reading,evidence=evidence,confidence=confidence,kind=kind,marked_in_H=marked,c_changed=cc,h_changed=hc,crop=cp(n),bbox=bbox if bbox is not None else crop_boxes[n],bbox_source='whole image, 1681 x 2138 pixels'))

# Raynaud and upper Illusie entries.
d('Raynaud entry, stop after Mumford','Mumford .','Mumford,','Mumford .','The half and crop show one low detached point after Mumford, without a descending comma tail. This is an internal entry stop, not one of H\'s editorial list-joining semicolons.','misread symbol or index',n=1,bbox=[744,106,764,123])
d('Raynaud entry, word after Theta',r'\unsure{function|fonction}','foundations',r'f\unsure{o|u}nction','After the tall f the first small body is a closed or nearly closed loop; o is preferred, but the thick junction admits u. The remaining compact nction does not supply the extra d/a/t sequence of foundations. The doubt is localized to the first vowel.','misread word','medium',cc=True,n=1,bbox=[814,65,1004,132])
d('Raynaud entry, I enclosure and I/II head and foot rules',r'\textcircled{\scriptsize $\overline{\underline{\mathrm I}}$}, $\overline{\underline{\mathrm{II}}}$',r'\add{I}, II','\n'.join([rl(r'\node at (1047'),rl(r'\draw[line width=.35pt] (1082'),rl(r'\node at (1084'),rl(r'\node at (1098')]),'I has separate head and foot strokes inside a tall tilted enclosure whose two upper ends do not close. II has common upper and lower rules. There is no insertion caret at I. C\'s circular enclosure is replaced by the observed open-ended contour; H omits the enclosure and rules and calls I an addition.','drawing or diagram','high',cc=True,n=1,bbox=[1024,35,1142,138])
d('Raynaud, Artin-Winters',r'\unsure{Artin}-Winters','Artin--Winters',r'\unsure{Artin}-Winters','A and final n are visible; the retraced r/t/i cluster has overlapping tall strokes. Artin remains a candidate rather than an unmarked name. Winters is read from its separate W, low i/n, tall t, looped e and final r/s.','other','medium',n=2)
d('Illusie, first Monsky-Washnitzer',r'\unsure{Monsky-Washnitzer}','Monsky--Washnitzer',r'\unsure{Monsky-Washnitzer}','The M, low onsk, descending y, hyphen, W, tall h and final t/z/e/r contours are visible. The filled first vowel and pale joined middle of the second name still prevent an unqualified reading; C\'s local uncertainty is retained.','other','medium',n=3,bbox=[504,461,851,514])
d('Illusie, Roman I and II rules',r'$\overline{\underline{\mathrm{I}}},\overline{\underline{\mathrm{II}}}$','I, II',r'$\overline{\underline{\mathrm I}},\overline{\underline{\mathrm{II}}}$','Each numeral has a detached upper rule and a lower foot rule; the second has two uprights. The comma is a separate descending stroke. These graphic rules are retained against H\'s bare numerals.','drawing or diagram',n=3,bbox=[863,462,941,508])
d('Illusie, letters to Hartshorne',r'\unsure{lettres|lettre}','Lettres Hartshorne','lettres Hartshorne','The final short r/e movement is followed by an additional long terminal s stroke with a downturned right end. The first letter is a slanted lower-case l form, unlike the square-footed L of the later entry. C\'s number doubt is removed.','misread word','medium',cc=True,n=4)
d('Illusie, diagonal before letters to Hartshorne',r'/\quad \unsure{lettres|lettre} Hartshorne','',rl(r'\draw[line width=.3pt] (455'),'Half a shows a single unheaded diagonal running from below-left toward the beginning of lettres, not a short baseline slash. H has no corresponding mark.','insertion or placement',cc=True,n=None,bbox=[452,549,510,612])
d('Illusie, letters to Quillen',r'\unsure{Lettres|Lettre}','Lettre Quillen','Lettres Quillen','There are two tall crossed t strokes, a low r/e movement and a further terminal s-like horizontal with a downturned end. The entry is read as plural Lettres; the initial L has a square foot.','misread word','medium',cc=True,n=5)
d('Illusie, second diagonal',r'/\quad \unsure{Lettres|Lettre} Quillen','',rl(r'\draw[line width=.3pt] (454'),'Half a shows a separate unheaded diagonal rising from the left of the following Notes line toward Lettres. Its observed lower position is retained. H does not transcribe it.','insertion or placement',cc=True,n=None,bbox=[451,676,514,736])
d('Illusie, infinitesimal extensions',r'\unsure{infinitésimales}','infinitésimales','infinitésimales','The crop separates the long f, the small i marks, tall t, accented low e, later i, and final m/a/l/e/s run. The accent is a small mark above the e, distinct from the following i dot. C\'s word doubt is removed.','other','medium',cc=True,hc=False,n=6)

# Cancelled Notes and remaining Illusie group.
d('Cancelled Notes, first vowel and last vowel of tapis',r'\unsure{tapis|topis|topos}','tapis',r't\unsure{a|o}pis','The tall t, descended p, detached i dot and final s survive. The first vowel is covered by the horizontal strike and remains a/o; the separate i dot favors i rather than the final o proposed in topos.','other','medium',cc=True,n=7,bbox=[726,750,820,798])
d('Cancelled Notes, parenthetical word and Quillen placement',r'(\unsure{pluriel|Gabriel}) Quillen','(Quillen)','(pluriel) Quillen','Within the parentheses are a descended p, tall looped l, low u/r, i dot, faint e and final l; pluriel is preferred without the Gabriel alternative. Quillen is to the right of the closing parenthesis. H places Quillen inside parentheses and omits the intervening word.','omission','medium',cc=True,n=7,bbox=[848,748,1216,802])
d('Cancelled Notes, long cancellation geometry',cl(r'\deleted{Notes sur'),hs(r'\struck{Notes sur'),rl(r'\draw[line width=.65pt] (527'),'One continuous nearly horizontal dark stroke crosses the complete entry, including its internal spaces, and projects beyond the terminal word. Both witnesses encode deletion state, but neither gives this physical extent. The added drawing is not a claim that either witness left the words live.','drawing or diagram',cc=True,n=7,bbox=[525,765,1215,787])
d('Bourbaki entry, R. Wood and following gap','Rapport Bourbaki','R. Wood à Bourbaki,','R. Wood Bourbaki','A large R is followed by a separate stop, then a W, two small rounded/open bodies, and a tall final d. The blank before Bourbaki contains no à. No comma appears after Bourbaki in half a.','misread word','high',cc=True,n=8)
d('Complexe cot and its small lower mark',r'cot$_{\unsure{*|+}}$','cotangent',r'cot$_{\unsure{*|+}}$','The written form is c-o-t followed by a compact lower intersecting mark. A vertical part, side arms and a dark oblique edge permit star or plus; the source does not spell out cotangent.','abbreviation expanded or spelling modernised','medium',n=9)
d('Atiyah entry, capital L',"L'extension","l'extension","L'extension",'Half a shows a tall upright with a broad lower horizontal foot, followed by the apostrophe. The source capital is retained.','misread word',n=None,bbox=[754,923,947,971])
d('Atiyah entry, pour',r'\unsure{pour|par}','pour','pour','The crop shows p, a separate small rounded o, then a low u movement and terminal r. Four letter positions are visible; par does not account for the intervening movement.','other','high',cc=True,hc=False,n=10,bbox=[1131,929,1211,967])
d('Atiyah entry, terminal marks',r'\unsure{..---|\ldots}',"\\ill\\",'\n'.join([rl(r'\draw[line width=.45pt] (1332'),rl(r'\fill (1351'),rl(r'\draw[line width=.25pt] (1368'),rl(r'\fill (1389')]),'There are two separate short marks and a much longer pale curved terminal stroke ending in a darker point. The literal three-part graphic replaces the uncertainty between a dash-ending and an ellipsis. H\'s ill is the local unread span immediately after Omega^1.','readable ink left as \\ill{}','high',marked=True,cc=True,n=10,bbox=[1327,939,1396,956])
d('Koszul entry, separator','Koszul\\quad 2 articles','Koszul, 2 articles','Koszul\\quad 2 articles','Half a has a blank gap between Koszul and the numeral 2, without a comma. This reports the within-entry punctuation only; H\'s semicolons between entries are treated as editorial list joining.','text not on the page',n=None,bbox=[533,973,915,1011])
d('Cancelled Borel, uncertainty',r'\unsure{Borel}','Borel','Borel','The crop gives the initial B body, low o, short r, e movement and final tall l despite the strike. C\'s whole-name doubt is removed.','other','medium',cc=True,hc=False,n=11,bbox=[529,1002,634,1045])
d('Cancelled Borel, title and punctuation',r'\qquad Lecture Notes',': lettre, notes','Lecture Notes','The first word starts with a tall L and continues e/c/t/u/r/e; the second begins with capital N. A broad gap, not a colon, separates Borel from this title. The source does not read lettre, notes.','misread word',n=11,bbox=[638,994,1018,1037])
d('Borel and Lecture Notes, separate cancellation runs and lower trace',cl(r'\deleted{\unsure{Borel}'),hs(r'\struck{Borel'), '\n'.join([rl(r'\draw[line width=.65pt] (535,1032)'),rl(r'\draw[line width=.65pt] (688'),rl(r'\node[anchor=center] at (556')]),'A short cancellation crosses Borel and a separate much longer one crosses Lecture Notes, leaving a gap between them. A lower oblique trace at Borel is also drawn with local doubt about its affiliation to the writing or cancellation. Both witnesses already mark the words deleted.','drawing or diagram','medium',cc=True,n=11,bbox=[530,997,1019,1046])
d('Divider above Deligne',block(C,r'\figure{\begin{tikzpicture}',r'\end{tikzpicture}}'),'','\n'.join([rl(r'\draw[line width=.25pt] (244'),rl(r'\draw[line width=.25pt] (735')]),'Two thin rising strokes are separated by a small gap near x=713–735. C already records two strokes; its equivalent drawing is retained in the page layout. H omits this divider.','drawing or diagram',cc=False,n=11,bbox=[240,1026,1100,1079])

# Deligne heading and Serre entry.
d('Deligne, small mark after heading',r'\unsure{1|2|?}','',r'\unsure{1|2|?}','The compact dark mark has a hooked upper-left part and a near-vertical lower stroke with a small loop. Retracing prevents a decision among 1, 2 and ?. The appended C note about ? is included here. H has no corresponding numeral/mark; its nearby suite is a different locus.','omission','low',n=12,bbox=[400,1065,433,1115])
d('Deligne, cancelled lower parenthesis',r'\deleted{(\unsure{suite|suiten})}',r'\emph{(suite)}',r'\deleted{(\unsure{suite|suiten})}','The parenthetical note is below the left-hand heading and visibly crossed by oblique hatching. The tall t and terminal loop support suite, but covered final strokes leave suiten possible. H gives suite live and places it inline with the heading.','deletion state (struck given live or live given struck)','medium',n=12,bbox=[238,1122,378,1166])
d('Deligne, hatching over the lower parenthesis',r'\deleted{(\unsure{suite|suiten})}',r'\emph{(suite)}',block(R,r'\node[anchor=north west] at (244,1127)',r'\end{tikzpicture}}};'),'The note carries a repeated oblique hatch run beyond a simple text strike. The drawing preserves six schematic diagonal portions and a short terminal return; overlaps leave the original pen-lift boundaries uncertain, so the graphic itself is locally marked doubtful. Neither witness depicts this hatching.','drawing or diagram','medium',cc=True,n=12,bbox=[242,1125,377,1166])
d('Serre, double underline',r'\uuline{Serre}','Serre',r'\uuline{Serre}','Two separate pale lower rules lie under Serre, below the dark cancellation. H\'s plain name lacks them.','omission',n=13,bbox=[539,1144,630,1166])
d('Serre, separator after the name',':',':',r'\unsure{:|.}','One low detached point is certain. A possible upper point lies on the cancellation and cannot be distinguished from it. The colon is preferred but a single stop remains possible; this doubt does not extend to Serre.','other','low',cc=True,n=13,bbox=[637,1119,656,1147])
d('Serre, Ch. abbreviation',r'\unsure{Coh.|Ch.}','cohomologie','Ch.','The open C joins a tall looped h; there is no independent closed o between them. A separate stop follows h. H expands the abbreviation, while C\'s Coh. first candidate is rejected in favor of Ch.','abbreviation expanded or spelling modernised','medium',cc=True,n=13,bbox=[675,1103,749,1142])
d('Serre, Vect. wording','Vect.','des vecteurs de','Vect.','The half and crop give a large V followed by low e/c, a crossed t and a separate stop. No des or de is written on either side of this abbreviation before Witt.','abbreviation expanded or spelling modernised',n=13,bbox=[759,1100,845,1138])
d('Serre, var. abeliennes','var. abéliennes','von Dieudonné','var. abéliennes','Half b shows the compact v/a/r and stop, then a/b, the high accent, l/i/e/n/n/e/s. These are the words between et and en car; H\'s von Dieudonné does not match those contours.','misread word','medium',n=None,bbox=[1055,1075,1349,1127])
d('Serre, car abbreviation','en car','en caractéristique','en car','Half b shows en followed by only c-a-r before p, with no further letter run and no abbreviation stop.','abbreviation expanded or spelling modernised',n=None,bbox=[1358,1078,1512,1117])
d('Serre, relation and zero',r'$p\unsure{\ne|>}0$',r'$p$',r'$p\unsure{\ne|>}0$.','The p has a descending loop, the following intersected/angular mark is partly buried under the strike, and a small closed oval zero plus a separate stop follow it. The relation remains ne/>. H stops at p and has no unread marker at this source locus.','omission','low',n=14,bbox=[1510,1075,1612,1124])
d('Serre, cancellation extent',cl(r'\deleted{\uuline{Serre}'),hs(r'\struck{Serre'),rl(r'\draw[line width=.6pt] (531'),'A continuous slightly rising dark line begins at Serre and crosses the whole title through the final mathematical condition. The physical course is added; both witnesses already give deletion state.','drawing or diagram',cc=True,n=None,bbox=[527,1089,1603,1148])

# Quoted title and cancelled letter.
d('Griffiths, quotation marks',"``On monodromy \\unsure{....|\\ldots}''",'« On monodromy \\ldots »',"``On monodromy ....''",'Half b shows paired opening pen hooks, and crop 15 shows two separate raised closing hooks. They are doubled quotation strokes, not angular guillemets. The two ends retain their differing physical heights in the layout.','misread symbol or index',n=15,bbox=[864,1128,1320,1190])
d('Griffiths, four terminal points',r'\unsure{....|\ldots}',r'\ldots','....','Four detached marks are visible: a small horizontal first mark, two compact middle points and an elongated fourth point. They are counted rather than normalized to a three-point ellipsis.','other','high',cc=True,n=15,bbox=[1218,1149,1266,1171])
d('Detached right-side point below the Serre ending','','',rl(r'\node[anchor=center] at (1608'),'Half b shows a small isolated dark point at x=1608, y=1156, well below the Serre stop and to the right of the title. It is preserved with uncertainty about intentional ink versus a surface speck, without assigning it to either phrase.','drawing or diagram','low',cc=True,n=None,bbox=[1604,1152,1613,1161])
d('Cancelled letter, surname after Lettre',r'\unsure{Rietzly|Rietzley}',"\\ill\\",r'\unsure{Rietzly|Rietzley}','R, i, e, a tall t and the final l/y-like movement survive, but the cancellation and a descender from Griffiths cross the central letters. Rietzly/Rietzley remains tentative. H\'s quoted ill is the undivided unread name span between Lettre and chapitre; it is not treated as definite absence of this name.','readable ink left as \\ill{}','low',marked=True,n=16,bbox=[664,1184,805,1246])
d('Cancelled letter, Chapin','Chapin','chapitre','Chapin','The crop gives a capital C, tall h, small a, descending p, dotted i and terminal n, followed by a comma. No t/r/e continuation is present. H\'s earlier ill belongs to the preceding name and does not mark this word doubtful.','misread word','high',n=16,bbox=[831,1187,966,1231])
d('Cancelled letter, class field thy',r'\unsure{class} field th\unsure{y|.}','de\nfamilles',r'\unsure{class} field thy','The first c/l is visible but the following low letters of class are covered, so its doubt remains. A long looped f and the field sequence follow. The final y descends separately from the long horizontal cancellation and is not a stop. H\'s plain de familles corresponds to this whole tail; its earlier ill does not mark the class/thy locus.','misread word','medium',cc=True,n=16,bbox=[970,1170,1205,1223])
d('Cancelled letter, wavy underline position',r'\uwave{\unsure{Rietzly|Rietzley} Chapin}',"\\ill\\ chapitre",rl(r'\draw[line width=.25pt] (698'),'The thin wavy stroke starts under the middle of the first name, not at the R, and continues under Chapin. C records waviness but its wrapper starts the underline before the full first name. H has no corresponding graphic; the ill in the quotation marks a name, not uncertainty about an underline.','insertion or placement','high',marked=False,cc=True,n=16,bbox=[694,1218,936,1250])
d('Cancelled letter, long rising strike',cl(r'\deleted{Lettre'),hs(r'\struck{Lettre'),rl(r'\draw[line width=.65pt] (535,1227)'),'The dark cancellation rises across the complete entry and continues to the right of thy. It is separate from the lower thin wavy underline. Both witnesses encode deletion, but the two distinct graphic paths require preservation.','drawing or diagram',cc=True,n=16,bbox=[531,1181,1202,1233])
d('Short cancelled start between letter and Weil',r'\deleted{\unsure{Qui|Que}}','',r'\deleted{\unsure{Que|Qui}}','Below Lettre is a separate short crossed start. The final low loop favors e; no secure detached i dot is visible. Que/Qui remains open. H has no separately corresponding text between its letter entry and Work entry; its ill within the earlier letter covers the earlier name span.','omission','low',cc=True,n=17)

# Lower cancelled entries.
d('Weil entry, author and separator','Weil :','Work,','Weil :','The crop shows the two open strokes of W, low e, short i and tall looped l. The following upper dark point at the strike and lower detached point support a colon. Work and a comma do not match.','misread word',n=18,bbox=[547,1256,671,1305])
d('Weil entry, final word',r'\unsure{intermédiaires}',"\\ill\\",r'\unsure{intermédiaires}','The long word retains its tall t/d, several dotted short letters and final -aires-like movement, but the strike conceals much of the low middle and the exact accented vowel. The candidate intermédiaires remains doubtful. H\'s ill immediately after Jacobiennes is the unread continuation span; no claim is made that H explicitly names a different word there.','readable ink left as \\ill{}','low',marked=True,n=19)
d('Weil entry, deletion state of the unread tail',cl(r'\deleted{Weil'),"\\struck{Work, Jacobiennes} \\ill\\",rl(r'\node at (958,1274)'),'The cancellation visibly continues through the whole final word. H closes its struck wrapper after Jacobiennes and leaves the following ill outside it. The chosen tentative word remains deleted.','deletion state (struck given live or live given struck)','high',marked=True,n=19)
d('Weil entry, long curved cancellation',cl(r'\deleted{Weil'),"\\struck{Work, Jacobiennes} \\ill\\",rl(r'\draw[line width=.8pt] (563,1287)'),'One broad line crosses Weil and Jacobiennes, briefly flattens across the middle of the last word, then rises toward the right end. The explicit path preserves that course. The graphic difference itself is not an H doubt marker.','drawing or diagram','high',marked=False,cc=True,n=None,bbox=[559,1238,1289,1296])
d('Papiers d Artin, two rules under 13',r'(\uuline{13})','(13)',r'(\uuline{13})','Half b shows 1 followed by 3 within parentheses and two separate short rules below the numeral. H gives the numeral without these rules.','omission',n=None,bbox=[882,1315,995,1381])
d('Papiers d Artin, two parallel cancellation strokes',cl(r"\deleted{Papiers d'Artin"),hs(r"\struck{Papiers d'Artin"),'\n'.join([rl(r'\draw[line width=.5pt] (548,1368)'),rl(r'\draw[line width=.5pt] (548,1375)')]),'Half b distinguishes two long near-parallel rising cancellation strokes through this entry, separately from the two short underline rules beneath 13. Both long paths are drawn. The witnesses\' single deletion wrappers encode the state without the doubled geometry.','drawing or diagram',cc=True,n=None,bbox=[542,1331,986,1381])
d('Lichtenbaum entry, author','Lichtenbaum','bibliothèque','Lichtenbaum','The crop shows initial L, the dotted i, c/h/t cluster, e/n, tall b and the low a/u/m termination. The lower-case bibliothèque supplied by H has neither the initial nor terminal contours of the name.','misread word',n=20,bbox=[545,1410,823,1459])
d('Lichtenbaum entry, surfaces','surfaces',"\\ill\\",'surfaces','A short s/u/r run is followed by the very long descending f and low a/c/e/s. H\'s ill between bibliothèque and arithmétiques is the unread span corresponding to this word.','readable ink left as \\ill{}','high',marked=True,n=20,bbox=[866,1405,1044,1469])
d('Lichtenbaum entry, arithmetiques uncertainty',r'\unsure{arithmétiques}','arithmétiques',r'\unsure{arithmétiques}','The tall stems, long q descender and final u/e/s support the candidate, but the grey strike obscures the middle low letters and the precise accent. C\'s doubt is retained. H prints this word unmarked; its preceding ill applies to surfaces, not this adjective.','other','medium',marked=False,n=20,bbox=[1079,1379,1394,1456])
d('Lichtenbaum entry, cancellation extent',cl(r'\deleted{Lichtenbaum'),hs(r'\struck{bibliothèque'),rl(r'\draw[line width=.8pt] (555,1440)'),'A broad grey line crosses the entire entry, rises across arithmétiques and extends just beyond its last letters. The explicit curve preserves the separate cancellation ink while retaining both witnesses\' deleted state.','drawing or diagram',cc=True,n=20,bbox=[548,1386,1393,1450])
d('Manin entry, cancellation course',cl(r'\deleted{Manin'),hs(r'\struck{Manin'),rl(r'\draw[line width=.8pt] (551,1511)'),'Half b shows one long pale broad cancellation beginning low across Manin, then rising through variétés rationnelles and the parenthetical 2 articles. The agreement text was read from the ink, including both accents and the numeral 2. The explicit source path supplements the deletion state.','drawing or diagram',cc=True,n=None,bbox=[546,1454,1422,1520])
d('Harder entry, name and comma',r'\unsure{Harder|Hardy}',"\\ill\\",'Harder,','The crop shows H, a closed a, short r, tall looped d, a low e movement, then a short r before a distinct descending comma. The last descent is separated from the name rather than being a y. H\'s ill is the local unread author span before sur conjecture de Weil.','readable ink left as \\ill{}','medium',marked=True,cc=True,n=21,bbox=[550,1547,699,1608])
d('Harder entry, extended cancellation',cl(r'\deleted{\unsure{Harder'),hs(r'\struck{\ill\ sur conjecture'),rl(r'\draw[line width=.65pt] (563,1587)'),'Half b shows a continuous dark line across the entry, rising through the last words and continuing far to the right of Weil before turning slightly down. Both witnesses already mark deletion; the source extension is separately drawn.','drawing or diagram',cc=True,n=None,bbox=[555,1543,1322,1600])
d('Isolated lower-left point','','',rl(r'\node[anchor=center] at (245,1763)'),'The whole page and half b show a conspicuous isolated dark point below the list near the left column. It is preserved as a locally uncertain graphic, without assigning character value or intention.','drawing or diagram','low',cc=True,n=None,bbox=[240,1758,252,1769])

c_doubts=[]
def q(place,c,decision,evidence,confidence='medium',n=None,bbox=None):
    c_doubts.append(dict(place=place,C=c,decision=decision,evidence=evidence,confidence=confidence,crop=cp(n),bbox=bbox if bbox is not None else crop_boxes[n],bbox_source='whole image, 1681 x 2138 pixels'))
q('Theta at Raynaud entry',r'$\Theta$',r'$\Theta$ retained','The circular body has a separate transverse median bar.','high',1,[770,76,809,113])
q('Roman numerals in the two first title entries',r'\textcircled{\scriptsize $\overline{\underline{\mathrm I}}$}, $\overline{\underline{\mathrm{II}}}$','I and II with head/foot rules retained; top I enclosure drawn as a tall open-ended loop','The top I has one upright and two rules within the loop; II has two uprights. The first Illusie pair independently has the same numeral counts and rules.','high',1,[1024,35,1142,138])
q('Two left diagonals before letter entries','/','Retained as two long unheaded diagonal paths at the observed lower-left positions','Both strokes were visible in half a; neither has an arrowhead.','high',None,[450,548,515,736])
q('Atiyah formula',r'$\Omega^{1}$',r'$\Omega^{1}$ retained','An open-bottom capital with two low feet is followed by a distinctly raised hooked 1 with a foot.','high',10,[1237,908,1320,957])
q('Griffiths quotation strokes',"``On monodromy \\unsure{....|\\ldots}''",'Doubled opening and closing pen quotation strokes retained','Half b gives the opening pair and crop 15 gives two raised closing hooks, rather than guillemets.','high',15,[864,1128,1320,1190])
q('Papiers d Artin, 13 rules',r'(\uuline{13})',r'(\uuline{13}) retained','Half b shows a single stem 1, a two-lobed 3, and two short lower rules inside the parenthetical entry.','high',None,[882,1315,995,1381])
q('Raynaud, function/fonction',r'\unsure{function|fonction}',r'f\unsure{o|u}nction','The first small vowel body is nearly closed, so o is first; thickness still admits u. The doubt is localized.', 'medium',1,[814,65,1004,132])
q('Artin-Winters',r'\unsure{Artin}',r'\unsure{Artin} retained','The dark retraced r/t/i cluster cannot be separated completely; the initial A and final n are secure.', 'medium',2)
q('First Monsky-Washnitzer',r'\unsure{Monsky-Washnitzer}',r'\unsure{Monsky-Washnitzer} retained','The filled vowel following W and pale joined middle prevent an unqualified whole-name reading.', 'medium',3,[504,461,851,514])
q('Letters Hartshorne',r'\unsure{lettres|lettre}','lettres','A further terminal s-shaped stroke follows the r/e movement.', 'medium',4)
q('Letters Quillen',r'\unsure{Lettres|Lettre}','Lettres','The final extended terminal with downturned end follows the r/e movement, supporting the plural.', 'medium',5)
q('Infinitesimal extensions',r'\unsure{infinitésimales}','infinitésimales','The individual tall stems, short letter marks, accent and final -males run can be followed in the crop.', 'medium',6)
q('Cancelled Notes, tapis/topis/topos',r'\unsure{tapis|topis|topos}',r't\unsure{a|o}pis','The first vowel is hidden; p descender, i dot and final s remain visible. The last-vowel o candidate is rejected.', 'medium',7,[726,750,820,798])
q('Cancelled Notes, parenthetical word',r'\unsure{pluriel|Gabriel}','pluriel','Descended p, tall l, low u/r, i dot, faint e and final l fit the seven letters. The Gabriel initial and inner b are absent.', 'medium',7,[848,748,1005,802])
q('Complexe cot, lower mark',r'\unsure{*|+}',r'\unsure{*|+} retained','A lower vertical component, side arms and dark oblique edge do not settle star versus plus.', 'medium',9)
q('Atiyah, pour/par',r'\unsure{pour|par}','pour','A separate o and following u movement occur between p and r.', 'high',10,[1131,929,1211,967])
q('Atiyah, trailing punctuation',r'\unsure{..---|\ldots}','Literal two short marks followed by one longer curved stroke','The last trace is much longer than either first mark and ends in a darker point; it is drawn rather than normalized to dots.', 'high',10,[1327,939,1396,956])
q('Borel',r'\unsure{Borel}','Borel','Initial B, low o/r/e and final l remain traceable across the strike.', 'medium',11,[529,1002,634,1045])
q('Mark beside Deligne, including appended question-mark note',r'\unsure{1|2|?}',r'\unsure{1|2|?} retained','The retraced hook, small loop and vertical stroke admit all three candidates. No new view was taken after the appended prior note.', 'low',12,[400,1065,433,1115])
q('Cancelled parenthesis below Deligne',r'\unsure{suite|suiten}',r'\unsure{suite|suiten} retained','The tall t and final loop support suite; cancellation and terminal hatching leave an additional n-like movement possible.', 'medium',12,[238,1122,378,1166])
q('Serre, Coh./Ch.',r'\unsure{Coh.|Ch.}','Ch.','The open C joins the tall h without a separate o body; the terminal stop is detached.', 'medium',13,[675,1103,749,1142])
q('Serre, p relation',r'\unsure{\ne|>}',r'\unsure{\ne|>} retained','The cancellation hides the upper portion of the angular/intersected sign. The zero and final stop are distinct and secure.', 'low',14,[1538,1077,1580,1121])
q('Griffiths, terminal points',r'\unsure{....|\ldots}','....','Four detached marks are countable in the crop.', 'high',15,[1218,1149,1266,1171])
q('Cancelled letter, first name',r'\unsure{Rietzly|Rietzley}',r'\unsure{Rietzly|Rietzley} retained','The strike and the preceding line\'s descender obscure the middle and the possible extra e; the initial and terminal movements survive.', 'low',16,[664,1184,805,1246])
q('Cancelled letter, class',r'\unsure{class}',r'\unsure{class} retained','The opening c/l is definite but the low a/s/s region is crossed by the strike.', 'low',16,[970,1181,1043,1218])
q('Cancelled letter, final y or stop',r'th\unsure{y|.}','thy','The final descent begins below the letter body and is separate from the continuing cancellation; it is too long and connected to be a stop.', 'medium',16,[1137,1172,1186,1212])
q('Short cancelled start',r'\unsure{Qui|Que}',r'\unsure{Que|Qui}','A low final loop favors e, while a secure separate i dot cannot be identified. Both alternatives remain.', 'low',17)
q('Weil, intermédiaires',r'\unsure{intermédiaires}',r'\unsure{intermédiaires} retained','The long cancellation covers low middle letters and leaves the exact accent uncertain; the tall stems and final -aires-like run support the tentative word.', 'low',19)
q('Lichtenbaum, arithmétiques',r'\unsure{arithmétiques}',r'\unsure{arithmétiques} retained','Several tall stems, the q descender and final letters survive, but the covered low middle and accent remain unresolved.', 'medium',20,[1079,1379,1394,1456])
q('Harder/Hardy',r'\unsure{Harder|Hardy}','Harder,','The low e and short r precede a separate descending comma; the descent is not a y attached to the word.', 'medium',21,[550,1547,699,1608])

inventory=[]
def inv(element,kind,bbox,first,hand='handwritten, blue/black ink with grey pencil-like strokes',extra=''):
    inventory.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,position={'bbox':bbox,'bbox_source':'whole image, 1681 x 2138 pixels','note':extra},first_words_or_objects=first,transcribed='yes'))
inv('Raynaud heading','text',[223,64,420,126],'Raynaud')
inv('Raynaud first title and numeral pair','text',[525,61,1141,139],'Mumford . Theta fonction/function I, II')
inv('Tall enclosure of first I','drawing',[1024,35,1092,138],'Open-ended tilted loop around I')
inv('Raynaud second entry','text',[530,130,806,180],'Papiers Kiehl')
inv('Raynaud third entry','text',[536,182,870,238],'Artin-Winters')
inv('Illusie heading and 1','text',[240,468,445,520],'Illusie 1')
inv('First Monsky-Washnitzer entry with I/II','text',[505,459,944,516],'Monsky-Washnitzer I, II')
inv('Hartshorne letter entry','text',[510,522,889,571],'lettres Hartshorne')
inv('First long slash','drawing',[451,548,512,613],'Unheaded diagonal',extra='Below-left of lettres; rises to its beginning')
inv('Hartshorne title entry','text',[517,573,1088,632],'Hartshorne : Affine duality')
inv('Quillen letter entry','text',[520,635,850,691],'Lettres Quillen')
inv('Second long slash','drawing',[450,675,515,738],'Unheaded diagonal',extra='Rises from left of Notes toward Lettres')
inv('Extensions entry','text',[522,685,1231,752],'Notes sur extensions infinitésimales')
inv('Cancelled Notes entry','deletion',[522,748,1223,805],'Notes sur tapis/topis (pluriel) Quillen')
inv('Long Notes cancellation','deletion',[524,765,1216,789],'Continuous dark strike through entire entry')
inv('Bourbaki entry','text',[525,807,1290,877],'R. Wood Bourbaki calcul différentiel')
inv('Complexe entry with lower mark','text',[516,872,1151,932],'Complexe cot with lower star/plus, relatif de Quillen')
inv('Atiyah entry and formula','text',[530,906,1322,979],"Notes sur L'extension d'Atiyah pour Omega^1")
inv('Atiyah terminal graphic','drawing',[1326,938,1397,958],'Two short marks and a longer curved terminal with attached dark endpoint')
inv('Koszul entry','text',[532,972,918,1016],'Koszul 2 articles')
inv('Cancelled Borel name','deletion',[529,1001,636,1048],'Borel')
inv('Cancelled Lecture Notes title','deletion',[686,992,1022,1040],'Lecture Notes')
inv('Separate Borel and Lecture Notes strikes','deletion',[532,1007,1020,1043],'Short name strike and separate long title strike')
inv('Borel lower oblique trace','drawing',[539,1012,581,1046],'Oblique lower trace',extra='Affiliation to letterform or cancellation is uncertain; locally marked')
inv('Two-part divider','drawing',[239,1025,1103,1081],'Two disconnected thin curved strokes')
inv('Deligne heading and doubtful adjacent mark','text',[235,1063,436,1127],'Deligne 1/2/?')
inv('Second Monsky-Washnitzer entry','text',[519,1048,920,1101],'Monsky-Washnitzer')
inv('Lower left cancelled parenthesis','deletion',[236,1120,381,1170],'(suite/suiten)',extra='Below Deligne; modest upward slant retained')
inv('Oblique hatching of lower parenthesis','deletion',[241,1124,380,1169],'Repeated hatch run and terminal return',extra='Six schematic diagonals and one return are drawn; original pen-lift boundaries remain uncertain')
inv('Cancelled Serre entry','deletion',[524,1073,1614,1153],'Serre :/. Ch. Vect. Witt et var. abéliennes en car p ne/> 0.')
inv('Two lower rules under Serre','drawing',[538,1142,634,1169],'Double underline below Serre')
inv('Serre long cancellation','deletion',[525,1087,1605,1150],'Continuous rising dark stroke across the title')
inv('Griffiths quoted title','text',[522,1126,1324,1210],'Preprint Griffiths : doubled quotes On monodromy four points',extra='Opening and closing quotes have their observed separate heights')
inv('Detached right-side point','drawing',[1603,1151,1614,1163],'Isolated point',extra='No attachment assigned; ink-versus-speck uncertainty retained')
inv('Cancelled letter entry','deletion',[525,1168,1208,1244],'Lettre Rietzly/Rietzley Chapin, class field thy')
inv('Letter long cancellation','deletion',[529,1180,1204,1235],'Rising dark strike through complete letter entry')
inv('Thin wavy underline below names','drawing',[693,1217,938,1252],'Wavy stroke beginning within first name and ending under Chapin')
inv('Short cancelled start','deletion',[519,1234,615,1278],'Que/Qui')
inv('Short-start cancellation','deletion',[528,1249,607,1270],'Short thick rising strike')
inv('Weil entry','deletion',[547,1232,1300,1314],'Weil : Jacobiennes intermédiaires.')
inv('Weil broad cancellation','deletion',[557,1236,1292,1300],'Broad line across the full entry, bending upward at right')
inv('Papiers d Artin entry','deletion',[540,1310,998,1387],"Papiers d'Artin (13)")
inv('Two long Papiers strikes','deletion',[541,1330,989,1383],'Two near-parallel rising cancellation strokes')
inv('Two short rules under 13','drawing',[914,1356,966,1375],'Double underline beneath 13')
inv('Lichtenbaum entry','deletion',[545,1374,1400,1474],'Lichtenbaum, surfaces arithmétiques')
inv('Lichtenbaum broad cancellation','deletion',[546,1382,1396,1453],'Long grey strike rising to the right')
inv('Manin entry','deletion',[542,1447,1422,1527],'Manin, variétés rationnelles (2 articles)')
inv('Manin broad cancellation','deletion',[544,1451,1426,1523],'Long grey rising strike')
inv('Harder entry','deletion',[550,1537,1324,1615],'Harder, sur conjecture de Weil')
inv('Harder extended cancellation','deletion',[552,1540,1326,1606],'Long dark strike extending beyond Weil')
inv('Isolated lower-left point','drawing',[239,1756,254,1771],'Point below list',extra='Intentional ink versus surface speck unresolved')
inv('Archive sheet number, comment only','text',[59,2046,101,2097],'3','handwritten archive mark',extra='Recorded only as the required archive-number comment; not an authorial page number')

remaining_doubts=[
 dict(place='Mumford title, first vowel',reading=r'f\unsure{o|u}nction',alternatives=['fonction','function'],confidence='medium'),
 dict(place='Artin, retraced inner cluster',reading=r'\unsure{Artin}',alternatives=['Artin; inner r/t/i not wholly separated'],confidence='medium'),
 dict(place='First Monsky-Washnitzer',reading=r'\unsure{Monsky-Washnitzer}',alternatives=['Monsky-Washnitzer; filled vowel and pale joined middle remain uncertain'],confidence='medium'),
 dict(place='Cancelled Notes, first vowel of tapis',reading=r't\unsure{a|o}pis',alternatives=['tapis','topis'],confidence='medium'),
 dict(place='Lower mark after cot',reading=r'cot$_{\unsure{*|+}}$',alternatives=['star','plus'],confidence='medium'),
 dict(place='Borel lower oblique trace',reading=rl(r'\node[anchor=center] at (556'),alternatives=['letter-terminal affiliation','additional cancellation trace'],confidence='low'),
 dict(place='Mark beside Deligne',reading=r'\unsure{1|2|?}',alternatives=['1','2','?'],confidence='low'),
 dict(place='Cancelled parenthesis below Deligne',reading=r'\unsure{suite|suiten}',alternatives=['suite','suiten'],confidence='medium'),
 dict(place='Hatching of cancelled parenthesis',reading=block(R,r'\node[anchor=north west] at (244,1127)',r'\end{tikzpicture}}};'),alternatives=['overlapping slanting hatch run; exact original joins and pen-lift boundaries unresolved'],confidence='medium'),
 dict(place='Serre separator',reading=r'\unsure{:|.}',alternatives=['colon with upper point on strike','single stop'],confidence='low'),
 dict(place='Serre relation after p',reading=r'\unsure{\ne|>}',alternatives=[r'\ne','>'],confidence='low'),
 dict(place='Detached right-side point',reading=rl(r'\node[anchor=center] at (1608'),alternatives=['intentional isolated ink','surface speck'],confidence='low'),
 dict(place='Surname after Lettre',reading=r'\unsure{Rietzly|Rietzley}',alternatives=['Rietzly','Rietzley'],confidence='low'),
 dict(place='class before field',reading=r'\unsure{class}',alternatives=['class; covered a/s/s remain uncertain'],confidence='low'),
 dict(place='Short cancelled start',reading=r'\unsure{Que|Qui}',alternatives=['Que','Qui'],confidence='low'),
 dict(place='Weil final adjective',reading=r'\unsure{intermédiaires}',alternatives=['intermédiaires; low middle and exact accented vowel remain uncertain'],confidence='low'),
 dict(place='Lichtenbaum final adjective',reading=r'\unsure{arithmétiques}',alternatives=['arithmétiques; low middle and exact accent remain uncertain'],confidence='medium'),
 dict(place='Lower-left point',reading=rl(r'\node[anchor=center] at (245,1763)'),alternatives=['intentional isolated ink','surface speck'],confidence='low')
]

notes=[
 {'topic':'Nature of page','text':'A handwritten working list in three physically distinct groups headed Raynaud, Illusie 1 and Deligne with a doubtful adjacent mark. The title entries are positioned in a right column. It is not a proof or a computation.'},
 {'topic':'Raynaud group','text':'Lists a Mumford Theta title with I and II, Papiers Kiehl, and Artin-Winters. The first vowel of the title word and the retraced Artin cluster remain doubtful.'},
 {'topic':'Illusie group','text':'Lists Monsky-Washnitzer I and II, letters and an Affine duality item for Hartshorne, letters to Quillen, infinitesimal extensions, a cancelled Notes item with (pluriel), R. Wood Bourbaki calcul différentiel, Complexe cot with a small lower mark, an Atiyah-extension item with Omega^1, Koszul 2 articles, and cancelled Borel Lecture Notes.'},
 {'topic':'Deligne group','text':'Includes a second Monsky-Washnitzer item, a cancelled Serre item on Vect. Witt and var. abéliennes with a characteristic condition, a Griffiths title beginning “On monodromy”, a cancelled letter entry, a cancelled short start, and cancelled Weil, Artin, Lichtenbaum, Manin and Harder items.'},
 {'topic':'Source hesitations and working state','text':'No securely readable verbal hesitation such as peut-être occurs. Source incompletion is explicit in the four terminal marks after “On monodromy” and the two-short-plus-long graphic after Omega^1. The cancelled “Que/Qui” is a short abandoned start. The mark after Deligne may itself be a question mark, but that is unresolved. Reading doubts are editorial and are not presented as authorial hesitations.'},
 {'topic':'Dates, numbering and counts','text':'No date or overall title is visible. Illusie is followed by 1; the mark after Deligne remains 1/2/?. Roman I and II occur in the first titles. Two entries explicitly say 2 articles. The underlined 13 in the Artin entry is preserved without assigning it a page-count meaning. The lower-left 3 is the archive mark and appears only in a comment.'},
 {'topic':'Media and alphabets','text':'All textual entries are handwritten. Dark blue/black writing and paler grey strokes are visible; pencil-like is a visual description, not a material identification. No typewriter double striking, script sheaf alphabet or double-struck mathematical alphabet is introduced. The Roman numeral head/foot rules are separately observed.'},
 {'topic':'Witness handling','text':'H is treated as an unverified direct transcription, not an independent authority for expanding Ch., Vect., car or cot. Its list-joining em dashes and semicolons are editorial separators and are excluded from differences. Local ill spans are quoted literally and scoped to the unread source region; nearby ill does not make an otherwise unmarked H word doubtful.'},
 {'topic':'Drawing treatment','text':'The supplied macros are not redefined. Existing deletion state is retained and literal paths are drawn additionally where source extents, separate strokes, hatching or waviness carry information. In the lower parenthesis, the six schematic diagonals and terminal return reproduce the observed hatch pattern approximately; original pen lifts remain unresolved.'}
]

notation=[
 {'form':'Theta','reading':r'\Theta','evidence':'Closed oval with a distinct transverse median bar in the Mumford entry.'},
 {'form':'Roman I and II','reading':r'\overline{\underline{\mathrm I}},\overline{\underline{\mathrm{II}}}','evidence':'Separate head and foot rules; top I additionally has a tall open-ended enclosing loop. The two occurrences were read independently.'},
 {'form':'Lower cot mark','reading':r'\unsure{*|+}','evidence':'Compact lower vertical, lateral and oblique parts; neither star nor plus is secure.'},
 {'form':'Omega with exponent','reading':r'\Omega^{1}','evidence':'Open-bottom capital and raised hooked numeral 1; no prime or lower index.'},
 {'form':'Characteristic condition','reading':r'p\unsure{\ne|>}0','evidence':'Lowercase p, covered angular/intersecting sign and closed zero. The cancellation does not decide the sign.'},
 {'form':'Quotation marks','reading':"``...''",'evidence':'Two opening hooks and two closing hooks around the Griffiths title; not guillemets.'},
 {'form':'13','reading':r'\uuline{13}','evidence':'Arabic 1 and 3 with two lower rules, independently of the two long cancellation strokes.'},
 {'form':'Cancelled short start','reading':r'\unsure{Que|Qui}','evidence':'Final low loop favors e; a distinct i dot is not secure.'}
]

abbreviations=[
 {'form':'R.','expansion':'Editorial: unresolved initial or abbreviation; no full name or Rapport expansion is adopted.'},
 {'form':'cot','expansion':'Editorial proposed expansion: cotangent. The lower star/plus mark is retained separately and is not expanded.'},
 {'form':'Ch.','expansion':'Editorial: unresolved abbreviation; cohomologie is a possible expansion suggested by H, not established by the ink and not substituted in the reading.'},
 {'form':'Vect.','expansion':'Editorial expansion: vecteurs.'},
 {'form':'var.','expansion':'Editorial expansion: variétés.'},
 {'form':'car','expansion':'Editorial expansion: caractéristique. The source has no stop after car.'},
 {'form':'thy','expansion':'Editorial expansion: theory. The written English abbreviation is retained.'}
]

math_checks=[
 {'check':'Scope of mathematical verification','performed':False,'result':'There is no stated proof or computation to verify on this list page. No theorem, bibliographic identity or document count was externally checked.'},
 {'check':'Theta versus unbarred circular letter','performed':True,'result':'A targeted visual comparison of the local oval and its transverse stroke confirms Theta. This is a glyph check, not a mathematical theorem check.'},
 {'check':'Omega exponent position and value','performed':True,'result':'The crop was checked for superscript versus subscript and numeral versus prime: the hooked 1 with its foot is raised to the upper right of Omega.'},
 {'check':'Relation in the characteristic condition','performed':True,'result':'The local sign was inspected for a second bar and crossing stroke. The deletion conceals enough of it that ne and > both remain. Mathematical expectations about characteristic were not used to select a reading.'},
 {'check':'Numeral counts and underlines','performed':True,'result':'The Roman groups visibly have one and two uprights; the Artin parenthesis reads 13 with two short rules. The two occurrences of 2 articles were read as source wording; no external count of articles was attempted.'}
]

report=dict(page='H162-01_162-1_scan004',reader='R2',viewed={
 'whole':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan004.jpg',
 'a':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan004_a.jpg',
 'b':'source/SP57_CW_97+123+162-1+162-6_scans/H162-01_162-1_scan004_b.jpg'},
 reading_file=str(base/'reading.tex'),differences=differences,c_doubts=c_doubts,inventory=inventory,remaining_doubts=remaining_doubts,notes=notes,notation=notation,abbreviations=abbreviations,math_checks=math_checks,crop_count=21,workflow_feedback=[
 'Read the four required briefing/convention files and the assigned C/H/question/meta packet. The appended current-page C note about the Deligne question-mark alternative was read and covered by the existing local locus.',
 'Whole image 1681 x 2138 viewed once for layout; half a 1681 x 1149 viewed once line by line; half b 1681 x 1149 viewed once line by line. Half b begins at whole-image y=989. Every agreement entry was checked from ink.',
 'Twenty-one tightly targeted crops were made with out/scripts/crop.py and each viewed once. Several crops cover a neighboring cluster of unresolved marks in one line. No crop was repeated and no decided locus was re-viewed.',
 'The complete reading.tex was saved before assembling this longer report. All output files and crop images were written only under the assigned R2 directory.',
 'No OCR, web lookup, external edition, other page image, other reader file, root decision file, extra agent or optional TeX compilation was used.',
 'Source geometry is encoded in one coordinate-based TikZ layout, with each list entry on its own source row. This preserves the two columns, the large blank above Illusie, the lower parenthetical note, and the long angled cancellations without redefining state macros.',
 'The finite source resolution and covered low letter bodies limit several name and adjective readings. Those doubts remain in place; no contextual repair was made.'
])
(base/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'saved':str(base/'report.json'),'differences':len(differences),'c_doubts':len(c_doubts),'inventory':len(inventory),'remaining_doubts':len(remaining_doubts),'crop_count':21},ensure_ascii=False))
