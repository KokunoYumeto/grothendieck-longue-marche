import csv
import json
import re
from pathlib import Path

OUT = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan041')
PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan041')
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
F = (OUT / 'candidate.tex').read_text()
BOXES = json.loads((OUT / 'crop_boxes.json').read_text())

def part(text, start, end, keep_end=True):
    a = text.index(start)
    b = text.index(end, a) + (len(end) if keep_end else 0)
    return text[a:b]

def crop(label):
    return 'crops/148_scan041_' + label + '.png'

changes = []
def change(place, c, h, final, ink, label, ac, ah, kind, math=False, confidence='high'):
    assert not c or c in C, ('C quotation not exact', place, c)
    assert not h or h in H, ('H quotation not exact', place, h)
    changes.append(dict(place=place, c=c, h=h, final=final, ink=ink,
                        crop=crop(label), box=BOXES[label], confidence=confidence,
                        kind=kind, against_c=ac, against_h=ah, math=math))

# Printed source and dated frame.
change('printed first job line', r'\texttt{/*JOB=CRAY2,ACCT=*********,ALL=M06}', '',
       r'\texttt{/*JOB=CRAY2;ACCT=*********,ALL=M06}',
       'After CRAY2 there is a raised dot over a lower comma stroke. Nine separate stars precede ALL=M06. The entire printed line is visible; H omits it.',
       'printed_header', True, True, 'misread symbol or index')
change('printed job identifier', r'\texttt{J0231CNU}', '', r'\texttt{J0231CNU}',
       'The hooked J, oval 0, digits 2, 3, 1 and the final CNU are individually visible.',
       'printed_job_id', False, True, 'omission')
change('printed JOB control line', r'\texttt{// JOB MSGLEVEL=(0,0),MSGCLASS=Z}', '',
       r'\texttt{// JOB MSGLEVEL=(0,0),MSGCLASS=Z}',
       'Both initial slashes, JOB, the two field names, parentheses, zeroes, comma and final Z are legible machine printing.',
       'printed_header', False, True, 'omission')
change('printed EXEC token', r'\texttt{// EXEC CSSBATCH}', '',
       r'\texttt{// EXEC \unsure{CSS3ATCH|CSSBATCH}}',
       'The disputed character has two open left halves, unlike the solid left stem of the B in JOB. A damaged B remains possible, so 3 is first with B retained as an alternative.',
       'printed_header', True, True, 'misread word', confidence='medium')
change('printed CRAYIN line', r'\texttt{//CRAYIN DD *}', '', r'\texttt{//CRAYIN DD *}',
       'The two slashes directly precede CRAYIN; DD and one terminal star are visible.',
       'printed_header', False, True, 'omission')
date_final = part(F, r'\figure{\begin{tikzpicture}[x=1cm,y=1cm]', r'\end{tikzpicture}}')
change('date and its frame', r'\uline{\unsure{Oct. 4 83|Oct. 1983}}', r'\marginal{Oct.\ 1983}', date_final,
       'The 4 has an open left cup joining its descending right limb, followed by distinct 8 and 3. The surrounding line has left, lower and right sides and remains open above.',
       'date', True, True, 'misread symbol or index')

# Upper diagram and its neighboring conditions.
change('upper diagram first R', r'\unsure{\mathbb R}', 'R = RR/\\sigma_1', 'R=RR/\\sigma_1',
       'The first R has one upright, a bowl and a diagonal leg, with an entry curl. No parallel second upright is visible, unlike the clear doubled N below.',
       'upper_diagram', True, False, 'misread symbol or index', True, 'medium')
change('upper diagram quotient RR', r'\unsure{RR}', 'RR', 'RR',
       'The small numerator contains two compressed but distinct upright-and-bowl forms, each with a leg.',
       'upper_diagram', True, False, 'misread symbol or index', True)
change('upper diagram central RR', r'\overset{\sigma_0,\sigma_1}{\unsure{RR}}', 'RR', r'\overset{\sigma_0,\sigma_1}{RR}',
       'Both large R forms have separate upright, bowl and leg strokes. The sigma labels above are 0 and 1.',
       'upper_diagram', True, False, 'misread symbol or index', True)
change('upper diagram sigma below A', r'\vec A\arrow[l]\arrow[loop below,"\sigma"]',
       'sous $\\vec{A}$, un\n$\\sigma$.', r'\underset{\sigma}{\vec A}\arrow[l]',
       'A sigma is written below the central vector A. There is no loop shaft or loop arrowhead around it.',
       'upper_diagram', True, False, 'drawing or diagram', True)
change('upper diagram A0-to-A hook', r'\vec A_0\arrow[l,leftrightarrow]\arrow[d,"\sigma"]',
       r'\vec{A} \arrow[l] \arrow[r, leftrightarrow] & \vec{A}_0 \arrow[d, "\sigma"]',
       r'\vec A_0\arrow[l,hook]\arrow[d,"\sigma"]',
       'The horizontal shaft has a pointed left head and a rounded hook at its right tail. The right end lacks the two opposed arms of an arrowhead.',
       'upper_diagram', True, True, 'drawing or diagram', True)
change('upper diagram target N alphabet', r'\mathbb N', 'N', r'\mathbb N',
       'The N has two close parallel strokes at its left upright, unlike the plain R above.',
       'upper_diagram', False, True, 'misread symbol or index', True)
change('condition a abbreviated ss', 'ss', r'\uncertain{sans}', 'ss',
       'The written form consists of two compressed s loops; there are no a and n strokes between them.',
       'conditions_ab', False, True, 'abbreviation expanded or spelling modernised')
change('condition a raised t in point abbreviation', 'pt fixe', 'pt fixe', r'p\textsuperscript{t} fixe',
       'The short t is raised above the p baseline. The following fixe is singular, without a separate final s.',
       'conditions_ab', True, True, 'misread symbol or index')
change('condition b capital Compatible', 'supp compatible avec', 'supp compatible avec', 'supp Compatible avec',
       'The initial open C is markedly taller than the following low letters; the remaining letters read ompatible.',
       'conditions_ab', True, True, 'misread word')
change('condition c RR', r'\unsure{RR}', 'RR', 'RR',
       'Two separate upright, bowl and leg forms are visible before the slash.',
       'condition_c', True, False, 'misread symbol or index', True)
change('condition c plain D infinity', r'\mathbb D_\infty', r'\mathbb{D}_{\infty}', r'D_\infty',
       'Here D has a single left stem. The b-line D immediately above has a visibly doubled stem.',
       'condition_c', True, True, 'misread symbol or index', True)
change('condition c hooked arrow', r'\longleftrightarrow', r'\xrightarrow{\sim}', r'\lhook\joinrel\longrightarrow',
       'The left end turns into a small rounded hook and the right end has an arrowhead. There is no left arrowhead and no tilde above the shaft.',
       'condition_c', True, True, 'misread symbol or index', True)
change('condition c small bij annotation', '', 'bij', r'\unsure{\mathrm{bij}}',
       'A small three-letter group below the arrow favors bij: an initial loop-and-stem, a short middle stroke and a descending final stroke. Its compactness prevents full resolution.',
       'condition_c', True, False, 'omission', True, 'low')
change('condition c lower curled sign', r'\unsure{\exists!}', r'\exists', r'\unsure{\exists}',
       'The lower mark has several horizontal or curled strokes, but no separate upright-and-dot exclamation mark. It may be an exists-like sign or strokes involving the j descender and an underline.',
       'condition_c', True, False, 'text not on the page', True, 'low')
change('condition d abbreviated opening', r'\unsure{évt}', 'évt.', r'\unsure{évt.}',
       'A short final mark follows the tall last stroke. The whole abbreviation favors évt. but remains locally uncertain.',
       'condition_d', True, False, 'misread symbol or index', confidence='low')
change('condition d parenthetical alternative', r'\unsure{cs hyperboliques|ou hyperbolique}', 'ou hyperbolique',
       r'\unsure{ou hyperbolique|cs hyperboliques}',
       'The first short word favors two rounded ou strokes; the final plural stroke of hyperbolique(s) is not secure. Both readings remain, with ou hyperbolique first.',
       'condition_d', True, False, 'misread word', confidence='low')
