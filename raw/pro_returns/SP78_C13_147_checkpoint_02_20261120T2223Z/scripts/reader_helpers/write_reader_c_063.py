from pathlib import Path
import json

ROOT = Path('/workspace/scratch/ea90d891106a')
WORK = ROOT / 'SP78_C13_147_work'
OUT = WORK / 'reader_returns/147_scan063'
OUT.mkdir(parents=True, exist_ok=True)

boxes = {
    1: [30, 523, 433, 1151],
    2: [426, 420, 1251, 645],
    3: [429, 629, 1666, 760],
    4: [430, 760, 1669, 890],
    5: [270, 912, 1593, 1159],
    6: [271, 1249, 791, 1380],
    7: [281, 1384, 1379, 1643],
    8: [1017, 1742, 1656, 1865],
    9: [276, 1858, 1513, 2028],
    10: [288, 2018, 1668, 2237],
    11: [309, 2236, 1660, 2351],
    12: [33, 2280, 107, 2340],
    13: [1178, 224, 1509, 324],
    14: [283, 325, 753, 413],
    15: [260, 15, 1680, 228],
}

opening = r"\chi_!(\widehat M^{\mathrm{an}}_{0,4})=\underbrace{\chi_!(U^{\mathrm{an}}_{0,3},\mathfrak S_4)}_{-1/24}+\underbrace{\chi_!(\{0,1,\infty\},\mathfrak S_4)}_{1/8}=\frac1{12}."
margin = r"\margin{valable au dessus de $\mathbb Z[\frac16]$ --- \unsure{pour dispenser|pour me dispenser} de faire le calcul plus fin au dessus de $\operatorname{Spec}\mathbb Z\ldots$}"
row1 = r"[M^!_{0,4}]&=[U_{\unsure{0,4|3,4}}]=\underbrace{T(1)}_{\substack{\text{``Tate''}\simeq[\mathbb E^1]\\(\text{d'augmentation }1)}}-2"
row2 = r"[M_{0,4}]&=\deleted{\unsure{\tfrac1{24}(T(1)-2)}}\frac14(T(1)-2)+\frac1{12}+\frac18=\frac14(T(1)-1)-\frac1{24}"
row3 = r"[\widehat M_{0,4}]&=[M_{0,4}]+\frac18=\deleted{\unsure{\tfrac1{24}(T(1)+1)}}=\frac14(T(1)-1)+\frac1{12}"
augment = r"Ces trois quantités sont d'augmentation égale resp\textsuperscript{t} : $-1,-1/24,1/12$."
heading = r"$2^\circ)$ \uline{Cas de} $\widehat M_{1,1}$."
diagram = r"""\diagram{\begin{tikzpicture}[x=1cm,y=1cm,line width=.55pt]
\node at (-1.35,.55) {$(77)$};
\draw (0,1.15)--(6,1.15);
\draw (3,1.8)--(3,-1.05);
\node at (1.35,1.5) {$\text{codim }0$};
\node at (4.65,1.5) {$\text{codim }1$};
\fill (1.25,0) circle (1.5pt);
\node at (1.25,.4) {$1$};
\node at (1.25,-.45) {$\underline1$};
\draw[->] (2.55,.08)--(3.55,.08);
\node at (2.85,.32) {$1$};
\draw (5,.1)..controls(4.72,.82)and(4.12,.88)..(4.05,-.05)..controls(3.98,-.42)and(4.55,-.18)..(5,.1);
\fill (5,.1) circle (2pt);
\node[above right] at (5,.1) {$1$};
\end{tikzpicture}}"""
lead = r"On a un morphisme (\uline{au dessus de} $\mathbb Z[\frac12]$)"
hat = r"\overset{\deleted{\unsure{\wedge}}}{M}"
morphism = r"(78)\qquad " + hat + r"_{1,1}\longrightarrow" + hat + r"'_{1,4}\overset{\mathrm{déf}}{=}(" + hat + r"^!_{1,4},\mathfrak S_3)"
gerbe = r"qui fait de $" + hat + r"_{1,1}$ une gerbe (de groupe constant $\{\pm1\}$) au dessus de $" + hat + r"'_{1,4}$ (en ca. $\neq2$)"
tail = r"\deleted{\unsure{=\tfrac1{12}[\mathbb E^1]-\tfrac14}}"
insertion = r"\underset{\inserted{T(1)}}{" + tail + "}"
bottom = r"\text{d'où}\qquad [M_{1,1}]=\frac12[U_{0,3},\mathfrak S_3]=\unsure{2|\frac12}[M_{0,4}]" + insertion

