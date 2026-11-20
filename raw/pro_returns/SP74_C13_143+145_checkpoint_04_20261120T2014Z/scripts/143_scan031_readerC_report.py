from pathlib import Path
import json

root=Path('/workspace/scratch/8f839dff4bf0')
work=root/'SP74_C13_143+145_work'
p=json.loads((root/'reader_packets/143_scan031.json').read_text())
C=p['witness_C']; H=p['witness_H']
boxes={
 'opening-on-a':[598,290,794,358], 'first-link':[246,409,367,469],
 'aliases-upper':[640,358,1277,532], 'aliases-lower':[640,487,1469,639],
 'equivalence-phrase':[667,831,1368,978], 'first-basepoint':[602,1027,894,1152],
 'first-target':[1004,987,1676,1118], 'quotient-expression':[721,1150,1656,1302],
 'last-operator':[608,1377,1258,1545], 'last-x-exponent':[1263,1397,1673,1536],
 'nb-du':[913,1742,1576,1864], 'nb-deletion':[858,1884,979,1964],
 'nb-equation-punctuation':[993,1833,1463,1968], 'nb-exception':[498,2073,834,2168],
 'question-expression':[704,2197,1233,2361], 'question-options':[1241,2191,1518,2361],
 'final-margin':[1263,2256,1677,2362]
}

diagram=r'''\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]
(5)\quad1 \arrow[r] \& \pi_1(\overline M_{g,\nu}) \arrow[r] \&
\pi_1(N_{g,\nu},\xi) \arrow[rr] \arrow[dr,phantom,"="] \arrow[dd,phantom,"\Vert"] \& \&
\mathfrak S_\nu\times\Gamma \arrow[r] \& 1\\
\& \& \& \pi_1(\overline N_{g,\nu},\Gamma;\unsure{\xi|j}) \arrow[d,phantom,"\Vert"]\\
\& \& \pi_1(M_{g,\nu},\mathfrak S_\nu,\xi) \arrow[r,phantom,"="] \&
\pi_1(\overline M_{g,\nu},\mathfrak S_\nu\times\Gamma)
\end{tikzcd}}'''
question_arg=r'''\begin{tikzpicture}[baseline=(arg.base)]
\node[inner sep=1pt] (arg) {$\bigl(\widehat{\mathcal T}_{g,\nu}\bigr)$};
\draw ([yshift=-1pt]arg.south west) -- ([yshift=-5pt]arg.south west) --
      ([yshift=-5pt]arg.south east) -- ([yshift=-1pt]arg.south east);
\node[anchor=north,inner sep=1pt] at ([yshift=-5pt]arg.south)
      {$\scriptstyle\pi_1(\overline M_{g,\nu})$};
\end{tikzpicture}'''
tex=r'''\scanpage{31}
\mspage{16}
Si on considère le quotient \inserted{$N_{g,\nu}$} de $M_{g,\nu}$ par $\mathfrak S_\nu$ (de sorte que $M_{g,\nu}$ est un rev. de groupe $\mathfrak S_\nu$ de $N_{g,\nu}$) \unsure{on a|\ldots}
'''+diagram+r'''
structure d'extension un peu plus riche que la première ligne de (4). La conjecture \unsure{faite|fait} équivaut \unsure{à|:} la suivante :
\[
\pi_1(N_{\unsure{g\nu|g,\nu}};\xi)\xrightarrow{\sim}\operatorname{Autextlac}\bigl(\pi_1(X_{\unsure{\xi|j}}\setminus\{x_1,\mathbin{-}x_\nu\})\bigr)
\]
ou encore
\[
\Gamma\simeq\operatorname{Autextlac}\bigl(\pi_1(X_{\unsure{\xi|j}}\setminus\{x_1,\mathbin{-}x_\nu\})\bigr)/\widetilde{\mathcal T}_{g,\nu}^{\wedge}
\]
où
\[
\widetilde{\mathcal T}_{g\nu}\simeq\operatorname{Autextlac}^{+}\bigl(\pi_1(X_{\unsure{\xi|j}}^{an}\setminus\{x_1,\mathbin{-}x_\nu\}).
\]

$*$ NB Il faudrait déterminer le groupe des automorphismes \inserted{$G_{g,\nu}$} du topos modulaire géom $\overline M_{g,\nu}$ \deleted{\unsure{est}} ($G_{g,\nu}=\inserted{\operatorname{Im}}\mathfrak S_\nu$ ? \unsure{\deleted{)}|\}} Sans doute $\mathfrak S_\nu$ opère fidèlement sauf $g=0,\nu\leq4$\textendash\,\textemdash)

\uline{Question}
\[
\Gamma\longrightarrow\operatorname{Autext}\,'''+question_arg+r'''
\quad\left\{\begin{array}{l}\text{injectif ?}\\\text{bijectif}\end{array}\right.
\]
\margin{(Sans doute il faut condition \unsure{sur le} \illegible{1}, cf NB.}
\mspage{30}
'''

