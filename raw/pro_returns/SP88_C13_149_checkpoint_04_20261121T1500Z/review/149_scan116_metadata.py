import json
from pathlib import Path

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan116'
BOXES = {
    'p01': [872, 55, 1549, 179], 'p02': [332, 133, 1518, 343],
    'p03': [328, 300, 1641, 452], 'p04': [331, 439, 1625, 616],
    'p05': [325, 576, 1673, 723], 'p06': [16, 48, 292, 435],
    'p07': [327, 730, 1574, 866], 'p08': [313, 855, 1590, 985],
    'p09': [355, 981, 1148, 1122], 'p10': [320, 1027, 497, 1134],
    'p11': [300, 1080, 1503, 1256], 'p12': [319, 1278, 874, 1388],
    'p13': [292, 1391, 966, 1496], 'p14': [297, 1505, 1590, 1630],
    'p15': [314, 1633, 1551, 1768], 'p16': [305, 1762, 1474, 1887],
    'p17': [285, 1884, 1644, 2168], 'p18': [263, 2151, 1622, 2348],
    'p19': [18, 2300, 94, 2354],
}


def crop(p):
    return f'crops/{PAGE}_{p}.png'


def change(id, place, C, H, final, evidence, confidence, vs_C, vs_H,
           kind, category, H_marked=False, consequential=False, crop_id=None):
    p = crop_id or id
    return dict(id=id, place=place, C=C, H=H, final=final,
                evidence=evidence, crop=crop(p), bbox=BOXES[p],
                confidence=confidence, vs_C=vs_C, vs_H=vs_H,
                kind=kind, error_category=category, H_marked=H_marked,
                consequential=consequential)


TOP = r'''c'est la partie ``universellement géom'' de $\mathcal E_{\deleted{\unsure{X}}L}^{\overline L}$, \deleted{noté $\mathcal E_{L/K}^{\unsure{g}\overline L}$} \deleted{qui \unsure{couvre} les \unsure{hom|bons}} \inserted{(relativement à $K$)} qui classifie les schémas (finis) étales sur $L$ qui sont ``non ramifiés'' sur \uline{tout} modèle \deleted{\unsure{étal}} régulier (propre ou non) de $L/K$.'''
MARGIN = r'''\margin{noté $\mathcal E_L^{\unsure{g}\overline L}$ ou\\ $\mathcal E_L^{\unsure{g(K)},\overline L}$}'''
FORMULA21 = r'''(21)\qquad \mathcal E_L^{\overline L}\unsure{\longrightarrow|\longleftrightarrow}\mathcal E_{\deleted{\unsure{L}}U}^{\overline L}\longrightarrow\mathcal E_X^{\overline L}=\mathcal E_{\deleted{\unsure{X}}L}^{\unsure{g}\overline L}'''
FORMULA22 = r'''(22)\qquad U=X\setminus Z'''
MODEL = r'''Si $U$ est un modèle quelconque\unsure{,|;} il se plonge dans un $X$, et on a des hom surjectifs
\deleted{\unsure{q}}
\[
''' + FORMULA21 + r'''
\]'''
BOUNDARY = r'''$Z$ partie ferm. de $X$ --- soient $D_i$ ses composantes de codim $1$, $x_i$ les \unsure{pts|pt} gén. de $D_i$. On a des'''
LOWER = r'''groupes de décomposition et d'inertie $N_{x_i'}$ et $I_{x_i'}$ \inserted{de $\mathcal E_U^{\overline L}$} \unsure{d|\deleted{d}} relatifs au choix d'un $x_i'$ au dessus de $x_i$ dans le normalisé de $X$ dans $\overline L$), et on trouve'''

