from pathlib import Path
import csv
import json

ROOT = Path('/workspace/scratch/937907bd75d7/SP75_C13_145_work')
PACKET = ROOT/'packets/145_scan013'
OUT = ROOT/'edition/reader_reports'
OUT.mkdir(parents=True, exist_ok=True)
crop_boxes = json.loads((ROOT/'edition/crops/145_scan013_crop_boxes.json').read_text())

def locus(n):
    stem = next(k for k in crop_boxes if k.startswith(f'145_scan013_{n:02d}_'))
    return {'crop': f'crops/{stem}.png', 'box': crop_boxes[stem]}

changes = []
def change(place, C, H, final, ink, confidence, kind, c_changed, h_changed,
           marked_in_H, crop_number, categories, consequence=''):
    entry = dict(id=f's013-{len(changes)+1:02d}', place=place, C=C, H=H,
                 final=final, ink=ink, confidence=confidence, kind=kind,
                 c_changed=c_changed, h_changed=h_changed,
                 marked_in_H=marked_in_H, **locus(crop_number),
                 error_category=categories, math_consequence=consequence)
    changes.append(entry)
    return entry['id']

comme = change('Initial word of the first line', 'Comme', 'comme', 'Comme',
    'The opening C is a large open curve rising above the small connected letters that follow.',
    'high', 'misread word', False, True, 'no', 1, [2])
nest = change('First line, after mais', "n'est", 'aussi', "n'est",
    'A short n is followed by an apostrophe and the connected est, ending in a rising t. There is no initial a or double-s sequence here.',
    'high', 'misread word', False, True, 'no', 1, [2],
    'The parenthesis states a possible failure of the square condition.')
carre = change('Start of the second line, before l_infinity', 'pas de carré',
    r'\uncertain{par} \ill{} avec', 'pas de carré',
    'The first word has a p descender followed by low a/s strokes; de has its looped d. Carré has the round opening c/a, two short r strokes and an accent above the final é. The proposed avec is absent.',
    'high', 'misread word', False, True, 'yes', 2, [2, 5, 9])
le = change('Second line, between on doit and multiplier', 'le', r'\ill{}', 'le',
    'A tall looped l and low e stand between the final t of doit and the initial m of multiplier, despite the nearby cancelled formula below.',
    'high', r'readable ink left as \ill{}', False, True, 'yes', 3, [5])
operator_insertion = change('Small raised operator added after the first epsilon definition',
    r'(\operatorname{int}(l_0)\sigma_\infty)\inserted{\unsure{\operatorname{int}(l_\infty^\alpha)}}',
    r'\bigl(\mathrm{int}(l_0)\sigma_\infty\bigr)^{\mathrm{int}(l_\infty^{\alpha})}',
    r'(\operatorname{int}(l_0)\sigma_\infty)\inserted{\operatorname{int}(l_\infty^\alpha)}',
    'The raised added group reads int(l_infinity^alpha): dotted i, low n, tall t, parentheses, looped l, infinity subscript and alpha above. It follows the closing parenthesis as an addition. The opening prose on this same page says to multiply on the right by this operator; that supports the insertion placement rather than a new exponent on the whole preceding operator.',
    'high', 'insertion or placement', False, True, 'yes', 4, [6],
    'Records the added right-hand operator factor without introducing exponentiation by an automorphism.')
missing_open = change('First action formula after i.e. on the upper display',
    r'\varepsilon_\infty(l_0)=l_0l_1l_0^{-1}',
    r'\varepsilon_\infty(l_0) = l_0 l_1 l_0^{-1}',
    r'\varepsilon_\infty l_0)=l_0l_1l_0^{-1}',
    'After epsilon and its infinity subscript the l_0 begins directly. There is a closing parenthesis after l_0, but no separate opening curve before it. In the following epsilon_infinity(l_1), the opening curve is distinct. Both witnesses supply the missing opening parenthesis.',
    'high', 'text not on the page', True, True, 'no', 4, [9],
    'An unmatched authorial closing parenthesis is preserved; the formula is not silently repaired.')
bar_m = change('Cancelled lead-in above the epsilon_0 and epsilon_1 definitions',
    r'et de $\unsure{=|\bar m}$', 'et de même', r'et de $\bar m$',
    'The upper stroke is a horizontal bar. The lower stroke is curved with shallow joined humps, rather than a second straight equality stroke. It is the barred-m short form, and these strokes are clear between the oblique cancellation lines.',
    'high', 'abbreviation expanded or spelling modernised', True, True, 'no', 5, [8])
pair_punctuation = change('Ends of the two cancelled epsilon definitions',
    r'\varepsilon_0=\operatorname{int}(l_{\unsure{1|0}})\sigma_0\qquad\varepsilon_1=\operatorname{int}(l_\infty)\sigma_1.',
    r'\varepsilon_0 = \mathrm{int}(l_1)\sigma_0,\qquad\varepsilon_1 = \mathrm{int}(l_\infty)\sigma_1',
    r'\varepsilon_0=\operatorname{int}(l_{\unsure{1|0}})\sigma_0\qquad\varepsilon_1=\operatorname{int}(l_\infty)\sigma_1',
    'No separate comma follows sigma_0, and no separate stop follows sigma_1. The small dark ending beneath the latter sigma is its subscript 1. The generator subscript in the first int argument remains entangled with a diagonal strike, so C\'s 1|0 doubt is retained.',
    'high', 'text not on the page', True, True, 'no', 5, [9])
aura_donc = change('Cancelled words following On',
    r'\deleted{aura donc}', r'\struck{aura} \ill{}', r'\deleted{aura donc}',
    'The low rising stroke crosses aura. A second, higher horizontal stroke traverses the following donc, whose d and low joined ending survive below it. Both words belong to the cancellation.',
    'high', 'deletion state', False, True, 'yes', 6, [3, 5, 7])
square_insert = change('Above-line replacement for aura donc',
    r'\inserted{doit écrire $\varepsilon_\infty^2=l_\infty$:}',
    r'\marginal{doit écrire $\varepsilon_0^2 = l_\infty$ \ill{}}',
    r'\inserted{doit écrire $\varepsilon_{\unsure{\infty|0}}^2=l_\infty$..}',
    'Doit écrire is clear above the cancellation. The epsilon subscript is compact: a small left component joins a larger closed right part, admitting infinity or 0; the square 2 and the right-hand l_infinity are clear. Two separate dark dots lie horizontally after the formula, not one above the other. This is an interlinear replacement after On, not an independent marginal note.',
    'medium', 'insertion or placement', True, True, 'yes', 6, [1, 5, 6, 9],
    'The compact subscript is left uncertain, infinity first; no expected square identity is used to normalize it.')
ecrivant = change('Remainder of the line beginning Ecrivant',
    r'Ecrivant $g$ au lieu de $\operatorname{int}(g)$',
    r'\uncertain{Écrivant} que \uncertain{$g$} \ill{} au $\mathrm{int}(g)$',
    r'Ecrivant $g$ au lieu de $\operatorname{int}(g)$',
    'The large E has no separate accent. Ecrivant ends before a blank and the looped, long-descending g; there is no intervening que. Two short strokes give au, followed by lieu with its tall l and dotted i, then de and int(g).',
    'high', r'readable ink left as \ill{}', False, True, 'yes', 7, [2, 3, 5, 8, 9])
