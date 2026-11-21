from pathlib import Path
import csv
import json
import os

root = Path(__file__).resolve().parents[1]
base = root.parent
manifest = json.loads((root / 'scripts/reader_c_059_crop_manifest.json').read_text())
by = {item['file'].split('_', 2)[2].removesuffix('.png'): item for item in manifest}

square = r"""\diagram{\begin{tikzcd}[row sep=large,column sep=large,name=s59square,execute at end picture={
\coordinate (s59ha) at ([xshift=10pt]s59sourcea.east);
\fill ([yshift=6pt]s59ha) circle[radius=.45pt];
\draw[line width=.7pt,line cap=round] ([xshift=-1.5pt,yshift=5.5pt]s59ha)--([xshift=-2.5pt,yshift=5pt]s59ha);
\draw[line width=.7pt,line cap=round] ([xshift=-3pt,yshift=4.3pt]s59ha)--([xshift=-3.4pt,yshift=3.4pt]s59ha);
\draw[line width=.7pt,line cap=round] ([xshift=-3.8pt,yshift=2.7pt]s59ha)--([xshift=-3.7pt,yshift=2pt]s59ha);
\draw[line width=.7pt,line cap=round] ([xshift=-3.2pt,yshift=1.2pt]s59ha)--([xshift=-2.6pt,yshift=.4pt]s59ha);
\coordinate (s59hb) at ([xshift=10pt]s59sourceb.east);
\fill ([yshift=6pt]s59hb) circle[radius=.45pt];
\fill ([xshift=-1.8pt,yshift=6.1pt]s59hb) circle[radius=.5pt];
\fill ([xshift=-3.7pt,yshift=4.7pt]s59hb) circle[radius=.55pt];
\fill ([xshift=-4.8pt,yshift=3.2pt]s59hb) circle[radius=.55pt];
\draw[line width=.8pt,line cap=round] ([xshift=-5pt,yshift=1.3pt]s59hb)--([xshift=-4.2pt,yshift=.3pt]s59hb);
\fill ([yshift=4pt]s59targetd.north) circle[radius=.9pt];
}]
|[alias=s59sourcea]|\Sigma^{<}(2)\arrow[r,"\uline{b'}",start anchor=east,shorten <=10pt]\arrow[d,"p_2"] & \Sigma^{<}(1)\arrow[d,"p_1=\uline{s}",dash,end anchor=north,shorten >=4pt]\\
|[alias=s59sourceb]|\Sigma^{<}(1)\arrow[r,"\uline{b}",start anchor=east,shorten <=10pt] & |[alias=s59targetd]|\Sigma
\arrow[ul,phantom,"\text{(cart)}" description]
\end{tikzcd}}"""

divider = r"""\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.45pt,line cap=round] (0,0)
.. controls (.65,-.02) and (.90,.02) .. (1.08,.13)
-- (1.30,.50)
.. controls (1.55,.72) and (1.70,.77) .. (1.90,.76)
.. controls (2.70,.70) and (3.50,.81) .. (4.90,.77);
\end{tikzpicture}}"""

diamond = r"""\diagram{\begin{tikzcd}[name=s59diamond,execute at end picture={
\coordinate (s59hc) at ([xshift=-6pt,yshift=6pt]s59sourcec.north west);
\draw[line width=.7pt,line cap=round] ([xshift=-4.5pt,yshift=2pt]s59hc)--([xshift=-4.2pt,yshift=1pt]s59hc);
\draw[line width=.7pt,line cap=round] ([xshift=-2.8pt]s59hc)--([xshift=-1.7pt,yshift=-.2pt]s59hc);
\fill (s59hc) circle[radius=.5pt];
\draw[line width=.7pt,line cap=round] ([xshift=2pt,yshift=.8pt]s59hc)--([xshift=2.8pt,yshift=1.5pt]s59hc);
}]
& \Sigma^{<}(1)\arrow[dl,"p_1"'] & \\
\Sigma && |[alias=s59sourcec]|\Sigma^{<}(2)\arrow[ul,"\uline{s'}"',start anchor=north west,shorten <=7pt]\arrow[dl,"p_2"]\\
&\Sigma^{<}(1)\arrow[ul,"p_1"]&
\end{tikzcd}}"""

