from pathlib import Path
import json,re,difflib
from datetime import datetime,timezone
ROOT=Path('/workspace/scratch/6d55c8c3e5a7')
D=ROOT/'work/readers/027/A'
C=(ROOT/'work/inputs/027/C.tex').read_text()
s=C
changes=[]
def ev(n):
 data=json.loads((D/'unresolved_frozen.json').read_text())['loci'][int(n)-1]
 return {'crop':str(D/f'crops/{int(n):02d}.jpg'),'source':str(ROOT/f"source/SP49_CW_109_scans/H109-02_109_scan027_{data['source']}.jpg"),'bbox':data['bbox']}
def change(id,place,c,reading,kind,evidence,n=None,confidence='high',source=None,bbox=None):
 d={'id':id,'place':place,'c':c,'h':None,'reading':reading,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence}
 d.update(ev(n) if n else {'crop':None,'source':source,'bbox':bbox})
 changes.append(d)
def sub(old,new):
 global s
 if old not in s: raise ValueError('not found '+old)
 s=s.replace(old,new,1)

# C's literal text is retained except for the individually documented places below.
old=r'\deleted{\unsure{l-2} ``play\'\' \unsure{no|not} ``s\'\'}'
# Explicit strings avoid Python quote escaping in the corresponding report fields.
old="\\deleted{\\unsure{l-2} ``play'' \\unsure{no|not} ``s''}"
new="\\deleted{\\unsure{l-2} ``play'' \\unsure{no|not} ``s}''"
sub(old,new)
change('304-final-quotes','304, end of cancelled play/no/s group',old,new,'deletion state (struck given live or live given struck)','The final two high strokes after s stand above and clear of the last return of the cancellation. The word and earlier quotation strokes are crossed. The final pair is therefore left live.',4,'medium')
old=r'\deleted{\unsure{l|it}}';new=r'\deleted{l}'
sub(old,new);change('306-old-l','306, before also',old,new,'misread word','One continuous tall loop with a low foot survives under the oblique strike; no second separate letter body or dot remains to support it.',6,'medium')
old=r'\unsure{l-6}';new='l-6'
sub(old,new);change('312-old-reference','312, cancelled reference after isn\'t',old,new,'misread symbol or index','The initial looped l, short horizontal and final closed lower bowl with an ascending lead-in distinguish l-6.',7)
old=r'\deleted{filtering \unsure{out|at|on|or}} \unsure{l-2|l-7}'
new=r'\deleted{filtering \raisebox{1.1ex}[0pt][0pt]{\unsure{out|at|on|or}} \unsure{l-2|l-7}}'
sub(old,new);change('313-cancelled-cluster','313, second physical line',old,new,'deletion state (struck given live or live given struck)','The two horizontal cancellation runs continue through the narrow reference cluster immediately before the live filtering. The preceding small uncertain word stands above the baseline. Letter and digit identities remain uncertain.',8,'medium')
old=r'Sent\deleted{\unsure{ann|en}}ence'
new=r'Sent\tikz[baseline=(sentA27.base)]{\node[inner sep=0pt] (sentA27) {\deleted{\unsure{ann|en}}};\node[anchor=base west,inner sep=0pt] at (sentA27.base west) {en};}ce'
sub(old,new);change('315-sentence-overlap','315, first word',old,new,'insertion or placement','The dense old and new medial letters share the same horizontal space after Sent; the visible live ending is ence. Printing the uncertain old ann/en as a separate preceding syllable would duplicate that physical space. The buried old letters remain doubtful.',9,'medium')
old=r'\deleted{\unsure{to}}';new=r'\deleted{to}'
sub(old,new);change('315-old-to','315, before in order to',old,new,'misread word','The short t stem and cross-stroke are followed by a closed right-hand loop; a diagonal cancellation crosses their lower part.',10,'medium')
old='respect.'
new=r'\tikz[baseline=(respectA27.base)]{\node[inner sep=0pt] (respectA27) {respect.};\draw[line width=.65pt,line cap=round] ([xshift=1.2em,yshift=-.55ex]respectA27.base west) -- ++(.12em,-.13ex);}'
sub(old,new);change('315-respect-mark','315, under the beginning of respect',old,new,'drawing or diagram','A separate short dark hooked stroke lies below the beginning of respect, just to the right of the vertical rule. It is reproduced geometrically without assigning punctuation function. The separate final stop after respect is retained.',11)
old=r'\inserted{certainly}'
new=r'\raisebox{1.2ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{certainly}}}'
sub(old,new);change('315-certainly-raised','315, cancelled parenthesis, above true',old,new,'insertion or placement','Certainly is interlinear, above the gap before true; its baseline is visibly higher than This is true. It remains within the abandoned parenthesis.',12)
old=r'\unsure{presumably} \inserted{as far as our}'
new=r'\tikz[baseline=(presA27.base)]{\node[inner sep=0pt] (presA27) {\unsure{presumably}};\node[anchor=base west,inner sep=0pt] at ([yshift=1.3ex]presA27.base west) {\inserted{as far as our}};}'
sub(old,new);change('315-as-far-raised','315, cancelled parenthesis, over presumably',old,new,'insertion or placement','As far as our occupies the interline immediately above presumably and overlaps it horizontally. The broad cancellation crosses the lower line and part of the upper addition. Presumably remains uncertain.',12)
old=r'\unsure{No|Now}---.'
new=r'\tikz[baseline=(noA27.base)]{\node[inner sep=0pt] (noA27) {\unsure{No|Now}};\fill ([xshift=.15em,yshift=-.45ex]noA27.base west) circle (.3pt);}- -.'
sub(old,new);change('315-no-terminal-marks','315, end of cancelled parenthesis after goes).',old,new,'other','Two independent low short horizontal marks and a final point follow the doubtful No/Now. The long higher stroke with its downturned end is the cancellation, not a third low dash. A small distinct point beneath the left part of N is retained geometrically.',13,'medium')
old="knowledge goes)''..."
new="knowledge goes\\tikz[baseline=0pt,x=1ex,y=1ex]{\\fill (.07,.22) circle (.025);\\draw[line width=.5pt] (.22,.45)--(.42,.51);})''..."
sub(old,new);change('315-before-close-marks','315, live final parenthesis, between goes and its closer',old,new,'drawing or diagram','A low point and short higher sloping stroke occur just before the tall closing parenthesis. They are separate from the three following low dots and are retained as geometry; no lexical or punctuation function is assigned.',14,'medium')
old=r'\inserted{would}'
new=r'\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.55pt] (0,-1.05)--(.15,-.45)--(.3,-1.02);}\raisebox{1.3ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{would}}}'
sub(old,new);change('315-would-raised','315, l.-3, between which and allow',old,new,'insertion or placement','Would is written above the start of allow; a small h-shaped caret lies below the gap between which and allow. Both height and the lower caret are preserved.',15)
old=r'\deleted{\unsure{it}}';new=r'\deleted{it}'
sub(old,new);change('316-old-it','316, l12, before is',old,new,'misread word','The upper i point, short first stem and taller t with its cross-stroke survive the diagonal cancellation distinctly.',16)
old=r'\deleted{\unsure{\&}}';new=r'\deleted{\&}\tikz[baseline=0pt,x=1ex,y=1ex]{\fill (.1,-.32) circle (.035);}'
sub(old,new);change('326-old-ampersand','326, after l-12',old,new,'misread symbol or index','The cancelled sign has a tall upper loop and a lower loop with a crossing diagonal, matching an ampersand. A separate low point below/right of its foot is also preserved geometrically.',19)
old=r'\tikz[remember picture,overlay]\coordinate(scxxviim); \inserted{\& l-3} ``commutes \uline{with}\'\' '
old="\\tikz[remember picture,overlay]\\coordinate(scxxviim); \\inserted{\\& l-3} ``commutes \\uline{with}''"
new=r'''\tikz[baseline=(commA27.base)]{\node[anchor=base west,inner sep=0pt] (commA27) {``commutes \uline{with}''};\node[anchor=south west,inner sep=0pt] (addA27) at ([xshift=-.3em,yshift=.45ex]commA27.north west) {\inserted{\& l-3}};\fill ([xshift=.15em,yshift=.9ex]addA27.base east) circle (.3pt);\draw[line width=.55pt] ([xshift=-.35em,yshift=1ex]commA27.base west)--([xshift=-.6em,yshift=-1.45ex]commA27.base west)--([xshift=-.43em,yshift=-.82ex]commA27.base west)--([xshift=-.32em,yshift=-1.1ex]commA27.base west);}'''
sub(old,new)
oldpointer=r'\tikz[remember picture,overlay]{\coordinate(scxxviin); \draw (scxxviim) -- ([yshift=.65ex]scxxviin) -- ([xshift=.09em,yshift=.93ex]scxxviin);}'
sub(oldpointer,'')
change('326-raised-addition-pointer','326, & l-3 over commutes; pointer below the gap',old+'\n'+oldpointer,new,'insertion or placement','The addition stands above commutes. The slanted stroke starts immediately left of its opening quotes and ends with a small return below the text line, above the 327 formula; it does not attach to either triangular symbol. A small high point after the raised 3 is separately retained.',20)
old=r'\deleted{\unsure{\'\'}}'
old="\\deleted{\\unsure{''}}";new="\\deleted{''}"
sub(old,new);change('327-old-quotes','327, l-14, immediately after isn\'t',old,new,'misread symbol or index','Two small high quotation legs survive beneath the short overstrike before there. The count is sufficiently distinct to remove the uncertainty while preserving their cancelled state.',22,'medium')
old="\\inserted{l-5 ``developing\\unsure{''}}"
new="\\raisebox{1.9ex}[0pt][0pt]{\\inserted{l-5 ``enveloping\\unsure{''|'}}}"
sub(old,new);change('329-enveloping','329, raised l-5 entry at right',"developing","enveloping",'misread word','The first letter is a low closed e loop, followed by n and v, before the clear eloping; there is no initial d ascender. The word is enveloping.',25)
change('329-raised-entry','329, l-5 entry above/right of semisimplicial',"\\inserted{l-5 ``developing\\unsure{''}}",new,'insertion or placement','The entire l-5 entry is raised above the semisimplicial line and reached by the long angled connector already present in C. The closing strokes at the clipped edge remain uncertain.',25)
change('329-clipped-closer','329, after enveloping',"\\unsure{''}","\\unsure{''|'}",'misread symbol or index','Only a short raised stroke can be seen at the cut right edge; the surviving ink does not decide one versus two closing strokes.',25,'low')
old=r"\margin{? (I'm not \unsure{certa|certain} if it is 1 or 2 \unsure{p|r}}"
new=r"\margin{\begin{tikzpicture}[x=1em,y=1ex,baseline=(margA27.base)]\node[anchor=base west,inner sep=0pt] at (.8,2.1) {?};\begin{scope}[rotate=14]\node[anchor=base west,inner sep=0pt] (margA27) at (0,0) {I'm not certa};\node[anchor=base west,inner sep=0pt] at (-.1,-1.8) {if it is 1 or 2 p};\draw[line width=.45pt] (-.65,-.55) .. controls (-1.15,-2.5) and (-.25,-3.0) .. (1.3,-2.8);\end{scope}\end{tikzpicture}}"
sub(old,new)
change('329-certa','329, clipped right margin, first prose line',r'\unsure{certa|certain}','certa','misread word','The visible beginning reads certa. The right edge cuts off what would follow; no visible in is supplied.',25,'medium')
change('329-final-p','329, clipped right margin, final visible letter',r'\unsure{p|r}','p','misread symbol or index','The surviving stem descends below the line of 1 or 2 and has the beginning of an upper bowl. This decides p over a nondescending r, although the rest beyond the edge is missing.',25,'medium')
change('329-margin-layout','329, slanted right-margin question and two prose lines',old,new,'insertion or placement','The question mark stands above the two slanted prose lines. The large opening curved stroke is lower-left beside the second line and curves underneath it; it is drawn at that observed position. The right-hand side remains physically right.',25)
# A small dark mark in the inter-entry blank, not a reconstructed letter.
mark=r'\noindent\hspace*{3em}\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.55pt,line cap=round] (0,0)--(.23,.07);}\par'
sub('\n\n316.', '\n\n'+mark+'\n\n316.')
change('315-316-short-mark','blank between the 315 continuation and 316','',mark,'drawing or diagram','One very short oblique dark dash lies in the blank just right of the left rule. The crop does not reveal a letter or reference; only its visible geometry is represented.',28,'medium')