proposed = '\n'.join([
    r'\scanpage{63}', r'\[', opening, r'\]',
    "De façon plus fine, dans un ``groupe de Grothendieck'' convenable, on aura",
    margin, r'\[', r'79\quad\left\{\begin{aligned}', row1 + r'\\', row2 + r'\\', row3,
    r'\end{aligned}\right.', r'\]', augment, '', heading, diagram,
    "Il y a exactement un point à l'infini.", '', lead, r'\[', morphism, r'\]', gerbe,
    r'\[', bottom, r'\]', r'\margin{62}', '',
])

changes = []
def change(place, C, H, final, evidence, crop, confidence='high', against_C=False,
           against_H=True, kind='other', marked_in_H=False, error_sheet_kind='other',
           consequential=False):
    changes.append({
        'id': f'063-{len(changes)+1:02d}', 'place': place, 'C': C, 'H': H,
        'final': final, 'evidence': evidence,
        'crop': f'147_scan063_place{crop:02d}.png', 'box': boxes[crop],
        'confidence': confidence, 'against_C': against_C, 'against_H': against_H,
        'kind': kind, 'marked_in_H': marked_in_H,
        'error_sheet_kind': error_sheet_kind, 'consequential': consequential,
    })

change('Introductory prose, opening quotation before groupe', '``', r'\og', '``',
       'The raised dark pair before the g is a compact double quotation stroke, not two angle strokes of a guillemet.', 13)
change('Introductory prose, closing quotation after Grothendieck', "''", r'\fg{}', "''",
       'Two separate short elevated vertical strokes follow the terminal k; neither has a guillemet angle.', 14)
change('Sloping left margin, both Z glyphs', r'\mathbf Z[\frac16]; \operatorname{Spec}\mathbf Z',
       r'\mathbb Z[\frac16]; \mathbb Z', r'\mathbb Z[\frac16]; \operatorname{Spec}\mathbb Z',
       'The first Z has two separated diagonals enclosing a narrow white strip; the lower Z after Spec repeats the doubled diagonal. This is an alphabet distinction, not just a heavier stroke.', 1,
       against_C=True, against_H=False, kind='misread symbol or index', error_sheet_kind='symbols and indices')
change('Sloping left margin, phrase after dash (M1039)', r'\unsure{je me dispense|pour dispenser}',
       r'\ill{} \ill{}', r'\unsure{pour dispenser|pour me dispenser}',
       'The initial letter has a long descending p stroke comparable with plus below. The compressed low humps that follow support pour; they do not separate a possible me securely. The following d-loop and dispenser body are present, but the phrase remains uncertain.', 1,
       confidence='low', against_C=True, kind=r'readable ink left as \ill{}', marked_in_H=True,
       error_sheet_kind='readable ink left as illegible')
change('Sloping left margin, continuation and final base',
       r'de faire le calcul plus fin au dessus de $\operatorname{Spec}\mathbf Z\ldots$',
       r'faire le calcul \ill{} au-dessus de $\mathbb Z$…',
       r'de faire le calcul plus fin au dessus de $\operatorname{Spec}\mathbb Z\ldots$',
       'The next row begins de before the tall f of faire. Below it, plus has a deep p and fin a long f. The bottom row has the tall S and descending p of Spec before Z and three dots. There is a word space, not a hyphen, between au and dessus.', 1,
       kind='omission', marked_in_H=True, error_sheet_kind='omissions')
change('Display 79, number and left grouping brace', r'79\quad\left\{',
       r'\marginal{\uncertain{79}}; no brace in the display', r'79\quad\left\{',
       'The upright 79 sits immediately to the left of the tall brace. Its baseline and orientation differ from the sloping marginal note; the brace groups the three displayed rows.', 1,
       kind='insertion or placement', marked_in_H=True, error_sheet_kind='insertions put in wrong place')
change('Display 79, first-row U subscript (M1040)', r'\unsure{3,4|0,4|0,3}', r'0,3',
       r'\unsure{0,4|3,4}',
       'The final digit has an angular upper hook and a single descending upright, the local form of 4 rather than two rounded lobes of 3. The first dark oval and following descending comma-like stroke are crowded: 0,4 is preferred, while 3,4 remains possible.', 2,
       confidence='low', against_C=True, kind='misread symbol or index', error_sheet_kind='symbols and indices', consequential=True)
change('Display 79, Tate annotation, E alphabet', r'\mathbf E^1', r'\mathbb E^1', r'\mathbb E^1',
       'The left of E consists of two separated vertical strokes, with the horizontal arms attached; it is visibly double-struck.', 2,
       against_C=True, against_H=False, kind='misread symbol or index', error_sheet_kind='symbols and indices')
