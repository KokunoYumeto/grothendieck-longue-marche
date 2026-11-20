from pathlib import Path
from datetime import datetime, timezone
import json

out = Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_065/R1')
src = Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans')
whole = str(src/'J156-4-08_156-4_scan065.jpg')
half_a = str(src/'J156-4-08_156-4_scan065_a.jpg')
half_b = str(src/'J156-4-08_156-4_scan065_b.jpg')
manifest = json.loads((out/'crops_manifest.json').read_text())
crop_by_number = {i+1: c for i,c in enumerate(manifest)}
differences=[]

def diff(location,c,h,reading,scan_shows,confidence='high',kind='other',marked='no',change_c=False,change_h=True,crop=None,bbox=None,source=None,math=False):
    if crop:
        evidence = crop_by_number[crop]
        crop_path=evidence['path']
        bbox=evidence['bbox'] if bbox is None else bbox
        source=whole if source is None else source
    else:
        crop_path=None
        source=half_a if source is None else source
    differences.append(dict(id=f'R1-D{len(differences)+1:02}',location=location,c=c,h=h,reading=reading,scan_shows=scan_shows,confidence=confidence,kind=kind,marked_in_h=marked,change_c=change_c,change_h=change_h,crop=crop_path,bbox=bbox,bbox_image=source,math_consequential=math))