inline = r"""\diagram{\begin{tikzcd}[column sep=large,execute at end picture={
\coordinate (s59hi) at ([xshift=9pt]s59inline.east);
\draw[line width=.65pt,line cap=round] ([yshift=6pt]s59hi)--([xshift=-1.4pt,yshift=5.8pt]s59hi);
\draw[line width=.65pt,line cap=round] ([xshift=-3pt,yshift=5pt]s59hi)--([xshift=-4.2pt,yshift=4.3pt]s59hi)--([xshift=-5pt,yshift=2.8pt]s59hi)--([xshift=-4.4pt,yshift=1.3pt]s59hi)--([xshift=-3pt,yshift=.4pt]s59hi);
\fill ([xshift=-1.5pt]s59hi) circle[radius=.4pt];
}]
|[alias=s59inline]|\Sigma^{<}(1)\arrow[r,"\uline{b}",start anchor=east,shorten <=9pt]&\Sigma
\end{tikzcd}}"""
square_hook_top = "\n".join(square.splitlines()[1:7])
square_hook_bottom = "\n".join(square.splitlines()[7:13])
diamond_hook = "\n".join(diamond.splitlines()[1:6])
inline_hook = "\n".join(inline.splitlines()[1:5])

header = r"\mspage{\unsure{\{25\}}}"
eq37 = r"(37)\qquad p_2:\Sigma^{<}(2)\longrightarrow\Sigma^{\unsure{<|*}}(1)"
eq38 = r"""\left\{\begin{aligned}
\uline{b}\circ p_2&=\uline{s}\circ\uline{b'}\\[6em]
p_1\circ p_2&=p_1\circ\uline{s'}
\end{aligned}\right."""
mono = r"(\deleted{\unsure{b}},p_1,\uline{b}):\Sigma^{<}(1)\unsure{\longrightarrow|\mathrel{-}}\Sigma\unsure{<|\times}\Sigma"
map_p1 = r"p_1:\Sigma^{<}(1)\unsure{\longrightarrow|\mathrel{-}}\Sigma"
eq39 = r"(39)\qquad x\prec y\quad\Longleftrightarrow\quad\exists\ u\in\Sigma_{<}(1)\text{ tel que }x=p_1u,\ y=\uline{b}u"
tex = r"""\scanpage{59}
""" + header + r"""
de telle façon qu'il existe
\[
""" + eq37 + r"""
\]
tel que
\[
(38)\qquad """ + eq38 + r"""
\]
i.e. le carré
""" + square + r"""
commutatif
""" + divider + r"""

i.e. le carré
""" + diamond + r"""
est comm.

Ce qui détermine $p_2$ de façon unique, puisque
$""" + mono + r"""$ est mono).
De plus, on \deleted{\unsure{suppose}}\inserted{doit} exiger que le premier carré
(38) soit \uline{cartésien}, et que $""" + map_p1 + r"""$
est \uline{transversal} p.r. à l'immersion bordante
$\uline{b}:$ """ + inline + r""" (ce qui est \deleted{\unsure{une}}\inserted{l'unique} condition de
nature non purement algébrique\ldots)
Posons alors, pour $x,y\in\Sigma$
\[
""" + eq39 + r"""
\]
\margin{58}
"""

changes = []

def change(place, C, H, final, ac, ah, kind, category, confidence, evidence, crop,
           marked=False, consequence=''):
    m = by[crop]
    changes.append({
        'id': f'059-{len(changes)+1:02d}', 'place': place, 'C': C, 'H': H,
        'final': final, 'against_C': ac, 'against_H': ah, 'kind': kind,
        'error_category': category, 'marked_in_H': marked,
        'confidence': confidence, 'evidence': evidence,
        'crop': m['file'], 'box': m['box'], 'mathematical_consequence': consequence
    })

change('top left, author number', r'\mspage{\unsure{\deleted{24}25}}', '25',
       header, True, False, 'misread symbol or index', 'Symbols and indices', 'medium',
       'The central 2 and 5 are legible. Dark paired strokes flank them, with upper and lower returns consistent with braces. The crowded side strokes do not expose a separately readable cancelled 24. The brace reading remains marked in place; H describes 25 enclosed by braces in an editorial note.',
       'p01_number')
change('display (37), source superscript', r'\Sigma^{<}(2)', r'\Sigma^{*}(2)',
       r'\Sigma^{<}(2)', False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
       'The small raised mark has a steep upper-right branch and a short lower-right return meeting at the left. Its narrow angle shape agrees with the more open left angles in the two diagrams; no independent central vertical arm is exposed here.',
       'p02_equation37', consequence='The superscript is retained as the locally written angle.')
change('display (37), target superscript', r'\Sigma^{<}(1)', r'\Sigma^{*}(1)',
       r'\Sigma^{\unsure{<|*}}(1)', False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
       'The raised strokes are crowded against the opening parenthesis. An angle with a retraced junction is plausible, while the extra short dark branch prevents a secure exclusion of the star reading. Both readings remain in the formula.',
       'p02_equation37', consequence='The target superscript remains unresolved in place.')
