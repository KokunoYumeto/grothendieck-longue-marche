import csv
import json
import re
from pathlib import Path

root = Path('/workspace/scratch/ea90d891106a')
work = root / 'SP78_C13_147_work'
out = work / 'reader_returns/147_scan072'
packet = root / 'runtime/packets/147_scan072'
boxes = json.loads((out/'crop_boxes.json').read_text())
proposed = (out/'proposed.tex').read_text()

canceled88 = r"\deleted{\simeq\bigl(\mathbb P^1_{\mathbb Z},\text{ avec signatures }4\text{ et }6\text{ le long des sections }0\text{ et }\unsure{J_1|j_1}=2^{\unsure{\alpha}}3^{\unsure{\beta}}\text{ (correspond. à la courbe elliptique d'autom }\unsure{\mathbb Z/4\mathbb Z|\mathbb Z/6\mathbb Z}\bigr)}"
canceled_line = r"\deleted{dans le dernier iso, \inserted{\deleted{\unsure{lorsque}}} la section à \unsure{l'infini} de $\widehat M_{D_1}$}"
eq89 = r'''(89)\qquad\left\{\begin{aligned}
\widehat M_G&\simeq\prod_{\alpha\in S}\widehat M^{!}_{g_\alpha,\widehat\nu_\alpha}\\
M_G&\simeq\prod_{\alpha\in S}\overset{\deleted{\unsure{\wedge}}}{M}^{!}_{g_\alpha,\widehat\nu_\alpha}
\end{aligned}\right.'''

changes = []
def change(place, c, h, final, evidence, crop, confidence='high', against_c=False,
           against_h=True, kind='misread word', sheet='words', marked=False,
           consequential=False):
    key = f'{crop:02}'
    changes.append(dict(id=f'072-{len(changes)+1:02}', place=place, C=c, H=h,
                        final=final, evidence=evidence,
                        crop=f'147_scan072_place{key}.png', box=boxes[key],
                        confidence=confidence, against_C=against_c, against_H=against_h,
                        kind=kind, marked_in_H=marked, error_sheet_kind=sheet,
                        consequential=consequential))

change('Introduction to (88), after D\'autre part,', 'on a', '', 'on a',
       'After the comma are a low linked on group and a separate small closed, ink-filled a. They are baseline writing before the display, not stray punctuation.', 1,
       kind='omission', sheet='omissions')
change('Whole live line of (88), first relation',
       r'\widehat M_{D_1}=\widehat M_{G_1}\simeq\widehat M_{1,1}',
       r'\widehat{M}_{D_1} \simeq \widehat{M}_{G_1} \simeq \widehat{M}_{1,1}',
       r'\widehat M_{D_1}\unsure{=|\simeq}\widehat M_{G_1}\simeq\widehat M_{1,1}',
       'The first sign has a straight lower bar and an upper stroke with only a shallow hook, less curved than the following explicit tilde. Equality remains preferred, but the upper stroke is not perfectly straight; neither = nor an isomorphism sign is ruled out. All three hats and the full D_1, G_1, 1,1 indices were read together. Adding this doubt is certainty-only against C; the H comparison remains unresolved.', 2,
       confidence='medium', kind='misread symbol or index', sheet='symbols and indices',
       consequential=True)
change('Cancellation begins at the next relation and includes the projective-line term',
       r'\deleted{\simeq\bigl(\mathbb P^1_{\mathbb Z},',
       r'\simeq (\mathbb{P}^1_{\mathbb{Z}},',
       r'\deleted{\simeq\bigl(\mathbb P^1_{\mathbb Z},',
       'Large diagonal cancellation strokes cover the continuation beginning with the isomorphism sign and the opening projective-line term. H leaves this prefix live in its main display and relegates subsequent words to an editorial note. The cited strings are the beginning of the longer span; its complete exact reading is supplied in B05.', 3,
       kind='deletion state', sheet='struck text', consequential=True)
change('Canceled continuation of (88), noun after avec', 'signatures',
       'singularités', 'signatures',
       'The word has the dotted i and long descending g, then compressed n-a followed by a crossed t and the short u-r-e-s tail. The longer u-l-a-r-i-t-é sequence of singularités is absent. Intersections of the broad strikes do not supply extra letters.', 3,
       confidence='medium')
