from pathlib import Path
from datetime import datetime, timezone
import json
root=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_073/R1')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_073')
C=(packet/'C.tex').read_text(); H=(packet/'H.tex').read_text()
meta=json.loads((packet/'metadata.json').read_text())
crops=json.loads((root/'crop_manifest.json').read_text())
whole=meta['images'][0]; a=meta['images'][1]; b=meta['images'][2]
by_name={Path(x['path']).stem:x for x in crops}
D=[]
def diff(location,c,h,reading,evidence,confidence,kind,change_c,change_h,crop=None,bbox=None,image=None,math=False,marked='no'):
 rec={'id':f'D{len(D)+1:03}','location':location,'c':c,'h':h,'reading':reading,'scan_shows':evidence,'confidence':confidence,'kind':kind,'marked_in_h':marked,'change_c':change_c,'change_h':change_h,'crop':by_name[crop]['path'] if crop else None,'bbox':bbox or (by_name[crop]['bbox'] if crop else None),'bbox_image':image or whole,'math_consequential':math}
 D.append(rec)
 return rec['id']

diff('Opening continuation, cancelled primed capital',r"\deleted{$\unsure{G'|F'}$}",r'\struck{\ill{}}',r"\deleted{$\unsure{G'|F'}$}",'One crossed capital with an independent high prime; a rounded lower turn favours G, while crossing bars leave F possible.','medium',r'readable ink left as \ill{}',False,True,'02_first_cancellation',marked='yes')
diff('Opening continuation, G before de F',r'\deleted{\unsure{F|E}}G','G',r'\deleted{F}G','An earlier straight stem and two right bars remain inside the later G bowl; no independent third E bar.','high','omission',True,True,'03_overwritten_g')
diff('Complete upper-left slanted note',r"\margin{\unsure{double} \unsure{Transitivité} de l'induction}",r'\marginal{\ill{} \ill{} \ill{}}',r"\margin{\unsure{double} \unsure{Transitivité} de l'induction}",'Rotation includes the isolated low de and the high end of induction. The two first words remain compressed; de l’induction is legible.','medium',r'readable ink left as \ill{}',False,True,'01_margin',marked='yes')
diff('C7 heading, underline extent',r'$\uline{C}7_0$',r'\emph{C$7_0$}',r'$\uline{C}7_0$','The underline stops under C, before the separate 7 and low oval 0.','high','other',False,True,bbox=[285,330,450,445],image=a)
diff('C7 statement, final verb',r'\unsure{induise|induit}','induise','induise','After indui the low curved s and final short e are present; there is no terminal tall t.','high','misread word',True,False,'04_c7_ending')
diff('C7 statement, final primed capital',r"\unsure{C'|G'}",r"G'",r"\unsure{C'|G'}",'The final capital is open, with a low terminal bar and no secure inward G hook. A reduced G remains possible.','medium','misread symbol or index',False,True,'04_c7_ending',math=True)
diff('C7 statement, final stop',"$\\unsure{C'|G'}$.","$G'$.","$\\unsure{C'|G'}$\\unsure{.|,}",'A small detached low mark has a short hooked contour; period and comma remain possible.','medium','other',True,True,'04_c7_ending',bbox=[1625,535,1668,595])
diff('Parenthesis, noun after les',r'\unsure{rôle|rôles}','rôles','rôle','The tall l ends in one low horizontal e stroke; there is no separate final s group.','high','misread word',True,True,'05_role_and_orders')
diff('Parenthesis, worked foot of symétrique q before the straight order',r'\deleted{\unsure{l|F}}','',r'\text{Inline graphic role-mark in reading.tex}','The long descending q reaches a short upright, two rising strokes and a low tick. A separate cancelled complete l/F is not securely recoverable.','low','drawing or diagram',True,True,'05_role_and_orders',bbox=[1137,680,1184,803])
diff('Parenthesis, second order after et',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','Both right ends bow down; the second lower stroke is curved rather than a straight oblique bar.','high','misread symbol or index',True,False,'05_role_and_orders',bbox=[1378,739,1477,791],math=True)
diff('Parenthesis, worked sign between faux and colon',r'\unsure{\deleted{)}|?|\}|!}','',r'\text{Inline graphic faux-mark in reading.tex}','Several crossed upper curls continue into a lower bent hook, with a long rising arm. A clear colon stands separately to its right.','low','drawing or diagram',True,True,'06_faux_mark',bbox=[630,850,714,941])
diff('Parenthesis, adjective after F-prime order F',r'\unsure{donnés|données}','donnés','donnés','After the two flattened n strokes, one accented e-shaped curve precedes the final s; a second e is not visible.','high','misread word',True,False,'07_donnes')
diff('Parenthesis, abbreviated quantifier','tte','ttes','tte','Two t uprights share their cross stroke; a low e follows with no s.','high','misread word',False,True,'08_sous_figure',bbox=[960,941,1088,1005])
diff('Parenthesis, sous figure spelling and number',r'\unsure{sous figure|sous-figure}','sous-figures','sous figure','A blank separates sous from the tall f, and the noun ends with the low e stroke, without a separate s.','high','misread word',True,True,'08_sous_figure',bbox=[1165,931,1492,1015])
diff('Parenthesis, verb after F-prime',r'\unsure{soit|sont|est}','soient',r'\unsure{soit|sont}','The opening s and terminal t are clear. The compressed middle has no secure detached i dot; est is excluded by the opening form.','medium','misread word',True,True,'09_soit_induite',bbox=[394,1085,504,1135])
diff('Parenthesis, participle after soit/sont','induite','induites','induite','The word ends with the t and a short low e; there is no additional terminal s.','high','misread word',False,True,'09_soit_induite',bbox=[547,1070,798,1134])
diff('Parenthesis, final overwritten F',r'\deleted{\unsure{G}}F','F',r'\deleted{G}F','A rounded G bowl and inner return lie under the long straight F stem and its bars.','high','omission',True,True,'10_last_overprint')
diff('Strengthening paragraph, verb and following phrase',r'\unsure{renforcera|renforce} par la suite',r'renforcer \uncertain{un peu} \struck{\ill{}}','renforcera par la suite','The verb ends in a small a loop. Three following groups read par, la, suite; no separately struck word occupies H’s last placeholder.','high','misread word',True,True,'11_strengthening',marked='yes')
diff('Strengthening paragraph, small stroke immediately before C7',r'\deleted{\unsure{s}}','',r'\text{Inline graphic before-c7 in reading.tex}','A small detached curved stroke stands left of C. Its s-like form is visible, but there is no secure separate cancellation stroke.','low','drawing or diagram',True,True,'11_strengthening',bbox=[440,1272,472,1320])
diff('Lower draft, broad deletion state only; internal lettering and local deletions are collated separately',r'\deleted{b) $\unsure{\Longrightarrow|\longrightarrow}$ a) résulte de $C7_0$}',r'b) $\Rightarrow$ a) résulte de C$7_0$.',r'\text{Figure cancelled-draft: all its text is cancelled by the three drawn oblique strokes}','The draft from the heading and Soient through the proof lines is cancelled as a block; H’s main transcription leaves most of this material live, although its note acknowledges cancellation.','high','deletion state (struck given live or live given struck)',False,True,bbox=[280,1470,1655,2310],marked='yes')
diff('Lower draft, actual broad cancellation geometry only',r'% Three diagonal cancellation strokes cover the draft below.',r'\note{ce dernier alinéa, depuis « Soient $F$, $G$ », est traversé de deux longs traits obliques ; en marge droite un petit schéma : $F$ et $F\prime$ reliés par un signe de subdivision barré, $G \leq F$ au-dessous, et $G\prime$ sous $F\prime$ relié par des pointillés à $G$ ; le mot barré qui précède « Soient » est illisible (on devine « Corollaire »), et le mot souligné ajouté dessous est « considérons »}',r'\text{Figure cancelled-draft: left, middle and shorter right oblique strokes}','There are three separate diagonal strokes. The middle reaches the diagram and ends above its bottom dots; the right stroke stops beside the two conditions.','high','drawing or diagram',True,True,bbox=[430,1468,1615,2245],marked='yes')
# Use the exact editorial note rather than reconstructing its mathematical quoting.
D[-1]['h']=next(line for line in H.splitlines() if line.startswith('\\note{ce dernier alinéa'))
diff('Cancelled heading, lettering only',r'\unsure{Corollaire|Comparabilité} \unsure{1}',r'\struck{\ill{}}',r'\text{Figure cancelled-draft, title nodes: }\unsure{Corollaire|Comparabilité}\ \unsure{1}','A large C and intervening low/tall strokes survive under a dense zigzag. Corollaire is preferred, but the middle and final numeral are not secure.','low',r'readable ink left as \ill{}',False,True,'12_crossed_heading',marked='yes')
diff('Cancelled heading, underline extent only',r'\uline{\unsure{Corollaire|Comparabilité} \unsure{1}}','',r'\text{Figure cancelled-draft, independent underline from x=315 to about x=630 on the scan}','The straight underline ends before the far-right upright/numeral-sized group; it does not securely underline that final group.','high','other',True,True,'12_crossed_heading',bbox=[300,1588,730,1620])
diff('Draft introduction, overwritten G after F comma',r'\deleted{\unsure{A|F}}G','G',r'\deleted{A}G','An earlier triangular A with an interior horizontal survives inside the later G; it has no F-like upper bar.','high','omission',True,True,'13_draft_capital',bbox=[1188,1494,1259,1573])
diff('Raised Considérons les, placement only',r'\inserted{Considérons les}','Considérons les',r'\inserted{Considérons les}','The whole phrase, including les, is written on the raised line before Conditions.','high','insertion or placement',False,True,'14_insertion')
diff('Raised phrase, long insertion enclosure/leader only','','',r'\text{Figure cancelled-draft, graphic insertion-arm}','A line runs beneath both inserted words, curls up at the right, and curves down at the left before Conditions. No definite arrowhead is visible.','high','drawing or diagram',True,True,'14_insertion',bbox=[297,1588,704,1712])
diff('Draft introductory noun, capital C','Conditions','conditions','Conditions','The initial is a large open capital C.','high','misread word',False,True,'14_insertion',bbox=[308,1641,635,1708])
diff('Draft introductory cancelled adjective',r'\deleted{\unsure{équivalentes}}',r'\struck{équivalentes}',r'\deleted{équivalentes}','Despite the horizontal strike, initial é, descending q, tall l and final tes remain legible.','high','misread word',True,False,'14_insertion',bbox=[670,1620,1023,1738])
diff('Draft conclusion, word after Mais pas',r'\unsure{vrai|vice}','nécess.',r'\unsure{vrai|vice}','A short group of low curves and a final short upright favours vrai; the middle stays compressed. There is no readable nécess. group.','low','misread word',False,True,'15_conclusion',bbox=[1248,2070,1348,2120],math=True)
diff('Draft conclusion, possible comma before a',r'\unsure{,}','',r'\text{Figure cancelled-draft, first conclusion-tick}','The short southwest tick is joined to the long cancellation stroke. Its independent punctuation function cannot be established.','low','drawing or diagram',True,True,'15_conclusion',bbox=[1328,2086,1357,2121])
diff('Draft conclusion, small mark on closing parenthesis',r'\unsure{.}','',r'\text{Figure cancelled-draft, second conclusion-tick}','A tiny rightward protrusion touches the middle of the closing curve; there is no secure detached terminal dot.','medium','drawing or diagram',True,True,'15_conclusion',bbox=[1597,2050,1642,2134])
diagram_c=C[C.index('\\diagram{'):C.index('\\deleted{\\deleted{a)')].strip()
diagram_h=next(line for line in H.splitlines() if line.startswith('\\drawing{'))
diff('Complete small lower-right diagram, geometry and worked relation only',diagram_c,diagram_h,r'\text{Figure cancelled-draft, complete subdiagram cancelled-draft/diagram}','Four plain nodes retain their uneven heights. The top bowed relation has two extra rising branches; the left side is round U-shaped ink, the bottom has three dots, and the broken right edge ends in a worked downward head. The broad slash is continuous with the draft cancellation.','high','drawing or diagram',True,True,'16_diagram',bbox=[1305,2115,1515,2260])
diff('Last line, implication',r'\unsure{\Longrightarrow|\longrightarrow}',r'\Rightarrow',r'\Longrightarrow','Two distinct horizontal shafts reach the dark right head.','high','misread symbol or index',True,False,'17_final_arrow',bbox=[426,2254,523,2291],math=True)
diff('Last line, accent in résulte','résulte','résulte',r'\unsure{résulte|resulte}','Unlike the acute in the preceding occurrence, the last occurrence has no securely separable accent over its first e; the upper oblique may belong to the letter.','medium','misread word',True,True,'17_final_arrow',bbox=[627,2237,824,2305])
diff('Last line, terminal stop only',r'$C7_0$',r'C$7_0$.',r'$C7_0$','The low zero is followed by blank paper, with no point.','high','text not on the page',False,True,'17_final_arrow',bbox=[954,2235,1125,2325])

CD=[]
def doubt(location,c,reading,status,evidence,crop=None,bbox=None,image=None):
 CD.append({'location':location,'c':c,'reading':reading,'status':status,'scan_shows':evidence,'crop':by_name[crop]['path'] if crop else None,'bbox':bbox or (by_name[crop]['bbox'] if crop else None),'bbox_image':image or whole})
doubt('Opening cancelled primed capital',r"\unsure{G'|F'}",r"\unsure{G'|F'}",'retained','Prime clear; crossing bars obscure the capital.','02_first_cancellation')
doubt('Opening earlier capital under G',r'\unsure{F|E}','F','resolved','Straight stem and two bars under the G bowl.','03_overwritten_g')
doubt('Margin, first word',r'\unsure{double}',r'\unsure{double}','retained','Looped d and final tall joined strokes fit double; middle remains reduced.','01_margin')
doubt('Margin, second word',r'\unsure{Transitivité}',r'\unsure{Transitivité}','retained','Large T, low connected middle and high ending with a detached short accent are visible.','01_margin')
doubt('C7 ending, verb',r'\unsure{induise|induit}','induise','resolved','Low final s/e; no final t stem.','04_c7_ending')
doubt('C7 ending, capital',r"\unsure{C'|G'}",r"\unsure{C'|G'}",'retained','Open capital with very short final return.','04_c7_ending')
doubt('Parenthesis, rôle',r'\unsure{rôle|rôles}','rôle','resolved','No final s after the low e stroke.','05_role_and_orders')
doubt('Parenthesis, worked foot before ≤',r'\deleted{\unsure{l|F}}',r'\text{Graphic role-mark}','revised','An attached q descender and extra short strokes do not securely separate into a full deleted letter.','05_role_and_orders')
doubt('Parenthesis, bowed order',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','Curved lower stroke and curved right end.','05_role_and_orders')
doubt('Parenthesis, mark after faux',r'\unsure{\deleted{)}|?|\}|!}',r'\text{Graphic faux-mark}','revised','Full worked curl, lower hook and rising arm preserved without naming a punctuation sign.','06_faux_mark')
doubt('Parenthesis, donnés',r'\unsure{donnés|données}','donnés','resolved','One e-shaped curve after nn, before s.','07_donnes')
doubt('Parenthesis, sous figure',r'\unsure{sous figure|sous-figure}','sous figure','resolved','Blank before f; no separate hyphen.','08_sous_figure')
doubt('Parenthesis, soit',r'\unsure{soit|sont|est}',r'\unsure{soit|sont}','revised','Opening s and terminal t clear; i/n middle remains reduced.','09_soit_induite')
doubt('Parenthesis, earlier G under final F',r'\deleted{\unsure{G}}',r'\deleted{G}','resolved','G bowl and inner return remain below the later F bars.','10_last_overprint')
doubt('Strengthening paragraph, verb',r'\unsure{renforcera|renforce}','renforcera','resolved','Final small a loop after the r-like rise.','11_strengthening')
doubt('Strengthening paragraph, mark before C7',r'\deleted{\unsure{s}}',r'\text{Graphic before-c7}','revised','Detached curved stroke present; cancellation state uncertain.','11_strengthening')
doubt('Cancelled heading, word',r'\unsure{Corollaire|Comparabilité}',r'\unsure{Corollaire|Comparabilité}','retained','Middle obscured by dense zigzag.','12_crossed_heading')
doubt('Cancelled heading, final numeral',r'\unsure{1}',r'\unsure{1}','retained','Tall final group is worked and partly joined to the crossing stroke.','12_crossed_heading')
doubt('Draft earlier capital under G',r'\unsure{A|F}','A','resolved','Triangular earlier A with crossbar.','13_draft_capital')
doubt('Draft adjective',r'\unsure{équivalentes}','équivalentes','resolved','Visible é, q descender, l and terminal tes under the strike.','14_insertion')
doubt('Draft conclusion, middle word',r'\unsure{vrai|vice}',r'\unsure{vrai|vice}','retained','Low connected middle remains unresolved.','15_conclusion')
doubt('Draft conclusion, comma',r'\unsure{,}',r'\text{First conclusion-tick in cancelled-draft}','revised','Short tick joins diagonal; comma function unresolved.','15_conclusion')
doubt('Draft conclusion, final point',r'\unsure{.}',r'\text{Second conclusion-tick in cancelled-draft}','revised','Small protrusion touches closing curve; no securely separate point.','15_conclusion')
doubt('Diagram, worked top relation',r'\unsure{\preceq\mkern-5mu{}^{\prime}|\preceq|\leqslant}',r'\text{Doubt-marked five-stroke relation in cancelled-draft/diagram}','revised','Bowed sign plus two rising branches drawn; no isolated prime is supplied.','16_diagram')
doubt('Diagram, left sign',r'\unsure{\cup|U|\vee}',r'\text{Round U-shaped curve in cancelled-draft/diagram}','revised','Smooth rounded bottom excludes a pointed vee; literal curve avoids assigning cup versus letter U.','16_diagram')
doubt('Last line, arrow',r'\unsure{\Longrightarrow|\longrightarrow}',r'\Longrightarrow','resolved','Two separate shafts and one right head.','17_final_arrow')
# Explicit local notation checks and grouped repeated context rows.
doubt('C_context: upper continuation and C7, all plain F/G alphabets and prime positions',r"F, G, \unsure{C'|G'}",r"F, G, \unsure{C'|G'}",'retained','All ordinary F/G letters and high single primes checked on half a; only the final open C7 letter remains ambiguous. The two overwritten positions have their own dispositions above.',bbox=[280,65,1665,640],image=a)
doubt('C_context: C7 heading and later references',r'C7_0',r'C7_0','resolved','Low oval 0 occurs in the heading, strengthening reference and last line; the target en C7 has no low numeral. Underline is under C only.',bbox=[285,330,450,445],image=a)
doubt('C_context: flat and bowed orders in parenthesis and both cancelled displays',r'\leq, \unsure{\preceq|\leqslant}',r'\leq,\preceq','resolved','Half a and the local order crop distinguish straight and curved forms; half b shows the two chains G≤F′≼F and G≼G′≤F with one prime on each middle term.',bbox=[690,710,1095,1000],image=b)
doubt('C_context: final implications, top relation, U curve and dotted edges',r'\Rightarrow, \unsure{\Longrightarrow|\longrightarrow}; \preceq; \cup / U / \vee',r'\Rightarrow,\Longrightarrow;\ \text{cancelled-draft/diagram}','revised','The conclusion and first proof arrows are double; the final is also double. Complete diagram preserves all extra branches, U curve, three bottom dots and worked right endpoint.','16_diagram')
doubt('C_context: inclined upper-left note including de l’induction',r"double Transitivité de l'induction",r"\unsure{double} \unsure{Transitivité} de l'induction",'retained','Entire three-line slanted baseline is inside crop 01, including the isolated low de.','01_margin')
doubt('C_context: cancelled draft conclusion and small square, repeated punctuation checks',r'vrai; possible comma and final dot; U-curve; curved comparison with second rising tip',r'\unsure{vrai|vice};\ \text{conclusion-ticks and cancelled-draft/diagram}','revised','Word still uncertain. Small punctuation-like marks are drawn at their actual attachment points. Top relation is drawn rather than interpreted as a secure prime.','15_conclusion')
doubt('C_context: repeated rôle, induise and final C-prime/G-prime checks',r"les rôle; induise C'",r"les rôle; induise $\unsure{C'|G'}$",'revised','Independent crops resolve rôle and induise, while preserving the terminal alphabet doubt.','04_c7_ending')

I=[]
def inv(element,kind,position,words):
 I.append({'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('folio','text','top centre','72')
inv('opening continuation','text','top, two lines','sous-figure de … la subdivision')
inv('cancelled primed capital','deletion','opening line after de',r"\unsure{G'|F'}")
inv('old F beneath opening G','deletion','second opening line',r'\deleted{F}G')
inv('slanted note','margin note','upper left, rising toward top',r"\unsure{double} \unsure{Transitivité} de l'induction")
inv('C7 statement and underlined C','text','upper third',r'$\uline{C}7_0$ Pour toute figure')
inv('parenthetical paragraph','text','middle upper block',"(mais l'énoncé symétrique")
inv('worked q foot','drawing','before ≤ in parenthesis','role-mark')
inv('worked curled punctuation','drawing','between faux and colon','faux-mark')
inv('old G beneath final parenthetical F','deletion','right end of parenthesis',r'\deleted{G}F')
inv('strengthening paragraph','text','middle block','On … renforcera par la suite')
inv('peut','deletion','after On','peut')
inv('small curved mark before C7','drawing','second strengthening line','before-c7')
inv('entire cancelled lower draft','deletion','lower third, three long diagonals','cancelled-draft')
inv('lower heading and underline','text','left of Soient',r'\unsure{Corollaire|Comparabilité} \unsure{1}')
inv('heading local scribble','deletion','across lower heading','zigzag cancellation')
inv('draft introduction','text','lower heading level, to right','Soient F,G deux figures.')
inv('old A beneath draft G','deletion','draft introduction',r'\deleted{A}G')
inv('raised phrase','insertion','above Conditions','Considérons les')
inv('raised-phrase enclosure and leader','drawing','under raised phrase, curving to Conditions','insertion-arm')
inv('conditions introduction','text','below raised phrase','Conditions … :')
inv('adjective local strike','deletion','after Conditions','équivalentes')
inv('condition a','text','lower draft','a) G est une sous-figure')
inv('condition a display','display','centred below a',r'G\leq F\prime\preceq F')
inv('condition b','text','below first display',"b) G est une subdivision d'une sous-figure")
inv('condition b display','display','centred below b',r'G\preceq G\prime\leq F.')
inv('draft conclusion','text','below second display, slanted upward to right','On a alors b) ⇒ a) (Mais pas …)')
inv('tick merged with broad slash','drawing','conclusion before a ⇒ b','first conclusion-tick')
inv('tick attached to close parenthesis','drawing','right end of conclusion','second conclusion-tick')
inv('complete lower-right diagram','diagram','right of the proof lines',r'F,F\prime,G,G\prime; worked top order; rounded cup; three dots; broken downward edge')
inv('first proof line and local strike','deletion','lower left, penultimate line','a) ⇒ b) résulte de C6')
inv('last proof line','text','bottom left','b) ⇒ a) résulte/resulte de C7₀')

R=[]
def rem(location,reading,alternatives,confidence,reason):
 R.append({'location':location,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason})
rem('Opening cancelled capital',r"\deleted{$\unsure{G'|F'}$}",["G'","F'"],'medium','Crossed body does not separate the two candidate capitals.')
rem('Slanted note, first word',r'\unsure{double}',['double'],'medium','Compressed middle strokes.')
rem('Slanted note, second word',r'\unsure{Transitivité}',['Transitivité'],'medium','Several medial letters are reduced to connected strokes.')
rem('C7 final capital',r"\unsure{C'|G'}",["C'","G'"],'medium','No secure inner G return.')
rem('C7 terminal mark',r'\unsure{.|,}',['.',','],'medium','Small low mark has a hooked edge.')
rem('Before ≤ in parenthesis',r'\text{Doubt-marked graphic role-mark}',[r'\deleted{l}',r'\deleted{F}','worked foot of the preceding q only'],'low','The q descender touches the same small stroke group.')
rem('After faux',r'\text{Doubt-marked graphic faux-mark}',[r'\deleted{)}','?',r'\}','!','unidentified worked curved mark'],'low','Multiple crossing and rising strokes obscure the underlying character.')
rem('Parenthesis, verb before induite',r'\unsure{soit|sont}',['soit','sont'],'medium','The middle is compressed and no independent i dot is secure.')
rem('Before second C7',r'\text{Doubt-marked graphic before-c7}',['s',r'\deleted{s}','worked beginning of C'],'low','Small curved stroke is legible as a shape, but its identity and state are not established.')
rem('Cancelled heading, word',r'\unsure{Corollaire|Comparabilité}',['Corollaire','Comparabilité'],'low','Dense scribbled cancellation covers most of the middle.')
rem('Cancelled heading, numeral',r'\unsure{1}',['1','part of the worked final heading stroke'],'low','Final upright group is connected to crossing ink.')
rem('Conclusion after Mais pas',r'\unsure{vrai|vice}',['vrai','vice'],'low','Short connected humps do not establish the middle letters.')
rem('Conclusion before a ⇒ b',r'\text{Drawn first conclusion-tick}',['comma','small part of the cancellation stroke'],'low','Tick touches the long diagonal; it is preserved without an independent comma claim.')
rem('Conclusion closing curve',r'\text{Drawn second conclusion-tick}',['point attached to parenthesis','irregular continuation of the closing curve'],'medium','No detached full stop.')
rem('Diagram top relation',r'\text{Doubt-marked five-stroke relation in cancelled-draft/diagram}',[r'\preceq\mkern-5mu{}^{\prime}',r'\preceq with retraced/extra branches'],'low','The extra strokes join the upper branch instead of forming a securely detached prime.')
rem('Last résulte',r'\unsure{résulte|resulte}',['résulte','resulte'],'medium','The first e has no securely detached acute, unlike the preceding occurrence.')

notation=[
 {'sign':'Individual figures','latex':'F,G,F\prime,G\prime','appearance':'Plain F with two bars; G bowl with locally varying inward return; primes are separate high ticks.','location':'throughout; final C7 capital excepted','alternatives':[]},
 {'sign':'Final C7 primed capital','latex':r"\unsure{C'|G'}",'appearance':'Open round capital with low terminal bar.','location':'right end of C7 statement','alternatives':["C'","G'"]},
 {'sign':'Reference with low zero','latex':'C7_0','appearance':'Large baseline C7 and separate low oval zero.','location':'heading, strengthening reference, last line','alternatives':[]},
 {'sign':'Straight and bowed orders','latex':r'\leq,\preceq','appearance':'Straight lower bar versus down-curved lower stroke.','location':'parenthesis and two cancelled displays','alternatives':[]},
 {'sign':'Double implications','latex':r'\Rightarrow,\Longrightarrow','appearance':'Two shafts and a right head; final head heavily retraced.','location':'conclusion and proof lines','alternatives':[]},
 {'sign':'Worked comparison in diagram','latex':r'\text{cancelled-draft/diagram}','appearance':'Bowed comparison with one short oblique branch, one tall hooked branch and another rising branch.','location':'diagram top edge','alternatives':[r'\preceq with prime',r'\preceq retraced']},
 {'sign':'Rounded vertical relation','latex':r'\text{drawn U-shaped curve}','appearance':'Smooth U bottom and two upright arms.','location':'diagram left edge','alternatives':[r'\cup','U']},
 {'sign':'Literal small worked marks','latex':r'\text{role-mark; faux-mark; before-c7; conclusion-ticks}','appearance':'Exact visible small-stroke geometry retained, without assigning unsupported characters or stops.','location':'named graphics in reading.tex','alternatives':[]}
]
report={'reader':'R1','cote':'156-4','scan':'073','brief_version':'v09','started_utc':'2026-11-20T12:58:41Z','finished_utc':datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),'image_views':meta['images'],'reading_file':str(root/'reading.tex'),'differences':D,'c_doubts':CD,'inventory':I,'remaining_doubts':R,'notation':notation,'abbreviations':[{'form':'tte','expansion':'toute'},{'form':'ss-figure','expansion':'sous-figure'},{'form':'subd.','expansion':'subdivision'}],
 'notes':{'summary':'Folio 72 continues an induction discussion, states C7₀, gives a parenthetical nonconverse, and proposes a later canonical strengthening. The complete lower draft and its diagram are cancelled. All three supplied images and seventeen own crops were inspected individually. Every target is fully framed; no missing continuation was found.','math_reading_decisions':'No theorem was proved or independently checked. The contrast between the two order signs prompted close inspection, but decisions use their ink. The quantified earlier G′ does not settle the final C′/G′. No mathematical expectation changed a letter or implication direction.','author_checks':'Local changes visible on the sheet: earlier capitals under G/F, cancelled peut, a separately scribbled heading, inserted Considérons les with a drawn leader, cancelled équivalentes, three broad diagonal strokes and an additional strike through the C6 proof line. The small marks at rôle, faux and before C7 are preserved graphically without inventing complete deleted characters.','title_dates_pagination':'Handwritten folio 72; scan marker 73 retained. No date or additional cote marker. The lower title remains uncertain.','scope':'Only the assigned packet, brief, notation snapshot and R1 output were used. The supplied C_context cross-page audit tail, encountered during its initial full read, was disregarded as instructed by the parent. No other page or reader was accessed.','collation_conventions':'Difference rows separate lexical readings, placement, underlining, broad deletion state and drawing geometry. marked_in_h=yes identifies an unreadable/doubt marker or an explicit editorial uncertainty/deletion note, not ordinary emphasis. Equivalent preceq/preccurlyeq encodings are not counted. Named figure references identify the complete TikZ in reading.tex.'},
 'check_events':[], 'crops':crops,'workflow_feedback':[], 'missing_crop_continuations':[]}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
observations=[
('01_margin','Complete note rotated clockwise 55 degrees. Retained double and Transitivité doubts; de l’induction read. Entire oblique continuation is inside the source box.'),
('02_first_cancellation','Crossed primed capital retains G′/F′ alternatives; prime secure.'),
('03_overwritten_g','Earlier F has two bars and a straight stem under later G; E alternative rejected.'),
('04_c7_ending','induise resolved; final C′/G′ retained; low stop has period/comma alternatives.'),
('05_role_and_orders','rôle singular; bowed order resolved. The worked foot before ≤ is drawn without asserting an independent complete l/F.'),
('06_faux_mark','Crossed curled mark drawn with all branches; separate colon clear.'),
('07_donnes','donnés resolved from one e-shaped group before final s; comma clear.'),
('08_sous_figure','tte singular and sous figure without visible hyphen or plural ending.'),
('09_soit_induite','soit/sont retained, est rejected; induite singular clear.'),
('10_last_overprint','Earlier G under final F resolved; final parenthesis and point clear.'),
('11_strengthening','renforcera par la suite resolved; H un peu and deleted placeholder do not match separate physical groups. Small stroke before C7 drawn with state unresolved.'),
('12_crossed_heading','Title and numeral remain uncertain. Underline stops before the final upright group; zigzag reproduced.'),
('13_draft_capital','Earlier triangular A under draft G resolved.'),
('14_insertion','Complete raised Considérons les and its open enclosure/leader; capital Conditions; crossed équivalentes resolved.'),
('15_conclusion','vrai/vice retained. Possible comma merges with diagonal; tiny terminal mark touches closing curve. Both preserved as drawn ticks.'),
('16_diagram','All four nodes, uneven heights, five worked top strokes, smooth U curve, three bottom dots and worked downward endpoint preserved. Full lower endpoints are framed.'),
('17_final_arrow','Final double arrow resolved. Last résulte/resulte accent retained as a new local doubt; no terminal point after C7₀.')]
with (root/'inspection_log.md').open('a') as f:
 for n,(name,obs) in enumerate(observations,4):
  rec=by_name[name]
  f.write(f"\n{n}. `{rec['path']}`, emitted alone, successfully viewed in full. Source `{rec['source']}`, bbox {rec['bbox']}, rotation {rec['rotation']}°, scale {rec['scale']:.6f}; PIL LANCZOS, autocontrast, UnsharpMask (1.1, 120, 3), JPEG quality 94. {obs}\n")
 f.write('\nNo truncated image displays occurred. No full image or half was viewed twice; no decided locus was recropped. Every crop target includes its endpoints and space beyond them; incidental neighbouring text may be clipped but no target continuation is missing.\n')
 f.write('\nThe C_context cross-page tail read initially was disregarded following the parent’s clarification; no evidence from its other-page comparisons was used.\n')
 f.write('\nFinished complete page and collation. Validation is restricted to fragment/report structure, witness snippet scope and crop existence. No LaTeX compiler, OCR or mathematical proof check was run.\n')
print(json.dumps({'differences':len(D),'c_doubts_and_context_dispositions':len(CD),'inventory':len(I),'remaining_doubts':len(R),'crops':len(crops)},ensure_ascii=False))
