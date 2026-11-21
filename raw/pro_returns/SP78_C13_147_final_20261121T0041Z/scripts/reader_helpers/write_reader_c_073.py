from pathlib import Path
from datetime import datetime, timezone
import json

ROOT=Path("/workspace/scratch/ea90d891106a")
WORK=ROOT/"SP78_C13_147_work"
OUT=WORK/"reader_returns/147_scan073"
OUT.mkdir(parents=True,exist_ok=True)
boxes={int(k):v for k,v in json.loads((ROOT/"runtime/reader_c_073_crops.json").read_text()).items()}
accent=r"\overset{\unsure{\deleted{\wedge}|\sim}}{M}"
insert_m=r"\unsure{\widehat M_{g,I}|M_{g,I}}"
upper_dim=r"\unsure{3g-1)+\nu=2|3(g-1)+\nu=2}"
lower_dim=r"N=\unsure{2|3}\unsure{(}g-1)+\nu\geq2"

lines=[
    r"et utilisant le fait que les $\widehat M^{!}_{g_\alpha,\widehat\nu_\alpha}$ sont",
    "connexes, on voit que $"+accent+r"_G^\infty=\widehat M_G\setminus M_G$",
    r"est connexe dès que \deleted{deux} parmi les",
    r"facteurs $\widehat M^{!}_{g_\alpha,\widehat\nu_\alpha}$, il y en a au moins",
    r"deux qui sont de dim $\geq1$ (en utilisant",
    r"le fait que pour un tel $\alpha$, on a",
    r"$M^\infty_{g_\alpha,\widehat\nu_\alpha}\ne\phi$). Donc il suffit de regarder",
    r"le cas où $\widehat M_G\simeq\widehat M^{!}_{g,\nu}\inserted{\simeq "+insert_m+r"}$, avec",
    r"\inserted{le cas où $"+upper_dim+r"$ est déjà vu, donc DPS $N\geq3$.}",
    r"\inserted{$(\dim M_{g,\nu}=)$} $"+lower_dim+r"$.",
    r"\deleted{Dans ce cas}, Il suffit de",
    r"voir que deux diviseurs à l'infini peuvent",
    r"être joints par une chaine de tels div.",
    r"dont deux consécutifs ont une intersection",
    r"non vide, compte tenu que ces diviseurs",
    r"sont eux aussi connexes. Or les diviseurs",
    r"à l'infini correspondent aux \deleted{types} \inserted{MD-}graphes",
    r"suivants",
]

figure=r"""\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm]
\node at (47,207) {$(90)$};
\draw (190,43)..controls(175,67)and(217,150)..(175,165)..controls(155,171)and(173,176)..(181,183)..controls(206,209)and(203,273)..(218,386);
\node at (253,70) {a)};
\fill(409,89)circle(1.5pt);
\draw(409,89)..controls(472,53)and(544,45)..(564,88)..controls(596,148)and(461,112)..(409,89);
\node at (391,30) {$I$};
\node at (411,142) {$g-1$};
\node at (826,57) {$(\text{si }g\geq1)$};
\node at (275,259) {b)};
\node at (560,250) {\deleted{$\unsure{g'}$}};
\draw (460,283)--(545,207);
\draw (499,237)..controls(515,228)and(532,217)..(542,215)..controls(552,212)and(540,230)..(525,240)..controls(541,234)and(554,224)..(562,225)..controls(575,225)and(540,257)..(528,269)..controls(548,253)and(579,229)..(594,226)..controls(615,225)and(552,273)..(523,295)..controls(548,280)and(596,252)..(620,244)..controls(636,244)and(590,274)..(580,284)..controls(596,284)and(625,268)..(640,268)..controls(650,267)and(640,274)..(636,280);
\draw (456,318)--(599,207);
\draw (486,219)--(677,289);
\fill(690,236)circle(1.5pt);
\draw(700,235)--(823,235);
\fill(823,235)circle(1.5pt);
\node at (692,171) {$I'$};
\node at (821,170) {$I''$};
\node at (705,278) {$g'$};
\node at (826,275) {$g''$};
\draw(971,204)..controls(980,235)and(978,296)..(957,310)..controls(949,316)and(944,318)..(937,319)..controls(957,325)and(962,341)..(966,365)..controls(974,398)and(974,441)..(982,465);
\node[anchor=base west] at (1007,218) {$I=I'\amalg I''$};
\node[anchor=base west] at (1018,289) {$g'+g''=0$};
\node[anchor=base west,font=\scriptsize] at (1041,339) {$\inserted{\text{si }g'\text{ (resp }g'')=0,\text{ alors}}$};
\node[anchor=base west,font=\small] at (1021,377) {$\deleted{2g'+\operatorname{card}I'\geq\unsure{2}}$};
\node[anchor=base west,font=\small] at (1021,432) {$\deleted{2g''+\operatorname{card}I''\geq2}$};
\node[anchor=base west,font=\scriptsize] at (1049,472) {$\inserted{\operatorname{card}I'\geq2\text{ (resp }\operatorname{card}I''\geq2\text{)}}$};
\end{tikzpicture}}"""
proposed="\\scanpage{73}\n"+"\n".join(lines)+"\n"+figure+"\n\\margin{72}\n"
(OUT/"proposed.tex").write_text(proposed)

