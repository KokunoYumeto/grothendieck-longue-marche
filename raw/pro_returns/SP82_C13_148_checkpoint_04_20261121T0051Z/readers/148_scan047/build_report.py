from pathlib import Path
import csv
import json
import re

ROOT = Path('/workspace/scratch/8132fe1cca43')
PACKET = ROOT / 'work/packets/148_scan047'
OUT = ROOT / 'work/SP82_C13_148/readers/148_scan047'
C = (PACKET / 'C.tex').read_text()
H = (PACKET / 'H.tex').read_text()
F = (OUT / 'candidate.tex').read_text()
manifest = json.loads((OUT / 'crop_manifest.json').read_text())
crops = {x['label']: x for x in manifest['crops']}

def macro(text, name, start=0):
    pos = text.index(name + '{', start)
    at = pos + len(name)
    depth = 0
    for i in range(at, len(text)):
        if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
            depth += 1
        elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
            depth -= 1
            if not depth:
                return text[pos:i+1]
    raise ValueError((name, pos))

graph = macro(F, r'\figure')
cgraph = macro(C, r'\figure')
hgraph = macro(H, r'\drawing')
circled = macro(F, r'\margin', F.index(r'\margin{\begin{tikzpicture}'))
central = F[F.index(r'\deleted{Ou encore'):F.index('\n\n\\margin{\\diagram')]
margin_s = macro(F, r'\diagram', F.index(r'\margin{\diagram'))
split_diagram = macro(F, r'\diagram', F.index(r'\widetilde A=\vec A/\sigma'))
order_diagram = macro(F, r'\diagram', F.index("Ordre d'un sommet"))
main_drawing = graph[:graph.index('\\fill (132,424)')] + '\\end{tikzpicture}}'
lower_drawing = '\\figure{\\begin{tikzpicture}[x=.013cm,y=-.013cm,line width=.55pt]\n' + graph[graph.index('\\fill (132,424)'):]

changes = []
def ev(place, c, h, final, ink, label, confidence='high', kind='misread word', against_c=False, against_h=True, math=False, **extra):
    if c is not None and c not in C:
        raise ValueError('C snippet not literal: ' + place + '\n' + c)
    if h is not None and h not in H:
        raise ValueError('H snippet not literal: ' + place + '\n' + h)
    cp = crops[label]
    row = dict(id=f'B047-C{len(changes)+1:02d}', place=place, c=c, h=h,
               final=final, ink=ink, crop=cp['path'], box=cp['box'],
               confidence=confidence, kind=kind, against_c=against_c,
               against_h=against_h, math=math)
    row.update(extra)
    changes.append(row)

ev('Header: tentative cancelled initials', r'\deleted{\mathrm{MD}}', r'\struck{\ill{}}',
   r'\deleted{\unsure{\mathrm{MD}}}',
   'Two capital-sized forms survive the diagonal hatching: angular left strokes and a right closed bowl support MD, but the left form is entangled with the strike.',
   'header', 'medium', r'readable ink left as \ill{}')
ev('Header: Grbip punctuation', r'\mathrm{Grbip}', '(Gr.bip)', r'\mathrm{Grbip}',
   'G-r-b-i-p run continuously; there is no interior dot after Gr and no pair of parentheses around this first name. The separate full stop belongs after the cancelled initials.', 'header', kind='text not on the page')
ev('Header: Grabipond', r'\unsure{\mathrm{Grabipond}}', '(Gra.bipond)', r'\mathrm{Grabipond}',
   'Open G, small r-a, tall b, dotted i, descending p, rounded o, low n and final tall d are visible. No dot separates Gra from bipond.',
   'header', against_c=True, certainty_resolution=True)
ev('Objects: plural structures', '$+$ structures suppl.', '+ structure suppl.', '$+$ structures suppl.',
   'The inserted word ends with a separate low s after structure; the plus is a crossing of two strokes.', 'objects')
ev('Objects: attachment of the supplementary-structures insertion', r'\inserted{$+$ structures suppl.}', r'\add{+ structure suppl.}',
   r'\inserted{$+$ structures suppl.}',
   'The curved placement line lies below the inserted phrase and joins the object/tuple area; the words are not an extension of the preceding groupoid name.',
   'objects', kind='insertion or placement')
ev('Objects: punctuation after the supplementary-structures insertion', r'\inserted{$+$ structures suppl.},', r'\add{+ structure suppl.}',
   r'\inserted{$+$ structures suppl.}',
   'The terminal point of suppl. is present; the farther curved stroke continues the placement leader rather than making an independent comma.',
   'objects', 'medium', 'text not on the page', True, False)
