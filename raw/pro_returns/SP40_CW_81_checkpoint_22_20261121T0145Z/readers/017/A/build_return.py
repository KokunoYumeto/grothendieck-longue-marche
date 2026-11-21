from pathlib import Path
import json
out=Path('/workspace/scratch/94548b74fbe0/out/readers/017/A')
tex=r'''\scanpage{17}
\uline{Cas particuliers}

Supposons que $\forall i\in I$, \deleted{$E_i$ \unsure{est|soit} rare dans $X$.} \inserted{on ait} (si $\Sigma_i^+\ \Sigma_i^-$ sont les deux comp. conn. de $X\setminus\Sigma_i$)

\deleted{Alors on trouve que}
\[
\begin{aligned}
\overline{\Sigma_i^+} &= \Sigma_i^+\cup E_i\\
\overline{\Sigma_i^-} &= \Sigma_i^-\cup E_i .
\end{aligned}
\]

Alors je dis qu'on a
\[
\overline{\Sigma_{12}}=\Sigma_{12}
% G01: retraced cup; full-scan origin (944,783), fixed local rectangle 36 by 36.
\mathbin{\vcenter{\hbox{\begin{tikzpicture}[x=0.007cm,y=-0.007cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (36,36);
\draw[line width=0.55pt,line cap=round,line join=round] (7,5) .. controls (7,13) and (7,21) .. (9,25) .. controls (18,33) and (32,30) .. (32,14) -- (30,7);
\draw[line width=0.4pt,line cap=round,line join=round] (25,7) .. controls (32,20) and (20,32) .. (8,25);
\end{tikzpicture}}}} E_1\cup E_2
\]

% G02: short curved separator with downturned right endpoint.
% Full-scan origin (300,887); fixed local rectangle 240 by 22.
\figure{\begin{tikzpicture}[x=0.01cm,y=-0.01cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (240,22);
\draw[line width=0.3pt,line cap=round] (2,14) .. controls (70,5) and (181,4) .. (232,8) .. controls (238,9) and (239,10) .. (238,14);
\end{tikzpicture}}

% slanted
\reversemarginpar
\margin{introduire la partition $\unsure{\Pi|\pi}_j=\{\deleted{\unsure{\Sigma}}E_j,\Sigma_j^+,\Sigma_j^-\}$}
\normalmarginpar
\deleted{Supposons}

Soit $J\subset I$ tel que $I=J\amalg\{i\}$.

Considerons la partition
% G03: upper Pi_J insertion and curved guide. Source origin (1215,1100).
% Fixed rectangle 175 by 135; base-west anchors and zero node separations.
\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(pide.base)]
\path[use as bounding box] (0,0) rectangle (175,135);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (6,65) {\inserted{$\Pi_J$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (pide) at (105,124) {de};
\draw[line width=0.3pt,line cap=round] (68,120) .. controls (73,91) and (129,99) .. (153,84) -- (152,79);
\end{tikzpicture}
$X$ \deleted{definie} definie par les $\deleted{\Sigma}E_j$ $(j\in J)$, \deleted{et} \unsure{Intersection|intersection} des partitions
% G04: ternaires Pi_j insertion and its long bent caret. Source origin (970,1345).
\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(terde.base)]
\path[use as bounding box] (0,0) rectangle (335,135);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,57) {\inserted{ternaires $\Pi_j$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (terde) at (270,118) {de};
\draw[line width=0.35pt,line cap=round,line join=round] (161,64) .. controls (177,65) and (206,70) .. (215,89) -- (218,105) .. controls (233,80) and (246,62) .. (260,48);
\end{tikzpicture}
$X$ $(j\in J)$ definies par les $E_j$ \deleted{$\unsure{\in|E}$} $(j\in J)$
\[
X=E_j\amalg\coprod_{\alpha\in\pi_0(X\setminus E_j)}\Sigma_j^{\unsure{\prime|\cdot}\alpha}
\]
% G05 is the small detached oblique mark immediately before upper alpha.
% It is represented once by the qualified prime/dot candidate above; no role is assigned.

-- c'est aussi la partition definie par celle de $\displaystyle\unsure{.}\,\bigcup_{j\in J}E_j$ en les $E_j$, et la partition
% G06 is the detached baseline point before the first indexed union, represented once above.
% G07: lower Pi_J insertion and curved guide. Source origin (770,1965).
\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=(lowde.base)]
\path[use as bounding box] (0,0) rectangle (145,100);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (4,54) {\inserted{$\Pi_J^{\unsure{\circ|0}}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (lowde) at (69,85) {de};
\draw[line width=0.3pt,line cap=round] (39,89) .. controls (40,65) and (55,62) .. (76,56) .. controls (93,51) and (119,40) .. (122,34) -- (118,30);
\end{tikzpicture}
$\displaystyle X\setminus
% G08: union with visible transverse stroke; interpretation of stroke stays qualified.
% Full-scan origin (1115,1970), fixed local rectangle 80 by 75.
\mathop{\unsure{\vcenter{\hbox{\begin{tikzpicture}[x=0.009cm,y=-0.009cm,baseline=0pt]
\path[use as bounding box] (0,0) rectangle (80,75);
\draw[line width=0.45pt,line cap=round] (18,9) .. controls (13,34) and (18,60) .. (38,63) .. controls (61,67) and (70,39) .. (63,10);
\draw[line width=0.4pt,line cap=round] (12,20) .. controls (26,20) and (39,17) .. (59,18);
\end{tikzpicture}}}}}\limits_{j\in J}E_j$
intersection des partitions binaires $\Pi_{J,j}^{\circ}$
% G09: inserted quantifier and guide over induites. Source origin (1230,2070).
% The recurring circle/zero doubt is marked at its first occurrence above.
\begin{tikzpicture}[x=0.0075cm,y=-0.0075cm,baseline=(induites.base)]
\path[use as bounding box] (0,0) rectangle (335,115);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (60,45) {\inserted{$(j\in J)$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (induites) at (52,91) {induites};
\draw[line width=0.3pt,line cap=round] (14,92) .. controls (0,72) and (30,57) .. (53,53) .. controls (99,66) and (189,54) .. (219,41) .. controls (224,39) and (216,32) .. (214,31);
\end{tikzpicture}
% G10: inserted U_J= and guide curling down to the right of sur.
% Full-scan origin (320,2155); fixed local rectangle 145 by 155.
\begin{tikzpicture}[x=0.008cm,y=-0.008cm,baseline=(sur.base)]
\path[use as bounding box] (0,0) rectangle (145,155);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (43,61) {\inserted{$U_{\unsure{\deleted{J}J|\deleted{j}J|J}}={}$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] (sur) at (0,111) {sur};
\draw[line width=0.3pt,line cap=round] (56,72) .. controls (88,81) and (111,74) .. (124,99) .. controls (133,121) and (132,138) .. (136,148);
\end{tikzpicture}
$\displaystyle X\setminus\bigcup_{j\in J}E_j$ par les $\Pi_j$ $(\unsure{g|j}\in J)$. Pour
% archive sheet number: 16
'''
(out/'reading.tex').write_text(tex,encoding='utf-8')
D=[]
def d(id,location,C,H,reading,evidence,confidence,kind,diff_C,diff_H,status=None,crop=None,bbox=None,row=None,part=None,consequence=None,**extra):
 o={'id':id,'location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':diff_C,'diff_H':diff_H,'C_doubt_status':status,'readers_crop':crop,'bbox':bbox}
 if row:o['C_source_row']=row
 if part:o['C_local_part']=part
 if consequence:o['mathematical_consequence']=consequence
 o.update(extra);D.append(o)
