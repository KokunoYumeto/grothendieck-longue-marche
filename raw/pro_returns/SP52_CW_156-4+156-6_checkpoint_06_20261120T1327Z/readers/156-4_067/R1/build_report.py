import json
from pathlib import Path

O=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_067/R1')
P=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_067')
S=Path('/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans')
A=str(S/'J156-4-09_156-4_scan067_a.jpg')
B=str(S/'J156-4-09_156-4_scan067_b.jpg')
W=str(S/'J156-4-09_156-4_scan067.jpg')
crops=json.loads((O/'crop_manifest.json').read_text())
cm={Path(c['path']).stem:c for c in crops}
diff=[]

def d(loc,c,h,reading,evidence,crop=None,bbox=None,source=None,confidence='high',kind='misread symbol or index',marked='no',cc=False,ch=True,math=False):
    if crop:
        cr=cm[crop]
        box=bbox or cr['bbox']; src=cr['source']; cp=cr['path']
    else:
        box=bbox;src=source;cp=None
    diff.append(dict(id=f'D{len(diff)+1:03}',location=loc,c=c,h=h,reading=reading,scan_shows=evidence,confidence=confidence,kind=kind,marked_in_h=marked,change_c=cc,change_h=ch,crop=cp,bbox=box,bbox_image=src,source=src,math_consequential=math))

# The alphabet differences are scoped to every occurrence in the indicated block.
# The order of tokens in each string follows their order in that block.
alphabet=[
('Top first definition: family label, operator subscript, family in set',r"\mathcal F';\mathcal F;\mathcal F",r"\mathfrak{F}';\mathfrak{F};\mathfrak{F}",'01_top_first',[445,110,1655,211]),
('Raised inclusion over top first closing brace',r'\mathcal F',r'\mathfrak{F}','01_top_first',[1500,25,1630,108]),
('Top second definition: M prime, subscript M, set M',r"M';M;M",r"\mathcal{M}';\mathcal{M};\mathcal{M}",'02_top_second',[440,204,1644,289]),
('Top third line: initial M, family subscript, final M',r'M;\mathcal F;M',r'\mathcal{M};\mathfrak{F};\mathcal{M}','02_top_second',[850,284,1550,381]),
('Cancelled Donc sentence: family membership, family prime, subscript family',r"\mathcal F;\mathcal F';\mathcal F",r"\mathfrak{F};\mathfrak{F}';\mathfrak{F}",'03_deleted_sentence',[1015,400,1648,490]),
('Cancelled middle formula row: family prime, family subscript, M prime, family prime, M',r"\mathcal F';\mathcal F;M';\mathcal F';M",r"\mathfrak{F}';\mathfrak{F};\mathcal{M}';\mathfrak{F}';\mathcal{M}",'05_deleted_formulas',[730,483,1616,554]),
('Cancelled lower right equality: surviving M subscript and family argument',r'M;\mathcal F',r'\mathcal{M};\mathfrak{F}','05_deleted_formulas',[1340,544,1641,614]),
('Live Donc pour line: family',r'\mathcal F',r'\mathfrak{F}',None,[791,601,950,660]),
('Brace first row: family prime and M prime',r"\mathcal F';M'",r"\mathfrak{F}';\mathcal{M}'",'07_brace',[501,690,1177,778]),
('Brace second row: M prime, family prime, M',r"M';\mathcal F';M",r"\mathcal{M}';\mathfrak{F}';\mathcal{M}",'07_brace',[520,771,829,840]),
('Slanted left margin: M prime and family prime',r"M';\mathcal F'",r"\mathcal{M}';\mathfrak{F}'",'06_left_note',[200,700,364,777]),
('Right NB note: family prime, M prime, family, M, lower family prime',r"\mathcal F';M';\mathcal F;M;\mathcal F'",r"\mathfrak{F}';\mathcal{M}';\mathfrak{F};\mathcal{M};\mathfrak{F}'",'08_right_note',[1235,620,1642,860]),
('First middle definition: family double prime and three family occurrences',r"\mathcal F'';\mathcal F;\mathcal F';\mathcal F",r"\mathfrak{F}'';\mathfrak{F};\mathfrak{F}';\mathfrak{F}",'09_middle_definitions',[518,894,1547,1005]),
('Second middle definition: M double prime, M subscript, family prime, M subscript',r"M'';M;\mathcal F';M",r"\mathcal{M}'';\mathcal{M};\mathfrak{F}';\mathcal{M}",'09_middle_definitions',[518,992,1549,1097]),
('On a line: both family double primes',r"\mathcal F'';\mathcal F''",r"\mathfrak{F}'';\mathfrak{F}''",'10_on_a',[777,1129,1262,1224]),
('Lower first equality: both family subscripts and M with barred Phi subscript',r'\mathcal F;\mathcal F;M_{\overline\Phi}',r'\mathfrak{F};\mathfrak{F};\mathcal{M}_{\overline{\Phi}}','13_lower_operators',[305,354,1098,478]),
('Lower set equality: M subscript, M in set, final M with barred Phi subscript',r'M;M;M_{\overline\Phi}',r'\mathcal{M};\mathcal{M};\mathcal{M}_{\overline{\Phi}}','14_lower_builder',[707,435,1655,567]),
('Conclusion dans M',r'M',r'\mathcal{M}','15_ramene',[478,683,589,745]),
('First saturée definition: inserted family zero, live family, family in parenthesis',r'\mathcal F_0;\mathcal F;\mathcal F',r'\mathfrak{F}_0;\mathfrak{F};\mathfrak{F}','16_saturee_heading',[778,704,1314,902]),
('Second saturée definition: inserted M zero, M and parenthetical M',r'M_0;M;M',r'\mathcal{M}_0;\mathcal{M};\mathcal{M}','17_saturee_sentence',[491,911,955,1096]),
('Bottom first equality: M zero, family zero, M',r'M_0;\mathcal F_0;M',r'\mathcal{M}_0;\mathfrak{F}_0;\mathcal{M}',None,[645,1112,1004,1188]),
('Bottom second equality: family zero, family, M zero',r'\mathcal F_0;\mathcal F;M_0',r'\mathfrak{F}_0;\mathfrak{F};\mathcal{M}_0',None,[651,1176,1320,1246]),
]
for loc,c,h,cr,box in alphabet:
    src=B if loc.startswith('Bottom') else A
    d(loc,c,h,c,'The family sign has a bent/curled upper stroke and hooked stem; M is a single plain peaked capital. The indicated occurrences were each read, and do not show a Gothic family alphabet or a separate calligraphic M.',cr,box,src)

