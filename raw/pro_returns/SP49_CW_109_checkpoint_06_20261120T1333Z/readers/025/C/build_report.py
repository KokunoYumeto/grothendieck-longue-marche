from pathlib import Path
import json
import itertools
import re

ROOT = Path('/workspace/scratch/6d55c8c3e5a7')
OUT = ROOT / 'work/readers/025/C'
SRC = ROOT / 'source/SP49_CW_109_scans'
WHOLE = str(SRC / 'H109-02_109_scan025.jpg')
A = str(SRC / 'H109-02_109_scan025_a.jpg')
B = str(SRC / 'H109-02_109_scan025_b.jpg')
frozen = json.loads((OUT / 'frozen_unresolved.json').read_text())
loc = {x['id']: x for x in frozen['loci']}

wave = r'''\tikz[baseline=-.4ex,x=.23em,y=.23em]{
  \draw[line width=.35pt] (0,0) .. controls (.6,.3) and (.9,.2) .. (1.1,.2)
    .. controls (1.2,.8) and (1.4,.6) .. (1.4,.1)
    .. controls (1.9,-.1) and (2.2,-.5) .. (2.6,-.5);
  \fill (3.8,-.6) circle (.25pt);
  \fill (5.2,-.8) circle (.22pt);
}'''
high_quote = r'''\raisebox{1.3ex}[0pt][0pt]{\deleted{\unsure{''}}}'''
neither_point = r'''\raisebox{1.1ex}[0pt][0pt]{\makebox[0pt][l]{\tikz{\fill (0,0) circle (.25pt);}}}'''
p273_point = r'''\hspace{.35em}\raisebox{.8ex}[0pt][0pt]{\tikz{\fill (0,0) circle (.25pt);}}'''

p247 = r'''p.247 \deleted{l.14 ``\unsure{aspheric}''}
\raisebox{2.6ex}[3.4ex][0pt]{\makebox[0pt][l]{\scriptsize
\inserted{(Cond\textsuperscript{n} (ii) should it be $i_0\colon N_{\unsure{0|i}}\to N$)}}}
\tikz[remember picture,baseline]{\coordinate (s025-p247-old);}%
\deleted{should it be $(i_{\unsure{0|i}}\colon N\unsure{)}$''}; l-9 ``standard''

l12 ``is aspheric''\tikz[remember picture,baseline]{\coordinate (s025-p247-lower);}%
\quad also \qquad l-2 ``didn't'''''

left_rule = r'''\draw[line width=.25pt]
  ([xshift=.065\linewidth,yshift=.7ex]s025-top) --
  ([xshift=.072\linewidth,yshift=-1.7ex]s025-bottom);'''
right_rule = r'''\draw[line width=.3pt]
  ([xshift=.94\linewidth,yshift=.8ex]s025-top) --
  ([xshift=.948\linewidth,yshift=-1.7ex]s025-bottom);'''
faint_rule = r'''\draw[line width=.15pt,black!25]
  ([xshift=-.06\linewidth,yshift=-2.0ex]s025-top) --
  ([xshift=-.058\linewidth,yshift=-1.0ex]s025-p245);'''
p247_connector = r'''\draw[line width=.35pt]
  ([xshift=.2em,yshift=.3ex]s025-p247-old)
  .. controls ([xshift=2em,yshift=-.4ex]s025-p247-old)
  and ([xshift=.9em,yshift=.7ex]s025-p247-lower)
  .. ([xshift=.25em,yshift=-.65ex]s025-p247-lower);'''
p247_tail = r'''\draw[line width=.3pt]
  ([xshift=6.3em,yshift=-1.0ex]s025-p247-old) --
  ([xshift=5.7em,yshift=-3.3ex]s025-p247-old);'''
p263_marks = r'''\draw[line width=.35pt]
  ([xshift=-.55cm,yshift=-1.0ex]s025-p263-end) --
  ([xshift=-.49cm,yshift=-1.3ex]s025-p263-end);
\draw[line width=.25pt]
  ([xshift=-2.1cm,yshift=-2.0ex]s025-p263-end) --
  ([xshift=-2.15cm,yshift=-2.15ex]s025-p263-end);
\fill ([xshift=-.2cm,yshift=-3.1ex]s025-p263-end) circle (.25pt);'''
p269_marks = r'''\fill ([xshift=.963\linewidth,yshift=-.65ex]s025-p269) circle (.25pt);
\fill ([xshift=.960\linewidth,yshift=-1.08ex]s025-p269) circle (.25pt);
\draw[line width=.35pt]
  ([xshift=.963\linewidth,yshift=-1.85ex]s025-p269) --
  ([xshift=.972\linewidth,yshift=-1.85ex]s025-p269);'''

