import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{82}
% archive foliation: 81
Inversement, soit $P_1$ (\deleted{$\unsure{\otimes}$} catégorie $\otimes$ additive) \inserted{\unsure{avec} $\otimes$ \unsure{ass.}, avec \uline{\unsure{unité}}}, munie d'un foncteur de $(P_1,+)$ dans $(P_1^{\mathrm{grad.}}_{\unsure{+}},\otimes)$, \deleted{\unsure{donc additif}}
\[\Gamma^*:(P_1,\oplus)\longrightarrow(P_1^{\mathrm{grad}},\otimes)\]
\unsure{donc}
\[\Gamma^*(0)=1\quad\text{i.e.}\quad\Gamma^{\unsure{i|\nu}}(0)=\begin{cases}1&\text{si }\nu=0\\0&\text{si }\nu>0\end{cases}\]
\inserted{\unsure{aux degr. }$0,1$}
\[\Gamma^*(X\oplus Y)\simeq\Gamma^*(X)\otimes\Gamma^*(Y)\]
(isom \unsure{gradué}, bifonctoriel en $X,Y$, compatible aux contraintes d'unité, d'ass., de comm.)
avec
\[\Gamma^i(M)=\begin{cases}0&\text{si }i<0\\1&\text{si }i=0\\M&\text{si }i=1\end{cases}\]
(isom de foncteurs en $M$). Supposons de plus donné des hom de foncteurs
\[\Gamma^{pq}\xrightarrow{\alpha_{pq}}\Gamma^p\circ\Gamma^q\]
\[(\text{i.e.}\qquad\Gamma^{pq}(X)\xrightarrow{\alpha^X_{pq}}\Gamma^p(\Gamma^q(X))\qquad)\]
satisfaisant la condition d'associativité ci-dessus, plus les conditions d'unité pour \deleted{$p,q$} l'un des deux $p,q$ égaux à $0$ ou $1$ :
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\text{(\unsure{u_1})}&\Gamma^q\arrow[r,"\alpha_{1,q}=\mathrm{id}"]\arrow[rd,bend right=20,"\alpha_{q,1}=\mathrm{id}"']&\Gamma^1\circ\Gamma^q=\mathrm{id}\circ\Gamma^q=\Gamma^q\\
&&\Gamma^q\circ\Gamma^1=\Gamma^q\circ\mathrm{id}=\Gamma^q
\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\text{(\unsure{u_0})}&\Gamma^0\arrow[r,"\alpha_{0,q}=\mathrm{id}"]\arrow[rd,bend right=20,"{\alpha_{q,0}\text{ un }\uline{\text{iso}}}"']&\Gamma^0\circ\Gamma^q=\Gamma^0\\
&&\Gamma^q\circ\Gamma^0.
\end{tikzcd}}
'''
e=[('text','top','Inversement soit P1'),('deletion','above catégorie','tensor'),('insertion','upper','avec tensor ass., avec unité'),('deletion','upper','donc additif'),('display','upper','Gamma*: (P1,oplus) -> (P1^grad,tensor)'),('text','upper','donc'),('display','upper-middle','Gamma*(0)=1 i.e. Gamma^nu(0)'),('insertion','above middle display','aux degr. 0,1'),('display','middle','Gamma*(X oplus Y) iso Gamma*(X) tensor Gamma*(Y)'),('text','middle','isom gradué bifonctoriel'),('text','middle','avec'),('display','middle','Gamma^i(M) cases'),('text','middle-lower','isom de foncteurs en M'),('display','lower','Gamma^pq -> Gamma^p circle Gamma^q'),('display','lower','i.e. Gamma^pq(X) -> Gamma^p(Gamma^q(X))'),('text','lower','satisfaisant la condition'),('deletion','lower','p,q'),('diagram','bottom','u1: Gamma^q two arrows'),('diagram','bottom','u0: Gamma^0 two arrows')]
save(82,text,e)
