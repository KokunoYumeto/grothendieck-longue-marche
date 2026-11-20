from pathlib import Path
import json, datetime
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_070/R1')
packet=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_070')
source='/workspace/scratch/6644f30583f9/source/SP52_CW_156-4+156-6_scans/J156-4-09_156-4_scan070.jpg'
a=source.replace('.jpg','_a.jpg'); b=source.replace('.jpg','_b.jpg')
C=(packet/'C.tex').read_text(); H=(packet/'H.tex').read_text(); R=(out/'reading.tex').read_text()
crops=json.loads((out/'crop_manifest.json').read_text())
cm={int(Path(x['path']).stem[:2]):x for x in crops}
diffs=[]
def D(location,c,h,reading,scan_shows,confidence,kind,marked_in_h,change_c,change_h,crop=None,bbox=None,math_consequential=False,bbox_image=None):
    if crop is not None:
        row=cm[crop]
        cp=row['path']; bi=row['source']; bb=bbox or row['bbox']
    else:
        cp=None; bi=bbox_image or source; bb=bbox
    diffs.append(dict(id=f'R1-D{len(diffs)+1:02}',location=location,c=c,h=h,reading=reading,scan_shows=scan_shows,confidence=confidence,kind=kind,marked_in_h=marked_in_h,change_c=change_c,change_h=change_h,crop=cp,bbox=bb,bbox_image=bi,math_consequential=math_consequential))
