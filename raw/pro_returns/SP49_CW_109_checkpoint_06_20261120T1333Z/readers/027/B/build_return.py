from pathlib import Path
import json,re,difflib
BASE=Path('work/readers/027/B')
ROOT=Path('/workspace/scratch/6d55c8c3e5a7')
C=Path('work/inputs/027/C.tex').read_text()
s=C
frozen=json.loads((BASE/'unresolved_frozen.json').read_text())
crops={q['id']:q for q in frozen['unresolved']}
a='source/SP49_CW_109_scans/H109-02_109_scan027_a.jpg'
b='source/SP49_CW_109_scans/H109-02_109_scan027_b.jpg'
w='source/SP49_CW_109_scans/H109-02_109_scan027.jpg'
changes=[]
def evidence(n=None,source=None,bbox=None):
    if n:
        q=crops[n]
        return dict(crop=str(ROOT/q['crop']),source=str(ROOT/q['source']),bbox=q['bbox'])
    return dict(crop=None,source=str(ROOT/source),bbox=bbox)
def change(id,place,old,new,kind,conf,why,n=None,source=None,bbox=None,replace=True,**extra):
    global s
    if replace:
        assert old in s,(id,old)
        s=s.replace(old,new,1)
    changes.append(dict(id=id,place=place,c=old,h=None,reading=new,diff_c=True,diff_h=False,kind=kind,marked_in_H=False,confidence=conf,evidence=why,**evidence(n,source,bbox),**extra))

# Rules are anchored alongside the transcription, with no separate geometry panel.
rule_top=r'''% Two manuscript column rules begin alongside the faded first entry.
\noindent\tikz[remember picture,overlay]{
  \coordinate (B27lefttop) at (2.65em,1.2ex);
  \coordinate (B27righttop) at (.955\linewidth,1.2ex);
}'''
rule_bottom=r'''% The same two rules continue to the foot, beyond the final correction entry.
\noindent\tikz[remember picture,overlay]{
  \coordinate (B27foot) at (0,-1.2ex);
  \draw[line width=.35pt] (B27lefttop) -- (B27lefttop |- B27foot);
  \draw[line width=.35pt] (B27righttop) -- (B27righttop |- B27foot);
}'''
s=s.replace(r'\scanpage{27}',r'\scanpage{27}'+'\n'+rule_top,1)
s=s.replace('% archive sheet number: 26',rule_bottom+'\n\n% archive sheet number: 26',1)
change('rule-left','Left rule between reference column and text','',r'\coordinate (B27lefttop) at (2.65em,1.2ex); \draw[line width=.35pt] (B27lefttop) -- (B27lefttop |- B27foot);','drawing or diagram','high','Both halves show a straight dark rule beside the line references. In the whole image it begins near (241,94) and continues to approximately (245,2335); no extension beyond these observed endpoints is claimed.',source=w,bbox=[235,85,251,2340],replace=False,code_reference='reading.tex: anchored B27lefttop / B27foot drawing')
change('rule-right','Right rule through the outer part of long entries','',r'\coordinate (B27righttop) at (.955\linewidth,1.2ex); \draw[line width=.35pt] (B27righttop) -- (B27righttop |- B27foot);','drawing or diagram','high','Both halves show the right-hand vertical rule, crossing the end of the p.315 rewrite and passing through the lower-right annotation. Observed endpoints are approximately (1516,96) and (1524,2335).',source=w,bbox=[1508,88,1532,2342],replace=False,code_reference='reading.tex: anchored B27righttop / B27foot drawing')

