"""Page-specific first-reader record generator. Retain with the evidence crops."""
from pathlib import Path
import json
import importlib.util

ROOT = Path('/workspace/scratch/f28c4f52d3ec')
PAGE = '148_scan061'
spec = importlib.util.spec_from_file_location('page061_crops', ROOT/'proposed/148_scan061_make_crops.py')
crops = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crops)
tex = (ROOT/'proposed'/f'{PAGE}.tex').read_text(encoding='utf-8')
changes = []

def change(place, c, h, final, diff_c, diff_h, kind, error_kind, evidence, crop,
           confidence='high', marked_in_h=False, consequential=False):
    changes.append(dict(id=f'{PAGE}-{len(changes)+1:02}', place=place, c=c, h=h,
        final=final, diff_c=diff_c, diff_h=diff_h, kind=kind, error_kind=error_kind,
        evidence=evidence, crop=f'crops/{PAGE}_{crop}.png', box=crops.SPECS[crop][0],
        confidence=confidence, marked_in_h=marked_in_h, consequential=consequential))

change('Inserted item 0, name of the sum', r'\unsure{disjointe|directe}', r'directe',
       r'\unsure{disjointe|directe}', False, True, 'misread word', 'Words',
       'The opening d and final -te-like run are visible. The middle strokes overlap the tall letters of total below; the possible j-descender cannot securely be assigned to this word. Neither alternative is promoted to certainty.',
       'zero_insert', 'low')
change('Item 0, insertion state', r'\inserted{$(0^\circ)$ Somme \unsure{disjointe|directe}}',
       r'\item[(0°)] Somme directe\supplied{s}.',
       r'\inserted{$(0^\circ)$ Somme \unsure{disjointe|directe}}', False, True,
       'insertion or placement', 'Insertions put in the wrong place',
       'The small (0°) and Somme row is squeezed between the heading and the later qualification above item 1. It is a separate added row; the supplied s in H is editorial and is not counted as ink.', 'zero_insert')
change('Item 0, terminal punctuation', r'\unsure{disjointe|directe}', r'directe\supplied{s}.',
       r'\unsure{disjointe|directe}', False, True, 'text not on the page', 'Text that is not on the page',
       'No independent final point follows the sum name in the enlarged inserted row. H’s supplied s is excluded from the comparison; the unmarked full stop is not supported.', 'zero_insert', 'medium')
change('Item 1, qualification above des repères',
       r'\inserted{\uline{total} des repères en $a$, i.e.}', r'\add{total} \struck{\ill{}}',
       r'\inserted{\uline{total} des repères en $a$, i.e.}', False, True,
       'deletion state (struck given live or live given struck)', 'Struck text',
       'The complete raised row reads total, then des repères en a, i.e. The underline is under total. The long lower curve under the following words bends into the gap after gommage as a leader; it does not cross the letters as a cancellation. The full-width boundary crop includes the complete right-hand abbreviation.', 'zero_insert_full')
change('Item 1, first raised circle expression after cercle', r'\inserted{\unsure{$C_a$}}',
       r'\add{\uncertain{les}}', r'\inserted{\unsure{$C_a$}}', False, True,
       'misread symbol or index', 'Symbols and indices',
       'The completed crop shows a narrow open curved upright and a separate small lower oval between cercle and de. C_a remains plausible, but the small upper curve is not secure enough to resolve the mark. H also places its uncertain word before cercle.',
       'item1_circles_full', 'medium', True)
change('Item 1, second raised expression after recollement', r'\inserted{\unsure{les|$C_a$}}',
       'absent', r'\inserted{\unsure{les|$C_a$}}', False, True, 'omission', 'Omissions',
       'A distinct small group stands above the gap after recollement, attached by a curved leader. Its tall left stroke and compressed right loops allow les or C_a; this group is separate from the first raised circle expression.',
       'item1_circles_full', 'low')
change('Item 1, cancelled wording after ou', r'\deleted{\unsure{sur un cercle}}',
       r'\struck{\ill{} \ill{}}', r'\deleted{\unsure{sur un cercle}}', False, True,
       r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'The crossed row retains a low sur-like opening, a separate un-like group, and the tall l in the final cercle-like group. The strike covers internal joins, so the existing uncertainty is retained rather than claiming every letter is plain.',
       'item1_circles_full', 'medium', True)
change('Item 1, overwritten article after suppression', r'de la', r"d'\add{une}",
       r"\unsure{d'une|de la}", True, False, 'misread word', 'Words',
       'An apostrophe-like raised stroke follows the d-group, and the next compressed group has u/n-like humps. The same overworked strokes can still support de la; the article and the separate insertion state attributed to une by H are not secure.',
       'item1_replace_full', 'medium')
change('Item 1, partie after suppression', r'\deleted{partie}', r'partie', r'\deleted{partie}',
       False, True, 'deletion state (struck given live or live given struck)', 'Struck text',
       'A heavy horizontal strike passes through partie, including the p stem and the terminal letters. The raised R_a above it is separate live replacement ink.', 'item1_replace_full')
change('Item 1, replacement R_a', r'\inserted{$R_a$}', r'$R_a$', r'\inserted{$R_a$}',
       False, True, 'insertion or placement', 'Insertions put in the wrong place',
       'The full tall R and its small lower a stand above the cancelled partie, not on the old baseline. The upward boundary extension includes the entire R.', 'item1_replace_full')
change('Item 1, live parameter after modification de', r'$r_a$', r'$r$', r'$\underline r$',
       True, True, 'misread symbol or index', 'Symbols and indices',
       'The r has a short straight horizontal stroke centred beneath it. There is no separate lower-right a loop. The bar is an underline, unlike the distinct small a subscripts elsewhere on the page.',
       'item1_replace_full', 'high', False, True)
