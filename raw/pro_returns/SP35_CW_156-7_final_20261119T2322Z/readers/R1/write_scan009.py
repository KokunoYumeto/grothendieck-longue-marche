from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import json

base=Path('/workspace/scratch/2b715fe259c4')
out=base/'SP35_CW_156-7/readers/R1'
source=base/'source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan009.tex'
tex=source.read_text()
crops=json.loads((out/'scan009_crops.json').read_text())
cm={Path(c['file']).stem.removeprefix('scan009_'):c for c in crops}

def replace(old,new,count=1):
    global tex
    assert old in tex,old
    tex=tex.replace(old,new,count)

compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}'
replace(r'\deleted{\unsure{\parallel}}',r'\deleted{\parallel}')
replace(r'\unsure{L|\mathcal L}',r'L')
replace(r'\unsure{immédiat}',r'immédiat')
replace(r'\Longrightarrow Z\ll X,\,Z\ll Y',r"\Longrightarrow Z\ll X,\,\unsure{Z'|Z}\ll Y")
replace(r'\deleted{\unsure{impossible}}',r'\deleted{impossible}')
replace(r'F,\unsure{C|G}\in',r'F,C\in')
replace(r'avec $F\parallel G$. Alors $F\ll F$',r'avec $F\parallel\unsure{C|G}$. Alors $F\ll F$')
replace(r'\deleted{$\unsure{L}=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z$}',
        r'\deleted{$\unsure{L=\underset{Z\in\widetilde F\cap\widetilde G}{\mathrm{Sup}}\,Z}$}')
replace(r"$F'\ll F,G'\ll G$. Supposons",r"$F'\ll F,C'\ll G$. Supposons")
replace(r'\unsure{tt}',r'tt')
replace(r'\unsure{cf|Cf}',r'cf')
replace(r'\deleted{\unsure{p.}}',r'\deleted{p.}')
old_arrow=r'\unsure{\mathrel{\tikz[x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.35,.42) and (1.38,.23) .. (1.28,.2);}}|\Rightarrow}'
literal_arrow=r'\mathrel{\tikz[baseline=-.25ex,x=.55em,y=.45em,line cap=round]{\draw (0,.2)--(1.05,.2) (.1,.47)--(1.02,.47);\draw (1.12,.72)..controls(1.29,.58)and(1.36,.17)..(1.38,-.04)..controls(1.30,-.12)and(1.18,-.14)..(1.08,-.14);}}'
replace(old_arrow,literal_arrow)
replace(r'\unsure{en} $\Rightarrow$',r'en $\Rightarrow$')
# The lower compatibility glyph is retraced, without a recoverable earlier sign.
heavy_compat=r'\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em,line cap=round]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);\draw[line width=.95pt] (.14,.62)--(.85,.65)--(.13,.26)--(.9,.12) (.91,.96)--(.12,.34)--(.78,.31)--(.1,-.16);}}'
replace("F'_{L}"+compat+"G'_{L}","F'_{L}"+heavy_compat+"G'_{L}")
replace(r'\margin{\tikz[x=.5em,y=.5em]{\draw (0,0)--(0,4.25);}\enspace\uline{Critère}',r'\margin{\uline{Critère}')
replace(r'\node at (.77,1.16) {\scriptsize $\unsure{x|+}$};',r'\draw[line width=1.2pt] (.65,1.05)--(.83,1.28) (.65,1.27)--(.83,1.09);')
replace(r'\node at (-.10,.04) {$\unsure{X|x}$};',r'\draw[thick] (-.41,.25)--(.02,-.13) (-.43,-.15)--(.02,.29);')
replace(r'\node at (2.71,-.04) {$\unsure{X|Y}$};',r'\draw[line width=1pt] (2.47,.13)--(2.88,-.29) (2.44,-.34)--(2.94,.15);\draw[line width=1.6pt] (2.54,-.41)--(2.96,.08);')
hashshape=r'\mathrel{\tikz[x=.55em,y=.60em,line cap=round]{\draw (0,-.12)--(0,1) (.48,-.12)--(.48,1) (-.06,.30)--(.54,.47) (-.05,.51)--(.53,.65);}}'
replace(r'\unsure{'+hashshape+r'|\mathrel{\#}|\nparallel|\parallel}',hashshape)
replace(r"\unsure{C'est un|C'est une}",r"C'est un")
replace(r"à l' \unsure{:} At",r"à l' \unsure{:|.} At")
replace(r'\deleted{\unsure{ex}} At 11',r'\unsure{\deleted{ex}|ex} At 11')
replace(r'\uline{At \unsure{DD|DC}}',r'\uline{At DD}')
replace(r'Soient \inserted{\unsure{ancien|ou bien|ou bien,}}',r'\tikz[baseline=(so.base)]{\node[inner sep=0pt] (so) {Soient};\node[anchor=south west,rotate=43,inner sep=0pt] at (so.north east) {\inserted{ancien}};}')
loop=r'\mathrel{\tikz[baseline=-.3ex,x=.48em,y=.65em,line cap=round]{\draw (.4,.9)..controls(-.05,.8)and(-.08,.04)..(.35,.04)..controls(.66,.04)and(.6,.6)..(.3,.63);\draw (.43,.33)--(.66,.35) (.33,.03)--(.36,-.1);}}'
replace(r'\unsure{o|,}',loop)
replace(r"\unsure{l'énoncé|l'inverse}",r"l'inverse\unsure{\, :|\, .|\,}")
replace(r'\deleted{\unsure{est}}',r'\deleted{est}')
replace(r'\uline{Corollaire} 1 \quad la ',r'\uline{Corollaire} 1 \quad \unsure{la|le} ')

