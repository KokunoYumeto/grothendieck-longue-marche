from pathlib import Path
import json

root = Path('/workspace/scratch/481648fc487b/SP90_C13_150_work')
packet = Path('/workspace/scratch/481648fc487b/reader_packets/150_scan029')
C = (packet / 'C.tex').read_text()
H = (packet / 'H.tex').read_text()

figure = r'''\figure{\begin{tikzpicture}[x=0.016cm,y=-0.016cm]
\draw[line width=1pt] (21,35)--(21,187);
\draw (26,35) .. controls (25,75) and (27,140) .. (22,176);
\draw[line width=1pt] (16,188)--(248,181);
\draw (24,187) .. controls (68,198) and (167,185) .. (213,188);
\draw (31,34) .. controls (40,28) and (55,24) .. (60,28)
.. controls (68,31) and (66,49) .. (76,53)
.. controls (90,59) and (103,48) .. (122,54)
.. controls (145,61) and (172,61) .. (186,72)
.. controls (193,79) and (201,72) .. (207,83)
.. controls (214,94) and (218,112) .. (226,121)
.. controls (238,132) and (246,153) .. (253,182);
\draw (32,22) .. controls (48,12) and (65,7) .. (78,10)
.. controls (93,14) and (113,31) .. (127,30)
.. controls (145,29) and (166,15) .. (174,22)
.. controls (185,31) and (183,35) .. (197,35)
.. controls (208,35) and (219,36) .. (226,46)
.. controls (229,54) and (228,65) .. (236,79)
--(222,87);
\draw (240,87) .. controls (251,91) and (246,101) .. (250,115)
.. controls (255,138) and (265,161) .. (262,181);
\draw[line width=1.6pt] (21,186)--(190,100);
\draw (55,184)--(67,161);
\draw (70,185)--(87,153);
\draw (89,184)--(112,143);
\draw (108,184)--(137,137);
\draw (150,183) .. controls (157,162) and (176,145) .. (171,137);
\end{tikzpicture}}'''

order_diagram = r'''\diagram{\begin{tikzcd}[column sep=small,row sep=small]
& j' \arrow[r,leftrightarrow,"\mathrm{préd}"'] \arrow[d,phantom,"{\rotatebox{90}{$\leq$}}" description] & j \arrow[d,phantom,"{\rotatebox{90}{$\leq$}}" description] \\
& k' \arrow[r,leftrightarrow] & k \\
i \arrow[uur,hook] \arrow[urr,hook] & &
\end{tikzcd}}'''

square = r'''\diagram{\begin{tikzcd}
X_{j'} \arrow[r,hook] & X_j \\
X_{k'} \arrow[u] \arrow[r,hook] & X_k \arrow[u]
\end{tikzcd}}'''

condition = r"La \deleted{condition} \inserted{c)} \unsure{impliquent|implique}"
power = r"$\mathcal P(\unsure{\sigma|F})$"
struck_set = r"\deleted{$\unsure{k\ne k'}$}"
set_line = r"$j'\subset j=j'\amalg\{\alpha\}$, et $k\in j$ mais non $k\subset j'$,"
set_end = r"alors \deleted{$\unsure{k\ne k'}$} $k=k'\amalg\{\alpha\}$ avec $k'=k\cap j'$, ..)"
hypothesis = r"$\unsure{1^\circ)|16)}$"
struck_map = r"\deleted{$(X_k\longrightarrow X_{\unsure{j}}$.}"
pair_map = r"$(X_k,X_{k'})\mathbin{-}(X_j,X_{j'})$"

