import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(52,r'''
\scanpage{52}
% archive foliation: 51
\[
\underbrace{\Omega(\mathbf R^{n-1},\mathbf R^n)}_{1}\wedge\Omega(\mathbf R^n)\longrightarrow\Omega(\mathbf R^{n-1})\qquad\text{i.e.}
\]
\inserted{on choisit $\mathbf R^{n-1}\times\mathbf R^+$ comme $1/2$ espace de $\mathbf R^n$}
\[
\omega_n\xrightarrow{\sim}\omega_{n-1}
\]
compatible avec $\operatorname{Aut}(\mathbf R^{n-1},\mathbf R^n)={}$ssgrpe de $\mathrm{GL}(n,\mathbf R)$ des matrices
\[
u_n:=\deleted{\unsure{\left(\begin{array}{c|c}u_{n-1}&\vdots\\\hline0&\lambda\end{array}\right)}}
\left(\begin{array}{c|c}
\begin{array}{c@{}c}\scriptstyle n-1\left\{\vphantom{\begin{matrix}a\\b\end{matrix}}\right.&\overbrace{u_{n-1}}^{n-1}\end{array}&\begin{matrix}\bullet\\\vdots\\\bullet\end{matrix}\\\hline
0\qquad0&\lambda
\end{array}\right)
\]
opérant sur $\omega_{n-1}$ par $\deleted{\unsure{\operatorname{sg}\det}}\varepsilon_{n-1}(u_{n-1})$, sur $\omega_n$ par $(\deleted{\unsure{\operatorname{sg}\det}}\inserted{\varepsilon_n}(u_n).\operatorname{sg}\lambda)\deleted{=\unsure{\operatorname{sg}\det u_{n-1}}}$
\[
\deleted{\unsure{\varepsilon_{n-1}(u_{n-1})}}
\]
\inserted{condition que l'application}
\[
\boxed{\varepsilon_n(u_n)=\operatorname{sg}(\lambda)\varepsilon_{n-1}(u_{n-1})}.
\]
\deleted{qui est donc \unsure{une condt satisfaite !}}

\deleted{Donc la donnée d'une théorie de \unsure{l'ori.} équivaut à la donnée de
\[
\left\{\begin{array}{ll}
(\varepsilon_n)_{n\in\mathbf N},&\text{où }\varepsilon_n:G_n\longrightarrow\{\pm1\}\\
(\unsure{s_n|\xi_n})_{n\in\mathbf N^*},&\text{où }\unsure{s_n|\xi_n}:\omega_n\xrightarrow{\sim}\omega_{n-1}
\end{array}\right\}
\]
(les iso $\omega_n\simeq\omega_{n-1}$, et $\omega_0\simeq\{\pm1\}$, donnent $\omega_n\simeq\{\pm1\}$)}

Ceci détermine $\varepsilon_1:\mathbf R^*\longrightarrow\{\pm1\}$ par
\[
\varepsilon_1=\operatorname{sg}:\mathbf R^*\longrightarrow\{\pm1\}
\]
et pr \unsure{dim|des} plus gén., par récurrence
\[
\varepsilon_n(u)=\operatorname{sg}\circ\det(u)\qquad u\in\mathrm{GL}(n,\mathbf R)
\]

\deleted{\illegible{1}}
\figure{\begin{tikzpicture}\draw (0,0)--(.75,0);\draw (.08,-.12)--(.75,-.12);\end{tikzpicture}}
''',[
('display','top','Omega(R^(n-1),R^n) wedge Omega(R^n) to Omega(R^(n-1)); first factor brace 1'),
('insertion','left linked to first factor','on choisit R^(n-1) x R+ comme 1/2 espace'),
('display','top','omega_n isomorphism omega_(n-1)'),
('text','upper','compatible avec Aut(R^(n-1),R^n)'),
('display','upper','u_n block matrix with n-1 braces and last entry lambda'),
('deletion','first version of matrix','block matrix'),
('text','upper-middle','opérant sur omega_(n-1) par epsilon_(n-1)'),
('deletion','before epsilon_(n-1)','sg det'),
('deletion','before inserted epsilon_n','sg det'),
('insertion','above cancelled sg det','epsilon_n'),
('deletion','after sg lambda','= sg det u_(n-1)'),
('deletion','under overwritten coefficient','epsilon_(n-1)(u_(n-1))'),
('insertion','above boxed equality','condition que lapplication'),
('display','upper-middle boxed','epsilon_n(u_n)=sg(lambda)epsilon_(n-1)(u_(n-1))'),
('deletion','under coefficients','qui est donc une condt satisfaite!'),
('deletion','large crossed paragraph','Donc la donnée dune théorie... equivaut à la donnée de'),
('display','inside crossed paragraph','epsilon_n:G_n to {+/-1}; s_n:omega_n isomorphism omega_(n-1)'),
('deletion','bottom of crossed paragraph','les iso omega_n isomorphic omega_(n-1) ... donnent omega_n isomorphic {+/-1}'),
('text','below crossed paragraph','Ceci détermine epsilon_1 par'),
('display','lower','epsilon_1=sg:R* to {+/-1}'),
('text','lower','et pr dim plus gén par récurrence'),
('display','lower','epsilon_n(u)=sg o det(u), u in GL(n,R)'),
('deletion','bottom left of writing','one obliterated word'),
('drawing','bottom of writing centre','two horizontal end strokes')
],[
('cancelled first matrix','block u_(n-1), zeros and lambda','original entries are mostly obliterated; matrix outline visible','low'),
('overworked coefficients below matrix','sg det; epsilon_n; epsilon_(n-1)(u_(n-1))','several layers of cancellation and replacement','low'),
('cancelled line before large box','qui est donc une condt satisfaite!','end of phrase largely intersected by border and overstrike','low'),
('large crossed paragraph first line','lori.','compressed abbreviation after théorie de','low'),
('large crossed paragraph isomorphism name','s_n','xi_n; curved symbol with a top dot-like stroke','low'),
('before par récurrence','dim plus gén.','des plus gén.','medium'),
('last cancelled word','illegible 1','Vérifier considered but no defensible complete letter sequence after enlargement','low')])
