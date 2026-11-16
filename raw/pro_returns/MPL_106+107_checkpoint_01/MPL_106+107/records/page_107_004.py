import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{a}
\deleted{\((A\times B)^\wedge\simeq\underline{\mathrm{Hom}}(A^o,B^\wedge)\simeq\underline{\mathrm{Hom}}(B^o,A^\wedge)\).}
\diagram{\begin{tikzcd}&A\times B\arrow[dl,"p_B"']\arrow[dr,"p_A"]&\\A\arrow[dr,"q_A"']&&B\arrow[dl,no head,"q_B"]\\&e&\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=small]
\underline{\mathrm{Hom}}(A^o,B^\wedge)\arrow[r,phantom,"\simeq"]\arrow[dd,"X'\mapsto\Gamma_B\circ X'"']&(A\times B)^\wedge\arrow[r,phantom,"\simeq"]\arrow[ddl,"(p_B)_*"']\arrow[ddr,"(p_A)_*"]&\underline{\mathrm{Hom}}(B^o,A^\wedge)\arrow[r]\arrow[dd,"X''\mapsto\Gamma_A\circ X''"]&[\underline{\mathrm{Hom}}(B^o,A)]\\
&&&\\
\underline{\mathrm{Hom}}(A^o,(\mathrm{Ens}))\simeq A^\wedge\arrow[dr,"\deleted{\unsure{p_A}}q_{A*}=\Gamma_A=\underline{\mathrm{Hom}}_A(e_{A^\wedge},\cdot)"']&&B^\wedge=\underline{\mathrm{Hom}}(B^o,(\mathrm{Ens}))\arrow[dl,"q_{B*}=\Gamma_B=\underline{\mathrm{Hom}}_B(e_{B^\wedge},\cdot)"]&\\
&(\mathrm{Ens})&&
\end{tikzcd}}
\margin{\[
\begin{aligned}
\underline{\mathrm{Hom}}_B(X,Y)&\overset{\mathrm{def}}=p_{A*}\underline{\mathrm{Hom}}_{A\times B}(X,Y)\\
\underline{\mathrm{Hom}}_A(X,Y)&\overset{\mathrm{def}}=p_{B*}\underline{\mathrm{Hom}}_{A\times B}(X,Y)
\end{aligned}
\]
\deleted{\(\unsure{\mathrm{Hom}(X,Y)=}\)} donc
\[\mathrm{Hom}(X,Y)\simeq\Gamma_{\unsure{A|B}}\underline{\mathrm{Hom}}_A(X,Y)\simeq\Gamma_B\underline{\mathrm{Hom}}_B(X,Y).\]}
\(A\) et \(B\) deux petites catégories.

on travaille dans \((A\times B)^\wedge\simeq\underline{\mathrm{Hom}}(A^o,B^\wedge)\simeq\underline{\mathrm{Hom}}(B^o,A^\wedge)\). On a indiqué sur le diagramme ci-dessus \unsure{qques} propriétés des foncteurs images directes. Pour \(b\in B\), on a un foncteur
\diagram{\begin{tikzcd}
\deleted{\unsure{q_b}}\Gamma_b'':(A\times B)^\wedge\arrow[r,Rightarrow]\arrow[d]&\unsure{A^\wedge}\arrow[d,phantom,"\parallel"]\\
\deleted{\unsure{\simeq}}\underline{\mathrm{Hom}}(B^o,A^\wedge)\arrow[r,no head]&\unsure{A^\wedge}\\
X''\arrow[r,mapsto]&X''(b)\deleted{\unsure{\simeq\mathrm{Hom}}}
\end{tikzcd}}
induit par \((A\times B)^\wedge\simeq\underline{\mathrm{Hom}}(A^o,\unsure{B})\)
\margin{\(\unsure{\downarrow}\)}
Je dis qu'on a
\[
\Gamma_b''(X)\simeq p_{\unsure{B|A}*}\underline{\mathrm{Hom}}(p_{\unsure{A|B}}^*(b),X)\qquad\text{fonctoriel en }b,X
\]
\[
(=\underline{\mathrm{Hom}}_A(p_A^*(b),X));
\]
ce qui signifie aussi qu'on a
\diagram{\begin{tikzcd}[column sep=large]
\mathrm{Hom}_{\unsure{B^\wedge|A^\wedge}}(\unsure{a|b},\Gamma_b''(X))\arrow[r,phantom,"\simeq"]\arrow[d,phantom,"\parallel"]&\mathrm{Hom}_{A^\wedge}(\unsure{a|b},p_{\unsure{B|A}*}\underline{\mathrm{Hom}}(p_A^*(b),X))\arrow[d,phantom,"\wr"]\\
X(a,b)&\mathrm{Hom}_{(A\times B)^\wedge}(p_B^*(a),\underline{\mathrm{Hom}}(p_A^*(b),X))\arrow[d,phantom,"\wr"]\\
&\mathrm{Hom}_{(A\times B)^\wedge}(p_B^*(a)\times p_A^*(b),X)
\end{tikzcd}}
\margin{fonctoriel en \(a,X,b\)\qquad OK}
\deleted{Symétriquement, on a des \(\Gamma_a'\), \(a\in A\)
\diagram{\begin{tikzcd}
\Gamma_a':(A\times B)^\wedge\arrow[r]\arrow[d,phantom,"\wr"]&B^\wedge\\
\underline{\mathrm{Hom}}(A^o,B^\wedge)&\\
X'\arrow[r,mapsto]&X'(a)
\end{tikzcd}}
et on a
\[
\Gamma_a'(X)\simeq p_{A*}(\underline{\mathrm{Hom}}(p_B^*(a),X))
\]}
\mspage{3}
"""
elements=[('text','top','a'),('diagram','upper left','A×B; A; B; e'),('diagram','upper centre','Hom(A^o,B^hat); (A×B)^hat; Hom(B^o,A^hat); direct images'),('display','upper right','definitions Hom_B, Hom_A'),('text','middle','A et B deux petites catégories'),('text','middle','on travaille dans'),('diagram','middle','Γ_b double prime; evaluation'),('text','middle right','induit par'),('text','lower middle','Je dis qu’on a'),('display','lower middle','Γ_b double prime(X)≃p_B*Hom'),('display','lower middle','(=Hom_A(p_A*(b),X))'),('text','lower middle','ce qui signifie aussi'),('diagram','lower','Hom identifications; X(a,b)'),('text','bottom','Symétriquement'),('diagram','bottom','Γ_a prime; X′↦X′(a)'),('display','bottom','Γ_a prime(X)≃p_A*Hom'),('text','foot','3')]
if __name__=='__main__':save(107,4,tex,elements,notes='Defines relative internal Hom for A×B and gives evaluation formula Γ_b″(X)≃p_B*Hom(p_A*b,X), then a Yoneda/adjunction chain ending “OK”. The symmetric Γ_a′ paragraph is diagonally cancelled. Several A/B overwrites and a displayed Hom(A^o,B) remain literal or doubtful. Top label a, foot 3. Strong distinction between cancellation and validation needed in research notes.')