page = r'''\scanpage{29}
structure locale de $X_j$ le long d'un $X_i$
(avec la stratification induite de type $I_{ij}$)
est ``cubique''
(coin de cube de
dimension $n=\operatorname{card}S$)

''' + figure + '\n\n' + condition + r''' que si $j'$ est
un prédécesseur de $j$, et si $k\in I$ est $\le j$
mais non $\le j'$, et s'il existe
un $i$ majoré par $k$ et $j'$, \uline{alors}
$k'=\operatorname{Inf}(k,j')$ existe, et $k'$ est
un prédécesseur de $k$.

''' + order_diagram + r'''

(Il suffit de voir que dans
un ens. ordonné de la forme ''' + power + r''',
les inf exist (c'est l'intersection) et si
''' + set_line + '\n' + set_end + r'''
\margin{$\sigma$ ens fini}

Ceci posé, considérons le diagramme
''' + square + r'''
où les flèches verticales, par l'hyp. ''' + hypothesis + r''',
sont des plongements bordants. Ceci posé, on
voit \inserted{(par b,c)} que ''' + struck_map + '\n' + pair_map + r'''
\margin{28}
'''

boxes = {
 'cubique':[325,254,782,468],
 'corner_drawing':[878,251,1152,455],
 'condition_verb':[440,518,1145,651],
 'order_body':[783,627,1654,1020],
 'order_diagram':[277,772,622,1071],
 'power_set':[1203,1125,1480,1235],
 'finite_margin':[42,1194,278,1299],
 'inf_existent':[333,1244,710,1340],
 'intersection_words':[752,1243,1322,1332],
 'set_calculation':[332,1335,1665,1560],
 'struck_set_formula':[616,1461,771,1548],
 'square_diagram':[568,1710,963,1990],
 'hypothesis_number':[1228,1977,1638,2100],
 'inserted_bc':[267,2173,604,2327],
 'struck_map':[617,2207,967,2324],
 'pair_map':[975,2195,1594,2323],
 'folio':[18,2301,81,2342],
}

def crop(name):
    return f'150_scan029_{name}.jpg'

def block(text, begin, end):
    return text[text.index(begin):text.index(end,text.index(begin))].strip()

C_figure = block(C, r'\figure{', '\n\nLa')
C_order = block(C, r'\diagram{', '\n\n(Il suffit')
H_order_start = H.index(r'\begin{tikzcd}')
H_order_end = H.index(r'\end{tikzcd}', H_order_start) + len(r'\end{tikzcd}')
H_order = H[H_order_start:H_order_end]
C_square_start = C.index(r'\diagram{', C.index('Ceci posé, considérons'))
C_square_end = C.index(r'\end{tikzcd}}', C_square_start) + len(r'\end{tikzcd}}')
C_square = C[C_square_start:C_square_end]
H_square_start = H.index(r'\begin{tikzcd}', H.index('Ceci posé, considérons'))
H_square_end = H.index(r'\end{tikzcd}', H_square_start) + len(r'\end{tikzcd}')
H_square = H[H_square_start:H_square_end]

changes = []
def change(place, c, h, final, evidence, name, kind, error_kind,
           change_C=False, change_H=False, confidence='high', marked=False, consequential=''):
    changes.append(dict(place=place,C=c,H=h,final=final,evidence=evidence,
        crop=crop(name),box=boxes[name],confidence=confidence,kind=kind,
        error_kind=error_kind,marked_in_H=marked,change_C=change_C,
        change_H=change_H,consequential=consequential))

change('opening local-model paragraph / quotation marks', "``cubique''", '« cubique »',
       "``cubique''", 'Each side has two short high ticks; there are no angle-shaped guillemets.',
       'cubique','other','other',change_H=True)
change('opening local-model paragraph / final punctuation',
       r'(coin de cube de dimension $n=\operatorname{card}S$)',
       r'(coin de cube de dimension $n=\mathrm{card}\,S$).',
       '(coin de cube de\ndimension $n=\\operatorname{card}S$)',
       'The curved closing parenthesis is followed by blank paper, without a separate full stop.',
       'cubique','text not on the page','text not on page',change_H=True)
change('upper-right corner drawing / five hatches and contour placement',
       C_figure,
       r'\drawing{À droite, un croquis : un coin de carré (deux axes), une courbe au-dessus et une demi-droite hachurée issue du sommet.}',
       figure,
       'Five distinct hatch strokes are visible: four comparatively straight strokes and the rightmost curved stroke. C draws six. The heavy diagonal stops inside the wavy boundary; the final three hatches end below it. Two wavy contours, a notched interruption at upper right, retraced axes, and the separate descending right contour are retained. There are no arrowheads or marked vertices.',
       'corner_drawing','drawing or diagram','drawings and diagrams',change_C=True,change_H=True,
       consequential='Preserves the actual number and disposition of drawn strokes; no mathematical interpretation of the drawing is supplied.')
