from records.record_page import save
tex=r'''\scanpage{122}
% archive foliation: 121
$1.$ \deleted{Appelons ``opération'' (sur cartes) \unsure{toute|tout}}
\deleted{Soit $C=(X,K,S)$ une carte \inserted{orientée}}, soit $F$ un \deleted{foncteur}\inserted{foncteur} sur la catégorie des
\deleted{surfaces compactes (avec comme morphismes les morphismes de revêtement (avec ramification))}
\inserted{cartes finies orientées}.
[On suppose que si $(X,H)$ est une surface compacte avec $H$ groupe fini opérant avec ramification isolée, on a
\[
F(X/H)=F(X)^H.
\]
]
$\operatorname{Aut}(C)$ opère sur $F(X)$, donc et son sous-groupe $N(C)\inserted{=\operatorname{Aut}^\circ(C)}$ des autom. isotopes à l’identité.
\margin{On suppose que \unsure{les foncteurs} \unsure{seront tous} \unsure{contravariants}.}
Quoi, soit
\[
F^{\unsure{\natural|\sharp}}(C)=F(X)/\operatorname{Aut}^\circ(C).
\]
C’est un \deleted{foncteur}\inserted{préfaisceau} en $C$, car si
\[
C'=(X',K',S')\xrightarrow{f}(X,K,S),
\]
on a $F(X)\to F(X')$ \deleted{et $\unsure{\operatorname{Aut}(f)}\operatorname{Aut}(f)^\circ$}
en façon compatible avec $\operatorname{Aut}(f)^\circ$, donc
\[
F(X)/\operatorname{Aut}(f)^\circ\longrightarrow F(X')/\operatorname{Aut}(f)^\circ,
\]
par $\operatorname{Aut}(f)^\circ\xrightarrow{\sim}\operatorname{Aut}(X)^\circ$ d’où par composition
\[
F(X)/\operatorname{Aut}(C)^\circ\longrightarrow F(X')/\operatorname{Aut}(f)^\circ
\longrightarrow F(X')/\operatorname{Aut}(C')^\circ
\]
i.e. $F^\natural(C)\to F^\natural(C')$.
On étend $F^\natural$ en un foncteur sur la catégorie des cartes finies $C$ avec groupe fini d’autom., en posant
\[
F^\natural(C,G)=F(C)^G/\operatorname{Aut}(C,G)^\circ.
\]
Ceci dit, on se propose de trouver les sections de \deleted{\unsure{ce $F$}}
\[
F^\natural:\underset{\text{finies}}{\text{Cartes}}\ \text{à opérateurs}\ \inserted{\text{finis}}\longrightarrow\text{ens}
\]'''
save(122,tex,[('heading','top','1.'),('deleted_text','top','Appelons opération'),('deleted_text','top','Soit C=(X,K,S)'),('text','upper','soit F un foncteur'),('deleted_text','upper','surfaces compactes'),('insertion','upper','cartes finies orientées'),('text','upper middle','On suppose que'),('formula','upper middle','F(X/H)=F(X)^H'),('text','middle','Aut(C) opère'),('insertion','middle','=Aut°(C)'),('margin','left middle','On suppose que lesfoncteurs'),('formula','middle','F natural(C)'),('deleted_text','middle','foncteur'),('insertion','middle','préfaisceau'),('formula','middle','C prime toC'),('formula','middle','F(X)toF(Xprime)'),('deleted_formula','middle','Aut(f)Aut(f)°'),('text','middle','en façon compatible'),('formula','lower middle','quotients byAut(f)°'),('formula','lower middle','Aut(f)°isoAut(X)°'),('formula','lower middle','three quotientchain'),('text','lower','On étend F'),('formula','lower','F natural(C,G)'),('text','bottom','Ceci dit'),('deleted_text','bottom','ceF'),('formula','bottom','Cartes àopérateurs toens')],doubts=[('left margin','les foncteurs seront tous contravariants','rapid cursive; phrase remains tentative after enlarged inspection','low'),('middle before soit','Quoi','Puis; short cursive word','low'),('superscript onF','natural','sharp; angular handwritten mark','medium'),('quotient isomorphism','Aut(X)°','Aut(C)° would be plausible but glyphlooksX','medium'),('deleted formula','Aut(f)Aut(f)°','first groupname overwritten','low')],notation=[('F with angular superscript','F^\\natural','provisional reading of recurring superscript; to compare subsequent sheets'),('N(C), Aut°(C)','N(C),\\operatorname{Aut}^\\circ(C)','above-line identification of isotopy subgroup'),('K','K','middle member of triple C=(X,K,S)')],abbreviations=[('autom.','automorphismes'),('ens','ensembles')],leads='Draft quotient construction F-natural(C)=F(X)/Aut°(C); descent invariant under finiteH with isolated ramification; Aut(f)°→Aut(X)° asserted iso; contravariant functoriality and equivariant extension F-natural(C,G)=F(C)^G/Aut(C,G)°. Goal find sections. Surface-category wording withdrawn and finite-oriented-map category inserted. Margin about contravariance remains lowconfidence.')
