from record import save
tex=r'''\scanpage{31}
\mspage{30}
\begin{center}-4.11-\end{center}
Now consider the skeleton $\Delta(T)$ in $\Delta(\overline{\mathrm{SL}(3)})$. It can be represented as the set of points on the circle
\[\begin{gathered}r_o+r_1+r_2=0\\r_o^2+r_1^2+r_2^2=6\end{gathered}\]
where the ratios of the $r_i$'s are rational. If $\ell_i$ is the line in $\mathbb P_2$ given by $x_i=0$, and if $P_i$ is the point in $\mathbb P_2$ with coordinates $x_j=\delta_{ij}$, then proceeding around this circle, the parabolic subgroups correspond to flags as indicated in Diagram 5. Furthermore, for a 1-PS $\lambda$ of $T$ as above, put:
\[\Vert\lambda\Vert=\sqrt{(r_o^2+r_1^2+r_2^2)/6}\]
The resulting function $\unsure{\nu|v}^{o(1)}(C,*)$ is indicated in Diagram 6, for some simple curves $C$.

\fbox{\S3.} In this section, we shall consider counter-examples. We would like to show how the reductive groups $\mathrm{SL}(n)$ can operate properly on \uline{quasi-projective} schemes $X$, simple over $\unsure{\mathbb Q|\mathbb C}$, but where there is \uline{no} geometric quotient of $X$ by $\mathrm{SL}(n)$; i.e, by Converse 1.12 and Proposition 0.7, there is no $L$ in $\mathrm{Pic}^G(X)$ such that $X=X^s(L)$. It should be emphasized that in any such case, there is an analytic space which is a quotient of the analytic space defined by $X$,by the analytic group $\mathrm{SL}(n)$: cf. Palais [31]. The moral of these examples is that the concept of stable points is purely algebraic, and not topological.
'''
e=[('text','top','-4.11-'),('text','upper','Now consider the skeleton Delta(T)'),('display','upper','r_o+r_1+r_2=0; sum r_i²=6'),('text','middle','where the ratios of the r_i’s are rational'),('display','middle','norm lambda = square root'),('text','middle lower','The resulting function'),('text','lower section 3','In this section, we shall consider counter-examples')]
d=[('function after norm','nu | v superscript o(1)','Small v-like glyph; superscript is small o, not silently made calligraphic O.','medium'),('section 3 base field','mathbb Q | mathbb C','Circular double-stem letter has apparent descending tail; context expectation not used.','medium'),('section 3 references','Converse 1.12; Proposition 0.7','Both labels transcribed as printed.','high')]
o=['Reused English section3: distinction between algebraic stable-point/quotient notion and analytic quotient; cites Palais.']
save(31,tex,e,d,o,sheet_kind='reused_typed')