change('Display 79, quotation marks around Tate', r'\text{``Tate\'\'}', r'\text{Tate}', r'\text{``Tate\'\'}',
       'There are two short elevated strokes before T and two after the final letter, on the annotation baseline below the brace.', 2,
       kind='omission', error_sheet_kind='omissions')
change('Display 79, second line of the T(1) annotation', r"(\text{d'augmentation }1)",
       r"\note{sous Tate : (d'\uncertain{augmentation} 1)}", r"(\text{d'augmentation }1)",
       'A separate parenthesized line is directly below Tate: d-apostrophe, the long descending g of augmentation, and a final upright 1. It is live manuscript annotation attached to T(1), not an editorial paragraph after the display.', 2,
       kind='insertion or placement', marked_in_H=True, error_sheet_kind='insertions put in wrong place')
change('Display 79, canceled trial in row 2', r'\deleted{\unsure{\tfrac1{24}(T(1)-2)}}',
       r'\note{un premier essai de calcul est raturé avant le résultat, illisible}',
       r'\deleted{\unsure{\tfrac1{24}(T(1)-2)}}',
       'Dense diagonal strokes occupy the interval after the first equals and before the live overworked 1/4. A fraction bar and several underlying curves survive, but they do not expose every numeral and letter; C’s entire tentative trial is kept under a doubt, not resolved.', 3,
       confidence='low', kind='deletion state', marked_in_H=True, error_sheet_kind='struck text')
change('Display 79, canceled trial and following equals in row 3',
       r'=\deleted{\unsure{\tfrac1{24}(T(1)+1)}}=',
       r'=; canceled trial described only as illisible in an editorial note',
       r'=\deleted{\unsure{\tfrac1{24}(T(1)+1)}}=',
       'Diagonal cancellation crosses a fraction with visible lower 24 and the parenthesized expression. The internal signs remain partly hidden. A separate live equals is visible to the right of the cancellation before the final 1/4.', 4,
       confidence='low', kind='deletion state', marked_in_H=True, error_sheet_kind='struck text')
change('Display 79, end of row 3', r'+\frac1{12}.', r'+\frac1{12}', r'+\frac1{12}',
       'The final 12 is followed by blank paper, with no detached dot. Parent review of the full scan also confirmed no period at this position; the opening equation has a different, clearly visible final dot.', 4,
       against_C=True, against_H=False, kind='text not on the page', error_sheet_kind='text not on page')
change('Two prose lines below display 79',
       r"Ces trois quantités sont d'augmentation égale respt à $-1,-1/24,1/12$.",
       r'On trouve \ill{} ces trois quantités \uncertain{à des} dénominateurs \uncertain{près} : $-1,-\frac1{24},\frac1{12}$.',
       augment,
       'The first line starts directly with Ces trois quantités, followed by sont and d’augmentation; there is no preceding On trouve. The next line starts égale and the compressed abbreviation resp with a raised final t. Two detached dots stand vertically after it, with no a-body, giving a colon. The long horizontal stroke under the start of augmentation is continuous with the g-descender, not a separate underline.', 5,
       against_C=True, kind='misread word', marked_in_H=True, error_sheet_kind='words', consequential=True)
change('Section heading, Cas de', r'\uline{Cas de}', r'\emph{Cas des}', r'\uline{Cas de}',
       'After the looped d, the e ends in the same descending exit hook as de elsewhere on this page. No additional terminal s-body is separated. A straight underline spans Cas de.', 6,
       kind='misread word', error_sheet_kind='words')
change('Diagram 77, ruled layout and labels',
       r'\begin{array}{c|c}... point and \xrightarrow{1} & loop ...\end{array}; lower point label \underline1',
       r'\begin{array}{c|c}...\underset{1}{\overset{1}{\bullet}}\xrightarrow{1}&\text{(boucle)}\overset1\bullet...\end{array}',
       diagram,
       'The arrow shaft visibly crosses the vertical divider and ends to its right; both witness arrays put the arrow in the left cell. The left point has a 1 above and an overworked, long-based lower 1, retained as underlined. The upper and right 1 bases resemble numeral feet rather than separate underlines. The right loop closes at its filled right-hand vertex. H’s separate drawing file was not supplied or assessed; the comparison concerns its provided array and label text.', 7,
       against_C=True, kind='drawing or diagram', error_sheet_kind='drawings and diagrams', consequential=True)
