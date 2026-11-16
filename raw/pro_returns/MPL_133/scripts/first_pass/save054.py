import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(54,r"""\scanpage{54}
\mspage{7}
$\eta_0=\operatorname{Coker}(\pi_1\longrightarrow\eta)$, et l'hom
\[
\lambda_0:\pi_0\otimes\pi_0\longrightarrow\eta_0
\]
déduit de $\lambda_G$ par passage au quotient. C'est
indépendant du choix de $G$, on le voit que
c'est ce qu'on construit directement dans
le groupe $K=G/\pi_1$. Il faut donc

b) $\lambda_0$ surjectif (car signifie aussi
que $N/\pi_1$ dans $K\subset M\times M'$ est $=DK$,
ou encore que $dN=DM\ \unsure{\}}$ exactement)
\margin{Vérifier}

\deleted{\unsure{a}} Introduisons alors $\operatorname{Ker}\lambda_0=P\subset\pi_0\otimes\pi_0$,
(indépendant de $G$), donc $\lambda_G$ induit
\[
\overline\lambda_G:P\twoheadrightarrow\pi_1^{\deleted{\unsure{*}}}{}_{\inserted{*}}=\operatorname{Im}(\pi_1\longrightarrow\eta)\subset\eta
\]
et la condition effective dépendant du
choix de $G$ qui reste à exprimer
est

c) $P\xrightarrow{\overline\lambda_G}\pi_1^{\deleted{\unsure{*}}}{}_{\inserted{*}}$ est un épi.

Ici la dépendance de cette condition
par $G$ variable est explicitée grâce à
la formule donnant $\overline\lambda_{\unsure{G_1}}$ en fonction
de $\lambda_G$, qui s'écrit de façon évidente
\[
\overline\lambda_{G_1}=\overline\lambda_G+pc_Ei
\]
$i$ l'inclusion $P\subset\pi_0\otimes\pi_0$, $p$ la projection $\pi_1\longrightarrow\pi_{1*}$.
\mspage{53}
""",'text',[
('text','top folio and formula','7; eta_0=Coker(pi_1 to eta)'),('display','top','lambda_0:pi_0 tensor pi_0 to eta_0'),('text','upper third','déduit de lambda_G'),('text','upper middle','b) lambda_0 surjectif'),('margin note','left beside dN=DM','Vérifier'),('deletion','before Introduisons','a'),('text','middle','Introduisons alors Ker lambda_0'),('display','middle','lambda bar_G:P to pi_1*'),('deletion','stars above pi_1','superscript star'),('insertion','stars below pi_1','subscript star'),('text','middle lower','et la condition effective'),('display','lower middle','c) P to pi_1* est un épi'),('text','lower third','Ici la dépendance'),('display','lower third','lambda bar_G1=lambda bar_G+p c_E i'),('text','last line','i l’inclusion; p la projection'),('text','bottom folio','53')],doubts=[('b) final punctuation','dN=DM } exactement','A curly crossing/bracket after DM has no secure textual value; retained with doubt','medium'),('pi_1 decoration','star above cancelled, star below added','Two overwritten stars are visible at each occurrence; exact earlier star shape uncertain','medium'),('first induced arrow','twoheaded arrow','Arrow is repeatedly inked and appears doubled; retained despite subsequent epi condition','medium')],observations='N=DG criterion refined by eta_0, lambda_0, P and residual epimorphism; explicit margin Vérifier at equivalence with dN=DM. Variation formula at foot ends the kept material.')
