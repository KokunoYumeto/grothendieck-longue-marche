from pathlib import Path
import json,re
out=Path('/workspace/scratch/42e661864e98/out/readers/scan012/R1')
source='/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012.jpg'
zig=r'\mathrel{\tikz[baseline=0pt,x=1em,y=1em]{\draw (-.38,.62)--(.38,.25)--(-.43,-.10); \draw (.34,.62)--(-.32,.25)--(.38,-.10);}}'
heavy=r'\mathrel{\tikz[baseline=0pt,x=1em,y=1em]{\draw[very thick] (-.38,.62)--(.38,.25)--(-.43,-.10); \draw[very thick] (.34,.62)--(-.32,.25)--(.38,-.10); \draw[very thick] (-.10,.65)--(-.10,-.12);}}'
stem=r'\mathrel{\deleted{\tikz[baseline=0pt,x=1em,y=1em]{\draw (0,.65)--(0,-.12);}}}'
uncertain_sign=r'\unsure{'+heavy+'|'+stem+zig+'}'
tex=r'''\scanpage{12}\mspage{11}
\diagram{%
\[
\vcenter{\hbox{\begin{tikzcd}[ampersand replacement=\&,row sep=1.25em,column sep=.2em,
execute at end picture={
\draw ([xshift=-.55em,yshift=1em]leq.north west) -- ([xshift=.80em,yshift=.05em]leq.north east);
\draw ([xshift=.65em,yshift=.1em]leq.north east) -- ([xshift=.75em,yshift=-.95em]ltlt.south east) -- ([xshift=-.9em,yshift=-.1em]ltlt.south west);
\draw ([xshift=-.85em,yshift=.12em]ltlt.south west) -- ([xshift=-.70em,yshift=.85em]leq.north west);
}]
\& \& G\triangleleft F \arrow[d,Rightarrow] \& \& \\
G\preccurlyeq F \arrow[dr,Rightarrow] \& \& |[alias=leq]| G\leq F \arrow[dl,Rightarrow] \arrow[dr,Rightarrow] \& \& G\parallel F \arrow[dl,Rightarrow] \\
\& |[alias=ltlt]| G\ll F \& \& G SIGN \unsure{F|\mathbb{F}} \&
\end{tikzcd}}} \tag*{(1.18)}
\]}
% The two left corners of the oblique frame are open. The extra upright in the
% dark compatibility glyph has uncertain live/canceled state; no earlier letter
% is inferred. The alternative explicitly cancels only that upright stroke.

Parmi les six relations, il y a quatre relations d'ordre $\triangleleft$, $\leq$, $\preccurlyeq$, $\ll$, et les deux autres relations $\parallel$ et $ZIG$ sont symétriques.
% slanted
\margin{Non, $\triangleleft$ n'est pas rel. d'ordre, elle est transitive mais non réflexive, car $F\triangleleft F\Longleftrightarrow F\unsure{\in|\overset{\prime}{\in}}\unsure{\mathcal{M}|M}$ Pour avoir une relation d'ordre il faudrait écrire \deleted{$F\triangleleft$} $F\trianglelefteq F\overset{\mathrm{déf}}{\Longleftrightarrow}F\triangleleft F$ \uuline{ou} $F=F$.}
La relation $ZIG$ est \inserted{de plus} réflexive, mais $\parallel$ ne l'est que si $\unsure{\mathcal{F}|\mathfrak{F}}$ est réduit à son seul \unsure{élémt|élément} $\varnothing_{\mathcal{F}}$, car
\[
F\parallel F\quad\Longleftrightarrow\quad F=\varnothing_{\mathcal{F}}\qquad\text{figure vide.}\tag*{(1.19)}
\]

\uline{Remarques}\quad a) Les relations $\triangleleft$ et $\leq$ se déterminent mutuellement. Connaissant $\leq$, on définit $\mathcal{M}\subset\mathcal{F}$ comme
\[
\mathcal{M}=\left\{\begin{aligned}
&X\in\mathcal{F}\mid X\ \underset{\text{pour }\leq}{\text{$\mathrm{str}^{\mathrm{t}}$. irréductible}},\quad\text{i.e.}\ X\leq\mathop{\mathrm{Sup}}\limits_i F_i\Rightarrow\\
&\hspace{12em}\exists i\ \text{avec }X\leq F_i
\end{aligned}\right\}\tag*{(1.20)}
\]
puis $\triangleleft$ par (1.17).
\deleted{\unsure{Et|En}} D'autre part, connaissant $\triangleleft$ on définit $\mathcal{M}$ par
\[
\mathcal{M}=\{X\in\mathcal{F}\mid X\triangleleft X\}\tag*{(1.21)}
\]
puis, pour $F\in\mathcal{F}$, son déployement
\[
\widetilde F=\{X\in\mathcal{M}\mid X\triangleleft\mathcal{F}\}\tag*{(1.22)}
\]
et enfin
\[
F\leq G\quad\Longleftrightarrow\quad\widetilde F\subset\widetilde G\tag*{(1,23)}
\]
Donc, pour déterminer \deleted{la structure, il est \unsure{équivalent|equivalent}} \inserted{les données \unsure{minima|minimes} qui} fixent la structure d'atelier, il est indifférent d'y
'''.replace('SIGN',uncertain_sign).replace('ZIG',zig)
(out/'reading.tex').write_text(tex,encoding='utf-8')

