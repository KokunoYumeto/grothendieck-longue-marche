from pathlib import Path
import json,re,datetime
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R1')
pkt=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_072')
C=(pkt/'C.tex').read_text(); H=(pkt/'H.tex').read_text(); R=(out/'reading.tex').read_text()
crops=json.loads((out/'crop_metadata.json').read_text())
whole=crops[0]['source']; half_a=whole.replace('.jpg','_a.jpg'); half_b=whole.replace('.jpg','_b.jpg')
def ev(n=None,bbox=None,source=None):
 if n:
  cr=crops[n-1]; return dict(crop=cr['path'],bbox=bbox or cr['bbox'],bbox_image=cr['source'],source=cr['source'])
 return dict(crop=None,bbox=bbox,bbox_image=source,source=source)
D=[]
def diff(loc,c,h,r,ink,kind='other',conf='high',marked='no',cc=True,ch=True,math=False,n=None,bbox=None,source=None,**extra):
 D.append(dict(id=f'D{len(D)+1:03}',location=loc,c=c,h=h,reading=r,scan_shows=ink,confidence=conf,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,math_consequential=math,**ev(n,bbox,source),**extra))
# Opening, definition and a.
diff('Opening, first word','Pour','Par','Pour','The low group after P includes the ou run.',kind='misread word',cc=False,bbox=[275,65,390,165],source=half_a)
diff('Opening, axioms phrase','les axiomes vont passer',r'les axiomes \ill{} passent','les axiomes vont passer','vont is a separate group; passer ends in the low er run.',kind='readable ink left as \\ill{}',marked='yes',cc=False,bbox=[515,180,1135,268],source=half_a)
diff('Opening, after quand',r'quand $=\unsure{=}$','quand même',r'quand $= =$','Two separate pairs of horizontal strokes; the second lower stroke has a left hook.',kind='misread symbol or index',n=1)
diff('Opening, last words',r'\unsure{en forme|en jeu}','en forme','en forme','A tall crossed descending f precedes the low orme run.',kind='other',ch=False,n=2)
diff('Raised bracket at upper right, linked to sous-contrée',r'\inserted{[\uline{pleine}]}',r'[\ill{}]',r'\inserted{[\uline{pleine}]}','pleine is bracketed and underlined above sous-contrée; the hook fixes its attachment.',kind='readable ink left as \\ill{}',marked='yes',cc=False,n=4,scope='Decipherment and relocation of H’s opening-paragraph bracketed placeholder; not a second omission of pleine.')
diff('Long hooked insertion connector for pleine','','','% R1-FIG-DEFINITION','One continuous hook runs beneath the raised word and bends to the end of sous-contrée.',kind='drawing or diagram',n=4,scope='Graphic stroke only; word/attachment are in D005.')
diff('Definition, capital before equals',r'\unsure{\deleted{\mathcal F}\mathcal C|\mathscr C|\mathbb C}',r'\mathcal{C}',r'\unsure{\rlap{\deleted{\mathcal F}}\mathcal C|\mathcal C|\mathscr C|\mathbb C}','An outer C-shaped curve and inner F-like stem/bar occupy ONE glyph position.',kind='deletion state (struck given live or live given struck)',conf='low',n=3)
diff('Definition, family F inside tuple',r'\mathcal F',r'\mathfrak{F}',r'\mathcal F','The upper stroke curves into the stem; no Gothic letter construction.',kind='misread symbol or index',cc=False,n=3,bbox=[1010,555,1082,649])
diff('Definition, second order',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','Bent upper part and bowed lower stroke differ from the straight preceding ≤.',kind='misread symbol or index',ch=False,math=True,n=3,bbox=[1195,555,1287,643])
diff('Definition, tout','tout',r'\struck{tout}',r'\unsure{\deleted{tout}|tout}','A long stroke crosses the latter letters; cancellation versus a broad t stroke is unresolved.',kind='deletion state (struck given live or live given struck)',conf='low',n=5,bbox=[1438,554,1604,655])
diff('Definition, verb after qui',r'\unsure{satisfait|satisfont}','satisfait',r'\unsure{satisfait|satisfont}','A closed low loop after f is followed by a reduced run and t; ai/on not separated securely.',kind='other',conf='medium',cc=False,n=5,bbox=[908,653,1212,781])
diff('a, after sup',r'\unsure{quelc.}','quelc.','quelc.','The abbreviated ending and detached stop are visible.',ch=False,n=6,bbox=[1490,775,1650,870])
diff('a, s’en correspondence phrase',r"s'en \unsure{correspond|correspondant}","s'en correspond","s'en correspond",'corre-/spond spans two lines and ends in d immediately before a comma, not -ant.',ch=False,n=6)
diff('a, inserted mapping sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mapsto',r'\mathrel{\vdash\joinrel\dashv}','A short upright caps each end of the horizontal stroke; no sloping head.',kind='misread symbol or index',n=7,bbox=[850,920,925,961])
diff('a, inserted mapping alphabets',r"\mathcal F'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}\mathcal F'\cap M",r"\mathfrak{F}' \mapsto \mathfrak{F}' \cap \mathcal{M}",r"\mathcal F'\mathrel{\vdash\joinrel\dashv}\mathcal F'\cap M",'Both F forms have curved tops; M is the plain two-peaked letter.',kind='misread symbol or index',cc=False,n=7,scope='Alphabet only; mapping sign is D014.')
diff('a, raised M prime and following baseline M',r"\inserted{$M'$} de $M$",r"\add{$\mathcal{M}'$} de $\mathcal{M}$",r"\inserted{$M'$} de $M$",'Both M letters are plain; the first is raised with a separate prime.',kind='misread symbol or index',cc=False,n=7,bbox=[1320,905,1550,1022])
diff('a, long leader under inserted mapping','','','% R1-FIG-A','A long rule below the raised phrase curls down before aux.',kind='drawing or diagram',n=7,scope='Long leader only.')
diff('a, short M-prime leader','','','% R1-FIG-A','A separate rising curved arm is attached to the gap before de M.',kind='drawing or diagram',n=7,bbox=[1360,925,1465,993],scope='Short leader only.')
diff('a, M-prime mapping endpoint',r'\unsure{\mathrel{\mapstochar\relbar}|\mapsto}',r'\mapsto',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mathrel{\mapstochar\relbar}|\mapsto}','Left cap is clear; the thick short right endpoint can be a cap, dark dash end, or compressed head.',kind='misread symbol or index',conf='low',n=7,bbox=[755,1035,863,1085])
c_formula=r"M'\unsure{\mathrel{\mapstochar\relbar}|\mapsto}\mathcal F'=\{F\in\mathcal F\mid\overline F\subset M'\}"
h_formula=r"\mathcal{M}' \mapsto \mathfrak{F}' = \lbrace F \in \mathfrak{F} \mid F \subset \mathcal{M}' \rbrace"
r_formula=r"M'\unsure{\mathrel{\vdash\joinrel\dashv}|\mathrel{\mapstochar\relbar}|\mapsto}\mathcal F'=\{F\in\mathcal F\mid\overline F\subset M'\}"
diff('a, baseline mapping alphabets',c_formula,h_formula,r_formula,'Both M forms are plain, both family F forms curved, and the individual F forms plain.',kind='misread symbol or index',cc=False,n=7,scope='Alphabet only; sign and roof are D019 and D021.')
diff('a, individual F in subset condition',r'\overline F','F',r'\overline F','A detached roof lies above that individual F.',kind='misread symbol or index',cc=False,math=True,n=7,bbox=[1212,1013,1280,1075])
cmargin=next(s for s in C.splitlines() if s.startswith(r'\margin{Je ne sais'))
hmargin=next(s for s in H.splitlines() if s.startswith(r'\marginal{il faudra'))
rmargin=next(s for s in R.splitlines() if s.startswith(r'\margin{Je ne sais'))
diff('Slanted left question, entire nonoverlapping H passage',cmargin,hmargin,rmargin,'Je ne sais, prendre, sup quelconques, stricte and de are legible; compressed condition, crossed et and the incompletely framed final parenthesis remain doubtful.',kind='readable ink left as \\ill{}',conf='medium',marked='yes',n=8,framing_failure='The final word/closing parenthesis meets the crop right edge near whole x≈550,y≈1000–1070; not used to establish absence.',scope='Accounts for all three unreadable placeholders in this H marginal passage; local C doubts are dispositions, not repeated H omissions.')
# b correction.
diff('b, after envisagées','envisagées','envisagées','envisagées,','A detached comma follows the complete final s near the sheet edge.',kind='omission',n=17,bbox=[1440,1210,1666,1283])
diff('b, ambient M pair',r"$M'$ de $M$",r"$\mathcal{M}'$ de $\mathcal{M}$",r"$M'$ de $M$",'Both capitals have plain peaked M outlines, with one prime on the first.',kind='misread symbol or index',cc=False,n=9,bbox=[548,1327,817,1405])
diff('b, extra mark after M',r'\unsure{\}|?}','','% R1-MARK-AFTER-M','The vertical curling mark has a small crossing at its head and precedes a separate comma.',kind='drawing or diagram',conf='low',n=9,bbox=[800,1318,888,1410])
diff('b, opening of cancelled clause',r'\unsure{à savoir|savoir} :',r'\ill{}',r'\unsure{savoir|à savoir} :','A savoir-like group lies under the rule; no distinct preceding à is secure.',kind='readable ink left as \\ill{}',conf='low',marked='yes',n=9,bbox=[930,1310,1220,1381])
diff('b, end of cancelled clause',r'si $X\in$',r'si $X \in F$',r'si $X\in$','The crossed line ends after the membership sign, with blank space where H adds F.',kind='text not on the page',cc=False,math=True,n=9,bbox=[1230,1295,1505,1380])
diff('b, raised replacement',r'\inserted{qu\'on va formuler}'.replace("\\'","'"),r'\ill{}',r"\inserted{qu'on va formuler}",'The complete raised line reads qu’on va formuler above the cancelled clause.',kind='readable ink left as \\ill{}',marked='yes',cc=False,n=9,bbox=[935,1265,1515,1350])
diff('b, placement of cancelled clause relative to plus bas',r"\deleted{\unsure{à savoir|savoir} : si $X\in$} \inserted{qu'on va formuler} plus bas)",r'\ill{} plus bas) \struck{\ill{} si $X \in F$}','% R1-FIG-B-CORRECTION','The replacement is above the deletion, both before the next physical line plus bas).',kind='insertion or placement',marked='yes',cc=False,n=9,scope='Placement only; lettering is covered by D026–D028.')
# Marginal c.
diff('Above marginal c, instruction',r'\unsure{reporter|rajouter}','','reporter','The instruction has a p descender and later t, not a dotted j.',kind='omission',n=10,bbox=[1142,1376,1360,1440])
diff('Marginal c, subd ending',r'\unsure{fixé|fixée}','fixée',r'\unsure{fixé|fixée}','An acute is visible, but a possible final e merges with the preceding group.',conf='medium',cc=False,n=10,bbox=[1175,1400,1268,1460])
diff('Marginal c, G application link',r'G\mathrel{\vdash\joinrel\dashv}G\' '.strip().replace("\\'","'"),r"G \mapsto G'",r"G\mathrel{\vdash\joinrel\dashv}G'",'The horizontal line has two upright caps and no angled arrowhead.',kind='misread symbol or index',cc=False,n=10,bbox=[1515,1392,1662,1450])
cc_initial=r"\deleted{\unsure{F}}sous-fig. de $F$ $\unsure{-|\longrightarrow}$ sous-fig. de $F'$ \deleted{\unsure{s}}"
hc_initial=r"sous-fig. de $F$ $\to$ sous-fig. de $F'$,"
diff('Marginal c, worked initial and supposed terminal deletion',cc_initial,hc_initial,r'\unsure{\rlap{\deleted{F}}S|S|s}ous-fig.','One dense initial position contains the F/S-like work and its lower residual strokes; no separate s follows the final F′.',kind='deletion state (struck given live or live given struck)',conf='low',n=10,scope='Worked initial/letter grouping only, including C’s misplaced separate s; headless link and comma are separate rows.')
diff('Marginal c, link between sous-figure phrases',r'\unsure{-|\longrightarrow}',r'\to','% R1-C-HEADLESS-LINK','A horizontal stroke ends with a very short upright tick; no arrowhead is visible.',kind='misread symbol or index',n=10,bbox=[1325,1450,1406,1493])
diff('Marginal c, verb before aux Sup','commute',r'\ill{}','commute','The low co/mm/u run rises to t before the final e.',kind='readable ink left as \\ill{}',marked='yes',cc=False,n=10,bbox=[1090,1490,1330,1555])
diff('Marginal c, last abbreviation',r'\unsure{i.e.}','i.e.','i.e.','Dotted i, a separate low stop, looped e and terminal stop are all present.',ch=False,n=10,bbox=[1080,1580,1170,1630])
diff('Marginal c, pointer','','','% R1-FIG-MARGINAL-C','The oblique pointer descends leftward and has a short return at its endpoint.',kind='drawing or diagram',marked='yes',n=10,scope='Pointer only; H notes it editorially, C mentions it in a comment but neither draws it.')
diff('Marginal c, punctuation after application G prime',r"G'$,",r"G'$,",r"G'$",'No detached comma follows the application’s final prime before the sheet edge.',kind='text not on the page',n=10,bbox=[1610,1390,1670,1460])
diff('Marginal c, punctuation after final F prime',r"$F'$",r"$F'$,",r"$F'$",'There is no detached comma after the final phrase’s F′.',kind='text not on the page',cc=False,n=10,bbox=[1600,1440,1670,1510])
# C6 and its margins.
cm_sym=r'\margin{symétrique en $\leq,\preceq$}'
h_sym=r'\ill{} symétrie \ill{} $\leq$, $\preccurlyeq$ \ill{}'
diff('C6, diagonal symmetry note',cm_sym,h_sym,r'sym\unsure{e|é}trique en $\leq,\preceq$','The first word continues through -trique; en is below it; an acute over the first e is not secure. No extra words flank the phrase.',kind='readable ink left as \\ill{}',conf='medium',marked='yes',n=14,scope='All three H placeholders around the symmetry phrase: the middle is en, the two flanking placeholders lack separate ink; lower sur note is handled separately.')
c_diagrams=re.findall(r'\\diagram\{[\s\S]*?\\end\{tikzcd\}\}',C)
h_first=r"$F' \preccurlyeq F$, $G \leq F$ dans $\mathfrak{F}$."
diff('C6, first diagram layout and editorial separators',c_diagrams[0],h_first,'% R1-DIAGRAM-FIRST','F′ is left of F; G lies directly below F with a downward-facing straight order. The scan has no prose separator comma or closing period.',kind='drawing or diagram',cc=False,n=11,scope='Geometry and separators only; qualifier/alphabet are D042.')
diff('C6, qualifier and family letter to right of first diagram',r'\text{\unsure{de|dans|ds}}~\mathcal F',r'dans $\mathfrak{F}$',r'\text{\unsure{de|dans|ds}}~\mathcal F','The d has only a low continuation; de/dans/ds remains open. The separate family F has a looped cap.',kind='misread word',conf='low',cc=False,n=11,bbox=[1240,1660,1535,1795])
diff('C6, detached small points','','','% R1-DETACHED-POINTS','Two offset points stand left of the first diagram; a third small point lies below the diagonal order note near the rule.',kind='drawing or diagram',n=11,evidence_additional=[ev(14)],scope='Small points only, no inferred punctuation role.')
diff('C6, long left rule','','','% R1-FIG-C6','One long slightly bent vertical rule crosses the diagonal note and continues beside part a.',kind='drawing or diagram',marked='yes',n=14,scope='Rule only; its full extent was seen in half b.',evidence_additional=[ev(None,[235,525,280,1047],half_b)])
diff('C6, circled labels a and c',r'\textcircled{a}',r'(a)',r'\textcircled{a}','Both a and c are enclosed by circles; H prints parenthesis labels and describes the circles in a note.',kind='drawing or diagram',marked='yes',cc=False,bbox=[250,800,309,884],source=half_b,evidence_additional=[ev(10,[1380,1349,1435,1410])],additional_witness_snippets={'c':r'\textcircled{c}','h':r'(c)','reading':r'\textcircled{c}'})
diff('C6 a, family letter after H membership',r'H\in\mathcal F',r'H \in \mathfrak{F}',r'H\in\mathcal F','H has two uprights; the following family F has a prominent upper loop.',kind='misread symbol or index',cc=False,n=12,bbox=[1235,1865,1486,1955])
diff('C6 a, word and punctuation after family F',r'\unsure{avec|ou}',r'\ill{} :',r'\unsure{ou|avec}','The opening is o-like with a low following run; ou is preferred, avec remains possible. No colon is visible.',kind='readable ink left as \\ill{}',conf='low',marked='yes',n=12,bbox=[1490,1860,1630,1970])
h_square=r"\[\n  F' \preccurlyeq F , \quad G' \preccurlyeq G , \qquad G' \leq F' , \quad G \leq F\n\]".replace('\\n','\n')
diff('C6, square diagram',c_diagrams[1],h_square,'% R1-DIAGRAM-SQUARE','The four nodes form a square; both downward straight signs have their detached bar to the right.',kind='drawing or diagram',marked='yes',cc=False,bbox=[650,920,930,1140],source=half_b,scope='Layout and separator punctuation only; H/G′ mismatch is retained, not repaired.')
diff('Right note b, label placement',r'et \textcircled{b}',r'(b) et',r'et \textcircled{b}','et precedes the raised circled b; les continues to its right.',kind='insertion or placement',marked='yes',cc=False,n=13,bbox=[1170,1948,1355,2055])
diff('Right note b, first strates-like noun',r'\unsure{strates|str.tes|arêtes}','strates',r'\unsure{str.tes|strates}','Initial st and r are visible; a detached medial dot-like mark favours the contraction str.tes. arêtes lacks the visible initial strokes.',kind='abbreviation expanded or spelling modernised',conf='medium',math=True,n=13,bbox=[1360,1970,1550,2055])
diff('Right note b, worked initial of second noun',r'\deleted{\unsure{S}} \unsure{strates|str.tes|arêtes}','strates',r'\unsure{\deleted{S}|S|s}tr\unsure{a|.}tes','The crossed S/s and following tr…tes occupy one word position; there is no separate additional complete initial s.',kind='deletion state (struck given live or live given struck)',conf='low',math=True,n=13,bbox=[1490,2010,1657,2102])
diff('Right note b, telles',r'\unsure{tel|\deleted{tel}}les','telles','telles','The long horizontal is the t bar; all letters continue as one live word without a second cancellation stroke.',kind='deletion state (struck given live or live given struck)',ch=False,n=13,bbox=[1412,2075,1548,2148])
diff('Right note b, final G and low tails',r'\unsure{G|G_m|G_n}','G',r'\unsure{G_n|G_m|G}','Two close low downstrokes follow the G; n is preferred, m or a retraced bare G remain possible.',kind='misread symbol or index',conf='low',math=True,n=13,bbox=[1347,2128,1415,2181])
diff('Right note b, smaller continuation',r'Ce complément \unsure{servira} plus bas','','Ce compl\\unsure{é|\\.{e}}ment \\unsure{servira} plus bas','Ce and plus bas are clear; the accent over the e is point-like and servira has reduced low strokes. This is a separate smaller continuation, not complètement.',kind='omission',conf='medium',marked='yes',n=13,bbox=[1210,2165,1635,2245],h_editorial_excerpt=r'« \ill{} complètement \ill{} »',scope='The whole continuation is absent from H transcription; its two editorial unreadable placeholders are accounted here, not counted again as separate omissions.')
diff('Right note b, double rule and lower crossing','','','% R1-C6-B-NOTE','Two parallel vertical rules stand left of b, joined/crossed by short darker strokes near their feet.',kind='drawing or diagram',marked='yes',n=13,bbox=[1150,2000,1205,2198],scope='Rules only; H mentions them editorially.')
# Final body and lower margin.
diff('Final body, first G-prime-like capital',r"$G'$",r"$G'$",r"$\unsure{G|\rlap{\deleted{F}}G|E}'$",'A looped outside and straight internal bars coexist in one capital position; bare G, an F-under-G overprint, or E remain possible.',kind='deletion state (struck given live or live given struck)',conf='low',math=True,n=15,bbox=[832,2240,919,2310])
diff('Final body, both subd abbreviation stops',r'\uline{subd}',r'subd.',r'\uline{subd}','Neither subd occurrence has a secure detached stop after d.',kind='text not on the page',cc=False,n=15,scope='Stops only; both local occurrences checked in crop 15.',additional_witness_snippets={'c':'par la subd','h':'par la subd.','reading':'par la subd'})
diff('Final body, underline extent',r'\uline{subd} \uline{de} $G$ induite',r'\emph{subd.\ de $G$ induite}',r'\uline{subd} \uline{de} $G$ induite','Two separate underlines lie under subd and de; neither G nor induite is underlined.',kind='other',cc=False,n=15,scope='Underlining only, abbreviation stops are D057.')
diff('Final body, conjunction before que','ou que',r'\ill{} que','ou que','Two low letter groups read ou, with no accent above them.',kind='readable ink left as \\ill{}',marked='yes',cc=False,n=15,bbox=[1040,2295,1168,2343])
diff('Final body, cancelled ending',r'\deleted{\unsure{sous-fig}}',r'\struck{sous-fig.}',r'\deleted{\unsure{sous-fig|sous-fig.}}','sous-fig is legible under the single crossing; a terminal point cannot be separated securely.',kind='other',conf='medium',n=15,bbox=[1478,2270,1667,2348])
diff('Lower-left sur note, placement',r'\margin{sur la sous-figure $G$ de $F$}',r'sur la sous-figure $G$ de $F$',r'\margin{sur la sous-figure $\unsure{\rlap{\deleted{F}}G|G|E}$ de $F$}','The sur note is a separate diagonal block beside the final body, below the earlier symmetry note.',kind='insertion or placement',cc=False,n=16,scope='Placement only; the local capital state is D062.')
diff('Lower-left sur note, worked G-like capital','G','G',r'\unsure{\rlap{\deleted{F}}G|G|E}','An inner F-like stem/top/middle bar lies inside the G-like outer curve at one glyph position.',kind='deletion state (struck given live or live given struck)',conf='low',math=True,n=16,bbox=[77,2280,143,2345])
# One disposition for EACH of C's thirty explicit unsure occurrences.
CD=[]
def doubt(loc,c,r,status,ink,n,**extra):
 CD.append(dict(id=f'CD{len(CD)+1:02}',location=loc,c=c,reading=r,status=status,scan_shows=ink,**ev(n),**extra))
doubt('Opening, second repetition mark',r'\unsure{=}','=','resolved','Both horizontal components are visible, with a hooked left foot.',1)
doubt('Opening, last two words',r'\unsure{en forme|en jeu}','en forme','resolved','Tall crossed f and following low orme run.',2)
doubt('Definition, first capital',r'\unsure{\deleted{\mathcal F}\mathcal C|\mathscr C|\mathbb C}',r'\unsure{\rlap{\deleted{\mathcal F}}\mathcal C|\mathcal C|\mathscr C|\mathbb C}','revised','One worked glyph position; inner F-like stem/bar and outer C curve.',3)
doubt('Definition, second order',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','Bowed lower stroke, unlike the straight preceding order.',3)
doubt('Definition, verb',r'\unsure{satisfait|satisfont}',r'\unsure{satisfait|satisfont}','retained','The closed low group and reduced following run do not decide ai/on.',5)
doubt('a, abbreviation after sup',r'\unsure{quelc.}','quelc.','resolved','Letters and final detached stop visible.',6)
doubt('a, correspondence wording',r'\unsure{correspond|correspondant}','correspond','resolved','The split word ends with d then comma, no -ant.',6)
doubt('a, first mapping sign',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mapsto}',r'\mathrel{\vdash\joinrel\dashv}','resolved','Both ends capped; no arrowhead.',7)
doubt('a, second mapping sign',r'\unsure{\mathrel{\mapstochar\relbar}|\mapsto}',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mathrel{\mapstochar\relbar}|\mapsto}','revised','The dark right endpoint may be a short cap; a head remains less certain.',7)
doubt('Slanted question, first parenthesis',r'\unsure{(condition stricte)|(condition stricts)}',r'(\unsure{condition} stricte)','revised','stricte is readable; the preceding condition group is compressed.',8)
doubt('Slanted question, cancelled et',r'\unsure{et}',r'\deleted{\unsure{et}}','retained','Small crossed group remains compatible with et.',8)
doubt('Slanted question, after ou bien',r'\unsure{de|des}','de','resolved','The short loop and exit lack the separate final s of the earlier des.',8)
doubt('Slanted question, final parenthesis',r'\unsure{(condition large)|(condition lge)}',r'\unsure{(condition large)|(condition lge)}','retained','The final letters/closing parenthesis are incompletely framed by the one crop; no absence is inferred.',8,missing_continuation_approx_bbox=[550,970,660,1100],missing_continuation_bbox_image=whole)
doubt('b, mark after M',r'\unsure{\}|?}',r'\unsure{\}}','revised','Curled vertical with crossed head; drawing retains the crossing, identity unresolved.',9,figure_reference='% R1-MARK-AFTER-M')
doubt('b, cancelled opening',r'\unsure{à savoir|savoir}',r'\unsure{savoir|à savoir}','revised','A savoir-like group is visible; no distinct initial à can be separated.',9)
doubt('Marginal c, instruction',r'\unsure{reporter|rajouter}','reporter','resolved','p descender and later t support reporter.',10)
doubt('Marginal c, fixé ending',r'\unsure{fixé|fixée}',r'\unsure{fixé|fixée}','retained','Acute visible; final e may be merged.',10)
doubt('Marginal c, purported deleted F',r'\unsure{F}',r'\unsure{\rlap{\deleted{F}}S|S|s}ous-fig.','revised','F/S-like strokes occupy the same initial position; no separate preceding word/letter is asserted.',10)
doubt('Marginal c, phrase-link',r'\unsure{-|\longrightarrow}','% R1-C-HEADLESS-LINK','resolved','The headless horizontal stroke has a tiny raised right endpoint.',10)
doubt('Marginal c, purported deleted terminal s',r'\unsure{s}','% R1-FIG-MARGINAL-C','revised','No s follows F′. Lower residual strokes are part of the one worked initial at the left.',10)
doubt('Marginal c, last abbreviation',r'\unsure{i.e.}','i.e.','resolved','i with its dot, low period, looped e and final point are present.',10)
doubt('First C6 diagram, qualifier',r'\unsure{de|dans|ds}',r'\unsure{de|dans|ds}','retained','d followed by one reduced low run does not decide the ending.',11)
doubt('C6 a, final word',r'\unsure{avec|ou}',r'\unsure{ou|avec}','revised','Tiny o-like group and low following strokes favour ou; avec remains possible.',12)
doubt('Right b note, first noun',r'\unsure{strates|str.tes|arêtes}',r'\unsure{str.tes|strates}','revised','st/r beginning is secure; a point-like medial component favours contraction.',13)
doubt('Right b note, cancelled S',r'\unsure{S}',r'\unsure{\deleted{S}|S|s}','revised','One crossed initial position, not an extra S before a second complete initial.',13)
doubt('Right b note, second noun',r'\unsure{strates|str.tes|arêtes}',r'\unsure{\deleted{S}|S|s}tr\unsure{a|.}tes','revised','The following tr…tes is tied to the worked initial; the medial small form can be a or point.',13)
doubt('Right b note, tel cancellation state',r'\unsure{tel|\deleted{tel}}','telles','resolved','A long t bar accounts for the horizontal touch; the word is live.',13)
doubt('Right b note, G tail',r'\unsure{G|G_m|G_n}',r'\unsure{G_n|G_m|G}','revised','Two low downstrokes favour n while retaining m or a retraced G.',13)
doubt('Right b note, continuation verb',r'\unsure{servira}',r'\unsure{servira}','retained','Low reduced medial strokes do not make every letter secure.',13)
doubt('Final cancelled ending',r'\unsure{sous-fig}',r'\unsure{sous-fig|sous-fig.}','revised','Word is readable; terminal stop remains entangled in the cancellation.',15)
# Explicit row-by-row dispositions of C_context's 23 table rows, independent of prior audit assertions.
CTX=[]
def ctx(i,prompt,disposition,cd,ns):
 CTX.append(dict(row=i,prompt=prompt,disposition=disposition,c_doubt_ids=cd,evidence=[ev(n) for n in ns]))
ctx(1,'Definition, capital and family F','Capital remains one-position overprint/single-letter doubt; adjacent family F has curved cap.',['CD03'],[3])
ctx(2,'Definition and C6 diagrams: orders and vertical signs','Tuple and all horizontal bowed signs are preceq; vertical signs point down with the detached bar to the right.',['CD04'],[3,11,13])
ctx(3,'a mappings and marginal c links','First a mapping and G mapping capped; M mapping endpoint uncertain; phrase-link headless with short tick.',['CD08','CD09','CD19'],[7,10])
ctx(4,'a bracket, roof over F and raised M prime','Roof over the individual F and prime on the raised M are distinct; final ambient M prime also visible.',[],[7])
ctx(5,'Right of square, G low ticks','Two low strokes retained as G_n/G_m/G alternatives.',['CD28'],[13])
ctx(6,'Circled a, b and c labels','All three letters are circled; b is raised after et. Definition a), b) have ordinary closing parentheses.',[],[10,12,13])
ctx(7,'First paragraph, repetition marks and en forme','Two paired strokes read literally; en forme resolved.',['CD01','CD02'],[1,2])
ctx(8,'Definition, first capital and second order','Capital state remains uncertain; bowed order is secure.',['CD03','CD04'],[3])
ctx(9,'a, quelc. and correspondence wording','quelc. and correspond resolved, with the visible stop and final d.',['CD06','CD07'],[6])
ctx(10,'a mappings and marginal c caps','No arrowhead on first a or G links; second a endpoint retains alternatives.',['CD08','CD09'],[7,10])
ctx(11,'Oblique question, condition endings and et','First condition group remains compressed; stricte and de readable; et uncertain; final parenthesis incompletely framed.',['CD10','CD11','CD12','CD13'],[8])
ctx(12,'b, curled mark and cancelled clause','Crossed-head curl retained graphically; savoir/à savoir remains; si X in has no trailing F.',['CD14','CD15'],[9])
ctx(13,'Marginal c, reporter/fixé/deletions/i.e.','reporter and i.e. resolved; fixé ending uncertain; the F/S work is one initial position with no separate terminal s.',['CD16','CD17','CD18','CD20','CD21'],[10])
ctx(14,'C6 qualifier','de/dans/ds remains uncertain.',['CD22'],[11])
ctx(15,'C6 a, end of line','ou preferred, avec retained; no colon.',['CD23'],[12])
ctx(16,'Right b note, repeated nouns','First contracted-looking str.tes/strates; second one worked initial and a/point medial uncertainty; arêtes excluded by initial st strokes.',['CD24','CD25','CD26'],[13])
ctx(17,'Right b note, telles and servira','telles is live with t bar; servira retains doubt.',['CD27','CD29'],[13])
ctx(18,'Last line, cancelled ending','sous-fig readable, terminal stop uncertain.',['CD30'],[15])
ctx(19,'Definition, verb after qui','satisfait/satisfont retained.',['CD05'],[5])
ctx(20,'Oblique note, de/des','de resolved at the second occurrence; earlier des remains distinct.',['CD12'],[8])
ctx(21,'Right b note, G versus index','Two low ticks retained locally; prose expectation does not remove them.',['CD28'],[13])
ctx(22,'C6 a H versus square G prime','Declaration clearly has H, square lower-left has G′; mismatch retained, no mathematical repair.',[],[12])
ctx(23,'a, s’en correspond repeated check','Final d and following comma support correspond; no grammatical repair.',['CD07'],[6])
# Non-proof remaining uncertainties; every entry points to an uncertainty in reading.tex.
RD=[]
def remaining(loc,r,alts,why,conf='low'):
 RD.append(dict(location=loc,reading=r,alternatives=alts,confidence=conf,reason=why))
remaining('Definition capital',r'\unsure{\rlap{\deleted{\mathcal F}}\mathcal C|\mathcal C|\mathscr C|\mathbb C}',[r'\rlap{\deleted{\mathcal F}}\mathcal C',r'\mathcal C',r'\mathscr C',r'\mathbb C'],'Inner bars may be an older F or the construction of a single elaborate C.')
remaining('Definition tout',r'\unsure{\deleted{tout}|tout}',[r'\deleted{tout}','tout'],'The long stroke may cancel the word or be a broad t stroke.')
remaining('Definition verb',r'\unsure{satisfait|satisfont}',['satisfait','satisfont'],'Medial low group does not distinguish ai/on.','medium')
remaining('Second a mapping',r'\unsure{\mathrel{\vdash\joinrel\dashv}|\mathrel{\mapstochar\relbar}|\mapsto}',[r'\mathrel{\vdash\joinrel\dashv}',r'\mathrel{\mapstochar\relbar}',r'\mapsto'],'Right endpoint is dark and short.')
remaining('Slanted question, first condition',r'\unsure{condition}',['condition','a contracted condition form'],'The word is compressed; no unsupported expansion is asserted as certain.','medium')
remaining('Slanted question, deletion',r'\unsure{et}',['et'],'The small crossed group remains only a plausible reading.')
remaining('Slanted question, final parenthesis',r'\unsure{(condition large)|(condition lge)}',['(condition large)','(condition lge)'],'Final letters/closing parenthesis extend beyond the one crop; approximate missing continuation whole [550,970,660,1100].')
remaining('b, mark after M',r'\unsure{\}}',[r'\}','?','an unassigned curled/crossed mark'],'Crossing at the head and curling lower stroke are preserved in R1-MARK-AFTER-M.')
remaining('b, cancelled opening',r'\unsure{savoir|à savoir}',['savoir','à savoir'],'The rule obscures the opening; a separate à is not secure.')
remaining('Marginal c, fixé ending',r'\unsure{fixé|fixée}',['fixé','fixée'],'The final e may merge with the preceding accented ending.','medium')
remaining('Marginal c, worked initial',r'\unsure{\rlap{\deleted{F}}S|S|s}',[r'\rlap{\deleted{F}}S','S','s'],'One F/S-like position with lower residual strokes; no second independent s.')
remaining('C6 qualifier',r'\unsure{de|dans|ds}',['de','dans','ds'],'The d is followed by only one low reduced run.')
remaining('Diagonal symmetry word accent',r'\unsure{e|é}',['e','é'],'No detached acute is secure over the first e in symetrique.')
remaining('C6 a, last word',r'\unsure{ou|avec}',['ou','avec'],'Small disconnected low groups permit both, with ou preferred.')
remaining('Right note b, first noun',r'\unsure{str.tes|strates}',['str.tes','strates'],'Medial point-like form does not clearly form a complete a.','medium')
remaining('Right note b, second noun initial',r'\unsure{\deleted{S}|S|s}',[r'\deleted{S}','S','s'],'Crossed initial’s case and cancellation/retracing state remain uncertain.')
remaining('Right note b, second noun medial form',r'\unsure{a|.}',['a','.'],'Small form between tr and tes is not separable securely.')
remaining('Right note b, G tail',r'\unsure{G_n|G_m|G}',[r'G_n',r'G_m','G'],'Two connected low descenders may be an index or retracing.')
remaining('Right note b, complément accent',r'\unsure{é|\.{e}}',['é',r'\.{e}'],'Detached mark is point-like and may represent a very short acute.','medium')
remaining('Right note b, continuation verb',r'\unsure{servira}',['servira'],'Reduced low medial strokes prevent complete certainty.','medium')
remaining('Final body, first G-like letter',r'\unsure{G|\rlap{\deleted{F}}G|E}',['G',r'\rlap{\deleted{F}}G','E'],'Straight internal bars coexist with a looped outside.')
remaining('Final cancelled word',r'\unsure{sous-fig|sous-fig.}',['sous-fig','sous-fig.'],'The terminal point is obscured or absent beneath the crossing.','medium')
remaining('Bottom-margin G-like letter',r'\unsure{\rlap{\deleted{F}}G|G|E}',[r'\rlap{\deleted{F}}G','G','E'],'A stronger inner F-like layer is visible within the outer loop.')
# Inventory: all handwritten elements, including uncertain correction states.
I=[]
def inv(element,kind,pos,first):
 I.append(dict(element=element,kind=kind,position=pos,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('Folio','text','top centre','71')
inv('Opening paragraph','text','top body','Pour la suite')
inv('Definition heading','text','upper body, underlined','Définition 1')
inv('Definition body','text','under opening','On appelle sous-contrée')
inv('Raised qualification','insertion','above sous-contrée','[pleine], underlined')
inv('Qualification hook','drawing','under raised qualification','long curved hook to sous-contrée')
inv('Possible overwritten definition capital','deletion','before tuple equals','one F/C worked position, uncertain layer')
inv('Possible tout cancellation','deletion','end of definition first formula line','tout, uncertain state')
inv('Clause a prose','text','middle upper body','a) fermé pour ≤')
inv('Raised mapping phrase','insertion','above aux parties','par F′ capped-link F′ cap M,')
inv('Raised ambient subset','insertion','before de M','M′')
inv('Mapping insertion leader','drawing','under raised mapping phrase','long hooked rule')
inv('M-prime insertion leader','drawing','before de M','short upward arm')
inv('a final set formula','display','last a line','par M′ link F′ = {F in F | F-bar subset M′}].')
inv('Finite/arbitrary supremum question','margin note','oblique left of a–b','Je ne sais')
inv('Question crossed word','deletion','after stricte','et, uncertain')
inv('Clause b body','text','middle body','b) fermé pour preceq')
inv('Mark after M','drawing','b, after M before comma','crossed-head curl')
inv('Superseded b clause','deletion','under replacement','savoir/à savoir : si X in')
inv('Replacement b clause','insertion','above cancelled clause','qu’on va formuler')
inv('Relocation instruction','margin note','above c note at left','reporter')
inv('c assertion','margin note','above C6, right side','circled c Pour F′ preceq F')
inv('Worked c initial','deletion','start of Sous-fig. line','one F/S-like position, state uncertain')
inv('Headless phrase link','drawing','between sous-figure phrases','horizontal with short raised right endpoint')
inv('c downward pointer','drawing','from aux toward C6','down-left stroke with short head/return')
inv('C6 heading','text','lower body, underlined','C6')
inv('C6 introduction','text','right of heading','Soit')
inv('First C6 relation diagram','diagram','below Soit','F′ preceq F, G beneath F, qualifier and family F at right')
inv('Detached point pair','drawing','left of first diagram','two offset points')
inv('Symmetry note','margin note','diagonal left of C6','symetrique/symétrique en ≤, preceq')
inv('C6 left rule','drawing','crossing symmetry note, beside a','long slightly bent rule')
inv('Small point by rule','drawing','below diagonal order note','one detached small point')
inv('C6 a sentence','text','between diagrams','circled a Alors il existe un unique H')
inv('Square relation diagram','diagram','below a sentence','F′ F / G′ G with horizontal bowed and vertical straight orders')
inv('Right b assertion','margin note','right of square','et raised circled b les str.tes/strates')
inv('Worked second noun initial','deletion','right b note second line','one crossed S/s initial')
inv('b double rule','drawing','left of b note','two vertical rules and low crossing')
inv('Small continuation of b','insertion','beneath X′ << G-tail','Ce complément servira plus bas')
inv('Final paragraph','text','foot of body','On dit que G-like-prime est la subd de G induite')
inv('Worked final body capital','deletion','after On dit que','one G/F/E-like position, uncertain layer')
inv('Final cancelled word','deletion','right foot','sous-fig, terminal stop uncertain')
inv('Bottom slanted note','margin note','lower left','sur la sous-figure G-like de F')
inv('Worked bottom-margin capital','deletion','after sous-figure','one F/G/E-like position, uncertain layer')
# Every H unreadable placeholder, in literal source order.
HP=[]
def did(prefix):
 return [d['id'] for d in D if d['location'].startswith(prefix)]
placeholder_rows=[
 ('les axiomes \\ill{} passent','vont, within vont passer','Opening, axioms'),
 ('en forme [\\ill{}]','raised [pleine], attached to sous-contrée','Raised bracket'),
 ('de $\\mathcal{M}$, \\ill{} plus bas','qu’on va formuler, raised replacement','b, raised replacement'),
 ('\\struck{\\ill{} si $X \\in F$}','savoir/à savoir, cancelled prefix','b, opening of cancelled'),
 ('il faudra \\ill{} des','part of full slanted question, including prendre','Slanted left question'),
 ('des \\ill{} (','part of full slanted question, sup quelconques and remaining words','Slanted left question'),
 ('(\\ill{})','the slanted condition phrase, with retained endpoint uncertainty','Slanted left question'),
 ("$F'$, \\ill{} aux Sup",'commute','Marginal c, verb'),
 ('\\mathfrak{F}$ \\ill{} :','ou/avec, no colon','C6 a, word'),
 ('« \\ill{} complètement','Ce in editorially described continuation','Right note b, smaller'),
 ('complètement \\ill{} »','servira plus bas in same continuation; whole line assessed once','Right note b, smaller'),
 ('\\marginal{\\ill{} symétrie','no separate word before symetrique/symétrique','C6, diagonal'),
 ('symétrie \\ill{} $\\leq$','en','C6, diagonal'),
 ('$\\preccurlyeq$ \\ill{} sur','no separate word after order pair; sur belongs to lower note','C6, diagonal'),
 (', \\ill{} que','ou','Final body, conjunction')
]
for j,(scope,reading,pref) in enumerate(placeholder_rows,1):
 HP.append(dict(occurrence=j,h_scope=scope,disposition=reading,difference_ids=did(pref)))
notation=[
 dict(sign='repetition-like pairs',latex=r'= =',appearance='two pairs of horizontal strokes, second lower stroke hooked at left',location='opening after quand',alternatives=[]),
 dict(sign='worked contrée capital',latex=RD[0]['reading'],appearance='outer loop with interior F-like upright and bar',location='definition before equals',alternatives=RD[0]['alternatives']),
 dict(sign='family F',latex=r'\mathcal F',appearance='curved or looped upper cap and curved stem',location='tuple; both a formulas; first diagram qualifier; H membership',alternatives=[]),
 dict(sign='ambient M',latex='M',appearance='plain two-peaked capital; local primes separately visible',location='a formulas and b ambient subset pair',alternatives=[]),
 dict(sign='two orders',latex=r'\leq,\preceq',appearance='straight angle/bar versus bent upper and bowed lower strokes',location='definition, a, b, c and both diagrams',alternatives=[]),
 dict(sign='vertical order',latex=r'\rotatebox{90}{$\leq$}',appearance='downward angle with detached stroke to right',location='C6 diagrams',alternatives=[]),
 dict(sign='capped application',latex=r'\mathrel{\vdash\joinrel\dashv}',appearance='short horizontal with upright caps and no arrowhead',location='first a mapping and marginal c G mapping',alternatives=[]),
 dict(sign='second a link',latex=RD[3]['reading'],appearance='clear left cap, thick short right endpoint',location='M′ to family F′',alternatives=RD[3]['alternatives']),
 dict(sign='headless phrase link',latex='% R1-C-HEADLESS-LINK',appearance='horizontal stroke with tiny raised right endpoint',location='marginal c between sous-figure phrases',alternatives=[]),
 dict(sign='F roof',latex=r'\overline F',appearance='detached upper line over plain individual F',location='a subset condition',alternatives=[]),
 dict(sign='low G tail',latex=r'\unsure{G_n|G_m|G}',appearance='two low close downstrokes connected to G endpoint',location='right b note X′ relation',alternatives=['G_n','G_m','G']),
 dict(sign='circled part labels',latex=r'\textcircled{a},\textcircled{b},\textcircled{c}',appearance='small circles; b is raised after et',location='C6 and marginal c',alternatives=[]),
 dict(sign='literal contracted-looking noun',latex=r'\unsure{str.tes|strates}',appearance='st/r followed by a detached dot-like component then tes',location='first noun in right b note',alternatives=['str.tes','strates'])
]
abbreviations=[
 {'form':'sous-ens.','expansion':'sous-ensemble'}, {'form':'sup','expansion':'supremum'},
 {'form':'quelc.','expansion':'quelconque'}, {'form':'subd. / subd','expansion':'subdivision'},
 {'form':'sous-fig. / sous-fig','expansion':'sous-figure'}, {'form':'Sup','expansion':'supremum'},
 {'form':'i.e.','expansion':'id est'}, {'form':'str.tes (uncertain)','expansion':'strates'}
]
report=dict(reader='R1',cote='156-4',scan='72',brief_version='v08',started_utc='2026-11-20T12:06:33Z',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),image_views=[whole,half_a,half_b],reading_file=str(out/'reading.tex'),differences=D,c_doubts=CD,context_dispositions=CTX,inventory=I,remaining_doubts=RD,notation=notation,abbreviations=abbreviations,notes={
 'summary':'Handwritten definition of a full sub-contrée followed by C6, two relation diagrams, and substantial marginal corrections. Graphic connectors/rules and local correction states are retained.',
 'math_reading_decisions':'No proof inference selected a reading. The visible H in the declaration and G′ in the square are both retained. The F roof and the low G-tail strokes were checked as ink, not repaired by expected mathematics.',
 'author_checks':'Only reading checks were performed. No theorem, closure property or commutation claim was independently proved or refuted. H editorial qui ne and complètement are not adopted as manuscript words.',
 'title_dates_pagination':'Running folio 71 at top centre; scan marker 72 retained. No date or title; Définition 1 and C6 are local headings.'},check_events=[],crops=crops,workflow_feedback=['The one-crop rule leaves an incompletely framed terminal locus unresolved; crop 08 is explicitly flagged with approximate missing original coordinates rather than silently recropped.'],h_placeholder_dispositions=HP,h_editorial_assessments=[
 {'scope':'H note above b cancellation','h':"au-dessus de la biffure de b) sont insérés deux mots, « qui ne » et un mot souligné non lu",'disposition':'The ink reads qu’on va formuler. No independent qui ne is transcribed; the long crossing belongs to the deleted baseline clause, not an invented word underline.'},
 {'scope':'H note under X′ relation','h':r'« \ill{} complètement \ill{} »','disposition':'The smaller continuation is Ce complément/point-accented-e servira plus bas. The editorial complètement is not counted as a literal H manuscript word.'},
 {'scope':'H diagrams, circles and rules notes','disposition':'The notes describe real geometry, circles and rules, which are drawn explicitly in reading.tex; their wording was not used as image evidence.'}],framing_limitations=[{'crop':crops[7]['path'],'source':whole,'bbox':crops[7]['bbox'],'missing_continuation_approx_bbox':[550,970,660,1100],'description':'Last letters and closing parenthesis of lower condition phrase reach the right edge of the one crop. Approximate continuation is more likely near y=1000–1070. No recrop/revisit; endpoint reading retained uncertain.'}],inspection_log=str(out/'inspection_log.md'),workflow={'whole_views':1,'half_a_views':1,'half_b_views':1,'successful_own_crop_views':17,'ocr_used':False,'external_research_used':False,'other_reader_files_used':False,'other_pages_used':False,'delegation_used':False,'latex_compilation_used':False,'restoration_note':'After workspace replacement, identical own crops were restored from the saved bboxes/transforms. Previously viewed images were not displayed again.'})

# Keep local alphabet rows at symbol scope and attach every separately checked occurrence.
byid={d['id']:d for d in D}
byid['D015'].update(c=r"\mathcal F'",h=r"\mathfrak{F}'",reading=r"\mathcal F'",scope='Alphabet only: both independently inspected F-prime occurrences and the plain ambient M.',additional_witness_snippets=[{'c':r"\mathcal F'",'h':r"\mathfrak{F}'",'reading':r"\mathcal F'",'location':'second family F prime in the same inserted mapping'},{'c':'M','h':r'\mathcal{M}','reading':'M','location':'ambient M at end of inserted mapping'}])
byid['D020'].update(c=r"\mathcal F'",h=r"\mathfrak{F}'",reading=r"\mathcal F'",scope='Alphabet only: family F prime, family F after membership, and both plain M primes in this one baseline formula.',additional_witness_snippets=[{'c':r'\mathcal F','h':r'\mathfrak{F}','reading':r'\mathcal F','location':'family after F membership'},{'c':"M'",'h':r"\mathcal{M}'",'reading':"M'",'location':'first M prime and final M prime, each checked in crop 07'}])
byid['D033'].update(c=r'\deleted{\unsure{F}}sous-fig.',h='sous-fig.',scope='One worked initial and the associated lower residual strokes; no independent terminal s.',additional_witness_snippets=[{'c':r'\deleted{\unsure{s}}','h':'','reading':'% R1-FIG-MARGINAL-C','location':'C’s separate deleted s after F prime is reassigned to residual strokes below the worked initial, not read as an independent letter'}])
CTX[1]['evidence'].append(ev(None,[650,920,930,1140],half_b))
CTX[5]['evidence'].extend([ev(None,[250,800,309,884],half_b),ev(None,[385,775,480,1210],half_a)])
CTX[21]['evidence'].append(ev(None,[650,920,930,1140],half_b))
RD[4]['alternatives']=['condition']

(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'differences':len(D),'c_doubts':len(CD),'context_rows':len(CTX),'remaining_doubts':len(RD),'inventory':len(I),'crops':len(crops),'H_placeholders':len(HP)},indent=2))
