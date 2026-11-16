from page_work import save_page
text=r'''\scanpage{97}
\deleted{dans la catégorie $C'(k)$ aux foncteurs compatibles avec les
limites inductives.}

On constate que le foncteur $\mathcal N$ qu'on vient de définir est exact
à gauche, \unsure{et} transforme groupes comm. en groupes comm., d'où
$C(S)\longrightarrow C'(k)$. On pose aussi
\[
\mathcal N(F)=\underline H^0_{S/k}(F)
\]
et \deleted{\unsure{de}} par suite
\[
R^i\mathcal N(F)=\underline H^i_{S/k}(F).
\]
Notons l'isomorphisme
\[
H^0_S\simeq H^0_k\circ\underline H^0_{S/k}
\]
et d'autre part que $\underline H^0_{S/k}$ \uline{transforme injectifs en injectifs}
\margin{à vérifier\ldots}
\deleted{\unsure{car on va voir} en construisant un adjoint à
$\mathcal N=\underline H^0_{S/k}$ et constatant que ce dernier est exact
à gauche :
\[
\operatorname{Hom}(\Phi,\mathcal N(F))\simeq
\operatorname{Hom}(\mathcal N^*(\Phi),F).
\]}
D'où une suite spectrale de Leray
\[
H^*(S,F)\Longleftarrow H^p(k,\underline H^q_{S/k}(F)).
\]
\mspage{96}
'''
save_page(97,text,[('deletion','top two lines','dans la catégorie C prime(k)'),('text','upper paragraph','On constate que le foncteur N'),('display','upper middle','N(F)=underlined H0 S/k(F)'),('text','middle','et par suite'),('deletion','middle after et','de'),('display','middle','Ri N(F)=underlined Hi S/k(F)'),('text','middle lower','Notons l’isomorphisme'),('display','middle lower','H0 S ≃ H0 k composed H0 S/k'),('text','lower','et d’autre part que H0 S/k transforme injectifs'),('margin note','left lower','à vérifier'),('deletion','lower cancelled paragraph','car on va voir en construisant'),('display','within cancelled paragraph','Hom(Phi,N(F)) ≃ Hom(N star(Phi),F)'),('text','bottom','D’où une suite spectrale de Leray'),('display','bottom','H star(S,F) ⇐ Hp(k,Hq S/k(F))'),('text','bottom left page number','96')],observations='The two supplied halves were reread against the full-page view, and the heavily cancelled lower adjunction paragraph and live opening were enlarged. The marginal à vérifier is not folded into the asserted text. The cancelled paragraph continues the same correction sequence begun on 96.')