c_text = (ROOT / 'work/inputs/025/C.tex').read_text()
reading = c_text
replacements = [
    (r'''...\deleted{\unsure{''}} ...''', '...'+high_quote+' '+wave),
    (r'''\deleted{p\unsure{23}}''', r'''\deleted{p23}'''),
    (r'''neither... \unsure{not|nor}....''', 'neither'+neither_point+r'''... not....'''),
    (r'''p.247 \deleted{\unsure{l.14} ``\unsure{aspheric}''} \inserted{(Cond\textsuperscript{n} (ii) should it be $i_{\unsure{0|i}}\colon N_0\to N$)} \deleted{should it be $(i_0\colon N)$\unsure{''}} \inserted{also}; l-9 ``standard''

l12 ``is aspheric'' l-2 ``didn't''''', p247),
    (r'''\deleted{\unsure{2}} 255''', r'''\deleted{2} 255'''),
    (r'''262 \deleted{\unsure{-13}} l-3 \& \unsure{-}2''', r'''262 -\deleted{\unsure{13|l13}} l-3 \& 2'''),
    (r'''allow\unsure{s} one to''', r'''allow\unsure{e|s} one to'''),
    (r'''``pushing on the.''', r'''``pushing on the.\tikz[remember picture,baseline]{\coordinate (s025-p263-end);}'''),
    (r'''264 \unsure{'}l12''', r'''264 'l12'''),
    (r'''\deleted{isn't the use of $\pi_0,\pi_1$ slightly confusing here!}''', r'''\deleted{isn't the use of $\pi_0,\pi_1$ slightly confusing here}!'''),
    (r'''\deleted{\unsure{not} $\pi_0,\pi_1$}''', r'''\deleted{not $\pi_0,\pi_1$}'''),
    (r'''p.273 l-7''', 'p.273'+p273_point+' l-7'),
]
for before, after in replacements:
    assert reading.count(before) == 1, before
    reading = reading.replace(before, after)
reading = reading.replace('p225 line', r'''\tikz[remember picture,baseline]{\coordinate (s025-top);}p225 line''', 1)
reading = reading.replace('p245. l.4', r'''\tikz[remember picture,baseline]{\coordinate (s025-p245);}p245. l.4''', 1)
reading = reading.replace('p.269: middle', r'''\tikz[remember picture,baseline]{\coordinate (s025-p269);}p.269: middle''', 1)
reading = reading.replace('p.274 l-9', r'''\tikz[remember picture,baseline]{\coordinate (s025-bottom);}p.274 l-9''', 1)
reading = reading.replace(r'\scanpage{25}', r'''\cotefile{109}
\scanpage{25}
\noindent\begin{minipage}{\linewidth}
\small
\setlength{\parindent}{0pt}
\setlength{\parskip}{2pt}''', 1)
overlay = '\n'.join([left_rule, right_rule, faint_rule, p247_connector, p247_tail, p263_marks, p269_marks])
reading += '\n% The rules and isolated marks remain anchored beside the corresponding writing.\n'
reading += r'\begin{tikzpicture}[remember picture,overlay]'+'\n'+overlay+'\n'+r'\end{tikzpicture}'+'\n'+r'\end{minipage}'+'\n'
(OUT / 'reading.tex').write_text(reading)

changes=[]
def change(id, place, c, new, kind, evidence, crop=None, source=None, bbox=None, confidence='high'):
    if crop:
        item=loc[crop]
        source=source or item['source']; bbox=bbox or item['bbox']; crop=item['output']
    changes.append(dict(id=id,place=place,c=c,h=None,reading=new,diff_c=True,diff_h=False,
                        kind=kind,marked_in_H=False,confidence=confidence,evidence=evidence,
                        crop=crop,source=source,bbox=bbox))

change('rules-left','long rule through the reference column','',left_rule,'drawing or diagram',
       'A continuous thin nearly vertical rule begins beside the first entry and descends through/along the right edges of the page references to the last entry.',source=WHOLE,bbox=[224,88,251,2300])
change('rules-right','long rule near the right edge of the writing','',right_rule,'drawing or diagram',
       'The right rule extends from first-entry height to the final-entry height; long lines of writing reach across it. The TeX anchors it beside the text.',source=WHOLE,bbox=[1500,86,1534,2297])
change('rules-faint-left','faint far-left partial vertical trace','',faint_rule,'drawing or diagram',
       'A faint narrow upright trace stands well left of the reference column and ends near the p245/p246 level; no editorial function is assigned.',source=WHOLE,bbox=[42,116,62,1081],confidence='medium')
