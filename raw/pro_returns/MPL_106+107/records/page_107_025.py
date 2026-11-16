import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from save_page import save
tex=r"""
\figure{\begin{tikzpicture}\node[draw,ellipse] {$\mspage{d}$};\end{tikzpicture}}
Returning to our initial pb, we get
\[
\deleted{\unsure{\lim}}\operatorname{Hom}(X_\infty,Y)\mathbin{-}\varprojlim\operatorname{Hom}(X_i,Y)
\]
\uline{surjective} (using strongly that the transition morphisms $X_i\mathbin{-}X_{i+1}$ are cofibrations). To prove it injective, let
\[
f,f':X_\infty\longrightarrow Y\qquad f_i=f|X_i,\quad f'_i=f'|X_i
\]
we have to prove that $f_i\sim f'_i\quad\forall i$, implies $f\sim f'$.

Consider
\diagram{\begin{tikzcd}[column sep=large]
\underbrace{X_\infty\times\Delta^{(1)}}_{B}\underset{\mathrm{cofib.}}{\supset}\underbrace{X_\infty\amalg X_\infty}_{A} \arrow[d,-,sloped,"(f,f')"]\\
Y
\end{tikzcd}}
we want to extend to $X_\infty\times\Delta(1)$, and we know it is possible upon $X_i\times\Delta(1)\quad\forall i$.
\diagram{\begin{tikzcd}[column sep=small]
B & \supset & A\\
\vdots & & \vdots\\
B_{i+1} \arrow[d,"\mathrm{cofib}"'] & \supset & A_{i+1}\arrow[d,"\mathrm{cofib}"]\\
B_i & \underset{\mathrm{cofib.}}{\supset} & A_i
\end{tikzcd}}
We have to extend stepwise given homotopies. The problem is to construct $h_{i+1}$ extending $h'_{i+1}$
\figure{\begin{tikzpicture}\draw[->] (0,.6)--(.1,0);\end{tikzpicture}}
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
A_i \arrow[r,hook,-] \arrow[d,hook] \arrow[dd,bend right=35,"\unsure{\varphi_i|\psi_i}"'] & B_i \arrow[d,hook] & \\
A_{i+1} \arrow[r,hook,-,""{name=s}] \arrow[d,"\varphi_{i+1}"'] & B'_{i+1}\arrow[r,hook,-] \arrow[dl,"h'_{i+1}"] & B_{i+1}\arrow[dll,dashed,bend left=15,"h_{\unsure{i-1|i+1}}?"]\\
Y' & &
\arrow[from=s,to=1-2]
\end{tikzcd}}
\[
\unsure{h'\!\!\!/}\qquad=B_i\amalg_{A_i}A_{\unsure{i-1|i+1}}
\]
\deleted{\diagram{\begin{tikzcd}& {}\arrow[dl,bend left=10,"\unsure{h?}"]\arrow[dl,bend right=10]\\{}&\end{tikzcd}}}
\figure{\begin{tikzpicture}\draw (0,0)--(.9,.7)--(.15,.2)--(1,1)--(.1,.1)--(.7,.7);\end{tikzpicture}}
\diagram{\begin{array}{c}
\Delta(1)\times X_{i+1}\\
\cup\\
(\Delta(1)\times X_i)\cup(\{0\}\times X_{i+1})\cup(\{1\}\times X_{\unsure{i-1|i+1}})
\end{array}}
\diagram{\begin{tikzcd}
Y\arrow[r,hook,-,shift left=.6pt]\arrow[r,-,shift right=.6pt]&Z_0\arrow[r,hook,-]&Z_1\arrow[r,hook,-]&Z_2\mathbin{\cdots-}
\end{tikzcd}}
Assume $\forall i$, $\exists$ retraction $Z_i\mathbin{-}Y$

Is there a retraction $Z_\infty\longrightarrow Y$?

\uline{not clear at all}, \unsure{our|or} \deleted{\unsure{contrary}} the whole point is to see that
\[
\varprojlim_i\pi_0\underline{\operatorname{Retr}}(\unsure{Z|Z_i},Y)\ne\varnothing.\mathbin{-}
\]
Ask Ronnie Brown!
\mspage{24}
"""
elements=[('text','top','circled d; Returning to our initial pb'),('display','top','Hom(X∞,Y)−lim← Hom(Xi,Y)'),('text','upper','surjective (using strongly'),('display','upper middle','f,f′:X∞→Y; fi=f|Xi; f′i=f′|Xi'),('text','upper middle','we have to prove'),('diagram','middle','X∞×Δ(1) ⊃ X∞ amalg X∞; (f,f′) to Y'),('text','middle right','we want to extend'),('diagram','middle left','B⊃A; Bi+1⊃Ai+1 down to Bi⊃Ai'),('text','middle','We have to extend stepwise given homotopies'),('drawing','middle left','short downward arrow'),('diagram','lower middle','Ai,Bi,Ai+1,B′i+1,Bi+1,Y′'),('display','under B′i+1','=Bi amalg_Ai Ai−1/i+1; cancelled trial label'),('diagram','right of pushout sketch','cancelled repeated arrows'),('drawing','right of pushout sketch','zigzag cancellation'),('display','lower left','Δ(1)×Xi+1; vertical cup; threefold union'),('diagram','lower right','Y,Z0,Z1,Z2'),('text','lower right','Assume ∀i ∃ retraction'),('text','lower right','Is there a retraction Z∞→Y?'),('text','bottom','not clear at all'),('display','bottom','lim← π0 Retr(Z,Y) ≠∅'),('text','bottom','Ask Ronnie Brown!'),('text','bottom left','24')]
if __name__=='__main__':save(107,25,tex,elements,'text',notes='Surjectivity claimed on returning to initial problem, with strong use of cofibration transitions. Injectivity reduced to extending homotopies coherently, then to a tower of retractions. Explicit questions: h_{i+1}? and “Is there a retraction Z∞→Y?”; “not clear at all” and “Ask Ronnie Brown!” leave the issue unresolved. lim← π0 Retr nonemptiness displayed as the whole point; never promote to proven. Investigate phantom-map/lim^1 obstruction only after freeze. Lower indices and initial deleted lim, last struck word are particularly uncertain.')