change('Item 1, cancelled continuation before remplaçant',
       r'\deleted{\unsure{de $R$ se trouvant dans une partie}}',
       r'\struck{\ill{} $R$ se trouvant sur une partie}',
       r'\deleted{\unsure{de $R$ se trouvant dans une partie}}', False, True,
       'misread word', 'Words',
       'The beginning has a de-like loop before R. After trouvant, the tall initial d and low following humps favour dans, not sur. The long strike masks several internal joins, so uncertainty remains over the whole cancelled run despite those recoverable letters.',
       'item1_replace_full', 'medium', True)
change('Margin to item 1, underlining', r'\uline{fortement irréversible}',
       r'fortement irréversible', r'\uline{fortement irréversible}', False, True,
       'other', 'Other',
       'There is a separate straight underline beneath fortement and another beneath irréversible on the following oblique row. Both word rows remain live.', 'margin1')
change('Margin to item 1, punctuation before condition',
       r'\uline{fortement irréversible}\quad $r_a\ne0$', r'fortement irréversible ; $r_a \neq 0$',
       r'\uline{fortement irréversible}\quad $r_a\ne0$', False, True,
       'text not on the page', 'Text that is not on the page',
       'The condition r_a≠0 occupies the next row; there is no semicolon between the label and condition.', 'margin1')
change('Item 2, raised heading',
       r"\inserted{\uline{gommage partiel uniforme}: \uline{d'exposant $d_a\mid r_a$}}",
       r"\emph{gommage partiel uniforme d'exposant $d_a \mid r_a$}",
       r"\inserted{\uline{gommage partiel uniforme}: \uline{d'exposant $d_a\mid r_a$}}",
       False, True, 'insertion or placement', 'Insertions put in the wrong place',
       'The small underlined heading is raised above the main Restriction row beginning at 2°). The full boundary crop shows all of d_a|r_a above its underline.', 'item2_full')
change('Item 2, colon in raised heading',
       r"\uline{gommage partiel uniforme}: \uline{d'exposant $d_a\mid r_a$}",
       r"\emph{gommage partiel uniforme d'exposant $d_a \mid r_a$} :",
       r"\uline{gommage partiel uniforme}: \uline{d'exposant $d_a\mid r_a$}",
       False, True, 'insertion or placement', 'Insertions put in the wrong place',
       'Two small vertically separated points occur after uniforme, before d’exposant. There is no second colon at the end of the multiplier condition.', 'item2_full')
change('Item 2, un before target quotient',
       r"à un $\mathbb Z_a/r'_a\mathbb Z_a$", r"à $\mathbf{Z}_a/r'_a\mathbf{Z}_a$",
       r"à un $\mathbb Z_a/r'_a\mathbb Z_a$", False, True, 'omission', 'Omissions',
       'A separate low two-hump un is present at the left of the target-quotient row. Its last stroke has the short descending finish of n, and there is no separate e.', 'item2_full')
change('Item 2, conjunction before on suppose', r'si on suppose', r'\uncertain{où} on suppose',
       r'où on suppose', True, False, 'misread word', 'Words',
       'After possibles and its comma the short compressed group has a curved o/u-like baseline and a small accent above it. It lacks the tall dotted i that would support si. Both readers favour où from this crop.',
       'item2_full', 'high', True)
change('Item 2, punctuation after d_a>1', r"$d_a>1$ i.e. $r'_a\ne r_a$",
       r"$d_a > 1$, i.e.\ $r'_a \neq r_a$", r"$d_a>1$ i.e. $r'_a\ne r_a$",
       False, True, 'text not on the page', 'Text that is not on the page',
       'The tall 1 is followed by a clear blank before i.e.; no separate comma is visible there.', 'item2_full')
change('Item 2, isolated glyph to the lower right of r prime divides r', 'absent', 'absent',
       r'\raisebox{-.4ex}{\unsure{2|?}}', True, True, 'omission', 'Omissions',
       'This is a dark, crisp isolated ink mark with an upper loop, descending diagonal and lower foot. It resembles 2 but could be a question-mark-like punctuation form. It is not the pale diffuse reverse-side texture and is not silently absorbed into the divisor formula.',
       'item2_full', 'medium')
change('Margin to item 2, crossed low word', 'absent', r'\struck{\ill{}}',
       r'\deleted{\unsure{anodin}}', True, True, r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'Beneath the r_a condition a separate low cursive run is crossed by a horizontal line. An initial small loop, low n/o-like joins and a later taller d-like stroke suggest anodin, but the crossing prevents secure recovery of every letter.',
       'margin2', 'low', True)
change('Margin to item 2, pair of divisor relations',
       r"r'_a\unsure{\mid|\ne}r_a\text{ et }r'_a\ne r_a",
       r"$r'_a \neq r_a$ et $r'_a \mid r_a$",
       r"$r'_a\unsure{\mid|\ne}r_a$ et $r'_a\ne r_a$", False, True,
       'misread symbol or index', 'Symbols and indices',
       'The first relation is overworked: a long near-upright stroke crosses shorter bars, allowing a divisor stroke or a modified not-equal. After et the second relation plainly has two short bars crossed by an upright stroke, hence ≠ rather than H’s divisor sign. The order is preserved.',
       'margin2', 'medium', False, True)
change('Margin to item 2, underline scope', r'\uline{renforcement de structure faible}',
       r'renforcement de structure faible', r'\uline{renforcement} de\quad\uline{structure faible}',
       True, True, 'other', 'Other',
       'The first underline stops after renforcement, before the separately written de. The lower structure and faible have their own lower strokes. The line above the whole label belongs to an open boundary, not an underline.', 'margin2')
