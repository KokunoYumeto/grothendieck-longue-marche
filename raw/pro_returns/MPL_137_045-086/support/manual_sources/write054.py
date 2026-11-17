import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{54}
% archive foliation: 53
en $L_\bullet$'', ce qui donne si on veut
\[
F\xrightarrow{u}\sigma\rho F
\]
hom fonctoriel en $F$, \unsure{d'où} \deleted{\unsure{la}} \unsure{l'un}
d'adjonction postulée
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\operatorname{Hom}(\rho F,C^\bullet)\arrow[rr]\arrow[dr,dashed]&&\operatorname{Hom}(F,\sigma C^\bullet)\\
&\operatorname{Hom}(\sigma\rho F,\sigma C^\bullet)\arrow[ur,"\alpha\longmapsto\alpha\circ u"']&
\end{tikzcd}}
à prouver que c'est un iso --- vérification
facile.

L'hom can
\[
\rho\sigma C^\bullet\unsure{-|\longrightarrow}C^\bullet
\]
est un iso, i.e. $\sigma$ est pl. fid. En effet,
\[
\rho(\sigma(C^\bullet))=\sigma(C^\bullet)(C_\bullet^\bullet)
=\left(\underbrace{\sigma(C^\bullet)(C_\bullet^i)}_{\substack{
\operatorname{Hom}_k^\bullet(C_i^\bullet,C^\bullet)\\\Vert\\C^i}}
\right)_i\simeq(C^i)_i\quad\mathrm{OK}.
\]
Ainsi on a une inclusion pl. fidèle
\[
B^\bullet\xhookrightarrow{\sigma}\underline{\operatorname{Hom}}_{k,\Sigma\text{-\unsure{sex|lex}}}
\subset\underline{\operatorname{Hom}}_{k\text{-lin}}
\]
où $\Sigma$-\unsure{sex|lex} désigne les foncteurs qui transforment
suites de $\Sigma$ en suites exactes à g.

Quelle est l'image essentielle de $B^\bullet$ ?
(On donnera des exemples \unsure{tantôt de|quantité de}
foncteurs dans l'image ess.) est-ce tout
$\underline{\operatorname{Hom}}_{k,\Sigma\text{-\unsure{sex|lex}}}$ ? Elle est formée des $F$
tels que
\[
F\xrightarrow{u}\sigma\rho(F)
\]
soit un iso. Or on a
'''
save(54,text,[('text','top continuation','en L'),('display','upper','F u sigma rho F'),('text','upper','hom fonctoriel en F'),('deletion','upper phrase','la'),('diagram','upper quarter','Hom(rhoF,C) Hom(F,sigmaC) Hom(sigmarhoF,sigmaC)'),('text','below diagram','à prouver que c’est un iso'),('text','middle','L’hom can'),('display','middle','rho sigma C → C'),('text','middle','est un iso'),('display','middle equality with annotation','rho(sigma(C)) = sigma(C)(C)'),('text','lower middle','Ainsi on a une inclusion'),('display','lower middle','B^• hook Hom_Sigma-sex subset Hom_k-lin'),('text','lower middle','où Sigma-sex désigne'),('text','lower quarter question','Quelle est l’image essentielle'),('display','bottom','F u sigma rho(F)'),('text','bottom','soit un iso Or on a')])