change('condition d canceled formula', r'\deleted{\unsure{2g(s)}}', r'\struck{\ill{}}', r'\deleted{\unsure{2g(s)}}',
       'Under the cancellation, a leading 2, a descending g-like curve and parenthesis-like strokes permit 2g(s); the obscured strokes prevent certainty.',
       'condition_d', False, True, r'readable ink left as \ill{}', True, 'low')
change('condition d punctuation after cancellation', ':\\ 2g(s)+\\nu_s\\ge3', '', r'\unsure{:}',
       'Two detached marks occur between the canceled term and the live formula. Their alignment is imperfect, so the colon is retained with doubt.',
       'condition_d', False, True, 'omission', True, 'low')
change('first margin inequality subscript', r'3\unsure{g_s|g_p}-3+\nu_s\ge0', r'3g_s - 3 + \nu_s \geqslant 0',
       r'3\unsure{g_p|g_s}-3+\nu_s\ge0',
       'The first g subscript has a closed p-like body. The g descender overlaps it, unlike the clear open s in the third inequality, so p remains first with s as an alternative.',
       'inequalities', True, True, 'misread symbol or index', True, 'low')
change('second margin inequality subscript', r'2\unsure{g_s|g_p}-2+\nu_s\ge1', r'2g_s - 2 + \nu_s \geqslant 1',
       r'2\unsure{g_p|g_s}-2+\nu_s\ge\unsure{1}',
       'The subscript again has a closed p-like outline, partly entangled with the g descender. The right-hand 1 has a left loop or retouch and is also left doubtful.',
       'inequalities', True, True, 'misread symbol or index', True, 'low')

# Operations and right-hand headings.
change('operation 1 terminal sign', r'\unsure{$+$}', '', r'\unsure{$+$}',
       'A cross-shaped stroke follows Somme. It may be a separate plus, but a terminal writing stroke cannot be excluded.',
       'somme_sign', False, True, 'omission', True, 'low')
change('operation 4 sans', r'\uline{\unsure{sous|sans}}', r'\emph{sans}', r'\uline{sans}',
       'The middle strokes form an a oval followed by n, between the two s forms. A separate underline lies below the word.',
       'operations_45', True, False, 'misread word')
change('operation 4 singular gommage', 'gommage', 'gommages', 'gommage',
       'The final e ends without a distinct subsequent s; the word is singular in the ink.',
       'operations_45', False, True, 'misread word')
change('operation 2 canceled repères', r'\deleted{\unsure{repères}}', r'\struck{\ill{}}', r'\deleted{\unsure{repères}}',
       'The struck word has a visible p descender and surviving loops consistent with repères. The overlying stroke hides internal letters, so the reading remains tentative.',
       'operations_23', False, True, r'readable ink left as \ill{}', confidence='low')
change('parallel strokes between operations 3 and 6',
       r'\draw[<-] (0,0)--(1.5,.12);\draw[<-] (0,-.08)--(1.5,.04);',
       'un double trait sépare 3) de\n6)',
       '\\draw (-.15,-3.86)--(6.2,-3.69);\n\\draw (-.15,-3.99)--(6.2,-3.82);',
       'Both strokes run as plain parallel lines. Neither left end has two converging arms forming an arrowhead.',
       'operations_67', True, False, 'drawing or diagram')
change('short double strokes beneath operation 7', r'7) \uline{gommage} de cercles de découpage',
       r'\item[7)] \emph{gommage de cercles de découpage}',
       '\\node[anchor=base east,inner sep=0pt] at (.25,-5.9) {7)};\n\\node[anchor=base west,inner sep=0pt] at (.85,-5.9) {gommage de cercles de découpage};\n\\draw (-.55,-6.19)--(1.04,-6.09);\n\\draw (-.55,-6.31)--(1.04,-6.22);',
       'The two lines begin in the left margin and stop around the initial g. They do not extend beneath the whole word or phrase.',
       'operations_67', True, True, 'drawing or diagram')
change('vertical note numeral cluster', '4,5 inverses', '', r'\unsure{4,5}',
       'The top cluster permits 4,5, with an open first numeral and a bent second form, but not every small stroke is secure.',
       'vertical_note', False, True, 'omission', confidence='low')
change('vertical note l’un', "l'un de l'autre", "l'une de l'autre", "l'un de l'autre",
       'The word ends at the n; there is no separate terminal e before de.',
       'vertical_note', False, True, 'misread word')
change('vertical note condition', "à condition que l'on ne découpe que par\ndes cercles \\uline{marqués}",
       'à \\uncertain{modifications}\nprès \\ill{} \\uncertain{données} \\ill{} \\uncertain{des} cercles\nmarqués',
       "à condition que l'on ne découpe que par\ndes cercles \\uline{marqués}",
       'The c-o-n-d-i-t-i-o-n sequence is followed by que l’on ne découpe que par des cercles. The q descender and the tall p in découpe are visible; marqués has an underline.',
       'vertical_note', False, True, 'misread word')
change('first circle heading capital', r'\uline{Cercles de découpage}', r'\text{cercles de découpage}', r'\uline{Cercles de découpage}',
       'The initial C is much taller than the interior c. The entire heading is underlined.',
       'circle_headings', False, True, 'misread word')
change('second circle heading capital', r'\uline{Cercles de raccord}', r'\text{cercles de raccord}', r'\uline{Cercles de raccord}',
       'The initial C has the same large open form as the first heading, and a line extends below the whole phrase.',
       'circle_headings', False, True, 'misread word')
change('first graph heading plurals and underline gap', r'\uline{graphes pondérés}', r'\text{graphe pondéré}', r'\uline{graphes} \uline{pondérés}',
       'Small terminal s strokes follow both words. Two separate underlines leave a gap between graphes and pondérés.',
       'graph_headings', True, True, 'other')
change('middle graph heading plural forms', 'graphes bipondérés', r'\text{graphe bipondéré}', r'graphes \unsure{bipondérés|bipondéré}',
       'Terminal curves favor the plurals. The last stroke of bipondérés is compressed enough to retain the singular alternative.',
       'graph_headings', False, True, 'misread word', confidence='medium')
change('middle graph heading canceled and double-underlined marqués', r'\deleted{\unsure{marqués}}',
       '« marqué » est biffé après « graphe bipondéré »', r'\deleted{\uuline{\unsure{marqués|marqué}}}',
       'A heavy line strikes the word, and two separate surviving strokes run below it. The last letter favors s but remains obscured.',
       'graph_headings', True, True, 'deletion state', confidence='medium')
change('last graph heading plural forms', 'graphes pondérés marqués', r'\text{graphe pondéré marqué}', 'graphes pondérés marqués',
       'The three words end in short final s curves rather than stopping at their preceding letters.',
       'graph_headings', False, True, 'misread word', confidence='medium')
change('capital Sommets', 'Sommets de marquage', 'sommets de marquage', 'Sommets de marquage',
       'The initial S is large and rises above the following low letters.',
       'sommet_labels', False, True, 'misread word')
change('interlinear rigidification phrase', r'\unsure{ou rigidification|antirigidification}', '\\add{ou\nde rigidification}',
       r'\inserted{ou de rigidification}',
       'Separate small ou and de precede rigidification. The phrase is written below marquage between the principal lines, rather than on the main baseline.',
       'sommet_labels', True, False, 'insertion or placement', confidence='medium')
change('brace beside vertex labels', r'\left\{\begin{array}{l}\text{périphériques}\\\text{intérieurs}\end{array}\right.',
       r'(\uncertain{périphériques}\,/\,intérieurs)',
       r'\left\{\begin{array}{l}\text{périphériques}\\\text{intérieurs}\end{array}\right.',
       'A left brace joins two vertically separated words, périphériques and intérieurs. The source does not use a slash between parenthesized labels.',
       'sommet_labels', False, True, 'drawing or diagram')
change('capital Cercles in marked-circle line', 'Cercles marqués (non marqués)', 'cercles marqués (non marqués)', 'Cercles marqués (non marqués)',
       'The first C is tall and open. Both marqués endings have a separate small s, and non is enclosed with the second word in parentheses.',
       'marked_circles', False, True, 'misread word')