old=r'''\deleted{\unsure{l-2} ``play'' \unsure{no|not} ``s''}'''
new=r"""\deleted{\unsure{l-2} ``play'' \unsure{no|not} ``s}''"""
change('304-final-quotes','304, end of the cancelled correction',old,new,'deletion state (struck given live or live given struck)','medium','The two high closing strokes after s stand above the final zigzag return. The word s is crossed. The other quote groups have lower parts meeting the cancellation; only the terminal pair is moved outside the deletion.',n='04')
change('306-cancelled-l','306, before also',r'\deleted{\unsure{l|it}}',r'\deleted{l}','misread word','medium','The crop separates one looped ascender and its low return from the oblique cancelling stroke. No independent dotted i and following t can be distinguished; the surviving glyph reads l.',n='06')
change('312-reference','312, cancelled reference',r'\deleted{\unsure{l-6} \unsure{lets|let\'s}}'.replace("\\'","'"),r'\deleted{l-6 \unsure{lets|let\'s}}'.replace("\\'","'"),'misread symbol or index','high','The looped l, a short horizontal, and the rounded lower bowl with rising stem of 6 remain separately legible beneath the zigzag. The following word remains doubtful.',n='08')
change('313-opening-quotes','313, should not contraction',"313 l9 'shouldn't''","313 l9 ``shouldn't''",'other','high','The opener has two adjacent descending members, one curved and one narrow, with a pale separation. It is a paired opener.',n='09')
old=r'''\deleted{filtering \unsure{out|at|on|or}} \unsure{l-2|l-7} filtering'''
new=r'''\deleted{filtering}\raisebox{1.2ex}[0pt][0pt]{\makebox[0pt][l]{\unsure{\deleted{\unsure{out|at|on|or}}|\unsure{out|at|on|or}}}}\hspace{1.6em}\unsure{l-2|l-7} filtering'''
change('313-raised-cluster','313, line below the contraction corrections',old,new,'insertion or placement','medium','The short cluster is visibly raised above the end of the cancelled filtering. Its main letter bodies lie above the horizontal cancelling strokes, while a descending continuation meets them near the reference. The crop does not settle its deletion state, so both state and letters remain explicit doubts; no insertion caret is inferred.',n='10')

