# Context search evidence for real/Hodge research

CT = supplied first-pass transcription `context/MPL_16+47+54+44_transcription.tex`; these are leads, not audited readings.

## period-normalization: `Kummer|2.*pi|Tate|TATE`

- CT 16/3, line 64: \node[anchor=west] at (2.1,.55) {$\left\{\begin{aligned}\pi_i^2&=\pi_i\\\pi_i\pi_j&=0\quad\text{si }i\neq j\\\sum\pi_i&=1\end{aligned}\right.$};
- CT 16/3, line 70: 2. Soit $\mathcal E^*$ une \deleted{$k$-algèbre}\inserted{anneau} graduée, et soient $\pi_i$ ($i\in\mathbb Z$) des éléments de $\mathcal E$, \inserted{nuls sauf un nb fini.} A quelles conditions les formules $(\unsure{1.3})$ définissent-elles
- CT 16/4, line 80: \pi_i^2&=\pi_i\\
- CT 16/5, line 139: donc $\mathcal E^0$ est le commutant de la $k$-algèbre engendrée par les $\pi_i$. Donc les $\pi_i$ sont dans le centre $\unsure{Z|\mathfrak Z}(\mathcal E^0)$ de $\mathcal E^0$, et ce sont des projecteurs \inserted{mutuellement} orthogonaux de somme $1$ de cet anneau commutatif. Supposons déterminés déjà les $\pi_\alpha$ pour $\alpha\notin[i,2n-i]$, \inserted{$i<n$,} et déterminons $\pi_i$ et $\pi_{2n-i}$ [i.e. $\pi_\alpha$ pour $\alpha\notin[i+1,2n-i-1]$.]
- CT 16/5, line 141: \node[anchor=north west,align=left,font=\small] at (.2,.8) {C'est clair si $i=n-1$, car on connaît les\\$\pi_\alpha$ pour $\alpha\neq n$, d'où on conclut $\pi_n=1-\sum_{\alpha\neq n}\pi_\alpha$. \unsure{Restons}\\donc pour $i<n-1$.};
- CT 16/5, line 148: \psi_{2n-i}=\left(1-\sum_{\alpha>2n-i}\pi_{\unsure{i|\alpha}}\right)=\sum_{\alpha\leq 2n-i}\pi_\alpha
- CT 16/5, line 153: =\sum_\alpha\psi_{2n-i}\pi_{\alpha+(2n-2i)}\mathcal E\pi_\alpha\varphi_i\unsure{)}
- CT 16/5, line 159: \psi_{2n-i}\pi_{\alpha+(2n-2i)}=
- CT 16/5, line 167: \pi_{\unsure{i|\alpha}+(2n-2i)}\mathcal E\pi_i=\pi_{2n-i}\mathcal E\pi_i=\mathcal E_{2n-i,i}.
- CT 16/6, line 176: $\unsure{u_{2n-i}|\pi_{2n-i}}$ est \unsure{donc} la \deleted{\unsure{qui}} conjonction des suivantes :
- CT 16/6, line 181: \figure{\begin{tikzpicture}[baseline=(e.base)]\node[draw,ellipse,inner sep=2pt] (e) {$\mathcal E_i^{2n-i}$};\end{tikzpicture}}u=0\bigr)
- CT 16/6, line 187: En effet, la relation $(3.1.)$ implique que \deleted{$\unsure{\pi_i(\mathfrak Z\mathcal E^0)}$}\inserted{l'annulateur de $\pi_i$ dans $\unsure{\mathfrak Z|\mathcal Z}\mathcal E^0$} est l'idéal des $u\in\unsure{\mathfrak Z|\mathcal Z}\mathcal E^0$ tels que $\mathcal E_i^{2n-i}u=0$; or dans un anneau commutatif, un idempotent est connu quand on connaît son annulateur. De même pour $\pi_{2n-i}$, son annulateur dans $\unsure{\mathfrak Z|\mathcal Z}\mathcal E^0$ est formé des $u\in\unsure{\mathfrak Z|\mathcal Z}\mathcal E^0$ tels que $u\mathcal E_i^{2n-i}=0$.
- CT 16/6, line 189: En même temps, les conditions $(3.1.)_i$, $(3.2.)_i$ pour tt $i$, donnent un \deleted{condition} procédé pour déterminer de proche en proche les $\pi_i$.
- CT 16/6, line 191: \figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[line width=.2pt] (0,0) .. controls (2,.15) and (3,-.04) .. (5,.08) .. controls (8,.25) and (10,.30) .. (12,.15);\draw[line width=.2pt] (.2,-.08) .. controls (1,.01) and (1.9,-.03) .. (2.6,-.05) .. controls (3.4,-.17) and (3.9,-.23) .. (4.2,-.07);\end{tikzpicture}}
- CT 16/7, line 216: Or, sans plus supposer que $\mathcal E^*$ se réalise à l'aide d'un $M^*$, on voit aussitôt que $(4.4)_i$ implique $(3.1)_i$ et $(3.2)_i$. En effet, quitte à remplacer $v,w$ par $v\pi_i=\pi_{2n-i}v$, $w\pi_{2n-i}=\pi_iw$, on peut supposer $v,w$ dans $\mathcal E_i^{2n-i}$, $\mathcal E_{2n-i}^i$. Si alors \deleted{\unsure{u}} $u\in\mathcal E^{(0)}$ est tel que $\mathcal E_i^{2n-i}u=0$, donc $vu=0$, on aura $wvu\pi_i\deleted{\unsure{=}}=0$ i.e. $wv\pi_i u=0$ donc $\pi_i u=0$ (car $wv\pi_i=\pi_i$). De $=$ pour $(3.2)_i$, en utilisant la deuxième relation $(\unsure{4.4})_i$.
- CT 16/8, line 244: \deleted{\unsure{Raisonnons par récurrence sur $i$.}}\inserted{Supposons prouvé \deleted{\unsure{que}} déjà $\pi_\alpha\in\mathcal E$ si $\alpha\notin[i,2n-i]$,} où $i<n$, et prouvons que l'on peut remplacer $i$ par $i+1$, \inserted{i.e. $\pi_i$ et $\pi_{2n-i}\in\mathcal E$.}\inserted{Trivial si $i=n-1$, supposons que $i\leq n-2$.}
- CT 16/8, line 249: \inserted{v'_i={}}\psi_{2n-i}v_i\varphi_i&=\pi_{2n-i}v_i\pi_i\in\mathcal E\\
- CT 16/8, line 250: \inserted{w'_i={}}\varphi_iw_i\psi_{2n-i}&=\pi_iw_i\pi_{2n-i}\in\mathcal E
- CT 16/8, line 255: w'_iv'_i=\pi_iw_i\pi_{2n-i}v_i\pi_i
- CT 16/8, line 256: \inserted{\quad\text{car }w_i\pi_{2n-i}=\pi_iw_i}\]
- CT 16/8, line 262: et de $=$ \deleted{$\unsure{=\pi_i}$} $v'_iw'_i=\pi_{2n-i}$, on conclut que $\pi_i\in\mathcal E$, $\pi_{2n-i}\in\mathcal E$.
- CT 16/9, line 271: Ceci implique déjà $(4.1)_i$ et $(4.2)_i$ donc $(3.1)_i$ et $(3.2)_i$; \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
- CT 16/9, line 279: \deleted{\unsure{Ceci}} L'ensemble des deux conditions $(6.1)$ et $(6.2)$, équivalent [en termes intrinsèques à $\mathcal E^*$, muni de $L\in\mathcal E^2$ si on suppose déjà les $\pi_i\in\mathcal E^*$]
- CT 16/9, line 287: Cette condition à son tour (indépendamment de la donnée préliminaire d'un $M^*$) implique $(4.4)_i$, \deleted{et on a donc $(3.1)_i$ et $(3.2)_i$}, \figure{\begin{tikzpicture}[x=1cm,y=1cm]
- CT 16/9, line 289: \node at (2.4,.65) {\inserted{$\pi_i\in\mathcal E$ et,}};
- CT 16/9, line 303: On désigne par $\pi_{i,\alpha}$ la projection de $M^i$ sur $L^\alpha P^{i-2\alpha}$, par $\pi_{2n-i,\alpha}$ celle de $M^{2n-i}$ sur $L^{n-i+\alpha}P^{i-2\alpha}$,
- CT 16/10, line 315: (i) Les conditions \inserted{$(6.1)_i$ et} $(6.2)_i$ pour tt $i$, et les $\pi_i\in\mathcal E$.
- CT 16/10, line 342: \Lambda L&=1-\sum_{n\leq i\leq2n}\pi_{i,0}
- CT 16/12, line 409: \pi_{i,\alpha}=L^\alpha w_{i-2\alpha}L^{n-i+\alpha}q_{i\alpha}=L^\alpha w_{i-2\alpha}L^{n-i+\alpha}(1-\sum_{\alpha'>\alpha}\pi_{i,\unsure{\alpha'}}
- CT 16/12, line 416: q_{2n-i,\alpha}=1-\sum_{\alpha'>\alpha}\pi_{2n-i,\alpha'}
- CT 16/12, line 424: \pi_{2n-i,\alpha}=L^{n-i}\pi_{i,\alpha}w_i\deleted{\unsure{\pi_{2n-i}}}
- CT 16/13, line 444: \left\{\quad\Lambda\pi_{i0}=0,\qquad\Lambda\pi_{i\alpha}=L^{\unsure{\alpha-1}}w_{i-2\alpha}L^{n-i+\alpha}\pi_{i\alpha}\quad\text{si }\alpha\geq1,\right.
- CT 16/13, line 453: \Lambda\pi_{2n-i,\alpha}=L^{n-i+\unsure{\alpha}-1}w_{i-2\alpha}\deleted{\unsure{\pi_{2n-i,\alpha}}}L^\alpha\pi_{2n-i,\alpha}\quad(\text{si }i\unsure{\leq|<}n-1)
- CT 16/13, line 458: \uline{Remarque} Voici un système de conditions déterminant de façon unique les éléments $\Lambda\in\mathcal E^{\unsure{(2)|(-2)}},\ \pi_{i,\alpha}\in\mathcal E^{(0)}$ en termes de $L$, et des $\pi_i\deleted{\unsure{\alpha}}$ (dont nous avons déjà une caractérisation intrinsèque par ailleurs, en termes de l'anneau gradué $\mathcal E$) :
- CT 16/13, line 463: \qquad\textcircled{2}\quad\deleted{\unsure{\pi_{2n-i}}}(L^{n-i}\Lambda^{n-i}-1)\deleted{\unsure{\pi_{2n-i}}}\pi_{2n-i}=0\\
- CT 16/13, line 464: \textcircled{3}\quad &\pi_{i,\alpha}=L^\alpha\deleted{\unsure{w_{i-2\alpha}}}\inserted{\Lambda^{n-i+2\alpha}}L^{n-i+\alpha}\bigl(1-\sum_{\alpha'>\alpha}\pi_{i,\alpha'}\bigr)\\
- CT 16/13, line 465: \textcircled{4}\quad &\pi_{2n-i,\alpha}=L^{n-i}\pi_{i,\alpha}\Lambda^{n-i}\\
- CT 16/13, line 468: \textcircled{6}\quad &\Lambda\pi_{i\alpha}=L^{\alpha-1}\Lambda^{n-i+2\alpha}L^{n-i+\alpha}\pi_{i\alpha}\quad\text{si }\alpha\geq1\\
- CT 16/13, line 469: \textcircled{7}\quad &\Lambda\pi_{2n-i,\alpha}=L^{n-i+\alpha-1}\Lambda^{n-i+2\alpha}L^\alpha\pi_{2n-i,\alpha}\quad\text{si }\unsure{\alpha|i}\leq n-1\\
- CT 16/14, line 490: \Lambda L&=1-\sum_{n\leq j\leq2n}\pi_{\deleted{\unsure{2}}j,0}
- CT 16/14, line 507: Partons pour ceci \deleted{de} d'un module libre $\mathbf M_0$ de rang $2n$ sur $\mathbb Z$, muni d'une $2$-forme alternée non dégénérée \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
- CT 16/14, line 510: \end{tikzpicture}}} $\xi_0\in\bigwedge^2\mathbf M_0$, \inserted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
- CT 16/17, line 668: \text{``}\ \exists w_i\in\mathcal E^{-(2n-2i)}\text{ tel que}\quad(w_iL^{n-i}-1)\pi_{\deleted{\unsure{i}}\inserted{2n-i}}\deleted{=0}\text{''}=0,
- CT 16/17, line 690: \figure{\begin{tikzpicture}\node at (0,0) {Non};\draw (80:.65cm) arc[start angle=80,end angle=400,radius=.65cm];\end{tikzpicture}}, déjà dans le cas $n=1$, $2n=2$, où il y a une base de $\Phi$ formée de $\pi_0,\pi_1,\pi_2,L,\Lambda$, et où $\mathbb Z[L]$ n'est que $\mathbb Z+\mathbb ZL$ ! Il faut donc se donner en même temps \uline{$L$ et les $\pi_i$}.
- CT 16/18, line 699: \node[align=left,text width=3.8cm,rotate=25] at (0,0) {un n\textsuperscript{o} : ``principe de dualité'' pour les anneaux de correspondances Lefschetziens.};
- CT 16/18, line 708: &(\Longleftrightarrow)\quad2)\ \pi_0,\deleted{\unsure{\pi_{2n}}}\neq0\quad\deleted{\unsure{\}}}
- CT 16/18, line 712: \node[align=left] at (0,0) {$\Longleftrightarrow\quad2')\ \pi_{2n}\neq0$};
- CT 16/18, line 713: \node[rotate=24] at (.15,1.7) {\unsure{déjà pour}};
- CT 16/18, line 714: \draw[rotate=24] (.8,1.45) ellipse (1.15cm and .35cm);
- CT 16/19, line 752: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(.18,.22);\draw (.03,.2)--(.16,.05);\end{tikzpicture}}}
- CT 16/19, line 769: dont on constate aisément qu'elle est indépendante de la résolution $X'$ choisie.
- CT 16/19, line 772: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(.18,.22);\draw (.03,.2)--(.16,.05);\end{tikzpicture}}}
- CT 16/21, line 864: on trouve une suite exacte canonique \inserted{(où $Z_\ell[1]=\varprojlim_\nu\deleted{Z}\mu_{\ell^\nu}$ est le faisceau $\ell$-adique de TATE)}:
- CT 16/21, line 882: \inserted{8.2.} Un passage à la limite analogue dans \deleted{les suites exactes}\inserted{la suite exacte} de Kummer (BR II 3.1) nous donne de même une suite exacte
- CT 16/21, line 886: en supposant maintenant que $\operatorname{Pic}(X)$ est extension d'un groupe de type fini $\operatorname{NS}(X)$ (le \uline{groupe de Néron--Sévéri}) par un groupe divisible, et que $H^2(X,\uline Z/\ell\uline Z)$ est fini. \deleted{\unsure{x}}On trouve en passant le fait, classique dans la théorie transcendante, que \deleted{le}\inserted{\figure{\begin{tikzpicture}
- CT 16/22, line 910: \node[anchor=base west] at(-2.8,-.9){$\displaystyle =L_0^{\unsure{n|\prime n}}\circ\alpha\beta\pi_0=\alpha\beta L_0^n.$};
- CT 16/23, line 963: \inserted{8.3.} Ce résultat ne concerne essentiellement que la partie divisible $\operatorname{Br}'(X)^0$ du groupe de Brauer cohomologique. On peut également donner une relation de dualité concernant le \deleted{\unsure{gour|grou}} groupe fini $\operatorname{Br}'(X)/\operatorname{Br}'(X)^0$, qui grâce à la suite exacte de Kummer (BR II 3.1) s'explicite comme
- CT 16/27, line 1129: \operatorname{Sym}^2(\bigwedge^2V)\arrow[rr,bend right=18,"\unsure{épi.}"']\&\text{, se factorise en}\&\bigwedge^4V
- CT 16/28, line 1183: [27] Tate, J., \uline{Cohomology of abelian varieties over p-adic fields}, (Cf. Notes by S. Lang, Princeton University, May, 1959.)
- CT 16/29, line 1199: \figure{\begin{tikzpicture}[x=0.3cm,y=0.3cm]\draw (0,4) .. controls (0.7,4) and (0.5,2) .. (1.4,1.2) .. controls (2.3,0.8) and (3.8,1.1) .. (4,0.1)--(4.3,-0.1);\end{tikzpicture}}
- CT 16/30, line 1219: However, the right hand group vanishes by results of Tate [27], and the proof is complete.
- CT 16/40, line 1560: \figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,.3)..controls(1,.5)and(2,.5)..(2.2,.15)..controls(2.3,-.1)and(2.25,-.3)..(2.6,-.3)--(7,-.4);\end{tikzpicture}}
- CT 16/42, line 1661: \node[rotate=45,text=blue!35] at (0.0,12.600000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1662: \node[rotate=45,text=blue!35] at (2.1,12.600000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1663: \node[rotate=45,text=blue!35] at (4.2,12.600000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1664: \node[rotate=45,text=blue!35] at (6.300000000000001,12.600000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1665: \node[rotate=45,text=blue!35] at (8.4,12.600000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1666: \node[rotate=45,text=blue!35] at (10.5,12.600000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1667: \node[rotate=45,text=blue!35] at (0.0,10.5){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1668: \node[rotate=45,text=blue!35] at (2.1,10.5){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1669: \node[rotate=45,text=blue!35] at (4.2,10.5){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1670: \node[rotate=45,text=blue!35] at (6.300000000000001,10.5){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1671: \node[rotate=45,text=blue!35] at (8.4,10.5){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1672: \node[rotate=45,text=blue!35] at (10.5,10.5){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1673: \node[rotate=45,text=blue!35] at (0.0,8.4){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1674: \node[rotate=45,text=blue!35] at (2.1,8.4){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1675: \node[rotate=45,text=blue!35] at (4.2,8.4){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1676: \node[rotate=45,text=blue!35] at (6.300000000000001,8.4){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1677: \node[rotate=45,text=blue!35] at (8.4,8.4){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1678: \node[rotate=45,text=blue!35] at (10.5,8.4){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1679: \node[rotate=45,text=blue!35] at (0.0,6.300000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1680: \node[rotate=45,text=blue!35] at (2.1,6.300000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1681: \node[rotate=45,text=blue!35] at (4.2,6.300000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1682: \node[rotate=45,text=blue!35] at (6.300000000000001,6.300000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1683: \node[rotate=45,text=blue!35] at (8.4,6.300000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1684: \node[rotate=45,text=blue!35] at (10.5,6.300000000000001){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1685: \node[rotate=45,text=blue!35] at (0.0,4.2){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1686: \node[rotate=45,text=blue!35] at (2.1,4.2){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1687: \node[rotate=45,text=blue!35] at (4.2,4.2){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1688: \node[rotate=45,text=blue!35] at (6.300000000000001,4.2){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1689: \node[rotate=45,text=blue!35] at (8.4,4.2){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1690: \node[rotate=45,text=blue!35] at (10.5,4.2){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1691: \node[rotate=45,text=blue!35] at (0.0,2.1){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1692: \node[rotate=45,text=blue!35] at (2.1,2.1){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1693: \node[rotate=45,text=blue!35] at (4.2,2.1){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1694: \node[rotate=45,text=blue!35] at (6.300000000000001,2.1){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1695: \node[rotate=45,text=blue!35] at (8.4,2.1){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1696: \node[rotate=45,text=blue!35] at (10.5,2.1){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1697: \node[rotate=45,text=blue!35] at (0.0,0.0){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1698: \node[rotate=45,text=blue!35] at (2.1,0.0){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1699: \node[rotate=45,text=blue!35] at (4.2,0.0){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1700: \node[rotate=45,text=blue!35] at (6.300000000000001,0.0){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1701: \node[rotate=45,text=blue!35] at (8.4,0.0){\unsure{Condor|Cordor|Concorde}};
- CT 16/42, line 1702: \node[rotate=45,text=blue!35] at (10.5,0.0){\unsure{Condor|Cordor|Concorde}};
- CT 16/44, line 1723: I think the best will be to state the index conjecture right after the statement of the main results of Hodge theory, adding that this conjecture will take its whole significance only when coupled with ``conj.A'' in the next paragraph. This will give more freedom in the next paragraph to express some extra relationships between various conjectures, such as $A+\text{index}$ implies $B$.
- CT 16/44, line 1725: In c\inserted{h}ar. zero, state some known extra features: index theorem holds, the \deleted{conjectures}\inserted{propositions} $A_{\unsure{\ell|\chi}}$ to $D_{\unsure{\ell|\chi}}$ are independant of $\unsure{\ell|\chi}$ (because of the existence of Betti cohomology, so that these \deleted{conjectures}\inserted{propositions} are equivalent to the corresponding one's for rational cohomology), \deleted{and} $A$ and $C$ are independant of the choosen polarization$_{\mathrm{x}}$ (for $A$ because it is equivalent with $B$, for $C$ because it can be expressed in terms of $A$, $C(X)=(A(X\mathrm{x}X)+A(Y\mathrm{x}Y)+\mathinner{..})$ Thus the \deleted{conjectures}\inserted{conditions} without ambigu
- CT 16/46, line 1778: For the list of the known facts, you can state that :
- CT 16/46, line 1780: 1) In arbitrary caracteristics, $C(X)$ is known if $\dim X\leq2$, because more generally, it is known that in arbitrary dimension $n$, $H^{2n-1}(X)\to H^1(X)$ is induced by an algebraic correspondance class; also, in arbitrary dimension, it is known that $\pi_0,\pi_{2n},\pi_1,\pi_{2n-1}$ are algebraic (trivial for the first two, not quite trivial for the two next one's). If $\dim X=3$, it is not known however, even in \unsure{dim|car} $0$, if $C(X)$ or only $D(X)$ hold, nor $A(X)$ and $B(X)$ in car. $p>0$;
- CT 16/47, line 1787: By the way, the fact that the $\pi_1$ for a surface are algebraic was pointed out (Tate tells me) by Hodge in Algebraic correspondances between surfaces, Proc. London Math. \unsure{Soc.} Seeies 2, Vol XLIV, 1938, p.226. It is rather striking that this statement should not have struck the algebraic geometers more, and has fallen into oblivion for \inserted{nearly} thirty years !
- CT 16/49, line 1823: NB In char. 0, \deleted{it is} the statement simplifies to: $C(X)$ equivalent to the existence of algebraic isomorphisms $H^{2n-i}(X)\to H^i(X)$,(as the preliminaray condition in b) is then automatically satisfied). Maybe with some extra care this can be proved too in arbitrary characteristics.
- CT 16/50, line 1845: \uline{Proposition}\quad $\unsure{C|A}_{\unsure{\ell|\chi}}(X)$ is equivalent to the \unsure{conjunction} $C_{\unsure{\ell|\chi}}(Y)+A'_{\unsure{\ell|\chi}}(X\times X)^0+A''_{\unsure{\ell|\chi}}(X\times X)^0$, hence (by induction) also to the conjunction of the conditions ${A'_{\unsure{\ell|\chi}}}^0$ and ${A''_{\unsure{\ell|\chi}}}^0$ for all of the varieties $X\times X,Y\times Y,Z\times Z\ \mathinner{\ldotp\ldotp\ldotp\ldotp}\ .$ Analogous statement with $X\times Y,Y\times Z$ etc instead of $X\times X,Y\times Y$ etc.
- CT 16/52, line 1912: Définir la différente de Dedekind par la trace, et montrer qu'elle coïncide avec celle de Kähler quand $A$ et $B$ sont des anneaux de valuation discrète (il s'agit du gros th. 3 du n° 7, § 2, avec son dévissage, -- éventuellement agrémenté des lemmes du n° 6 s'ils n'ont pas été faits dans un chapitre antérieur pour illustrer la notion d'intersection complète. En tous cas on aura dit que si $A$ et $B$ sont réguliers, $A\to B$ est une intersection complète relative. La prop. 11 sera éclairée par le lemme suivant :
- CT 16/52, line 1922: Donner la description Kummerienne des extensions totalement et modérément ramifiées (extraire la racine n-ième d'une uniformisante bien choisie ; ceci dans le cas complet); exemple des surfaces de Riemann (ici le groupe de Galois a un générateur canonique $\exp\left(\dfrac{2i\pi}{n}\right)$).
- CT 47/4, line 2159: A\times A \arrow[d,"\pi"'] \arrow[dr,phantom,"\text{\textcircled{cart}}"] \& A\times_S A\times_S B \arrow[l,"\operatorname{pr}_{12}"'] \arrow[d,"\pi\times\operatorname{id}_B"] \arrow[dr,"\operatorname{pr}_3"] \& \\
- CT 47/4, line 2173: &=\mathbf R\operatorname{pr}_{2*}\bigl(\mathbf L\operatorname{pr}_1^*(\unsure{\pi_*|\mathbf R\pi_*}(F\overset{\mathbf L}{\otimes}G))\inserted{\otimes\mathcal L}\bigr)\\
- CT 47/4, line 2175: \mathbf R\operatorname{pr}_{2*}\bigl(\mathbf R(\pi\times\operatorname{id}_B)_*\bigl(\mathbf L\operatorname{pr}_{12}^*(F\overset{\mathbf L}{\otimes}_S G)\bigr)\otimes\mathcal L\bigr)\\
- CT 47/4, line 2177: \mathbf R\operatorname{pr}_{2*}\bigl(\mathbf R(\pi\times\operatorname{id}_B)_*\bigl(\mathbf L\operatorname{pr}_{12}^*(F\overset{\mathbf L}{\otimes}_S G)\otimes(\pi\times\operatorname{id}_B)^*(\mathcal L)\bigr)\bigr)\\
- CT 47/4, line 2179: \mathbf R\operatorname{pr}_{3*}\bigl(\mathbf L\operatorname{pr}_{12}^*(F\overset{\mathbf L}{\otimes}_S G)\otimes(\pi\times\operatorname{id}_B)^*(\mathcal L)\bigr).
- CT 47/4, line 2190: \mathbf L\operatorname{pr}_{12}^*(F\overset{\mathbf L}{\otimes}_S G)\otimes(\pi\times\operatorname{id}_B)^*(\mathcal L)
- CT 47/10, line 2474: \node at (2.9,.55) {par R.R. pour $A\times A\xrightarrow{\pi_A}A$};
- CT 47/10, line 2504: \margin{\figure{\begin{tikzpicture}[x=.25cm,y=.55cm]\draw (1,2.1)--(.15,2.1)..controls (0,2.1) and (0,1.8)..(0,1.6)--(0,.2)..controls (0,0) and (.2,0)..(1,0);\end{tikzpicture}}}
- CT 54/4, line 2679: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(-.2,.05)--(-.24,.4)--(-.25,1.7)--(0,1.75);\end{tikzpicture}}}
- CT 54/5, line 2684: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(-.12,1.15);\draw (.05,0)--(-.07,1.15);\end{tikzpicture}}}
- CT 44/2, line 2787: \uline{Th. 1} $N(\unsure{\xi|\zeta})\subset\operatorname{Alb}(S)$ n'est autre\deleted{\unsure{des|donc}}\inserted{\figure{\begin{tikzpicture}\node[draw,rounded corners=9pt,inner sep=3pt](n){en substance};\draw(n.south west)--++(.45,-.02)--++(.04,-.25);\end{tikzpicture}}} que le noyau de l'application naturelle
- CT 44/2, line 2791: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(.2,0)--(.2,1.6)--(0,1.6);\end{tikzpicture}}}
- CT 44/2, line 2794: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(.25,0)--(.25,1.9)--(0,1.9);\draw(.12,.85)--(.25,.85);\end{tikzpicture}}}
- CT 44/2, line 2800: \margin{\figure{\begin{tikzpicture}\draw (0,0)--(.2,.05)--(.2,1.65);\end{tikzpicture}}}
- CT 44/2, line 2802: \margin{\figure{\begin{tikzpicture}\node[draw,ellipse,align=center,inner sep=4pt](n){Connu\\tel\\quel};\draw[->](n.south east)--++(.35,-.2);\end{tikzpicture}}\uline{Hodge}}
- CT 44/3, line 2840: \margin{\inserted{\uuline{En tous cas} \unsure{on voit que} $M\mapsto\hat M$ sur les modules \uline{gradués}, \figure{\begin{tikzpicture}\node at(0,.3){\unsure{TF}};\draw(-.28,.22)--(0,-.25)--(.35,.25);\end{tikzpicture}} est exact et \uline{fidèle}}}
- CT 44/4, line 2857: soient alg. équiv. à $0$\inserted{\figure{\begin{tikzpicture}\node(n){sur $Y$};\draw(n.south west) to[out=-90,in=180](.2,-.4)--(.4,-.6)--(.85,-.2);\end{tikzpicture}}}
- CT 44/4, line 2862: donc \deleted{\unsure{sont des}}\inserted{définissent des} éléments de $P^{\unsure{i}}(Y),P^{\unsure{j|0}}(Y)$ et par la forme de Néron--Tate [définie grâce à l'isomorphisme entre $P^{\unsure{i}}(Y)$ et $P^{\unsure{j|0}}(Y)$] on \deleted{alors} définit $\langle\zeta,\zeta'\rangle$. Ceci posé, on a \deleted{[au signe près ??]}
- CT 44/4, line 2868: \node[draw,ellipse,rotate=28,align=left,inner sep=6pt]{\uline{N.B.} Sauf\\si $2i=2j=n$\\les deux mbres\\sont nuls\\par Lefschetz \unsure{au|en}\\\unsure{sens général|sens géométrique}};
- CT 44/4, line 2886: \margin{\uline{``Lefschetz''}\figure{\begin{tikzpicture}\draw(0,0)--(0,3.6);\draw(.12,3.9)--(.12,4.7)--(.36,4.7);\end{tikzpicture}}}
- CT 44/5, line 2916: \margin{\figure{\begin{tikzpicture}\draw(0,.25)--(.35,.25)--(0,.55)--(.35,.55);\draw(.65,.25)--(.95,.25);\draw(.65,.55)--(.95,.55);\end{tikzpicture}}}
- CT 44/5, line 2929: \margin{\inserted{Si $\alpha'=\varphi(\alpha)$, on a $\langle\alpha',\alpha\rangle=2$}\figure{\begin{tikzpicture}\draw(0,0)--(.4,.65);\draw(.4,.65) circle(.04);\end{tikzpicture}}}

## hodge-duality: `Hodge|extension universelle|transpos`

- CT 16/18, line 697: (NB. À noter que $L$ se déduit de $\Lambda$ comme $\Lambda$ de $L$, par simple symétrie sur les degrés de $\mathcal E^*$ \deleted{$\unsure{\xi_0}$} $\unsure{-}$, et passage à l'anneau opposé --- \deleted{\unsure{transposé}} isom de transposition ---).
- CT 16/25, line 979: \begin{flushright}\fbox{Algèbres de Hodge d'ordre 2}\end{flushright}
- CT 16/31, line 1239: \begin{flushright}Algèbres de Hodge\end{flushright}
- CT 16/33, line 1285: \inserted{et formules ``transposées''.}}
- CT 16/44, line 1723: I think the best will be to state the index conjecture right after the statement of the main results of Hodge theory, adding that this conjecture will take its whole significance only when coupled with ``conj.A'' in the next paragraph. This will give more freedom in the next paragraph to express some extra relationships between various conjectures, such as $A+\text{index}$ implies $B$.
- CT 16/46, line 1767: For \unsure{thenproof|the proof} of the proposition, I told you already the equivalence of (i) and (ii),(ii bis). The equivalence of (iv) and (iv bis) is trivial by transposition, they \deleted{are of course implied by (i) because of the stabilities because $C_{\unsure{\ell|\chi}}(X)$ \unsure{et} $C_{\unsure{\ell|\chi}}(Y)$} imply (i) because $H^{2n-i}(X)\to H^i(X)$ is the compositum
- CT 16/47, line 1787: By the way, the fact that the $\pi_1$ for a surface are algebraic was pointed out (Tate tells me) by Hodge in Algebraic correspondances between surfaces, Proc. London Math. \unsure{Soc.} Seeies 2, Vol XLIV, 1938, p.226. It is rather striking that this statement should not have struck the algebraic geometers more, and has fallen into oblivion for \inserted{nearly} thirty years !
- CT 16/49, line 1827: Indeed, the two spaces can be identified ``algebraically'' (both directions !) to their dual, so taht the transpose of $u$ can be viewed as an isomorphism $u':H^{i+2\unsure{\delta|d}}(X')\mathrel{-}H^i(X)$. Thus $u'u$ is an \inserted{algebraic} automorphism \inserted{$w$} of $H^i(X)$, and by the previous argument we see that $w^{-1}$ is algebraic, hence so is $u^{-1}=w^{-1}u'$.
- CT 16/49, line 1829: As a consequence, we see that if $x\in H^i(X)$ is such that $u(x)$ is algebraic ($i$ being now assumed to be even), then so is $x$. The same result should hold in fact if $u$ is a monomorphism, the reason being that in this case there should exist a left-inverse which is algebraic; this exists indeed in a case like $H^{n-1}(X)\to H^{n-1}(Y)$ (where we take the left inverse $\Lambda_X\phi_*$). But to get \unsure{it} in general, it seems we need moreover the Hodge index relation. (The complete yoga then being that we have the category of motives which is semi-simple !). Without speeking of motives, and staying down on earth, it would be nice to explain in the notes that $C(X)$ together with th
- CT 16/51, line 1863: \uline{Lemme}\quad Soit $A$ un anneau d'endomorphismes du groupe abélien $H^*(X)$, stable par composantes homogènes (degré \uuline{total}), par transposition. \deleted{\unsure{et}} \inserted{Supposons $\xi\in A$, et} que pour tout $0\leq i<n$, il existe $u_i\in A$, \inserted{de degré $\deleted{\unsure{2n}}-2(n-i)$,} tel que
- CT 16/51, line 1879: \uline{Dém du lemme.}\quad Comme $A$ stable par transposition, il suffit de regarder les $\unsure{\xi^j|\xi_j}P^i$, pour $i+2j\leq n$. Soit $k=i+2j$. -- procéder par récurrence sur $k$, trivial si $k<0$.
- CT 54/3, line 2614: \qquad \text{\unsure{Ch.|Coh.} de Hodge-DeRham}
- CT 54/3, line 2633: \unsure{donc} l'extension universelle est
- CT 54/3, line 2646: et que de plus elle est \uline{\unsure{transposée}} de $S_A$, ce qui donne en passant
- CT 54/7, line 2716: formellement sur le diagramme des deux suites transposées l'une de l'autre
- CT 44/2, line 2802: \margin{\figure{\begin{tikzpicture}\node[draw,ellipse,align=center,inner sep=4pt](n){Connu\\tel\\quel};\draw[->](n.south east)--++(.35,-.2);\end{tikzpicture}}\uline{Hodge}}
- CT 44/8, line 2974: Je commence à avoir de faibles lumières sur la façon de faire \inserted{d}es VA avec les cycles al\inserted{g}ébriquement équivalents à zéro d'une variété projective non singulière $X$ (sur un corps alg clos $k$). Si $X$ est connexe de dimension $n$, je sais associer à chaque entier $i$ \inserted{c}ompris entre $\unsure{0|1}$ et $n$ une VA $J^i(X)$, jouant le rôle d'une ``jacobienne intermédiaire'' au sens de Weil, correspondant à des classes de cycles de codimension $i$ (pour une relation d'équivalence que je ne sais pas bien identifier pour l'instant, mais qui mérite certainement d'être appelée ``équivalence d'Albanese''). Je suis moralement sûr que ce sont ``les bonnes'', bien que je n'ai
- CT 44/8, line 2977: \margin{\deleted{$H^{\unsure{1|i}}(J^i)\simeq$ \unsure{Alg. de Hodge}}}
- CT 44/8, line 2979: Moyennant un certain nombre de choses non prouvées (qui risquent d'ailleurs d'être vaches) le théorème de positivité de Hodge se ramène à l'énoncé suivant, que je ne sais pas prouver, et que j'ai envie de te communiquer car il est bien terre à terre. Moralement, il s'agit de prouver que dans le cas où $\dim X=2m-1$, l'autodualité de $J^m$ (qui s'exprime par une classe de correspondance divisorielle sur $J^m\mathbin{x}J^m$ \deleted{anti} \uline{symétrique}, donc provenant -- du moins modulo le facteur 2--

## polarization: `polari|positive|ampl`

- CT 16/33, line 1249: $X$ variété projective lisse connexe polarisée par $\xi_X\in H^2(X)$, $L_X$ opération de cup-produit associée, $\Lambda_X$ opération de degré $-2$ correspondante, $p_i^X$ les projections de $H^*(X)$ sur les morceaux primitifs $P^i(X)$ pour $0\leq i\leq2n$, $Y$ une section hyperplane lisse de $X$, $\xi_Y\in H^2(Y)$ la self-intersection (induite par $\xi_X$), d'où $L_Y$, $\Lambda_Y$, $p_Y^i$; $\phi:Y\to X$ l'immersion, d'où $\phi^*$ et $\phi_*$.
- CT 16/42, line 1629: sur $X\times Y$, que nous \unsure{polarisons} par $\xi_X\otimes1+1\otimes\xi_Y$.
- CT 16/44, line 1725: In c\inserted{h}ar. zero, state some known extra features: index theorem holds, the \deleted{conjectures}\inserted{propositions} $A_{\unsure{\ell|\chi}}$ to $D_{\unsure{\ell|\chi}}$ are independant of $\unsure{\ell|\chi}$ (because of the existence of Betti cohomology, so that these \deleted{conjectures}\inserted{propositions} are equivalent to the corresponding one's for rational cohomology), \deleted{and} $A$ and $C$ are independant of the choosen polarization$_{\mathrm{x}}$ (for $A$ because it is equivalent with $B$, for $C$ because it can be expressed in terms of $A$, $C(X)=(A(X\mathrm{x}X)+A(Y\mathrm{x}Y)+\mathinner{..})$ Thus the \deleted{conjectures}\inserted{conditions} without ambigu
- CT 16/45, line 1729: se, if the index theorem is proved for $X$, then $\unsure{A|Q}_{\unsure{\ell|\chi}}(X,\inserted{\unsure{\xi}})=B_{\unsure{\ell|\chi}}(X)$ is again independant of the polarization, and analoguous remark for $C_{\unsure{\ell|\chi}}(X,\inserted{\unsure{\xi}})$.
- CT 16/45, line 1733: \uline{Proposition}\quad Condititions équivalentes sur $X$(verieté \uline{polarisée}):
- CT 16/46, line 1765: Of course, the products and hyperplane sections are endowed with the polarizations stemming from the polarization on $X$. The conditions (v) and (vi) have \unsure{thhe|the} slight interest that they allow to express the conjecture $A(k)=C(k)$ in terms of $A(T)^0$ for every $T$ of even (resp. odd dimension), where the upper $0$ means that it is sufficient to look at what happens in critical dimensions.
- CT 16/48, line 1803: Here a\inserted{\ }few more comments to my talk on the conjectures. The following proposition shows that the conjecture $C_{\unsure{\ell|\chi}}(X)$ is independant of the choosen polarization, and has also some extra interest, in showing the part playd by the fact that $H^i(X)$ should be ``motive-theoretically'' isomorphic to its natural dual $H^{2n-i}(X)$ (as usual, I drop the twist for simplicity).
- CT 44/2, line 2803: \uline{Th. 4} Si $n=2m-1$, alors l'autodualité canonique de $P^m(X)$ [\unsure{donc la corr. sur} $\uline{P}^{m}(X)$] est \unsure{associé|associée} à une \uline{polarisation} de $P^m(X)$
- CT 44/9, line 2989: d'un élément du groupe de Néron Severi de $J^m$) est \uline{positive} i.e. l'élément en question de Néron--Severi est ample, i.e. une polarisation.
- CT 44/9, line 2995: qui est une classe de diviseurs sur $T\mathbin{x}T$, que nous considérons comme une classe de correspondance divisorielle sur $T\mathbin{x}T$. Si $A=\operatorname{Alb}^0(T)$ (NB si tu veux, tu peux supposer $T=A$ et $a$ l'origine), elle provient donc d'une classe de correspondance sur $A\mathbin{x}A$, évidemment symétrique. Soit $N$ le ``noyau'' de cette classe (i.e. le noyau de $A\longrightarrow(\text{duale de }A)$ qu'elle définit), on obtient alors une classe de correspondance symétrique sur $J\mathbin{x}J$, où $J=A/N$. A prouver que cette dernière est \uline{positive} ! Je me demande si les spécialistes ``abéliens'' pourraient avoir une idée sur une telle question, peut-être Matsusaka ? O

## topology-real: `réell|Frobenius|Betti|topologi|réel`

- CT 16/28, line 1179: [25] \rule{2cm}{0.4pt}, Sur la topologie des variétés algébriques en caractéristique p, Symposium Int. de Top. Alg., 1958, Mexico City.
- CT 16/35, line 1376: Soit $\mathcal C$ une catégorie additive $^{(*)}$. Le \uline{groupe de Grothendieck} $K(\mathcal C)$ de la catégorie $\mathcal C$ est le quotient du groupe libre engendré par les classes d'isomorphie $\{G\}$ d'objets $G$ de $\mathcal C$ par le sous-groupe engendré par les relations $\{E+F\}-\{E\}-\{F\}=0$. Pour des applications topologiques du groupe de Grothendieck, voir par exemple $^{(1)}$. Dans cette note on se propose de définir de même, pour des catégories additives munies d'une certaine structure, des groupes $K^n(\mathcal C)$, $n\in Z$, avec $K^0(\mathcal C)\approx K(\mathcal C)$, jouissant de certaines propriétés ``cohomologiques'' en relation avec les théorèmes de périodicité de Bo
- CT 16/44, line 1725: In c\inserted{h}ar. zero, state some known extra features: index theorem holds, the \deleted{conjectures}\inserted{propositions} $A_{\unsure{\ell|\chi}}$ to $D_{\unsure{\ell|\chi}}$ are independant of $\unsure{\ell|\chi}$ (because of the existence of Betti cohomology, so that these \deleted{conjectures}\inserted{propositions} are equivalent to the corresponding one's for rational cohomology), \deleted{and} $A$ and $C$ are independant of the choosen polarization$_{\mathrm{x}}$ (for $A$ because it is equivalent with $B$, for $C$ because it can be expressed in terms of $A$, $C(X)=(A(X\mathrm{x}X)+A(Y\mathrm{x}Y)+\mathinner{..})$ Thus the \deleted{conjectures}\inserted{conditions} without ambigu
- CT 44/8, line 2974: Je commence à avoir de faibles lumières sur la façon de faire \inserted{d}es VA avec les cycles al\inserted{g}ébriquement équivalents à zéro d'une variété projective non singulière $X$ (sur un corps alg clos $k$). Si $X$ est connexe de dimension $n$, je sais associer à chaque entier $i$ \inserted{c}ompris entre $\unsure{0|1}$ et $n$ une VA $J^i(X)$, jouant le rôle d'une ``jacobienne intermédiaire'' au sens de Weil, correspondant à des classes de cycles de codimension $i$ (pour une relation d'équivalence que je ne sais pas bien identifier pour l'instant, mais qui mérite certainement d'être appelée ``équivalence d'Albanese''). Je suis moralement sûr que ce sont ``les bonnes'', bien que je n'ai

## totally-real: `tot.*réel|K_r`

- No matching line in CT.

## tensor: `foncteur|semi.simple|motif|motives`

- CT 16/49, line 1829: As a consequence, we see that if $x\in H^i(X)$ is such that $u(x)$ is algebraic ($i$ being now assumed to be even), then so is $x$. The same result should hold in fact if $u$ is a monomorphism, the reason being that in this case there should exist a left-inverse which is algebraic; this exists indeed in a case like $H^{n-1}(X)\to H^{n-1}(Y)$ (where we take the left inverse $\Lambda_X\phi_*$). But to get \unsure{it} in general, it seems we need moreover the Hodge index relation. (The complete yoga then being that we have the category of motives which is semi-simple !). Without speeking of motives, and staying down on earth, it would be nice to explain in the notes that $C(X)$ together with th
- CT 47/3, line 2096: définie par \deleted{l'application additive} le foncteur de catégories\\
- CT 47/3, line 2103: de foncteurs de catégories triangulées
- CT 47/5, line 2228: Plus précisément, le foncteur composé
- CT 47/5, line 2232: est \inserted{can.} isomorphe au foncteur \deleted{identique, \illegible{2}}\\
- CT 47/5, line 2262: Or le composé des foncteurs\\
