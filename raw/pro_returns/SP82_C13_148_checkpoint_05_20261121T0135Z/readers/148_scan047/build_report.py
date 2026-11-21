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

decisions = []
def decide(id, decision, reading, ink, label, confidence):
    cp=crops[label]
    decisions.append(dict(id=id, decision=decision, reading=reading, ink=ink,
                          crop=cp['path'], box=cp['box'], confidence=confidence))

decide('M0689','first',r'\mathrm{Grabipond}',
       'G-r-a-b-i-p-o-n-d are individually distinguishable; no internal punctuation interrupts them.', 'header','high')
decide('M0690','alternative','arcs',
       'The short run has rounded a, small r, open c and final s, without a t ascender or o-u sequence.', 'free_edges','high')
decide('M0691','first',r'\gamma',
       'The live letter has a low descending loop and an ascending right arm beside the crossed former label.', 'genus_map','high')
decide('M0692','first',r'A_\ell',
       'The live triangular A and lowered looped ell with hooked foot are visible despite local retouch at the apex.', 'rigidity_map','high')
decide('M0693','undecided',r'\unsure{A_\ell}',
       'The lower relation is crossed by horizontal and oblique strokes. An A-like body and lowered loop support A ell, but the cancellation prevents certifying all original strokes.', 'free_definition','medium')
decide('M0694','first',r'T_a',
       'The capital has a long T crossbar and upright, with a distinct small rounded a below to the right.', 'slant_margin','high')
decide('M0695','undecided',r'\unsure{T|T_a}',
       'A T-like bar and upright survive inside omega parentheses; its lower-right dark stroke is not securely a separate subscript a.', 'slant_margin','medium')

inventory=[]
def inv(element,kind,position,first,hand='primary manuscript hand'):
    inventory.append(dict(element=element,kind=kind,position=position,
                          first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))