d('Top first operator',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosupp}',r'\operatorname{cosup}','Only one terminal descending p stem is visible. The middle double-p entries have two distinct downstrokes.','01_top_first',[538,150,675,199],kind='abbreviation expanded or spelling modernised',cc=True)
d('First disjoint clause',r'\text{disjoint \unsure{des|de} }',r'\text{disjoint des}',r'\text{disjoint \unsure{des|de} }','After d and e the heavily extended exit permits a terminal s but does not decide it.','01_top_first',[1219,124,1466,181],confidence='medium',kind='other')
d('First H_i relation to Phi',r'H_i\unsure{\vdash|\in}\Phi',r'H_i\in\Phi',r'H_i\vdash\Phi','A straight upright with one right-facing middle tick is visible; there is no lower rounded return.','01_top_first',[1496,108,1613,164],cc=True,math=True)
d('Raised inclusion and drawn enclosure',r'\Phi\inserted{\subset\mathcal F}',r'\Phi\rbrace\quad(\subset\mathfrak{F})',r'\Phi\quad\inserted{\subset\mathcal F}','The inclusion is above the first closing brace. A curved open enclosure runs under it, with a short downward pointer near Phi. No mathematical pair of parentheses surrounds it. Reading.tex reproduces the connector in TikZ.','01_top_first',[1495,24,1664,188],kind='drawing or diagram',cc=True)
d('Second top operator',r'\operatorname{cosup}_{M}',r'\operatorname{cosupp}_{\mathcal{M}}',r'\operatorname{cosup}_{M}','One p downstroke precedes the M subscript.','02_top_second',[533,242,743,310],kind='abbreviation expanded or spelling modernised')
d('Second disjoint clause',r'\text{disjoint \unsure{de|des} }',r'\text{disjoint des}',r'\text{disjoint de }','The ending after d-e is a short horizontal exit; no extra s body can be separated.','02_top_second',[1244,199,1497,266],confidence='medium',kind='misread word',cc=True)
d('Second top set final phi',r'\unsure{\Phi|\varphi}',r'\Phi',r'\unsure{\Phi|\varphi}','The small oval and descending stem have a short upturned foot; capital Phi and a cursive phi remain possible.','02_top_second',[1582,192,1617,232],confidence='medium',kind='other')
d('Second top set closing mark',r'\unsure{)|\}}\,\}',r'\rbrace',r'\}','The upper round portion, middle return and lower hooked portion form one continuous closing-brace group. I do not see a separate parenthesis followed by a full second brace.','02_top_second',[1608,192,1642,255],confidence='medium',cc=True,ch=False,math=True)
d('Inserted third top row',r'\inserted{=M\cap\operatorname{cosup}_{\mathcal F}(\Phi)\subset M}',r'=\mathcal{M}\cap\operatorname{cosupp}_{\mathfrak{F}}(\Phi)\subset\mathcal{M}',r'\inserted{=M\cap\operatorname{cosup}_{\mathcal F}(\Phi)\subset M}','The whole third equality is below a long connecting stroke turning down at its left edge. It is a raised/additional row relative to the second definition, and the operator has one p. The curve is reproduced in TikZ.','02_top_second',[845,274,1657,383],kind='insertion or placement',cc=True)
d('Cancelled Donc, words before comma',r'\unsure{on aura|on a}',r'\ill{}',r'\unsure{on aura|on a}','Two word-sized groups survive under crossing strokes; on is best in the first, with an a-led extended second group. The middle of the second group remains obscured.','03_deleted_sentence',[474,442,840,486],confidence='low',kind='readable ink left as \\ill{}',marked='yes')
d('Cancelled sentence, after membership',r'F\in\mathcal F\text{ posant}',r'F\in\mathfrak{F},\text{ posant}',r'F\in\mathcal F\text{ posant}','There is no separate comma between the family symbol and posant; the transverse ink is cancellation.','03_deleted_sentence',[1030,410,1375,492],kind='text not on the page')
d('Cancelled sentence, first incomplete definition',r"\mathcal F'=\operatorname{cosup}_{\mathcal F},",r"\mathfrak{F}'=\operatorname{cosupp}_{\mathfrak{F}}(\Phi)",r"\mathcal F'=\operatorname{cosup}_{\mathcal F},",'The top cancelled line stops after the operator subscript and a comma. The argument Phi belongs to the separately repeated definition on the line below, which H combines with this one.','03_deleted_sentence',[1385,400,1648,491],kind='insertion or placement')
d('Cancelled repeated definition on next row',r"\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi)",'',r"\deleted{\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi)}",'The second family-prime equation is independently written below the first cancelled sentence. It has two p stems and a Phi argument. H has only one family-prime equation.','05_deleted_formulas',[730,484,1234,565],kind='omission')
d('Isolated cancelled phi, letter form and position',r'\deleted{\unsure{\phi|\Phi}}',r'\struck{\Phi}',r'\deleted{\unsure{\phi|\Phi}}','The isolated group is below Donc at the left of the cancelled equations, with a long stem below the oval and no unambiguous foot. Lowercase phi is preferred; capital remains possible. H moves it after the formula chain.','04_deleted_phi',[327,500,407,574],confidence='low',kind='insertion or placement')
d('Cancelled lower-left operator and residual subscript',r'F\in\operatorname{cosup}_{\unsure{,|\mathcal F}}',r'F\in\operatorname{cosupp}',r'\deleted{F\in\operatorname{cosup}_{\unsure{,|\mathcal F}}}','One p stem is followed by a separate small low hook. It can be a comma-like remnant or an incomplete family subscript. H omits the remnant and supplies a second p.','05_deleted_formulas',[480,548,825,608],confidence='low',kind='omission')
d('Cancelled M-prime formula ending',r"M'=\mathcal F'\cap M,",r"\mathcal{M}'=\mathfrak{F}'\cap\mathcal{M}=",r"\deleted{M'=\mathcal F'\cap M,}", 'A separate comma follows M on that row; the equals sign is on the lower continuation.','05_deleted_formulas',[1300,484,1623,551],kind='insertion or placement')
d('Cancelled lower-right operator',r'\operatorname{cosup}_{\deleted{\unsure{\mathcal F}}M}',r'\operatorname{cosupp}_{\mathcal{M}}',r'\operatorname{cosup}_{\deleted{\unsure{\mathcal F}}M}','The operator has one p; below it M covers a hooked earlier subscript. Its underlying family identity is plausible but not fully separable.','05_deleted_formulas',[1398,551,1596,614],confidence='low',kind='omission')
d('Left margin initial',r'Ainsi,',r'ainsi,',r'Ainsi,','A tall capital A with a cross stroke starts the note.','06_left_note',[43,762,192,821],kind='misread word')
d('Left margin final word',r'\unsure{mutuellement}',r'mutuellement',r'\unsure{mutuellement}','The t and tall l-strokes and terminal t support mutuellement, but compressed initial and medial links remain unresolved.','06_left_note',[91,806,394,915],confidence='medium',kind='other')
d('Left margin pointer to brace',r'\margin{Ainsi, M\text{ et }\mathcal F\text{ se déterminent mutuellement}}',r'\note{la première note est en marge gauche, avec une flèche vers l’accolade}',r'\figure{\begin{tikzpicture}\draw[->] (0,0)--(.45,.08);\end{tikzpicture}}','A short shaft with a rightward point stands at the end of the slanted second line and points toward the brace. The note and pointer are represented together, with note text only once.','06_left_note',[348,762,416,802],confidence='medium',kind='drawing or diagram',cc=True)
d('Brace second row low point',r'\unsure{.|\cdot}',r'',r'.','A separate point is below the equals-sign centre, at the lower level of the adjacent lettering. It is preserved as a low point, without supplying a multiplication meaning.','07_brace',[645,805,674,833],cc=True,kind='omission')
d('NB note, gap and lower subject',r"\mathcal F'",r"\ill{}\mathfrak{F}'",r"\mathcal F'",'There is a separate family-prime label above Stable and a connecting/enclosing stroke. I see no additional word-sized group requiring an illegible-text placeholder.','08_right_note',[1235,786,1380,861],kind='text not on the page',marked='yes')
d('NB note, Stable ending/capital',r'\unsure{Stable|Stables}',r'stables',r'Stable','The large looped initial is capital S; after l and e the line exits horizontally. No separately formed final s can be followed.','08_right_note',[1248,846,1440,898],confidence='medium',kind='misread word',cc=True)
d('NB note, Sup capitalization',r'Sup.',r'sup.',r'Sup.','The initial S is a large looped capital, followed by one p and a separate terminal point.','08_right_note',[1530,852,1653,911],kind='misread word')
d('NB note, underline and enclosure',r"\mathcal F'\ \uline{\unsure{Stable|Stables} par Sup.}",r"\mathfrak{F}'\ (stables par sup.)",r"\mathcal F'\ \uline{Stable par Sup.}",'The phrase is underlined, with an additional open angular/curved enclosure and a rising arm under the separate family-prime label. There are no mathematical parentheses. The distinct strokes are reproduced in TikZ.','08_right_note',[1219,789,1658,950],kind='drawing or diagram',cc=True)
d('Middle definitions, equality labels at both occurrences',r'\overset{\text{def}}{=}',r'\overset{\text{déf}}{=}',r'\overset{\text{def}}{=}','Both small labels have d-e-f strokes without a distinct accent over e.','09_middle_definitions',[1090,880,1202,1046],kind='abbreviation expanded or spelling modernised')
d('Middle second operator',r'\operatorname{cosup}_{M}',r'\operatorname{cosupp}_{\mathcal{M}}',r'\operatorname{cosup}_{M}','This operator has one descending p, whereas the family-double-prime operator above has two.','09_middle_definitions',[705,1019,923,1092],kind='abbreviation expanded or spelling modernised')
d('Word after On a',r'\unsure{bien|vu|la|là}',r'donc',r'\unsure{vu|bien|la|là}','One short initial upright/curved stroke is followed by a nearly level run; there is no clearly dotted i or detached accent. Vu is my best reading, but the reduced strokes do not settle the alternatives. Donc has no visible supporting loop sequence.','10_on_a',[548,1171,664,1218],confidence='low',kind='misread word',cc=True)
d('On a line, Sup spelling',r'\unsure{Sup|Supp}',r'Sup.',r'\unsure{Sup|Supp},','The p-region is multiply traced, so one p versus two cannot be decided. The following detached stroke is a comma, not a full stop.','10_on_a',[1535,1149,1642,1240],confidence='low',kind='misread word')
d('Cancelled contient Phi',r'\deleted{contient $\Phi$}',r'\struck{\ill{} $\Phi$}',r'\deleted{contient $\Phi$}','The surviving c/on cluster, t stem, dotted i and ent exit permit contient despite the horizontal cancellation. Phi is separately visible and cancelled with it.','11_passage',[311,158,739,225],confidence='medium',kind='readable ink left as \\ill{}',marked='yes')
d('After passage through sous-figure',r'\unsure{à|:} une sous-figure.',r'aux sous-figures.',r'\unsure{:|à} une sous-figure.','Two separated short marks after passage look most like a colon, although an extremely reduced à remains possible. A separate wavy une follows; sous-figure ends with e and a full stop, without a visible plural s.','11_passage',[307,143,1519,323],confidence='medium',kind='misread word',marked='yes',cc=True)
d('Union, cancelled symbol before barred Phi',r'\deleted{\unsure{M}}',r'',r'\deleted{\unsure{M}}','A separate heavily cancelled symbol with two rising stems precedes the barred Phi. M is plausible, but it is not fully recoverable. It must not be omitted.','12_union',[1033,217,1095,291],confidence='low',kind='omission')
d('Lower first equality, both operators',r'\operatorname{cosup}_{\mathcal F}(\Phi)=\operatorname{cosup}_{\mathcal F}(M_{\overline\Phi})',r'\operatorname{cosupp}_{\mathfrak{F}}(\Phi)=\operatorname{cosupp}_{\mathfrak{F}}(\mathcal{M}_{\overline\Phi})',r'\operatorname{cosup}_{\mathcal F}(\Phi)=\operatorname{cosup}_{\mathcal F}(M_{\overline\Phi})','Each operator has one long p stem; neither has the two separate descending strokes seen in the middle cosupp and supp entries.','13_lower_operators',[305,357,1098,480],kind='abbreviation expanded or spelling modernised')
d('Lower second operator and overwritten subscript',r'\operatorname{cosup}_{\deleted{\unsure{\mathcal F}}M}',r'\operatorname{cosupp}_{\mathcal M}',r'\operatorname{cosup}_{\deleted{\unsure{\mathcal F}}M}','One p precedes the subscript; an earlier hooked character is covered by the live M. The earlier family letter remains uncertain.','13_lower_operators',[302,517,502,586],confidence='low',kind='omission')
d('Lower second operator, two separate low marks after M subscript',r'',r'',r'_{M\unsure{..|:}}','Two small dark isolated points stand immediately to the right of the M subscript and well below the following argument baseline. They slope slightly down to the right; their purpose and punctuation identity remain uncertain.','13_lower_operators',[501,541,522,559],confidence='low',kind='omission',cc=True)
d('Lower set, crossed loop before first X',r'\deleted{\unsure{\varnothing|x}}',r'',r'\deleted{\unsure{\varnothing|x}}','A small crossed loop lies between the set brace and the first full X. It is distinct from that X; empty-set sign or a small x remains unresolved.','14_lower_builder',[750,475,776,512],confidence='low',kind='omission')
d('Lower set, tt or universal sign',r'\unsure{\mathrm{tt}|\forall}',r'\text{tt}',r'\unsure{\mathrm{tt}|\forall}','Two high uprights and a shared cross-stroke can be read as compressed tt; the angular connection also permits a universal sign. Context does not settle the ink.','14_lower_builder',[1373,437,1441,498],confidence='medium',kind='other',math=True)
d('Conclusion word before à',r'\unsure{ramené|revenu}',r'ramené',r'\unsure{ramené|revenu}','The compressed middle is not fully recoverable, and the final rising tick could be an accent or exit stroke. Ramené remains preferred with revenu retained.','15_ramene',[749,584,982,641],confidence='medium',kind='other')
d('Conclusion terminal section sign',r'\unsure{\S|?}',r'§',r'\S','A narrow connected double-loop mark stands separately after M. It has no detached question-mark dot.','15_ramene',[693,662,725,726],cc=True,ch=False)
d('First saturée heading, raised family-zero label',r'\inserted{\mathcal F_0}',r'\struck{\mathfrak{F}_0}',r'\inserted{\mathcal F_0}','The zero is a small lower oval and the whole family-zero label is raised between saturée and de. No cancellation line passes through it.','16_saturee_heading',[783,707,869,776],kind='deletion state (struck given live or live given struck)',math=True)
d('First saturée heading, overwritten M under live family',r'\deleted{\unsure{M}}\mathcal F',r'\mathfrak{F}',r'\deleted{\unsure{M}}\mathcal F','The live family sign is superposed on a two-stem earlier character; M is plausible but still uncertain.','16_saturee_heading',[946,734,1038,814],confidence='low',kind='omission')
d('Heading underline extent',r'\uline{Partie saturée \inserted{$\mathcal F_0$} de}',r'\emph{Partie saturée de $\mathfrak{F}$}',r'\uline{Partie saturée \inserted{$\mathcal F_0$} de}','The line extends below Partie saturée de and ends before the overwritten family capital. The raised zero-label is above the underlined text.','16_saturee_heading',[388,772,1042,865],kind='insertion or placement')
d('First definition, parenthetical placement',r'\text{cosupport de son cosupport }(\text{p. r. à }\mathcal F)',r'\text{cosupport }(\uncertain{p.r. à}\mathfrak{F})\text{ de son cosupport}',r'\text{cosupport de son cosupport }(\text{p. r. à }\mathcal F)','The parenthesis follows the second cosupport on the next line; H moves it after the first.','16_saturee_heading',[303,842,1309,929],kind='insertion or placement',marked='yes')
d('Parenthetical abbreviation certainty',r'\text{p. r. à }',r'\uncertain{p.r. à}',r'\text{p. r. à }','The p descender, first point, r-like stroke, second point and accented a are visible. The spacing is retained, and no expansion is supplied.','16_saturee_heading',[990,841,1150,914],kind='other',marked='yes')
d('Second occurrence of saturée',r'\unsure{saturée}',r'saturée',r'\unsure{saturée|saturee}','The word is reduced to a leading s, ascending t and flattened connecting strokes. The acute accent is not separately secure, so both accent states are retained.','17_saturee_sentence',[307,970,520,1024],confidence='medium',kind='other',cc=True)
d('Second saturée definition, son support',r'\text{cosupport de son support}',r'\text{cosupport de son cosupport}',r'\text{cosupport de son support}','The second term begins with the s-shaped stroke followed immediately by u and two p stems; no co group precedes it. The apparent mathematical mismatch is preserved.','17_saturee_sentence',[305,1022,579,1109],kind='misread word',math=True)
d('Final mutuellement',r'\unsure{mutuellement}',r'mutuellement',r'\unsure{mutuellement}','The two l-stems and terminal t are clear, but the central t/u/e group is heavily worked.','18_mutuellement_par',[556,1075,920,1135],confidence='medium',kind='other')
d('Final par, including possible cancellation state',r'\unsure{par}',r'par',r'\unsure{par|\deleted{par}}','There is one word-sized group: a looped p with a long dark horizontal exit across the ar region. The stroke can be a retraced exit or a cancellation, so no second word is invented.','18_mutuellement_par',[954,1089,1039,1130],confidence='low',kind='deletion state (struck given live or live given struck)',cc=True)
d('Bottom first equality, terminal comma in H',r'M_0=\mathcal F_0\cap M',r'\mathcal{M}_0=\mathfrak{F}_0\cap\mathcal{M},',r'M_0=\mathcal F_0\cap M','No independent comma follows the final M; the next equation is a separate lower row.',None,[646,1117,1010,1190],B,kind='text not on the page')
d('Bottom set condition, bar over F',r'\overline F\subset M_0',r'F\subset\mathcal{M}_0',r'\overline F\subset M_0','A distinct horizontal bar stands above F in the set condition. H omits it.',None,[1051,1167,1282,1239],B,math=True)
d('Bottom display row arrangement and final stop',r'\begin{aligned}M_0&=\mathcal F_0\cap M\\\mathcal F_0&=\{F\in\mathcal F\mid\overline F\subset M_0\}\end{aligned}',r'\mathcal{M}_0=\mathfrak{F}_0\cap\mathcal{M},\qquad\mathfrak{F}_0=\lbrace F\in\mathfrak{F}\mid F\subset\mathcal{M}_0\rbrace.',r'\begin{aligned}M_0&=\mathcal F_0\cap M\\\mathcal F_0&=\{F\in\mathcal F\mid\overline F\subset M_0\}\end{aligned}','The equations are stacked on two lines. After the last closing brace no separate full stop is visible.',None,[642,1111,1320,1248],B,kind='insertion or placement')

