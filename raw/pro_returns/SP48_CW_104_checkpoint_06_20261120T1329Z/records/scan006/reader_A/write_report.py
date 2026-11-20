from pathlib import Path
import json
from datetime import datetime, timezone

OUT = Path(__file__).parent
SRC = Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans')
issues = []

def add(id, location, C, H, reading, evidence, bbox, crop='', confidence='high', diff_C=False, diff_H=True, kind='misread symbol or index', marked_in_H='no', unresolved=False):
    issues.append(dict(id=id,location=location,C=C,H=H,reading=reading,evidence=evidence,confidence=confidence,diff_C=diff_C,diff_H=diff_H,kind=kind.replace(chr(92)*2,chr(92)),marked_in_H=marked_in_H,crop=('crops/'+crop+'.png') if crop else '',bbox=bbox,unresolved=unresolved))

add('A01','Sideways typed heading, round argument',r'B(\unsure{0|O})',r'B(0)',r'B(\unsure{0|O})',
    'One unslashed oval fills the parentheses. Its ink gives no reliable distinction between typewriter zero and capital O. The same oval is checked in the body and uses the first candidate after the first doubt.',[115,590,177,697],'01_typed_strip',confidence='medium',unresolved=True)
add('A02','Complete sideways typed strip', 'Complete English strip, including both isolated hatted B groups', 'Editorial French summary, no diplomatic transcription of the strip', 'Complete English strip, as in C',
    'All five typed lines and the three heading groups are visible after rotation. Underlines sit below B, D and N; the first isolated caret is over B, the second follows the closing parenthesis. Gr-stacks has capital G, lower-case r and a hyphen.',[103,60,445,1445],'01_typed_strip',kind='omission')
add('A03','Typed line 2, amountsto', 'amountsto', 'Summary only; wording not transcribed', 'amountsto',
    'The s and following t have the same character pitch as the interior letters, with no intervening word space. The surrounding word spaces are visibly wider.',[238,624,282,763],'01_typed_strip',kind='omission')
add('A04','Typed final line, n before underlined N',r'n\ \underline{N}',r'n\in\underline{N}',r'n\ \underline{N}',
    'There is a blank character space between n and the underlined N. No membership glyph or ink trace occupies it.',[391,1066,445,1165],'01_typed_strip',kind='text not on the page')
add('A05','Top isolated tilded D',r'\widetilde{\unsure{D|\mathbb D}}',r'\widetilde D',r'\widetilde{\mathbb D}',
    'Two separately drawn descending stem edges enclose a narrow white channel; the inner returning stroke ends just above the foot. The nearby D_n has only one upright. The detached wave above is clear.',[648,80,754,183],'02_top_symbols',diff_C=True)
add('A06','Top domain of map',r'\unsure{N|\mathscr N}\mapsto',r'\mathbb N\ni n\mapsto',r'\unsure{N|\mathscr N}\mapsto',
    'A single large curved letter precedes the mapsto tail: a rising left sweep, heavy central downstroke and upper-right arch. Its calligraphic status remains uncertain. There are no separate membership and small n between it and the arrow.',[945,120,1121,203],'02_top_symbols',confidence='medium',unresolved=True)
add('A07','Crossed older form above top D_n',r'\deleted{\unsure{I_n|D_n}}','Omitted',r'\deleted{\unsure{I_n|D_n}}',
    'A tall upright, long upper and lower bars, and a small low n survive under two rising cancellation strokes. I_n is favoured; a D boundary cannot be separated confidently from the diagonal overstrike.',[1064,37,1178,153],'02_top_symbols',confidence='low',kind='omission',unresolved=True)
add('A08','Three parallel maps at upper left', 'Three right arrows', 'Two right arrows', 'Three right arrows',
    'An upper arched shaft, a middle straight shaft and a lower curved shaft each end in a separate right-facing arrowhead.',[705,272,823,385],kind='drawing or diagram')
add('A09','Vertical map to n in I',r'\widetilde D_n\downarrow n\in\unsure{\mathbb I|I}',r'\widetilde D_n\longrightarrow n\in I',r'\widetilde D_n\downarrow n\in\mathbb I',
    'A long downward shaft has a V-shaped head. The I below has two narrow parallel stems with a visible white channel between broad top and bottom bars. The map is vertical, not a horizontal line of objects.',[871,388,1110,626],diff_C=True,kind='drawing or diagram')