old=r'Sent\deleted{\unsure{ann|en}}ence'
new=r'''Sent\tikz[baseline=(B27sentold.base)]{\node[inner sep=0pt] (B27sentold) {\deleted{\unsure{ann|en}}};\node[anchor=base west,inner sep=0pt] at (B27sentold.base west) {en};}ce'''
change('315-sentence-overwrite','315, first word',old,new,'insertion or placement','medium','The heavy medial letter group occupies one physical place between Sent and ce. C prints the old and new portions consecutively. The new en is placed over the doubtful old ann/en, while Sent and ce are each represented once. The buried old letters remain doubtful.',n='11')
change('315-to','315, before in order to',r'\deleted{\unsure{to}}',r'\deleted{to}','misread word','medium','A tall left stem with crossing stroke and an attached closed bowl to its right survive under the cancellation; they support to.',n='12')
change('315-certainly-height','315, first cancelled parenthesis',r'\inserted{certainly} true',r'\raisebox{1.15ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{certainly}}}true','insertion or placement','high','Certainly is written above true, not on the running baseline. The abandoned parenthesis remains cancelled as in C.',n='14')
change('315-presumably-and-raised-replacement','315, right part of first cancelled parenthesis line',r'\unsure{presumably} \inserted{as far as our}',r'\raisebox{1.15ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{as far as our}}}presumably','insertion or placement','medium','The underlying word has p descender, successive short humps, tall medial strokes and terminal y; it reads presumably. As far as our is raised over that word and extends to its right. The overlaid phrase is not a baseline continuation after the word.',n='14')
change('315-no-tail','315, after the cancelled goes).',r'\unsure{No|Now}---.',r'\unsure{No|Now}...','other','medium','Three separate low punctuation groups remain after No/Now. The first two are short and elongated; the long higher stroke is part of the cancellation, not an independent em dash. The final letter of No/Now is still obscured.',n='15')
old=r'\inserted{would} allow'
new=r'''\raisebox{1.2ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{would}}}\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.4pt] (0,-.85)--(.25,-.25)--(.48,-.72);}allow'''
change('315-would-height-caret','315, l.-3, between which and allow',old,new,'insertion or placement','high','Would sits above the line; a small two-stroke caret lies below the gap immediately before allow. The insertion macro alone in C does not preserve that height or the drawn caret.',source=b,bbox=[989,94,1120,189])
change('316-it','316, before is a',r'\deleted{\unsure{it}}',r'\deleted{it}','misread word','high','The first short upright has a separate dot and the second upright has the horizontal of t. Both letters remain visible under the oblique cancellation.',n='18')
change('317-opening-quotes','317, its',"317. l.11 'its''","317. l.11 ``its''",'other','high','The opener consists of a long curved stroke and a separate short raised mark to its right. Both are distinct from the lower i-dot.',n='19')
change('326-old-sign','326, before the live ampersand',r'\deleted{\unsure{\&}}',r'\deleted{\unsure{\&|l}}','misread symbol or index','low','The crossed old form retains an upper loop and a lower return. An ampersand remains plausible, but a looped l with a cancelling stroke also fits the surviving contour; the crop does not decide them.',n='20')
old=r'\deleted{\unsure{\&|l}}'
point=r'\tikz[baseline=0pt,overlay,x=1em,y=1ex]{\fill (-.4,-.52) circle (.035em);}'
s=s.replace(old,old+point,1)
change('326-low-point','326, below the cancelled old sign','',point,'omission','medium','A separate compact dark point lies below the old sign and left of the live ampersand. Its geometry is retained without assigning a punctuation function or an origin.',n='20',replace=False)
old=r"""\tikz[remember picture,overlay]\coordinate(scxxviim); \inserted{\& l-3} ``commutes \uline{with}''"""
new=r'''\tikz[baseline=(B27comm.base),x=1em,y=1ex]{
  \node[anchor=base west,inner sep=0pt] (B27comm) at (0,0) {``commutes \uline{with}''};
  \node[anchor=base west,inner sep=0pt] at (-.55,2.1) {\inserted{\& l-3}};
  \fill (2.55,3.0) circle (.035em);
  \draw[line width=.4pt] (-.28,.9)--(-.55,-1.9);
  \draw[line width=.4pt] (-.47,-1.1)--(-.35,-1.45)--(-.25,-1.1);
}'''
old_connector=r'''\tikz[remember picture,overlay]{\coordinate(scxxviin); \draw (scxxviim) -- ([yshift=.65ex]scxxviin) -- ([xshift=.09em,yshift=.93ex]scxxviin);}'''
change('326-raised-reference-and-connector','326, after l.-8 and above/beside commutes',old,new,'insertion or placement','high','The added & l-3 stands above the line. A small isolated high point follows 3. The long slanted stroke begins just left of the opening quote of commutes, descends below that line, and has a small separate hooked return near its foot; it does not join the p.327 triangle. C attached it to the following formula. The revised drawing is local to the p.326 entry.',n='21',c_additional_literal=old_connector,reading_additional_literal='')
assert old_connector in s
s=s.replace(old_connector,'',1)
change('328-apostrophe','p328, cancelled contraction',r"\deleted{wouldn't}",r"\deleted{would'nt}",'misread word','high','The isolated apostrophe stands after the tall d and before the lower n. The n precedes the final t. The entire old contraction is cancelled.',n='24')
change('329-word','p329, raised l-5 word','l-5 ``developing', 'l-5 ``enveloping','misread word','high','The initial letter is a short looped e, followed by n-v-e; there is no d ascender before it. The remaining l-o-p-i-n-g is readable, with the terminal g against the clipped edge.',n='26')
change('329-clipped-closer','p329, after enveloping',r"\unsure{''}",r"\unsure{''|'}",'other','low','Only a short raised bent stroke survives at the right boundary after the word. A paired closer remains possible with its second stroke clipped, but a single closer is also allowed by the remaining ink.',n='26',replace=False)
s=s.replace(r"enveloping\unsure{''}",r"enveloping\unsure{''|'}",1)
old=r'''\inserted{l-5 ``enveloping\unsure{''|'}}'''
new=r'''\raisebox{1.7ex}[0pt][0pt]{\inserted{l-5 ``enveloping\unsure{''|'}}}'''
change('329-raised-entry','p329, inserted l-5 correction',r'''\inserted{l-5 ``developing\unsure{''}}''',new,'insertion or placement','high','The l-5 entry sits distinctly above the semisimplicial baseline and to the right of its two-stroke connector. Its raised position is retained. The word and clipped closer have their own reading decisions.',n='26',replace=False)
assert old in s
s=s.replace(old,new,1)
# Keep the question and the two clipped text lines on the physical right side.
old=r'''\margin{? (I'm not \unsure{certa|certain} if it is 1 or 2 \unsure{p|r}}'''
new=r'''\margin{\begin{tikzpicture}[x=1em,y=1ex]
  \node[anchor=west,inner sep=0pt] at (1.1,2.2) {?};
  \node[anchor=west,inner sep=0pt] at (0,0) {I'm not \unsure{certa|certain}};
  \node[anchor=west,inner sep=0pt] at (0,-2.0) {if it is 1 or 2 \unsure{p|r}};
  \draw[line width=.35pt] (-.25,-.4) .. controls (-.95,-1.7) and (-.25,-3.2) .. (1.25,-3.2);
  \fill (4.3,-3.8) circle (.035em);
\end{tikzpicture}}'''
change('329-note-layout','p329, right-hand marginal question',old,new,'insertion or placement','high','The question mark is above the two slanted text lines. The large left curve begins near the lower part of the first line and bends beneath the second; it is retained as drawn geometry, not an ordinary opening parenthesis before the whole note. The small separate dark point below/right is also retained. The visible certa and final p/r remain clipped and doubtful; no closing delimiter is supplied.',n='26')
pts=r'\tikz[baseline=0pt,overlay,x=1em,y=1ex]{\fill (1.0,5.3) circle (.035em);\fill (.84,4.9) circle (.035em);}'
raised_entry=r'''\raisebox{1.7ex}[0pt][0pt]{\inserted{l-5 ``enveloping\unsure{''|'}}}'''
s=s.replace(raised_entry,pts+raised_entry,1)
change('329-upper-points','p329, two points above-left of the raised l-5 entry','',pts,'omission','medium','Two small separated dark points stand above the l-5 annotation, one higher and slightly to the right. They are reproduced without assigning a punctuation function. Their existence is clear; their origin is not asserted.',n='26',replace=False)

