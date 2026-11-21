"""Frozen first-reading metadata for 149_scan119. Source-only visual reading."""
import csv
import importlib.util
import json
from pathlib import Path

ROOT = Path('/workspace/scratch/0cab6a548abb')
HERE = ROOT / 'edition/review'
PAGE = '149_scan119'
spec = importlib.util.spec_from_file_location('scan119_crops', HERE / f'{PAGE}_crop.py')
crop_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crop_module)
CROPS = crop_module.CROPS

def change(place_id, place, C, H, final, evidence, confidence, vs_C, kind,
           error_category, H_marked=False, consequential=False):
    return {
        'id': place_id, 'place': place, 'C': C, 'H': H, 'final': final,
        'evidence': evidence, 'crop': f'crops/{PAGE}_{place_id}.png',
        'bbox': CROPS[place_id][0], 'confidence': confidence,
        'vs_C': vs_C, 'vs_H': True, 'kind': kind,
        'error_category': error_category, 'H_marked': H_marked,
        'consequential': consequential,
    }

changes = [
    change('p01', 'Main line 1: cancellation and raised replacement after universel',
           r"\deleted{\unsure{(ou} \illegible{1}} \inserted{ou encore} d'un",
           r"\struck{\uncertain{(précis.}} \add{\uncertain{ou} \ill{}} d'une",
           r"\deleted{\unsure{(précis.|(precis.}} \inserted{ou encore} d'un",
           'The crossed word has an initial opening curve and a letter with a long p-like descender, then small r/e/c/i/s-like remnants and a terminal dot. It is not a plain ou followed by wholly unreadable ink. The strike traverses the middle letters and no detached accent is secure; both spelling variants remain inside the doubt. Above it, ou encore is legible. Its long curved leader ends before d\'un; that final word has no terminal e, and no closing parenthesis is supplied from the leader.',
           'medium', True, r'readable ink left as \ill{}',
           'Readable ink left as illegible', True),
    change('p02', 'Main line 2: point abbreviation, Greek point, retouched field label and d\'une',
           r"pt géom $\unsure{\xi|\zeta}$ de $\unsure{\widetilde K_x|\widetilde U_x}$ --- i.e. \unsure{d'une|de une}",
           r"pt géométrique de $\tilde{U}_x$ --- i.e. de l'une",
           r"pt géom $\unsure{\zeta|\xi}$ de $\unsure{\widetilde K_x|\widetilde U_x}$ --- i.e. d'une",
           'Only pt géom is written; the word is not expanded. A large descending Greek sign is present before de. The next label has a wavy upper stroke, a tiny lower x and heavily retraced K/U strokes; their current outline does not securely distinguish the alternatives, and a separate earlier layer cannot be reconstructed. The last word has a d-like loop and upright, a detached apostrophe, and une; no separate l is visible. Reordering the Greek alternatives and resolving d\'une to C\'s first reading are not counted as changes against C.',
           'medium', False, 'misread word', 'Words'),
    change('p03', 'Main line 3: field in the algebraic-closure phrase',
           r"clôture algébrique de $\widetilde K_x$ --- \uline{et} d'une",
           r"clôture algébrique de $\tilde{L}_x$ --- \emph{et} d'une",
           r"clôture algébrique de $\widetilde K_x$ --- \uline{et} d'une",
           'The label has a separate upright and two oblique arms forming K, a visible wavy tilde and lower x. It has no L-shaped horizontal base. The circumflex in clôture, acute stroke in algébrique, independent underline beneath et and the literal d\'une are retained.',
           'high', False, 'misread symbol or index', 'Symbols and indices',
           consequential=True),
    change('p04', 'Main line 4, left and centre: crossed isom and quoted phrase',
           r'\deleted{\unsure{isom}} ``chemin de \unsure{domaines|chemins}'' entre',
           r'\struck{\ill{}} « domaine de \ill{} » entre',
           r"\deleted{\unsure{isom}} ``chemin de domaines'' entre",
           'The first live word begins with a c/h sequence and is read chemin; after de, the large loop and ascender of d are followed by o/m/a/i/n/e/s-like cursive strokes. Domaines is therefore C\'s first reading. Both quotation marks consist of paired short upright strokes, not angled guillemets. The cancelled isom remains doubtful because its middle strokes merge with the strike; the crop does not justify resolving every cancelled letter.',
           'high', False, r'readable ink left as \ill{}',
           'Readable ink left as illegible', True),
    change('p05', 'Main line 4, right: complete path to Spec(L)',
           r'$\unsure{\xi|\zeta}_{\widetilde U_x}\unsure{\mathrel{\text{---}}|\longrightarrow}\unsure{\widetilde K_x|\widetilde U_x}\longrightarrow\operatorname{Spec}(L)$',
           r'$\tilde{U}_x \to U$ \ill{} \uncertain{(Spec L)},',
           r'$\unsure{\zeta|\xi}_{\widetilde U_x}\longrightarrow\unsure{\widetilde K_x|\widetilde U_x}\longrightarrow\operatorname{Spec}(L)$',
           'The left Greek sign is separate from its visibly tilde-marked U_x subscript. The first short shaft has a small downward terminal barb on the right and no left head; the following shaft has a more pronounced right terminal hook. This supports two rightward arrows, the first at medium confidence. The middle field letter is strongly retouched with overlapping upright and diagonal/cup strokes; K versus U remains unsettled. Spec is followed by a genuine opening parenthesis, L and a closing parenthesis. No following comma is visible.',
           'medium', True, 'misread symbol or index', 'Symbols and indices', True,
           consequential=True),
    change('p06', 'Main line 5: second point, its field decoration and following prose',
           r'et $\unsure{\xi|\zeta}_L$ défini par $\unsure{\widetilde L|\overline L}$ --- ou ce qui',
           r'et $\mathcal{E}_L$ défini par $\overline{L}$ : \uncertain{i.e.} \uncertain{compris des situations}',
           r'et $\unsure{\zeta|\xi}_L$ défini par $\widetilde L$ --- ou ce qui',
           'The point sign is a long bent descending Greek form, not the double-lobed E used below. Its exact zeta/xi identity remains open. The decoration above the large L visibly bends up and down; it is a tilde rather than the flat bars over L elsewhere on this page. After it is a separate horizontal dash followed by ou ce qui. Resolving the tilde to C\'s first alternative and reordering the Greek alternatives do not count against C.',
           'high', False, 'misread symbol or index', 'Symbols and indices', True,
           consequential=True),
    change('p07', 'Between main lines 5–6 and main line 6: inserted qualification and overwritten L-hom',
           r"revient au $=$, \inserted{à isom près des \unsure{revts|relvts}} d'un $\unsure{K|L}$-hom de",
           r"\uncertain{revient} à \ill{}, d'un $\overline{L}$-\ill{} de",
           r"revient au $=$, \inserted{à isom près des \unsure{revts|relvts}} d'un $\deleted{\unsure{K}}L$-hom de",
           'The baseline explicitly reads revient au followed by two equality strokes and a separate low comma. Above it is à isom près des and a contracted final word whose tall central stroke does not securely settle revts versus relvts. A continuous line under this addition curves down to the baseline after the equality. In the following label the heavy upright and rightward base make live L; finer K-like upright/diagonal strokes survive behind it and are retained as a doubtful cancelled K. The line above is the insertion leader, not an overbar on L. The written -hom and de follow.',
           'medium', True, 'deletion state', 'Struck text', True,
           consequential=True),
    change('p08', 'Main line 7: two cancelled labels before tilde L_x and the end of the line',
           r"\deleted{$\unsure{K}$} \deleted{$\unsure{K}$} $\widetilde L_x$ dans $\overline L$ --- et ceci à son",
           r"\struck{\ill{}} $\tilde{L}_x$ dans $\overline{L}$ --- et ceci \ill{} \ill{}",
           r"\deleted{$\unsure{K_x|K}$} \deleted{$\unsure{K_x|K}$} $\widetilde L_x$ dans $\overline L$ --- et ceci à son",
           'Two distinct K-like forms are crossed by a zigzag cancellation. Each has an additional small lower-right loop/cross-shaped trace; these may be x subscripts rather than merely K exits, so K_x is retained as a doubtful reading with K as alternative. The following live label is a large L with a wavy tilde and lower x; the later L has a straight overbar. The words et ceci à son are present and legible.',
           'medium', True, 'omission', 'Omissions', True),
    change('p09', 'Main line 8: tour équivaut à la donnée d\'un',
           r"tour équivaut à la donnée d'un",
           r"donc \uncertain{équivaut} à la donnée d'un",
           r"tour équivaut à la donnée d'un",
           'The first word begins with a tall crossed t and a low joined our ending, not a d-loop and nc. The long q descender in équivaut, the raised accent stroke, and the rest of the phrase are visible. Tour continues the preceding à son.',
           'high', False, 'misread word', 'Words', True),
    change('p10', 'Main line 9: cancellation between x-prime and comme dessus',
           r"$x'$, \deleted{\uline{et} \unsure{d'un is}} comme dessus. Ceci",
           r"$x'$, \struck{et d'un \ill{}} \uncertain{comme} dessus. \uncertain{Ceci}",
           r"$x'$, \deleted{\uline{et} d'un is} comme dessus. Ceci",
           'A long oblique cancellation crosses et d\'un is. Under it, et has a separate short underline; the d loop/upright, apostrophe, un, dotted i and final s are distinguishable. The crossed phrase is not extended beyond the final s. The q descender from équivaut above is a separate vertical stroke and does not cancel additional live text. Comme dessus. Ceci is readable. Resolving the unlisted C doubt to its preferred d\'un is does not change C\'s base text and does not create a mark id.',
           'high', False, r'readable ink left as \ill{}',
           'Readable ink left as illegible', True),
    change('p11', 'Main line 10: isom can.',
           'posé, on a des isom can.',
           r'posé, on a des \uncertain{isom. canon.}',
           'posé, on a des isom can.',
           'Posé has a raised accent and a low comma. Isom ends without a separate stop. The next contraction has the c/a/n cursive outline and a distinct final dot; it is can., not an expanded canon. No omitted om/extra on strokes are supplied.',
           'high', False, 'abbreviation expanded or spelling modernised',
           'Abbreviations expanded, spelling modernised', True),
    change('p12', 'Formula (30), second row and raised surjectif',
           r"\text{Noyau de l'hom canonique }\inserted{\text{surjectif}}",
           r"\operatorname{Noyau} \text{ de l'homom. canonique}; \note{au-dessus de la seconde ligne, entre parenthèses et souligné, un mot lu sans certitude « \uncertain{surjectif} »}",
           r"\text{Noyau de l'hom canonique }\inserted{\text{surjectif}}",
           'The whole three-row formula, its left brace and number30 were read. The prose has l\'hom without an added om or stop. Surjectif is legible above canonique. A single curved line starts to its left, runs beneath it and turns down at the attachment; there is no independent pair of parentheses or separate underline. The slash through the barred L of the third-row source descends continuously from the y of Noyau; it is not a cancellation of L. Both isomorphism signs have a wave over a lower stroke, and the third-row map has a right head.',
           'high', False, 'insertion or placement',
           'Insertions put in the wrong place', True),
    change('p13', 'Four-line parenthesis beside and below formula (30)',
           r'(où la clôture \inserted{alg} $\overline{k(x)}$ de $k(x)$ est induite par la clôture alg. $\overline L$ de $\widetilde K_x$)',
           r'($\overline{k(x)}$ : clôture \uncertain{sép.} de $k(x)$ --- \uncertain{induite} par \uncertain{la} clôture alg. $\overline{L}$ de $\tilde{K}_x$)',
           r'(où la clôture \inserted{alg} $\overline{k(x)}$ de $k(x)$ est induite par la clôture alg. $\overline L$ de $\widetilde K_x$)',
           'The parenthesis starts with où la beside the map. The following line has clôture, a raised alg attached with a short V-shaped leader, then barred k(x), de k(x), est. It does not say sép. or put a colon after the first field. The next lines read induite par la clôture alg. and barred L de tilde K_x with a closing parenthesis. The K has an upright and two oblique arms, and its tilde is wavy. The source spelling alg/alg. and both circumflexes are retained.',
           'high', False, 'misread word', 'Words', True,
           consequential=True),
    change('p14', 'Five slanted margin lines to the left of formula (30)',
           r"Cf théorie galoisienne des traits henséliens. Ici $I_{x'}$ joue le rôle d'un $\pi_{\widetilde U_x/k(x)}^{\overline L}$ ; en fait il est $=\pi_{\widetilde U_x/\widetilde S_x}^{\overline L}$ !",
           r"Cf. Hensel \ill{} \ill{} \ill{} \ill{} \ill{} \ill{} \ill{} fait ici \ill{} \ill{} $I_{x'}$ \ill{} \ill{} $\pi^{\overline{L}}_{\tilde{U}_x/k(x)} = \pi^{\overline{L}}_{\tilde{U}_x/\tilde{S}_x}$ !",
           r"Cf théorie galoisienne\\ des traits henséliens\\ ici $I_{x'}$ joue le rôle\\ d'un $\unsure{\Pi|\pi}_{\widetilde U_x/k(x)}^{\overline L}$ ; en fait\\ il est $=\unsure{\Pi|\pi}_{\widetilde U_x/\widetilde S_x}^{\overline L}$ !",
           'The saved crop is rotated clockwise25 degrees. Five distinct rows read Cf théorie galoisienne / des traits henséliens / ici I_x-prime joue le rôle / d\'un [relative Pi expression] ; en fait / il est = [second expression] !. There is no secure stop after Cf or henséliens; ici begins with a dotted lowercase i. The two Pi-like signs have flat caps and posts, but their relative size does not securely establish case, so capital/lowercase remains open. The first denominator is k(x), the second tilde S_x; the field exponent is barred L in each. The semicolon and intervening words are real ink, not a single equality joining the two expressions.',
           'medium', True, 'misread word', 'Words', True),
    change('p15', 'Line following the closure parenthesis: Kummer reference and displaced comma',
           r'(\unsure{Alors} (27) est déduit par théorie de Kummer)',
           r'\uncertain{(dont} (27) est déduit par théorie de Kummer). \note{l\'appel « (27) » est surchargé ; la lecture du chiffre reste incertaine}',
           r'(\unsure{Alors} (27) est déduit par théorie de Kummer)\unsure{,}',
           'The first cursive word has a broad initial loop and compressed following strokes; Alors remains a tentative proposal rather than a resolved word. The live reference27 has a clear2 and descending crossed7 and is not the separately crossed reference below. Est déduit par théorie de Kummer is legible. A detached dark slanted tick sits below the right end near the closing parenthesis; it is preserved as an uncertain comma, with a pen-return interpretation still possible. No firm period is supplied.',
           'low', True, 'omission', 'Omissions', True),
    change('p16', 'Short cancelled formula between the Kummer line and the bottom paragraph',
           r'\deleted{$I_{x\prime}\simeq$}',
           r'\struck{$I_{x\prime} = \ill{}$}',
           r'\deleted{$I_{x\prime}\unsure{\simeq|=}$}',
           'The I has separate cap, stem and foot; a lower x and prime survive. To its right there is a low straight relation stroke and an upper loop/wave traversed by the oblique cancellation. Simeq is preferred but equality remains possible; the strike prevents a secure reading of the upper relation. There is no distinct additional text after the relation. This new uncertainty leaves C\'s preferred relation in first position and is not counted against C.',
           'medium', False, 'misread symbol or index', 'Symbols and indices', True),
    change('p17', 'Separately cancelled parenthesized reference above Je présume',
           r'\deleted{(\unsure{27|28})}',
           r'(\struck{\ill{}})',
           r'\deleted{(27)}',
           'The first digit has the rounded upper sweep and descending diagonal of2. The second has a distinct descending stem and crossbar, matching the live7 immediately above; crossing hatches account for the apparent extra loop that could suggest8. Both outer parentheses remain visible. The proposed cancelled27 is medium confidence. This resolves C\'s first alternative and therefore adds no correction against C and no invented mark id.',
           'medium', False, r'readable ink left as \ill{}',
           'Readable ink left as illegible', True),
    change('p18', 'First two lines of the bottom paragraph',
           r'Je présume que (dans la situation actuelle --- ou même, avec un corps de base $K$)',
           r'Supposons que (\uncertain{dans} la situation actuelle, \uncertain{il existe un} corps de base $K$ \ill{} \uncertain{premier}, \uncertain{\ill{}} $\mathbb{C}$.)',
           r'Je présume que (dans la situation actuelle --- ou même, avec un corps de base $K$)',
           'The initial large cursive J is followed by the legible présume que, including an accent stroke. The parenthesis reads dans la situation actuelle, continues with a dash at the next line\'s left, then ou même, avec un corps de base K and a closing parenthesis. There is no written il existe, premier or C phrase. The wording is conjectural Je présume, not Supposons.',
           'high', False, 'misread word', 'Words', True,
           consequential=True),
    change('p19', 'Last two main lines and raised a priori qualification',
           r"on a $N_{x'}=\operatorname{Norm}_{\mathcal E_L}(I_{x'})$, \inserted{(a priori, on a seulement $\subset$)} ce qui est lié à l'idée qu'on doit avoir $I_{x'}=\operatorname{Norm}_{\pi_{L/K}}(I_{x'})$",
           r"On a $N_{x'}=\operatorname{Norm}_{\mathcal E_L}(I_{x'})$, ce qui \uncertain{est lié} \ill{} à l'idée qu'\uncertain{on devrait avoir} $I_{x'}=\operatorname{Norm}_{\pi_{L/K}}(I_{x'})$",
           r"on a $N_{x'}=\operatorname{Norm}_{\mathcal E_L}(I_{x'})$, \inserted{(a priori, on a seulement $\subset$)} ce qui est lié à l'idée qu'on doit avoir $I_{x'}=\operatorname{Norm}_{\unsure{\Pi|\pi}_{L/K}}(I_{x'})$",
           'The raised addition visibly reads a priori, on a seulement followed by a left-opening inclusion sign. Its outer parentheses are independent of the attachment line; the latter runs beneath a priori and down after the first normalizer formula, so no independent underline is added. The baseline reads ce qui est lié and qu\'on doit avoir; there are no extra strokes for devrait. Both equality signs, both x-primes, E_L and the final L/K subscript are present. The small relative Pi-like sign has a cap and two legs but insufficient size contrast to settle case; its new case doubt alone is not counted against C. The complete lower audit region extends to the right paper edge and includes the final closing parenthesis.',
           'high', False, 'omission', 'Omissions', True,
           consequential=True),
    change('p20', 'Bottom left margin: question, paired long strokes, and thin folio118',
           r'\margin{$\Vert$ ?} ... \margin{118}',
           r'\marginal{? (\uncertain{trait vertical double} le long du paragraphe qui suit)}; [folio118 absent]',
           'A question mark to the left of two long, slightly converging vertical strokes, joined in a darker lower tip; folio118 below in a thinner hand.',
           'The question mark is separate from the two long lines. The lines run beside the full bottom paragraph, begin distinctly apart and approach/join at the dark lower end. The candidate uses a small TikZ reproduction for the lines and ordinary text for the question, preserving their relative positions rather than a generic short parallel sign. At the extreme lower left are two1 stems and a two-loop8 in a thinner foliation hand.',
           'high', True, 'drawing or diagram', 'Drawings and diagrams', True),
]

