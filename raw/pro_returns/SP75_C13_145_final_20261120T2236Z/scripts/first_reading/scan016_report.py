from pathlib import Path
import csv
import json

ROOT = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
PACKET = ROOT / 'packets/145_scan016'
OUT = ROOT / 'edition'

boxes = {
    'profinis': [230,65,480,175],
    'plural_groupoides': [220,165,1645,365],
    'on_pourra': [1090,260,1425,360],
    'initial_pi_formula': [500,390,1170,620],
    'dotted_rho': [210,820,900,945],
    'struck_qui': [205,940,725,1035],
    'aut_complexes_sigmas': [355,1190,1080,1340],
    'echangent_fixent': [1200,1190,1660,1335],
    'struck_sur': [195,1340,510,1435],
    'sont_resp': [215,1410,500,1520],
    'rotations_symetries': [515,1395,760,1505],
    'struck_axes': [1245,1395,1375,1505],
    'oblique_margin': [15,1200,420,2130],
    'au_plan': [780,1590,1420,1685],
    'ornamental_s_pair': [890,1660,1330,1880],
    'dotted_sigmas_semicolon': [600,1865,1555,2000],
    'dotted_tau_extension_label': [205,1970,1515,2095],
    'extension_notation': [210,2055,1480,2195],
    'final_extension_display': [520,2200,1290,2348],
    'manuscript_number_fifteen': [25,2265,105,2345],
}

def crop(name):
    return 'crops/145_scan016_' + name + '.png'

S = r'\unsure{\mathfrak S_3|\mathcal S_3}'
initial = (
    r'\Pi=\Pi_{\unsure{1|*}}(\overbrace{\mathbb P^1(\mathbb C)'
    r'\setminus\{0,1,\infty\}}^{U=U_{0,3}},P)'
)
ending = (
    r'\mathcal E=\Pi_1\left(\underset{\substack{\Vert\\U_{0,3}}}'
    r'{U_{\deleted{\unsure{0,3}}}},\underbrace{'
    + S + r'\times\mathbb Z/2}_{\Gamma};P\right)'
)
margin = r"""\margin{Sur la sphère de Riemann on a
\[
\begin{aligned}
\sigma_0(z)&=\frac{-z}{1-z}=\frac{z}{z-1}\\
\sigma_1(z)&=\frac1z\\
\sigma_\infty(z)&=1-z\\
\rho(z)&=\frac1{1-z}\\
\rho^2(z)&=1-\frac1z
\end{aligned}
\]}"""

tex = (PACKET / 'C.tex').read_text()
replacements = [
    (r'\pi=\pi_{0,3}', r'\Pi=\Pi_{0,3}'),
    (r'\pi=\pi_{\unsure{1|*}}', r'\Pi=\Pi_{\unsure{1|*}}'),
    (r'\inserted{\deleted{fixent}}', r'\inserted{\deleted{\unsure{fixent}}}'),
    (r'\deleted{\unsure{sur}} sur', r'\deleted{\unsure{resp|sur}.} sur'),
    (r'\deleted{rotations}', r'\deleted{\unsure{rotations}}'),
    (r'\rho^2(z)&=1-\frac1z.', r'\rho^2(z)&=1-\frac1z'),
    ('comme opérant sur la sphère, via', 'comme opérant sur la sphère; via'),
    (r"\inserted{$\unsure{\mathcal E_0}$}", r"\inserted{$\deleted{\unsure{\mathcal E_0}}$}"),
    (r'par $\pi$,', r'par $\Pi$,'),
    (r'\mathcal E=\pi_1', r'\mathcal E=\Pi_1'),
]
for old, new in replacements:
    assert tex.count(old) == 1, (old, tex.count(old))
    tex = tex.replace(old, new)
assert initial in tex
assert ending in tex
assert margin in tex
(OUT / 'reader_reports/145_scan016.tex').write_text(tex)

changes = []

def change(n, place, C, H, final, ink, confidence, kind, cc, hc, marked, name, cats, consequence=''):
    changes.append({
        'id': f's016-{n:02d}', 'place': place, 'C': C, 'H': H, 'final': final,
        'ink': ink, 'confidence': confidence, 'kind': kind,
        'c_changed': cc, 'h_changed': hc, 'marked_in_H': marked,
        'crop': crop(name), 'box': boxes[name], 'error_category': cats,
        'math_consequence': consequence,
    })

change(1, 'opening line, first word', 'profinis,', 'profini,', 'profinis,',
       'The p descender and tall f are clear. After the compressed ini body there is a separate small terminal s hook before the comma; H drops this final consonant.',
       'high', 'misread word', False, True, 'no', 'profinis', [2])
change(2, 'opening prose, lines 2–3 across the fonda-/mentaux line break',
       'des groupoïdes fondamentaux', 'du groupoïde fondamental', 'des groupoïdes fondamentaux',
       'The article has the e body and a terminal s hook. groupoïdes also has a final s. The adjective is physically divided fonda-/mentaux; the lower continuation visibly ends aux, not al. These plural endings are ink readings, not agreement supplied by grammar.',
       'high', 'misread word', False, True, 'no', 'plural_groupoides', [2])
change(3, 'end of opening prose line 3',
       r'On \deleted{pourra}', r'\struck{On pose} On', r'On \deleted{pourra}',
       'On lies before and outside the strike. The cancelled word has the p descender, rounded o, low u, two short r bodies and terminal a of pourra. No second On follows and no pose is written.',
       'high', 'misread word', False, True, 'no', 'on_pourra', [2,7,9])