change('display (38), brace joining both equalities',
       eq38,
       '', eq38, False, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'A continuous tall left brace has an upper vertical part, a small left loop at the middle, and a lower outward return, spanning the two written equalities. H mentions the brace in a note but does not set it with the equations.',
       'p03_equations38')
for position, form in [('upper-left', r'\Sigma^{<}(2)'), ('upper-right', r'\Sigma^{<}(1)'), ('lower-left', r'\Sigma^{<}(1)')]:
    change('first square, '+position+' object', form, form.replace('^{<}', '^{*}'), form,
           False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
           'The raised sign is a small left-facing angle with a compressed or retraced vertex. The upper-right example shows the two branches most openly. The same form occurs at this object; the opening parenthesis is read separately.',
           'p04_square', consequence='The diagram object keeps the angle superscript.')
change('first square, upper horizontal hook',
       r'\draw[densely dotted] ([xshift=7pt]s59sourcea.east) arc[start angle=270,end angle=90,radius=3pt];',
       r"""\arrow[r, hook, "\underline b'"]""",
       square_hook_top,
       False, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'The source hook has five discrete dark components: an upper point and four successively lower short marks, turning left before returning toward the shaft. C already gives a dotted curve; its implementation is refined to preserve the observed components. H draws a continuous hook although its editorial note calls the hook dotted.',
       'p04_square')
change('first square, lower horizontal hook',
       r'\draw[densely dotted] ([xshift=7pt]s59sourceb.east) arc[start angle=270,end angle=90,radius=3pt];',
       r"""\arrow[r, hook, "\underline b"']""",
       square_hook_bottom,
       False, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'Four rounded separated points follow the upper and left curve; the fifth component is a short thick lower segment. The lower hook remains distinct from the following horizontal shaft.',
       'p04_square')
change('first square, left vertical label', r"""\arrow[d,"p_2"']""", r"""\arrow[d, "p_2"']""",
       r'\arrow[d,"p_2"]', True, True, 'insertion or placement', 'Insertions put in the wrong place', 'high',
       'The p and its lowered 2 lie to the right of the descending left shaft. Both witness diagrams place this label on the other side by their primed label option.',
       'p04_square')
change('first square, lower horizontal label', r"""\arrow[r,"\uline{b}"',start anchor=east,shorten <=7pt]""", r"""\arrow[r, hook, "\underline b"']""",
       r'\arrow[r,"\uline{b}"]', True, True, 'insertion or placement', 'Insertions put in the wrong place', 'high',
       'The upright b and its underline sit above the lower horizontal shaft. Their source position is retained by the unprimed label option.',
       'p04_square')
change('first square, right vertical endpoint', r'\arrow[d,"p_1=\uline{s}"]', r'\arrow[d, "p_1=\underline s"]',
       r'\arrow[d,"p_1=\uline{s}",dash,end anchor=north,shorten >=4pt]\fill ([yshift=4pt]s59targetd.north) circle[radius=.9pt];',
       True, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'The vertical shaft ends in a filled rounded dark blob. The two exposed oblique strokes of a V-shaped head cannot be isolated there. The rounded terminal mark is reproduced directly; the left vertical arrow has its separately visible V-shaped head.',
       'p04_square')
change('first square, center', r'\text{(cart.)}', '(cart.)', r'\text{(cart)}',
       True, True, 'other', 'Other', 'high',
       'The central parenthesis encloses c, the low joined ar, and a tall final t. The gap before the closing parenthesis contains no separate dark dot.',
       'p04_square')
change('line 5, below first square', 'commutatif', r'\ill{} \uncertain{relatif}', 'commutatif',
       False, True, 'misread word', 'Words', 'medium',
       'Low joined groups begin the word; the right-hand end has the tall t, dotted i, and long descending f. They form commutatif. The rising separator crosses the final descending stroke but does not cancel the word. H reports the alternative within an editorial note.',
       'p05_commutatif', marked=True)
change('between the two diagrams, curved divider', '', '', divider,
       True, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'A separate unheaded thin stroke begins below the word, runs briefly rightward, rises in a broad curve across the final f descender, and continues nearly horizontally beneath the first square. C omits the stroke; H describes it in a note without reproducing it.',
       'p05_commutatif')
for position, form in [('top', r'\Sigma^{<}(1)'), ('right', r'\Sigma^{<}(2)'), ('bottom', r'\Sigma^{<}(1)')]:
    change('second square, '+position+' object', form, form.replace('^{<}', '^{*}'), form,
           False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
           'The superscript has a left-pointing junction, an upper-right branch and a short lower-right return. The right and bottom examples join visually toward the following opening parenthesis; that joining stroke is retained as part of the hand rather than supplied as an extra star arm.',
           'p06_diamond', consequence='The object retains the locally written angle superscript.')