changes=[]
def add(place,c,h,final,ac,ah,kind,ink,confidence='high',crop='page',marked=False,consequential=False):
    assert c in C, ('C excerpt',place,c)
    assert h=='[no witness]' or h in H, ('H excerpt',place,h)
    assert final in tex, ('final excerpt',place,final)
    changes.append(dict(place=place,C=c,H=h,final=final,against_C=ac,against_H=ah,kind=kind,ink=ink,confidence=confidence,crop='page' if crop=='page' else f'crops/143_scan031_readerC_{crop}.png',box=None if crop=='page' else boxes[crop],marked_in_H=marked,consequential=consequential))

add('Opening paragraph: inserted quotient name',r'\inserted{$N_{g,\nu}$}',r'$N_{g,\nu}$',r'\inserted{$N_{g,\nu}$}',False,True,'insertion or placement','The name stands above the text line in the gap after quotient; its placement is an insertion, not ordinary baseline text.')
add('Opening paragraph: final three small strokes',r') on a',r') \ldots',r') \unsure{on a|\ldots}',False,True,'misread word','Three separate gestures have a small o-like opening, a shallow n-like arc, and a separate oval a-like ending; they are not three uniform points. The reduced forms still admit suspension.', 'medium','opening-on-a')
add('Extension display: formula number at the left',r'\end{tikzcd}}\hfill(5)',r'(5) \qquad 1',r'(5)\quad1',True,False,'insertion or placement','The parenthesized 5 is physically to the left of the initial 1, not at the right end of the extension.')
add('Extension display: first link',r'1 \arrow[r,dash]',r'1 \to',r'1 \arrow[r]',True,False,'drawing or diagram','At the right end of the short first shaft, two oblique return branches form a small triangular endpoint. It favors a headed arrow over a bare shaft.','medium','first-link',consequential=True)
cstack=C[C.index(r'\begin{gathered}'):C.index(r'\end{gathered}')+len(r'\end{gathered}')]
hstack=H[H.index(r'  \pi_1(N_{g,\nu;\xi}) ='):H.index(r'\note{les trois')]
add('Extension display: four middle expressions and equality topology',cstack,hstack,diagram,True,True,'drawing or diagram','Four expressions form two offset columns: the upper-left and upper-right are joined by =, each has a separate vertical pair of equality strokes to the expression below it, and the lower pair are joined by =. C collapses the two columns into one gathered stack; H gives a horizontal equality chain. The two existing alias crops jointly support this arrangement.','high','aliases-upper',consequential=True)
add('Extension display: top middle N-expression punctuation and basepoint level',r'\pi_1(N_{g,\nu};\xi)',r'\pi_1(N_{g,\nu;\xi})',r'\pi_1(N_{g,\nu},\xi)',True,True,'misread symbol or index','The separator before the full-sized basepoint is one low comma with no upper dot. The basepoint stands at the expression baseline outside the N subscript.','high','aliases-upper',consequential=True)
add('Extension display: lower-left M,S,xi separators',r'\pi_1(M_{g,\nu},\mathfrak S_\nu;\xi)',r'\pi_1(M_{g,\nu}; \mathfrak{S}_\nu, \xi)',r'\pi_1(M_{g,\nu},\mathfrak S_\nu,\xi)',True,True,'misread symbol or index','Both separators are single low comma strokes, after the indexed M and after S_nu respectively. The xi is full-sized and has the upper turn and lower loop.','high','aliases-lower',consequential=True)
add('Conjecture prose: faite/fait',r'conjecture faite',r'conjecture fait',r'conjecture \unsure{faite|fait}',False,True,'misread word','After the tall t there is a low finishing stroke, but it does not securely isolate a final e; the C reading is retained first with fait explicit.','low','equivalence-phrase')
add('Conjecture prose: équivaut',r'équivaut',r'équivalent',r'équivaut',False,True,'misread word','After the q descender the sequence has ui/v, a rounded a, u, and a final tall t; there is no separate l/e/n sequence of équivalent.','high','equivalence-phrase')
add('Conjecture prose: à or colon',r'à la suivante',r': la suivante',r'\unsure{à|:} la suivante',False,True,'misread word','The two stacked small marks include a curved lower oval that favors a reduced accented a, but two-point punctuation cannot be excluded.','medium','equivalence-phrase')
add('First conjecture display: N index and basepoint placement',r'\pi_1(N_{g,\nu};\xi)',r'\pi_1(N_{g,\nu;\xi})',r'\pi_1(N_{\unsure{g\nu|g,\nu}};\xi)',True,True,'misread symbol or index','The g descender and nu form a joined run without a securely separable comma. After the subscript there is a semicolon-like upper part and lower comma, followed by a full-sized basepoint outside the N index. The uncertain subscript punctuation is kept distinct from the secure basepoint level.','medium','first-basepoint',consequential=True)
add('First conjecture display: Autextlac baseline',r'\operatorname{Autextlac}',r'\mathrm{Autext}_{\mathrm{lac}}',r'\operatorname{Autextlac}',False,True,'misread symbol or index','The small letters lac continue on the same writing line as Autext; they do not descend to a subscript line.','high','first-target')
add('First conjecture display: puncture-list continuation',r'\{x_1,\ldots,x_\nu\}',r'\{x_1, \ldots, x_\nu\}',r'\{x_1,\mathbin{-}x_\nu\}',True,True,'misread symbol or index','After the comma following x_1 there is one continuous horizontal stroke, followed by x_nu. Three separate dots and a separate comma before x_nu are not present. The minus macro records the stroke only, not an arithmetic interpretation.','high','first-target')
add('Connector between first and second conjecture displays',r'ou encore',r'on en tire',r'ou encore',False,True,'misread word','The opening is ou, followed by the compact e-n-c-o-r-e sequence; the half shows the rounded c/o run rather than tire.')
add('Second conjecture display: Autextlac baseline',r'\operatorname{Autextlac}',r'\mathrm{Autext}_{\mathrm{lac}}',r'\operatorname{Autextlac}',False,True,'misread symbol or index','Here too lac is written directly along the Autext baseline, with no downward displacement.','high','quotient-expression')
add('Second conjecture display: puncture-list continuation',r'\{x_1,\ldots,x_\nu\}',r'\{x_1, \ldots, x_\nu\}',r'\{x_1,\mathbin{-}x_\nu\}',True,True,'misread symbol or index','The continuation consists of a single nearly straight horizontal stroke. There is a comma after x_1, but no independently written comma before the final x_nu.','high','quotient-expression')
add('Second conjecture display: completion wedge position',r'\widetilde{\mathcal T}_{g,\nu}^{\wedge}',r'\widehat{\widetilde{\mathcal{T}}}_{g,\nu}',r'\widetilde{\mathcal T}_{g,\nu}^{\wedge}',False,True,'misread symbol or index','The tilde is above T, while a separate wedge stands at its upper right beyond the indexed expression. It is not a second centered hat above the tilde. The comma between g and nu is distinct here.','high','quotient-expression',consequential=True)
add('Third conjecture display: tilde-T subscript',r'\widetilde{\mathcal T}_{g,\nu}\simeq',r'\widetilde{\mathcal{T}}_{g,\nu} \simeq',r'\widetilde{\mathcal T}_{g\nu}\simeq',True,True,'misread symbol or index','There is a white gap between the g and nu with no comma stroke. It differs from the visible comma in the preceding denominator.','high','last-operator',consequential=True)
add('Third conjecture display: Autextlac baseline',r'\operatorname{Autextlac}^{+}',r'\mathrm{Autext}_{\mathrm{lac}}^{+}',r'\operatorname{Autextlac}^{+}',False,True,'misread symbol or index','The lac letters again sit on the operator baseline. The separate plus has an upright crossing its bar and is retained as a superscript.','high','last-operator')
add('Third conjecture display: X exponent',r'^{\unsure{an|top}}',r'^{\mathrm{top}}',r'^{an}',False,True,'misread symbol or index','Two small gestures occupy the exponent line: a compact round a-like mark and a low n-like arc. No tall t or descending p is recoverable.','medium','last-x-exponent',marked=True,consequential=True)
add('Third conjecture display: puncture-list continuation',r'\{x_1,\ldots,x_\nu\}',r'\{x_1, \ldots, x_\nu\}',r'\{x_1,\mathbin{-}x_\nu\}',True,True,'misread symbol or index','A single longer, slightly wavy continuation stroke runs toward the last x. There are no three discrete dots and no separate second comma.','high','last-x-exponent')
add('Third conjecture display: right-parenthesis count',r'\})\bigr).',r'\})\bigr).',r'\}).',True,True,'text not on the page','After the closing set brace there is one right-parenthesis curve followed by a period. The second closing parenthesis supplied by both witnesses has no separate stroke. Two opening parentheses remain in the transcription.','high','last-x-exponent',consequential=True)
add('NB: inserted automorphism-group name',r'\inserted{$G_{g,\nu}$}',r'$G_{g,\nu}$',r'\inserted{$G_{g,\nu}$}',False,True,'insertion or placement','The G label is written above the line with a curved attachment stroke leading into the gap before du; its g, comma, nu indices are distinguishable.','high','nb-du')
add('NB: du and absence of an opening parenthesis before it',r'du topos',r'(des topos',r'du topos',False,True,'misread word','The first letter has a d bowl and tall stem, followed by u. The larger arc nearby belongs to the inserted G attachment, not an opening text parenthesis.','high','nb-du')
add('NB: singular modulaire',r'modulaire',r'modulaires',r'modulaire',False,True,'misread word','The written sequence ends in a low e return; no independent final s follows it.','medium','nb-du')
add('NB: abbreviation géom without a point',r'géom $',r'géom.\ $',r'géom $',False,True,'abbreviation expanded or spelling modernised','The word ends after its m. The white gap before the barred M has no terminal ink point.')
add('NB: canceled word after barred M',r'\deleted{\unsure{est}}',r'\struck{\ill{}}',r'\deleted{\unsure{est}}',False,True,r'readable ink left as \ill{}','Strong horizontal and diagonal cancellation strokes cover the word. A final tall t-like stem and earlier low fragments permit est provisionally, but the whole reading is not secure.','low','nb-deletion',marked=True)
add('NB: H closing parenthesis after canceled word',r'\deleted{\unsure{est}} (',r'\struck{\ill{}}) (',r'\deleted{\unsure{est}} (',False,True,'text not on the page','The cancellation is followed by the new opening parenthesis of the G equation; no independent closing parenthesis lies between them.','high','nb-deletion')
add('NB equation: Im insertion',r'\inserted{\operatorname{Im}}',r'\mathrm{Im}',r'\inserted{\operatorname{Im}}',False,True,'insertion or placement','Im is placed above the S_nu term and has its own curved left attachment. This is a correction above the line, not ordinary baseline text.','high','nb-equation-punctuation')
add('NB equation: crossed closing punctuation',r'\unsure{\}}',r'?)',r'\unsure{\deleted{)}|\}}',True,True,'deletion state','Beyond the question mark, multiple loops cross a long closing curve. A canceled right parenthesis is the leading reading; an overwritten brace-like sign remains possible. The alternative records both uncertain glyph and state.','low','nb-equation-punctuation')
add('NB: Sans doute',r'Sans doute', 'sauf\n\\ill{}',r'Sans doute',False,True,'misread word','The word Sans begins with a broad S and ends in the ns run; doute continues on the next line with the d ascender and final te. H replaces the first word with sauf and leaves the next unread.',marked=True)
add('NB: opère',r'opère',r'\uncertain{pour}',r'opère',False,True,'misread word','An opening round o precedes a p with a long descender; the following accented e, r and final e are visible. The sequence is opère, not pour.',marked=True)
add('NB: sauf before the exception',r'sauf',r'fidèlement \ill{}',r'sauf',False,True,r'readable ink left as \ill{}','The s-a-u run ends in a tall f before the following g=0, so the conjunction can be read rather than left as an unread word.','high','nb-exception',marked=True)
add('NB exception: suspension strokes',r'\ldots)',r'\ldots)',r'\textendash\,\textemdash)',True,True,'misread symbol or index','After the 4 there are two horizontal marks, first shorter and then longer and slightly wavy, before the final parenthesis. They are reproduced as two strokes rather than three dots.','high','nb-exception')
add('Question display: underbracket scope and shape',r'\left(\underbrace{\widehat{\mathcal T}_{g,\nu}}_{\pi_1(\overline M_{g,\nu})}\right)',r'\bigl(\underbrace{\widehat{\mathcal{T}}_{g,\nu}}_{\pi_1(\overline{M}_{g,\nu})}\bigr)',question_arg,True,True,'drawing or diagram','The straight bracket with upturned ends extends from before the opening parenthesis to after the closing parenthesis. Its pi_1 label is below the entire parenthesized argument, not just below T. The bracket is reproduced in TikZ.','high','question-expression',consequential=True)
add('Question options: question-mark placement and open right side',r'\left\{\begin{array}{l}\text{injectif ?}\\\text{bijectif}\end{array}\right.',r'\left\{\begin{array}{l} \text{injectif} \\ \text{bijectif} \end{array}\right\} ?',r'\left\{\begin{array}{l}\text{injectif ?}\\\text{bijectif}\end{array}\right.',False,True,'drawing or diagram','A question mark sits beside injectif on its row. The long descending curve near bijectif belongs to its final f and adjoining ink, not an independent right curly brace. Only the left brace is supplied.','high','question-options',consequential=True)
add('Bottom marginal note: no ajouter phrase between il faut and condition',r'\unsure{il faut} \unsure{condition}',r'il faut ajouter \ill{} condition',r'il faut condition',False,True,'text not on the page','The readable il faut is immediately followed by condition across the large descending letter stroke. There is no additional written ajouter or intervening word group in that gap.','high','final-margin',marked=True)
add('Bottom marginal note: sur le',r'\unsure{sur le}',r'condition \ill{},',r'\unsure{sur le}',False,True,r'readable ink left as \ill{}','The bottom line begins with a low s/u/r-like run and a short l/e group. The image edge cuts the lower strokes, so sur le remains tentative.','medium','final-margin',marked=True)
add('Bottom marginal note: partially readable final reference',r'\illegible{2}',r'\ill{}, cf.\ NB.',r'\illegible{1}, cf NB.',True,True,r'readable ink left as \ill{}','An unread short group meets the bottom edge, followed by a comma and a c/f-like reference with N and B and a final point. No separate point after cf is recoverable. The unknown group remains explicit; the H wording is not used to complete it.','medium','final-margin',marked=True)
add('Bottom marginal note: no closing parenthesis visible',r'\illegible{2}}',r'NB.)',r'cf NB.}',False,True,'text not on the page','The final visible point is followed by the right image boundary; no closing parenthesis is recoverable. The opening parenthesis remains unmatched.','high','final-margin')
add('Bottom-left pencil numeral',r'\mspage{30}','[no witness]',r'\mspage{30}',False,True,'omission','A light pencil 30 is written separately at the lower left. Its hand is not identified from this page.')