change(4, 'naming of the discrete group, line 4',
       r'\pi=\pi_{0,3}', r'\Pi = \Pi_{0,3}', r'\Pi=\Pi_{0,3}',
       'Both signs have a long top bar and two separate tall straight legs; the indexed one has a round 0, comma and open 3 below it. These local forms support capital Pi.',
       'high', 'misread symbol or index', True, False, 'no', 'initial_pi_formula', [1],
       'Preserves the locally written tall Pi form in the name of the discrete group.')
change(5, 'first display, left member and fundamental-group sign',
       r'\pi=\pi_{\unsure{1|*}}', r'\Pi = \pi_1', r'\Pi=\Pi_{\unsure{1|*}}',
       'The two displayed Pi signs have the same top bar and long separate legs as the naming immediately above. The small index of the right sign is dark and overwritten, with several branching lobes; it does not independently decide 1 against *. The whole displayed expression was read.',
       'high', 'misread symbol or index', True, True, 'no', 'initial_pi_formula', [1],
       'The sign is transcribed as capital Pi; the index remains explicitly uncertain.')
change(6, 'first display, between the projective line and the puncture set',
       r'\mathbb P^1(\mathbb C)\setminus\{0,1,\infty\}',
       r'\mathbb{P}^1(\mathbb{C}) - \{0, 1, \infty\}',
       r'\mathbb P^1(\mathbb C)\setminus\{0,1,\infty\}',
       'The separation mark descends obliquely from left to right and has substantial vertical extent. It is not the level short minus drawn elsewhere in the same calculation. The set braces and the three entries are visible.',
       'high', 'misread symbol or index', False, True, 'no', 'initial_pi_formula', [1],
       'Retains the written set-difference sign.')
change(7, 'rotation named above the baseline, before d’angle',
       r'\inserted{$\dot\rho$}', r'$\rho$', r'\inserted{$\dot\rho$}',
       'A dark round dot is separated from the rho loop above and to its right. The loop, long descender and raised position are clear. The insertion belongs between rotation and d’angle; the following angle is +2pi/3.',
       'high', 'misread symbol or index', False, True, 'no', 'dotted_rho', [1,6],
       'Restores the dotted notation for the geometric rotation.')
change(8, 'cancelled word after P, barred P',
       r'\deleted{\unsure{qui}}', r'\struck{\ill{}}', r'\deleted{\unsure{qui}}',
       'A small loop with a descending stroke supports q, followed by strokes compatible with ui. Crossing strokes and dark overlap prevent separating every letter or a final i dot. The tentative qui is retained as a doubt, not resolved.',
       'low', r'readable ink left as \ill{}', False, True, 'yes', 'struck_qui', [5,7])
change(9, 'aut complexes and the raised sigma list, main line 12',
       r'aut complexes \inserted{$\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$}',
       r'$\sigma_0, \sigma_1, \sigma_\infty$ \struck{\ill{}} sont les automorphismes \ill{}',
       r'aut complexes \inserted{$\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$}',
       'The baseline reads aut complexes: a/u bodies and tall crossed t are clear, with no stop after aut; complexes has co, the p descender, tall l and the final x/es sequence. None is struck. The raised list has a distinct dot for each sigma and the indices 0,1,infinity. A guide attaches the list after complexes and before de. H’s sont les automorphismes and cancelled material at this point are absent.',
       'high', 'misread word', False, True, 'yes', 'aut_complexes_sigmas', [1,2,5,6,8,9],
       'Preserves the abbreviation and the insertion of the three dotted geometric involutions.')
change(10, 'cancelled baseline verb before live induisent',
       r'\deleted{\unsure{échangent}}', r'\struck{\ill{}}', r'\deleted{\unsure{échangent}}',
       'The opening accented e/c/h shapes and the g descender support échangent. The central letters and final nt meet the cancellation line, so not every letter can be separated. The reading remains tentative.',
       'low', r'readable ink left as \ill{}', False, True, 'yes', 'echangent_fixent', [5,7])
change(11, 'cancelled word immediately before the live sur of line 13',
       r'\deleted{\unsure{sur}} sur', 'sur', r'\deleted{\unsure{resp|sur}.} sur',
       'The crossed word has an initial rising body, a largely horizontal middle and a descending stroke close to its right end. A detached dark terminal point is plain. The descender and point resemble the clear inserted resp. immediately below more closely than sur, but the middle is too obscured to settle the word. The live sur to its right is separate and unstruck.',
       'medium', 'misread word', True, True, 'no', 'struck_sur', [2,3,7,10])
change(12, 'sont and its interlinear qualification, before les symétries',
       r'sont \inserted{resp.}', 'i.e.', r'sont \inserted{resp.}',
       'The baseline has the separate s/o traces, horizontal n and terminal tall t of sont. Above it, resp. has a short initial r, compressed es, a long p descender and a separate stop. The curved guide returns to the gap before les. There is no i.e. on the baseline.',
       'high', 'misread word', False, True, 'no', 'sont_resp', [2,6,9])
change(13, 'crossed axis notation immediately before (0,2)',
       r'\deleted{$\unsure{P,\bar P}$}', '', r'\deleted{$\unsure{P,\bar P}$}',
       'Two tall letter bodies and a low comma survive beneath horizontal and oblique cancellation strokes. They support P, barred P, but the right head and any independent bar are obscured. The crossed notation is present and must not be omitted.',
       'low', 'omission', False, True, 'no', 'struck_axes', [3,7],
       'Retains an abandoned axis notation without resolving its obscured components.')
change(14, 'heading of the oblique left-margin calculation',
       'Sur la sphère de Riemann on a', 'sur la sphère on a', 'Sur la sphère de Riemann on a',
       'After sphère there is a small de, then a tall initial R, dotted i and the connected e/m/a/n/n sequence of Riemann. This continuous cursive is live; it is not a separate struck word. on a occupies the next slanted line. The initial S of Sur is tall.',
       'high', 'omission', False, True, 'no', 'oblique_margin', [2,3,7])