changes=[]
def change(place,c,h,final,evidence,crop,ac=False,ah=True,kind="misread word",err="words",conf="high",marked=False,cons=False):
    changes.append({"id":f"073-{len(changes)+1:02d}","place":place,"C":c,"H":h,"final":final,
                    "evidence":evidence,"crop":f"147_scan073_place{crop:02d}.png","box":boxes[crop],
                    "confidence":conf,"against_C":ac,"against_H":ah,"kind":kind,"marked_in_H":marked,
                    "error_sheet_kind":err,"consequential":cons})
change("opening verb","utilisant","utilisons","utilisant",
       "The end has a low a/n run and a final rising crossed t-like stroke; it lacks the rounded o and terminal s required by utilisons.",1)
change("after sont connexes","on voit que","ainsi que","on voit que",
       "Two separate groups appear before que: the short low on and then voit with a tall terminal t. They cannot be read as the single word ainsi.",2)
change("first M_G at infinity, accent state",r"\widehat M_G^\infty",r"\widetilde M_G^\infty",accent+r"_G^\infty",
       "The accent has a small angular peak, a looped/retraced left part, and a long horizontal continuation across its lower level. A canceled/overworked hat is preferred, with a live tilde retained as alternative; it is unlike the clean hat on the next M.",2,
       ac=True,kind="deletion state",err="symbols and indices",conf="low",cons=True)
change("before the repeated factor formula","facteurs","","facteurs",
       "The line begins with a tall descending f, followed by the joined a-c-t-e-u-r-s run before the M formula.",3,kind="omission",err="omissions")
change("parenthetical explanation, verbal phrase","en utilisant","on utilise","en utilisant",
       "The first word begins with a low e-shaped loop, not a closed o. The second has the extended a-n-t ending, matching utilisant in the first line.",4)
change("after pour un tel alpha","on a",r"\ill{}","on a",
       "After alpha and a comma, a short low on is followed by a small closed a-like dot/loop. The same reduced a occurs in il y en a above.",4,
       kind=r"readable ink left as \ill{}",err="readable ink left as illegible",marked=True)
change("whole nonempty-boundary formula, empty-set glyph",r"M^\infty_{g_\alpha,\widehat\nu_\alpha}\ne\varnothing",
       r"M^\infty_{g_\alpha,\widehat\nu_\alpha}\ne\emptyset",r"M^\infty_{g_\alpha,\widehat\nu_\alpha}\ne\phi",
       "The sign has a small high loop and a long slanted stem extending far below it, matching the locally established phi-shaped empty-set notation. The M is bare with infinity, and the nu has its own angular hat.",5,
       ac=True,kind="misread symbol or index",err="symbols and indices")
