from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]
rv=runpy.run_path(str(root/'scripts/review.py'))
upcap=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.45pt] (0,0)--(1,0)--(1,.12);}}'
hookhead=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.45pt] (0,0)--(1,0) (.88,.10)--(1,0)--(.98,-.19)--(.91,-.20);}}'
leftcurve=r'\mathrel{\tikz[baseline=-.3ex,x=1em,y=1em]{\draw[line width=.45pt] (1,0)--(.08,.02) (.16,.10) .. controls (-.02,.05) and (-.02,-.12) .. (.17,-.17);}}'
d={'cote':57,'scan':3,'sheet_kind':'typescript','hand':'typewriter','replace':[
 (r'\deleted{\unsure{X}}',r'\deleted{\unsure{Mr|Xx|X}}'),
 (r'\deleted{\unsure{gro}}',r'\deleted{gro}'),
 (r'\deleted{some}',r'\deleted{som}e'),
 (r'$k$-valued',r'$k$-val\unsure{ae|ue}d'),
 (r'\handwritten{\longleftarrow}',r'\handwritten{'+leftcurve+'}'),
 (r'\handwritten{\xrightarrow{\sim}}',r'\handwritten{\overset{\sim}{'+hookhead+'}}'),
 (r'$P_m\handwritten{\longrightarrow}P_n$ $(m',r'$P_m\handwritten{'+upcap+r'}P_n$ $(m'),
 ],'decisions':[],'inventory':[],
 'review':'The primary reader inspected the whole sheet, then both supplied halves, then C and H. H has the title immediately before its page marker; that title was included in the comparison. Six broad crops at 3–6× were read line by line, followed by eighteen focused crops at 8–14× of every cancelled or doubtful passage, disputed subscript, mathematical connector, relation, product sign and exponent. The prose is horizontal typescript; the handwritten additions are upright, so no rotation was required on this sheet. Every agreed word, punctuation mark and formula was read against the ink, including the visibly congested letters in k-valued. The inventory distinguishes typing and handwritten additions. No OCR, context, delegated reading or compilation was used.'}
# Handwritten equation numbers are at the left of the expressions, not right tags.
for n in (1,2,3):
 old='\\[\n'
 # The exact display is obtained from C; replacements are applied sequentially by commit.
 c=(rv['WIT']/rv['row'](57,3)['codex_file']).read_text()
 tag='\\tag*{\\handwritten{('+str(n)+')}}'
 pos=c.index(tag);start=c.rfind('\\[',0,pos);end=c.index('\\]',pos)+2
 block=c[start:end]
 inner=block[2:block.index(tag)].strip()
 for source,target in d['replace']:inner=inner.replace(source,target)
 current=block
 for source,target in d['replace']:current=current.replace(source,target)
 replacement='\\[\n\\begin{aligned}\n\\handwritten{('+str(n)+')}\\qquad\\qquad & '+inner+'\n\\end{aligned}\n\\]'
 d['replace'].append((current,replacement))
def a(p,c,h,f,s,cf='high',cc=False,hc=False,k='other',m='no',q=None):
 x=dict(place=p,c=c,h=h,final=f,shows=s,confidence=cf,c_changed=cc,h_changed=hc,kind=k,marked_in_H=m)
 if q:x['consequential']=q
 d['decisions'].append(x)
