from pathlib import Path
import json, re
from collections import Counter

ROOT = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
PACKET = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan033')
OUT = ROOT / 'reader_returns'
TEX = OUT / '150_scan033.tex'
tex = TEX.read_text()
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()

def between(s, start, end, include_end=False):
    a = s.index(start)
    b = s.index(end, a) + (len(end) if include_end else 0)
    return s[a:b]

def macro(s, start, offset=0):
    a = s.index(start, offset)
    p = s.index('{', a)
    depth = 0
    for j in range(p, len(s)):
        if s[j] == '{' and (j == 0 or s[j-1] != '\\'):
            depth += 1
        elif s[j] == '}' and (j == 0 or s[j-1] != '\\'):
            depth -= 1
            if depth == 0:
                return s[a:j+1]
    raise ValueError(start)

def norm(s):
    return re.sub(r'\s+', '', s)

crops = {}
for p in sorted((ROOT / 'crops').glob('150_scan033_*.json')):
    x = json.loads(p.read_text())
    crops[p.stem.removeprefix('150_scan033_')] = x

def cfile(name):
    return '150_scan033_' + name + '.jpg'

def cbox(name):
    return crops[name]['box']

top_display = between(tex, '\\[\n(18)', '\\]', True)
top_with_prose = top_display + '\nde la façon suivante :'
top_dot_pair = between(tex, '\\left(\\underset{\\substack{\\parallel\\\\\\dot T_\\beta}}', ',\n\\underset{(B_\\alpha')
top_brace = between(tex, '\\overbrace{', ',\n\\left(\\underset{\\substack{\\parallel\\\\X_i')
top_B = between(tex, '\\underset{(B_\\alpha,\\mathcal E_\\alpha)|X^*}', '\n}^{\\substack')
top_Bbeta = between(tex, '\\underbrace{(B_{\\beta,\\alpha}', ',\\\\\n(\\dot X_\\beta')
hat_formula = between(tex, '\\widehat X&=', '\\\\\nT_\\beta')
T_formula = r'T_\beta&=C(p_\beta)'
Xi_intro = between(tex, 'X_i&\\quad', '\\\\\n\\deleted{X_i}')
Xi_struck = macro(tex, '\\deleted{X_i=')
Xi_formula = between(tex, '\\deleted{X_i}\\quad', '\\\\\nB_\\alpha')
Xi_def = between(tex, '\\underset{\\substack{\\parallel\\text{déf}\\\\X_i^*', '\n\\deleted{\\unsure{I.(')
B_formula = between(tex, 'B_\\alpha&=', '\\\\\n\\mathcal E_\\alpha')
B_def = between(tex, '\\underset{\\substack{\\parallel\\text{déf}\\\\B_\\alpha^*', '\\\\\n\\mathcal E_\\alpha')
E_formula = between(tex, '\\mathcal E_\\alpha&', '\n\\end{aligned}')
condition_a = r'\text{\textcircled{a} Les }X_\beta\text{ disjoints}'
condition_b = between(tex, '\\text{\\textcircled{b} Chaque }', '\n&\\\\[1em]')
condition_d = between(tex, '\\text{\\textcircled{d}}', '\n&\\\\\n&\\hspace')
final_condition = macro(tex, '\\inserted{\\text{\\textcircled{\\unsure{c|d}}')
right_note = macro(tex, '\\margin{le syst.')
left_brace = macro(tex, '\\smash{\\raisebox{-1.25cm}')
right_brace = macro(tex, '\\smash{\\raisebox{-0.30cm}')

changes = []
def add(place, cq, hq, final, evidence, crop, confidence='high', kind='misread symbol or index', error_kind='symbols and indices', change_C=False, change_H=True, marked_in_H=False, consequential=''):
    changes.append(dict(place=place, C=cq, H=hq, final=final, evidence=evidence, crop=cfile(crop), box=cbox(crop), confidence=confidence, kind=kind, error_kind=error_kind, marked_in_H=marked_in_H, change_C=change_C, change_H=change_H, consequential=consequential))