change('Morphism lead-in, Z alphabet', r'\mathbf Z[\frac12]', r'\mathbb Z[\frac12]', r'\mathbb Z[\frac12]',
       'The Z has two separated diagonal strokes joined by top and bottom strokes, leaving a narrow white strip.', 8,
       against_C=True, against_H=False, kind='misread symbol or index', error_sheet_kind='symbols and indices')
change('Morphism lead-in, au dessus', r'\uline{au dessus de}', r'\emph{au-dessus de}', r'\uline{au dessus de}',
       'There is a clear word space between au and the looped d of dessus, with no hyphen. The single long stroke lies beneath the full phrase.', 8,
       kind='abbreviation expanded or spelling modernised', error_sheet_kind='abbreviations expanded spelling modernised')
change('Display 78, all three canceled accents',
       hat + r'_{1,1}\longrightarrow' + hat + r"'_{1,4}=(" + hat + r'^!_{1,4},\mathfrak S_3)',
       r"\widehat M_{1,1}\longrightarrow\widehat M'_{1,4}=(\widehat M^!_{1,4},\mathfrak S_3)",
       morphism,
       'Above each of the three M letters is a compact group of multiple dark oblique strokes crossing the former accent. These are cancellation clusters, unlike the clean angular live hat in the section heading. The underlying wedge shapes remain doubtful. The target indices have straight 1s and angular 4s and stay 1,4.', 9,
       kind='deletion state', error_sheet_kind='struck text', consequential=True)
change('Display 78, definition label', r'\mathrm{déf}', r'\mathrm{def}', r'\mathrm{déf}',
       'A short separate raised stroke is present over the e between the d-loop and the tall descending f.', 9,
       kind='misread word', error_sheet_kind='words')
change('Gerbe prose, both canceled accents',
       hat + r'_{1,1}; ' + hat + r"'_{1,4}", r"\widehat M_{1,1};\widehat M'_{1,4}",
       hat + r'_{1,1}; ' + hat + r"'_{1,4}",
       'Both accents are filled and overcrossed by additional dark strokes. The M bodies and their indices remain live, as does the prime on the right-hand M. C’s original wedge readings stay doubtful.', 10,
       kind='deletion state', error_sheet_kind='struck text', consequential=True)
change('Gerbe prose, group description', r'constant $\{\pm1\}$', r'\uncertain{$\{\pm1\}$}', r'constant $\{\pm1\}$',
       'The second physical line begins with constant: initial c, a tall t in the middle, and the final t immediately before the opening brace. The ± has a vertical stroke through its upper bar and a second lower bar; the 1 is upright.', 10,
       kind='omission', marked_in_H=True, error_sheet_kind='omissions', consequential=True)
change('Gerbe prose, au dessus', 'au dessus de', 'au-dessus de', 'au dessus de',
       'The end of au and the looped initial d are separated by ordinary white space; there is no intervening hyphen.', 10,
       kind='abbreviation expanded or spelling modernised', error_sheet_kind='abbreviations expanded spelling modernised')
change('Gerbe prose, characteristic abbreviation', r'en ca. $\neq2$', r'\uncertain{en car.} $\neq2$', r'en ca. $\neq2$',
       'The rounded c and small a are followed directly by a dark dot. There is no separate r-stroke between the a and that dot. The crossed equals and the 2 remain distinct to the right.', 10,
       kind='abbreviation expanded or spelling modernised', marked_in_H=True, error_sheet_kind='abbreviations expanded spelling modernised')
change('End of gerbe prose, punctuation before the next line d’où', r'(en ca. $\neq2$)',
       r'(\uncertain{en car.} $\neq2$),', r'(en ca. $\neq2$)',
       'The closing parenthesis has blank paper after its lower end; no detached comma is present. D’où starts the next physical line at the left of the final formula.', 10,
       kind='text not on the page', error_sheet_kind='text not on page')
change('Final line, coefficient of [M_{0,4}]', r'2', r'\tfrac12', r'\unsure{2|\frac12}',
       'The sign has a large curved upper stroke and a looped lower return, supporting an overworked 2, but an internal horizontal stroke and stacked contour also permit 1/2. The crop does not settle the layering, so the distinction remains explicit.', 11,
       confidence='low', kind='misread symbol or index', error_sheet_kind='symbols and indices', consequential=True)
change('Final line, canceled calculation and E alphabet',
       r'\deleted{\unsure{=\tfrac1{12}[\mathbf E^1]-\tfrac14}}',
       r'\struck{\ldots}; editorial note says one can make out [\mathbb E^1]', tail,
       'Diagonal zigzags cross the whole tail after [M_{0,4}]. A fraction and bracketed E with two parallel verticals and superscript 1 survive among the strokes; the last fraction is not fully exposed. The full calculation stays tentative, while the visible double-stroked alphabet is preserved.', 11,
       confidence='low', against_C=True, kind='deletion state', marked_in_H=True, error_sheet_kind='struck text', consequential=True)