ss = change('Next prose line, before groupe', 'ss-groupe', 'sous-groupe', 'ss-groupe',
    'Two compressed s strokes precede a short hyphen and the large descending g of groupe. There are no written ou letters between the s strokes.',
    'high', 'abbreviation expanded or spelling modernised', False, True, 'no', 8, [8])
je_ecris = change('Right end of the line after Aut(pi)',
    r'je \deleted{\unsure{trouve}} \inserted{\unsure{écris}}',
    'on trouve', r'je \deleted{\unsure{trouve}} \inserted{\unsure{écris}}',
    'The live pronoun has a long descending j followed by e, not two low letters on. The following lower word is crossed horizontally and is best read trouve, but the middle joins remain obscured. Above it is an added word beginning écr; its ending reaches the scan edge, so écris remains uncertain. H loses both the cancellation and its replacement.',
    'medium', 'deletion state', False, True, 'no', 8, [2, 3, 6, 7])
brace_scope = change('First surviving square computation, lower bracket',
    r'\varepsilon_\infty^2=l_0\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty l_\infty^\alpha}',
    r'\varepsilon_\infty^2 = l_0\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty}l_\infty^\alpha',
    r'\varepsilon_\infty^2=l_0\unsure{\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty l_\infty^\alpha}}',
    'The lower stroke begins beneath the first sigma and runs to the final l_infinity^alpha. An internal upturn occurs under the second sigma, followed by a further curl under the final factor. Its full extent is visible, but whether it is one bracket or a shorter bracket with an adjacent mark is not settled. The mathematical letters and exponents are clear.',
    'low', 'other', False, True, 'no', 9, [10],
    'The doubt concerns the extent of a grouping mark, not the product itself.')
deleted_argument = change('Second sigma argument in the zigzag-cancelled expansion',
    r'\sigma_\infty(l_\infty)^{\alpha-1}',
    r'\sigma_\infty(l_0)^{\alpha-1}',
    r'\sigma_\infty(l_\infty)^{\alpha-1}',
    'Inside the second parenthesis the l has a two-lobed infinity subscript, visible below and to the right of its foot. The superscript alpha-1 is clear above the cancellation. It is not the single small 0 used in the later sigma(l_0) factor.',
    'high', 'misread symbol or index', False, True, 'no', 10, [1],
    'Retains the infinity argument in this rejected calculation.')
live_equals = change('Initial equals sign of the zigzag-cancelled expansion',
    r'\deleted{=}', '=', '=',
    'The equals sign stands to the left of the first l_0. The zigzag cancellation begins at the factors to its right and does not traverse either equality stroke.',
    'high', 'deletion state', True, False, 'no', 10, [7])
lower_annotation = change('Small lower annotation beneath the first underbraced factor of that expansion',
    r'\inserted{\unsure{l_0l_\infty}}',
    r'\note{sous la ligne biffée, deux ébauches également biffées : $l_0 l_\infty$ et $l_1^{-1} l_0^{-1}$}',
    r'\inserted{l_0l_\infty.}',
    'Two looped l letters have respectively a small closed 0 and a two-lobed infinity below them. A separate dark final stop follows. All these strokes are below the zigzag and remain unstruck. C nests the annotation inside its larger deleted expression; H calls both lower drafts struck. The annotation itself is live.',
    'high', 'deletion state', True, True, 'no', 10, [3, 6, 7],
    'Preserves the live lower annotation attached to a cancelled factor.')
inverse_insert = change('Struck insertion above et la relation, after the square relation',
    r'\inserted{\deleted{$(=l_1^{-1}l_0^{-1})$}}', '',
    r'\inserted{\deleted{$(=)l_1^{-1}l_{\unsure{0|\infty}}^{-1}$}}',
    'The opening curve and a short closing curve enclose the equals at the left of the added inverse product. Both l letters and their -1 exponents are visible under the strike; the first subscript is 1. The second low index is broad and curved, so 0 and infinity cannot be conclusively separated; a local 0-first doubt remains. No closing parenthesis is visible after the last inverse. The unusual (=) position is retained, rather than relocating the closing curve to the end.',
    'medium', 'insertion or placement', True, True, 'no', 11, [1, 3, 6, 7, 9])
aussi = change('Prose after et la relation epsilon_infinity squared equals l_infinity',
    'aussi', r'\uncertain{ainsi}', 'aussi',
    'The word has a low opening a/u sequence, two separate small s strokes and a final dotted i. It does not have the n of ainsi. Aussi is complete in crop12; the upper strokes of the following multipliant are outside this crop, but that following word was read on the original native half. A larger later-reading box includes the whole sentence.',
    'high', 'misread word', False, True, 'yes', 12, [2])
annotated_relation = change('First cancelled relation below en multipliant par l_0l_1',
    r'l_0l_\infty\underbrace{\sigma_\infty(l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1',
    r'l_0 l_\infty\,\sigma_\infty(l_\infty)^{\alpha-1}\,\sigma_\infty(l_0)\,l_\infty^{\alpha-1}=1',
    r'l_0l_\infty\underbrace{\sigma_\infty(l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1',
    'Two lower grouping strokes attach explicit labels: the left label is (l_0^{-1}l_1^{-1})^{alpha-1}, and the right is l_1. The long diagonal cancellations cross the relation and its lower writing. H moves the labels into an editorial note rather than preserving their attachment in the formula.',
    'high', 'insertion or placement', False, True, 'no', 13, [6])
ie_live = change('Left-hand i.e. before the next cancelled relation',
    'i.e.', r'\struck{\text{i.e.}}', 'i.e.',
    'The short i.e. is well to the left of all the long oblique cancellation strokes. Its letters and stops have no crossing line.',
    'high', 'deletion state', False, True, 'no', 14, [7])
cancelled_prefix = change('Separately crossed prefix of the second cancelled relation',
    r'\deleted{\unsure{l_\infty^{-1}l_\infty}}',
    r'l_0^{-1}l_1', r'\deleted{\unsure{l_\infty^{-1}l_\infty}}',
    'The two l stems and first exponent -1 survive, but a heavy horizontal line obscures their subscripts. The second subscript has a surviving downward stroke suggestive of 1. Neither subscript is fully plain, so the nested C doubt is retained; H\'s unqualified reading and omission of this additional crossing are not adopted.',
    'low', 'deletion state', False, True, 'no', 14, [1, 7])
margin = change('Right marginal query beside the live product equation',
    r'\margin{\unsure{prends} $\alpha=\unsure{2|1}$ ?}',
    r'\marginal{prenons $\alpha = 1$ ?}',
    r'\margin{\unsure{prends} $\alpha=\unsure{2|1}$ ?}',
    'The word begins with a long p descender and has a low joined middle followed by a dark rising and looped ending, supporting prends provisionally. The ending is dense, so the word remains uncertain. The digit after alpha= is overwritten, combining an upright with a lower horizontal foot and another curved stroke; 2 and 1 cannot be cleanly separated. The question mark is clear.',
    'low', 'misread word', False, True, 'no', 15, [1, 2])