cd=[]
def doubt(loc,c,r,status,ev,cr=None,box=None,src=None):
    if cr:
        p=cm[cr]; cp=p['path']; box=box or p['bbox']; src=p['source']
    else:cp=None
    cd.append(dict(location=loc,c=c,reading=r,status=status,scan_shows=ev,crop=cp,bbox=box,bbox_image=src,source=src))

# One disposition for each of the 26 explicit unsure macros in C.tex.
u=[
('C.tex doubt 01, first operator',r'\unsure{\operatorname{cosup}|\operatorname{cosupp}}',r'\operatorname{cosup}','resolved','One terminal p downstroke.','01_top_first'),
('C.tex doubt 02, first disjoint ending',r'\unsure{des|de}',r'\unsure{des|de}','retained','The last exit is too heavy to isolate an s.','01_top_first'),
('C.tex doubt 03, first H_i relation',r'\unsure{\vdash|\in}',r'\vdash','resolved','Straight upright with right tick, no curved lower member stroke.','01_top_first'),
('C.tex doubt 04, second disjoint ending',r'\unsure{de|des}',r'de','resolved','Short terminal exit with no separately formed s.','02_top_second'),
('C.tex doubt 05, second final phi',r'\unsure{\Phi|\varphi}',r'\unsure{\Phi|\varphi}','retained','Small oval, long stem and abbreviated rising foot do not decide case/form.','02_top_second'),
('C.tex doubt 06, second closing strokes',r'\unsure{)|\}}\,\}',r'\}','revised','The rounded upper stroke and lower hook belong to one continuous brace.','02_top_second'),
('C.tex doubt 07, cancelled on aura/on a',r'\unsure{on aura|on a}',r'\unsure{on aura|on a}','retained','Two word groups are present; cancellation hides the middle of the second.','03_deleted_sentence'),
('C.tex doubt 08, isolated cancelled phi',r'\unsure{\phi|\Phi}',r'\unsure{\phi|\Phi}','retained','Long descender with no secure lower foot.','04_deleted_phi'),
('C.tex doubt 09, cancelled residual subscript',r'\unsure{,|\mathcal F}',r'\unsure{,|\mathcal F}','retained','Small low open hook survives below strike.','05_deleted_formulas'),
('C.tex doubt 10, cancelled lower-right underlying subscript',r'\deleted{\unsure{\mathcal F}}',r'\deleted{\unsure{\mathcal F}}','retained','Hooked strokes remain beneath live M but do not fully recover the earlier symbol.','05_deleted_formulas'),
('C.tex doubt 11, left note mutuellement',r'\unsure{mutuellement}',r'\unsure{mutuellement}','retained','Tall strokes and final t survive; compressed links remain uncertain.','06_left_note'),
('C.tex doubt 12, low point',r'\unsure{.|\cdot}',r'.','resolved','Point lies at low punctuation level below equals centre.','07_brace'),
('C.tex doubt 13, Stable ending',r'\unsure{Stable|Stables}',r'Stable','resolved','No independent terminal s after e.','08_right_note'),
('C.tex doubt 14, word after On a',r'\unsure{bien|vu|la|là}',r'\unsure{vu|bien|la|là}','revised','Initial short upright and a long low run favour vu weakly; no secure accent or i dot.','10_on_a'),
('C.tex doubt 15, Sup spelling',r'\unsure{Sup|Supp}',r'\unsure{Sup|Supp}','retained','p region is retraced and does not securely count one or two p strokes.','10_on_a'),
('C.tex doubt 16, mark after passage',r'\unsure{à|:}',r'\unsure{:|à}','revised','Two isolated marks favour colon; extremely abbreviated à remains possible.','11_passage'),
('C.tex doubt 17, cancelled M before barred Phi',r'\deleted{\unsure{M}}',r'\deleted{\unsure{M}}','retained','Two ascending strokes exist beneath a heavy cancellation.','12_union'),
('C.tex doubt 18, underlying lower operator subscript',r'\deleted{\unsure{\mathcal F}}',r'\deleted{\unsure{\mathcal F}}','retained','A hooked earlier form is covered by M.','13_lower_operators'),
('C.tex doubt 19, crossed loop before X',r'\unsure{\varnothing|x}',r'\unsure{\varnothing|x}','retained','A small crossed oval separate from the full X is visible.','14_lower_builder'),
('C.tex doubt 20, tt/forall',r'\unsure{\mathrm{tt}|\forall}',r'\unsure{\mathrm{tt}|\forall}','retained','Two uprights and shared cross stroke allow both stated candidates.','14_lower_builder'),
('C.tex doubt 21, ramené/revenu',r'\unsure{ramené|revenu}',r'\unsure{ramené|revenu}','retained','Compressed middle and ambiguous final rising tick remain.','15_ramene'),
('C.tex doubt 22, section/question marker',r'\unsure{\S|?}',r'\S','resolved','Connected narrow double loop, no detached question dot.','15_ramene'),
('C.tex doubt 23, overwritten M in heading',r'\deleted{\unsure{M}}',r'\deleted{\unsure{M}}','retained','Two earlier stems under the live hooked family sign remain partly covered.','16_saturee_heading'),
('C.tex doubt 24, second saturée',r'\unsure{saturée}',r'\unsure{saturée|saturee}','revised','The word is plausible but a separate acute is not secure.','17_saturee_sentence'),
('C.tex doubt 25, bottom mutuellement',r'\unsure{mutuellement}',r'\unsure{mutuellement}','retained','Two l stems are clear; the central worked cluster is not.','18_mutuellement_par'),
('C.tex doubt 26, final par',r'\unsure{par}',r'\unsure{par|\deleted{par}}','revised','One group has a dark horizontal that may be either retracing or cancellation.','18_mutuellement_par')
]
for z in u:doubt(*z)

