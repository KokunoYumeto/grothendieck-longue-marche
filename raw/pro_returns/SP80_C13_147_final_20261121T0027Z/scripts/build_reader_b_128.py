#!/usr/bin/env python3
"""Build reader_b's scan128 return from this page's packet only.

The readings were made visually, without OCR or compilation.  This builder is
retained with the reader return so that the report and proposed text are
reproducible; it does not read or modify any other page or any global edition.
"""
from pathlib import Path
import json
import re

ROOT = Path('/workspace/scratch/12caffedf246')
PACKET = ROOT / 'packets/147_scan128'
OUT = ROOT / 'edition/reports'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
CROPS = {
    Path(x['crop']).stem.removeprefix('147_scan128_'): x
    for x in map(json.loads, (OUT / '147_scan128_crops.jsonl').read_text().splitlines())
}

def between(source, first, last):
    start = source.index(first)
    return source[start:source.index(last, start) + len(last)]

hook = r'\text{\tikz[x=.07cm,y=.07cm,baseline=0pt]{\draw[line width=.3pt] (0,0) .. controls (2.1,.4) and (2.9,.4) .. (3,2);}}'
annotation = r'''\substack{\text{ens des ``\deleted{\illegible{1}}\inserted{drapeaux} de}\\
\text{type }d_*\text{'' de l'ens fini}\\
I_{d_0}=[1,d_0]\cap\mathbb N\quad''' + hook + '}'
formula203 = r'\tag{203}\Delta_r=[0,r]\cap\mathbb N'
formula204 = r'''\tag{204}
\underset{\inserted{\substack{\text{ou}\\D_{\Delta_r}}}}{\mathcal D_r}
=\overset{\inserted{D_{\Delta_r}}}{\deleted{\unsure{D_{\Delta_I}|D_{\Delta_r}}}}
=\coprod_{\substack{(d_0,\ldots,d_r)\in\mathbb N^r\\d_0>d_1\cdots>d_r}}
D_{d_0,d_1,\ldots,d_r}'''
formula205_main = r'''D_{d_*}=D^{!}_{d_0}\wedge_{(\mathfrak S_{d_0})_{D_{d_0}}}
\underbrace{\mathcal P_{d_*}\bigl(\deleted{\unsure{[1,d_0]}}I_{d_0}\bigr)}'''
formula205 = '\\tag{205}\n' + formula205_main + '_{\n' + annotation + '}'

proposed = r'''\scanpage{128}
\mspage{63}
Il faut introduire encore les espaces analytiques
de drapeaux $D_{d_0,d_1,\ldots,d_r}$ pour $d_0\geq \unsure{d_2|d_1}\geq\cdots\geq d_r\geq0$
leur somme est notée $D_{\Delta_r}$, où $\Delta_r$ désigne
maintenant l'ens. ordonné
\[
''' + formula203 + r'''
\]
ou simplexe ordonné type de dim $r$. Cette notation
$D_{\Delta_r}$ est compatible avec la notation $D_J$ pour $J$
ens. fini ordonné ayant un plus petit élément.
Alors $D_{I_r}$ dépend fonctoriellement de façon
contravariante en $I_r$, pour les applications
croissantes, entre simplexes, donc on a un
espace analytique $1/2$-simplicial, qu'on désigne par
$\mathcal D_*$, donc
\[
''' + formula204 + r'''
\]
\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}
La composante $D_{d_*}=D_{d_0,d_1,\ldots,d_r}$ est
un \unsure{revêt} étale fini de $D_{d_0}$, s'identifiant
à
\[
''' + formula205 + r'''
\]
on désigne par $D^*_{d_0,d_1,\ldots,d_r}$ l'image inverse
de $D^*_{d_0}$, qui est donc le complémentaire
de l'image inverse $\Delta_{d_0-d_r}$ du diviseur
$\Theta_{d_0}$ sur $D_{d_0}$. On peut bien sûr plus simple-
\margin{127}
'''

rows = []
def row(place, c, h, final, evidence, crop, kind, against_c=False,
        against_h=True, marked_h=False, math=False, confidence='high', category='Words'):
    assert not c or c in C, ('C span is not literal', place, c)
    assert not h or h in H, ('H span is not literal', place, h)
    item = CROPS[crop]
    rows.append(dict(place=place, C=c, H=h, final=final, scan_shows=evidence,
                     crop=item['crop'], box=item['box'], confidence=confidence,
                     kind=kind, against_C=against_c, against_H=against_h,
                     marked_in_H=marked_h, math_consequential=math,
                     error_category=category))