change('Margin to item 2, punctuation inserted by H',
       r"r_a\unsure{\ge|>}1$ \[ r'_a\unsure{\mid|\ne}r_a\text{ et }r'_a\ne r_a \qquad\text{i.e. }",
       r"$r_a \geq 1$ \struck{\ill{}} ; $r'_a \neq r_a$ et $r'_a \mid r_a$, i.e.\ $d_a",
       r"$r_a\unsure{\ge|>}1$\quad\deleted{\unsure{anodin}}\quad $r'_a\unsure{\mid|\ne}r_a$ et $r'_a\ne r_a$\quad i.e.",
       False, True, 'text not on the page', 'Text that is not on the page',
       'The conditions occupy successive oblique rows. There is no independent semicolon after the crossed word and no comma after the second r_a relation. H’s semicolon after faible is likewise absent; the visible surrounding lines are rules.', 'margin2')
change('Margin to item 2, final full stop', r'\ne1.', r'\neq 1', r'\ne1', True, False,
       'text not on the page', 'Text that is not on the page',
       'The last 1 after the fractional identity ends the row without a separate punctuation point.', 'margin2')
change('Margin to item 2, open boundary', 'absent', 'absent',
       r'\draw ([xshift=-1pt,yshift=3pt]m2label.north west) -- ([xshift=3pt,yshift=3pt]m2label.north east) -- ([xshift=3pt]m2label.south east);',
       True, True, 'drawing or diagram', 'Drawings and diagrams',
       'A long upper rule turns down at the right of the classification and first condition; no closing left or lower edge is visible. The proposal draws this open boundary. H describes a frame in an editorial note but does not reproduce it in the page text.', 'margin2')
change('Item 3, replacement heading and capital initial',
       r"\inserted{\uline{Surmarquage uniforme} \uline{d'exposant} $d_a>1$}",
       r"\emph{surmarquage uniforme d'exposant $d_a > 1$}",
       r"\inserted{\uline{Surmarquage uniforme} \uline{d'exposant} $d_a>1$}",
       False, True, 'insertion or placement', 'Insertions put in the wrong place',
       'The replacement heading stands above cancelled Extension des. Its initial S is a full-height separately formed letter. Underlines run beneath Surmarquage uniforme and d’exposant, stopping before d_a>1; this is live raised ink, not the old line.', 'item3_title')
change('Item 3, target quotient indices', r'$\mathbb Z_a/d_ar_a\mathbb Z_a$',
       r'$\mathbf{Z}_a/d_a r_a\mathbf{Z}_a$', r'$\unsure{\mathbb Z|\mathbb Z_a}/d_ar_a\mathbb Z$',
       True, True, 'misread symbol or index', 'Symbols and indices',
       'In the target quotient the final Z has only its terminal foot and no detached a. The numerator Z has a thick closed terminal foot that may be a reinforced serif or an attached a, so it remains Z|Z_a. Both target Zs have doubled diagonal strokes, preserved as mathbb Z rather than H’s bold Z. In the source quotient both Zs have distinct separate a subscripts. The whole pair was read, not just the doubtful target letter.',
       'item3_formula', 'medium', False, True)
change('Item 3, terminal comma', r'$\mathbb Z_a/d_ar_a\mathbb Z_a$,',
       r'$\mathbf{Z}_a/d_a r_a\mathbf{Z}_a$.', r'$\unsure{\mathbb Z|\mathbb Z_a}/d_ar_a\mathbb Z$,',
       False, True, 'other', 'Other',
       'A dark short mark after the final Z has a descending curved tail, making it a comma rather than a point.', 'item3_formula')
change('Margin to item 3, underline scope', r'\uline{affaiblissement de structure faible}',
       r'affaiblissement de structure faible', r'\uline{affaiblissement de}\quad structure \uline{faible}',
       True, True, 'other', 'Other',
       'A line runs under affaiblissement de and another under faible. There is no secure continuous lower stroke beneath structure; only a faint short trace occurs near its beginning. The upper and right rule is separate from these underlines.',
       'margin3', 'medium')
change('Margin to item 3, punctuation before condition',
       r'\uline{affaiblissement de structure faible}\quad $r_a\ne0$',
       r'affaiblissement de structure faible ; $r_a \neq 0$',
       r'\uline{affaiblissement de}\quad structure \uline{faible}\quad $r_a\ne0$',
       False, True, 'text not on the page', 'Text that is not on the page',
       'The r_a≠0 condition sits on its own lower row. No semicolon intervenes after faible.', 'margin3')
change('Margin to item 3, open upper and right rule', 'absent', 'absent',
       r'\draw ([xshift=-1pt,yshift=3pt]m3label.north west) -- ([xshift=3pt,yshift=3pt]m3label.north east) -- ([xshift=3pt]m3label.south east);',
       True, True, 'drawing or diagram', 'Drawings and diagrams',
       'A long upper boundary turns down obliquely at the right, ending at the first-row underline. It does not close a box around the whole margin note. The proposal preserves the open form.', 'margin3')
change('Item 4, terminal punctuation', r'$(a\in A_0)$', r'($a \in A_0$).',
       r'$(a\in A_0)$', False, True, 'text not on the page', 'Text that is not on the page',
       'The separate membership row ends at its curved right parenthesis; there is no following full stop.', 'items45')
change('Item 5, terminal punctuation', r'$(a\in A_l)$', r'($a \in A_{\ell}$).',
       r'$(a\in A_l)$', False, True, 'text not on the page', 'Text that is not on the page',
       'The row ends with the large right parenthesis and blank paper beyond it. The looped index is l/ell, not a numeric 1; the l/ell macro difference is not counted.', 'items45')
