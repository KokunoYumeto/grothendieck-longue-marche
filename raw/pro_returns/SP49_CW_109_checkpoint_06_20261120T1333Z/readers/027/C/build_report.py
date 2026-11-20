from pathlib import Path
import json,re,difflib
root=Path('work/readers/027/C')
C=Path('work/inputs/027/C.tex').read_text()
R=(root/'reading.tex').read_text()
frozen=json.loads((root/'unresolved_frozen.json').read_text())
base=Path('/workspace/scratch/6d55c8c3e5a7')
A=str(base/'source/SP49_CW_109_scans/H109-02_109_scan027_a.jpg')
B=str(base/'source/SP49_CW_109_scans/H109-02_109_scan027_b.jpg')
W=str(base/'source/SP49_CW_109_scans/H109-02_109_scan027.jpg')

def segment(s,start,end,include=False):
    a=s.index(start); b=s.index(end,a)
    return s[a:b+len(end) if include else b]

def ev(n=None,source=None,bbox=None):
    if n:
        z=frozen['loci'][n-1]
        return {'crop':'crops/'+Path(z['crop']).name,'source':str(base/z['source']),'bbox':z['bbox']}
    return {'crop':None,'source':source,'bbox':bbox}

changes=[]
def change(i,place,c,reading,kind,evidence,n=None,confidence='high',source=None,bbox=None):
    assert not c or c in C,(i,'C fragment not literal',c)
    assert not reading or reading in R,(i,'reading fragment not literal',reading)
    changes.append({'id':i,'place':place,'c':c,'h':None,'reading':reading,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence,**ev(n,source,bbox)})

