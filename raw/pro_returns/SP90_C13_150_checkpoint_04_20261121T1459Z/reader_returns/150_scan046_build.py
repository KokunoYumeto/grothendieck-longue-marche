from pathlib import Path
import json, re

ROOT = Path('/workspace/scratch/481648fc487b')
WORK = ROOT / 'SP90_C13_150_work'
PACKET = ROOT / 'reader_packets/150_scan046'
OUT = WORK / 'reader_returns'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
T = (OUT / '150_scan046.tex').read_text()

crop_names = '''opening_insert map_opening margin_e label_e label_f cancel_non first_ie_map bord_dash tq_preced cancel_sigma_i final_insert codim du_bord alors d_fullflag bord_p cofinal en_forment bord_de star_upper star_lower vertical_note lower_case en_plus insert_fibrations lower_map fibre_reunion est_reunion donne strict_pair final_phrase final_product label_g folio45 margin_e_tail crowded_tails opening_stop label_e_end label_f_end'''.split()
crops = {}
for n in crop_names:
    m = json.loads((WORK / 'crops' / f'150_scan046_{n}.json').read_text())
    crops[n] = {'file': f'150_scan046_{n}.jpg', 'box': m['box']}

D = dict(scan=46, reader='reader_c', line_count=52,
         crop_place_count=35, crop_image_count=39,
         changes=[], marks=[], inventory=[], doubts=[], notes=[],
         check_events=[], notation=[], abbreviations=[], hand_log=[], second_boxes=[])

def change(place, c, h, final, evidence, crop, kind, error_kind,
           change_C=False, change_H=False, confidence='high', consequential=''):
    D['changes'].append(dict(place=place, C=c, H=h, final=final,
        evidence=evidence, crop=crops[crop]['file'], box=crops[crop]['box'],
        confidence=confidence, kind=kind, error_kind=error_kind,
        marked_in_H=(r'\uncertain' in h or r'\ill' in h),
        change_C=change_C, change_H=change_H, consequential=consequential))

def mark(m, context, decision, reading, evidence, crop, confidence='low'):
    D['marks'].append(dict(mark=m, context=context, decision=decision,
        reading=reading, evidence=evidence, crop=crops[crop]['file'],
        box=crops[crop]['box'], confidence=confidence))

def box(n, kind, coords, reading, reason):
    D['second_boxes'].append(dict(box=f'b{n:02}', kind=kind, coords=coords,
                                 reading=reading, reason=reason))

# Opening and upper main paragraph.
change('opening: apparent additions are marginal continuation',
       'dans le cas équisingulier',
       r"dans le cas \add{\uncertain{d'un espace}} \add{\uncertain{stratifié}} équisingulier",
       'dans le cas équisingulier',
       "The diagonal words above the line are est une and segment initial de, continuing Cela implique ...; their direction and uninterrupted marginal syntax are established by margin_e plus margin_e_tail. There are no independent d’un espace / stratifié insertions in the main opening.",
       'opening_insert', 'text not on the page', 'text not on page', change_H=True)
change('opening: no comma before on', 'équisingulier on', 'équisingulier, on',
       'équisingulier on',
       'The gap after the ending -lier is blank. The next short horizontal stroke belongs to the flattened o of on, followed by its low n.',
       'opening_stop', 'text not on the page', 'other', change_H=True)
change('first main display: headless shaft',
       r'\Sigma_{ij}\longrightarrow\Sigma_i', r'\Sigma_{ij}\longrightarrow\Sigma_i',
       r'\Sigma_{ij}-\Sigma_i',
       'The shaft is one blunt horizontal stroke. Its thick rounded right tip has no independent returning arrowhead. The separate marginal and lower main arrows have visible heads, so their form is not imported here.',
       'map_opening', 'misread symbol or index', 'symbols and indices', True, True,
       consequential='Preserves the drawn headless connecting stroke without supplying a map arrow.')
change('apparent second interlinear map belongs to the margin',
       r'\Sigma_{ij}\longrightarrow\Sigma_i',
       r'\add{$\Sigma_{d\'}\to\Sigma_d$ \ill{} \ill{}}'.replace("d\\'", "d'"),
       r'\margin{[Cela implique que $\Sigma_d\longrightarrow\Sigma_{d\'}$ est une fibration, si $d\'\subset d$ est un \uline{segment initial} de $d$.]}'.replace("d\\'", "d'"),
       'The alleged interlinear formula is the map in the diagonal Cela note. Its source is d, its target d-prime, and the following est une continues above/right. It is not a second main-line formula or a canceled addition.',
       'margin_e', 'insertion or placement', 'insertion placement', change_H=True)
change('before non singulières: phantom cancellation',
       r'strates \deleted{\illegible{1}} non-singulières',
       r'strates \struck{\ill{}} non singulières',
       'strates non singulières',
       'The supposed canceled fragment is not an independent crossed word. The observed low and upright strokes belong to the live words non singulières; no separate cancellation line or underlying additional token is recoverable.',
       'cancel_non', 'text not on the page', 'text not on page', True, True)