change('predecessor assertion / deletion scope',
       r'La \deleted{condition c)}',r'\struck{La condition} c)',
       r'La \deleted{condition} \inserted{c)}',
       'The cancellation traverses condition only. La is clear of the strike. The c) is above and to the right of the canceled word and is not crossed.',
       'condition_verb','deletion state (struck given live or live given struck)','struck text',change_C=True,change_H=True)
change('predecessor assertion / raised c)',
       r'\deleted{condition c)}',r'\struck{La condition} c)',
       r'La \deleted{condition} \inserted{c)}',
       'The live c) is raised above the principal baseline beside the struck word; it is encoded as an insertion at that location.',
       'condition_verb','insertion or placement','insertion placement',change_C=True,change_H=True)
change('predecessor assertion / capital Inf',
       r"$k'=\operatorname{Inf}(k,j')$",r"$k'=\inf(k,j')$",
       r"$k'=\operatorname{Inf}(k,j')$",
       'The first letter has a tall straight capital-I stem with horizontal extremities. It differs from the small dotted i of the later les inf.',
       'order_body','misread symbol or index','symbols and indices',change_H=True)
change('first diagram / the two vertical order signs',C_order,H_order,order_diagram,
       'Both vertical marks have two unequal branches meeting toward the lower node and a separate extra stroke on the right. They are vertical order signs, represented by a +90-degree rotation of ≤, not downward arrows or ordinary horizontal ≥ signs.',
       'order_diagram','misread symbol or index','symbols and indices',change_C=True,change_H=True,
       consequential='Distinguishes the order relations j′ ≥ k′ and j ≥ k, drawn vertically, from directed morphisms.')
change('first diagram / the two arrows leaving i',C_order,H_order,order_diagram,
       'Each oblique line starts at i with a curled hook and has a terminal arrowhead at the indicated upper node. The top and middle horizontal links have heads at both ends; their label and disposition are retained.',
       'order_diagram','drawing or diagram','drawings and diagrams',change_H=True)
change('parenthetical set argument / truncated exist',
       'les inf existent','les inf existent','les inf exist',
       'After exis the final tall t and its cross-stroke are visible, followed by clear blank space before the parenthesis. There is no following ent and no abbreviation stop. Both witnesses expand the written form.',
       'inf_existent','abbreviation expanded or spelling modernised','abbreviation/spelling',change_C=True,change_H=True)
change('parenthetical set argument / c’est',
       "(c'est l'intersection)","(l'intersection)","(c'est l'intersection)",
       'Between the opening parenthesis and l’intersection there are the connected c, apostrophe, es, and a final raised t stroke. These constitute c’est, absent from H.',
       'intersection_words','omission','omissions',change_H=True)
change('set calculation / lower-case j in first line',
       set_line,
       r"$J'\subset J=J'\amalg\lbrace\alpha\rbrace$, et $k\in J$ mais non $k\subset J'$,",
       set_line,
       'The repeated j stems are narrow and return into small hooked feet; several have the same pointed or looped head as the lower-case j in the surrounding predecessor statement. No separate capital-letter scale or uniform capital-J crossbar is present. The visible ∈ in k∈j is retained, without replacing it by a mathematically more expected subset sign.',
       'set_calculation','misread symbol or index','symbols and indices',change_H=True,
       consequential='Retains the manuscript’s local j notation and its literal k∈j, without repairing the apparent set-theoretic slip.')
change('set calculation / readable letters inside cancellation',
       struck_set,r'\struck{\ill{}}',struck_set,
       'The initial k is visible and a second k-like stem and upper branch survive the cancellation. The relation and the final prime are obscured by the heavy zigzag, so k≠k′ remains explicitly doubtful; the span is not wholly unreadable.',
       'struck_set_formula',r'readable ink left as \ill{}','readable ink left as illegible',
       change_H=True,confidence='low',marked=True)
