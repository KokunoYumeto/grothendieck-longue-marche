import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{94}
% archive foliation: 96
Pour une courbe elliptique \uline{conforme} donnée, définie
par un réseau \inserted{$\pi$} dans un espace vectoriel \unsure{complexe|conforme}\inserted{$V$} de dim $1$,
les structures réelles qu'on peut mettre dessus correspondent
aux \deleted{\unsure{involutions} $\sigma$}\inserted{droites réelles de $V$}, telles que la
\deleted{\unsure{symétrie}}\inserted{réflexion} orth.
p.r. à $D$ conserve $\pi$. Peut-il y en avoir plusieurs ?
Si oui, les structures réelles correspondantes sont elles isom.
(i.e. conjuguées de l'une d'elles par les autos complexes
de la courbe) ? \deleted{En tous cas, si $\sigma,\sigma'$ sont les deux \unsure{involutions des}}

\deleted{Cas de} Dans tous les cas, soit $G$ le groupe des autos
\uline{conformes} de la courbe elliptique \unsure{conforme}\inserted{$X$ définie par $(\pi,c)$}.
Pour que \deleted{\unsure{l'on}\unsure{ remarque}}\inserted{$X$} admette une structure réelle, il \uline{faut} en
tous cas que $G\overset{\mathrm{det}}\longrightarrow\pm1$ soit surjectif, en autres termes,
on a
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
1\arrow[r,dash]&G^+\arrow[r]\arrow[d,equal]&G\arrow[r]&\pm1\arrow[r,dash]&1\\
&\operatorname{Aut}(X)&&&
\end{tikzcd}}

Mais un élément $\sigma$ de $G$ de déterminant $-1$
est une transformation orth. de déterminant $-1$,
c'est donc une réflexion, donc c'est une structure
réelle sur la courbe elliptique : les courbes elliptiques
qui admettent une structure réelles sont donc celles
isom. à la conjuguée, i.e. celles dont l'invariant
modulaire est \uline{réel}. L'ens \deleted{de ces structures
(pour $X$ fixée) \inserted{s'identifie à $G^-$ et} est un torseur sous $G^+$, qui est}
\inserted{$G^+$ est cyclique d'ordre} $n=2,4$ ou $6$, et $G$ \deleted{\unsure{se trouve}\unsure{ par}\unsure{ g}\unsure{ 1}\unsure{ 0}}
avec sa structure d'extension,
est isomorphe au groupe diédral $D_n$. L'un des
"""
save(94,tex,[('text','upper','Pour une courbe elliptique conforme donnée'),('insertion','above réseau','pi'),('insertion','above complexe','V'),('deletion','after aux','involutions sigma'),('insertion','above deletion','droites réelles de V'),('deletion','before orth.','symétrie'),('insertion','above symétrie','réflexion'),('text','upper middle questions','Peut-il y en avoir plusieurs'),('deletion','middle two lines','En tous cas si sigma sigma prime'),('deletion','before Dans tous','Cas de'),('text','middle','Dans tous les cas soit G'),('insertion','above conforme','X définie par pi,c'),('deletion','after Pour que','l’on remarque'),('insertion','above deletion','X'),('diagram','middle lower','1 G+ G plus minus 1 1 ; G+=Aut(X)'),('text','lower','Mais un élément sigma de G'),('text','lower criterion','les courbes elliptiques qui admettent une structure réelles'),('deletion','foot three lines','de ces structures pour X fixée est un torseur'),('insertion','within cancelled block','s’identifie à G- et'),('insertion','right above cancelled block','G+ est cyclique d’ordre'),('deletion','foot after G','se trouve par g 1 0'),('text','last two lines','avec sa structure d’extension est isomorphe')],doubts=[('space in first paragraph','complexe','conforme is the visible alternative; the repeated word on first line is clearly conforme.','medium'),('cancelled involution description','involutions sigma','First letters are under a long strike, may read symétries.','low'),('cancelled end of question paragraph','involutions des','Last word is unfinished or cut by a stroke.','low'),('definition of G insertion','X définie par (pi,c)','Insertion scope reaches back to courbe elliptique, not a separate formula.','medium'),('foot cancellation after G','se trouve par g 1 0','Only isolated strokes remain below the long cancellation.','low'),('first and final arrows of exact sequence','plain dashes','No arrowhead discernible; retained as dashes, not silently promoted to arrows.','medium')],notations=[('conformal automorphism extension',r'1-G^+\longrightarrow G\longrightarrow\pm1-1','First and last connectors have no clear arrowheads.'),('dihedral group',r'D_n','Subscript n, not superscript.'),('real-reflection line',r'D','Plain capital D here, unrelated to unit disc notation.')],abbreviations=[('orth.','orthogonale'),('p.r.','par rapport'),('dim','dimension'),('L’ens','L’ensemble')],leads=['Questions whether several real structures on one complex elliptic curve are all isomorphic.','Real modular invariant is claimed equivalent to existence of a real structure, via an orientation-reversing orthogonal automorphism.','Full conformal group with real structures is dihedral D_n, n=2,4,6, with cyclic orientation-preserving subgroup; distinguish all conformal automorphisms from origin-preserving ones.'])
