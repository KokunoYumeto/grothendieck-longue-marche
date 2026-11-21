from pathlib import Path
import json, re

ROOT = Path('/workspace/scratch/481648fc487b')
WORK = ROOT / 'SP90_C13_150_work'
PACKET = ROOT / 'reader_packets/150_scan048'
OUT = WORK / 'reader_returns'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
T = (OUT / '150_scan048.tex').read_text()

def crop(name):
    return f'150_scan048_{name}.jpg'

def box(name):
    return json.loads((WORK / 'crops' / f'150_scan048_{name}.json').read_text())['box']

changes = []
def change(place, c, h, final, evidence, name, confidence, kind, error_kind,
           change_C=False, change_H=False, marked_in_H=False, consequential=''):
    changes.append(dict(place=place, C=c, H=h, final=final, evidence=evidence,
                        crop=crop(name), box=box(name), confidence=confidence,
                        kind=kind, error_kind=error_kind, marked_in_H=marked_in_H,
                        change_C=change_C, change_H=change_H,
                        consequential=consequential))

change('line 1 / parenthesis after lissité',
       'à tous les coups', r'\ill{} \ill{} \ill{}', 'à tous les coups',
       'The accented initial à, tall crossed t, low ous run, looped l, and final c-ou-p-s sequence are visible. The p descends and the final s has a short angular turn. The whole parenthesis is readable; no words are supplied from the subject matter.',
       'coups_cancel', 'high', r'readable ink left as \ill{}', 'readable ink left as illegible',
       change_H=True, marked_in_H=True)

change('line 2 / continuation of the opening index sequence',
       r'i_p\ i_{p+1}--i_n', r'i_p\,i_{p+1}\ldots i_n',
       r'i_p\ i_{p+1}-\, -\,i_n',
       'Two separate short horizontal strokes occur after i_(p+1). There are no three points and no comma between the first two terms. The low 1 after the small plus is retained. Spacing the two existing C dashes is encoding only.',
       'top_indices', 'high', 'misread symbol or index', 'symbols and indices',
       change_H=True)

change('line 3 / two raised additions and their attachments',
       r'chaque terme \inserted{(sauf le premier)} est successeur \inserted{dans $I$} du précédent.',
       r'chaque terme est \add{(\uncertain{le plus proche}, au sens de $I$)} successeur du précédent.',
       r'chaque terme \inserted{(sauf le premier)} est successeur \inserted{dans $I$} du précédent.',
       'The first raised group is parenthesized and begins with the s-au-f run and a long f; le premier follows. Its curved lower leader ends in the gap after terme, before est. A separate raised dans I, with the serifed capital I, is above the gap after successeur and has its own low curved leader. There is no independent plus proche or au sens de wording.',
       'top_insertions', 'high', 'insertion or placement', 'insertion placement',
       change_H=True, marked_in_H=True,
       consequential='The first term is excepted, and the successor condition is expressly in I; H attaches and reads the additions differently.')

change('line 5 / underlined section title',
       r'11. \uline{Digression : où on laisse tomber} $I$.',
       r'\emph{11. Digression : \ill{} \uncertain{cas} \ill{} \ill{}} $I$.',
       r'11. \uline{Digression : où on laisse tomber} $I$.',
       'After the single colon come the grave-accented où, low on, tall looped l of laisse, and the t-o-m-b-er run. One continuous underline runs beneath Digression through tomber; 11 and I lie outside that line. H separately notes that the title is underlined, so the underline itself is not counted as absent.',
       'heading', 'high', r'readable ink left as \ill{}', 'readable ink left as illegible',
       change_H=True, marked_in_H=True)

change('line 6 / first abbreviation ens.',
       'Soit donné un ens. ordonné', 'Soit donné un ensemble \\uncertain{ordonné}',
       'Soit donné un ens. ordonné',
       'The short ens group ends in a distinct baseline dot before ordonné. No emble continuation is written. The ordonné certainty difference alone is not counted.',
       'ens_cancelled', 'high', 'abbreviation expanded or spelling modernised', 'abbreviation/spelling',
       change_H=True)

