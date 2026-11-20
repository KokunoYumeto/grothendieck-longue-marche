from pathlib import Path
from datetime import datetime, timezone
import json
O=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R3')
B='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-08_156-4_scan065'
S=B+'.jpg'; A=B+'_a.jpg'; HLF=B+'_b.jpg'
crops=json.loads((O/'crop_manifest.json').read_text())
cp={int(Path(z['path']).stem[:2]):z for z in crops}
d=[]
def diff(location,c,h,reading,scan_shows,confidence='high',kind='misread word',marked='no',cc=False,ch=True,crop=None,bbox=None,math=False,source=None):
 if crop:
  item=cp[crop]; crop=item['path']; bbox=bbox or item['bbox']; source=source or S
 else: source=source or A
 d.append(dict(id=f'R3-D{len(d)+1:02}',location=location,c=c,h=h,reading=reading,scan_shows=f'Image: {source}. '+scan_shows,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=crop,bbox=bbox,math_consequential=math))
diff('Opening: donnons nous',r'donnons nous',r'donnons-nous',r'donnons nous','There is an ordinary gap between the two words and no connecting hyphen.',kind='abbreviation expanded or spelling modernised',bbox=[780,150,1240,220])
diff('Opening: canceled formula',r'\deleted{$\unsure{F_i\in|F_i}$}',r'\struck{$F_i \in$}',r'\deleted{$\unsure{F_i\in|F_i}$}','The F and low i are visible; the rightward crossed stroke meets a C-shaped mark. Membership versus the start of the parenthesis cannot be cleanly segmented.',confidence='low',kind='other',crop=1,math=True)
diff('Opening: quantifier parentheses and following comma',r'$\unsure{(}\forall i\in I)$',r'$\forall i \in I$,',r'$\unsure{(}\forall i\in I)$','The closing parenthesis after I is clear, and no following comma is visible. A possible opening parenthesis is crowded against the cancellation.',confidence='medium',kind='omission',crop=1,math=True)
diff('Opening: family in chosen component',r'F_i\in\mathcal F_i',r'F_i\in\mathfrak{F}_i',r'F_i\in\mathcal F_i','The individual F has a straight upper arm; the family F has an arcing hooked upper arm and curved foot, without Gothic angular construction.',kind='misread symbol or index',bbox=[480,242,706,320],math=True)
diff('Opening: question wording',r'quand peut-on dire',r'pouvons-nous \uncertain{affirmer}',r'quand peut-on dire','The first word begins with a long descending q, followed by the separate peut-on and dire groups.',marked='yes',bbox=[778,264,1493,338])
diff('Opening: existential family',r'F\in\mathcal F',r'F\in\mathfrak{F}',r'F\in\mathcal F','The family has the bent upper arm and curled foot also visible beside the individual F in this crop.',kind='misread symbol or index',crop=2,math=True)
diff('Opening: i composante',r'$i$ composante',r'$i$-composante',r'$i$ composante','A gap follows i; no hyphen connects i to composante.',kind='abbreviation expanded or spelling modernised',bbox=[440,455,831,506])
diff('Opening: overwritten final F',r'\deleted{\unsure{\mathcal F}}',r'',r'\deleted{\unsure{\mathcal F}}','The final capital has a curved top and foot beneath a heavily reinforced straight F; the underlying calligraphic reading remains uncertain.',confidence='medium',kind='omission',crop=2,math=True)
diff('Opening: low mark beside final F',r'\unsure{F_0|F}',r'F',r'\unsure{F_0|F}','A distinct small closed loop with a short tail is below and to the right of the F. It may be a subscript 0; its size and tail prevent excluding a stray mark.',confidence='low',kind='misread symbol or index',crop=2,math=True)
diff('Second paragraph: faudrait',r'il le faudrait',r'il le faut \uncertain{sûrement}',r'il le faudrait','The long word after le continues through the -drait ending; there is no separate sûrement word.',marked='yes',bbox=[607,526,1131,638])
diff('Second paragraph: before tous',r'pour \unsure{le|les} cas où',r'pour \struck{\ill{}} \ill{}',r'pour \unsure{le|les} cas où','The looped le/les group and cas are live. The following line begins où. The terminal stroke of le/les remains compressed.',confidence='medium',kind='readable ink left as \\ill{}',marked='yes',crop=3)
diff('Second paragraph: sont',r'sont',r'soient',r'sont','The final word of this line has the so- body and terminal nt stroke, without an i-dot or separate ie group.',bbox=[1519,636,1634,688])
diff('Second paragraph: transition to C4',r'On va supposer donc',r'Donc on supposera donc',r'On va supposer donc','The line after vides starts with the looped capital O of On, then va, then supposer, then donc.',bbox=[597,709,1312,789])
diff('C4: first pair of variables',r'x,y',r'X,Y',r'x,y','The small crossed x and short descending y are lower in height than M and match the later variables in this paragraph.',kind='misread symbol or index',crop=4,math=True)
diff('C4: ambient set at both occurrences',r'M',r'\mathcal{M}',r'M','Both occurrences use a single plain peaked M, without a distinct calligraphic loop or flourish.',kind='misread symbol or index',crop=4,math=True)
diff('C4: final pair of variables',r'x \text{ et } y',r'X \text{ et } Y',r'x \text{ et } y','The later x and y repeat the small crossed/descending forms of the first pair.',kind='misread symbol or index',bbox=[302,1067,526,1146],math=True)
diff('C4: des comp.',r'\unsure{des|deux}',r'deux',r'des','The short word ends in an un-crossed returning s stroke, not the crossed x form. The visible word is des.',cc=True,crop=4)
diff('Inserted sentence: abbreviation néc',r'\unsure{néc|néc.}',r'nécessaire',r'néc','The abbreviation has n, a small accented e, and an open terminal c. There is no separate dot after c.',kind='abbreviation expanded or spelling modernised',cc=True,crop=5)
diff('Inserted sentence: validity group and possible canceled beginning',r'\deleted{\unsure{déd|val}} \unsure{validité|déduction}',r'\ill{}',r'\unsure{validité|\deleted{val}idité}','The lower line has an initial val-like group, an i-dot, and a following dité-like group. I see one word-sized group rather than a canceled word followed by another complete word. The stroke along the first letters may be joining/retracing or cancellation; this state is unresolved.',confidence='low',kind='other',marked='yes',cc=True,crop=5)
diff('Inserted sentence: placement relative to canceled Cor',r'\deleted{Cor} \inserted{C\textquotesingle est ... des}',r'C\textquotesingle est ... des \ill{}; \struck{Cor}',r'\deleted{Cor} \inserted{C\textquotesingle est ... des}','The necessity sentence is interlined above the old canceled Cor and introduces Corollaire 1. It is represented as an insertion replacing that abandoned beginning.',kind='insertion or placement',marked='yes',crop=5)
diff('Inserted sentence: alleged extra word after des',r'des',r'des \ill{}',r'des','After the final des group, the rest of the interline is blank; no further word is present.',kind='text not on the page',marked='yes',crop=5)
diff('Corollary 1: map family alphabet',r'\mathcal F\to\prod\mathcal F_i',r'\mathfrak{F}\to\prod\mathfrak{F}_i',r'\mathcal F\to\prod\mathcal F_i','The family letters have curved/hooked upper arms. The arrow has a clear right-pointing head and the product has its separate top bar.',kind='misread symbol or index',bbox=[1074,153,1368,226],source=HLF,math=True)
diff('Corollary 1: canceled sauf',r'\deleted{sauf}',r'sauf',r'\deleted{sauf}','A heavy horizontal cancellation crosses the word from its initial s to the final descending f.',kind='deletion state (struck given live or live given struck)',crop=7,math=True)
diff('Corollary 1: finite-support ending and pres/que separation',r'pour \deleted{\unsure{pres}}que tout $i$',r'pour \struck{\ill{}} un nb fini d\textquotesingle $i$',r'pour \deleted{\unsure{pres}} que tout $i$','A canceled p/r/e/s-like group is followed by the separately spaced, live que, then tout i. There is no un nb fini d\textquotesingle i here. The initial canceled group remains doubtful.',confidence='medium',kind='misread word',marked='yes',cc=True,crop=6,math=True)
diff('Corollary 2: added heading and enclosure',r'\inserted{\uline{Cor. 2}}',r'\emph{Cor. 2}; \note{... cadre ...}',r'\figure{\begin{tikzpicture}...\inserted{\uline{Cor. 2}}...\end{tikzpicture}}','Cor. 2 is underlined above the old donc. An open angular enclosure has a top stroke, a long left side, and a lower-left arm reaching toward the continuation. The reading reproduces that shape in TikZ; it is not a closed rectangle.',kind='drawing or diagram',marked='yes',cc=True,crop=8)
diff('Corollary 2: canceled donc initial',r'\deleted{\unsure{donc}}',r'\struck{Donc}',r'\deleted{\unsure{donc}}','The visible initial has a low loop and upright ascender of d beneath the cancellation, rather than a separate capital D arch. The remaining nc is heavily covered.',confidence='medium',kind='misread word',crop=8)
diff('Corollary 2: map family alphabet',r'\mathcal F\to\prod\mathcal F_i',r'\mathfrak{F}\to\prod\mathfrak{F}_i',r'\mathcal F\to\prod\mathcal F_i','The family F has the same hooked upper stroke and curved foot as elsewhere; the map has a bold complete right arrowhead.',kind='misread symbol or index',crop=8,math=True)
diff('Corollary 2: le/les correction',r'\deleted{les} le',r'les',r'le\deleted{\unsure{s}}','Only one l loop and one e loop are visible. The thickened trailing short stroke looks like the s being canceled; I do not see a second complete le written separately. The extent of the correction remains uncertain.',confidence='low',kind='deletion state (struck given live or live given struck)',cc=True,crop=9)
diff('Corollary 2: whole inserted I est fini and old suivants placement',r'\deleted{suivants} \inserted{$I$ est} \deleted{\unsure{f}} fini.',r'$I$ est fini \struck{suivants : ...}',r'\deleted{suivants} \inserted{$I$ est fini.}','I est fini lies together on an interline above the old canceled suivants. The reading marks the entire new phrase as inserted and keeps the old word at its original position after où.',kind='insertion or placement',cc=True,crop=10,math=True)
diff('Corollary 2: alleged isolated canceled f',r'\deleted{\unsure{f}}',r'',r'','The f-like upright below the insertion belongs to the last letters of the canceled suivants: it is connected to the preceding word and followed by its terminal curve. I find no separate old f to transcribe.',confidence='medium',kind='text not on the page',cc=True,ch=False,crop=10)
diff('Corollary 2: colon after canceled suivants',r'\deleted{suivants}',r'\struck{suivants :}',r'\deleted{suivants}','No two-dot colon follows the canceled word. A period belongs to the inserted fini on the line above.',kind='text not on the page',crop=10)
diff('Canceled case a: semicolon',r'\deleted{a) $I$ est fini}',r'\struck{a) $I$ est fini ;}',r'\deleted{a) $I$ est fini}','The crossed case a ends after fini; no semicolon is visible before the next, separate canceled line.',kind='text not on the page',bbox=[340,622,740,694],source=HLF)
diff('Canceled case b: capital Toute',r'Toute',r'toute',r'Toute','The first letter has a broad capital upper bar and upright stroke.',kind='abbreviation expanded or spelling modernised',bbox=[443,706,651,757],source=HLF)
diff('Canceled case b: short dash',r'\unsure{--}',r'\ill{}',r'--','A short horizontal stroke is separately visible below the long cancellation and before alors.',kind='readable ink left as \\ill{}',marked='yes',cc=True,crop=11)
diff('Corollary 3: canceled group after figures',r'\deleted{\unsure{de}}',r'\struck{\ill{}}',r'\deleted{\unsure{de}}','A low initial loop with an ascending stroke supports d; the short remaining ending is obscured by cancellation. de is the best reading, retained as uncertain.',confidence='low',kind='readable ink left as \\ill{}',marked='yes',crop=12)
diff('Corollary 3: membership family alphabet',r'\in\mathcal F',r'\in\mathfrak{F}',r'\in\mathcal F','The family F has a long curved top stroke and hooked lower stem.',kind='misread symbol or index',crop=14,math=True)
diff('Corollary 3: resp. finies insertion state and placement',r'\deleted{Alors il} \inserted{(resp. finies)}.',r'(resp. finies) \struck{\ill{}}.',r'\deleted{Alors il} \inserted{(resp. finies)}.','The parenthesis is above the canceled Alors il. The period after t.f. remains visible before the old phrase, and another period follows the inserted parenthesis at the live Alors line.',kind='insertion or placement',marked='yes',crop=13)
diff('Corollary 3: readable canceled Alors il',r'\deleted{Alors il}',r'\struck{\ill{}}',r'\deleted{Alors il}','The capital A, joined lors, and separated il remain visible beneath the horizontal strike.',kind='readable ink left as \\ill{}',marked='yes',crop=13)
diff('Corollary 3: two-stroke repetition mark',r'\unsure{=|\text{même}}',r'même',r'=','Two short stacked horizontal strokes are visible; the letters of même are not written. The reading retains the graphic mark literally.',kind='abbreviation expanded or spelling modernised',cc=True,crop=14)
diff('Corollary 3: canceled de after repetition mark',r'\deleted{\unsure{de}}',r'',r'\deleted{\unsure{de}}','A separate crossed group has a low d loop and short obscured ending. It is present between the two-stroke mark and pour.',confidence='medium',kind='omission',crop=14)
diff('Corollary 3: family after pour',r'\mathcal F_i',r'\mathfrak{F}_i',r'\mathcal F_i','The family has a curved leftward upper hook and separate low i.',kind='misread symbol or index',crop=14,math=True)
diff('Corollary 3: final map family alphabet',r'\mathcal F\unsure{\text{---}|\longrightarrow}\prod\mathcal F_i',r'\mathfrak{F}\to\prod\mathfrak{F}_i',r'\mathcal F\unsure{\text{---}|\longrightarrow}\prod\mathcal F_i','Both family letters have hooked upper strokes; the second i is separately low and dotted.',kind='misread symbol or index',crop=15,math=True)
diff('Corollary 3: final connector',r'\unsure{\text{---}|\longrightarrow}',r'\to',r'\unsure{\text{---}|\longrightarrow}','The connector is horizontal with one short downward terminal turn. A full two-branch arrowhead is absent, unlike the two earlier maps. A reduced arrow remains possible.',confidence='medium',kind='misread symbol or index',crop=15,math=True)
diff('Corollary 3: abbreviation ens punctuation',r'l\textquotesingle ens',r'l\textquotesingle ens.',r'l\textquotesingle ens','No dot separates the ending ens from the following des.',kind='text not on the page',crop=16)
diff('Corollary 3: pres que',r'pres que',r'presque',r'pres que','The pres group ends before a visible gap; the following que begins with a separately drawn long descending q.',kind='abbreviation expanded or spelling modernised',crop=16)

