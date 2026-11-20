from pathlib import Path
import csv
import json
import re

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet = root / 'packets/145_scan025'
out = root / 'edition/reader_reports'
C = (packet / 'C.tex').read_text()
H = (packet / 'H.tex').read_text()
manifest = json.loads((out / '145_scan025_crop_boxes.json').read_text())
crops = {x['name']: x for x in manifest}
cd = re.findall(r'\\\[(.*?)\\\]', C, re.S)
hd = re.findall(r'\\\[(.*?)\\\]', H, re.S)

E = r'\widehat{\widehat{\mathcal E}}^!'
wave = r'\unsure{\sim|\deleted{\sim}}'
WE = r'\overset{' + wave + r'}{\widehat{\widehat{\mathcal E}}}^!'
SE = 'S' + E
SWE = 'S' + WE
inverse = r'\unsure{\deleted{\unsure{-1}}|\unsure{-1}}'
baseC = r'\tilde v(\tilde u_i(\tilde u))\cdot\gamma_i(\tilde v)'
baseH = r'\tilde v(\gamma_i(\tilde u))\cdot\gamma_i(\tilde v)'
crossed_upper = r'\gamma_i(\tilde v)\cdot v(\gamma_i(\tilde u))'
live24 = r'\tilde v(\gamma_i(\tilde u)\gamma_i(\tilde v)'
final_choice = r'\unsure{(\hat{\mathbb Z})^{\{0,1,\infty\}}|(\hat{\mathbb Z})^3}'
pi_doubt = r'\widehat{\unsure{\pi|\Pi}}'
margin_index = r'\unsure{[0,1,\infty]|\{0,1,\infty\}}'

opening = r'est unique, et $g_i$ défini multiplication à gauche par un él. quelconque de $L_i$, soit $l_i^{\unsure{\alpha_i}}$ $(\alpha_i\in\hat{\mathbb Z})$.'
action = r'On passe de $u$ à $\operatorname{int}(g)\circ u$ en \inserted{gardant $p$, et en\unsure{,}} remplaçant les $g_i$ par les $gg_i$.'
intro = r'Si $v$ est donné par $q,(h_i)$, on a'
f1 = r'vu(l_i)=v(\operatorname{int}(g_i^{' + inverse + r'})l_i^p)=\operatorname{int}(v(g_i^{' + inverse + r'}))v(l_i)^p'
f2 = r'v(l_i)=\operatorname{int}(h_i^{' + inverse + r'})l_i^q\qquad\text{donc}\qquad v(l_i)^p=\operatorname{int}(h_i^{' + inverse + r'})l_i^{pq}'
product23 = r'v(g_i^{' + inverse + r'})h_i^{' + inverse + '}'
bracket23 = r'''\begin{tikzpicture}[baseline=(prod.base)]
\node[inner sep=0pt] (prod) {$''' + product23 + r'''$};
\draw[line width=0.4pt] ([yshift=1pt]prod.north west) -- ([yshift=5pt]prod.north west) -- ([yshift=5pt]prod.north east);
\draw[line width=0.6pt] ([yshift=5pt]prod.north east) -- ++(-0.06,0.025) -- ++(0.035,-0.055);
\end{tikzpicture}'''
annotation23 = r'\deleted{\unsure{(h_i v(g_i))^{-1}}}'
f23 = r'(23)\quad vu(l_i)=\operatorname{int}\bigl(\overset{' + annotation23 + '}{' + bracket23 + r'}\bigr)l_i^{pq}'
definition_start = r"Si on désigne par $" + SWE + r"$ l'extension de $" + E + r"$ par $\hat{\mathbb Z}^{\{0,1,\infty\}}$ définie \deleted{\unsure{par le couple|par le groupe}} groupe des\unsure{.} \deleted{couples} triples d'un $u\in" + E + r"$ et d'un"
definition_rest = r"système de $g_i$ qui explicitent \inserted{via (21)} l'isomorphisme de la structure à lacets ($p$ étant le multiplicateur), on a sur $" + SWE + r'$ trois fonctions à valeurs dans $\deleted{\unsure{\mathcal E}}\hat\Pi$'
mapping = r'(u,(g_i))\overset{\gamma_i}{\longmapsto}g_i,'
f24 = r'(24)\quad\gamma_i(\tilde v\tilde u)=\deleted{\unsure{' + baseC + '|' + baseH + r'}}\inserted{\deleted{\unsure{' + crossed_upper + '}} ' + live24 + '}'
cocycle = r'i.e. $(\gamma_i)$ est un 1-cocycle sur le groupe \deleted{$\unsure{' + E + r'}$}\inserted{$' + SWE + r'$} à valeurs dans le groupe \deleted{\unsure{produit du groupe}}\inserted{opposé au groupe} $\pi^{\{0,1,\infty\}}$.'
margin_formula = r'(p,g_0,g_1,g_\infty)\in\hat{\mathbb Z}^*\times\Pi^{' + margin_index + '}'
margin = r'\margin{\uline{NB} $' + SE + r'''$ a été construit comme le groupe des Systèmes
\[
''' + margin_formula + r'''
\]
satisfaisant la relation (22)}'''
kernel = r'Le sous-groupe de $' + SE + r'$ noyau de $' + SWE + r'\longrightarrow\operatorname{Aut}\operatorname{ext}_{\mathrm{lac}}^!(' + pi_doubt + r")$ s'identifie au groupe produit"
lower_trace = r'''\begin{tikzpicture}[x=0.10cm,y=0.10cm,baseline=0ex]
\draw[line width=0.3pt] (0,1.35) -- (0.25,0) -- (0.65,1.25);
\draw[line width=0.3pt] (1.05,1.15) -- (1.15,0.1);
\fill (1.0,1.65) circle (0.08);
\end{tikzpicture}'''
last_formula = r'\left(\hat\Pi\times\prod_{i\in\{0,1,\infty\}}L_i\right)\simeq' + pi_doubt + r'\times\underset{' + lower_trace + '}{' + final_choice + '}'
def display(body):
    return '\\[\n' + body + '\n\\]'
tex = '\n'.join([r'\scanpage{25}', r'\mspage{11}', opening + ' ' + action, '', intro,
                  display(f1), 'où', display(f2), 'donc', display(f23),
                  definition_start + ' ' + definition_rest, display(mapping), 'et on aura',
                  display(f24), cocycle, margin, r'\deleted{groupe}', kernel,
                  display(last_formula), r'\mspage{24}', ''])
