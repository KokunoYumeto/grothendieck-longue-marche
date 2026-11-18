"""Mechanically regenerated from the saved page and authoritative JSON.
No scan reading or mathematical correction is performed by this script.
"""
from save_page import save_page

save_page(137,
    "\\scanpage{137}\n% archive foliation: 136\nSoit $S$ un schéma \\uline{réduit} \\uline{connexe}.\n\nOn considère des schémas en groupes, finis et plats sur $S$, soit $G$, pour lesquels on a une suite exacte\n\\diagram{\\begin{tikzcd}[column sep=small]\ne \\arrow[r,no head] & \\unsure{U|H} \\arrow[r] & G \\arrow[r,no head] & \\Gamma \\arrow[r] & e\n\\end{tikzcd}}\noù la projection $U\\to S$ est plate, finie, \\deleted{\\unsure{s}} et géométriquement \\deleted{\\unsure{un homéomorphisme}} injectif, et où $\\Gamma\\unsure{-|\\to}S$ est plat, fini, séparable. Alors le sous-$S$-groupe $U$ de $G$ est déterminé de façon unique [pour cette assertion, l'hypothèse ``$S$ réduit'' est-elle nécessaire?].\n\\margin{\\uline{$S$-Groupes} \\uline{admissibles} ($S$ réduit?)}\nOn veut étudier des fibrés principaux \\inserted{hom.} $P$ sur de tels $S$-groupes. On suppose $S$ pointé par $a\\deleted{\\unsure{\\xi}}$, et on considère des $P$ avec structure pointée.\n\n\\margin{\\figure{\\begin{tikzpicture}\\draw[line width=.55pt] (0,2.5) .. controls (.02,1.7) and (.02,.7) .. (.07,0);\\end{tikzpicture}}}\n\\uline{Proposition} \\deleted{\\unsure{soit $S'\\to S$}} Soit $S'\\to S$ un morphisme \\deleted{plat fini surjectif fidèlement plat}, $G$ un $S$-groupe fini. \\deleted{Si $G\\times_S S'$ est admissible,} \\unsure{?} \\inserted{Si $G\\deleted{\\unsure{\\times_S S'}}$ est admissible, $G\\times_S S'$ aussi;} la réciproque est vraie si $S'\\to S$ est fidèlement plat.\n\\margin{$S'$ et $S$ réduits}\n\nDirect est trivial. Réciproque résulte de le théorème de la descente et unicité.\n",
    elements=[['text', 'first line', 'Soit S un schéma réduit connexe'],
 ['text', 'group introduction', 'On considère des schémas en groupes'],
 ['diagram', 'exact sequence', 'e — U → G — Γ → e'],
 ['text', 'conditions and uniqueness', 'où la projection U→S est plate'],
 ['deletion', 'after finie', 's'],
 ['deletion', 'after géométriquement', 'un homéomorphisme'],
 ['margin note', 'left midway', 'S-Groupes admissibles (S réduit?)'],
 ['text', 'pointed torsor paragraph', 'On veut étudier des fibrés principaux'],
 ['insertion', 'above before P', 'hom.'],
 ['deletion', 'after a', 'ξ'],
 ['drawing', 'left of base-change proposition', 'vertical emphasis rule'],
 ['text', 'proposition', 'Soit S′→S un morphisme'],
 ['deletion', 'after proposition heading', 'soit S′→S'],
 ['deletion', 'qualifiers of morphism', 'plat fini surjectif fidèlement plat'],
 ['deletion', 'original implication after fini', 'Si G×_S S′ est admissible'],
 ['text', 'question at cancelled implication', '?'],
 ['insertion', 'new implication above cancelled one', 'Si G est admissible, G×_S S′ aussi'],
 ['deletion', 'inside inserted implication after G', '×_S S′'],
 ['margin note', 'left beside proposition', 'S′ et S réduits'],
 ['text', 'proof', 'Direct est trivial. Réciproque résulte']],
    doubts=[['second object in sequence',
  'U',
  'H is possible beneath retracing; U in surrounding prose',
  'medium'],
 ['sequence connectors', 'e—U and G—Γ', 'no clear heads; unlike the U→G and Γ→e arrows', 'medium'],
 ['conditions of U',
  'cancelled s; un homéomorphisme',
  'small isolated cancellation and crossed phrase are uncertain',
  'low'],
 ['Γ to S connector', 'dash', 'could be a minimally drawn arrow', 'medium'],
 ['after point a', 'cancelled ξ', 'small zigzag heavily cancelled', 'low'],
 ['after Proposition', 'soit S′→S', 'heavily scribbled; first word and symbols tentative', 'low'],
 ['question at old implication',
  '?',
  'small isolated mark above the end of cancellation may be a question mark',
  'low'],
 ['proof wording',
  'de le théorème',
  'visible de at previous line end followed by le; no contraction supplied',
  'medium']],
    leads=['The page names finite flat S-groups admitting a geometrically injective connected part U and a '
 'finite separable quotient Γ “admissibles”. It explicitly asks whether reducedness of S is needed '
 'for uniqueness of U.',
 'The base-change proposition is revised on the page: forward preservation of admissibility is '
 'written over a cancelled earlier formulation, and faithful-flat reflection is then asserted by '
 'descent and uniqueness. A marginal condition says S′ and S reduced; it must accompany any use of '
 'the proposition.',
 'Pointed principal homogeneous bundles are the intended objects of study, with S itself pointed. '
 'Compare the typed pointed-torsor construction without importing its hypotheses into this page.'],
    sheet_kind='text',
)
