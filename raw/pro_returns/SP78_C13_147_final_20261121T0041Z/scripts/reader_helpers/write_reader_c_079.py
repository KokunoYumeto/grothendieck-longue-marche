from pathlib import Path
import json
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/ea90d891106a')
WORK = ROOT / 'SP78_C13_147_work'
OUT = WORK / 'reader_returns/147_scan079'
OUT.mkdir(parents=True, exist_ok=True)
meta = json.loads((ROOT / 'runtime/reader_c_079_crops.json').read_text())
qopen = chr(96) * 2
qclose = "''"
quoted_infini = qopen + "l'infini" + qclose

second_opening = r'\overset{\unsure{\deleted{\wedge}}}{M}{}^*_{\underline G,\underline G\prime}'
# Use the same literal prime convention as the packet everywhere.
second_opening = second_opening.replace(r'\underline G\prime', r"\underline G'")
first_gamma = r"\unsure{\Gamma^!_{\underline G,\underline G'}}"
canceled_mprime = r"\unsure{\widehat M_{\underline G'}}"
canceled_tuple = r"\unsure{(\widehat M_{\underline G},\Gamma^!_{G,G'})}"
inserted_m = r'\widehat M_{\unsure{\underline G|G}}'
first_100 = r"\Pi M^{\unsure{*}}_{\underline G,\underline G'}"
du_connexe = r'\unsure{du connexe}'
first_ou = r'\unsure{ou}'
final_preposition = r'\unsure{à|:}'

opening = (r"Je désigne par $\widehat M^*_{\underline G,\underline G'}$, $" + second_opening
           + r"$ les germes de multiplicités obtenus en")
deleted_main = (r'\deleted{enlevant (' + quoted_infini
                + r") $\widehat M_{\underline G}$ resp. $M_{\underline G}$, $" + first_gamma
                + r"$ (les traces de la \unsure{réunion} des diviseurs de $" + canceled_mprime
                + r"$ \unsure{qui contiennent} $" + canceled_tuple + r"$)}")
trial = r'\deleted{\unsure{prenant les traces de} $M$}'
insert = (r'\inserted{' + trial
          + r" enlevant les traces des diviseurs à l'infini de $\widehat M_{\underline G'}$ "
          + r'\deleted{\unsure{non seuls}} qui contiennent $' + inserted_m
          + r"$ -- dans le cas de $M^*_{\underline G,\underline G'}$, on prend la \uline{trace} de $M_{\underline G'}$ sur $\widehat M_{\underline G,\underline G'}$}")
filter_sentence = (r"Ils sont donc des filtres d'ouverts de la multiplicité $M_{G'}$, "
                   r"et les groupoïdes fondamentaux* \deleted{$\unsure{\Pi}$}")
display100 = (r'\[' + '\n' + r'(100)\qquad' + first_100
              + r",\qquad\Pi M^*_{\underline G,\underline G'}" + '\n' + r'\]')
categories = (r"sont définis comme des Catégories $\underset{\longrightarrow}{\lim}$ des catégories de revêtements universels, "
              + first_ou + r' ou comme des catégories des revêtts ' + du_connexe
              + r" desdits germes de multiplicités (comparer [5], n°5, p. $768'$).")
diagram_intro = 'On a alors des diagrammes de germes de multiplicités analytiques'
diagram101 = r'''\diagram{\begin{tikzpicture}[x=1cm,y=1cm]
\node[inner sep=2pt] (A) at (0,0) {$M^*_{\underline G,\underline G'}$};
\node[inner sep=2pt] (B) at (4,0) {$M_{\underline G'}\deleted{\unsure{M}}$};
\node[inner sep=2pt] (C) at (-2.6,-2) {$(M_{\underline G}\deleted{\unsure{,\Gamma^!}})$};
\node[inner sep=2pt] (D) at (0,-2) {$M_{\underline G,\underline G'}$};
\draw[line cap=round] ([xshift=4pt]A.east) -- ([xshift=-8pt]B.west);
\draw[->] ([yshift=-5pt]A.south) -- ([yshift=5pt]D.north);
\draw[->] (C.east) -- (D.west);
\node[anchor=east] at (-3.75,-1.05) {$(101)$};
\node[anchor=north west,inner sep=0pt] (caption) at (-1.65,-2.55) {(équiv d'homotopie !)};
\node[anchor=base west,inner sep=0pt] at ([xshift=5pt,yshift=5pt]caption.north east) {$\unsure{)}$};
\end{tikzpicture}}'''
last = 'donnant lieu ' + final_preposition + ' des morphismes de groupoïdes'
proposed = (r'\scanpage{79}' + '\n' + opening + ' ' + deleted_main + '\n' + insert + '\n'
            + filter_sentence + '\n' + display100 + '\n' + categories + '\n\n'
            + diagram_intro + '\n' + diagram101 + '\n' + last + '\n' + r'\margin{78}' + '\n')
(OUT / 'proposed.tex').write_text(proposed, encoding='utf-8')