D('Opening, rel',r'rel',r'rel.',r'rel','The l ends with its descending return; the space before d’ordre contains no separate stop.','high','other','no',False,True,bbox=[880,150,1030,250],bbox_image=a)
D('Opening order relation',r'\unsure{\preceq|\leqslant}',r'\preccurlyeq',r'\preceq','The lower detached stroke bends down at the right; the upper angle is also bowed. This is distinct from the straight final ≤ after avec. H’s bowed-order macro is treated as equivalent notation, not a separate difference.','high','misread symbol or index','no',True,False,crop=1,bbox=[1270,163,1358,233],math_consequential=True)
D('After (subdivision)',r'(subdivision),',r'(subdivision)',r'(subdivision),','A detached hooked comma stands below the closing parenthesis at the extreme right.','high','omission','no',False,True,crop=1,bbox=[1372,160,1670,278])
D('First paragraph, très/trs',r'\unsure{très|trs}',r'très',r'\unsure{très|trs}','A short raised mark follows the t/r group; a separate e is not securely distinguishable from the reduced central stroke. The spelling doubt is retained.','medium','other','no',False,True,crop=1,bbox=[647,247,764,326])
D('First paragraph, Il n’y aura',r'\unsure{aura}',r'a',r'aura','After n’y there are two surviving groups, au and ra, with the latter extending substantially farther right than a single a.','high','misread word','no',True,True,crop=1,bbox=[1388,260,1602,321])
D('Deleted noun after de deux',r'\deleted{\unsure{éléments|élémen}}',r'\struck{\ill{}}',r'\deleted{\unsure{éléments|élémen}}','Opening é/l and another tall stem remain beneath the horizontal strike; the end is obscured. The ink supports a partial noun reading but not a certain ending.','medium','readable ink left as \\ill{}','yes',False,True,crop=2,bbox=[1220,400,1535,486])
D('Live replacement noun before raised formula',r'figures',r'',r'figures','The live word figures is on the baseline below the deleted noun, with a long descending f and looped g.','high','omission','no',False,True,crop=2,bbox=[260,524,473,619])
D('Raised formula over figures and the following word',r'\inserted{$F\prime,F\prime\prime\preceq-$}',r'\add{$F\prime$, $F\prime\prime$} \struck{$\preccurlyeq$}',r'\inserted{$F\prime,F\prime\prime\unsure{\deleted{\preceq}|\preceq}-$}','The F pair has one and two short high ticks. Farther right the small relation is heavily retraced or struck, and a separate short horizontal dash follows it. Cancellation of the relation is plausible but not settled. The whole formula occupies the raised line.','low','deletion state (struck given live or live given struck)','yes',True,True,crop=2,bbox=[314,486,591,556],math_consequential=True)
D('Word after figures / raised formula',r'\unsure{en général|en position}',r'toujours',r'\unsure{toujours}','The right group has a clear descending j followed by a rounded o and low urs-like strokes. The left group is crossed by a long oblique stroke and is reduced; toujours is a much closer reading than général or position, but the whole word is left uncertain.','medium','misread word','no',True,True,crop=2,bbox=[481,508,821,598],math_consequential=True)
D('Group before Subdivisions',r'\unsure{(i.e.|liée.|lire.}',r'(i.e.',r'\unsure{(i.e.|liée.}','An open curve begins the group, followed by a high point and a small e-like loop, with a detached terminal point. The curve could belong to a parenthesis or a cursive initial; no convincing r is isolated.','medium','other','no',True,True,crop=2,bbox=[905,507,1053,569])
D('Capital at Subdivisions',r'Subdivisions',r'subdivisions',r'Subdivisions','The initial has the tall angular upper sweep of a capital S, unlike the small s strokes elsewhere in the word.','high','misread word','no',False,True,crop=2,bbox=[1088,482,1450,558])
D('Repeated-word mark in d’une = figure',r'\unsure{=|même}',r'même',r'$=$','There are two short horizontal strokes, joined at the left; no letters of même are present.','high','misread symbol or index','no',True,True,crop=2,bbox=[441,610,533,671])
D('After figure F in first paragraph',r'$F$,',r'$F$),',r'$F$,','The F is followed by a single low comma. The intervening space does not contain a closing parenthesis.','high','text not on the page','no',False,True,crop=2,bbox=[880,576,1010,674])
D('Second paragraph, deux subdivision',r'deux subdivision',r'deux subdivisions',r'deux subdivision','The ending is a long low n sweep without a distinct following s.','high','abbreviation expanded or spelling modernised','no',False,True,crop=3,bbox=[780,763,1393,838])
D('Second named subdivision in paragraph 2',r'F\prime,\unsure{F\prime\prime\prime|F\prime\prime}',r'F\prime,F\prime\prime',r'F\prime,F\prime\prime\prime','Three separate short high dark strokes follow the second F; the first is somewhat taller. The lower node in the diagram separately has two.','high','misread symbol or index','no',True,True,crop=3,bbox=[1420,751,1598,839],math_consequential=True)
D('Overwritten underlined adjective',r'\uline{comp\deleted{\unsure{ati|atib}}\unsure{ara|ati|ata}bles}',r'\emph{\uncertain{compatibles}}',r'\uline{comp\unsure{\deleted{ati}ara|\deleted{atib}ara|ata|ati}bles}','One word-sized group begins comp and ends bles. Its middle contains retraced bowls, a tall crossed stem and a separate high point. Neither the final middle nor the complete extent of an older ati/atib layer is settled. The alternatives preserve one word, rather than inventing a second complete deleted word.','low','deletion state (struck given live or live given struck)','yes',True,True,crop=3,bbox=[633,856,1007,965],math_consequential=True)
D('Cancelled phrase following the adjective',r'\deleted{\unsure{on dit|c.à.d.} que \unsure{sub}}',r'\struck{quand et que seulement}',r'\deleted{\unsure{quand et que} \unsure{seul|sub|seulement}}','The first cancelled run has a long d-like stem and a following small crossed group before a clear descending q. This favours quand et que over C’s first groups. The last compact group has a tall final stroke but its compressed interior does not settle seul/sub/seulement.','low','misread word','no',True,True,crop=3,bbox=[1050,840,1622,950])
D('Quotation marks around compatibles',r"``compatibles''",r'« compatibles »',r"``compatibles''",'Two small high opening ticks and two closing ticks surround the word; no angular guillemets are drawn.','high','other','no',False,True,bbox=[795,943,1220,1045],bbox_image=a)
D('Parenthesis, vu que',r'vu que',r'car le',r'vu que le','The relevant run has the low v/u of vu followed by a descending q of que and then le. H’s car replaces vu que, while its following le remains.','high','misread word','no',False,True,bbox=[1310,944,1634,1049],bbox_image=a)
# Full diagram scopes keep geometry and worked-stroke differences together.
cdiag=C[C.index('\\diagram{'):C.index('% slanted')].strip()
rdiag=R[R.index('\\diagram{'):R.index('% slanted')].strip()
hdiag=r'$F\prime\prime\prime \preccurlyeq F\prime \preccurlyeq F$, \ $F\prime\prime\prime \preccurlyeq F\prime\prime \preccurlyeq$'
D('Small diagram beside the definition',cdiag,hdiag,rdiag,'The left node has three primes, the upper node one, the lower node two, and the right node none. The right F is level with the upper F′, rather than at the middle row. Four relation marks and no connecting lines are visible. The upper-right mark has a thin additional upper arm: an entire older ≤ or ≺ cannot be recovered with confidence. The drawn label preserves those strokes with uncertainty. H’s linear chains lose the shared right node and placement.','high','drawing or diagram','yes',True,True,crop=4,math_consequential=False)
D('Oblique middle note, H unreadable run',r'renforcer encore cette condition sur',r'\ill{} \ill{} \ill{}',r'renforcer encore cette condition sur','After rotation, the f and tall stems of renforcer, the second encore, the two t stems of cette, condition, and the separate sur are legible across three short lines. These words precede the already-read les contrées modérées.','high','readable ink left as \\ill{}','yes',False,True,crop=5,bbox=[22,1180,474,1595])
D('Definition, contrée and its underline',r'\uuline{\unsure{contrée|contrie}}',r'contrée',r'\uuline{\unsure{contrée|contrie}}','Two separate rules run under the word. After tr the small upright and detached mark do not securely distinguish a reduced accented e from i.','medium','other','no',False,True,crop=6,bbox=[1383,1192,1625,1280])
D('Definition, modérée underline',r'\uuline{modérée}',r'\emph{modérée}',r'\uuline{modérée}','Two complete, separated underline strokes are visible. H’s single emphasis does not encode the doubling.','high','other','no',False,True,crop=6,bbox=[935,1273,1259,1384])
D('Definition, subdivision spelling and state',r'subdivisions',r'\add{subdivisions}',r'subdivision','The word is on the ordinary continuation line, with no insertion leader. Its final n has a long exit but no distinct following s.','high','insertion or placement','no',True,True,crop=7,bbox=[283,1388,700,1473])
D('Definition, rewritten d’un(e) and repeated-word mark',r"\deleted{\unsure{d'un}} \unsure{d'une =|d'un =}",r'\struck{\ill{}} de',r"\unsure{\deleted{d'}d'|d'}\unsure{une|un} $=$",'There is one densely worked d′-sized initial group, followed by a low un(e) run. A complete earlier d’un is not separately recoverable. The extra initial strokes may preserve an older d′; that state and the terminal e remain open. Two horizontal strokes follow the word before F.','low','deletion state (struck given live or live given struck)','yes',True,True,crop=7,bbox=[751,1368,1111,1452])
D('Definition, final comparables certainty',r'comparables',r'\uncertain{comparables}',r'comparables','The c/o, descending p, middle ara, and separate b/l stems are legible; this occurrence is not the overwritten adjective above.','high','other','yes',False,True,crop=7,bbox=[268,1481,725,1555])
D('Cancelled clause after definition',r'\deleted{Dans le cas qui vient,}',r'\struck{Dans le cas général,}',r'\deleted{Dans le cas qui vient,}','A descending q and high dot followed by the short vient run occur after cas. The cancellation is a single long horizontal line; the final low comma remains visible.','high','misread word','no',False,True,crop=7,bbox=[787,1455,1595,1549])
D('Cancelled on a and following stop',r'\deleted{on a}.',r'',r'\deleted{on a}\unsure{..|:}','The small on a is struck. Two detached dots stand to its right, the second slightly lower; the mark is not safely reduced to a single full stop.','medium','omission','no',True,True,crop=8,bbox=[264,1600,501,1664])
D('Cancelled axiom label beside start of lower paragraph',r'\deleted{\uline{C5}}',r'\struck{\ill{}}',r'\deleted{\uline{C5}}','C and 5 are visible inside diagonal cancelling strokes; the underline remains. The label is physically below the first line, left of aucune.','high','readable ink left as \\ill{}','yes',False,True,crop=8,bbox=[278,1642,464,1760])
D('H extra deletion after donner',r'donner aucune',r'donner \struck{\ill{}} aucune',r'donner aucune','No intervening deleted word is visible after donner. The next line begins aucune; the cancelled C5 is to its left and is already accounted for separately.','high','text not on the page','yes',False,True,crop=8,bbox=[270,1549,1625,1790])
D('Lower paragraph, seul',r'seul.',r'seule.',r'seul.','A final tall l returns to the baseline, followed by a separate point; there is no terminal e.','high','abbreviation expanded or spelling modernised','no',False,True,crop=9,bbox=[505,1804,668,1858])
D('Lower paragraph, ses/les relations',r'ses relations',r'les relations',r'\unsure{ses|les} relations','The first short group is heavily inked at its opening and reduced at its end. A short loop favours ses, but an l-like opening remains possible.','medium','misread word','no',True,True,crop=9,bbox=[879,1867,1260,1925])
D('Lower paragraph, placement of avec',r'avec',r'\add{avec}',r'avec','Avec follows relations on the same rising baseline, without a caret or separate insertion leader.','high','insertion or placement','no',False,True,crop=9,bbox=[1303,1849,1436,1919])
D('C5, abbreviation before figure',r'\unsure{tte}',r'toute',r'tte','Two tall joined stems carry a shared bar, followed by a small open e. There is no ou sequence between them.','high','abbreviation expanded or spelling modernised','no',True,True,crop=10,bbox=[1421,1985,1541,2080])
D('NB corrected letter before equals',r'\deleted{\unsure{F}}\unsure{G|F}',r'G',r'\deleted{F}G','A stem and two F arms remain inside a broader open rounded G return. The two layers occupy one glyph position.','medium','deletion state (struck given live or live given struck)','no',True,True,crop=11,bbox=[728,2270,790,2336],math_consequential=True)
D('NB letter after equals',r'\unsure{X|x}',r'X',r'\unsure{X|x}','The two diagonals cross over a small loop, but the reduced size and retracing do not securely settle upper versus lower case. No subscript is present.','medium','other','no',False,True,crop=11,bbox=[787,2273,828,2335],math_consequential=False)
D('NB ambient M alphabet',r'M',r'\mathcal{M}',r'M','The letter is a compact ordinary peaked M with no separate calligraphic flourish or second alphabetic stem.','high','misread symbol or index','no',False,True,crop=11,bbox=[839,2268,889,2334],math_consequential=False)
D('Lower slanted note, first word',r'\unsure{Reporter|Rejeter}',r'\ill{}',r'\unsure{Reporter|reporter|Rejeter|rejeter}','The descending middle stroke and following low run favour Reporter, but the reduced middle and opening swash leave rejeter and initial case open. The crop contains the complete first word.','medium','readable ink left as \\ill{}','yes',True,True,crop=12,bbox=[34,2011,202,2162])
D('Lower slanted note, C7 index and punctuation',r'C7_0',r'C7,',r'C7_0','A separate small closed oval is at the foot of the 7. It is retained as subscript 0. No additional comma after that index is isolated; the next small group is ces on a raised line.','high','misread symbol or index','no',False,True,crop=12,bbox=[140,2079,220,2178],math_consequential=True)
D('Lower slanted note, phrase after C7 index',r'\unsure{ces|mes} axiomes de \uline{disjonction}',r'\ill{} des disjonctions',r'ces axiomes de \uline{disjonction}','Three small groups read ces above the axiomes line. Axiomes has the x, dotted i and low m sequence. The next line reads de followed by singular disjonction, with an underline under that final word. H’s one unreadable placeholder and altered ending are handled in this single nonoverlapping scope.','high','readable ink left as \\ill{}','yes',True,True,crop=12,bbox=[28,2015,301,2327])
bars=r'\draw[line width=0.6pt] (-0.36,-0.48) .. controls (-0.30,-1.2) and (-0.42,-2.1) .. (-0.28,-2.66);'+'\n'+r'\draw[line width=0.6pt] (-0.13,-0.47) .. controls (-0.07,-1.2) and (-0.16,-2.2) .. (-0.05,-2.65);'
D('Two vertical emphasis strokes beside C5',r'',r'\note{double trait vertical en marge de C5}',bars,'Two distinct long slightly bowed vertical strokes run down the left of C5’s body and cross the far end of the oblique note. They are drawn in the same local TikZ group as that note and the axiom. H describes them editorially, but does not reproduce them.','high','drawing or diagram','yes',True,True,crop=12,bbox=[248,2090,303,2320])
# Normalize quotations to literal witness prime syntax rather than an equivalent \prime spelling.
for d in diffs:
    for k in ['c','h','reading']:
        d[k]=d[k].replace('\\prime',"'")