change('left margin beside On suppose / narrowed wording',
       r'\unsure{On retient ce cas}', r'\ill{} \uncertain{autres} \ill{}',
       r'On retient \unsure{ce} cas',
       'On begins with a round O and low n; the following group has the r/e entry, a conspicuous crossed t and a low continuing run compatible with retient. The next short ce group is compressed and remains doubtful. The separate lower cas is legible. The longer lower loop at the right belongs to main-text le, not to the margin note. C’s broad doubt is narrowed, not silently removed.',
       'margin_note', 'medium', 'misread word', 'words',
       change_C=True, change_H=True, marked_in_H=True)

change('line 13 / parenthetical conclusion of condition a',
       '(donc finie)', r'(\uncertain{à fibres finies})', '(donc fini)',
       'The full completion shows a d-o-n-c run, a tall f with a long lower loop, then the low i-n-i run with a final detached i dot. A blank gap separates the terminal i from the closing parenthesis; no separate e follows it. The broad map crop had clipped the f descender, which is why one completion was made.',
       'donc_finie_complete', 'high', 'misread word', 'words',
       change_C=True, change_H=True, marked_in_H=True,
       consequential='The written conclusion is donc fini; no replacement by a fibres-finiteness formulation is made.')

change('line 14 left / crossed circled b',
       r'\deleted{\textcircled{b}}', r'(b)\note{« b » cerclé, surchargé.}',
       r'\deleted{\textcircled{b}}',
       'A small b with stem and lower loop is enclosed and crossed by several oblique strokes. The transcription treats the crossed label as cancelled. H does explicitly describe both the enclosure and surcharge; the difference recorded here is its live label encoding, not an omission of the observed crossings.',
       'label_b', 'high', 'deletion state (struck given live or live given struck)', 'struck text',
       change_H=True, marked_in_H=True)

change('line 16 / first superscript on Sigma',
       r'\Sigma^{<}(1)',
       r"\Sigma^{*}(1)$\note{l'exposant, une petite étoile ou un point épais, est lu $*$ ; il distingue ces espaces de drapeaux stricts de $\Sigma(0)$, $\Sigma(1)$, et de l'indice $\Sigma_{*}$ des pages précédentes.}",
       r'\Sigma^{<}(1)',
       'The superscript has an angular left point and two arms, with a small entry/retrace near the left point. It is less clean than the next < but does not have the multiple independent rays of the later star. The following parenthesized digit is the hooked 1. H’s exact explanatory note is retained as evidence rather than treated as manuscript text.',
       'first_decoration', 'medium', 'misread symbol or index', 'symbols and indices',
       change_H=True, marked_in_H=True,
       consequential='The first strict-relation object is literally written with <; the later star is preserved separately.')

change('line 17 / punctuation of the lower i.e abbreviation',
       r"l'image, i.e. l'ens", r"l'image, i.e.\ l'ens.",
       r"l'image, i.e l'ens",
       'The lower abbreviation has an internal small stop and the low e stroke, followed by blank space before l’ens. No detached terminal stop is visible there. This local punctuation differs from the clearer fully stopped i.e. in the opening and introductory lines.',
       'ens_inequalities', 'medium', 'text not on the page', 'text not on page',
       change_C=True, change_H=True)

change('line 17 / extra linked words after l’ens',
       r"l'ens \unsure{où} une des inégalités", r"l'ens.\ des inégalités",
       r"l'ens où \unsure{une|on a} des inégalités",
       'After l’ens there is a detached short accented group read où, then an independently written low linked group before des. The latter is compatible with une or tightly joined on a; the ink does not settle it. H omits both groups and supplies a full stop immediately after ens. No detached stop is present at that location. The awkward wording is not regularized by choosing the mathematically smoother alternative.',
       'ens_inequalities', 'medium', 'omission', 'omissions',
       change_C=True, change_H=True,
       consequential='The possible connective wording remains unresolved; H’s shorter wording does not exhaust the visible ink.')

change('line 18 / second superscript on Sigma',
       r'\Sigma^{<}(n)', r'\Sigma^{*}(n)', r'\Sigma^{<}(n)',
       'The small superscript consists of two oblique arms meeting at a left point, with no crossing rays. The contrast with the subsequent multi-rayed star is directly visible.',
       'second_decoration', 'high', 'misread symbol or index', 'symbols and indices',
       change_H=True,
       consequential='The definition of flag spaces uses < locally, despite the later star.')