row('opening line, after introduire', 'encore', 'ensuite', 'encore',
    'The short word has an initial e loop, low n, open c, rounded o and r/e ending; there is no tall t of ensuite.',
    'encore', 'misread word')
row('opening range, immediately after the first ≥; final punctuation of that range',
    r'$d_0\geq d_1\geq\cdots\geq d_r\geq0$',
    r'$d_0 \geqslant d_1 \geqslant \dots \geqslant d_r \geqslant 0$,',
    r'$d_0\geq \unsure{d_2|d_1}\geq\cdots\geq d_r\geq0$',
    'The small index beneath the second d has a curled or angled upper turn, a dark descending stroke and a low rightward return. It is 2-like, unlike the narrow clear 1 in the preceding D tuple, but retracing prevents certainty. The relation signs have lower bars. There is no comma after the final 0.',
    'initial_range', 'misread symbol or index', against_c=True, math=True,
    confidence='medium', category='Symbols and indices')
row('line 3, leur somme', 'somme', 'réunion', 'somme',
    'After the short s/o beginning, the body has the two low m groups and a final e; it does not have the longer réunion sequence.',
    'somme', 'misread word')
row('line before (203)', "maintenant l'ens. ordonné", "l'ens. ordonné", "maintenant l'ens. ordonné",
    'The full word maintenant is on its own continuation line before l’ens. ordonné. Its letters are not an interlinear addition, and the point after ens is visible.',
    'maintenant', 'omission', category='Omissions')
row('(203), alphabet of N', r'\Delta_r=[0,r]\cap\mathbf N',
    r'\Delta_r = [0,r] \cap \mathbb{N}', r'\Delta_r=[0,r]\cap\mathbb N',
    'The left upright of N is doubled with a narrow white separation; the diagonal and right upright remain distinct. The triangle of Delta and the interval endpoints 0,r are clear.',
    'formula203', 'misread symbol or index', against_c=True, against_h=False,
    math=False, category='Symbols and indices')
row('line after (203), dim r.', r'dim $r$.', r'dim.~$r$.', r'dim $r$.',
    'The dot above the i belongs to the letter; no point follows dim. A separate dark point does follow r.',
    'dim_r', 'text not on the page', category='Text that is not on the page')
row('notation sentence, D_J pour J', r'$D_J$ pour $J$', r'$D_I$ pour $I$', r'$D_J$ pour $J$',
    'Both Js have right-hand stems with leftward terminal returns; the free J has a curved upper turn and a lower hook. They differ from the stem-plus-two-bars I forms lower on this page.',
    'j_notation', 'misread symbol or index', math=True, category='Symbols and indices')
row('end of the ordered-set condition', 'ordonné ayant un plus petit élément.',
    'ordonné, rajoutant une\nplus petite \\uncertain{élément}.', 'ordonné ayant un plus petit élément.',
    'Ayant begins immediately after ordonné, without a comma or the rajout- prefix; its y descends. Un is short and has no terminal e. Petit ends at its t before the separate élément.',
    'ayant', 'misread word', marked_h=True, math=True)
row('Alors D_{I_r}', r'$D_{\unsure{I_r|\Delta_r}}$', r'$D_{\Delta_r}$', r'$D_{I_r}$',
    'The subscript is a straight I with upper and lower bars and a separate small r, not a triangular Delta. The whole D expression and adjacent text were inspected.',
    'ir_depend', 'misread symbol or index', math=True, category='Symbols and indices')
row('contravariante en I_r, pour les applications',
    r'en $\unsure{I_r|\Delta_r}$, pour les applications',
    r'de $\Delta_r$, par les relations', r'en $I_r$, pour les applications',
    'The written preposition is en; I has a straight stem and two bars. Pour has its full rounded ou body. Applications has the two descending p strokes and its longer ending, rather than relations.',
    'ir_applications', 'misread word', math=True)