change('Canceled continuation of (88), whole numbered-parameter expression',
       r'j_1=2^{\unsure{\alpha}}3^{\unsure{\beta}}',
       r'J_1 = 2^{\alpha}3^{\beta}',
       r'\unsure{J_1|j_1}=2^{\unsure{\alpha}}3^{\unsure{\beta}}',
       'The parameter letter has a long stem and lower leftward hook with a black, overworked top continuous with the stem. A capital J is favored, but an overwritten dot or head of j cannot be separated. The lower 1, equality bars, bases 2 and 3 are visible; strikes partly cover the alpha-like and beta-like superscripts, whose doubts remain. The comparison changes C\'s preferred case without asserting that the alternative is impossible.', 3,
       confidence='medium', against_c=True, against_h=False,
       kind='misread symbol or index', sheet='symbols and indices')
change('Canceled continuation of (88), abbreviation before à la courbe',
       'correspondant', 'correspond.', 'correspond.',
       'The letter sequence ends with a tall d and a detached dot. No following a-n-t group is written. The abbreviated form agrees with H\'s quoted reading.', 3,
       against_c=True, against_h=False,
       kind='abbreviation expanded or spelling modernised',
       sheet='abbreviations expanded spelling modernised')
change('Canceled continuation of (88), automorphism abbreviation',
       "d'autom", "d'automorphisme", "d'autom",
       'After d and its apostrophe are the short a-u-t-o-m strokes; the low terminal m stops before the quotient formula. There is no following orphisme group.', 3,
       kind='abbreviation expanded or spelling modernised',
       sheet='abbreviations expanded spelling modernised')
change('Two canceled baselines after (88), including separately canceled interlinear word',
       r"\deleted{dans le dernier iso, \deleted{\unsure{lorsque}} la section à l'infini de $\widehat M_{D_1}$}",
       r'« … des sections $\infty$, … $\widehat{M}_{D_1}$ … »',
       canceled_line,
       'The lower two baselines read dans le dernier iso, then la section à l\'infini, continued as de and a complete hatted M_{D_1}. The main text is crossed by broad diagonals and a horizontal strike. The short lorsque candidate is above the line, with its own smaller cancellation and connector: its insertion status must be preserved inside the larger deletion. Its internal letters remain obscured. The crossed infini tail receives a certainty-only doubt. H\'s quoted summary omits readable words and turns the written word into an infinity sign; its surrounding editorial speculation is not treated as source text.', 4,
       confidence='medium', against_c=True, kind='insertion or placement',
       sheet='insertions put in wrong place', marked=True)
change('Main prose, opening clause', 'Je me rends compte',
       "J'y renonce, compte tenu", 'Je me rends compte',
       'The opening J is followed by a small e, then the two low humps of me. The next word has r-e-n-d-s with the looped d, and compte has the descending p and crossed t. There is no apostrophe-y, renonce, comma, or following tenu in this clause.', 5)
change('Main prose, word before comprendre', 'mieux', "d'abord", 'mieux',
       'The word has low m humps, a detached i dot, a short e/u group and a separate final crossing x. It has neither an initial d loop nor an apostrophe.', 6)
change('Main prose, complete first M_{1,1} formula',
       r'$\widehat M_{1,1}$', r'$M_{1,1}$', r'$\widehat M_{1,1}$',
       'Above the M is a distinct angular roof with both arms. The long descender of f in faudrait meets its left region, but the right arm and leftward extension are independent strokes. Both lower 1 digits and their comma are present. The hat is therefore retained, not inferred from the intended moduli space.', 7,
       kind='misread symbol or index', sheet='symbols and indices', consequential=True)
change('Main prose, complete parenthetical repetition phrase',
       r'(et $=$ de $M_{1,1}$)',
       r"(\add{\uncertain{c'est}} $=$ de $M_{1,1}$)",
       r'(et $=$ de $M_{1,1}$)',
       'Inside the opening parenthesis, e joins a tall t. There is no leading c or apostrophe and no insertion connector. Two separate horizontal bars follow, then de and an unhatted M with indices 1,1, ending at the closing parenthesis.', 8,
       marked=True)