add('A10','Canceled N before the upper live I',r'\deleted{\unsure{N}}',r'\struck{\mathbb N}',r'\deleted{N}',
    'The underlying left upright, falling diagonal and right upright form N. Three rising strokes cancel it; those cancellation strokes do not establish an independent doubled alphabet.',[1390,269,1478,350],'03_upper_map_words',diff_C=True,kind='deletion state')
add('A11','Upper live I following canceled N',r'\mathbb I',r'I',r'\mathbb I',
    'A thin returning stem and heavier adjacent stem enclose a white wedge above the lower serif. This occurrence was checked separately from the I under the downward arrow.',[1461,282,1541,349],'03_upper_map_words')
add('A12','Word below strictement',r'\unsure{croissante}', 'croissante', 'croissante',
    'The opening c-r-o-i is followed by two joined s-like bends, a low a/n sequence, a tall crossed t and final e. The word is legible despite the connected middle.',[1250,398,1468,448],'03_upper_map_words',diff_C=True,diff_H=False,kind='misread word')
add('A13','After image in upper annotation',r'\unsure{est|=|\subset}','No word or relation here',r'\unsure{est|=|\subset}',
    'A shallow open loop continues into a long low stroke and angular upturn. The image does not securely separate a cursive est from shorthand relation strokes; it does not show two clean parallel equals bars. Retained as a genuine in-place doubt.',[1397,465,1471,506],'03_upper_map_words',confidence='low',kind='omission',unresolved=True)
add('A14','I in upper image annotation',r'\mathbb I',r'I',r'\mathbb I',
    'The large I has an independently returning inner stem and white channel, with broad horizontal caps.',[1490,438,1589,511],'03_upper_map_words')
add('A15','Crossed qualifier below the image I',r'\deleted{\unsure{\in n}}',r'\struck{\mathbb N}',r'\deleted{\unsure{\in n}}',
    'An open loop and short wavy n-like trace lie under an oblique cancellation; the surviving live qualifier is a separate less-or-equal sign followed by n. No clear full capital N can be isolated in the crossed trace.',[1531,492,1615,528],'03_upper_map_words',confidence='low',kind='deletion state',unresolved=True)
add('A16','Upper right calculation, continuation and trailing equals',r'2^2\ \text{---}\ +2^n;\quad =(1+2)^n=',r'2^2+\cdots+2^n=(1+2)^n',r'2^2\ \text{---}\ +2^n;\quad =(1+2)^n=',
    'After 2^2 is one long horizontal stroke, followed farther right by +2^n. On the next line a clear equals follows the exponent n, then blank paper. It is not completed with 3^n.',[1500,85,2257,289],kind='omission')
add('A17','Sideways diagram, initial J',r'\unsure{J|I}_{n\prime\prime}','Omitted',r'J_{n\prime\prime}',
    'The upright returns in an oval loop to its lower-left, unlike the straight lower bar of the upright I elsewhere. Two separate prime strokes follow the n.',[2196,247,2278,378],'04_margin_diagram',diff_C=True,kind='omission')
add('A18','Sideways first arrow label',r'\unsure{u_\eta|u_g|u_y}','Omitted',r'\unsure{u_\eta|u_y}',
    'The subscript has an open short upper stroke, round right turn and long descending hook. There is no closed g-bowl. Eta is favoured, with y still graphically possible.',[2237,407,2286,464],'04_margin_diagram',confidence='medium',diff_C=True,kind='omission',unresolved=True)
add('A19','Sideways letter over middle J',r'\unsure{\eta|y}','Omitted',r'\eta\text{ (same retained eta/y doubt as first arrow label)}',
    'The upper letter has the same open hooked contour as the first-arrow subscript. Its ambiguity is retained at that first occurrence; the repeated marker can be consolidated without claiming independent resolution.',[2278,493,2322,537],'04_margin_diagram',confidence='medium',kind='omission',unresolved=True)
add('A20','Sideways membership above middle J',r'\rotatebox{90}{\in}','Omitted',r'\rotatebox{-90}{\in}',
    'In the upright rotated crop, the arch opens downward and its middle stroke also descends. This requires a minus-90-degree rotation of the usual right-open membership sign.',[2275,522,2305,555],'04_margin_diagram',diff_C=True,kind='misread symbol or index')
add('A21','Sideways crossed second-arrow label',r'\deleted{\unsure{u_\eta|u_g}}','Omitted',r'\deleted{\unsure{u_\eta|u_g}}',
    'An older pair of loops and a hooked low trace are crossed above the live u-subscript label. Cancellation intersections prevent secure separation of the older subscript.',[2254,674,2306,729],'04_margin_diagram',confidence='low',kind='omission',unresolved=True)