row('(204), complete display and both insertions',
    between(C, r'\tag{204}', 'D_{d_0,d_1,\\ldots,d_r}.'),
    between(H, '(204)', 'D_{d_0,d_1,\\dots,d_r}\n\\]')[:-3], formula204,
    'The left calligraphic D_r has ou and D_{Delta_r} written on two small lines below it. The old term after the first equals sign is crossed; a main D and dark lower cluster survive, with its exact Delta_I/Delta_r index still uncertain. The replacement D_{Delta_r} is raised above that cancellation and attached there by a curved leader. N has a doubled left upright and exponent r alone. The condition has d_0>d_1 followed directly by the short ellipsis strokes, then >d_r: there is no extra > between d_1 and those strokes. No point follows the right-hand D tuple. H’s note correctly recognizes the raised replacement and the strict inequalities; its missing lower alias and added intermediate > are separate from that editorial explanation.',
    'formula204', 'misread symbol or index', against_c=True, math=True,
    confidence='medium', category='Symbols and indices')
row('cancelled fragment before La composante',
    r'\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}', r'\struck{\ill{}}',
    r'\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}',
    'The strike crosses the complete fragment and ends before La composante. A large D, a small first upright/bowl with a low oval, a comma and final d_r survive. D_{d_0,d_r} is the leading partial reading, but the first index is obscured enough to retain C’s alternative.',
    'cancelled_component', r'readable ink left as \ill{}', marked_h=True,
    math=True, confidence='medium', category='Readable ink left as illegible')
row('short form before étale fini', 'revêtement', 'revêtement', r'\unsure{revêt}',
    'Only revê followed by a crowded t-like upright/cross-stroke or raised terminal form is separable. There are no distinct m,e,n letters spelling out ment. The exact abbreviated ending is left doubtful; revêtement belongs only in the expansion list.',
    'revetement', 'abbreviation expanded or spelling modernised', against_c=True,
    confidence='medium', category='Abbreviations expanded, spelling modernised')
row('right end of the finite-cover sentence', "s'identifiant", "s'identifie", "s'identifiant",
    'The tall f descends; after it there is an extended i/a/n body and a terminal t-like stroke, not merely the short ending of s’identifie.',
    'sidentifiant', 'misread word')
row('(205), torsor exponent, group placement and flag-set symbol',
    between(C, r"D_{d_*}=D'_{d_0}", r'I_{d_0}\bigr)}'),
    between(H, r'D_{d_*} = D^{!}_{d_0}', r'I_{d_0})}'), formula205_main,
    'The exponent over D has a separate upright and a detached dot: it is !, not a prime. The broad curled group letter is S, and the parenthesized group with base D_{d_0} is below the wedge, not above it. The flag symbol has an angular but closed P bowl and a stem, not an F crossbar. The crossed old argument retains brackets and d_0; the first 1/comma is obscured, so its existing doubt remains. The following live I_{d_0} has a stem and two bars.',
    'formula205', 'misread symbol or index', against_c=True, math=True,
    category='Symbols and indices')
row('three-line annotation under the flag factor of (205)',
    between(C, r'\substack{\text{ens des', r'I_{d_0}=[1,d_0]\cap\mathbf N}}'),
    between(H, r'\marginal{ens.', r'mot biffé (\ill{}).}'), annotation,
    'The annotation is attached to the underbrace. Both ens forms have no point. Its quotation marks are paired high strokes rather than angle brackets. Drapeaux is inserted above a separately crossed word whose surviving body cannot be recovered; de follows to the right. The final N has the same doubled upright as the other two Ns. A distinct short curved stroke at the lower right runs rightward and then upward; its ink is reproduced literally, without assigning a certain closing-parenthesis or bracket interpretation. H explicitly mentions the cancelled word and interlinear drapeaux in its note; that recognition is not counted as an omission of the revision.',
    'flag_note', 'insertion or placement', against_c=True, marked_h=True,
    math=False, confidence='medium', category='Insertions put in the wrong place')
row('opening of final paragraph', 'on désigne par', 'On désigne par', 'on désigne par',
    'The first o is a small low stroke at the prose baseline, with no capital-height loop; désigne and par follow plainly.',
    'on_designe', 'misread word')
row('complement sentence before Delta', "de l'image inverse", "d'un diviseur", "de l'image inverse",
    'The line begins de followed by l’ and the long image sequence with its g descender, then inverse. The later du diviseur remains a separate phrase.',
    'image_inverse', 'misread word', math=True)
row('Delta subscript in final paragraph', r'$\Delta_{d_0- d_r}$', r'$\Delta_{d_0 \dots d_r}$',
    r'$\Delta_{d_0-d_r}$',
    'Delta is an angular three-sided glyph. Between d_0 and d_r there is one continuous horizontal dash, not a series of dots. No substitution of a tuple index is made from the surrounding mathematics.',
    'image_inverse', 'misread symbol or index', math=True, category='Symbols and indices')