change("start of the reduction sentence","Donc il suffit de regarder","Dans","Donc il suffit de regarder",
       "The capital D is followed by the short on/c sequence; distinct il, suffit with tall f strokes, de, and regarder occupy the rest of the line.",5)
change("next line, case condition","le cas où",r"le cas \uncertain{contraire}, on a","le cas où",
       "After le cas is one reduced où group with a detached accent. No space contains contraire or on a before the displayed M formula.",6,marked=True)
change("inserted isomorphism, M accent",r"\inserted{\simeq M_{g,I}}",r"(\simeq M_{g,I}\ldots)",
       r"\inserted{\simeq "+insert_m+r"}",
       "Two sloping arms form a wedge immediately above the inserted M, but the f-descender of suffit passes through their vertex. A hat is preferred with bare M retained as the alternative; the stroke attribution is not secure.",6,
       ac=True,kind="misread symbol or index",err="symbols and indices",conf="medium",cons=True)
change("inserted isomorphism, supplied delimiters and ellipsis",r"\inserted{\simeq M_{g,I}}",
       r"(\simeq M_{g,I}\ldots)",r"\inserted{\simeq "+insert_m+r"}",
       "The upper addition consists of the isomorphism sign, M and its g,I index, with a curved insertion connector underneath. There are no enclosing parentheses or ellipsis dots around it.",6,
       kind="text not on the page",err="text not on page")
change("word after the M chain","avec","","avec",
       "To the right of the baseline comma and below the insertion are the low joined strokes of avec. They are distinct from the connector.",6,
       kind="omission",err="omissions")
change("upper dimension note, opening parenthesis",r"3(g-1)+\nu=2",r"3(g-1)+\nu=2",upper_dim,
       "After 3, the next curved head joins directly to g's descender; no separate opening parenthesis can be isolated. The closing parenthesis after 1 is distinct. The literal missing-opening form is preferred, with the supplied-parenthesis form shown only as an uncertain alternative.",7,
       ac=True,kind="misread symbol or index",err="symbols and indices",conf="medium",cons=True)
change("upper note, word before DPS","donc",r"\struck{\ill{}} dans","donc",
       "One live word lies after vu and its comma: a looped d followed by the low onc run. It has no independent cancellation crossing it, and there is no additional canceled group before it.",7,
       marked=True)
change("dimension label and N formula, parenthetical extent",
       r"\inserted{$(\dim M_{g,\nu}=)$} $N=\unsure{2|3}(g-1)+\nu\geq2$.",
       r"\marginal{$(\dim M_{g,\nu}=N=3(g-1)+\nu\geq2.)$}",
       r"\inserted{$(\dim M_{g,\nu}=)$} $"+lower_dim+r"$.",
       "The upper dim label has its own closing parenthesis immediately after the equals sign. A curved insertion connector reaches toward the N line below. The lower N expression is outside those parentheses and ends with a separate period.",8,
       kind="insertion or placement",err="insertions put in wrong place",cons=True)
change("lower N expression, coefficient and opening curve",
       r"N=\unsure{2|3}(g-1)+\nu\geq2",r"N=3(g-1)+\nu\geq2",lower_dim,
       "The coefficient is a thick crossed/overwritten group with a lower returning stroke, still compatible with 2 or 3. Its meeting with the following g also prevents a secure separation of an opening parenthesis. The -1), plus nu, inequality and terminal 2 remain readable.",8,
       kind="misread symbol or index",err="symbols and indices",conf="low",cons=True)
change("canceled Dans ce cas, following comma",r"\deleted{Dans ce cas,}",r"\struck{Dans ce cas},",
       r"\deleted{Dans ce cas},",
       "The long strike runs through the three words and stops before a detached curved comma situated lower and to their right. That comma is live.",7,
       ac=True,ah=False,kind="deletion state",err="struck text")
