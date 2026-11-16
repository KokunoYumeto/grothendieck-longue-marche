from page_work import save_page
text=r'''\scanpage{98}
Plus généralement, définissons
\[
\underline{\operatorname{Hom}}_{S/k}(F,G)=
\underline H^0_{S/k}(\underline{\operatorname{Hom}}_S(\unsure{F|G},G))
\]
\deleted{\unsure{Alors}} et \inserted{notons} les foncteurs dérivés de
$G\longmapsto\underline{\operatorname{Hom}}_{S/k}(F,G)$ par
\[
\underline{\operatorname{Ext}}^i_{S/k}(F,G).
\]
On a alors, si on admet que pour $G$ injectif,
$\underline{\operatorname{Hom}}_S(F,G)$ est acyclique pour
$\underline H^0_{S/k}$, \deleted{et pour $H^0_S$}, les suites spectrales
\margin{vérifier}
\[
\underline{\operatorname{Ext}}^{*\deleted{\unsure{p+q}}}_{S/k}(F,G)
\Longleftarrow\underline H^p_{S/k}
(\underline{\operatorname{Ext}}^q_S(\unsure{F|k},G))
\]
et compte tenu de
\[
\operatorname{Hom}_S(F,G)\simeq
H^0(k,\underline{\operatorname{Hom}}_{S/k}(F,G))
\]
et admettant que pour $G$ injectif,
$\underline{\operatorname{Hom}}_{S/k}(F,G)$ est acyclique pour $H^0(k,-)$,
on trouve
\margin{vérifier}
\[
\operatorname{Ext}^*(S;F,G)\Longleftarrow
H^p(k,\underline{\operatorname{Ext}}^q_{S/k}(F,G)).
\]
Enfin on aura
\[
\underline H^*_{S/k}(F)\simeq
\underline{\operatorname{Ext}}^*_{S/k}(\mathbb Z_S,F).
\]

Notations et remarques analogues en partant de faisceaux sur
$U\unsure{\subset|\in}S$, au lieu de $S$.
\mspage{97}
'''
save_page(98,text,[('text','top','Plus généralement définissons'),('display','top','Hom S/k(F,G)=H0 S/k(Hom S(F,G))'),('deletion','upper before et','Alors'),('insertion','upper above les','notons'),('text','upper','et notons les foncteurs dérivés'),('display','upper middle','Ext i S/k(F,G)'),('text','middle','On a alors si on admet'),('deletion','middle after H0 S/k','et pour H0 S'),('margin note','left middle bracket','vérifier'),('display','middle','Ext star S/k ⇐ Hp S/k(Ext q S)'),('deletion','in exponent of middle display','p+q'),('text','middle lower','et compte tenu de'),('display','middle lower','Hom S(F,G) ≃ H0(k,Hom S/k(F,G))'),('text','lower','et admettant que pour G injectif'),('margin note','left lower bracket','vérifier'),('display','lower','Ext star(S;F,G) ⇐ Hp(k,Ext q S/k(F,G))'),('text','lower','Enfin on aura'),('display','lower','H star S/k(F) ≃ Ext star S/k(Z S,F)'),('text','bottom','Notations et remarques analogues'),('text','bottom left page number','97')],observations='Both halves reread, including each spectral-sequence arrow and underline. Marginal vérifier appears twice. The overwritten exponent and the final relation U to S are explicitly doubtful.')