row('last word at the right scan edge', r'\unsure{simple-|simple}', r'simpl\supplied{ement}', 'simple-',
    'The visible word ends in the compressed l/e group followed by a separate short dark horizontal terminal stroke immediately before the right edge. No further letters are visible. H labels its ement completion as supplied; the present reading retains the visible ending and hyphen and makes no claim about continuation beyond this scan.',
    'simple', 'omission', marked_h=True, category='Omissions')
row('pencil foliation at lower left', r'\margin{127}', '', r'\margin{127}',
    'The pale pencil sequence has a sloping entry and upright 1, curved upper/downward/lower sweep of 2, and a tall 7 with a transverse bar. It is separate from the dark main hand and from author page 63.',
    'footer127', 'omission', category='Omissions')

decisions = []
def decision(id, reading, ink, crop):
    c = CROPS[crop]
    decisions.append(dict(id=id, decision='first', reading=reading, ink=ink,
                          crop=c['crop'], box=c['box'], confidence='high'))
decision('M1279', r'I_r', 'Straight stem and upper/lower bars of I; separate r. The adjacent full D expression was read, not the isolated index alone.', 'ir_depend')
decision('M1280', r'I_r', 'The free I again has a stem with two bars, distinct from the closed Delta triangles elsewhere on this same page.', 'ir_applications')
decision('M1281', r'\mathfrak S_{d_0}', 'The broad curled S form is visible beneath the wedge; the whole (205) expression, group base, exponent, flag symbol and cancelled argument were read together.', 'formula205')
decision('M1282', 'simple-', 'A small dark horizontal terminal stroke is separated from the l/e ending and visible before the right black scan edge.', 'simple')

inventory = []
def inv(kind, position, start, hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}', kind=kind,
                          position=position, first_words_or_objects=start,
                          sheet_kind='text', hand=hand, transcribed='yes'))
inv('margin note', 'top centre, above opening prose', '63')
inv('text', 'upper opening block, above (203)', 'Il faut introduire encore les espaces analytiques')
inv('display', 'upper quarter, left numbered (203)', formula203)
inv('text', 'between (203) and (204)', 'ou simplexe ordonné type de dim r.')
inv('display', 'middle of sheet, numbered (204)', formula204)
inv('insertion', 'below the left calligraphic D_r of (204), two short lines', r'ou / D_{\Delta_r}')
inv('deletion', 'first term after the first equality of (204)', r'\deleted{\unsure{D_{\Delta_I}|D_{\Delta_r}}}')
inv('insertion', 'above that cancelled term, with a curved attachment leader', r'D_{\Delta_r}')
inv('deletion', 'left edge of the La composante line', r'\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}')
inv('text', 'between (204) and (205), with isolated à on a short line', 'La composante')
inv('display', 'lower middle, numbered (205)', formula205)
inv('deletion', 'inside parentheses in the flag factor of (205)', r'\deleted{\unsure{[1,d_0]}}')
inv('margin note', 'three lines under the brace on the right of (205)', annotation)
inv('deletion', 'old word after ens des, under interlinear drapeaux', r'\deleted{\illegible{1}}')
inv('insertion', 'above that cancelled word in the annotation', 'drapeaux')
inv('drawing', 'small detached curved stroke at the lower right of the annotation', hook)
inv('text', 'four last main prose baselines', 'on désigne par')
inv('margin note', 'lower left, near the bottom paper edge', '127', 'pencil foliation, hand unassigned')

doubts = [
    dict(place='opening range, second index after first ≥', reading=r'\unsure{d_2|d_1}', alternatives='2-like retraced digit; 1 remains possible', confidence='medium'),
    dict(place='cancelled old term in (204)', reading=r'\deleted{\unsure{D_{\Delta_I}|D_{\Delta_r}}}', alternatives='Delta_I / Delta_r; lower cluster is crossed and not fully separable', confidence='low'),
    dict(place='cancelled fragment before La composante', reading=r'\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}', alternatives='d_0,d_r / Delta_r,d_r; first index obscured', confidence='medium'),
    dict(place='short form before étale fini', reading=r'\unsure{revêt}', alternatives='terminal t-like/raised form is crowded; no expansion to revêtement in the text', confidence='medium'),
    dict(place='cancelled old argument in (205)', reading=r'\deleted{\unsure{[1,d_0]}}', alternatives='[1,d_0] plausible; first 1/comma crossed', confidence='medium'),
    dict(place='cancelled old word in the annotation', reading=r'\deleted{\illegible{1}}', alternatives='No defensible full word can be recovered under the strike', confidence='low'),
    dict(place='detached terminal curved stroke in the annotation', reading=hook, alternatives='Possible partial closing parenthesis or bracket; literal curve is certain, interpretation is not', confidence='medium')
]