change('line 19 / literal continuation in the strict flag',
       r'i_0<i_1--<i_n', r'i_0<i_1<\cdots<i_n',
       r'i_0<i_1-\, -\,<i_n',
       'After i_1 there are exactly two headless short horizontal strokes followed by one < before i_n. No separate < precedes the two dashes. The initial i has a long leftward entry; the zero is a low closed loop and the following 1 has a hooked top and heavy low foot.',
       'strict_chain', 'high', 'misread symbol or index', 'symbols and indices',
       change_H=True)

change('line 20 / isolated stop after Les',
       r'Les $\Sigma^{\unsure{*|<}}(n)$', r'Les $\Sigma^{*}(n)$',
       r'Les. $\Sigma^*(n)$',
       'A separate dark baseline point lies after the final s of Les and before Sigma, around original coordinate (973,2068). It is neither part of the Sigma nor a letter dot. The following superscript is addressed separately, so only the added manuscript stop is counted in this row.',
       'forment_cancel', 'high', 'omission', 'omissions',
       change_C=True, change_H=True)

change('line 20 / third superscript on Sigma',
       r'\Sigma^{\unsure{*|<}}(n)', r'\Sigma^{*}(n)', r'\Sigma^*(n)',
       'Several thick short rays cross at the superscript’s centre. This is visibly a heavier multi-rayed star, unlike the two earlier angular < signs. C’s first candidate is selected from the ink rather than by imposing consistency.',
       'forment_cancel', 'high', 'misread symbol or index', 'symbols and indices',
       change_C=True,
       consequential='The local < / < / * variation is retained.')

change('line 20 / raised forment above cancelled word',
       r'\deleted{\unsure{sont}} \unsure{forment}',
       r'\struck{\ill{}} \uncertain{forment}',
       r'\deleted{\unsure{sont}} \inserted{forment}',
       'The live upper word has a tall f with returning hook, followed by o/r and a connected low m-en-t run. It lies above the long horizontal strike through the lower word, so it is encoded as a replacement insertion. The heavily covered lower word remains only tentatively sont and is not claimed fully recovered from H’s illegible span.',
       'forment_cancel', 'medium', 'insertion or placement', 'insertion placement',
       change_C=True, change_H=True, marked_in_H=True)

change('line 21 / NB at start of parenthesis',
       r"(\uline{NB} pas d'applications", r"(pas d'applications",
       r"(\uline{NB} pas d'applications",
       'The parenthesis is followed by distinct capital N and B strokes with a short independent underline below them. These precede pas; the letters are not a flourish of the parenthesis.',
       'presimplicial', 'high', 'omission', 'omissions', change_H=True)

change('line 23 / three continuation marks after Sigma(n)',
       r'\Sigma(n)\ldots', r'$\Sigma(n)$\ldots',
       r'\Sigma(n)\mathinner{\cdotp\cdotp-}',
       'There are three separated continuation marks: two small point-like strokes and a third distinctly wider horizontal stroke. The closing prose parenthesis and its following full stop are separate. The transcription preserves the point-point-dash sequence rather than drawing three equivalent points.',
       'ending', 'high', 'misread symbol or index', 'symbols and indices',
       change_C=True, change_H=True)

change('bottom left / separate thin foliation 47',
       r'\mspage{47}', r'\note{Suite de la page 46, sans numéro de sa main.}',
       r'\margin{47}',
       'Thin grey digits 4 and 7 sit at the lower-left edge. The 4 has an angular lower return and the 7 a horizontal top with a crossed descending stroke. The hand/material differs from the broad main text; attribution is uncertain. H’s note about no number in his hand does not transcribe this separate visible 47. C’s numeral itself is unchanged; the macro adjustment avoids asserting an authorship not established by this image.',
       'folio47', 'high', 'omission', 'omissions', change_H=True)