a('heading underline','underlined Local Picard schemes','section heading without underline','C retained','A continuous independent line runs beneath all three words and stops before the point. (265,151,685,202), 6×.',hc=True,k='insertion or placement')
a('heading final point','point','none','C retained','A separate round typed point follows schemes outside the underline. Same crop.',hc=True,k='omission')
a('cancelled text after ring comma',r'\unsure{X}','omitted',r'\unsure{Mr|Xx|X}','Two type positions are occupied. The first has two tall serifed sides and a middle valley-like remnant; the second has an r-like upper return over a clear x-shaped crossing. Heavy overprinting prevents a secure reconstruction; Mr is a visual candidate, not an inferred word. (972,244,1024,281), 14×.','low',True,True,'omission')
a('opening definitions','A complete local ring; S=Spec(A); U=S-{s}','same','C retained','Every typed letter and equality is visible. The lower-case s has two bowls; the braces are thin handwritten marks with middle returns, one on each side. Paragraph (268,236,1669,642), 3×; braces (1388,232,1453,296), 12×.')
a('interprete spelling','interprete','same','C retained','The typed verb ends in a distinct e after the t, and is preserved without correcting its spelling. Paragraph crop, 3×.')
a('cancelled gro',r'\unsure{gro}','omitted','gro deleted','The descending lower loop of g, upright/shoulder of r and closed oval of o remain discernible under the typed x overstrikes. (1582,316,1656,354), 12×.','medium',True,True,'omission')
a('som cancellation and final e','whole some deleted','omitted','som deleted, e live','The first three type positions carry independent x-shaped overstrikes; the last e has its ordinary upper bowl, horizontal bar and lower curve without an overstrike. No cancellation of the final e is supplied from the apparent intention. (580,385,670,425), 12×.','high',True,True,'deletion state (struck given live or live given struck)')
a('two crowded letters in k-valued','ue','ue',r'\unsure{ae|ue}','The first crowded body after l has two white counters, resembling a more open a; the next has a heavy upper body and curved lower e-like opening. Both positions are much more congested than the surrounding type, and ue remains an alternative. No order of overtyping is assigned. (1037,386,1197,425), 10×.','low',True,True,'misread word')
a('remaining first paragraph','group P(k) ... proper morphism','same','C retained','The capital P and lower k, group-scheme hyphen, residue field k of A, regularity of U, comma before and, resolution of singularities, not changing U, and i.e. are all visible. Paragraph crop, 3×.')
a('f display','f colon X right-arrow S','same','C retained','The typed colon has two separate points. The handwritten shaft has a definite two-armed pointed right head. Middle (260,663,1638,1144), 3×.')
a('cancelled last letter of isomorphisms',r'\deleted{\unsure{s}}','omitted','C retained','A single lower-case type body is densely overstruck by x; curved remnants support s, but the upper and middle shape is masked. (711,744,752,775), 14×.','low',hc=True,k='omission')
a('first inverse-image isomorphism','f inverse(U) simeq U','same','C retained','The exponent has a distinct minus and serifed 1; the handwritten relation has one upper wave and one lower straight bar. (891,743,946,780), 14×; middle crop, 3×.')
a('closure clause','such that X be regular and equal to the closure ...','same','C retained','The printed be, both occurrences of X/f-inverse(U), and complete parenthetical phrase ending with U and a point are visible. No wording is normalized. Middle crop, 3×.')
a('first special-fiber subscript','letter o','numeral 0','C retained','The subscript is a short nearly round lower-case type body, about the x-height of the prose o. The typed zero in equation (1) is distinctly taller and more elongated. (349,883,398,938), 12×; comparison (1171,1090,1208,1130), 12×.',hc=True,k='misread symbol or index')
a('subscript in U=X-X-o','letter o','numeral 0','C retained','The smaller circular lower type form repeats the first o, whereas the X and the zero of the later sequence have full-height bodies. (833,951,886,1007), 12×.',hc=True,k='misread symbol or index')
a('U display and exactness introduction','U=X-X-o; point; Because X is regular ...','same except subscript','C retained','The subtraction is one short heavy horizontal, followed by a separate typed point. The next sentence says exact sequence without a final colon. Middle crop, 3×.')
a('equation 1 objects and connectors','D to Pic(X) to Pic(U) to 0; comma','same','C retained','Each handwritten connector has a shaft and a small pointed right ending, with a descending arm; the objects, both parentheses and final tall zero and comma are clear. (675,1084,1237,1139), 8×.')
a('equation 1 label position','right-side tag','right-side tag','handwritten (1) at left','The parenthesized handwritten 1 stands near the left prose margin, well left of D. Middle crop, 3×. The source display is adjusted to preserve that order.','high',True,True,'insertion or placement')
a('subscript in concentrated-on phrase','letter o','numeral 0','C retained','The round lower-case type body beneath X matches the first two o subscripts and is smaller than the capital X. Divisors (268,1165,1634,1424), 3×.',hc=True,k='misread symbol or index')
a('free group and exponent','underlined Z power I','same','C retained','The capital Z has an independent lower horizontal; the raised I has both top and bottom serifs. The next I in the prose is the same full-height character. Divisors crop, 3×.')
a('subscript in components phrase','letter o','numeral 0','C retained','The round lowered o repeats the earlier small type body; the following closing parenthesis and point are separately visible. Divisors crop, 3×.',hc=True,k='misread symbol or index')
a('existence-theorem clause','On the other hand ... it is known that','same','C retained','The comma after hand, existence theorem, coherent sheaves and comma before it are all visible. Divisors crop, 3×.')
a('equation 2 relation and arguments','Pic(X) simeq lim-n Pic(X-n),','same','C retained','A handwritten upper wave and separate lower bar lie between Pic(X) and lim. The target X has lower n and a closing parenthesis, followed by a typed comma. Limits (260,1437,1657,1718), 3×.')
a('limit arrow shape','ordinary left arrow under lim','standard projective-limit arrow','left-curved endpoint under lim drawn','The horizontal runs from right to left into a short curved C-shaped return with unequal upper and lower arms, above the separate n. It is reproduced graphically. (819,1450,889,1523), 12×.','high',True,True,'drawing or diagram')
a('equation 2 label position','right-side tag','right-side tag','handwritten (2) at left','The handwritten parenthesized 2 lies near the left margin, before the centered Pic expression. Limits crop, 3×.','high',True,True,'insertion or placement')
a('fiber-product sign','typed lower-case x','times','C retained','The small x has four horizontal serif feet and is lower than the preceding capital X; it is a typewriter letter, not a diagonal multiplication glyph. S is lowered beneath it. (389,1510,554,1578), 10×.',hc=True,k='misread symbol or index')
a('infinitesimal-base formula','S-n=Spec(A/underlined m power n+1)','same','C retained','The m has two low arches with an independent underline. The exponent has n, a two-stroke plus and serifed 1, and the closing parenthesis and following point are present. (820,1505,925,1558), 12×; limits crop, 3×.')
a('existence of P-n phrase','Assume we can find group schemes P-n over k and isomorphisms','same','C retained','All words are plainly typed. The lower n is attached to P on the following line; isomorphisms has an unstruck final s. Limits crop, 3×.')
a('equation 3 connector','ordinary right arrow with sim','same','wave above shaft with hooked right head','A separate upper wave lies over the shaft. The right endpoint has a short upward angled stroke and a long downward return ending in a leftward hook. (790,1651,855,1705), 12×.','high',True,True,'drawing or diagram')
a('equation 3 objects','Pic(X-n) and P-n(k),','same','C retained','Both lower n forms, both pairs of parentheses and the final comma are visible. Limits crop, 3×.')
a('equation 3 label position','right-side tag','right-side tag','handwritten (3) at left','The handwritten 3 has two rightward lobes and is enclosed in parentheses near the left prose margin. Limits crop, 3×.','high',True,True,'insertion or placement')
a('first transition connector','ordinary right arrow','same','horizontal with upward right cap','The horizontal has only a short upward stroke at its right end, with no descending head arm. (824,1731,874,1766), 14×.','high',True,True,'drawing or diagram')
a('transition inequality','m greater-than-or-equal n','same','C retained','The upper mark points right and a separate low curved bar lies beneath it; m and n and both parentheses are typed. (1013,1729,1042,1768), 14×.')
a('transition compatibility prose','compatible ... Denoting by P the pro-group (P-n),','same','C retained','Every word, the full point after Pic(X-n), the hyphen of pro-group, the enclosing parentheses and comma are visible. End (267,1718,1660,2053), 3×.')
a('second transition connector','right arrow','same','C retained','The shaft ends in both an upper short arm and a long oblique lower arm. A paper stain below it is not transcribed as ink. (1361,1881,1432,1911), 14×.')
a('closing paragraph','or if one prefers ... and an isomorphism','same','C retained','The commas, affine, inverse limit, (EGA IV 8), P-n, pro-group scheme, resp. and group-scheme P all remain visible through minor paper staining. The line ends at isomorphism without final punctuation. End crop, 3×.')
d['unresolved']='The cancelled opening type group Mr/Xx/X; the crowded ae/ue in k-val...d; and the cancelled final s after isomorphism. Lower-case o is retained for all four special-fiber subscripts after direct comparison with the taller typed zero. The final e after cancelled som is visibly unoverstruck and is kept live without inferring the typist’s intention.'
d['inventory']=[
 ['text','heading','Local Picard schemes.'],
 ['text','opening paragraph','Let A be a complete local ring ... a proper morphism'],
 ['deletion','after opening ring comma','Mr/Xx/X'],
 ['insertion','around s in U definition','handwritten braces','his hand'],
 ['deletion','after first Picard','gro'],
 ['deletion','after as','som; final e remains live'],
 ['display','first display','f: X to S'],
 ['insertion','first display connector','handwritten right arrow','his hand'],
 ['text','after first display','inducing an isomorphism ... Let X-o be the special fiber of X, so that'],
 ['deletion','end of isomorphisms','s uncertain'],
 ['insertion','within inverse-image formula','handwritten simeq','his hand'],
 ['display','second display','U=X-X-o.'],
 ['text','before equation 1','Because X is regular, we have an exact sequence'],
 ['display','equation 1','D to Pic(X) to Pic(U) to 0,'],
 ['insertion','left of equation 1','(1)','his hand'],
 ['insertion','equation 1','three handwritten connectors','his hand'],
 ['text','after equation 1','where D is the group of divisors ... it is known that'],
 ['display','equation 2','Pic(X) simeq lim-n Pic(X-n),'],
 ['insertion','left of equation 2','(2)','his hand'],
 ['insertion','equation 2','simeq and left-curved limit arrow','his hand'],
 ['text','after equation 2','where X-n=X x-S S-n ... P-n over k and isomorphisms'],
 ['display','equation 3','Pic(X-n) to P-n(k),'],
 ['insertion','left of equation 3','(3)','his hand'],
 ['insertion','equation 3','wave above hooked right arrow','his hand'],
 ['text','last paragraph','and transition morphisms ... and an isomorphism'],
 ['insertion','first P-m to P-n','capped connector and greater-than-or-equal sign','his hand'],
 ['insertion','second P-m to P-n','handwritten right arrow','his hand'],
 ['text','bottom left','2 (archive sheet number; retained as comment)','another hand'],
]
rv['commit'](d)