diff('Opening, donnons nous',r'donnons nous',r'donnons-nous',r'donnons nous','Half a: the two words are separated; no connecting hyphen is visible.',kind='abbreviation expanded or spelling modernised',bbox=[775,140,1300,227])
diff('Opening deletion after donnons nous',r'\deleted{$\unsure{F_i\in|F_i}$}',r'\struck{$F_i \in$}',r'\deleted{$\unsure{F_i\in|F_i}$}','The deleted F and small i can be seen. The canceled strokes to their right do not securely distinguish a membership sign from the adjacent possible parenthesis.',confidence='low',kind='misread symbol or index',crop=1,math=True)
diff('Opening quantifier, parentheses and punctuation',r'$\unsure{(}\forall i\in I)$',r'$\forall i \in I$,',r'$\unsure{(}\forall i\in I)$','The right-hand mark is a large closing parenthesis. The matching opening curved stroke meets the old cancellation and remains uncertain. There is no independent comma after the closing parenthesis.',confidence='medium',kind='misread symbol or index',crop=1,math=True)
diff('Opening, family containing F_i',r'$F_i\in\mathcal F_i$',r'$F_i\in\mathfrak{F}_i$',r'$F_i\in\mathcal F_i$','Half a: the family capital has a curved upper arm and a turned stem, unlike the adjacent plain individual F; it does not have a Gothic construction.',kind='misread symbol or index',bbox=[485,237,705,315],math=True)
diff('Opening question, quand peut-on dire',r'quand peut-on dire',r'pouvons-nous \uncertain{affirmer}',r'quand peut-on dire','Half a: the first word begins with the long descender of q; the next group reads peut-on and the last group begins with a looped d and has the i-dot of dire.',kind='misread word',marked='yes',bbox=[780,248,1500,344])
diff('Opening existential formula, family F',r'$F\in\mathcal F$',r'$F\in\mathfrak{F}$',r'$F\in\mathcal F$','Half a, also visible in crop 02: plain F is followed by membership and a family F with a curved upper arm and turned stem.',kind='misread symbol or index',bbox=[810,325,971,410],math=True)
diff('Opening, i composante',r'la $i$ composante',r'la $i$-composante',r'la $i$ composante','Half a: the small i is separate from composante; no joining hyphen is present.',kind='abbreviation expanded or spelling modernised',bbox=[292,442,835,514])
diff('Opening question, corrected final F and low loop',r'$\deleted{\unsure{\mathcal F}}\unsure{F_0|F}$',r'$F$',r'$\deleted{\unsure{\mathcal F}}\unsure{F_0|F}$','There are overlapping upper and middle arms and a surviving hooked upper stroke beneath the final straight F. A small closed low loop sits at its right. F_0 is the best reading, but its status as an index rather than a stray or punctuation-like mark is not settled.',confidence='low',kind='omission',crop=2,math=True)
diff('Déjà paragraph, faudrait',r'il le faudrait',r'il le faut',r'il le faudrait','Half a: after the tall f the word continues through the -drait ending, including the final high t stroke; it is longer than faut.',kind='misread word',bbox=[607,519,1138,648])
diff('Déjà paragraph, H surely',r'il le faudrait pour',r'il le faut \uncertain{sûrement} pour',r'il le faudrait pour','Half a: the continuous written sequence is il le faudrait pour. There is no separate word between the long faudrait group and pour.',kind='text not on the page',marked='yes',bbox=[605,518,1315,650])
diff('Déjà paragraph, le/les and alleged deletion',r'pour \unsure{le|les} cas',r'pour \struck{\ill{}} \ill{}',r'pour \unsure{le|les} cas','The small word has a tall initial loop and a thickened ending. It may be le or les; I do not see an independent cancellation line that would justify an additional struck word here.',confidence='low',kind='deletion state (struck given live or live given struck)',marked='yes',crop=3)
diff('Déjà paragraph, cas où',r'cas où tous',r'\ill{} tous',r'cas où tous','Half a: cas is at the end of the line and où starts the next line with a visible accent. Both are readable, though H leaves this passage unidentified.',kind='readable ink left as \\ill{}',marked='yes',bbox=[295,531,1620,708])
diff('Déjà paragraph, sauf',r'sauf',r'\uncertain{sauf}',r'sauf','Half a: s, the connected au group and the long descending final f are visible.',kind='other',marked='yes',bbox=[947,622,1087,721])
diff('Déjà paragraph, sont',r'sont',r'soient',r'sont','Half a and crop 03: the word has the short s entry, the long on connection and terminal t; there is no intervening i-dot or an extra i/e group.',kind='misread word',bbox=[1510,617,1632,691])
diff('Déjà paragraph, On va supposer donc',r'On va supposer donc',r'Donc on supposera donc',r'On va supposer donc','Half a: the initial capital and following n read On, followed by the separate short va. The large double-descender word is supposer, with no added final a.',kind='misread word',bbox=[586,702,1320,802])
diff('C4, first formula',r'$x,y\in M$',r'$X,Y\in\mathcal M$',r'$x,y\in M$','The x and y are smaller than the adjacent M. M is a single plain capital with two upper strokes, not a calligraphic alphabet. The membership sign has its inner stroke.',kind='misread symbol or index',crop=4,math=True)
diff('C4, later M, x and y',r'de $M$, alors $x$ et $y$',r'de $\mathcal M$, alors $X$ et $Y$',r'de $M$, alors $x$ et $y$','Half a: the later M retains the same plain form. The following variables repeat the lower-case x and y forms seen in the initial formula.',kind='misread symbol or index',bbox=[300,928,1570,1144],math=True)
diff('C4, des/deux',r'\unsure{des|deux}',r'deux',r'des','The final letter has a short downward terminal turn; there is no crossing for x. The word reads des. The following adjective independently reads disjointes, with its descending j.',confidence='medium',kind='misread word',change_c=True,crop=4,math=True)
diff('Interlinear note, néc abbreviation',r'\unsure{néc|néc.}',r'nécessaire',r'néc','Only the short néc group is written. Its small accent is present; no separate terminal period is visible after c.',confidence='medium',kind='abbreviation expanded or spelling modernised',change_c=True,crop=5)
diff('Interlinear note, validity word and possible cancellation',r'\deleted{\unsure{déd|val}} \unsure{validité|déduction}',r'\ill{}',r'\unsure{validité|\deleted{déd} validité|\deleted{val} validité}','The lower line shows a reinforced vali-like cluster followed by dité and des. Its horizontal stroke lies at the connecting baseline. I cannot securely tell a separate canceled beginning from retracing within validité. No independent full second vali group is visible. Déduction is not supported by the final letter shapes.',confidence='low',kind='deletion state (struck given live or live given struck)',marked='yes',change_c=True,crop=5)
diff('Interlinear note and canceled Cor, placement',r"\deleted{Cor} \inserted{C'est \unsure{néc|néc.} et suffisant pour la \deleted{\unsure{déd|val}} \unsure{validité|déduction} des}",r"C'est nécessaire et suffisant pour la \ill{} des \ill{}"+'\n\n'+r'\struck{Cor}',r"\deleted{Cor} \inserted{C'est néc et suffisant pour la \unsure{validité|\deleted{déd} validité|\deleted{val} validité} des}",'Half a and half b: Cor is the canceled left-hand beginning. The smaller two-line sentence occupies the interlinear space above Corollaire 1 and continues grammatically into that heading. The insertion state is explicit in the reading.',kind='insertion or placement',bbox=[300,1115,1465,1255],source=whole)
diff('Interlinear note, after des',r'des',r'des \ill{}',r'des','Crop 05 and the two halves show des at the end of the small lower line, then the following Corollaire 1 below. No additional word is visible after des in the insertion.',kind='text not on the page',marked='yes',crop=5)
diff('Corollary 1, map alphabets',r'$\mathcal F\to\prod\mathcal F_i$',r'$\mathfrak F\to\prod\mathfrak F_i$',r'$\mathcal F\to\prod\mathcal F_i$','Half b: both family capitals have the looped or turned cursive F form. The product has its top bar; the map has an explicit right arrowhead.',kind='misread symbol or index',bbox=[1080,147,1370,231],source=half_b,math=True)
diff('Corollary 1, sauf deletion',r'\deleted{sauf}',r'sauf',r'\deleted{sauf}','Half b and crop 07: the horizontal cancellation crosses the whole sauf, including its final long f loop.',kind='deletion state (struck given live or live given struck)',bbox=[1500,248,1630,325],source=half_b,math=True)
diff('Corollary 1, crossed pres and its separation from que',r'\deleted{\unsure{pres}}que',r'\struck{\ill{}}',r'\deleted{\unsure{pres}} que','The crossed group has a descending p-like stroke and subsequent small connected loops; pres is the best but not certain reading. A gap separates its final stroke from the live q of que.',confidence='low',kind='readable ink left as \\ill{}',marked='yes',change_c=True,crop=6,math=True)
diff('Corollary 1, final live condition',r'que tout $i$',r"un nb fini d'$i$",r'que tout $i$','The crop clearly shows q with a long descender, then ue; tout has its long connection and terminal t; the final i has a dot and is followed by a stop. The phrase un nb fini d’i is absent here.',kind='misread word',crop=6,math=True)
diff('Corollary 2, canceled donc',r'\deleted{\unsure{donc}}',r'\struck{Donc}',r'\deleted{donc}','Under the inserted heading there is a canceled small looped d followed by the low onc group. It is not a capital D. The cancellation is separate from the heading underline.',confidence='medium',kind='misread word',change_c=True,crop=7)
diff('Corollary 2, map alphabets',r'$\mathcal F\to\prod\mathcal F_i$',r'$\mathfrak F\to\prod\mathfrak F_i$',r'$\mathcal F\to\prod\mathcal F_i$','The family F at the left has a looped upper stroke; the product’s family F has the same turned form. The arrowhead is explicit and the final i is low.',kind='misread symbol or index',crop=7,math=True)
diff('Corollary 2, les/le correction',r'\deleted{les} le',r'les',r'\unsure{le\deleted{s}|les}','Only one l-e group is visible. Its final portion is heavily retraced. The best reading is le with the old s canceled, but live les cannot be excluded. A separate replacement le is not independently written beside the old word.',confidence='low',kind='deletion state (struck given live or live given struck)',change_c=True,crop=8)
diff('Corollary 2, inserted I est fini and canceled suivants',r'\deleted{suivants} \inserted{$I$ est} \deleted{\unsure{f}} fini.',r'$I$ est fini \struck{suivants : a) $I$ est fini ; b) toute figure est de t.f. \ill{} alors}',r'\deleted{\unsure{suivants|suivants f}} \inserted{$I$ est fini.}','The whole live I est fini. is on the upper replacement line. The canceled suivants is lower. The surviving final stop belongs to the upper phrase. H places the canceled original after the live replacement without recording this interlinear state.',confidence='medium',kind='insertion or placement',change_c=True,crop=9,math=True)
diff('Corollary 2, supposed separate canceled f',r'\deleted{\unsure{f}}',r'',r'\deleted{\unsure{suivants|suivants f}}','The apparent additional f coincides with the tall ending and terminal curl of the canceled suivants. I prefer no additional letter, but retain suivants f as the alternative because the superposed strokes do not decisively exclude it.',confidence='low',kind='misread word',change_c=True,crop=9)
diff('Corollary 2, colon after canceled suivants',r'\deleted{suivants}',r'\struck{suivants :}',r'\deleted{\unsure{suivants|suivants f}}','No two-dot colon can be distinguished after the canceled word. The separated punctuation visible to the right is the period of the upper fini.',kind='text not on the page',crop=9)
diff('Canceled a-case, terminal semicolon',r'\deleted{a) $I$ est fini}',r'\struck{a) $I$ est fini ;}',r'\deleted{a) $I$ est fini}','Half b: the canceled a-case ends after fini; no semicolon is visible. The following b-case starts on the next manuscript line.',kind='text not on the page',bbox=[340,620,743,704],source=half_b)
diff('Canceled b-case, initial capital',r'Toute',r'toute',r'Toute','Half b: the initial T has the tall capital stem and broad top stroke; it is not the small t used inside the phrase.',kind='misread word',bbox=[365,700,655,777],source=half_b)
diff('Canceled b-case, dash before alors',r'\unsure{--}',r'\ill{}',r'--','A separate short horizontal mark lies below the long cancellation line between t.f. and alors. It is a dash, not merely part of the cancellation.',confidence='medium',kind='readable ink left as \\ill{}',marked='yes',change_c=True,crop=10)
diff('Corollary 3, canceled group after figures',r'\deleted{\unsure{de}}',r'\struck{\ill{}}',r'\deleted{\unsure{de|des}}','The first loop and small upper stroke support d. The rest is blackened by cancellation; the terminal curl can be e alone or an ending s, so de/des remains open.',confidence='low',kind='readable ink left as \\ill{}',marked='yes',change_c=True,crop=11)
diff('Corollary 3, family in its hypothesis',r'$\in\mathcal F$',r'$\in\mathfrak F$',r'$\in\mathcal F$','Half b and crop 12: the membership sign is open with an inner bar; the family capital has a looped upper stroke and turned lower stem.',kind='misread symbol or index',bbox=[278,877,391,958],source=half_b,math=True)
diff('Corollary 3, resp. finies insertion',r'\inserted{(resp. finies)}',r'(resp. finies)',r'\inserted{(resp. finies)}','The parenthesis is on the interlinear line directly above the canceled Alors il, not on the main baseline after t.f.',kind='insertion or placement',crop=12,math=True)
diff('Corollary 3, canceled Alors il',r'\deleted{Alors il}',r'\struck{\ill{}}',r'\deleted{Alors il}','The large initial A, low lors connection and final i/l strokes remain visible through one horizontal cancellation. They are below the inserted parenthesis.',kind='readable ink left as \\ill{}',marked='yes',crop=12)
diff('Corollary 3, two-bar shorthand',r'$\unsure{=|\text{même}}$',r'même',r'$=$','The mark consists of two separate approximately horizontal bars, the lower one with a turned left entry. No written letters of même occur here. I preserve the visible two-bar form.',kind='abbreviation expanded or spelling modernised',change_c=True,crop=13)
diff('Corollary 3, deleted de after the two-bar mark',r'\deleted{\unsure{de}}',r'',r'\deleted{\unsure{de}}','A separate canceled group follows the bars. Its first rounded d-like loop and terminal small oval support de, but the heavy strike prevents a fully secure reading.',confidence='low',kind='omission',crop=13)
diff('Corollary 3, family after pour',r'$\mathcal F_i$',r'$\mathfrak F_i$',r'$\mathcal F_i$','Half b: the same turned family F is followed by a distinct low i with its dot.',kind='misread symbol or index',bbox=[1110,915,1210,1000],source=half_b,math=True)
diff('Corollary 3, last-map alphabets',r'$\mathcal F\unsure{\text{---}|\longrightarrow}\prod\mathcal F_i$',r'$\mathfrak F\to\prod\mathfrak F_i$',r'$\mathcal F\unsure{\text{---}|\longrightarrow}\prod\mathcal F_i$','Both family capitals have the same looped or turned cursive form as above. The right-hand one has a separate low i. The product has two descending stems joined at the top.',kind='misread symbol or index',crop=14,math=True)
diff('Corollary 3, last-map connecting stroke',r'\unsure{\text{---}|\longrightarrow}',r'\to',r'\unsure{\text{---}|\longrightarrow}','The stroke is horizontal with a small downward terminal turn. It lacks the two clear arrowhead arms of the two upper maps. A rough arrow is possible but cannot be asserted from this crop.',confidence='low',kind='misread symbol or index',crop=14,math=True)
diff('Corollary 3, ens abbreviation stop',r"l'ens des",r"l'ens. des",r"l'ens des",'The terminal stroke of ens is followed by clear blank space and then des; no abbreviation stop is visible.',kind='other',crop=15)
diff('Corollary 3, final pres que spacing and tiny mark',r'pres que',r'presque',r'\unsure{pres|près|prés} que','There is a visible gap between the pres group and the long descending q of que. A very small isolated mark above the middle of pres may be an accent or a stray point; its direction is not securely readable. The spelling is therefore kept in two groups with the accent doubt explicit.',confidence='low',kind='abbreviation expanded or spelling modernised',change_c=True,crop=15)

