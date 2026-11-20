from pathlib import Path
from datetime import datetime, timezone
import json
P=Path('/workspace/scratch/94548b74fbe0/out/readers/004/A')
CP=Path('/workspace/scratch/94548b74fbe0/packets/004')
crops=json.loads((P/'crop_manifest.json').read_text())
cm={c['path']:c for c in crops}
D=[]
def row(id,loc,C,H,reading,evidence,confidence='high',kind='other',dc=False,dh=False,status=None,crop=None,bbox=None,refs=None,consequence=None):
 d={'id':id,'location':loc,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':crop,'bbox':({'image':'full','origin':'upper left','xyxy':cm[crop]['bbox']} if crop else bbox)}
 if refs: d['C_doubt_refs']=refs
 if consequence: d['mathematical_consequence']=consequence
 D.append(d)
def full(b):return {'image':'full','origin':'upper left','xyxy':b}
def half(n,b):return {'image':'half '+n,'origin':'upper left','xyxy':b}
row('A004-001','Left top, descended letter in parenthesis',r'\unsure{\eta|\gamma}_{d-1}',r'\eta_{d-1}',r'\unsure{\eta|\gamma}_{d-1}','An entry hook rises into one shoulder and a long right descender curves left. The form supports eta most strongly, with gamma still visually supportable. The repeated shape is treated consistently after this first occurrence.','medium',status='retained',crop='01_top_eta_brace.png',refs=['Left top and right system','Left top, equality in parentheses'])
row('A004-002','Left top, mark after subscript d−1',r'\unsure{\}|\,}',r'\eta_{d-1}=\eta',r'\unsure{\}|\,}','A separately visible tall, doubly looped mark occupies the space before the following equals. A retraced right brace is the leading reading; the overlap leaves a retrace-only alternative.','low','omission',dh=True,status='retained',crop='01_top_eta_brace.png',refs=['Left top after subscript d−1'])
row('A004-003','Below left box, relation following xf₁',r'\unsure{=|\equiv}',r'=',r'=','Two strong horizontal bars are visible. The paler marks below run downward/obliquely; they supply no complete third horizontal bar.','high',dc=True,status='resolved',crop='02_xf_equality.png',refs=['Below left box'])
row('A004-004','Below xf₁ line, isolated locally struck term',r'\deleted{\unsure{xf_1}}','',r'\deleted{xf_1}','The crossed x at left, tall looped f with a descender, and separate short 1 at right survive the diagonal local strikes.','medium','omission',dc=True,dh=True,status='resolved',crop='03_cancelled_xf.png',refs=['Below xf₁'])
row('A004-005','Left expansion, sign of lower second annotation',r'\inserted{\deleted{\unsure{-}e_{i+1}}}','',r'\inserted{\deleted{\unsure{-|\,}e_{i+1}}}','The lower annotation has e with i+1. The horizontal stroke extends from before e across the annotation and can include a minus or the local strike alone. Both are retained.','low','omission',dc=True,dh=True,status='retained',crop='04_expansion_annotations.png',refs=['Left expansion, lower annotation'])
row('A004-006','Bottom left, first delta expression terminal character',r'\deleted{\delta(e_i e_j)=\unsure{0}}','',r'\deleted{\delta(e_i e_j)=\unsure{0}}','A small upper loop survives immediately after the equals, while the strike thickens and turns at its right. Zero remains a candidate; the terminal stroke cannot be separated securely.','low','omission',dh=True,status='retained',crop='06_delta_zero.png',refs=['Bottom left, first δ'])
row('A004-007','Upper right system, cancelled character in first eᵢf₁ case',r'-\deleted{\unsure{a|0}}\eta_{i+1}',r'-\eta_{i+1}',r'\overset{\inserted{-}}{\deleted{\unsure{a|0}}}\eta_{i+1}','The dark cancelled loop lies below the live short minus. The loop has a right descending/end stroke supporting a, with 0 remaining supportable.','low','omission',dh=True,status='retained',crop='07_upper_right_cancel.png',refs=['Upper right, case after eᵢf₁'])
row('A004-008','Upper right system, live minus above cancelled character',r'-\deleted{\unsure{a|0}}\eta_{i+1}',r'-\eta_{i+1}',r'\overset{\inserted{-}}{\deleted{\unsure{a|0}}}\eta_{i+1}','The minus is on the higher baseline, directly over the locally cancelled loop; the eta follows to the right. The transcription now retains that superposed placement.','high','insertion or placement',dc=True,dh=True,crop='07_upper_right_cancel.png')
row('A004-009','Right formula above the rule, cancelled factor after f₁e₁',r'\deleted{\unsure{f_1}}','',r'\deleted{\unsure{f_1}}','A tall narrow stem with top and bottom loops and a short lower-right stroke remains under retraced diagonal cancellation. f₁ is the strongest surviving reading, but overlap keeps it uncertain.','medium','omission',dh=True,status='retained',crop='09_underlined_cancel.png',refs=['Right, above horizontal rule'])
row('A004-010','Right below rule, locally cancelled expression before brace',r'\deleted{\unsure{-e_i}}','',r'\deleted{\unsure{-e_i}}','A short low bar and looped e-like body survive; a wavy strike runs across them and merges with the brace. The lowered ending remains crowded.','low','omission',dh=True,status='retained',crop='10_lower_brace_cancel.png',refs=['Right, below rule before brace'])
row('A004-011','Right lower system, even-branch eta subscript',r'\eta_{i\unsure{-|+}1}',r'\eta_{i+1}',r'\eta_{i\unsure{-|+}1}','After i, the visible pale stroke runs mainly horizontally toward 1. A minute central rise leaves plus possible. The adjacent odd-row plus has a conspicuous crossing stroke.','low','misread symbol or index',dh=True,status='retained',crop='11_even_branch.png',refs=['Below rule, second case, subscript on η'],consequence='The unresolved mark selects i−1 or i+1 in this factor; the following written result retains i+2. No index was repaired from the algebra.')
row('A004-012','Right lower system, factor immediately after even-branch eta',r'\unsure{e|a}_1',r'e_1',r'\unsure{e|a}_1','The letter has a narrow upper loop, a crossing/retrace, and a lower-right return before a clear 1. The overlap leaves both e and a readings.','medium',status='retained',crop='11_even_branch.png',refs=['Below rule, second case'])
row('A004-013','Right bottom, initials after δη=±e(d−2)',r'\unsure{Q\Phi S|QDS|QPS|QFS}','',r'\unsure{Q\Phi S|QDS|QPS|QFS}','There are three joined characters: a large initial loop with an internal connector, a central vertical and loop/cross, and a final S-shaped curve. The central overlaps retain all supplied candidate readings. No expanded phrase is written.','low','omission',dh=True,status='retained',crop='12_initials.png',refs=['Right bottom','After δη=±e(d−2)','QΦS / QDS / QPS / QFS | expansion uncertain'])
row('A004-014','Below left box, abbreviation after si',r'\deg x',r'\deg x',r'\deg x','Three letters d-e-g are followed immediately by x; no accented additional ending is visible.','high',status='resolved',bbox=half('a',[572,955,681,1034]),refs=['deg | degré'])
row('A004-015','Right lower system, first case condition',r'i\text{ imp}',r'i\text{ impair}',r'i\text{ imp}','The condition ends after the descending p; there is no following a-i-r sequence and no terminal full stop.','high','abbreviation expanded or spelling modernised',dh=True,status='resolved',bbox=half('b',[1183,834,1284,900]),refs=['imp | impair'])
row('A004-016','Right edge inside the left box, between the two eᵢf₁ case baselines','','',r"\unsure{\text{''}}",'Two isolated short black slanting ticks are visible. Their function is unresolved; a quotation/ditto-like pair is represented without expansion.','low','omission',dc=True,dh=True,crop='13_box_marks.png')
# Explicit local checks for the alphabet/sign groups listed in C_doubts.
for id,loc,C,H,rd,ev,bb,refs in [
 ('017','Left boxed first row, eᵢ',r'e_i',r'e_i',r'e_i','The looped e has a short lowered i with a distinct dot.',half('a',[152,580,233,651]),['Box left; bracket right: e_i']),
 ('018','Left boxed second row, fᵢ',r'f_i',r'f_i',r'f_i','The f has a tall upper stroke and a lower loop; the small i is dotted.',half('a',[165,650,233,760]),['Box left; bracket right: f_i']),
 ('019','Left boxed first row, e₁',r'e_1',r'e_1',r'e_1','A looped e is followed by one short lowered straight stroke.',half('a',[234,584,282,654]),['Box left; bracket right: e_1']),
 ('020','Left boxed fᵢf₁ relation, f₁',r'f_1',r'f_1',r'f_1','The tall f is followed by the short angled numeral 1.',half('a',[530,548,581,675]),['Box left; bracket right: f_1']),
 ('021','Bottom-left delta expressions, eⱼ',r'e_j','',r'e_j','The lowered j returns conspicuously left below the baseline; the dot is visible. Both bottom expressions were read.',full([215,1602,610,1715]),['Box left; bracket right: e_j']),
 ('022','Below left box, e(d−1)',r'e_{d-1}',r'e_{d-1}',r'e_{d-1}','The lowered sequence has d, a horizontal minus, and a final 1.',half('a',[908,921,1000,982]),['Throughout: e_{d-1}']),
 ('023','Top left, f(d−2)',r'f_{d-2}',r'f_{d-2}',r'f_{d-2}','The lower index has a short d, a separate minus, and a curled numeral 2.',half('a',[218,227,314,343]),['Throughout: f_{d-2}']),
 ('024','Foot of right column, f(d−3)',r'f_{d-3}',r'f_{d-3}',r'f_{d-3}','The final right-hand f is tall; its lowered d−3 ends in a double-curved 3.',half('b',[828,1681,928,1774]),['Throughout: f_{d-3}']),
 ('025','Left expansion first factor, lambda',r'\lambda',r'\lambda',r'\lambda','The letter has two oblique legs joined at the top and an extended lower right stroke.',half('a',[493,1122,546,1206]),['Left expansion; right system: lambda']),
 ('026','Right upper third row, alpha',r'\alpha',r'\alpha',r'\alpha','The low alpha has a loop and an oblique finishing arm.',half('b',[547,333,603,386]),['Left expansion; right system: alpha']),
 ('027','Right upper third row, beta',r'\beta',r'\beta',r'\beta','The beta has a long stem and two curves to its right.',half('b',[748,325,797,426]),['Left expansion; right system: beta']),
 ('028','Left top, delta',r'\delta',r'\delta',r'\delta','The delta has an open upper hook and a closed lower loop before the argument parenthesis.',half('a',[236,360,285,433]),['Left top and bottom: delta, top']),
 ('029','Left bottom, second delta',r'\delta','',r'\delta','The tall open upper hook descends into a lower loop at the beginning of the unfinished expression.',full([415,1588,484,1690]),['Left top and bottom: delta, bottom']),
 ('030','Right vertical chain, first separator',r'\rotatebox{90}{$=$}',r'= (vertical placement described in H note)',r'\rotatebox{90}{$=$}','Two short parallel strokes descend below the initial left member.',half('b',[325,984,357,1025]),['Right column, lower steps: first']),
 ('031','Right vertical chain, second separator',r'\rotatebox{90}{$=$}',r'= (vertical placement described in H note)',r'\rotatebox{90}{$=$}','Two short parallel strokes stand between eᵢ(f₁e₁) and −eᵢ(e₁f₁).',half('b',[321,1147,356,1183]),['Right column, lower steps: second']),
 ('032','Right vertical chain, third separator',r'\rotatebox{90}{$=$}',r'= (vertical placement described in H note)',r'\rotatebox{90}{$=$}','Two short parallel strokes stand above −(eᵢe₁)f₁.',half('b',[332,1290,365,1328]),['Right column, lower steps: third']),
]:row('A004-'+id,loc,C,H,rd,ev,status='resolved',bbox=bb,refs=refs)
# H-specific structure and content differences, separately located.
row('A004-033','Left boxed range, manuscript parentheses',r'(1\leq i\leq d-2)',r'1\leq i\leq d-2',r'(1\leq i\leq d-2)','A tall opening and closing parenthesis enclose the range.','high','omission',dh=True,bbox=half('a',[338,466,603,549]))
row('A004-034','Left boxed system, left brace',r'\left\{...\right.',r'e_i e_1=0,\qquad f_i f_1=...','Large left brace enclosing the three stacked left relations, with fᵢf₁ to the right of the first relation.','The continuous tall brace has a central inward cusp, covering the stacked eᵢe₁, fᵢe₁, eᵢf₁ relations. H calls the block framed but omits this brace.','high','drawing or diagram',dh=True,bbox=half('a',[86,480,178,893]))
row('A004-035','Below box, order and relative position of xf₁ and eta formulas',r'xf_1=f_1x=0 ... \qquad \eta=e_{d-1} ...',r'\eta=e_{d-1},\delta(e_{d-1})=e_{d-2};xf_1=f_1x=0 ...','xf₁ relation at left; η=e(d−1) and δ(e(d−1))=e(d−2) at its upper right.','The xf₁ line starts at x≈172; eta begins near x≈815 just above that baseline.','high','insertion or placement',dh=True,bbox=full([156,905,1340,1068]))
for id,loc,C,H,rd,bb in [
 ('036','Expansion, first f in first factor',r'f_i',r'f_1',r'f_i',half('a',[382,1118,454,1236])),
 ('037','Expansion, e in first factor',r'e_i',r'e_1',r'e_i',half('a',[543,1147,593,1208])),
 ('038','Expansion RHS, first product first factor',r'f_i f_1',r'f_1 f_1',r'f_i f_1',half('a',[507,1240,601,1374])),
 ('039','Expansion RHS, lambda-squared product first factor',r'e_i e_1',r'e_1 e_1',r'e_i e_1',half('a',[712,1266,808,1336])),
 ('040','Expansion RHS, first cross term first factor',r'f_i e_1',r'f_1 e_1',r'f_i e_1',half('a',[968,1230,1074,1368])),
 ('041','Expansion RHS, second cross term first factor',r'e_i f_1',r'e_1 f_1',r'e_i f_1',half('a',[1103,1228,1222,1369])),
]:row('A004-'+id,loc,C,H,rd,'The first factor carries a short lowered dotted i; the succeeding fixed factor carries 1.','high','misread symbol or index',dh=True,bbox=bb)
row('A004-042','Expansion RHS, first product local strike',r'\deleted{f_i f_1}',r'f_1 f_1',r'\deleted{f_i f_1}','A local oblique stroke crosses this product, separately from the long page diagonal.','high','deletion state (struck given live or live given struck)',dh=True,crop='04_expansion_annotations.png')
row('A004-043','Expansion RHS, lambda-squared product local strike',r'\deleted{e_i e_1}',r'e_1 e_1',r'\deleted{e_i e_1}','A local rising diagonal cuts the eᵢe₁ product after λ².','high','deletion state (struck given live or live given struck)',dh=True,crop='04_expansion_annotations.png')
row('A004-044','Expansion RHS, second cross term local strike',r'\deleted{e_i f_1}',r'e_1 f_1',r'\deleted{e_i f_1}','Two local diagonals cross the term at the large f₁ and continue toward its lower annotation.','high','deletion state (struck given live or live given struck)',dh=True,crop='04_expansion_annotations.png')
row('A004-045','Expansion, annotation under first product',r'\inserted{f_{i+1}}','',r'\inserted{f_{i+1}}','A lower f carries i+1 directly beneath the first struck product. Read on half a; crop 04 includes only its upper part and is not used to decide this annotation.','high','omission',dh=True,bbox=half('a',[527,1374,614,1461]))
row('A004-046','Expansion, annotation under first cross term',r'\inserted{e_{i+1}}','',r'\inserted{e_{i+1}}','A short bracket under fᵢe₁ leads to the lower e with index i+1.','high','omission',dh=True,crop='04_expansion_annotations.png')
row('A004-047','Expansion, underbrackets beneath two cross terms',r'\underbrace{f_i e_1}...\underbrace{e_i f_1}',r'f_1 e_1+e_1 f_1','Two short underbrackets attach the evaluated terms to the respective products.','The two horizontal curved brackets occupy separate intervals under the two cross terms.','high','insertion or placement',dh=True,crop='04_expansion_annotations.png')
row('A004-048','Lower far left, two-line e₂/e₃ block',r'\begin{aligned}e_2&=f_1e_1\\e_3&=f_2e_1\end{aligned}',r'\qquad e_2=f_1e_1,\quad e_3=f_2e_1 .','e₂=f₁e₁ above e₃=f₂e₁ as an independent block at the far left.','The two equalities begin near the left edge and are stacked beside the expansion, rather than appended to its RHS.','high','insertion or placement',dh=True,bbox=half('a',[35,1269,286,1461]))
for id,loc,C,rd,ev in [
 ('049','Upside-down note, first locally cancelled line',r'\deleted{e_1 f_d}',r'\deleted{e_1 f_d}','The rotated crop shows e₁, tall f, lowered d, and one horizontal strike through the whole short expression.'),
 ('050','Upside-down note, main equality',r'e_i e_1=0',r'e_i e_1=0','The looped e factors, lowered i and 1, equals, and zero are readable after rotation.'),
 ('051','Upside-down note, range at right',r'1\leq i\leq d-2',r'1\leq i\leq d-2','Both less-than-or-equal signs and the final d−2 are distinct in the rotated crop.'),
 ('052','Upside-down note, unfinished lower line',r'f_i f_1=',r'f_i f_1=','The two tall f glyphs have lowered i and 1; the equality ends with blank space.'),
]:row('A004-'+id,loc,C,'',rd,ev,'high','omission',dh=True,crop='05_upside_down.png')
row('A004-053','Bottom left, second unfinished delta expression',r'\delta(e_i e_j)=','',r'\delta(e_i e_j)=','The second expression retains its final equals with a blank continuation. Its j descender and closing parenthesis are both visible.','high','omission',dh=True,crop='06_delta_zero.png')
row('A004-054','Upper right system, enclosing brace',r'\left\{...\right.',r'e_i e_1=0,\qquad f_i f_1=...','One tall left brace encloses the upper-right system.','The long vertical upper and lower parts meet at a left-pointing cusp beside fᵢe₁.','high','drawing or diagram',dh=True,bbox=half('b',[177,129,255,605]))
row('A004-055','Upper right fᵢf₁, odd condition',r'\text{si }i\text{ impair}',r'i\text{ impair}',r'\text{si }i\text{ impair}','A small si precedes the distinct next i and the word impair.','high','omission',dh=True,bbox=half('b',[502,166,832,231]))
row('A004-056','Upper right fᵢf₁, even condition',r'\text{si }i\text{ pair}',r'i\text{ pair}',r'\text{si }i\text{ pair}','A small si stands before the following i and pair.','high','omission',dh=True,bbox=half('b',[585,236,833,293]))
row('A004-057','Right formula above rule, underlining',r'\underline{f_1e_1...+\beta f_2}',r'f_1e_1...+\beta f_2','The entire single-line identity has one underline.','A long shallow curved horizontal stroke runs below the identity from near the left column edge past the last factor.','high','omission',dh=True,bbox=half('b',[132,741,1117,823]))
row('A004-058','Right lower even case, local strike through e(i+1)e₁',r'\deleted{e_{i+1}e_1}',r'e_{i+1}e_1',r'\deleted{e_{i+1}e_1}','A local X crosses the added e(i+1)e₁ product.','high','deletion state (struck given live or live given struck)',dh=True,crop='11_even_branch.png')
row('A004-059','First horizontal continuation of right vertical chain',r'\deleted{=e_i\eta_2=e_i(\alpha e_2+\beta f_2)}','',r'\deleted{=e_i\eta_2=e_i(\alpha e_2+\beta f_2)}','A horizontal strike crosses the complete RHS after eᵢ(f₁e₁), including both equals, η₂, and the parenthesized linear combination. The factors and indices remain legible.','high','omission',dh=True,bbox=half('b',[449,1038,986,1146]))
row('A004-060','Right vertical chain layout',r'\begin{gathered}...\end{gathered}',r'\note{...la seconde chaîne...descend verticalement sous le premier membre}',r'\begin{array}{c l}...\end{array}','Each rotated equals falls directly beneath the left member, with the cancelled RHS extending right from the first continuation. The array preserves that physical attachment.','high','insertion or placement',dc=True,dh=False,bbox=half('b',[182,875,990,1404]))
row('A004-061','Lower right result, circle around β=0',r'\tikz...\node[draw,circle]...{$\beta=0$}',r'\beta=0','β=0 enclosed by a hand-drawn circle.','An enclosing curved stroke surrounds the beta equation, with a short overlapping arc at its upper left.','high','drawing or diagram',dh=True,bbox=half('b',[884,1271,1101,1449]))
# Explicit H punctuation has no matching ink at the corresponding locus.
for id,loc,H,rd,bb in [
 ('062','Left box, after eᵢe₁=0',r'e_i e_1=0,',r'e_i e_1=0',half('a',[282,592,372,639])),
 ('063','Left box, after fᵢf₁ cases',r'\end{cases},',r'\end{cases}',half('a',[1015,520,1122,684])),
 ('064','Left box, after fᵢe₁=e(i+1)',r'f_i e_1=e_{i+1},',r'f_i e_1=e_{i+1}',half('a',[329,684,454,743])),
 ('065','Below box, after η=e(d−1)',r'\eta=e_{d-1},',r'\eta=e_{d-1}',half('a',[907,914,1076,986])),
 ('066','Below box, after δ(e(d−1))=e(d−2)',r'\delta(e_{d-1})=e_{d-2};',r'\delta(e_{d-1})=e_{d-2}',full([1170,927,1350,1000])),
 ('067','Below box, after pair',r'\deg x\text{ pair};',r'\deg x\text{ pair}',half('a',[694,965,812,1034])),
 ('068','Expansion, after closing RHS parenthesis',r'\lambda(...),',r'\lambda(...)',half('a',[1186,1234,1268,1399])),
 ('069','Lower far left, after e₂ equality',r'e_2=f_1e_1,',r'e_2=f_1e_1',half('a',[207,1294,309,1364])),
 ('070','Lower far left, after e₃ equality',r'e_3=f_2e_1 .',r'e_3=f_2e_1',half('a',[211,1371,310,1453])),
 ('071','Upper right, after eᵢe₁=0',r'e_i e_1=0,',r'e_i e_1=0',half('b',[346,118,456,174])),
 ('072','Upper right, after fᵢf₁ cases',r'\end{cases},',r'\end{cases}',half('b',[748,165,880,296])),
 ('073','Upper right, after fᵢe₁ linear combination',r'\alpha e_{i+1}+\beta f_{i+1},',r'\alpha e_{i+1}+\beta f_{i+1}',half('b',[815,329,924,426])),
 ('074','Right, after underlined identity',r'\alpha e_2+\beta f_2;',r'\alpha e_2+\beta f_2',half('b',[844,680,996,810])),
 ('075','Right, after lower range',r'1\leq i\leq d-3,',r'1\leq i\leq d-3',half('b',[449,797,544,861])),
 ('076','Lower right, after β=0',r'\beta=0,',r'\beta=0',half('b',[1010,1300,1134,1421])),
 ('077','Lower right, after α=±1',r'\alpha=\pm1,',r'\alpha=\pm1',half('b',[1134,1322,1277,1393])),
 ('078','Lower right, after signed delta result',r'\delta\eta=\pm e_{d-2};',r'\delta\eta=\pm e_{d-2}',half('b',[871,1477,1047,1568])),
 ('079','Foot right, after η=f(d−2)e₁',r'\eta=f_{d-2}e_1,',r'\eta=f_{d-2}e_1',half('b',[602,1612,739,1698])),
]:row('A004-'+id,loc,rd,H,rd,'The expression terminates or continues into blank space at this locus; the punctuation added by H has no separate matching stroke.','high','text not on the page',dh=True,bbox=bb)
# Prose wrappers outside H's notes are separately identified, without counting the notes as manuscript.
row('A004-080','Introduction of left boxed block','',r'Encadré, pour ... :','Only the framed range and equations.','The page has the parenthesized numeric range; H supplies these descriptive words and colon outside its note apparatus.','high','text not on the page',dh=True,bbox=half('a',[330,463,617,547]))
row('A004-081','Introduction of upper-right system','',r'À droite, pour ... :','Only the numeric range and braced equations.','The visible top line is 1≤i≤d−2; H supplies this descriptive wording and colon outside its note apparatus.','high','text not on the page',dh=True,bbox=half('b',[597,51,819,105]))
row('A004-082','Introduction of lower-right range','',r'pour','Only 1≤i≤d−3.','The range begins with 1 and carries no preceding prose word at its left.','high','text not on the page',dh=True,bbox=half('b',[350,801,544,860]))
row('A004-083','Beginning of H horizontal version of descending chain','',r'(e_i f_1)e_1 = e_i(f_1e_1)',r'\rotatebox{90}{$=$}\quad e_i(f_1e_1)','The manuscript continues below the earlier left member using a vertical equals; it writes no second copy of (eᵢf₁)e₁. H’s note correctly describes the vertical layout.','high','text not on the page',dh=True,bbox=half('b',[187,984,458,1145]))
# Resolved coefficient appearance is an inspection note, not a witness difference.
notes={
 'page_content':'A landscape cancelled algebra draft with two main columns. The left gives relations and an expansion in lambda, an independent e₂/e₃ block, an upside-down marginal start, and two delta starts. The right gives a parameterized relation system, a descending associativity calculation, a circled beta result, a signed delta result, and two final identities.',
 'author_uncertainty':{'exact_words':[],'description':'No explicit prose statement of uncertainty was read. Editorial uncertainty is retained only at the recorded ink loci.'},
 'title_date_page_counts':{'title':None,'date':None,'author_page_number':None,'archive_sheet_number':'3','scan':4,'H_page':3},
 'cancellation':'Two long diagonal strokes cross both columns. H acknowledges this whole-page cancellation in its opening note; no false H omission row is assigned for that note. Local strikes are recorded separately.',
 'mathematics_led_reading_decisions':[
  'The upper-right even-case coefficient initially looked like 1+alpha in the half image. Crop 08 shows one vertical numeral 1 immediately touching the minus bar; no separate plus-sign vertical was isolated. The written (1−alpha) is retained from direct ink, with no alteration to the witnesses.',
  'The lower even-case eta subscript remains i−1|i+1. The adjacent expressions were used to locate the mark, not to replace it by the mathematically expected index.',
  'The six dotted i indices in the lambda expansion were read individually. H gives 1 at those places; the proposed page preserves i.',
  'The terminal f(d−3)e₁ is preserved as written. No algebraic repair or proof verification was performed.'
 ],
 'unassigned_surface_traces':[
  {'crop':'14_faint_lower_right.png','description':'Several very pale short curves/vertical traces occur between the signed result and final identities. Their status as recto writing is unresolved, and no legible token is proposed. Their location is retained in a reading.tex comment.'},
  {'crop':'15_faint_lower_left.png','description':'A pale short dash/smudge appears above the e₂ block. The crop shows diffuse traces in the paper background. No legible token is proposed; the location is retained in a reading.tex comment.'}
 ],
 'witness_apparatus':'H note explanations were treated as apparatus, not manuscript words. Three bare descriptive introductions outside H notes and its duplicated left member are reported explicitly so the root can distinguish editorial linearization from literal ink.',
 'crop_scope':'Whole image and each supplied half viewed once. Each of 15 crop files was generated once and viewed once. Crop 04 clips the lower part of the first f(i+1) annotation at the edge; that annotation had already been settled on half a and is supported there. Crop 04’s unresolved lower second annotation is fully contained. No place was recropped.'
}
inv=json.loads((CP/'C_inventory.json').read_text())
for it in inv:
 it.pop('cote',None);it.pop('scan',None)
 it['hand']='his hand'
 if it['element']=='004.21':it['first_words_or_objects']='cancelled a or 0, with live minus directly above'
 if it['element']=='004.13':it['first_words_or_objects']='uncertain minus or no minus, then e(i+1)'
 if it['element']=='004.14':it['first_words_or_objects']='locally struck lower annotation, uncertain minus then e(i+1)'
 if it['element']=='004.25':it['first_words_or_objects']='uncertain cancelled −eᵢ'
 if it['element']=='004.26':it['position']='right lower even case, crossed product'
for el,kind,pos,words,hand in [
 ('004.32','text','right column above descending chain','underlining beneath the entire f₁e₁ identity','his hand'),
 ('004.33','drawing','lower right, around β=0','circle surrounding β=0 with short overlap at upper left','his hand'),
 ('004.34','text','right edge inside left boxed system','two isolated quotation-like ticks, function uncertain','his hand'),
 ('004.35','text','upper left edge of paper','archive numeral 3, recorded in comment','another unnamed hand'),
 ('004.36','drawing','left boxed system boundary','frame with retraced/doubled lower and left edges','his hand'),
]:inv.append({'sheet_kind':'cancelled_draft','hand':hand,'element':el,'kind':kind,'position':pos,'first_words_or_objects':words,'transcribed':'yes'})
notation=[
 {'location':'Left top first parenthetical eta; repeated throughout','reading':r'\unsure{\eta|\gamma}','evidence':'Single shoulder with long right-descending curve and a short left entry hook; first occurrence marked, repetitions use eta.'},
 {'location':'Boxed left relations and right upper system','reading':r'e_i, f_i, e_1, f_1','evidence':'Short lowered dotted i, short separate 1, low-loop e and tall-loop f.'},
 {'location':'Both bottom-left delta expressions','reading':r'e_j','evidence':'Lowered j with a long hooked descender and its dot.'},
 {'location':'Left top and both bottom blocks','reading':r'\delta','evidence':'Open upper hook connected to a lower loop.'},
 {'location':'Left expansion','reading':r'\lambda','evidence':'Two oblique legs; squared occurrence has a distinct raised 2.'},
 {'location':'Right upper system and lower result','reading':r'\alpha,\beta','evidence':'Looped low alpha; tall beta with two right curves.'},
 {'location':'Below left box','reading':r'\deg','evidence':'Written abbreviation deg, without expansion.'},
 {'location':'First lower-right branch','reading':r'\text{imp}','evidence':'Condition stops at p, without a full stop.'},
 {'location':'Three right vertical-chain connectors','reading':r'\rotatebox{90}{$=$}','evidence':'Paired short parallel vertical/slanting strokes at each connector.'},
 {'location':'Lower right two signed results','reading':r'\pm','evidence':'A plus over a separate lower horizontal bar.'},
 {'location':'Right bottom initials','reading':r'\unsure{Q\Phi S|QDS|QPS|QFS}','evidence':'Three joined looped characters; central stroke complex remains unresolved.'},
 {'location':'Inside left box at far right','reading':r"\unsure{\text{''}}",'evidence':'Two short slanting black ticks; no expansion assigned.'}
]
doubts=[
 {'location':d['location'],'reading':d['reading'],'alternatives':alts,'confidence':d['confidence'],'reason':d['evidence'],'crop':d['readers_crop']}
 for d,alts in [(D[0],[r'\gamma']),(D[1],['retrace only']),(D[4],['no minus']),(D[5],[]),(D[6],['0']),(D[8],[]),(D[9],[]),(D[10],['i+1']),(D[11],['a₁']),(D[12],['QDS','QPS','QFS']),(D[15],['function of isolated ticks unresolved'])]
]
report={'scan':4,'reader':'A','start_utc':'2026-11-20T09:33:52.429103+00:00','end_utc':datetime.now(timezone.utc).isoformat(),'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,'halves_detail':['a viewed once','b viewed once'],'differences':D,'doubts':doubts,'inventory':inv,'notes':notes,'notation':notation,'check_events':[],'crops':crops,'brief_feedback':[
 'The brief has no explicit convention for isolated quotation-like ticks with unresolved function; I retained the two visible marks using an unsure text pair and recorded their location.',
 'Very faint unassigned surface traces were documented with crops and comments without inventing a lexical reading; the root can adjudicate their origin.',
 'H has descriptive introductions outside its note macro as well as mathematical linearization. These are separately flagged; its note apparatus is excluded from text-not-on-page rows.',
 'The global cancellation and individual local strikes are distinguishable on this page. H’s opening note records the global state; local states still require separate collation.'
]}
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote report:',len(D),'differences/check entries,',len(doubts),'remaining doubts,',len(inv),'inventory elements,',len(crops),'crops.')
