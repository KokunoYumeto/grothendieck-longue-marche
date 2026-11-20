import json
from pathlib import Path

base = Path('/workspace/scratch/98070f078628')
out = base / 'SP116_CW_75_work/readers/scan008'
boxes = json.loads((out / 'crop_boxes.json').read_text())
proposal = (base / 'packets/scan008/C.tex').read_text()
replacements = {
    r'\unsure{tte|les|toute}': 'tte',
    r'\unsure{\omega|w}': r'\omega',
    r'\unsure{arc|ar}': 'arc',
    r'\unsure{donc|alors}': 'donc',
    r'\unsure{\operatorname{or}|{\rm Or}}': r'\operatorname{or}',
    r'\unsure{avec|sur}': 'avec',
    r'\unsure{$1^{\circ}$ ou $2^{\circ}\big\}$|$1^{\circ}$ ou $2^{\circ})$}': r'\unsure{$1^{\circ}$ ou $2^{\circ})\big\}$|$1^{\circ}$ ou $2^{\circ}\big\}$}',
    r'\deleted{Se donner un}': r"\deleted{\unsure{Se donner un|La donnée d'un}}",
    r'\unsure{élément|éléments}': 'élément',
    r'\unsure{$^{\times}$|$^{*}$}': r'$^{\times}$',
}
for old, new in replacements.items():
    assert old in proposal, old
    proposal = proposal.replace(old, new)
(out / 'proposal.tex').write_text(proposal)

changes = []
def change(place, crop, c, h, final, evidence, confidence='high', kind='word', against_c=False, against_h=True, marked=False, math_note=''):
    bbox = boxes[crop]
    changes.append(dict(id=f'008-{len(changes)+1:02d}', place=place, c=c, h=h, final=final,
        evidence=f'{evidence} Crop scan008_{crop}.jpg; source J75-01_75_scan008.jpg, original pixel bbox {bbox}.',
        crop=f'crops/scan008_{crop}.jpg', box=bbox, confidence=confidence, kind=kind,
        against_c=against_c, against_h=against_h, marked_in_H=marked, math_note=math_note))

change('opening, Choix pour tte arête', 'tte', r'\unsure{tte|les|toute}', 'toute', 'tte',
       'Two tall t stems precede the small final loop; the intervening round o and u of toute are absent.', kind='uncertainty resolution')
change('opening quotation mark before orientation', 'orientation_quotes', '``', '«', '``',
       'The opening mark consists of two short high parallel strokes, with no paired angular chevrons.', kind='punctuation')
change('closing quotation mark after a', 'orientation_quotes', "''", '»', "''",
       'The closing mark is two high separate ticks rather than two chevrons.', kind='punctuation')
change('overwritten symbol before live sigma(a)', 'origin_deleted', r'\deleted{\unsure{o|\omega}}', '(omitted)', r'\deleted{\unsure{o|\omega}}',
       'The canceled cluster immediately before sigma contains round inner strokes beneath heavier overwriting; the crossing strokes do not distinguish one oval from two lobes.', 'low', 'deletion')
change('slanted marginal map label', 'slanted_margin', r'A\xrightarrow{\substack{\sigma\\\sim}}S', r'A\xrightarrow{\sigma}S', r'A\xrightarrow{\substack{\sigma\\\sim}}S',
       'Above the shaft are a sigma-shaped upper stroke and a separate small wavy stroke; a terminal point is visible at the S end.', kind='symbol')
change('slanted margin, cancellation before (sigma(a),a)', 'slanted_margin', r'\deleted{\unsure{\exists1|\exists}}', '(omitted)', r'\deleted{\unsure{\exists1|\exists}}',
       'A struck existential-shaped group survives before the opening parenthesis; its right-hand upright is crossed and does not settle whether a 1 was present.', 'low', 'deletion')
change('slanted margin, canceled final line', 'slanted_margin', r'\deleted{$\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,$}', '(omitted)', r'\deleted{$\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,$}',
       'The separate lower line is crossed through; the initial variable is obscured, while the later existential, continuous upright 1, a, membership sign and capital A remain discernible.', 'medium', 'deletion')
change('orientation condition, Si', 'si', 'Si', r'\uncertain{Si}', 'Si',
       'A long S-shaped stroke is followed by a short upright with a detached dot, giving Si.', kind='uncertainty resolution', against_h=False, marked=True)
change('orientation condition, existential followed by 1', 'exists_one', r'\exists1', r'\exists!', r'\exists1',
       'The character after the existential is one continuous upright with an entry stroke; there is no detached dot beneath it.', kind='symbol', math_note='The literal numeral 1 is retained; no normalization to an exclamation mark.')
change('orientation condition, stop after s=sigma(a)', 'condition_line_end', r's=\sigma(a).', r's=\sigma(a)', r's=\sigma(a).',
       'A separate dark round stop follows the closing parenthesis at the baseline.', kind='punctuation')
change('connected contour proposition, omega pair', 'omega_pair', r'(\unsure{\omega|w}\text{ et }-\omega)', r'(\omega\text{ et }-\omega)', r'(\omega\text{ et }-\omega)',
       'The first symbol has two rounded lobes and an upward central join; the negative symbol repeats that rounded form rather than a pointed Latin w.', kind='uncertainty resolution', against_h=False)
change('second proposition, du contour', 'du_contour', 'du contour', 'des contours', 'du contour',
       'After the d ascender the next stroke is a shallow u; there is no terminal s there, and contour ends in the short rising r stroke without an additional s.')