ev('Objects heading: underline absent', 'Objets :', r'\emph{Objets} :', 'Objets :',
   'Capital O and the following b-j-e-t-s are on one baseline with a colon; there is no line beneath the word.', 'objects', kind='text not on the page')
ev('Object description: pouvant avoir', 'pouvant avoir', 'permettant\naussi', 'pouvant avoir',
   'The first word has p-o-u-v-a-n-t, with a low rounded o/u sequence and a v angle, and the second begins a-v; neither the extra letters of permettant nor an initial aussi sequence is present.', 'objects')
ev('Object description: a fortiori', 'a fortiori', '+ plusieurs', 'a fortiori',
   'A separate unaccented a precedes the tall f and the o-r-t-i-o-r-i run; this is written text, not a plus sign.', 'objects')
ev('Free edges: underline scope', r'\uline{arêtes libres}', r'\emph{arêtes libres}', r'\uline{arêtes} libres',
   'The horizontal underline ends after arêtes, before the l of libres. The second word is not underlined.',
   'free_edges', kind='insertion or placement', against_c=True)
ev('Inserted alternative name: arcs', r'\unsure{trous|arcs}', '« arcs »', 'arcs',
   'The four forms are a rounded a, small r, open c and final s; no tall t or separate o-u sequence is present.',
   'free_edges', against_c=True, against_h=False, certainty_resolution=True)
ev('Inserted alternative names: position', r'\inserted{(``sommets\'\', ``\unsure{trous|arcs}\'\')}'.replace("\\'", "'"),
   '(« sommets », « arcs »)', r'\inserted{(``sommets\'\', ``arcs\'\')}'.replace("\\'", "'"),
   'The parenthetical phrase is inserted at arêtes libres with its own curved placement stroke, before correspondant; it is not appended after the closing sigma parenthesis.',
   'free_edges', kind='insertion or placement')
ev('After the sigma parenthesis: no colon', 'de $\sigma$)\n$S,', 'de $\sigma$) (« sommets », « arcs ») : $S$',
   'de $\sigma$)\n$S,', 'The closing parenthesis is followed by the next set-definition baseline, with no two-dot colon in the intervening space.',
   'free_edges', kind='text not on the page')
ev('Set definition: raised vector A', r'$S,\vec A$ ens.', r'$S$, $\vec{A}$ ens.', r'$S,\inserted{\vec A}$ ens.',
   'Vector A is written above the baseline between S and ens.; a curved cue descends to that gap. The word ens. itself stays on the baseline.',
   'set_definition', kind='insertion or placement', against_c=True, math=True)
ev('Genus-map label: gamma', r'\inserted{\unsure{\gamma}}', r'\gamma', r'\inserted{\gamma}',
   'The live letter has a low descending loop and a rising right arm, visibly distinct from the crossed g-like trace to its left.',
   'genus_map', kind='misread symbol or index', against_c=True, against_h=False, math=True, certainty_resolution=True)
ev('Genus map: tentative earlier label', r'\deleted{\unsure{g}}', None, r'\deleted{\unsure{g}}',
   'The older crossed label has a small closed upper body and a descending stroke, compatible with g; crossing strokes still prevent a secure letter reading.',
   'genus_map', 'medium', 'omission', math=True)
ev('Genus-map codomain alphabet', r'\mathbb N', r'\mathbf{N}', r'\mathbb N',
   'The N has two separate left ascending strokes enclosing a narrow white channel; it is not merely a heavy single-stem letter.',
   'genus_map', kind='misread symbol or index', math=True)
ev('Rigidity-map cancelled domain: vector and deletion state', r'\deleted{\unsure{\widetilde A}}', r'\vec{A}^{\sigma} = A_{\ell}',
   r'\deleted{\unsure{\vec A^{\sigma}|\vec A}}=A_\ell',
   'A horizontal shaft with a right arrowhead is visible above the cancelled triangular A. The possible raised sigma is entangled in the hatching. The domain is crossed out; H explicitly supplies its unstruck exponent editorially.',
   'rigidity_map', 'medium', 'misread symbol or index', True, True, True)
ev('Rigidity-map live domain: A ell', r'=\unsure{A_\ell}', r'= A_{\ell}', r'=A_\ell',
   'The live A has two legs and a crossbar, and the lowered right form has a loop and long foot characteristic of ell. The retouch at the A apex is not a separate exponent.',
   'rigidity_map', kind='misread symbol or index', against_c=True, against_h=False, math=True, certainty_resolution=True)
