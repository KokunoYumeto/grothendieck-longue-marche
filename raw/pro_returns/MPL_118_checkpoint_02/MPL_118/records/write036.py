from save_page import save
text=r'''
\scanpage{36}
% archive foliation: 35
\deleted{Mais il n'est pas clair pour moi si}

\deleted{la} \uline{NB} La condition $(ii)$ est visiblement stable par sommes (i.e. si des $A_\alpha$ y satisfont, $A=\coprod_\alpha A_\alpha$ aussi), mais la condition $(i)$ non, donc \deleted{$(i)$ est} \inserted{l'implication} $(i)\Longrightarrow(ii)$ est stricte. Mais un $A$ qui satisfait $(ii)$, et qui est $0$-connexe \deleted{\unsure{je}} est alors \inserted{$\underline W$-}asphérique (même tot. $\underline W$-asphérique).

\uuline{NB} Prenons p.ex. \deleted{un} $A$ un groupoïde, alors dans $\widehat A$ $\underline W_A$ est formé des seuls iso (cas où $\underline W$ est l'équiv. faible habituelle) donc stable \uline{par produits} finis...

Cet argument de commutation \inserted{aux produits finis} marche directement dans $(\mathrm{Cat})$ également, \deleted{\unsure{donc on sait}} \inserted{puisqu'on sait} qu'un produit \deleted{\unsure{cartésien}} fini de foncteurs $\in\underline W$ est $\in\underline W$.

Pour le cas des produits infinis, il faut voir qu'un produit des $f_j\in\underline W$ est dans $\underline W$, \deleted{et} et/ou item dans un $\widehat A$ (le deuxième impliquera le premier). Déjà pour l'équiv. faible habituelle $\underline W_0$, ce n'est pas évident. Il y a des
'''
elements=[('deletion','top','Mais il n’est pas clair pour moi si'),('deletion','before NB','la'),('text','upper','NB La condition (ii) est visiblement stable par sommes'),('display','upper','A=coprod A_alpha'),('deletion','upper middle','(i) est'),('insertion','above (i) est','l’implication'),('display','upper middle','(i) ⇒ (ii)'),('text','middle','Mais un A qui satisfait (ii)'),('deletion','middle left','je'),('insertion','before asphérique','W-'),('text','middle','NB Prenons p.ex.'),('deletion','middle','un'),('display','middle','Ahat; W_A'),('text','middle lower','est formé des seuls iso'),('text','lower middle','Cet argument de commutation'),('insertion','above commutation','aux produits finis'),('deletion','lower middle','donc on sait'),('insertion','above cancelled phrase','puisqu’on sait'),('deletion','lower middle','cartésien'),('display','lower middle','in W; in W'),('text','bottom','Pour le cas des produits infinis'),('display','bottom','f_j in W; Ahat; W_0'),('deletion','bottom','et'),('text','bottom','Déjà pour l’équiv. faible habituelle')]
save(36,text,'text',elements,'Brown/black foreground text distinguished from pale blue reverse-side bleed-through. Two NBs: sums preserve condition (ii), 0-connectedness is used for the converse; groupoid example; infinite products are explicitly doubtful even for usual weak equivalences. A heavily cancelled short word before est alors and two cancellation readings are tentative. No mathematical claim checked.')
