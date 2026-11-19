from pathlib import Path
from datetime import datetime, timezone
import json
import re

ROOT = Path('/workspace/scratch/17347c1714f0')
OUT = ROOT / 'out/readers/scan006/R2'
PACKET = ROOT / 'packets/scan006'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
HD = (PACKET / 'H_drawing_01-3.tex').read_text()
R = (OUT / 'reading.tex').read_text()
findings = []

def add(place, c, h, reading, *, dc=False, dh=False, doubt=None,
        kind='other', marked=False, evidence='', crop=None,
        confidence='high', unresolved=False, consequential=False):
    if c:
        assert c in C, ('C snippet not found', place, c)
    if h is not None:
        assert h in H or h in HD, ('H snippet not found', place, h)
    assert reading in R, ('Reading snippet not found', place, reading)
    findings.append({
        'id': f'R2-006-{len(findings)+1:02d}', 'place': place,
        'c': c, 'h': h, 'reading': reading, 'diff_c': dc, 'diff_h': dh,
        'c_doubt': doubt is not None, 'c_doubt_id': doubt, 's_id': None,
        'kind': kind, 'marked_in_H': marked, 'evidence': evidence,
        'crop': str(OUT / (crop + '.jpg')) if crop else None,
        'confidence': confidence, 'unresolved': unresolved,
        'consequential': consequential,
    })

add('Opening script capital', r'\unsure{\mathcal{X}|\mathscr{X}}',
    r'\mathcal{X}', r'\unsure{\mathcal{X}|\mathscr{X}}', dh=True,
    doubt='C-D01', kind='other',
    evidence='Two sweeping crossing curves and a separate transverse stroke establish a script X distinct from the straight X at the map target. The crop does not choose a unique script typeface.',
    crop='01_script_x', confidence='medium', unresolved=True)
add('Opening words after the script capital', r'qui est \unsure{aussi}',
    r"\uncertain{peut aussi s'identifier à}", 'qui est aussi', dc=True, dh=True,
    doubt='C-D02', kind='misread word', marked=True,
    evidence='Half a shows the descending q of qui, a separate est, and the short waves and dots of aussi. There are no strokes for peut or s\u2019identifier à.')
add('Opening: somme amalgamée', r'\unsure{somme amalgamée}',
    r'\uncertain{somme amalgamée}', 'somme amalgamée', dc=True, dh=True,
    doubt='C-D03', marked=True,
    evidence='Half a shows the two-word run, the descending loop of g in amalgamée, and the terminal accented ending. The lexical reading is settled.', confidence='medium')
add('First de: cancelled ending', r'de\deleted{\unsure{s}}',
    'des', r'de\deleted{\unsure{s}}', dh=True, doubt='C-D04',
    kind='deletion state (struck given live or live given struck)',
    evidence='After the intact looped de is a long flattened loop with an overlying retrace and final downstroke. A cancelled s remains the best candidate, but the letter is not independently clear.',
    crop='02_first_de', confidence='low', unresolved=True)
add('Second de: cancelled ending', r'de\deleted{s}', 'des',
    r'de\deleted{s}', dh=True,
    kind='deletion state (struck given live or live given struck)',
    evidence='The second de has a shorter blackened horizontal ending and a downstroke. It repeats the uncertain cancelled s of the first de; absence of another uncertainty marker is not increased confidence.',
    crop='03_second_de', confidence='low', unresolved=True)
add('Word at the opening parenthesis', r'\unsure{sur}', 'via',
    r'\unsure{sur}', dh=True, doubt='C-D05', kind='misread word',
    evidence='The first small glyph is a curved hook, followed by detached marks and a long low terminal stroke. These favour sur, but the cramped strokes remain incomplete; via is not supported.',
    crop='04_sur', confidence='low', unresolved=True)
diagram = R[R.index(r'\diagram{'):R.index(') :')].rstrip()
add('Opening diagram: common source with horizontal and descending arrows',
    diagram,
    '$\\coprod_i B_i \\hookrightarrow \\overline{W}$,\n$\\coprod_i B_i \\to \\coprod_i \\overline{U_i}$',
    diagram, dh=True, kind='drawing or diagram',
    evidence='Half a shows one coproduct B_i at the fork, the hooked horizontal arrow to barred W, and the descending arrow to the coproduct of barred U_i. H gives two separate inline maps; its objects and labels are present, not omitted.')
add('Cancelled heading: naturelle',
    "\\deleted{L'application \\unsure{naturelle}}",
    "\\struck{L'application naturelle}", "\\deleted{L'application naturelle}",
    dc=True, doubt='C-D06',
    evidence='The crossed line leaves the tall t and terminal relle visible, while the beginning has the low na strokes. The whole heading reads L\u2019application naturelle.',
    crop='05_cancelled_heading', confidence='medium')