diff('C4: punctuation after comp',r'comp.',r'comp.',r'comp','The last stroke remains joined to the p-like ending; no separate abbreviation point follows it.',kind='text not on the page',cc=True,crop=17)

cd=[]
def doubt(location,c,reading,status,scan,crop=None,bbox=None,source=None):
 if crop:
  item=cp[crop]; crop=item['path']; bbox=bbox or item['bbox']; source=source or S
 else: source=source or A
 cd.append(dict(location=location,c=c,reading=reading,status=status,scan_shows=f'Image: {source}. '+scan,crop=crop,bbox=bbox))
doubt('Opening: canceled formula',r'\unsure{F_i\in|F_i}',r'\unsure{F_i\in|F_i}','retained','Cancellation joins the old membership-like stroke and neighboring C shape.',1)
doubt('Opening: opening parenthesis',r'\unsure{(}',r'\unsure{(}','retained','A C-shaped stroke may be the opening parenthesis, but it is too close to the canceled formula to separate reliably.',1)
doubt('Opening: underlying final family F',r'\deleted{\unsure{\mathcal F}}',r'\deleted{\unsure{\mathcal F}}','retained','Curved top and foot survive beneath the heavy final F.',2)
doubt('Opening: low mark beside final F',r'\unsure{F_0|F}',r'\unsure{F_0|F}','retained','A closed low loop with short tail supports subscript 0 but could be a stray ink mark.',2)
doubt('Second paragraph: le or les cas',r'\unsure{le|les}',r'\unsure{le|les}','retained','The tall l and compressed ending are visible; the last stroke does not decide the s.',3)
doubt('C4: des or deux',r'\unsure{des|deux}',r'des','resolved','The terminal s-like returning stroke is not a crossed x.',4)
doubt('Inserted sentence: néc punctuation',r'\unsure{néc|néc.}',r'néc','resolved','No separate dot follows the final c.',5)
doubt('Inserted sentence: alleged canceled déd/val',r'\deleted{\unsure{déd|val}}',r'\unsure{validité|\deleted{val}idité}','revised','The val-like start and subsequent idité-like ink form one word-sized group. Whether the first letters are crossed or joined/retraced remains unsettled.',5)
doubt('Inserted sentence: alleged following complete word',r'\unsure{validité|déduction}',r'\unsure{validité|\deleted{val}idité}','revised','The visible remainder is only the latter part of a validity-like word; a separate complete validité or déduction after a canceled word is not supported.',5)
doubt('Corollary 1: canceled pres',r'\deleted{\unsure{pres}}',r'\deleted{\unsure{pres}}','retained','Initial p descender and crowded later small letters are partly obliterated.',6)
doubt('Corollary 2: canceled donc',r'\deleted{\unsure{donc}}',r'\deleted{\unsure{donc}}','retained','Low d loops and final compressed strokes survive under a long cancellation.',8)
doubt('Corollary 2: alleged canceled f',r'\deleted{\unsure{f}}',r'','resolved','The upright joins the ending of canceled suivants rather than forming a separate word or letter.',10)
doubt('Canceled b: dash before alors',r'\unsure{--}',r'--','resolved','The short horizontal mark is distinct from the main strike above it.',11)
doubt('Corollary 3: canceled de after figures',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de}}','retained','The d-like loop and ascender are visible; the short ending remains heavily obscured.',12)
doubt('Corollary 3: repetition mark',r'\unsure{=|\text{même}}',r'=','resolved','The ink consists of two stacked strokes; the word même is not written.',14)
doubt('Corollary 3: canceled de after repetition mark',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de}}','retained','A separate d-like loop is visible, with the e largely hidden by cancellation.',14)
doubt('Corollary 3: last map connector',r'\unsure{\text{---}|\longrightarrow}',r'\unsure{\text{---}|\longrightarrow}','retained','Horizontal stroke with a single downward terminal turn, not a complete arrowhead.',15)
doubt('C_context: family/individual F and dotted i distinction',r'F_i,\mathcal F_i,\forall i,(F_i)_{i\in I}',r'F_i,\mathcal F_i,\forall i,(F_i)_{i\in I}','resolved','The plain individual F and hooked family F, the crossbar of the quantifier, and separate dotted i indices were checked in the upper half and crop 6.',6)
doubt('C_context: C4 x,y,M and membership',r'x,y\in M',r'x,y\in M','resolved','Small crossed x, descending y, plain peaked M, and open membership sign with internal bar are visible.',4)
doubt('C_context: empty signs and first two arrows',r'\varnothing,\to',r'\varnothing,\to','resolved','The empty sign is a slashed oval; the first two map strokes have complete right arrowheads.',7)
doubt('C_context: final pres que',r'pres que',r'pres que','resolved','Separate pres and que groups have a clear intervening gap.',16)