change('set calculation / final j after intersection',
       r"$k'=k\cap j'$",r"$k'=k\cap J'$",r"$k'=k\cap j'$",
       'This j has a wider top/return than the preceding ones, but its hooked stem is compatible with their lower-case form and with the broad-footed j in the final pair. The letter is not capitalized merely because the terminal return is broad.',
       'set_calculation','misread symbol or index','symbols and indices',change_H=True,confidence='medium')
change('set calculation / terminal two points',
       r", \ldots)",r", \ldots)",', ..)',
       'After the comma there are two separate dark points before the closing parenthesis. There is no third ellipsis point.',
       'set_calculation','text not on the page','text not on page',change_C=True,change_H=True)
change('left marginal note / ens fini',
       r'\margin{$\sigma$ ens fini}',r'\marginal{$\sigma$ \uncertain{sur} $F$}',
       r'\margin{$\sigma$ ens fini}',
       'After the clear sigma are a small e-loop and connected n/s humps, then the tall f, short dotted i, n, and final dotted i of fini. Neither sur nor a lone capital F fits the strokes. No stop is visible after ens.',
       'finite_margin','misread word','words',change_H=True,marked=True)
change('second square / horizontal hooked arrows',C_square,H_square,square,
       'Both horizontal arrows have curled tails at the left; the lower tail is a particularly clear C-shaped hook. Right arrowheads and plain upward vertical arrows are retained. There are no point markers.',
       'square_diagram','drawing or diagram','drawings and diagrams',change_H=True)
change('reference after l’hyp. / number and closing parenthesis',
       r'$\unsure{1^\circ|a)}$',r'\ill{}',hypothesis,
       'A leading 1 is plain, followed by a loop with a small upper tail that permits either the ordinal-degree mark or 6. A distinct closing parenthesis follows before the comma. The form a) is unsupported; the 1°)/16) ambiguity is not resolved from the expected hypothesis.',
       'hypothesis_number','misread symbol or index','symbols and indices',
       change_C=True,change_H=True,confidence='medium',marked=True,
       consequential='The hypothesis reference remains uncertain, with its legible leading digit and closing parenthesis preserved.')
change('canceled bottom map / opening parenthesis',
       r'\deleted{$X_k\longrightarrow X_{\unsure{j}}$}',
       r'\struck{$(X_k\to X)$}',struck_map,
       'A large curved opening parenthesis stands before Xk and is crossed by the same cancellation line. It is missing in C.',
       'struck_map','omission','omissions',change_C=True)
change('canceled bottom map / no closing parenthesis',
       r'\deleted{$X_k\longrightarrow X_{\unsure{j}}$}',
       r'\struck{$(X_k\to X)$}',struck_map,
       'To the right of the target X there is a separate dot but no curved closing parenthesis. The unmatched opening parenthesis is preserved.',
       'struck_map','text not on the page','text not on page',change_H=True)
change('canceled bottom map / terminal dot',
       r'\deleted{$X_k\longrightarrow X_{\unsure{j}}$}',
       r'\struck{$(X_k\to X)$}',struck_map,
       'A distinct detached dot follows the canceled target X on the main row. A separate low oblique tick below the target does not securely identify its subscript and remains covered by C’s doubtful j.',
       'struck_map','omission','omissions',change_C=True,change_H=True)
change('bottom pair expression / headless connector',
       pair_map,r"$(X_k,X_{k'})\to(X_j,X_{j'})$",pair_map,
       'The connector is one short horizontal stroke with a blunt right termination and no oblique arrowhead strokes. The two ordered pairs and their primes are legible.',
       'pair_map','misread symbol or index','symbols and indices',change_H=True,
       consequential='The manuscript’s headless stroke is retained rather than supplied with a direction.')
change('bottom-left marginal number / 28',r'\margin{28}','[absent]',r'\margin{28}',
       'A two-part 2 followed by a double-loop 8 is written in thin lighter ink at the bottom left. Its hand is uncertain and is not identified as the author’s own foliation.',
       'folio','omission','omissions',change_H=True)

