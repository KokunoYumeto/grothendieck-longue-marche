import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\diagram{\begin{tikzcd}
& A\times\Delta\arrow[dl,"p_\Delta"']\arrow[dr,"p_A"] &\\
A\arrow[dr,"q_A"'] &&\Delta\arrow[dl,"q_\Delta"]\\
&e&
\end{tikzcd}}
\deleted{
\[
X_*,Y_*\in\mathrm{Ob}\underbrace{(A\times\Delta)^\wedge}_{\simeq\underline{\mathrm{Hom}}(\Delta^o,A^\wedge)\simeq\mathrm{Hom}(A^o,\Delta^\wedge)}
\]
\[
\left\{\begin{aligned}
\mathrm{Hom}_{A\times\Delta}(X_*,Y_*)&=\Gamma_{A\times\Delta}(\underline{\mathrm{Hom}}_{A\times\Delta}(X_*,Y_*))\\
\underline{\mathrm{Hom}}_A(X_*,Y_*)&=p_{\Delta*}\underline{\mathrm{Hom}}_{A\times\Delta}(X_*,Y_*)\\
\underline{\mathrm{Hom}}_\Delta(X_*,Y_*)&=p_{A*}\underline{\mathrm{Hom}}_{A\times\Delta}(X_*,Y_*)
\end{aligned}\right.
\]
\margin{\[
\left\{\begin{aligned}p_{A*}\deleted{\unsure{Y}}X_*&=(\Gamma_A X_n)_n\\p_{\Delta*}X_*&=X_0\end{aligned}\right.
\]
\[(q_\Delta p_A)_*(X_*)=(q_Ap_\Delta)_*X_*=\Gamma_A\unsure{X_0}\]
\figure{\begin{tikzpicture}\draw (0,3)--(1,1.5)--(2.1,.3)--(4.4,.5);\end{tikzpicture}}}
}
\margin{\deleted{\unsure{\mathrm{Hom}}}
\diagram{\begin{tikzcd}
&(A\times\Delta)^\wedge\supset s\underline A=\underline{\mathrm{Hom}}(\Delta^o,A)\arrow[dl,"p_{\Delta*}"']\arrow[dr,"p_{A*}"]&\\
A^\wedge\arrow[dr,"q_{A*}"']&&\Delta^\wedge\arrow[dl,"q_{\Delta*}"]\\
&(\mathrm{Ens})&
\end{tikzcd}}}
\deleted{
\deleted{\unsure{A}} \unsure{What about}
\[
(\underline{\mathrm{Hom}}_A(L,X_n))_n\overset{?}{\in}(A\times\Delta)^\wedge
\]
\[
(\mathrm{Hom}_A(L,X_n))_n\in\Delta^\wedge
\]
for given \(L\in\mathrm{Ob}A^\wedge\) (more generally, \unsure{\(L\in\mathrm{Ob}A^\wedge\)} ?)
the second is the transform of the first by \(p_{A*}\) (\(=\Gamma_A\) applied componentwise).

I contend that if we identify \(L\) with the constant \unsure{complex with value} \(L\), i.e. with \(p_\Delta^*(L)\), we get
\[
(\underline{\mathrm{Hom}}_A(L,X_n))_{n\in\mathbb N}=\underline{\mathrm{Hom}}_{A\times\Delta}(p_\Delta^*(L),X_*)
\]
\margin{hence, by applying \deleted{\unsure{\Gamma_A}} \(p_{A*}\)}
\[
(\mathrm{Hom}_A(L,X_n))_{n\in\mathbb N}=\underline{\mathrm{Hom}}_\Delta(p_\Delta^*(L),X_*)
\]
To get the first one, we apply the definition of \(\underline{\mathrm{Hom}}\), we have to get the \(n^{\mathrm{th}}\) component of the \unsure{second hand side}; \deleted{\unsure{we}} This is easily checked (see below) to be
}
\margin{\(A\)
\diagram{\begin{tikzcd}a_0\arrow[r,leftrightarrow]&a\end{tikzcd}}
\(i_0\in I\qquad I\)}
\margin{\(M(b)\qquad X(a,b)=M(b)\)
\diagram{\begin{tikzcd}
&\{i_0\}\arrow[d,Rightarrow]\\
\underline{\mathrm{Hom}}(\unsure{a|a_1},a_0)\arrow[ur]\arrow[r]&I\\
u\arrow[r,mapsto]&u(i_0)\deleted{\unsure{\varphi}}
\end{tikzcd}}}
\mspage{2}
"""
elements=[('diagram','upper left','A×Δ; A; Δ; e'),('display','upper centre','X_*,Y_*∈Ob(A×Δ)^hat'),('display','upper centre','Hom; three identities'),('display','upper right','p_A*X_*; p_Δ*X_*'),('display','upper right','(q_Δp_A)_*'),('drawing','upper right','three-segment border'),('text','left middle','(A×Δ)^hat⊃sA'),('diagram','left middle','presheaf categories; (Ens)'),('text','middle','What about'),('display','middle','(underlinedHom_A(L,X_n))_n'),('display','middle','(Hom_A(L,X_n))_n'),('text','middle','for given L'),('text','middle lower','I contend'),('display','lower','relative internal Hom identity'),('display','lower','relative Δ Hom identity'),('text','lower','To get the first one'),('diagram','left lower margin','a_0↔a'),('text','left lower margin','A; i_0∈I; I'),('display','bottom rotated margin','M(b); X(a,b)=M(b)'),('diagram','bottom rotated margin','Hom(a,a_0)→I; {i_0}; u↦u(i_0)'),('text','foot','2')]
if __name__=='__main__':save(107,3,tex,elements,kind='cancelled_draft',notes='Cancelled draft on relative Hom in (A×Δ)^hat. Central question and claim identify degreewise internal Hom with internal Hom out of p_Δ^*L, then apply p_A*. Final verification stops after “This is easily checked (see below) to be”. Several English phrases and the parenthesis at the right edge are doubtful. The two projection diamonds and rotated marginal calculation remain separately represented. Compare later pages only after reading them; no context used.')