# Anchored long rules remain beside/through the corresponding text.
sub('\\scanpage{27}\n',r'''\scanpage{27}
\begingroup
\setlength{\parindent}{0pt}
\everypar{\hangindent=2.9em\hangafter=1}
\noindent\tikz[remember picture,overlay]{\coordinate (ruleA27top);}
''')
sub('l.17 ``its\'\' ',"\\noindent\\hspace*{2.9em}l.17 ``its'' ")
sub("one to compute''", "one to compute''\\tikz[remember picture,overlay]{\\coordinate (ruleA27gap) at (0,-2.1ex);}")
sub('316. l.1',r'\noindent\tikz[remember picture,overlay]{\coordinate (ruleA27restart) at (0,1.7ex);}316. l.1')
sub("\\deleted{filtering", r'\noindent\hspace*{2.9em}\deleted{filtering')
# Continuation references physically start to the right of the left rule.
for prefix in ['l-17 ``allows','l-5 ``don\'t','l-10 doesn\'t','l12 ``don\'t']:
 sub('\n\n'+prefix,'\n\n'+r'\noindent\hspace*{2.9em}'+prefix)
rules=r'''\tikz[remember picture,overlay]{\coordinate (ruleA27bottom) at (0,-3ex);
% left rule, two observed segments with a small break above 316
\draw[line width=.35pt] ([xshift=1.9em,yshift=1.3ex]ruleA27top)--([xshift=1.9em]ruleA27top |- ruleA27gap);
\draw[line width=.35pt] ([xshift=1.9em]ruleA27top |- ruleA27restart)--([xshift=1.9em]ruleA27top |- ruleA27bottom);
% right rule, beside and sometimes through the end of long text lines
\draw[line width=.4pt] ([xshift=\linewidth,yshift=1.3ex]ruleA27top)--([xshift=\linewidth]ruleA27top |- ruleA27bottom);
}
\endgroup
'''
sub('\n\n% archive sheet number: 26','\n'+rules+'\n% archive sheet number: 26')
change('left-vertical-rule','left edge of correction text, beside page-reference column','',r'\draw[line width=.35pt] ([xshift=1.9em,yshift=1.3ex]ruleA27top)--([xshift=1.9em]ruleA27top |- ruleA27gap); \draw[line width=.35pt] ([xshift=1.9em]ruleA27top |- ruleA27restart)--([xshift=1.9em]ruleA27top |- ruleA27bottom);','drawing or diagram','A fine nearly vertical rule runs at x241–246 from about y97 to y1302, breaks briefly, resumes about y1325 and continues to y2338. It separates the page references from most corrections and is anchored to those text blocks.',None,'high',str(ROOT/'source/SP49_CW_109_scans/H109-02_109_scan027.jpg'),[232,86,254,2344])
change('right-vertical-rule','right side of main correction text','',r'\draw[line width=.4pt] ([xshift=\linewidth,yshift=1.3ex]ruleA27top)--([xshift=\linewidth]ruleA27top |- ruleA27bottom);','drawing or diagram','A dark vertical rule at x1517–1525 runs from about y95 to the foot near y2348. It crosses the ends of some long lines, including the vicinity of respect and the right-margin note; it is retained beside the text.',None,'high',str(ROOT/'source/SP49_CW_109_scans/H109-02_109_scan027.jpg'),[1507,84,1534,2353])
(D/'reading.tex').write_text(s)