change('p234-high-cancel','p234 l.7, cancelled high mark between continuation groups',r'''\deleted{\unsure{''}}''',high_quote,'insertion or placement',
       'The crossed cluster sits above the baseline beneath synonym, not at the height of the surrounding low continuation marks. Its possible quote identity remains doubtful.','03',confidence='medium')
change('p234-wave','p234 l.7, second continuation group','...',wave,'drawing or diagram',
       'The group consists of a connected wavy stroke with an upward nib, followed by two separated low points. Its geometry is preserved without naming a mathematical sign.','03',confidence='medium')
change('p234-cancel-ref','cancelled page reference before l.-6',r'''\deleted{p\unsure{23}}''',r'''\deleted{p23}''','misread symbol or index',
       'The p stem/bowl, angular foot of 2, and two rightward lobes of 3 survive the two crossing rules; the terminal curved cancellation return is not read as another digit.','04',confidence='medium')
change('p243-not','p243 l-6, conjunction after neither...',r'''\unsure{not|nor}''','not','misread word',
       'The last letter has an upright extending through the middle horizontal and a long cross-stroke; the surviving form is t. The grammatical attraction of nor is not used.','07')
change('p243-high-point','p243 l-6, high point after neither','',neither_point,'omission',
       'A separate small upright point stands above/right of the terminal r, before the low three-dot group; it is not the dot of the earlier i.','07',bbox=[1306,813,1321,836],confidence='medium')
change('p247-line-ref','p247 first cancelled reference',r'''\unsure{l.14}''','l.14','misread symbol or index',
       'The initial looped l, low point, following straight 1 and crossed 4 remain distinguishable below/through the zigzag.','08',confidence='medium')
change('p247-live-i0','p247 raised note, subscript of i',r'''i_{\unsure{0|i}}''','i_0','misread symbol or index',
       'The lowered character is a closed oval with a white centre. The separate high dot belongs to the main i; the low character itself has no separate dot.','09')
change('p247-live-N-index','p247 raised note, subscript of N','N_0',r'''N_{\unsure{0|i}}''','misread symbol or index',
       'Unlike the preceding i subscript, this tiny lowered character has an open lower cup and a detached dark upper touch; a broken 0 and a small dotted i remain possible.','09',confidence='low')
change('p247-old-i-index','p247 cancelled lower mapping, subscript of i','i_0',r'''i_{\unsure{0|i}}''','misread symbol or index',
       'The lower companion of i is crossed by a heavy oblique cancellation stroke, so the unmarked 0 in C is not secure at this separate occurrence.','10',confidence='low')
change('p247-old-closer','p247 cancelled mapping, closing parenthesis',')',r'''\unsure{)}''','misread symbol or index',
       'The final curved stroke merges with the terminal cancellation zigzag. A closing parenthesis remains the best reading but is not independently separable.','10',confidence='low')
change('p247-old-quotes','p247 right end of cancelled mapping',r'''\unsure{\'\'}'''.replace('\\\'','\''),"''",'misread symbol or index',
       'Two short raised tips remain at the right edge, with their lower portions crossed by the terminal diagonal; the paired quotation reading is retained without the old doubt.','10',confidence='medium')
# Keep the exact C literal, including the two ordinary apostrophes.
changes[-1]['c'] = r"\unsure{''}"
change('p247-also','p247, also beside the lower l12 entry',r'''\inserted{also}; l-9 ``standard''

l12 ``is aspheric'' l-2 ``didn't''''',r'''; l-9 ``standard''

l12 ``is aspheric'' \quad also \qquad l-2 ``didn't''''','insertion or placement',
       'Also is written on the lower line after is aspheric, beyond a descending curved rule. There is no caret placing it before the upper semicolon. The word is preserved at its observed lower position.','10')
change('p247-curved-rule','p247, curve descending beside also','',p247_connector,'drawing or diagram',
       'A long curved stroke begins by the cancelled should phrase, bows right, and descends to the gap between the lower quoted phrase and also. No arrowhead is visible.','10')
change('p247-descending-tail','p247, oblique tail below the cancelled mapping','',p247_tail,'drawing or diagram',
       'An oblique downward-left tail continues below the low parenthesis/cancellation area and stops beside the lower line; it is not a textual slash between words.','10',confidence='medium')
change('p255-old-digit','cancelled numeral before 255',r'''\unsure{2}''','2','misread symbol or index',
       'The original upper curved start, diagonal descent and low rightward foot of 2 survive under the crossing slash. The following 255 is not used to supply the digit.','14',confidence='medium')
change('p262-old-ref','262, old cancelled reference',r'''\deleted{\unsure{-13}}''',r'''-\deleted{\unsure{13|l13}}''','deletion state (struck given live or live given struck)',
       'The short leading dash is separated by white space from the crossing strokes and is left live. The heavily crossed group has a final double-lobed 3 and preceding vertical strokes; 13 is favoured, with a possible initial looped l retained.','15',confidence='low')