add('Cancelled small word before the cancelled map',
    r'\deleted{\unsure{\text{de}}\quad\mathcal{X}\longrightarrow X}',
    r'\struck{$\mathcal{X} \to X$}',
    r'\deleted{\unsure{\text{de}}\quad\mathcal{X}\longrightarrow X}',
    dh=True, doubt='C-D07', kind='omission',
    evidence='A closed lower-left bowl and an upright loop survive in the crossed cluster before the map. They favour de; the second letter is obscured. H omits this cluster.',
    crop='06_cancelled_de', confidence='low', unresolved=True)
add('Main display: overwritten union before the live coproduct',
    r'\deleted{\unsure{\bigcup}}\coprod_i\overline U_i',
    r'\Bigl(\coprod_i \overline{U_i}\Bigr)',
    r'\deleted{\unsure{\bigcup}}\coprod_i\overline U_i',
    dh=True, doubt='C-D08', kind='omission',
    evidence='The live operator has upright posts and a horizontal foot; lower rounded remnants and extra curved legs remain underneath. A prior union is plausible but not fully separable from the overwrite.',
    crop='07_overwritten_operator', confidence='low', unresolved=True)
add('Second display row: parenthesized letter below the coproduct',
    r'\coprod_{i\,(\unsure{W|w})}X_i',
    r'\coprod_{i\,(W)} X_i', r'\coprod_{i\,(\unsure{w|W})}X_i',
    dc=True, dh=True, doubt='C-D09', kind='misread symbol or index',
    evidence='The letter has two rounded low troughs and a central peak; its shape favours lowercase w. A small handwritten capital W cannot be excluded, so both candidates are retained in ink-first order.',
    crop='08_coproduct_suffix', confidence='medium', unresolved=True, consequential=True)
add('Side display: subscript on the first plain X',
    r'X_{\unsure{w|i}}\simeq\mathcal X_i', r'X_i \simeq \mathcal{X}_i',
    r'X_{\unsure{w|i}}\simeq\mathcal X_i', dh=True, doubt='C-D10',
    kind='misread symbol or index',
    evidence='The lower-right continuation of X turns up, down, then up again with no separate dot. It favours w; a compressed undotted i remains possible. The adjacent script-X subscript and the Im-X subscript are i-like and are not silently used to repair this one.',
    crop='09_side_formula_gloss', confidence='low', unresolved=True, consequential=True)
add('Arrowed gloss: ouvert', r'\unsure{ouvert}', r'\uncertain{ouvert}',
    'ouvert', dc=True, dh=True, doubt='C-D11', marked=True,
    evidence='The enlarged gloss gives the initial rounded o/u group, low ve/r continuation and short terminal t, followed by de and the script X.',
    crop='09_side_formula_gloss', confidence='medium')
old_arrow = r'\tikz[baseline=-.2ex]{\draw[->] (.38,.25) to[bend right=12] (0,0);}'
new_arrow = r'\tikz[baseline=-.2ex]{\draw (.58,.34) .. controls (.44,.36) and (.15,.12) .. (0,0); \draw (0,0) .. controls (-.08,.09) and (-.13,.06) .. (-.09,0) .. controls (-.05,-.04) and (.01,-.01) .. (0,0) -- (.08,.025);}'
add('Arrow to the gloss: small closed return at the down-left tip',
    old_arrow, 'une flèche', new_arrow, dc=True, dh=True, kind='drawing or diagram',
    evidence='The curved line ends in a small closed loop with a short right-going terminal stroke. The reading traces both sides of that loop. C uses a standard pointed arrowhead; H acknowledges an arrow in words but has no corresponding drawn stroke.',
    crop='09_side_formula_gloss')
add('First abbreviation for points below the display', r'\unsure{pts}',
    'pts', 'pts', dc=True, doubt='C-D12',
    evidence='Half a shows the long descending p and the raised compact ts; the same form recurs later in the sentence.')
add('Connector between the two map assertions', "c'est une", r'i.e.\ une',
    "c'est une", dh=True, kind='misread word',
    evidence='Half a has a curved c followed by the raised apostrophe and est before une. It does not show i.e.')
add('Abbreviation and adjective before en les pts', r'\unsure{imm} fermée',
    r'\ill{} \uncertain{fermée}', 'imm fermée', dc=True, dh=True,
    doubt='C-D13', kind=r'readable ink left as \ill{}', marked=True,
    evidence='The crop shows a dotted initial i followed by two low connected m-like waves. Fermée has a tall f, low middle strokes and the accented final vowel. No abbreviation point is visible.',
    crop='11_imm', confidence='medium')
add('Complement sign in the first map assertion',
    r'\mathcal X\smallsetminus\coprod_i C_i',
    r'\mathcal{X} - \coprod_i C_i', r'\mathcal X\smallsetminus\coprod_i C_i',
    dh=True, kind='misread symbol or index',
    evidence='Half a shows a short descending oblique stroke between the script X and the coproduct, represented as a set-difference slash.', consequential=True)
add('End of the map-assertion paragraph', r'$\coprod C_i$',
    r'$\coprod C_i$.', r'$\coprod C_i$', dh=True, kind='text not on the page',
    evidence='Half a ends with the C subscript i; no separate sentence period follows it.')