d('A017-D01','Deleted first supposition: subject',r'\unsure{E_i|\Sigma_i}',r'E_i',r'E_i','A left vertical and three separate horizontal levels survive the crossing strokes; the lowered i is retained.','medium','other',True,False,'resolved','01_upper_correction.png',[1040,213,1146,282],'R01','subject E_i versus Sigma_i')
d('A017-D02','Deleted first supposition: verb',r'\unsure{est}','soit',r'\unsure{est|soit}','A short low run and final tall crossed stem support est first; the densely crossed middle does not settle the competing soit reading. H remains an explicit alternative, not a conclusively excluded reading.','low','misread word',True,True,'retained','01_upper_correction.png',[1112,226,1247,277],'R01','verb est')
d('A017-D03','Deleted first supposition: adjective',r'\unsure{rare|dense}','rare','rare','Two short r-like shoulders with an intervening low rounded a and terminal e survive; no distinct initial tall d is visible in this word.','medium','other',True,False,'resolved','01_upper_correction.png',[1248,238,1400,280],'R01','adjective rare versus dense')
d('A017-D04','Parenthesis following on ait','si','où','si','The small s loop and separate i stroke are visible immediately after the opening parenthesis.','high','misread word',False,True,crop='01_upper_correction.png',bbox=[1395,184,1477,242])
d('A017-D05','End of deleted first sentence','X.','X','X.','A distinct dark point follows the crossed X.','high','omission',False,True,crop='01_upper_correction.png',bbox=[1530,236,1614,288])
d('A017-D06','Raised on ait',r'\inserted{on ait}','on ait',r'\inserted{on ait}','The words sit above the cancelled clause, with a clear vertical displacement.','high','insertion or placement',False,True,crop='01_upper_correction.png',bbox=[1134,186,1343,236])
d('A017-D07','Cancelled sentence before two equalities',r'\unsure{trouve}','trouve','trouve','The tall initial t, short following shoulder, low round/return strokes and final e-like return remain visible beneath the long cancellation line.','medium','other',True,False,'resolved','02_struck_sentence.png',[553,328,732,381],'R02','trouve')
d('A017-D08','First equality endpoint after E_i','no comma',r'E_i,','no comma','The index has its dot and stem; the area immediately to its right contains no comma. The separate point beside the second equality is retained as that equality\'s endpoint.','high','text not on the page',False,True,crop='03_equation_endpoints.png',bbox=[940,425,1080,495])
d('A017-D09','Sentence before third equality',"Alors je dis qu'on a",'Alors je dis que',"Alors je dis qu'on a",'The half shows an apostrophe after qu, the low on run, and a separate small final a oval.','high','omission',False,True,bbox={'image':'half a','origin':'upper left','box':[300,620,1000,776]})
d('A017-D10','First join of Sigma12 equality',r'\unsure{\cup|\amalg}',r'\cup','cup form with doubled curved right return, drawn as G01','Both surviving bottoms curve upward into the right arms. Two distinct right returns are present. The cup reading is selected; the extra return is drawn without assigning a correction chronology.','medium','drawing or diagram',True,True,'resolved','04_first_join.png',[944,783,980,819],'R03','first join',physical_cluster='G01',shape_confidence='high',role_of_retracing='unestablished')
d('A017-D11','Separator below third equality',r'\rule{2.4cm}{0.3pt}','omitted','G02: shallow curved rule with downturned right endpoint','The half shows a shallow rise across the rule and a small downward turn at the right end.','high','drawing or diagram',True,True,bbox={'image':'half a','origin':'upper left','box':[297,884,543,910]},physical_cluster='G02')
d('A017-D12','Opening of slanted margin note','introduire','introduisons','introduire','After introdui the surviving short shoulder and low terminal return support re; the longer sons ending is not written.','medium','misread word',False,True,crop='05_margin_note.png',bbox=[39,943,260,1115])
d('A017-D13','Slanted margin partition name',r'\unsure{\Pi|\pi}_j',r'\Pi_j',r'\unsure{\Pi|\pi}_j','A connected top and two legs are visible. The local capital/lowercase scale remains insufficiently distinct.','medium','other',False,False,'retained','05_margin_note.png',[31,1217,111,1321],'R04','Pi versus pi')
d('A017-D14','Cancelled predecessor within marginal E_j',r'\deleted{\unsure{\Sigma}}E_j',r'E_j ... \ill{}',r'\deleted{\unsure{\Sigma}}E_j','Angular dark remnants are superimposed on E. Sigma remains the supported but uncertain predecessor. The inspected note ends at its closing brace; H\'s trailing ill is not assigned an invented extra word. This is the single H placeholder/cancellation cluster for this note.','low',r'readable ink left as \ill{}',False,True,'retained','05_margin_note.png',[132,1146,190,1206],'R04','crossed Sigma',H_parent='H-MARGIN-ILL')
d('A017-D15','Start of main lower paragraph','Considérons','Considérons','Considerons','The entire word and the area above its e are visible; no detached acute stroke is present.','high','abbreviation expanded or spelling modernised',True,True,crop='17_considerons.png',bbox=[315,1148,713,1222])
d('A017-D16','Upper Pi_J insertion over de',r'\inserted{\Pi_J} de',r'\add{\Pi_J} de','same words with literal guide G03','The half shows a separate curved stroke rising from the gap before de toward an upturned right endpoint below the raised name. The insertion state itself agrees with both witnesses.','high','drawing or diagram',True,True,bbox={'image':'half a','origin':'upper left','box':[1215,1100,1390,1235]},physical_cluster='G03')
d('A017-D17','Cancelled word following de X',r'\deleted{\unsure{des parties|définie}}',r'\struck{définie}',r'\deleted{definie}','The cancelled word begins d-e followed by one tall descending f and the short i/n/i/e continuation. There is no detached acute above e. The live following word has its own separate strokes.','medium','misread word',True,True,'resolved','06_cancelled_definie.png',[420,1263,650,1388],'R05','cancelled wording')
d('A017-D18','Live word after cancelled definie','définie','définie','definie','The low e between d and the tall f has blank space above it, with no separate acute.','high','abbreviation expanded or spelling modernised',True,True,crop='06_cancelled_definie.png',bbox=[682,1260,884,1370])
d('A017-D19','Predecessor beneath first E_j after les',r'\deleted{\Sigma}E_j',r'E_j',r'\deleted{\Sigma}E_j','The diagonal middle and returning lower limb of Sigma remain beneath the E bars; a separate diagonal crosses this cluster. C\'s doubt-table row qualifies this locus although C.tex has no unsure macro here.','high','omission',True,True,'resolved','07_first_E_predecessor.png',[1283,1277,1366,1379],'R07','first predecessor Sigma')
d('A017-D20','Cancelled opening before intersection',r'\deleted{\unsure{et}}',r'\struck{intersection}\add{intersection}',r'\deleted{et}','A small e followed by a tall t survives under the short low crossing. One following continuous word is visible. This H correction cluster is counted here once; its live word qualification is D21.','medium','deletion state (struck given live or live given struck)',True,True,'resolved','08_intersection_start.png',[327,1428,406,1484],'R06','et',H_parent='H-INTERSECTION-CLUSTER')
d('A017-D21','Live word following cancelled et',r'\unsure{intersection}',r'\struck{intersection}\add{intersection}',r'\unsure{Intersection|intersection}','The leading stroke rises well above the low bodies and has no separable initial i dot. The remainder supports intersection. Capital I is selected with lowercase retained; the opening remains crowded. H\'s duplication/insertion state is collated once in D20.','low','misread word',True,False,'retained','08_intersection_start.png',[400,1409,652,1487],'R06','intersection',H_parent='H-INTERSECTION-CLUSTER')
d('A017-D22','Guide beneath inserted ternaires Pi_j',r'\inserted{ternaires \Pi_j}',r'\add{ternaires \Pi_j}','same insertion plus G04 bent caret','The lower half shows a low curved left arm descending into a long pointed caret and a rising right arm. Both endpoints are visible.','high','drawing or diagram',True,True,bbox={'image':'half b','origin':'upper left','box':[970,244,1305,394]},physical_cluster='G04')
d('A017-D23','Plural defined word before second E_j','définies','définies','definies','Both i dots and the ending are visible. The region above the e before f has no acute.','high','abbreviation expanded or spelling modernised',True,True,crop='18_definies.png',bbox=[550,1519,730,1616])
d('A017-D24','Cancelled isolated sign after later E_j',r'\deleted{\unsure{E|\in}}',r'\ill{}',r'\deleted{\unsure{\in|E}}','Two curved lobes with an open right side lie beneath a rising cancelling slash. Membership is the stronger candidate; E survives as an alternative.','low',r'readable ink left as \ill{}',True,True,'retained','09_later_cancelled_sign.png',[1181,1507,1217,1584],'R07','later isolated E/in',H_parent='H-LATER-SIGN-ILL')
d('A017-D25','Small upper mark before alpha in partition display','omitted','omitted',r'\Sigma_j^{\unsure{\prime|\cdot}\alpha}','A short dark detached oblique dab lies between the Sigma head endpoint and alpha. Its shape supports prime/dot candidates; hand, origin and role are unestablished. It is represented once at its observed upper position.','medium','omission',True,True,crop='10_partition_display.png',bbox=[1190,1624,1200,1636],physical_cluster='G05',shape_confidence='high')
d('A017-D26','Final defined word in c\'est aussi paragraph','définie','définie','definie','The enlarged word shows d-e-f and both i dots; there is no detached acute over e.','high','abbreviation expanded or spelling modernised',True,True,crop='19_last_definie.png',bbox=[1116,1745,1298,1826])
d('A017-D27','Detached baseline point before first large union','omitted','omitted',r'\unsure{.}\,\bigcup_{j\in J}E_j','A compact dark horizontal point sits to the left of the cup near its lower baseline. No connection or mathematical role is supplied. Hand and surface origin remain undetermined.','medium','omission',True,True,crop='11_first_union_dot.png',bbox=[734,1899,743,1907],physical_cluster='G06',shape_confidence='high')
d('A017-D28','Inserted Pi_J upper ring',r'\Pi_J^{\unsure{\circ|0}}',r'\Pi_J^0',r'\Pi_J^{\unsure{\circ|0}}','A small raised nearly round open-centred loop is visible. Its circular shape alone leaves circle/zero unresolved. H\'s zero is retained explicitly as the alternative.','medium','misread symbol or index',False,True,'retained','12_inserted_partition_ring.png',[831,1974,854,1996],'R08','inserted Pi_J upper ring')
d('A017-D29','Guide beneath inserted lower Pi_J',r'\inserted{\Pi_J^{\circ|0}} de',r'\add{\Pi_J^0} de','same wording and ring qualification with guide G07','A long independent curved stroke begins before de, rises beneath the inserted name and ends with a short upward hook at the right.','high','drawing or diagram',True,True,crop='12_inserted_partition_ring.png',bbox=[805,1991,897,2059],physical_cluster='G07')
d('A017-D30','Middle large union after X complement',r'\unsure{\overline{\bigcup}|\bigcup}',r'\bigcup','G08: visible cup plus short transverse stroke; role locally qualified','The horizontal crosses the left stem below its top and ends before the right stem. Its presence is resolved. Its interpretation as an overbar or another stroke remains unestablished, so the literal two-path graphic is qualified locally.','high','drawing or diagram',True,True,'resolved','13_middle_union.png',[1121,1974,1188,2040],'R11','bar presence',physical_cluster='G08',interpretation_confidence='low')
d('A017-D31','Binary partition name upper ring',r'\Pi_{J,j}^{\circ}',r'\Pi_{J,j}^0',r'\Pi_{J,j}^{\circ} (circle/zero qualification inherited from first occurrence)','The separate small raised ring has an open centre. The same circle/zero uncertainty persists at this independently inspected occurrence. C\'s source R08 explicitly includes it despite no unsure macro here.','medium','misread symbol or index',False,True,'retained','14_binary_partition_guide.png',[1185,2125,1209,2148],'R08','binary partition name ring')
d('A017-D32','Inserted quantifier and apparent opening parenthesis at induites',r'\inserted{(j\in J)} induites',r'\add{(j\in J)} (induites','inserted quantifier and induites with G09 guide; no prose opening parenthesis','The putative left parenthesis continues upward into one long curved rule under the added quantifier, terminating in a small upturned right hook. The complete path is preserved.','high','drawing or diagram',True,True,crop='14_binary_partition_guide.png',bbox=[1233,2101,1461,2170],physical_cluster='G09')
d('A017-D33','U subscript: predecessor and replacement state',r'U_{\deleted{\unsure{J|j}}J}',r'U_J',r'U_{\unsure{\deleted{J}J|\deleted{j}J|J}}','Two displaced lower feet are visible with one heavier final right stem and upper bar. The predecessor supports J/j; the strokes also leave one retraced J as a complete-state alternative. No writing chronology is inferred. H\'s J remains an explicit complete-state alternative.','low','deletion state (struck given live or live given struck)',True,True,'retained','15_U_subscript.png',[390,2179,424,2233],'R12','predecessor J versus j and state',physical_cluster='U-SUBSCRIPT')
d('A017-D34','U subscript: final capital J','J','J','J in all selected complete-state alternatives','The final heavier stem has a horizontal top and left-returning foot. This confirmation is separate from the predecessor/state doubt and makes no additional witness change.','high','other',False,False,crop='15_U_subscript.png',bbox=[396,2184,425,2233],row='R12',part='final J',physical_cluster='U-SUBSCRIPT')
d('A017-D35','U_J equals insertion and guide around sur',r'\inserted{U_J={}}',r'U_J=','insertion retained, with literal G10 guide','The name and equality are raised above sur. A separate line runs below the name and curves down to the right of sur; its entire endpoint is included in the crop. H prints the name at the baseline.','high','insertion or placement',True,True,crop='15_U_subscript.png',bbox=[359,2159,460,2307],physical_cluster='G10')
d('A017-D36','Final quantified letter',r'\unsure{g|j}',r'j',r'\unsure{g|j}','A small closed upper loop is followed by a long descending stem and leftward foot. The loop supports g first; j remains possible in the crowded joining strokes. H\'s j is expressly retained as an alternative.','low','misread symbol or index',False,True,'retained','16_final_words.png',[1251,2241,1289,2312],'R09','g versus j')
d('A017-D37','Final parenthesis count',r'(g|j\in J).',r'(j\in J)).',r'(\unsure{g|j}\in J).','One closing curve and a separate full stop follow J. There is no second closing curve. The guide misread as an opening parenthesis is recorded separately in D32.','high','text not on the page',False,True,crop='16_final_words.png',bbox=[1378,2218,1461,2295])
d('A017-D38','Final word',r'\unsure{Pour|Puis}',r'\uncertain{Pour}','Pour','The P is followed by a small round o reduced to a dark point and a low u/r run. There is no raised dot for an internal i. The decision uses this page alone; the witness\'s next-sheet argument is not used.','medium','other',True,False,'resolved','16_final_words.png',[1500,2214,1641,2293],'R10','Pour versus Puis')