change(15, 'line endings of the first four margin formulas',
       r'\sigma_0(z)=\frac{-z}{1-z}=\frac{z}{z-1}\\ \sigma_1(z)=\frac1z\\ \sigma_\infty(z)=1-z\\ \rho(z)=\frac1{1-z}',
       r'$\sigma_0(z) = \frac{-z}{1-z} = \frac{z}{z-1}$, $\sigma_1(z) = \frac{1}{z}$, $\sigma_\infty(z) = 1 - z$, $\rho(z) = \frac{1}{1-z}$,',
       r'\sigma_0(z)=\frac{-z}{1-z}=\frac{z}{z-1}\\ \sigma_1(z)=\frac1z\\ \sigma_\infty(z)=1-z\\ \rho(z)=\frac1{1-z}',
       'The five equalities are written on separate oblique rows. After the final term of each of the first four rows there is blank paper, with no comma. H supplies commas when recasting the rows as an inline list.',
       'high', 'other', False, True, 'no', 'oblique_margin', [10])
change(16, 'last margin formula, final punctuation',
       r'\rho^2(z)=1-\frac1z.', r'\rho^2(z) = 1 - \frac{1}{z}', r'\rho^2(z)=1-\frac1z',
       'The last row ends with the denominator z. There is no dark punctuation mark immediately after the fraction. A remote small speck below and left is not in the terminal punctuation position.',
       'high', 'other', True, False, 'no', 'oblique_margin', [10])
change(17, 'punctuation between sphère and via, line 19',
       'sur la sphère, via', 'sur la sphère, via', 'sur la sphère; via',
       'A comma-shaped lower stroke has a separate dark upper point above it. The two-level punctuation is a semicolon, not a comma.',
       'high', 'other', True, True, 'no', 'dotted_sigmas_semicolon', [10])
change(18, 'later inline sigma list, after via les',
       r'\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty',
       r'\sigma_0, \sigma_1, \sigma_\infty',
       r'\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty',
       'Each of the three sigma bodies has a separate dark dot above and slightly to its right. The low round 0, vertical 1 and double-loop infinity are clear; the dots are not those subscripts or punctuation.',
       'high', 'misread symbol or index', False, True, 'no', 'dotted_sigmas_semicolon', [1],
       'Distinguishes the dotted geometric action symbols from the undotted margin transformations.')
change(19, 'tau in the membership statement, line 20',
       r'\dot\tau\in\mathbb Z/2', r'\tau \in \mathbb{Z}/2', r'\dot\tau\in\mathbb Z/2',
       'The tau body has a horizontal top and curled short upright. A distinct dark dot stands above its right end. Membership, the double-stroked Z, slash and 2 are visible.',
       'high', 'misread symbol or index', False, True, 'no', 'dotted_tau_extension_label', [1],
       'Retains the dotted symbol for complex conjugation.')
change(20, 'raised and overwritten extension label after l’extension',
       r'\inserted{$\unsure{\mathcal E_0}$}', r'\struck{\ill{}}',
       r'\inserted{$\deleted{\unsure{\mathcal E_0}}$}',
       'The guide rises from after extension to the raised label. Curved E-like strokes and a small closed low body support script E with index 0. Oblique overlapping strokes traverse the left and middle of the raised label, supporting cancellation; their order relative to the dark rewriting cannot be reconstructed. The insertion is recorded as struck, while the reading and index remain uncertain. The upper edge is also visible in the overlapping dotted_sigmas_semicolon crop.',
       'medium', 'deletion state', True, True, 'yes', 'dotted_tau_extension_label', [5,6,7],
       'Records an abandoned extension label rather than treating it as a live additional name.')
changes[-1]['additional_crop'] = crop('dotted_sigmas_semicolon')
changes[-1]['additional_box'] = boxes['dotted_sigmas_semicolon']
change(21, 'group after par in the extension sentence',
       r'par $\pi$,', r'par $\Pi$,', r'par $\Pi$,',
       'The isolated sign after par has a level cap and two tall vertical legs, matching the capital Pi forms in the naming and first display. Its comma is separate.',
       'high', 'misread symbol or index', True, False, 'no', 'extension_notation', [1])
change(22, 'raised E0,3 ou attached before the baseline E',
       r'notée \inserted{$\mathcal E_{0,3}$ ou} $\mathcal E$',
       r'notée $\mathcal{E}$ \marginal{$\mathcal{E}_{0,3}$ ou}',
       r'notée \inserted{$\mathcal E_{0,3}$ ou} $\mathcal E$',
       'The raised text reads script E with 0, comma, 3, then ou. Its curved insertion guide descends into the gap immediately before the baseline E, after notée. It therefore reads E0,3 ou E, not E followed by an unattached E0,3 ou.',
       'high', 'insertion or placement', False, True, 'no', 'extension_notation', [6],
       'Preserves the attachment of the two alternative extension names.')
changes[-1]['additional_crop'] = crop('dotted_tau_extension_label')
changes[-1]['additional_box'] = boxes['dotted_tau_extension_label']
change(23, 'final display, fundamental-group sign',
       r'\mathcal E=\pi_1', r'\mathcal{E} = \pi_1', r'\mathcal E=\Pi_1',
       'The sign has a long cap and two distinct full-height legs. The right leg reaches the baseline; the subscript 1 is a separate short vertical stroke. This is the same tall Pi form as earlier on this page. The later underbrace label has only a short downturned right tip and is Gamma, not this two-legged sign.',
       'high', 'misread symbol or index', True, True, 'no', 'final_extension_display', [1])
