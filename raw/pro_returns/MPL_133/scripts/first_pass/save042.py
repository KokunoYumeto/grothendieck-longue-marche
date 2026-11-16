import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(42,r"""\scanpage{42}
$G$ groupe alg. lisse connexe sur $k$, ayant une décomposition en ext. de Chevalley
(p.ex. $k$ parfait)
\[
1\longrightarrow\deleted{\unsure{H}}\inserted{L}\longrightarrow G\longrightarrow A^{\unsure{\mathrm{ab}}}\;---\;1
\qquad (*)\quad A\text{ schéma abélien},\ L\text{ groupe alg. affine lisse connexe}
\]
Considérons de plus $M=G_{\mathrm{aff}}$, le plus grand quotient affine de $G$,
et la suite
\[1\;---\;Z\;---\;G\longrightarrow\deleted{\unsure{A}}M\longrightarrow1\]
on sait que $(**)$ $M$ affine, $Z_{\mathrm{aff}}=1$ (\unsure{caractéristiques} pour cette ext.
et que cela entraîne $Z$ central dans $G$, $Z\longrightarrow A$ \uline{épi}.

Considérons
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&&1\arrow[dr]&&&1\\
&&&L\arrow[dr,hook]\arrow[rr,dashed]&&M\arrow[ur]\\
(\mathrm D)&L\cap Z=\mathfrak z\arrow[urr,hook]\arrow[drr,hook]&&&G\arrow[ur]\arrow[dr]&\\
&&&Z\arrow[ur,hook]\arrow[rr]&&A\arrow[dr]\\
&&1\arrow[ur]&&&&1
\end{tikzcd}}

avec $Z\longrightarrow A$ épi, donc $G=Z.L$, i.e. $L\;---\;M$ épi.

$G$ est une extension centrale de $A\times M$ par $\mathfrak z$, et est connu (comme
telle, avec reconstitution du diagramme (D)) par la connaissance
des deux extensions centrales $L$ de $M$ par $\mathfrak z$ et $Z$ de $A$ par $\mathfrak z$.
Donc la donnée de $G$ \deleted{\unsure{(avec sa décomposition}} \inserted{(satisfaisant l'hyp. du} début équi-
vaut à celle de

a) des groupes alg. $M,A,\mathfrak z$ ($M$ affine lisse connexe, $A$ V.A., $\mathfrak z$ \inserted{affine} commutatif)

b) d'extensions centrales $L$ de $M$ par $\mathfrak z$, et $Z$ de $A$ par $\mathfrak z$, satisfaisant

(i) $L$ lisse connexe,\quad (ii) $Z_{\mathrm{aff}}=1$

On peut reformuler ces données en

a') groupe alg. affine lisse connexe $L^{\unsure{*}}$, et V.A. $A$

b') ss-groupe \inserted{alg.} $\mathfrak z\subset\operatorname{Cent}(L)$

c') Extension \deleted{\unsure{de}} \inserted{centrale} $Z$ de $A$ par $\mathfrak z$ telle que $Z_{\mathrm{aff}}=1$.

On sait déterminer les ext. centrales d'un schéma abélien $A$
par un groupe \inserted{alg.} comm. affine $\mathfrak z$ par
\[
\operatorname{Ext}^1(A,\mathfrak z)=\operatorname{Hom}(D(\mathfrak z),\uline{\operatorname{Pic}}_{A/k})
\]
(la catégorie de ces extensions est rigide puisque le
$\operatorname{Ext}^0=\operatorname{Hom}(A,\mathfrak z)=0$) donc la donnée \deleted{de} \inserted{d'une extension} $Z$ équivaut à
la donnée de
\[\varphi:D(\mathfrak z)\longrightarrow\uline{\operatorname{Pic}}_{A/k}\]
et il reste à expliciter la condition $Z_{\mathrm{aff}}=1$, \deleted{\unsure{par suite}} \inserted{(plus gén.}
\mspage{41}
""",'text',[('text','top','G groupe alg. lisse connexe'),('diagram','upper','1 L G A 1'),('text','upper','Considérons de plus M=Gaff'),('diagram','upper','1 Z G M 1'),('text','upper-middle','on sait que M affine'),('diagram','middle','D L intersection Z L Z G M A'),('text','middle','avec Z to A épi'),('text','middle','G est une extension centrale'),('text','middle-lower','Donc la donnée de G'),('text','lower-middle','a) des groupes alg.'),('text','lower-middle','b) d’extensions centrales'),('text','lower-middle','On peut reformuler'),('text','lower','a prime groupe alg. affine'),('text','lower','b prime ss-groupe'),('text','lower','c prime Extension centrale'),('text','lower','On sait déterminer'),('display','lower','Ext1(A,z)=Hom(D(z),Pic)'),('text','bottom','la catégorie de ces extensions'),('display','bottom','phi D(z) to Pic'),('text','bottom edge','et il reste à expliciter'),('marginalia','bottom-left','41')],doubts=[('first sequence','A superscript ab','Small superscript is heavily retraced; retained as uncertain rather than removed.','medium'),('middle substitution','with its decomposition','Cancelled phrase is only partially separable from the replacement; exact wording uncertain.','low')],observations='Chevalley extension of a smooth connected algebraic group and its maximal affine quotient. Z is central and has Zaff=1. Data via two central extensions by z=L∩Z and Cartier-dual/Picard classification Ext1(A,z)=Hom(D(z),Pic_A/k). Anti-affine interpretation should be researched only after freeze; source uses Zaff=1, not the modern term.')