change('definition at a vertex, canceled earlier notation', 'deleted_u_and_insert', r'\deleted{\unsure{\omega(s)|w(s)}\unsure{u_{\omega}|u}}', r'\struck{\ill{}}', r'\deleted{\unsure{\omega(s)|w(s)}\unsure{u_{\omega}|u}}',
       'Round strokes with parentheses remain under the first cancellation, and a low u-like stroke under the second; heavy repeated strokes conceal the omega/w distinction and the possible subscript.', 'low', 'deletion', marked=True)
change('definition at a vertex, insertion of sigma inverse', 'sigma_insert', r'\inserted{$\sigma^{-1}(s)$}', r'\struck{\ill{}} $\sigma^{-1}(s)$', r'\inserted{$\sigma^{-1}(s)$}',
       'Sigma with raised minus and continuous 1, followed by (s), is written above arête with a curved insertion guide below; there is no separate canceled word at H’s position before this insertion.', kind='insertion/placement', marked=True)
change('definition at a vertex, canceled comme after qui ait', 'deleted_comme', r'\deleted{\unsure{comme}}', '(omitted here; an illegible cancellation is placed before sigma inverse)', r'\deleted{\unsure{comme}}',
       'A c-shaped opening, rounded middle humps, and terminal e loop lie under a heavy stroke between ait and the live s; the middle letters remain obscured.', 'medium', 'deletion/placement', marked=True)
change('definition at a vertex, no stop after origine', 'origine_stop', 'origine', 'origine.', 'origine',
       'The word ends in its small e loop before the formula bracket; there is no separate baseline stop after the e.', kind='punctuation')
change('definition at an edge, arc de S', 'arc', r"l'unique \unsure{arc|ar} de $S$", r"l'unique arc de $S$", r"l'unique arc de $S$",
       'The word has an a oval, a short r shoulder, and a final c opening to the right.', kind='uncertainty resolution', against_h=False,
       math_note='The following S remains as written; the expected role of A does not authorize changing it. No proof check was used.')
change('automorphism map, canceled letter before A', 'map_and_deleted_RA', r'\deleted{\unsure{R|B}}A', 'A', r'\deleted{\unsure{R|B}}A',
       'An overwritten capital with an upper loop and a lower crossing survives immediately before the live A; the lower ink cannot separate R from B.', 'low', 'deletion')
change('automorphism map, shaft between the ordered pairs', 'map_and_deleted_RA', r'\unsure{-|\to}', r'\to', r'\unsure{-|\to}',
       'The connecting stroke has a straight shaft and a small downturned termination; two distinct arrowhead barbs cannot be resolved.', 'low', 'symbol', math_note='The map interpretation is contextual; it is not substituted for the unresolved terminal ink.')
change('Alors paragraph, autom', 'autom_first', 'autom', 'automorphisme', 'autom',
       'The sequence ends at the m humps, followed by a gap before du; no letters orphisme follow.')
change('left brace beside Alors and On a', 'left_brace', r'\margin{$\big\}$}', '(omitted)', r'\margin{$\big\}$}',
       'A tall curved stroke has an upper bend, a central inward turn and a lower return, forming the margin brace.', kind='margin note')
change('Les autom, absence of stop', 'autom_second', 'autom', 'autom.', 'autom',
       'After the terminal m there is blank space before the following formula; no detached stop occurs.', kind='punctuation')
change('canceled fait que', 'deleted_fait_que', r'\deleted{fait que}', r'\struck{faits que}', r'\deleted{fait que}',
       'The canceled first word has f, a oval, dotted i and t stem; a gap follows t before the q descender of que, with no s stroke.', kind='deletion')
change('order statement, no stop after final n', 'order_line_end', 'est $n$', 'est $n$.', 'est $n$',
       'The final n has its small upturn and then blank paper to the right, without a separate dot.', kind='punctuation')
change('line beginning below order statement', 'first_word_fleche', r'\unsure{flèche|et}', 'Donc', r'\unsure{flèche|et}',
       'The initial tall loop descends below the line, followed by compressed low strokes and an upright; the strokes do not give a separated capital D with o-n-c, but the internal letters of the first candidate are not all distinguishable.', 'low', 'word')
change('comparison of u_omega and u_minus_omega, sss', 'sss', 'sss', 'ssi', 'sss',
       'Three connected long-s-like strokes are visible; the last bends downward and has no detached i dot.')
change('after n greater than or equal to 3, donc', 'donc', r'\unsure{donc|alors}', 'donc', 'donc',
       'A tall looped d is followed by a compressed low rounded tail; there is no initial a followed by a separate l ascender.', kind='uncertainty resolution', against_h=False)
change('orientation operator', 'or_operator', r'\unsure{\operatorname{or}|{\rm Or}}', r'\operatorname{Or}', r'\operatorname{or}',
       'The first oval and following r shoulder are both at lower-case height, below the neighboring S, A and R capitals.', kind='uncertainty resolution')
change('bijection phrase, avec', 'avec', r'\unsure{avec|sur}', 'avec', 'avec',
       'An initial oval a is followed by a rising v and two low terminal curves e-c.', kind='uncertainty resolution', against_h=False)
change('bijection phrase, ens without stop', 'lens', "l'ens", "l'ens.", "l'ens",
       'The final s stroke ends directly before the gap and des; no separate point follows.', kind='punctuation')
change('before g in Aut, no opening set brace', 'g_aut', r'g\in\operatorname{Aut}(S,A,R)', r'\{g\in\operatorname{Aut}(S,A,R)', r'g\in\operatorname{Aut}(S,A,R)',
       'The long returning left stroke joins the oval and descender of the g itself; no detached opening brace is present.', kind='symbol')
