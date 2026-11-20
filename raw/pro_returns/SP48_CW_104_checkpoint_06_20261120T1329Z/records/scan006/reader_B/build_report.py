from pathlib import Path
from datetime import datetime, timezone
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan006/reader_B')
source=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans')
proc=json.loads((root/'processing_log.json').read_text())
crops={i+1:Path(p['path']).relative_to(root).as_posix() for i,p in enumerate(proc['processing'])}
issues=[]
def add(id,location,C,H,reading,evidence,confidence,diff_C,diff_H,kind,bbox,crop=0,unresolved=False,marked='no'):
    issues.append({'id':id,'location':location,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'diff_C':diff_C,'diff_H':diff_H,'kind':kind,'marked_in_H':marked,'crop':crops[crop] if crop else '', 'bbox':bbox,'unresolved':unresolved})
add('B01','Sideways typed heading, parenthesized argument',r'\unsure{0|\mathrm O}',r'0 in an editorial summary',r'\unsure{0|\mathrm O}',
    'One oval typewriter character fills the parentheses. The second occurrence has the same form; no securely contrasting zero and capital O occurs in the visible type. The first occurrence retains both candidates.', 'medium',False,True,'misread symbol or index',[123,611,176,690],1,True)
add('B02','Entire sideways typed passage and its three-part heading',r'Complete typed passage',r'Only a French editorial synopsis, including B=(Gr-stacks), B(0), D_n and N',r'Complete English type and three-part heading as in reading.tex',
    'All five prose lines are recoverable. Rules are immediately beneath B, D and N; a caret is directly above the isolated B and another is raised after the closing parenthesis of B(0/O). The type says Gr-stacks and component-wise. There is no handwritten replacement within the type.', 'high',False,True,'omission',[105,65,452,1455],1)
add('B03','Second typed prose line, joined words',r'amountsto',r'Not transcribed verbatim',r'amountsto',
    'The typewriter positions between amounts and to have the same character spacing as the letters inside the word, while adjacent word spaces are substantially wider. The joined form is retained; this explicitly resolves the contextual spacing question in favor of C.', 'high',False,True,'omission',[241,620,283,803],1)
add('B04','Last typed line, between n and underlined N',r'n\ \underline{\mathrm N}',r'n\in\underline{N} in the editorial synopsis',r'n\ \underline{\mathrm N}',
    'There is blank paper between the typed lower-case n and underlined capital N. No membership character is visible. The final full stop and closing parenthesis are both present.', 'high',False,True,'text not on the page',[397,1068,447,1173],1)
add('B05','Top, isolated tilded capital D',r'\widetilde{\unsure{D|\mathbb D}}',r'\widetilde D',r'\widetilde{\mathbb D}',
    'The complete stem has a separate inner upright ending just above the baseline, with a narrow white channel between it and the left stem. This is distinct from the single-stem D in the adjacent live D_n. The detached wave is a tilde.', 'high',True,True,'misread symbol or index',[650,82,751,181],2)
add('B06','Top, domain of the map',r'\unsure{N|\mathscr N}',r'\mathbb N',r'\unsure{\mathscr N|N}',
    'The letter has a broad ascending left sweep and a curved high right return, with no separate parallel stem establishing a doubled N. A script N is preferred, but the thick retracing does not settle script versus an embellished ordinary N.', 'medium',True,True,'misread symbol or index',[949,123,1039,199],2,True)
add('B07','Top map, gap between domain letter and mapsto',r'N-like letter directly followed by mapsto',r'\mathbb N\ni n\longmapsto',r'N-like letter directly followed by mapsto',
    'The mapsto bar begins just to the right of the single large N-like glyph. There is no intervening membership sign or lower-case n.', 'high',False,True,'text not on the page',[941,122,1122,205],2)
add('B08','Top map, canceled letter above live D_n',r'\deleted{\unsure{I_n|D_n}}',r'Omitted',r'\deleted{\unsure{I_n|D_n}}',
    'A long upper bar, upright and foot survive several diagonal cancellations; a bent low suffix remains at the right. The I-like framework is clearer than any rounded bowl, but the overstrike still permits an angular D. The C doubt is retained.', 'low',False,True,'omission',[1068,39,1159,137],2,True)
add('B09','Upper-left group of parallel maps',r'Three rightward arrows',r'Two rightward arrows',r'Three rightward arrows',
    'There is one upper bowed shaft, one straight middle shaft and one lower bowed shaft, each with its own right-facing head. Both D labels, their tildes and the single prime in n-prime were checked independently.', 'high',False,True,'drawing or diagram',[611,245,955,385])
add('B10','Under the downward arrow, n membership I',r'n\in\unsure{\mathbb I|I}',r'n\in I',r'n\in\mathbb I',
    'Two narrow separated upright stems run between the long horizontal top and bottom bars. The target letter is doubled, whereas the lower I beside ens has one stem. The membership sign opens to the right.', 'high',True,True,'misread symbol or index',[885,540,1109,618])