notes = [
    'Scan128, author page63, pencil foliation127. The sheet is upright. Whole page and both native halves were read once; all 21 first-pass crops were then viewed. The principal baseline count is22:19 prose baselines (including the isolated à) and3 displayed-formula baselines. The three underbrace-note lines, its interlinear drapeaux, two-line lower alias of (204), raised replacement in (204), author number and pencil foliation are separately inventoried and excluded from that count.',
    'S128-01: the opening introduces analytic flag spaces indexed by a displayed degree sequence, and denotes their sum by D_{Delta_r}, with Delta_r=[0,r]∩N in (203). The initial range’s second tiny digit is genuinely doubtful (2 first, 1 alternative); it has not been selected to fit the preceding tuple. Both witnesses’ primary d_1 is therefore a departure. The initial ≥ signs, the later strict > signs, the literal exponent N^r and the lack of an additional > after d_1 in (204) are all retained.',
    'S128-02: the page asserts compatibility with D_J for a finite ordered set having a least element, then writes I_r twice and asserts contravariant functoriality for increasing applications, yielding a 1/2-simplicial analytic space. The I forms are clear literal stems with bars; they are not silently replaced by the previously defined Delta_r. This geometric/functorial assertion is recorded as background, not verified from this sheet alone.',
    'S128-03: (204) displays the coproduct of the flag components. A limited arity check counts r+1 entries in the written tuple (d_0,...,d_r), whereas the exponent written over N is r. Under the ordinary convention for N^r this is a notation mismatch; no missing +1 has been supplied. The strict/weak-chain discrepancy is also recorded without deciding whether it reflects different intended classes of flags. No global repair or proof of the analytic construction follows from this count.',
    'S128-04: the prose and (205) claim that each component is a finite étale cover of D_{d_0}, identified with the product contracted over the symmetric group of the D_{d_0}^{!} object and the finite flag set. Only the displayed bang, P form, group placement, base, indices and revision states have been checked visually. The analytic hypotheses and torsor property needed for that identification are not established on this page, so the geometric claim remains background.',
    'S128-05: the last paragraph defines the starred component as an inverse image and calls it the complement of the inverse image of the divisor Theta_{d_0}. A targeted set-theoretic check was performed: for f:Y→X and Z⊆X, y∈f^{-1}(X\\Z) iff f(y)∉Z iff y∉f^{-1}(Z), hence f^{-1}(X\\Z)=Y\\f^{-1}(Z). Conditional on the stated open-complement identification on the base, this verifies the complement-of-inverse-image step only. It does not verify that the inverse image is a divisor or settle the written Delta_{d_0-d_r} index.',
    'The final Theta has a clear oval and middle horizontal bar over an older angular trace. The earlier trace cannot be isolated as a complete deleted letter; no fabricated old Delta or other glyph has been inserted. The final live reading Theta_{d_0} is retained. The following base has the small dark 0 and a separate terminal point.',
    'In the annotation, the old word is struck and drapeaux is inserted above it; the detached short rightward/upward curve at the lower right is reproduced as a small TikZ stroke. It could be the terminal part of a closing parenthesis or bracket, but no matching opener or certain semantic role has been supplied. The brace scopes the flag-set factor. Both ens forms lack points, and the written quotes are paired strokes.',
    'The abbreviated revêt has a crowded terminal/raised form; it is not expanded in the transcription. At the bottom right, simple- ends at the scan boundary. The small dark terminal dash is visible, but the continuation beyond that boundary is not on this scan. H’s supplied completion is editorial and has not been used as visible evidence. No watermark, pale texture, shadow or black border has been transcribed.',
    'The three doubled-stroke N forms are transcribed as mathbb N. This is an alphabet correction relative to C, with no changed mathematical object. No diagram with objects or arrows occurs on this page; the only nonalphabetic drawing reproduced separately is the small detached terminal hook. The insertion leader in (204) is represented by the attachment and raised placement of the replacement rather than treated as a mathematical arrow.'
]