change('equivalent-condition reference, ou', 'condition_labels', r'$1^{\circ}$ ou $2^{\circ}$', r'$1^{\circ},2^{\circ}$', r'$1^{\circ}$ ou $2^{\circ}$',
       'Between the two numbered circles are a small round stroke and a joined shallow upturn, the compressed letters ou rather than a lone comma.')
change('equivalent-condition reference, final parenthesis and brace', 'condition_labels', r'\unsure{$1^{\circ}$ ou $2^{\circ}\big\}$|$1^{\circ}$ ou $2^{\circ})$}', r'$1^{\circ},2^{\circ}\}$', r'\unsure{$1^{\circ}$ ou $2^{\circ})\big\}$|$1^{\circ}$ ou $2^{\circ}\big\}$}',
       'A large closing curly brace is visible at the right. A separate small curved stroke below the second degree circle and just left of that brace may be a closing parenthesis; it remains doubtful.', 'low', 'symbol', against_c=True,
       math_note='The visible closing brace is retained even though no opening brace is visible before g. No balancing brace is supplied.')
change('Et le following the condition reference', 'Et', 'Et', 'et', 'Et',
       'The first letter has the tall overwritten vertical and multiple horizontal bars of capital E, followed by a tall t.')
change('gpe cyclique', 'gpe_first', r'\unsure{gpe|grpe}', 'groupe', r'\unsure{gpe|grpe}',
       'The initial g loop, p descender and compressed e are visible, but the joining hump may carry an r; no separate ou sequence is written.', 'medium', 'word')
change('canceled word after est', 'formed_and_le', r'\deleted{\unsure{formé|form}}', r'\struck{\ill{}}', r'\deleted{\unsure{formé|form}}',
       'The f ascender and following round/arched strokes survive under the line; the heavy strike crosses the terminal region, where an accent-like mark survives but the final e is not fully separable.', 'low', 'deletion', marked=True)
change('inserted group name in lower left margin', 'gpe_G0_insert', r'\inserted{gpe $G^{\unsure{0|\circ}}$}', 'groupe $G^0$', r'\inserted{gpe $G^{\unsure{0|\circ}}$}',
       'The added word has a g loop and p descender followed by compressed e, without the expanded rou sequence; the following G has a small raised closed ring. Its position and guide attach it before des autom.', 'medium', 'word',
       math_note='The raised ring remains 0/circle in the first occurrence. The later G^0 follows the first candidate without a repeated mark.')
change('des autom orientés', 'autom_last', 'autom', 'automorphismes', 'autom',
       'The live word stops after the m humps before the next word; no continuation orphismes is written.')
change('interlinear annotation after (S,A,R,omega)', 'parenthesis_insert', r'\inserted{\unsure{lire|les} de $S,A,R;\omega)$}', r'(i.e. de $(S,A,R;\omega)$) before de $(S,A,R,\omega)$', r'\inserted{\unsure{lire|les} de $S,A,R;\omega)$}',
       'The small first word begins with a tall l-like stroke and has compressed low following strokes, without distinct i.e. dots. The remaining line shows de S,A,R;omega and a closing parenthesis, without an opening parenthesis before S. Its guide returns from after the body tuple.', 'low', 'word/placement')
change('canceled line above Torseur', 'deleted_se_donner', r'\deleted{Se donner un}', r"\struck{La donnée d'un}", r"\deleted{\unsure{Se donner un|La donnée d'un}}",
       'The initial tall stroke and small second loop, then a d ascender and rounded/n-humped middle strokes, fit Se donner; the final compact pair fits un without a distinct preceding d-apostrophe. Crossing strokes still conceal individual letters.', 'low', 'deletion')
change('canceled word after ensemble', 'deleted_ou', r'\deleted{\unsure{où}}', '(omitted)', r'\deleted{\unsure{où}}',
       'A heavy canceled round group with short following bumps and a small upper accent-like stroke precedes live à; individual interior strokes remain obscured.', 'low', 'deletion')
change('final line, élément singular', 'elements', r'\unsure{élément|éléments}', 'éléments', 'élément',
       'The word ends with the t stem and crossbar followed by its rightward exit; no extra s is present before muni.', kind='uncertainty resolution')
change('raised cross before circulaire', 'star_circulaire', r'\unsure{$^{\times}$|$^{*}$}', '«', r'$^{\times}$',
       'Two oblique strokes cross at one center and make four tips above the text line; no additional ray or paired chevrons occur.', kind='uncertainty resolution')
change('after circulaire, absence of closing guillemet', 'star_circulaire', 'circulaire.', 'circulaire ».', 'circulaire.',
       'The word is followed by its period and then Se; no paired angle strokes stand between the word and period.', kind='punctuation')