change('Shared margin to items 4 and 5, ending of adjective', r'irréversible', r'irréversibles',
       r'irréversible', False, True, 'misread word', 'Words',
       'The last visible hook is the ending of the e-like terminal. No separate final s follows it before the brace. The agreement is not supplied from the two numbered items.', 'margin45')
change('Shared margin to items 4 and 5, underline scope', r'\uline{fortement irréversible}',
       r'fortement irréversibles', r'fortement \uline{irréversible}', True, True, 'other', 'Other',
       'The line above fortement is a separator. There is no lower underline beneath that word; the single lower underline lies beneath irréversible.', 'margin45')
change('Brace joining items 4 and 5', r'$\left\{\begin{array}{l}4^\circ\\5^\circ\end{array}\right.$',
       'absent', 'A single TikZ left brace joins the actual two circled numbered lines; neither number is duplicated.',
       True, True, 'drawing or diagram', 'Drawings and diagrams',
       'One leftward central point and upper/lower curved arms span the two circled labels. There is no second written pair of 4° and 5° inside the margin. H’s editorial note describes the brace; the proposal reproduces it beside the actual items.', 'items45')
change('Item 6, punctuation after star', r'\({}^*\)', r'${}^{*}$.', r'\({}^*\)', False, True,
       'text not on the page', 'Text that is not on the page',
       'The asterisk is above and to the right of the membership parenthesis. No separate point follows it.', 'item6')
change('Margin to item 6, réversible classification', r'réversible = anodin',
       r'réversible à \ill{} près', r'réversible = anodin', False, True,
       r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'Two short near-parallel horizontal strokes follow réversible. The next word has a low initial a, n/o-like humps, tall d, dotted i and a final n run: anodin. There are no independent à or près groups.', 'margin6', 'high', True)
change('Margin to item 6, final full stop', r'$r_a\ge1$.', r'$r_a \geq 1$',
       r'$r_a\ge1$.', False, True, 'omission', 'Omissions',
       'A separate dark point follows the 1 at the end of the condition, above the lower separator rule.', 'margin6')
change('Item 7, word after opening parenthesis', r'(avec', r'($a, a\'', r'(avec',
       False, True, 'omission', 'Omissions',
       'Between the opening parenthesis and the a,a′ pair there is a faint but separate compressed avec run. The low a/v connection and short terminal c-like stroke occupy this space; it is not blank.', 'item7', 'medium')
change('Item 7, equality inserted before closing parenthesis', r'\inserted{$r_a=r_{a\'}$}',
       r'$r_a = r_{a\'}$', r'\inserted{$r_a=r_{a\'}$}', False, True,
       'insertion or placement', 'Insertions put in the wrong place',
       'The small equality is raised above a broad curved leader whose point enters the gap before the closing parenthesis. Both lower a indices and the prime on the right one are visible.', 'item7')
change('Margin to item 7, réversible classification', r'réversible = anodin',
       r'réversible à \ill{} près', r'réversible = anodin', False, True,
       r'readable ink left as \ill{}', 'Readable ink left as illegible',
       'The short equality has two horizontal strokes. The following a-n-o-d-i-n sequence is visible, including the tall d and dotted i; there are no separate à or près words.', 'margin7', 'high', True)
change('Margin to item 7, punctuation around classification',
       r'$r_a=r_{a\'}\ge1$\quad réversible = anodin.',
       r'$r_a = r_{a\'} \geq 1$ ; réversible à \ill{} près',
       r'$r_a=r_{a\'}\ge1$\quad réversible = anodin', True, True,
       'text not on the page', 'Text that is not on the page',
       'There is no semicolon after the upper condition and no independent full stop after the final n of anodin on the lower row.', 'margin7')
change('Footnote, peut-être insertion', r'\inserted{peut-être}', r'peut-être',
       r'\inserted{peut-être}', False, True, 'insertion or placement', 'Insertions put in the wrong place',
       'The complete peut-être group is written above the line. A curved leader descends between faudrait and séparer. The short hyphen and the circumflex/raised strokes belong to the word, which remains live.', 'footnote')
change('Footnote, extra group before exclure', 'absent', 'absent',
       r'\unsure{$=$|\deleted{ou}}', True, True, 'omission', 'Omissions',
       'At the start of the last row there is a short straight upper bar and a separated wavy lower stroke. These support an equals shorthand; alternatively the lower run could be repeated ou with a cancellation above it. The physical ambiguity is retained. The main reader reports a matching straight-upper/wavy-lower equals in 063; reader_b did not open that page.',
       'footnote', 'medium')
change('Footnote, terminal punctuation', r'$r_a=0$?).', r'$r_a = 0$ ?)', r'$r_a=0$?)',
       True, False, 'text not on the page', 'Text that is not on the page',
       'The question mark and long right parenthesis are visible at the edge. There is no additional point outside the parenthesis.', 'footnote')
change('Lower-left folio annotation', r'\mspage{60}', 'absent', r'\mspage{60}', False, True,
       'omission', 'Omissions',
       'A pale 6 with a closed lower bowl is followed by a tall oval 0 near the lower left edge. Its writer cannot be attributed from appearance alone.', 'folio')
change('Separator above shared margin to items4 and5', 'absent', 'absent',
       r'\rule{2cm}{.3pt}', True, True, 'drawing or diagram', 'Drawings and diagrams',
       'A long oblique line lies above fortement, separated from the word. It is reproduced as a separator, not as an underline or a closed frame. H mentions separators only in an editorial note.', 'margin45')
