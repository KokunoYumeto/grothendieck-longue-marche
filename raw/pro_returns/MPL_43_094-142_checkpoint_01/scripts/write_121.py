from page_work import save_page
text=r'''\scanpage{121}
\mspage{III-42}
En outre, on sait que $H^i(X,\underline F)=0$ sauf pour un nombre fini de valeurs de $i$ (\uline{loc.cit.}) ; le nombre entier
\[
(15)\qquad\chi_A(\underline F)=\sum_{i=0}^{\infty}(-1)^i\operatorname{Long}(H^i(X,\underline F))
\]
est donc défini pour tout $\underline O_X$-module cohérent $\underline F$ ; on l'appelle la \uline{caractéristique d'Euler-Poincaré de $\underline F$} (\uline{par rapport à l'anneau A}).
\margin{si $A$ est local}
\figure{\begin{tikzpicture}[x=.6cm,y=.6cm]\draw(0,0)--(.1,1.5);\draw(.1,1.5)circle(.08);\draw(5,0)--(5.5,1.4);\draw(5.5,1.4)circle(.08);\end{tikzpicture}}
Pour $\underline F=\underline O_X$, on dit que $\chi_A(\underline O_X)$ est le \uline{genre} \deleted{\illegible{1}} \uline{arithmétique} de $X$.

\uline{Proposition 13 .- Soit} $0\to\underline{F'}\to\underline F\to\underline{F''}\to0$ \uline{une suite exacte de $\underline O_X$-modules cohérents. On a alors}
\[
(16)\qquad\chi_A(\underline F)=\chi_A(\underline{F'})+\chi_A(\underline{F''}).
\]
On a en effet, par la suite exacte de cohomologie, une suite \unsure{exacte}
\[
\begin{gathered}
0\to H^0(X,\underline{F'})\to H^0(X,\underline F)\to H^0(X,\underline{F''})\to H^1(X,\underline{F'})\to\cdots\\
\to H^r(X,\underline{F'})\to H^r(X,\underline F)\to H^r(X,\underline{F''})\to0
\end{gathered}
\]
\deleted{\illegible{1}} les modules de cohomologie d'indice $>r$ étant nuls pour $\underline F$, $\underline{F'}$ et $\underline{F''}$. Or on sait que dans une suite exacte de modules de longueur finie, ayant des 0 aux deux extrémités, la somme alternée des longueurs est nulle ; appliquant ce résultat, on trouve immédiatement (16).

\uline{Théorème 2 .-} \inserted{\uline{Soit $\underline F$ un $\underline O_X$-module cohérent}.}
(i) \deleted{\illegible{3}} \uline{La fonction} $n\to\chi_A(\underline F(n))$ \uline{est \inserted{égale à} un polynôme \inserted{en $n$}.}

(ii) \uline{Pour n assez grand, on a} $\chi_A(\underline F(n))=\operatorname{Long}\Gamma(X,\underline F(n))$ ; \uline{si} $\underline F=\widetilde M$, \deleted{\illegible{2}} (\uline{où M est un S-module gradué de type fini}), \uline{on a} $\chi_A(\underline F(n))=\operatorname{Long}(M_n)$ \uline{pour n assez grand}.

(iii) \uline{Le terme de plus haut degré de} $\chi_A(\underline F(n))$ \uline{a un coefficient} $\geq0$.
\margin{$>$}

(iv) \uline{Le degré de} $\chi_A(\underline F(n))$ \uline{est égale à la dimension du support de $\underline F$}.

Soient \deleted{$\unsure{z}$} $\xi_1,\ldots,\xi_m$ les points de $Z=\operatorname{Spec}(A)$ ; on sait que \deleted{$\unsure{Z}$} $Z$ est somme des schémas $Z_i=\operatorname{Spec}(A_i)$, \deleted{\unsure{et}} où \deleted{\unsure{les}} les $A_i$ sont les composants locaux de $A$, et l'espace de base de $Z_i$ est $\{\xi_i\}$ (I,4,1,prop.4) ; si $f:X\to Z$ est le morphisme structural, $X$ est alors somme des présché-
\margin{Joube}
\figure{\begin{tikzpicture}\draw(0,0)--(.1,2.7);\end{tikzpicture}}
\mspage{120}
'''
save_page(121,text,[('text','top internal page number','III-42'),('text','upper paragraph','En outre on sait que Hi(X,F)=0 sauf pour un nombre fini'),('display','upper numbered equation 15','chiA(F)=sum i=0 infinity (-1)i Long(Hi(X,F))'),('text','upper definition','est donc défini pour tout OX-module cohérent F'),('margin note','upper left beside definition','si A est local'),('drawing','upper marginal reference marks','two stems ending in small circles'),('text','upper genus definition','Pour F=OX on dit que chiA(OX) est le genre arithmétique de X'),('deletion','upper genus definition','one blacked-out word'),('text','middle proposition13','Soit 0→Fprime→F→Fsecond→0 une suite exacte'),('display','middle numbered equation16','chiA(F)=chiA(Fprime)+chiA(Fsecond)'),('text','middle proof opening','On a en effet par la suite exacte de cohomologie'),('display','middle cohomology sequence','0→H0(X,Fprime)→H0(X,F)→H0(X,Fsecond)→H1(X,Fprime)→...→Hr...→0'),('deletion','middle proof before les modules','one blacked-out word'),('text','middle proof continuation','les modules de cohomologie d’indice >r étant nuls'),('text','lower theorem2','Théorème2 (i) La fonction n→chiA(F(n))'),('insertion','above theorem2 item i','Soit F un OX-module cohérent'),('deletion','theorem2 item i after number','three blacked-out words'),('insertion','theorem2 item i above est un','égale à'),('insertion','theorem2 item i after polynôme','en n'),('text','lower item ii','Pour n assez grand on a chiA(F(n))=Long Gamma(X,F(n))'),('deletion','lower item ii before où M','two blacked-out words'),('text','lower item iii','Le terme de plus haut degré a un coefficient ≥0'),('margin note','left of item iii','>'),('text','lower item iv','Le degré est égale à la dimension du support de F'),('text','bottom paragraph','Soient xi1...xim les points de Z=Spec(A)'),('deletion','bottom after Soient','z'),('deletion','bottom before Z est','Z'),('deletion','bottom before où','et'),('deletion','bottom after où','les'),('margin note','bottom left slanted','Joube'),('drawing','bottom left','vertical marginal line'),('text','bottom page number','120')],sheet_kind='reused_typed',observations='Whole and both halves read; all four heavily blacked-out word groups inspected in enlarged crops before using illegible. Math underlines in yellow are retained. Handwritten additions égale à and en n are placed at their carets. The inserted hypothesis is attached to Théorème 2 before (i) by its curved placement mark. Printed agreement est égale and the physical ending présché- are retained. Bottom short marginal word is transcribed as visible Joube; final audit to recheck its last letter.')