# Mark the physical leader from the slanted upper NB toward the old At DC 1.
replace(r'\margin{\uline{NB}',r'\margin{\tikz[x=.4em,y=.4em]{\draw (0,0)--(3.0,2.1);}\quad\uline{NB}')
# Preserve global cancellation geometry separately from the semantic deletion macros.
upper_start=tex.index(r'\deleted{\uline{At} DC 1')
upper_end=tex.index('\nOn voudra la',upper_start)
upper=tex[upper_start:upper_end]
margin_start=upper.index('% slanted\n\\margin{')
margin_end=upper.index('\n\n\\deleted{\\uline{Cor}',margin_start)
upper_margin=upper[margin_start:margin_end]
upper=upper[:margin_start]+upper[margin_end:]
upper_draw=r'''% Two long diagonal cancellations and the open lower return stroke.
\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt,text width=.93\linewidth,font=\small] (old) at (0,0) {%
@UPPER@
};
\draw ($(old.north west)!.02!(old.north east)+(0,.8em)$)--($(old.south west)!.50!(old.south east)+(0,.6em)$);
\draw ($(old.north west)!.56!(old.north east)+(0,.5em)$)--($(old.south west)!.93!(old.south east)+(0,4.0em)$);
\draw ($(old.south west)+(.2em,-.15em)$)..controls($(old.south west)+(6em,.2em)$)and($(old.south west)+(12em,.2em)$)..($(old.south west)+(18em,-.1em)$)--($(old.south west)+(24em,-.18em)$)..controls($(old.south west)+(24.5em,.6em)$)and($(old.south west)+(25em,2.2em)$)..($(old.south west)+(26.2em,2.7em)$);
\end{tikzpicture}}
'''.replace('@UPPER@',upper.strip())
tex=tex[:upper_start]+upper_margin+'\n\n'+upper_draw+tex[upper_end:]
# The vertical rule belongs to the lower main axiom, not to the slanted criterion.
lower_start=tex.index(r'\uline{At DD} 1')
lower_end=tex.index('\n\n\\uline{Corollaire} 1',lower_start)
lower=tex[lower_start:lower_end]
lower_draw=r'''\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0pt,text width=.92\linewidth] (ax) at (0,0) {@AX@};
\draw ([xshift=-.65em,yshift=-1em]ax.north west)--([xshift=-.65em,yshift=1em]ax.south west);
\end{tikzpicture}}'''.replace('@AX@',lower)
tex=tex[:lower_start]+lower_draw+tex[lower_end:]
tex='% R1 independent reading of scan009. Literal irregular letters and unfinished statements retained.\n\\usetikzlibrary{calc}\n'+tex
(out/'scan009.tex').write_text(tex)

rows=[]
audit=[]
def D(place,C,H,reading,dc,dh,kind,evidence,crop=None,confidence='high',marked=False,status='not applicable',math=None):
    c=cm.get(crop)
    row={'id':f'R1-009-{len(rows)+1:03d}','place':place,'C':C,'H':H,'reading':reading,'diff_C':dc,'diff_H':dh,'kind':kind,'marked_in_H':marked,'confidence':confidence,'evidence':evidence,'crop':c['file'] if c else None,'crop_coordinates':c['box'] if c else None,'crop_rotation_degrees':c['rotation_degrees'] if c else None,'C_doubt_status':status,'math_consequence':math}
    rows.append(row)
    return row
def A(n,place,C,H,reading,status,evidence,crop,confidence='medium',marked=False,kind='misread word',dh=True,math=None):
    row=D(place,C,H,reading,status!='retained',dh,kind,evidence,crop,confidence,marked,status,math)
    audit.append({'number':n,'place':place,'C':C,'reading':reading,'status':status,'confidence':confidence,'evidence':evidence,'crop':row['crop'],'crop_coordinates':row['crop_coordinates'],'difference_id':row['id']})
    return row

D('Opening, final word',"d'autres",r'\ill{}',"d'autres",False,True,r'readable ink left as `\ill{}`',
  'The upper half shows d, a raised apostrophe, and a connected autres ending. No final sentence stop follows before the draft heading.',marked=True)
D('Old At DC 1 heading underline',r'\uline{At} DC 1',r'At DC 1, struck without emphasis',r'\uline{At} DC 1',False,True,'omission',
  'The separate short underline ends beneath At; DC 1 lies beyond it.')
A(1,'Old At DC 1, membership alphabet',r'\unsure{M|\mathcal M}',r'\mathcal M',r'\unsure{M|\mathcal M}','retained',
  'The letter has two uprights and a curved lower join. M is certain, but ordinary versus calligraphic alphabet is not independently settled.','opening_M',kind='misread symbol or index')
A(2,'Old At DC 1, relation overwritten by compatibility',r'\deleted{\unsure{\parallel}}','only compatibility',r'\deleted{\parallel}','resolved',
  'Two distinct upright stems survive inside the newer opposed-chevron outline. Their direction differs from the four diagonal compatibility arms.','old_relation_end','high',kind='misread symbol or index',math='Records the earlier relation, not a repair of the final hypothesis.')
A(3,'Old At DC 1, glyph after Y',r'\unsure{\text{\S}|?|.}','omitted',r'\unsure{\text{\S}|?|.}','retained',
  'Upper and lower hooks favor a section-like mark, but the cancellation crosses its waist. A detached dot lies down and right; it may belong to the same question/terminal-mark group rather than a second stop.','old_relation_end','low',kind='misread symbol or index')
A(4,'Old second line, locally struck opening',r'\deleted{\unsure{Alors}}',r'\struck{At}',r'\deleted{\unsure{Alors}}','retained',
  'A tall A and the following tall/looped stroke are visible; the rest is under a long cancellation. Alors remains the best candidate, but its full ending is not independently recoverable.','old_Alors','low')
D('Old second line, Soient insertion','inserted Soient','baseline Soient','Soient inserted above the cancelled opening',False,True,'insertion or placement',
  'Soient is on the raised line directly above the locally struck opening.','old_Alors')
A(5,'Interlinear condition, letter after intersection',r'\unsure{L|\mathcal L}','L','L','resolved',
  'The letter is a single upright with a straight lower foot and no ornamental loop.','inserted_L','high',kind='misread symbol or index',dh=False)
D('Interlinear disjointness condition, anchor and parentheses','inserted after X′≪X; comma and (i.e. …)','added after the first X compatibility Y line; i.e. without parentheses','inserted after X′≪X; avec X′∥X∩Y=L, (i.e. X′∥Z pour Z≤X,Y)',False,True,'insertion or placement',
  'The raised phrase lies over the continuation of X′≪X. A comma follows L and a clear opening curve begins i.e.; the closing curve is at the right edge of the parenthetical.','inserted_L')
D('Global cancellation of the first draft and corollaries','whole passage marked deleted','first axiom struck; later lines and Cor 1/Cor.2 live inline; note acknowledges two long biffures','the old At DC 1 continuation and both corollaries are within the two diagonal cancellation strokes',False,True,'deletion state (struck given live or live given struck)',
  'Both long oblique strokes traverse the upper statement and corollaries. H records their existence in a note but does not consistently apply the state to its inline text.')
D('Geometry of global cancellation strokes','semantic deletion macros','prose note only','two long oblique strokes drawn across the old block',True,True,'drawing or diagram',
  'The whole page shows the two long diagonals spanning several old lines. Their geometry is independent of the small local cancellations.')
D('Upper NB, opening words','La chose importante est',r'Il \ill{} choisi \ill{}','La chose importante est',False,True,'misread word',
  'After NB, the rotated crop shows La, the low ch-o-se sequence, importante with its long p, and est.','upper_margin',marked=True)
