from pathlib import Path
import csv
import json
import re

root = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
packet = root / 'packets/145_scan022'
out = root / 'edition/reader_reports'
manifest = json.loads((out / '145_scan022_crop_boxes.json').read_text())
crops = {item['name']: item for item in manifest}

# These drawings reproduce strokes; they do not assign a lexical reading or
# an editorial function to either marginal mark.
upper_mark = r'''\begin{tikzpicture}[x=0.13cm,y=0.13cm,baseline=-0.5ex]
\draw[line width=0.35pt] (0,0) .. controls (0.3,1.1) and (0.0,2.6) .. (0.45,3.6) .. controls (0.65,3.9) and (0.95,3.9) .. (1.2,3.7);
\draw[line width=0.5pt] (0,0.1) -- (0.2,-0.1) -- (0.25,0.5) -- (0.6,0.2);
\draw[line width=0.4pt] (0.95,2.2) .. controls (0.8,2.5) and (1.3,2.6) .. (1.4,2.25) .. controls (1.2,2.1) and (1.05,2.1) .. (0.95,2.2);
\draw[line width=0.45pt] (-0.45,-0.1) .. controls (-0.25,0.1) and (-0.2,0.4) .. (-0.25,0.6);
\end{tikzpicture}'''
lower_connector = r'''\begin{tikzpicture}[x=0.18cm,y=0.18cm,baseline=-0.5ex]
\draw[line width=0.35pt] (-0.5,2.8) .. controls (-1.0,1.7) and (-0.7,1.0) .. (0.25,0.4) .. controls (0.5,0.2) and (0.55,0.0) .. (0.4,-0.2);
\draw[line width=0.35pt] (5.7,2.1) .. controls (3.9,1.65) and (2.0,1.5) .. (1.0,1.3) .. controls (0.55,1.2) and (0.4,0.4) .. (0.15,-0.2);
\draw[line width=0.5pt] (0.15,-0.2) -- (0.55,0.1) -- (0.6,0.5);
\end{tikzpicture}'''

system10 = r'''\[
(10)\quad\left\{\begin{aligned}
\rho^3&=1\\
\varepsilon_\infty^2\varepsilon_1^2\varepsilon_0^2&=1\\
\deleted{\unsure{\varepsilon_0}}\ \varepsilon_1&=\varepsilon_0^{\deleted{4}}\varepsilon_\infty^4\rho\varepsilon_0^2\deleted{\unsure{\rho}}\varepsilon_\infty^2\\
\varepsilon_\infty&=\varepsilon_1\varepsilon_0^4\rho\varepsilon_{\unsure{1|\infty}}^2\deleted{\unsure{\rho}}\varepsilon_0^2\\
\varepsilon_0&=\varepsilon_\infty\varepsilon_1^4\rho\varepsilon_\infty^2\deleted{\unsure{\rho}}\varepsilon_1^2
\end{aligned}\right.
\]'''
upper_note = r'''\margin{il faut aussi ajouter (au moins!) les relations $\rho\varepsilon_0\rho^{-1}=\varepsilon_1$ etc donc on a deux gén. $(\varepsilon_0,\rho)$ ''' + upper_mark + '}'
question = r'''On peut encore se demander si $\rho$ s'exprime en fonction des $\varepsilon_i$, et on trouve comme tantôt que non.'''
paragraph = r'''Quant à relever $\dot\tau$ en un élément de $\mathcal E$, par un chemin de $P$ à $\bar P$, on ne voit pas de choix privilégié --- on voit trois choix également naturels. Au lieu de les expliciter d'emblée, je préfère considérer le sous-groupe d'isotropie de $P$ dans $\Gamma=\Gamma_{0,3}=\unsure{\mathfrak S_3|\mathcal S_3}\times\mathbb Z/2$, qui est formé des couples $\dot\sigma,\dot\tau^\varepsilon$ tels que $\operatorname{sg}(\dot\sigma)=\varepsilon$; \deleted{On} i.e. les éléments'''
sigma_display = r'''\[
\widetilde{\dot\sigma}=(\dot\sigma,\dot\tau^{\operatorname{sg}(\dot\sigma)})\in\Gamma
\]'''
releves = r'''qui sont relevés canoniquement en des éléments $(\widetilde{\dot\sigma},\text{lacet trivial en }P)$ de $\mathcal E$. On trouve un hom'''
system11 = r'''\[
(11)\quad\left\{\begin{aligned}
\varphi:\unsure{\mathfrak S_3|\mathcal S_3}&\longrightarrow\Gamma=\unsure{\mathfrak S_3|\mathcal S_3}\times\mathbb Z/2\\
\dot\sigma&\longmapsto\dot\sigma,\operatorname{sg}(\dot\sigma)
\end{aligned}\right.
\]'''
bridge = r'''et un relèvement canonique de $\varphi$ en'''
system12 = r'''\[
(12)\qquad\sigma\longrightarrow\tilde\sigma:\quad\unsure{\mathfrak S_3|\mathcal S_3}\longrightarrow\mathcal E
\]'''
final_display = r'''\[
\tilde\sigma_i=\widetilde{\dot\sigma_i}
\]'''
lower_note = r'''\margin{on a d'autre part \deleted{$\unsure{\tilde\rho}$} $\widetilde{\dot\rho}=\rho$ ''' + lower_connector + '}'
tex = '\n'.join([
    r'\scanpage{22}', r'\mspage{9}', system10, upper_note, question, '',
    paragraph, sigma_display, releves, system11, bridge, system12,
    'On pose', final_display, lower_note, r'\mspage{21}', ''
])
(out / '145_scan022.tex').write_text(tex)