def decision(mark_id, outcome, reading, evidence, crop, confidence):
    return {'id': mark_id, 'cote': '149', 'scan': '119', 'decision': outcome,
            'reading': reading, 'evidence': evidence,
            'crop': f'crops/{PAGE}_{crop}.png', 'bbox': CROPS[crop][0],
            'confidence': confidence}

decisions = [
    decision('M0104', 'undecided', r'\unsure{\zeta|\xi}',
             'A separate long descending Greek sign stands after géom; the upper bends remain compatible with zeta or xi. Only the common preference order changes.', 'p02', 'low'),
    decision('M0105', 'undecided', r'\unsure{\widetilde K_x|\widetilde U_x}',
             'The tilde and lower x are distinct, but several upright, diagonal and curved strokes overlap in the retouched main letter; neither K/U identity nor a separate earlier layer is secure.', 'p02', 'low'),
    decision('M0106', 'first', "d'une",
             'There is a d-like loop/upright, a detached apostrophe and une; no separate l or separately written de une is required. The similar literal d\'une on the next line supports the stroke segmentation.', 'p02', 'medium'),
    decision('M0107', 'first', 'domaines',
             'A round d loop and ascender lead into o/m/a/i/n/e/s-like strokes after de; the word does not begin with the ch outline of chemin earlier in the same line.', 'p04', 'high'),
    decision('M0108', 'undecided', r'\unsure{\zeta|\xi}_{\widetilde U_x}',
             'The long Greek stem and upper bend are visible above/left of the tilde U_x subscript; the Greek identity remains open.', 'p05', 'low'),
    decision('M0109', 'alternative', r'\longrightarrow',
             'The short first shaft ends in a small downward barb on the right, like the clearer following map; its left end has no head.', 'p05', 'medium'),
    decision('M0110', 'undecided', r'\unsure{\widetilde K_x|\widetilde U_x}',
             'The middle letter of the whole path is heavily retraced; extra upright and cup/diagonal strokes keep both K and U possible. Its tilde and x are clear.', 'p05', 'low'),
    decision('M0111', 'undecided', r'\unsure{\zeta|\xi}_L',
             'The sign has a bent upper stroke and long descending stroke rather than the later E outline, but zeta and xi cannot be separated securely.', 'p06', 'low'),
    decision('M0112', 'first', r'\widetilde L',
             'The detached decoration above L visibly rises, dips and rises again; compare the unambiguously straight overbar on the following line\'s L.', 'p06', 'high'),
    decision('M0113', 'undecided', r'\unsure{revts|relvts}',
             'The contraction after des has a tall middle stroke and compressed final letters, but the potential l/v ligature does not securely distinguish the two written short forms.', 'p07', 'low'),
    decision('M0114', 'alternative', r'\deleted{\unsure{K}}L',
             'The heavy current stroke has the upright and long horizontal base of L. A finer K-like upright and two branches survive behind it; that earlier letter is separately retained as doubtful deleted ink. The line overhead is the insertion leader, not a bar on L.', 'p07', 'medium'),
    decision('M0115', 'undecided', r'\unsure{Alors}',
             'The broad initial loop and compressed following cursive strokes allow Alors, but all individual letters are not secure enough to resolve C\'s doubt.', 'p15', 'low'),
]