D('Upper NB emphasis and leader',r'\uline{NB}; no leader drawn','NB without emphasis; no leader','NB underlined, with a thin unheaded diagonal connector toward the old At DC 1',True,True,'drawing or diagram',
  'The short underline is distinct from the thin oblique line extending toward the draft label. The line has no arrowhead.','upper_margin')
A(6,'Upper NB, after the empty-intersection formula',r'\unsure{immédiat}',r'\uncertain{immédiat}','immédiat','resolved',
  'The rotated crop exposes the i, two low m groups, accented e, d stem, i and final a-t. The ending t is distinct.','upper_margin','high',True)
D('Upper NB, Car and punctuation','immédiat. Car',r'immédiat (\ill{}','immédiat. Car',False,True,r'readable ink left as `\ill{}`',
  'A stop follows immédiat, then a capital C with a connected ar; no opening parenthesis begins this sentence.','upper_margin',marked=True)
D('Upper NB, old first relation on Z',r'Z\deleted{\ll}\leq X′','Z≤X′',r'Z\deleted{\ll}\leq X′',False,True,'omission',
  'A double-angle trace is locally crossed before the clear live less-than-or-equal relation.','upper_margin')
D('Upper NB, second Z in the consequence','Z≪Y','Z≪Y',r"\unsure{Z'|Z}\ll Y",True,True,'misread symbol or index',
  'A short raised stroke immediately follows the second Z. It is separate from the lower double-angle arms, but the surrounding slanted lines are crowded; a prime is preferred with doubt.','upper_margin','medium',math='If a prime is written, it breaks the repeated-Z chain. It is retained as a possible written slip rather than removed for consistency.')
D('Upper NB, connective or twice and parenthetical compatibility','or …, or … (d’où/comme Z compatibility L)','semicolons; et …; two illegible groups','or …, or … (d’où/comme Z compatibility L)',False,True,'misread word',
  'Both connective words have a low rounded o followed by r. The parenthetical includes a clear Z, opposed-chevron relation and L.','upper_margin',marked=True)
A(7,'Upper NB, first locally struck word',r'\deleted{\unsure{impossible}}',r'\ill{}',r'\deleted{impossible}','resolved',
  'Initial i, the m dips, a descending p and the ossible tail remain visible below/through the local strike.','upper_margin','medium',True)
A(8,'Upper NB, parenthetical connector',r"\unsure{d'où|comme}",r'\ill{}',r"\unsure{d'où|comme}",'retained',
  'The upper strokes cross the cancelled word above and the lower connected tail does not expose enough letters to choose d’où over comme.','upper_margin','low',True)
A(9,'Upper NB, second locally struck word',r'\deleted{\unsure{absurde}}',r'\ill{}',r'\deleted{\unsure{absurde}}','retained',
  'An initial loop, a tall b-like stroke and low middle strokes survive, but the final letters merge into the heavy cancellation.','upper_margin','low',True)
D('Upper NB, final two relations and car','⇒Z≤L … car Z∩L=∅!','⇒Z overlined-parallel L=∅!','⇒Z≤L … car Z∩L=∅!',False,True,'misread symbol or index',
  'The first relation is a slanted less-than arm over a short lower bar. The next written word is car, followed by Z, an arch intersection sign, L, equals and an empty symbol. A plus-like crossing nearby belongs to the main text direction.','upper_margin',math='H merges the intermediate comparison with the separate final contradiction. No proof is supplied here.')
D('Upper NB, final underline',r'\uline{Z∩L=∅ !}','no emphasis on final formula',r'\uline{Z∩L=∅ !}',False,True,'omission',
  'A separate long stroke underlines the entire final formula and exclamation.','upper_margin')
A(10,'Cancelled Cor 1, second named object',r'\unsure{C|G}','G','C','resolved',
  'The letter is open on the right, with no inward lower return. The later conclusion G on the same crop has the return stroke, giving a direct graphic comparison.','Cor1','high',kind='misread symbol or index',math='C is retained although the following argument uses G; no renaming is imposed.')
A(11,'Cancelled Cor 1, family alphabet',r'\unsure{\mathscr F|\mathcal F}',r'\mathfrak F',r'\unsure{\mathscr F|\mathcal F}','retained',
  'The extended upper bar and curved stem support a script or calligraphic F; the crossing line prevents a secure choice between those two alphabets. It is not visibly a blackletter construction.','Cor1',kind='misread symbol or index')
D('Cancelled Cor 1, first disjointness premise','F∥G','F∥G',r'F\parallel\unsure{C|G}',True,True,'misread symbol or index',
  'The right-hand glyph has an open C-like bowl without a clearly separable inward G bar. C is preferred, but a faint return cannot be excluded under the crossing.','Cor1','medium',math='Possible C/G draft inconsistency is preserved.')
D('Cancelled Cor 1, first refinement variable','F≪F','F′≪F','F≪F',False,True,'misread symbol or index',
  'There is no separate raised stroke after the first F. The actual primes elsewhere in the same crop are clearly detached.','Cor1',math='Unprimed F is a written irregularity; H supplies a mathematically expected prime.')
D('Cancelled Cor 1, second refinement variable','C′≪G','G′≪G','C′≪G',False,True,'misread symbol or index',
  'The first letter is an open C with a detached prime, while the second letter has the G return.','Cor1',math='Literal C′ is retained, without identifying it with G′.')
D('Cancelled Cor 1, emphasis span',r'\uline{Cor} 1',r'\emph{Cor 1}',r'\uline{Cor} 1',False,True,'other',
  'The underline terminates before the digit 1. This is a real span difference; merely converting same-span emph to uline is not counted.','Cor1')
D('Figure-family letters outside Cor 1',r'\mathscr F',r'\mathfrak F',r'\mathscr F',False,True,'misread symbol or index',
  'The upper and lower halves show the same flowing F-family form in Cor.2 and Propriété 1, with curved rather than blackletter strokes.')
A(12,'Cancelled Cor.2, entire earlier equation',r'\unsure{L}=Sup_{Z∈F̃∩G̃} Z',r'\struck{\ill{}}',r'\deleted{\unsure{L=Sup_{Z∈F̃∩G̃} Z}}','changed',
  'Cross-hatching masks the left letter and much of the operator and index. A terminal Z and portions of the lower F∩G group survive, but the entire equation cannot be certified symbol by symbol. The clear replacement L=F∩G is separate above it. C’s uncertainty is therefore widened from L to the old formula.','Cor2_old','low',True,kind='misread symbol or index',math='The plausible Sup expansion is explicitly uncertain and is not recovered merely from the mathematical role of L.')