marks = [
    dict(mark=r'\unsure{pour|$i_p$}', context=r'ssi \deleted{\unsure{pour|$i_p$}} la suite',
         decision='undecided', reading=r'\unsure{$i_p$|pour}',
         evidence='A compact initial stroke and a lower p-like remainder survive the heavy strike. A putative i dot/body is not independently secure enough to exclude pour. The candidates are reordered, not declared resolved.',
         crop=crop('coups_cancel'), box=box('coups_cancel'), confidence='low'),
    dict(mark=r'\unsure{On retient ce cas}', context=r'\margin{\unsure{On retient ce cas}}',
         decision='other', reading=r'On retient \unsure{ce} cas',
         evidence='The rotated note gives clear On, the crossed t and low continuation of retient, and the separate cas. The short intervening ce remains compressed; the large lower-right loop is neighboring main-text le.',
         crop=crop('margin_note'), box=box('margin_note'), confidence='medium'),
    dict(mark=r'\unsure{où}', context=r"l'ens \unsure{où} une des inégalités",
         decision='first', reading='où',
         evidence='The short group after ens has the separated initial oval/point, low following stroke and small upper accent seen in the other où of this leaf. The next low linked group is a separate word group and is retained as une|on a uncertain.',
         crop=crop('ens_inequalities'), box=box('ens_inequalities'), confidence='medium'),
    dict(mark=r'\unsure{*|<}', context=r'Les $\Sigma^{\unsure{*|<}}(n)$',
         decision='first', reading='*',
         evidence='The raised glyph has several crossing thick rays; it is not the two-armed angular sign seen twice earlier.',
         crop=crop('forment_cancel'), box=box('forment_cancel'), confidence='high'),
    dict(mark=r'\unsure{sont}', context=r'\deleted{\unsure{sont}} \unsure{forment}',
         decision='undecided', reading=r'\unsure{sont}',
         evidence='The long heavy stroke covers nearly the whole lower baseline. Small surviving low turns are compatible with sont, but the complete letter sequence cannot be independently recovered.',
         crop=crop('forment_cancel'), box=box('forment_cancel'), confidence='low'),
    dict(mark=r'\unsure{forment}', context=r'\deleted{\unsure{sont}} \unsure{forment} un espace',
         decision='first', reading='forment',
         evidence='The upper live group has an unmistakable tall f, small rounded next turn and low connected continuation ending in a t-like return. Its vertical displacement above the cancelled baseline is clear; the compressed middle letters are readable at medium confidence.',
         crop=crop('forment_cancel'), box=box('forment_cancel'), confidence='medium'),
    dict(mark=r'\unsure{car par}', context=r'\deleted{\unsure{car par}} ils sont',
         decision='undecided', reading=r'\unsure{car par}',
         evidence='The initial c-like loop and a following lower p-like descender survive, but a thick horizontal strike covers the intermediate and final bodies. No full recovery is claimed.',
         crop=crop('car_cancel'), box=box('car_cancel'), confidence='low')
]

inventory = []
def item(element, kind, position, first, hand='his hand'):
    inventory.append(dict(element=element, kind=kind, position=position,
                          first_words_or_objects=first, sheet_kind='text',
                          hand=hand, transcribed='yes'))

