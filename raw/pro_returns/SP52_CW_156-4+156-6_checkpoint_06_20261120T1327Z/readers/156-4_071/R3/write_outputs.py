from pathlib import Path
import json
from datetime import datetime, timezone
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_071/R3')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_071')
meta=json.loads((packet/'metadata.json').read_text())
whole,half_a,half_b=meta['images']
crops=json.loads((out/'crop_metadata.json').read_text())
cp={Path(c['path']).stem:c for c in crops}
L1=r'''% Figure L1: the two broken vertical groups in the left margin; no linguistic function assigned.
\margin{\figure{\begin{tikzpicture}[x=0.009cm,y=0.009cm,line cap=round]
\fill (0,0) ellipse (1.7 and 2.6);
\draw[line width=0.9pt] (-0.5,-5) -- (0.6,-10) -- (-0.5,-15);
\draw[line width=0.9pt] (0,-20) -- (1,-25) -- (-0.7,-31);
\fill (8,-35) ellipse (1.4 and 1.8);
\fill (195,31) circle (1.5);
\draw[line width=0.8pt] (194,27) -- (196,23) -- (194,21);
\fill (196,17) circle (1.4);
\fill (196,11) circle (1.3);
\fill (194,-2) circle (1.6);
\end{tikzpicture}}}'''
L2=r'''% Figure L2: raised insertion and its curved oblique arm; the arm crosses the older de.
\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round]
\node[anchor=base west,inner sep=0pt] at (0,0) {Le cosupport};
\node[anchor=base west,inner sep=0pt] at (3.0,0) {\unsure{de|\deleted{de}}};
\node[anchor=base west,inner sep=0pt] at (5.2,0) {tout objet $G$};
\node[anchor=base west,inner sep=0pt] at (2.75,0.65) {\inserted{dans $\unsure{\mathcal F|F}$}};
\draw (2.60,0.07) .. controls (3.25,0.29) and (4.10,0.43) .. (4.48,0.65)
 .. controls (4.57,0.72) and (4.52,0.78) .. (4.45,0.73);
\end{tikzpicture}}'''
L3=r'''% Figure L3: crowded punctuation at the right edge after the order sign; identities remain open.
\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round]
\node[anchor=base west,inner sep=0pt] at (0,0) {en termes de $\leq$};
\draw[line width=0.6pt] (3.27,-0.04) .. controls (3.30,-0.14) and (3.22,-0.23) .. (3.16,-0.28);
\draw[line width=0.6pt] (3.42,0.43) .. controls (3.68,0.10) and (3.66,-0.15) .. (3.45,-0.32);
\draw[line width=0.6pt] (3.56,0.28) .. controls (3.70,0.24) and (3.89,0.20) .. (3.71,0.08)
 -- (3.63,0.01) .. controls (3.77,-0.03) and (3.83,-0.08) .. (3.94,-0.10);
\end{tikzpicture}}'''
L4=r'''% Figure L4: long separator with a downward notch and a rounded descending right end, in scan orientation.
\figure{\begin{tikzpicture}[x=0.006cm,y=0.006cm,line cap=round]
\draw (118,0) .. controls (230,15) and (355,37) .. (441,35)
 .. controls (463,33) and (463,0) .. (492,0)
 .. controls (535,3) and (558,17) .. (592,20)
 .. controls (890,31) and (1325,69) .. (1606,70)
 .. controls (1642,70) and (1641,38) .. (1648,-18)
 .. controls (1652,-92) and (1650,-160) .. (1680,-220);
\end{tikzpicture}}'''
L5=r'''% Figure L5: penultimate line of the inverted cancelled draft, shown upright for reading.
% The point above the second internal deletion and two low points beneath irreductibles are retained.
\figure{\begin{tikzpicture}[x=1cm,y=1cm,line cap=round]
\node[anchor=base west,inner sep=0pt] at (0,0) {\deleted{des}};
\node[anchor=base west,inner sep=0pt] at (0.8,0) {\deleted{\deleted{\unsure{ses|son}}}};
\node[anchor=base west,inner sep=0pt] at (2.2,0) {\deleted{\deleted{\unsure{par|p}}}};
\node[anchor=base west,inner sep=0pt] at (3.7,0) {\deleted{objets}};
\node[anchor=base west,inner sep=0pt] at (4.9,0) {\deleted{irréductibles}};
\node[anchor=base west,inner sep=0pt] at (7.5,0) {\deleted{de $\Phi$.}};
\fill (3.45,0.27) circle (0.018);
\fill (5.20,-0.29) circle (0.018);
\fill (5.27,-0.34) circle (0.018);
\end{tikzpicture}}'''
reading=r'''\scanpage{71}
\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}

Il revient au $=$ de dire que $F$ et $F'$ ont $=$ cosupport, ou encore, même support.

\unsure{Donnons nous} un support.

''' + L1 + r'''
Une autre façon de dire que $F,G\ \text{disj.}\Longrightarrow F',G\ \text{disj}$, est ainsi :

\uline{Corollaire}
''' + L2 + r'''
de $\mathcal F$ est fermé, non seult pour $\leq$, mais aussi pour $\preceq$ -- c'est donc ce qu'on appelle une \uline{sous}-\unsure{contrée|contrie}.

Donc \unsure{itou} pour toute partie $\Phi\subset\mathcal F$.

En d'autres termes, \deleted{toute} partie de $\mathcal F$ qui est un $\mathcal F$-support (ou ``$\mathcal F$-saturée, sous-entendu :
''' + L3 + r'''
cf page $67$) est \unsure{automatiquemt|automatiquement} \deleted{\unsure{f}}une sous-contrée.

''' + L4 + r'''
% Cancelled draft is written upside down on the sheet; the long oblique strokes cancel the entire text block.
% Its text is given below in its own reading order. The folio belongs to that cancelled draft.
\mspage{\deleted{5\deleted{\unsure{4|3}}5}}

\deleted{un ensemble, et $\deleted{\unsure{\mathcal F|F}}\Phi$ un ens de parties de $M$, satisfaisant la condition précédente \unsure{(au --)|(ou --)|(en --)}.}

\deleted{Alors $\Phi$, muni de la relation d'inclusion, satisfait $C\,1$, et ses objets irréductibles sont les $A_x$ $(x\in M)$, l'application $x\mathrel{\vdash\joinrel\dashv} A_x$ étant une bijection de $M$ sur l'ens}
''' + L5 + r'''

\deleted{Dém $A_x$ est irréductible, car si $A_x=\bigcup_{i\in I} A_i$}
'''
(out/'reading.tex').write_text(reading,encoding='utf-8')
D=[]
def diff(id,location,c,h,r,shows,confidence='high',kind='other',marked='no',cc=False,ch=True,crop=None,bbox=None,source=None,math=False):
    if crop:
        cm=cp[crop]; path=cm['path']; bbox=bbox or cm['bbox']; source=source or cm['source']
    else: path=None
    D.append(dict(id=id,location=location,c=c,h=h,reading=r,scan_shows=shows,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=path,bbox=bbox,bbox_image=source,source=source,math_consequential=math))