(out / '145_scan025.tex').write_text(tex)

changes = []
def change(n, place, c, h, final, ink, crop, kind, cc=False, hc=True,
           marked='no', confidence='high', categories=(2,), consequence=''):
    image = crops[crop]
    changes.append({'id': f's025-{n:02d}', 'place': place, 'C': c, 'H': h, 'final': final,
                    'ink': ink, 'confidence': confidence, 'kind': kind,
                    'c_changed': cc, 'h_changed': hc, 'marked_in_H': marked,
                    'crop': image['crop'], 'box': image['box'],
                    'error_category': list(categories), 'math_consequence': consequence})

change(1, 'Opening, immediately after défini', r'défini \unsure{à} multiplication',
       r'défini \uncertain{à} multiplication', 'défini multiplication',
       'After the final dotted i of défini there is a clear gap followed directly by the low initial m/u strokes of multiplication. No separate a body or accent occupies that gap. The later à before gauche is distinct and remains.',
       'opening', 'text not on the page', cc=True, marked='yes', categories=(9,))
change(2, 'Opening, after à gauche', 'à gauche par', r'\uncertain{à gauche} près par', 'à gauche par',
       'The dark retraced gauche ends at the right edge of the first line. The next line begins par. No près is written between them. The darker word still reads gauche; no older word can be recovered confidently beneath its retracing.',
       'opening', 'text not on the page', marked='yes', categories=(9,))
change(3, 'Opening abbreviation', 'él.', 'élt.', 'él.',
       'The accented e joins one high looped l and is followed by a separate dark point. There is no crossed t or additional terminal letter.',
       'opening', 'abbreviation expanded or spelling modernised', categories=(8,))
change(4, 'End of opening paragraph, replacement by an inner automorphism',
       r'On passe de $u$ à $\operatorname{int}(g)\circ u$ en \inserted{gardant $p$, et en} remplaçant les $g_i$ par les $gg_i$.',
       r'Les \ill{} de $u$ : $\operatorname{int}(g)\circ u$ \uncertain{gardent} $p$, et \uncertain{remplacent} les $g_i$ par les $gg_i$.',
       action,
       'The initial capital O and short n, then the p descender and joined body of passe, are visible. The small accented à separates u from int(g) circle u. The baseline en remains before remplaçant; gardant p, et en is written above as an insertion attached there. Both g descenders in gg_i are plain. A small detached hook after the inserted en is retained only as a local punctuation/pen-trace doubt, not a certain comma.',
       'action_insertion', 'insertion or placement', marked='yes', categories=(2,3,5,6))
change(5, 'First preliminary formula, both g_i exponents', cd[0].strip(), hd[0].strip(), f1,
       'Both very small exponent areas are dark angular masses. Extra upstrokes favor cancellation over a clean written minus followed by1, but the second is especially compact; the live-state alternative cannot be excluded. The underlying minus1 is itself doubtful. Both glyph and state alternatives are therefore explicit at each position.',
       'composition_first', 'deletion state', confidence='low', categories=(7,),
       consequence='The exponent state is not decided from either conjugation convention.')
change(6, 'Second preliminary formula, both h_i exponents', cd[1].strip(), hd[1].strip(), f2,
       'Each h_i has a short raised dark mass with several angular strokes. The last has multiple extra upward ticks, favoring a scribbled cancellation. Neither underlying minus1 is fully legible; live versus cancelled remains an explicit alternative. The final pq is followed by no comma.',
       'composition_first', 'deletion state', confidence='low', categories=(7,9))
change(7, '(23), two inverse-exponent positions in the main argument',
       r'v(g_i^{\deleted{\unsure{-1}}})h_i^{\deleted{\unsure{-1}}}',
       r'v(g_i^{-1})\, h_i^{-1}', product23,
       'The two exponent traces have black angled upper strokes beyond the expected two characters. Cancellation is favored but not absolute; their residual glyphs remain unsure minus1. The underlying factors v(g_i) and h_i are not themselves struck.',
       'formula23', 'deletion state', confidence='low', categories=(7,))
change(8, '(23), cancelled upper annotation and its supporting straight bar',
       r'\overbrace{v(g_i^{\deleted{\unsure{-1}}})h_i^{\deleted{\unsure{-1}}}}^{\deleted{\unsure{(h_i v(g_i))^{-1}}}}',
       '', r'\overset{' + annotation23 + '}{' + bracket23 + '}',
       'Above the main product, a hatched expression supports (h_i v(g_i)) with a tiny obscured exponent. The whole annotation is cancelled and remains uncertain. Below it is a straight horizontal bar with a short downward left end and a thick pointed right tip; it is not a curly overbrace. TikZ preserves that geometry. H describes the crossed annotation editorially but omits it from the transcription.',
       'formula23', 'drawing or diagram', cc=True, marked='yes', confidence='medium', categories=(3,4,7))
change(9, 'Word introducing (23)', 'donc', "d'où", 'donc',
       'The word begins with a looped d, continues with a low joined o-n body and ends with the short open terminal c. There is no apostrophe or separate accented u.',
       'formula23', 'misread word')
change(10, '(23), terminal punctuation', r'l_i^{pq}.', r'l_i^{\,pq}', r'l_i^{pq}',
       'The final raised pq and the lower l_i are followed by clear paper, with no separate terminal stop.',
       'formula23', 'text not on the page', cc=True, hc=False, categories=(9,))
change(11, 'First S-extension name in the definition, upper mark', SE, SE, SWE,
       'Above the two sharp hat strokes is a separate dark wavy/zigzag trace. Its ink is real, but it may be a live tilde or a cancelled upper decoration; its proximity to the preceding g descender complicates attachment. The mark is represented locally and uncertainly, rather than omitted or propagated to every S-extension name.',
       'extension_definition', 'omission', cc=True, confidence='low', categories=(1,3))
change(12, 'Definition, crossed words after définie and live groupe',
       r'\deleted{\unsure{par le couple|par le groupe}} \unsure{groupe|formé}',
       r'\struck{\ill{}} \uncertain{par le} groupe',
       r'\deleted{\unsure{par le couple|par le groupe}} groupe',
       'The horizontal cancellation begins at the p of par and runs through the following le and obscured noun. The noun cannot be resolved between couple and groupe. The following live word has a looped g with a long descender and a later p descender: groupe, not formé. There is no extra live par le between the cancellation and groupe.',
       'extension_definition', 'deletion state', marked='yes', confidence='medium', categories=(2,5,7,9))