check_events = [
    dict(statement_id='S128-01', type='carried as background without fault found', outcome='Read the proposed flag-space notation and (203), without independently constructing the analytic spaces. Kept the locally doubtful digit in the opening range.'),
    dict(statement_id='S128-02', type='carried as background without fault found', outcome='Recorded the asserted contravariant functoriality and 1/2-simplicial structure. No verification of the analytic maps or their composition laws was undertaken.'),
    dict(statement_id='S128-03', type='targeted proof check', outcome='Counted the entries in (d_0,...,d_r): there are r+1, while the written exponent in N^r is r. This is only a syntactic arity check under the ordinary convention, and it does not prove or repair the intended coproduct statement.'),
    dict(statement_id='S128-04', type='carried as background without fault found', outcome='Recorded the finite étale/contracted-product assertion. No independent check of the torsor property, analytic hypotheses or flag-space construction was made.'),
    dict(statement_id='S128-05', type='targeted proof check', outcome='Verified by element membership that f^{-1}(X\\Z)=Y\\f^{-1}(Z) for a function f:Y→X. This supports the complement step conditionally on the stated base open set; divisor status and the Delta index remain outside the check.')
]

hand_log = [
    dict(habit='I is a straight stem with upper and lower bars, while Delta is angular and closed.', places='D_{I_r} after Alors; free I_r after contravariante; I_{d_0} in (205) and annotation; Delta in (203), (204), final paragraph', scope='Confirmed on these occurrences on scan128 only, using this page’s contrasting forms.', misreadings='H reads both I_r forms as Delta_r; C marks both as doubtful. Both are resolved to I_r.'),
    dict(habit='J can resemble a right bracket, with leftward terminal returns.', places='D_J pour J above the functoriality sentence', scope='Both adjacent Js on scan128 were checked.', misreadings='H reads I in both places; C’s J readings stand.'),
    dict(habit='The natural-number N has a visibly doubled left stroke.', places='(203), coproduct index of (204), last annotation line under (205)', scope='All three occurrences on scan128 were inspected on their crops.', misreadings='C uses bold N at all three places; mathbb N preserves the doubled form. No mathematical object is changed.'),
    dict(habit='A bang exponent has an upright and a detached dark dot; the flag P has an angular closed upper bowl.', places='D_{d_0}^{!} and mathcal P in (205)', scope='One occurrence of each on scan128.', misreadings='C gives a prime in the torsor exponent; H reads the flag symbol as F.'),
    dict(habit='The group S has a broad curled outline and is written below the wedge.', places='group of (205)', scope='The single group occurrence on scan128.', misreadings='C’s S/G doubt resolves to S; H’s superscript placement is contrary to the ink.'),
    dict(habit='Very small digit strokes may be retraced into a 2-like form; the expected sequence is insufficient to settle them.', places='second d in the opening range, compared with the clear d_1 in the preceding D tuple', scope='This one digit remains undecided on scan128.', misreadings='Both witnesses give d_1 without this local uncertainty; d_2 is the leading visual candidate.'),
    dict(habit='A shortened word can carry a crowded raised or retraced ending without spelling out its ordinary completion.', places='revêt before étale fini', scope='One abbreviation on scan128; its precise terminal form remains doubtful.', misreadings='Both C and H expand to revêtement.'),
    dict(habit='A live correction may be legible over an older angular trace even when the earlier glyph cannot be isolated.', places='Theta_{d_0} at bottom left', scope='One overwritten glyph on scan128.', misreadings='H marks the final Theta doubtful; final oval plus middle bar is clear, but the earlier trace is not assigned a fabricated value.')
]

