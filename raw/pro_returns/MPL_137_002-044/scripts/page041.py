from record_page import record
tex=r'''\scanpage{41}
% archive foliation: 40
\deleted{
$\{C$. catégorie $\{$ des $k$-modules $\frac12$ simpliciaux \deleted{\unsure{str.}}\inserted{$L_*$} qui
sont flasques et str. $\partial$-parfaits, i.e. qui satisfont
aux deux conditions équivalentes

$a)$ $L_*$ est \deleted{isomorphe}\inserted{isomorphe} à une somme directe finie
de modules $\frac12$ simpliciaux
\[
\inserted{C^i_*=\Lambda^{i+1}\Phi_{*k}\ (i\geqslant0)}
\qquad\deleted{\unsure{\Phi(i)_*=\Lambda^i\Phi_{*k}}\ (i\geqslant1)}.
\]
\margin{\unsure{On suppose les modules proj. de type fini sur $k$ libres pour $k$ principal}.}

$b)$ les $L_n$ sont libres de type fini, de rang constant
sur $\operatorname{Spec}k$, la fonction $n\longmapsto\operatorname{rg}_kL_n$ est polynomiale
pour $n$ grand, $L_*$ est flasque i.e. $\pi_i(L_*)=0$ pour $i\geqslant0$.

$A\subset C$ la sous-catégorie pleine formée des \deleted{\unsure{\Phi(i)_*}}\inserted{$C^i_*$}.

\uline{NB}. $C$ est additive (et karoubienne), $A$ n'est pas
stable par sommes finies, mais hérite une structure
$k$-linéaire. On a
\[
\operatorname{Hom}(\deleted{\unsure{\Phi}}C^i_*,\deleted{\unsure{\Phi}}C^j_*)=
\begin{cases}
0&\text{si }j\ne i,i+1\\
k&\text{si }j=i,\ \text{base }\operatorname{id}_{(C^i)}\\
k&\text{si }j=i+1,\ \text{base }d^i=T_*\wedge
\end{cases}
\]
Notons que
\deleted{\unsure{\Phi(i)_*=C^{i-1}_*\ (i\geqslant1),\qquad C^i_*=\Phi(i+1)_*\ (i\geqslant0)}}

$C^\bullet_*=(C^i_*,T_*\wedge)$ est un complexe de cochaînes dans
$A$ ou dans $C$ ou dans $\widehat\Delta_{k\text{-}lin}$ --- il jouera
le rôle du complexe de cochaînes \uline{universel}.
}

\deleted{\unsure{En effet}}
\uline{Prop. 1} Soit $B$ une catégor. \deleted{additive}\inserted{$k$-additive}. Alors
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\underline{\operatorname{Hom}}_{\unsure{add\,k|additif}}(C,B)
\arrow[r,"{\mathrm{res}}","\simeq"']&
\underline{\operatorname{Hom}}_{k\text{-}lin}(A,B)\arrow[d,"\simeq"']\\
& B^\bullet_k=\text{cat. des \inserted{complexes de} cochaînes de }B
\end{tikzcd}}
\[
F\longmapsto F(C^\bullet_*)
\]
\deleted{\uline{\unsure{Assertion}} Soit $E^\bullet\in\operatorname{Ob}B^\bullet$ un complexe de cochaînes
de $B$.}

\uline{Exemple 1} \inserted{Faisons $B=\mathrm{Ab}_k$.} Soit $L_*\in\operatorname{Ob}C$, considérons le
foncteur cov. qu'il représente
\[
C\longrightarrow\mathrm{Ab}_k:\quad M_*\longmapsto\operatorname{Hom}_C(L_*,M_*).
\]
On a ainsi un foncteur pl. fid (\unsure{nature des fonct. repr.} $\ldots$)
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
C^\circ\arrow[r,hook]&\underline{\operatorname{Hom}}_{k\text{-}lin}(C,\mathrm{Ab}_k)\arrow[dr,"\simeq"]&&\\
&&\underline{\operatorname{Hom}}_{\unsure{k\text{-}lin|add}}(A,\mathrm{Ab}_k)\arrow[r,"\simeq"]&\mathrm{Ab}^{\bullet}_{k}
\end{tikzcd}}
'''
record(41,tex,[('deletion','upper three-fifths','large diagonal cancellation through C definition and universal-complex discussion'),('text','cancelled top','C catégorie k-modules ½ simpliciaux flasques str ∂-parfaits'),('deletion','top before qui','str'),('insertion','top above deleted qualification','L*'),('text','cancelled a','somme directe finie modules ½ simpliciaux'),('deletion','a verb','isomorphe'),('insertion','a above verb','isomorphe'),('display','a inserted generators','Ci*=Λi+1 Φ*k (i≥0)'),('deletion','a old generators','Φ(i)*=Λi Φ*k (i≥1)'),('margin note','left of a','modules proj de type fini; k principal'),('text','cancelled b','L_n libres t.f.; rang constant; polynomial; flasque π_i=0'),('text','cancelled middle','A⊂C pleine formée des Ci*'),('deletion','after formée des','Φ(i)*'),('insertion','after formée des','Ci*'),('text','cancelled NB','C additive et karoubienne; A k-linéaire'),('display','cancelled Hom table','0 if j≠i,i+1; k base id; k base di=T*∧'),('deletion','Hom arguments','old Φ symbols'),('text','cancelled after table','Notons que'),('deletion','entire short formula line','Φ(i)*=Ci-1*; Ci*=Φ(i+1)*'),('text','cancelled end','C•* complexe de cochaînes universel'),('deletion','above Prop 1','En effet'),('text','Prop 1','B catégorie; Alors'),('deletion','Prop 1 adjective','additive'),('insertion','above additive','k-additive'),('diagram','Prop 1','Hom(C,B)→Hom(A,B)→B•_k equivalences'),('display','beside second equivalence','F↦F(C•*)'),('insertion','description B•_k','complexes de'),('deletion','below diagram','Assertion Soit E•∈ObB• un complexe de cochaînes de B'),('text','Exemple 1','Soit L*∈ObC; foncteur cov représenté'),('insertion','Exemple 1 above Soit','Faisons B=Ab_k'),('display','Exemple 1','C→Ab_k, M*↦Hom_C(L*,M*)'),('text','bottom','foncteur pl fid; nature des fonct repr'),('diagram','bottom','C°↪Hom(C,Ab_k)≃Hom(A,Ab_k)≃Ab_k•')],doubts=[('margin beside a','On suppose les modules proj. de type fini sur k libres pour k principal','initial k may belong to first clause; whole marginal note highly compressed','low'),('deleted generators in a','Φ(i)*=Λi Φ*k','superscript/index overwritten when Ci* was added','low'),('Hom table first arguments','Ci*, Cj* with deleted Φ','multiple overwrites; letter C visible in blue','medium'),('deleted formula below table','Φ(i)*=Ci-1* (i≥1), Ci*=Φ(i+1)* (i≥0)','index shifts inferred only tentatively from visible strokes, not silently repaired','low'),('Prop 1 first subscript','add k','additif; k-add; heavily overwritten','low'),('crossed heading before E•','Assertion','Question; cancellation obscures beginning','low'),('fully faithful parenthesis','nature des fonct. repr.','routine des fonct. repr.; middle word abbreviated and faint','low'),('last diagram final equivalence','Ab_k^bullet','possible extra subscript/decoration at page edge beneath k','low')],sheet_kind='cancelled_draft',notation=[('universal cochain complex in simplicial modules',r'$C^i_*=\Lambda^{i+1}\Phi_{*k},\ d^i=T_*\wedge$','scan 41 cancelled draft, upper/right and Hom table'),('category of cochain complexes',r'$B^\bullet_k$','scan 41 proposition')])