change('p262-second-ref','262, after the ampersand',r'''\& \unsure{-}2''',r'''\& 2''','text not on the page',
       'There is no separate horizontal minus between the ampersand terminal and the 2. The nearby oblique/low stroke is part of the numeral contour.','16')
change('p263-allow','263 l.19, final letter after allow',r'''allow\unsure{s}''',r'''allow\unsure{e|s}''','misread word',
       'The small retraced character has an oval/loop with a short rightward exit, favouring e; a compact s is still possible. Expected English allows is not allowed to decide the ink.','17',confidence='low')
change('p263-marks','263, blank area below/right of pushing on the.','',p263_marks,'drawing or diagram',
       'The lower half clearly shows two short oblique touches and one lower point in the blank area to the right of the next correction line; they are reproduced in their local relation.',source=B,bbox=[1248,662,1472,725],confidence='medium')
change('p264-high-stroke','264, immediately before l12',r'''\unsure{'}''',"'",'misread symbol or index',
       'One detached high upright stroke stands left of the looped l. The crop separates it from the l ascender and shows no second quote stroke. Its grammatical role is not inferred.','18')
change('p269-exclamation','p269, final exclamation of the cancelled first question',r'''\deleted{isn't the use of $\pi_0,\pi_1$ slightly confusing here!}''',r'''\deleted{isn't the use of $\pi_0,\pi_1$ slightly confusing here}!''','deletion state (struck given live or live given struck)',
       'The cancellation runs through the space between the high exclamation stem and its detached lower point; neither component is crossed. The word here remains in the cancelled phrase.','19')
change('p269-not','p269, beginning of the second cancelled group',r'''\unsure{not}''','not','misread word',
       'The n shoulder, the lower oval of o, and the t upright/crossbar/foot survive the separate cancellation strokes.','20')
change('p269-margin-marks','right margin at p269, beyond the long rule','',p269_marks,'drawing or diagram',
       'Two separated round points and a lower short horizontal stroke are visible to the right of the rule. They are retained geometrically without assigning punctuation or a mathematical role.','21')
change('p273-point','between p.273 and l-7','',p273_point,'omission',
       'A distinct raised point is visible between the reference number and l; it is preserved at that height rather than silently classified as a baseline period.','22')

c_doubts=[]
def doubt(place,c,new,resolved,evidence,crop=None,source=None,bbox=None,confidence='medium'):
    if crop:
        item=loc[crop];source=source or item['source'];bbox=bbox or item['bbox'];crop=item['output']
    c_doubts.append(dict(place=place,c=c,reading=new,resolved=resolved,confidence=confidence,
                         evidence=evidence,crop=crop,source=source,bbox=bbox))

doubt('p234 l.7, high cancelled group',r"\deleted{\unsure{''}}",high_quote,False,
      'The upper cluster is blackened and crossed. Short quote-like legs survive, but the original count/identity cannot be recovered securely; only the raised placement is decided.','03',confidence='low')
doubt('p234 l.-6, cancelled page reference',r'\deleted{p\unsure{23}}',r'\deleted{p23}',True,
      'Surviving numeral contours support 2 then 3 independently of the page reference above.','04')
doubt('p234 l.-6, cancelled false start',r'\deleted{\unsure{if}}',r'\deleted{\unsure{if}}',False,
      'Parallel crossing strokes blacken the interior. The small lower oblique trace does not securely distinguish the proposed letters; if remains a low-confidence conjectural reading.','05',confidence='low')
doubt('p243 l-6, not/nor',r'\unsure{not|nor}','not',True,
      'The final upright and long cross-stroke favour t and exclude the contextual correction to nor.','07',confidence='high')
doubt('p247 first cancelled line reference',r'\unsure{l.14}','l.14',True,
      'The l loop, point, 1 and crossbar/diagonal of 4 are independently distinguishable under the zigzag.','08')
doubt('p247 first cancelled quoted word',r'\unsure{aspheric}',r'\unsure{aspheric}',False,
      'Several lower loops and one long descender survive, but the heavy zigzag obscures enough letters that aspheric cannot be made certain from this occurrence.','08',confidence='low')
doubt('p247 raised mapping, i subscript',r'i_{\unsure{0|i}}','i_0',True,
      'The subscript itself is a closed oval, distinct from the high dot of the main i.','09',confidence='high')
doubt('p247 cancelled mapping, terminal quotes',r"\unsure{''}","''",True,
      'Two raised tips survive at the right edge; their lower portions lie within the crossing.','10')