change('Main prose, transition into the transcendental setting',
       'à commencer dans le', r'\uncertain{ce que je ne connais} dans la',
       'à commencer dans le',
       'The reduced à is an accented small loop, followed by the long low c-o-m-m-e-n-c-e-r sequence. The later dans has its tall d loop; the final article is le, ending in an open e rather than a closed a.', 8,
       marked=True)
change('Main prose, name of the setting', 'cadre transcendant',
       'catégorie transcendante', 'cadre transcendant',
       'Cadre is short, with a d ascender and no g descender. Transcendant ends after its final t-like angular stroke, without an additional e. The parenthesized analytique complexe follows.', 9)
change('Main prose, abbreviation after avec', 'évt.',
       r'\uncertain{éventuellement}', 'évt.',
       'A short accent is visible over e, followed by the small v, tall t and detached final dot. No remaining letters of éventuellement are written.', 10,
       kind='abbreviation expanded or spelling modernised',
       sheet='abbreviations expanded spelling modernised', marked=True)
change('Main prose, adjective after structure réelle', 'explicite',
       'explicitée', 'explicite',
       'After the descending p and tall l, the short final i-t-e group ends without a further e or a final acute accent. The following separate dash begins the i.e. clause.', 10)
change('Proposition heading, after the final n', r'\uline{Proposition}',
       r'\emph{Proposition.}', r'\uline{Proposition}',
       'The final n has its terminal return above the underline, then blank space precedes Si. No detached period follows the heading.', 11,
       kind='text not on the page', sheet='text not on page')
change('Proposition, relative placement of the two insertions',
       r'est \inserted{\unsure{géom.}} connexe \inserted{(fibre par fibre)}.',
       r'est connexe \add{(fibre par fibre)} \add{\uncertain{géom.}}.',
       r'est \inserted{\unsure{géom.}} connexe \inserted{(fibre par fibre)}.',
       'The short lower connector from the géom. candidate descends before connexe. The higher and longer connector from (fibre par fibre) ends after connexe. Thus the first insertion precedes connexe and the parenthesis follows it. The small word\'s g loop and compressed middle support géom., but an independent accent and final abbreviation dot are not secure, so its original doubt remains.', 11,
       confidence='medium', kind='insertion or placement',
       sheet='insertions put in wrong place', marked=True)
change('Second row of (89), accent on the nu index',
       r'\widehat\nu_\alpha', r'\nu_\alpha', r'\widehat\nu_\alpha',
       'A separate angular roof sits above the descending nu shape in the lower row, just as in the upper row. It is distinct from the exclamation mark to the upper left and from the small lower alpha.', 12,
       kind='misread symbol or index', sheet='symbols and indices', consequential=True)
change('Second row of (89), canceled accent above the right-hand M',
       r'M^{!}', r'M^{!}; \note{sous le second produit, un indice raturé}',
       r'\overset{\deleted{\unsure{\wedge}}}{M}^{!}',
       'Immediately above the second right-hand M is a compact black overwork crossing an angular trace. It is in the accent position, while the M body and raised upright-plus-dot remain live. A canceled hat is the preferred underlying candidate, but its exact original strokes are not recoverable. H notes a rature without reproducing this accent; no additional underlying letter or index is invented.', 12,
       confidence='medium', against_c=True, kind='deletion state',
       sheet='struck text', marked=True)
change('Lower-left pale foliation', r'\margin{71}', '', r'\margin{71}',
       'The separate pale number has an angled 7 with a short crossbar, followed by a long 1. It is not the black-ink author page number 35 at the head.', 13,
       kind='omission', sheet='omissions')

decisions = [dict(
    id='M1062', cote=147, scan=72, decision='undecided', reading=r'\unsure{géom.}',
    ink='The inserted group begins with a looped descending g and has a compressed e/o/m-like middle. The higher connector is too close to establish a separate acute accent, and the ending meets its own connector without a securely detached dot. The preferred abbreviation remains plausible, but not all its marks are independently identifiable.',
    crop='147_scan072_place11.png and (260, 1810, 1679, 2044)', confidence='medium')]

inventory = []
def item(kind, position, first, hand='his hand'):
    inventory.append(dict(scan=72, sheet_kind='text', hand=hand,
                          element=f'{len(inventory)+1:02}', kind=kind,
                          position=position, first_words_or_objects=first,
                          transcribed='yes'))