ev('Rigidity-map label: live 2 after the crossed form', r'r\deleted{\unsure{\rho_2}}', r'\xrightarrow{\ r\ }',
   r'r\,\deleted{\unsure{\rho}}\,2',
   'The rho-like loop and descending stroke are crossed. The clear curved top, diagonal and lower foot of 2 lie to its right beyond the main cancellation; the digit is near the new r baseline, so it is retained there rather than silently made a cancelled subscript.',
   'rigidity_map', 'medium', 'deletion state', True, True, True)
ev('Rigidity-map codomain alphabet', r'\mathbb N', r'\mathbf{N}', r'\mathbb N',
   'Two left ascending strokes of N enclose a long narrow white channel; the diagonal then joins its right stem.',
   'rigidity_map', kind='misread symbol or index', math=True)
ev('Rigidity caption: two cancelled traces', r'\deleted{\unsure{rigidification}}', r'\struck{\ill{}}',
   r'\deleted{\unsure{rigi}} \deleted{\unsure{rigidification}}',
   'A short upper run has r/g-like bodies and two separate dot or stem remnants; a separate much longer lower word is struck by a horizontal line and retains long f/g-like descenders. They cannot be collapsed into one certainly legible word.',
   'rigidity_caption', 'low', 'omission', True, True)
ev('Crossed gloss: duplicated A ell removed', r'\deleted{$\unsure{A_\ell}\quad\text{``\unsure{arêtes libres}\'\'}$}'.replace("\\'", "'"),
   None, r'\deleted{``\unsure{arêtes libres}\'\'}'.replace("\\'", "'"),
   'The upper crossed run is the arêtes-libres gloss below the map domain. No independently written second A ell precedes it; the next A-like term begins the lower relation.',
   'free_definition', 'medium', 'text not on the page', True, False, True)
ev('Lower relation: cancellation scope', r'$\underset{\mathrm{def}}{\unsure{A_\ell}\subset\vec A/\sigma}$',
   r'\struck{\ldots\,\vec{A}/\sigma}',
   r'\deleted{$\unsure{A_\ell}\overset{\mathrm{def}}{\subset}\vec A/\sigma$}',
   'A long horizontal cancellation passes through the whole lower relation and continues through the following quoted phrase. The left A-like term remains crossed and uncertain.',
   'free_definition', kind='deletion state', against_c=True, against_h=False, math=True)
ev('Lower relation: position of def', r'\underset{\mathrm{def}}{\unsure{A_\ell}\subset\vec A/\sigma}',
   r'\overset{\mathrm{def}}{=}', r'\unsure{A_\ell}\overset{\mathrm{def}}{\subset}\vec A/\sigma',
   'The small d-e-f is between the two lines, at about native (900,938), above the lower inclusion and to the right of the upper equality. Its position does not support an underset beneath the whole formula or an upper equality label.',
   'free_definition', 'medium', 'insertion or placement', True, True, True)
ev('Crossed quotation: ens. is abbreviated', r'\unsure{ensemble des sommets supplémentaires}', '« ens.\ des sommets\nsupplémentaires »',
   r'ens. des \unsure{sommets supplémentaires}',
   'The first word is a short e-n-s run followed by a point; there is no room or stroke sequence for the remainder of ensemble. The subsequent crossed words remain qualified.',
   'free_definition', kind='abbreviation expanded or spelling modernised', against_c=True, against_h=False)
ev('Slanted note: punctuation after précis and donnée', 'pas assez précis comme donnée.', 'pas assez précis, comme donnée :',
   'pas assez précis comme donnée.',
   'There is no independent comma after précis. A single small terminal point follows donnée; no second point makes a colon.', 'slant_margin', 'medium', 'text not on the page')
ev('Slanted note: first T a', r'\unsure{T_a}', r'T_a', r'T_a',
   'The first symbol has a full transverse T bar and one long upright; a distinct small rounded a sits below and to its right.',
   'slant_margin', kind='misread symbol or index', against_c=True, against_h=False, math=True, certainty_resolution=True)
ev('Slanted note: second T and uncertain subscript', r'\omega(\unsure{T_a})\simeq\omega(a)', r'\omega(T_a) \simeq \omega(a)',
   r'\omega(\unsure{T|T_a})\simeq\omega(a)',
   'Inside the left omega parentheses the capital has a T-like bar and upright. The dark lower-right stroke does not securely separate into the little a visible on the preceding T a; both local readings are retained.',
   'slant_margin', 'medium', 'misread symbol or index', True, True, True)