change('second square, source hook of underlined s prime',
       r'\draw[densely dotted] ([xshift=-5pt,yshift=5pt]s59sourcec.north west) arc[start angle=135,end angle=315,radius=3pt];',
       r"""\arrow[ul, "\underline s'"']""",
       diamond_hook,
       False, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'Four separated ink components bend below and to the left of the rising diagonal shaft: a left slanted segment, a low segment, a point, and a right slanted segment. The hook is visible above the right-hand object; H omits it.',
       'p06_diamond')
change('line 7, after second square', 'est comm.', 'est commutatif.', 'est comm.',
       False, True, 'abbreviation expanded or spelling modernised', 'Abbreviations expanded, spelling modernised', 'high',
       'After est, three low groups give comm followed by a separate stop. No following tall t, dotted i or descending f is written.',
       'p07_est_comm')
change('line 9, cancelled first component', r'\deleted{\unsure{b,}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{b}}', False, True, r'readable ink left as \ill{}', 'Readable ink left as illegible', 'medium',
       'A tall initial stem and a low right bowl remain visible under several dark cancelling strokes. They support b as a partial reading, but the overlap prevents certainty about its full original form or any underline. The separate comma is handled in the next row.',
       'p08_monomorphism', marked=True)
change('line 9, comma following cancelled first component', r'\deleted{\unsure{b,}}', r'\struck{\ill{}}\,p_1',
       r'\deleted{\unsure{b}},p_1', True, True, 'deletion state', 'Struck text', 'high',
       'The small descending comma is positioned at the lower right of the cancelled letter cluster. No cancelling stroke crosses it. It remains live before p_1.',
       'p08_monomorphism', marked=True)
change('line 9, source superscript', r'\Sigma^{<}(1)', r'\Sigma^{*}(1)', r'\Sigma^{<}(1)',
       False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
       'Above the opening parenthesis, a narrow high diagonal returns to a short low branch at a left-facing junction. The source Sigma itself is retraced; no earlier complete letter can be recovered separately from the overtracing.',
       'p08_monomorphism', consequence='The source superscript remains the locally written angle.')
change('line 9, mark between the two terminal Sigmas', r'\Sigma\times\Sigma', r'\Sigma\times\Sigma',
       r'\Sigma\unsure{<|\times}\Sigma', True, True, 'misread symbol or index', 'Symbols and indices', 'low',
       'The small sign has an acute left-pointing junction, a rising rightward stroke and a lower rightward return. A separate crossing extension is not securely exposed. The visible angle-like form is placed first, and the witnesses’ multiplication sign remains an explicit alternative.',
       'p08_monomorphism', consequence='The glyph connecting the terminal Sigmas is unresolved; no product interpretation is supplied as a correction.')
change('line 10, after De plus', 'De plus, on', 'De plus on', 'De plus, on',
       False, True, 'other', 'Other', 'medium',
       'The final s is followed by a further low rightward stroke turning down. Its comma-like return precedes the separated on. C’s punctuation is retained.',
       'p09_de_plus')
change('line 11, p1 source superscript', r'\Sigma^{<}(1)', r'\Sigma^{*}(1)', r'\Sigma^{<}(1)',
       False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
       'The raised narrow angle stands immediately above the left parenthesis. Its upper-right branch and low return remain visible despite the close joining with the parenthesis.',
       'p11_cartesian', consequence='The p1 source retains the written angle superscript.')
change('line 12, opening verb', 'est', 'soit', 'est',
       False, True, 'misread word', 'Words', 'high',
       'The word begins with a low open e-like curve and continues directly into the tall terminal t with its short cross stroke. Its outline repeats the est in line 7; there is no initial s followed by an independent oi group.',
       'p12_est_transversal')
change('line 13, inline b-map source superscript', r'\Sigma^{<}(1)', r'\Sigma^{*}(1)', r'\Sigma^{<}(1)',
       False, True, 'misread symbol or index', 'Symbols and indices', 'medium',
       'A small left-facing angle is raised between Sigma and the opening parenthesis; its right branch meets the upper return of the parenthesis.',
       'p13_inline_arrow', consequence='The inline source retains the angle superscript.')
change('line 13, inline b-map hook',
       r'\draw[densely dotted] ([xshift=7pt]s59inline.east) arc[start angle=270,end angle=90,radius=3pt];',
       r'\overset{\underline b}{\hookrightarrow}',
       inline_hook,
       False, True, 'drawing or diagram', 'Drawings and diagrams', 'high',
       'The hook has three separated components. A short upper bar sits over a connected angular C-like middle piece, followed by a small lower point before the ordinary shaft. The shaft’s terminal V is clearly exposed. H’s continuous hook does not preserve these gaps.',
       'p13_inline_arrow')