crop_info={}
for p in sorted((out/'crops').glob('*.json')):
 d=json.loads(p.read_text()); key=p.stem
 crop_info[key]=dict(crop='readers/scan012/R1/crops/'+key+'.jpg',crop_box=d['box'],crop_source=d['source'])
def ev(crop=None,box=None):
 if crop:return crop_info[crop].copy()
 return dict(crop=None,crop_box=box,crop_source=source)
D=[]
def diff(id,place,c,h,reading,against_C,against_H,kind,marked,confidence,evidence,crop=None,box=None,mathematical=False):
 d=dict(id=id,place=place,c=c,h=h,reading=reading,against_C=against_C,against_H=against_H,kind=kind,marked_in_H=marked,confidence=confidence,evidence=evidence,mathematical=mathematical)
 d.update(ev(crop,box));D.append(d)
# Diagram and main paragraph.
diff('012-R1-D01','(1.18), oblique enclosure','closed quadrilateral (draw path ends -- cycle)','note: cadre oblique entoure G\\leq F et G\\ll F','Oblique frame with a gap at each left corner and a small top-right overrun.',True,False,'drawing or diagram','no','high','Crop 01 shows white gaps between the left side and the top/bottom sides. C closes both. H is credited for identifying the enclosure; its note does not specify these corners.',crop='01_diagram_frame',mathematical=True)
diff('012-R1-D02','(1.18), lower-right relation sign',zig,r'\between',uncertain_sign,True,True,'misread symbol or index','no','medium','Four free diagonal ends and two crossing zigzags are visible, together with an extra near-vertical upright. Heavy retracing does not decide whether that upright is live or canceled residue. The first reading includes it; the alternative cancels only this physical stroke.',crop='02_diagram_compatibility',mathematical=True)
diff('012-R1-D03','(1.18), lower-right final F','F','F',r'\unsure{F|\mathbb{F}}',True,True,'misread symbol or index','no','medium','The F has two separately visible upright tracks enclosing a narrow white channel and joining below. Retraced ordinary F remains first; a deliberately doubled F cannot be excluded.',crop='02_diagram_compatibility',mathematical=True)
diff('012-R1-D04','first body paragraph, relation after parallel',zig,r'\between',zig,False,True,'misread symbol or index','no','high','Half a shows two opposed zigzags with four free diagonal tips and no horizontal caps; the actual drawn geometry is retained.',box=[1132,903,1194,968],mathematical=True)
# Marginal correction.
diff('012-R1-D05','slanted margin, after non réflexive','car','omitted','car',False,True,'omission','no','high','The rotated note has the separate c-a-r word before its first equivalence.',crop='03_slanted_correction')
diff('012-R1-D06','slanted margin, membership in first equivalence',r'\unsure{\in|\overset{\prime}{\in}}',r'\in',r'\unsure{\in|\overset{\prime}{\in}}',False,True,'misread symbol or index','no','low','An oblique stroke lies above the membership sign. The note crosses neighboring writing, and its affiliation to the sign or preceding prose remains unresolved even after rotation.',crop='03_slanted_correction',mathematical=True)
diff('012-R1-D07','slanted margin, M in first equivalence','M',r'\mathcal{M}',r'\unsure{\mathcal{M}|M}',True,True,'misread symbol or index','no','medium','The letter has a curved rising entry and two upper humps. Its identity is M; handwritten ordinary versus calligraphic alphabet is not determined. First occurrence is marked, later local occurrences use the first candidate.',crop='03_slanted_correction',mathematical=True)
diff('012-R1-D08','slanted margin, punctuation after M','no point','.','no point',False,True,'text not on the page','no','high','No independent point follows the M; the next marginal sentence starts Pour on the next note line.',crop='03_slanted_correction')
diff('012-R1-D09','slanted margin, Pour avoir une','avoir',r'\ill{}','avoir',False,True,r'readable ink left as \ill{}','yes','high','The rotated crop separates the small a, v, dotted i and terminal r between Pour and une.',crop='03_slanted_correction')
diff('012-R1-D10','slanted margin, une relation d’ordre','relation','rel.','relation',False,True,'misread word','no','high','The full word continues beyond rel through its t and reduced ion ending. It is not abbreviated here.',crop='03_slanted_correction')
diff('012-R1-D11','slanted margin, il faudrait écrire','il faudrait écrire',r'\ill{} avoir écrit','il faudrait écrire',False,True,r'readable ink left as \ill{}','yes','high','The separate initial il, long f, reduced audr- group and final t of faudrait are visible; écrire has a final e-shaped return, not terminal t. This is one aligned local H phrase.',crop='03_slanted_correction')
diff('012-R1-D12','slanted margin, canceled start after écrire',r'\deleted{\unsure{F\triangleleft|F}}','omitted',r'\deleted{F\triangleleft}',True,True,'deletion state','no','high','Under the cancellation, an F stem with arms is followed by a separate triangular wedge and right side. Both F and triangle survive; the group is canceled.',crop='03_slanted_correction',mathematical=True)
diff('012-R1-D13','slanted margin, ou in proposed definition',r'\uuline{ou}','ou',r'\uuline{ou}',False,True,'omission','no','high','Two separate short rules are visible beneath ou.',crop='03_slanted_correction')
diff('012-R1-D14','slanted margin, terminal punctuation after F=F','.','no point','.',False,True,'omission','no','medium','A small separate terminal mark follows the last F on the same oblique baseline; it is read as the final point.',crop='03_slanted_correction')
diff('012-R1-D15','H note about a second standalone F trianglelefteq F','no separate repetition',r'note: le dernier F\trianglelefteq F est aussi porté seul au bas de la note','Only one live F\\trianglelefteq F, at the left of the proposed definition.',False,True,'text not on the page','no','high','The low-left formula belongs to the same line as the definition arrow. There is no additional standalone repetition; the other nearby group is the canceled F and triangle already recorded.',crop='03_slanted_correction',mathematical=True)
# Reflexivity paragraph.
diff('012-R1-D16','body, before La relation','no canceled word',r'\struck{Les}','no canceled Les',False,True,'text not on the page','no','high','Crop 04 shows the live capital La followed by relation; crossing strokes belong to the slanted note. No separate canceled Les is present.',crop='04_relation_start')
diff('012-R1-D17','body, relation in La relation … est',zig,r'\between',zig,False,True,'misread symbol or index','no','high','The clean second body occurrence again has two opposed zigzags and four free tips.',box=[658,989,723,1059],mathematical=True)
diff('012-R1-D18','insertion after est',r'\inserted{de plus}',r'\add{de plus,}',r'\inserted{de plus}',False,True,'text not on the page','no','high','The detached small terminal curve is the s of plus. The following longer curved stroke continues down to the insertion site; there is no separate comma.',crop='11_de_plus_punctuation')
diff('012-R1-D19','body, first family F after si',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\mathfrak{F}',r'\unsure{\mathcal{F}|\mathfrak{F}}',True,True,'misread symbol or index','no','medium','A broad swept top arm, crossing middle arm and curled foot distinguish the family glyph from ordinary F. Exact calligraphic/Gothic typography remains open; the supplied table’s alternatives are used.',crop='05_family_f',mathematical=True)
diff('012-R1-D20','body, son seul element word',r'\unsure{élémt|élément}','élément',r'\unsure{élémt|élément}',False,True,'abbreviation expanded or spelling modernised','no','medium','The two acute strokes and tall l are visible; after them one long low stroke and a terminal upright do not determine whether the middle is abbreviated.',crop='06_element_word')
diff('012-R1-D21','body, empty-figure subscript before car',r'\varnothing_{\mathcal{F}}',r'\emptyset_{\mathfrak{F}}',r'\varnothing_{\mathcal{F}}',False,True,'misread symbol or index','no','medium','The subscript is the same family F with swept upper arm and hooked foot. Its glyph convention follows the marked first family occurrence. The two empty-set macro names alone are not counted as a difference.',crop='06_element_word',mathematical=True)
diff('012-R1-D22','(1.19), empty-figure subscript',r'\varnothing_{\mathcal{F}}',r'\emptyset_{\mathfrak{F}}',r'\varnothing_{\mathcal{F}}',False,True,'misread symbol or index','no','medium','Half b shows a small swept-arm family F below the slashed open oval, distinct from the two plain outer Fs; recurring alphabet is marked at the earlier occurrence.',box=[1021,1222,1178,1324],mathematical=True)
# Remarks and definitions.
diff('012-R1-D23','Remarques a), initial Les','Les','les','Les',False,True,'misread word','no','high','The initial letter is a large straight-stem capital L, followed by reduced es.',crop='07_remarques_initial')
diff('012-R1-D24','Remarques a), on définit M subset family F',r'M\subset\mathcal{F}',r'\mathcal{M}\subset\mathfrak{F}',r'\mathcal{M}\subset\mathcal{F}',True,True,'misread symbol or index','no','medium','Half b shows the same sweeping two-hump M and the swept-arm family F. Recurring alphabet alternatives are given at their respective first occurrences.',box=[1484,1440,1637,1522],mathematical=True)
diff('012-R1-D25','(1.20), leading M and family F in set',r'M=\{X\in\mathcal{F}',r'\mathcal{M}=\lbrace X\in\mathfrak{F}',r'\mathcal{M}=\{X\in\mathcal{F}',True,True,'misread symbol or index','no','medium','Half b shows the wide entry and two peaks of M and the family F’s swept cap; their recurring alphabet choices are retained.',box=[542,1583,851,1694],mathematical=True)
diff('012-R1-D26','(1.20), abbreviation before irréductible',r'\mathrm{str}^{\mathrm{t}}.','strict.',r'\mathrm{str}^{\mathrm{t}}.',False,True,'abbreviation expanded or spelling modernised','no','high','Half b shows baseline str, a raised t, and a point. No baseline ic is present.',box=[931,1572,1012,1649])
diff('012-R1-D27','(1.20), supremum name',r'\mathop{\mathrm{Sup}}\limits_i',r'\sup_i',r'\mathop{\mathrm{Sup}}\limits_i',False,True,'misread symbol or index','no','high','Half b shows a capital looped S followed by reduced u and descending p; dotted i is below.',box=[1400,1568,1482,1650],mathematical=True)
diff('012-R1-D28','after (1.20), canceled group before D’autre',r'\deleted{\unsure{Et|En}}',r'\struck{D’autre}',r'\deleted{\unsure{Et|En}}',False,True,'deletion state','no','medium','Crop 09 shows a very short crossed group above the live D. An E and an upright/crossing terminal favour Et, but En remains possible. It does not have the length or surviving letter forms of D’autre.',crop='09_deleted_before_dautre')
diff('012-R1-D29','D’autre part, on définit M par','M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','no','medium','The local M again has the sweeping entry and two peaks; first-occurrence alphabet uncertainty is carried consistently.',box=[1463,1752,1539,1838],mathematical=True)
diff('012-R1-D30','(1.21), M and family F',r'M=\{X\in\mathcal{F}\mid X\triangleleft X\}',r'\mathcal{M}=\lbrace X\in\mathfrak{F}\mid X\triangleleft X\rbrace',r'\mathcal{M}=\{X\in\mathcal{F}\mid X\triangleleft X\}',True,True,'misread symbol or index','no','medium','Half b independently shows the same two letter forms here; the Xs and triangle are unchanged.',box=[574,1842,1119,1934],mathematical=True)
diff('012-R1-D31','before (1.22), F in family F',r'F\in\mathcal{F}',r'F\in\mathfrak{F}',r'F\in\mathcal{F}',False,True,'misread symbol or index','no','medium','The ordinary first F has a straight cap; the second has a swept cap and turned foot. Recurring family alphabet choice follows its marked first occurrence.',box=[561,1920,691,1993],mathematical=True)
diff('012-R1-D32','before (1.22), son déployement',r'\unsure{déployement|déploiement}','déploiement','déployement',True,True,'abbreviation expanded or spelling modernised','no','high','Half b shows a long diagonal descender in the medial y after déplo; it is not an i with a dot.',box=[799,1909,1144,1998])
diff('012-R1-D33','(1.22), M in the set condition','M',r'\mathcal{M}',r'\mathcal{M}',True,False,'misread symbol or index','no','medium','The local M has the same broad two-peak form as the preceding definitions.',box=[810,1980,905,2054],mathematical=True)
diff('012-R1-D34','(1.22), last F',r'\unsure{\mathcal{F}|F}',r'F; note explicitly reads manuscript \mathfrak{F}',r'\mathcal{F}',True,False,'misread symbol or index','no','high','Half b shows a broad curved cap and a closed turned foot, unlike the plain deployment F at left. The family identity is resolved; recurring font uncertainty is already marked. H is credited for its explicit literal-reading note, despite the emended plain F in its displayed text.',box=[1030,1968,1117,2042],mathematical=True)
diff('012-R1-D35','last display label',r'\unsure{(1,23)|(1.23)}','(1.23)','(1,23)',True,True,'misread symbol or index','no','high','Half b shows the separator after 1 below the numeral baseline, with a descending tail; the label has a comma.',box=[265,2128,397,2202])
diff('012-R1-D36','bottom canceled phrase, equivalent',r'\unsure{équivalent}','équivalent',r'\unsure{équivalent|equivalent}',True,True,'deletion state','no','medium','The struck word’s equivale- skeleton and final upright are visible, but the possible acute lies under the descender of the inserted qui. Word identity is strong; accent remains open.',crop='10_bottom_revision')
diff('012-R1-D37','bottom insertion, adjective after données',r'\unsure{minima|minimes}',r'\uncertain{minimales}',r'\unsure{minima|minimes}',False,True,'misread word','yes','medium','The word has low repeated humps and short uprights, with no tall l for minimales. The terminal reduced strokes still allow minima or minimes.',crop='10_bottom_revision')
diff('012-R1-D38','bottom line, final d’y',"d’y","de s’y","d’y",False,True,'text not on the page','no','high','Half b shows one d, an apostrophe above the following y, and the long y descender. There is no intervening e or separate s.',box=[1523,2242,1652,2320])

CD=[]
def cd(place,c,reading,disposition,evidence,crop=None,box=None):
 d=dict(place=place,c=c,reading=reading,disposition=disposition,evidence=evidence);d.update(ev(crop,box));CD.append(d)
cd('slanted margin, first equivalence membership',r'\unsure{\in|\overset{\prime}{\in}}',r'\unsure{\in|\overset{\prime}{\in}}','retained','The detached oblique mark remains ambiguous between a prime-like addition and adjacent slanted prose.',crop='03_slanted_correction')
cd('slanted margin, canceled start before definition',r'\deleted{\unsure{F\triangleleft|F}}',r'\deleted{F\triangleleft}','resolved','The enhanced rotated view shows both an F and a separate triangle under cancellation.',crop='03_slanted_correction')
cd('body, first family F',r'\unsure{\mathcal{F}|\mathscr{F}}',r'\unsure{\mathcal{F}|\mathfrak{F}}','retained','Family identity is clear from swept cap and turned foot. Exact alphabet remains open, with alternatives aligned to the supplied notation table.',crop='05_family_f')
cd('body, son seul element word',r'\unsure{élémt|élément}',r'\unsure{élémt|élément}','retained','The long compressed middle does not separate abbreviated mt from ment; both acute marks and the l are visible.',crop='06_element_word')
cd('after (1.20), canceled short group',r'\deleted{\unsure{Et|En}}',r'\deleted{\unsure{Et|En}}','retained','Crossed upright favours t, but the terminal group is obscured by its cancellation.',crop='09_deleted_before_dautre')
cd('before (1.22), deployment word',r'\unsure{déployement|déploiement}','déployement','resolved','Half b shows the medial letter’s diagonal descender, deciding y.',box=[799,1909,1144,1998])
cd('(1.22), last letter',r'\unsure{\mathcal{F}|F}',r'\mathcal{F}','resolved','Swept cap and turned foot identify the family glyph, unlike ordinary F at the start of the same formula. General family-font ambiguity is separately marked at its first occurrence.',box=[1030,1968,1117,2042])
cd('last display label',r'\unsure{(1,23)|(1.23)}','(1,23)','resolved','The separator is visibly lower than the digits and has a tail.',box=[265,2128,397,2202])
cd('bottom deletion, equivalent',r'\unsure{équivalent}',r'\unsure{équivalent|equivalent}','retained','Underlying word is readable, but the accent is not separable from the inserted qui above it.',crop='10_bottom_revision')
cd('bottom insertion, adjective',r'\unsure{minima|minimes}',r'\unsure{minima|minimes}','retained','Low humps and terminal reduced strokes do not resolve a versus es; no tall l supports H’s minimales.',crop='10_bottom_revision')

I=[]
def inv(element,kind,position,words):I.append(dict(element=element,kind=kind,position=position,first_words_or_objects=words,sheet_kind='text',hand='his hand',transcribed='yes'))
inv('manuscript page number','text','top centre','11')
inv('implication diagram (1.18), including oblique frame','diagram','upper centre','G triangleleft F; G preccurlyeq F; G leq F; G parallel F; G ll F; G compatibility F; five downward double arrows')
inv('uncertain state of extra upright in dark diagram sign','deletion','lower-right vertex of (1.18)','live upright / canceled upright alternatives')
inv('six-relation classification paragraph','text','below diagram','Parmi les six relations')
inv('slanted correction of order-relation claim','margin note','left margin alongside first two paragraphs','Non, triangleleft n’est pas rel. d’ordre')
inv('canceled start of marginal definition','deletion','slanted margin after écrire','F triangleleft')
inv('marginal proposed reflexivization, within note','display','last line of slanted note','F trianglelefteq F déf iff F triangleleft F ou F=F.')
inv('reflexivity paragraph','text','middle, above (1.19)','La relation [compatibility sign] est')
inv('de plus insertion','insertion','above est réflexive','de plus')
inv('empty-figure equivalence (1.19)','display','middle','F parallel F iff F = empty figure; figure vide.')
inv('underlined heading','text','below (1.19)','Remarques')
inv('remark a) introduction','text','lower half, above (1.20)','a) Les relations triangleleft et leq se déterminent mutuellement')
inv('irreducible definition (1.20)','display','lower half','M={X in family F | X str raised t. irréductible pour leq, i.e. X leq Sup_i F_i implies exists i avec X leq F_i}')
inv('reference to incidence definition','text','after (1.20)','puis triangleleft par (1.17).')
inv('canceled opening group','deletion','above D of D’autre part','Et / En')
inv('converse reconstruction introduction','text','above (1.21)','D’autre part, connaissant triangleleft on définit M par')
inv('self-incidence definition (1.21)','display','lower quarter','M={X in family F | X triangleleft X}')
inv('deployment introduction','text','above (1.22)','puis, pour F in family F, son déployement')
inv('deployment definition (1.22)','display','lower quarter','tilde F={X in M | X triangleleft family F}')
inv('final equivalence introduction','text','above (1,23)','et enfin')
inv('order-recovery equivalence (1,23)','display','near foot','F leq G iff tilde F subset tilde G')
inv('unfinished concluding sentence','text','last two baselines','Donc, pour déterminer … fixent la structure d’atelier, il est indifférent d’y')
inv('canceled conclusion phrase','deletion','last paragraph, first baseline','la structure, il est équivalent / equivalent')
inv('replacement conclusion phrase','insertion','above canceled conclusion','les données minima / minimes qui')

view_times=[('whole','/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012.jpg','11:20:00'),('half_a','/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012_a.jpg','11:20:06'),('half_b','/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012_b.jpg','11:20:32')]
ct=['11:22:28','11:22:44','11:23:25','11:24:25','11:24:34','11:24:46','11:25:00','11:25:05','11:25:19','11:25:36','11:27:26']
for key,t in zip(sorted(crop_info),ct):view_times.append(('crop',str(out/'crops'/f'{key}.jpg'),t))
views=[dict(image=p,role=role,viewed_utc='2026-11-20 '+t+' UTC') for role,p,t in view_times]
U=[
 dict(place='(1.18), dark compatibility sign',reading='full zigzag sign with extra upright live',alternatives=['the extra upright is canceled residue; zigzags live'],confidence='medium',evidence='Crop 02: separate upright survives, but dark retracing obscures stroke history.'),
 dict(place='(1.18), lower-right final F',reading='F',alternatives=[r'\mathbb{F}'],confidence='medium',evidence='Crop 02: two upright tracks join at bottom; ordinary retracing and deliberate doubling remain possible.'),
 dict(place='slanted margin, membership',reading=r'\in',alternatives=[r'\overset{\prime}{\in}'],confidence='low',evidence='Crop 03: detached oblique mark above membership lies among adjoining note strokes.'),
 dict(place='slanted margin, first M; recurring collection letter',reading=r'\mathcal{M}',alternatives=['M'],confidence='medium',evidence='Crop 03 and half b: sweeping entry and two upper humps do not identify a unique typeset alphabet.'),
 dict(place='body, first family F; recurring family glyph',reading=r'\mathcal{F}',alternatives=[r'\mathfrak{F}'],confidence='medium',evidence='Crop 05: swept cap, crossing mid arm, curved foot; exact calligraphic/Gothic typography unresolved.'),
 dict(place='body, son seul element word',reading='élémt',alternatives=['élément'],confidence='medium',evidence='Crop 06: compressed middle and terminal upright do not separate full versus abbreviated form.'),
 dict(place='after (1.20), deletion',reading='Et',alternatives=['En'],confidence='medium',evidence='Crop 09: a crossed terminal upright favours t, but cancellation prevents a confident final-letter reading.'),
 dict(place='bottom deletion, equivalent',reading='équivalent',alternatives=['equivalent'],confidence='medium',evidence='Crop 10: possible accent overlaps the inserted qui; word skeleton is readable.'),
 dict(place='bottom insertion, adjective',reading='minima',alternatives=['minimes'],confidence='medium',evidence='Crop 10: low repeated humps and reduced final stroke do not decide the ending.')
]
notes=[dict(
 content='The page arranges six relations in an implication diagram (1.18), initially calls four of them order relations, distinguishes the two symmetric relations, and gives the empty-figure criterion for self-parallelism (1.19). Remark a) explains recovery of incidence from the order using strict irreducibles (1.20), then recovery of the distinguished family, deployment and order from incidence in (1.21), (1.22), and the literally comma-numbered (1,23). The final sentence about data fixing the atelier structure continues off the page.',
 math_reading_decisions='Five implication arrows point downward. The enclosure has two left-corner gaps. The dark compatibility sign includes an uncertain extra upright; the two cleaner body signs are open opposed zigzags. The marginal proposed definition repeats F in all variable positions; no G is supplied. Formula (1.22) literally ends in the family F glyph, even though the preceding prose names an ordinary F. Tildes are waves, the final inclusion is open with no lower bar, and the index under Sup and both F subscripts in (1.20) are i; the quantified variable after the existential sign is also i. H’s note about the retraced last inequality is credited; no recoverable canceled operand was found there.',
 author_doubts=[r'Non, $\triangleleft$ n’est pas rel. d’ordre, elle est transitive mais non réflexive, car $F\triangleleft F\Longleftrightarrow F\unsure{\in|\overset{\prime}{\in}}\unsure{\mathcal{M}|M}$',r'Pour avoir une relation d’ordre il faudrait écrire $F\trianglelefteq F\overset{\mathrm{déf}}{\Longleftrightarrow}F\triangleleft F$ ou $F=F$.'],
 titles_dates_counts='Own page number 11; underlined Remarques with a); display labels (1.18), (1.19), (1.20), (1.21), (1.22), (1,23); internal reference (1.17). No date, title sheet, archive pencil number or page-count declaration is visible.'
)]
checks=[
 dict(statement_id='scan012-(1.18)',type='carried as background without fault found',outcome="read as the author's assertion; no mathematical verification performed"),
 dict(statement_id='scan012-marginal-order-correction',type='carried as background without fault found',outcome="read as the author's assertion; no mathematical verification performed; the note itself challenges the initial claim and its repeated F variables are preserved"),
 dict(statement_id='scan012-(1.19)',type='carried as background without fault found',outcome="read as the author's assertion; no mathematical verification performed"),
 dict(statement_id='scan012-(1.20)-(1,23)',type='carried as background without fault found',outcome="read as the author's assertion; no mathematical verification performed; the reference (1.17) was not available for a proof check in this single-page packet")
]
proposals=[
 dict(sign='collection M',latex=r'\unsure{\mathcal{M}|M}',ink='Curved rising entry and two upper humps in the margin and lower displays.',alternatives=['ordinary M']),
 dict(sign='family F',latex=r'\unsure{\mathcal{F}|\mathfrak{F}}',ink='Swept cap and crossing middle arm; turned or looped foot, clearly separate from ordinary F.',alternatives=[r'\mathfrak{F}']),
 dict(sign='compatibility, clean body occurrences',latex=zig,ink='Two opposed zigzags, central diamond and four free diagonal tips; no horizontal caps.',alternatives=[]),
 dict(sign='compatibility, retraced diagram occurrence',latex=uncertain_sign,ink='Same diagonals with a distinct extra upright; its state remains uncertain.',alternatives=['upright canceled beneath the live zigzags']),
 dict(sign='retraced diagram operand F',latex=r'\unsure{F|\mathbb{F}}',ink='Two vertical tracks enclosing a narrow white channel and joining below.',alternatives=[r'\mathbb{F}']),
 dict(sign='empty figure',latex=r'\varnothing_{\mathcal{F}}',ink='Small open/slashed oval with family F below.',alternatives=[]),
 dict(sign='supremum abbreviation',latex=r'\mathop{\mathrm{Sup}}\limits_i',ink='Capital looped S, reduced u, descending p; dotted i underneath.',alternatives=[]),
 dict(sign='deployment',latex=r'\widetilde F,\widetilde G',ink='Separate wavy strokes over F and G.',alternatives=[])
]
report=dict(scan=12,reader='R1',started_utc='2026-11-20 11:19:55 UTC',finished_utc=None,status='draft',view_log=views,differences=D,c_doubts=CD,s_rows=[],inventory=I,notes=notes,check_events=checks,notation_proposals=proposals,abbreviations=[dict(form='rel.',expansion='relation'),dict(form='déf',expansion='définition'),dict(form=r'str^{t}.',expansion='strictement'),dict(form='i.e.',expansion='id est'),dict(form='élémt (uncertain)',expansion='élément'),dict(form='Sup',expansion='supremum')],unresolved=U,brief_feedback=[],crop_log=[],counts={})
for key in sorted(crop_info):
 meta=json.loads((out/'crops'/f'{key}.json').read_text())
 report['crop_log'].append(dict(image=str(out/'crops'/f'{key}.jpg'),source=meta['source'],box=meta['box'],rotation=meta['rotation'],width=meta['width'],transform=meta['transform'],created_utc=meta['created_utc']))
report['counts']=dict(whole_views=1,half_views=2,crops_created=len(crop_info),crop_views=len(crop_info),total_image_views=len(views),differences=len(D),c_doubt_loci=len(CD),c_doubts_resolved=sum(d['disposition']=='resolved' for d in CD),c_doubts_retained=sum(d['disposition']=='retained' for d in CD),inventory_elements=len(I),unresolved_loci=len(U),unsure_macros=len(re.findall(r'\\unsure\{',tex)),illegible_macros=len(re.findall(r'\\illegible\{',tex)),deleted_macros=len(re.findall(r'\\deleted\{',tex)),inserted_macros=len(re.findall(r'\\inserted\{',tex)))
(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report['counts'],indent=2))