add('upper annotation / cylindres-bord', r'\text{syst. de cylindres-bord}', r'\text{syst. de cylindres-bords transversaux}', r'\text{syst. de cylindres-bord}', 'The final d has its ascending stroke and return; no separate following s is written before the line ends. The hyphen and abbreviation stop are visible.', 'header_annotation', kind='misread word', error_kind='words')
add('(18) / first dotted-X pair / second entry', r'\unsure{\mathcal E_\beta}', r'(\dot X_\beta)_{\beta\in I_0}', top_dot_pair, 'An additional E/epsilon-like body and a cramped lower beta-shaped cluster follow the dotted X. The ink is overtraced and does not settle the precise special form; the C doubt remains. H omits the second entry.', 'opening_dotX_pair', confidence='low', kind='omission', error_kind='omissions')
add('(18) / upper-brace scope', between(C, '\\overbrace{', ',\n\\left(\\underset{\\substack{\\parallel\\\\X_i'), between(H, '\\overbrace{', ',\\ (X^{*}_i)'), top_brace, 'The upper brace begins over the dotted-X pair and ends over the starred boundary pair. Its left endpoint is to the right of the initial X-star, which is outside this brace.', 'header_annotation', kind='drawing or diagram', error_kind='drawings and diagrams')
add('(18) / initial X-star identity', r'\underset{\substack{\parallel\\X\setminus\mathring T_{I_0}}}{X^*}', r'X^{*}=X\setminus\overset{\circ}{T}_{I_0}', r'\underset{\substack{\parallel\\X\setminus\mathring T_{I_0}}}{X^*}', 'Two upright strokes lie between the stacked expressions. The T has a hollow ring and an I with a small lower zero. H turns the upright relation into an inline horizontal equality.', 'opening_Xstar', kind='insertion or placement', error_kind='insertion placement')
add('(18) / dotted-X identity', r'\underset{\substack{\parallel\\\dot T_\beta}}{\dot X_\beta}', r'\dot X_\beta=\dot T_\beta', r'\underset{\substack{\parallel\\\dot T_\beta}}{\dot X_\beta}', 'The lower T has a distinct overhead dot and beta. Two vertical strokes, not a horizontal equality, link it to the upper dotted X.', 'opening_dotX_pair', kind='insertion or placement', error_kind='insertion placement')
add('(18) / starred boundary pair and lower restriction', between(C, '\\underbrace{(B_\\alpha^*,\\mathcal E_\\alpha^*)}', '\n}^{\\substack'), r'(B^{*}_\alpha,\mathcal E^{*}_\alpha)=(B_\alpha,\mathcal E_\alpha)|X^{*}', top_B, 'The restriction is directly beneath the pair. The connecting line is flat through its middle, without the distinct downward cusp seen under the last tuple and under C(p). The lower B and E are unstarred; the upper entries carry stars.', 'opening_Bstar', kind='drawing or diagram', error_kind='drawings and diagrams', change_C=True)
add('(18) / starred indexed-X identity', r'\underset{\substack{\parallel\\X_i\cap X^*}}{X_i^*}', r'X^{*}_i=X_i\cap X^{*}', r'\underset{\substack{\parallel\\X_i\cap X^*}}{X_i^*}', 'The intersection is below the starred X_i, connected by two upright strokes. Both i marks have the short hooked foot and separate dot seen elsewhere on this sheet.', 'opening_Xistar', kind='insertion or placement', error_kind='insertion placement')
add('(18) / final boundary pair restriction', between(C, '\\underbrace{(B_{\\beta,\\alpha}', ',\\\\\n(\\dot X_\\beta'), r'(B_{\beta,\alpha},\mathcal E_{\beta,\alpha})=(B_\alpha,\mathcal E_\alpha)|X_\beta', top_Bbeta, 'The lower restriction is attached by a visibly cusped underbrace. It is not an inline equality introduced later. Commas separate beta and alpha in both upper entries. The lower first index is retraced but has the alpha exit stroke.', 'opening_B_betaalpha', kind='insertion or placement', error_kind='insertion placement')
add('prose following (18) / la façon', 'de la façon suivante :', r'de \uncertain{façon} suivante :', 'de la façon suivante :', 'Between de and the long descending f there is a distinct l-a run. The c-cedilla/ç formation, final on, and the following suivante are visible; no word is inferred from syntax.', 'de_la_facon', kind='omission', error_kind='omissions', marked_in_H=True)
add('(18) / H introductory avec', '[absent]', 'avec ', 'de la façon suivante :', 'No avec is written before the below-line definitions. Those definitions are attached to their objects by upright relations or brackets. The actual prose at the right of the second display row begins de la façon suivante.', 'de_la_facon', kind='text not on the page', error_kind='text not on page')
add('(19) / crossed sign before the lower coproduct', r'\deleted{\unsure{I}}', '[absent]', r'\deleted{\unsure{I}}', 'A separate cancelled upright/serif-like sign precedes the lower coproduct. The crossing obscures the lower form, so I is retained only as the unresolved C candidate.', 'cone_formula', confidence='low', kind='omission', error_kind='struck text')
add('(19) / clair stop', r'\text{clair}.', r'\text{clair}', r'\text{clair}.', 'An isolated dark point is written at the end of the line, well to the right of clair; it is of the source pen rather than the pale background texture.', 'Xbeta_clair', kind='omission', error_kind='omissions')
add('(19) / first cancelled Xi equation and its lower annotation', r'\deleted{\unsure{X_i=I.\dot X_i}}', r'X_i=\mathbf{I}.\dot X_i', Xi_struck, 'The two X bodies, their short dotted i endings, the two equality strokes, and the serif I are readable beneath the zigzag strike. A separate multiplication point cannot be isolated from the crossing. A shallow bracket below the final dotted X and a crossed two-upright/def-like annotation are present; they are absent from both transcriptions and remain doubtful as to their exact letters.', 'Xi_cancelled_first_complete', confidence='low', kind='omission', error_kind='struck text', change_C=True)
add('(19) / cancelled initial Xi before the replacement equation', r'\deleted{\unsure{X_i}}', '[absent]', r'\deleted{X_i}', 'The two diagonals of X, a small lower right continuation, and its separate dot remain distinguishable beneath the short cancellation. There is no beta loop at this position.', 'Xi_equation', kind='misread symbol or index', error_kind='struck text', change_C=True)
add('(19) / live Xi and possible pale overhead stroke', 'X_i&=X_i^*', r'\bar X_i=X^{*}_i', r'\unsure{X_i|\bar X_i}', 'A very short pale grey streak and a small dark speck lie above the live X. The streak is unlike the black source pen of the adjacent letters, stars, and dots. Plain X_i is favored, but the possible thin bar cannot be excluded from this image.', 'Xi_equation', confidence='low', kind='other', consequential='The distinction between a plain and a barred name remains unresolved; neither is silently normalized.')
add('(19) / cancelled union after Xi-star', r'\deleted{\unsure{\cup}}', '[absent]', r'\deleted{\unsure{\cup}}', 'There is a densely crossed small form after the starred X_i and before the live union. A rounded cup-like stroke survives, but the crossing prevents a secure resolution.', 'Xi_equation', confidence='low', kind='omission', error_kind='struck text')
add('(19) / old cancelled union condition', r'\deleted{\unsure{i\in I_\beta}}', '[absent]', r'\deleted{\unsure{i\in I_\beta}}', 'The lower crossed line remains separate from the live beta-in-I-zero and beta-less-than-or-equal-to-i limits. Its letters are partly buried by the replacement and strike; the C candidate is retained as a doubt.', 'Xi_equation', confidence='low', kind='omission', error_kind='struck text')
add('(19) / Xi under-definition / accent in déf', r'\parallel\mathrm{def}', r'\text{déf}', r'\parallel\text{déf}', 'A detached dark accent-like mark is above the e run, before the tall descending f. The same pattern is visible in the B under-definition. The two upright relation strokes stand to its left.', 'Xi_equation', kind='misread word', error_kind='words', change_C=True, change_H=False)
add('(19) / Xi under-definition / bracket and placement', between(C, '\\underbrace{\\dot X_{i\\beta}}', '\n\\deleted{\\unsure{I.('), r'\dot X_{i\beta}\overset{\text{déf}}{=}X^{*}_i\cap\dot X_\beta', Xi_def, 'The line beneath dotted X_i-beta is a shallow flat bracket with upturned ends. Under it are upright relation strokes, déf, and the intersection on the next line. There is no central cusp and no horizontal equality beside the formula.', 'Xi_equation', kind='insertion or placement', error_kind='insertion placement', change_C=True)
add('(19) / cancelled expanded term inside the parentheses', r'\deleted{\unsure{I.(X_i^*\cap\dot X_\beta)}}', '[absent]', r'\deleted{\unsure{I.(X_i^*\cap\dot X_\beta)}}', 'A sizeable expanded expression is crossed between the newly defined dotted X_i-beta and the final live union X_beta. Fragments of a parenthesis, X strokes, a star, and dotted X remain, but the first factor and several connectors are too heavily crossed to settle the entire C candidate.', 'Xi_equation', confidence='low', kind='omission', error_kind='struck text')
add('(19) / B equation / product point', r'I\underbrace{\dot B_\alpha}', r'\mathbf{I}.\dot B_\alpha', 'I' + B_def, 'The space between the serif I and the dotted B is blank. The dot is above B, not a multiplication point following I. H supplies a point at a separate location where no ink is present.', 'B_equation', kind='text not on the page', error_kind='text not on page')
add('(19) / B under-definition / accent in déf', r'\parallel\mathrm{def}', r'\text{déf}', r'\parallel\text{déf}', 'The detached mark above the small e run is distinct from the two upright relation strokes and the tall f. It matches the accent pattern in the Xi definition on this sheet.', 'B_equation', kind='misread word', error_kind='words', change_C=True, change_H=False)
add('(19) / B under-definition / bracket and placement', between(C, '\\underbrace{\\dot B_\\alpha}', '\\\\\n\\mathcal E_\\alpha'), r'\dot B_\alpha\overset{\text{déf}}{=}B^{*}_\alpha\cap\dot X_\beta', B_def, 'The leader beneath dotted B is a flat bracket with raised ends. Upright relation strokes and déf stand below it, above the starred-B intersection. H relocates the definition inline and turns its upright relation into a horizontal equality.', 'B_equation', kind='insertion or placement', error_kind='insertion placement', change_C=True)
add('(19) / final E entry / comma in beta-alpha', r'(B_{\beta,\alpha},\mathcal E_{\beta,\alpha})', r'(B_{\beta,\alpha},\mathcal E_{\beta\alpha})', r'(B_{\beta,\alpha},\mathcal E_{\beta,\alpha})', 'A short low comma-shaped mark separates the beta loop from alpha in the final E subscript, matching the separator in the B entry immediately before it.', 'E_definition')
add('Conditions heading / extent of underline', r'\uline{Conditions} sur (18)', r'\emph{Conditions sur (18)}', r'\uline{Conditions} sur (18)', 'The single underline ends beneath Conditions. It does not continue under sur or the parenthesized 18.', 'conditions_heading', kind='other', error_kind='other')
add('condition a / undotted X-beta', r'\text{\textcircled{a} Les }\dot X_\beta\text{ disjoints}', r'\text{Les } X_\beta \text{ disjoints}', condition_a, 'There is no source-pen dot above this X. Its upper surroundings were read in the whole page and native half and are also included in the overlapping heading crop; the tight condition-a crop alone has a close upper edge. The dots over X in condition b and the margin note are separate and clear.', 'condition_a', change_C=True, change_H=False)
add('condition b / preposition or punctuation', r'\text{ transverse à }', r'\text{ transverse : }', r'\text{ transverse \unsure{à|:} }', 'Two detached dark marks follow transverse. The upper one is slightly curved and can be a compressed accent-and-letter formation, but the pair also permits colon punctuation. Neither reading is settled by the ink.', 'condition_b', confidence='low', kind='other', error_kind='words')
add('right margin / des', 'le syst. des', 'le syst. induit dans', 'le syst. des', 'After le and syst. there is a compact d-e-s run with one ascender and a long finishing stroke. It does not have the length or separate tall strokes required for induit dans.', 'right_margin', kind='misread word', error_kind='words', marked_in_H=True)
add('right margin / first tuple second entry', r'\unsure{\mathcal E_\beta}', r'(\dot X_\beta,\ldots)', r'$(\dot X_\beta,\unsure{\mathcal E_\beta}$', 'An E/epsilon-like body and a lower beta-like loop are visible at the paper edge after dotted X_beta. The right side is physically cut, so the precise special form remains doubtful; an editorial ellipsis is not the written symbol.', 'right_margin', confidence='low', kind='omission', error_kind='omissions', marked_in_H=True)
add('right margin / missing first closing delimiter and separator', r'$(\dot X_\beta,\unsure{\mathcal E_\beta})$,', r'(\dot X_\beta,\ldots)', r'$(\dot X_\beta,\unsure{\mathcal E_\beta}$', 'The first pair reaches the physical right edge after its second symbol. No closing parenthesis or following comma is visible there. The separate second pair below has its own closing curved stroke, which is retained.', 'right_margin', kind='text not on the page', error_kind='text not on page', change_C=True, marked_in_H=True)
add('right margin / second starred pair', r'$(B_\alpha^*,\mathcal E_\alpha^*)$', r'(\dot B^{\alpha},\dot{\mathcal E}^{\alpha})', r'$(B_\alpha^*,\mathcal E_\alpha^*)$', 'Each main symbol has a small star at upper right and an alpha below. No overhead dot is written above either symbol. Both lower indices and the comma are visible; the closing curve meets the edge.', 'right_margin', marked_in_H=True)
add('right margin / cut terminal word', r'est \unsure{transverse}', r'\uncertain{est transverse}', r'est transv\unsure{e}', 'The visible run supports transv and a final compact blob that may be e; the physical edge cuts off any continuation. No letters r-s-e beyond that edge, and no ellipsis, are supplied.', 'right_margin', confidence='medium', kind='text not on the page', error_kind='text not on page', change_C=True, marked_in_H=True)
add('third condition / circled d', r'\textcircled{d}', '(c) &', r'\text{\textcircled{d}}', 'Inside the circle is a tall upright with a low left bowl and descending exit, plainly d. It is different from the heavily overwritten last label.', 'condition_d')
add('third condition / induced pair without stars', r'\text{par }(B_\alpha^*,\mathcal E_\alpha^*)', r'\text{par }(B_\alpha,\mathcal E_\alpha)', r'\text{par }(B_{\unsure{\alpha}},\mathcal E_{\unsure{\alpha}})', 'No detached star is present after either B or E in this lower annotation. The subscripts are strongly overtraced; alpha is retained with narrow doubts, without reconstructing an underlying correction. Removing the absent stars is based on the empty upper-right spaces, not the mathematical context.', 'induced_definition', confidence='medium', change_C=True, change_H=False, consequential='The written induced pair is unstarred even though nearby boundary pairs are starred; this apparent mismatch is preserved.')
add('third condition / flat lower leader', r'\underbrace{\dot B_{\beta\alpha},\dot{\mathcal E}_{\beta\alpha}}', r'\underbrace{\dot B_{\beta\alpha},\dot{\mathcal E}_{\beta\alpha}}', r'\underline{\dot B_{\beta\alpha},\dot{\mathcal E}_{\beta\alpha}}', 'The leader under the two dotted entries is a shallow continuous bracket without a central cusp, above the two-line annotation. It resembles the other flat definition brackets on this sheet.', 'condition_d', kind='drawing or diagram', error_kind='drawings and diagrams', change_C=True)
add('third condition / dotted target E', r'(X_\beta,B_{\beta,\alpha},\dot{\mathcal E}_{\beta,\alpha})', r'(X_\beta,B_{\beta,\alpha},\mathcal E_{\beta,\alpha})', r'(X_\beta,B_{\beta,\alpha},\dot{\mathcal E}_{\beta,\alpha})', 'A distinct round point sits above the target E. It is separate from the letter body and is as dark as the surrounding writing. Both commas in the beta-alpha subscripts are retained.', 'condition_d')
add('last condition / overwritten circled letter', r'\textcircled{\unsure{c}}', '(d) &', r'\textcircled{\unsure{c|d}}', 'The circled letter has an open upper c-like curve over a heavy lower upright/loop. The superposition does not disclose a secure last layer. c remains the first candidate, with d a visible alternative; no alphabetical ordering is imposed.', 'inserted_c_label', confidence='low', kind='other')
add('conditions / scope of left brace and (20)', between(C, '(20)\\quad\\left\\{', '\n\\margin{'), '(20)\\quad', left_brace, 'The left stroke starts beside b, continues down the d row and the last condition, and has its mid-height loop beside the handwritten (20). It does not begin beside a. H describes this scope in its positional note, so no H content error is assigned here.', 'conditions_braces', kind='drawing or diagram', error_kind='drawings and diagrams', change_C=True, change_H=False)
add('conditions / right brace joining a and b', '[absent]', '[absent]', right_brace, 'A separate right brace spans a and b and meets the two-shaft rightward implication arrow. C retains the arrow in a margin macro but loses the joining brace. H records this brace in its positional note.', 'right_margin', kind='drawing or diagram', error_kind='drawings and diagrams', change_C=True, change_H=False)
add('conditions / separate curved relocation leader', '[absent]', '[absent]', '% Separate curved leader: from the lower-left edge of circled d, down between\n% the left brace and the labels, then right beneath the last circled label.', 'The leader begins at the lower-left edge of circled d, runs down separately to the right of the grouping brace, and curves right below the last circled label to a visible arrowhead. Neither witness represents this separate leader. Its geometry is recorded in a TeX comment and in the notes, as instructed by the editor; no running text is drawn.', 'conditions_braces', kind='drawing or diagram', error_kind='drawings and diagrams', change_C=True)
add('lower-left foliation', r'\margin{32}', '[absent]', r'\margin{32}', 'Two thin grey digits at the lower left read 32: an open double curve followed by a curved 2 with a long foot. They are distinct in weight from the authorial 12 at the head.', 'margin32', kind='omission', error_kind='omissions')

