import sys
sys.path.insert(0,'/workspace/scratch/74077fe5e995/MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{43}
Avec les conditions de la proposition \unsure{générale}, soit $G'\subset G$, et soit $A'=B^{G'}$, $A\subset A'\subset B$. Conditions équivalentes
\[
a)\ \operatorname{Tr}_{G/G'}A'=A\qquad(\operatorname{Tr}_{G/G'}=\text{transfert})
\]
\[
a')\ \operatorname{Tr}_{G/G'}A'\ni1
\]
$b)$ Pour tout $(G,B)$-module $M$,
\diagram{\begin{tikzcd}[column sep=large]
\widehat H(G',M)^G\arrow[r,"{\deleted{\unsure{t(G',G)}}\inserted{t(G,G')}}"]&\widehat H(G,M)^{\deleted{\unsure{G}}}
\end{tikzcd}}
est \deleted{\unsure{bijectif|injectif}} \inserted{bijectif}

$b')$ \deleted{$\unsure{\widehat H(G)}$}
\diagram{\begin{tikzcd}\widehat H(G',M)\arrow[r]&\widehat H(G,M)\end{tikzcd}}
\deleted{bijectif} \inserted{surjectif}

$b(q))$

$b'(q)$
\figure{\begin{tikzpicture}[x=.5cm,y=.5cm]\draw (0,8)--(-.25,8)--(-.15,0)--(.25,0);\draw[->] (.55,1.1)--(-1.15,-.65);\end{tikzpicture}}

$a)\Leftrightarrow a'$ trivialement. $a)\Rightarrow b)$ car on a encore
\[
t(G,G')\varphi(b)=\varphi(t(G,G')b)
\]
pour $b\in A'$, d'où si $t(G,G')b=1$, $t(G,G')\varphi(b)=1$, d'où $b)$ d'après un lemme précédent
\diagram{\begin{tikzcd}
b\arrow[r,Rightarrow]\arrow[d,Rightarrow]&b'\arrow[d,Rightarrow]\\
b(q)\arrow[r,Rightarrow]&b'(q)
\end{tikzcd}}
De plus on voit toujours de la $=$ façon que $b'(q)\Rightarrow b'(q+1)$ et $b'(q)\Rightarrow b'(q-1)$, donc $b'(q)\Leftrightarrow b'(0)$. Appliquons $b'(0)$ à $M=B$, on trouve que
\[
\deleted{\unsure{\widehat H}}\quad A/\operatorname{Tr}_G B\longleftarrow(A'/\operatorname{Tr}_{G'}B)^{\deleted{\unsure{G}}}
\]
est surjectif, i.e. que l'on a
\[
1\in\operatorname{Tr}_G B+\operatorname{Tr}_{G/G'}A'=\operatorname{Tr}_{G/G'}A'
\]

\margin{\unsure{On voit l'intérêt} \unsure{énoncé} en prenant $G'=G_i$, mais aussi pour $G'$ un sous-groupe de Sylow $H$ pour $p$, où $p$ est la \uline{caractéristique} de $k$. On est donc \unsure{ramené} à établir \unsure{dans d'autres} \unsure{termes} $(O'^H/\operatorname{Tr}_H O')^G$, \deleted{\unsure{$\Leftarrow$}} : \unsure{déterminer} \unsure{un} $O'^H/\operatorname{Tr}_H O'$ par une \unsure{$G/H$-covariance}.}

\uline{\unsure{Reste} à prouver} Soient $G'\subset G$ ($G$ fini) soit $M$ un $G$-module, si $1\in\operatorname{Hom}_Z(M,M)$ est du type
\[
1=\operatorname{Tr}_{G/G'}\varphi\quad\deleted{\unsure{\text{avec}}}\quad(\varphi\in\operatorname{Hom}_{G'}(M,M))
\]
alors
\diagram{\begin{tikzcd}[column sep=large]
\operatorname{Tr}_{G/G'}&\widehat H_{\deleted{\unsure{G}}}(G',M)\arrow[r]&\widehat H(G,M)&\text{est surjective}\\
\unsure{\operatorname{Tr}'_{G'/G}|\operatorname{Rr}'_{G'/G}}&\widehat H(G',M)&\widehat H(G,M)\arrow[l]&\text{est injection},
\end{tikzcd}}
l'image de \deleted{\unsure{ce}} dernier hom est l'ens des éléments de $\widehat H(G',M)$ qui sont ``stables'', noté $\widehat H(G',M)^G$.

