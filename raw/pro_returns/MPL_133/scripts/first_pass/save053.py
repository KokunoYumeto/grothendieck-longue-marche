import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(53,r"""\scanpage{53}
\mspage{6}
ou encore
\[
M'\times M'\xrightarrow{\lambda_G}\eta
\]
C'est obtenu ainsi : si $x,y\in M'(\unsure{\ell})$, on relève en
$\bar{x},\bar{y}\in\unsure{G|N}$, on prend $(\bar{x},\bar{y})=\bar{x}\bar{y}\bar{x}^{-1}\bar{y}^{-1}$, qui est
dans $N$, on réduit mod $N_0$, et c'est $\lambda_G(x,y)$.
(\deleted{\unsure{Comme}}\inserted{Si} $N'$ est central (ce qu'on suppose))
cette description montre que si $\unsure{\bar{x}},\unsure{\bar{y}}$
$\in d'(N')\subset M'$, alors \deleted{$\unsure{q}$} $\lambda_G(x,y)=0$, donc $\lambda_G$
s'interprète comme un hom
\[
\pi_0\otimes\pi_0\xrightarrow{\lambda_G}\eta=(N_{\mathrm{comm}})_M
\]
Notons aussi que $\lambda_G$ est alternée. Ceci
posé, \deleted{la condition} on a évidemment
\[
N/DG\simeq\eta/\lambda_G(\pi_0\otimes\pi_0)
\]
donc la condition cherchée est que
$\lambda_G$ \uline{est surjective}. Pour apprécier
cette condition, il faut voir comment
$\lambda_G$ varie avec $G$, on trouve (si $G_1$ \unsure{est déduit de}
$G$ défini par l'extension $E$ de $\pi_0$ par $\pi_1$)
\[
\lambda_{G_1}=\lambda_G+\beta c_E
\]
où $c_E:\pi_0\otimes\pi_0\longrightarrow\pi_1$ est l'accouplement
associé à l'ext. centrale de $\pi_0$ \inserted{(comm)} par $\pi_1$,
et où
\[
\beta:\pi_1\longrightarrow\eta=(N_{\mathrm{comm}})_M
\]
est le passage au quotient. \deleted{$\unsure{N_0}$}

Nous pouvons dévisser la condition
$\lambda_G$ \uline{surjective}, en introduisant encore
\mspage{52}
""",'text',[
('text','top folio and continuation','6; ou encore'),('display','top','M prime times M prime to eta'),('text','upper third','C’est obtenu ainsi'),('deletion','parenthesis','Comme'),('insertion','over Comme','Si'),('text','upper middle','cette description montre'),('deletion','before lambda_G','q'),('display','middle','pi_0 tensor pi_0 to eta'),('text','middle','Notons aussi que lambda_G est alternée'),('deletion','middle','la condition'),('display','middle','N/DG=eta/lambda_G'),('text','below fold','donc la condition cherchée'),('display','lower third','lambda_G1=lambda_G+beta c_E'),('text','lower third','où c_E; et où'),('insertion','over pi_0','comm'),('display','lower third','beta:pi_1 to eta'),('deletion','right of passage au quotient','N_0'),('text','bottom','Nous pouvons dévisser'),('text','bottom folio','52')],doubts=[('first construction','G / N','Letter overwritten; G appears superposed on N-like strokes','medium'),('variation parenthesis','est déduit de G défini','Compressed overwritten phrase; not smoothed to a grammatically expected form','low'),('vanishing condition','bar x, bar y','Tiny marks above x and y might be crossing rather than bars; retained with doubt','medium')],observations='Alternating commutator pairing lambda_G on pi_0 tensor pi_0 with values in (N_comm)_M; quotient N/DG and surjectivity criterion; change under extension E via beta c_E. No proof beyond sketch.')