item('T01','text','top, main lines 1–4','On a lissité (à tous les coups) ssi … du précédent.')
item('D01','deletion','line 1, after ssi',r'\unsure{$i_p$|pour}')
item('F01','display','line 2, within opening prose',r'i_p\ i_{p+1}-\, -\,i_n; à partir de i_p, pas de i_1')
item('I01','insertion','above line 3, leader after terme','(sauf le premier)')
item('I02','insertion','above line 3, leader after successeur',r'dans I')
item('T02','text','line 5, section heading','11. Digression : où on laisse tomber I.; title underline ends before I')
item('T03','text','lines 6–11','Soit donné un ens. ordonné topologique … On suppose')
item('D02','deletion','line 7, between un and ens. ordonné','espace topologique')
item('F02','display','line 7, within prose',r'\Sigma=\Sigma(0),\Sigma(1)')
item('F03','display','lines 8–9, within prose',r'\Sigma(0),\Sigma(1);\Sigma(0)\times\Sigma(0)')
item('M01','margin note','left margin, diagonally rising, beside On suppose',r'On retient \unsure{ce} cas')
item('T04','text','lines 12–13, condition a','circled a; est une immersion localement bordante, et propre (donc fini)')
item('F04','display','line 12, within condition a',r'\Sigma(1)\xrightarrow{but}\Sigma(0)')
item('D03','deletion','left of line 14','crossed circled b')
item('T05','text','lines 14–16','Cela implique que … un isomorphisme sur une partie ouverte et fermée.')
item('F05','display','line 14, within prose',r'\Sigma(0)\xrightarrow{diag}\Sigma(1)')
item('T06','text','lines 16–18',r'Soit \Sigma^{<}(1) le complémentaire … où \unsure{une|on a} des inégalités strictes i<j.')
item('T07','text','lines 18–20',r'On désigne par \Sigma^{<}(n) l’espace des drapeaux stricts … de longueur n.')
item('F06','display','line 19, within prose',r'i_0<i_1-\, -\,<i_n; stricts underlined')
item('T08','text','lines 20–23',r'Les. \Sigma^*(n) … un espace pré-semi-simplicial (NB …). Si on a un')
item('D04','deletion','line 20, lower baseline after Sigma-star',r'\unsure{sont}')
item('I03','insertion','line 20, raised over cancelled sont','forment')
item('I04','insertion','line 21, raised before cancelled semi','pré')
item('D05','deletion','line 21, before -simplicial','semi')
item('T09','text','line 21, start of parenthesis','underlined NB, then pas d’applications')
item('D06','deletion','line 22, after dégénérescence',r'\unsure{car par}')
item('F07','display','line 23, within prose',r'\Sigma(n)\mathinner{\cdotp\cdotp-}')
item('D07','deletion','line 23, between closing parenthesis and Si',r'\unsure{\deleted{Les}|Les}; deletion state uncertain')
item('M02','margin note','extreme lower-left corner','47','thin separate foliation; attribution uncertain')

doubts = [
    dict(place='line 1 / cancelled token after ssi', reading=r'\deleted{\unsure{$i_p$|pour}}',
         alternatives='i_p; pour; cancellation obscures the initial independent strokes',confidence='low'),
    dict(place='left marginal note / short word before cas',reading=r'On retient \unsure{ce} cas',
         alternatives='ce is the candidate; its short compressed strokes remain uncertain',confidence='medium'),
    dict(place='line 17 / linked group between où and des',reading=r"l'ens où \unsure{une|on a} des inégalités",
         alternatives='une; tightly linked on a',confidence='medium'),
    dict(place='line 20 / cancelled lower word',reading=r'\deleted{\unsure{sont}}',
         alternatives='sont remains a tentative recovery beneath the heavy strike',confidence='low'),
    dict(place='line 22 / cancelled group',reading=r'\deleted{\unsure{car par}}',
         alternatives='car par remains tentative; first loop and lower descender survive but intermediate bodies are covered',confidence='low'),
    dict(place='line 23 / terminal Les before Si',reading=r'\unsure{\deleted{Les}|Les}',
         alternatives='cancelled Les; live Les with a long low connecting stroke',confidence='medium')
]

notes = [
    'The opening reports a smoothness criterion: the tail beginning at i_p is strict and each term except the first is a successor in I of the preceding term. This is a report of the manuscript, not a proof check.',
    'Section 11 is an explicitly titled digression in which I is dropped. The page describes a topological ordered set by its space of elements and closed order-relation graph, assumes a locally boundary-immersive proper target map, and states that the diagonal is an isomorphism onto an open-and-closed part. It then introduces strict flags and calls their spaces pre-simplicial without degeneracy maps. None of these claims was independently proved in this reading.',
    'The first two strict-flag superscripts are angular < signs; the third is a multi-rayed star. The visible variation is retained rather than harmonized. The isolated stop after Les is also retained even though it leaves awkward punctuation.',
    'The lower explanation contains visible où and a second linked word group before des. The latter remains une|on a uncertain; expected grammar or mathematics is not used to decide it. The lower i.e has no independently visible final stop.',
    'The cancelled words sont and car par remain doubtful. The opening cancelled token remains i_p|pour uncertain. The final word Les is legible but its deletion state is uncertain: its long low line nearly coincides with the normal connecting baseline.',
    'Each of the two top additions has a curved placement leader. The first is attached after terme, the second after successeur. Raised forment replaces the struck lower word; raised pré replaces struck semi. No separate underline is inferred from the placement leaders.',
    'The right end of localement reaches the scan edge; its surviving body and final strokes support the reading, without supplying additional text beyond the edge. The introductory and concluding grammatical continuations are left as written; the page ends at Si on a un.',
    'The lower-left 47 is thin separate foliation. Attribution to the author is uncertain, so it is represented as a marginal numeral rather than asserted to be his page number. H’s editorial note refers to the preceding page but does not transcribe this visible numeral.',
    'Main-line count is 23, excluding the separately raised insertions, diagonal marginal note and thin foliation. The whole image and each existing native half were viewed once. Nineteen distinct crop places were made and every crop was viewed; the map-parenthesis place has one completion because the broad crop clipped the f descender, giving twenty saved images total.',
    'H’s editorial wording about the title underline, the circled/surcharged labels and the first star interpretation was treated as evidence. Editorial explanations are not inserted into the transcription. H uncertainty on ordonné and isomorphisme is certainty-only and is not separately counted; retained tentative cancelled readings versus H illegibility are documented in marks rather than claimed as recovered text.'
]

