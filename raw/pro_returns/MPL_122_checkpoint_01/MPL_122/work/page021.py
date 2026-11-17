from record import save
save(21,r'''\scanpage{21}
\begin{center}-4.15-\end{center}

$V_5$ into $V_5$. Let $G$ be the semi-direct product of $\mathbb G_m$ and $\mathbb Z_2$ defined by $\sigma\alpha=\alpha^{-1}\sigma$ for $\alpha\in\unsure{\overline{\mathbb G}_m|\mathbb G_m}$, $\sigma\in\mathbb Z_2$, $\sigma\ne1$. Then we have now defined an action of $G$ on $V_5$ such that there is no geometric quotient. Moreover, note that $V_5$ is quasi-projective (recall that blowing up any sheaf of ideals takes a projective variety into a projective variety).

This completes the second step of the construction. Finally fix some very ample sheaf $L$ on $\overline V_5$. By Proposition 1.6, some power $L^n$ of $L$ is $\mathbb G_m$-linearizable. Moreover, it is easy to check that then $\sigma^*L^n\otimes L^n$ admits a $G$-linearization. Put $M=\sigma^*L^n\otimes L^n$. Since $L$ is very ample, it follows that $M$ is very ample. By Proposition 1.7, there is an action of $G$ on $\mathbb P_n$, a $G$-linearization of $\underline{o}(1)$ and a $G$-linear immersion
\diagram{\begin{tikzcd}
\phi:\ V_5 \arrow[r] &\mathbb P_n
\end{tikzcd}}
such that $\phi^*(\underline{o}(1))\cong M$. Let $\beta:G\longrightarrow\operatorname{PGL}(n)$ be the homomorphism which induces the action of $G$ on $\mathbb P_n$. It is well-known that the coset space $\operatorname{PGL}(n)/\beta(g)$ exists (cf. [8], Exposé 8). Define $V_6$ to be the locally closed reduced subscheme of $\mathbb P_n\times[\operatorname{PGL}(n)/\beta(g)]$ whose geometric points are the pairs
\[
(\sigma(\alpha,\phi x),\quad\alpha\bmod\beta(G))
\]
for geometric points $\alpha$ in $\operatorname{PGL}(n)$, $x$ in $V_5$, and where $\sigma$ indicates the usual action of $\operatorname{PGL}(n)$ on $\mathbb P_n$. Then one sees easily that a
\mspage{20}
''',[
('text','top centre','-4.15-'),
('text','upper paragraph','V5 into V5. Let G be the semi-direct product'),
('text','middle paragraph','This completes the second step of the construction'),
('diagram','middle-lower','φ:V5→P_n'),
('text','below immersion','such that φ*(o(1))≅M. Let β:G→PGL(n)'),
('display','lower','(σ(α,φx), α mod β(G))'),
('text','last paragraph','for geometric points α in PGL(n)'),
('margin note','bottom left','20')
],[
('first paragraph, α∈','overline G_m|G_m','A horizontal line appears above the doubled G, possibly a separate bar.','medium'),
('coset-space paragraph','β(g), twice','Both letters are visibly lower-case; the later displayed β(G) is upper-case.','high'),
('middle paragraph and φ*','underlined o(1)','The sheaf symbol is a small underlined o, not silently replaced by calligraphic O.','high')
],['Reused English sheet constructs an action of G_m⋊Z_2 without geometric quotient and discusses G-linearization and an induced PGL construction; the preceding and following proof are absent.'],sheet_kind='reused_typed')