add('Item 6: first word', '6) Énoncé', r'6) \uncertain{Lemme}',
    '6) Énoncé', dh=True, kind='misread word', marked=True,
    evidence='Half b shows the tall accented É and the following noncé. The first word is not Lemme.')
add('Item 6: invariance', r"d'\unsure{invariance}", "d'immersion",
    "d'invariance", dc=True, dh=True, doubt='C-D14', kind='misread word',
    evidence='Half b gives initial in, a v-shaped turn, the separated r/i marks and the final ance run. The reading is invariance, without a doubt marker.', consequential=True)
add('Item 6: relation to replacement of K',
    r'par rapport au \unsure{remplacement} de',
    '\\ill{}\n\n\\uncertain{remplaçant} au voisinage de',
    'par rapport au remplacement de', dc=True, dh=True, doubt='C-D15',
    kind='misread word', marked=True,
    evidence='Half b places par at the end of the first line and rapport au remplacement de on the next. The tall p/l strokes and terminal ment are visible; no voisinage is written.')
add('Interlinear replacement formula: star-shaped superscripts and insertion',
    r"\inserted{$U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*$}",
    r"$U'^{*}_i = U'_i \cap K^{*}$",
    r"\inserted{$U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*$}",
    dh=True, doubt='C-D16', kind='insertion or placement',
    evidence='A guide beneath the interlinear formula bends down into the point after the first replacement formula. The two small raised signs have peaked limbs and a short retrace, compatible with compressed stars or wedges. The first is marked; the later K-star here inherits the same unresolved status.',
    crop='12_inserted_superscripts', confidence='medium', unresolved=True, consequential=True)
add('Item 6: condition-introducing words', r'\unsure{pourvu} que',
    r'\uncertain{on suppose} que', 'pourvu que', dc=True, dh=True,
    doubt='C-D17', kind='misread word', marked=True,
    evidence='Half b has the descending p, low ourvu waves and separate que. There is no separate on or suppose.')
add('Slanted margin, first line', r'\unsure{vérifier}', 'vérifier',
    'vérifier', dc=True, doubt='C-D18',
    evidence='After rotation, the crop shows the initial v, accented é, the dotted short strokes and the long f. The word is vérifier.',
    crop='13_slanted_margin')
add('Slanted margin, second line', "l'énoncé", r'\ill{}',
    "l'énoncé", dh=True, kind=r'readable ink left as \ill{}', marked=True,
    evidence='The rotated crop shows a looped l, apostrophe, accented initial vowel, nonc run and terminal acute; this line reads l\u2019énoncé.',
    crop='13_slanted_margin')
add('Slanted margin, third line', r'\unsure{précis}\ldots',
    r'\ill{}…', r'précis\ldots', dc=True, dh=True, doubt='C-D19',
    kind=r'readable ink left as \ill{}', marked=True,
    evidence='The rotated crop shows the long p descender, accented short group and terminal s followed by three separate dots.',
    crop='13_slanted_margin')
add('Cancelled original condition before the inserted dotted K-star condition',
    r"\deleted{$\unsure{K'|\dot K'}\subset\bigcup U_i$, et}",
    r'\struck{$\dot{K} \subset \bigcup U_i$, et}',
    r"\deleted{$\unsure{K'|\dot K'}\subset\bigcup U_i$, et}",
    dh=True, doubt='C-D20', kind='misread symbol or index',
    evidence='The original K has a distinct high right tick, hence a prime. A possible overdot is entangled with the opening zigzag/arrowlike cancellation stroke; plain K-prime remains the leading candidate.',
    crop='14_replaced_condition', confidence='low', unresolved=True, consequential=True)
add('Inserted boundary condition: union sign and placement',
    r'\inserted{$\dot K^*\subset\bigcup U_i$, et}',
    r'$\dot{K}^{*} \subset U_i$, et',
    r'\inserted{$\dot K^*\subset\bigcup U_i$, et}',
    dh=True, kind='misread symbol or index',
    evidence='Above the crossed original line are a separate dot over K, a many-rayed star, the inclusion sign and a tall separate union before U_i. The new condition is an interlinear replacement; H omits its union.',
    crop='14_replaced_condition', consequential=True)
add('Cancelled parenthesis: raised final dash',
    r"\deleted{(K\smallsetminus K')^{\unsure{-}}}",
    r"\struck{$(K \setminus K')$}",
    r"\deleted{(K\smallsetminus K')^{-}}", dc=True, dh=True,
    doubt='C-D21', kind='omission',
    evidence='A thick horizontal raised dash stands just beyond the closing parenthesis, independent of the thinner oblique cancellation lines. The crossing oblique line does not make this an independently written arrow.',
    crop='15_cancelled_parenthesis', confidence='medium', consequential=True)
add('Quantifier following the cancelled parenthesis', r'\forall i',
    r'= V_i', r'\forall i', dh=True, kind='misread symbol or index',
    evidence='The crop gives two upward limbs joined by the low curved turn and a crossbar, followed by a dotted i. There is no equals sign or indexed V.',
    crop='15_cancelled_parenthesis', consequential=True)