def element(n, kind, position, words, hand='his hand'):
    return {'sheet_kind': 'text', 'hand': hand, 'element': f'e{n:02d}',
            'kind': kind, 'position': position,
            'first_words_or_objects': words, 'transcribed': 'yes'}

inventory = [
    element(1, 'margin note', 'Top centre, above the first prose line', '59'),
    element(2, 'text', 'First ten main lines', "celui d'un rev. universel ... isom can."),
    element(3, 'deletion', 'Main line1 after universel', r'\unsure{(précis.|(precis.}'),
    element(4, 'insertion', 'Above main line1, leader to gap before d\'un', 'ou encore'),
    element(5, 'text', 'Main line2 retouched field label', r'\unsure{\widetilde K_x|\widetilde U_x}; earlier layer not independently recoverable'),
    element(6, 'text', 'Main line3, separately underlined conjunction', r'\uline{et}'),
    element(7, 'deletion', 'Beginning of main line4', r'\unsure{isom}'),
    element(8, 'text', 'Main line4 quoted phrase and complete path', r"``chemin de domaines'' entre [Greek point] ... Spec(L)"),
    element(9, 'insertion', 'Raised between lines5–6, continuous leader to after equality', r'à isom près des \unsure{revts|relvts}'),
    element(10, 'deletion', 'Under heavy L in line6 L-hom', r'\unsure{K}'),
    element(11, 'deletion', 'First cancelled label at line7 start', r'\unsure{K_x|K}'),
    element(12, 'deletion', 'Second cancelled label at line7 start', r'\unsure{K_x|K}'),
    element(13, 'deletion', 'Main line9 after x-prime comma', r"\uline{et} d'un is"),
    element(14, 'display', 'Three rows below isom can., left brace and number30', r'(30) N_{x\prime}\simeq ... ; I_{x\prime}\simeq ... ; E\longrightarrow E'),
    element(15, 'insertion', 'Above canonique in formula30, with continuous leader', 'surjectif'),
    element(16, 'text', 'Four-line parenthesis starting beside the third formula row', r'(où la clôture ... \widetilde K_x)'),
    element(17, 'insertion', 'Above the second line of that parenthesis, short V leader', 'alg'),
    element(18, 'margin note', 'Five slanting rows left of formula30 and its parenthesis', r'Cf théorie galoisienne ... il est = [relative Pi expression] !'),
    element(19, 'text', 'Kummer reference below the closure parenthesis', r'(\unsure{Alors} (27) est déduit par théorie de Kummer)\unsure{,}'),
    element(20, 'deletion', 'Short separate formula beneath the Kummer line', r'I_{x\prime}\unsure{\simeq|=}'),
    element(21, 'deletion', 'Separate crossed reference above Je présume', '(27)'),
    element(22, 'text', 'Last four main lines', r'Je présume que ... I_{x\prime}=Norm_{[relative Pi]_{L/K}}(I_{x\prime})'),
    element(23, 'insertion', 'Raised in the bottom paragraph, attached after the first Norm formula', r'(a priori, on a seulement \subset)'),
    element(24, 'drawing', 'Left of the bottom paragraph, beside separate question mark', 'Two long slightly converging strokes, dark joined lower tip'),
    element(25, 'margin note', 'Left of those strokes, near the upper part of their span', '?'),
    element(26, 'margin note', 'Extreme lower left', '118', 'thinner foliation hand'),
]