(BASE/'reading.tex').write_text(s)

c_doubts=[]
def doubt(place,c,reading,resolved,conf,why,n=None,source=None,bbox=None,**extra):
    c_doubts.append(dict(place=place,c=c,reading=reading,resolved=resolved,confidence=conf,evidence=why,**evidence(n,source,bbox),**extra))
# Every one of the 21 explicit C uncertainty macros is represented independently.
doubt('Opening reference',r'\unsure{302}',r'\unsure{302}',False,'medium','Only faded upper traces and lower contours of the three digits survive. The lower shapes favour 302, but they do not settle all strokes. No sequence-based reconstruction is used.',n='01',decision_type='explicit C doubt')
doubt('Opening line reference',r'\unsure{15}',r'\unsure{15}',False,'medium','The 1 stem and lower round part of the next digit are visible. The faint top does not securely decide the second digit, so 15 remains doubtful.',n='01',decision_type='explicit C doubt')
doubt('303, cancelled word before which',r'\unsure{with|who}',r'\unsure{with|who}',False,'low','The crossing obscures the short medial strokes and ending. Two tall remnants do not separate with from who with confidence.',n='02',decision_type='explicit C doubt')
doubt('304, cancelled reference',r'\unsure{l-2}',r'\unsure{l-2}',False,'low','The l survives, but the horizontal and possible digit are entangled with the repeated zigzag; l-2 is retained as a tentative reading.',n='04',decision_type='explicit C doubt')
doubt('304, cancelled no/not',r'\unsure{no|not}',r'\unsure{no|not}',False,'low','A rounded o and preceding short stroke survive; a possible final t could lie beneath the descending cancellation.',n='04',decision_type='explicit C doubt')
doubt('306, cancelled glyph before also',r'\unsure{l|it}','l',True,'medium','One looped ascender is distinguishable from its cancelling stroke; the crop supports l.',n='06',decision_type='explicit C doubt')
doubt('312, cancelled line reference',r'\unsure{l-6}','l-6',True,'high','Separate l, short horizontal and a 6 with a closed lower bowl remain visible.',n='08',decision_type='explicit C doubt')
doubt('312, cancelled lets',r"\unsure{lets|let's}",r"\unsure{lets|let's}",False,'low','The l, t cross and curled terminal s are legible. The apostrophe zone is crossed; its presence or absence is not decided.',n='08',decision_type='explicit C doubt')
doubt('313, raised short cluster',r'\unsure{out|at|on|or}',r'\unsure{\deleted{\unsure{out|at|on|or}}|\unsure{out|at|on|or}}',False,'low','The small raised strokes do not securely separate the proposed short words. Their connection toward the cancelled reference leaves deletion state uncertain as well; both uncertainties are local to this occurrence.',n='10',decision_type='explicit C doubt')
doubt('313, reference before live filtering',r'\unsure{l-2|l-7}',r'\unsure{l-2|l-7}',False,'low','The tall reference stroke and low digit overlap the cancelling return. The lower turn favours 2, but a crossed 7 and the status of the intervening stroke remain unresolved.',n='10',decision_type='explicit C doubt')
doubt('315, overwritten medial letters of Sentence',r'\unsure{ann|en}',r'\unsure{ann|en}',False,'low','The dense overwritten group is bounded by clear Sent and ce. Its old internal letters remain obscured. The live en is overlaid at the same location, with unchanged surrounding letters printed once.',n='11',decision_type='explicit C doubt')
doubt('315, false start before in order to',r'\unsure{to}','to',True,'medium','A tall t and an attached o-shaped loop are still legible beneath the stroke.',n='12',decision_type='explicit C doubt')
doubt('315, cancelled presumably',r'\unsure{presumably}','presumably',True,'medium','The p descender, sequence of short letters, tall medial strokes and final y support presumably despite the crossing.',n='14',decision_type='explicit C doubt')
doubt('315, cancelled No/Now',r'\unsure{No|Now}',r'\unsure{No|Now}',False,'low','The N and rounded following part survive. The long cancellation coincides with the terminal part and does not exclude an additional w.',n='15',decision_type='explicit C doubt')
doubt('316, cancelled it',r'\unsure{it}','it',True,'high','A separate i-dot, short i stem, and crossed t are distinct in the crop.',n='18',decision_type='explicit C doubt')
doubt('316, cancelled ending after is a',r'\unsure{to|is}',r'\unsure{to|is}',False,'low','The tall crossed loop and lower curl do not separate to from is under the dense crossing. Deletion extent is clear; the cancelled letters are not.',n='18',decision_type='explicit C doubt')
doubt('326, cancelled sign',r'\unsure{\&}',r'\unsure{\&|l}',False,'low','The old upper loop and lower return allow both an ampersand and a looped l. The new lower-right ampersand is separately clear.',n='20',decision_type='explicit C doubt')
doubt('327, cancelled quote-like group after isn\'t',r"\unsure{''}",r"\unsure{''}",False,'medium','The small high pair-like remnant has extra crossing strokes. Its height and two limbs support closing quotation marks, but the obliterated interior prevents certainty.',n='23',decision_type='explicit C doubt')
doubt('329, clipped closing marks after enveloping',r"\unsure{''}",r"\unsure{''|'}",False,'low','A surviving bent high stroke reaches the right boundary; the second member of a pair could be outside the image, while a single closer also remains possible.',n='26',decision_type='explicit C doubt')
doubt('329, clipped certa/certain in marginal question',r'\unsure{certa|certain}',r'\unsure{certa|certain}',False,'low','Certa is visible at the cut edge; a further n cannot be established or excluded beyond the boundary. The word is not completed silently.',n='26',decision_type='explicit C doubt')
doubt('329, clipped last p/r of marginal question',r'\unsure{p|r}',r'\unsure{p|r}',False,'low','Only the beginning of the last letter survives against the dark clipped edge. Its remaining stem/shoulder does not decide p versus r.',n='26',decision_type='explicit C doubt')