for row in [
('I047-01','margin note','top center','3)'),
('I047-02','text','top line','qui forment un groupoïde'),
('I047-03','deletion','header, before Grbip',r'\unsure{\mathrm{MD}}'),
('I047-04','text','upper body','Objets : graphes'),
('I047-05','insertion','above graphes/tuple','finis'),
('I047-06','insertion','above the object parenthesis','$+$ structures suppl.'),
('I047-07','text','upper object-description lines','(pouvant avoir des sommets isolés'),
('I047-08','insertion','at arêtes libres','(``sommets\'\', ``arcs\'\')'.replace("\\'","'")),
('I047-09','text','upper set-definition lines',r'S, ens. finis; \sigma; o; On se donne de plus'),
('I047-10','insertion','above S, ens.',r'\vec A'),
('I047-11','diagram','first displayed map',r'S\longrightarrow\mathbb N'),
('I047-12','deletion','above first map shaft',r'\unsure{g}'),
('I047-13','insertion','beside crossed first-map label',r'\gamma'),
('I047-14','text','right of first map','(application ``genre\'\' ou ``poids\'\')'.replace("\\'","'")),
('I047-15','diagram','second displayed map',r'\deleted{\unsure{\vec A^\sigma|\vec A}}=A_\ell\longrightarrow\mathbb N'),
('I047-16','deletion','left of second-map domain',r'\unsure{\vec A^\sigma|\vec A}'),
('I047-17','deletion','second-map label between r and live 2',r'\unsure{\rho}'),
('I047-18','text','second-map label, right of cancelled form','2'),
('I047-19','text','right of second map','(application ``indice de rigidification\'\')'.replace("\\'","'")),
('I047-20','deletion','upper short caption fragment',r'\unsure{rigi}'),
('I047-21','deletion','longer lower caption fragment',r'\unsure{rigidification}'),
('I047-22','deletion','beneath second-map domain','``arêtes libres\'\''.replace("\\'","'")),
('I047-23','deletion','lower crossed relation and its quote',r'\unsure{A_\ell}\subset\vec A/\sigma; ens. des sommets supplémentaires'),
('I047-24','insertion','between upper map and lower inclusion','def'),
('I047-25','margin note','upper-left diagonal note','pas assez précis comme donnée.'),
('I047-26','display','end of diagonal note',r'T_a; \omega(\unsure{T|T_a})\simeq\omega(a)'),
('I047-27','margin note','upper-left enclosed three-line note',"J'ai indiqué une pondé- / ration des sommets, / mais pas des arêtes"),
('I047-28','drawing','around the three-line margin note','open enclosing curve'),
('I047-29','drawing','left-middle, main connected graph','vertices 0, 13, 4, 2, 0, 3, 1; parallel edges, loop and free arms'),
('I047-30','drawing','below main graph, left of its lower endpoint','isolated filled vertex labelled 2'),
('I047-31','drawing','below isolated 2','vertex 0 with three free arms'),
('I047-32','drawing','lowest separate graph component','vertex 3 with one oval loop'),
('I047-33','deletion','large crossed central proposal','Ou encore, posons'),
('I047-34','insertion','inside cancelled proposal, above sommets phrase',r'\unsure{apparents|marqués}'),
('I047-35','deletion','locally crossed word within cancelled proposal',r'\unsure{marqués}'),
('I047-36','insertion','within cancelled proposal above libres/du graphe',r'(i.e. correspondant à \unsure{\alpha|a}\in A_\ell)'),
('I047-37','diagram','bottom of crossed central proposal',r'\widetilde S\xrightarrow{\pi}\mathbb N'),
('I047-38','text','right of crossed proposal enclosure',r'(\uline{pondération} du graphe)'),
('I047-39','display','lower left, first marginal equation',r'\widetilde S=S\amalg\deleted{\unsure{S_\ell}}'),
('I047-40','deletion','right term in first marginal equation',r'\unsure{S_\ell}'),
('I047-41','deletion','to right of first marginal equation',r'\unsure{apparents}'),
('I047-42','insertion','below cancelled right term in first marginal equation',r'A_\ell'),
('I047-43','display','lower-left quotient equation',r'\widetilde A=\vec A/\sigma=A\amalg A_\ell'),
('I047-44','diagram','lower-left decomposition and quotient maps',r'\vec A=\vec A_0\amalg\vec A_\ell; \deg2,\deg1; \widetilde A=A\amalg A_\ell'),
('I047-45','deletion','left of the long live vertical quotient arrow','crossed older shafts, no certified letter'),
('I047-46','margin note','bottom-left heading',"Ordre d'un sommet"),
('I047-47','display','below order heading',r'\sigma(s)=\sigma_\ell(s)+\sigma_0(s)'),
('I047-48','margin note','below square bracket under sigma ell(s)','correspond aux ``trous\'\' ou cercles de recollage'.replace("\\'","'")),
('I047-49','text','lower main paragraph','La donnée du graphe sous-jacent'),
('I047-50','deletion','lower paragraph after graphe','MD'),
('I047-51','insertion','above lower cancelled MD','bip.'),
('I047-52','display','lower main tuple',r'(S,(\vec A\setminus\vec A^\sigma),\sigma|(\vec A\setminus\vec A^\sigma),o|(\vec A\setminus\vec A^\sigma))'),
('I047-53','text','below tuple','plus un ensemble A ell (arêtes libres)'),
('I047-54','insertion','above ensemble','fini'),
('I047-55','deletion','between arêtes and libres','small unreadable crossed trace of three bars'),
('I047-56','deletion','penultimate prose line','ou ``sommets-trous)'),
('I047-57','text','after the cancelled alternative','et une application'),
('I047-58','diagram','last displayed map',r'A_\ell\longrightarrow S'),
('I047-59','text','bottom line','Flèches Les iso. de telles structures'),
]:
    inv(*row)
inv('I047-60','margin note','bottom right','46','separate thin foliation hand; attribution undetermined')

unresolved=[]
def doubt(place,reading,issue,alternatives,confidence,label):
    cp=crops[label]
    unresolved.append(dict(place=place,reading=reading,issue=issue,alternatives=alternatives,
                           confidence=confidence,crop=cp['path'],box=cp['box']))
doubt('Header cancelled initials',r'\deleted{\unsure{\mathrm{MD}}}',
      'The left capital is crossed; D is clearer than M.', ['MD','unrecoverable earlier left capital followed by D'],'medium','header')
doubt('First-map earlier label',r'\deleted{\unsure{g}}',
      'Hatching obscures the original loop/descender junction.', ['g','another crossed looped label'],'medium','genus_map')
doubt('Second-map cancelled domain',r'\deleted{\unsure{\vec A^\sigma|\vec A}}',
      'Vector arrow is certain, but a distinct raised sigma cannot be isolated from the cancellation.', [r'\vec A^\sigma',r'\vec A'],'medium','rigidity_map')
doubt('Second-map crossed label and position of 2',r'r\,\deleted{\unsure{\rho}}\,2',
      'The crossed loop is rho-like; the surviving digit 2 is near r baseline, but its prior relation to the cancelled form cannot be fixed.',
      [r'r\,\deleted{\rho}\,2',r'r\,\deleted{\rho}_{2}'],'medium','rigidity_map')