change(13, 'Definition, système de g_i through structure à lacets and via(21)',
       r"système de $g_i$ qui explicitent \inserted{via (21)} l'isomorphisme de la structure à lacets",
       r'\ill{} (21) \ill{} des $g_i$ qui explicite \ill{}',
       r"système de $g_i$ qui explicitent \inserted{via (21)} l'isomorphisme de la structure à lacets",
       'Despite overlap from the slanted margin at the left, the joined système body and separate de can be followed. After g_i, qui and the final t of explicitent are visible. Via(21) is above the line with a curved guide attaching before l’isomorphisme. The remaining live words are l’isomorphisme de la structure à lacets; their long l, p and t strokes are visible, and the phrase is not blank.',
       'structure_via', 'readable ink left as \\ill{}', marked='yes', categories=(2,3,5,6))
change(14, 'On a sur S-extension, upper mark', SE, SE, SWE,
       'A short dark wavy trace sits above two separate small hats. It is separated from the letters of lacets above, so it is retained as an uncertain upper mark; whether it is a live tilde or a cancelled decoration remains open.',
       'structure_via', 'omission', cc=True, confidence='low', categories=(1,3))
change(15, 'Target of the three functions, before their displayed mapping',
       r'\deleted{\unsure{\mathcal E}}\hat\pi', r'\hat\pi', r'\deleted{\unsure{\mathcal E}}\hat\Pi',
       'A large looped E-like trace is scribbled through immediately before the live group sign. Its exact underlying shape remains doubtful. The live sign has a separate hat, a level upper cap and two full-height legs, supporting capital Pi locally. H omits the crossed trace; both witnesses use lower-case pi.',
       'mapping_pi', 'misread symbol or index', cc=True, confidence='medium', categories=(1,3,7))
change(16, '(24), cancelled baseline expression', r'\deleted{\unsure{' + baseC + '}}',
       r'\struck{' + baseH + '}', r'\deleted{\unsure{' + baseC + '|' + baseH + '}}',
       'One long strike crosses the entire baseline right member. The first inner letter is heavily retraced: a dark u-like body and upper curve favor C’s tilde-u_i, while a gamma reading remains possible. The other factors and parentheses are partly visible but the expression remains uncertain as a whole.',
       'formula24', 'misread symbol or index', confidence='low', categories=(1,7))
change(17, '(24), upper inserted expression subsequently hatched out',
       r'\inserted{\deleted{\unsure{' + crossed_upper + '}}}', '',
       r'\inserted{\deleted{\unsure{' + crossed_upper + '}}}',
       'A distinct second expression lies above the baseline and is covered by repeated oblique hatching. Surviving gamma-like initial strokes, a tilded v and the final gamma_i(tilde u) support C’s provisional reading, but the cancellation obscures the full sequence. It is both inserted and deleted. H’s editorial note reports two cancellations, but its transcription supplies only the baseline one.',
       'formula24', 'omission', marked='yes', confidence='low', categories=(3,6,7))
change(18, '(24), surviving upper-right insertion and parenthesis count',
       r'\unsure{\tilde v(\gamma_i(\tilde u)\gamma_i(\tilde v)|\tilde v(\gamma_i(\tilde u))\gamma_i(\tilde v)}',
       r'\tilde v(\gamma_i(\tilde u))\,\gamma_i(\tilde v)', live24,
       'The surviving writing is above/right of the cancelled baseline and is attached by a curved guide. It has one closing parenthesis after tilde u and one after tilde v. There is no second close after u and no additional terminal close for the outer opening after tilde v. The literal first C alternative is therefore retained, including its unmatched opening.',
       'formula24', 'text not on the page', categories=(1,6,9),
       consequence='The written outer parenthesis remains unmatched; no corrected cocycle formula is substituted.')
change(19, 'Cocycle statement, old group replaced above the line',
       r'\deleted{$\unsure{' + E + r'}$}\inserted{$' + SE + '$}',
       r'$S\hat{\hat{\mathcal{E}}}^{!}$ \struck{\ill{}}',
       r'\deleted{$\unsure{' + E + r'}$}\inserted{$' + SWE + '$}',
       'The old group name is crossed on the baseline after groupe; the replacement beginning S is above that place. The old base/accents are not fully recoverable. H reverses the textual placement of the replacement and crossed residue. Above the replacement’s two hats is a separate wavy mark whose state remains uncertain.',
       'cocycle', 'insertion or placement', cc=True, marked='yes', confidence='low', categories=(1,3,6,7))
change(20, 'Cocycle statement, replacement of the phrase before the target group',
       r'\deleted{\unsure{produit du groupe}}\inserted{opposé au groupe}',
       r'\struck{\ill{} \ill{}}',
       r'\deleted{\unsure{produit du groupe}}\inserted{opposé au groupe}',
       'The baseline phrase is covered by repeated cancellation strokes, leaving produit du groupe plausible but not fully plain. Above it, opposé au groupe is live: the two p descenders, the accent on the ending and the separate au can be read. H does not transcribe the live replacement.',
       'cocycle', 'readable ink left as \\ill{}', marked='yes', confidence='medium', categories=(2,3,5,6,7))
change(21, 'Cocycle statement, target group', r'\pi^{\{0,1,\infty\}}',
       r'\hat\pi^{\{0,1,\infty\}}', r'\pi^{\{0,1,\infty\}}',
       'The base sign is small, with a curved right foot. No hat lies above it; the following set exponent is separate. A dark terminal stop follows the expression.',
       'cocycle', 'misread symbol or index', categories=(1,9))
change(22, 'Slanted NB note, opening description',
       r'\uline{NB} $' + SE + r'$ a été construit comme le groupe des Systèmes',
       r'\textbf{NB} $S\hat{\hat{\mathcal{E}}}^{!}$ a été construit comme ensemble des systèmes',
       r'\uline{NB} $' + SE + r'$ a été construit comme le groupe des Systèmes',
       'A single independent line underlines NB. The description visibly reads comme le, then groupe des Systèmes: the g has a long lower loop, the later p descends, and Systèmes begins with a large capital S. The margin’s group name has only two hats; no additional wave is supplied.',
       'margin_nb', 'misread word', categories=(2,3,10))