inv=[]
def inventory(element,kind,position,words):
 inv.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='handwritten manuscript',hand='his hand',transcribed='yes'))
inventory('Manuscript pagination','pagination','top center, whole [685,45,759,103]','64')
inventory('Opening question','text block','upper page, whole [303,145,1650,510]','Inversement, donnons nous')
inventory('Opening old formula','deletion','end of first line, whole [1310,151,1419,216]',r'F_i\in / F_i')
inventory('Overwritten final family F','deletion','end of opening question, whole [980,432,1054,504]',r'\mathcal F beneath F')
inventory('Preliminary finite-support paragraph','text block','whole [296,525,1632,815]','Déjà, il le faudrait')
inventory('Empty-set sign before vides','deletion','whole [295,726,362,813]',r'\varnothing')
inventory('Condition C4','text block','whole [287,854,1555,1148]','C4 Si x,y∈M')
inventory('Abandoned Cor heading','deletion','whole [305,1191,451,1256]','Cor')
inventory('Necessity and sufficiency sentence','insertion','interline, whole [555,1117,1446,1223]',"C'est néc et suffisant pour la")
inventory('Possible cancellation in validity group','deletion (uncertain state)','whole [782,1183,897,1220]','val / live first part of validité')
inventory('Corollary 1','text block','whole [307,1260,1635,1577]',"Corollaire 1 L'image")
inventory('sauf after equality','deletion','whole [1507,1358,1628,1417]','sauf')
inventory('pres before que','deletion','whole [507,1480,632,1543]','pres')
inventory('Corollary 2 heading','insertion','right-hand interline, whole [1135,1425,1302,1483]','Cor. 2')
inventory('Angular enclosure and insertion connector','drawing','whole [877,1404,1339,1583]','open top/left enclosure with lower-left arm')
inventory('Old donc under Cor. 2','deletion','whole [1134,1478,1371,1513]','donc')
inventory('Corollary 2 statement','text block','whole [303,1448,1632,1729]',r'\mathcal F\to\prod\mathcal F_i est une bijection')
inventory('Possible terminal s cancellation in les','deletion','whole [1149,1562,1192,1593]','s in les')
inventory('deux in Corollary 2','deletion','whole [1282,1550,1437,1590]','deux')
inventory('suivants after cas où','deletion','whole [299,1659,626,1728]','suivants')
inventory('I est fini replacement','insertion','whole [365,1641,741,1728]','I est fini.')
inventory('Old case a','deletion','whole [341,1727,745,1794]','a) I est fini')
inventory('Old case b','deletion','whole [372,1746,1625,1862]','b) Toute figure est de t.f. -- alors')
inventory('Corollary 3','text block','whole [285,1820,1633,2303]','Cor 3 Supposons que les figures')
inventory('de after figures','deletion','whole [1537,1834,1631,1870]','de')
inventory('Alors il before parenthetical insertion','deletion','whole [892,1943,1165,2012]','Alors il')
inventory('Parenthetical finiteness alternative','insertion','whole [846,1908,1209,1984]','(resp. finies)')
inventory('de after repetition mark','deletion','whole [766,2053,860,2091]','de')

