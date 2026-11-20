from records import *
p=page('162-6',2)
tex=r'''\scanpage{2}
\[
\begin{aligned}
\gamma_{\mathbb{R}}(s)&=\pi^{\frac{s}{2}}\,\Gamma\bigl(\tfrac{s}{2}\bigr)\\[4pt]
\gamma_{\mathbb{C}}(s)&=\tfrac{1}{2}\,\deleted{\unsure{\tfrac{1}{2}|2}}\,(2\pi)^{s}\,\Gamma(s)
\end{aligned}
\]
\figure{\begin{tikzpicture}[x=.75cm,y=.75cm]
\draw[line width=.25pt] (0,0) .. controls (2,.05) and (4.5,.13) .. (6,.04) .. controls (7.5,0) and (9,-.12) .. (10,-.14);
\end{tikzpicture}}

\[
\begin{aligned}
&\begin{aligned}[t]
&\text{\uline{$\mathbb{R}$}}\\[6pt]
&n=2p
\end{aligned}
\quad
\prod_{p<q}\gamma_{\mathbb{C}}(s-p)^{h(p,q)}\cdot
\left\{\begin{array}{@{}l@{\quad}l@{}}
h_{p}^{+}: & F=(-1)^{p}\\
h_{p}^{-}: & F=\deleted{\unsure{(-1)|(1)|(}}-(-1)^{p}\\[2pt]
\multicolumn{2}{@{}l@{}}{\displaystyle {}\cdot\gamma_{\mathbb{R}}(s-p)^{h_{p}^{+}}\,\gamma_{\mathbb{R}}(s-p+1)^{h_{p}^{-}}}
\end{array}\right.
\end{aligned}
\]

\[
\text{\uline{$\mathbb{C}$}}\qquad
\prod_{pq}\gamma_{\mathbb{C}}\bigl(s-\inf(p,q){\bigr)\rlap{\(\unsure{\mathpunct{:}|\mathpunct{.}}\)}}^{h(p,q)}
\]
% archive sheet number: 1
\clearpage
'''
def c(place,C,H,F,S,K='misread symbol or index',conf='high',a='H',m='no'):change(p,place,C,H,F,S,K,conf,a,m)
c('gamma C / cancelled coefficient',r'\deleted{\unsure{1/2|2}}',r'\ill, cancellation mentioned in editorial note',r'\deleted{\unsure{1/2|2}}','Crop 162-6/002 (387,190,443,285): a short upper upright, horizontal middle and curved lower foot survive the crossing. A duplicate 1/2 is favored, with 2 retained; the live 1/2 stands separately to the left.','readable ink left as \\ill{}','low','H','yes')
c('horizontal divider','drawn separator','verbal description of separator','drawn separator','Whole and both halves: one long shallow curved horizontal separates definitions from products. It is reproduced in TikZ; H’s descriptive sentence is not source writing.','drawing or diagram','high')
c('real and complex labels','underlined field labels, n=2p below real label','Cas R, avec n=2p :; Cas C :','underlined field labels, n=2p below real label','Halves a/b: only the doubled field letters and their underlines are written at the left; n=2p is below R. No Cas or avec appears.','text not on the page','high')
c('lower F / earlier state',r'\deleted{\unsure{(-1)|(1)|(}} before -(-1)^p','only final -(-1)^p in text; earlier state described in note',r'\deleted{\unsure{(-1)|(1)|(}} before -(-1)^p','Crop 162-6/002 (851,382,980,449): lighter parenthesis and upright traces are overlaid by the darker final -(-1)^p. The earlier group is uncertain; the final minus before the opening parenthesis is dark and separate.','omission','low','H','yes')
c('brace / final row','leading multiplication point','no leading point','leading multiplication point','Half b: a dark point sits immediately left of the first gamma in the bottom line within the brace.','misread symbol or index','high')
c('bottom / product index',r'\unsure{pq|p,q}','p,q','pq','Crop 162-6/002 (175,690,245,747): p and q are closely joined; no independent comma is visible between them. The commas in the two h(p,q) exponents are separately confirmed by crops (516,312,630,368) and (641,585,768,647).','misread symbol or index','medium')
c('bottom / points after argument',r'\unsure{:|.}','absent',r'\unsure{:|.}','Crop 162-6/002 (639,632,681,692): two unequal dark points, one high and one lower, to the right of the large closing parenthesis and below h. They may be punctuation or incidental marks; their apparent colon is retained with doubt.','omission','low')
for a in [('cancelled coefficient','1/2|2','retained','Crossed numerator/bar/foot do not fully settle the earlier coefficient.'),('lower F earlier state','(-1)|(1)|(','retained','Earlier light curves cannot be separated completely from final writing.'),('bottom product','pq|p,q','pq','No distinct comma in the enlarged index.'),('bottom points',':|.','retained','Two visible points, but intention remains uncertain.')]:certainty(p,*a)
for a in [('top cancelled coefficient','1/2','2','low','Crossing obscures original middle and foot.'),('lower F cancelled state','(-1)','(1); opening parenthesis only','low','Multiple pencil states overlap.'),('bottom points',':','. or incidental marks','low','Point positions are clear but semantic role is not.')]:doubt(p,*a)
for k,pos,t in [('display','upper first line','gamma_R(s)=pi^(s/2) Gamma(s/2)'),('display','upper second line','gamma_C(s)=1/2 [cancelled coefficient] (2pi)^s Gamma(s)'),('deletion','within upper second line','earlier 1/2 or 2'),('drawing','across upper middle','shallow horizontal divider'),('display','middle left heading','underlined R, n=2p'),('display','middle product','product over p<q gamma_C(s-p)^h(p,q), point and brace'),('display','brace line 1','h_p+ : F=(-1)^p'),('display','brace line 2','h_p- : F=[earlier state]-(-1)^p'),('deletion','brace line 2 overlap','earlier (-1), (1), or opening parenthesis'),('display','brace line 3','leading point; gamma_R(s-p)^h_p+ gamma_R(s-p+1)^h_p-'),('display','bottom left and product','underlined C; product_pq gamma_C(s-inf(p,q))^h(p,q), doubtful punctuation')]:inventory(p,k,pos,t,sheet_kind='text')
p['notation']=[['gamma versus Gamma','Lowercase looped descender with doubled field subscript on left; angular capital Gamma on right of the top definitions.'],['Field letters','Doubled R and C in subscripts and underlined headings; distinct from plain F.'],['Positive exponents','s/2 on pi and s on (2pi), without a preceding minus.'],['Hodge-style indices','h(p,q) has a real comma in both exponent occurrences; product index below the lower Pi has pq without a separately visible comma.'],['Two eigenvalue signs','h_p+ accompanies F=(-1)^p; h_p- accompanies final F=-(-1)^p.'],['Product punctuation','Large multiplication points are distinct from the two very small uncertain points at the bottom.']]
p['hand']=[['Looped gamma and angular Gamma','All seven small gamma signs on this sheet are looped with descenders; the two capital Gamma signs are angular.','No divergence retained between C and H.'],['Compressed paired indices','The lower product index has no independently visible comma; both raised h(p,q) groups have clear descending comma strokes.','H supplied a comma below the product; C marked it doubtful.'],['Overwrite versus extra factor','The lower F relation has a pale earlier state overlaid by a darker complete final sign group. Linear deleted-then-live notation is editorial sequencing of these states, not a claim that both stood side by side.','H omitted the earlier state from the formula.']]
p['abbreviations']=[['inf','infimum']]
p['notes']=['The sheet gives two gamma-factor definitions, then real and complex product expressions. Both powers of pi have positive written exponents. The cancelled symbol after the live 1/2 and the earlier state of the lower F relation remain uncertain. The separator is a drawn rule, and the left labels are underlined field symbols without accompanying prose.', 'For integral p, the written values (-1)^p and -(-1)^p are opposite: at even p they are +1 and -1, and at odd p -1 and +1. This simple parity check is consistent with the + and - labels and helped focus inspection of the overloaded lower sign; the dark external minus is visible independently in the crop. It does not establish the product formula or identify the spaces whose dimensions h might denote.', 'Both h(p,q) exponents retain visible commas; the lower product index is written pq. No dates, page counts, or verbal qualifications of a proof appear. Archive number 1.']
p['checks']=[[ '162-6/002-N02',utc().split(' ')[0],'GPT-6 Astra Pro; effort not exposed; SP62 second pass; /root','used and rechecked in this run','Conditional elementary parity check: for integer p, (-1)^p and -(-1)^p are opposite, with values (+1,-1) for even p and (-1,+1) for odd p. No gamma-factor or dimension formula proved.']]
save(p,tex)
print('Saved',p['filename'],len(p['changes']),'changes;',p['done'])