add('A22','Sideways live second-arrow label',r'\unsure{u_\xi|u_f}','Omitted',r'\unsure{u_\xi|u_f}',
    'After u, a winding descending stroke crosses the arrow shaft. Its upper and middle turns favour xi, but the surviving contour also permits a cursive f.',[2221,678,2275,727],'04_margin_diagram',confidence='medium',kind='omission',unresolved=True)
add('A23','Sideways diagonal arrow caption',r'\unsure{u}','Omitted',r'\unsure{u}',
    'A short rising stroke and a long loop are superposed on the oblique arrow shaft. Only a possible u is separable; no additional subscript is invented.',[2130,668,2191,786],'04_margin_diagram',confidence='low',kind='omission',unresolved=True)
add('A24','Sideways letter above last J',r'\unsure{\xi|x}','Omitted',r'\unsure{\xi|x}',
    'The small letter consists of crossed loops and a downward tail. Xi is favoured but the congested crossed form also allows x.',[2292,775,2338,821],'04_margin_diagram',confidence='low',kind='omission',unresolved=True)
add('A25','Sideways membership above last J',r'\rotatebox{90}{\in}','Omitted',r'\rotatebox{-90}{\in}',
    'Checked independently: the right-hand arch likewise opens down in the upright crop, with its middle stroke directed into the opening.',[2276,812,2310,847],'04_margin_diagram',diff_C=True)
add('A26','Sideways last J corrected index',r'J_{\deleted{\unsure{n\prime}}n}','Omitted',r'J_{\deleted{\unsure{n\prime}}n}',
    'A low n-like group is crossed by the leftward baseline/overstrike; a short higher tick may be the old prime. The final live n is clear.',[2204,785,2243,871],'04_margin_diagram',confidence='low',kind='omission',unresolved=True)
add('A27','Sideways diagonal arrow endpoint',r'\unsure{\xi|x|f}','Omitted',r'\unsure{\xi|x|f}',
    'Two dark loops and a long descending stem are visible at the oblique arrow endpoint; the upper part is heavily retraced. No candidate is secure enough to remove the doubt.',[2115,783,2194,850],'04_margin_diagram',confidence='low',kind='omission',unresolved=True)
add('A28','Sideways diagram, structure',r'J_{n\prime\prime}\to J_{n\prime}\to J_n\text{ plus diagonal arrow}','Omitted', 'Same structure as C, with both vertical membership signs corrected',
    'There are two horizontal right arrows in the rotated view and one oblique arrow to the lower-right glyph. The middle object has a square-backed J and one prime on n. No French prose accompanies this margin construction.',[2095,240,2345,890],'04_margin_diagram',kind='omission')
add('A29','Sideways equality below diagram',r'u_\xi u_\eta=', 'Omitted',r'u_\xi u_\eta=',
    'Two u letters are followed respectively by the winding and hooked descending subscripts. Two separate equals bars are followed by blank paper. The relation has no written right member.',[2130,1015,2290,1215],'05_margin_equality',kind='omission')
add('A30','Right-hand x/y array, relations',r'x^{\prime\prime}<x^\prime;\ y^{\prime\prime}<y^\prime',r'x^{\prime\prime}\leq x^\prime;\ y^{\prime\prime}\leq y^\prime',r'x^{\prime\prime}<x^\prime;\ y^{\prime\prime}<y^\prime',
    'Each relation has only an upper oblique and lower near-horizontal branch meeting at the left. There is no detached lower bar in either occurrence.',[1800,725,1879,850],'06_xy_array')
add('A31','Crossed vertical mark between x-double-prime and y-double-prime',r'\deleted{\unsure{=}}','Omitted',r'\deleted{\unsure{=|\downarrow}}',
    'Several short horizontal/oblique bars intersect a central vertical ending in a dark downward point. A canceled equals is possible, but the central shaft and point also allow a canceled down-arrow. The exact older sign remains uncertain.',[1743,765,1793,819],'06_xy_array',confidence='low',diff_C=True,kind='deletion state',unresolved=True)
add('A32','Older D over the right-hand array object',r'\deleted{\unsure{D}}','Omitted',r'\deleted{\unsure{D}}',
    'A left upright and right bowl-like boundary are crossed by diagonals above the live tilde. The old character is D-like, but its intersections remain too dense for certain removal of the doubt.',[2032,702,2095,768],'06_xy_array',confidence='low',kind='omission',unresolved=True)