marks = []
def mark(m, context, decision, reading, evidence, crop, confidence):
    marks.append(dict(mark=m, context=context, decision=decision, reading=reading, evidence=evidence, crop=cfile(crop), box=cbox(crop), confidence=confidence))

mark(r'\unsure{\mathcal E_\beta}', r'\dot X_\beta},\n\unsure{\mathcal E_\beta}', 'undecided', r'\unsure{\mathcal E_\beta}', 'The additional special E/epsilon-like body and lower beta are real ink, but crowded overtracing prevents a secure exact form.', 'opening_dotX_pair', 'low')
mark(r'\unsure{I}', r'\deleted{\unsure{I}}\coprod_\beta C(p_\beta)', 'undecided', r'\unsure{I}', 'A crossed upright with serif-like traces survives before the lower coproduct, but the underlying full letter is not plain.', 'cone_formula', 'low')
mark(r'\unsure{X_i=I.\dot X_i}', r'\text{ est donné par }\n\deleted{\unsure{X_i=I.\dot X_i}}', 'undecided', Xi_struck, 'Most letter bodies can be separated from the strike, but the point after I and the newly recorded under-bracket annotation remain unresolved. This is a narrowed doubt, not a complete resolution of the struck formula.', 'Xi_cancelled_first_complete', 'low')
mark(r'\unsure{X_i}', r'\deleted{\unsure{X_i}}\quad X_i&=', 'first', r'\deleted{X_i}', 'The two X diagonals, short lower right i continuation, and separate index dot are distinguishable despite the cancellation.', 'Xi_equation', 'high')
mark(r'\unsure{\cup}', r'X_i^*\deleted{\unsure{\cup}}', 'undecided', r'\unsure{\cup}', 'The small heavily crossed rounded form could be a cup; the crossing obscures a secure outline.', 'Xi_equation', 'low')
mark(r'\unsure{i\in I_\beta}', r'\beta\le i\\\deleted{\unsure{i\in I_\beta}}', 'undecided', r'\unsure{i\in I_\beta}', 'The old lower limit is covered by strike and nearby replacement ink. The full sequence is not recoverable letter by letter.', 'Xi_equation', 'low')
mark(r'\unsure{I.(X_i^*\cap\dot X_\beta)}', r'\deleted{\unsure{I.(X_i^*\cap\dot X_\beta)}}\cup X_\beta', 'undecided', r'\unsure{I.(X_i^*\cap\dot X_\beta)}', 'Parenthesis and X-shaped remnants are visible, but the initial factor and connectors remain buried in the zigzag cancellation.', 'Xi_equation', 'low')
mark(r'\unsure{\mathcal E_\beta}', r'le syst. des $(\dot X_\beta,\unsure{\mathcal E_\beta})$', 'undecided', r'\unsure{\mathcal E_\beta}', 'The special E/epsilon-like body and beta-shaped lower loop meet the physical edge. The exact symbol form is unresolved and the invisible closing delimiter is not supplied.', 'right_margin', 'low')
mark(r'\unsure{transverse}', r'est \unsure{transverse}', 'other', r'transv\unsure{e}', 'The page shows only transv and a possibly e-shaped terminal blob before the cut edge. The longer word is not visible. This replaces an unsupported completion while retaining uncertainty on the last visible letter.', 'right_margin', 'medium')
mark(r'\unsure{c}', r'\inserted{\textcircled{\unsure{c}} Les', 'undecided', r'\unsure{c|d}', 'Open upper curve and heavy lower upright/loop are superposed. The final layer is not separable; c and d remain candidates.', 'inserted_c_label', 'low')

