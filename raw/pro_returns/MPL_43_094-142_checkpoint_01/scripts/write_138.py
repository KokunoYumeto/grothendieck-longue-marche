from page_work import save_page
text=r'''\scanpage{138}
\margin{$\underline H^i_{\unsure{S|C}/k}(F)$\par $H$}
\diagram{\begin{tikzcd}[column sep=huge,row sep=large]
\underline H^{i-1}_{S/k}(G)\arrow[d,dash]&\underline H^{\overset{\inserted{3-i}}{\overbrace{2-(i-1)}}}_{Y/k}(S,\widehat{\unsure{G|C}})\arrow[d]\\
\underline H^{i-1}_{U/k}(\deleted{\unsure{G}}G)\arrow[d]&\deleted{\operatorname{Ext}}\inserted{\unsure{\underline H}}^{\overset{\inserted{2-i}}{\overbrace{1-(i-1)}}}_{U/k}(\widehat G)\\
\underline H^i_{Y/k}(S,G)\arrow[d]&\deleted{\operatorname{Ext}}\inserted{\unsure{\underline H}}^{2-i}_{S/k}(\widehat G)\arrow[u,leftrightarrow,line width=1.5pt]\\
\underline H^i_{S/k}(G)\arrow[d]&\underline H^{2-i}_{Y/k}(\widehat G)\arrow[u]\\
\underline H^i_{U/k}(G)&\underline H^{1-i}_{U/k}(\widehat G)\arrow[u]
\end{tikzcd}}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw(.15,5.9)--(6.95,6)..controls(7.2,6)and(7.1,5.8)..(7.1,5.4)--(6.8,0)--(0,0)..controls(-.05,1.4)and(.02,4.8)..(.15,5.8);
\draw(.28,6.1)--(.43,6.04)--(.29,5.98);
\end{tikzpicture}}
\deleted{$\underline H^i_{U/k}(G)$}
\deleted{\unsure{isom}}
\[
\rotatebox{90}{$\simeq$}?\qquad
\deleted{\underline H^{i\deleted{\unsure{+1}}}_{S/k}(\unsure{\widehat G|\widetilde G})}
\]
$H$
\mspage{137}
'''
elements=[('margin note','top right','H^i_(S/C)/k(F); H'),('diagram','upper boxed','five paired cohomology terms, downward left arrows, opposed right arrows'),('insertion','above first right exponent','3-i'),('deletion','left second-row argument','G'),('deletion','right rows two and three','Ext overprinted by H'),('insertion','right rows two and three','H'),('insertion','above second right exponent','2-i'),('drawing','around main diagram','slightly curved rectangular frame and short angle at upper left'),('deletion','below box','H^i_U/k(G)'),('deletion','below box left','isom'),('display','below box','vertical equivalence with question mark'),('deletion','below question mark','H^{i...}_S/k(G hat/tilde)'),('deletion','inside canceled exponent','+1'),('display','lower left','H'),('text','bottom left','137')]
save_page(138,text,elements,observations='Whole and both supplied halves read; top-right overwriting and lower canceled relation enlarged. Upper two Ext/H overprints and degree annotations kept. Opposed directions in right column, plain first left connector, and lower question mark preserved. Blue mirrored type is reverse-side show-through.')