(Ceci contient le th. sur les groupes de Sylow, \deleted{\unsure{abéliens}} --- passant dans la catégorie des groupes abéliens \inserted{mod} les groupes de torsion où $p$ est inversible.
\figure{\begin{tikzpicture}[x=.5cm,y=.5cm]\draw (0,8)--(0,0)--(12,0);\draw (-.17,7.9)--(-.15,2.7);\draw[->] (2.5,5.9)--(-1.8,3.4);\draw (-3,3.3) .. controls (-3.2,4) and (-2.8,4.1) .. (-2.1,4) .. controls (-1.3,3.8) and (-1.1,4.3) .. (-.75,3.9) .. controls (-.4,3.6) and (-.7,3.2) .. (-.3,3.1) .. controls (.2,2.7) and (-.1,2.2) .. (.4,2.1) .. controls (.6,1.8) and (.5,1.6) .. (.8,1.5) .. controls (.4,1.2) and (.7,.3) .. (1,0);\end{tikzpicture}}
\margin{Le \unsure{coimage} du premier est $\widehat H(G',M)_G$, i.e. le quotient de $\widehat H(G',M)$ \unsure{par les relations} \deleted{\unsure{imposées par} \illegible{2}}}

\unsure{Une explication par les} \unsure{coefficients}
\[
\deleted{\unsure{\operatorname{Tr}_{G/G'}}}\sum_g\left\{\operatorname{Tr}_{\unsure{G'/G'\cap G'^g}}\right\}\deleted{\unsure{\varphi}}g\left\{\operatorname{Tr}_{\unsure{G'^g/G'\cap G'^g}}\right\}
\]
\margin{42}
'''
elements=[('text','top','Avec les conditions de la proposition générale'),('display','top inline','G′⊂G; A′=B^G′; A⊂A′⊂B'),('text','top','Conditions équivalentes'),('display','upper','a) Tr_G/G′ A′=A (Tr=transfert)'),('display','upper','a′) Tr_G/G′ A′∋1'),('text','upper','b) Pour tout (G,B)-module M'),('diagram','upper right','Hhat(G′,M)^G→Hhat(G,M)'),('deletion','above upper map','t(G′,G)'),('insertion','above upper map','t(G,G′)'),('deletion','upper target superscript','G'),('text','upper right','est'),('deletion','upper right','bijectif|injectif'),('insertion','upper right','bijectif'),('text','upper','b′)'),('deletion','under b′ source','Hhat(G)'),('diagram','upper right second map','Hhat(G′,M)→Hhat(G,M)'),('deletion','second map right','bijectif'),('insertion','second map right','surjectif'),('text','upper blank rows','b(q))'),('text','upper blank rows','b′(q)'),('drawing','upper left','vertical bracket and arrow to margin'),('text','middle','a)⇔a′ trivialement'),('display','middle','t(G,G′)φ(b)=φ(t(G,G′)b)'),('text','middle','pour b∈A′, d’où si'),('display','middle inline','t(G,G′)b=1; t(G,G′)φ(b)=1'),('text','middle','d’où b) d’après un lemme précédent'),('diagram','middle right','b⇒b′; b(q)⇒b′(q); downward implications'),('text','middle','De plus on voit toujours'),('display','middle inline','b′(q)⇒b′(q+1); b′(q)⇒b′(q-1)'),('display','middle inline','b′(q)⇔b′(0)'),('text','middle','Appliquons b′(0) à M=B'),('deletion','before quotient map','Hhat'),('display','middle','A/Tr_G B←(A′/Tr_G′ B)'),('deletion','quotient superscript','G'),('text','middle','est surjectif, i.e. que l’on a'),('display','middle','1∈Tr_G B+Tr_G/G′ A′=Tr_G/G′ A′'),('margin note','left diagonal','On voit l’intérêt; G′=G_i; sous-groupe de Sylow H'),('display','within left margin','(O′^H/Tr_H O′)^G'),('deletion','left margin','⇐'),('display','within left margin','O′^H/Tr_H O′'),('text','lower','Reste à prouver'),('text','lower','Soient G′⊂G (G fini) soit M'),('display','lower inline','1∈Hom_Z(M,M)'),('display','lower','1=Tr_G/G′ φ; φ∈Hom_G′(M,M)'),('deletion','after φ','avec'),('text','lower','alors'),('diagram','lower','Tr_G/G′; Hhat(G′,M)→Hhat(G,M) est surjective'),('deletion','lower first Hhat index','G'),('diagram','lower','Tr′_G′/G; Hhat(G′,M)←Hhat(G,M) est injection'),('text','lower','l’image de dernier hom est l’ens'),('deletion','before dernier','ce'),('display','lower inline','Hhat(G′,M); Hhat(G′,M)^G'),('text','lower','Ceci contient le th. sur les groupes de Sylow'),('deletion','after Sylow','abéliens'),('insertion','after groupes abéliens','mod'),('text','bottom','les groupes de torsion où p est inversible'),('drawing','lower left and bottom','double boundary, arrow, scalloped marginal enclosure'),('margin note','bottom left enclosure','Le coimage du premier est'),('display','bottom left enclosure','Hhat(G′,M)_G'),('text','bottom left enclosure','i.e. le quotient de Hhat(G′,M)'),('deletion','bottom left enclosure','imposées par; two unreadable words'),('text','bottom edge','Une explication par les coefficients'),('display','bottom edge','sum_g {Tr_G′/G′∩G′^g} g {Tr_G′^g/G′∩G′^g}'),('deletion','before bottom sum','Tr_G/G′'),('deletion','bottom product','φ'),('margin note','bottom right','42')]
save(43,text,elements,observations='Whole and both halves personally read. Large crops were split into smaller crops when an image-output limit prevented viewing; every split was then viewed. The diagonal margin and the scalloped lower-left note were additionally rotated/enlarged; both remain low confidence, as do the bottom-edge sentence and cancelled labels. Two words under the heavy bottom-left cancellation remain physically unrecoverable after enlargement. Top source superscript G remains live; target superscript G is cancelled. The lower restriction label is overwritten and preserved as an explicit alternative. The logical square and all boundary/callout strokes are included; no missing contents were supplied for the two bare condition labels.')
