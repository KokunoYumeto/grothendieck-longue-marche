from save_page import save_page

save_page(97, r'''
\scanpage{97}
% Image orientation: upside-down typescript; archive foliation: 96.
\uline{Corollaire} 3.4. Soient $S$ un préschéma, $u:G\quad H$ un homomorphisme de \deleted{\unsure{$S$-groupes}} $S$-préschémas en groupes localement diagonalisables,\inserted{avec $H$ de type fini sur $S$} Alors:

a) $G'=\operatorname{Ker}u$ est localement diagonalisable, il est de type fini sur $S$ si $G$ l'est.

b) Le quotient $G/G'$ existe, de façon plus précise la relation d'équivalence définie par $G'$ dans $G$ est effective pour la descente fidèlement plate quasi-compacte (cf exposé IV). De plus $\unsure{G/G'}$ est localement diagonalisable.

c) \deleted{Par \unsure{suite} (\unsure{image})} L'homomorphisme $u:G\quad H$ se factorise de façon unique en
\diagram{\begin{tikzcd}[column sep=small]
G \arrow[r,phantom,"v"] & G/G' \arrow[r,phantom,"w"] & H
\end{tikzcd}}
, où $v$ est l'homomorphisme canonique (donc $v$ est fidèlement plat et quasi-compact)\deleted{\unsure{et}} De plus $w$ est une immersion fermée, et à fortiori un monomorphisme.

La première assertion de c) est conséquence de b), par définition du quotient $G/G'$. Comme toutes les assertions faites sont de nature locale sur $S$, on peut alors supposer $G$ et $H$ \deleted{\unsure{définis par}} diagonalisables, \deleted{\unsure{définis}} de la forme $D_S(M)$ et $D_S(N)$, et (compte tenu de 1.5.\inserted{qui implique $N$ de type fini} et 2.1. b)) $u$ défini par un homomorphisme $u':N\quad M$. Alors en vertu de 3.1. $G'$ est isomorphe à $D_S(\operatorname{Coker}u')$, ce qui prouve a). Pour prouver b) et c), il suffit de réaliser $G/G'$ comme $D_S(\operatorname{Im}u')$, en appliquant 3.3.

\uline{Remarques} Le résultat d'existence de quotients 3.4. sera substantiellement généralisé au N° suivant, \deleted{\unsure{ainsi que}} On notera que dans le présent N° et le précédent, l'hypothèse $S\ne\varnothing$ n'est intervenue que pour assurer la validité de certaines réciproques, \deleted{\unsure{affirmant que si $G=D_S$}} permettant de certaines hypothèses sur des schémas en groupes sur $S$, de conclure des propriétés correspondantes pour certains groupes ordinaires Les résultats en sens inverse sont valables sans restriction sur $S$, et les démonstrations données ici s'appliquent dans le cas général.
''', [
('text','top, Corollaire 3.4 hypotheses','Soient S un préschéma'),
('deletion','top, after de','S-groupes'),
('insertion','top, above end of hypotheses','avec H de type fini sur S'),
('text','upper, a)','G prime = Ker u'),
('text','upper-middle, b)','Le quotient G/G prime existe'),
('text','middle, c)','L\u0027homomorphisme u se factorise'),
('deletion','middle, beginning c)','Par suite (image)'),
('diagram','middle, inline factorization','G v G/G prime w H'),
('deletion','middle, after quasi-compact','et'),
('text','lower-middle, proof','La première assertion de c)'),
('deletion','lower-middle, after G et H','définis par'),
('deletion','lower-middle, after diagonalisables','définis'),
('insertion','lower-middle, following citation 1.5','qui implique N de type fini'),
('text','lower, Remarques','Le résultat d\u0027existence de quotients'),
('deletion','lower, following N° suivant','ainsi que'),
('deletion','lower, after réciproques','affirmant que si G=D_S')
], [
('b), final quotient','G/G prime','An extra overtyped mark appears before the prime','medium'),
('c), initial deletion','Par suite (image)','Last parenthetical word heavily overtyped','low'),
('c), deletion after quasi-compact','et','Several cancellation x strokes','low'),
('proof, deletions','définis par; définis','Overtyped, especially first phrase','medium'),
('Remarques, first deletion','ainsi que','Heavy cancellation','low'),
('Remarques, second deletion','affirmant que si G=D_S','Last symbols partly overtyped','low'),
('all homomorphism and factorization gaps','Spaces and phantom connectors retained','No visible arrow strokes in this carbon copy','high')
], [
'Cor. 3.4 includes the inserted finite-type condition on H and the corresponding finite-generation explanation for N. The alteration is material to the descent/quotient argument.',
'Remarques promises a substantial generalization of quotient existence in the following N° and distinguishes the need for nonempty S only in reverse implications.'
], sheet_kind='reused_typed')