add('A33','Live right-hand array object and both memberships',r'\widetilde D_n\text{ with one membership on each row}',r'\widetilde D_{\ill{}}\text{ after the two-row array}',r'\widetilde D_n\text{ with one membership on each row}',
    'A wavy n sits low to the right of the live D. Two separate membership glyphs are visible, one level with each row. The n is readable and is not an illegible word.',[1977,751,2113,846],'06_xy_array',kind='readable ink left as \\ill{}',marked_in_H='yes')
add('A34','Array vertical connectors, lower n labels and bowed strokes', 'Vertical connectors, n-double-prime/n-prime, two bowed strokes and two dots', 'Omitted', 'Same elements as C',
    'A plain vertical stroke connects x-prime to y-prime, with a second stroke below y-prime. n-prime is below; n-double-prime is leftward and touched by the upper of two bowed curves. Two strong detached dots are farther right. The curves are open at both ends.',[1685,760,2051,1080],kind='omission')
add('A35','I ens ordonné',r'\unsure{ens}', 'un', 'ens',
    'An initial low loop is followed by two joined humps and a terminal s-like sweep. It matches the other ens contractions on this page. The following ordonné has a detached acute.',[707,747,811,797],'07_middle_words',diff_C=True,kind='misread word')
add('A36','Family description, first word after D_n',r'\unsure{famille|échelle};\text{ audit also floated symbole d\prime un ordre}', 'famille', 'famille',
    'The first letter has a tall loop and long descending f-stem, followed by low a/m strokes and two ascenders. This resolves famille and does not support échelle or the contextual earlier symbole phrase.',[927,804,1093,901],'07_middle_words',diff_C=True,diff_H=False,kind='misread word')
add('A37','Family description, final word',r'\unsure{ordonnés}', 'ordonnés', 'ordonnés',
    'The initial oval and r/d sequence, repeated low n humps, final accent mark and terminal s-like stroke are readable; a separate comma follows.',[1263,809,1548,864],'07_middle_words',diff_C=True,diff_H=False,kind='misread word')
add('A38','Family description, d’ens punctuation', "d'ens", "d'ens.", "d'ens",
    'The s joins a terminal low sweep; the following space contains no abbreviation stop before ordonnés.',[1113,809,1262,862],'07_middle_words',kind='abbreviation expanded or spelling modernised')
add('A39','Overwritten older label on middle map',r'\deleted{\unsure{\phi}}', 'Omitted',r'\deleted{\unsure{\phi}}',
    'A vertical passes through a rounded loop, with a lower tail extending beyond the live k-like arms. The phi-like contour is visible, but the exact boundary and writing order at the overlap remain uncertain.',[683,905,729,976],'08_corrected_map_label',confidence='low',kind='omission',unresolved=True)
add('A40','Live label on middle map',r'\unsure{k_n|\kappa_n|\tau_n}',r'\tau_n',r'\unsure{k_n|\kappa_n|K_n}',
    'The live form has a rightward upper arm and a distinct slanting lower-right arm beside the overwritten upright. Together with the independently inspected set-condition occurrence this excludes a simple tau. The Latin/Greek form and capitalization remain uncertain.',[689,921,744,975],'08_corrected_map_label',confidence='medium',diff_C=True,unresolved=True)
add('A41','Canceled opening after Si n-prime less-or-equal n',r'\deleted{\unsure{Soit|Sinon}}',r'\struck{soit}',r'\deleted{\unsure{Soit|Sinon}}',
    'The high initial S and small following strokes are crossed by the long cancellation. The middle letters are not separable enough to decide Soit versus Sinon. The initial is capital-sized, as is the live Soit to its right.',[873,1066,1019,1125],'10_canceled_opening',confidence='low',kind='deletion state',unresolved=True)
add('A42','Canceled l’ens, stop', "l'ens", "l'ens.", "l'ens",
    'The tall l loop, apostrophe and low ens humps remain readable below the strike. No separate stop follows the s before the capital K.',[1017,1068,1194,1125],'10_canceled_opening',kind='abbreviation expanded or spelling modernised')
add('A43','Canceled capital before live Soit',r'\unsure{K}',r'\ill{}',r'K',
    'The character has a full vertical upright and two distinct right branches, one rising and one descending. The crossing horizontal cancellation does not obscure the capital K.',[1224,1056,1298,1118],'10_canceled_opening',diff_C=True,kind='readable ink left as \\ill{}',marked_in_H='yes')