add('B11','Upper central map, canceled N before I',r'\deleted{\unsure{N}}',r'\struck{\mathbb N}',r'\deleted{N}',
    'The surviving left upright, descending diagonal and right upright give ordinary N; the additional oblique strokes pass across the whole letter as cancellation. They do not form a parallel doubled stem.', 'high',True,True,'misread symbol or index',[1394,264,1478,346],3)
add('B12','Upper central map, live target I',r'\mathbb I',r'I',r'\mathbb I',
    'A second lower upright is separated from the thicker right upright by a triangular white channel between the long top and bottom rules. The doubled appearance is present in the ink, unlike the later single-stem I.', 'high',False,True,'misread symbol or index',[1465,280,1533,346],3)
add('B13','Qualifier below strictement',r'\unsure{croissante}',r'croissante',r'croissante',
    'Initial cr, the closed o, the short i, joined double s, the a/n sequence, a tall crossed t and final e are recoverable. The word is not struck. The C doubt is resolved.', 'high',True,False,'misread word',[1250,397,1460,443],3)
add('B14','After image in the upper central qualifier',r'\unsure{est|=|\subset}',r'No intervening word/sign in the editorial description',r'\unsure{est|\subset}',
    'A low open e-like curve joins a long low stroke and a raised terminal hook. This favors the compressed word est; one subset-like curve remains possible. There are not two separated horizontal strokes for equals, so that candidate is removed.', 'medium',True,True,'omission',[1245,448,1465,515],3,True)
add('B15','Canceled qualifier below the upper image I',r'\deleted{\unsure{\in n}}',r'A struck \mathbb N described after image',r'\deleted{\unsure{\in n|<n}}',
    'The canceled material sits low as a subscript of the live I. An open curved mark and a low n-like turn survive under a diagonal stroke, before a separate live less-than-or-equal n. A membership-like form is preferred, but a less-than mark is also possible. It is not a separate full-size N.', 'low',True,True,'deletion state',[1530,481,1620,526],3,True)
add('B16','Sideways margin, first object and recurring object letter',r'\unsure{J|I}_{n\prime\prime}',r'Omitted',r'J_{n\prime\prime}',
    'After counterclockwise rotation the first object has a long upper bar and a descending right stem which returns into a left loop at the baseline. The middle and last objects share the hooked J construction. The first subscript has two distinct prime strokes.', 'high',True,True,'misread symbol or index',[2195,250,2277,373],11)
add('B17','Sideways margin, first arrow label',r'\unsure{u_\eta|u_g|u_y}',r'Omitted',r'u_{\unsure{\eta|g|y}}',
    'The u is clear. Its subscript has a small upper hook and a long descending sweep to the left; the upper closure is too thick to distinguish eta, g and y securely. The C alternatives are retained, with the uncertainty attached to the subscript.', 'medium',False,True,'omission',[2222,402,2293,472],11,True)
add('B18','Sideways margin, glyph above middle J',r'\unsure{\eta|y}',r'Omitted',r'\eta, using the first candidate of the preceding same-page doubt',
    'The same upper hook and long returning tail occur above the middle object. This local inspection does not settle the letter further. Its duplicate inline doubt is consolidated at B17, not claimed as a new resolution; no cross-page assertion was used.', 'medium',False,True,'omission',[2283,493,2336,540],11,True)
add('B19','Sideways margin, membership above middle J',r'\rotatebox{90}{\in}',r'Omitted',r'\rotatebox{-90}{\in}',
    'In the upright orientation the outer arch opens downward and its middle stroke points down into that opening. Positive 90 degrees would open upward, opposite to the visible sign.', 'high',True,True,'misread symbol or index',[2268,520,2318,559],11)
add('B20','Sideways margin, canceled label over second arrow',r'\deleted{\unsure{u_\eta|u_g}}',r'Omitted',r'\deleted{\unsure{u_\eta|u_g}}',
    'Several intersecting loops and a descending hook remain above the live u. A u and hooked subscript are compatible with the ink, but cancellation prevents a secure local distinction. The alternatives remain in place.', 'low',False,True,'omission',[2235,657,2310,751],11,True)
add('B21','Sideways margin, live second arrow label',r'\unsure{u_\xi|u_f}',r'Omitted',r'\unsure{u_\xi|u_f}',
    'A clear u is followed by a narrow winding descender that crosses the arrow shaft. Its upper turn favors xi, but the long descending stem also permits f. This is a local uncertainty independent of the canceled label above.', 'medium',False,True,'omission',[2209,671,2261,741],11,True)
add('B22','Sideways margin, label on the slanting lower arrow',r'\unsure{u}',r'Omitted',r'\unsure{u}',
    'Two broad rising and returning strokes lie along the oblique shaft. They can be read as u, but the label and shaft retrace each other and no additional subscript can be recovered securely. No unreadable-word count is invented.', 'low',False,True,'omission',[2130,641,2197,788],11,True)