# Keep short contexts as actual contiguous source text, including real newlines.
for entry, match in zip(marks, re.finditer(r'\\(?:unsure|illegible)\{', C)):
    original_mark = macro(C, match.group(0), match.start())
    assert original_mark == entry['mark']
    entry['context'] = C[max(0, match.start()-46):match.start()+len(original_mark)+38]

inventory = []
def inv(e, k, p, w, hand='his hand'):
    inventory.append(dict(element=e, kind=k, position=p, first_words_or_objects=w, sheet_kind='text', hand=hand, transcribed='yes'))

inv('N01', 'margin note', 'upper left, x45–111 y43–99', '12')
inv('T01', 'text', 'above first display, x490–935 y25–112', 'syst. de cylindres-bord / transversaux')
inv('D01', 'display', 'top, parenthesized (18), two rows with definitions below the first row', '(18) X*, dotted-X pair, starred boundary pair, indexed X*, X_beta, boundary pair, p_beta map')
inv('I01', 'insertion', 'below initial X* in (18)', 'upright relation / X minus open-ring T_I0')
inv('I02', 'insertion', 'below first dotted X_beta in (18)', 'upright relation / dotted T_beta')
inv('I03', 'insertion', 'below starred boundary pair in (18)', '(B_alpha,E_alpha)|X* under a flat leader')
inv('I04', 'insertion', 'below X_i* in (18)', 'upright relation / X_i intersect X*')
inv('I05', 'insertion', 'below last pair in first row of (18)', '(B_alpha,E_alpha)|X_beta under a cusped brace')
inv('T02', 'text', 'right of second row of (18)', 'de la façon suivante :')
inv('M01', 'margin note', 'left of the start of (19), slanting upward', 'les dotted X_beta disjoints')
inv('D02', 'display', 'middle page, long left brace labelled (19)', 'hat X; T_beta; X_beta pour beta in I0; X_i; B_alpha; E_alpha')
inv('I06', 'insertion', 'below C(p = coproduct p_beta)', 'coproduct_beta C(p_beta)')
inv('S01', 'deletion', 'immediately before I06 lower coproduct', 'doubtful I under crossing')
inv('S02', 'deletion', 'after est donné par, first cancelled Xi equation', 'X_i=I [point doubtful] dotted X_i')
inv('S03', 'deletion', 'below final dotted X_i of S02', 'flat bracket and crossed upright-relation/def-like annotation')
inv('S04', 'deletion', 'start of next Xi equation', 'X_i')
inv('S05', 'deletion', 'after X_i* and before the live union', 'doubtful cup')
inv('S06', 'deletion', 'below the live union limits', 'doubtful i in I_beta')
inv('S07', 'deletion', 'inside the large parenthesis after the newly defined dotted X_i-beta', 'doubtful I.(X_i* intersect dotted X_beta)')
inv('I07', 'insertion', 'beneath dotted X_i-beta in the live equation', 'upright relation déf / X_i* intersect dotted X_beta')
inv('I08', 'insertion', 'beneath dotted B_alpha in the B equation', 'upright relation déf / B_alpha* intersect dotted X_beta')
inv('T03', 'text', 'lower-page heading', 'Conditions sur (18), underline under Conditions alone')
inv('D03', 'display', 'lower-page conditions in source order a, b, d, last overwritten label', 'Les X_beta disjoints; Chaque dotted X_beta; map of triples; Les X_i*')
inv('G01', 'drawing', 'left side of lower conditions', 'left brace labelled (20), beginning at b and ending beside the last condition')
inv('G02', 'drawing', 'right side of conditions a and b', 'right brace joining a and b; two-shaft implication arrow to margin')
inv('M02', 'margin note', 'right edge beside a–d', 'le syst. des (dotted X_beta, doubtful E_beta / (B_alpha*,E_alpha*) est transv[e doubtful]')
inv('I09', 'insertion', 'beneath the two dotted structure entries in the source of the d map', 'induit sur dotted X_beta / par (B_alpha,E_alpha), both subscripts overtraced')
inv('I10', 'insertion', 'last line at foot of sheet', 'overwritten circled label, Les X_i* transverses aux ...')
inv('G03', 'drawing', 'curved leader from circled d, down between left brace and labels, then right beneath the last label', 'one curved right-pointing relocation arrow; geometry recorded precisely in notes')
inv('M03', 'margin note', 'lower left, x18–85 y2290–2348', '32', 'thin grey foliation; attribution uncertain')