add('Scribbled symbol after il suffit que', r"\deleted{\unsure{K^*|K'}}",
    r'\struck{\ill{}}', r"\deleted{\unsure{K^*|K'}}", dh=True,
    doubt='C-D22', kind=r'readable ink left as \ill{}', marked=True,
    evidence='The long stem and diverging lower legs of K survive. Upper rays are covered by repeated cancellation strokes, leaving star versus prime unresolved; the visible K should not be replaced by an unreadable-word marker.',
    crop='16_sufficient_condition', confidence='low', unresolved=True, consequential=True)
add('Live word immediately before K-prime in the sufficient condition',
    'soit', r'\operatorname{int}', r'\operatorname{int}', dc=True,
    kind='misread word',
    evidence='The crop shows a separate dotted i, one long low n, and a raised terminal t before K-prime. There is no initial s or o. The ink reads int, agreeing with H.',
    crop='16_sufficient_condition', consequential=True)
add('Dash after the opening parenthesis of the sufficient condition',
    '(- il suffit que', '(il suffit que', '(- il suffit que', dh=True,
    kind='omission',
    evidence='Half b shows a distinct short dash immediately after the opening parenthesis and before il.')
add('End of the sufficient-condition line', r'\bigcup C_i$',
    r'\bigcup C_i$.', r'\bigcup C_i$', dh=True, kind='text not on the page',
    evidence='Half b and the close crop finish at C_i without a separate period or a closing parenthesis. The manuscript parenthesis remains open.',
    crop='16_sufficient_condition')
add('Final verification request: abbreviated div. and following noun',
    r'\unsure{div.} hypothèses', 'développements', 'div. hypothèses',
    dc=True, dh=True, doubt='C-D23',
    kind='abbreviation expanded or spelling modernised',
    evidence='Half b shows the separate d, i, v and final point before the long word hypothèses. H substitutes développements for this written abbreviation-plus-noun sequence.')
add('Own page numeral above the archival number', r'\mspage{\unsure{5}}',
    r'\page{5}', r'\mspage{5}', dc=True, doubt='C-D24',
    evidence='The close view gives a slanting top bar, a descending bent stem and a lower return loop. It is the author\u2019s freehand 5, distinct from the darker archival 5 at the corner.',
    crop='17_page_number', confidence='medium')

thin_h = r'\draw (22.5,-30.6) -- (26.3,-32.3) -- (40.7,-44.3);'
thick_h = {
    'left': r'\draw[very thick] (49.5,-49.6) -- (40.7,-44.3);',
    'right': r'\draw[very thick] (49.5,-49.6) -- (59,-45.5);',
    'lower': r'\draw[very thick] (49.5,-49.6) -- (46.7,-60);',
}
for place, segment, h_segment, evidence in [
    ('Drawing: transverse tick near the upper-left outer junction',
     '(-1.65,1.10)--(-1.58,1.23)', thin_h,
     'A short dark diagonal crosses the thin descending line just inside the upper-left junction.'),
    ('Drawing: second tick on the thin upper-left branch',
     '(-.90,.60)--(-.88,.66)', thin_h,
     'A very short upward spur meets the thin line shortly before the heavy B_3 endpoint.'),
    ('Drawing: cross-stroke at B_3',
     '(-.75,.25)--(-.62,.53)', thick_h['left'],
     'A broad diagonal stroke projects to both sides of the heavy upper-left branch at its outer endpoint.'),
    ('Drawing: cross-stroke by C_3',
     '(-.34,.07)--(-.26,.26)', thick_h['left'],
     'A diagonal transverse mark has a lower-left projection and an upper-right continuation by C_3.'),
    ('Drawing: cross-stroke by C_2',
     '(.36,.09)--(.29,.25)', thick_h['right'],
     'A short almost upright stroke crosses the right heavy branch beside C_2.'),
    ('Drawing: cross-stroke by C_1',
     '(-.17,-.34)--(.01,-.32)', thick_h['lower'],
     'A near-horizontal short bar projects to both sides of the descending heavy branch beside C_1.'),
]:
    add(place, segment, h_segment, segment, dh=True, kind='drawing or diagram',
        evidence=evidence + ' C includes this mark. The actual H asset has only the branch path here; its comments acknowledge two omitted thin-branch ticks but do not draw them or these heavy-branch cross-strokes.',
        crop='10_drawing_ticks')
new_loop = r'\draw (-1.92,1.36) .. controls (-1.75,1.37) and (-1.61,1.32) .. (-1.58,1.14);'
add('Drawing: second edge of the narrow upper-left return loop', '', None,
    new_loop, dc=True, dh=True, kind='drawing or diagram',
    evidence='The source has two distinct thin edges enclosing a narrow white lens between the outer junction and its first transverse tick. Neither supplied drawing source includes the second edge; this is an added actual stroke, not a cosmetic reparameterization.',
    crop='10_drawing_ticks')
