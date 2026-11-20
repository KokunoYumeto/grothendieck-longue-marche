from pathlib import Path

root=Path('/workspace/scratch/2b715fe259c4')
source=root/'source/SP35_CW_156-7_witnesses/codex/H156-01/pages/H156-01_156-7_scan007.tex'
s=source.read_text()
s=s.replace(r'\unsure{\Phi|\varphi}',r'\Phi')
s=s.replace(r'\unsure{élément}',r'élément')
s=s.replace(r'\unsure{termes|terme}',r'termes')
s=s.replace(r'\unsure{défini}',r'\unsure{dfn|défini}')
s=s.replace(r'\unsure{est|ent}',r'est')
s=s.replace(r'\unsure{i.e.}',r'i.e.')
s=s.replace(r'\unsure{posons|posant}',r'posons')
s=s.replace(r'\mathrm{At}_{M}\,1$ à $\mathrm{At}_{M}\,3',r'\mathrm{At}_{M}\,1$ ; $\mathrm{At}_{M}\,3')
s=s.replace(r'\unsure{1|0}',r'1')
s=s.replace(r'\unsure{page|p.}',r'page')
s=s.replace(r'\unsure{\mathrel{\tikz[x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.35,.42) and (1.38,.23) .. (1.28,.2);}}|\Longrightarrow}',r'\mathrel{\tikz[x=.5em,y=.28em]{\draw (0,.08)--(1.2,.08) (0,.42)--(1.2,.42) .. controls (1.35,.42) and (1.38,.23) .. (1.28,.2);}}')
s=s.replace(r"Y$ et $X'\leq X,\ Y'\leq Y$",r"Y$ et $\unsure{X'|Y'}\leq X,\ Y'\leq Y$")
s=s.replace(r'\unsure{formées}',r'formées')
s=s.replace('un choix de structure de plus','un choix de structure en plus')
s=s.replace(r'\unsure{GF|GE}',r'GF')

# Preserve the two interlinear additions and their curved insertion/arrow strokes.
start=s.index('\\[\n\\begin{aligned}\n\\widetilde{\\mathscr F}_{\\mathrm{tf}}')
end=s.index('\\]',start)+2
finite=r'''\diagram{\begin{tikzpicture}[every node/.style={inner sep=0pt}]
\node[anchor=base west] (main) at (0,0) {$\widetilde{\mathscr F}_{\mathrm{tf}}=\text{ensemble des parties fermées }$};
\node[anchor=base west,xshift=.25em] (tail) at (main.base east) {$\text{de }M,\leq$};
\node[anchor=base west,xshift=-.35em,yshift=2.9ex] (addition) at (tail.base west) {$\inserted{\Phi\ \text{de t.f.}}$};
\draw ([xshift=-.35em,yshift=-.35ex]tail.base west) .. controls ([xshift=-.45em,yshift=1.5ex]tail.base west) and ([xshift=.7em,yshift=-1.3ex]addition.base west) .. ([xshift=-.2em,yshift=-.8ex]addition.base east) .. controls ([xshift=.4em,yshift=-.5ex]addition.base east) and ([xshift=.35em,yshift=.7ex]addition.base east) .. ([xshift=.2em,yshift=.8ex]addition.base east);
\node[anchor=base west] (old) at (1em,-4.6ex) {$\deleted{\text{formées \unsure{t.q.}}}$};
\node[anchor=base west,yshift=1.4ex] at (old.base west) {$\inserted{\text{telles que :}}$};
\node[anchor=base west,xshift=.8em] (condition) at (old.base east) {$X,Y\in\Phi$};
\node[anchor=base west,xshift=.2em] at (condition.base east) {$\mathrel{\tikz[baseline=-.4ex,x=.6em,y=.45em]{\draw (0,.8)..controls(.2,.05)and(.7,.05)..(1.15,.05)--(2.45,.05); \draw (1.05,-.18)--(2.45,-.18); \draw (2.1,.42)--(2.45,-.065)--(2.1,-.3);}}\ X\mathrel{\tikz[baseline=-.4ex,x=.65em,y=.65em]{\draw (0,1.1)--(1,.5)--(0,-.1) (1,1.1)--(0,.5)--(1,-.1);}}Y.$};
\end{tikzpicture}}'''
s=s[:start]+finite+s[end:]
s=s.replace('\\margin{J\'ai exprimé', '% Upper-left marginal annotation.\n\\reversemarginpar\n\\margin{J\'ai exprimé',1)
s=s.replace('% slanted','% Slanted left margin')
s+='\n\\normalmarginpar\n'
(Path(__file__).parent/'scan007.tex').write_text(s)
print('Saved complete scan007.tex:',len(s),'characters')
