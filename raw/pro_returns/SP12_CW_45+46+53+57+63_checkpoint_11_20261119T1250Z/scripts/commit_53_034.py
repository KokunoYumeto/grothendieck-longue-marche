from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
d={'cote':53,'scan':34,'sheet_kind':'text','hand':'his hand','replace':[
 (r'\unsure{tjrs|tjrs.}',r'\unsure{tjrs|tjs}'),
 (r'\unsure{\mathcal{O}|\mathscr{O}}',r'\mathbb{O}'),
 (r'\mathcal{O}',r'\mathbb{O}'),
 (r"\unsure{M_{k'}|M}",r"M_{k'}"),
 (r'\unsure{Or|or}','Or'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader viewed the whole image and both supplied halves before reading C and H, then read every line against the ink in eight broad crops at 4–5× and twenty-four focused crops at 8–14×. One batch of six focus images was truncated entirely in the tool output; all six were displayed again in smaller batches and actually inspected. Four supplementary crops at 8–14× checked both lower O letters, the vertical equals rotated clockwise 90 degrees, and the lower Hom formula rotated counterclockwise 3 degrees. Earlier focused crops were revisited where the overwritten symbols or short abbreviation remained doubtful. A final whole-page view checked placement, the unclosed square bracket and the large unused lower area. All C doubts and H differences, every agreed word and mathematical sign, and the cancellations and inserted explanation were compared with the ink. No OCR, context, delegated reading or LaTeX compilation was used.'}
# The explanatory underbrace has a retraced right lobe with a closed loop.
old=r'''\underbrace{\underline{\operatorname{Hom}}_{\mathbb{O}_k}
 (W(M),\deleted{\unsure{\mathbb{O}_k|\mathbb E_k}}W(k))}'''
brace=r'''\tikz[baseline=0pt,x=1em,y=1em]{\draw[line width=.45pt] (0,.15) .. controls (.1,0) and (2,.14) .. (2.75,-.22) .. controls (2.83,-.28) and (2.82,-.38) .. (2.84,-.4) .. controls (2.89,-.08) and (3.05,.04) .. (3.5,.03) .. controls (4.2,.02) and (5.1,0) .. (5.65,.28);\draw[line width=.45pt] (2.88,-.37) .. controls (2.88,-.14) and (3.05,.05) .. (3.47,.02) .. controls (4.2,-.18) and (4.75,.05) .. (5.16,.18); }'''
new=r'''\underset{'''+brace+r'''}{\underline{\operatorname{Hom}}_{\mathbb{O}_k}
 (W(M),\deleted{\unsure{\mathbb{O}_k|\mathbb E_k}}W(k))}'''
d['replace'].append((old,new))
# The warning-shaped mark contains a point; its long left stroke is external.
d['replace'].append((r'\draw (-.10,.25) -- (-.12,-.21) (.01,.23) -- (.09,.30);',r'\draw (-.10,.25) -- (-.12,-.21) (.01,.23) -- (.09,.30);\draw (.01,.21) to[out=5,in=145] (.19,.16) (-.11,-.08) to[out=-5,in=210] (-.025,-.065);'))
d['replace'].append((r'\node[inner sep=0pt] at (.02,.01) {\tiny\(\unsure{!|\cdot}\)};',r'\fill (-.045,-.04) circle (.012);'))
# Two separate oblique points follow the f; no point follows t.
points=r'\tikz[baseline=-.2ex,x=1ex,y=1ex]{\fill (0,.3) circle (.055);\fill (.12,.12) circle (.08);}'
d['replace'].append((r'\unsure{t f.|t.f.}',r't f\hspace{.1em}'+points))
# Draw the doubled-descender mu without assigning it an extra semantic label.
mu=r'''\mathord{\tikz[baseline=-.25ex,x=1ex,y=1ex]{\draw[line width=.08ex,line cap=round,line join=round] (.04,1.05) .. controls (.07,.4) and (.04,-.48) .. (.08,-.83) .. controls (.1,-.98) and (.15,-1.05) .. (.2,-1.12);\draw[line width=.09ex,line cap=round,line join=round] (.24,1.03)--(.28,1.15)--(.37,1.09) (.2,.56) .. controls (.16,.2) and (.21,-.57) .. (.32,-.89) (.19,.33) .. controls (.38,.31) and (.58,.53) .. (.66,.8) .. controls (.65,.37) and (.63,.19) .. (.96,.12);}}'''
d['replace'].append((r'\mu_n',mu+'_n'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('first V alphabet',r'\unsure{\mathbb{V}|V}','ordinary V','C retained','The two heavy stems join in a filled lower vertex, with two separate upper-right tips but no securely open internal space. (244,83,310,150), 14×. The later clearer doubled V does not remove the physical doubt at this first occurrence.','low')
a('first Hom formula','Hom subscript k-mod; Hom subscript k-prime-mod','same','C retained','Both minus signs and the three-letter mod groups are visible below the baseline. Every k-prime has its detached high stroke, and the tensor has a lower k. Both closing parentheses and equals signs are present. Top (229,75,1473,183), 4×.')
a('short underlined abbreviation',r'\unsure{tjrs|tjrs.}','struck est',r'\unsure{tjrs|tjs}','A small looped opening t, long descending j and compressed final arched group precede blank paper; there is no detached final point. The middle r-like arch is not securely separated from the last letter. (322,208,387,270), 14×.','low',True,True,'misread word')
a('abbreviation state','underlined','struck','C retained','The independent horizontal is entirely below the short word and meets only its j descender. It does not strike through the letter bodies. Same crop.',hc=True,k='deletion state (struck given live or live given struck)')
a('representability words','représentable par','same','C retained','The acute accent, p descender, tall t/b/l and final e are visible, followed by a separate par. Representation crop (317,186,1301,288), 5×.')
a('Sym exponents and summation','star; lower n greater-than-or-equal zero; upper n','same','C retained','The first raised mark has six radiating strokes. The summation condition has a clear n, upper angle and lower bar followed by an oval zero; the final Sym has a raised n and lower k. (841,192,885,234), 14×; (984,197,1071,282), 12×.')
a('open square bracket','opening only','opening only','C retained','The tall left vertical has short rightward top and bottom returns; no corresponding closing square bracket appears to the right or below. Central (237,300,1466,492), 4×; final whole-page view.')
a('pairing V and W','ordinary V and W','same','C retained','The first V has two single strokes, while W has two lower turns; their parenthesized M letters and intervening cross are clear. The arrow has two oblique right-head arms. Central crop, 4×.')
a('overwritten E in pairing target',r'\deleted{\unsure{\mathbb{E}|E}}','omitted','C retained','Three horizontal E-like strokes and upright remnants lie within the newer oval and crossing. One upright may be shared with the new O, so the old alphabet remains doubtful. (628,326,706,414), 12×.','low',hc=True,k='omission')
a('live pairing O alphabet',r'\unsure{\mathcal{O}|\mathscr{O}}',r'\mathcal{O}',r'\mathbb{O}','The outer oval and independent inner upright match the unobscured doubled O of the Hom coefficient and lower Mod expression; k is separately lowered. Same crop; (1148,386,1224,456), 12×.','medium',True,True,'misread symbol or index')
a('target equality','O subscript k equals W(k)','same','C retained','Two short horizontal equality strokes precede a W with two lower turns and a parenthesized branched k. Central crop, 4×.')
a('second V alphabet',r'\mathbb{V}','ordinary V','C retained','An open inner loop lies beside the lower left stem and another beside the right stem, unlike the single-line V at the pairing start. (822,328,890,390), 12×.',hc=True,k='misread symbol or index')
a('isomorphism connector','right arrow with wave','same','C retained','A separate upper wave lies above a shaft with two oblique right-head arms. Central crop, 4×.')
a('Hom coefficient alphabet',r'\mathcal{O}_k',r'\mathcal{O}_k',r'\mathbb{O}_k','A full inner upright joins the upper and lower edges of the oval, leaving a narrow separate left compartment. The k is below and to the right. (1148,386,1224,456), 12×.','high',True,True,'misread symbol or index')
a('old coefficient before first W(k)',r'\deleted{\unsure{\mathcal{O}_k|\mathbb E_k}}','omitted',r'\deleted{\unsure{\mathbb{O}_k|\mathbb E_k}}','An old outer O-shaped curve, doubled upright and E-like bars overlap the new W; a lower k remains beside the newer parenthesized k. The layers cannot securely distinguish O from E or justify additional separate deleted states. (1322,310,1457,413), 10×.','low',True,True,'omission')
a('isolated mark below pairing',r'\unsure{V|\surd}','omitted','C retained','Two heavy descending-and-rising strokes make a V-like form; a thinner upper curl returns into the right stem. Its identity is not settled. (537,450,586,510), 14×.','low',hc=True,k='omission')
a('explanatory underbrace','ordinary underbrace','brace described in note','brace with retraced right loop drawn','The left lobe bends into a low central cusp; the right lobe has a second returning stroke that closes a long narrow loop and extends upward. (1100,445,1456,490), 8×.','high',True,True,'drawing or diagram')
a('explanatory formula placement','beneath underbrace','text of note','C retained','The k-prime mapsto Hom line is below the brace, the W(M-k-prime) insertion is above its first argument, and the next Hom equality is on a still lower line. Explanation (1094,465,1717,659), 5×.',hc=True,k='insertion or placement')
a('explanatory map and W(M) index','k-prime mapsto Hom(W(M) subscript k-prime,...)','same in note','C retained','The map has an independent left bar and two right-head arms. The first W has two low turns; its parenthesized M is followed by the lower k and separate prime. Explanation crop, 5×.')
a('raised W argument',r"\unsure{M_{k'}|M}",r"M_{k'}",r"M_{k'}",'The raised W contains a two-stem M with a distinct lower branched k and detached short prime before its closing parenthesis. (1494,458,1611,509), 12×.','high',True,False,'misread symbol or index')
a('raised insertion guide','overbrace and inserted equivalence','explained in note','C retained','A rising wavy guide runs over W(M) and ends below the separate two-stroke equivalence and raised W expression. Explanation crop, 5×.',hc=True,k='insertion or placement')
a('old coefficient before W(k-prime)',r"\deleted{\unsure{\mathcal{O}_{k'}|\mathcal{O}_{k}}}",'omitted',r"\deleted{\unsure{\mathbb{O}_{k'}|\mathbb{O}_{k}}}",'A doubled old O overlaps the new W and its opening parenthesis; lower k remnants are visible, but a prime cannot be securely assigned to the old layer separately from the new k-prime. (1530,503,1651,578), 10×.','low',True,True,'omission')
a('vertical equality','rotated equals','ordinary equals in note','C retained','After clockwise 90-degree rotation, two separate approximately horizontal strokes are visible, the upper ending in a small upturn. (1417,578,1457,624), 14×.',hc=True,k='insertion or placement')
a('lower Hom subscripts and arguments',r"Hom_{k'}(M_{k'},k')=Hom_k(M,k'...",'same','C retained','The first Hom has lower k-prime, and M has its own lower k-prime. The first target has a high prime. The second Hom has only lower k and its argument M has no subscript. (1297,583,1717,675), 8×; (1297,583,1727,681), counterclockwise 3 degrees, 8×.')
a('far-right closing parenthesis',r'\unsure{)}',')','C retained','A thin oblique lower tail emerges from the black right boundary after k-prime, but the upper part is clipped. Its interpretation as the closing parenthesis remains uncertain. (1636,610,1727,681), 14×.','low')
a('Or case',r'\unsure{Or|or}','Or','Or','The large opening oval rises above the short r body and descends farther; it has the capital form despite heavy retracing. (309,567,373,620), 14×.','medium',True,False,'misread word')
a('Or state','live','struck','C retained','The dark horizontal belongs to the r foot and stops at its endpoint; no independent line crosses the two letters. Same crop.',hc=True,k='deletion state (struck given live or live given struck)')
a('functor assignment','M mapsto W(M)','same','C retained','The M has two tall stems with short feet, and the connector has a separate left bar and pointed right head. Mod block (297,561,1463,707), 4×.')
a('category connector',r'\longmapsto',r'\longrightarrow','C retained','A short vertical bar stands at the left end of the horizontal; the right end has two oblique head arms. Mod block, 4×.',hc=True,k='drawing or diagram')
a('Mod coefficient alphabet',r'\mathcal{O}_k',r'\mathcal{O}_k',r'\mathbb{O}_k','The oval contains a second upright from top to bottom and a clear narrow left space; the lower k is separate. (737,634,807,709), 12×.','high',True,True,'misread symbol or index')
a('faithfulness underline','einement fidèle only','whole pleinement fidèle emphasized','C retained','The horizontal begins after the opening pl and extends under einement fidèle. A detached final point follows the last e. Mod crop, 4×.',hc=True,k='insertion or placement')
a('De-m abbreviation','De m with overbar','De illegible','C retained','The capital D, small e and separate low m are clear; a single horizontal bar lies above m. (203,682,349,740), 12×.',hc=True,k=r'readable ink left as \ill{}',m='yes')
a('De-m state','live','struck','C retained','The long wavy framing line is below the text, with blank paper between it and the letters. It does not cancel De or the barred m. Same crop.',hc=True,k='deletion state (struck given live or live given struck)')
a('De-m placement','before old Mod and M mapsto V(M)','after M mapsto V(M) line','C retained','De and the barred m lie at the far left on the same level as the crossed Mod and live assignment. Note block (107,681,1717,897), 4×.',hc=True,k='insertion or placement')
a('deleted Mod','struck Mod','same','C retained','A clear M, o loop and tall d are crossed by an independent long horizontal. (409,695,499,741), 14×.')
a('live underlined assignment','underlined M mapsto V(M)','same','C retained','A short underline lies below M; a separate left-barred right-headed shaft leads to ordinary V with parenthesized M. Note block, 4×.')
a('base-change abbreviation','chgt','ext.','C retained','The opening joined c/h group is followed by a closed descending g and a separate tall t. No detached point follows the abbreviation. (1122,704,1301,762), 10×.',hc=True,k='misread word')
a('base-change article','de base','de la base','C retained','The small looped de is followed directly by the b ascender of base, without an intervening la group. Note block, 4×.',hc=True,k='text not on the page')
a('remainder of side note','idem après ... à k-prime','same','C retained','The dotted i, tall d and joined em are followed by après with its accent and s. The final à has its separate accent; k has a detached prime. Note block, 4×.')
a('triangular mark','triangle with uncertain exclamation/dot','struck illegible','triangle with point and exterior strokes','A triangular outline surrounds a separate dark point near its lower-left interior. The long upright lies outside the triangle to the left; no independent vertical body stands above the interior point. The upper-right return and short lower-left inner curve are also drawn. (288,764,344,841), 14×.','medium',True,True,'drawing or diagram','yes')
a('left frame','drawn','described in note','C retained','The long upper wavy horizontal turns down at the left of Donc and then right below Donc on a. The triangle lies outside and left of that vertical. Note block, 4×.',hc=True,k='drawing or diagram')
a('biduality word','bidualité','uncertain dualité; perhaps bi-dualité in note','C retained','A tall initial b and dotted i precede the looped d, compressed ua, tall l and crossed t with final accented é. There is no hyphen. (908,770,1118,837), 10×.',hc=True,k='misread word',m='yes')
a('biduality sentence','Donc on a une ... parfaite entre V(M) et W(M)','same','C retained','Every short word, the p descender and final e of parfaite, entre and et, and the distinct ordinary V and W with complete parentheses are visible. Note block, 4×.')
a('points below biduality sentence','five','three','C retained','Five separate principal points run across the lower right of the block. Note block, 4×.',hc=True,k='omission')
a('Aut coefficient alphabet',r'\mathcal{O}',r'\mathcal{O}',r'\mathbb{O}','The oval has an independent full inner left upright and open narrow space beside it. (368,944,428,997), 12×.','high',True,True,'misread symbol or index')
a('End coefficient alphabet',r'\mathcal{O}',r'\mathcal{O}',r'\mathbb{O}','The oval likewise has a full internal upright joined at the bottom, with a top return extending right. (638,943,692,987), 12×.','high',True,True,'misread symbol or index')
a('Aut-End relation','underlined Aut; subset; underlined End','same','C retained','Both operator names have separate lower horizontal lines; the subset sign has a rounded left end and two right arms, with no middle bar. Aut block (295,900,1668,1008), 4×.')
a('projectivity clause','représentable si M est proj.,','same without comma','C retained','The r/e/p/r group, accent and final e are visible; after proj. a separate thin curved comma lies before t. (1463,924,1641,995), 10×.',hc=True,k='omission')
a('finite-type abbreviation and punctuation',r'\unsure{t f.|t.f.}','t.f.','t f followed by two oblique points drawn','There is no detached point after t. The tall f has a long lower return and two distinct small dark points to its right, the first higher and left of the second. Both are reproduced without assigning them a normalized punctuation value. Same crop.','high',True,True,'drawing or diagram')
a('separator','horizontal rule','described in note','C retained','A long nearly straight horizontal separates the last line from the preceding formulas. End block (219,1037,715,1194), 5×.',hc=True,k='drawing or diagram')
a('last mu-shaped symbol',r'\mu_n','uncertain fla/fl-subscript-a','mu shape with doubled left descender and lower n drawn','The main shape has the descending left and rising-right bowl of mu, with a second long parallel left stroke and a short detached hooked upper remnant. The following small lower letter is a single n arch. (298,1096,383,1191), 12×.','high',True,True,'misread symbol or index','yes')
a('argument of D','drawn angular dotted glyph, Gamma/Pi alternatives','Gamma','C retained','A tall left stem joins a horizontal top, which turns down in a short right stem; a separate point lies inside near the left. The shape alone does not establish Gamma or Pi. (526,1090,579,1150), 14×.','low',hc=True,k='misread symbol or index')
a('last punctuation','comma after mu-n; three points after D(...)','same','C retained','The comma is a separate hooked stroke. Both D parentheses are visible, followed by three separated low points. End block, 5×.')
d['unresolved']='The first V alphabet; tjrs/tjs; the alphabet of overwritten E; old O/E before W(k); the isolated V/surd-shaped mark; the old O subscript k-prime/k before W(k-prime); the clipped closing parenthesis at the right edge; and the angular dotted argument of D. The doubled mu and two punctuation points are drawn as seen. The relation of the doubled mu and O forms to earlier sheets remains for the global visual audit.'
d['inventory']=[
 ['display','top','V(M)=Hom-k-mod(M,k-prime)=Hom-k-prime-mod(M tensor-k k-prime,k-prime)'],
 ['text','second line','underlined tjrs/tjs représentable par'],
 ['display','right of second line','Sym-star-k(M)=sum-n-ge-zero Sym-n-k(M)'],
 ['drawing','left of central formulas','unclosed square bracket'],
 ['display','central left','V(M) times W(M) arrow O-k equals W(k)'],
 ['deletion','pairing target','overwritten E alphabet uncertain'],
 ['display','central right','double V(M) isomorphism to underlined Hom-O-k(W(M),W(k))'],
 ['deletion','inside central Hom','old doubled O-k/E-k before W(k)'],
 ['drawing','below pairing','isolated V/surd-shaped mark'],
 ['drawing','under central Hom','underbrace with retraced right loop'],
 ['display','below brace','k-prime mapsto Hom(W(M)-k-prime,W(k-prime))'],
 ['insertion','above first Hom argument','equivalence W(M-k-prime)'],
 ['drawing','above W(M)-k-prime','rising overbrace/guide'],
 ['deletion','inside lower Hom','old doubled O-k-prime/O-k'],
 ['display','below explanatory Hom','vertical equals'],
 ['display','lower-right explanation','Hom-k-prime(M-k-prime,k-prime)=Hom-k(M,k-prime; clipped closing parenthesis)'],
 ['text','middle left','Or'],
 ['display','after Or','M mapsto W(M)'],
 ['display','next line','Mod(k) mapsto Mod(double O-k)'],
 ['text','right of category line','est pleinement fidèle; partial underline'],
 ['text','left above frame','De barred m'],
 ['deletion','after De-m','Mod'],
 ['display','after old Mod','underlined M mapsto V(M)'],
 ['text','right of assignment','idem après chgt de base à k-prime'],
 ['drawing','left of Donc block','wavy upper line, left vertical, lower horizontal frame'],
 ['drawing','left of frame','triangle, interior point and outer strokes'],
 ['text','framed line','Donc on a une bidualité parfaite entre V(M) et W(M)'],
 ['drawing','lower right of framed line','five points'],
 ['display','next line','underlined Aut-double-O(M) subset underlined End-double-O(M)'],
 ['text','right of Aut-End','représentable si M est proj., t f'],
 ['drawing','after f','two oblique punctuation points'],
 ['drawing','above last line','horizontal separator'],
 ['display','last line','doubled-descender mu with lower n, D(angular dotted glyph)'],
 ['drawing','after last formula','three points'],
 ['text','bottom left','33 (archive sheet number; retained as comment)','another hand'],
]
rv['commit'](d)