remaining=[
 dict(location='Opening canceled formula and opening parenthesis',reading=r'\deleted{$\unsure{F_i\in|F_i}$} $\unsure{(}\forall i\in I)$',alternatives=[r'\deleted{$F_i\in$} $(\forall i\in I)$',r'\deleted{$F_i$} $\forall i\in I)$'],confidence='low',reason='Overlapping cancellation and C-shaped curve prevent reliable segmentation.'),
 dict(location='Opening final overwritten F',reading=r'\deleted{\unsure{\mathcal F}}\unsure{F_0|F}',alternatives=[r'\deleted{\mathcal F}F_0',r'\deleted{\mathcal F}F',r'F_0'],confidence='low',reason='The underlying family form is probable, and the low loop may be a 0 or a stray mark.'),
 dict(location='Second paragraph before cas',reading=r'\unsure{le|les}',alternatives=['le','les'],confidence='medium',reason='Compressed terminal stroke does not securely decide the s.'),
 dict(location='Inserted validity phrase',reading=r'\unsure{validité|\deleted{val}idité}',alternatives=['validité',r'\deleted{val}idité'],confidence='low',reason='The initial val-like cluster has a strong baseline stroke that may be ordinary joining/retracing or cancellation. A second full word is not separately visible.'),
 dict(location='Corollary 1 canceled start before que',reading=r'\deleted{\unsure{pres}}',alternatives=['pres'],confidence='medium',reason='Cancellation masks the middle letters, although the initial p and terminal short strokes support pres.'),
 dict(location='Corollary 2 old word under added heading',reading=r'\deleted{\unsure{donc}}',alternatives=['donc'],confidence='medium',reason='The long strike hides much of the letter sequence.'),
 dict(location='Corollary 2 le/les correction',reading=r'le\deleted{\unsure{s}}',alternatives=[r'le\deleted{s}',r'\deleted{les}le','les'],confidence='low',reason='The first l and e are clear and singular; the heavy final stroke may cancel only s or more of the old word.'),
 dict(location='Corollary 3 canceled word after figures',reading=r'\deleted{\unsure{de}}',alternatives=['de'],confidence='low',reason='The ending is almost fully covered by the cancellation.'),
 dict(location='Corollary 3 canceled word after repetition sign',reading=r'\deleted{\unsure{de}}',alternatives=['de'],confidence='medium',reason='The d survives, but the e is mostly obliterated.'),
 dict(location='Corollary 3 final map connector',reading=r'\unsure{\text{---}|\longrightarrow}',alternatives=[r'\text{---}',r'\longrightarrow'],confidence='medium',reason='A horizontal stroke has a tiny downturned right end but lacks a full arrowhead.'),
]
notations=[
 dict(sign='individual figure',latex=r'F,F_i',appearance='Plain upright F with a fairly straight top arm; low i with a separate dot.',location='Opening question and tuple/equality expressions',alternatives=[]),
 dict(sign='family of figures',latex=r'\mathcal F,\mathcal F_i',appearance='Hooked/arcing upper arm and curved lower stem; distinct from the plain individual F.',location='Throughout the page',alternatives=[]),
 dict(sign='ambient set',latex='M',appearance='Plain peaked letter of single strokes, without separate calligraphic loops.',location='C4, twice',alternatives=[]),
 dict(sign='variables',latex='x,y',appearance='Small crossed x and descending short y.',location='C4, first and final pairs',alternatives=[]),
 dict(sign='membership',latex=r'\in',appearance='Open curved form with internal horizontal stroke.',location='Opening and C4; Cor. 3',alternatives=[]),
 dict(sign='universal quantifier',latex=r'\forall',appearance='Long V-like limbs with a transverse bar.',location='Opening question, twice',alternatives=[]),
 dict(sign='empty figure',latex=r'\varnothing',appearance='Small oval crossed by a long rising diagonal.',location='Deleted before vides; Cor. 1 equality; final line',alternatives=[]),
 dict(sign='product',latex=r'\prod',appearance='Separate long top bar and two descending stems; no product index visible.',location='Three maps',alternatives=[]),
 dict(sign='first two map connectors',latex=r'\to',appearance='Horizontal stroke with complete right-pointing head.',location='Cor. 1 and Cor. 2',alternatives=[]),
 dict(sign='last connector',latex=r'\unsure{\text{---}|\longrightarrow}',appearance='Horizontal line with one tiny downturned terminal stroke.',location='Cor. 3 last map',alternatives=[r'\longrightarrow']),
 dict(sign='repetition mark',latex='=',appearance='Two stacked nearly horizontal strokes; the lower one has a curved left start.',location='Cor. 3: en est de ...',alternatives=[]),
 dict(sign='possible subscript on final opening F',latex=r'\unsure{F_0|F}',appearance='Small closed low loop with a short descending tail to the right of a heavily retraced F.',location='End of opening question',alternatives=['no subscript; stray mark']),
]
abbr=[dict(form='néc',expansion='nécessaire'),dict(form='Cor.',expansion='Corollaire'),dict(form='Cor',expansion='Corollaire'),dict(form='nb',expansion='nombre'),dict(form='comp',expansion='composantes'),dict(form='resp.',expansion='respectivement'),dict(form='t.f.',expansion='type fini'),dict(form='ens',expansion='ensemble'),dict(form='=',expansion='même (probable repetition abbreviation; retained graphically)')]