doubts = [
 dict(place='canceled origin notation', reading='o', alternatives=['omega'], confidence='low'),
 dict(place='slanted margin, canceled existential', reading=r'\exists1', alternatives=[r'\exists'], confidence='low'),
 dict(place='slanted margin, canceled quantified variable', reading=r'\forall s\in S', alternatives=[r'\forall a\in S'], confidence='low'),
 dict(place='orientation condition label', reading='O', alternatives=['0'], confidence='medium'),
 dict(place='definition at vertex, first canceled notation', reading=r'\omega(s)', alternatives=['w(s)'], confidence='low'),
 dict(place='definition at vertex, second canceled notation', reading=r'u_{\omega}', alternatives=['u'], confidence='low'),
 dict(place='canceled comme', reading='comme', alternatives=[], confidence='medium'),
 dict(place='arc de S', reading='S', alternatives=[], confidence='high'),
 dict(place='canceled letter before A', reading='R', alternatives=['B'], confidence='low'),
 dict(place='shaft in u_omega:(S,A)...(S,A)', reading='-', alternatives=[r'\to'], confidence='low'),
 dict(place='first word below order statement', reading='flèche', alternatives=['et'], confidence='low'),
 dict(place='condition reference ending', reading=r'$1^{\circ}$ ou $2^{\circ})\big\}$', alternatives=[r'$1^{\circ}$ ou $2^{\circ}\big\}$'], confidence='low'),
 dict(place='abbreviation gpe cyclique and its recurrence in inserted gpe G', reading='gpe', alternatives=['grpe'], confidence='medium'),
 dict(place='canceled formé', reading='formé', alternatives=['form'], confidence='low'),
 dict(place='raised ring on inserted G and later G', reading='0', alternatives=[r'\circ'], confidence='medium'),
 dict(place='first word of interlinear annotation', reading='lire', alternatives=['les'], confidence='low'),
 dict(place='canceled line above Torseur', reading='Se donner un', alternatives=["La donnée d'un"], confidence='low'),
 dict(place='canceled où', reading='où', alternatives=[], confidence='low'),
]

inventory = []
def inv(element, kind, position, first, hand='Grothendieck, blue ink'):
    inventory.append(dict(element=element, kind=kind, position=position, first_words_or_objects=first,
                          sheet_kind='handwritten mathematical notes', hand=hand, transcribed='yes'))
inv('heading', 'text', 'top, y75-125', "Orientation d'un contour.")
inv('opening definition', 'text', 'upper body, y140-280', 'Choix pour tte arête')
inv('canceled origin notation', 'deletion', 'body y201-270 before sigma(a)', r'\unsure{o|\omega}')
inv('slanted margin', 'margin note', 'upper left, x29-304 y104-546, slanted', r'A\to S;\ \forall a\in A')
inv('slanted map', 'diagram', 'within upper left margin', r'A\xrightarrow{\sigma,\sim}S')
inv('margin canceled existential', 'deletion', 'middle marginal line', r'\unsure{\exists1|\exists}')
inv('margin canceled line', 'deletion', 'lowest marginal line', r'\unsure{\forall s\in S|\forall a\in S},\exists1a\in A')
inv('orientation condition', 'display', 'upper body y275-415', r'(\unsure{O|0})\quad Si\ldots s=\sigma(a).')
inv('condition cancellation', 'deletion', 'upper display y267-354', r'R\{s\}=\{a,b\},\text{ alors }\exists')
inv('reduction heading', 'text', 'body y420-455', 'Réduction au cas connexe')
inv('connected proposition', 'text', 'body y468-610', 'Prop Si (S,A,R) est un contour connexe')
inv('two joined oriented arcs', 'drawing', 'left margin x145-379 y488-586', 'two arcs, one vertex, two arrowheads')
inv('canceled Prop', 'deletion', 'body-left x261-382 y635-728', 'Prop')
inv('orientation proposition', 'text', 'body y643-727', 'Prop Soit omega orientation du contour')
inv('vertex sketch', 'drawing', 'left margin x80-263 y635-769', r's,\sigma^{-1}s,u_\omega(s)')
inv('vertex successor definition', 'text', 'body y718-899', r'\forall s\in S,\text{ soit }u_\omega(s)')
inv('canceled vertex notation', 'deletion', 'body x626-897 y718-813', r'\omega(s)\text{ or }w(s),\ u_\omega\text{ or }u')
inv('inserted vertex notation', 'insertion', 'above canceled notation x626-897 y718-813', r'u_\omega')
inv('inserted inverse label', 'insertion', 'above arête x370-495 y787-897', r'\sigma^{-1}(s)')
inv('canceled comme', 'deletion', 'after qui ait x640-801 y832-899', 'comme')
inv('vertex relation', 'display', 'right of definition x1220-1575 y811-935', r'(u_\omega(s),\sigma^{-1}(s))\in R;\ u_\omega(s)\ne s')
inv('edge sketch', 'drawing', 'left margin x53-284 y918-1113', r'\sigma a,a,\sigma u_\omega(a),u_\omega(a)')
inv('edge successor definition', 'text', 'body y910-1100', r"\forall a\in A,\text{ soit }u_\omega(a)\text{ l'unique arc de }S")
inv('edge relation', 'display', 'right/body y990-1115', r'(\sigma u_\omega(a),a)\in R,\ \sigma u_\omega(a)\ne\sigma a;\ u_\omega(a)\ne a')
inv('automorphism conclusions', 'text', 'body y1094-1392', 'Alors u_omega:(S,A) ...')
inv('canceled capital in source pair', 'deletion', 'x397-817 y1094-1188', r'\unsure{R|B}')
inv('margin brace', 'margin note', 'left x238-286 y1143-1274', r'\big\}')
inv('canceled fait que', 'deletion', 'x831-1080 y1286-1392', 'fait que')
inv('first equivalent condition', 'display', 'body y1380-1455', r'1^\circ)\ \forall s\in S,\ s\text{ lié à }gs')
inv('second equivalent condition', 'display', 'body y1455-1525', r'2^\circ)\ \forall a\in A,\ a\text{ lié à }ga')
inv('order statement', 'text', 'body y1525-1620', 'Si n=card S=card A')
inv('orientation bijection and cyclic group', 'text', 'body y1598-2153', r'\unsure{flèche|et}\ u_\omega\ne u_{-\omega}')
inv('canceled formé', 'deletion', 'line end x1513-1658 y1875-2001', r'\unsure{formé|form}')
inv('inserted le', 'insertion', 'above canceled formé x1513-1658 y1875-2001', 'le')
inv('inserted group name', 'insertion', 'lower left margin x197-420 y1945-2061', r'gpe\ G^{\unsure{0|\circ}}')
inv('inserted orientés', 'insertion', 'above autom x582-777 y1941-2050', 'orientés')
inv('interlinear annotation', 'insertion', 'above tuple x963-1308 y1938-2059', r'\unsure{lire|les}\text{ de }S,A,R;\omega)')
inv('canceled abandoned line', 'deletion', 'x425-812 y2160-2250', r"\unsure{Se donner un|La donnée d'un}")
inv('final paragraph', 'text', 'bottom body y2230-2366', r'Torseur sous\ \mathbb Z/n\mathbb Z')
inv('inserted lower bound', 'insertion', 'above final paragraph x883-1069 y2171-2319', r'(n\geq1)')
inv('canceled où', 'deletion', 'x1181-1318 y2221-2312', r'\unsure{où}')
inv('archive sheet number', 'text', 'bottom-left x35-96 y2280-2356; comment only', '7', 'archival pencil hand')