change('Separator above margin to item6', 'absent', 'absent',
       r'\rule{2cm}{.3pt}', True, True, 'drawing or diagram', 'Drawings and diagrams',
       'The upper long line separates this note from the shared items4/5 note. It runs above the letters of fortement irréversible without striking them.', 'margin6')
change('Separator above margin to item7', 'absent', 'absent',
       r'\rule{2cm}{.3pt}', True, True, 'drawing or diagram', 'Drawings and diagrams',
       'A long oblique rule separates the completed item6 condition from the item7 r_a=r_a′≥1 row. It is kept as a separator.', 'margin7')
change('Item2, doubled integer alphabet in both quotients',
       r"$\mathbb Z_a/r_a\mathbb Z$ à un $\mathbb Z_a/r'_a\mathbb Z_a$",
       r"$\mathbf{Z}_a/r_a\mathbf{Z}$ à $\mathbf{Z}_a/r'_a\mathbf{Z}_a$",
       r"$\mathbb Z_a/r_a\mathbb Z$ à un $\mathbb Z_a/r'_a\mathbb Z_a$",
       False, True, 'misread symbol or index', 'Symbols and indices',
       'Each of the four Z letters has two separated diagonal strokes between its upper and lower strokes. The written doubled alphabet is retained as mathbb Z. This row concerns alphabet form; the missing un in H is recorded separately, and no mathematical-consequence flag is attached to the alphabet style.', 'item2_full')
change('Item3, doubled integer alphabet in source quotient',
       r'$\mathbb Z_a/r_a\mathbb Z_a$', r'$\mathbf{Z}_a/r_a\mathbf{Z}_a$',
       r'$\mathbb Z_a/r_a\mathbb Z_a$', False, True, 'misread symbol or index', 'Symbols and indices',
       'The source numerator and denominator Z each have two separated diagonal strokes and a distinct lower a. The alphabet is doubled, not merely a thick plain Z. The target alphabet is included in the target-quotient row; no mathematical-consequence flag is attached to alphabet style.', 'item3_formula')

# Supplied MARKS only. All five remain explicitly undecided.
decisions = []
def decision(id, reading, evidence, crop, confidence='medium'):
    decisions.append(dict(id=id, decision='undecided', reading=reading, evidence=evidence,
                         crop=f'crops/{PAGE}_{crop}.png', box=crops.SPECS[crop][0], confidence=confidence))
decision('M0751', r'\unsure{disjointe|directe}',
         'The d and final -te run are recoverable, but the middle and possible j-descender overlap total below. No resolving stroke can be assigned securely.', 'zero_insert', 'low')
decision('M0752', r'\unsure{$C_a$}',
         'The completed crop contains a narrow open curved upright and a small detached lower oval. C_a is plausible, but the upper form is too small to distinguish conclusively from a compressed letter group.', 'item1_circles_full')
decision('M0753', r'\unsure{les|$C_a$}',
         'The second raised group has a tall left stroke, compressed loops and a leader. These permit les or C_a without a deciding separation of all letters.', 'item1_circles_full', 'low')
decision('M0754', r'\unsure{\ge|>}',
         'The complete r_a relation 1 has a heavy > outline and shorter crossing/lower bars. Retracing prevents a secure decision whether a separate lower equality bar belongs to the final sign.', 'margin2', 'low')
decision('M0755', r'\unsure{\mid|\ne}',
         'In the complete pair r′_a ? r_a et r′_a≠r_a, the first symbol has a near-vertical heavy stroke crossing short bars. The later ≠ is clear, but it does not decide the overworked first sign.', 'margin2', 'low')

implicit_decisions = []
def implicit(id, reading, evidence, crop, confidence='medium'):
    implicit_decisions.append(dict(id=id,decision='undecided',reading=reading,evidence=evidence,
        crop=f'crops/{PAGE}_{crop}.png',box=crops.SPECS[crop][0],confidence=confidence))
implicit('I061-01',r'\deleted{\unsure{sur un cercle}}',
         'The crossed group has readable remnants compatible with sur un cercle, but the heavy strike masks internal joins. Not every letter is plain.', 'item1_circles_full')
implicit('I061-02',r'\deleted{\unsure{de $R$ se trouvant dans une partie}}',
         'The d of dans favours C over H’s sur; the long strike still masks letters elsewhere, so the whole cancelled wording remains marked.', 'item1_replace_full')
implicit('I061-03',r'\deleted{\unsure{anodin}}',
         'The low crossed word under the first margin2 condition has an a-like opening and a later taller d-like stroke, but internal letters are obscured.', 'margin2','low')
implicit('I061-04',r'\unsure{$=$|\deleted{ou}}',
         'Separated straight upper and wavy lower strokes allow equals; a repeated ou under a cancellation remains a physical alternative.', 'footnote')