change('non singulières: word gap', 'non-singulières', 'non singulières',
       'non singulières',
       'There is a gap between the low final n and the initial s; no detached hyphen crosses that gap.',
       'cancel_non', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', change_C=True)
change('stop after non singulières', 'non-singulières on', 'non singulières, on',
       r'non singulières\unsure{,|.} on',
       'A separate dark low stroke follows the final s, near source x1015,y530. It is textual punctuation, but its short tail does not decisively distinguish a comma from a point. H’s comma remains an admissible alternative, so the new doubt is not charged to H.',
       'cancel_non', 'omission', 'omissions', change_C=True, confidence='medium')
change('first j<i: canceled closing parenthesis',
       r'(\deleted{$j<i$}', r'\struck{($j<i$)}',
       r'\deleted{($j<i$)}',
       'A separate closing curve after i is crossed by the same horizontal cancellation as j<i. The opening group also meets that crossing. The later live close after tq-précédemment is preserved, without balancing it editorially.',
       'tq_preced', 'deletion state (struck given live or live given struck)', 'struck text',
       change_C=True, confidence='medium')
change('first j<i: tq-précédemment',
       r'\unsure{tq-précédemment|toujours distinctes}', r'\uncertain{toujours distinctes}',
       'tq-précédemment',
       'There are a t upright/low bar and a separate q descender, followed by a short hyphen, a descending p, and the two accent strokes of précédemment. The source has the short written tq form, not the longer toujours distinctes.',
       'tq_preced', 'misread word', 'words', True, True, 'medium')
change('second j<i: phantom i elt final insertion',
       r"$\Sigma_{ji}$ ($j<i$ \inserted{\unsure{$i$ elt final}})",
       r'$\Sigma_{ji}$ ($j<i$)',
       r'$\Sigma_{ji}$ ($j<i$)',
       'The alleged i ... final is made from the final i_n) of the diagonal marginal Drap factor, the main-line f of forment, and the diagonal où / Drap explanation below. The completion crowded_tails exposes those separate writing directions. No independent insertion i elt final is on the page.',
       'crowded_tails', 'text not on the page', 'text not on page', change_C=True)
change('main verb after second j<i',
       r'\unsure{forment|définissent}', r'\uncertain{forment}',
       'forment',
       'The initial tall looped f and low following run belong to the main baseline; the marginal factor crosses nearby but does not turn the word into définissent. The first C alternative is supported. H’s same word is not counted as a correction of certainty alone.',
       'crowded_tails', 'misread word', 'words', change_C=True, confidence='medium')
change('raised codimension phrase: first word',
       r'\unsure{les}', r'\uncertain{le long de}',
       r'\unsure{les}',
       'The first small group has one looped l followed by a short low ending. It is compatible with les but remains compressed. There is no separate long word with its own l and g descender; H’s le long de cannot occupy this single group. The retained C doubt is not a correction to C.',
       'codim', 'misread word', 'words', change_H=True, confidence='low')
change('raised codimension phrase: abbreviated objt candidate',
       r'\illegible{1}', r'\ill{}', r'\unsure{objt}',
       'The small word has an o-like loop, a b upright, a descending j-like turn and a t-like final upright/crossbar. These permit the narrow written candidate objt, without supplying the expanded objets. The precise abbreviated form remains doubtful.',
       'codim', r'readable ink left as \ill{}', 'readable ink left as illegible', True, True, 'low')
change('raised codimension phrase: final d-apostrophe',
       r"\unsure{d'}", r'\uncertain{codim.}\ 1', "codim $1$ d'",
       'After the single vertical 1 is a looped d with an upright and one detached apostrophe at its upper right. The written d’ is retained as a contraction, not completed to a word.',
       'codim', 'misread word', 'words', True, True, 'medium')
change('raised codimension phrase: no stop after codim',
       'codim $1$', r'\uncertain{codim.}\ 1', 'codim $1$',
       'The low final m run is followed by white space and the upright 1. There is no detached abbreviation point.',
       'codim', 'text not on the page', 'other', change_H=True)
change('raised codimension phrase: leader, not parentheses',
       r"(\inserted{\unsure{les} \illegible{1} \unsure{de} codim $1$ \unsure{d'}})",
       r'\add{\uncertain{le long de} \ill{} \uncertain{codim.}\ 1}',
       r"\inserted{\unsure{les} \unsure{objt} \unsure{de|e} codim $1$ d'}",
       'The long line runs beneath the raised phrase and curves upward at its right end. It is an insertion leader; there is no independent opening parenthesis before les and no independent paired close. This row records placement/punctuation, not an additional resolution of its doubtful words.',
       'codim', 'insertion or placement', 'insertion placement', change_C=True, confidence='medium')
change('du bord par: omitted live text and canceled Sigma',
       r'du \deleted{$\unsure{\Sigma_*}$} bord par des variétés à bord',
       'des variétés à bord',
       r'du \deleted{$\unsure{\Sigma_*}$} bord par des variétés à bord',
       'The main baseline has du, a separately canceled Sigma-like symbol with small star-like index, then bord par des. The canceled symbol remains doubtful because the crossing masks part of its outline. H omits this whole intermediate sequence.',
       'du_bord', 'omission', 'omissions', change_H=True, confidence='medium')
change('Alors after the boundary sentence', 'Alors', r'\uncertain{plus généralement}',
       'Alors',
       'One large capital A is followed by a short low lors run; there are no two long words beginning with p and g.',
       'alors', 'misread word', 'words', change_H=True, confidence='medium')
change('full-flag Sigma index: two strokes and no comma',
       r'\Sigma_d=\Sigma_{i_1,--i_n}', r'\Sigma_d=\Sigma_{i_1\cdots i_n}',
       r'\Sigma_d=\Sigma_{i_1-\, -i_n}',
       'The right index is i_1, then two separate short horizontal strokes, then i_n. The first i has a detached dot and the digit 1 is a straight lower stroke. There is no comma between 1 and the two continuation strokes.',
       'd_fullflag', 'misread symbol or index', 'symbols and indices', True, True)
change('fragment after bord: crossed, interior unresolved',
       r'bord \unsure{p.} et les', 'bord et les',
       r'bord \deleted{\unsure{p.}} et les',
       'A descending p-like stroke and a separate point remain, but a heavy horizontal overtrace/cancellation masks the upper interior. The crossing state is visible; the existing p. reading is not resolved.',
       'bord_p', 'deletion state (struck given live or live given struck)', 'struck text', True, True, 'medium')
change('cofinal extension relation: one extra lower bar',
       r"d'\supsetneqq d", r"d'\supsetneq d", r"d'\supsetneq d",
       'The curved superset has its own lower stroke and only one additional lower horizontal bar, crossed by an oblique slash. There is not a second extra lower bar. This is the narrower supsetneq glyph.',
       'cofinal', 'misread symbol or index', 'symbols and indices', change_C=True)
change('canceled en forment retained as candidate',
       r'\deleted{\unsure{en forment}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{en forment}}',
       'An initial e loop, a low n-like turn and the tall f are recoverable under the cancellation. The interiors of the remaining letters merge into the strike, so the strict C doubt remains. H records only illegibility at this place.',
       'en_forment', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='low')
change('canceled de before dotted Sigma_d',
       r'\deleted{de} $\dot\Sigma_d$', r'bord $\dot\Sigma_d$',
       r'\deleted{de} $\dot\Sigma_d$',
       'A looped d and low e are crossed out immediately before the Sigma with its distinct upper dot. H omits the canceled word.',
       'bord_de', 'omission', 'omissions', change_H=True)

# Upper diagonal labels and explanatory note.
change('condition e label: opening parenthesis', 'condition e)', 'condition (e)',
       'condition (e)', 'Both small parentheses are independently visible around the e; they are not a circle.',
       'label_e', 'omission', 'omissions', change_C=True)
change('condition e quotation strokes and absence of stop',
       "``équisingularité''", '« équisingularité ».', "``équisingularité''",
       'The opening is two upright quote strokes. The completion shows a compact double-lobed closing mark, with no separate terminal point; it is not a pair of drawn guillemets.',
       'label_e_end', 'misread symbol or index', 'other', change_H=True, confidence='medium')
change('square brackets enclosing Cela note',
       r'\margin{Cela implique que', r'Cela implique que',
       r'\margin{[Cela implique que $\Sigma_d\longrightarrow\Sigma_{d\'}$ est une fibration, si $d\'\subset d$ est un \uline{segment initial} de $d$.]}'.replace("d\\'", "d'"),
       'An outer opening bracket precedes Cela; a separate closing bracket with horizontal caps follows d. The completion confirms the upper continuation rather than supplying words to close the bracket.',
       'margin_e', 'omission', 'omissions', True, True)
change('Cela note: recoverable prose',
       r"est une fibration, si $d'\subset d$ est un \uline{segment initial} de $d$.",
       r"\ill{} \ill{} fibrations, si $d\subset d'$ \ill{}",
       r"est une fibration, si $d'\subset d$ est un \uline{segment initial} de $d$.",
       'The upper-right completion reads est une. The next diagonal line has singular fibration and a comma; the following est un segment initial de and final d. are readable. segment initial has a separate underline. This records prose lost to H’s illegibilities and plural form; the set relation itself is separately collated.',
       'margin_e_tail', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='medium')
change('Cela note map: target d-prime',
       r"\Sigma_d\longrightarrow\Sigma_{d'}", r'\Sigma_d\to\Sigma_{\ill{}}',
       r"\Sigma_d\longrightarrow\Sigma_{d'}",
       'The source has unprimed d. The target has a d loop/upright and a separate short prime. The connecting line has a definite right arrowhead.',
       'margin_e', 'misread symbol or index', 'symbols and indices', change_H=True)
change('Cela note: d-prime subset d', r"d'\subset d", r"d\subset d'", r"d'\subset d",
       'The separate prime is on the left d before the subset sign; the right d is unprimed. The direction is read from these strokes, not inferred from the fibration claim.',
       'margin_e', 'misread symbol or index', 'symbols and indices', change_H=True,
       consequential='Restores the written direction of the initial-segment hypothesis.')
change('condition f label: capital C', 'Condition', 'condition (f)',
       'Condition (f)', 'The initial C of this label is large and open, unlike the small c in the e label.',
       'label_f', 'misread word', 'words', change_H=True)
change('condition f label: opening parenthesis', 'Condition f)', 'condition (f)',
       'Condition (f)', 'A separate opening parenthesis stands to the left of f, and a separate closing parenthesis to its right.',
       'label_f', 'omission', 'omissions', change_C=True)
change('condition f label: no hyphen', "non-singularité''", 'non-singularité »',
       r"non singularité\unsure{''}",
       'The space between non and singularité contains no detached hyphen. The ending is entangled with the large main Sigma_i, so its closing quote is kept doubtful rather than certified from the main symbol.',
       'label_f', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', True, True, 'medium')
change('condition f label: opening quotation mark form', "``non-singularité''", '« non-singularité »',
       r"``non singularité\unsure{''}",
       'Two upright opening quote strokes precede non. No drawn opening guillemet is present. The closing form remains narrowly doubtful because of the main Sigma_i crossing; that new uncertainty is not separately counted.',
       'label_f_end', 'misread symbol or index', 'other', change_H=True, confidence='medium')

# Starred note, its extra raised factor, and the vertical alternative expression.
change('star call and curved attachment', r'\margin{$*$ cet ens',
       r"$d$ cofinal dans $d'$)*", r'\margin{$*$}du',
       'The main star is at the left of the du/bord line, with a long curved arrow leading down-left to the marginal star. It is not a star after the later cofinal parenthesis. C gives the note’s star but omits its separate main call.',
       'star_upper', 'insertion or placement', 'insertion placement', True, True)
change('star note opening: cet ens d’indices', "cet ens d'indices", r"et \uncertain{l'ensemble}",
       "cet ens d'indices",
       'The first group has c-e-t rather than et; ens is a short low three-letter abbreviation, followed by d’indices with a distinct apostrophe and the tall d stem. The manuscript does not write the expanded l’ensemble.',
       'star_upper', 'misread word', 'words', change_H=True, confidence='medium')
change('star note: au sous-ens de', 'au sous-ens de', r"s'identifie \uncertain{à} \ill{} \ill{}",
       "s'identifie au sous-ens de",
       'The note continues with au, a low sous followed by a detached hyphen and ens, then de. The shortened sous-ens is preserved without expansion.',
       'star_upper', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='medium')
change('star product: raised extra factor at the later junction',
       r'\inserted{\widehat{\operatorname{Drap}}(I_{\cdot<i_1})\times}',
       r'\widehat{\mathrm{Drap}}(I_{<i_1})\times',
       r'& \inserted{\widehat{\operatorname{Drap}}(I_{\cdot<i_1})\times}',
       'The extra hatted Drap factor is written above the product. Its short leader heads down/right near the closing parenthesis of the i_2<dot<i_3 factor, not toward the beginning. The array preserves that position; the intended algebraic ordering is not supplied.',
       'star_upper', 'insertion or placement', 'insertion placement', True, True, 'medium')
change('raised marginal factor: dot before less-than',
       r'I_{\cdot<i_1}', r'I_{<i_1}', r'I_{\cdot<i_1}',
       'A distinct central dot appears between I’s subscript start and the less-than sign. The endpoint has i and the digit 1.',
       'star_upper', 'misread symbol or index', 'symbols and indices', change_H=True)
change('star product: explicit i_2 to i_3 factor',
       r'\widehat{\operatorname{Drap}}(I_{i_2<\cdot<i_3})',
       r'\widehat{\mathrm{Drap}}(I_{i_1<\cdot<i_2})\times\cdots\times',
       r'\widehat{\operatorname{Drap}}(I_{i_2<\cdot<i_3})',
       'The second main factor has its own hat, Drap, parenthesized I, and the endpoint digits 2 and 3. H’s product skips this independently written factor.',
       'star_upper', 'omission', 'omissions', change_H=True, confidence='medium')
change('star product: two continuation strokes', r'\times\ldots\times', r'\times\cdots\times',
       r'\times-\, -\times',
       'Between the two multiplication crosses are exactly two short horizontal continuation strokes, not three points.',
       'star_upper', 'misread symbol or index', 'symbols and indices', True, True)
change('star product: partially readable final factor',
       r'\unsure{\widehat{\operatorname{Drap}}(I_{i_{n-1}<\cdot<i_n})}',
       r'\widehat{\mathrm{Drap}}(\ill{})',
       r'\widehat{\operatorname{Drap}}(I_{\unsure{i_{n-1}<\cdot<}i_n})',
       'The completion exposes the hat, Drap, I, final i_n and close. The earlier endpoint/relation is crossed by the tall main-line f, so i_{n-1}<dot< remains a narrow unresolved candidate. This narrows C’s uncertainty without counting it as a resolution; H loses recoverable outer symbols and final endpoint.',
       'crowded_tails', 'misread symbol or index', 'symbols and indices', change_H=True, confidence='low')
change('star note: readable explanation around the strict doubts',
       r"où $\widehat{\operatorname{Drap}}$ désigne les drapeaux, \unsure{y.c. vides}, privé du \deleted{\unsure{drapeau}} pt unique \unsure{correspondant aux} drapeaux vides",
       r"où $\widehat{\mathrm{Drap}}$ désigne les \ill{} \ill{} \ill{} \ill{} (\uncertain{y compris} \ill{} \ill{}) \ldots",
       r"où $\widehat{\operatorname{Drap}}$ désigne les drapeaux, \unsure{y.c. vides}, privé du \deleted{\unsure{drapeau}} pt unique \unsure{correspondant aux} drapeaux vides",
       'The diagonal baselines give désigne les drapeaux, privé du, pt unique and the later drapeaux vides. The canceled drapeau and compressed correspondant aux remain strict doubts. The broad H illegibility sequence is replaced only to the extent shown by these strokes; it is not treated as a mathematical reconstruction.',
       'star_lower', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='medium')
change('star note: short y.c. form, not expansion',
       r'\unsure{y.c. vides}', r'\uncertain{y compris}', r'\unsure{y.c. vides}',
       'The small group is abbreviated: the y/c-like strokes and stops do not supply the full letters compris. The abbreviation plus vides remains doubtful; no expanded alternative is placed in the transcription.',
       'star_upper', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', change_H=True, confidence='low')
change('star note: cancellation before pt unique',
       r'\deleted{\unsure{drapeau}} pt unique', r'\ill{} \ill{}) \ldots',
       r'\deleted{\unsure{drapeau}} pt unique',
       'The word before pt unique is explicitly crossed. Initial d and the p descender survive, but several interiors are hidden, so the C candidate drapeau remains unresolved. H does not preserve this cancellation.',
       'star_lower', 'omission', 'struck text', change_H=True, confidence='low')
change('star tuple: one dash, one close, no terminal stop',
       r"(pour $d'=d=(i_1,\ldots i_n)$).", '[absent]',
       r"(pour $d'=d=(i_1,-i_n)$",
       'The tuple reads d-prime=d=(i_1, then one continuous headless dash, then i_n and one closing parenthesis. No second closing parenthesis or terminal stop is visible. The prose opening before pour remains unmatched.',
       'star_lower', 'misread symbol or index', 'symbols and indices', True, True,
       consequential='Preserves the source’s written continuation and unbalanced parenthesis rather than completing the tuple prose.')
change('vertical marginal note: aussi', "il s'identifie aussi à", r"il s'identifie \uncertain{à}",
       "il s'identifie aussi à",
       'Between s’identifie and the final à is a separate short aussi run with its dot; H omits it.',
       'vertical_note', 'omission', 'omissions', change_H=True, confidence='medium')
change('vertical marginal formula: coproduct shape',
       r'I_{<i_1}\coprod I_{i_1<\cdot<i_2}',
       r'I_{<i_1}\amalg I_{i_1<\cdot<i_2}',
       r'I_{<i_1}\coprod I_{i_1<\cdot<i_2}',
       'Each separator has two upright strokes rising from a horizontal lower bar with outward extensions, the written coproduct form. This row concerns the literal glyph choice, not a claimed difference in mathematical meaning.',
       'vertical_note', 'misread symbol or index', 'symbols and indices', change_H=True)
change('vertical marginal formula: continuation across two lines',
       r'\coprod\ldots\coprod', r'\amalg\cdots\amalg',
       r'\coprod -\,\cdot\,-\\\qquad\cdot\,-\coprod',
       'After the second coproduct on the first written line are three small marks: a short stroke, a point and a short stroke. The next written line begins with a point and a longer headless stroke before the next coproduct. Both groups and the line break are retained, rather than collapsing them to one conventional ellipsis.',
       'vertical_note', 'misread symbol or index', 'symbols and indices', True, True)

# Lower paragraph and canceled ending.
change('lower combined case: no second hyphen',
       'équisingulier-non-singulier', 'équisingulier-non singulier',
       'équisingulier-non singulier',
       'There is a detached hyphen after équisingulier, but the gap between non and singulier has no hyphen.',
       'lower_case', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling', change_C=True)
change('lower hypothesis: baseline en plus de',
       'suppose, en plus de e) et f)',
       r'\uncertain{suppose} \add{\uncertain{de plus}} (e) et (f)',
       'suppose, en plus de e) et f)',
       'The words en plus de are written on the main baseline, with en before the descending p of plus and de after it. The raised material below is fibrations, not de plus. The comma after suppose belongs to that baseline.',
       'en_plus', 'misread word', 'words', change_H=True, confidence='medium')
change('lower hypothesis: e) and f) have no opening parentheses',
       'e) et f)', '(e) et (f)', 'e) et f)',
       'Both inline reference letters have closing curves to their right and no separate opening curves to their left. This differs from the genuine paired parentheses in the margin labels (e) and (f).',
       'en_plus', 'text not on the page', 'other', change_H=True)
change('lower le: canceled réunion candidate',
       r'\deleted{\unsure{réunion}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{réunion}}',
       'Several low loops and an accent survive beneath a straight cancellation. They support the retained réunion candidate but do not expose every letter; the strict C doubt is kept. H provides no reading.',
       'fibre_reunion', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='low')
change('lower est: canceled formé des',
       r'\deleted{formé des}', r'\struck{\ill{}}', r'\deleted{formé des}',
       'The tall looped f, low ormé run with accent, and a separate d/e/s group remain recoverable under the line. The source has two canceled words rather than wholly unreadable ink.',
       'est_reunion', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='medium')
change('raised réunion was struck again',
       r'\inserted{\unsure{réunion}}', r'\add{\uncertain{réunion}}',
       r'\inserted{\deleted{\unsure{réunion}}}',
       'The raised word has a straight horizontal cancellation through its own letters. A different curved leader runs below it toward the main line. The inner word remains doubtful; the later cancellation is independently visible.',
       'est_reunion', 'deletion state (struck given live or live given struck)', 'struck text', True, True)
change('lower d: canceled donne candidate',
       r'\deleted{\unsure{donne}}', r'\struck{\ill{}}',
       r'\deleted{\unsure{donne}}',
       'An initial d-like upright and a low following run survive under the cancellation. The central letters merge into the strike and do not justify clearing C’s doubt. H gives only illegibility.',
       'donne', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='low')
change('strict pair: round delimiters', '$(i,j)$', r'$\lbrace i,j\rbrace$', '$(i,j)$',
       'The live group is bounded by single smooth round curves, without the inward knees of braces. The comma between i and the long j descender is separate.',
       'strict_pair', 'misread symbol or index', 'symbols and indices', change_H=True)
change('canceled Sigma before strict pair',
       r'\deleted{$\unsure{\Sigma}$}', r'$\lbrace i,j\rbrace$',
       r'\deleted{$\unsure{\Sigma}$} $(i,j)$',
       'A separately canceled Sigma-like sign precedes the live round pair. Its lower zigzag remains while the top is covered; the strict Sigma doubt is retained. H omits the sign.',
       'strict_pair', 'omission', 'struck text', change_H=True, confidence='medium')
change('final canceled phrase: retained par l’ancien candidate',
       r"\unsure{élément par l'ancien produit}", r'élément ; \ill{} produit',
       r"\unsure{élément par l'ancien produit}",
       'The run after élément has a descending p-like start, then a clearly separate l and apostrophe before the later produit. The crossed interiors do not identify every letter of par l’ancien, so the whole C doubt is retained. No isolated semicolon is identified at H’s position.',
       'final_phrase', 'misread word', 'words', change_H=True, confidence='low')
change('final canceled product: two hats',
       r'\widehat{\operatorname{Drap}}(I_{i<\cdot<j})\times\widehat{\operatorname{Drap}}(I_{>j})',
       r'\mathrm{Drap}(I_{i<\cdot<j})\times\mathrm{Drap}(I_{>j})',
       r'\underbrace{\deleted{\widehat{\operatorname{Drap}}}}',
       'Each Drap has its own detached angular hat above it, unaffected by the horizontal cancellation. H transcribes both factors without hats. The whole canceled product is supplied in the audit box.',
       'final_product', 'misread symbol or index', 'symbols and indices', change_H=True)
change('final product: both underbraces and caption placement',
       r'\margin{\unsure{drapeaux} \unsure{\deleted{côt. vide}}\qquad\unsure{drapeaux}\unsure{\deleted{stricts}}}',
       '[absent]',
       r'\underbrace{\deleted{\widehat{\operatorname{Drap}}}}_{\substack{\text{\unsure{\deleted{drapeaux}|drapeaux}}\\\text{\unsure{\deleted{côt. vide}|côt. vide}}}}',
       'The first underbrace spans the first hatted Drap only and stops before its opening parenthesis; the second spans the second factor. The captions lie on two small baselines below these braces, not in an independent margin note. H mentions captions editorially but supplies no brace structure in its transcription. Their cancellation reach is kept uncertain, not assumed from the main strike.',
       'final_product', 'drawing or diagram', 'drawings and diagrams', True, True, 'medium')
change('first bottom caption: vide candidate, not stricts',
       r'\unsure{\deleted{côt. vide}}', r'\uncertain{cot.\ stricts}',
       r'\unsure{\deleted{côt. vide}|côt. vide}',
       'The lower first caption has a v-shaped start followed by i/d/e-like strokes, not a long stricts sequence. Its bottom is at the dark scan edge and the accent/abbreviation interior is not secure; the existing candidate and explicit cancellation-state doubt remain.',
       'final_product', 'misread word', 'words', change_H=True, confidence='low')
change('second bottom caption: stricts candidate',
       r'\unsure{\deleted{stricts}}', r'drapeaux \ill{}',
       r'\unsure{\deleted{stricts}|stricts}',
       'The second lower caption has the short s/t run, an i dot and final t/s-like turns compatible with stricts. Crossing and the dark lower edge prevent a full letter-by-letter resolution, so the candidate and state doubt remain.',
       'final_product', r'readable ink left as \ill{}', 'readable ink left as illegible', change_H=True, confidence='low')
change('low terminal mark after canceled product',
       r'\widehat{\operatorname{Drap}}(I_{>j})$}', ',', r'\unsure{,|)}',
       'A separate low curved mark follows the final factor’s closing parenthesis. Its placement favors a comma, but its longer curve permits a second closing parenthesis. It is retained narrowly; H’s comma remains an alternative and is not counted as corrected.',
       'final_product', 'omission', 'omissions', change_C=True, confidence='medium')
change('Condition g marginal label', r'\margin{Condition g)}', '[absent]',
       r'\margin{Condition g)}',
       'The lower left margin plainly has capital Condition followed by g and a closing parenthesis. There is no opening parenthesis before g. H omits this marginal label.',
       'label_g', 'omission', 'omissions', change_H=True)
change('thin lower-left foliation 45', r'\mspage{45}', '[absent]', r'\margin{45}',
       'The digits 4 and 5 are in thin pale ink, distinct from the heavy main handwriting. The number is transcribed as marginal foliation with hand attribution uncertain, not certified as his own page number. H’s editorial page note is not manuscript text and does not transcribe this visible number.',
       'folio45', 'other', 'other', True, True)

# Every original C uncertainty/illegibility, including repeated and nested marks.
mark(r'\illegible{1}', r'strates \deleted{\illegible{1}} non-singulières', 'other', '',
     'No independent canceled fragment exists here. The alleged ink belongs to the live non singulières; this is a phantom-span removal, not a guessed replacement word.',
     'cancel_non', 'high')
mark(r'\unsure{tq-précédemment|toujours distinctes}', r'(\deleted{$j<i$} \unsure{tq-précédemment|toujours distinctes})',
     'first', 'tq-précédemment',
     'The t upright, q descender, short hyphen, p descender and two accent strokes support the first written abbreviated reading.',
     'tq_preced', 'medium')
mark(r'\unsure{$i$ elt final}', r'($j<i$ \inserted{\unsure{$i$ elt final}})',
     'other', '',
     'No separate insertion: upper i_n) belongs to the diagonal Drap factor, f to main forment, and the lower diagonal words to où / Drap. crowded_tails completes the earlier clipped view.',
     'crowded_tails', 'high')
mark(r'\unsure{forment|définissent}', r'\unsure{forment|définissent} (\inserted',
     'first', 'forment',
     'The main word begins with a tall looped f and a low orment run. It is not a d-initial word; the nearby diagonal writing is separately assigned.',
     'crowded_tails', 'medium')
mark(r'\unsure{les}', r'\inserted{\unsure{les} \illegible{1}',
     'undecided', r'\unsure{les}',
     'Looped l is clear; the short low e/s ending remains compressed. The source group is one word, not H’s le long de.',
     'codim')
mark(r'\illegible{1}', r'\unsure{les} \illegible{1} \unsure{de}',
     'other', r'\unsure{objt}',
     'The o-like loop, b upright, descending j-like stroke and final t-like upright allow a narrow abbreviation candidate. Its exact form remains uncertain; it is not expanded.',
     'codim')
mark(r'\unsure{de}', r'\illegible{1} \unsure{de} codim',
     'undecided', r'\unsure{de|e}',
     'A loop and low return are visible, but the supposed d upright is not separable enough to exclude an e-like group.',
     'codim')
mark(r"\unsure{d'}", r"codim $1$ \unsure{d'}", 'first', "d'",
     'The d loop/upright is followed by one independent apostrophe at upper right. No completion of the contraction is supplied.',
     'codim', 'medium')
mark(r'\unsure{\Sigma_*}', r'du \deleted{$\unsure{\Sigma_*}$} bord',
     'undecided', r'\unsure{\Sigma_*}',
     'The Sigma-like zigzag and small star-like index survive, but a crossing covers part of the top and index junction. Existing struck-symbol doubt retained.',
     'du_bord')
mark(r'\unsure{p.}', r'bord \unsure{p.} et les',
     'undecided', r'\deleted{\unsure{p.}}',
     'A p-like descender and detached point remain, with heavy overtrace/cancellation across the upper interior. Only cancellation state is corrected; the candidate is not resolved.',
     'bord_p')
mark(r'\unsure{en forment}', r"$d$ cofinal dans $d'$) \deleted{\unsure{en forment}}",
     'undecided', r'\unsure{en forment}',
     'Initial e, low n and tall f are visible; several interiors lie directly under the strike. The strict criterion for clearing canceled text is not met.',
     'en_forment')
mark(r'\unsure{\widehat{\operatorname{Drap}}(I_{i_{n-1}<\cdot<i_n})}',
     r'\times\ldots\times\unsure{\widehat{\operatorname{Drap}}(I_{i_{n-1}<\cdot<i_n})}',
     'undecided', r'\widehat{\operatorname{Drap}}(I_{\unsure{i_{n-1}<\cdot<}i_n})',
     'The completion exposes the hat, operator, I, final i_n and closing curve. The initial endpoint and middle relation are crossed by main-line forment’s f and remain narrowly doubtful. No mathematical completion is asserted.',
     'crowded_tails')
mark(r'\unsure{y.c. vides}', r'désigne les drapeaux, \unsure{y.c. vides}',
     'undecided', r'\unsure{y.c. vides}',
     'The small abbreviated y/c-like group with stops and following vides-like run is compressed and crossed by neighboring writing. Keep the written abbreviation candidate; do not expand y compris in the text.',
     'star_upper')
mark(r'\unsure{drapeau}', r'privé du \deleted{\unsure{drapeau}} pt unique',
     'undecided', r'\unsure{drapeau}',
     'Initial d and p descent survive but not every interior under the strike. Existing canceled-word doubt retained.',
     'star_lower')
mark(r'\unsure{correspondant aux}', r'pt unique \unsure{correspondant aux} drapeaux vides',
     'undecided', r'\unsure{correspondant aux}',
     'The long low word and short aux-like ending are present, but crossing strokes and the compressed middle prevent full separation of the letters.',
     'star_upper')
mark(r'\unsure{réunion}', r'-- le \deleted{\unsure{réunion}} \inserted',
     'undecided', r'\unsure{réunion}',
     'Several low loops and an accent survive. The cancellation covers the intervening letters, so the existing candidate remains doubtful.',
     'fibre_reunion')
mark(r'\unsure{réunion}', r'\deleted{formé des}\inserted{\unsure{réunion}}',
     'undecided', r'\inserted{\deleted{\unsure{réunion}}}',
     'The raised candidate has its own straight cancellation, distinct from the curved insertion leader below. The interior remains partly covered, so only state is corrected.',
     'est_reunion')
mark(r'\unsure{donne}', r'où $d$ \deleted{\unsure{donne}} parcourt',
     'undecided', r'\unsure{donne}',
     'Initial d-like upright survives, but the central low letters are fused with the cancellation. No letter-by-letter resolution.',
     'donne')
mark(r'\unsure{\Sigma}', r'\uline{strictement} \deleted{$\unsure{\Sigma}$} $(i,j)$',
     'undecided', r'\unsure{\Sigma}',
     'The lower zigzag is visible while the top is covered by the cancellation. Preserve the narrow Sigma candidate.',
     'strict_pair')
mark(r"\unsure{élément par l'ancien produit}", r"\deleted{\unsure{élément par l'ancien produit}",
     'undecided', r"\unsure{élément par l'ancien produit}",
     'The p-like descent after élément, l-apostrophe and produit are recognizable, but several intervening letters remain covered by the doubled strike. The whole existing canceled phrase stays doubtful.',
     'final_phrase')
mark(r'\unsure{drapeaux}', r'\margin{\unsure{drapeaux} \unsure{\deleted{côt. vide}}',
     'undecided', r'\unsure{\deleted{drapeaux}|drapeaux}',
     'First caption: d/r/a/p-like strokes survive but its lower run meets the horizontal crossing. Both the complete word and the extent of cancellation remain uncertain.',
     'final_product')
mark(r'\unsure{\deleted{côt. vide}}', r'\unsure{drapeaux} \unsure{\deleted{côt. vide}}',
     'undecided', r'\unsure{\deleted{côt. vide}|côt. vide}',
     'The short cot-like abbreviation and vide-like second group are at the dark lower edge. A distinct accent cannot be certified; neither the full letters nor cancellation reach is settled. The C candidate is retained under doubt rather than modernized or expanded.',
     'final_product')
mark(r'\unsure{drapeaux}', r'\qquad\unsure{drapeaux}\unsure{\deleted{stricts}}',
     'undecided', r'\unsure{\deleted{drapeaux}|drapeaux}',
     'Second caption: compressed drapeaux-like run lies immediately against the horizontal crossing. Full spelling and strike reach remain uncertain.',
     'final_product')
mark(r'\unsure{\deleted{stricts}}', r'\unsure{drapeaux}\unsure{\deleted{stricts}}',
     'undecided', r'\unsure{\deleted{stricts}|stricts}',
     'Short s/t-like start, i dot and terminal turns support the candidate, but crossing and the dark paper edge conceal interiors and deletion state. Strict doubt retained.',
     'final_product')

# Complete inventory of independent source elements and editing states.
inventory = [
 ('text','top main baseline','Enfin, dans le cas équisingulier'),
 ('display','first centered main display','Sigma_ij — Sigma_i, headless connector'),
 ('text','upper main paragraph','sont des fibrations ... non singulières'),
 ('display','inline after first i.e.','Sigma_** with headed s-arrow to Sigma_*'),
 ('text','upper main paragraph, next baselines','Sigma_i sont des variétés à bord ...'),
 ('display','second inline i.e.','Sigma_* variété à bord'),
 ('deletion','first parenthetic index condition','(j<i), crossed including its close'),
 ('text','after canceled condition','tq-précédemment)'),
 ('deletion','after à bord du','Sigma_i, heavily overwritten/crossed'),
 ('display','upper main boundary statement','dot Sigma_i de Sigma_i, puis Sigma_ji (j<i)'),
 ('insertion','raised above une stratification','les objt de/e codim 1 d’, with long curved leader'),
 ('margin note','left at the du/bord line','asterisk call and long curved arrow down-left to star note'),
 ('deletion','before bord par','Sigma_* candidate under cancellation'),
 ('text','main conclusion of f','bord par des variétés à bord -- Alors les'),
 ('display','main full-flag expression','Sigma_d=Sigma_{i_1, two strokes, i_n}; no comma'),
 ('deletion','after variétés à bord','p. candidate, heavy overtrace/crossing'),
 ('display','cofinal parenthesis','Sigma_d-prime; d-prime supersetneq d; d cofinal dans d-prime'),
 ('deletion','before live forment','en forment candidate, crossed'),
 ('text','end of upper main paragraph','forment une stratification cylindrique du bord'),
 ('deletion','immediately before dot Sigma_d','de'),
 ('display','upper paragraph ending','dot Sigma_d de Sigma_d, final point'),
 ('margin note','upper left, diagonal, two baselines','condition (e) double-quoted équisingularité'),
 ('margin note','upper diagonal, three continuations into top center','[Cela implique que ... segment initial de d.]'),
 ('margin note','left middle, two baselines','Condition (f) double-quoted non singularité; closing quote doubtful'),
 ('margin note','left lower-middle, diagonal, starred','cet ens d’indices des d-prime s’identifie au sous-ens de'),
 ('display','diagonal star note main product','hatted Drap factors, explicit i_1/i_2 and i_2/i_3 intervals, two-stroke continuation, crowded final factor'),
 ('insertion','above later junction of star-note product','hatted Drap(I_dot<i_1) times, with short curved down-right leader'),
 ('margin note','continuation of diagonal star note','où hatted Drap désigne les drapeaux, y.c. vides, privé du ...'),
 ('deletion','inside diagonal star note','drapeau candidate before pt unique'),
 ('margin note','last diagonal star-note baselines','pt unique correspondant aux drapeaux vides (pour d-prime=d=(i_1, one dash, i_n)'),
 ('margin note','far left, vertical to main writing','il s’identifie aussi à Drap of coproduct intervals; continuation split over two formula lines'),
 ('text','lower main paragraph','Dans le cas équisingulier-non singulier, on suppose, en plus de e) et f)'),
 ('insertion','above lower main map','fibrations, with a curved placement leader'),
 ('display','inline in lower main paragraph','Sigma_ij with headed arrow to Sigma_i'),
 ('deletion','after lower le','réunion candidate'),
 ('insertion','above canceled réunion after le','fibré sur Sigma_i'),
 ('text','lower main paragraph','des bords des fibres est ... stratifié par les Sigma_d'),
 ('deletion','after est','formé des'),
 ('insertion','raised above canceled formé des','réunion candidate, inserted then crossed again'),
 ('deletion','on raised insertion above formé des','separate straight cancellation through réunion, distinct from curved leader'),
 ('deletion','after lower d','donne candidate'),
 ('text','last live main baselines','parcourt les drapeaux qui contiennent strictly underlined strictement ...'),
 ('deletion','before live (i,j)','Sigma candidate'),
 ('display','last live pair','(i,j), round delimiters'),
 ('text','last live words','et ont i comme premier'),
 ('deletion','bottom main baseline','élément par l’ancien produit candidate and product of two hatted Drap factors'),
 ('display','bottom canceled product','two hats, i<dot<j and >j; first underbrace under operator only; second under whole factor'),
 ('text','two small baselines under first brace','drapeaux / côt. vide candidates, cancellation extent doubtful'),
 ('text','two small baselines under second brace','drapeaux / stricts candidates, cancellation extent doubtful'),
 ('margin note','lower left near the combined case','Condition g)'),
 ('margin note','bottom-left foliation','45'),
]
for i,(kind,position,first) in enumerate(inventory,1):
    D['inventory'].append(dict(element=f'046.E{i:02}', kind=kind,
        position=position, first_words_or_objects=first, sheet_kind='text',
        hand=('thin separate foliation hand, attribution uncertain' if first=='45' else 'his hand'),
        transcribed='yes'))

for place,reading,alts,conf in [
 ('stop after non singulières',r'\unsure{,|.}','comma or point','medium'),
 ('raised codimension first word',r'\unsure{les}','compressed les candidate; no full le long de','low'),
 ('raised codimension abbreviation',r'\unsure{objt}','written objt-like abbreviation; not expanded objets','low'),
 ('raised codimension preposition',r'\unsure{de|e}','de or e-like group','low'),
 ('canceled Sigma before bord par',r'\unsure{\Sigma_*}','Sigma-star candidate under crossing','low'),
 ('crossed fragment after bord',r'\deleted{\unsure{p.}}','p.-like fragment; interior covered','low'),
 ('canceled en forment',r'\unsure{en forment}','existing candidate; interiors covered','low'),
 ('f label closing quote',r"\unsure{''}",'closing double quote possibly entangled with main Sigma_i','low'),
 ('final marginal factor',r'\widehat{\operatorname{Drap}}(I_{\unsure{i_{n-1}<\cdot<}i_n})','initial endpoint and relations crossed by main f; final i_n clear','low'),
 ('marginal abbreviated inclusion of empty flags',r'\unsure{y.c. vides}','abbreviated y.c. vides candidate','low'),
 ('canceled marginal drapeau',r'\unsure{drapeau}','candidate remains partly hidden by strike','low'),
 ('marginal correspondant aux',r'\unsure{correspondant aux}','compressed and crossed interior','low'),
 ('first canceled réunion',r'\unsure{réunion}','strict existing canceled-word doubt','low'),
 ('raised canceled réunion',r'\inserted{\deleted{\unsure{réunion}}}','word remains strict; later strike visible','low'),
 ('canceled donne',r'\unsure{donne}','central letters masked','low'),
 ('canceled Sigma before pair',r'\unsure{\Sigma}','upper shape covered','low'),
 ('final canceled prose',r"\unsure{élément par l'ancien produit}",'letter interiors under doubled strike','low'),
 ('first caption word and state',r'\unsure{\deleted{drapeaux}|drapeaux}','candidate with unresolved cancellation reach','low'),
 ('first caption lower line and state',r'\unsure{\deleted{côt. vide}|côt. vide}','candidate; accent not separately certified; dark lower edge','low'),
 ('second caption word and state',r'\unsure{\deleted{drapeaux}|drapeaux}','candidate with unresolved cancellation reach','low'),
 ('second caption lower line and state',r'\unsure{\deleted{stricts}|stricts}','candidate; lower edge/crossing; strike reach uncertain','low'),
 ('terminal low mark',r'\unsure{,|)}','comma favored, extra closing parenthesis possible','medium'),
]:
    D['doubts'].append(dict(place=place,reading=reading,alternatives=alts,confidence=conf))

D['notes'] = [
 'Reported content only: condition e requires the written Sigma_ij-to-Sigma_i morphisms to be fibrations; its diagonal note says Sigma_d to Sigma_d-prime is a fibration when d-prime is an initial segment of d. No proof of that claim was attempted here.',
 'Reported content only: condition f concerns non singular strata and manifolds with boundary, their boundary strata, and Sigma_d for a flag d. Proper cofinal refinements d-prime are said to stratify the boundary of Sigma_d. The displayed supersetneq glyph is read from one separate lower bar, not chosen by interpreting strictness.',
 'Reported content only: the starred note describes the refinement index set using products of hatted Drap interval flags, including empty flags through the still-doubtful written abbreviation y.c. vides, with the all-empty point removed. Its raised extra factor is recorded where its short leader lands near a later junction; no factor order has been repaired by commutativity.',
 'Reported content only: the far-left vertical note gives an alternative Drap expression using coproduct intervals. Its continuation is physically split over two written formula lines: three small marks on the first line, then point plus dash on the second. The prose and all endpoint digits are transcribed.',
 'Reported content only: condition g supplements e and f by requiring manifold-with-boundary fibers and describing their boundary strata through flags strictly containing (i,j), with i first. The live sentence stops at premier; the following prose and product are canceled. No completion from another page has been supplied.',
 'No CHECK_EVENTS occurred in this reading. Identifying the claims and noting the likely role of empty flags are not proof checks, computations, or validations of the mathematics.',
 'Source-line coverage count: 52 separately written baselines, counted as 23 main prose/display baselines, 4 interlinear insertion baselines, 20 marginal prose/formula/label baselines (including the raised marginal factor), 4 small bottom-caption baselines, and 1 thin foliation baseline. This is reading coverage rather than edition line numbering; juxtaposed independent captions count separately.',
 'Whole image viewed once and native top/bottom halves once. All 39 created crops were viewed. There are 35 named distinct crop places. margin_e_tail is one necessary completion of the clipped upper continuation; crowded_tails jointly completes the overlapping final_insert/star_upper endings; label_e_end and label_f_end complete the two still-unsettled label edges. These four completion images are not additional physical places. No settled crop was regenerated and no other page or reader return was consulted.',
 'Important assignment corrections: H’s opening d’un espace / stratifié additions and its inverted second interlinear map are fragments of the diagonal Cela note. C’s i elt final insertion combines the final marginal index i_n), main forment’s f, and the diagonal où/Drap explanation. Both witnesses’ deleted illegible span before non singulières has no independent canceled source ink.',
 'The main opening Sigma_ij—Sigma_i connector is blunt and headless. The s-labeled inline map, the diagonal Sigma_d-to-Sigma_d-prime map, and the lower Sigma_ij-to-Sigma_i map have right heads. Their endpoints, labels and star counts were inspected individually.',
 'The long curved arrow joins the main asterisk at the left of the du/bord line to the star of the diagonal explanation. The short curved leader from the raised marginal Drap factor is a different annotation; it heads down/right near the end of the second explicit interval factor. These are placement leaders, not additional mathematical maps.',
 'The codimension insertion’s long curved line is a placement leader, not a pair of parentheses or cancellation. Its tentative word is the short written objt-like form; no expanded objets is inserted. Its final d-apostrophe is transcribed as written. Main forment remains live under the crossing marginal writing.',
 'Cancellation checks were separate: canceled (j<i) includes an actual closing curve; the later live parenthesis after tq-précédemment remains unmatched. The p.-like fragment after bord is crossed but unreadable inside. The raised réunion has its own straight strike in addition to its curved insertion leader. None of the existing canceled-word doubts was cleared without fully visible letters.',
 'Continuation counts are literal: main full-flag Sigma has two dashes and no comma; the star product has two dashes; the final starred tuple has comma after i_1 then one dash and only one visible close, without terminal point; the vertical formula preserves its separate three-mark and two-mark line segments. Prose -- encodes one written long dash in TeX typography and is not an assertion of two separate pen strokes.',
 'The first bottom underbrace attaches to hatted Drap only, ending before its opening parenthesis; the second underbrace attaches to the whole second factor. Long horizontal crossings leave the captions’ deletion reach uncertain, so live/struck alternatives are explicit. Their lower parts meet the dark scan edge. The cautious côt. vide candidate retains C’s doubt: no independent circumflex is certified.',
 'A separate low curved mark after the canceled product is preserved as comma-or-close uncertainty. A separate low stroke after non singulières is preserved as comma-or-point uncertainty. These are supported textual positions; isolated light background specks are not transcribed.',
 'The e-label opening and closing quotation form is double strokes, with the closing pair compactly merged, and no separate point. The f-label opening double strokes are clear; its closing quote is narrowly doubtful where it meets the large main Sigma_i. Both (e) and (f) have actual paired parentheses; inline e), f) and marginal g) do not have supplied opening parentheses.',
 'The thin pale 45 at the lower-left edge is a foliation number in a visibly different pen/hand, with attribution uncertain. It is not certified as Grothendieck’s own numbering. The sheet contains no dated entry; no date is supplied.',
 'Correction accounting excludes uncertainty-only changes when a witness reading remains an alternative. Retained strict doubts are fully logged in marks and doubts. Where H provides only illegibility but visible letter fragments support a narrow candidate, the confidence remains low and the C doubt is not counted as resolved. H editorial continuation and descriptive notes are excluded from source text.',
]

D['notation'] = [
 dict(form=r'\Sigma_{ij}-\Sigma_i',meaning_or_shape='Main opening connector is one blunt headless shaft; other maps on this leaf have explicit heads.',places='046 opening main display'),
 dict(form=r'\Sigma_{**}\xrightarrow{s}\Sigma_*',meaning_or_shape='Two source stars, one target star, explicit lower-case s over a headed right arrow; Sigma cap belongs to the letter.',places='046 first inline i.e.'),
 dict(form=r'\Sigma_{i_1-\, -i_n}',meaning_or_shape='Literal full-flag index uses two short continuation strokes and no comma after i_1.',places='046 main full-flag display'),
 dict(form=r"d'\supsetneq d",meaning_or_shape='Superset curve with one extra crossed lower bar, not two extra bars.',places='046 cofinal condition'),
 dict(form=r'\widehat{\operatorname{Drap}}',meaning_or_shape='Hatted Drap in the flag product and canceled final product; two final hats are independently visible.',places='046 star note and canceled lower product'),
 dict(form=r'I_{\cdot<i_1}',meaning_or_shape='Inserted interval index has an explicit dot before the less-than sign.',places='046 raised marginal factor'),
 dict(form=r"d'=d=(i_1,-i_n)",meaning_or_shape='Final star-note tuple has comma and one long continuation stroke, one visible closing parenthesis only.',places='046 last diagonal note line'),
 dict(form=r'\coprod -\,\cdot\,-\\\qquad\cdot\,-\coprod',meaning_or_shape='Continuation is split over source lines: short stroke/point/short stroke, then point/long stroke.',places='046 far-left vertical formula'),
]
D['abbreviations'] = [
 dict(form='i.e.',expansion='id est; both visible points retained in the inspected first occurrence'),
 dict(form='tq-précédemment',expansion='tq likely tel(s) que; written short form preserved; no expansion in the transcription'),
 dict(form=r'\unsure{objt}',expansion='tentative abbreviation for objet(s); exact written form remains uncertain'),
 dict(form='codim',expansion='codimension; no supplied terminal point'),
 dict(form='ens',expansion='ensemble'),
 dict(form='sous-ens',expansion='sous-ensemble'),
 dict(form=r'\unsure{y.c. vides}',expansion='y.c. likely y compris; remains a written abbreviation under doubt'),
 dict(form='pt',expansion='point'),
 dict(form=r'\unsure{côt. vide}',expansion='uncertain caption abbreviation; no firm expansion supplied'),
]
D['hand_log'] = [
 dict(habit='Very low flattened o/n and long return strokes can look like detached punctuation or hyphens.',places='046 opening on; non singulières; non singularité; lower combined case',consistent='All listed gaps/strokes compared locally; independent punctuation retained only after the upper singulières.',witness_errors='H adds opening comma; C adds hyphens in upper/lower main non singulier forms; both add the f-label hyphen.'),
 dict(habit='A diagonal marginal baseline can cross several main lines and masquerade as a main insertion.',places='046 Cela tail; final marginal Drap factor near second j<i/forment',consistent='The separate direction is visible in each discussed overlap.',witness_errors='H phantom d’un espace/stratifié and second map; C phantom i elt final.'),
 dict(habit='Headless shaft and explicit arrowhead are distinct on this same leaf.',places='046 first display, first inline i.e., marginal map, lower map',consistent='Only the first main displayed connector lacks a head.',witness_errors='Both witnesses supply an arrowhead in the opening display.'),
 dict(habit='Sigma top cap may be detached from its body; dot/star and lower index remain separate marks.',places='046 full-flag equality, dotted boundaries, first i.e., lower map',consistent='No detached Sigma cap was promoted to an overbar.',witness_errors='No new overbar error established; cap/body distinction checked throughout.'),
 dict(habit='j may have a long hooked descending stroke; i has a small detached dot and a short body.',places='046 ij/ji maps, both j<i groups, strict pair, final interval product',consistent='Separate comma read only where a distinct low curve is present, notably (i,j).',witness_errors='H changes round pair to braces; C inserts comma after i_1 in full-flag index.'),
 dict(habit='Continuation marks vary in count and length rather than following one normalized ellipsis shape.',places='046 main flag index, star product, final star tuple, vertical marginal formula',consistent='Two short strokes, one long stroke, and the split three-plus-two pattern coexist.',witness_errors='Both normalize multiple groups to ellipses; C also supplies a tuple close and stop.'),
 dict(habit='Straight cancellation across raised text is distinct from a curved placement leader beneath it.',places='046 codimension insertion; fibrations; fibré sur Sigma_i; raised réunion',consistent='Only the raised réunion has its own straight letter-crossing strike among those listed insertions.',witness_errors='Both witnesses leave the raised réunion live; C treats the codimension leader as parentheses.'),
 dict(habit='Small quotation strokes may merge into a compact dark two-lobed closing mark.',places='046 e/f marginal labels',consistent='E closing pair supported at medium confidence; f ending remains entangled with main Sigma_i.',witness_errors='H uses guillemets and adds a stop after the e-label.'),
 dict(habit='Thin pale foliation is visually distinct from the heavy main handwriting.',places='046 lower-left 45',consistent='One such foliation on this leaf; attribution remains uncertain.',witness_errors='C labels it as own manuscript pagination; H does not transcribe it.'),
]

# Literal, complete first readings for mandatory second-pass boxes.
celanote = T[T.index(r'\margin{[Cela'):T.index(r'\margin{Condition (f)')].strip()
starformula = T[T.index(r'$\begin{array}{rl}'):T.index(r'\end{array}$')+len(r'\end{array}$')]
starexplanation = T[T.index(r'où $\widehat'):T.index(r"\margin{il s'identifie")].strip()
starexplanation = starexplanation[:-1]  # final macro close is not source ink
verticalnote = T[T.index(r"\margin{il s'identifie"):T.index('\n\nDans le cas')].strip()
finalformula = T[T.rindex(r'\['):T.rindex(r'\]')+2]
for row in D['changes']:
    if row['place'] in ('final canceled product: two hats', 'final product: both underbraces and caption placement'):
        row['final'] = finalformula

box(1, 'C/H word difference', [275,70,1665,195],
    'Enfin, dans le cas équisingulier on suppose que les',
    'Whole opening baseline, including removal of H’s phantom additions and its supplied comma.')
box(2, 'low-confidence departure', [690,205,1035,313],
    r'\Sigma_{ij}-\Sigma_i',
    'Whole opening connector, preserving the headless shaft and both indices.')
box(3, 'margin note|C/H word difference|insertion', [18,20,1000,618], celanote,
    'Entire bracketed diagonal Cela note including its completed upper-right tail, both maps/relations, underline and final stop; also covers H’s misplaced interlinear fragments.')
box(4, 'margin note|C/H word difference|low-confidence departure', [20,175,540,468],
    r"\margin{condition (e) ``équisingularité''}",
    'Whole e-label and its completed quote ending; capital/lower-case, paired parentheses and quote strokes retained.')
box(5, 'doubt formula', [875,300,1640,400],
    r'$\Sigma_{**}\xrightarrow{s}\Sigma_*$',
    'Whole hard inline formula, including label, arrowhead and two/one stars; reviewed independently of opening shaft.')
box(6, 'C/H word difference|struck passage|low-confidence departure', [280,470,1060,580],
    r'non singulières\unsure{,|.}',
    'Live word group replacing both phantom struck-illegible spans; hyphen absence and narrow stop doubt.')
box(7, 'margin note|C/H word difference|low-confidence departure', [22,525,500,815],
    r"\margin{Condition (f) ``non singularité\unsure{''}}",
    'Whole f-label with completion, word gap and uncertain closing quote at main Sigma overlap.')
box(8, 'struck passage|doubt formula|C/H word difference|low-confidence departure', [422,764,1097,867],
    r'\deleted{($j<i$)} tq-précédemment)',
    'Complete canceled condition and adjacent resolved abbreviation, preserving the later unmatched live close.')
box(9, 'struck passage', [520,854,748,936],
    r'\deleted{$\Sigma_i$}',
    'Complete overwritten/canceled Sigma with its lower index.')
box(10, 'insertion|C/H word difference|handwritten number|low-confidence departure', [765,907,1283,1002],
    r"\inserted{\unsure{les} \unsure{objt} \unsure{de|e} codim $1$ d'}",
    'Whole raised codimension phrase and digit 1; all unresolved word groups and final d-apostrophe; curved leader is not parentheses.')
box(11, 'C/H word difference|low-confidence departure', [283,940,910,1070],
    r'$\Sigma_{ji}$ ($j<i$) forment',
    'Main formula and verb after excluding C’s phantom i elt final; the diagonal factor is covered separately in its complete product box.')
box(12, 'struck passage|doubt formula|C/H word difference|margin note', [280,1065,1120,1177],
    r'\margin{$*$}du \deleted{$\unsure{\Sigma_*}$} bord par',
    'Main star call, the omitted du/bord/par words, and whole canceled Sigma-star candidate.')
box(13, 'C/H word difference|low-confidence departure', [540,1176,824,1279],
    'Alors', 'Complete capitalized main word opposed to H’s plus généralement.')
box(14, 'handwritten number|doubt formula', [904,1146,1313,1252],
    r'$\Sigma_d=\Sigma_{i_1-\, -i_n}$',
    'Complete flag equality including digit 1, both continuation strokes and absent comma.')
box(15, 'struck passage|low-confidence departure', [484,1266,790,1390],
    r'bord \deleted{\unsure{p.}} et les',
    'Whole crossed p.-like fragment with surrounding words; interior remains strict doubt.')
box(16, 'doubt formula', [275,1258,1665,1465],
    r"$\Sigma_{d'}$ ($d'\supsetneq d$, $d$ cofinal dans $d'$)",
    'Complete cofinal condition across its source line break, including both primes and the one-extra-bar relation.')
box(17, 'struck passage|C/H word difference', [610,1376,891,1460],
    r'\deleted{\unsure{en forment}}',
    'Whole canceled phrase, strict existing doubt retained.')
box(18, 'struck passage|C/H word difference', [1070,1450,1524,1547],
    r'\deleted{de} $\dot\Sigma_d$ de $\Sigma_d$.',
    'Canceled de with the complete dotted-boundary ending and its final point.')
box(19, 'margin note|C/H word difference', [15,1070,710,1640],
    r"$*$ cet ens d'indices des $d'$ s'identifie au sous-ens de",
    'Entire marginal opening, including the written abbreviations and the note’s star.')
box(20, 'margin note|insertion|doubt formula|handwritten number|C/H word difference|low-confidence departure', [15,790,1170,1640],
    starformula,
    'Whole marginal product, all endpoint digits and hats, raised extra factor at its observed junction, two continuation strokes, and complete crowded final factor including its completed edge.')
box(21, 'margin note|struck passage|doubt formula|handwritten number|C/H word difference', [15,1050,900,1905],
    starexplanation,
    'All remaining starred-note prose, strict canceled drapeau, abbreviation and compressed phrase doubts, and full final tuple with digit 1, one dash, one close and no supplied stop.')
box(22, 'margin note|doubt formula|handwritten number|C/H word difference', [15,775,195,1310],
    verticalnote,
    'Entire vertical note and its two-line formula, every endpoint digit, all coproducts and both literal continuation groups.')
box(23, 'C/H word difference', [760,1565,1585,1675],
    'équisingulier-non singulier,',
    'Whole combined-case phrase with its one hyphen and written comma.')
box(24, 'C/H word difference', [295,1662,1275,1795],
    'en plus de e) et f),',
    'Baseline phrase and the two references, without supplied opening parentheses.')
box(25, 'insertion', [545,1728,870,1832],
    r'\inserted{fibrations}',
    'Whole raised insertion and its separate curved placement leader.')
box(26, 'doubt formula', [751,1775,1100,1887],
    r'$\Sigma_{ij}\longrightarrow\Sigma_i$',
    'Whole lower map and indices, with its clear right head; not normalized to the headless opening display.')
box(27, 'struck passage|insertion|C/H word difference', [715,1855,1076,1971],
    r'\deleted{\unsure{réunion}} \inserted{fibré sur $\Sigma_i$}',
    'Canceled réunion under its replacement, including complete inserted Sigma_i formula.')
box(28, 'struck passage|insertion|C/H word difference', [335,1963,795,2080],
    r'\deleted{formé des}\inserted{\deleted{\unsure{réunion}}}',
    'Both main canceled words and the raised insertion canceled a second time; straight strike distinct from curved leader.')
box(29, 'struck passage|C/H word difference', [320,2070,816,2175],
    r'$d$ \deleted{\unsure{donne}} parcourt',
    'Whole strict canceled-word candidate, with its main-line neighbors.')
box(30, 'struck passage|doubt formula|C/H word difference', [700,2140,885,2260],
    r'\deleted{$\unsure{\Sigma}$} $(i,j)$',
    'Whole canceled Sigma candidate and the complete live pair, comma and both round delimiters.')
box(31, 'struck passage|C/H word difference', [285,2218,1066,2328],
    r"\deleted{\unsure{élément par l'ancien produit}}",
    'Whole existing canceled prose doubt, with no restoration from expected grammar.')
box(32, 'struck passage|doubt formula|C/H word difference|low-confidence departure', [1025,2208,1684,2359],
    finalformula,
    'Complete canceled product with two hats, both interval factors, differently scoped underbraces, all caption reading/state doubts and the low terminal comma-or-close mark.')
box(33, 'margin note|C/H word difference', [18,1735,314,1929],
    r'\margin{Condition g)}',
    'Complete lower marginal label; no opening parenthesis supplied.')
box(34, 'margin note|handwritten number|low-confidence departure', [15,2255,195,2358],
    r'\margin{45}',
    'Both thin foliation digits, with hand attribution uncertain rather than own manuscript numbering.')

# Put source-coordinate boxes in page order; logical groups remain intact.
D['second_boxes'].sort(key=lambda b: (b['coords'][1], b['coords'][0]))
for i,b in enumerate(D['second_boxes'],1):
    b['box'] = f'b{i:02}'

def norm(s):
    return re.sub(r'\s+', '', s)

issues = []
for i,r in enumerate(D['changes'],1):
    for key,source in [('C',C),('H',H)]:
        if r[key] != '[absent]' and norm(r[key]) not in norm(source):
            issues.append(f'change {i} {key} excerpt not exact: {r[key]}')
    if norm(r['final']) not in norm(T):
        issues.append(f'change {i} final not in TeX: {r["final"]}')
    if not (WORK/'crops'/r['crop']).exists():
        issues.append(f'change {i} missing crop')
for i,m in enumerate(D['marks'],1):
    if m['mark'] not in C or norm(m['context']) not in norm(C):
        issues.append(f'mark {i} original/context not exact')
    if m['reading'] and norm(m['reading']) not in norm(T):
        issues.append(f'mark {i} reading not in TeX')
for b in D['second_boxes']:
    if norm(b['reading']) not in norm(T):
        issues.append(f'{b["box"]} reading not literal in TeX')
    x0,y0,x1,y1=b['coords']
    if not (0<=x0<x1<=1684 and 0<=y0<y1<=2359):
        issues.append(f'{b["box"]} invalid bounds')

depth=0
for i,ch in enumerate(T):
    if ch in '{}':
        # All braces on this page are TeX grouping braces, not escaped literal braces.
        depth += 1 if ch=='{' else -1
        if depth < 0:
            issues.append(f'negative brace depth at {i}')
if depth:
    issues.append(f'brace imbalance {depth}')
if T.count('$') % 2:
    issues.append('odd dollar count')

(OUT/'150_scan046.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(D['changes']),'marks':len(D['marks']),
 'inventory':len(D['inventory']),'second_boxes':len(D['second_boxes']),
 'doubts':len(D['doubts']),'crops':len(crop_names),'issues':issues},ensure_ascii=False,indent=2))