rejected_product = change('Long rejected product ending =1? Non!',
    r'l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1l_0^{-1}l_1^{-1}l_0^{-1}=1?\qquad\text{Non !}',
    r'l_0 l_1 l_0 l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1l_0^{-1}=1\quad ?\quad\text{Non !}',
    r'l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1?\qquad\text{Non !}',
    'Counting the twelve factors from the left, both the ninth and eleventh have separate raised minus and 1 strokes above their l_1. The ninth exponent is absent from C; the eleventh is absent from H. These superscripts lie above the long horizontal cancellation and remain readable. The first seven factors also have individual diagonal crossings; the horizontal strike continues through the rejection Non !.',
    'high', 'misread symbol or index', True, True, 'no', 16, [1, 7],
    'The rejected twelve-factor product contains inverses at both disputed l_1 positions; neither complete witness string is retained.')
factor_scope = change('Next product: eight individually cancelled factors and live result',
    r'\deleted{l_0}\deleted{l_1}\deleted{l_0}\deleted{l_0^{-1}}\deleted{l_1^{-1}}\deleted{l_1}\deleted{l_1^{-1}}\deleted{l_0^{-1}}=1',
    r'\struck{l_0l_1l_0l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}=1}',
    r'\deleted{l_0}\deleted{l_1}\deleted{l_0}\deleted{l_0^{-1}}\deleted{l_1^{-1}}\deleted{l_1}\deleted{l_1^{-1}}\deleted{l_0^{-1}}=1',
    'Each of the eight factors has an oblique cancellation. The equals and final upright 1 stand beyond those strokes and remain live. There is no horizontal strike through the result.',
    'high', 'deletion state', False, True, 'no', 17, [7])
ok = change('Live comment to the right of the eight-factor cancellation', 'OK', 'ok', 'OK',
    'Both letters are large capitals, taller than the following small cursive donc. No cancellation crosses either letter.',
    'high', 'misread word', False, True, 'no', 17, [2])
footer = change('Handwritten lower-left page number', r'\mspage{12}', '', r'\mspage{12}',
    'A tall 1 with a small lead-in is followed by a 2 with a curved head, diagonal descent and horizontal foot. These are physical source digits at the lower left.',
    'high', 'omission', False, True, 'no', 18, [3])

tex = r'''\scanpage{13}
Comme $\operatorname{int}(l_0)\sigma_\infty$ fixe $l_\infty$ (mais n'est peut-être pas de carré $l_\infty$), on doit le multiplier à droite par un $\operatorname{int}(l_\infty^\alpha)$ $(\alpha\in\widehat{\mathbb Z})$.
\deleted{\[
\varepsilon_\infty(l_\infty)=l_\infty,\qquad\varepsilon_\infty(l_0)=
\]}
\[
\varepsilon_\infty=(\operatorname{int}(l_0)\sigma_\infty)\inserted{\operatorname{int}(l_\infty^\alpha)}\qquad\text{i.e.}\quad
\varepsilon_\infty l_0)=l_0l_1l_0^{-1},\quad\varepsilon_\infty(l_1)=l_0,\quad\varepsilon_\infty(l_\infty)=l_\infty
\]
\deleted{et de $\bar m$
\[
\varepsilon_0=\operatorname{int}(l_{\unsure{1|0}})\sigma_0
\qquad
\varepsilon_1=\operatorname{int}(l_\infty)\sigma_1
\]}
On \deleted{aura donc} \inserted{doit écrire $\varepsilon_{\unsure{\infty|0}}^2=l_\infty$..} Ecrivant $g$ au lieu de $\operatorname{int}(g)$ pour $g\in\pi$, i.e. identifiant $\pi$ à un ss-groupe de $\operatorname{Aut}(\pi)$, je \deleted{\unsure{trouve}} \inserted{\unsure{écris}}
\deleted{comme $\varepsilon_\infty=l_0\sigma_\infty$}
\[
\varepsilon_\infty=l_0\sigma_\infty l_\infty^\alpha.
\]
\deleted{\[
\varepsilon_\infty^2=l_0\sigma_\infty l_0\sigma_\infty
=l_0\sigma_\infty l_0\sigma_\infty^{-1}=l_0\sigma_\infty(l_0)
\]}
donc
\[
\begin{aligned}
\varepsilon_\infty^2&=l_0\unsure{\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty l_\infty^\alpha}}\\
&=l_0\sigma_\infty(l_\infty^\alpha l_0)l_\infty^\alpha
=l_0(l_0^{-1}l_1^{-1})^\alpha l_1(l_1^{-1}l_0^{-1})^\alpha\\
&=\underbrace{\deleted{l_0\sigma_\infty(l_\infty)}}_{\inserted{l_0l_\infty.}}\deleted{\sigma_\infty(l_\infty)^{\alpha-1}\sigma_\infty(l_0)l_\infty^\alpha}
\end{aligned}
\]
et la relation $\varepsilon_\infty^2=l_\infty$ \inserted{\deleted{$(=)l_1^{-1}l_{\unsure{0|\infty}}^{-1}$}} s'écrit aussi, en multipliant par $l_0l_1$
\deleted{\[
l_0l_\infty\underbrace{\sigma_\infty(l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1
\]}
i.e.
\deleted{\[
\deleted{\unsure{l_\infty^{-1}l_\infty}}l_0^{1-\alpha}l_1^{2-\alpha}l_\infty^\alpha=1
\]}
\[
l_0l_1l_0(l_0^{-1}l_1^{-1})^\alpha l_1(l_1^{-1}l_0^{-1})^\alpha=1
\]
\margin{\unsure{prends} $\alpha=\unsure{2|1}$ ?}
\deleted{\[
l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1?\qquad\text{Non !}
\]}
\[
\deleted{l_0}\deleted{l_1}\deleted{l_0}\deleted{l_0^{-1}}\deleted{l_1^{-1}}\deleted{l_1}\deleted{l_1^{-1}}\deleted{l_0^{-1}}=1
\qquad\text{OK}\qquad\text{donc}
\]
\[
\left\{\begin{aligned}
\varepsilon_\infty&=l_0\sigma_\infty l_\infty\quad\text{(ou encore }\operatorname{int}(l_0)\sigma_\infty\operatorname{int}(l_\infty)\text{)}\\
\varepsilon_0&=l_1\sigma_0l_0\\
\varepsilon_1&=l_\infty\sigma_1l_1
\end{aligned}\right.
\]
\mspage{12}
'''

