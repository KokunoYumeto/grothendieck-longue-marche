import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(39,r"""\scanpage{39}
\margin{$\unsure{G|g}$\quad $\unsure{Z}$\quad $\unsure{G}$}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&Z\arrow[dr,dash]&&&\\
\unsure{\mathfrak z}=Z\cap DG\arrow[ur,dash]\arrow[dr,dash,"H"']&&Z.DG\arrow[r,dash]&G\arrow[r,dash]&\unsure{\mathcal G|G}\\
&DG\arrow[ur,dash]&&&
\end{tikzcd}}
\[\underbrace{Z.DG\;---\;G}\]
\[---\;\underbrace{Z\cap DG\;---\;DG\;---\;Z.DG}\;---\;G\]
\[DG\qquad G/Z\]
\[DG/Z\cap DG\qquad 1\]

\diagram{\begin{tikzcd}
1\arrow[r,dash]&\mathfrak z\arrow[r,dash]&\mathbb D\arrow[r,dash]&\widehat{\mathbb H}\arrow[r]&1
\end{tikzcd}}

$H$ groupe alg. linéaire connexe (lisse)

$D^{\unsure{3|\mathfrak z}}$ \inserted{groupe formel divisible (lisse)}
extension centrale de $\widehat H$ par $\mathfrak z$

\deleted{\unsure{groupe formel}\quad\unsure{commutatif}}
\inserted{$\mathfrak z$ groupe formel \unsure{com.}}

$\mathfrak z\longrightarrow Z$ hom. de groupes formels
commutatifs
\mspage{38}
""",'scratch',[('marginalia','clipped top edge','G Z G'),('diagram','upper-left','Z intersection DG Z DG Z.DG G'),('display','upper-middle brace','Z.DG to G'),('display','upper-middle','Z intersection DG DG Z.DG G'),('display','middle','DG G/Z'),('display','middle','DG/Z intersection DG 1'),('diagram','lower-middle','1 z D Hhat 1'),('text','lower','H groupe alg. linéaire'),('text','lower','D extension centrale'),('marginalia','lower-right insertion','z groupe formel com.'),('text','bottom','z to Z hom. de groupes formels'),('marginalia','upper-right inverted','38')],doubts=[('top edge','three clipped ink fragments','Only lower parts of characters survive the crop. G/g, Z, G are tentative glyph readings, not supplied text.','low'),('lower diagram','outlined D and H','Heavily retraced capitals represented by blackboard bold, without interpreting this as a new mathematical species.','medium')], observations='Formal group scratch construction: central extension of a completion of a connected linear algebraic group H and a map from a commutative formal group z to Z. Lowercase z-like letter has no secure font distinction; repeated lower form is represented as fraktur z.')