I=[]
def inv(el,kind,pos,first,hand='his hand',**extra):
 o={'sheet_kind':'text','hand':hand,'element':el,'kind':kind,'position':pos,'first_words_or_objects':first,'transcribed':'yes'};o.update(extra);I.append(o)
inv('017.A.01','text','top heading, single continuous underline','Cas particuliers; underlining reproduced')
inv('017.A.02','text','upper two prose lines','Supposons que ∀i∈I; si Σ_i+ Σ_i−; comp. conn.; X\\Sigma_i')
inv('017.A.03','deletion','right of first prose line','E_i unsure(est|soit) rare dans X.')
inv('017.A.04','insertion','above previous cancellation','on ait')
inv('017.A.05','deletion','immediately above first display','Alors on trouve que')
inv('017.A.06','display','upper quarter, two rows','barred Σ_i+ and Σ_i− equalities, lower endpoint point retained at far right')
inv('017.A.07','text','above third equality',"Alors je dis qu'on a")
inv('017.A.08','display','above short separator','barred Σ_12 = Σ_12, G01, E_1 ∪ E_2')
inv('017.A.09','drawing','first join in third equality','G01 two curved right returns; literal two paths',components=['G01 path 1 outer cup','G01 path 2 inner return'])
inv('017.A.10','drawing','separator after third equality','G02 shallow curved rule with downturned right end')
inv('017.A.11','margin note','slanted along left middle margin','introduire la partition unsure(Pi|pi)_j = {cancelled uncertain Sigma, E_j, Sigma_j+, Sigma_j−}')
inv('017.A.12','deletion','within marginal E_j','cancelled uncertain Sigma predecessor')
inv('017.A.13','deletion','below separator','Supposons')
inv('017.A.14','text','middle line','Soit J subset I tel que I = J amalg {i}.')
inv('017.A.15','text','main lower paragraph through second quantifier before display','Considerons la partition; definie; unsure Intersection|intersection; definies')
inv('017.A.16','insertion','above first de X','Pi_J')
inv('017.A.17','drawing','at preceding insertion','G03 curved guide; one path')
inv('017.A.18','deletion','after de X','definie')
inv('017.A.19','deletion','beneath first E_j after les','Sigma predecessor')
inv('017.A.20','deletion','beginning of next physical line','et')
inv('017.A.21','insertion','following partitions','ternaires Pi_j')
inv('017.A.22','drawing','under ternaires Pi_j','G04 bent pointed guide; one connected path')
inv('017.A.23','deletion','after later E_j','unsure in|E under rising slash')
inv('017.A.24','display','lower middle','X = E_j amalg coproduct over alpha in pi_0(X minus E_j) of Sigma_j with upper mark and alpha')
inv('017.A.25','drawing','just before alpha in display exponent','G05 detached oblique mark, unsure prime|dot','undetermined hand',role='unestablished',surface_origin='unestablished')
inv('017.A.26','text','bottom paragraph through final Pour',"-- c'est aussi la partition definie; indexed unions; binary partitions; induced partitions; Pour")
inv('017.A.27','drawing','left of first indexed union, near its baseline','G06 compact detached point, locally qualified','undetermined hand',role='unestablished',surface_origin='unestablished')
inv('017.A.28','insertion','above de before first complement in final paragraph','Pi_J with unsure circle|zero')
inv('017.A.29','drawing','below previous insertion','G07 curved guide with upturned right endpoint; one path')
inv('017.A.30','drawing','middle large union, first complement of last paragraph','G08 cup plus transverse stroke; role locally qualified',components=['G08 path 1 cup','G08 path 2 transverse stroke'])
inv('017.A.31','insertion','above induites','(j in J)')
inv('017.A.32','drawing','over induites','G09 long curved insertion guide; one path')
inv('017.A.33','insertion','above sur','U with complete-state subscript alternatives, equals')
inv('017.A.34','deletion','within U subscript','qualified cancelled J then J; cancelled j then J; or one retraced J',state_confidence='low')
inv('017.A.35','drawing','below U name, curling down right of sur','G10 complete insertion guide; one path')
inv('017.A.36','text','bottom left','archive numeral 16, recorded in comment only','undetermined hand')