second = []
def sb(name, kind, reading, box=None):
    bb=boxes[name] if box is None else box
    second.append(dict(box=f'b{len(second)+1:02d}', kind=kind, x0=bb[0],y0=bb[1],x1=bb[2],y1=bb[3],reading=reading))
sb('tte','word','tte')
sb('orientation_quotes','punctuation',r"``orientation de $a$''")
sb('origin_deleted','deletion',r'\deleted{\unsure{o|\omega}}\sigma(a)')
sb('slanted_margin','margin note',r'\margin{\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small] A \arrow[r,"{\substack{\sigma\\[-.35ex]\sim}}"] \& S \end{tikzcd}} $\forall a\in A,\ \deleted{\unsure{\exists1|\exists}}(\sigma(a),a)\in R$\\ \deleted{$\unsure{\forall s\in S|\forall a\in S},\exists1\,a\in A,$}}')
sb('label_O','formula',r'\text{Si}\quad \deleted{R\{s\}=\{a,b\},\ \text{alors }\exists}\quad s\in S,\quad \exists1\ a\in R\{s\}\ \text{tel que }s=\sigma(a).\quad(\unsure{O|0})',[270,267,1665,419])
sb('si','word','Si')
sb('deleted_condition','deletion',r'\deleted{R\{s\}=\{a,b\},\ \text{alors }\exists}')
sb('exists_one','number',r'\exists1\ a\in R\{s\}')
sb('condition_line_end','punctuation',r's=\sigma(a).')
sb('omega_pair','formula',r'($\omega$ et $-\omega$)')
sb('drawing1','drawing',r'\figure{\begin{tikzpicture}[x=.02cm,y=.02cm]\draw[->,line width=.6pt] (0,0) .. controls (18,-2) and (39,-2) .. (56,-1);\fill (61,0) circle[radius=1.7];\draw[->,line width=.65pt] (62,0) .. controls (75,5) and (92,15) .. (108,25);\end{tikzpicture}}')
sb('drawing2','drawing',r'\figure{\begin{tikzpicture}[x=.03cm,y=.03cm]\fill (0,0) circle[radius=1.25];\draw[->,line width=.65pt] (0,0)--(54,24);\node[below] at (0,0) {$s$};\node[above] at (21,12) {$\sigma^{-1}s$};\node[below right] at (48,22) {$u_{\omega}(s)$};\end{tikzpicture}}')
sb('deleted_prop','deletion',r'\deleted{Prop}')
sb('du_contour','word','du contour')
sb('deleted_u_and_insert','deletion/insertion',r'$\deleted{\unsure{\omega(s)|w(s)}\unsure{u_{\omega}|u}}\inserted{u_{\omega}}(s)$')
sb('sigma_insert','insertion',r'\inserted{$\sigma^{-1}(s)$}')
sb('deleted_comme','deletion',r'\deleted{\unsure{comme}}')
sb('origine_stop','punctuation','origine')
sb('s_relation','formula',r'\left[\begin{aligned}(u_{\omega}(s),\sigma^{-1}(s))&\in R,\\u_{\omega}(s)&\ne s\end{aligned}\right]')
sb('drawing3','drawing',r'\figure{\begin{tikzpicture}[x=.022cm,y=.022cm]\fill (0,0) circle[radius=1.3];\draw[->,line width=.7pt] (0,0) .. controls (23,3) and (50,15) .. (68,26);\fill (70,28) circle[radius=1.7];\draw[->,line width=.8pt] (71,28) .. controls (82,44) and (89,78) .. (97,91);\node[below] at (2,0) {$\sigma a$};\node[above] at (31,11) {$a$};\node[right] at (68,20) {$\sigma u_{\omega}(a)$};\node[left] at (89,62) {$u_{\omega}(a)$};\end{tikzpicture}}')
sb('arc','word','arc')
sb('arc','formula',r'\left[\begin{aligned}(\sigma u_{\omega}(a),a)&\in R,\quad \sigma u_{\omega}(a)\ne\sigma a\\&\hspace{6em}\text{i.e.}\quad u_{\omega}(a)\ne a\end{aligned}\right]',[665,980,1650,1115])
sb('map_and_deleted_RA','formula',r'u_{\omega}:(S,\deleted{\unsure{R|B}}A)\unsure{-|\to}(S,A)')
sb('autom_first','word','autom')
sb('left_brace','margin note',r'\margin{$\big\}$}')
sb('inverse_identity','number/formula',r'u_{-\omega}=u_{\omega}^{-1}')
sb('autom_second','punctuation','autom')
sb('autom_second','number/formula',r'u_{\omega},u_{\omega}^{-1}',[1300,1184,1665,1285])
sb('deleted_fait_que','deletion',r'\deleted{fait que}')
sb('first_word_fleche','number/formula',r'$1^{\circ})$ $\forall s\in S$, $s$ lié à $gs$',[275,1370,950,1455])
sb('first_word_fleche','number/formula',r'$2^{\circ})$ $\forall a\in A$, $a$ lié à $ga$',[275,1450,950,1525])
sb('order_line_end','number/formula',r"Si $n=\operatorname{card}S=\operatorname{card}A$, l'ordre de $u_{\omega},u_{\omega}^{-1}=u_{-\omega}$ est $n$")
sb('first_word_fleche','word',r'\unsure{flèche|et}')
sb('sss','word','sss')
sb('sss','number/formula',r'$u_{\omega}\ne u_{-\omega}$ sss $n\ne2$ i.e. $n\geq3$',[410,1600,1140,1710])
sb('donc','word','donc')
sb('donc','formula',r'\omega\longmapsto u_{\omega}',[1250,1600,1635,1705])
sb('or_operator','word/formula',r'\operatorname{or}(S,A,R)')
sb('avec','word','avec')
sb('lens','punctuation',"l'ens")
sb('g_aut','formula',r'g\in\operatorname{Aut}(S,A,R)')
sb('condition_labels','number/formula',r'\unsure{$1^{\circ}$ ou $2^{\circ})\big\}$|$1^{\circ}$ ou $2^{\circ}\big\}$}')
sb('Et','word','Et')
sb('gpe_first','word',r'\unsure{gpe|grpe}')
sb('formed_and_le','deletion/insertion',r'\deleted{\unsure{formé|form}} \inserted{le}')
sb('gpe_G0_insert','insertion/number',r'\inserted{gpe $G^{\unsure{0|\circ}}$}')
sb('orientes_insert','insertion',r'\inserted{orientés}')
sb('autom_last','word','autom')
sb('parenthesis_insert','insertion/formula',r'\inserted{\unsure{lire|les} de $S,A,R;\omega)$}')
sb('lower_G0','number/formula',r'G^{0}')
sb('deleted_se_donner','deletion',r"\deleted{\unsure{Se donner un|La donnée d'un}}")
sb('n_ge_1_insert','insertion/number',r'\inserted{$(n\geq1)$}')
sb('deleted_ou','deletion',r'\deleted{\unsure{où}}')
sb('elements','word','élément')
sb('star_circulaire','symbol/punctuation',r'$^{\times}$ circulaire.')
sb('archive7','number','% archive sheet number: 7')