change("after canceled Dans ce cas","Il suffit","il suffit","Il suffit",
       "The initial I is large and has distinct upper and lower horizontal bars; it is followed by the separate tall l. It is not a dotted lowercase i.",7)
change("chain of divisors","chaine",r"\uncertain{chaîne}","chaine",
       "The i carries a small dot. No circumflex is present over it; the h ascender and the following n/e strokes are separate.",9,
       kind="abbreviation expanded or spelling modernised",err="abbreviations expanded spelling modernised",marked=True)
change("connectedness of the divisors","eux aussi","eux-mêmes","eux aussi",
       "After eux the word has the low a/u run, two s-like connections and a final dotted i. There is no m-m structure or circumflex.",10)
change("canceled word before graphes",r"\deleted{types}",r"\struck{1-types}",r"\deleted{types}",
       "The tall initial t joins directly to the descending y and p. The horizontal line is the cancellation through the word; no independent numeral 1 plus hyphen precedes it.",11,
       kind="misread word",err="struck text")
change("(90)b, canceled patch",
       r"\deleted{$\unsure{g'}$} with four straight crossing lines",
       "[canceled drawing mentioned in an editorial note but not reproduced]",
       "the visible zigzag returns, long rising diagonal and long descending cross-stroke, with g' retained only as a doubtful buried suggestion",
       "The patch contains several connected rising returns rather than only four isolated lines. Two long diagonals cross that band. No separate g body or prime can be isolated securely; the existing g' suggestion remains explicitly doubtful beneath the reproduced cancellation.",13,
       ac=True,kind="drawing or diagram",err="drawings and diagrams",conf="low")
change("(90)b, left endpoint of live segment","segment joined to both points","segment joined to both points",
       r"\fill(690,236)circle(1.5pt);\draw(700,235)--(823,235);\fill(823,235)circle(1.5pt);",
       "A narrow white gap separates the left filled point from the beginning of the horizontal line. The line joins the right point. The gap is preserved geometrically without inferring disconnection of the graph.",13,
       ac=True,kind="drawing or diagram",err="drawings and diagrams",cons=False)
change("(90)b, position of the first replacement condition",
       "si g' ... then after both canceled inequalities",
       "si g' ... then above the two canceled inequalities",
       r"\inserted{\text{si }g'\text{ (resp }g'')=0,\text{ alors}} above the first canceled inequality",
       "The small live si...alors line lies between g'+g''=0 and the first crossed inequality. Its g'' descender reaches into the lower canceled line; the condition is not below both deletions.",14,
       ac=True,ah=False,kind="insertion or placement",err="insertions put in wrong place")
change("(90)b, first parenthetical abbreviation","resp","ou","resp",
       "The compact group has an initial r/e run and a descending p. It is not the two low letters ou. No detached abbreviation dot is visible.",14,
       kind="misread word",err="words")
change("(90)b, last parenthetical abbreviation","resp","ou","resp",
       "The bottom group repeats the low joined beginning and long p descender of resp on the upper inserted line; it does not read ou.",14)
change("lower-left pencil foliation",r"\margin{72}","",r"\margin{72}",
       "The light pencil digits are a crossed 7 followed by a curved 2 with a long lower return. There is no separate ink author number at the head of this continuation page.",15,
       kind="omission",err="omissions")