D('Cancelled Cor.2, second refinement letter','G′≪G','G′≪G','C′≪G',True,True,'misread symbol or index',
  'The primed left glyph is an open C without a lower inward hook. The unprimed G to its right and the concluding G′ below both carry the inward return.','Cor2_right','high',math='The unexpected C′ is literal ink, not a mathematical correction.')
A(13,'Cancelled At DC 2, locally struck word at title end',r'\unsure{Soit|Soient}','Soient, not locally deleted',r'\deleted{\unsure{Soit|Soient}}','retained',
  'S and o are followed by a short low run and a tall final t-like stem under the heavy return stroke. Soit is favored; the middle does not securely rule out the longer ending. A local horizontal stroke crosses the word.','At2_Soit','low',kind='deletion state (struck given live or live given struck)')
D('Cancelled At DC 2, adjective','spacieux','spécieux','spacieux',False,True,'misread word',
  'The upper half shows an a bowl after sp and no acute accent over that letter.')
A(14,'Cancelled At DC 2, older letter under K',r'\deleted{\unsure{L}}','no older letter',r'\deleted{\unsure{L}}','retained',
  'A heavy horizontal arm runs right from the upright independently of K’s two oblique arms. It can be an older L foot, but the complete earlier letter cannot be isolated from the retracing.','At2_K','low',kind='misread symbol or index')
A(15,'Cancelled At DC 2, after pour',r'\unsure{tt}','tous','tt','resolved',
  'There are two upright hooked stems linked by one common crossbar, with no intervening o or u.','At2_tt','high',kind='abbreviation expanded or spelling modernised')
D('Cancelled At DC 2, underline in the hypotheses','underline Y′≪Y, X′∥K','none','underline Y′≪Y, X′∥K',False,True,'omission',
  'The supplied half shows a distinct horizontal stroke beginning under Y′ and ending under K, before the following Y′∥K.')
D('Cancelled At DC 2, heading emphasis extent',r'\uline{At DC} 2',r'\emph{At DC 2}',r'\uline{At DC} 2',False,True,'other',
  'The heading underline ends before 2. The difference is its span, not emph versus uline syntax.')
D('Cancelled At DC 2, lower framing line','not drawn','note says encadré','open long lower line, turning upward at its right end; no closed rectangle',True,True,'drawing or diagram',
  'A low continuous line runs under on ait … Alors and curves steeply upward at the right. Its left start is low; the rising diagonal nearby belongs to a cancellation stroke, not a completed left box edge.','At2_frame')
D('Transition before the live property','On voudra la','On voudrait la','On voudra la',False,True,'misread word',
  'The lower half shows the final a and then a clear gap before la. There is no final i-t group.')
D('Live heading','Propriété 1','Proposition 1','Propriété 1',False,True,'misread word',
  'The word has the short pr-i-é-t-é sequence and final accented e, not the longer position ending.')
D('Live property, display layout','two rows, equivalence at left of second row','single row','two rows; F′ compatibility G′ above ⇔ F′_L compatibility G′_L',False,True,'insertion or placement',
  'The first formula occupies a separate line. The equivalence sign begins the lower line to the left of both lowered L indices.')
D('Live property, retraced lower compatibility sign','clean opposed chevrons','standard between symbol','opposed chevrons with several heavy retraced central strokes, drawn literally',True,True,'drawing or diagram',
  'Four outer diagonal arms remain clear, while the center has two additional thick short transverse/diagonal runs. These do not expose a recoverable independent older relation.','property_relation','medium')
A(16,'Reference, first word',r'\unsure{cf|Cf}','cf.','cf','resolved',
  'The c is a low open curve and the f has a high loop and long descender. No distinct point follows f before the small crossed p.','reference_cf','high')
A(17,'Reference, small deleted group',r'\deleted{\unsure{p.}}','omitted',r'\deleted{p.}','resolved',
  'A descending p stem, crossed upper bowl and a separate point at its right are visible above the broad cancellation of the next line.','reference_cf','high')
A(18,'Reference, page digits',r'\uline{\unsure{73|13}}','73',r'\uline{\unsure{73|13}}','retained',
  'The first digit has a hooked upper stroke and a long downward stem, favoring 7, but 1 cannot be excluded from the overlap with the following 3. The underline is separate beneath both digits.','reference_73','medium',kind='misread symbol or index')
D('Both GF VI citations, bars on the numeral','VI with upper and lower rules','plain VI','VI with upper and lower rules',False,True,'omission',
  'The lower half and rotated counterexample crop show a rule above VI and another below it in both citations.','counterexample_margin')
D('Reference line, deletion state','live cf … On a en tous cas tjrs','entire line struck','live reference and assertion line',False,True,'deletion state (struck given live or live given struck)',
  'The long cancellation follows the baseline of the next, abandoned Montrons clause. It crosses only the descending f of the higher reference, not that entire sentence.','reference_cf')
D('Reference line, abbreviation after cas','tjrs','omitted','tjrs',False,True,'omission',
  'The lower half shows the tall t-j stem group followed by low r-s immediately before the direction mark.')
A(19,'Reference line, terminal direction mark','uncertain literal rounded arrow | ⇒','⇒',literal_arrow,'resolved',
  'Two horizontal shafts end before a detached curved right stroke. The right stroke bends downward and then left; it is not a sharp triangular arrowhead. The physical form is resolved, while its interpretation as an implication direction is left to context.','reference_arrow','high',kind='drawing or diagram')
A(20,'Deleted proof line, opening',r'\unsure{Montrons}','omitted',r'\unsure{Montrons}','retained',
  'The large M, a low rounded run and a central tall t-like stem survive. Several terminal letters are broken by the horizontal cancellation, so the full word remains provisional.','Montrons','low')
D('Deleted proof line, middle words','qu’on a bien','omitted','qu’on a bien',False,True,'omission',
  'The lower half shows qu’on a and the tall b followed by the connected ien run beneath the cancellation.','old_en')
A(21,'Deleted proof line, before the arrow',r'\unsure{en}','omitted','en','resolved',
  'A small looped e is followed by a low arch and downturned n ending; the cancellation crosses the upper part, but both connected letters remain separable.','old_en','medium')
D('Deleted proof line, final arrow and punctuation','⇒. En effet,','only En effet, merged into preceding deletion','⇒. En effet, on the lower abandoned line',False,True,'omission',
  'The arrow has a clear sharp right head, unlike the curled symbol on the live line. A separate stop follows it before En effet, which ends with a comma.','old_en')
D('Equivalence discussion, parenthetical wording','Ceci est équivalent (si on le voit de façon générale)',r'Ceci est équivalent \ill{} (\ill{} \ill{})','Ceci est équivalent (si on le voit de façon générale)',False,True,r'readable ink left as `\ill{}`',
  'The lower half gives all words in the parenthesis, including voit with its tall t and the accented générale.','ancien',marked=True)