# Original packet MARKS only, in original order.
def decision(mid,choice,reading,ink,confidence,crop):
 return dict(id=mid,decision=choice,reading=reading,ink=ink,crop=f'crops/143_scan031_readerC_{crop}.png',box=boxes[crop],confidence=confidence)
decisions=[
 decision('M0738','undecided',r'\unsure{\xi|j}','The small basepoint is a long j-like curve without reliably isolated upper lobes. Full-sized xi examples in the diagram support xi as the first reading but do not settle this reduced shape.','medium','aliases-upper'),
 decision('M0739','undecided',r'\unsure{\xi|j}','The subscript below X is nearly a single long stem with a tiny upper shoulder. The page-wide xi comparison favors xi, but the local reduced form also admits j.','medium','first-target'),
 decision('M0740','undecided',r'\unsure{\xi|j}','The descending subscript curve partly meets the lower X stroke. There is insufficient independent upper articulation to exclude j.','medium','quotient-expression'),
 decision('M0741','undecided',r'\unsure{\xi|j}','The reduced glyph has an S-like curve and upper turn but no separate dot; the upper structure remains too compressed to decide xi versus j on ink alone.','medium','last-x-exponent'),
 decision('M0742','first','an','The exponent consists of a compact round a-like mark followed by a low n-like arc. No t ascender or p descender supports top.','medium','last-x-exponent'),
 decision('M0743','undecided',r'\unsure{\deleted{)}|\}}','Several crossing loops overlie a long closing curve after the question mark. Canceled right parenthesis is preferred, but a brace-like overwritten sign remains possible.','low','nb-equation-punctuation'),
 decision('M0744','first','il faut','The short dotted i, l upright and separate f-a-u-t run are readable in the left part of the margin, below the question options.','high','final-margin'),
 decision('M0745','first','condition','The c-o-n-d opening, tall d, and following i-t-i-o-n run can be followed across the middle of the note despite crossing descenders.','high','final-margin'),
 decision('M0746','undecided',r'\unsure{sur le}','The low opening run and following l/e-like group favor sur le, but their feet are cut by the image edge.','medium','final-margin'),
 decision('M0747','other',r'\illegible{1}, cf NB.','The lower-edge group remains unread. A comma and cf NB. are recoverable at its right; the point after cf and a final closing parenthesis supplied by H are not visible.','medium','final-margin')
]

