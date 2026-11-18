import sys
sys.path.insert(0,'MPL_159/scripts')
from record_page import commit
commit(31,r'''\scanpage{31}
\[
\begin{aligned}
C(\omega^u)&=\deleted{\unsure{\omega+\omega}}\ C\omega+\sum_{i\geq2}C(\omega)u_i+\omega C(u_i)\\
&=C(\omega)(1+\sum_{i\geq2}u_i)+\omega\sum C(u_i).
\end{aligned}
\]
\deleted{Prenons}
\[
C\upharpoonright\Omega:\quad\Omega\xrightarrow{C}\widehat S\otimes\Omega^1_{X/S}
\qquad C(\omega)=\unsure{\varpi_1+\omega\varpi_0+\varpi_1}.
\]
\[\Omega^{\otimes i}\]
\[
C(\lambda\omega^{\otimes i})=
\deleted{\omega^{\otimes i}\otimes d\lambda+\lambda i\omega^{\otimes(i-1)}}
\quad\underbrace{\omega^i\otimes d\lambda+\lambda i\omega^{i-1}(\unsure{\varpi_1+\omega\varpi_1})}.
\]
\[\omega=\lambda\omega_0\qquad u_i=\deleted{\unsure{\alpha_i\omega_0^i}}\alpha_i\omega_0^i.\]
\[
\begin{aligned}
C((\lambda\omega_0)^u)&=(\lambda\deleted{C(\omega)}\inserted{C(\omega_0)}+\omega_0\otimes d\lambda)(1+\sum_{i\geq2}\alpha_i\omega_0^i)\\
&\quad+\lambda\omega_0\sum_{i\geq2}(\omega_0^i\otimes d\alpha_i+i\alpha_i\omega_0^{i-1}C(\omega_0)).
\end{aligned}
\]
\[
C(\omega_0)=\deleted{\unsure{\varpi_0+\varpi_1+\varpi_2}}
\inserted{\unsure{\varpi_0|\bar\omega_0}+\omega_0\unsure{\varpi_1|\bar\omega_1}+\omega_0^2\unsure{\varpi_2|\bar\omega_2}}
\qquad\unsure{\varpi_i|\bar\omega_i}\in\deleted{\unsure{\Omega}}\ \Omega^1_{X/S}.
\]
\[
C(\deleted{\lambda}\omega_0^u)=\deleted{C(\omega_0)}(\unsure{\varpi_0+\varpi_1+\varpi_2})(1+\sum_{i\geq2}\alpha_i\omega_0^i+\sum_{i\geq2}i\alpha_i\omega_0^{\unsure{i|i-1}}).
\]
\[
\begin{aligned}
C(\omega_0^u)&=C(\omega_0(1+\sum_{i\geq2}\alpha_i\omega_0^i))\\
&=C(\omega_0)(1+\sum\alpha_i\omega_0^i)\\
&\quad+\omega_0\sum_{i\geq2}(\omega_0^i\otimes d\alpha_i+i\alpha_i\omega_0^{i-1}C(\omega_0))\\
&=C(\omega_0)(1+\sum_{i\geq2}(i+1)\alpha_i\omega_0^i)+\omega_0^3\sum_{i\geq2}\omega_0^{i-2}\otimes d\alpha_i\\
&=(\unsure{\varpi_0+\varpi_1+\varpi_2})(\qquad\text{''}\qquad)+\qquad\text{''}
\end{aligned}
\]
\[\deleted{\unsure{C(\omega_0^u)^{u^{-1}}=C(1+\sum_{i\geq2}}}\]
\[
\begin{aligned}
C(\omega_0^u)^{u^{-1}}&=\unsure{C(\omega_0)^{u^{-1}}}
\left(1+\sum_{i\geq2}(i+1)\alpha_i\left(\frac{\omega_0}{1+\sum\alpha_j\omega_0^j}\right)^i\right)\\
&\quad+\deleted{\omega_0}\sum_{i\geq2}\left(\frac{\omega_0}{1+\sum_{j\geq2}\alpha_j\omega_0^j}\right)^{i+1}\otimes d\alpha_i.
\end{aligned}
\]
\[
\deleted{C(\omega_0)^{u^{-1}}=\unsure{\varpi_0|\bar\omega_0}+\frac{\unsure{\varpi_1|\bar\omega_1}}{\unsure{1+\sum\alpha_j\omega_0^j}}+\omega_0^{u^{-1}}\unsure{\varpi_2|\bar\omega_2}}.
\]
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\node at (0.9,0) {$\unsure{!|?}$};\draw[->] (0,0.7)--(-0.2,-0.1);\draw[->] (1.8,0.7)--(-0.2,-0.1);\end{tikzpicture}}
% archive foliation: 30
''',[
 ('display','top','C(omega^u) expansion in u_i'),('deletion','first formula','omega+omega'),
 ('deletion','upper left','Prenons'),('display','upper third','C restricted to Omega'),('display','upper third right','C(omega) coefficient sketch'),
 ('display','isolated above calculation','Omega tensor i'),('display','upper middle','C(lambda omega tensor i)'),('deletion','upper middle calculation','omega tensor i d lambda'),
 ('display','middle left','omega=lambda omega_0; u_i=alpha_i omega_0^i'),('deletion','middle coefficient','alpha_i omega_0^i'),
 ('display','middle','C((lambda omega_0)^u)'),('deletion','middle product','C(omega)'),('insertion','above middle product','C(omega_0)'),
 ('display','middle lower','C(omega_0) coefficient expansion'),('deletion','middle lower','varpi_0+varpi_1+varpi_2'),('insertion','above coefficient expansion','varpi_0+omega_0 varpi_1+omega_0^2 varpi_2'),('deletion','coefficient membership','Omega'),
 ('display','below coefficients','C(omega_0^u) preliminary product'),('deletion','preliminary product argument','lambda'),('deletion','preliminary product RHS','C(omega_0)'),
 ('display','lower half','C(omega_0^u) full product differentiation'),('deletion','below expansion','C(omega_0^u) transformed unfinished'),
 ('display','lower quarter','C(omega_0^u)^{u inverse}'),('deletion','second line transformed formula','omega_0'),
 ('deletion','bottom','C(omega_0)^{u inverse} coefficient fraction'),('drawing','bottom under deleted fraction','two correction arrows and punctuation')
],observations='Formal coordinate change calculations, heavily cancelled. Coefficient glyph varpi/barred omega and overwritten expressions remain uncertain. The clean expansion has omega_0^3 times a sum with exponent i-2; it has been retained literally. No algebraic verification is claimed by the reading.')
