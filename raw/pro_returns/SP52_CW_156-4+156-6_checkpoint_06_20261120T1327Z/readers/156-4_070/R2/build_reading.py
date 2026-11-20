from pathlib import Path
import json
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R2')
whole='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan070.jpg'
halfa=whole.replace('.jpg','_a.jpg'); halfb=whole.replace('.jpg','_b.jpg')
manifest=json.loads((out/'crop_manifest.json').read_text())
byname={Path(x['path']).stem:x for x in manifest}
fig1=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=base west] at (0,0) {figures};
\node[anchor=base west] at (0.55,0.58) {\inserted{$F',F''$}};
\node[anchor=base west] at (2.55,0.69) {$\inserted{\unsure{\deleted{\preceq}|\preceq}-}$};
\draw (2.50,-0.08) .. controls (2.57,0.18) and (3.16,0.37) .. (3.70,0.61);
\node[anchor=base west] at (2.95,0.03) {\unsure{en général|en position}};
\end{tikzpicture}}'''
diag=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,row sep=0.25em,column sep=0.4em]
\& F' \arrow[r,phantom,"{\begin{tikzpicture}[baseline=-0.5ex,x=0.5cm,y=0.5cm]\node at (0,0) {$\scriptstyle\unsure{\preceq}$};\draw[thin] (-0.18,0.02) -- (0.24,0.28);\end{tikzpicture}}" description] \& F \\
F''' + "'''" + r''' \arrow[ur,phantom,"\scriptstyle\preceq" description,sloped] \arrow[dr,phantom,"\scriptstyle\preceq" description,sloped] \& \& {} \\
\& F'' \arrow[ur,phantom,"\scriptstyle\preceq" description,sloped] \&
\end{tikzcd}}'''
fig3=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=base west] at (0,0) {\deleted{on a}};
\fill (1.65,0.10) circle (0.012);
\fill (1.75,0.02) circle (0.012);
\end{tikzpicture}}'''
fig4=r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) .. controls (0.03,-0.55) and (0.02,-1.44) .. (0.12,-1.72);
\draw (0.17,0.01) .. controls (0.25,-0.60) and (0.22,-1.30) .. (0.27,-1.65);
\node[anchor=north west,text width=12cm,align=left] at (0.45,0.55) {\uline{C5} Soit $F'\preceq F$. Alors pour tte figure $G$, $G$ est disjointe de $F$ ssi elle est disjointe de $F'$. [\uline{NB} Il suffit de le poser pour $\deleted{\unsure{F}}G=\unsure{X|x}\in M$, à cause de C3]};
\end{tikzpicture}}'''
reading=r'''\scanpage{70}\mspage{69}
J'en viens à la rel d'ordre $\preceq$ (subdivision), de nature \unsure{très|trs} différente. Il n'y \unsure{aura} pas de plus petit (ni de plus grand) élément, pas de $\mathrm{Sup}$ de deux \deleted{\unsure{éléments|élémen}}
% G1: local interlinear layout; the separate oblique arm has no supplied arrowhead.
'''+fig1+r'''
(i.e. Subdivisions d'une $=$ figure $F$, mais parfois un $\inf$.

On dit que deux subdivision $F',F'''+"'''"+r'''$ de $F$ sont \uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles} \deleted{\unsure{quand et|on dit|c.à.d.} que \unsure{seulement|sub}} (je ne dirai pas ``compatibles'', vu que le terme est déjà pris) si elles admettent une subdivision commune.

% D1: the sole right F is level with the upper F'; the lower-right relation ends in blank space.
% The additional thin upper stroke belongs to the worked upper-right relation; no separate complete older glyph is asserted.
'''+diag+r'''
% slanted
\margin{On sera amené à renforcer encore cette condition sur les contrées modérées !}

On dit que la \uuline{\unsure{contrée|contrie}} est \uuline{modérée} si deux subdivisions \unsure{d'|\deleted{d'}}\unsure{une|un} $=$ $F$ sont toujours comparables. \deleted{Dans le cas qui vient,}
% G3: cancelled words and their two detached points, kept without assigning punctuation function.
'''+fig3+r'''

\deleted{\uline{C5}} Je ne saurais donner aucune propriété particulière de $\preceq$ \deleted{tout} seul. Les propriétés que j'ai en vue concernent \unsure{ses|les} relations avec $\leq$.

% slanted
\margin{Reporter après C6, $C7_0$ \unsure{ces|mes} axiomes de \uline{disjonction}}
% G4: the two long marks stand to the left of the live C5 axiom.
'''+fig4+'\n'
(out/'reading.tex').write_text(reading)
D=[]
def diff(i,loc,c,h,reading,evidence,confidence='high',kind='other',marked='no',cc=False,ch=False,crop=None,bbox=None,source=None,math=False):
    z={'id':i,'location':loc,'c':c,'h':h,'reading':reading,'scan_shows':evidence,'confidence':confidence,'kind':kind,'marked_in_h':marked,'change_c':cc,'change_h':ch,'crop':None,'bbox':bbox,'bbox_image':source or whole,'math_consequential':math}
    if crop:
        cr=byname[crop];z.update(crop=cr['path'],bbox=list(cr['bbox']),bbox_image=cr['source'])
    D.append(z)
