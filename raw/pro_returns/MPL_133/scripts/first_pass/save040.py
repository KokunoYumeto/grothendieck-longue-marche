import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(40,r"""\scanpage{40}
\diagram{\begin{tikzcd}[row sep=small,column sep=small]
H&H_T\arrow[l]&H_T^i& W\supset W_i\\
\widehat G\arrow[d]&\widehat G_T\arrow[l]\arrow[d]&&\\
I&T\arrow[l]&W&\\
&T_i&&
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw[->] (4,1.6)--(4,0)--(0,0);\end{tikzpicture}}

\diagram{\begin{tikzcd}
1\arrow[r,dash]&H\arrow[r,dash]&E\arrow[r,dash]&G\arrow[r,dash]&1
\end{tikzcd}}
\[\varphi(x,y)\]
\[
\varphi(x,y)\deleted{\unsure{\varphi}}\,(\unsure{\varphi(y,x)|\varphi(x,y)})^{-1}=\unsure{\varphi_{x,y}|\varphi xy}
\]
\[\Psi(x+y)-\Psi(x)-\Psi(y)=\varphi(x,y)\]

\diagram{\begin{tikzcd}
1\arrow[r]&\widehat G_a\arrow[r,dash]\arrow[d,dash,"\unsure{\simeq}"]&E\arrow[r]&\widehat G_a\arrow[r,dash]&1\\
&Z(E)=D(E)&&&
\end{tikzcd}}
\[\unsure{H_a}\]

\diagram{\begin{tikzcd}
\deleted{\unsure{\widehat G}}\arrow[r,dash]&\unsure{G'}\\
\unsure{\mathfrak z} &
\end{tikzcd}}

\[
\begin{array}{cc}
[Z\longrightarrow A]&[Z\longrightarrow A]\\
\unsure{\simeq} &\unsure{\simeq}\\
[D\longrightarrow L]&\widehat{[D\longrightarrow L]}
\end{array}
\]

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&Z\arrow[r]&A\arrow[dr,"\unsure{?}"]&\\
\unsure{\pi_0|\pi_1}\arrow[ur,"\unsure{?}"]\arrow[dr,"\unsure{\sim}"']&&&\pi_0\\
&D\arrow[r]&L\arrow[ur,"?"']&
\end{tikzcd}}
\[ [\downarrow] \]
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&Z\arrow[r,dash]&A\arrow[dr,dash]&\\
\pi_1\arrow[ur,dash]\arrow[dr,dash]&&&\pi_0\\
&\widehat D\arrow[r,dash]&\widehat L\arrow[ur,dash]&
\end{tikzcd}}

\diagram{\begin{tikzcd}[row sep=small]
Z\arrow[r]&A\\
\widehat D\arrow[r]\arrow[u,phantom,"\unsure{\simeq}"]&\widehat L\arrow[u,phantom,"\unsure{\simeq}"]\\
Z\arrow[r,dash]&A\\
D\arrow[r,"0"']&L
\end{tikzcd}}

\[\deleted{\unsure{\Phi}(x,y)=}\]
\[
\uline{\Phi}(x,y)=\underbrace{\varphi(x,y)}_{\unsure{\varphi}}+
\underbrace{\Psi(x+y)-\Psi(x)-\Psi(y)}
\]
\[H^2(G_a,G_a)\]
\mspage{39}
""",'scratch',[('diagram','upper-left','H HT H superscript i'),('figure','upper-left long return arrow','long bent arrow'),('diagram','upper-middle','1 H E G 1'),('display','upper-middle','phi(x,y)'),('display','upper-right','phi(x,y) phi(y,x) inverse'),('display','upper-middle','Psi(x+y)-Psi(x)-Psi(y)'),('diagram','left-middle','1 Ga hat E Ga hat 1'),('display','left-middle','Z(E)=D(E)'),('diagram','centre cancelled','G G prime'),('display','lower-left','[Z to A] [D to L]'),('diagram','lower-left','pi Z A D L pi0'),('diagram','lower-middle','pi1 Z A Dhat Lhat pi0'),('diagram','upper-right','Z A Dhat Lhat D L'),('display','right cancellation','Phi(x,y)='),('display','lower-right','Phi=phi+Psi(x+y)'),('display','lower-right','H2(Ga,Ga)'),('marginalia','bottom-left','39')],doubts=[('central and lower diagrams','plain versus headed arrows','Only visible heads were added; uncertain equivalences and indices are marked.','medium'),('whole page','capital Psi and Phi','The large forks/loops are distinguished visually from the thinner phi.','medium')],observations='Scratch diagrams of extensions, a cocycle-like phi, additive coboundary Psi(x+y)-Psi(x)-Psi(y), and H2(Ga,Ga); several alternative diagrams compare [Z→A] and [D→L] with completions. No interpretation supplied to incomplete formulae.')
