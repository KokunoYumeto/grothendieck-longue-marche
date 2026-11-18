"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(138,
    "\\scanpage{138}\n% archive foliation: 137\n\\uline{Corollaire} Supposons $G$ admissible, et $P$ un fibré principal sous $G$. Alors, $\\operatorname{ad}(P)$, considéré comme $S$-groupe, est admissible.\n\n\\uline{Proposition 2} Soit $(P,\\xi)$ un fibré principal pointé sous un $S$-groupe admissible $G$. Alors $\\operatorname{Aut}(P,\\xi)$ est réduit à l'identité.\n\nCeci résulte, moyennant le corollaire précédent, \\deleted{du}\n\n\\deleted{\\uuline{Lemme}} \\uline{Proposition 3} Deux sections d'un $P$ \\inserted{\\unsure{princ. sous $G$|principal sous $G$}} (admissible sur $S$ \\inserted{réduit connexe}) qui ont $=$ valeur en un pt, sont identiques. [De façon plus précise, si $s$ est une section de $P/S$, alors il existe une composante connexe \\deleted{\\unsure{$P$}} $Q$ de $P$, tel que $Q_{\\text{réd}}\\to S$ soit un isom, et l'isomorphisme réciproque induit par $s$]\n\\margin{\\figure{\\begin{tikzpicture}[x=1cm,y=1cm]\n\\draw (0,0)--(0,1.8); \\draw (0,2)--(0,3.2);\n\\end{tikzpicture}}}\n\nUn $(P,\\xi)$ \\deleted{\\unsure{est dit}} (relatif à $G$ admissible) est dit \\uline{minimal} si \\unsure{on ne peut trouver} de $S$-ss-groupe admissible $G'$ de $G$ et $(P',\\xi')$ relatif à $G$, t.q.\n\\[\n(P,\\deleted{\\unsure{\\xi'}}\\xi)\\simeq(P',\\xi')\\times_G G'.\n\\]\n",
    elements=[['text', 'top corollary', 'Supposons G admissible'],
 ['text', 'proposition 2', 'Soit (P,ξ) un fibré principal pointé'],
 ['text', 'transition', 'Ceci résulte, moyennant le corollaire précédent'],
 ['deletion', 'after transition', 'du'],
 ['deletion', 'before proposition 3 heading', 'Lemme'],
 ['text', 'proposition 3', 'Deux sections d’un P'],
 ['insertion', 'above after P', 'princ. sous G'],
 ['insertion', 'above after S', 'réduit connexe'],
 ['text', 'bracketed strengthening', 'De façon plus précise'],
 ['deletion', 'before Q', 'P'],
 ['drawing', 'left margin beside proposition 3', 'two vertical emphasis rules'],
 ['text', 'bottom definition', 'Un (P,ξ) (relatif à G admissible)'],
 ['deletion', 'after first (P,ξ)', 'est dit'],
 ['display', 'last line', '(P,ξ) ≃ (P′,ξ′) ×_G G′'],
 ['deletion', 'above ξ in left side of last formula', 'ξ′']],
    doubts=[['insertion after P in proposition 3',
  'princ. sous G',
  'could be principal sous G; abbreviation cramped',
  'low'],
 ['proposition 3 phrase', 'ont = valeur', 'literal equality sign; no expansion to même', 'high'],
 ['before Q in bracketed paragraph', 'cancelled P', 'heavily overwritten letter', 'low'],
 ['end of bracketed paragraph',
  'et l’isomorphisme réciproque induit par s',
  'no est supplied: none clearly written',
  'medium'],
 ['cancelled words before relatif', 'est dit', 'heavy horizontal cancellation', 'low'],
 ['minimality condition',
  'on ne peut trouver',
  'compressed handwriting; tentative word sequence',
  'medium'],
 ['minimality, group of (P′,ξ′)', 'G', 'no prime clearly visible here', 'medium'],
 ['contracted product in final formula',
  '×_G G′',
  'subscript G and terminal G′ read literally, despite expected opposite order',
  'high'],
 ['overwriting of ξ in final formula',
  'cancelled ξ′',
  'small dark overwritten mark above ξ; identification tentative',
  'low']],
    leads=['Admissibility is asserted to persist for the twisted group ad(P), and the resulting corollary is '
 'used to reduce triviality of pointed-torsor automorphisms to the next rigidity proposition.',
 'Proposition 3 asserts that sections agreeing at one point agree everywhere; reduced connected S '
 'is inserted. The bracketed strengthening identifies a connected component whose reduction maps '
 'isomorphically to S, with reciprocal induced by the section.',
 'The final definition of minimal pointed torsor has a potentially reversed contracted-product '
 'formula, literally (P′,ξ′) ×_G G′, and gives G without a clear prime as the group of (P′,ξ′). '
 'Keep this as a reading question rather than silently repairing it.'],
    sheet_kind='text',
)