D('Criterion margin, omitted phrase','pour les raffinements de sous-figures','struck/added illegible fragments','pour les raffinements de sous-figures',False,True,r'readable ink left as `\ill{}`',
  'The rotated note shows pour les, the long raffinements word with its tall f stems, de, and the hyphenated sous-figures below. The continuous strokes beneath are underlines rather than deletion of the wording.','criterion_margin',marked=True)
D('Criterion margin, underline spans','Critère; compatibilité; sous-figures underlined','no emphasis on these spans','Critère; compatibilité; sous-figures underlined',False,True,'omission',
  'Three separate underlining runs follow these words. The line beneath sous-figures sits above the baseline of Mais, which remains live.','criterion_margin')
D('Criterion margin, punctuation before Mais','no period after sous-figures','period after preceding added fragment','line break before Mais, no independently visible period after sous-figures',False,True,'text not on the page',
  'The rotated crop has the underline ending and the new Mais line; no isolated stop can be separated at that transition.','criterion_margin','medium')
D('Vertical rule beside lower axiom','rule prepended to criterion margin','note identifies a rule bordering the lower axiom; no drawing','rule at the left of the main At DD 1 / Posons–implique block',True,True,'insertion or placement',
  'In the whole page the rule is nearly vertical in the main text direction and extends beside the lower axiom. Rotating the margin makes that rule oblique, confirming it is not the criterion’s left border.','criterion_margin')
D('Example, outer and inner geometry','diamond, oval, diagonal, two dots','description without reproduction','drawn quadrilateral with bottom gap; oval with a lower-right gap; line between opposite vertices; two filled contacts',False,True,'drawing or diagram',
  'The crop exposes the two small gaps, the continuous near-vertical diagonal in the rotated direction, and both thickened contact points.','diagram')
A(22,'Example, small interior mark',r'\unsure{x|+}','small mark described','literal two short crossed strokes drawn in TikZ','resolved',
  'Two short thick strokes cross to the left of the oval. The physical mark can be drawn without deciding whether the writer intended a letter x or a plus.','diagram','high',kind='drawing or diagram',math='The semantic identity of the crossing mark is not resolved or used.')
A(23,'Example, exterior lower-left mark',r'\unsure{X|x}','cross described','literal diagonal cross drawn in TikZ','resolved',
  'Two distinct thin diagonals form a cross outside the lower-left side in the note’s reading orientation. No typographic case is needed to reproduce them.','diagram','high',kind='drawing or diagram')
A(24,'Example, exterior lower-right mark',r'\unsure{X|Y}','cross described','literal crossed diagonals with a reinforced lower-left-to-upper-right stroke','resolved',
  'The mark has two crossing directions, with a third heavy nearly parallel run reinforcing one diagonal and projecting lower-left. It is reproduced without assigning X or Y.','diagram','high',kind='drawing or diagram',math='The diagram labels are not inferred from the X,Y formula beside them.')
A(25,'Counterexample margin, consequent relation','literal two uprights and two bars | # | nparallel | parallel','overlined parallel, explicitly uncertain','literal two uprights crossed by two short oblique bars','resolved',
  'Both tall stems run above and below two distinct transverse strokes. There is neither a single top overline nor a single diagonal negation slash.','counterexample_margin','high',True,kind='drawing or diagram',math='The physical glyph is resolved; no standard relation is substituted and the author’s counterexample is not thereby proved.')
A(26,'Counterexample margin, short sentence opening',r"\unsure{C'est un|C'est une}","c'est un", "C'est un",'resolved',
  'The connected short group after est ends with a downturned n; there is no extra e loop before the next word. The initial C is capital in the note.','counterexample_margin','medium',dh=False)
A(27,'Counterexample margin, noun',r'\unsure{contre-exemple|contre-exple|contre exemple}','contre-ex.',r'\unsure{contre-exemple|contre-exple|contre exemple}','retained',
  'The beginning contre is visible, but its middle/end is interlaced with the main-text implique and Corollaire directions. The exact abbreviation and hyphen remain uncertain.','counterexample_margin','low',kind='abbreviation expanded or spelling modernised')
A(28,'Counterexample margin, mark before At',r'\unsure{:}','omitted',r'\unsure{:|.}','changed',
  'A separate lower point is clear before At. A possible second point lies among the overlapping end of the previous line, so colon versus a single point remains open.','counterexample_margin','low',kind='other')
A(29,'Counterexample margin, ex before At 11',r'\deleted{\unsure{ex}}',r'\ill{}',r'\unsure{\deleted{ex}|ex}','changed',
  'The e loop and crossed x strokes are now readable. The dark diagonal may be part of x or an additional local cancellation; deletion state remains uncertain.','counterexample_margin','low',True,kind='deletion state (struck given live or live given struck)')
D('Counterexample margin, first axiom label','At ∥','At 11','At ∥',False,True,'misread symbol or index',
  'After At there are two long parallel upright strokes, matching the disjointness sign in the formula above rather than the two short numeral ones in the next At 11.','counterexample_margin',math='The first cited axiom label differs from At 11; the page explicitly distinguishes them.')
D('Counterexample margin, comparison words','et a fortiori à',r'et \ill{}','et a fortiori à',False,True,r'readable ink left as `\ill{}`',
  'The rotated crop shows the separated a and the connected fortiori sequence, followed by the accented à before the old ex group.','counterexample_margin',marked=True)
D('Counterexample margin, citation and punctuation','comma after formula; C’est un … (cf GF barred VI, p.67,68)','parenthesis begins before c’est un; abbreviated citation at end','comma after formula; C’est un … (cf GF barred VI, p.67,68)',False,True,'insertion or placement',
  'A comma follows the consequent. The opening parenthesis belongs to cf GF at the later citation, and the closing curve follows 68. H’s prose note identifies GF VI but does not reproduce this placement in the marginal text.','counterexample_margin')
A(30,'Lower live axiom heading',r'\unsure{DD|DC}','CD with note of underlying DD/DC','DD','resolved',
  'Both letters have closed counters and a stem. The first is heavily retraced, but the second has a clear closed right-hand bowl; neither reads as an open C.','AtDD','high',kind='misread symbol or index',math='DD is kept without harmonizing it to the earlier DC headings.')
D('Lower live axiom, heading underline span',r'\uline{At DD} 1',r'\emph{At CD 1}',r'\uline{At DD} 1',False,True,'other',
  'The underline ends below the second D and stops before the digit 1. This is a span difference in addition to the letter reading.','AtDD')
A(31,'Oblique insertion above Soient',r'\unsure{ancien|ou bien|ou bien,}',r'ou \uncertain{ancien}','ancien','resolved',
  'The first run begins with an a oval and low n. The second run has a small c-like loop, a dotted i and connected en; no tall b appears. Its physical position is above/by Soient, while its intended grammatical attachment is still uncertain.','ancien','high',True,kind='insertion or placement')