c_doubts=[]
def doubt(location,c,reading,status,scan_shows,crop=None,bbox=None,source=None):
    cp=crop_by_number[crop] if crop else None
    c_doubts.append(dict(location=location,c=c,reading=reading,status=status,scan_shows=scan_shows,crop=cp['path'] if cp else None,bbox=bbox if bbox is not None else cp['bbox'] if cp else None,bbox_image=source or whole))

doubt('Opening, deleted formula',r'\unsure{F_i\in|F_i}',r'\unsure{F_i\in|F_i}','retained','F and i are visible; the membership-sized curved group meets the cancellation and possible opening parenthesis.',1)
doubt('Opening, opening parenthesis',r'\unsure{(}',r'\unsure{(}','retained','The curved stroke before the quantifier may belong to the old formula. The closing parenthesis is definite.',1)
doubt('Opening, overwritten family capital',r'\deleted{\unsure{\mathcal F}}',r'\deleted{\unsure{\mathcal F}}','retained','The old hooked upper arm survives beneath a reinforced plain F, but superposition obscures the full earlier capital.',2)
doubt('Opening, final low index or mark',r'\unsure{F_0|F}',r'\unsure{F_0|F}','retained','The low closed loop is definite; reading it specifically as an index zero remains less secure than its existence.',2)
doubt('Déjà paragraph, le/les',r'\unsure{le|les}',r'\unsure{le|les}','retained','The terminal bumps of the reinforced word do not securely distinguish singular from plural.',3)
doubt('C4, des/deux',r'\unsure{des|deux}',r'des','resolved','The ending has a short down-turn but no crossing that could supply x.',4)
doubt('Interlinear note, néc stop',r'\unsure{néc|néc.}',r'néc','resolved','The short abbreviation has no independent terminal dot after c.',5)
doubt('Interlinear note, deleted déd/val',r'\deleted{\unsure{déd|val}}',r'\unsure{validité|\deleted{déd} validité|\deleted{val} validité}','revised','The alleged deletion may be the reinforced vali beginning itself. All three state/readout possibilities are explicit in the transcription.',5)
doubt('Interlinear note, validité/déduction',r'\unsure{validité|déduction}',r'\unsure{validité|\deleted{déd} validité|\deleted{val} validité}','revised','The ending reads dité rather than duction; the remaining doubt concerns the reinforced first group and its state.',5)
doubt('Corollary 1, deleted pres',r'\deleted{\unsure{pres}}',r'\deleted{\unsure{pres}}','retained','A p-like descender and smaller loops remain, but the strike prevents fully secure pres.',6)
doubt('Corollary 2, canceled donc',r'\deleted{\unsure{donc}}',r'\deleted{donc}','resolved','The small initial looped d and lower onc group are visible beneath the heading underline.',7)
doubt('Corollary 2, supposed canceled f',r'\deleted{\unsure{f}}',r'\deleted{\unsure{suivants|suivants f}}','revised','The alleged f is at the end of the canceled suivants and can be its tall t and terminal s; a separate f remains only an alternative.',9)
doubt('Canceled b-case, dash',r'\unsure{--}',r'--','resolved','A short separate horizontal stroke can be seen beneath the much longer cancellation line.',10)
doubt('Corollary 3, deleted de after figures',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de|des}}','revised','The end is obscured enough to allow a final s; de remains first candidate.',11)
doubt('Corollary 3, two-bar sign',r'\unsure{=|\text{même}}',r'=','resolved','The visible object is two bars, with no letters. Its possible meaning is discussed separately from its transcription.',13)
doubt('Corollary 3, canceled de after two-bar sign',r'\deleted{\unsure{de}}',r'\deleted{\unsure{de}}','retained','The underlying d-like loop is visible but the small ending remains hidden by the thick strike.',13)
doubt('Corollary 3, last-map stroke',r'\unsure{\text{---}|\longrightarrow}',r'\unsure{\text{---}|\longrightarrow}','retained','The slight downward terminal turn does not provide an unambiguous arrowhead.',14)
doubt('Corollary 3, C_context spacing pres que',r'pres que',r'\unsure{pres|près|prés} que','revised','The inter-group gap is clear. A small isolated mark above the first group introduces an accent doubt not retained in C.',15)
doubt('C_context notation: individual and family F',r'F_i,\mathcal F_i',r'F_i,\mathcal F_i','resolved','The plain F has straight upper and middle bars; the family F has a hooked or looped top and turned stem. Each occurrence was checked in its half.',bbox=[485,237,705,315],source=half_a)
doubt('C_context notation: C4 variables and M',r'x,y\in M',r'x,y\in M','resolved','The two small variable forms and the larger plain M are distinct; no calligraphic M is present.',4)
doubt('C_context notation: empty-set sign',r'\varnothing',r'\varnothing','resolved','The page uses an oval crossed by a long oblique slash. The two glyph macros emptyset and varnothing in the witnesses were not counted as a separate semantic difference.',bbox=[1330,235,1462,327],source=half_b)