doubts=[
    {"place":"first M_G at infinity","reading":accent+r"_G^\infty","alternatives":r"\widetilde M_G^\infty; an overworked live hat is also not fully excluded","confidence":"low","reason":"The angular peak, looped left end and crossing horizontal continuation do not decide the accent's live/canceled state."},
    {"place":"inserted M_{g,I}","reading":insert_m,"alternatives":r"M_{g,I}","confidence":"medium","reason":"A wedge is visible, but its vertex coincides with the descending f of suffit; the two source strokes cannot be assigned independently with certainty."},
    {"place":"upper dimension insertion","reading":upper_dim,"alternatives":r"3(g-1)+\nu=2","confidence":"medium","reason":"Only the closing parenthesis is separately visible. The next curve after 3 is g's own head, so an opening parenthesis is not silently supplied."},
    {"place":"M1064, lower coefficient","reading":r"\unsure{2|3}","alternatives":"3","confidence":"low","reason":"The coefficient is thickened and crossed where the following g begins; neither the upper lobes nor the lower return separates 2 from 3 securely."},
    {"place":"lower N formula, opening parenthesis","reading":r"\unsure{(}","alternatives":"no opening parenthesis","confidence":"low","reason":"The coefficient and following g overlap too much to isolate a separate opening curve. The closing parenthesis after 1 is plain."},
    {"place":"(90)b, canceled patch","reading":r"\deleted{$\unsure{g'}$} beneath reproduced crossing paths","alternatives":"unrecoverable prior drawing or another mathematical label","confidence":"low","reason":"No independent g body or prime can be extracted from the multiple zigzag returns and crossing diagonals; g' remains only a tentative witness suggestion."},
    {"place":"first canceled inequality, final number","reading":r"\deleted{2g'+\operatorname{card}I'\geq\unsure{2}}","alternatives":"unrecoverable overworked final digit","confidence":"medium","reason":"The live inserted g'' descender crosses the final digit as well as the strike. Its lower foot and possible upper curve favor 2, but its full outline is not exposed."},
]