change('01-top-line15','Top entry, line reference',r'l.\unsure{15}',r'l.15','misread symbol or index','The faint upper horizontal and lower open curl form 5 after the straight 1; the numeral is readable although the page reference remains faded.',1,'medium')
change('02-304-final-quotes','304, final quotation after cancelled s',"\\deleted{\\unsure{l-2} ``play'' \\unsure{no|not} ``s''}","\\deleted{\\unsure{l-2} ``play'' \\unsure{no|not} ``s}''",'deletion state (struck given live or live given struck)','The last two high strokes stand above the terminal rising cancellation, clear of its path. The inner word and preceding quotation pair are crossed. The final pair is therefore outside the deletion.',4,'medium')
change('03-306-old-l','306, cancelled start before also',r'\deleted{\unsure{l|it}}',r'\deleted{l}','misread word','One looped ascender, descending main stroke and returned foot remain visible. No independent i-dot or second t is distinguishable.',5,'medium')
change('04-312-old-reference','312, cancelled reference after isn\'t',r'\unsure{l-6}',r'l-6','misread symbol or index','A looped l, separate short dash and closed low bowl with an upper return identify l-6 beneath the zigzag.',6,'high')
change('05-313-raised-fragment','313 continuation, cancelled word after filtering',r'\deleted{filtering \unsure{out|at|on|or}}',r'\deleted{filtering \raisebox{.7ex}[0pt][0pt]{\unsure{out|at|on|or}}}','insertion or placement','The small cancelled cluster is written above the baseline at the right end of filtering. Its letters remain unresolved; no caret is visible, so it is raised text within the deletion rather than a newly inferred insertion.',7,'high')
old=r'Sent\deleted{\unsure{ann|en}}ence'
new=segment(R,'Sent\\tikz',' starting l.7')
change('06-315-sentence-overwrite','315, Sentence',old,new,'insertion or placement','The heavy medial cluster occupies the same physical space as the final en; it is not a separate cancelled ann/en followed by another full ence. Shared Sent and ce are represented once and the old and new middle overlap. The buried letters remain doubtful.',8,'medium')
change('07-315-to','315, false start before in order',r'\deleted{\unsure{to}}',r'\deleted{to}','misread word','The cancelled cluster has a long t stem and cross-stroke with a closed o at its right.',9,'medium')
change('08-315-certainly-raised','315, first cancelled parenthesis, certainly',r'\inserted{certainly}',r'\raisebox{1.1ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{certainly}}}','insertion or placement','Certainly is written on the interline directly above true. It remains within the cancelled parenthetical attempt.',10,'high')
change('09-315-asfar-raised','315, first cancelled parenthesis, as far as our',r'\unsure{presumably} \inserted{as far as our}',r'\raisebox{1.1ex}[0pt][0pt]{\makebox[0pt][l]{\inserted{as far as our}}}\unsure{presumably}','insertion or placement','As far as our is above the cancelled presumably area, with its left edge over that word; it is not a baseline continuation after it.',10,'high')
change('10-315-cancelled-terminal-strokes','315, after cancelled No/Now',r'\unsure{No|Now}---.',r'\unsure{No|Now} \textendash{}\,\textendash{}.','other','Two short low horizontal strokes and a final low point remain beneath the long rightward cancellation. The long upper line belongs to the cancellation, and is not counted as a third textual dash.',11,'medium')
new=segment(R,'\\tikz[baseline=(sc27Cwouldbase.base)]',' allow one to compute')
change('11-315-would-raised','315, line -3, would',r'\inserted{would}',new,'insertion or placement','Would is above the line between which and allow; a small two-sided caret is below that gap. Both height and caret are retained.',source=B,bbox=[983,95,1115,190])
change('12-316-it','316, cancelled it between i(a) and is',r'\deleted{\unsure{it}}',r'\deleted{it}','misread word','The short dotted i and crossed t are separately visible under the oblique crossing.',12,'high')
change('13-317-opening-quote','317, l-16 opening quotation',"l-16 ``isn't''","l-16 \\unsure{``|'}isn't''",'misread symbol or index','The high opener has one continuous hooked body and a short right leg. It can be a joined pair or a single hooked stroke; the lower point aligns with the i and does not settle the quotation count.',14,'low')
change('14-326-old-ampersand','326, first cancelled ampersand',r'\deleted{\unsure{\&}}',r'\deleted{\&}','misread symbol or index','The upper and lower loops and terminal return of the crossed ampersand remain distinct beside the lower live ampersand.',15,'medium')
old=segment(C,'\\tikz[remember picture,overlay]\\coordinate(scxxviim);'," ``commutes")
new=segment(R,'\\tikz[remember picture,overlay]{\\coordinate(scxxviim);'," ``commutes")
change('15-326-raised-reference','326, added & l-3 above commutes',old,new,'insertion or placement','The added reference is on the interline above the beginning of commutes, after the l.-8 reference. A separate small high point after the 3 is also visible and is drawn without assigning it a punctuation function.',15,'high')
old=r'\draw (scxxviim) -- ([yshift=.65ex]scxxviin) -- ([xshift=.09em,yshift=.93ex]scxxviin);'
new=r'\draw ([xshift=.2em]scxxviim) -- ([xshift=.4em,yshift=1.3ex]scxxviin); \draw ([xshift=.57em,yshift=1.7ex]scxxviin) -- ([xshift=.67em,yshift=1.4ex]scxxviin) -- ([xshift=.77em,yshift=1.6ex]scxxviin);'
change('16-326-connector','Between the 326 reference and the 327 formula',old,new,'drawing or diagram','The long slightly oblique stroke ends above/right of the first triangle. Its short bent tick is separated by a visible white interval; it is not one continuous bent path.',15,'high')
change('17-327-deleted-quotes','327, l-14, cancelled quotation after isn\'t',"\\deleted{\\unsure{''}}","\\deleted{''}",'misread symbol or index','Two short raised bodies survive in the crossed cluster, before the live there!; the deletion is local to that former closing pair.',17,'medium')
change('18-329-semisimplicial-edges','329, second l.-13, quotation and terminal mark',"``semisimplicial.","\\unsure{``|'}semisimplicial\\unsure{,|.}",'misread symbol or index','The opener is a compact branching stroke, compatible with a joined pair or one hooked quote. The low terminal mark has a short descending/curved body, favouring a comma but not securely excluding a period. No closing quotation is supplied.',19,'low')
old="\\inserted{l-5 ``developing\\unsure{''}}"
new=segment(R,'\\node[anchor=south west,inner sep=0pt] at (-.75,2.1)',r'\fill (-.25,4.8)')
change('19-329-added-enveloping','329, raised l-5 addition at the right edge',old,new,'misread word','The first letter is a small e loop, followed by the n/v sequence: enveloping. There is no initial tall d. A low point follows l-5. The entry stands above semisimplicial beside the long slanted sign. Only one terminal high quote stroke is visible before the clipped edge, so both a single and an incompletely preserved double remain possible.',20,'high')
old="\\margin{? (I'm not \\unsure{certa|certain} if it is 1 or 2 \\unsure{p|r}}"
new=segment(R,'\\normalmarginpar\\margin{',r'% slanted').rstrip()
change('20-329-margin-layout','329, clipped slanted note in the right margin',old,new,'insertion or placement','The question mark sits above two slanted lines. The broad left curve begins below the first-line height and turns underneath the second line; it is reproduced geometrically, without supplying a lost closing parenthesis. The margin stays on the right. The low isolated point is separately inventoried.',21,'high')
change('21-329-high-points','Above the raised l-5 note', '',r'\fill (-.25,4.8) circle (.035);\fill (-.18,5.1) circle (.03);','drawing or diagram','Two separate dark points/strokes are above-left of l-5, clear of the reference letters. Their geometrical positions are retained without assigning a textual role.',20,'medium')
change('22-329-low-point','Below/right of the right marginal note','',r'\fill (2.8,-3.2) circle (.035);','drawing or diagram','A separate small dark point is below the writing and right of the physical hole. It is drawn without interpreting its function.',21,'medium')
change('23-left-rule','Long rule separating page references from corrections','',r'\draw[line width=.3pt] ([xshift=.45em,yshift=1.3ex]sc27Clefttop) -- ([xshift=.05em,yshift=-2.6ex]sc27Cleftbottom);','drawing or diagram','The thin rule begins at the upper reference area near x241 and continues to the lower paper edge near x247. It is placed through the list at the boundary of the page-number column, not in a detached panel.',source=W,bbox=[236,88,252,2349])
change('24-right-rule','Long rule near the right edge of the main writing','',r'\draw[line width=.3pt] ([xshift=.93\linewidth,yshift=1.1ex]sc27Ctop) -- ([xshift=.935\linewidth,yshift=-2.8ex]sc27Cbottom);','drawing or diagram','The thin right rule starts near x1516,y95, passes through the 303 and 315 long lines and beside the marginal note, and reaches the lower paper edge near x1526. The whole and both halves show its extent.',source=W,bbox=[1510,90,1532,2349])

