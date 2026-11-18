import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\cotefile{67}
\scanpage{53}
% archive foliation: 55
\margin{\unsure{torseurs sur groupes diédriques}
\diagram{\begin{tikzcd}[column sep=small]
\unsure{\text{torseurs sur groupes diédriques}} \arrow[r,leftrightarrow] & \text{Cercles toriques}
\end{tikzcd}}
\deleted{\unsure{(syst. à torsion)}}
\deleted{$\unsure{\simeq\mathbb U\rtimes\mathbb Z/2\mathbb Z}$}
\deleted{\unsure{(comm.}\ $\unsure{\mathbb Z/2\mathbb Z}$\unsure{)}}}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\text{Cercles toriques} \arrow[r,leftrightarrow] &
\begin{gathered}\deleted{\unsure{\text{plan}}}\ \text{vectoriel}\ \inserted{\text{réel}}\ \text{euclidien}\ \deleted{\unsure{\text{uni}}}\end{gathered}
\arrow[r,leftrightarrow] &
\left[\begin{gathered}\unsure{\text{Droite vectorielle}}\ \inserted{\text{unitaire}}\ \text{sur corps }\mathbb C\\
\text{iso. à }\mathbb C\ \unsure{\text{(mais pas can. +)}}\end{gathered}\right]
\\
\text{Cercles toriques orientés}\arrow[r,leftrightarrow]\arrow[d,leftrightarrow] &
\uline{\text{plans}}\ \text{vectoriel réel orienté}\arrow[r,leftrightarrow] &
\begin{gathered}\deleted{\text{plan}}\ \inserted{\text{droites vectorielles}}\\
\text{complexes}\ \inserted{\text{unitaires}}\ \deleted{\unsure{D}}\ T\\
\deleted{\unsure{\text{structure euclidienne}}}\\
\text{i.e. avec iso }T\simeq\overline T^{\vee}\ \text{i.e.}\\ T^{\vee}\simeq\overline T\end{gathered}
\\
\text{torseurs sous }\mathbb U & {}\arrow[r,leftrightarrow] &
\begin{gathered}\text{droites vectorielles complexes}\\
\text{conformes, avec}\ \deleted{\unsure{\text{disques}}}\\
\deleted{\text{conformes}}\\
\unsure{\text{contenant}}\ \unsure{\text{fixé}}\ D\end{gathered}
\end{tikzcd}}

\deleted{\unsure{Tandis que deux flèches de catégories}}