doubts = [
 dict(place='Inserted item 0',reading=r'\unsure{disjointe|directe}',alternatives='disjointe; directe',confidence='low',reason='The possible descending letter overlaps the lower total insertion; agreement with an operation name would not resolve its owner.'),
 dict(place='Item 1, first raised circle group',reading=r'\inserted{\unsure{$C_a$}}',alternatives='C_a; compressed les-like group',confidence='medium',reason='The completed boundary reveals the whole group, but its narrow upper stroke is not diagnostic.'),
 dict(place='Item 1, second raised group',reading=r'\inserted{\unsure{les|$C_a$}}',alternatives='les; C_a',confidence='low',reason='Tall left and compressed right strokes remain compatible with either reading; the leader fixes the attachment but not the letters.'),
 dict(place='Item 1, cancelled sur un cercle',reading=r'\deleted{\unsure{sur un cercle}}',alternatives='sur un cercle; incompletely recoverable cancelled wording',confidence='medium',reason='The strike obscures enough joins that every letter cannot be certified.'),
 dict(place='Item 1, article after suppression',reading=r"\unsure{d'une|de la}",alternatives="d'une; de la; une possibly an interlinear addition as in H",confidence='medium',reason='The apostrophe-like stroke and u/n humps favour d’une, but overwritten earlier strokes and exact addition state cannot be separated.'),
 dict(place='Item 1, cancelled de R continuation',reading=r'\deleted{\unsure{de $R$ se trouvant dans une partie}}',alternatives='de R se trouvant dans une partie; H has an illegible opening and sur',confidence='medium',reason='Dans is favoured by its d-ascender, but the whole cancellation still hides other letters.'),
 dict(place='Item 2, isolated glyph beside divisor relation',reading=r'\unsure{2|?}',alternatives='2; question-mark-like punctuation',confidence='medium',reason='It is definite dark ink, but its loop, descending stroke and lower foot do not establish its function.'),
 dict(place='Margin to item 2, r_a condition',reading=r'$r_a\unsure{\ge|>}1$',alternatives='r_a≥1; r_a>1',confidence='low',reason='The additional short bars merge with the retraced > outline.'),
 dict(place='Margin to item 2, crossed low word',reading=r'\deleted{\unsure{anodin}}',alternatives='anodin; incompletely recoverable cancelled word',confidence='low',reason='The horizontal cancellation masks central cursive joins; no argument from the classification is used to supply them.'),
 dict(place='Margin to item 2, first divisor relation',reading=r"$r'_a\unsure{\mid|\ne}r_a$ et $r'_a\ne r_a$",alternatives='first relation divides; first relation not-equal',confidence='low',reason='A long heavy stroke crosses shorter bars. The later clear not-equal and the identity d_a=r_a/r′_a do not settle the overwritten sign.'),
 dict(place='Item 3, whole quotient pair',reading=r'$\mathbb Z_a/r_a\mathbb Z_a$ à $\unsure{\mathbb Z|\mathbb Z_a}/d_ar_a\mathbb Z$',alternatives='target numerator Z; target numerator Z_a',confidence='medium',reason='The target numerator foot could contain an attached a; the final denominator Z has no separate a. The source quotient visibly has both a indices.'),
 dict(place='Margin to item 3, underline extent',reading=r'\uline{affaiblissement de}\quad structure \uline{faible}',alternatives='a faint incomplete underline may have extended beneath structure',confidence='medium',reason='Only a short pale trace lies near structure; the full continuous underline of C is not visible.'),
 dict(place='Footnote, extra group before exclure',reading=r'\unsure{$=$|\deleted{ou}}',alternatives='equals shorthand, possibly même; cancelled repeated ou',confidence='medium',reason='The short straight upper bar and separate wavy lower stroke favour equals. Main reader reports the same form in 063 same_temps, which reader_b did not inspect; the local alternative is retained.'),
]