inventory=[]
def inv(element,kind,position,first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='handwritten manuscript leaf',hand='his hand',transcribed='yes'))
inv('Manuscript page number','pagination','Top centre, whole [682,45,763,101]','64')
inv('Opening question','text block','Whole [300,145,1647,515]','Inversement, donnons nous')
inv('Opening canceled formula','deletion','Whole [1310,151,1425,226]',r'F_i\in / F_i')
inv('Opening overwritten final capital','deletion and replacement','Whole [980,431,1065,508]',r'\mathcal F overwritten by F, low 0-like loop')
inv('Déjà paragraph','text block','Whole [294,526,1633,815]','Déjà, il le faudrait')
inv('Empty symbol before vides','deletion','Whole [295,725,361,814]',r'\varnothing')
inv('C4 statement','text block','Whole [285,850,1577,1137]','C4 Si x,y∈M')
inv('C4 heading underline','underline','Whole [285,942,433,963]','C4')
inv('Canceled Cor heading','deletion','Whole [302,1185,451,1257]','Cor')
inv('Small necessity/sufficiency sentence','insertion','Whole [555,1115,1448,1230]',"C'est néc et suffisant pour la ... des")
inv('Reinforced beginning in validity wording','possible deletion or overwrite','Whole [779,1184,900,1222]',r'vali / canceled déd / canceled val, explicit alternatives')
inv('Corollary 1','text block','Whole [302,1261,1631,1577]',"Corollaire 1 L'image de")
inv('Corollary 1 heading underline','underline','Whole [334,1347,582,1371]','Corollaire 1')
inv('sauf in Corollary 1','deletion','Whole [1503,1350,1630,1420]','sauf')
inv('pres in Corollary 1','deletion','Whole [511,1504,635,1557]','pres, uncertain')
inv('Corollary 2 heading','insertion','Whole [1135,1421,1311,1489]','Cor. 2')
inv('Corollary 2 placement bracket','insertion connector','Whole [878,1404,1338,1581]','Angular connector enclosing the inserted label; encoded by inserted placement, not an independent mathematical drawing')
inv('Corollary 2 heading underline','underline','Whole [1139,1471,1313,1490]','Cor. 2')
inv('donc under Corollary 2 label','deletion','Whole [1135,1483,1374,1519]','donc')
inv('Corollary 2 statement','text block','Whole [301,1444,1630,1717]',r'\mathcal F\to\prod\mathcal F_i est une bijection')
inv('Final portion of les in Corollary 2','possible deletion','Whole [1110,1550,1198,1591]','le with canceled s / live les')
inv('deux in Corollary 2','deletion','Whole [1286,1555,1434,1592]','deux')
inv('suivants in Corollary 2','deletion','Whole [294,1643,624,1724]','suivants / suivants f')
inv('Finite-index replacement','insertion','Whole [364,1627,742,1692]','I est fini.')
inv('Canceled a-case','deletion block','Whole [342,1723,739,1804]','a) I est fini')
inv('Canceled b-case','deletion block','Whole [373,1751,1621,1871]','b) Toute figure est de t.f. -- alors')
inv('Corollary 3','text block','Whole [284,1829,1630,2304]','Cor 3 Supposons que les figures')
inv('Corollary 3 heading underline','underline','Whole [294,1934,461,1963]','Cor 3')
inv('Group after figures','deletion','Whole [1538,1839,1628,1881]','de / des')
inv('Old Alors il in Corollary 3','deletion','Whole [892,1951,1171,2015]','Alors il')
inv('Finiteness parenthesis','insertion','Whole [850,1906,1206,1981]','(resp. finies)')
inv('Two-bar repetition shorthand','notation in text','Whole [610,2061,687,2104]','=')
inv('Group after two-bar sign','deletion','Whole [763,2059,861,2095]','de, uncertain')