coverage = {
1:'Archive/scan macro difference only; source archive 7 recorded in inventory and comment, not a textual change.',
2:'Crop tte; resolve the abbreviated tte, without expansion to toute.',
3:'Crop orientation_quotes; opening paired ticks retained.',
4:'Crop orientation_quotes; closing paired ticks retained.',
5:'Crop origin_deleted; retain canceled o/omega doubt, omitted by H.',
6:'Crop slanted_margin; full diagram, sigma and tilde, live relation and canceled existential transcribed.',
7:'Alignment artifact between marginal sigma(a) and display label; both read independently; label O/0 retained.',
8:'Crop slanted_margin; canceled quantified final line retained, with initial variable doubt.',
9:'Crop exists_one; literal continuous 1 after existential retained, no exclamation dot.',
10:'Crop condition_line_end retains stop; H marginal text restored at its physical position, no macro-only change.',
11:'Crop label_O; O/0 remains unresolved; H alignment with sigma(a) is not a substitution.',
12:'Display syntax and H editorial note only; marginal separation and slant recorded in inventory/notes.',
13:'Crop omega_pair resolves rounded omega.',
14:'Drawing syntax versus prose description only; first drawing read and reproduced.',
15:'First drawing two arcs and shared point verified on drawing1 crop.',
16:'Second drawing shaft and labels verified on drawing2 crop.',
17:'Drawing coordinate token 0 is not handwritten text; source vertex s retained.',
18:'Drawing syntax/prose span; all three drawing crops inspected, topology and labels retained.',
19:'Drawing coordinates versus H relative placement description only.',
20:'Second/third drawing alignment artifact; both actual sketches retained in their positions.',
21:'H third-drawing a aligned to C second-drawing s; each actual label retained in its own sketch.',
22:'Drawing markup/prose only; sigma u_omega(a) label is present in third drawing.',
23:'Crop du_contour; du contour retained without plural endings.',
24:'Crop deleted_u_and_insert; canceled candidate readings and inserted u_omega retained; H illegibility mark recorded.',
25:'Underline and spacing syntax only; actual extrémité underline retained.',
26:'Crop deleted_comme; cancellation is after qui ait, not at H’s earlier location.',
27:'Crop origine_stop; no separate period after origine.',
28:'Aligned environment only; vertex relation read in full.',
29:'Alignment artifact from multiline relation; no extra u is supplied.',
30:'Aligned environment only; both vertex-relation rows retained.',
31:'Third-drawing syntax and following paragraph alignment only; drawing and edge definition read fully.',
32:'Crop arc resolves final c; literal de S retained.',
33:'Aligned environment only; edge relation read fully.',
34:'Horizontal-spacing macro only.',
35:'Aligned environment only.',
36:'Crop map_and_deleted_RA; canceled R/B retained before live A.',
37:'Crop map_and_deleted_RA; shaft remains minus/arrow uncertain.',
38:'Crop autom_first; five-letter abbreviation autom retained.',
39:'Crop autom_second; no punctuation stop after autom.',
40:'Crop deleted_fait_que; singular fait retained under cancellation.',
41:'Itemize wrapper only; handwritten condition labels reproduced.',
42:'Equivalent degree-symbol macro syntax only; first numeral 1 read.',
43:'Item-label delimiter syntax only.',
44:'Item-label delimiter syntax only.',
45:'Equivalent degree-symbol macro syntax only; second numeral 2 read.',
46:'Item-label delimiter syntax only.',
47:'Itemize wrapper only.',
48:'Crops order_line_end and first_word_fleche; no stop after n; doubtful flèche/et retained instead of Donc.',
49:'Crop sss; three long-s forms retained.',
50:'Crop donc resolves donc.',
51:'Mapsto versus longmapsto representation only; both shaft ends and source/target read in half-page, no symbol insertion.',
52:'Crop or_operator; lowercase or resolved.',
53:'Crop avec resolves avec.',
54:'Crop lens; no stop after ens.',
55:'Crop condition_labels; compressed ou retained between numbered conditions.',
56:'Crop condition_labels; closing brace visible, small preceding parenthesis doubtful; proposal retains both alternatives with brace.',
57:'Crop gpe_first; abbreviation gpe/grpe retained, not expanded.',
58:'Crop formed_and_le; canceled formé/form remains doubtful, H ill mark recorded.',
59:'Crop gpe_G0_insert; inserted abbreviation retained, not expanded.',
60:'Crop gpe_G0_insert; raised closed ring remains 0/circle; doubt carried unmarked to later recurrence.',
61:'Crop autom_last; abbreviation autom retained.',
62:'Crop parenthesis_insert; words and attachment retained as doubtful annotation after tuple, without H’s supplied i.e. or opening parentheses.',
63:'Same annotation crop; lire/les retained doubtful, remaining de S,A,R;omega) read.',
64:'Crop deleted_se_donner; Se donner un/La donnée d’un doubtful under strike; H editorial placement note not source text.',
65:'Crop deleted_ou; canceled où retained doubtful.',
66:'Crop elements; singular élément resolved despite surrounding grammar.',
67:'Crop star_circulaire; raised four-tip cross resolved, not guillemets.',
68:'Crop star_circulaire; no closing guillemet before the period.',
69:'H editorial comment and next heading excluded: not source text on scan008; this sheet ends at contour.'
}
assert set(coverage)==set(range(1,70))