marks = [
 dict(mark=r'\unsure{\downarrow|\geq}',context="first diagram: j′ above k′, left vertical relation",decision='other',reading=r'\rotatebox{90}{$\leq$}',evidence='Two branches form a vertical order sign with the extra parallel stroke on the right; no arrow shaft and head are distinguished.',crop=crop('order_diagram'),box=boxes['order_diagram'],confidence='high'),
 dict(mark=r'\unsure{\downarrow|\geq}',context="first diagram: j above k, right vertical relation",decision='other',reading=r'\rotatebox{90}{$\leq$}',evidence='The right sign repeats the left sign’s two branches and extra right-hand stroke, and is rendered with the same rotation.',crop=crop('order_diagram'),box=boxes['order_diagram'],confidence='high'),
 dict(mark=r'\unsure{\sigma|F}',context=r'la forme $\mathcal P(\unsure{\sigma|F})$',decision='undecided',reading=r'\unsure{\sigma|F}',evidence='The argument is overtraced: an oval sigma-like component and F-like upright/top/middle strokes coexist. The clear marginal sigma is not sufficient to decide the underlying letter or sequence of writing.',crop=crop('power_set'),box=boxes['power_set'],confidence='low'),
 dict(mark=r"\unsure{k\ne k'}",context=r"alors \deleted{$\unsure{k\ne k'}$}",decision='undecided',reading=r"\unsure{k\ne k'}",evidence='The two k-like letter portions remain; cancellation obscures the relation and possible prime. No mathematical inference is used to settle them.',crop=crop('struck_set_formula'),box=boxes['struck_set_formula'],confidence='low'),
 dict(mark=r'\unsure{1^\circ|a)}',context=r"par l'hyp. $\unsure{1^\circ|a)}$",decision='other',reading=r'\unsure{1^\circ)|16)}',evidence='Leading 1 and closing parenthesis are legible. The intervening loop has a small upper tail compatible with either a degree mark or 6; a) does not fit the visible stem.',crop=crop('hypothesis_number'),box=boxes['hypothesis_number'],confidence='medium'),
 dict(mark=r'\unsure{j}',context=r'\deleted{$X_k\longrightarrow X_{\unsure{j}}$}',decision='undecided',reading=r'\unsure{j}',evidence='The target X is crossed; a detached low oblique tick is present below it, without a sufficiently clear full index to resolve j. The final dot on the main row is separate.',crop=crop('struck_map'),box=boxes['struck_map'],confidence='low'),
]

inventory = []
def item(ident,kind,position,first,hand='his hand'):
    inventory.append(dict(element=ident,kind=kind,position=position,first_words_or_objects=first,sheet_kind='text',hand=hand,transcribed='yes'))
item('029.E01','text','upper part / principal lines 1–5','structure locale de X_j le long d’un X_i; induced type I_ij and cubical corner of dimension n=card S')
item('029.E02','drawing','upper right beside lines 3–5','retraced corner axes, heavy interior diagonal, five hatch strokes, two irregular contours')
item('029.E03','text','middle part / principal lines 6–11','La … c) … que si j′ est un prédécesseur de j; existence and predecessor property of k′')
item('029.E04','deletion','principal line 6 after live La','condition')
item('029.E05','insertion','above principal line 6 after canceled condition','c)')
item('029.E06','text','end of principal line 9','underlined alors')
item('029.E07','diagram','left of principal lines 9–11','j′ ↔ j over k′ ↔ k; vertical order signs; two hooked arrows from i')
item('029.E08','text','principal lines 12–16','(Il suffit de voir que dans un ens. ordonné de la forme P(σ/F) …)')
item('029.E09','margin note','left margin level with principal lines 13–14','σ ens fini')
item('029.E10','deletion','principal line 16 after alors','doubtful k≠k′ canceled under zigzag')
item('029.E11','text','principal line 17','Ceci posé, considérons le diagramme')
item('029.E12','diagram','below principal line 17','square X_j′ to X_j, X_k′ to X_k; hooked horizontal and plain upward arrows')
item('029.E13','text','principal lines 18–20','où les flèches verticales, par l’hyp. 1°)/16), sont des plongements bordants …')
item('029.E14','insertion','above principal line 20 between voit and que','(par b,c), with curved placement leader')
item('029.E15','deletion','principal line 20 after que','(X_k → X_j? . with unmatched opening parenthesis and final dot')
item('029.E16','display','right side of principal line 20','(X_k,X_k′) – (X_j,X_j′) with headless connector')
item('029.E17','margin note','extreme bottom-left corner','28','uncertain; thin lighter ink distinct from principal text')

