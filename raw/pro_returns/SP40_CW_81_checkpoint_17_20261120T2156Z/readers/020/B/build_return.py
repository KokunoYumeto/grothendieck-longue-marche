from pathlib import Path
import json
from datetime import datetime, timezone
B=Path('out/readers/020/B')
tex=r'''\scanpage{20}
Ainsi les classes de $\Pi_I^{\unsure{\circ|0}}$ sont les classes de $\Pi_J^\circ$ distinctes de $\deleted{\Pi}U_{J,i}$, et de plus les \unsure{clas.|deux.} parmi
\[
U_{J,i}\cap\Sigma_{\unsure{\deleted{J}i|j|i}}^+,\quad U_{J,i}\cap\Sigma_i^-
\]
qui sont non vides. Or les deux classes en question sont non vides, car
% B_G01: cancelled Sigma and its two visible crossing runs. Observed locus (320,810,403,900).
% Source origin (315,803); x right, y down; 0.25 pt per source pixel. Baseline y=76.
% The visible node occurs once; its phantom carries the deletion state without a generic extra rule.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,76)}]
\path[use as bounding box] (0,0) rectangle (95,100);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,76) {\rlap{$\unsure{\Sigma_j|\Sigma_i}$}\phantom{\deleted{$\unsure{\Sigma_j|\Sigma_i}$}}};
\draw[line width=0.45pt,line cap=round] (10,73) .. controls (20,54) and (30,31) .. (40,12);
\draw[line width=0.45pt,line cap=round] (45,73) .. controls (43,80) and (49,82) .. (54,76) -- (69,35);
\end{tikzpicture}
$U_{J,i}$ est un voisinage de $\deleted{\Sigma}E_{\unsure{i|j}}$, et
\[
\overline{\Sigma_i^+}\cap\deleted{\Sigma}E_i\ne\varnothing,\quad
\overline{\deleted{E}\Sigma_i^-}\cap\deleted{\Sigma}E_i\ne\varnothing.
\]
On sait donc que le nb des classes est en \deleted{\unsure{tout|est}} $(n-1)+2=n+1=\operatorname{card} I+1$ (ce qui achève \unsure{aussi|ainsi}
% B_G02: complete word-bearing group la and one qualified detached point above/right.
% Origin (500,1347), 0.25 pt per source pixel, baseline y=49. Observed point locus (566,1363,575,1373).
% Inner graphic origin is explicitly translated by (66,18); base-west anchor and baseline (0,0) fix its placement.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline=(Bla.base)]
\path[use as bounding box] (0,0) rectangle (88,62);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (Bla) at (0,49) {la};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (66,18) {\unsure{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,0)}]
\path[use as bounding box] (0,0) rectangle (7,8);
\fill (2,0) -- (5,4) -- (4,7) -- (1,6) -- cycle;
\end{tikzpicture}}};
\end{tikzpicture}
\unsure{dèm.|dém.|dem.} par récurrence sur le nb des classes).

\uline{Lemme} Toute classe de $\Pi_I^\circ$ est de la forme
% B_G03: union, complete parenthesized expression, overwritten limit, raised hatted Sigma, and literal brace.
% Origin (1010,1600), 0.25 pt per source pixel, baseline y=140; fixed drawing rectangle (0,15)-(390,200).
% Pi above and X setminus to the left are outside this group. No generic bigcup or overbrace is also drawn.
$X\setminus\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,140)}]
\path[use as bounding box] (0,15) rectangle (390,200);
% U01 body; U02 upper-right loop; U03 pale lower retrace.
\draw[line width=0.95pt,line cap=round] (17,90) .. controls (17,122) and (24,140) .. (45,142) .. controls (63,142) and (72,133) .. (71,115) -- (68,87);
\draw[line width=0.55pt,line cap=round] (68,87) .. controls (66,77) and (63,81) .. (64,89) .. controls (65,96) and (68,99) .. (68,104);
\draw[black!55,line width=0.45pt,line cap=round] (19,114) .. controls (23,140) and (51,150) .. (65,133);
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (0,190) {$\alpha\in\unsure{\deleted{I}K|K}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small] at (91,140) {$(\Sigma_\alpha^+\cup E_\alpha)$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\scriptsize] at (184,58) {$\inserted{\widehat{\Sigma}_\alpha^+}$};
% BR01 main run and central turn; BR02 closed left loop; BR03 left retrace.
\draw[line width=0.65pt,line cap=round] (108,79) .. controls (132,75) and (151,71) .. (180,74) .. controls (193,75) and (204,70) .. (217,72) -- (220,62) .. controls (234,70) and (256,68) .. (287,64) .. controls (307,60) and (326,59) .. (339,62) .. controls (344,63) and (345,66) .. (345,69);
\draw[line width=0.55pt,line cap=round] (132,76) .. controls (141,68) and (160,69) .. (164,74) .. controls (153,81) and (142,82) .. (132,76);
\draw[line width=0.85pt,line cap=round] (120,80) .. controls (145,74) and (178,73) .. (210,74);
\end{tikzpicture}}$
où $K$ est une
% B_G04 contains exactly partie, the inserted/deleted non vide, and de I, et.
% Source origin (997,1750), 0.25 pt per source pixel, baseline y=110. Fixed rectangle (0,0)-(530,160).
% NV01 is the rising cancellation run with its right return. NV02 is the separate curved insertion guide.
\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,110)}]
\path[use as bounding box] (0,0) rectangle (530,160);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,115) {partie};
\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\small,rotate=8] at (157,45) {\inserted{\rlap{non vide}\phantom{\deleted{non vide}}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (200,89) {de $I$, et};
\draw[line width=0.55pt,line cap=round] (154,53) .. controls (203,44) and (282,30) .. (331,24) .. controls (331,31) and (325,37) .. (315,43);
\draw[line width=0.45pt,line cap=round] (182,94) .. controls (172,61) and (272,47) .. (339,40) .. controls (346,39) and (351,39) .. (355,43);
\end{tikzpicture}
% slanted; the two written conditions have no punctuation between them.
\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=19,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{$K$ est $\ne\varnothing$\\si $I\ne\varnothing$}};\end{tikzpicture}}\normalmarginpar
$\forall\alpha\in K$, \deleted{on a} $\Sigma_\alpha^+
% B_G05 literal reworked relation, followed inside the qualifier by its supported complete-state interpretations.
% Origin (943,1947), 0.25 pt per source pixel, baseline y=43; observed locus (944,1949,999,2004).
% M01 curved body, M02 middle shaft, M03 thin right head. No additional unqualified membership or arrow is drawn.
\mathrel{\unsure{\text{\begin{tikzpicture}[x=0.25pt,y=-0.25pt,baseline={(0,43)}]
\path[use as bounding box] (0,0) rectangle (62,66);
\draw[line width=0.70pt,line cap=round] (45,11) .. controls (35,-1) and (16,17) .. (7,32) .. controls (1,43) and (5,51) .. (15,55) .. controls (23,58) and (32,56) .. (39,51);
\draw[line width=0.75pt,line cap=round] (4,40) -- (43,32);
\draw[line width=0.40pt,line cap=round] (35,24) .. controls (38,16) and (51,29) .. (54,36) .. controls (56,34) and (54,20) .. (48,19);
\end{tikzpicture}}|\deleted{\Rightarrow}\in|\deleted{\to}\in|\in}}
\pi_0(X\setminus E_\alpha)$, tels que $\forall\alpha,\beta\in K$, $\alpha\ne\beta$, on ait $\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing$ $(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing)$.
% archive sheet number: 19
'''
(B/'reading.tex').write_text(tex)
manifest=json.loads((B/'crop_manifest.json').read_text())
M={i+1:x for i,x in enumerate(manifest)}
d=[]
def add(id,loc,C,H,reading,evidence,confidence,kind,dC=False,dH=False,status=None,crop=None,bbox=None,row=None,**extra):
 o={'id':id,'location':loc,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dC,'diff_H':dH,'C_doubt_status':status,'readers_crop':M[crop]['path'] if crop else None,'bbox':bbox or (M[crop]['bbox'] if crop else None)}
 if row:o['C_source_row']=row
 o.update(extra);d.append(o)