changes = []
def change(n, place, C, H, final, ink, crop, kind, c_changed=False,
           h_changed=True, marked='no', confidence='high', categories=(2,), consequence=''):
    item = crops[crop]
    changes.append({
        'id': f's022-{n:02d}', 'place': place, 'C': C, 'H': H, 'final': final,
        'ink': ink, 'confidence': confidence, 'kind': kind,
        'c_changed': c_changed, 'h_changed': h_changed, 'marked_in_H': marked,
        'crop': item['crop'], 'box': item['box'],
        'error_category': list(categories), 'math_consequence': consequence
    })

change(1, '(10), first of the three product rows: cancelled beginning and exponent',
       r'\deleted{\unsure{\varepsilon_0}}\ \varepsilon_1=\varepsilon_0^{\deleted{4}}',
       r'\varepsilon_1 = \varepsilon_0',
       r'\deleted{\unsure{\varepsilon_0}}\ \varepsilon_1=\varepsilon_0^{\deleted{4}}',
       'A compact crossed epsilon-like body and low round index precede the live epsilon_1; their internal strokes remain obscured. Above the first live epsilon_0 a cancelled angular 4 retains its diagonal and dark right foot. H mentions both areas in its editorial note but leaves them out of its transcription. The three following live exponents 4 have open angular outlines, distinct from the curved 2s.',
       'formula10', 'deletion state', marked='yes', confidence='medium', categories=(3,7))
change(2, '(10), one crossed factor in each of the last three rows',
       r'\deleted{\rho}', '', r'\deleted{\unsure{\rho}}',
       'Each of the three positions has a long downward stem matching the adjacent live rho stems, but several oblique strokes obscure its head. All three signs are explicitly cancelled, not gaps between the live factors. The same quoted reading applies to all three occurrences; uncertainty about each head is retained separately. H describes the crossed traces in its note but omits them from its formulas.',
       'formula10', 'deletion state', marked='yes', confidence='low', categories=(3,7))
change(3, '(10), second product, epsilon immediately following the live rho',
       r'\varepsilon_1^2', r'\varepsilon_{\uncertain{\infty}}^{2}',
       r'\varepsilon_{\unsure{1|\infty}}^2',
       'The subscript has a small leftward loop and a blackened downward right stroke. The right stem supports 1, but the joined/retraced loop prevents exclusion of infinity. The reading is not settled from the cyclic pattern of the neighboring rows.',
       'formula10', 'misread symbol or index', marked='yes', confidence='low', categories=(1,))
change(4, '(10), end of the final row', r'\varepsilon_1^2.',
       r'\varepsilon_1^{2}', r'\varepsilon_1^2',
       'The final epsilon_1 and superscript 2 are followed by clear paper. There is no separate terminal ink dot.',
       'formula10', 'text not on the page', c_changed=True, h_changed=False, categories=(9,))
change(5, 'Upper slanted margin, opening words',
       'il faut aussi ajouter (au moins!) les relations',
       'il faut aussi écrire (au moins !) les relations',
       'il faut aussi ajouter (au moins!) les relations',
       'After the first line il faut aussi, the next word begins with a low a and a long descending j, followed by the joined outer body and tall t of ajouter. It does not have the initial accented e and c-r sequence of écrire. The parentheses and exclamation mark around au moins are present.',
       'upper_margin', 'misread word')
change(6, 'Upper slanted margin, relation and generator statement',
       r'$\rho\varepsilon_0\rho^{-1}=\varepsilon_1$ etc donc on a deux gén. $(\varepsilon_0,\rho)$',
       r'$\rho\,\varepsilon_0\,\rho^{-1} = \varepsilon_1$ etc., donc \uncertain{on a} \ill{} \ill{} $(\varepsilon_0\rho)$',
       r'$\rho\varepsilon_0\rho^{-1}=\varepsilon_1$ etc donc on a deux gén. $(\varepsilon_0,\rho)$',
       'The conjugation shows epsilon_0, superscript minus 1 on the second rho, and epsilon_1 on the right. The continuation reads etc with no separate stop/comma, then donc on a deux gén.; the two following word bodies have the d ascender and terminal x, then the g descender, accent and final abbreviation stop. A comma separates epsilon_0 from rho inside the parentheses.',
       'upper_margin', 'readable ink left as \\ill{}', marked='yes', categories=(1,2,3,5,9))
change(7, 'Upper slanted margin, mark immediately after the generator parenthesis',
       '.', r'\ill{}', upper_mark,
       'The mark is substantially taller than punctuation: a thin hooked stem rises above a dark foot, with a small upper loop and an adjacent short hook. It cannot be reduced to C’s stop. Its visible geometry is reproduced in TikZ without identifying it as a letter, punctuation sign or reference mark.',
       'upper_margin', 'drawing or diagram', c_changed=True, marked='yes',
       confidence='medium', categories=(4,9))
change(8, 'Three-line question following (10)', question,
       r"\uncertain{Chacun} \ill{} des $\varepsilon_i$, $\rho$ s'expriment en fonction des $\varepsilon_i$, et on trouve comme \ill{} \uncertain{tantôt} \ill{}.",
       question,
       'The opening capital O and joined n are partly overlaid by the darker slanted margin, but the following p descender, peut, encore and se demander can be followed across the line. The main subject is the single rho, followed by s’exprime with no final t. The last line has the tall first and final t of tantôt, then que and the two humps of non followed by a dark stop. The negative answer is explicit ink.',
       'question', 'readable ink left as \\ill{}', marked='yes', categories=(2,3,5),
       consequence='The author’s explicit negative answer is retained. Its compatibility with the preceding relation is left to the root mathematical audit.')
