"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(98,
    "\\scanpage{98}\n\\mspage{6}\n% archive foliation: 97\n2°) $\\boxed{X_0-D'_0=\\mathbf{P}^1_k}$ i.e. $X_0=\\mathbf{P}^1_k$, $D'_0=\\varnothing$. Alors \\deleted{$\\unsure{\\Pi|\\pi}_1^t(\\unsure{X}/D,\\bar\\xi_1)$}\\inserted{$\\unsure{\\Pi|\\pi}_1^t(\\underline{\\mathcal{X}}/D,\\bar\\xi_1)$} est \\deleted{une extension} isomorphe à $\\mu_n(k)$, où $n$ est la partie première à $p=\\operatorname{car}k$ du degré de la self-intersection $X_0.X_0$ dans $\\mathcal{X}$.\n\n\\uline{Exemple} II a) $X_0=\\operatorname{Spec}\\mathbf{Z}$. Alors $\\mu_{t,X_0}^\\infty=0$,\n\\margin{\\figure{\\begin{tikzpicture}\n\\node[draw,ellipse,align=left,text width=7cm,inner sep=7pt] (n) at (0,0) {[\\unsure{puisque} dans $X_0$ \\unsure{tous|toutes} les car. résiduelles existent]};\n\\draw (n.south west) .. controls (-2,-0.8) and (-2.4,-1) .. (-2.2,-1.4);\n\\end{tikzpicture}}}\nd'où\n\\[\n\\unsure{\\Pi|\\pi}_1^t(\\mathcal{X}/D,\\bar\\xi_1)\\simeq\\unsure{\\Pi|\\pi}_1^t(X_0/D'_0,\\bar\\xi_0).\n\\]\n\\deleted{\\unsure{Le pb de}} Si $D'_0=\\varnothing$, on trouve $0$.\n\nSi $D'_0\\ne\\varnothing$, la partie abélienne de $\\unsure{\\Pi|\\pi}_1^t(X_0/D'_0,\\bar\\xi_0)$ est calculable par le corps des classes\\inserted{$\\bigl(\\simeq\\prod_{\\ell\\in D'_0}(\\mathbf{Z}/\\ell\\mathbf{Z})^*\\bigr)$}; \\unsure{sans} doute $\\unsure{\\Pi|\\pi}_1^t(X_0/D'_0,\\bar\\xi_0)$ \\unsure{n'est} \\unsure{en général pas} abélien fini. il y a des \\deleted{\\unsure{vraiment}} corps de nombres tamely ramifiés sur $\\mathbf{Q}$, qui ne sont pas abéliens .... ??].\n\\margin{?}\n\nb) $X_0=\\operatorname{Spec}\\mathbf{Z}-S$, $S\\ne\\varnothing$. Alors\n\\[\n\\mu_{t,X_0}^\\infty=\\prod_{\\ell\\in S}\\mu^\\infty(\\ell)_{X_0}.\n\\]\nMais qu'est $\\unsure{\\Pi|\\pi}_2^t(X_0/D'_0)$\n\n???\n",
    elements=[['text', 'top, item 2', 'X_0-D_0 prime = P^1_k'],
 ['deletion', 'upper, first pi_1 formula', 'pi_1^t(X/D,xi-bar_1)'],
 ['insertion', 'upper, above cancelled pi_1 formula', 'pi_1^t(underlined script X/D,xi-bar_1)'],
 ['deletion', 'upper, after est', 'une extension'],
 ['text', 'middle, Exemple II a)', 'X_0=Spec Z; Alors mu=0'],
 ['margin note',
  'middle-right, outlined callout with leader',
  'puisque dans X_0 tous les car. résiduelles existent'],
 ['drawing', 'middle-right, callout outline and leader', 'oval enclosing the marginal explanation'],
 ['display', "middle, isomorphism after d'où", 'pi_1^t(script X/D) simeq pi_1^t(X_0/D_0 prime)'],
 ['deletion', 'middle-left, before Si', 'Le pb de'],
 ['text', 'middle, empty boundary case', 'Si D_0 prime = emptyset'],
 ['text', 'lower-middle, abelian part and nonabelian question', 'Si D_0 prime neq emptyset'],
 ['insertion', 'lower-middle, after corps des classes', 'simeq product (Z/ell Z)^*'],
 ['deletion', 'lower-middle, before corps de nombres', 'vraiment'],
 ['margin note', 'left of doubtful arithmetic paragraph', '?'],
 ['text', 'lower, Exemple II b)', 'X_0=Spec Z-S; S neq emptyset'],
 ['display', 'lower, product of root-of-unity factors', 'mu^infty = product mu^infty(ell)'],
 ['text', 'bottom-right and continuation beneath', "Mais qu'est pi_2^t(X_0/D_0 prime) ???"]],
    doubts=[['upper cancelled formula', 'plain X', 'Overwritten central letter', 'medium'],
 ['outlined marginal note',
  'puisque; tous / toutes',
  'Opening word and agreement compressed',
  'low'],
 ['deletion before Si', 'Le pb de', 'Abbreviation pb and last word crossed', 'medium'],
 ['arithmetic paragraph after classes',
  "sans doute; n'est en général pas",
  'Very compressed phrase; negation needs further comparison',
  'low'],
 ['arithmetic paragraph, cancelled word', 'vraiment', 'Last strokes overstruck', 'low'],
 ['inserted product',
  '(Z/ell Z)^*',
  'No real/infinite-place qualifier supplied by the manuscript here',
  'high'],
 ['final product', 'mu^infty(ell)_{X_0}', 'The parenthesized letter resembles ell', 'medium'],
 ['recurring handwritten homotopy-group sign',
  'Π',
  'π; angular two-stem handwriting does not securely distinguish typographic case; reconciled '
  'consistently across 096, 098, 100 and 107',
  'medium']],
    leads=['Continuation of Exemple I: in the P^1 exceptional case the tame fundamental group is identified '
 'with mu_n(k), n the prime-to-characteristic part of the self-intersection degree.',
 'Exemple II a) sets X_0=Spec Z and mu_t^infty=0 because all residual characteristics occur; class '
 'field theory is invoked for the abelian part, with inserted product of (Z/ell Z)^*. A marginal ? '
 'and terminal ?? flag the nonabelian discussion.',
 "Exemple II b) X_0=Spec Z-S ends Mais qu'est pi_2^t(X_0/D_0 prime) ???. This is an explicit open "
 'question in the manuscript.'],
    sheet_kind='text',
)
