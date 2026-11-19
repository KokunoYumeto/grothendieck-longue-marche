from pathlib import Path
root=Path('/workspace/scratch/17347c1714f0/out/readers/scan006/R3')
s=(Path('/workspace/scratch/17347c1714f0/packets/scan006')/'C.tex').read_text()
changes=[
 (r'qui est \unsure{aussi} la \unsure{somme amalgamée}',r'qui est aussi la somme amalgamée'),
 (r'i\,(\unsure{W|w})',r'i\,(\unsure{w|W})'),
 (r'\unsure{ouvert} de',r'ouvert de'),
 (r'les \unsure{pts}',r'les pts'),
 (r'une \unsure{imm} fermée',r'une imm fermée'),
 (r"d'\unsure{invariance}",r"d'invariance"),
 (r'\unsure{remplacement}',r'remplacement'),
 (r"U_i'{}^{\unsure{*|\wedge}}=U'_i\cap K^*",r"U_i'{}^{\unsure{\wedge|*}}=U'_i\cap K^\wedge"),
 (r'\unsure{pourvu}',r'pourvu'),
 (r"\unsure{vérifier} l'énoncé \unsure{précis}",r"vérifier l'énoncé précis"),
 (r"$ soit $K'\supset\bigcup C_i",r"$ $\operatorname{int} K'\supset\bigcup C_i"),
 (r'\unsure{div.}',r'div.'),
 (r'\mspage{\unsure{5}}',r'\mspage{5}'),
]
for a,b in changes:
 assert s.count(a)==1,(a,s.count(a))
 s=s.replace(a,b)
s=s.replace('% slanted','% Slanted note at the left of the replacement conditions; three lines in the manuscript.')
s=s.replace('% vertical pen stroke to the left of the last line','% Vertical pen stroke to the left of the last two manuscript lines.')
s=s.replace('\\draw (0,0) .. controls (-.23,-.96) and (-.51,-2.12) .. (-.75,-2.78);','% The descending interior line stops just short and to the left of the lower cusp.\n\\draw (0,0) .. controls (-.23,-.96) and (-.51,-2.12) .. (-.75,-2.78);')
s=s.replace('\\margin{\\tikz[baseline=-.2ex]', '% The curved arrow runs from below the right-hand isomorphism down-left to the gloss.\n\\margin{\\tikz[baseline=-.2ex]')
s=s.replace("\\inserted{$U_i'{}^{\\unsure{\\wedge|*}}=U'_i\\cap K^\\wedge$}","\\inserted{$U_i'{}^{\\unsure{\\wedge|*}}=U'_i\\cap K^\\wedge$}")
(root/'reading.tex').write_text(s)
print('Wrote reading.tex.')