add('B23','Sideways margin, glyph above last J',r'\unsure{\xi|x}',r'Omitted',r'\unsure{\xi|x}',
    'The upper small contour has more than one turn and a descending crossing. It favors xi, but the crossings do not securely separate a winding letter from an overwritten x. The local alternatives are retained.', 'low',False,True,'omission',[2279,775,2340,817],11,True)
add('B24','Sideways margin, membership above last J',r'\rotatebox{90}{\in}',r'Omitted',r'\rotatebox{-90}{\in}',
    'This sign was checked separately from the middle one: its outer curve is an arch open downward in the rotated reading orientation, with an inner downward stroke. The visible opening again requires negative 90 degrees.', 'high',True,True,'misread symbol or index',[2256,795,2314,848],11)
add('B25','Sideways margin, canceled subscript at last J',r'\deleted{\unsure{n\prime}}n',r'Omitted',r'\deleted{\unsure{n\prime}}n',
    'A compressed older low hump and a short high stroke are crossed before a separate live n-like hump. The first group may be n-prime, but its tick is entangled with the cancellation. The doubt is retained.', 'low',False,True,'omission',[2197,798,2251,875],11,True)
add('B26','Sideways margin, endpoint under the last J',r'\unsure{\xi|x|f}',r'Omitted',r'\unsure{\xi|x|f}',
    'A heavy winding upper contour crosses a long descending stem at the end of the lower arrow. Xi best preserves the multiple turns; x and f remain possible locally because the shaft intersects the glyph.', 'low',False,True,'omission',[2085,789,2200,849],11,True)
add('B27','Sideways margin, unfinished composite',r'u_\xi u_\eta=',r'Omitted',r'u_\xi u_\eta=',
    'The first subscript has a winding descender, the second a longer hooked tail, followed by two equal-sign strokes. The page remains blank to the right in the reading orientation; no right member is supplied. This explicitly confirms C’s contextual doubt about incompleteness.', 'high',False,True,'omission',[2147,1033,2264,1200],11)
add('B28','Upper-right numerical display',r'2^2 followed by one long dash, then +2^n; next line ends =',r'+\cdots+2^n and no final equals',r'2^2\ \text{---}\ +2^n; =(1+2)^n=',
    'One horizontal continuation stroke follows the 2-squared term; no preceding plus and no row of separate dots is present. The last visible sign after (1+2)^n is an equals with blank paper after it. The exponent 1, coefficient, denominator 2 and other exponents were independently checked.', 'high',False,True,'misread symbol or index',[1495,84,2281,291])
add('B29','Right-center x/y array, two horizontal comparisons',r'x\prime\prime<x\prime; y\prime\prime<y\prime',r'x\prime\prime\leq x\prime; y\prime\prime\leq y\prime',r'x\prime\prime<x\prime; y\prime\prime<y\prime',
    'Each relation consists of two joined diagonal/horizontal arms meeting at the left, with no separate lower equality bar. The single and double primes are separate short upright strokes.', 'high',False,True,'misread symbol or index',[1725,725,1970,871],10)
add('B30','Right-center array, canceled vertical material between x-double-prime and y-double-prime',r'Live headless connector with a deleted uncertain equals label',r'Omitted',r'\deleted{\unsure{\downarrow|=}} in the intervening position; no separate live connector',
    'The vertical stem and dark lower triangular tip are crossed by several short bars and obliques. They favor a canceled downward arrow, while an underlying equals remains possible. There is no independently surviving second live vertical line beside this canceled cluster.', 'low',True,True,'deletion state',[1740,768,1796,816],10,True)
add('B31','Right-center array, canceled letter above live tilded D',r'\deleted{\unsure{D}}',r'Omitted',r'\deleted{\unsure{D}}',
    'An upright and outer bowl-like contour survive the cross-striking above the live tilde. The diagonal overstrike creates a second lobe, so D is possible but not fully secure. No index is recoverable there. The C doubt is retained.', 'low',False,True,'omission',[2033,703,2105,767],10,True)
add('B32','Right-center array, live D subscript',r'\widetilde D_n',r'\widetilde D_{\ill{}}',r'\widetilde D_n',
    'The live low suffix is a short two-part n-shaped turn immediately to the lower right of D. It is separate from the canceled letter above. The tilde and both membership signs on the two rows are visible.', 'high',False,True,'readable ink left as \\ill{}',[2018,758,2101,819],10,False,'yes')
add('B33','Right-center array, headless right verticals and low n-prime',r'Two headless vertical links and n-prime',r'No vertical links or low n labels',r'x\prime--y\prime--n\prime, with gaps at the letters and no arrowheads',
    'The upper thick vertical segment stops above y-prime; a separate thinner segment below y-prime stops before n-prime. Neither has an arrowhead. The source does not identify the relations further.', 'high',False,True,'drawing or diagram',[1889,753,1962,983],10)
