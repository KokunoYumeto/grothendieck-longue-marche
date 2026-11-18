"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(107,
    "\\scanpage{107}\n% archive foliation: 106 (first digit partly clipped)\n\\figure{\\begin{tikzpicture}[x=0.85cm,y=0.85cm]\n\\draw[thick] (-3.6,0)--(4.3,0.12);\n\\draw[thick] (0,-2.2)--(0,3.7);\n\\draw[very thick] (0,-2.2)--(0.07,-0.65)--(0,0)--(-0.03,0.7);\n\\draw (-2.1,0.43) .. controls (-0.65,0.02) and (0.3,-0.13) .. (2.8,-0.38);\n\\draw (-2.05,-0.42) .. controls (-0.8,0.01) and (0.5,-0.09) .. (3.1,0.64);\n\\draw (-0.49,2.40) .. controls (0.08,0.80) and (0.12,-0.54) .. (-0.43,-1.50);\n\\draw (0.65,2.65) .. controls (-0.18,1.22) and (-0.09,-0.69) .. (0.67,-1.71);\n\\draw (-0.29,1.99)--(0.43,2.13);\n\\draw (-0.21,1.68)--(0.32,1.81);\n\\draw (-0.14,1.37)--(0.23,1.48);\n\\draw (-0.09,1.09)--(0.16,1.13);\n\\draw (-0.12,-0.78)--(0.18,-0.76);\n\\draw (-0.21,-1.06)--(0.29,-1.04);\n\\draw (-0.32,-1.31)--(0.44,-1.34);\n\\foreach \\x/\\lo/\\hi in {-1.8/-0.31/0.34,-1.5/-0.21/0.25,-1.2/-0.15/0.18,-0.9/-0.09/0.12,1.05/-0.16/0.18,1.4/-0.20/0.28,1.8/-0.26/0.39,2.2/-0.30/0.49,2.62/-0.36/0.59}{\\draw (\\x,\\lo)--(\\x,\\hi);}\n\\draw (-0.98,-0.46) .. controls (-1.48,1.28) and (1.18,1.49) .. (0.99,0.07)\n .. controls (1.09,-0.75) and (-0.10,-1.03) .. (-0.91,-0.51);\n\\foreach \\x/\\y in {-0.67/0.50,-0.42/0.63,-0.72/0.26,-0.40/0.33,-0.24/0.15,-0.60/-0.39,-0.20/-0.54,0.26/-0.56,0.41/-0.39,0.60/-0.46,0.78/-0.29,0.54/0.62}{\\fill (\\x,\\y) circle (0.012);}\n\\node at (0.53,0.48) {$Z$};\n\\node at (3.29,0.24) {$X_{T'}$};\n\\node[right] at (0.02,3.15) {$X_{T''}$};\n\\draw (2.6,-1.46) .. controls (3.62,-0.43) and (4.72,-0.62) .. (4.89,0.48)\n .. controls (5.07,1.64) and (5.16,2.30) .. (6.09,2.82);\n\\end{tikzpicture}}\n\n\\margin{$*$}\n\\diagram{\\begin{tikzcd}[column sep=small,row sep=large]\n\\widehat{\\mathbf Z}=\\unsure{\\Pi|\\pi}_1(Z') \\arrow[d] \\arrow[drr] & & \\unsure{\\Pi|\\pi}_1(Z'')=\\widehat{\\mathbf Z} \\arrow[dl] \\arrow[d] \\\\\n\\unsure{\\Pi|\\pi}_1(X_{T'}) \\arrow[dr] & \\unsure{\\Pi|\\pi}_1(X_{T''}) \\arrow[d] & \\unsure{\\Pi|\\pi}_1(Z)=\\widehat{\\mathbf Z}^{2} \\arrow[dl] \\\\\n& \\unsure{\\Pi|\\pi}_1(X_T) &\n\\end{tikzcd}}\n\n\\figure{\\begin{tikzpicture}\n\\node at (-1.4,0) {$Z=\\operatorname{Spec}$};\n\\node at (0,0) {$\\widehat{\\mathrm O}_{X,a}$};\n\\draw (0.03,-0.60) .. controls (-0.91,-0.42) and (-0.88,0.51) .. (-0.06,0.61)\n .. controls (0.95,0.78) and (0.83,-0.44) .. (0.03,-0.60);\n\\node at (0.42,0.77) {$A$};\n\\end{tikzpicture}}\n\\[\nX_{T'}\\cap X_{T''}=\\varnothing\n\\]\n\\[\nX_{T'}\\cap Z_{\\deleted{\\unsure{a}}}=Z'=\\widehat A_{\\unsure{p'|\\mathfrak p'}}\n\\quad\\begin{gathered}\\unsure{correspond} -- \\text{corps}\\\\\n\\text{résiduel }k(p')=\\text{corps local en }a\\text{ de }T'_0\n\\end{gathered}\n\\]\n\\[\nX_{T''}\\cap Z=Z''=\\widehat A_{\\unsure{p''|\\mathfrak p''}}\n\\quad\\begin{gathered}\\unsure{correspond} -- \\text{corps}\\\\\n\\text{résiduel }k(p'')=\\text{corps local en }a\\text{ de }T''_0\n\\end{gathered}\n\\]\n\nOn doit prouver un \\uline{\\unsure{th.} de descente} de nature essentiellement locale\n\n$+$ déterminer certains \\unsure{hom.} canoniques\n\n\\figure{\\begin{tikzpicture}\\draw (0,0)--(0.2,0.04);\\draw (0.4,0.02)--(1.25,0.03);\\draw (1.55,0.04)--(2.15,0.04);\\end{tikzpicture}}\n\n\\margin{\\diagram{\\begin{tikzcd}[row sep=small]\n\\deleted{\\unsure{A'}}\\unsure{\\}} \\arrow[d,dash,bend right=30] \\\\\nA \\arrow[d] \\\\\nB\n\\end{tikzcd}}}\n",
    elements=[['drawing', 'top left', 'crossing strips and central stippled Z; labels X_T′, X_T″'],
 ['margin note', 'top middle above diagram', 'asterisk'],
 ['diagram', 'upper right', 'Ẑ=π₁(Z′), π₁(Z″)=Ẑ to three groups, then π₁(X_T)'],
 ['drawing', 'middle left formula', 'Z=Spec(Ô_X,a), circled ring, A above'],
 ['display', 'middle left', 'X_T′∩X_T″=∅'],
 ['display', 'middle', 'X_T′∩Z=Z′=Â_p′; corps résiduel k(p′)'],
 ['deletion', 'subscript of Z in first intersection', 'a'],
 ['display', 'middle lower', 'X_T″∩Z=Z″=Â_p″; corps résiduel k(p″)'],
 ['text', 'lower', 'On doit prouver un th. de descente'],
 ['text', 'lower second paragraph', '+ déterminer certains hom. canoniques'],
 ['drawing', 'below prose', 'three short horizontal strokes'],
 ['margin note', 'bottom left', 'cancelled A′ and brace linked to A→B'],
 ['deletion', 'top of bottom-left diagram', 'A′']],
    doubts=[['annotations after completed rings',
  'correspond -- corps résiduel',
  'first word very compressed; may be a different abbreviation',
  'low'],
 ['completed-ring subscripts',
  'p′ and p″',
  'ordinary p versus Gothic p not settled by heavy ink',
  'medium'],
 ['subscript cancelled beneath Z', 'a', 'overwritten blob retains no reliable full outline', 'low'],
 ['last prose line', 'hom. canoniques', 'hom. is abbreviated and compressed', 'medium'],
 ['bottom margin diagram',
  'cancelled A′ and brace, then A→B',
  'tiny top scribble may be lettering practice; preserved with doubt',
  'low'],
 ['recurring handwritten homotopy-group sign',
  'Π',
  'π; angular two-stem handwriting does not securely distinguish typographic case; reconciled '
  'consistently across 096, 098, 100 and 107',
  'medium']],
    leads=['Explicit unfinished program: “On doit prouver un th. de descente de nature essentiellement '
 'locale” and “déterminer certains hom. canoniques”; the pictured local crossing induces a '
 'proposed fundamental-group gluing diagram, without a proof on this sheet.',
 'Reading question to retain: Z is written Spec of a completed local ring but its depicted '
 'fundamental group is Z-hat squared; do not silently insert a puncture or boundary complement '
 'into the transcription.'],
    sheet_kind='text',
)