diff('D01','Running folio',r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}',r'\page{70}',r'\mspage{\deleted{\unsure{69|79}}\unsure{70|79}}','Two overworked numeral positions; the large second loop and descending older stroke do not fix the sequence.','low','deletion state (struck given live or live given struck)',crop='01_folio')
diff('D02','Opening, after au',r'au $=$','au même',r'au $=$','Two separate unequal horizontal strokes replace the word même.',kind='misread symbol or index',bbox=[620,95,815,161],source=half_a)
diff('D03','Opening, after ont',r'ont $=$','ont même',r'ont $=$','A second pair of horizontal strokes is visible after ont.',kind='misread symbol or index',bbox=[270,198,500,250],source=half_a)
diff('D04','Third line',r'\unsure{Donnons nous} un support.',r'Donc \ill{} un support.',r'\unsure{Donnons nous} un support.','The first group is substantially longer than Donc; the medial humps of both words remain compressed.','medium','misread word','yes',crop='02_donnons')
diff('D05','Left margin opposite Une autre façon',r'\margin{$\unsure{!|\vdots}\qquad\unsure{!|\vdots}$}','',L1,'Two broken, vertically offset columns with separate lower points are drawn, without assigning an exclamation-mark function.','high','drawing or diagram',cc=True,crop='03_margin_marks')
diff('D06','Implication sentence punctuation',r'Une autre façon de dire que $F,G\ \text{disj.}\Longrightarrow F\prime,G\ \text{disj}$, est ainsi :'.replace(r'F\prime',"F'"),r'Une autre façon de dire (que $F, G$ disj. $\Longrightarrow F\prime, G$ disj.) est ainsi :'.replace(r'F\prime',"F'"),r'Une autre façon de dire que $F,G\ \text{disj.}\Longrightarrow F\prime,G\ \text{disj}$, est ainsi :'.replace(r'F\prime',"F'"),'There is no opening parenthesis before que; a comma follows the second disj, whose j has no separate following point.','high','other',bbox=[280,375,1580,595],source=half_a)
diff('D07','Corollary correction: de',r'\inserted{dans $\mathcal F$} de',r'\struck{de} \add{dans $\mathfrak{F}$}',r'\unsure{de|\deleted{de}} with raised \inserted{dans $\unsure{\mathcal F|F}$} (Figure L2)','A long rising curved stroke crosses the de ascender and continues under the added phrase; cancellation versus an insertion arm remains open.','low','deletion state (struck given live or live given struck)',cc=True,crop='04_insertion')
diff('D08','Corollary insertion, alphabet only',r'\inserted{dans $\mathcal F$}',r'\add{dans $\mathfrak{F}$}',r'\inserted{dans $\unsure{\mathcal F|F}$}','The small F has a bent stem and extended top, but no securely closed upper loop; Gothic form is unsupported.','medium','misread symbol or index',cc=True,crop='04_insertion')
diff('D09','Corollary insertion arm only','% no drawing','% no drawing',L2,'The distinct rising arm ends in a small curl to the right of the raised F.','high','drawing or diagram',cc=True,crop='04_insertion')
diff('D10','Corollary, de F after objet G',r'de $\mathcal F$',r'de $\mathfrak{F}$',r'de $\mathcal F$','F has a curved stem and looped upper arm, without Gothic angular strokes.',kind='misread symbol or index',bbox=[270,735,470,818],source=half_a)
diff('D11','Corollary, non ... pour',r'non \unsure{seult|seulemt} pour','non seulement pour','non seult pour','After the tall l the stroke runs directly to the final rising t; no second e or full ment is distinguishable.',kind='abbreviation expanded or spelling modernised',cc=True,crop='05_orders_abbreviation')
diff('D12','Corollary, second order sign',r'$\unsure{\preceq|\leqslant}$',r'$\preccurlyeq$',r'$\preceq$','The second sign has two rounded lower strokes, unlike the preceding straight inequality.',kind='misread symbol or index',cc=True,ch=False,crop='05_orders_abbreviation',math=True)
diff('D13','Corollary, after c’est donc',"c'est donc ce qu'on appelle une",r"c'est donc \ill{} \ill{} une","c'est donc ce qu'on appelle une",'The successive groups ce, qu’on and appelle are visible across the line turn.',kind=r'readable ink left as \ill{}',marked='yes',bbox=[277,783,1568,1008],source=half_a)
diff('D14','First sous-contrée',r'\uline{sous}-\unsure{contrée|contrie}',r'\emph{sous}-contrée',r'\uline{sous}-\unsure{contrée|contrie}','The short penultimate letter under its raised tick does not securely distinguish é from i.','medium','misread word',crop='06_contree')
diff('D15','Donc itou',r'Donc \unsure{itou}','Donc itou',r'Donc \unsure{itou}','The i and ou are visible, but the tall retraced middle and high terminal stroke leave the word uncertain.','medium','misread word',crop='07_itou')
diff('D16','Donc paragraph, family alphabet',r'$\Phi\subset\mathcal F$',r'$\Phi \subset \mathfrak{F}$',r'$\Phi\subset\mathcal F$','The final F has a clear oval upper loop and curved lower stem.',kind='misread symbol or index',crop='06_contree')
diff('D17','Restatement, toute state',r'\deleted{toute} partie','toute partie',r'\deleted{toute} partie','A horizontal cancellation crosses the whole of toute before partie.',kind='deletion state (struck given live or live given struck)',bbox=[1135,1090,1525,1175],source=half_a)
diff('D18','Restatement, three family-F occurrences',r'de $\mathcal F$ qui est un $\mathcal F$-support (ou ``$\mathcal F$-saturée',r'de $\mathfrak{F}$ qui est un $\mathfrak{F}$-support (ou « $\mathfrak{F}$-saturée »',r'de $\mathcal F$ qui est un $\mathcal F$-support (ou ``$\mathcal F$-saturée','All three F forms are looped or bent manuscript forms; the alphabet is not Gothic. This row concerns alphabet only.',kind='misread symbol or index',crop='08_live_final')
diff('D19','Restatement quotation marks',r'(ou ``$\mathcal F$-saturée,',r'(ou « $\mathfrak{F}$-saturée »,',r'(ou ``$\mathcal F$-saturée,','Two short opening quote strokes occur before F; no closing pair occurs before the comma. This row concerns quotation marks only.',kind='other',crop='08_live_final')
diff('D20','Restatement, punctuation after order sign',r'en termes de $\leq$\unsure{,)|,) ;}',r'en termes de $\leq$,',L3,'Comma-like lower curve, tall closing curve and connected rightmost angular strokes are all retained graphically.','low','drawing or diagram',cc=True,crop='08_live_final')
diff('D21','Restatement page reference','cf page $67$','cf p. 67','cf page $67$','The group after cf is the longer page with a descending loop, without an abbreviation point.',kind='abbreviation expanded or spelling modernised',crop='08_live_final')
diff('D22','Restatement, automatically',r'\unsure{automatiquemt|automatiquement}','automatiquement',r'\unsure{automatiquemt|automatiquement}','The latter part contracts to a long connecting stroke and final t; abbreviated versus full ending is unresolved.','low','misread word',crop='08_live_final')
diff('D23','Restatement, mark immediately before une',r'\deleted{\unsure{f}}une','une',r'\deleted{\unsure{f}}une','A separately placed looped f-like form is crossed by a descending stroke.','medium','omission',crop='08_live_final')
diff('D24','Live paragraph divisions','Donc ...\n\nEn d\'autres termes,','Donc ... En d\'autres termes,','Donc ...\n\nEn d\'autres termes,','Donc and En d’autres termes start independent left-aligned blocks.','high','insertion or placement',bbox=[270,970,1610,1215],source=half_a)
diff('D25','Separator between live text and inverted draft','% no drawn separator',r'\note{la moitié inférieure de la feuille porte, écrit tête-bêche et séparé du haut par un trait, un début de page numéroté « 55 » (chiffre surchargé), barré de longs traits obliques : c\'est le texte donné ici entre les marques de biffure}',L4,'A long rule has a notch near the left and a rounded descending return at the right; H mentions a rule only editorially.','high','drawing or diagram',cc=True,bbox=[112,425,1689,750],source=half_b)
diff('D26','Inverted folio',r'\mspage{\deleted{\unsure{5\deleted{\unsure{4|3}}5}}}',r'\note{... numéroté « 55 » (chiffre surchargé) ...} [editorial note]',r'\mspage{\deleted{5\deleted{\unsure{4|3}}5}}','The first and surface second digits have clear 5 forms; only the overwritten upper strokes in the second digit remain uncertain.','medium','other',cc=True,crop='09_draft_folio')
diff('D27','Inverted draft, worked capital after et',r'$\deleted{\unsure{\mathcal F|F}}\Phi$',r'$\Phi$',r'$\deleted{\unsure{\mathcal F|F}}\Phi$','The live oval and central stem of Phi contain older straight cross-strokes; the underlying F alphabet remains uncertain.','low','omission',crop='10_draft_opening_right',math=True)
diff('D28','Inverted draft, un after Phi',r'\unsure{un}','un','un','The small two-hump group after the worked Phi reads un.',kind='misread word',cc=True,ch=False,crop='10_draft_opening_right')
diff('D29','Inverted draft, first ens abbreviation','ens','ens.','ens','No detached point follows the final downward ens tail.',kind='abbreviation expanded or spelling modernised',crop='11_draft_opening_left')
diff('D30','Inverted draft, de parties',r'\unsure{de|des} parties','de parties','de parties','The compact loop and tail match de; no separate terminal s is visible.',kind='misread word',cc=True,ch=False,crop='11_draft_opening_left')
diff('D31','Inverted draft, first ambient M',r'$M$',r'$\mathcal{M}$',r'$M$','Two plain peaks and a returned final stem form M.',kind='misread symbol or index',crop='11_draft_opening_left')
diff('D32','Inverted draft, satisfaisant la condition','satisfaisant la condition','satisfaisant à la condition','satisfaisant la condition','The next group after satisfaisant is la; there is no separate à before it.',kind='text not on the page',crop='10_draft_opening_right')
diff('D33','Inverted draft, parenthetical after précédente',r'\unsure{(au --)|(ou --)|(en --)}',r'(\ill{})',r'\unsure{(au --)|(ou --)|(en --)}','A small looped vowel group and a separate short dash lie inside the parentheses.','low',r'readable ink left as \ill{}','yes',crop='11_draft_opening_left')
diff('D34','Inverted draft, inclusion punctuation',"relation d'inclusion, satisfait", "relation d'inclusion satisfait", "relation d'inclusion, satisfait",'A small descending hooked stop follows the final inclusion strokes at the margin.','medium','other',crop='12_draft_alors')
diff('D35','Inverted draft, object/quantifier letters',r'$A_x$ $(x\in M)$',r'$A_X$ ($X \in \mathcal{M}$)',r'$A_x$ $(x\in M)$','Both crosses are small lower-case x forms; M has two plain peaks.',kind='misread symbol or index',crop='14_draft_Ax_M')
diff('D36','Inverted draft, application relation and endpoints',r'$x\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto} A_x$',r'$X \mapsto A_X$',r'$x\mathrel{\vdash\joinrel\dashv} A_x$','The horizontal has a vertical tick at each end and no pointed right head; both x forms are small crosses.',kind='misread symbol or index',cc=True,crop='13_draft_application',math=True)
diff('D37','Inverted draft, M after bijection de',r'$M$',r'$\mathcal{M}$',r'$M$','The M has a looped entry but remains a single cursive two-peak capital, not a separate decorated alphabet.',kind='misread symbol or index',crop='13_draft_application')
diff('D38','Inverted draft, second ens abbreviation',"l'ens", "l'ens.","l'ens",'The final ens tail has no detached following point.',kind='abbreviation expanded or spelling modernised',crop='13_draft_application')
diff('D39','Inverted draft, internal deletion',r'\deleted{\unsure{ses|son} \unsure{par|p}}',r'\struck{\ill{}}',r'\deleted{\unsure{ses|son} \unsure{par|p}}','Two word-sized groups have separate horizontal strikes; the first begins s, the second has a clear descending p.','low',r'readable ink left as \ill{}','yes',crop='16_draft_deletion_dem')
diff('D40','Inverted draft, point above second internal deletion','% no point','% no point',L5+'\n% Scope: the point above the second deletion only.','A separate small point stands above and just beyond the second crossed group.','high','drawing or diagram',cc=True,crop='16_draft_deletion_dem')
diff('D41','Inverted draft, two points below irréductibles','% no points','% no points',L5+'\n% Scope: the two low points beneath irréductibles only.','Two separate points sit below the word, the right one lower; no function is assigned.','high','drawing or diagram',cc=True,crop='15_draft_final_left')
diff('D42','Inverted final line, proof abbreviation',r'\unsure{Dém|Dire|Bien}','Dém.','Dém','A D loop, a short raised accent and final m humps are visible; there is no terminal point.',kind='abbreviation expanded or spelling modernised',cc=True,crop='16_draft_deletion_dem')
diff('D43','Inverted final line, repeated x subscripts',r'$A_x$ est irréductible, car si $A_x=\bigcup_{i\in I} A_i$',r'$A_X$ est irréductible, car si $A_X = \bigcup_{i \in I} A_i$',r'$A_x$ est irréductible, car si $A_x=\bigcup_{i\in I} A_i$','The two subscripts are lower-positioned small crosses, matching x in the quantified line.',kind='misread symbol or index',crop='15_draft_final_left',bbox=[45,1485,1135,1735])
diff('D44','Inverted draft paragraph divisions','un ensemble ...\n\nAlors ...\n\nDém ...',r'\struck{un ensemble ... Alors ... Dém. ...}','un ensemble ...\n\nAlors ...\n\nDém ...','Alors and Dém begin separate lines with fresh starts; their paragraph boundaries are preserved.','high','insertion or placement',bbox=[50,1490,1440,2280],source=whole)

