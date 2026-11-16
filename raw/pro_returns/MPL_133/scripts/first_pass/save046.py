import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(46,r"""\scanpage{46}
\mspage{1}

I \quad $(N,M,d,\theta)=C$

\deleted{$\unsure{\theta:M\longrightarrow\operatorname{Aut}_{\mathrm{gr}}(N)}$}

\deleted{$\unsure{\beta:C'\longrightarrow C}$}

II \quad $(N',M',d',\theta')=C'_{\unsure{1}}$

III \quad $\textcircled{$\beta$}\left\{
\begin{array}{l}\pi_0(C)\simeq\pi_0(C'_{\unsure{1}})\\
\pi_1(C)\simeq\pi_1(C'_{\unsure{1}})
\end{array}\right.$ compatibles aux op. de $\pi_0$ sur $\pi_1$

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&N\cap N'=z=\pi_1\arrow[dl,dash]\arrow[dr,dash]&\\
N\arrow[dr,dash]\arrow[ddr,dash,bend right=50,"M'"']&&N'\arrow[dl,dash]\arrow[ddl,dash,bend left=50,"M"]\\
&NN'=H\arrow[d,dash]&\\
&G&
\end{tikzcd}}

problème de reconstitution pour $K=G/z\simeq\operatorname{Im}(G\to M\times M')$
et $H=\operatorname{Im}(N\times N'\to G)$

\diagram{\begin{tikzcd}[column sep=small]
& (N\times N'\underset{\unsure{z}}{\longrightarrow}G,D_1,\Theta_1)\arrow[dl]\arrow[dr]&\\
(N,M,d,\theta)\arrow[dr]&&(N',M',d',\theta')\arrow[dl]\\
&(G,M\times M',D_2,\Theta_2)&
\end{tikzcd}}
\[
(H,K,D,\Theta)
\]

\diagram{\begin{tikzcd}[column sep=small]
1\arrow[r,leftrightarrow]&z\arrow[r]&H&G\arrow[l,dash]
\end{tikzcd}}
\figure{\begin{tikzpicture}[x=.8cm,y=.35cm]
\draw (1,1)--(1,1.5)--(3,1.5)--(3,1);\draw(0,0)--(0,-.5)--(2,-.5)--(2,0);
\end{tikzpicture}}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
H\arrow[rrr,bend left=20]&N\times N'\arrow[l]\arrow[r]&M\times M'\arrow[d]&K\arrow[l]\arrow[d]\\
\pi_1\arrow[u]&\pi_1\times\pi_1\arrow[u]\arrow[l,"\mathrm{épi}"']&\pi_0\times\pi_0\arrow[r]&\pi_0
\end{tikzcd}}
\quad cocart \qquad cart
\[
(\alpha,\alpha').(\lambda,\lambda')=(\alpha.\lambda,\alpha'.\lambda')
\]
\[
(\alpha,\alpha').(\lambda,-\lambda)=(\alpha.\lambda,-\alpha'\lambda)
\]

Obstruction dans $H^3(B_{\pi_0}/X,\pi_1)$

Indétermination dans $\begin{array}{c}H^2(B_{\pi_0}/X,\pi_1)\\ \Vert\\ \operatorname{Ext}_{\mathrm{gr}}(\pi_0,\pi_1)\end{array}$

\hrulefill

\deleted{\unsure{A}}
\[
\left\{\begin{array}{l}
N'\text{ central}\ \inserted{\text{i.e. }N'\subset\operatorname{Cent}(G)}
\Longleftrightarrow\uline{\theta':M'\longrightarrow\operatorname{Aut}_{\mathrm{gr}}(N')\text{ triviale}}\quad(\text{d'où }N'\text{ commut})\\
N\text{ cocentral}\ \inserted{\text{i.e. }N\supset DG}\Longleftrightarrow M'\text{ commutatif}
\end{array}\right.
\]

L'ensemble des deux conditions signifie que
la donnée de $C'$ se réduit à la donnée
de groupes comm. $N'$ et $M'$ et un
hom
\[
N'\xrightarrow{d'}M'
\]
sans plus. Cela implique que l'opération
de $\pi'_0$ sur $\pi'_1$ est triviale, donc itou pour
$\pi_0$ sur $\pi_1$ (condition à mettre sur $C$)
ceci dit, la donnée de
\[
\boxed{\begin{array}{cc}N'\xrightarrow{d'}M'&d'(x')\text{ \uline{central}}\\&N'\text{ commutatif}\end{array}}
\]
pour \textcircled{A} est sans condition
de compatibilité supplémentaire

\margin{\deleted{Lieber \unsure{Edgar},\par
Wie die lieben Leute sich miteinander vergnügen --- ob allein, zu zwein, zu drei, zu \unsure{fünf} oder zu zwanzig}}
\margin{$\deleted{\unsure{H(\beta)}}$}
\mspage{45}
""",'text',[
('text','upper left','I (N,M,d,theta)=C'),('deletion','below I','theta:M; beta:C'),('display','upper left','II; III; pi_0,pi_1'),('diagram','upper right','N intersection N prime = z'),('text','upper right','problème de reconstitution'),('diagram','middle left','N times N prime; G; D_1'),('display','middle left lower','H,K,D,Theta'),('diagram','middle right top','1,z,H,G'),('drawing','around short diagram','two rectangular braces'),('diagram','middle right','H,N times N prime,M times M prime,K'),('display','middle right bottom','alpha,alpha prime action'),('text','below fold','Obstruction; Indétermination'),('deletion','above lower brace','A'),('display','lower third','N prime central; N cocentral'),('insertion','over central conditions','i.e. N prime subset Cent(G); N superset DG'),('text','lower third','L’ensemble des deux conditions'),('display','lower third','N prime d prime to M prime'),('text','bottom','sans plus. Cela implique'),('display','bottom box','N prime to M prime; d prime x prime central'),('text','bottom edge','pour A est sans condition'),('margin note','right margin rotated','Lieber Edgar'),('deletion','right margin','German paragraph; H(beta)'),('text','top and bottom folios','1;45')],doubts=[('top cancellations','theta:M to Aut(N); beta:C prime to C','Heavy crossing overwrites most letter bodies; formulas are tentative ink readings','low'),('tuple diamond','z below arrow','The small mark beneath the arrow may be a comma or z; no quotient inserted','low'),('German margin','zu fünf','The numeral-like word is crossed; retains a tentative written word','medium')],observations='Crossed-module reconstruction, H^3 obstruction and H^2 indeterminacy; central/cocentral specialization. Cancelled German personal wording on right margin.')
