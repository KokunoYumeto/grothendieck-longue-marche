from pathlib import Path
import json, re

root = Path('/workspace/scratch/15c7af26487b/edition')
page = '148_scan018'
packet = (root/'packets'/f'{page}.md').read_text()
tex = (root/'work'/f'{page}.tex').read_text()
C = packet.split('## Witness C')[1].split('## Witness H')[0].split('```tex')[1].split('```')[0].strip()
H = packet.split('## Witness H')[1].split('```tex')[1].split('```')[0].strip()
cfig = re.findall(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}', C, re.S)
fig = re.findall(r'\\figure\{\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}\}', tex, re.S)
assert len(cfig) == len(fig) == 8
omega = tex.split('% F1:')[1].split('\\diagram{')[0]
omega = omega[omega.index('\\margin{'):].strip()
rep = re.search(r'\\diagram\{\\begin\{tikzcd\}.*?\\end\{tikzcd\}\}', tex, re.S).group()

boxes = {
 'top_counts':[189,25,1442,172], 'gray_tetra':[285,182,680,523],
 'red_tetra':[862,139,1222,434], 'verso':[1222,193,1528,416],
 'counts_formula':[968,452,1384,635], 'upper_sphere':[112,609,513,983],
 'green_tetra':[691,510,1190,892], 'diagonal_note':[1173,688,1527,899],
 'tetra_line':[870,976,1527,1055], 'bipantal':[871,1018,1528,1177],
 'pantal':[868,1147,1528,1355], 'omega':[690,947,861,1197],
 'small_sphere':[49,1012,326,1314], 'pants':[512,1052,691,1193],
 'left_note':[37,1328,434,1648], 'large_tetra':[132,1242,1061,1905],
 'paths_heading':[850,1340,1529,1425], 'paths_ab':[1069,1414,1530,1598],
 'paths_cd':[1080,1582,1530,1762], 'paths_efg':[881,1737,1530,2007],
 'footnote':[619,2007,1521,2224], 'bottom_sphere':[280,1931,536,2198],
 'footer':[30,2130,114,2212], 'green_attachment':[780,850,1184,987]
}
changes=[]
def change(place, c, h, final, evidence, crop, confidence='high', kind='misread word', sheet='Words', dc=False, dh=True, mh=False, consequential=False):
    ident=f'{page}-{len(changes)+1:02d}'
    changes.append(dict(id=ident,place=place,C=c,H=h,final=final,evidence=f'{evidence} Evidence: {page}_{crop}.png, original box {boxes[crop]}.',crop=f'{page}_{crop}.png',box=boxes[crop],confidence=confidence,kind=kind,error_sheet_kind=sheet,differs_C=dc,differs_H=dh,marked_in_H=mh,consequential=consequential))
    return ident