add('A44','Named subset letter',r'\unsure{\mathscr L|\Phi|L}',r'\Phi',r'\unsure{\Phi|\mathscr L|L}',
    'The upper contour has an open left oval and closed right oval, split by a central descending stem ending on a broad horizontal foot. This favours Phi, but the open loop and flourish still permit a script L. The same local form was checked in the canceled next line.',[1455,1047,1526,1113],'09_subset_definition',confidence='medium',diff_C=True,unresolved=True)
add('A45','Definition layout, vertical equals', 'Vertical equals between subset name and set expression', 'Horizontal equals in the same running line', 'Vertical equals as C',
    'Two short parallel vertical strokes sit directly below the subset name and above the opening brace. The source arranges the definition on two levels.',[1514,1128,1553,1174],'09_subset_definition',kind='insertion or placement')
add('A46','Map label inside the set condition',r'\unsure{k_n|\kappa_n|\tau_n}',r'\tau_n',r'k_n\text{ using the first-occurrence k/kappa/K doubt}',
    'This clearer occurrence has a vertical left stem, upper-right arm and detached lower-right diagonal, followed by a low n. The lower arm is incompatible with plain tau. It was inspected independently; uncertainty is consolidated at the first occurrence.',[1690,1190,1757,1248],'09_subset_definition',confidence='medium',diff_C=True,unresolved=True)
add('A47','Canceled next line, subset subscript',r'\mathscr L_{\unsure{n\prime}}',r'\Phi_{n\prime}',r'\Phi_{n\prime}\text{ with capital-letter doubt retained above}',
    'The small n is followed by a separate short high tick and a lower comma. The prime itself is clear, so that local index doubt is resolved. The capital shape remains covered by A44.',[948,1272,1013,1316],'11_canceled_soit',diff_C=True,diff_H=False)
add('A48','Considérons',r'\unsure{Considérons}', 'Considérons', 'Considérons',
    'A large C is followed by the low joined onsi sequence, a distinct d ascender, an acute above the next vowel and a final rons run. The word is readable.',[591,1337,872,1399],'12_considérons',diff_C=True,diff_H=False,kind='misread word')
add('A49','Considérons l’ens, stop', "l'ens", "l'ens.", "l'ens",
    'The abbreviation has a tall l, apostrophe and low ens; no stop appears after its final upward s stroke.',[934,1326,1101,1398],'12_considérons',kind='abbreviation expanded or spelling modernised')
add('A50','Canceled object before large B',r'\deleted{\unsure{\widetilde D_{n\prime}|D_n}}',r'\struck{\ill{}}',r'\deleted{\unsure{\widetilde D_{n\prime}|D_n}}',
    'A D-like upright/bowl, small n-like low group and possible upper wave survive through dense cross-hatching. The original tilde and prime cannot be securely separated from the crossing strokes.',[1237,1300,1353,1400],'12_considérons',confidence='low',kind='readable ink left as \\ill{}',marked_in_H='yes',unresolved=True)
add('A51','Large live B',r'\unsure{B|\mathscr B}', 'Omitted',r'\unsure{B|\mathscr B}',
    'One tall left contour joins a rounded upper lobe and very broad oblique lower lobe. The letter is B-shaped; its flourished versus ordinary alphabet is not securely distinguishable.',[1413,1304,1547,1420],'12_considérons',confidence='medium',kind='omission',unresolved=True)
add('A52','F chain, middle F_1',r'\mathbb F_1',r'F_1',r'\mathbb F_1',
    'Two separate upright contours enclose a long white channel running from below the top arm to near the foot; a middle arm crosses both.',[943,1434,993,1517],'13_F_chain')
add('A53','F chain, last F_2',r'F_2',r'F_2',r'\mathbb F_2',
    'The full stem contains two distinct returning contours with white space both above and below the middle arm. This is not merely the curved top-arm hook. F_0 was separately checked and has one stem.',[1106,1434,1182,1515],'13_F_chain',diff_C=True)
add('A54','Loop beside x, actual H drawing', 'Open loop arrow at x, without an added vertex dot', 'H_drawing uses a filled point and a geometrically closed returning loop', 'Keep C loop diagram; preserve the left-end gap and no separate point',
    'The source has a short lower-left starting stroke and an upper-left arrowhead separated by a visible gap, with x left of the gap. There is no independent filled circular vertex. H_drawing header is correct for archive 5 / PDF 6 and was compared as the actual drawing, not only its prose description.',[786,1533,951,1635],kind='drawing or diagram')