doubt('before 255, crossed numeral',r'\unsure{2}','2',True,
      'The original curved top, diagonal and low foot remain visible through the slash.','14')
doubt('262, earlier reference',r'\deleted{\unsure{-13}}',r'-\deleted{\unsure{13|l13}}',False,
      'The leading dash is live; the crossed internal vertical strokes do not exclude a looped l before 13. The uncertainty is narrowed/relocalized rather than resolved.','15',confidence='low')
doubt('262, possible minus before 2',r'\unsure{-}2','2',True,
      'The crop shows no independent minus; the oblique/low trace belongs to the 2 contour.','16',confidence='high')
doubt('263 l.19, final letter after allow',r'allow\unsure{s}',r'allow\unsure{e|s}',False,
      'An oval retraced body and rightward exit favour e, but the compact s alternative remains possible.','17',confidence='low')
doubt('264, high mark before l12',r"\unsure{'}","'",True,
      'A single high upright stroke is independent of the following l loop; no second stroke is present.','18',confidence='high')
doubt('p269, second cancelled group',r'\unsure{not}','not',True,
      'The n, lower o loop, and t upright/crossbar/foot are visible.','20',confidence='high')

# Page-specific contextual alternatives/notation decisions, including separate occurrences.
doubt('C_context: p234 l.7, pair and comma',r'$(A,i)$',r'$(A,i)$',True,
      'The lower comma is separate from A; the following short i has its own high dot.',source=A,bbox=[1288,359,1469,456],confidence='high')
doubt('C_context: p240 l.3, double subscript, inverse and underline',r'$W=(i_{M,i})^{-1}(\underline W)$',r'$W=(i_{M,i})^{-1}(\underline{W})$',True,
      'The subscript comma and dotted second i are visible, as are raised -1 and the line confined to the final W. Braces around W are syntax only.','06',confidence='high')
doubt('C_context: p247 raised abbreviation',r'Cond\textsuperscript{n}',r'Cond\textsuperscript{n}',True,
      'A small raised n stands above and after the final d.','09',confidence='high')
doubt('C_context: p247 raised N companion','N_0',r'N_{\unsure{0|i}}',False,
      'This separate tiny lowered glyph has an open lower cup plus a detached dark upper touch; a broken 0 and dotted i remain possible.','09',confidence='low')
doubt('C_context: p247 cancelled i companion','i_0',r'i_{\unsure{0|i}}',False,
      'The low companion is merged into the cancellation; the clearer raised occurrence does not decide this one.','10',confidence='low')
doubt('C_context: p248 hat',r'\widehat C',r'\widehat C',True,
      'Two small oblique strokes form a roof above a single-contour C.',source=B,bbox=[868,155,909,212],confidence='high')
doubt('C_context: p269 three pi pairs',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,
      'Each of the three occurrences was read separately. The lower zero is oval and the lower one is a short upright; the cancelled second pair is additionally legible in crop 20.','20',source=B,bbox=[474,864,949,982],confidence='high')

remaining=[]
def remain(place,reading,alternatives,reason,crop,confidence='low'):
    item=loc[crop]
    remaining.append(dict(place=place,reading=reading,alternatives=alternatives,
                          confidence=confidence,reason=reason,crop=item['output'],
                          source=item['source'],bbox=item['bbox']))
remain('p234 l.7, cancelled raised group',r"\deleted{\unsure{''}}","'' conjectured; precise original mark/count not recoverable",
       'Crossing/blackening hides the original bodies of the short raised strokes.','03')
remain('p234 l.-6, cancelled false start',r'\deleted{\unsure{if}}','if conjectured',
       'Only small peripheral traces remain below the dense parallel cancellation.','05')
remain('p247 cancelled quoted word',r'\unsure{aspheric}','aspheric conjectured',
       'The zigzag hides several interior letters; repetition elsewhere is not used to restore them.','08')
remain('p247 raised mapping, N subscript',r'N_{\unsure{0|i}}','0 | i',
       'Open lower cup and detached upper touch remain ambiguous at this separate occurrence.','09')
remain('p247 cancelled mapping, i subscript',r'i_{\unsure{0|i}}','0 | i',
       'The low glyph merges into a cancellation diagonal.','10')
remain('p247 cancelled mapping, closing delimiter',r'\unsure{)}',') conjectured',
       'The candidate closing curve cannot be separated securely from the terminal crossing.','10')
remain('262 cancelled old reference',r'\unsure{13|l13}','13 | l13',
       'Multiple old vertical/loop strokes remain under the cross; the preceding live dash is independently clear.','15')
remain('263 l.19, last letter after allow',r'allow\unsure{e|s}','e | s',
       'The small retrace has an e-like loop but permits a compact s.','17')