change(23, 'NB note, tuple membership formula',
       r'(p,g_0,g_1,g_\infty)\in\hat{\mathbb Z}^*\times\pi^{\{0,1,\infty\}}',
       r'(p,g_0,g_1,g_\infty)\in\hat{\mathbb Z}^{*}\times\hat\pi^{\{0,1,\infty\}}',
       margin_formula,
       'The tuple and its 0,1,infinity indices are visible. Hat Z has a separate star; the following Pi has two tall legs and no hat. Its exponent delimiters are unusually straight/heavy: the right is bracket-like and the left lacks a secure middle waist. Square brackets are the first local reading, with curly set braces retained as an alternative.',
       'margin_nb', 'misread symbol or index', cc=True, confidence='medium', categories=(1,9))
change(24, 'NB note, ending after the relation number', 'satisfaisant la relation (22).',
       'satisfaisant la relation (22)', 'satisfaisant la relation (22)',
       'The note ends with the curved closing parenthesis of (22). No separate stop is visible after it.',
       'margin_nb', 'text not on the page', cc=True, hc=False, categories=(9,))
change(25, 'Standalone cancelled word above the final paragraph',
       r'\deleted{groupe} Le sous-groupe', r'Le sous-groupe \struck{\ill{}}',
       r'\deleted{groupe} Le sous-groupe',
       'A long dark line crosses groupe on its own baseline above Le sous-groupe. The g descender and joined r-o-u-p-e body remain readable. The word is not inserted after the live sous-groupe as H’s linear placement suggests.',
       'kernel_final', 'insertion or placement', marked='yes', categories=(2,5,6,7))
change(26, 'Final kernel-map domain, upper mark', SE, SE, SWE,
       'Above the map-domain E’s two hats is a dark wavy trace near the cancelled groupe above. Its presence is secure, but attachment and live/cancelled state remain uncertain. It is retained locally; the preceding de S-extension name has only two hats and is not given the extra mark.',
       'kernel_final', 'omission', cc=True, confidence='low', categories=(1,3))
change(27, 'Final product, left hatted group factor', r'\hat\pi\times\prod_{i\in\{0,1,\infty\}}L_i',
       r'\hat\pi \times \prod_{i \in \{0,1,\infty\}} L_i',
       r'\hat\Pi\times\prod_{i\in\{0,1,\infty\}}L_i',
       'The left factor has a separate hat and a cap with two full-height legs, supporting capital Pi. The large product operator and its set index are separate and visible. The smaller Pi-like signs in the adjacent Autext argument and right side are not mechanically capitalized; their local case doubts are retained.',
       'kernel_final', 'misread symbol or index', cc=True, categories=(1,))
change(28, 'Final right-hand Z-like factor, small lower traces', final_choice,
       r'\hat{\mathbb{Z}}^{\{0,1,\infty\}}',
       r'\underset{' + lower_trace + '}{' + final_choice + '}',
       'The terminal factor is retraced and crowded against the right page edge. Beneath its Z-like body are a narrow v-shaped trace and a separate short near-vertical mark with a small high point. These are reproduced graphically without assigning a subscript or reconstructing an older formula. The live exponent still cannot be resolved securely; its ending approaches the clipped edge.',
       'kernel_final', 'drawing or diagram', cc=True, confidence='low', categories=(1,3,4))
change(29, 'Bottom-left handwritten page number', r'\mspage{24}', '', r'\mspage{24}',
       'A curved2 and an angular4 stand in dark ink at the bottom left. H omits this actual inscription; it is distinct from editorial page notices.',
       'kernel_final', 'omission', categories=(3,))

decisions = [
    {'id': 'M0863', 'decision': 'other', 'reading': '',
     'ink': 'No separate a body or accent occurs between défini and multiplication. The later à before gauche is present.',
     'crop': crops['opening']['crop'], 'box': crops['opening']['box'], 'confidence': 'high'},
    {'id': 'M0864', 'decision': 'first', 'reading': 'groupe',
     'ink': 'The live word following the crossed phrase has a looped g descender and a later p descender, followed by e; it is groupe, not formé.',
     'crop': crops['extension_definition']['crop'], 'box': crops['extension_definition']['box'], 'confidence': 'high'},
    {'id': 'M0865', 'decision': 'first', 'reading': live24,
     'ink': 'The surviving upper-right formula has only one close after tilde u and one after tilde v. The outer opening after the leading tilde v is left unclosed. No parenthesis is supplied from the expected cocycle law.',
     'crop': crops['formula24']['crop'], 'box': crops['formula24']['box'], 'confidence': 'high'},
    {'id': 'M0866', 'decision': 'undecided', 'reading': final_choice,
     'ink': 'The final Z-like body and its immediate delimiters are retraced. The exponent reaches the page edge and contains compressed marks that favor the longer indexed form but do not securely distinguish it from the shorter3 reading. Small lower traces are recorded separately without inventing a layer order.',
     'crop': crops['kernel_final']['crop'], 'box': crops['kernel_final']['box'], 'confidence': 'low'},
]

unlisted = []
for n, locus, crop in [
    (1, 'First preliminary formula, g_i in the left v(int(...)) term', 'composition_first'),
    (2, 'First preliminary formula, g_i in the right int(v(...)) term', 'composition_first'),
    (3, 'Second preliminary formula, h_i defining v(l_i)', 'composition_first'),
    (4, 'Second preliminary formula, h_i defining v(l_i)^p', 'composition_first'),
    (5, '(23), g_i inside v', 'formula23'),
    (6, '(23), following h_i', 'formula23'),
]:
    image = crops[crop]
    unlisted.append({'id': f'U025-{n:02d}', 'decision': 'undecided', 'reading': inverse,
                     'ink': locus + ': small black angular extra strokes favor cancellation. The underlying minus1 is not fully legible; a live exponent remains possible, so both state and glyph uncertainty are explicit.',
                     'crop': image['crop'], 'box': image['box'], 'confidence': 'low'})