doubts = [
    dict(place='(18), first pair second entry', reading=r'\unsure{\mathcal E_\beta}', alternatives='Special E/epsilon-like body and beta-shaped subscript are cramped and overtraced; no alternate alphabet is established.', confidence='low'),
    dict(place='(19), crossed sign before lower coproduct', reading=r'\deleted{\unsure{I}}', alternatives='Serif I is possible; the crossing prevents secure recovery.', confidence='low'),
    dict(place='(19), first cancelled Xi equation', reading=Xi_struck, alternatives='Main X_i=I and dotted X_i bodies are legible; an independent multiplication point and the exact lower annotation remain uncertain.', confidence='low'),
    dict(place='(19), live Xi name', reading=r'\unsure{X_i|\bar X_i}', alternatives='Plain X_i favored; pale overhead streak may be a thin bar or background/show-through.', confidence='low'),
    dict(place='(19), cancelled cup', reading=r'\deleted{\unsure{\cup}}', alternatives='Rounded remnants are compatible with cup but not decisive.', confidence='low'),
    dict(place='(19), cancelled old union limit', reading=r'\deleted{\unsure{i\in I_\beta}}', alternatives='The exact old index sequence remains obscured.', confidence='low'),
    dict(place='(19), cancelled expanded term', reading=r'\deleted{\unsure{I.(X_i^*\cap\dot X_\beta)}}', alternatives='First factor and several connecting signs remain buried in cancellation.', confidence='low'),
    dict(place='condition b, after transverse', reading=r'\unsure{à|:}', alternatives='Compressed accented preposition or two-point punctuation.', confidence='low'),
    dict(place='right margin, first tuple second symbol', reading=r'\unsure{\mathcal E_\beta}', alternatives='E/epsilon-like body with beta at the cut edge; no right delimiter is visible.', confidence='low'),
    dict(place='right margin, final visible word fragment', reading=r'transv\unsure{e}', alternatives='The final small blob may be e; anything after it is outside the physical page and is not completed.', confidence='medium'),
    dict(place='condition d, induced pair subscripts', reading=r'(B_{\unsure{\alpha}},\mathcal E_{\unsure{\alpha}})', alternatives='Alpha is the leading candidate at both strongly overtraced indices; the underlying correction is not recoverable. Neither main letter has a star.', confidence='medium'),
    dict(place='last circled label', reading=r'\textcircled{\unsure{c|d}}', alternatives='Upper open curve and lower loop/upright overlap; the final layer cannot be assigned securely.', confidence='low'),
]