diff('D01','Opening abbreviation',r'rel',r'rel.',r'rel','Upper half: final l ends in a hook; the following blank has no detached full stop.',kind='abbreviation expanded or spelling modernised',ch=True,bbox=[882,155,1032,235],source=halfa)
diff('D02','Opening relation',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','Bent upper angle and separately bowed lower stroke, unlike the straight final order sign after avec.',kind='misread symbol or index',cc=True,crop='c01_opening',math=True)
diff('D03','After (subdivision)',r'(subdivision),',r'(subdivision)',r'(subdivision),','A detached comma curls below and to the right of the closing parenthesis.',ch=True,crop='c01_opening')
diff('D04','Reduced word before différente',r'\unsure{très|trs}',r'très',r'\unsure{très|trs}','The t and final reduced s are clear, but an independent e cannot be isolated; the high point is too compact to settle accent versus dot.',confidence='medium',ch=True,crop='c01_opening')
diff('D05','Verb after Il n\'y',r'\unsure{aura}',r'a',r'\unsure{aura}','There are two separated groups after n\'y: an au-like group and a further ra-like group. The latter cannot be omitted; reduced internal letters retain doubt.',confidence='medium',kind='misread word',ch=True,crop='c01_opening')
diff('D06','Cancelled noun after de deux',r'\deleted{\unsure{éléments|élémen}}',r'\struck{\ill{}}',r'\deleted{\unsure{éléments|élémen}}','An initial accented e, a tall l and later upright survive a long cancellation; the full ending remains obscured.',confidence='medium',kind='readable ink left as \\ill{}',marked='yes',ch=True,crop='c02_cancelled_noun')
diff('D07','Live noun below raised formula',r'figures',r'',r'figures','The large live word under the raised F letters has the initial looped f, descending g and final reduced plural group.',kind='omission',ch=True,crop='c03_raised_condition')
diff('D08','Raised relation, trailing dash and state',r'\inserted{$F\',F\'\'\preceq-$}',r'\add{$F\'$, $F\'\'$} \struck{$\preccurlyeq$}',r'\inserted{$F\',F\'\'$} $\inserted{\unsure{\deleted{\preceq}|\preceq}-}$','F prime and F double prime are securely raised; a heavily worked relation and separate short dash occupy the same raised line. Dense extra horizontal strokes leave cancellation versus retracing open.',confidence='low',kind='deletion state (struck given live or live given struck)',cc=True,ch=True,crop='c03_raised_condition',math=True)
diff('D09','Distinct arm below raised condition',r'',r'',fig1,'A separate long curved diagonal runs from below the raised relation down-left towards the baseline phrase. It has no secure arrowhead; G1 reproduces it and the adjoining words once.',kind='drawing or diagram',cc=True,ch=True,crop='c03_raised_condition')
diff('D10','Phrase after figures',r'\unsure{en général|en position}',r'toujours',r'\unsure{en général|en position}','A short en-like group precedes a separate descender-led word. The latter is too reduced for a secure choice between the retained readings; a single toujours does not account for the separated groups.',confidence='low',kind='misread word',ch=True,crop='c03_raised_condition')
diff('D11','Dotted parenthetic group',r'\unsure{(i.e.|liée.|lire.}',r'(i.e.',r'(i.e.','An opening curved parenthesis precedes a dotted short i and a low point, then an e-like stroke and a separate final point.',kind='misread word',cc=True,crop='c04_ie_subdivisions')
diff('D12','Initial of Subdivisions',r'Subdivisions',r'subdivisions',r'Subdivisions','The initial is a full-height separate capital S-like stroke.',kind='abbreviation expanded or spelling modernised',ch=True,crop='c04_ie_subdivisions')
diff('D13','Repetition sign before figure F',r'\unsure{=|même}',r'même',r'$=$','Two parallel horizontal traces joined at their left end occupy the whole space; no letters of même are present.',kind='misread symbol or index',cc=True,ch=True,crop='c05_repetition_f')
diff('D14','Punctuation after figure F',r'$F$,',r'$F$),',r'$F$,','A comma follows F. The open space before it has no closing parenthesis.',kind='text not on the page',ch=True,crop='c05_repetition_f')
diff('D15','Second paragraph noun ending',r'deux subdivision',r'deux subdivisions',r'deux subdivision','The final group ends in one n-like angular sweep; there is no distinguishable terminal plural s.',kind='abbreviation expanded or spelling modernised',ch=True,crop='c06_second_noun_primes')
diff('D16','Second subdivision prime count',r"F',\unsure{F'''|F''}",r"F',F''",r"F',F'''",'Three short distinct ticks follow the second F; the first F has one.',kind='misread symbol or index',cc=True,ch=True,crop='c06_second_noun_primes',math=True)
diff('D17','Underlined worked adjective',r'\uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles}',r'\emph{\uncertain{compatibles}}',r'\uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles}','One underlined word has clearly worked central letters. The comp opening and bles ending survive; the prior ati/atib and final ara/ati/ata cannot be separated securely. H\'s editorial comment correctly notes overworking, but its literal transcription does not retain the central deleted layer.',confidence='low',kind='deletion state (struck given live or live given struck)',marked='yes',ch=True,crop='c07_worked_adjective',math=True)
diff('D18','Cancelled clause after adjective',r'\deleted{\unsure{on dit|c.à.d.} que \unsure{sub}}',r'\struck{quand et que seulement}',r'\deleted{\unsure{quand et|on dit|c.à.d.} que \unsure{seulement|sub}}','A long cancellation crosses three main groups. The middle que is secure; the first includes a round initial and two tall stems, and the last begins with an s-like stroke and ends in a tall stroke. Neither witness settles the obscured interiors.',confidence='low',kind='misread word',cc=True,ch=True,crop='c07_worked_adjective')
diff('D19','Quotation marks around compatibles',r"``compatibles''",'« compatibles »',r"``compatibles''",'Two short opening strokes and two closing upright strokes are visible, rather than guillemets.',ch=True,crop='c07_worked_adjective')
diff('D20','Word before que le terme',r'vu',r'car',r'vu','The group has a two-hump v/u movement, without the letters c-a-r.',kind='misread word',ch=True,crop='c07_worked_adjective')
diff('D21','Subdivision diagram: layout and endpoint placement',r'\diagram{\begin{tikzcd} & F\' & \\ F\'\'\' & & F \\ & F\'\' & \end{tikzcd}}',r"$F''' \preccurlyeq F' \preccurlyeq F$, \ $F''' \preccurlyeq F'' \preccurlyeq$",diag,'The sole right-hand F is at the upper F\' level; the lower-right relation ends into blank space. Four sloping or bowed signs stand without connecting lines. H\'s prose note recognizes the missing lower endpoint, but literal line equations lose the spatial arrangement.',kind='drawing or diagram',cc=True,ch=True,crop='c08_diamond',math=True)
diff('D22','Diagram upper-right worked sign',r'\deleted{\unsure{\leq|\prec}}\preceq',r'\preccurlyeq',r'\unsure{\preceq}\quad\text{with the extra thin upper stroke drawn in D1}','There is one worked relation position with two rising upper strokes. A separate complete deleted ≤ or prec is not recoverable; the final bowed sign is retained with doubt and the extra stroke is drawn.',confidence='low',kind='deletion state (struck given live or live given struck)',cc=True,ch=True,crop='c08_diamond',math=True)
diff('D23','Upper oblique marginal note, words missing in H',r'On sera amené à renforcer encore cette condition sur les contrées modérées !',r'On sera amené à \ill{} \ill{} \ill{} les contrées modérées !',r'On sera amené à renforcer encore cette condition sur les contrées modérées !','The rotated complete note supplies renforcer, encore, cette, condition and sur between à and les; no independently unreadable additional word is present.',kind='readable ink left as \\ill{}',marked='yes',ch=True,crop='c09_upper_margin')
diff('D24','Definition word and underline',r'\uuline{\unsure{contrée|contrie}}',r'contrée',r'\uuline{\unsure{contrée|contrie}}','Two complete underline strokes run below the word. Its reduced accented/dotted penultimate group remains compatible with contrée or contrie.',confidence='medium',ch=True,crop='c10_definition_words')
diff('D25','Definition: modérée underline',r'\uuline{modérée}',r'\emph{modérée}',r'\uuline{modérée}','Two distinct long rules are visible below modérée.',ch=True,crop='c10_definition_words')
diff('D26','Definition: subdivisions state',r'subdivisions',r'\add{subdivisions}',r'subdivisions','The word begins the next ordinary baseline; there is no separate raised insertion or insertion leader at it.',kind='insertion or placement',ch=True,crop='c11_definition_corrections')
diff('D27','Definition: dense d\'une group and repetition',r'\deleted{\unsure{d\'un}} \unsure{d\'une =|d\'un =}',r'\struck{\ill{}} de',r'\unsure{d\'|\deleted{d\'}}\unsure{une|un} $=$','There is one crowded word-sized group followed by two parallel repetition strokes. Its d/apostrophe beginning is worked, and the live continuation can be une or un. The scan does not establish two complete successive words, an older d\'un plus a full new d\'une.',confidence='low',kind='deletion state (struck given live or live given struck)',marked='yes',cc=True,ch=True,crop='c11_definition_corrections')
diff('D28','Definition: comparables certainty',r'comparables',r'\uncertain{comparables}',r'comparables','The unworked comparison word has clear comp, ara, bles groups and terminal stop.',marked='yes',ch=True,crop='c11_definition_corrections')
diff('D29','Cancelled Dans clause',r'\deleted{Dans le cas qui vient,}',r'\struck{Dans le cas général,}',r'\deleted{Dans le cas qui vient,}','After cas the descender q, dotted i and separate vient group remain visible under the line; final comma is present.',kind='misread word',ch=True,crop='c11_definition_corrections')
diff('D30','Cancelled on a',r'\deleted{on a}',r'',r'\deleted{on a}','Two reduced word groups sit under a horizontal cancellation immediately before the large Je line.',kind='omission',ch=True,crop='c12_initial_c5')
diff('D31','Detached points after cancelled on a',r'.',r'',fig3,'Two separate small points descend diagonally after the cancelled words. G3 preserves both without deciding colon or sentence punctuation.',kind='drawing or diagram',cc=True,ch=True,crop='c12_initial_c5')
diff('D32','Cancelled earlier C5 label',r'\deleted{\uline{C5}}',r'\struck{\ill{}}',r'\deleted{\uline{C5}}','The large C and 5, underline, and diagonal cancellation strokes are readable.',kind='readable ink left as \\ill{}',marked='yes',ch=True,crop='c12_initial_c5')
diff('D33','H placeholder after donner',r'donner aucune',r'donner \struck{\ill{}} aucune',r'donner aucune','The space after donner and before the next-line aucune contains no separate cancelled word. The cancelled C5 is left of the paragraph and accounted for separately.',kind='text not on the page',marked='yes',ch=True,crop='c12_initial_c5')
diff('D34','Ending of seul',r'seul',r'seule',r'seul','The final looped l ends in a short exit stroke, followed by a separate period; no additional e is visible.',kind='abbreviation expanded or spelling modernised',ch=True,crop='c13_ses_relations')
diff('D35','Possessive/article before relations',r'ses',r'les',r'\unsure{ses|les}','The initial is a small dense upright loop; its height and entry permit both s and l. The rest of the group does not decide between the witnesses.',confidence='low',kind='misread word',cc=True,ch=True,crop='c13_ses_relations')
diff('D36','Placement/state of avec',r'avec',r'\add{avec}',r'avec','Avec stands on the ordinary baseline following relations, with no raised placement or insertion leader.',kind='insertion or placement',ch=True,crop='c13_ses_relations')
diff('D37','Lower note first word',r'\unsure{Reporter|Rejeter}',r'\ill{}',r'Reporter','The descender has the high return of p and is followed by the reduced orter sequence; it is not a simple dotted j.',kind='readable ink left as \\ill{}',marked='yes',cc=True,ch=True,crop='c14_lower_margin')
diff('D38','Lower note C7 suffix and punctuation',r'$C7_0$',r'C7,',r'$C7_0$','A small closed oval sits at the foot of 7. No extra comma follows this group; the earlier comma after C6 is visible.',kind='misread symbol or index',ch=True,crop='c14_lower_margin',math=True)
diff('D39','Lower note ces axiomes',r'\unsure{ces|mes} axiomes',r'\ill{}',r'\unsure{ces|mes} axiomes','A short reduced ces/mes group is above the fully readable axiomes. The first tiny group remains ambiguous.',confidence='medium',kind='readable ink left as \\ill{}',marked='yes',ch=True,crop='c14_lower_margin')
diff('D40','Lower note de disjonction and underline',r'de \uline{disjonction}',r'des disjonctions',r'de \uline{disjonction}','The short first group has de without an added s; the following singular word terminates in n at the long bars and is underlined.',kind='abbreviation expanded or spelling modernised',ch=True,crop='c14_lower_margin')
diff('D41','Pair of long bars beside C5',r'',r'',fig4,'Two long nearly vertical strokes extend down beside the axiom. H mentions them only in an editorial note; neither witness renders the actual marks.',kind='drawing or diagram',cc=True,ch=True,crop='c14_lower_margin')
diff('D42','C5 abbreviation before figure G',r'\unsure{tte}',r'toute',r'tte','There are two tall t-like stems and a small final e, without an ou group.',kind='abbreviation expanded or spelling modernised',cc=True,ch=True,crop='c15_tte')
diff('D43','NB overwritten letter before equals',r'\deleted{\unsure{F}}\unsure{G|F}',r'G',r'\deleted{\unsure{F}}G','A broad outside curve and lower-right spur settle the surviving G. Inner straight F-like strokes are overwritten, but the older letter remains less secure.',confidence='medium',kind='deletion state (struck given live or live given struck)',cc=True,ch=True,crop='c16_nb_formula',math=True)
diff('D44','NB X case uncertainty',r'\unsure{X|x}',r'X',r'\unsure{X|x}','A heavy pair of diagonals crosses a curved stroke. Its scale favours X, but the written shape does not securely exclude x.',confidence='medium',ch=True,crop='c16_nb_formula',math=True)
diff('D45','NB ambient M alphabet',r'M',r'\mathcal{M}',r'M','The letter has plain peaked strokes, without a separate calligraphic entry or trailing flourish.',kind='misread symbol or index',ch=True,crop='c16_nb_formula')
# C doubts and explicit context checks: one disposition for each distinct doubtful locus, plus all notation checks.
CD=[]
def doubt(i,loc,c,reading,status,evidence,crop=None,bbox=None,source=None,refs=None):
    z={'id':i,'location':loc,'c':c,'reading':reading,'status':status,'scan_shows':evidence,'crop':None,'bbox':bbox,'bbox_image':source or whole,'context_refs':refs or []}
    if crop:
        cr=byname[crop];z.update(crop=cr['path'],bbox=cr['bbox'],bbox_image=cr['source'])
    CD.append(z)
doubt('CD01','First-line relation',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','The lower stroke is bowed downward and the upper angle is bent, distinct from the final straight ≤.','c01_opening',refs=['C_context row: first line; diamond; C5','C_context row: first line relation'])
doubt('CD02','All four diagram relation positions',r'\preceq',r'\preceq;\preceq;\unsure{\preceq};\preceq','revised','Four signs are visible. Three are uncomplicated bowed relations; the upper-right has an extra upper stroke and remains a worked single sign.','c08_diamond',refs=['C_context row: first line; diamond; C5'])
doubt('CD03','C5 relation F prime to F',r"F'\preceq F",r"F'\preceq F",'resolved','The axiom sign has a broad angular upper branch, a downward bowed lower branch and a separate bowed lower stroke.',bbox=[730,910,980,1000],source=halfb,refs=['C_context row: first line; diamond; C5'])
doubt('CD04','Diagram objects and primes',r"F''',F',F'',F",r"F''',F',F'',F",'resolved','Left has three ticks, upper one, lower two, and the right object none. The right object is level with the upper one.','c08_diamond',refs=['C_context row: middle diamond positions'])
doubt('CD05','Upper paragraph repetition sign',r'\unsure{=|même}',r'$=$','resolved','Two short parallel strokes with a left return, no letter-shaped contents.','c05_repetition_f',refs=['C_context row: repeated-word mark','C_context row: before figure F'])
doubt('CD06','C5 G, F prime, X and ssi notation check',r"G,F',X,\mathrm{ssi}",r"G,F',\unsure{X|x},\mathrm{ssi}",'revised','C5 has plain G, single-prime F and the three-letter ssi group. At the NB occurrence X has no index but its case remains uncertain. Main-letter evidence is in lower half; NB case is in c16.','c16_nb_formula',refs=['C_context row: C5 plain G F prime subscript-free X equivalence abbreviation'])
doubt('CD07','Très/trs',r'\unsure{très|trs}',r'\unsure{très|trs}','retained','Reduced internal letters and high point do not securely isolate an e and accent.','c01_opening',refs=['C_context row: second line'])
doubt('CD08','Aura',r'\unsure{aura}',r'\unsure{aura}','retained','There are visibly two small groups after n\'y, au-like then ra-like; their reduction prevents full certainty.','c01_opening',refs=['C_context row: second line after Il n\'y'])
doubt('CD09','Cancelled noun éléments/élémen',r'\deleted{\unsure{éléments|élémen}}',r'\deleted{\unsure{éléments|élémen}}','retained','Initial accent, l and later upright survive, but the ending is merged with the strike.','c02_cancelled_noun',refs=['C_context row: fourth line cancelled noun'])
doubt('CD10','En phrase',r'\unsure{en général|en position}',r'\unsure{en général|en position}','retained','Distinct en-like group and following descender-led reduced word; neither full expansion is certain.','c03_raised_condition',refs=['C_context row: after figures and its interline condition'])
doubt('CD11','Dotted abbreviation (i.e.',r'\unsure{(i.e.|liée.|lire.}',r'(i.e.','resolved','Curved opening parenthesis, dotted i, low point, e-like flourish, and a detached final point are all visible.','c04_ie_subdivisions',refs=['C_context row: after figures and its interline condition'])
doubt('CD12','Second F prime count in prose',r"\unsure{F'''|F''}",r"F'''",'resolved','Three distinct short ticks follow this occurrence.','c06_second_noun_primes',refs=['C_context row: second paragraph second subdivision'])
doubt('CD13','Deleted middle of underlined adjective',r'\deleted{\unsure{ati|atib}}',r'\deleted{\unsure{ati|atib}}','retained','Crossed and retraced central upright/dotted strokes do not decide how much of b belongs to the older layer. This is one word-sized group.','c07_worked_adjective',refs=['C_context row: underlined adjective'])
doubt('CD14','Final middle of underlined adjective',r'\unsure{ara|ati|ata}',r'\unsure{ara|ati|ata}','retained','The worked short middle between comp and bles admits all three candidates; the following parenthesis is not substituted for ink.','c07_worked_adjective',refs=['C_context row: underlined adjective','C_context row: underlined adjective and parenthesis'])
doubt('CD15','First group in cancelled clause',r'\unsure{on dit|c.à.d.}',r'\unsure{quand et|on dit|c.à.d.}','revised','Round first stroke and two tall stems also support H\'s quand et; the cancellation prevents a secure segmentation.','c07_worked_adjective',refs=['C_context row: deletion after underlined word'])
doubt('CD16','Last group in cancelled clause',r'\unsure{sub}',r'\unsure{seulement|sub}','revised','There is a long reduced s-led group with a tall final stroke, allowing seulement as well as C\'s short sub reading.','c07_worked_adjective',refs=['C_context row: deletion after underlined word'])
doubt('CD17','Definition contrée/contrie',r'\unsure{contrée|contrie}',r'\unsure{contrée|contrie}','retained','The penultimate tiny upright/dotted group is not enough to settle é versus i.','c10_definition_words',refs=['C_context row: left note and definition at right'])
doubt('CD18','Upper-note contrées',r'contrées',r'contrées','resolved','The complete rotated marginal word is readable as contrées with its plural ending. The uncertainty in the separate definition is not propagated here.','c09_upper_margin',refs=['C_context row: left note and definition at right'])
doubt('CD19','Proposed older d\'un layer',r'\deleted{\unsure{d\'un}}',r'\unsure{d\'|\deleted{d\'}}','revised','Only one crowded word-sized group is visible; separate complete old and new words cannot be recovered. Cancellation uncertainty is retained at the worked initial part.','c11_definition_corrections',refs=['C_context row: after subdivisions over older letters'])
doubt('CD20','Final d\'une/d\'un and repetition',r'\unsure{d\'une =|d\'un =}',r'\unsure{d\'|\deleted{d\'}}\unsure{une|un} $=$','revised','The final reduced continuation allows une/un. The following two-stroke mark is secure as the literal repetition sign.','c11_definition_corrections',refs=['C_context row: before F sont toujours'])
doubt('CD21','Lower-note Reporter/Rejeter',r'\unsure{Reporter|Rejeter}',r'Reporter','resolved','The long descender has a p-like upper return, with a later tall t; the complete group reads Reporter.','c14_lower_margin',refs=['C_context row: lower-left note first word'])
doubt('CD22','Lower-note ces/mes',r'\unsure{ces|mes}',r'\unsure{ces|mes}','retained','The initial stroke is densely reduced; neither c nor m is secure.','c14_lower_margin',refs=['C_context row: lower-left note above axiomes'])
doubt('CD23','C5 tte',r'\unsure{tte}',r'tte','resolved','Two tall t stems and a separate small e; no ou letters.','c15_tte',refs=['C_context row: C5 before figure G'])
doubt('CD24','NB surviving G/F',r'\unsure{G|F}',r'G','resolved','The broad rounded outside stroke and lower-right spur establish G.','c16_nb_formula',refs=['C_context row: NB letter before equals'])
doubt('CD25','NB older F',r'\deleted{\unsure{F}}',r'\deleted{\unsure{F}}','retained','Straight inner stem and bars favour an older F, but shared and overwritten strokes prevent certainty.','c16_nb_formula',refs=['C_context prior-audit revised NB'])
doubt('CD26','Upper-right diagram underlayer',r'\deleted{\unsure{\leq|\prec}}',r'\unsure{\preceq}\quad\text{plus drawn extra stroke}','revised','One sign position is retraced with an extra rising stroke. A complete older ≤ or prec is not separately readable; D1 draws the stroke without inventing an older complete sign.','c08_diamond',refs=['C_context row: upper-right comparison in diamond'])
doubt('CD27','NB X/x',r'\unsure{X|x}',r'\unsure{X|x}','retained','Two heavy diagonals are crossed over a curved stroke; case is not securely determined by shape.','c16_nb_formula',refs=['C_context row: after equals in NB'])
doubt('CD28','Singular subdivision after deux',r'deux subdivision',r'deux subdivision','resolved','No distinct final plural s follows the n-like terminal sweep.','c06_second_noun_primes',refs=['C_context row: after On dit que deux'])
doubt('CD29','Quoted adjective versus lower comparables',r'``compatibles\'\'; comparables',r'``compatibles\'\'; comparables','resolved','The parenthetic quoted word is clear, and the lower unworked comparables is independently clear. Neither settles the overwritten earlier adjective.',bbox=[270,950,1640,1560],source=whole,refs=['C_context row: underlined adjective and parenthesis'])
doubt('CD30','Lower-note C7 tiny oval',r'$C7_0$',r'$C7_0$','resolved','The tiny closed oval is at the foot of 7. This decision uses this page alone.','c14_lower_margin',refs=['C_context prior-audit revised C7'])
doubt('CD31','Property paragraph order signs',r'\preceq;\leq',r'\preceq;\leq','resolved','The sign by particulière has bent strokes; the final sign after avec has straight angled branches and a straight lower bar.',bbox=[1340,560,1620,810],source=halfb,refs=['C_context prior-audit order signs'])
R=[]
def remain(loc,reading,alts,conf,reason):R.append({'location':loc,'reading':reading,'alternatives':alts,'confidence':conf,'reason':reason})
remain('Opening reduced très/trs',r'\unsure{très|trs}',['très','trs'],'medium','The independent e and the nature of the high point are not securely visible.')
remain('Verb after n\'y',r'\unsure{aura}',['aura'],'medium','Two reduced groups survive, but individual internal letters are not fully separable.')
remain('Cancelled noun after deux',r'\deleted{\unsure{éléments|élémen}}',['éléments','élémen'],'medium','Strike obscures the ending.')
remain('Raised order sign state',r'\unsure{\deleted{\preceq}|\preceq}',[r'\deleted{\preceq}',r'\preceq'],'low','Heavy extra horizontals may be cancellation or retracing; trailing dash is secure.')
remain('Phrase after figures',r'\unsure{en général|en position}',['en général','en position'],'low','The long second word is severely reduced.')
remain('Underlined adjective older central layer',r'\deleted{\unsure{ati|atib}}',['ati','atib'],'low','Worked central strokes do not separate the layers.')
remain('Underlined adjective final central layer',r'\unsure{ara|ati|ata}',['ara','ati','ata'],'low','One overwritten word; visible middle does not decide final letters.')
remain('Cancelled clause first group',r'\unsure{quand et|on dit|c.à.d.}',['quand et','on dit','c.à.d.'],'low','Long cancellation hides the short internal strokes and word divisions.')
remain('Cancelled clause final group',r'\unsure{seulement|sub}',['seulement','sub'],'low','Reduced s-led group and a tall final stroke survive.')
remain('Upper-right diagram relation',r'\unsure{\preceq}',[r'\preceq retraced',r'\deleted{\prec} under \preceq',r'\deleted{\leq} under \preceq'],'low','The extra upper stroke is drawn; no complete separately legible older glyph can be assigned.')
remain('Definition contrée/contrie',r'\unsure{contrée|contrie}',['contrée','contrie'],'medium','Reduced penultimate mark may be an accented e or dotted i.')
remain('Definition worked initial d\'',r'\unsure{d\'|\deleted{d\'}}',[r"d'",r"\deleted{d'}"],'low','The initial d/apostrophe part is overwritten and possibly cancelled; no separate old word is asserted.')
remain('Definition continuation une/un',r'\unsure{une|un}',['une','un'],'medium','Final e cannot be securely separated from the exit stroke.')
remain('Before relations',r'\unsure{ses|les}',['ses','les'],'low','Small initial upright loop is compatible with both readings.')
remain('Lower-note ces/mes',r'\unsure{ces|mes}',['ces','mes'],'medium','First tiny character is too reduced.')
remain('NB overwritten older letter',r'\deleted{\unsure{F}}',['F'],'medium','Inner straight bars favour F but share ink with the surviving G.')
remain('NB X case',r'\unsure{X|x}',['X','x'],'medium','Crossed shape and scale do not settle case.')
I=[]
def inv(n,kind,pos,first):I.append({'element':n,'kind':kind,'position':pos,'first_words_or_objects':first,'sheet_kind':'text','hand':'his hand','transcribed':'yes'})
inv('I01','text','top centre','69')
inv('I02','text','upper main paragraph','J\'en viens à la rel d\'ordre')
inv('I03','deletion','upper paragraph after deux','éléments/élémen')
inv('I04','insertion','above figures','F\', F\'\' and the raised relation/dash')
inv('I05','deletion','raised relation to the right of F letters','possibly cancelled preceq; alternative state retained')
inv('I06','drawing','below raised relation','G1 curved oblique arm, no arrowhead')
inv('I07','text','second main paragraph','On dit que deux subdivision')
inv('I08','deletion','inside underlined adjective','ati/atib older central strokes')
inv('I09','deletion','after worked adjective','quand et/on dit/c.à.d. que seulement/sub')
inv('I10','diagram','left middle beside definition','D1: F triple prime, F prime, F double prime, F; four bowed signs; extra upper stroke')
inv('I11','margin note','slanted left middle','On sera amené à renforcer encore')
inv('I12','text','middle right and following full lines','On dit que la contrée est modérée')
inv('I13','deletion','definition after subdivisions','possibly cancelled worked d\' within one group')
inv('I14','deletion','definition end','Dans le cas qui vient,')
inv('I15','deletion','next line left','on a')
inv('I16','drawing','after cancelled on a','G3 two detached points')
inv('I17','deletion','left of property paragraph','underlined C5 with diagonal cancellation')
inv('I18','text','lower main paragraph','Je ne saurais donner aucune propriété')
inv('I19','deletion','before seul','tout')
inv('I20','margin note','slanted lower left','Reporter après C6, C7 subscript 0')
inv('I21','drawing','left of live axiom C5','G4 pair of long nearly vertical bars')
inv('I22','text','bottom main block','C5 Soit F prime preceq F; NB Il suffit')
inv('I23','deletion','NB condition before equals','older F-like strokes below surviving G')
report={'reader':'R2','cote':'156-4','scan':'70','brief_version':'v06','started_utc':'2026-11-20T11:00:52Z','finished_utc':None,'image_views':[whole,halfa,halfb],'reading_file':str(out/'reading.tex'),'differences':D,'c_doubts':CD,'inventory':I,'remaining_doubts':R,'notation':[
{'sign':'subdivision relation','latex':r'\preceq','appearance':'Bent upper angle with bowed lower stroke; upper-right diagram occurrence overworked.','location':'opening, diagram, property paragraph, C5','alternatives':[r'\leqslant only for the rejected opening alternative; upper-right underlayer unresolved']},
{'sign':'ordinary order','latex':r'\leq','appearance':'Straight two-branch angle and lower bar.','location':'after avec in property paragraph','alternatives':[]},
{'sign':'prime counts','latex':r"F',F'',F'''",'appearance':'One, two or three short upright ticks.','location':'raised condition, second paragraph, diagram, C5','alternatives':[]},
{'sign':'literal repetition sign','latex':'=','appearance':'Two short parallel strokes with left joining return.','location':'before figure F; before F in definition','alternatives':[]},
{'sign':'ambient M','latex':'M','appearance':'Plain pair of peaked strokes.','location':'NB condition','alternatives':[]},
{'sign':'NB variable','latex':r'\unsure{X|x}','appearance':'Heavy crossed diagonals, one curved/retraced.','location':'NB after equals','alternatives':['X','x']},
{'sign':'C7 suffix','latex':r'C7_0','appearance':'Small closed oval at foot of 7.','location':'lower oblique note','alternatives':[]},
{'sign':'detached points','latex':fig3,'appearance':'Two small points descending diagonally.','location':'after cancelled on a','alternatives':['unassigned punctuation function']}
], 'abbreviations':[{'form':'rel','expansion':'relation'},{'form':'Sup','expansion':'supremum'},{'form':'inf','expansion':'infimum'},{'form':'i.e.','expansion':'id est'},{'form':'tte','expansion':'toute'},{'form':'ssi','expansion':'si et seulement si'},{'form':'NB','expansion':'nota bene'}],
'notes':{'summary':'The page introduces the subdivision relation, names a common-subdivision condition with a worked adjective, defines a modérée contrée, and states C5 on disjointness. Both oblique notes, the diagram, all visible corrections, and the otherwise omitted marks are retained.','math_reading_decisions':'No theorem was proved or independently validated. Comparison of the bent relation with the straight sign after avec triggered a local shape check. The prose prime count was read as three ticks despite the two ticks at the lower diagram node. The diagram was kept with its single right-hand F at the upper level; a common lower endpoint was not supplied from expected mathematics.','author_checks':'The in-page note says Reporter après C6, C7_0 ces/mes axiomes de disjonction. The other note proposes strengthening the condition for contrées modérées. These are manuscript directions, not work performed by this reader. No outside page was consulted.','title_dates_pagination':'Manuscript page number 69; scan 70. No title or date. One cancelled C5 label precedes the surviving underlined C5.'},
'check_events':[],'crops':manifest,'workflow_feedback':'The single-crop rule was workable. For crowded corrections, the report distinguishes one word-sized group from a confidently recoverable separate deleted layer. The diagram convention should explicitly permit literal node positions even when the mathematical endpoint arrangement is incomplete.'}
def fix_apostrophes(obj):
    if isinstance(obj,str): return obj.replace("\\'", "'")
    if isinstance(obj,list): return [fix_apostrophes(x) for x in obj]
    if isinstance(obj,dict): return {k:fix_apostrophes(v) for k,v in obj.items()}
    return obj
report=fix_apostrophes(report)
c_source=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_070/C.tex').read_text()
start=c_source.index('\\diagram{')
end=c_source.index('\\end{tikzcd}}',start)+len('\\end{tikzcd}}')
next(d for d in report['differences'] if d['id']=='D21')['c']=c_source[start:end]
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(out/'diagram_fragments.json').write_text(json.dumps({'G1':fig1,'D1':diag,'G3':fig3,'G4':fig4},ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex and report.json:',len(D),'differences;',len(CD),'C dispositions;',len(R),'remaining doubts;',len(I),'inventory items.')