notation = [
    dict(notation=r'\Delta_r=[0,r]\cap\mathbb N', meaning_or_form='Definition of the standard ordered simplex on the page; N has a doubled left stem.', places='(203)'),
    dict(notation=r'D_J; D_{I_r}; I_r', meaning_or_form='Literal J and I forms retained. I_r is not silently converted into the preceding Delta_r.', places='compatibility and functoriality prose'),
    dict(notation=r'\mathcal D_r; D_{\Delta_r}', meaning_or_form='The calligraphic component notation has the alternative ou D_{Delta_r} below it; a second D_{Delta_r} replaces a crossed term above the baseline.', places='(204)'),
    dict(notation=r'D_{d_0}^{!}', meaning_or_form='Exclamation exponent with a separate dot, not a prime.', places='(205)'),
    dict(notation=r'\mathcal P_{d_*}(I_{d_0})', meaning_or_form='Angular P for the flag set, described below as drapeaux of type d_* of I_{d_0}=[1,d_0]∩N.', places='(205) and its annotation'),
    dict(notation=r'\wedge_{(\mathfrak S_{d_0})_{D_{d_0}}}', meaning_or_form='The broad curled group letter is S; the full parenthesized group and its base are beneath the wedge.', places='(205)'),
    dict(notation=r'\Delta_{d_0-d_r};\ \Theta_{d_0}', meaning_or_form='The first glyph is an angular Delta with a literal horizontal dash in its subscript; the final Theta is a readable oval and middle bar over an unrecoverable earlier trace.', places='last two prose baselines')
]
abbreviations = [
    dict(form='ens.', expansion='ensemble (upper prose)'),
    dict(form='ens', expansion='ensemble (both unpointed forms in the flag annotation)'),
    dict(form='dim', expansion='dimension; no point after the abbreviation in this line'),
    dict(form=r'\unsure{revêt}', expansion='revêtement; only the shortened written form is transcribed, and its terminal strokes remain doubtful'),
    dict(form='1/2-simplicial', expansion='demi-simplicial; written as the fraction-like 1/2, not expanded in the page')
]

second_boxes = []
def box(kind, coords, reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}', kind=kind, coords=coords, reading=reading))
box('number', [775, 0, 895, 65], '63')
box('different words', CROPS['encore']['box'], 'encore')
box('doubtful formula', CROPS['initial_range']['box'], r'$D_{d_0,d_1,\ldots,d_r}$ pour $d_0\geq\unsure{d_2|d_1}\geq\cdots\geq d_r\geq0$')
box('different words', CROPS['somme']['box'], 'somme')
box('different words', CROPS['maintenant']['box'], "maintenant l'ens. ordonné")
box('number', CROPS['formula203']['box'], '\\[\n' + formula203 + '\n\\]')
box('different words', CROPS['dim_r']['box'], r'dim $r$.')
box('different words', CROPS['j_notation']['box'], r'$D_J$ pour $J$')
box('different words', CROPS['ayant']['box'], 'ordonné ayant un plus petit élément.')
box('doubtful formula', [225, 750, 1660, 835], r'Alors $D_{I_r}$ dépend fonctoriellement de façon')
box('doubtful formula', [225, 825, 1660, 930], r'contravariante en $I_r$, pour les applications')
box('number', [225, 1020, 1660, 1135], r"espace analytique $1/2$-simplicial, qu'on désigne par")
box('doubtful formula', CROPS['formula204']['box'], '\\[\n' + formula204 + '\n\\]')
box('struck passage', CROPS['cancelled_component']['box'], r'\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}')
box('number', [420, 1410, 1670, 1500], r'La composante $D_{d_*}=D_{d_0,d_1,\ldots,d_r}$ est')
box('low confidence departure', [225, 1500, 1665, 1620], r"un \unsure{revêt} étale fini de $D_{d_0}$, s'identifiant")
box('doubtful formula', [505, 1620, 1670, 1995], '\\[\n' + formula205 + '\n\\]')
box('number', [220, 1990, 1670, 2110], r"on désigne par $D^*_{d_0,d_1,\ldots,d_r}$ l'image inverse")
box('number', [225, 2100, 1665, 2185], r'de $D^*_{d_0}$, qui est donc le complémentaire')
box('different words', CROPS['image_inverse']['box'], r"de l'image inverse $\Delta_{d_0-d_r}$ du diviseur")
box('doubtful formula', CROPS['theta_base']['box'], r'$\Theta_{d_0}$ sur $D_{d_0}$.')
box('different words', CROPS['simple']['box'], 'plus simple-')
box('margin note', CROPS['footer127']['box'], r'\margin{127}')