inventory=[]
def inv(kind,position,first,hand='his hand',transcribed='yes'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=f'{len(inventory)+1:02d}',
                          kind=kind,position=position,first_words_or_objects=first,transcribed=transcribed))
entries=[
('p225, first reference','p225 line 12 delete ``that\'\''),
('p225, second reference',"l.-7 don't"),
('226','226 l.2 ``do not\'\''),
('230',"230 l.-2 'informal''"),
('p232',"p232 l-3 ``inessential''"),
('p233, first reference',"p.233 l.1 ``its''"),
('p233, second reference',"l2 & 3 ``shouldn't''"),
('p233, third reference',"l-2 ``synonym''"),
('p234 l.7',"surely it should be ``Then W is a mildly"),
('p234 l.-6, two written lines','x is aspheric iff u is aspheric; I suppose! A tautology it surely is as it stands!.'),
('p239',"p.239 l.3 ``suggests that we call an ...''"),
('p240, first reference',r'W=(i_{M,i})^{-1}(\underline W)'),
('p240, second reference',"l.10 ``its''"),
('p240, third reference',"l-8 ``doesn't''"),
('p241',"p241 l-15 ``suggested a long time ago''"),
('p242, first reference',"p242 l-12 ``its''"),
('p242, second reference',"l-2 ``its''"),
('p243, two lines','too many negatives: We assume beforehand neither... not.... is one of many possibilities'),
('p244',"p244 l-15 ``doesn't''"),
('p245',"p245. l.4 ``we'll''"),
('p246',"p246 l.2 ``its''"),
('p247, upper live entry',"l-9 ``standard''"),
('p247, lower first entry',"l12 ``is aspheric''"),
('p247, lower word to the right of the curved stroke','also'),
('p247, lower second entry',"l-2 ``didn't''"),
('p248',r'handwritten: such that \widehat C is totally ...'),
('p248, nested underline','handwritten'),
('p248, nested underline','is'),
('p249',"p249 l-2 ``isn't''"),
('p250, first reference',"p.250 l.10 ``developed''"),
('p250, second reference',"l.12 ``its''"),
('p250, third reference',"l.13 ``its''"),
('p251, first reference',"p251 l.9 ``last but not least''"),
('p251, second reference',r'l.15 ``i\colon A\to M\'\'.'),
('255',"255 l16 ``developed''"),
('260',"260 l.13 ``didn't''"),
('262','262, l-3 & 2, may as well'),
('263, first reference',r'263 l.19 ``allow\unsure{e|s} one to\'\''),
('263, second reference',"l20 'wasn't''"),
('263, third reference','l.-13 ``pushing on the.'),
('263, lower first reference',"l-11 ``and was finally''"),
('263, lower second reference',"l.-4 ``developing''"),
('264',"264 'l12 ``developed'' ``length''"),
('p267, first reference',"p267 l.2 ``developed''"),
('p267, second reference',"l-2 ``amounts to it being contractible''"),
('p269, introduction','p.269: middle of page -'),
('p269, live conclusion',r'\pi_0,\pi_1 are undefined here. Notation is confusing.'),
('p269, nested underline','here'),
('p270',"p.270 l.-2 ``we've got''"),
('p273',"p.273 l-7 ``isn't''"),
('p274',"p.274 l-9 ``if I've got''"),
]
for position,first in entries: inv('text',position,first)
inv('deletion','p234 l.7, raised above continuation',r"\deleted{\unsure{''}}")
inv('deletion','p234 l.-6, before line reference',r'\deleted{p23}')
inv('deletion','p234 l.-6, between aspheric and iff',r'\deleted{\unsure{if}}')
inv('deletion','p247 upper left, reference and quoted word',r'\deleted{l.14 ``\unsure{aspheric}\'\'}')
inv('insertion','p247, raised above the cancelled proposal',r'(Cond\textsuperscript{n} (ii) should it be i_0\colon N_{\unsure{0|i}}\to N)')
inv('deletion','p247, upper cancelled proposal',r"\deleted{should it be $(i_{\unsure{0|i}}\colon N\unsure{)}$''}")
inv('deletion','before 255',r'\deleted{2}')
inv('deletion','262, after a live leading dash',r'\deleted{\unsure{13|l13}}')
inv('insertion','p267, caret between to and being','it')
inv('deletion','p269, first question; exclamation remains uncrossed',r"isn't the use of \pi_0,\pi_1 slightly confusing here")
inv('deletion','p269, beginning of the second line',r'not \pi_0,\pi_1')
inv('drawing','left edge of reference column, nearly full height','thin long rule',hand='rule hand not determined')
inv('drawing','right edge of text, nearly full height','thin long rule',hand='rule hand not determined')
inv('drawing','far-left margin, upper portion','faint partial upright trace',hand='trace hand not determined')
inv('drawing','p234 l.7, second continuation group','wavy stroke and two low points')
inv('drawing','p243 l-6, above first continuation group','isolated high point')
inv('drawing','p247, beside also','long bowed downward curve')
inv('drawing','p247, below cancelled mapping','oblique descending tail')
inv('drawing','p263, blank area below/right of pushing on the.','two oblique touches and one point')
inv('drawing','p269, right of the long rule','two points and one short horizontal stroke')
inv('drawing','p273, between page and line references','raised isolated point')
inv('margin note','lower-left archive corner','% archive sheet number: 24',hand='archive numbering hand')

