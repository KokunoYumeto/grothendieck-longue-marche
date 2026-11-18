from save_page import save
save(19,r'''\scanpage{19}
\mspage{1}

\diagram{\begin{tikzcd}
Y\arrow[r,hook,"i"]\arrow[d,"g"']&X\arrow[d,"f"]&U\arrow[l,hook]\arrow[d,"\wr"]\\
Y'\arrow[r,hook,"i'"']&X'&U'\arrow[l,hook]
\end{tikzcd}}

Soient $X'$ dans $(\mathrm{Cat})$

$Y'$ sous-objet fermé, $U'$ compl. ouvert

\margin{\unsure{Même}}

\[
f:X\longrightarrow X',\quad Y=f^{-1}(Y'),\qquad U=f^{-1}(U')
\]

Supposons que $U\xrightarrow{\sim}U'$

alors \deleted{$f$}\inserted{le carré} est-il néc. cocartésien ? Non bien sûr, comme on voit en prenant $\unsure{X'=U'|X=U}$, $f$ l'inclusion, alors $Y=\varnothing$.

\uline{Mais} supposons que $f$ soit cofibré, le carré est-il cocartésien ? En d'autres termes, a-t-on pour $u'\in U'$, $y'\in Y'$
\[
\mathrm{Hom}_{X'}(u',y')\xleftarrow[\sim]{?}
\underbrace{\underset{y\;\mathrm{ds}\;Y_{/y'}}{\varinjlim}\mathrm{Hom}(u,y)}_{\underset{Y_{y'}}{\varinjlim}\mathrm{Hom}(u,Y_{y'})}\;?
\]
\margin{(où $u\in\mathrm{Ob}\,U$ au dessus de $u'$) ?}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
u&\deleted{\unsure{y}}\arrow[d,dashed,dash]&y\arrow[d,dashed]\\
u'\arrow[r,dashed,dash]&\deleted{\unsure{f(y)}}\arrow[r]&y'
\end{tikzcd}}

Oui, car \deleted{$\mathrm{Hom}(u,$}

(i) Surjectif et

(ii) Pour $\unsure{\xi|f}:u\longrightarrow y'$ fixé \ldots

Nous nous intéressons donc à la situation des diagrammes du type précédent, avec $f$ \uline{cocartésien} / Peut se décrire par un foncteur
\[
X'\longrightarrow(\mathrm{Cat}),
\]
\deleted{dans} dont la restriction à $U'$ soit le foncteur $c^t$ de valeur $\Delta_0=e_{(\mathrm{Cat})}$,

i.e.

(i) $Y'\xrightarrow{\Phi}\mathrm{Cat}$ (définissant \deleted{$\unsure{f}$} $Y\longrightarrow Y'$)

(ii) $\mathrm{Hom}(u',y')\longrightarrow\mathrm{Ob}\,\Phi(y')$ bifonctoriel en $u',y'$ ds $U'\times Y'$
% archive foliation: 18
''','text',[
('text','top author number','1 circled'),('diagram','upper left','Y hook X left hook U; g f iso; Y prime X prime U prime'),('text','upper right','Soient X prime dans Cat; Y prime sous-objet fermé U prime compl. ouvert'),('margin note','top right pencil','Même'),('display','upper right','f:X→X prime; Y=f inverse Y prime; U=f inverse U prime'),('text','upper middle','Supposons que U isom U prime; est-il néc. cocartésien'),('deletion','upper question subject','f'),('insertion','above question subject','le carré'),('text','middle first answer','Non bien sûr comme on voit en prenant X prime=U prime'),('text','middle second question','Mais supposons que f soit cofibré; a-t-on'),('display','middle','Hom_X prime(u prime,y prime) ← colimit Hom(u,y); comparison question'),('margin note','right of display','où u in Ob U au dessus de u prime; ?'),('diagram','middle left','u; y; y; u prime dotted f(y)→y prime'),('deletion','middle sketch','y; f(y)'),('text','middle answer outline','Oui car; (i) Surjectif et (ii) Pour xi:u→y prime fixé'),('deletion','middle answer outline','Hom(u,'),('text','lower paragraph','Nous nous intéressons donc à la situation des diagrammes'),('display','lower paragraph','X prime→Cat'),('deletion','lower paragraph','dans'),('text','lower paragraph continuation','dont la restriction à U prime soit le foncteur c^t de valeur Delta0'),('display','bottom i','Y prime Phi→Cat définissant Y→Y prime'),('deletion','bottom i','f'),('display','bottom ii','Hom(u prime,y prime)→Ob Phi(y prime) bifonctoriel')],
'First clearly circled author page number in this sequence: 1. The initial counterexample line has an ambiguous prime placement (X prime=U prime versus X=U); no mathematical correction applied. The cofibration pushout question is followed by “Oui” and a two-part outline ending in ellipsis, not a completed injectivity proof. The colimit comparison has an explicit question mark. A faint pencil “Même” in the upper right is recorded as a marginal reading.')