CD=[]
def doubt(location,c,r,status,shows,crop=None,bbox=None,source=None,contexts=None):
    if crop:
        cm=cp[crop]; path=cm['path']; bbox=bbox or cm['bbox']; source=source or cm['source']
    else:path=None
    CD.append(dict(location=location,c=c,reading=r,status=status,scan_shows=shows,crop=path,bbox=bbox,bbox_image=source,source=source,context_rows=contexts or []))
doubt('Running folio, underlying number',r'\deleted{\unsure{69|79}}',r'\deleted{\unsure{69|79}}','retained','The older loop and transverse strokes cannot be isolated securely.','01_folio',contexts=[7])
doubt('Running folio, surface number',r'\unsure{70|79}',r'\unsure{70|79}','retained','The last digit combines a large loop and descending stem.','01_folio',contexts=[7])
doubt('Donnons nous',r'\unsure{Donnons nous}',r'\unsure{Donnons nous}','retained','Several medial groups are low disconnected humps.','02_donnons',contexts=[8])
doubt('First marginal column',r'\unsure{!|\vdots}',L1,'revised','Broken vertical strokes and a low offset point are drawn literally.','03_margin_marks',contexts=[6,21])
doubt('Second marginal column',r'\unsure{!|\vdots}',L1,'revised','Several separated points form the second, higher column.','03_margin_marks',contexts=[6,21])
doubt('non ... pour',r'\unsure{seult|seulemt}','seult','resolved','The l is followed by a connecting stroke and final t.','05_orders_abbreviation',contexts=[9])
doubt('Second order glyph',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','Both lower strokes are rounded, unlike the preceding straight sign.','05_orders_abbreviation',contexts=[2,10])
doubt('First contrée',r'\unsure{contrée|contrie}',r'\unsure{contrée|contrie}','retained','The letter beneath the short raised stroke is too compressed.','06_contree',contexts=[11])
doubt('itou',r'\unsure{itou}',r'\unsure{itou}','retained','The worked tall middle cannot be separated into secure individual strokes.','07_itou',contexts=[12])
doubt('After live-text order sign',r'\unsure{,)|,) ;}',L3,'revised','The visible comma-like curve and composite closing strokes are drawn without suppressing the right-hand component.','08_live_final',contexts=[13])
doubt('automatiquemt',r'\unsure{automatiquemt|automatiquement}',r'\unsure{automatiquemt|automatiquement}','retained','The latter letters contract into a long stroke before final t.','08_live_final',contexts=[14])
doubt('Cancelled mark before une',r'\deleted{\unsure{f}}',r'\deleted{\unsure{f}}','retained','A crossed looped f-like form is clear, but its identity is not.','08_live_final',contexts=[15])
doubt('Inverted folio, outer uncertainty',r'\unsure{5\deleted{\unsure{4|3}}5}',r'5\deleted{\unsure{4|3}}5','revised','First and final visible digits are 5; uncertainty is restricted to the overwritten digit.','09_draft_folio',contexts=[16])
doubt('Inverted folio, underlying digit',r'\unsure{4|3}',r'\unsure{4|3}','retained','The worked upper bar and interior strokes do not determine 4 versus 3.','09_draft_folio',contexts=[16])
doubt('Capital beneath inverted Phi',r'\deleted{\unsure{\mathcal F|F}}',r'\deleted{\unsure{\mathcal F|F}}','retained','Additional cross-strokes occupy the same capital position; their F alphabet is not secure.','10_draft_opening_right',contexts=[17])
doubt('un after inverted Phi',r'\unsure{un}','un','resolved','The small group has a u-like entry and final n hump.','10_draft_opening_right',contexts=[17])
doubt('de before parties',r'\unsure{de|des}','de','resolved','The loop and terminal tail form de without a separate s.','11_draft_opening_left',contexts=[22])
doubt('Parenthetical after précédente',r'\unsure{(au --)|(ou --)|(en --)}',r'\unsure{(au --)|(ou --)|(en --)}','retained','The initial loop allows different small-vowel readings; the short dash is separate.','11_draft_opening_left',contexts=[17])
doubt('Application sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mathrel{\vdash\joinrel\dashv}','resolved','The right end is an upright tick without an arrowhead.','13_draft_application',contexts=[4,18])
doubt('First internal deleted word',r'\unsure{ses|son}',r'\unsure{ses|son}','retained','The horizontal strike masks the middle and final joins.','16_draft_deletion_dem',contexts=[19])
doubt('Second internal deleted word',r'\unsure{par|p}',r'\unsure{par|p}','retained','A descending p is visible, with the remaining horizontal strokes obscured.','16_draft_deletion_dem',contexts=[19])
doubt('Last line initial abbreviation',r'\unsure{Dém|Dire|Bien}','Dém','resolved','The D loop, raised accent and m humps are visible.','16_draft_deletion_dem',contexts=[20])
doubt('Opening literal repetition signs',r'$=$ (twice)',r'$=$ (twice)','resolved','Two unequal horizontal strokes appear in each place.',bbox=[270,95,820,255],source=half_a,contexts=[1])
doubt('First straight order sign',r'\leq',r'\leq','resolved','The upper angled stroke and separate straight lower bar remain distinct.','05_orders_abbreviation',contexts=[2])
doubt('Inserted family alphabet',r'\mathcal F',r'\unsure{\mathcal F|F}','revised','The small inserted F has a bent stem but lacks a secure closed top loop.','04_insertion',contexts=[3])
doubt('Donc formula: Phi and inclusion and family F',r'\Phi\subset\mathcal F',r'\Phi\subset\mathcal F','resolved','Phi is oval with a central upright and foot; inclusion is open; F has a clear loop.','06_contree',contexts=[3])
doubt('Final union index and final A subscript',r'\bigcup_{i\in I} A_i',r'\bigcup_{i\in I} A_i','resolved','The lower i is dotted, I has bars, and the final raised dot belongs to the small i rather than a terminal stop.','15_draft_final_left',contexts=[5,23])
doubt('toute deletion before partie',r'\deleted{toute} partie',r'\deleted{toute} partie','resolved','The whole of toute has a horizontal cancellation.',bbox=[1135,1090,1525,1175],source=half_a,contexts=[24])
doubt('Inverted muni',r'\Phi, muni',r'\Phi, muni','resolved','The final narrow stroke has no separate following e.','12_draft_alors',contexts=[25])

R=[]
def rem(loc,r,alts,conf,reason):R.append(dict(location=loc,reading=r,alternatives=alts,confidence=conf,reason=reason))
rem('Running folio',r'\deleted{\unsure{69|79}}\unsure{70|79}',['69 beneath 70','79 as underlying or surface number'],'low','Overwritten loops and descending stems do not establish writing order.')
rem('Third line',r'\unsure{Donnons nous}',['Donnons nous'],'medium','The medial letters reduce to disconnected low strokes.')
rem('Margin columns','Figure L1',['exclamation-like marks','vertical dot groups','incidental marks'],'low','The shapes can be drawn but their function and intentionality are not established.')
rem('Corollary de',r'\unsure{de|\deleted{de}}',['live de crossed incidentally by insertion arm','cancelled de'],'low','The same oblique stroke can be read as leader or cancellation.')
rem('Inserted F',r'\unsure{\mathcal F|F}',[r'\mathcal F','F'],'medium','The small form has a curved stem but no secure upper loop.')
rem('First sous-contrée',r'\unsure{contrée|contrie}',['contrée','contrie'],'medium','The accented/dotted penultimate letter is reduced.')
rem('Donc itou',r'\unsure{itou}',['itou'],'medium','The tall middle is heavily retraced and a high final stroke remains difficult to assign.')
rem('After live order sign','Figure L3',[',)',',);',',)}','one worked composite closing mark'],'low','The extra rightmost strokes cannot be assigned securely to punctuation types.')
rem('Restatement adverb',r'\unsure{automatiquemt|automatiquement}',['automatiquemt','automatiquement'],'low','The contracted ending does not expose all individual letters.')
rem('Cancelled form before une',r'\deleted{\unsure{f}}',['f'],'medium','A looped cancelled form is readable only approximately.')
rem('Inverted folio underlying digit',r'5\deleted{\unsure{4|3}}5',['4','3'],'low','Upper cross-strokes overlap the surface 5.')
rem('Inverted worked Phi',r'\deleted{\unsure{\mathcal F|F}}\Phi',[r'\mathcal F under \Phi',r'F under \Phi'],'low','The older strokes share the live capital position.')
rem('Inverted parenthetical',r'\unsure{(au --)|(ou --)|(en --)}',['(au --)','(ou --)','(en --)'],'low','A looped small vowel group precedes a clear short dash.')
rem('First internal deletion',r'\unsure{ses|son}',['ses','son'],'low','A straight cancellation masks the joins.')
rem('Second internal deletion',r'\unsure{par|p}',['par','p'],'low','Only the p descender is secure below the horizontal strike.')

inventory=[]
def inv(element,kind,position,first,sheet='text'):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind=sheet,hand='his hand',transcribed='yes'))
inv('I01','text','top centre','Worked running folio 70/79')
inv('I02','deletion','under running folio','Older 69/79')
inv('I03','text','upper two lines','Il revient au =')
inv('I04','text','upper third line','Donnons nous un support')
inv('I05','margin note','left of Une autre façon','Two vertical broken groups')
inv('I06','drawing','same margin, Figure L1','Broken columns and low points')
inv('I07','text','upper middle, two lines','Une autre façon de dire')
inv('I08','text','middle, heading and corollary','Corollaire; Le cosupport')
inv('I09','insertion','above de after cosupport','dans F')
inv('I10','deletion','de after cosupport, state uncertain','de, possibly cancelled')
inv('I11','drawing','around raised phrase, Figure L2','Curved oblique insertion/cancellation arm')
inv('I12','text','middle lower','Donc itou pour toute partie')
inv('I13','text','last live paragraph','En d’autres termes')
inv('I14','deletion','after En d’autres termes','toute')
inv('I15','drawing','right edge after ≤, Figure L3','Comma-like and closing strokes')
inv('I16','deletion','before une in last live paragraph','f-like looped form')
inv('I17','drawing','between upright and inverted writing, Figure L4','Long notched separator and right return')
inv('I18','text','bottom centre in scan orientation; top of inverted draft','Worked folio 55','cancelled_draft')
inv('I19','deletion','second digit of inverted folio','Underlying 4/3','cancelled_draft')
inv('I20','deletion','entire inverted lower block','Long oblique cancellation of draft','cancelled_draft')
inv('I21','text','first paragraph in rotated reading order','un ensemble, et Phi un ens','cancelled_draft')
inv('I22','deletion','same capital position beneath first Phi','Earlier F-like capital','cancelled_draft')
inv('I23','text','second paragraph in rotated reading order','Alors Phi, muni','cancelled_draft')
inv('I24','deletion','after l’ens des','ses/son','cancelled_draft')
inv('I25','deletion','next crossed group','par/p','cancelled_draft')
inv('I26','drawing','above second crossed group, Figure L5','One detached point','cancelled_draft')
inv('I27','drawing','below irréductibles, Figure L5','Two diagonally offset points','cancelled_draft')
inv('I28','text','last line of inverted draft','Dém Ax est irréductible','cancelled_draft')