remaining=[
    dict(location='Opening deletion',reading=r'\deleted{$\unsure{F_i\in|F_i}$}',alternatives=[r'F_i\in',r'F_i'],confidence='low',reason='The cancellation meets the curved mark before the quantifier.'),
    dict(location='Opening quantifier',reading=r'\unsure{(}\forall i\in I)',alternatives=['opening parenthesis present','opening parenthesis absent; curve belongs to deletion'],confidence='low',reason='A closing parenthesis is definite, but its expected mate must not be supplied from symmetry.'),
    dict(location='Opening corrected final capital',reading=r'\deleted{\unsure{\mathcal F}}',alternatives=[r'old \mathcal F','unidentified old F-form'],confidence='low',reason='The old hooked arm is visible, but superposition hides the full old glyph.'),
    dict(location='Opening final low mark',reading=r'\unsure{F_0|F}',alternatives=[r'F_0',r'F with stray or punctuation-like low loop'],confidence='low',reason='The closed loop is visible; its function as an index is not certain.'),
    dict(location='Déjà paragraph before cas',reading=r'\unsure{le|les}',alternatives=['le','les'],confidence='low',reason='The reinforced ending permits either letter count.'),
    dict(location='Interlinear note after pour la',reading=r'\unsure{validité|\deleted{déd} validité|\deleted{val} validité}',alternatives=['validité with a reinforced beginning','canceled déd before corrected validité','canceled val before corrected validité'],confidence='low',reason='The baseline stroke may be the word connection rather than cancellation; the dité ending is clearer than the beginning.'),
    dict(location='Corollary 1 before que tout i',reading=r'\deleted{\unsure{pres}}',alternatives=['pres','another short canceled p-initial group'],confidence='low',reason='The crossed p and loops survive, but not all letters are individually secure.'),
    dict(location='Corollary 2 after dans',reading=r'\unsure{le\deleted{s}|les}',alternatives=['le with canceled s','live les'],confidence='low',reason='The end is heavily retraced; only one l-e group exists, so C’s two complete words overstate the visible duplication.'),
    dict(location='Corollary 2 canceled suivants ending',reading=r'\deleted{\unsure{suivants|suivants f}}',alternatives=['suivants','suivants followed by a canceled f'],confidence='low',reason='The alleged f is at the same position as the tall t/s ending of suivants.'),
    dict(location='Corollary 3 after figures',reading=r'\deleted{\unsure{de|des}}',alternatives=['de','des'],confidence='low',reason='The ending is buried under a heavy stroke, and the rightmost curl allows an s.'),
    dict(location='Corollary 3 after the two-bar sign',reading=r'\deleted{\unsure{de}}',alternatives=['de','unidentified short d-initial group'],confidence='low',reason='Only the initial loop and a small terminal oval are visible through the strike.'),
    dict(location='Corollary 3 last map',reading=r'\unsure{\text{---}|\longrightarrow}',alternatives=['plain horizontal stroke','rough right arrow'],confidence='low',reason='The end turns down, but lacks a definite arrowhead.'),
    dict(location='Final pres que',reading=r'\unsure{pres|près|prés} que',alternatives=['pres que','près que','prés que'],confidence='low',reason='The tiny isolated mark above pres may be stray or an accent; there is no secure accent direction.'),
]