change('line 13, cancelled word after ce qui est', r'\deleted{une}', r'\struck{\ill{}}', r'\deleted{\unsure{une}}',
       False, True, r'readable ink left as \ill{}', 'Readable ink left as illegible', 'medium',
       'A short low three-letter group lies under a dense horizontal cancellation. The initial u-like trough, central small rise and low terminal loop permit une, but do not expose every letter independently. The word stays doubtful under its deletion.',
       'p14_unique', marked=True)
change('line 13, placement of inserted l’unique', r"\inserted{l'unique}", r"\add{\uncertain{l'unique}}",
       r"\deleted{\unsure{une}}\inserted{l'unique}", False, True, 'insertion or placement', 'Insertions put in the wrong place', 'high',
       'The inserted l with its apostrophe stands above the crossed short word, followed by the joined unique group with a long q descender. The nearby curved lead ends at the condition phrase. It replaces the crossed word after ce qui est; it is not attached before the earlier b-map.',
       'p14_unique', marked=True)
change('line 13, H’s extra inserted une', '', r'\add{une}', '',
       False, True, 'text not on the page', 'Text that is not on the page', 'high',
       'Only the crossed low group and the upper l’unique insertion occupy this place. No second live inserted une is written between the cancellation and condition.',
       'p14_unique')
change('display (39), Sigma index position', r'\unsure{\Sigma_{<}(1)|\Sigma^{<}(1)}', r'\Sigma^{*}(1)',
       r'\Sigma_{<}(1)', False, True, 'misread symbol or index', 'Symbols and indices', 'high',
       'The small left-angle mark lies below the bottom horizontal stroke of Sigma, immediately before the opening parenthesis. It has an upper-right branch and lower return. Its lowered placement is explicit and is preserved even though the preceding occurrences have raised signs.',
       'p15_equation39', consequence='The final displayed expression retains the author’s lowered angle rather than a supplied superscript.')
change('bottom left foliation', r'\mspage{58}', '', r'\margin{58}',
       False, True, 'omission', 'Omissions', 'high',
       'Thin pale strokes at the bottom left form 58, in a hand and medium visibly lighter than the dark authorial writing. It is retained as another hand’s foliation. The C-to-final wrapper change alone is not counted as a substantive departure.',
       'p16_foliation')

decisions = [
    {
        'id': 'M0597', 'decision': 'undecided', 'reading': header,
        'evidence': 'Central 25 is clear. The dark side strokes have paired upper and lower returns supporting braces, but are crowded and retraced. A separate cancelled 24 is not independently legible, and the enclosing-brace reading is still marked in place.',
        'crop': by['p01_number']['file'], 'box': by['p01_number']['box'], 'confidence': 'medium'
    },
    {
        'id': 'M0598', 'decision': 'first', 'reading': r'\Sigma_{<}(1)',
        'evidence': 'The small angular mark is wholly below the lower stroke of Sigma and directly before the opening parenthesis. Its two rightward branches meet at a left-facing low point. The whole formula, including x prec y, double arrow, existence sign, u, and both terminal equations, was read on the same crop.',
        'crop': by['p15_equation39']['file'], 'box': by['p15_equation39']['box'], 'confidence': 'high'
    }
]

inventory = []
def inv(kind, position, text, hand='his hand'):
    inventory.append({'element': f'E{len(inventory)+1:02d}', 'kind': kind, 'position': position,
                      'first_words_or_objects': text, 'sheet_kind': 'text',
                      'hand': hand, 'transcribed': 'yes'})

inv('margin note', 'top left', header)
inv('text', 'line 1', "de telle façon qu'il existe")
inv('display', 'line 2, display (37)', eq37)
inv('text', 'line 3', 'tel que')
inv('display', 'lines 4 and 6, joined by left brace', '(38) '+eq38)
inv('text', 'line 4, right of first equality', 'i.e. le carré')
inv('diagram', 'upper right, first square', square)
inv('text', 'line 5, below first square', 'commutatif')
inv('drawing', 'between first and second squares', divider)
inv('text', 'line 6, right of second equality', 'i.e. le carré')
inv('diagram', 'right middle, second square', diamond)
inv('text', 'line 7, below second equality', 'est comm.')
inv('text', 'lines 8–9', 'Ce qui détermine '+r'$p_2$'+' de façon unique, puisque '+r'$'+mono+r'$ est mono).')
inv('deletion', 'line 9, first component of pair', r'\deleted{\unsure{b}}')
inv('text', 'lines 10–14', 'De plus, on … nature non purement algébrique…)')
inv('deletion', 'line 10, before exiger', r'\deleted{\unsure{suppose}}')
inv('insertion', 'above cancelled suppose in line 10', r'\inserted{doit}')
inv('display', 'line 11, inline p1 map', map_p1)
inv('diagram', 'line 13, inline b map', r'$\uline{b}:$ '+inline)
inv('deletion', 'line 13, after ce qui est', r'\deleted{\unsure{une}}')
inv('insertion', 'above crossed une in line 13', r"\inserted{l'unique}")
inv('text', 'line 15', r'Posons alors, pour $x,y\in\Sigma$')
inv('display', 'line 16, display (39)', eq39)
inv('margin note', 'bottom left', '58', hand='another unnamed hand')