# Right-hand symbols and diamonds.
change('canceled symbol before SDTtop', r'\deleted{\unsure{\mathcal T}}', r'\struck{\ill{}}', r'\deleted{\unsure{\mathcal T}}',
       'The crossed blob retains a broad cap and descending curled stroke compatible with calligraphic T, but the deletion prevents certainty.',
       'combinatorial_type', False, True, r'readable ink left as \ill{}', True, 'low')
change('possible comma after canceled symbol', ',\\ SD\\unsure{\\mathcal T}_{\\mathrm{top}}', '', r'\unsure{,}',
       'A small curved stroke beside the canceled blob could be a comma or part of the canceled glyph. No separate comma is secure.',
       'combinatorial_type', False, True, 'omission', confidence='low')
change('live SD calligraphic T top', r'SD\unsure{\mathcal T}_{\mathrm{top}}', r'SD\mathcal{T}_{\mathrm{top}}', r'SD\mathcal T_{\mathrm{top}}',
       'The T has a broad looped cap, curved descending stem and lower curl, matching the clear calligraphic T forms in the table below.',
       'combinatorial_type', True, False, 'misread symbol or index', True)
change('divider beside canceled symbols', '', '', r'\draw (3.3,.15)--(3.3,-1.95);',
       'A long upright divider stands to the right of the canceled groups and to the left of the small notation-column phrase. It is separate from the diagonal cancellation strokes.',
       'canceled_symbols', True, True, 'omission')
change('notation-column phrase and separate plus-minus', r'$\unsure{\text{avec inv}}^{\pm}$',
       'avec $\\omega^{L}$\n$\\pm$', r'\unsure{avec $\omega^L$|avec inv}\qquad$\pm$',
       'After avec are two disconnected curls, a detached dot and an upper L-like stroke. They favor omega with raised L but do not settle the alternative inv. The plus-minus stands separately to the right at the main level.',
       'notation_columns', True, False, 'misread symbol or index', True, 'low')
change('standalone calligraphic T in notation column', r'$\unsure{\mathcal T}$', r'$\mathcal{T}$', r'$\mathcal T$',
       'The glyph has the same looped cap and curled lower body as the three calligraphic T forms directly below it.',
       'notation_columns', True, False, 'misread symbol or index', True)
change('large diamond graphes b label', r'\unsure{graphes b}', 'graphes b', 'graphes b',
       'The final b has a plain tall ascender and a closed lower bowl. All letters of graphes are visible before it.',
       'large_diamond', True, False, 'misread word')
large_c = part(C, r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]', r'\unsure{graphes b}\qquad\text{graphes pondérés}\qquad\text{graphes}')
large_h = part(H, r'\begin{tikzcd}[column sep=small, row sep=small]'+'\n & \\mathcal{T}', r'\end{tikzcd}')
large_f = part(F, r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]', r'\end{tikzcd}}')
change('large diamond annotation placement', large_c, large_h, large_f,
       'The top annotation lies to the upper right of calligraphic T, graphes b to the left of S calligraphic T, graphes pondérés to the right of D calligraphic T, and graphes beside the lower SD calligraphic T. The four shafts are headless.',
       'large_diamond', True, False, 'drawing or diagram', True)
small_c = part(C, r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small]'+'\n\\&t', r'\end{tikzcd}}')
small_h = part(H, r'\begin{tikzcd}[column sep=small, row sep=small]'+'\n & \\mathbb{L}', r'\end{tikzcd}')
small_f = part(F, r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=small,row sep=small]'+'\n\\&\\unsure{t', r'\end{tikzcd}}')
change('small diamond repeated glyph and lowercase prefixes', small_c, small_h, small_f,
       'Each repeated glyph has a doubled tall body, a crossing bar and a lower foot, leaving t versus blackboard L unresolved. The s and d prefixes are lowercase cursive. All four connecting strokes are bent plain lines without arrowheads.',
       'small_diamond', False, True, 'drawing or diagram', True, 'low')

# Relative twist, boxed diagram, and final sloping passage.
change('canceled word after Le', r'\deleted{\unsure{foncteur|point}}', r'\struck{\uncertain{point}}', r'\deleted{\unsure{point|foncteur}}',
       'The canceled word has a long p-like descender and a short body favoring point. The crossing stroke prevents a complete letter-by-letter resolution; foncteur remains an alternative.',
       'relative_twist', True, False, 'misread word', confidence='low')
change('interlinear relatif and its stroke', 'relatif à un cercle', r'\add{\emph{relatif}}',
       r'\inserted{\unsure{\uline{relatif}|\deleted{relatif}}}',
       'Relatif is placed below the canceled word between the lines. A dark stroke passes through or just under its left portion, so underline versus cancellation is explicitly left open.',
       'relative_twist', True, False, 'insertion or placement', confidence='low')
change('relative twist first parameter', r'$\tau_r$', r'$\tau_{\rho}$', r'$\tau_r$',
       'The subscript has a short upright and a right shoulder, without the closed bowl and descending stem of rho.',
       'relative_twist', False, True, 'misread symbol or index', True)
change('relative twist canceled rational parameter', r'\deleted{$(r\in\mathbb Q)$}', r'\struck{($\rho \in Q$)}', r'\deleted{$(r\in\mathbb Q)$}',
       'The canceled parameter has the same short r form. The Q includes an internal upright in addition to its outer oval and tail; parentheses and membership sign survive the deletion.',
       'relative_twist', False, True, 'misread symbol or index', True, 'medium')
change('relative twist à after parameter', 'relatif à un cercle', ': un cercle', 'à un cercle',
       'A small accented à occurs before un; the interlinear relatif is accounted for separately.',
       'relative_twist', False, True, 'misread word')
change('relative twist en termes', 'en termes de 4) 5)', r'au \uncertain{moyen} de 4)5)', 'en termes de 4) 5)',
       'The lower line begins en, followed by a tall crossed t and the connected e-r-m-e-s strokes of termes.',
       'relative_twist', False, True, 'misread word')
change('relative twist identity parameter', r'\tau_r=\mathrm{id}', r'\tau_{\rho} = \mathrm{id}', r'\tau_r=\mathrm{id}',
       'The subscript again has a short r shoulder and no rho bowl or descending stem.',
       'relative_twist', False, True, 'misread symbol or index', True)
change('relative twist integral parameter and alphabet', r'r\in\mathbb Z', r'\rho \in \mathbf{Z}', r'r\in\mathbb Z',
       'The parameter is the same r, and Z has a distinct retraced or doubled diagonal. The integral alphabet is retained literally.',
       'relative_twist', False, True, 'misread symbol or index', True, 'medium')
change('relative twist terminal period', '$r\\in\\mathbb Z$.', '$\\rho \\in \\mathbf{Z}$', '$r\\in\\mathbb Z$.',
       'A detached dark point follows the lower right end of the Z rather than extending its diagonal.',
       'relative_twist', False, True, 'omission', confidence='medium')
change('boxed diagram S subscript', r'S_1', r'S_{*}', r'S_1',
       'The subscript is a single descending upright with a short head and dark foot, not several rays meeting as a star.',
       'boxed_diagram', False, True, 'misread symbol or index', True)
change('boxed diagram first calligraphic T', r'\unsure{\mathcal T}_{g,\nu}^{\pm1}', r'\mathcal{T}^{\pm 1}_{g,\nu}', r'\mathcal T_{g,\nu}^{\pm1}',
       'The first T has a looped top and curled bottom. Its g, comma, nu and ±1 are also visible in the same formula.',
       'boxed_diagram', True, False, 'misread symbol or index', True)
change('boxed diagram second calligraphic T', r'\unsure{\mathcal T}_{g,\nu}^{\pm1}', r'\mathcal{T}^{\pm 1}_{g,\nu}', r'\mathcal T_{g,\nu}^{\pm1}',
       'The second T has the same cap and curled stem as the first. The neighboring indices and exponent were read with it.',
       'boxed_diagram', True, False, 'misread symbol or index', True)
change('boxed diagram final factor', r'\unsure{[\pm1]|[\mathrm I\mid J]}', '[\\pm 1]', r'[\pm1]',
       'Inside the brackets the first sign has two horizontal bars and one vertical, matching the ± signs above the two T letters; the next stroke is 1.',
       'boxed_diagram', True, False, 'misread symbol or index', True, 'medium')