change('Final line, inserted T(1)', r'...\deleted{...}\inserted{T(1)}',
       r'\note{la fin de la ligne, où l’on devine [\mathbb E^1] et T(1), est raturée}', insertion,
       'The clear T(1) is on a separate lower baseline, beneath the canceled tail near its E term. No cancellation passes through T(1) itself. Underset placement preserves this relation without claiming an otherwise unseen replacement arrow or precise scope beyond the tail.', 11,
       against_C=True, kind='insertion or placement', marked_in_H=True, error_sheet_kind='insertions put in wrong place')
change('Lower-left pencil foliation', r'\margin{62}', '(nothing)', r'\margin{62}',
       'The lighter separate hand has a tall looped 6 followed by a curved 2 with a horizontal foot. It is retained as margin foliation rather than an authorial manuscript page number.', 12,
       kind='omission', error_sheet_kind='omissions')

# Correct literal quotation snippets in the two JSON fields without altering the manuscript.
changes[8]['C'] = r"\text{``Tate''}"
changes[8]['final'] = r"\text{``Tate''}"

decisions = [
    {'id':'M1039','cote':147,'scan':63,'decision':'undecided',
     'reading':r'\unsure{pour dispenser|pour me dispenser}',
     'ink':'Initial long p-descender rules against je. The compressed humps before dispenser do not isolate a possible me; the two surviving readings remain explicit.',
     'crop':'147_scan063_place01.png (30,523,433,1151); rotated -43 degrees', 'confidence':'low'},
    {'id':'M1040','cote':147,'scan':63,'decision':'undecided',
     'reading':r'\unsure{0,4|3,4}',
     'ink':'Final angular hook plus upright identifies 4. The preceding crowded oval and descending comma-like stroke favor 0,4 but do not exclude 3,4. No normalization to U_{0,3}.',
     'crop':'147_scan063_place02.png (426,420,1251,645)', 'confidence':'low'},
]

inventory = []
def inv(kind, position, first, hand='his hand'):
    inventory.append({'scan':63,'sheet_kind':'text','hand':hand,'element':f'{len(inventory)+1:02d}',
                      'kind':kind,'position':position,'first_words_or_objects':first,'transcribed':'yes'})
inv('display','top, first two written bands','chi_! of hat M_{0,4} an; two underbraces, values -1/24 and 1/8; final 1/12 and period')
inv('text','two introductory prose lines','De façon plus fine, dans un ``groupe de Grothendieck\'\' convenable, on aura')
inv('margin note','six slanting lines at upper left beside 79','valable au dessus de Z[1/6] — pour dispenser|pour me dispenser ... Spec Z...')
inv('display','upper middle, braced three-row group labeled 79','[M!_{0,4}], [M_{0,4}], [hat M_{0,4}]')
inv('text','two annotation bands under T(1) in first row of 79','``Tate\'\' ≃ [double-struck E^1]; (d’augmentation 1)')
inv('deletion','second row of 79, between equals and live overworked 1/4','tentative 1/24(T(1)-2)')
inv('deletion','third row of 79, before a further live equals','tentative 1/24(T(1)+1)')
inv('text','two lines below 79','Ces trois quantités sont d’augmentation égale resp raised t : -1,-1/24,1/12.')
inv('text','middle heading','2°) underlined Cas de; hat M_{1,1}.')
inv('diagram','middle, (77), two columns and horizontal rule','codim 0/codim 1; isolated labeled point; arrow 1 across divider; closed loop at filled labeled vertex')
inv('text','line below diagram','Il y a exactement un point à l’infini.')
inv('text','lower lead-in','On a un morphisme (underlined au dessus de Z[1/2])')
inv('display','lower, (78), morphism and definition','M_{1,1} to M’_{1,4} = déf (M!_{1,4}, S_3)')
inv('deletion','above three M letters in 78 and two M letters in following prose','five canceled, still doubtful wedge accents')
inv('text','two lines following 78','qui fait de M_{1,1} une gerbe (de groupe constant {±1}) au dessus de M’_{1,4} (en ca. ≠2)')
inv('display','last main baseline','d’où [M_{1,1}] = 1/2[U_{0,3},S_3] = doubtful 2|1/2[M_{0,4}]')
inv('deletion','right end of last main baseline','tentative =1/12[double-struck E^1]-1/4')
inv('insertion','separate lower baseline below canceled tail','T(1)')
inv('margin note','bottom left','62','lighter pencil hand, not confidently attributed')