decisions = [
    dict(id='M0802', decision='first', reading=r'\operatorname{int}(l_\infty^\alpha)',
         ink='The raised addition has dotted i, low n, tall t, an argument with looped l, infinity subscript and alpha exponent, and a closing parenthesis. The entire surrounding definition and all three action formulas were read on crop04; the first action has the separately logged missing opening parenthesis.',
         **locus(4), confidence='high'),
    dict(id='M0803', decision='undecided', reading=r'\unsure{écris}',
         ink='The beginning écr is visible above the crossed lower word, but the remaining short strokes meet the right scan edge. The full ending is not plain enough to remove C\'s doubt.',
         **locus(8), confidence='medium'),
    dict(id='M0804', decision='undecided', reading=r'\unsure{prends}',
         ink='The long p and low joined middle support prends, with a dense rising and looped final group. The final letters are too compressed to exclude the longer alternative prenons with confidence.',
         **locus(15), confidence='medium'),
    dict(id='M0805', decision='undecided', reading=r'\unsure{2|1}',
         ink='The digit is overwritten: a dark upright, a curved upper entry and a lower foot cannot be separated into a unique surviving 2 or 1. The neighboring alpha, equals and question mark are clear.',
         **locus(15), confidence='low'),
]

unlisted_decisions = [
    dict(id='U013-01', source_mark=r'\unsure{=|\bar m}', decision='alternative', reading=r'\bar m',
         ink='The lower component has curved joined humps beneath a separate horizontal bar; it is not a second straight equality stroke. No cancellation conceals these local strokes.', **locus(5), confidence='high'),
    dict(id='U013-02', source_mark=r'l_{\unsure{1|0}}', decision='undecided', reading=r'l_{\unsure{1|0}}',
         ink='A small upright suggests 1, but the diagonal cancellation touches the base/subscript area and prevents a completely plain reading. The whole cancelled definition is retained with C\'s choice.', **locus(5), confidence='low'),
    dict(id='U013-03', source_mark=r'\deleted{\unsure{trouve}}', decision='undecided', reading=r'\deleted{\unsure{trouve}}',
         ink='The t and some low joined letters remain visible under the horizontal line; the full middle sequence is obscured. The doubt inside the deletion remains.', **locus(8), confidence='low'),
    dict(id='U013-04', source_mark=r'\inserted{\unsure{l_0l_\infty}}', decision='first', reading=r'\inserted{l_0l_\infty.}',
         ink='Both l stems, the closed 0 and the two-lobed infinity are clear below the cancellation. A separate dark final stop is also present. These lower characters are not crossed.', **locus(10), confidence='high'),
    dict(id='U013-05', source_mark=r'\deleted{\unsure{l_\infty^{-1}l_\infty}}', decision='undecided', reading=r'\deleted{\unsure{l_\infty^{-1}l_\infty}}',
         ink='The horizontal crossing obscures both subscripts. A surviving downward stroke permits 1 for the second, but the complete underlying form is not legible; the first exponent -1 is plain.', **locus(14), confidence='low'),
]

inventory = []
def item(kind, position, first_words, box, **extra):
    inventory.append(dict(element=f'E{len(inventory)+1:02d}', kind=kind,
                          position=position, first_words_or_objects=first_words,
                          box=box, sheet_kind='text', hand='his hand',
                          transcribed='yes', **extra))

item('text', 'Top opening prose, two long lines and the small alpha condition below',
     'Comme int(l_0)sigma_infinity fixe l_infinity', [205,17,1664,181])
item('deletion', 'Horizontal cancellation between the opening prose and first definition',
     r'\varepsilon_\infty(l_\infty)=l_\infty,\quad\varepsilon_\infty(l_0)=', [397,106,992,175])
item('display', 'First definition and the three action formulas across the upper sheet',
     r'\varepsilon_\infty=(\operatorname{int}(l_0)\sigma_\infty)', [325,149,1677,285],
     layout_marks='Curved linking strokes run around this revised upper block. They are revision/connection marks, not an independent mathematical diagram; the associated insertion and cancelled earlier conditions are separately inventoried.')
item('insertion', 'Raised added right-hand operator after the first parenthesized definition',
     r'\inserted{\operatorname{int}(l_\infty^\alpha)}', [659,149,833,205])
item('deletion', 'Lead-in above the two rejected cyclic definitions',
     r'et de $\bar m$', [230,298,505,365])
item('deletion', 'First of the two rejected cyclic definitions',
     r'\varepsilon_0=\operatorname{int}(l_{\unsure{1|0}})\sigma_0', [350,355,746,447])
item('deletion', 'Second of the two rejected cyclic definitions',
     r'\varepsilon_1=\operatorname{int}(l_\infty)\sigma_1', [364,437,746,516])
item('text', 'Two prose lines beginning On and continuing to je at the right edge',
     'On ... Ecrivant g au lieu de int(g)', [211,553,1671,754])
item('deletion', 'Words replaced above the line after On',
     r'\deleted{aura donc}', [322,575,588,621])
item('insertion', 'Replacement above aura donc',
     r'\inserted{doit écrire $\varepsilon_{\unsure{\infty|0}}^2=l_\infty$..}', [342,511,759,583])
item('deletion', 'Crossed lower word at the right edge after je',
     r'\deleted{\unsure{trouve}}', [1540,690,1671,754])
item('insertion', 'Replacement above the crossed lower word at the right edge',
     r'\inserted{\unsure{écris}}', [1540,650,1671,708])
item('deletion', 'Crossed lead-in and preliminary epsilon expression',
     r'comme $\varepsilon_\infty=l_0\sigma_\infty$', [226,767,748,833])
item('display', 'Live epsilon expression to the right of the crossed lead-in',
     r'\varepsilon_\infty=l_0\sigma_\infty l_\infty^\alpha.', [764,740,1140,833])
item('deletion', 'Horizontal cancellation across the initial square computation',
     r'\varepsilon_\infty^2=l_0\sigma_\infty l_0\sigma_\infty', [500,846,1420,926])
item('text', 'Short lead-in at the left of the surviving computation', 'donc', [223,935,350,1007])
item('display', 'First line of the surviving computation, with ambiguous grouping mark below',
     r'\varepsilon_\infty^2=l_0\sigma_\infty l_\infty^\alpha l_0\sigma_\infty l_\infty^\alpha', [453,941,1117,1061])
item('display', 'Second computation line, continuing almost to the right edge',
     r'=l_0\sigma_\infty(l_\infty^\alpha l_0)l_\infty^\alpha', [552,1052,1668,1152])
item('display', 'Third computation line, with live equals and lower annotation but cancelled factors',
     r'=\underbrace{\deleted{l_0\sigma_\infty(l_\infty)}}', [551,1147,1336,1306])
item('deletion', 'Zigzag across the factors of that third computation line',
     r'l_0\sigma_\infty(l_\infty)\sigma_\infty(l_\infty)^{\alpha-1}\sigma_\infty(l_0)l_\infty^\alpha', [620,1147,1336,1275])
item('insertion', 'Live label below the cancelled first underbraced group',
     r'\inserted{l_0l_\infty.}', [681,1246,812,1306])
item('text', 'Sentence beginning et la relation, ending below with par l_0l_1',
     r'et la relation $\varepsilon_\infty^2=l_\infty$', [210,1315,1665,1458])
