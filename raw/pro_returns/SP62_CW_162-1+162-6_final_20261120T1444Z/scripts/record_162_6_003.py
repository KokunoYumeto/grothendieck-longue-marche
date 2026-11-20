from records import *
p=page('162-6',3)
tex=r'''\scanpage{3}
\noindent\uuline{$\unsure{\operatorname{Gal}|\operatorname{gal}}(E/\mathbb{Q})\;-\;C(E)$}

\diagram{\(\displaystyle
\begin{array}{@{}l@{\qquad}c|l@{}}
\text{\uline{$W_{\mathbb{R}}^{\unsure{\prime|\cdot}}$}}: & \sigma & \sigma\unsure{x|u}\sigma^{-1}=\bar{x}\\[3pt]
\tikz[baseline=(z.base)]{\node[inner sep=1pt] (z) at (0,0) {$\mathbb{Z}/2$};\node[inner sep=1pt] at (1.7,0) {$\mathbb{C}^{*}$};\draw (-.45,-.22) -- (-.45,-.36) .. controls (.3,-.40) and (1.4,-.65) .. (1.94,-.52) .. controls (2.15,-.47) and (2.18,-.41) .. (2.15,-.28);}
& \mathbb{C}^{*} &
\sigma^{2}=\tikz[baseline=(one.base)]{\node[inner sep=1pt] (one) {$-1$};\draw[rotate around={15:(one.center)}] (one.center) ellipse [x radius=1.05em,y radius=.72em];}
\end{array}
\)}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.25pt] (0,.04) .. controls (1.2,-.10) and (2.4,.05) .. (3.3,0) .. controls (5,-.04) and (5.8,-.27) .. (6.8,-.16) .. controls (8,-.08) and (9,-.18) .. (9.7,-.21);
\end{tikzpicture}}

\[
H^{2}(\mathbb{Z}/2,\mathbb{C}^{*})=\text{\uline{$\mathbb{Z}/2$}}
\]

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.25pt] (0,0) .. controls (.6,.14) and (1.6,.12) .. (3,.09) .. controls (5,.12) and (7.6,-.03) .. (8.5,-.07) -- (9.6,-.16);
\draw[line width=.18pt] (10.04,-.31) -- (10.52,-.35);
\end{tikzpicture}}
\diagram{\(\displaystyle
\begin{array}{@{}l@{\quad}l@{\,}c@{\,}l@{}}
\begin{array}[t]{@{}l@{}}
M\\[2pt]R\;-\;\text{\uline{$\mathbb{C}$}}
\end{array}
&
\begin{array}[t]{@{}l@{}}
{\deleted{H(\mathbb{C})}}^{(\unsure{p\cdot q|p,q|pq|p:q})}\\[2pt]
H(M(\mathbb{C}),\mathbb{R})
\end{array}
&
\begin{array}[t]{@{}c|c@{}}
\sigma & \sigma\\[5pt]
\deleted{\mathbb{C}^{*}} & S
\end{array}
&
\bigg|\;\sigma^{2}=+1\\[-1pt]
&\multicolumn{2}{c}{\displaystyle
\prod_{\unsure{\mathbb{C}|C}/\unsure{\mathbb{R}|R}}\mathbb{G}_{m}\;=}
&
\end{array}
\)}
% archive sheet number: 2
\clearpage
'''
def c(place,C,H,F,S,K='misread symbol or index',conf='high',a='H',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('heading / letter case and underline','double-underlined Gal(E|B/Q) - C(E)','gal(E/Q) - C(E), no double underline',r'double-underlined \unsure{Gal|gal}(E/Q) - C(E)','Crop 162-6/003 (126,41,443,147): large looped initial and tall l; case remains uncertain. The retouched field letter has E’s lower horizontal arms. Whole page shows two sloping underline strokes, not a cancellation.','other','medium')
c('W label / raised trace',r'\unsure{prime|point}','absent',r'\unsure{prime|point}','Crop 162-6/003 (127,211,225,301): a minute high slanted mark to the right of W and above R; its role is not secure. The separate colon farther right is clear.','omission','low')
c('upper conjugation variable',r'\unsure{x|u}; barred x','z; barred z',r'\unsure{x|u}; barred x','Crop 162-6/003 (627,276,933,332): both variables have the same two hooked strokes with a rightward tail; neither has z’s flat upper and lower strokes. A separate overbar belongs to the right occurrence. The dummy-variable role cannot decide x versus u.','misread symbol or index','medium')
c('upper left labels / curved grouping','straight underline beneath Z/2 and C*','described as an accolade beneath labels','curved lower bracket/underline with upturned ends, drawn','Crop 162-6/003 (57,353,330,454): the stroke begins with a short upturn at the left and curves down then up beneath the second label; no central brace cusp. Labels remain side by side, separately from the vertical sigma/C* column.','drawing or diagram','high','CH')
c('upper square relation / enclosure','oval around -1','(-1), with editorial note saying circled','oval around -1','Half b: a single closed tilted oval surrounds minus one; it is reproduced rather than supplied as ordinary parentheses.','drawing or diagram','high')
c('horizontal separators','two drawn long dividers, with short right trace on lower','one verbal trait horizontal; upper divider not reproduced','two drawn dividers and short right trace','Whole page and halves: one divider lies above H^2, one below it; a short faint detached line is near the lower divider’s right end.','drawing or diagram','high')
c('underlines','W_R, result Z/2, lower C underlined','underlines omitted','source underlines retained','Halves a/b: independent lines below W, the right Z/2 of the cohomology equality, and C after the lower R dash.','other','high')
c('lower / struck H argument','H(C) with doubled C','H(E)','H(C) with doubled C','Crop 162-6/003 (371,640,640,767): curved outer C and a short inner stroke remain below the cancellation; there are no three horizontal E arms.','misread symbol or index','high')
c('lower / raised pair',r'(\unsure{p dot q|p,q|pq|p:q})','(p,q)',r'(\unsure{p dot q|p,q|pq|p:q})','Crop 162-6/003 (518,621,634,684): a small round point lies immediately after p; a much fainter fleck lies lower. The first point has no secure descending comma tail.','misread symbol or index','low')
c('lower / live H expression','H(M(C),R), doubled field letters','H(D(E),R)','H(M(C),R), doubled field letters','Crop 162-6/003 (371,640,640,767): inner M has two side stems and a dipped top like the isolated M at left; C is rounded/doubled and R has two close uprights.','misread symbol or index','high')
c('lower / cancelled field group','struck C*','struck ill','struck C*','Half b: doubled C curve and raised asterisk survive the diagonal cancellation; no unknown full word.','readable ink left as \\ill{}','high','H','yes')
c('bottom product and unfinished equality',r'product_{C|mathbb C / R|mathbb R} mathbb G|G_m =','not transcribed; note proposes c_R, tensor product, equals and missing remainder',r'product_{mathbb C|C / mathbb R|R} mathbb G_m =','Crop 162-6/003 (514,777,654,846): capped Pi with two descending legs, low C/R, then G with inner line and cross stroke and low m. The whole/right-half view shows two equals strokes to its right and blank space after them. The edge clips low writing but does not supply a missing right-hand expression.','misread symbol or index','medium','CH','yes')
for a in [('heading field','E|B','E','Retouched lower arms and comparison with C(E) favor E.'),('heading initial','Gal (unmarked)','Gal|gal','Large cursive loop can be a capital or enlarged lower-case g.'),('W high mark','prime|point','retained','Minute high trace; not confidently intentional.'),('conjugation','x|u','retained consistently in both occurrences','Same shape recurs; mathematics does not select the dummy letter.'),('raised pair','p dot q|p,q|pq|p:q','retained','One dark point, lower faint fleck.'),('bottom G','mathbb G|G','mathbb G','Distinct inner upright and cross stroke.')]:certainty(p,*a)
for a in [('heading initial','Gal','gal','medium','Cursive case ambiguity.'),('W raised mark','prime','point; incidental trace','low','Very small separated mark.'),('conjugation variable','x','u','medium','Two joined hooks do not determine letter; z unsupported.'),('raised pair','p dot q','p,q; pq; p:q','low','Unequal small marks between letters.'),('bottom product fields','mathbb C / mathbb R','plain C / R','medium','Tiny doubled-looking strokes close to paper edge.')]:doubt(p,*a)
for k,pos,t in [('display','top heading','double-underlined Gal(E/Q) - C(E)'),('display','upper left','underlined W_R with doubtful prime and colon'),('display','upper array left column','sigma above C*'),('display','upper array right, first line','sigma x sigma^-1 = barred x'),('display','upper array right, second line','sigma² = circled -1'),('drawing','around upper -1','tilted oval enclosure'),('display','beneath W at left','Z/2 and C* with curved underline/bracket'),('drawing','above H^2','first long separator'),('display','middle','H^2(Z/2,C*)=underlined Z/2'),('drawing','below H^2','second long separator and short detached trace'),('display','lower left','M above R - underlined C'),('deletion','lower middle upper line','H(C), with live raised pair (p dot q)'),('display','lower middle raised position','parenthesized p dot q'),('display','lower middle lower line','H(M(C),R)'),('display','lower right register','sigma sigma separated by vertical rule; C* and S below; second vertical rule; sigma²=+1'),('deletion','under first lower sigma','C*'),('display','bottom edge','product_C/R G_m =, no right-hand expression')]:inventory(p,k,pos,t,sheet_kind='text')
p['notation']=[['Heading separator','Single horizontal dash between Gal(E/Q) and C(E); not an arrow.'],['sigma','Loop with rightward upper tail, repeated in both registers; squared in two relations.'],['Conjugation variable','Same ambiguous x|u in the argument and under the bar; not H’s z.'],['Two square relations','Upper sigma²=-1, with -1 enclosed; lower sigma²=+1 with explicit plus.'],['Plain versus doubled fields','Plain R in lower left label; doubled R inside H; tiny product C/R remains uncertain as to doubling.'],['Multiplicative group','G with internal line and cross stroke followed by low m, set mathbb G_m.']]
p['hand']=[['Square-topped M','Isolated M at lower left and the M inside H have matching two sides and a shallow dipped top. Holds at these two occurrences.','H reads inner M as D.'],['C with an inner stroke','Doubled C is curved and has an interior downstroke; no E-like arms in either lower H argument.','H reads both as E.'],['Hooked dummy variable','Two repeated x/u shapes have a low joined hook and rightward exit. Their algebraic role allows either letter.','H z unsupported by shape.'],['Pi versus tensor symbol','Bottom Pi has a long cap and two upright legs; no enclosing circle or crossed tensor mark.','H’s editorial description misidentifies the bottom line.']]
p['abbreviations']=[['Gal / gal','Galois group, probable reading of the heading']]
p['notes']=['The sheet has a twice-underlined Gal(E/Q) - C(E) heading, an upper register giving conjugation and sigma²=-1, the equality H²(Z/2,C*)=Z/2, and a lower register containing M, H(M(C),R), sigma²=+1 and an unfinished product_C/R G_m =. The bottom writing is close to the edge but the equals sign is visible and no right-hand expression can be supplied.', 'Targeted check of the middle equality, conditional on the conjugation action indicated immediately above: a normalized 2-cocycle for the two-element group is determined by a=c(t,t). Its cocycle equation at (t,t,t) requires a=bar(a), so a is a nonzero real number. Changing the normalized 1-cochain value to z multiplies a by z bar(z), a positive real number; conversely every positive real is such a norm. Thus the classes are R*/R_{>0}, with two elements, as the written Z/2 states. The circled -1 gives the negative class. This checks that equality under the displayed action, not the undefined lower H or product notation.', 'The check confirms that the opposite square signs are meaningful; it cannot distinguish x from u, because either can name the conjugated variable. No extra z or missing tensor product was supplied from mathematical expectation. Archive number 2; no date, page count or verbal question mark.']
p['checks']=[['162-6/003-N02',utc().split(' ')[0],'GPT-6 Astra Pro; effort not exposed; SP62 second pass; /root','targeted proof check','With C2 acting on C* by conjugation, normalized cocycles are a in R*, and coboundaries multiply by |z|². The quotient has positive and negative classes, hence is Z/2. This checks the written H² equality under that action only.']]
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