doubt('Caption short cancelled fragment',r'\deleted{\unsure{rigi}}',
      'Small dots and descender remnants support only a tentative short run.', ['rigi','rig with further crossed remnant'],'low','rigidity_caption')
doubt('Caption longer cancelled word',r'\deleted{\unsure{rigidification}}',
      'Long horizontal cancellation erases much of the body; f/g-like descenders alone do not certify every letter.', ['rigidification','partially unreadable longer word'],'low','rigidity_caption')
doubt('Crossed gloss',r'\deleted{``\unsure{arêtes libres}\'\'}'.replace("\\'","'"),
      'Several letter bodies lie under diagonal hatching.', ['arêtes libres','partly unrecoverable gloss'],'medium','free_definition')
doubt('Crossed lower relation',r'\deleted{\unsure{A_\ell}\overset{\mathrm{def}}{\subset}\vec A/\sigma}',
      'Left term remains uncertain under the strike. Def is drawn above the inclusion, between lines; exact attachment is a placement judgement.',
      [r'A_\ell\overset{\mathrm{def}}{\subset}\vec A/\sigma','def as a detached between-line annotation'],'medium','free_definition')
doubt('Crossed quoted phrase',r'ens. des \unsure{sommets supplémentaires}',
      'Ens. is clear, but crossing strokes obscure parts of the following two words and their line break.', ['sommets supplémentaires','partly unrecoverable quoted description'],'medium','free_definition')
doubt('Slanted note capitalization',r'\unsure{La|la}',
      'The initial joining stroke and loop do not decisively distinguish a capital L from the small l form in this slant.', ['La','la'],'medium','slant_margin')
doubt('Second marginal T',r'\omega(\unsure{T|T_a})\simeq\omega(a)',
      'No separately bounded a is secure in the dark lower-right stroke inside the first parentheses.', ['T',r'T_a'],'medium','slant_margin')
doubt('Cancelled proposal interlinear word',r'\inserted{\unsure{apparents|marqués}}',
      'Two early downward strokes and the final rise fit apparents, while crossing strokes leave a marqués-like alternative viable.', ['apparents','marqués'],'low','cancelled_main')
doubt('Cancelled proposal local deletion',r'\deleted{\unsure{marqués}}',
      'The local horizontal strike runs across the word body.', ['marqués','partly unreadable crossed word'],'medium','cancelled_main')
doubt('Cancelled proposal libres',r'``\unsure{libres}\'\''.replace("\\'","'"),
      'The beginning and ending are crossed by the large cancellation and boundary line.', ['libres','partly unreadable quoted word'],'medium','cancelled_main')
doubt('Cancelled proposal inserted element',r'\unsure{\alpha|a}\in A_\ell',
      'The small rounded element has a short right rising stroke; Latin a and alpha remain graphically compatible.', [r'\alpha','a'],'medium','cancelled_main')
doubt('Marginal cancelled right term',r'\deleted{\unsure{S_\ell}}',
      'The upper body is densely retraced; ell survives separately, but the leading S cannot be certified.', [r'S_\ell','another crossed leading capital with ell'],'low','margin_S')
doubt('Marginal crossed word',r'\deleted{\unsure{apparents}}',
      'Two early descenders and terminal t/s-like strokes survive, with middle letters hidden by the horizontal strike.', ['apparents','partly unrecoverable crossed word'],'medium','margin_S')
doubt('Old shafts beside marginal quotient arrow',split_diagram,
      'The lower crossed turns look A-like but do not certify an independent letter; only the visible paths are reproduced.', ['crossed former arrow shafts','crossed shafts mixed with an unrecoverable earlier mark'],'medium','margin_split')
doubt('Small deletion after arêtes',r'\deleted{\illegible{1}}',
      'Three short bars and connecting overtrace do not yield a readable word or symbol.', [],'low','free_attachment')
doubt('Ending of cancelled sommets-trous',r'\deleted{ou ``sommets-trous)}',
      'Closing parenthesis is visible; a separate closing quotation pair is not distinguishable beneath the cancellation.', ['no secure closing pair','closing pair absorbed by the strike'],'medium','free_attachment')

