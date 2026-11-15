import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(34,r'''\scanpage{34}
\mspage{5}
(iii) \uline{The} \uline{space} $Y$ \uline{can} \uline{be} \uline{written} \uline{as} \uline{a} \uline{direct} \uline{sum}
\[
Y=Y_1\oplus Y_0,
\]
\uline{where}
\[
\begin{aligned}
Y_1&=\{y\in Y:y\text{ is a T-fixed point}\}\\
&=\theta(Y)
\end{aligned}
\]
\uline{and}
\[
\begin{aligned}
Y_0&=\{y\in Y:0\in\unsure{\mathcal O|O}(y)\}\\
&=\text{kernel of }\theta.
\end{aligned}
\]

PROOF. The assumption that each $\unsure{\mathcal O|O}(y)$ is weakly compact insures that the weak operator closure $S$ of $T$ in $B(Y)$ is compact in the weak operator topology. Moreover, $\unsure{\mathcal O|O}(y)=\{s(y):s\in S\}$ for every $y$ in $Y$. By the lemma, $T$ converges in the weak operator topology to a zero $\theta$ for $S$. Since $t\circ\theta=\theta$ for all $t$ in $T$, $\theta(y)$ is T-fixed for any $y$. If $z$ is any T-fixed point in $\unsure{\mathcal O|\theta}(y)$, then $z=s(y)$ for some $s$ in $S$ and
\[
z=\theta(z)=\theta(s(y))=\theta(y).
\]
\margin{\unsure{;}}

Hence (i) and the first part of statement (ii) hold; (iii) follows trivially. It remains only to show that $T$ converges to $\theta$ in the strong operator topology.
\margin{33}
''','reused_typed',[
('text','top','(iii) The space Y can be written'),('display','upper','Y = Y_1 direct sum Y_0'),('text','upper middle','where'),('display','upper middle','Y_1 = fixed points = theta(Y)'),('text','middle','and'),('display','middle','Y_0 = kernel'),('text','lower half','PROOF. The assumption'),('display','lower','z = theta(z)'),('margin note','below last display','semicolon-like mark'),('text','bottom','Hence (i) and the first part'),('margin note','bottom of original orientation','33')
],[
('Y_0 display and proof, orbit notation','mathcal O(y)','O(y)','medium','Hand-filled oval O differs from the typewriter alphabet; script versus plain form not fully decisive.'),
('proof, T-fixed point in ...','mathcal O(y)','theta(y)','low','An overwritten or overtyped character retains a horizontal bar; the top stroke suggests a replacement O.'),
('below z display',';','ink artifact','low','Isolated two-part black mark; preserved because its intended status cannot be decided from the scan.')
])