box_c = part(C, r'\diagram{\fbox{', r'\end{tikzcd}}}')
box_h = part(H, r'\boxed{S_{*}', '[\\pm 1]}')
box_f = part(F, r'\diagram{\begin{tikzpicture}', r'\end{tikzpicture}}')
change('boxed diagram frame gaps', box_c, box_h, box_f,
       'The left upright starts below the top horizontal line. At the upper right a short downward turn ends before the longer right upright resumes. The lower sides join, but the upper corner gaps are preserved.',
       'boxed_diagram', True, True, 'drawing or diagram', True, 'medium')
canceled_c = part(C, r'\deleted{$\unsure{\mathcal T_{g,\nu}^{\pm}', '(TSD)_{g,\\nu}}$}')
canceled_h = r'\struck{$\mathcal{T}_{g,\ill{}}$ \ill{} $(T S R)_{g,\nu}$}'
canceled_f = part(F, r'\deleted{$\unsure{\mathcal T_{g,\nu}^{\pm}', '(TSD)_{g,\\nu}}$}')
change('canceled formulas below the box', canceled_c, canceled_h, canceled_f,
       'The first two groups retain strokes consistent with calligraphic T, g/nu, ± and top, but cancellation prevents full resolution. The last parenthesized letter has an upper bowl and an oblique leg favoring R; the crossing deletion line leaves D possible.',
       'canceled_formulas', True, True, 'misread symbol or index', True, 'low')
change('colon before live T formula', '', '} :\n$\\mathcal{T}_{g,\\nu} S_{\\alpha}$', ':',
       'Two discrete dark dots stand between the canceled material and the live formula. Root and reader independently read the colon.',
       'canceled_formulas', True, False, 'omission', confidence='medium')
change('live plain T formula below box', r'\unsure{T_{g,\nu}S_\alpha}', r'\mathcal{T}_{g,\nu} S_{\alpha}', r'T_{g,\nu}S_\alpha',
       'The T has a straight horizontal cap and one stem with a small hooked foot, without the looped cap or curled body of calligraphic T. The g, nu, S and alpha are visible.',
       'canceled_formulas', True, True, 'misread symbol or index', True, 'medium')
change('last paragraph abbreviated iso', r'\uline{iso}', r'\emph{isom}', r'\uline{iso}',
       'The underline lies below i-s-o. The terminal writing stroke does not form a separate m with two humps.',
       'iso_twist_open', False, True, 'abbreviation expanded or spelling modernised')
change('last paragraph canceled est un', r'\deleted{\unsure{est un}}', r'\struck{\ill{}}', r'\deleted{\unsure{est un}}',
       'The strike leaves an e-like entry, a tall t-like stroke and low connected strokes compatible with un, but not every letter is plain.',
       'iso_twist_open', False, True, r'readable ink left as \ill{}', confidence='low')
change('last paragraph relatif à', 'relatif à\nun cercle', 'relatif :\nun cercle', 'relatif à\nun cercle',
       'A small a body and detached accent precede un, rather than two vertically aligned punctuation dots.',
       'iso_twist_open', False, True, 'misread word')
change('last paragraph de raccord', 'de découpage ou de raccord', 'de découpage ou non)', 'de découpage ou de raccord',
       'After ou, the short de and the r-a-c-c-o-r-d sequence are visible; the d has a tall final ascender.',
       'bottom_circle', False, True, 'misread word')
change('last paragraph marqué ou pas and parenthesis scope', 'marqué ou pas)', r'\uncertain{marqué} ou non,', 'marqué ou pas)',
       'The q descender in marqué and the p ascender and a body in pas are visible. The closing parenthesis follows pas, so the marked/unmarked phrase remains inside it.',
       'bottom_circle', False, True, 'misread word')
change('colon after pas parenthesis', 'pas),', 'ou non,', 'pas):',
       'Two separate dark dots follow the closing parenthesis. Their vertical pairing is distinct from the surrounding paper mottles.',
       'bottom_circle', True, True, 'misread symbol or index', confidence='medium')
change('last paragraph interlinear recollement phrase', r'\inserted{\unsure{ou de recollement}}', r'\add{ou de} relatif ;', r'\inserted{\unsure{ou de recollement}}',
       'The thick interlinear addition clearly begins ou de. The following r-e-c-o-l-l-like strokes favor recollement, while the ending remains too compressed to resolve.',
       'bottom_circle', False, True, 'misread word', confidence='low')
change('marqué inside final tau parenthesis', '(pour un cercle de découpage)', '(pour un cercle de découpage)', '(pour un cercle de découpage marqué)',
       'Before the closing parenthesis there is a separate word with m-a-r, a long q descender and an accented ending: marqué. Both witnesses omit it.',
       'new_structure', True, True, 'omission')
change('final une nouvelle structure', 'est une\n\\uline{nouvelle structure}',
       'est\n\\uncertain{composé} \\uncertain{des} nouvelles structures', 'est une nouvelle structure',
       'The text after est reads une, then nouvelle with its two tall l strokes, followed by singular structure. There are no visible composé or des words and no final s after structure.',
       'new_structure', False, True, 'misread word')
underline_f = part(F, r'\begin{tikzpicture}[baseline=(une.base)]', r'\uline{structure}')
change('separate final underlines', r'\uline{nouvelle structure}', 'nouvelles structures', underline_f,
       'The first underline starts near or within une and runs beneath nouvelle. A separate lower line lies beneath structure; the two are not one continuous underline.',
       'new_structure', True, True, 'drawing or diagram')
change('final word importante', r'\unsure{importante}', r'\uncertain{équivalentes}', r'\unsure{importante}',
       'An initial dotted i, connected m-like strokes, a descending p and later tall t strokes favor importante. The ending remains uncertain; the q and v pattern needed for équivalentes is absent.',
       'new_structure', False, True, 'misread word', confidence='low')
change('no secure final period after importante', r'\unsure{importante}.', r'\uncertain{équivalentes}', r'\unsure{importante}',
       'The final connected word ends in a writing curl. No separate terminal punctuation dot is visible beside it.',
       'new_structure', True, False, 'text not on the page', confidence='medium')
change('unattributed foliation', r'\mspage{40}', '', r'\margin{40}',
       'A thin gray open 4 and oval 0 are written at the lower left. Their hand differs from the heavy note hand; no attribution is supplied.',
       'folio', False, True, 'omission')

decisions = []
def decision(id, status, reading, ink, label, confidence):
    decisions.append(dict(id=id, decision=status, reading=reading, ink=ink,
                          crop=crop(label), box=BOXES[label], confidence=confidence))