notes = [
    'The page reports a reconstruction from the data (18): a space with a hat is assembled from X* and cones of the maps p_beta; formulas then specify T_beta, the X strata, boundary sets B_alpha, and the associated E structures. It lists disjointness and transversality conditions below. These are reported manuscript claims, not results proved or checked in this reading.',
    'No mathematical check event was performed. Visual comparison, symbol comparison, and source collation are reading operations only; check_events is intentionally empty.',
    'Whole page and both native halves were each viewed once. Every created zoom was viewed. There are 26 distinct cropped places and 27 saved crop images: Xi_cancelled_first clipped its lower annotation, and Xi_cancelled_first_complete is the single complete replacement attempt for that same unsettled place. The initial image is retained in the crop register.',
    'Own page number 12 is in the dark main hand at upper left. The thin grey lower-left foliation is 32; its attribution is uncertain and it is not identified as the author’s own numbering.',
    'In (18), (X_beta) is indexed by beta in I, without a small zero. The other relevant families and definitions visibly use I_0. This difference is retained without correction.',
    'The E/epsilon-like notation is rendered with the established E macro. The first tuple and the right-edge instance remain doubtful in form; no new alphabet distinction is inferred. C(p) is retained as an ordinary C: the handwritten open curve does not establish a separate ordinary-versus-calligraphic alphabet. Likewise the heavy serif I is not treated as a distinct bold alphabet.',
    'Under-definitions remain stacked. The pair under X*, the lower cone formula, and the other attached definitions are not introduced by an invented avec. Three straight shallow leaders and the leader in condition d are encoded by underline/underset; their ends curl slightly upward. The upper system brace and the last tuple/ cone lower braces have actual cusps.',
    'The first cancelled Xi attempt contains a bracket and a crossed lower annotation omitted by both witnesses. Its upper letter bodies can be separated from the zigzag, but the multiplication point and lower label are uncertain. No continuation is reconstructed from the mathematical role of that definition.',
    'The right-margin first tuple is physically cut after its second symbol, so its closing parenthesis and following separator are not supplied. The second tuple has a visible closing curve. The final word is transv plus an uncertain e-like blob, not a completed transverse and not an added ellipsis.',
    'Condition a has a plain X_beta, whereas nearby occurrences have distinct dots. The induced pair under condition d is bare B/E without stars, although other pairs are starred. Both apparent asymmetries are retained literally.',
    'Condition labels remain in physical source order: a, b, d, and a heavily overwritten c-or-d. No alphabetical renumbering is applied. The right brace groups a and b and feeds the margin implication; the left brace labelled (20) begins beside b and extends to the last condition.',
    'A separate curved leader leaves the lower-left edge of the circled d at approximately (440,2040), descends around x410 between the left brace and the labels, bends right near y2325, and ends in a right-pointing head around (535,2335), beneath the last circled label. It is distinct from the long left grouping brace. Its geometry is recorded here under the editor’s instruction; the main running text remains ordinary LaTeX in source order.',
    'The map arrow in condition d has a nearly horizontal shaft and only a tiny blunt upward terminal return; the established single-return arrow habit supports retaining the arrow. The p_beta arrow in (18) has a much more explicit head. No paired arrowhead is required.',
    'line_count counts 25 main reading lines, including the upper two-line annotation and the stacked below-formula annotations, but excludes foliation and the two independent margin notes. Inventory entries separately account for every attached annotation, cancellation, and leader.',
]

