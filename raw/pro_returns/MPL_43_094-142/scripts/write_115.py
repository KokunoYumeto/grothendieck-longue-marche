from page_work import save_page
text=r'''\scanpage{115}
\mspage{114}
\mspage{III-49}
me de dévissage (II,1,5,cor. du th.3), on est ramené à prouver que
lorsque $X$ est irréductible, il existe \uuline{un} $\underline O_X$-Module cohérent de support
$X$ appartenant à \uuline{$K'$}: en effet, si ce point est établi, on
pourra l'appliquer à toute partie fermée irréductible $Y$ de $X$, car
si $\underline G$ est un $\underline O_Y$-Module cohérent et $j$ l'injection canonique $Y\to X$, on
a $R^q(f\circ j)_*(\underline G)=R^qf_*(j_*(\underline G))$ (G,II,4.9.1), et le corollaire du lemme
de dévissage s'applique.

En vertu du lemme de Chow (II,5,2,cor.1 du th.1), il existe un
préschéma irréductible $X'$ et un morphisme \inserted{\uline{projectif}} surjectif \inserted{\uline{et}} birationnel $g:$
$X'\to X$ tels que $f\circ g:X'\to Y$ soit \uline{projectif}. Comme $X$ est noethérien
\deleted{\unsure{et $g$ fermé}, on en déduit (II,4,6,th.3 (ii)) que $g$ est aussi un morphisme projectif; comme $X$ est noethérien},
$X'$ est isomorphe à un
préschéma $\operatorname{Proj}(\underline S)$, où $\underline S$ est une $\underline O_X$-Algèbre \deleted{\unsure{$g$}} quasi-cohérente
graduée à degrés positifs, engendrée par $\underline S_1$, où $\underline S_1$ est un $\underline O_X$-Module
cohérent (II,4,6,prop.21 (ii)). Le th.1 du \S\ 2,n\textsuperscript{o}2 est applicable
à $g:X'\to X$, et il existe donc un entier $n>0$ tel que \deleted{$\unsure{R^qg_*}$}
$\underline F=g_*(\underline O_{X'}(n))$ soit cohérent et $R^qg_*(\underline O_{X'}(n))=0$ pour tout $q>0$; en outre,
comme $g$ est birationnel, le support de $\underline F$ contient un ouvert
partout dense de $X$, et comme ce support est fermé\inserted{(FAG,I,2,12,prop.1)}, il est identique
à $X$. D'autre part, comme $f\circ g$ est projectif et $Y$ noethérien,
le \uline{même raisonnement} (II,4,6,prop.21 (ii) et \S\ 2,n\textsuperscript{o}2,th.1) montre
que les $R^p(f\circ g)_*(\underline O_{X'}(n))$ sont cohérents. Cela étant, \deleted{$\unsure{R^pf_*}$}
$R^*(f\circ g)_*(\underline O_{X'}(n))$ est l'aboutissement d'une suite spectrale dont le
terme $E_2$ est donné par $E_2^{pq}=R^pf_*(R^qg_*(\underline O_{X'}(n)))$ (suite spectrale de
Leray; \S\ 0,n\textsuperscript{o}\quad). D'après ce qui précède, on a $E_2^{pq}=0$ pour $q>0$;
on sait alors que \deleted{\unsure{le}} $E_2^{p0}=R^pf_*(\underline F)$ est isomorphe à $R^p(f\circ g)_*(\underline O_{X'}(n))$
(G,I,4.4.1), ce qui achève la démonstration.
\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.15,.15);\draw (.08,.1)--(.22,-.04);\end{tikzpicture}}}

\uline{Corollaire 1 .- Soit} $Y$ \uline{un préschéma localement noethérien. Pour tout}
\uline{morphisme propre} $f:X\to Y$ \deleted{\unsure{noethérien}}, \uline{l'image directe par $f$ de}
'''
save_page(115,text,[('text','archive folio original bottom','114'),('text','typed heading after rotation','III-49'),('text','reading upper continuation','me de dévissage (II,1,5,cor. du th.3)'),('display','within upper paragraph','R q(f circle j)star(G)=R q fstar(jstar(G))'),('text','reading middle paragraph','En vertu du lemme de Chow'),('insertion','above surjectif','projectif'),('insertion','above birationnel','et'),('deletion','middle two crossed lines','et g fermé on en déduit ... comme X est noethérien'),('deletion','before quasi-cohérente','g'),('deletion','after tel que','R q gstar'),('display','within middle paragraph','F=gstar(O Xprime(n)); R q gstar(...)=0'),('insertion','support est fermé','FAG,I,2,12,prop.1'),('text','reading lower continuation','D’autre part comme f circle g est projectif'),('deletion','after Cela étant','R p fstar'),('display','spectral sequence definition','E2 pq=R p fstar(R q gstar(OXprime(n)))'),('deletion','after on sait alors que','le'),('display','spectral degeneration','E2 p0=R p fstar(F) isomorphe à R p(f circle g)star'),('drawing','left next to même raisonnement','small crossed check stroke'),('text','bottom corollary opening','Corollaire1 Soit Y un préschéma localement noethérien'),('deletion','bottom after X→Y','noethérien')],sheet_kind='reused_typed',observations='Original whole viewed, then upright rotated whole and both supplied halves, with enlarged cancellations. All yellow single underlines on O, S, G and F are represented as underlines on the printed letters, not silently converted to a different alphabet. Black and red emphasis under K prime is double-underlined. The blank section-number reference after section0 no is preserved. Several completely overstruck formula attempts remain best readings with doubt marks. The page begins and ends mid-sentence.')