truth_table=[{'P_x':p,'P_u':q,'equivalence':p==q} for p,q in itertools.product([False,True],repeat=2)]
(OUT / 'math_check.json').write_text(json.dumps({'statement':'P(x) iff P(u)','truth_table':truth_table,
    'limit':'P(x) and P(u) were treated as independent propositions; the missing original mathematical context may relate them.'},indent=2)+'\n')

notation=[
dict(sign='ordinary capitals',location='p234, p240, raised p247, p248, p251',reading='W, A, M, N, C',evidence='Single main contours; no independently doubled alphabet is visible in the assigned handwritten page.'),
dict(sign='(A,i)',location='p234 l.7',reading=r'(A,i)',evidence='Low comma and separately dotted i; upper half.'),
dict(sign='double subscript/inverse/underline',location='p240 l.3',reading=r'W=(i_{M,i})^{-1}(\underline{W})',evidence='Crop 06 separates the lowered M, comma and dotted i; -1 is raised and only the final W is underlined.'),
dict(sign='Cond raised n',location='p247 raised note',reading=r'Cond\textsuperscript{n}',evidence='Crop 09 shows the raised small n after d.'),
dict(sign='separate small indices',location='p247 raised and cancelled proposals',reading=r'i_0; N_{\unsure{0|i}}; i_{\unsure{0|i}}',evidence='Crops 09 and 10 were judged separately; a clear closed oval on the first i does not settle the other occurrences.'),
dict(sign='hat',location='p248',reading=r'\widehat C',evidence='Two small oblique strokes form a roof; C has a single contour.'),
dict(sign='three pi pairs',location='p269 first cancelled question, second cancelled group, live sentence',reading=r'\pi_0,\pi_1',evidence='The three pairs separately have lower oval 0 and lower upright 1; crop 20 further separates the second pair.'),
dict(sign='quotation pairs',location='p232 closer; p234 opener before surely; p240 opener; p248 opener; p250 l.13 opener',reading="''; ``; ``; ``; ``",evidence='Crops 01,02,06,11,13 show paired tips/legs, sometimes connected; each occurrence was judged independently and C is confirmed.'),
dict(sign='three continuation marks',location='p248 final group',reading='...',evidence='Crop 12 shows exactly three low marks, the first two elongated and the last short/upright; no closing quote is supplied.'),
dict(sign='single high stroke',location='264 before l12',reading="'",evidence='Crop 18 separates one high upright from the l; its function is left uninterpreted.'),
dict(sign='uncrossed exclamation',location='p269 first cancelled question',reading='!',evidence='Crop 19 shows the cancellation passing through the gap between stem and lower point.'),
]

crop_decisions=[
('01','Confirmed the paired closer after inessential.'),
('02','Confirmed the fused double opener before surely.'),
('03','Retained uncertainty in the crossed raised group; corrected its placement and preserved the low wavy continuation geometry.'),
('04','Resolved cancelled p23.'),
('05','Retained the cancelled if conjecture; confirmed the live variable u from its open upper cup.'),
('06','Confirmed the formula, double subscript, inverse, underline and opening pair.'),
('07','Resolved not; retained three dots after neither and four after not, including the faint point beyond the rule; preserved the separate high point.'),
('08','Resolved l.14; retained aspheric as uncertain beneath the zigzag.'),
('09','Resolved raised i_0; retained a separate 0/i uncertainty on N; confirmed Cond raised n and the rightward arrow.'),
('10','Marked the cancelled i subscript and closing parenthesis doubtful, resolved the terminal pair, and placed also on the lower line with its adjacent curves.'),
('11','Confirmed the paired opener and underline confined to handwritten.'),
('12','Confirmed three low continuation marks and no additional delimiter.'),
('13','Confirmed the paired opener before its; the long lower mark belongs to the i-dot, not another quote.'),
('14','Resolved the crossed digit as 2.'),
('15','Separated the live minus from the cancelled 13/l13 group.'),
('16','Removed the proposed independent minus before 2.'),
('17','Changed the final-letter uncertainty from s alone to e|s.'),
('18','Resolved one high quote-like stroke before l12.'),
('19','Left the final exclamation live because both parts avoid the cancellation.'),
('20','Resolved not; confirmed the independently read second pi pair.'),
('21','Preserved two dots and one lower dash geometrically beyond the right rule.'),
('22','Preserved the raised isolated point after p.273 without assigning a period function.'),
]
(OUT/'crop_inspection_log.json').write_text(json.dumps([
    dict(id=i,displayed=True,display_order=int(i),source=loc[i]['source'],bbox=loc[i]['bbox'],
         crop=loc[i]['output'],decision=d) for i,d in crop_decisions],indent=2)+'\n')

