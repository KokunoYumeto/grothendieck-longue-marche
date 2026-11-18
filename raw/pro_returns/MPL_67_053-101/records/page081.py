import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{81}
% archive foliation: 83
\[
\left\{\begin{gathered}
\text{paires de pantalons }\deleted{\text{\unsure{dég.}}}\inserted{\text{\unsure{généralisés}}}\inserted{X',X''},\ \inserted{\text{\unsure{à trous}}}\ \text{indexés}\\
\text{par }\varepsilon'\amalg\{s\},\quad\varepsilon''\amalg\{t\},\quad\text{avec }s,t\ \text{correspondant}\\
\text{aux }\deleted{\text{bords}}\ \text{composantes ponctuelles du}\\
\text{bord, avec les paramètres }(\lambda_i)_{i\in\varepsilon'\amalg\varepsilon''}\in\unsure{(\mathbb R^{*+})^{\varepsilon'\amalg\varepsilon''}}\\
\text{et un isom d'identification}\\
\text{des }\mathbb C^*\wedge_{\pm1}(\varepsilon'\wedge\varepsilon'')
\end{gathered}\right.
\]
Une fois ce cas compris, et revenant
alors au cas général, il faudrait déjà,
pour un type de découpage donné
incarné par un diagramme MD
dans $md_{g,\nu}$, comprendre l'application
sur les groupes fondamentaux
induite par
\diagram{\begin{tikzcd}
\unsure{\varphi})\quad MD\deleted{B}_{\unsure{g}} \arrow[r] & M_{\mathrm{st}}N\deleted{\unsure{D}}_{g,\nu},
\end{tikzcd}}
ceux du deuxième membre étant
essentiellement compris, en termes de
groupes de Teichmüller spéciaux
--- \uline{mais il doit en être pareil pour le
premier} ! Également, il ne devrait
pas être bien dur de vérifier si $\unsure{\varphi}$
"""
save(81,tex,[('display','top brace','paires de pantalons; paramètres; isom'),('deletion','top after pantalons','dég.'),('insertion','above deleted dég.','généralisés'),('insertion','upper right','X prime, X double-prime'),('insertion','upper right','à trous'),('deletion','third line brace','bords'),('text','middle','Une fois ce cas compris'),('diagram','lower middle','phi MD to M st N'),('deletion','source of lower diagram','B'),('deletion','target of lower diagram','D'),('text','bottom','ceux du deuxième membre étant')],doubts=[('first brace line','généralisés','Correction overlaps preceding dég.','low'),('first brace line upper right','à trous','Heavily retraced; cancellation status uncertain.','low'),('right edge of parameters','(R*+) to epsilon prime disjoint epsilon double-prime','Some strokes reach right edge; grouping parentheses supplied only where tentatively read.','low'),('morphism symbol','varphi','Phi-like circle crossed by a slanting stroke.','medium'),('diagram source subscript','g','Heavily crossed with B; nu not clearly present.','low')],notations=[('label of surgery map',r'\varphi','Phi-like symbol; kept unsure where retraced.'),('torsor contract',r'\mathbb C^*\wedge_{\pm1}(\varepsilon'+'\u0027'+r'\wedge\varepsilon'+'\u0027\u0027'+')','Contracted product with a two-element torsor.')],leads=['Understanding induced fundamental-group map is posed as the next task; target groups described as special Teichmüller groups, source expected analogous.','Degenerate/generalised pants with puncture components, positive parameters and C* torsor identification are the proposed target of pants gluing.'])
