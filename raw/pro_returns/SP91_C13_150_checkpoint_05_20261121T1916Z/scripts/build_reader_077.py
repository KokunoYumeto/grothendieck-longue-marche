from pathlib import Path
import json, os, re
BASE=Path('/workspace/scratch/b12af914b284')
M=json.loads((BASE/'edition/scripts/150_scan077_crop_index.json').read_text())
CP={i:c for i,c in enumerate(M['crops'])}
V=r'{\unsure{V|\mathcal V}}'
C=(BASE/'input/SP91_C13_150_texts/pages/150_scan077.tex').read_text()
H=(BASE/'input/SP91_C13_150_texts/hua/hua_150_scan077.tex').read_text()
rows=[]
def ch(place,c,h,final,ac,ah,kind,cat,confidence,evidence,p,marked=False,consequence=''):
    rows.append(dict(id=f'077-{len(rows)+1:02d}',place=place,C=c,H=h,final=final,against_C=ac,against_H=ah,kind=kind,error_category=cat,marked_in_H=marked,confidence=confidence,evidence=evidence,crop=CP[p]['file'],box=CP[p]['box'],mathematical_consequence=consequence))
def font(place,c,h,final,p,evidence):
    ch(place,'V',r'\mathcal V',V,False,True,'misread symbol or index','Symbols and indices','low',evidence+' Plain V is the leading typographic candidate; calligraphic V remains explicitly open. This row compares only the base alphabet with H, without resolving it; other local symbols and revisions have separate rows.',p)
