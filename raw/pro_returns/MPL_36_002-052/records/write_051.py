from save_page import save
tex=r'''\scanpage{51}
\mspage{13}
\[
\mathcal H^0:\widetilde C_A\longrightarrow\widehat C_A \qquad(10)
\]
le foncteur d'injection des faisceaux dans les préfaisceaux.
Le foncteur $\mathcal H^0$ est un foncteur exact à gauche (2.3.14.II).
Ses foncteurs dérivés droitsseront notés :
\[
\mathcal H^q:\widetilde C_A\longrightarrow\widehat C_A \qquad(11)
\]
Pour tout objet $X$ de $C$ \deleted{\illegible{1}} et pour tout A-Module $F$, on a :
\[
\inserted{\mathcal H^q(F)(X)}\;\deleted{\unsure{\mathcal H^q}}\;
\deleted{H^0(\widehat C/X,\mathcal H^q(F))}=H^q(\widetilde C/X,F)\qquad(12)
\]
En effet pour $q=0$, cet isomorphisme résulte immédiatement des définitions. On l'en déduit pour tout $q$ en remarquant que le foncteur ``sections sur $X$'' est exact à sur la catégorie des préfaisceaux.

Soit $L:\widehat C\longrightarrow\widehat C$ le foncteur défini en (2.3.11.II).
Le foncteur $L$ commute aux limites projectives finies et par suite transforme \inserted{les} préfaisceaux d' A-modules en préfaisceaux de A-modules. Nous noterons :
\[
\check{\mathcal H}^{0}:\widehat C_A\longrightarrow\widehat C_A \qquad(13)
\]
le foncteur induit par $L$ sur les préfaisceaux de A-modules.
Le foncteur $\check{\mathcal H}^0$ est exact à \deleted{droite} gauche. Ses foncteurs dérivés droits seront notés $\check{\mathcal H}^q$. \deleted{\unsure{Les préfai}} Soit $G$ un préfaisceau de A-modules. Les préfaisceaux $\check{\mathcal H}^q(G)$ seront appelés les préfaisceaux de \uline{cohomologie de \v{C}ech} du préfaisceau $G$.

Ppour tout objet $X$ de $C$, on a un isomorphisme canonique :
\deleted{
\[
\deleted{\unsure{H^0(\widehat C, H^0(\widehat C/X,\qquad(G)))=\operatorname{Lim}}}
\]
\[
H^0(\widehat C/X,\qquad(G))=\underset R{\operatorname{Lim}}\,H^q(\widehat C/R,G)^{\unsure{C}}
\]
En effet pour $q=0$, cet isomorphisme résulte immédiatement des définitions
}
\[
\inserted{\check{\mathcal H}^q(G)(X)}\;\deleted{H^0(\widehat C/X,\check{\mathcal H}^q(G))}
=\varinjlim_R H^q(\widehat C/R,G)\qquad(14)
\]
\deleted{Ainsi qu'il} \inserted{Comme} resulte immédiatement des définitions (2.3.11.II).

(Dans cette formule la limite inductive est prise suivant la catégorie des cribles couvrants $X$).
\margin{50}
'''
e=[('display','top','H^0: C tilde_A → C hat_A (10)'),('text','upper','le foncteur d’injection; exact à gauche; droitsseront'),('display','upper','H^q: C tilde_A → C hat_A (11)'),('text','upper','Pour tout objet X'),('deletion','upper after C','overtyped word'),('display','upper','H^q(F)(X) = H^q(C tilde/X,F) (12)'),('insertion','formula 12 left','H^q(F)(X)'),('deletion','formula 12 left','small H^q and H^0(C hat/X,H^q(F))'),('text','upper middle','En effet pour q=0'),('text','middle','Soit L; Le foncteur L commute'),('insertion','middle margin into transforme préfaisceaux','les'),('display','middle','check H^0: C hat_A → C hat_A (13)'),('text','middle lower','le foncteur induit; Le foncteur check H^0'),('deletion','middle lower','droite'),('deletion','middle lower','Les préfai'),('text','lower','Ppour tout objet X'),('deletion','lower hatched block','overtyped former formula, H^0(C hat/X,(G)) = Lim_R H^q(C hat/R,G), En effet'),('display','bottom','check H^q(G)(X) = lim_R H^q(C hat/R,G) (14)'),('insertion','formula 14 left','check H^q(G)(X)'),('deletion','formula 14 left','H^0(C hat/X,check H^q(G))'),('text','bottom','Ainsi qu’il / Comme resulte; Dans cette formule'),('deletion','bottom sentence beginning','Ainsi qu’il'),('insertion','bottom sentence beginning','Comme'),('margin note','upper right and lower left','13; 50')]
d=[{'line':'after Pour tout objet X de C','reading':r'\illegible{1}','alternatives':'overtyping prevents recovery','confidence':'low'},{'line':'formula (12), small deleted expression','reading':r'\mathcal H^q','alternatives':'cancellation obscures base and exponent','confidence':'low'},{'line':'after derived functors of check H^0','reading':'Les préfai','alternatives':'Les préfais (unfinished typed word)','confidence':'medium'},{'line':'first line of hatched block','reading':r'H^0(\widehat C,H^0(\widehat C/X,\quad(G)))=\operatorname{Lim}','alternatives':'most letters overwritten with x; arrangement uncertain','confidence':'low'},{'line':'hatched block, above right end','reading':'C','alternatives':'stray letter or amendment to preceding G','confidence':'low'}]
save(51,tex,e,d,'Reused cohomology typescript p.13. Corrections replace section-of-presheaf formulations by evaluation H^q(F)(X) and check H^q(G)(X); exact à droite becomes gauche. The deleted intermediate formula remains heavily overtyped. Literal droitsseront, Ppour, and exact à sur retained; the missing accent in resulte is not supplied. This page states derived Čech functors and the covering-sieve colimit, which are claims to compare only after freeze.',sheet_kind='reused_typed')
