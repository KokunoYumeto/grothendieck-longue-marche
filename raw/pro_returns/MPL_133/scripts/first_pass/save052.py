import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(52,r"""\scanpage{52}
\mspage{\unsure{5}}
\[
\overline\psi_{G_1}:\zeta/\zeta_0=\pi_0^*\longrightarrow\uline{\operatorname{Hom}}(\pi_0,\pi_1)/\zeta_0
\]
déduit de $\psi_{G_1}$ par passage au quotient.
La condition à exprimer encore est

c) $\overline\psi_{G_1}$ est injective

Cette condition dépend effectivement de
$G_1$ à priori, puisque $\psi_{G_1}$ donc $\overline\psi_{G_1}$ en
dépend (de la manière explicitée plus
haut). Cette condition sur $G_1$ i.e. sur
\[
E_{\unsure{G}}\in\operatorname{Ob}\ \uline{\operatorname{Ext}}_{\mathrm{gr}}(\pi_0,\pi_1)
\]
\margin{(annulé\unsure{?})}

\figure{\begin{tikzpicture}\draw(0,0)--(3,.25);\draw(.45,-.1)--(3.2,.05);\end{tikzpicture}}

On veut exprimer maintenant
$N=DG$. Donc

 a) $N\supset DG$ i.e. $M'\ (=G/N)$ commutatif
\[
(\Longrightarrow\pi_0\text{ comm})
\]
Il faut exprimer ensuite que pour tout
ss-grpe \inserted{inv} $N_1\subset N$ tel que $G/N_1$ comm, on a
$N_1=N$. $G/N_1$ comm signifie que $G$ y
opère trivialt, cela implique qu'il opère
trivialt sur $N/N_1$ \inserted{et que celui-ci est comm}, or $G$ opère sur $N$
(ou $N/N_1$) via $M$, donc la condition est que
\deleted{$\unsure{N_1}$} $N/N_1$ est majoré par $\eta=N_{\unsure{\mathrm{coinv}\,M|\mathrm{comm}\,M}}$ \inserted{$=N/N_0$, i.e. $N_1\supset N_0$}.
Ceci dit dans l'extension \inserted{$G/N_0$} de $G/N=M'$ par
$\eta$, $G$ y opère, \inserted{en induisant l'id. sur les facteurs}, d'où un hom
\[
G\longrightarrow\uline{\operatorname{Hom}}(M',\eta)
\]
d'ailleurs nul sur $N$, d'où hom
\[
M'\longrightarrow\uline{\operatorname{Hom}}(M',\eta)
\]
\mspage{51}
""",'text',[
('text','top clipped folio','5'),('display','top','psi bar_G1:zeta/zeta_0'),('text','upper third','déduit de psi_G1; La condition'),('text','upper third','c) psi bar est injective'),('text','upper half','Cette condition dépend effectivement'),('display','upper half lower','E_G in Ob Ext_gr'),('margin note','left upper half','annulé?'),('drawing','between sections','two horizontal separating strokes'),('text','middle','On veut exprimer maintenant N=DG'),('display','middle','a) N superset DG; M prime commutatif'),('text','lower half','Il faut exprimer ensuite'),('insertion','above ss-grpe','inv'),('insertion','after N/N_1','et que celui-ci est comm'),('deletion','before quotient','N_1'),('display','within lower text','eta=N_coinv M'),('insertion','right margin','=N/N_0;i.e.N_1 superset N_0'),('insertion','over extension','G/N_0'),('insertion','over d’où','en induisant l’id. sur les facteurs'),('display','near foot','G to Hom(M prime,eta)'),('text','near foot','d’ailleurs nul sur N'),('display','bottom','M prime to Hom(M prime,eta)'),('text','bottom folio','51')],doubts=[('coinvariant notation','N_coinv M / N_comm M','Abbreviated subscript is not fully distinct; first reading follows visible strokes','medium'),('upper margin','annulé?','Margin flags the preceding condition, but no diagonal crossing; retained as marginal cancellation instruction without silently removing the text','medium')],observations='Upper continuation marked annulé? in margin; lower section begins criterion N=DG with coinvariant quotient eta and action pairing.')