notation=[
dict(sign='literal repetition',latex=r'=',appearance='Two separate unequal horizontal strokes.',location='Opening, twice',alternatives=[]),
dict(sign='family F',latex=r'\mathcal F',appearance='Looped top and bent stem; inserted small F is less complete.',location='Live corollary and restatement',alternatives=[r'F at the insertion only']),
dict(sign='straight order',latex=r'\leq',appearance='Angled upper stroke and separate straight lower bar.',location='Corollary first order and restatement',alternatives=[]),
dict(sign='curved order',latex=r'\preceq',appearance='Pointed upper branch and two rounded lower strokes.',location='Corollary second order',alternatives=[]),
dict(sign='Phi and inclusion',latex=r'\Phi\subset\mathcal F',appearance='Oval with upright and foot, then open curved inclusion.',location='Donc paragraph',alternatives=[]),
dict(sign='ticked application line',latex=r'\mathrel{\vdash\joinrel\dashv}',appearance='Horizontal line with a short vertical tick at each end; no pointed head.',location='Inverted application',alternatives=[]),
dict(sign='x and i indices',latex=r'A_x,\;\bigcup_{i\in I} A_i',appearance='Crossed lower x, small dotted i, barred capital I.',location='Inverted statements and final formula',alternatives=[]),
dict(sign='ambient M',latex='M',appearance='Single two-peak capital; one cursive entry loop does not establish a separate alphabet.',location='All three inverted occurrences',alternatives=[]),
dict(sign='graphic points',latex='Figures L1 and L5',appearance='Broken marginal columns, one high point, and two low diagonally offset points.',location='Left margin and inverted penultimate line',alternatives=['Function not assigned']),
]
abbreviations=[dict(form='disj.',expansion='disjoints'),dict(form='disj',expansion='disjoints'),dict(form='seult',expansion='seulement'),dict(form='automatiquemt',expansion='automatiquement (abbreviated candidate)'),dict(form='cf',expansion='confer'),dict(form='ens',expansion='ensemble'),dict(form='Dém',expansion='Démonstration'),dict(form='(au --)',expansion='Possibly au moins; not expanded in the transcription')]
report=dict(reader='R3',cote='156-4',scan='71',brief_version='v07',started_utc='2026-11-20T11:30:32Z',finished_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),image_views=meta['images'],reading_file=str(out/'reading.tex'),differences=D,c_doubts=CD,inventory=inventory,remaining_doubts=R,notation=notation,abbreviations=abbreviations,notes=dict(summary='The upright passage is followed by an inverted cancelled draft. Literal equals signs, contractions and overwritten states are retained; five TikZ figures preserve marginal and connecting marks.',math_reading_decisions='The contrast between the two order signs prompted a local comparison of their lower strokes. The apparent mapping prompted inspection of its right end; ink gives a terminal upright, not a visible arrowhead. All x/i/I decisions use local strokes. No theorem was proved or checked.',author_checks='No explicit author proof check appears; Dém starts an unfinished proof inside the cancelled draft. Its statement is transcribed, not validated.',title_dates_pagination='No title or date. Running folio remains 70/79 over 69/79; inverted draft surface folio is 55 over an uncertain 4/3 in its second position. No adjacent folios were consulted.'),check_events=[],crops=crops,workflow_feedback=['The instruction to make one crop per open place can conflict with collecting nearby small marks on the same line; adjacent unresolved loci were combined in a single tight crop, with no recrop of any decided locus.','Several crowded punctuation/leader shapes are more faithful as local TikZ drawings than as invented conventional punctuation.'])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
log=['# R3 inspection log — scan 071','', 'Started at first recorded clock: 2026-11-20T11:30:32Z.','Packet text, conventions, preamble, C context and the supplied notation snapshot were read before image inspection. No other readers, scans, OCR, external sources, or LaTeX compiler were used.','', '## Supplied views (each once, in order)','1. '+whole+' — whole-page layout; upright text, overwritten folio, left marks, raised phrase, separator, inverted cancelled draft.','2. '+half_a+' — upper half, every line read against C and H.','3. '+half_b+' — lower half, remaining live text and all inverted lines inspected; rotated readings deferred to tight crops.','','## Own crops (each viewed once, in order)']
evidence=[
'Numeral layers remain uncertain; complete running folio retained.',
'Long first group supports Donnons; the reduced middles keep the phrase doubtful.',
'Two broken columns, offset in height, with low detached points; shapes drawn literally.',
'Raised dans F, arm crossing de, small alphabet doubt; objet G has a returned lower-right stroke.',
'seult resolves; first inequality straight, second with rounded lower strokes.',
'First contrée remains doubtful; Phi/inclusion/final family F are clear.',
'itou has a retraced middle; no separate older complete word asserted.',
'Opening quote pair only; cf page; punctuation after ≤ drawn; adverb and cancelled f-like form remain doubtful.',
'Surface 55 clear; underlying second digit remains 4/3.',
'Overwritten Phi includes older F-like strokes; un resolves; satisfaisant followed directly by la.',
'No point after ens; de resolves; plain M; short vowel group and separate dash retained in parentheses.',
'muni, C 1 and the following words read; marginal comma after inclusion retained.',
'Horizontal application sign has two upright ends; M and point-less l’ens inspected. Adjacent capital tops are clipped, but the target sign is wholly framed.',
'Local small x forms, membership, plain M and bijection read.',
'Final i, membership and barred I read; no additional terminal stop. Two low points under preceding word identified.',
'Two independently crossed groups remain ses/son and par/p. One high detached point retained. Dém resolves without a final point.'
]
for i,(c,e) in enumerate(zip(crops,evidence),4):
 log += [f'{i}. {c["path"]}',f'   Source: {c["source"]}; original bbox {c["bbox"]}; scale {c["scale"]:.9f}; rotation {c["rotation"]} degrees.', '   Transforms: '+', '.join(c['transforms'])+'.','   Evidence: '+e]
log += ['', '## Completion checks','All image emissions were visible and untruncated. No image was reopened and no place recropped.','Structural checks only: balanced braces/environment pairs, required fields, boolean types, crop existence, exact-source coordinates, all 25 C-context rows mapped, no math illegible marker, and remaining-doubt snippets aligned with reading.tex.','No mathematical validation was performed; check_events is empty.']
(out/'inspection_log.md').write_text('\n'.join(log)+'\n',encoding='utf-8')
print(json.dumps({'differences':len(D),'c_doubts':len(CD),'remaining_doubts':len(R),'inventory':len(inventory),'crops':len(crops)},indent=2))
