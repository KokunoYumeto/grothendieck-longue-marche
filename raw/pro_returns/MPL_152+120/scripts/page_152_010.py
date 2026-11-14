from record_page import save_page
save_page(152,10,r'''
\mspage{2'}
Ces deux données \deleted{\unsure{par}} sur le contour $C$ permettent de récupérer un graphe circularisé $\Gamma$, ayant $\vec A$ comme ens des arêtes orientées, avec opérations $\sigma_A$, $\rho_S$ données ainsi :
\[
\left\{\begin{aligned}
\sigma_\Gamma&=\sigma_C\\
\rho_\Gamma&=\rho_C
\end{aligned}\right.
\]

\uline{En résumé} La catégorie des graphes combinatoires circularisés $\Gamma$ (sans sommet isolé) \inserted{$(\vec A\deleted{\unsure{_\Gamma}}(\Gamma),\rho_\Gamma,\sigma_\Gamma)$} est équivalente à celle des contours orientés, avec involution \inserted{sans pt fixe $\sigma_C$} sur l'ens des \uline{arêtes}, soit $C$ ($=A(C)$ ens des arêtes de $C$, $\rho_C$ rotation fondamentale de $C$, $\sigma_C$ involution sur $A(C)$). \deleted{\unsure{par la}} \deleted{\unsure{p}} correspondance fondamentale :
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\vec A(\Gamma)&A(C)\arrow[l,"\sim"']\\
\sigma_\Gamma\arrow[r,leftrightarrow]&\unsure{\sigma_C|\rho_C}\\
\rho_\Gamma^{\unsure{\sigma|-1}}\sigma_\Gamma&\rho_C\arrow[l,maps to]\\
\rho_\Gamma&\rho_C\sigma_C\arrow[l,maps to]
\end{tikzcd}}
\margin{On appellera cela \uline{déploiement} \unsure{du} graphe plan donné}
\margin{$\rho_\Gamma^{\unsure{\sigma}}$ rotation renversée pour \unsure{la circ\({}^{\mathrm{on}}\) actuelle définie|le contour actuel défini} par $\Gamma$}

\begin{center}\fbox{\begin{minipage}{.92\linewidth}
$\Gamma$ un arbre $\Longleftrightarrow$ $C$ est un polygone comb. (non ponctuel), et l'involution $\sigma_C$ de $A(C)$ est totalement non pénétrante, i.e. pour deux \deleted{\unsure{paires}} \inserted{orbites} disjointes d'arêtes sous $\sigma_C$, \unsure{leur position|la partition} est n.p.
\end{minipage}}\end{center}
\mspage{\unsure{9|09}}
''',[
('text','top centre page number',"2 prime"),('text','top','Ces deux données sur le contour C'),('deletion','top first line','par'),('display','upper brace','sigma_Gamma=sigma_C; rho_Gamma=rho_C'),('text','middle','En résumé La catégorie des graphes combinatoires circularisés'),('insertion','middle after sommet isolé','(vec A(Gamma),rho_Gamma,sigma_Gamma)'),('deletion','in inserted tuple','subscript Gamma'),('insertion','middle above involution','sans pt fixe sigma_C'),('deletion','after involution sur A(C)','par la'),('deletion','before correspondance','p'),('text','below middle paragraph','correspondance fondamentale'),('diagram','lower-middle table','vec A(Gamma), A(C), sigma_Gamma, sigma_C, rho_Gamma^sigma sigma_Gamma, rho_C, rho_Gamma, rho_C sigma_C'),('margin note','left oblique beside table','On appellera cela déploiement du graphe plan donné'),('margin note','left below oblique note','rho_Gamma^sigma rotation renversée'),('text','bottom boxed','Gamma un arbre iff C est un polygone comb.'),('deletion','box last two lines','paires'),('insertion','box above deleted word','orbites'),('text','bottom left page number','9 or 09')
],observations='The paragraph gives sigma_Gamma=sigma_C and rho_Gamma=rho_C, whereas the later correspondence table has products and a small exponent read tentatively as sigma. Retain the formulas independently as ink; the margin calls the construction déploiement and the small exponent appears again beside rotation renversée. The box gives a non-penetration criterion for a tree; the final words before est n.p. and the overwritten table symbol remain uncertain.')
