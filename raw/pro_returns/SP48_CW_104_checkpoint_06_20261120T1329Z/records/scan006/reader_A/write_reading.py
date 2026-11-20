from pathlib import Path

out = Path(__file__).parent
c = Path('/workspace/scratch/7178efd1cfac/reader_inputs/scan006/C.tex').read_text()
replacements = [
 (r'\widetilde{\unsure{D|\mathbb D}}', r'\widetilde{\mathbb D}'),
 (r'n\in{\unsure{\mathbb I|I}}', r'n\in\mathbb I'),
 (r'\longrightarrow\deleted{\unsure{N}}\mathbb I', r'\longrightarrow\deleted{N}\mathbb I'),
 (r'\text{\unsure{croissante}}', r'\text{croissante}'),
 (r'{\unsure{J|I}_{n\'\'}}', r'{J_{n\'\'}}'),
 (r'\unsure{u_\eta|u_g|u_y}', r'\unsure{u_\eta|u_y}'),
 (r'\unsure{\eta|y}', r'\eta'),
 (r'\rotatebox{90}{\(\in\)}', r'\rotatebox{-90}{\(\in\)}'),
 (r'\deleted{\unsure{=}}', r'\deleted{\unsure{=|\downarrow}}'),
 (r'\(I\) \unsure{ens} ordonné', r'\(I\) ens ordonné'),
 (r'\unsure{famille|échelle} d\'ens \unsure{ordonnés}', r'famille d\'ens ordonnés'),
 (r'\unsure{k_n|\kappa_n|\tau_n}', r'\unsure{k_n|\kappa_n|K_n}'),
 (r'l\'ens \(\unsure{K}\)', r'l\'ens \(K\)'),
 (r'\unsure{\mathscr L|\Phi|L}_{n\',n}', r'\unsure{\Phi|\mathscr L|L}_{n\',n}'),
 (r'\mathscr L_{\unsure{n\'}}', r'\Phi_{n\'}'),
 (r'\unsure{Considérons}', r'Considérons'),
 (r'\& F_2\arrow', r'\& \mathbb F_2\arrow'),
 (r'F_{\unsure{*|x}}', r'F_*'),
 (r'\text{\unsure{ens} des \unsure{classes} d\'\unsure{hom.topie|homotopie} des}', r'\text{ens des classes d\'hom.topie. des}'),
 (r'\text{\unsure{lacets} en }', r'\text{lacets en }'),
 (r'\draw (.67,-.52)--(1.84,-.29);', r'\draw (.67,-.59)--(.67,-.52)--(1.84,-.29);'),
]
# Apostrophes in the raw source literals above are escaped for Python only.
replacements = [(a.replace("\\'", "'"), b.replace("\\'", "'")) for a,b in replacements]
for old,new in replacements:
    if old not in c:
        raise ValueError('Replacement target absent: '+old)
    c = c.replace(old,new)

# Mark the uncertain recurring map label once. Its second occurrence was inspected
# independently, with the same retained k/kappa/case alternatives.
target = r'\unsure{k_n|\kappa_n|K_n}'
first = c.index(target)
tail = c[first+len(target):].replace(target, 'k_n')
c = c[:first+len(target)]+tail

# Actual handwriting on the reused typed sheet, after the fully transcribed strip.
needle = '\\[\n\\widetilde{\\mathbb D}'
c = c.replace(needle, '\\handwritten{\n'+needle, 1)
c = c.replace('% archive sheet number: 5', '}% end handwriting\n% archive sheet number: 5')

# Small detached strokes are nonlinguistic ink, not word reconstructions.
needle = '\\[\n\\widetilde D_{n\'}\\longrightarrow\\widetilde D_n\n\\]'
marks = r'''% Two isolated short marks, at full-image (557,522) and (879,677).
\figure{\begin{tikzpicture}[line width=.5pt,line cap=round]
\draw (0,.9)--(.15,.9);
\draw (2,0)--(2.27,-.015);
\fill (1.99,.075) circle[radius=.012];
\end{tikzpicture}}

'''
c = c.replace(needle, marks+needle, 1)

# C's loop diagram is retained: source has an open gap at the left around x;
# no independent point is supplied there. H's filled point is not copied.
c = c.replace('\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,column sep=1em]',
 '% Loop: the two ends are separated at the left beside x; no separate vertex dot.\n\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,column sep=1em]')

(out/'reading.tex').write_text(c)
print('Wrote reading.tex')