deleted_inserted = [
 'Before sigma(a): crossed earlier o/omega preserved as deletion; final sigma remains live.',
 'Slanted margin: existential group is canceled; adjacent (sigma(a),a) in R remains live.',
 'Slanted margin: entire lowest quantified line is canceled, including its final comma.',
 'Main condition: only R{s}={a,b}, alors exists is canceled; Si and subsequent s in S remain live.',
 'Second proposition: first Prop is canceled and following underlined Prop is live.',
 'Vertex definition: both earlier notation groups are canceled; raised u_omega is inserted; following (s) remains live.',
 'Sigma inverse(s) above arête is an insertion with a guide, not a deleted word.',
 'Canceled comme is after qui ait and before live s comme origine; not before the inverse insertion.',
 'The overwritten R/B before A in the pair is canceled; A remains live.',
 'Fait que is canceled while following conditions équivalentes remains live.',
 'Formé/form is canceled; le is inserted above it and gpe G ring is a separate marginal insertion before des autom.',
 'Orientés is inserted above the line between autom and de.',
 'The annotation lire/les de S,A,R;omega) is above the line and attached after the body tuple by its guide.',
 'The abandoned Se donner un/La donnée d’un line is wholly canceled.',
 '(n>=1) is an interlinear insertion in the final Torseur paragraph.',
 'The overwritten où before live à n is canceled; its interior remains doubtful.'
]