change(9, 'Quant à relever, first symbol', r'\dot\tau', r'\tau', r'\dot\tau',
       'A discrete dark dot sits above the tau bar, separated by clear paper. It is not an accent belonging to a neighboring word.',
       'path_negative', 'misread symbol or index', categories=(1,3))
change(10, 'Quant à relever, path phrase across the first two lines',
       r'par un chemin de $P$ à $\bar P$',
       r'\uncertain{pour} $\Gamma : \overline{P}$',
       r'par un chemin de $P$ à $\bar P$',
       'The word at the right edge begins with a long p and reads par. The next line visibly has un chemin de, followed by the open-loop capital P, a small accented à and a second P with a separate overbar. No Gamma is written at this position.',
       'path_negative', 'misread word', marked='yes', categories=(1,2,3))
change(11, 'Quant à relever, negative phrase and ending of privilégié',
       'on ne voit pas de choix privilégié', 'on voit par des \\uncertain{choix} privilégiés',
       'on ne voit pas de choix privilégié',
       'After the comma following bar P, two separate low word groups give on ne before voit. The p descender and joined low body of pas precede de; the latter has no terminal s. The next line ends privilégié with an accented final e and no added s. The following dash is distinct.',
       'path_negative', 'misread word', marked='yes', categories=(2,3))
change(12, 'Au lieu de les expliciter, final word', "d'emblée", 'directement', "d'emblée",
       'The compact initial d is followed by the apostrophe and the joined em body, then the taller b/l sequence and accented ending; a comma follows. The long horizontal upper stroke belongs to the word’s diacritic/upper ductus and does not supply the missing letters of directement.',
       'demblee_prefere', 'misread word')
change(13, 'Beginning of the next physical line', 'je préfère',
       r'\uncertain{il est plus simple de}', 'je préfère',
       'The first word has a dotted descending j and short e. The second begins with a p descender and shows the tall f and accented joined ending of préfère. The proposed longer H phrase has no corresponding series of words.',
       'demblee_prefere', 'misread word', marked='yes', categories=(2,9))
change(14, 'After the Gamma identity', 'qui est formé', 'qui se forme', 'qui est formé',
       'After qui, the separate short body ends in a raised t/crossing rather than the open se of H. The following f has its tall stem and descending loop; the terminal formé carries an accent.',
       'gamma_couples_display', 'misread word')
change(15, 'After sg(dot sigma)=epsilon and the semicolon',
       r'\deleted{On}', r'\struck{\uncertain{donc}}', r'\deleted{On}',
       'A tall closed capital O and one joined low n remain visible above/through a horizontal cancellation. There is no sequence d-o-n-c. The strike crosses this word alone; i.e. on the next line is live.',
       'gamma_couples_display', 'misread word', marked='yes', categories=(2,7))
change(16, 'Unnumbered sigma display, left member', r'\widetilde{\dot\sigma}',
       r'\dot\sigma^{*}', r'\widetilde{\dot\sigma}',
       'The ornament is a wavy line directly above the dotted sigma; it is centered over the letter and not a separate star at the upper right. The intervening dark dot remains distinct.',
       'gamma_couples_display', 'misread symbol or index', categories=(1,))
change(17, 'Prose following the unnumbered display',
       'qui sont relevés canoniquement en des éléments',
       'qui se relèvent canoniquement en des éléments',
       'qui sont relevés canoniquement en des éléments',
       'The word after qui ends with a tall final t and reads sont. The following participle has an accented e and a terminal s, without the final n-t of relèvent. All following agreed words were read against the native half and this crop.',
       'releves_hom', 'misread word')
change(18, 'Parenthesized pair in the prose',
       r'$(\widetilde{\dot\sigma},\text{lacet trivial en }P)$',
       r'($\tilde\sigma$, \uncertain{fixant} un $P$)',
       r'$(\widetilde{\dot\sigma},\text{lacet trivial en }P)$',
       'The sigma carries a separated dot below its tilde. The following noun begins with a high looped l and continues a-c-e-t; trivial has its initial crossed t, dotted i strokes and tall final l. The final short word is en, then a capital P and the closing parenthesis.',
       'releves_hom', 'misread word', marked='yes', categories=(1,2))
change(19, 'Sentence introducing (11)', 'On trouve un hom.',
       r'Ces termes \uncertain{définissent} une section', 'On trouve un hom',
       'On has a looped capital O, trouve a prominent crossed initial t, and the next line begins un followed by the tall h and joined o-m of hom. There is no additional dark stop after hom; the final ink thickening is attached to the m. The H words are absent.',
       'releves_hom', 'misread word', c_changed=True, marked='yes', categories=(2,8,9))
change(20, '(11), two-row layout, target punctuation and target parentheses', system11,
       r'''\[
(11)\quad
\varphi : \mathfrak{S}_3 \longrightarrow \Gamma = \mathfrak{S}_3 \times \mathbb{Z}/2,
\qquad \dot\sigma \longmapsto (\dot\sigma, \operatorname{sg}(\dot\sigma))
\]''',
       system11,
       'A tall left brace groups two rows. The second arrow has a short upright tail bar, hence mapsto. Its image starts immediately with dotted sigma; no opening or closing outer parentheses enclose the pair. The parentheses around the argument of sg are present. After the upper-row Z/2 there is no comma. Both ornate S signs remain locally alphabetically uncertain.',
       'formula11', 'other', categories=(1,3,6,9))