decision('M0619','first','Oct. 4 83','The open left cup and long right limb make a single4, followed by8 and3. The frame is open above.','date','high')
decision('M0620','other','R','One upright, bowl and diagonal leg are visible; no second parallel stem occurs as in the N below.','upper_diagram','medium')
decision('M0621','first','RR','The small quotient numerator has two separate compressed upright-and-bowl forms.','upper_diagram','high')
decision('M0622','first','RR','The larger central group has two distinct upright, bowl and leg forms.','upper_diagram','high')
decision('M0623','first','RR','The condition-c numerator contains two complete R forms.','condition_c','high')
decision('M0624','undecided',r'\substack{\unsure{\mathrm{bij}}\\[-.4ex]\unsure{\exists}}','A small bij-like group sits above a lower curled multiline mark; no separate exclamation is present. The lower mark may involve an underline and j-descender.','condition_c','low')
decision('M0625','undecided',r'\unsure{évt.}','The tall final stroke and adjacent small mark favor abbreviated évt., but remain compressed.','condition_d','low')
decision('M0626','undecided',r'\unsure{ou hyperbolique|cs hyperboliques}','The initial pair favors rounded ou; the word ending does not securely settle a final s.','condition_d','low')
decision('M0627','undecided',r'\unsure{g_p|g_s}','A closed p-like shape is entangled with the g-descender; the third inequality has a clearer open s.','inequalities','low')
decision('M0628','undecided',r'\unsure{g_p|g_s}','A second closed p-like outline overlaps the g-descender; p is first, with s retained.','inequalities','low')
decision('M0629','undecided',r'\unsure{$+$}','A cross-shaped terminal stroke may be a separate plus or a writing flourish.','somme_sign','low')
decision('M0630','alternative',r'\uline{sans}','The middle letters are an a oval and n rather than o and u; the underline is distinct.','operations_45','high')
decision('M0631','other',r'\inserted{ou de rigidification}','Separate small ou and de precede rigidification in the interline below marquage.','sommet_labels','medium')
decision('M0632','first',r'\mathcal T','The first boxed T has a looped cap and lower curl; all adjacent indices and the exponent were read with it.','boxed_diagram','high')
decision('M0633','first',r'\mathcal T','The second boxed T repeats the first glyph’s looped cap and lower curl.','boxed_diagram','high')
decision('M0634','undecided',r'\unsure{\nu|\omega}','The Ens argument has a curled low form, less clear than the two nu subscripts; nu and omega remain possible.','boxed_diagram','low')
decision('M0635','first',r'[\pm1]','The two-bar-plus-upright sign matches the two ± superscripts, followed by a single1 inside brackets.','boxed_diagram','medium')
decision('M0636','first',r'T_{g,\nu}S_\alpha','The initial T has a horizontal cap and a single hooked stem, unlike the looped calligraphic T forms. The following indices and letters are visible.','canceled_formulas','medium')
decision('M0637','undecided',r'\unsure{ou de recollement}','Ou de is clear; the following recol(l)-like strokes favor recollement but the ending is compressed.','bottom_circle','low')
decision('M0638','undecided',r'\unsure{importante}','The dotted i, m, descending p and tall t strokes support importante, but not every final stroke is secure.','new_structure','low')
decision('M0639','first',r'\mathcal T','The looped cap, curved stem and lower curl match the clear calligraphic T forms elsewhere on the page.','combinatorial_type','high')
decision('M0640','undecided',r'\unsure{avec $\omega^L$|avec inv}\qquad$\pm$','Two low curls, a detached dot and an upper L-like stroke favor omega^L; inv cannot be excluded. Plus-minus stands separately to the right.','notation_columns','low')
decision('M0641','first',r'\mathcal T','The standalone glyph has the looped top and curled bottom of the three calligraphic T letters below.','notation_columns','high')
decision('M0642','first','graphes b','The final b has a tall ascender and a distinct lower bowl.','large_diamond','high')

# Remaining report sections are appended below.
inventory = []
def item(element, kind, position, first_words, hand='his hand'):
    inventory.append(dict(element=element, kind=kind, position=position,
                          first_words_or_objects=first_words, sheet_kind='reused_typed',
                          hand=hand, transcribed='yes'))

item('printed listing header','text','top left','/*JOB=CRAY2;ACCT=*********,ALL=M06; // JOB; // EXEC; //CRAYIN','machine printing, no manuscript hand')
item('printed job identifier','text','top center','J0231CNU','machine printing, no manuscript hand')
item('dated open frame','drawing','upper center-left','Oct. 4 83; three-sided frame open above')
item('upper combinatorial diagram','diagram','upper left','R=RR/σ1, RR, A, vector A, vector A0, S, blackboard N')
item('condition a','text','right of upper diagram, first line','a) sigma squared=id, sigma ss p with raised t fixe')
item('condition b','text','right of upper diagram, second line','b) supp Compatible avec blackboard D infinity to {±1}')
item('condition c','display','right of upper diagram, third line','c) RR/D infinity hooked arrow A=vector A/{±1}, with lower annotations')
item('condition d opening','text','right of upper diagram, below c','d) (évt.) condition anabélienne (ou hyperbolique | cs hyperboliques)')
item('condition d canceled term','deletion','within d, before live inequality','doubtful 2g(s)')
item('condition d quantifier and inequality','display','lower part of d','∀s∈S, on a; 2g(s)+ν_s≥3')
item('three upper-right inequalities','margin note','upper right','3g_p-3+ν_s≥0; 2g_p-2+ν_s≥1; 2g_s+ν_s≥3, with local doubts')
item('operation 1','text','left center, above numbered list','1) Somme, doubtful plus')
item('operations 4 and 5','text','left center, first brace','4) amalgamation (sans gommage); 5) découpage (en gardant données de recollement)')
item('first operation brace','drawing','left of operations4 and5','one brace spanning both lines')
item('operations 2 and 3','text','left center, second brace','2) gommage de ... sommets de marquage.; 3) surmarquage')
item('canceled repères','deletion','inside operation2','doubtful repères')
item('second operation brace','drawing','left of operations2 and3','one brace spanning both lines')
item('parallel strokes between3 and6','drawing','below operation3','two plain shafts without heads')
item('operation6','text','left center, below separator','6) Bouchage des trous (gommage des cercles de raccord)')
item('operation7','text','below operation6','7) gommage de cercles de découpage')
item('short strokes under7','drawing','left margin to initial g of operation7','two short parallel lines')
item('inverses note','margin note','narrow column to right of operations','doubtful4,5 inverses l’un de l’autre (à condition que l’on ne découpe que par des cercles marqués)')
item('circle headings','text','center right, left of graph headings','Cercles de découpage; Cercles de raccord')
item('graph headings','text','upper right below inequalities','graphes pondérés; graphes bipondérés; graphes pondérés marqués')
item('graph-heading divider','drawing','left of graph headings','one vertical divider')
item('canceled marqués in graph headings','deletion','after middle graph heading','doubtful marqués, crossed and double-underlined')
item('vertex heading','text','right center','Sommets de marquage')
item('rigidification addition','insertion','interline below marquage','ou de rigidification')
item('vertex labels and brace','diagram','right of vertex heading','périphériques and intérieurs, joined by a brace')
item('marked-circle line','text','below vertex heading','Cercles marqués (non marqués)')
item('combinatorial-type phrase','text','right middle','type combinatoire d’un objet de ... SD calligraphic T_top')
item('canceled symbol in combinatorial-type phrase','deletion','before live SD calligraphic T_top','doubtful calligraphic T with possible following comma')
item('category heading','text','below combinatorial-type phrase','Catégorie des types combinatoires')
item('canceled upper symbol groups','deletion','right lower-middle, left of divider','calligraphic T S; calligraphic T D; calligraphic T SD')
item('canceled lower symbol group','deletion','below preceding symbol groups','doubtful calligraphic T star of Gamma')
item('symbol-column divider','drawing','between canceled groups and small phrase','long vertical stroke')
item('small notation phrase','text','right of canceled groups','doubtful avec omega^L | avec inv; separate ±')
item('standalone calligraphic T','display','below small notation phrase','calligraphic T')
item('three-row notation table','display','right lower column','S calligraphic T | ST; SD calligraphic T | SDT; D calligraphic T | DT')
item('large labeled diamond','diagram','lower right, left of small diamond','calligraphic T, S calligraphic T, D calligraphic T, SD calligraphic T with four graph labels')
item('small diamond','diagram','far lower right','doubtful t | blackboard L; lowercase s and d prefixes; four plain connectors')
item('relative-twist paragraph','text','lower left, above and around boxed diagram','Le ... twist ... tau_r ... à un cercle de découpage marqué, est défini en termes de4)5)')
item('canceled word after Le','deletion','opening of relative-twist paragraph','doubtful point | foncteur')
item('interlinear relatif','insertion','below canceled word in relative-twist paragraph','relatif, with underline versus deletion status unresolved')
item('canceled rational parameter','deletion','after first tau_r','(r∈blackboard Q)')
item('integer twist identity','display','beneath boxed diagram’s left portion','tau_r=id si r∈blackboard Z')
item('boxed two-arrow diagram','diagram','lower middle','S1 calligraphic T with g,nu and ±1 to calligraphic T to Ens(nu|omega) times [±1], with upper frame gaps')
item('canceled formulas below box','deletion','below boxed diagram','doubtful calligraphic T_g,nu^±, calligraphic T_top, and (TSR|TSD)_g,nu')
item('live formula below box','display','right of canceled formulas','colon and plain T_g,nu S_alpha')
item('final sloping paragraph','text','bottom left through bottom center','Mais l’iso de twist ... relatif à un cercle ... tau_r ... est une nouvelle structure importante')
item('canceled est un','deletion','near opening of final paragraph','doubtful est un')
item('recollement addition','insertion','below circle parenthesis in final paragraph','doubtful ou de recollement')
item('separate final underlines','drawing','beneath une nouvelle and beneath structure','first line starts near or within une; second line below structure')
item('folio40','margin note','bottom left','40','another unnamed hand')