notation = [
    dict(form=r'\Sigma^{<}(1),\ \Sigma^{<}(n),\ \Sigma^*(n)',
         meaning_or_shape='The first two superscripts are angular left-pointing two-armed signs, the first retraced; the third has several crossing rays. The page uses them for strict-relation/flag spaces but does not explain this local shape change.',
         places='lines 16, 18, 20'),
    dict(form=r'i_p\ i_{p+1}-\, -\,i_n;\quad i_0<i_1-\, -\,<i_n',
         meaning_or_shape='Two distinct short horizontal continuation strokes in each sequence; no extra comparison sign immediately after i_1 in the second sequence.',
         places='lines 2, 19'),
    dict(form=r'\mathinner{\cdotp\cdotp-}',
         meaning_or_shape='Three continuation marks: two points followed by a short horizontal mark.',
         places='line 23 after Sigma(n)'),
    dict(form=r'\Sigma(0),\ \Sigma(1)',
         meaning_or_shape='Parenthesized argument 0 is a small oval, sometimes heavily retraced. Argument 1 has a hooked top and a low foot. Sigma’s separate-looking upper cap belongs to its letter.',
         places='introductory definition and but/diag maps'),
    dict(form=r'\xrightarrow{\mathrm{but}},\ \xrightarrow{\mathrm{diag}}',
         meaning_or_shape='Single rightward shafts with short terminal heads and small labels above. The labels are written but and diag.',
         places='lines 12, 14'),
    dict(form='I', meaning_or_shape='Serifed capital I with separate upper and lower horizontal bars; the successor condition is explicitly dans I.',
         places='top insertion, heading')
]

abbreviations = [
    dict(form='ssi',expansion='si et seulement si'),
    dict(form='ens.',expansion='ensemble'),
    dict(form="l'ens",expansion="l’ensemble; no final abbreviation stop is visible in this occurrence"),
    dict(form='i.e.; i.e',expansion='id est; the lower occurrence lacks a detached final stop'),
    dict(form='diag',expansion='diagonale'),
    dict(form='NB',expansion='nota bene')
]

hand_log = [
    dict(habit='Low word bodies are frequently reduced to one linked horizontal run, while tall letters retain conspicuous loops or descenders.',
         places='laisse tomber; On retient; forment; où une|on a',
         consistent='These compressions recur in the observed main and marginal text; the most compressed linked group remains doubtful.',
         witness_errors='H loses the title, reads the margin as autres, and omits the extra lower groups.'),
    dict(habit='Small 1 can have a hooked top and heavy low foot; 0 can be filled or retraced.',
         places='Sigma(0)/Sigma(1), strict flag i_0<i_1, top i_(p+1)',
         consistent='The repeated forms support the numeral readings, without changing any candidate from mathematical expectation.',
         witness_errors='No numeral correction established on this page.'),
    dict(habit='Short continuation marks vary between dashes and points within the same leaf.',
         places='opening index sequence, strict flag, final Sigma(n)',
         consistent='Two dashes in each sequence; two points and one dash at the end.',
         witness_errors='H normalizes both sequences to ellipses; C and H normalize the final mixed three marks to dots.'),
    dict(habit='Raised replacement words may have curved attachment leaders; cancellation strokes can obscure the whole lower letter body.',
         places='top sauf le premier and dans I; raised forment; pré/semi; car par',
         consistent='All observed additions and strikes inspected separately. The terminal Les is an exception whose state remains uncertain.',
         witness_errors='H merges the two top additions and both witnesses omit raised status for forment; no full recovery of struck sont/car par is claimed.'),
    dict(habit='Strict-space superscripts change visibly from two-armed < to a thicker multi-rayed star.',
         places='three Sigma strict-space occurrences',
         consistent='First two <; third *; local inconsistency preserved.',
         witness_errors='H homogenizes to stars; C doubts the final form.'),
    dict(habit='A separate thin grey foliation differs materially from the broad dark main writing.',
         places='lower-left 47',
         consistent='Only this foliation is visible on the assigned leaf; no author attribution inferred.',
         witness_errors='H omits the numeral; C’s numeral retained with neutral marginal treatment.')
]