change(21, '(12), initial arrow and terminal punctuation',
       system12.replace('\\mathcal E\n', '\\mathcal E.\n'),
       r'''\[
(12)\quad \sigma \longmapsto \tilde\sigma : \mathfrak{S}_3 \longrightarrow \mathcal{E} .
\]''',
       system12,
       'The first arrow has an uninterrupted plain shaft and an arrowhead, with no upright tail bar. The source sigma has no separate overdot, and the image has a tilde only. A colon separates this map from the group-to-E arrow. No distinct ink point follows the E; both witnesses supplied one.',
       'formula12', 'misread symbol or index', c_changed=True, categories=(1,9))
change(22, 'Lower marginal equality, live rho on the left',
       r'\widetilde{\dot\rho}=\rho', r'\tilde\rho = \rho', r'\widetilde{\dot\rho}=\rho',
       'The live left rho has a clear small dot between its looped head and the wavy tilde. The two parallel equality strokes and the right rho are plain. H’s final note expresses uncertainty about the equality; the dot is nevertheless absent from its proposed text.',
       'lower_margin_footer', 'misread symbol or index', marked='yes', categories=(1,3))
change(23, 'Lower margin, cancelled sign before the live equality',
       r'\deleted{$\unsure{\tilde\rho}$}', r'\struck{\ill{}}',
       r'\deleted{$\unsure{\tilde\rho}$}',
       'A waved upper stroke and a lower loop with a long descended stroke support tilde rho, but cancellation and the approaching connector cross the head. The full sign cannot be resolved; C’s explicit local doubt is retained rather than treating the trace as blank.',
       'lower_margin_footer', 'readable ink left as \\ill{}', marked='yes',
       confidence='low', categories=(3,5,7))
change(24, 'Lower marginal note, curved left hook and descending connector',
       r"\margin{on a d'autre part \deleted{$\unsure{\tilde\rho}$} $\widetilde{\dot\rho}=\rho$}",
       r"(on a d'autre part \struck{\ill{}} $\tilde\rho = \rho$)",
       lower_note,
       'A separate broad left hook spans the marginal text and approaches the crossed sign below it. A long thin sloping line runs beneath on a d’autre part from the right and bends down toward that cancelled sign, ending in a short darker hooked foot. The geometry favors a connector/bracket, not an emphasis underline. No matching right closing parenthesis is visible. The two strokes are reproduced as a small adjacent graphic, and their exact role is left open.',
       'lower_margin_footer', 'drawing or diagram', c_changed=True,
       confidence='medium', categories=(4,6,9))
change(25, 'Bottom-left handwritten page number', r'\mspage{21}', '', r'\mspage{21}',
       'Two dark full-height digits stand at the bottom left: a curved 2 and a straight 1. This is an actual inscription omitted by H, not an editorial scan marker.',
       'lower_margin_footer', 'omission', categories=(3,))

decisions = []
for mark_id, place, crop in [
    ('M0847', 'Gamma identity in prose', 'gamma_couples_display'),
    ('M0848', '(11), source of phi', 'formula11'),
    ('M0849', '(11), factor after Gamma=', 'formula11'),
    ('M0850', '(12), source of the group-to-E arrow', 'formula12'),
]:
    item = crops[crop]
    decisions.append({
        'id': mark_id, 'decision': 'undecided',
        'reading': r'\unsure{\mathfrak S_3|\mathcal S_3}',
        'ink': f'{place}: the large sign has a broad outer loop, an upper returning stroke and an inner curling lower stroke, with a distinct subscript 3. It is consistently ornate S-shaped here, but its ductus alone does not determine a modern fraktur versus calligraphic alphabet.',
        'crop': item['crop'], 'box': item['box'], 'confidence': 'medium'
    })
unlisted = [
    {'id': 'U022-01', 'decision': 'undecided', 'reading': r'\deleted{\unsure{\varepsilon_0}}',
     'ink': 'Before the first live product’s epsilon_1, the crossed compact body and low round trace support epsilon_0; superimposed strokes prevent resolution of the complete cancelled sign.',
     'crop': crops['formula10']['crop'], 'box': crops['formula10']['box'], 'confidence': 'low'},
    {'id': 'U022-02', 'decision': 'undecided', 'reading': r'\deleted{$\unsure{\tilde\rho}$}',
     'ink': 'The lower marginal cancellation leaves a wavy upper trace and a descended looped sign, but its head is obscured by several crossing strokes and the connector.',
     'crop': crops['lower_margin_footer']['crop'], 'box': crops['lower_margin_footer']['box'], 'confidence': 'low'},
]

doubts = []
for item in decisions:
    doubts.append({'place': item['id'], 'reading': item['reading'],
                   'alternatives': [r'\mathfrak S_3', r'\mathcal S_3'],
                   'confidence': 'medium', 'reason': item['ink']})