notation=[
    dict(sign='Individual figure F',latex=r'F, F_i',appearance='Straight upper and middle bars, unlike the family capital.',location='Opening question and all tuples/components.',alternatives=[]),
    dict(sign='Family F',latex=r'\mathcal F,\mathcal F_i',appearance='Hooked or looped upper stroke and turned stem; no Gothic construction.',location='Opening membership formulas, three corollaries.',alternatives=[]),
    dict(sign='Underlying corrected family F',latex=r'\deleted{\unsure{\mathcal F}}',appearance='Hooked arm surviving under reinforced plain F.',location='End of opening question.',alternatives=['old unidentified F-form']),
    dict(sign='Low loop after corrected F',latex=r'\unsure{F_0|F}',appearance='Small closed loop with a lower-left tail at subscript height.',location='End of opening question.',alternatives=['subscript zero','stray or punctuation-like mark']),
    dict(sign='C4 variables and space',latex=r'x,y\in M',appearance='Small crossed x, short forked y, plain larger M, open membership sign with inner bar.',location='C4.',alternatives=[]),
    dict(sign='Quantifier',latex=r'\forall',appearance='Two opening arms with a transverse bar.',location='Opening question twice.',alternatives=[]),
    dict(sign='Product',latex=r'\prod',appearance='Two long descending stems below a top bar.',location='Three map expressions.',alternatives=[]),
    dict(sign='Empty set',latex=r'\varnothing',appearance='Small oval crossed by a long rising oblique slash.',location='Déjà paragraph, Corollary 1 and Corollary 3.',alternatives=[]),
    dict(sign='Clear arrows',latex=r'\to',appearance='Horizontal shaft with visible convergent head strokes.',location='Corollaries 1 and 2.',alternatives=[]),
    dict(sign='Last map stroke',latex=r'\unsure{\text{---}|\longrightarrow}',appearance='Horizontal line ending in a short downward turn.',location='Corollary 3.',alternatives=[r'\text{---}',r'\longrightarrow']),
    dict(sign='Two-bar shorthand',latex=r'=',appearance='Two separate horizontal bars, lower left end curved slightly upward.',location='Corollary 3 after en est de.',alternatives=['May mean même in context; that expansion is not written.']),
]
abbreviations=[
    dict(form='nb',expansion='nombre'),
    dict(form='comp.',expansion='composantes'),
    dict(form='néc',expansion='nécessaire'),
    dict(form='Cor / Cor.',expansion='Corollaire'),
    dict(form='t.f.',expansion='type fini'),
    dict(form='resp.',expansion='respectivement'),
    dict(form='ens',expansion='ensemble'),
    dict(form='=',expansion='possibly même; retained as a two-bar sign in the transcription'),
]