observations={
1:'The old F_i and C-shaped adjoining stroke are visible; cancellation/parenthesis boundary remains open. Clear closing parenthesis and no comma after it.',
2:'Curved family-like strokes lie below the heavy F. A tiny separate closed low loop with tail remains ambiguous between 0 and stray mark.',
3:'le/les has a compressed endpoint; cas and live status are clear. The line below reads nb fini sont.',
4:'Small x,y and plain M verified. Terminal uncrossed stroke supports des; following adjective has a descending j and is disjointes.',
5:'néc has no following dot. Lower val...dité cluster appears one word-sized group; deletion state of initial val remains unresolved. No extra word after des.',
6:'Canceled pres-like cluster followed by spaced live que tout i and a final point. Tuple index i∈I verified.',
7:'sauf is visibly crossed, while the equality and slashed empty sign are live.',
8:'Cor. 2 underlined above old lowercase donc; open angular enclosure reaches down-left. Right map has a complete head.',
9:'One l and one e are visible, with heavy trailing s-like cancellation. Chosen le with canceled doubtful s; no second full le seen.',
10:'Whole I est fini is interlined above canceled suivants. Alleged isolated old f belongs to the t/s ending of suivants. No colon after old word.',
11:'A distinct short horizontal dash lies below the cancellation before alors.',
12:'Canceled de-like word after figures has visible d-like loop/ascender; ending remains masked.',
13:'(resp. finies) inserted above crossed Alors il. Both the t.f. point and the later point before live Alors are visible.',
14:'Two literal stacked strokes, not written letters même. Separate canceled de-like group; family F_i and its index verified.',
15:'Last connector is horizontal with a downturned right tip, no complete head; retained dash/arrow uncertainty. Plain tuple F_i differs from hooked family F.',
16:'Visible pres / que gap and no abbreviation dot after ens. Final tout i and point verified.',
17:'The abbreviation comp has no separately written point. Its p-like ending has a connected small terminal curl; both witnesses supply a period absent as a separate mark.'}
log='# R3 inspection log — scan 065\n\n1. Whole page: '+S+' — viewed once, no transform, for layout.\n2. Upper half: '+A+' — viewed once, no transform; all lines compared with C and H.\n3. Lower half: '+HLF+' — viewed once, no transform; all lines compared with C and H.\n\nNo OCR, text recognition, other scans, reader files, or outside sources.\n'
log+='\n## Own crop views, in order\n\n'
for i,item in enumerate(crops,4):
 n=int(Path(item['path']).stem[:2])
 log+=f"{i}. `{item['path']}`\n   - Source: `{item['source']}`\n   - Original bbox: {item['bbox']}; scale {item['scale']:.9f}; rotation {item['rotation']} degrees.\n   - Transforms: {item['transforms']}.\n   - Visible evidence: {observations[n]}\n\n"