doubts = [
    {'place':'M1039, left margin after dash','reading':'pour dispenser','alternatives':'pour me dispenser','confidence':'low',
     'reason':'The p is visible, but the compact joining humps leave a possible me inseparable. Je me dispense is not supported by the long initial p.'},
    {'place':'M1040, U subscript in row 1 of 79','reading':'0,4','alternatives':'3,4','confidence':'low',
     'reason':'The last 4 is angular and distinct; the first oval/comma group is crowded. The page’s other U_{0,3} occurrences do not license normalizing this index.'},
    {'place':'79 row 2, canceled trial','reading':r'\deleted{\unsure{\tfrac1{24}(T(1)-2)}}','alternatives':'Underlying fraction and expression not wholly recovered','confidence':'low',
     'reason':'Dense diagonal strokes obscure several characters; this is an unindexed C doubt and is not resolved.'},
    {'place':'79 row 3, canceled trial','reading':r'\deleted{\unsure{\tfrac1{24}(T(1)+1)}}','alternatives':'Underlying expression not wholly recovered','confidence':'low',
     'reason':'24 and some T/parenthesis strokes survive, but the crossing prevents an every-character reading. Unindexed C doubt retained.'},
    {'place':'78, three canceled accents above M','reading':r'\deleted{\unsure{\wedge}} at all three places','alternatives':'Exact original accent under hatching is not certain','confidence':'low',
     'reason':'Cancellation is evident; the former angular mark is incompletely exposed. All three doubtful wedges are preserved.'},
    {'place':'Gerbe prose, two canceled accents above M','reading':r'\deleted{\unsure{\wedge}} at both places','alternatives':'Exact original accent under hatching is not certain','confidence':'low',
     'reason':'Each dark accent cluster is overcrossed, but the original wedge cannot be fully recovered. Both unindexed C doubts remain.'},
    {'place':'Final coefficient of [M_{0,4}]','reading':r'\unsure{2|\frac12}','alternatives':'2 or 1/2; overwritten layering not resolved','confidence':'low',
     'reason':'The large looped contour favors 2 while the internal bar admits a stacked fraction; mathematical expectation does not decide the ink.'},
    {'place':'Final canceled tail','reading':tail,'alternatives':'Some fraction/sign strokes remain physically obscured','confidence':'low',
     'reason':'The double-stroked E is identifiable but the entire canceled calculation is not exposed. The unindexed C doubt remains.'},
    {'place':'Attachment of the live lower T(1)','reading':insertion,'alternatives':'Precise intended replacement scope within the canceled tail is not marked','confidence':'medium',
     'reason':'Physical position beneath the tail near E^1 is clear; no connector specifies a narrower semantic scope.'},
]

notes = [
    '147-063-N1: The manuscript gives chi_!(hat M_{0,4}^{an}) as the sum of two terms annotated -1/24 and 1/8, with result 1/12. Exact rational arithmetic in this run verified only -1/24+1/8=1/12, not the geometric identifications of the two terms.',
    '147-063-N2: In a claimed suitable Grothendieck group, display 79 writes the three classes as expressions in T(1), annotating T(1) as “Tate” ≃ [double-struck E^1] of augmentation 1. Exact Fraction arithmetic checked the two live affine expressions in rows 2 and 3 and the stated augmentations -1,-1/24,1/12. It did not prove that these expressions represent the manuscript’s moduli objects. The first U index is kept as 0,4|3,4, although U_{0,3} appears elsewhere on this same page.',
    '147-063-N3: The sloping marginal note limits the preceding calculation to above Z[1/6] and mentions avoiding a finer calculation above Spec Z. Its purpose phrase remains pour dispenser|pour me dispenser. The 79 belongs to the upright braced display, not to the marginal sentence.',
    '147-063-N4: The manuscript begins the case of hat M_{1,1}, draws a codimension-0 labeled point and a codimension-1 loop, and states that there is exactly one point at infinity. This geometric claim was read, not independently proved in this run. The arrow labeled 1 crosses the vertical rule; its two-dimensional placement is preserved in the complete TikZ diagram.',
    '147-063-N5: Over Z[1/2], the manuscript writes the morphism M_{1,1} to M’_{1,4} = déf (M!_{1,4},S_3), then calls it a gerbe with constant group {±1} in ca. ≠2. The three literal target indices 1,4 are retained even though H’s editorial note suggests 0,4. Five formerly hatted M letters are visibly canceled at the accent only. No proof of this morphism/gerbe assertion was performed.',
    '147-063-N6: The last line relates [M_{1,1}] to 1/2[U_{0,3},S_3] and then to a coefficient 2|1/2 times [M_{0,4}]. The coefficient remains unresolved from the overworked ink. A further calculation is canceled, and T(1) is live beneath its tail near E^1; the exact intended replacement scope is not inferred. No mathematical consistency argument was used to choose the coefficient or repair the literal indices.',
    '147-063-N7: Reading coverage: scan layout once, each native half once, then 15 unique crop places viewed; crop01 rotated -43 degrees, the others unrotated. Physical_lines_read=31 counts 24 main-body written bands plus six marginal lines and one pencil foliation: opening formula and underbrace labels (2), introduction (2), display79 including two annotation bands (5), augmentation prose (2), heading (1), diagram header/upper-label/point-arrow/lower-label bands (4), infinity sentence (1), morphism lead-in (1), formula78 and raised déf label (2), gerbe prose (2), final formula (1), and lower T(1) insertion (1). Superscripts and subscripts are otherwise part of their formula band; cancellation strokes do not create extra lines. No OCR, internet lookup, or TeX compilation was used.',
    '147-063-N8: Punctuation and hand limits: the colon after raised resp-t consists of two dots, and no a-body is present; no period follows the final 1/12 of display79, whereas the opening equation has a period. The long returning g-descender in augmentation is not an underline. The diagram’s upper and right 1 bases are treated as numeral feet; only the lower label retains C’s underline. H’s separate drawing file was not provided, so no claim is made about its unseen geometry.',
]

