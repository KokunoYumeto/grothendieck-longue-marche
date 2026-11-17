import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
s=r'''\scanpage{29}
\uuline{Lemme} Notations $\unsure{\mathbb T|T},F,n,\mathcal M$ comme dans le
lemme de Cartan.\inserted{Considérons les} Conditions \deleted{équivalentes}

(i) $\forall S\in\mathcal M$,
\figure{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=5pt] (n) {$\deleted{\unsure{H}}\varinjlim_{\mathcal U}H^i(\mathcal U,F)$};\end{tikzpicture}}
$\simeq H^i(S,F).\qquad i\leq n$

[$\mathcal U$ parcourt les rec. de $S$ formés de $S_i\in\mathcal M$,]

(ii) $\forall S\in\mathcal M$, \deleted{et tt rec. $\mathcal U$ de $S$ formé
d'objets de $\unsure{S|\mathcal M}$, et tt élément:}
\[
\varinjlim_{\mathcal U}H^p(\mathcal U;H^q(F))=0\quad\text{pour }
\deleted{\unsure{0<q\leq n|0<p+q\leq n}\text{ et }q\ne0}\inserted{0<q\leq n\unsure{+1}}
\]

(iii)
\[
\varinjlim_{\mathcal U}H^p(\mathcal U,\overline H^q(F))=0\quad\text{pour }0<q\leq n\unsure{+1}
\quad\deleted{\text{et }\unsure{p|q}=0}
\]
où on pose\inserted{pour $T\in\mathcal M$,}
\[
\overline H^q(F)(T)=\varinjlim_{\mathcal V}H^q(\mathcal V,T),
\]
$\mathcal V$ parcourant les rec. de $T$ formés d'objets de $\mathcal M$.

(ii bis) $\forall S\in\mathcal M$, $\mathcal U$ rec. de $S$ par des $U_i\in\mathcal M$,
et $\unsure{\gamma|\zeta}\in\unsure{C^p|Z^p}(\mathcal U,H^q(F))$,
\deleted{($\unsure{p\geq0},p+q\leq n-1,\ q\ne0$)}\inserted{$0<q\leq n$}
il existe $\mathcal U'$ rec. de $S$ par des $U_i\in\mathcal M$, majorant $\mathcal U$,
\deleted{\unsure{tel que le}} et $\mathcal U'\unsure{-|\longrightarrow}\mathcal U$, tel que l'image de
$\unsure{\gamma|\zeta}$ dans $C^p(\mathcal U',H^q(F))$ soit nulle.

(iii bis) \deleted{$\unsure{\Leftarrow|\Leftrightarrow}$} Comme (ii bis), mais $H^qF$,
remplacé par $\overline H^q(F)$.

Mais on a
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\deleted{\text{(ii bis)}}\arrow[r,Rightarrow]\arrow[d,Rightarrow]&\deleted{\text{(ii)}}\arrow[d,Rightarrow]\\
{}\arrow[r,dash]&{}
\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
\text{(ii bis)}\arrow[r,Leftrightarrow]\arrow[d,Rightarrow]&\text{(iii bis)}\\
\text{(ii \deleted{\unsure{bis}})}\arrow[r,Leftrightarrow]\arrow[d,Rightarrow]&\text{(iii)}\\
\text{(i)}&
\end{tikzcd}}
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,4.8)--(.02,4.1);
\draw[thin] (.15,3.7)..controls(-.3,3.6)and(-.2,3.5)..(-.16,3.1)--(-.04,2.2)..controls(.1,2.2)and(.3,2.25)..(.48,2.3);
\draw[thin] (.1,1.8)..controls(-.1,1.8)and(-.08,1.7)..(-.1,1.5)--(-.1,.1)..controls(-.08,0)and(.06,0)..(.2,0);
\end{tikzpicture}}}
\margin{28}
'''
e=[('text','top heading','Lemme Notations T F n M'),('text','top continuation','comme dans le lemme de Cartan'),('insertion','above Conditions','Considérons les'),('deletion','top after Conditions','équivalentes'),('text','condition i','∀S∈M'),('display','condition i','lim_U H^i(U,F) ≃ H^i(S,F) i≤n'),('deletion','condition i before lim','H'),('drawing','condition i','pencil ellipse around limit term'),('text','bracket under i','U parcourt les rec. de S'),('text','condition ii','∀S∈M'),('deletion','condition ii two lines','et tt rec. U de S formé d’objets'),('display','condition ii','lim_U H^p(U;H^q(F))=0'),('deletion','condition ii right','0<q≤n et q≠0'),('insertion','condition ii right above','0<q≤n+1'),('display','condition iii','lim_U H^p(U,bar H^q(F))=0'),('deletion','condition iii right below','et p=0'),('text','definition introduction','où on pose'),('insertion','definition above','pour T∈M'),('display','definition','bar H^q(F)(T)=lim_V H^q(V,T)'),('text','definition continuation','V parcourant les rec. de T'),('text','condition ii bis','∀S∈M U rec. de S par des Ui∈M'),('display','condition ii bis','γ∈C^p(U,H^q(F))'),('deletion','condition ii bis right','p≥0 p+q≤n−1 q≠0'),('insertion','condition ii bis right above','0<q≤n'),('text','condition ii bis','il existe U′ rec. de S'),('deletion','condition ii bis lower','tel que le'),('display','condition ii bis lower','U′—U'),('text','condition ii bis end','tel que l’image de γ dans C^p soit nulle'),('text','condition iii bis','Comme (ii bis) mais H^qF remplacé'),('deletion','after iii bis label','left double arrow'),('text','bottom','Mais on a'),('diagram','bottom middle','cancelled (ii bis)⇒(ii), lower connecting strokes'),('diagram','bottom right','(ii bis)⇔(iii bis), (ii)⇔(iii), (i)'),('deletion','bottom right diagram second row','bis'),('drawing','left margin','vertical emphasis strokes and brackets'),('margin note','bottom left','28')]
save(29,s,e,observations='Whole, both halves and six enlarged regions inspected. The upper right bounds were revised repeatedly and remain marked where the terminal +1 is cramped. H^q(V,T) has a clearly T-shaped second argument and is retained as written. The element letter and overwritten C/Z remain uncertain. Bars over H are short horizontal strokes rather than Čech checks. The two bottom implication sketches are both transcribed; no equivalence is supplied outside their actual arrows. Marginal brackets and the pencilled ellipse are reproduced.')
