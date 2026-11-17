import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(36,r'''
\scanpage{36}
% archive foliation: 35
\uline{\unsure{Exponentielle|Exponentielles}} (en car. 0)

\margin{\deleted{\unsure{I)}}}
I) \uline{Généralités}

$A$ $\mathbf Q$-algèbre (ass. avec 1)

$N(A)$ ens des él. nilp. de $A$. On a donc $1+N(A)\subset A^*$ (ens des él. inv. de $A$)
\[
N(A)\xrightarrow{\exp}1+N(A)\qquad\exp x=\sum_{n\geq0}\frac{x^n}{n!}
\]
\uline{Th 1} 1) $\exp$ est bijective. L'application inverse est donnée par
\[
\log(1+y)=\sum_{n\geq1}(-1)^{n+1}\frac{y^n}{n}\qquad(y\in N(A))
\]
2) Si $x,y\in N(A)$ commutent, alors $x+y\in N(A)$ et
\[
\exp(x+y)=\exp x\ \exp y
\]
\margin{NB $\exp0=1$}
Si $u,v\in1+N(A)$ commutent, alors $uv\in1+N(A)$, et
\[
\log(uv)=\log u+\log v
\]
\margin{NB $\exp1=0$}
3) Soit $L\subset A$ un sous-$\mathbf Q$-espace vectoriel tel que $x\in L$, $n\in\mathbf N^*$ implique $x^n\in L$, \deleted{\unsure{Alors}} et $L$ formé d'éléments nilpotents. Alors
\[
x\longmapsto\exp x:\quad L\xrightarrow{\sim}1+L
\]
\uline{Remarque} Soit \deleted{\unsure{les conditions de 3), supposons que}} \inserted{$L\subset A$ un sous $\mathbf Q$-espace vectoriel de $A$} tel que $L\subset N(A)$, et tel que $x,y\in L\Rightarrow xy\in L$. Alors $L\xrightarrow{\sim}1+L$ par $3^\circ$, et de plus $1+L$ est un sous-groupe de $A^*$. D'où par transport de str une str. de groupe sur $L$. Elle est comm. \unsure{ssi|si} $L$ est commutative, i.e. si $x,y\in L\Rightarrow xy=yx$ --- \inserted{et dans ce cas cette structure est l'\uline{additive} de $L$.}
\margin{réciproque ? \unsure{par l'identité} \unsure{d'indéterminées} \unsure{voir} ---}

\uline{Exemple 1} Soient $K$ une $\mathbf Q$-alg. comm., $A$ une $K$-algèbre (ass. avec 1), $J$ un \deleted{\unsure{formé}} \inserted{nil} idéal de $K$. Alors $J.A$ satisfait les conditions de la Remarque, et on a donc
\[
JA\longrightarrow1+JA
\]
\uline{NB} Soient $K_0=K/J$, $A_0=A/JA=A\otimes_KK_0$, \inserted{$\unsure{\alpha_A|\alpha_U}:A\to A_0$ app. can.} Alors \deleted{\unsure{JA\longrightarrow}}
\[
JA=\{x\in A\mid\alpha_A(x)=0\},\qquad1+JA=\{x\in A\mid\alpha_A(x)=1\}
\]
\uline{Exemple 2} $K,J$ comme dans Exemple 1, \inserted{mais ici $J$ \uline{nilpotent},} $M$ un $K$-module,
\[
U=\operatorname{End}_K(M),\quad
\deleted{\unsure{U_0=U\otimes_KK_0\simeq U/JU}}\quad
\inserted{M_0=M\otimes_KK_0\simeq M/\unsure{JM}},
\]
$\alpha_M:M\longrightarrow M_0$ appl. can.; posons
\[
L=\{u\in U\unsure{=|:}\operatorname{End}_K(M)\mid u\otimes_KK_0=0\}
=\{u\in\unsure{U|M}\mid u(M)\subset JM\}
\]
alors
\[
1+L=\{u\in U=\operatorname{End}_K(M)\mid u\otimes_KK_0=\operatorname{id}_{M_0}\}.
\qquad\deleted{\unsure{L=\text{pos}}}
\]
Ceci posé, les conditions de la remarque sont satisfaites, donc on a
\[
\exp:L\xrightarrow{\sim}1+L
\]
''',[
('text','top title','Exponentielle (en car. 0)'),
('deletion','left of heading I','I) (doubtful)'),
('text','upper','I) Généralités; A Q-algèbre'),
('text','upper','N(A) ens des él. nilp.'),
('display','upper','N(A) exp arrow 1+N(A); exp series'),
('text','upper','Th 1 1) exp est bijective'),
('display','upper-middle','log(1+y) alternating series'),
('text','upper-middle','2) Si x,y in N(A) commutent'),
('display','upper-middle','exp(x+y)=exp x exp y'),
('margin note','right of exp identity','NB exp 0 = 1'),
('text','upper-middle','Si u,v in 1+N(A) commutent'),
('display','middle','log(uv)=log u+log v'),
('margin note','right of log identity','NB exp 1 = 0'),
('text','middle','3) Soit L subset A'),
('deletion','condition 3 after x^n in L','Alors'),
('display','middle','x maps to exp x: L isomorphism 1+L'),
('text','around fold','Remarque Soit; tel que L subset N(A)'),
('deletion','after Soit','les conditions de 3), supposons que'),
('insertion','above cancelled clause','L subset A un sous Q-espace vectoriel de A'),
('text','below fold','L isomorphism 1+L par 3°; Dou par transport'),
('insertion','between remark and example 1','et dans ce cas cette structure est ladditive de L'),
('margin note','slanting left of example 1','réciproque ? par lidentité (faint)'),
('text','lower-middle','Exemple 1 Soient K une Q-alg. comm.'),
('deletion','above idéal','formé'),
('insertion','before idéal','nil'),
('display','lower-middle','JA arrow 1+JA'),
('text','lower','NB Soient K_0=K/J, A_0=A/JA'),
('insertion','above Alors','alpha_A: A to A_0 app. can.'),
('deletion','right of Alors','JA arrow'),
('display','lower','JA zero fibre; 1+JA identity fibre'),
('text','lower','Exemple 2 K,J comme dans Exemple 1; M un K-module'),
('insertion','above M un K-module','mais ici J nilpotent'),
('display','near bottom','U=End_K(M)'),
('deletion','after End_K(M)','U_0=U tensor K_0 isomorphic U/JU'),
('insertion','above cancelled U_0 formula','M_0=M tensor K_0 isomorphic M/JM'),
('text','near bottom','alpha_M: M to M_0 appl. can.; posons; alors'),
('display','near bottom','L={u in U=End_K(M) | u tensor K_0=0}'),
('display','bottom','1+L={u in U=End_K(M) | u tensor K_0=id}'),
('deletion','right of 1+L display','L=pos'),
('text','bottom','Ceci posé, les conditions de la remarque'),
('display','bottom','exp: L isomorphism 1+L')
],[
('title','Exponentielle','Exponentielles; final stroke unclear','medium'),
('left of I)','I)','cancelled earlier heading','low'),
('condition 3 deletion','Alors','overwritten word','medium'),
('remark deletion','les conditions de 3), supposons que','cancelled clause; initial determiner uncertain','medium'),
('commutativity criterion','ssi','si; overtraced strokes','medium'),
('left marginal note after réciproque ?','par lidentité; dindéterminées; voir','very faint oblique writing; all three groups remain conjectural after enlarged inspection','low'),
('above idéal','formé','cancelled word; placement uncertain','low'),
('canonical algebra map subscript','alpha_A','alpha_U; subscript resembles u','medium'),
('NB cancelled fragment','JA arrow','endpoint absent / cancellation','low'),
('Exemple 2 deleted U_0 expression','U_0=U tensor_K K_0 isomorphic U/JU','heavily cancelled','low'),
('Exemple 2 inserted quotient','M/JM','J retraced, resembles circled symbol','medium'),
('L definition separator','equals','colon','medium'),
('second L set ambient letter','U','M; heavily retraced letter','low'),
('bottom cancellation','L=pos','fragment not fully recoverable','low')])