unresolved = []
def doubt(place, reading, issue, alternatives, confidence='low'):
    unresolved.append(dict(place=place, reading=reading, issue=issue,
                           alternatives=alternatives, confidence=confidence))

doubt('printed EXEC token',r'\unsure{CSS3ATCH|CSSBATCH}','The left side of the B/3-shaped character is open; damaged printing could account for a missing B stem.',['CSS3ATCH','CSSBATCH'],'medium')
doubt('condition a sigma decoration',r'\unsure{\vec\sigma|\bar\sigma}^{2}','The mark above sigma is faint and discontinuous, unlike the clear vector arrows over A.',['vector sigma squared','bar sigma squared'])
doubt('condition c small annotation',r'\unsure{\mathrm{bij}}','The compact letters favor bij, but the final descender merges with lower strokes.',['bij','unresolved compact annotation'])
doubt('condition c lower annotation',r'\unsure{\exists}','The curled multiline mark may be a sign or the j-descender with an underline; no exclamation is visible.',['exists-like sign','descender and underline strokes'])
doubt('condition d abbreviated opening',r'\unsure{évt.}','The tall final stroke and following point are compressed.',['évt.','unresolved abbreviated form'])
doubt('condition d parenthetical words',r'\unsure{ou hyperbolique|cs hyperboliques}','The first short word and the final plural stroke are not fully secure.',['ou hyperbolique','cs hyperboliques'])
doubt('condition d canceled term',r'\deleted{\unsure{2g(s)}}','Cancellation crosses the internal signs and prevents full letter resolution.',['2g(s)','unresolved canceled formula'])
doubt('condition d punctuation',r'\unsure{:}','Two detached marks are not perfectly vertically aligned.',['colon','unresolved detached marks'])
doubt('first upper-right inequality',r'3\unsure{g_p|g_s}-3+\nu_s\ge0','The closed p-like subscript overlaps the g descender.',['g_p','g_s'])
doubt('second upper-right inequality',r'2\unsure{g_p|g_s}-2+\nu_s\ge\unsure{1}','The subscript is entangled with the descender, and the final1 has a loop or retouch.',['g_p versus g_s','1 versus unresolved retraced numeral'])
doubt('operation1 terminal sign',r'\unsure{$+$}','The cross-like terminal stroke may be a separate plus or a writing flourish.',['+','terminal stroke'])
doubt('operation2 canceled word',r'\deleted{\unsure{repères}}','The p descender survives, but the strike hides internal letters.',['repères','unresolved canceled word'])
doubt('vertical note top numerals',r'\unsure{4,5}','The compact numeral cluster is not completely separable.',['4,5','unresolved numeral cluster'])
doubt('middle graph compound ending',r'\unsure{bipondérés|bipondéré}','A small terminal curve favors plural s but is compressed.',['bipondérés','bipondéré'],'medium')
doubt('middle graph canceled word',r'\deleted{\uuline{\unsure{marqués|marqué}}}','The deletion crosses the final letters, while two underline strokes survive.',['marqués','marqué'],'medium')
doubt('relative-twist canceled word',r'\deleted{\unsure{point|foncteur}}','The p-like descender and short body favor point, but the deletion prevents every letter being read.',['point','foncteur'])
doubt('interlinear relatif status',r'\inserted{\unsure{\uline{relatif}|\deleted{relatif}}}','A dark stroke lies through or beneath the left part of this interlinear word.',['underlined insertion','canceled insertion'])
doubt('boxed Ens argument',r'\mathrm{Ens}(\unsure{\nu|\omega})','The argument is more curled than the clear nu subscripts.',['nu','omega'])
doubt('canceled formulas below box',canceled_f,'The deletion obscures the first two formulas and crosses the final R/D-shaped letter.',['calligraphic T_g,nu^±; calligraphic T_top; (TSR)_g,nu','same initial groups; (TSD)_g,nu'])
doubt('last paragraph canceled phrase',r'\deleted{\unsure{est un}}','The strike hides internal letters, though an e entry and tall t-like stroke survive.',['est un','unresolved canceled phrase'])
doubt('last paragraph insertion',r'\inserted{\unsure{ou de recollement}}','Ou de is clear; the ending after recol(l)-like strokes is compressed.',['ou de recollement','ou de followed by an unresolved word'])
doubt('last word of sloping paragraph',r'\unsure{importante}','The initial and medial strokes fit importante, but the ending is not fully secure.',['importante','unresolved ending of important-'])
doubt('canceled symbol before SDTtop',r'\deleted{\unsure{\mathcal T}}','The surviving cap and curled body are covered by deletion strokes.',['calligraphic T','unresolved canceled symbol'])
doubt('possible comma before SDTtop',r'\unsure{,}','The curved stroke may belong to the canceled glyph rather than separate punctuation.',['comma','part of canceled glyph'])
doubt('canceled star-Gamma expression',r'\deleted{\unsure{\mathcal T^*(\Gamma)}}','The superscript has several rays but is crossed; the argument’s upper and right strokes are also obscured.',['calligraphic T star of Gamma','unresolved superscript and argument'])
doubt('notation-column phrase',r'\unsure{avec $\omega^L$|avec inv}\qquad$\pm$','The dot, two curls and upper L-like stroke leave the form open.',['avec omega^L, separate ±','avec inv, separate ±'])
doubt('small diamond repeated glyph',r'\unsure{t|\mathbb L}','The tall doubled body has both a middle crossing and a lower foot. Neither alphabet is secure.',['t','blackboard L'])

notes = [
    dict(id='148-041-N01',type='date',place='top date',text='The manuscript date is read Oct. 4 83. Its surrounding frame has three sides and is open above. A pale mark after83 was initially considered by reader C, then excluded after root independently judged it a mottle lighter than the numeral strokes.'),
    dict(id='148-041-N02',type='source',place='printed header',text='The front-side industrial listing is part of the source and is transcribed in full. The literal EXEC token remains CSS3ATCH|CSSBATCH; no command-name normalization has been applied.'),
    dict(id='148-041-N03',type='claim',place='conditions and upper-right inequalities',text='The page writes conditions on sigma, supp and RR, then a stability inequality2g(s)+nu_s≥3. Three additional inequalities are written separately at the upper right. The first two g subscripts remain p|s uncertain; the transcription does not assert equivalence among the three inequalities.'),
    dict(id='148-041-N04',type='claim',place='vertical operations note',text='The note calls4,5 inverses of one another, under the condition that cutting is only along marked circles. This is a source claim; reader C did not verify it.'),
    dict(id='148-041-N05',type='claim',place='relative-twist paragraph',text='The paragraph says the relative twist is defined in terms of4) and5), with tau_r=id when r belongs to blackboard Z. The subscripts are read as r from their short shoulder strokes. Reader C did not prove the stated identity.'),
    dict(id='148-041-N06',type='claim',place='final sloping paragraph',text='The final sentence calls the twist associated with a marked cutting circle a new structure, with the last word tentatively importante. The clear word marqué before the parenthesis was omitted by both witnesses.'),
    dict(id='148-041-N07',type='reading',place='condition c',text='The lower arrow annotation is not resolved as a semantic exists sign: its strokes may involve a j-descender and an underline. The tentative sign remains marked in place, and no exclamation is supplied.'),
    dict(id='148-041-N08',type='reading',place='interlinear relatif',text='Relatif is an interlinear addition below the canceled word after Le. The dark stroke over its left portion remains uncertain between underline and deletion, so both local states are retained inside the insertion.'),
    dict(id='148-041-N09',type='reading',place='operation numbers',text='The current2 and5 are retraced. No separate earlier numeral can be read securely beneath them, so no invented canceled digit has been added.'),
    dict(id='148-041-N10',type='reading',place='two colons',text='Reader and root independently saw paired dark dots after the earlier pas) and before the live T_g,nu S_alpha. Both colons are retained at medium confidence.'),
    dict(id='148-041-N11',type='reading',place='small diamond',text='The repeated crossed doubled glyph remains t|blackboard L. Its prefixes s and d are lowercase. The four connectors are plain shafts, not arrows; nearby paper holes are excluded.'),
    dict(id='148-041-N12',type='reading',place='notation column',text='The small upper phrase favors avec omega^L over avec inv, but its disconnected curls and raised stroke remain open. Plus-minus stands separately to the right, rather than as a superscript attached to the prose.'),
    dict(id='148-041-N13',type='attribution',place='folio',text='The lower-left40 is retained as a margin number in another unnamed hand. It is not assigned to the author’s own pagination.'),
    dict(id='148-041-N14',type='coverage',place='whole page',text='All visible front-side wording, signs and drawing strokes were read from the whole page, two native halves and29 saved crops. The logical line count78 includes text lines, displayed formula rows, diagram rows, the date, printed identifier and folio. No OCR, research or TeX compilation was used, and reader C performed no mathematical computation or proof on this page.')
]