add('B34','Right-center paired arcs and n-double-prime label',r'n-double-prime in a detached array row, followed by separate unlabelled arcs',r'Omitted',r'Two arcs, with n-double-prime crossing the upper arc',
    'The n-double-prime is written on the upper/right bowed stroke, not horizontally aligned with n-prime. The two arc ends remain separated. A small local rise near the n can belong to its initial stroke; no independent arrowhead is asserted. C geometry is retained except for attaching the label to the actual arc position.', 'high',True,True,'drawing or diagram',[1688,864,1834,1036],10)
add('B35','Right-center blank area, paired dots below the array',r'Two separate filled dots',r'Omitted',r'Two separate filled dots',
    'Two small dark points are vertically separated and detached from the bowed strokes and formulas. They are kept as graphic points without a linguistic or mathematical interpretation.', 'high',False,True,'drawing or diagram',[2023,1005,2050,1083])
add('B36','Middle-left first prose line',r'I\ \unsure{ens}\ ordonné',r'I un ordonné',r'I ens ordonné',
    'After the single-stem I is a small initial e-loop, a low n hump and a long final s-like sweep, matching the contractions elsewhere on this page. The last word has a detached accent over its ending. The source does not read un.', 'high',True,True,'misread word',[619,724,1104,794],4)
add('B37','Middle-left second prose line, word after the map',r'\unsure{famille|échelle} d\prime ens',r'famille d\prime ens.',r'famille d\prime ens',
    'The initial has a long looped ascender and descending f-stem; two later l ascenders are visible. This resolves famille and rejects échelle as well as the older contextual guess about symbole. There is no full stop after ens.', 'high',True,True,'misread word',[929,810,1251,901],4)
add('B38','Middle-left second prose line, final word and comma',r'\unsure{ordonnés} ,',r'ordonnés without comma',r'ordonnés ,',
    'The initial o/r, tall d, joined n sequence and final low ending are recoverable; a small detached accent stands above the end. A separate comma follows the word. The C word doubt is resolved.', 'high',True,True,'misread word',[1273,808,1550,866],4)
add('B39','Direct map to I, older loop under the live label',r'\deleted{\unsure{\phi}}',r'Omitted',r'\deleted{\unsure{\phi}}',
    'An older oval contour straddles the tall upright and remains visible to its left and upper right beneath the new arms. Phi is plausible but the overlap prevents a secure chronology or complete old outline. The C doubt is retained as an overwritten older form.', 'low',False,True,'omission',[681,905,722,977],5,True)
add('B40','Direct map to I, live label',r'\unsure{k_n|\kappa_n|\tau_n}',r'\tau_n',r'k_n',
    'The live letter has a tall upright and two right-hand arms, the lower arm descending separately, followed by a low n. It does not have the single upper bar and hooked stem of tau. The later defining occurrence independently shows the same k form.', 'high',True,True,'misread symbol or index',[683,905,747,978],5)
add('B41','Si line, first canceled word',r'\unsure{Soit|Sinon}',r'soit',r'\unsure{Soit|Sinon}',
    'A large leading S and a detached short high mark remain; the low middle letters have been largely merged into the cancellation rule. Soit is favored, but the surviving low run does not exclude Sinon. The following l-apostrophe-ens has no full stop.', 'low',False,True,'deletion state',[875,1059,1164,1130],6,True)
add('B42','Si line, final canceled capital',r'\unsure{K}',r'\ill{}',r'K',
    'A complete tall stem and two distinct right arms survive the horizontal cancellation. The capital K is readable. No word count is needed.', 'high',True,True,'readable ink left as \\ill{}',[1228,1062,1293,1122],6,False,'yes')
add('B43','Named subset before n-prime,n',r'\unsure{\mathscr L|\Phi|L}',r'\Phi',r'\Phi',
    'The upper rounded contour forms a left open lobe and right closed lobe around a descending central stem; that stem meets a broad horizontal foot. This is a phi-shaped capital, not a tall ascending L loop. The same construction is separately visible in the canceled line below. The subscript is n-prime, comma, n.', 'medium',True,False,'misread symbol or index',[1454,1051,1617,1130],7)
add('B44','Defining set, map applied to x',r'\unsure{k_n|\kappa_n|\tau_n}(x)=n\prime',r'\tau_n(x)=n\prime',r'k_n(x)=n\prime',
    'Here the letter is uncanceled: a tall straight stem has an upper right arm and a detached descending lower right arm, with low n after it. The tall k form is clearer here than on the overwritten arrow. Parentheses, equality and final prime are all present.', 'high',True,True,'misread symbol or index',[1690,1183,1923,1249],7)