ch('Heading, item 15',r'\uline{15}.','15.',r'\uline{15}.',False,True,'other','Other','high','A separate heavy line extends under the two digits and ends before the detached full stop.',0)
ch('Heading, words proespaces/provoisinages','proespaces','provoisinages','proespaces',False,True,'misread word','Words','high','After pro, the pen makes the low e/s sequence and a descending p, followed by aces; the written word is proespaces.',1)
ch('Heading, underline scope','Introduction des proespaces',r'\emph{Introduction des provoisinages}','Introduction des proespaces',False,True,'other','Other','high','No separate line runs under the heading words. The two bars on the initial I belong to that letter; the actual item-number underline is isolated to the left.',1)
font('Heading, both V bases',r'V_{i_0\ldots i_n},\ V_J',r'$\mathcal V_{i_0\ldots i_n}$, $\mathcal V_J$',V+r'_{i_0.\!-.i_n},\ '+V+r'_J',2,'Both bases have a descending curved left arm and a rounded bowl; the first has a looped upper-right return and the second a flatter cap.')
ch('Heading, continuation inside first subscript',r'i_0\ldots i_n',r'i_0\ldots i_n',r'i_0.\!-.i_n',True,True,'misread symbol or index','Symbols and indices','high','Between the initial i with round lowered 0 and the final dotted i/n are a point, a short horizontal dash, and a point, visibly separated.',2)
ch('Heading, live raised L beside the crossed mark',r'\deleted{\unsure{*}}\unsure{L}',r'un petit exposant biffé (une étoile ?)',r'\deleted{\unsure{*}}L',False,True,'omission','Omissions','high','To the right of the crossed raised cluster is a distinct tall upright with a broad rightward horizontal foot. The earlier cluster remains a masked star candidate. H describes only a small crossed exponent.',2,True)
font('Designation, V_i base',r'V_i^{\unsure{\deleted{*}|*}}',r'\mathcal V_i',V+r'_i^{\unsure{*|<|\deleted{*}}}',3,'The base has an arched left entry, a rounded bottom, and an upper-right sloping return; i has a separate point and short curved foot.')
ch('Designation, raised glyph and strike state',r'\unsure{\deleted{*}|*}',r'un petit exposant biffé (une étoile ?)',r'\unsure{*|<|\deleted{*}}',True,True,'deletion state','Struck text','low','The raised dark group exposes a left vertex, two nearly parallel upper/right rays and a dense lower mass. A star, a left-angle form, and a struck star remain open; no independent strike can be isolated securely from the merged strokes.',3,True)
ch('Designation, crossed le',r'\unsure{\deleted{le}|le}',r'\struck{\ill{}}',r'\unsure{\deleted{le}|le}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','low','A tall looped l and a low e-like continuation remain under a nearly horizontal stroke which extends beyond the right fragment. Deletion leads, but the merged low bodies and live alternative remain explicit.',3,True)
ch('Parenthesis au sens des proespaces','proespaces','provoisinages','proespaces',False,True,'misread word','Words','high','The same pro-e/s-p-aces run is visible between the written des and the closing parenthesis.',4)
ch('After Ainsi, crossed group',r'\deleted{\unsure{on}}',r'\struck{\ill{}}',r'\deleted{\unsure{on}}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','low','A continuous dark horizontal strike masks a short low word. Small rises survive beneath it; on is retained as a doubtful reading rather than completed with certainty.',6,True)
ch('After the crossed group, live on a','on a','(absent)',r'\unsure{on a}',False,True,'omission','Omissions','low','Three separate foreground groups follow the strike: a filled round o-like mark, a shallow n-like arch, and a small a-like blot. Their compressed form is explicitly doubtful.',6)
font('Display (51), target V_i',r'V_i^{\unsure{\deleted{*}|*}}',r'\mathcal V_i',V+r'_i^{\unsure{*|\deleted{*}}}',7,'The target base has a tall left arc and a rounded bowl with a right upper return; its dotted i is separate.')
ch('Display (51), target exponent and strike state',r'\unsure{\deleted{*}|*}',r'un petit exposant biffé (une étoile ?)',r'\unsure{*|\deleted{*}}',True,True,'deletion state','Struck text','low','Several short outward star spurs remain around a dense raised centre. The centre is overdrawn, but a distinct crossing stroke cannot be separated securely; live star leads with the struck reading retained.',7,True)
ch('Display (51), written line-end hyphen',"équivalence d'homotopie", "équivalence d'homotopie", "équivalence d'homo- / topie",True,True,'other','Other','high','A short horizontal stroke follows homo at the physical right edge, and topie begins the next written line. The transcription retains that hyphen and line division.',8)
ch('Display (51), caption de/des','de','des',r'\unsure{des|de}',True,False,'misread word','Words','low','After the tall looped d is a low run ending in a downward s-like curl, comparable to the definite des in the earlier parenthesis. The e/s segmentation remains compressed, so de stays open. This row compares only the small de/des group; the following noun has its own row.',8)
ch('Display (51), caption proespaces/provoisinages','proespaces','provoisinages','proespaces',False,True,'misread word','Words','high','The caption repeats the low pro-e/s sequence followed by the descending p and the compact aces ending.',8)
ch('Condition below the cancelled line, stroke after Si','Si','Si',r'Si\unsure{)}',True,True,'omission','Omissions','medium','Immediately right of the separately dotted i is a distinct long curved stroke shaped like a closing parenthesis. The far-left loop belongs to the descending cancelled P above; no matching opening is supplied.',9)
font('Display (52), right-hand V_i and V_j',r'V_i\cap V_j',r'\mathcal V_i\cap \mathcal V_j',V+r'_i\cap '+V+r'_j',10,'Both right-hand bases have rounded bowls, high entry strokes and upper-right caps. The first subscript is dotted i; the second is a long j with a leftward foot.')
ch('Display (52), single overwritten left base and shared ij',r'\deleted{X_{ij}}\inserted{V_{ij}}',r'\mathcal V_{ij}',r'\unsure{\rlap{$X$}V|\rlap{$X$}\mathcal V}_{ij}',True,True,'insertion or placement','Insertions put in the wrong place','low','Two crossing diagonal strokes overlap the rounded V-shaped bowl at one position. One dotted i and one long j follow the whole cluster. The temporal order and cancellation state are not separable; the return superposes X and V with a single shared index instead of asserting two separately indexed objects.',10,False,'The manuscript retains one reworked base with the written shared ij; its live letter is not established by a mathematical inference.')
ch('Left oblique note, opening words','Pourquoi',r'Pour un \ill{}','Pour un',True,True,'misread word','Words','medium','A tall P is followed by a low our-like run; a separate low un cluster follows. No recoverable q descender or dotted terminal i appears. Between un and the formula there is no additional word-sized ink for H\'s placeholder.',11,True)
font('Left oblique note, V bases',r'V_{ij}^{\unsure{b}}=V_i',r'\mathcal V_{ij}^{\ill{}}=\mathcal V_i',V+r'_{ij}^{\unsure{b}}='+V+r'_i',11,'The first base has two curved upright arms and the second a simpler U-shaped bowl; the i/j strokes remain separate below.')
ch('Left oblique note, superscript candidate b',r'\unsure{b}',r'\ill{}',r'\unsure{b}',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','low','The raised glyph has an oblique upper stem and a compact doubled lower bend/loop. b remains a supported candidate, with its exact contour unresolved.',11,True)
ch('Left oblique note, X_j star and terminal hook arrow',r'V_i\cap X_j^*\arrow[r,hook]',r'\mathcal V_i\cap$ \ldots\ équivalence',V+r'_i\cap X_j^*\arrow[r,hook]&{}',False,True,'omission','Omissions','high','After the intersection arch are an X, a long hooked lower j and a small raised star. The following connector has a curved source hook, a short shaft and a rounded returning terminal head.',11,True)
ch('Left oblique note, supplied target',r'\unsure{V_{ij}}','(absent)','(no written target)',True,False,'text not on the page','Text that is not on the page','high','The written connector ends after its curved terminal head. No independent V, i or j target group is visible beyond it in the inspected crop and the whole-page review.',11)
ch('Left oblique note, est-ce une',r'\unsure{est une|est-ce une}',r'\ldots\ équivalence',"est-ce une équivalence",True,True,r'readable ink left as \ill{}','Readable ink left as illegible','medium','The est run ends in a tall t; a separate short horizontal hyphen and a compact ce cluster precede the low repeated humps of une.',11,True)
ch('Right NB, underline scope','NB',r'\emph{NB}','NB',False,True,'other','Other','high','The N and B have no independent underline below them. The lower diagonal is the B\'s own closing stroke.',12)
font('Right NB, the five V occurrences',r'$V_{ij}$',r'$\mathcal V_{ij}$',V+r'_{ij}; '+V+r'_i\cap '+V+r'_j; '+V+r'_{ii}='+V+r'_i',12,'The note repeats curved, U-like bowls with varying upper curls in V_ij, V_i, V_j and the final V_ii=V_i.')
ch('Right NB, crossed si before live si',r'\deleted{\unsure{si}} si','a un sens si',r'\deleted{\unsure{si}} si',False,True,'omission','Omissions','low','A short crossed group appears after sens and before the live dotted si. Its low body is masked by a dark horizontal stroke and touched by the long j from the preceding line; si remains doubtful.',12,True)
ch('Right marginal insertion, du moins','du moins',r'\ill{}','du moins',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','medium','The parenthesis opens before a looped d and low u, then a compressed m/o/i run and a reworked ns ending. The following dotted si is separate.',13,True)
ch('Right marginal insertion, attachment',r'\inserted{(du moins si les ouverts de $X$ sont normaux, p.ex. $X$ métrisable)} si $i=j$',r'$\mathcal V_{ii}=\mathcal V_i$ (\ill{} si les ouverts de $X$ sont normaux, p.ex.\ $X$ métrisable)',r'\inserted{(du moins si les ouverts de $X$ sont normaux, p.ex. $X$ métrisable)} si $i=j$',False,True,'insertion or placement','Insertions put in the wrong place','high','The continuous curved leader begins by the intersection-empty clause and descends to the opening parenthesis of the added text. Its physical position below the final equality does not move its attachment after that equality.',13,True)
font('Central diagram, the three V nodes',r'V_{ij}',r'\mathcal V_{ij}',V+r'_{ij},\ '+V+r'_j,\ '+V+r'_i',14,'All three nodes use the same rounded bowl construction, with open or looped upper returns; the subscripts are separately written.')
ch('Central diagram, horizontal source hook',r'\arrow[r,"b_{ij}"]',r'\arrow[r, "b_{ij}"]',r'\arrow[r,hook,"b_{ij}"]',True,True,'drawing or diagram','Drawings and diagrams','high','The horizontal shaft starts with a separate curved upward hook on the left and ends with a rounded two-arm head on the right; b_ij sits above.',14,False,'A source hook is visibly part of the manuscript connector labelled b_ij.')
ch('Central diagram, s_ij placement',r'\arrow[d,hook,"s_{ij}"]',r'''\arrow[d, hook, "s_{ij}"']''',r'\arrow[d,hook,"s_{ij}"]',False,True,'drawing or diagram','Drawings and diagrams','high','The s_ij label is written to the right of the thick downward shaft, whose upper endpoint is hooked and whose lower endpoint has a full arrowhead.',14)
ch('Lower diagram, upper label',r'\unsure{(w)|(h)}',r'(h)',r'\unsure{(w)|(h)}',False,True,'misread symbol or index','Symbols and indices','low','Inside the small parentheses, the stem and two low turns support w as the leading reading; the tall first stroke also leaves h possible. Neither letter is inferred from the displayed map.',14)
ch('Lower diagram, single tilde',r'\sim',r'\approx',r'\sim',False,True,'misread symbol or index','Symbols and indices','high','A single wavy horizontal stroke is written below the parenthesized label; there is no second parallel wave.',14)
ch('Lower diagram, dense left-pointing mark',r'\deleted{\longleftarrow}','(absent)',r'\unsure{\longleftarrow|\deleted{\longleftarrow}}',True,True,'deletion state','Struck text','low','A short dense left-pointing mark sits above a separate right arrow. Its head and thick shaft are visible; an independently crossing deletion stroke cannot be isolated, so live and struck states remain open.',14)
ch('Lower diagram, closing parenthesis position',r')V_i',r'\mathcal V_i\bigr)',r'\Bigr)'+V+r'_i',False,True,'insertion or placement','Insertions put in the wrong place','high','The tall closing parenthesis lies between the two lower arrows and V_i. V_i is outside it and directly below the vertical arrow.',14)
font('Display (53), V_i and V_ij',r'V_i,V_{ij}',r'\mathcal V_i,\ \mathcal V_{ij}',V+r'_i,'+V+r'_{ij}',15,'The two bases have the same rounded bowls as elsewhere; their separate lower i and ij groups are visible inside the parenthesis.')
ch('Display (53), crossed brace-like group',r'\unsure{\deleted{\}}|\rightrightarrows}',r'\rightrightarrows',r'\unsure{\deleted{\}}|\}}',False,True,'misread symbol or index','Symbols and indices','low','The vertical group has an upper bend, a central rightward angular turn and a lower leftward sweep. Diagonal/retraced strokes cross its upper portion. The brace-like shape and its strike state remain doubtful; no pair of horizontal shafts with right heads is recoverable.',15,False,'The literal reworked brace-like mark is retained within the author\'s displayed colimit expression; no mathematical replacement is made.')
font('Recollement sentence, V_i and V_ij',r'$V_i$ suivant les $V_{ij}$',r'$\mathcal V_i$ suivant les $\mathcal V_{ij}$',V+r'_i\text{ suivant les }'+V+r'_{ij}',16,'The first base has a simple right cap; the lower V_ij has an open high left curve and a sloping right return, both with rounded bowls.')
font('Display (54), all three V bases',r'V_{i_0\ldots i_n}=V_{i_0}\cap\ldots\cap V_{i_n}',r'\mathcal V_{i_0\ldots i_n}=\mathcal V_{i_0}\cap\cdots\cap \mathcal V_{i_n}',V+r'_{i_0.\!-i_n}='+V+r'_{i_0}\cap\mathord{-}\,\mathord{-}\cap '+V+r'_{i_n}',17,'The first base has a looped upper return; the middle one is a simple curved bowl; the last is heavily retraced, with no independently recoverable underlying letter.')
ch('Display (54), left subscript continuation',r'i_0\ldots i_n',r'i_0\ldots i_n',r'i_0.\!-i_n',True,True,'misread symbol or index','Symbols and indices','high','One point followed by one short horizontal dash lies between the initial i_0 and final i_n.',17)
ch('Display (54), right continuation',r'\cap\ldots\cap',r'\cap\cdots\cap',r'\cap\mathord{-}\,\mathord{-}\cap',True,True,'misread symbol or index','Symbols and indices','high','Two separately written short horizontal dashes lie between the two intersection arches. The first is slightly shorter.',17)
ch('Last main line, flag continuation',r'i_0<i_1<\ldots<i_n',r'i_0<i_1<\cdots<i_n',r'i_0<i_1<.\!-<i_n',True,True,'misread symbol or index','Symbols and indices','high','After the second less-than sign are one dot and one short dash before the final less-than sign. The lowered numerals 0 and 1 are individually visible.',18)
ch('Bottom NB, = si l\'ens.',r"\unsure{même} si l'ens.",r'pour $(i_0,\ldots,i_n)$',r"$=$ si l'ens.",True,True,'abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised','high','After a un sens are two horizontal strokes, the lower slightly wavy, followed by dotted si. The next line begins l\'ens. with a written full stop. No letters même are supplied.',19)
ch('Bottom NB, set delimiters',r'\{i_0,\ldots,i_n\}',r'(i_0,\ldots,i_n)',r'\{i_0,\mathord{-}i_n\}',False,True,'misread symbol or index','Symbols and indices','high','The left delimiter has an upper curved entry and a middle inward kink; the right delimiter has the complementary two-bend brace contour.',19)
ch('Bottom NB, single index-continuation dash',r'i_0,\ldots,i_n',r'i_0,\ldots,i_n',r'i_0,\mathord{-}i_n',True,True,'misread symbol or index','Symbols and indices','high','A separate comma follows i_0; then one long horizontal dash precedes the dotted i/n group. There is no second comma after the dash.',19)
ch('Bottom NB, ne forme pas un drapeau','ne forme pas un drapeau','quelconque','ne forme pas un drapeau',False,True,'misread word','Words','high','The low ne run is followed by a tall looped f with a descending return and the forme continuation; the next line has pas un drapeau with a visible comma at its edge.',19)
ch('Bottom NB, il est','mais il est vide',r'mais \ill{} vide','mais il est vide',False,True,r'readable ink left as \ill{}','Readable ink left as illegible','high','Between mais and vide are a separately dotted i, a tall l, and the low est run ending in a raised t.',19,True)
ch('Bottom-left other-hand foliation',r'\mspage{76}','(absent)',r'\margin{76}',False,True,'omission','Omissions','high','A pale 7 with a crossing bar and a rounded 6 stand at the bottom-left paper edge in another hand. The macro change records hand/placement rather than a changed numeral.',20)
# One record for each packet mark, in packet order.
decisions=[]
def decision(mid,status,reading,p,confidence,evidence):
    decisions.append(dict(id=mid,decision=status,reading=reading,evidence=evidence,crop=CP[p]['file'],box=CP[p]['box'],confidence=confidence))
decision('M0649','first','L',2,'high','The right-hand raised glyph has a tall retraced upright and a broad rightward foot, distinct from the crossed group on its left.')
decision('M0650','undecided',r'\unsure{*|<|\deleted{*}}',3,'low','A left vertex, two upper/right rays and dense lower ink admit star and left-angle readings. The deletion state is inseparable from the overdrawn body.')
decision('M0651','undecided',r'\unsure{\deleted{le}|le}',3,'low','A separate nearly horizontal stroke crosses the low bodies and extends beyond the right fragment. The l loop and e-like continuation survive, but the mask leaves both lexical recovery and live/struck state incompletely secure; deletion leads.')
decision('M0652','undecided',r'\unsure{*|\deleted{*}}',7,'low','The raised dense centre has outward star spurs. Overdraw is evident, while an independently separable crossing line is not; the strike alternative stays open.')
decision('M0653','undecided',r'\unsure{b}',11,'low','A raised oblique stem and a compact doubled lower turn support b without settling the exact contour.')
decision('M0654','other',r'\arrow[r,hook]&{}',11,'high','The curved head ends the written connector. No separate target letters follow it; the proposed diagram leaves that endpoint unlabeled.')
decision('M0655','alternative','est-ce une',11,'medium','A short separate hyphen follows the high t of est; a compact ce cluster precedes the repeated low humps of une.')
decision('M0656','undecided',r'\unsure{(w)|(h)}',14,'low','The first tall stroke and two low turns favour w, while h remains possible. The parentheses and the separate single tilde are visible.')
decision('M0657','undecided',r'\unsure{\deleted{\}}|\}}',15,'low','The group is vertical and brace-like, with a rightward middle turn and leftward lower sweep. Its upper strokes are crossed/retraced; the live/struck alternatives remain. A pair of right arrows is not recovered from the visible strokes.')
decision('M0658','other','=',19,'high','Two separate horizontal strokes occur after a un sens; the lower is slightly wavy. The literal sign is retained, with même entered only as an abbreviation expansion.')
decision('M0659','first','ce',19,'medium','The compact low c/e group stands between the separately dotted si and the taller n\'est sequence.')

inventory=[]
def inv(kind,position,first,hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
inv('text','upper-left, above the heading','34')
inv('text','heading across the top',r'\uline{15}. Introduction des proespaces : '+V+r'_{i_0.\!-.i_n}, '+V+r'_J')
inv('deletion','heading, raised group before L; earlier glyph masked',r'\deleted{\unsure{*}}')
inv('insertion','heading, live raised L immediately right of the crossed group','L; replacement relation retained as position, with no independent leader')
inv('text','three opening main baselines','On désigne par ... voisinage tubulaire (au sens des proespaces) de X_i^*=X_i ... dans X.')
inv('deletion','opening line after V_i; deletion leads but live state remains open',r'\unsure{\deleted{le}|le}')
inv('insertion','above voisinage, curved leader ending before its first letter',r'\inserted{pro}')
inv('deletion','after Ainsi, before the surviving short live groups',r'\deleted{\unsure{on}}')
inv('text','immediately after the crossed on',r'\unsure{on a}')
inv('display','display (51) and its two-line right caption',r'(51) X_i^*\longrightarrow '+V+r'_i^{\unsure{*|\deleted{*}}}; équivalence d’homo- / topie ...')
inv('deletion','separate cancelled line before Si',r'\deleted{\unsure{Pour un drapeau}}')
inv('text','line below the cancelled phrase',r'Si\unsure{)} $i<j$, on pose')
inv('display','display (52)',r'(52) '+r'\unsure{\rlap{$X$}V|\rlap{$X$}\mathcal V}_{ij}='+V+r'_i\cap '+V+r'_j')
inv('deletion','display (52), superposed base; layer and strike state unresolved','Overlapping X and V with one shared ij; no temporal layer order asserted')
inv('margin note','left margin, oblique, opposite (52)','Pour un ... est-ce une équivalence d’homotopie ?')
inv('diagram','formula within the oblique left note',V+r'_{ij}^{\unsure{b}}='+V+r'_i\cap X_j^* followed by hooked connector, without target letters')
inv('margin note','right margin opposite (52) and the central diagram','NB V_ij a un sens ... V_i cap V_j = slashed circle ... V_ii=V_i')
inv('deletion','right NB, between sens and the live si',r'\deleted{\unsure{si}}')
inv('insertion','right margin below V_ii=V_i; long curved leader attaches to the intersection-empty clause','(du moins si les ouverts de X sont normaux, p.ex. X métrisable)')
inv('text','main line introducing central diagram',"de sorte qu'on a")
inv('diagram','central diagram, two hooked main arrows and lower parenthetical expression','V_ij with b_ij right hook and s_ij down hook; (X_i, w|h, one tilde, two opposite arrow marks) V_i')
inv('deletion','lower diagram, dense left-pointing mark; strike state unresolved',r'\unsure{\longleftarrow|\deleted{\longleftarrow}}')
inv('text','main line immediately above (53)','On a :')
inv('display','display (53)',r'(53) X=\varinjlim(V_i,V_ij, crossed brace-like group b_ij,s_ij)')
inv('deletion','display (53), brace-like glyph before b_ij; strike state unresolved',r'\unsure{\deleted{\}}|\}}')
inv('text','two lines following (53)',r'X est obtenu par \uline{recollement} des V_i suivant les V_ij.')
inv('text','main line preceding (54)','On définit aussi, plus généralement, les')
inv('display','display (54)',r'(54) V_{i_0.-i_n}=V_{i_0}\cap- -\cap V_{i_n}; final V retraced')
inv('text','final main line at the lower paper edge',r'pour un drapeau i_0<i_1<.-<i_n')
inv('margin note','oblique bottom-right note',r'\uline{NB} L’expression a un sens = si l’ens. {i_0, -i_n} ne forme pas un drapeau, mais il est vide si ce n’est pas un drapeau')
inv('text','bottom-left foliation, pale strokes','76','another unnamed hand')

doubts=[
 dict(place='All V bases on scan 077',reading=V,alternatives=r'V | \mathcal V',confidence='low',reason='Rounded bowls, upper curls and caps recur throughout the page, but this page does not independently establish whether they encode a distinct alphabet. Each occurrence retains the plain/calligraphic alternative; H comparison rows use only the leading candidate.'),
 dict(place='Heading, crossed raised group before L',reading=r'\deleted{\unsure{*}}',alternatives='star candidate under a mask; no additional supported glyph recovered',confidence='low',reason='The zigzag/retraced cluster does not expose all arms independently; the adjacent live L is secure.'),
 dict(place='Designation, exponent M0650',reading=r'\unsure{*|<|\deleted{*}}',alternatives='live star | left angle | struck star',confidence='low',reason='Exposed left vertex and parallel upper rays leave the glyph shape open; the dense body also masks its strike state.'),
 dict(place='Designation, le M0651',reading=r'\unsure{\deleted{le}|le}',alternatives='struck le | live le',confidence='low',reason='A visible independent horizontal crossing favours deletion; the low letter bodies are merged and partly masked.'),
 dict(place='After Ainsi, crossed on',reading=r'\deleted{\unsure{on}}',alternatives='on retained as a tentative lexical recovery',confidence='low',reason='The strike obscures the low bodies. This is a certainty-only addition relative to the same candidate in C.'),
 dict(place='After the crossed on, live short group',reading=r'\unsure{on a}',alternatives='compressed on a; no supported fuller phrase',confidence='low',reason='The three live groups are a filled point, a shallow arch and a tiny a-like blot. C gives the same letters without doubt; H omits the groups.'),
 dict(place='Display (51), target exponent M0652',reading=r'\unsure{*|\deleted{*}}',alternatives='live star | struck star',confidence='low',reason='Several star spurs survive, while the centre is dense enough to conceal a strike.'),
 dict(place='Display (51), caption',reading=r'\unsure{des|de}',alternatives='des | de',confidence='low',reason='The terminal down-curl supports s, but e/s segmentation remains compressed. The comparison uses des as leading candidate.'),
 dict(place='Cancelled Pour un drapeau',reading=r'\deleted{\unsure{Pour un drapeau}}',alternatives='the same words as C/H, under a broad crossing',confidence='low',reason='The strike merges much of the low Pour/un run and crosses drapeau; all letters are not independently exposed. This adds doubt without changing witness letters.'),
 dict(place='After live Si',reading=r'Si\unsure{)}',alternatives='closing-parenthesis-like stroke; its syntactic role remains open',confidence='medium',reason='A separate long curved stroke follows the dotted i. No independent matching opening has been isolated.'),
 dict(place='Display (52), left base',reading=r'\unsure{\rlap{$X$}V|\rlap{$X$}\mathcal V}_{ij}',alternatives='overlapping X/V with unresolved temporal order and cancellation state',confidence='low',reason='Crossing diagonals and a U-like bowl occupy the same baseline position and share one ij. The expected intersection notation was not used to assign the live layer.'),
 dict(place='Left margin, raised b M0653',reading=r'\unsure{b}',alternatives='b candidate with unresolved doubled lower contour',confidence='low',reason='The oblique upper stem and doubled lower turn are visible but do not settle the character completely.'),
 dict(place='Lower diagram label M0656',reading=r'\unsure{(w)|(h)}',alternatives='(w) | (h)',confidence='low',reason='A tall first stem and two low turns leave both letter forms open; w leads by the local lower contour.'),
 dict(place='Lower diagram, dense left arrow',reading=r'\unsure{\longleftarrow|\deleted{\longleftarrow}}',alternatives='live | struck left-pointing mark',confidence='low',reason='The mark is heavily overdrawn, but no independent cancellation stroke can be separated. The lower right arrow is distinct and clear.'),
 dict(place='Display (53), M0657',reading=r'\unsure{\deleted{\}}|\}}',alternatives='struck brace-like glyph | live brace-like glyph',confidence='low',reason='Its upper turns are crossed/reworked and its lower sweep is clear. The record retains state doubt after narrowing the shape to a brace candidate.'),
]

notes=[
 dict(id='150-077-N01',text='The author numbers this sheet 34 and heads it with underlined item 15, Introduction des proespaces. The pale bottom-left 76 is foliation in another unnamed hand and is represented separately.'),
 dict(id='150-077-N02',text='The manuscript designates a tubular provoisinage for the written X_i star complement and labels display (51) an équivalence d’homo- / topie des|de proespaces. The raised marks on the V symbols are overdrawn; their glyph and strike states remain local doubts. These sentences report the manuscript and do not certify its mathematical claims.'),
 dict(id='150-077-N03',text='The author introduces the i<j line and writes the intersection display (52). Its first base contains superposed X and V strokes with one shared ij. The intersection expression was not used to infer which layer is live. The diagram has a horizontal b_ij hook and a downward s_ij hook, with the lower Xi expression, a w|h label, one tilde and two opposite arrow marks. The closing parenthesis is visibly before V_i.'),
 dict(id='150-077-N04',text='The oblique left marginal question begins Pour un and asks est-ce une équivalence d’homotopie ?. Its formula contains a doubtful raised b and ends at a hooked connector without written target letters. The manuscript’s question is preserved as a question; no proof check of it was undertaken.'),
 dict(id='150-077-N05',text='The right NB relates its written V_i intersection V_j equals slashed-circle formula to the words i et j ne sont pas comparables. Its long insertion leader attaches the parenthesis du moins si les ouverts de X sont normaux, p.ex. X métrisable to that clause. The note also writes V_ii=V_i. These are attributed manuscript statements, with no independent result asserted here.'),
 dict(id='150-077-N06',text='Display (53) and its following sentence present X as the author’s colimit/recollement expression. The vertical crossed brace-like glyph before b_ij is retained with state doubt; it was not replaced by a mathematically expected pair of arrows.'),
 dict(id='150-077-N07',text='Display (54) gives the author’s multi-index intersection notation, followed by a drapeau line. The bottom NB is transcribed literally, including = for the written même abbreviation, l’ens., braces, one continuation dash, ne forme pas un drapeau, and mais il est vide. The varied continuation marks in the heading, (54), the flag and the note were read separately.'),
 dict(id='150-077-N08',text='All first-pass reading decisions on this page were based on visible strokes and the supplied witness collation. No theorem, categorical identification, or conditional claim was proved or introduced. check_events is empty because transcription reading alone was not treated as mathematical verification.'),
 dict(id='150-077-N09',text='The repeated curved V bases have no independent alphabet contrast established on this sheet. Plain V leads only as a typographic candidate and calligraphic V remains visible in the doubt alternatives. Two tiny pale marks near the upper-left start of the lower V in the recollement caption have uncertain provenance; no extra accent or prime is assigned. The final V in (54) is retraced without an independently recoverable cancelled letter.'),
]
notation=[
 dict(form=V,meaning='The manuscript’s neighbourhood symbols; the plain/calligraphic alphabet remains unresolved.',evidence='Rounded U-like bowl with varying upper curls/caps in every inspected occurrence.',places='077 heading, designation, (51)–(54), all marginal formulas and diagram nodes'),
 dict(form=r'V_J^{\deleted{\unsure{*}}L}',meaning='The raised reworked notation written in the heading.',evidence='A crossed small cluster precedes a distinct tall L with a broad foot.',places='077 heading, p02'),
 dict(form=r'X_i^*=X_i\setminus\bigcup_{j<i}X_j',meaning='The manuscript’s displayed local designation of X_i star.',evidence='Six-spur star, a sloping set-difference stroke, a union bowl, and the written bound j<i.',places='077 opening definition, p05'),
 dict(form=r'.-.;\quad .-;\quad -\ -;\quad -',meaning='Literal local continuation marks, without uniform substitution.',evidence='Heading has dot-dash-dot; (54) left index and final flag have dot-dash; (54) right side has two dashes; bottom set has one dash.',places='077 p02, p17, p18, p19'),
 dict(form='=',meaning='Written short form read as même in the bottom prose note.',evidence='Two separate horizontal strokes, the lower slightly wavy, immediately before si.',places='077 bottom NB, p19'),
 dict(form=r'\hookrightarrow',meaning='Hooked connectors as actually drawn on this page.',evidence='Left margin and both main diagram arrows have source hooks; terminal heads and directions were read individually.',places='077 p11 and p14'),
 dict(form=r'\sim',meaning='The one wavy mark below the lower parenthesized diagram label.',evidence='A single wave is visible, separated from the w|h label and the arrow marks.',places='077 lower diagram, p14'),
]
abbreviations=[
 dict(written='NB',expansion='nota bene',places='077 right and bottom marginal notes; only bottom NB underlined'),
 dict(written='p.ex.',expansion='par exemple',places='077 right inserted parenthesis'),
 dict(written='ens.',expansion='ensemble',places='077 bottom NB'),
 dict(written='=',expansion='même',places='077 bottom NB after a un sens'),
]
hand_log=[
 dict(habit='V bases have rounded U-like bowls with variable upper hooks or loops; alphabet assignment remains open.',places='077 all V occurrences',scope='All observed V bases on this page, including the retraced last V in (54).',witness_errors='C prints plain V and H prints calligraphic V throughout; the return retains both candidates rather than claiming an established alphabet contrast.'),
 dict(habit='Subscript i can share the lower returning stroke of X while retaining a detached dot.',places='077 definition and source of (51)',scope='Both inspected X_i constructions; the first X_i in the definition also has a separate short stem.',witness_errors='No changed witness letters; the comparison prevented supplying an extra stroke or dropping the joined i.'),
 dict(habit='j has a long low stem with an angular or curled leftward foot, which can cross the following baseline.',places='077 all ij and j labels, especially right NB and central diagram',scope='Observed j occurrences on this sheet.',witness_errors='The j descender touches the cancelled si in the right NB; it is not treated as a separate cancellation.'),
 dict(habit='Small prose groups can reduce to points, shallow arches and dark blots.',places='077 on a after Ainsi; de/des in the caption; ce in the bottom note',scope='Only the listed local forms, with uncertainty preserved where segmentation is not secure.',witness_errors='H omits on a; C/H differ at caption de/des. The same letters ce are retained after crop review.'),
 dict(habit='Continuation marks vary locally between points and horizontal dashes.',places='077 heading, (54), final flag and bottom set',scope='Each listed group counted separately.',witness_errors='Both witnesses use uniform ellipsis macros at these local groups.'),
 dict(habit='A curved insertion leader can end beside a genuine parenthesis and can pass other written lines.',places='077 raised pro; right parenthetical insertion',scope='Both actual insertions on this sheet.',witness_errors='H positions the right qualification after the final equality; the leader attaches to the earlier intersection-empty clause.'),
 dict(habit='A dense old-looking diagram mark need not expose a separate cancellation line.',places='077 lower left arrow and brace-like sign in (53)',scope='Strike state remains open at these two positions.',witness_errors='C marks the lower arrow deleted; H omits it. Both state and geometry are preserved explicitly.'),
]
# Tight rectangles for the blind audit. Where rectangular bounds intersect the
# neighbouring line, the reading records the clipped foreground explicitly.
audit=[]
def box(kind,b,reading):
    audit.append(dict(box=f'B{len(audit)+1:02d}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
tex=(BASE/'edition/reader_returns/150_scan077.tex').read_text()
central=tex.split("de sorte qu'on a\n",1)[1].split('On a :',1)[0].strip()
leftdiagram=r'\diagram{\begin{tikzcd}[column sep=small] '+V+r'_{ij}^{\unsure{b}}='+V+r'_i\cap X_j^*\arrow[r,hook]&{}\end{tikzcd}}'
box('handwritten number',[49,25,101,77],r'\mspage{34}')
box('handwritten number',[258,45,335,120],r'\uline{15}.')
box('lexical disagreement',[398,50,1210,139],'Introduction des proespaces :')
box('doubtful formula',CP[2]['box'],'$'+V+r'_{i_0.\!-.i_n},\ '+V+r'_J^{\deleted{\unsure{*}}L}$,')
box('doubtful formula',CP[3]['box'],'$'+V+r'_i^{\unsure{*|<|\deleted{*}}}$ \unsure{\deleted{le}|le} \inserted{pro}voisinage % pro is above the line; its curved leader ends before voisinage.')
box('insertion',[1034,161,1126,235],r'\inserted{pro} % Curved insertion leader; lower boundary intersects the neighbouring opening vo of voisinage, with its next dotted-stroke fragment at the right boundary.')
box('struck passage',[936,191,1027,238],r'\unsure{\deleted{le}|le}')
box('lexical disagreement',CP[4]['box'],'(au sens des proespaces)')
box('doubtful formula',CP[5]['box'],r'$X_i^*=X_i\setminus\bigcup_{j<i}X_j$ % The middle i shares the returning lower stroke of X.')
box('struck passage',[794,432,881,451],r'\deleted{\unsure{on}}')
box('lexical disagreement',[922,425,1037,451],r'\unsure{on a}')
box('doubtful formula',CP[7]['box'],r'(51)\qquad X_i^*\longrightarrow '+V+r'_i^{\unsure{*|\deleted{*}}}')
box('lexical disagreement',[1171,490,1678,681],r"équivalence d'homo-"+'\n'+r'topie \unsure{des|de} proespaces.')
box('struck passage',CP[9]['box'],r'\deleted{\unsure{Pour un drapeau}}'+'\n'+r'Si\unsure{)} $i<j$, on pose % The long descending cancelled P intersects the left edge of the live line.')
box('medium-confidence departure',[430,742,506,827],r'Si\unsure{)} % Upper boundary clips the horizontal strike belonging to the previous line; no independent opening parenthesis is supplied.')
box('handwritten number',[231,827,340,902],'(52)')
box('doubtful formula',[622,827,1113,980],r'\unsure{\rlap{$X$}V|\rlap{$X$}\mathcal V}_{ij}='+V+r'_i\cap '+V+r'_j % One shared ij follows the overlapping X/V base; layer order remains open.')
box('margin note',CP[11]['box'],'Pour un\n'+leftdiagram+"\nest-ce une équivalence d'homotopie ? % Neighbouring complete (52) lies above-right in this rectangle; the clipped main-text initial d of de sorte qu’on a lies below-right.")
box('margin note',CP[12]['box'],'NB $'+V+r'_{ij}$ a un sens \deleted{\unsure{si}} si $i\neq j$ mais si $i$ et $j$ ne sont pas comparables, on a $'+V+r'_i\cap '+V+r'_j=\varnothing$, si $i=j$, on a $'+V+r'_{ii}='+V+r'_i$ % A portion of the curved insertion leader runs along the left/lower side; its words are below this rectangle.')
box('struck passage',[1440,850,1495,882],r'\deleted{\unsure{si}} % The lower hooked tail of the preceding V_ij descender crosses the upper edge of the group.')
box('insertion',CP[13]['box'],r'\inserted{(du moins si les ouverts de $X$ sont normaux, p.ex. $X$ métrisable)} % Long curved leader attaches above to the intersection-empty clause. The rectangle also contains the preceding live si $i=j$, on a $'+V+r'_{ii}='+V+r'_i$; its top edge clips the lower tails of $'+V+r'_i\cap '+V+r'_j=\varnothing$, and the comma.')
box('doubtful formula',CP[14]['box'],central+'\n% The top-left edge contains only a clipped descending stroke from the preceding main text.')
box('struck passage',[512,1345,862,1509],r'\Bigl(X_i\quad\substack{\unsure{(w)|(h)}\\\sim\\\unsure{\longleftarrow|\deleted{\longleftarrow}}\\\longrightarrow}\quad\Bigr)'+V+r'_i % The top of this rectangle includes the terminal portion of the downward s_ij arrow, with the lower part of its label; the complete diagram is in the preceding box.')
box('doubtful formula',[232,1608,1374,1771],r'(53)\qquad X=\varinjlim\bigl('+V+r'_i,'+V+r'_{ij},\unsure{\deleted{\}}|\}}\ b_{ij},s_{ij}\bigr)')
box('struck passage',[1050,1606,1103,1725],r'\unsure{\deleted{\}}|\}} % Vertical brace-like group, with upper diagonal/retraced strokes; no extra label assigned.')
box('doubtful formula',[1433,1754,1565,1854],V+r'_i')
box('doubtful formula',[267,1884,850,2017],'suivant les $'+V+r'_{ij}$. % Two tiny pale marks by the upper-left entry of V have uncertain provenance; no extra prime or accent is assigned.')
box('doubtful formula',[233,2110,1235,2279],r'(54)\qquad '+V+r'_{i_0.\!-i_n}='+V+r'_{i_0}\cap\mathord{-}\,\mathord{-}\cap '+V+r'_{i_n} % The final V is retraced. A clipped neighbouring descender fragment enters at the upper edge.')
box('handwritten number',[264,2280,1274,2359],r'pour un drapeau $i_0<i_1<.\!-<i_n$ % The lower paper edge meets the initial p descender.')
box('margin note',CP[19]['box'],r"\uline{NB} L'expression a un sens $=$ si l'ens. $\{i_0,\mathord{-}i_n\}$ ne forme pas un drapeau, mais il est vide si ce n'est pas un drapeau % One neighbouring comma from the main line above appears separately at the upper edge of the rectangle.")
box('handwritten number',CP[20]['box'],r'\margin{76} % Pale other-hand foliation.')

result=dict(scan='077',reader='reader_b',line_count=17,changes=rows,decisions=decisions,inventory=inventory,doubts=doubts,notes=notes,check_events=[],notation=notation,abbreviations=abbreviations,hand_log=hand_log,audit_boxes=audit,crops=M['crops'],unresolved=[
 'The plain/calligraphic V assignment remains open at every occurrence.',
 'The crossed title exponent remains a masked star candidate; its adjacent L is secure.',
 'M0650 retains live star, left-angle and struck-star candidates; M0652 retains live/struck star.',
 'The le recovery and its live/struck alternative, the crossed on, and the compressed live on a remain doubtful.',
 'The caption des/de segmentation remains open.',
 'The cancelled Pour un drapeau is lexically retained with doubt; the separate closing-parenthesis-like stroke after Si has unresolved role.',
 'The overlapping X/V base in (52) has unresolved layer and strike state, with one shared ij.',
 'The left marginal superscript b remains doubtful; the connector has no written target.',
 'The lower diagram label remains w/h, and the dense left arrow retains live/struck doubt.',
 'The brace-like group in (53) retains live/struck doubt; no double right arrow is supplied.',
 'Tiny pale marks by the lower caption V have uncertain provenance and no assigned linguistic role.'
],coverage=dict(whole_image_viewed=True,halves_viewed=['top','bottom'],all_tokens_read=True,all_C_insertions_deletions_checked=True,differences_considered=35,macro_only_differences_ignored=r'scan/page wrappers, H editorial notes as notes, equivalent text/math wrappers, \struck/\deleted and \supplied/\inserted where they express the same observed insertion, emphasis/underline where the actual scope agrees, \emptyset/\varnothing as the same visible slashed-circle sign, delimiter sizing and ordinary spacing; substantive font, placement, strike, and graphic differences are recorded.',main_line_count_basis='17 main written baselines, counting each numbered display as one, the wrapped caption as a second baseline, and the cancelled phrase; separate diagram rows, marginal baselines and isolated foliation are inventoried separately.',successful_crop_views=21,failed_or_truncated_views='An initial p05–p10 batch exceeded the available display context and was not counted; all six were subsequently displayed successfully in smaller batches.',no_OCR=True,no_web=True,no_TeX_compilation=True))

# Validate the exact quoted witness substrings (whitespace differences only).
def norm(s): return ' '.join(s.split())
quotation_issues=[]
for row in rows:
    for witness, source in [('C',C),('H',H)]:
        value=row[witness]
        if value=='(absent)': continue
        if norm(value) not in norm(source): quotation_issues.append((row['id'],witness,value))
if quotation_issues:
    print('QUOTATION_ISSUES',json.dumps(quotation_issues,ensure_ascii=False,indent=2))
    raise SystemExit(1)
assert len(decisions)==11 and [d['id'] for d in decisions]==[f'M{x:04d}' for x in range(649,660)]
assert all(i['transcribed']=='yes' for i in inventory)
assert all(0<=b['x0']<b['x1']<=1678 and 0<=b['y0']<b['y1']<=2359 for b in audit)
assert all((BASE/'edition'/c['file']).is_file() for c in M['crops'])
assert r'\illegible' not in tex
out=BASE/'edition/reader_returns/150_scan077.json'
tmp=out.with_name(out.name+'.tmp')
tmp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(tmp,out)
print(json.dumps(dict(path=str(out),changes=len(rows),against_C=sum(r['against_C'] for r in rows),against_H=sum(r['against_H'] for r in rows),decisions=len(decisions),inventory=len(inventory),doubts=len(doubts),audit_boxes=len(audit),crops=len(M['crops']),all_quotes_exact=True),ensure_ascii=False))
