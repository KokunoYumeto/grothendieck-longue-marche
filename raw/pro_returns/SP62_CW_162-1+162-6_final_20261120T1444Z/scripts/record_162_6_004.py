from records import *
p=page('162-6',4)
tex=r'''\scanpage{4}
\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=1.8em,
execute at end picture={\draw[line width=.25pt] ([xshift=-2pt,yshift=-2pt]dom.south west) -- ([xshift=-2pt,yshift=-5pt]dom.south west) -- ([xshift=2pt,yshift=-5pt]gm.south east) -- ([xshift=2pt,yshift=-2pt]gm.south east);}]
N\unsure{\mathpunct{;}|\mathpunct{:}}\& |[alias=dom]| S_E \arrow[r] \& S_{\mathbb{Q}}\arrow[r] \& |[alias=gm]| {\mathbb{G}_{m}}
\end{tikzcd}}

\[
(x,(y_{\alpha}))\longrightarrow x\cdot
\prod_{\alpha<\infty}\lVert y_{\alpha}\rVert\cdot
\prod_{\alpha=\infty}\operatorname{sign}(y_{\alpha})
\]

\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=2.1em,
execute at end picture={\begin{scope}[shift={([xshift=-1.3em,yshift=.1em]csource.north west)},x=1em,y=1em]
\draw[line width=.35pt] (0,0) .. controls (.04,.63) and (.23,1.28) .. (.38,1.65) .. controls (.33,1.12) and (.16,.46) .. (.1,0) -- (0,0);
\end{scope}}]
|[alias=csource]| C(E)\arrow[r]\arrow[rr,bend right=24,swap,"{\text{\uuline{$\lVert x\rVert$}}}"] \&
S_E\inserted{(\mathbb{A})}\arrow[r] \&
{\tikz[baseline=(secondS.base)]{\node[inner sep=0pt] (secondS) {$S$};\draw[gray,line width=.28pt] ([xshift=.35pt,yshift=.4pt]secondS.west) -- ([xshift=-.1pt,yshift=1.05pt]secondS.east);}}_{\unsure{E|\epsilon}}(R)\arrow[r] \& \mathbb{R}^{*}
\end{tikzcd}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.25pt] (0,0) .. controls (.8,.01) and (1.7,.23) .. (2.6,.17) .. controls (3.8,.04) and (4.8,.18) .. (5.9,.14) .. controls (7,.08) and (7.8,.22) .. (8.5,.18);
\end{tikzpicture}}
\figure{\begin{tikzpicture}
\node[inner sep=3pt] (ineq) {$-1\ne\lVert-1\rVert\unsure{\mathpunct{.}|\mathpunct{:}}$};
\draw[line width=.25pt] ([xshift=-1pt]ineq.south west) .. controls ([xshift=-3pt]ineq.west) and (ineq.north west) .. ([xshift=6pt,yshift=1pt]ineq.north west);
\draw[line width=.25pt] ([xshift=6pt]ineq.north west) .. controls (ineq.north) and (ineq.north east) .. ([xshift=2pt]ineq.east) -- (ineq.south east);
\end{tikzpicture}}
% archive sheet number: 3
\clearpage
'''
def c(place,C,H,F,S,K='misread symbol or index',conf='high',a='H',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('top / N punctuation',r'\unsure{;|:}',':',r'\unsure{;|:}','Crop 162-6/004 (111,58,205,120): a high point and longer downward curved lower trace favor semicolon, though colon remains possible.','other','medium')
c('top / bracket under chain','bracket under S_E through G_m','not reproduced','bracket under S_E through G_m','Half a/b: one lower rule begins just left of S_E, extends beneath all three objects, and turns upward after G_m.','drawing or diagram','high')
c('pair / arrow','ordinary right arrow','mapsto','ordinary right arrow','Half a: the shaft begins as a plain horizontal stroke; there is no perpendicular starting bar.','misread symbol or index','high')
c('first product / bound','alpha < infinity','alpha not-equal infinity','alpha < infinity','Half a/b: two strokes meet at a left-pointing angle; there is no second parallel bar or crossing slash of not-equal.','misread symbol or index','high')
c('middle / narrow left mark','narrow closed pencil mark','omitted','mark reproduced in TikZ','Half a: two close tapering slants form a narrow unlabelled shape left of C(E). It is neither supplied as a numeral nor omitted.','drawing or diagram','high')
c('middle / argument addition',r'S_E inserted (mathbb A|A)','S_E(mathbb A)',r'S_E inserted (mathbb A)','Crop 162-6/004 (411,473,718,590): doubled left obliques and a right leg within parentheses sit high across the start of the outgoing arrow; the argument is attached to S_E and retains its raised/interpolated placement.','insertion or placement','high')
c('middle / second S argument','S_{E|epsilon}(R), plain R','S_E(mathbb R)','S_{E|epsilon}(R), plain R','Same crop (411,473,718,590): R has one main stem and a diagonal leg, unlike the doubled R at the final object. The low E/epsilon has angled top and curved lower trace; not resolved by context.','misread symbol or index','high')
c('middle / pale overtrace','short pale stroke across upper S','omitted','short pale stroke retained, no whole-S deletion','Same crop: an oblique light line crosses only the upper part of S and extends a little left; no line cancels the full S(R) object.','drawing or diagram','medium')
c('middle / curved arrow endpoint','C(E) to third object S_{E|epsilon}(R), label norm x double-underlined','editorial note says C(E) to final R*','drawn to third object, with label double-underlined','Crop 162-6/004 (596,555,883,631): the curved arrowhead ends beneath the right edge of S(R), before the short arrow leading to R*. It does not reach the final R*. The visible endpoint is retained, without extending the curve to an expected composite target.','drawing or diagram','medium')
c('bottom / divider and open contour','drawn divider and open contour around inequality','verbal divider description; parentheses around inequality','drawn divider and open contour','Halves a/b: long horizontal line separates lower inequality; its outline goes above and down both sides but stays open below. These are not ordinary parentheses.','drawing or diagram','high')
c('bottom / punctuation',r'\unsure{:|.}','absent',r'\unsure{.|:}','Crop 162-6/004 (583,764,665,825): one strong dark point lies after the double norm bar; a lower faint fleck could give a colon but may be paper/scan texture. The single point is now preferred.','other','low','CH')
for a in [('N punctuation',';|:','retained','Longer lower curl favors semicolon but not conclusive.'),('middle A','mathbb A|A','mathbb A','Close doubled left obliques separate from opening parenthesis.'),('second S index','E|epsilon','retained','Small angular upper and curved lower trace; neighboring E forms do not settle this token.')]:certainty(p,*a)
for a in [('N punctuation','; ',':','medium','Lower trace is curved but pale.'),('second S index','E','epsilon','medium','Small rounded low sign.'),('bottom punctuation','. ',':; incidental marks','low','Only one point strongly dark; another is faint.')]:doubt(p,*a)
for k,pos,t in [('diagram','top','N; S_E to S_Q to G_m, lower bracket'),('drawing','beneath top objects','bracket with two upturned ends'),('display','upper middle','(x,(y_alpha)) to x product_alpha<infinity norms times product_alpha=infinity sign'),('drawing','left of C(E)','narrow tapering closed pencil mark'),('diagram','middle','C(E) to S_E(A) to S_{E|epsilon}(R) to R*; curved arrow from first to third'),('insertion','first S argument across outgoing shaft','(A), doubled A'),('drawing','on second S','short pale oblique overtrace'),('display','below curved arrow','double-underlined norm x label'),('drawing','lower separator','long slightly curved horizontal'),('display','bottom','-1 not equal norm -1, doubtful point'),('drawing','around bottom inequality','open-bottom outline')]:inventory(p,k,pos,t,sheet_kind='text')
p['notation']=[['Index conditions','First product alpha<infinity, second alpha=infinity; < is not normalized to not-equal.'],['Element arrow','Ordinary right-pointing arrow after the pair; no mapsto starting bar.'],['Norm notation','Two strokes on each side of y_alpha, x and -1; curved-arrow norm x label double-underlined.'],['Arrow endpoint','Long curved head is beneath S(R), before the separate arrow to R*. Source geometry determines the transcription.'],['Fields','Doubled A in the interpolated argument; plain R in S(R), doubled R at the final R*.']]
p['hand']=[['Less-than versus not-equal','The product index has a clear angle <; the bottom inequality has two short horizontal strokes crossed obliquely. Each is distinct on this sheet.','H rewrites the product condition as not-equal.'],['Low E versus epsilon','Second S index is smaller and more rounded than the first S_E; remains marked rather than normalized.','H silently resolves as E.'],['One dark point with faint companion','Bottom inequality has one dark point and one weak fleck, unlike the two dark points on 162-6/002.','C preferred colon; final prefers point with doubt.']]
p['abbreviations']=[['sign','sign function; written as four letters']]
p['notes']=['The sheet gives a chain N; S_E to S_Q to G_m, an explicit product involving norms and sign factors, a second chain from C(E) through two S objects to R*, and the outlined inequality -1 ≠ norm(-1). The first product condition is written alpha<infinity; no mathematical convention warrants replacing the visible angle with not-equal.', 'The long curved arrow labelled norm(x) visibly stops beneath the third object S(R), before the separate final arrow to R*. This differs from H’s statement that it reaches the final term. Its intended mathematical composite cannot be settled from the undefined S notation on this sheet; the drawn endpoint controls the diagram.', 'Elementary conditional check: for the ordinary absolute-value norm, norm(-1)=1, hence -1≠norm(-1); more generally any norm valued in positive reals gives the displayed inequality. This checks the sign distinction, not the complete adelic formula or the meaning of S_E. No written question mark is present; the tiny marks after the inequality are doubtful punctuation. Archive number 3; no date or page count.']
p['checks']=[['162-6/004-N03',utc().split(' ')[0],'GPT-6 Astra Pro; effort not exposed; SP62 second pass; /root','used and rechecked in this run','Conditional check of the bottom sign distinction: ordinary absolute value gives |-1|=1, so -1≠1. The same inequality follows if the displayed norm has positive-real values. No proof of the product or arrow-chain construction is claimed.']]
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