CHANGES = [
    change('p01', 'Opening quoted qualification',
           r"``\unsure{universellement|universelles} géom''",
           '« universellement générique »', r"``universellement géom''",
           'After the paired l ascenders, the low compressed continuation ends in a raised t turn, favoring universellement over universelles. The next word is the short form géom, with a g descent, small accented e/o forms and a low final m; the letters of générique are not present. Both quote positions have ordinary doubled pen strokes. Resolving the first alternative does not replace C’s preferred word and is not counted as a C correction.',
           'medium', False, True, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised', False, True),
    change('p02a', 'First live E expression: overwritten subscript before the comma',
           r'\mathcal E_L^{\overline L}', r'\mathcal{E}^{\overline{L}}_{L}',
           r'\mathcal E_{\deleted{\unsure{X}}L}^{\overline L}',
           'The live dark L has a heavy upright and rightward foot. Two thinner oblique strokes cross behind it, extending on opposite diagonals beyond the heavy letter. They support an earlier X, but the overlap prevents full certainty; that underletter is therefore retained as doubtful cancelled text. The overbar and superscript L are clear, and the following comma is independent.',
           'medium', True, True, 'omission', 'Struck text', False, False, 'p02'),
    change('p02b', 'Raised cancelled notation after the first live E expression',
           r'\deleted{noté $\mathcal E_{L/K}^{\unsure{g},\overline L}$}',
           r'\struck{relative à \ill{}}',
           r'\deleted{noté $\mathcal E_{L/K}^{\unsure{g}\overline L}$}',
           'The upper crossed line contains noté, then an E expression with L/K below and a small looped-descender sign followed by barred L above. No independent comma stroke separates that small sign from barred L. The cancellation crosses the whole note. The sign remains g-uncertain; its identity is not resolved from the mathematical context.',
           'medium', True, True, 'misread word', 'Words', True, False, 'p02'),
    change('p02c', 'Lower cancelled phrase across the second main line',
           r'\deleted{qui \unsure{couvre} les \unsure{hom|bons}}',
           r'\struck{qui \ill{} les \ill{}}',
           r'\deleted{qui \unsure{couvre} les \unsure{hom|bons}}',
           'The initial q descends below its loop and is followed by u/i; les is separately visible. The next two small-letter words are crossed along their bodies. Couvre is supported by the opening c/o and following humps but remains doubtful. The final word has a tall initial stem and a compressed ending, compatible with hom or bons; no certainty is supplied beneath the strike.',
           'low', False, True, 'readable ink left as \\ill{}',
           'Readable ink left as illegible', True, False, 'p02'),
    change('p02d', 'Inserted qualification and its attachment before the live qui',
           r'\inserted{(relativement à $K$),} qui',
           r'(qui \ill{} \ill{}) classifie',
           r'\inserted{(relativement à $K$)} qui',
           'The raised words read relativement à K within parentheses. The long curved stroke at their right runs down-left to the gap before the live qui. It is a continuous attachment leader, not a comma. The separate comma after the first E term is retained; no comma is supplied at the end of this insertion.',
           'high', True, True, 'insertion or placement',
           'Insertions put in the wrong place', True, False, 'p02'),
    change('p03', 'Line classifie les schémas (finis) étales sur L',
           r'classifie les schémas (finis) étales sur $L$',
           r'classifie les \uncertain{sel.} (finis) \ill{} sur $L$',
           r'classifie les schémas (finis) étales sur $L$',
           'The word after les shows the s/c opening, the h ascender and a longer low continuation corresponding to schémas, rather than the short sel. After the intact parenthesis (finis), the accented opening and t/l rises of étales are readable. The final L stands unbarred in the prose.',
           'high', False, True, 'readable ink left as \\ill{}',
           'Readable ink left as illegible', True),
    change('p04', 'Quoted non ramifiés and underlined tout',
           r"qui sont ``non ramifiés'' sur \uline{tout} modèle",
           r'qui sont « \uncertain{non ramifiés} » sur tout modèle',
           r"qui sont ``non ramifiés'' sur \uline{tout} modèle",
           'The quote marks are paired short strokes, not angular guillemets. Non ramifiés is legible on the crop. Tout contains two t stems with small intervening o/u strokes, and an independent underline lies below the word; it is not reduced to the abbreviation tt.',
           'high', False, True, 'other', 'Other', True),
    change('p05', 'Cancelled word before régulier',
           r'\deleted{\unsure{étal}} régulier', 'régulier',
           r'\deleted{\unsure{étal}} régulier',
           'A crossed word precedes régulier. A small initial loop, an early raised stem and a final tall l support étal, but the strike intersects its small letters and the reading remains doubtful. Régulier itself, the following parenthesis and L/K. are live.',
           'low', False, True, 'omission', 'Struck text'),
    change('p06', 'Two-row slanted marginal notation',
           r'\margin{noté $\mathcal E_L^{\unsure{g},\overline L}$ ou $\mathcal E_L^{\unsure{g(K)},\overline L}$}',
           r'\marginal{$\mathcal{E}^{\mathrm{g}\overline{L}}_{L}$ \ill{} \struck{\ill{}} \ill{} $\mathcal{E}^{\overline{L}}_{L}$}',
           MARGIN,
           'The clockwise-rotated crop reads noté, the first indexed E expression, ou, then a second indexed E expression on a separate marginal row. Both lower indices are L and both upper Ls have bars. In the first exponent the g-like sign is followed directly by barred L, with no distinct comma. The second exponent is heavily retraced around g(K), whose reading remains doubtful, and has a separate comma-like curve before barred L. No separable older letter sequence is invented within that retracing.',
           'medium', True, True, 'misread symbol or index',
           'Symbols and indices', True),
    change('p07', 'Punctuation after quelconque',
           'quelconque;', 'quelconque,', r'quelconque\unsure{,|;}',
           'After the q descent are a low continuation and a small detached e-like final turn, followed by a lower comma. The high turn may belong to the word’s final e rather than being an independent semicolon dot. Comma is preferred, with semicolon retained as the alternative.',
           'medium', True, False, 'other', 'Other'),
    change('p08', 'Following line: un X',
           r'il se plonge dans un $X$', r'il se plonge dans les $X$',
           r'il se plonge dans un $X$',
           'Before X are two low joined humps and a terminal n return. There is no tall l ascender and no separate e/s sequence. The word is un.',
           'high', False, True, 'misread word', 'Words'),
    change('p09', 'Short form before surjectifs',
           'des hom surjectifs', 'des homomorphismes surjectifs',
           'des hom surjectifs',
           'The short word consists of a tall h, a small o and a low m ending; it stops there without a terminal dot. The much longer continuation of homomorphismes is not written. The descender in surjectifs belongs to its f.',
           'high', False, True, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised'),
    change('p10', 'Small isolated crossed fragment above (21), left of des',
           r'\deleted{\unsure{q}}', '[absent]', r'\deleted{\unsure{q}}',
           'A small looped upper form and long retraced descending strokes occupy a separate low level between the prose and (21). The heavy overlapping strokes obscure the original letter. The tentative q reading and cancellation are retained without resolution.',
           'low', False, True, 'omission', 'Struck text'),
    change('p11', 'Complete display (21): overwritten subscripts and last exponent',
           r'(21)\qquad \mathcal E_L^{\overline L}\longrightarrow\mathcal E_U^{\overline L}\longrightarrow\mathcal E_X^{\overline L}=\mathcal E_L^{\unsure{g},\overline L}',
           r'\text{(21)}\qquad\mathcal{E}^{\overline L}_{L}\longrightarrow\mathcal{E}^{\overline L}_{U}\longrightarrow\mathcal{E}^{\overline L}_{X}=\mathcal{E}^{\mathrm g\overline L}_{L}',
           FORMULA21,
           'Beneath the curved live U is a thinner upright and rightward base compatible with an earlier L. Behind the last heavy L are thin crossed diagonals compatible with an earlier X, as in the first prose expression. Both underletters remain doubtful. The final g-like sign is followed by barred L without an independent comma. The first arrow has a clear right head and a tiny tapered left return; that return may be a nib entry or a second head, so the new arrow doubt alone is not counted as a correction. The second arrow points right. The complete four-term formula, overbars and (21) were inspected.',
           'medium', True, True, 'omission', 'Struck text'),
    change('p12', 'Cancelled word after On aura',
           r'On aura \deleted{\unsure{alors}}', r'On aura \struck{\ill{}}',
           r'On aura \deleted{\unsure{alors}}',
           'The cancelled cluster has a looped opening, tall intersecting strokes and a low rounded body. The crossing strokes prevent a letter-by-letter reading. Alors remains only a tentative undertext, not a resolved word; On aura is plain.',
           'low', False, True, 'readable ink left as \\ill{}',
           'Readable ink left as illegible', True),
    change('p14', 'Boundary description: ferm.',
           r'$Z$ partie ferm. de $X$', r'$Z$ partie fermée de $X$',
           r'$Z$ partie ferm. de $X$',
           'The long f and low erm continuation end before a separate small stop. No final é/e sequence follows. The written form is ferm., retained without expansion.',
           'high', False, True, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised'),
    change('p16', 'Line describing the generic points of D_i',
           r'pts gén. de $D_i$. On a des',
           r'pts génériques des $D_i$. On a des',
           r'\unsure{pts|pt} gén. de $D_i$. On a des',
           'The generic-point abbreviation ends at n and a separate stop; the following short preposition is de, without an s. The first point abbreviation has a clear p/t shape but no securely separable final s, so pts is retained first with pt as a new alternative, not a correction against either witness. The O of On is heavily retraced; an older A-like outline is not independently secure enough to transcribe as a separate letter.',
           'medium', False, True, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised'),
    change('p17', 'Inserted group membership phrase and d-like glyph before relatifs',
           r"$N_{x_i'}$ et $I_{x_i'}$ \inserted{de $\mathcal E_U^{\overline L}$}, (relatifs au choix d'un",
           r"dans $\mathcal{E}^{\overline L}_U$ $N_{x'_i}$ et $I_{x'_i}$ (\struck{d} relatifs au choix d'un",
           r"$N_{x_i'}$ et $I_{x_i'}$ \inserted{de $\mathcal E_U^{\overline L}$} \unsure{d|\deleted{d}} relatifs au choix d'un",
           'The raised word is de, followed by E with lower U and upper barred L. Its long leader runs continuously from the right side down-left into the baseline gap before relatifs. The apparent opening parenthesis is part of that same leader; no independent opening parenthesis or comma is visible after I. A clear d is present on the baseline, omitted by C. Its upper stem is crossed by the leader, but there is no separate cancellation stroke, so live d is preferred with deleted d retained as a state alternative. The two group labels and their primed x/i subscripts were read in full. TeX x_i-prime versus x-prime_i order denotes the same observed arrangement and is not a correction.',
           'medium', True, True, 'insertion or placement',
           'Insertions put in the wrong place'),
    change('p19', 'Lower-left foliation', r'\margin{115}', '[absent]',
           r'\margin{115}',
           'The separate thin foliation contains two upright 1s with oblique entries and a 5 with a horizontal upper stroke and lower curve. It is retained as 115. No authorial page number was identified at the head.',
           'high', False, True, 'omission', 'Omissions'),
]

DECISIONS = [
    dict(id='M0072', cote='149', scan='116', decision='first', reading='universellement',
         evidence='After the two l ascenders, the low compressed continuation ends in a raised t turn. That terminal form favors universellement over universelles; the short following géom was also read in the same crop.',
         crop=crop('p01'), bbox=BOXES['p01'], confidence='medium'),
    dict(id='M0073', cote='149', scan='116', decision='undecided', reading=r'\unsure{g}',
         evidence='The first marginal exponent has a small loop with a descending stroke, compatible with g. Its exact letter identity is not settled by the local shape. The whole E expression and neighboring notation were inspected; no comma is visible before barred L.',
         crop=crop('p06'), bbox=BOXES['p06'], confidence='medium'),
    dict(id='M0074', cote='149', scan='116', decision='undecided', reading=r'\unsure{g(K)}',
         evidence='The second marginal exponent is heavily retraced around the looped letter and parenthesized K-like form. The preferred g(K) reading remains uncertain. A separate comma-like curve follows it before barred L. No older character sequence can be isolated securely beneath the retracing.',
         crop=crop('p06'), bbox=BOXES['p06'], confidence='low'),
    dict(id='M0075', cote='149', scan='116', decision='undecided', reading=r'\unsure{g}',
         evidence='The last exponent in (21) contains a small looped descending sign before barred L. It is consistent with the marginal g-like form but does not uniquely settle the letter. The whole formula and its overwritten subscripts were inspected.',
         crop=crop('p11'), bbox=BOXES['p11'], confidence='medium'),
]

DOUBTS = [
    dict(place='First live E expression, overwritten lower index', reading=r'\deleted{\unsure{X}}L', alternatives='Two thin crossed diagonals support an earlier X behind the heavy live L, but part of the underletter is obscured.', confidence='medium'),
    dict(place='Raised cancelled notation, small exponent before barred L', reading=r'\unsure{g}', alternatives='The looped descending sign supports g but remains letter-uncertain inside the cancellation.', confidence='low'),
    dict(place='Lower cancelled phrase, word after qui', reading=r'\unsure{couvre}', alternatives='Couvre is supported by the remaining upper loops and humps, but the strike overlaps the small-letter bodies.', confidence='low'),
    dict(place='Lower cancelled phrase, last word', reading=r'\unsure{hom|bons}', alternatives='The tall opening and compressed ending admit hom and bons beneath the strike.', confidence='low'),
    dict(place='Cancelled word before régulier', reading=r'\unsure{étal}', alternatives='The initial loop and tall final l support étal, but cancellation obscures the small letters.', confidence='low'),
    dict(place='First marginal E exponent', reading=r'\unsure{g}', alternatives='A g-like loop and descender are visible, without a uniquely decisive letter form.', confidence='medium'),
    dict(place='Second marginal E exponent', reading=r'\unsure{g(K)}', alternatives='The parenthesized K-like form and preceding looped sign are heavily retraced; no distinct older string is secure.', confidence='low'),
    dict(place='Punctuation after quelconque', reading=r'\unsure{,|;}', alternatives='The high small stroke may be the final e rather than a semicolon dot. The lower comma is clear.', confidence='medium'),
    dict(place='Small crossed fragment before (21)', reading=r'\deleted{\unsure{q}}', alternatives='The loop and long overlapping strokes do not securely recover the letter. The inherited q proposal remains tentative.', confidence='low'),
    dict(place='First arrow in (21)', reading=r'\unsure{\longrightarrow|\longleftrightarrow}', alternatives='Right head certain; the tiny left-pointed return may be pen entry or a second head. Surjectivity is not used to decide the ink.', confidence='medium'),
    dict(place='Middle subscript in (21)', reading=r'\deleted{\unsure{L}}U', alternatives='The thin upright and base beneath the curved U suggest an earlier L, but the overlap is incomplete.', confidence='medium'),
    dict(place='Final subscript in (21)', reading=r'\deleted{\unsure{X}}L', alternatives='Thin crossed diagonals behind the final heavy L suggest an earlier X; parts are hidden.', confidence='medium'),
    dict(place='Final exponent in (21)', reading=r'\unsure{g}', alternatives='The small looped descending glyph remains g-like but unresolved.', confidence='medium'),
    dict(place='Cancelled word after On aura', reading=r'\deleted{\unsure{alors}}', alternatives='Crossing strokes obscure the interior; alors remains a tentative undertext only.', confidence='low'),
    dict(place='Point abbreviation before gén.', reading=r'\unsure{pts|pt}', alternatives='The p/t shape is clear but a distinct final s is not secure. Superscript typography is not additionally inferred here.', confidence='medium'),
    dict(place='Baseline d before relatifs, crossed by the insertion leader', reading=r'\unsure{d|\deleted{d}}', alternatives='The letter is d. Its live/cancelled state is uncertain because the only crossing is the continuous insertion leader, not an independent deletion stroke.', confidence='medium'),
]

INVENTORY = [
    dict(sheet_kind='text', hand='his hand', element='e01', kind='text', position='first five main baselines', first_words_or_objects="c'est la partie", transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e02', kind='deletion', position='subscript of first live E expression', first_words_or_objects=r'\deleted{\unsure{X}}L', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e03', kind='deletion', position='raised note between first and second main lines', first_words_or_objects=r'noté E_{L/K}^{g-like barred-L}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e04', kind='deletion', position='across second main line', first_words_or_objects=r'qui \unsure{couvre} les \unsure{hom|bons}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e05', kind='insertion', position='raised to the right of the cancelled note; leader to live qui', first_words_or_objects='(relativement à K)', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e06', kind='deletion', position='start of fifth main line, before régulier', first_words_or_objects=r'\unsure{étal}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e07', kind='margin note', position='slanted upper-left margin, two written rows', first_words_or_objects='noté E... ou E...', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e08', kind='text', position='three lines beginning Si U', first_words_or_objects='Si U est un modèle quelconque', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e09', kind='deletion', position='isolated below-left of des, above (21)', first_words_or_objects=r'\unsure{q}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e10', kind='display', position='middle of page, after surjectifs', first_words_or_objects=FORMULA21, transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e11', kind='deletion', position='beneath live U in (21)', first_words_or_objects=r'\deleted{\unsure{L}}U', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e12', kind='deletion', position='beneath final live L in (21)', first_words_or_objects=r'\deleted{\unsure{X}}L', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e13', kind='text', position='between (21) and (22)', first_words_or_objects='On aura', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e14', kind='deletion', position='after On aura', first_words_or_objects=r'\unsure{alors}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e15', kind='display', position='below On aura', first_words_or_objects=FORMULA22, transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e16', kind='text', position='last seven main lines, from Z partie to et on trouve', first_words_or_objects='Z partie ferm. de X', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e17', kind='insertion', position='above N and I line, leader to gap before relatifs', first_words_or_objects=r'de \mathcal E_U^{\overline L}', transcribed='yes'),
    dict(sheet_kind='text', hand='his hand', element='e18', kind='text', position='baseline before relatifs; cancellation state uncertain', first_words_or_objects=r'\unsure{d|\deleted{d}}', transcribed='yes'),
    dict(sheet_kind='text', hand='separate thin foliation hand', element='e19', kind='margin note', position='bottom left', first_words_or_objects='115', transcribed='yes'),
]

AUDIT = [
    dict(box='b01', kind='C/H word difference; insertion; deletion; doubtful formula; less-than-high C departure', bbox=[320, 45, 1673, 724], reading=TOP),
    dict(box='b02', kind='margin note; doubtful formula; C/H word difference; less-than-high C departure', bbox=BOXES['p06'], reading=MARGIN),
    dict(box='b03', kind='C/H word difference; deletion; doubtful formula; handwritten number; less-than-high C departure', bbox=[299, 729, 1591, 1257], reading=MODEL),
    dict(box='b04', kind='deletion; C/H word difference; handwritten number', bbox=[290, 1278, 966, 1497], reading=r'On aura \deleted{\unsure{alors}}' + '\n\\[\n' + FORMULA22 + '\n\\]'),
    dict(box='b05', kind='C/H word difference; handwritten number', bbox=[296, 1505, 1591, 1887], reading=BOUNDARY),
    dict(box='b06', kind='insertion; deletion; doubtful formula; C/H word difference; less-than-high C departure', bbox=[262, 1883, 1644, 2349], reading=LOWER),
    dict(box='b07', kind='margin note; handwritten number; C/H word difference', bbox=BOXES['p19'], reading=r'\margin{115}'),
]

DATA = dict(
    page=PAGE, scan=116, reader='reader_b', line_count=24,
    line_count_detail=dict(main=19, diagram=0, margin=2, insertion=2, standalone_numbers=1),
    changes=CHANGES, decisions=DECISIONS, inventory=INVENTORY, doubts=DOUBTS,
    audit_boxes=AUDIT,
    notes=[
        'The leaf describes a universally geometric part relative to K through covers unramified on every regular model, gives the maps (21), writes U=X minus Z in (22), and introduces codimension-one components and decomposition/inertia groups. This summarizes the written claims; it is not proof verification.',
        'All-ink logical line count: five introductory main lines; three model-paragraph lines; the isolated crossed q-like fragment; (21); On aura; (22); and seven concluding main lines give 19. The raised top correction row and raised lower de E row contribute two. The slanted marginal notation has two written rows. The separate foliation 115 contributes one. Total 24. The top raised row contains the cancelled note and its adjacent live qualification at a common sloping level.',
        'There is no identified authorial page number at the head. The handwritten numerals (21), (22), the inline codim 1, and foliation 115 all have explicit blind-audit coverage. The i subscripts on D and x are dotted letters rather than extra numerical labels.',
        'The initial and final heavy L subscripts cover thin crossed diagonals suggestive of X. The middle U in (21) covers a thin L-like upright/base. Those earlier letters remain uncertain and are retained as cancelled undertext. No separate older letter is invented inside the dark marginal g(K) retracing or the retraced O of On.',
        'The curved top attachment stroke is a leader from the raised qualification to the live qui; it is not the comma supplied by C. The initial live E expression has a separate actual comma, which remains.',
        'At the lower insertion, the long stroke from de E is continuous with the apparent opening parenthesis before relatifs. It crosses the d stem but supplies no independent deletion stroke. The candidate preserves live d first with cancellation-state alternative and omits the inferred comma/opening parenthesis. The actual closing parenthesis after barred L on the last line remains unmatched.',
        'The first arrow in (21) certainly points right; its small left return may or may not be a second head. This is marked locally and is not settled by the sentence about surjectivity. Adding this doubt alone is not a correction count.',
        'No comma is independently visible between g-like sign and barred L in the cancelled top exponent, first marginal exponent or final exponent of (21). The second marginal g(K) expression does have a separate comma-like curve. The case-by-case differences are retained.',
        'The short forms géom, hom, ferm. and gén. remain unexpanded. Tout has intervening o/u ink between its two t stems and a separate underline. The less secure point abbreviation remains pts|pt, without claiming a newly certain superscript level.',
        'The large audit boxes cover complete contiguous passages, including all neighboring words and complete formulas rather than isolated indices. This avoids presenting clipped correction context to the blind reader. The evidence crops remain the nineteen distinct saved local places.',
        'The margin crop p06 was rotated clockwise 45 degrees after extraction; its recorded bbox is in original page coordinates. Every crop was generated once and visually inspected. The full source and both native halves were each inspected once.',
        'Only the assigned page packet, its current notation table, the common reading instructions and the reader’s own files were accessed. There was no OCR, external research or TeX compilation. No proof verification is claimed.',
        'Only M0072–M0075 appear in decisions. Doubts within cancellations, new underletter doubts and new geometry/state doubts receive no invented mark IDs. H editorial notes and macro-only differences are not source-text changes.',
    ],
    checks=[],
    hand_observations=[
        dict(habit='Heavy current subscripts may cover finer earlier strokes.', places='Initial live E_L; middle E_U and final E_L in (21).', holds='Two places have crossed fine strokes compatible with X beneath L; the U place has a fine L-like base/upright. All earlier-letter identifications remain doubtful.', witness_errors='Both witnesses omit the possible earlier letters.'),
        dict(habit='Insertion leaders can resemble a comma or an opening parenthesis and can cross a letter without separately cancelling it.', places='Raised relativement à K; raised de E_U before relatifs.', holds='The continuous paths are visible in p02 and p17. The lower d is crossed only by the leader; its cancellation state remains uncertain.', witness_errors='C supplies punctuation from these leaders and omits the d; H treats the lower d as certainly struck and also supplies an opening parenthesis.'),
        dict(habit='A tiny return at an arrow tail is not always distinguishable from a second head.', places='First arrow of (21), compared with the blunt start of the second arrow.', holds='The right head is clear; the left feature remains a local geometry doubt.', witness_errors='Both witnesses give an unqualified rightward arrow.'),
        dict(habit='The g-like exponent sign is a small loop with a descender; retracing may obscure its letter identity.', places='Cancelled top note; both marginal forms; final term of (21).', holds='All four occurrences were inspected in their full expressions. The exact letter remains unresolved.', witness_errors='C records uncertainty; H also comments on uncertainty. No shared choice is used to force a letter reading.'),
        dict(habit='Exponential separators must be checked individually.', places='The four g-like exponents.', holds='Only the second marginal g(K),barred-L expression has a separate comma-like curve.', witness_errors='C supplies commas in the other three expressions.'),
        dict(habit='Short forms have separately written terminal stops, and small terminal strokes can be ambiguous.', places='géom, hom, ferm., gén.; quelconque; pts|pt.', holds='géom and hom lack stops, ferm. and gén. have stops. The punctuation after quelconque and the final s of the point abbreviation remain local doubts.', witness_errors='H expands several abbreviations; C’s semicolon is less secure than its confident presentation.'),
    ],
    notation=[
        dict(written=r'\mathcal E_L^{\overline L}', meaning_or_use='The live field-indexed E expression at the opening and start of (21); the opening lower L is overwritten.', places='First paragraph and (21).'),
        dict(written=r'\mathcal E_{L/K}^{\unsure{g}\overline L}', meaning_or_use='Cancelled raised notation, including a literal relative L/K subscript.', places='Top correction cluster.'),
        dict(written=r'\mathcal E_L^{\unsure{g}\overline L}\ \text{ou}\ \mathcal E_L^{\unsure{g(K)},\overline L}', meaning_or_use='Two marginal notations for the part described relative to K; exact g-like lettering remains unresolved.', places='Slanted upper-left margin.'),
        dict(written=r'\mathcal E_U^{\overline L},\ \mathcal E_X^{\overline L}', meaning_or_use='Middle terms of (21); U is visibly rewritten over a doubtful L-like earlier form.', places='Display (21); the U expression also appears in the lower insertion.'),
        dict(written=r'U=X\setminus Z', meaning_or_use='Literal expression (22), followed by the description of Z as a closed part of X.', places='Display (22) and following prose.'),
        dict(written=r'D_i,\ x_i,\ N_{x_i\prime},\ I_{x_i\prime}', meaning_or_use='Names for components, generic points, and the decomposition/inertia group labels written on the leaf.', places='Concluding seven main lines.'),
    ],
    abbreviations=[
        dict(written='géom', expansion='géométrique, retained as the written short form'),
        dict(written='hom', expansion='homomorphismes'),
        dict(written='ferm.', expansion='fermée'),
        dict(written='codim', expansion='codimension'),
        dict(written=r'\unsure{pts|pt}', expansion='points or point; final s remains uncertain'),
        dict(written='gén.', expansion='génériques'),
    ],
    inspection=dict(whole=True, halves=['top', 'bottom'],
                    crops=[crop(p) for p in BOXES],
                    deletions_insertions_checked=True),
)

if __name__ == '__main__':
    target = ROOT / f'edition/review/{PAGE}.json'
    if target.exists():
        raise FileExistsError(f'Refusing to overwrite frozen metadata: {target}')
    target.write_text(json.dumps(DATA, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(path=str(target), changes=len(CHANGES),
                         crops=len(BOXES), doubts=len(DOUBTS),
                         audit_boxes=len(AUDIT), line_count=DATA['line_count'])))
