from record_page import record
tex=r'''\scanpage{5}
% archive foliation: 4
The map $\phi$ of $M$ to the compact nil-manifold $H/\Gamma$
also generalizes and we obtain a tower of maps of $M$
into a tower of nil-manifolds beginning with the Jacobian
$H_1(M,R)/H_1(M,Z)$.

The next section shows how this construction becomes
canonical if $M$ is Riemannian

\begin{center}\uline{The} \uline{Model} \uline{of} \uline{a} \uline{Riemannian} \uline{Manifold}\end{center}

If $M$ is Riemannian we have the $*$-operator on forms,
the adjoint of $d$, $d^*=*d*$, and the Hodge decomposition
\[
\omega=dx_\omega+d^*y_\omega+h_\omega
\]
where $x_\omega$, $y_\omega$, and $h_\omega$ are unique subject to the conditions
\[
x_\omega\in\text{image of }d^*,\quad y_\omega\in\text{image }d,\quad
h_\omega\in\ker d\cap\ker d^*.
\]
This follows on the formal level from the ``disjoint-
ness'' of $d$ and $d^*$:
\[
\begin{aligned}
dd^*x=0&\Rightarrow d^*x=0\\
d^*dy=0&\Rightarrow dy=0.
\end{aligned}
\]
Thus $\omega$ is closed iff $y_\omega=0$. Then $\omega$ is cohomologous
to a canonical form, the harmonic representative $h_\omega$.
And finally if $\omega$ is exact $y_\omega$ and $h_\omega$ are zero and $\omega$ is the
differential of a canonical form $x_\omega$.

We can use the Hodge decomposition to rigidify the
model of a Riemannian manifold. In the construction of
$\rho$
\diagram{\begin{tikzcd}
\Lambda(x_1,x_2\unsure{,|;}\ldots;d)\arrow[r,"\rho"]&\{\text{smooth forms}\}
\end{tikzcd}}
we have to make various choices. For example we have to
choose
'''
record(5,tex,[('text','upper paragraph','The map φ of M'),('text','upper paragraph 2','The next section'),('text','heading','The Model of a Riemannian Manifold'),('text','middle paragraph','If M is Riemannian'),('display','middle','ω=dx_ω+d* y_ω+h_ω'),('text','middle below display','where x_ω'),('display','middle conditions','x_ω∈image of d*'),('text','middle','This follows'),('display','below fold','dd*x=0 ⇒ d*x=0; d*dy=0 ⇒ dy=0'),('text','lower paragraph','Thus ω is closed'),('text','lower paragraph','We can use the Hodge decomposition'),('diagram','near bottom','Λ(x_1,x_2,…;d) → {smooth forms}'),('text','bottom continuation','we have to make various choices')],sheet_kind='reused_typed',doubts=[('last display punctuation','comma after x_2','semicolon-like type / overstrike','medium')],notation=[('typed coefficient letters',r'$R$, $Z$','scan 5: plain typescript letters, not silently blackboard-bold')])
