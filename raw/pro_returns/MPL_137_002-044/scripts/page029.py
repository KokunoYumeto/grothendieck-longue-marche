from record_page import record
tex=r'''\scanpage{29}
% archive foliation: 28
Soit $C$ une catégorie, $A$ une sous-catégorie
\inserted{pleine.}\deleted{On} Considérons les foncteurs composés
\diagram{\begin{tikzcd}[column sep=large]
C\arrow[r,"\mathrm{can}"]\arrow[rr,bend right=22,"\rho"']&
\widehat C\arrow[r,"\mathrm{rest.}"]&
\widehat A=\underline{\operatorname{Hom}}(A^\circ,\mathrm{Ens})
\end{tikzcd}}
si \deleted{tout $\forall X\in C$} tout objet \inserted{$X$} de $C$ est
$\varinjlim$ \deleted{de}\inserted{dans $C$} un diagramme de $A$ (ce à
quoi revient au même, $X\simeq\varinjlim_{Y\in\operatorname{Ob}A_{/X}}Y$),
alors le foncteur $\rho$ est pl. fidèle.
Si $C$ est additive \inserted{(mais pas néc. $A$)}, le diagramme ci
dessus se complète en
\diagram{\begin{tikzcd}[column sep=large,row sep=huge]
C\arrow[r,"c_{ab}"]\arrow[rr,bend left=22,"\rho_{ab}"]\arrow[dr,"c"']\arrow[drr,bend right=35,"\rho"']&
\widehat C_{ab}\arrow[r,"\mathrm{rest.}\,\rho_{ab}"]\arrow[d,"\mathrm{oubli}\,\omega_C"']&
\widehat A_{ab}\arrow[d,"\mathrm{oubli}\,\omega_A"]\\
&\widehat C\arrow[r,"\mathrm{rest.}\,\rho"]&\widehat A
\end{tikzcd}}
\margin{idem pour structure $k$-lin. sur $C$}
avec $\omega_A$ fidèle, d'où il résulte
que $\rho_{ab}$ est aussi pl. fidèle.
[C'est le cas en particulier si $\forall X\in C$
est $\simeq$ somme d'objets de $\unsure{C|A}$]

Supposons de plus que tout
$X\in C$ est aussi isom. à une $\varprojlim$
\inserted{dans $C$} d'objets de $C_0$. Alors l'image essentielle
de $C$ dans $\widehat A$ (resp. $\widehat A_{ab}$)
est contenue dans la sous cat. pleine
de $\widehat A$ resp. $\widehat A_{ab}$ formée des foncteurs
'''
record(29,tex,[('text','top','Soit C une catégorie, A sous-catégorie'),('insertion','above second line','pleine.'),('deletion','before Considérons','On'),('text','top','Considérons les foncteurs composés'),('diagram','upper','C→Ĉ→Â=Hom(A°,Ens), ρ curved'),('deletion','before tout objet','tout ∀X∈C'),('insertion','above objet','X'),('text','upper-middle','si tout objet de C est lim un diagramme de A'),('deletion','after lim','de'),('insertion','above de','dans C'),('display','upper-middle parenthesis','X≃colim_Y∈ObA/X Y'),('text','middle','ρ pl fidèle; Si C additive diagramme se complète'),('insertion','after additive','mais pas néc. A'),('diagram','middle','C→Ĉ_ab→Â_ab, forgetful verticals; C→Ĉ→Â; ρ and ρ_ab'),('margin note','left middle slanting','idem pour structure k-lin sur C'),('text','lower-middle','ω_A fidèle, ρ_ab pl fidèle; cas somme d’objets'),('text','bottom','Supposons tout X isom à lim objets de C0; image essentielle'),('insertion','above d’objets','dans C')],doubts=[('top functor symbol','ρ','may be f; curved descender and loop recur in diagram','medium'),('canonical colimit indexing','Y∈Ob A_/X','small slash/arrow could denote A→X; convention preserved by slash subscript','medium'),('phrase before colimit','ce à quoi revient au même','visible wording awkward; ce qui revient au même possible','low'),('inserted additive parenthesis','mais pas néc. A','short abbreviation néc. faint','medium'),('diagram labels','c_ab, ρ_ab, oubli ω_C, oubli ω_A','ω and cursive w nearly identical; rest labels touch arrow shafts','medium'),('bracketed sufficient condition','objets de C','A possible; ink seems rounded C, not silently amended','low'),('bottom limit-source category','C_0','small circle after C read as subscript 0','medium')],notation=[('category of presheaves',r'$\widehat C,\widehat A$','scan 29; hats are visible, not tildes'),('underlined Hom for a functor category',r'$\underline{\operatorname{Hom}}(A^\circ,\mathrm{Ens})$','scan 29; underline in source retained'),('direct / inverse limit arrows',r'$\varinjlim,\varprojlim$','scan 29; directions read from ink')])
