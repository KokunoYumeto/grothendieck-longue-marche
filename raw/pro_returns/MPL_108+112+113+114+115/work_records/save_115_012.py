from record import save_page
tex=r'''\scanpage{12}
\mspage{6}
% archive foliation: 11
\uline{NB} $\widetilde{A^\circ}\simeq\widetilde A^\circ$ canonique

$\varphi^{\circ\unsure{\sharp|\natural}}$ s'identifie à $(\varphi^{\unsure{\sharp|\natural}})^\circ$

\margin{Cas où $\varphi^{\unsure{\sharp|\natural}}$ est pl. fidèle ?
Il suffit que $f$ soit strict. génér. ou fon. cogénérateur.}

Cas \diagram{\begin{tikzcd}A\arrow[r,"\varphi=h_A"]&\widehat A\end{tikzcd}}
\deleted{$\unsure F$}
\[
\varphi^{\unsure{\sharp|\natural}}_{\deleted{\unsure a}}(F)_*=F
\qquad
\underbrace{\varphi^{\unsure{\sharp|\natural}}(F)^*}_{F^{\unsure{\sharp|\natural}}}(a)=\mathrm{Hom}(F,a)
\]
\margin{$\varphi^{\unsure{\sharp|\natural}}$ fidèle}
\diagram{\begin{tikzcd}[column sep=large]
F\arrow[d,"\varphi_*"']&F^{\unsure{\sharp|\natural}}\\
\unsure{F'|G}&\unsure{F'|G}^{\unsure{\sharp|\natural}}\arrow[u,"\varphi^*"']
\end{tikzcd}}
\inserted{$(\stackrel{?}{=}\varphi_*^{\unsure{\sharp|\natural}})$}
\figure{\begin{tikzpicture}\draw[->,double](.4,.4)--(0,0);\end{tikzpicture}}
tels que $u\in F(a)$, $u'\in\unsure{F'|G}^{\unsure{\sharp|\natural}}(b)$ implique
(i.e. $a\longrightarrow F\quad\unsure{F'|G}\longrightarrow b$)
\margin{\deleted{$\unsure\varphi$}\diagram{\begin{tikzcd}A\arrow[r,bend right]&e\arrow[l,bend right]\end{tikzcd}}}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
a\arrow[dr,"u"']\arrow[drr,bend left=18,"u'=\varphi_*(u)\deleted{\unsure{\varphi^*}}=\varphi\circ u"]&&\\
&F\arrow[r,"\varphi_*"]\arrow[dl,"v"']&G\arrow[dll,bend left=15,"v'"']\\
b&&
\end{tikzcd}}
\margin{\deleted{$\unsure{v'\varphi_*}$}\figure{\begin{tikzpicture}\draw[->,double](.45,.3)--(0,0);\end{tikzpicture}}}
\margin{comm.\quad comm ?}
\[
v=v'\circ\varphi_*\ ?
\]
On sait que $v\circ u=v'\circ u'=v'(\varphi_*u)=(v'\varphi_*)u$

\uline{Considérons} alors la \deleted{image essentielle} sous catégorie pleine de
$\unsure{\widetilde{\widetilde A}|\widetilde A}$
\deleted{\unsure{réciproquement}}
\deleted{formée des}
\inserted{dont l'un des objets est}
\unsure{la réunion} des \unsure{images} essentielles de
\[
F\qquad G
\]
\figure{\begin{tikzpicture}\draw(0,0)--(0,.2);\end{tikzpicture}}
\diagram{\begin{tikzcd}
\Psi_1^\circ\arrow[r,no head]&a\arrow[r]&\Phi\arrow[r]&\Psi_2^\circ
\end{tikzcd}}
\diagram{\begin{tikzcd}[row sep=small,column sep=small]
\Phi_1\arrow[r]\arrow[d,equal]&\Psi\arrow[rr,no head]\arrow[d,equal]\arrow[dr]&&\Phi_2\\
\underset{i}{\lim}\,a_i&\cdot&a\arrow[ur]&
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw(0,0)..controls(2,-.1)and(3,-.1)..(3.5,.3)..controls(4,1)and(4.5,2.6)..(5.3,3.3)..controls(5.8,3.8)and(7,3.7)..(8,3.8);\end{tikzpicture}}
\[
\widetilde A\subset
\]
\diagram{\begin{tikzcd}[row sep=small,column sep=large]
F,&G\\
\widehat A\arrow[u]&A^\vee\arrow[u]
\end{tikzcd}}
ou bien \deleted{$\unsure{G=}$}
\[
(F,G,\alpha)\simeq(F,F^{\unsure{\sharp|\natural}},\alpha_F)
\]
\[
(F,G,\alpha)\simeq(G^b,G,\alpha^G)
\]
\diagram{\begin{tikzcd}a\arrow[r]&F\arrow[l,bend left=25]\end{tikzcd}}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
A\arrow[d,"f"']&\widetilde A&\widehat A\\
B&\widetilde B\arrow[u,"\widetilde f"']&\widehat B\arrow[u,"f^*"']
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw(0,0)--(.8,2);\end{tikzpicture}}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\widehat A\arrow[d,"f_!"']&A\arrow[d,"f"']&A^\vee\arrow[d,"f^\circ_!"]&A^\vee\\
\widehat B&B&B^\vee&B^\vee\arrow[u,"f^{\circ *}"]
\end{tikzcd}}
\diagram{\begin{tikzpicture}
\node at (0,0){\begin{tikzcd}[row sep=large,column sep=large]
\widehat A\arrow[r,hook]&\widetilde A\arrow[d,"\widetilde f"]&A^{\vee\circ}\arrow[l,hook']\\
\widehat B\arrow[u,"f^*"']\arrow[r,hook]&\widetilde B&B^{\vee\circ}\arrow[l,hook']\arrow[u,"f^{\circ *\circ}"]
\end{tikzcd}};
\draw(0,0) ellipse(4.4cm and 2.3cm);
\end{tikzpicture}}
'''
el=[('text','top NB','Atilde opposite canonical'),('display','top next','phi°sharp identified with (phisharp)°'),('margin note','top right','Cas où phisharp est pl. fidèle ? strict. génér. ou fon. cogénérateur'),('diagram','upper left Cas','A → phi=h_A Ahat'),('deletion','below Ahat','F'),('display','upper','phisharp(F)_*=F'),('display','upper next','phisharp(F)*(a)=Hom(F,a); Fsharp'),('deletion','phisharp subscript','a'),('margin note','upper right','phisharp fidèle'),('diagram','upper middle','F→F′; F′sharp→Fsharp'),('insertion','upper diagram arrow label','?=phi_*sharp'),('drawing','upper diagram right','short double arrow'),('text','middle','tels que u∈F(a), u′∈F′sharp(b) implique'),('display','middle parenthesis','i.e. a→F, F′→b'),('margin note','left middle','cancelled phi; A⇄e'),('diagram','middle','a→F→G→b and two diagonal arrows'),('deletion','middle upper arrow label','phi*'),('deletion','left of middle diagram','v′phi_*'),('drawing','left of middle diagram','double arrow'),('margin note','middle diagram','comm.; comm ?'),('display','middle right','v=v′∘phi_* ?'),('text','middle right lower','On sait que v∘u=v′∘u′=v′(phi_*u)=(v′phi_*)u'),('text','Considérons','alors la sous catégorie pleine de Atilde'),('deletion','Considérons first line','image essentielle'),('deletion','Considérons second line above','réciproquement'),('deletion','Considérons second line','formée des'),('insertion','Considérons between lines','dont l’un des objets est'),('text','Considérons continuation','la réunion des images essentielles de'),('display','middle lower','F G'),('drawing','under F','short vertical stroke'),('diagram','middle lower left first','Psi1° — a → Phi → Psi2°'),('diagram','middle lower left second','Phi1→Psi—Phi2; Psi→a→Phi2; Phi1=lim a_i'),('drawing','middle dividing line','long rising curved separator'),('display','middle lower','Atilde ⊂'),('diagram','lower middle','Ahat → F; Avee → G'),('deletion','ou bien','G='),('display','lower right first','(F,G,alpha)≃(F,Fsharp,alpha_F)'),('display','lower right second','(F,G,alpha)≃(G^b,G,alpha^G)'),('diagram','lower right above columns','a ⇄ F'),('diagram','lower left','A→B; Btilde→Atilde; Bhat→Ahat'),('drawing','lower left','diagonal separator'),('diagram','lower middle','Ahat→Bhat; A→B; Avee→Bvee; Bvee→Avee'),('diagram','bottom circled','Ahat↪Atilde↩Aveeo; Bhat↪Btilde↩Bveeo, mixed vertical arrows')]
save_page(115,12,tex,el,doubts=[('recurring superscript','sharp','natural; drawn like a bent double stroke','medium'),('top right','fon. cogénérateur','fonct. abbreviated very briefly','medium'),('F/F′ diagrams','F′','G overwritten over F′ in several places','low'),('Considérons deleted insertion','réciproquement','first and last strokes cancelled','low'),('Considérons category','double tilde A','tilde overwritten','low'),('Considérons continuation','la réunion des images essentielles de','unfinished and partly reworked wording','low'),('G^b','superscript b','flat sign','medium'),('lower final diagram','Atilde downward to Btilde','earlier isolated Btilde upward to Atilde; both retained','high')],notes='Questions when phisharp is fully faithful; writes sufficiency of strict generating or cogenerating condition. Yoneda case claimed faithful, then morphism compatibility is investigated with v=v′phi_*?. Reworked “Considérons” passage tries to select triples from images of the two constructions. Bottom isolated diagram has Btilde→Atilde, but circled six-node diagram has Atilde→Btilde: retain contrary directions. Superscript resembling sharp/natural now particularly visible; no context consulted.')