item('insertion', 'Added inverse product above the square-relation sentence, subsequently cancelled',
     r'\inserted{\deleted{$(=)l_1^{-1}l_{\unsure{0|\infty}}^{-1}$}}', [879,1273,1128,1365])
item('deletion', 'Strike through that above-line insertion',
     r'\deleted{$(=)l_1^{-1}l_{\unsure{0|\infty}}^{-1}$}', [879,1273,1128,1365])
item('deletion', 'First rejected relation, with two lower factor labels',
     r'l_0l_\infty\sigma_\infty(l_\infty)^{\alpha-1}\sigma_\infty(l_0)l_\infty^{\alpha-1}=1', [416,1436,1165,1641])
item('display', 'Left lower label within that cancelled relation',
     r'(l_0^{-1}l_1^{-1})^{\alpha-1}', [540,1549,794,1641])
item('display', 'Right lower label within that cancelled relation',
     r'l_1', [851,1549,940,1630])
item('text', 'Unstruck lead-in well to the left of the next rejected formula', 'i.e.', [214,1637,293,1748])
item('deletion', 'Second rejected relation, crossed by oblique strokes',
     r'\deleted{\unsure{l_\infty^{-1}l_\infty}}l_0^{1-\alpha}l_1^{2-\alpha}l_\infty^\alpha=1', [565,1637,1155,1748])
item('deletion', 'Additional horizontal crossing over the prefix of that relation',
     r'\deleted{\unsure{l_\infty^{-1}l_\infty}}', [565,1650,697,1748])
item('display', 'Live product equality below the rejected relations',
     r'l_0l_1l_0(l_0^{-1}l_1^{-1})^\alpha l_1(l_1^{-1}l_0^{-1})^\alpha=1', [275,1747,1119,1874])
item('margin note', 'Right margin beside the live product',
     r'\unsure{prends} $\alpha=\unsure{2|1}$ ?', [1232,1720,1615,1842])
item('deletion', 'Long rejected twelve-factor trial and rejection Non !',
     r'l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1?', [288,1870,1586,1991])
item('display', 'Next trial, with individual factor cancellations and live result and comments',
     r'l_0l_1l_0l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}=1\quad OK\quad donc', [291,1980,1444,2097])
for n, (factor, coords) in enumerate([
    (r'l_0', [329,2000,416,2085]),
    (r'l_1', [401,1998,476,2085]),
    (r'l_0', [455,1992,542,2082]),
    (r'l_0^{-1}', [523,1987,626,2080]),
    (r'l_1^{-1}', [605,1984,703,2077]),
    (r'l_1', [683,1990,761,2077]),
    (r'l_1^{-1}', [739,1980,837,2077]),
    (r'l_0^{-1}', [820,1982,922,2077]),
], 1):
    item('deletion', f'Individually cancelled factor {n} in the eight-factor trial',
         '\\deleted{'+factor+'}', coords)
item('text', 'Live result and comments to the right of the eight cancelled factors',
     r'$=1$ OK donc', [919,1980,1444,2097])
item('display', 'Final three-line system enclosed by a left brace',
     r'\varepsilon_\infty=l_0\sigma_\infty l_\infty;\quad\varepsilon_0=l_1\sigma_0l_0;\quad\varepsilon_1=l_\infty\sigma_1l_1', [485,2084,1572,2346])
item('text', 'Handwritten lower-left page number', r'\mspage{12}', [31,2277,113,2346])

second_boxes = []
def second(kind, coords, reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}', kind=kind,
                             coords=coords, reading=reading))

second('Opening lexical disagreements and complete formulas with handwritten generator indices',
       [205,17,1664,181],
       r"Comme $\operatorname{int}(l_0)\sigma_\infty$ fixe $l_\infty$ (mais n'est peut-être pas de carré $l_\infty$), on doit le multiplier à droite par un $\operatorname{int}(l_\infty^\alpha)$ $(\alpha\in\widehat{\mathbb Z})$.")
second('Entire initial cancellation, including the incomplete equality and all indices',
       [397,106,992,175],
       r'\deleted{\[\varepsilon_\infty(l_\infty)=l_\infty,\qquad\varepsilon_\infty(l_0)=\]}')
second('Entire upper definition and three action formulas; inserted C-doubt operator, missing opening parenthesis, numeric indices',
       [325,149,1677,285],
       r'\[\varepsilon_\infty=(\operatorname{int}(l_0)\sigma_\infty)\inserted{\operatorname{int}(l_\infty^\alpha)}\qquad\text{i.e.}\quad\varepsilon_\infty l_0)=l_0l_1l_0^{-1},\quad\varepsilon_\infty(l_1)=l_0,\quad\varepsilon_\infty(l_\infty)=l_\infty\]')
second('Complete cancelled lead-in and both epsilon definitions, including barred m and unresolved index',
       [230,298,746,516],
       r'\deleted{et de $\bar m$ \[\varepsilon_0=\operatorname{int}(l_{\unsure{1|0}})\sigma_0\qquad\varepsilon_1=\operatorname{int}(l_\infty)\sigma_1\]}')
second('On, its cancellation and full interlinear replacement; uncertain epsilon subscript and handwritten square 2',
       [211,511,759,641],
       r'On \deleted{aura donc} \inserted{doit écrire $\varepsilon_{\unsure{\infty|0}}^2=l_\infty$..}')
second('Full Ecrivant phrase and its lexical disagreements',
       [638,553,1668,648],
       r'Ecrivant $g$ au lieu de $\operatorname{int}(g)$ pour $g\in\pi$,')
second('Full following prose line, abbreviation, live je, cancelled trouve and inserted écris',
       [215,650,1671,754],
       r'i.e. identifiant $\pi$ à un ss-groupe de $\operatorname{Aut}(\pi)$, je \deleted{\unsure{trouve}} \inserted{\unsure{écris}}')
second('Cancelled preliminary expression and complete live epsilon formula with index 0',
       [226,740,1140,833],
       r'\deleted{comme $\varepsilon_\infty=l_0\sigma_\infty$} \[\varepsilon_\infty=l_0\sigma_\infty l_\infty^\alpha.\]')
second('Complete first cancelled square computation, including square 2 and inverse -1',
       [500,846,1420,926],
       r'\deleted{\[\varepsilon_\infty^2=l_0\sigma_\infty l_0\sigma_\infty=l_0\sigma_\infty l_0\sigma_\infty^{-1}=l_0\sigma_\infty(l_0)\]}')
second('Complete first surviving square formula; proposed doubt concerns lower grouping mark',
       [223,935,1124,1062],
       r'donc \[\varepsilon_\infty^2=l_0\unsure{\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty l_\infty^\alpha}}\]')
second('Entire next computation line, including every handwritten inverse and numeric index',
       [552,1052,1668,1152],
       r'\[=l_0\sigma_\infty(l_\infty^\alpha l_0)l_\infty^\alpha=l_0(l_0^{-1}l_1^{-1})^\alpha l_1(l_1^{-1}l_0^{-1})^\alpha\]')