item('text', 'Top centre, black-ink foliation', '35')
item('text', 'First two main baselines', r'dans ce dernier iso, $P_0$ correspond')
item('text', 'Baseline above (88)', "D'autre part, on a")
item('display', 'Upper display, live left-hand part', r'(88) $\widehat M_{D_1}\unsure{=|\simeq}\widehat M_{G_1}\simeq\widehat M_{1,1}$')
item('deletion', 'Six-baseline continuation on the right of (88)', r'$\simeq(\mathbb P^1_{\mathbb Z}$, avec signatures')
item('deletion', 'Two baselines immediately below (88)', r'dans le dernier iso, ... la section à ... de $\widehat M_{D_1}$')
item('insertion', 'Above la section inside the larger canceled passage', r'\deleted{\unsure{lorsque}}')
item('deletion', 'Separate small strike on that interlinear insertion', r'\unsure{lorsque}')
item('text', 'Seven main prose baselines below the canceled material', "Je me rends compte qu'il me faudrait")
item('text', 'Separate underlined heading above the proposition', 'Notons déjà')
item('text', 'Proposition baseline', r'Underlined Proposition; Si $\dim M_G\geq2$')
item('insertion', 'Immediately above connexe, with connector before the word', r'\unsure{géom.}')
item('insertion', 'Higher at right, with connector after connexe', '(fibre par fibre)')
item('text', 'Introduction to the lower display', 'Dém. Écrivons')
item('display', 'Lower two-row product display with left brace', '(89) compactified and uncompactified product expressions')
item('deletion', 'Above the right-hand M in the second row of (89)', r'\unsure{\wedge}')
item('margin note', 'Extreme lower-left pale pencil foliation', '71', 'hand not confidently attributed')

doubts = [
    dict(place='First relation of the live line (88), crop02', reading=r'\unsure{=|\simeq}', alternatives=r'=; \simeq', confidence='medium', reason='The upper bar is only shallowly hooked, but is not perfectly straight. Equality remains preferred; the following clearer tilde and the compressed sign in (89) do not eliminate the alternative. This adds certainty information only against C.'),
    dict(place='Parameter letter in canceled (88), crop03', reading=r'\unsure{J_1|j_1}', alternatives=r'J_1; j_1', confidence='medium', reason='The head is black and overworked, continuous with a long stem and lower hook. Capital J is favored, but a lowercase dot or overwritten head cannot be separated.'),
    dict(place='Exponent of 2 in canceled (88), unindexed C doubt, crop03', reading=r'2^{\unsure{\alpha}}', alternatives=r'\alpha; unresolved superscript', confidence='medium', reason='The small alpha-like loop and right stroke merge with a diagonal cancellation. Its original doubt is retained.'),
    dict(place='Exponent of 3 in canceled (88), unindexed C doubt, crop03', reading=r'3^{\unsure{\beta}}', alternatives=r'\beta; unresolved superscript', confidence='medium', reason='An upright and two beta-like lobes are visible, but the lower part is crossed by the long diagonal. Its original doubt is retained.'),
    dict(place='Automorphism quotient in canceled (88), unindexed C doubt, crop03', reading=r'\unsure{\mathbb Z/4\mathbb Z|\mathbb Z/6\mathbb Z}', alternatives=r'\mathbb Z/4\mathbb Z; \mathbb Z/6\mathbb Z', confidence='low', reason='The two double-stroked Z forms and slash are identifiable, while the denominator digit is intersected by the broad cancellation. Its original 4/6 doubt remains; expected elliptic-curve automorphisms do not decide the ink.'),
    dict(place='Separately canceled interlinear word in the following passage, crop04', reading=r'\inserted{\deleted{\unsure{lorsque}}}', alternatives='lorsque; unresolved crossed word', confidence='low', reason='A tall first stem, low loops and a q-like descender survive, but the small horizontal strike covers the middle. The insertion and its separate deletion are both represented inside the larger deletion.'),
    dict(place='Tail of the canceled la section phrase, crop04', reading=r"\unsure{l'infini}", alternatives="l'infini; unresolved crossed tail", confidence='medium', reason='The initial l and apostrophe survive, but the following strokes meet the horizontal cancellation and several diagonals. This is an added certainty-only doubt on C\'s preferred word.'),
    dict(place='Proposition insertion, M1062, crop11', reading=r'\inserted{\unsure{géom.}}', alternatives='géom.; geom.; accent and abbreviation dot unresolved', confidence='medium', reason='The g and compressed middle are compatible with géom., but its separate accent and terminal dot cannot both be identified independently of the neighboring connectors.'),
    dict(place='Overworked accent above the lower right M in (89), crop12', reading=r'\overset{\deleted{\unsure{\wedge}}}{M}^{!}', alternatives='canceled hat; unresolved canceled accent', confidence='medium', reason='The overwork occupies the accent position and crosses an angular trace. A hat is a candidate, not a claimed fully recovered underlying sign; the live M and exclamation remain untouched.'),
]