change(24, 'final display, cancelled subscript on upper U',
       r'\underset{\substack{\Vert\\U_{0,3}}}{U_{\deleted{\unsure{0,3}}}}',
       r'\underset{\substack{\| \\ U_{0,3}}}{U}',
       r'\underset{\substack{\Vert\\U_{0,3}}}{U_{\deleted{\unsure{0,3}}}}',
       'To the lower right of the upper U, looped and curved small strokes are visibly crossed. They are compatible with 0,3 but not separable enough to resolve. Below the U stand two short parallel uprights and the clear replacement U0,3. H omits the crossed subscript.',
       'medium', 'omission', False, True, 'no', 'final_extension_display', [3,7],
       'Preserves the cancellation while retaining the clear lower U0,3 annotation.')
change(25, 'lower-left handwritten page number',
       r'\mspage{15}', '', r'\mspage{15}',
       'A tall angled-entry 1 stands beside a 5 with an upper horizontal stroke, short downstroke and broad curved lower bowl. This is an actual ink page number, not the editorial scan identifier.',
       'high', 'omission', False, True, 'no', 'manuscript_number_fifteen', [3])

decisions = []
def decision(id, name, reading, ink, confidence='medium', result='undecided'):
    decisions.append({
        'id': id, 'decision': result, 'reading': reading, 'ink': ink,
        'crop': crop(name), 'box': boxes[name], 'confidence': confidence,
    })

decision('M0810', 'initial_pi_formula', r'\unsure{1|*}',
         'The small index is overwritten and has several dark branching lobes. Neither a single 1 stroke nor the complete arms of a star can be isolated; the surrounding displayed formula is otherwise read.', 'low')
decision('M0811', 'au_plan', r'\unsure{au|un}',
         'The first small body is compressed almost to a horizontal dark mark; the following shallow connected body could be u or n. au is favored, but the strokes alone do not securely exclude un.')
for id, name, place in [
    ('M0812','ornamental_s_pair','first On considère'),
    ('M0813','ornamental_s_pair','second product with Z/2'),
    ('M0814','dotted_sigmas_semicolon','membership after the later sigma list'),
]:
    decision(id, name, S,
             'At '+place+', the capital has a large rounded outer sweep and an inner returning curve, with a separate small 3. Its identity as the ornate S is clear, but handwritten shape does not securely choose between the two supplied TeX alphabets.')
decision('M0815','dotted_tau_extension_label',r'\inserted{$\deleted{\unsure{\mathcal E_0}}$}',
         'Raised curved E-like strokes and a low closed index are crossed by oblique overlapping strokes. The label is treated as inserted and struck; E0 remains tentative, and the exact overwrite sequence cannot be established. Its upper edge is in the overlapping sigma crop.', 'low')
decisions[-1]['additional_crop'] = crop('dotted_sigmas_semicolon')
decisions[-1]['additional_box'] = boxes['dotted_sigmas_semicolon']
decision('M0816','extension_notation',S,
         'The product at the beginning of the last prose line has the same rounded outer sweep, returning inner curve and separate 3. The S identity is plain; the typographic alphabet remains open.')
decision('M0817','final_extension_display',S,
         'The final displayed product has the same ornate S form and separate 3. Its whole surrounding formula, lower U annotation, underbrace and Gamma label were read; the alphabet choice remains unresolved.')

unlisted_decisions = []
for id, name, reading, ink, conf in [
    ('U016-01','struck_qui',r'\deleted{\unsure{qui}}','q-like loop and descending stroke survive; ui and its dot cannot be separated through the cancellation.','low'),
    ('U016-02','echangent_fixent',r'\deleted{\unsure{échangent}}','The opening e/c/h and g descender support the word; the crossed middle and final nt are not all individually plain.','low'),
    ('U016-03','struck_sur',r'\deleted{\unsure{resp|sur}.}','A right-hand descender and separate terminal point favor resp. over C’s sur; the flattened middle leaves the alternative open. The visible stop is retained outside the doubt.','medium'),
    ('U016-04','struck_axes',r'\deleted{$\unsure{P,\bar P}$}','Two upright letter bodies and a comma survive; hatching hides the right head and any distinct bar.','low'),
    ('U016-05','final_extension_display',r'\deleted{\unsure{0,3}}','The upper U has a crossed small index; loop and curve fragments support 0,3 but do not securely resolve it.','low'),
]:
    unlisted_decisions.append({
        'id':id,'decision':'undecided','reading':reading,'ink':ink,
        'crop':crop(name),'box':boxes[name],'confidence':conf,
    })