changes = []
def ch(place, C, H, final, evidence, crop, *, confidence='high', against_C=False,
       against_H=True, kind='misread word', marked_in_H=False, error_sheet_kind='words',
       consequential=False):
    changes.append(dict(id=f'079-{len(changes)+1:02d}', place=place, C=C, H=H, final=final,
                        evidence=evidence, crop=meta[str(crop)]['file'], box=meta[str(crop)]['box'],
                        confidence=confidence, against_C=against_C, against_H=against_H,
                        kind=kind, marked_in_H=marked_in_H,
                        error_sheet_kind=error_sheet_kind, consequential=consequential))

ch('Opening pair: state of the second accent',
   r"\overset{\deleted{\unsure{\wedge}}}{M}{}^*_{\underline G,\underline G'}",
   r"\widehat M^*_{\underline G,\underline G'}", second_opening,
   'The first M has a simple two-arm roof. Above the second, several angular and transverse strokes cross one another; a clean live roof cannot be separated. The crossed-roof reading is retained as doubtful, independently of the clear star to its right.', 1,
   confidence='medium', kind='deletion state', error_sheet_kind='struck text',
   marked_in_H=True, consequential=True)
ch('Large canceled main passage: opening verb and parenthetical phrase',
   'enlevant (' + quoted_infini + ')',
   r"prenant les traces des ...; later \struck{\og l'infini\fg{} \ill{}}",
   'enlevant (' + quoted_infini + ')',
   'The main-size canceled baseline has the long enlevant run followed by a large opening parenthesis, paired upper quote strokes around l’infini, and its closing parenthesis. The separate slanted prenant trial is not this main baseline.', 2,
   kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Large canceled main passage: first M formula',
   r'\widehat M_{\underline G}', r'\ill{}', r'\widehat M_{\underline G}',
   'A detached two-arm roof sits directly above M. Its small G has a separate lower bar. This formula follows the parenthesized l’infini, before resp.', 2,
   kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Large canceled main passage: abbreviation after the first M',
   'resp.', r'\ill{}', 'resp.',
   'The short r/e/s run is followed by a descending p and a separate terminal point. It is not a full expanded word.', 2,
   kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Large canceled main passage: following M and doubtful Gamma formula',
   r"$M_{\underline G}$, $\unsure{\Gamma^!_{\underline G,\underline G'}}$",
   r'\ill{}',
   r'$M_{\underline G}$, $' + first_gamma + '$',
   'The second large M has no separate roof, and its G lower stroke is visible. At the far right a tall Gamma-like upright and top bar survive, but the raised sign and smaller indices are crossed and crowded; the full Gamma reading remains explicitly doubtful.', 2,
   confidence='low', kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Small canceled parenthetical line: opening words',
   r'(les traces de la \unsure{réunion}', r'les traces, \ill{} \ill{}',
   r'(les traces de la \unsure{réunion}',
   'The opening parenthesis and les traces run remain visible under the horizontal strike. The following short de/la groups are present; the central word is too crossed to resolve beyond the provisional réunion reading.', 2,
   confidence='low', kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Small canceled parenthetical lines: divisors and the M-prime expression',
   r"des diviseurs de $\widehat M_{\underline G'}$", r'\ill{}',
   r'des diviseurs de $' + canceled_mprime + '$',
   'The des and diviseurs runs lie on the small canceled baseline. The following de and M with a small primed G occupy the return line. The crowded roof of that M is retained provisionally inside a formula-level doubt.', 2,
   confidence='medium', kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Small canceled parenthetical passage: words immediately before the final tuple',
   r'\unsure{qui contiennent}',
   r'\ill{}',
   r'\unsure{qui contiennent}',
   'The q-like beginning and long low word run after the M-prime remain crossed. They are compatible with qui contiennent, but several internal bodies cannot be separated from the strike. This row concerns only the words; the following formula is recorded in 079-09.', 2,
   confidence='low', kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Complete canceled final tuple, including Gamma index decorations',
   r"(\widehat M_{\underline G},\Gamma^!_{\underline G,\underline G'})",
   r'\ill{}', canceled_tuple,
   'An opening curve, M, comma, Gamma-like stem, two small G bodies and terminal curve are visible. Completion crop18 exposes the lower ink: the M’s G has a separate horizontal bar, but the spaces below both G bodies following Gamma are blank. The whole tuple remains doubtful because its exponent and overlapping roof are not fully exposed; no bars are restored from usual notation.', 18,
   confidence='low', against_C=True, kind='misread symbol or index',
   marked_in_H=True, error_sheet_kind='symbols and indices', consequential=True)
ch('Slanted canceled trial at the beginning of the replacement',
   r'\deleted{prenant les traces de $M$}',
   r"\struck{prenant les traces des $\widehat M_{\underline G'}$ \ill{}}",
   trial,
   'The slanted trial reads prenant les traces provisionally under a long strike, then continues on a short separate canceled line with de and a bare M. That M has neither a roof nor a G-prime subscript. The nearby live hatted M-prime belongs to the replacement, not to this short trial.', 4,
   confidence='medium', kind='misread symbol or index', marked_in_H=True,
   error_sheet_kind='symbols and indices')
ch('Inserted replacement: canceled words after the live hatted M-prime',
   r'\deleted{\unsure{non seuls}}', '(nothing)', r'\deleted{\unsure{non seuls}}',
   'A separate strike covers the short run to the right of the live hatted M-prime. The n/o-like low opening and the later tall l are compatible with non seuls, but several intervening letters merge into the strike; the reading is not resolved.', 3,
   confidence='low', kind='omission', error_sheet_kind='struck text')