# Correct the scope of the vu/car quotation to include the same following le in each witness.
diffs[18]['c']='vu que le'
diffs[14]['c']="$F',\\unsure{F'''|F''}$"
diffs[14]['h']="$F'$, $F''$"
diffs[14]['reading']="$F',F'''$"
diffs[25]['crop']=None
diffs[25]['bbox_image']=b
diffs[25]['bbox']=[268,382,725,480]
diffs[25]['scan_shows']='The complete lower half shows the c/o, descending p, middle ara, and b/l stems clearly. Crop 07 cuts the extreme lower p descender near original y=1555, so this certainty decision is anchored to the supplied lower half, not to an absence at that crop boundary.'
diffs[27]['h']=r'\struck{\ill{}}'
diffs[27]['kind']='readable ink left as \\ill{}'
diffs[27]['marked_in_h']='yes'
diffs[27]['location']='Cancelled on a before Je: first of H’s two lower-paragraph struck placeholders'
diffs[27]['scan_shows']='The small on a is struck before Je on the same manuscript line. This maps H’s first struck unreadable placeholder here. Two detached dots stand to the right, the second slightly lower; the stop is not safely reduced to a single period.'
diffs[28]['location']='Cancelled C5 before aucune: second of H’s two lower-paragraph struck placeholders'
diffs[28]['scan_shows']='C and 5 are visible inside diagonal cancelling strokes, with an underline. This label stands below the Je ne saurais donner line, immediately left/above aucune, and maps H’s second struck unreadable placeholder.'
diffs[29]['location']='Physical reading order of cancelled C5 around Je ne saurais donner / aucune'
diffs[29]['c']=r'\deleted{\uline{C5}} Je ne saurais donner aucune'
diffs[29]['h']=r'Je ne saurais donner \struck{\ill{}} aucune'
diffs[29]['reading']=r'Je ne saurais donner \deleted{\uline{C5}} aucune'
diffs[29]['scan_shows']='The cancelled C5 is below the first line Je ne saurais donner and before the next line aucune. The fragment therefore places it at that physical reading-order position. H’s second placeholder occupies this position; it is not an extra deleted word. Deciphering that placeholder is recorded separately in D29.'
diffs[29]['kind']='insertion or placement'
diffs[29]['change_c']=True
diffs[29]['change_h']=False


