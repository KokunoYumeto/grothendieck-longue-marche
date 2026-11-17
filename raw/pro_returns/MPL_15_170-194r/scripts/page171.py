from record_page import record

record(171, r'''\scanpage{171}

SYSTÈMES de RACINES (20)\hfill Tribu n\textsuperscript{o} 59

de signe $+1$.

1) On pose $E=Q/3P$. C'est un $\underline{F}_3$-espace vectoriel de dimension 5. Montrer que le produit $(x,y)$ définit sur $E$ une forme bil. sym. non dégénérée. Montrer que deux éléments distincts de $R$ ont des images distinctes dans $E$.

2) On note $O(E)$ le groupe orthogonal de $E$, muni de la forme bil. précédente. On a $O(E)=\{\pm1\}\times SO(E)$. La norme spinorielle définit un homomorphisme surjectif $SO(E)\longrightarrow\{\pm1\}$ dont le noyau est noté $SO^+(E)$. Le groupe $SO^+(E)$ est simple, (d'ordre $25\ 920$) ; le quotient $O(E)/SO^+(E)$ est de type $(2,2)$. En déduire que $O(E)$ contient un sous-groupe $\Omega(E)$ d'indice 2 distinct de $SO(E)$ et ne contenant pas $-1$ ; montrer que ce sous-groupe est unique.

3) Tout élément de $\operatorname{Aut}(R)$ définit par passage au quotient un élément de $O(E)$. Montrer, (en comparant les ordres), que l'on obtient ainsi un isomorphisme de $\operatorname{Aut}(R)$ sur $O(E)$ ; l'image de $W(R)$ par cet isomorphisme est $\Omega(E)$, celle de $W^+(R)$ est $SO^+(E)$.

(Ainsi, $W(R)$ est extension d'un groupe à deux éléments par le groupe simple d'ordre $25\ 920$).

F) Groupe de Weyl $W$ de $E_7$.

Soient $Q$ le réseau radiciel, $P$ celui des poids. On a $2P\subset Q$. Posons $E=Q/2P$. La forme bilinéaire $(x\ y)$ définit, par passage au quotient, une forme bilinéaire sur le $\underline{F}_2$-espace vectoriel $E$, (noter que $(Q\mid 2P)\subset 2Z$). Montrer que cette forme est non dégénérée et alternée, (noter que $\dim(E)=6$). En déduire un homomorphisme $W\longrightarrow\operatorname{Sp}(E)=\operatorname{Sp}(3,\underline{F}_2)$.

Montrer que la suite
\diagram{\[
\text{(s)}\qquad
\begin{tikzcd}[column sep=large]
1 \arrow[r] & (1,-1) \arrow[r] & W \arrow[r] & \operatorname{Sp}(3,\underline{F}_2) \arrow[r] & 1
\end{tikzcd}
\]}
est exacte, (on peut utiliser le fait que $\operatorname{Sp}(3,\underline{F}_2)$ est d'ordre $2^9.3^4.5.7$ ; cf. Alg. IX).

Montrer que le sous-groupe $W^+$ formé des éléments de déterminant 1 de $W$ se projette isomorphiquement sur $\operatorname{Sp}(3,\underline{F}_2)$, (noter que ce sous-groupe ne contient pas $-1$).

Donner une seconde démonstration de (s) en utilisant la structure de $W(E_8)$ et l'isomorphisme $\operatorname{Sp}(3,\underline{F}_2)\longrightarrow\underline{O}(7,\underline{F}_2)$.

\margin{170}
''', [
('text','header left','SYSTÈMES de RACINES (20)'),
('text','header right','Tribu n° 59'),
('text','opening continuation','de signe +1.'),
('text','paragraph 1','On pose E = Q/3P'),
('text','paragraph 2','On note O(E)'),
('text','paragraph 3','Tout élément de Aut(R)'),
('text','parenthesis after 3','Ainsi, W(R) est extension'),
('text','section heading','F) Groupe de Weyl W de E7'),
('text','section F first paragraph','Soient Q le réseau radiciel'),
('text','sequence introduction','Montrer que la suite'),
('diagram','display (s)','1 → (1,-1) → W → Sp(3,F2) → 1'),
('text','after display','est exacte'),
('text','penultimate paragraph','Montrer que le sous-groupe W+'),
('text','last paragraph','Donner une seconde démonstration'),
('margin note','bottom left pencil','170')
], sheet_kind='reused_typed', observations='''Whole image and both halves read directly. Unrelated typed root-system exercise sheet, headed SYSTÈMES de RACINES (20), Tribu n° 59; marked reused_typed. Typed F symbols have a short underbar; the last O also has an explicit underbar. The parenthesized kernel in (s) is (1,-1), not braces. The paired scalar product in the E7 paragraph has a space between x and y, without an evident comma or vertical stroke; the later (Q|2P) does have a vertical stroke. The printed order has raised 9 and 4. Bottom pencil 170 is retained separately. All prose and mathematics reread against the halves.''')