second_boxes = []
def second(number, kind, coords, reading, reason):
    second_boxes.append(dict(box=f'b{number:02}',kind=kind,coords=coords,reading=reading,reason=reason))

second(1,'struck passage; insertion; doubt formula; handwritten number; C/H word difference; low-confidence departure',
       [315,45,1630,390],
       r'On a lissité (à tous les coups) ssi \deleted{\unsure{$i_p$|pour}} la suite $i_p\ i_{p+1}-\, -\,i_n$ (à partir de $i_p$, pas de $i_1$ !) est stricte, i.e. chaque terme \inserted{(sauf le premier)} est successeur \inserted{dans $I$} du précédent.',
       'Complete opening paragraph: cancelled token, both additions and leaders, all index digits and the full index sequence, and all opening word disagreements.')
second(2,'handwritten number; C/H word difference',[345,455,1505,565],
       r'11. \uline{Digression : où on laisse tomber} $I$.',
       'Both heading digits, complete disputed title, its underline extent and final I.')
second(3,'C/H word difference',[400,592,1535,696],
       'Soit donné un ens. ordonné topologique, i.e.',
       'Complete line containing the written ens. abbreviation expanded by H; ordonné itself is not a textual disagreement.')
second(4,'struck passage; handwritten number',[325,685,1660,778],
       r'un \deleted{espace topologique} ens. ordonné $\Sigma=\Sigma(0),\Sigma(1)$,',
       'Complete cancelled phrase and complete defining tuple with both parenthesized digits.')
second(5,'handwritten number',[325,777,1590,870],
       r'où $\Sigma(0)$ est un espace topologique, $\Sigma(1)$ une',
       'Both numerical arguments in the next complete main line.')
second(6,'handwritten number',[320,878,1565,987],
       r'partie fermée de $\Sigma(0)\times\Sigma(0)$, qui soit',
       'Complete product formula with both zeros, including the retraced first one.')
second(7,'margin note; C/H word difference; low-confidence departure',[28,968,414,1269],
       r'On retient \unsure{ce} cas',
       'Entire diagonally written margin note, including the lower cas; neighboring main-line le and circled a are context, not duplicated note words.')
second(8,'handwritten number; C/H word difference',[333,1183,1680,1360],
       r'\textcircled{a}\quad $\Sigma(1)\xrightarrow{\mathrm{but}}\Sigma(0)$ est une immersion localement bordante, et propre (donc fini)',
       'Whole condition a: full labelled map and both digits, edge-reaching localement, complete disputed final parenthesis including the f descender.')
second(9,'struck passage',[315,1350,425,1458],
       r'\deleted{\textcircled{b}}',
       'Entire crossed and circled label; H’s explicit surcharge note is acknowledged.')
second(10,'handwritten number',[487,1352,1598,1460],
       r'Cela implique que $\Sigma(0)\xrightarrow{\mathrm{diag}}\Sigma(1)$ est',
       'Complete labelled diagonal map and both numerical arguments.')
second(11,'handwritten number; low-confidence departure',[340,1478,1620,1685],
       r'un isomorphisme sur une partie ouverte et fermée. Soit $\Sigma^{<}(1)$ le complémentaire de',
       'Complete first decorated Sigma expression with its retraced < and parenthesized 1; H’s first-star reading differs.')