notes=[
dict(id='N047-01',text='This is a continuation leaf beginning “qui forment un groupoïde”. It defines finite graph data (S, vector A, sigma, o), permits isolated vertices, loops, multiple edges and free edges, and adds supplementary structure.'),
dict(id='N047-02',text='The first displayed map assigns a genre or poids to vertices. The second is captioned indice de rigidification. The live 2 beside its crossed former label is preserved on the baseline; no mathematical interpretation is used to delete it or force it into a subscript.'),
dict(id='N047-03',text='The crossed lower inclusion and the crossed proposal using S-tilde are retained as cancelled work. The pondération du graphe caption is outside the enclosure and remains live because no cancellation crosses it.'),
dict(id='N047-04',text='The diagonal margin note says that the data are not precise enough and that an edge weighting should be replaced by a combinatorial pol. T_a with the stated omega relation. The page does not establish the meaning of pol. or prove that relation; its second T subscript remains open.'),
dict(id='N047-05',text='The enclosed note says that vertex weights have been indicated but edge weights have not. The adjacent drawing contains seven connected weighted vertices and an isolated vertex labelled 2, followed below by a three-arm vertex 0 and a loop at vertex 3. Pale centers, gaps and thin arms are retained as drawing features.'),
dict(id='N047-06',text='The marginal decomposition separates nonfixed and fixed elements of the involution and labels their quotient maps degree 2 and degree 1. The lower paragraph states that an ordinary graph together with a finite free-edge set and its attachment to S recovers the graph with free edges. Check B047-K01 verifies these claims conditionally on the stated definitions.'),
dict(id='N047-07',text='Sigma is used both for the involution on vector A and in the local order notation sigma(s)=sigma_ell(s)+sigma_0(s). The latter ell component is associated on the page with holes or gluing circles. This notational reuse is retained.'),
dict(id='N047-08',text='The top 3) is the manuscript’s own page number. The bottom 46 is written in a separate thin hand and is retained as an unassigned margin foliation; no attribution is inferred.'),
dict(id='N047-09',text='H’s explanatory notes and repeated align formulas are editorial witnesses, not extra source text. The source has one decomposition diagram with explanatory formulas under brackets. C’s extra A_ell before the crossed arêtes-libres gloss has no independently visible token and is omitted.'),
dict(id='N047-10',text='The first involution-map shaft has only a small terminal tip; no hook or origin bar has been added. The final attachment-map A is retraced, but no independent earlier letter is secure. A faint isolated spot below its S is not treated as punctuation.'),
]
checks=[dict(statement_id='B047-K01',date='2026-11-21',
             who='Reader B; GPT-6 Astra Pro; effort not exposed; run SP82_C13_148',
             type='targeted proof check',
             outcome='Verified conditionally on sigma being an involution and o: vector A -> S being the stated origin map. If a is not fixed, sigma(a) differs from a and sigma(sigma(a))=a, so its orbit has exactly two elements. A fixed element has a one-element orbit. Thus the quotient restricts to degree 2 on vector A minus vector A^sigma and degree 1 on vector A^sigma, as labelled. Restricting o and sigma to the nonfixed part gives the ordinary graph; retaining the fixed elements as A_ell with their o-values gives A_ell -> S. Conversely adjoining those fixed elements with this attachment reconstructs the original unweighted graph data. This check does not decide the cancelled domain exponent, the live 2 beside r, or the marginal T subscript.')]