inventory=[]
def inv(element,kind,position,first,hand='his hand'):
 inventory.append(dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('E01','margin note','top right','16','unnamed hand (pencil)')
inv('E02','text','top paragraph','Si on considère le quotient')
inv('E03','insertion','above opening quotient gap',r'N_{g,\nu}')
inv('E04','diagram','upper third, including left formula label','(5) 1 → π₁(bar M) → middle four-expression arrangement → Sν×Γ → 1')
inv('E05','text','below diagram','structure d’extension un peu plus riche')
inv('E06','display','upper-middle','π₁(N;ξ) → Autextlac(π₁(X…))')
inv('E07','text','between first two conjecture displays','ou encore')
inv('E08','display','middle','Γ ≃ Autextlac(π₁(X…))/tilde-T with upper-right wedge')
inv('E09','text','before third conjecture display','où')
inv('E10','display','below middle','tilde-T_gν ≃ Autextlac⁺(π₁(X^an…); only one closing parenthesis')
inv('E11','text','lower third, lighter ink','* NB Il faudrait déterminer le groupe des automorphismes')
inv('E12','insertion','above NB before du topos',r'G_{g,\nu}')
inv('E13','deletion','NB after barred M','est (uncertain underlying word)')
inv('E14','insertion','above NB S_nu term','Im')
inv('E15','deletion','NB immediately after question mark','crossed closing punctuation; canceled ) preferred, alternative brace retained')
inv('E16','text','lower left heading','Question (underlined)')
inv('E17','diagram','bottom display','Γ → Autext(parenthesized hat-T), straight underbracket and two question options')
inv('E18','margin note','bottom right, reaches image edges','(Sans doute il faut condition sur le …, cf NB.')
inv('E19','margin note','bottom left','30','unnamed hand (pencil)')

remaining=[
 dict(place='Opening paragraph ending',reading=r'\unsure{on a|\ldots}',alternatives='on a / suspension points',confidence='medium',reason='The three distinct pen gestures favor reduced words, but remain small enough to admit suspension.'),
 dict(place='Conjecture prose, past participle',reading=r'\unsure{faite|fait}',alternatives='faite / fait',confidence='low',reason='The final low return after t does not isolate e securely.'),
 dict(place='Conjecture prose before la suivante',reading=r'\unsure{à|:}',alternatives='accented a / colon',confidence='medium',reason='The lower mark is curved but very reduced; both constructions remain on the ink.'),
 dict(place='First conjecture display, N subscript',reading=r'N_{\unsure{g\nu|g,\nu}}',alternatives='gν without comma / g,ν',confidence='medium',reason='The joined g-to-nu run does not expose a separate comma.'),
 dict(place='Extension upper-right basepoint M0738',reading=r'\unsure{\xi|j}',alternatives='ξ / j',confidence='medium',reason='Long reduced curve lacks the distinct lobes of the full-sized xi elsewhere on this page.'),
 dict(place='First display X subscript M0739',reading=r'\unsure{\xi|j}',alternatives='ξ / j',confidence='medium',reason='One long stem and upper shoulder do not uniquely name the reduced letter.'),
 dict(place='Second display X subscript M0740',reading=r'\unsure{\xi|j}',alternatives='ξ / j',confidence='medium',reason='The small descending curve partly merges with the X stroke.'),
 dict(place='Third display X subscript M0741',reading=r'\unsure{\xi|j}',alternatives='ξ / j',confidence='medium',reason='The tiny S-like curve remains consistent with both forms.'),
 dict(place='Canceled NB word (not an original MARK)',reading=r'\deleted{\unsure{est}}',alternatives='est / unread canceled word',confidence='low',reason='Cancellation hides the early letters; only the tall final stem and low fragments survive.'),
 dict(place='NB closing punctuation M0743',reading=r'\unsure{\deleted{)}|\}}',alternatives='canceled right parenthesis / overwritten brace-like sign',confidence='low',reason='Crossing loops obscure the underlying closing curve and exact deletion state.'),
 dict(place='Final margin M0746',reading=r'\unsure{sur le}',alternatives='sur le / incompletely recoverable short words',confidence='medium',reason='Lower letter strokes meet the cropped image edge.'),
 dict(place='Final margin M0747, group before cf NB.',reading=r'\illegible{1}',alternatives='unread short group; no completion proposed',confidence='low',reason='Its lower strokes leave the photographed field; no full lexical reading is recoverable.'),
]
certainty=[
 dict(place='Third display exponent M0742',C=r'\unsure{an|top}',final='an',ink='The crop shows a round first gesture and low n-like second gesture, without t or p strokes.'),
 dict(place='Final margin M0744',C=r'\unsure{il faut}',final='il faut',ink='The dotted short i, l and f-a-u-t sequence are separable at the enlarged crop.'),
 dict(place='Final margin M0745',C=r'\unsure{condition}',final='condition',ink='The con/d opening and following ition run remain visible across the middle line.')
]
notation=[
 dict(form=r'\mathcal T, \widetilde{\mathcal T}, \widehat{\mathcal T}',meaning='Retained C encoding of the modular/Teichmüller notation.',evidence='Font rendering alone is not a material difference. The third-display index, tilde, upper-right completion wedge and final centered hat are separately inspected physical features.'),
 dict(form=r'\operatorname{Autextlac}',meaning='Source exterior-automorphism notation with lac written on the baseline.',evidence='All three occurrences have lac aligned with Autext; H subscript placement changes physical notation.'),
 dict(form=r'\mathbin{-}',meaning='Single continuous continuation stroke in each puncture list; no arithmetic-minus interpretation imposed.',evidence='Each of the three lists has one horizontal stroke and lacks a separate comma before final x_nu.'),
 dict(form=r'\textendash\,\textemdash',meaning='Two unequal suspension strokes after the NB exception.',evidence='The crop shows a short horizontal mark and a longer wavy horizontal mark, not three points.'),
 dict(form=r'\unsure{\xi|j}',meaning='Reduced basepoint/index letter, preferred xi but still provisional.',evidence='Full-sized xi instances have clearer two-part curves. The four tiny flagged forms are not settled by expected mathematical role.'),
 dict(form=r'\Vert',meaning='Two short vertical equality strokes between upper and lower middle expressions.',evidence='There is one such pair in each of the two physical columns, not one shared pair.'),
 dict(form='Straight underbracket',meaning='Annotation spanning the complete parenthesized argument of Autext in the Question.',evidence='Both bracket ends extend beyond the parentheses; its pi_1(bar M) label lies beneath the span.')
]
abbreviations=[dict(form='rev.',expansion='revêtement'),dict(form='géom',expansion='géométrique'),dict(form='NB',expansion='nota bene'),dict(form='cf',expansion='confer')]
hand_log=[
 dict(habit='Full-sized xi has more visible lobes than its reduced basepoint and subscript forms, which can resemble j.',places='143_scan031 extension aliases and all three X subscripts',scope='All occurrences on this page inspected; four reduced forms remain unresolved.',misreadings='C marks four xi/j choices; H silently settles them as xi. Neither witness settles the tiny local shapes.'),
 dict(habit='A comma is a low single stroke; a semicolon has an independently raised component.',places='143_scan031 top N alias, lower M/S alias, and first conjecture source group',scope='Separators inspected locally, not standardized across expressions.',misreadings='C supplies semicolons in two diagram positions; H also nests the top basepoint in the N index and changes the lower first comma.'),
 dict(habit='Small lac letters stay on the operator baseline.',places='143_scan031 three conjecture displays',scope='All three occurrences inspected in crops.',misreadings='H sets lac as a subscript in all three.'),
 dict(habit='Continuation is sometimes drawn as a continuous stroke rather than separated points.',places='143_scan031 three puncture lists and NB exception ending',scope='Three single list strokes and two NB suspension strokes are separately observed.',misreadings='C and H normalize these to ellipses, and insert a second list comma.'),
 dict(habit='Comma omission in small genus/marking indices is local.',places='143_scan031 denominator, third tilde-T index, first conjecture N index',scope='The denominator comma is visible; third tilde-T has no comma; first N index remains doubtful.',misreadings='Both witnesses regularize all three to g,nu.'),
 dict(habit='Curved insertion attachment strokes can resemble parentheses.',places='143_scan031 inserted G and Im in the NB',scope='Both corrections inspected; the separate crossed closing punctuation remains doubtful.',misreadings='H introduces a parenthesis before des and ordinary baseline Im.'),
 dict(habit='A long final f descender can look like a closing brace near neighboring lines.',places='143_scan031 bijectif and bottom margin',scope='The final question options are inspected as a whole.',misreadings='H supplies a right brace and shared question mark; the curve belongs to the f while the visible mark sits beside injectif.'),
 dict(habit='Reduced accented a can resemble two punctuation points.',places='143_scan031 équivaut à la suivante',scope='This one occurrence remains an explicit alternative.',misreadings='C reads à; H reads colon.'),
 dict(habit='Lighter ink alone does not establish a new hand.',places='143_scan031 NB and final Question',scope='Source handwriting retained as his hand; pencil numerals remain unnamed.',misreadings='H editorial ink note is not transcribed as source prose.')
]
notes=[
 dict(id='143_scan031-N1',text='The page considers the quotient N of M by the symmetric group and writes extension (5). The four forms of the middle fundamental group occupy two offset columns with two separate vertical equalities. The following sentence calls this extension structure a little richer than the first line of (4). These are accounts of the source, not proved claims.'),
 dict(id='143_scan031-N2',text='The author says the earlier conjecture is equivalent to the following displayed comparison with Autextlac and then gives an alternative Gamma quotient expression. The exact prose retains « faite|fait » and « à|: » as visible doubts. The completion wedge in the quotient is an upper-right exponent, not a second hat over T.'),
 dict(id='143_scan031-N3',text='Each puncture set uses one continuous horizontal continuation stroke after the first comma, without a second comma before the last x. The minus macro reproduces the stroke and makes no arithmetic claim. Both witnesses regularize these strokes as ellipses.'),
 dict(id='143_scan031-N4',text='In the third display the tilde-T subscript is written gν without a comma, the X exponent favors an, and only one closing parenthesis follows the set brace before the period. These physical peculiarities are kept without completing the mathematical expression. The four tiny ξ/j forms remain provisional despite the preferred basepoint interpretation.'),
 dict(id='143_scan031-N5',text='The lighter-ink NB asks to determine the automorphism group G of the geometric modular topos and tentatively writes G=Im Sν. It continues « Sans doute » with a faithfulness assertion qualified by g=0, ν≤4 and two suspension strokes. The canceled word after barred M and the crossed closing punctuation remain uncertain. This is the author’s tentative discussion, not a verified theorem.'),
 dict(id='143_scan031-N6',text='The final Question displays the map from Gamma to Autext of the hatted T and places a straight bracket under the whole parenthesized argument with pi_1(bar M) beneath it. A left brace introduces injectif ? and bijectif. The lower-right note visibly reads « (Sans doute il faut condition », then tentative « sur le », an unread short group, and « cf NB. ». Its lower and right edges are clipped; H’s ajouter and final closing parenthesis are not supplied.'),
 dict(id='143_scan031-N7',text='The page has a top pencil 16 and a bottom-left pencil 30, each transcribed as a numeral but assigned to an unnamed hand. The NB and Question use lighter ink, which does not by itself establish a different writer. No watermark or pale background mark has been promoted to source text.')
]
checks=[
 dict(statement_id='143_scan031-N1',type='carried as background without fault found',outcome='Compared the stated quotient and extension with the visible objects, arrowheads, labels, equality strokes and local punctuation. No exactness or quotient theorem was proved.'),
 dict(statement_id='143_scan031-N2',type='carried as background without fault found',outcome='Checked the visible three formulas and their connecting words against both witnesses, including indices, lac baseline, completion accents, plus, list strokes and closing parentheses. The conjectural equivalence was not independently proved.'),
 dict(statement_id='143_scan031-N5',type='carried as background without fault found',outcome='Read the NB’s tentative group equality, insertions, cancellation and stated exceptional parameters as source claims. No computation or proof of faithfulness was performed.'),
 dict(statement_id='143_scan031-N6',type='carried as background without fault found',outcome='Checked the final map, bracket scope, annotation and questions from the image. Injectivity and bijectivity were not answered or assumed to complete the clipped note.')
]

report=dict(key='143_scan031',reader='C',stage='first',image_views=['original','half1','half2'],changes=changes,decisions=decisions,inventory=inventory,remaining_doubts=remaining,certainty_resolutions=certainty,notation=notation,abbreviations=abbreviations,hand_log=hand_log,notes=notes,check_events=checks,unresolved_for_main=[
 'Opening on a versus suspension: crops/143_scan031_readerC_opening-on-a.png.',
 'Conjecture faite/fait and à/colon: crops/143_scan031_readerC_equivalence-phrase.png.',
 'First conjecture N index may omit its comma: crops/143_scan031_readerC_first-basepoint.png.',
 'Four reduced ξ/j shapes remain: aliases-upper, first-target, quotient-expression and last-x-exponent crops.',
 'Canceled est remains tentative; the crossed closing sign prefers canceled ) but may be brace-like: nb-deletion and nb-equation-punctuation crops.',
 'Bottom margin retains uncertain sur le and an unread short group; no hidden wording supplied: crops/143_scan031_readerC_final-margin.png.',
 'The two-column diagram with both vertical equalities, the three single list strokes, two NB suspension strokes, and single final formula close are preserved for source-faithful adjudication, not corrected mathematically.'
],raw_difference_disposition='All 38 packet differences were inspected against the original once, both native halves once, and 17 unique crops (one per unresolved locus). D01–02 are editorial scan/page wrappers; the source pencil numerals are inventoried separately. D03 is opening on a/suspension. D04–07 and D09–13 concern the actual label position, headed link, two-column equality topology and punctuation; macro layout syntax and H editorial description are excluded. D08,16,19,22 are the retained ξ/j certainty alternatives, with original-MARK decisions. D14 is split into faite/fait, équivaut and à/colon rows. D15,18,21 are the physical lac baseline differences. D17 is ou encore. D20 is the upper-right wedge. D23–24 are the an/top decision and H editorial note (note excluded). D25–28 are du/no opening parenthesis, singular modulaire, point after géom, canceled-word reading and absent H closing parenthesis. D29 is H thin-space macro punctuation, not a written comma; Im insertion is independently recorded. D30–32 are crossed closing punctuation, Sans doute, opère and sauf. D33 is equivalent leq/leqslant macro rendering, with the visible lower bar retained. D34 is an editorial ink note, excluded from source. D35–36 concern the question-mark row and absence of a right brace. D37 is the absent ajouter phrase. D38 is the clipped marginal reading, visible cf NB. and bottom numeral. Additional agreement errors are recorded for all three continuation strokes, local index omission, third-display parenthesis count and underbracket scope. Pure alphabet/font encodings and setminus/smallsetminus are not material rows.')

assert [d['id'] for d in decisions]==[m['id'] for m in p['marks']]
assert all(d['reading'] in tex for d in decisions)
assert len(boxes)==17
for name in boxes:
 assert (work/'crops'/f'143_scan031_readerC_{name}.png').is_file()
for f in ['key','reader','stage','image_views','changes','decisions','inventory','remaining_doubts','certainty_resolutions','notation','abbreviations','hand_log','notes','check_events','unresolved_for_main','raw_difference_disposition']:
 assert f in report
(work/'reviews/143_scan031_readerC.tex').write_text(tex)
(work/'reviews/143_scan031_readerC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'candidate':str(work/'reviews/143_scan031_readerC.tex'),'report':str(work/'reviews/143_scan031_readerC.json'),'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),'crops':len(boxes),'remaining_doubts':len(remaining)},ensure_ascii=False,indent=2))
