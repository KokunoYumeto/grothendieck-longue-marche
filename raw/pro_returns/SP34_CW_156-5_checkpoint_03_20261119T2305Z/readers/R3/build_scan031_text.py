from pathlib import Path
P=Path('/workspace/scratch/4770596940a0')
s=(P/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan031.tex').read_text()
changes={r"${\unsure{F|\mathcal F}}'$":r"$F'$",r'\deleted{\unsure{B}} $x\in B$':r'\deleted{$\unsure{B}\ni$} $x\in B$',r"c'est le plus petit":r"c'est lui plus petit",r'\deleted{\unsure{raffine}}':r'\deleted{raffine}',r'\unsure{seult}':'seult',r'\deleted{Soit}':r'\deleted{$\forall$}'}
for old,new in changes.items():
 assert old in s,old
 s=s.replace(old,new)
# Two small two-stroke relations retain a visual alternative rather than a silent emendation.
s=s.replace('|F\'|=|F|\n\\]','|F\'|\\unsure{=|\\geq}|F|\n\\]')
s=s.replace(r"Comme $|F'|=|F|$",r"Comme $|F'|\unsure{=|\geq}|F|$")
a=s.index('% @ lower part, cancelled attempt');b=s.index('% @ lower part, restated first condition',a)
draft=r'''% @ lower part, cancelled attempt: interlinear family, original sentence,
% left insertion and lower cancellation enclosure reproduced together
\figure{\begin{tikzpicture}[font=\small]
\node[anchor=north west,inner sep=0pt,text width=10.2cm] (family) at (3.0,0.65) {\deleted{\inserted{l'ens $F^A$ des $B\in F$ tels que $A\subset B$}}};
\node[anchor=north west,inner sep=0pt,text width=13.2cm] (attempt) at (0,0) {\deleted{1$^\circ$) \deleted{$\forall$} $A\in F'$, \unsure{est contenu dans} un plus petit}};
\node[anchor=north west,inner sep=0pt,text width=13.2cm] (resumption) at (0,-0.85) {\deleted{\unsure{élémt|élément|élt} de $F$. C'est évident si $A\in F$ c'est évident. Si}};
\node[anchor=north west,inner sep=0pt,text width=3.7cm] (addition) at (-1.1,-0.42) {\deleted{\inserted{\unsure{a un plus petit}}}};
\draw ([xshift=3pt]addition.south west) .. controls (-0.45,-0.72) and (-0.15,-0.6) .. (resumption.north west);
\node[anchor=north west,inner sep=0pt,text width=8cm] (abandoned) at (0,-1.5) {\deleted{\unsure{str.} de de $F'$ raffine $F$. Si}};
\draw ([xshift=-2pt,yshift=2pt]resumption.north west)
 .. controls (-0.15,-0.85) and (-0.10,-1.05) .. ([xshift=-2pt]resumption.south west)
 -- ([xshift=-2pt]abandoned.south west)
 -- ([xshift=2pt]abandoned.south east)
 -- ([xshift=2pt,yshift=3pt]abandoned.north east);
\end{tikzpicture}}

'''
s=s[:a]+draft+s[b:]
s += r'''
% @ far right edge, beside the final replacement: two unlabelled curved pen strokes
\margin{\figure{\begin{tikzpicture}[x=1ex,y=1ex]
\draw (0,0.45) .. controls (0.25,0.95) and (0.9,1.1) .. (1,0.65)
 .. controls (0.82,0.15) and (0.30,0.12) .. (0.08,0.05);
\draw (0.25,0.45) .. controls (0.5,0.72) and (0.45,0.93) .. (0.7,0.98);
\end{tikzpicture}}}
'''
(P/'out/readers/R3/scan031.tex').write_text(s)
(P/'out/readers/R3/scan031_working_notes.txt').write_text('Full proposed scan031.tex saved; detailed JSON in progress. Read whole/a/b and all29 documented crops. Proposed F plain, canceled B-ni fragment, c’est lui, two canceled forall symbols, interlinear family in deleted draft, raffine/seult resolved, two small support equalities marked =|geq. C et before l’ens not an independent word; lower est contenu dans remains uncertain. Right-edge unlabeled hook reproduced as TikZ. No later-page images or transcriptions opened.\n')
print('Saved proposed scan031.tex, with two TikZ drawings.')