unresolved = [
    'Opening range: the second index is 2-like and retraced; d_2|d_1 remains open, with d_2 first.',
    'Cancelled term of (204): Delta_I versus Delta_r cannot be fully recovered under the strike.',
    'Cancelled fragment before La composante: the first index remains obscured; d_0,d_r is leading but Delta_r,d_r remains possible.',
    'The exact crowded terminal/raised form of the abbreviation revêt remains uncertain; ment is not visibly written.',
    'The first numeral/comma of the cancelled [1,d_0] in (205) is obscured; the local C doubt is retained.',
    'The old word below inserted drapeaux is physically unreadable under its strike.',
    'The detached terminal curve in the annotation is reproduced, but its role as a closing parenthesis, bracket or other mark remains open.',
    'The earlier angular trace beneath the final Theta is not independently recoverable. The final Theta is clear; no deleted old letter has been invented.',
    'Continuation beyond the right scan edge after simple- is outside the visible source and has not been supplied.'
]

deletion_checks = [
    dict(span=r'\inserted{\text{ou }D_{\Delta_r}}', finding='The alternative is written below the calligraphic D_r, with ou above D_{Delta_r}; the proposed TeX retains that two-line placement and insertion state.'),
    dict(span=r'\deleted{\unsure{D_{\Delta_I}|D_{\Delta_r}}}', finding='The crossing covers the old D/index cluster. The main D survives, but the subscript is too dense to remove its existing doubt.'),
    dict(span=r'\inserted{D_{\Delta_r}}', finding='The replacement is raised above the crossed term after the first equals sign; the curved leader attaches to that term, not to the coproduct. It is set above the cancellation in the proposed text.'),
    dict(span=r'\deleted{$\unsure{D_{d_0,d_r}|D_{\Delta_r,d_r}}$}', finding='The cancellation is confined to the left fragment and stops before La composante. Partial letters/indices remain readable, but not every crossed stroke is plain.'),
    dict(span=r'\deleted{\unsure{[1,d_0]}}', finding='Diagonal strokes cross the old bracketed argument; the live I_{d_0} to the right is outside that cancellation. The first numeral and comma remain obscured, so the doubt stays.'),
    dict(span=r'\deleted{\illegible{1}}drapeaux', finding='The old word is crossed through on the annotation baseline; drapeaux is written above it. Its long p descender overlaps the lower area but is not a cancellation of the replacement. The new word receives its missing inserted wrapper.'),
    dict(span=r'$\Theta_{d_0}$', finding='The final oval and middle bar form Theta over an older angular trace. No complete earlier glyph can be separated, and there is no independent cancellation of the live Theta.'),
    dict(span='all remaining unmarked text', finding='All prose, displays, punctuation, small numbers, margins and the bottom scan boundary were compared visually with both witnesses. No additional legible struck word or insertion was found. The terminal annotation hook is retained as literal geometry rather than interpreted as a deletion.'),
]

report = dict(scan=128, reader='reader_b', line_count=22, rows=rows,
              decisions=decisions, inventory=inventory, doubts=doubts,
              notes=notes, check_events=check_events, hand_log=hand_log,
              notation=notation, abbreviations=abbreviations,
              second_boxes=second_boxes, unresolved=unresolved,
              deletion_insertion_checks=deletion_checks)

allowed_kinds = {'misread word', 'misread symbol or index', 'omission',
    'text not on the page', 'deletion state (struck given live or live given struck)',
    'insertion or placement', 'abbreviation expanded or spelling modernised',
    r'readable ink left as \ill{}', 'drawing or diagram', 'other'}
assert all(r['kind'] in allowed_kinds for r in rows)
assert {d['id'] for d in decisions} == {'M1279', 'M1280', 'M1281', 'M1282'}
assert all(r['against_C'] or r['against_H'] for r in rows)
for item in rows + decisions:
    assert (ROOT / 'edition' / item['crop']).is_file(), item['crop']
for item in second_boxes:
    x0, y0, x1, y1 = item['coords']
    assert 0 <= x0 < x1 <= 1692 and 0 <= y0 < y1 <= 2363, item
assert proposed.count(r'\[') == proposed.count(r'\]') == 3
assert proposed.count('{') == proposed.count('}'), 'unbalanced braces'
assert proposed.count('$') % 2 == 0, 'unbalanced dollar signs'
assert '\\diagram' not in proposed

(OUT / '147_scan128_proposed.tex').write_text(proposed)
(OUT / '147_scan128_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(scan=128, rows=len(rows), decisions=len(decisions),
                     resolved=sum(d['decision'] != 'undecided' for d in decisions),
                     crops=len(CROPS), second_boxes=len(second_boxes),
                     inventory=len(inventory), doubts=len(doubts),
                     against_C=sum(r['against_C'] for r in rows),
                     against_H=sum(r['against_H'] for r in rows))))
