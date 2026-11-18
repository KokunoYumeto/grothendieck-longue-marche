import sys
sys.path.insert(0,'MPL_159/scripts')
from record_page import commit
commit(34,r'''\scanpage{34}
où
\[\unsure{\varpi_0|\bar\omega_0}\in\Gamma(\Omega^{-1}\otimes\Omega^1_{X/S})=\operatorname{Hom}(\Omega,\Omega^1_{X/S})\]
est indépendant de $i$, et est le $\unsure{\varpi_0|\bar\omega_0}$ de tout à l'heure pour un splitting. On dit que $C$ est connexion \uline{régulière} si la section $\unsure{\varpi_0|\bar\omega_0}$ de $\Omega^{-1}\otimes\Omega^1_{X/S}$ est \uline{régulière}.

\deleted{(\unsure{terme que nous utiliserons par la suite sans autres})}
\inserted{très régulière si} \deleted{\unsure{l'on a}}
\[\unsure{\varpi_0|\bar\omega_0}:\Omega\xrightarrow{\sim}\Omega^1_{X/S}\quad!\quad)\]
\uline{Prop} \inserted{(car. nulle)} Supposons
\[\mathcal P=\widehat S=\mathcal O_{\widehat P},\quad\text{où }(P,\sigma)\]
associé à une suite ex. de $0\longrightarrow\Omega\longrightarrow E\longrightarrow\mathcal O_X\longrightarrow0$.

Soit \deleted{\unsure{Supposons}} $\operatorname{Conn}(P)\deleted{\unsure{^{*}}}$ l'ens des conn. \deleted{\unsure{régulières}} $c$ de $P$, \deleted{telles que $\hat c$} $\operatorname{Conn}(\widehat S)$ \inserted{l'ens des} conn. de $\widehat S$, d'où $c\longmapsto\hat c$
\[\operatorname{Conn}(P)\longrightarrow\operatorname{Conn}(\widehat S)\]
et soit $\operatorname{Conn}^{*}(\widehat S)\subset\operatorname{Conn}(\widehat S)$ formé des conn. \uline{régulières} \inserted{(\unsure{un peu fort})} de $\widehat S$, $\operatorname{Conn}^{*}(P)$ son image inverse dans $\operatorname{Conn}(P)$. Soit $G$ ($G_0$) le gpe des auto de $\widehat S$ augmenté qui sont l'identité mod $J^3$ ($J^4$).

\inserted{Alors,} L'application
\diagram{\begin{tikzcd}
\operatorname{Conn}^{*}(P)\times G_0\arrow[r] & \operatorname{Conn}^{*}(\widehat S)\\
(c,g)\arrow[r,mapsto] & g.\hat c
\end{tikzcd}}
est bijective (\unsure{unq.|resp.} bijective)
\margin{De plus, \unsure{l'action de $G_0$ dans $\operatorname{Conn}^{*}(\widehat S)$} \deleted{\unsure{de}\ \illegible{2}} \unsure{est libre}.}
\uline{Cor} \inserted{Soit $c\in\operatorname{Conn}^{*}(P)$,}
L'ens $G(c)\subset G$ des $g\in G$ tels que
\[g\hat c\in\operatorname{Im}\operatorname{Conn}^{*}(P)\]
est tel que
\[
G(c)\xrightarrow{\sim}G/G_0\quad\begin{matrix}\simeq\\\Gamma(X,\Omega^{\otimes2})\end{matrix}
\]
% archive foliation: 33
''',[
 ('text','top','où'),('display','top','varpi_0 in Gamma Omega inverse tensor Omega^1 equals Hom'),('text','upper third','est indépendant de i'),
 ('text','upper third','On dit que C est connexion régulière'),('deletion','upper middle parenthesis','terme que nous utiliserons par la suite sans autres'),('insertion','above cancelled parenthesis','très régulière si'),('deletion','above final definition','l on a'),
 ('display','upper middle','varpi_0:Omega isomorphic Omega^1 !'),('text','middle','Prop Supposons'),('insertion','above Prop','car. nulle'),('display','middle','P script=hat S=O_hat P where P sigma'),
 ('text','middle','associé à une suite exacte'),('display','middle inline','0 to Omega to E to O_X to 0'),('text','middle','Soit Conn(P) l ens des conn c'),('deletion','middle start','Supposons'),('deletion','after Conn(P)','star'),('deletion','before c','régulières'),('deletion','after de P','telles que hat c'),('insertion','above Conn(hat S)','l ens des'),
 ('display','middle lower','Conn(P) to Conn(hat S)'),('text','middle lower','et soit Conn star S formé des conn régulières'),('insertion','above de S','un peu fort'),('text','lower third','Soit G (G_0) group automorphisms identity mod J^3 (J^4)'),
 ('insertion','above application','Alors'),('text','lower quarter','L application'),('diagram','lower quarter','Conn star P times G_0 to Conn star S'),('text','lower quarter','est bijective'),('margin note','left lower margin','De plus action of G_0'),('deletion','left lower margin','de and two unreadable words'),
 ('text','bottom','Cor L ens G(c) subset G'),('insertion','above corollary','Soit c in Conn star P'),('display','bottom','g hat c in Im Conn star P'),('text','bottom','est tel que'),('display','bottom right','G(c) isomorphic G/G_0 isomorphic Gamma X Omega tensor 2')
],observations='Final page: regular versus very regular connection terminology is revised; proposition explicitly inserts characteristic zero. Formal conjugation bijection and G(c) quotient corollary. Dense left margin and some parenthetic qualifications are unresolved readings, retained as doubts. No p-curvature expression or cote 93/64 citation was visibly read in the first pass; this is a provisional transcription observation, not a contextual conclusion.')