vertical = r'\margin{\tikz{\draw[line width=.3pt] (0,0) .. controls (-.04,.25) and (-.05,.6) .. (0,.9);}}'
add('Independent vertical pen stroke beside the final line', vertical, None,
    vertical, dh=True, kind='omission',
    evidence='Half b shows one long slightly bowed vertical stroke immediately left of the concluding text. C draws it; H has no counterpart.')
short_mark = r'\margin{\tikz[baseline=-.2ex]{\draw[line width=.3pt] (0,0) -- (.015,-.07);}}'
add('Detached short pen stroke below-left of the own page numeral', '', None,
    short_mark, dc=True, dh=True, kind='omission',
    evidence='The numeral crop shows a short separate dark downstroke below-left of the 5. It is reproduced as an independent mark rather than interpreted as part of the number.',
    crop='17_page_number')

observations = [
    'Script X established by crossing curves and transverse stroke; mathcal versus mathscr remains unresolved.',
    'Retraced elongated ending after de; cancelled s remains uncertain.',
    'Shorter blackened ending after the second de; same uncertain cancelled s as the first occurrence.',
    'Cramped curved first glyph and low terminal stroke favour sur; uncertainty retained, via not supported.',
    'L\u2019application naturelle read under a horizontal cancellation; naturelle resolved.',
    'Initial bowl and upright loop favour de before the map; uncertainty retained.',
    'Coproduct is live; underlying rounded remnants favour a cancelled union, still uncertain.',
    'Two rounded troughs favour lowercase w; W retained as an alternative, reordered to w|W.',
    'First subscript w|i retained; ouvert resolved; parallel strokes and Im X_i confirmed; loop-headed down-left arrow traced.',
    'Six transverse marks and all B/C subscripts confirmed; a second thin edge at the upper-left junction closes a small return loop missing from C and H.',
    'Dotted i and two low m groups support imm; fermée confirmed; no abbreviation point visible.',
    'Interlinear U-prime replacement and its insertion guide confirmed; small raised signs remain star|wedge, including the repeated K sign.',
    'Clockwise rotation makes vérifier / l\u2019énoncé / précis followed by three dots readable; all words resolved.',
    'Original K-prime retains possible overdot uncertainty; inserted dotted K-star has a separate union sign before U_i.',
    'Raised horizontal dash resolved as minus; following mark is forall i, without an equals sign.',
    'Cancelled K-star|K-prime retained; live dotted i, low n and terminal t read int, not soit; no final period.',
    'Freehand numeral resolved as 5; separate short dark downstroke below-left recorded independently.',
]
crops = json.loads((OUT / 'crop_manifest.json').read_text())
assert len(crops) == len(observations)
for crop, observed in zip(crops, observations):
    crop['observed'] = observed
    crop['viewed_once'] = True
(OUT / 'crop_manifest.json').write_text(json.dumps(crops, ensure_ascii=False, indent=2) + '\n')

inventory_specs = [
    ('text', 'opening above drawing', 'Script X qui est aussi la somme amalgamée'),
    ('deletion', 'opening before barred W', 'cancelled final s after de'),
    ('deletion', 'opening before the first coproduct', 'cancelled final s after the second de'),
    ('diagram', 'upper right inside the opening parenthesis', 'coprod_i B_i, barred W, coproduct of barred U_i, two arrows'),
    ('drawing', 'upper and middle left', 'three lobes, thin inner lines, thick Y, six cross-marks, narrow return loop, B_3 C_3 B_2 C_2 C_1 B_1, K'),
    ('deletion', 'upper right first crossed line', 'L\u2019application naturelle'),
    ('deletion', 'upper right second crossed line', 'uncertain de, script X to plain X'),
    ('display', 'middle right first construction and continuation', 'script X amalgamated over coproduct B_i; coproduct with i(w|W), X_i'),
    ('deletion', 'operator within the parentheses of the main display', 'uncertain union overwritten by coproduct'),
    ('display', 'right of the continuation', 'X_{w|i} isomorphic to script X_i; two vertical strokes; Im X_i'),
    ('margin note', 'beneath side display', 'curved loop-headed arrow and ouvert de script X'),
    ('text', 'beneath the display and drawing', 'script X to X est étale; c\u2019est une imm fermée'),
    ('text', 'lower half, item 6 beginning', 'Énoncé d\u2019invariance; par rapport au remplacement de K'),
    ('insertion', 'interlinear after the first U replacement', 'U-prime_i^{star|wedge}=U-prime_i intersect K^{star|wedge}'),
    ('margin note', 'oblique left margin alongside item 6', 'vérifier l\u2019énoncé précis...'),
    ('deletion', 'original first condition in item 6', 'K-prime or dotted K-prime subset union U_i, et'),
    ('insertion', 'above the original crossed condition', 'dotted K-star subset union U_i, et'),
    ('deletion', 'before the live forall i', '(K setminus K-prime) with a raised minus'),
    ('text', 'conditions continuing item 6', 'forall i, C_i subset closures of U_i-star and U-prime_i-star'),
    ('deletion', 'after il suffit que', 'uncertain K-star or K-prime'),
    ('text', 'sufficient-condition parenthesis', '(- il suffit que ... int K-prime superset union C_i; parenthesis not closed'),
    ('text', 'final three body lines', 'vérifier si dans les div. hypothèses précédentes ... union C_i subset int K; equivalent condition written with dotted K'),
    ('drawing', 'left of final line', 'single long vertical pen stroke'),
    ('drawing', 'below-left of own page numeral', 'detached short dark downstroke'),
    ('text', 'lower left above archival numeral', 'own page number 5'),
    ('text', 'bottom-left corner', 'archival numeral 5, comment only'),
]
inventory = []
for n, (kind, position, first) in enumerate(inventory_specs, 1):
    inventory.append({
        'scan': 6, 'sheet_kind': 'text',
        'hand': 'another unnamed hand' if n == len(inventory_specs) else 'his hand',
        'element': f'006-R2-{n:02d}', 'kind': kind, 'position': position,
        'first_words_or_objects': first, 'transcribed': 'yes',
    })

