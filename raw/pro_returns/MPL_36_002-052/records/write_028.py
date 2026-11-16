from save_page import save
tex=r'''
\scanpage{28}

\diagram{\begin{tikzcd}[row sep=small,column sep=small]
 & M \arrow[dr,"{\text{\unsure{Situation}}}"] & & & \unsure{-} \\
 \unsure{\bullet|0} \arrow[r,no head] & T \arrow[r] \arrow[d,equal] & G \arrow[r,no head] & B & 0 \arrow[l] \\
 & D(M') & & \times & \unsure{1|\vert} \\
 \unsure{\bullet|0} \arrow[r,no head] & T' \arrow[r] \arrow[d,equal] & G' \arrow[r,no head] & B' \arrow[r] & 0 \\
 & D(M) & & & \\
 & M' \arrow[uur,"{\unsure{R^1}}"'] & & &
\end{tikzcd}}

\margin{27}
'''
e=[('diagram','upper right','M; T=D(M prime); G; B; 0; T prime=D(M); G prime; B prime; M prime'),('margin note','bottom left pencil','27')]
d=[{'line':'above upper diagonal arrow','reading':'Situation','alternatives':'extremely compressed heading/arrow label','confidence':'low'},{'line':'leftmost objects, both rows','reading':'bullet','alternatives':'0 written as a dot','confidence':'low'},{'line':'upper far right','reading':'short dash; 1','alternatives':'stray strokes; vertical bar','confidence':'low'},{'line':'beside lower diagonal arrow','reading':'R^1','alternatives':'overwritten or cancelled symbol cluster','confidence':'low'},{'line':'upper B to 0 connection','reading':'0 -> B, pointing left','alternatives':'unusual arrow, retained from visible left-pointing head','confidence':'medium'}]
save(28,tex,e,d,'Sparse diagram linking lattices M,M-prime, tori T=D(M-prime), T-prime=D(M), G/G-prime and B/B-prime. Plain horizontal strokes preserved as no-head connections; upper last arrow visibly points left, unlike lower one. Do not repair into expected exact sequences. Potential dual 1-motive structure only an interpretive lead. Pencil page 27; no author page number visible.')