cd=[]
def Q(location,c,reading,status,scan_shows,crop=None,bbox=None,bbox_image=None,context_checks=None):
    cp=cm[crop]['path'] if crop else None
    bi=cm[crop]['source'] if crop else (bbox_image or source)
    bb=bbox or (cm[crop]['bbox'] if crop else None)
    cd.append(dict(location=location,c=c,reading=reading,status=status,scan_shows=scan_shows,crop=cp,bbox=bb,bbox_image=bi,context_checks=context_checks or []))
Q('Opening bowed order relation',r'\unsure{\preceq|\leqslant}',r'\preceq','resolved','The lower stroke is curved down at the right, unlike the straight ≤ after avec.',1,[1270,163,1358,233],context_checks=['C_context rows: first line relation; bent upper angle over curved lower stroke'])
Q('First paragraph, très/trs',r'\unsure{très|trs}',r'\unsure{très|trs}','retained','The reduced central strokes and raised mark do not isolate a certain e.',1,[647,247,764,326])
Q('Il n’y aura',r'\unsure{aura}',r'aura','resolved','The visible au and ra groups cannot be reduced to a lone a.',1,[1388,260,1602,321])
Q('Deleted noun after de deux',r'\deleted{\unsure{éléments|élémen}}',r'\deleted{\unsure{éléments|élémen}}','retained','The final letters remain under the cancellation line.',2,[1220,400,1535,486])
Q('Word after figures',r'\unsure{en général|en position}',r'\unsure{toujours}','revised','A descending j, o loop and low urs-like run favour toujours; the initial portion remains crowded.',2,[481,508,821,598])
Q('Group before Subdivisions',r'\unsure{(i.e.|liée.|lire.}',r'\unsure{(i.e.|liée.}','revised','The open curve, high point and e-like loop permit (i.e. or liée.; no independent r is established.',2,[905,507,1053,569])
Q('First repeated-word mark',r'\unsure{=|même}',r'$=$','resolved','Two short horizontal strokes stand between une and figure; there are no letter-shaped groups.',2,[441,610,533,671],context_checks=['C_context repeated-word mark before figure F; upper paragraph repeated-word check'])
Q('Second named subdivision in paragraph 2',r"F',\unsure{F'''|F''}",r"F',F'''",'resolved','Three distinct raised ticks follow the second F.',3,[1420,751,1598,839])
Q('Underlined adjective: proposed older ati/atib layer',r'\deleted{\unsure{ati|atib}}',r'\unsure{\deleted{ati}ara|\deleted{atib}ara|ata|ati}','revised','Only one worked word exists. A tall crossed stem and point could be old ati/atib, but separating a complete old suffix from the live middle is uncertain.',3,[633,856,1007,965])
Q('Underlined adjective: final ara/ati/ata middle',r'\unsure{ara|ati|ata}',r'\unsure{\deleted{ati}ara|\deleted{atib}ara|ata|ati}','revised','Comparables remains the best first expansion of the strokes, but the middle is not settled; ata and ati are retained without a confidently separable older layer.',3,[633,856,1007,965])
Q('Cancelled phrase: first groups',r'\unsure{on dit|c.à.d.} que',r'\unsure{quand et que}','revised','The first run has a tall d-like end, a further short crossed group, then a descending q; quand et que fits the visible groups better.',3,[1050,840,1392,950])
Q('Cancelled phrase: last group',r'\unsure{sub}',r'\unsure{seul|sub|seulement}','revised','The short run ends in a tall stroke. The cancellation prevents resolving its interior or expansion.',3,[1405,840,1622,921])
Q('Worked upper-right comparison in diagram',r'\deleted{\unsure{\leq|\prec}}\preceq','Uncertain TikZ rendering of the four visible strokes in the upper-right relation','revised','A thin extra rising arm is certain. It does not alone establish an entire cancelled ≤ or ≺; the label is reproduced graphically with a doubt mark.',4,[527,1188,619,1250])
Q('Definition, contrée/contrie',r'\uuline{\unsure{contrée|contrie}}',r'\uuline{\unsure{contrée|contrie}}','retained','The small upright after tr and detached mark can be reduced é or i. Both underlines are secure.',6,[1383,1192,1625,1280])
Q('Definition, proposed deleted d’un',r"\deleted{\unsure{d'un}}",r"\unsure{\deleted{d'}d'|d'}",'revised','The overworked group occupies only the initial d′ position. A whole old d’un is not independently visible; an older d′ is possible, not asserted.',7,[751,1368,865,1452])
Q('Definition, live d’une = / d’un =',r"\unsure{d'une =|d'un =}",r"\unsure{\deleted{d'}d'|d'}\unsure{une|un} $=$",'revised','The ending un(e) remains reduced. The following two-stroke equality/repetition mark is secure.',7,[751,1368,1111,1452])
Q('Lower marginal instruction, Reporter/Rejeter',r'\unsure{Reporter|Rejeter}',r'\unsure{Reporter|reporter|Rejeter|rejeter}','revised','Reporter remains favoured, but the middle and opening case are not settled. Entire word and baseline are framed.',12,[34,2011,202,2162])
Q('Lower marginal instruction, ces/mes',r'\unsure{ces|mes}',r'ces','resolved','The short first curve is followed by separate low e/s shapes. It is raised beside the C6/C7 line.',12,[189,1997,342,2085])
Q('C5, tte',r'\unsure{tte}',r'tte','resolved','Two tall joined stems and a small final e are visible; no ou is present.',10,[1421,1985,1541,2080])
Q('NB older letter',r'\deleted{\unsure{F}}',r'\deleted{F}','resolved','A straight stem and the two F arms remain within the later rounded outer form.',11,[728,2270,790,2336])
Q('NB final letter',r'\unsure{G|F}',r'G','resolved','A broader open rounded return and lower rightward stroke make the live form G.',11,[728,2270,790,2336])
Q('NB X/x',r'\unsure{X|x}',r'\unsure{X|x}','retained','The crossed diagonals are sure, but reduced size and retracing leave case open; no subscript is visible.',11,[787,2273,828,2335])
Q('C_context explicit diagram nodes and primes',r"F''',F',F'',F",r"F''',F',F'',F",'resolved','The left/upper/lower/right prime counts are 3/1/2/0. The right F is level with the upper F′, not centred vertically. Four signs are present without edge lines.',4,[350,1180,661,1349],context_checks=['positions of F and primes'])
Q('C_context explicit bowed signs across page',r'\preceq',r'\preceq','resolved','Opening, diagram, lower paragraph and C5 all use the bent/curved order sign. The final relation after avec is straight ≤. Opening and diagram are cropped; lower paragraph is in crop 08; C5 is clear in the lower half.',4,[350,1180,661,1349],context_checks=['first line; diamond; C5 order-sign check'])
Q('C_context explicit C5 G, F′, X, ssi',r"G,F',X,\mathrm{ssi}",r"G,F',\unsure{X|x},\mathrm{ssi}",'retained','The body G letters are plain rounded G; F′ has one tick; ssi is the compact three-letter abbreviation. In NB, X/x retains a local case doubt, while the two-stroke equals, membership and plain M are secure.',11,[305,2140,1645,2354],context_checks=['plain G, F′ and subscript-free X; equivalence abbreviation'])
Q('C_context contrées in middle slanted note',r'contrées',r'contrées','resolved','The rotated note has the plural ending and raised accent; the separate main-text occurrence remains uncertain locally.',5,[60,1331,345,1628],context_checks=['left note and definition at right, contrée/contrie'])
Q('C_context first deux subdivision ending',r'deux subdivision',r'deux subdivision','resolved','The first occurrence ends in n without a separate s. The definition’s second occurrence is likewise singular-looking and is recorded separately as a difference from C.',3,[780,763,1393,838],context_checks=['after On dit que deux'])
Q('C_context overwritten adjective versus quoted word',r'comp…bles; compatibles',r"\uline{comp\unsure{\deleted{ati}ara|\deleted{atib}ara|ata|ati}bles}; ``compatibles''",'retained','The parenthetical quoted word compatibles is clear. It does not decide the overwritten adjective’s letters; the latter retains its own alternatives.',3,[633,856,1200,1030],context_checks=['underlined adjective and parenthesis'])