lines = [
 '01 main: Orientation d’un contour.',
 '02 main: Choix pour tte arête a in A d’une double-quoted orientation de a i.e. d’une',
 '03 main: origine [canceled o/omega] sigma(a) de a, de telle façon que l’on ait',
 '04 margin, slanted: A to S with sigma and tilde above the shaft',
 '05 margin, slanted: forall a in A, canceled exists1/exists, (sigma(a),a) in R',
 '06 margin, slanted: canceled forall s/a in S, exists1 a in A,',
 '07 main display: (O/0), Si, canceled R{s}={a,b}, alors exists; s in S, exists1 a in R{s} tel que',
 '08 main display continuation: s=sigma(a).',
 '09 main: Réduction au cas connexe',
 '10 main: underlined Prop Si (S,A,R) est un contour connexe, il a',
 '11 main: exactement underlined deux orientations (omega et -omega).',
 '12 main: canceled Prop, underlined Prop Soit omega orientation du contour (S,A,R).',
 '13 main: forall s in S, soit canceled notation / inserted u_omega(s), l’underlined extrémité de l’unique',
 '14 main with two-row relation at right: arête [inserted sigma inverse(s)] qui ait [canceled comme] s comme origine; (u_omega(s),sigma inverse(s)) in R, u_omega(s) != s',
 '15 main: forall a in A, soit u_omega(a) l’unique arc de S dont l’origine soit',
 '16 main with two-row relation: l’extrémité de a; (sigma u_omega(a),a) in R, sigma u_omega(a) != sigma a; i.e. u_omega(a) != a',
 '17 main: Alors u_omega:(S,[canceled R/B]A) -/arrow (S,A) est un autom du graphe',
 '18 main: (S,A,R). On a u_minusomega=u_omega inverse. Les autom u_omega,u_omega inverse',
 '19 main: sont caractérisés par les [canceled fait que] conditions équivalentes',
 '20 main: 1°) forall s in S, s lié à gs',
 '21 main: 2°) forall a in A, a lié à ga',
 '22 main: Si n=card S=card A, l’ordre de u_omega,u_omega inverse=u_minusomega est n',
 '23 main: flèche/et u_omega != u_minusomega sss n!=2 i.e. n>=3; donc omega mapsto u_omega est',
 '24 main: bijection de or(S,A,R) avec l’ens des g in Aut(S,A,R)',
 '25 main: satisfaisant les conditions équiv. 1° ou 2° [parenthesis doubtful] closing brace, Et le',
 '26 main: gpe/grpe cyclique isomorphic Z/nZ engendré par u_omega est [canceled formé/form] [inserted le]',
 '27 main: [inserted gpe G ring] des autom [inserted orientés] de (S,A,R,omega) [inserted lire/les de S,A,R;omega)]. S et A sont des underlined torseurs',
 '28 main: sous G^0.',
 '29 main: wholly canceled Se donner un/La donnée d’un',
 '30 main: Torseur sous Z/nZ [inserted (n>=1)] = ensemble [canceled où] à n élément muni',
 '31 main: d’un ordre raised cross circulaire. Se donner un contour'
]

record = dict(scan='scan008', line_count=len(lines), changes=changes, doubts=doubts, inventory=inventory,
 second_boxes=second,
 notation=[
  'scan008: literal existential followed by numeral 1, with no detached exclamation dot, in the main condition and marginal cancellation.',
  'scan008: omega has two rounded lobes and a central rise; confirmed in the opposite-orientation pair and subsequent u subscripts.',
  'scan008: lowercase or is written for the orientation operator.',
  'scan008: gpe/grpe is a compressed group abbreviation; uncertainty marked at first occurrence, later inserted recurrence uses gpe.',
  'scan008: the raised ring in G is ambiguous between 0 and circle; first occurrence marked, later G^0 uses first candidate.',
  'scan008: arc de S, sss, singular élément, and the unmatched closing brace are retained literally.',
  'scan008: the elevated cross before circulaire has four tips, transcribed as times; its editorial or mathematical function is not inferred.'
 ],
 hand_habits=[
  'scan008: tte contracts toute into two tall t stems and a small terminal e loop; H expands this abbreviation.',
  'scan008: autom terminates at m without a written stop or expanded orphisme(s), at all three occurrences checked.',
  'scan008: long s strokes in sss can resemble i; the last stroke has no separate dot and bends downward.',
  'scan008: sigma and omega are distinguished by the latter’s two rounded lower lobes; opposite omega pair confirms the shape.',
  'scan008: lower-case o in or is short relative to the neighboring mathematical capitals.',
  'scan008: short abbreviations and interlinear words use flattened joins that can hide r or other internal letters; corresponding doubts retained.',
  'scan008: arrow shafts were read at both ends; the marginal map has a terminal head, while the body map’s small terminal hook remains unresolved.'
 ],
 notes=[
  'Only scan008 packet, its supplied images, RULES/PREAMBLE and current notation were used. No other page packet or global witness was opened.',
  'Whole page and both supplied halves each viewed once; every source word and symbol, including agreements, was compared.',
  '50 bounded original-coordinate crops were generated by autocontrast and LANCZOS enlargement, JPEG quality 94; the slanted margin crop was additionally rotated -55 degrees. Every crop was visually inspected once.',
  'A batch display that returned truncated output did not expose the last three images; they were subsequently displayed individually. No settled place was cropped again.',
  'Line count is 31 reading units: 28 main text/display lines plus 3 slanted marginal lines. Two-row side formulas are grouped with their associated body line; insertions are separately inventoried.',
  'No manuscript page number is visible. The penciled archive sheet number 7 is recorded only as a comment and inventory entry; scan8 and H page7 are wrapper metadata.',
  'All three geometric sketches were compared against the images and H drawing files; C’s topology and labels were retained in TikZ.',
  'A separating rule between the slanted upper-left note and body is a layout stroke, not an extra mathematical symbol.',
  'The terminal S in arc de S is visibly retained; mathematical expectations did not change it.',
  'The closing brace after the numbered-condition reference is visible despite no separate opening brace before g. No opening brace was supplied.',
  'No independent proof check, computation, web lookup, OCR, or TeX compilation was performed. Mathematical consistency was used only to identify ink requiring examination.',
  'H’s editorial notes and its following heading Ensembles à permutation are not source text on this image and are excluded.',
  'Changes include substantive H differences and cropped uncertainty resolutions; pure new/retained doubts and macro-only differences are excluded from substantive change counts.'
 ], check_events=[], deleted_inserted_check=deleted_inserted,
 diff_coverage=[dict(row=i, disposition=coverage[i]) for i in range(1,70)], lines_read=lines)
(out / 'record.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'proposal':str(out/'proposal.tex'),'record':str(out/'record.json'),'changes':len(changes),'doubts':len(doubts),'inventory':len(inventory),'second_boxes':len(second),'diff_rows':len(coverage),'lines':len(lines)},ensure_ascii=False))