log+='No place was recropped after decision. Some neighboring-context portions overlap because distinct unresolved targets need neighboring-line context. Crop 17 was made during final punctuation review for the previously uncropped comp ending; it is the first crop of that target. No half was viewed twice or enlarged as a whole.\n'
(O/'inspection_log.md').write_text(log)
report=dict(reader='R3',cote='156-4',scan='65',brief_version='v01',started_utc='2026-11-20T08:57:56Z',finished_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),image_views=[S,A,HLF],reading_file=str(O/'reading.tex'),differences=d,c_doubts=cd,inventory=inv,remaining_doubts=remaining,notation=notations,abbreviations=abbr,notes=dict(summary='Complete independent reading of manuscript page 64 / scan 65. All lines were checked against both drafts using the whole-page layout view, each supplied half once, and seventeen own tight crops. The reading retains uncertain small/canceled marks and supplies the open Cor. 2 insertion enclosure in TikZ. The most substantial proposed corrections to C concern the validity-group segmentation, the scope of the les correction, and the alleged isolated canceled f at the end of suivants.',math_reading_decisions='The repeated map context and the later word image made the final connector mathematically consequential and triggered crop 15. Its ink did not supply a complete arrowhead, so the dash-first uncertainty was retained. The opening existential question did not justify removing the small mark by F: F_0/F is retained. No statement was proved or computationally tested; reading a corollary is not counted as mathematical validation.',author_checks='Confirmed cancellations of the old Cor, sauf, pres-like start, donc, deux, suivants, cases a and b, Alors il, and both de-like groups. The validity-group and les correction extents remain explicitly uncertain. All insertions and their placement are recorded. No outside-page assumptions or earlier mathematical results were imported.',title_dates_pagination='Handwritten page number 64 at top center; scan marker 65 retained. No title, date, archive sheet number, stamp, or letterhead is visible. No independent mathematical diagram appears; the one graphic is the open editorial enclosure connecting the added Cor. 2 label to its continuation. marked_in_h=yes denotes an uncertainty/illegibility/editorial note at the locus, not merely a struck-state macro.'),check_events=[],crops=[{k:v for k,v in q.items() if k!='transforms'} for q in crops],workflow_feedback=['The instruction to include one surrounding line can make neighboring crops overlap; overlap here is contextual and is not a repeated crop of a decided target.','Deletion-state uncertainty inside a word, as in validité and les, is not well represented by a single reading/alternative without nested macros. I retained explicit alternatives rather than silently adopting a complete-word deletion.'])
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(d),'c_doubts':len(cd),'inventory':len(inv),'remaining_doubts':len(remaining),'crops':len(crops)},ensure_ascii=False))