doubts = [
    {'place':'first display, right Pi index','reading':r'\unsure{1|*}','alternatives':['1','*'],'confidence':'low','reason':'Overwritten, branching dark strokes do not isolate either complete alternative.'},
    {'place':'cancelled word after P, barred P','reading':r'\deleted{\unsure{qui}}','alternatives':['qui'],'confidence':'low','reason':'A q-like loop survives, but the remaining letters and i dot are not independently clear.'},
    {'place':'cancelled baseline verb before induisent','reading':r'\deleted{\unsure{échangent}}','alternatives':['échangent'],'confidence':'low','reason':'Beginning and g descender support the word; the cancellation covers several central and final strokes.'},
    {'place':'inserted and then struck replacement above échangent','reading':r'\inserted{\deleted{\unsure{fixent}}}','alternatives':['fixent'],'confidence':'medium','reason':'New local doubt: f, the i dot, x and the terminal t-like stroke are visible, but e/n are flattened by the horizontal strike. Agreement of C and H does not resolve them.'},
    {'place':'cancelled word before live sur','reading':r'\deleted{\unsure{resp|sur}.}','alternatives':['resp.','sur.'],'confidence':'medium','reason':'Right descender and stop favor resp.; the obscured body does not exclude C’s sur. The terminal point is certain.'},
    {'place':'cancelled rotations below symétries','reading':r'\deleted{\unsure{rotations}}','alternatives':['rotations'],'confidence':'medium','reason':'New local doubt: opening r/o, tall strokes and the terminal ons contour are recognizable, but the heavy cancellation flattens the middle a/ti sequence.'},
    {'place':'cancelled axis notation before (0,2)','reading':r'\deleted{$\unsure{P,\bar P}$}','alternatives':[r'P,\bar P'],'confidence':'low','reason':'Hatching obscures the letter heads and whether the bar is independent of the cancellation.'},
    {'place':'p.r. au/un plan','reading':r'\unsure{au|un}','alternatives':['au','un'],'confidence':'medium','reason':'au is favored, but the compressed first body and shallow following strokes do not conclusively distinguish the alternatives.'},
    {'place':'first On considère, ornate S3','reading':S,'alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'Ornate S and index 3 are clear; the exact TeX alphabet remains a representational uncertainty.'},
    {'place':'cet ordre, et ornate S3 times Z/2','reading':S,'alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'Rounded outer sweep and returning inner curve do not settle the supplied typographic alternatives.'},
    {'place':'membership following the later dotted sigma list','reading':S,'alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'The S identity and 3 are clear; the exact alphabet remains unresolved.'},
    {'place':'raised and struck extension label','reading':r'\inserted{$\deleted{\unsure{\mathcal E_0}}$}','alternatives':[r'\mathcal E_0'],'confidence':'low','reason':'Crossed and overwritten E-like strokes with a low closed index support E0. The exact index and stroke sequence remain uncertain, although insertion and cancellation are recorded.'},
    {'place':'product beginning the last prose line','reading':S,'alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'Same local ornate S form; neither supplied alphabet is decisively distinguished.'},
    {'place':'upper U subscript in final display','reading':r'\deleted{\unsure{0,3}}','alternatives':['0,3'],'confidence':'low','reason':'The cancellation crosses both small digit bodies; the lower replacement U0,3 is clear but does not license resolving the old subscript.'},
    {'place':'product under the final display brace','reading':S,'alternatives':[r'\mathfrak S_3',r'\mathcal S_3'],'confidence':'medium','reason':'Identity S3 clear; typographic alphabet left open.'},
]

inventory = []
def inv(kind, position, words, box):
    inventory.append({
        'element':f'I{len(inventory)+1:02d}','kind':kind,'position':position,
        'first_words_or_objects':words,'box':box,'sheet_kind':'text',
        'hand':'his hand','transcribed':'yes',
    })

inv('text','top prose, four physical baseline lines','profinis, dans une certaine mesure !) utiliser',[220,65,1645,465])
inv('display','first main display, with upper brace caption',initial,[500,465,1170,620])
inv('text','sphere structure and cyclic rotation paragraph','où ... riemannienne ... la rotation ... permutation circulaire',[205,620,1645,1210])
inv('text','automorphisms, revised verbs and symmetry-axis list','où les aut complexes ... autour des axes',[205,1190,1660,1620])
inv('text','conjugation and extension construction','Quant à la conjugaison complexe ... définie par',[205,1520,1645,2195])
inv('display','bottom display with struck upper index and lower annotations',ending,[520,2200,1290,2348])
inv('margin note','oblique left margin, two heading rows and five formula rows',margin,boxes['oblique_margin'])
inv('text','lower-left handwritten pagination',r'\mspage{15}',boxes['manuscript_number_fifteen'])
inv('deletion','end of opening line 3',r'\deleted{pourra}',boxes['on_pourra'])
inv('insertion','above structure / before riemannienne',r'\inserted{de sphère}',[205,580,1645,725])
inv('insertion','above riemannienne / before unique',r'\inserted{orientée}',[205,690,1645,820])
inv('insertion','raised symbol after rotation',r'\inserted{$\dot\rho$}',boxes['dotted_rho'])
inv('deletion','after P, barred P',r'\deleted{\unsure{qui}}',boxes['struck_qui'])
inv('insertion','above complexes / before de',r'\inserted{$\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$}',boxes['aut_complexes_sigmas'])
inv('deletion','baseline before induisent',r'\deleted{\unsure{échangent}}',boxes['echangent_fixent'])
inv('insertion','above cancelled échangent, itself cancelled',r'\inserted{\deleted{\unsure{fixent}}}',boxes['echangent_fixent'])
inv('deletion','strike through the raised replacement fixent',r'\deleted{\unsure{fixent}}',boxes['echangent_fixent'])
inv('deletion','before the live sur of the transpositions line',r'\deleted{\unsure{resp|sur}.}',boxes['struck_sur'])
inv('insertion','above sont, attaching before les',r'\inserted{resp.}',boxes['sont_resp'])
inv('deletion','below replacement symétries',r'\deleted{\unsure{rotations}}',boxes['rotations_symetries'])
inv('insertion','above cancelled rotations',r'\inserted{symétries}',boxes['rotations_symetries'])
inv('deletion','before the first surviving axis pair',r'\deleted{$\unsure{P,\bar P}$}',boxes['struck_axes'])
inv('insertion','above extension, attached after that word; itself struck',r'\inserted{$\deleted{\unsure{\mathcal E_0}}$}',[1300,1935,1470,2055])
inv('deletion','oblique cancellation through the raised extension label',r'$\deleted{\unsure{\mathcal E_0}}$',[1300,1935,1470,2055])
inv('insertion','above notée E, guide attaching before E',r'\inserted{$\mathcal E_{0,3}$ ou}',[900,2020,1145,2170])
inv('deletion','small subscript on upper U of bottom display',r'\deleted{\unsure{0,3}}',boxes['final_extension_display'])

second_boxes = []
def second(kind, coords, reading):
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,'coords':coords,'reading':reading})

second('lexical C/H disagreement',boxes['profinis'],'profinis,')
second('plural C/H disagreement and complete first prose formula with handwritten numbers',
       [220,165,1645,365],
       r'le langage géométrique des groupoïdes fondamentaux de $\mathbb P^1(\mathbb C)-\{0,1,\infty\}$. On \deleted{pourra}')
second('cancelled word and live/cancelled scope disagreement',boxes['on_pourra'],r'On \deleted{pourra}')
second('complete naming and first display; every digit, overwritten index and upper brace caption',
       [205,390,1645,620],
       r'notera donc $\Pi=\Pi_{0,3}$ le groupe discret'+'\n\\[\n'+initial+'\n\\]')
second('two interlinear word insertions and complete projective-line formula including its exponent',
       [205,580,1645,820],
       r'où $\mathbb P^1(\mathbb C)$ est muni de la structure \inserted{de sphère} riemannienne \inserted{orientée} unique pour laquelle')
second('raised dotted rotation symbol and the complete numerical angle',
       [210,820,1645,945],
       r"la rotation \inserted{$\dot\rho$} d'angle $+\frac{2\pi}{3}$ autour de l'axe")
second('struck word and complete puncture tuple and cyclic arrow formula',
       [205,940,1645,1135],
       r'$P,\bar P$ \deleted{\unsure{qui}} induit sur $(0,1,\infty)$ la permutation circulaire $0\longrightarrow1\longrightarrow\infty\longrightarrow0$ (ceci correspond à')
second('lexical disagreement, full inserted sigma formula and projective-line exponent, two deleted verb layers',
       [205,1190,1660,1340],
       r'où les aut complexes \inserted{$\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty$} de $\mathbb P^1_{\mathbb C}$ qui \deleted{\unsure{échangent}} \inserted{\deleted{\unsure{fixent}}} induisent')
second('cancelled abbreviation with surviving point, and both full numerical tuples',
       [195,1340,1660,1435],
       r'\deleted{\unsure{resp|sur}.} sur $(0,1,\infty)$ les transpositions fixant resp. $0,1,\infty$,')
second('inserted abbreviation and replacement noun, cancelled noun and axis notation, first full numeric axis pair',
       [215,1395,1660,1530],
       r'sont \inserted{resp.} les \deleted{\unsure{rotations}} \inserted{symétries} autour des axes \deleted{$\unsure{P,\bar P}$} $(0,2)$,')
second('complete remaining axis pairs including negative digit and fraction',
       [205,1520,1645,1620],
       r'$(1,-1)$ et $(\infty,\frac12)$. Quant à la conjugaison')
second('unresolved au/un reading, with its preceding abbreviation',
       boxes['au_plan'],r"symétrie p.r. \unsure{au|un} plan")
second('complete plane tuple and first ornate-S formula with its index',
       [205,1680,1645,1805],
       r'$(0,1,\infty)$. On considère $'+S+r'$ comme opérant sur')
second('complete action tuple and product formula with every numeric index and quotient',
       [205,1795,1645,1895],
       r'$(0,1,\infty)$ dans cet ordre, et $'+S+r'\times\mathbb Z/2$ comme')
second('semicolon disagreement and complete dotted-sigma membership formula',
       [205,1865,1590,2000],
       r'opérant sur la sphère; via les $\dot\sigma_0,\dot\sigma_1,\dot\sigma_\infty\in'+S+r'$')
second('complete dotted-tau membership formula and raised/struck extension label including its doubtful numeric index',
       [205,1935,1515,2095],
       r"et $\dot\tau\in\mathbb Z/2$. On considère l'extension \inserted{$\deleted{\unsure{\mathcal E_0}}$} de")
second('complete extension product, Pi and interlinear naming formula including every numeric index',
       [210,2020,1515,2195],
       r'$'+S+r'\times\mathbb Z/2$ par $\Pi$, notée \inserted{$\mathcal E_{0,3}$ ou} $\mathcal E$, définie par')
second('complete final doubtful display including every number, deletion, lower U label, brace and Gamma',
       boxes['final_extension_display'],'\\[\n'+ending+'\n\\]')
second('actual handwritten page number omitted in H',
       boxes['manuscript_number_fifteen'],r'\mspage{15}')
second('entire oblique margin, live heading and all five numerical rational formulas',
       boxes['oblique_margin'],margin)

diff_coverage = []
def diff(row, status, explanation, change_id=None):
    d={'row':row,'status':status,'explanation':explanation}
    if change_id:
        d['change_id']=change_id
    diff_coverage.append(d)

diff(1,'substantive','The token 16 is the editorial scan marker and is excluded. The final s of profinis is substantive.','s016-01')
diff(2,'substantive','All three plural forms are supported by the enlarged lexical crop.','s016-02')
diff(3,'substantive','H misreads the cancelled word, extends the deletion over On and duplicates On.','s016-03')
diff(4,'macro/editorial','The 1|* index doubt is retained as M0810; a change of certainty alone is not a changes row. The separately observed Pi case difference is s016-05.')
diff(5,'substantive','The written separation sign is oblique setminus, not the level minus in H.','s016-06')
diff(6,'macro/editorial','Both texts have the actual argument-separating comma. H additionally has a TeX thin-space command backslash-comma; its token is not another ink comma.')
diff(7,'substantive','The struck traces permit a tentative qui; they are not resolved and not omitted.','s016-08')
diff(8,'substantive','Live aut complexes is present; the raised sigma list follows it.','s016-09')
diff(9,'substantive','The extra H sont les automorphismes belongs to the same mistranscribed clause as row 8 and is not ink at that place.','s016-09')
diff(10,'substantive','The baseline cancelled verb supports uncertain échangent. The added uncertainty on the separately inserted-and-struck fixent is in doubts only.','s016-10')
diff(11,'substantive','There is a cancelled word before the live sur. Its descender and terminal dot favor resp., with sur retained as an alternative.','s016-11')
diff(12,'substantive','The baseline sont and raised resp. are visible; H i.e. is not.','s016-12')
diff(13,'macro/editorial','Both witnesses identify symétries as the interlinear replacement and rotations as cancelled at the same location. Their opposite serialization order is not a second lexical inscription. New uncertainty on the cancelled rotations is in doubts only.')
diff(14,'macro/editorial','Paired token realignment with row 13: replacement above the struck word is preserved by the deletion/insertion macros.')
diff(15,'substantive','The crossed P, barred-P-like axis notation is actual ink and remains doubtful.','s016-13')
diff(16,'macro/editorial','C’s unbraced frac12 and H’s braced frac{1}{2} denote the same written fraction one-half.')
diff(17,'substantive','The large token shift results from H moving the margin calculation after the main text. The margin is not wholly absent. Its omitted de Riemann is s016-14; supplied inline commas are s016-15; C’s unsupported final period is s016-16.','s016-14')
diff(18,'macro/editorial','The au|un doubt is retained as M0811; H’s certainty supplies no new inscription.')
diff(19,'macro/editorial','M0812 retains the ornate-S alphabet alternatives; there is no differing word or different group index.')
diff(20,'macro/editorial','M0813 retains the ornate-S alphabet alternatives in the complete product.')
diff(21,'macro/editorial','M0814 retains the ornate-S alphabet alternatives. The substantive omission of dots earlier in the same formula is separately logged as s016-18.')
diff(22,'substantive','Raised E0-like text is present and is inserted-and-struck. The reading remains doubtful, but its diplomatic state changes C and its partly readable content changes H.','s016-20')
diff(23,'macro/editorial','M0816 retains the same ornate-S alphabet alternatives; the nearby Pi case correction is s016-21.')
diff(24,'substantive','H serializes the inserted E0,3 ou after the baseline E; the guide attaches it before E.','s016-22')
diff(25,'substantive','Continuation of the same insertion-placement realignment as row 24.','s016-22')
diff(26,'macro/editorial','The extra vertical-bar token comes from H’s backslash-double-bar notation in the lower U annotation. It is the same pair of short uprights as C’s Vert. The tall Pi case correction is separately s016-23.')
diff(27,'substantive','H omits the crossed upper U subscript, of which this row captures the first token.','s016-24')
diff(28,'substantive','The remaining 3 belongs to the same crossed subscript as row 27. The ornate-S alternatives are certainty/representation only; H’s additional semicolon token is a TeX spacing command, not an ink mark.','s016-24')
diff(29,'macro/editorial','Both texts retain the actual semicolon before P. H’s further backslash-semicolon is TeX spacing and is not a second handwritten semicolon.')
diff(30,'substantive','The actual handwritten page number 15 is omitted in H (s016-25). H’s explanatory notes are editorial, not source inscriptions. Its relocated margin is accounted for by s016-14 through s016-16; no extra struck margin word is visible.','s016-25')

report = {
    'scan':16,'reader':'reader_c','lines_read':42,
    'layout':'Upright handwritten text sheet continuing a sentence. Twenty-two main baseline lines include two displays. Nine interlinear additions revise words and symbols, including two additions later struck. The left margin holds a seven-line oblique calculation. An upper brace caption, two lower annotation levels in the last display, and the lower-left handwritten 15 complete the reading units. No independent diagram or drawing is present.',
    'changes':changes,'decisions':decisions,'unlisted_decisions':unlisted_decisions,
    'doubts':doubts,'inventory':inventory,'second_boxes':second_boxes,
    'notation':[
        'The four Pi forms in the naming and first display, the Pi after par, and the final Pi_1 have long caps and two tall legs. They are transcribed locally as capital Pi. This does not impose case on other pages or change the pi in the numerical angle.',
        'A distinct dot appears over the raised rho, all three raised sigmas, all three later inline sigmas and the later tau. The sigma/rho functions in the oblique margin have no detached upper dots; their dark bar ends are parts of the letters.',
        'The ornate S with index 3 recurs five times. Its identity and index are clear, while the supplied mathfrak/mathcal alternatives are retained at each occurrence.',
        'The two initial basepoints are P and barred P. The abandoned later axis notation plausibly repeats them, but hatching prevents resolution.',
        'The first display’s overbrace covers the punctured projective line and bears U=U0,3. The final display puts two short vertical parallel strokes and U0,3 below the upper U and labels the brace under S3 times Z/2 by Gamma.',
        'The final Gamma has a full left upright, a top bar and only a short downturned right tip; it differs locally from the two full legs of Pi.',
        'The last display retains a comma after the U argument and a semicolon before P. TeX spacing commands in H do not constitute additional punctuation.',
    ],
    'hand':[
        'On this page the plural endings of profinis, des and groupoïdes can be very short terminal hooks. H loses them; the enlarged words support the plural forms.',
        'The word complexes is rapidly connected, with a conspicuous p descender and tall l; its compressed middle caused H to substitute expanded prose and illegibility marks. It is live, not cancelled.',
        'Detached mathematical dots sit above and usually a little to the right of rho, sigma and tau. H repeatedly omits them on this page.',
        'Interlinear guides curve into a precise baseline gap: the sigma list attaches after complexes, resp. before les, and E0,3 ou before the baseline E. A guide must not be mistaken for a strike or punctuation.',
        'Heavy horizontal and oblique cancellation strokes obscure short words and indices. The cancelled resp.|sur. has a right descender and a separate visible stop, resembling the clear raised resp. nearby. The word remains doubtful.',
        'Riemann in the slanted margin is continuous live cursive. Its extended final n strokes do not form a cancellation; H’s editorial suggestion of an unreadable struck margin word is unsupported.',
        'The semicolon after sphère has a dark upper point and lower comma. The manuscript’s separate punctuation points are stronger and better placed than surrounding paper specks.',
    ],
    'abbreviations':[
        {'form':'aut','expansion':'automorphismes','place':'aut complexes before the inserted sigma list; no written terminal stop'},
        {'form':'resp.','expansion':'respectivement','place':'fixant resp. 0,1,infinity and the clear insertion after sont; also favored but uncertain in the cancelled word before sur'},
        {'form':'p.r.','expansion':'par rapport','place':'complex conjugation described as a symmetry relative to a plane'},
    ],
    'notes':[
        'The opening continues a preceding sentence with profinis, dans une certaine mesure !). The limiting phrase and exclamation/closing-parenthesis sequence are the author’s and are preserved. No preceding missing text is supplied.',
        'The author introduces a discrete fundamental group of the complex projective line punctured at 0,1,infinity, based at P, and labels the punctured surface U=U0,3. The first fundamental-group index is overwritten and left as 1|*.',
        'The author describes an oriented Riemannian sphere, a dotted rotation of angle +2pi/3 about the P, barred-P axis, the cyclic permutation 0 to 1 to infinity to 0, and three dotted complex automorphisms inducing the transpositions. The revised noun is symétries, replacing cancelled rotations. These are transcribed claims, not independently verified here.',
        'The oblique margin gives sigma0(z)=-z/(1-z)=z/(z-1), sigma1(z)=1/z, sigma-infinity(z)=1-z, rho(z)=1/(1-z), and rho squared(z)=1-1/z. The heading is Sur la sphère de Riemann, followed on another oblique row by on a. There are no commas between the written formula rows and no final period.',
        'The lower prose describes complex conjugation as the symmetry p.r. au/un plan (0,1,infinity), then an action of the ornate S3 times Z/2 on the sphere. The dotted tau belongs to Z/2. The compressed au/un reading remains uncertain without grammatical normalization.',
        'The author names an extension by the discrete group, inserts E0,3 ou before the live E, and writes the final fundamental-group display with a lower U0,3 annotation and an underbrace labelled Gamma. The earlier raised E0-like label is inserted and cancelled; its exact reading and overwriting chronology remain uncertain.',
        'All C insertions and deletions were checked individually against the first half readings and the saved crops. New doubts on the cancelled fixent and rotations are certainty changes only and therefore have no changes row. Unindexed struck doubts are kept in unlisted_decisions, not mixed into the eight MARKS decisions.',
        'The twenty saved crops are the only first-reading enlarged loci; the margin crop is rotated clockwise 45 degrees. Two overlapping existing crops jointly expose the raised E0 label and the E0,3 ou insertion. No new crop was made to revisit either place.',
        'The actual handwritten page number is 15 at lower left. The scan identifier 16 is editorial. No date is visible. The sheet and all visible inscriptions appear to be in his hand.',
        'The count of 42 read units comprises 22 main baseline lines, nine interlinear addition lines, seven oblique margin lines, one upper brace-caption line, two lower annotation levels in the final display, and the handwritten pagination. Whole page, top half and bottom half were viewed once each; every agreement was read as well as every disagreement.',
        'No mathematical verification, proof reconstruction or external comparison was performed by this reader. The root reader may add targeted checks separately. No claim is corrected to a mathematically expected form.',
    ],
    'check_events':[],
    'diff_coverage':diff_coverage,
}

mark_ids = [r['id'] for r in csv.DictReader((PACKET/'marks.tsv').open(), delimiter='\t')]
assert [d['id'] for d in decisions] == mark_ids
assert len(diff_coverage) == len(list(csv.DictReader((PACKET/'differences.tsv').open(), delimiter='\t')))
assert [d['row'] for d in diff_coverage] == list(range(1,31))
assert all(c['c_changed'] or c['h_changed'] for c in changes)
for obj in changes + decisions + unlisted_decisions:
    assert (OUT / obj['crop']).is_file(), obj['crop']
    assert len(obj['box']) == 4
    x0,y0,x1,y1 = obj['box']
    assert 0 <= x0 < x1 <= 1677 and 0 <= y0 < y1 <= 2362
for obj in inventory:
    assert obj['sheet_kind'] == 'text' and obj['hand'] == 'his hand' and obj['transcribed'] == 'yes'
for obj in inventory + second_boxes:
    b = obj.get('coords',obj.get('box'))
    x0,y0,x1,y1 = b
    assert 0 <= x0 < x1 <= 1677 and 0 <= y0 < y1 <= 2362, obj
assert len(set(o['box'] for o in second_boxes)) == len(second_boxes)
assert len(changes) == 25
assert len(doubts) == 15
assert tex.count(r'\unsure{') == len(doubts)
(OUT/'reader_reports/145_scan016.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({
    'scan':16,'changes':len(changes),'indexed_decisions':len(decisions),
    'unlisted_decisions':len(unlisted_decisions),'doubts':len(doubts),
    'inventory':len(inventory),'second_boxes':len(second_boxes),
    'diff_rows':len(diff_coverage),'crops':len(boxes),
    'C_changed':sum(c['c_changed'] for c in changes),
    'H_changed':sum(c['h_changed'] for c in changes),
},indent=2))