check_events = [
    {'statement_id':'147-063-N1','date':'2026-11-20T21:28:56Z','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed',
     'type':'computation or formal certificate',
     'outcome':'Python fractions.Fraction computed -1/24+1/8=1/12 exactly. Only this rational equality was checked; the Euler-characteristic values of the geometric strata were not proved.'},
    {'statement_id':'147-063-N2','date':'2026-11-20T21:28:56Z','who':'reader_c; GPT-6 Astra Pro; reasoning effort not exposed',
     'type':'computation or formal certificate',
     'outcome':'Using T(1) as a formal variable, Fraction computation compared coefficient/constant pairs: row2 gives (1/4,-7/24) on both sides; row3 gives (1/4,-1/6) on both sides. Substitution T(1)=1 gave -1, -1/24, 1/12 for the three rows. This checks internal affine arithmetic only, not the asserted Grothendieck-class identities or geometry.'},
]

notation = [
    {'sign':r'\mathbb Z','reading':'double-struck Z in both margin bases and the lower Z[1/2]',
     'evidence':'Each has separated parallel diagonals with a narrow white interior.','scope':'scan063, three glyphs'},
    {'sign':r'\mathbb E^1','reading':'double-struck E with superscript 1',
     'evidence':'Two separated verticals at the left of the annotation E; repeated under the final cancellation.','scope':'scan063, Tate annotation and final canceled tail'},
    {'sign':r'T(1)','reading':'Tate expression, annotated augmentation 1',
     'evidence':'Underbrace and two annotation bands are present in the first row of 79; T(1) also appears as a lower insertion at the end.','scope':'scan063'},
    {'sign':r'\deleted{\unsure{\wedge}}','reading':'canceled former accent, tentatively a wedge',
     'evidence':'Multiple oblique dark strokes cross all five accents; the clean live heading hat supplies a local contrast.','scope':'scan063, three in 78 and two in gerbe prose'},
    {'sign':'4 versus 3','reading':'final digit 4 in the disputed U subscript',
     'evidence':'Angular upper hook plus upright rather than the two rounded lobes of 3. The first digit/comma group remains uncertain.','scope':'scan063, first row79'},
]

hand_log = [
    {'habit':'Long returning g-descender can look like a short underline.','pages':[63],
     'all_occurrences':'In augmentation the line returns left continuously from g; the gerbe g also has a broad leftward return. Neither is a separately drawn underline.',
     'witness_misreadings':'No underline is added in augmentation; parent’s initial apparent underline was rejected after crop review.'},
    {'habit':'Double-stroked Z and E are alphabet distinctions, not simply bold letters.','pages':[63],
     'all_occurrences':'Three Z glyphs and two E glyphs were checked locally; separated diagonals or verticals are visible in all five.',
     'witness_misreadings':r'C gives \mathbf Z and \mathbf E where the ink supports \mathbb.'},
    {'habit':'A base stroke on 1 may be a numeral foot rather than an added underline.','pages':[63],
     'all_occurrences':'Diagram top/right 1 labels have comparable attached feet; the lower 1 is overworked and has the longer base, retained as C’s underlined 1.',
     'witness_misreadings':'H drops the lower underline in its provided array; no new underline is inferred for the top or right labels.'},
    {'habit':'Final abbreviation letters can be raised above the base word.','pages':[63],
     'all_occurrences':r'The t of resp\textsuperscript{t} is elevated in the augmentation sentence.',
     'witness_misreadings':'C flattens the final t and reads the following colon as à; H misses the abbreviation in its rewritten prose.'},
]