doubts = [
 dict(place='predecessor assertion / impliquent or implique',reading=r'\unsure{impliquent|implique}',alternatives='impliquent | implique; C reads impliquent, H marks implique uncertain',confidence='medium'),
 dict(place='power-set argument',reading=r'\mathcal P(\unsure{\sigma|F})',alternatives='σ | F; overtracing prevents a secure sequence or final form',confidence='low'),
 dict(place='canceled set calculation',reading=struck_set,alternatives='k≠k′ is only a provisional reading; relation and final prime remain hidden',confidence='low'),
 dict(place='hypothesis reference',reading=hypothesis,alternatives='1°) | 16); leading 1 and closing parenthesis are secure',confidence='medium'),
 dict(place='target subscript in canceled bottom map',reading=r'X_{\unsure{j}}',alternatives='j remains provisional; low detached tick insufficient to establish a complete index',confidence='low'),
]

notes = [
 'The page continues a statement that the local structure of X_j along X_i, with induced stratification of type I_ij, is cubical, with a corner model of dimension n=card S. This is a transcription of the claim, not a verification of the local model.',
 'It reports a predecessor/infimum assertion for j′, j, k and a common lower bound i, illustrated by a poset diagram. The adjoining power-set paragraph offers an intersection argument. Its mathematical validity was not independently re-proved in this reading.',
 'The visible membership sign in k∈j is retained even though subset membership is the more expected relation in the set calculation. The final sentence refers to vertical bordering embeddings and starts a pair expression; the headless connector is not supplied with an arrowhead.',
 'The verb after raised c) is still uncertain between impliquent and implique. Both readings remain in the transcription; no agreement correction has been made.',
 'The argument of P remains σ/F because the overtrace is unresolved. The legible marginal σ ens fini cannot establish which component is final or which was written first.',
 'The number after l’hyp. is narrowed to 1°)/16); both possibilities include the visible closing parenthesis. Neither the expected hypothesis nor the diagram is used to choose a numeral.',
 'The canceled bottom map starts with ( and has no visible closing mate; a separate final dot is retained. A low detached oblique mark below its target is inventoried through the unresolved j subscript and is not silently discarded.',
 'Five hatch strokes were counted in the upper-right drawing. The two contour traces, small interruption/notch, retraced corner axes and heavy diagonal are reproduced approximately in TikZ, with their topological placement preserved and no point markers added.',
 'The source has comma plus two points before the closing parenthesis of the set argument. The abbreviation exist ends at t with no full stop. Capital Inf in the earlier formula and lower-case inf in prose are deliberately distinguished.',
 'The bottom-left 28 is in thin lighter ink; attribution to the principal hand is uncertain. It is encoded as a margin number rather than asserted to be the author’s own foliation. Scan number 29 is editorial metadata.',
 'Line count 20 refers to principal text baselines, excluding diagram rows, the separate drawing, raised insertions and marginal notes. Every such excluded element is listed separately in the inventory.',
 'H’s opening bibliographical note, prose drawing comments, and final section heading are editorial material. The drawing comments inform the collation but are not copied into the manuscript transcription. Macro-only differences in card/P typography, brace commands, and emphasis conventions are not treated as independent misreadings.',
 'All seventeen first-pass crops were viewed. The four final crops were reissued after a combined tool output was truncated before usable image content reached the reader. No OCR, external research, TeX compilation or other page was used.',
]