second('Entire third computation line, its cancellation, live equals and live lower annotation',
       [551,1147,1336,1306],
       r'\[=\underbrace{\deleted{l_0\sigma_\infty(l_\infty)}}_{\inserted{l_0l_\infty.}}\deleted{\sigma_\infty(l_\infty)^{\alpha-1}\sigma_\infty(l_0)l_\infty^\alpha}\]')
second('Full square-relation sentence and its struck insertion, including odd parenthesis placement and aussi',
       [210,1273,1665,1458],
       r"et la relation $\varepsilon_\infty^2=l_\infty$ \inserted{\deleted{$(=)l_1^{-1}l_{\unsure{0|\infty}}^{-1}$}} s'écrit aussi, en multipliant par $l_0l_1$")
second('Complete cancelled relation with both lower labels and all handwritten numbers',
       [416,1436,1165,1641],
       r'\deleted{\[l_0l_\infty\underbrace{\sigma_\infty(l_\infty)^{\alpha-1}}_{(l_0^{-1}l_1^{-1})^{\alpha-1}}\underbrace{\sigma_\infty(l_0)}_{l_1}l_\infty^{\alpha-1}=1\]}')
second('Live i.e., complete second cancelled relation, and separately crossed doubtful prefix',
       [214,1637,1155,1748],
       r'i.e. \deleted{\[\deleted{\unsure{l_\infty^{-1}l_\infty}}l_0^{1-\alpha}l_1^{2-\alpha}l_\infty^\alpha=1\]}')
second('Entire live product equality, all handwritten inverses, indices and final 1',
       [275,1747,1119,1874],
       r'\[l_0l_1l_0(l_0^{-1}l_1^{-1})^\alpha l_1(l_1^{-1}l_0^{-1})^\alpha=1\]')
second('Complete marginal query; C word doubt and overwritten digit choice',
       [1232,1720,1615,1842],
       r'\margin{\unsure{prends} $\alpha=\unsure{2|1}$ ?}')
second('Complete rejected twelve-factor trial; ninth and eleventh inverse disagreements, rejection and cancellation',
       [288,1870,1586,1991],
       r'\deleted{\[l_0l_1l_0l_0^{-1}l_1^{-1}l_0^{-1}l_1^{-1}l_1l_1^{-1}l_0^{-1}l_1^{-1}l_0^{-1}=1?\qquad\text{Non !}\]}')
second('All eight individual cancellations, complete live result and OK donc',
       [291,1980,1444,2097],
       r'\[\deleted{l_0}\deleted{l_1}\deleted{l_0}\deleted{l_0^{-1}}\deleted{l_1^{-1}}\deleted{l_1}\deleted{l_1^{-1}}\deleted{l_0^{-1}}=1\qquad\text{OK}\qquad\text{donc}\]')
second('Entire final braced system with every numeric index',
       [485,2084,1572,2346],
       r'\[\left\{\begin{aligned}\varepsilon_\infty&=l_0\sigma_\infty l_\infty\quad\text{(ou encore }\operatorname{int}(l_0)\sigma_\infty\operatorname{int}(l_\infty)\text{)}\\\varepsilon_0&=l_1\sigma_0l_0\\\varepsilon_1&=l_\infty\sigma_1l_1\end{aligned}\right.\]')
second('Handwritten page number', [31,2277,113,2346], r'\mspage{12}')

diff_rows = list(csv.DictReader((PACKET/'differences.tsv').open(), delimiter='\t'))
substantive_rows = {
    2: ([nest], ''), 3: ([carre], ''), 4: ([le], ''),
    5: ([operator_insertion], 'Raised placement is an insertion after the parenthesis; the opening sentence expressly says to multiply on the right.'),
    9: ([bar_m], ''),
    11: ([pair_punctuation], 'H inserts a comma after the first cancelled definition.'),
    12: ([pair_punctuation], 'C supplies a stop after the second cancelled definition; none is visible.'),
    13: ([aura_donc,square_insert,ecrivant], 'Long alignment span includes the deleted donc, the above-line replacement, and the following Ecrivant phrase.'),
    14: ([ecrivant], ''), 15: ([ss], ''), 16: ([je_ecris], ''), 17: ([je_ecris], ''),
    20: ([square_insert], 'H relocates the above-line replacement and supplies an editorial note about its index. The following cancelled square computation is present in both witnesses.'),
    33: ([deleted_argument,lower_annotation], 'Alignment fragment from the third computation line and its lower label; not a new extra sigma in the source.'),
    34: ([deleted_argument,lower_annotation], 'Continuation of the same alignment shift around the labelled cancelled factor.'),
    35: ([lower_annotation,deleted_argument], 'The l_0l_infinity label and neighboring argument are misaligned by the token comparison; see the complete formula entries.'),
    36: ([deleted_argument,lower_annotation,inverse_insert,aussi], 'The long shifted segment crosses H\'s editorial lower-label note and the following prose. It does not represent one continuous source substitution.'),
    39: ([inverse_insert], 'C preserves an added struck inverse product that H leaves out of the prose; its actual parentheses are also corrected.'),
    40: ([annotated_relation,ie_live], 'Cross-alignment between the inserted product, the first rejected relation and H\'s struck i.e.; the complete inscriptions are logged separately.'),
    41: ([aussi,inverse_insert], 'The prose contains aussi, not H\'s ainsi; the long token shift also reflects the nearby inserted parenthesis.'),
    42: ([annotated_relation,cancelled_prefix], 'Not a literal change from 0l to 1: this alignment jumps between the two cancelled relations. Their lower labels and doubtful prefix are handled at the linked loci.'),
    43: ([annotated_relation], 'Alignment fragment caused by H moving the first formula\'s lower labels into an editorial note.'),
    44: ([annotated_relation], 'Continuation of that lower-label alignment shift; no independent parenthesis omission is inferred from the token row.'),
    45: ([annotated_relation], 'The minus and equals belong to differently aligned formula positions; the full source relation and labels are preserved.'),
    46: ([annotated_relation], 'H\'s explanatory note reports source labels that belong beneath the cancelled factors.'),
    47: ([annotated_relation], 'Continuation of the lower-label alignment; the label l_1 is restored to its attached factor.'),
    48: ([annotated_relation], 'Continuation of H\'s editorial description of the source lower labels.'),
    49: ([annotated_relation], 'Closing fragment of the underbrace/label alignment shift.'),
    50: ([cancelled_prefix,ie_live], 'The C passage spans the first relation ending, the live i.e., and a doubly crossed prefix; the latter differs substantively from H.'),
    54: ([margin], ''), 55: ([margin], 'The overwritten digit remains 2|1 rather than being regularized to H\'s 1.'),
    60: ([rejected_product], 'Ninth factor has exponent -1: C omits it.'),
    61: ([rejected_product], 'Eleventh factor has exponent -1: H omits it.'),
    74: ([footer], 'The physical page number 12 is present in the lower-left corner.'),
}
coverage = []
for row_number, raw in enumerate(diff_rows, 1):
    row = {'row':row_number}
    if row_number in substantive_rows:
        ids, explanation = substantive_rows[row_number]
        row.update(status='substantive', change_id=ids[0])
        if len(ids)>1:
            row['related_change_ids']=ids[1:]
        if explanation:
            row['explanation']=explanation
    else:
        if row_number == 1:
            explanation='C scanpage13 is an editorial page-identification macro, not a source numeral.'
        elif row_number == 8:
            explanation='H editorial note about the raised addition and curved connecting stroke. Its prose is not source text; the actual insertion is logged separately.'
        elif row_number == 10:
            explanation='Tokenization of C\'s unresolved alternative 0. The primary 1 and alternative 0 remain uncertain under the strike; see U013-02 and the doubts list. No certainty-only change is entered as a substantive locus.'
        elif row_number == 51:
            explanation='Closing alignment shift between the second cancelled relation and the following live product. Their shared remaining factors are read from the ink; the doubtful prefix is logged separately.'
        elif row_number in (62,63):
            explanation='H editorial note about the factor cancellations and live comments; the note itself is excluded. The actual cancellation extent and capital OK are logged separately.'
        elif row_number in (64,73):
            explanation='aligned/cases and right-dot delimiter syntax express the same final left-braced system. The delimiter dot is not source punctuation.'
        else:
            explanation=r'TeX spacing or multiplication-factor token boundaries, including \,; no written comma or change of letters, indices or signs.'
        row.update(status='macro/editorial', explanation=explanation)
        if row_number in (23,24,25,26):
            row['related_change_ids']=[brace_scope]
            row['explanation'] += ' The distinct ambiguity about the lower bracket extent is recorded separately.'
    coverage.append(row)

