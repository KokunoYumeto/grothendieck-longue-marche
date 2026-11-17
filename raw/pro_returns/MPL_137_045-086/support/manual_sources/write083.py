import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{83}
% archive foliation: 82
Les $\alpha_{p,q}$ permettent de définir des \deleted{\unsure{lois}}
\margin{\unsure{9}}
\[P_n(X,Y)=\operatorname{Hom}_{P_1}(\Gamma^nX,Y)\]
\inserted{donc $\left\{\begin{array}{l}P_1(X,Y)=\operatorname{Hom}_{P_1}(X,Y)\\P_0(X,Y)=\operatorname{Hom}_{P_1}(1,Y)\end{array}\right.$}
et des applications
\[\begin{aligned}P_p(X,Y)\times P_q(Y,Z)&\longrightarrow P_{pq}(X,Z)\\f\quad,\quad g&\longmapsto g\circ f\end{aligned}\]
par
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\Gamma^pX\arrow[r,"f"]&Y&\Gamma^qY\arrow[r,"g"]&Z\\
\Gamma^q(\Gamma^pX)\arrow[urr,"\Gamma^q(f)"]&\deleted{\unsure{\alpha}\longleftarrow\unsure{\Gamma^p(\Gamma^q(X))}\longleftarrow\Gamma}&&\\
\Gamma^{pq}(X)\arrow[u,"\alpha^X_{q,p}"]&&g\circ f=g\Gamma^q(f)\alpha^X_{q,p}&
\end{tikzcd}}
Le diagramme comm. (A) assure l'associativité de la composition, $(\unsure{u_1})$ \unsure{est une exigence} que si \inserted{$p=1$ ou $q=1$} \deleted{\unsure{$g$ ou $f$ est}} \deleted{de degré $1$}, alors le composé est celui provenant de la bifonctorialité des $P_p(X,Y)$ sur $P_1^\circ\times P_1$, enfin la compatibilité $(\unsure{u_0})$ signifie, pour le \unsure{premier}, que
\[g\circ f=g\qquad\text{si }g\text{ de degré }0\]
le deuxième signifie
\diagram{\begin{tikzcd}[column sep=large,execute at end picture={\draw[rotate=7] (current bounding box.center) ellipse (2.5cm and .9cm);}]
\deleted{\unsure{\Gamma^0}}&\\[-1.5ex]
1\arrow[r,"\alpha_{q,0}"]&\Gamma^q(1)
\end{tikzcd}}
\margin{\unsure{pourtant}}
\figure{\begin{tikzpicture}\draw (0,0)--(.1,1.6);\draw (.08,0)--(.16,1.6);\end{tikzpicture}}
Je l'avais oublié dans les axiomes préliminaires il me semble, \unsure{que}\newline
\unsure{je n'} \unsure{d'avais des} \unsure{vrais} \illegible{1}
'''
e=[('text','top','Les alpha_p,q permettent'),('deletion','top','lois'),('margin note','upper right','9'),('display','upper','P_n(X,Y)=Hom_P1(Gamma^nX,Y)'),('insertion','upper below formula','donc P1(X,Y) ... P0(X,Y)'),('text','upper','et des applications'),('display','upper','Pp(X,Y) times Pq(Y,Z) -> Ppq(X,Z)'),('text','middle','par'),('diagram','middle','Gamma^pX -> Y; Gamma^qY -> Z; Gamma^pqX -> Gamma^q(Gamma^pX)'),('deletion','middle within diagram','cancelled horizontal Gamma expression and arrows'),('text','lower','Le diagramme comm. A assure'),('insertion','lower above line','p=1 ou q=1'),('deletion','lower','g ou f est'),('deletion','lower','de degré 1'),('display','lower','g circle f = g si g de degré 0'),('text','lower','le deuxième signifie'),('diagram','bottom circled','1 -> Gamma^q(1)'),('deletion','above 1 in circled diagram','Gamma^0'),('margin note','bottom left','pourtant'),('drawing','bottom left','two vertical slanted lines'),('text','bottom','Je l’avais oublié'),('text','bottom edge dark ink','je n’ ... d’avais des vrais ...')]
save(83,text,e)
