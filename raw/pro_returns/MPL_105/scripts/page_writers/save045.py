import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{45}
\mspage{7}

On a aussi
\[U\simeq\unsure{X}_{/a},\quad U'=X_{/b},\quad U\cap U'=X_{/0}.\]
Ainsi le diagramme dans $\mathrm{Cat}$
\[(6)\qquad\diagram{\begin{tikzcd} & U\\ U\cap U'\arrow[ur,"i'_0"]\arrow[dr,"i_0"'] & \\ & U'\end{tikzcd}}\]
du type $\underline\Psi$ n'est-il autre que le foncteur $\underline\Psi\longrightarrow\mathrm{Cat}$ qui définit la cat. \inserted{cofibrée scindée} $\Psi(X/\underline\psi)=\overline X$ sur $\Psi$
\[\diagram{\begin{tikzcd}X\arrow[rr,"\alpha"]\arrow[dr,no head,"\varphi"']&&\overline X\arrow[dl,no head,"\overline\varphi"]\\&\underline\Psi&\end{tikzcd}}\qquad\alpha\in W^{\unsure{g}}_{\underline\Psi}\]
\[U=\overline X_a,\quad U'=\overline X_b,\quad U\cap U'=\overline X_0,\]
les foncteurs $i'_0,i_0$ de (6) étant les foncteurs changement de base relatifs à
\[0\xrightarrow{\underline{i}'_0}a\quad\text{et}\quad0\xrightarrow{\underline{i}_0}b.\qquad\deleted{\text{D'autre}}\]
D'autre part $\overline\varphi$ est \uline{propre}, donc $\overline\varphi_*$ se calcule \unsure{en fibres|fibre} par \unsure{fibres}, en particulier, pour coeff. const. $\xi_{\overline X}$, avec $\xi\in\mathcal A$
\[\overline\varphi_*(\xi_{\overline X})(s)=\begin{cases}H^{\unsure{\bullet}}_{\underline D}(U\cap U',\xi)&\text{si }s=0\\H^{\unsure{\bullet}}_{\underline D}(U,\xi)\deleted{\unsure{*}}&\text{si }s=a\\H^{\unsure{\bullet}}_{\underline D}(U',\xi)&\text{si }s=b.\end{cases}\]
\mspage{44}
'''
e=[('text','top','7'),('text','top','On a aussi'),('display','top','U ≃ X/a'),('text','upper','Ainsi le diagramme'),('diagram','upper','(6) U intersection U prime'),('text','middle','du type Ψ'),('insertion','middle','cofibrée scindée'),('diagram','middle','X alpha Xbar over Ψ'),('display','middle right','alpha in W'),('display','lower middle','U=Xbar a'),('text','lower','les foncteurs'),('display','lower','0 to a et 0 to b'),('deletion','lower right',"D'autre"),('text','lower',"D'autre part"),('display','bottom','phibar star xi'),('deletion','bottom display second branch','star'),('text','bottom','44')]
record_page(45,s,e,notes='No arrowheads on triangle legs. Fibres phrase and W superscript uncertain; H superscript appears a heavy dot. Distinguish underlined capital Ψ and lower ψ as ink suggests.')
build_doubts()