second(12,'C/H word difference; low-confidence departure',[340,1688,1638,1891],
       r"l'image, i.e l'ens où \unsure{une|on a} des inégalités strictes $i<j$. On désigne par $\Sigma^{<}(n)$",
       'Complete disputed explanation, both mathematical expressions, lower abbreviation punctuation and second superscript; no grammatical completion supplied.')
second(13,'handwritten number',[380,1903,1662,1998],
       r"l'espace des drapeaux \uline{stricts} $i_0<i_1-\, -\,<i_n$",
       'Entire strict flag with digits 0 and 1, exact two-dash continuation, comparison signs and adjacent underlined word.')
second(14,'struck passage; insertion; doubt formula; low-confidence departure',[390,1996,1652,2117],
       r'de longueur $n$. Les. $\Sigma^*(n)$ \deleted{\unsure{sont}} \inserted{forment} un',
       'Complete line: third Sigma superscript originally doubtful in C, full cancelled word, raised replacement, and isolated point after Les.')
second(15,'struck passage; insertion; C/H word difference',[385,2097,1635,2208],
       r"espace \inserted{pré}\deleted{semi}-simplicial (\uline{NB} pas d'applications",
       'Whole pré/semi replacement with the accent, hyphen, opening parenthesis and omitted underlined NB.')
second(16,'struck passage; low-confidence departure',[390,2193,1595,2345],
       r'de dégénérescence, \deleted{\unsure{car par}} ils sont dans les $\Sigma(n)\mathinner{\cdotp\cdotp-}$). \unsure{\deleted{Les}|Les} Si on a un',
       'Both remaining cancelled-or-possibly-cancelled groups, complete final Sigma expression and exact continuation mark sequence, closing punctuation and unfinished sentence.')
second(17,'margin note; handwritten number',[20,2297,87,2348],
       '47',
       'Complete thin lower-left foliation with both digits.')

data = dict(scan=48,reader='reader_b',line_count=23,changes=changes,marks=marks,
            inventory=inventory,doubts=doubts,notes=notes,check_events=[],
            notation=notation,abbreviations=abbreviations,hand_log=hand_log,
            second_boxes=second_boxes)

def macros(text, name):
    ans=[]
    for m in re.finditer(re.escape('\\'+name+'{'),text):
        start=m.start(); i=m.end(); depth=1
        while i<len(text) and depth:
            if text[i]=='{' and (i==0 or text[i-1]!='\\'): depth+=1
            elif text[i]=='}' and (i==0 or text[i-1]!='\\'): depth-=1
            i+=1
        assert depth==0
        ans.append(text[start:i])
    return ans

expected=macros(C,'unsure')+macros(C,'illegible')
assert [m['mark'] for m in marks]==expected, (expected,[m['mark'] for m in marks])
for m in marks:
    assert m['context'] in C,m['context']
for row in changes:
    assert row['C'] in C,('C snippet missing',row['place'],row['C'])
    assert row['H'] in H,('H snippet missing',row['place'],row['H'])
    assert row['final'] in T,('Final snippet missing',row['place'],row['final'])
for row in changes+marks:
    assert (WORK/'crops'/row['crop']).exists(),row['crop']
for b in second_boxes:
    x0,y0,x1,y1=b['coords']
    assert 0<=x0<x1<=1690 and 0<=y0<y1<=2361,b
depth=0
for i,ch in enumerate(T):
    if ch=='{' and (i==0 or T[i-1]!='\\'):depth+=1
    elif ch=='}' and (i==0 or T[i-1]!='\\'):depth-=1
    assert depth>=0
assert depth==0
assert len(list((WORK/'crops').glob('150_scan048_*.jpg')))==20
(OUT/'150_scan048.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(changes=len(changes),change_C=sum(x['change_C'] for x in changes),
                      change_H=sum(x['change_H'] for x in changes),marks=len(marks),
                      resolved_or_reassigned_marks=sum(x['decision']!='undecided' for x in marks),
                      inventory=len(inventory),doubts=len(doubts),second_boxes=len(second_boxes),
                      crop_places=19,crop_images=20),ensure_ascii=False))