for n, reading, ink, crop in [
    (7, annotation23, 'The entire upper annotation is diagonally hatched. h_i v(g_i) is supported, but the letter intersections and tiny final exponent do not permit complete resolution.', 'formula23'),
    (8, r'\deleted{\unsure{par le couple|par le groupe}}', 'The phrase begins par le; the remaining crossed noun has overlapping looped/descending strokes compatible with couple or groupe.', 'extension_definition'),
    (9, r'\deleted{\unsure{\mathcal E}}', 'The crossed looped sign before the hatted Pi is E-like, but its exact base/upper decoration cannot be recovered fully.', 'mapping_pi'),
    (10, r'\deleted{\unsure{' + baseC + '|' + baseH + '}}', 'The baseline expression is crossed once; the inner u/gamma area is retraced, so the C-like and H-like readings are both retained.', 'formula24'),
    (11, r'\inserted{\deleted{\unsure{' + crossed_upper + '}}}', 'The upper inserted formula is heavily hatched; the surviving fragments support C’s reading without resolving every letter.', 'formula24'),
    (12, r'\deleted{$\unsure{' + E + '}$}', 'The old group name is crossed on the baseline below its S-prefixed replacement, with its accents and base obscured.', 'cocycle'),
    (13, r'\deleted{\unsure{produit du groupe}}', 'Repeated crossing strokes obscure the baseline phrase; produit du groupe remains a provisional reading beneath the live opposé au groupe.', 'cocycle'),
]:
    image = crops[crop]
    unlisted.append({'id': f'U025-{n:02d}', 'decision': 'undecided', 'reading': reading,
                     'ink': ink, 'crop': image['crop'], 'box': image['box'], 'confidence': 'low'})

doubts = []
for x in unlisted:
    if int(x['id'].split('-')[1]) <= 6:
        alternatives = ['cancelled exponent, provisionally -1', 'live exponent, provisionally -1', 'another obscured original glyph']
    else:
        alternatives = [x['reading'], 'unresolved obscured strokes within the cancelled range']
    doubts.append({'place': x['id'], 'reading': x['reading'], 'alternatives': alternatives,
                   'confidence': 'low', 'reason': x['ink']})
doubts.append({'place': 'M0866', 'reading': final_choice,
               'alternatives': [r'(\hat{\mathbb Z})^{\{0,1,\infty\}}', r'(\hat{\mathbb Z})^3'],
               'confidence': 'low', 'reason': decisions[3]['ink']})
doubts.extend([
    {'place': 'Opening, exponent of l_i', 'reading': r'\unsure{\alpha_i}',
     'alternatives': [r'\alpha_i', 'overwritten alpha-like indexed exponent'], 'confidence': 'low',
     'reason': 'The exponent is much darker and more retraced than the clear following parenthetical alpha_i; the loop/body and index are not fully separable.'},
    {'place': 'End of inserted gardant p, et en', 'reading': r'\unsure{,}',
     'alternatives': ['comma', 'detached pen/insertion trace'], 'confidence': 'low',
     'reason': 'A small detached hook follows the inserted en. It is comma-like but not securely punctuation; it is represented only as doubtful.'},
    {'place': 'After des, before crossed couples', 'reading': r'\unsure{.}',
     'alternatives': ['point', 'pen trace amid the nearby marginal overlap'], 'confidence': 'low',
     'reason': 'A small isolated dark point is present. Its position and nearby crossing baselines do not establish punctuation; it is not promoted to a certain stop.'},
])
for place in ['First S-extension name in the definition', 'On a sur S-extension', 'Inserted S-extension in the cocycle statement', 'Final kernel-map domain S-extension']:
    doubts.append({'place': place + ', upper mark', 'reading': wave,
                   'alternatives': ['live tilde/wavy upper mark', 'cancelled tilde or other upper decoration', 'overlapping stroke with uncertain attachment'],
                   'confidence': 'low', 'reason': 'A dark wavy trace is separate from the two small hats. Its glyph/state and, where nearby writing intrudes, exact attachment remain uncertain. No analogous mark is supplied to the other group-name occurrences.'})
for place in ['Autext argument in the final sentence', 'Right-hand hatted group factor in the final product']:
    doubts.append({'place': place, 'reading': pi_doubt, 'alternatives': [r'\hat\pi', r'\hat\Pi'],
                   'confidence': 'medium', 'reason': 'This sign is smaller and more compressed than the clearly tall two-leg Pi at the left of the final product. The right foot is curved; local case remains open.'})
doubts.extend([
    {'place': 'NB tuple, exponent delimiters on Pi', 'reading': margin_index,
     'alternatives': [r'[0,1,\infty]', r'\{0,1,\infty\}'], 'confidence': 'medium',
     'reason': 'The left delimiter is straight and heavy, the right bracket-like; curvature sufficient to establish a matched curly-brace pair is not secure.'},
    {'place': 'Small lower strokes beneath final Z-like factor', 'reading': lower_trace,
     'alternatives': ['residue of an overwritten lower layer', 'unidentified lower index/letter strokes'], 'confidence': 'low',
     'reason': 'The narrow v-shaped stroke, separate short vertical and high point are visible, but do not support a secure lexical or mathematical reading or chronology.'},
])

inventory = []
def inv(kind, pos, words, box):
    inventory.append({'element': f'I{len(inventory)+1:02d}', 'kind': kind, 'position': pos,
                      'first_words_or_objects': words, 'box': box,
                      'sheet_kind': 'text', 'hand': 'his hand', 'transcribed': 'yes'})