\deleted{Soient $C',C''$ deux cercles toriques orientés,}
\deleted{\unsure{alors on a}}
\deleted{$\unsure{\mathbb C\operatorname{Isom}}(C'^{-1},C'')\simeq
\operatorname{Isom}(C''^{-1},C')$}

\margin{\uline{NB} Pour $D$ droite conforme fixée, on a
\unsure{tous les}\ \unsure{jauges en}\ $D=\unsure{\delta\rtimes\mathbb U}$,
et $\unsure{\mathcal J_G(D)\simeq\mathcal J(D)^{\leftarrow\varepsilon}_{\frac12}}$ ;
(i.e. $\unsure{G}$ = groupe de \unsure{rotations}).}

\margin{\unsure{condition des}\ $\mathbb R^{*+}$\unsure{-torseurs}}

Le passage aux cercles toriques \inserted{orientés} duals correspond au passage
à l'espace vectoriel \deleted{réel euclidien}
\inserted{complexe dual} $\deleted{\unsure{T}}T^{\vee}$ $(\simeq\overline T)$.

La donnée, pour deux \uline{droites} vect complexes $T',T''$
d'un système $((D',D''),u)$, où $D',D''$ sont des
disques dans $T',T''$ et
\[
\begin{aligned}
u\in\delta D'\wedge_{\mathbb U}\delta D''\quad
(&\simeq\operatorname{Isom}_{\mathbb U}(\delta D'^{-1},\delta D'')\\
&\simeq\operatorname{Isom}_{\mathbb U}(\delta D''^{-1},\delta D')
\simeq\operatorname{Isom}(T'^{-1},T'')
\simeq\operatorname{Isom}(T''^{-1},T')
\simeq\unsure{\operatorname{Biisom}}(T'\otimes T'')\\
&\simeq\unsure{T'^{\times}\wedge_{\mathbb C^{\times}}T''^{\times}}
\unsure{\}}\simeq\deleted{\unsure{\text{flèches de }D',D''\ \text{pour}}}
\text{dualités entre }(T',T''))
\end{aligned}
\]
revient à la donnée d'une $v\in(T'\otimes_{\mathbb C}T'')^{\unsure{\times|*}}$
i.e. une dualité entre $T',T''$, \uline{plus} une jauge \inserted{$D'$} dans $T'$
(ou ce qui revient au \unsure{même}\ \unsure{quasi.}\ ; plus une jauge
$D''$ dans $\overline T''$).
"""
elements=[
('margin note','upper left, diagonal','torseurs sur groupes diédriques'),
('diagram','upper left margin','torseurs ↔ Cercles toriques'),
('deletion','upper left margin','syst. à torsion'),
('deletion','upper left margin','U ⋊ Z/2Z'),
('deletion','upper left margin','comm. Z/2Z'),
('diagram','upper third, three rows','Cercles toriques; plans; droites; torseurs'),
('deletion','diagram row 1','plan; uni'),
('insertion','diagram row 1','réel; unitaire'),
('deletion','diagram row 2','plan; D; structure euclidienne'),
('insertion','diagram row 2','droites vectorielles; unitaires'),
('deletion','diagram row 3','disques; conformes'),
('deletion','upper middle','Tandis que deux flèches de catégories'),
('deletion','middle left','Soient C′,C″ deux cercles toriques orientés'),
('deletion','middle left, below','alors on a'),
('display','middle left, crossed out','C Isom(C′−1,C″) ≃ Isom(C″−1,C′)'),
('deletion','middle left display','C Isom(C′−1,C″)'),
('margin note','middle right, bracketed','NB Pour D droite conforme fixée'),
('margin note','middle left, diagonal','condition des R*+-torseurs'),
('text','middle','Le passage aux cercles toriques duals'),
('insertion','above duals','orientés'),
('deletion','below passage','réel euclidien; T'),
('insertion','above deletion','complexe dual'),
('text','lower half','La donnée, pour deux droites vect complexes'),
('display','lower half, three lines','u ∈ δD′ ∧U δD″; Isom; dualités'),
('deletion','display last line','flèches de D′,D″ pour'),
('text','lower third','revient à la donnée d’une v'),
('insertion','above jauge','D′'),
]
save(53,tex,elements,
 doubts=[('upper diagram','plans / vectoriel / euclidien','Singular/plural and cancelled noun uncertain','low'),('NB marginal note','jauges en D; J_G(D)','Dense overwritten formula and letters','low'),('lower display','Biisom; nonzero-vector superscripts','Letterforms and stars/crosses uncertain','low'),('last paragraph','même quasi.','Faint compressed words','low')],
 notations=[('Double-lined U',r'\mathbb U','Circle group, scan 53'),('Boundary of disc',r'\delta D','Scan 53; do not silently change to partial'),('Dual of line',r'T^{\vee}','Scan 53, distinguish from inverse exponent -1'),('Bar over T',r'\overline T','Scan 53'),('Contracted-product wedge',r'\wedge_{\mathbb U}','Scan 53'),('Prime and double prime',r"T',T''",'Scan 53: two short ticks, not exclamation mark')],
 abbreviations=[('NB','nota bene'),('i.e.','id est'),('iso.','isomorphe / isomorphisme'),('vect','vectorielles'),('can.','canonique')],
 leads=['Equivalences between toric circles, oriented planes and unitary complex lines; cancellations and singular/plural ambiguity make the precise categorical claim uncertain.','Dual circle and dual/conjugate line; disc-boundary contracted products and the residual gauge choice.'])