# Explicit C doubt decisions, plus all page-specific alternatives and notation confirmations.
cd=[]
def doubt(place,c,reading,resolved,evidence,n=None,confidence='medium',source=None,bbox=None):
 d={'place':place,'c':c,'reading':reading,'resolved':resolved,'confidence':confidence,'evidence':evidence}
 d.update(ev(n) if n else {'crop':None,'source':source,'bbox':bbox})
 cd.append(d)
doubt('top entry, page reference',r'\unsure{302}',r'\unsure{302}',False,'The lower shapes favour 302, but their upper contours are faint or missing in the reproduction; the crop does not restore them.',1)
doubt('top entry, line reference',r'\unsure{15}',r'\unsure{15}',False,'The first upright and rounded lower ending favour 15; the erased/faint top of the second character does not permit full certainty.',1)
doubt('303, cancelled word before which',r'\unsure{with|who}',r'\unsure{with|who}',False,'The crossing obscures the central strokes and terminal loop; the preserved tall strokes do not decisively separate with from who.',2,'low')
doubt('304, cancelled line reference',r'\unsure{l-2}',r'\unsure{l-2}',False,'The first l is visible, but the putative final 2 shares strokes with the broad zigzag cancellation.',4,'low')
doubt('304, cancelled no/not',r'\unsure{no|not}',r'\unsure{no|not}',False,'An n and rounded o survive; the final area is traversed by the cancellation, leaving a possible t undecidable.',4,'low')
doubt('306, cancelled sign before also',r'\unsure{l|it}','l',True,'One looped tall body and low foot remain, without a second distinct stem or i dot.',6)
doubt('312, cancelled line reference',r'\unsure{l-6}','l-6',True,'Looped l, a short dash and the closed lower bowl of 6 are independently visible.',7,'high')
doubt('312, cancelled lets',r"\unsure{lets|let's}",r"\unsure{lets|let's}",False,'The terminal t crossbar and curled s survive, but the apostrophe position is crossed by a heavy diagonal.',7,'low')
doubt('313, small raised cancelled word',r'\unsure{out|at|on|or}',r'\raisebox{1.1ex}[0pt][0pt]{\unsure{out|at|on|or}}',False,'The upper cluster is clearly raised; its short loops and final turn do not decide among the supplied alternatives.',8,'low')
doubt('313, narrow reference before live filtering',r'\unsure{l-2|l-7}',r'\deleted{\unsure{l-2|l-7}}',False,'The reference lies in the cancellation path; the digit remains obscured and may be 2 or 7.',8,'low')
doubt('315, overwritten medial letters of Sentence',r'\unsure{ann|en}',r'\unsure{ann|en}',False,'The correction is visibly superposed on the medial syllable; dense coincident humps do not reveal the exact old sequence.',9,'low')
doubt('315, false start before in order to',r'\unsure{to}','to',True,'A t stem/crossbar and closed right-hand o loop survive the short cancellation.',10)
doubt('315, cancelled presumably',r'\unsure{presumably}',r'\unsure{presumably}',False,'The descending p, medial small humps and final y favour presumably, but the long crossing strokes conceal part of its centre.',12)
doubt('315, cancelled No/Now',r'\unsure{No|Now}',r'\unsure{No|Now}',False,'A capital N and rounded continuation remain; the last part is entwined with the heavy cancellation return.',13,'low')
doubt('316, cancelled it before is',r'\unsure{it}','it',True,'Separate i point and stem, followed by a taller crossed t, are visible.',16,'high')
doubt('316, cancelled final to/is',r'\unsure{to|is}',r'\unsure{to|is}',False,'The tall crossed loop and curled lower stroke remain compatible with both supplied readings.',17,'low')
doubt('326, cancelled ampersand',r'\unsure{\&}',r'\&',True,'Upper and lower loops plus the oblique joining/crossing stroke distinguish the sign.',19,'high')
doubt('327, cancelled closing quotes after isn\'t',"\\unsure{''}","''",True,'Two small elevated quotation legs remain beneath their short overstrike.',22)
doubt('329, clipped closer after enveloping',"\\unsure{''}","\\unsure{''|'}",False,'The edge leaves one raised dark remnant; it cannot establish whether a second closing stroke was present.',25,'low')
doubt('329, clipped certa/certain',r'\unsure{certa|certain}','certa',True,'The surviving letters read certa; the image edge has removed any continuation, which is not supplied.',25)
doubt('329, clipped last letter p/r',r'\unsure{p|r}','p',True,'The remnant includes a stem below the numeral baseline with part of an upper bowl; r does not account for that descender.',25)
# Context-only confirmations are not changes when C already gives the same literal text.
doubt('C_context: 303, final capital of image of A by A',r'A\text{ by }A',r'A\text{ by }A',True,'The final capital has a lower loop at the start of its crossbar; the only detached high group is the closing quote pair. No separate prime survives.',3,'high')
doubt('C_context: 315, respect. concerning','respect. concerning','respect. concerning',True,'A separate low stop follows respect; the following concerning begins with a small c in half a. Five low marks before theory are retained as C gives them.',11,'high')
doubt('C_context: 316, i(a)',r'i(a)',r'i(a)',True,'A dotted i precedes two round parentheses containing a closed-loop a.',16,'high')
tri1=r'\mathord{\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.085ex,line cap=round,line join=round] (.19,0)--(.86,1.37)--(1.08,0)--(.71,.025) (.61,.032)--(.19,0) (-.05,.08)--(.51,1.12);}}'
tri2=r'\mathord{\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.085ex,line cap=round,line join=round] (.20,0)--(.83,1.12)--(1.22,.05)--(.82,.04) (.72,.02)--(0,0)--(.64,.99);}}'
tri3=r'\mathord{\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.09ex,line cap=round,line join=round] (.16,-.05)--(.77,1.5)--(1.21,.04)--(.16,.0) (.49,1.36)--(-.04,0)--(.21,0);}}'
doubt('C_context: 327, first triangle',tri1,tri1,True,'The outer left stroke ends just above and clear of the baseline; a small break appears in the triangle base. C\'s individually drawn contour is retained.',21,'high')
doubt('C_context: 327, second triangle',tri2,tri2,True,'The lower end of the outer diagonal meets the extended base; this differs from the first triangle and is already represented by C.',21,'high')
doubt('C_context: 327, alpha, arrow and /F',r'\alpha:\longrightarrow /F',r'\alpha:\longrightarrow /F',True,'The alpha loop, two colon points, right-pointing arrowhead and baseline slash before ordinary F are separately visible; F has no independent doubled stem.',21,'high')
doubt('C_context: 329, third triangle',tri3,tri3,True,'This taller triangle has an outer diagonal reaching the base. Its distinct proportions and doubled left side are already in C.',24,'high')
doubt('C_context: 334, b in A with n-1',r'b\in A_{n-1}',r'b\in A_{n-1}',True,'The open-right membership sign has a separate middle bar; n, a short minus and a hooked 1 form one lowered group after A.',26,'high')
# Other supplied contextual statements, verified on the given halves/crops.
doubt('C_context: 303 comment','- not clear what you mean.','- not clear what you mean.',True,'The second physical line visibly has the initial dash and the complete comment with its final point.',None,'high',str(ROOT/'source/SP49_CW_109_scans/H109-02_109_scan027_a.jpg'),[265,205,861,260])
doubt('C_context: 315 judgement and replacement','difficult to understand. Possibly:','difficult to understand. Possibly:',True,'The judgement is followed by a strong stop and Possibly with a colon. The replacement retains its stated uncertainty and the cancelled first attempt.',None,'high',str(ROOT/'source/SP49_CW_109_scans/H109-02_109_scan027_a.jpg'),[747,762,1496,838])
doubt('C_context: 327 unfinished question',"should it be '","should it be '",True,'The visible wording ends with a single high tick; no completed alternative formula or question mark is supplied.',None,'high',str(ROOT/'source/SP49_CW_109_scans/H109-02_109_scan027_b.jpg'),[787,627,1090,679])
doubt('C_context: 328 proposed verbal equality',"should ``wouldn't'' = ``shouldn't''","should ``wouldn't'' = ``shouldn't''",True,'The live should is followed by quoted wouldn\'t, two equality strokes and quoted shouldn\'t. The earlier wouldn\'t is cancelled.',23,'high')
doubt('C_context: 329 explanatory parenthesis','(doubled side is missing)','(doubled side is missing)',True,'The two parentheses enclose the visible explanatory words; no mathematical repair to the displayed handwritten glyph is made.',None,'high',str(ROOT/'source/SP49_CW_109_scans/H109-02_109_scan027_b.jpg'),[468,932,938,1005])