inv('text', 'Top center', '11', [820,35,865,79])
inv('text', 'Four opening main-text lines', 'est unique, et g_i défini', [270,60,1655,485])
inv('insertion', 'Above en remplaçant', 'gardant p, et en, with doubtful detached hook', [1192,228,1605,286])
inv('text', 'Line introducing composition', 'Si v est donné par q,(h_i)', [382,493,1460,581])
inv('display', 'First preliminary composition formula', 'vu(l_i)=v(int(g_i...))', [295,600,1310,715])
inv('deletion', 'First formula, first tiny exponent: state itself doubtful', inverse, [640,627,680,664])
inv('deletion', 'First formula, second tiny exponent: state itself doubtful', inverse, [1045,614,1087,651])
inv('text', 'At left of second preliminary formula', 'où', [304,769,385,813])
inv('display', 'Second preliminary formula with donc', 'v(l_i)=int(h_i...)l_i^q', [470,697,1615,816])
inv('deletion', 'Second formula, first tiny exponent: state itself doubtful', inverse, [749,704,790,745])
inv('deletion', 'Second formula, second tiny exponent: state itself doubtful', inverse, [1392,694,1435,732])
inv('text', 'At left above (23)', 'donc', [245,904,354,948])
inv('display', '(23), complete composition result', f23, [240,810,1265,1018])
inv('deletion', '(23), exponent on g_i: state itself doubtful', inverse, [928,890,973,926])
inv('deletion', '(23), exponent on h_i: state itself doubtful', inverse, [1036,888,1082,928])
inv('deletion', 'Above main product in (23)', annotation23, [898,811,1140,885])
inv('drawing', 'Straight support below the crossed annotation', 'Horizontal bar, short left downstroke, pointed right thickening', [884,878,1075,902])
inv('text', 'Six-line definition before mapping', 'Si on désigne par S...', [240,990,1665,1685])
inv('text', 'Upper decoration on first S-extension name', wave, [947,986,1018,1014])
inv('deletion', 'After définie', r'\deleted{\unsure{par le couple|par le groupe}}', [1071,1115,1410,1203])
inv('deletion', 'Before triples', r'\deleted{couples}', [411,1270,622,1342])
inv('text', 'Isolated point after des, function doubtful', r'\unsure{.}', [374,1301,393,1320])
inv('insertion', 'Above l’isomorphisme', 'via (21)', [1196,1298,1370,1398])
inv('text', 'Upper decoration on on a sur S-extension', wave, [704,1552,764,1591])
inv('deletion', 'Before hatted Pi at start of mapping line', r'\deleted{\unsure{\mathcal E}}', [276,1752,344,1827])
inv('display', 'Displayed gamma_i mapping', mapping, [581,1728,1060,1832])
inv('text', 'Right of mapping', 'et on aura', [1160,1726,1515,1787])
inv('display', '(24), all three right-member layers', f24, [260,1810,1585,2015])
inv('deletion', '(24), baseline right member', r'\deleted{\unsure{' + baseC + '|' + baseH + '}}', [750,1900,1198,2003])
inv('insertion', '(24), upper expression later cancelled', r'\inserted{\deleted{\unsure{' + crossed_upper + '}}}', [790,1836,1193,1912])
inv('deletion', '(24), hatching of upper inserted expression', r'\deleted{\unsure{' + crossed_upper + '}}', [790,1836,1193,1912])
inv('insertion', '(24), surviving upper-right expression with curved guide', live24, [1198,1821,1542,2003])
inv('text', 'Two-line cocycle statement', 'i.e. (gamma_i) est un 1-cocycle', [250,2010,1665,2175])
inv('deletion', 'Old group after groupe', r'\deleted{$\unsure{' + E + '}$}', [1387,1990,1578,2062])
inv('insertion', 'Replacement group above old group', SWE, [1392,1917,1508,2006])
inv('text', 'Upper decoration on inserted S-extension', wave, [1441,1916,1500,1948])
inv('deletion', 'Below opposé au groupe', r'\deleted{\unsure{produit du groupe}}', [930,2083,1410,2173])
inv('insertion', 'Above crossed target-group description', 'opposé au groupe', [1013,2068,1418,2129])
inv('margin note', 'Six slanted lines at left, single underlined NB', 'NB S... a été construit', [20,1250,370,2005])
inv('deletion', 'Standalone word above Le sous-groupe', r'\deleted{groupe}', [265,2173,548,2223])
inv('text', 'Final kernel paragraph', 'Le sous-groupe de S...', [280,2120,1675,2343])
inv('text', 'Upper mark near final map-domain E', wave, [1285,2123,1361,2166])
inv('display', 'Final product identification at lower right', last_formula, [1145,2243,1680,2354])
inv('drawing', 'Small lower traces under last Z-like body', lower_trace, [1585,2310,1631,2355])
inv('text', 'Bottom-left handwritten number', '24', [39,2292,117,2350])

second_boxes = [
    {'box': 'B01', 'kind': 'Opening word differences, missing à, overwritten alpha exponent, every handwritten digit/header11',
     'coords': [270,35,1655,242], 'reading': r'\mspage{11}' + '\n' + opening},
    {'box': 'B02', 'kind': 'Complete action phrase and interlinear insertion, doubtful detached hook, gg_i order',
     'coords': [275,225,1645,485], 'reading': action},
    {'box': 'B03', 'kind': 'Full preliminary formulas, four inverse glyph/state doubts and all their numerical strokes',
     'coords': [295,495,1615,820], 'reading': intro + '\n' + display(f1) + '\noù\n' + display(f2)},
    {'box': 'B04', 'kind': 'Entire (23), two inverse glyph/state doubts, crossed annotation, straight bar, handwritten23 and missing stop',
     'coords': [240,810,1265,1018], 'reading': 'donc\n' + display(f23)},
    {'box': 'B05', 'kind': 'Complete extension-definition opening, numerical set exponent, upper mark, crossed phrase, groupe, crossed couples and doubtful point',
     'coords': [240,990,1630,1345], 'reading': definition_start},
    {'box': 'B06', 'kind': 'Système phrase, via(21) insertion, entire structure phrase, upper mark above later S-extension',
     'coords': [235,1250,1665,1685], 'reading': r"triples d'un $u\in" + E + r"$ et d'un " + definition_rest.split(r' à valeurs dans ')[0] + ' à valeurs dans'},
    {'box': 'B07', 'kind': 'Crossed E, hatted capital Pi, entire gamma_i map with arrow/label',
     'coords': [255,1695,1540,1845], 'reading': r'$\deleted{\unsure{\mathcal E}}\hat\Pi$' + '\n' + display(mapping) + '\net on aura'},
    {'box': 'B08', 'kind': 'Entire (24), all cancelled/inserted layers, literal parenthesis count, number24 and adjacent inserted group upper mark',
     'coords': [260,1810,1585,2015], 'reading': display(f24) + '\n' + r'\inserted{$' + SWE + '$}'},
    {'box': 'B09', 'kind': 'Complete cocycle statement, every correction and inserted upper mark, number1 and full numerical exponent',
     'coords': [250,1915,1665,2175], 'reading': cocycle},
    {'box': 'B10', 'kind': 'Entire NB margin, underline, tuple with all numbers, Pi case/hat and bracket doubt, relation22',
     'coords': [20,1250,370,2005], 'reading': margin},
    {'box': 'B11', 'kind': 'Entire final paragraph and full product, standalone cancellation, all hats/Pi-case doubts, edge-clipped exponent, lower traces and footer24',
     'coords': [25,2120,1680,2358], 'reading': r'\deleted{groupe}' + '\n' + kernel + '\n' + display(last_formula) + '\n' + r'\mspage{24}'},
]

