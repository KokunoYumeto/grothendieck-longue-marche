from record_page import record
tex=r'''\scanpage{23}
% archive foliation: 22
\uline{En résumé} Dans la \uline{catégorie}
\uline{abélienne} \inserted{$k$-lin. $C$} de tous les $k$-modules
$\frac12$ simpliciaux, ceux qui sont \inserted{str. $\partial$-} parfaits
forment une sous-catégorie \uline{additive}
$C_0$ \unsure{en question|engendrée}, dans laquelle
on a un complexe de \unsure{cochaînes}
\diagram{\begin{tikzcd}
0\arrow[r,dash]&\Phi_*^{(0)}\arrow[r,dash]&\Phi_*^{(1)}\arrow[r,dash]&
\Phi_*^{(2)}\arrow[r,dash]&\cdots\arrow[r,dash]&
\Phi_*^{(i)}\arrow[r,"\lambda_i"]&\Phi_*^{(i+1)}
\end{tikzcd}}
satisfaisant à ceci

a) Complexe str. acyclique dans $C$, \deleted{\unsure{$\forall i\geq0$}}

b) Pour tout $i,j\geq0$, on a
\[
\operatorname{Hom}(\Phi_*^{(i)},\Phi_*^{(j)})\simeq
\left\{\begin{array}{ll}
0&\text{si }j\neq i,i+1\\
k\ (\text{engendré par id})&\text{si }j=i\\
k\ (\unsure{\text{engendré par }}\lambda_i)&\text{si }j=i+1
\end{array}\right.
\]

\deleted{\unsure{c)}} Posant
\[
\Psi_*^{(i)}=Z^{\unsure{i+1}}(\Phi_*^*)
=\operatorname{Ker}_C(\Phi^{i+1}\xrightarrow{\lambda_{\unsure{i+1}}}\Phi^{i+2})
\]
\inserted{$=\operatorname{Coker}_C(\Phi^{i-1}\xrightarrow{\lambda_{i-1}}\Phi^i)$}
\margin{\unsure{conséq. de a) b)}}
on a donc \deleted{\unsure{$\operatorname{Hom}(\Psi_i$}}
\[
\Psi^0\simeq\Phi^0
\]
\diagram{\begin{tikzcd}[column sep=large]
(*)\quad0\arrow[r,dash]&\Psi^{i-1}\arrow[r,hook,"\iota_i"]&
\Phi^i\arrow[r,two heads,"u_i"]\arrow[dr,"\lambda_i"']&
\Psi^i\arrow[r]\arrow[d,hook]&0\quad\text{ext. can.}\\
&\Phi^{i-1}\arrow[u,two heads,"u_{i-1}"]\arrow[ur,"\lambda_{i-1}"']&&\Phi^{i+1}&
\end{tikzcd}}
\[
\operatorname{Hom}(\Psi^i,\Psi^j)
\subset\operatorname{Hom}(\Phi^i,\Phi^{j+1})=
\left\{\begin{array}{ll}
0&\text{si }j\neq i\deleted{\unsure{,i+1}}\\
k&\text{si }j=i\ (\text{par id})
\end{array}\right.
\]
\[
\operatorname{Hom}(\Phi^i,\Psi^j)\deleted{\unsure{\simeq}}
\subset\operatorname{Hom}(\Phi^i,\Phi^{j+1})\simeq
\left\{\begin{array}{ll}0&\text{si }j\neq i\\
k&\text{si }j=i\ (\text{par }u_i)
\end{array}\right.
\]
\[
\operatorname{Hom}(\Psi^i,\Phi^j)
\subset\operatorname{Hom}(\Phi^i,\Phi^j)\simeq
\left\{\begin{array}{ll}
0&\text{si }j\neq i+1\ (i\neq0)\\
k&\text{si }j=i+1\ (\text{par }\iota_i)\\
k&\text{si }j=i=0\ (\text{par id})
\end{array}\right.
\]
\margin{\unsure{via composée} $\Phi^i\longrightarrow\Psi^i\longrightarrow
\Phi^{j+1}$ \illegible{3}}

d) Soit, \deleted{\unsure{$\Phi(i)$}} pour $n\in k-0$
\inserted{et $i\geq1$}, $\Phi(i,n)$
l'ext. de \deleted{\unsure{$\Phi^i$}} $\Psi^i$ par $\Psi^{i-1}$ déduite de
l'ext. $\Phi^i$ (*) par $n\operatorname{id}_{\Psi^{i-1}}$, de
sorte qu'on a un hom des suites
ex. can
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r]&\Psi^{i-1}\arrow[r,"\iota_i"]\arrow[d,"n\operatorname{id}"']&
\Phi^i\arrow[r,"u_i"]\arrow[d]&\Psi^i\arrow[r]\arrow[d,"\operatorname{id}"]&0\\
0\arrow[r]&\Psi^{i-1}\arrow[r]&\Phi(i,n)\arrow[r,dash]&\Psi^i\arrow[r,dash]&0
\end{tikzcd}}
(\uline{NB}\quad $\Phi(i,1)=\Phi^i$)
\margin{On a aussi
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
0\arrow[r,dash]&\Psi^{i-1}\arrow[r,dash]\arrow[d,"\operatorname{id}"']&
\Phi(i,n)\arrow[r,dash]\arrow[d]&\Psi^i\arrow[r]\arrow[d,"n\operatorname{id}"]&0\\
0\arrow[r,dash]&\Psi^{i-1}\arrow[r]&\Phi^i\arrow[r]&\Psi^i\arrow[r]&0
\end{tikzcd}}}
Alors on a
\[
\operatorname{Hom}(\Phi(i,n),\Phi(j,m))\longrightarrow
\operatorname{Hom}(\Psi^i,\Psi^j)
\]
et si $j\neq i$, le dernier Hom est nul,
donc si $j\neq i$, la structure d'extension
est respectée par tt hom $\alpha:\Phi(i,n)\longrightarrow\Phi(j,m)$
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r,dash]&\Psi^{i-1}\arrow[r,dash]\arrow[d]&\Phi(i,n)\arrow[r]\arrow[d]&
\Psi^i\arrow[r,dash]\arrow[d]&0\\
0\arrow[r,dash]&\Psi^{j-1}\arrow[r,dash]&\Phi(j,m)\arrow[r,dash]&\Psi^j\arrow[r,dash]&0
\end{tikzcd}}
Si \inserted{de plus} $j\neq i$, les flèches verticales extrêmes
sont nulles, donc on trouve
\[
\operatorname{Hom}(\Phi(i,n),\Phi(j,m))\simeq
\operatorname{Hom}(\Psi^i,\Psi^{j-1})
\]
\inserted{$\simeq k$ si $j=i+1$,\quad $0$ si $j\neq i+1$}
\margin{\unsure{via composée}
$\Phi(i,n)\longrightarrow\Psi^i\longrightarrow\Psi^{j-1}\longrightarrow\Phi(j,m)$}

\uline{Cas $j=i$}. Tout hom induit une
$p.\operatorname{id}$ sur $\Psi^{i-1}$ et $q.\operatorname{id}$ sur $\Psi^i$,
\diagram{\begin{tikzcd}[column sep=large]
0\arrow[r,dash]&\Psi^{i-1}\arrow[r,dash]\arrow[d,"p\operatorname{id}"']&
\Phi(i,n)\arrow[r,dash]\arrow[d,"\alpha"]&\Psi^i\arrow[r,dash]\arrow[d,"q\operatorname{id}"]&0\\
0\arrow[r,dash]&\Psi^{i-1}\arrow[r,dash]&\Phi(i,m)\arrow[r,dash]&\Psi^i\arrow[r,dash]&0
\end{tikzcd}}
\unsure{$p,q$ uniquement déterminés par $\alpha$.}
On a alors (pour qu'il existe $\alpha$ défini sur
$p$ et $q$) que l'élément de $\operatorname{Ext}^1(\Psi^i,\Psi^{i-1})$
défini par $q^*(e_{i,n})-p_*(e_{i,m})$ (où
$e_{i,n}$, $e_{i,m}$ désignent resp. les ext $\Phi(i,n)$ et $\Phi(i,m)$)
'''
record(23,tex,[('text','left top heading','En résumé; catégorie abélienne'),('insertion','left above abélienne','k-lin. C'),('text','left top','k-modules ½ simpliciaux; sous-catégorie additive C0'),('insertion','left above parfaits','str. ∂-'),('diagram','left upper cochain sequence','Φ^(0)→Φ^(1)→Φ^(2)→…→Φ^(i)—λ_i→Φ^(i+1)'),('text','left a','Complexe str. acyclique dans C'),('deletion','left end a','∀i≥0'),('text','left b','Pour tout i,j≥0'),('display','left b cases','Hom(Φ^i,Φ^j):0,k id,kλ_i'),('deletion','left before Posant','c)'),('display','left definition of Ψ','Ψ^(i)=Z^(i+1)(Φ*)=Ker_C'),('insertion','below definition','Coker_C(Φ^(i−1)→Φ^i)'),('margin note','left of definition','conséq. de a) b)'),('text','left continuation','on a donc'),('deletion','left continuation','Hom(Ψ_i'),('display','left middle','Ψ^0≃Φ^0'),('diagram','left canonical extension','0→Ψ^(i−1)→Φ^i→Ψ^i→0; Φ^(i−1),Φ^(i+1); u,ι,λ'),('display','left first lower Hom','Hom(Ψ^i,Ψ^j)⊂Hom(Φ^i,Φ^(j+1))'),('deletion','first lower cases','i+1'),('display','left second lower Hom','Hom(Φ^i,Ψ^j)⊂Hom(Φ^i,Φ^(j+1))'),('deletion','second lower Hom','≃'),('display','left third lower Hom','Hom(Ψ^i,Φ^j) three cases'),('margin note','center beside Hom formulas','via composée Φ^i→Ψ^i→Φ^(j+1)'),('text','left bottom d','Soit pour n∈k−0, Φ(i,n)'),('deletion','left d after Soit','Φ(i)'),('insertion','left d above n','et i≥1'),('deletion','left d after ext de','Φ^i'),('text','left d continuation','extension Ψ^i par Ψ^(i−1); n id'),('diagram','right top','two exact sequences; n id, unnamed middle arrow, id'),('text','right top NB','Φ(i,1)=Φ^i'),('margin note','upper right','On a aussi'),('diagram','upper right small alternative','Φ(i,n)→Φ^i diagram; id and n id'),('text','right upper','Alors on a'),('display','right Hom map','Hom(Φ(i,n),Φ(j,m))→Hom(Ψ^i,Ψ^j)'),('text','right middle','j≠i; Hom nul; structure d’extension respectée'),('diagram','right middle comparison','Φ(i,n)→Φ(j,m) between Ψ endpoints'),('insertion','right after Si','de plus'),('text','right lower-middle','flèches verticales extrêmes nulles'),('display','right lower-middle Hom','Hom(Φ(i,n),Φ(j,m))≃Hom(Ψ^i,Ψ^(j−1))'),('insertion','right below Hom','k si j=i+1; 0 si j≠i+1'),('margin note','center oblique','via composée Φ(i,n)→Ψ^i→Ψ^(j−1)→Φ(j,m)'),('text','right case j=i','Tout hom induit p id et q id'),('diagram','right lower case j=i','two extension rows; p id, α, q id'),('text','right below diagram','p,q uniquement déterminés par α'),('text','right bottom obstruction','élément de Ext^1; q*(e_i,n)−p_*(e_i,m)')],doubts=[('left opening C0 qualifier','en question / engendrée','faint joined word','low'),('left complex type','cochaînes','handwritten word faint over staff','medium'),('left a deletion','∀i≥0','blue hatching; condition not completely recoverable','low'),('left b labels','Φ_*^(i),Φ_*^(j)','overwritten sub/superscripts, intended shapes not silently normalized','medium'),('left definition of Ψ','Z^(i+1); Ker(Φ^(i+1)→Φ^(i+2))','tiny shifts; λ index particularly uncertain','low'),('left added Coker','Φ^(i−1)→Φ^i','small cramped addition','medium'),('left canonical diagram','ι_i,u_i,λ_i,λ_i−1','multiple reinforced arrows; arrow-head type locally uncertain','medium'),('left Hom inclusions','Hom(Φ^i,Φ^(j+1)); Hom(Φ^i,Φ^j)','small extra superscripts and crossing staff','low'),('left Hom case exception','i≠0; j=i=0','several alterations; exceptional third line retained','medium'),('center notes','via composée ...','oblique words crossing fold; three words unreadable','low'),('left d deleted Φ','Φ(i), Φ^i','dense cancellation','low'),('right small alternate diagram','id,n id labels; Φ(i,n) above Φ^i','tiny writing, independently represented','medium'),('right inequality clauses','j≠i','reinforced corrections after i; inequality visible','medium'),('right lower Hom zero case','j≠i+1','small parentheses/extra marks after i unclear','low'),('right bottom p,q sentence','p,q uniquement déterminés par α','faint abbreviated line','low'),('right final obstruction wording','pour qu’il existe α défini sur p et q','compressed prose, grammatical form retained tentatively','low'),('right Ext expression','q*(e_i,n)−p_*(e_i,m)','star positions fairly clear; e subscripts faint','medium')],notation=[('local cochain-style abbreviations',r'$\Phi^i,\Psi^i$','scan 23 shifts to superscripts; not changed back into exterior powers'),('parenthesized superscripts',r'$\Phi_*^{(i)},\Psi_*^{(i)}$','scan 23 early formulas; parentheses retained locally'),('extension maps',r'$\iota_i,u_i,\lambda_i$','scan 23 canonical sequence'),('extension class notation',r'$e_{i,n},q^*,p_*$','scan 23 lower right; stars are operations, not primes')])