remaining=[]
for d in cd[:21]:
 if not d['resolved']:
  remaining.append({'place':d['place'],'reading':d['reading'],'alternatives':d['reading'],'confidence':d['confidence'],'reason':d['evidence']})

inventory=[]
def inv(kind,pos,words,hand='his hand'):
 inventory.append({'sheet_kind':'list','hand':hand,'element':f'{len(inventory)+1:02d}','kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
inv('drawing','left reference/text boundary, nearly full height','Vertical rule, two segments with small gap above 316')
inv('drawing','right edge of main text, nearly full height','Vertical rule through ends of some long lines')
entries=[('top, faint first line','302 l.15 ``its'),('303, two physical lines','303 l.1 ... which will be; l2 ... we\'ve got; l.-3 ... image of A by A; - not clear what you mean.'),('304, single long line','304 l-15 ... commutes with ... also l-13.'),('305','305 l.5 ... interpret ... l14 commutes with'),('306','306 l.19 ... its ... also l-5. l-4 ... test category'),('309','309 l.-8 ... on the previous'),('312','312 l-.8 ... isn\'t'),('313, first line','313 l9 ... shouldn\'t ... l.18 don\'t ... l-12 commutes with'),('313, second line','cancelled filtering cluster; live filtering\'\''),('314','314 l.5 ... isn\'t ... l.6 as is'),('315, long entry','315 Sentence starting l.7 - difficult to understand. Possibly:'),('315, proposed wording','I add this comment, of course ... push home ... does the cat. ... stand singled out.'),('315, live final parenthesis','(This certainly seems to be so as far as our present knowledge goes)\'\'...'),('315, continuation references','l.17 ... its ... l.-3 ... and which would allow one to compute'),('316','316. l.1 ... shouldn\'t ... l12 i(a) ... is a'),('317','317. l.11 ... its ... l-16 isn\'t'),('320','320 l 8. ... indispensable ... l-15 developing ... l-8 its'),('321','321 l.9 ... isn\'t'),('323','323 l13 ... don\'t'),('326','326 l-12 ... & l.-8 ... commutes with ... and'),('327, first line','p.327. l7 alpha, triangles, arrow and /F; should it be'),('327, second line','l-17 ... allows one to ... l-16 doesn\'t ... l-14 isn\'t ... there!'),('327, third line','l-5 ... don\'t'),('328, first line','p328 l-12 ... should wouldn\'t = shouldn\'t'),('328, second line','l-10 doesn\'t'),('329, first line','p329 l.6 triangular glyph (doubled side is missing) ... its'),('329, second line','l12 ... don\'t ... l-13 makes sense ... l.-13 semisimplicial.'),('333','p.333 l.-12 ... makes sense'),('334','p.334 l.3 b in A_{n-1}; l-6 its also in l-5.')]
for p,w in entries:inv('text',p,w)
for pos,words in [('303 before which','with/who'),('304 after also l-13','l-2 play no/not s; final quote pair live'),('306 before also','l'),('312 after isn\'t','l-6 lets/let\'s'),('313 second line','filtering, raised out/at/on/or, l-2/l-7'),('315 in Sentence','ann/en overwritten by en'),('315 before in order to','to'),('315 after singled out','(This is certainly true presumably/as far as our at the present knowledge goes). No/Now- -.'),('316 before is','it'),('316 after is a and the closing quotation pair','to/is'),('326 after l-12','old ampersand'),('327 after isn\'t','old closing quotation pair'),('328 before should','wouldn\'t')]:inv('deletion',pos,words)
inv('text','313, within cancelled cluster above baseline','out/at/on/or raised')
for pos,words in [('315 over medial Sentence','live en over old ann/en'),('315 cancelled parenthesis above true','certainly'),('315 cancelled parenthesis above presumably','as far as our'),('315 above allow','would'),('326 above commutes','& l-3'),('329 above/right of semisimplicial','l-5 enveloping with clipped closing quote')]:inv('insertion',pos,words)
for pos,words in [('306','single underline beneath category'),('309','single underline beneath the'),('315 proposed wording','single underline beneath push home'),('315 proposed wording','single underline beneath no more'),('315 proposed wording','single underline beneath to express'),('315 proposed wording','single underline beneath does'),('315 proposed wording','single underline beneath stand'),('326','single underline beneath with'),('327','single underline beneath one')]:inv('text',pos,words)
for pos,words in [('315 under respect','short dark hook without assigned punctuation function'),('315 at cancelled No/Now','small point beneath left part and two low short dashes'),('315 just before live closing parenthesis','small point and slanted short stroke'),('315 below which/allow gap','small insertion caret'),('between 315 and 316','short oblique isolated dash'),('326 below old ampersand','separate low point'),('326 below gap before commutes','downward oblique pointer with small return, not joined to formula'),('326 after raised 3','small high isolated point'),('327 before arrow','first triangle, outer diagonal clear of base'),('327 after arrow','second triangle, outer diagonal meeting base'),('329 first line','third triangle, taller, doubled left side'),('329 after semisimplicial','long angled connector with short branch'),('329 right-margin note','large low opening curved stroke')]:inv('drawing',pos,words)
inv('margin note','right of 329 second line; slanted and clipped','?; I\'m not certa / if it is 1 or 2 p')
inv('text','lower-left archive corner','26, preserved only as archive comment','another unnamed hand')

notation=[
 {'sign':'A','location':'303 image of A by A','reading':r'A\text{ by }A','evidence':'Crop03: ordinary capital contours; final high strokes are the closing quote pair, not a separate prime.'},
 {'sign':r'i(a)','location':'316 l12','reading':r'i(a)','evidence':'Crop16: dotted upright i, round parentheses and closed a bowl.'},
 {'sign':'first and second triangular glyphs','location':'327 l7','reading':tri1+'; '+tri2,'evidence':'Crop21 independently preserves a detached lower outer stroke on the first and a base-meeting outer stroke on the second.'},
 {'sign':r'\alpha,\ /F','location':'327 l7','reading':r'\alpha,\ /F','evidence':'Crop21: rounded alpha, two colon points, one right arrowhead, baseline slash and ordinary F.'},
 {'sign':'third triangular glyph','location':'329 l.6','reading':tri3,'evidence':'Crop24: taller narrow contour and an extra left diagonal joining the base.'},
 {'sign':r'b\in A_{n-1}','location':'334 l.3','reading':r'b\in A_{n-1}','evidence':'Crop26: open-right membership sign with middle bar; n, dash and hooked 1 are all lowered.'},
 {'sign':'single closing quotation stroke','location':'305 interpret','reading':"``interpret'",'evidence':'Crop05: two opening strokes but one continuous curled closing stroke.'},
 {'sign':'single opening quotation stroke','location':'320 developing','reading':"'developing''",'evidence':'Crop18: one oblique high opening stroke, then a paired closing group.'},
 {'sign':'paired opening quotation strokes','location':'329 semisimplicial','reading':"``semisimplicial.",'evidence':'Crop27: the connected high opening group has two distinguishable legs. No closing pair is invented.'},
 {'sign':'five low dots','location':'315 before theory','reading':'situations.....theory','evidence':'Crop11: five distinct dark low marks after situations.'}
]
report={'scan':27,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed','viewed':[str(ROOT/'source/SP49_CW_109_scans'/f'H109-02_109_{n}.jpg') for n in ['scan027','scan027_a','scan027_b']],
 'layout':'One dense handwritten correction list, citing pages 302 through 334, on a sheet bounded internally by two long vertical rules. Page references generally stand left of the left rule; correction text sits right of it. The top entry has faint upper contours. A long rewritten sentence occupies the middle at 315, with an abandoned parenthesis and raised additions. The lower right l-5 entry and a slanted two-line marginal question are cut off by the right edge. Three inline triangular signs are drawn separately. No freestanding display or mathematical diagram occurs. The archive number 26 is lower left in a different hand. Pale circular/right-edge surface traces are not read as text or intentional diagrams.',
 'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inventory,
 'notes':['English correction list for cited pages 302–334; these are references to another text, not page numbering of the present note. No title, date, salutation, signature or stated page count appears.',
 'At 303 l.-3 the writer quotes image of A by A and says it is not clear what is meant; the second A has no distinct prime in this image.',
 'At 315 the sentence beginning l.7 is called difficult to understand. A proposed wording is introduced by Possibly and retains the qualifications about present knowledge and the ability to express basic situations. The first parenthetical attempt is cancelled and followed by a live replacement.',
 'At 327 the formula with alpha, two doubled-left triangular signs and /F is followed by the unfinished wording should it be and a high tick. No alternate formula is supplied on this page.',
 'At 328 the note asks should wouldn\'t = shouldn\'t after cancelling an earlier wouldn\'t.',
 'At 329 the parenthesis says doubled side is missing. The raised right-edge word is enveloping; the marginal question is clipped after certa and a final visible p in the phrase if it is 1 or 2 p.',
 'The complete inventory covers every list block and continuation, all nested cancellations and raised insertions, underlines, the three mathematical glyph drawings, both long rules, local connectors and preserved isolated marks. H is description-only and is not collated as a textual witness.'],
 'math_checks':[],
 'notation':notation,
 'abbreviations':[{'form':'l., l, l-','expansion':'line or line counted from the end, tentative interpretation only','place':'reference column throughout'},{'form':'p., p','expansion':'page, tentative interpretation only','place':'327–334 references'},{'form':'resp...','expansion':'respect, tentative and not expanded in the transcription','place':'315 proposed wording'},{'form':'cat.','expansion':'category, tentative and not expanded in the transcription','place':'315 proposed wording'}],
 'brief_feedback':'Whole and both halves were each displayed exactly once. The unresolved list was frozen before making 28 one-time enhanced crops, all displayed; crop25 was rotated -15 degrees to reduce the note\'s slant. No OCR, text-recognition library, outside research, other-page image, other-reader output or compilation was used. All 21 explicit C uncertainty macros have individual decisions, followed by context confirmations. Mathematical signs and index placement were followed on the ink, but these isolated correction fragments contain no locally complete claim for which a substantive mathematical proof check was actually performed; math_checks is therefore empty. The supplied C has no cotefile macro because it is a page excerpt; that structure is preserved. The old/new medial letters of Sentence and raised additions require overlapping/raised layout rather than consecutive baseline text.'}
(D/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(D/'literal_diff.txt').write_text(''.join(difflib.unified_diff(C.splitlines(True),s.splitlines(True),fromfile='C.tex',tofile='reading.tex')))
# Static checks only.
stack=[]; errors=[]
for i,ch in enumerate(s):
 if ch not in '{}': continue
 # Count immediately preceding slashes, so escaped literal braces would be ignored.
 q=i-1; k=0
 while q>=0 and s[q]=='\\': k+=1;q-=1
 if k%2: continue
 if ch=='{':stack.append(i)
 elif stack:stack.pop()
 else:errors.append('unmatched closing brace at '+str(i))
if stack:errors.append('unmatched opening braces: '+str(stack))
bs=re.findall(r'\\begin\{([^}]+)\}',s);es=re.findall(r'\\end\{([^}]+)\}',s)
if sorted(bs)!=sorted(es):errors.append('environment mismatch')
if s.count('$')%2:errors.append('odd dollar count')
if len(cd[:21])!=21:errors.append('C doubt coverage count')
for d in changes+cd:
 if not d.get('crop') and not(d.get('source') and d.get('bbox')): errors.append('missing evidence '+d.get('id',d.get('place','')))
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
for d in changes:
 if d['kind'] not in allowed:errors.append('invalid kind '+d['id'])
audit={'utc':datetime.now(timezone.utc).isoformat(),'whole_view_count':1,'half_a_view_count':1,'half_b_view_count':1,'frozen_unresolved_count':28,'created_crops':28,'displayed_crops':[f'{i:02d}' for i in range(1,29)],'ocr_used':False,'outside_research':False,'compilation_attempted':False,'static_errors':errors,'changes':len(changes),'explicit_c_doubts':21,'all_c_doubt_context_rows':len(cd),'resolved_explicit_c_doubts':sum(d['resolved'] for d in cd[:21]),'remaining_doubts':len(remaining),'inventory_rows':len(inventory),'math_check_events':0}
(D/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(audit,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