add('B45','Canceled Soit x membership line',r'\deleted{Soit x\in\mathscr L_{\unsure{n\prime}},}',r'\struck{Soit x\in\Phi_{n\prime}}',r'\deleted{Soit x\in\Phi_{n\prime},}',
    'The same round capital with central descending stem is visible above the rule. The subscript has a low n and a short separate upward prime after it; a detached comma lies below and to the right. The prime doubt is resolved. The strike runs through the whole phrase.', 'high',True,True,'misread symbol or index',[660,1247,1095,1325],8)
add('B46','Bottom prose opening',r'\unsure{Considérons} l\prime ens',r'Considérons l\prime ens.',r'Considérons l\prime ens',
    'The initial C, joined onset, dotted i, tall d and detached acute are present; the low ending and explicit l-apostrophe-ens are recoverable. There is no final stop after ens. The C word doubt is resolved.', 'high',True,True,'misread word',[592,1330,1112,1400],9)
add('B47','Bottom prose, heavily canceled D-like group',r'\deleted{\unsure{\widetilde D_{n\prime}|D_n}}',r'\struck{\ill{}}',r'\deleted{\unsure{\widetilde D_{n\prime}|D_n}}',
    'An upright/bowl outline, possible upper wave and low n-like suffix survive several diagonal strokes. The high suffix stroke is entangled with the cancellation, so n versus n-prime and the tilde remain unresolved. C’s alternatives are retained.', 'low',False,True,'readable ink left as \\ill{}',[1236,1298,1354,1400],9,True,'yes')
add('B48','Bottom prose, large final capital',r'\unsure{B|\mathscr B}',r'Omitted',r'\unsure{B|\mathscr B}',
    'Two large rightward bowls meet a tall left upright; the lower bowl ends across a small gap near the stem. Several contours are retraced. B is secure as the letter, but ordinary versus script treatment cannot be settled from this emphatic form. The C alphabet doubt is retained.', 'medium',False,True,'omission',[1419,1303,1550,1417],9,True)
add('B49','Bottom chain, central F_1',r'\mathbb F_1',r'F_1',r'\mathbb F_1',
    'The central F has two distinct upright lines with visible white space and separate returning upper strokes. F_0 and F_2 have single principal stems in their own occurrences. Each pair of arrows points left; both arrowheads in each pair were checked.', 'high',False,True,'misread symbol or index',[940,1437,998,1520])
add('B50','Lower-right x-prime over y-prime sketch',r'x\prime with headless vertical link to y\prime',r'Omitted',r'x\prime with headless vertical link to y\prime',
    'A thin vertical segment lies between the two primed variables, with clear gaps at both labels and no arrowhead. The y has a curled lower return. The source is not an equality sign.', 'high',False,True,'drawing or diagram',[1641,1348,1719,1545])
add('B51','Loop beside the final display; H actual drawing checked',r'TikZcd loop at x, without the short lower endpoint returns',r'H_drawing.tex closes the curve on one filled base point',r'Open loop contour beside x, upper inward arrowhead, separate lower start with short returns; no base dot',
    'The upper arrowhead and lower start are separated by a visible vertical gap. The x is detached to their left. The lower start has a short upright projection and a small leftward return. H’s drawing explicitly places a filled node at a single shared start/end coordinate, which is not the source geometry. Its editorial prose is not counted as a second discrepancy.', 'high',True,True,'drawing or diagram',[790,1536,951,1638],12)
add('B52','Small lower-right arrow, point and oblique segment',r'Curved arrow between filled knots, detached point, plain lower segment',r'Omitted',r'Same sketch, with a short downward return at the left end of the lower segment',
    'The lower-left knot is filled, the upper knot is solid with two arrowhead returns, and the separate right point is detached. No enclosed white counter is visible in either knot; the white below the top knot opens to the arrowhead gap. The low oblique stroke has a short downward turn at its left end, omitted by C.', 'high',True,True,'drawing or diagram',[1872,1244,2083,1415],13)
add('B53','Final display, subscript of F',r'F_{\unsure{*|x}}',r'F_*',r'F_*',
    'The low mark has several short projections around a crossing, distinct from the following clearly two-stroke x. The long down-curving comma is separate on its right. The C star/x doubt is resolved as star.', 'high',True,False,'misread symbol or index',[1125,1545,1211,1608],14)
add('B54','Final display, abbreviation after equals',r'\unsure{ens}',r'ens.',r'ens',
    'A low e-like opening, n hump and final s-like sweep form the same contraction seen above. There is no following period before des. The C abbreviation doubt is resolved without expanding it.', 'high',True,True,'abbreviation expanded or spelling modernised',[1319,1543,1418,1595],14)
add('B55','Final display, word after des',r'\unsure{classes}',r'\uncertain{classes}',r'\unsure{classes}',
    'An initial c-like loop merges with a tall l, followed by a compressed low run and terminal s-like ending. Classes remains the best reading, but the internal joined strokes do not establish every letter. Both witnesses mark this word as doubtful, and the doubt is retained.', 'medium',False,False,'misread word',[1540,1517,1678,1590],14,True,'yes')