doubts.extend([
    {'place': '(10), cancelled prefix before the first product',
     'reading': r'\deleted{\unsure{\varepsilon_0}}', 'alternatives': [r'\varepsilon_0', 'another obscured epsilon/index combination'],
     'confidence': 'low', 'reason': unlisted[0]['ink']},
    {'place': '(10), second product, post-rho epsilon subscript',
     'reading': r'\varepsilon_{\unsure{1|\infty}}^2', 'alternatives': ['1', r'\infty'],
     'confidence': 'low', 'reason': 'A left loop and a dark descending right stem coexist in the retraced subscript. Neither layer can be isolated with confidence.'},
])
for position in ['first', 'second', 'third']:
    doubts.append({'place': f'(10), {position} product, cancelled rho before the last factor',
                   'reading': r'\deleted{\unsure{\rho}}', 'alternatives': [r'\rho', 'obscured loop-headed descended sign'],
                   'confidence': 'low', 'reason': 'The long descender remains visible; the head is covered by several cancellation strokes. The rho reading is plausible but not fully legible.'})
doubts.extend([
    {'place': 'Lower margin, cancelled sign', 'reading': r'\deleted{$\unsure{\tilde\rho}$}',
     'alternatives': [r'\tilde\rho', 'obscured accented descended sign'], 'confidence': 'low', 'reason': unlisted[1]['ink']},
    {'place': 'Upper margin, terminal nonverbal mark', 'reading': upper_mark,
     'alternatives': ['reference mark', 'letter/punctuation group whose identity is not determined'],
     'confidence': 'low', 'reason': 'The hooked stem, upper loop and dark foot are visible and reproduced; their lexical or referential function is not determined.'},
    {'place': 'Lower margin, broad left hook and sloping line', 'reading': lower_connector,
     'alternatives': ['connector/bracket attaching the note to the cancelled sign', 'other nonverbal grouping/reference strokes'],
     'confidence': 'medium', 'reason': 'The line changes direction toward the cancelled sign. Its attachment argues against emphasis, but no unambiguous arrow label or paired bracket fixes its exact function.'},
])

inventory = []
def inv(kind, position, words, box):
    inventory.append({'element': f'I{len(inventory)+1:02d}', 'kind': kind, 'position': position,
                      'first_words_or_objects': words, 'box': box, 'sheet_kind': 'text',
                      'hand': 'his hand', 'transcribed': 'yes'})
inv('text', 'Top center, separate from (10)', '9', [878,23,925,87])
inv('display', 'Top of page, five rows with left brace and (10)', r'\rho^3=1; product relations', [210,15,1040,375])
inv('deletion', '(10), before first product’s live epsilon_1', r'\deleted{\unsure{\varepsilon_0}}', [526,158,583,217])
inv('deletion', '(10), exponent on first product’s first epsilon_0', r'\deleted{4}', [720,146,755,187])
inv('deletion', '(10), first product, before final epsilon_infty^2', r'\deleted{\unsure{\rho}}', [886,177,921,245])
inv('deletion', '(10), second product, before final epsilon_0^2', r'\deleted{\unsure{\rho}}', [886,245,925,317])
inv('deletion', '(10), third product, before final epsilon_1^2', r'\deleted{\unsure{\rho}}', [902,299,939,373])
inv('margin note', 'Upper left, six slanted lines beside and below (10)', 'il faut aussi ajouter (au moins!)', [22,181,418,850])
inv('drawing', 'End of upper marginal generator parenthesis', 'Tall hooked mark with small loop and short adjacent hook', [145,658,190,755])
inv('text', 'Three lines below (10)', 'On peut encore se demander si', [240,365,1610,680])
inv('text', 'Main paragraph, eight physical lines before unnumbered display', 'Quant à relever', [230,680,1635,1550])
inv('deletion', 'After the semicolon in the couples line', r'\deleted{On}', [1384,1320,1481,1394])
inv('display', 'Below i.e. les éléments', r'\widetilde{\dot\sigma}=(\dot\sigma,\dot\tau^{\operatorname{sg}(\dot\sigma)})\in\Gamma', [680,1548,1208,1624])
inv('text', 'Three lines before/alongside (11)', 'qui sont relevés canoniquement', [240,1620,1600,1945])
inv('display', 'Two-row display with left brace and (11)', r'\varphi:S_3\longrightarrow\Gamma', [330,1830,1405,2045])
inv('text', 'Line above (12)', 'et un relèvement canonique', [260,2050,1365,2132])
inv('display', 'Single line labeled (12)', r'\sigma\longrightarrow\tilde\sigma', [345,2120,1380,2220])
inv('text', 'Bottom main text, left of last display', 'On pose', [297,2230,560,2300])
inv('display', 'Bottom center', r'\tilde\sigma_i=\widetilde{\dot\sigma_i}', [659,2247,920,2344])
inv('margin note', 'Bottom right, two lines', "on a d'autre part", [951,2201,1430,2350])
inv('deletion', 'Lower marginal note, before live dotted-rho equality', r'\deleted{$\unsure{\tilde\rho}$}', [1010,2262,1145,2348])
inv('drawing', 'Broad hook left of bottom note and line beneath it, bending to cancelled sign', 'Connector/bracket, exact function uncertain', [948,2205,1425,2350])
inv('text', 'Bottom-left corner', '21', [29,2273,102,2346])