# Context rows are tracked separately, including repeated cautions and explicit
# notation checks, so none is silently omitted as duplicating a C.tex macro.
context_rows=[l for l in (P/'C_context.md').read_text().splitlines() if l.startswith('| 67')]
ctx=[
(r"\mathcal F',M',\mathcal F'',M''",'resolved','Raised ticks are one in the first pair and two in the lower pair. M is plain and family F is hooked.','09_middle_definitions'),
(r'\operatorname{cosup};\operatorname{cosupp};\operatorname{supp};\overset{\text{def}}{=}','resolved','Top three operators each have one terminal p; the middle family operator has two, the middle M operator one, both supp terms two. The def labels have no secure accent.','09_middle_definitions'),
(r'\overline F;\Longleftrightarrow','resolved','The F has a separate upper bar; the equivalence has two shafts and two heads.','07_brace'),
(r'H_i;\overline H_i;\mathcal F_0;M_0','resolved','The two union indices are short dotted i forms, and the overbar covers H rather than i; bottom zero forms are low ovals.','12_union'),
(r'\unsure{\mathrm{tt}|\forall}','retained','Two high strokes share a crossbar; the form alone leaves both candidates.','14_lower_builder'),
(r'\}','revised','One continuous brace has a round upper portion; no independent extra parenthesis is established.','02_top_second'),
(r'\unsure{on aura|on a}','retained','Crossing lines mask medial letters after on.','03_deleted_sentence'),
(r'\unsure{,|\mathcal F}','retained','A low hook survives but no complete family sign.','05_deleted_formulas'),
(r'\deleted{\unsure{\mathcal F}}M','retained','Both overwritten subscript sites show partial hooked strokes under M; neither is fully recovered.','13_lower_operators'),
(r'\unsure{mutuellement}','retained','Left slanted note has clear tall strokes with compressed connectors.','06_left_note'),
(r'Stable','resolved','No separately formed final s follows e.','08_right_note'),
(r'\unsure{vu|bien|la|là}','revised','The few strokes weakly favour vu; no candidate is established.','10_on_a'),
(r'\deleted{\unsure{M}}','retained','Two rises under the cancellation before barred Phi.','12_union'),
(r'\deleted{\unsure{\varnothing|x}}','retained','Small crossed loop before full X.','14_lower_builder'),
(r'\unsure{\mathrm{tt}|\forall}','retained','Angular shared cross-stroke does not determine tt versus universal sign.','14_lower_builder'),
(r'\unsure{ramené|revenu}','retained','Medial strokes and final tick remain inconclusive.','15_ramene'),
(r'\S','resolved','Two connected loops, no separate question dot.','15_ramene'),
(r'\deleted{\unsure{M}}','retained','Earlier two-stem character is covered by live family F in heading.','16_saturee_heading'),
(r'\unsure{saturée|saturee}','revised','Abbreviated word is retained with an explicit accent-state alternative.','17_saturee_sentence'),
(r'\unsure{mutuellement}','retained','Two l stems are visible but worked centre remains.','18_mutuellement_par'),
(r'\vdash','resolved','First H relation is a straight stem and right tick.','01_top_first'),
(r'\unsure{\Phi|\varphi}','retained','Small oval/stem form has an abbreviated foot.','02_top_second'),
(r'\deleted{\unsure{\phi|\Phi}}','retained','Cancelled isolated glyph has a long descending stem.','04_deleted_phi'),
(r'.','resolved','Isolated point is low, not centred on the equals axis.','07_brace'),
(r'\unsure{Sup|Supp};\unsure{:|à}','revised','The p group remains retraced; two separated marks after passage favour colon over à.','11_passage'),
(r'\unsure{par|\deleted{par}}','revised','One word-sized group admits a cancellation-state doubt.','18_mutuellement_par'),
(r'\operatorname{cosup}','resolved','The single-descender operator forms are retained with one p; two-p comparanda on this page are distinct.','13_lower_operators'),
(r'\unsure{des|de};de','revised','First ending remains heavy and uncertain; second has no separately formed terminal s.','02_top_second'),
(r'\}','revised','The extra putative closing stroke is treated as the rounded upper part of a single brace.','02_top_second'),
(r'\text{cosupport de son support}','resolved','Second noun begins with s, with no co prefix.','17_saturee_sentence')
]
assert len(context_rows)==len(ctx),(len(context_rows),len(ctx))
for i,(row,z) in enumerate(zip(context_rows,ctx),1):
    r,st,ev,cr=z
    doubt(f'C_context row {i:02}',row,r,st,ev,cr)