add('B56','Final display, apostrophized word before final des',r'd\prime\unsure{hom.topie|homotopie} des',r'de lacets, omitting the homotopy phrase',r'd\prime hom.topie. des',
    'After d-apostrophe, a tall h and compressed om run are followed by a distinct detached dot, then a tall crossed t and the opie ending. The internal dot is ink, so hom.topie is retained as the written abbreviation. The following des and the next-line lacets are separate.', 'high',True,True,'omission',[1705,1519,1995,1590],14)
add('B57','Final display, stop after hom.topie',r'No final stop',r'Phrase omitted',r'hom.topie.',
    'A detached low dot follows the ending of topie and precedes a substantial gap before des. It is separate from the higher dot of the i. The terminal stop is retained in addition to the internal abbreviation dot.', 'high',True,True,'omission',[1955,1532,1999,1586],14)
add('B58','Final display, lower line',r'\unsure{lacets} en x',r'lacets en x',r'lacets en x',
    'The tall looped l, low a/c/e sequence, tall crossed t and short terminal s are recoverable, followed by en and an unprimed x. The C word doubt is resolved.', 'high',True,False,'misread word',[1310,1585,1615,1635],14)
add('B59','Middle-left, isolated point before n mapsto',r'Omitted',r'Omitted',r'A literal small point before n, without algebraic interpretation',
    'A discrete dark point sits just left of n, below its midline, separated from the letter by blank paper. It is preserved as a point, not interpreted as multiplication or a word.', 'high',True,True,'omission',[608,851,674,885],4)
add('B60','Blank space left of the downward map',r'Omitted',r'Omitted',r'Short detached horizontal pen stroke',
    'A short dark horizontal stub is visible on the left half near y=522, apart from the formulas and pale background traces. Its function is unassigned.', 'medium',True,True,'drawing or diagram',[550,515,577,530])
add('B61','Blank space below the downward map',r'Omitted',r'Omitted',r'Detached small point and a separate short almost horizontal stroke',
    'The half shows a small point to the upper left of a short horizontal dark stroke below the downward map. The marks do not form a recoverable word or formula and are traced literally.', 'medium',True,True,'drawing or diagram',[831,659,921,686])
add('B62','Bottom blank space left of the loop',r'Omitted',r'Omitted',r'Two short detached angled pen strokes',
    'The left half shows a small low angled stroke and a separated rising stroke beside it, to the left of the loop. Their origin and function are not assigned; no unreadable-word count is used.', 'medium',True,True,'drawing or diagram',[674,1576,711,1599])
add('B63','Direct map qualifiers, contextual abbreviation check',r'str. croiss.; image; single-stem I',r'str. croiss.; image; I',r'str. croiss.; image; single-stem I',
    'Both abbreviation stops are discrete low points. The source writes image without an added verb in this lower occurrence. The target I and the later I with subscript less-than-or-equal n each have a single main stem. This resolves the contextual distinction from the doubled upper I forms without changing either witness here.', 'high',False,False,'other',[890,914,1735,1008])


add('B64','Subset definition, two levels and vertical equals',r'Vertical equals between the named subset and brace definition',r'Inline horizontal equals after a comma',r'Named subset above the brace definition, joined by a vertically oriented equals',
    'Two short parallel vertical strokes stand below the named subset and above the left part of the brace expression. The top line ends after D_n without a written comma. H flattens this arrangement into an inline horizontal equals; the source orientation and vertical placement are retained.', 'high',False,True,'insertion or placement',[1435,1028,1970,1280],7)

inventory=[]
def inv(element,kind,box,words,hand='his hand'):
    inventory.append({'element':element,'kind':kind,'position':f'whole-image bbox {box}','first_words_or_objects':words,'sheet_kind':'reused_typed','hand':hand,'transcribed':'yes'})
