from record import save
tex=r'''\scanpage{29}
\begin{center}-4.12-\end{center}
The first example is due to Nagata [27]. Here $\mathrm{SL}(3)$ is acting on an open set $U$ in $|5H|$, as in \S2. The geometric points of $U$ are precisely those plane quintic curves $C$ such that:

\begin{enumerate}
\item[i)] $C$ has no 4th order points,
\item[ii)] $C$ has no triple points, with tangent cone one line, and that line having 5-fold contact with $C$,
\item[iii)] $C$ has no triple points, consisting of a simple branch, and a tacnode,
\item[iv)] no component of $C$ is a line.
\end{enumerate}
Nagata has proven that $\mathrm{SL}(3)$ acts properly on $U$. But from the results of \S2, it follows that no geometric quotient of $U$ by $\mathrm{SL}(3)$ exists.

The second example is based on an example of Hironaka [15]. Let $V_o$ be $\mathbb P_3$, and let $\gamma_1$, $\gamma_2$ be two conics in $V_o$, intersecting normally in exactly two points $P_1$ and $P_2$. Following Hironaka, construct $\overline V_i$, for $i=1$ and $2$, by (a) blowing up $\gamma_i$ in $V_o$; (b) blowing up $\gamma_{3-i}$ in the result (cf. Figure 7). Let $V_i$ be the open set in $\overline V_i$ of points lying over $(V_o-P_{3-i})$. Then by patching $V_1$ and $V_2$, we obtain a single non-projective variety $V_3$ in which, over $P_1$ and $P_2$ the two curves $\gamma_1$ and $\gamma_2$ have been blown up in opposite orders! Now let $\sigma_o:V_o\longrightarrow V_o$ be a projective transformation of order 2 which permutes $P_1$ and $P_2$, and also $\gamma_1$ and $\gamma_2$. Then $\sigma_o$ induces an automorphism of $V_3$ of order 2. Hironaka has shown that there is no geometric quotient of $V_3$ by the group $\mathbb Z_2=\{1,\sigma\}$, although of course there is an analytic space $[V_3/\mathrm{mod}\,\mathbb Z_2]$.
\mspage{28}
'''
e=[('text','top','-4.12-'),('text','first paragraph','The first example is due to Nagata [27]'),('text','list i)','C has no 4th order points'),('text','list ii)','C has no triple points with tangent cone one line'),('text','list iii)','C has no triple points consisting of a simple branch'),('text','list iv)','no component of C is a line'),('text','middle','Nagata has proven that SL(3) acts properly'),('text','lower paragraph first half','The second example is based on an example of Hironaka [15]'),('text','lower paragraph second half','Now let sigma_o:Vo → Vo')]
d=[('base point subscripts','o','Round subscript shape retained consistently with reused pp4.13–14; may denote zero.','medium')]
o=['Reused p4.12: two nonexistence-of-geometric-quotient examples, attributed to Nagata and Hironaka, to distinguish from the topological manuscript.']
save(29,tex,e,d,o,sheet_kind='reused_typed')