c_doubts=[]
def doubt(place,c,reading,resolved,evidence,n=None,confidence='low',source=None,bbox=None,category='explicit C doubt'):
    c_doubts.append({'place':place,'c':c,'reading':reading,'resolved':resolved,'confidence':confidence,'evidence':evidence,'category':category,**ev(n,source,bbox)})

doubt('Top page reference',r'\unsure{302}',r'\unsure{302}',False,'The surviving lower curves support 302, but the faint upper portions do not decide all three numerals. The text is faded within the photograph rather than physically cut at its top edge.',1,'medium')
doubt('Top line reference',r'\unsure{15}','15',True,'Straight 1 followed by a faint upper bar and an open lower 5 curl.',1,'medium')
doubt('303, cancelled word before which',r'\unsure{with|who}',r'\unsure{with|who}',False,'The cancellation covers the central humps and the connection into the last body. A tall crossed stroke and a right loop do not securely distinguish with and who.',2)
doubt('304, cancelled line reference',r'\unsure{l-2}',r'\unsure{l-2}',False,'The l and a short dash are visible, but the following numeral shares the zigzag crossing.',4)
doubt('304, cancelled no/not',r'\unsure{no|not}',r'\unsure{no|not}',False,'The n and o survive; the crossing at their right edge could cover a short final t, so the two candidates are retained.',4)
doubt('306, cancelled upright before also',r'\unsure{l|it}','l',True,'One looped ascender and its foot are visible; there is no independent dotted i or separate t.',5,'medium')
doubt('312, cancelled line reference',r'\unsure{l-6}','l-6',True,'The low closed 6 bowl and its upward return survive below the cancellation.',6,'high')
doubt('312, cancelled lets/let\'s',r"\unsure{lets|let's}",r"\unsure{lets|let's}",False,'The l, t cross-stroke and final s remain, but a tiny raised remnant near the apostrophe position is not securely separable from the crossing.',6)
doubt('313 continuation, raised cancelled fragment',r'\unsure{out|at|on|or}',r'\unsure{out|at|on|or}',False,'The opening small loop and following short humps are visible above the cancellation; the terminal part runs into the adjacent crossed reference. No candidate is excluded confidently.',7)
doubt('313 continuation, line reference before live filtering',r'\unsure{l-2|l-7}',r'\unsure{l-2|l-7}',False,'The lower numeral favours 2, but its upper path and the l are crossed and joined to the cancelled cluster; 7 cannot be excluded securely.',7)
doubt('315, old middle of Sentence',r'\unsure{ann|en}',r'\unsure{ann|en}',False,'The old and new medial strokes overlap. The live form is Sentence; the buried ann/en remains unresolved, independently of the certain overwrite extent.',8)
doubt('315, short cancelled word before in order',r'\unsure{to}','to',True,'A crossed t and the small right-hand o loop are both visible.',9,'medium')
doubt('315, cancelled presumably',r'\unsure{presumably}',r'\unsure{presumably}',False,'The p stem, central humps and terminal y favour presumably, but the middle letters are crossed by both the insertion and the long cancellation.',10,'medium')
doubt('315, cancelled No/Now',r'\unsure{No|Now}',r'\unsure{No|Now}',False,'The N and round continuation remain; the long crossing hides whether a terminal w was present.',11)
doubt('316, cancelled it before is',r'\unsure{it}','it',True,'Short dotted i and a separate crossed t can be followed underneath the diagonal strike.',12,'high')
doubt('316, final cancelled word after a',r'\unsure{to|is}',r'\unsure{to|is}',False,'The tall overwritten loop, upper right return and lower curl remain ambiguous. The quote pair before the cluster is live and separate.',13)
doubt('326, first cancelled ampersand',r'\unsure{\&}',r'\&',True,'Two loops and a terminal return identify the character despite the crossing.',15,'medium')
doubt('327, cancelled quotes before there',r"\unsure{''}","''",True,'The crossed cluster contains two short raised quote bodies before the separate live word there.',17,'medium')
doubt('329, clipped final quote of added word',r"\unsure{''}",r"\unsure{'|''}",False,'One high oblique stroke is preserved at the cropped edge. A second member may be lost; the single visible member is not silently doubled.',20)
doubt('329, clipped certa/certain',r'\unsure{certa|certain}',r'\unsure{certa|certain}',False,'The visible start is certa-. The edge cuts the end, so the supplied longer alternative remains uncertain.',21)
doubt('329, clipped final p/r',r'\unsure{p|r}',r'\unsure{p|r}',False,'A left stem and shoulder survive after 2; the right and lower extent are interrupted by the physical edge. Context is not used to force p.',21)