inventory = []
def inv(kind, position, first, hand='his hand'):
    inventory.append(dict(element=f'E{len(inventory)+1:02}',sheet_kind='text',hand=hand,
        kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('text','head of sheet','17; Récapitulation des opérations élémentaires')
inv('insertion','small row between heading and item1','(0°) Somme disjointe|directe')
inv('text','item1 main lines','1°) gommage; circle/deletion/modification description')
inv('insertion','above and between item1 rows','total des repères en a, i.e.; first C_a; second les|C_a; R_a')
inv('deletion','item1 after ou, after suppression, and before remplaçant','sur un cercle; partie; de R se trouvant dans une partie')
inv('margin note','upper left opposite item1','fortement irréversible; r_a≠0')
inv('text','item2 main paragraph','Restriction des; quotient pair; choice count; isolated 2|?')
inv('insertion','above and within item2','gommage partiel uniforme: d’exposant d_a|r_a; groupes de R_a')
inv('deletion','item2 first main row','scalaires')
inv('margin note','left opposite item2','renforcement de structure faible; r_a relation 1; divisor pair; d_a identity')
inv('deletion','under first condition in item2 margin','anodin-like crossed word')
inv('drawing','around item2 marginal classification','open upper/right rule, with separate underlines')
inv('text','item3 main paragraph','extension des groupes de R_a; quotient pair')
inv('insertion','above item3 cancelled opening','Surmarquage uniforme d’exposant d_a>1')
inv('deletion','item3 opening','Extension des')
inv('margin note','left opposite item3','affaiblissement de structure faible; r_a≠0')
inv('drawing','around first row of item3 margin','open upper/right rule; partial underlining')
inv('text','items4 and5','gommage de cercle de découpage C_a; bouchage de trou C_a')
inv('drawing','left of items4 and5','two circles around actual numerals and one joining left brace')
inv('margin note','shared left note for items4 and5','fortement irréversible; separator above and underline below')
inv('text','item6','Découpage le long de C_a (a∈A_0), star reference')
inv('margin note','left opposite item6','fortement irréversible si r_a=0; réversible=anodin si r_a≥1')
inv('deletion','within margin to item6','faible')
inv('text','item7 and product row','Recollement le long de C_a,C_a′; via un élément de R_a wedge R_a′')
inv('insertion','above item7 membership parenthesis','r_a=r_a′, joined by a curved leader')
inv('margin note','lower left opposite item7','r_a=r_a′≥1; réversible=anodin; separator above')
inv('margin note','lower right star footnote','Il faudrait séparer 6°) en deux; r_a zero/nonzero cases')
inv('insertion','above footnote first row','peut-être, with curved insertion leader')
inv('text','footnote last row before exclure','ambiguous equals shorthand or cancelled repeated ou')
inv('text','pale lower-left folio','60','unnamed hand (folio annotation; attribution uncertain)')

notes = [
 dict(id=f'{PAGE}-N01',text='The sheet recapitulates operations numbered 0 through 7, with marginal labels of irreversibility, weak strengthening or weakening, and réversible = anodin. These are the author’s classifications. They are transcribed here; no proof of the geometric classifications was attempted on this page.'),
 dict(id=f'{PAGE}-N02',text='Item2 states restriction from the written cyclic group to a divisor-sized group, with r_a/r′_a=d_a possible choices and d_a>1. The margin contains overworked relations and a crossed word; their uncertainty is retained. The displayed choice count is carried as source background, not independently proved in this reading.'),
 dict(id=f'{PAGE}-N03',text='Item3 writes a target quotient whose final Z has no separate a index; its numerator remains Z|Z_a because the foot is overworked. Both indices are distinct on the preceding source quotient. No missing index has been supplied from the expected group construction.'),
 dict(id=f'{PAGE}-N04',text='The footnote asks whether operation6 should be divided according to r_a=0 or r_a≠0, or whether the zero case should be excluded. The extra two-stroke group before exclure is retained as unsure{equals|cancelled ou}; the proposal does not answer the author’s question.'),
 dict(id=f'{PAGE}-N05',text='The main reader reports that the clear equals in 148_scan063 same_temps has the same straight upper bar and wavy lower bar as the extra group in this footnote. Reader_b did not open that page. This reported handwriting comparison strengthens the leading equals reading but is not a mathematical proof or a reason to erase the local alternative.'),
 dict(id=f'{PAGE}-N06',text='There are 20 distinct evidence places and 24 retained crop files. All 20 initial crops were inspected. Four retained _full versions complete upper boundaries in the two item1 crops, the combined item2 heading/body, and the full-width raised item0/item1-qualification run. The original crop files remain unchanged. These extensions completed evidence boundaries and were not a blind second audit. Original and prepared halves were each viewed once.'),
 dict(id=f'{PAGE}-N07',text='The marginal rules are open upper/right boundaries or oblique separators, rather than closed boxes around all the text. They are represented with open TikZ paths or separator rules. One brace joins the actual circled items4 and5; C’s extra repeated numerals are removed. Underlining is restricted to the strokes seen.'),
 dict(id=f'{PAGE}-N08',text='The pale lower folio reads 60. Its hand is recorded as unnamed and its attribution uncertain; pale appearance alone does not establish who wrote it. The ordinary mathematical sheet, including cancelled passages, remains classified as text.'),
 dict(id=f'{PAGE}-N09',text='The heading has no ink underline. H’s emphasis wrapper on that heading is treated as typographical editorial styling and excluded from the material collation; no underline is invented. By contrast, the two separate diagonal strokes of the integer Z are actual alphabet evidence and are recorded in the quotient collation.'),
]
check_events = [
 dict(statement_id=f'{PAGE}-N01',type='carried as background without fault found',outcome='Read and transcribed the operation names and marginal classifications; no independent proof of reversibility, irreversibility or surface constructions was performed.'),
 dict(statement_id=f'{PAGE}-N02',type='carried as background without fault found',outcome='Read the complete quotient pair, choice-count equation and conditions against the ink. This is a transcription check only, not a new proof of the torsor choice count.'),
 dict(statement_id=f'{PAGE}-N03',type='carried as background without fault found',outcome='Preserved the written source/target indices and the local numerator doubt. No formal correction or proof was used to determine a missing index.'),
 dict(statement_id=f'{PAGE}-N04',type='carried as background without fault found',outcome='Recorded the author’s zero-case question and extra shorthand mark without answering or proving the proposed case division.'),
]

notation = [
 dict(sign=r'\underline r',meaning_or_form='r with a short centred lower bar; no separate lower-right a.',places='Item1, modification de r.',universality='One underlined global parameter on this page; distinct local r_a indices were checked individually.',witness_errors='C gives r_a; H gives plain r.'),
 dict(sign=r'\mathbb Z',meaning_or_form='Z with two distinct diagonal strokes, sometimes retraced; the small a is separately checked.',places='Both quotient pairs in items2 and3.',universality='All clear live Z shapes on this page have the doubled diagonal alphabet. The target numerator in item3 has a locally ambiguous foot.',witness_errors='H uses bold Z. The actual doubled alphabet is recorded for both item2 quotients and the item3 source quotient. The target alphabet is included with its index departure, without an extra mathematical-consequence flag for alphabet style.'),
 dict(sign='l / ell',meaning_or_form='Looped lower-case l as the free-circle index, distinct from digit1.',places='A_l in items5 and7.',universality='Both occurrences have a looped stem and lower exit; no numeral is substituted.',witness_errors='C uses l and H ell, treated as the same letter.'),
 dict(sign='= before anodin',meaning_or_form='Two short horizontal bars; no accent or additional word.',places='Margins to items6 and7.',universality='Both occurrences are visibly equality signs followed by the same word anodin.',witness_errors='H reads à followed by illegible wording and près at both places.'),
 dict(sign=r'\unsure{$=$|\deleted{ou}}',meaning_or_form='A straight upper bar separated from a wavy lower run; likely equals shorthand, with cancelled repeated ou retained as alternative.',places='Footnote, immediately before exclure.',universality='One ambiguous occurrence on this assigned page. Main reader reports a matching equals form in 063 same_temps; that page was not opened by this reader.',witness_errors='Both witnesses omit this separate ink group.'),
 dict(sign='curved insertion leader',meaning_or_form='A curved line beneath an added group that descends to the intended gap, without striking the letters.',places='Item1 qualification and second raised group; item7 equality; footnote peut-être.',universality='These leaders were checked at each occurrence, independently of the cancellation lines.',witness_errors='H treats part of item1’s live qualification as struck and omits addition state for the item7 equality and peut-être.'),
 dict(sign='open marginal boundary',meaning_or_form='Upper rule with descending right end and no closing left edge; other oblique rules separate notes.',places='Margins to items2 and3; separators before shared4/5,6 and7 notes.',universality='Geometry varies at each note; no single closed frame is imposed.',witness_errors='C does not reproduce these boundaries; H describes them in editorial notes rather than drawing them.'),
]
abbreviations = [
 dict(form='i.e.',expansion='id est'),
 dict(form=r'\unsure{$=$|\deleted{ou}}',expansion='Possibly même, if the equals-shorthand reading is correct; no expansion is inserted in the transcription.'),
]

def block(start,end):
    return tex[tex.index(start):tex.index(end,tex.index(start))].strip()
margin2 = block(r'\margin{%\n'.replace('\\n','\n')+'\\begin{tikzpicture}[baseline=(m2label.base)]', '$3^\\circ$)')
margin3 = block(r'\margin{%\n'.replace('\\n','\n')+'\\begin{tikzpicture}[baseline=(m3label.base)]', r'\margin{\rule{2cm}{.3pt}\\fortement \uline{irréversible}}')
brace = block(r'\noindent\begin{tikzpicture}[baseline=(ops.center)]', '$6^\\circ$)')
second_boxes=[]
def box(kind,coords,reading):
    second_boxes.append(dict(box=f'B{len(second_boxes)+1:02}',kind=kind,
                             **dict(zip(('x0','y0','x1','y1'),coords)),reading=reading))
box('handwritten number',[248,22,1430,155],r'\mspage{17} Récapitulation des opérations élémentaires')
box('insertion',[300,108,1660,232],r"\inserted{$(0^\circ)$ Somme \unsure{disjointe|directe}} \inserted{\uline{total} des repères en $a$, i.e.}")
box('insertion',[300,198,1645,389],r'$1^\circ$) \uline{gommage} des repères se trouvant sur un cercle \inserted{\unsure{$C_a$}} de recollement \inserted{\unsure{les|$C_a$}}, ou \deleted{\unsure{sur un cercle}}')
box('struck passage',[375,312,1643,602],r"de découpage $\Longleftrightarrow$ suppression \unsure{d'une|de la} \deleted{partie} \inserted{$R_a$} $(a\in A)$ $\Longleftrightarrow$ modification de $\underline r$ en le \deleted{\unsure{de $R$ se trouvant dans une partie}} remplaçant par $0$ en $a$.")
box('margin note',[50,228,319,523],r'\margin{\uline{fortement irréversible}\quad $r_a\ne0$}')
box('handwritten number',[290,520,1663,1040],block('$2^\\circ$)',r'\margin{%'))
box('doubtful formula',[14,482,434,1063],margin2)
box('insertion',[312,1008,1640,1165],r"$3^\circ$) \deleted{Extension des} \inserted{\uline{Surmarquage uniforme} \uline{d'exposant} $d_a>1$}")
box('doubtful formula',[386,1115,1640,1390],r'--- i.e. extension des groupes de $R_a$ de $\mathbb Z_a/r_a\mathbb Z_a$ à $\unsure{\mathbb Z|\mathbb Z_a}/d_ar_a\mathbb Z$,')
box('margin note',[24,984,409,1392],margin3)
box('handwritten number',[260,1388,1617,1697],brace)
box('margin note',[18,1380,319,1772],r'\margin{\rule{2cm}{.3pt}\\fortement \uline{irréversible}}')
box('handwritten number',[310,1638,1620,1807],r'$6^\circ$) Découpage le long de $C_a$ $(a\in A_0)$ \({}^*\)')
box('margin note',[20,1642,418,2098],r'\margin{\rule{2cm}{.3pt}\\fortement irréversible si $r_a=0$, \deleted{faible} réversible = anodin si $r_a\ge1$.}')
box('insertion',[310,1775,1668,2140],r"$7^\circ$) Recollement le long de $C_a,C_{a'}$ (avec $a,a'\in A_l$, $a\ne a'$, \inserted{$r_a=r_{a'}$}), via un élément de $R_a\mathbin{\wedge}R_{a'}$.")
box('margin note',[20,1907,413,2300],r"\margin{\rule{2cm}{.3pt}\\$r_a=r_{a'}\ge1$\quad réversible = anodin}")
box('margin note',[1005,2010,1671,2338],r"\margin{\({}^*\) Il faudrait \inserted{peut-être} séparer $6^\circ)$ en deux, suivant que $r_a=0$ ou $r_a\ne0$ (ou \unsure{$=$|\deleted{ou}} exclure le cas $r_a=0$?)}")
box('handwritten number',[22,2294,88,2349],r'\mspage{60}')

# Some raw Python strings above quote apostrophes with a backslash for readability;
# that backslash is not part of the source TeX and is removed before serialization.
def clean(value):
    if isinstance(value,str): return value.replace("\\'", "'")
    if isinstance(value,list): return [clean(v) for v in value]
    if isinstance(value,dict): return {k:clean(v) for k,v in value.items()}
    return value

record=clean(dict(page=PAGE,reader='reader_b',lines_read=56,places_cropped=20,changes=changes,decisions=decisions,
    implicit_decisions=implicit_decisions,doubts=doubts,inventory=inventory,notes=notes,
    check_events=check_events,notation=notation,abbreviations=abbreviations,second_boxes=second_boxes))
out=ROOT/'proposed'/f'{PAGE}.json'
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:len(record[k]) for k in ('changes','decisions','implicit_decisions','doubts','inventory','second_boxes')}))