inventory=[]
def I(element,kind,position,first):
    inventory.append(dict(element=element,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand='his hand',transcribed='yes'))
I('I01 manuscript page number','text','Top centre','69')
I('I02 opening paragraph','text','Upper body, seven manuscript lines','J’en viens à la rel d’ordre')
I('I03 cancelled noun','deletion','Opening paragraph after de deux','éléments / élémen')
I('I04 raised formula','insertion','Above figures and the next word',"F′, F″; worked order sign; dash")
I('I05 possibly cancelled small relation','deletion','Raised formula to the right of the two F labels','≼ (deletion state uncertain, retained in place)')
I('I06 comparability paragraph','text','Second body paragraph','On dit que deux subdivision')
I('I07 worked adjective middle','deletion','Inside underlined comp…bles','ati/atib possible older strokes; state alternatives retained')
I('I08 cancelled clause after adjective','deletion','End of second line of paragraph 2','quand et que … (uncertain)')
I('I09 subdivision diagram','diagram','Middle left, beside definition','F‴; upper F′; lower F″; shared right F; four relation marks')
I('I10 extra arm in worked diagram relation','drawing','Upper-right diagram relation','Thin additional rising stroke, reproduced with the other relation strokes')
I('I11 oblique middle note','margin note','Left margin beside diagram/definition, rising to right','On sera amené à renforcer encore cette condition')
I('I12 definition paragraph','text','Middle right, continuing across body','On dit que la contrée est modérée')
I('I13 overwritten d′ group','deletion','Definition after subdivision','Possible earlier d′ under final d′; one word position')
I('I14 cancelled clause after definition','deletion','Right of definition’s last line','Dans le cas qui vient,')
I('I15 cancelled short clause','deletion','Left below definition','on a')
I('I16 two-point stop','text','Immediately right of cancelled on a','.. / :')
I('I17 cancelled C5 label','deletion','Left of aucune, below the first line Je ne saurais donner','Underlined C5 with diagonal cancellation')
I('I18 lower relation paragraph','text','Lower body before live C5','Je ne saurais donner aucune propriété particulière')
I('I19 cancelled tout','deletion','Lower relation paragraph before seul','tout')
I('I20 live C5 axiom','text','Bottom body, beside two vertical strokes','C5 Soit F′ ≼ F. Alors pour tte figure G')
I('I21 bracketed NB','text','Bottom two lines of C5','[NB Il suffit de le poser pour …, à cause de C3]')
I('I22 overwritten NB letter','deletion','Before equals in the NB formula','F underneath live G')
I('I23 lower oblique note','margin note','Bottom left, beside C5','Reporter après C6, C7₀ ces axiomes de disjonction')
I('I24 C5 emphasis strokes','drawing','Two long vertical strokes at left of C5’s body','Two slightly bowed parallel strokes crossing far end of note')