# Page-specific C_context alternatives and notation, each occurrence checked independently.
triangle1=segment(C,r'\mathord{\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.085ex',r'\tikz[remember picture,overlay]{\coordinate(scxxviin);')
second_start=r'\mathord{\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.085ex,line cap=round,line join=round] (.20,0)'
triangle2=segment(C,second_start,'/F$')
triangle3=segment(C,r'\mathord{\tikz[baseline=0pt,x=1ex,y=1ex]{\draw[line width=.09ex',"$ (doubled")
doubt('327 l7, first double-sided triangle',triangle1,triangle1,True,'The extra left stroke starts clear of the base; the first triangle is retained as its individually traced glyph.',15,'high',category='page-specific context')
doubt('327 l7, second double-sided triangle',triangle2,triangle2,True,'The outer diagonal meets the left foot of this second outline; its shape is independently visible.',15,'high',category='page-specific context')
doubt('329 l6, third double-sided triangle',triangle3,triangle3,True,'This outline is taller and its second left stroke meets the foot, unlike the first 327 glyph.',source=B,bbox=[402,934,457,997],confidence='high',category='page-specific context')
doubt('327 l7, alpha, colon, slash and F',r'\alpha; /F',r'\alpha; /F',True,'The rounded alpha has its own lower loop; two colon points, a right arrowhead, an oblique slash and ordinary F are visible. No subscript placement or doubled F is supplied.',15,'high',category='page-specific context')
doubt('334 l3, membership and each lowered index',r'b\in A_{n-1}',r'b\in A_{n-1}',True,'Small b precedes the right-open membership sign. The n, short horizontal, and final 1 are separately below the ordinary A baseline.',source=B,bbox=[386,1125,578,1197],confidence='high',category='page-specific context')
doubt('316 l12, i(a)',r'i(a)',r'i(a)',True,'The leading i has its own dot; the argument is a closed a, inside round parentheses.',12,'high',category='page-specific context')
doubt('303 l.-3, final A and possible prime',r'$A$ by $A$',r'$A$ by $A$',True,'The final A has a retraced crossbar and left return; the next two high strokes are the closing quotation. No separate prime occurs between them and A.',3,'high',category='page-specific context')
doubt('315, respect. concerning',r'respect. concerning',r'respect. concerning',True,'The upper half shows a low point after respect and a lowercase c at the beginning of the next manuscript line.',source=A,bbox=[1434,908,1645,967],confidence='high',category='page-specific context')
doubt('327, terminal mark after should it be',"should it be '","should it be '",True,'The terminal small oblique mark is raised, not on the word baseline. It is retained as the single visible tick without supplying a missing question mark.',16,'high',category='page-specific context')
doubt('329, word beside the clipped spelling question','developing','enveloping',True,'The initial small e loop and following n/v sequence are visible. This is independent of the ordinary developing entry at p.320.',20,'high',category='page-specific context')