inventory=[]
def inv(el,kind,pos,first):inventory.append(dict(element=el,kind=kind,position=pos,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
for x in [
('I01','text','top centre','66'),
('I02','display','top row',r"\mathcal F'=\operatorname{cosup}_{\mathcal F}(\Phi)"),
('I03','insertion','above top row at right',r'\subset\mathcal F'),
('I04','drawing','beneath raised top inclusion','Curved open enclosure and short downward pointer'),
('I05','display','second row',r"M'=\operatorname{cosup}_M(\Phi)"),
('I06','insertion','third row under second definition',r'=M\cap\operatorname{cosup}_{\mathcal F}(\Phi)\subset M'),
('I07','drawing','above third row','Long curved connecting stroke from right edge turning down at equality'),
('I08','deletion','upper third, first cancelled prose row','Donc on aura/on a, pour'),
('I09','deletion','left below cancelled Donc',r'\phi/\Phi'),
('I10','deletion','second cancelled row',r"\mathcal F'=\operatorname{cosupp}_{\mathcal F}(\Phi),M'=\mathcal F'\cap M,"),
('I11','deletion','lower left cancelled row',r'F\in\operatorname{cosup}'),
('I12','deletion','lower right cancelled row',r'=\operatorname{cosup}_M(\mathcal F)'),
('I13','deletion','overwritten subscript within cancelled lower-right operator',r'\unsure{\mathcal F}'),
('I14','text','below cancelled block',r'Donc pour $F\in\mathcal F$'),
('I15','display','central brace',r"F\in\mathcal F'\Longleftrightarrow\overline F\subset M';M'=.\mathcal F'\cap M"),
('I16','margin note','slanted at left of brace','Ainsi, M′ et ℱ′ se déterminent mutuellement'),
('I17','drawing','between slanted note and brace','Short right-pointing arrow'),
('I18','margin note','right of brace','NB ℱ′, M′ sont des parties fermées de ℱ, M.'),
('I19','margin note','below NB note, shifted left','ℱ′ Stable par Sup.'),
('I20','drawing','around lower right margin note','Raised arm under ℱ′ and open enclosure around underlined Stable par Sup.'),
('I21','text','between brace and double-prime definitions',"Soit d'autre part"),
('I22','display','first double-prime row',r"\mathcal F''=\operatorname{cosupp}_{\mathcal F}(\mathcal F')\overset{\text{def}}{=}\operatorname{supp}_{\mathcal F}(\Phi)"),
('I23','display','second double-prime row',r"M''=\operatorname{cosup}_M(\mathcal F')\overset{\text{def}}{=}\operatorname{supp}_M(\Phi)"),
('I24','text','middle paragraph through union and alors','On a vu/bien/la/là … et par passage :/à une sous-figure. Soit … alors'),
('I25','deletion','second line of On a paragraph','contient Φ'),
('I26','deletion','before barred Phi in union',r'\unsure{M}'),
('I27','display','first lower equality',r'\operatorname{cosup}_{\mathcal F}(\Phi)=\operatorname{cosup}_{\mathcal F}(M_{\overline\Phi})'),
('I28','display','second lower equality',r'\operatorname{cosup}_M(\Phi)=\{X\in M\mid X\text{ disjoint de tt/}\forall\ Y\in M_{\overline\Phi}\}'),
('I29','deletion','second lower operator subscript',r'\unsure{\mathcal F}'),
('I30','deletion','between lower set brace and X',r'\unsure{\varnothing|x}'),
('I31','text','below lower display','donc on est ramené/revenu à des constructions dans M. §'),
('I32','text','underlined heading and first saturée definition','Partie saturée de ℱ : égale au cosupport de son cosupport (p. r. à ℱ).'),
('I33','insertion','above heading between saturée and de',r'\mathcal F_0'),
('I34','deletion','beneath corrected family capital in heading',r'\unsure{M}'),
('I35','text','second saturée definition','Partie saturée de M : égale au cosupport de son support (dans M).'),
('I36','insertion','above second definition between saturée and de',r'M_0'),
('I37','text','last prose lines','Elles se correspondent mutuellement par'),
('I38','deletion','possible state of final par',r'\unsure{par|\deleted{par}}'),
('I39','display','two stacked bottom rows',r'M_0=\mathcal F_0\cap M;\mathcal F_0=\{F\in\mathcal F\mid\overline F\subset M_0\}')
]: inv(*x)

remaining=[]
def rem(loc,reading,alts,conf,reason):remaining.append(dict(location=loc,reading=reading,alternatives=alts,confidence=conf,reason=reason))
for x in [
('Top first disjoint',r'des',[r'de'],'medium','The exit after e remains too heavy to separate s.'),
('Top second phi',r'\Phi',[r'\varphi'],'medium','Small loop/stem with an abbreviated foot.'),
('Cancelled after Donc','on aura',['on a'],'low','The second word group is crossed through twice.'),
('Isolated cancelled phi',r'\phi',[r'\Phi'],'low','Long descender survives but cancellation obscures the oval/foot relation.'),
('Cancelled lower-left operator subscript',r',',[r'\mathcal F'],'low','Only a small hook remains.'),
('Cancelled lower-right overwritten subscript',r'\mathcal F',[],'low','Earlier hooked strokes under M are incomplete.'),
('Left marginal final word','mutuellement',[],'medium','Compressed links between tall strokes.'),
('After On a','vu',['bien','la','là'],'low','One short initial stroke and flat run do not decide the word.'),
('On a line after stable par','Sup',['Supp'],'low','The final p cluster is heavily retraced.'),
('After passage',':',['à'],'medium','Two separate points could represent an extremely reduced accented a.'),
('Cancelled symbol before barred Phi',r'M',[],'low','Heavy crossing masks the two-stem symbol.'),
('Lower live operator underlying subscript',r'\mathcal F',[],'low','Hooked earlier form only partially survives under M.'),
('Two low marks following lower M subscript',r'..',[r':'],'low','They are isolated and slightly diagonal; their role is unknown.'),
('Crossed loop before X',r'\varnothing',[r'x'],'low','Small crossed oval is not completely recoverable.'),
('After disjoint de before Y',r'\mathrm{tt}',[r'\forall'],'medium','Shared crossbar and uprights allow two graphic readings.'),
('Conclusion before à','ramené',['revenu'],'medium','Compressed middle and an accent-like terminal tick.'),
('Overwritten symbol under heading family',r'M',[],'low','Two stems remain below a heavily retraced live family F.'),
('Second saturée','saturée',['saturee'],'medium','The accent is not securely separated from surrounding traces.'),
('Final mutuellement','mutuellement',[],'medium','Worked central cluster between clear stems.'),
('Final par state',r'par',[r'\deleted{par}'],'low','Dark horizontal could be a retraced word exit or a cancellation.')
]:rem(*x)

notation=[
dict(sign='Family of figures',latex=r'\mathcal F,\mathcal F\prime,\mathcal F\prime\prime,\mathcal F_0',appearance='Bent or curled upper stroke and hooked descending stem; later hurried forms can be angular.',location='Throughout, individually checked in each block.',alternatives=[]),
dict(sign='Ambient M',latex=r'M,M\prime,M\prime\prime,M_0',appearance='One plain peaked capital with two rises; no distinct calligraphic alphabet.',location='All definitions and final display.',alternatives=[]),
dict(sign='Individual F',latex=r'F,\overline F',appearance='Plain stem and two arms; upper bars are separate strokes.',location='Set builders, brace equivalence, final condition.',alternatives=[]),
dict(sign='First H relation',latex=r'\vdash',appearance='Straight upright with short right tick; no rounded lower return.',location='Top first set, H_i before Phi.',alternatives=[]),
dict(sign='Second small phi',latex=r'\unsure{\Phi|\varphi}',appearance='Small closed oval with descending stem and shortened rising foot.',location='Top second set final glyph.',alternatives=[r'\varphi']),
dict(sign='Equivalence arrow',latex=r'\Longleftrightarrow',appearance='Two distinct shafts and left/right heads.',location='Brace first row.',alternatives=[]),
dict(sign='Low point',latex='.',appearance='Small detached point below equals centre.',location='Brace second row before family prime.',alternatives=[]),
dict(sign='Two low points',latex=r'\unsure{..|:}',appearance='Two black dots immediately right of lower M subscript, diagonally offset.',location='Lower second cosup operator.',alternatives=[':']),
dict(sign='tt/universal glyph',latex=r'\unsure{\mathrm{tt}|\forall}',appearance='Two uprights sharing a horizontal cross-stroke and angular connecting line.',location='Lower set after disjoint de.',alternatives=[r'\forall']),
dict(sign='Section marker',latex=r'\S',appearance='Narrow double loop with continuous centre, no detached dot.',location='After dans M.',alternatives=[]),
dict(sign='H indices and overbar',latex=r'H_i,\overline H_i',appearance='Short dotted i, with upper horizontal over H only.',location='Top definitions and union.',alternatives=[]),
dict(sign='Zero subscripts',latex=r'\mathcal F_0,M_0',appearance='Small low oval.',location='Raised additions and final display.',alternatives=[]),
]

viewnotes={
'01_top_first':'cosup has one p; first des/de retained; H_i relation is a straight upright and right tick; raised inclusion has enclosure and downward pointer.',
'02_top_second':'cosup has one p; disjoint de; small phi retained uncertain; one continuous closing brace; third-row curve inspected.',
'03_deleted_sentence':'Two groups on aura/on a remain masked; no comma after family membership; first incomplete operator ends with comma.',
'04_deleted_phi':'One isolated cancelled phi group, long descender and no secure foot; lowercase preferred.',
'05_deleted_formulas':'Repeated family-prime equation with two p stems; lower operators one p; low left remnant and covered right subscript retained.',
'06_left_note':'Rotated -15 degrees; capital Ainsi; uncertain mutuellement; short rightward pointer at line end.',
'07_brace':'Bar over F and double-headed two-shaft arrow clear; separate low point before family prime.',
'08_right_note':'No extra word before lower family prime; Stable singular preferred, capital Sup.; underline and open enclosure arms recorded.',
'09_middle_definitions':'Top cosupp two p, lower cosup one p; both supp two p; def labels without clear accents; double primes verified.',
'10_on_a':'vu preferred but four alternatives retained; Sup/Supp unresolved; terminal comma.',
'11_passage':'contient recovered under strike; two point-like marks after passage; une and singular sous-figure visible.',
'12_union':'Cancelled M-like group retained; Phi and H bars, short dotted i indices verified.',
'13_lower_operators':'All three lower cosup occurrences one p; overwritten M subscript; two previously omitted isolated low dots noticed.',
'14_lower_builder':'Crossed small loop before X preserved; tt/forall remains unresolved; Y membership and final brace inspected.',
'15_ramene':'ramené/revenu retained; section sign resolved as connected double loop.',
'16_saturee_heading':'Raised family zero is live; underline ends before overwritten family; parenthetical p. r. à follows second cosupport.',
'17_saturee_sentence':'Second saturée accent not secure; raised M0; son support has no co prefix.',
'18_mutuellement_par':'Central mutuellement cluster still worked; one par group with uncertain cancellation state.'
}
log=['# R1 independent inspection log — 156-4 scan 067','',
'Started timestamp is the first recorded session clock, after packet reads and before image views: 2026-11-20T09:53:10Z.',
'Read only assignment, brief v03, assigned packet metadata/C/H/conventions/preamble/context, and supplied notation snapshot. No other reader, page, source, OCR, web research or compiler was used.',
'',f'1. Viewed whole once: {W}. No transformation; layout, number 66, top additions, cancellation block, brace and marginalia, lower definitions and bottom formulas inventoried.',
f'2. Viewed half a once: {A}. No transformation; read every top-half row and both marginal notes against C and H.',
f'3. Viewed half b once: {B}. No transformation; read the overlap and every remaining lower row against C and H.',
'Initial three view timestamps were not individually recorded; all preceded the clock reading 2026-11-20T09:54:32Z. Neither half was displayed again or enlarged as a whole.',
'', 'All crops were made once by make_crops.py from the supplied halves. Autocontrast, LANCZOS enlargement, and UnsharpMask(radius=1.2, percent=115, threshold=3) were applied; only crop 06 was rotated (-15 degrees, BICUBIC, expanded canvas). JPEG quality 94. Original bounding boxes below are on the named half. No crop was remade or re-viewed.', '']
batch_times=['09:54:57','09:55:26','09:55:57','09:56:17','09:56:48','09:57:28']
for i,c in enumerate(crops):
    stem=Path(c['path']).stem
    log.append(f"{i+4}. Viewed {c['path']}; source {c['source']}; original bbox {c['bbox']}; scale {c['scale']}; rotation {c['rotation']} degrees. {viewnotes[stem]} View included in the batch ending at the recorded UTC clock 2026-11-20T{batch_times[i//3]}Z.")
log += ['', 'At most three crop images were emitted per result. All eighteen were visibly returned; no image output was truncated. No additional full-page or half-page view occurred.', 'After viewing, reading.tex and report.json were prepared. Structural checks only; no mathematical theorem was proved and no LaTeX compiler was invoked.']
(O/'inspection_log.md').write_text('\n\n'.join(log)+'\n')

report=dict(
reader='R1',cote='156-4',scan='67',brief_version='v03',started_utc='2026-11-20T09:53:10Z',finished_utc='2026-11-20T10:07:35Z',
image_views=[W,A,B],reading_file=str(O/'reading.tex'),differences=diff,c_doubts=cd,inventory=inventory,remaining_doubts=remaining,notation=notation,
abbreviations=[dict(form='cosup',expansion='cosupport'),dict(form='cosupp',expansion='cosupport'),dict(form='supp',expansion='support'),dict(form='def',expansion='définition'),dict(form='NB',expansion='nota bene'),dict(form='Sup.',expansion='supremum'),dict(form='Sup',expansion='supremum'),dict(form='p. r. à',expansion='par rapport à'),dict(form='tt',expansion='tout (only if tt is the correct glyph reading)')],
notes=dict(summary='Handwritten subject notes, manuscript page 66. Cosupport definitions, a cancelled draft, a live mutual-determination brace with two marginal annotations, double cosupport/support definitions, reduction to M, and definitions of saturated parts. Raised labels and distinct drawn connectors are included; unresolved letter and cancellation states remain marked.',math_reading_decisions='The potentially consequential loci were inspected directly: first H_i relation is \\vdash-like, the lower definition says support without co, and the bottom set condition has barred F. The expectation of repeating cosupport prompted attention to the second saturated definition, but the visible initial s and absence of co decided the transcription. No inference from a theorem was used to repair the wording. No mathematical validation or proof was performed.',author_checks='The author cancels the initial Donc paragraph and its formula rows, cancels contient Phi, overwrites two operator subscripts and two M-like symbols, and adds the raised inclusion, third equality, F_0 and M_0. These visible revisions are transcription evidence only, not external verification of the mathematics.',title_dates_pagination='Visible manuscript number 66 at top centre; scan 67 retained. No title, date, archive page number, or page-count statement is visible.'),
check_events=[],crops=crops,inspection_log=str(O/'inspection_log.md'),
workflow_feedback=['The fixed report schema omits bbox_image although the clarification requires it; this report supplies both bbox_image and source on every locus.','The one-crop rule can leave short punctuation or cancellation states unresolved; these are reported rather than re-cropped.'])
(O/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(differences=len(diff),c_doubts=len(cd),context_rows=len(context_rows),inventory=len(inventory),remaining_doubts=len(remaining),crops=len(crops)),indent=2))