notes = [
    'The opening continuation says that P_0 corresponds to the infinity section and P_1 to section 2 of the projective line over Z. The page supplies this as a manuscript assertion referring to a preceding isomorphism. That preceding construction was not inspected for this one-page task, and no independent verification of the section identification was attempted.',
    'The live portion of (88) relates the hatted spaces indexed by D_1, G_1 and (1,1); its first relation remains =/isomorphism uncertain from the ink. The author cancels a continuation describing a projective line with signatures 4 and 6 along section 0 and a parameter section J_1/j_1 expressed using doubtful powers of 2 and 3, with a doubtful Z/4Z versus Z/6Z automorphism group. The subsequent canceled sentence is also retained. These are canceled proposals, not silently restored live claims. The next live paragraph explicitly says that the author needs to understand the structure of hatted M_{1,1}, and also unhatted M_{1,1}, better in the transcendental setting. No value for the exponents or automorphism denominator was reconstructed mathematically.',
    'The manuscript then states that if dim M_G is at least 2, its boundary M_G^infinity is connected, with a doubtful géom. insertion before connexe and an inserted fibre par fibre parenthesis after it. It begins a proof with compactified and uncompactified product expressions in (89). Both nu indices have hats, both right-hand M factors have exclamation exponents, and the second right-hand M has a doubtful canceled hat. The page stops after these two rows; no completion or independent proof of the connectedness proposition was supplied.',
    'Diplomatic details include correspond., d\'autom, évt., the literal repetition sign = in the parenthesis, the lack of a period after Proposition, and the absence of an underline under Dém. The canceled continuation of (88) has an opening parenthesis for the projective-line description and another before correspond., but only one closing parenthesis is visible; no additional delimiter was inserted. H\'s editorial page label and speculation about D_1 are not manuscript text.',
    'The interlinear lorsque candidate has its own strike within a larger canceled two-line passage. In (89) the overwork lies above the second right-hand M; it is represented as a doubtful canceled wedge in the accent position, without inventing an earlier letter or index. The first prose M has a separate real hat despite the f descender from faudrait meeting it. The following parenthetical M is unhatted. Pencil foliation 71 remains separate from the author\'s ink page 35.',
    'Physical-line count: 28 writing units, comprising 23 main/formula baselines, 3 separate interlinear insertions (including the canceled lorsque), and the two isolated foliation numbers. The six-baseline canceled continuation of (88) shares its first baseline with the live formula, so that shared baseline is counted once; the two later canceled baselines and both (89) rows are included. Equation numbers are counted with their displays. The complete scan was viewed once for layout, both native halves once line by line, and all 13 saved crops were viewed. No OCR, external research, TeX compilation, or second reading was performed.'
]

check_events = [dict(statement_id=f'147-072-N{i}', date='2026-11-20 22:10:35 UTC',
                     who='reader_a; GPT-6 Astra Pro; inherited reasoning effort not separately exposed',
                     type='carried as background without fault found', outcome=outcome)
                for i, outcome in [
                    (1, 'The opening section correspondence was recorded as a manuscript assertion. No preceding page was read and no independent proof of the identification was made.'),
                    (2, 'The live relations and the canceled projective-line description were recorded with their source states and unresolved symbols. No elliptic-curve invariant, exponent, or automorphism computation was used to resolve the ink.'),
                    (3, 'The connectedness proposition and the product expressions beginning its proof were carried as manuscript background. No independent geometric proof, product-connectedness argument, or formal computation was performed.')]]