A(32,'Lower axiom, separator between Y and X′',r'\unsure{o|,}','et','literal small closed loop with a rightward tick and short lower spur','resolved',
  'The narrow closed oval is much taller than the nearby comma. It has a small rightward tick and a tiny lower spur; it is drawn without turning it into et or choosing a grammatical separator.','separator','high',kind='drawing or diagram')
D('Lower axiom, definition of K','K=X∩Y','K=X∧Y','K=X∩Y',False,True,'misread symbol or index',
  'The lower half shows the rounded arch of intersection, not the sharp two-sided wedge.','bottom_NB',math='The definition writes K, while the conclusion uses L; both are kept as written.')
D('Lower axiom, NB placement','after X′ compatibility Y′','between restricted antecedent and implique','after the conclusion X′ compatibility Y′',False,True,'insertion or placement',
  'The parenthesis begins on the lower/right line after the conclusion. The marginal GF reference crosses nearby but belongs to the slanted note.','bottom_NB')
A(33,'Lower axiom NB, noun',r"\unsure{l'énoncé|l'inverse}","l'inverse","l'inverse",'resolved',
  'The visible sequence begins with l’, then a narrow i/n run and low v-e-r-s strokes; there is no initial accented e followed by a tall n-o-n-c sequence. Tiny terminal dots are separately left as a punctuation doubt.','bottom_NB','medium',dh=False)
D('Lower axiom NB, marks after inverse','no independent punctuation','no independent punctuation',r"l'inverse\unsure{\, :|\, .|\,}",True,True,'other',
  'Two tiny dark points lie diagonally at the word’s right end. They may be terminal cursive fragments, a colon or a point. They are not silently omitted or promoted to certain punctuation.','bottom_NB','low')
A(34,'Lower axiom NB, older verb',r'\deleted{\unsure{est}}',r'\ill{}',r'\deleted{est}','resolved',
  'A small e loop, a low s turn and the tall crossed t-like stroke survive in the older word; a separate faint live est follows it.','bottom_NB','medium',True)
D('Lower axiom NB, abbreviation','est tjrs vrai','always expanded as toujours; preceding verb illegible','est tjrs vrai',False,True,'abbreviation expanded or spelling modernised',
  'The live est is followed by the tall t-j group and short r-s; there is no long toujours letter sequence.','bottom_NB',marked=True)
D('Lower axiom, spurious main-line reference','no main-text cf GF VI after implique','implique (cf. GF VI)','no main-text cf GF VI after implique',False,True,'text not on the page',
  'The GF VI text is slanted in the counterexample note’s direction and joins its p.67,68 citation, rather than the main implication line.','counterexample_margin')
D('Corollaire 1, label and separate assertion','Corollaire 1; la quoted propriété ci dessus','Cor. Main 1, with parenthetical cf. and formula combined','Corollaire 1; la/le quoted propriété ci dessus, separate from the next formula',False,True,'misread word',
  'The lower half shows the full long Corollaire word, a separate digit 1, then the short text referring to the property. There is no Main and no cf. at this location.')
D('Corollaire 1, article','la','la',r'\unsure{la|le}',True,True,'misread word',
  'A tall l is followed by a single broad loop and low terminal stroke. The second vowel’s closure does not securely distinguish a from e; the grammatically expected la is not forced.','Cor1_la','medium')
D('Corollaire 1, quotation and spelling','double tick quotes; ci dessus','guillemets; ci-dessus','double tick quotes; ci dessus',False,True,'abbreviation expanded or spelling modernised',
  'The lower half has short paired high strokes around propriété and no hyphen between ci and dessus.')
D('Corollaire 2, label attached to disjointness consequence','Corollaire 2 aligned at left of F∥G,…⇒F′∥G′','formula combined with Cor. Main 1','Corollaire 2 aligned with this formula',False,True,'insertion or placement',
  'A separate underlined Corollaire and digit 2 occupy the left of the disjointness implication display.')
D('Final generalization heading','Plus gén.','Cor. Main 2; note suggests pour que','Plus gén.',False,True,'misread word',
  'The crop shows a capital P with a loop, tall l, low us ending, and a separate gén. with accent and final point. There are no letters for Cor. Main here.','Plus_gen',marked=True)

coverage=[
('text','top','page number 8 and opening J’explicite … d’autres'),
('deletion','upper block','old At DC 1 full heading, membership and compatibility hypothesis'),
('deletion','upper block','older parallel inside compatibility and terminal hooked glyph'),
('deletion','upper block','Alors and earlier Y′≪Y⇒X′∥Y′'),
('insertion','upper block','raised Soient'),
('insertion','upper block','avec X′∥X∩Y=L, (i.e. X′∥Z pour Z≤X,Y)'),
('text','upper block','repeated Y′≪Y avec Y′∥L. Alors X′∥Y′'),
('margin note','upper left slanted','entire NB from La chose importante est through final contradiction'),
('deletion','upper left slanted','old ≪, impossible, doubtful absurde'),
('drawing','upper left','NB underline and unheaded leader toward old At DC 1'),
('deletion','upper block','Cor 1 full text, C/G forms, absent F prime, C′ premise'),
('deletion','upper block','Cor.2 full text and uncertain old Sup equation'),
('insertion','upper block','Cor.2 L=F∩G above old equation'),
('deletion','middle upper','At DC 2, title, old Soit/Soient, old L under K, all hypotheses and dangling Alors'),
('drawing','middle upper','local underline Y′≪Y, X′∥K; open lower framing stroke'),
('drawing','upper through middle','two long global diagonal cancellation strokes'),
('text','middle','On voudra la; Propriété 1 with F,G and L definition'),
('display','middle','two-line compatibility equivalence with both lowered L indices and retraced sign'),
('text','middle lower','live cf p.-deletion GF barred VI p.73/13; On a en tous cas tjrs'),
('drawing','middle lower','literal double shaft and detached curled right end'),
('deletion','middle lower','Montrons qu’on a bien en ⇒. En effet,'),
('text','middle lower','Ceci est équivalent (si on le voit de façon générale) à l’ancien At12, qui prend le nom'),
('margin note','lower left slanted','Critère de compatibilité pour les raffinements de sous-figures; Mais c’est faux dans le cas simplicial, ex :'),
('drawing','lower left slanted','diamond, gapped oval, diagonal, two contact dots, interior cross and two exterior crosses'),
('margin note','bottom left slanted','Mais on aura … literal double-barred relation; C’est un contre-… à l’ … At ∥, et a fortiori à ex At11 (cf GF barred VI,p.67,68)'),
('deletion','bottom left slanted','ex, readable but local cancellation state uncertain'),
('text','lower main','At DD 1, full membership/refinement statement and definition K=X∩Y=Sup Z'),
('insertion','lower main','slanted ancien above/by Soient, attachment uncertain'),
('drawing','lower main','closed-loop separator and vertical border beside the axiom'),
('text','lower main','restricted compatibility implies unrestricted compatibility with L subscripts kept'),
('text','lower right','NB l’inverse, doubtful terminal dots, old est, live est tjrs vrai'),
('deletion','lower right','old est'),
('text','bottom','Corollaire 1, la/le quoted propriété ci dessus'),
('display','bottom','Corollaire 2 and F∥G,F′≪F,G′≪G⇒F′∥G′'),
('text','bottom','Plus gén. Si F compatibility G,F′≪F,G′≪G,alors'),
('display','bottom','final F′∥G′⇔F′_L∥G′_L')]