coverage = {
 1: ('macro/editorial',None,'C scan25 is an editorial identifier; H p. introduces its notice of the handwritten header11.'),
 2: ('macro/editorial',None,'H de l’auteur is editorial. The handwritten11 is retained.'),
 3: ('substantive',2,'No près follows gauche in the ink.'),
 4: ('substantive',3,'The abbreviation is él., without t.'),
 5: ('substantive',4,'On passe, not Les followed by an illegible gap.'),
 6: ('substantive',4,'An accented à links u to int(g) circle u; H colon is a misreading.'),
 7: ('substantive',4,'Baseline en plus inserted gardant p, et en; not live gardent.'),
 8: ('substantive',4,'The insertion and baseline remplaçant are retained, not H remplacent.'),
 9: ('macro/editorial',None,'H backslash-comma denotes thin spacing, not literal punctuation. The exponent-state disagreement is separately logged in s025-05.'),
 10: ('macro/editorial',None,'H thin-space macro in the exponent, not a comma.'),
 11: ('macro/editorial',None,'H thin-space macro; exponent states are s025-05.'),
 12: ('macro/editorial',None,'H thin-space macro; exponent states are s025-06.'),
 13: ('macro/editorial',None,'H thin-space macro in exponent placement.'),
 14: ('macro/editorial',None,'H thin-space macro; exponent states are s025-06.'),
 15: ('macro/editorial',None,'H thin-space macro in exponent placement.'),
 16: ('substantive',6,'The final literal comma in H’s second preliminary formula is absent; the same locus records inverse-state uncertainty.'),
 17: ('substantive',9,'The visible word is donc.'),
 18: ('macro/editorial',None,'H thin-space macro in(23); exponent-state disagreement is s025-07.'),
 19: ('substantive',8,'Alignment spans C’s upper annotation and H’s omission from the displayed formula; s025-07 covers the main-product inverse states.'),
 20: ('substantive',8,'H describes the crossed upper annotation only editorially. Its ink and straight support are transcribed.'),
 21: ('macro/editorial',None,'H backslash-comma within its quoted annotation is spacing, not an ink comma.'),
 22: ('substantive',10,'No stop follows(23); the displaced H editorial reference to a brace is covered by s025-08.'),
 23: ('substantive',12,'Crossed phrase remains par le couple|par le groupe; no new live par le is supplied.'),
 24: ('substantive',12,'The live word resolves groupe. Alternative-token spelling alone is not a further inscription.'),
 25: ('substantive',13,'Système de is visible; the(21) phrase is an insertion farther along the line.'),
 26: ('substantive',13,'Explicitent and the complete l’isomorphisme de la structure à lacets phrase are read; via(21) remains inserted.'),
 27: ('substantive',15,'Crossed E-like sign is present before the hatted Pi.'),
 28: ('substantive',16,'Baseline inner u/gamma area remains uncertain under the strike.'),
 29: ('substantive',17,'Alignment conflates two crossed layers; the separately inserted-and-cancelled expression is retained.'),
 30: ('substantive',18,'Surviving formula selects C’s literal first alternative with no extra close after tilde u.'),
 31: ('substantive',17,'H’s explanatory note is editorial; it reports the second cancellation that its transcript omits.'),
 32: ('substantive',19,'Old group is crossed on the baseline and replaced above, with its extra upper mark recorded.'),
 33: ('substantive',20,'The crossed phrase remains doubtful; opposé au groupe is visibly inserted and live.'),
 34: ('substantive',22,'Margin/main-text ordering creates the long alignment shift. The entire margin is transcribed; s025-22 to24 cover its differences, s025-25 to29 the final paragraph.'),
 35: ('substantive',22,'The margin says le groupe, not ensemble.'),
 36: ('substantive',23,'Display syntax is editorial, but the complete margin tuple has real Pi case/hat and delimiter differences recorded in s025-23.'),
 37: ('macro/editorial',None,'Closing display delimiter; the full margin formula is preserved.'),
 38: ('substantive',24,'The margin has no final stop. The displaced main paragraph includes the crossed groupe, local upper mark, final product uncertainties and omitted footer24, covered by s025-25 to29.'),
}
with (packet/'differences.tsv').open(newline='') as fh:
    rows = list(csv.DictReader(fh, delimiter='\t'))
diffs = []
for n,row in enumerate(rows,1):
    status,num,explanation=coverage[n]
    entry={'row':n,'status':status,'C_tokens':row['witness C'],'H_tokens':row['witness H'],
           'words_before':row['words before'],'raw_note':row['note'],'explanation':explanation}
    if num is not None: entry['change_id']=f's025-{num:02d}'
    diffs.append(entry)