ch('Inserted replacement: live relative clause',
   'qui contiennent', r'\uncertain{qui} \uncertain{sont} \uncertain{\ill{}}', 'qui contiennent',
   'The first word has its long q descender and i dot. The next has the initial low co/n run, a tall t, the dotted i, and the joined -ennent continuation; it is not a short sont.', 4,
   marked_in_H=True)
ch('Inserted replacement: M after qui contiennent',
   r'M_{\underline G}', r'\uncertain{\ill{}}', inserted_m,
   'A distinct two-arm angular roof sits immediately over this M, to the left of the tall descender from infini. It is independent of that descender. The small G body is legible, but its separate underline cannot be isolated securely among the nearby crossing strokes, so underline/plain remains doubtful.', 4,
   confidence='medium', against_C=True, kind='misread symbol or index',
   marked_in_H=True, error_sheet_kind='symbols and indices', consequential=True)
ch('Inserted case clause: word after cas',
   'de', r'\uncertain{présent} les', 'de',
   'The small word at the end of dans le cas has a looped d and a short e return. There is no long présent run or separate les before the following M-star formula.', 5,
   marked_in_H=True)
ch('Inserted case clause: trace construction',
   r'on prend la \uline{trace} de', '(nothing)', r'on prend la \uline{trace} de',
   'The short on group precedes a long p descender and the -rend run, then la. Trace is written on the next slanted line with a separate underline, followed by de before the bare M-prime.', 5,
   kind='omission', error_sheet_kind='omissions')
ch('Inserted case clause: preposition before the final hatted formula',
   'sur', r'\uncertain{dans} \uncertain{\ill{}}', 'sur',
   'The low short word before the final hatted M has no tall d ascender. Its s/u/r run is visible, and it is followed directly by the M formula.', 5,
   marked_in_H=True)
ch('Inserted replacement: terminal punctuation',
   r"$\widehat M_{\underline G,\underline G'}$.", r"$\widehat M_{\underline G,\underline G'}$",
   r"$\widehat M_{\underline G,\underline G'}$",
   'After the final primed G, the nearby lower stroke is its underline. The space following the formula has no independent dark point; the source does not supply C’s terminal period.', 5,
   against_C=True, against_H=False, kind='text not on the page', error_sheet_kind='text not on page')
