import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{91}
% archive foliation: 93
\margin{\uline{Déc 83}}
\uline{Courbes elliptiques réelles}

Soit $k$ un anneau (pas néc comm.)

\deleted{$M$ un $k$-\unsure{module}}
Considérons la catégorie des $k$-Modules
$M$ munis d'un \unsure{autom.} $\sigma$ \deleted{tel que}
tel que
\[
\begin{array}{ll}
\text{a)}&\sigma^2=\operatorname{id}\\
\text{b)}&2\operatorname{id}_M\text{ injectif (on dit alors }M\text{ 2-régulier)}
\end{array}
\]
A un tel couple $(M,\sigma)$, \inserted{nous} associons le couple
$(P,Q,m)$ de deux \inserted{$k$-}modules pour lesquels $2\operatorname{id}_P$ et $2\operatorname{id}_Q$
sont injectifs (i.e. $P,Q$ 2-réguliers), et
$m\subset P/2P\oplus Q/2Q$ \inserted{sous $k/2k$-module} avec
$m\cap P/2P=0$, $m\cap Q/2Q=0$
(c'est deux sous-modules $p'\subset p\overset{\mathrm{def}}=P/2P$, $q'\subset q=Q/2Q$,
et un iso. $p'\simeq q'$), de la façon suivante
\[
\begin{aligned}
P=M_+&=\operatorname{Ker}(\operatorname{id}_M-\sigma)=\{x\in M\mid\sigma x=x\}\\
Q=M_-&=\operatorname{Ker}(\operatorname{id}_M\unsure{-|+}\sigma)=\{\unsure{x|m}\in M\mid\sigma x=-x\}.
\end{aligned}
\]
NB $M_+\cap M_-=0$ dans $M$, car $M$ 2-régulier, donc
\margin{!}
\[
2M\subset M_+\oplus M_-\subset M\deleted{\subset\tfrac12(M_+\oplus M_-)}
\quad\text{car }\forall x\in M,\text{ on a }2x=\underbrace{(x+\sigma x)}_{M_+}+\underbrace{(x-\sigma x)}_{M_-}.
\]
soit
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
M' \arrow[d,equal] \arrow[r,phantom,"\subset"] & M_+\oplus M_-=P\oplus Q & \unsure{\sigma}\\
2M &&
\end{tikzcd}}
on a donc
\[
\deleted{\unsure{M'\supset}}2P\oplus2Q\subset M'\subset P\oplus Q.
\]
donc $M'$ est l'image d'un sous-module $m$ de
\[
(P\oplus Q)/2P\oplus2Q\simeq\underbrace{P/2P}_p\oplus\underbrace{Q/2Q}_q,
\quad\text{et on vérifie que}
\]
\[
\left\{\begin{aligned}
m\cap\deleted{\unsure{q}}p&=0\quad\text{i.e.}\quad
\underbrace{M'\cap(P+(2P+2Q))}_{M'\cap P+(2P+2Q)}=(2P+2Q)\quad\text{car }M'\cap P=2P\\
m\cap q&=0\quad\text{car}\quad M'\cap Q+(2P+2Q)=\unsure{2Q}\quad\text{car }M'\cap Q=2Q
\end{aligned}\right.
\]
\margin{puisque $2x\in P$ i.e. $2\sigma x=2x$ implique $x\in P$ i.e. $\sigma x=x$}

D'ailleurs \deleted{\unsure{M'\oplus Q}} $(M,\sigma)$ se reconstitue à isom can près de
$(P,Q,m)$, car $M'\subset P\oplus Q$ se reconstitue, et
\deleted{\unsure{M}}$\sigma_{M'}$ aussi \unsure{l'étant} par $\operatorname{id}_P\oplus(-\operatorname{id}_Q)$,
Or $2\operatorname{id}_M\deleted{\unsure{M}}:M\longrightarrow M'$ est un iso de $(M,\sigma_M)$ vers $(M',\sigma_{M'})$.

\uline{Prop} Le foncteur précédent $(M,\sigma)\longmapsto(P,Q,m)$ est une équivalence
de catégories.

\uline{Cor} Supposons $k$ \deleted{\unsure{un anneau}\unsure{ intègre}\unsure{ de Dedekind}\unsure{ projectif}}
\inserted{comm.}\inserted{\unsure{et} $k$ 2-régulier}, prenons
\deleted{\unsure{des}}\inserted{$(M,\sigma)$} $M$ \deleted{\unsure{projectif}}\inserted{\unsure{projectif}} de \unsure{rang} $2$
avec $\sigma\ne\operatorname{id}_M,-\operatorname{id}_M$, alors la cat
\deleted{de}\inserted{des} \unsure{formés} \deleted{\unsure{par}\unsure{ ces}\unsure{ objets}\unsure{ est}}\inserted{\unsure{on a} $\sigma^2=\operatorname{id}$}
\unsure{(H Q.\ 1\text{ ou }2?)}
équivaut à celle des paires $(P,Q)$ avec $P,Q$ inv., et
$p'\subset P/2P$, $q'\subset Q/2Q$ et $p'\overset{u}\simeq q'$ donné.
"""
save(91,tex,[('margin note','top left','Déc 83'),('text','top right title','Courbes elliptiques réelles'),('text','top','Soit k un anneau'),('deletion','above Considérons','M un k-module'),('text','upper','Considérons la catégorie des k-Modules'),('deletion','after sigma','tel que'),('display','upper list','a sigma squared=id b 2id injectif'),('text','upper middle','A un tel couple'),('insertion','before associons','nous'),('insertion','before modules','k-'),('insertion','above avec','sous k/2k-module'),('display','middle','P=M+ ; Q=M-'),('text','middle NB','M+ intersection M-=0'),('margin note','left of inclusions','!'),('display','middle','2M subset M+ direct sum M-'),('deletion','after subset M','subset half of M+ direct sum M-'),('text','below inclusions','soit'),('diagram','middle','M prime =2M subset P direct sum Q'),('text','middle lower','on a donc'),('display','middle lower','2P direct sum 2Q subset M prime'),('deletion','left of 2P','M prime superset'),('text','middle lower','donc M prime est l’image'),('display','lower quotient','P direct sum Q / 2P direct sum 2Q'),('display','lower brace','m intersection p=0 m intersection q=0'),('deletion','first intersection','q'),('margin note','right of brace','puisque 2x in P'),('text','lower','D’ailleurs (M,sigma) se reconstitue'),('deletion','after D’ailleurs','M prime direct sum Q'),('deletion','before sigma M prime','M'),('deletion','after 2id_M','M'),('text','lower proposition','Le foncteur précédent'),('text','foot corollary','Supposons k'),('deletion','after k','un anneau intègre de Dedekind projectif'),('insertion','above first deletion','comm.'),('insertion','above prenons','et k 2-régulier'),('deletion','after prenons','des'),('insertion','above des','M sigma'),('deletion','after M','projectif'),('insertion','above M','projectif'),('deletion','after la cat','de'),('insertion','above de','des'),('deletion','after formés','par ces objets est'),('insertion','above long deletion','on a sigma squared=id'),('margin note','far right at foot','H Q. 1 ou 2?')],doubts=[('top parenthesis','pas néc comm.','Read abbreviated néc without expansion.','medium'),('M endowed with sigma','autom.','Last strokes and period uncertain.','medium'),('kernel defining Q','minus','Could be a collapsed plus; the minus reading is first because the visible short stroke does not clearly cross.','low'),('condition m intersection q','2Q','Ink looks 2Q despite expected 2P+2Q; retained, no correction.','medium'),('right of M prime diagram','sigma','Detached loop could be a stray writing mark.','low'),('lower reconstruction paragraph','l’étant','Verb phrase strongly compressed.','low'),('entire corollary revisions','un anneau intègre de Dedekind projectif; projectif; formés; on a','Several overlapping drafts; word order and whether some retraced words are cancelled remain low confidence.','low'),('far-right parenthesis at foot','H Q. 1 ou 2?','Several characters appear as Roman or mathematical capitals, unresolved.','low')],notations=[('involution',r'\sigma','Lowercase sigma, square equal id.'),('eigenspaces',r'M_+,M_-','Signs used as subscripts.'),('reduction submodules',r'p,q,p\prime,q\prime,m','Plain lowercase letters, primes distinct from exponent !.'),('divisibility integer',r'2','Two, not capital Z.')],abbreviations=[('néc','nécessairement'),('comm.','commutatif'),('inv.','inversibles'),('cat','catégorie'),('isom can','isomorphisme canonique')],leads=['Classification of 2-torsion-free modules with involution via two eigenspaces and a graph submodule of their reductions modulo 2.','Potential sign ambiguity in Q=Ker(id_M minus/plus sigma) and incomplete-looking formula for m intersection q; keep reading questions separate from proof.','Bottom corollary on rank-2 projective modules and invertible eigenspaces is heavily revised; assumptions on k require checking rather than silently completing.','Separate title Courbes elliptiques réelles and date Déc 83, no author page number visible.'])