report = {
 'scan':25,'reader':'reader_c','lines_read':38,
 'layout':'Handwritten sheet with header11, four opening main lines and an insertion, composition formulas and(23) with a crossed upper annotation, a six-line extension definition, a left slanted NB note, gamma_i mapping, heavily corrected(24), a two-line corrected cocycle statement, and the final kernel/product paragraph ending at the right edge; footer24. Separate interlinear and side-by-side writing units are counted in lines_read.',
 'changes':changes,'decisions':decisions,'unlisted_decisions':unlisted,'doubts':doubts,
 'inventory':inventory,'second_boxes':second_boxes,
 'notation':[
  'Six tiny inverse exponents have both explicit glyph and state alternatives. Angular extra strokes favor cancellation, but the live-exponent alternative survives; the original glyph is provisionally minus1 and is not resolved by convention.',
  'Hatted Pi after the crossed E and unhatted Pi in the marginal tuple have tall two-leg forms and are transcribed capital Pi. The cocycle target is smaller with a curved right foot and remains lower-case pi, without a hat. The final product’s left factor is capital Pi; its right factor and the Autext argument retain local case doubts.',
  'Four S-extension occurrences have a wavy trace above their two hats: first definition, on a sur, the inserted cocycle group, and the final map domain. Their live/cancelled state and occasional overlap/attachment remain uncertain. The NB group and the earlier de S-extension in the final paragraph have only two hats; no wave is added there.',
  'The gamma_i mapping arrow has a short vertical tail bar and a separate gamma_i label. The straight bar below the crossed annotation of(23) has a short left downstroke and a thick pointed right tip; it is represented geometrically rather than as a curly brace.',
  'The surviving(24) has one close after tilde u and one after tilde v, leaving the outer opening unclosed. Parenthesis balance is not repaired from the cocycle interpretation.',
  'The margin Pi exponent has square-bracket-like end strokes, with curly braces retained as an alternative. The final Z-like factor and exponent remain retraced and edge-crowded; separate small lower traces are reproduced without assigning a subscript.'
 ],
 'hand':[
  'The main prose is pale, while several corrections and accents are dark/retraced. These differences do not establish a different hand; all elements are assigned to his hand.',
  'Long p and g descenders distinguish On passe, groupe and gg_i from H’s readings. In the last product and the cocycle target, the scale and curved foot of Pi-like signs prevent a universal case normalization.',
  'The compact low body of a French word may be almost horizontal: système, explicitent and l’isomorphisme remain readable from their tall stems and dotted letters. A faint connecting line is not expanded into an extra word.',
  'Tiny black angular marks may be cancellation scribbles rather than legible numerical exponents; their state is recorded independently of the formulas’ mathematical interpretation.',
  'Small detached marks after inserted en and after des are recorded only as doubtful punctuation/pen traces. They are not promoted to certain punctuation, particularly where slanted marginal text overlaps.'
 ],
 'abbreviations':[
  {'form':'él.','expansion':'élément','place':'Opening paragraph'},
  {'form':'NB','expansion':'nota bene','place':'Single-underlined marginal heading'},
  {'form':'i.e.','expansion':'id est','place':'Cocycle interpretation'},
  {'form':'int','expansion':'inner automorphism notation','place':'Opening and composition formulas'},
  {'form':'Aut ext','expansion':'automorphismes extérieurs','place':'Final kernel-map target'},
  {'form':'lac','expansion':'à lacets / structure à lacets','place':'Subscript of final automorphism-group target'}
 ],
 'notes':[
  'The opening states uniqueness and ambiguity by left multiplication, then describes replacing u by int(g) circle u while replacing g_i by gg_i and keeping p. The separate à after défini is absent. The visible à gauche and gg_i are both retained; no convention-driven repair is made. The alpha_i exponent is retraced and remains doubtful.',
  'The author writes two preliminary composition formulas and(23). Six tiny inverse-exponent positions favor cancellation but preserve explicit live-state alternatives and underlying-glyph uncertainty. The crossed upper annotation also remains uncertain. Root is comparing both algebraic conventions independently; this reader performed no mathematical verification and does not use either convention to decide the strokes.',
  'The author introduces an S-prefixed extension and describes triples involving u and a system of g_i, with a via(21) insertion specifying the isomorphism of a structure à lacets. After a crossed phrase the live word is groupe. The small point after des is not accepted as certain punctuation.',
  'Formula(24) has a cancelled baseline expression, a separately inserted expression subsequently hatched out, and a surviving upper-right expression linked by a curved guide. The surviving expression literally lacks an outer closing parenthesis. The following prose calls the gamma_i a1-cocycle and replaces produit du groupe by opposé au groupe. These are the author’s written claims, not proof certifications.',
  'The NB note says le groupe des Systèmes, gives the tuple condition and refers to relation(22). It uses an unhatted capital Pi, not the hatted lower-case pi supplied by H. The note’s opening group has two hats and no additional upper wave. Its endpoint has no separate stop.',
  'The final paragraph identifies a kernel with a product. The rightmost factor is retraced and reaches the page edge; its exponent, the local Pi case, and unidentified lower traces remain explicit. No older formula is reconstructed from an expected direct-product description.',
  'The actual handwritten numbers are11 at the head and24 at the foot. Formula labels23 and24 and references21 and22 are retained in physical order; the numerical indices and exponents are covered by full second-reading boxes. No date is visible. Editorial scan25 and H’s explanatory notes are not manuscript text.',
  'All fifteen C cancellation ranges and five C insertion ranges were checked, including the inserted-and-cancelled upper formula. The whole image and each native overlapping half were inspected once, followed by eleven enlarged crops made once each. Root reviewed all eleven crops. No other page, OCR, research or TeX compilation was used.'
 ],
 'check_events':[], 'diff_coverage':diffs
}
(out/'145_scan025.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

# Structural checks only, without compilation or further image inspection.
with (packet/'marks.tsv').open(newline='') as fh:
    marks=list(csv.DictReader(fh,delimiter='\t'))
assert [x['id'] for x in decisions]==[x['id'] for x in marks]
assert len(rows)==len(diffs)==38
assert [x['row'] for x in diffs]==list(range(1,39))
assert all(x['c_changed'] or x['h_changed'] for x in changes)
assert len({x['id'] for x in changes})==len(changes)
for x in changes+decisions+unlisted:
    assert (root/'edition'/x['crop']).is_file()
    a,b,c,d=x['box']; assert 0<=a<c<=1686 and 0<=b<d<=2370
for x in second_boxes:
    a,b,c,d=x['coords']; assert 0<=a<c<=1686 and 0<=b<d<=2370
assert len({x['box'] for x in second_boxes})==len(second_boxes)
depth=0
for m in re.finditer(r'(?<!\\)[{}]',tex):
    depth+=1 if m.group()=='{' else -1
    assert depth>=0
assert depth==0
assert tex.count('$')%2==0
assert tex.count(r'\[')==tex.count(r'\]')==7
assert tex.count(r'\begin{tikzpicture}')==tex.count(r'\end{tikzpicture}')==2
assert tex.count(r'\inserted{')==5
assert all(x['sheet_kind']=='text' and x['hand']=='his hand' for x in inventory)
print(json.dumps({'scan':25,'changes':len(changes),'marks':len(decisions),
                  'unlisted':len(unlisted),'doubts':len(doubts),'inventory':len(inventory),
                  'second_boxes':len(second_boxes),'diff_rows':len(diffs),'crops':len(manifest),
                  'status':'structural checks passed'}))