notes=[
    "The manuscript continues an argument using connectedness of the factors hat M^!_{g_alpha,hat nu_alpha}. It claims the boundary of hat M_G is connected whenever at least two factors have dimension at least 1, using nonemptiness of the relevant factor boundaries. The first boundary symbol's accent is overworked and is retained as a canceled-hat/live-tilde alternative. Connectedness and nonemptiness of the particular moduli factors were not established in this reading.",
    "Conditional topological check performed here: let X be a finite product of nonempty connected X_i, with U the product of U_i, and suppose two distinct complements D_i=X_i minus U_i and D_j=X_j minus U_j are nonempty. Choose a_i in D_i and a_j in D_j. The coordinate slices x_i=a_i and x_j=a_j are connected and meet, hence form a connected core in X minus U. Every boundary point lies in a connected slice x_k=d for some d in D_k; that slice meets the first core slice when k differs from i, or the second when k=i. Thus the union of all boundary slices is connected. This proves the elementary product-boundary implication under those hypotheses, without proving that the manuscript's moduli spaces satisfy them or are identified with the required product.",
    "The manuscript reduces to a single M factor and inserts an additional isomorphism to a possibly hatted M_{g,I}. It says the dimension-2 case was already treated and then writes DPS N>=3. The upper expression visibly has a closing parenthesis after 1 but no separable opening one; the literal 3g-1)+nu=2 is preferred with the conventional parenthesized version only an uncertain alternative. The lower N coefficient and opening parenthesis remain doubtful. No dimension formula or prior-case coverage was proved here.",
    "The manuscript says it suffices to join any two infinity divisors by a chain in which successive divisors meet, since those divisors are connected. The sufficiency of that topological criterion was checked conditionally: the union along any such finite chain is connected by induction, and the chain-connected family of connected divisors has a connected total union. This does not prove the needed chains exist or that the individual divisors in this moduli problem are connected.",
    "The manuscript presents the two graph forms (90): a loop on one vertex of weight g-1, for g>=1; and an edge between two vertices with labels I',g' and I'',g''. The right-hand conditions retain the literal equality g'+g''=0. The two displayed stability inequalities are canceled and replaced by the condition about card I' and card I'' when the respective genus is zero. The geometric classification and the stability conditions were carried as source claims without proof.",
    "Graph arithmetic was checked only at the level of the usual weighted-graph genus sum of vertex weights plus first Betti number. The connected loop graph has one edge and one vertex, so its cycle rank is 1 and its total weighted genus is (g-1)+1=g. The connected two-vertex, one-edge graph has cycle rank 0, so its weighted genus is g'+g''. If it represents a generic genus-g case, this suggests the expected relation g'+g''=g. The source instead writes a complete closed oval 0 with no descender, which is retained; the check flags the discrepancy and does not supply g or prove an authorial intention. The small visible gap beside the drawn left vertex is not used as a topological conclusion.",
    "Reading count: 29 physical reading bands: 16 main prose baselines; 4 separate addition bands (the isomorphism, dimension-case insertion, marginal dim label, and MD-); 8 diagram bands (two graph bands and six right-hand condition lines); and the pencil foliation. No separate ink author page number appears. The complete scan and both native halves were read once. Fifteen unique crops were saved and all were viewed. No OCR, internet research or TeX compilation was used.",
    "The lower-left 72 is pencil foliation in an unattributed hand and remains margin text. The accents, canceled mathematical group, and overworked coefficient/digit remain explicit doubts. The source spelling chaine, short forms dim, div., card, resp and DPS are retained. The meaning of DPS is not expanded from context. The two tiny spots beside the graph-a I label were not interpreted as extra labels or graph vertices.",
]
date=datetime.now(timezone.utc).isoformat()
event_data=[
    (1,"carried as background without fault found","Read the factor-connectivity and nonempty-boundary claims, including the full formulas. Did not prove the moduli hypotheses."),
    (2,"targeted proof check","Proved the finite-product boundary lemma stated in N2 by a connected core of two coordinate slices, with every other boundary slice meeting that core. Assumed nonempty connected factors, a product open part and two nonempty complements; did not establish those hypotheses for the manuscript's objects."),
    (3,"carried as background without fault found","Read the isomorphism chain and both dimension expressions. Did not prove their moduli interpretation or verify the claim that the dimension-2 case had already been covered. No ambiguous glyph was decided from a dimension formula."),
    (4,"targeted proof check","Verified the sufficient connected-union criterion by induction along a finite chain of intersecting connected sets, then union over chains. Did not construct the manuscript's divisor chains or prove divisor connectedness."),
    (5,"carried as background without fault found","Read both graph forms, label primes, cancellation extent and replacement stability conditions. Did not prove the claimed boundary-divisor classification or stability inequalities."),
    (6,"used and rechecked in this run","Computed cycle ranks E-V+1 as 1 for the one-vertex loop and 0 for the two-vertex edge; added the displayed vertex weights. This gives the conditional genus expectation described in N6, not a replacement for the clearly written 0."),
]
events=[{"statement_id":f"147-073-N{n}","date":date,"who":"reader_c, GPT-6 Astra Pro (effort setting not exposed)","type":typ,"outcome":outcome} for n,typ,outcome in event_data]

inventory=[]
def inv(kind,pos,first,hand="his hand"):
    inventory.append({"scan":73,"sheet_kind":"text","hand":hand,"element":f"{len(inventory)+1:02d}","kind":kind,"position":pos,"first_words_or_objects":first,"transcribed":"yes"})
inv("text","opening eight main baselines","et utilisant ... le cas où ... avec")
inv("deletion","third main baseline","deux")
inv("insertion","above the M-chain comma","isomorphism to doubtful hat/bare M_{g,I}")
inv("insertion","between M chain and next main line","le cas où ... déjà vu, donc DPS N>=3")
inv("insertion","left margin above N","(dim M_{g,nu}=)")
inv("text","next main baseline, left","full N formula, overworked coefficient")
inv("deletion","same main baseline, right","Dans ce cas; following comma live")
inv("text","divisor-chain argument","Il suffit de voir ... sont eux aussi connexes")
inv("text","last prose lines","Or les diviseurs ... graphes suivants")
inv("deletion","before graphes","types")
inv("insertion","above canceled types","MD-")
inv("drawing","lower part, whole (90)","two graph cases and right-hand condition brace")
inv("drawing","(90)a","pointed loop, I, g-1 and g>=1")
inv("drawing","(90)b","two points and nearly joining line, I'/I'', g'/g''")
inv("deletion","left of the live (90)b segment","crossed zigzag patch, doubtful underlying g'")
inv("display","right of (90)b","I=I' amalg I''; g'+g''=0")
inv("insertion","above first canceled inequality","si g' (resp g'')=0, alors")
inv("deletion","first crossed inequality","2g'+card I'>=doubtful2")
inv("deletion","second crossed inequality","2g''+card I''>=2")
inv("insertion","bottom of condition block","card I'>=2 (resp card I''>=2)")
inv("margin note","lower-left corner","72","unattributed pencil hand")