checks = []

hand_log = [
    dict(form=r'\mathcal T versus T',habit='Calligraphic T is drawn with a looped cap and a curled lower body; the live plain T beneath the box has a straight horizontal cap and one hooked stem.',pages=[41],holds_at_every_observed_occurrence=False,witness_effect='The clear calligraphic forms resolve several C doubts. H reads the live plain T beneath the box as calligraphic T. Canceled forms remain locally uncertain.'),
    dict(form='r versus rho',habit='The twist subscript r has a short upright and right shoulder, without a closed bowl and descending stem.',pages=[41],holds_at_every_observed_occurrence=True,witness_effect='H uses rho for the four parameter occurrences in the relative-twist paragraph; all four are read as r. The final paragraph also uses the same r form.'),
    dict(form='g with a lower subscript',habit='A g descender can enclose or overlap its subscript, producing a p-like closed outline even when another reading remains possible.',pages=[41],holds_at_every_observed_occurrence=False,witness_effect='The first two upper-right subscripts remain g_p|g_s; the third g_s is clearer. Neither witness is used to normalize the first two.'),
    dict(form='ss',habit='The abbreviation ss is written as two tightly compressed s loops.',pages=[41],holds_at_every_observed_occurrence=True,witness_effect='H expands the observed form to sans in condition a; the transcription preserves ss.'),
    dict(form='p with raised t',habit='The point abbreviation places a short t above the p baseline.',pages=[41],holds_at_every_observed_occurrence=True,witness_effect='Both witnesses flatten the raised t in condition a to pt.'),
    dict(form='small final s',habit='Plural s can be a short terminal curl separated only slightly from the preceding letter.',pages=[41],holds_at_every_observed_occurrence=False,witness_effect='Several graph headings have plural first readings against H’s singular forms. The middle compound and canceled marqués retain local uncertainty.'),
    dict(form='plain and doubled capitals',habit='Plain R and condition-c D have one left upright; the lower N and condition-b D show doubled uprights.',pages=[41],holds_at_every_observed_occurrence=True,witness_effect='C’s first blackboard R is changed to plain R, both witnesses’ condition-c blackboard D to plain D, and H’s plain N to blackboard N.'),
    dict(form='retraced operation digits',habit='The current2 and5 are written with dense retracing that does not reveal a separately readable earlier numeral.',pages=[41],holds_at_every_observed_occurrence=False,witness_effect='H describes underlying digits without naming them. The transcription retains the readable current numerals and does not invent canceled underforms.'),
    dict(form=r't|\mathbb L',habit='The small diamond repeats a tall doubled glyph with a middle crossing and lower foot, making t and blackboard L difficult to separate.',pages=[41],holds_at_every_observed_occurrence=True,witness_effect='C prints t and H prints blackboard L; the repeated form remains explicitly doubtful at all four vertices.')
]

notation = [
    dict(form='RR',use='Two plain R letters in the upper diagram and condition c.',pages=[41],caution='Do not replace the pair by one blackboard letter.'),
    dict(form=r'\vec A,\vec A_0',use='A symbols with clear right-pointing vector decorations in the upper diagram and quotient.',pages=[41],caution='The decoration above sigma squared is fainter and remains vector/bar uncertain.'),
    dict(form=r'\mathbb D_\infty versus D_\infty',use='The b-line D has a doubled upright; the c-line D has one upright.',pages=[41],caution='Keep the local alphabet difference even if a uniform notation might be expected.'),
    dict(form=r'\mathbb N',use='Target of the g arrow below S.',pages=[41],caution='The left stem is doubled.'),
    dict(form=r'\mathbb Q,\mathbb Z',use='Rational and integral parameter conditions in the relative-twist paragraph.',pages=[41],caution='The Q has an internal upright and the Z a doubled or retraced diagonal; retain these observed forms.'),
    dict(form=r'\tau_r',use='Twist notation in both lower paragraphs.',pages=[41],caution='Read the short r from ink; H’s rho is not retained.'),
    dict(form=r'\mathcal T versus T',use='The notation table explicitly contrasts calligraphic and plain T groups.',pages=[41],caution='The live T_g,nu S_alpha below the canceled formulas uses plain T.'),
    dict(form=r'[\pm1]',use='Final factor of the boxed diagram.',pages=[41],caution='Literal square brackets and plus-minus are preserved.'),
    dict(form=r'\mathcal T,S\mathcal T,D\mathcal T,SD\mathcal T',use='Four vertices of the large diamond.',pages=[41],caution='All four connectors are headless; labels remain beside their corresponding vertices.'),
    dict(form=r't|\mathbb L',use='Repeated glyph in the small diamond with lowercase s,d prefixes.',pages=[41],caution='No alphabet is settled from mathematical expectation.'),
    dict(form=r'\omega^L|\mathrm{inv}',use='Unresolved form after avec in the small notation column.',pages=[41],caution='The separate plus-minus is not attached as its superscript.')
]

abbreviations = [
    dict(form='ss',expansion='sans'),
    dict(form=r'p\textsuperscript{t}',expansion='point'),
    dict(form=r'\unsure{évt.}',expansion='éventuellement'),
    dict(form='supp',expansion='support'),
    dict(form='iso',expansion='isomorphisme'),
    dict(form='pond.',expansion='pondérés'),
    dict(form='graphes b',expansion='graphes bipondérés (proposed expansion of the final b)'),
    dict(form='Ens',expansion='ensembles'),
    dict(form='id',expansion='identité')
]

second_boxes = []
def second(id, kind, label, reading, box=None):
    b = BOXES[label] if box is None else box
    second_boxes.append(dict(box=id, kind=kind, x0=b[0], y0=b[1], x1=b[2], y1=b[3], reading=reading))