second_boxes = [
    {'box': 'B01', 'kind': 'Handwritten header 9 and entire (10), all numerical signs and cancellations, full doubtful product formulas',
     'coords': [210,15,1040,375], 'reading': r'\mspage{9}' + '\n' + system10},
    {'box': 'B02', 'kind': 'Complete upper margin, all numerical indices/exponent, lexical differences and terminal graphic',
     'coords': [22,181,418,850], 'reading': upper_note},
    {'box': 'B03', 'kind': 'Complete disputed question and explicit negative answer',
     'coords': [240,365,1610,680], 'reading': question},
    {'box': 'B04', 'kind': 'Dotted tau, path phrase, negative phrase and singular ending',
     'coords': [240,680,1605,995],
     'reading': r'Quant à relever $\dot\tau$ en un élément de $\mathcal E$, par un chemin de $P$ à $\bar P$, on ne voit pas de choix privilégié --- on voit trois choix également'},
    {'box': 'B05', 'kind': 'Lexical disagreements d’emblée and je préfère, with complete surrounding lines',
     'coords': [230,980,1620,1230],
     'reading': "naturels. Au lieu de les expliciter d'emblée, je préfère considérer le sous-groupe d'isotropie"},
    {'box': 'B06', 'kind': 'Full Gamma formula with 0,3,3,2, M0847, all coupled symbols, cancelled On, and entire doubtful sigma display',
     'coords': [235,1215,1635,1625],
     'reading': r"de $P$ dans $\Gamma=\Gamma_{0,3}=\unsure{\mathfrak S_3|\mathcal S_3}\times\mathbb Z/2$, qui est formé des couples $\dot\sigma,\dot\tau^\varepsilon$ tels que $\operatorname{sg}(\dot\sigma)=\varepsilon$; \deleted{On} i.e. les éléments" + '\n' + sigma_display},
    {'box': 'B07', 'kind': 'Sont relevés, complete parenthesized pair and On trouve',
     'coords': [240,1620,1600,1845],
     'reading': r'qui sont relevés canoniquement en des éléments $(\widetilde{\dot\sigma},\text{lacet trivial en }P)$ de $\mathcal E$. On trouve'},
    {'box': 'B08', 'kind': 'Abbreviation hom without stop, full (11), every number, both ornate S doubts and target punctuation',
     'coords': [240,1830,1420,2045], 'reading': 'un hom\n' + system11},
    {'box': 'B09', 'kind': 'Complete bridge and (12), numerical label and subscript, full formula with M0850, plain arrow and no final stop',
     'coords': [260,2050,1380,2220], 'reading': bridge + '\n' + system12},
    {'box': 'B10', 'kind': 'Complete final display and marginal note, cancellation, connector, and handwritten footer21',
     'coords': [20,2200,1450,2358],
     'reading': 'On pose\n' + final_display + '\n' + lower_note + '\n' + r'\mspage{21}'},
]

# Every raw token-difference row is retained.  Split/moved margin text and H's
# explanatory note cause extensive alignment artifacts; these are named here.
coverage_spec = {
    1: ('macro/editorial', None, 'C scan22 is an editorial scan identifier; H p. introduces its editorial notice of the actual handwritten header9, retained as mspage9.'),
    2: ('substantive', 5, 'Moved upper margin: ajouter/écrire is s022-05; remainder, punctuation and terminal graphic are s022-06 and s022-07. H de l’auteur is editorial.'),
    3: ('substantive', 1, 'Cancelled epsilon_0 before first product is omitted from H’s displayed transcription.'),
    4: ('substantive', 1, 'Cancelled first exponent4 is present; the apparent H comma also includes its TeX thin-space token.'),
    5: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing, not a comma in the ink.'),
    6: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    7: ('substantive', 2, 'First of three cancelled rho-like factors omitted from H’s transcription.'),
    8: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    9: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    10: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    11: ('substantive', 3, 'The second product’s post-rho epsilon subscript remains locally unsure1|infty.'),
    12: ('substantive', 2, 'Second of three cancelled rho-like factors omitted from H’s transcription.'),
    13: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    14: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    15: ('macro/editorial', None, 'H backslash-comma denotes thin mathematical spacing.'),
    16: ('substantive', 2, 'Third of three cancelled rho-like factors omitted from H’s transcription.'),
    17: ('substantive', 4, 'No terminal stop follows the final epsilon_1^2.'),
    18: ('substantive', 5, 'Moved margin is collation material, s022-05 to s022-07. H system-reading note is editorial and not an inscription.'),
    19: ('substantive', 6, 'Margin words and relation retained; H alignment lands inside its editorial discussion of an overwrite.'),
    20: ('substantive', 6, 'Margin relation retained; H alternative formula in an editorial note is not a second manuscript formula.'),
    21: ('substantive', 6, 'Minus1 belongs to the marginal conjugating rho. H 2 here comes from its displaced editorial alternative, not the same ink position.'),
    22: ('substantive', 6, 'The margin visibly reads etc donc on a deux gén. followed by the generator pair.'),
    23: ('substantive', 8, 'Alignment crosses from H’s editorial alternative to its mistaken question opening. Complete question is s022-08; margin pair is s022-06.'),
    24: ('substantive', 8, 'Complete question has On peut encore se demander si rho s’exprime, singular. Preceding marginal end is separately s022-07.'),
    25: ('substantive', 8, 'Que non is plainly present before the final stop.'),
    26: ('substantive', 10, 'Par un chemin de P à barP, not pour Gamma colon barP.'),
    27: ('substantive', 11, 'Ne is a separate visible low word between on and voit.'),
    28: ('substantive', 11, 'Pas de is visible; H par des is rejected.'),
    29: ('substantive', 11, 'The final accented e has no terminal s.'),
    30: ('substantive', 12, 'D’emblée is confirmed on its crop.'),
    31: ('substantive', 13, 'Je préfère is confirmed; H’s longer phrase is absent.'),
    32: ('macro/editorial', None, 'Tokenization of C’s unresolved font alternatives; M0847 remains in decisions and doubts. No independent additional S is written.'),
    33: ('substantive', 14, 'Qui est formé is retained.'),
    34: ('substantive', 15, 'Cancelled On, not cancelled donc.'),
    35: ('substantive', 16, 'The accent is a tilde over dotted sigma, not a right-side star.'),
    36: ('substantive', 17, 'Qui sont relevés is retained.'),
    37: ('substantive', 18, 'Lacet trivial en P is visible; the same pair also has a dot omitted by H.'),
    38: ('substantive', 19, 'On trouve un hom is visible; the C stop after hom is absent.'),
    39: ('substantive', 20, 'Environment spelling is editorial, but its two-row grouping and visible left brace are substantive layout retained in s022-20.'),
    40: ('macro/editorial', None, 'C alternative-font tokenization; M0848 remains unresolved, without a textual insertion of another S.'),
    41: ('macro/editorial', None, 'C alternative-font tokenization; M0849 remains unresolved.'),
    42: ('substantive', 20, 'No comma follows Z/2 in (11).'),
    43: ('substantive', 20, 'No outer opening parenthesis precedes the dotted sigma image in (11).'),
    44: ('substantive', 20, 'No corresponding outer closing parenthesis is written. Aligned/right-dot syntax is not punctuation.'),
    45: ('substantive', 21, 'Initial arrow in (12) is plain longrightarrow, without the tail bar in H longmapsto.'),
    46: ('macro/editorial', None, 'C alternative-font tokenization; M0850 remains unresolved.'),
    47: ('macro/editorial', None, 'Display delimiters and inline placement of the same final sigma equation; the display is visible and preserved.'),
    48: ('substantive', 24, 'The following lower note has a left hook/connector, not a parenthesis closing/opening an inline equation sequence; its physical placement is preserved.'),
    49: ('substantive', 23, 'The separate cancelled tilde-rho-like sign is recorded, with uncertainty. The live dotted rho is also restored against H in s022-22.'),
    50: ('substantive', 25, 'Handwritten footer21 is omitted by H. H’s closing parenthesis is unsupported and is covered by s022-24; its explanatory note is editorial.'),
}
with (packet / 'differences.tsv').open(newline='') as fh:
    raw_diffs = list(csv.DictReader(fh, delimiter='\t'))