remaining=[
 dict(location='First paragraph, très/trs',reading=r'\unsure{très|trs}',alternatives=['très','trs'],confidence='medium',reason='Reduced central e and raised mark do not decide full spelling.'),
 dict(location='Deleted noun after deux',reading=r'\deleted{\unsure{éléments|élémen}}',alternatives=['éléments','élémen'],confidence='medium',reason='The ending lies beneath the cancellation stroke.'),
 dict(location='Raised small relation after F pair',reading=r'\unsure{\deleted{\preceq}|\preceq}',alternatives=[r'\deleted{\preceq}',r'\preceq'],confidence='low',reason='Dense short overtraces may cancel the relation or retrace it.'),
 dict(location='Word following figures',reading=r'\unsure{toujours}',alternatives=['toujours'],confidence='medium',reason='The j and following low run are legible, but the initial tou portion is crowded by an oblique stroke.'),
 dict(location='Group before Subdivisions',reading=r'\unsure{(i.e.|liée.}',alternatives=['(i.e.','liée.'],confidence='medium',reason='An open initial curve could be a parenthesis or a cursive initial.'),
 dict(location='Underlined adjective',reading=r'\uline{comp\unsure{\deleted{ati}ara|\deleted{atib}ara|ata|ati}bles}',alternatives=[r'comp\deleted{ati}arables',r'comp\deleted{atib}arables','compatables','compatibles'],confidence='low',reason='The middle has multiple superposed bowls, tall strokes and a point; the final letters and exact older layer are not separately certain.'),
 dict(location='Cancelled phrase, first groups',reading=r'\deleted{\unsure{quand et que}}',alternatives=['quand et que'],confidence='low',reason='The cancellation obscures much of the first run; d-like, crossed and q-descending groups favour the reading.'),
 dict(location='Cancelled phrase, last group',reading=r'\deleted{\unsure{seul|sub|seulement}}',alternatives=['seul','sub','seulement'],confidence='low',reason='Short compact run and tall end are visible but interior strokes are obscured.'),
 dict(location='Diagram upper-right relation',reading='Doubt-marked TikZ drawing of the four visible relation strokes in reading.tex',alternatives=['A retraced upper arm of the live relation','An earlier overwritten ≤','An earlier overwritten ≺'],confidence='low',reason='The additional thin arm is visible; no complete earlier sign is recoverable. The final file draws the ink without asserting a whole deleted sign.'),
 dict(location='Definition, contrée/contrie',reading=r'\uuline{\unsure{contrée|contrie}}',alternatives=['contrée','contrie'],confidence='medium',reason='Small upright and detached mark after tr could be a reduced é or i.'),
 dict(location='Definition, corrected d’un(e)',reading=r"\unsure{\deleted{d'}d'|d'}\unsure{une|un}",alternatives=[r"\deleted{d'}d'une",r"\deleted{d'}d'un","d'une","d'un"],confidence='low',reason='One dense initial group may include old d′ strokes; terminal e is reduced. No separate full old d’un is asserted.'),
 dict(location='Stop after cancelled on a',reading=r'\unsure{..|:}',alternatives=['..',':'],confidence='medium',reason='Two detached dots are diagonally offset; neither a single period nor a standard vertical colon is secure.'),
 dict(location='Lower paragraph, ses/les relations',reading=r'\unsure{ses|les}',alternatives=['ses','les'],confidence='medium',reason='The initial of the short group is dark and retraced.'),
 dict(location='Lower slanted instruction, first word and case',reading=r'\unsure{Reporter|reporter|Rejeter|rejeter}',alternatives=['Reporter','reporter','Rejeter','rejeter'],confidence='medium',reason='The descending middle favours reporter, but the short strokes and initial swash leave the alternatives open.'),
 dict(location='NB letter after equals',reading=r'\unsure{X|x}',alternatives=['X','x'],confidence='medium',reason='The two diagonals are certain; letter case is not.'),
]
notation=[
 dict(sign='Bowed subdivision order',latex=r'\preceq',appearance='Left-pointing upper fork and a detached lower stroke both curve to the right.',location='Opening; diagram; lower paragraph; C5',alternatives=[]),
 dict(sign='Straight order relation',latex=r'\leq',appearance='Straight sloping upper stroke with straight lower bar.',location='After avec at end of lower paragraph',alternatives=[]),
 dict(sign='Plain figure letters and primes',latex=r"F',F'',F''',F",appearance='Straight F stems and arms; primes are separate short high ticks.',location='Raised formula, paragraph 2, diagram and C5',alternatives=[]),
 dict(sign='Literal repeated-word mark',latex='=',appearance='Two short horizontal traces, sometimes joined at left.',location='d’une = figure; definition before F',alternatives=[]),
 dict(sign='Worked small relation plus dash',latex=r'\unsure{\deleted{\preceq}|\preceq}-',appearance='Dense small angled/horizontal strokes followed by a detached short horizontal dash.',location='Raised formula in first paragraph',alternatives=['cancelled relation','retraced live relation']),
 dict(sign='Worked diagram relation',latex='TikZ label in the diagram',appearance='Bowed relation with a thin additional upper rising arm.',location='Between upper F′ and right F',alternatives=['retracing','overwritten ≤','overwritten ≺']),
 dict(sign='Corrected NB letter',latex=r'\deleted{F}G',appearance='F stem and two arms inside a later rounded open G return.',location='NB before equals',alternatives=[]),
 dict(sign='NB crossed letter',latex=r'\unsure{X|x}',appearance='Two crossing diagonals over a small loop; no subscript.',location='NB after equals',alternatives=['X','x']),
 dict(sign='Ambient letter',latex='M',appearance='Plain short peaked capital without calligraphic flourish.',location='NB after membership sign',alternatives=[]),
 dict(sign='Axiom index',latex='C7_0',appearance='Closed small oval at the foot/right of the seven.',location='Lower slanted note',alternatives=[]),
 dict(sign='Two-point stop',latex=r'\unsure{..|:}',appearance='Two small detached dots with slight diagonal offset.',location='After cancelled on a',alternatives=['..',':']),
 dict(sign='Equivalence abbreviation',latex='ssi',appearance='Compact three-letter run with two looped s strokes.',location='C5 main body',alternatives=[]),
]
notes=dict(
 summary='The page contrasts the subdivision order with the earlier straight order, defines comparability and modération, sketches four related figures, and states a disjunction axiom C5. Two slanted notes ask for a stronger condition and relocation of the disjunction axioms. Several corrections remain materially uncertain.',
 math_reading_decisions='The possible mismatch between the second figure named in paragraph 2 and the lower diagram node prompted a prime-count check: the paragraph has three ticks, while the lower diagram node has two. Neither was repaired. Comparing the bowed order sign with the visibly straight ≤ after avec prompted shape inspection. The diagram’s geometry and shared right F were taken from the ink. These were transcription checks, not proofs; no theorem was validated.',
 author_checks='The author writes « Je ne saurais donner aucune propriété particulière … seul » and separately says the condition will need strengthening. The lower note reads a still-uncertain Reporter/reporter/Rejeter instruction after C6, C7₀. No author proof-check mark is inferred from these statements.',
 title_dates_pagination='Manuscript page number 69 is visible at the top; scan 70 is retained. No title, date, separate cover, or archive sheet number was identified. C5 occurs once cancelled and once live/underlined. The page is ordinary handwritten text.'
)
views=[dict(order=1,path=source,kind='whole',transform='None; viewed once for layout'),dict(order=2,path=a,kind='half',transform='None; supplied full-resolution upper half viewed once'),dict(order=3,path=b,kind='half',transform='None; supplied full-resolution lower half viewed once')]
for i,cr in enumerate(crops,4):
    views.append(dict(order=i,path=cr['path'],kind='own tight crop',source=cr['source'],bbox=cr['bbox'],scale=cr['scale'],rotation=cr['rotation'],transform=cr['transform'],viewed=True))