doubts = [
    {'place': 'top left, M0597', 'reading': header, 'alternatives': r'C: \deleted{24}25; paired surrounding braces remain the preferred uncertain reading',
     'confidence': 'medium', 'reason': 'The central digits are legible; the flanking dark flourishes are retraced and do not expose a separate earlier number.'},
    {'place': 'display (37), target exponent', 'reading': r'\Sigma^{\unsure{<|*}}(1)', 'alternatives': r'\Sigma^{<}(1) | \Sigma^{*}(1)',
     'confidence': 'medium', 'reason': 'The raised mark and opening parenthesis meet in a dark multi-branched junction.'},
    {'place': 'line 9, cancelled first component', 'reading': r'\deleted{\unsure{b}}', 'alternatives': 'b-like letter; original underlining cannot be isolated',
     'confidence': 'medium', 'reason': 'Several cancelling strokes cover the lower bowl and any possible separate underline.'},
    {'place': 'line 9, map shaft', 'reading': r'\unsure{\longrightarrow|\mathrel{-}}', 'alternatives': 'headed arrow | unheaded horizontal shaft',
     'confidence': 'medium', 'reason': 'The horizontal stroke ends in a short raised thickening; a two-sided V is not independently exposed.'},
    {'place': 'line 9, terminal binary glyph', 'reading': r'\unsure{<|\times}', 'alternatives': r'< | \times',
     'confidence': 'low', 'reason': 'The acute left-facing junction is visible; the crossing extension required to separate the witnesses’ multiplication reading remains obscured or absent.'},
    {'place': 'line 10, struck suppose', 'reading': r'\deleted{\unsure{suppose}}', 'alternatives': 'suppose remains a partial reading',
     'confidence': 'medium', 'reason': 'An initial s-like curve, two p descenders and final low strokes survive; the broad horizontal cancellation hides the intervening letters.'},
    {'place': 'line 11, map shaft', 'reading': r'\unsure{\longrightarrow|\mathrel{-}}', 'alternatives': 'headed arrow | unheaded horizontal shaft',
     'confidence': 'medium', 'reason': 'A tiny raised thickening appears at the shaft’s end, without a securely exposed lower V stroke. The clearer head of the following b map is kept distinct in the drawing.'},
    {'place': 'line 13, struck une', 'reading': r'\deleted{\unsure{une}}', 'alternatives': 'une remains a partial reading',
     'confidence': 'medium', 'reason': 'The low letter troughs and terminal loop remain beneath dense horizontal ink, but each letter is not independently legible.'}
]

notes = [
    {'id': '150-059-N01', 'text': 'The central authorial number at the top is 25. Its flanking dark strokes support an enclosing-brace reading, retained with doubt; C’s cancelled 24 cannot be separately recovered. A lighter 58 at the lower left belongs to another unnamed hand and is retained as foliation.'},
    {'id': '150-059-N02', 'text': 'The author introduces p_2 in (37), writes the two equalities joined by the brace of (38), and accompanies them with two diagrams. The words below them are commutatif and est comm. He puts (cart) in the first square and later requires that first square to be cartésien. He also writes that p_1 is transversal p.r. à the immersion bordante b. These are accounts of the manuscript’s assertions, not proof checks.'},
    {'id': '150-059-N03', 'text': 'The author says that p_2 is uniquely determined and invokes the displayed map beginning with the pair (p_1,b) as mono. The cancelled initial b-like component and the surviving comma are preserved. The small sign between the two terminal Sigmas remains <|×, and the shortened map endpoint remains arrow|shaft; no interpretation of these uncertain strokes was used to repair the transcription. The unmatched closing parenthesis in est mono). is retained.'},
    {'id': '150-059-N04', 'text': 'The author replaces suppose by doit and a crossed short word, read tentatively as une, by l’unique. The cancellation hides much of suppose and une, so both remain doubtful. The l’unique insertion attaches after ce qui est, above the crossed word; it does not attach before the b map.'},
    {'id': '150-059-N05', 'text': 'In (39) the author gives x prec y by the displayed existence expression. The small angle is below Sigma in that formula; this explicit placement resolves M0598 to the first reading. The earlier Sigma expressions have raised small angle forms, with the crowded target superscript of (37) still open as angle|star. This is a report of the written positions and symbols; no equivalence of the expressions was assumed or proved.'},
    {'id': '150-059-N06', 'text': 'The dotted source hooks are reproduced with their observed separate components: five in each horizontal hook of the first square, four in the second square, and three in the inline b map. The first square’s right vertical stroke has a rounded filled terminal mark. The curved divider crosses the descender of commutatif without cancelling the word. These graphic readings were based on the visible strokes.'}
]