notation = [
    dict(form=r'X^*=X\setminus\mathring T_{I_0}', meaning_or_shape='The page gives this relation vertically, with a hollow ring above T and a small subscript zero on the serif I.', places='(18), under initial X*'),
    dict(form=r'\dot X_\beta,\dot T_\beta,\dot X_{i\beta},\dot B_\alpha', meaning_or_shape='Distinct overhead dots; the dot can be broad or slightly elongated. The source omits a dot on X_beta in condition a.', places='(18), (19), condition b and d, final condition; exception condition a'),
    dict(form=r'\parallel\text{déf}', meaning_or_shape='Two upright relation strokes with a small accented déf label, above a lower intersection expression.', places='live Xi and B under-definitions in (19)'),
    dict(form=r'I, I_0, I^*', meaning_or_shape='Serif capital I; top bar may be detached. The zero is a small closed loop and the star can be abbreviated to a compact three-pronged form.', places='(18), union limits and products in (19), final condition'),
    dict(form=r'\widehat X', meaning_or_shape='Clear small caret over the first X of (19). This is distinct from the faint possible bar over the later live X_i.', places='first equation of (19)'),
    dict(form=r'\unsure{X_i|\bar X_i}', meaning_or_shape='Short pale grey line over live X_i is not securely source ink; plain form is the first candidate.', places='live Xi equation in (19)'),
    dict(form=r'C(p_\beta)', meaning_or_shape='Open C-shaped cone notation; no visibly distinct calligraphic alphabet is established from this page.', places='hat-X equation and T_beta equation in (19)'),
    dict(form=r'\mathcal E_\alpha,\mathcal E_{\beta,\alpha}', meaning_or_shape='The E-like body is frequently epsilon-shaped. Commas in beta-alpha subscripts are independent short low strokes.', places='boundary tuples and final E definition'),
    dict(form=r'\longrightarrow', meaning_or_shape='An arrow may have only a tiny terminal return; the condition-d arrow is much less pronounced than the p_beta arrow.', places='(18) p_beta map; condition d map'),
]

abbreviations = [dict(form='syst.', expansion='système'), dict(form='déf', expansion='définition; retained as an unexpanded label without supplied stop'), dict(form='def', expansion='Possible definition label in the cancelled annotation; exact reading and accent remain uncertain')]

hand_log = [
    dict(habit='The dot of a small i can be detached to the right of a short foot joined to X.', places='(18) X_i*, both cancelled/live Xi attempts in (19), final condition', consistent='All clearly legible i indices on this sheet; cancellations can obscure the foot.', witness_errors='The initial cancelled Xi can be read more fully than C’s doubt; the live overhead bar remains unresolved.'),
    dict(habit='Small stars vary from full crossed rays to compact three-pronged shapes resembling a small alpha or 2.', places='upper B/E pair, I* index, B_alpha* in (19), final B/E pair', consistent='The same variation occurs at clearly star-valued positions; no numeral is inferred from the compact shape.', witness_errors='No independent star/numeral error established; C’s supplied stars in the induced pair are absent ink, not this variant.'),
    dict(habit='Capital I has a serif top and foot, with the top sometimes detached; zero may be attached as a small closed loop.', places='all I0 indices and the two I product factors', consistent='All live occurrences; heavily struck I-like sign under the cone remains doubtful.', witness_errors='No alphabet change justified by H’s bold I. H adds an unsupported multiplication point after I in the B equation.'),
    dict(habit='E-like neighborhood symbols often have an epsilon-shaped open body.', places='first tuple, final E definition, right margin, lower conditions', consistent='Most live entries are readable; first tuple and cut-margin instances remain cramped exceptions.', witness_errors='H omits the first tuple’s second entry and substitutes an ellipsis in the cut margin.'),
    dict(habit='Flat under-definition brackets with curled ends are distinct from braces with a central cusp.', places='starred pair, Xi definition, B definition, condition-d source; contrasting cusp under cone and final upper tuple', consistent='Distinction is visible in all listed instances.', witness_errors='C and sometimes H encode the flat leaders as underbraces; H relocates several stacked definitions inline.'),
    dict(habit='A defining relation written as two upright strokes stays vertical.', places='three upper identities and two live under-definitions', consistent='All five clear live vertical relations on this sheet.', witness_errors='H turns these into horizontal inline equalities.'),
    dict(habit='Small detached accent marks may be nearly point-shaped.', places='déf in Xi/B under-definitions; défini in final line of (19)', consistent='Both live déf labels have a separate dark mark; cancelled lower label is not settled.', witness_errors='C omits the accents in both live déf labels.'),
    dict(habit='One short terminal return may carry an arrowhead.', places='condition-d map, contrasted with explicit p_beta head', consistent='The two map arrows differ in prominence; no contrary new rule inferred.', witness_errors='No change required to either witness’s map arrow.'),
]

second_boxes = []
def sb(kind, coords, reading, reason):
    second_boxes.append(dict(box=f'b{len(second_boxes)+1:02d}', kind=kind, coords=coords, reading=reading, reason=reason))

