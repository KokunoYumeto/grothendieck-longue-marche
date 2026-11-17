import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
s=r'''\scanpage{59}
% archive foliation: 58
% Manuscript written upside down relative to the supplied scan.
\deleted{Il faut prouver que \deleted{le noyau} l'hom}
\[
\deleted{\operatorname{Hom}_k^\bullet(L^\bullet,C^\bullet)\longrightarrow
Z^n(C^\bullet)^{\unsure{p|\beta}}\subset(C^n)^{\unsure{p|\beta}}}
\]
\deleted{admet un $\Sigma$-noyau}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
&\deleted{\underline{\operatorname{Hom}}_{\Sigma\text{-sex}}}\arrow[d]&\\
&\deleted{B^\bullet}\arrow[dl,bend right=15]\arrow[dr,bend right=12]&\\
\deleted{\underline{\operatorname{Hom}}_{\Sigma\text{-ex}}\simeq B^{\mathrm{rés}}}\arrow[ddr,bend right=15]&&\deleted{\underline{\operatorname{Hom}}_{\mathrm{sex}}\deleted{\unsure{\mathrm{pl}}}}\arrow[d,bend right=12]\\
&&\deleted{B^{\bullet\mathrm{pl}}\deleted{\unsure{\underline{\operatorname{Hom}}_{\mathrm{sex}}}}}\\
&\deleted{B^{\mathrm{rés.pl}}}&
\end{tikzcd}}
\margin{\deleted{$\left\{\begin{array}{l}B\text{ cat. abélienne}\\\Sigma\text{ suites exactes}\\\text{ordinaires}\end{array}\right.$}}
\[
\deleted{\operatorname{Ext}^1(L^\bullet,M)\Longleftarrow0}
\]
\[
\deleted{\underline{\operatorname{Hom}}_{\Sigma\text{-ex}}(\mathcal P,B)
\overset{\sim}{\unsure{-|\longrightarrow}}\underline{\operatorname{Hom}}_{\Sigma\text{-ex}}(\mathcal P_0,B)}
\]
\deleted{$\unsure{\forall|N} B$ \deleted{\unsure{cat. de}}\inserted{admet}
(\inserted{$\Sigma$-}noyaux)}
'''
e=[('deletion','whole sheet','long diagonal cancellation'),('text','top in rotated orientation','Il faut prouver que'),('deletion','top phrase','le noyau'),('display','upper','Hom(L,C) -> Z^n(C)^p subset(C^n)^p'),('text','upper','admet un Sigma-noyau'),('diagram','upper middle','Hom Sigma-sex; B bullet; Hom Sigma-ex; B rés.pl'),('deletion','diagram right upper','pl'),('deletion','diagram right lower','Hom sex'),('margin note','right of diagram','B cat. abélienne Sigma suites exactes ordinaires'),('display','middle lower','Ext1(L,M) Longleftarrow0'),('display','lower','Hom(P,B) isom Hom(P0,B)'),('text','below final display','forall B admet Sigma-noyaux'),('deletion','final line','cat. de'),('insertion','final line','admet'),('insertion','final line','Sigma-')]
save(59,s,e,'cancelled_draft')