notation = [
    {'form': r'\Sigma^{<}(1),\Sigma^{<}(2)', 'meaning': 'The manuscript’s raised-angle object notation in the maps and diagrams.', 'evidence': 'Narrow left-pointing raised forms with two rightward branches; the most open examples are in the two squares.', 'places': 'display (37), both squares, lines 9, 11 and 13'},
    {'form': r'\Sigma^{\unsure{<|*}}(1)', 'meaning': 'The unresolved target exponent of (37).', 'evidence': 'The raised mark is crowded against the following parenthesis, with a short extra dark branch.', 'places': 'display (37), target'},
    {'form': r'\Sigma_{<}(1)', 'meaning': 'The explicitly lowered-angle expression written in (39).', 'evidence': 'The small angle sits below the lower Sigma stroke.', 'places': 'display (39)'},
    {'form': r"\uline{b},\uline{b'},\uline{s},\uline{s'}", 'meaning': 'Underlined map letters used by the author in the equalities and diagrams.', 'evidence': 'Short separate horizontal underline strokes lie beneath the b and s letters; primes sit above and to the right.', 'places': '(38), both squares, lines 9, 12–13 and (39)'},
    {'form': r'p_1,p_2', 'meaning': 'The author’s indexed map labels.', 'evidence': 'Distinct lowered 1 and 2 forms beside tall p stems.', 'places': '(37), (38), both squares, lines 8–11 and (39)'},
    {'form': r'\prec', 'meaning': 'The relation sign used by the author in (39).', 'evidence': 'A broad curved left-pointing relation mark separates x and y.', 'places': 'display (39)'},
    {'form': 'broken source hooks', 'meaning': 'Graphical source decorations on four drawn shafts.', 'evidence': 'Five, five, four and three separated components respectively, preserving visible gaps.', 'places': 'first square twice, second square s-prime shaft, inline b map'}
]

abbreviations = [
    {'written': 'i.e.', 'expansion': 'id est', 'places': 'lines 4 and 6'},
    {'written': 'cart', 'expansion': 'cartésien', 'places': 'center of first square; no separate stop is written'},
    {'written': 'comm.', 'expansion': 'commutatif', 'places': 'line 7'},
    {'written': 'mono', 'expansion': 'monomorphisme (tentative expansion of the manuscript’s short form)', 'places': 'line 9'},
    {'written': 'p.r.', 'expansion': 'par rapport', 'places': 'line 12'}
]

hand_log = [
    {'habit': 'The narrow left-angle superscript may have a looped or retraced vertex and may join the following parenthesis.', 'places': '059: (37), both squares, lines 9, 11 and 13', 'scope': 'All raised-angle occurrences inspected; the densest target of (37) remains doubtful.', 'witness_errors': 'H writes * at all these occurrences; the locally open two-branch forms support <, while the crowded target stays <|*.'},
    {'habit': 'Low connected cursive groups compress commutatif and comm.; the final tall strokes or their absence determine the written length.', 'places': '059: lines 5 and 7', 'scope': 'The full word and its shortened form on this page only.', 'witness_errors': 'H’s note proposes relatif at line 5, and H expands line 7 comm. to commutatif.'},
    {'habit': 'The short est can be a long low curve ending in a compact crossed upright.', 'places': '059: lines 7, 9, 12 and 13', 'scope': 'All visible occurrences of est on this page.', 'witness_errors': 'H reads soit at line 12.'},
    {'habit': 'A curved divider may cross the descender of an adjacent word without cancelling it.', 'places': '059: line 5, final f of commutatif', 'scope': 'One observed divider crossing.', 'witness_errors': 'C omits the divider; H describes it and leaves the associated word partly illegible.'},
    {'habit': 'The drawn source hooks consist of visibly separated ink parts with unequal shapes, rather than a uniform solid hook.', 'places': '059: first square upper and lower shafts; second square s-prime shaft; line 13 b shaft', 'scope': 'All four source hooks on this page were counted.', 'witness_errors': 'H draws the first-square and inline hooks continuously and omits the second-square hook.'},
    {'habit': 'Cancellation strokes can cover most internal letters while leaving descenders and isolated loops.', 'places': '059: cancelled b-like component, suppose, une', 'scope': 'All three cancellation groups, each retained with local doubt.', 'witness_errors': 'H leaves b and une as illegible; C gives suppose and une without doubt and includes the surviving comma in its cancelled group.'}
]