# Page-specific context alternatives and notation statements are not authorities against the ink.
doubt('303, final capital in image of A by A',r'image of $A$ by $A$',r'image of $A$ by $A$',True,'high','The final capital has two sides and a retraced crossbar; the two high strokes are the closing quotation pair. No independent prime is visible.',n='03',decision_type='C_context alternative',rejected_alternative=r"image of $A$ by $A'$")
doubt('315, respect. concerning','respect. concerning','respect. concerning',True,'high','The half shows a separate low stop after respect. The next physical line begins with a lowercase c. The stop is preserved.',source=a,bbox=[1457,906,1641,970],decision_type='C_context alternative',rejected_alternative='respect concerning')
doubt('316, i(a)',r'i(a)',r'i(a)',True,'high','The short initial stem has a separate dot; the round parentheses enclose a closed-loop a. The surrounding cancelled words are decided separately.',source=b,bbox=[756,239,850,300],decision_type='C_context notation')
# Preserve the exact glyph code rather than naming a standard Delta in its place.
glyphs=re.findall(r'\\mathord\{\\tikz\[baseline=0pt,x=1ex,y=1ex\]\{\\draw\[.*?;\}\}',C)
assert len(glyphs)==3,len(glyphs)
doubt('327, first doubled-left triangle',glyphs[0],glyphs[0],True,'high','The lower half shows the extra left oblique starting separately from the base and ending below the top. The triangular contour is distinct from the second glyph and is retained individually.',source=b,bbox=[483,626,531,667],decision_type='C_context notation')
doubt('327, second doubled-left triangle',glyphs[1],glyphs[1],True,'high','The lower half shows a second left oblique meeting the foot, with a lower and wider outline than the first glyph. C\'s separate traced shape is confirmed.',source=b,bbox=[652,629,699,669],decision_type='C_context notation')
doubt('329, taller doubled-left triangle',glyphs[2],glyphs[2],True,'high','The lower half independently shows the taller triangular outline and extra left stroke meeting the foot. The adjacent comment does not override the visible double-sided form.',source=b,bbox=[406,938,456,997],decision_type='C_context notation')
doubt('327, alpha, arrow, slash and F',r'\alpha:\longrightarrow /F',r'\alpha:\longrightarrow /F',True,'high','A rounded alpha is followed by two colon points; the horizontal arrow has a right arrowhead; the slash is diagonal before a single-contour F on the baseline. No F subscript is supplied.',source=b,bbox=[405,624,748,683],decision_type='C_context notation')
doubt('334, membership and individual lowered signs',r'b\in A_{n-1}',r'b\in A_{n-1}',True,'high','The lower half shows ordinary b and A, a right-opening membership sign, and a lowered n, short horizontal and 1. Each of the three lower components was read independently. The quotation crop incidentally corroborates them.',n='27',decision_type='C_context notation')