report = {
    'scan':13,
    'reader':'/root/reader_b',
    'lines_read':33,
    'layout':'Upright handwritten working sheet, dominated by epsilon definitions and algebra. Two opening prose lines lead into an initial horizontal cancellation, a definition with a small raised addition and three action formulas, and two cancelled cyclic definitions. A two-line prose passage has two interlinear replacements. The middle has successive live and cancelled square computations, lower factor labels, and a separately struck added inverse expression. Two further relations are cancelled, followed by a live product, a short right-margin query, a rejected twelve-factor trial, an eight-factor cancellation with live result and comments, and a final left-braced three-line system. Handwritten page number 12 is at the lower left. Whole image and both native overlapping halves were each viewed once; eighteen local crops followed. No OCR, outside page, external source, TeX compilation or proof verification was used.',
    'changes':changes,
    'decisions':decisions,
    'unlisted_decisions':unlisted_decisions,
    'doubts':[
        dict(place='Cancelled epsilon_0 definition, generator index', reading=r'l_{\unsure{1|0}}', alternatives=['1','0'], confidence='low', reason='The diagonal strike touches the base/subscript area; not every index stroke is plain.'),
        dict(place='Interlinear square relation after doit écrire', reading=r'\varepsilon_{\unsure{\infty|0}}^2=l_\infty', alternatives=[r'\varepsilon_\infty^2=l_\infty',r'\varepsilon_0^2=l_\infty'], confidence='medium', reason='The compact subscript has a small left component and closed right portion. It may be infinity or 0; the expected later formula does not settle the ink.'),
        dict(place='Cancelled word after je', reading=r'\deleted{\unsure{trouve}}', alternatives=['trouve; no secure full alternative'], confidence='low', reason='The horizontal crossing obscures the joined middle letters.'),
        dict(place='Added word above the cancelled trouve', reading=r'\inserted{\unsure{écris}}', alternatives=['écris; ending partly lost at the scan edge'], confidence='medium', reason='The visible beginning supports écris, but the final small strokes meet the right image boundary.'),
        dict(place='Lower grouping stroke beneath the first surviving square product', reading=r'\unsure{\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty l_\infty^\alpha}}', alternatives=[r'\underbrace{\sigma_\infty l_\infty^\alpha l_0\sigma_\infty}l_\infty^\alpha','One long span or adjacent lower marks'], confidence='low', reason='The stroke extends to the last factor but has an internal upturn under the second sigma and a further curl; its grouping scope is not unambiguous.'),
        dict(place='Second index in the added and struck (=) inverse expression', reading=r'l_{\unsure{0|\infty}}^{-1}', alternatives=['0',r'\infty'], confidence='low', reason='The low outline has a broad curved form which can be read as one 0 with the preceding l foot or as a compact infinity. The expected inverse identity is not used to decide it.'),
        dict(place='Doubly cancelled prefix after live i.e.', reading=r'\deleted{\unsure{l_\infty^{-1}l_\infty}}', alternatives=[r'l_0^{-1}l_1',r'l_\infty^{-1}l_1'], confidence='low', reason='Both subscripts are crossed by a thick horizontal line. A downward trace supports 1 for the second, but full underlying forms remain obscured.'),
        dict(place='Word of the right marginal query', reading=r'\unsure{prends}', alternatives=['prenons'], confidence='medium', reason='The low middle and dark looped ending support prends provisionally but do not distinguish every terminal letter.'),
        dict(place='Overwritten value in the right marginal query', reading=r'\alpha=\unsure{2|1}', alternatives=['2','1'], confidence='low', reason='Overlapping upright, curved entry and lower foot do not separate a unique surviving digit.'),
    ],
    'inventory':inventory,
    'second_boxes':second_boxes,
    'notation':[
        {'observation':'The generator is written as a looped lower-case l with subscript 0, 1 or infinity. Its loop is part of the base letter; inverse exponents are separate raised minus and 1 strokes.', 'places':'All formulas; especially the rejected twelve-factor trial.', 'qualification':'Each factor in both trial products was read individually; no exponent is supplied from the intended cancellation.'},
        {'observation':'Epsilon and sigma have recurring curved forms, with small indices. A compact epsilon subscript in the interlinear square relation can look like either infinity or 0.', 'places':'Upper definitions, interlinear doit écrire formula, square computations and final system.', 'qualification':'The doubtful interlinear occurrence is left local and does not force the other clearly indexed occurrences to match it.'},
        {'observation':'The raised int(l_infinity^alpha) is an added right-hand operator factor in the first definition.', 'places':'Opening prose says multiplier à droite; upper formula contains the raised addition; later live epsilon expression.', 'qualification':'Its placement uses explicit same-page wording, not an independent algebraic proof.'},
        {'observation':'The barred m stands for même in the cancelled et de phrase.', 'places':'Cancelled lead-in above epsilon_0 and epsilon_1.', 'qualification':'The curved lower component distinguishes it from the equality-sign alternative in C.'},
        {'observation':'The small pi-shaped group sign appears in the prose g in pi and Aut(pi).', 'places':'Two-line Ecrivant passage.', 'qualification':'Retained as pi locally; no global Pi/pi ruling is inferred.'},
        {'observation':'The final system has a left brace; the intermediate lower strokes include both curved underbraces and a flat-ended bracket.', 'places':'Upper part of the surviving square computation, two lower-labelled rejected factors, final three definitions.', 'qualification':'The first long lower stroke has explicitly retained scope uncertainty.'},
    ],
    'hand':[
        {'habit':'Separate superscript inverses can remain clear above a horizontal cancellation even when the bases are crossed.', 'places':'Ninth and eleventh factors in the rejected twelve-factor trial.', 'universal_on_this_page':False, 'witness_effect':'C loses the ninth inverse; H loses the eleventh. Both are visible above the cancellation.'},
        {'habit':'Infinity can be compressed into a small left component adjoining a larger closed loop.', 'places':'Interlinear square relation after doit écrire.', 'universal_on_this_page':False, 'witness_effect':'C reads infinity, H reads 0; the local distinction remains uncertain.'},
        {'habit':'A dark cancellation may conceal an index while leaving a misleading vertical remnant.', 'places':'Generator index in the rejected epsilon_0 definition; the doubly crossed prefix after i.e.', 'universal_on_this_page':False, 'witness_effect':'The struck C doubts remain, instead of accepting H\'s unqualified indices.'},
        {'habit':'Revision state must be read locally: a cancelled row may have a live equals and an unstruck label below it.', 'places':'Third square-computation line and lower l_0l_infinity. annotation; final eight-factor cancellation.', 'universal_on_this_page':False, 'witness_effect':'C overextends the third-line deletion to its equals and lower label; H overextends the later cancellation through =1.'},
        {'habit':'Short forms and accents are locally distinct from full-word spellings.', 'places':'et de barred m; ss-groupe; unaccented Ecrivant.', 'universal_on_this_page':False, 'witness_effect':'H expands même and sous-groupe and adds an accent to Ecrivant.'},
        {'habit':'Final short words can reach the scanned edge and lose their last small strokes.', 'places':'Added écris above the crossed trouve.', 'universal_on_this_page':False, 'witness_effect':'C\'s doubt is retained; H omits the replacement and changes live je to on.'},
    ],
    'abbreviations':[
        {'form':r'$\bar m$', 'expansion':'même', 'place':'Cancelled et de phrase above the two cyclic definitions.'},
        {'form':'ss-groupe', 'expansion':'sous-groupe', 'place':'Ecrivant passage identifying pi with a subgroup of Aut(pi).'},
        {'form':'i.e.', 'expansion':'id est', 'place':'Upper action formulas; prose after g in pi; live lead-in before the doubly cancelled relation.'},
        {'form':'int', 'expansion':'intérieur, in the notation for inner conjugation', 'place':'Opening and upper operator formulas, Ecrivant passage, final parenthetical expression.'},
        {'form':'Aut', 'expansion':'automorphismes', 'place':'Aut(pi) in the prose.'},
    ],
    'notes':[
        'The author begins by saying that int(l_0)sigma_infinity fixes l_infinity, with the doubt phrase mais n\'est peut-être pas de carré l_infinity, and says to multiply on the right by int(l_infinity^alpha). Several preliminary definitions and computations are then cancelled or amended. The raised right-hand operator is preserved as an insertion, supported by the explicit opening instruction.',
        'The author next writes g in place of int(g), identifying pi with a subgroup of Aut(pi), and develops epsilon_infinity=l_0 sigma_infinity l_infinity^alpha. He computes a square, tries a further expansion which he cancels, and writes a condition obtained by multiplying by l_0l_1. The two lower factor labels remain attached to their rejected relation. These are descriptions of the written calculations, not independent mathematical verification.',
        'A right-margin query provisionally reads prends alpha=2|1 ?, with its word and overwritten numeral left uncertain. A twelve-factor trial is rejected with =1? Non !. In that cancelled trial both the ninth and eleventh l_1 factors have visible inverse exponents. The next eight factors are individually cancelled, while =1, OK and donc remain live. The final system gives epsilon_infinity=l_0 sigma_infinity l_infinity, epsilon_0=l_1 sigma_0 l_0, and epsilon_1=l_infinity sigma_1 l_1.',
        'Several visible irregularities are retained: the first upper action has epsilon_infinity l_0) with no opening parenthesis; the added struck inverse product has (=) before its factors rather than a closing parenthesis at the end, and its second generator index remains locally 0|infinity; two horizontally separated dots follow the inserted square relation. The compact epsilon subscript in the square insertion is left infinity|0, and the first long lower grouping stroke has uncertain scope. No mathematical expectation was used to repair these inscriptions.',
        'The lower l_0l_infinity. annotation and the equals to the left of its cancelled row are live. The separate inverse insertion above the following prose is struck. The upper curved revision/linking strokes are treated as connecting marks within the revised definition block, not as an independent mathematical diagram. The lower final brace groups the three surviving epsilon definitions.',
        'The indexed C mark M0802 is resolved on crop04. M0803–M0805 remain. Unlisted C marks are recorded in unlisted_decisions: barred m and l_0l_infinity are resolved from crops05 and10; the struck generator index, trouve, and the crossed prefix remain uncertain. Crop12 completely contains aussi but clips upper strokes of the following multipliant, which had been read on the native half; the later-reading box contains the complete sentence. No second first-reading crop was made.',
        'The handwritten page number is 12, at the lower left; no date or formula number is present. The source expresses uncertainty with peut-être, the marginal question, and the rejected =1? Non !. The wording and later OK are retained in their original states.',
        'All eighteen crops were reviewed by root during this first-pass reporting task, and the stated decisions and retained uncertainties were accepted. This reader performed no proof check or formal calculation and did not consult another page or external source.',
    ],
    'check_events':[],
    'diff_coverage':coverage,
}