ids={}
ids['top']=change('first count line, retraced addend',r'$+6$ sommets',r'$+$ \struck{6} 6 sommets',r'$+\unsure{6}$ sommets','One heavily retraced 6 occupies the addend position. Its overlapping strokes do not expose a second adjacent canceled 6. The graphic state remains doubtful; the primary digit is unchanged from C.','top_counts','medium','deletion state','Struck text')
ids['gray']=change('upper-left pencil drawing',cfig[0],r'\drawing{un tétraèdre au crayon aux sommets tronqués par de petits cercles}',fig[0],'The pencil drawing exposes a truncated top cone/oval with projecting tips, two lower rings with angular inner strokes, an open/retraced right ring, a broken rear diagonal, a bowed heavy middle bar with small under-returns and a rising right branch, and faint curved interior traces. C adds a regular hatch sequence coinciding with the printed listing band. H gives only a broad description and makes no corresponding hatch claim.','gray_tetra','medium','drawing or diagram','Drawings and diagrams',True,False)
ids['red']=change('upper-right red-and-black drawing',cfig[1],r'\drawing{un tétraèdre à l’encre dont la subdivision barycentrique est tracée en rouge}',fig[1],'The crop exposes six separate substantial black interior marks, five red junctions, unequal thin links and overtraced corner loops. A short separate black oblique stroke lies beside the right corner on its inward red link. C regularizes the corner loops and omits this short stroke; H does not record the interior point marks. No interior written labels are exposed.','red_tetra','high','drawing or diagram','Drawings and diagrams',True,True)
ids['verso']=change('upper-right note',r'mieux cf verso (subdivision barycentrique)',r'mieux, cf.\ \uncertain{verso} (subdivision barycentrique)',r'mieux cf verso (subdivision barycentrique)','The note has mieux on the first baseline, cf verso on the next, and the parenthetical subdivision barycentrique below. No attached comma after mieux or secure baseline point after cf is exposed. Tiny detached specks near the long f return are not assigned punctuation.','verso')
counts=r'\begin{aligned}s_0&=4+6+\unsure{4}.3=22\\s_1&=12+4.\unsure{9|8}=\unsure{48}\\s_2&=4.7=28\end{aligned}'
ids['counts']=change('three displayed counts',r's_0=4+6+4.3=22; s_1=12+4.\unsure{9|8}=48; s_2=4.7=28',r's_0=4+6+\struck{4}\,3=22\quad\struck{\ill{}}; s_1=12+4.\struck{9}\ldots=\struck{4}\,8\ldots; s_2=4.7=28',counts,'The 4 before 3, the two-loop 9/8 factor with a heavy right/down return, and the result 48 have superimposed/retraced strokes. The crop does not isolate H’s additional canceled material or ellipsis marks. Preserve the factor and state doubts, the low product points, and the written results without repairing them. No arithmetic is used to choose the factor.','counts_formula','low','deletion state','Struck text',False,True,True,True)
ids['upper']=change('upper large sphere',cfig[2],r'\drawing{les pôles en rouge, des points noirs sur l’équateur, et de petits hexagones de points autour de deux sommets de l’équateur et d’un point du méridien central}',fig[2],'The three small contours have irregular bends, gaps and four prominent filled corner marks apiece; additional bends are unfilled. Three substantial isolated black marks lie at rear-left, front-center and rear-right; the poles are red. The red transverse strokes have unequal ends, the right-sector pencil strokes are slanted and interrupted, and lower arcs are separate/retraced. C substitutes clean circles, changes pole color and collapses point/contour detail; H’s hexagones de points does not determine six filled marks.','upper_sphere','medium','drawing or diagram','Drawings and diagrams',True,True)
ids['green']=change('central coloured tetrahedron and attached oblique links',cfig[3],r'\drawing{un tétraèdre à l’encre verte et brune : deux arêtes opposées repassées en noir, l’arête cachée en pointillé vert ; un trait noir épais joint les milieux de deux arêtes opposées et deux traits verts épais le relient au sommet du haut et au sommet du bas ; du sommet du bas part une flèche vers la note de la marge droite.}',fig[3],'The hidden diagonal has separated brown dashes; the green dotted graph and its two inner junctions are separate. Thick green lines are partly overtraced in black. In addition to the outward curved arrow, a black oblique shaft starts above/before the t in the following heading and reaches the dark lower vertex with a visible lower return. Its previously clipped start is documented by the sole completion crop green_attachment [780,850,1184,987]. The observed return is drawn without forcing an ideal arrowhead.','green_tetra','high','drawing or diagram','Drawings and diagrams',True,True)
ids['power']=change('diagonal note, whole opening formula',r'ça fait $2^4-1=15$',r'ça fait $2^{4}-1=15$',r'ça fait $2^{\unsure{9|4}}-1=15$','The exponent has a closed upper loop with a descending right stem. It strongly resembles 9; a closed 4 remains possible. The nearby exposed heading 4 has an open angular form, but its larger size does not settle this small glyph. The written 15 is preserved; arithmetic does not choose the exponent.','diagonal_note','medium','misread symbol or index','Symbols and indices',True,True,False,True)
ids['poss']=change('diagonal note, second baseline, first word',r'\unsure{possibilités|positions}',r'positions','possibilités','The long word exposes the medial b and following -ilités sequence; it extends beyond the shorter positions reading. Resolving C’s primary word is certainty-only against C.','diagonal_note')
ids['inversion']=change('diagonal note, second baseline, following word',r"\unsure{d'inversion|limites}",r'\uncertain{limites}',r'\unsure{inversion|limites}','The exposed word resembles inversion, beginning with a short dotted upright and connected low strokes. No separate leading d or apostrophe can be securely isolated. Interior compressed strokes remain open, so the candidate is not resolved.','diagonal_note','low','misread word','Words',True,True,True)
ids['faces']=change('diagonal note, middle baseline',r'\unsure{des faces choisies|invariantes possibles}',r'\uncertain{invariantes} \uncertain{possibles}','des faces choisies','The short des, looped/descending f and -aces, then the tall h and -oisies sequence are visible as three groups. C’s primary reading is retained with resolved certainty.','diagonal_note','high','misread word','Words',False,True,True)
ids['vue']=change('diagonal note, final two baselines',r'\unsure{en des bords|\illegible{3} de vue} !',r': \ill{} \ill{} \ill{} de vue !',r'\unsure{en} \illegible{2} \unsure{de} vue !','Final vue and the exclamation mark are exposed. Before them, the first short group is compatible with en, two intervening groups remain undeciphered, and the last short group resembles de. No settled en des bords phrase or detached colon is exposed. The partial readings remain locally marked.','diagonal_note','low','misread word','Words',True,True,True)
ids['tetra']=change('second point, final word and marginal continuation',r'\unsure{orientation|orientations} des faces',r'orientations \marginal{des faces}',r'\unsure{orientation|orientations}\margin{des faces}','The final n/s strokes of orientation(s) crowd the right edge above the descending marginal continuation des faces. The ending remains unresolved. The continuation is offset at the right on the lower baseline, as H locates it; C runs it into the main line.','tetra_line','medium','insertion or placement','Insertions put in the wrong place',True,True)
ids['pantaln']=change('third point, raised addition and main noun',r'\inserted{bi}\unsure{pantaloniques}',r'\supplied{bi}pantalonniques',r'\inserted{bi}pantaloniques','Raised b and dotted i sit immediately before/above the initial p with a curved attachment stroke. After lo there is one n arch, then the short i and q descender. The same o–n–i–q sequence recurs in the fourth point; there is no separately exposed second n arch.','bipantal','high','misread word','Words')
ids['opposees']=change('third point, right marginal word',r'\unsure{opposées|appariées}',r'\marginal{opposées}',r'\margin{opposées}','The word is offset downward at the right of the first baseline, crowded by a punch hole. Its opening rounded o, p descenders and ending -sées support opposées. Its marginal attachment, already represented by H, is retained.','bipantal','high','insertion or placement','Insertions put in the wrong place',True,False)
ids['ceinture']=change('third point, first parenthesis','maillot ceinturé','maillot ceinture','maillot ceinturé','The ending has an exposed raised acute accent on é. Both l strokes of maillot are also visible.','bipantal')
ids['codiagonale']=change('third point, lower parenthesis','carrée $+$ codiagonale','carrée $+$ 1 diagonale','carrée $+$ codiagonale','A continuous co opening joins the d and the rest of codiagonale; there is no independent numeral 1. The full parenthetical expression is visible.','bipantal')
ids['jparen']=change('third point, end of lower continuation',r'repère de $J$)',r'repère de $J$',r'repère de $J$)','The source has a separate curved closing mark after J on the lower continuation. It is preserved without supplying an opening parenthesis.','bipantal','high','omission','Omissions')
ids['guingois']=change('fourth point, second baseline',r'de \unsure{quasi-gois|quasi-gss|genre gois}',r'de genre $0$','de guingois','The first character has a closed loop and descender, followed by u, dotted i and n; a second g precedes -ois. The left-note recurrence exposes the same sequence with an intervening short horizontal hyphen. Here no separate hyphen is exposed. No independent quasi prefix or numeral 0 appears.','pantal','high','misread word','Words',True,True,True)
ids['tour']=change('fourth point, parenthesis',r'(quart de \unsure{sorte|tore|tour})','(quart de sorte)','(quart de tour)','The second word has a tall t, connected o/u and terminal r; the same tour sequence is exposed in the sixth-turn path below. C’s third alternative is retained.','pantal','high','misread word','Words',True,True)
ids['relation']=change('fourth point, relation before carré',r'($\simeq$ carré',r'(\struck{\ill{}} carré',r'(\unsure{$\simeq|=$} carré','The relation has two thick horizontal/retraced elements with a bowed upper stroke. A separate readable canceled expression cannot be isolated; the relation identity and source state remain doubtful. C’s primary relation is retained.','pantal','low','deletion state','Struck text',False,True,True)
ids['ieparen']=change('fourth point, two-line final parenthesis',r'orientation de $I$ i.e. de $J$ $\simeq$ repère de $J$)',r'orientation de $I$ i.e.\ de $J$ $\simeq$ repère de $J$)',r'orientation de $I$ i.e.)\par de $J$ $\simeq$ repère de $J$)','A long exposed closing curve follows i.e. at the right edge, above the continuation de J ≃ repère de J). Both visible closing marks are preserved. No parenthesis is supplied or moved to make a paired expression.','pantal','high','omission','Omissions',True,True)
ids['omega']=change('small formula left of the point list',r'\omega_I\unsure{={}^{6J}\omega_J|\overset{\sim}{=}\omega_J}',r'\omega_I\overset{\sim}{=}\omega_J',omega,'Above the ω_J baseline there is a large closed lower loop with a tall doubled diagonal/upward stem, and J is placed at its upper right. The identity of the looped glyph remains open (6-like is the graphic candidate). Its actual contour and relative placement are drawn, with a visible uncertainty node. C places its raised 6J pair on one level; H’s short tilde does not represent the loop/stem.','omega','low','misread symbol or index','Symbols and indices',True,True,False,True)
ids['small']=change('smaller left sphere',cfig[4],r'\drawing{un équateur et quatre points (un en haut, un en bas, un petit cercle à droite sur l’équateur, un groupe de quatre points à gauche)}',fig[4],'The central rear contour is open and 3-shaped with a separate lower arc; it is drawing ink, not a written number. The rear arc is broken, the outer contour has small gaps, the left-front junction has four heavy marks with white openings, and the right-front ring is doubled/lobed. C substitutes clean circles and straight segments; H omits the central open contour.','small_sphere','high','drawing or diagram','Drawings and diagrams',True,True)
ids['pants']=change('small four-holed drawing',cfig[5],r'\drawing{un petit croquis d’une sphère à quatre trous (« pantalon » à quatre jambes), la ceinture marquée en rouge}',fig[5],'The upper-left and upper-right hole contours have gaps; the lower contours are elongated and unequal. Of the two dark coloured central vertical strokes, the left reaches the lower bow and has a short upper inner return, while the right ends higher and has two irregular bends. C closes all holes and makes both central strokes similar. The broad H description is compatible with the drawing.','pants','high','drawing or diagram','Drawings and diagrams',True,False)
ids['leftopen']=change('left note, first baseline','sur cette figure, on',r'en outre les \uncertain{\ill{}}, on','sur cette figure, on','The short opening sur is followed by cette, with two exposed tall t strokes, then figure with its long f and descending g.','left_note','high','misread word','Words',False,True,True)
ids['abbr']=change('left note, second baseline',r'voit à la fois la \unsure{p.r.q.|proj.}',r'voit à la fois la \uncertain{projection}',r'voit à la fois la \unsure{p.r.q.|proj.}','The source ends this line in a short group with descenders and small separated point-like marks. It does not expose the long ending -jection. The exact short-form reading and its internal points remain open; no expansion is inserted.','left_note','low','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,True,True)
ids['leftconfig']=change('left note, middle baselines','du tétraèdre : la configuration-carré, et : la configuration','du tétraèdre à la configuration carrée, et à la configuration','du tétraèdre à la configuration-carré, et à la configuration','The small forms after tétraèdre and et repeat the reduced lower a-body plus detached upper accent of à in voit à la fois within the same note. They are read à, following root adjudication of the same crop. The short horizontal hyphen links configuration and carré, whose ending does not expose the additional e supplied in H; the comma after carré is visible.','left_note','high','misread word','Words',True,True)
ids['leftpantal']=change('left note, penultimate baseline',r'bien \unsure{pantalonique|pantalonnée}',r'\uncertain{tétraédrale} \uncertain{pour la \ill{}}','bien pantalonique','The initial tall b and compact ien are followed by p-a-n-t-a-l-o-n-i-q-u-e; the long initial p and later q descenders are exposed. C’s primary word is retained, with its certainty resolved.','left_note','high','misread word','Words',False,True,True)
ids['leftguin']=change('left note, final baseline',r'du \unsure{quasi-gois|quasi-gss|genre gois}.',r'du genre $0$ \ill{}','du guin-gois.','The word begins with a closed loop and descender, then u, a dotted i and n, a short horizontal separation, and a second g followed by -ois. The final point is separate and aligned with the word ending. The same letter sequence recurs in the fourth point without an isolated hyphen.','left_note','high','misread word','Words',True,True)
ids['large']=change('large lower truncated tetrahedron',cfig[6],r'\drawing{un grand tétraèdre aux quatre sommets tronqués (de petites ellipses brunes), arêtes vertes et brunes, l’arête cachée en tirets bruns ; à l’intérieur, en vert, deux graphes en forme de H joignant les quatre trous, l’un en trait plein épais, l’autre en pointillé.}',fig[6],'Twelve substantial dark marks occur around the four unequal truncation contours. The rear diagonal is broken brown; green dots follow the visible two-junction geometry, separately from the solid green graph. The pencil scaffold projects beyond all truncations; a thin bowed pencil trace rises across the upper-right interior. C gives eight corner marks and a different dotted route. H’s broad description is retained as compatible rather than treated as a lexical error.','large_tetra','high','drawing or diagram','Drawings and diagrams',True,False)
ids['pathc']=change('path c, two baselines',r'c) pôle vers trou $(2\times2\times3)$ et inv.',r'c) pôle vers trou \uncertain{voisin} $(2\times2\times3)$',r'c) pôle vers trou $(2\times2\times3)$\par et inv.','No word intervenes between trou and the product. On the next baseline, et precedes the short inv. with a visible terminal point.','paths_cd','high','misread word','Words',False,True,True)
ids['pathd']=change('path d, two baselines',r'd) pôle vers équateur et inv. $(2\times2\times3)$',r'd) pôle vers équateur \uncertain{voisin} $(2\times2\times3)$',r'd) pôle vers équateur\par et inv. $(2\times2\times3)$','After équateur the next baseline starts et inv., with the i upright, low n/v and a separate terminal point before the product.','paths_cd','high','misread word','Words',False,True,True)
ids['supplem']=change('heading above composed paths',r'$2$ types composés supplém.',r'2 types composés \uncertain{supplémentaires}.',r'$2$ types composés supplém.','The final word ends after the short m with a separate baseline point; no -entaires continuation is exposed.','paths_efg','high','abbreviation expanded or spelling modernised','Abbreviations expanded, spelling modernised',False,True,True)
ids['pathg']=change('bracketed path g',r'[et bien sûr, g) twist complet $2\times2\times3)$]',r'[et bien sûr, g) twist complet $2\times2\times3$]',r'[et bien sûr, g) twist complet $2\times2\times3)$]','The product is followed by a separate closing curved mark inside the closing bracket. There is no supplied opening product parenthesis.','paths_efg','high','omission','Omissions')
ids['bottom']=change('bottom sphere',cfig[7],r'\drawing{une sphère au crayon : l’équateur à l’encre, tracé en entier, portant quatre points ; deux méridiens en rouge passant chacun par deux de ces points.}',fig[7],'The rear equatorial arc ends in a distinct leftward arrowhead just to the right of the rear-left point, with a gap before that point. The front arc also has small endpoint gaps. Four filled marks are exposed; the red broken rear segments lie inside on the left and outside on the right. The outer pencil contour is retraced. C omits the arrowhead and much of the right broken red path; H’s tracé en entier misses the visible endpoint gap/arrow.','bottom_sphere','high','drawing or diagram','Drawings and diagrams',True,True)
ids['footer']=change('lighter lower-left number',r'\margin{17}','[omitted]',r'\margin{17}','A light 1 with a long lead-in is followed by a curved-roof, crossbar 7. Its position and lighter medium are preserved with the margin convention. The isolated small speck lower-right is not assigned a punctuation mark.','footer','high','omission','Omissions')
ids['footvisual']=change('bottom starred note, transition after déformations',', à visualiser',r': \uncertain{viendraient}',', à visualiser','A descending comma follows déformations; the next baseline begins à, then the v-i-s-u-a-l-i-s-e-r sequence. The final r is exposed before a).','footnote','high','misread word','Words',False,True,True)
ids['foot_a']=change('bottom starred note, a clause','a) du pt de vue conforme',r'a) deux pts d’un même \uncertain{confluent},','a) du pt de vue conforme','The short du is followed by the isolated abbreviation pt, de vue and conforme. The word ends -forme; no independent même or terminal comma is exposed.','footnote','high','misread word','Words',False,True,True)
ids['foot_b']=change('bottom starred note, b clause','b) du pt de vue combinatoire',r'b) deux pts d’un \uncertain{même} combinatoire','b) du pt de vue combinatoire','The same short du pt de vue sequence recurs before combinatoire. pt has no added full stop.','footnote','high','misread word','Words',False,True,True)
ids['foot_end']=change('bottom starred note, final parenthesis','(ici encore, deux pts de vue possibles)',r'(ici \uncertain{encore}, deux pts d’un \uncertain{même} voisin)','(ici encore, deux pts de vue possibles)','ici is attached at the right of the preceding baseline; encore, then deux pts de vue possibles follows on the bottom line. The descender in possibles and final closing parenthesis are exposed despite the close lower scan edge.','footnote','high','misread word','Words',False,True,True)

decisions=[]
def decision(num, choice, reading, evidence, crop, confidence):
    decisions.append(dict(id=f'M{num:04d}',decision=choice,reading=reading,evidence=evidence,crop=f'{page}_{crop}.png {boxes[crop]}',confidence=confidence))
decision(119,'undecided',r'\unsure{9|8}','Two loops and a heavy right/down return are exposed in the overwritten factor. Neither a unique numeral nor a distinct deletion layer is established. Arithmetic does not choose the reading.','counts_formula','low')
decision(120,'first','possibilités','The long medial -bilités sequence and raised accent are exposed; positions does not account for those strokes.','diagonal_note','high')
decision(121,'undecided',r'\unsure{inversion|limites}','The short dotted initial and low connected interior suggest inversion, but the interior is compressed. No secure separate d or apostrophe precedes the word.','diagonal_note','low')
decision(122,'first','des faces choisies','Three groups expose des, the descending f and -aces, and the tall h with -oisies.','diagonal_note','high')
decision(123,'undecided',r'\unsure{en} \illegible{2} \unsure{de} vue','Final vue is legible; the preceding four graphic groups are only partly readable. The tentative first en and final de are locally marked; the two intervening groups remain unreadable.','diagonal_note','low')
decision(124,'first','tétraédrales','The source has the -édrales sequence, with d, r and tall l followed by -es.','tetra_line','high')
decision(125,'undecided',r'\unsure{orientation|orientations}','The terminal n/s strokes crowd the right edge immediately above the offset des faces. No distinct final s can be securely separated.','tetra_line','medium')
decision(126,'first','pantaloniques','After lo, one n arch is followed by the short i and descending q. The fourth-point occurrence exposes the same sequence. The raised bi is a separately attached addition.','bipantal','high')
decision(127,'first','opposées','The offset right-hand word exposes rounded o, p descenders and -sées, despite crowding around the punch hole.','bipantal','high')
decision(128,'other','guingois','Closed initial loop/descender, u, dotted i, n, second g and -ois are exposed. Compare the left-note guin-gois; no detached hyphen is exposed at this occurrence.','pantal','high')
decision(129,'alternative','tour','The tall t, connected o/u and terminal r match the tour sequence in the path list; no initial s or -te ending is exposed.','pantal','high')
decision(130,'undecided',omega,'The raised main glyph has a closed lower loop and a tall doubled diagonal stem; J lies beside its upper part. Identity remains undecided, so the graphic is reproduced with a visible uncertainty node, preserving the separate = and ω_J below.','omega','low')
decision(131,'undecided',r'\unsure{p.r.q.|proj.}','The short group and its small point-like strokes remain difficult to separate. The long expansion projection is not exposed.','left_note','low')
decision(132,'first','pantalonique','The p-a-n-t-a-l-o-n-i-q-u-e sequence and both descenders are visible. No -nnée ending is exposed.','left_note','high')
decision(133,'other','guin-gois','The initial loop/descender, u, dotted i, n, short horizontal hyphen, second g and -ois are visible; compare the fourth point guingois.','left_note','high')

second=[]
def box(kind,b,reading):
    second.append(dict(box=f'B{len(second)+1:02d}',kind=kind,x0=b[0],y0=b[1],x1=b[2],y1=b[3],reading=reading))
box('uppermost full baseline',[189,25,1442,109],r'$4$ sommets d’ordre $6$ $+\unsure{6}$ sommets d’ordre $6$ $+12$ sommets d’ordre $3$')
box('second full baseline',[189,109,805,172],r'$24$ triangles $+4$ hexagones')
box('upper-left drawing only',boxes['gray_tetra'],fig[0])
box('upper-right drawing only',boxes['red_tetra'],fig[1])
box('upper two baselines of right marginal note',[1222,193,1528,316],r'mieux\par cf verso')
box('lower parenthetical portion of right marginal note',[1222,303,1528,416],r'(subdivision\par barycentrique)')
box('complete three-line displayed formula',boxes['counts_formula'],r'\['+counts+r'\]')
box('upper-left rounded drawing only',boxes['upper_sphere'],fig[2])
box('central drawing and its two oblique attachments only; exclude surrounding upright and diagonal text',[691,510,1190,928],fig[3])
box('upper baseline of diagonal marginal note only; exclude lower diagonal baselines',[1180,688,1527,794],r'ça fait $2^{\unsure{9|4}}-1=15$')
box('middle two baselines of diagonal marginal note only; exclude upper and lower diagonal baselines',[1173,744,1527,861],r'possibilités \unsure{inversion|limites}\par des faces choisies')
box('lower two baselines of diagonal marginal note only; exclude upper diagonal baselines',[1180,811,1527,899],r'\unsure{en} \illegible{2} \unsure{de}\par vue !')
box('underlined central heading and following full baseline; exclude oblique connector above',[856,889,1528,993],r'\uline{$4$ types de points-base}\par $\bullet$ $3$ structures carrées sur $I$ (ou $J$)')
box('next point with its right-hand continuation; exclude raised writing from following point',[870,976,1527,1066],r'$\textcolor{red!70!black}{\bullet}$ $2$ structures tétraédrales $=$ \unsure{orientation|orientations}\margin{des faces}')
box('following point with raised addition, right marginal word and first parenthetical baseline; exclude preceding point',[871,1018,1528,1115],r'$\textcolor{red!30!black}{\bullet}$ $6$ structures \inserted{bi}pantaloniques\margin{opposées}\par (maillot ceinturé)')
box('lower parenthetical expression and continuation below same point',[946,1107,1488,1177],r'(carrée $+$ codiagonale) $\simeq$\par repère de $J$)')
box('vertical link at left of adjacent points only',[870,1053,896,1136],r'$\updownarrow$')
box('last point and its short following baseline; exclude preceding continuation',[868,1154,1460,1247],r'$\bullet$ $6$ structures pantaloniques\par de guingois')
box('short parenthetical baseline below last point only',[1000,1210,1465,1262],r'(quart de tour)')
box('complete final parenthetical expression across two baselines',[946,1243,1528,1355],r'(\unsure{$\simeq|=$} carré, $+$ orientation de $I$ i.e.)\par de $J$ $\simeq$ repère de $J$)')
box('complete small raised formula left of list',[690,947,861,1049],omega)
box('complete vertical diagram beneath small formula',[690,1049,861,1197],rep)
box('lower-left rounded drawing only',boxes['small_sphere'],fig[4])
box('small central four-opening drawing only',boxes['pants'],fig[5])
box('first two baselines of left marginal note; exclude crossing drawing',[37,1328,434,1450],r'sur cette figure, on\par voit à la fois la \unsure{p.r.q.|proj.}')
box('middle two baselines of left marginal note; exclude crossing drawing',[37,1438,434,1534],r'du tétraèdre à la\par configuration-carré,')
box('following two baselines of left marginal note; exclude crossing drawing',[37,1505,434,1603],r'et à la configuration\par bien pantalonique')
box('final baseline of left marginal note; exclude crossing drawing',[37,1604,319,1648],r'du guin-gois.')
box('large lower drawing only; exclude surrounding and crossing prose',boxes['large_tetra'],fig[6])
box('underlined right-side heading with raised mark',boxes['paths_heading'],r'$4$ \uline{types de chemins élémentaires}$^{*}$')
box('first path and its continuation',[1045,1414,1531,1510],r'a) ``quart de twist\textquotesingle\textquotesingle\ $(2\times3\times4\unsure{)}$\par (contour d’un trou)')
box('second path and its continuation',[1069,1493,1531,1598],r'b) ``sixième de tour\textquotesingle\textquotesingle\ $(2\times2\times3)$\par (sur équateur)')
box('third path and its continuation',[1080,1582,1530,1683],r'c) pôle vers trou $(2\times2\times3)$\par et inv.')
box('fourth path and its continuation',[1080,1665,1530,1762],r'd) pôle vers équateur\par et inv. $(2\times2\times3)$')
box('short heading above lower paths',[1000,1743,1529,1802],r'$2$ types composés supplém.')
box('first lower path and its continuation',[1067,1795,1530,1887],r'e) trou vers trou $(2\times3)$\par ou ``tiers de tour\textquotesingle\textquotesingle')
box('next lower path',[1074,1866,1530,1926],r'f) demi twist $(2\times2\times3)$')
box('bracketed lower baseline',[881,1910,1530,1974],r'[et bien sûr, g) twist complet $2\times2\times3)$]')
box('underlined short lower heading',[883,1957,1169,2007],r'\uline{relations} ...')
box('bottom-left drawing only',boxes['bottom_sphere'],fig[7])
box('lower-left marginal numeral only',boxes['footer'],r'\margin{17}')
box('opening two baselines of starred bottom note',[619,2007,1521,2126],r'$*$ avec les deux sens de parcours, cela\par fait \uline{huit} types de déformations,')
box('next full baseline of starred bottom note',[631,2117,1494,2177],r'à visualiser a) du pt de vue conforme')
box('final two baselines of starred bottom note',[632,2153,1521,2224],r'b) du pt de vue combinatoire (ici\par encore, deux pts de vue possibles)')
# The delivered LaTeX uses straight paired quotation strokes consistently.
for s in second:
    s['reading']=s['reading'].replace(r'\textquotesingle\textquotesingle', "''")

inventory=[]
def inv(kind,position,first,hand='his hand',sheet='text'):
    inventory.append(dict(sheet_kind=sheet,hand=hand,element=f'E{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
inv('text','top, two baselines','4 sommets d’ordre 6; 24 triangles')
inv('drawing','upper left','pencil tetrahedron with top truncated cone and three corner contours',sheet='drawing')
inv('drawing','upper right','black/red tetrahedron; six black interior marks and five red junctions',sheet='drawing')
inv('margin note','right of upper drawing','mieux cf verso (subdivision barycentrique)')
inv('display','below upper-right drawing','s_0; s_1; s_2 count equations')
inv('drawing','left upper-middle','sphere with red and pencil sectors, three irregular point contours and coloured poles',sheet='drawing')
inv('drawing','middle right','green/brown tetrahedron with solid and dotted structures and two attached oblique links',sheet='drawing')
inv('margin note','diagonal at right of central drawing','ça fait 2^{9|4}−1=15; possibilités; des faces choisies; final vue !')
inv('text','under central drawing','4 types de points-base; four coloured/brown/black bullet points')
inv('insertion','raised above initial p of third point','bi, with curved attachment before pantaloniques')
inv('margin note','right of second point','des faces')
inv('margin note','right of third point','opposées')
inv('diagram','left of third/fourth points','vertical single-shaft link with two heads')
inv('display','left of point list','omega_I =, raised looped glyph and raised J, omega_J')
inv('diagram','below omega expression','rep(J), vertical single-shaft two-headed link, J×omega_J')
inv('drawing','left below upper sphere','smaller sphere with four-mark left-front cluster, lobed right ring and central open double-bowed contour',sheet='drawing')
inv('drawing','right of smaller sphere','four-holed drawing with open upper contours and unequal middle verticals',sheet='drawing')
inv('margin note','left of large lower drawing','sur cette figure, on voit à la fois la ... du guin-gois.')
inv('drawing','large lower-left/central area','truncated tetrahedron with twelve dark truncation marks, pencil scaffold, brown hidden edge and two green structures',sheet='drawing')
inv('text','right beside large lower drawing','4 types de chemins élémentaires; a–d; 2 types composés supplém.; e–g; relations ...')
inv('drawing','bottom left','sphere with four black points, rear leftward arrow, red solid/broken meridians and retraced pencil contour',sheet='drawing')
inv('margin note','bottom left corner','17','lighter numbering; hand not established')
inv('margin note','bottom right, five cramped baselines','* avec les deux sens de parcours ... deux pts de vue possibles)')

doubts=[
 dict(place='first count line, addend 6',reading=r'\unsure{6}',alternatives='one retraced numeral; underlying stroke order unresolved',confidence='medium',reason='The single occupied addend is heavily retraced. No independent adjacent canceled numeral is exposed.'),
 dict(place='count display, 4 before 3 and final 48',reading=r'\unsure{4}.3; \unsure{48}',alternatives='retraced or overwritten state; prior layers not separately readable',confidence='medium',reason='The visible primary digits remain 4 and 48, but superimposed strokes do not establish separate deletions.'),
 dict(place='count display, middle factor',reading=r'\unsure{9|8}',alternatives='9; 8',confidence='low',reason='Two loops and a heavy descending return coexist. No mathematical correction is made.'),
 dict(place='diagonal note, exponent',reading=r'2^{\unsure{9|4}}-1=15',alternatives='9; closed 4',confidence='medium',reason='Closed upper loop and right descender favour 9 graphically; the small glyph remains locally open. Written 15 does not decide it.'),
 dict(place='diagonal note, word after possibilités',reading=r'\unsure{inversion|limites}',alternatives='inversion; limites; other compressed word',confidence='low',reason='Interior strokes are compressed; no separate leading d/apostrophe is securely exposed.'),
 dict(place='diagonal note, final phrase',reading=r'\unsure{en} \illegible{2} \unsure{de} vue !',alternatives='two middle groups unreadable; first and last short groups tentative',confidence='low',reason='Only final vue ! is secure. Four preceding graphic groups do not support a complete phrase.'),
 dict(place='second point, terminal word',reading=r'\unsure{orientation|orientations}',alternatives='orientation; orientations',confidence='medium',reason='The final n/s strokes crowd the right edge above the lower continuation.'),
 dict(place='fourth point, initial relation in final parenthesis',reading=r'\unsure{\simeq|=}',alternatives='simeq; equals; retraced unresolved relation state',confidence='low',reason='Two thick horizontal elements have a bowed upper stroke, without a separately exposed canceled expression.'),
 dict(place='small omega formula',reading=omega,alternatives='6-like raised looped glyph; identity open; J upper-right',confidence='low',reason='A tall doubled diagonal and closed loop are visible. The graphic is reproduced without assigning a numeric or alphabetic identity; uncertainty node is visible.'),
 dict(place='left note, short form',reading=r'\unsure{p.r.q.|proj.}',alternatives='p.r.q.; proj.; exact internal points open',confidence='low',reason='The compact group has two descenders and small point-like strokes whose allocation remains uncertain.'),
 dict(place='first path, closing parenthesis at scan edge',reading=r'(2\times3\times4\unsure{)}',alternatives='closing parenthesis partly merged with edge; no secure separate full contour',confidence='medium',reason='The ends of the closing curve protrude at the dark right scan edge, while its middle merges into that edge. The same saved paths_ab crop supports the clipped contour, retained with local uncertainty.'),
 dict(place='upper sphere and pencil drawing detail',reading='explicit TikZ contours, dots and separate arcs',alternatives='minor faint return contours remain approximate; prominent point marks and observed gaps retained',confidence='medium',reason='Pencil retracing and listing ruling overlap. The report distinguishes prominent black marks from unfilled contour bends and paper texture, and does not infer extra points or a regular hatch pattern.'),
]

coverage={}
def cov(rows,text):
    for row in rows: coverage[row]=text
cov([521],'C scanpage is editorial scan metadata; H paper/medium/no-top-number note is editorial. No top manuscript number is added; the lighter footer is separately recorded in '+ids['footer']+'.')
cov([522],ids['top'])
cov([523,524],ids['gray']+'; '+ids['red']+'; '+ids['verso']+'. Long mechanically crossed figure/note alignment; compare physical loci, not code tokens.')
cov([525],ids['red']+' and '+ids['counts']+'. H’s graph description is editorial prose, not handwritten text.')
cov([526,528,531],'Same-reading display/aligned environment delimiters; no source-word or mathematical change.')
cov([527,529,530],ids['counts']+'. The complete three-line formula is retained, including product points and uncertain overwritten state.')
cov([532,533,534],ids['counts']+'. H’s explanatory surcharge note is editorial; its mathematical strings are not extra source equations.')
cov([535,536,537,538,539,540],ids['upper']+'; '+ids['green']+'; '+ids['small']+'; '+ids['pants']+'; '+ids['large']+'; '+ids['power']+'. Mechanically interleaved descriptions and drawing code are adjudicated by their physical figures and attached formula.')
cov([541],ids['poss']+'; M0120 resolved first, certainty-only against C.')
cov([542],ids['inversion']+'; M0121 remains locally uncertain.')
cov([543],ids['faces']+'; M0122 resolved first, certainty-only against C.')
cov([544],ids['vue']+'; M0123 partial reading retained with local doubts.')
cov([545],'H’s long figure/drawing descriptions are editorial; all eight actual drawings are transcribed. See drawing changes and inventory; do not insert the description as source prose.')
cov([546,567,570,573,574,577,579,581,582,585,586],'List/environment syntax only; source point/path lettering is transcribed directly.')
cov([547,550],'Coloured bullet markup versus H editorial colour note; red second bullet and brown third bullet are preserved from the ink, without adding source words.')
cov([548],'M0124 resolved first: tétraédrales. Same primary word in both witnesses, no substantive change.')
cov([549],ids['tetra']+'; M0125 unresolved ending and right-hand des faces placement.')
cov([551],ids['pantaln']+'; '+ids['opposees']+'. M0126 and M0127 resolved first; bi remains a raised attached addition.')
cov([552],ids['ceinture'])
cov([553],ids['codiagonale'])
cov([554],ids['jparen']+' and '+ids['opposees']+'. Brown-point editorial note is not source text.')
cov([555,556],ids['guingois']+'; M0128 other reading. H’s proposed genre-gois note is an editorial uncertainty, not extra source words.')
cov([557],ids['tour']+'; M0129 retains the third C alternative.')
cov([558],ids['relation']+'. The complete final parenthesis is in B20; the additional closing mark after i.e. is '+ids['ieparen']+'.')
cov([559],'H list closure/location prose is editorial. The omega formula and vertical diagram are preserved at the left of the point list.')
cov([560,561],ids['omega']+'; M0130 retains glyph uncertainty and actual raised placement.')
cov([562,563],'Same observed single-shaft vertical link with both heads; tikz-cd syntax versus H verbal description. Complete diagram preserved.')
cov([564,565,566],ids['small']+'; '+ids['pants']+'; '+ids['leftopen']+'; '+ids['abbr']+'; '+ids['leftconfig']+'; '+ids['leftpantal']+'; '+ids['leftguin']+'; '+ids['large']+'. H’s separate list-link description corresponds to the observed second two-headed vertical link, also preserved.')
cov([568,569,571,572,583,584],'Source paired quotation strokes retained using straight paired quotation typography. The underlying quoted words agree; H certainty markers on twist are not separate word errors. Both tour occurrences and contour are legible on the saved path crops.')
cov([575,576],ids['pathc'])
cov([578],ids['pathd'])
cov([580],ids['supplem'])
cov([587],ids['pathg'])
cov([588],ids['bottom']+' and '+ids['footer']+'. Relations underline and three detached ellipsis points are preserved; long figure-code alignment is not source prose.')
cov([589],ids['footvisual'])
cov([590],ids['foot_a'])
cov([591],ids['foot_b'])
cov([592,593],ids['foot_end']+'; '+ids['leftopen']+'; '+ids['abbr']+'; '+ids['leftconfig']+'; '+ids['leftpantal']+'; '+ids['leftguin']+'. H’s end-of-page/location notes are editorial. All lower-margin writing is transcribed.')
assert sorted(coverage)==list(range(521,594))

report=dict(
 page=page,reader='reader_a',line_count=60,
 line_count_basis='Physical text/formula baselines, including the raised bi and offset marginal words, excluding nonalphabetic drawing strokes; the compact starred note has five baselines.',
 layout='Listing-paper sheet with two opening count lines, two upper drawings and a right note, three count equations, a large left sphere and a central coloured tetrahedron, a diagonal right note, four points-base bullets with two separate vertical links and a small raised formula at their left, a smaller sphere and four-holed drawing, a large lower truncated tetrahedron with prose at left and paths at right, a bottom sphere, lighter footer17 and a five-baseline starred note. Eight drawings are reconstructed. The additional oblique connector from above types to the central tetrahedron’s lower vertex is preserved separately from the outward arrow to the diagonal note.',
 legibility='The main black body is mostly legible, with compressed minims, tall looped ascenders and long descenders. The diagonal note, overwritten digits and compact left abbreviation remain difficult. Right punch holes crowd opposées and path endings; the bottom note nearly meets the scan edge. Pencil curves cross printed diagonal listing bands, so actual curved/retraced traces are separated from the repetitive paper ruling. Coloured outlines remain visible, including red poles, green solid/dotted graph structures and brown broken edges. Whole image and both prepared halves were read once each; all24 saved crop targets were personally viewed. Large PNG displays were replaced only by same-dimension JPEG quality96/subsampling0 view derivatives, without a new crop or resize; original PNG evidence is retained. An earlier output-truncated image was not counted as seen until its successful subsequent display.',
 witness_comparison='C generally preserves the body wording, abbreviations, products and short parenthetical continuations more closely. Its unresolved marks cover the important local textual uncertainties, but its diagrams often replace broken/retraced or lobed contours by clean ellipses and omit individual marks or the lower rear arrow. Both witnesses miss the heading-to-vertex connector and the closing parenthesis after i.e.; both misread the repeated guingois/guin-gois. H adds a second canceled6 and interprets overlapping count strokes as separately canceled digits, expands supplém. and the uncertain short form, misreads et inv. as voisin, and substantially misreads the starred note. H accurately records several marginal placements and broadly describes the coloured drawings; compatible broad descriptions are not treated as invented handwritten prose. Certainty-only C resolutions remain decisions, not reading-error counts.',
 changes=changes,decisions=decisions,unnumbered_decisions=[],inventory=inventory,doubts=doubts,
 notation=[
  dict(form=r's_0,s_1,s_2',meaning='labels on the three written count equations',evidence='counts_formula; subscripts0,1,2 and complete equations read directly',scope='this page’s count block only'),
  dict(form=r'\omega_I,\omega_J,\operatorname{rep}(J),J\times\omega_J',meaning='symbols occurring in the small left formula and vertical diagram; no definition or identification of the raised glyph is supplied',evidence='omega crop; actual =, raised looped glyph/J and both link heads',scope='this page’s two adjacent symbolic displays only'),
  dict(form='guingois / guin-gois',meaning='the source’s repeated designation after de/du; the page supplies no separate definition',evidence='pantal and left_note; same loop–u–dotted i–n–g–ois sequence, with a visible hyphen in the left note',scope='the two inspected occurrences on018 only')
 ],
 abbreviations=[
  dict(form='cf',expansion='confer / compare, tentative; the source has no secure baseline point'),
  dict(form='inv.',expansion='inverse(s), tentative; source abbreviation retained'),
  dict(form='supplém.',expansion='supplémentaires, tentative; source abbreviation retained'),
  dict(form='pt / pts',expansion='point / points, tentative; source has no added full stops'),
  dict(form='i.e.',expansion='id est, tentative; both source points and following parenthesis retained'),
  dict(form=r'\unsure{p.r.q.|proj.}',expansion='undecided short form; no expansion assigned')
 ],
 hand=[
  dict(habit='Closed rounded lower loops with long downstrokes distinguish the repeated g-like initials and medial g; i dots remain detached.',places='guingois in fourth point and guin-gois in left note',scope='these two directly compared occurrences only',witness_errors='C quasi-/genre alternatives and H genre0'),
  dict(habit='A single compact n arch can run directly into the short i before the q descender.',places='third and fourth pantaloniques; left pantalonique',scope='three local occurrences inspected',witness_errors='H pantalonniques in third point'),
  dict(habit='Retracing can produce superimposed loops and long returns without an independently readable canceled layer.',places='top addend6; displayed4, factor9/8 and48; relation before carré',scope='these inspected loci only',witness_errors='H separately canceled digit/word claims'),
  dict(habit='Marginal continuation words are lowered and displaced to the right; the raised bi has a curved attachment to the initial p.',places='des faces; opposées; bi',scope='these list attachments only',witness_errors='C inline placement of right-hand continuation words'),
  dict(habit='Short forms end in a compact letter followed by a detached point, while pt/pts have no added point.',places='inv., supplém., bottom pt/pts',scope='the visible occurrences on018',witness_errors='H expansions and voisin readings')
 ],
 notes='018 opens with the written counts of vertices of stated orders and triangles/hexagons, then records s_0=4+6+4.3=22, s_1=12+4.(uncertain9/8)=48 and s_2=4.7=28 with overlapping numeral strokes. These are transcription readings, not arithmetic verification. The diagonal note attaches a written 2^(uncertain9/4)−1=15 formula to possibilités, des faces choisies and an unresolved final phrase ending vue !. The point list records3 square structures,2 tétraédrales structures with an unresolved orientation(s) ending,6 bi-pantaloniques structures with marginal opposées and a maillot/codiagonale parenthesis, and6 pantaloniques structures de guingois with quart de tour. The small omega formula is graphically retained with an unidentified raised looped glyph and upper-right J; below, rep(J) is vertically linked to J×omega_J. The left note describes what the drawing shows using an unresolved short form and the source phrases configuration-carré, bien pantalonique and guin-gois. The path list writes the products associated with a–g, preserves inv., supplém., and the unmatched closing marks, then leaves relations followed by three points. The starred note says the two traversal senses give eight types of deformations to visualize from the conforme and combinatoire points of view; it also writes two possible points of view in its final parenthesis. No mathematical definition, proof, correction, or conditional theorem is supplied by this reader. Printed listing bands and punch holes are sheet support, not additional source drawing strokes.',
 check_events=[],second_boxes=second,diff_coverage=[dict(row=r,disposition=coverage[r]) for r in sorted(coverage)],
 deletion_insertion_check='The only explicit letter insertion is raised bi immediately before the p of third-point pantaloniques; its curved attachment and full word are preserved. The right-hand des faces and opposées are retained as offset marginal continuations. The top6, displayed4/factor9-or8/48 and relation before carré were separately crop-inspected: superimposed/retraced strokes are visible, but no separately decipherable prior glyph layer or independent cancellation justifies H’s extra struck6, struck digits, struck illegible text or trailing ellipses. Those states remain local doubts; no deleted word is invented. The long t-crossing connector above the points-base heading belongs to the drawing attachment and is not a cancellation of types. All extra closing marks, abbreviations, coloured points, figure gaps and the bottom equatorial arrow are retained.',
 layout_evidence=[
  dict(place='points-base heading attachment',evidence='green_tetra clipped the start of an unresolved oblique stroke. green_attachment [780,850,1184,987] completes its start above the t and its endpoint at the dark lower vertex. This is the only additional crop of a previously clipped unresolved target; the decided drawing interior was not recropped.'),
  dict(place='paths heading underline',evidence='The underline begins just to the right of the4 and runs under types de chemins élémentaires. TeX preserves this extent; this is layout evidence rather than a lexical error count.')
 ],
 crops=[dict(file=f'{page}_{name}.png',box=b,angle=-16 if name=='diagonal_note' else 0,inspected=True) for name,b in boxes.items()],
 structural_validation='No OCR, outside research or TeX compilation. Report checks cover15 original M IDs,73 original physical difference rows, all24 crop paths and neutral localized box bounds; exact drawing and formula serialization is drawn from the delivered TeX.'
)
hdraw = re.findall(r'\\drawing\{.*?\}', H, re.S)
assert len(hdraw) == 6
for key, index in [('gray',0),('red',0),('upper',1),('green',3),('small',2),('pants',2),('large',4),('bottom',5)]:
    next(c for c in changes if c['id']==ids[key])['H']=hdraw[index]
for c in changes:
    c['C']=c['C'].replace('’', "'")
    c['H']=c['H'].replace('’', "'")
(root/'work'/f'{page}_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'page':page,'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),'doubts':len(doubts),'second_boxes':len(second),'diff_coverage':len(coverage),'crops':len(boxes)},ensure_ascii=False))
