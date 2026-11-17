from record import draft
draft(142,r"""
\scanpage{142}
\mspage{141}

Si on a pu définir $F_{11}$, \unsure{avec} commutativité des deux autres carrés, alors l'hom $F$ est un hom d'ext. au sens strict (avec id sur $L_1\otimes L_2$ et sur $M_1\otimes M_2$), donc c'est un iso.

\unsure{Concentrons} sur $F_{11}:E_1\otimes E_2\longrightarrow E_1\otimes E_2$ seulement.

1°) Connu sur $E_1\otimes_0 E_2$, doit \unsure{être} le composé
\[
 E_1\otimes_0 E_2\xrightarrow{\pi}L_1\otimes L_2\mathrel{-\!\!-\!\!-}E_1\otimes E_2
\]
($\chi$-rétraction de $E_1\otimes_0 E_2$ sur le sous-module $L_1\otimes L_2$)

i.e. $F_{11}\circ\mu$ est connu
\diagram{\begin{tikzcd}
 E_1\otimes_0\uline{E_2}\arrow[r,hook,"\mu"]\arrow[dr,dashed,no head,"\pi"']&
 E_1\otimes E_2\arrow[r,"F_{11}"]&E_1\otimes E_2\\
 &L_1\otimes L_2\arrow[ur,dashed,"\alpha_1\otimes\alpha_2"']&
\end{tikzcd}}

2°) $\nu\circ F_{11}$ est connu, de façon précise on a
\diagram{\begin{tikzcd}
 E_1\otimes E_2\arrow[r,"F_{11}"]\arrow[dr,"\psi_1\otimes\psi_2"']&
 E_1\otimes E_2\arrow[r,"\nu"]&\deleted{\unsure{E_1}}E_1\otimes^0 E_2\\
 &M_1\otimes M_2\arrow[ur,"\omega"']&
\end{tikzcd}}

\margin{\deleted{NB $\pi\big|_{L_1\otimes L_2}=\chi\,\mathrm{id}_{L_1\otimes L_2}$}}

\margin{NB $\pi\circ(\alpha_1\otimes\alpha_2)=\chi\,\mathrm{id}_{L_1\otimes L_2}$\\
$(\psi_1\otimes\psi_2)\circ\omega=\chi\,\mathrm{id}_{M_1\otimes M_2}$.}

\[
 \boxed{\begin{gathered}
 \chi\,\mathrm{id}-(\pi'_1+\pi'_2)+\gamma\,\pi'_1\otimes\pi'_2\\
 \gamma\chi=2\qquad\text{e.g. }\chi=2,\ \gamma=1
 \end{gathered}}
\]
dans le cas $\chi=2$, on aura
\[
 \left\{\begin{aligned}
 F_{11}(\deleted{\unsure{x_1\otimes x_2}}x)&=\bar x+x\\
 \bar x_i&=x_i-\pi_i(x_i)
 \end{aligned}\right.
 \qquad
 \begin{gathered}
 \overline{x_1\otimes x_2}=\bar x_1\otimes\bar x_2\\
 \text{i.e.}\qquad \boxed{\pi_i(x)=x_i-\bar x_i}
 \end{gathered}
\]

\margin{NB La \unsure{donnée} du $\pi_1$ \unsure{équivaut} à celle de $\sigma_1$ \unsure{involution} \unsure{qui induit} $-\mathrm{id}_{L_1}$ et $+\mathrm{id}_{M_1}$.}

\figure{\begin{tikzpicture}
\draw (0,0)--(0,1.9); \draw (.07,0)--(.07,1.9);
\end{tikzpicture}}
""")