add('A55','Small x-prime / y-prime vertical diagram at foot', 'x-prime and y-prime joined by a plain line', 'Omitted', 'Same as C',
    'One prime follows x and one follows y; the intervening narrow line has no arrowhead. The curled end of y is part of the letter.',[1643,1353,1728,1540],kind='omission')
add('A56','Lower-right curved arrow, dot and sloping segment', 'Curved arrow between two solid points, separate dot, simple lower segment', 'Omitted', 'Same arrangement, with short downward peg at left end of lower segment',
    'The start and target are solid black knots without enclosed white counters; the arrowhead has two branches below the target knot. A separate small black dot lies to the right. The lower sloping segment begins with a short downward attached peg, omitted by C.',[1867,1239,2081,1415],'15_curved_arrow',diff_C=True,kind='drawing or diagram')
add('A57','Index of F in pi-zero expression',r'F_{\unsure{*|x}}',r'F_*',r'F_*',
    'The small index has multiple short crossing rays, including an extra low stroke, unlike the separate two-stroke x after the comma. Asterisk is resolved as the best ink reading.',[1152,1574,1207,1604],'14_pi_formula',confidence='medium',diff_C=True,diff_H=False)
add('A58','First abbreviation in pi-zero expression',r'\unsure{ens}', 'ens.', 'ens',
    'The initial low loop and joined n/s humps agree with the page’s other ens abbreviations. No baseline stop is written after the final s.',[1310,1546,1410,1586],'14_pi_formula',diff_C=True,kind='abbreviation expanded or spelling modernised')
add('A59','Word classes in pi-zero expression',r'\unsure{classes}',r'\uncertain{classes}', 'classes',
    'The c and tall l are joined into a d-like opening, followed by a low a and repeated s/e/s turns. The word is readable in the line.',[1534,1526,1672,1585],'14_pi_formula',confidence='medium',diff_C=True,diff_H=True,kind='misread word',marked_in_H='yes')
add('A60','Phrase after classes',r"d'\unsure{hom.topie|homotopie} des", 'de lacets (homotopy phrase omitted)', "d'hom.topie. des",
    'After d-apostrophe, the hom group ends before a distinct low dot; t begins the next group. A second separate dot follows the terminal e of topie before des. These visible stops are retained, and the absent o is not supplied.',[1701,1516,2098,1589],'14_pi_formula',confidence='medium',diff_C=True,kind='omission')
add('A61','Second line, lacets en x',r'\unsure{lacets}', 'lacets', 'lacets',
    'The initial l has a tall closed loop; a low a/c run leads to crossed t and final s. en x follows clearly.',[1307,1583,1458,1635],'14_pi_formula',diff_C=True,diff_H=False,kind='misread word')
add('A62','Detached short marks in upper-middle blank areas', 'Omitted', 'Omitted', 'Two short nonlinguistic strokes, with one tiny detached mark above the second',
    'The half images show a short dark horizontal stroke near (557,522), and another slightly sloping stroke near (879,677) with a tiny upright fleck just above its left end. They are traced without assigning a word or mathematical role.',[550,512,921,686],diff_C=True,kind='drawing or diagram')
add('A63','Punctuation after str. croiss.', 'str. croiss.', 'str. croiss.,', 'str. croiss.',
    'A separate stop follows each abbreviation. There is no further comma after the second stop before image.',[893,942,1162,995],kind='text not on the page')
add('A64','Placement of separate right-hand D map', 'Before the central ordered-set prose', 'After the bottom pi-zero paragraph', 'Source right-hand fragment above the x/y array',
    'The separate D_n-prime to D_n arrow is positioned in the upper-right portion immediately above the x/y array, not after the foot paragraph.',[1738,552,2082,661],kind='insertion or placement')

inventory = []
def inv(element,kind,bbox,first,hand='his hand'):
    inventory.append(dict(element=element,kind=kind,position='full-image bbox '+str(bbox),first_words_or_objects=first,sheet_kind='reused_typed',hand=hand,transcribed='yes'))