notation=[
{'sign':'opposed-chevron compatibility','reading':'literal TikZ opposed chevrons','page_observation':'Recurs in the old and live statements. The second sign in the property display has substantial retracing; no older relation is identifiable there.'},
{'sign':'parallel','reading':r'\parallel','page_observation':'Plain two uprights in disjointness hypotheses; old uprights also survive under the first compatibility sign.'},
{'sign':'counterexample consequent','reading':'two uprights crossed by two transverse oblique bars','page_observation':'Draw literally; neither a single overline nor standard nparallel. Semantic interpretation remains unproved.'},
{'sign':'curled double-shaft direction','reading':'two shafts plus detached curved right end','page_observation':'Distinct physical form from the sharp arrow in the cancelled line below.'},
{'sign':'F/G/C','reading':'C and C′ retained where open bowls lack G return','page_observation':'Cor 1 starts F,C; its first disjointness right letter remains C|G; Cor.2 has C′≪G.'},
{'sign':'family F','reading':r'\mathscr F, with \mathcal F alternative at first Cor 1 occurrence','page_observation':'Flowing F family is not silently converted to H’s blackletter choice.'},
{'sign':'M','reading':r'M|\mathcal M at first occurrence','page_observation':'Letter identity clear; alphabet convention unresolved; later plain-M choices remain diplomatic conventional rendering.'},
{'sign':'At DD 1','reading':'DD','page_observation':'Both closed counters visible. First D retraced; no reconstructed earlier CD/DC layer certified.'},
{'sign':'K / L','reading':'K defined, L used in restrictions','page_observation':'Written mismatch retained, without substitution.'},
{'sign':'tt; tjrs; gén.; cf; p.','reading':'literal abbreviations','page_observation':'Possible expansions only in metadata: tous/tout; toujours; généralement/général; confer; page. No expansion inserted into transcription.'},
{'sign':'diagram marks','reading':'geometric crossed strokes','page_observation':'Reproduced physically without a claim of x/X/Y/plus identity.'},
{'sign':'emphasis conventions','reading':'same-span H emph to final uline not counted alone','page_observation':'Actual omitted emphasis and different span boundaries remain differences; documentary finding in emphasis_audit applies.'}]

unresolved=[]
for r in rows:
    if r['C_doubt_status'] in ('retained','changed') or r['confidence']=='low' or r['place'] in ('Upper NB, second Z in the consequence','Cancelled Cor 1, first disjointness premise','Corollaire 1, article'):
        unresolved.append({k:r[k] for k in ['place','reading','confidence','evidence','crop']})
