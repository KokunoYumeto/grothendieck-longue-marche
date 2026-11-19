from pathlib import Path

ROOT = Path('/workspace/scratch/17347c1714f0')
OUT = ROOT / 'out/readers/scan006/R2'
text = (ROOT / 'packets/scan006/C.tex').read_text()

# C's syntax is reused only after the complete page has been read against ink.
replacements = {
    r'\unsure{aussi}': 'aussi',
    r'\unsure{somme amalgamée}': 'somme amalgamée',
    r'\deleted{L\'application \unsure{naturelle}}': r'\deleted{L\'application naturelle}',
    r'\unsure{W|w}': r'\unsure{w|W}',
    r'\unsure{ouvert}': 'ouvert',
    r'\unsure{pts}': 'pts',
    r'\unsure{imm}': 'imm',
    r'\unsure{invariance}': 'invariance',
    r'\unsure{remplacement}': 'remplacement',
    r'\unsure{pourvu}': 'pourvu',
    r'\unsure{vérifier}': 'vérifier',
    r'\unsure{précis}': 'précis',
    r'^{\unsure{-}}': r'^{-}',
    r'\unsure{div.}': 'div.',
    r'\mspage{\unsure{5}}': r'\mspage{5}',
    r'soit $K\'\supset\bigcup C_i$': r'$\operatorname{int}K\'\supset\bigcup C_i$',
}
# Apostrophes in raw literals above retain their escaping; use literal forms here.
replacements.pop(r'\deleted{L\'application \unsure{naturelle}}')
replacements["\\deleted{L'application \\unsure{naturelle}}"] = "\\deleted{L'application naturelle}"
replacements.pop(r'soit $K\'\supset\bigcup C_i$')
replacements["soit $K'\\supset\\bigcup C_i$"] = "$\\operatorname{int}K'\\supset\\bigcup C_i$"
for old, new in replacements.items():
    assert old in text, old
    text = text.replace(old, new)

old_path = r'\draw (-1.92,1.36) .. controls (-1.30,.99) and (-.96,.44) .. (0,0);'
new_path = r'''\draw (-1.92,1.36) .. controls (-1.78,1.35) and (-1.65,1.25) .. (-1.58,1.14)
 .. controls (-1.30,.99) and (-.96,.44) .. (0,0);
% Narrow return loop at the upper-left outer junction: both edges are visible.
\draw (-1.92,1.36) .. controls (-1.75,1.37) and (-1.61,1.32) .. (-1.58,1.14);'''
assert old_path in text
text = text.replace(old_path, new_path)

old_arrow = r'\tikz[baseline=-.2ex]{\draw[->] (.38,.25) to[bend right=12] (0,0);}'
new_arrow = r'\tikz[baseline=-.2ex]{\draw (.58,.34) .. controls (.44,.36) and (.15,.12) .. (0,0); \draw (0,0) .. controls (-.08,.09) and (-.13,.06) .. (-.09,0) .. controls (-.05,-.04) and (.01,-.01) .. (0,0) -- (.08,.025);}'
assert old_arrow in text
text = text.replace(old_arrow, new_arrow)

text = text.replace(r'\mspage{5}', r'''% Detached short pen stroke below-left of his own page numeral.
\margin{\tikz[baseline=-.2ex]{\draw[line width=.3pt] (0,0) -- (.015,-.07);}}
\mspage{5}''')
(OUT / 'reading.tex').write_text(text)
print('Wrote reading.tex')
