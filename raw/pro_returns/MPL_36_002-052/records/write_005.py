from save_page import save
tex=r'''
\scanpage{5}
\mspage{3}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {3};\draw (0,0) ellipse (0.23 and 0.28);\end{tikzpicture}}
\uline{pg23}\quad On peut dire plus simplement que ${}_nK$ est étale séparé car ${}_nK=\operatorname{Ker}({}_nG\longrightarrow{}_nH)$. En a), ne dirais-tu pas que ${}_nK_{\bar s}$ est isomorphe à un sous-groupe de ${}_nK_{\bar t}$.

\uline{pg24}\quad a) $\ell\,15$ :\quad
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=2pt] (t) {$\dim$};\draw (0,0) ellipse (0.43 and 0.28);\end{tikzpicture}}
$\operatorname{Ker}(u_{\unsure{s|\eta}})=0$\quad ?

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {\uline{pg28}};\draw[rotate=20] (0,0) ellipse (0.65 and 0.72);\end{tikzpicture}}
Les notions introduites dans 3.5 ont elles été définies pour $S$ non hensélien ? (il faudrait au moins choisir un groupe d'inertie).
\inserted{[itou pour 3.7]}

\uline{pg29}\quad $\ell-2$\quad la terminologie ``clôture normale'' est-elle encore canonique ?

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {4};\draw (0,0) ellipse (0.22 and 0.26);\end{tikzpicture}}
\uline{p32}\quad $\ell\,8$\quad ne dépend
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=2pt] (t) {pas};\draw (0,0) ellipse (0.28 and 0.27);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {\uline{pg33 ss}};\node at (-1.05,-0.18) {?};\draw[rotate=12] (-0.28,-0.15) ellipse (1.08 and 0.62);\end{tikzpicture}}
(4.2)\quad Ne donnerais tu pas un énoncé style ``voisinage tubulaire'' compréhensible. La vérité est

\deleted{\unsure{a)}} on a un morphisme de topos $\operatorname{Spec}(K)_{\mathrm{et}}\xrightarrow{\varphi}\operatorname{Spec}(k)_{\mathrm{et}}$ (``\unsure{ext.|ent.} du corps résiduel'') et $A_0^0$ est un schéma relatif sur $(\operatorname{Spec}(K))_{\mathrm{et}}$ annelé par $\varphi^*\mathcal O$ [le $\varphi^*$ des faisceaux d'ensembles]. Même chose d'ailleurs pour
\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) at (0,0) {\unsure{liss}};\draw[->] (-0.2,-0.15)--(0.25,-0.15);\node at (0,-0.42) {\unsure{ramifier}.};\end{tikzpicture}}
$A_0$

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {\uline{pg36}};\node at (-0.85,-0.22) {\unsure{si} ?};\draw[rotate=22] (-0.27,-0.10) ellipse (1.05 and 0.45);\end{tikzpicture}}
$\ell-6$.\quad ``ce n'est pas la trace qui est \unsure{contragrédiente}; l'énoncé primitif était correct.

\uline{pg40}\quad (4.5.4)\quad Qu'est-il écrit dans la marge ?

$\ell-1$\quad Quel est loc cit. ?

$\ell\,3$\quad $\ell$-groupe signifie-t-il tué par $\ell$, ou par un $\ell^{\unsure{n}}$ ?

Le trait est-il strictement local ? ce serait plus agréable.

\margin{4}
'''
e=[('text','upper right','3'),('drawing','top left section marker','circled 3'),('text','top pg23','On peut dire plus simplement'),('display','within pg23','nK = Ker(nG -> nH)'),('text','upper pg24 a l15','dim Ker(u_s)=0 ?'),('drawing','upper pg24','dim circled'),('drawing','middle left reference','pg28 circled'),('text','middle pg28','Les notions introduites dans 3.5'),('insertion','under pg28 note','[itou pour 3.7]'),('text','middle pg29 l-2','la terminologie clôture normale'),('drawing','middle separator','three parallel horizontal strokes'),('drawing','lower section marker','circled 4'),('text','lower p32 l8','ne dépend pas'),('drawing','p32 l8','pas circled'),('drawing','lower pg33 reference','pg33 ss and ? inside oval'),('text','lower (4.2)','Ne donnerais tu pas un énoncé'),('deletion','before on a','a) uncertain'),('text','lower paragraph','on a un morphisme de topos'),('display','within lower paragraph','Spec(K)_et -> Spec(k)_et'),('drawing','left of A_0, below paragraph','liss; right arrow; ramifier'),('text','end of lower paragraph','A_0'),('drawing','lower pg36 reference','pg36 and si? inside oval'),('text','pg36 l-6','ce n’est pas la trace'),('text','bottom pg40 (4.5.4)','Qu’est-il écrit dans la marge ?'),('text','bottom l-1','Quel est loc cit. ?'),('text','bottom l3','ell-groupe signifie-t-il'),('text','bottom last line','Le trait est-il strictement local ?'),('margin note','bottom left pencil','4')]
d=[{'line':'pg24 a), l15','reading':'u_s','alternatives':'u_eta','confidence':'low'},{'line':'(4.2), beginning of paragraph','reading':'deleted a)','alternatives':'small heavily cancelled fragment','confidence':'low'},{'line':'(4.2), parenthesis','reading':'ext.','alternatives':'ent.','confidence':'medium'},{'line':'(4.2), last line annotation','reading':'liss; ramifier','alternatives':'abbreviated first word; function of arrow uncertain','confidence':'low'},{'line':'pg36, pencil margin','reading':'si ?','alternatives':'first token faint','confidence':'medium'},{'line':'pg36, l-6','reading':'contragrédiente','alternatives':'compressed middle letters','confidence':'medium'},{'line':'pg40, l3','reading':'ell^n','alternatives':'superscript resembles h','confidence':'medium'}]
save(5,tex,e,d,'Questions: is nK etale separated simply as kernel of nG -> nH; specialization as subgroup; dim Ker(u_s)=0?; definitions in 3.5 and 3.7 for nonhenselian S require inertia-group choice. Request for a comprehensible “voisinage tubulaire” formulation, followed by topos/ringed-topos description of A_0^0 and A_0. Note on trace and contragredience: blue sentence says original statement correct; pencil “si?” possibly challenges it. Distinguish ell-torsion from ell-power torsion and strict locality. No context consulted.')