doubts = [
    {'place': 'Line1 cancelled word', 'reading': r'\deleted{\unsure{(précis.|(precis.}}', 'alternatives': 'p/r-initial contracted word; middle letters and accent obscured by the strike; no closing parenthesis supplied', 'confidence': 'low'},
    {'place': 'Line2 geometric-point sign', 'reading': r'\unsure{\zeta|\xi}', 'alternatives': r'\xi', 'confidence': 'low'},
    {'place': 'Line2 retouched field label', 'reading': r'\unsure{\widetilde K_x|\widetilde U_x}', 'alternatives': 'K/U and their retraced layers cannot be separated securely', 'confidence': 'low'},
    {'place': 'Line4 cancelled word before the quotation', 'reading': r'\deleted{\unsure{isom}}', 'alternatives': 'isom preferred; crossed middle strokes not individually secure', 'confidence': 'medium'},
    {'place': 'Line4 path initial Greek point', 'reading': r'\unsure{\zeta|\xi}_{\widetilde U_x}', 'alternatives': r'\xi_{\widetilde U_x}', 'confidence': 'low'},
    {'place': 'Line4 path middle retouched label', 'reading': r'\unsure{\widetilde K_x|\widetilde U_x}', 'alternatives': 'K/U and previous/live layer ordering remain open', 'confidence': 'low'},
    {'place': 'Line5 field point', 'reading': r'\unsure{\zeta|\xi}_L', 'alternatives': r'\xi_L', 'confidence': 'low'},
    {'place': 'Raised qualification between lines5–6', 'reading': r'\unsure{revts|relvts}', 'alternatives': 'The extra tall stroke may belong to an l in relvts rather than to the compressed revts connection.', 'confidence': 'low'},
    {'place': 'Line6 overwritten letter beneath live L-hom', 'reading': r'\deleted{\unsure{K}}L', 'alternatives': 'Earlier K-like form is partly obscured by the heavy live L.', 'confidence': 'medium'},
    {'place': 'Line7 first cancelled label', 'reading': r'\deleted{\unsure{K_x|K}}', 'alternatives': 'The small lower-right loop may be x or a K exit under the strike.', 'confidence': 'medium'},
    {'place': 'Line7 second cancelled label', 'reading': r'\deleted{\unsure{K_x|K}}', 'alternatives': 'The small lower-right loop may be x or a K exit under the strike.', 'confidence': 'medium'},
    {'place': 'Slanted margin first relative sign', 'reading': r'\unsure{\Pi|\pi}_{\widetilde U_x/k(x)}^{\overline L}', 'alternatives': r'\pi; cap and posts alone do not settle case', 'confidence': 'medium'},
    {'place': 'Slanted margin second relative sign', 'reading': r'\unsure{\Pi|\pi}_{\widetilde U_x/\widetilde S_x}^{\overline L}', 'alternatives': r'\pi; cap and posts alone do not settle case', 'confidence': 'medium'},
    {'place': 'Opening word of the Kummer parenthesis', 'reading': r'\unsure{Alors}', 'alternatives': 'Alors preferred, individual compressed letters unresolved', 'confidence': 'low'},
    {'place': 'After closing Kummer parenthesis, below the right line end', 'reading': r'\unsure{,}', 'alternatives': 'A displaced comma or a detached pen-return stroke; not a secure full stop', 'confidence': 'low'},
    {'place': 'Cancelled short I formula below the Kummer line', 'reading': r'\deleted{I_{x\prime}\unsure{\simeq|=}}', 'alternatives': 'Equality possible because the upper wave is crossed by the cancellation; this is new uncertainty, not a changed C base reading', 'confidence': 'medium'},
    {'place': 'Final Norm formula relative sign', 'reading': r'\operatorname{Norm}_{\unsure{\Pi|\pi}_{L/K}}(I_{x\prime})', 'alternatives': r'\pi; the small index position prevents a secure case comparison', 'confidence': 'medium'},
]