check_events = [
 dict(statement_id='150.029.N1',type='carried as background without fault found',outcome='Read the reported cubical local-model claim and its dimension expression against both witnesses and the manuscript; no independent local-model proof was undertaken.'),
 dict(statement_id='150.029.N2',type='carried as background without fault found',outcome='Read the predecessor/infimum assertion and the power-set argument. Recorded literal k∈j and unresolved P-argument/deletion; no proof or mathematical correction is claimed.'),
 dict(statement_id='150.029.N3',type='carried as background without fault found',outcome='Read the square, bordering-embedding sentence, inserted reference and unfinished pair expression. The hypothesis number remains uncertain and no implication was independently checked.'),
]

notation = [
 dict(form=r'\operatorname{Inf}',meaning_or_shape='Capital initial I in the displayed infimum expression; distinguish from small dotted i in prose inf.',places='predecessor formula; later les inf exist'),
 dict(form=r'\rotatebox{90}{$\leq$}',meaning_or_shape='A vertical order sign whose angle points toward the lower node and whose separate parallel stroke lies to the right.',places='both vertical relations in the first diagram'),
 dict(form=r'\hookrightarrow',meaning_or_shape='Hooked tail and single terminal arrowhead; ordinary labels are not point markers.',places='two oblique arrows from i in first diagram; two horizontal arrows in second square'),
 dict(form=r'j,j\prime',meaning_or_shape='Lower-case j has a variable pointed/looped head and hooked foot, sometimes broad; isolated breadth alone does not establish capital J.',places='set calculation and final pair expression'),
 dict(form=r'\mathcal P(\unsure{\sigma|F})',meaning_or_shape='Calligraphic handwritten P with overtraced, unresolved argument; no claim of a distinct mathfrak versus mathcal alphabet.',places='parenthetical set argument'),
 dict(form=r'\mathbin{-}',meaning_or_shape='Short headless horizontal connector, with blunt right end.',places='last pair expression'),
]

abbreviations = [
 dict(form='ens.',expansion='ensemble'),
 dict(form='ens',expansion='ensemble; marginal form has no stop'),
 dict(form='exist',expansion='existent; manuscript stops at t without a stop'),
 dict(form='préd',expansion='prédécesseur; diagram label has no stop'),
 dict(form='hyp.',expansion='hypothèse'),
 dict(form='card',expansion='cardinal'),
 dict(form='Inf / inf',expansion='infimum; source distinguishes capitalization'),
]

hand_log = [
 dict(habit='A cancellation may pass through one word while adjacent live writing is raised above it.',places='La [condition] c)',consistent='Only condition is crossed; La and raised c) remain live.',witness_errors='C crosses c) with condition; H crosses La with condition; both lose the raised placement of c).'),
 dict(habit='Capital I in a formula is taller and horizontally finished, whereas prose inf begins with a short dotted i.',places='k′=Inf(k,j′); les inf exist',consistent='The two different initial forms are visible on the same page.',witness_errors='H regularizes the earlier capital Inf to lowercase inf; both expand exist to existent.'),
 dict(habit='Vertical order signs have a long branch, shorter return and a separate right-hand parallel stroke.',places='j′/k′ and j/k in the first diagram',consistent='Both instances agree in orientation.',witness_errors='C leaves arrow/order alternatives; H prints ordinary ≥ in its code despite its descriptive note about a turned sign.'),
 dict(habit='Hooked tails are small curved returns that can be missed when close to a node.',places='both oblique arrows from i and both horizontal arrows in the lower square',consistent='Four visible hooked tails; vertical square arrows are plain.',witness_errors='H omits all four hooks; C preserves them.'),
 dict(habit='Lower-case j varies in head and foot width; the larger return does not by itself prove capitalization.',places='repeated set-calculation j and final pair j subscripts',consistent='Broad final returns are compatible with otherwise lowercase uses; no absolute case rule is claimed.',witness_errors='H capitalizes all set-calculation J forms; C retains lowercase.'),
 dict(habit='A dense overtrace can preserve mutually incompatible apparent letter components.',places='argument of handwritten P',consistent='Only one such σ/F overlap on this page; sequence unresolved.',witness_errors='H fixes F while C’s uncertainty remains warranted.'),
 dict(habit='Tiny final punctuation must be counted separately from closing curved marks.',places='two points at end of set argument; dot after canceled map; missing stop after opening dimension parenthesis',consistent='Three distinct punctuation checks, each retained literally.',witness_errors='Both witnesses supply a third ellipsis point and omit the map’s dot; H supplies a full stop after the dimension parenthesis and a closing parenthesis to the canceled map.'),
]