inv('Typed English paragraph','text',[183,65,452,1455],'commutes not only with arbitrary projective limits','typewriter, author unattributed from this image')
inv('Typed three-part heading','display',[119,589,179,1195],'underlined B=(Gr-stacks); hatted underlined B; underlined B(0/O) with raised caret','typewriter, author unattributed from this image')
inv('Canceled old target above first map','deletion',[1068,39,1159,137],'I_n / D_n')
inv('Separate tilded D','display',[650,82,751,181],'doubled D with detached tilde')
inv('Upper-right calculation','display',[1495,84,2281,291],'1+n . 2^1 + ... ; =(1+2)^n=')
inv('First assignment','display',[949,120,1230,215],'N-like letter mapsto tilded D_n')
inv('Sideways marginal chain and composite','margin note',[2085,235,2345,1218],'J_n-double-prime to J_n-prime to J_n; u_xi u_eta=')
inv('Three parallel maps','diagram',[611,245,955,385],'tilded D_n-prime to tilded D_n, three arrows')
inv('Independent downward map','diagram',[873,389,1114,620],'tilded D_n down to n in doubled I')
inv('Diagram inside sideways margin','diagram',[2085,235,2345,886],'J_n-double-prime to J_n-prime to J_n, with witnesses and lower slanting arrow')
inv('Unfinished display inside sideways margin','display',[2147,1033,2264,1200],'u_xi u_eta=')
inv('Upper central level map','display',[1065,254,1840,357],'d_n in tilded D_n to canceled N and doubled I; d_n mapsto n')
inv('Canceled upper N','deletion',[1394,264,1478,346],'N')
inv('Three qualifier lines','text',[1245,351,1680,540],'strictement; croissante; image est/subset I')
inv('Canceled upper image subscript','deletion',[1530,481,1620,526],'in n / less-than n')
inv('Short isolated stub','drawing',[550,515,577,530],'one short horizontal dark stroke')
inv('Right-center map','display',[1744,558,2069,656],'tilded D_n-prime to tilded D_n')
inv('Isolated point and stroke','drawing',[831,659,921,686],'point plus separate nearly horizontal stroke')
inv('Canceled second margin arrow label','deletion',[2235,657,2310,751],'u_eta / u_g')
inv('Right-center x/y array','diagram',[1715,702,2105,983],'x-double-prime < x-prime; y-double-prime < y-prime; memberships and vertical strokes')
inv('Canceled D above array target','deletion',[2033,703,2105,767],'D-like capital')
inv('Ordered-set text','text',[619,724,1104,794],'I ens ordonné')
inv('Canceled left array connector','deletion',[1740,768,1796,816],'downward-arrow-like / equals cluster')
inv('Canceled last marginal index','deletion',[2197,798,2251,875],'n-prime before live n')
inv('Family text','text',[608,806,1555,905],'. n mapsto tilded D_n famille d-apostrophe-ens ordonnés ,')
inv('Paired arcs with n-double-prime','drawing',[1688,864,1834,1036],'two bowed strokes, n-double-prime on upper stroke')
inv('Direct map and abbreviated qualifiers','display',[560,895,1735,1018],'tilded D_n to I, k_n; str. croiss.; image I_less-than-or-equal n')
inv('Overwritten phi-like old label','deletion',[681,905,722,977],'phi-like loop under k_n')
inv('Detached pair of dots','drawing',[2023,1005,2050,1083],'two separate dark points')
inv('Conditional sentence','text',[550,1030,1735,1155],'Si n-prime less-than-or-equal n, canceled phrase, Soit')
inv('Named subset and vertical equality to its definition','display',[1435,1028,1970,1280],'Phi_n-prime,n subset tilded D_n; vertical equals; {x ... k_n(x)=n-prime}')
inv('Canceled opening after Si','deletion',[855,1045,1310,1155],'Soit/Sinon l-apostrophe-ens K')
inv('Lower-right arrow sketch','drawing',[1860,1230,2090,1430],'filled point, upward-curving arrow with upper knot, separate right point, low segment with left return')
inv('Canceled Soit membership sentence','deletion',[650,1235,1105,1330],'Soit x in Phi_n-prime,')
inv('Bottom prose and large B','text',[585,1298,1570,1425],'Considérons l-apostrophe-ens; canceled D-like group; B/script B')
inv('Canceled D-like group before B','deletion',[1236,1298,1354,1400],'tilded D_n-prime / D_n')
inv('Separate primed vertical pair','diagram',[1641,1348,1719,1545],'x-prime above y-prime with headless stroke')
inv('Bottom three-object chain','diagram',[778,1435,1175,1527],'F_0 leftleftarrows doubled F_1 leftleftarrows F_2')
inv('Loop beside final display','drawing',[790,1536,951,1638],'x; open loop contour; upper returning arrowhead; lower short endpoint returns')
inv('Final pi-zero display','display',[1030,1500,2110,1645],'pi_0(F_*,x)=ens des classes d-apostrophe-hom.topie. des; lacets en x')
inv('Small detached bottom pen mark','drawing',[674,1576,711,1599],'two short angled strokes')
inv('Archive sheet number','text',[42,1601,92,1659],'5, encoded as archive comment','unattributed archival hand')

import re
inventory.sort(key=lambda item: int(re.search(r'\[(\d+), (\d+),', item['position']).group(2)))