hand_log=[
dict(habit='Vector A is marked by a separate short horizontal shaft with a rightward head; the tilde on A or S is a curved wave.',pages=[47],scope='holds_at_every_observed_occurrence',holds_at_every_observed_occurrence=True,
     observed_scope='All readable vector and tilde marks in the main definitions, cancelled rigidity domain, marginal quotient/decomposition and final tuple on scan047.',
     witness_effect='C used a tilde on the cancelled rigidity domain although its overmark has a visible arrowhead. The raised sigma of that domain remains uncertain independently.'),
dict(habit='The unstruck ell index has a small loop and a long rightward foot, distinct from the numerical 1 in graph and degree labels.',pages=[47],scope='holds_at_every_observed_occurrence',holds_at_every_observed_occurrence=True,
     observed_scope='All readable live A_ell and vector A_ell indices in the two maps, marginal equations/decomposition and attachment statement.',
     witness_effect='This form supports resolving C’s doubt at the live rigidity-map A_ell. It does not resolve the heavily crossed lower relation or cancelled marginal capital.'),
dict(habit='The codomain N of each displayed map has a doubled left stem with a narrow white channel.',pages=[47],scope='holds_at_every_observed_occurrence',holds_at_every_observed_occurrence=True,
     observed_scope='The three N codomains: genus map, rigidity map and cancelled S-tilde map.',
     witness_effect='H typesets these as bold N; the visible double stroke is preserved as mathbb N.'),
]
notation=[
dict(symbol=r'(S,\vec A,\sigma,o)',meaning='Finite vertex and directed-edge data with an involution and an origin map.',pages=[47],confidence='high'),
dict(symbol=r'A_\ell',meaning='The free-edge set, with an attachment map to S; corresponding fixed elements are written vector A_ell = vector A^sigma in the marginal diagram.',pages=[47],confidence='high'),
dict(symbol=r'\widetilde A=\vec A/\sigma=A\amalg A_\ell',meaning='The orbit set is decomposed into ordinary edge orbits and free edges.',pages=[47],confidence='high'),
dict(symbol=r'\vec A_0',meaning='The under-bracket formula is vector A minus vector A^sigma; its quotient arrow has label deg 2.',pages=[47],confidence='high'),
dict(symbol=r'\gamma:S\longrightarrow\mathbb N',meaning='Captioned application genre ou poids.',pages=[47],confidence='high'),
dict(symbol=r'r:A_\ell\longrightarrow\mathbb N',meaning='Captioned indice de rigidification. A separate live 2 and an earlier crossed label are present beside r; their role is left unresolved.',pages=[47],confidence='medium'),
dict(symbol=r'\sigma(s)=\sigma_\ell(s)+\sigma_0(s)',meaning='Order of a vertex; a square bracket associates the ell summand with trous ou cercles de recollage.',pages=[47],confidence='high'),
dict(symbol=r'T_a',meaning='Called a pol. comb. in the diagonal margin note; the second occurrence inside omega may omit its subscript.',pages=[47],confidence='medium'),
]
abbreviations=[
dict(form='suppl.',expansion='supplémentaires',confidence='high'),
dict(form='pts',expansion='points',confidence='high'),
dict(form='ens.',expansion='ensemble',confidence='high'),
dict(form='ens',expansion='ensemble',confidence='high'),
dict(form='appl.',expansion='application',confidence='high'),
dict(form='pol.',expansion='undetermined on this page',confidence='low'),
dict(form='comb.',expansion='combinatoire',confidence='high'),
dict(form='identif.',expansion='identifié',confidence='medium'),
dict(form='bip.',expansion='bipondéré',confidence='medium',note='Inferred only from the neighbouring Grbip/Grabipond naming on this page.'),
dict(form='ss',expansion='sans',confidence='high'),
dict(form='deg',expansion='degré',confidence='high'),
dict(form='iso.',expansion='isomorphismes',confidence='high'),
dict(form='i.e.',expansion='id est',confidence='high'),
]

def between(start,end):
    return F[F.index(start):F.index(end,F.index(start))].strip()