ch('Return to the main text: opening of the filter sentence',
   'Ils sont donc des', r'\ill{}', 'Ils sont donc des',
   'Below the deleted block, a separate live line begins with Ils, then the short sont run, the d/onc group and des. These words are not part of the crossed parenthetical above them.', 6,
   kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('Live filter sentence: first noun',
   'filtres', r'\uncertain{filtrées}', 'filtres',
   'The completion crop shows the full looped f and its descender, dotted i, tall l/t group, and the short -res ending. There is no extra -ées sequence or independent accent after r.', 18,
   marked_in_H=True)
ch('Live filter sentence: complement',
   "d'ouverts", r"\uncertain{d'}\uncertain{éléments}", "d'ouverts",
   'After the looped d and apostrophe, the broad o/u opening, the v/e run and terminal r/t/s strokes are visible. There is no initial é or the tall medial l required by éléments.', 18,
   marked_in_H=True)
ch('Live multiplicité formula: G-prime without an underline',
   r"M_{\underline G'}", r"M_{\underline G'}", r"M_{G'}",
   'This G has its own returning lower hook, followed by the separate prime. The exposed white space beneath the body contains no independent lower bar, unlike the neighboring explicitly underlined G glyphs.', 6,
   against_C=True, kind='misread symbol or index', error_sheet_kind='symbols and indices',
   consequential=True)
ch('After groupoïdes fondamentaux: asterisk',
   'fondamentaux', 'fondamentaux*', 'fondamentaux*',
   'A dark multi-stroke asterisk stands immediately after fondamentaux and before the separate canceled Pi-like glyph. It is not a paper speck or part of that later cancellation.', 7,
   against_C=True, against_H=False, kind='omission', error_sheet_kind='omissions')
ch('Before (100): canceled Pi-like glyph',
   r'\deleted{$\unsure{\Pi}$}', r'\uncertain{\ill{}}', r'\deleted{$\unsure{\Pi}$}',
   'A tall left stroke, upper horizontal and a right-hand leg survive beneath zigzag cancellation. Capital Pi is plausible, but the overstrike hides enough of the right portion that the reading stays doubtful.', 7,
   confidence='medium', kind=r'readable ink left as \ill{}', marked_in_H=True,
   error_sheet_kind='readable ink left as illegible')
ch('After (100): verb construction',
   'sont définis comme des', r'sont définis par \uncertain{une} \uncertain{des}', 'sont définis comme des',
   'The word after définis is a long low comme run, followed by the distinct looped des. It does not contain a separate par followed by une.', 9,
   marked_in_H=True)
ch('After (100): capitalized category noun',
   'Catégories', 'catégories', 'Catégories',
   'The first C is a large open curve rising to the height of the following tall letter strokes. It is visibly larger than the low c that opens the next line’s catégories.', 9)
ch('After universels: repeated conjunction across the line break',
   'universels, ou', 'universels, ou', 'universels, ' + first_ou + ' ou',
   'Completion crop19 shows a reduced separate ou-like run after the comma at the far right. Crop11 begins a new baseline with another distinct ou before comme. They are two written groups, not one word split across crops; the first remains uncertain because its opening is compressed.', 19,
   confidence='medium', against_C=True, kind='omission', error_sheet_kind='omissions')
ch('Next baseline: comme after the second ou',
   'ou comme des catégories', 'ou des catégories', 'ou comme des catégories',
   'A long low word with the two m humps lies between the second ou and des. It is the same comme form as in the preceding definition line.', 11,
   kind='omission', error_sheet_kind='omissions')
ch('Next baseline: abbreviated revêtts',
   'revêtts', r'\uncertain{revêtements}', 'revêtts',
   'The written run has revê followed by the tall compact t/t group and final s. There is no -ements continuation and no detached final period.', 11,
   kind='abbreviation expanded or spelling modernised', marked_in_H=True,
   error_sheet_kind='abbreviations expanded spelling modernised')
ch('After revêtts: unresolved qualifying phrase, M1076',
   r'\unsure{du connexe}', r'\uncertain{connexes}', du_connexe,
   'A separate tall looped d with a short following return precedes the low co/n/n/e-like run. The ending is too flattened to settle its last letters or number. The manuscript’s provisional du connexe remains doubtful; grammar does not replace it with connexes.', 12,
   confidence='low', marked_in_H=True, consequential=True)
ch('Bibliographic reference: bracketed number',
   '[5]', '[53]', '[5]',
   'There is one numeral 5 between the brackets. The following curved upright with lower foot is the closing bracket, not a second numeral 3. The subsequent n°5 and p.768-prime are separate and were also inspected.', 13,
   kind='misread symbol or index', error_sheet_kind='symbols and indices')
ch('Diagram (101): upper connection',
   r'M^*_{\underline G,\underline G\prime}\arrow[r,dash]'.replace(r'\underline G\prime', r"\underline G'"),
   r'M^*_{\underline G,\underline G\prime}\longrightarrow M_{\underline G\prime}'.replace(r'\underline G\prime', r"\underline G'"),
   r'\draw[line cap=round] ([xshift=4pt]A.east) -- ([xshift=-8pt]B.west);',
   'The upper horizontal shaft has a slightly thickened rounded right endpoint but no two-arm arrowhead. The lower horizontal arrow and vertical arrow, by contrast, have definite heads.', 15,
   kind='drawing or diagram', error_sheet_kind='drawings and diagrams', consequential=True)
ch('Diagram (101): downward arrow target and object alignment',
   r"M^*_{\underline G,\underline G'}\longrightarrow M_{\underline G,\underline G'}",
   r"M^*_{\underline G,\underline G'}\longrightarrow (M_{\underline G})",
   r'\draw[->] ([yshift=-5pt]A.south) -- ([yshift=5pt]D.north);',
   'The vertical shaft descends directly above the lower M with the two G indices. The parenthesized M_G and its canceled continuation sit to the left and supply the separate rightward arrow.', 15,
   kind='drawing or diagram', error_sheet_kind='drawings and diagrams', consequential=True)
ch('Diagram (101): canceled upper-right mark',
   r"M_{\underline G'}\deleted{\unsure{M}}", r"M_{\underline G'}; editorial note: an index is crossed out",
   r"M_{\underline G'}\deleted{\unsure{M}}",
   'A compact patch of diagonal strokes survives immediately to the right of the upper-right M_G-prime. A buried M is only a provisional reading; the cancellation is retained instead of dropping the patch or identifying it as a clean index.', 15,
   confidence='low', kind='omission', error_sheet_kind='struck text')
ch('Diagram (101): lower-left canceled group',
   r'(M_{\underline G}\deleted{\unsure{,\Gamma^!}})',
   r'(M_{\underline G}) with \struck{\ill{}} above the following arrow',
   r'(M_{\underline G}\deleted{\unsure{,\Gamma^!}})',
   'The dense overstrike follows the underlined G within the left parenthetical object and meets the origin of the rightward arrow. A vertical remnant is compatible with Gamma, but the comma and raised sign are buried; the full comma-Gamma-bang reading remains tentative.', 15,
   confidence='low', kind='drawing or diagram', marked_in_H=True,
   error_sheet_kind='drawings and diagrams')
ch('Diagram (101): abbreviated caption word and its punctuation',
   'équiv.', 'équivalence', 'équiv',
   'The caption stops after the short équiv run before the separate d’apostrophe. The final dark part belongs to the connected v terminal; completion crop20 shows no independent period. No -alence continuation is written.', 20,
   against_C=True, kind='abbreviation expanded or spelling modernised',
   error_sheet_kind='abbreviations expanded spelling modernised')
ch('Diagram (101): separate closing curve above/right of the caption',
   '(nothing)', '(nothing)',
   r'\node[anchor=base west,inner sep=0pt] at ([xshift=5pt,yshift=5pt]caption.north east) {$\unsure{)}$};',
   'A detached )-shaped stroke stands above and to the right of the ordinary caption-closing parenthesis. The latter descends toward the following d; the detached stroke is a separate piece of ink. Its attachment is unclear, so it is positioned separately and marked doubtful rather than paired by inference.', 20,
   confidence='medium', against_C=True, kind='omission', error_sheet_kind='drawings and diagrams')
ch('Last sentence: reduced mark after lieu',
   'à', ':', final_preposition,
   'The upper component is a small curved cap and the lower component a dark point. This is compatible with the writer’s locally reduced à, but the absence of a full lower letter body leaves a colon alternative. The ambiguity is retained in place.', 16,
   confidence='medium', kind='misread symbol or index', error_sheet_kind='other')
ch('Lower-left pencil foliation',
   r'\margin{78}', '(nothing)', r'\margin{78}',
   'The first pencil digit has the top and diagonal of 7; the second has two joined loops forming 8. It is separate pencil foliation, not an ink author page number.', 17,
   kind='omission', error_sheet_kind='omissions')

decisions = [
    dict(id='M1074', cote=147, scan=79, decision='first', reading=first_100,
         ink='The space directly above the first M body in (100) is blank. The overworked raised mark lies to its right in the star position, like the second term’s star. Thus no independent hat is supplied; only the local star reading remains doubtful.',
         crop='147_scan079_place08.png (291,780,1355,907)', confidence='high'),
    dict(id='M1075', cote=147, scan=79, decision='first', reading='universels',
         ink='The complete crop exposes the low uni opening, v/e/r/s run, small e, tall looped l and final s. The previously clipped l is now complete; the written word is universels.',
         crop='147_scan079_place19.png (1210,963,1655,1115)', confidence='high'),
    dict(id='M1076', cote=147, scan=79, decision='undecided', reading=du_connexe,
         ink='The separate d-plus-short-return group is visible, but the compressed following ending does not securely settle connexe/connexes or the exact short preceding form. No grammatical repair is made.',
         crop='147_scan079_place12.png (328,1205,1672,1350)', confidence='low')
]

inventory = []
def inv(kind, position, first, hand='his hand'):
    inventory.append(dict(scan=79, sheet_kind='text', hand=hand, element=f'{len(inventory)+1:02d}',
                          kind=kind, position=position, first_words_or_objects=first, transcribed='yes'))
inv('text', 'First main baseline and its continuation', opening)
inv('deletion', 'Roof of the second M in the opening pair; state/underlying roof doubtful', r'\unsure{\deleted{\wedge}}')
inv('deletion', 'Large main canceled passage on three overlapping baselines', deleted_main)
inv('deletion', 'Two slanted trial baselines at the start of the replacement', trial)
inv('insertion', 'Slanted replacement surrounding the left side of the canceled main block', r"enlevant les traces des diviseurs à l'infini de $\widehat M_{\underline G'}$")
inv('deletion', 'After the live hatted M-prime in the replacement', r'\deleted{\unsure{non seuls}}')
inv('insertion', 'Next slanted line of the replacement', 'qui contiennent $' + inserted_m + '$')
inv('insertion', 'Lower slanted case clause', r"-- dans le cas de $M^*_{\underline G,\underline G'}$, on prend la \uline{trace} de $M_{\underline G'}$ sur $\widehat M_{\underline G,\underline G'}$")
inv('text', 'Main line below the cancellation', "Ils sont donc des filtres d'ouverts de")
inv('text', 'Following main baseline', r"la multiplicité $M_{G'}$, et les")
inv('text', 'Next main baseline before (100)', 'groupoïdes fondamentaux*')
inv('deletion', 'To the right of the asterisk on that baseline', r'\deleted{$\unsure{\Pi}$}')
inv('display', 'Display (100), including the uncertain first star', display100)
inv('text', 'Definition paragraph below (100)', categories)
inv('text', 'Two baselines introducing the diagram', diagram_intro)
inv('diagram', 'Diagram (101), all four objects and three connections', diagram101)
inv('deletion', 'Upper-right diagram object', r'\deleted{\unsure{M}}')
inv('deletion', 'Lower-left diagram object, before the rightward arrow', r'\deleted{\unsure{,\Gamma^!}}')
inv('text', 'Caption below the lower horizontal arrow', "(équiv d'homotopie !)")
inv('drawing', 'Detached curve above/right of the ordinary caption closing parenthesis', r'\unsure{)} with unresolved attachment')
inv('text', 'Final two baselines, with live des despite overlap', last)
inv('margin note', 'Lower-left pencil foliation', r'\margin{78}', hand='pencil hand not confidently attributed')

doubts = []
def doubt(place, reading, alternatives, confidence, reason):
    doubts.append(dict(place=place, reading=reading, alternatives=alternatives,
                       confidence=confidence, reason=reason))
doubt('Second opening M accent', second_opening, 'Canceled underlying roof preferred; an overworked live or doubled roof cannot be excluded.',
      'medium', 'Several angular/transverse strokes overlap above the M, unlike the simple first roof. The separate star remains legible.')
doubt('First Gamma group in the large canceled main baseline', first_gamma,
      'The raised bang and exact two-index decoration remain provisional.', 'low',
      'The right edge of the canceled block is densely crossed; the tall Gamma outline survives better than its exponent and indices.')
doubt('Small canceled parenthetical: réunion', r'\unsure{réunion}', 'Other buried word possible; no secure alternative supplied.',
      'low', 'The central letter run is cut by long horizontal and vertical strokes. Every letter is not separately exposed.')
doubt('Small canceled parenthetical: hatted M-prime', canceled_mprime, 'Roof state/form may be obscured by crossing strokes.',
      'medium', 'M and its primed G are discernible; the small roof is less independent of the cancellation.')
doubt('Small canceled parenthetical: qui contiennent', r'\unsure{qui contiennent}', 'The crossed word group is not fully recoverable.',
      'low', 'The q-like start and long continuation fit the reading, but several internal bodies lie under the strike.')
doubt('Canceled final tuple', canceled_tuple, 'Roof and Gamma raised sign remain doubtful; Gamma indices are read bare.',
      'low', 'Completion crop18 exposes the M’s underlined G and two later unbarred G bodies, but the exponent and upper overlapping strokes remain obscured.')
doubt('Slanted canceled trial', trial, 'The taking-traces wording remains provisional under the strike.',
      'medium', 'The separate de M line is clear; portions of prenant les traces are merged into the long cancellation stroke.')
doubt('Slanted canceled non seuls', r'\deleted{\unsure{non seuls}}', 'Other buried word(s) possible; no secure alternative supplied.',
      'low', 'Some low n/o shapes and the tall l survive, but the entire intervening sequence is not separable.')
doubt('Inserted M after qui contiennent: underline state', inserted_m, r'\widehat M_{\underline G} or \widehat M_G',
      'medium', 'The independent two-arm roof is clear. A separate G underline is not securely isolated from adjacent crossing ink.')
doubt('Canceled glyph after fondamentaux*', r'\deleted{$\unsure{\Pi}$}', 'Capital Pi preferred; right-side stroke sequence remains obscured.',
      'medium', 'Upper bar and tall strokes survive beneath the cancellation, but the full outline is not plain.')
doubt('First star in (100)', first_100, 'Overworked star preferred; no independent hat above M.',
      'medium', 'The filled raised group has extra retracing but occupies the star position, with blank space above M’s body.')
doubt('First of the repeated ou groups', first_ou, 'Reduced conjunction ou preferred.',
      'medium', 'The far-right run after the comma is much compressed; the next-line ou is a separate definite group.')
doubt('M1076: du connexe', du_connexe, 'Exact short prefix and singular/plural ending remain uncertain; H has connexes.',
      'low', 'A d-like group precedes the flattened connexe-like run. Grammar cannot settle the written ending.')
doubt('Upper-right canceled mark in (101)', r'\deleted{\unsure{M}}', 'Underlying mark unidentified beyond the provisional M suggestion.',
      'low', 'Multiple diagonal overstrikes conceal the internal character; no clean underlying index is recoverable.')
doubt('Lower-left canceled group in (101)', r'\deleted{\unsure{,\Gamma^!}}', 'Comma, Gamma and bang are provisional as a group.',
      'low', 'The overstrike meets the rightward arrow. A vertical remnant survives, but the raised sign and separating punctuation are buried.')
doubt('Detached closing curve beside the diagram caption', r'\unsure{)}',
      'Glyph is clearly )-shaped; attachment to the caption or another parenthetical group is uncertain.',
      'medium', 'It is separate from the ordinary caption closing parenthesis and sits higher/rightward. No pairing is supplied.')
doubt('Last preposition/punctuation after lieu', final_preposition, 'à or colon',
      'medium', 'Small curved upper mark plus lower point fits a reduced à but does not expose a full letter body.')

notes = [
    'Physical coverage: 32 reading bands were inspected: 21 primary baselines including the two diagram object rows and caption, the separate (101) label band, nine slanted trial/replacement lines, and pencil foliation 78. The whole scan and both native halves were each viewed once. All 20 saved crops were viewed: 17 initial crops and three documented completion crops for still-open clipped ascenders in filtres/universels and the caption q-descender. No decided place was recropped. No OCR, outside research, TeX compilation, or blind second reading was used.',
    'The manuscript introduces two starred germs of multiplicities and revises the wording of their construction by traces and removal of divisors at infinity. The long original statement, the shorter taking-traces trial, and non seuls are canceled; their doubtful portions remain explicit. The slanted replacement is read as part of this definition before the live Ils sont donc sentence. The geometry of these germs and the claimed trace/removal construction have not been proved or reconstructed here.',
    'The opening first M has a clear roof and star; the second roof is crossed/overworked and remains doubtful. The M after qui contiennent in the live insertion has an independent roof next to the infini descender, which C omitted. Local index underlines are not uniform: the live multiplicité M_{G-prime} and the two Gamma indices in the canceled final tuple have no separate bars. The inserted M’s small G underline remains uncertain. In (100) both M bodies are bare; a distinction expected from the opening pair does not supply an absent roof. The first star alone remains locally doubtful.',
    'The text calls the germs filtres d’ouverts and describes their fundamental groupoids through a rightward-limit category of categories of revêtements universels, or the subsequent unresolved du connexe wording. Both written ou groups across the line break are retained, the first as doubtful. These are manuscript definitions/assertions; this reading has not constructed the limit, proved equivalence of the descriptions, or used an expected category of coverings to repair the words.',
    'The written cross-reference is comparer [5], n°5, p.768-prime. The right bracket is not a numeral 3. No cited work was identified or consulted, and no external bibliographic claim is made.',
    'Diagram (101) has four objects: the starred two-index M above the lower two-index M; the upper-right M_{G-prime} with a canceled mark; and the lower-left parenthesized M_G with a canceled continuation. Its upper horizontal connection is headless. The vertical arrow points to the lower two-index M, and the lower arrow points right from the parenthesized object to that same target. The author labels the latter équiv d’homotopie !. That homotopy-equivalence assertion and the existence of the germ morphisms are carried as manuscript claims; no proof was performed.',
    'The caption’s abbreviation is équiv with no independent dot. A separate )-shaped stroke above/right of its ordinary closing parenthesis is positioned independently, with attachment uncertain. The ordinary closing stroke descends into the following live des, whose d is retraced; no canceled underlying word is supplied there. The final à/colon mark remains doubtful, and the last phrase ends on this sheet without a completed statement or terminal punctuation.',
    'No ink author page number 39 is visible on this sheet, so none is inferred. The separate pale pencil 78 is kept in margin{}, with its hand unattributed. The asterisk after fondamentaux is transcribed without inventing a footnote or explanation.'
]
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
who = 'reader_c, GPT-6 Astra Pro (effort setting not exposed)'
check_events = [
    dict(statement_id='147-079-N2', date=now, who=who, type='carried as background without fault found',
         outcome='Read the revised definition of starred germs and its trace/removal wording. No local geometric construction, independence assertion, or analytic theorem was proved; the canceled wording remains uncertain where the ink is obscured.'),
    dict(statement_id='147-079-N3', date=now, who=who, type='carried as background without fault found',
         outcome='Checked only the written roofs, stars and index bars in the displayed and inline expressions. This is transcription verification, not a mathematical verification that the two germs or repeated (100) terms are correct; no absent hat or bar was supplied from expectation.'),
    dict(statement_id='147-079-N4', date=now, who=who, type='carried as background without fault found',
         outcome='Read filtres d’ouverts, the rightward-limit notation, universels and the unresolved later phrase. No limit category was constructed and no equivalence between the descriptions was proved. The word universels was resolved from the complete ink crop only.'),
    dict(statement_id='147-079-N6', date=now, who=who, type='carried as background without fault found',
         outcome='Read the source diagram and homotopy-equivalence caption, checking which objects each visible arrow joins and the missing upper arrowhead. No topological or germ-theoretic equivalence proof was performed; the canceled groups were not recovered from a presumed theorem.')
]

notation = [
    dict(sign='Angular roof beside a higher-line descender', reading=inserted_m,
         evidence='Crop04 separates the two-arm roof over M from the tall infini descender immediately to its right.',
         scope='Only the live inserted M after qui contiennent; its G underline remains doubtful.'),
    dict(sign='G with or without a separate lower bar', reading='Preserve local bars rather than applying a uniform convention.',
         evidence='The live M_{G-prime} in the multiplicité sentence has blank space below G; the canceled final tuple has a barred M-index G but two unbarred Gamma-index G bodies.',
         scope='These local counterexamples on079; other visible bars remain as drawn.'),
    dict(sign='Retraced raised star', reading=first_100,
         evidence='The first raised mark in (100) is right of the M body, while the space directly above the body is blank.',
         scope='The first term of (100); its independent-hat choice is resolved, its overworked star remains doubtful.'),
    dict(sign='Asterisk after prose', reading='fondamentaux*',
         evidence='Separate dark crossing strokes follow the word and precede the canceled Pi-like group.',
         scope='One prose asterisk on this page, without an inferred note.'),
    dict(sign='Headless horizontal diagram shaft', reading='An undirected drawn connection, without a supplied arrowhead.',
         evidence='The upper shaft ends in a thickened round termination; both other diagram connections have clear V-shaped heads.',
         scope='Upper connection of (101).'),
    dict(sign='Reduced à-like mark', reading=final_preposition,
         evidence='A short curved upper component lies above a separate lower point.',
         scope='Final donnant lieu phrase only; the colon alternative remains open.')
]
hand_log = [
    dict(habit='Repeated words across a physical line break must not be silently collapsed.', pages=[79],
         all_occurrences='One local case: a reduced ou after the comma following universels, then another ou at the next baseline before comme.',
         witness_misreadings='Both witnesses supply only one ou.'),
    dict(habit='Index underlining varies locally, even within a closely related formula group.', pages=[79],
         all_occurrences='Checked the opening pair, revised definition, (100) and (101). The live multiplicité formula has plain G-prime, and the canceled final Gamma tuple has two bare G indices; the nearby M-index G has a separate bar.',
         witness_misreadings='Both witnesses supply a bar on the live G-prime; C also supplies bars on the two canceled Gamma indices.'),
    dict(habit='A complete two-arm roof may stand immediately beside a prose descender.', pages=[79],
         all_occurrences='Confirmed for the inserted M after qui contiennent. The nearby infini descender is not the roof; the second opening roof is instead genuinely crossed/overworked.',
         witness_misreadings='C gives that inserted M bare.'),
    dict(habit='A shortened abbreviation can end in a connected terminal stroke without a separate dot.', pages=[79],
         all_occurrences='The caption has équiv without a detached period. Revêtts is also shortened without expansion; resp. and p. have their own visible dots.',
         witness_misreadings='C adds a point after équiv; H expands équiv and revêtts.'),
    dict(habit='A descending parenthesis can meet the initial letter of the next line without deleting the word.', pages=[79],
         all_occurrences='One case: the ordinary caption closing stroke meets the retraced d of live des in the final sentence.',
         witness_misreadings='No underlying word is recoverable or supplied; H marks des doubtful rather than identifying a separate deletion.')
]
abbreviations = [
    dict(written='resp.', expansion='respectivement'),
    dict(written='revêtts', expansion='revêtements; the source abbreviation is retained'),
    dict(written='équiv', expansion='équivalence; no final dot is written in this caption'),
    dict(written='lim with a rightward arrow underneath', expansion='limite in the directed notation written by the author; no category-theoretic proof is implied'),
    dict(written='n°', expansion='numéro'),
    dict(written='p.', expansion='page')
]

second_boxes = []
def sb(kind, box, reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02d}', kind=kind,
                             x0=box[0], y0=box[1], x1=box[2], y1=box[3], reading=reading))