diff_coverage = []
for n, row in enumerate(raw_diffs, 1):
    status, change_number, explanation = coverage_spec[n]
    record = {'row': n, 'status': status, 'C_tokens': row['witness C'],
              'H_tokens': row['witness H'], 'words_before': row['words before'],
              'raw_note': row['note'], 'explanation': explanation}
    if change_number is not None:
        record['change_id'] = f's022-{change_number:02d}'
    diff_coverage.append(record)

report = {
    'scan': 22, 'reader': 'reader_c', 'lines_read': 35,
    'layout': 'Handwritten text sheet: header9 at the top; five-row system(10); a six-line slanted upper-left margin crossing near the first three-line question; eight physical lines of main prose; one unnumbered sigma display; three further prose units; two-row system(11); bridge and one-row(12); final On pose display; a two-line lower marginal note with cancellation and connector; footer21. Side-by-side prose and formula units are counted separately in lines_read.',
    'changes': changes, 'decisions': decisions, 'unlisted_decisions': unlisted,
    'doubts': doubts, 'inventory': inventory, 'second_boxes': second_boxes,
    'notation': [
        'All four ornate S_3 signs have a large outer looping body and inner return. The identity as ornate S with subscript3 is plain locally; fraktur versus calligraphic representation remains explicitly open in M0847–M0850.',
        'Gamma has a tall left stem and short downturned upper-right end in the prose identity and both displays. No capital Pi is introduced on this page.',
        'Distinct dots occur over the first tau, the sigma and tau of the isotropy condition, the lifted sigma display and the prose pair, all dotted sigmas in(11), and the live left rho of the lower margin. The sigmas in(12) have no overdot.',
        'The arrow in the second row of(11) has a short vertical tail bar. The first arrow in(12) has no bar and remains a plain arrow.',
        'The live exponents4 in the three products are angular, unlike the rounded 2s. The second product’s post-rho epsilon index is retraced and remains 1|infinity. The second row of(10) is a juxtaposed product with one final equality, not the chain of equalities suggested by H’s editorial note.',
        'The upper marginal terminal mark and the lower hook/connector are reproduced geometrically. Neither is interpreted as a mathematical symbol, certain punctuation or underline.'
    ],
    'hand': [
        'The slanted marginal ink is darker than much of the main prose. Its crossing near the question opening complicates the capital O, but does not establish a second hand. All inscriptions are assigned to his hand absent contrary evidence.',
        'Low joined word bodies can collapse into almost horizontal strokes. In this page they caused H’s loss of ne, its paraphrase of On trouve un hom, and misreadings of est formé and the initial question. Tall p, j, f and t strokes provide local anchors; the habit is not asserted for every word.',
        'Sigma often has a compact loop with a nearly horizontal right stroke. A separate dot above that stroke is meaningful and distinct from a tilde higher above; H drops dots in the prose pair and lower marginal rho, and mistakes the display tilde for a star.',
        'Rho has a long lower stem. Cancellation strokes cover the heads of all three crossed factors in(10), so the unambiguous descender alone is insufficient to resolve those letters.',
        'Terminal letter strokes can darken at their ends without becoming separate punctuation. No separate stop is visible after hom, the last product of(10), or E in(12). By contrast, the stop after non and the semicolon after the isotropy condition are distinct.'
    ],
    'abbreviations': [
        {'form': 'gén.', 'expansion': 'générateurs', 'place': 'Upper marginal two-generator statement'},
        {'form': 'etc', 'expansion': 'et cetera', 'place': 'Upper margin after the conjugation; no terminal abbreviation point is written'},
        {'form': 'i.e.', 'expansion': 'id est', 'place': 'After cancelled On, before the lifted sigma display'},
        {'form': 'hom', 'expansion': 'homomorphisme', 'place': 'Introduction to(11), without a written stop'},
        {'form': 'sg', 'expansion': 'signature/signe in the author’s notation', 'place': 'Isotropy condition, lifted sigma display and(11)'}
    ],
    'notes': [
        'The author writes five relations under(10), including rho cubed equals1 and the product of three squared epsilons equals1. Three later rows retain cancelled prefactors/exponents and cancelled rho-like factors. The marginal addition says that conjugation relations must also be added, with the explicit reservation au moins!, and says there are two generators. These statements are transcribed as claims rather than verified here.',
        'The author explicitly asks whether rho is expressible in terms of the epsilons and writes that, as before, the answer is no. Root alerted the reader to a possible conflict between this statement and the first surviving product. The entire first product and following sentence were inspected on separate complete crops; the live exponent4 and que non are retained. No algebraic verification was performed by this reader; root will record its scoped checks separately.',
        'The subsequent discussion says there is no privileged path from P to barP for lifting dotted tau, but there are three equally natural choices. The author prefers to consider the isotropy subgroup and writes the lift of dotted sigma, the homomorphism(11), its canonical lift(12), and the final tilde-sigma_i definition. The wording je préfère and the author’s stated alternatives are retained.',
        'The upper marginal ending after the generator pair has a tall hooked stem, small upper loop, dark foot and adjacent short hook. It is represented graphically rather than forced into a period or identified as a letter. Its function remains uncertain. The lower margin has a separate broad left hook and a long sloping line under on a d’autre part bending toward the cancelled rho-like sign; the approximate geometry is reproduced in an adjacent graphic, not as an underline or a supplied closing parenthesis.',
        'All C deleted passages were checked individually: cancelled epsilon_0-like prefix; cancelled exponent4; three cancelled rho-like factors; cancelled On; lower cancelled tilde-rho-like sign. C contains no inserted macro on this page, and no distinct interlinear lexical insertion was found. The margin notes are separately inventoried.',
        'The actual handwritten page numbers are9 at the head and21 at the bottom left. Formula numbers10,11,12 occur in that physical order. No date is visible. Scan22 is only the editorial identifier. H’s editorial page notice and interpretive notes are not copied as manuscript text, while its omission of footer21 is logged as a real omission.',
        'The whole image and each supplied native overlapping half were read once for this first pass; ten enlarged crops were made once and individually inspected. Root reviewed all ten crops and confirmed the principal readings and nonverbal-mark treatment. No other page, OCR, external source or TeX compilation was used.'
    ],
    'check_events': [], 'diff_coverage': diff_coverage
}
(out / '145_scan022.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')