doubts = [
    {'place': 'Opening script capital, recurring throughout page', 'reading': r'\unsure{\mathcal{X}|\mathscr{X}}', 'alternatives': r'\mathscr{X}', 'confidence': 'medium', 'reason': 'The handwritten curves establish script X but do not uniquely select a typographic script alphabet. Later occurrences use the first candidate without repeating the marker.'},
    {'place': 'Both cancelled endings after de', 'reading': r'de\deleted{\unsure{s}}', 'alternatives': 'No secure second letter candidate', 'confidence': 'low', 'reason': 'Both endings are retraced into horizontal blackened loops; s is plausible but not individually settled. The second unmarked s inherits this uncertainty.'},
    {'place': 'Opening parenthesis word', 'reading': r'\unsure{sur}', 'alternatives': 'No secure second word candidate', 'confidence': 'low', 'reason': 'The first hook and following low strokes favour sur but remain too compressed for a settled reading.'},
    {'place': 'Cancelled word before the cancelled map', 'reading': r'\unsure{\text{de}}', 'alternatives': 'No secure second word candidate', 'confidence': 'low', 'reason': 'A lower bowl and tall loop survive, but crossing strokes hide the second letter.'},
    {'place': 'Overwritten operator inside the main-display parentheses', 'reading': r'\deleted{\unsure{\bigcup}}', 'alternatives': 'No secure other mathematical symbol candidate', 'confidence': 'low', 'reason': 'Rounded underlying remnants are visible; the live coproduct prevents complete separation of the older strokes.'},
    {'place': 'Parenthesized letter below the second-row coproduct', 'reading': r'\unsure{w|W}', 'alternatives': 'W', 'confidence': 'medium', 'reason': 'Two rounded troughs favour w, though a small capital W remains supported.'},
    {'place': 'First X subscript in the side display', 'reading': r'X_{\unsure{w|i}}', 'alternatives': 'i', 'confidence': 'low', 'reason': 'Connected up-down-up ending lacks a clear dot and favours w; a compressed i remains possible.'},
    {'place': 'Both small raised marks in the interlinear U-prime formula', 'reading': r"U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*", 'alternatives': r'\wedge for both small raised signs', 'confidence': 'medium', 'reason': 'The little peaked shapes have less crossing detail than the full-size stars. The later unmarked K-star inherits the first sign\u2019s unresolved status.'},
    {'place': 'Original cancelled K-prime condition', 'reading': r"\unsure{K'|\dot K'}", 'alternatives': r"\dot K'", 'confidence': 'low', 'reason': 'Prime is visible; possible overdot cannot be separated from the cancellation\u2019s initial high stroke.'},
    {'place': 'Cancelled K-like group after il suffit que', 'reading': r"\deleted{\unsure{K^*|K'}}", 'alternatives': "K'", 'confidence': 'low', 'reason': 'K\u2019s stem and lower legs remain; upper star or prime is obscured by repeated scribbling.'},
]
for d in doubts:
    assert d['reading'] in R, ('Doubt not in TeX', d)