evidence={
1:'Bowed opening relation; comma after closing parenthesis; no point after rel; retained très/trs; distinct au and ra groups.',
2:'Live figures; one/two raised F primes; densely worked relation plus dash; j-containing following word; open i.e./liée group; capital S; literal =; comma without closing parenthesis after F.',
3:'First subdivision is singular-looking; second F has three ticks; one overwritten underlined adjective; cancelled phrase uncertain; quoted compatibles and vu que clear.',
4:'Four nodes, prime counts 3/1/2/0; right F level with upper F′; four signs; thin extra upper arm in upper-right sign.',
5:'Entire note fits the source rectangle and is legible after rotation: On sera amené à renforcer encore cette condition sur les contrées modérées !',
6:'Both words doubly underlined; contrée/contrie retains local spelling doubt; modérée legible.',
7:'Second subdivision is also singular-looking; one dense d′ group, un(e), literal =; crossed Dans le cas qui vient and comma. The lower edge clips the extreme p descender in comparables near source y=1555; the full word was seen in the supplied lower half. No recrop was made.',
8:'Crossed on a before Je, followed by two points; cancelled underlined C5 below the donner line and before aucune. H’s two struck placeholders map to these two actual groups. Bowed relation also visible.',
9:'Crossed tout; seul without terminal e; initial of ses/les unresolved; avec is baseline; straight ≤ at end.',
10:'Two tall stems plus e establish tte; C5’s ssi and following elle are legible.',
11:'NB and underline; suffit de le poser pour; F under live G; X/x unresolved; membership and plain M; à cause de C3 and closing bracket.',
12:'Whole marginal baseline and line endings fit the crop; uncertain Reporter/reporter/Rejeter; C6, C7₀; raised ces; axiomes de disjonction with underline; both long vertical strokes fully present.'
}
for cr in crops:
    cr['viewed']=True
    cr['visible_evidence']=evidence[int(Path(cr['path']).stem[:2])]