unresolved.append({'place':'Oblique ancien attachment','reading':'ancien is legible, but its grammatical attachment remains uncertain','confidence':'low','evidence':'The word is floating obliquely above/by Soient; no unambiguous caret assigns it to an exact word.','crop':cm['ancien']['file']})
images=[{'file':f'source/SP35_CW_156-7_scans/H156-01_156-7_scan009{s}.jpg','role':role,'views':1} for s,role in [('', 'whole page'),('_a','supplied upper half'),('_b','supplied lower half')]]
images += [{**c,'role':'targeted unresolved-locus crop','views':1} for c in crops]
end=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
report={
'reader':'R1','scan':'009','H_page':8,'model':'GPT-6 Astra Pro, inherited configuration; effort setting not exposed',
'start_utc':(out/'scan009_start.txt').read_text().strip(),'end_utc':end,
'independence':'Only current C/H page8 and C metadata were used for page009; no other-reader or main009 material was opened. A separate authorized read-only emphasis audit of already-gated main002–007 had ended before this page task. No later page, new S row, OCR, compilation, or external research was used.',
'images_viewed':images,'image_attempt_note':'A tool batch containing Cor2_old, Cor2_right, and At2_Soit was truncated before usable images reached the reader; those existing crop files were subsequently displayed separately. Each usable whole/half/crop was inspected once. No crop was regenerated.',
'coverage':[{'order':i+1,'sheet_kind':'text','hand':'his hand','kind':k,'position':p,'element':e,'transcribed':'yes'} for i,(k,p,e) in enumerate(coverage)],
'agreed_targeted_checks':[
{'place':'Repeated Y′≪Y line','result':'The small round mark after Y begins avec; no extra stop is inserted there. Point after L is retained.','crop':cm['Y_line_punctuation']['file']},
{'place':'Cor.2 replacement','result':'L=F∩G is clear above the cancelled equation.','crop':cm['Cor2_old']['file']},
{'place':'Cor.2 conclusion','result':'F′∥G′ is clear, and its G′ has an inward return distinct from C′ in the premise.','crop':cm['Cor2_right']['file']},
{'place':'Final restriction indices','result':'Both lowered indices are L, not i or j, and each primed F/G is preserved.','source':'supplied lower half'}],
'notation':notation,
'math_notes':{
 'page_claims':[{'place':'old At DC1 and Cor1/Cor.2','claim':'Cancelled disjointness propagation statements with compatibility and restriction-to-intersection hypotheses.','status':'Author’s draft claims; not independently proved.'},
 {'place':'upper NB','claim':'The note reduces disjointness to compatibility and an empty intersection, then sketches a Z-based contradiction.','status':'Read as a proposed argument. Possible written Z′ and C/G slips are not silently repaired.'},
 {'place':'At DC2','claim':'An unfinished spacieux axiom whose hypotheses impose disjointness of compatible refinements avoiding K.','status':'Cancelled and ends at Alors; no missing conclusion supplied.'},
 {'place':'Propriété1','claim':'Compatibility of F′ and G′ is equivalent to compatibility of their L-restrictions.','status':'Proposed by On voudra la; no independent proof checked.'},
 {'place':'lower axiom','claim':'The proposed property is related to old At12 and given as At DD1; NB calls the reverse always true.','status':'K/L discrepancy is literal. Both directions were read, not proved.'},
 {'place':'criterion margin and drawing','claim':'The author says the criterion is false in the simplicial case and offers a geometric counterexample, also against At ∥ and a fortiori At11.','status':'Author’s refutation is transcribed; the diagram was not converted to a formal countermodel or independently verified.'},
 {'place':'bottom corollaries','claim':'Disjointness is asserted to pass to refinements, then to be equivalent to disjointness of restricted refinements.','status':'Transcribed claims only.'}],
 'actual_check_events':[],
 'actual_check_limits':'No targeted proof, re-proof, computation, formal certificate, or independent counterexample validation occurred in this page task. Line-by-line following of the mathematics is not counted as a check event.',
 'mathematics_led_to_reading':[],
 'ink_over_expectation':['F≪F is unprimed in cancelled Cor1.','Open C/C′ forms are kept where the surrounding argument uses G/G′.','The possible raised prime on the second Z remains doubtful.','DD is not harmonized to DC or CD.','The lower axiom defines K but writes L in its conclusion.','The marginal relation is drawn literally rather than normalized to a negated parallel sign.','La/le before propriété remains an ink doubt despite the grammatical expectation.']},
'author_qualifications':["bien qu'elle sera conséquence de diverses façons d'autres",'Alors [dangling at the end of cancelled At DC 2]','On voudra la',r'On a en tous cas tjrs [literal curled direction mark]',"Ceci est équivalent (si on le voit de façon générale) à l'ancien At 12, qui prend le nom","Mais c'est faux dans le cas simplicial, ex :",'Mais on aura',"C'est un [contre-exemple/contre-exple/contre exemple] à l' … At ∥, et a fortiori à … At 11",r"NB l'inverse [terminal dots uncertain] [deleted est] est tjrs vrai"],
'differences':rows,'C_doubt_audit':sorted(audit,key=lambda a:a['number']),'unresolved':unresolved,
'missing_from_both':[
{'place':'Cor.2 premise','reading':'C′≪G, not G′≪G','certainty':'high','crop':cm['Cor2_right']['file']},
{'place':'upper NB consequence','reading':'possible raised prime on the second Z','certainty':'medium; retained doubt','crop':cm['upper_margin']['file']},
{'place':'upper NB leader','reading':'thin unheaded connector toward the old At DC1','certainty':'high','crop':cm['upper_margin']['file']},
{'place':'lower NB terminal dots','reading':'possible punctuation after inverse, or terminal letter fragments','certainty':'low','crop':cm['bottom_NB']['file']},
{'place':'property display','reading':'retraced lower compatibility sign','certainty':'medium','crop':cm['property_relation']['file']}],
'S_audit':'No S row applies directly to scan009, and no S row was opened in this page task.',
'counts':{'difference_rows':len(rows),'diff_C':sum(r['diff_C'] for r in rows),'diff_H':sum(r['diff_H'] for r in rows),'C_doubts':len(audit),'C_doubts_resolved':sum(a['status']=='resolved' for a in audit),'C_doubts_retained':sum(a['status']=='retained' for a in audit),'C_doubts_changed':sum(a['status']=='changed' for a in audit),'targeted_crops':len(crops),'inventory_elements':len(coverage)}
}
assert sorted(a['number'] for a in audit)==list(range(1,35))
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as `\ill{}`','drawing or diagram','other'}
assert all(r['kind'] in allowed for r in rows)
assert len(crops)==28
(out/'scan009.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
md=['# R1 independent scan009 / handwritten page8','',f"Reading interval: {report['start_utc']} to {end}.",'',
    'Whole page and both supplied halves were inspected once, followed by 28 once-only targeted crops. No OCR, external research, compilation, other-reader report or main009 decision was used. The only read of consolidated main records was the separately authorized, completed documentary emphasis audit of already-gated scans002–007.','',
    '## Principal findings','',
    '- Lower heading: **At DD 1**. Both D counters close; the first D is retraced. The slanted insertion reads **ancien**, but its grammatical attachment is uncertain.',
    '- The old Cor1 has **F,C**, a possible **C|G** in the first disjointness premise, **F≪F** without a first prime, and **C′≪G**. Cor.2 likewise has a clear **C′≪G**. These are kept as written.',
    '- The first NB has **La chose importante est**, **immédiat**, and a readable deleted **impossible**. Its second Z may carry a raised prime. The connector **d’où|comme** and deleted **absurde** remain uncertain.',
    '- The old Cor.2 Sup equation is heavily cross-hatched: its uncertainty is widened to the entire old formula, while the replacement **L=F∩G** is clear.',
    '- **tt** is literal. The cancelled AtDC2 has an open lower framing stroke, not a closed box. The reference line is live; the abandoned **Montrons … ⇒. En effet,** line below is cancelled.',
    '- The live direction mark is drawn as two bars with a detached curved right end. The lower marginal consequent has two uprights crossed by two short bars. The drawing’s marks are reproduced as geometric strokes, without forcing X/Y/x/plus identities.',
    '- The vertical border belongs beside the lower main axiom. The definition writes **K=X∩Y**, followed by **L** restrictions. The NB reads **l’inverse**, with a deleted old **est**, a live **est tjrs vrai**, and uncertain tiny terminal dots after the noun.',
    '- The bottom has separate **Corollaire1**, **Corollaire2**, and **Plus gén.** The article before quoted propriété remains **la|le**.',
    '- Same-span H emph → uline conversion is not counted by itself; differing underline spans and omitted emphasis are counted.','',
    '## Limits of mathematical checking','',
    report['math_notes']['actual_check_limits'],
    'The source’s declaration that the simplicial case supplies a counterexample is reported as the author’s claim. No formal countermodel was reconstructed from the drawing. No mathematical expectation determined a glyph, prime, index, spelling or correction.','',
    '## Coverage and counts','',json.dumps(report['counts'],ensure_ascii=False,indent=2),'',
    'The JSON contains the ordered 36-element inventory, all witness-difference rows, all 34 C doubts, evidence and crop coordinates, notation, uncertainties, and the explicit empty check-event list.','',
    '## Remaining doubts','']
for u in unresolved:
    md.append(f"- **{u['place']}**: `{u['reading']}` — {u['evidence']}")
md += ['', '## Decision index','', '| ID | Place | C difference | H difference | Confidence |','|---|---|---:|---:|---|']
for r in rows:
    md.append(f"| {r['id']} | {r['place']} | {r['diff_C']} | {r['diff_H']} | {r['confidence']} |")
(out/'scan009.md').write_text('\n'.join(md)+'\n')
print(json.dumps(report['counts'],ensure_ascii=False))