sb('handwritten number', [45,43,111,99], r'\mspage{12}', 'The handwritten page number at the head.')
sb('insertion|doubt formula|handwritten number|C/H word difference|low-confidence departure', [130,15,1682,485], top_with_prose, 'The whole displayed tuple and its attached definitions/upper annotation, including its doubtful entry, handwritten label and numerical indices, together with the adjacent prose comparison.')
sb('margin note', [45,510,310,646], r'\margin{les $\dot X_\beta$ disjoints}', 'The complete left-margin annotation.')
sb('insertion|struck passage|doubt formula', [320,505,1135,775], hat_formula + '\\\\\n' + T_formula, 'The whole first equation with its lower annotation and crossed sign; the adjacent complete T equation is in the same box.')
sb('handwritten number', [330,775,1110,885], r'X_\beta&\quad\text{pour }\beta\in I_0\quad\text{clair}.', 'The complete line containing a numerical subscript.')
sb('struck passage|doubt formula|low-confidence departure', [330,860,1540,1105], Xi_intro, 'The whole first Xi statement and its cancelled formula, including the lower bracketed annotation.')
sb('insertion|struck passage|doubt formula|handwritten number|C/H word difference|low-confidence departure', [490,970,1682,1295], Xi_formula, 'The whole replacement Xi equation, its numerical index, lower definition, and all nearby cancelled components.')
sb('handwritten number', [140,1080,305,1240], '(19)', 'The handwritten display label at the long left brace.')
sb('insertion|handwritten number|C/H word difference', [390,1235,963,1528], B_formula, 'The complete B equation and lower defining annotation, including the numerical index and abbreviation comparison.')
sb('handwritten number', [325,1735,910,1830], r'\uline{Conditions} sur (18)', 'The heading with its parenthesized numerical reference and underline extent.')
sb('doubt formula|C/H word difference|low-confidence departure', [450,1868,1495,1990], condition_b, 'The complete condition containing the two possible readings after transverse.')
sb('margin note|doubt formula|C/H word difference|low-confidence departure', [1480,1775,1682,2142], right_note, 'The complete visible right-margin note, including both tuples and the cut final word.')
sb('insertion|doubt formula|low-confidence departure', [430,1975,1495,2230], condition_d + '\n' + r'\text{est transverse}', 'The whole map condition with its attached two-line annotation and following predicate.')
sb('handwritten number|insertion', [270,1800,550,2350], '(20)', 'The handwritten label and the adjacent grouping stroke and curved relocation leader; the numbered reading itself is fully within the box.')
sb('insertion|doubt formula|handwritten number|low-confidence departure', [445,2190,1682,2348], final_condition, 'The whole final condition, including its circled label and numerical subscript.')
sb('margin note|handwritten number', [18,2290,85,2348], r'\margin{32}', 'The complete thin lower-left foliation.')

crop_register = []
for name, info in crops.items():
    crop_register.append(dict(file=cfile(name), box=info['box'], rotation_degrees=info['rotation_degrees'], viewed=True, distinct_place=('Xi_cancelled_first' if name == 'Xi_cancelled_first_complete' else name), note=('Initial attempt clips the lower cancelled annotation.' if name == 'Xi_cancelled_first' else 'Complete replacement for the same unsettled place.' if name == 'Xi_cancelled_first_complete' else '')))

data = dict(scan=33, reader='reader_a', line_count=25, changes=changes, marks=marks, inventory=inventory, doubts=doubts, notes=notes, check_events=[], notation=notation, abbreviations=abbreviations, hand_log=hand_log, second_boxes=second_boxes, crops=crop_register, crop_count=27, distinct_crop_places=26)

# Static integrity only: no TeX compilation and no mathematical proof test.
issues = []
for row in changes:
    if not (ROOT / 'crops' / row['crop']).is_file():
        issues.append('missing crop: ' + row['crop'])
    if norm(row['final']) not in norm(tex):
        issues.append('final not in TeX: ' + row['place'])
    for label, source in [('C', C), ('H', H)]:
        q = row[label]
        if q != '[absent]' and norm(q) not in norm(source):
            issues.append(label + ' quote not in source: ' + row['place'] + ' / ' + repr(q))
for row in second_boxes:
    # Adjacent complete formula rows may be separated in the source by alignment wrappers.
    pieces = row['reading'].split('\\\\\n') if row['box'] == 'b04' else [row['reading']]
    if row['box'] == 'b13':
        pieces = [condition_d, r'\text{est transverse}']
    if row['box'] == 'b02':
        pieces = [top_display, 'de la façon suivante :']
    for q in pieces:
        if norm(q) not in norm(tex):
            issues.append('second reading not in TeX: ' + row['box'])
    x0,y0,x1,y1 = row['coords']
    if not (0 <= x0 < x1 <= 1682 and 0 <= y0 < y1 <= 2361):
        issues.append('bad box: ' + row['box'])

def extract_marks(s):
    result = []
    for m in re.finditer(r'\\(?:unsure|illegible)\{', s):
        result.append(macro(s, m.group(0), m.start()))
    return result

if Counter(extract_marks(C)) != Counter(m['mark'] for m in marks):
    issues.append('C mark inventory differs')

def brace_balance(s):
    level = 0
    for line in s.splitlines():
        line = re.split(r'(?<!\\)%', line)[0]
        for i,ch in enumerate(line):
            if ch not in '{}':
                continue
            n = 0
            j = i-1
            while j >= 0 and line[j] == '\\':
                n += 1
                j -= 1
            if n % 2:
                continue
            level += (1 if ch == '{' else -1)
            if level < 0:
                return False
    return level == 0

if not brace_balance(tex):
    issues.append('unbalanced TeX braces')
for m in marks:
    if not (ROOT / 'crops' / m['crop']).is_file():
        issues.append('missing mark crop')
    if m['context'] not in C:
        issues.append('mark context not in source')
allowed_kinds = {'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
if any(c['kind'] not in allowed_kinds for c in changes):
    issues.append('invalid change kind')

data['validation'] = dict(complete=not issues, all_crops_viewed=True, source_marks=10, return_marks=len(marks), tex_braces_balanced=brace_balance(tex), compiled=False, issues=issues)
(OUT / '150_scan033.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(changes=len(changes), marks=len(marks), inventory=len(inventory), doubts=len(doubts), second_boxes=len(second_boxes), crops=len(crop_register), distinct_crop_places=26, issues=issues), ensure_ascii=False, indent=2))