notation = [
    dict(sign='Shallow upper stroke above a lower bar in first (88) relation', reading=r'\unsure{=|\simeq}', evidence='The upper stroke is shallower than the following tilde, yet not fully straight. This is a local unresolved distinction.', scope='Scan072, first relation only; the later isomorphism signs retain their visible wavy upper strokes.'),
    dict(sign='Hat meeting a descender from the preceding text line', reading=r'\widehat M_{1,1}', evidence='The angular mark has two independent arms, although the descending f from faudrait touches its left region.', scope='Scan072, first M formula in the main prose; the next parenthetical M has no hat.'),
    dict(sign='Angular accent over each nu in the product factors', reading=r'\widehat\nu_\alpha', evidence='Both rows of (89) have a detached two-arm roof over the descending nu shape.', scope='Scan072, both product rows.'),
    dict(sign='Raised upright and detached dot after each factor M', reading='^!', evidence='The upright and dot are separately visible in both right-hand factors of (89).', scope='Scan072, both product rows; neither exponent is a prime.'),
    dict(sign='Black overwork in the lower factor accent position', reading=r'\overset{\deleted{\unsure{\wedge}}}{M}', evidence='An angular trace is crossed above the live M body. The underlying hat remains tentative.', scope='Scan072, second row of (89).'),
]

hand_log = [
    dict(habit='A letter descender from an upper line may meet a genuine accent on the line below without replacing it.', pages=[72], all_occurrences='Checked at faudrait above the first prose M; the independent arms establish its hat. The other hats in (88) and (89) are separate.', witness_misreadings='H omits the first prose M hat.'),
    dict(habit='Small angular hats and exclamation dots remain distinct from the nearby subscript letters.', pages=[72], all_occurrences='Both nu hats and both exclamation exponents in (89) were checked in the full two-row formula.', witness_misreadings='H omits the second nu hat and mentions a rature without reproducing the overworked accent above the second factor M.'),
    dict(habit='A compressed superscript or overwritten letter head is not safely resolved by familiar mathematical values.', pages=[72], all_occurrences='The J/j head, alpha-like and beta-like exponents, and the 4/6 denominator all retain doubt under cancellation.', witness_misreadings='C chooses lowercase j without a doubt; H gives uppercase J, alpha, beta, and denominator 4 without signaling the same ink uncertainty.'),
]

abbreviations = [
    dict(written='iso', expansion='isomorphisme'),
    dict(written='correspond.', expansion='correspondant'),
    dict(written="d'autom", expansion="d'automorphisme(s)"),
    dict(written='évt.', expansion='éventuellement'),
    dict(written='i.e.', expansion='id est'),
    dict(written=r'\unsure{géom.}', expansion='géométriquement, if the preferred reading is correct'),
    dict(written='Dém.', expansion='Démonstration'),
    dict(written='=', expansion='même, repetition sign retained literally in the parenthetical phrase'),
]

second_boxes = []
def blind(kind, box, reading):
    x0, y0, x1, y1 = box
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02}', kind=kind,
                             x0=x0, y0=y0, x1=x1, y1=y1, reading=reading))

blind('handwritten number', [843, 15, 924, 63], r'\mspage{35}')
blind('handwritten number', [315, 52, 1668, 243], r"dans ce dernier iso, $P_0$ correspond à la section à l'infini, et $P_1$ à la section $2$ de $\mathbb P^1_{\mathbb Z}$.")
blind('word disagreement', boxes['01'], "D'autre part, on a")
blind('doubtful formula', boxes['02'], r'(88)\qquad \widehat M_{D_1}\unsure{=|\simeq}\widehat M_{G_1}\simeq\widehat M_{1,1}')
blind('doubtful formula', boxes['03'], canceled88)
blind('struck passage', boxes['04'], canceled_line)
blind('word disagreement', boxes['05'], "Je me rends compte qu'il me faudrait")
blind('word disagreement', boxes['06'], 'mieux comprendre')
blind('handwritten number', [1460, 1070, 1585, 1185], r'$\widehat M_{1,1}$')
blind('word disagreement', boxes['08'], r'(et $=$ de $M_{1,1}$), à commencer dans le')
blind('word disagreement', boxes['09'], 'cadre transcendant (analytique complexe,')
blind('word disagreement', boxes['10'], 'avec évt. la structure réelle explicite -- i.e.')
blind('insertion', boxes['11'], r'''\uline{Notons déjà}

\uline{Proposition} Si $\dim M_G\geq2$, alors $M_G^\infty$ est \inserted{\unsure{géom.}} connexe \inserted{(fibre par fibre)}.''')
blind('doubtful formula', boxes['12'], 'Dém. Écrivons\n\\[\n'+eq89+'\n\\]')
blind('handwritten number', boxes['13'], r'\margin{71}')