remaining=[]
def rem(place,reading,alternatives,confidence,reason):
    remaining.append({'place':place,'reading':reading,'alternatives':alternatives,'confidence':confidence,'reason':reason})
for d in c_doubts:
    if d['category']=='explicit C doubt' and not d['resolved']:
        reading=d['reading']
        alternatives=reading.removeprefix('\\unsure{').removesuffix('}')
        remaining.append({'place':d['place'],'reading':reading,'alternatives':alternatives,'confidence':d['confidence'],'reason':d['evidence']})
rem('317 l-16 opener',r"\unsure{``|'}","double opener | single opener",'low','The compact hook has a short second leg but no secure separation into two strokes; the i-dot is a different, lower mark.')
rem('329 semisimplicial opener',r"\unsure{``|'}","double opener | single opener",'low','One branching high body remains compatible with a fused pair and with a single hook.')
rem('329 semisimplicial terminal mark',r'\unsure{,|.}','comma | period','low','The low mark has a small downward/curved extension, favouring comma, but its short size leaves a period possible.')

inventory=[]
def inv(kind,position,first,hand='his hand'):
    inventory.append({'sheet_kind':'list','hand':hand,'element':f'{len(inventory)+1:02d}','kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('text','Top faint entry','302 l.15 ``its')
inv('drawing','Left boundary of page-reference column, upper entry to foot','Thin near-vertical rule','unassigned ruled line; surrounding text in his hand')
inv('drawing','Right boundary of main writing, upper margin to foot','Thin near-vertical rule','unassigned ruled line; surrounding text in his hand')
inv('text','303 entry, first line and continuation','303 l.1; l2; l.-3; - not clear what you mean.')
inv('deletion','303, immediately before which','with|who')
inv('text','304 entry','304 l-15 ``commutes with'' also l-13.')
inv('deletion','304, right-hand cancelled continuation','l-2 ``play'' no|not ``s; last quote pair outside cancellation')
inv('text','305 entry','305 l.5 ``interpret\' l14 ``commutes with''')
inv('text','306 entry','306 l.19 ``its''; also l-5; l-4 test category')
inv('deletion','306 before also','l')
inv('text','306 l-4, nested underline','category, single underline')
inv('text','309 entry','309 l.-8 ``on the previous''')
inv('text','309, nested underline','the, single underline')
inv('text','312 entry','312 l-.8 ``isn\'t''')
inv('deletion','312, cancelled continuation','l-6 lets|let\'s')
inv('text','313 main line','313 l9; l.18; l-12')
inv('text','313 continuation, replacement entry','l-2|l-7 filtering''')
inv('deletion','313 continuation, before replacement','filtering')
inv('deletion','313 continuation, nested raised fragment','out|at|on|or above baseline')
inv('text','314 entry','314 l.5 ``isn\'t'' l.6 ``as is''')
inv('text','315 long proposed rewording','Sentence starting l.7 - difficult to understand. Possibly:')
inv('deletion','315, middle of Sentence','Old ann|en, overwritten in place')
inv('text','315, live middle of Sentence over old cluster','en; shared Sent and ce occur once')
inv('deletion','315, before in order to','to')
inv('text','315 quoted proposal, nested underline','push home')
inv('text','315 quoted proposal, nested underline','no more')
inv('text','315 quoted proposal, nested underline','to express')
inv('text','315 quoted proposal, nested underline','does')
inv('text','315 quoted proposal, nested underline','stand')
inv('deletion','315, abandoned parenthesis, first manuscript line','(This is true presumably')
inv('insertion','315, above true within cancelled parenthesis','certainly')
inv('insertion','315, above presumably within cancelled parenthesis','as far as our')
inv('deletion','315, abandoned parenthesis, second manuscript line','at the present knowledge goes). No|Now and two short low dashes with a point')
inv('text','315, live rewritten parenthesis across two manuscript lines','(This certainly seems to be so as far as our present knowledge goes)')
inv('text','315 continuation, l.17 and l.-3','``its''; and which allow one to compute')
inv('insertion','315 l.-3, above line with lower caret','would')
inv('text','316 entry','316. l.1 ``shouldn\'t'' l12 i(a) is a')
inv('deletion','316 l12, before is','it')
inv('deletion','316 l12, after a and live closing pair','to|is')
inv('text','317 entry','317. l.11 its; l-16 isn\'t')
inv('text','320 entry','320 l 8. indispensable; l-15 developing; l-8 its')
inv('text','321 entry','321 l.9 isn\'t')
inv('text','323 entry','323 l13 don\'t')
inv('text','326 entry','326 l-12 & l.-8 commutes with and')
inv('deletion','326, upper first ampersand','&')
inv('insertion','326, raised over opening of commutes','& l-3')
inv('drawing','326, after raised 3','Small high point, unassigned punctuation function')
inv('drawing','Between 326 and 327, just right of first triangle','Long oblique stroke and separate short bent tick')
inv('text','326, nested underline','with')
inv('text','327 l7, quoted formula and following question','alpha: first doubled-side triangle -> second doubled-side triangle /F; should it be and one raised tick')
inv('text','327 continuation, l-17 to l-14','allows one to; doesn\'t; isn\'t there!')
inv('text','327 l-17, nested underline','one')
inv('deletion','327 l-14, between isn\'t and there','Former closing quotation pair')
inv('text','327 short continuation','l-5 don\'t')
inv('text','328 main entry','p328 l-12 should ``wouldn\'t'' = ``shouldn\'t''')
inv('deletion','328, before should','wouldn\'t')
inv('text','328 short continuation','l-10 doesn\'t')
inv('text','329 l.6','Third doubled-side triangle (doubled side is missing) its')
inv('text','329 lower main line','l12 don\'t; l-13 makes sense; l.-13 semisimplicial')
inv('insertion','329, above/right of semisimplicial beside long mark','l-5. enveloping with clipped closing quote')
inv('drawing','329, after semisimplicial at right edge of body','Long oblique sign with a short lower branch')
inv('drawing','329, above-left of added l-5','Two isolated high points/strokes')
inv('margin note','329, right margin, slanted and clipped','? above I\'m not certa|certain / if it is 1 or 2 p|r')
inv('drawing','329, left and underside of right marginal writing','Broad opening curve, with no supplied closing mate')
inv('drawing','329, below/right of marginal writing','Isolated low point')
inv('text','333 entry','p.333 l.-12 makes sense')
inv('text','334 final entry','p.334 l.3 b in A_(n-1); l-6 its also in l-5.')
inv('margin note','Lower-left archive corner; comment only','26','another unnamed hand (archive pencil number)')

report={
'scan':27,'reader':'C','model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':[W,A,B],
'layout':'One densely written handwritten correction list, faint first entry and a large rewritten paragraph under 315. Page references occupy the narrow left column separated by a thin vertical rule; a second thin rule runs near the right edge and through several long lines. Both rules reach the lower paper edge. The top entry is faded within the photographed sheet, not physically clipped by the top edge. There are multiple local cancellations, an overwritten middle in Sentence, three raised/interlinear corrections in 315, a raised & l-3 above 326, a two-stroke connector beside the 327 formula, and a raised clipped correction plus two-line slanted right marginal note at 329. All textual entries are in the same principal hand. There is no title or manuscript page number; 26 is an archive corner annotation. The circular edge marks are physical holes, not mathematical drawings.',
'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
'notes':[
'This sheet lists correction targets from the faint 302 reference through 334, with gaps in the sequence. The line references and quoted spellings are retained, including missing or asymmetric delimiters.',
'At 303 l.-3, the manuscript says image of A by A and adds - not clear what you mean. The final A has no separately visible prime.',
'At 315, the sentence starting l.7 is called difficult to understand, followed by Possibly and an extended proposed wording. The live qualification reads This certainly seems to be so as far as our present knowledge goes; the prior parenthetical attempt is cancelled, including its raised additions.',
'At 327 l7, the question after alpha and the two individually shaped doubled-side triangle glyphs ends should it be with a raised tick. The target is written slash F, not supplied as a subscript. No mathematical conclusion is inferred from the question.',
'At 328 l-12, the cancellation of the first wouldn\'t and the following wording should ``wouldn\'t'' = ``shouldn\'t'' are retained literally.',
'At 329 l6, the third triangle is followed by doubled side is missing. The raised clipped l-5 correction reads enveloping, and the neighbouring question refers to whether there is 1 or 2 of an edge-clipped letter that remains p/r.',
'At 334 l3, b in A_(n-1) is quoted. There is no stated total page count, title sheet, date, or author pagination on this assigned image.'
],
'math_checks':[],
'notation':[
{'sign':'three doubled-left-side triangles','location':'327 l7, two occurrences; 329 l6','reading':triangle1+' ; '+triangle2+' ; '+triangle3,'evidence':'Each outline was checked separately. The first extra stroke starts above the base; the second and third meet the left foot. C\'s three individual TikZ traces are retained.'},
{'sign':'alpha, colon, right arrow, slash F','location':'327 l7','reading':r'\alpha; :; \longrightarrow; /F','evidence':'Rounded alpha, two colon points, a right-facing arrowhead, diagonal slash and single-contour F.'},
{'sign':'A by A','location':'303 l.-3','reading':r'$A$ by $A$','evidence':'The final A has a retraced crossbar; the high pair is the closing quotation, with no independent prime.'},
{'sign':'i(a)','location':'316 l12','reading':r'i(a)','evidence':'Separate i-dot, round parentheses and closed a.'},
{'sign':'b in A_(n-1)','location':'334 l3','reading':r'b\in A_{n-1}','evidence':'Ordinary b and A; right-open membership sign; each of n, dash and 1 lowered independently.'},
{'sign':'single and double quotation strokes','location':'Throughout; especially 317 l-16 and 329 semisimplicial/addition','reading':r"\unsure{``|'}; \unsure{``|'}; \unsure{'|''}",'evidence':'Quotation edges were read separately. Two compact openers and the clipped added-word closer remain individually doubtful; ordinary clear singles and pairs elsewhere are not regularized.'},
{'sign':'underline spans','location':'306 category;309 the;315 push home/no more/to express/does/stand;326 with;327 one','reading':r'\uline{category}; \uline{the}; \uline{push home}; \uline{no more}; \uline{to express}; \uline{does}; \uline{stand}; \uline{with}; \uline{one}','evidence':'Each is a single baseline rule confined to the indicated word or phrase.'}
],
'abbreviations':[
{'form':'l. / l','expansion':'line; negative references appear to count back from the end (interpretation only)','place':'Correction references throughout'},
{'form':'p. / p','expansion':'page (interpretation only)','place':'327–334 page references'},
{'form':'resp...','expansion':'respect, or related abbreviation; incomplete in the quoted proposal','place':'315 proposed wording'},
{'form':'cat.','expansion':'category (tentative interpretation only)','place':'315 proposed wording'}
],
'brief_feedback':'Required files were read. Exactly one whole-page and one view of each supplied half were made, followed by 21 frozen tight enhanced crops, each displayed once. The half images themselves have native width 1685 pixels; crop.py supplied the single enhanced version at 2400 pixels. No OCR, recognition library, other page image, other reader return, external research, or compilation was used. Full inventory coverage includes each correction entry/continuation, the nested cancellations and insertions, all underline spans, both long rules, the lower marginal drawing/text and small isolated dark marks. H is description-only; h is null and diff_h false in every change, with no H collation rows. math_checks is empty because no proof, computation, or substantive mathematical check was performed beyond reading the quoted correction targets. The parent should adjudicate the low-confidence quotation and cancelled-letter readings from the retained crops.'
}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
observations=[
'302 retained doubtful; l.15 resolved from faint upper bar and lower 5 curve.',
'Cancelled with/who retained; old endings not separable.',
'Final A confirmed unprimed; high pair belongs to closing quotation.',
'Line l-2 and no/not retained doubtful; final quote pair outside cancellation.',
'Cancelled l resolved.',
'Cancelled l-6 resolved; lets/let\'s retained.',
'Raised cancelled fragment and adjacent reference remain doubtful; raised height retained.',
'Live Sentence with overlapping uncertain old ann/en middle.',
'Cancelled to resolved.',
'Interlinear certainly and as far as our placed above old words; presumably retained doubtful.',
'No/Now retained; two low dash strokes plus a point after the word.',
'Cancelled it resolved; i(a) separately confirmed.',
'Cancelled final to/is retained; preceding quote pair live.',
'317 opener remains double/single; separate lower point is i-dot.',
'Old & resolved; raised reference, high point and separate connector tick retained.',
'Terminal raised tick after should it be confirmed.',
'Cancelled pair after isn\'t resolved; there! remains live.',
'329 don\'t opener confirmed double.',
'Semisimplicial opener and low terminal comma/period remain doubtful.',
'Enveloping read clearly; low point after l-5; clipped final quote revised to single/double doubt; two high points retained geometrically.',
'Clipped certa/certain and p/r retained; question/lines/curve/right margin placement and isolated low point retained.'
]
(root/'crop_view_audit.json').write_text(json.dumps([{'id':z['id'],'crop':'crops/'+Path(z['crop']).name,'displayed':True,'display_count':1,'observation':o} for z,o in zip(frozen['loci'],observations)],ensure_ascii=False,indent=2)+'\n')
(root/'literal_diff.txt').write_text(''.join(difflib.unified_diff(C.splitlines(True),R.splitlines(True),fromfile='supplied C.tex',tofile='reader C reading.tex')))
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'explicit_c_doubts':sum(x['category']=='explicit C doubt' for x in c_doubts),'explicit_c_doubts_resolved':sum(x['category']=='explicit C doubt' and x['resolved'] for x in c_doubts),'remaining_doubts':len(remaining),'inventory_rows':len(inventory),'crops':len(observations),'math_checks':0},indent=2))