remaining=[]
for q in c_doubts:
    if not q['resolved']:
        remaining.append(dict(place=q['place'],reading=q['reading'],alternatives=q['reading'],confidence=q['confidence'],reason=q['evidence']))

inventory=[]
def inv(kind,position,words,hand='his hand'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=f'{len(inventory)+1:02}',kind=kind,position=position,first_words_or_objects=words,transcribed='yes'))
inv('text','Top, faded first entry','302 l.15 ``its')
inv('text','303, two physical lines','303 l.1; l2; l.-3; - not clear what you mean.')
inv('deletion','303, before which','with|who')
inv('text','304, main entry','304 l-15 ``commutes with\'\' also l-13.')
inv('deletion','304, end of entry','l-2 ``play\'\' no|not ``s; final quote pair retained outside crossing')
inv('text','305 entry','305 l.5 ``interpret\' l14 ``commutes with\'\'')
inv('text','306 entry','306 l.19 ``its\'\'; also l-5; l-4 ``test category\'\'')
inv('deletion','306, before also','l')
inv('text','306, within test category','single underline under category')
inv('text','309 entry','309 l.-8 ``on the previous\'\'')
inv('text','309, within quotation','single underline under the')
inv('text','312 entry','312 l-.8 ``isn\'t\'\'')
inv('deletion','312, end of entry','l-6 lets|let\'s')
inv('text','313, first physical line','313 l9 ``shouldn\'t\'\'; l.18 ``don\'t\'\'; l-12 ``commutes with\'\'')
inv('text','313, continuation line','l-2|l-7 filtering\'\'')
inv('deletion','313, beginning of continuation','filtering')
inv('text','313, raised short cluster over cancelled ending','out|at|on|or; deletion state uncertain')
inv('text','314 entry','314 l.5 ``isn\'t\'\' l.6 ``as is\'\'')
inv('text','315, heading of long entry','Sentence starting l.7 - difficult to understand. Possibly:')
inv('deletion','315, overwritten medial group in Sentence','ann|en, overlaid by live en; Sent and ce shared')
inv('text','315, proposed rewrite, beginning through singled out.','I add this comment, of course, in order to push home the point ...')
inv('deletion','315, after of course,','to')
inv('text','315, rewrite first line','single underline under push home')
inv('text','315, rewrite second line','single underline under no more')
inv('text','315, rewrite third line','single underline under to express')
inv('text','315, rewrite fourth line','single underline under does')
inv('text','315, rewrite fourth line','single underline under stand')
inv('deletion','315, abandoned parenthesis across two lines and following No/Now','(This is ... at the present knowledge goes). No|Now...')
inv('insertion','315, above true in abandoned parenthesis','certainly')
inv('deletion','315, denser local crossing under raised as far as our','presumably')
inv('insertion','315, above presumably and extending right','as far as our')
inv('text','315, live replacement parenthesis','(This certainly seems to be so as far as our present knowledge goes)\'\'...')
inv('text','315, following correction line','l.17 ``its\'\' l.-3 \'and which would allow one to compute\'\'')
inv('insertion','315 l.-3, above gap before allow','would')
inv('drawing','315 l.-3, below gap before allow','two-stroke insertion caret')
inv('text','316 entry','316. l.1 ``shouldn\'t\'\' l12 ``i(a) ... is a\'\'')
inv('deletion','316, before is','it')
inv('deletion','316, after closing quotes','to|is')
inv('text','317 entry','317. l.11 ``its\'\' l-16 ``isn\'t\'\'')
inv('text','320 entry','320 l 8. ``indispensable\'\'; l-15 \'developing\'\'; l-8 ``its\'\'')
inv('text','321 entry','321 l.9 \'isn\'t\'\'')
inv('text','323 entry','323 l13 ``don\'t\'\'')
inv('text','326 baseline entry','326 l-12; & l.-8; ``commutes with\'\' and')
inv('deletion','326, between l-12 and live &','&|l')
inv('drawing','326, below crossed old sign','isolated dark point')
inv('insertion','326, above commutes','& l-3')
inv('drawing','326, high after inserted 3','isolated raised point')
inv('drawing','326, left of commutes','long slanted downward stroke with small hooked return near foot')
inv('text','326, within commutes with','single underline under with')
inv('text','p.327 first line','p.327. l7, alpha with two triangular glyphs and slash F; should it be and a high tick')
inv('drawing','p.327 formula, first object','first separately traced double-left triangular glyph')
inv('drawing','p.327 formula, second object','second separately traced double-left triangular glyph')
inv('text','p.327 continuation line','l-17 ``allows one to\'\' l-16 ``doesn\'t\'\' l-14 ``isn\'t ... there!\'\'')
inv('text','p.327 l-17','single underline under one')
inv('deletion','p.327 l-14, after isn\'t','doubtful closing quote group')
inv('text','p.327 following line','l-5 ``don\'t\'\'')
inv('text','p328 entry','p328 l-12, should ``wouldn\'t\'\' = ``shouldn\'t\'\'')
inv('deletion','p328, before should','would\'nt')
inv('text','p328 continuation','l-10 doesn\'t')
inv('text','p329 first line','p329 l.6; (doubled side is missing); ``its\'\'')
inv('drawing','p329 l.6','taller separately traced double-left triangular glyph')
inv('text','p329 main continuation','l12 ``don\'t\'\' l-13 ``makes sense\'\' l.-13 ``semisimplicial.')
inv('drawing','After semisimplicial.','long slanted stroke with short right branch')
inv('insertion','p329, raised at right of semisimplicial.','l-5 ``enveloping with clipped closing mark(s)')
inv('drawing','Above p329 raised l-5 entry','two isolated dark points')
inv('margin note','Physical right margin at p329/p333 height, slanted and clipped','?; I\'m not certa|certain; if it is 1 or 2 p|r')
inv('drawing','Left and below the two text lines of marginal note','long curved parenthesis-like stroke')
inv('drawing','Below/right of the marginal note','isolated dark point')
inv('text','p.333 entry','p.333 l.-12 ``makes sense\'\'')
inv('text','p.334 final entry','p.334 l.3 \'b in A with n-1\'\'; l-6 ``its\'\' also in l-5.')
inv('drawing','Between page-reference column and text, top to foot','left vertical rule')
inv('drawing','Near right margin, top to foot','right vertical rule')