report = dict(scan=72, reader='reader_a', physical_lines_read=28,
              changes=changes, decisions=decisions, inventory=inventory,
              doubts=doubts, notes=notes, check_events=check_events,
              notation=notation, hand_log=hand_log, abbreviations=abbreviations,
              second_boxes=second_boxes,
              unresolved=[
                  'First live (88) relation: equality preferred, isomorphism sign not excluded.',
                  'Canceled (88): capital J preferred over j, both exponent letters still doubtful, and quotient denominator 4/6 unresolved.',
                  'Canceled interlinear lorsque and the crossed l\'infini tail remain tentative.',
                  'M1062 géom. remains unresolved, especially its accent and final dot.',
                  'The canceled lower-product accent is a hat candidate, not a fully recovered underlying glyph.'
              ],
              witness_comparison='C is much closer to the live prose, retains the substantial canceled material and correct first prose hat, and gives both nu hats. Its expanded correspondant should be abbreviated correspond.; it omits the insertion status of the canceled lorsque and the crossed accent above the second factor M. C\'s unmarked lowercase j is less favored than capital J, but the head remains unresolved. H preserves correspond. in its editorial quotation and favors capital J, while misreading most of the opening live prose, expanding évt. and d\'autom, omitting the first prose M hat and second nu hat, moving géom., leaving the beginning of the canceled continuation live, and omitting pencil foliation 71. The first (88) relation is an unresolved comparison, not a demonstrated H error. Macro-only changes, editorial apparatus, and added certainty-only doubts are excluded from the substantive change count.')

assert len(changes) == 21
assert [d['id'] for d in decisions] == [row['id'] for row in csv.DictReader((packet/'marks.tsv').open(), delimiter='\t')]
assert all(c['against_C'] or c['against_H'] for c in changes)
assert all((work/'crops'/c['crop']).is_file() for c in changes)
assert all(c['final'] in proposed for c in changes)
assert all(b['reading'] in proposed for b in second_boxes)
assert all(0 <= c['box'][0] < c['box'][2] <= 1691 and 0 <= c['box'][1] < c['box'][3] <= 2359 for c in changes)
assert all(0 <= b['x0'] < b['x1'] <= 1691 and 0 <= b['y0'] < b['y1'] <= 2359 for b in second_boxes)
group_text = re.sub(r'\\[{}]', '', proposed)
group_depth = 0
for char in group_text:
    if char == '{':
        group_depth += 1
    elif char == '}':
        group_depth -= 1
        assert group_depth >= 0
assert group_depth == 0
assert proposed.count('$') % 2 == 0
assert proposed.count('\\inserted{') == 3
assert proposed.count('\\deleted{') == 4
assert proposed.count('\\begin{aligned}') == proposed.count('\\end{aligned}') == 1
assert proposed.count('\\[') == proposed.count('\\]') == 2
assert set(re.findall(r'\\([A-Za-z]+)', proposed)) <= {
    'scanpage','mspage','mathbb','qquad','widehat','unsure','simeq','deleted','bigl',
    'text','alpha','beta','bigr','inserted','ldots','uline','dim','geq','infty','left',
    'begin','prod','in','nu','overset','wedge','end','right','margin'
}

(out/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(dict(changes=len(changes), against_C=sum(c['against_C'] for c in changes),
                      against_H=sum(c['against_H'] for c in changes), decisions=len(decisions),
                      crops=len(boxes), second_boxes=len(second_boxes), inventory=len(inventory),
                      physical_lines=28, doubts=len(doubts)), ensure_ascii=False))