abbreviations = [
    {'written':r'resp\textsuperscript{t}','expansion':'respectivement'},
    {'written':'ca.','expansion':'caractéristique'},
    {'written':'codim','expansion':'codimension'},
    {'written':'an','expansion':'analytique'},
    {'written':'déf','expansion':'définition'},
]

second_boxes = []
def second(kind, crop, reading, box_override=None):
    x0,y0,x1,y1 = box_override or boxes[crop]
    second_boxes.append({'box':f'B{len(second_boxes)+1:02d}','kind':kind,
                         'x0':x0,'y0':y0,'x1':x1,'y1':y1,'reading':reading})
second('handwritten number',15,r'\['+'\n'+opening+'\n'+r'\]')
second('word disagreement',13,'``groupe de')
second('word disagreement',14,"Grothendieck''")
second('margin note',1,margin+'\n'+r'79\quad\left\{')
second('doubtful formula',2,row1)
second('struck passage',3,row2)
second('struck passage',4,row3)
second('word disagreement',5,augment)
second('handwritten number',6,heading)
second('handwritten number',7,diagram)
second('handwritten number',8,r'(\uline{au dessus de} $\mathbb Z[\frac12]$)')
second('struck passage',9,morphism)
second('struck passage',10,gerbe)
second('doubtful formula',11,bottom)
second('margin note',12,r'\margin{62}')

report = {
    'scan':63,'reader':'reader_c','physical_lines_read':31,
    'changes':changes,'decisions':decisions,'inventory':inventory,'doubts':doubts,
    'notes':notes,'check_events':check_events,'notation':notation,'hand_log':hand_log,
    'abbreviations':abbreviations,'second_boxes':second_boxes,
    'unresolved':[
        'M1039: pour dispenser|pour me dispenser in the sloping margin.',
        'M1040: first U subscript digit/comma remains 0,4|3,4; final 4 is distinct.',
        'Two canceled trials in display79 remain tentative as whole expressions.',
        'All five canceled original accents remain doubtful wedges.',
        'Final coefficient remains 2|1/2; final canceled calculation remains tentative.',
        'T(1) is live below the canceled tail, but no connector specifies its narrower intended replacement scope.',
    ],
    'witness_comparison': 'C preserves the full prose, margin, canceled trials, short ca., and more of the diagram and final line. It needs the double-struck alphabets, colon and raised resp-t, removal of the supplied period after 79, and physical placement of the divider-crossing arrow and lower T(1). H preserves the double-struck alphabets and the colon, but replaces the augmentation sentence with a different reading, puts 79 in the margin, leaves readable marginal material and struck trials in editorial notes/ill marks, gives the five canceled accents as live hats, omits constant, expands ca. to car., adds hyphens and a comma, and prefers 1/2 for the unresolved final coefficient. The current page retains uncertainty where cancellation/overwork prevents a firm choice. Only H’s supplied text and array, not its unavailable separate drawing, were compared.',
}

assert len(changes) == 29
assert [d['id'] for d in decisions] == ['M1039','M1040']
assert [c['id'] for c in changes] == [f'063-{i:02d}' for i in range(1,30)]
for c in changes:
    assert (WORK/'crops'/c['crop']).is_file()
    assert c['against_C'] or c['against_H']
for n in boxes:
    assert (WORK/'crops'/f'147_scan063_place{n:02d}.png').is_file()
for e in check_events:
    assert any(note.startswith(e['statement_id']+':') for note in notes)
assert proposed.count(r'\deleted{\unsure{\wedge}}') == 5
assert proposed.count(r'\mathbb Z') == 3
assert proposed.count(r'\mathbb E') == 2
assert r'\illegible' not in proposed
assert r'\margin{62}' in proposed

(OUT/'proposed.tex').write_text(proposed)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'return_dir':str(OUT),'physical_lines_read':31,'crops':15,'changes':len(changes),
                  'decisions':len(decisions),'inventory':len(inventory),'doubts':len(doubts),
                  'second_boxes':len(second_boxes),'check_events':len(check_events)},ensure_ascii=False))