notation=[
 {'sign':'Typed B, D, N and argument 0/O','evidence':'Single typed capitals with separate underline rules. The parenthesized oval remains 0/O; later same-page type uses its first candidate without a duplicate doubt.'},
 {'sign':'D alphabet','evidence':'Only the isolated first D has a separately visible inner upright; neighboring D_n forms have single principal stems. No uniform doubled alphabet is imposed.'},
 {'sign':'N-like domain','evidence':'Curved sweep and heavy high return favor script N; ordinary embellished N remains possible. No double-stem structure is established.'},
 {'sign':'I alphabets','evidence':'The upper targets have separated upright contours, most clearly below the down arrow. The lower ordered-set I and direct-map I have a single main stem.'},
 {'sign':'k_n','evidence':'Tall upright and two right arms, clear in the defining set and visible through the overstrike above the map. n is a small low hump.'},
 {'sign':'Phi','evidence':'An upper rounded contour split by a descending central stem ending on a horizontal foot occurs in both the named subset and the canceled membership line.'},
 {'sign':'Margin J','evidence':'Long top bar, right descending stem and lower left return. The first has a closed lower return loop; the middle form has a more open foot.'},
 {'sign':'Margin eta-like and xi-like subscripts','evidence':'Eta-like forms have a hook and long returning tail; the middle occurrence is consolidated at the first uncertainty. The overwritten xi/x/f groups have distinct local ambiguities, kept at their individual loci rather than assumed identical. No other-page exemplar was used.'},
 {'sign':'Vertical membership','evidence':'Both sideways-note signs, after the note is turned upright, have downward-open arches and inner downward strokes; encoded with rotatebox -90 separately at both occurrences.'},
 {'sign':'ens; str.; croiss.','evidence':'ens has low joined humps and no visible stop in its four textual occurrences. str. and croiss. each have a discrete stop.'},
 {'sign':'Primes and star','evidence':'Single and double prime ticks are distinguished locally. The footer F subscript has several radial projections and is star, separate from the comma and following x.'},
 {'sign':'hom.topie.','evidence':'A detached internal dot follows hom, and a separate low terminal stop follows topie; neither is silently expanded to homotopie.'},
 {'sign':'Graphic endpoints and isolated marks','evidence':'Loop ends remain separated; no base dot is added. Lower arrow knots are solid with no enclosed white counters. Detached dots, short endpoint returns and isolated strokes are preserved without assigning functions.'}
]
notes=[
 'Landscape whole image is 2375 by 1690 pixels. The supplied halves are 1247 by 1690 and 1248 by 1690; full, a and b were each viewed exactly once before decision crops.',
 'H_drawing.tex explicitly identifies archive page 5 / PDF page 6, matching this scan packet. Its actual drawing was compared as code to the source loop; its editorial description was not counted again as a second discrepancy.',
 'The source is a visibly reused typed sheet with a complete sideways English paragraph at the left and handwritten notes elsewhere. Pale background impressions do not yield additional recoverable text and are not reconstructed.',
 'No manuscript folio, title or date is visible. A lighter archival 5 appears at the lower left and is retained only as an archive-sheet comment. H’s editorial section title and surrounding editorial note are not manuscript text.',
 'Observed content: tilded D objects and level maps into an ordered set, an unfinished arithmetic expansion, a named fiber-like subset defined by k_n(x)=n-prime, a chain F_0/F_1/F_2, and a pi-zero description using lacets. This is a description of what is written, not a proof or validation of the mathematics.',
 'The arithmetic display ends with =(1+2)^n= and the sideways composite ends with u_xi u_eta=. Both right sides are blank in the source. The typed final line has n followed by underlined N without a membership sign. These are preserved as written.',
 'No explicit verbal author doubt was found. Readable cancellations and superpositions are recorded. The apparent old phi under k_n and several marginal labels remain locally uncertain; their exact chronology is not claimed beyond the visible overwritten state.',
 'The packet originally contained one stray doubt-table row explicitly about scan 7; the main reader corrected the packet. That row and all cross-page witness assertions were excluded as evidence. No other page or reader file was opened.',
 'No OCR, recognition software, web research, parallel text, rendering or compilation was used. Pillow operations were crop, the recorded right-angle rotations, autocontrast at cutoff zero and LANCZOS resizing; no sharpening was applied.',
 'Mathematics was not used as a corrective authority. No proof, re-proof or computational certificate was performed, so checks is empty.'
]
report={'scan':6,'reader':'B','model':'GPT-6 Astra Pro','effort':'inherited / not exposed','started_utc':'2026-11-20T11:11:46Z','finished_utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
 'views':[str(source/'H104-01_104_scan006.jpg'),str(source/'H104-01_104_scan006_a.jpg'),str(source/'H104-01_104_scan006_b.jpg')]+[p['path'] for p in proc['processing']],
 'issues':issues,'inventory':inventory,'notes':notes,'notation':notation,'checks':[],'crop_count':len(crops),
 'brief_feedback':'The scope, header check and once-only view rules were sufficient. A stray scan-7 row initially present in the supplied C context needed exclusion after the main reader’s correction. An explicit allowance for locally different ambiguities in overwritten repetitions would make the first-occurrence-only doubt rule easier to apply without suppressing distinct uncertainties.'}
(root/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote report: {len(issues)} issues, {len(inventory)} inventory elements, {len(crops)} crops.')