# Structural validation only: no compilation or further image reading.
with (packet / 'marks.tsv').open(newline='') as fh:
    marks = list(csv.DictReader(fh, delimiter='\t'))
assert [x['id'] for x in decisions] == [x['id'] for x in marks]
assert len(raw_diffs) == len(diff_coverage) == 50
assert [x['row'] for x in diff_coverage] == list(range(1, 51))
assert all(x['c_changed'] or x['h_changed'] for x in changes)
assert len({x['id'] for x in changes}) == len(changes)
assert len({x['box'] for x in second_boxes}) == len(second_boxes)
for item in changes + decisions + unlisted:
    assert (root / 'edition' / item['crop']).is_file()
    x0, y0, x1, y1 = item['box']
    assert 0 <= x0 < x1 <= 1678 and 0 <= y0 < y1 <= 2364
for item in inventory:
    assert item['sheet_kind'] == 'text' and item['hand'] == 'his hand'
for item in second_boxes:
    x0, y0, x1, y1 = item['coords']
    assert 0 <= x0 < x1 <= 1678 and 0 <= y0 < y1 <= 2364
depth = 0
for match in re.finditer(r'(?<!\\)[{}]', tex):
    depth += 1 if match.group() == '{' else -1
    assert depth >= 0
assert depth == 0
assert tex.count('$') % 2 == 0
assert tex.count(r'\[') == tex.count(r'\]') == 5
assert tex.count(r'\begin{aligned}') == tex.count(r'\end{aligned}') == 2
assert tex.count(r'\begin{tikzpicture}') == tex.count(r'\end{tikzpicture}') == 2
assert tex.count(r'\deleted{') == 7
assert tex.count(r'\unsure{') == 10
assert not re.search(r'\\(?:rho|infty)(?:l|varepsilon)\b', tex)
print(json.dumps({'scan': 22, 'changes': len(changes), 'marks': len(decisions),
                  'unlisted_decisions': len(unlisted), 'doubts': len(doubts),
                  'inventory': len(inventory), 'second_boxes': len(second_boxes),
                  'diff_rows': len(diff_coverage), 'crops': len(manifest),
                  'validation': 'structural checks passed'}, ensure_ascii=False))