inv('Sideways typewritten heading','display',[103,60,181,1192],'Underlined B = (Gr-stacks); hatted B; B(0/O) with raised caret','typewriter, unattributed')
inv('Sideways typewritten body','text',[178,60,445,1445],'commutes not only with arbitrary projective limits','typewriter, unattributed')
inv('Isolated doubled D','display',[648,80,754,183],r'\widetilde{\mathbb D}')
inv('Top mapping rule','display',[945,120,1214,205],r'N\mapsto\widetilde D_n')
inv('Old form over top mapping target','deletion',[1064,37,1178,153],'I_n / D_n under cancellation')
inv('Unfinished binomial calculation','display',[1500,85,2257,289],'1+n·2^1+...; =(1+2)^n=')
inv('Three arrows','diagram',[614,243,948,386],r'\widetilde D_{n\prime}\to\widetilde D_n, three arrows')
inv('Upper d_n map and rule','display',[1069,251,1838,367],r'd_n\in\widetilde D_n\to I; d_n\mapsto n')
inv('Canceled N at upper target','deletion',[1390,269,1478,350],'N')
inv('Increasing-image annotation','text',[1248,351,1667,534],'strictement croissante; image est/= /subset I')
inv('Canceled image qualifier','deletion',[1531,492,1615,528],r'\in n, uncertain')
inv('Map down to n in I','diagram',[871,388,1110,626],r'\widetilde D_n\downarrow n\in\mathbb I')
inv('Sideways margin construction','margin note',[2095,240,2345,890],'J_n-double-prime → J_n-prime → J_n and diagonal arrow')
inv('Sideways older arrow label','deletion',[2254,674,2306,729],'u_eta / u_g')
inv('Sideways corrected final index','deletion',[2204,785,2243,871],'old n-prime / live n')
inv('Sideways unfinished equality','margin note',[2130,1015,2290,1215],'u_xi u_eta =')
inv('Two isolated marks','drawing',[550,512,921,686],'short strokes and small fleck')
inv('Right-hand D map','display',[1738,553,2082,661],r'\widetilde D_{n\prime}\to\widetilde D_n')
inv('Two-row x/y array','diagram',[1717,708,2112,992],'x-double-prime < x-prime; y-double-prime < y-prime')
inv('Crossed vertical relation','deletion',[1743,765,1793,819],'equals / down-arrow')
inv('Crossed older D at array','deletion',[2032,702,2095,768],'D-like glyph')
inv('Bowed strokes and two dots','drawing',[1685,865,2051,1080],'two open curves, two strong dots')
inv('Ordered-set declaration','text',[615,721,1093,799],'I ens ordonné')
inv('Family declaration','text',[604,806,1548,899],r'n\mapsto\widetilde D_n famille d’ens ordonnés ,')
inv('Labeled map to I','display',[576,900,1714,1014],r'\widetilde D_n\to I; str. croiss.; image I_{\le n}')
inv('Older phi-like map label','deletion',[683,905,729,976],'phi-like loop')
inv('Conditional definition introduction','text',[564,1061,1412,1147],'Si n-prime ≤ n, ... Soit')
inv('Canceled first opening','deletion',[873,1056,1298,1125],'Soit/Sinon l’ens K')
inv('Subset definition','display',[1442,1035,1957,1280],'Phi/script L/L_{n-prime,n} subset D_n; vertical equals; set builder')
inv('Canceled Soit line','deletion',[650,1252,1090,1322],'Soit x in Phi_{n-prime},')
inv('Considérons line','text',[591,1304,1547,1420],'Considérons l’ens ... B')
inv('Canceled object before B','deletion',[1237,1300,1353,1400],'D-like object with small index')
inv('Curved arrow and segment sketch','drawing',[1867,1239,2081,1415],'two solid knots, arrow, separate dot, sloping segment and peg')
inv('x-prime to y-prime sketch','diagram',[1643,1353,1728,1540],'x-prime | y-prime')
inv('F chain','diagram',[778,1434,1182,1520],'F_0 leftleftarrows doubled F_1 leftleftarrows doubled F_2')
inv('Loop at x','diagram',[786,1533,951,1635],'x and returning loop with open left gap')
inv('Pi-zero formula','display',[1035,1516,2140,1649],'pi_0(F_*,x) = ens des classes d’hom.topie. des lacets en x')
inv('Archive numeral','text',[39,1598,94,1652],'5','archive marking, unattributed')