evidence_notes=[
    'F_i and the old deletion are visible; membership versus bracket remains unresolved. Closing parenthesis definite.',
    'An old hooked F-form is overwritten. The low closed loop favours subscript 0 but its role remains doubtful.',
    'le/les remains unresolved. The lower context clearly has un nb fini sont.',
    'Plain M and lower-case x/y confirmed. des has no crossed x; disjointes has its descending j.',
    'néc has no independent final stop. dité is visible; the vali-like cluster may be retraced rather than a separate canceled word.',
    'Crossed pres remains doubtful. The live que tout i. is clear, with a gap before q.',
    'Inserted underlined Cor. 2 and canceled lower-case donc. The map has a clear head; family capitals are cursive.',
    'Only one l-e group is present; the end may be a canceled s or live s. deux is independently canceled.',
    'I est fini. lies above canceled suivants. The supposed separate f can be the old word’s t/s ending.',
    'A short dash is distinct below the long cancellation line, before alors.',
    'After figures a canceled d-initial group remains; de/des are both possible.',
    'soient, t.f., inserted (resp. finies) and canceled Alors il verified.',
    'Two bars, not letters of même. Following canceled de remains uncertain.',
    'Final connecting mark has a downward hook, not a definite arrowhead. The families and low index i are visible.',
    'No stop after ens. pres and que are visibly separated; tiny mark over pres may be stray or an accent.',
]

report=dict(
    reader='R1',cote='156-4',scan='065',brief_version='v01',
    started_utc='2026-11-20T08:57:46Z',
    finished_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    image_views=[whole,half_a,half_b],reading_file=str(out/'reading.tex'),
    differences=differences,c_doubts=c_doubts,inventory=inventory,remaining_doubts=remaining,
    notation=notation,abbreviations=abbreviations,
    notes=dict(
        summary='Independent full-page reading: one whole-page view, then one view of each supplied half in order, then 15 own tight crops. C and H were checked against every manuscript line. No other reader material, other scan, OCR, external source, or research was used. The main H errors occur in the opening question, the Déjà paragraph, the final condition of Corollary 1, and correction states. C remains close overall but has several unresolved or revised state readings. Differences in equivalent macro names alone were not counted; marked_in_h means H signals uncertainty/unread text or explicitly annotates the relevant issue, not merely that it uses a deletion macro.',
        math_reading_decisions='No theorem or corollary was proved. Recognizing that three written expressions refer to a family/product map prompted scrutiny of the last short connector; the expected map did not supply an arrowhead. In C4 the visible word des was selected from its final stroke, not from a claim about components. The visible two-bar sign was kept without expanding it to même. No mathematical correctness assumption was used to repair the page.',
        author_checks='No explicit author proof-check annotation is present. C4 and the three corollaries are transcribed as written, with the old lettered cases canceled. The interlinear necessity/sufficiency statement is partly uncertain in its correction state. Cancellations and insertions are recorded, not interpreted as validation of the assertions.',
        title_dates_pagination='The top-centre handwritten page number is 64; the scan is 65. No title, date, archive sheet number, stamp, or stated page total is visible on this leaf. No independent mathematical diagram or drawing is present. The angular mark around Cor. 2 is an insertion connector; its role is encoded by the inserted heading and described in the inventory, rather than treated as a mathematical drawing.',
    ),
    check_events=[],crops=manifest,
    workflow_feedback=[
        'For highly superposed writing, a single crop may settle the letters but not whether a connecting baseline is cancellation or retracing; the validity cluster remains explicitly open for that reason.',
        'The requested bbox field lacks an explicit image-name slot, so bbox_image has been added to every difference and C-doubt item. Coordinates refer to that exact original image, never to the enlarged crop.',
        'The brief should clarify whether insertion brackets must be reproduced as drawings; this report treats the Cor. 2 bracket as placement apparatus rather than an independent diagram.'
    ],
)
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

