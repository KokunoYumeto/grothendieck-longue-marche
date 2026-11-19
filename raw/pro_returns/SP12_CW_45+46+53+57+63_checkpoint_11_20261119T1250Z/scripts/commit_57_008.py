from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
slash=r'\mathord{\tikz[baseline=-.25ex,x=1em,y=1em]{\draw[line width=.7pt] (0,-.05)--(.32,.72);\fill (.13,.45) ellipse[x radius=.06em,y radius=.08em];\fill (.14,.18) ellipse[x radius=.06em,y radius=.08em];}}'
suitable=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){a curve};\node[anchor=south,inner sep=0pt] at ([xshift=-.6em,yshift=-1pt]s.north){\inserted{suitable}};}'
crosses=r'\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){xx};}'
blot=r'\mathrel{\tikz[baseline=(s.base)]{\node[inner sep=0pt](s){$\unsure{\longrightarrow|\hookrightarrow}$};\path[fill=gray,opacity=.45] ([xshift=2pt,yshift=2pt]s.west)--([xshift=3pt,yshift=12pt]s.west)--([xshift=6pt,yshift=8pt]s.west)--([xshift=-1pt,yshift=2pt]s.east)--cycle;\draw[gray,line width=.6pt] ([xshift=4pt,yshift=11pt]s.west) to[out=250,in=100] ([xshift=3pt,yshift=5pt]s.west);}}'
dots=r'\qquad\qquad\mathord{\tikz[baseline=-.3ex,x=1em,y=1em]{\fill (.1,0) circle (.35pt);\fill (.3,.3) circle (.35pt);}}'
d={'cote':57,'scan':8,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'\underline{\operatorname{Pic}}_{Z_n/k}',r'\underline{\operatorname{Pic}}_{Z_n'+slash+'k}'),
 (r'\deleted{\unsure{and it}}',r'\deleted{and it}'+crosses),
 (r'a \inserted{suitable} curve',suitable),
 (r'\unsure{locally|focally}',r'\rlap{r}l\rlap{e}ocally'),
 (r'P^{\unsure{o|0}}',r'P^o'),
 (r'\unsure{ixomorphism|isomorphism}',r'i\rlap{x}somorphism'),
 (r'H_s^2(S)',r'H_s^2(S)'+dots),
 (r'\handwritten{the sheaf}',r'\inserted{\handwritten{the sheaf}}'),
 (r'\handwritten{\unsure{\longrightarrow|\hookrightarrow}}',blot),
 (r'H^1(X,i_*(\underline{O}_U))',r'H^1(X,i_{\handwritten{*}}(\underline{O}_U))'),
 (r'\unsure{Thhs|Thus}',r'Th\rlap{i}us'),
 (r'\handwritten{\geq}3',r'\handwritten{\geq 3}'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole sheet and both halves before the two witnesses, then read seven broad 3× crops line by line. Twenty-nine focused crops at 6–18×, including the handwritten the sheaf rotated 6 degrees counterclockwise, and nine supplemental crops at 7–24× covered C doubts, H differences, overprints, cancellations, formula signs and detached marks. One supplemental strip was blank and another fell on already-read type; no new reading was inferred from either. The three lower broad crops that were lost to a truncated tool result were redisplayed and actually inspected before the focused reading. No OCR, delegated reading, context or compilation was used.'}
c=(rv['WIT']/rv['row'](57,8)['codex_file']).read_text()
for n in range(13,18):
 tag=r'\tag*{('+str(n)+')}'
 pos=c.index(tag);i=c.rfind('\\[',0,pos);j=c.index('\\]',pos)+2
 block=c[i:j];inner=block[2:block.index(tag)].strip();current=block
 for old,new in d['replace']:
  inner=inner.replace(old,new);current=current.replace(old,new)
 d['replace'].append((current,'\\[\n\\begin{aligned}\n('+str(n)+r')\qquad\qquad & '+inner+'\n\\end{aligned}\n\\]'))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('cancelled type after above',r'\unsure{x} deleted','omitted','C retained','A serifed x-shaped overstrike has further vertical and curved traces beneath it; the underlying character is not securely separable. (597,177,632,215), 18×.','low',hc=True,k='omission')
a('first Pic subscript slash','plain slash','plain slash','slash with two rounded protrusions drawn','The sloping stroke bears a rounded body on its upper left and another on its lower right, as in 57/7. Neither body is supplied with a punctuation meaning. (934,176,1280,251), 7×.','high',True,True,'drawing or diagram')
a('first X subscript','o','0','C retained','The lowered character is short and round, with the lower-case o form. Both Pic underlines and the right-pointing arrow are separate and visible. Same Pic crop, 7×.',hc=True,k='misread symbol or index')
a('NS morphism X subscript','o','0','C retained','The short round o differs from a full-height zero; both NS operators are plain, without lower lines. The connecting hand-drawn arrow has a clear right head. (402,244,704,300), 8×.',hc=True,k='misread symbol or index')
a('affineness and expectation clauses','is affine ... has finite kernel.) I expect ... always the case','same','C retained','Every word and the unusual period before the closing parenthesis are visible. Top (262,171,1657,432), 3×.')
a('deleted and it',r'\unsure{and it}',r'\ill{} deleted','and it deleted','The a bowl, n arch, d ascender, i dot and t crossbar with curved foot survive the x overstrikes. The reading is resolved for those words. (599,319,765,356), 12×; (681,319,773,357), 20×.','high',True,True,r'readable ink left as \ill{}','yes')
a('two further overstrikes after and it','omitted','omitted','two typed x-shaped marks reproduced','Two further x-shaped type positions follow the t. No underlying word is inferred from the congested last cell. Same deletion crops, 12–20×.','high',True,True,'drawing or diagram')
a('dash before Mumford','single hyphen','double-hyphen dash','C retained','The mark is a short single typewriter hyphen, matching the hyphen inside Du-Val. (521,391,707,429), 10×.',hc=True,k='other')
a('would he','would he','would he','C retained','The first letter of he has a tall left stem and an open h arch, not a closed b bowl. (1538,394,1590,433), 16×.')
a('right-edge definiteness','definiteness','same','C retained','The last two s bodies are crowded at the paper edge, but both upper and lower curved bodies remain visible. (1540,461,1674,501), 10×; (1634,470,1674,501), 24×.','medium')
a('intersection proposal','matric; X-i period C-j','same','C retained','The last letter of matric is open c. The product has raised dotted i and descending j, with a baseline point between X and C. Matrix (258,449,1670,794), 3×; (788,505,936,571), 12×.')
a('component X subscript','o','0','C retained','The lowered component index has the same short round form as the first two X indices. Matrix crop, 3×.',hc=True,k='misread symbol or index')
a('suitable insertion','inline between a and curve','same','typed suitable above a curve','The word is typed in the interline space, beginning above the end of denotes and extending above curve. No insertion guide is visible, so none is drawn. (629,582,942,644), 8×.','high',True,True,'insertion or placement')
a('denotes','denotes','same','C retained','The t has a clear upper stem and crossbar; its lower stroke is broken by a pale patch. The other letters remain legible. Same insertion crop, 8×.')
a('deleted ample','ample deleted','omitted','C retained','The a bowl, m arches, p descender, l ascender and e body survive the x overstrikes. (655,674,762,710), 14×.',hc=True,k='omission')
a('final cancelled plural letter',r'\unsure{s} deleted','live s','C retained','An x covers the last type position after the apostrophe. Curved remnants support s, but the overstrike prevents a secure full letter reading. The following question mark, closing parenthesis and point are distinct. (1432,730,1626,792), 8×; (1518,747,1548,781), 24×.','low',hc=True,k='deletion state (struck given live or live given struck)')
a('conditional definition paragraph','In case (12) is indeed injective ... Q=P/underlined D','same','C retained','The reference (12), every word of the condition and all three formula letters were read. Q and P are plain; D has an independent lower bar. Quotient (258,808,1500,1144), 3×; (631,874,786,931), 10×.')
a('locally first two type positions',r'\unsure{locally|focally}','locally','l/r and o/e overprints followed by cally','The first cell has a tall l stem with its upper left serif, together with a lower r shoulder. The next cell has a closed o outline and an additional e-like middle bar. Both layers are preserved without assigning correction order. (617,950,760,990), 12×; (619,951,671,989), 24×.','high',True,True,'misread word')
a('finite-type emphasis','group-scheme ... over underlined','same emphasis','C retained','The underline begins below group-scheme and stops after over, before k. Quotient crop, 3×.')
a('equation 14 P exponent',r'\unsure{o|0}','0','o','The raised character is short and round like the adjacent Q exponent and the lower-case o in the prose. (609,1009,889,1064), 9×.','high',True,True,'misread symbol or index')
a('equation 14 Q exponent','o','0','C retained','The second exponent has the same short round form. The arrow has a right-pointing head and a separate upper wave; the final comma is visible. Same equation crop, 9×.',hc=True,k='misread symbol or index')
a('equation 15 Q exponent','o','0','C retained','The raised quotient exponent has the same round lower-case form as equation (14). (647,1153,1307,1236), 6×.',hc=True,k='misread symbol or index')
a('equation 15 P exponent','o','0','C retained','The P exponent is also short round o. Both D symbols and NS have their own separate underlines; the nested Z-n/k index, equality and simeq are legible. Same equation crop, 6×.',hc=True,k='misread symbol or index')
a('isomorphism before equation 16',r'\unsure{ixomorphism|isomorphism}','isomorphism','i followed by x/s overprint, then omorphism','The second cell contains crossed diagonals with serifs together with the upper and lower curves of s. Both are reproduced. (264,1307,487,1342), 12×.','high',True,True,'misread word')
a('equation 16 O','underlined O','calligraphic O','C retained','The plain O has a separate lower bar and lowered X. The Lie underline, Q, simeq, cohomology degree 1 and final point are clear. (644,1355,1056,1437), 8×.',hc=True,k='misread symbol or index')
a('equation 17 first O','underlined O-X','calligraphic O-X','C retained','The first upright O has an independent lower bar. (685,1500,1244,1576), 6×.',hc=True,k='misread symbol or index')
a('equation 17 second O','underlined O-U','calligraphic O-U','C retained','The second upright O also has an independent lower bar and lowered U. Same equation crop, 6×.',hc=True,k='misread symbol or index')
a('equation 17 remaining signs','hook arrow; H-1 twice; H-sub-s power 2 of S','same','C retained','The left end of the arrow curves up and back to the right, and the right end is a pointed head. The two degrees 1, degree 2, lower-case s index, equality and parentheses are clear. Same equation crop, 6×.')
a('marks far to right of equation 17','omitted','omitted','two obliquely placed points drawn','Two small dark bodies lie to the right of the formula; the right one is higher. They are detached from the formula and are not assigned a meaning. (1536,1515,1567,1545), 24×.','high',True,True,'drawing or diagram')
a('J in notation list','underlined J','plain J','C retained','A separate horizontal line is clearly visible below J; L also has its own lower line. (1425,1574,1674,1650), 8×.',hc=True,k='misread symbol or index')
a('the sheaf addition','handwritten the sheaf','addition the sheaf','same words, marked as handwritten insertion','The t crossbar, h ascender, e and all letters of sheaf are visible, including the long final f descender at the paper edge. (1541,1576,1674,1650), 12×, rotated 6 degrees counterclockwise. This is a macro-only encoding clarification.')
a('deleted of',r'\unsure{of}','omitted','C retained','The two type positions are heavily overwritten by x strokes and an additional looped mark. The proposed o and f cannot be securely isolated. (257,1653,310,1704), 16×.','low',hc=True,k='omission')
a('quotient sheaf first O','underlined O-U','calligraphic O-U','C retained','The plain O has its own underline. The hand-added star has several distinct rays below i. (336,1649,520,1719), 10×.',hc=True,k='misread symbol or index')
a('quotient sheaf second O','underlined O-X','calligraphic O-X','C retained','The second plain O has a separate bar; X is lowered. The slash and parentheses are clear. Same quotient crop, 10×.',hc=True,k='misread symbol or index')
a('inclusion and composition-series clause','i:U right arrow X ... composition series','same','C retained','The handwritten arrow has a distinct right-pointing head; the colon, parentheses and every word of the clause are legible. (592,1653,1027,1704), 8×; sheaf (251,1651,1671,1857), 3×.')
a('quotients and bound','underlined L power -n; n greater than or equal 1','same','C retained','The L underline is separate; the exponent has a clear minus and n. The hand-drawn inequality has a right-pointing upper angle and a separate lower bar. (609,1715,997,1777), 8×.')
a('H exponent in vanishing clause','o','0','C retained','The exponent is short and round, matching the small o forms elsewhere on the page. Same quotient/bound crop, 8×.',hc=True,k='misread symbol or index')
a('canonical-map first O','underlined O-X','calligraphic O-X','C retained','The first plain O has an independent lower bar and lowered X. (629,1783,1102,1857), 8×.',hc=True,k='misread symbol or index')
a('canonical-map arrow',r'\unsure{\longrightarrow|\hookrightarrow}','hook arrow','C doubt retained, with the overlying blot reproduced','The dark horizontal shaft and right head are clear. A gray-blue triangular overmark above them partly masks the left return, so a plain versus hooked left end remains uncertain. (629,1783,1102,1857), 8×; (792,1789,849,1836), 22×.','low',True,True,'drawing or diagram','yes')
a('canonical-map second O','underlined O-U','calligraphic O-U','C retained','The second plain O has an independent lower bar and lowered U. Both closing parentheses, the outer X and the degree 1 are visible. Same canonical-map crop, 8×.',hc=True,k='misread symbol or index')
a('canonical-map i star','star','star, noted handwritten','same star marked handwritten','The star below the second i has six distinct handwritten rays. The transcription now marks its hand consistently with the first star; the reading itself is unchanged. Same canonical-map crop, 8×.')
a('Thhs/Thus before Lie algebra',r'\unsure{Thhs|Thus}','Thus','Th followed by i/u overprint, then s','The third cell has the upper i dot and central stem together with the two sides and lower turn of u. The two visible layers are retained without choosing a correction order. (1135,1803,1229,1849), 14×; (1140,1807,1226,1847), 22×.','high',True,True,'misread word')
a('last cohomology O','underlined O-U','calligraphic O-U','C retained','The plain O is separately underlined; U is lowered, and the degree 1 and final point are visible. (1369,1860,1559,1928), 10×.',hc=True,k='misread symbol or index')
a('dimension bound and final suggestion','dim. greater than or equal 3; Q discrete; Pic(U) countable','same','C retained','The inequality has both strokes; 3 is also handwritten, with an angled upper part and round lower bowl. The surrounding words, Q and Pic(U) are legible. (1237,1943,1304,1989), 14×; end (251,1854,1641,2072), 3×. Only the handwriting wrapper for 3 is adjusted.')
a('final punctuation','etc, then closing parenthesis and point','etc., then closing parenthesis','C retained','There is no point after etc. A single full stop follows the closing parenthesis. (712,2011,840,2066), 12×.',hc=True,k='other')
for n in range(13,18):
 a('equation '+str(n)+' label','right-side tag','right-side tag','label at left','The typed ('+str(n)+') is at the left prose margin, preceding the centered formula. Whole page, both halves and the appropriate quotient/lie/restrict 3× crop.','high',True,True,'insertion or placement')
d['unresolved']='The cancelled x-shaped position after above, the cancelled s after the final X-i apostrophe, the deleted of, and the canonical-map arrow beneath its triangular overmark remain uncertain. Extra overstrikes and detached points are reproduced without inferring hidden text or a meaning. No order is assigned to the l/r, o/e, x/s and i/u overprints.'
d['inventory']=[
 ['text','top continuation','as recalled above ... morphism ... is affine ... finite kernel.)'],
 ['deletion','after above','x-shaped position uncertain'],
 ['drawing','first Pic subscript','slash with two rounded protrusions'],
 ['insertion','between the two Pic schemes','right arrow','his hand'],
 ['insertion','between the two NS groups','right arrow','his hand'],
 ['text','expectation and normal surface case','I expect ... always the case ... negative definiteness.'],
 ['deletion','after always the case','and it'],
 ['drawing','after deleted and it','two further x-shaped overstrikes'],
 ['text','intersection-matrix proposal','It would he nice ... matric X-i.C-j ... suitable curve ...'],
 ['insertion','above a curve','suitable'],
 ['deletion','before relatively ample','ample'],
 ['deletion','after final X-i apostrophe','s uncertain'],
 ['text','conditional definition','In case (12) is indeed injective ... defining'],
 ['display','equation 13, left label','Q=P/underlined D'],
 ['text','between equations 13 and 14','as a group-scheme locally ... We then have'],
 ['text','first two cells of locally','l/r and o/e overprints'],
 ['drawing','finite-type conclusion','underline ending before k','his hand'],
 ['display','equation 14, left label','P-o right arrow with upper wave Q-o,'],
 ['insertion','equation 14 relation','right arrow and upper wave','his hand'],
 ['text','between equations 14 and 15','an isomorphism for the connected components, and'],
 ['display','equation 15, left label','Q/Q-o=(P/P-o)/underlined D simeq underlined NS-Z-n/k / underlined D,'],
 ['insertion','equation 15 relation','simeq','his hand'],
 ['text','before equation 16','where n is chosen large enough ... yield an isomorphism'],
 ['text','second cell of isomorphism','x/s overprint'],
 ['display','equation 16, left label','underlined Lie(Q) simeq H-1(X,underlined O-X).'],
 ['insertion','equation 16 relation','simeq','his hand'],
 ['text','before equation 17','Let us remark ... injective restriction morphism'],
 ['drawing','under injective','underline','his hand'],
 ['display','equation 17, left label','H-1(X,underlined O-X) hooked right arrow H-1(U,underlined O-U)=H-sub-s power 2(S)'],
 ['insertion','equation 17 relation','hooked right arrow','his hand'],
 ['drawing','far right of equation 17','two oblique detached points','another unnamed hand'],
 ['text','argument following equation 17','as one sees ... notations for underlined J, underlined L, ...'],
 ['insertion','right edge after L comma','the sheaf','his hand'],
 ['deletion','following line start','of uncertain'],
 ['text','sheaf quotient and inclusion','i-star(underlined O-U)/underlined O-X (i:U right arrow X the inclusion) ...'],
 ['insertion','first i subscript','star','his hand'],
 ['insertion','inclusion formula','right arrow','his hand'],
 ['text','composition-series continuation','quotients ... underlined L power -n, n greater than or equal 1, whose H-o is zero ...'],
 ['insertion','bound on n','greater than or equal','his hand'],
 ['text','canonical map','H-1(X,underlined O-X) uncertain arrow H-1(X,i-star(underlined O-U)).'],
 ['insertion','canonical-map relation','right arrow, uncertain left return','his hand'],
 ['drawing','above canonical-map arrow','triangular overmark with curved left trace','his hand'],
 ['insertion','second i subscript','star','his hand'],
 ['text','conclusion','Thus with i/u overprint ... local Picard scheme ... subspace of H-1(U,underlined O-U).'],
 ['text','final parenthetic suggestion','This suggests ... Cohen-Macaulay ... Q discrete ... Pic(U) countable etc ).'],
 ['insertion','last dimension bound','greater than or equal 3','his hand'],
]
rv['commit'](d)