report=dict(reader='R1',cote='156-4',scan='70',brief_version='v06',started_utc='2026-11-20T11:00:44Z',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),image_views=[source,a,b],reading_file=str(out/'reading.tex'),differences=diffs,c_doubts=cd,inventory=inventory,remaining_doubts=remaining,notation=notation,abbreviations=[dict(form='rel',expansion='relation'),dict(form='Sup',expansion='supremum'),dict(form='inf',expansion='infimum'),dict(form='tte',expansion='toute'),dict(form='ssi',expansion='si et seulement si'),dict(form='NB',expansion='nota bene'),dict(form='i.e. (uncertain reading)',expansion='id est')],notes=notes,check_events=[],crops=crops,inspection_log_file=str(out/'inspection_log.json'),workflow_feedback=['The available source has low spatial resolution at several overworked words; enlargement cannot separate strokes that share the same pixels. Retaining local uncertainty is necessary.','The brief asks for both exact ink-state preservation and a readable symbolic transcription of the upper-right worked relation. A doubt-marked TikZ stroke rendering avoids asserting an unrecoverable whole earlier glyph.'],h_editorial_notes_disposition=[dict(note='Bowed subdivision sign rendered preccurlyeq',disposition='Accepted as a graphical encoding convention; equivalent to the selected preceq here, and not an independent manuscript word.'),dict(note='Overwritten adjective to reread',disposition='Reread on own crop; uncertainty retained, not decided by the parenthetical word.'),dict(note='Oblique note with two chains, second final object not written',disposition='The four physical nodes are shared in a 2D layout. The right F is drawn once, and serves both paths.'),dict(note='Double vertical stroke by C5',disposition='Reproduced as two strokes in the local TikZ group; counted as a drawing difference, not as manuscript prose.')])
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
(out/'inspection_log.json').write_text(json.dumps(dict(reader='R1',scan='70',views=views,restrictions='Whole once; upper and lower supplied halves once each; each of 12 own crops viewed once. No OCR, external research, other-reader access, previous-page access, or LaTeX compilation. Source rectangles were not recropped after viewing.',framing='Both marginal notes are completely framed. Crop 07 clips the extreme lower p descender of comparables at original y≈1555; the whole word was already visible in the lower half and its certainty disposition cites that half. This framing limitation is disclosed rather than recropped. Other clipped neighbouring line fragments are not used for target absence claims.'),ensure_ascii=False,indent=2))
print(json.dumps(dict(differences=len(diffs),c_doubt_dispositions=len(cd),inventory=len(inventory),remaining_doubts=len(remaining),crops=len(crops),reading_file=str(out/'reading.tex'),report_file=str(out/'report.json')),ensure_ascii=False))