printed_reading = '\n'.join([
    r'\texttt{/*JOB=CRAY2;ACCT=*********,ALL=M06}',
    r'\texttt{// JOB MSGLEVEL=(0,0),MSGCLASS=Z}',
    r'\texttt{// EXEC \unsure{CSS3ATCH|CSSBATCH}}',
    r'\texttt{//CRAYIN DD *}'
])
second('041-SB01','C/H different words and open printed token','printed_header',printed_reading)
second('041-SB02','C/H omission','printed_job_id',r'\texttt{J0231CNU}')
second('041-SB03','handwritten date and frame on reused typescript','date',date_final)
upper_f = part(F,r'\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=large,row sep=large]',r'\end{tikzcd}}')
second('041-SB04','whole diagram with alphabet and arrow decisions','upper_diagram',upper_f)
second('041-SB05','handwritten formulas and words on reused typescript','conditions_ab',part(F,'a) $','c) $',False).strip())
second('041-SB06','whole formula with doubtful lower annotations','condition_c',part(F,'c) $','d) (',False).strip())
second('041-SB07','handwritten words and canceled formula','condition_d',part(F,'d) (',r'\margin{\[',False).strip())
second('041-SB08','whole doubtful formulas in margin','inequalities',part(F,r'\margin{\[','1) Somme',False).strip())
second('041-SB09','handwritten number and open sign','somme_sign',r'1) Somme \unsure{$+$}')
ops45 = part(F,r'\node[anchor=base east,inner sep=0pt] at (.25,0)',r'(.68,-1.15);')
second('041-SB10','handwritten operations and numbers','operations_45','\\begin{tikzpicture}[x=1cm,y=.65cm]\n'+ops45+'\n\\end{tikzpicture}')
ops23 = part(F,r'\node[anchor=base east,inner sep=0pt] at (.25,-2.2)',r'(.68,-3.35);')
second('041-SB11','handwritten operations and struck word','operations_23','\\begin{tikzpicture}[x=1cm,y=.65cm]\n'+ops23+'\n\\end{tikzpicture}')
ops67 = part(F,r'\draw (-.15,-3.86)',r'\draw (-.55,-6.31)--(1.04,-6.22);')
second('041-SB12','handwritten operations and partial line scopes','operations_67','\\begin{tikzpicture}[x=1cm,y=.65cm]\n'+ops67+'\n\\end{tikzpicture}')
second('041-SB13','margin note and handwritten numbers','vertical_note',part(F,r'\margin{\unsure{4,5}',r'\uline{marqués})}'))
second('041-SB14','handwritten circle headings','circle_headings',r'\uline{Cercles de découpage}'+'\n\n'+r'\uline{Cercles de raccord}')
second('041-SB15','handwritten heading, interlinear insertion and brace labels','sommet_labels',part(F,'Sommets de marquage',r'\end{array}\right.$'))
second('041-SB16','handwritten marked-circle line','marked_circles','Cercles marqués (non marqués)')
second('041-SB17','handwritten graph headings and canceled word','graph_headings',part(F,r'\margin{\begin{tabular}{|l}',r'\end{tabular}}'))
second('041-SB18','handwritten prose, canceled symbol and doubtful comma','combinatorial_type',part(F,r'\margin{type combinatoire',r'Catégorie des types combinatoires}'))
symbol_f = part(F,r'\figure{\begin{tikzpicture}[x=1cm,y=1cm]'+'\n\\node at (0,0)',r'\end{tikzpicture}}')
second('041-SB19','struck formulas and entire handwritten notation column','canceled_symbols',symbol_f,[2090,1385,2920,1995])
second('041-SB20','whole labeled diagram','large_diamond',large_f)
second('041-SB21','whole diagram with doubtful repeated glyph','small_diamond',small_f)
second('041-SB22','handwritten prose, insertion, deletions and parameters','relative_twist',part(F,'Le \\deleted{\\unsure{point|foncteur}}',r'\diagram{\begin{tikzpicture}',False).strip())
second('041-SB23','whole boxed formula with doubtful argument','boxed_diagram',box_f)
second('041-SB24','struck formulas and live formula with alphabet decision','canceled_formulas',part(F,canceled_f,'$T_{g,\\nu}S_\\alpha$'))
second('041-SB25','handwritten final opening and canceled words','iso_twist_open',part(F,"Mais l'",'un cercle (',False).strip())
second('041-SB26','handwritten parenthesis and interlinear addition','bottom_circle',part(F,'un cercle (de découpage ou de raccord',r'\inserted{\unsure{ou de recollement}}'))
second('041-SB27','whole final statement with omitted word and uncertain ending','new_structure',part(F,'$\\tau_r$ (pour un cercle de découpage marqué)',r'\uline{structure} \unsure{importante}'))
second('041-SB28','handwritten foliation','folio',r'\margin{40}')

macro_rows = {
    778:'H editorial description of the dated sheet',
    779:'upper diagram ampersand syntax',780:'upper diagram column spacing',781:'upper diagram row spacing',
    782:'sigma labels placed in H editorial note',787:'itemize syntax',789:'itemize syntax',790:'itemize syntax',
    791:'itemize syntax',792:'itemize syntax',795:'itemize syntax',799:'ge versus geqslant',800:'itemize syntax',
    801:'spacing in first inequality',803:'ge versus geqslant',804:'display and spacing syntax',
    806:'ge versus geqslant',807:'display separation',808:'ge versus geqslant',809:'H editorial layout note',
    810:'item label syntax',812:'item label syntax',815:'item label syntax',816:'item label syntax',
    817:'row spacing syntax',818:'item label syntax',820:'item label syntax',821:'item label syntax',
    822:'array and figure wrappers',824:'item label syntax',825:'item label syntax',826:'item label syntax',
    827:'itemize wrapper',828:'same brace grouping described in H note',833:'array wrapper',
    851:'tikz-cd options',854:'superscript and arrow serialization',855:'tikz-cd arrow serialization',
    856:'superscript and arrow serialization',858:'tikz-cd wrapper'
}
reading_rows = {
    777:'printed source, identifier and date',783:'upper diagram standalone sigma and horizontal hook',
    784:'upper diagram standalone sigma',785:'upper diagram A0-to-A hook',786:'upper diagram alphabets and arrow reading',
    788:'condition a ss',793:'condition c lower annotation without exclamation',794:'condition c small bij annotation',
    796:'condition d abbreviated opening',797:'condition d parenthetical alternative',798:'condition d cancellation and punctuation',
    802:'first margin inequality subscript',805:'second margin inequality subscript',811:'operation1 terminal plus',
    813:'operation4 sans',814:'operation4 singular gommage',819:'operation2 canceled repères',
    823:'parallel strokes between operations3 and6',829:'retraced current2 and5 without readable prior digits',
    830:'short strokes at7 and vertical numeral cluster',831:'vertical note l’un',832:'vertical note condition',
    834:'first graph heading plurals and separate underlines',835:'middle and lower graph headings, canceled word',
    836:'vertex labels and brace',837:'interlinear ou de rigidification',838:'rigidification insertion reading and placement',
    839:'right-hand prose, canceled symbols, notation column and diamonds',840:'large diamond annotation placement',
    841:'graph heading readings and large diamond labels',842:'canceled point and small diamond glyph',
    843:'interlinear relatif',844:'relative twist first r',845:'canceled rational parameter r',846:'relative twist à',
    847:'relative twist en termes',848:'relative twist identity parameter r',849:'relative twist integer parameter r',
    850:'relative twist terminal period',852:'boxed S subscript1',853:'boxed first calligraphic T',
    857:'boxed final factor [±1]',859:'canceled formulas beneath box',860:'canceled TSR versus TSD',
    861:'colon before live formula',862:'live plain T formula and boxed S1',863:'last paragraph iso',
    864:'last paragraph canceled est un',865:'last paragraph relatif à',866:'last paragraph de raccord',
    867:'last paragraph marqué ou pas and parenthesis scope',868:'interlinear ou de recollement',
    869:'final marked-circle phrase, une nouvelle structure and importante',870:'canceled symbol in combinatorial-type phrase',
    871:'right-hand symbols, diagrams and omitted foliation'
}
with (PACKET/'differences.tsv').open(newline='') as stream:
    source_diffs=list(csv.DictReader(stream,delimiter='\t',quoting=csv.QUOTE_NONE))
differences_review=[]
for row in source_diffs:
    n=int(row['source_row'])
    assert (n in macro_rows) != (n in reading_rows), n
    differences_review.append(dict(source_row=n,
        classification='macro-only' if n in macro_rows else 'reading decision',
        place=(macro_rows if n in macro_rows else reading_rows)[n]))

assert len(decisions)==24 and len({x['id'] for x in decisions})==24
assert {x['id'] for x in decisions}=={f'M{n:04d}' for n in range(619,643)}
assert len(differences_review)==95
assert {x['source_row'] for x in differences_review}==set(range(777,872))
assert len({x['box'] for x in second_boxes})==len(second_boxes)
assert all(0<=x['x0']<x['x1']<=3007 and 0<=x['y0']<x['y1']<=2228 for x in second_boxes)
assert all((OUT.parent.parent/x['crop']).exists() for x in changes+decisions)

result=dict(scan=41,reader='C',lines_read=78,changes=changes,decisions=decisions,
            inventory=inventory,unresolved=unresolved,notes=notes,checks=checks,
            hand_log=hand_log,notation=notation,abbreviations=abbreviations,
            second_boxes=second_boxes,differences_review=differences_review)
prose_fields={'ink','issue','habit','witness_effect','use','caution','text','position','first_words_or_objects'}
def space_prose(value):
    if isinstance(value,list):
        for entry in value:
            space_prose(entry)
    elif isinstance(value,dict):
        for key,entry in value.items():
            if key in prose_fields and isinstance(entry,str):
                value[key]=re.sub(r'(?<=[A-Za-zÀ-ÿ])(?=\d)',' ',entry)
            elif isinstance(entry,(list,dict)):
                space_prose(entry)
space_prose(result)
(OUT/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({key:len(result[key]) for key in ['changes','decisions','inventory','unresolved','notes','checks','hand_log','notation','abbreviations','second_boxes','differences_review']}))