assert len(diff_rows)==74
assert [x['row'] for x in coverage]==list(range(1,75))
assert all(c['c_changed'] or c['h_changed'] for c in changes)
mark_ids=[r['id'] for r in csv.DictReader((PACKET/'marks.tsv').open(), delimiter='\t')]
assert [d['id'] for d in decisions]==mark_ids
for entry in changes+decisions+unlisted_decisions:
    assert (ROOT/'edition'/entry['crop']).is_file(), entry['crop']
assert all(x['sheet_kind']=='text' and x['hand']=='his hand' and x['transcribed']=='yes' for x in inventory)
assert len({x['box'] for x in second_boxes})==len(second_boxes)
assert all(0 <= x['coords'][0] < x['coords'][2] <= 1677 and 0 <= x['coords'][1] < x['coords'][3] <= 2364 for x in second_boxes)
group_text=tex.replace(r'\{','').replace(r'\}','')
assert group_text.count('{')==group_text.count('}')
assert len(report['doubts'])==tex.count(r'\unsure{')

(OUT/'145_scan013.tex').write_text(tex)
(OUT/'145_scan013.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'scan':13, 'changes':len(changes), 'c_substantive_changes':sum(c['c_changed'] for c in changes), 'indexed_decisions':len(decisions), 'unlisted_decisions':len(unlisted_decisions), 'doubts':len(report['doubts']), 'inventory':len(inventory), 'second_boxes':len(second_boxes), 'crops':len(crop_boxes), 'diff_rows':len(coverage)}, ensure_ascii=False))