ev('Slanted note: no final period', r'\omega(a)$.}', r'\omega(a)$}', r'\omega(a)$}',
   'The formula ends at its right parenthesis; no equally dark separate punctuation point follows it.',
   'slant_margin', kind='text not on the page', against_c=True, against_h=False)
ev('Encircled note: capital J', "J'ai indiqué", "j'ai indiqué", "J'ai indiqué",
   'The initial letter is a full-height downstroke ending in a broad left hook, larger than the following letters.', 'circled_margin')
ev('Encircled note: written line-end hyphen', 'une pondération des sommets', 'une pondération des sommets',
   'une pondé-\\\\ration des sommets',
   'The first line ends pondé followed by a separate short hyphen; ration begins the next line. The written break is retained in the text node.',
   'circled_margin', kind='abbreviation expanded or spelling modernised', against_c=True)
ev('Encircled note: enclosing curve', r'\margin{J\'ai indiqué une pondération des sommets, mais pas des arêtes}'.replace("\\'", "'"),
   r'\note{note encerclée, marge gauche}', circled,
   'A continuous curve starts above the right of the note, rounds its right end and runs below the three lines before bending down at the lower left; it is reproduced as an open enclosing curve.',
   'circled_margin', kind='drawing or diagram', against_c=True, against_h=False)
ev('Main weighted graph: white centers and faint free arm', cgraph, hgraph, main_drawing,
   'Seven connected marked vertices carry 0,2,0,4,13,1,3. Three edges join the left 0 to 2 and two join 13 to 4. The endpoint 1 has a white center, and central 2 has a small off-center light hole. The second upward arm at the left 0 contains a pale segment and gaps; C fills every point solid and draws the arm uniformly.',
   'main_graph', kind='drawing or diagram', against_c=True, against_h=False, math=True)
ev('Main weighted graph: isolated vertex labelled 2', r'\fill (.7,-1.25) circle(2pt); \node[left] at (.7,-1.25) {$2$};',
   'sous « 2° »', r'\fill (130,303) circle[radius=4.5];\node[below left] at (126,305) {$2$};',
   'The round mark above and to the right of 2 is a substantial filled point, matching the graph vertices, not a small hollow degree sign. It has no attached edge.',
   'main_graph', kind='misread symbol or index', math=True)
ev('Lower graph components: fine third arm and pale loop vertex',
   r'\fill (.7,-2.8) circle(2pt); \node[left] at (.7,-2.8) {$0$};' + C.split(r'\fill (.7,-2.8) circle(2pt); \node[left] at (.7,-2.8) {$0$};',1)[1].split(r'\end{tikzpicture}',1)[0],
   hgraph, lower_drawing,
   'The 0 vertex has three arms: a near-vertical one, a thin diagonal one with pale breaks and a curved right arm. The 3 vertex has a rightward oval loop and a pale narrow center in its dark point. H’s later note correctly restores the third arm; C lacks the pale/gapped detail and fills the lower point solid.',
   'lower_graphs', kind='drawing or diagram', against_c=True, against_h=False, math=True)
ev('Cancelled proposal: Ou encore', 'Ou encore', r'\ill{} encore', 'Ou encore',
   'The initial O has an open rounded body and the attached low u survives beside the oblique strike; encore follows with its e-n-c-o-r-e sequence.',
   'cancelled_main', kind=r'readable ink left as \ill{}')
ev('Cancelled proposal: posons', 'posons', 'posant', 'posons',
   'After the descending p, the remaining low run has rounded o forms and a final s-like exit; there is no final tall t.',
   'cancelled_main', 'medium')
ev('Cancelled proposal: parenthesis and abbreviated identif.', 'identif.', 'identifié', '(identif.',
   'A separate opening curved parenthesis precedes the i; the word ends with the long f stroke and a point, rather than the letters of identifié.',
   'cancelled_main', kind='abbreviation expanded or spelling modernised', against_c=True)
ev('Cancelled proposal: underline beneath tous', 'de tous les', None, r'de \uline{tous} les',
   'A short horizontal line is drawn directly beneath tous and ends before les.',
   'cancelled_main', kind='insertion or placement', against_c=True)