second_boxes = []
def audit(kind, coords, reading, reason):
    second_boxes.append(dict(box=f'b{len(second_boxes)+1:02d}',kind=kind,coords=coords,reading=reading,reason=reason))

audit('C/H word difference',boxes['cubique'],r"est ``cubique'' (coin de cube de dimension $n=\operatorname{card}S$)",
      'Quotation and punctuation differences surrounding a common word; the whole opening model phrase is supplied without explanatory additions.')
audit('drawing',boxes['corner_drawing'],figure,'Drawing correction: count and disposition of five hatch strokes, contours, axes and diagonal.')
audit('insertion; struck passage; C/H word difference; low-confidence departure',boxes['condition_verb'],condition,
      'Live La, canceled condition, raised live c), and the genuine C/H impliquent/implique word difference. Added verb uncertainty remains explicit.')
audit('doubt formula; diagram',boxes['order_diagram'],order_diagram,
      'Whole first diagram, including both formulas containing C doubts, horizontal links, labels and oblique hooked arrows.')
audit('C/H symbol difference',[783,850,1654,961],r"$k'=\operatorname{Inf}(k,j')$ existe, et $k'$ est",
      'Complete infimum formula with capital Inf, compared with H’s lowercase inf.')
audit('doubt formula',boxes['power_set'],power,'Whole formula containing unresolved C and proposed σ/F doubt.')
audit('margin note; C/H word difference',boxes['finite_margin'],r'\margin{$\sigma$ ens fini}',
      'Entire marginal note, including the genuine ens fini versus sur F difference.')
audit('C/H word difference',boxes['inf_existent'],'les inf exist','Both witnesses expand the manuscript’s terminal word; retain the actual abbreviated form without stop.')
audit('C/H word difference',boxes['intersection_words'],"(c'est l'intersection)",'H omits the genuine c’est words.')
audit('C/H symbol difference',[332,1335,1665,1453],set_line,'Whole first set-calculation line preserves lowercase j and literal membership sign.')
audit('struck passage; doubt formula; low-confidence departure',[332,1452,1665,1560],set_end,
      'Whole second set-calculation line includes the canceled doubtful formula, final broad-form lower-case j, and comma plus two points.')
audit('diagram',boxes['square_diagram'],square,'All four nodes and arrows, with both horizontal hooks, for diagram verification.')
audit('handwritten number; doubt formula; low-confidence departure',boxes['hypothesis_number'],hypothesis,
      'Complete doubtful reference, including leading 1, ambiguous ordinal mark or 6, and closing parenthesis.')
audit('insertion',boxes['inserted_bc'],r'voit \inserted{(par b,c)} que','Entire inserted phrase and its attachment between voit and que.')
audit('struck passage; doubt formula',boxes['struck_map'],struck_map,
      'Whole canceled map including the C/proposed index doubt, opening parenthesis, unmatched closing side, final dot and low detached tick.')
audit('C/H symbol difference',boxes['pair_map'],pair_map,'Whole pair expression with literal headless connector.')
audit('margin note; handwritten number',boxes['folio'],r'\margin{28}','Entire marginal 28; attribution of the thin lighter hand remains uncertain.')

result = dict(scan=29,reader='reader_c',line_count=20,changes=changes,marks=marks,
              inventory=inventory,doubts=doubts,notes=notes,check_events=check_events,
              notation=notation,abbreviations=abbreviations,hand_log=hand_log,
              second_boxes=second_boxes)

(root/'reader_returns'/'150_scan029.tex').write_text(page)
(root/'reader_returns'/'150_scan029.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

print(json.dumps({'tex':str(root/'reader_returns'/'150_scan029.tex'),
                  'json':str(root/'reader_returns'/'150_scan029.json'),
                  'changes':len(changes),'marks':len(marks),'inventory':len(inventory),
                  'doubts':len(doubts),'second_boxes':len(second_boxes),'crops':len(boxes)},indent=2))