notes = [
    'The page continues an identification of the script-X object as an amalgamated sum of barred W and the coproduct of barred U_i over the coproduct of B_i. A second row gives a coproduct of X_i, with its parenthesized lower letter unresolved as w/W.',
    'The side display identifies an ambiguously subscripted plain X with script X_i, places Im X_i beneath two vertical equality-like strokes, and labels the associated object as an open part of script X.',
    'The three-lobed picture labelled K has a common three-branch junction, thick inner portions, B_1/B_2/B_3 at their outer ends, C_1/C_2/C_3 nearer the junction, six transverse marks, and a small return loop at the upper-left join.',
    'The map from script X to X is stated to be étale away from the coproduct of the C_i and a closed immersion at points of the coproduct of C_i. The latter is written with the abbreviation imm.',
    'Item 6 proposes invariance of script X on replacing K by K-star contained in K and replacing U_i and U-prime_i by their intersections with K-star. Its first condition has been rewritten above a cancelled line; the next displayed inclusion involves closures of the two restricted U sets.',
    'The sufficient-condition parenthesis contains a cancelled K-like group followed by int K-prime superset union C_i. The parenthesis is left open in the ink.',
    'The slanted note says "vérifier l\u2019énoncé précis...". The final paragraph asks whether the preceding hypotheses should have required the union of the C_i to lie in int K, and writes an i.e. condition using C_i intersect dotted K equal to the empty set for every i in I.',
    'The visible section number is 6), and the author\u2019s page number is 5. A separate darker archival 5 is at the lower-left corner. No date or independent title is present on this page.',
]
checks = [
    {'statement_id': '006-R2-M01', 'type': 'carried as background without fault found', 'statement': 'Amalgamated-sum and coproduct identifications of script X.', 'outcome': 'Read and compared as written. Definitions and the construction are not supplied on this page; no proof or universal-property check was performed.'},
    {'statement_id': '006-R2-M02', 'type': 'carried as background without fault found', 'statement': 'Side identification with Im X_i and the open-subobject gloss.', 'outcome': 'No mathematical verification performed. The first subscript remains w|i; it has not been changed to match the adjacent i subscripts.'},
    {'statement_id': '006-R2-M03', 'type': 'carried as background without fault found', 'statement': 'The map is étale off the coproduct C_i and a closed immersion at its points.', 'outcome': 'The two assertions were transcribed; no morphism definitions or local models are present to prove them here.'},
    {'statement_id': '006-R2-M04', 'type': 'carried as background without fault found', 'statement': 'Proposed invariance after restriction from K to K-star under the written conditions.', 'outcome': 'The author himself asks to verify the precise statement. This reading does not supply a proof or repair the condition, and retains the uncertain superscripts and cancelled terms.'},
    {'statement_id': '006-R2-M05', 'type': 'carried as background without fault found', 'statement': 'The written sufficient condition involving int K-prime and union C_i.', 'outcome': 'The change from C\u2019s soit to int is a reading of visible letters, not a mathematical correction or a verification of sufficiency.'},
    {'statement_id': '006-R2-M06', 'type': 'carried as background without fault found', 'statement': 'The final i.e. relation between inclusion in int K and disjointness from dotted K.', 'outcome': 'Only the written relation was read. This page does not define dotted K or state all containment assumptions, so no unconditional equivalence proof is claimed.'},
]
notation = [
    {'sign': 'Script X versus plain X', 'tex': r'\unsure{\mathcal{X}|\mathscr{X}}; X', 'place': 'opening, cancelled/live maps, displays, gloss, item 6', 'ink': 'Script form has sweeping curved limbs and a transverse stroke; plain X is two crossing slants.', 'alternatives': r'\mathscr{X} remains a typographic alternative; later script forms inherit this uncertainty.'},
    {'sign': 'Barred W and U_i', 'tex': r'\overline W,\overline U_i', 'place': 'opening, upper diagram and main display', 'ink': 'Long separate horizontal overlines; U and W have distinct one- and two-trough forms.', 'alternatives': ''},
    {'sign': 'Coproduct and amalgamation', 'tex': r'\coprod_i,\amalg_{(\coprod_i B_i)}', 'place': 'opening and displays', 'ink': 'Pairs of upright limbs on a horizontal foot; dotted i beneath.', 'alternatives': r'An overwritten earlier \bigcup remains uncertain inside the main parentheses.'},
    {'sign': 'B and C labels', 'tex': r'B_1,B_2,B_3,C_1,C_2,C_3', 'place': 'three-branch drawing', 'ink': 'B has two bowls; C is open; all six low numerals were read, including the angular 2 and 3.', 'alternatives': ''},
    {'sign': 'Isomorphism and upright pair', 'tex': r'\simeq,\shortparallel', 'place': 'construction and side display', 'ink': 'A wave over one bar; two short upright marks between script X_i and Im X_i.', 'alternatives': ''},
    {'sign': 'Parenthesized lower w/W', 'tex': r'\unsure{w|W}', 'place': 'second-row coproduct index', 'ink': 'Two rounded low troughs with a central peak.', 'alternatives': 'W remains unresolved.'},
    {'sign': 'Side X subscript', 'tex': r'X_{\unsure{w|i}}', 'place': 'first object in right-side display', 'ink': 'Connected curved ending with an additional up-down-up sequence, without a distinct dot.', 'alternatives': 'i remains unresolved.'},
    {'sign': 'Prime and full-size star', 'tex': r"U'_i,U_i^*,K',K^*,\dot K^*", 'place': 'item 6 replacement and conditions', 'ink': 'Prime is a single slant; full-size stars have multiple crossing rays; inserted boundary K has a separate dot.', 'alternatives': 'Cancelled symbols have local uncertainties recorded separately.'},
    {'sign': 'Small raised star/wedge', 'tex': r"U_i'{}^{\unsure{*|\wedge}};K^*", 'place': 'small interlinear formula', 'ink': 'Peaked limbs with a short retrace, less detail than the larger stars.', 'alternatives': r'\wedge; repeated K mark remains unresolved even though unmarked.'},
    {'sign': 'Complement and raised minus', 'tex': r"\smallsetminus;(K\smallsetminus K')^{-}", 'place': 'map assertion and cancelled parenthesis', 'ink': 'Oblique set-difference stroke; separate thick horizontal raised dash after the cancelled closing parenthesis.', 'alternatives': ''},
    {'sign': 'Empty set', 'tex': r'\varnothing', 'place': 'last line', 'ink': 'Small open oval with a long diagonal stroke extending well below the line.', 'alternatives': ''},
    {'sign': 'Inclusion and quantifier', 'tex': r'\subset,\supset,\forall i\in I', 'place': 'item 6 and final line', 'ink': 'Open curved inclusion signs; rounded two-limbed forall with crossbar; dotted i and capital serifed I.', 'alternatives': ''},
]
abbreviations = [
    {'written': 'pts', 'expansion': 'points'},
    {'written': 'imm', 'expansion': 'immersion'},
    {'written': 'Im', 'expansion': 'image'},
    {'written': 'int', 'expansion': 'intérieur'},
    {'written': 'div.', 'expansion': 'diverses'},
    {'written': 'i.e.', 'expansion': 'id est; that is'},
]