ev('Cancelled proposal: upper interlinear word and leader', None, None, r'\inserted{\unsure{apparents|marqués}}',
   'An additional word lies below the S-tilde equation and above sommets, with a curved leader into the following phrase. Two early downward strokes and a terminal short rise support apparents, but crossing strokes also permit a marqués-like reading; it is distinct from the separately crossed baseline token.',
   'cancelled_main', 'low', 'omission', True, True)
ev('Cancelled proposal: lower quoted marqués without non', r'``\uline{marqués}\'\''.replace("\\'", "'"),
   '« non marqués »', r'``\uline{marqués}\'\''.replace("\\'", "'"),
   'The underlined lower run starts with the m of marqués and occupies the same compact seven-letter width as the nearby form. No separate preceding n-o-n run is visible.',
   'cancelled_main', kind='text not on the page')
ev('Cancelled proposal: closing parenthesis after graphe', 'du graphe,', 'du\ngraphe)', 'du graphe),',
   'A tall closing curve follows the final e of graphe before the comma and l’on donne.',
   'cancelled_main', kind='omission', against_c=True, against_h=False)
ev('Cancelled proposal: l’on donne', "l'on donne", r'\ldots\ on donne', "l'on donne",
   'A distinct tall initial stroke and small detached apostrophe precede the low o-n of on; donne follows.', 'cancelled_main', 'medium', 'omission')
ev('Cancelled proposal: codomain alphabet', r'\mathbb N', r'\mathbf{N}', r'\mathbb N',
   'The diagram’s N has a doubled ascending left stem, separated by a white channel, below the cancelling diagonals.',
   'cancelled_main', kind='misread symbol or index', math=True)
ev('Pondération caption: live rather than cancelled', r'(\uline{pondération} du graphe)}', r'(\emph{pondération} du graphe)',
   r'(\uline{pondération} du graphe)',
   'The caption is to the right of the large enclosing curve and below the crossed prose; no cancellation stroke crosses its letters. Only pondération has its own short underline.',
   'cancelled_main', kind='deletion state', against_c=True, against_h=False)
ev('Marginal S-tilde correction: lower insertion and crossed word',
   r'\widetilde S=S\amalg\deleted{\unsure{S_\ell}}\inserted{A_\ell}' + '\n' + r'\qquad\deleted{\unsure{\mathrm{apparents}}}',
   r'\widetilde{S} &= S \sqcup A_{\ell},', margin_s,
   'The old term is heavily crossed, with a surviving lowered ell; A ell is written on a separate lower line and linked upward by a curved cue. A separate long crossed word to the right retains two p-like descenders and final t/s-like strokes, compatible with apparents. The candidate preserves both uncertainties and the physical insertion.',
   'margin_S', 'medium', 'insertion or placement', True, True, True)
ev('Marginal quotient identity: no terminal period', r'\widetilde A=\vec A/\sigma=A\amalg A_\ell.',
   r'\widetilde{A} &= \vec{A}/\sigma = A \sqcup A_{\ell},', r'\widetilde A=\vec A/\sigma=A\amalg A_\ell',
   'The last ell ends in its hooked foot; the space following it has no independent punctuation dot. H’s alignment comma is also not an ink mark.',
   'margin_A', kind='text not on the page', against_c=True, math=True)
ev('Decomposition diagram: brackets and crossed old shafts',
   r'\underbrace{\vec A_\ell}_{\vec A^\sigma}',
   r"\note{la flèche verticale de gauche est doublée d'un faisceau de traits" + '\n' + '(une flèche hachurée)}',
   split_diagram,
   'The lower bracket under vector A ell is squared, whereas the other grouping is curved. To the left of the live long downward arrow are old crossed shafts with triangular/looped turns; no independent letter can be certified among them. These strokes are drawn literally.',
   'margin_split', kind='drawing or diagram', against_c=True, against_h=False, math=True)
ev('Decomposition formulas: no extra standalone align block', None,
   r'\vec{A} &= \vec{A}_0 \sqcup \vec{A}_{\ell},' + '\n' + r'  \qquad \vec{A}_0 = \vec{A} \setminus \vec{A}^{\sigma},' + '\n' + r'  \quad \vec{A}_{\ell} = \vec{A}^{\sigma},',
   split_diagram,
   'The top equation and its two explanatory formulas occur once in the diagram: the latter are beneath grouping brackets, not separate equations with written equals signs. H repeats and expands this material in a preceding align block.',
   'margin_split', kind='text not on the page', math=True)