rowmap=[
 {'row':'R01','source_place':'first line directly under on ait','parts':{'subject':'A017-D01','verb':'A017-D02','adjective':'A017-D03'}},
 {'row':'R02','source_place':'struck sentence above equalities','parts':{'trouve':'A017-D07'}},
 {'row':'R03','source_place':'third equality, first join','parts':{'join':'A017-D10'}},
 {'row':'R04','source_place':'left note','parts':{'Pi/pi':'A017-D13','crossed Sigma':'A017-D14'}},
 {'row':'R05','source_place':'after de X','parts':{'cancelled wording':'A017-D17'}},
 {'row':'R06','source_place':'start of intersection','parts':{'et':'A017-D20','intersection':'A017-D21'}},
 {'row':'R07','source_place':'under E_j and after later E_j','parts':{'first Sigma':'A017-D19','later E/in':'A017-D24'}},
 {'row':'R08','source_place':'Pi_J above de, and binary partition name','parts':{'inserted ring':'A017-D28','binary ring':'A017-D31'}},
 {'row':'R09','source_place':'last parenthesis','parts':{'g/j':'A017-D36'}},
 {'row':'R10','source_place':'last word at right edge','parts':{'Pour/Puis':'A017-D38'}},
 {'row':'R11','source_place':'first complement after inserted Pi_J','parts':{'transverse bar presence':'A017-D30'}},
 {'row':'R12','source_place':'above sur, U subscript','parts':{'predecessor and complete state':'A017-D33','final J':'A017-D34'}}
]
doubts=[
 {'location':'first cancelled verb','reading':'est','alternatives':['soit'],'confidence':'low','reason':'crossing strokes conceal the short central letters','crop':'01_upper_correction.png','source_row':'R01','difference':'A017-D02'},
 {'location':'marginal partition name','reading':'Pi','alternatives':['pi'],'confidence':'medium','reason':'connected top and legs do not settle local case/size','crop':'05_margin_note.png','source_row':'R04','difference':'A017-D13'},
 {'location':'marginal E predecessor','reading':'cancelled Sigma','alternatives':[],'confidence':'low','reason':'surviving angular under-strokes are crowded','crop':'05_margin_note.png','source_row':'R04','difference':'A017-D14'},
 {'location':'after cancelled et','reading':'Intersection','alternatives':['intersection'],'confidence':'low','reason':'leading stroke tall and crowded; capital/lowercase unsettled','crop':'08_intersection_start.png','source_row':'R06','difference':'A017-D21'},
 {'location':'sign after later E_j','reading':'cancelled in','alternatives':['cancelled E'],'confidence':'low','reason':'lobes crossed by rising slash','crop':'09_later_cancelled_sign.png','source_row':'R07','difference':'A017-D24'},
 {'location':'detached upper mark before alpha','reading':'prime-shaped mark','alternatives':['dot-shaped mark'],'confidence':'medium','reason':'shape clear, character/role/hand/origin unestablished','crop':'10_partition_display.png','difference':'A017-D25'},
 {'location':'point before first union','reading':'baseline point','alternatives':[],'confidence':'medium','reason':'character role, hand and surface origin unestablished','crop':'11_first_union_dot.png','difference':'A017-D27'},
 {'location':'inserted Pi_J superscript','reading':'circle','alternatives':['zero'],'confidence':'medium','reason':'raised round open-centred loop supports both','crop':'12_inserted_partition_ring.png','source_row':'R08','difference':'A017-D28'},
 {'location':'middle union transverse stroke','reading':'literal cup with transverse stroke','alternatives':['overbar interpretation','unassigned extra stroke interpretation'],'confidence':'low','reason':'presence clear; mathematical role unestablished','crop':'13_middle_union.png','source_row':'R11','difference':'A017-D30'},
 {'location':'binary Pi_{J,j} superscript','reading':'circle','alternatives':['zero'],'confidence':'medium','reason':'same local round-loop ambiguity; first occurrence carries the explicit TeX doubt','crop':'14_binary_partition_guide.png','source_row':'R08','difference':'A017-D31'},
 {'location':'U subscript','reading':'cancelled J followed by live J','alternatives':['cancelled j followed by live J','one retraced J'],'confidence':'low','reason':'two displaced feet do not determine separate cancellation and replacement states','crop':'15_U_subscript.png','source_row':'R12','difference':'A017-D33'},
 {'location':'final quantifier','reading':'g','alternatives':['j'],'confidence':'low','reason':'closed loop and descending foot remain locally ambiguous','crop':'16_final_words.png','source_row':'R09','difference':'A017-D36'}
]
notation=[
 {'location':'title','sign':'single underline','latex':r'\uline{Cas particuliers}','evidence':'one continuous line under both words'},
 {'location':'two upper equations and preceding parenthesis','sign':'signed Sigma with lowered dotted i; separate closure rules','latex':r'\Sigma_i^+,\Sigma_i^-,\overline{\Sigma_i^+},\overline{\Sigma_i^-}','evidence':'signed letters and upper rules inspected on half a; no mathematical inference'},
 {'location':'upper parenthesis','sign':'comp. conn.','latex':'comp. conn.','evidence':'points after the two abbreviations retained; no expansion'},
 {'location':'third equality','sign':'bar over Sigma12; retraced curved join','latex':r'\overline{\Sigma_{12}}; G01','evidence':'separate upper rule and two curved right returns'},
 {'location':'Soit and lower display','sign':'square join with extended foot','latex':r'\amalg','evidence':'uprights and horizontal extended base; H sqcup treated as same local reading, no macro-only row'},
 {'location':'partition display','sign':'large coproduct, lowered alpha in pi_0(X minus E_j)','latex':r'\coprod_{\alpha\in\pi_0(X\setminus E_j)}','evidence':'wide squared bottom and upright legs; small pi and low round zero visible in crop10'},
 {'location':'named main partitions','sign':'capital Pi and capital J index','latex':r'\Pi_J,\Pi_j,\Pi_{J,j}','evidence':'joined cap with two legs; J has upper bar and returning foot'},
 {'location':'two lower superscripts','sign':'small upper ring','latex':r'\Pi_J^{\unsure{\circ|0}};\Pi_{J,j}^{\circ}','evidence':'two independently inspected open-centred loops; recurring-doubt convention'},
 {'location':'main lower prose','sign':'locally absent acute strokes','latex':'Considerons; definie (cancelled); definie; definies; definie','evidence':'separate source crops retained; no spelling normalization'},
 {'location':'foot','sign':'archive numeral','latex':'% archive sheet number: 16','evidence':'small pale 16 at lower-left page edge, half b'}
]
report={
 'scan':17,'reader':'A','start_utc':'2026-11-20 17:08:54 UTC','end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'model':'GPT-6 Astra Pro','effort':'not separately exposed',
 'differences':D,'doubts':doubts,'inventory':I,
 'notes':{
  'page_content':'Underlined Cas particuliers; an upper supposition and two recorded closure equalities; a further Sigma12 equality; a separator; a slanted partition note; and prose defining partitions for J, continuing through the final Pour. These are descriptions of the manuscript assertions, not proof endorsements.',
  'authors_own_uncertainty':{'exact_words':[],'comment':'No explicit authorial uncertainty formula was identified on this sheet; editorial reading doubts are recorded separately.'},
  'title_date_page_counts':{'title':'Cas particuliers','date':None,'author_page_number':None,'archive_number':'16','H_page':'16','comment':'H page16 is the metadata convention for our scan17. The visible pale16 is recorded only as the archive-number comment, not mspage.'},
  'source_scope':'Only the assigned packet, brief, PREAMBLE, notation snapshot, and scan017 images were read. The note in C R10 about a following sheet was not used as ink evidence. No other reader or later page was inspected.',
  'workflow':'Brief read first; current UTC start was then recorded before packet/image reading. Whole scan opened once for layout, half a once, half b once. Sixteen initial distinct tight crops and three later previously uncropped accent loci were each displayed once. No successfully viewed image or decided locus was reopened. No crop retry occurred.',
  'coordinates':'Full scan is 1685x2363. Half a is 1685x1261 and starts at full y=0. Half b is 1685x1262; bottom alignment yields full y=half-b y+1101, using 2363-1262. Report full boxes use upper-left origin and [left,top,right,bottom]. Unrotated crop display coordinates use x_full=left+x_display*(right-left)/2600 and y_full=top+y_display*(bottom-top)/output_height. These maps locate hand-estimated graphical anchors. The rotated marginal crop was used for reading without a computed inverse rotation.',
  'graphics':'G01 and G08 each contain two literal draw paths. G02,G03,G04,G07,G09,G10 each contain one. G05 is represented once by a qualified prime/dot candidate, and G06 once by a qualified baseline point. Every insertion-guide path appearing in reading.tex has its own difference and inventory item. Local drawing origins, rectangles, coordinate units, baselines and zero-separation base-west text anchors are declared in TeX; font extents are not asserted to coincide with the source boxes.',
  'crop_bounds':'All intended target ascenders, descenders and guide endpoints are included. Some crops contain clipped unrelated adjacent-line context, including the neighboring mark at the margin-note crop boundary and preceding/following formula remnants; none is supplied as an extra manuscript word. No target was recropped.',
  'mathematics_led_reading_decisions':'No mathematical computation, morphism, theorem verification or algebraic correspondence was used. The written X minus Sigma_i is preserved. No mathematical repair was made. Bars, cup shapes, indices, circle/zero doubts and the literal transverse union stroke were selected from strokes only.',
  'C_source_row_map':rowmap,
  'actual_computations':[
   {'operation':'image dimension reads','inputs':['J81-02_81_scan017.jpg','J81-02_81_scan017_a.jpg','J81-02_81_scan017_b.jpg'],'result':[[1685,2363],[1685,1261],[1685,1262]],'scope':'PIL metadata size only, no image comparison'},
   {'operation':'half-b coordinate offset','inputs':[2363,1262],'mapping':'2363-1262','result':1101,'scope':'source-coordinate conversion only'},
   {'operation':'crop processing','inputs':'nineteen exact boxes in crop_manifest.json','mapping':'crop; RGB autocontrast; only crop05 rotates -40 degrees with BICUBIC, expand and white fill; every crop becomes width2600 with height=round(pre_height*2600/pre_width), LANCZOS','result':'nineteen PNGs with recorded input/output dimensions in crop_manifest.json','scope':'visual legibility only; no OCR, pixel-difference calculation, registration, numerical curve analysis or image comparison'},
   {'operation':'graphical anchor coordinate conversion','inputs':'unrotated crop origins, original box dimensions, 2600 output width and recorded output heights','mapping':'affine coordinate formula in notes.coordinates','result':'hand-estimated full-scan path anchors declared for G01-G10 in reading.tex/report','scope':'placement approximations only, no computed identity or geometric theorem'}
  ],
  'structural_verification':'pending final source-only check',
  'reading_report_pair_review':'pending final complete joint read'
 },
 'notation':notation,'check_events':[],
 'crops':json.loads((out/'crop_manifest.json').read_text()),
 'brief_feedback':[
  'A local upper mark before alpha and a baseline point before the first union have supported visible shapes but no established role. The brief permits qualified candidates; these are kept without mathematical interpretation.',
  'The middle union bar is visibly inside the tops of the stems. Literal paths preserve that placement while the role remains qualified; a conventional overline would move it.',
  'Inline insertion-guide graphics need to include their adjacent attachment word once. The selected TeX uses zero-separation base-west nodes and declared local origins rather than duplicating the words in a separate illustration.'
 ]
}
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Wrote complete reading.tex and report.json under reader A directory.')