tex = (HERE / f'{PAGE}.tex').read_text()
top, lower = tex.split('\\[', 1)
top_reading = top.replace('\\scanpage{119}\n', '', 1).strip()
lower_reading = '\\[' + lower.strip()
audit_boxes = [
    {'box': 'b01', 'kind': 'insertion; deletion; handwritten number; doubtful formula; C/H word difference; less-than-high C departure',
     'bbox': [300, 25, 1679, 1168], 'reading': top_reading},
    {'box': 'b02', 'kind': 'insertion; margin note; deletion; handwritten number; doubtful formula; C/H word difference; less-than-high C departure',
     'bbox': [18, 1169, 1679, 2349], 'reading': lower_reading},
    {'box': 'b03', 'kind': 'deletion; doubtful formula; C/H word difference',
     'bbox': CROPS['p16'][0], 'reading': r'\deleted{$I_{x\prime}\unsure{\simeq|=}$}'},
    {'box': 'b04', 'kind': 'deletion; handwritten number; C/H word difference',
     'bbox': CROPS['p17'][0], 'reading': r'\deleted{(27)}'},
]

data = {
    'page': PAGE, 'scan': 119, 'reader': 'reader_b',
    'line_count': 37,
    'line_count_detail': {'main': 23, 'diagram': 0, 'margin': 6, 'insertion': 5, 'standalone_numbers': 3},
    'changes': changes, 'decisions': decisions, 'inventory': inventory,
    'doubts': doubts, 'audit_boxes': audit_boxes,
    'notes': [
        'This leaf continues a discussion of universal covers, geometric points and fields. Formula(30) identifies the written N and I expressions, and a slanting note compares the inertia expression to relative Pi notation. These are descriptions of the manuscript, not verified mathematical results.',
        'The last paragraph explicitly starts Je présume and includes the raised qualification a priori, on a seulement [inclusion sign]. Its conjectural status is retained; no proof verification was performed.',
        'Literal K and L labels are preserved independently. The unretouched K_x in the algebraic-closure phrase and the closing parenthesis is clear; the two earlier retouched K/U labels remain open. The heavy live L in L-hom has a finer doubtful K layer beneath it. No field name is regularized from the argument.',
        'All three geometric-point signs retain zeta/xi uncertainty. The two relative Pi-like margin signs and the final relative sign in the Norm subscript retain uppercase/lowercase uncertainty; flat caps with two posts do not alone decide case. No mathematical consequence is asserted solely from that case preference.',
        'The ou encore and à isom... additions have continuous attachment leaders. Surjectif has one curved under-running leader rather than independent parentheses/underlining. The a priori addition has genuine outer parentheses but its lower line is the leader. Raised alg has a short V-like leader before barred k(x). No punctuation is inferred from any of these leaders.',
        'The y descender of Noyau crosses the upper bar/L of the next formula row without deleting it. The q descender of équivaut above is distinct from the strike through et d\'un is.',
        'The separately cancelled parenthesized27 is resolved from its visible descending seven-stem and crossbar, compared with the live27 above. Its second digit was not decided from numerical sequence or formula content.',
        'The detached dark tick below the right end of the Kummer parenthesis is transcribed as an uncertain comma, with a pen-return interpretation retained in doubts. The cancelled opening word near the top has uncertain middle letters and uncertain accent and remains marked accordingly.',
        'The paired long margin strokes are reproduced with their slight convergence and darker joined lower tip; the adjacent question mark remains text. The thin lower-left118 is recorded as foliation in a different-looking hand, distinct from the author\'s59.',
        'The line count uses logical written baselines: top prose10; formula30 three rows; closure parenthesis four rows, including the independent (où la beside the map; Kummer line1; cancelled I formula1; bottom prose4 = main23. Five slanted margin rows plus the separate question/paired-stroke element = margin6. Five raised insertions are counted separately. Author59, cancelled27 and thin folio118 are separate numbering lines; formula30 and live27 already lie on counted main rows.',
        'Audit boxes b01 and b02 contain complete upper and lower text regions. The wide lower region avoids clipping the interleaved slanted margin, formula, parenthesis and bottom paragraph, and reaches the right paper edge for the final parenthesis. Two isolated boxes additionally expose the short cancelled formula and cancelled reference without witness-based labels.',
        'The full page was inspected once and each native half once, followed by one saved enlarged crop for each listed place. Every crop p01–p21 was visually inspected. The margin crop was rotated clockwise25 degrees. No OCR, external source, other page, or TeX compilation was used.',
        'Static metadata checks verify exact supplied mark ids, unique change ids, existing crop references, valid image-coordinate boxes and the line-count sum. These checks do not establish the mathematical claims.',
    ],
    'checks': [],
    'hand_observations': [
        {'habit': 'Very short rightward maps can have only a small downward terminal barb.', 'places': 'Line4 complete path; formula30 third row', 'holds': 'Both endpoints of each local shaft were inspected; the first short map is medium confidence.', 'witness_errors': 'C left the first short shaft as dash/arrow; H omitted much of the path.'},
        {'habit': 'Insertion leaders may run under words and turn like parentheses or punctuation.', 'places': 'ou encore; à isom près...; surjectif; alg; a priori', 'holds': 'Each leader was traced independently. The a priori parentheses are separate real strokes, unlike the apparent enclosure of surjectif.', 'witness_errors': 'H described extra parentheses/underline around surjectif and omitted or misread the other additions.'},
        {'habit': 'A heavy replacement can retain a finer earlier letter beneath it.', 'places': 'Line6 L-hom and the two retouched labels in lines2/4', 'holds': 'Live L over doubtful K is distinguishable at L-hom. The K/U labels do not permit secure layer separation and remain unresolved.', 'witness_errors': 'C did not separately retain the finer K under L; H treated the leader as an overbar.'},
        {'habit': 'Tiny lower-right strokes in cancelled capitals can be subscripts.', 'places': 'Both cancelled K-like forms at line7 start', 'holds': 'Both have x-like traces, but neither is forced beyond K_x|K.', 'witness_errors': 'C gave bare doubtful K twice; H reduced the cluster to unreadable cancellation.'},
        {'habit': 'Relative Pi-like signs with flat caps and posts can remain case-ambiguous.', 'places': 'Two slanted margin formulae and final Norm subscript', 'holds': 'Case remains open in all three local occurrences; no cross-page shape is used to settle them.', 'witness_errors': 'Both witnesses print lowercase pi without expressing the local case uncertainty.'},
        {'habit': 'Long descenders may cross the following line without being cancellation strokes.', 'places': 'équivaut q above et d\'un is; Noyau y above barred L', 'holds': 'The continuous connections to the parent letters are visible.', 'witness_errors': 'No extra cancellation is introduced from either crossing.'},
        {'habit': 'The seven has a descending stem and a separate crossing bar.', 'places': 'Live27 in the Kummer line; separately cancelled27 below', 'holds': 'The visible stem/crossbar is shared by both local sevens despite cancellation hatches below.', 'witness_errors': 'C left the cancelled digit as27|28; H conflated an uncertain reference with the clear live27.'},
        {'habit': 'Contractions omit stops that an expansion might invite.', 'places': 'pt géom; isom can.; hom; inserted alg; margin Cf', 'holds': 'Only can., rev., i.e. and the later alg. have the corresponding written stops in their local occurrences.', 'witness_errors': 'H expanded géom, hom and can and supplied a stop after isom/Cf.'},
    ],
    'notation': [
        {'written': r'\unsure{\zeta|\xi}', 'meaning_or_use': 'The geometric-point sign; identity remains unresolved.', 'places': 'Three occurrences in the top paragraph'},
        {'written': r'\unsure{\widetilde K_x|\widetilde U_x}', 'meaning_or_use': 'Retouched labels in the point description and complete path; no secure prior/live layer separation.', 'places': 'Main lines2 and4'},
        {'written': r'\widetilde K_x', 'meaning_or_use': 'Literal field label in the two algebraic-closure phrases.', 'places': 'Main line3; closure parenthesis below formula30'},
        {'written': r'\widetilde L;\ \widetilde L_x;\ \overline L', 'meaning_or_use': 'Distinct written L decorations and indexing preserved from local ink.', 'places': 'Top paragraph; formula30; closure parenthesis; slanted margin'},
        {'written': r'N_{x\prime}\simeq\mathcal E_{\widetilde U_x}^{\overline L}', 'meaning_or_use': 'First identification written in formula30.', 'places': 'Formula30 first row'},
        {'written': r'I_{x\prime}\simeq\text{Noyau de l\'hom canonique surjectif }\mathcal E_{\widetilde U_x}^{\overline L}\longrightarrow\mathcal E_{\overline{k(x)}}', 'meaning_or_use': 'Second identification, with surjectif added above the row.', 'places': 'Formula30 second and third rows'},
        {'written': r'\unsure{\Pi|\pi}_{\widetilde U_x/k(x)}^{\overline L};\ \unsure{\Pi|\pi}_{\widetilde U_x/\widetilde S_x}^{\overline L}', 'meaning_or_use': 'Two relative expressions in the margin; case is not resolved.', 'places': 'Slanted margin rows4–5'},
        {'written': r'N_{x\prime}=\operatorname{Norm}_{\mathcal E_L}(I_{x\prime});\ I_{x\prime}=\operatorname{Norm}_{\unsure{\Pi|\pi}_{L/K}}(I_{x\prime})', 'meaning_or_use': 'Literal normalizer assertions in the paragraph introduced by Je présume, with the a priori inclusion qualification.', 'places': 'Last two main lines'},
        {'written': '=', 'meaning_or_use': 'Short form for même in revient au =; ordinary equality separately in the formulae.', 'places': 'Main line6; later equations'},
    ],
    'abbreviations': [
        {'written': 'rev.', 'expansion': 'revêtement'},
        {'written': 'pt', 'expansion': 'point'},
        {'written': 'géom', 'expansion': 'géométrique'},
        {'written': 'i.e.', 'expansion': 'id est'},
        {'written': 'isom', 'expansion': 'isomorphisme / isomorphismes, according to the local phrase'},
        {'written': 'can.', 'expansion': 'canoniques'},
        {'written': 'hom', 'expansion': 'homomorphisme'},
        {'written': 'alg; alg.', 'expansion': 'algébrique'},
        {'written': 'Cf', 'expansion': 'confer'},
        {'written': r'\unsure{revts|relvts}', 'expansion': 'revêtements / relèvements; the written contraction remains unresolved'},
    ],
    'inspection': {'whole': True, 'halves': ['top', 'bottom'],
                   'crops': [f'crops/{PAGE}_{p}.png' for p in CROPS],
                   'deletions_insertions_checked': True},
}

if __name__ == '__main__':
    with (ROOT / 'packets/149_scan119/marks.tsv').open(newline='') as stream:
        supplied_ids = {row['id'] for row in csv.DictReader(stream, delimiter='\t')}
    assert supplied_ids == {d['id'] for d in decisions}
    assert len({c['id'] for c in changes}) == len(changes)
    assert sum(data['line_count_detail'].values()) == data['line_count']
    for item in changes + decisions:
        assert (ROOT / 'edition' / item['crop']).is_file()
    for item in changes + decisions + audit_boxes:
        x0, y0, x1, y1 = item['bbox']
        assert 0 <= x0 < x1 <= 1679 and 0 <= y0 < y1 <= 2365
    target = HERE / f'{PAGE}.json'
    if target.exists():
        raise FileExistsError(f'Refusing to overwrite frozen metadata: {target}')
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(f'{PAGE}: {len(changes)} changes ({sum(c["vs_C"] for c in changes)} against C), '
          f'{len(CROPS)} crops, {len(doubts)} doubts, {len(audit_boxes)} audit boxes, '
          f'{len(decisions)} supplied-mark decisions; line_count={data["line_count"]}.')