ev('Order formula: square bracket and unexpanded correspond',
   r"\underbrace{\sigma_\ell(s)}_{\substack{\text{correspond aux ``trous''}\\" + '\n' + r'\text{ou cercles de recollage}}}',
   r'$\sigma_{\ell}$ correspondant aux « trous » ou cercles de recollage.',
   order_diagram,
   'The grouping under sigma ell(s) has a straight horizontal base and short upturned ends. Beneath it the first line ends with a tall d in correspond, followed on separate lines by aux “trous”, ou cercles, de recollage; no -ant or final period is written.',
   'margin_order', kind='drawing or diagram', against_c=True, math=True)
ev('Order formula: no terminal comma', r'+\sigma_0(s)', r'+ \sigma_0(s),', r'+\sigma_0(s)',
   'The final closing parenthesis is followed by empty space, with no separate comma.',
   'margin_order', kind='text not on the page', math=True)
ev('Underlying graph: singular du graphe', r'du \uline{graphe}', r'des \emph{graphes}', r'du \uline{graphe}',
   'The preposition has d followed by one u form; graphe ends with a low e and no extra terminal s.', 'underlying_text')
ev('Underlying graph: singular sous-jacent', 'sous-jacent', 'sous-jacents', 'sous-jacent',
   'The t has a tall finishing stroke and crossbar; no additional low s follows it before à.', 'underlying_text')
ev('Underlying graph: singular corresponding ordinary graph', "d'un graphe\n``ordinaire'' correspondant", 'des graphes « ordinaires » correspondants',
   "d'un graphe\n``ordinaire'' correspondant",
   'The article is a compact d’un. Graphe and ordinaire end without s, and correspondant has its final tall t followed by the opening parenthesis, not a plural s.', 'underlying_text')
ev('Underlying graph: comma after libres', 'sans arêtes libres i.e.', 'sans arêtes\nlibres, i.e.', 'sans arêtes libres, i.e.',
   'A short descending stroke directly after libres at the far right is of the same dark ink and sits just below the word’s baseline, supporting a comma.',
   'underlying_text', 'medium', 'omission', True, False)
ev('Underlying graph: ss abbreviation', 'opère\nss pts fixes', 'opère sans pts fixes', 'opère ss pts fixes',
   'Two short s-like forms stand between opère and pts; no a-n middle sequence spells out sans.',
   'underlying_text', kind='abbreviation expanded or spelling modernised')
ev('Free-edge parenthesis: small crossed trace and underline extent', r'(\uline{arêtes} libres)', r'(arêtes \struck{\ill{}} libres)',
   r'(\uline{arêtes \deleted{\illegible{1}}} libres)',
   'Between arêtes and libres are three short dark horizontal bars and connecting overtrace. No word can be recovered. The underline runs beneath arêtes through this small cancelled area and stops before libres.',
   'free_attachment', 'medium', 'omission', True, False)
ev('Cancelled sommets-trous: punctuation', r'\deleted{ou ``sommets-trous\'\')}'.replace("\\'", "'"),
   r'\struck{ou « sommets-trous »}', r'\deleted{ou ``sommets-trous)}',
   'Two opening quotation ticks precede sommets. The cancellation obscures the ending, with no separately secure closing quotation pair; a large closing parenthesis is nevertheless visible and is itself crossed.',
   'free_attachment', 'medium', 'text not on the page', True, True)
ev('Attachment map: no terminal period', r'A_\ell\arrow[r]\&S', r'A_{\ell} \longrightarrow S .',
   r'A_\ell\arrow[r]\&S',
   'The S is followed by no dark baseline punctuation; the much paler isolated spot below it is not a terminal stop. The arrow has one shaft and a full rightward head.',
   'attachment_map', kind='text not on the page', math=True)
ev('Final heading: no colon', r'\uline{Flèches} Les', r'\emph{Flèches} : Les', r'\uline{Flèches} Les',
   'The underlined heading ends with s; a clear blank gap separates it from capital Les, with no pair of dots.', 'arrows_end', kind='text not on the page')
ev('Final sentence: no terminal stop', 'de telles structures', 'de telles structures.', 'de telles structures',
   'The last s is the final dark mark in the line. There is no following period.', 'arrows_end', kind='text not on the page')
ev('Bottom foliation: 46', r'\mspage{46}', None, r'\margin{46}',
   'The separate thin hand writes a tall 4 with a cross stroke and a long descending stem, followed by an open-topped 6 with a rounded lower loop. Attribution of this number to the author is not established.',
   'foliation', kind='omission')

