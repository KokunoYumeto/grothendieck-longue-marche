import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(37,r"""\scanpage{37}
Dans la situation générale des ext. pour $G$ correspondant
à une extension

\diagram{\begin{tikzcd}[column sep=small]
1\arrow[r,dash]&\pi_1\arrow[r,dash]&G_1\arrow[r,dash,"d"]&G_0\arrow[r,dash]\arrow[d,dashed,"\theta"]&\pi_0\arrow[r,dash]&1\\
&&&\operatorname{Aut}(G_1,\pi_1)&&
\end{tikzcd}}

on a (pour le $G$ donné) un hom
\[
\operatorname{Cent}(G_0)\cap\operatorname{Ker}\theta\xrightarrow{\varphi_G}Z^1(\pi_0,\pi_1)
\]
dont le noyau est l'image de $Z(G)$ dans $G_0$.

\margin{$\overbrace{\underbrace{\pi_0,\operatorname{Im}d}_{G_0},\pi_1}^{G}$}

Dans le cas qui nous intéresse
\[
\begin{aligned}
[\ G_1&=D'=L_1.D_1=\operatorname{Cent}G.\operatorname{Der}G,\quad
G_0=L'=G/L_1\cap D_1\\
&=G/\operatorname{Cent}G\cap\operatorname{Der}G\quad ---\ ]
\end{aligned}
\]
cela \deleted{\unsure{aussi}} s'exprime par
\[
\operatorname{Cent}(D_0)\cap\operatorname{Ker}\theta\xrightarrow{\varphi_G}\operatorname{Hom}(\pi_0,\pi_1)
\]
\inserted{(c'est ce qui exprime que $L_0\longleftrightarrow\operatorname{Cent}G$ est iso)}
dont le noyau doit être nul; ceci montre
donc qu'on doit avoir (compte tenu
que $\pi_1$ est quasi-unipot.)
\[
\boxed{\operatorname{Cent}D_0\cap\operatorname{Ker}\theta\text{ est quasi-unipotent}}
\]
\inserted{$\simeq[\operatorname{Cent}(\operatorname{Dér}(G))/\operatorname{Cent}(G)]\cap\operatorname{Cent}D'_0$}
\margin{$D_0\simeq G/\unsure{(\operatorname{Cent}G)}$}

En fait, on doit avoir mieux, comme
\unsure{à savoir} \uline{$\operatorname{Cent}(D_0)$ unipotent}

\diagram{\begin{tikzcd}[column sep=small,row sep=large]
&&L_1\arrow[dl,dash,hook',"A"']\arrow[dr,dash,hook',"H"]\arrow[drr,bend left=40,dash,"D_0"]&&\\
1\arrow[r,dash,hook]&\pi_1=L_1\cap D_1\arrow[rr,dash,hook,"A\times H"]\arrow[dr,dash,hook,"H"']&&D'\arrow[r,dash,hook]&G\\
&&D_1\arrow[ur,dash,hook,"A"']\arrow[urr,bend right=40,dash,"L_0"']&&
\end{tikzcd}}
\margin{\unsure{donc}}
\mspage{36}
""",'text',[('text','top','Dans la situation générale'),('diagram','upper','1 pi1 G1 G0 pi0 1'),('display','upper-middle','Cent(G0) intersection Ker theta'),('marginalia','upper-right braces','G pi0 Imd pi1 G0'),('text','middle','Dans le cas qui nous intéresse'),('display','middle','G1 D prime L1 D1'),('display','middle','Cent(D0) intersection Ker theta'),('marginalia','middle insertion','c’est ce qui exprime'),('text','lower-middle','dont le noyau doit être nul'),('display','lower-middle box','Cent D0 intersection Ker theta est quasi-unipotent'),('marginalia','lower-right','Cent(Der(G)) / Cent(G)'),('text','lower','En fait on doit avoir mieux'),('diagram','bottom','L1 D1 D prime G'),('marginalia','bottom-left','36')],doubts=[('lower-right edge','D0 isomorphic G / (Cent G)','The denominator continues into the cropped right edge.','low'),('bottom diagram','hooked connections','The visible hooks are preserved without adding full arrowheads to the source connections.','medium')],observations='Formal group continuation gives a map Cent(G0) intersect Ker theta to Z1(pi0,pi1), specialized to Hom(pi0,pi1), and a boxed quasi-unipotence assertion; a stronger unipotence claim is tentative. Source central and derived group notation and diagram require cautious contextual interpretation.')