report=dict(
    scan=25,reader='C',model='GPT-6 Astra Pro',effort='not exposed',viewed=[WHOLE,A,B],
    layout='One handwritten correction list, citing pages 225 through 274, on a sheet with archive number 24 at the lower left. There is no title, date or authorial page count. Page references form a loose left column; line references and quoted replacements follow to the right. Most entries take one line; p234, p243, p247, p263 and p269 continue below. The p247 cluster contains broad zigzag deletions, a small raised parenthetical condition/mapping proposal, also on the lower line, a bowed descending curve and an oblique tail. At p267 a caret places it between to and being. The p269 first question and a short second group are separately cancelled. Long left-column and right-side rules remain beside/through the writing; a faint partial trace occurs farther left. Underlining is visible on handwritten and is at p248 and here at p269. Small isolated marks are retained locally. Circular edge punch traces and scan/paper mottling are physical substrate features, not added text or authored pictures. No commutative diagram or separate mathematical display occurs.',
    changes=changes,c_doubts=c_doubts,remaining_doubts=remaining,inventory=inventory,
    notes=[
        'The entries cite p225 through p274. There is no title, date, stated page count or authorial sheet number; the separate lower-left archive number is 24.',
        'At p234 l.7, surely it should be introduces the proposed wording about W and (A,i), with literal continuation marks. At l.-6 the page says x is aspheric iff u is aspheric, followed by I suppose! A tautology it surely is as it stands!. Those qualifications and the final !. are preserved.',
        'At p243 l-6 the author writes too many negatives, gives We assume beforehand neither... not...., and explicitly calls this one of many possibilities. The visible t is not changed to the grammatically expected r.',
        'The raised p247 note asks Condⁿ (ii) should it be and proposes a mapping to N. The shorter should it be proposal below is cancelled. Also is physically on the lower line beside is aspheric.',
        'At p248 l.-3, handwritten and is are separately underlined in such that C-hat is totally, followed by three low continuation marks. The written opening quotation is preserved without supplying a missing closer.',
        'At p251 l.15 the visible map is i: A to M. At p269 the cancelled question calls use of pi_0, pi_1 slightly confusing here!; the live sentence says they are undefined here and the notation is confusing, with here underlined.'
    ],
    math_checks=[dict(statement_id='S025-aspheric-iff-scope',type='targeted proof check',
        outcome='I evaluated the four Boolean assignments for P(x) iff P(u), treating the two as independent predicates. The assignments (true,false) and (false,true) make the equivalence false, so the literal logical form alone is not a tautology. This does not refute the author’s contextual comment: the assigned sheet does not define x, u, aspheric, or a relation that would identify the predicates. No other page was consulted. The word tautology and the variables are transcribed unchanged.')],
    notation=notation,
    abbreviations=[
        dict(form='p',expansion='page (tentative interpretation only)',place='reference column throughout'),
        dict(form='l',expansion='line (tentative interpretation only)',place='line references throughout'),
        dict(form=r'Cond\textsuperscript{n}',expansion='Condition (tentative interpretation only)',place='raised p247 note'),
        dict(form='iff',expansion='if and only if (interpretation only)',place='p234 l.-6')
    ],
    brief_feedback='The whole image and each supplied half were viewed exactly once, in that order. The 22-locus frozen list was written before any enhanced crop; crop.py generated exactly one crop for each locus, and every generated crop was displayed once. Frozen list, generation log and inspection decisions accompany the report. H has desc status, so there are no H comparison rows. Inventory covers every correction entry and nested deletion/insertion/underline, plus the visible rule and mark groups; the archive number is preserved only as a comment. The physical interpretation of the p247 curves is deliberately not elevated to an inferred insertion instruction. Static syntax and literal-diff checks only were used; no OCR, external research, other-page images, other-reader outputs, agents, compilation or installation was used.'
)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),
                  'inventory':len(inventory),'crops':len(crop_decisions),'math_checks':len(report['math_checks'])}))