notation=[
{'sign':'Three individually traced doubled-left triangles','location':'327 l7 (two); 329 l6 (one)','reading':' ; '.join(glyphs),'evidence':'Read independently in half b. First extra left stroke begins clear of base; second and third meet the foot. Third outline is taller. The adjacent missing-side comment does not alter the ink.'},
{'sign':r'\alpha,\ :\ ,\longrightarrow,\ /F','location':'327 l7','reading':r'\alpha:\longrightarrow /F','evidence':'Rounded alpha; two colon points; one shaft with a right arrowhead; diagonal slash and a single-contour F, with no supplied subscript.'},
{'sign':'A','location':'303 l.-3, both occurrences','reading':'A by A','evidence':'Ordinary triangular A forms. Crop03 separates the final A crossbar/retrace from the high closing quotation pair and shows no independent prime.'},
{'sign':r'i(a)','location':'316 l12','reading':r'i(a)','evidence':'Dotted short upright i, round parentheses, and closed-loop a; half b and crop18.'},
{'sign':r'b\in A_{n-1}','location':'334 l3','reading':r'b\in A_{n-1}','evidence':'Plain b and A; open-right membership sign; individual lowered n, short minus and 1; half b, corroborated incidentally by quote crop27.'},
{'sign':'single underlines','location':'306 category; 309 the; 315 push home/no more/to express/does/stand; 326 with; 327 one','reading':r'\uline{category}; \uline{the}; \uline{push home}; \uline{no more}; \uline{to express}; \uline{does}; \uline{stand}; \uline{with}; \uline{one}','evidence':'Separate baseline rules confined to the named spans. Crop07 confirms category has one partly broken rule, not two.'},
{'sign':'quotation counts','location':'305 interpret; 313 should not contraction; 315 its and compute; 317 its; 334 membership expression','reading':"``interpret'; ``shouldn't''; ``its''; compute''; ``its''; '$b\\in A_{n-1}$''",'evidence':'Separate local crop decisions: 05 single closer; 09 paired opener;16/17 connected paired closers;19 long opener plus a short second mark;27 single opener and paired closer.'},
{'sign':'apostrophe position in cancellation','location':'328 l-12, old word','reading':r"\deleted{would'nt}",'evidence':'Crop24 locates the detached apostrophe between d and n.'},
{'sign':'five continuation points','location':'315, situations to theory','reading':'situations.....theory','evidence':'Crop13 shows five low dark groups; the faint nearby speck is not counted as a sixth point.'},
{'sign':'terminal high tick','location':'327, after should it be','reading':"should it be '",'evidence':'Crop22 shows a single small high tapered mark, no question-mark stem and dot.'},
{'sign':'raised insertion positions and connectors','location':'315 certainly/as far as our/would; 326 & l-3; 329 l-5 and right note','reading':'Explicit raised text and local TikZ paths in reading.tex','evidence':'Crops14/21/26 and half b establish relative height. The p.326 stroke is local to commutes rather than joined to the following formula.'}
]

