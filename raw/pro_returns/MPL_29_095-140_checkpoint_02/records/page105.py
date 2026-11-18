"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(105,
    '\\scanpage{105}\n% archive foliation: 104\n$\\Pi_2(X,\\xi)$\n\na) Si $X$ simplement connexe\n\nalors\n\\[\nM\\unsure{\\rightsquigarrow|\\longmapsto}H^2(X,M)\n\\]\navec $M$ \\deleted{\\unsure{faisceau de}} \\inserted{groupe de} torsion \\deleted{\\unsure{constant}} fini est exact à g., donc proreprésentable par\n\\[\nH^2(X,M)=\\operatorname{Hom\\,cont}(\\uline{\\Pi_2(X)},M)\n\\]\n\nb) Dans le cas général,\n\\diagram{\\begin{tikzcd}[column sep=small,row sep=small]\n\\Pi_2(X,\\xi)=\\Pi_2(\\widetilde{X(\\xi)}) \\arrow[d,phantom,shift right=3em] \\arrow[d,shift right=4em] \\\\\n\\text{revêtement universel \\unsure{pointé} défini par }\\xi\n\\end{tikzcd}}\n\n\\figure{\\begin{tikzpicture}[x=1cm,y=1cm]\n\\draw (0.05,0.12) .. controls (0.35,0.10) and (0.65,0.06) .. (0.90,0.08)\n .. controls (1.15,-0.03) and (1.40,0.03) .. (1.60,0.12);\n\\draw (1.60,0.12) .. controls (1.91,0.02) and (2.30,0.05) .. (2.61,0.07);\n\\draw (0.05,0.12) .. controls (0,0.62) and (0.14,1.35) .. (0.08,2.16);\n\\draw (2.61,0.02) .. controls (2.55,0.80) and (2.80,2.19) .. (2.89,2.79)\n .. controls (2.84,2.93) and (2.38,2.80) .. (1.82,2.83)\n .. controls (0.78,2.92) and (0.35,2.84) .. (0.10,2.63);\n\\draw (1.22,0.17) .. controls (1.37,0.65) and (1.26,2.03) .. (1.28,2.79);\n\\draw (1.25,2.95) .. controls (2.08,3.84) and (3.29,4.72) .. (3.99,5.18);\n\\draw (3.99,5.18) .. controls (3.99,4.40) and (4.01,3.34) .. (4.03,2.14);\n\\draw (1.27,0.17) .. controls (2.24,1.04) and (3.28,2.05) .. (3.93,2.31);\n\\draw (0.08,1.43) -- (1.36,1.41) -- (3.92,3.91);\n\\draw (0.08,1.43) .. controls (0.60,2.24) and (0.95,3.34) .. (1.30,4.07);\n\\draw (1.46,4.38) .. controls (2.02,4.45) and (2.70,3.83) .. (3.92,3.91);\n\\node[above] at (1.73,4.52) {$D_0$};\n\\node[above right] at (4.05,5.18) {$D_1$};\n\\node[below left] at (0.04,0.01) {$D_2$};\n\\end{tikzpicture}}\n\n\\figure{\\begin{tikzpicture}\n\\begin{scope}[rotate=180,transform shape]\n\\node at (0,0) {$\\mathbf T(\\mathbf E_1,\\ldots,\\mathbf E_n)^{\\deleted{\\unsure{\\Phi}}}$};\n\\node at (3.25,0.05) {$\\deleted{\\unsure{E}}\\quad\\mathcal F$};\n\\node at (-2.9,-0.67) {$\\mathbf X$};\n\\node at (-1.70,-1.12) {$\\mathbf K$};\n\\node at (-0.67,-0.63) {$\\deleted{\\unsure{\\pi}}$};\n\\node at (-0.60,-0.92) {$p_1$};\n\\node at (0.55,-0.92) {$p_n$};\n\\node at (0.75,-2.03) {$\\mathbf G_1\\times\\cdots\\times\\mathbf G_n$};\n\\node at (3.27,-1.99) {$\\unsure{\\mathcal K}$};\n\\end{scope}\n\\end{tikzpicture}}\n',
    elements=[['text', 'top title', 'Π₂(X,ξ)'],
 ['text', 'upper', 'a) Si X simplement connexe'],
 ['display', 'upper', 'M↦H²(X,M)'],
 ['text', 'upper middle', 'avec M … torsion … fini'],
 ['deletion', 'after M', 'faisceau de'],
 ['insertion', 'above deleted faisceau de', 'groupe de'],
 ['deletion', 'between torsion and fini', 'constant'],
 ['display', 'middle', 'H²(X,M)=Hom cont(Π₂(X),M)'],
 ['text', 'middle', 'b) Dans le cas général'],
 ['diagram',
  'middle right with annotation below',
  'Π₂(X,ξ)=Π₂(X̃(ξ)); arrow to revêtement universel'],
 ['drawing', 'lower left', 'three intersecting surfaces labelled D₀ D₁ D₂'],
 ['drawing', 'bottom upside down', 'T(E₁,…,E_n), X,K,G₁×⋯×G_n, calligraphic letters'],
 ['deletion', 'bottom pen samples superscript', 'Φ'],
 ['deletion', 'bottom pen samples near F', 'E'],
 ['deletion', 'bottom pen samples above p₁', 'π']],
    doubts=[['with M, cancelled words',
  'faisceau de; constant',
  'faint pencil crossed by horizontal lines',
  'low'],
 ['annotation beneath X tilde', 'pointé', 'possibly ponctué; compressed central strokes', 'medium'],
 ['pen samples, upside-down bottom',
  'T(E₁,…,E_n), X, K, F, K',
  'letter styles approximated; heavily inked small shapes marked unsure',
  'medium'],
 ['pen samples, small indices',
  'p₁, p_n; deleted π',
  'small upper shape may be a different letter or pen test',
  'low'],
 ['cohomology-functor connector',
  'wavy arrow / mapsto',
  'pencil stroke is wavy and the usual mapsto initial bar is not clear',
  'medium']],
    leads=['Definition sketch: for simply connected X, M↦H²(X,M) on finite torsion groups is said to be left '
 'exact and prorepresentable by Π₂(X); general Π₂(X,ξ) is assigned to the pointed universal cover. '
 'No proof on this page.',
 'Drawing of three intersecting divisors D₀,D₁,D₂ has no accompanying claim; bottom lettering '
 'exercises should not be mistaken for a mathematical assertion.'],
    sheet_kind='text',
)