lines=[
    '# R1 inspection log — 156-4 scan 065',
    '',
    'Brief v01. Started UTC: 2026-11-20T08:57:46Z. All inspections were visual; no OCR/text recognition was run.',
    '',
    '## Ordered image views',
    '',
    f'1. `{whole}` — whole page, once, unmodified. Layout: page number; opening question; Déjà paragraph; C4; interlinear addition and canceled Cor; Corollary 1; inserted Cor. 2 with placement bracket; canceled lettered cases; Corollary 3. No margin note or independent diagram.',
    f'2. `{half_a}` — supplied full-resolution first half, once, no enlargement or transformation. Every line checked against C and H, including agreed formulas and punctuation.',
    f'3. `{half_b}` — supplied full-resolution second half, once, no enlargement or transformation. Every line checked against C and H, including the overlapped interlinear note and all canceled cases.',
]
for i,(crop,note) in enumerate(zip(manifest,evidence_notes),start=4):
    lines.extend(['',f'{i}. `{crop["path"]}`',f'   - Source: `{crop["source"]}`; original bbox {crop["bbox"]}.',f'   - Scale {crop["scale"]:.9f}; rotation {crop["rotation"]} degrees; {crop["transforms"]}.',f'   - Reason: {crop["reason"]}',f'   - Visible evidence/decision: {note}'])
lines.extend([
    '', '## Line-by-line coverage of agreed and disputed text', '',
    '- Opening line 1: Inversement, donnons nous, old formula, quantifier and closing parenthesis; no hyphen silently added to donnons nous.',
    '- Opening line 2: un F_i in the cursive family F_i, comma, quand peut-on dire.',
    '- Opening line 3: qu’il existe F in the cursive family F, telle que, second universal quantifier, F_i soit.',
    '- Opening line 4: la i composante de, overwritten final F and low mark, question mark; no hyphen before composante.',
    '- Déjà lines: Déjà, il le faudrait pour le/les cas; où tous les F_i sauf un nb fini sont; canceled empty sign, vides. On va supposer donc. Accents, stops and the absent terminal stop after donc were checked.',
    '- C4 lines: underlined C4; Si x,y∈M appartiennent à des; comp. connexes disjointes de M, alors; x et y sont compatibles. Lower-case variables and plain M checked independently of H.',
    '- Interlinear material: canceled Cor; C’est néc et suffisant pour la; validity cluster and des. No extra terminal word added from H.',
    '- Corollary 1 lines: underlined heading; L’image de cursive-family map; contient les (F_i)_{i∈I} tels que F_i=empty; canceled sauf; pour canceled pres, que tout i. Tuple indices, product sign and arrowhead checked.',
    '- Corollary 2: inserted underlined Cor. 2; lower-case canceled donc; cursive-family map with arrowhead; est une bijection dans; disputed le/les correction; canceled deux; cas où; canceled suivants with doubtful extra f; upper I est fini. and final stop.',
    '- Canceled cases: a) I est fini; b) Toute figure est de t.f. -- alors. Each initial, formula, abbreviation, dash and whole-line cancellation checked; no colon or semicolon supplied.',
    '- Corollary 3 first lines: underlined Cor 3; Supposons que les figures; canceled de/des; membership and cursive family F; soient de t.f.; canceled Alors il; interlinear (resp. finies); stop; live Alors il en.',
    '- Corollary 3 remaining lines: est de two-bar sign; canceled de; pour cursive F_i, de plus; cursive family/product expression with doubtful connector; a comme image l’ens des; (F_i) tels que F_i soit empty pour pres/près/prés que tout i. Commas, final stop, low indices and the absence of an ens stop checked.',
    '', 'No place was recropped after decision, and neither full half was displayed a second time. The overlapping context within tight crops was used only to identify the local disputed marks. All 15 crops were created in one script before crop inspection; no second-stage or replacement crops were made.',
    '', f'Final report: {len(differences)} difference records, {len(c_doubts)} C-doubt/notation checks, {len(remaining)} remaining doubts, {len(manifest)} crops.',
])
(out/'inspection_log.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(dict(differences=len(differences),c_doubts=len(c_doubts),remaining_doubts=len(remaining),inventory=len(inventory),crops=len(manifest)),ensure_ascii=False))