notes=[
'Handwritten correction list citing typescript pages 302 through 334, with a faded first reference and archive corner number 26. No title, date, manuscript pagination, or stated page count is visible.',
'At 303 l.-3 the quoted image of A by A is followed by - not clear what you mean. The second A is not given a prime by this reading.',
'At 315 the sentence starting l.7 is called difficult to understand. A wording is proposed under Possibly. It includes the qualification concerning present knowledge; an earlier parenthesis and the following No/Now are cancelled before a live replacement parenthesis.',
'At 327 l7 a formula with alpha, two individually drawn doubled-left triangular signs, an arrow and slash F is followed by should it be and a single high tick. No answer or question mark is supplied.',
'At 328 l-12 the cancelled form reads would\'nt; the live comparison is should ``wouldn\'t\'\' = ``shouldn\'t\'\'.',
'At 329 l6 the explicit comment says doubled side is missing. The later raised l-5 correction reads enveloping. A right-hand clipped note asks whether it is 1 or 2 p/r; the ending of certa/certain and the last letter remain doubtful.',
'At 334 l3 the quoted expression reads b in A with subscript n-1. The following l-6 its correction also applies in l-5.'
]

report=dict(scan=27,reader='B',model='GPT-6 Astra Pro (inherited)',effort='not exposed',viewed=[str(ROOT/x) for x in [w,a,b]],layout='One handwritten correction-list sheet, a single main hand, with a narrow left reference column and two long dark vertical rules. A faded first entry precedes p.303; short corrections continue to p.334. The p.315 entry expands into a multiline proposed rewrite, an abandoned two-line parenthesis, two raised additions, a live replacement parenthesis, and a further raised would with a low caret. The p.326 addition is above its line with a long local descending mark. Three separately drawn triangular mathematical glyphs occur in the lower half. A raised p.329 l-5 entry and a slanted question at the physical right are cut by the right edge. Circular edge defects near the upper and lower right and the archive number 26 are physical/archive features rather than manuscript text. There are no standalone displayed equations or commutative diagrams. Inventory covers every list block, all nested deletions/insertions, underline spans and retained drawn marks.',changes=changes,c_doubts=c_doubts,remaining_doubts=remaining,inventory=inventory,notes=notes,math_checks=[],notation=notation,abbreviations=[{'form':'l., l, l-','expansion':'line (tentative interpretation of references)','place':'Throughout correction references'},{'form':'p., p','expansion':'page (tentative interpretation of references)','place':'327, 328, 329, 333, 334'},{'form':'resp...','expansion':'respect (tentative; abbreviation and following continuation points retained)','place':'315 proposed rewrite'},{'form':'cat.','expansion':'category (tentative)','place':'315 proposed rewrite'}],brief_feedback='Read only the assigned page and supplied inputs. Whole view exactly once, each half exactly once, then 27 frozen local loci cropped once with crop.py; all 27 enhanced outputs displayed. Crop26 was rotated -12 degrees for the slanted note. No OCR, outside research, other-reader output, other-page images, or compilation was used. All 21 explicit C doubts and the page-specific notation/context alternatives are recorded. H is description-only, so there are no H collation rows. Mathematical fragments were parsed for letters, indices and operators; no substantive theorem/proof/computation was actually checked, so math_checks is intentionally empty. Deletion extent is distinguished from buried lettering. The raised cluster near filtering retains an additional state uncertainty. The two physical rules are anchored alongside the text; no isolated drawing panel is used.')
(BASE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(BASE/'literal_diff.txt').write_text(''.join(difflib.unified_diff(C.splitlines(True),s.splitlines(True),fromfile='C.tex',tofile='B/reading.tex')))
print(json.dumps({'changes':len(changes),'explicit_c_doubts':sum(x.get('decision_type')=='explicit C doubt' for x in c_doubts),'all_c_decisions':len(c_doubts),'resolved_explicit_c_doubts':sum(x.get('decision_type')=='explicit C doubt' and x['resolved'] for x in c_doubts),'remaining_doubts':len(remaining),'inventory_rows':len(inventory),'crops':len(crops)},indent=2))