add('B020-D01','Opening line, Pi-I superscript',r'\Pi_I^{\unsure{\circ|0}}',r'\Pi_I^0',r'\Pi_I^{\unsure{\circ|0}}','Small closed rounded loop above the separately footed I; its strokes retain both a circle and a small zero. H zero survives as an alternative.','medium','misread symbol or index',dH=True,status='retained',crop=1,row='R01',sublocus='R01a',qualification='Qualified primary difference from H, not a conclusive exclusion of H zero.')
add('B020-D02','Second line, Pi-J superscript',r'\Pi_J^\circ',r'\Pi_J^0',r'\Pi_J^\circ; local alternatives \circ|0','Closed small upper loop, locally inspected separately. First-occurrence convention prints the circle primary here without a second qualifier.','medium','misread symbol or index',dH=True,status='retained',crop=2,row='R01',sublocus='R01b',qualification='Zero remains supported here despite the unmarked recurring primary in reading.tex.')
add('B020-D03','Second line, U after distinctes de',r'\deleted{\Pi}U_{J,i}',r'U_{J,i}',r'\deleted{\Pi}U_{J,i}','Horizontal Pi head and two shorter upright remnants remain beneath the taller curved U; both lowered J and dotted i and their separator are visible.','high','omission',dH=True,crop=3)
add('B020-D04','Third line, word after les',r'\unsure{clas.|deux}',r'deux',r'\unsure{clas.|deux.}','Small open first curl followed by a tall loop and flattened low continuation; clas. remains first but the joined strokes retain deux. Endpoint point is separately recorded in D05.','medium','misread word',dH=True,status='retained',crop=4,row='R02',qualification='H deux survives as a lexical alternative; the terminal point is present for either candidate.')
add('B020-D05','Third line, point after doubtful word',r'clas. (point in first candidate); deux (no point in alternative)',r'deux (no point)',r'.','A discrete dark point stands after the final downward turn and before the large gap preceding parmi. Both complete candidates in reading.tex include it.','high','omission',dH=True,crop=4,physical_scope='The endpoint point only; D04 counts only the word reading.')
add('B020-D06','First positive paired intersection, Sigma index',r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+',r'\Sigma_i^+',r'\Sigma_{\unsure{\deleted{J}i|j|i}}^+','A short dotted right return lies beside a much deeper descending stem and left-returning foot. The shared junction does not settle overwritten J+i, j, or i as complete states.','low','misread symbol or index',dH=True,status='retained',crop=5,row='R03',qualification='H simple i survives as an alternative; no chronology is inferred.')
add('B020-D07','Cancelled Sigma group before U est un voisinage',r'\deleted{\unsure{\Sigma_i|\Sigma_j}}',r'\struck{\ill{}}',r'\deleted{\unsure{\Sigma_j|\Sigma_i}}; literal B_G01 crossing paths','The cancelled Sigma is recoverable; the small index has a substantial descending return, favoring j, but crossing strokes leave i supported. Two separately visible sloping cancellation runs are preserved by G01, with a small hooked return in the second path.','low','readable ink left as \\ill{}',dC=True,dH=True,status='retained',crop=6,row='R04',physical_scope='One cancelled glyph/index/state cluster and one H ill placeholder; geometry is included in this parent count.',shape_confidence='high for the two crossing runs; low for index identification',components=['G01.C01','G01.C02'])
add('B020-D08','Index of E after voisinage de',r'E_{\unsure{i|j}}',r'E_i',r'E_{\unsure{i|j}}','The short index is a hooked undotted stroke. Its limited downward extent favors i, while j remains possible. The separate lower comma is not used as its dot or tail.','medium','other',status='retained',crop=7,row='R05')
add('B020-D09','Base E after voisinage de',r'\deleted{\Sigma}E',r'E',r'\deleted{\Sigma}E','Thin diagonal Sigma returns remain inside the heavier vertical and horizontal E strokes.','high','omission',dH=True,crop=7)
add('B020-D10','After E index before et',r'E_{\unsure{i|j}}, et',r'E_i et',r'E_{\unsure{i|j}}, et','A distinct curved mark falls below the index and turns left at its lower end.','high','omission',dH=True,crop=7)
add('B020-D11','First non-emptiness intersection, E base',r'\deleted{\Sigma}E_i',r'E_i',r'\deleted{\Sigma}E_i','Angular thinner return survives between the thick E bars. The lowered hook and point are retained as the written i.','high','omission',dH=True,crop=8,bbox=[470,944,533,1004])
add('B020-D12','Second non-emptiness intersection, barred Sigma base',r'\overline{\deleted{E}\Sigma_i^-}',r'\overline{\Sigma_i^-}',r'\overline{\deleted{E}\Sigma_i^-}','A left upright and short middle-bar remnant occur beneath the diagonal Sigma strokes. The independent upper closure rule and minus are already present in C and H.','high','omission',dH=True,crop=8,bbox=[744,908,861,996])
add('B020-D13','Second non-emptiness intersection, E base',r'\deleted{\Sigma}E_i',r'E_i',r'\deleted{\Sigma}E_i','The small E retains an interior diagonal return of Sigma beneath its three heavier arms.','high','omission',dH=True,crop=8,bbox=[911,922,978,989])
add('B020-D14','On ... donc above count',r'\unsure{voit|sait}',r'voit','sait','The first stroke curls back into a low s; it is followed by a small a bowl, the raised point, and the tall terminal t. The crop supports sait.','high','misread word',dC=True,dH=True,status='resolved',crop=9,row='R10')
add('B020-D15','Live word between est and cancelled word before count','est en',r'est \struck{\ill{}}','est en','The low open e/u-shaped entry and following n run are visibly separated from the cancelled word at the right; the live en has no crossing stroke.','high','omission',dH=True,crop=10,bbox=[1317,1034,1427,1100],physical_scope='Live en only; the following one H ill placeholder is counted in D16.')
add('B020-D16','Cancelled word at right before count',r'\deleted{\unsure{tout|est}}',r'\struck{\ill{}}',r'\deleted{\unsure{tout|est}}','A tall first rise and reduced low middle remain under the long diagonal. The crossing masks the letter sequence enough to retain both tout and est.','low','readable ink left as \\ill{}',dH=True,status='retained',crop=10,row='R06',physical_scope='One recovered qualified cancelled word, one H ill placeholder.')
add('B020-D17','Parenthesis, adverb before la',r'\unsure{aussi|ainsi}',r'aussi',r'\unsure{aussi|ainsi}','The initial point/low run and joined middle reduce the u/n/s distinctions; the terminal i has a separate point. Both adverbs remain supported.','medium','other',status='retained',crop=12,row='R11')
add('B020-D18','Above/right of la, in parenthesis','No separate component','No separate component','One locally qualified tapered point in B_G02','A small discrete dark tapered mark lies around full-scan (570,1367), above and to the right of the la body. It is preserved once graphically. Its attachment to the adjoining word, character, role, hand and surface origin remain unsettled.','medium','drawing or diagram',dC=True,dH=True,crop=12,bbox=[566,1363,575,1373],shape_confidence='high for presence and small tapered outline',role_confidence='undetermined',component='G02.P01',source_boundaries='B_G02 contains la once and the qualified point once; no punctuation value is supplied.')
add('B020-D19','Parenthesis, abbreviated proof word',r'\unsure{dém.|dem.}',r'dém.',r'\unsure{dèm.|dém.|dem.}','The detached short upper stroke leans down-right, favoring a grave accent. Its near-upright shape and very close approach to the small body do not settle direction/presence completely; acute and unaccented candidates remain explicit. The endpoint point is clear.','medium','misread word',dC=True,dH=True,status='retained',crop=12,row='R07',qualification='H dém. survives as an alternative; this is a qualified primary accent change.')
add('B020-D20','Lemma opening, Pi-I superscript',r'\Pi_I^\circ',r'\Pi_I^0',r'\Pi_I^\circ; local alternatives \circ|0','Small closed oval with a short entry at upper left. This third local occurrence retains circle/zero uncertainty; only the first occurrence has a printed qualifier.','medium','misread symbol or index',dH=True,status='retained',crop=13,bbox=[1222,1558,1363,1642],row='R01',sublocus='R01c',qualification='H zero survives locally as an alternative.')
add('B020-D21','Lemma, large indexed union sign',r'\bigcup',r'\bigcup','Literal B_G03 U01/U02/U03','The large curved body has a narrow loop at its upper-right entrance and a paler lower retracing curve. All three runs are represented literally; the interpretation as the indexed union is retained.','high','drawing or diagram',dC=True,dH=True,crop=13,bbox=[1017,1675,1092,1752],components=['G03.U01','G03.U02','G03.U03'],source_boundaries='Only the union sign paths; X setminus is outside G03, and the formula/limit nodes are separately identified.')
add('B020-D22','Lemma, overwritten union limit',r'\alpha\in\deleted{\unsure{I}}K',r'\alpha\in K',r'\alpha\in\unsure{\deleted{I}K|K}','An I-like vertical with top and foot is visible within the heavier K. Its relation to the K body remains open: overwritten I+K and one elaborately drawn K are explicit complete states.','medium','misread symbol or index',dH=True,status='retained',crop=13,bbox=[1004,1747,1125,1805],row='R08',qualification='C implicit absence alternative is made explicit; this wrapper/state clarification alone creates no C count. H K survives as an alternative.')
add('B020-D23','Lemma, brace above parenthesized union term',r'\overbrace{\Sigma_\alpha^+\cup E_\alpha}^{\inserted{\widehat{\Sigma}_\alpha^+}}',r'\note{au-dessus de ... il écrit \widehat{\Sigma}_\alpha^+}','B_G03 BR01/BR02/BR03 beside unchanged formula and inserted hatted Sigma','The brace has a main run with a sharp central upturn, a closed narrow loop within the left arm, and a thicker retraced left run. The raised hat/Sigma label is already present in C and H apparatus.','high','drawing or diagram',dC=True,dH=True,crop=13,bbox=[1110,1654,1362,1691],components=['G03.BR01','G03.BR02','G03.BR03'],source_boundaries='G03 contains one body term and one raised hatted label; no generic overbrace is also drawn.')
add('B020-D24','Inserted non vide above de I',r'\inserted{\deleted{non vide}}',r'\add{\uncertain{non vide}}','Readable inserted non vide, cancelled; literal B_G04 NV01','A rising long stroke crosses the inserted words and turns back at the right. The words themselves remain readable. H carries insertion but prints them live. C already has their cancellation state; the explicit rising run and right return replace its generic strike geometry.','high','deletion state (struck given live or live given struck)',dC=True,dH=True,crop=13,bbox=[1145,1767,1335,1813],components=['G04.NV01'],C_change_scope='Geometry only: wording, insertion and cancellation state retained.',H_change_scope='One physical inserted/deleted phrase cluster, including its cancellation geometry.')
add('B020-D25','Curved guide from gap before de I to inserted phrase','Insertion macro only; no guide path','Insertion macro only; no guide path','Literal B_G04 NV02','The separate long curve starts low beside the gap after partie, rises rightward under the inserted phrase, and ends with a short downward return.','high','insertion or placement',dC=True,dH=True,crop=13,bbox=[1171,1784,1362,1854],components=['G04.NV02'],source_boundaries='B_G04 contains partie, inserted/deleted non vide, and de I, et exactly once; une remains outside.')
add('B020-D26','After forall alpha in K, cancelled prose',r'\deleted{on a}',r'\struck{\ill{}}',r'\deleted{on a}','An o loop and joined n remain at the left of the crossing rule; a small separate a loop occurs farther right.','high','readable ink left as \\ill{}',dH=True,crop=14,bbox=[606,1975,766,2010],physical_scope='One H ill placeholder, one cancelled phrase.')
add('B020-D27','Between positive Sigma and pi_0 in lemma',r'\deleted{\unsure{\Rightarrow}}\in',r'\in','Qualified literal B_G05; supported complete states deleted Rightarrow+in / deleted to+in / in with retracing','The curved left body and a dark middle shaft coexist with a thinner right-pointing head. One recovered shaft is visible; the full predecessor glyph and cancellation target remain open. The graphic is preserved with all three state interpretations inside the local qualifier.','low','misread symbol or index',dC=True,dH=True,status='retained',crop=14,bbox=[944,1949,999,2004],row='R09',components=['G05.M01','G05.M02','G05.M03'],shape_confidence='high for the three literal runs',qualification='C original Rightarrow candidate and H in candidate both remain supported. No chronology or mathematical repair is asserted.',source_boundaries='G05 owns the whole local relation; no unqualified second arrow or membership sign appears beside it.')

inv=[]
def item(n,kind,pos,first,hand='his hand',**extra):
 o={'sheet_kind':'text','hand':hand,'element':f'020.B.{n:02d}','kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'};o.update(extra);inv.append(o)
item(1,'text','Top, opening three physical lines','Ainsi les classes ... les clas./deux. parmi')
item(2,'deletion','Opening U group','Pi beneath live U')
item(3,'display','First paired intersection line','U_{J,i} cap Sigma-index-plus, U_{J,i} cap Sigma_i-minus')
item(4,'deletion','First positive Sigma index','Possible overwritten J under i; alternatives j/i',state='uncertain complete states')
item(5,'text','Following three prose lines','qui sont non vides ... est un voisinage ... et')
item(6,'deletion','Before live U est un voisinage','Cancelled Sigma_j/Sigma_i',state='cancellation clear; index unresolved')
item(7,'drawing','Same cancelled Sigma group','B_G01: two crossing runs, second with low return',components=['G01.C01','G01.C02'])
item(8,'deletion','Voisinage de E','Sigma beneath E')
item(9,'display','Middle, non-emptiness line','Two barred Sigma intersections with E_i, both nonempty')
item(10,'deletion','First intersectand E_i','Sigma beneath E')
item(11,'deletion','Second barred Sigma','E beneath Sigma')
item(12,'deletion','Second intersectand E_i','Sigma beneath E')
item(13,'text','Count and parenthesis','On sait donc ... le nb des classes).')
item(14,'deletion','After live en before count','tout/est, crossed')
item(15,'drawing','Above/right of la in parenthesis','B_G02: one qualified tapered point',hand='undetermined hand',components=['G02.P01'],role='unresolved; possible adjoining-word attachment')
item(16,'text','Lemma heading','Lemme')
item(17,'text','Under lemma heading','One underline spanning Lemme')
item(18,'text','Lemma prose through conditions','Toute classe ... de la forme ... où K est une partie ... tels que')
item(19,'display','Lemma set expression','X setminus indexed union of (Sigma_alpha-plus cup E_alpha)')
item(20,'drawing','Large union in lemma','B_G03 union body, upper loop and pale lower retrace',components=['G03.U01','G03.U02','G03.U03'])
item(21,'deletion','Union index','Possible old I beneath K',state='deleted I K / K retained')
item(22,'insertion','Above parenthesized union term','Hatted Sigma_alpha-plus above brace')
item(23,'drawing','Above parenthesized union term','B_G03 main brace, closed left loop, left retrace',components=['G03.BR01','G03.BR02','G03.BR03'])
item(24,'insertion','Above de I','Inserted non vide, cancelled')
item(25,'deletion','Same inserted phrase','Cancelled non vide, rising run and right return',components=['G04.NV01'])
item(26,'drawing','From gap before de I toward inserted phrase','Long curved guide with right return',components=['G04.NV02'])
item(27,'margin note','Lower left, slanted upward','K est neq empty / si I neq empty')
item(28,'deletion','After forall alpha in K','on a')
item(29,'drawing','Before pi_0','B_G05 curved relation body, middle shaft and thin right head',components=['G05.M01','G05.M02','G05.M03'],state='whole relation locally qualified')
item(30,'deletion','Same relation before pi_0','Possible cancelled Rightarrow or single arrow',state='predecessor/cancellation open; in/retracing alternative retained')
item(31,'text','Final two lines','forall alpha,beta ... hatted disjointness ... parenthesized Longleftrightarrow un-hatted disjointness')
item(32,'text','Lower left page foot','Archive numeral 19, preserved only in TeX comment',hand='undetermined hand')

source_rows=[
 ('R01','opening and lemma','superscript circle','0','retained',['B020-D01','B020-D02','B020-D20']),
 ('R02','line 3','clas.','deux','retained',['B020-D04']),
 ('R03','first paired intersection','i written on J','j / i','retained',['B020-D06']),
 ('R04','before U est un voisinage',r'\Sigma_i',r'\Sigma_j','retained',['B020-D07']),
 ('R05','voisinage de E','i','j','retained',['B020-D08']),
 ('R06','word struck at right before count','tout','est','retained',['B020-D16']),
 ('R07','in the parenthesis','dém.','dem.','retained',['B020-D19']),
 ('R08','under K, union index','I','—','retained',['B020-D22']),
 ('R09','beside membership sign before π₀','⇒','—','retained',['B020-D27']),
 ('R10','above the count','voit','sait','resolved',['B020-D14']),
 ('R11','in the parenthesis, before la','aussi','ainsi','retained',['B020-D17'])
]
rowmap=[{'id':a,'actual_source_order':i+1,'source_location':b,'source_reading':c,'source_other_readings':dd,'status':s,'local_records':r} for i,(a,b,c,dd,s,r) in enumerate(source_rows)]

doubt_ids=['B020-D01','B020-D02','B020-D04','B020-D06','B020-D07','B020-D08','B020-D16','B020-D17','B020-D18','B020-D19','B020-D20','B020-D22','B020-D27']
alts={
'B020-D01':[r'\circ','0'], 'B020-D02':[r'\circ','0'], 'B020-D04':['clas.','deux.'],
'B020-D06':[r'\deleted{J}i','j','i'], 'B020-D07':[r'\Sigma_j',r'\Sigma_i'],
'B020-D08':['i','j'], 'B020-D16':['tout','est'], 'B020-D17':['aussi','ainsi'],
'B020-D18':['Tapered dark point; attachment to la or detached mark unresolved; no character assigned'],
'B020-D19':['dèm.','dém.','dem.'], 'B020-D20':[r'\circ','0'],
'B020-D22':[r'\deleted{I}K','K'], 'B020-D27':[r'\deleted{\Rightarrow}\in',r'\deleted{\to}\in',r'\in (with retracing)']}
byid={x['id']:x for x in d}
doubts=[{'id':id,'location':byid[id]['location'],'reading':byid[id]['reading'],'alternatives':alts[id],'confidence':byid[id]['confidence'],'reason':byid[id]['evidence'],'crop':byid[id]['readers_crop'],'source_row':byid[id].get('C_source_row'),'printed_qualifier':id not in ['B020-D02','B020-D20']} for id in doubt_ids]

notation=[
 {'location':'Three Pi occurrences','visible_form':'Small upper closed loops, lower I/J distinct','latex':r'\Pi_I^{\unsure{\circ|0}}, \Pi_J^\circ, \Pi_I^\circ','qualification':'Local circle/zero alternatives remain at all three physical occurrences.'},
 {'location':'Opening U and each subsequent U','visible_form':'Large curved U, lowered hooked J and dotted i separated by comma','latex':r'U_{J,i}'},
 {'location':'Two non-emptiness intersections','visible_form':'Separate long horizontal closure rules above Sigma and its raised sign','latex':r'\overline{\Sigma_i^+}, \overline{\Sigma_i^-}','status':'Already in C and H; S concern confirmed locally without current-witness bar correction.'},
 {'location':'Count and parenthetical conclusion','visible_form':'nb without a terminal abbreviation point; lower card lettering; point after proof abbreviation','latex':r'nb, \operatorname{card} I, \unsure{dèm.|dém.|dem.}'},
 {'location':'Lemma raised label and hatted disjointness pair','visible_form':'Three separate roof accents over Sigma','latex':r'\widehat{\Sigma}_\alpha^+; \widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+'},
 {'location':'Last parenthesized expression','visible_form':'Un-hatted Sigma heads, two-ended double-line arrow, equality and slashed empty-set form','latex':r'(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing).'},
 {'location':'Lower-left margin','visible_form':'Slanted two-line K est neq empty / si I neq empty','latex':r'K\text{ est }\ne\varnothing;\quad\text{si }I\ne\varnothing','qualification':'Semicolon here describes two lines only; reading.tex adds no punctuation between the conditions.'}
]

source_choices=[
 {'location':'Start/foot','selected':r'\scanpage{20}; % archive sheet number: 19','evidence':'Packet scan020/H page19 mapping plus visible lower-left archive19. No manuscript page marker or cotefile is supplied.','source_only':True,'diff_C':False,'diff_H':False},
 {'location':'Opening/paired line','selected':'Ainsi; classes; distinctes; et de plus les; parmi; separate comma between the two intersections; second Sigma_i-minus','evidence':'Complete half-a reading; no inferred closure bar on either first pair member.'},
 {'location':'Upper prose','selected':'qui sont non vides. Or les deux classes en question sont non vides, car','evidence':'Half a, lines beneath the pair; full stop after first vides and comma after second vides retained.'},
 {'location':'Non-emptiness display','selected':'First comma and second full stop; both ne signs; slashed empty-set shapes','evidence':'Half a and complete crop08. No additional separate mark is supplied for the letter-index joins.'},
 {'location':'Count','selected':r'(n-1)+2=n+1=\operatorname{card} I+1','evidence':'Half b, upper count line. Transcribed without arithmetic check or proof inference.'},
 {'location':'Parenthesis','selected':'ce qui achève','evidence':'Crop11: detached short downward-right upper accent group over the e; full q descender included. Unchanged C/H spelling is an explicit selection.'},
 {'location':'Parenthesis','selected':'par récurrence sur le nb des classes).','evidence':'Half b and crop12 context: compact par group, acute at récurrence, nb, closing parenthesis and point. No abbreviation expansion is inferred beyond the selected visible compact par reading.'},
 {'location':'Lemma prose','selected':'Lemme (single underline), Toute classe, de la forme, où K est une partie de I, et, tels que, on ait','evidence':'Half b and crop13. où carries the separately visible upper slant; all these words occur once in the complete source, including words held inside G04.'},
 {'location':'Final two lines','selected':r'\forall\alpha,\beta\in K,\quad\alpha\ne\beta,\quad\widehat{\Sigma}_\alpha^+\cap\widehat{\Sigma}_\beta^+=\varnothing;\quad(\Longleftrightarrow\Sigma_\alpha^+\cap\Sigma_\beta^+=\varnothing).','evidence':'Half b, each local alpha/beta, two hats, plus signs, equalities, arrowheads, parentheses and endpoint point read independently; the semicolon in this audit is an item separator, not supplied manuscript punctuation.'},
 {'location':'Guide/graphic groups','selected':'G01 cancelled Sigma; G02 la+point; G03 union+limit+parenthesized term+hat+brace; G04 partie+non vide+de I, et; G05 whole relation','evidence':'Exact source boundaries are stated in comments and graphic_groups; no adjoining word is duplicated and the G05 formula continues directly with pi_0.'}
]

report={
 'scan':'020','reader':'B','start_utc':'2026-11-20 20:45:44 UTC','end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':d,'doubts':doubts,'inventory':inv,
 'notes':{
  'page_content':'The author continues a class-count argument, then writes an underlined Lemme giving a form for classes of Pi_I with the upper round mark. The author writes the count (n-1)+2=n+1=card I+1 and the parenthetical statement that this also completes the induction on the number of classes. The lemma names complements of indexed unions of Sigma_alpha-plus cup E_alpha, the membership condition in pi_0(X setminus E_alpha), and pairwise disjointness of the hatted sets. The final written double arrow relates the hatted and un-hatted disjointness expressions. These are attributed manuscript assertions; this reading establishes no proof of them.',
  'author_uncertainty':{'exact_words':[],'note':'No explicit authorial question or uncertainty wording was recovered. The manuscript has corrections and a crossed inserted non vide; editorial doubtful readings are kept separately.'},
  'title_date_page_counts':{'heading':'Lemme, single underline','date':None,'own_page_number':None,'archive_number':'19','scan_number':20,'H_page_number':19},
  'mathematics_led_reading_decisions':'The repeated indexing and formulas were followed to locate small signs and correction clusters. No expected identity or theorem was used to replace a visible sign. No mathematical calculation, proof check, OCR or external research was performed.',
  'processing_note':'Start UTC was recorded before packet reading. All requested text files were read. A truncated initial combined text delivery affected notation.md; its complete standalone text was then read successfully. Whole image, each supplied half, and each of fourteen crops were delivered successfully once. There were no failed unseen image deliveries or repeated image views. A root checkpoint hold was observed after the completed visual phase; this same context resumed without reopening an image.',
  'image_audit_file':'image_audit.json','source_choices':source_choices,
  'S_coverage':{'row_id':'SA01-K81-06','item':'SA01-29','stated_where':'81/15-22','stated_reader':'Claude Opus 5.5 at effort max, reader R4 (no scan viewed)','scope':'Witness proposals over scans015–022; no visual authority is inferred from that broad span.','local_result':'The two closure bars on this sheet were confirmed on half a and already occur in both current C and H. None of the exact quoted example expressions is written verbatim here; the same closure-bar concern was considered only at the two local barred Sigma intersections. No bar is inferred on an unbarred U or the initial paired intersections.','diff_C':False,'diff_H':False,'source_only_scope_choice':True},
  'H_collation':'H has text. Its editorial note about neighboring pages supplies no manuscript words on this sheet. Its note describing the raised hatted Sigma is collated with the body as one existing label, not an omitted second formula. H emphasis and our underline carry the same single-underline span. Each of its three ill placeholders is counted once (D07, D16, D26).'
 },
 'notation':notation,'check_events':[],
 'crops':manifest,
 'brief_feedback':[
  'A nearly vertical accent in dém./dem. admits a grave-primary reading; the exact source row is retained while the additional supported accent candidate is exposed.',
  'The membership correction is most faithfully retained as literal geometry plus complete state interpretations. G05 makes its three runs and the unresolved old-arrow/live-membership states explicit.',
  'A detached point above/right of la can have unresolved attachment as well as role/hand. G02 keeps the word and shape together without assigning a punctuation value.',
  'No missing convention blocked completion. The prescribed first-occurrence rule is followed for the three Pi rings, while every local alternative remains in the report.'
 ],
 'C_doubt_source_map':rowmap,
 'image_audit':json.loads((B/'image_audit.json').read_text()),
 'graphic_groups':[
  {'id':'B_G01','source_origin':[315,803],'units':'x=0.25pt,y=-0.25pt per full-scan pixel','baseline':[0,76],'drawing_rectangle':[0,0,95,100],'components':['C01 diagonal','C02 diagonal with low hooked return'],'word_formula_boundary':r'\unsure{\Sigma_j|\Sigma_i} visible once; phantom deletion annotation invisible','confidence':'two run shapes high; index low'},
  {'id':'B_G02','source_origin':[500,1347],'units':'x=0.25pt,y=-0.25pt per full-scan pixel','baseline':[0,49],'drawing_rectangle':[0,0,88,62],'inner_translation':[66,18],'inner_baseline':[0,0],'inner_drawing_rectangle':[0,0,7,8],'anchor':'base west; inner sep 0pt; outer sep 0pt','components':['P01 tapered point'],'word_formula_boundary':'la visible once plus one locally qualified point','confidence':'point shape high; attachment/hand/role/origin undetermined'},
  {'id':'B_G03','source_origin':[1010,1600],'units':'x=0.25pt,y=-0.25pt per full-scan pixel','baseline':[0,140],'drawing_rectangle':[0,15,390,200],'components':['U01 union body','U02 upper-right loop','U03 pale lower retrace','BR01 main brace and turn','BR02 left loop','BR03 left retrace'],'word_formula_boundary':'Union, alpha in qualified I/K limit, parenthesized Sigma_alpha-plus cup E_alpha, inserted hatted Sigma and brace. X setminus and the earlier Pi remain outside.','confidence':'geometry high; limit state medium'},
  {'id':'B_G04','source_origin':[997,1750],'units':'x=0.25pt,y=-0.25pt per full-scan pixel','baseline':[0,110],'drawing_rectangle':[0,0,530,160],'components':['NV01 rising cancellation and right return','NV02 curved insertion guide and right return'],'word_formula_boundary':'partie; inserted/deleted non vide; de I, et. une is outside. Phantom deletion annotation adds no visible words or generic strike.','confidence':'high'},
  {'id':'B_G05','source_origin':[943,1947],'units':'x=0.25pt,y=-0.25pt per full-scan pixel','baseline':[0,43],'drawing_rectangle':[0,0,62,66],'components':['M01 curved body','M02 middle shaft','M03 thin right head'],'word_formula_boundary':'Whole qualified relation between Sigma_alpha-plus and pi_0. Formal state alternatives are editorial alternatives inside the same qualifier, not additional manuscript occurrences.','confidence':'shapes high; state low'}
 ],
 'structural_validation':{'status':'pending source-only check','compiled':False,'rendered':False,'mathematical_validation':False},
 'counts':{'C_actual_source_doubt_rows':11,'C_source_doubt_rows_resolved':1,'C_source_doubt_rows_retained':10,'C_source_doubt_local_records':13,'differences_records':len(d),'diff_C_true':sum(x['diff_C'] for x in d),'diff_H_true':sum(x['diff_H'] for x in d),'remaining_doubt_loci':len(doubts),'inventory_items':len(inv),'local_crops':len(manifest),'whole_views':1,'half_views':2,'local_crop_views':14,'successful_image_views':17,'failed_unseen_deliveries':0,'mathematical_check_events':0}
}
(B/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

md=r'''# Scan 020 — independent reader B

## Scope and processing

UTC start **2026-11-20 20:45:44 UTC**, recorded before the packet was read. The full v18 brief, preamble and requested packet were read. The first combined text delivery truncated a small part of `notation.md`; its complete text was then read alone. Whole scan, half a, half b, and all fourteen local crops were each successfully displayed once, one image per call. **17 successful views; no failed unseen deliveries; no reopened image.** A root checkpoint pause occurred after the complete visual phase; work resumed in this same context.

The full image measures 1683 × 2362; each supplied half measures 1683 × 1261. Crops use full-scan upper-left coordinates directly. The lower-half edge offset is 1101 (= 2362 − 1261); no image comparison or optional geometric calculation was performed. `crop_manifest.json`, `image_audit.json` and `make_crops.py` give the actual crops and processing.

## Line-by-line visual audit

| Physical line / region | Complete selected reading and audit |
| --- | --- |
| 1, y90–160 | **Ainsi les classes de Π_I [upper round mark] sont les**. Pi/I strokes clear; circle/zero unresolved locally (R01a, crop01). |
| 2, y167–273 | **classes de Π_J [upper round mark] distinctes de [Π overwritten by U] U_{J,i},**. Second circle/zero remains independently open (R01b, crop02). Pi predecessor, J, comma separator, dotted i, final comma confirmed (crop03). |
| 3, y294–365 | **et de plus les clas./deux. parmi**. Both word candidates retained; a distinct terminal point belongs to either candidate (R02, crop04). |
| 4, y391–498 | **U_{J,i} ∩ Σ_{old J+i / j / i}^+, U_{J,i} ∩ Σ_i^-**. First index remains a whole-state ambiguity (R03, crop05). The second index, minus and intervening comma were read on half a. No closure bar is supplied here. |
| 5, y520–681 | **qui sont non vides. Or les deux classes**. All prose, first period and word endings retained as seen on half a. |
| 6, y681–799 | **en question sont non vides, car**. Comma after vides retained. |
| 7, y775–898 | **[cancelled Σ_j/Σ_i] U_{J,i} est un voisinage de [Σ overwritten by E] E_{i/j}, et**. j is primary in the crossed index; i survives (R04, crop06). G01 draws two actual cancellation runs. Voisinage E index remains i/j (R05); predecessor Sigma and separate comma are confirmed (crop07). |
| 8, y906–1020 | **barred Σ_i^+ ∩ [Σ overwritten by E] E_i ≠ ∅, barred [E overwritten by Σ] Σ_i^- ∩ [Σ overwritten by E] E_i ≠ ∅. On sait donc**. Three predecessor bases confirmed; both closure bars already occur in C/H (crop08). **sait** resolved from its own word strokes (R10, crop09). |
| 9, y1040–1215 | **que le nb des classes est en [cancelled tout/est]**. Live en is separate from the cancelled word. The cancelled word stays qualified (R06, crop10). |
| 10, y1170–1310 | **(n−1)+2=n+1=card I+1 (ce qui achève**. Count read without arithmetic check. The complete ce qui achève crop includes the full q descender; the short descending-right accent supports the selected achève spelling (crop11). |
| 11, y1320–1410 | **aussi/ainsi la [small qualified upper-right point] dèm./dém./dem. par récurrence sur**. R11 retains both adverbs; R07 favors grave but keeps acute and unaccented candidates (crop12). G02 owns la and one qualified point; its attachment, role, hand and origin stay open. Compact par is retained as the selected visible reading; récurrence's acute was seen on half b. |
| 12, y1432–1538 | **le nb des classes).** Closing parenthesis and period retained. |
| 13, y1578–1697 | **Lemme** with one underline; **Toute classe de Π_I [upper round mark] est**. Third circle/zero remains recorded (R01c, crop13), with the first-candidate convention in TeX. |
| 14 / formula, y1630–1830 | **de la forme X \ indexed union (Σ_α^+ ∪ E_α)**, with **α ∈ [old I+K / K]**, and inserted **hat Σ_α^+** above the brace. Union upper loop/lower retrace and brace main run/left loop/retrace are literal G03 components. R08 retains complete index-state alternatives. No generic duplicate union or brace is present (crop13). |
| 15, y1765–1915 | **où K est une partie [inserted and cancelled non vide] de I, et**. The crossed wording is readable; G04 retains the rising cancellation with right return and the separate long curved insertion guide. It owns partie / non vide / de I, et once; une remains outside (crop13). |
| Left margin, y1885–2120 | Slanted **K est ≠∅ / si I ≠∅**, no interposed punctuation. Read on half b; both witnesses preserve the content. |
| 16, y1920–2050 | **∀α ∈ K, [cancelled on a] Σ_α^+ [qualified reworked relation] π₀(X \ E_α), tels que**. Cancelled on a is recoverable. R09 retains the literal curved body/shaft/head plus old double arrow + membership, old single arrow + membership, and membership/retracing interpretations (crop14). |
| 17, y2030–2170 | **∀α,β ∈ K, α≠β, on ait hat Σ_α^+ ∩ hat Σ_β^+=∅**. Each local index, both hats, plus signs, equality, commas and slashed empty form read on half b. |
| 18, y2175–2295 | **(⇔ Σ_α^+ ∩ Σ_β^+=∅).** Both Sigma forms un-hatted; both plus signs, double arrow, equality, parentheses and endpoint point retained. |
| Foot, y2300–2345 | Archive **19**, undetermined hand; TeX comment only. No manuscript page number is supplied. |

## Original C doubts — actual source identities

The source's **Doubtful readings** section contains **11 rows**. Its seven notation rows and its one retained-slip row are not counted as doubts. R01 includes three separately inspected rings; no source row is silently split or attached to a neighbor.

| Row in original order | Source scope | Return |
| --- | --- | --- |
| R01 | opening and lemma, circle / 0 | Retained at opening I, opening J and lemma I; one first printed qualifier, three local records. |
| R02 | line3, clas. / deux | Retained; definite terminal point applies to both complete candidates. |
| R03 | first paired intersection, i on J / j / i | Retained as complete states. |
| R04 | cancelled Sigma before U, i / j | Retained; j is now primary, i alternative; two cancellation runs explicit. |
| R05 | voisinage E index, i / j | Retained, independent of predecessor base and separate comma. |
| R06 | cancelled word before count, tout / est | Retained. |
| R07 | proof abbreviation, dém. / dem. | Retained with grave-primary **dèm.**, acute and unaccented alternatives explicit. |
| R08 | old I under union K | Retained as **deleted I K / K**; glyph/state question preserved. |
| R09 | sign before π₀, ⇒ / implicit absence | Retained as literal geometry and full arrow/membership state alternatives. |
| R10 | On voit / sait | **Resolved: sait.** |
| R11 | aussi / ainsi | Retained. |

## Explicit source boundaries and geometry

`B_G01` has one visible Sigma/index node, one invisible deletion annotation and two visible crossing paths. `B_G02` has la once and one locally qualified point; the inner base-west origin, baseline, zero separations and translation are declared. `B_G03` owns the union sign, qualified index, parenthesized body, raised hatted label and three brace paths; X setminus and the preceding Pi are outside. `B_G04` owns partie, the inserted/deleted non vide, and de I, et once; it has one cancellation path and one separate guide path. `B_G05` owns the entire local relation and then the formula continues with pi₀. Its formal readings are editorial alternatives within the qualifier, not additional physical occurrences.

All path coordinates are manual approximations from the single planned crops. Source origins and fixed rectangles describe the chosen coordinate maps; they do not establish pixel or rendered equality. No compiler, rendering or optional curve/extrema/pixel comparison was used. The full selected TeX is the authority for word boundaries and visible components; `graphic_groups` in the report exposes them.

## S and witness coverage

S row **SA01-K81-06**, item SA01-29, states **81/15–22** and explicitly records that its author viewed **no scan**. It is treated as a witness proposal. This page has two locally visible closure bars, both already present in current C/H. Its exact quoted example strings do not occur verbatim here; no current-witness bar omission is invented and no bar is inferred on an unbarred expression.

H supplies full text. Its note on the neighboring proof pages is apparatus. Its raised-hat note describes the one existing inserted label and creates no second formula. H's three ill placeholders each get one physical recovery count; local uncertainties inside them remain attached to that parent. Emphasis/underline macro conversion alone is not counted. The scan20/H-page19 mapping and archive-number comment are administrative source choices with no ink-correction count.

## Mathematical account and limits

The author writes the count and the claim that the parenthesis completes an induction on the number of classes. The lemma states the complement-of-unions form, a π₀ membership condition and pairwise hatted-set disjointness, followed by a written equivalence with the un-hatted disjointness expression. These are the author's assertions. Reading them supplied no proof check, reconstructed theorem or repair. **`check_events` is empty.**

Counts and source-only validation results are recorded in `report.json`; no image remains scheduled for viewing.
'''
(B/'reading.md').write_text(md)
print(json.dumps(report['counts'],ensure_ascii=False))