report = dict(
    scan=6,reader='A',model='GPT-6 Astra Pro',effort='inherited/not exposed',
    started_utc='2026-11-20T11:11:42Z',finished_utc=datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),
    views=[str(SRC/'H104-01_104_scan006.jpg'),str(SRC/'H104-01_104_scan006_a.jpg'),str(SRC/'H104-01_104_scan006_b.jpg')]+[str(OUT/x['file']) for x in json.loads((OUT/'crop_processing.json').read_text())],
    issues=issues,inventory=inventory,
    notes=[
        'Source is landscape, 2375 by 1690 pixels. Whole viewed once, left half a once, right half b once, then fifteen unique decision crops once each. No OCR, web, render, compilation or other scan used.',
        'The source is visibly a reused typed sheet: a sideways English typescript block occupies the left edge and handwriting fills the rest. Faint background traces are not reconstructed as additional words.',
        'H_drawing.tex explicitly identifies archive page 5 / PDF page 6, so it is authorized current-page evidence. Its actual TikZ was compared; only its loop is supplied, and the separate lower-right sketch remains absent from H.',
        'The initial clock timestamp is the first recorded clock immediately before the whole-image view. Brief and authorized text packet were read just before it.',
        'A stray row labelled scan 7 in the original C_context was excluded as current-page evidence when the packet correction arrived. Earlier cross-page claims in C are not treated as verified evidence.',
        'Handwritten notes introduce an ordered I, a family of ordered sets D_n, a strictly increasing map with image I_{≤n}, and a named subset defined by a fiber condition. This is a content observation, not a proof check.',
        'The calculation visibly ends =(1+2)^n= with no last member. The sideways equality u_xi u_eta= is also unfinished. No completion has been supplied.',
        'The last formula visibly uses pi_0 and refers to classes d’hom.topie. of loops based at x. Its mathematical index is transcribed without changing it to pi_1 or asserting a correction.',
        'No written author question or explicit doubt word was found. The reader’s doubts are the in-place unsure macros. The page has no manuscript title, date or own folio; 5 at bottom left is recorded only as an archive sheet number.',
        'Crop 14 includes the complete F symbol and its small index; several tall ascender tips farther along the slanting prose touch its top edge. Those complete letters had already been seen in half b. No recrop was made.',
        'The detached-stroke drawing records visible ink without assigning mathematical or lexical significance. Pale show-through, grain and pressure texture are not inventoried as extra objects.',
    ],
    notation=[
        {'sign':'N / script N','evidence':'One large curved domain glyph; no independent membership sign or small n is present. Alphabet remains uncertain.'},
        {'sign':'D and doubled D','evidence':'Only isolated top D has a clear returning inner stem with a white channel. Each later D was inspected separately and remains plain.'},
        {'sign':'I / doubled I','evidence':'Upper three large I forms have separated inner returns; the middle declaration I and labeled-map target have single stems. No uniform alphabet imposed.'},
        {'sign':'eta / y and xi / f / x','evidence':'Sideways diagram uses a hooked descending contour and a winding descending contour. Equality repeats them. First eta/y doubt retained at its first label; obstructed occurrences retain local alternatives.'},
        {'sign':'vertical membership','evidence':'Both rotated-view arches open down, with a central downward stroke: rotatebox -90 of in. Each was inspected independently.'},
        {'sign':'k / kappa / K','evidence':'A distinct lower-right diagonal arm occurs in the clearer set condition and is present in the overwritten map label. Tau is excluded; Latin/Greek and case remain uncertain. First occurrence carries the doubt.'},
        {'sign':'Phi / script L / L','evidence':'Open left oval, closed right oval, central descending stem and broad foot. Phi placed first provisionally, alternatives retained. Later canceled occurrence uses this first candidate.'},
        {'sign':'F alphabets','evidence':'F_0 has a single stem; F_1 and F_2 have separate returning stems and white channels. F in pi-zero expression is plain. The asterisk has multiple rays, distinct from following x.'},
        {'sign':'ens and hom.topie.','evidence':'The ens contractions have no clear baseline stops where H adds them; str. and croiss. each have explicit stops. The final hom.topie. has two visible dots, one internal and one terminal.'},
        {'sign':'primes','evidence':'n-prime, n-double-prime, x-prime/x-double-prime and y-prime/y-double-prime are short raised strokes, not exclamation marks; the canceled Soit-line index has a distinct single prime.'},
        {'sign':'typed zero / O','evidence':'The same unmarked oval appears in both B arguments. Distinction remains unresolved; first occurrence carries the alternatives and the next uses zero.'},
    ],
    checks=[],crop_count=15,
    brief_feedback='The explicit H_drawing page-header check prevented a suffix-based page assumption. Fifteen crops were warranted by the many existing C doubts and crowded cancellations; several neighboring doubts share one tight line crop. No additional instructions were needed.'
)

# Sort inventory by the top of its source box, retaining source order within a level.
def top(item):
    return json.loads(item['position'].split('bbox ',1)[1])[1]
report['inventory'].sort(key=top)
(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'issues':len(issues),'inventory':len(inventory),'crops':15}))
