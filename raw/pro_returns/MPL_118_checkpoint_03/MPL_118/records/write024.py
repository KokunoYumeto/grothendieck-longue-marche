from save_page import save
text=r'''\scanpage{24}
\mspage{\unsure{5}}
% archive foliation: 23
\margin{$4$\quad\deleted{$\unsure{4}\ \unsure{4}$}}

\uline{Corollaire} Considérons $\overline{\widehat A}$ la catégorie localisée de
$\widehat A$ pour les homotopismes (relatifs à $h_{\underline W_A}$), de sorte que
$\mathrm{Hot}_A$ apparaît comme une catégorie quotient
\[
\mathrm{Hot}_A\simeq\overline{\underline W}_A^{-1}\,\overline{\widehat A}.
\]
Je dis que $\overline{\underline W}_A$ permet un calcul des fractions à gauche.
\margin{Il faut supposer que $A$ soit catégorie test locale.}
\margin{\uline{idem} dans \deleted{$\mathrm{Hot}$} $\mathrm{Cat}$}

\deleted{\unsure{Cela}} Soit un \unsure{dblt}
\diagram{\begin{tikzcd}
\unsure{Y|X}\arrow[r,"i"]\arrow[d,dash,"{g\in\overline{\underline W}_A}"']&X\\Y'&
\end{tikzcd}}, \inserted{dans $\overline{\widehat A}$}, on veut compléter en
\diagram{\begin{tikzcd}
Y\arrow[r,"i"]\arrow[d,"g"']&X\arrow[d,dash,"f"]\\
Y'\arrow[r,dash,"i'"']&X'
\end{tikzcd}}
comm. avec $f\in\overline{\underline W}_A$.

On va factoriser \deleted{\unsure{le}} $i$ en \deleted{\unsure{mono}}
\diagram{\begin{tikzcd}
Y\arrow[r,dash,"i''"]&X_1\arrow[r,dash,"h"]&X
\end{tikzcd}}, avec $h$ homotopisme
\deleted{\diagram{\begin{tikzcd}Y\arrow[r,hook]&(Y\times I)\end{tikzcd}}}
(cf plus bas), on est ramené au cas où $i$ \deleted{$\unsure{\Longrightarrow}$} mono,
on prend $X'$ somme amalgamée.

D'autre part, on doit montrer que
'''
e=[('text','top','Corollaire Considérons A hat bar'),('margin note','top left','4 and two cancelled numerals'),('deletion','top left','4 4'),('text','upper','la catégorie localisée de A hat'),('display','upper','h sub W A relative homotopisms'),('display','middle','Hot A is W A bar inverse A hat bar'),('text','middle','Je dis que W A bar permet un calcul des fractions à gauche'),('margin note','upper left diagonal','Il faut supposer que A soit catégorie test locale'),('margin note','left diagonal','idem dans Cat'),('deletion','left diagonal','Hot'),('deletion','lower middle left','Cela'),('text','lower middle','Soit un dblt'),('diagram','lower middle','Y to i X down g in W bar A Y prime'),('insertion','lower middle right','dans A hat bar'),('text','lower middle','on veut compléter en'),('diagram','lower','Y to i X; g f; Y prime to i prime X prime'),('text','lower right','comm. avec f in W A bar'),('text','bottom','On va factoriser i'),('deletion','bottom','le'),('deletion','bottom','mono'),('diagram','bottom','Y i double prime X1 h X'),('text','bottom','avec h homotopisme cf plus bas'),('deletion','bottom diagram','Y hook Y times I'),('diagram','bottom cancelled','Y hook Y times I'),('deletion','bottom','double arrow after i'),('text','bottom','on est ramené au cas où i mono'),('text','bottom last','D autre part on doit montrer que')]
save(24,text,'text',e,'Calculus of left fractions in homotopy quotient of presheaves, local test category hypothesis added in margin, idem in Cat with Hot deleted. Factorization into a monomorphism and homotopism, cf plus bas. Heavily retraced page/draft numbering and span abbreviation remain doubtful. Continues next scan.')