# Static checks only: never compile the transcription.
no_comments = re.sub(r'(?m)(?<!\\)%.*$', '', R)
brace_stack = []
for m in re.finditer(r'(?<!\\)[{}]', no_comments):
    if m.group() == '{':
        brace_stack.append(m.start())
    else:
        assert brace_stack, ('Unmatched closing brace', m.start())
        brace_stack.pop()
assert not brace_stack, ('Unclosed braces', brace_stack)
env_stack = []
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', no_comments):
    action, env = m.groups()
    if action == 'begin':
        env_stack.append(env)
    else:
        assert env_stack and env_stack[-1] == env, ('Environment mismatch', env, env_stack)
        env_stack.pop()
assert not env_stack
assert len(re.findall(r'(?<!\\)\\\[', no_comments)) == len(re.findall(r'(?<!\\)\\\]', no_comments))
assert len(re.findall(r'(?<!\\)\\\(', no_comments)) == len(re.findall(r'(?<!\\)\\\)', no_comments))
assert len(re.findall(r'(?<!\\)\$', no_comments)) % 2 == 0
assert {f['c_doubt_id'] for f in findings if f['c_doubt']} == {f'C-D{n:02d}' for n in range(1, 25)}
assert json.loads((PACKET / 'S.json').read_text()) == []

report = {
    'scan': 6, 'reader': 'R2', 'model': 'inherited parent model',
    'effort': 'inherited; value not independently exposed',
    'started_utc': '2026-11-19T22:17:22Z',
    'finished_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'timestamp_note': 'Start is the first recorded clock reading, after the supplied packet was opened and before the whole image was viewed.',
    'images_viewed': json.loads((PACKET / 'meta.json').read_text())['images'],
    'image_view_counts': {'whole': 1, 'half_a': 1, 'half_b': 1},
    'crops': crops, 'findings': findings, 'inventory': inventory,
    'doubts': doubts, 'notes': notes, 'checks': checks, 'notation': notation,
    'abbreviations': abbreviations,
    's_decisions': [],
    'materials_read': ['meta.json', 'C.tex', 'H.tex', 'H_drawing_01-3.tex', 'C_doubts.md', 'C_audit.md', 'C_notes.md', 'C_inventory.json', 'S.json', 'PREAMBLE.tex', 'notation.md'],
    'validation': {
        'all_24_C_doubts_addressed': True,
        'all_finding_readings_are_exact_substrings_of_reading_tex': True,
        'all_nonempty_C_snippets_found_in_C_tex': True,
        'all_nonnull_H_snippets_found_in_H_text_or_supplied_drawing_asset': True,
        'brace_balance': 'passed', 'environment_balance': 'passed',
        'math_delimiter_balance': 'passed', 'compiled': False,
        'ocr_or_text_recognition_used': False, 'internet_used': False,
        'other_pages_or_readers_consulted': False,
        'S_packet_status': 'Empty array; no S rows supplied for this page.',
    },
    'brief_feedback': [
        'No blocking ambiguity. In findings, differences in uncertainty status count as local differences; equivalent witness macro vocabulary by itself does not. H drawing comparisons use the supplied actual TikZ paths and comments, without compilation.',
    ],
}
(OUT / 'report.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
(OUT / 'static_validation.json').write_text(json.dumps(report['validation'], indent=2) + '\n')
print(json.dumps({'findings': len(findings), 'c_doubts': 24, 'crops': len(crops), 'inventory': len(inventory), 'remaining_doubts': len(doubts), 'static_checks': 'passed'}, ensure_ascii=False))