second=[]
def sb(kind,box,reading):
    second.append({"box":f"B{len(second)+1:02d}","kind":kind,"x0":box[0],"y0":box[1],"x1":box[2],"y1":box[3],"reading":reading})
sb("word disagreement",boxes[1],lines[0])
sb("doubtful formula",boxes[2],lines[1])
sb("struck passage",boxes[3],"\n".join(lines[2:4]))
sb("word disagreement",boxes[4],"\n".join(lines[4:6]))
sb("doubtful formula",boxes[5],lines[6])
sb("insertion",boxes[6],lines[7])
sb("doubtful formula",[577,857,1681,953],lines[8])
sb("insertion",boxes[8],lines[9])
sb("struck passage",[687,930,1495,1021],lines[10])
sb("word disagreement",boxes[9],"\n".join(lines[11:13]))
sb("word disagreement",boxes[10],"\n".join(lines[13:16]))
sb("struck passage",boxes[11],"\n".join(lines[16:18]))
sb("doubtful formula",[179,1808,1692,2314],figure)
sb("handwritten number",boxes[15],r"\margin{72}")

report={
    "scan":73,"reader":"reader_c","physical_lines_read":29,"changes":changes,
    "decisions":[
        {"id":"M1063","cote":147,"scan":73,"decision":"first","reading":"DPS","ink":"The first capital has a distinct left stroke with a single right bowl, unlike a plain oval O. P has its upright and upper bowl; S has the angular returning form. The whole dimension note and N>=3 were read.","crop":"147_scan073_place07.png (577,857,1681,1012)","confidence":"high"},
        {"id":"M1064","cote":147,"scan":73,"decision":"undecided","reading":r"\unsure{2|3}","ink":"The entire N expression was inspected. The coefficient is thick and overworked where it meets the opening-curve/g cluster; it does not expose enough of either a 2 or a 3 to decide. The expected dimension formula was not used to supply 3.","crop":"147_scan073_place08.png (99,922,644,1059)","confidence":"low"},
        {"id":"M1065","cote":147,"scan":73,"decision":"first","reading":"0","ink":"The right-hand result in g'+g''=0 is a complete closed oval with no descending stroke. The neighboring g' and g'' have long descenders, providing direct local comparison. The whole right-hand condition block was read.","crop":"147_scan073_place14.png (1121,1965,1692,2314)","confidence":"high"},
    ],
    "inventory":inventory,"doubts":doubts,"notes":notes,"check_events":events,
    "notation":[
        {"sign":"high loop with a long descending stem for the empty set","reading":r"\phi","evidence":"The complete parenthetical boundary formula has the same long-stem, small-high-loop construction recorded locally, not a centered circular set-minus sign.","scope":"147 scan073, nonempty-boundary formula"},
        {"sign":"overworked accent above first boundary M","reading":accent,"evidence":"Angular peak with looped/retraced left end and crossing horizontal continuation; normal hats on adjacent M letters differ.","scope":"147 scan073, first M_G^infinity only"},
        {"sign":"DPS","reading":"DPS","evidence":"Distinct straight left part and right bowl on D, followed by P and S; preserved as a source abbreviation without an inferred expansion.","scope":"147 scan073, dimension-case insertion"},
        {"sign":"closed oval in g'+g''=0","reading":"0","evidence":"No descender; contrast with both adjacent g labels. Generic genus arithmetic does not replace the oval.","scope":"147 scan073, (90)b"},
    ],
    "hand_log":[
        {"habit":"A long descender from an upper prose line can meet a mathematical accent on an insertion.","pages":[73],"all_occurrences":"The f of suffit crosses the wedge-like mark above inserted M_{g,I}; this occurrence remains a hat/no-hat doubt rather than a global rule.","witness_misreadings":"Both witnesses omit the possible hat."},
        {"habit":"A small final a may reduce to a filled loop/dot.","pages":[73],"all_occurrences":"on a and il y en a; the tiny a) case label is similarly reduced.","witness_misreadings":"H leaves on a illegible."},
        {"habit":"Tall t joined to y and p in a struck word can resemble a separate 1-hyphen.","pages":[73],"all_occurrences":"The canceled types before MD-graphes; no independent numeral/hyphen is present.","witness_misreadings":"H gives 1-types."},
        {"habit":"Resp has a long p descender despite its compressed preceding letters.","pages":[73],"all_occurrences":"Both replacements in the right-hand (90)b block, no separate final dot.","witness_misreadings":"H gives ou twice."},
        {"habit":"A compact zero can be a fully closed oval or a filled dot at a smaller scale.","pages":[73],"all_occurrences":"The large equation result g'+g''=0 is an open-centered oval; the smaller inserted equality to zero is dark and compact.","witness_misreadings":"C retains a 0/g doubt on the clearly oval equation result."},
    ],
    "abbreviations":[{"written":"dim","expansion":"dimension"},{"written":"div.","expansion":"diviseurs"},{"written":"card","expansion":"cardinal"},{"written":"resp","expansion":"respectivement"},{"written":"DPS","expansion":"not established on this leaf; not expanded"}],
    "second_boxes":second,
    "unresolved":[
        "First boundary-M accent: canceled/overworked hat versus live tilde.",
        "Inserted M_{g,I}: wedge coincides with an upper f-descender; hat versus bare M remains doubtful.",
        "Upper dimension formula lacks a separable opening parenthesis; both literal and supplied-parenthesis readings are shown.",
        "M1064 coefficient 2/3 and lower opening parenthesis remain unresolved.",
        "Underlying g' in the canceled diagram patch is only a tentative suggestion.",
        "Final digit of the first canceled inequality is overlapped by a live inserted descender and remains doubtful.",
        "The literal g'+g''=0 is retained despite the generic weighted-genus expectation.",
    ],
    "witness_comparison":"C is substantially closer to the prose, short forms, inserted-note wording and replacement conditions. H preserves the possibility of a different first-M accent and places the first replacement condition above the canceled inequalities, but neither witness captures the accent/deletion uncertainty or the possible inserted hat. Both supply an opening parenthesis in the upper dimension note that is not separately visible. C's canceled-patch rendering and connected left endpoint are too schematic; H omits that patch and changes resp to ou. The literal zero, not a mathematically expected g, is supported decisively by the ink."
}
assert [d["id"] for d in report["decisions"]]==["M1063","M1064","M1065"]
for row in changes:
    assert row["against_C"] or row["against_H"]
    assert (WORK/"crops"/row["crop"]).is_file()
for b in second:
    assert b["reading"] in proposed,b["box"]
for e in events:
    assert 1<=int(e["statement_id"].split("-N")[-1])<=len(notes)
assert all((WORK/"crops"/f"147_scan073_place{i:02d}.png").is_file() for i in range(1,16))
(OUT/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"scan":73,"physical_bands":29,"crops":15,"changes":len(changes),"decisions":3,"inventory":len(inventory),"doubts":len(doubts),"second_boxes":len(second),"check_events":len(events),"out":str(OUT)},ensure_ascii=False))
