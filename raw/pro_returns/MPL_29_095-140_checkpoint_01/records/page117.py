from save_page import save_page

save_page(117, r'''
\scanpage{117}
% archive foliation: 116
Comportement fonctoriel des groupes d'inertie.

1. Soient $X$ un schéma, $U$ un ouvert de $X$, $G$ un groupe profini, $U'$ un revêtement principal de $U$ de groupe $G^{\deleted{\unsure{'}}}$, $x$ un point \inserted{géom.} de $X$, $\overline X$ le localisé strict de $X$ en $x$, $\overline U$ l'image inverse de $U$ dans $\overline X$, $\overline U'=U'\times_U\overline U$. On suppose donné de plus un schéma $\overline X'$ sur $\overline X$, avec des opérations de $G$ sur $\overline X'$, de telle façon que le \deleted{espace} \inserted{$\overline U$-schéma} à opérateurs $\overline X'|\overline U$ coïncide avec $\overline U'$.

Pratiquement, on sera intéressé par le cas où $x\in X-U$ et où $x$ est adhérent à $U$, où $\overline X'$ est entier sur $\overline X$ et où $\underline{\mathrm O}_{\overline X}=\overline p(\underline{\mathrm O}_{\overline X'})^G$, $\overline p:\overline X'\to\overline X$ étant la projection canonique, - de sorte que $G$ opère transitiv\deleted{\unsure{e}}ement sur l'ensemble fibre $\overline X'_{\overline x}$. De plus, on \deleted{\unsure{se placera}} sera \inserted{le plus souvent,} sous des conditions où on peut construire canoniquement $\overline X'$ en termes de $\overline U'$; par exemple, si on suppose $X$ normal en $x$, donc $\overline X^{\deleted{\unsure{'}}}$ normal, et $\overline U$ non vide, on définira $\overline X'$ comme le normalisé de $\overline U$ relativement à $\overline U'$ sur $\overline U$ (i.e. comme limite projective des \unsure{normaalisés|normalisés} dans les $\overline{U'(i)}$ sur $\overline U$, $U'$ étant écrit comme limite projective de schémas principaux $U'(i)$ sur les groupes quotients finis $G(i)$ de $G$).

Si maintenant \deleted{\unsure{$X$} est} \inserted{$\xi$} est un point de $\overline X'_{\overline x}$, on peut considérer le groupe de stabilité $G_\xi$ de $\xi$, formé des $g\in G$ tels que $g.\xi=\xi$; ce groupe prendra le nom de \uline{groupe d'inertie} \uline{relatif à} $\xi$. Dans le cas envisagé plus haut où les points de $\overline X'$ sur $\overline x$ sont tous conjugués sous $G$, on voit que pour $\xi$ variable\deleted{\unsure{s}}, les $G_\xi$ parcourent une classe de sous-groupes conjugués de $G$, qu'on appellera \inserted{(par abus de langage)} \uline{les sous-groupes d'inertie} \deleted{de} \uline{relatifs à} $x$. Noter qu'en toute rigueur cette classe de sous-groupes \deleted{d'inertie} n'est pas déterminée par la seule connaissance de $x\in X$, mais dépend du choix du prolongement de $\overline U'$ en $\overline X'$. Lorsque $X$ est normal en $x$ et que $x$ est spécialisation d'un point de $U$ (ce qui signifie que $x$ est adhérent à $U$ si $\operatorname{esp}(X)$ est localement noethérien), il sera sous-entendu, sauf mention du contraire, que le choix en question est fait par normalisation, comme expliqué plus haut.
''', [
('text','title','Comportement fonctoriel des groupes d’inertie'),
('text','handwritten paragraph number','1.'),
('text','first paragraph','Soient X un schéma, U un ouvert'),
('deletion','after G de groupe G','prime-like superscript'),
('insertion','above point de X','géom.'),
('deletion','first paragraph last line after le','espace'),
('insertion','above espace','Ū-schéma'),
('text','second paragraph','Pratiquement, on sera intéressé'),
('deletion','within transitivement','overtyped extra e'),
('deletion','second paragraph after on','se placera'),
('insertion','above sous','le plus souvent,'),
('deletion','after donc X̄ normal','prime-like superscript'),
('text','third paragraph','Si maintenant … ξ est un point'),
('deletion','after maintenant','X est'),
('insertion','after deleted X est','ξ'),
('deletion','after variable','s'),
('insertion','above les sous-groupes','(par abus de langage)'),
('deletion','after sous-groupes d’inertie','de'),
('deletion','after cette classe de sous-groupes','d’inertie'),
], [
('superscripts after G and after donc X̄','cancelled prime-like marks','heavily inked marks could be other typed accidents','low'),
('transitivity word','transitiv[deleted e]ement','x overstrike appears between v and e; original character doubtful','medium'),
('second paragraph crossed word','se placera','x-overtyping leaves only some consonants visible','low'),
('normalisation paragraph','normalisé de Ū; relatief to Ū′ sur Ū','Ū is visible where mathematical context might suggest X̄; retained as written','high'),
('normalisation plural','normaalisés','overlapping type could instead be normalisés','low'),
('third paragraph initial cancellation','X est','first symbol densely overwritten','low'),
('bar-p formula','p̄(O_X̄′)^G','no pushforward star or subscript is visible after p̄','high'),
], [
'Title-bearing typescript defines inertia as the stabilizer of a point in a chosen extension of a principal G-cover over the strict localization. It explicitly warns that the conjugacy class depends on the extension, not only on x, and stipulates normalization under normality and specialization hypotheses.',
'Potential reading question: the normalization paragraph repeatedly prints Ū rather than X̄; preserve this in the frozen transcription and later compare with neighbouring context only as a question.',
'Transitivity of G on the fibre is asserted from integrality and the invariant-ring condition, without proof on this page; identify the hypotheses needed if using the claim.',
], sheet_kind='typed')