sb('doubtful formula', [330,18,1625,178],
   r"Je désigne par $\widehat M^*_{\underline G,\underline G'}$, $" + second_opening + '$ les')
sb('struck passage', [325,279,1667,492], deleted_main)
sb('insertion', [18,250,906,910], insert)
sb('word disagreement', [330,392,1620,658],
   r"Ils sont donc des filtres d'ouverts de la multiplicité $M_{G'}$, et les")
sb('struck passage', [332,635,1410,787],
   r"groupoïdes fondamentaux* \deleted{$\unsure{\Pi}$}")
sb('handwritten number', [291,780,1355,907], display100)
sb('word disagreement', [330,884,1655,1245],
   r"sont définis comme des Catégories $\underset{\longrightarrow}{\lim}$ des catégories de revêtements universels, "
   + first_ou + r' ou comme des catégories des revêtts')
sb('word disagreement', [328,1205,1672,1464],
   du_connexe + r" desdits germes de multiplicités (comparer [5], n°5, p. $768'$).")
sb('doubtful formula', [319,1718,1285,2160], diagram101)
sb('non-high-confidence change', [330,2050,1536,2305], last)
sb('margin note', [20,2300,90,2348], r'\margin{78}')

report = dict(scan=79, reader='reader_c', physical_lines_read=32, changes=changes,
              decisions=decisions, inventory=inventory, doubts=doubts, notes=notes,
              check_events=check_events, notation=notation, hand_log=hand_log,
              abbreviations=abbreviations, second_boxes=second_boxes,
              unresolved=[
                  'Crossed second opening roof and several words/formulas inside the large top cancellation remain doubtful.',
                  'The slanted trial and non seuls stay provisional under the strike; the inserted M hat is clear but its G underline is uncertain.',
                  'The first star in (100) remains locally doubtful after resolving the absent independent hat.',
                  'The first repeated ou is reduced; du connexe remains unresolved.',
                  'Both canceled diagram groups remain provisional; the extra closing curve has uncertain attachment.',
                  'The final reduced à/colon mark remains unresolved. No following-page completion is supplied.'
              ],
              witness_comparison='C preserves far more of the top cancellation, the slanted replacement, and the live prose than H, and it gets the topology of the visible diagram connections closer. H correctly retains the prose asterisk that C omits. Both witnesses supply a G underline absent in the live multiplicité formula and collapse a written repetition of ou. C omits a clear inserted M roof, adds a terminal period to the insertion and a point to équiv, and supplies Gamma-index bars absent in the exposed canceled tuple. H omits or misorders much readable replacement text, expands revêtts/équiv, reads the closing bracket as a second citation digit, gives the upper diagram shaft an arrowhead, and sends the vertical arrow to the wrong lower object. Editorial notes and macro-only differences were not treated as manuscript text or counted as independent changes.')
(OUT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Structural checks only: this task forbids TeX compilation.
assert [d['id'] for d in decisions] == ['M1074','M1075','M1076']
assert len(meta) == 20
for k, item in meta.items():
    assert (WORK / 'crops' / item['file']).is_file()
for row in changes:
    assert (WORK / 'crops' / row['crop']).is_file()
for box in second_boxes:
    assert box['reading'] in proposed, box['box']
assert r'\margin{78}' in proposed and r'\mspage{' not in proposed
assert proposed.count(r'\deleted{') == 7
assert proposed.count(r'\inserted{') == 1
for ev in check_events:
    assert 1 <= int(ev['statement_id'].rsplit('N',1)[1]) <= len(notes)
print(json.dumps({'scan':79, 'physical_bands':32, 'crops':20, 'changes':len(changes),
                  'decisions':len(decisions), 'inventory':len(inventory), 'doubts':len(doubts),
                  'notes':len(notes), 'check_events':len(check_events), 'second_boxes':len(second_boxes)}))