audit_boxes = []
def audit(kind, box, reading):
    audit_boxes.append({'box': f'B{len(audit_boxes)+1:02d}', 'kind': kind,
                        'x0': box[0], 'y0': box[1], 'x1': box[2], 'y1': box[3],
                        'reading': reading})

audit('handwritten number', [21,25,142,108], header)
audit('doubtful formula', [235,250,1090,350], eq37)
audit('handwritten number', [239,402,1670,1102],
      'tel que '+r'\[(38)\qquad '+eq38+r'\] i.e. le carré '+square+
      ' commutatif '+divider+' i.e. le carré '+diamond+' est comm.')
audit('handwritten number', [827,1199,887,1269], r'p_2')
audit('doubtful formula', [226,1317,1488,1444], '$'+mono+'$ est mono).')
audit('lexical disagreement', [227,1468,561,1588], 'De plus, on')
audit('struck passage', [590,1468,837,1589], r'\deleted{\unsure{suppose}}\inserted{doit}')
audit('insertion', [684,1468,788,1517], r'\inserted{doit}')
audit('doubtful formula', [205,1596,1560,1719], r'(38) soit \uline{cartésien}, et que $'+map_p1+'$')
audit('insertion', [239,1735,1670,1948],
      r"est \uline{transversal} p.r. à l'immersion bordante $\uline{b}:$ "+inline+
      r" (ce qui est \deleted{\unsure{une}}\inserted{l'unique} condition de")
audit('doubtful formula', [213,2137,1669,2264], eq39)
audit('handwritten number', [21,2291,86,2340], r'\margin{58}')

record = {
    'scan': '059', 'reader': 'reader_c', 'line_count': 21,
    'line_count_basis': 'Sixteen main writing baselines, including numbered displays and equation/prose baselines, plus five object rows across the two separate diagrams; author number and other-hand foliation excluded.',
    'changes': changes, 'decisions': decisions, 'inventory': inventory, 'doubts': doubts,
    'notes': notes, 'check_events': [], 'notation': notation,
    'abbreviations': abbreviations, 'hand_log': hand_log, 'audit_boxes': audit_boxes,
    'crops': manifest,
    'unresolved': [
        'M0597: central 25 is clear; surrounding braces remain tentative and no separate cancelled 24 is recovered.',
        'Display (37): target superscript remains <|*.',
        'Line 9: cancelled b-like component; original underlining cannot be recovered.',
        'Line 9: arrow versus reduced unheaded shaft at the map endpoint.',
        'Line 9: < versus × between the two terminal Sigmas.',
        'Line 10: suppose is only partly exposed beneath its cancellation.',
        'Line 11: the map endpoint remains arrow|unheaded shaft.',
        'Line 13: une remains a partial reading under dense cancellation.'
    ],
    'coverage': {
        'whole_image_viewed': True, 'halves_viewed': ['top','bottom'], 'all_tokens_read': True,
        'all_C_insertions_deletions_checked': True, 'differences_considered': 47,
        'macro_only_differences_ignored': 'Equivalent underline macros, add/inserted and struck/deleted wrappers, arrow command lengths, i.e. spacing, display/environment scaffolding, diagram aliases, and editorial H notes were not counted solely for their syntax. Actual label positions, missing graphical parts, shorthand expansion, source superscripts and foliation omission were considered individually. The C-to-final foliation wrapper change alone is not counted.'
    }
}

def atomic(path, value):
    tmp = path.with_name(path.name+'.tmp')
    with tmp.open('w', encoding='utf-8') as f:
        f.write(value)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)

atomic(root/'reader_returns/150_scan059.tex', tex)
atomic(root/'reader_returns/150_scan059.json', json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(f"Saved scan059: {len(changes)} changes, {len(decisions)} decisions, {len(inventory)} inventory entries, {len(audit_boxes)} audit boxes, {len(manifest)} crops.")
print('Against C:', sum(r['against_C'] for r in changes), 'Against H:', sum(r['against_H'] for r in changes))