second_boxes=[]
def blind(label,kind,reading,box=None):
    b=box or crops[label]['box']
    second_boxes.append(dict(box=f'B047-B{len(second_boxes)+1:02d}',kind=kind,
                             x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
blind('author_number','handwritten number',r'\mspage{3)}')
blind('header','different-word passage and deletion',between('qui forment','\n\nObjets'),[232,80,1660,161])
blind('objects','different-word passage and insertions',between('Objets :','plusieurs arêtes'))
blind('free_edges','different-word passage and insertion',between('plusieurs arêtes',r'$S,\inserted'))
blind('set_definition','insertion and complete formulas',between(r'$S,\inserted',r'\diagram{\begin{tikzcd}'))
blind('genus_map','doubtful whole formula and insertion',macro(F,r'\diagram'))
blind('rigidity_map','doubtful whole formula, deletion and handwritten number',macro(F,r'\diagram',F.index('(application ``genre')))
blind('rigidity_caption','cancelled words',between('(application \\deleted','\n\n\\deleted{``'))
blind('free_definition','cancelled gloss and whole doubtful relation',between(r'\deleted{``',r'\margin{pas assez'))
blind('slant_margin','margin note and whole doubtful formula',macro(F,r'\margin'))
blind('circled_margin','margin note and enclosure',circled)
blind('main_graph','drawing and handwritten numbers',main_drawing)
blind('lower_graphs','drawings and handwritten numbers',lower_drawing)
blind('cancelled_main','struck passage, insertions and live caption',central)
blind('margin_S','margin formula, deletion and insertion',margin_s)
blind('margin_A','margin formula',r'\widetilde A=\vec A/\sigma=A\amalg A_\ell')
blind('margin_split','margin diagram, handwritten numbers and cancelled strokes',split_diagram)
blind('margin_order','margin note and formula',"Ordre d'un sommet\n"+order_diagram,[56,2040,475,2334])
blind('underlying_text','different-word passage, deletion and insertion',between('La donnée',r'\['))
blind('underlying_tuple','whole formula',between(r'\left(S,',r'\]'))
blind('free_attachment','insertion, deletion and different-word passage',between(r'\uline{plus}',r'\diagram{\begin{tikzcd}'))
blind('attachment_map','formula',macro(F,r'\diagram',F.index('et une application')))
blind('arrows_end','different punctuation passage',between(r'\uline{Flèches}',r'\margin{46}'))
blind('foliation','handwritten number',r'\margin{46}')

logical_lines=[
'3)', 'qui forment un groupoïde … Grbip ou (Grabipond)',
'Objets : graphes … tuple', 'finis (upper insertion)', '+ structures suppl. (upper insertion)',
'(pouvant avoir des', 'sommets isolés, des boucles fermées, a fortiori',
'plusieurs arêtes entre deux sommets, et aussi', 'des arêtes libres … fixes de sigma)',
'(sommets, arcs) (insertion)', 'S, ens. finis, sigma map and involution',
'vector A (raised insertion)', 'o map, appl. origine', 'On se donne de plus',
'S to N with corrected gamma', 'application genre ou poids',
'cancelled domain = A ell to N with r/cancelled form/live 2',
'application and longer cancelled caption word', 'upper short cancelled rigi fragment',
'indice de rigidification (replacement caption)', 'crossed arêtes libres gloss',
'crossed A ell subset vector A/sigma and beginning quoted ens. phrase',
'continuation of the crossed supplementary-vertices phrase', 'def (between-line annotation)',
'Ou encore, posons S tilde = S disjoint-union A ell, (identif.',
'à l’ens de tous les sommets, crossed word and et', 'upper interlinear apparents/marqués',
'lower quoted marqués (i.e. in S)', 'i.e. correspondant à alpha/a in A ell (insertion)',
'et libres du graphe), l’on donne', 'cancelled S tilde to N with pi',
'pondération du graphe (live caption)', 'pas assez précis', 'comme donnée.',
'La/la pondération', 'd’une arête doit être', 'remplacée par celle', 'd’un pol. comb.',
'T_a avec', 'omega relation', 'J’ai indiqué une pondé-', 'ration des sommets,',
'mais pas des arêtes', 'marginal S tilde equation and crossed apparents',
'A ell (lower insertion)', 'marginal A tilde quotient equation',
'decomposition top row', 'two explanatory bracket formulas on one row',
'deg 2 and deg 1 labels on the downward-arrow row', 'decomposition bottom row',
'Ordre d’un sommet', 'sigma(s) order equation', 'correspond', 'aux trous',
'ou cercles', 'de recollage', 'La donnée du graphe sous-jacent à un',
'graphe MD/bip. revient à celle d’un graphe', 'bip. (raised insertion)',
'ordinaire correspondant (sans arêtes libres,', 'i.e. où sigma opère ss pts fixes), i.e.',
'complete tuple', 'plus un ensemble A ell (arêtes, crossed trace, libres)',
'fini (raised insertion)', 'cancelled ou sommets-trous) et une application',
'A ell to S', 'Flèches Les iso. de telles structures', '46',
]

reviews={}
def review(ids,decision,reading,evidence):
    for i in ids:
        reviews[i]=dict(decision=decision,reading=reading,evidence=evidence)
review([1043,1044],'editorial/macro only',r'\scanpage{47}\mspage{3)}','Archive marker and H’s explanatory author-page note are not additional source words; author_number crop confirms 3).')
review([1045,1046],'C supported',r'\deleted{\unsure{\mathrm{MD}}}.\ \mathrm{Grbip}','header: cancelled capitals remain qualified; first name has no internal dot or enclosing parentheses.')
review([1047],'C doubt resolved',r'(\mathrm{Grabipond})','header: complete letter run and absence of internal dot.')
review([1048,1049],'other',r'\inserted{$+$ structures suppl.}','objects: plural s and placement leader attach the addition to the object data; extra C comma is not separate ink.')
review([1050],'C supported','pouvant avoir','objects: p-o-u-v-a-n-t and a-v-o-i-r.')
review([1051],'C supported','a fortiori','objects: the full written words replace H’s plus sign.')
review([1052,1055,1059,1060,1068,1106],'quotation convention',"paired `` and '' ticks",'Paired handwritten ticks are set in the required C quotation convention; H’s guillemets are an encoding convention, not separate words.')
review([1053,1054],'other',r'\uline{arêtes} libres; \inserted{(``sommets\'\', ``arcs\'\')}'.replace("\\'","'"),'free_edges: underline ends before libres, arcs is readable, insertion attaches locally, no final colon after sigma parenthesis.')
review([1056,1057,1058],'diagram reading checked',r'S\xrightarrow{\deleted{\unsure{g}}\inserted{\gamma}}\mathbb N','genus_map: gamma resolved and doubled N preserved; TikZ/arrow syntax differences alone are not source changes.')
review([1061],'editorial description incorporated',r'\deleted{\unsure{g}}\inserted{\gamma}','genus_map: H’s note describes a real correction, not a further textual sentence.')
review([1062,1064,1066,1090,1108,1109,1111],'macro only','same diagram content','Macro and arrow syntax do not add source characters; every actual diagram was read on its saved crop.')
review([1063],'other',r'\deleted{\unsure{\vec A^\sigma|\vec A}}','rigidity_map: vector head certain, raised sigma and crossed original body remain uncertain; H’s live exponent was editorial.')
review([1065],'other',r'r\,\deleted{\unsure{\rho}}\,2','rigidity_map: 2 survives to the right of the crossed form, near r baseline.')
review([1067],'other',r'\deleted{\unsure{rigi}}\deleted{\unsure{rigidification}}','rigidity_caption: two separate cancelled traces, neither fully readable.')
review([1069,1070,1071],'other',r'\deleted{``\unsure{arêtes libres}\'\'};\ \deleted{\unsure{A_\ell}\overset{\mathrm{def}}{\subset}\vec A/\sigma}'.replace("\\'","'"),'free_definition: no extra A ell before the gloss; lower relation is struck; def sits above the lower inclusion.')
review([1072,1073,1074],'alignment mismatch reviewed',central,'The table aligns different parts of the crossed block. free_definition/cancelled_main support short ens., Ou encore, posons, (identif., underlined tous/marqués, inserted alpha/a phrase, closing graphe), l’on donne, and a live pondération caption. H’s non is unsupported.')
review([1075,1076],'C supported','pas assez précis comme donnée.','slant_margin: no comma after précis; one point after donnée rather than a colon.')
review([1077],'other',r'\omega(\unsure{T|T_a})\simeq\omega(a)','slant_margin: first T_a resolved, second subscript open; no final period.')
review(list(range(1078,1083)),'drawing fully checked',main_drawing,'main_graph/circled_margin: enclosing curve restored, all seven main vertices and edges counted, white centers and fine/gapped arm preserved.')
review([1083,1084],'other','isolated filled vertex 2; lower vertex 0 with three free arms','main_graph/lower_graphs: H’s 2-degree reading is unsupported; H’s later note correctly restores the third arm.')
review([1085,1086,1087],'drawing fully checked',lower_drawing,'lower_graphs: thin upper-right arm and pale center of the loop vertex retained; table also spills into the marginal equations.')
review([1088],'alignment mismatch reviewed',central,'cancelled_main: full cancelled proposal is transcribed from ink rather than H’s synopsis; the next marginal equations are separate.')
review([1089],'other',margin_s+'\n'+split_diagram,'margin_S/margin_A/margin_split: preserve cancelled term/word and lower insertion, omit unsupported punctuation and H’s duplicated expanded align block.')
review([1091,1092],'C placement supported',split_diagram,'margin_split: the two formulas belong beneath the diagram brackets, with no separately written equality expansions.')
review([1093],'H observation incorporated',split_diagram,'margin_split: literal crossed old shafts are drawn beside the live downward arrow; no independent text is certified.')
review([1094,1096],'other',order_diagram,'margin_order: square bracket, correspond without -ant, lower four-line annotation, no added terminal period.')
review([1095],'C supported',r'\sigma(s)=\sigma_\ell(s)+\sigma_0(s)','margin_order: no comma after the last parenthesis.')
review([1097],'C supported',r'du \uline{graphe}','underlying_text: singular du graphe.')
review([1098],'C supported','sous-jacent','underlying_text: final t without s.')
review([1099],'C supported',"d'un graphe ``ordinaire'' correspondant",'underlying_text: all singular forms are visible.')
review([1100],'H supported','sans arêtes libres, i.e.','underlying_text: short dark descending comma at the far right.')
review([1101],'C supported','ss pts fixes','underlying_text: the abbreviation is not expanded.')
review([1102,1103,1104,1105],'macro only',r'\sigma|(\vec A\setminus\vec A^\sigma),\ o|(\vec A\setminus\vec A^\sigma)','underlying_tuple: these apparent commas arise from H’s LaTeX thin-space command; no extra ink punctuation is implied.')
review([1107],'other',r'\deleted{ou ``sommets-trous)}','free_attachment: opening quote ticks and closing parenthesis survive; closing quote pair is not independently secure.')
review([1110],'C supported',r'A_\ell\longrightarrow S','attachment_map: one full rightward arrow; no dark terminal period.')
review([1112],'C supported',r'\uline{Flèches} Les','arrows_end: no colon in the gap.')
review([1113],'other',r'Les iso. de telles structures\quad\margin{46}','arrows_end/foliation: no terminal full stop; separate thin-hand 46 is retained.')
differences_review=[]
for raw in csv.DictReader((PACKET/'differences.tsv').open(),delimiter='\t'):
    num=int(raw['source_row'])
    if num not in reviews:
        raise ValueError('Unreviewed difference '+str(num))
    differences_review.append(dict(source_row=num,c=raw['witness C'],h=raw['witness H'],
                                   context=raw['words before'],**reviews[num]))

reading_workflow=[
'Read only the scan047 packet, its current notation snapshot, source image, native halves and saved page047 crops.',
'Viewed the whole source image once for layout and read each native overlapping half once line by line against C.',
'Created 24 enhanced evidence crops once each; displayed same-pixel JPEG encodings and actually viewed all 24.',
'Reused the existing rigidity_map and free_definition crops to settle physical placement; no second crop was created.',
'Read every C/H differing-word passage, every C marked doubt, all insertion/deletion scopes, all formulas, every graph label and every diagram shaft/head.',
'Inspected each drawing’s components on the half and again on its evidence crop; no OCR, internet research or TeX compilation was used.',
'Parent reader independently viewed the whole, both halves and all 24 crops; agreed corrections were incorporated without reading another page.',
]
result=dict(scan=47,reader='B',model='GPT-6 Astra Pro',reasoning_effort='not exposed',run='SP82_C13_148',
            lines_read=len(logical_lines),
            lines_read_basis='68 logical source text/display baselines: prose baselines, separate insertion baselines, displayed map/equation rows and marginal-note lines each count once. Parallel diagram columns on one row count once. Individual graph numerals and path strokes are fully inventoried and boxed but are not added to this text-line count.',
            reading_workflow=reading_workflow,changes=changes,decisions=decisions,inventory=inventory,
            unresolved=unresolved,notes=notes,checks=checks,hand_log=hand_log,notation=notation,
            abbreviations=abbreviations,second_boxes=second_boxes,differences_review=differences_review,
            reading_procedure=dict(whole_views=1,native_half_views=[1,1],crop_count=24,crops_created_once=True,
                                   all_crops_actually_viewed=True,crop_manifest='readers/148_scan047/crop_manifest.json',
                                   no_ocr=True,no_web_research=True,no_tex_compilation=True,
                                   logical_source_lines=logical_lines))

expected_marks={x['id'] for x in csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t')}
assert {x['id'] for x in decisions}==expected_marks and len(decisions)==len(expected_marks)
assert len(logical_lines)==68
assert len(differences_review)==71 and len({x['source_row'] for x in differences_review})==71
assert len(second_boxes)==24 and len({x['box'] for x in second_boxes})==24
assert all(0<=b['x0']<b['x1']<=1686 and 0<=b['y0']<b['y1']<=2356 for b in second_boxes)
assert all((ROOT/'work/SP82_C13_148'/x['crop']).exists() for x in changes+decisions)
assert all(x['box']==crops[Path(x['crop']).stem.removeprefix('148_scan047_')]['box'] for x in changes+decisions)
assert all(x['confidence'] in {'high','medium','low'} for x in changes+decisions+unresolved)
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in inventory)
assert all(x['sheet_kind']=='text' for x in inventory)
assert all(x['transcribed']=='yes' for x in inventory)
assert all(x['type'] in {'targeted proof check','computation or formal certificate'} for x in checks)
assert all('effort not exposed' in x['who'] and 'SP82_C13_148' in x['who'] for x in checks)
assert all(x['scope']=='holds_at_every_observed_occurrence' for x in hand_log)
for text in [F]+[x['reading'] for x in second_boxes]:
    braces=0
    for i,ch in enumerate(text):
        if ch in '{}' and (i==0 or text[i-1]!='\\'):
            braces += 1 if ch=='{' else -1
            assert braces>=0, text[:100]
    assert braces==0, (braces,text[:100])
    assert len(re.findall(r'\\begin\{tikzpicture\}',text))==len(re.findall(r'\\end\{tikzpicture\}',text))
    assert len(re.findall(r'\\begin\{tikzcd\}',text))==len(re.findall(r'\\end\{tikzcd\}',text))
(OUT/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(scan=47,changes=len(changes),marks=len(decisions),inventory=len(inventory),
                     unresolved=len(unresolved),second_boxes=len(second_boxes),differences=len(differences_review),
                     lines_read=len(logical_lines),checks=len(checks)),ensure_ascii=False))

